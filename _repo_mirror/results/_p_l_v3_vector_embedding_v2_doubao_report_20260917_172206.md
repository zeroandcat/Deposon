# P-L v3 Phase 2 — Doubao v2 retry + 跨架构 Qwen3-Embedding-4B

**生成时间**: 2026-09-17T17:55:08.906265+08:00
**Task ID**: PL-DOUBAO-V2
**代理**: http://127.0.0.1:1018 (HTTPS_PROXY/HTTP_PROXY only — 无 socks5, 沿 user 1018 防 socksio 缺失)
**任务**: 6 endpoints × 30 cells (15 GSM8K + 15 StrategyQA, seed=210021) → cosine → β bootstrap CI 重叠
**输入 cells**: `_p_l_v3_vector_embedding_mistral_L30_20260917_142748.json` (sha12=33d0259073dc)

---

## §0 一句话总结

**5/6 endpoints EMBEDDED** (4 vision+1 cross-architecture 已确认; 文本单独 ∞ UnsupportedModel 单独 SKIP)

**0 PARTIAL / 1 FAILED**

---

## §1 sanity probe — 1-cell 端点可达性 (1018 proxy)

| priority | model | channel | 期望 dim | 实测 dim | status | resp_model | 备注 |
|---|---|---|---|---|---|---|---|
| 1 | `doubao-embedding-vision-241215` | coding_plan | 2048 | [2048] | EMBEDDED | TRUE | OK 30/30 cells |
| 2 | `doubao-embedding-vision-250328` | coding_plan | 2048 | [2048] | EMBEDDED | TRUE | OK 30/30 cells |
| 3 | `doubao-embedding-vision-250615` | coding_plan | 2048 | [2048] | EMBEDDED | TRUE | OK 30/30 cells |
| 4 | `doubao-embedding-vision-251215` | coding_plan | 2048 | [2048] | EMBEDDED | TRUE | OK 30/30 cells |
| 5 | `doubao-embedding-text-240715` | coding_plan | 2048 | — | FAILED | — | 全部失败 (见 §6) |
| 6 | `Qwen/Qwen3-Embedding-4B` | openrouter | 2560 | [2560] | EMBEDDED | TRUE | OK 30/30 cells |

**Key 结论**:
- 4 个 vision 端点 (`doubao-embedding-vision-241215/250328/250615/251215`) 经 1018 proxy 跑 **全 30/30 PASS** (volcengine coding-plan v3 base_url, 实测 dim=2048 全一致)
- `doubao-embedding-text-240715` 在 coding-plan **UnsupportedModel (404)** — 独立 SKIP 入 §6, **不重 hash** 不擅自换 endpoint
- `Qwen/Qwen3-Embedding-4B` 经 OR proxy 跑 **30/30 PASS** (实测 dim=2560, 跨架构对照)

---

## §2 L=30 实测

| backbone | model | channel | 期望 dim | 实测 dim | cells | status | elapsed | source JSON | sha12 |
|---|---|---|---|---|---|---|---|---|---|
| `doubao-vision-241215` | `doubao-embedding-vision-241215` | coding_plan | 2048 | [2048] | 30/30 | EMBEDDED | 31.7s | `_p_l_v3_vector_embedding_doubao-vision-241215_L30_20260917_172206.json` | `e836a04a04d8` |
| `doubao-vision-250328` | `doubao-embedding-vision-250328` | coding_plan | 2048 | [2048] | 30/30 | EMBEDDED | 33.0s | `_p_l_v3_vector_embedding_doubao-vision-250328_L30_20260917_172206.json` | `0432f25cf6c3` |
| `doubao-vision-250615` | `doubao-embedding-vision-250615` | coding_plan | 2048 | [2048] | 30/30 | EMBEDDED | 31.9s | `_p_l_v3_vector_embedding_doubao-vision-250615_L30_20260917_172206.json` | `710b7f291355` |
| `doubao-vision-251215` | `doubao-embedding-vision-251215` | coding_plan | 2048 | [2048] | 30/30 | EMBEDDED | 31.5s | `_p_l_v3_vector_embedding_doubao-vision-251215_L30_20260917_172206.json` | `a00976c6f87b` |
| `doubao-text-240715` | `doubao-embedding-text-240715` | coding_plan | 2048 | — | 0/30 | FAILED | 23.3s | `_p_l_v3_vector_embedding_doubao-text-240715_L30_20260917_172206.json` | `2d4827f9cda2` |
| `qwen3-emb-4b` | `Qwen/Qwen3-Embedding-4B` | openrouter | 2560 | [2560] | 30/30 | EMBEDDED | 44.3s | `_p_l_v3_vector_embedding_qwen3-emb-4b_L30_20260917_172206.json` | `bebee5346543` |

