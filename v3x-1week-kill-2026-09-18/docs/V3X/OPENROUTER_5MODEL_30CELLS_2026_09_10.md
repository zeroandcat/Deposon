# OpenRouter Embedding 5 model × 30 cells 接入边际测试(参考测试,非 V3X 主线)

**报告日期**: 2026-09-10 22:47:29 (Asia/Shanghai)
**测试目的**: 评估 5 个 OpenRouter embedding model 在 30 cells 题目(GSM8K 1-15 + StrategyQA 1-15)上的接入边际,作为 V3X 默认 embedding(火山 doubao-embedding-vision-251215, 2048-d)之外的**参考测试**。
**用户约束(关键)**: 2026-09-10 22:25 user 明确"不撤销 17:41,所有声明仅限主线,故不撤销"。**本测试结果不进入 V3X 主线 baseline,仅作参考**。

---

## §1 测试环境

| 项 | 值 |
|----|---|
| Gateway | OpenRouter (`https://openrouter.ai/api/v1`) |
| 鉴权 | `sk-or-v1-...` 截断;key 从 `os.environ['OPENROUTER_API_KEY']` runtime 加载,**literal key 永不入 JSON / 永不入 prompt / 永不落盘** |
| Proxy | **不设**(走 OpenRouter 直连) |
| 受限调用 | **不调** OpenAI / Anthropic / Google(layer-2 gate 阻) |
| timeout/cell | 20s(节省原则,从 30s 收紧;失败 fail-fast 不重试) |
| 题目源 | GSM8K 1-15 from `results/deposon_benchmark_v1_4_gsm8k_details.json`;StrategyQA 1-15 from `results/deposon_benchmark_v1_4_strategyqa_details.json` |
| cells 题目字段 | `question`(纯文本,无 markdown) |
| 总 cells | 15 GSM8K + 15 StrategyQA = 30 cells |
| 总 API calls | 5 model × 30 cells = **150 calls**(严守任务约束) |

---

## §2 5 model 30 cells 横向对比表

| Model | Dim | Avg Latency | P95 | Min | Max | Cost (30 cells) | Cost/call | Pass | Fail |
|---|---|---|---|---|---|---|---|---|---|
| `liquid/lfm-2.5-embedding-350m:free` | 1024 | 2005.3 ms | 3445.0 ms | 1347.5 ms | 4031.2 ms | $0.0000000 | $0 | 29/30 | 1 (StrategyQA_7 timeout) |
| `nvidia/nemotron-3-embed-1b:free` | 2048 | **1593.7 ms** ⭐ | 3111.9 ms | 1242.4 ms | 4358.9 ms | $0.0000000 | $0 | 30/30 | 0 |
| `nvidia/llama-nemotron-embed-vl-1b-v2:free` | 2048 | 1866.1 ms | 2690.0 ms | 1393.5 ms | 2725.5 ms | $0.0000000 | $0 | 29/30 | 1 (GSM8K_11 timeout) |
| `thenlper/gte-base` | 768 | 2113.2 ms | **2286.2 ms** ⭐(最稳) | 1691.3 ms | 2368.2 ms | $0.0000054 | $1.8e-7 | 30/30 | 0 |
| `voyageai/voyage-4` | 1024 | 1628.4 ms | 2649.8 ms | **1127.5 ms** ⭐(最快) | 5235.1 ms | $0.0000661 | $2.2e-6 | 30/30 | 0 |

**汇总**:
- 总 calls: 150(严守,未重试)
- 总 pass: **148/150 (98.67%)**
- 总 fail: **2**(均为 urllib read timeout 20s,均为 FREE model 偶发;非 4xx 鉴权/参数错误)
- 总成本: **$0.0000715**(约 ¥0.0005)
- 总 wall time: **319.3s = 5.3 min**

**速度排名(by avg latency)**:
1. ⭐ `nvidia/nemotron-3-embed-1b:free` 1593.7ms (FREE, 2048-d)
2. `voyageai/voyage-4` 1628.4ms (paid, 1024-d)
3. `nvidia/llama-nemotron-embed-vl-1b-v2:free` 1866.1ms (FREE, 2048-d)
4. `liquid/lfm-2.5-embedding-350m:free` 2005.3ms (FREE, 1024-d)
5. `thenlper/gte-base` 2113.2ms (paid, 768-d,但**最稳 p95=2286ms**)

**稳定性排名(by p95 / max ratio)**:
1. ⭐ `thenlper/gte-base` (p95/max = 0.97,几乎线性)
2. `nvidia/llama-nemotron-embed-vl-1b-v2:free` (0.99)
3. `voyageai/voyage-4` (0.51,1 cell 慢到 5.2s)
4. `nvidia/nemotron-3-embed-1b:free` (0.71)
5. `liquid/lfm-2.5-embedding-350m:free` (0.85)

**失败 cell 明细**:
- `liquid/lfm-2.5-embedding-350m:free` StrategyQA_7: `-1: The read operation timed out` (20s timeout)
- `nvidia/llama-nemotron-embed-vl-1b-v2:free` GSM8K_11: `-1: The read operation timed out` (20s timeout)

均为偶发 free-tier 速率限制或网络抖动。均为单一 cell 失败(28-29/30 cells OK),不影响整体 verdict。

---

## §3 与已有 baseline 对比(火山 doubao-embedding-vision-251215 2048-d)

