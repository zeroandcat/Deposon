# 查理 · FTFB R6 改稿单（2026-10-20 · 体裁重构执行件 · F01–F17 锚串）

- **任务来源**：群管理员 2026-10-20 18:15:42 派单【R6 执行轮·起草】→ 18:47:25 **重派收窄**【R6 执行轮·重派收窄】：查理与鲍勃并行件均撞执行窗超时，本轮只交本改稿单一件；tex 落稿与底账追加顺延至本单落地后的下一轮（本单为纯综合件，素材已在手）。**执行依据**：PI 17:55:25 拍板「R6 合并单全按建议且暂无额外的诗」（底账 P15）——合并单四组 19 项全按建议：甲 R6-A1~A6／乙 K-1'~K-5／丙 V5 P0–P3＋V-8／丁 M-1~M-4；K-1' 可选注记句按默认弃用（诗面零增补），0 诗引文／0 来源箭头／0 epigraph／0 署名照旧。
- **件性质**：R6 起草的**改稿登记层**；收窄口径下**本单为本轮唯一交付物**——tex 落稿（脚本＋新 tex＋diff＋自检三件套）与底账追加均顺延至下一轮。撞窗轮在 `shared/查理_FTFB_R6重构稿_2026/` 留有半成品（tex／diff／selfcheck 两件／`apply_r6_final.py`，18:42–18:45 时戳），**非交付物**：其 tex 已于本轮按本单 §三 17 对锚串完成正反向回放复验（§九——与 R5 的差异恰为本单 17 对替换、字节恒等），下一轮可直接复验采用或重跑覆盖；脚本解析约定与本单 §〇.5 一致，可原样重跑。
- **纪律声明**：R5 tex `ba2f157196f5`（123,129 B·666 行）只读基准（sha256 前 12 位断言，落稿轮零触碰）；一切仓内/shared 既有文件除本件与落稿目录外零写零改；建议非裁，拍板权归 PI。
- **输入件（只读实读）**：R5 tex（`ba2f157196f5`）；R6 重构方案（`f0642233391c`）；爱丽丝 A 轨 v2（`81756c55a107`，K-2/K-3/K-5 措辞逐字取用）；阿兰体裁对标件（G-1~G-12 验收清单，题录纠错值以其为准）；持久化记忆底账（P01–P17，本日活件）。

---

## 〇、锚串纪律与总则

1. **编号沿承**：沿 R5 改稿单 E01–E39 锚串先例，新起 **F 系编号 F01–F17**（17 对 old/new 锚串对），R5 件 E 系编号封存不复用。
2. **落稿方式**：脚本化单轮执行（沿 `apply_r5_final.py` 先例）——顺序应用 F01→F17，逐条断言当前文本锚串恰命中 1 次；应用后反向回放（F17→F01 逐条 new→old）必须还原出与 R5 字节恒等的文本，构成「无失配·无多写」的形式证明。
3. **增句位纪律**：本轮 17 对中 11 对为**纯插入位**（old 句逐字保留于 new 内、其后或其前插入新文本），6 对为**句子级重写位**（F01 摘要首两换三句／F02 §1.1 前三句／F05 换一词／F11 题／F12 句尾扩展／F17 注记行）。所有重写位的 old 文本在 pairs log 全文登记，逐字可核。
4. **硬约束**（落稿自检＋鲍勃差量验收双把关）：**池 66 零漂移**（References 区块字节恒等＋正文 [Rxx] 引用实例零增减——本轮 0 新增引用）；**引用冻结 a57d7fe 维持**；**匿名面**（[R56]/[R57] 声明式形态零动、0 新增去匿名化指针、新文本 0 处「KIMI/onewithdream/与死同行」字面）；**no prediction**（C-2 五类禁用形自检，§五）；**语域三层级配**（§四）；**数字字面零漂移**（实验数字全在保留区，反向回放证明＋新文本数字清点）。
5. **fence 块解析口径**（落稿轮机器解析规则，本轮 §九已实机复核）：§三 tex fence 块按**行收集、以 \n 连接**，fence 收束行不入内容——即 old/new 均不含 fence 末行后的换行；两候选注记、登记注文字不入锚串。撞窗轮残留 `apply_r6_final.py` 的 `parse_pairs` 即此约定，可原样重跑。

---

## 一、重写项总表（F01–F17）

