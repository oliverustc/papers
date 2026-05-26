#!/usr/bin/env -S python3 -u
"""
generate_note.py — 读取 mineru-output MD，调用 LLM API 生成结构化笔记，
                   写入 references/ 对应文件的 ## 笔记 字段（完全替换）

用法:
    python3 .claude/skills/paper-pipeline/generate_note.py <citation_key>
    python3 .claude/skills/paper-pipeline/generate_note.py --dry-run <citation_key>
"""

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from env import LLM_URL, LLM_TOKEN, LLM_MODEL, REPO_ROOT

# ── 配置 ──────────────────────────────────────────────────────────────────────
REFERENCES   = REPO_ROOT / "references"
STORAGE      = REPO_ROOT / "storage"
LLM_BASE_URL = LLM_URL
TIMEOUT      = 300  # 秒

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


# ── LLM 调用 ──────────────────────────────────────────────────────────────────

def call_llm(paper_content: str) -> str | None:
    payload = json.dumps({
        "model": LLM_MODEL,
        "messages": [
            {"role": "user", "content": NOTE_PROMPT.format(paper_content=paper_content)}
        ],
    })
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
        f.write(payload)
        payload_path = f.name
    cmd = [
        "curl", "-s", "-m", str(TIMEOUT), "--noproxy", "*",
        "-X", "POST", LLM_BASE_URL,
        "-H", "Content-Type: application/json",
        "-H", f"Authorization: Bearer {LLM_TOKEN}",
        "-d", f"@{payload_path}",
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=TIMEOUT + 10)
    except subprocess.TimeoutExpired:
        print("  [LLM] 请求超时", file=sys.stderr)
        return None
    finally:
        Path(payload_path).unlink(missing_ok=True)

    if result.returncode != 0:
        print(f"  [LLM] curl 失败: {result.stderr[:200]}", file=sys.stderr)
        return None

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        print(f"  [LLM] 响应非 JSON: {result.stdout[:300]}", file=sys.stderr)
        return None

    if "error" in data:
        print(f"  [LLM] API 错误: {data['error']}", file=sys.stderr)
        return None

    try:
        return data["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError) as e:
        print(f"  [LLM] 解析响应失败: {e}", file=sys.stderr)
        return None


# ── 工具函数 ──────────────────────────────────────────────────────────────────

def find_mineru_md(key: str) -> Path | None:
    matches = list(STORAGE.rglob(f"{key}/mineru-output/{key}.md"))
    return matches[0] if matches else None


def find_reference_md(key: str) -> Path | None:
    matches = list(REFERENCES.rglob(f"{key}.md"))
    matches = [p for p in matches if p.name != "index.md"]
    return matches[0] if matches else None


def has_note(ref_md: Path) -> bool:
    """检查 ## 笔记 下是否已有结构化内容（含 ### 背景与动机）。"""
    text = ref_md.read_text(encoding="utf-8")
    idx = text.find("## 笔记")
    return idx != -1 and "### 背景与动机" in text[idx:]


def all_pending_keys() -> list[str]:
    """返回所有有 mineru-output 但笔记尚未生成的 citation key。"""
    keys = []
    for mineru_md in STORAGE.rglob("*/mineru-output/*.md"):
        key = mineru_md.stem
        ref_md = find_reference_md(key)
        if ref_md is not None and not has_note(ref_md):
            keys.append(key)
    return sorted(keys)


def replace_notes_section(md_text: str, new_notes: str) -> str:
    """将 ## 笔记 到下一个 ## 标题（或文末）之间的内容替换为 new_notes。"""
    note_header = "## 笔记"
    note_start = md_text.find(note_header)
    if note_start == -1:
        return md_text.rstrip() + f"\n\n{note_header}\n\n{new_notes}\n"

    after_header = note_start + len(note_header)
    next_section = re.search(r"\n## ", md_text[after_header:])
    if next_section:
        note_end = after_header + next_section.start()
    else:
        note_end = len(md_text)

    return md_text[:after_header] + "\n\n" + new_notes + "\n\n" + md_text[note_end:]



# ── 核心逻辑 ──────────────────────────────────────────────────────────────────

def generate_note(key: str, dry_run: bool = False) -> bool:
    mineru_md = find_mineru_md(key)
    if mineru_md is None:
        print(f"[{key}] 未找到 mineru-output，请先运行 convert_pdf.py")
        return False

    ref_md = find_reference_md(key)
    if ref_md is None:
        print(f"[{key}] 未找到对应的 references md 文件")
        return False

    paper_content = mineru_md.read_text(encoding="utf-8")
    print(f"[{key}] 论文全文：{len(paper_content)} 字符，调用 {LLM_MODEL}...")

    notes = call_llm(paper_content)
    if notes is None:
        print(f"[{key}] ✗ LLM 调用失败")
        return False

    if dry_run:
        print(f"\n{'='*60}")
        print(f"[{key}] [dry-run] 生成的笔记内容：")
        print(f"{'='*60}\n")
        print(notes)
        print(f"\n{'='*60}")
        print(f"将写入：{ref_md.relative_to(REPO_ROOT)}")
        return True

    original = ref_md.read_text(encoding="utf-8")
    updated  = replace_notes_section(original, notes)
    ref_md.write_text(updated, encoding="utf-8")
    print(f"[{key}] ✓ 笔记已写入：{ref_md.relative_to(REPO_ROOT)}")
    return True


# ── 主程序 ───────────────────────────────────────────────────────────────────

def main():
    import signal
    import time
    from datetime import datetime, timedelta

    parser = argparse.ArgumentParser(description="调用 LLM 生成论文结构化笔记")
    parser.add_argument("key", nargs="?", help="citation key，例如 bunz2018bulletproofs")
    parser.add_argument("--all",      action="store_true", help="处理所有有 mineru-output 但缺笔记的论文")
    parser.add_argument("--dry-run",  action="store_true", help="只打印结果，不写文件")
    parser.add_argument("--interval", type=int, default=30,
                        help="批量模式下两次 API 调用的间隔秒数（默认 30）")
    args = parser.parse_args()

    if args.all:
        keys = all_pending_keys()
        if not keys:
            print("没有待生成笔记的论文（所有有 mineru-output 的论文均已有笔记）")
            return

        interval = 0 if args.dry_run else args.interval
        total = len(keys)
        print(f"待生成笔记：{total} 篇，间隔 {interval}s，预计总耗时 {timedelta(seconds=interval * (total - 1))}\n")

        interrupted = False
        def _handle_sigint(*_):
            nonlocal interrupted
            print("\n\n[中断] 收到 Ctrl-C，完成当前任务后退出...")
            interrupted = True
        signal.signal(signal.SIGINT, _handle_sigint)

        ok = fail = 0
        for i, key in enumerate(keys, 1):
            print(f"[{i}/{total}]", end=" ")
            if generate_note(key, dry_run=args.dry_run):
                ok += 1
            else:
                fail += 1
            if interrupted:
                break
            if not args.dry_run and i < total:
                eta = datetime.now() + timedelta(seconds=interval * (total - i))
                print(f"  → 等待 {interval}s，预计完成 {eta.strftime('%H:%M:%S')}（剩余 {total - i} 篇）")
                time.sleep(interval)

        status = "中断" if interrupted else "完成"
        print(f"\n{status}：成功 {ok}，失败 {fail}，剩余 {total - ok - fail} 篇未处理")

    elif args.key:
        ok = generate_note(args.key, dry_run=args.dry_run)
        sys.exit(0 if ok else 1)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