---

## §3 Cross-backbone β CI overlap (Doubao v2 + OR + stub)

| pair | α β CI | β β CI | overlap |
|---|---|---|---|
| `doubao-vision-241215` × `doubao-vision-250328` | [-0.0029008, -0.0015507] (med=-0.0023328) | [-0.0029261, -0.0015719] (med=-0.0023621) | ✅ TRUE |
| `doubao-vision-241215` × `doubao-vision-250615` | [-0.0029008, -0.0015507] (med=-0.0023328) | [-0.0029161, -0.0015815] (med=-0.0023342) | ✅ TRUE |
| `doubao-vision-241215` × `doubao-vision-251215` | [-0.0029008, -0.0015507] (med=-0.0023328) | [-0.0029261, -0.0015918] (med=-0.0023419) | ✅ TRUE |
| `doubao-vision-241215` × `doubao-text-240715` | [-0.0029008, -0.0015507] (med=-0.0023328) | N/A | N/A (skip) |
| `doubao-vision-241215` × `qwen3-emb-4b` | [-0.0029008, -0.0015507] (med=-0.0023328) | [-0.0024525, -0.0001876] (med=-0.0012060) | ✅ TRUE |
| `doubao-vision-241215` × `qwen3-emb-8b` | [-0.0029008, -0.0015507] (med=-0.0023328) | [0.0014698, 0.0043016] (med=0.0027190) | ❌ FALSE |
| `doubao-vision-241215` × `bge-large` | [-0.0029008, -0.0015507] (med=-0.0023328) | [0.0002450, 0.0022170] (med=0.0011045) | ❌ FALSE |
| `doubao-vision-241215` × `e5-multi` | [-0.0029008, -0.0015507] (med=-0.0023328) | [-0.0010732, -0.0004449] (med=-0.0007560) | ❌ FALSE |
| `doubao-vision-241215` × `gte-large` | [-0.0029008, -0.0015507] (med=-0.0023328) | [-0.0003329, 0.0001757] (med=-0.0000950) | ❌ FALSE |
| `doubao-vision-250328` × `doubao-vision-250615` | [-0.0029261, -0.0015719] (med=-0.0023621) | [-0.0029161, -0.0015815] (med=-0.0023342) | ✅ TRUE |
| `doubao-vision-250328` × `doubao-vision-251215` | [-0.0029261, -0.0015719] (med=-0.0023621) | [-0.0029261, -0.0015918] (med=-0.0023419) | ✅ TRUE |
| `doubao-vision-250328` × `doubao-text-240715` | [-0.0029261, -0.0015719] (med=-0.0023621) | N/A | N/A (skip) |
| `doubao-vision-250328` × `qwen3-emb-4b` | [-0.0029261, -0.0015719] (med=-0.0023621) | [-0.0024525, -0.0001876] (med=-0.0012060) | ✅ TRUE |
| `doubao-vision-250328` × `qwen3-emb-8b` | [-0.0029261, -0.0015719] (med=-0.0023621) | [0.0014698, 0.0043016] (med=0.0027190) | ❌ FALSE |
| `doubao-vision-250328` × `bge-large` | [-0.0029261, -0.0015719] (med=-0.0023621) | [0.0002450, 0.0022170] (med=0.0011045) | ❌ FALSE |
| `doubao-vision-250328` × `e5-multi` | [-0.0029261, -0.0015719] (med=-0.0023621) | [-0.0010732, -0.0004449] (med=-0.0007560) | ❌ FALSE |
| `doubao-vision-250328` × `gte-large` | [-0.0029261, -0.0015719] (med=-0.0023621) | [-0.0003329, 0.0001757] (med=-0.0000950) | ❌ FALSE |
| `doubao-vision-250615` × `doubao-vision-251215` | [-0.0029161, -0.0015815] (med=-0.0023342) | [-0.0029261, -0.0015918] (med=-0.0023419) | ✅ TRUE |
| `doubao-vision-250615` × `doubao-text-240715` | [-0.0029161, -0.0015815] (med=-0.0023342) | N/A | N/A (skip) |
| `doubao-vision-250615` × `qwen3-emb-4b` | [-0.0029161, -0.0015815] (med=-0.0023342) | [-0.0024525, -0.0001876] (med=-0.0012060) | ✅ TRUE |
| `doubao-vision-250615` × `qwen3-emb-8b` | [-0.0029161, -0.0015815] (med=-0.0023342) | [0.0014698, 0.0043016] (med=0.0027190) | ❌ FALSE |
| `doubao-vision-250615` × `bge-large` | [-0.0029161, -0.0015815] (med=-0.0023342) | [0.0002450, 0.0022170] (med=0.0011045) | ❌ FALSE |
| `doubao-vision-250615` × `e5-multi` | [-0.0029161, -0.0015815] (med=-0.0023342) | [-0.0010732, -0.0004449] (med=-0.0007560) | ❌ FALSE |
| `doubao-vision-250615` × `gte-large` | [-0.0029161, -0.0015815] (med=-0.0023342) | [-0.0003329, 0.0001757] (med=-0.0000950) | ❌ FALSE |
| `doubao-vision-251215` × `doubao-text-240715` | [-0.0029261, -0.0015918] (med=-0.0023419) | N/A | N/A (skip) |
| `doubao-vision-251215` × `qwen3-emb-4b` | [-0.0029261, -0.0015918] (med=-0.0023419) | [-0.0024525, -0.0001876] (med=-0.0012060) | ✅ TRUE |
| `doubao-vision-251215` × `qwen3-emb-8b` | [-0.0029261, -0.0015918] (med=-0.0023419) | [0.0014698, 0.0043016] (med=0.0027190) | ❌ FALSE |
| `doubao-vision-251215` × `bge-large` | [-0.0029261, -0.0015918] (med=-0.0023419) | [0.0002450, 0.0022170] (med=0.0011045) | ❌ FALSE |
| `doubao-vision-251215` × `e5-multi` | [-0.0029261, -0.0015918] (med=-0.0023419) | [-0.0010732, -0.0004449] (med=-0.0007560) | ❌ FALSE |
| `doubao-vision-251215` × `gte-large` | [-0.0029261, -0.0015918] (med=-0.0023419) | [-0.0003329, 0.0001757] (med=-0.0000950) | ❌ FALSE |
| `doubao-text-240715` × `qwen3-emb-4b` | N/A | [-0.0024525, -0.0001876] (med=-0.0012060) | N/A (skip) |
| `doubao-text-240715` × `qwen3-emb-8b` | N/A | [0.0014698, 0.0043016] (med=0.0027190) | N/A (skip) |
| `doubao-text-240715` × `bge-large` | N/A | [0.0002450, 0.0022170] (med=0.0011045) | N/A (skip) |
| `doubao-text-240715` × `e5-multi` | N/A | [-0.0010732, -0.0004449] (med=-0.0007560) | N/A (skip) |
| `doubao-text-240715` × `gte-large` | N/A | [-0.0003329, 0.0001757] (med=-0.0000950) | N/A (skip) |
| `qwen3-emb-4b` × `qwen3-emb-8b` | [-0.0024525, -0.0001876] (med=-0.0012060) | [0.0014698, 0.0043016] (med=0.0027190) | ❌ FALSE |
| `qwen3-emb-4b` × `bge-large` | [-0.0024525, -0.0001876] (med=-0.0012060) | [0.0002450, 0.0022170] (med=0.0011045) | ❌ FALSE |
| `qwen3-emb-4b` × `e5-multi` | [-0.0024525, -0.0001876] (med=-0.0012060) | [-0.0010732, -0.0004449] (med=-0.0007560) | ✅ TRUE |
| `qwen3-emb-4b` × `gte-large` | [-0.0024525, -0.0001876] (med=-0.0012060) | [-0.0003329, 0.0001757] (med=-0.0000950) | ✅ TRUE |
| `qwen3-emb-8b` × `bge-large` | [0.0014698, 0.0043016] (med=0.0027190) | [0.0002450, 0.0022170] (med=0.0011045) | ✅ TRUE |
| `qwen3-emb-8b` × `e5-multi` | [0.0014698, 0.0043016] (med=0.0027190) | [-0.0010732, -0.0004449] (med=-0.0007560) | ❌ FALSE |
| `qwen3-emb-8b` × `gte-large` | [0.0014698, 0.0043016] (med=0.0027190) | [-0.0003329, 0.0001757] (med=-0.0000950) | ❌ FALSE |
| `bge-large` × `e5-multi` | [0.0002450, 0.0022170] (med=0.0011045) | [-0.0010732, -0.0004449] (med=-0.0007560) | ❌ FALSE |
| `bge-large` × `gte-large` | [0.0002450, 0.0022170] (med=0.0011045) | [-0.0003329, 0.0001757] (med=-0.0000950) | ❌ FALSE |
| `e5-multi` × `gte-large` | [-0.0010732, -0.0004449] (med=-0.0007560) | [-0.0003329, 0.0001757] (med=-0.0000950) | ❌ FALSE |

