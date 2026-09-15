# 火山方舟 Embedding 4 model × 30 cells 接入边际测试(对照 OpenRouter 5 model 参考测试)

**报告日期**: 2026-09-10 23:08:53 (Asia/Shanghai)
**测试目的**: 评估 4 个火山方舟 catalog 内 coding-plan 支持的 embedding model 在 30 cells 题目(GSM8K 1-15 + StrategyQA 1-15)上的接入边际,对照 OpenRouter 5 model 30 cells 参考测试(`OPENROUTER_5MODEL_30CELLS_2026_09_10.md`)。
**用户约束(关键)**: 2026-09-10 22:55 user 明确"同样测试下火山 embedding model 的成绩如何"。**严守 user 17:38(火山 catalog 内)+ 17:41(只走 coding-plan)**;不切 OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan。

---

## §1 测试环境

| 项 | 值 |
|----|---|
| Gateway | 火山方舟 Coding Plan (`https://ark.cn-beijing.volces.com/api/coding/v3`) |
| 鉴权 | `ark-de0b484e-...` 截断;key 从 `os.environ['ARK_CODING_PLAN_KEY']` runtime 加载,**literal key 永不入 JSON / 永不入 prompt / 永不落盘** |
| Proxy | **不设**(火山国内,直连) |
| 受限调用 | **不调** OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan(严守 user 17:38+17:41) |
| 错 endpoint | **不用** `/api/v3`(产生额外费用) |
| timeout/cell | 30s(节省原则;失败 fail-fast 不重试) |
| 题目源 | GSM8K 1-15 from `results/deposon_benchmark_v1_4_gsm8k_details.json`;StrategyQA 1-15 from `results/deposon_benchmark_v1_4_strategyqa_details.json` |
| cells 题目字段 | `question`(纯文本,无 markdown) |
| 题目总长范围 | GSM8K: 134-356 字符;StrategyQA: 25-84 字符 |
| 总 cells | 15 GSM8K + 15 StrategyQA = 30 cells |
| 总 API calls | 4 model × 30 cells(3 chunks × 10 cells) = **12 calls**;3 个 model 全 OK(12 calls),1 个 model chunk 3 fail(2 calls) = 实际 12 calls,无重试 |

---

## §2 火山 catalog embedding models 接入性筛选

`/api/coding/v3/models` 列 130 model,8 个 `*embedding*`:

| Model | coding-plan 支持 | 备注 |
|---|---|---|
| `doubao-embedding-text-240515` | ❌ UnsupportedModel (404) | 旧 text embedding,被 coding plan 弃 |
| `doubao-embedding-text-240715` | ❌ UnsupportedModel (404) | 同上 |
| `doubao-embedding-large-text-240915` | ❌ UnsupportedModel (404) | 同上 |
| `doubao-embedding-large-text-250515` | ❌ UnsupportedModel (404) | 同上 |
| `doubao-embedding-vision-241215` | ✅ 200, dim=2048 | **测试** |
| `doubao-embedding-vision-250328` | ✅ 200, dim=2048 | **测试**(chunk 3 timeout) |
| `doubao-embedding-vision-250615` | ✅ 200, dim=2048 | **测试** |
| `doubao-embedding-vision-251215` | ✅ 200, dim=2048 | **测试**(当前 baseline) |

**结论**: 8 个 catalog embedding model 中,**仅 4 个 `*vision*` model 支持 coding plan**;4 个 `*text*` / `*large-text*` 全部 404 `UnsupportedModel`。本次测试 4 vision model。

---

## §3 4 model 30 cells 横向对比表

