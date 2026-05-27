"""
sync.py — 从 Zotero storage 同步 PDF 到项目 storage/ 目录。
"""

import shutil
import sqlite3
import sys

from pipeline.common import (
    parse_frontmatter, storage_dir, find_reference_md, normalize_title, winpath_to_wsl
)
from pipeline.env import REFERENCES, ZOTERO_DB, ZOTERO_STORE


def _find_in_zotero(title: str):
    if not ZOTERO_DB.exists():
        print(f"  [错误] Zotero 数据库不存在: {ZOTERO_DB}", file=sys.stderr)
        return None
    norm = normalize_title(title)
    conn = sqlite3.connect(str(ZOTERO_DB))
    try:
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
            AND ia.path IS NOT NULL AND f.fieldName = 'title'
        """)
        rows = cur.fetchall()
    finally:
        conn.close()

    for attach_key, raw_path, db_title in rows:
        if normalize_title(db_title) != norm:
            continue
        if raw_path.startswith("storage:"):
            pdf = ZOTERO_STORE / attach_key / raw_path[len("storage:"):]
        else:
            pdf = winpath_to_wsl(raw_path)
        if pdf.exists():
            return pdf, attach_key
    return None


def _process_one(key: str, dry_run: bool) -> bool:
    md = find_reference_md(key)
    if md is None:
        print(f"[{key}] 未找到 references md 文件")
        return False
    fm, _, _ = parse_frontmatter(md)
    title = fm.get("title", "")
    if not title:
        print(f"[{key}] 无标题")
        return False
    dest = storage_dir(key, fm) / f"{key}.pdf"
    if dest.exists():
        print(f"[{key}] PDF 已存在，跳过")
        return True
    print(f"[{key}] 搜索: {title[:60]}...")
    result = _find_in_zotero(title)
    if result is None:
        print(f"[{key}] Zotero 中未找到")
        return False
    src, attach_key = result
    print(f"[{key}] 找到: {src.name}  (key: {attach_key})")
    if dry_run:
        print(f"[{key}] [dry-run] → {dest}")
        return True
    shutil.copy2(str(src), str(dest))
    print(f"[{key}] ✓ 已同步")
    return True


def run(args) -> None:
    if args.dry_run:
        print("[dry-run 模式]\n")

    if args.key:
        _process_one(args.key, dry_run=args.dry_run)
        return

    if args.all:
        keys = sorted(
            md.stem for md in REFERENCES.rglob("*.md")
            if md.name != "index.md" and parse_frontmatter(md)[0].get("论文类型")
        )
        print(f"共 {len(keys)} 篇\n")
        ok = fail = skip = 0
        for k in keys:
            md = find_reference_md(k)
            if md:
                fm, _, _ = parse_frontmatter(md)
                dest = storage_dir(k, fm) / f"{k}.pdf"
                if dest.exists():
                    skip += 1
                    continue
            if _process_one(k, dry_run=args.dry_run):
                ok += 1
            else:
                fail += 1
        print(f"\n完成：同步 {ok}，跳过 {skip}，未找到 {fail}")
        return

    print("请指定 key 或使用 --all")
