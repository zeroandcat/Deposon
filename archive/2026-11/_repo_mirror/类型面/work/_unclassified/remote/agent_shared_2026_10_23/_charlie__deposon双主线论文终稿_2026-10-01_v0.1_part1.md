# deposon 双主线研究报告：判死线制度下的博弈论验证与思维链批判性蒸馏（V3 × V4）

> **〔分件元信息 · 装配轮剥离〕**
> - **本件**：part1（前置区＋§1 引言＋§2 主线帧与术语约定＋§3 方法论：判死线制度）· v0.1 · 2026-10-01
> - **派发**：群管理员 2026-10-01 10:13:42 派单（第 2 轮 · part1 写作轮；沿《双主线论文骨架与分件计划》§2.1 切分表与 §2.2 分件纪律执行）
> - **本轮精读素材（按派单）**：委托书 v0.2（`a17275086734` · 21,014 B，总纲复阅）；线索册 v0.2（`998221ed5947` · 63,656 B）§0/§4.1/§4.3/§6＋卷首主线帧＋条目 2.35/2.44/2.80；鲍勃体例底账①（`22533dd80d50` · 17,311 B，回函/体例惯例面）；交叉面底账 §3（`246b6923cefd` · 10,277 B，引用注意事项）
> - **引用锚当轮实测**：本 part 引用的 25 件素材（含上述依据件 5 件）已按分件纪律逐件 sha256/stat 实测复算，实测值与底账登记值全等；登记表见件尾
> - **落盘检查**：落盘前实测撞名，目标名为新建件（0 覆写任何既有件）
> - **本件自身指纹**：落盘后实测随群内通报回执报出（0 自写入本件）

---

## 前置区

### 题名块

**中文题名**：deposon 双主线研究报告：判死线制度下的博弈论验证与思维链批判性蒸馏（V3 × V4）

**英文题名**：*Deposon Dual-Track Report: Kill-Line-Governed Game-Theoretic Verification and Critical Chain-of-Thought Distillation (V3 × V4)*

**版本行**：v0.1（分件 part1 · 2026-10-01）｜体裁：预印本/技术报告体例（目标期刊/会议「待PI补」——体裁与引用格式终裁归 PI）｜载体：Markdown 单载体（`.tex` 转换留排版轮）

**署名面**：起草方署名 GLM 侧名义；起草 model/版本「以PI为准」；双盲/署名口径归 PI（在双盲语境下给出已发表件编号 arXiv:2609.09001 即构成去匿名，投稿口径由 PI 裁定，见 §1.1）[R-1][R-3]

### 摘要

deposon 项目在 V1（脑图主线）与 V2（博弈论解释）合并发表（arXiv:2609.09001，元数据「待核」）之后，沿两条主线推进：V3（博弈论主线）与 V4（蒸馏主线）。本报告呈交双主线的判定实践与结果。其方法论底座为全项目统一的判死线制度：分支终态只出 PASS／FAIL／KD 三态；判死线（`K-*`／`TH-*`）先于实验冻结、生效即锁、冻后 0 改、0 事后追加口径；每条判定必附根因（真证伪／假证伪／混合／不明）；双向外推禁令与软化禁令双向生效；历史上一例「假判定」事件经六项复核全部照录落位。

V3 主线：GT 系 5 案经判死线 v2 并列判正式收档——gt5 claim 终态＝FAIL（判死落定），根因＝混合（构造面真证伪＋素材面 4/22 未覆盖全称＋载荷集中单图）；gt6、gt8、gt5b 与 GT-4 腿、GT-1 腿＝PASS（构造面·封口生效，0 新判）；主读法与两个替代读法（分腿读法、均值尺度读法）三者并列，分歧如实写明。#35 复合 claim v2＝FAIL（α、β 两腿成对 FAIL），根因＝假证伪 ×3（真证伪 0／混合 0／不明 0）；v3 尚未出判定（登记状态：提案·待 PI 复核）。P-J／P-M／P-C 三族终态全部落 KD（P-J、P-M＝假证伪；P-C＝0 真证伪 0 假证伪 ⇒ 不可算落 KD）；其覆盖面自证落 FAIL（该判定棒总判 FAIL 成立）。理论界链（C4／P-B 失真界 D(M,T)）理论侧四输入未到位 ⇒ 结构性不可算、判死线悬空。

V4 主线：蒸馏目标＝AI 批判性学习 PI 思维方式（非画像），度量三件套＝结构相似＋分歧批判理由＋盲从率（v1「复现一致率」画像式口径已废，0 沿用）。任务 B v2 正式判定＝FAIL——四 kill-line 全 hit（K-V2-a 结构相似 0.0909＜0.80；K-V2-b1 分歧批判理由覆盖 0.6842＜1.00；K-V2-b2 盲从率 0.3333＞0.10；K-V2-c bootstrap CI [0.0, 0.2045]＜0.50），复合定性＝2 复合＋2 β（0 纯 α），verifier 独立复核签字 VERDICT: PASS。任务 B v3（消解 A／B 落地后）正式判定＝FAIL（5/6 hit 全 FAIL；K-V3-E 双口径一致线不触发）。FAIL 判定 0 外推为「思维链不可蒸馏」。

全部判定字面与读数按盘上登记值逐字保真引述（0 软化、0 外推、0 改写数值）；不可判面照写不可判；引用素材以「路径＋SHA-12＋字节」三元组锚定并在写作轮当轮实测复算；已发表件元数据与缺件读数等不可核面按三标注体例如实标注。

**关键词**：判死线；三态制度；博弈论验证；思维链蒸馏；负结果；假判定复核；可核性

