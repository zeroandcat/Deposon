# Review — Deposon v2.X 论文骨架（paper-review-coach 四维框架）

> 评审日期：2026-08-30。评审对象：paper/v2/outline_v2X.md、paper/v2/related_work_v2X.md，
> 对照证据：docs/Findings_v2.0.md、docs/Findings_v2.0_corrections.md（C1–C5）、
> docs/Findings_v2.0_crossval.md、docs/Findings_v2.0_skills.md、docs/Findings_GT3.md、
> docs/SPEC_v2.0.md、docs/SPEC_GT3.md（含 A1/A2/A3）、reviews/literature_scan_v2X_A.md。
> 目标 venue 校准：NeurIPS/ICLR Datasets & Benchmarks 轨 / boundary-analysis 体裁。
> 本文件为新建评审，不改动任何既有文件。

## 总分与总评

| 维度 | 分数 | 一句话理由 |
|---|---|---|
| Originality | **7/10** | 分工+划界定位与势博弈×扩散交叉空位有新意；但理论贡献尚无定理支撑，语料规模小（20–22 图、30–45 节点 DAG）。 |
| Methodology | **8/10** | 预登记+斩杀线+修正案+机械判定+三厂商 GT-3b 是罕见的纪律资产；扣分点为 PoA 操作化非标准、统计口径多次事后漂移（20→22 图）、verifier 曾漏查 kill_lines。 |
| Results | **5/10** | 底层数据扎实且诚实归档，但**摘要骨架与更正文档存在三处未同步的直接矛盾**（M1–M3），PoA 叙事过度解读（M4）。 |
| Writing | **6/10** | 证据映射表与衔接声明清晰、体裁自觉性强；但摘要违反自家「headline 一律标注判死状态」规则，待办清单过时。 |

**总评：borderline**（NeurIPS D&B 口径）。作为骨架其定位与方法论资产足以支撑 weak accept，
但 M1–M5 若不闭合，正文成稿必然继承过时/被撤回宣称，届时将滑向 reject。
骨架阶段发现这些问题成本最低——这正是本轮评审的价值。**Major 5 条，Minor 7 条。**

---

## Major findings

### M1（Results/Writing，最高严重度）：摘要 ② 原样复活了已被 C2 撤回的「先验=CoT」宣称
- **位置**：outline_v2X.md §2 摘要骨架：「达到直接 CoT 问答水平（92.5% vs 92.5%）」。
- **证据**：Findings_v2.0_corrections.md C2 明确撤回该声称——题库陷阱选项非图节点，
  先验有效任务 39/40 退化为 2 选 1，期望 94.4% 完全解释观测的 92.5%；可比口径为
  CoT 92.5%（4 选 1 带选项文本）vs 先验开放 top-1 67.5% / top-3 82.5%。
- **影响**：这是骨架里最危险的一处——把一个被预登记修正案正式撤回的 headline 写进摘要，
  若进入正文将构成实质性错误宣称，审稿人一旦追查到 corrections 文档，全文可信度崩塌。
- **必须改为**：删除「92.5% vs 92.5%」，替换为可比口径三元组，并注明题库 92.5% 为
  2 选 1 退化口径、不携带信息（corrections C2 与 SPEC_v2.0_amendment1 的既有口径）。

### M2（Results）：摘要 ① 未标注 H-A 判死状态，且 p 值为过时口径
- **位置**：outline §2 摘要 ①：「场在枢纽结构上显著优于结构基线（G=20 符号检验 p=0.0075…）」。
- **证据**：corrections C1——冻结结果 JSON `H_A_dead.triggered=true`（20 图 3 反转），
  按预登记析取规则 **H-A（vs random）判死**；存活表述应为「vs degree 跨口径稳健
  （Holm 过）+ 高 hub 图局部优势（S6 族 0.471）」；且 22 图口径下 H-A1 p=0.0118，
  「p=0.0075」是 20 图旧口径（corrections E1：MANIFEST 快照 20→22 使 p 漂移）。
  corrections 明文规定「headline 一律标注判死状态」。
- **影响**：摘要使用「显著优于结构基线」且引用旧 p 值，双重违反自家诚实规则；
  「枢纽结构上」的限定也强于证据（反转图恰分布于语义/低枢纽图，边界证据与优势同体）。
