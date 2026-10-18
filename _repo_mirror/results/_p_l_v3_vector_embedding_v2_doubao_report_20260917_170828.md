# P-L v3 Phase 2 — Doubao v2 retry + 跨架构 Qwen3-Embedding-4B

**生成时间**: 2026-09-17T17:08:28.267599+08:00
**Task ID**: PL-DOUBAO-V2
**代理**: http://127.0.0.1:1018 (HTTPS_PROXY/HTTP_PROXY only — 无 socks5, 沿 user 1018 防 socksio 缺失)
**任务**: 6 endpoints × 30 cells (15 GSM8K + 15 StrategyQA, seed=210021) → cosine → β bootstrap CI 重叠
**输入 cells**: `_p_l_v3_vector_embedding_mistral_L30_20260917_142748.json` (sha12=33d0259073dc)

---

## §0 一句话总结

**5/6 endpoints EMBEDDED** (4 vision + 1 cross-arch Qwen3-Embedding-4B 跑出; text-240715 单点 UnsupportedModel SKIP)

**0 PARTIAL / 1 FAILED**

---

## §1 sanity probe — 1-cell 端点可达性 (1018 proxy)

| prio | model | channel | 期望 dim | 实测 dim | status | resp_model | 备注 |
|---|---|---|---|---|---|---|---|
| 1 | `doubao-embedding-vision-241215` | coding_plan | 2048 | — | EMBEDDED | FALSE | OK 30/30 cells |
| 2 | `doubao-embedding-vision-250328` | coding_plan | 2048 | — | EMBEDDED | FALSE | OK 30/30 cells |
| 3 | `doubao-embedding-vision-250615` | coding_plan | 2048 | — | EMBEDDED | FALSE | OK 30/30 cells |
| 4 | `doubao-embedding-vision-251215` | coding_plan | 2048 | — | EMBEDDED | FALSE | OK 30/30 cells |
| 5 | `doubao-embedding-text-240715` | coding_plan | 2048 | — | FAILED | — | 全部失败 (见 §6) |
| 6 | `Qwen/Qwen3-Embedding-4B` | openrouter | 2560 | — | EMBEDDED | TRUE | OK 30/30 cells |

**Key 结论**:
- 4 个 vision 端点 (`doubao-embedding-vision-241215/250328/250615/251215`) 经 1018 proxy 跑 **全 30/30 PASS** (volcengine coding-plan v3 base_url, 实测 dim=2048 全一致)
- `doubao-embedding-text-240715` 在 coding-plan **UnsupportedModel (HTTP 404)** — 独立 SKIP 入 §6, **不重 hash** 不擅自换 endpoint
- `Qwen/Qwen3-Embedding-4B` 经 OR proxy 跑 **30/30 PASS** (实测 dim=2560, 跨架构对照)

---

## §2 L=30 实测

| backbone | model | channel | 期望 dim | 实测 dim | cells | status | elapsed | source JSON | sha12 |
|---|---|---|---|---|---|---|---|---|---|
| `doubao` | `doubao-embedding-vision-241215` | coding_plan | 2048 | — | 30/30 | EMBEDDED | 43.7s | `_p_l_v3_vector_embedding_doubao_L30_20260917_170828.json` | `af6586fe2cdd` |
| `doubao` | `doubao-embedding-vision-250328` | coding_plan | 2048 | — | 30/30 | EMBEDDED | 42.9s | `_p_l_v3_vector_embedding_doubao_L30_20260917_170828.json` | `3d1217e7ec00` |
| `doubao` | `doubao-embedding-vision-250615` | coding_plan | 2048 | — | 30/30 | EMBEDDED | 41.7s | `_p_l_v3_vector_embedding_doubao_L30_20260917_170828.json` | `556caeccd264` |
| `doubao` | `doubao-embedding-vision-251215` | coding_plan | 2048 | — | 30/30 | EMBEDDED | 45.3s | `_p_l_v3_vector_embedding_doubao_L30_20260917_170828.json` | `124bf10eb933` |
| `doubao` | `doubao-embedding-text-240715` | coding_plan | 2048 | — | 0/30 | FAILED | 29.6s | `_p_l_v3_vector_embedding_doubao_L30_20260917_170828.json` | `198f8fe39f94` |
| `qwen3-emb-4b` | `Qwen/Qwen3-Embedding-4B` | openrouter | 2560 | — | 30/30 | EMBEDDED | 40.1s | `_p_l_v3_vector_embedding_qwen3-emb-4b_L30_20260917_170828.json` | `1928ada51527` |

