"""
env.py — 从 repo 根目录的 .env 文件加载配置，提供各脚本所需的常量。

不依赖 python-dotenv，使用标准库手动解析。
"""

import os
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent.parent
_ENV_FILE = Path(__file__).parent / ".env"


def _load_dotenv() -> dict[str, str]:
    if not _ENV_FILE.exists():
        return {}
    result = {}
    for line in _ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        result[key.strip()] = val.strip().strip('"').strip("'")
    return result


_env = _load_dotenv()


def _get(key: str, default: str) -> str:
    return os.environ.get(key) or _env.get(key) or default


# ── MinerU API ────────────────────────────────────────────────────────────────
MINERU_URL   = _get("MINERU_URL",   "https://api.llm.ustc.edu.cn/mineru/file_parse")
MINERU_TOKEN = _get("MINERU_TOKEN", "")

# ── LLM API ───────────────────────────────────────────────────────────────────
LLM_URL   = _get("LLM_URL",   "https://api.llm.ustc.edu.cn/v1/chat/completions")
LLM_TOKEN = _get("LLM_TOKEN", "")
LLM_MODEL = _get("LLM_MODEL", "deepseek-v4-flash-ascend")

# ── Zotero（WSL 路径）────────────────────────────────────────────────────────
ZOTERO_DB    = Path(_get("ZOTERO_DB",    "/mnt/c/Users/swt/Zotero/zotero.sqlite"))
ZOTERO_STORE = Path(_get("ZOTERO_STORE", "/mnt/c/Users/swt/Zotero/storage"))