> 摘要读数来源：委托书 §4 摘要视图与线索册对应条目关键读数（线索册自判定件实读摘引，0 改写）[R-1][R-2]；逐案锚件（判定件本体，当轮指纹实测）见件尾引用登记表 R-11、R-14–R-17。

### Abstract

Following the merged publication of the V1 (mind-map track) and V2 (game-theoretic interpretation) results (arXiv:2609.09001; metadata pending verification), the deposon project advanced along two tracks: V3 (game-theory track) and V4 (distillation track). This report presents the adjudication practice and outcomes of both tracks on a shared methodological foundation: the project-wide kill-line regime. Terminal states admit exactly three values — PASS / FAIL / KD ("not computable"); kill-lines (`K-*` / `TH-*`) are frozen before experiments, locked upon activation, and never altered or appended after freezing; every verdict carries a mandatory root-cause classification (true falsification / spurious falsification / mixed / indeterminate); bidirectional extrapolation bans and anti-softening bans are in force; and one historical "fake-verdict" incident was disposed of through a six-item re-verification, all items recorded verbatim.

On the V3 track, the five GT cases were formally closed under kill-line v2 parallel adjudication: gt5 — claim terminal state FAIL (kill confirmed; root cause: mixed — genuine falsification on the constructed surface, 4/22 material under-coverage of the universal claim, and load concentration on a single graph); gt6, gt8, gt5b, and the GT-4 and GT-1 legs — PASS (constructed surface; sealing effective, no new verdict); the primary reading and two alternative readings (per-leg reading; mean-scale reading) are reported side by side with the divergence stated. The #35 composite claim v2 is FAIL (both the α and β legs FAIL), root cause spurious falsification ×3 (true 0 / mixed 0 / indeterminate 0); v3 has not yet produced a verdict. The P-J / P-M / P-C families all terminate in KD (P-J / P-M: spurious falsification; P-C: 0 true and 0 spurious, hence not computable); their coverage self-check terminates FAIL. The theoretical bound chain (C4 / P-B distortion measure D(M,T)) remains structurally non-computable — four theoretical inputs outstanding — leaving its kill-line suspended.

On the V4 track, the distillation target is the AI's critical learning of the PI's way of thinking (not profiling), measured by the triad of structural similarity, divergence-critique justification, and blind-obedience rate. Task B v2 is formally FAIL — all four kill-lines hit (structural similarity 0.0909 < 0.80; divergence-critique coverage 0.6842 < 1.00; blind-obedience rate 0.3333 > 0.10; bootstrap CI [0.0, 0.2045] < 0.50); composite qualification: 2 composite + 2 β (0 pure α); the verifier's independent re-check is signed VERDICT: PASS. Task B v3 (after dispositions A and B) is FAIL (5/6 kill-lines hit, all FAIL; the dual-caliber consistency line K-V3-E not triggered). The FAIL verdicts are not extrapolated to "chain-of-thought is undistillable."

All verdict literals and readings are quoted verbatim from on-disk registered values (no softening, no extrapolation, no rewritten numbers); non-decidable faces are reported as non-decidable; every cited artifact is anchored by the triple of path, SHA-12, and byte count, re-verified in the writing round.

**Keywords**: kill-line; three-state regime; game-theoretic verification; chain-of-thought distillation; negative results; fake-verdict re-verification; auditability

### 标注体例说明（三条字面 · 0 变体）

本报告全文仅使用以下三种标注字面：

1. **「待PI补」**——素材有登记、盘上无实体（缺件类）：相关读数在本工作区不可复核，须 PI 补送原件后方可升格核验。
2. **「待核」**——实体在盘（指纹可实测）、相应内容或元数据未完成核实；或双版本/多口径并存需 PI 裁定；或外部原文不在本工作区、无法独立核实。计数类沿旧件登记值引用时，一律采用句式「沿旧件登记值，现值待核」（归「待核」族）。
3. **「以PI为准」**——口径/权属类信息：权威源或裁定权在 PI 侧，本报告不代填、不代裁。

**判定字面纪律**：本报告所有判定读数与 verdict 字面沿盘上登记值逐字保真引述（0 软化、0 外推、0 改写数值）；判定句不使用「但／然而／仍有希望／不排除／证据不足／待进一步验证／初步／大致」等软化措辞——「诚实的根因是不误导：机械诚实不合格」（沿线索册 §4 节首纪律字面）[R-2]。

---

## §1 引言

### §1.1 背景与起点

deposon 项目的第一阶段成果已合并发表：*Deposon: An Auditable, Conservation-Guaranteed, Game-Theoretically Tested Scattering Layer over LLM Reasoning Paths*（arXiv:2609.09001；登记元数据：作者 Qihao Yuan · 日期 2026-09-08 · 分类 cs.AI）。按委托口径，该四项元数据系委托材料登记值，已发表原文不在本工作区、起草侧 0 打开外部原文核实 ⇒ 标注「待核」[R-1][R-3]。已发表件的中文／英文论文本体在盘：`paper/deposon_paper_final_cn.md`（`c5f6a23f4408` · 53,838 B）[R-5]、`paper/deposon_paper_final_en.md`（`2ec20b96e941` · 68,164 B）[R-6]；本报告引用已发表件时按路径调阅原件、0 复制其正文段落（沿线索册 §1.2 口径）[R-2]。已发表件代码仓库的权威源「以PI为准」——委托材料明示不将登记 URL 代填为唯一权威源，涉外部表述以 PI 侧确认为准 [R-1][R-3]。

**双盲提示**：本报告与已发表件同属一个项目链条——在双盲评审语境下，给出 arXiv:2609.09001 即构成去匿名（该警示字面在盘上 WORLDVIEW 件 L82 逐字在案，本段沿交叉面底账 §3 转引）[R-3]；投稿版本是否保留该编号由 PI 按目标期刊/会议的双盲要求裁定「以PI为准」。

