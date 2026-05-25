---
name: paper-pipeline
description: >
  论文笔记自动化流水线。给定一个 citation key，依次执行：
  1. 从 Zotero storage 同步 PDF（sync_pdf.py）
  2. 调用 USTC MinerU API 将 PDF 转换为 Markdown（convert_pdf.py）
  3. 调用 USTC LLM API 生成结构化中文笔记，写入 references/ 对应文件的 ## 笔记 字段（generate_note.py）
  触发词：处理论文、生成笔记、paper pipeline、处理 <key>、为 <key> 生成笔记
allowed-tools: Bash(python3 .claude/skills/paper-pipeline/sync_pdf.py *), Bash(python3 .claude/skills/paper-pipeline/convert_pdf.py *), Bash(python3 .claude/skills/paper-pipeline/generate_note.py *)
---

# Paper Pipeline

给定一个 citation key，自动完成 PDF 同步 → MinerU 转换 → LLM 笔记生成的完整流程。

所有脚本位于 `.claude/skills/paper-pipeline/`，MinerU API 文档见同目录下 `mineru.md`。

## 使用方式

用户说：
- "处理 bunz2018bulletproofs"
- "为 sun2025committed 生成笔记"
- "run paper pipeline for groth2016"

## 执行步骤

收到 citation key 后，按顺序执行以下三步，**每步执行前告知用户当前步骤，失败时停止并报告原因**。

### Step 1：同步 PDF

```bash
python3 .claude/skills/paper-pipeline/sync_pdf.py <key>
```

- 成功（输出包含 `✓` 或 `已存在`）→ 继续
- 失败（输出包含 `未找到`）→ 告知用户该论文在 Zotero 中没有 PDF，需要先在 Zotero 中添加，停止流程

### Step 2：MinerU 转换

```bash
python3 .claude/skills/paper-pipeline/convert_pdf.py <key>
```

- 成功（输出包含 `✓` 或 `已存在`）→ 继续
- 失败 → 告知用户 MinerU API 不可用，停止流程

### Step 3：LLM 生成笔记

```bash
python3 .claude/skills/paper-pipeline/generate_note.py <key>
```

- 成功（输出包含 `✓`）→ 告知用户完成，并说明笔记已写入的文件路径
- 失败 → 告知用户 LLM API 不可用

## 完成后

告知用户：
1. 每步的执行结果（成功/跳过/失败）
2. 最终笔记写入的路径：`references/{类型}/{会议}/{年}/{key}.md`
3. 如有任何步骤失败，说明原因和下一步建议
