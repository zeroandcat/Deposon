# Findings GT-8：「领域鉴定器 v0」hub_concentration 轴语料外预登记复现

- 预登记：docs/SPEC_GT8.md（先于任何 GT-8 数据提交，git 时间戳为证）。
- 结果文件：results/deposon_v20_gt8.json；实验脚本 run_v20_gt8.py；
  测试 tests/test_v20_gt8.py。
- 零 LLM API；全程本地种子化 numpy 运行（runtime ≈ 4.8s）。

## 1. 结果

**verdict = supports_H_GT8（2/2 对同向）**——预登记成功标准达成。

| 对 | 图 | 拓扑 | N | n_edges | named | hub_concentration | field_named | random_named | degree_named | diff（fm−rand） |
|---|---|---|---|---|---|---|---|---|---|---|
| A | GT8_A_high | 星-链双汇聚 | 31 | 30 | 24 | **0.5000** | 1.0000 | 0.2083 | 1.0000 | **+0.7917** |
| A | GT8_A_low  | 毛虫链 | 31 | 30 | 15 | 0.0667 | 0.1333 | 0.0000 | 0.0000 | +0.1333 |
| B | GT8_B_high | 带超枢纽的平衡树 | 40 | 39 | 19 | **0.4872** | 0.0526 | 0.0000 | 1.0000 | **+0.0526** |
| B | GT8_B_low  | 平衡三叉树 | 40 | 39 | 12 | 0.0256 | 0.1667 | 0.2500 | 0.0000 | −0.0833 |

- 对 A：diff 0.7917（高 hub） > 0.1333（低 hub）⇒ 同向。
- 对 B：diff 0.0526（高 hub） > −0.0833（低 hub）⇒ 同向。
- 每对 N 与 n_edges 完全对配（31/30 与 40/39），real_semantics=0（族 S
  合成标签）。新图与全部 22 张语料图不变量 (N, E, 入度/出度多重集)
  全异（不同构哨兵，tests/test_v20_gt8.py 锁定）。

## 2. 与 v0 规则的一致性

hub_concentration 轴方向复现成功：语料外 2 对新图上，高 hub 图的场优势
（field_named − random_named）一致大于配对的低 hub 图，与 OLS
β=+2.12（p=0.00028）的预测方向一致。real_semantics 轴本轮 deferred
（需 LLM 先验 API 预算，零 API 实验不测）。

## 3. 观察与次要发现（如实双报）

- **degree 基线在高 hub 图上极强**：A_high 与 B_high 的 degree_named 均
  = 1.0000（超枢纽星边的终点入度最大，degree 直接命中），diff_fm_deg
  分别为 0.0 与 −0.9474。即「场 > random」的 hub 轴方向成立，但
  「场 > degree」在高 hub 新图上不成立——hub 集中度同时放大了 degree
  平凡基线。这与语料内 S6（degree_named 0.3529 > 0）现象同向，非新
  现象，但提示 v0 的 hub 轴鉴别的是「结构信号整体可利用性」而非场独有
  优势。
- B_low（平衡三叉树）field 0.1667 < random 0.2500（diff 为负）：低 hub
  纯树结构上场无优势且被随机臂反超，单图小样本（named=12）波动大，
  如实披露。
- A_high 场满分（1.0000）与 degree 满分并列：双汇聚拓扑中场与度基线
  不可分（ceiling），该对的鉴别力主要来自 random 臂。

## 4. 局限性

1. 样本仅 2 对（评审要求的下限设计）：方向性证据，不能估计效应量，
   也不做显著性检验（n=2 无统计功效；成功标准为预登记的机械方向规则）。
2. real_semantics 轴 deferred：本轮零 API，LLM 先验轴未复现。
3. 仅族 S 合成标签（real_semantics=0）：结论不外推至族 L 真实语义图。
4. named/filler 口径虽冻结于 SPEC，但新拓扑的 named 定义（汇聚边 /
   主干链 / 超枢纽星边 / S2 式内部边）各自不同，跨对比较 diff 绝对值
   无意义，仅有对内方向有意义。
5. 高 hub 图上 degree 基线饱和（§3），hub 轴的场-vs-random 复现不能
   解读为场-vs-degree 的复现。

## 5. 复现性

- 种子冻结：GT8_SEEDS = 208801–208804；每边 rng = default_rng(
  g_seed·100003+ei)；场实例种子 g_seed+ei（与 run_v20_corpus_eval
  逐行同式）。
- 特征锚点复核：hub_concentration 对语料 S1/S2/S3 重算 = CSV 值
  0.0526 / 0.0333 / 0.0625（tests/test_v20_gt8.py 锁定）。
- 全套 pytest：237 passed（基线 228 + 新增 9 项 GT-8 测试），无回归。