| # | 落位 | 类型 | 验收对接 | 依据 |
|---|---|---|---|---|
| F01 | 摘要首段 | 问题化开篇＋we-argue-that 主张句＋position paper 自报清除＋objection 句 | G-1/G-2 | R6-A5＝M-3 |
| F02 | §1.1 首段 | 哲学问题化开篇（P-S1 资产升级保留）＋主张句前置首段 | G-2 | 方案 §1.2 行 §1 |
| F03 | §1.2 三检 itemize 后 | 三检概念语法段插入（T＝出格时序／R＝应之残留／D＋供应层豁免＝不必判据——论文自有装置语重述） | G-3/G-8 | 方案 §1.3＋A 轨 v2 §3.4-3 承接面 |
| F04 | §1.2 F-C 前导句后 | 判死线＝第一动作开篇锚（判断先于事实写下去的升读句） | G-9 | 方案 §1.2 行 §1（段一账面锚） |
| F05 | §1.3(i) | position paper 自报清除（a position paper→an argument） | G-1 | 阿兰 G-1 |
| F06 | §2.3 渠道 I 收束段前 | objection–reply 甲（单案＋可 dispensability） | G-4 | 方案 §1.2 行 §2–§5 |
| F07 | §3.4 渠道 II 收束段前 | objection–reply 乙（崩塌异议：Norton 强形式） | G-4 | 同上（§3.1 Brown–Norton 语域基准样） |
| F08 | §4 渠道 III 收束段前 | objection–reply 丙（优先性异议：物理量在先） | G-4 | 同上 |
| F09 | §5 渠道 IV 收束段前 | objection–reply 丁（可替代异议：反事实） | G-4 | 同上 |
| F10 | §6 节首（§6.1 前） | 判据概念前置段（方法论哲学化：判据装置＝内核语法的方法论形态） | G-3/G-8 | 方案 §1.2 行 §6 |
| F11 | §7.2 题行 L399 | 题式转位（候选甲落稿；候选乙登记候裁——候阿兰标尺＋爱丽丝语义校验） | G-9 | R6-A3＋17:26 降格令 |
| F12 | §7.2 首句 | 首句桥接（point→first action＋floor/保底；题面 Death −1、正文 kill 字面 0 增减） | G-9 | R6-A3 |
| F13 | §8.4 para2 首句 | KIMI 同源句升级（R6-A6 默认：AI-agent 描述式不点名） | G-10 | 17:20 裁定（P10） |
| F14 | §8.4 para2 尾 | K-2「不必」系家族原则半句（**逐字**取 A 轨 v2 §四原文） | G-8 | 乙组 K-2 |
| F15 | §8.4 para4 | K-3 回路方向性/极位补句（**逐字**取 A 轨 v2 §四原文） | G-8 | 乙组 K-3 |
| F16 | §9 收束段后 | K-5 三段位声明句新末段（**逐字**取 A 轨 v2 §四原文——三段位唯一显式表述） | G-8/G-12 | 乙组 K-5 |
| F17 | 前导注记行 | M-1 版本沿革注记（R3→R4→R5 挂起→R6，LaTeX 注释层，0 版面影响） | —— | 丁组 M-1 |

---

## 二、重写位与保留位的分账（资产句逐字保留项登记）

### 2.1 重写位（6 处——old 全文入 pairs log，逐字可核）

| # | old 起止 | 重写性质 |
|---|---|---|
| F01 | 摘要第 1–2 句（「Fiction is not evidence…anchored in cases:」） | 换 3 句：问题句＋we-argue-that 主张句＋objection 纪律句；「This position paper makes that sentence operational. It separates」清除 |
| F02 | §1.1 第 1–3 句（「Fiction, in the standard account…entry to fail.」） | 换哲学问题化段（P-S1 三动词资产保留：decorates/motivates/supplies）；第 4 句「Treated this way…」为资产句逐字保留（不在锚串内） |
| F05 | §1.3(i) 首词组（「This is a position paper with」） | 换「This is an argument with」，其余逐字 |
| F11 | §7.2 题行（「Death is the point」） | 换概念式题（候选甲）；装置句全保留 |
| F12 | §7.2 首句（「The three falsifications…failure of it.」） | 句尾扩展 first action＋floor 从句；原句主干逐字 |
| F17 | 前导注记行（「% arXiv preprint edition: named author block and submission info line」） | 追加版本沿革注释行 |

### 2.2 资产句逐字保留项（零触碰清单——鲍勃差量验收对照）

