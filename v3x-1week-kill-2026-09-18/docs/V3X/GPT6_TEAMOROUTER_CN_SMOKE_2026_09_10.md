# GPT-6 via TeamoRouter (.cn) — 5-Cell GSM8K Smoke Test

**日期**:2026-09-10 16:55-17:00 (CST)
**执行人**:Worker 子代理(`mvs_d2b35682a0134c9f81e3c09ad1f67e82`)
**任务来源**:parent `mvs_bbeb804b1a6a41109be740636eed1709`
**结果文件**:`results/deposon_gpt6_teamorouter_cn_2026_09_10.json`

---

## §1 测试环境

| 项 | 值 |
|---|---|
| Gateway | TeamoRouter |
| base_url | `https://api.teamorouter.cn/v1` (user 2026-09-10 16:55 确认:.cn 不是 .com) |
| auth | `sk-teamo-...` (前 12 位 `sk-teamo-356b3`,runtime 读,JSON 截断,key 永不入文件) |
| model | `gpt-6-astra` (TeamoRouter `/v1/models` 字面 GPT-6;不 fallback gpt-5.6-*) |
| proxy | **无**(TeamoRouter 自带海外 endpoint) |
| temperature | 0.0 |
| max_tokens | 256 |
| prompt 模板 | `Question: {q}\nAnswer in one number:` |
| 数据源 | `results/deposon_benchmark_v1_4_gsm8k_details.json` cells 1-5 |
| 评估 | 数字提取(优先 `Answer: X`,否则末位数字),`abs(pred-gt)<1e-3` 算 correct |

---

## §2 base_url 验证(.cn vs .com)

| URL | 状态 | 现象 | 备注 |
|---|---|---|---|
| `https://api.teamorouter.com/v1/models` | BLOCKED | DNS 解析到 Facebook IP 段 (31.13.x.x) | **域名被抢注**,前 worker `bg_914691da` 在此 fail |
| `https://api.teamorouter.cn/v1/models` | **200 OK** | 220ms,返回 40 models,4 个 GPT-6 候选 | user 2026-09-10 16:55 纠正后正确 |

**TeamoRouter 提供的 GPT-6 候选**(从 `/v1/models` 过滤 `gpt`+`6`):
1. `gpt-5.6-luna`
2. `gpt-5.6-sol`
3. `gpt-5.6-terra`
4. `gpt-6-astra` ← **选这个**(字面 GPT-6 Astra,严格按任务要求)

附加观察:`kimi-k3` 也存在(确认 user memory 2026-09-08 纠正:产品名 KIMI-K3,不是 k2)。

---

## §3 5 cells 结果

