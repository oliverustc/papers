"""
fetch.py — 自动下载论文 PDF（DBLP/ePrint → Unpaywall → Sci-Hub 链接）。
"""

import json
import re
import sys
import time
import urllib.parse
import urllib.request

from pipeline.common import (
    parse_frontmatter, storage_dir, already_has_pdf, find_reference_md
)
from pipeline.env import REFERENCES, UNPAYWALL_EMAIL

REQUEST_DELAY = 2.0
TIMEOUT       = 30


def _http_get(url: str, headers: dict | None = None) -> bytes | None:
    req = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.read()
    except Exception:
        return None


def _save_pdf(data: bytes, dest) -> bool:
    if len(data) < 10_000 or not data.startswith(b"%PDF"):
        return False
    dest.write_bytes(data)
    return True


def _download_pdf(url: str, dest) -> bool:
    data = _http_get(url, headers={"User-Agent": "paper-pipeline/1.0"})
    return _save_pdf(data, dest) if data else False


def _try_dblp_eprint(title: str, dest) -> str | None:
    params = urllib.parse.urlencode({"q": title, "format": "json", "h": "5"})
    data = _http_get(
        "https://dblp.org/search/publ/api?" + params,
        headers={"User-Agent": "paper-pipeline/1.0"},
    )
    if not data:
        return None
    try:
        hits = json.loads(data).get("result", {}).get("hits", {}).get("hit", [])
    except json.JSONDecodeError:
        return None
    for hit in hits:
        ee = hit.get("info", {}).get("ee", "")
        ee_list = [ee] if isinstance(ee, str) else (ee if isinstance(ee, list) else [])
        for link in ee_list:
            m = re.match(r"https://eprint\.iacr\.org/(\d{4}/\d+)", link)
            if m:
                pdf_url = f"https://eprint.iacr.org/{m.group(1)}.pdf"
                if _download_pdf(pdf_url, dest):
                    return pdf_url
    return None


def _try_unpaywall(doi: str, dest) -> str | None:
    if not doi:
        return None
    if not UNPAYWALL_EMAIL:
        print("    [Unpaywall] 未配置 UNPAYWALL_EMAIL，跳过")
        return None
    api_url = (
        f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi, safe='')}?"
        f"email={urllib.parse.quote(UNPAYWALL_EMAIL)}"
    )
    data = _http_get(api_url, headers={"User-Agent": "paper-pipeline/1.0"})
    if not data:
        return None
    try:
        best = json.loads(data).get("best_oa_location")
    except json.JSONDecodeError:
        return None
    if not best:
        return None
    pdf_url = best.get("url_for_pdf") or best.get("url")
    return pdf_url if pdf_url and _download_pdf(pdf_url, dest) else None


def _scihub_link(doi: str, title: str) -> str:
    return f"https://sci-hub.se/{doi}" if doi else \
           f"https://sci-hub.se/?query={urllib.parse.quote(title)}"


def _process_one(md_path, dry_run: bool) -> str:
    fm, _, _ = parse_frontmatter(md_path)
    key   = md_path.stem
    title = fm.get("title", "")
    doi   = fm.get("doi", "")
    if not title:
        print(f"  [{key}] 无标题，跳过")
        return "fail"
    if already_has_pdf(key):
        return "skip"
    dest = storage_dir(key, fm) / f"{key}.pdf"
    if dry_run:
        print(f"  [{key}] [dry-run] DBLP/ePrint → Unpaywall → Sci-Hub")
        print(f"    {title[:70]}")
        return "ok"
    print(f"  [{key}] {title[:65]}")
    if doi:
        print(f"    DOI: {doi}")

    print("    尝试 DBLP/ePrint...", end=" ", flush=True)
    url = _try_dblp_eprint(title, dest)
    if url:
        print("✓")
        print(f"  [{key}] ✓ ePrint: {url}")
        return "ok"
    print("✗")
    time.sleep(REQUEST_DELAY)

    print("    尝试 Unpaywall...", end=" ", flush=True)
    url = _try_unpaywall(doi, dest)
    if url:
        print("✓")
        print(f"  [{key}] ✓ Unpaywall: {url}")
        return "ok"
    print("✗")

    print(f"  [{key}] ⚠ 自动下载失败，请手动获取：")
    print(f"    Sci-Hub: {_scihub_link(doi, title)}")
    return "manual"


def _all_missing():
    paths = []
    for md in sorted(REFERENCES.rglob("*.md")):
        if md.name == "index.md":
            continue
        fm, _, _ = parse_frontmatter(md)
        if fm.get("论文类型") and fm.get("title") and not already_has_pdf(md.stem):
            paths.append(md)
    return paths


def run(args) -> None:
    if args.key:
        md = find_reference_md(args.key)
        if md is None:
            print(f"未找到 {args.key}.md")
            sys.exit(1)
        result = _process_one(md, dry_run=args.dry_run)
        sys.exit(0 if result in ("ok", "skip") else 1)

    if args.all:
        paths = _all_missing()
        if not paths:
            print("所有论文均已有 PDF")
            return
        total = len(paths)
        print(f"待获取 PDF：{total} 篇\n")
        ok = manual = fail = skip = 0
        for i, md in enumerate(paths, 1):
            print(f"[{i}/{total}] {md.stem}")
            result = _process_one(md, dry_run=args.dry_run)
            if result == "ok":       ok     += 1
            elif result == "manual": manual += 1
            elif result == "fail":   fail   += 1
            else:                    skip   += 1
            if i < total:
                time.sleep(REQUEST_DELAY)
        print(f"\n完成：✓ {ok} 篇下载，⚠ {manual} 篇需手动，✗ {fail} 篇失败，⏭ {skip} 篇已有")