起点之后，项目沿两条主线并行推进（PI 明示主线帧，定义见 §2.1）：V3＝博弈论主线，V4＝蒸馏主线。本报告的起草依据为 PI 侧打包提供的委托书与素材线索册：其中主线与硬约束已点明给足，论文结构 0 预设（0 大纲口径）——本报告的体裁、语言、章节安排与引用体例系起草侧在授权范围内的自定决定 [R-1]。

### §1.2 两主线的核心问题

**V3 · 博弈论主线**（主线一）：沿委托书登记口径，覆盖「deposon 机制 / 判死线 / 理论界链：P-A/B/C、#21/C4、GT 验核等」[R-1][R-2]。其核心实践为：GT 系用例的判死线 v2 并列判（正式判定收口件 `_v5_gt_verdict_2026_09_29.md`，`45648b0ec940` · 57,227 B）[R-11]、#35 复合 claim 构造面判定（v2 判定件 `_v5_item35_v2_verdict_2026_09_29.md`，`b59bef293712` · 26,232 B）[R-16]、P-J/P-M/P-C 退化/共线族判死处置（`_v5_pjpm_pc_verdict_bang3_2026_09_29.md`，`1814f9590f0f` · 41,566 B）[R-17]、C5 修复线与 B 组停步（`_v5_v3_deg_c5_b_halt_report_2026_09_29.md`，`f2b68ee099b5` · 14,862 B）[R-19]，以及 C4/#21 理论输入链与 P-B 失真界的理论面。主线问题可陈述为：机制主张在预冻结判死线治理下的存活面与非存活面各是什么，每条判定的根因归属为何。

**V4 · 蒸馏主线**（主线二）：沿 PI 已拍板口径（论文须准确表述），蒸馏＝AI 批判性学习 PI 思维方式，非画像；呼应 V1 脑图主题 G1「AI 应当如何思考」（GOAL 拓扑智能）；度量三件套＝结构相似＋分歧批判理由＋盲从率，v1「复现一致率」画像式口径已废（0 沿用）[R-1][R-2]。其核心实践为任务 B 判定链 v1→v2→v3（v2 正式判定件 `_v4_pi_cot_v2_verdict_v2.md`，`5d79e67a4e9d` · 33,723 B [R-14]；v3 正式判定件 `_v4_pi_cot_v3_verdict_v3.md`，`bb44fdc7ab0f` · 53,751 B [R-15]）、D 波次采集（D1–D8＋SQ 补采）与 S3/S4 跨日采集实践。主线问题可陈述为：以度量三件套为尺的任务 B 判定链在判死线治理下得出何种终态；不可判面为何不可判。

### §1.3 本文定位与贡献

本报告是 deposon 项目双主线的判定报告（report），非综述、非新理论提出件。其价值主张沿委托目标原文口径：「结论准确、证据可核、不误导」[R-1]。贡献声明四条：

1. **制度层（方法论贡献）**：将全项目统一的判死线制度作为可陈述、可复核的方法论显化呈现——三态冻结、kill-line 先于实验冻结与生效即锁、根因三分类、双向外推禁令、软化禁令、假判定复核制度、指纹锚定（§3）。该制度同时治理两主线的全部判定实践。
2. **V3 主线判定如实归集**（§4）：GT 系 5 案、#35 构造面、#21 族、P 族三案、C5 修复线、理论界链的全部终态与根因按原字面呈交（摘要级读数见摘要；全量判定表见 §6）。
3. **V4 主线负结果如实呈交**（§5）：任务 B v2/v3 正式判定 FAIL 及其全部读数、度量口径与消解路径；FAIL 判定 0 外推为「思维链不可蒸馏」。
4. **诚实纪律的制度化证据**（§3.6）：2026-09-28「假判定」事件经 2026-09-30 六项复核全部照录落位——制度不仅约束常规判定，也约束对判定本身的修正（含登记动作层级的变更与来源等级的保留）。

### §1.4 结构与阅读指引

本报告结构：§2 主线帧与术语约定（帧定义、命名纪律、术语表、引用体例）；§3 方法论（判死线制度，两主线的共同底座）；§4 V3 博弈论主线（4.1 GT 系判定链／4.2 #35 构造面／4.3 #21 族／4.4 P-J·P-M·P-C 三族与覆盖面自证／4.5 C5 修复线与 B 组停步／4.6 P-6 与 F2 执行面／4.7 理论界链 C4-P-B／4.8 R-J5 三方对质）；§5 V4 蒸馏主线（5.1 蒸馏目标口径／5.2 协议面／5.3 任务 B 判定链／5.4 D 波次采集／5.5 S3-S4 面／5.6 V4-LLM 资产面／5.7 补审链）；§6 负向结论与判死线汇总（全量判定表按原字面归集、两处「诚实但不好看」、分歧并报）；§7 核心准则四条（显化呈现）；§8 跨主线讨论；§9 局限与未完成面；§10 结论；§11 AI 使用披露；References 与附录 A（任务 B v2 kill-line 逐行表）、附录 B（三标注总表）。

阅读提示三条：其一，本报告为分件交付的 v0.1 初稿（本件为 part1，覆盖前置区＋§1–§3；§4–§11 与 References 由后续分件续成，装配轮合并）；其二，判定字面与读数逐字保真（0 软化／0 外推），请勿期待对冲性措辞；其三，全部盘上素材引用以「路径＋SHA-12＋字节」三元组锚定（件尾登记表），已发表件元数据与缺件读数按三标注体例如实标注。

---

## §2 主线帧与术语约定

### §2.1 主线帧定义

主线帧沿 PI 明示口径（委托书 §1.1 与线索册卷首两处登记一致）[R-1][R-2]：

