# GPT-6 via TeamoRouter (.cn) — 30 Cells 边际验证 (15 GSM8K + 15 StrategyQA)

**日期**:2026-09-10 17:05-17:30 (CST)
**执行人**:Worker 子代理(`mvs_f82cdcdc226043cd85721df8c1f9f3bf`)
**任务来源**:parent `mvs_bbeb804b1a6a41109be740636eed1709`
**结果文件**:`results/deposon_gpt6_teamorouter_30cells_2026_09_10.json`
**运行脚本**:`scripts/gpt6_30cells_2026_09_10.py` (v2:硬超时 120s via thread)

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
| max_tokens | **1024** (从 256 提到 1024,给 GPT-6 足够空间) |
| timeout | **120s** (从 60s 提到 120s,避免偶发 timeout) |
| 硬超时 | thread-based wall-clock 120s + `socket.setdefaulttimeout(125s)` 双保险 |
| 数据源 | GSM8K cells 1-15 + StrategyQA cells 1-15 |
| prompt 模板 | GSM8K: `Question: {q}\nAnswer in one number:` / StrategyQA: `Question: {q}\nAnswer Yes or No:` |
| 评估 | GSM8K:数字提取(优先 `Answer: X`,否则末位数字),`abs(pred-gt)<1e-3` / StrategyQA:提取 Yes/No(取出现更晚的) |

---

## §2 1-cell sanity 结果

| 测试 | 状态 | 现象 | 备注 |
|---|---|---|---|
| `GET /v1/models` | **200 OK** | 220ms,40 models 列表,gpt-6-astra 确认存在 | 模型含 claude-fable-5, claude-opus-4-8, gpt-6-astra 等 |
| `POST /chat/completions` "What is 1+1?" | **200 OK** | 1902ms,返回 `"1 + 1 = 2."` | sanity 通过,端到端可达 |

**base_url `.cn` 验证**:40 models 中包括 gpt-6-astra,与上轮 5-cell smoke 一致(沿用同 base_url)。

---

## §3 30 cells 结果

### §3.1 GSM8K (15 cells)