| Model | Dim | Avg Latency | Median | P95 | Min | Max | Wall (30 cells) | Cost | Pass | Fail |
|---|---|---|---|---|---|---|---|---|---|---|
| `doubao-embedding-vision-241215` | 2048 | 164.1 ms | 182.5 ms | 205.2 ms | 104.7 ms | 205.2 ms | 4.93 s | $0.00 | 30/30 | 0 |
| `doubao-embedding-vision-250328` | 2048 | 107.3 ms | 118.7 ms | 118.7 ms | 96.0 ms | 118.7 ms | 33.27 s ⏱ | $0.00 | 20/30 | **10** (StrategyQA 6-15 全部 timeout) |
| `doubao-embedding-vision-250615` | 2048 | 132.8 ms | 69.8 ms | 269.7 ms | 59.0 ms | 269.7 ms | 3.99 s | $0.00 | 30/30 | 0 |
| ⭐ `doubao-embedding-vision-251215` | 2048 | **44.2 ms** | 47.5 ms | 73.2 ms | **34.0 ms** | 73.2 ms | **1.33 s** | $0.00 | 30/30 | 0 |

**汇总**:
- 总 calls: **12**(4 model × 3 chunks;chunk 内部 batch=10)
- 总 pass: **110/120 (91.67%)**
- 总 fail: **10**(全部为 `doubao-embedding-vision-250328` chunk 3,StrategyQA 6-15,均为 30s urllib read timeout;非 4xx 鉴权/参数错误)
- 总成本: **$0.00**(coding-plan 内,coding plan 限额内,无额外扣费)
- 总 wall time: **43.52 s = 0.7 min**

**速度排名(by avg latency)**:
1. ⭐ `doubao-embedding-vision-251215` 44.2 ms(2048-d,coding-plan 内,**最新版本**)
2. `doubao-embedding-vision-250328` 107.3 ms(2048-d,coding-plan 内;但 chunk 3 全 timeout)
3. `doubao-embedding-vision-250615` 132.8 ms(2048-d,coding-plan 内)
4. `doubao-embedding-vision-241215` 164.1 ms(2048-d,最旧 vision embedding,仍稳定 30/30)

**稳定性排名(by p95 / max ratio,越小越稳)**:
1. ⭐ `doubao-embedding-vision-241215` (p95/max = 1.0;前 10 cell 严格 205.2ms)
2. `doubao-embedding-vision-250328` (p95/max = 1.0;但 chunk 3 全 30s timeout,真稳假稳需重测)
3. `doubao-embedding-vision-250615` (p95/max = 1.0;StrategyQA 6-15 慢到 269.7ms 拖尾)
4. `doubao-embedding-vision-251215` (p95/max ≈ 1.0;最低 34ms 最高 73ms,几乎全在 100ms 内)

**失败 cell 明细**:
- `doubao-embedding-vision-250328` StrategyQA 6-15 全部 `-1: The read operation timed out`(30s urllib read timeout)。**整段 10 cells 同时失败**,不是单 cell 偶发,可能是 chunk 3 batch size 触发服务端限流或该 model 内部 batching 死锁。**无重试约束,标记 fail 但不补跑**。

---

## §4 与 OpenRouter 5 model 30 cells 对比表(关键)

| 维度 | 火山 (best: 251215) | OpenRouter (best: nemotron) | 火山 4 model avg | OpenRouter 5 model avg |
|---|---|---|---|---|
| Gateway | 火山方舟 coding plan | OpenRouter | 火山方舟 coding plan | OpenRouter |
| 接入路径 | 严守 user 17:38 + 17:41 | user 17:38 不允许(仅参考测试) | 同左 | 同左 |
| model 数 | 4 (8 catalog,4 text-embedding 不支持 coding plan) | 5 (5/5 supported) | 4 | 5 |
| 维度范围 | 2048 (统一) | 768 / 1024 / 2048 | 2048 | 1024 / 2048 / 768 |
| Avg Latency (best) | **44.2 ms** | 1593.7 ms | 112.1 ms (avg of 4) | 1841.3 ms (avg of 5) |
| Avg Latency (avg) | 112.1 ms | 1841.3 ms | 112.1 ms | 1841.3 ms |
| 速度优势倍数 | **36×** vs OpenRouter best | 1× baseline | **16×** vs OpenRouter avg | 1× baseline |
| 总 pass rate | 110/120 = 91.67% | 148/150 = 98.67% | 91.67% | 98.67% |
| 失败原因 | 1 model (250328) chunk 3 全 timeout | 2 single-cell timeout (free tier) | 同左 | 同左 |
| 总 wall time | 43.52 s = 0.7 min | 319.3 s = 5.3 min | 0.7 min | 5.3 min |
| 总成本 | $0.00 (coding plan) | $0.0000715 (~$0.0005) | $0.00 | $0.0000715 |
| 鉴权复杂度 | coding-plan key | OpenRouter key | 同左 | 同左 |
| 与 22 caption SVD 2D 76.5% var 对齐 | ✅ 已有 baseline `doubao-embedding-vision-251215` | ❌ 不在 22 caption baseline 范围 | n/a | n/a |