- **必须改为**：标注 H-A vs random 判死；改写为「vs degree 稳健 + 枢纽局部优势 +
  斩杀线触发本身即边界证据」；p 值统一为最终语料口径并注明语料 sha。

### M3（Results/Writing）：摘要 ④ 与 Related Work §2.5 混淆了两条 GT-2 证据轨的判定
- **位置**：outline 摘要 ④「自适应攻击者 100% 绕过关键词规则基线（规则防御降至机会水平）」；
  related_work_v2X.md §2.5「规则基线降至机会水平 27.5%」。
- **证据**：预登记主协议（crossval §三）的机械判定是 **no_separation**——rule_filter
  仅 −7.5pp，未达 20pp 阈值，「攻击强度未达决定性强度」如实归档；
  「27.5%≈机会水平（25%）」来自**另一条题库轨**（Findings_v2.0_skills.md §三）。
- **影响**：摘要把题库轨的戏剧化数字嫁接在主协议的攻击宣称上，隐去了 no_separation
  判定——这属于选择性引用自家数据，与全文「机械判定为准」的纪律直接冲突。
- **必须改为**：双轨并述（LOO 协议 no_separation、−7.5pp；题库轨 rule=27.5%≈机会），
  并注明 GT-2 升级（多陷阱强度）为 v2.1 候选后再谈防御结论。

### M4（Results/Originality）：PoA「几乎精确落在 Pigou 界上」是数值巧合级的过度解读
- **位置**：related_work §2.4「median PoA=1.33 几乎精确落在 Pigou 界上」「实例级复现」。
- **证据**：(i) SPEC_v2.0 §3 的操作化 PoA = field_mean / max（自利臂），这不是经典
  worst-case-NE/social-optimum 比值，与 Roughgarden–Tardos 4/3（仿射拥塞 worst-case 界）
  不同度量；(ii) literature_scan_v2X_A.md 第 102/132 行自己都加了前提——「需讨论我们的
  成本结构是否仿射型」，该前提至今未闭合；(iii) Findings_v2.0 §三：4 张真实语义图中
  2 张 PoA<1（0.5、0.75），GT-4 判定自带裂缝。
- **影响**：boundary 体裁最忌在理论锚点上 overclaim；「实例级复现 Pigou 界」一旦被
  博弈论审稿人拆穿，空位 3 整条实证叙事受损。
- **必须改为**：改称「分布级 PoA 报告（应用文献稀少，Benita 2020 例外）+ 中位数
  数值上与 4/3 的巧合性对齐」，或先证明成本结构仿射/可分再主张复现；PoA<1 两图必须并列呈现。

### M5（Writing/Results）：GT-3b 完成后，同源污染与单模型族措辞全线未更新
- **位置**：outline 摘要结尾「同源污染与单模型族局限如实声明」；outline §5 投稿前检查单
  「GT-3 跨模型先验完成或明确降级声明」；outline §6 待办「GT-3 跨模型先验（需第二模型族；
  未做则 §6 明确降级）」；related_work §2.2「须声明两点降级：图与先验同模型族（同源污染）」。
- **证据**：Findings_GT3.md——GT-3b 已完成：E3 doubao（ByteDance）4/4、E4 deepseek 6/6，
  合计 0 败绩，全 ok 域 Kendall W=1.0；「同源污染 artifact 假说被实质性削弱」，
  残余局限为三族均为中文优化大模型（GT3 局限 #1）。
- **影响**：骨架仍按「局限未解」的旧状态组织叙事，既低估了已有证据（underclaim，
  与 Bowman 设防自相矛盾），也让 §6 降级预案成为死条款。
- **必须改为**：摘要结果区补 GT-3b 一句话（跨厂商 0 败绩、W=1.0、未排除共享中文语料）；
  related_work §2.2 的降级声明改为「削弱但未排除」口径；划掉过时待办。

---

## Minor findings

- **m1（Writing）**：标题候选 2「The Field Detects Skeletons」在 H-B1 两例违规
  （L_historical_causality filler=0.344，Findings_v2.0 §一）之后过强；建议改用
  「Structure-Sensitive Ranker」类措辞或标题内自带边界限定。