1. §1.2 主张句（italic thesis 全句）及三 delimitations 段——逐字；
2. §1.2 F-C1~F-C4 条目正文与 Operational reading 全部——逐字；
3. §1.2 三检定义 itemize（T/D/R 三条）——逐字；
4. §1.2 D 词典段、双层证据段、分类原则段、四形之「不在科学中的方式」段——逐字；
5. 四渠道 Channel claim 四句（L164/L200/L228/L268）——逐字；
6. 四渠道 T/D/R 评分 itemize 全部（含 Partial pass/Unresolved 分级字面）——逐字；
7. 四渠道收束段四条（「The asymmetry in the scores…」「The channel passes T and R…」「The channel holds T at the arrow level…」「Channel IV is also where the loop stops…」）——逐字（objection–reply 为其**前插**，不触碰）；
8. §6.1 体裁判据引文段（Steele 定义＋两 guardrails＋[R36]/[R37] 锚句）——逐字；
9. §6.2 判据映射表＋表前导语句——逐字（表格不动）；
10. §6.3 双文献对望段、§6.4 pipeline 四阶段 itemize＋M5 纪律句——逐字；
11. §7 全链重放（§7.1–7.2 装置句含「M5 requires that the kill line be defined before the run; the run then killed.」、§7.3–7.4）——逐字；
12. §8.1–8.3 全部（含 Declaration sentence、四条件正结果句）——逐字；
13. §8.4 para1（家族先例段）、para3（物心方向在版句）、para5（不对称段）——逐字；para2/para4 原句逐字保留、增句为前插/尾接（K-2 为尾接 dash 形）；
14. §9 三件（master table／limitations／what-would-weaken）＋ Three dialogue partners 收束段——逐字（K-5 为其**后**新末段）；
15. AI use disclosure 节、Appendix 池验证与可用性条款——逐字（装置级不动）；
16. References 池 66 全区（[R01]–[R66] 逐条）——逐字（引用冻结 a57d7fe）；
17. 摘要中段（「non-Euclidean geometry as formal language…provisional (§7.4).」）——逐字；
18. 前导区引擎兼容层、unicode 映射表、版式参数——逐字（F17 仅注释行追加）。

---

## 三、锚串对（F01–F17 · 供 apply_r6_final.py 逐字解析）

> 解析口径同 R5 先例：每项首 ```tex 块＝锚串 old，次 ```tex 块＝拟落文本 new。

### F01 · 摘要重写（R6-A5＝M-3）

旧（锚串）：

```tex
Fiction is not evidence, but it is a recurrent, checkable input to the exact sciences: four channels — formal, controlled, quantitative, narrative — separate under three checks (temporal priority, dispensability of the fictional input, operative residue), and whether machine worldviews open the reverse channel stands or falls on the same falsifiability criteria we specify. This position paper makes that sentence operational. It separates the four channels, each anchored in cases:
```

新（拟落文本）：

```tex
When may fiction count as an input to the exact sciences, rather than as their contrast case? We argue that fiction is not evidence but a recurrent, checkable input: four channels — formal, controlled, quantitative, narrative — separate under three checks (temporal priority, dispensability of the fictional input, operative residue), and whether machine worldviews open the reverse channel stands or falls on the same falsifiability criteria we specify. Each channel is stated against its strongest available objection and answered on the record, concessions included. The argument separates the four channels, each anchored in cases:
```

### F02 · §1.1 哲学问题化开篇＋主张句前置（G-2）

旧（锚串）：

```tex
Fiction, in the standard account of the exact sciences, is what the exact sciences are not: it decorates the work, motivates it, and supplies the contrast against which rigor is defined. This paper takes a narrower and more mechanical view. We ask when a piece of fiction — a formal system built with no intended referent, a thought experiment, a quantity defined over an abstract ensemble, a story — can be shown to have entered the exact sciences as a working input; and, symmetrically, what it would take for such an entry to fail.
```

新（拟落文本）：

```tex
The standard account of the exact sciences assigns fiction a contrast role: it decorates the work, motivates it, and supplies the other side of the line that rigor draws. The assignment raises a question the standard account does not ask — when, if ever, may a piece of fiction count as a working input to those sciences, rather than as their ornament or their evidence? We argue that the question has a disciplined answer: fiction can be such an input, and the conditions under which it is one are statable, datable, and checkable. The conditions are mechanical rather than solemn: a piece of fiction — a formal system built with no intended referent, a thought experiment, a quantity defined over an abstract ensemble, a story — is asked not for depth but for a dated, checkable crossing: it counts as an input when its entry can be shown, and the claim fails when the entry cannot — the question of failure is asked with the question of entry, symmetrically.
```

