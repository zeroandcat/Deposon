# GPT-6 Astra vs MiniMax-M3 对照实验 SPEC (V0 草稿)

> **日期**: 2026-09-10  
> **执行方**: Mavis worker（仅写 spec，不调 API）  
> **任务来源**: 工单"等 API 期间可做的 3 件事"第 3 项  
> **状态**: V0 草稿（占位 spec，**实现冻结于等 coding-plan 2h API 恢复 + OpenRouter 验证通过**）

---

## §0.5 已知陷阱:Billing Address 灰区

### 0.5.1 OpenRouter 平台规则
- OpenRouter ToS 明确要求 billing address 与卡片发卡国一致
- US 虚拟地址(Privacy.com / 51101 等)被 OpenRouter 风控识别为"高风险账单地"
- 已知失败模式:首次充值成功 → 第二次扣款被拒 → 余额不退

### 0.5.2 数据出境合规
- 任何 prompt 内容经 OpenRouter 转发至 GPT-6(Astra 后端)
- 走 US 网络路径 → 中国数据出境合规风险
- 内部 V3X 任务族可能含敏感概念域(GSM8K 商业题、StrategyQA 间接涉政、22 受控概念图)
- **必须先在 prompt 层做敏感字段脱敏**(已沿用 4 SPEC V0.1 模板的脱敏协议)

### 0.5.3 余额风险
- OpenRouter 预付费模型,用户已改 US billing address
- 充值到账与扣款独立结算
- 若 OpenRouter 判定 billing 异常 → 可能冻结余额
- **对应 mitigation**:只充 30 cells 所需最小额度(~5 USD),分 2 次充,失败立即停

### 0.5.4 风险等级
- **LOW**(整体):30 cells 边界 + 1 USD 充值 + 已知可失败止损
- **触发升级条件**:OpenRouter 拒收 + 余额冻结 + 数据出境合规投诉任一

---

## §1 简介

### 1.1 背景
- GPT-6 Astra(2026-09-03 上 OpenRouter,$10/$50 per 1M tokens input/output)
- MiniMax-M3(Mavis 自身模型,国内 MiniMax 公司,走 minimax.chat 官方 API)
- V3X 任务族(T1 GSM8K + T2 StrategyQA + T3 22 受控概念图 + T4 50 受控图)
- 用户 2026-09-10 改 OpenRouter billing address 为 US 虚拟地址

### 1.2 目的
- 在 V3X 任务族上做小规模(30 cells)边际对照
- 验证 MiniMax-M3 是否可完全替代 GPT-6(成本/合规优势)
- 决策点:是否在 V3X 后续阶段(M4-M6)全切 MiniMax-M3

### 1.3 非目的
- **不**做模型能力全面评估(只测 V3X 4 任务族)
- **不**做 human eval(纯自动 accuracy)
- **不**做多语言对照(中英 V3X 测试集已固定)
- **不**做 prompt engineering 优化(沿用现有 4 SPEC prompt 模板)

---

## §2 任务族(沿用 V3X SPEC V0.1)

| 任务族 | 来源 | 规模 | 测法 |
|---|---|---|---|
| T1 GSM8K | v19 frozen (800 条) | 10 cells | 算术 + 多步推理 |
| T2 StrategyQA | v19 frozen (792 条) | 10 cells | 隐式推理 + 是/否 |
| T3 22 受控概念图 | deposon_agents 受控生成 | 5 cells | 概念关系判定 |
| T4 50 受控图 | deposon_photonics 受控生成 | 5 cells | 物理场分布理解 |

合计:30 cells × 2 模型 = **60 query**（注：每 cell 1 query，2 模型各 30 query = 总 60 query，非 240 query；240 query 估算以"4 任务族 × 30 cells × 2 模型" 计，但 §3 明确每 cell 1 query，2 模型 = 60 query）

**修正**:§3 算式按"4 任务族 × 30 cells × 2 模型"得 240 query,但实际每 cell 仅 1 query(不重试)→ 60 query。**沿用 60 query,不重做 240**。

---

## §3 实验设计

### 3.1 单元定义
- 1 cell = 1 question × 1 model × 1 query
- 30 cells = 4 任务族按上述规模分配
- 2 模型 = GPT-6 + MiniMax-M3

### 3.2 样本量
- 每 cell 仅 1 query,**不重试**(节省原则 §8)
- 总 query:60(每模型 30)

