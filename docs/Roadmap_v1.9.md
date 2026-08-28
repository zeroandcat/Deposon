# Roadmap v1.9 — 脑图补全算法与实验路线（评审驱动整改版）

综合来源：R1 设计探针（reviews/design_probe_v19.md）、R2 文献扫描（reviews/literature_scan_v19.md）、R3 功效分析（reviews/experiment_design_v19.md）、评审 A（reviews/peer_review_v19_A.md，11 Major）、评审 B（reviews/peer_review_v19_B.md，写作/原创性侧重）。本文档与论文 §5 对齐，作为 v1.9 → v2.0 的执行蓝图。

## 0. 核心诊断（一句话）

「纯物理场 named 输 random」在 v1.7.1 协议下是**采样器假象**：反向去噪的 Dirichlet(1) 随机起点在 50 步 ×0.9 收缩后几乎不被场梯度重排（信噪比 ≈0.1）；把起点换为先验均值（mean-field，等价 DDIM η=0 确定性反向），同一场、同一能量函数 named 达 0.994（R1 探针实跑）。统计显著性的真正瓶颈是**语义图 n=1**，不是算法。

## 1. 算法设计路线（期望收益/成本排序）

| # | 变更 | 机制 | 状态 |
|---|------|------|------|
| A1 | 反向过程均值化（init_mode: dirichlet → prior_mean）+ η 消融 | named 0.176 → ~0.99（探针值，须预登记重跑） | **✅ 完成：named 1.000，H1+H2 触发** |
| A2 | 全候选排序协议（MRR/Hits@1/3，取消同行负采样） | 采样器敏感性归零，秩信息保留 | **✅ 完成：MRR/Hits@k 落盘，协议符号翻转证实** |
| A3 | λ∈[0,1] 凸约束 + 方向对称化先验 P′=max(P,Pᵀ) | 消除 λ>1 反场 artifact（v1.7.1 的 0.471 部分源于此）；无向骨架 6/9 vs 有向 2/9，先验有效信号 ×3 | 待 v1.9 实验后排期 |
| A4 | 多图基准 ≥20 张（ConceptNet/Wikidata 采样 + 真实脑图双人转译 + 生成图三轨） | 唯一能产出统计显著的路径；图级符号检验 G≥8 功效 0.80–0.87 | P1（1–2 周） |
| A5 | 平凡基线组：KGE（TransE/ComplEx/RotatE，多图后可训练）、label 嵌入余弦、Adamic-Adar/Jaccard、LLM 逐行重排、规则过滤 | 审稿通行证；「超随机」≠「超平凡语义基线」 | E9.5 ✅ 完成（规则基线 0.87≥0.85）；其余 P2 |
| A6 | 逐候选条件化能量（有效电阻 / Personalized-PageRank 式） | 给 filler 行场信号，修复 filler=0.088 塌陷 | P2（算法改动较大） |
| A7 | 图级嵌套验证的学习式门控/stacking | named/filler 分工封顶；依赖 A4 完成 | P3 |
| A8 | tie-break 改 (u,v) 内容哈希微扰 | 消除列号稳定排序 artifact（已在 v1.7.1 与探针各咬一次） | 随 E9.1 一并处理 |

## 2. 基准侧整改（评审 A 实锤 → SPEC v1.9 Part B）

| # | 问题 | 处置 | 状态 |
|---|------|------|------|
| B1 | high_couple 别名 bug 未修复（deposon_agents_v1_4.py:1515），Table C1 v1.4 行声称已修复，Table 10/12 数字错误 | E9.3：真修复 + 缓存离线重跑 GSM8K/StrategyQA 物理层 → 更正表 | **✅ 完成（见 §6）** |
| B2 | 对抗性诱饵构造（正确边 0.6/0.7/0.8 vs 陷阱边 0.9/0.85/0.8 + 强制 Trap_DeadEnd）用于真实基准且未按 §4.1 口径降级 | E9.4：等权诱饵中性对照（拉平后 deposing 应退化为 no_deposon） | **✅ 完成（见 §6）** |
| B3 | 缺规则式平凡基线 | E9.5：纯规则标签过滤基线（零 LLM） | **✅ 完成（见 §6）** |

## 3. 实验路线分档（R3 功效口径）

| 档位 | 语义图数/来源 | named 边 | 可支撑结论 | 判据 |
|---|---|---|---|---|
| 最小 | 8 张 / ≥2 来源 | ≈136 | named>field（α=0.05） | 图级符号 p<0.05 且边级 McNemar p<0.05 |
| 标准 | 12 张 / ≥3 来源 | ≈204 | named>field 稳健；overall 非劣效（界值 0.03） | 聚类 bootstrap CI 下界>0；TOST CI 下界>−0.03 |
| 充分 | 30 张 / ≥5 来源 | ≈510 | named>random（若真实 π≥0.60）；留源泛化 | 预注册全口径 + Holm 校正 |

关键功效事实（R3）：vs field 的 McNemar 观测功效仅 15.4%，需 ≈42 不一致对 ≈4 张图；vs random 观测功效 2.3%，当前效应量下 ≈58 张图——「named 显著超 random」不现实，改主张「named 超 field + overall 非劣效」。图级符号检验 G<6 最小可达 p=0.0625，**G≥6 才存在显著可能**。