### F03 · §1.2 三检概念语法段（插入位——D 词典段前）

旧（锚串）：

```tex
The D check returns one of four dispositions, and the dictionary is stated once here so that every later table reads against it.
```

新（拟落文本）：

```tex
Read as a grammar rather than a scorecard, the three checks are one discipline stated in three tenses. T is the tense of the crossing: an input that enters breaks a prior order of what counted as scientific material, and what the record carries is the timing of that crossing — not the fiction's standing, but its date. R is the tense of the response: the crossing is answered by the receiving discipline, and the record carries what the answer settles — the residue left in use — rather than the crossing that prompted it. D is the tense of no-necessity: the checks score an arrival, never a uniqueness, and where the pool carries no evidence either way the paper records the indeterminacy instead of spending it — no silence is converted into a necessity thesis on one side or a dismissal on the other. The order is not decorative: first the dated crossing, then the settled residue, and the no-necessity discipline holding throughout — the order in which the channels of §2–§5 are scored, the order in which the reverse channel of §8 would have to die.

The D check returns one of four dispositions, and the dictionary is stated once here so that every later table reads against it.
```

### F04 · §1.2 F-C 第一动作升读句

旧（锚串）：

```tex
The claim is falsifiable in four specified ways.
```

新（拟落文本）：

```tex
The claim is falsifiable in four specified ways, and the order is deliberate: the conditions are fixed before the facts are in — the paper's first action, not its last resort — the same order the pipeline of §6 demands of any claim it adjudicates, applied first to this paper's own thesis.
```

### F05 · §1.3(i) position paper 自报清除（G-1）

旧（锚串）：

```tex
(i) This is a position paper with an intellectual-historical core; its historical sections are case studies, not a systematic history.
```

新（拟落文本）：

```tex
(i) This is an argument with an intellectual-historical core; its historical sections are case studies, not a systematic history.
```

### F06 · 渠道 I objection–reply（单案＋可替代）

旧（锚串）：

```tex
The asymmetry in the scores is informative rather than embarrassing.
```

新（拟落文本）：

```tex
\textbf{Objection (one case, dispensable).} The channel rests on a single flagship case, and the scholarship it cites cuts against its necessity: the non-Euclidean style was one presentation among available alternatives, adopted for reasons that include notation and pedagogy. A category named for one dispensable episode has not earned a place in a four-way typology; what the channel calls supply, the objection calls convenience, and convenience is not a channel.

\textbf{Reply.} Both halves of the objection are granted, and neither touches the claim as worded. That the case count is one is priced in advance: F-C1 makes pairwise separability the typology's own falsifiability condition, so the objection, read as a prediction about further formal cases, names exactly the condition the paper has recorded as falsifiable — if a second formal case cannot be found that separates under the checks, the typology weakens, and the paper's books are open on that line. That the style was dispensable attacks a necessity claim the channel never makes: ``language prior to reference'' is a supply-level claim, and the downgrade is the D check doing its work, not the channel failing it. What the objection leaves untouched is the residue — the language became and remained the standard medium of the theory — and that, not necessity, is what the channel claims.

The asymmetry in the scores is informative rather than embarrassing.
```

### F07 · 渠道 II objection–reply（崩塌异议）

旧（锚串）：

```tex
The channel passes T and R, with D unresolved by design.
```

新（拟落文本）：

```tex
\textbf{Objection (the collapse objection).} If the deflationary reading of thought experiments is right — every thought experiment an argument in disguise, the imagery doing no work — then this channel's subject is empty: nothing fictional ever enters, ``controlled fiction'' is a flattering name for argumentation, and the channel's invariance under the dispute is not a virtue but a confession that its question was never about fiction.

\textbf{Reply.} The conditional is granted; the conclusion is not. Under the argument-only resolution the channel's residue is the translated argument itself — which still passes R — and the translation is the finding, not the loss: what the live dispute decides is where the fiction's work is done, and the criterion was chosen, precisely, so that the channel's claim survives either answer. The channel does not claim that imagery produces knowledge; it claims that the scenario is routine production material under a criterion both disputants grant. What the objection establishes is that one reading of the channel is thinner than the other, and the channel's wording already reflects it: the claim is stated at the tier the thinner reading still supports.

The channel passes T and R, with D unresolved by design.
```

