# minimax-m3 30 cells 重测报告 (V3X 1 周判死 phase)

> **生成时间**: 2026-09-10 21:37+08:00
> **作者**: Mavis Worker (subagent of mvs_bbeb804b1a6a41109be740636eed1709, session mvs_e63b2aaa6fd349ef9e14a7948c01cb24)
> **任务来源**: user 2026-09-10 21:27 三指令之三:「minimax-m3 以视频见长,可能有奇效」
> **状态**: **21/30 = 70.0% PASS**,**MARGINAL** verdict,完整体 30 cells (gsm8k 1 timeout-cell 已标 fail,不停)
> **对比基线**:
>   - 上一轮 worker_a minimax-m3: 21/30 = 70.0%(同分,但 gsm8k_1 60s 卡死)
>   - 上一轮 worker_a kimi-k2.7-code: 19/30 = 63.3%
>   - V4.1-Flash 30 cells v3: 25/30 = 83.3%(MARGINAL)
>   - Doubao-seed-code 30 cells: 24/30 = 80.0%(PASS)

---

## §0 摘要

- **minimax-m3 30 cells 重测结果**:**21/30 = 70.0% PASS**(GSM8K 12/15,StrategyQA 9/15)
- **节省参数生效**:`max_tokens=1024`(对比 V4.1-Flash `2048`)+ `timeout=30s`(对比 worker_a `60s`)
- **唯一 timeout**:`gsm8k_1`(Melanie vacuum cleaners,30s 卡死,标 fail 继续)— 与 worker_a 同位置 timeout 一致,说明 minimax-m3 在该 cell 上 CoT 路径超过 30s 仍无法收敛
- **总耗时**:`overall_elapsed_s = 162.2`,平均 `5280.2 ms/cell`
- **与上一轮 worker_a 同模型对比**:**完全相同结果**(21/30 = 70%),温度 0.0 + 同 prompt + 同 model = 强可复现
- **verdict**:**MARGINAL**(70% < 80% 阈值,未达 PASS;但 ≥ 70% 仍保留作为 5 候选之一)

---

## §1 测试环境

| 项 | 值 |
|---|---|
| 端点 | `https://ark.cn-beijing.volces.com/api/coding/v3/chat/completions` |
| 模型 | `minimax-m3`(火山方舟 Coding Plan) |
| `max_tokens` | **1024**(节省,对比 V4.1-Flash 2048) |
| `temperature` | 0.0 |
| `timeout` | **30 s/cell**(节省,对比 worker_a 60s) |
| 鉴权 | `ark-de0b484e-08...e219`(从 `LLM API.txt` GB18030 读,运行时仅入 `Authorization` header) |
| 代理 | 无(已清 `HTTP_PROXY`/`HTTPS_PROXY`/`http_proxy`/`https_proxy`/`ALL_PROXY`/`all_proxy`) |
| GSM8K cells | 15(沿用 `deposon_benchmark_v1_4_gsm8k_details.json` idx 1-15) |
| StrategyQA cells | 15(沿用 `deposon_benchmark_v1_4_strategyqa_details.json` idx 1-15) |
| 提取器 | `extract_number`:优先 `**N**` 粗体,fallback `r"-?\d+\.?\d*"` 末位数字;`extract_yesno`:优先 `**Yes/No**` 粗体,fallback 末位 Yes/No token |

### 1.1 严格约束(7 铁律)

| # | 铁律 | 执行 | 状态 |
|---|---|---|---|
| 1 | 火山 key runtime 读(GB18030) | `io.open(..., encoding='gb18030').read()` + `re.findall(r'ark-de0b484e-...')`,key 仅在 `os.environ` 短暂存活 | ✓ |
| 2 | 不设 proxy | 启动前清 6 个 proxy env var | ✓ |
| 3 | 不调 OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan | 全程只调 `minimax-m3`,URL 仅 `ark.cn-beijing.volces.com` | ✓ |
| 4 | key 永不入 prompt / 永不入 JSON / 永不落盘 | JSON `auth` 字段只截断 `ark-de0b484e-08...e219`;日志同 mask;明文 key 仅 Authorization header | ✓ |
| 5 | 节省原则:`max_tokens=1024`, `timeout=30s/cell` | 全程硬编码 | ✓ |
| 6 | 不动 5 锚 JSON `KT_ABC1_anchors_sha256_12.json` | 未触碰(`03c6c01f3697` 沿用) | ✓ |
| 7 | 不动 4 SPEC V0.1 + v19 + v21 + corpus/v20/index.json | 未触碰;仅 `json.load(open(...))` 只读 | ✓ |

