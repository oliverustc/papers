#!/usr/bin/env python3
"""
pipeline_status.py — 生成全流水线状态看板 pipeline-status.md

用法:
    python3 .claude/skills/paper-pipeline/pipeline_status.py

每篇论文检查三步状态：
    PDF    ✅ storage/ 中有 PDF  |  📥 Zotero 有但未同步  |  ⬜ 无
    MinerU ✅ mineru-output 已生成  |  ⬜ 无
    笔记   ✅ ## 笔记 下有结构化内容  |  ⬜ 无
"""

import re
import sqlite3
from datetime import date
from pathlib import Path
from urllib.parse import quote_plus

import yaml

import sys
sys.path.insert(0, str(Path(__file__).parent))
from env import ZOTERO_DB, ZOTERO_STORE, REPO_ROOT

REFERENCES  = REPO_ROOT / "references"
STORAGE     = REPO_ROOT / "storage"
OUTPUT_FILE = Path(__file__).parent / "pipeline-status.md"

# ── 工具函数 ──────────────────────────────────────────────────────────────────

def normalize_title(t: str) -> str:
    return re.sub(r"[^a-z0-9]", "", t.lower())


def parse_frontmatter(md_path: Path) -> dict:
    text = md_path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}


def venue_str(fm: dict) -> str:
    ptype = fm.get("论文类型", "")
    year  = str(fm.get("发表年份", ""))
    if ptype == "conference":
        return f"{fm.get('会议简称', '')} {year}"
    elif ptype == "journal":
        return f"{fm.get('期刊简称', '')} {year}"
    elif ptype == "preprint":
        return f"{fm.get('预印本简称', '')} {year}"
    return year


def scholar_url(title: str) -> str:
    return f"https://scholar.google.com/scholar?q={quote_plus(title)}"


def ref_rel(md_path: Path) -> str:
    return str(md_path.relative_to(REPO_ROOT))


# ── 三步状态检测 ──────────────────────────────────────────────────────────────

def check_pdf(key: str, title: str) -> str:
    """✅ 本地有 | 📥 Zotero有 | ⬜ 无"""
    if list(STORAGE.rglob(f"{key}/{key}.pdf")):
        return "✅"
    if ZOTERO_DB.exists():
        norm = normalize_title(title)
        try:
            conn = sqlite3.connect(str(ZOTERO_DB))
            cur = conn.cursor()
            cur.execute("""
                SELECT i.key, ia.path, idv.value
                FROM itemAttachments ia
                JOIN items i   ON ia.itemID = i.itemID
                JOIN items pi  ON ia.parentItemID = pi.itemID
                JOIN itemData id ON id.itemID = pi.itemID
                JOIN fields f  ON id.fieldID = f.fieldID
                JOIN itemDataValues idv ON id.valueID = idv.valueID
                WHERE ia.contentType = 'application/pdf'
                AND ia.path IS NOT NULL AND f.fieldName = 'title'
            """)
            for attach_key, raw_path, db_title in cur.fetchall():
                if normalize_title(db_title) != norm:
                    continue
                if raw_path.startswith("storage:"):
                    pdf = ZOTERO_STORE / attach_key / raw_path[len("storage:"):]
                else:
                    m = re.match(r"^([A-Za-z]):\\(.*)", raw_path)
                    pdf = Path(f"/mnt/{m.group(1).lower()}/{m.group(2).replace(chr(92),'/')}") if m else Path(raw_path)
                if pdf.exists():
                    return "📥"
            conn.close()
        except Exception:
            pass
    return "⬜"


def check_mineru(key: str) -> str:
    """✅ 已转换 | ⬜ 无"""
    return "✅" if list(STORAGE.rglob(f"{key}/mineru-output/{key}.md")) else "⬜"


def check_note(key: str) -> str:
    """✅ 有结构化笔记 | ⬜ 无"""
    matches = [p for p in REFERENCES.rglob(f"{key}.md") if p.name != "index.md"]
    if not matches:
        return "⬜"
    text = matches[0].read_text(encoding="utf-8")
    note_start = text.find("## 笔记")
    if note_start == -1:
        return "⬜"
    after = text[note_start:]
    return "✅" if "### 背景与动机" in after else "⬜"


# ── 主逻辑 ────────────────────────────────────────────────────────────────────

