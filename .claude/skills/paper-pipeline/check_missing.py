#!/usr/bin/env python3
"""
check_missing.py — 扫描 references/ 中没有 PDF 的论文，生成 missing-pdfs.md

用法:
    python3 .claude/skills/paper-pipeline/check_missing.py          # 生成/更新列表
    python3 .claude/skills/paper-pipeline/check_missing.py --rescan # 重新扫描，更新已获取的条目

状态说明：
    ⬜ 待添加   — Zotero 中没有该 PDF，需手动搜索添加
    📥 Zotero已有 — Zotero 中已有，但尚未同步到 storage/（运行 sync_pdf.py 即可）
    ✅ 已获取   — PDF 已在 storage/ 中，无需处理（重扫时从列表移除）
"""

import re
import sqlite3
import sys
from datetime import date
from pathlib import Path
from urllib.parse import quote_plus

import yaml

import sys
sys.path.insert(0, str(Path(__file__).parent))
from env import ZOTERO_DB, ZOTERO_STORE, REPO_ROOT

REFERENCES  = REPO_ROOT / "references"
STORAGE     = REPO_ROOT / "storage"
OUTPUT_FILE = REPO_ROOT / "missing-pdfs.md"

STATUS_PENDING  = "⬜"   # 待添加
STATUS_INZOTERO = "📥"   # Zotero已有，未同步
STATUS_DONE     = "✅"   # 已获取（有 PDF）


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


def scholar_url(title: str) -> str:
    return f"https://scholar.google.com/scholar?q={quote_plus(title)}"


def has_pdf_in_storage(key: str) -> bool:
    return bool(list(STORAGE.rglob(f"{key}/{key}.pdf")))


def winpath_to_wsl(path_str: str) -> Path:
    import re as _re
    m = _re.match(r"^([A-Za-z]):\\(.*)", path_str)
    if m:
        return Path(f"/mnt/{m.group(1).lower()}/{m.group(2).replace(chr(92), '/')}")
    return Path(path_str)


def is_in_zotero(title: str) -> bool:
    """检查 Zotero 数据库中是否有该标题的 PDF，且文件实际可访问。"""
    if not ZOTERO_DB.exists():
        return False
    norm = normalize_title(title)
    zotero_store = ZOTERO_STORE
    try:
        conn = sqlite3.connect(str(ZOTERO_DB))
        cur = conn.cursor()
        cur.execute("""
            SELECT i.key, ia.path, idv.value
            FROM itemAttachments ia
            JOIN items i        ON ia.itemID = i.itemID
            JOIN items pi       ON ia.parentItemID = pi.itemID
            JOIN itemData id    ON id.itemID = pi.itemID
            JOIN fields f       ON id.fieldID = f.fieldID
            JOIN itemDataValues idv ON id.valueID = idv.valueID
            WHERE ia.contentType = 'application/pdf'
            AND ia.path IS NOT NULL
            AND f.fieldName = 'title'
        """)
        for attach_key, raw_path, db_title in cur.fetchall():
            if normalize_title(db_title) != norm:
                continue
            # 验证文件实际存在
            if raw_path.startswith("storage:"):
                pdf = zotero_store / attach_key / raw_path[len("storage:"):]
            else:
                pdf = winpath_to_wsl(raw_path)
            if pdf.exists():
                return True
        return False
    except Exception:
        return False
    finally:
        conn.close()


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


def ref_rel_path(md_path: Path) -> str:
    return str(md_path.relative_to(REPO_ROOT))


# ── 解析已有 missing-pdfs.md，提取各 key 的当前状态 ──────────────────────────

def load_existing_statuses() -> dict[str, str]:
    """从已有文件中读取各 citation key 对应的状态符号。"""
    if not OUTPUT_FILE.exists():
        return {}
    text = OUTPUT_FILE.read_text(encoding="utf-8")
    statuses = {}
    # 匹配表格行：| 状态符号 | `key` | ...
    for m in re.finditer(r"^\|\s*([⬜📥✅])\s*\|\s*`([^`]+)`", text, re.MULTILINE):
        statuses[m.group(2)] = m.group(1)
    return statuses


# ── 主逻辑 ────────────────────────────────────────────────────────────────────