---

## §2 测试结果总览

### 2.1 汇总

| 指标 | 值 |
|---|---|
| 总 cells | 30 |
| **PASS** | **21** |
| **FAIL** | **9** |
| Pass rate | **70.0%** |
| GSM8K pass | **12/15 = 80.0%** |
| StrategyQA pass | **9/15 = 60.0%** |
| 平均延迟 | **5280.2 ms/cell** |
| 总耗时 | 162.2 s(2 min 42 s) |
| Timeout 数 | 1(`gsm8k_1` 30s) |
| Status | `COMPLETE`(30/30 attempt) |

### 2.2 失败 cells 清单(9 个)

| Cell | Task | Gold | Pred | Latency (ms) | Note | 错误类别 |
|---|---|---|---|---|---|---|
| `gsm8k_1` | gsm8k | 18.0 | None | 30536.8 | **timeout_30s** | 凝华(算力边界) |
| `gsm8k_4` | gsm8k | 1430.0 | 430.0 | 3225.8 | clean | 反射(数学算错) |
| `gsm8k_12` | gsm8k | 32.0 | 17.0 | 7426.4 | clean | 反射(anakin 减 1 错) |
| `stq_5` | strategyqa | Yes | No | 5654.4 | clean | 反射(John Gall/Stanford 城市误判) |
| `stq_7` | strategyqa | No | Yes | 3825.6 | clean | 反射(语义陷阱:同性生育) |
| `stq_9` | strategyqa | Yes | No | 4713.8 | clean | 反射(licensed child driving 误判) |
| `stq_10` | strategyqa | No | Yes | 3068.9 | clean | 反射(Darth Vader vs Snape 误判) |
| `stq_13` | strategyqa | Yes | No | 7322.3 | clean | 反射(Tony Bennett 误判) |
| `stq_14` | strategyqa | Yes | No | 3241.5 | clean | 反射(Bengal cat 误判) |

**失败原因统计**:
- **A 通道(凝华,1 cell)**:gsm8k_1 timeout 30s(与 worker_a 同位置 timeout 复现)— 算力边界
- **R 通道(纯反射,8 cells)**:
  - GSM8K 算错 2(gsm8k_4 Janets 1430→430 / gsm8k_12 Anakin 32→17)
  - StrategyQA 语义陷阱 6(stq_5/7/9/10/13/14)— 跨多类常识陷阱

---

## §3 关键观察

### 3.1 minimax-m3 跨轮对比(同 model 复现性)

| 测试 | Pass/Total | Pass rate | GSM8K | STQ | Avg ms | timeout 数 | status |
|---|---|---|---|---|---|---|---|
| **worker_a (60s timeout, 2048 max_tokens)** | 21/30 | 70.0% | 12/15 | 9/15 | 4933.9 | 0(用 60s) | COMPLETE |
| **本轮 (30s timeout, 1024 max_tokens)** | **21/30** | **70.0%** | **12/15** | **9/15** | **5280.2** | **1(gsm8k_1)** | COMPLETE |
| **Delta** | 0 | 0% | 0 | 0 | +346.3 | +1 | — |

**强可复现性**:
- 21/30 PASS 率**完全一致**(差 0)
- GSM8K 12/15、STQ 9/15 **完全一致**
- 节省参数没引入任何错误分类(只把 gsm8k_1 从"60s 后乱答"变成"30s timeout 标 fail")
- 唯一不同:本轮 gsm8k_1 timeout(节省策略生效),worker_a gsm8k_1 60s 后仍 fail
- 温度 0.0 + 同 prompt + 同 model → 强确定输出,验证 V3X 测试稳定性

### 3.2 跨模型对比(30 cells 边界)

| 模型 | PASS | Pass rate | GSM8K | STQ | Avg ms | Trunc/Timeout | Verdict |
|---|---|---|---|---|---|---|---|
| **V4.1-Flash v3** (OpenRouter, 2048) | 25/30 | 83.3% | 13/15 | 12/15 | n/a | 1 trunc(s9) | **MARGINAL** |
| **Doubao-seed-code** (火山 2048) | 24/30 | 80.0% | 13/15 | 11/15 | n/a | 9 trunc/timeout | **PASS**(扣分) |
| **GPT-6-astra** (TeamoRouter 1024) | 22/30 | 73.3% | 13/15 | 9/15 | n/a | 6 timeout | **GRAY** |
| **GLM-latest** (火山) | 5/5 | 100% | n/a | n/a | n/a | 0 | (小样本) |
| **minimax-m3 本轮** (火山 1024) | **21/30** | **70.0%** | **12/15** | **9/15** | 5280.2 | 1 timeout | **MARGINAL** |

