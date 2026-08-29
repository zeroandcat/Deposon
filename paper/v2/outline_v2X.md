# v2.X 论文骨架（独立新稿，不改动 1.X 论文）

> 2026-08-28 起草（文献定位待 reviews/literature_scan_v2X_A/B.md 回填后定稿）。
> 与 1.X 论文（paper/deposon_paper_v1.md / _en.md）的关系：**接续而非覆盖**——
> v2.X 论文是独立新稿，引用 1.X 作为前序工作；1.X 论文冻结于 v1.9 状态（arXiv 背书待办）。

## 0. 定位声明（三选一，文献调研后定夺）

- **首选定位：分工与边界（division-of-labor + boundary mapping）**（文献已确认，2026-08-28）。
  体裁先例三层齐备（Lipton CACM 2019 宣言 / Recht-D'Amour 等顶会模板 / Negative Results
  workshop 六届）；Bowman ACL 2022「Dangers of Underclaiming」作自我设防。
- 备选定位 A：博弈论重构（场=势博弈最好响应极限）——若 A 路文献显示该空位真实存在。
- 备选定位 B：方法论论文（预登记+独立多角色评审+版本化 verifier 的科研工程范式）。

## 1. 标题候选

1. "Structure or Semantics? Mapping the Domains of Physical-Field and LLM-Prior Signals for Concept-Map Completion"
2. "A Structure-Sensitive Ranker vs a Label-Reading Prior: A Boundary Study of Physics-Constrained Diffusion and LLM Priors with Preregistered Kill Criteria"
   （原候选 "The Field Detects Skeletons…" 已弃用——H-B1 两例违规后措辞过强，见评审 m1）
3. "Potential Games on Mind Maps: Best-Response Limits of a Physics-Constrained Scattering Layer"（博弈论主线备选）

## 2. 摘要骨架（≤250 词，要素已全）

背景：脑图/概念图补全是教育知识工程与 LLM 推理审计的交叉任务，现有工作
或依赖结构启发式或依赖 LLM 语义，二者价值域从未被系统划界。
方法：物理约束散射层的均值场反向（场，纯结构信号）vs labels-only LLM 先验
（纯语义信号），在三大规律设计的 22 图语料（结构否定族 S×16 + 真实语义族 L×4
+ S1/S2 尺寸扫描档；以最终语料快照 sha 为准）上以全候选排序协议对比；
全部实验预登记、判死刑则（kill criteria）先于数据冻结。
结果：① 场对结构基线的优势按预登记析取斩杀线 **H-A1（vs random）判死**
（冻结 JSON `H_A_dead.triggered=true`，22 图 4 反转）；存活表述为
**field_mean > degree 跨口径稳健**（Holm 过；22 图口径 H-A1 p=0.0118，
语料 20→22 快照漂移已归档）加高 hub 图局部优势（S6 族 0.471），
且斩杀线触发本身（反转图全部分布于语义/低枢纽图）即分工边界的直接证据；
枢纽集中度是其效力的主导预测子（OLS β=2.12, p=0.0003；n=20 小样本、
探索性 v0，v2.1 扩图后重估）；
② 先验在真实语义图上碾压全部臂（named Hits@3 0.48–1.00）；可比口径为
CoT 92.5%（带选项文本的 4 选 1）vs 先验开放 top-1 67.5% / top-3 82.5%——
题库 92.5% 系陷阱选项非图节点导致的 2 选 1 退化口径（期望 94.4% 完全解释
观测），不携带信息，「先验=CoT」宣称已按修正案 C2 正式撤回；
③ 融合在所测 λ 档上均不增（稀释效应；实测点：v1.6 单图 λ∈{0.25,0.5,1,2}，
λ=0.25 即量纲饱和；v2.0 四图 λ=0.5）；
④ 自适应攻击者 100% 绕过关键词规则基线，但两条证据轨判定不同：
主 LOO 协议（crossval §三）为 **no_separation**（rule_filter −7.5pp，
未达预登记 20pp 阈值，攻击强度未达决定性强度如实归档，GT-2 多陷阱升级
列为 v2.1 候选）；题库轨（skills §三）rule=27.5%≈机会水平（25%）。
场对语义陷阱机制性免疫（不读标签，注入下 −0.0pp）；
⑤ 噪声反向动态相对确定性极限的收敛差（gap 0.30，20/20）**与势博弈解读一致**
（consistent with a potential-game reading；一致性证据而非证明，
形式化命题见 §5 待办）。结论：结构场与语义先验的价值域正交互补，
我们给出两特征领域鉴定器（hub_concentration, real_semantics）与全套
可复现预登记工件；GT-3b 跨厂商检验已完成——doubao（ByteDance）4/4、
deepseek（DeepSeek）6/6，三模型族合计 0 败绩、全 ok 域 Kendall W=1.0，
「同源污染 artifact」假说被实质性削弱（残余局限：三族均为中文优化大模型，
共享中文语料不可排除）。

## 3. 章节结构与证据映射

