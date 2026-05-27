"""
note.py — 读取 mineru-output MD，调用 LLM 生成结构化笔记。
"""

import json
import re
import signal
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timedelta
from pathlib import Path

from pipeline.common import parse_frontmatter, find_reference_md
from pipeline.env import LLM_URL, LLM_TOKEN, LLM_MODEL, STORAGE

TIMEOUT = 600

NOTE_PROMPT = """\
你是一位密码学领域的研究助手，擅长深度阅读和分析学术论文。
请根据以下论文全文，按照指定格式输出详尽的结构化笔记。

【行文要求】
1. 语言：中文，行文流畅，像论述文章而非条目摘要。
2. 严禁括号插入式表达——信息直接融入句子，引用用编号 [n]，例如"Smith 于 CCS 2020 提出的方案 [5]"。
3. 深入挖掘核心逻辑链，禁止用"本文提出了某某方法"之类的空话代替实质内容。
4. 公式、算法步骤、协议流程须给出实质内容，不得省略或以"详见论文"代替。
5. 引用编号须与原文参考文献列表一致，不得捏造。
6. 各列表条目之间必须有一个空行，否则 Markdown 会将它们渲染成一行。
7. 所有数学内容（变量、表达式、公式、算法步骤中的符号）一律使用 LaTeX 语法：行内用 $…$，独立公式块用 $$…$$，不得用纯文本写数学符号。

---

【论文全文】
{paper_content}

---

请严格按以下格式输出笔记，不要输出格式以外的任何内容：

### 背景与动机
<!-- 该问题为何重要？现有方案存在哪些具体瓶颈？本文试图填补什么空白？
     流畅叙述，引用用 [n] -->
（6-10句）

### 相关工作
<!-- 每条格式（条目之间必须空一行）：

[编号] 作者姓氏等. 论文标题. **期刊/会议缩写 年份** [Google Scholar](https://scholar.google.com/scholar?q=标题URL编码)
> 核心思路：该工作做了什么，一句话。
> 局限与区别：该工作的具体瓶颈，以及本文在哪个技术点上与之不同。

只列与本文技术路线直接相关的工作，不超过 10 条 -->

### 核心技术与方案
<!-- 说明本文的整体框架，若存在多个层次或模块则按层次分小节描述。
     每个模块/层次说明：构造思路、关键步骤（含数学表达）、正确性或安全性的直觉论证。
     若涉及安全性证明，说明所依赖的假设、证明所保证的性质（完备性/可靠性/零知识等）及证明策略。
     给出系统的渐进复杂度（通信量、计算量，区分各参与方）。
     流畅叙述，引用用 [n] -->
（可分小节，15-30句）

### 核心公式与流程
<!-- 提取核心的公式、算法或协议步骤，每条格式：

**[名称]**
$$LaTeX$$
> 作用：……

条目之间空一行 -->

### 实验结果
<!-- 实验设置（硬件/数据集/对比基线）；核心性能数值（须精确，来自论文原文）；
     与 baseline 的对比；适用规模或参数范围。
     流畅叙述，引用用 [n] -->
（6-10句）

### 局限性与开放问题
（3-5句）

### 强关联论文
<!-- 从正文引用中识别被本文直接构建、改进或对比的论文（不超过 10 篇）。
     每条格式（条目之间必须空一行）：

[编号] 作者姓氏等. 论文标题. **期刊/会议缩写 年份** [Google Scholar](https://scholar.google.com/scholar?q=标题URL编码)

编号须与原文一致，不得捏造 -->\
"""


def _do_curl(payload_path: str) -> tuple[int, str, str]:
    cmd = [
        "curl", "-s", "-m", str(TIMEOUT), "--noproxy", "*",
        "-X", "POST", LLM_URL,
        "-H", "Content-Type: application/json",
        "-H", f"Authorization: Bearer {LLM_TOKEN}",
        "-d", f"@{payload_path}",
    ]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=TIMEOUT + 10)
        return r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "timeout"


