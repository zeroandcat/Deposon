# 海外开源 Model 接入测试 (2026-09-10)

> **核心结论**:**OpenRouter 接入成功** — 5/5 HTTP 200,所有调用从 cn 出口 IP 通过。GPT-6 失败的 region gate 限制(OpenRouter 对 OpenAI/Anthropic/Google 模型按出口 IP gate),对海外开源 model **不适用**。

---

## §1 测试环境

| 项 | 值 |
|---|---|
| Gateway | OpenRouter (`https://openrouter.ai/api/v1/chat/completions`) |
| Model | `nvidia/nemotron-3-ultra-550b-a55b:free` (NVIDIA, US 厂商) |
| Model 选择 | brief 优先级 1 (`llama-3.3-70b-instruct:free`) 不在当前 catalog,自动回退到优先级 3(Nemotron-3-Ultra :free)— 仍满足"海外开源 + 免费 + 不受 region gate" |
| 任务 | GSM8K 单数字回答 |
| 题面 | `results/deposon_benchmark_v1_4_gsm8k_details.json` id 1-5 |
| Prompt | `Question: {q}\nAnswer in one number:` |
| 参数 | temperature=0.0, max_tokens=256 |
| Cells | 5 (与 GPT-6 接入测试对齐) |
| Billing 地址 | 已改 US 虚拟地址(袁祺皓 + 3088204160@qq.com + 1018 SW Main St, Portland, OR 97201 US) |
| Request exit region | **cn**(Mavis worker 跑在 user 本机,出口 IP 在境内) |
| Auth | OpenRouter key 从 `C:\Users\Administrator\Desktop\AI\LLM API.txt` GB18030 读取 → `os.environ['OPENROUTER_API_KEY']` 注入(永不入 prompt / JSON / 落盘) |

---

## §2 5 cells 结果

| Cell | GSM8K id | Expected | Predicted | Match | HTTP | Tokens | Latency |
|---|---|---|---|---|---|---|---|
| 1 | Melanie vacuum | 18.0 | 2.0 | ❌ | 200 | 338 (reasoning=205) | 72.88 s |
| 2 | Tom ship | 5.0 | 5.0 | ✅ | 200 | 220 (reasoning=122) | 16.23 s |
| 3 | Doubtfire kittens | 40.0 | 40.0 | ✅ | 200 | 316 (reasoning=137) | 82.03 s |
| 4 | Janet brooch | 1430.0 | None | — | 200 | N/A | 18.83 s |
| 5 | Jim TV+read 4wk | 36.0 | 36.0 | ✅ | 200 | 293 (reasoning=166) | 53.48 s |

**Reachability summary**:
- **5/5 HTTP 200** ✓ (vs GPT-6 接入测试 0/5 = 全部 403)
- Match 3/5(仅作参考 — Nemotron-3-Ultra 是 reasoning model,256 max_tokens 不足以完成推理+输出最终数字;cell 1 因 `finish_reason=length` 提前截断;cell 4 返回非数字文本)
- 总 tokens:1167,总 latency:243.4 s
- **cost=0** ✓(:free tier 确认生效)

> **重要**:match 2/5 不代表 model 能力差。Nemotron-3-Ultra 是 reasoning model(每 call ~200 reasoning tokens 占用),本 smoke test 的 max_tokens=256 把推理截断了。要拿到 GSM8K 真分数,应禁用 reasoning 模式或上调 max_tokens≥1024。但**这不在本接入测试范围内** — 接入测试只验证 OpenRouter + 此 model 可达性。

---

## §3 与 GPT-6 (openai/gpt-6-astra) 对比

| 维度 | GPT-6 Astra | Nemotron-3-Ultra :free |
|---|---|---|
| HTTP 200 比例 | 0/5 (全 403) | **5/5** ✓ |
| Region gate | 受 OpenRouter 出口 IP gate(改 US billing 无效) | **不受 gate** ✓ |
| 接入成本 | (无法接入) | cost=0(:free) |
| 适配 cn 出口 | ❌ | ✓ |
| 适配公开论文署名 | ❌ | ✓(NVIDIA 开源 + 公开 US 厂商) |

**结论**:对 deposon 公开论文 / arXiv 署名场景,海外开源 model(:free 或低付费)是**唯一可行路线**。OpenAI/Anthropic/Google 系模型在中国出口 IP 下不可达。

---

## §4 关键诚实声明

1. **接入测试 ≠ 完整判死**。本次只验证 "OpenRouter + 此 model 在 cn 出口 IP 下可达",**不**等价于 "此 model 在 deposon 30-cell benchmark 上 5/5 PASS"。要进入判死阶段需另跑 30 cells。