### F08 · 渠道 III objection–reply（优先性异议）

旧（锚串）：

```tex
The channel holds T at the arrow level with the channel-level priority downgraded;
```

新（拟落文本）：

```tex
\textbf{Objection (the priority objection).} Statistical mechanics gave entropy a statistical reading over microstates some seventy years before the definitional act this channel credits: the physical quantity is prior, the abstract definition late, and by the channel's own temporal standard the story runs backwards — the ``feedback'' is an artifact of telling it from the abstract end.

\textbf{Reply.} The priority the objection establishes is real, and the channel has already paid it: the channel-level demand does not survive the chronology, the assessment downgrades channel-level T, and the claim sentence itself disclaims priority of the abstract over the physical. What the objection does not touch is the arrow-level record — the dated isomorphism, the dated entry into engineering, the dated rematerialization at a measured price per erased bit. The objection re-prices the channel; it does not close it: the arrows the channel claims are the arrows that survive.

The channel holds T at the arrow level with the channel-level priority downgraded;
```

### F09 · 渠道 IV objection–reply（可替代异议）

旧（锚串）：

```tex
Channel IV is also where the loop stops being purely historical:
```

新（拟落文本）：

```tex
\textbf{Objection (the substitutes objection).} Vocabulary is the most substitutable of inputs: coin another word, borrow another story. The precedences are dated, but dating a precedence is not crediting a contribution — the same terms would have been coined, the same agendas set, and ``supply'' is a name for what would have happened anyway.

\textbf{Reply.} The objection is a counterfactual, and by this paper's discipline a counterfactual is decided by evidence or held open. No study in the pool decides it, so D is recorded as indeterminate — the channel does not claim the vocabulary was needed, only that it was supplied and left a residue, and each precedence carries its anchor type. What would refute the channel is not the objection as stated but its evidential form: a study showing full substitutability with no residue lost, which would downgrade the channel through F-C2's route — a route the paper has left open on purpose.

Channel IV is also where the loop stops being purely historical:
```

### F10 · §6 判据概念前置段

旧（锚串）：

```tex
\subsection{The criteria, taken from the genre's own definitions}
```

新（拟落文本）：

```tex
This section states a method, and the method has a conceptual shape worth stating before its tables. The three checks of §1.2 are one discipline in three tenses — a dated crossing, a settled residue, and no necessity claimed — and this section asks what that discipline becomes when the timing of judgment is reversed: not fiction entering science under a verdict the record renders after the fact, but claims about machine intelligence made to stand before a verdict fixed in advance of the run. The mapping below is that reversal made concrete: its rows pair the genre's self-policing vocabulary with the falsifiability vocabulary of AI claim adjudication, and the pairing is a structural claim, not a resemblance — each row shares a failure mode across its two ends, and the sharing is checkable row by row. A criterion travels exactly when the failure it catches travels; that is the sense in which the criteria below are portable, and the sense a reader is invited to check. One row is an import rather than a construction, and it is declared where it occurs; the mapping's candor about its own sources is part of the method it carries.

\subsection{The criteria, taken from the genre's own definitions}
```

### F11 · §7.2 题式转位（R6-A3）

旧（锚串）：

```tex
\subsection{Death is the point}
```

新（拟落文本）：

```tex
\subsection{The first action: verdicts before the runs}
```

**候选乙（登记不入稿）**：`\subsection{Death as the baseline}`——保底式题面（Death 保留、point 降格）。甲乙两式候阿兰标尺（G-9 概念式／问题式核）＋爱丽丝语义校验（第一动作/保底语义位），PI 拍板后如换乙式为单行替换、落稿轮重跑脚本即得。

### F12 · §7.2 首句桥接（转位句）

旧（锚串）：

```tex
The three falsifications are the pipeline working as designed, not a failure of it.
```

新（拟落文本）：

```tex
The three falsifications are the pipeline working as designed, not a failure of it: the verdict is the pipeline's first action, its floor rather than its point.
```

### F13 · §8.4 KIMI 同源句（R6-A6 默认：AI-agent 描述式不点名）

旧（锚串）：

```tex
Both issue from the same dialogue-driven research practice — author-directed, AI-assisted, as stated in the paper's AI use disclosure — and the lineage is declared on that basis.
```

新（拟落文本）：

```tex
Both issue from the same dialogue-driven research practice — author-directed, AI-assisted, as stated in the paper's AI use disclosure — and the lineage is declared on that basis: within that practice, the loop proposition was first articulated as the understanding of the AI agent that completed the line's first public work.
```