| 节 | 内容 | 证据资产 |
|---|---|---|
| §1 Intro | 任务定位 + 划界问题 + 贡献四条 | docs/Findings_v2.0*.md |
| §2 Related Work | 结构补全 / LLM KGC / 博弈论图算法 / 边界论文范式 | reviews/literature_scan_v2X_A/B.md（回填） |
| §3 Methods | 场（mean-field 反向）+ 先验 + 全候选协议 + 三大规律语料设计 | SPEC v2.0、mindmap_corpus_v20.py |
| §4 Experiments | 4.1 场 vs 结构基线（H-A1/A2）；4.2 先验 vs 全部臂（族 L）；4.3 融合稀释；4.4 GT-2 自适应攻击；4.5 领域鉴定器；4.6 题库效度；4.7 CoT 收编 | results/deposon_v20_*.json、quizbank |
| §5 Game-theoretic analysis | GT-1 势博弈收敛（consistency 口径，除非补形式化命题+证明，见评审 m4）、GT-4 PoA（操作化定义与经典 PoA 差异如实声明；median 1.5 / 13 图；族 L 2 图 PoA<1 并列披露，见评审 M4）、向量属性审计 | results/deposon_v20_gt.json、vector_audit |
| §6 Boundary & Discussion | H-B1 违规 2 例、相变阴性、同源污染（GT-3b 后口径：跨厂商削弱、中文优化族残余局限）、领域鉴定器适用范围 | Findings 全文 |
| §7 Methodology artifact | 预登记/修正案/阴性归档/独立评审/verifier 工程 | SPEC、reviews、verifier/ |
| Appendix | 基线注册表、逐图数字、缓存 provenance、攻击者标签样例 | BASELINE_REGISTRY、familyL caches |

## 4. 与 1.X 论文的衔接声明（写入 §1）

1.X 建立了散射层框架与基准纪律，并在整改中证明：基准效应量结构性不可归因、
规则基线可追平管线（v1.9）。v2.X 把这些阴性结果转化为研究问题本身：
信号的价值域在哪里？——否定之否定作为方法论（1.X 为正题，v1.9 为反题，
本稿为合题）。

## 5. 目标 venue 分析（文献调研后定稿，2026-08-28）

- 主选：NeurIPS/ICLR（Datasets & Benchmarks 轨）——22 图语料（最终快照口径）+预登记工件+基线注册表是硬资产；
  理论空位（势博弈×扩散互不引用——阴性文献宣称，须附可审计检索协议入附录，
  否则统一改写「尚未发现」，见评审 m3）与实证空位（分布级 PoA 报告：median PoA=1.5，
  13 图有限值；操作化 PoA=field_mean/max(自利臂) 与经典 worst-case-NE/社会最优
  比值不同度量，数值上与 Pigou 4/3 的对齐仅为巧合性对齐、不再主张「实例级复现」；
  族 L 2/4 图 PoA<1（0.5、0.75）必须并列披露；方向一致率 vs Reversal Curse）
  足以支撑 Methods 轨备选。
- 备选一：Insights from Negative Results workshop（体裁完全对口，可作先声）。
- 备选二：LAK/EDM（KitBuild 同体裁社群，须先承认 Pinandito 2021 与 Ma & Chen 2025）。
- 投稿前检查单：领域鉴定器 v0 须在 ≥2 张新图上复现；GT-3b 跨厂商先验已完成
  （doubao 4/4、deepseek 6/6、0 败绩、W=1.0），口径统一为「同源污染被实质性
  削弱但未完全排除（三族均中文优化模型）」，§6 降级条款随之关闭。

## 6. 待办（投稿前 kill list）

- [x] ~~文献定位回填（A/B 扫描）与 Related Work 成稿~~（related_work_v2X.md 已成稿）
- [x] ~~GT-3 跨模型先验~~（GT-3b 完成，2026-08-30，见 docs/Findings_GT3.md；
  残余局限为三族均中文优化模型，§6 保留如实声明而非降级）
- [ ] 领域鉴定器 v0 新图复现（≥2 张）
- [ ] 双语稿（CN/EN 同步，沿用 1.X 的独立编辑+独立复核流程）
- [ ] arXiv 背书（1.X 遗留，两稿可共用一次背书通道）
- [ ] 空位 1 阴性文献宣称的可审计检索协议（查询式/库/日期/命中数）入附录，
      否则全稿统一「尚未发现」（评审 m3）
- [ ] 势博弈形式化命题（小图类「mean-field 反向=无噪声最好响应动态」），
      未补则全稿维持 consistency 口径（评审 m4）
- [ ] §4.6/4.7 裁定 52.5% 口径矛盾（skills「2×机会 部分迁移」vs corrections C2
      「2 选 1 机会水平，不携带信息」），成稿前取其一（评审 m6）

---
修订记录：2026-08-30 按 reviews/review_coach_v2X_outline.md 闭合 M1–M5
（M1 摘要②撤回「92.5% vs 92.5%」改 C2 可比口径；M2 摘要①标 H-A1 判死 +
22 图 p=0.0118；M3 摘要④双轨并述 no_separation −7.5pp / 题库轨 27.5%；
M4 PoA 叙事降级为分布级报告 + PoA<1 两图披露；M5 全文更新 GT-3b 后同源污染
措辞并清除过时待办；Minor m1/m2/m3/m4/m5/m6/m7 一并处理）。