### 3.3 随机性
- 选 cell:沿用 v19 frozen 顺序,**不 shuffle**(节省原则)
- 模型调用顺序:交替(避免时间漂移)
- 温度:0(各模型默认,确保复现)

---

## §4 测法

### 4.1 指标
| 指标 | 测法 | 单位 |
|---|---|---|
| accuracy | answer 与 v19 gt 精确匹配 | 比例 (0-1) |
| latency | API 调用起止 wall time | 秒 |
| cost | input + output tokens × 模型单价 | USD |

### 4.2 评分规则
- T1 GSM8K:numerical match(允许尾数 0.001 误差)
- T2 StrategyQA:'Yes'/'No' 精确匹配
- T3 概念图:选项序号(A/B/C/D)匹配
- T4 受控图:多选标签集合精确匹配

### 4.3 成本估算
- 平均 query 长度:输入 800 tokens,输出 200 tokens
- GPT-6:30 query × (800 × $10/1M + 200 × $50/1M) = 30 × $0.018 = **$0.54**
- MiniMax-M3:30 query × (800 × $X/1M + 200 × $Y/1M) = 待 Mavis 确认(MiniMax 公开价)
- **预算上限**:$5 USD(两模型合计,含 buffer)

---

## §5 判死标准

### 5.1 PASS
**任一任务族**满足:
- `accuracy(GPT-6) - accuracy(MiniMax-M3) > 5pp`
- **含义**:GPT-6 在该任务族上明显胜出,值得付出 billing 灰区成本

### 5.2 GRAY
**任一任务族**满足:
- `|accuracy(GPT-6) - accuracy(MiniMax-M3)| ≤ 5pp`
- **且** `latency(MiniMax-M3) > 2 × latency(GPT-6)` 或 `cost(MiniMax-M3) > 2 × cost(GPT-6)`
- **含义**:准确率打平但 MiniMax-M3 显著劣,折中选 GPT-6

### 5.3 FAIL
**全部 4 任务族**满足:
- `|accuracy(GPT-6) - accuracy(MiniMax-M3)| ≤ 5pp`
- **且** `latency/cost` 相当(MiniMax-M3 不显著劣)
- **含义**:MiniMax-M3 完全替代 GPT-6,切回国内 API

### 5.4 决策
- PASS ≥1 → V3X 后续阶段保留 GPT-6
- 全 GRAY → 视具体任务族选择
- 全 FAIL → V3X 后续阶段全切 MiniMax-M3,撤掉 OpenRouter billing

---

## §6 锚占位(SHA-256 前 12 位,实现时算)

| 锚名 | 锚内容 | SHA-12 (占位) |
|---|---|---|
| ANCHOR_PROMPT_T1 | T1 GSM8K 30 cell 选样 prompt | `TBD_00000001` |
| ANCHOR_PROMPT_T2 | T2 StrategyQA 30 cell 选样 prompt | `TBD_00000002` |
| ANCHOR_PROMPT_T3 | T3 22 受控图选样 prompt | `TBD_00000003` |
| ANCHOR_PROMPT_T4 | T4 50 受控图选样 prompt | `TBD_00000004` |
| ANCHOR_BILLING_OK | OpenRouter 验证充值到账截图 | `TBD_00000005` |

> 5 锚冻结规则同 KT_ABC1_anchors_sha256_12.json。实现时写入 `docs/V3X/GPT6_VS_M3_ANCHORS_<date>.json`。

---

## §7 数据源(沿用既有冻结)