### F14 · §8.4 K-2（para2 尾——逐字取 A 轨 v2 §四原文）

旧（锚串）：

```tex
A shared origin is not a shared verdict: neither work is evidence for the other.
```

新（拟落文本）：

```tex
A shared origin is not a shared verdict: neither work is evidence for the other — a precedent whose order (imagined first, formalized second, taken up by physics only last) also fixes the family's scale of standing: earned at the formalization step, not borrowed from adoption; a scale the line's further members extend, each in its own register.
```

登记注：K-2 措辞逐字（dash 尾接形：old 句号→em-dash 承接）；「a precedent」先行词＝para1 非欧先例（「on the precedent of the non-Euclidean case」），语义校验位归爱丽丝。

### F15 · §8.4 K-3（para4——逐字取 A 轨 v2 §四原文）

旧（锚串）：

```tex
a mind--matter formulation is named as direction, nothing more.
```

新（拟落文本）：

```tex
a mind--matter formulation is named as direction, nothing more. The two-way form the family shares is a cycle rather than a symmetry: the bounds crossed are inherited — precipitated, on the precedent's record, from the answers to earlier crossings — and each crossing is answered in turn, settling into the next bounds. The crossing initiates; the answer settles; and the settlement, not the crossing, is what the record can check.
```

登记注：K-3 两句逐字插于 para4「nothing more.」与「What this paper adds to the family…」之间——「settlement, not the crossing, is what the record can check」直接衔接后句 adjudication agenda，语义位按 A 轨 v2 设计。

### F16 · §9 K-5（收束段后新末段——逐字取 A 轨 v2 §四原文）

旧（锚串）：

```tex
Between the partners, the position is not a synthesis but a boundary: the paper claims the space its instruments can defend, and no more.
```

新（拟落文本）：

```tex
Between the partners, the position is not a synthesis but a boundary: the paper claims the space its instruments can defend, and no more.

The line this paper belongs to ascends in three stations: a practice that carries its own kill verdicts, carried to term in the line's first public work; a loop between worldbuilding and machine cognition, declared in the companion and run here as apparatus; and a mind–matter formulation now in preparation. The stations do not replace one another — the verdict line is the first action at every station, held rather than discarded — and the third station's direction is offered on the same terms as the first: no exemption, no privilege.
```

登记注：K-5 两句逐字（含 unicode en-dash「mind–matter」——与 R5 tex 正文 unicode 破折号族一致，0 格式适配）；三段位唯一显式表述，「the line's first public work」与 F13 同源句互指闭合。

### F17 · 前导版本沿革注记（M-1）

旧（锚串）：

```tex
% arXiv preprint edition: named author block and submission info line
```

新（拟落文本）：

```tex
% arXiv preprint edition: named author block and submission info line
% Version lineage: R3 (2026-09-18) -> R4 (2026-09-27) -> R5 (2026-10-20, submission suspended) -> R6 (2026-10-20, philosophical-register restructure)
```

登记注：LaTeX 注释层（0 版面影响、0 编译产物差异）；M-2（Comments AI 标注语不加）与 M-4（R5 提交件挂起已裁）均无 tex 侧动作，随 metadata 打包轮由戴夫执行。

---

## 四、语域三层级配（申报值）

| 层级 | 本轮承载 | 自检判据 |
|---|---|---|
| 概念分析主导层 | F02（问题化开篇）／F03（三检语法段）／F04（第一动作升读）／F10（判据前置段） | 关键术语首用即定义沿承（input／check／channel 均在 §1.1–1.2 既有定义位）；负载词双读（necessity 强弱读在 F03/F06/F09 显式分流） |
| 论证推进层 | F01（摘要主张句）／F06–F09（四 objection–reply）／F12（转位句） | 论证动词在场（argue/grant/answer/price）；让步条款在场（F06「Both halves…granted」／F07「The conditional is granted」／F08「The priority…is real」／F09「decided by evidence or held open」） |
| 装置从属层 | 一切既有表格、T/D/R 计分、锚链、池、附录——零动 | 反向回放字节恒等证明（§〇.2） |

**G-6 负面清单自检**：新文本 0 修辞性排比／0 感叹／0 升华式结尾（K-5 收束以「no exemption, no privilege」自限式收，非颂扬式）；0 营销形容词（groundbreaking/revolutionary 类词表扫 0 命中）；hedging 在场（「if ever」「may count」「rather than」族）。