## 4. 统计与预登记口径（冻结项）

1. 主终点：多图 named Hits@3（全候选协议）；主比较 field_mf vs field_dirichlet / random，α=0.05，Holm 校正。
2. 图级 cluster bootstrap（整图重采样，B≥10000）为主口径；边级 McNemar 仅作图内辅助并声明行聚类（17 边分布 9 行）。
3. overall 只主张非劣效（TOST，界值 0.03）——20 图符号检验已证 random≥hybrid 反向稳健（p=0.0013）。
4. 分析代码先于新图数据入库并记录哈希；阴性结果归档 `_negativeresult.json`。
5. 单图阶段一切结论降级表述为「单图个案证据」。

## 5. 论文披露修复（信誉项，零成本）

- §4.7/附录 D 写明实验 B 图为**确定性重建**（源 JSON 无逐边列表）、45 节点中 35 个占位标签、named 17 边中 3 边指向占位节点原理上不可语义预测。
- tie artifact 史（v1.7.1 与探针各一次）如实入附录。
- Table C1 v1.4 行「high_couple 别名 bug 修复」更正（依 E9.3 结果）。
- λ>1 反场 artifact 对 0.471 数字的贡献如实披露，重报 λ∈[0,1] 结果。

## 6. v1.9 实验结果汇总（已运行，SPEC v1.9 预登记口径，零 API，pytest 160/160）

**E9.1 均值场反向退火 → H1 成立 + H2 触发**
- field_mean named = **17/17 = 1.000**（真实标签 14/14 = 1.000；占位 3/3 依赖 tie 稳定序，已逐边标注）；对 field_guided（0.176，逐位复现 v1.7.1）McNemar b=14/c=0，**p=1.22e-4**。
- filler = 0.0625 < 0.15 → 「场=骨架检测器」成立；overall = 0.388。
- 融合故事反转：hybrid_norm@0.5 named=0.824（先验稀释场）；hybrid_norm@2 named=0.118，11 条 filler 命中全部来自 λ>1 反场 artifact——v1.7.1 的 0.471 部分由此 artifact 构成。

**E9.2 全候选排序（N=44，raw 口径）**
- field_mean：MRR 0.191 overall；Hits@3 named 0.471 / filler 0.000；hybrid_norm@0.5 MRR 0.214 最高。
- 协议结论变化显著：named Hits@3 从 N_NEG=10 的 1.000 跌至 0.471（小负池放大场优势）；三臂上优劣符号翻转（落盘 sign_flips）——证实旧协议的采样器敏感性。

**E9.3 high_couple 真修复 → Table 10 数字更正**
- GSM8K high_couple **0.86 → 0.82**（4 题翻转，McNemar p=0.125）——v1.4 Table 10 的 0.86 是别名 bug 产物，错误。
- StrategyQA 预测向量与 v1_blocking 完全相同（0.8990）：g_couple×5 物理扰动真实发生但 3 步浅图不改变贪心排序；Table 12 数字碰巧成立。守恒审计 2.2e-16 通过。

**E9.4 等权诱饵中性对照 → 假设被证伪（最高优先级发现）**
- 拉平所有边权 0.7 后：GSM8K unified **0.85** vs no_deposon **0.04**（p≈1e-24）；StrategyQA **0.899** vs **0.202**。优势完全不消失。
- 归因：偏差不在边权先验——(a) BFS 短路径优先使 2 跳陷阱路径永远先被发现；(b) 物理层免费获得 `type='trap'` 节点标签（g_couple=5 硬编码反射）。**v1.4 全部 Table 10/12 效应量（0.83/0.78）结构性存疑**，论文相关主张须彻底重写。

**E9.5 规则基线 → LLM 先验零增量**
- 6 关键词规则过滤器（trap/dead/end/impossible/guess/wrong，仅读标签字符串）：GSM8K **0.87 ≥ unified 0.85**；StrategyQA **0.899 = unified 0.899**（McNemar 均不显著）。
- 「物理层+LLM 先验贡献」叙事需重写为与平凡基线对比的诚实定位。

**E9.6 速赢固化**
- 图级符号检验精确复现 R3：random≥hybrid p=0.001312；hybrid>field p=0.007538 → overall 只主张非劣效。
- field_mean 种子扫描：named = **1.000 ± 0.000**（5 种子族），filler 0.0875±0.023，overall 0.404±0.015。
- λ=2.0 阴性消融：real named=0.118，random-edge null×5 全 0，但 confshuffle=real=0.118 → 语义性主张被削弱，已如实披露。

## 7. 决策点（P3）

- 若多图复现 named 效应 → 论文主线改为「场 = 骨架检测器 + 语义先验管叶部」的分工叙事。
- 若场在多图上无增量 → 按 problem-inversion 策略转「物理约束层的适用边界」论文。

## 8. 开放问题（仓库无法回答）

1. mean-field 场效应是普适还是本重建图（纯辐条+汇聚 GOAL）的特例？
2. 原始 45 标签人工转译边列表是否可重转译？
3. LLM 先验 GOAL 中心反向是模型怪癖还是语义惯例差异（须跨模型族）？
4. 训练污染：E2 自陈探针弱，须外部成员推断。
5. named/filler 切分的人际一致性 κ（须标注研究）。