| Cell | ID | ground truth | predicted | correct? | ms | 备注 |
|---|---|---|---|---|---|---|
| 1 | 1 (saleswoman) | 18.0 | 18 | ✓ | 15309 | 直接答出 |
| 2 | 2 (Tom's ship) | 5.0 | 5 | ✓ | 9747 | |
| 3 | 3 (Doubtfire kittens) | 40.0 | 40 | ✓ | 14667 | |
| 4 | 4 (Janet brooch) | 1430.0 | 1430 | ✓ | 3686 | |
| 5 | 5 (Jim TV) | 36.0 | 36 | ✓ | 19226 | |
| 6 | 6 (Marilyn record) | 8000.0 | null | ✗ | **120097** | **HARD_TIMEOUT** 120s |
| 7 | 7 (Lee hurdles) | 36.0 | 36 | ✓ | 3030 | |
| 8 | 8 (Jamal phone) | 6.0 | 6 | ✓ | 2682 | |
| 9 | 9 (Bobby videos) | 40.0 | 40 | ✓ | 1896 | |
| 10 | 10 (Jordan video games) | 140.0 | null | ✗ | **120074** | **HARD_TIMEOUT** 120s (read op timeout) |
| 11 | 11 (Johnny toys) | 2125.0 | null | ✗ | **120025** | **HARD_TIMEOUT** 120s |
| 12 | 12 (Anakin beach) | 32.0 | 32 | ✓ | 57972 | 慢但答对(57.9s) |
| 13 | 13 (toys in room) | 50.0 | 50 | ✓ | 8033 | |
| 14 | 14 (Rani crabs) | 122.0 | 122 | ✓ | 8692 | |
| 15 | 15 (3 tickets) | 34.0 | 34 | ✓ | 4424 | |

**GSM8K 答对率:12/15 = 80%** (3 个 timeout,失败 cells: 6, 10, 11)

### §3.2 StrategyQA (15 cells)

| Cell | ID | ground truth | predicted | correct? | ms | 备注 |
|---|---|---|---|---|---|---|
| 1 | 1 (Voldemort Durmstrang) | Yes | null | ✗ | **120034** | **HARD_TIMEOUT** |
| 2 | 2 (injera Taco Bell) | No | null | ✗ | **120007** | **HARD_TIMEOUT** |
| 3 | 3 (Brazilian Navy) | Yes | null | ✗ | **120016** | **HARD_TIMEOUT** |
| 4 | 4 (retail suited) | No | No | ✓ | 4236 | |
| 5 | 5 (John Gall Stanford) | Yes | Yes | ✓ | 24849 | |
| 6 | 6 (Michael unpopular) | No | No | ✓ | 3086 | |
| 7 | 7 (gay male couples) | No | **Yes** | ✗ | 4530 | **错误回答**:模型倾向 Yes |
| 8 | 8 (Martin Luther sect) | No | No | ✓ | 3367 | |
| 9 | 9 (licensed child driving) | Yes | Yes | ✓ | 51535 | 慢但答对 |
| 10 | 10 (Darth Vader Snape) | No | **Yes** | ✗ | 40541 | **错误回答**:模型倾向 Yes |
| 11 | 11 (Boris Yeltsin 2008) | No | No | ✓ | 18151 | |
| 12 | 12 (fish tonsillitis) | No | No | ✓ | 3298 | |
| 13 | 13 (Tony Bennett children) | Yes | Yes | ✓ | 3154 | |
| 14 | 14 (Bengal cat Sotomayor) | Yes | Yes | ✓ | 40938 | 慢但答对 |
| 15 | 15 (Snowdon Tenzing) | Yes | Yes | ✓ | 6162 | |

**StrategyQA 答对率:10/15 = 66.7%** (3 个 timeout,2 个错误回答;失败 cells: 1, 2, 3, 7, 10)

### §3.3 总体

| 维度 | 数值 |
|---|---|
| 总 cells | 30 |
| 总答对 | **22** |
| 总 timeout | 6 (GSM8K: 3, StrategyQA: 3) |
| 总错误回答 | 2 (StrategyQA: cells 7, 10) |
| **总通过率** | **22/30 = 73.3%** |
| **verdict** | **GRAY** (18-23 区间) |

---

## §4 对比表

| 测试 | 结果 | 备注 |
|---|---|---|
| GPT-6 5 cells smoke (60s timeout) | 4/5 = 80% PASS | GSM8K 4/4 = 100% 答对率(已答对 4/4),1 timeout(60s 偶发) |
| V4.1-Flash 30 cells v3 (max=2048) | 25/30 = 83.3% MARGINAL | 此前 baseline(用于对比边际) |
| **GPT-6 30 cells (本次,120s timeout)** | **22/30 = 73.3% GRAY** | 6 timeout + 2 wrong,**低于 V4.1-Flash 基准 10 pp** |

**关键观察**:

1. **超时率上升(20% vs 4-cell smoke 的 20%)**:6/30 = 20% timeout,集中在 cells 6/10/11(GSM8K)+ cells 1/2/3(StrategyQA)。三个 GSM8K 连续 timeout 之后,模型"恢复"正常响应(7-9 全 PASS),类似 burst 模式。
2. **GSM8K 答对率仍 100%**:在非 timeout 的 12 个 cells 上,GPT-6 答对 12/12 = **100%**,与 5-cell smoke 一致。说明数学推理能力无衰减,**问题在 server-side availability,不在 model 能力**。
3. **StrategyQA 出现 2 个 Yes-bias 错答**:cells 7 和 10 都是模型在 gold=No 时答 Yes,显示 GPT-6 对 StrategyQA 的 binary 判断存在正倾向。**这是一个真实的能力差异**,不是 timeout。
4. **慢 cells(>20s)**:GSM8K 12 (58s), StrategyQA 5/9/14 (25-52s),9 个 cells > 20s(30%)。TeamoRouter .cn 端到端时延波动明显,非恒定。

---

## §5 7 铁律自检

| # | 铁律 | 执行 |
|---|---|---|
| 1 | TeamoRouter key runtime 读 | ✓ `LLM API.txt` GB18030 读 → `os.environ['TEAMOROUTER_API_KEY']` |
| 2 | OpenRouter key 永不入 prompt | ✓ 本任务全程仅用 TeamoRouter key,无 OpenRouter key 出现 |
| 3 | 不设 proxy | ✓ `HTTP_PROXY/HTTPS_PROXY/ALL_PROXY/all_proxy` 全清 |
| 4 | key 永不入 prompt / 永不入 JSON / 永不落盘 | ✓ JSON `auth` 字段 = `sk-teamo-...` 截断(只 `sk-teamo-356` 前 12 位);key 文件未写;所有 completion 无 key |
| 5 | 30 cells 严格(不重试 / 不切 model) | ✓ 6 个 timeout **未重试**,model 严格 `gpt-6-astra`,未切 gpt-5.6-* |
| 6 | 不动 5 锚 JSON `KT_ABC1_anchors_sha256_12.json` | ✓ 沿用 `03c6c01f3697`,未读未写 |
| 7 | 不动 4 SPEC V0.1 冻结版 + v19/v21 frozen JSON | ✓ 未读未写 |

**key 文件处理清单**:
- 读:`C:\Users\Administrator\Desktop\AI\LLM API.txt` (只读,GB18030)
- 写:无
- 网络出:`api.teamorouter.cn` (HTTPS,Authorization: Bearer sk-teamo-...)
- 落盘:仅 `sk-teamo-...` + 前 12 位 `sk-teamo-356` 在 JSON `auth` 字段

---

## §6 下一步(给 user 决策,本次任务不擅自执行)

**判定**:**GRAY(73.3%)**,低于 V4.1-Flash 基准 10 pp。

### 路径 A(继续 GPT-6,降 timeout 影响)
- 实施 3 个补救:
  1. **显式 retry-once on 120s timeout**(单次重试,不计额外 cell 配额)
  2. **切 max_tokens 256 → 1024** 已做,慢但答对
  3. **prompt 加 "Be concise. Answer in one number/word only."** 防 Yes-bias
- 预期 30 cells 重跑 24+/30 = 80%+
- 成本:30 cells × ~3-5K tokens ≈ 100K tokens(20 倍于 5-cell smoke)

### 路径 B(降级到 V4.1-Flash 30 cells)
- 沿用 V4.1-Flash V3 baseline 25/30 = 83.3% MARGINAL
- 不再投入 GPT-6 边际成本
- 缺点:丢失 GPT-6 reasoning 优势(cell 2 reasoning_tokens=16,可能有更复杂推理场景)

### 路径 C(混合策略)
- GPT-6 做 GSM8K(100% 答对率稳定的部分)+ V4.1-Flash 做 StrategyQA(更稳)
- 优点:扬长避短
- 缺点:增加集成复杂度,V3.X 简明性受损

### 路径 D(暂不决策,等 user 直接 say-so)
- 22/30 = 73.3% GRAY 是不上不下的结果,user 一句话定方向:
  - "再跑 30 cells 加 retry" → 走 A
  - "切 V4.1-Flash" → 走 B
  - "混合 model" → 走 C
  - "B V2 启动 5 候选 × 1 周判死" → 立刻启动(无论 GPT-6 / V4.1-Flash)

**不擅自执行下一步** —— 本次任务交付到此为止,等 parent 决策。

---

## 附:已知风险/阻塞

1. **TeamoRouter .cn 20% timeout 率**:6/30 cells 在 120s 客户端 timeout 内未响应。TCP 连接建立成功(`117.185.125.188:443`)但服务端不发 body。可能原因:
   - 服务端 reasoning 超长(类似 cell 2 的 reasoning_tokens,但某些请求触发更慢路径)
   - CDN 边缘节点负载/路由抖动
   - gpt-6-astra 模型本身的请求分布不均
2. **StrategyQA Yes-bias**:cells 7, 10 gold=No 模型答 Yes,显示在 binary 判断上倾向 positive。**这是 model 特性,不是 timeout**。
3. **本任务硬超时为 120s**:若实际服务端可用时延 > 120s(部分 cells 看到 58s),理论上有更多 timeout 风险。retry-once 可缓解。
4. **未触发 fallback**:本次 6 个 timeout 全部走 HARD_TIMEOUT 路径,无 OpenAI/Anthropic 兜底。若 TeamoRouter .cn 全挂,无备份 gateway(OpenRouter 4 路径仍 fail)。
5. **base_url `.cn` 单点依赖**:与 5-cell smoke 一致,如未来 `.cn` 也失效,需提前 plan B(OpenRouter user_id gate 解锁?Nemotron?DeepSeek V4.1?)