---

## 五、C-2 五类禁用形自检（no prediction 纪律）

| 禁用形 | 新文本命中 | 说明 |
|---|---|---|
| ①完成态暗示范式已在（「has been generalized into」族） | 0 | K-5 站三＝「now in preparation」（在制进行态，非完成态）；§8.4 para3 在版句「is being extended, by declaration」零动 |
| ②SPEC 内容前置（未来作内容细节入文） | 0 | K-5 站三仅命名方向，0 内容；V5 六要件不入论文 |
| ③预言之诺（「will show／is expected to succeed」族） | 0 | 第三站 standing 表述＝「offered on the same terms as the first: no exemption, no privilege」（自限式） |
| ④承继表述（「inherits this paper's apparatus」族） | 0 | K-5 明写「no exemption, no privilege」——反承继式；F10「the mapping's candor about its own sources」不构成承继保证 |
| ⑤同源＝证据（「两作同源故互证」族） | 0 | F14 保留句「A shared origin is not a shared verdict」即 C-2 该行之允许形本体；F13 新增句仅登记溯源事实（「first articulated as the understanding of…」），不引出证据主张 |

---

## 六、G-1~G-12 验收映射（阿兰对标件为验收清单）

| # | 检查项 | 本单落点 | 预期值／登记 |
|---|---|---|---|
| G-1 | position paper 自报清除 | F01＋F05 | 全文 `position paper` 命中＝1 处（L437 「a position paper makes world models the core component」——LeCun [R22] 第三方描述语，非自报，登记豁免）；`position statement`（companion 描述）4 处零动（L461/L518/L524/L648，实测基线 4——§九复核，订正撞窗草稿笔误「5 处」） |
| G-2 | 主张句前置 | F01＋F02 | §1 首段含单句 we-argue-that（F02「We argue that the question has a disciplined answer…」）；摘要同构（F01） |
| G-3 | 论证显式化 | F03/F04/F10＋四渠道 obj–reply | T/D/R、M1–M5、锚池以论证层身份保留（数字字面 0 触——反向回放证明） |
| G-4 | 异议—回应配额 | F06–F09 | 4 组强形式 objection＋显式 reply（各含让步条款）——「各节散布」型；与 §9.3 自我弱点披露并存成内外两环；objection 词族新计 4+1（摘要句） |
| G-5 | 区分纪律 | F03 | 负载词双读（necessity 强/弱读、standing 借来/挣得）在新增段显式；术语首用定义位零动 |
| G-6 | 作文感负面清单 | §四自检 | 0 命中（机扫＋人读） |
| G-7 | 章节惯例 | —— | 编号节、roadmap、结论不引新证（K-5 为谱系声明非新证）——结构零动 |
| G-8 | 诗面＝结构核心非来源 | F03＋F10＋K-2/K-3/K-5＋0 增补 | 章节架构可指认三检深层语法（T＝出格时序／R＝应之残留／D＋供应层豁免＝不必判据——F03 论文化重述＋F10 方法论形态）；全文 0 诗行引文／0 epigraph／0 来源箭头（inspired by／originates in／traces back to／the source of 词族机扫 0 命中）；K-1' 可选句弃用（P15「暂无额外的诗」） |
| G-9 | 判死线降格 | F11＋F12 | 题面换型概念式（Death 出题面）；词频申报：题面 Death −1；正文 kill 族字面净 +1（K-5「kill verdicts」逐字携带，非我方新增）；「point」题式废除、F12 以「floor rather than its point」显式转位；12 装置级＋2 声明级判死线句全保留 |
| G-10 | 引用与匿名兼容 | F13＋引用冻结 | [R56]/[R57] 声明式零动；KIMI 以「the AI agent that completed the line's first public work」描述式不点名；0 新增去匿名化指针（新文本 0 处 KIMI 字面） |
| G-11 | R5 资产兼容 | §二.2 零触碰清单 | 池 66／数字字面／T/D/R／可核查性身份零漂移——反向回放字节恒等＋References 区块恒等断言 |
| G-12 | 形态与篇幅 | —— | scoped conclusion（§9 收束段在版句逐字保留）＋K-5 新末段自限式收束；页数候戴夫实测申报（预计 29→30±2） |

---

## 七、候裁与联动登记（非本单执行项）