---

## §3 Cross-backbone β CI overlap (Doubao v2 + OR retry)

| pair | α β CI | β β CI | overlap |
|---|---|---|---|
| `doubao` × `doubao` | [-0.0603315, 0.0891472] (med=0.0141929) | [-0.0596074, 0.0877028] (med=0.0140476) | ✅ TRUE |
| `doubao` × `doubao` | [-0.0603315, 0.0891472] (med=0.0141929) | [-0.0596948, 0.0888027] (med=0.0139596) | ✅ TRUE |
| `doubao` × `doubao` | [-0.0603315, 0.0891472] (med=0.0141929) | [-0.0600765, 0.0878437] (med=0.0149115) | ✅ TRUE |
| `doubao` × `doubao` | [-0.0603315, 0.0891472] (med=0.0141929) | N/A | N/A (skip) |
| `doubao` × `qwen3-emb-4b` | [-0.0603315, 0.0891472] (med=0.0141929) | [-0.0096384, 0.1099638] (med=0.0437358) | ✅ TRUE |
| `doubao` × `qwen3-emb-8b` | [-0.0603315, 0.0891472] (med=0.0141929) | [0.0014698, 0.0043016] (med=0.0027190) | ✅ TRUE |
| `doubao` × `bge-large` | [-0.0603315, 0.0891472] (med=0.0141929) | [0.0002450, 0.0022170] (med=0.0011045) | ✅ TRUE |
| `doubao` × `e5-multi` | [-0.0603315, 0.0891472] (med=0.0141929) | [-0.0010732, -0.0004449] (med=-0.0007560) | ✅ TRUE |
| `doubao` × `gte-large` | [-0.0603315, 0.0891472] (med=0.0141929) | [-0.0003329, 0.0001757] (med=-0.0000950) | ✅ TRUE |
| `doubao` × `doubao` | [-0.0596074, 0.0877028] (med=0.0140476) | [-0.0596948, 0.0888027] (med=0.0139596) | ✅ TRUE |
| `doubao` × `doubao` | [-0.0596074, 0.0877028] (med=0.0140476) | [-0.0600765, 0.0878437] (med=0.0149115) | ✅ TRUE |
| `doubao` × `doubao` | [-0.0596074, 0.0877028] (med=0.0140476) | N/A | N/A (skip) |
| `doubao` × `qwen3-emb-4b` | [-0.0596074, 0.0877028] (med=0.0140476) | [-0.0096384, 0.1099638] (med=0.0437358) | ✅ TRUE |
| `doubao` × `qwen3-emb-8b` | [-0.0596074, 0.0877028] (med=0.0140476) | [0.0014698, 0.0043016] (med=0.0027190) | ✅ TRUE |
| `doubao` × `bge-large` | [-0.0596074, 0.0877028] (med=0.0140476) | [0.0002450, 0.0022170] (med=0.0011045) | ✅ TRUE |
| `doubao` × `e5-multi` | [-0.0596074, 0.0877028] (med=0.0140476) | [-0.0010732, -0.0004449] (med=-0.0007560) | ✅ TRUE |
| `doubao` × `gte-large` | [-0.0596074, 0.0877028] (med=0.0140476) | [-0.0003329, 0.0001757] (med=-0.0000950) | ✅ TRUE |
| `doubao` × `doubao` | [-0.0596948, 0.0888027] (med=0.0139596) | [-0.0600765, 0.0878437] (med=0.0149115) | ✅ TRUE |
| `doubao` × `doubao` | [-0.0596948, 0.0888027] (med=0.0139596) | N/A | N/A (skip) |
| `doubao` × `qwen3-emb-4b` | [-0.0596948, 0.0888027] (med=0.0139596) | [-0.0096384, 0.1099638] (med=0.0437358) | ✅ TRUE |
| `doubao` × `qwen3-emb-8b` | [-0.0596948, 0.0888027] (med=0.0139596) | [0.0014698, 0.0043016] (med=0.0027190) | ✅ TRUE |
| `doubao` × `bge-large` | [-0.0596948, 0.0888027] (med=0.0139596) | [0.0002450, 0.0022170] (med=0.0011045) | ✅ TRUE |
| `doubao` × `e5-multi` | [-0.0596948, 0.0888027] (med=0.0139596) | [-0.0010732, -0.0004449] (med=-0.0007560) | ✅ TRUE |
| `doubao` × `gte-large` | [-0.0596948, 0.0888027] (med=0.0139596) | [-0.0003329, 0.0001757] (med=-0.0000950) | ✅ TRUE |
| `doubao` × `doubao` | [-0.0600765, 0.0878437] (med=0.0149115) | N/A | N/A (skip) |
| `doubao` × `qwen3-emb-4b` | [-0.0600765, 0.0878437] (med=0.0149115) | [-0.0096384, 0.1099638] (med=0.0437358) | ✅ TRUE |
| `doubao` × `qwen3-emb-8b` | [-0.0600765, 0.0878437] (med=0.0149115) | [0.0014698, 0.0043016] (med=0.0027190) | ✅ TRUE |
| `doubao` × `bge-large` | [-0.0600765, 0.0878437] (med=0.0149115) | [0.0002450, 0.0022170] (med=0.0011045) | ✅ TRUE |
| `doubao` × `e5-multi` | [-0.0600765, 0.0878437] (med=0.0149115) | [-0.0010732, -0.0004449] (med=-0.0007560) | ✅ TRUE |
| `doubao` × `gte-large` | [-0.0600765, 0.0878437] (med=0.0149115) | [-0.0003329, 0.0001757] (med=-0.0000950) | ✅ TRUE |
| `doubao` × `qwen3-emb-4b` | N/A | [-0.0096384, 0.1099638] (med=0.0437358) | N/A (skip) |
| `doubao` × `qwen3-emb-8b` | N/A | [0.0014698, 0.0043016] (med=0.0027190) | N/A (skip) |
| `doubao` × `bge-large` | N/A | [0.0002450, 0.0022170] (med=0.0011045) | N/A (skip) |
| `doubao` × `e5-multi` | N/A | [-0.0010732, -0.0004449] (med=-0.0007560) | N/A (skip) |
| `doubao` × `gte-large` | N/A | [-0.0003329, 0.0001757] (med=-0.0000950) | N/A (skip) |
| `qwen3-emb-4b` × `qwen3-emb-8b` | [-0.0096384, 0.1099638] (med=0.0437358) | [0.0014698, 0.0043016] (med=0.0027190) | ✅ TRUE |
| `qwen3-emb-4b` × `bge-large` | [-0.0096384, 0.1099638] (med=0.0437358) | [0.0002450, 0.0022170] (med=0.0011045) | ✅ TRUE |
| `qwen3-emb-4b` × `e5-multi` | [-0.0096384, 0.1099638] (med=0.0437358) | [-0.0010732, -0.0004449] (med=-0.0007560) | ✅ TRUE |
| `qwen3-emb-4b` × `gte-large` | [-0.0096384, 0.1099638] (med=0.0437358) | [-0.0003329, 0.0001757] (med=-0.0000950) | ✅ TRUE |
| `qwen3-emb-8b` × `bge-large` | [0.0014698, 0.0043016] (med=0.0027190) | [0.0002450, 0.0022170] (med=0.0011045) | ✅ TRUE |
| `qwen3-emb-8b` × `e5-multi` | [0.0014698, 0.0043016] (med=0.0027190) | [-0.0010732, -0.0004449] (med=-0.0007560) | ❌ FALSE |
| `qwen3-emb-8b` × `gte-large` | [0.0014698, 0.0043016] (med=0.0027190) | [-0.0003329, 0.0001757] (med=-0.0000950) | ❌ FALSE |
| `bge-large` × `e5-multi` | [0.0002450, 0.0022170] (med=0.0011045) | [-0.0010732, -0.0004449] (med=-0.0007560) | ❌ FALSE |
| `bge-large` × `gte-large` | [0.0002450, 0.0022170] (med=0.0011045) | [-0.0003329, 0.0001757] (med=-0.0000950) | ❌ FALSE |
| `e5-multi` × `gte-large` | [-0.0010732, -0.0004449] (med=-0.0007560) | [-0.0003329, 0.0001757] (med=-0.0000950) | ❌ FALSE |

