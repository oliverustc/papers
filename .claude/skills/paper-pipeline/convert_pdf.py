#!/usr/bin/env -S python3 -u
"""
convert_pdf.py — 调用 MinerU API 将 storage/ 中的 PDF 转换为 Markdown

用法:
    python3 .claude/skills/paper-pipeline/convert_pdf.py <citation_key>
    python3 .claude/skills/paper-pipeline/convert_pdf.py --all
    python3 .claude/skills/paper-pipeline/convert_pdf.py --dry-run --all
"""

import argparse
import base64
import json
import signal
import subprocess
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

import urllib.request
import urllib.error

import sys
sys.path.insert(0, str(Path(__file__).parent))
from env import MINERU_URL, MINERU_TOKEN, REPO_ROOT

# ── 配置 ──────────────────────────────────────────────────────────────────────
STORAGE    = REPO_ROOT / "storage"
USTC_URL   = MINERU_URL
USTC_TOKEN = MINERU_TOKEN
TIMEOUT    = 300   # 秒


# ── MinerU API 调用 ───────────────────────────────────────────────────────────

def call_ustc_api(pdf_path: Path) -> str | None:
    """
    调用 USTC MinerU API，返回 Markdown 字符串，失败返回 None。
    使用 curl 发送 multipart/form-data（避免 Python 标准库的 multipart 复杂性）。
    """
    cmd = [
        "curl", "-s", "-m", str(TIMEOUT), "--noproxy", "*",
        "-H", f"Authorization: Bearer {USTC_TOKEN}",
        "-F", f"files=@{pdf_path}",
        "-F", "return_md=true",
        USTC_URL,
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=TIMEOUT + 10)
    except subprocess.TimeoutExpired:
        print("  [USTC] 请求超时", file=sys.stderr)
        return None

    if result.returncode != 0:
        print(f"  [USTC] curl 失败: {result.stderr[:200]}", file=sys.stderr)
        return None

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        print(f"  [USTC] 响应非 JSON: {result.stdout[:200]}", file=sys.stderr)
        return None

    # 响应结构：{"status": "completed", "results": {"<filename>": {"md_content": "..."}}}
    try:
        status = data.get("status", "")
        if status == "failed":
            err = data.get("error") or data.get("message", "unknown")
            print(f"  [USTC] 任务失败: {str(err)[:200]}", file=sys.stderr)
            return None
        # 顶层 error 字段（非 null）
        if data.get("error"):
            print(f"  [USTC] API 错误: {str(data['error'])[:200]}", file=sys.stderr)
            return None
        entries = data.get("results", {})
        if not entries:
            print(f"  [USTC] 响应中无 results: {str(data)[:300]}", file=sys.stderr)
            return None
        # results key 是文件名（去掉扩展名），value 含 md_content
        md_parts = [v["md_content"] for v in entries.values() if isinstance(v, dict) and "md_content" in v]
        return "\n\n".join(md_parts) if md_parts else None
    except (KeyError, TypeError) as e:
        print(f"  [USTC] 解析响应失败: {e}\n  响应: {str(data)[:300]}", file=sys.stderr)
        return None


def call_cli_fallback(pdf_path: Path, out_dir: Path) -> str | None:
    """
    Fallback：调用 mineru-open-api CLI，返回 Markdown 字符串，失败返回 None。
    """
    cmd = ["mineru-open-api", "extract", str(pdf_path), "-o", str(out_dir), "--language", "en"]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=TIMEOUT + 10)
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        print(f"  [CLI] {e}", file=sys.stderr)
        return None

    if result.returncode != 0:
        print(f"  [CLI] 失败: {result.stderr[:200]}", file=sys.stderr)
        return None

    # CLI 将 md 输出到 out_dir，找到它
    md_files = list(out_dir.glob("**/*.md"))
    if not md_files:
        return None
    return md_files[0].read_text(encoding="utf-8")


# ── 核心转换逻辑 ──────────────────────────────────────────────────────────────

def find_pdf(key: str) -> Path | None:
    """在 storage/ 中查找 citation key 对应的 PDF"""
    matches = list(STORAGE.rglob(f"{key}/{key}.pdf"))
    return matches[0] if matches else None


