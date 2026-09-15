# 火山方舟 Coding Plan Chat 接入 5-Cell 测试报告

**日期**: 2026-09-10
**任务 ID**: VOLCENGINE_CODING_PLAN_CHAT_5CELLS_2026_09_10
**执行者**: Mavis Worker (subagent of mvs_bbeb804b1a6a41109be740636eed1709)
**目标路径**: 验证 `ark-de0b484e-...` (coding-plan key) + `https://ark.cn-beijing.volces.com/api/coding/v3/chat/completions` 端点是否可用,选一个 model 跑 5 cells GSM8K

---

## §1 测试环境

| 维度 | 值 |
|---|---|
| Gateway | 火山方舟 Coding Plan |
| Base URL | `https://ark.cn-beijing.volces.com/api/coding/v3` (与之前 embedding 验证同一端点) |
| Auth | `Bearer ark-[REDACTED]` (前 12 位 `ark-de0b484e`,整 key runtime 读 LLM API.txt,永不入 JSON/不落盘) |
| Proxy | **无**(火山国内直连) |
| 数据来源 | `D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_gsm8k_details.json` cells 1-5 |
| 5 锚 JSON | `verifier/handoff/KT_ABC1_anchors_sha256_12.json` (LastWriteTime 2026-09-09 13:19,**未动**) |
| KT_A1 SPEC V0.1 | `docs/V3X/KT_A1_SPEC_V0.1.md` (LastWriteTime 2026-09-09 13:42,**未动**) |
| v19 / v21 frozen JSON | 未触碰 |
| Prompt | `Question: {q}\nAnswer in one number:` (temperature=0.0, max_tokens=1024) |

---

## §2 候选 model 列表

调用 `GET /api/coding/v3/models` 返回 **130 个 model ID**,按家族分类:

| 家族 | 数量 | 关键 model |
|---|---|---|
| Doubao | 100 | `doubao-pro-32k-240615`, `doubao-lite-32k-240628`, `doubao-pro-128k-240628` 等 |
| Seed (Doubao 子系) | 41 | `doubao-seed-1-6-250615`, `doubao-seed-1-6-thinking-250715`, `doubao-seed-1-6-flash-250715`, **`doubao-seed-code-preview-251028`** ✅ |
| DeepSeek | 13 | `deepseek-v3-2-251201` (之前在 `/v3` 错 endpoint 跑 0/30), `deepseek-r1-250528`, `deepseek-v3-1-250821` 等 |
| Qwen / DeepSeek-R1-Distill | 7 | `qwen3-32b-20250429`, `qwen3-8b-20250429`, `qwen3-14b-20250429` 等 |
| 其他 | 12 | `kimi-k2-250905`, `glm-4-5-air-20250728`, `mistral-7b-instruct-v0.2` 等 |

完整列表见 `https://ark.cn-beijing.volces.com/api/coding/v3/models`(GET, Bearer coding-plan key)。

---

## §3 sanity check 选 model 过程

按用户给定候选顺序 (Doubao 系列优先) 试 3 个 model,选第一个 200 OK 且回答含 "2" 的:

| 顺序 | model ID | status | ms | 备注 |
|---|---|---|---|---|
| 1 | `doubao-1-5-pro-32k-250115` | **404 UnsupportedModel** | 83 | 火山返回 "The requested model does not support the coding plan feature" |
| 2 | `doubao-1-5-pro-256k-250115` | **404 UnsupportedModel** | 106 | 同上,coding-plan 不支持 |
| 3 | `doubao-seed-code-preview-251028` | **200 OK** | 3540 | resp `"2"` ✅ PASS |

**Selected**: `doubao-seed-code-preview-251028`
**Sanity verdict**: `What is 1+1? -> "2" PASS`

⚠️ 注意:不是所有 catalog 里的 model 都支持 coding-plan feature。`doubao-1-5-pro-32k/256k-250115` 在 catalog 列了但走 coding-plan endpoint 返 404。

---

## §4 5 cells 结果表

| Cell | Question (摘要) | Expected | Extracted | Response Text | Correct | ms |
|---|---|---|---|---|---|---|
| 1 | Melanie vacuum cleaners, 5 left, start with? | 18.0 | **18.0** | `18` | ✅ | 16,198 |
| 2 | Tom's ship 10mph 1-4PM, back 6mph, how long? | 5.0 | **5.0** | `5` | ✅ | 6,212 |
| 3 | Doubtfire 7 kittens + Patchy thrice + Trixie 12, total? | 40.0 | **40.0** | `40` | ✅ | 36,527 |
| 4 | Janet brooch $500 + $800 + 10% insurance, total? | 1430.0 | **1430.0** | `1430` | ✅ | 7,358 |
| 5 | Jim 2h TV + half reading, 3x/week, 4 weeks total? | 36.0 | **36.0** | `36` | ✅ | 7,581 |