**核心 verdict**: 火山方舟 vision embedding 显著优于 OpenRouter 5 model
- **速度优势 16-36 倍**:火山 112ms avg vs OpenRouter 1841ms avg(维度相近 2048-d);即使火山最慢(241215, 164ms)仍快 11×。
- **成本优势**:两者都 ~$0,但火山 coding-plan 内"限额"语义,OpenRouter 走 token 计费。
- **稳定性略输**:火山 91.67% vs OpenRouter 98.67%(因 250328 整 chunk timeout),但 best model (251215) 是 100% pass。
- **接入严守 user 17:38 + 17:41**:火山 catalog 内 + coding plan 唯一,**唯一合规选项**。

---

## §5 5/8 vision embedding 性价比分析(本次测试 4 个 + 历史 baseline)

| Model | 发布日期 | 2048-d | Avg ms | Pass | 综合 |
|---|---|---|---|---|---|
| `doubao-embedding-vision-241215` | 2024-12-15 | ✅ | 164.1 | 30/30 | 旧但稳 |
| `doubao-embedding-vision-250328` | 2025-03-28 | ✅ | 107.3 | 20/30 | 快但 chunk 3 timeout |
| `doubao-embedding-vision-250615` | 2025-06-15 | ✅ | 132.8 | 30/30 | 稳定 |
| ⭐ `doubao-embedding-vision-251215` | 2025-12-15 | ✅ | **44.2** | 30/30 | **最新 + 最快 + 100% pass** |

**结论**: 4 个 vision embedding model 行为高度一致(2048-d 统一;速度 44-164ms;除 250328 偶发 chunk timeout 外都 30/30 pass)。**最新 `251215` 是明显优胜者**:速度比 241215 快 4×,比 250328 快 2.4×(且稳定),比 250615 快 3×。

---

## §6 7 铁律自检

| # | 铁律 | 实际行为 | 验证 |
|---|---|---|---|
| 1 | coding-plan key runtime 读 | `re.search(r'ark-de0b484e-[a-zA-Z0-9-]+')` from `LLM API.txt` GB18030 → `os.environ['ARK_CODING_PLAN_KEY']` | ✅ key 永不入 JSON(只 `ark-de0b484e-...` 截断) |
| 2 | 不设 proxy | `os.environ.pop` HTTP_PROXY/HTTPS_PROXY/http_proxy/https_proxy/ALL_PROXY/all_proxy | ✅ |
| 3 | 不调 OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan | 只调 `https://ark.cn-beijing.volces.com/api/coding/v3/{models,embeddings}` | ✅ |
| 4 | key 永不入 prompt / 永不入 JSON / 永不落盘 | JSON `auth` 字段 = `"ark-de0b484e-... (key loaded from env at runtime; literal key never written to disk)"`;cell texts 全是 dataset question 字段(无 key) | ✅ literal key 仅在 console |
| 5 | 节省原则:max_tokens 不用(只 embedding),timeout=30s/cell | embedding API 不需要 max_tokens;每 cell timeout=30s;失败 fail-fast 不重试 | ✅ 12 calls 严格(4 model × 3 chunks,1 chunk fail 仍计 12 calls,不补跑) |
| 6 | 不动 5 锚 JSON `KT_ABC1_anchors_sha256_12.json` (沿用 `03c6c01f3697`) | 未读未改 | ✅(未触) |
| 7 | 不动 4 SPEC V0.1 + v19 + v21 + corpus/v20 | 未触 | ✅(未触) |

---

## §7 错 endpoint / 错 key 自检