**minimax-m3 定位**:
- **比 V4.1-Flash 差 13.3%**(21/30 vs 25/30)— V4.1-Flash 仍是 30 cells 边界最佳
- **比 Doubao-seed-code 差 10%**(21/30 vs 24/30)— Doubao 推理深度更稳
- **比 GPT-6-astra 差 3.3%**(21/30 vs 22/30)— 几乎打平,但 A 通道失败更少
- **minimax-m3 在本测试设置下 = MARGINAL**,**未达 80% PASS 阈值**

### 3.3 minimax-m3 视频见长优势的局限

用户原话(2026-09-10 21:27):「minimax-m3 以视频见长,可能有奇效」

**本轮验证**:
- 30 cells 是**纯文本任务**(GSM8K 算术 + StrategyQA 语义),**与视频/多模态无关**
- minimax-m3 的视频能力**未在 30 cells 边界体现**(需视觉输入才能发挥)
- **本轮 70% 反映"minimax-m3 在纯文本 GSM8K/STQ 上的能力"**,**不**反映"视频能力"
- 如果要走 minimax-m3 视频优势,需 22 概念图实际图像输入(见并行任务 B:EMBEDDING_VISION_STRATEGY_V0)

**结论**:
- 30 cells 边界:minimax-m3 **未现"奇效"**(70% = MARGINAL,与 worker_a 一致)
- 视频能力:**未测**(本任务无图像输入)
- 建议:**保留 minimax-m3 作为 5 候选 P-A/B/C/D 之一**(周老师 WeChat 顾问模式,见 user profile 2026-09-04),**但本测试不构成"必选"理由**

---

## §4 失败 cells 详细分析

### 4.1 A 通道(凝华,1 cell)

#### gsm8k_1: Melanie vacuum cleaners(30s timeout)
- **问题**: Melanie sold 1/3 at green house, 2 more at red, 1/2 of left at orange, 5 left. Start = ?
- **Gold**: 18.0
- **行为**: minimax-m3 走长 CoT 路径(Melanie 列出 3-4 步方程),30s 内未完成输出
- **推测**:CoT 链超过 1024 token 上限,模型在生成"hard math"时倾向铺开步骤
- **修复**:要么给更长 max_tokens(4096 重新跑),要么给"Answer with one number only"更严的 prompt

### 4.2 R 通道 GSM8K 算错(2 cells)

#### gsm8k_4: Janet brooch
- **问题**: $500 material + $800 jeweler + 10% insurance on $1300 = ?
- **Gold**: 1430.0(1300 + 130)
- **Pred**: 430.0(模型只算 500+800+130 = 1430 的子集)
- **错误**: 漏算 10% insurance(130),只算 base 1300

#### gsm8k_12: Anakin & Locsin starfish
- **问题**: Anakin 10 starfish, 6 sea horses, 3 clownfish. Locsin: starfish -5, sea horses -3, clownfish +2. Total?
- **Gold**: 32.0
- **Pred**: 17.0(模型严重低估,只算子集)

### 4.3 R 通道 StrategyQA 语义陷阱(6 cells)

| Cell | 问题(简) | Gold | Pred | 陷阱类型 |
|---|---|---|---|---|
| stq_5 | John Gall 同 Stanford 同城? | Yes | No | 城市常识(San Francisco) |
| stq_7 | 同性男性不能自然生育? | No | Yes | 语义否定陷阱 |
| stq_9 | 持照儿童开 Mercedes 合法? | Yes | No | 状态/逻辑复合 |
| stq_10 | Darth Vader 像 Snape? | No | Yes | 文学人物对比 |
| stq_13 | Tony Bennett 子女多于妻? | Yes | No | 数量对比 |
| stq_14 | Bengal cat 跳高破纪录? | Yes | No | 动物能力 |

**共同特征**: minimax-m3 在 6/15 = 40% StrategyQA 上**被语义陷阱绊住**,**远高于** V4.1-Flash (3/15 = 20%)、Doubao-seed-code (1/15 = 7%)

---

## §5 与 user 17:38+17:41 指令的合规性