def convert_one(key: str, dry_run: bool = False) -> bool:
    """转换单篇论文。返回是否成功。"""
    pdf_path = find_pdf(key)
    if pdf_path is None:
        print(f"[{key}] storage/ 中未找到 PDF，请先运行 sync_pdf.py")
        return False

    out_dir = pdf_path.parent / "mineru-output"

    # 幂等检查：已有 md 文件则跳过
    existing_md = out_dir / f"{key}.md"
    if existing_md.exists():
        print(f"[{key}] mineru-output 已存在，跳过")
        return True

    if dry_run:
        print(f"[{key}] [dry-run] 将转换: {pdf_path.relative_to(REPO_ROOT)}")
        print(f"[{key}] [dry-run] 输出到: {out_dir.relative_to(REPO_ROOT)}/")
        return True

    print(f"[{key}] 调用 USTC MinerU API...")
    md_content = call_ustc_api(pdf_path)

    if md_content is None:
        print(f"[{key}] USTC 首次失败，3 秒后重试...")
        time.sleep(3)
        md_content = call_ustc_api(pdf_path)

    if md_content is None:
        print(f"[{key}] USTC 失败，尝试 CLI fallback...")
        tmp_dir = out_dir / "_cli_tmp"
        md_content = call_cli_fallback(pdf_path, tmp_dir)
        if tmp_dir.exists():
            import shutil
            shutil.rmtree(tmp_dir)

    if md_content is None:
        print(f"[{key}] ✗ 转换失败（USTC + CLI 均不可用）")
        return False

    out_dir.mkdir(parents=True, exist_ok=True)
    existing_md.write_text(md_content, encoding="utf-8")
    size_kb = len(md_content.encode()) // 1024
    print(f"[{key}] ✓ 转换完成，{size_kb} KB → {existing_md.relative_to(REPO_ROOT)}")
    return True


def all_pending_keys() -> list[str]:
    """返回所有有 PDF 但没有 mineru-output/{key}.md 的 citation key"""
    keys = []
    for pdf in STORAGE.rglob("*.pdf"):
        key = pdf.stem
        if pdf.name == f"{pdf.parent.name}.pdf":   # storage/.../key/key.pdf
            md = pdf.parent / "mineru-output" / f"{key}.md"
            if not md.exists():
                keys.append(key)
    return sorted(keys)


# ── 主程序 ───────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="调用 MinerU API 转换 PDF → Markdown")
    parser.add_argument("key", nargs="?", help="citation key，例如 abbaszadeh2024zero")
    parser.add_argument("--all",      action="store_true", help="处理所有待转换论文")
    parser.add_argument("--dry-run",  action="store_true", help="预览，不实际转换")
    parser.add_argument("--interval", type=int, default=120,
                        help="批量模式下两次 API 调用的间隔秒数（默认 120）")
    args = parser.parse_args()

    if args.dry_run:
        print("[dry-run 模式] 不会实际调用 API\n")

    if args.all:
        keys = all_pending_keys()
        if not keys:
            print("没有待转换的论文（所有有 PDF 的论文均已转换）")
            return

        interval = 0 if args.dry_run else args.interval
        total = len(keys)
        eta_total = timedelta(seconds=interval * (total - 1))
        print(f"待转换：{total} 篇，间隔 {interval}s，预计总耗时 {eta_total}\n")

        interrupted = False
        def _handle_sigint(sig, frame):
            nonlocal interrupted
            print("\n\n[中断] 收到 Ctrl-C，完成当前任务后退出...")
            interrupted = True
        signal.signal(signal.SIGINT, _handle_sigint)

        ok = fail = 0
        for i, k in enumerate(keys, 1):
            print(f"[{i}/{total}]", end=" ")
            if convert_one(k, dry_run=args.dry_run):
                ok += 1
            else:
                fail += 1
            if interrupted:
                break
            if not args.dry_run and i < total:
                eta = datetime.now() + timedelta(seconds=interval * (total - i))
                print(f"  → 等待 {interval}s，预计完成时间 {eta.strftime('%H:%M:%S')} "
                      f"（剩余 {total - i} 篇）")
                time.sleep(interval)

        status = "中断" if interrupted else "完成"
        print(f"\n{status}：成功 {ok}，失败 {fail}，剩余 {total - ok - fail} 篇未处理")

    elif args.key:
        convert_one(args.key, dry_run=args.dry_run)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
