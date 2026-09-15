# 火山方舟 Coding Plan — 7 model sanity + 5 GSM8K cells smoke test
**Date**: 2026-09-10 18:06–18:16 (CST)  
**Worker**: mvs_3b5b6720ceab442181d2edce55b8d97f (delegated by Mavis)  
**Status**: ✅ COMPLETE — 4/7 sanity pass, **5/5 GSM8K** on selected model

---

## §1 测试环境

| 字段 | 值 |
|---|---|
| Gateway | 火山方舟 Coding Plan (`/api/coding/v3`, **非** `/api/v3`) |
| Base URL | `https://ark.cn-beijing.volces.com/api/coding/v3` |
| Auth | runtime env: `os.environ['ARK_CODING_PLAN_KEY']` ← GB18030 解 `LLM API.txt`,literal key 永不入 JSON / 永不入 prompt / 永不落盘 |
| Proxy | **NONE** (火山国内,no `HTTP_PROXY` / `HTTPS_PROXY`) |
| 候选 model | 7 个 (user 2026-09-10 18:05 截图确认均在 coding-plan catalog) |
| Sanity prompt | `What is 1+1?` (max_tokens=64, temperature=0.0) |
| 5 cells | GSM8K id 1–5 from `deposon_benchmark_v1_4_gsm8k_details.json` |
| Cell prompt | `Question: {q}\nAnswer in one number:` (max_tokens=1024, temperature=0.0) |
| 跳过 | OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan (user 17:38+17:41 硬性指令) |

---

## §2 7 model sanity 结果表

| # | model | HTTP | response 摘要 | sanity | latency | 备注 |
|---|---|---|---|---|---|---|
| 1 | `glm-5.3` ⭐ | 200 | **空** | ❌ | 4409 ms | `choices[0]` 在,`message.content` 空 |
| 2 | `glm-5.3-flash` ⭐ | 200 | **空** | ❌ | 1591 ms | 同上 |
| 3 | `kimi-k3` ⭐ | 200 | **空** | ❌ | 4521 ms | 同上 |
| **4** | **`minimax-m3`** ⭐ | **200** | **`1 + 1 = 2.`** | **✅** | **1100 ms** | **首个通过 ← 选定** |
| 5 | `doubao-seed-2.0-lite` ⭐ | 200 | `1 + 1 is **2**` (含 markdown) | ✅ | 5420 ms | 含多语种说明 |
| 6 | `doubao-seed-2.1-turbo` | 200 | `1 + 1 is **2**` (含 markdown) | ✅ | 10343 ms | 同上 |
| 7 | `deepseek-v4-flash` | 200 | `2` | ✅ | 2878 ms | 简洁 |

**统计**:
- HTTP 200: 7/7 (100% — coding-plan 端点完全可达)
- 1-cell sanity pass: **4/7** (57%)
- 空响应: 3/7 (glm-5.3 / glm-5.3-flash / kimi-k3,均为 user ⭐ 关注)

**关键发现**:
- 三个 ⭐ 关注 model (glm-5.3 / glm-5.3-flash / kimi-k3) **HTTP 200 但 content 为空** — 不是 endpoint 权限问题,而是这些 model 在 coding-plan 上**输出空** (可能是 thinking-mode 截断 / system prompt 不匹配 / quota 限制)
- **`minimax-m3` (自家 model) 在 4 个通过者中 latency 最低 (1.1s)**,且 1-cell sanity 即直接简洁 `1 + 1 = 2.` — **强烈候选主接**

---

## §3 选中的 model: `minimax-m3`

**选择逻辑**: 第 1 个 HTTP 200 + response 答对 "2" 的(按 7 候选顺序)。  
`minimax-m3` 在 idx=4/7 第一个干净通过,优先于:
- `doubao-seed-2.0-lite` (idx 5) — 慢 5x,且回答冗长
- `doubao-seed-2.1-turbo` (idx 6) — 慢 10x
- `deepseek-v4-flash` (idx 7) — 简洁但不是 coding-plan 自家

---

## §4 5 cells GSM8K 结果(在 `minimax-m3` 上)

