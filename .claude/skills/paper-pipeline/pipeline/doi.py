"""
doi.py — 通过 CrossRef API 自动补充论文 DOI 字段。
"""

import difflib
import json
import re
import sys
import time
import urllib.parse
import urllib.request

from pipeline.common import parse_frontmatter, find_reference_md
from pipeline.env import REFERENCES

CROSSREF_URL         = "https://api.crossref.org/works"
SIMILARITY_THRESHOLD = 0.82
REQUEST_DELAY        = 1.0


def _normalize(s: str) -> str:
    return re.sub(r"[^a-z0-9 ]", "", s.lower()).strip()


def _title_similarity(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, _normalize(a), _normalize(b)).ratio()


def _query_crossref(title: str, year: int | None) -> list[dict]:
    params = {"query.title": title, "rows": "5", "select": "DOI,title,published,author"}
    if year:
        params["query.bibliographic"] = str(year)
    url = CROSSREF_URL + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "paper-pipeline/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read()).get("message", {}).get("items", [])
    except Exception as e:
        print(f"  [CrossRef] 请求失败: {e}", file=sys.stderr)
        return []


def find_doi(title: str, year: int | None) -> tuple[str | None, float]:
    """返回 (doi, similarity)，未找到返回 (None, 0.0)"""
    items = _query_crossref(title, year)
    best_doi, best_sim = None, 0.0
    for item in items:
        raw_titles = item.get("title", [])
        if not raw_titles:
            continue
        sim = max(_title_similarity(title, t) for t in raw_titles)
        pub = item.get("published", {}).get("date-parts", [[None]])[0]
        pub_year = pub[0] if pub else None
        if year and pub_year and abs(pub_year - year) > 2:
            sim *= 0.7
        if sim > best_sim:
            best_sim = sim
            best_doi = item.get("DOI")
    return best_doi, best_sim


def write_doi(md_path, doi: str) -> None:
    fm, fm_raw, body = parse_frontmatter(md_path)
    if fm.get("doi"):
        return
    lines, inserted = fm_raw.splitlines(), False
    new_lines = []
    for line in lines:
        new_lines.append(line)
        if not inserted and line.startswith("title:"):
            new_lines.append(f"doi: {doi}")
            inserted = True
    if not inserted:
        new_lines.append(f"doi: {doi}")
    md_path.write_text("---\n" + "\n".join(new_lines) + "\n---\n" + body, encoding="utf-8")


def _all_missing() -> list:
    paths = []
    for md in sorted(REFERENCES.rglob("*.md")):
        if md.name == "index.md":
            continue
        fm, _, _ = parse_frontmatter(md)
        if fm.get("论文类型") and fm.get("title") and not fm.get("doi"):
            paths.append(md)
    return paths


def _process_one(md_path, dry_run: bool) -> str:
    fm, _, _ = parse_frontmatter(md_path)
    if fm.get("doi"):
        return "skip"
    title = fm.get("title", "")
    year  = fm.get("发表年份")
    if not title:
        print(f"  [{md_path.stem}] 无标题，跳过")
        return "fail"
    doi, sim = find_doi(title, int(year) if year else None)
    if doi is None:
        print(f"  [{md_path.stem}] CrossRef 无结果")
        return "fail"
    if sim < SIMILARITY_THRESHOLD:
        print(f"  [{md_path.stem}] 相似度过低 ({sim:.2f})，需手动确认")
        print(f"    标题: {title[:70]}")
        print(f"    DOI:  {doi}  → https://doi.org/{doi}")
        return "low"
    if dry_run:
        print(f"  [{md_path.stem}] [dry-run] doi: {doi}  (sim={sim:.2f})")
        return "ok"
    write_doi(md_path, doi)
    print(f"  [{md_path.stem}] ✓ doi: {doi}  (sim={sim:.2f})")
    return "ok"


def run(args) -> None:
    if args.key:
        md = find_reference_md(args.key)
        if md is None:
            print(f"未找到 {args.key}.md")
            sys.exit(1)
        _process_one(md, dry_run=args.dry_run)
        return

    paths = _all_missing()
    if not paths:
        print("所有论文均已有 DOI 字段")
        return
    total = len(paths)
    print(f"待补充 DOI：{total} 篇\n")
    ok = low = fail = skip = 0
    for i, md in enumerate(paths, 1):
        print(f"[{i}/{total}] {md.stem}")
        result = _process_one(md, dry_run=args.dry_run)
        if result == "ok":     ok   += 1
        elif result == "low":  low  += 1
        elif result == "fail": fail += 1
        else:                  skip += 1
        if i < total:
            time.sleep(REQUEST_DELAY)
    print(f"\n完成：✓ {ok} 篇写入，⚠ {low} 篇相似度低，✗ {fail} 篇失败，⏭ {skip} 篇已有")