- ❌ **不调用** `/api/v3`(产生额外费用,任务硬性禁止)— 实际只调 `/api/coding/v3/{models,embeddings}` ✅
- ❌ **不调** `/api/v3/chat/completions` 错 model 当 embedding(本测试全走 `/embeddings` 端点)✅

---

## §8 下一步(给 user 参考,worker 不决定)

**1. 当前 V3X baseline 不动**:`doubao-embedding-vision-251215` 仍是 22 caption SVD 2D 投影 76.5% var baseline,本测试确认 30 cells 题目 embedding 路径 OK。
**2. 若 user 后续要在 4 vision embedding 中切换**:
- **首选**:`doubao-embedding-vision-251215`(2048-d, 44ms avg, 30/30 pass,**最新版本**)
- **次选**:`doubao-embedding-vision-241215`(2048-d, 164ms avg, 30/30 pass,**最稳**;若担心 251215 太新有 edge case)
- **不推荐**:`doubao-embedding-vision-250328`(快但 chunk 3 整段 timeout,生产不可靠)
**3. 4 个 text-embedding(`text-240515/240715` / `large-text-240915/250515`)**: coding plan 不支持,**本测试无法覆盖**;若 user 后续切到非 coding-plan 路径才能测试,但违反 user 17:38+17:41。
**4. 不建议**:切到 OpenRouter 任一 embedding(违反 user 17:38 + 17:41,且 16-36× 慢于火山)。

**最终 verdict**:
- 火山方舟 vision embedding 在 30 cells 接入边际**显著优于** OpenRouter 5 model(速度 16-36×,成本持平,coding-plan 合规)
- `doubao-embedding-vision-251215` 是 4 vision embedding 中的明显优胜者(最新、最快、100% pass)
- 4 text-embedding model 受 coding plan 限制无法测试(均 UnsupportedModel 404)
- V3X baseline `doubao-embedding-vision-251215` 保持不变,本测试仅作横向参照存档

---

## 附录 A:输出文件

| 路径 | 用途 | 大小 | SHA256 |
|---|---|---|---|
| `D:\私人资料\deposon-repo\results\deposon_volcengine_embedding_30cells_2026_09_10.json` | 完整 4 model × 30 cells 详细结果(含 cells_results, errors, latency per cell, summary) | 24,793 bytes | `271bee340ebaf82c789074badc743e650b3d6d15ecac0dce109669784604f85d` |
| `D:\私人资料\deposon-repo\docs\V3X\VOLCENGINE_EMBEDDING_30CELLS_2026_09_10.md` | 本报告 | ~7 KB | (git history 跟踪) |

## 附录 B:失败 cell 重跑建议(若 user 要求)

- 10 个失败 cell 全部为 `doubao-embedding-vision-250328` StrategyQA 6-15,**整 chunk 30s timeout**
- 重跑建议:该 model 单跑(不 batch)+ timeout 60s + 1-2s 间隔
- 但按"**不重试**"约束,本测试**不**重跑这 10 cell
- 若 user 后续需要 250328 100% pass,可单独 1 model × 10 cell 重跑(10 calls 总成本 ~$0)

## 附录 C:与已有 baseline 关系

- **22 caption embedding baseline**(`deposon_volcengine_22caption_embedding_2026_09_10`):用 `doubao-embedding-vision-251215`,SVD 2D 投影 76.5% var,**不动**
- **30 cells 题目 embedding 边际测试**(本报告):同 251215,4 vision embedding 横向对比,**作 V3X 后续 RAG 选型参照**
- **OpenRouter 5 model 30 cells 参考测试**(`OPENROUTER_5MODEL_30CELLS_2026_09_10.md`):非主线,仅参考
- **三者关系**: 22 caption baseline = 主线,本测试 = 横向扩展,OpenRouter 5 model = 跨平台参考

---

**报告生成**: 2026-09-10 23:08:53 +08:00 by worker sub-agent
**严守**: user 17:38 + 17:41 + 22:55(本次任务边界)
**Verdict**: 火山方舟 embedding(4 vision)显著优于 OpenRouter 5 model;`doubao-embedding-vision-251215` 是 4 model 中最优选(最新、最快、100% pass)