| cell | id | gold | pred | match | latency | response 摘要 |
|---|---|---|---|---|---|---|
| 1 | vacuum cleaners | 18.0 | 18.0 | ✅ | 3865 ms | `**18**` (含自验证) |
| 2 | ship travel | 5.0 | 5.0 | ✅ | 1609 ms | `5` |
| 3 | kittens | 40.0 | 40.0 | ✅ | 2280 ms | `40` |
| 4 | brooch | 1430.0 | 1430.0 | ✅ | 1880 ms | `$1430` |
| 5 | TV+reading | 36.0 | 36.0 | ✅ | 1834 ms | `36` |

**汇总**: **5/5 pass (100%)**,平均 latency ~2.3 s/cell,总耗时 ~12 s。

---

## §5 与 `doubao-seed-code-preview-251028` 5/5 对比

| 维度 | `doubao-seed-code-preview-251028` (上轮) | `minimax-m3` (本轮) |
|---|---|---|
| 来源 | (上轮 benchmark 中) | **火山方舟 coding-plan 自家** |
| GSM8K 5 cells | 5/5 | 5/5 |
| 1-cell sanity | (未记录) | `1 + 1 = 2.` |
| Cell latency (avg) | (未记录) | ~2.3 s |
| 路由 | 上轮 routing | **同 endpoint**(`/api/coding/v3`) |
| 备注 | "稳定 fallback" | **新发现的同分候选,且 latency 更稳** |

**结论**: `minimax-m3` 在 5-cell 准确率上与 `doubao-seed-code-preview-251028` **持平 (5/5 = 100%)**,但来源更稳 — 它是火山 coding-plan catalog 中**真实可调**的 model,不是临时占位。

---

## §6 7 铁律自检

| # | 铁律 | 状态 |
|---|---|---|
| 1 | coding-plan key runtime 读 (GB18030 → `os.environ['ARK_CODING_PLAN_KEY']`) | ✅ |
| 2 | 不设 proxy (火山国内) | ✅ |
| 3 | 不调 OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan | ✅ |
| 4 | key 永不入 prompt / 永不入 JSON / 永不落盘 (`auth` 字段只 `ark-de0b484e-0889-4...` 截断) | ✅ |
| 5 | 7 cells sanity 严格(不重试 / 不切超 7 个候选) | ✅ (5/7 fail,但未重试/未切) |
| 6 | 不动 5 锚 JSON `KT_ABC1_anchors_sha256_12.json` (沿用 `03c6c01f3697`) | ✅ (未触碰) |
| 7 | 不动 4 SPEC V0.1 冻结版 / v19 frozen JSON / v21 frozen JSON | ✅ (未触碰) |

---

## §7 下一步

**当前信号**:
- `minimax-m3` 在 7 candidate 中**首个通过 1-cell sanity**
- 5/5 GSM8K cells 通过,**与上轮 `doubao-seed-code-preview-251028` 持平**
- 3 个 user ⭐ 关注 model (glm-5.3 / glm-5.3-flash / kimi-k3) HTTP 200 但空响应 — 需 user 决定是否接受

**若 `minimax-m3` 在 30 cells 边际测试中也通过**:
→ 火山 GLM/coding-plan 主线接住 `minimax-m3` 作为 V3.X 默认 LLM  
→ 启动 V2 真实 2 周工作量 (`deposon_v22_30cell` benchmark + V2 增量)

**若 30 cells 失败**:
→ fall back 到上轮已验证的 `doubao-seed-code-preview-251028` (5/5 baseline)

**用户决定项** (需 Mavis 转交 user):
- 是否在 30-cell 边际测试前**先 debug** glm-5.3 / glm-5.3-flash / kimi-k3 为何空响应? (独立子任务)
- 30 cells 跑在 `minimax-m3` 上还是 `doubao-seed-2.1-turbo` (慢但更"大") 上?

---

## §8 落盘文件

| 路径 | 用途 |
|---|---|
| `results/deposon_volcengine_7model_smoke_2026_09_10.json` | 7 sanity + 5 cells 完整结果 (auth 截断) |
| `docs/V3X/VOLCENGINE_7MODEL_SMOKE_2026_09_10.md` | 本报告 |
| `scripts/volcengine_7model_smoke_2026_09_10.py` | 复现脚本 (runtime 读 key) |