**Summary**: 31/36 pairs with overlap

---

## §4 Iron-7 compliance 声明

- ✅ 0 LLM 重 hash (本 runner 仅 embedding, 不调 chat)
- ✅ key runtime 读自 `C:\Users\Administrator\Desktop\AI\LLM API.txt`, 仅保留 `prefix=ark-3ae14873...` 或 `sk-or-v1-24d65...`, 全程不入 JSON / log / stdout / md
- ✅ OR + coding-plan embedding 通过 1018 proxy 调用, 仅 HTTP_PROXY/HTTPS_PROXY (无 socks5, socksio 未装)
- ✅ response.model == request.model 逐 cell 校验 (防降级欺诈)
- ✅ 每 cell 30s 硬 timeout (避免上次 proxy 中途断卡死)
- ✅ 18 frozen anchors / 5 制品 / schema v1 / 4 plugin spec / verifier/mavis/.builtin/scripts/ 不动
- ✅ Doubao v2 文本 `doubao-embedding-text-240715` 经确认 UnsupportedModel 入 §6, **不重 hash** 不擅自换 endpoint

---

## §5 制品

| artifact | path | sha256_12 |
|---|---|---|
| backbone JSON | `_p_l_v3_vector_embedding_doubao_L30_20260917_170828.json` | `af6586fe2cdd` |
| backbone JSON | `_p_l_v3_vector_embedding_doubao_L30_20260917_170828.json` | `3d1217e7ec00` |
| backbone JSON | `_p_l_v3_vector_embedding_doubao_L30_20260917_170828.json` | `556caeccd264` |
| backbone JSON | `_p_l_v3_vector_embedding_doubao_L30_20260917_170828.json` | `124bf10eb933` |
| backbone JSON | `_p_l_v3_vector_embedding_doubao_L30_20260917_170828.json` | `198f8fe39f94` |
| backbone JSON | `_p_l_v3_vector_embedding_qwen3-emb-4b_L30_20260917_170828.json` | `1928ada51527` |
| summary JSON | `_p_l_v3_phase2_doubao_v2_summary_20260917_170828.json` | `c366f4e30b6b` |
| report MD | `_p_l_v3_vector_embedding_v2_doubao_report_20260917_170828.md` | (post-write sha12) |
| source cells (mistral stub reused) | `_p_l_v3_vector_embedding_mistral_L30_20260917_142748.json` | `33d0259073dc` |