| 帧标签 | 含义（沿登记字面） |
|---|---|
| **V1** | **脑图主线**（核心主题 **G1「AI 应当如何思考」** · GOAL 拓扑智能） |
| **V2** | **博弈论解释** |
| **V1V2** | **已合并发表**：*Deposon: An Auditable, Conservation-Guaranteed, Game-Theoretically Tested Scattering Layer over LLM Reasoning Paths*，arXiv:2609.09001（作者 Qihao Yuan · 2026-09-08 · cs.AI；元数据四项「待核」，见 §1.1） |
| **V3** | **博弈论主线**（本报告主线一） |
| **V4** | **蒸馏主线**（本报告主线二） |

⛔ 勿将 V1/V2/V3/V4 作普通阶段序号混用——阶段/版本名（V1/V2/V3/V4/V5…）的**启用权属 PI** [R-1][R-2]。

### §2.2 阶段名纪律与 `_v5_` 前缀声明

本报告所引素材中，部分既有件文件名前缀含 `_v5_` 字样。该前缀系**盘上既有文件名的一部分（历史事实）**：本报告按实照录路径（0 改名、0 覆写），**不将 `_v5_` 前缀解读为阶段名或版本号**——阶段/版本名的启用权属 PI，起草侧不自行启用或沿用阶段名 [R-2]。该命名漂移面已由盘上件 `results/_naming_ruling_note_2026_09_29.md`（`57024f2cd30a` · 7,843 B）登记在案 [R-7]。

### §2.3 术语表

以下术语按盘上字面约定（本报告 0 自行新设口径；语义以所锚登记原文为准）：

| 术语 | 口径（沿盘上字面） | 锚 |
|---|---|---|
| 判死线（kill-line） | 以 `K-*` 编号的终止判定线；`TH-*` 为阈值线；切点全部沿盘上既有字面，0 新设、0 调整、0 以「更合理」为由替换 | [R-2] §4.1 |
| 三态 | PASS / FAIL / KD；KD＝kill-death「不可算」（「不明」按 PI 裁定＝扩写后的 KD，须并报） | [R-2] §4.1 |
| 根因三分类 | 真证伪／假证伪／混合／不明；每条判定必附根因列 | [R-2] §4.1 |
| 预登记／生效即锁 | claim 与判死线在实验前登记并生效锁定；冻后 0 改、0 事后追加口径 | [R-2] §4.1 |
| 构造面／真实面 | 判定覆盖范围的限定语成对面（GT 系判定以「构造面」限定覆盖范围，如「仅覆盖 4 图构造面」；两面向之间的推断受双向外推禁令约束，见 §3.4） | [R-1][R-2] |
| α 腿／β 腿 | 复合 claim 的分腿称谓（软化禁令示例字面：「直书『α 腿被证伪』『β 腿被证伪』」；#35 v2 登记「α、β 两腿成对 FAIL」） | [R-1][R-2] |
| 复合定性（α／β） | 任务 B v2 判定件的复合定性用语族（登记字面「2 复合＋2 β（0 纯 α）」）；语义以判定件原文为准，本报告 0 自行定义 | [R-1][R-14] |
| 度量三件套 | 结构相似＋分歧批判理由＋盲从率；蒸馏成功 ⇔ 结构可迁移 且 对分歧能给出批判理由 且 盲从率低；v1「复现一致率」画像式口径已废 | [R-2] §3.1 |
| 盲从率 | 度量三件套之一；kill-line `K-V2-b2` 的度量项（v2 读数 0.3333＞0.10，hit） | [R-1][R-14] |
| 指纹锚 | `sha256(全文字节)` 取前 12 位、小写＋字节落盘实测；与既有件内登记值不一致者以盘上实测为准并显式标注 | [R-2] §0 |
| 漂移登记 | 既有件 0 回改（追加行模式）；登记差异、0 代裁 | [R-2] §5 |
| E-C 级 | 拍板转述的来源等级标注；「派工单转述 E-C」原字面保留、不抹来源等级 | [R-2] §4.3 |
| 假判定 | 2026-09-28 取证「六案挂假」事件及其复核处置（见 §3.6） | [R-2] §4.3 |
| GT 系 | 博弈论验证用例族：gt5／gt6／gt8／gt5b／GT-4 腿／GT-1 腿（详 §4） | [R-2] §2.2 |
| 双读法 | gt5 的主读法＋替代读法 A（分腿读法）＋替代读法 B（均值尺度读法），三者并列、分歧如实写明（详 §4／§6） | [R-1][R-2] |
| pi_cot／D1–D8／S3／S4／任务 B | V4 主线素材与采集代号（详 §5） | [R-2] §3 |
| 消解 A／B | 任务 B v3 所落地的两项判定消解项（登记字面「消解 A/B 落地后」；详 §5） | [R-1][R-15] |
| 未交付 | 未出判定态：修复件未出（区别于 KD 终态，见 §3.1） | [R-2] §4.2 |
| 棒 | 项目内工作流/交付件的自称用语（沿盘上件字面，如「执行棒报告」「本棒新发现」）；本报告照录用语，0 另行定义 | [R-2] |
| G1 | V1 脑图主线核心主题「AI 应当如何思考」（GOAL 拓扑智能）；V4 蒸馏目标口径呼应 G1 | [R-1][R-2] |

### §2.4 引用与标注体例

