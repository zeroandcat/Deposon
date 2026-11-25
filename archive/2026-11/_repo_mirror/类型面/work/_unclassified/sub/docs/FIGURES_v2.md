# FIGURES_v2 — v2X 论文附录 D 五图中文版制作记录

> 2026-08-30。制作脚本：`tools/make_figures_v2.py`（可复跑，出图前 56 项
> 数据点计数自检，任一不过即 assert 中止）。输出：`figures/fig1..fig5 *.png`
> （300 dpi）。全部数据机械读取自 `results/` 下冻结 JSON/CSV，未手写任何数字。
> 中文渲染依赖运行环境预配置的中文字体（脚本不改 rcParams 的
> font.family / axes.unicode_minus / font.sans-serif；本工作区 ipython
> 内核已配置，裸 shell python3 未配置，复跑请用已配字体环境）。
> 配色：灰青 #5F8D86（场/族 S）、灰赭 #C08552（先验/族 L）、中灰/灰蓝
> （基线参考）、灰红 #A26769（Φ 轴）、cividis 连续色标（图 3）；
> 白底浅灰网格，无高饱和背景与蓝紫渐变。

## 图 1：分工边界总览——22 图场-先验胜负地图（fig1_boundary_map_cn.png）

- 数据源：
  - `results/deposon_v20_corpus_eval.json` → `graph_level.named_hits3.{gid}.{arm}`
    （arm ∈ field_mean / random / degree，named Hits@3，22 图）；
    `per_graph[].family`（族 L/S 归属与排序）。
  - `results/deposon_v20_crossval.json` → `prior_arm_eval.{gid}.llm_prior.named`
    （先验臂 named Hits@3，族 L 四图，0.4839–1.0；预登记口径先验臂仅族 L 主报，
    族 S 不可得，与论文 §3.2/§4.2 一致）。
- 图元：22 图 × 场条形 + 4 图先验条形 + random/degree 参考散点 + 逐图第一名 ★。
- 计数自检：22 图（=语料 22 图口径）；先验臂 4 图且全部属于族 L。

## 图 2：H-A1 斩杀线与反转图分布（fig2_killsign_scatter_cn.png）

- 数据源：
  - `results/deposon_v20_corpus_eval.json` → `graph_level.named_hits3.{gid}.field_mean / .random`
    （x=random，y=field_mean，22 点）；
  - `verdicts.H_A1_field_mean_gt_random.sign_test`（n_pos=16 / n_neg=4 / n_tie=2 /
    p_exact=0.0118，图中标注直接读字段）；
  - `verdicts.kill_lines.H_A_dead`（triggered=true；reversals_vs_random 四图：
    L_historical_causality、L_physics_concepts、L_project_management、S2_n45，
    红框标注）。
- 计数自检：22 点；由数据现算的 n+/n−/平 与 sign_test 字段逐一相等；反转图
  集合与 n− 图集合相等（4 张）；斩杀线 triggered=true 在案。口径对照论文 §4.1。

## 图 3：分工规律散点（fig3_division_scatter_cn.png）

- 数据源：`results/v20_graph_features.csv`（20 行：hub_concentration、
  real_semantics、field_named、family）；回归注释读
  `results/v20_regression_field_v2.json` → `coefficients.hub_concentration`
  （β=2.1177，p=2.79e-4）、`coefficients.real_semantics`（β=−0.1618，
  p=0.0122）、`r_squared=0.628226`、`n_observations=20`。
- 图元：x=hub_concentration，y=real_semantics（0/1，y 向加修饰性抖动，
  seed 固定，非数据），着色=field_named（cividis），形状区分族 S/L。
- 计数自检：CSV 20 行 = 回归 n_observations=20（论文 §4.4 口径 n=20；
  族 L 扩展图 L_geography_world / L_project_management 不在该回归样本内，
  与冻结回归一致，不外推）。

## 图 4：GT-7 温度前沿逐图形态（fig4_gt7_frontier_cn.png）

- 数据源：`results/deposon_v20_gt7.json` →
  `per_graph.{S6,L_physics_concepts,L_biological_taxonomy,L_algorithm_process}.temperatures.{α}`
  （hits_mean/hits_std/phi_mean/phi_std/n_seeds）与 `.meanfield`（T=0 端点
  虚线）；`temperature_knob.alphas`=[0.3,0.5,1.0,2.0,5.0,20.0]；
  `verdict.per_graph_direction`（前沿温度档标注）；verdict="mixed"。
- 图元：2×2 面板，x=α（log），左轴命中率（灰青，5 seed 均值±std），
  右轴终点 Φ（灰红，均值±std），mean-field 双虚线。
- 计数自检：4 图（=preregistered.graphs）× 6 温度档（=alphas）× 5 seed
  （=seeds_per_temperature，逐档 n_seeds=5 核验）。口径对照论文 §5.5。

## 图 5：分布级 PoA 全 22 图条形（fig5_poa_distribution_cn.png）

- 数据源（追溯路径同论文附录 A）：
  - `results/deposon_v20_gt.json` → `GT4_price_of_anarchy.poa_per_graph`
    （冻结 20 图：17 有限值 + 3 张 "Infinity"）与
    `GT4_price_of_anarchy.verdict`（poa_per_graph_finite 17 项、
    median_poa=1.3333、n_poa_inf=3、pass_threshold=1.2）。
  - `results/deposon_v20_corpus_eval.json` → `graph_level.named_hits3`
    （22 图；GT-4 的官方输入，见 run_v20_gt.py §GT-4）。
- 口径说明（重要）：冻结 GT-4 判定时语料为 20 图；L_geography_world 与
  L_project_management 两图在冻结时未入 GT-4。本图按附录 D「全 22 图」要求，
  用 GT-4 预登记公式 PoA = field_mean / max(random, degree)（run_v20_gt.py
  逐字口径；自利臂 named=0 而 field>0 记 ∞）对 22 图从 corpus_eval 机械复算：
  冻结 20 图逐值吻合（20 项一致性断言全过），补算的 2 图
  （L_geography_world=3.0、L_project_management=0.2）以点纹区分并在图例
  声明「不计入中位数」。中位数、通过线、∞ 计数一律读冻结 verdict 字段。
- 图元：19 根有限值条（降序）+ 3 根 ∞ 条（灰斜纹，单独计数）；PoA<1 红框
  （冻结集中族 L 两图 L_historical_causality=0.5、L_physics_concepts=0.75，
  另有族 S 的 S2_n45=0.5 同标红框，如实呈现）；通过线 1.2 与中位 1.333 横线。
- 计数自检：17 有限 + 3 ∞（=论文 §5.4 口径）+ 2 补充 = 22 条形；
  median(17 有限值)=1.3333 与冻结字段相等。

## 自检台账

脚本每次运行打印 56 项 `[PASS]` 自检（图数、符号检验计数、反转图集合、
回归 n、温度档×seed 数、PoA 冻结/复算逐值一致等），全部通过方出图；
台账随 stdout 留存，复跑即复算。