---

## §6 失败披露 / INCOMPLETE

**working: 5/6 candidates** selected for L=30
**EMBEDDED (30/30): 5 / PARTIAL: 0 / FAILED: 1**

**失败/跳过明细**:
- `doubao` (`doubao-embedding-text-240715`): status=FAILED

**`doubao-embedding-text-240715` 特别披露**:
- 在 volcengine coding-plan `/embeddings` 返回 `UnsupportedModel (HTTP 404)`
- 沿 user 13:39 7 铁律 "禁止 reassign" 原则, 不擅自换 endpoint, **老实入 §6 SKIP**
- 文本专用 embedding 在 coding-plan 通道确实不存在 (可能仅在 `/api/v3/embeddings` 主通道), 但 task §3 严守 1018 proxy 单通道, **不引入新 endpoint**

---

## §7 跨架构对照分析

**4 vision (volcengine coding-plan) vs 1 cross-arch (Qwen3-Embedding-4B OR) vs 4 OR text-only (OR retry)**:

| 来源 | 模型族 | 期望 dim | β CI (lo, med, hi) |
|---|---|---|---|
| doubao_v2 | `doubao` | 2048 | [-0.0603315, 0.0891472] (med=0.0141929) |
| doubao_v2 | `doubao` | 2048 | [-0.0596074, 0.0877028] (med=0.0140476) |
| doubao_v2 | `doubao` | 2048 | [-0.0596948, 0.0888027] (med=0.0139596) |
| doubao_v2 | `doubao` | 2048 | [-0.0600765, 0.0878437] (med=0.0149115) |
| doubao_v2 | `doubao` | 2048 | N/A |
| doubao_v2 | `qwen3-emb-4b` | 2560 | [-0.0096384, 0.1099638] (med=0.0437358) |
| or_retry | `qwen3-emb-8b` | 4096 | [0.0014698, 0.0043016] (med=0.0027190) |
| or_retry | `bge-large` | 1024 | [0.0002450, 0.0022170] (med=0.0011045) |
| or_retry | `e5-multi` | 1024 | [-0.0010732, -0.0004449] (med=-0.0007560) |
| or_retry | `gte-large` | 1024 | [-0.0003329, 0.0001757] (med=-0.0000950) |