2. **5 cells 限制部分违反 — 自我披露** ⚠️:
   - **原计划**:总计 5 次 API call,5 cells,无重试
   - **实际情况**:Worker early-on 不熟悉 bash 后台 auto-resume 机制,重复启动了 step2 脚本;实际累计 **10 次 API call(2 × 5 cells)**。落盘 JSON 为第二次结果(第二次写覆盖第一次)。
   - **影响**:Reachability 结论不变(5/5 HTTP 200 两次都成立); match_rate 略有变化(第一次 2/5,第二次 3/5)。最终落盘文件仍为 5 cells 结构。
   - **修复**:JSON 中已加 `honest_disclosure` 字段;报告 §7 已加备注。**下次类似任务只启动 1 个 step2 后台并等 auto-resume。**

3. **Model 自动回退 = 1 次,不是 5 次**。Brief 优先级 1 不在 catalog 时,我按 brief 列表的优先级 3 选 model,这一选择对所有 5 cells 生效,未在 cells 之间再次切换。

4. **request exit region = cn,只验证 model 自身是否过 region gate**。OpenRouter 对 OpenAI/Anthropic/Google 的 gate 是按"调用方出口 IP"判定的(改 billing 无效),开源 model 是否同样受限是本次测试的目的。

5. **本测试不评估 GSM8K 真分数**。Reasoning model + max_tokens=256 的 prompt 配置不是该 model 的最佳用法,2/5 match 仅供参考。

---

## §5 7 铁律自检

| # | 铁律 | 状态 |
|---|---|---|
| 1 | API key runtime 读 + GB18030 | ✅ 从 `LLM API.txt` GB18030 读入,`os.environ` 注入 |
| 2 | key 永不入 prompt / JSON / 落盘 | ✅ JSON `auth` 字段仅写 `sk-or-v1-... (key loaded from env...)` 占位;无任何文件含完整 key |
| 3 | 5 cells 限制(不重试 / 不切换 / 不调 6 个) | ⚠️ **部分违反** — 因 worker 重复启动 step2 脚本,实际 10 次 API call(2 × 5 cells),落盘仍为 5 cells。已在 `honest_disclosure` 字段记录。|
| 4 | 不动 5 锚 JSON `KT_ABC1_anchors_sha256_12.json` | ✅ 未读取 / 未修改 |
| 5 | 不动 4 SPEC V0.1 冻结版 | ✅ 未读取 / 未修改 |
| 6 | 不动 v19 frozen JSON | ✅ 未读取 / 未修改 |
| 7 | 结果落盘(审计用,不含 key) | ✅ `results/deposon_overseas_open_smoke_2026_09_10.json` + `docs/V3X/OVERSEAS_OPEN_SMOKE_2026_09_10.md` 已写,均无 key |

---

## §6 下一步建议(供父 agent 决策)

| 触发条件 | 建议 |
|---|---|
| **本次 5 cells 中 5/5 HTTP 200 = 接入成功** ✓ | 可考虑 **30 cells 边际验证**(对同一 model,改 reasoning off / max_tokens=1024,验证 GSM8K 真分数) |
| 若 30 cells ≥ 24/5 (80%) | model 候选进入下一步(可审计 LLM 议价 / 别家 :free 横向比较) |
| 若 30 cells < 24/5 | 切换下一优先级(只剩 Mistral Large 2407 付费,或换非 OpenRouter 通道) |
| 不建议 | 立即全量 100 cells — 边际 30 cells 已能给出足够判死信号 |

**保留硬约束**:即便下一步上 30 cells,5 锚 JSON / 4 SPEC V0.1 / v19 frozen JSON 仍不动;key 仍只走 env;审计用 JSON / MD 仍不落 key。

---

## §7 文件清单

- 结果 JSON: `D:\私人资料\deposon-repo\results\deposon_overseas_open_smoke_2026_09_10.json` (~6 KB,5 cells + summary)
- 交付报告: `D:\私人资料\deposon-repo\docs\V3X\OVERSEAS_OPEN_SMOKE_2026_09_10.md` (本文件)
- 测试脚本: `D:\私人资料\deposon-repo\tools\step1_verify.py` (key 加载 + catalog 验证)
- 测试脚本: `D:\私人资料\deposon-repo\tools\step2_overseas_smoke.py` (5 cells GSM8K,**实际跑 2 次,见 §4 第 2 条 self-disclosure**)
- **未创建任何含完整 key 的文件**

---

**Worker handoff**: 本次任务闭环。5/5 HTTP 200 确认海外开源 model 接入 OpenRouter 不受 region gate 限制;match 2/5 为 reasoning model + 短 max_tokens 配置问题,非接入问题。父 agent 拿到本结果即可决策是否进入 30 cells 边际验证。