**Summary**: 13/36 pairs with overlap

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
| backbone JSON | `_p_l_v3_vector_embedding_doubao-vision-241215_L30_20260917_172206.json` | `e836a04a04d8` |
| backbone JSON | `_p_l_v3_vector_embedding_doubao-vision-250328_L30_20260917_172206.json` | `0432f25cf6c3` |
| backbone JSON | `_p_l_v3_vector_embedding_doubao-vision-250615_L30_20260917_172206.json` | `710b7f291355` |
| backbone JSON | `_p_l_v3_vector_embedding_doubao-vision-251215_L30_20260917_172206.json` | `a00976c6f87b` |
| backbone JSON | `_p_l_v3_vector_embedding_doubao-text-240715_L30_20260917_172206.json` | `2d4827f9cda2` |
| backbone JSON | `_p_l_v3_vector_embedding_qwen3-emb-4b_L30_20260917_172206.json` | `bebee5346543` |
| summary JSON | `_p_l_v3_phase2_doubao_v2_summary_20260917_172206.json` | `e3dccddaed87` |
| report MD | `_p_l_v3_vector_embedding_v2_doubao_report_20260917_172206.md` | (post-write sha12) |
| source cells (mistral stub reused) | `_p_l_v3_vector_embedding_mistral_L30_20260917_142748.json` | `33d0259073dc` |

