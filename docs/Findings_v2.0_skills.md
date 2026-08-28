# Findings v2.0-Skills — 新技能三联验证（统计复核 × 领域鉴定器 × 题库）

> 2026-08-28。零 API（全部本地/缓存）。技能：auto-stat-test、regression-insight、
> bloom-quiz-maker（题型规范）。数据：results/v20_graph_features.csv、
> v20_statcheck_*.json、v20_regression_field*.json、quizbank_v20.json、
> deposon_v20_quiz_eval.json。

## 一、统计复核（auto-stat-test 第二意见）

| 比较 | 我们的符号检验 | auto-stat-test 复核 | 结论 |
|---|---|---|---|
| field_mean vs random（20 图配对） | p=0.0075 | Wilcoxon 符号秩 **p=0.0031，\|r\|=0.83（大效应）** | 一致显著，方法学稳健 |
| field_mean vs degree（20 图配对） | p=7.6e-6 | 配对 t **p<0.0001，Cohen's d=2.05（大效应）** | 一致显著 |

检验选择合理性：Shapiro-Wilk 显示差值非正态（p=0.012）→ Wilcoxon 为正确选择，
与我们预登记的符号检验同族（非参数），结论互相印证。

## 二、领域鉴定器 v0（regression-insight）

field_named ~ density + hub_concentration + real_semantics（OLS，n=20）：

| 特征 | β | p | 解读 |
|---|---|---|---|
| **hub_concentration** | **+2.12** | **0.00028** | 枢纽集中度是场效力的主导预测子——「场=汇聚结构检测器」的机理级证据 |
| **real_semantics** | **−0.16** | **0.012** | 真实语义图显著压低场表现（先验的主场） |
| density | −3.32 | 0.132 | 不显著 |

模型 R²=0.63（调整 0.56），F p=0.001。**领域鉴定器规则 v0**：
hub_concentration 高 → 用场；real_semantics=1 → 用先验。两特征 VIF<4，
与 CrossVal 的「分工叙事」互为定量/定性互证。（n=20 小样本，标记为探索性 v0，
v2.1 扩图后重估。）

## 三、题库横向验证（bloom-quiz-maker 题型 × GT-2 攻击者干扰项）

题库 quizbank_v20.json：40 题（4 域 × 10），L4 分析级单选——
「与源概念存在最直接合理后继关系的是？」，干扰项 = 自适应攻击者陷阱 ×2 + 图内随机节点 ×1。

| 臂 | 总准确率 | bio | hist | algo | phys |
|---|---|---|---|---|---|
| **llm_prior** | **92.5%** | 100% | 100% | 80% | 90% |
| field_mean | 52.5% | 70% | 50% | 40% | 50% |
| rule_filter | 27.5% | 10% | 30% | 40% | 30% |
| random（机会） | 25% | 10% | 40% | 20% | 30% |

- 先验在题库格式下同样碾压（92.5%），与 LOO 协议结论一致 → 题库效度成立。
- **rule_filter ≈ 机会水平（27.5% vs 25%）**：GT-2 自适应陷阱在题库格式下复现渗漏——
  规则防御对自适应攻击者基本无效，与 GT-2 的 −7.5pp 方向一致且更直观。
- field_mean 52.5%（2× 机会）：结构信号在语义任务上有部分迁移，但非主场。
- 机制披露：陷阱标签不在图节点集内，field/prior 对其打 −inf——不被骗是排序
  对象域的机制结果；rule_filter 的渗漏才是标签攻击的真实战场。

## 四、对 v2.1 的输入

1. 领域鉴定器 v0 投入试用：新图先入先算 hub_concentration 与 real_semantics，
   按 v0 规则选信号源，并记录鉴定准确率（预登记 v2.1 SPEC）。
2. 题库轨转正：quizbank 模式（bloom 题型 + 自适应干扰项）作为 v2.1 横向对比的
   标准组件；GT-2 升级（多陷阱注入）以 rule_filter 的题库表现为直接度量。
3. GT-3 跨模型先验仍为 H-C 洗白的唯一路径（技能侧无替代）。
