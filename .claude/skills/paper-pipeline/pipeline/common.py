"""
common.py — 各模块共用的工具函数。
"""

import re
from pathlib import Path

import yaml

from pipeline.env import STORAGE, REFERENCES


def parse_frontmatter(md_path: Path) -> tuple[dict, str, str]:
    """返回 (frontmatter_dict, fm_raw_str, body_str)"""
    text = md_path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)", text, re.DOTALL)
    if not m:
        return {}, "", text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, m.group(1), m.group(2)


def storage_dir(key: str, fm: dict) -> Path:
    """返回 storage/{类型}/{会议}/{年}/{key}/ 目录，不存在则创建。"""
    ptype = fm.get("论文类型", "unknown")
    year  = str(fm.get("发表年份", "unknown"))
    if ptype == "conference":
        venue = fm.get("会议简称", "unknown")
    elif ptype == "journal":
        venue = fm.get("期刊简称", "unknown")
    elif ptype == "preprint":
        venue = fm.get("预印本简称", "unknown")
    else:
        venue = "unknown"
    d = STORAGE / ptype / venue / year / key
    d.mkdir(parents=True, exist_ok=True)
    return d


def already_has_pdf(key: str) -> bool:
    return bool(list(STORAGE.rglob(f"{key}/{key}.pdf")))


def find_reference_md(key: str) -> Path | None:
    matches = [p for p in REFERENCES.rglob(f"{key}.md") if p.name != "index.md"]
    return matches[0] if matches else None


def normalize_title(t: str) -> str:
    return re.sub(r"[^a-z0-9]", "", t.lower())


def winpath_to_wsl(path_str: str) -> Path:
    m = re.match(r"^([A-Za-z]):\\(.*)", path_str)
    if m:
        return Path(f"/mnt/{m.group(1).lower()}/{m.group(2).replace(chr(92), '/')}")
    return Path(path_str)