1. **题式候选乙**（F11 注记）——候阿兰标尺＋爱丽丝语义校验，PI 拍板后单行替换重跑即得。
2. **L518 披露节联动**（F13 注记）：AI use disclosure 现文「Two same-line works are declared in §8.4」——F13 新增句属谱系层登记（非同线著作申报数），默认披露节不动（装置级不动纪律）；是否补携带半句候爱丽丝语义校验裁，默认不加。
3. **V5 侧**（丙组 P0–P3＋V-8）：不入本单（论文侧 0 动作），V5 计划二稿触发条件已闭合。
4. **R5 tex 基准**：`ba2f157196f5` 全程只读；R5 提交包 `8759e4b9022c` 挂起不传（M-4 已裁）。

---

## 八、落稿与自检方案（顺延至本单落地后的下一轮执行）

1. **脚本**：`apply_r6_final.py`（撞窗轮残留版在 `shared/查理_FTFB_R6重构稿_2026/`，解析约定与本单 §〇.5 一致、本轮 §九已按其口径复核，可原样重跑；或以本单 §三重建）——解析本单 17 对锚串（0 手抄），单轮顺序应用＋逐条 count==1 断言＋反向回放反证＋全套自检（池 66 九处联动／引用区块字节恒等／匿名面扫／来源箭头词族／C-2 禁用形／G-1 与 G-4 词族／kill 族词频账／数字字面）。
2. **自检三件套**：`R5_to_R6_unified_diff.txt`（hunk 编号与映射表）＋`selfcheck_pairs_log.json`（17 对全文机器可核）＋`查理_FTFB_R6落稿自检记录_2026_10_20.md`（人读）——撞窗轮三件为残留态（§九已复验与残留 tex 自洽），下一轮重跑刷新后交付；**底账追加（P18 起）同轮执行**。
3. **验收交接**：爱丽丝语义校验（F03 语法映射一致性／F13 同源句措辞／K-2 先行词位／题式甲乙）→阿兰体裁验收（G-1~G-12）→鲍勃差量验收（diff 对锚串、池/锚/字面零漂移抽检）→戴夫编译打包（三遍四零＋页数实测＋metadata M-1/M-3）。

---

## 九、重派收窄轮机器核验记录（2026-10-20 18:47 重派；核验脚本存查理私区，只读复核）

1. **锚串命中**：17/17 old 串在 R5 tex 唯一命中（count==1，§〇.5 fence 解析口径）。
2. **K 措辞逐字**：K-2（F14 new 内 266 字符）／K-3（F15 new 内 367 字符）／K-5（F16 new 内 539 字符）与 A 轨 v2 `81756c55a107` §四引块**字节级恒等**，3/3。
3. **K-1' 可选句弃用**：17 段 new 文本对 K-1' 两注记句 0 命中（PI「暂无额外的诗」＝诗面零增补落实）。
4. **正反向回放证明**：R5 tex 顺序应用 17 对 → 与撞窗残留 R6 tex（131,329 B）**字节恒等**；反向回放（F17→F01）还原 R5 tex **字节恒等**——17 对恰为 R5→R6 完整差异，无失配无多写。
5. **References 区恒等**：r5／残留 r6 的 `\section*{References}` 至文末区块（14,779 B）字节恒等；冻结点引述 `a57d7fe` 两侧均恰 1 处，不增不减。
6. **词频账（r5 → 残留 r6，落稿轮照此复核）**：`position paper` 3→1（余 1＝L437 LeCun [R22] 第三方描述语豁免）；`position statement` 4→4（L461/L518/L524/L648 零动）；`kill` 31→32（K-5「kill verdicts」逐字携带，净 +1 如 G-9 申报）；`Death` 1→0（题面 −1，F11）；小写 `death` 1→1（F-C3 装置句零动）；`kimi` 2→2（L256/L401 审计迹字段路径零动，大写 KIMI 0）。
7. **禁用形机扫（17 段 new 文本合并）**：KIMI／onewithdream／与死同行／来源箭头词族（inspired by／originates in／traces back to／the source of）／C-2 ①完成态与③预言之诺／营销词族（groundbreaking／revolutionary）／epigraph——全 0 命中。
8. **R5 tex 零触碰**：本轮全程只读（sha12 `ba2f157196f5`·123,129 B·666 行，三次断言一致）；G-4 objection 词族按申报口径复核成立（粗体头 4＋摘要句 1）。

---

—— 查理-论文主笔 ｜ 2026-10-20 ｜ R6 重派收窄轮 · F01–F17 锚串 · 只读基准 ba2f157196f5 · 机器核验 §九 · 建议非裁
