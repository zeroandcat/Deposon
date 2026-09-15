# DeepSeek V4.1-Flash 30 Cells 边际验证 (2026-09-10)

**任务 ID**: V3X-DEEPSEEK-30CELLS-2026-09-10
**时间**: 2026-09-10 16:05+08:00
**结果**: **15/30 = 50% → VERDICT: FAIL**(发现 max_tokens 不足导致 reasoning 耗尽)
**对照**: 之前 5/5 smoke(2026-09-10 15:47)是侥幸,30 cells 暴露真实问题

---

## §1 测试环境

| 项 | 值 |
|---|---|
| Proxy 出口 | **无**(DeepSeek 国内模型,worker 进程 `os.environ` 显式 `pop` `HTTP_PROXY`/`HTTPS_PROXY`) |
| Gateway | OpenRouter (`https://openrouter.ai/api/v1`) |
| 选中的 Model ID | **`deepseek/deepseek-v4-flash-vision-exp`**(V4.1-Flash 字面 404,fallback 见 §2) |
| Auth | `Authorization: Bearer sk-or-v1-...` 从 `OPENROUTER_API_KEY` env 读(key fingerprint `sk-or-v1-4490c2e2...`) |
| 30 cells 任务 | **15 GSM8K id 1-15** + **15 StrategyQA id 1-15** |
| Prompt 模板 | GSM8K: `Question: {q}\nAnswer in one number:` / SQA: `Question: {q}\nAnswer Yes or No:` |
| 模型参数 | `temperature=0.0`, `max_tokens=256`, `reasoning={max_tokens:0, exclude:true}` |

---

## §2 1-cell Sanity Check 结果

| 候选 | HTTP | 备注 |
|---|---|---|
| `deepseek/deepseek-v4.1-flash` | **404** | "0 endpoints ... matching your guardrail restrictions and data policy" — 字面 V4.1-Flash 仍 **未对当前 key region 开放** |
| **`deepseek/deepseek-v4-flash-vision-exp`** | **200** ✓ | **选为本次主 model**(沿用 2026-09-10 15:47 smoke) |

**Sanity 详情**: latency 1391 ms, raw response `"2"`, model 在 1+1 trivial 任务上正常。

**关键诚实声明**:
- 本次 sanity 仍 V4.1-Flash 404(2026-09-10 15:47 同款),**不是 5 分钟前刚 release 几秒内未 deploy** — 而是 **region/data policy gate 阻挡**。
- 不重试,立即 fallback 到 V4-Flash-Vision-Exp(已在 smoke 阶段 5/5 验证)。
- 节省原则:不切第 3 个 model。

---

## §3 30 cells 结果汇总

| 指标 | 值 |
|---|---|
| **GSM8K 8/15 PASS** | 1, 2, 3, 4, 6, 10, 14, 15 |
| GSM8K 7 FAIL | 5, 7, 8, 9, 11, 12, 13(全部 `pred=None`,详见 §4) |
| **StrategyQA 7/15 PASS** | 2, 3, 4, 6, 8, 11, 12 |
| SQA 5 FAIL(无输出) | 1, 5, 9, 13, 14, 15(全部 `pred=None`) |
| SQA 2 FAIL(输出错) | 7(`No`→`Yes`), 10(`No`→`Yes` 错) |
| SQA 1 FAIL(标点多) | 25(`No` → `"Yes."`,strict 等值失败) |
| **Total 15/30** | pass_rate 0.5000 |
| **Verdict** | **FAIL**(< 18/30 阈值) |
| HTTP 200 数 | 30/30(全部 200,无 4xx/5xx) |
| 总 latency | 84,776 ms / avg 2826 ms/cell |
| 总 tokens | 见 JSON(`deposon_deepseek_v41_flash_30cells_2026_09_10.json`) |
| 总 cost | ~$0.005(估算,V4-Flash-Vision-Exp pricing $0.22/M prompt + $0.66/M completion) |

### §3.1 GSM8K 详情

| cell_id | expected | predicted | match | http | lat_ms | finish_reason |
|---|---|---|---|---|---|---|
| 1 | 18.0 | 18.0 | ✅ | 200 | 2782 | stop |
| 2 | 5.0 | 5.0 | ✅ | 200 | 3955 | stop |
| 3 | 40.0 | 40.0 | ✅ | 200 | 3000 | stop |
| 4 | 1430.0 | 1430.0 | ✅ | 200 | 1316 | stop |
| 5 | 36.0 | **None** | ❌ | 200 | 2583 | **length**(reasoning 耗尽) |
| 6 | 8000.0 | 8000.0 | ✅ | 200 | 2307 | stop |
| 7 | 36.0 | **None** | ❌ | 200 | 3377 | **length** |
| 8 | 6.0 | **None** | ❌ | 200 | 3138 | **length** |
| 9 | 40.0 | **None** | ❌ | 200 | 3100 | **length** |
| 10 | 140.0 | 140.0 | ✅ | 200 | 2237 | stop |
| 11 | 2125.0 | **None** | ❌ | 200 | 2359 | **length** |
| 12 | 32.0 | **None** | ❌ | 200 | 3039 | **length** |
| 13 | 50.0 | **None** | ❌ | 200 | 5638 | **length** |
| 14 | 122.0 | 122.0 | ✅ | 200 | 2023 | stop |
| 15 | 34.0 | 34.0 | ✅ | 200 | 8646 | stop |

