# Paper Pipeline

论文笔记自动化流水线：Zotero PDF 同步 → MinerU Markdown 转换 → LLM 结构化笔记生成。

---

## 环境配置

### 依赖

- Python 3.10+（脚本使用 `str | None` 类型注解）
- PyYAML（唯一第三方库）：`pip install pyyaml`
- `curl`（系统自带，用于调用 MinerU / LLM API）

### API 凭证与路径配置

所有凭证和路径统一在 repo 根目录的 `.env` 文件中配置（不入 git）：

```bash
cp .claude/skills/paper-pipeline/.env.example .claude/skills/paper-pipeline/.env
# 编辑 .env，填入真实 token 和本机 Zotero 路径
```

`.env` 支持的变量（见 `.env.example`）：

| 变量 | 说明 | 默认值 |
|:---|:---|:---|
| `MINERU_URL` | MinerU API 端点 | USTC 地址 |
| `MINERU_TOKEN` | MinerU API Token | — |
| `LLM_URL` | LLM API 端点（OpenAI 兼容） | USTC 地址 |
| `LLM_TOKEN` | LLM API Token | — |
| `LLM_MODEL` | 模型名称 | `deepseek-v4-flash-ascend` |
| `ZOTERO_DB` | Zotero SQLite 路径 | `/mnt/c/Users/swt/Zotero/zotero.sqlite` |
| `ZOTERO_STORE` | Zotero 附件目录 | `/mnt/c/Users/swt/Zotero/storage` |

配置由 `env.py` 统一加载，优先级：系统环境变量 > `.env` 文件 > 内置默认值。

### 项目目录约定

```
docs/papers/
├── references/          # 论文笔记 Markdown（含 YAML frontmatter）
├── storage/             # PDF 及 MinerU 输出（已加入 .gitignore）
│   └── {类型}/{会议}/{年}/{key}/
│       ├── {key}.pdf
│       └── mineru-output/{key}.md
└── .claude/skills/paper-pipeline/
    └── pipeline-status.md   # 流水线状态看板（由 pipeline_status.py 生成）
```

---

## 命令速查

### 1. `sync_pdf.py` — 从 Zotero 同步 PDF

```bash
# 同步单篇
python3 .claude/skills/paper-pipeline/sync_pdf.py <key>

# 同步所有缺 PDF 的论文
python3 .claude/skills/paper-pipeline/sync_pdf.py --all

# 预览，不实际复制
python3 .claude/skills/paper-pipeline/sync_pdf.py --dry-run --all
```

通过 Zotero SQLite 按论文标题匹配 PDF，验证文件实际可访问后复制到 `storage/`。

---

### 2. `convert_pdf.py` — MinerU PDF → Markdown

```bash
# 转换单篇
python3 .claude/skills/paper-pipeline/convert_pdf.py <key>

# 批量转换所有有 PDF 但缺 mineru-output 的论文（默认间隔 120s）
python3 .claude/skills/paper-pipeline/convert_pdf.py --all

# 自定义间隔（秒），后台运行
nohup python3 -u .claude/skills/paper-pipeline/convert_pdf.py --all --interval 120 \
  > /tmp/mineru_batch.log 2>&1 &

# 实时查看进度
tail -f /tmp/mineru_batch.log

# 预览待转换列表
python3 .claude/skills/paper-pipeline/convert_pdf.py --dry-run --all
```

幂等：已存在 `mineru-output/{key}.md` 的论文自动跳过。首次失败自动重试一次。

---

### 3. `generate_note.py` — LLM 生成结构化笔记

```bash
# 生成并写入笔记（替换 ## 笔记 章节）
python3 .claude/skills/paper-pipeline/generate_note.py <key>

# 预览生成内容，不写文件
python3 .claude/skills/paper-pipeline/generate_note.py --dry-run <key>
```

读取 `storage/.../mineru-output/{key}.md`，调用 `deepseek-v4-flash-ascend`，将生成的笔记写入 `references/` 对应文件的 `## 笔记` 章节。

笔记结构：背景与动机 / 相关工作 / 核心技术与方案 / 核心公式与流程 / 实验结果 / 局限性与开放问题 / 强关联论文（含 Google Scholar 链接）。

---

### 4. `check_missing.py` — 生成缺失 PDF 列表

```bash
# 生成 / 更新 missing-pdfs.md（保留上次 Zotero 查询结果，速度快）
python3 .claude/skills/paper-pipeline/check_missing.py

# 重新查询 Zotero，更新所有状态
python3 .claude/skills/paper-pipeline/check_missing.py --rescan
```

输出 `missing-pdfs.md`（repo 根目录），包含 Google Scholar 链接，状态分三类：
- `⬜` 待添加到 Zotero
- `📥` Zotero 已有，运行 `sync_pdf.py --all` 即可同步
- `✅` 已在 `storage/` 中

---

### 5. `pipeline_status.py` — 全流水线状态看板

```bash
python3 .claude/skills/paper-pipeline/pipeline_status.py
```

扫描全部 391 篇论文，输出 `.claude/skills/paper-pipeline/pipeline-status.md`，按完成度分组：

| 组 | 含义 |
|:---|:---|
| ✅ 全部完成 | PDF + MinerU + 笔记均就绪 |
| 📝 待生成笔记 | PDF + MinerU 就绪，缺笔记 |
| ⚙️ 待 MinerU 转换 | 有 PDF，缺 mineru-output |
| 📥 Zotero 待同步 | Zotero 有 PDF，未同步到 storage |
| ⬜ 待添加 PDF | 无 PDF |

---

## 典型完整流程（单篇）

```bash
KEY=bunz2018bulletproofs

python3 .claude/skills/paper-pipeline/sync_pdf.py $KEY
python3 .claude/skills/paper-pipeline/convert_pdf.py $KEY
python3 .claude/skills/paper-pipeline/generate_note.py $KEY
```

也可直接对 Claude Code 说「处理 `<key>`」，skill 会自动按顺序执行三步。

---

## 批量处理建议顺序

```bash
# Step 1: 同步所有 Zotero 已有 PDF
python3 .claude/skills/paper-pipeline/sync_pdf.py --all

# Step 2: 后台批量 MinerU 转换（2分钟/篇，约5小时跑完158篇）
nohup python3 -u .claude/skills/paper-pipeline/convert_pdf.py --all --interval 120 \
  > /tmp/mineru_batch.log 2>&1 &

# Step 3: 对已完成 MinerU 的论文逐篇生成笔记（通过 Claude Code skill 触发）

# Step 4: 更新看板
python3 .claude/skills/paper-pipeline/pipeline_status.py
```