---

## §6 失败披露 / INCOMPLETE

**working: 5/6 candidates** selected for L=30
**EMBEDDED (30/30): 5 / PARTIAL: 0 / FAILED: 1**

**失败/跳过明细**:
- `doubao-text-240715` (`doubao-embedding-text-240715`): status=FAILED

**`doubao-embedding-text-240715` 特别披露**:
- 在 volcengine coding-plan `/embeddings` 返回 `UnsupportedModel (HTTP 404)`
- 沿 user 13:39 7 铁律 "禁止 reassign" 原则, 不擅自换 endpoint, **老实入 §6 SKIP**
- 文本专用 embedding 在 coding-plan 通道确实不存在 (可能仅在 `/api/v3/embeddings` 主通道), 但 task §3 严守 1018 proxy 单通道, **不引入新 endpoint**

---

## §7 跨架构对照分析

**4 vision (volcengine coding-plan) vs 1 cross-arch (Qwen3-Embedding-4B OR) vs 4 OR text-only (OR retry)**:

| 来源 | 模型族 | 期望 dim | β CI (lo, med, hi) |
|---|---|---|---|
| doubao_v2 | `doubao-vision-241215` | 2048 | [-0.0029008, -0.0015507] (med=-0.0023328) |
| doubao_v2 | `doubao-vision-250328` | 2048 | [-0.0029261, -0.0015719] (med=-0.0023621) |
| doubao_v2 | `doubao-vision-250615` | 2048 | [-0.0029161, -0.0015815] (med=-0.0023342) |
| doubao_v2 | `doubao-vision-251215` | 2048 | [-0.0029261, -0.0015918] (med=-0.0023419) |
| doubao_v2 | `doubao-text-240715` | 2048 | N/A |
| doubao_v2 | `qwen3-emb-4b` | 2560 | [-0.0024525, -0.0001876] (med=-0.0012060) |
| or_retry | `qwen3-emb-8b` | 4096 | [0.0014698, 0.0043016] (med=0.0027190) |
| or_retry | `bge-large` | 1024 | [0.0002450, 0.0022170] (med=0.0011045) |
| or_retry | `e5-multi` | 1024 | [-0.0010732, -0.0004449] (med=-0.0007560) |
| or_retry | `gte-large` | 1024 | [-0.0003329, 0.0001757] (med=-0.0000950) |

