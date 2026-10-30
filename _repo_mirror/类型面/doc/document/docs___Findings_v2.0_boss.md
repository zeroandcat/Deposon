# Findings v2.0-BOSS — 基线注册表与 BOSS 扫描 × CoT 收编 × 向量属性审计

> 2026-08-28。用户双指令：① 横向对比算法充分查找，不留 v1.X 式后期大 BOSS；
> ② Deposon 向量属性（单纯形非负，负值无意义）。
> 数据：results/deposon_v20_baselines.json、deposon_v20_cot_quiz.json、
> deposon_v20_vector_audit.json。注册表：docs/BASELINE_REGISTRY.md。

## 一、基线注册表（防 BOSS 机制化）

按族穷举：A 结构启发式 10 臂（+common_neighbors/preferential_attachment/PPR/Katz/
node2vec_shallow）、B 语义非 LLM（规则过滤 + ngram_tfidf_cosine 代理）、
C LLM 直接类（labels-only 先验 + **直接 CoT**）、D 本方法族、E 人类平凡基线。
⬜ 待补：KGE（v2.1）、Self-Consistency（v2.1）、真实 embedding 余弦（待端点）。
每族至少一臂在场，新增实验先查表。

## 二、BOSS 扫描结果：alert 触发，两个 BOSS 提前现形 ✅（这正是注册表的目的）

| BOSS | 击败 field_mean 的图 | 最大 margin |
|---|---|---|
| **ngram_tfidf_cosine**（零 API 字符 3-gram 余弦） | S4、S5、L_bio、L_hist、L_phys（5 图） | +0.143（S5） |
| **common_neighbors** | L_historical_causality | +0.130 |

逐图第一名：**field_mean 15/20**、tfidf 4/20、common_neighbors 1/20。
**头条披露（收编纪律 #2）**：BOSS 全部出现在**低枢纽或语义真实图**——
与领域鉴定器 v0 完全一致（hub_concentration 低 → 场弱；real_semantics=1 → 语义臂强）。
场的基本盘（S6 族 0.471、高枢纽图）无人能撼；场不是通用方法，是枢纽结构 specialist，
这一边界由 BOSS 扫描坐实而非掩埋。

附注（诚实）：tfidf 在 S4/S5（标签与结构脱钩的合成图）上获胜出乎意料——
内置本体标签共享中文字后缀（纲/门/科），字符 n-gram 捕获的是本体层级后缀聚类，
其信号性质接近「标签词法模式」而非结构；margin ≤0.143 且 n=20，解读从慎。

## 三、直接 CoT 大 BOSS 正面收编（C 族）

题库 40 题直接问答（8 prompt / 9 次 HTTP，每域 2 prompt 打包）：

| 臂 | 准确率 | 信息通道 |
|---|---|---|
| **直接 CoT** | **92.5%** | 看见题干+选项（易） |
| **labels-only 先验** | **92.5%** | 只看见标签列表（难） |
| field_mean | 52.5% | 结构 |
| rule_filter | 27.5% | 关键词表 |

CoT 与先验同分——**先验在更难的信息通道上达到了直接问答的水平**，
v1.4「CoT 是天花板」的担忧在脑图任务上转化为「先验=CoT 水平」的正面证据
（同源污染警告继续有效，GT-3 跨模型复现为必做）。

## 四、向量属性审计（指令②）

run_v20_vector_audit.py：全 20 图 × 全部留一任务 × 双起点（mean-field/dirichlet），
共 **1740 个任务**：
- V1 非负性：W_done[mask] ≥ −1e-9 —— **0 违规**
- V2 单纯形性：含 mask 行行和 ≤ 1+1e-6 —— **0 违规**
- V3 NaN/+inf —— **0 违规**（-inf 仅为掩码占位，在排序域外）
- V4 排序域候选分非负无 NaN —— **0 违规**

结论：场分值域为 [0,1] 单纯形权重，全链路（打分/排序/融合 min-max）无负值泄漏；
-inf 是掩码约定不是分数，已在所有结果 JSON honesty 声明。

## 五、对 v2.1 的输入

1. 基线注册表转为活文档：新版本启动先过表；KGE 与 Self-Consistency 排期。
2. tfidf_cosine 收编为常驻臂（零 API、BOSS 级），入 run_v20_corpus_eval 主评估。
3. GT-3 跨模型先验：先验=CoT 同分使跨模型复现的优先级再升一档。