1. **三元组引用**：盘上素材引用一律「路径＋SHA-12（小写 12 位）＋字节」；正文以 `[R-n]` 编号与件尾引用登记表闭合（装配轮合并去重为 References，跑闭合断言：0 未引、0 悬空）。
2. **三标注三条字面（0 变体）**：「待PI补」「待核」「以PI为准」（定义见前置区标注体例说明）；计数类沿旧件登记值引用时用句式「沿旧件登记值，现值待核」。
3. **读数转引载体**：核心结论读数系线索册自判定件**实读摘引（0 改写）**——本报告按登记值转引并给出判定件锚（判定件本体为本 part 提供复核入口；其正文内容本 part 未通读，仅作当轮指纹实测）。读数以线索册摘引为载体、以判定件锚为复核入口 [R-2]。
4. **已发表件引用**：按路径调阅原件（`paper/` 两本体，R-5/R-6）；0 复制正文段落；`paper/v2/outline_v2X.md` 虽在盘登记，⛔ 不作为本报告结构约束（0 大纲口径）[R-2][R-3]。

---

## §3 方法论：判死线制度

两主线的全部判定实践共享同一方法论底座。本章按制度要素分七节陈述：三态制度（§3.1）、判死线预冻结与生效即锁（§3.2）、根因三分类（§3.3）、双向外推禁令（§3.4）、软化禁令与如实呈报（§3.5）、假判定复核（§3.6）、指纹锚定与可核性（§3.7）。

### §3.1 三态制度：终态只出 PASS／FAIL／KD

**制度字面**（沿线索册 §4.1）：所有分支终点**只出 PASS / FAIL / KD**；⛔ 0「维持不明」、0「等 PI 拍板」、0「如实报区间」三类悬置态作为**终态**；⛔ 0 用 `UNVERIFIED`／`PARTIAL`／`GRAY`／「不明」／「未观察到」充当结论（「不明」按 PI 裁定＝**扩写后的 KD**，须并报）[R-2]。

**KD 的语义与实例**：KD＝kill-death「不可算」。项目内 KD 的两条典型落位：其一，判定所依赖的证伪/证真双不可得——P-C 族登记「0 真证伪 0 假证伪 ⇒ 不可算落 KD」[R-1][R-17]；其二，判定输入未到位的悬置——#21 族登记「维持 KD」[R-2 条目 4.17][R-18]。

**KD ≠ 未交付**：「未交付」是**未到终点的未出判定态**（修复件未出），不是三态终态。实例：C5 B 组修复登记「**未交付**（①修复件、②B3 重走件均未出）」，根因＝外部依赖硬阻塞（embedding API 配额 429）[R-2 条目 4.14][R-19]。本报告对两类状态严格区分：未交付 0 写成 KD，也 0 写成 PASS/FAIL；反之亦然。

**制度意义**：三态冻结使「悬置」不可能作为终态存在——判定链要么落于三态之一，要么如实登记为未到达终点（未交付）。这是全部判定可归档、可审计的前提；「终态无悬置」与「未出判定如实登记」共同构成判定的完备账面。

### §3.2 kill-line 先于实验冻结、生效即锁

**制度字面**（沿线索册 §4.1）：判死线（`K-*`／`TH-*`）**先于实验冻结、生效即锁、冻后 0 改、0 事后追加口径**；GT 判定链与任务 B 预登记链均留有时序实证 [R-2]。

**时序实证一（GT 判定链）**：立线件（判死线 v2，**kill-line 字面唯一源**）`results/_v5_gt5_gt6_gt8_gt5b_gt_prereg_2026_09_28.md`（`2505ff5d203f` · 63,447 B，文件名日期 2026-09-28）[R-9] → 执行棒报告（**执行≠判定**，0 出判定字面）`results/_v5_gt_exec_2026_09_29.md`（`9a679f43f796` · 27,701 B，2026-09-29）[R-10] → 正式判定收口件 `results/_v5_gt_verdict_2026_09_29.md`（`45648b0ec940` · 57,227 B，2026-09-29；逐案原判/v2 并列判/终态三列并报＋逐案裁根因＋逐案裁 kill-line＋双读法）[R-11]。三件的日期与内容分工构成「线在跑前、判在跑后」的盘上时序证据：判死线字面冻结于 09-28 立线件，执行（09-29）不出判定，判定（09-29）收口。

**时序实证二（任务 B 预登记链）**：预登记件（**任务 B v2.2 预登记**：claim 重定三指标——结构相似 ≥0.8＋分歧批判理由 100%＋盲从率 ≤0.1；**kill-line 先于实验冻结的范例面**）`results/_v4_pi_cot_v2_prereg.md`（`cc25c5149ce1` · 4,247 B）[R-12] → 预登记生效件（**生效即锁面**）`results/_v4_pi_cot_v2_prereg_activation_2026_09_23.md`（`00584e5a5c78` · 1,016 B，2026-09-23）[R-13] → 正式判定 `results/_v4_pi_cot_v2_verdict_v2.md`（`5d79e67a4e9d` · 33,723 B）[R-14]。预登记→生效→判定的三件链与 GT 链同构。

**阈值字面唯一源**：S 系预登记件 `results/_v3_s_prereg_v1_2026_09_27.md`（`ef5a40554960` · 46,836 B）为 `K-V3S-3-*`／`K-V3S-4-*` 阈值字面唯一源（跨日/单日占比协议锚），**横跨 V3 与 V4 两线**（V4 蒸馏采集协议的阈值出处）；登记 `K-V3S-3-1/2/3/4`＋`K-V3S-4-1/2/3`＋`TH-v2-*` 沿用表，⛔ 0 擅调任何切点 [R-2][R-8]。

**0 擅调阈值**：`TH-*`／`K-*`／切点全部沿盘上既有字面——0 新设、0 调整、0 以「更合理」为由替换 [R-2]。本报告写作层同步执行：凡引用阈值，只照录登记字面。

### §3.3 根因三分类

**制度**（沿线索册 §4.1）：根因三分类＝**真证伪／假证伪／混合／不明**；**每条判定必附根因列** [R-2]。