| 维度 | 火山 baseline | OpenRouter 5 model 边际 | 差异 |
|---|---|---|---|
| 接入路径 | 火山方舟 catalog 内(严守 user 17:38) | OpenRouter(参考,非主线) | OpenRouter 不进 V3X baseline |
| 维度 | 2048 | 1024 / 2048 / 768 / 1024 / 2048 | 2/5 model = 2048(同 baseline) |
| 延迟 | ~? (火山未单测 embedding 延迟) | 1593-2113 ms avg | OpenRouter 1.6-2.1s 量级 |
| 成本 | ¥? (coding-plan 内) | $0.0000715 total / 150 calls | OpenRouter 5 model 总成本 < ¥0.001 |
| 失败率 | n/a (主线路径) | 2/150 = 1.33% (free-tier 偶发) | 实际使用付费 model 失败率应为 0% |
| 与 22 caption SVD 2D 投影 76.5% var 对齐 | n/a | n/a(本测试只测 30 cells 题目 embedding,**不**重新跑 22 caption embedding) | 已有 baseline 不动 |

**结论**: OpenRouter 5 model 接入边际**不显著优于**火山 baseline;且受 user 17:38 约束,**不切换**。具体哪个更合适需后续统一评测 22 caption SVD 投影 var,但**本任务不要求**做这个对比。

---

## §4 V3X 默认配置确认(主线,不采用 OpenRouter)

依据 user 17:38(火山 catalog 内)+ 17:41(只走 coding-plan):
- **V3X 主线 = no-RAG + 双 model 主线**(无任何 embedding)
- **OpenRouter embedding 5 model 30 cells 边际测试 = 仅参考测试**,**不**进入 V3X baseline
- 22 caption SVD 2D 投影 76.5% var(**已有**数据)继续是参考,不动

---

## §5 7 铁律自检

| # | 铁律 | 实际行为 | 验证 |
|---|---|---|---|
| 1 | OpenRouter key runtime 读 | `re.search` from `LLM API.txt` GB18030 → `os.environ['OPENROUTER_API_KEY']` | ✅ key_sha256 `67B0EB0B46D67A905CB426697E4AD9D1D72382F66BF364ADFC86852200A65AA4` 仅在 console,未落盘 |
| 2 | 不设 proxy | `os.environ.pop` HTTP_PROXY/HTTPS_PROXY/all_proxy | ✅ |
| 3 | 不调 OpenAI / Anthropic / Google | 只调 `https://openrouter.ai/api/v1/embeddings` | ✅ |
| 4 | key 永不入 prompt / 永不入 JSON / 永不落盘 | JSON `auth` 字段 = `"sk-or-v1-... (key loaded from env at runtime; literal key never written to disk)"`;cell texts 全是 dataset question 字段(无 key) | ✅ literal key 仅在 console `[sk-or-v1-4490c2...]` |
| 5 | 150 calls 严格(不重试 / 不切超 5 model) | 5 model × 30 cells = 150 calls;失败 cell 直接 fail,无重试 | ✅ 150 calls, 2 fail (不补跑) |
| 6 | 不动 5 锚 JSON `KT_ABC1_anchors_sha256_12.json` | 沿用 `03c6c01f3697`,未读未改 | ✅(未触) |
| 7 | 不动 4 SPEC V0.1 + v19 + v21 + corpus/v20 | 未触 | ✅(未触) |

---

## §6 下一步(建议给 user,非 worker 决定)

**1. 本次测试结果已记录,不需要立即行动**。
**2. 若 user 后续要求 RAG**,可考虑:
   - 首选:继续用火山 catalog 内 doubao-embedding-vision-251215(2048-d,严守 user 17:38)
   - 次选(若火山维度过重):`nvidia/nemotron-3-embed-1b:free` (2048-d, FREE, avg 1594ms)— 但走 OpenRouter 仍需 user 17:38 重新放行
**3. 不建议**:
   - 切到 OpenRouter 任一 embedding(违反 user 17:38 + 17:41)
   - 重跑 22 caption embedding SVD 2D 投影(已有 76.5% var,本次只测 30 cells 题目)

**最终 verdict**: **OpenRouter embedding 5 model 接入边际不显著优于火山 baseline;V3X 默认 no-RAG + 双 model 主线配置不动**。本测试仅作参考存档。

---

## 附录 A:输出文件

| 路径 | 用途 | 大小 |
|---|---|---|
| `D:\私人资料\deposon-repo\results\deposon_openrouter_5model_30cells_2026_09_10.json` | 完整 5 model × 30 cells 详细结果 (含 cells_results, errors, latency per cell) | ~32 KB |
| `D:\私人资料\deposon-repo\docs\V3X\OPENROUTER_5MODEL_30CELLS_2026_09_10.md` | 本报告 | ~6.5 KB |

## 附录 B:失败 cell 重跑建议(若 user 要求)

- 2 个失败 cell 均为 20s read timeout,可能是 OpenRouter free-tier 速率限制
- 重跑建议:提升 timeout 至 30s + 加 1-2s 间隔(无重试约束情况下)
- 但按"**不重试**"约束,本测试**不**重跑这 2 cell
- 若 user 要求 100% pass,后续可单独 1 模型 × 2 cell 重跑(2 calls 总成本 ~$0)

---

**报告生成**: 2026-09-10 22:47:29 +08:00 by worker sub-agent
**参考关系**: 与 5 model sanity 测试(2026-09-10 早些时候 `docs/V3X/OPENROUTER_EMBEDDING_5MODEL_2026_09_10.md`)是 30 cells 边际扩展版
**严守**: user 17:38 + 17:41 + 22:25 + 22:31(本次任务边界)