def build_missing_list(rescan: bool) -> None:
    existing = load_existing_statuses()

    # 收集所有论文
    all_papers = []
    for md_path in sorted(REFERENCES.rglob("*.md")):
        if md_path.name == "index.md":
            continue
        fm = parse_frontmatter(md_path)
        if not fm.get("论文类型"):
            continue
        key   = md_path.stem
        title = fm.get("title", "")
        if not title:
            continue
        all_papers.append((key, title, fm, md_path))

    rows_pending  = []   # 待添加 / Zotero已有
    rows_done     = []   # 已获取（PDF 在 storage/）
    n_total = len(all_papers)

    print(f"扫描 {n_total} 篇论文...")

    for i, (key, title, fm, md_path) in enumerate(all_papers, 1):
        print(f"  [{i}/{n_total}] {key}", end="\r", flush=True)

        if has_pdf_in_storage(key):
            rows_done.append((key, title, fm, md_path))
            continue

        # 没有本地 PDF：检查 Zotero
        prev_status = existing.get(key, "")

        if rescan or not prev_status:
            in_zotero = is_in_zotero(title)
            status = STATUS_INZOTERO if in_zotero else STATUS_PENDING
        else:
            # 保留上次状态，不重查 Zotero（节省时间）
            status = prev_status if prev_status in (STATUS_PENDING, STATUS_INZOTERO) else STATUS_PENDING

        rows_pending.append((status, key, title, fm, md_path))

    print(f"\n完成：{len(rows_done)} 篇已有 PDF，{len(rows_pending)} 篇待处理")

    # 按状态排序：📥 在前（可直接同步），⬜ 在后
    rows_pending.sort(key=lambda r: (0 if r[0] == STATUS_INZOTERO else 1, r[2]))

    n_inzotero = sum(1 for r in rows_pending if r[0] == STATUS_INZOTERO)
    n_pending  = sum(1 for r in rows_pending if r[0] == STATUS_PENDING)

    # ── 生成 Markdown ──────────────────────────────────────────────────────────
    lines = [
        "# 缺失 PDF 列表\n",
        f"> 最后扫描：{date.today()}  |  "
        f"总计 **{n_total}** 篇  |  "
        f"已获取 **{len(rows_done)}**  |  "
        f"📥 Zotero已有（可直接同步）**{n_inzotero}**  |  "
        f"⬜ 待添加 **{n_pending}**\n",
        "## 说明\n",
        "- **⬜ 待添加**：在 Google Scholar 搜索论文，下载 PDF 后添加到 Zotero\n",
        "- **📥 Zotero已有**：Zotero 中已有该 PDF，运行以下命令同步到 storage/：\n",
        "  ```bash\n",
        "  python3 .claude/skills/paper-pipeline/sync_pdf.py --all\n",
        "  ```\n",
        "- 重新扫描并更新列表：\n",
        "  ```bash\n",
        "  python3 .claude/skills/paper-pipeline/check_missing.py --rescan\n",
        "  ```\n",
        "\n---\n",
    ]

    if n_inzotero > 0:
        lines.append("\n## 📥 Zotero已有（运行 sync 即可获取）\n\n")
        lines.append("| 状态 | Citation Key | 标题 | 来源 | Google Scholar |\n")
        lines.append("|:---:|:---|:---|:---:|:---:|\n")
        for status, key, title, fm, md_path in rows_pending:
            if status != STATUS_INZOTERO:
                continue
            short = title[:60] + "…" if len(title) > 60 else title
            url   = scholar_url(title)
            lines.append(
                f"| {status} | `{key}` | [{short}]({ref_rel_path(md_path)}) "
                f"| {venue_str(fm)} | [搜索]({url}) |\n"
            )

    lines.append("\n## ⬜ 待添加到 Zotero\n\n")
    lines.append("| 状态 | Citation Key | 标题 | 来源 | Google Scholar |\n")
    lines.append("|:---:|:---|:---|:---:|:---:|\n")
    for status, key, title, fm, md_path in rows_pending:
        if status != STATUS_PENDING:
            continue
        short = title[:60] + "…" if len(title) > 60 else title
        url   = scholar_url(title)
        lines.append(
            f"| {status} | `{key}` | [{short}]({ref_rel_path(md_path)}) "
            f"| {venue_str(fm)} | [搜索]({url}) |\n"
        )

    OUTPUT_FILE.write_text("".join(lines), encoding="utf-8")
    print(f"已写入：{OUTPUT_FILE.relative_to(REPO_ROOT)}")


# ── 入口 ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="生成/更新缺失 PDF 列表")
    parser.add_argument("--rescan", action="store_true",
                        help="重新查询 Zotero（默认保留上次状态，节省时间）")
    args = parser.parse_args()
    build_missing_list(rescan=args.rescan)