| Cell | GSM8K ID | ground truth | predicted | correct? | status | ms | 备注 |
|---|---|---|---|---|---|---|---|
| 1 | 1 (saleswoman) | 18.0 | 18.0 | ✓ | 200 | 4152 | 直接答出 |
| 2 | 2 (Tom's ship) | 5.0 | 5.0 | ✓ | 200 | 4425 | reasoning_tokens=16 |
| 3 | 3 (Doubtfire kittens) | 40.0 | 40.0 | ✓ | 200 | 4798 | prompt 94 toks |
| 4 | 4 (Janet brooch) | 1430.0 | 1430.0 | ✓ | 200 | 28992 | **大 prompt**:prompt_tokens=4449,cached=4352,服务端波动 |
| 5 | 5 (Jim TV) | 36.0 | null | ✗ | **-1 (60s timeout)** | 60028 | 单次偶发 timeout,**未重试** |

**核心数字**:
- 5 cells 完成率:4/5 (80%)
- GSM8K 答对率(在完成 cells 上):**4/4 = 100%**
- 1 个 timeout(cells 5):60s 客户端 timeout,服务端可能长推理或网络抖动
- 4 个 200 OK cells 全部答对 ground truth(无幻觉、无算错)

**usage 总览**:
- 总 tokens 约 5K(包含 cell 4 大 prompt 4449)
- completion tokens 极短(5-27,模型非常简洁)
- cell 2 出现 `reasoning_tokens=16`,cell 4 出现 `cached_tokens=4352` → TeamoRouter 端有 reasoning + cache 机制

---

## §4 对比表:OpenRouter 4 路径 + TeamoRouter .com + TeamoRouter .cn

| 路径 | 结果 | 原因 |
|---|---|---|
| OpenRouter 直接 | 0/20 全 403 | layer-2 user_id gate 绑死 `user_3J7P6ghveKjYjvgV8u3JEyBq4Dm`,4 路径全 fail |
| TeamoRouter `.com` | BLOCKED at Step 1 | 域名被抢注 → DNS 解析到 Facebook IP 段 (31.13.x.x),前 worker `bg_914691da` 失败 |
| **TeamoRouter `.cn` (本任务)** | **4/5 cells 200 OK + 答对 4/4,1/5 timeout** | user 16:55 纠正域名后正确 |

**关键转换**:OpenRouter 4 路径全 fail → TeamoRouter `.com` 域名被抢注 → TeamoRouter `.cn` base_url 正确,4/5 cells 端到端可达 + GSM8K 答对 100%。

---

## §5 7 铁律自检

| # | 铁律 | 执行 |
|---|---|---|
| 1 | TeamoRouter key runtime 读 | ✓ `LLM API.txt` GB18030 读 → `os.environ['TEAMOROUTER_API_KEY']` |
| 2 | OpenRouter key 永不入 prompt | ✓ 本任务全程仅用 TeamoRouter key,无 OpenRouter key 出现 |
| 3 | 不设 proxy | ✓ `HTTP_PROXY/HTTPS_PROXY/ALL_PROXY` 全清 |
| 4 | key 永不入 prompt / 永不入 JSON / 永不落盘 | ✓ JSON `auth` 字段 = `sk-teamo-...` 截断;key 文件未写;所有 completion 无 key |
| 5 | 5 cells 严格 | ✓ cell 5 timeout 未重试,直接记录为失败 |
| 6 | 不动 5 锚 JSON `KT_ABC1_anchors_sha256_12.json` | ✓ 沿用 `03c6c01f3697` |
| 7 | 不动 4 SPEC V0.1 冻结版 + v19/v21 frozen JSON | ✓ 未读未写 |

**key 文件处理清单**:
- 读:`C:\Users\Administrator\Desktop\AI\LLM API.txt` (只读,GB18030)
- 写:无
- 网络出:`api.teamorouter.cn` (HTTPS,Authorization: Bearer sk-teamo-...)
- 落盘:无 literal key,仅 `sk-teamo-...` 12 字符前缀在 JSON 中

---

## §6 下一步(给 user 决策,本次任务不擅自执行)

**判定**:**接入基本 PASS**(4/5 200 OK + GSM8K 答对 4/4),但有 1 个 timeout 不能算完全 PASS。

**两条路**(需 user 选):

### 路径 A:跑 30 cells 边际验证稳定性(建议)
- 扩大样本到 30 cells(GSM8K cells 6-35),看 timeout 率是否持续 ~20% 还是 ~5% 偶发
- **调 timeout 90-120s**(从 60s 提到 120s,cell 4 用了 29s,120s 留足 buffer)
- 预计 30 cells × 8-30s = 4-15 分钟
- 成本估算:30 cells × ~100 tokens ≈ 3K tokens
- 若 30 cells 答对率 ≥ 90%:正式启动 B V2 真实 2 周工作量

### 路径 B:直接宣布 GPT-6 路径可用,启动 B V2(乐观)
- 当前 4/4 答对已经够强,timeout 视为偶发可接受
- 立即用 30 cells 跑 B V2 5 候选 × 1 周判死(按 user memory 2026-09-04 V3.X = 1 周预筛)
- 风险:30 cells 边际若 timeout 率 > 30%,会拖慢 B V2 节奏

### 路径 C:再次明确要 user 决策 (最稳妥)
- 当前 4/5 PASS 不上不下,user 一句话定方向:
  - "跑 30 cells 再决定" → 走 A
  - "直接启动 B V2" → 走 B
  - "换 model(放弃 GPT-6,用 gpt-5.6-luna)" → 不建议(违反严格 GPT-6 要求)
  - "换 gateway(回到 OpenRouter)" → 已确认 4 路径全 fail,不建议

**不擅自执行下一步** —— 本任务交付到此为止,等 parent 决策。

---

## 附:已知风险/阻塞

1. **cell 5 60s timeout**:原因未明,可能是:
   - 服务端长推理(类似 cell 2 的 reasoning_tokens,但更长)
   - 网络层 jitter
   - gpt-6-astra 模型本身的 1/5 偶发慢响应
2. **cell 4 prompt 4449 tokens**:远高于其他 cells(67-94),cached 4352 提示 prompt 模板或 system message 注入大量 cache
3. **base_url `.cn` 单点依赖**:如未来 `.cn` 也失效,需提前 plan B(OpenRouter user_id gate 解锁?Nemotron?DeepSeek V4.1?)
4. **未验证 `max_tokens=256` 是否需要调高**:cell 4 completion 仅 6 tokens,够用;但若未来加 CoT 需 `max_tokens=512+`
