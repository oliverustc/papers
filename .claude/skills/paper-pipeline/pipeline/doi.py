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


def _query_dblp(title: str) -> tuple[str | None, float, str]:
    """通过 DBLP 搜索，从 ee 字段提取 DOI。返回 (doi, similarity, dblp_title)"""
    params = urllib.parse.urlencode({"q": title, "format": "json", "h": "5"})
    req = urllib.request.Request(
        "https://dblp.org/search/publ/api?" + params,
        headers={"User-Agent": "paper-pipeline/1.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            hits = json.loads(resp.read()).get("result", {}).get("hits", {}).get("hit", [])
    except Exception as e:
        print(f"  [DBLP] 请求失败: {e}", file=sys.stderr)
        return None, 0.0, ""

    best_doi, best_sim, best_title = None, 0.0, ""
    for hit in hits:
        info = hit.get("info", {})
        db_title = info.get("title", "").rstrip(".")
        if not db_title:
            continue
        sim = _title_similarity(title, db_title)
        if sim <= best_sim:
            continue
        # 提取 DOI：ee 可能是字符串或列表
        ee = info.get("ee", "")
        ee_list = [ee] if isinstance(ee, str) else (ee if isinstance(ee, list) else [])
        for link in ee_list:
            if link.startswith("https://doi.org/"):
                best_sim = sim
                best_doi = link[len("https://doi.org/"):]
                best_title = db_title
                break
    return best_doi, best_sim, best_title


def find_doi(title: str, year: int | None) -> tuple[str | None, float, str]:
    """
    先查 DBLP（CS 论文精确），若相似度不足再查 CrossRef（兜底）。
    返回 (doi, similarity, source_title)，未找到返回 (None, 0.0, '')
    """
    # DBLP（主）
    dblp_doi, dblp_sim, dblp_title = _query_dblp(title)
    if dblp_doi and dblp_sim >= SIMILARITY_THRESHOLD:
        return dblp_doi, dblp_sim, f"[DBLP] {dblp_title}"

    # CrossRef（辅）
    items = _query_crossref(title, year)
    best_doi, best_sim, best_cr_title = None, 0.0, ""
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
            best_cr_title = raw_titles[0]

    # 取两者中更好的结果
    if dblp_doi and dblp_sim > best_sim:
        return dblp_doi, dblp_sim, f"[DBLP] {dblp_title}"
    return best_doi, best_sim, f"[CrossRef] {best_cr_title}"


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
    """返回 'ok'/'low'/'fail'/'skip'"""
    fm, _, _ = parse_frontmatter(md_path)
    if fm.get("doi"):
        return "skip"
    title = fm.get("title", "")
    year  = fm.get("发表年份")
    if not title:
        print(f"  [{md_path.stem}] 无标题，跳过")
        return "fail"
    doi, sim, cr_title = find_doi(title, int(year) if year else None)
    if doi is None:
        print(f"  [{md_path.stem}] CrossRef 无结果")
        return "fail"
    if sim < SIMILARITY_THRESHOLD:
        print(f"  [{md_path.stem}] 相似度过低 ({sim:.2f})")
        print(f"    我们的标题:    {title[:70]}")
        print(f"    CrossRef标题: {cr_title[:70]}")
        print(f"    DOI:  {doi}  → https://doi.org/{doi}")
        return "low"
    if dry_run:
        print(f"  [{md_path.stem}] [dry-run] doi: {doi}  (sim={sim:.2f})")
        return "ok"
    write_doi(md_path, doi)
    print(f"  [{md_path.stem}] ✓ doi: {doi}  (sim={sim:.2f})")
    return "ok"


def _interactive_review(paths: list) -> tuple[int, int, int]:
    """
    逐条查询 CrossRef 并交互审核：
    - 高相似度 (>= 0.82)：自动写入，无需确认
    - 低相似度：停下来询问 y/n/m/q
    - 无结果：自动跳过
    返回 (accepted, skipped, manual)
    """
    total = len(paths)
    print(f"共 {total} 篇待审核，高相似度自动写入，低相似度停下来询问")
    print("按键说明：[y] 接受候选DOI  [n] 跳过  [m] 手动输入DOI  [q] 退出\n")

    auto = accepted = skipped = manual_count = 0
    review_idx = 0  # 需要人工确认的计数

    for i, md_path in enumerate(paths, 1):
        fm, _, _ = parse_frontmatter(md_path)
        if fm.get("doi"):
            continue
        title = fm.get("title", "")
        year  = fm.get("发表年份")
        if not title:
            continue

        print(f"[{i}/{total}] 查询 {md_path.stem}...", end=" ", flush=True)
        doi, sim, cr_title = find_doi(title, int(year) if year else None)

        # 无结果，自动跳过
        if doi is None:
            print("无结果，跳过")
            skipped += 1
            time.sleep(REQUEST_DELAY)
            continue

        # 高相似度，自动写入
        if sim >= SIMILARITY_THRESHOLD:
            write_doi(md_path, doi)
            print(f"✓ 自动写入 (sim={sim:.2f})")
            auto += 1
            time.sleep(REQUEST_DELAY)
            continue

        # 低相似度，停下来询问
        review_idx += 1
        print(f"sim={sim:.2f}，需确认")
        print(f"  我们的标题:    {title}")
        print(f"  CrossRef标题: {cr_title}")
        print(f"  DOI: https://doi.org/{doi}")
        print(f"  Scholar: https://scholar.google.com/scholar?q={urllib.parse.quote(title)}")

        while True:
            try:
                choice = input("  → [y]接受 / [n]跳过 / [m]手动输入 / [q]退出: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\n已退出")
                return auto + accepted, skipped, manual_count

            if choice == "q":
                print("已退出")
                return auto + accepted, skipped, manual_count
            elif choice == "y":
                write_doi(md_path, doi)
                print(f"  ✓ 已写入 doi: {doi}")
                accepted += 1
                break
            elif choice == "n":
                print("  跳过")
                skipped += 1
                break
            elif choice == "m":
                try:
                    manual_doi = input("  输入 DOI（留空跳过）: ").strip()
                except (EOFError, KeyboardInterrupt):
                    break
                if manual_doi:
                    write_doi(md_path, manual_doi)
                    print(f"  ✓ 已写入 doi: {manual_doi}")
                    manual_count += 1
                else:
                    print("  跳过")
                    skipped += 1
                break
            else:
                print("  请输入 y / n / m / q")
        print()
        time.sleep(REQUEST_DELAY)

    if auto:
        print(f"（另自动写入高相似度 {auto} 篇）")
    return auto + accepted, skipped, manual_count


def run(args) -> None:
    if args.key:
        md = find_reference_md(args.key)
        if md is None:
            print(f"未找到 {args.key}.md")
            sys.exit(1)
        _process_one(md, dry_run=args.dry_run)
        return

    # 交互审核模式：逐条实时查询并审核
    if getattr(args, "interactive", False):
        paths = _all_missing()
        if not paths:
            print("所有论文均已有 DOI 字段")
            return
        accepted, skipped, manual_count = _interactive_review(paths)
        print(f"\n审核完成：✓ {accepted} 篇接受，✎ {manual_count} 篇手动输入，⏭ {skipped} 篇跳过")
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

    if low > 0:
        print(f"\n提示：运行 `pp doi --interactive` 对 {low} 篇低相似度论文逐条审核")