**实例**（终态与根因均按登记字面转引，逐案锚见右列）：

| 案 | 终态（登记字面） | 根因（登记字面） | 锚 |
|---|---|---|---|
| gt5 | FAIL（判死落定） | ③ 混合（构造面真证伪＋素材面 4/22 未覆盖全称＋载荷集中单图） | [R-1][R-11] |
| #35 v2 | FAIL（α、β 两腿成对 FAIL） | 假证伪 ×3（真证伪 0／混合 0／不明 0） | [R-1][R-16] |
| P-J／P-M | KD | 假证伪 | [R-1][R-17] |
| P-C | KD | 0 真证伪 0 假证伪 ⇒ 不可算落 KD | [R-1][R-17] |
| 任务 B v2 | FAIL | 复合定性 2 复合＋2 β（0 纯 α） | [R-1][R-14] |

根因列独立于终态列存在——判定说「结果是什么」，根因说「结果归属于谁（命题／工具／构造／混合）」。这一分离结构是外推禁令（§3.4）得以执行的前提：没有独立根因列，「验证失败」与「命题失败」就会混写。

### §3.4 双向外推禁令

**制度字面**（沿线索册 §4.1 与 H-F）：根因＝假证伪 ⇒ 「工具/构造失灵」⛔ 0 写成「命题已死」；同时「**构造面 PASS ⛔ 0 外推真实面**」的**对称禁令**同样生效；构造面 FAIL ⛔ 0 反推真实面；S3 面读数 ⛔ 0 外推为 S4 结论 [R-2]。

**GT 系本轮字面**（线索册自正式判定件 2.9 实读摘引）：「本轮构造面落 FAIL 处，0 由 FAIL 反推真实面命题的任何方向」[R-2]。

**落地到本报告的两条写作红线**：其一，任务 B v2/v3 的 FAIL 判定 0 外推为「思维链不可蒸馏」[R-1]；其二，GT 系构造面读数 0 外推真实面——PASS 方向与 FAIL 方向均禁 [R-2]。

**制度意义**：外推禁令把「某次验证的结论」与「命题本身的存亡」隔离——结论的可述范围由根因归属决定（工具/构造失灵不可上推为命题否定；构造面成立不可下推为真实面成立）。这是负结果「不误导」的核心机制。

### §3.5 软化禁令与如实呈报

**制度字面**（沿线索册 §4.1 与 H-E）：直书「α 腿被证伪」「β 腿被证伪」；根因列独立给出；⛔ 0 用「未观察到／证据不足／待进一步验证」类措辞；判定条目 ⛔ 0「但／然而／仍有希望／不排除／证据不足／待进一步验证／初步／大致」[R-2]。「**诚实的根因是不误导——机械诚实不合格**」[R-1][R-2]。

**分歧并报（0 消解）**：gt5 的主读法＋替代读法 A（分腿读法：读 gt5＝「一条存活＋一条判死」，非「整体被证伪」）＋替代读法 B（均值尺度读法：B 腿方向由单图决定、在均值帧下不稳健）**三者并列，分歧如实写明** [R-1][R-2]。

**如实呈报的两类「不好看」面**（本节为制度例证级预告；读数详情在 §5/§6 呈交）：其一，**达标路径与预估不同**——跨日指标达标，其达标来源非 R 系配对跨日（登记读数：D8 反转配对（≥1 天）**不符**，3/3 `actual_interval_days = 0`）；其二，**不可判面照写不可判**——纠正事件计数线三读差异 2↔7 ⇒ **不可判**（口径不唯一＋旧基线不可复现）。上述读数沿线索册 §4.2 行 4.11/4.12 登记值 [R-2]；其锚件 `_d8_closeout_protocol_recompute_2026_09_30.md`（册载 `57aba2cd26a6` · 31,007 B）系**已登记缺件**——团队核验底账查证：该件在仓内工作树、git 全史与镜像清单三面均无踪迹，判定为 PI 盘上 09-30 落盘但未推仓，论文引用前须 PI 补送原件，否则读数一律标「待PI补」[R-25]。本报告据此将其读数按登记值转引并标「待PI补」。

### §3.6 假判定复核：诚实纪律的制度化证据

**事件与复核面**：2026-09-28 取证「六案挂假」（假判定取证件＋会话日志＋v1.x 预登记三件），2026-09-30 执行六项复核（复核总账＋会话日志复验两件）。复核面五件登记（当轮指纹实测）：

| 件 | 路径 | SHA-12 | 字节 | 要点（沿线索册 §4.3 登记） |
|---|---|---|---|---|
| 取证件 | `results/_v5_fake_verdict_forensics_2026_09_28.md` | `1b135d8b1e08` | 35,870 | 假判定取证 [R-22] |
| 会话日志 | `results/_v5_fake_verdict_session_log_2026_09_28.md` | `132bfa0c02f5` | 18,877 | 假判定会话日志 [R-23] |
| v1.x 预登记 | `results/_v5_fake_verdict_v1x_prereg_2026_09_28.md` | `088085d6c90d` | 28,484 | 假判定 v1.x 预登记 [R-24] |
| 复核总账 | `results/_fake_verdict_reverify_sixitem_ledger_2026_09_30.md` | `41d7b76ea4d6` | 40,957 | 悬案 2 复核栏六项落位登记 [R-20] |
| 复核会话日志 | `results/_fake_verdict_session_log_reverify_2026_09_30.md` | `c14094bdf815` | 25,953 | 复核栏会话日志复验 [R-21] |