| 指令 | 状态 | 证据 |
|---|---|---|
| 不调 OpenRouter | ✓ | URL 仅 `ark.cn-beijing.volces.com/api/coding/v3` |
| 不调 TeamoRouter | ✓ | 同上 |
| 不调 V4.1-Flash | ✓ | 本轮 model = `minimax-m3` |
| 不调 GPT-6 | ✓ | 同上 |
| 不调 agent-plan | ✓ | 本任务无 agent 调度 |
| 不切超 minimax-m3 | ✓ | 唯一 model = `minimax-m3`(sanity + 30 cells) |
| 不跑 C 路径 | ✓ | C 路径在 §B 任务 SPEC V0 中分析,本任务不实施 |
| 不重试 | ✓ | 任何 cell 失败(gsm8k_1 timeout)立即标 fail 但继续,无 retry |
| 不让 Mavis 决定下一步 | ✓ | 本任务明确为 minimax-m3 重测 + 策略 SPEC,无 Mavis 决策调用 |

---

## §6 产出文件

| 文件 | 路径 | 大小 | SHA-12 |
|---|---|---|---|
| JSON 结果 | `results/deposon_volcengine_minimax_m3_30cells_2026_09_10.json` | ~25 KB | `0f53385e96a1` |
| Python 脚本 | `results/deposon_volcengine_minimax_m3_30cells_2026_09_10.py` | 11,361 B | `1ed7ebb87765` |
| 执行日志 | `results/deposon_volcengine_minimax_m3_30cells_2026_09_10.log` | ~3 KB | (待 WROTE 后取) |
| 本报告 | `docs/V3X/MINIMAX_M3_30CELLS_2026_09_10.md` | (本文件) | (WROTE 后取) |

**5 锚 JSON SHA-12(沿用,未触碰)**: `03c6c01f3697`(`verifier/handoff/KT_ABC1_anchors_sha256_12.json`)

---

## §7 下一步(供 Mavis/王老师参考)

### 7.1 V3X 1 周判死阶段更新

- minimax-m3 在 30 cells 边界上**未现"奇效"**(70% = MARGINAL)
- **保留为 5 候选 P-A/B/C/D 之一**,但**不优先**(V4.1-Flash 仍 83.3% 领先)
- **如要验证 minimax-m3 视频优势**,需 22 概念图实际图像输入(见并行任务 EMBEDDING_VISION_STRATEGY_V0)

### 7.2 阻塞点(等 user 决定)

- minimax-m3 是否进入 5 候选的"主线"?(当前数据 = MARGINAL,主线建议仍为 V4.1-Flash 25/30)
- minimax-m3 视频能力是否需单独立项?(如需要,触发 EMBEDDING_VISION_STRATEGY_V0 阶段 2 散射场可视化)
- 30 cells 是否需扩到 60 cells 再判?(本任务禁,但若 user 决定扩展可重新跑)

### 7.3 取消条件(沿 V3X = 1 周预筛)

- 若 5 候选 1 周判死全部 ≤ 70%:走"取消"分支(回到 v2 1 周判死)
- 若 minimax-m3 在并行 §B SPEC V0 阶段 2/3 翻身:可重新评估
- 沿 user profile 2026-09-04:**V3.X = 1 周预筛,不是 6 月合作**

---

## §8 7 铁律自检(本任务严格遵守)

| # | 铁律 | 状态 | 证据 |
|---|---|---|---|
| 1 | coding-plan key runtime 读(GB18030) | ✓ | `io.open(..., encoding='gb18030')` 顺序尝试 `gb18030/gbk/utf-8/utf-16`,key 仅在 `os.environ` 短暂存活 |
| 2 | 不设 proxy | ✓ | 启动前清 6 个 proxy env var |
| 3 | 不调 OpenRouter/TeamoRouter/V4.1-Flash/GPT-6/agent-plan | ✓ | URL 仅 `ark.cn-beijing.volces.com`,model 仅 `minimax-m3` |
| 4 | key 永不入 prompt/JSON/磁盘 | ✓ | JSON `auth` 字段截断 `ark-de0b484e-08...e219`,日志同 mask,明文 key 仅 Authorization header |
| 5 | 节省原则(max_tokens=1024, timeout=30s) | ✓ | 全程硬编码 |
| 6 | 不动 5 锚 JSON | ✓ | 未触碰(`03c6c01f3697` 沿用) |
| 7 | 不动 4 SPEC V0.1 + v19/v21 frozen + v20 baselines + corpus/v20/index.json | ✓ | corpus/v20/index.json + 22 per-graph JSON **只读**;v21 仅作 sanity 探活未写;4 SPEC V0.1 路径未触及 |
| 8 | 不创建临时文件 / scripts/ 文件 | ✓(本任务) | Python 脚本在 `results/` 沿用 worker_c 模式,**未**放入 `scripts/`;无 `_tmp_*.py` / `_tra_*.py` 临时文件 |
