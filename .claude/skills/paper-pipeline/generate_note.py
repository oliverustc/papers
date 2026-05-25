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
TIMEOUT      = 120  # 秒

NOTE_PROMPT = """\
你是一位密码学领域的研究助手，擅长深度阅读和分析学术论文。
请根据以下论文全文，按照指定格式输出详尽的结构化笔记。

要求：
1. 语言：中文
2. 深入挖掘论文的核心逻辑链条，不要只停留在表面描述
3. 对公式、协议步骤、算法要给出实质内容，不要用"本文提出了某某方法"这类空话代替
4. 强关联论文须从正文引用中识别，不要凭空捏造

---

【论文全文】
{paper_content}

---

请严格按以下格式输出笔记，不要输出格式以外的任何内容：

### 背景与动机
<!-- 该问题为何重要？现有方案在效率/安全性/功能性上存在哪些具体缺陷？本文试图填补什么空白？-->
（6-10句，说清楚问题的来龙去脉和现有方案的具体瓶颈）

### 相关工作
<!-- 按技术路线分类列举代表性工作，说明各自的核心思路和局限，再点明本文与它们的本质区别-->
（8-15句，可用列表；区别要落到具体技术点，不要只写"本文更好"）

### 核心技术与方案
<!-- 详细描述本文提出的构造/协议/算法：
     - 整体框架和主要模块
     - 关键步骤（含必要的数学表达，如承诺方案、多项式编码、证明系统构造等）
     - 核心洞察：为什么这样设计能解决问题？正确性/安全性的直觉论证
     - 若有创新的数学工具（如新的多项式恒等式、向量内积论证等），须解释其含义 -->
（15-25句，可分小节；对重要公式或协议步骤须给出实质描述，不得省略）

### 核心公式与流程
<!-- 从论文中提取最核心的 3-6 个公式、算法步骤或协议流程：
     - 每条给出原始数学表达式（LaTeX 格式）或逐步协议描述
     - 简要说明该公式/步骤的作用和意义
     示例格式：
     **[公式/步骤名]**
     $$公式或协议步骤$$
     > 作用：……-->
（必须给出实质内容，不得以"详见论文"代替）

### 实验结果
<!-- 实验设置（硬件、数据集、对比基线）；核心性能数据（证明大小、验证时间、证明时间等具体数值）；与 baseline 相比的提升幅度；适用规模或参数范围-->
（6-10句，数据要具体，有数字有对比）

### 局限性与开放问题
<!-- 本文明确指出或隐含的局限；未来值得研究的方向-->
（3-5句）

### 强关联论文
<!-- 从正文引用中识别与本文技术最相关的论文（被本文直接构建、改进或对比的工作），每条给出：
     作者关键词 + 标题 + 发表年份（从引用文献中提取），并拼接 Google Scholar 搜索链接。
     链接格式：https://scholar.google.com/scholar?q=URL编码后的论文标题
     示例：
     - [Groth16] Groth, "On the Size of Pairing-Based Non-interactive Arguments", EUROCRYPT 2016
       🔗 https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-interactive+Arguments
     只列与本文技术路线直接相关的论文，不超过 10 篇，不得捏造未在正文出现的引用 -->
（每篇一行，含链接）\
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
        "curl", "-s", "-m", str(TIMEOUT),
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


def truncate_paper(content: str, max_chars: int = 60000) -> str:
    """超长论文截断：保留前 2/3 + 后 1/3，避免只看摘要。"""
    if len(content) <= max_chars:
        return content
    front = int(max_chars * 2 / 3)
    back  = max_chars - front
    return (
        content[:front]
        + "\n\n...[内容过长，已截断中间部分]...\n\n"
        + content[-back:]
    )


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

    paper_content = truncate_paper(mineru_md.read_text(encoding="utf-8"))
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
    parser = argparse.ArgumentParser(description="调用 LLM 生成论文结构化笔记")
    parser.add_argument("key", help="citation key，例如 bunz2018bulletproofs")
    parser.add_argument("--dry-run", action="store_true", help="只打印结果，不写文件")
    args = parser.parse_args()

    ok = generate_note(args.key, dry_run=args.dry_run)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
