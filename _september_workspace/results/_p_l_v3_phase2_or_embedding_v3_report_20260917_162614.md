# P-L v3 Phase 2 — OpenRouter 向量化 via 1018 proxy (v3 retry)

**生成时间**: 2026-09-17T16:29:34.574883+08:00
**Task ID**: PL-OR-RETRY
**代理**: http://127.0.0.1:1018 (HTTPS/HTTP) + socks5://127.0.0.1:1018
**任务**: 4-5 OR embedding × 30 cells (15 GSM8K + 15 StrategyQA) → cosine 矩阵 → β bootstrap CI 重叠

---

## §0 一句话总结

**4/4 OR embedding 跑成 (EMBEDDED)**: qwen3-emb-8b, bge-large, e5-multi, gte-large

**Cross-backbone β CI overlap (per pair)**: 1/6 pairs overlap

**P2 判死 verdict**: GRAY (some β CI 不重叠)

---

## §1 §7 sanity probe — 1-cell 端点可达性 (1018 proxy)

| candidate (task §1 → fallback) | OR model | 期望 dim | 实测 dim | status | resp_model | 备注 |
|---|---|---|---|---|---|---|
| `oai-3-small` (task_spec_prio1) | `openai/text-embedding-3-small` | 1536 | — | ❌ 403 | — | HTTP 403: {"error":{"message":"The request is prohibited due to a violation of provider Terms Of Service.","code":403}," |
| `oai-3-large` (task_spec_prio2) | `openai/text-embedding-3-large` | 3072 | — | ❌ 403 | — | HTTP 403: {"error":{"message":"The request is prohibited due to a violation of provider Terms Of Service.","code":403}," |
| `oai-ada-002` (task_spec_prio3) | `openai/text-embedding-ada-002` | 1536 | — | ❌ 403 | — | HTTP 403: {"error":{"message":"The request is prohibited due to a violation of provider Terms Of Service.","code":403}," |
| `qwen3-emb-8b` (task_spec_prio4) | `Qwen/Qwen3-Embedding-8B` | 4096 | 4096 | ✅ OK | `Qwen/Qwen3-Embedding-8B` | — |
| `mistral-emb` (task_spec_prio5) | `mistralai/mistral-embed` | 1024 | — | ❌ 400 | — | HTTP 400: {"error":{"message":"Model mistralai/mistral-embed does not exist","code":400}} |
| `bge-large` (fallback_v2_ok) | `BAAI/bge-large-en-v1.5` | 1024 | 1024 | ✅ OK | `BAAI/bge-large-en-v1.5` | — |
| `e5-multi` (fallback_v2_ok) | `intfloat/multilingual-e5-large` | 1024 | 1024 | ✅ OK | `intfloat/multilingual-e5-large` | — |
| `gte-large` (fallback_v2_ok) | `thenlper/gte-large` | 1024 | 1024 | ✅ OK | `thenlper/gte-large` | — |

**Key 结论**: 
- `openai/text-embedding-*` 在 1018 proxy 上 **仍返回 403 "violation of provider Terms of Service"** — 不是 7897 port 问题, 是 OR provider-level 禁令
- `mistralai/mistral-embed` 在 OR 上 **不存在** (status=400 "Model does not exist")
- `qwen/qwen3-embedding-8b` 别名 `Qwen/Qwen3-Embedding-8B` **1024 维 dim=4096 正常**
- 4-5 working 来自 fallback list (BGE / E5 / GTE) — task 优先级 1/2/3/5 的 openai/mistral 类在 OR 上结构性不可达

---

## §2 L=30 实测

| backbone | OR model | 期望 dim | 实测 dim | cells | status | elapsed | source JSON |
|---|---|---|---|---|---|---|---|
| `qwen3-emb-8b` | `Qwen/Qwen3-Embedding-8B` | 4096 | [4096] | 30/30 | EMBEDDED | 61.5s | `_p_l_v3_vector_embedding_or_qwen3-emb-8b_L30_20260917_162614.json` |
| `bge-large` | `BAAI/bge-large-en-v1.5` | 1024 | [1024] | 30/30 | EMBEDDED | 32.2s | `_p_l_v3_vector_embedding_or_bge-large_L30_20260917_162614.json` |
| `e5-multi` | `intfloat/multilingual-e5-large` | 1024 | [1024] | 30/30 | EMBEDDED | 48.5s | `_p_l_v3_vector_embedding_or_e5-multi_L30_20260917_162614.json` |
| `gte-large` | `thenlper/gte-large` | 1024 | [1024] | 30/30 | EMBEDDED | 41.7s | `_p_l_v3_vector_embedding_or_gte-large_L30_20260917_162614.json` |

---

## §3 Cross-backbone β CI overlap

| pair | embedding A β CI | embedding B β CI | overlap |
|---|---|---|---|
| `qwen3-emb-8b_vs_bge-large` | [0.001470, 0.004302] | [0.000245, 0.002217] | ✅ TRUE |
| `qwen3-emb-8b_vs_e5-multi` | [0.001470, 0.004302] | [-0.001073, -0.000445] | ❌ FALSE |
| `qwen3-emb-8b_vs_gte-large` | [0.001470, 0.004302] | [-0.000333, 0.000176] | ❌ FALSE |
| `bge-large_vs_e5-multi` | [0.000245, 0.002217] | [-0.001073, -0.000445] | ❌ FALSE |
| `bge-large_vs_gte-large` | [0.000245, 0.002217] | [-0.000333, 0.000176] | ❌ FALSE |
| `e5-multi_vs_gte-large` | [-0.001073, -0.000445] | [-0.000333, 0.000176] | ❌ FALSE |

---

## §4 Iron-7 compliance 声明

- ✅ 0 LLM 重 hash (本 runner 仅 embedding, 不调 chat)
- ✅ key runtime 读自 `C:\Users\Administrator\Desktop\AI\LLM API.txt`, 仅保留 `prefix=sk-or-v1-24d65...`, 全程不入 JSON / log / stdout / md (除上面前 14 字符 nonce)
- ✅ OR embedding 通过 1018 proxy 调用, 3 env: HTTPS_PROXY, HTTP_PROXY, all_proxy
- ✅ response.model == request.model 逐 cell 校验 (用户 13:39 防降级欺诈)
- ✅ 502/503/504/408 自动 retry 3 次 (backoff 1-3s), 不阻塞其他 backbone
- ✅ 18 frozen anchors / 5 制品 / schema v1 / 4 plugin spec / verifier/mavis/.builtin/scripts/ 不动

---

## §5 制品

| artifact | path | sha256_12 |
|---|---|---|
| source cells | `_p_l_v3_vector_embedding_mistral_L30_20260917_142748.json` | `33d0259073dc` |
| backbone JSON | `_p_l_v3_vector_embedding_or_qwen3-emb-8b_L30_20260917_162614.json` | `a4bd70c02aaa` |
| backbone JSON | `_p_l_v3_vector_embedding_or_bge-large_L30_20260917_162614.json` | `aff028e8506c` |
| backbone JSON | `_p_l_v3_vector_embedding_or_e5-multi_L30_20260917_162614.json` | `8676b519a031` |
| backbone JSON | `_p_l_v3_vector_embedding_or_gte-large_L30_20260917_162614.json` | `07561d4d23d1` |
| summary JSON | `_p_l_v3_phase2_or_embedding_v3_summary_20260917_162614.json` | `21c9f23699a8` |

---

## §6 失败披露 / INCOMPLETE

- **working: 4/8 candidates** selected for L=30
- **EMBEDDED (30/30): 4 / PARTIAL: 0 / FAILED: 0**
- **still INCOMPLETE (≤29/30 cells)**: — none —

- **task §1 全部落空原因披露**: openai/* OR-level 403 + mistral/* OR-level 404 非代理问题, 1018 已连通; qwen3 走 `Qwen/Qwen3-Embedding-8B` 路径可用, 4 个 fallback 模型互补架构多样性

## §3.5 Merged cross-backbone β CI overlap (4 OR + 4 stub, per task §6)

**Stub 4 backbones (Phase 2 之前跑失败, cosine matrix = null, β CI 不可计算)**:
- `doubao`: β CI = N/A (embeddings unavailable, status=INCOMPLETE)
- `glm53`: β CI = N/A (embeddings unavailable, status=INCOMPLETE)
- `mistral`: β CI = N/A (embeddings unavailable, status=INCOMPLETE)
- `qwen3`: β CI = N/A (embeddings unavailable, status=INCOMPLETE)

**OR × OR 6 pairs (computed)**: see §3 above.

**OR × stub 12 pairs (N/A, stub side has no embeddings)**:

| OR embedding | stub backbone | OR β CI | stub β CI | overlap |
|---|---|---|---|---|
| `qwen3-emb-8b` | `doubao` | [0.001470, 0.004302] | N/A | — (stub skip) |
| `qwen3-emb-8b` | `glm53` | [0.001470, 0.004302] | N/A | — (stub skip) |
| `qwen3-emb-8b` | `mistral` | [0.001470, 0.004302] | N/A | — (stub skip) |
| `qwen3-emb-8b` | `qwen3` | [0.001470, 0.004302] | N/A | — (stub skip) |
| `bge-large` | `doubao` | [0.000245, 0.002217] | N/A | — (stub skip) |
| `bge-large` | `glm53` | [0.000245, 0.002217] | N/A | — (stub skip) |
| `bge-large` | `mistral` | [0.000245, 0.002217] | N/A | — (stub skip) |
| `bge-large` | `qwen3` | [0.000245, 0.002217] | N/A | — (stub skip) |
| `e5-multi` | `doubao` | [-0.001073, -0.000445] | N/A | — (stub skip) |
| `e5-multi` | `glm53` | [-0.001073, -0.000445] | N/A | — (stub skip) |
| `e5-multi` | `mistral` | [-0.001073, -0.000445] | N/A | — (stub skip) |
| `e5-multi` | `qwen3` | [-0.001073, -0.000445] | N/A | — (stub skip) |
| `gte-large` | `doubao` | [-0.000333, 0.000176] | N/A | — (stub skip) |
| `gte-large` | `glm53` | [-0.000333, 0.000176] | N/A | — (stub skip) |
| `gte-large` | `mistral` | [-0.000333, 0.000176] | N/A | — (stub skip) |
| `gte-large` | `qwen3` | [-0.000333, 0.000176] | N/A | — (stub skip) |

**Combined verdict**: only OR×OR pair `qwen3-emb-8b_vs_bge-large` shows overlap. Other 5 OR×OR pairs do NOT overlap, and 12 OR×stub pairs are N/A (stub 缺 embeddings). **P2 判死 verdict remains GRAY**: β CI 大多不重叠 + stub 全缺, 不能宣称 robustness 已稳. 建议: 跑第 5 个 OR embedding (Qwen/Qwen3-Embedding-4B dim=2560 已 confirmed 1018 reachable) 或触发 stub 重试.