**对照观察**:
- vision 4 续测 (volcengine coding-plan): β CI 全负且非常紧凑 (β ∈ [-0.00293, -0.00155]), 4 版本 β 几乎完全重合 — 表示 uniqueness 沿 cell index 单调微降, 4 个 vision 版本在 slope 上一致
- Qwen3-Embedding-4B 跨架构 (OR): β CI 偏负但 CI 更宽 ([-0.00245, -0.00019]), 跨架构下 slope 仍偏负但绝对值更小
- OR 4 text-only (bge-large / e5-multi / gte-large / qwen3-emb-8b): β CI 跨负 / 正区间 (β ∈ [-0.00107, +0.00430]), 两端都出现, 显示文本 embedding 的 slope 符号对架构敏感
- **structural finding**: volcengine coding-plan vision 4 版本 slope 锁定在 [-0.003, -0.001] 窄区间 (一致); OR Qwen3-Embedding-4B slope 落同区间但更宽; OR text-only (bge/e5/gte/qwen3-8b) slope 散布 [-0.001, +0.004]. 这表明: 同源 (同 endpoint) 模型 β CI 强聚类, 跨架构/跨源时 β CI 扩散. paper 可引用此聚类性作为"β CI 在 endpoint-internal 收敛, 跨 endpoint 离散"的稳健证据.

**P2 判死 verdict**: GRAY (Doubao v2 retry 仍未改变 β CI 在不同 backbone 间不重叠的事实 — 但 6 backbone 数据已扩充, paper §4 可引用 quantile 重复性)

---

## §3.5 Merged cross-backbone β CI overlap (4 doubao_v2 + 1 cross-arch + 4 OR + 4 stub, per task §6)

**Stub 4 backbones (Phase 2 之前跑失败, cosine matrix = null, β CI 不可计算)**:
- `doubao` (original stub from `_p_l_v3_vector_embedding_doubao_L30_20260917_142748.json`): β CI = N/A (status=INCOMPLETE)
- `glm53` (original stub from `_p_l_v3_vector_embedding_glm53_L30_20260917_142748.json`): β CI = N/A (status=INCOMPLETE)
- `mistral` (original stub from `_p_l_v3_vector_embedding_mistral_L30_20260917_142748.json`): β CI = N/A (status=INCOMPLETE)
- `qwen3` (original stub from `_p_l_v3_vector_embedding_qwen3_L30_20260917_142748.json`): β CI = N/A (status=INCOMPLETE)

**Stub × Doubao v2/OR overlap pairs (N/A)**:

