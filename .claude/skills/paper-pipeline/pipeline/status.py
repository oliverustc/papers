"""
status.py — 生成全流水线状态看板 pipeline-status.md。
"""

import re
import sqlite3
from datetime import date
from pathlib import Path
from urllib.parse import quote, quote_plus

from pipeline.common import parse_frontmatter, normalize_title, winpath_to_wsl
from pipeline.env import REFERENCES, STORAGE, ZOTERO_DB, ZOTERO_STORE

OUTPUT_FILE = Path(__file__).parent.parent / "pipeline-status.md"


def _check_pdf(key: str, title: str) -> str:
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
                    pdf = winpath_to_wsl(raw_path)
                if pdf.exists():
                    return "📥"
            conn.close()
        except Exception:
            pass
    return "⬜"


def _check_mineru(key: str) -> str:
    return "✅" if list(STORAGE.rglob(f"{key}/mineru-output/{key}.md")) else "⬜"


def _check_note(key: str) -> str:
    matches = [p for p in REFERENCES.rglob(f"{key}.md") if p.name != "index.md"]
    if not matches:
        return "⬜"
    text = matches[0].read_text(encoding="utf-8")
    idx = text.find("## 笔记")
    return "✅" if idx != -1 and "### 背景与动机" in text[idx:] else "⬜"


def _venue(fm: dict) -> str:
    ptype = fm.get("论文类型", "")
    year  = str(fm.get("发表年份", ""))
    if ptype == "conference": return f"{fm.get('会议简称', '')} {year}"
    if ptype == "journal":    return f"{fm.get('期刊简称', '')} {year}"
    if ptype == "preprint":   return f"{fm.get('预印本简称', '')} {year}"
    return year


def _ref_rel(md_path: Path) -> str:
    return quote(str(md_path.relative_to(REFERENCES.parent)), safe="/")


def run(args) -> None:
    papers = []
    for md in sorted(REFERENCES.rglob("*.md")):
        if md.name == "index.md":
            continue
        fm, _, _ = parse_frontmatter(md)
        if fm.get("论文类型") and fm.get("title"):
            papers.append((md.stem, fm.get("title", ""), fm, md))

    total = len(papers)
    print(f"检查 {total} 篇论文...")

    rows = []
    for i, (key, title, fm, md) in enumerate(papers, 1):
        print(f"  [{i}/{total}] {key}", end="\r", flush=True)
        rows.append((key, title, fm, md, _check_pdf(key, title), _check_mineru(key), _check_note(key)))
    print("\n扫描完成")

    n_pdf  = sum(1 for r in rows if r[4] == "✅")
    n_mu   = sum(1 for r in rows if r[5] == "✅")
    n_note = sum(1 for r in rows if r[6] == "✅")
    n_all  = sum(1 for r in rows if r[4] == r[5] == r[6] == "✅")

    def _priority(r):
        p, m, n = r[4], r[5], r[6]
        if p == m == n == "✅": return 0
        if p == m == "✅":      return 1
        if p == "✅":           return 2
        if p == "📥":           return 3
        return 4

    rows.sort(key=lambda r: (_priority(r), r[1]))
    groups = {i: [] for i in range(5)}
    for r in rows:
        groups[_priority(r)].append(r)

    def _section(title_str, group_rows, show_scholar=False):
        if not group_rows:
            return []
        out = [f"## {title_str}  ({len(group_rows)} 篇)\n\n"]
        header = "| Citation Key | 标题 | 来源 | PDF | MinerU | 笔记 |"
        sep    = "|:---|:---|:---:|:---:|:---:|:---:|"
        if show_scholar:
            header += " Google Scholar |"
            sep    += ":---:|"
        out += [header + "\n", sep + "\n"]
        for key, title, fm, md, pdf, mu, note in group_rows:
            short = title[:55] + "…" if len(title) > 55 else title
            row = f"| `{key}` | [{short}]({_ref_rel(md)}) | {_venue(fm)} | {pdf} | {mu} | {note} |"
            if show_scholar:
                row += f" [搜索](https://scholar.google.com/scholar?q={quote_plus(title)}) |"
            out.append(row + "\n")
        out.append("\n")
        return out

    lines = [
        "# 论文流水线状态看板\n\n",
        f"> 最后更新：{date.today()}  |  总计 **{total}** 篇  |  "
        f"PDF ✅ **{n_pdf}**  |  MinerU ✅ **{n_mu}**  |  "
        f"笔记 ✅ **{n_note}**  |  全部完成 **{n_all}**\n\n",
        "## 状态说明\n\n| 图标 | 含义 |\n|:---:|---|\n",
        "| ✅ | 已完成 |\n",
        "| 📥 | Zotero 有 PDF，运行 `pp fetch --all` 或 `pp sync --all` 同步 |\n",
        "| ⬜ | 待处理 |\n\n---\n\n",
    ]
    lines += _section("✅ 全部完成", groups[0])
    lines += _section("📝 待生成笔记（PDF + MinerU 就绪）", groups[1])
    lines += _section("⚙️ 待 MinerU 转换（有 PDF）", groups[2])
    lines += _section("📥 Zotero 已有（待同步）", groups[3])
    lines += _section("⬜ 待添加 PDF", groups[4], show_scholar=True)

    OUTPUT_FILE.write_text("".join(lines), encoding="utf-8")
    from pipeline.env import REPO_ROOT
    print(f"已写入：{OUTPUT_FILE.relative_to(REPO_ROOT)}")
    print(f"\n汇总：全完成 {n_all} | 待笔记 {len(groups[1])} | 待MinerU {len(groups[2])} | Zotero待同步 {len(groups[3])} | 待PDF {len(groups[4])}")