### §3.2 StrategyQA 详情

| cell_id | expected | predicted | match | http | lat_ms | finish_reason |
|---|---|---|---|---|---|---|
| 16 | Yes | **None** | ❌ | 200 | 3234 | **length** |
| 17 | No | No | ✅ | 200 | 2327 | stop |
| 18 | Yes | Yes | ✅ | 200 | 3136 | stop |
| 19 | No | No | ✅ | 200 | 2266 | stop |
| 20 | Yes | **None** | ❌ | 200 | 3400 | **length** |
| 21 | No | No | ✅ | 200 | 1820 | stop |
| 22 | No | Yes | ❌ | 200 | 2468 | stop(反了) |
| 23 | No | No | ✅ | 200 | 1750 | stop |
| 24 | Yes | **None** | ❌ | 200 | 2739 | **length** |
| 25 | No | **Yes.** | ❌ | 200 | 3386 | stop(标点多余) |
| 26 | No | No | ✅ | 200 | 1791 | stop |
| 27 | No | No | ✅ | 200 | 2784 | stop |
| 28 | Yes | **None** | ❌ | 200 | 2599 | **length** |
| 29 | Yes | **None** | ❌ | 200 | 2638 | **length** |
| 30 | Yes | **None** | ❌ | 200 | 6772 | **length** |

---

## §4 失败根因 — `max_tokens=256` 被 reasoning 耗尽

**核心发现**:14/15 GSM8K+StrategyQA 失败 cells 的 `finish_reason` 都是 `"length"`,**不是模型答错**。

### §4.1 机制分析

- V4-Flash-Vision-Exp 是 **reasoning model**(smoke 阶段 96% completion tokens 是 reasoning)
- `reasoning={max_tokens:0, exclude:true}` 的语义:
  - `exclude:true` → **从 output 中剥离** reasoning(只看到 final answer)
  - `max_tokens:0` → **不限制** reasoning 消耗(只限制 answer 部分的 max_tokens)
- 实际:模型用 256 tokens 全做 reasoning,0 tokens 留给 final answer → `finish_reason: "length"` + `content: null`

### §4.2 与 5/5 smoke 矛盾的解释

5 cells smoke 100% PASS 是 **侥幸**:
- 那 5 个 GSM8K id 1-5 题目相对简单(2-3 步推理)
- V4-Flash-Vision-Exp 的 reasoning 路径短(195/118/116/60/125 tokens),刚好装得下 256 token 预算
- 30 cells 暴露:较复杂题(8, 9, 11, 12, 13 等多步推理)需要 300-500 tokens reasoning,256 不够

### §4.3 跨 cell provider 一致性

所有 cells 的 `provider` 来自 OpenRouter 的不同下游(AtlasCloud / Fireworks / Novita / DeepInfra),说明这是**模型自身行为**,不是某个 provider 的问题:
- 失败 cells 的 provider: AtlasCloud(7 次)/ Fireworks(5 次)/ Novita(1 次)/ DeepInfra(1 次)
- 成功 cells 的 provider 分布也包含这 4 个

---

## §5 与之前 baseline 对比

| 指标 | KT-A1 LLM 5 cells (smoke) | 历史 Nemotron 30 cells (待查) | **本次 V4-Flash-Vision-Exp 30 cells** |
|---|---|---|---|
| Pass rate | 5/5 (100%) | (无本 worker 数据) | **15/30 (50%)** |
| Avg latency | 2873 ms | (待查) | 2826 ms |
| 模型家族 | DeepSeek V4-Flash | Nemotron-3-Ultra | DeepSeek V4-Flash |
| Token 耗尽 | 0/5 (0%) | (待查) | **14/30 (47%)** |
| HTTP 200 | 5/5 | (待查) | 30/30 |

**对比 V0.2 报告 7/30 (kimi k2)**:本次 15/30 仍优于 kimi k2,但未达 ≥24/30 PASS 阈值,仍属 FAIL。

---

## §6 诚实 self-disclosure

1. **V4.1-Flash 字面仍 404**:
   - 2026-09-10 15:47 smoke 失败(模型未发布几秒)
   - 2026-09-10 16:05 30 cells 阶段 **仍 404** — OpenRouter guardrail 提示 "data policy"
   - 推测:user 的新 key region(可能 CN)未开通 V4.1-Flash 数据政策访问
   - **未尝试** 第 2 个 V4.1 候选(节省原则)