- **m2（Results）**：摘要 ③「融合在任一图上均不增（λ∈[0,1]）」——实际证据为
  v1.6 单图 λ∈{0.25,0.5,1,2}（量纲饱和，λ=0.25 即饱和，paper/_paper_backup_v19 §相关段落）
  与 v2.0 四图 λ=0.5（crossval §一）；全区间宣称超出实测点，应写「在所测 λ 档上」。
- **m3（Originality）**：空位 1「五簇理论与扩散生成模型互不引用」是阴性文献宣称，
  目前仅有 literature_scan_v2X_A §66/§136 的定性观察（且 Teng 2017 已命中一例部分桥接）。
  投稿前须给出可审计的检索协议（查询式、库、日期、命中数）入附录，否则改为「尚未发现」。
- **m4（Methodology）**：GT-1「gap 0.30、20/20 支持势博弈解释」（Findings_v2.0 §三）是
  一致性证据而非证明——「场=势函数最好响应极限」（related_work §2.4 称「升格为理论主张」）
  目前无命题+证明。要么补一个形式化命题（即使在小图类上），要么摘要改为
  「consistent with a potential-game reading」。
- **m5（Results）**：摘要引用 OLS β=2.12, p=0.0003（Findings_v2.0_skills.md §二），
  但源文档自标「n=20 小样本、探索性 v0、v2.1 扩图后重估」——摘要须带同样限定词，
  否则与 H-A 判死并置时显得选择性呈现。
- **m6（Writing）**：skills.md §三「field_mean 52.5%（2×机会）：部分迁移」与 corrections
  C2「52.5% 记为 2 选 1 机会水平，不携带信息」相互矛盾；§4.6/4.7 成稿前须裁定其一。
- **m7（Writing）**：outline §6 kill list 中「文献定位回填」已完成（related_work 成稿）、
  GT-3 已完成——待办清单整体过时，且 22 图口径（corpus 含 S1/S2 尺寸扫描档）与
  摘要「20 图语料」表述需统一为最终快照口径。

---

## 针对四项特别审查的结论

1. **摘要同步性**：未通过。M1（92.5%）、M2（判死+p 值）、M3（机会水平）三处与
   corrections/crossval 直接冲突，是本轮评审最重的一簇问题。
2. **boundary 体裁的 overclaim 面**：存在。M4（PoA）、m1（标题）、m2（λ 区间）、
   m4（势博弈升格）构成 overclaim 清单；Bowman 设防防了 underclaim，未防 overclaim。
3. **Related Work 三空位支撑**：边界体裁空位（§2.6 三层先例）支撑充分；PoA 4/3
   空位叙事建立在对齐巧合上（M4）；势博弈×扩散空位方向可信但需检索协议固化（m3）。
4. **同源污染措辞**：必须更新（M5）——GT-3b 证据已在库，骨架却仍按未完成状态写作。

## Top-5 投稿前必须闭合的行动项

1. **重写摘要 ①②④**：按 C1 标判死、按 C2 撤回 92.5% 对比、按 crossval 双轨并述
   GT-2；摘要每个数字机械追溯到结果 JSON 字段（沿用 corrections D 节规矩）。
2. **全库同步 GT-3b 后口径**：摘要、related_work §2.2、outline §5/§6 的同源污染/
   单模型族表述统一为「跨厂商削弱、中文优化族残余局限」。
3. **PoA 叙事降级或证明**：定义清操作化 PoA 与经典 PoA 的差异，并列 PoA<1 两图；
   或补仿射成本结构论证后再用「Pigou 对齐」。
4. **势博弈主张形式化或降调**：给出「mean-field 反向=无噪声最好响应动态」的命题
   与证明（至少在小图类），否则全稿统一为 consistency 口径。
5. **领域鉴定器 v0 新图复现**：按 outline §5 检查单在 ≥2 张新图上预登记复现
   （hub_concentration/real_semantics 规则），并在摘要为 OLS 结果加探索性限定。

---
*评审人：独立 review specialist（paper-review-coach 四维框架）。未改动任何既有文件。*
