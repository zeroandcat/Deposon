# SPEC GT-8：「领域鉴定器 v0」hub_concentration 轴的语料外预登记复现

> 本文档先于 GT-8 任何实验数据写盘并提交（远端 commit 时序即为预登记证据）。
> 零 LLM API 实验：全程本地种子化 numpy 运行，不发起任何 API 调用。

## 1. 背景与假设

既有 OLS（n=20 图，results/v20_regression_field_v2.json）给出两特征
「领域鉴定器 v0」：

- **hub_concentration** β = +2.12，p = 0.00028：hub 集中度越高 → 结构场
  （field）越强；
- real_semantics = 1（族 L 真实语义标签）→ LLM 先验强。

**H_GT8**：在语料外新图上，hub_concentration 轴的预测方向成立——
高 hub 新图的 `field_named − random_named`（named Hits@3 之差，下称 diff）
**显著大于**配对的低 hub 新图的 diff。

## 2. 特征操作化定义（锁定，逐字沿用）

- `hub_concentration = max_in_degree / n_edges`
  （有向图最大入度除以边数）。验证锚点：results/v20_graph_features.csv 中
  S1 = 1/19 = 0.0526、S2 = 1/30 = 0.0333、S3 = 2/32 = 0.0625。
- `real_semantics` = 1（族 L 真实语义标签）/ 0（族 S 合成标签）。
  本实验全部新图均为族 S 合成标签（种子驱动本体池随机指派，语义与结构
  脱钩），real_semantics = 0。

## 3. 设计

≥ 2 对新图；每对一张高 hub 拓扑 + 一张低 hub 拓扑，N 与 n_edges 尽量对配，
均为族 S 合成标签、real_semantics = 0。新拓扑不得与语料 S1–S6（及全部
语料族 S 图）同构——以 (N, n_edges, 入度多重集, 出度多重集) 不变量作
不同构哨兵（tests/test_v20_gt8.py 锁定）。

冻结拓扑（常量冻结于 run_v20_gt8.py，先于数据）：

| 图 | 拓扑 | N | n_edges | 预计算 hub_concentration |
|---|---|---|---|---|
| GT8_A_high | 星-链双汇聚（root→双枢纽；13+7 条星边 + 2 条链汇聚入枢纽） | 31 | 30 | 15/30 = 0.5000 |
| GT8_A_low  | 毛虫链（16 节点主干链 + 15 叶指回主干，最大入度 2） | 31 | 30 | 2/30 = 0.0667 |
| GT8_B_high | 带超枢纽的平衡树（21 节点二叉树 + 19 条超枢纽星边） | 40 | 39 | 19/39 = 0.4872 |
| GT8_B_low  | 平衡三叉树（parent=(i−1)//3，最大入度 1） | 40 | 39 | 1/39 = 0.0256 |

- 对 A：N=31/31、n_edges=30/30 完全对配；hub 0.5000 vs 0.0667。
- 对 B：N=40/40、n_edges=39/39 完全对配；hub 0.4872 vs 0.0256。

named/filler 操作化（冻结）：
- GT8_A_high：named = 全部以双枢纽（节点 1/2）为终点的汇聚边（24 条），
  filler = 其余结构边（外悬叶）；
- GT8_A_low：named = 主干链 15 边，filler = 叶指回边 15 条；
- GT8_B_high：named = 超枢纽星边 19 条，filler = 二叉树边 20 条；
- GT8_B_low：named = 子节点仍为内部节点的父子边（沿用 S2 口径，12 条），
  filler = 叶边。

## 4. 协议

与 run_v20 系列完全相同：全边留一、全候选协议（raw 口径，
full_candidate_mask），臂 = field_mean（prior_mean 起点）/ random /
degree；每边 rng = default_rng(g_seed·100003+ei)，场实例种子 =
g_seed+ei；指标 = named Hits@3（gold_rank < 3）。diff = field_named −
random_named；degree 臂差值（diff_fm_deg）如实双报作次要参照。
新图种子 208801–208804（区别于语料 200101–200106 族）。

## 5. 成功标准（预登记，机械求值）

- **支持**：≥2/2 对同向（每对高 hub 图 diff > 配对低 hub 图 diff）
  ⇒ verdict = `supports_H_GT8`；
- **判死线**：2/2 对全反（每对高 hub 图 diff < 低 hub 图 diff）
  ⇒ verdict = `H_GT8_dead`，如实宣布；
- **其余**（1/2 或出现持平对）：`inconclusive`，预登记未定义区间，如实报。

## 6. 如实声明

- **real_semantics 轴 deferred**：该轴需 LLM 先验 API 预算，本轮为零 API
  实验，不测，留待后续有预算轮次。
- 样本仅 2 对（评审要求 ≥2 张新图的下限设计），方向性证据，非效应量估计。
- 仅族 S 合成标签；结论不外推至族 L。
- 零 LLM API；语料只读加载；既有 run_v20 系列文件一行不动（协议函数经
  只读 import 复用）。
