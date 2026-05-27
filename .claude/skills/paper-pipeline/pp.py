#!/usr/bin/env -S python3 -u
"""
pp — Paper Pipeline 统一命令行入口

用法:
    python3 .claude/skills/paper-pipeline/pp.py <command> [options]

命令:
    sync      从 Zotero 同步 PDF 到 storage/
    fetch     自动下载 PDF（IACR ePrint / Unpaywall / Sci-Hub 链接）
    convert   MinerU PDF → Markdown
    note      LLM 生成结构化笔记
    doi       CrossRef 自动补充 DOI 字段
    status    生成流水线状态看板
"""

import argparse
import sys
from pathlib import Path

# 将 paper-pipeline/ 加入路径，使 `import pipeline` 可用
sys.path.insert(0, str(Path(__file__).parent))


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pp",
        description="Paper Pipeline — 论文笔记自动化流水线",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "典型单篇流程:\n"
            "  pp doi <key>      # 补充 DOI\n"
            "  pp fetch <key>    # 下载 PDF\n"
            "  pp convert <key>  # MinerU 转换\n"
            "  pp note <key>     # 生成笔记\n\n"
            "批量流程:\n"
            "  pp doi --dry-run  # 预览 DOI 补充\n"
            "  pp fetch --all    # 批量下载\n"
            "  pp convert --all --interval 120\n"
            "  pp note --all --interval 30\n"
            "  pp status         # 更新状态看板\n"
        ),
    )
    sub = parser.add_subparsers(dest="command", metavar="command")
    sub.required = True

    # ── sync ──────────────────────────────────────────────────────────────────
    p = sub.add_parser("sync", help="从 Zotero 同步 PDF 到 storage/")
    p.add_argument("key", nargs="?", help="citation key")
    p.add_argument("--all",     action="store_true", help="处理所有论文")
    p.add_argument("--dry-run", action="store_true", help="预览，不复制")

    # ── fetch ─────────────────────────────────────────────────────────────────
    p = sub.add_parser("fetch", help="自动下载 PDF（IACR ePrint / Unpaywall）")
    p.add_argument("key", nargs="?", help="citation key")
    p.add_argument("--all",     action="store_true", help="处理所有缺 PDF 的论文")
    p.add_argument("--dry-run", action="store_true", help="预览，不下载")

    # ── convert ───────────────────────────────────────────────────────────────
    p = sub.add_parser("convert", help="MinerU PDF → Markdown")
    p.add_argument("key", nargs="?", help="citation key")
    p.add_argument("--all",      action="store_true", help="处理所有待转换论文")
    p.add_argument("--dry-run",  action="store_true", help="预览，不调用 API")
    p.add_argument("--interval", type=int, default=120, metavar="SEC",
                   help="批量模式调用间隔秒数（默认 120）")

    # ── note ──────────────────────────────────────────────────────────────────
    p = sub.add_parser("note", help="LLM 生成结构化笔记")
    p.add_argument("key", nargs="?", help="citation key")
    p.add_argument("--all",      action="store_true", help="处理所有待生成笔记的论文")
    p.add_argument("--dry-run",  action="store_true", help="预览，不写文件")
    p.add_argument("--interval", type=int, default=30, metavar="SEC",
                   help="批量模式调用间隔秒数（默认 30）")

    # ── doi ───────────────────────────────────────────────────────────────────
    p = sub.add_parser("doi", help="CrossRef 自动补充 DOI 字段")
    p.add_argument("key", nargs="?", help="citation key，留空则处理所有缺 DOI 的论文")
    p.add_argument("--dry-run",     action="store_true", help="预览，不写文件")
    p.add_argument("--interactive", action="store_true",
                   help="对相似度低的论文逐条交互审核（y/n/m/q）")

    # ── status ────────────────────────────────────────────────────────────────
    sub.add_parser("status", help="生成流水线状态看板（pipeline-status.md）")

    return parser


def main() -> None:
    parser = _parser()
    args = parser.parse_args()

    if args.command == "sync":
        from pipeline.sync import run
    elif args.command == "fetch":
        from pipeline.fetch import run
    elif args.command == "convert":
        from pipeline.convert import run
    elif args.command == "note":
        from pipeline.note import run
    elif args.command == "doi":
        from pipeline.doi import run
    elif args.command == "status":
        from pipeline.status import run
    else:
        parser.print_help()
        sys.exit(1)

    run(args)


if __name__ == "__main__":
    main()
