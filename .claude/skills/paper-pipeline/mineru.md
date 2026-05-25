
## 一、USTC MinerU API（推荐优先使用）

**Base URL:** `https://api.llm.ustc.edu.cn/mineru`  
**Token:** `sk-fjFmIE5cwKSgzC2gvUlKCQ`  
**认证方式:** `Authorization: Bearer <token>`（OpenAI 兼容格式）  
**服务器版本:** 3.1.15（后端部署于 `http://114.214.240.30:30001`）

### 健康检查

```bash
curl -s https://api.llm.ustc.edu.cn/mineru/health \
  -H "Authorization: Bearer sk-fjFmIE5cwKSgzC2gvUlKCQ"
```

### 同步转换（PDF → Markdown，推荐）

```bash
curl -s -X POST \
  -H "Authorization: Bearer sk-fjFmIE5cwKSgzC2gvUlKCQ" \
  -F "files=@paper.pdf" \
  -F "return_md=true" \
  "https://api.llm.ustc.edu.cn/mineru/file_parse"
```

### 异步模式（大文件）

```bash
# 提交任务
curl -s -X POST \
  -H "Authorization: Bearer sk-fjFmIE5cwKSgzC2gvUlKCQ" \
  -F "files=@paper.pdf" \
  -F "return_md=true" \
  "https://api.llm.ustc.edu.cn/mineru/tasks"

# 查状态
curl -s https://api.llm.ustc.edu.cn/mineru/tasks/{task_id} \
  -H "Authorization: Bearer sk-fjFmIE5cwKSgzC2gvUlKCQ"

# 取结果
curl -s https://api.llm.ustc.edu.cn/mineru/tasks/{task_id}/result \
  -H "Authorization: Bearer sk-fjFmIE5cwKSgzC2gvUlKCQ"
```

### 可用后端参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `backend` | string | `hybrid-auto-engine` | 处理引擎 |
| `formula_enable` | boolean | `true` | 公式识别 |
| `table_enable` | boolean | `true` | 表格识别 |
| `image_analysis` | boolean | `true` | 图片分析 |
| `start_page_id` | int | `0` | 起始页 |
| `end_page_id` | int | `99999` | 结束页 |
| `return_md` | boolean | `true` | 返回 Markdown |
| `return_images` | boolean | `false` | 返回提取的图片 |
| `lang_list` | string[] | `["ch"]` | 语言包（`en`/`ch`/`japan`/`korean` 等） |

### backend 可选值

| 值 | 说明 |
|----|------|
| `pipeline` | 流水线模型，无幻觉，多语言 |
| `vlm-auto-engine` | VLM 高精度，本地计算，仅中英文 |
| `vlm-http-client` | VLM 高精度，远程计算，仅中英文 |
| `hybrid-auto-engine` | ✅ **默认/推荐**，混合引擎，本地计算，多语言 |
| `hybrid-http-client` | 混合引擎，远程+部分本地计算，多语言 |

### 提取 Markdown 的 jq 命令

```bash
... | jq -r '.results | to_entries[] | .value.md_content'
```

### API 文档地址

```
https://api.llm.ustc.edu.cn/mineru/openapi.json    # OpenAPI 规范
https://api.llm.ustc.edu.cn/mineru/docs             # Swagger UI
```

---


## 二、官方 MinerU API（作为 USTC 的 Fallback）

**Base URL:** `https://api.mineru.cc/`  
**Token:** 已在 `~/.mineru/config.yaml` 中配置  
**CLI 工具:** `mineru-open-api`（需先安装 `npm install -g mineru-open-api`）

---

### Quick Start（免费，无需 Token）

```bash
mineru-open-api flash-extract paper.pdf           # 输出到 stdout
mineru-open-api flash-extract paper.pdf -o ./out/ # 保存到文件
```

限制：10MB / 20 页，仅 Markdown 输出，仅 pipeline 模型。

### 完整转换（需要 Token）

```bash
# 先配置 Token
export MINERU_TOKEN="your-token"
# 或
mineru-open-api auth

# 转换
mineru-open-api extract paper.pdf                 # Markdown 到 stdout
mineru-open-api extract paper.pdf -o ./out/       # 保存
mineru-open-api extract paper.pdf -f html         # HTML 格式
mineru-open-api extract paper.pdf -f md,docx      # 多格式
mineru-open-api extract *.pdf -o ./results/       # 批量
```

### 常用参数

| 参数 | 说明 |
|------|------|
| `-o ./out/` | 输出目录 |
| `-f md,html,latex,docx,json` | 输出格式 |
| `--model vlm` | 使用 VLM 高精度模型 |
| `--model pipeline` | 使用 pipeline 无幻觉模型 |
| `--language en` | 语言（默认 ch） |
| `--pages 1-10` | 页码范围 |
| `--timeout 900` | 超时秒数 |
| `--concurrency 4` | 并发数 |
| `--ocr` | 启用 OCR |
| `--formula` | 公式识别 |

### Web 页面提取

```bash
mineru-open-api crawl https://example.com/article
```

### 凭证管理

```bash
mineru-open-api auth               # 交互式设置
mineru-open-api auth --verify      # 校验当前 Token
mineru-open-api auth --show        # 显示 Token 来源
```

---

## 三、Fallback 策略（推荐流程）

```
目标: PDF → Markdown

1. 尝试 USTC 接口
   curl -s -X POST -H "Authorization: Bearer sk-xxx" \
     -F "files=@paper.pdf" -F "return_md=true" \
     https://api.llm.ustc.edu.cn/mineru/file_parse
       
   ↓ 若失败 (HTTP 非 200 或 timeout)

2. 回退到官方 CLI
   mineru-open-api extract paper.pdf -o ./out/
```