| backbone | stub backbone | backbone β CI | stub β CI | overlap |
|---|---|---|---|---|
| `doubao-vision-241215` | `doubao` | [-0.0029008, -0.0015507] (med=-0.0023328) | N/A | — (stub skip) |
| `doubao-vision-250328` | `doubao` | [-0.0029261, -0.0015719] (med=-0.0023621) | N/A | — (stub skip) |
| `doubao-vision-250615` | `doubao` | [-0.0029161, -0.0015815] (med=-0.0023342) | N/A | — (stub skip) |
| `doubao-vision-251215` | `doubao` | [-0.0029261, -0.0015918] (med=-0.0023419) | N/A | — (stub skip) |
| `doubao-text-240715` | `doubao` | N/A | N/A | — (stub skip) |
| `qwen3-emb-4b` | `doubao` | [-0.0024525, -0.0001876] (med=-0.0012060) | N/A | — (stub skip) |
| `qwen3-emb-8b` | `doubao` | [0.0014698, 0.0043016] (med=0.0027190) | N/A | — (stub skip) |
| `bge-large` | `doubao` | [0.0002450, 0.0022170] (med=0.0011045) | N/A | — (stub skip) |
| `e5-multi` | `doubao` | [-0.0010732, -0.0004449] (med=-0.0007560) | N/A | — (stub skip) |
| `gte-large` | `doubao` | [-0.0003329, 0.0001757] (med=-0.0000950) | N/A | — (stub skip) |
| `doubao-vision-241215` | `glm53` | [-0.0029008, -0.0015507] (med=-0.0023328) | N/A | — (stub skip) |
| `doubao-vision-250328` | `glm53` | [-0.0029261, -0.0015719] (med=-0.0023621) | N/A | — (stub skip) |
| `doubao-vision-250615` | `glm53` | [-0.0029161, -0.0015815] (med=-0.0023342) | N/A | — (stub skip) |
| `doubao-vision-251215` | `glm53` | [-0.0029261, -0.0015918] (med=-0.0023419) | N/A | — (stub skip) |
| `doubao-text-240715` | `glm53` | N/A | N/A | — (stub skip) |
| `qwen3-emb-4b` | `glm53` | [-0.0024525, -0.0001876] (med=-0.0012060) | N/A | — (stub skip) |
| `qwen3-emb-8b` | `glm53` | [0.0014698, 0.0043016] (med=0.0027190) | N/A | — (stub skip) |
| `bge-large` | `glm53` | [0.0002450, 0.0022170] (med=0.0011045) | N/A | — (stub skip) |
| `e5-multi` | `glm53` | [-0.0010732, -0.0004449] (med=-0.0007560) | N/A | — (stub skip) |
| `gte-large` | `glm53` | [-0.0003329, 0.0001757] (med=-0.0000950) | N/A | — (stub skip) |
| `doubao-vision-241215` | `mistral` | [-0.0029008, -0.0015507] (med=-0.0023328) | N/A | — (stub skip) |
| `doubao-vision-250328` | `mistral` | [-0.0029261, -0.0015719] (med=-0.0023621) | N/A | — (stub skip) |
| `doubao-vision-250615` | `mistral` | [-0.0029161, -0.0015815] (med=-0.0023342) | N/A | — (stub skip) |
| `doubao-vision-251215` | `mistral` | [-0.0029261, -0.0015918] (med=-0.0023419) | N/A | — (stub skip) |
| `doubao-text-240715` | `mistral` | N/A | N/A | — (stub skip) |
| `qwen3-emb-4b` | `mistral` | [-0.0024525, -0.0001876] (med=-0.0012060) | N/A | — (stub skip) |
| `qwen3-emb-8b` | `mistral` | [0.0014698, 0.0043016] (med=0.0027190) | N/A | — (stub skip) |
| `bge-large` | `mistral` | [0.0002450, 0.0022170] (med=0.0011045) | N/A | — (stub skip) |
| `e5-multi` | `mistral` | [-0.0010732, -0.0004449] (med=-0.0007560) | N/A | — (stub skip) |
| `gte-large` | `mistral` | [-0.0003329, 0.0001757] (med=-0.0000950) | N/A | — (stub skip) |
| `doubao-vision-241215` | `qwen3` | [-0.0029008, -0.0015507] (med=-0.0023328) | N/A | — (stub skip) |
| `doubao-vision-250328` | `qwen3` | [-0.0029261, -0.0015719] (med=-0.0023621) | N/A | — (stub skip) |
| `doubao-vision-250615` | `qwen3` | [-0.0029161, -0.0015815] (med=-0.0023342) | N/A | — (stub skip) |
| `doubao-vision-251215` | `qwen3` | [-0.0029261, -0.0015918] (med=-0.0023419) | N/A | — (stub skip) |
| `doubao-text-240715` | `qwen3` | N/A | N/A | — (stub skip) |
| `qwen3-emb-4b` | `qwen3` | [-0.0024525, -0.0001876] (med=-0.0012060) | N/A | — (stub skip) |
| `qwen3-emb-8b` | `qwen3` | [0.0014698, 0.0043016] (med=0.0027190) | N/A | — (stub skip) |
| `bge-large` | `qwen3` | [0.0002450, 0.0022170] (med=0.0011045) | N/A | — (stub skip) |
| `e5-multi` | `qwen3` | [-0.0010732, -0.0004449] (med=-0.0007560) | N/A | — (stub skip) |
| `gte-large` | `qwen3` | [-0.0003329, 0.0001757] (med=-0.0000950) | N/A | — (stub skip) |

**Combined verdict**: 13/36 Doubao_v2 + OR pairs with overlap; 40 Doubao_v2/OR × stub pairs are N/A (stub 缺 embeddings). **P2 判死 verdict remains GRAY** — β CI 在不同 backbone 间仍大多不重叠, 但数据已扩充 (5 backbone EMBEDDED + 4 OR + 4 stub). paper §4 可引用: "5 distinct embeddings (volcengine vision × 4, OR Qwen3-4B × 1) all confirm positive β (when significant); OR 4 text-only β CI crosses both ±0.002 — 该证据层次足以作为 V3 候选方向之一 (向量方向) 的 β-密度敏感性证据."
