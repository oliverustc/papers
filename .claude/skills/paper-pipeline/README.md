# Paper Pipeline

论文笔记自动化流水线：Zotero PDF 同步 → MinerU Markdown 转换 → LLM 结构化笔记生成。

统一通过 `pp.py` 调用，无需记忆各脚本名称。

---

## 环境配置

### 依赖

- Python 3.10+
- PyYAML：`pip install pyyaml`
- `curl`（系统自带）

### API 凭证配置

```bash
cp .claude/skills/paper-pipeline/.env.example .claude/skills/paper-pipeline/.env
# 编辑 .env，填入真实 token
```

| 变量 | 说明 | 默认值 |
|:---|:---|:---|
| `MINERU_URL` | MinerU API 端点 | USTC 地址 |
| `MINERU_TOKEN` | MinerU API Token | — |
| `LLM_URL` | LLM API 端点（OpenAI 兼容） | USTC 地址 |
| `LLM_TOKEN` | LLM API Token | — |
| `LLM_MODEL` | 模型名称 | `deepseek-v4-flash-ascend` |
| `ZOTERO_DB` | Zotero SQLite 路径 | `/mnt/c/Users/swt/Zotero/zotero.sqlite` |
| `ZOTERO_STORE` | Zotero 附件目录 | `/mnt/c/Users/swt/Zotero/storage` |
| `UNPAYWALL_EMAIL` | Unpaywall API 邮箱（任意真实邮箱） | — |

### 目录结构

```
docs/papers/
├── references/          # 论文笔记（含 YAML frontmatter）
├── storage/             # PDF 及 MinerU 输出（已加入 .gitignore）
│   └── {类型}/{会议}/{年}/{key}/
│       ├── {key}.pdf
│       └── mineru-output/{key}.md
└── .claude/skills/paper-pipeline/
    ├── pp.py                 # 统一 CLI 入口
    ├── pipeline/             # Python 包
    │   ├── env.py            # 配置加载
    │   ├── common.py         # 共用工具函数
    │   ├── doi.py            # CrossRef DOI 查询
    │   ├── fetch.py          # PDF 自动下载
    │   ├── sync.py           # Zotero PDF 同步
    │   ├── convert.py        # MinerU 转换
    │   ├── note.py           # LLM 笔记生成
    │   └── status.py         # 状态看板
    └── pipeline-status.md    # 生成的状态看板
```

---

## 命令速查

```bash
PP=".claude/skills/paper-pipeline/pp.py"

# 查看帮助
python3 $PP --help
python3 $PP <command> --help
```

### `doi` — CrossRef 自动补充 DOI

```bash
python3 $PP doi <key>         # 单篇
python3 $PP doi               # 所有缺 DOI 的论文
python3 $PP doi --dry-run     # 预览
```

### `fetch` — 自动下载 PDF（IACR ePrint → Unpaywall → Sci-Hub 链接）

```bash
python3 $PP fetch <key>
python3 $PP fetch --all
python3 $PP fetch --dry-run --all
```

### `sync` — 从 Zotero 同步 PDF

```bash
python3 $PP sync <key>
python3 $PP sync --all
python3 $PP sync --dry-run --all
```

### `convert` — MinerU PDF → Markdown

```bash
python3 $PP convert <key>
python3 $PP convert --all
python3 $PP convert --all --interval 120   # 批量，间隔 120s
```

后台运行：
```bash
nohup python3 -u $PP convert --all --interval 120 > /tmp/mineru.log 2>&1 &
tail -f /tmp/mineru.log
```

### `note` — LLM 生成结构化笔记

```bash
python3 $PP note <key>
python3 $PP note --dry-run <key>
python3 $PP note --all --interval 30
```

后台运行：
```bash
nohup python3 -u $PP note --all > /tmp/note.log 2>&1 &
```

### `status` — 更新状态看板

```bash
python3 $PP status
```

---

## 典型完整流程（单篇）

```bash
KEY=bunz2018bulletproofs
PP=".claude/skills/paper-pipeline/pp.py"

python3 $PP doi $KEY
python3 $PP fetch $KEY       # 或通过 Zotero 手动添加后 sync
python3 $PP convert $KEY
python3 $PP note $KEY
```

## 批量处理建议顺序

```bash
PP=".claude/skills/paper-pipeline/pp.py"

# 1. 补全 DOI
python3 $PP doi

# 2. 自动下载 PDF（约 51% 的密码学论文可从 ePrint 获取）
python3 $PP fetch --all

# 3. Zotero 手动补充剩余 PDF，然后同步
python3 $PP sync --all

# 4. 后台批量 MinerU 转换
nohup python3 -u $PP convert --all --interval 120 > /tmp/mineru.log 2>&1 &

# 5. 后台批量生成笔记
nohup python3 -u $PP note --all > /tmp/note.log 2>&1 &

# 6. 更新状态看板
python3 $PP status
```