**关键读数**（线索册自 4.18 实读摘引、0 改写；本报告按登记值转引）[R-2]：六项全部照录落位（PI 裁示字面 0 改写）；动作层级由「判死」改登记为「已复原」；E-C 级拍板转述升格为可引（保留「派工单转述 E-C」原标注，不抹来源等级）；`2f34ce11b3b4` 回填实测 15 命中件 → 10 追加／5 跳过并登记。⚠️ 本棒新发现：v1.2 锚件「登记滞后」1 例（终局核验抓出，0 代裁）；对六项③采认 0 影响（§0 哈希表位于未变前缀内，前缀逐字节恒等 ⇒ 15/15 MATCH 不受追加影响）。⛔ 禁内建 `hash()`（须 `hashlib.sha256`）。

**制度意义（四点）**：其一，**判定可被推翻并留痕**——「已复原」是登记动作层级的变更，非静默消标；其二，**转述升格不抹来源等级**——E-C 级标注随转述保留，来源等级链不断裂；其三，**复核中发现的新问题照实登记**（登记滞后 1 例由终局核验抓出，0 代裁）；其四，**复核读数本身锚定指纹**（15 命中件回填实测）。假判定复核与三态制度互补：三态制度保证判定账面完备，复核制度保证账面错误可被显式修正。

**陈述边界**：本报告对六项复核的呈述以线索册摘引为载体；六项复核的原始字面在其锚件（上表五件，本 part 仅作当轮指纹实测、0 通读正文）。

### §3.7 指纹锚定与可核性

**引用三元组**：路径＋SHA-12（`sha256(全文字节)` 取前 12 位、小写）＋字节（落盘实测）[R-2 §0]。指纹口径纪律：与既有件内登记值不一致者，以盘上实测为准并显式标注 [R-2]。