def _call_llm(paper_content: str) -> str | None:
    payload = json.dumps({
        "model": LLM_MODEL,
        "messages": [{"role": "user", "content": NOTE_PROMPT.format(paper_content=paper_content)}],
    })
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
        f.write(payload)
        payload_path = f.name
    try:
        for attempt in (1, 2):
            rc, stdout, stderr = _do_curl(payload_path)
            if rc != 0:
                print(f"  [LLM] curl 失败 (rc={rc}){': ' + stderr[:100] if stderr else ''}", file=sys.stderr)
                if attempt == 1:
                    print("  [LLM] 60s 后重试...", file=sys.stderr)
                    time.sleep(60)
                    continue
                return None
            try:
                data = json.loads(stdout)
            except json.JSONDecodeError:
                print(f"  [LLM] 响应非 JSON: {stdout[:300]}", file=sys.stderr)
                return None
            err = data.get("error")
            if err:
                print(f"  [LLM] API 错误: {str(err)[:300]}", file=sys.stderr)
                if attempt == 1 and str(err.get("code") if isinstance(err, dict) else "") in ("500", "502", "503"):
                    time.sleep(60)
                    continue
                return None
            try:
                msg = data["choices"][0]["message"]
                return (msg.get("content") or msg.get("reasoning_content") or "").strip() or None
            except (KeyError, IndexError) as e:
                print(f"  [LLM] 解析失败: {e}", file=sys.stderr)
                return None
    finally:
        Path(payload_path).unlink(missing_ok=True)
    return None


def _find_mineru(key: str):
    matches = list(STORAGE.rglob(f"{key}/mineru-output/{key}.md"))
    return matches[0] if matches else None


def _has_note(ref_md) -> bool:
    text = ref_md.read_text(encoding="utf-8")
    idx = text.find("## 笔记")
    return idx != -1 and "### 背景与动机" in text[idx:]


def _replace_notes(md_text: str, new_notes: str) -> str:
    header = "## 笔记"
    start = md_text.find(header)
    if start == -1:
        return md_text.rstrip() + f"\n\n{header}\n\n{new_notes}\n"
    after = start + len(header)
    nxt = re.search(r"\n## ", md_text[after:])
    end = after + nxt.start() if nxt else len(md_text)
    return md_text[:after] + "\n\n" + new_notes + "\n\n" + md_text[end:]


def _all_pending():
    keys = []
    for mineru_md in STORAGE.rglob("*/mineru-output/*.md"):
        key = mineru_md.stem
        ref = find_reference_md(key)
        if ref is not None and not _has_note(ref):
            keys.append(key)
    return sorted(keys)


def _process_one(key: str, dry_run: bool) -> bool:
    mineru = _find_mineru(key)
    if mineru is None:
        print(f"[{key}] 未找到 mineru-output，请先运行 convert")
        return False
    ref = find_reference_md(key)
    if ref is None:
        print(f"[{key}] 未找到 references md")
        return False
    content = mineru.read_text(encoding="utf-8")
    print(f"[{key}] {len(content)} 字符，调用 {LLM_MODEL}...")
    notes = _call_llm(content)
    if notes is None:
        print(f"[{key}] ✗ LLM 调用失败")
        return False
    if dry_run:
        print(f"\n{'='*60}\n[dry-run] 生成内容预览：\n{'='*60}\n")
        print(notes[:1000], "...")
        return True
    updated = _replace_notes(ref.read_text(encoding="utf-8"), notes)
    ref.write_text(updated, encoding="utf-8")
    print(f"[{key}] ✓ 笔记已写入")
    return True


def run(args) -> None:
    if args.key:
        ok = _process_one(args.key, dry_run=args.dry_run)
        sys.exit(0 if ok else 1)

    if args.all:
        keys = _all_pending()
        if not keys:
            print("没有待生成笔记的论文")
            return
        interval = 0 if args.dry_run else args.interval
        total = len(keys)
        print(f"待生成笔记：{total} 篇，间隔 {interval}s，预计 {timedelta(seconds=interval*(total-1))}\n")

        interrupted = False
        def _sigint(*_):
            nonlocal interrupted
            print("\n[中断] 完成当前任务后退出...")
            interrupted = True
        signal.signal(signal.SIGINT, _sigint)

        ok = fail = 0
        for i, key in enumerate(keys, 1):
            print(f"[{i}/{total}]", end=" ")
            try:
                if _process_one(key, dry_run=args.dry_run):
                    ok += 1
                else:
                    fail += 1
            except Exception as e:
                print(f"[{key}] ✗ 未预期错误: {e}", file=sys.stderr)
                fail += 1
            if interrupted:
                break
            if not args.dry_run and i < total:
                eta = datetime.now() + timedelta(seconds=interval * (total - i))
                print(f"  → 等待 {interval}s，预计 {eta.strftime('%H:%M:%S')}（剩余 {total-i} 篇）")
                time.sleep(interval)

        status = "中断" if interrupted else "完成"
        print(f"\n{status}：成功 {ok}，失败 {fail}，剩余 {total-ok-fail} 篇")
        return

    print("请指定 key 或使用 --all")