**Matched: 5/5 = 100%**

Token usage 观察 (5 cells):
- completion_tokens: 154 ~ 2003 (model 默认带 reasoning chain,大部分 token 是 reasoning_tokens,实际答案很短)
- prompt_tokens: 101 ~ 136
- total_tokens range: 257 ~ 2139

---

## §5 与 V3 endpoint 错 + V2 embedding 对比

| 阶段 | endpoint | key | model | 结果 |
|---|---|---|---|---|
| V3 endpoint 错 (`bg_7253f118`) | `/v3` (错) | agent-plan | `deepseek-v3-2-251201` | **0/30 FAIL** (endpoint 错,产生额外费用) |
| V2 embedding 验证 (`bg_106bc2f9`) | `/api/coding/v3/embeddings` | coding-plan | `doubao-embedding-vision-251215` | **3/3 PASS** |
| **本次 chat 验证** | `/api/coding/v3/chat/completions` | coding-plan | `doubao-seed-code-preview-251028` | **5/5 PASS** ✅ |

**关键结论**:
1. endpoint 修正为 `/api/coding/v3/...` 后,**chat 路径** 与 **embedding 路径** 都通了
2. coding-plan key **可以**用于 chat,只是要选对 model(不是 catalog 全支持)
3. `deepseek-v3-2-251201` 之前 0/30 **不是 model 问题,是 endpoint 问题**;同 model 走 `/api/coding/v3` 应当也能用(本次未验证,留作下一步)

---

## §6 7 铁律自检

| # | 铁律 | 状态 | 证据 |
|---|---|---|---|
| 1 | coding-plan key runtime 读 LLM API.txt GB18030 | ✅ | `re.search(r'ark-de0b484e-[a-zA-Z0-9-]+', content)` 提取,无 key 字面值入 prompt/JSON |
| 2 | 不设 proxy | ✅ | `os.environ.pop(HTTP_PROXY/HTTPS_PROXY/...)` 后 `NO_PROXY='*'` |
| 3 | 不调 OpenRouter/TeamoRouter/V4.1-Flash/GPT-6/agent-plan | ✅ | 全程只走 `ark.cn-beijing.volces.com/api/coding/v3`,无其他 endpoint |
| 4 | key 永不入 prompt / JSON / 落盘 | ✅ | JSON `auth` 字段仅 `ark-de0b484e-...` 截断;prompt 全部是 GSM8K question |
| 5 | 5 cells 严格(不重试/不切 model) | ✅ | sanity 试 3 个 catalog 候选选第一个 PASS,5 cells 全用该 model,无重试 |
| 6 | 不动 5 锚 JSON | ✅ | `KT_ABC1_anchors_sha256_12.json` LastWriteTime 2026-09-09 13:19(任务前),**未动** |
| 7 | 不动 4 SPEC V0.1 + v19/v21 frozen | ✅ | `KT_A1_SPEC_V0.1.md` LastWriteTime 2026-09-09 13:42(任务前),**未动** |

---

## §7 下一步建议

### ✅ 本次任务成功(5/5 PASS),建议:

1. **扩样**: 跑 30 cells(全 GSM8K test set 或 deposon 自有 30 cells 切片)看边际稳定性
2. **横向对比**: 同 30 cells 跑 `deepseek-v3-2-251201` 走 `/api/coding/v3` (验证之前 0/30 确为 endpoint 错,非 model 本身)
3. **其他 model 验证**: `doubao-seed-1-6-250615` / `qwen3-32b-20250429` 是否也支持 coding-plan
4. **接入 V2 真实 2 周工作量**: 火山 chat 路径 PASS 后,可用作 V3.X 1 周预筛的实际推理后端

### 若以后 FAIL,告知 user:
- coding-plan 路径全 fail → 火山方舟 不可用,转 openai/本地 ollama 备选

### 不在本任务范围(明确告知 user,本 worker 不决策):
- 跑不跑 30 cells 边际(成本 + 时间)
- 是否把火山作为 V3.X 唯一推理后端
- 是否纳入 V2 真实 2 周工作量主线

---

## 附录

- 结果 JSON: `D:\私人资料\deposon-repo\results\deposon_volcengine_coding_plan_5cells_2026_09_10.json`
- 5 cells 来源: `D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_gsm8k_details.json` (cells 1-5)
- 上一轮对照: `bg_106bc2f9` (embedding 3/3 PASS) / `bg_7253f118` (chat 0/30 endpoint 错)