def build_status() -> None:
    papers = []
    for md_path in sorted(REFERENCES.rglob("*.md")):
        if md_path.name == "index.md":
            continue
        fm = parse_frontmatter(md_path)
        if not fm.get("论文类型") or not fm.get("title"):
            continue
        papers.append((md_path.stem, fm.get("title", ""), fm, md_path))

    total = len(papers)
    print(f"检查 {total} 篇论文（需查询 Zotero，稍慢）...")

    rows = []
    for i, (key, title, fm, md_path) in enumerate(papers, 1):
        print(f"  [{i}/{total}] {key}", end="\r", flush=True)
        pdf    = check_pdf(key, title)
        mineru = check_mineru(key)
        note   = check_note(key)
        rows.append((key, title, fm, md_path, pdf, mineru, note))

    print(f"\n扫描完成")

    # 统计
    n_all  = sum(1 for r in rows if r[4]=="✅" and r[5]=="✅" and r[6]=="✅")
    n_pdf  = sum(1 for r in rows if r[4]=="✅")
    n_mu   = sum(1 for r in rows if r[5]=="✅")
    n_note = sum(1 for r in rows if r[6]=="✅")

    # 分组（按流水线完成度降序）
    def priority(r):
        pdf, mu, note = r[4], r[5], r[6]
        if pdf=="✅" and mu=="✅" and note=="✅": return 0   # 全完成
        if pdf=="✅" and mu=="✅" and note=="⬜": return 1   # 待生成笔记
        if pdf=="✅" and mu=="⬜":                return 2   # 待 MinerU
        if pdf=="📥":                             return 3   # Zotero有，待同步
        return 4                                             # 待添加 PDF

    rows.sort(key=lambda r: (priority(r), r[1]))

    groups = {0: [], 1: [], 2: [], 3: [], 4: []}
    for r in rows:
        groups[priority(r)].append(r)

    # ── 写文件 ────────────────────────────────────────────────────────────────
    lines = [
        "# 论文流水线状态看板\n\n",
        f"> 最后更新：{date.today()}  |  "
        f"总计 **{total}** 篇  |  "
        f"PDF ✅ **{n_pdf}**  |  "
        f"MinerU ✅ **{n_mu}**  |  "
        f"笔记 ✅ **{n_note}**  |  "
        f"全部完成 **{n_all}**\n\n",

        "## 状态说明\n\n",
        "| 图标 | 含义 |\n|:---:|---|\n",
        "| ✅ | 已完成 |\n",
        "| 📥 | Zotero 有 PDF，运行 `sync_pdf.py --all` 即可同步 |\n",
        "| ⬜ | 待处理 |\n\n",
        "---\n\n",
    ]

    def table_section(title_str, group_rows, show_scholar=False):
        if not group_rows:
            return []
        out = [f"## {title_str}  ({len(group_rows)} 篇)\n\n"]
        out.append("| Citation Key | 标题 | 来源 | PDF | MinerU | 笔记 |")
        if show_scholar:
            out[-1] += " Google Scholar |"
        out.append("\n")
        out.append("|:---|:---|:---:|:---:|:---:|:---:|")
        if show_scholar:
            out[-1] += ":---:|"
        out.append("\n")
        for key, title, fm, md_path, pdf, mineru, note in group_rows:
            short = title[:55] + "…" if len(title) > 55 else title
            row = (
                f"| `{key}` "
                f"| [{short}]({ref_rel(md_path)}) "
                f"| {venue_str(fm)} "
                f"| {pdf} | {mineru} | {note} |"
            )
            if show_scholar:
                row += f" [搜索]({scholar_url(title)}) |"
            out.append(row + "\n")
        out.append("\n")
        return out

    lines += table_section("✅ 全部完成", groups[0])
    lines += table_section("📝 待生成笔记（PDF + MinerU 就绪）", groups[1])
    lines += table_section("⚙️ 待 MinerU 转换（有 PDF）", groups[2])
    lines += table_section("📥 Zotero 已有（待同步）", groups[3], show_scholar=False)
    lines += table_section("⬜ 待添加 PDF", groups[4], show_scholar=True)

    OUTPUT_FILE.write_text("".join(lines), encoding="utf-8")
    print(f"已写入：{OUTPUT_FILE.relative_to(REPO_ROOT)}")
    print(f"\n汇总：全完成 {n_all} | 待生成笔记 {len(groups[1])} | 待MinerU {len(groups[2])} | Zotero待同步 {len(groups[3])} | 待添PDF {len(groups[4])}")


if __name__ == "__main__":
    build_status()