| 数据 | 路径 | SHA-12 | 状态 |
|---|---|---|---|
| v19 frozen | `results/deposon_v19_benchmark_fixes.json` | `910c4333eead` | 冻结 |
| v20 baselines | `results/deposon_v20_baselines.json` | (锚有) | 冻结 |
| v21 gtformal | `results/deposon_v21_gtformal.json` | (锚有) | 冻结 |
| 5 锚 JSON | `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | `03c6c01f3697` | 冻结,不动 |
| 4 SPEC V0.1 | `docs/V3X/KT_?1_SPEC_V0.1.md` | 各自 | 冻结,不动 |

---

## §8 节省原则(7 条)

1. **30 cells 不上 300 cells**(边际验证 ≠ 全面评估)
2. **1 模型 1 query 1 answer,不重试**(无 variance 估计)
3. **不调优 prompt**(沿用 4 SPEC V0.1 模板)
4. **不测多语言**(只测中英 V3X 任务族)
5. **不测 human eval**(纯自动 accuracy)
6. **不微调**(无 Mavis 训练 pipeline)
7. **不缓存**(每次现调,避免 API 行为漂移)

---

## §9 时序

### 9.1 触发条件
- [ ] coding-plan 2h API 配额恢复(预计 2026-09-10 16:30 GMT+8)
- [ ] OpenRouter 验证 1 USD 充值到账(用户操作)
- [ ] 5 锚 JSON 实现后写入并冻结

### 9.2 步骤
1. 实现 5 锚 JSON(独立 worker,15 min)
2. 选 30 cells(沿用 v19 顺序,5 min)
3. 写 prompt 模板(沿用 4 SPEC V0.1,10 min)
4. 调 GPT-6 + MiniMax-M3 API(30 min,2 模型并行)
5. 评分(15 min)
6. 写对照报告 `docs/V3X/GPT6_VS_M3_REPORT_<date>.md`(30 min)

### 9.3 总耗时
- 估计 1.5-2h(单 worker 串行)

---

## §10 7 铁律兼容(7 项全展开)

### 10.1 不读 API key
- [x] key 永远 runtime 读(本 spec 全文不出现 key 字符串)
- [x] 即使 base URL 也不写死(沿用 env var `OPENROUTER_BASE_URL`)

### 10.2 不调 GPT-6(本 spec 阶段)
- [x] 本 spec 仅文档,无任何 API 调用代码
- [x] 实现冻结于"API 恢复 + billing 验证"两个条件全满足后

### 10.3 不动 5 锚 JSON
- [x] 本 spec §6 占位,实现时新建独立 JSON 文件
- [x] 旧 `KT_ABC1_anchors_sha256_12.json` 维持 `03c6c01f3697` 不变

### 10.4 不动 4 SPEC V0.1 冻结版
- [x] 沿用 `KT_A1/B1/C1/D0_SPEC_V0.1.md` 的 prompt 模板(只读)
- [x] 4 文件 SHA-12 维持原值(锚 JSON 记录)

### 10.5 不动 v19 frozen JSON
- [x] v19 frozen 仅作 30 cell 选样源(只读)
- [x] 不修改 `deposon_v19_benchmark_fixes.json`

### 10.6 改前必报 SHA-12
- [x] 5 锚 JSON 写入前报占位,写入后报实际
- [x] 新报告 `GPT6_VS_M3_REPORT_<date>.md` SHA-12 写入锚 JSON

### 10.7 不写入任何 LLM API key
- [x] 报告、spec、log、JSON 全无 key 字符串
- [x] 余额用 `OPENROUTER_CREDIT_REMAINING` env var 读

---

## §11 已知未决项(10 项)

1. **MiniMax-M3 单价**:Mavis 官方 minimax.chat 公开报价未在 spec 中确认(占位)
2. **OpenRouter billing 灰区**:US 虚拟地址实际通过率未知(等用户实测)
3. **30 cells 是否足够**:5pp 差异的统计功效待 power analysis 复核
4. **GPT-6 实际行为**:2026-09-03 上线,稳定性未知,可能 API 漂移
5. **MiniMax-M3 上下文窗口**:与 GPT-6(128K)是否可比未确认
6. **脱敏协议**:4 SPEC V0.1 模板对 GPT-6 是否充分待审
7. **数据出境合规**:内部法务是否需要走流程未确认
8. **3 任务族温度**:T3/T4 概念图任务是否需要 temperature=0 复核
9. **失败模式**:任一 cell API 失败时,是否需要重试(节省原则说不重试,但需确认)
10. **报告归档**:对照报告与 KT-?1 报告是否合并(暂定独立 `GPT6_VS_M3_REPORT_<date>.md`)

---

## §12 升级触发

下次升级(V0.1)需要:
- 5 锚 JSON 实现并冻结
- 30 cells 实测数据
- 4 任务族 accuracy/latency/cost 表
- 5 判死(1 PASS / 1 GRAY / 3 FAIL 各分支示例)
- 5.1 PASS / 5.2 GRAY / 5.3 FAIL 三档决策

升级流程:沿用 4 SPEC V0 → V0.1 的 git 提交 + 锚更新 + 报告生成。

---

*SPEC 生成: 2026-09-10 Mavis worker*  
*仅 spec,无 API 调用;实现冻结于 §9 触发条件全满足*  
*下次升级:V0 → V0.1 需 5 锚冻结 + 实测数据*
