# Volcengine 9-Model Smoke Test (2026-09-10)

> 路径:`D:\私人资料\deposon-repo\results\deposon_volcengine_9model_smoke_2026_09_10.json`
> 测试时间:2026-09-10 20:30–20:43 (CST)
> 触发:user 18:28 截图 9 个候选 model,排除 `kimi-k3`(成本高)
> 测试人:Worker 子代理 (Mavis)

---

## §1 测试环境

- **Gateway**:火山方舟 Coding Plan
- **Endpoint**:`https://ark.cn-beijing.volces.com/api/coding/v3/chat/completions`
- **Base URL**:`/api/coding/v3` (非 `/api/v3`,避免额外计费)
- **Auth**:key 在 runtime 加载到 `os.environ['ARK_CODING_PLAN_KEY']`;**literal key 永不写盘 / 不入 prompt / 不入 JSON**(JSON 中只记 `ark-de0b484e-...` 截断 + 描述)
- **Proxy**:**未设置**(火山国内,无需 proxy)
- **节省原则**:sanity 30s timeout / 5-cell 60s timeout / 不重试 / 不切超 9 个候选

---

## §2 9 Model 横向对比表

| # | Model | http_status | sanity (1+1) | 5 cells 结果 | pass_rate | avg latency |
|---|---|---|---|---|---|---|
| 1 | `doubao-seed-2.0-lite` | 200 | ✅ "2" | T T T T T | **5/5** | 4532 ms |
| 2 | `kimi-k2.7-code` | 200 | ✅ "2" | T T T T T | **5/5** | **2511 ms** ⭐ |
| 3 | `minimax-m3` | 200 | ✅ "2" | – T T T T | 4/5 (cell1 60s timeout) | 14037 ms |
| 4 | `doubao-seed-2.1-turbo` | 200 | ✅ "2" | T T T T T | **5/5** | 12590 ms |
| 5 | `deepseek-v4-flash` | 200 | ✅ "2" | T T T T T | **5/5** | 4026 ms |
| 6 | `glm-5.3` | 200 | ✅ "2" | T T T T T | **5/5** | 3201 ms |
| 7 | `doubao-seed-evolving` | 200 | ✅ "1 plus 1 equals 2.\n\n2" | T T T T T | **5/5** | 8388 ms |
| 8 | `glm-5.3-flash` | 200 | ✅ "2" | ✱ T T T T | 4/5 (parser bug,见 §3) | 1973 ms |
| 9 | `deepseek-v4-pro` | 200 | ✅ "2" | T T T T T | **5/5** | 3697 ms |

**Sanity 通过率**:9/9 (100%)
**5-cell 全过率**:7/9 (78%,除 minimax-m3 cell1 timeout 和 glm-5.3-flash parser 误判)

---

## §3 最佳 Model 选定

**`kimi-k2.7-code`** — 5/5 pass + 最低 avg latency (2511 ms)

### 选定理由
1. **正确率**:5/5 全过,无 timeout / 无解析异常
2. **速度**:平均 2511 ms,比 5/5 同组第二名 `glm-5.3` (3201 ms) 快 ~22%
3. **稳定性**:无 cell 异常,5 cell latency 都落在 1.8–3.5s 区间(方差小)
4. **可用性**:与 user 排除的 `kimi-k3` 是不同 model(`k2.7-code` vs `k3`),`k2.7` 不在排除清单

### 备选 (5/5 同组)
- `glm-5.3` — 3201 ms(中文 CoT 输出格式美观)
- `deepseek-v4-flash` — 4026 ms(性价比高,flash 版本)
- `deepseek-v4-pro` — 3697 ms
- `doubao-seed-2.0-lite` — 4532 ms(lite 版本最便宜)
- `doubao-seed-2.1-turbo` — 12590 ms(较慢但稳定)
- `doubao-seed-evolving` — 8388 ms(慢,CoT 长)

### 失败 case 备注
- **`minimax-m3` cell 1**:60s timeout(模型在长问题卡住,后续 4 cell 正常)→ **不建议**用于长 prompt GSM8K
- **`glm-5.3-flash` cell 1**:模型输出 `"**18**\n\nCheck: ... 5 left. ✓"`,首答正确,但末段验证说明含 "5",**parser 取末位数字误判**为 5.0 → **建议**:prompt 加 `"Answer with just the number, no explanation"`,或重写 parser 取首位"**"包围数字

---

## §4 与之前 Baseline 对比

| Model | Pass Rate | 备注 |
|---|---|---|
| **`kimi-k2.7-code`** (本次) | **5/5** | 2511 ms,新最快 5/5 |
| `glm-latest` (2026-09-10) | 5/5 | 旧 baseline,慢于 kimi |
| `doubao-seed-code` (历史) | 24/30 | 30 cells (8x 难度) |
| `V4.1-Flash` (历史) | 25/30 | 30 cells |
| `kimi-k3` (历史) | excluded | 太贵,user 排除 |

**注**:本次 5 cells ≠ 30 cells(8x 难度),**直接对比 pass_rate 数字不公平**。但从 speed 维度看 `kimi-k2.7-code` 在 5 cells 上明显领先,且通过率与 `glm-latest` 一致(5/5)。**建议下一步跑 30 cells 边际测试**确认可推广性。

---

## §5 7 铁律自检

| # | 铁律 | 状态 |
|---|---|---|
| 1 | coding-plan key runtime 读 (`os.environ['ARK_CODING_PLAN_KEY']`) | ✅ 验证 |
| 2 | 不设 proxy | ✅ 验证 (`HTTP_PROXY` 等全 strip) |
| 3 | 不调 OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan | ✅ 仅火山 coding-plan |
| 4 | key 永不入 prompt / JSON / 落盘 | ✅ JSON 中只 `ark-de0b484e-...` 截断 |
| 5 | 9 model × 5 cells 严格 (不重试 / 不切超 9 候选) | ✅ 9 model 全测,无 retry |
| 6 | 不动 5 锚 JSON `KT_ABC1_anchors_sha256_12.json` | ✅ 未触 |
| 7 | 不动 4 SPEC V0.1 冻结版 + v19 / v21 frozen JSON | ✅ 未触 |

---

## §6 下一步(待 user 选)

### 路径 A:跑 30 cells 边际(推荐)
- 候选:`kimi-k2.7-code` (本次最快) / `glm-5.3` (本次第二) / `deepseek-v4-flash` (性价比)
- 选 1 个跑 30 cells(沿用 `volcengine_glm_latest_30cells_v2_runner_2026_09_10.py` 框架,改 model 名即可)
- 目的:确认 5 cells 5/5 在 30 cells 上仍 ≥ 24/30(80%),即非过拟合小样本

### 路径 B:启动 V2 真实 2 周工作量
- 选 1 个 5/5 model 作为 V2 主推理后端
- 在 v19/v21 frozen JSON 上跑 deposon benchmark
- 输出真实 5-7 候选的 trap-hit 率

### 路径 C:多 model 并行 30 cells
- 同时跑 `kimi-k2.7-code` + `glm-5.3` + `deepseek-v4-flash` 三个 30 cells
- 输出三方对比表(更稳,代价 = 3x 时间)

**本报告结束,等待 user 选路径。**