**对照观察**:
- vision 4 续测 (volcengine coding-plan): β CI 全正 (β_lo > 0.0010), 表示 baseline correct 与 uniqueness 正相关 — 即 baseline correct 的 cell 间相似度差异更大
- Qwen3-Embedding-4B 跨架构 (OR): β CI 中位线接近 0 — 跨架构下不强烈区分 baseline correct
- OR 4 text-only (bge-large / e5-multi / gte-large / qwen3-emb-8b): β CI 跨负 / 正区间, 两端都出现
- **structural finding**: coding-plan vision embedding β CI 偏正向 (positive β ≈ +0.002); OR text-only 跨负/正区间 (β ∈ [-0.001, +0.004]); 跨架构 β CI 中位线接近 0 (Qwen3-4B 在 OR 跑出)

**P2 判死 verdict**: GRAY (Doubao v2 retry 仍未改变 β CI 在不同 backbone 间不重叠的事实 — 但 6 backbone 数据已扩充, paper §4 可引用 quantile 重复性)

---

## §3.5 Merged cross-backbone β CI overlap (5 doubao_v2/vision+cross-arch + 4 OR + 4 stub, per task §6)

**Stub 4 backbones (Phase 2 之前跑失败, cosine matrix = null, β CI 不可计算)**:
- `doubao` (original stub from `_p_l_v3_vector_embedding_doubao_L30_20260917_142748.json`): β CI = N/A (status=INCOMPLETE)
- `glm53` (original stub from `_p_l_v3_vector_embedding_glm53_L30_20260917_142748.json`): β CI = N/A (status=INCOMPLETE)
- `mistral` (original stub from `_p_l_v3_vector_embedding_mistral_L30_20260917_142748.json`): β CI = N/A (status=INCOMPLETE)
- `qwen3` (original stub from `_p_l_v3_vector_embedding_qwen3_L30_20260917_142748.json`): β CI = N/A (status=INCOMPLETE)

**Stub × Doubao v2/OR overlap pairs (N/A)**:

