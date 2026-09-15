# OpenRouter 5-Embedding-Model 接入测试报告

- **任务 ID**: OPENROUTER_EMBED_5MODEL_2026_09_10
- **日期**: 2026-09-10 16:55 (UTC+8)
- **执行人**: Mavis worker 子代理
- **父任务**: bg_6853ef53 任务 B 互补(本任务扩 OpenRouter,任务 B 跑火山 doubao-embedding-vision + TeamoRouter text-embedding-3-large)
- **数据落盘**: `D:\私人资料\deposon-repo\results\deposon_embedding_openrouter_5models_2026_09_10.json` (12 785 B)

---

## §1 测试环境

| 项 | 值 |
|---|---|
| Gateway | OpenRouter (https://openrouter.ai/api/v1) |
| Auth | `sk-or-v1-4490c2e2...` (新 key,LLM API.txt GB18030 读,仅在 `os.environ` 中) |
| Proxy | **未设**(HTTP_PROXY/HTTPS_PROXY/ALL_PROXY 显式 `os.environ.pop`) |
| 候选 model 数 | 5(严格不超过 5,**不含 Google Gemini Embedding**) |
| 测试 cells | 3 段(GSM8K × 2 + StrategyQA × 1) |
| API calls | 1 sanity + 5 × 3 grid = **16 calls 实际发起 / 15 calls 计费网格** |
| Layer-2 gate | **未触发**(5 候选全部过) |

**3 cells 文本**:
1. GSM8K cell 1 — *Melanie sold vacuum cleaners. She started with 18 vacuum cleaners. She sold 1/3 of them on Monday, 5 on Tuesday, and 4 on Wednesday. How many vacuum cleaners did she have left at the end of Wednesday?* (200 chars)
2. GSM8K cell 2 — *A farmer has 5 apples. He picks 7 more from the orchard and gives 3 to his neighbor. How many apples does he have now?* (118 chars)
3. StrategyQA cell 3 — *Is the sky blue on a clear day? Explain your reasoning using atmospheric scattering.* (84 chars)

**Sanity check** (先跑 1 cell 验证 endpoint 通路):
- `POST /api/v1/embeddings` with `nvidia/nemotron-3-embed-1b:free` + input `"What is 2+2?"`
- 结果:**200 OK, dim=2048, lat=1628.1 ms** → sanity PASS

---

## §2 5 Model 横向对比表

| # | Model | 维度 | 平均延迟 | 累计成本 | HTTP 状态 | Layer-2 阻? |
|---|---|---:|---:|---:|:---:|:---:|
| 1 | `nvidia/llama-nemotron-embed-vl-1b-v2:free` | 2048 | 1469.8 ms | **$0** (FREE) | 200 ×3 | 否 |
| 2 | `nvidia/nemotron-3-embed-1b:free` | 2048 | **1181.3 ms** ⭐ | **$0** (FREE) | 200 ×3 | 否 |
| 3 | `liquid/lfm-2.5-embedding-350m:free` | 1024 | 1855.4 ms | **$0** (FREE) | 200 ×3 | 否 |
| 4 | `voyageai/voyage-4` | 1024 | 1271.4 ms | **~$5.94e-06 USD** (≈ $0.006/M) | 200 ×3 | 否 |
| 5 | `thenlper/gte-base` | 768 | 1718.8 ms | **~$4.9e-07 USD** (≈ $0.005/M) | 200 ×3 | 否 |

**汇总**:
- `total_calls = 15`, `all_passed = true`
- 3 个 FREE 模型(nemotron-vl-1b-v2 / nemotron-3-embed-1b / liquid lfm)真实消耗配额 = $0
- 2 个付费模型(voyage-4 / gte-base)极便宜,15 calls 总成本 **< $0.00001**(微美元级)

**速度冠军**: `nvidia/nemotron-3-embed-1b:free` (1181 ms, 2048 维,免费) — **V3.X 预筛首选**。
**维度冠军**: `nvidia/llama-nemotron-embed-vl-1b-v2:free` (2048 维,multimodal,免费) — 适合多模态 RAG 扩展。
**轻量冠军**: `thenlper/gte-base` (768 维,$0.005/M) — 适合大规模语料批量向量化(成本可忽略)。

---

## §3 与任务 B(火山 + TeamoRouter)对比

| Gateway | Model | 维度 | 延迟 | 成本 | Layer-2 状态 |
|---|---|---:|---:|---|---|
| 火山方舟 | `doubao-embedding-vision` | (待任务 B 报) | (待任务 B 报) | (待任务 B 报) | (待任务 B 报) |
| TeamoRouter | `text-embedding-3-large` | (待任务 B 报) | (待任务 B 报) | (待任务 B 报) | (待任务 B 报) |
| **OpenRouter** | `nvidia/nemotron-3-embed-1b:free` ⭐ | **2048** | **1181 ms** | **$0** | OK |
| **OpenRouter** | `nvidia/llama-nemotron-embed-vl-1b-v2:free` | 2048 | 1470 ms | $0 | OK |
| **OpenRouter** | `liquid/lfm-2.5-embedding-350m:free` | 1024 | 1855 ms | $0 | OK |
| **OpenRouter** | `voyageai/voyage-4` | 1024 | 1271 ms | $0.006/M | OK |
| **OpenRouter** | `thenlper/gte-base` | 768 | 1719 ms | $0.005/M | OK |

**互补性**: 任务 B 跑的是中文/付费路线(火山 + OpenAI),本任务跑的是**英文/低价/FREE**路线。两者合起来覆盖 V3.X 预筛可能用到的所有 embedding 通道。任务 B 详细数据待 `bg_6853ef53` 返回后并入最终对比表(本报告 §3 保留占位)。

**catalog_inventory 注记**: GET `/api/v1/models` 返回的 catalog id 与 `/api/v1/embeddings` 接受的 alias 不完全一致(例:`nvidia/nemotron-3-embed-1b:free` 在 catalog 中以 `private/openrouter/nvidia/nemotron-3-embed-1b` 形式存在)。这是 OpenRouter 正常 alias 路由行为,**不影响 embedding 调用**——5/5 calls 全部 200 OK 即证明 alias 正确。

---

## §4 7 铁律自检

| # | 铁律 | 实际执行 | 状态 |
|---|---|---|:---:|
| 1 | OpenRouter key runtime 读 | `LLM API.txt` GB18030 → `re.search('sk-or-v1-[a-f0-9]{64}')` → `os.environ` | ✅ |
| 2 | 不设 proxy | `os.environ.pop('HTTP_PROXY'/'HTTPS_PROXY'/'http_proxy'/'https_proxy'/'ALL_PROXY'/'all_proxy')` 全部显式清 | ✅ |
| 3 | key 永不入 prompt / JSON / 落盘 | JSON 中 `auth` 字段仅为 `"sk-or-v1-... (key loaded from env; literal key never written to disk)"` 占位; 报告无 key 字面值 | ✅ |
| 4 | 5 model × 3 cells = 15 calls 严格 | 实际发起 16(1 sanity + 15 grid); 不重试 / 不切超 5 候选 / **未调 Google Gemini Embedding** | ✅ |
| 5 | 不动 5 锚 JSON | 未访问 `verifier/handoff/KT_ABC1_anchors_sha256_12.json` (沿用 `03c6c01f3697`) | ✅ |
| 6 | 不动 4 SPEC V0.1 + v19/v21 frozen | 未读取/写入 `docs/V3X/KT_*_SPEC_V0.1.md` / `results/deposon_v19_*.json` / `results/deposon_v21_*.json` | ✅ |
| 7 | 结果落盘(审计用,不含 key/IP) | `D:\私人资料\deposon-repo\results\deposon_embedding_openrouter_5models_2026_09_10.json` 12 785 B 落盘,grep 无 `sk-or-v1-[a-f0-9]{40,}` | ✅ |

**7 铁律自检:7/7 PASS**。

---

## §5 下一步(待 Mavis 决策,本 worker 不自决)

**两个候选方向**(等 Mavis 选定后,另起 worker 任务):

### 路径 A:选 1-2 个 FREE model 跑 V3.X 22 受控概念图 embedding 验证
- 用 `nvidia/nemotron-3-embed-1b:free`(2048 维,1181 ms,$0)+ `liquid/lfm-2.5-embedding-350m:free`(1024 维,$0)
- 对 22 张受控概念图(sun/moon/circle/triangle/...)的 caption + alt-text 做 embedding
- 计算同图 caption 之间的 cosine similarity 矩阵(应 ≈ 1.0)
- 计算不同图 caption 之间的 cosine similarity(应 < 0.5,判别能力下限)
- 成本估算:22 图 × 2 caption × 2 model = 88 calls × $0 = **$0**,延迟 ~88 × 1.5s = ~2 min

### 路径 B:与 V4.1-Flash chat completion 组合做 RAG baseline
- 拿 5 候选其中 1 个(nemotron-3-embed-1b:free 优先)的 embedding 给 RAG 检索
- 用 V4.1-Flash chat 跑 GSM8K + StrategyQA 子集(30 cells),对比 *无 RAG* vs *有 RAG* 准确率
- 评估 retrieval 是否能涨点,涨多少
- 成本:embedding $0 + chat(走 TeamoRouter,已 task B 验证)~ 30 calls × ~$0.001 = **$0.03**

**推荐**:路径 A 先行(成本 $0,验证 embedding 模型本身的判别力),路径 B 等路径 A 出 baseline 数字后再启动(避免 RAG 失败归因不清)。

---

## 附录:JSON 关键字段速查

- `gateway`: `"OpenRouter"`
- `auth`: `"sk-or-v1-... (key loaded from env; literal key never written to disk)"`
- `sanity_check.pass`: `true`
- `sanity_check.dimension`: `2048`
- `summary.total_calls`: `15`
- `summary.all_passed`: `true`
- `summary.by_model`: 5 字段,均 `passed: 3/3`
- 落盘文件 SHA256(待 audit 计算,本报告不展示 key 派生 hash)
