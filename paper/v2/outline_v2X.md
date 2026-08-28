# v2.X 论文骨架（独立新稿，不改动 1.X 论文）

> 2026-08-28 起草（文献定位已回填 reviews/literature_scan_v2X_A/B.md，2026-08-28 定稿）。
> 与 1.X 论文（paper/deposon_paper_v1.md / _en.md）的关系：**接续而非覆盖**——
> v2.X 论文是独立新稿，引用 1.X 作为前序工作；1.X 论文冻结于 v1.9 状态（arXiv 背书待办）。

## 0. 定位声明（文献调研后定稿）

- **首选定位：分工与边界（division-of-labor + boundary mapping）**（文献已确认，2026-08-28）。
  体裁先例三层齐备（Lipton CACM 2019 宣言 / Recht-D'Amour 等顶会模板 / Negative Results
  workshop 六届）；Bowman ACL 2022「Dangers of Underclaiming」作自我设防。
- 备选定位 A：博弈论重构（场=势博弈最好响应极限）——A 路文献确认理论空位存在
  （势博弈/学习动态/图流分解/graphon 极限 × 扩散生成，互不引用），可作 §5 主线。
- 备选定位 B：方法论论文（预登记+独立多角色评审+版本化 verifier 的科研工程范式）。

## 1. 标题候选

1. "Structure or Semantics? Mapping the Domains of Physical-Field and LLM-Prior Signals for Concept-Map Completion"
2. "The Field Detects Skeletons, the Prior Reads Labels: A Boundary Study of Physics-Constrained Diffusion and LLM Priors with Preregistered Kill Criteria"
3. "Potential Games on Mind Maps: Best-Response Limits of a Physics-Constrained Scattering Layer"（博弈论主线备选）

## 2. 摘要骨架（≤250 词，要素已全）

背景：脑图/概念图补全是教育知识工程与 LLM 推理审计的交叉任务，现有工作
或依赖结构启发式或依赖 LLM 语义，二者价值域从未被系统划界。
方法：物理约束散射层的均值场反向（场，纯结构信号）vs labels-only LLM 先验
（纯语义信号），在三大规律设计的 20 图语料（结构否定族 S×16 + 真实语义族 L×4）
上以全候选排序协议对比；全部实验预登记、判死刑则（kill criteria）先于数据冻结。
结果：① 场在枢纽结构上显著优于结构基线（G=20 符号检验 p=0.0075，Wilcoxon 复核
p=0.0031），枢纽集中度是其效力的主导预测子（OLS β=2.12, p=0.0003）；
② 先验在真实语义图上碾压全部臂（named Hits@3 0.48–1.00）并达到直接 CoT 问答
水平（92.5% vs 92.5%）；③ 融合在任一图上均不增（稀释效应，λ∈[0,1]）；
④ 自适应攻击者 100% 绕过关键词规则基线（规则防御降至机会水平），
场对语义陷阱机制性免疫；⑤ 噪声反向动态相对确定性极限的收敛差（gap 0.30，
20/20）支持势博弈解释。结论：结构场与语义先验的价值域正交互补，
我们给出两特征领域鉴定器（hub_concentration, real_semantics）与全套
可复现预登记工件；同源污染与单模型族局限如实声明。

## 3. 章节结构与证据映射

| 节 | 内容 | 证据资产 |
|---|---|---|
| §1 Intro | 任务定位 + 划界问题 + 贡献四条 | docs/Findings_v2.0*.md |
| §2 Related Work | 结构补全 / LLM KGC / 概念图 / 博弈论 / 自适应攻击 / 边界体裁 | paper/v2/related_work_v2X.md（已成稿） |
| §3 Methods | 场（mean-field 反向）+ 先验 + 全候选协议 + 三大规律语料设计 | SPEC v2.0、mindmap_corpus_v20.py |
| §4 Experiments | 4.1 场 vs 结构基线（H-A1/A2）；4.2 先验 vs 全部臂（族 L）；4.3 融合稀释；4.4 BOSS 扫描披露；4.5 GT-2 自适应攻击；4.6 方向一致率 vs Reversal Curse；4.7 领域鉴定器；4.8 题库效度与 CoT 收编 | results/deposon_v20_*.json、quizbank |
| §5 Game-theoretic analysis | GT-1 势博弈收敛、GT-4 PoA（median 1.33 ≈ Pigou 4/3）、向量属性审计 | results/deposon_v20_gt.json、vector_audit |
| §6 Boundary & Discussion | H-B1 违规 2 例、相变阴性、同源污染、单模型族局限、领域鉴定器适用范围 | Findings 全文 |
| §7 Methodology artifact | 预登记/修正案/阴性归档/独立评审/verifier 工程 | SPEC、reviews、verifier/ |
| Appendix | 基线注册表、逐图数字、缓存 provenance、攻击者标签样例 | BASELINE_REGISTRY、familyL caches |

## 4. 与 1.X 论文的衔接声明（写入 §1）

1.X 建立了散射层框架与基准纪律，并在整改中证明：基准效应量结构性不可归因、
规则基线可追平管线（v1.9）。v2.X 把这些阴性结果转化为研究问题本身：
信号的价值域在哪里？——否定之否定作为方法论（1.X 为正题，v1.9 为反题，
本稿为合题）。

## 5. 目标 venue 分析（文献调研后定稿，2026-08-28）

- 主选：NeurIPS/ICLR（Datasets & Benchmarks 轨）——20 图语料+预登记工件+基线注册表是硬资产；
  理论空位（势博弈×扩散互不引用）与实证空位（PoA=4/3 实例级复现、方向一致率 vs Reversal Curse）
  足以支撑 Methods 轨备选。
- 备选一：Insights from Negative Results workshop（体裁完全对口，可作先声）。
- 备选二：LAK/EDM（KitBuild 同体裁社群，须先承认 Pinandito 2021 与 Ma & Chen 2025）。
- 投稿前检查单：领域鉴定器 v0 须在 ≥2 张新图上复现；GT-3 跨模型先验完成或明确降级声明。

## 6. 待办（投稿前 kill list）

- [x] 文献定位回填（A/B 扫描，2026-08-28）与 Related Work 成稿
- [ ] GT-3 跨模型先验（需第二模型族；未做则 §6 明确降级）
- [ ] 领域鉴定器 v0 新图复现（≥2 张）
- [ ] 双语稿（CN/EN 同步，沿用 1.X 的独立编辑+独立复核流程）
- [ ] arXiv 背书（1.X 遗留，两稿可共用一次背书通道）