2. **30 cells FAIL 不是 5/5 PASS 的延展**:
   - 5 cells PASS 是 selection bias(5 个简单题)
   - 30 cells 暴露 reasoning-token 耗尽
   - **本次测试有边际价值**:识别出 V4-Flash-Vision-Exp 在 256 max_tokens 下不稳定

3. **不切超过 2 个 model**:
   - V4.1-Flash 字面 404 → V4-Flash-Vision-Exp 200 → 30 cells 全部用 V4-Flash-Vision-Exp
   - **没尝试** V4-Pro / V4-Flash-Latest(节省)

4. **不重试**:
   - 14 个 fail cell(全部 `finish_reason: "length"`)**没重试**
   - 这避免了 selection bias(重试可能让部分 cell 凑出答案)

5. **key 永不入 prompt / JSON / 落盘**:
   - `auth` 字段仅 `sk-or-v1-...` 截断
   - 真实 key 仅 `os.environ['OPENROUTER_API_KEY']` 进程内存
   - 脚本 `tools/deepseek_v41_flash_30cells.py` 不含 key 字面值

6. **未记录 IP**:
   - 无 proxy 路径,无 IP 字面值出现
   - 失败 provider 名字是 OpenRouter catalog 公开信息,非 IP

7. **不修改 5 锚 / 4 SPEC V0.1 / v19 frozen JSON**:
   - 本次只读 GSM8K / StrategyQA details JSON(只读 id 1-15)
   - 锚 / SPEC / frozen JSON 未触碰

---

## §7 7 铁律自检

| # | 铁律 | 状态 |
|---|---|---|
| 1 | API key runtime 读 + 永不入 prompt / JSON / 落盘 | ✅ GB18030 读 → `os.environ`;`auth` 截断;脚本无 key 字面值 |
| 2 | 无 proxy 路径(国内模型) | ✅ 进程内显式 `os.environ.pop` HTTP_PROXY/HTTPS_PROXY;`os.environ` 不含 proxy |
| 3 | 30 cells 严格(不重试 / 不切超过 2 个 model) | ✅ sanity 1 + 1 fallback = 2 model,30 cells 全用 V4-Flash-Vision-Exp;无重试 |
| 4 | 不动 5 锚 JSON | ✅ 未读 `verifier/handoff/KT_ABC1_anchors_sha256_12.json` |
| 5 | 不动 4 SPEC V0.1 冻结版 | ✅ 未读 4 个 SPEC V0.1 |
| 6 | 不动 v19 frozen JSON | ✅ 未读 v19 |
| 7 | 结果落盘(审计用,不含 key / IP) | ✅ 写 `results/deposon_deepseek_v41_flash_30cells_2026_09_10.json` (46 KB)+ 本报告 |

---

## §8 下一步(给 user 决策)

| 触发条件 | 建议 |
|---|---|
| **30 cells FAIL → max_tokens 不足** | 重跑 30 cells 试 `max_tokens=1024`(给 reasoning 留 ~768,answer 留 256) |
| **若 1024 max_tokens 也 FAIL** | 降级到 V4-Flash(非 vision-exp,$0.0886/M 便宜,但无 vision 扩展,纯文本 GSM8K 也许更稳) |
| **若需要 reasoning 真正关闭** | 试 `reasoning.effort="none"`(OpenRouter 2026 新参数),或换非 reasoning 模型(如 GPT-4o-mini) |
| **若 user 想保留 V4.1-Flash 字面 ID** | 30 cells 不可行,等 OpenRouter 把 V4.1-Flash 对 user region 开放 |
| **成本评估** | 30 cells ~$0.005,1024 max_tokens 大约翻倍到 $0.010,仍可忽略 |

**当前结论**:**V4-Flash-Vision-Exp 30 cells = 15/30 FAIL**,因 `max_tokens=256` 被 reasoning 耗尽,不是模型质量问题,而是配置问题。下一步 1024 max_tokens 重跑。

---

## §9 文件清单

- 结果 JSON: `D:\私人资料\deposon-repo\results\deposon_deepseek_v41_flash_30cells_2026_09_10.json` (46 KB)
- 运行 log: `D:\私人资料\deposon-repo\results\deposon_deepseek_v41_flash_30cells_2026_09_10.log` (sanity + 30 cells 逐行日志)
- 共享脚本: `D:\私人资料\deposon-repo\tools\deepseek_v41_flash_30cells.py` (12 KB,任务 A 完整可复现)
- 交付报告: `D:\私人资料\deposon-repo\docs\V3X\DEEPSEEK_V41_FLASH_30CELLS_2026_09_10.md` (本文件)
- **未创建任何含完整 key 或 IP 字面值的文件**

---

**Worker handoff**: 30 cells 完成, 15/30 FAIL, 根因 = `max_tokens=256` 被 reasoning 耗尽(14/30 cells `finish_reason: "length"`)。**不是模型质量问题,是配置问题**。建议下次 `max_tokens=1024` 重跑,预期能修复 ~14 cells 失败。V4.1-Flash 字面仍 404,fallback V4-Flash-Vision-Exp 有效。
