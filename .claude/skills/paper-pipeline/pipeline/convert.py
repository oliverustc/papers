"""
convert.py — 调用 MinerU API 将 PDF 转换为 Markdown。
"""

import json
import shutil
import signal
import subprocess
import sys
import time
from datetime import datetime, timedelta

from pipeline.env import MINERU_URL, MINERU_TOKEN, STORAGE

TIMEOUT = 300


def _call_ustc(pdf_path) -> str | None:
    cmd = [
        "curl", "-s", "-m", str(TIMEOUT), "--noproxy", "*",
        "-H", f"Authorization: Bearer {MINERU_TOKEN}",
        "-F", f"files=@{pdf_path}",
        "-F", "return_md=true",
        MINERU_URL,
    ]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=TIMEOUT + 10)
    except subprocess.TimeoutExpired:
        print("  [MinerU] 请求超时", file=sys.stderr)
        return None
    if r.returncode != 0:
        print(f"  [MinerU] curl 失败: {r.stderr[:200]}", file=sys.stderr)
        return None
    try:
        data = json.loads(r.stdout)
    except json.JSONDecodeError:
        print(f"  [MinerU] 响应非 JSON: {r.stdout[:200]}", file=sys.stderr)
        return None
    if data.get("status") == "failed" or data.get("error"):
        print(f"  [MinerU] 失败: {data.get('error') or data.get('message', '?')}", file=sys.stderr)
        return None
    parts = [v["md_content"] for v in data.get("results", {}).values()
             if isinstance(v, dict) and "md_content" in v]
    return "\n\n".join(parts) if parts else None


def _find_pdf(key: str):
    matches = list(STORAGE.rglob(f"{key}/{key}.pdf"))
    return matches[0] if matches else None


def _process_one(key: str, dry_run: bool) -> bool:
    pdf = _find_pdf(key)
    if pdf is None:
        print(f"[{key}] storage/ 中未找到 PDF")
        return False
    out_dir = pdf.parent / "mineru-output"
    existing = out_dir / f"{key}.md"
    if existing.exists():
        print(f"[{key}] 已转换，跳过")
        return True
    if dry_run:
        print(f"[{key}] [dry-run] → {out_dir}/")
        return True
    print(f"[{key}] 调用 MinerU...")
    md = _call_ustc(pdf)
    if md is None:
        print(f"[{key}] 首次失败，3s 后重试...")
        time.sleep(3)
        md = _call_ustc(pdf)
    if md is None:
        print(f"[{key}] ✗ 转换失败")
        return False
    out_dir.mkdir(parents=True, exist_ok=True)
    existing.write_text(md, encoding="utf-8")
    print(f"[{key}] ✓ {len(md.encode()) // 1024} KB → {existing.name}")
    return True


def _all_pending():
    keys = []
    for pdf in STORAGE.rglob("*.pdf"):
        key = pdf.stem
        if pdf.name == f"{pdf.parent.name}.pdf":
            if not (pdf.parent / "mineru-output" / f"{key}.md").exists():
                keys.append(key)
    return sorted(keys)


def run(args) -> None:
    if args.dry_run:
        print("[dry-run 模式]\n")

    if args.key:
        _process_one(args.key, dry_run=args.dry_run)
        return

    if args.all:
        keys = _all_pending()
        if not keys:
            print("没有待转换的论文")
            return
        interval = 0 if args.dry_run else args.interval
        total = len(keys)
        print(f"待转换：{total} 篇，间隔 {interval}s，预计 {timedelta(seconds=interval*(total-1))}\n")

        interrupted = False
        def _sigint(*_):
            nonlocal interrupted
            print("\n[中断] 完成当前任务后退出...")
            interrupted = True
        signal.signal(signal.SIGINT, _sigint)

        ok = fail = 0
        for i, k in enumerate(keys, 1):
            print(f"[{i}/{total}]", end=" ")
            if _process_one(k, dry_run=args.dry_run):
                ok += 1
            else:
                fail += 1
            if interrupted:
                break
            if not args.dry_run and i < total:
                eta = datetime.now() + timedelta(seconds=interval * (total - i))
                print(f"  → 等待 {interval}s，预计 {eta.strftime('%H:%M:%S')}（剩余 {total-i} 篇）")
                time.sleep(interval)

        status = "中断" if interrupted else "完成"
        print(f"\n{status}：成功 {ok}，失败 {fail}，剩余 {total-ok-fail} 篇")
        return

    print("请指定 key 或使用 --all")