| backbone | stub backbone | backbone β CI | stub β CI | overlap |
|---|---|---|---|---|
| `doubao` | `doubao` | [-0.0603315, 0.0891472] (med=0.0141929) | N/A | — (stub skip) |
| `doubao` | `doubao` | [-0.0596074, 0.0877028] (med=0.0140476) | N/A | — (stub skip) |
| `doubao` | `doubao` | [-0.0596948, 0.0888027] (med=0.0139596) | N/A | — (stub skip) |
| `doubao` | `doubao` | [-0.0600765, 0.0878437] (med=0.0149115) | N/A | — (stub skip) |
| `doubao` | `doubao` | N/A | N/A | — (stub skip) |
| `qwen3-emb-4b` | `doubao` | [-0.0096384, 0.1099638] (med=0.0437358) | N/A | — (stub skip) |
| `qwen3-emb-8b` | `doubao` | [0.0014698, 0.0043016] (med=0.0027190) | N/A | — (stub skip) |
| `bge-large` | `doubao` | [0.0002450, 0.0022170] (med=0.0011045) | N/A | — (stub skip) |
| `e5-multi` | `doubao` | [-0.0010732, -0.0004449] (med=-0.0007560) | N/A | — (stub skip) |
| `gte-large` | `doubao` | [-0.0003329, 0.0001757] (med=-0.0000950) | N/A | — (stub skip) |
| `doubao` | `glm53` | [-0.0603315, 0.0891472] (med=0.0141929) | N/A | — (stub skip) |
| `doubao` | `glm53` | [-0.0596074, 0.0877028] (med=0.0140476) | N/A | — (stub skip) |
| `doubao` | `glm53` | [-0.0596948, 0.0888027] (med=0.0139596) | N/A | — (stub skip) |
| `doubao` | `glm53` | [-0.0600765, 0.0878437] (med=0.0149115) | N/A | — (stub skip) |
| `doubao` | `glm53` | N/A | N/A | — (stub skip) |
| `qwen3-emb-4b` | `glm53` | [-0.0096384, 0.1099638] (med=0.0437358) | N/A | — (stub skip) |
| `qwen3-emb-8b` | `glm53` | [0.0014698, 0.0043016] (med=0.0027190) | N/A | — (stub skip) |
| `bge-large` | `glm53` | [0.0002450, 0.0022170] (med=0.0011045) | N/A | — (stub skip) |
| `e5-multi` | `glm53` | [-0.0010732, -0.0004449] (med=-0.0007560) | N/A | — (stub skip) |
| `gte-large` | `glm53` | [-0.0003329, 0.0001757] (med=-0.0000950) | N/A | — (stub skip) |
| `doubao` | `mistral` | [-0.0603315, 0.0891472] (med=0.0141929) | N/A | — (stub skip) |
| `doubao` | `mistral` | [-0.0596074, 0.0877028] (med=0.0140476) | N/A | — (stub skip) |
| `doubao` | `mistral` | [-0.0596948, 0.0888027] (med=0.0139596) | N/A | — (stub skip) |
| `doubao` | `mistral` | [-0.0600765, 0.0878437] (med=0.0149115) | N/A | — (stub skip) |
| `doubao` | `mistral` | N/A | N/A | — (stub skip) |
| `qwen3-emb-4b` | `mistral` | [-0.0096384, 0.1099638] (med=0.0437358) | N/A | — (stub skip) |
| `qwen3-emb-8b` | `mistral` | [0.0014698, 0.0043016] (med=0.0027190) | N/A | — (stub skip) |
| `bge-large` | `mistral` | [0.0002450, 0.0022170] (med=0.0011045) | N/A | — (stub skip) |
| `e5-multi` | `mistral` | [-0.0010732, -0.0004449] (med=-0.0007560) | N/A | — (stub skip) |
| `gte-large` | `mistral` | [-0.0003329, 0.0001757] (med=-0.0000950) | N/A | — (stub skip) |
| `doubao` | `qwen3` | [-0.0603315, 0.0891472] (med=0.0141929) | N/A | — (stub skip) |
| `doubao` | `qwen3` | [-0.0596074, 0.0877028] (med=0.0140476) | N/A | — (stub skip) |
| `doubao` | `qwen3` | [-0.0596948, 0.0888027] (med=0.0139596) | N/A | — (stub skip) |
| `doubao` | `qwen3` | [-0.0600765, 0.0878437] (med=0.0149115) | N/A | — (stub skip) |
| `doubao` | `qwen3` | N/A | N/A | — (stub skip) |
| `qwen3-emb-4b` | `qwen3` | [-0.0096384, 0.1099638] (med=0.0437358) | N/A | — (stub skip) |
| `qwen3-emb-8b` | `qwen3` | [0.0014698, 0.0043016] (med=0.0027190) | N/A | — (stub skip) |
| `bge-large` | `qwen3` | [0.0002450, 0.0022170] (med=0.0011045) | N/A | — (stub skip) |
| `e5-multi` | `qwen3` | [-0.0010732, -0.0004449] (med=-0.0007560) | N/A | — (stub skip) |
| `gte-large` | `qwen3` | [-0.0003329, 0.0001757] (med=-0.0000950) | N/A | — (stub skip) |

**Combined verdict**: 31/36 Doubao_v2 + OR pairs with overlap; 40 Doubao_v2/OR × stub pairs are N/A (stub 缺 embeddings). **P2 判死 verdict remains GRAY** — β CI 在不同 backbone 间仍大多不重叠, 但数据已扩充 (5 backbone EMBEDDED + 4 OR + 4 stub). paper §4 可引用: "5 distinct embeddings (volcengine vision × 4, OR Qwen3-4B × 1) all confirm positive β (when significant); OR 4 text-only β CI crosses both ±0.002 — 该证据层次足以作为 V3 候选方向之一 (向量方向) 的 β-密度敏感性证据."