**漂移登记制度**（沿线索册 §5）：既有件 **0 回改**（追加行模式）；0 代裁、仅登记差异。线索册 2026-10-01 实测登记的漂移实例（本节按登记值转引；漂移件本 part 未另行实测，属 part2 复核面）：`docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（登记 239,387 B／`849d76be3a06` → 线索册实测 857,551 B／`41f5f1689d09`）；`docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md`（三级漂移已登记后**第四次漂移** → 15,457 B／`423c84de20d5`）；三目录盘点件（登记 355,687 B／355,816 B → 实测 355,819 B／`df7e9cd39251`）[R-2]。

**H10 计数纪律**：三目录计数/圈定面/清单面各计数（MAIN 986／ARCHIVE 1,669／SUB 467；圈定 571 件；清单一 342 件；覆盖面 16 件；拟上传 358 件——**沿旧件登记值，现值待核**）；线索册对计数类 0 复算，归 PI 侧 V4 收尾整理统一校正 [R-2]。本报告 0 将任何上述计数引用为现值。

**当轮实测复算**：本报告各 part 写作轮开工先做该轮引用锚 `sha256`/`stat` 实测复算——引用一律采用当轮实测值，防素材漂移；底账已实测者以底账值为基准、当轮复算核对 [R-2 引用规范＋分件纪律]。本 part 25 件全等（登记表见件尾）。团队核验件同按「逐件实测 sha256[:12]＋字节；0 通读粘贴文本与敏感正文」惯例执行 [R-3][R-4]。

**可核性闭环**：正文引用 → `[R-n]` 编号 → 三元组 → 盘上原件 → 判定字面。全链在工作区内闭合；已发表件外部元数据为唯一例外（外部原文不在工作区 ⇒ 「待核」）。缺件类读数（如 §3.5 D8 收尾重算件）在该闭环中显式断链并标「待PI补」——断链可见本身即是可核性的一部分。

---

## 本 part 引用登记表（part1 · 当轮实测）

> 路径口径：相对 `〔本地路径已脱敏〕`；`repos/Deposon/_september_workspace/results/` 即素材登记口径的 `results/`（沿交叉面底账头注：`results/` 物理位置＝`_september_workspace/results/`，`paper/` 在仓库根）。全部 25 件于 2026-10-01 当轮 `sha256`/`stat` 实测，与底账登记值全等。

| 编号 | 路径（相对 〔本地路径已脱敏〕） | 实测 SHA-12 | 实测字节 | 引用位置（章） |
|---|---|---|---|---|
| R-1 | `upload/6abd3b9447b17fad6c25e25f__commission_glm_dualtrack_paper_v0-2_2026_10_01.md` | a17275086734 | 21,014 | 前置区／§1／§2／§3 |
| R-2 | `upload/6abd3a8c2cbacfe9dfb68258__dualtrack_paper_clue_book_v0-2_2026_10_01.md` | 998221ed5947 | 63,656 | 前置区／§1／§2／§3 |
| R-3 | `shared/爱丽丝_交叉面素材核验底账_2026-10-01.md` | 246b6923cefd | 10,277 | §1／§3 |
| R-4 | `shared/鲍勃_体例与沿革及V4-LLM资产核验底账_2026-10-01.md` | 22533dd80d50 | 17,311 | §3 |
| R-5 | `repos/Deposon/paper/deposon_paper_final_cn.md` | c5f6a23f4408 | 53,838 | §1 |
| R-6 | `repos/Deposon/paper/deposon_paper_final_en.md` | 2ec20b96e941 | 68,164 | §1 |
| R-7 | `repos/Deposon/_september_workspace/results/_naming_ruling_note_2026_09_29.md` | 57024f2cd30a | 7,843 | §2 |
| R-8 | `repos/Deposon/_september_workspace/results/_v3_s_prereg_v1_2026_09_27.md` | ef5a40554960 | 46,836 | §2／§3 |
| R-9 | `repos/Deposon/_september_workspace/results/_v5_gt5_gt6_gt8_gt5b_gt_prereg_2026_09_28.md` | 2505ff5d203f | 63,447 | §3 |
| R-10 | `repos/Deposon/_september_workspace/results/_v5_gt_exec_2026_09_29.md` | 9a679f43f796 | 27,701 | §3 |
| R-11 | `repos/Deposon/_september_workspace/results/_v5_gt_verdict_2026_09_29.md` | 45648b0ec940 | 57,227 | §1／§3 |
| R-12 | `repos/Deposon/_september_workspace/results/_v4_pi_cot_v2_prereg.md` | cc25c5149ce1 | 4,247 | §3 |
| R-13 | `repos/Deposon/_september_workspace/results/_v4_pi_cot_v2_prereg_activation_2026_09_23.md` | 00584e5a5c78 | 1,016 | §3 |
| R-14 | `repos/Deposon/_september_workspace/results/_v4_pi_cot_v2_verdict_v2.md` | 5d79e67a4e9d | 33,723 | §1／§2／§3 |
| R-15 | `repos/Deposon/_september_workspace/results/_v4_pi_cot_v3_verdict_v3.md` | bb44fdc7ab0f | 53,751 | §1 |
| R-16 | `repos/Deposon/_september_workspace/results/_v5_item35_v2_verdict_2026_09_29.md` | b59bef293712 | 26,232 | §1／§3 |
| R-17 | `repos/Deposon/_september_workspace/results/_v5_pjpm_pc_verdict_bang3_2026_09_29.md` | 1814f9590f0f | 41,566 | §1／§3 |
| R-18 | `repos/Deposon/_september_workspace/results/_v5_item21_verdict_2026_09_28.md` | de274bd38955 | 28,155 | §3 |
| R-19 | `repos/Deposon/_september_workspace/results/_v5_v3_deg_c5_b_halt_report_2026_09_29.md` | f2b68ee099b5 | 14,862 | §1／§3 |
| R-20 | `repos/Deposon/_september_workspace/results/_fake_verdict_reverify_sixitem_ledger_2026_09_30.md` | 41d7b76ea4d6 | 40,957 | §3 |
| R-21 | `repos/Deposon/_september_workspace/results/_fake_verdict_session_log_reverify_2026_09_30.md` | c14094bdf815 | 25,953 | §3 |
| R-22 | `repos/Deposon/_september_workspace/results/_v5_fake_verdict_forensics_2026_09_28.md` | 1b135d8b1e08 | 35,870 | §3 |
| R-23 | `repos/Deposon/_september_workspace/results/_v5_fake_verdict_session_log_2026_09_28.md` | 132bfa0c02f5 | 18,877 | §3 |
| R-24 | `repos/Deposon/_september_workspace/results/_v5_fake_verdict_v1x_prereg_2026_09_28.md` | 088085d6c90d | 28,484 | §3 |
| R-25 | `shared/鲍勃_V4主线素材核验底账_2026-10-01.md` | b78dbf0266e8 | 44,280 | §3.5（D8 缺件状态定向查证） |

---

## part1 自检与纪律执行声明

1. **三标注 0 变体**：全文标注仅用「待PI补」「待核」「以PI为准」三种字面（出现于前置区体例说明、§1.1、§2.1、§3.5、§3.7 与本声明）。H10 句式「沿旧件登记值，现值待核」用于 §3.7 三目录计数行（归「待核」族）。源件内的其他字面（如「待 PI 复核」「待 PI 审发」）均置于引号内作为源件原文转引，不作本报告标注使用。
2. **判定字面 0 软化 0 外推**：摘要与正文中的全部终态、根因与读数按登记值逐字转引（gt5 FAIL／#35 v2 FAIL／P 族 KD／任务 B v2·v3 FAIL 及数值读数等）；判定句无「但／然而／仍有希望／不排除／证据不足／待进一步验证／初步／大致」；任务 B FAIL 未外推为「思维链不可蒸馏」，GT 构造面读数未外推真实面。
3. **0 空节**：前置区（题名块／中英摘要／标注体例说明）、§1（四小节）、§2（四小节）、§3（七小节）均成节成文，无占位空节。
4. **引用锚当轮实测**：25 件逐件 `sha256[:12]`＋字节实测复算，与底账登记值全等（登记表已列）；0 引用未实测件（D8 收尾重算件缺件，其读数仅按线索册登记值转引并标「待PI补」，不以缺件为锚出具读数）。
5. **0 覆写**：落盘前实测撞名（目标名在 `shared/` 不存在），本件为新建件；写作全程对全部引用件只读。
6. **精读范围**：按派单执行——委托书总纲复阅；线索册 §0/§4.1/§4.3/§6＋卷首主线帧＋条目 2.35/2.44/2.80 精读；鲍勃体例底账①精读；交叉面底账 §3 精读。摘要与 §1/§3 所用判定读数载体为委托书 §4 摘要视图与线索册关键读数（骨架件 §2.1 已登记的摘要级素材面）；判定件本体仅作当轮指纹实测、0 通读正文（复核入口以登记表三元组给出）。§3.5 为核 D8 件状态对鲍勃 V4 底账作两行定向查证（缺件登记与引用注意事项），非 V4 主线判定素材使用；爱丽丝 V3 底账未使用。
7. **隐私与敏感面**：0 贴 dataset 内部字段、0 贴推理全文、0 复制已发表件正文段落；引用一律路径＋SHA-12＋字节三元组。
8. **AI 参与**：本 part 由 GLM 侧起草（model/版本「以PI为准」）；起草过程 0 联网、0 调外部 API、0 读密钥、0 跑实验；本轮写作遇环境 502 多次，均按分件纪律自行重试完成（0 中止）。

---

**出件**：查理-论文主笔（GLM 侧 · deposon 论文终稿起草线）｜2026-10-01
**下一分件（待管理员派发）**：part2＝§4 V3 博弈论主线（4.1–4.8，预计 40–50 KB）
