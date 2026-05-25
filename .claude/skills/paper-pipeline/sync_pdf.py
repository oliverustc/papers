#!/usr/bin/env -S python3 -u
"""
sync_pdf.py — 从 Zotero storage 同步 PDF 到项目 storage/ 目录

用法:
    python3 .claude/skills/paper-pipeline/sync_pdf.py <citation_key>
    python3 .claude/skills/paper-pipeline/sync_pdf.py --all
    python3 .claude/skills/paper-pipeline/sync_pdf.py --dry-run --all
"""

import argparse
import re
import shutil
import sqlite3
import sys
from pathlib import Path

import yaml

import sys
sys.path.insert(0, str(Path(__file__).parent))
from env import ZOTERO_DB, ZOTERO_STORE, REPO_ROOT

# ── 路径配置 ─────────────────────────────────────────────────────────────────
REFERENCES = REPO_ROOT / "references"
STORAGE    = REPO_ROOT / "storage"


# ── 工具函数 ──────────────────────────────────────────────────────────────────

def normalize_title(t: str) -> str:
    """去除标点、空白、大小写，用于模糊匹配"""
    return re.sub(r"[^a-z0-9]", "", t.lower())


def winpath_to_wsl(path_str: str) -> Path:
    """将 Windows 绝对路径转换为 WSL 挂载路径"""
    # C:\Users\... → /mnt/c/Users/...
    m = re.match(r"^([A-Za-z]):\\(.*)", path_str)
    if m:
        drive = m.group(1).lower()
        rest  = m.group(2).replace("\\", "/")
        return Path(f"/mnt/{drive}/{rest}")
    return Path(path_str)


def parse_frontmatter(md_path: Path) -> dict:
    """解析 Markdown 文件的 YAML frontmatter"""
    text = md_path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}


def storage_path_for(key: str, fm: dict) -> Path:
    """根据 frontmatter 推断 storage 子目录路径"""
    ptype = fm.get("论文类型", "")
    year  = str(fm.get("发表年份", "unknown"))

    if ptype == "conference":
        venue = fm.get("会议简称", "unknown")
    elif ptype == "journal":
        venue = fm.get("期刊简称", "unknown")
    elif ptype == "preprint":
        venue = fm.get("预印本简称", "unknown")
    else:
        venue = "unknown"

    return STORAGE / ptype / venue / year / key


def find_pdf_in_zotero(title: str) -> tuple[Path, str] | None:
    """
    在 Zotero SQLite 中按标题查找 PDF。
    返回 (pdf_path, attach_key) 或 None。
    """
    if not ZOTERO_DB.exists():
        print(f"  [错误] Zotero 数据库不存在: {ZOTERO_DB}", file=sys.stderr)
        return None

    norm_title = normalize_title(title)

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
            AND ia.path IS NOT NULL
            AND f.fieldName = 'title'
        """)
        rows = cur.fetchall()
    finally:
        conn.close()

    best_key  = None
    best_path = None

    for attach_key, raw_path, db_title in rows:
        if normalize_title(db_title) == norm_title:
            best_key  = attach_key
            best_path = raw_path
            break

    if best_key is None:
        return None

    # 解析实际文件路径
    if raw_path.startswith("storage:"):
        filename = raw_path[len("storage:"):]
        pdf_path = ZOTERO_STORE / best_key / filename
    else:
        pdf_path = winpath_to_wsl(raw_path)

    if not pdf_path.exists():
        print(f"  [警告] Zotero 数据库有记录，但文件不存在: {pdf_path}", file=sys.stderr)
        return None

    return pdf_path, best_key


def sync_one(key: str, dry_run: bool = False) -> bool:
    """同步单篇论文的 PDF。返回是否成功。"""
    # 查找对应的 md 文件
    matches = list(REFERENCES.rglob(f"{key}.md"))
    matches = [p for p in matches if p.name != "index.md"]
    if not matches:
        print(f"[{key}] 未找到对应的 references md 文件")
        return False

    md_path = matches[0]
    fm = parse_frontmatter(md_path)

    title = fm.get("title", "")
    if not title:
        print(f"[{key}] frontmatter 中没有 title 字段")
        return False

    dest_dir = storage_path_for(key, fm)
    dest_pdf  = dest_dir / f"{key}.pdf"

    if dest_pdf.exists():
        print(f"[{key}] PDF 已存在，跳过: {dest_pdf.relative_to(REPO_ROOT)}")
        return True

    print(f"[{key}] 搜索: {title[:60]}...")
    result = find_pdf_in_zotero(title)
    if result is None:
        print(f"[{key}] Zotero 中未找到匹配 PDF")
        return False

    src_pdf, attach_key = result
    print(f"[{key}] 找到: {src_pdf.name}  (Zotero key: {attach_key})")

    if dry_run:
        print(f"[{key}] [dry-run] 将复制到: {dest_pdf.relative_to(REPO_ROOT)}")
        return True

    dest_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(str(src_pdf), str(dest_pdf))
    print(f"[{key}] ✓ 已复制到: {dest_pdf.relative_to(REPO_ROOT)}")
    return True


def all_citation_keys() -> list[str]:
    """遍历 references/ 下所有论文 md 文件，返回 citation key 列表"""
    keys = []
    for p in REFERENCES.rglob("*.md"):
        if p.name == "index.md":
            continue
        fm = parse_frontmatter(p)
        if fm.get("论文类型"):   # 只处理有论文类型的文件
            keys.append(p.stem)
    return sorted(keys)


# ── 主程序 ───────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="从 Zotero 同步 PDF 到项目 storage/")
    parser.add_argument("key", nargs="?", help="citation key，例如 sun2025committed")
    parser.add_argument("--all",     action="store_true", help="处理所有论文")
    parser.add_argument("--dry-run", action="store_true", help="预览，不实际复制")
    args = parser.parse_args()

    if args.dry_run:
        print("[dry-run 模式] 不会实际复制文件\n")

    if args.all:
        keys = all_citation_keys()
        print(f"共找到 {len(keys)} 篇论文\n")
        ok = fail = skip = 0
        for k in keys:
            dest_dir = None
            # 快速预检：已有 PDF 则不搜索数据库
            matches = list(REFERENCES.rglob(f"{k}.md"))
            matches = [p for p in matches if p.name != "index.md"]
            if matches:
                fm = parse_frontmatter(matches[0])
                dest_pdf = storage_path_for(k, fm) / f"{k}.pdf"
                if dest_pdf.exists():
                    skip += 1
                    continue
            result = sync_one(k, dry_run=args.dry_run)
            if result:
                ok += 1
            else:
                fail += 1
        print(f"\n完成：成功 {ok}，跳过（已有）{skip}，未找到 {fail}")

    elif args.key:
        sync_one(args.key, dry_run=args.dry_run)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
