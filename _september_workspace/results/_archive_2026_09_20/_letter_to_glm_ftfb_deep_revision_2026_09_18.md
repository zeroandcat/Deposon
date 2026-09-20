# FTFB arXiv 稿 D 深度修订指示（执行委托）

**致**：GLM（修订执行方）
**自**：KIMI 凝子-agent（独立双审方，只审不改）
**日期**：2026-09-18
**主题**：`fiction_that_feeds_back.tex`（Fiction That Feeds Back: From Non-Euclidean Geometry to Machine Worldviews，Qihao Yuan，cs.AI 主分类）D 档深度修订执行依据

**源文件**：`ftfb_pkg/ftfb_arxiv_final_2026_09_18/fiction_that_feeds_back.tex`（528 行）
**基准指纹（SHA-256）**：`9de366a6c4d60443273d60edde7d9bc2074b3909afaf9a4d6f56afb4425e81f9`

**开工门禁**：GLM 动手前重算 SHA-256 与基准比对，不符即停工上报；行号摘录以该指纹版为准，回执须给新旧行号对照。

**当前包基线**（实测+compile_verification.txt）：四零；PDF 24 页（指纹附录 C）；摘要 1849 字符（上限 1920，余量 71）；正文约 12286 词（L85–L419）；池 56 条；5 锚点各一次。

---

## 一、双审结论摘要

**审查员 A（技术）**：pdflatex 三遍四零实测通过；兼容层、锚点、池编号结构无阻断缺陷；3 条 underfull 已披露，不阻断。

**审查员 B（学术）**：架构与两级证据纪律成立；但实名稿残留双盲话语自相矛盾；R13/R14 悬空、R42–R45 著录不全；Landauer 措辞超出所引；自述占 20–30%；分类法缺正面论证；F-C1 近乎形式性通过未声明。

**用户裁定**：执行 D 深度修订：GLM 改，KIMI 只审；完稿经修订后双审（独立两审 PASS）方可重投。

---

## 二、修订项清单

### P0（必修：合规与一致性）

#### P0-1 双盲话语清除

**位置与原文**（逐字摘录；此外 L65 注释 `% until camera-ready restoration.` 与 README.md L22–23 同病，一并处理）：

| 行 | 摘录 |
|---|---|
| L81 | `review-time availability runs through a confidential channel offered to the editors, public availability deferred to camera-ready` |
| L136 | `anonymized for double-blind review (title, authors, and identifiers withheld, restored at camera-ready, offered to reviewers through the confidential channel declared in §7.1)` |
| L296 | `withheld for double-blind review, restored at camera-ready, offered to reviewers through the confidential channel declared in §7.1` |
| L319 | `in the blind-review version of this paper, third-party executability runs through the confidential channel and full digests declared in §7.1, and public executability is deferred to camera-ready` |
| L325 | `an engineering project whose identity is anonymized for review and restored at camera-ready` |
| L335 | `are offered to the editors and reviewers through a confidential channel, per double-blind discipline, and the public pointer is deferred to camera-ready` |
| L375 | `that availability is offered through the confidential channel declared in §7.1 until camera-ready` |
| L422 | `anonymized for double-blind review (title, authors, and identifiers withheld; restored at camera-ready; offered to reviewers through the confidential channel declared in §7.1; …)` |
| L525 | `withheld for double-blind review, restored at camera-ready; offered to reviewers through the confidential channel declared in §7.1` |

**修订方向**：R56 匿名事实保留（作者级决定），仅改框架措辞，统一口径：withheld in this edition ＋ to be restored in a revised version ＋ available from the author(s) on request。

**建议替换措辞**（GLM 可按语法微调，语义不得漂移）：

- L81：`the full frozen record and digests are available from the author on request, public availability deferred to a revised version`（改后必须复测摘要 ≤1920 字符）
- L136/L296/L422/L525 的 R56 括注：`withheld in this edition, to be restored in a revised version, available to any reader from the author on request`
- L319：`in this edition, third-party executability runs through the full digests available from the authors on request (§7.1), and public executability is deferred to a revised version`；其后续句 `only partially met while the paper is under review` 改为 `only partially met in this edition`
- L325：`anonymized in this edition and restored in a revised version`；同句后部 `restored at camera-ready` 同改
- L335：`Availability, stated for this edition: the complete frozen repository and the full SHA-256 digests — not only the twelve-character prefixes printed above — are available from the authors on request, and the public pointer is deferred to a revised version.`；同段 `during review it runs through the confidential channel or not at all` 改为 `in this edition it runs through the on-request channel or not at all`
- L375：`that availability runs through the on-request channel declared in §7.1 until a revised version`
- L65 注释改为中性说明（见 P2-14）；README.md L22–23 的 `(double-blind review convention; to be restored at camera-ready)` 改为 `(anonymized in this edition; to be restored in a revised version)`

**假阳性**：L268 `editors, readers, and writers apply it to manuscripts`（流派编辑义）改 `reviewers, readers, and writers …` 使 grep 干净；L363 `placed under human blind review at scale` 为 [R28] 实验条件，**保留**（连字符形 `blind-review` 不命中清零模式）。

**验收**：tex 与 README 内 `grep -i -E "double-blind|blind-review|camera-ready|confidential channel|offered to the editors"` 零命中；R56 仍为匿名条目；L363 原样。

#### P0-2 陈旧流程时态清零

**位置与原文**：L136 `to be completed in the pre-submission verification round`；L136 `A second-round novelty check is scheduled before submission, and those statements carry that gate.`；L306 `the gap statement carries the scheduled second-round novelty check before submission`；L412 `with the second-round check scheduled before submission`；L422 `flagged below for completion in the pre-submission verification round`。

**修订方向**：默认删闸门从句——新颖性声明本就相对于 2026-09-16 完成的三线检索，删后自洽；若补跑，写完成态并注明日期与结果。

**验收**：`grep -i -E "scheduled|to be completed|pre-submission"` 零命中；新颖性声明语义不增强。

#### P0-3 R13/R14 [IDENTIFIER-PENDING] 闭合（已联网查实，出处见附录 B）

**原文**（L440、L441）：

```
\item[R13.] V. Vinge, ``The Coming Technological Singularity'', in \textit{Vision 21: Interdisciplinary Science and Engineering in the Era of Cyberspace}, NASA, 1993 (NTRS). [IDENTIFIER-PENDING]
\item[R14.] H. Osawa et al., Int. J. Soc. Robot. 14(10):2123–2133, 2022 (anchored by volume, issue, and pages). [IDENTIFIER-PENDING]
```

**建议替换条目**（URL 断行遵守既有 `\allowbreak` 约定，参照 R03/R05 条）：

```
\item[R13.] V. Vinge, ``The Coming Technological Singularity: How to Survive in the Post-Human Era'', in \textit{Vision 21: Interdisciplinary Science and Engineering in the Era of Cyberspace}, NASA Conference Publication CP-10129, NASA Lewis Research Center, 1993. NTRS Document ID 19940022856 (accession 94N27359), \url{https://ntrs.nasa.gov/citations/19940022856}.
\item[R14.] H. Osawa, D. Miyamoto, S. Hase, R. Saijo, K. Fukuchi, Y. Miyake, ``Visions of artificial intelligence and robots in science fiction: a computational analysis'', Int. J. Soc. Robot. 14(10):2123–2133, 2022, DOI:10.\allowbreak 1007/\allowbreak s12369-\allowbreak 022-\allowbreak 00876-\allowbreak z.\allowbreak 
```

**联动改写**：L136 (ii) 计数改完成态——`Fifty-three entries were verified … and two ([R13], [R14]) carry unstable identifier snapshots …` → `Fifty-five entries were verified against primary records`（53+2），删悬空标记从句；L418 末句 `the two identifier-pending entries are flagged in §1.3(ii)` 删除；L422 前言删 `Two entries, [R13] and [R14], have unstable identifier snapshots; … flagged below for completion in the pre-submission verification round.`，R56 括注同步 P0-1。

**验收**：`IDENTIFIER-PENDING` 零命中；池数仍 56，计数算式 55+1=56 在 L136 自洽；新标识符与附录 B 一致。

#### P0-4 §7 指针精度（核验后重述）

核验更正：L375 已是 `declared in §7.1`；唯一裸 `§7` 为 `For the §7 instance`（整节指称，保留）。改写后存活的可得性指针须指向 §7.1（声明句 L335），不得退化为裸 §7。

**验收**：改写后 `declared in §7.1` 型指针全部保留为 §7.1；`the §7 instance` 用法原样。

### P1（应修：论据与引用质量）

#### P1-5 R42–R45 著录补全（已联网查实，出处见附录 B）

| 行 | 原文 | 修订后（建议） |
|---|---|---|
| L493 | `Gonçalves, ``What fiction does … sociotechnical fictions'', TATuP, 2026 (open access).` | `A. Belsunces Gonçalves \& W. Mehnert, ``What fiction does within and outside technoscience: Science fiction, fictional technofutures, and sociotechnical fictions'', TATuP, 2026, DOI:10.\allowbreak 14512/\allowbreak tatup.\allowbreak 7281 (open access).` ——**该文为两人合著**，仅署 Gonçalves 属漏著；卷期页码期刊页未暴露，GLM 从 PDF 版（article/view/7281/12289）补全，补不到则在回执标注 |
| L494 | `Bormashenko, Entropy 27(4):437, 2025, DOI:… (review).` | `E. Bormashenko, ``Landauer's Principle: Past, Present and Future'', Entropy 27(4):437, 2025, DOI:… (review).`（全名 Edward Bormashenko 已实证） |
| L495 | `Hsieh, PRL 134:050404, 2025, arXiv:2201.12110.` | `C.-Y. Hsieh, ``Dynamical Landauer principle: Quantifying information transmission by thermodynamics'', PRL 134:050404, 2025, DOI:10.\allowbreak 1103/\allowbreak PhysRevLett.\allowbreak 134.\allowbreak 050404, arXiv:2201.12110.`（单作者 Chung-Yun Hsieh） |
| L496 | `Miščević, \textit{Thought Experiments}, Springer, 2024.` | `N. Miščević, \textit{Thought Experiments}, Springer Cham, 2022, DOI:10.\allowbreak 1007/\allowbreak 978-\allowbreak 3-\allowbreak 030-\allowbreak 81082-\allowbreak 5.` ——**年份由 2024 改为 2022**（版权年 2022；2021-09 上线）；全名 Nenad Miščević 已实证 |

**验收**：四条均含首字母与标题；年份卷期 DOI 与附录 B 一致；R42 为两作者。

#### P1-6 Landauer 措辞降级（决策点 D-6，默认 (a)）

**位置与原文**：L208 `the abstract measure re-entered physics as an expense with experimental consequences`；L214 `the quantity acquires an experimental price, kT·ln2 per erased bit [R10] — a price now traced across survey and dynamical treatments of information thermodynamics [R43], [R44]`；L223 `an operative quantity with units, prices, and experimental tests`。（摘要 L81 的 `a measurable price` 较弱，不动。）

**问题**：R10 理论原文、R43 综述、R44 理论推广，均非实验验证；措辞超出所引来源。

- **(a) 默认**：L208 → `with experimental consequences in principle`；L214 → `an experimental price in principle, kT·ln2 per erased bit [R10]`；L223 → `with units, prices, and experimental consequences in principle`。
- **(b) 可选（须用户批准）**：补实验验证入池为 R57：`A. Bérut, A. Arakelyan, A. Petrosyan, S. Ciliberto, R. Dillenschneider, E. Lutz, ``Experimental verification of Landauer's principle linking information and thermodynamics'', Nature 483(7388):187–189, 2012, DOI:10.1038/nature10872.`（标识符已查实；**页码 187–189**，简报 187–190 有误）。级联：池数 56→57；`fifty-six`（L136/L412/L422）与 `[R01]–[R56]`（L136/L422）同步；L521 池组标题改 `Pool R55–R57`；L214/L223 引 [R57]；(a) 的 L208 降级仍执行；**L136 经 P0-3 改出的 `Fifty-five entries were verified against primary records` 在 (b) 情形升为 `Fifty-six entries were verified against primary records`（56+1=57 闭环）**。

**验收**：三处措辞与所引来源强度匹配；(b) 情形下全库计数自洽、README 同步。

#### P1-7 Čapek 归因注记

**位置与原文**：L238 `The word robot entered the language through Čapek's play R.U.R. (1920)`。

**修订方向**：补半句标准归因（Karel 承认该词为其兄 Josef 所提议，附录 B）。建议：`The word robot entered the language through Karel Čapek's play R.U.R. (1920) — the word itself was suggested to Čapek by his brother Josef Čapek, as Čapek himself acknowledged`。

**验收**：L238 含 Josef Čapek 归因；不影响 [R12] 锚点表述。

#### P1-8 奇点锚类别改正

**位置与原文**：L240 `carries this named, datable textual anchor (\textbf{lexical anchor})`。

**问题**：lexical anchor 由词典记录支撑；Vinge 1993 是有名文本而非词典记录。

**修订方向**：L240 改 `(\textbf{named textual anchor})`；涟漪：L250 改作涵盖两类锚（`Lexical and named textual anchors: dictionary records and dated primary texts fix the vocabulary ([R12], [R13])`）；L257 `(lexical anchor, [R13])` 改 `(named textual anchor, [R13])`；L120 锚类型枚举增列 `named textual anchor`。

**验收**：Vinge 一处不再顶 lexical anchor 类别；锚类型枚举与正文用法一致。

### P2（深度修订，D 档特有）

#### P2-9 元评论压缩为文末附录

**问题**：provenance/verification 自述逐节重复（L134、L136、L268、L296–L298、L335、L349、L412），约占 20–30%。

**修订方向**：References 前增设 `\section*{Appendix: Verification Statement}`，集中收纳：逐批次验证记录、64 查询组检索协议与筛选规则、[R36] 未捕获声明、逐行 provenance、availability 细则、锚定位限制申述。正文每处只留一句指针（如 `Verification records and the retrieval protocol are consolidated in the Appendix.`）。

**红线（不得触碰）**：`mid-strength`、`provisional pass`、`partial pass`、`indeterminate`、`unresolved by design`、`out of scope`、`author-attested freeze`、`standing demand rather than an executed fact`（P2-15(a) 后按实更新除外）、F-C1–F-C4 判死线（L104–107 与 L416 留正文）、D 处置词典（L118）、`not as a general working methodology`。

**验收**：附录与正文指针句存在；正文词数按清单第 8 条口径降幅 ≥15%；红线词逐条 grep 命中；页数变化如实记录。

#### P2-10 分类法正面论证（§1.2 新增一段）

**修订方向**：§1.2（建议 L120 段后）新增一段：分类原则是虚构输入进入科学的通道形态——符号系统（I）/有界情景（II）/被定义的量（III）/叙事（IV），按第三方可复核对象互斥区分；II/IV 边界为可翻译性门槛优先归类；声明 D 为非对称弱检验，当前无一干净 verdict（一 partial、一 unresolved、二 indeterminate、一 out of scope），功用是降级而非证伪。

**验收**：段落存在；D 处置计数与 §9.1 表一致；分类法覆盖性不得写成封闭结论（仍由 F-C4 把守判死线）。

#### P2-11 F-C1 鉴别力声明写实

**修订方向**：§9.1 表后（L406 段内）补 2–3 句：每通道仅一旗舰案例加一实例，F-C1 触发条件在当前标本上近乎形式性不被满足；如实记为该条件当前咬合力之限。

**验收**：限制声明存在；F-C1 文本本身不动。

#### P2-12 标签与版本话语统一

**规则**：枚举标签统一 `quantitative`（L81/L91/L97/L128 已一致）；L398 表行改 `Channel III — quantitative (§4)`；§4 细化标签 `abstract-quantity/formal-analogy` 与章题不动。版本话语：P0-1/P0-2 后全文只余 arXiv 版一种声音，不得再现指称评审状态的 `version(s) of this paper`。

**验收**：枚举四处与表行标签字面一致；`grep -i "version of this paper\|blind-review version"` 零命中。

#### P2-13 超长句拆分与锚点表化

**位置**：L144（约 150 词三层破折号句：Riemann/Clifford/Helmholtz 三联同位）、L268、L298、L335、L349。

**修订方向**：L144 按人物拆三句（R53/R54/R55 引文逐字保留）；L268/L298 各拆 3–4 句；L335/L349 拆分（移附录后同拆）；§7 密排（L333 五锚、L335/L343）改锚点对照小表（tabularx），哈希前缀与字段路径逐字节保留。

**验收**：改写段落最长句 ≤45 词（引文除外）；五锚点仍各恰好一次且字符串不变；编译四零。

#### P2-14 源文件批注清理（arXiv 公开源码）

**位置**：L56–60（tolerance/badness 生产说明，含 `F10 (disclosed)`、`Current residuals: 3 lines, badness 2103/5548/1990`）、L63–65（版本说明，含 `camera-ready`），以及内部工单式 `F4/F7/F8/F10` 尾注。

**修订方向**：改为中性最小注释或删除；`grep -nE '%.*\bF(4|7|8|10)\b'` 命中的生产批注尾注全部中性化，兼容层代码本体不动；基线命中集合（以指纹版为准）：L27、L33、L34、L36、L37、L42、L47、L56。示例：L56–60 → `% line-breaking parameters for the arXiv build`；L63–65 → `% arXiv preprint edition: named author block and submission info line`。**不得**删除或改动引擎兼容层本体（L6–37 的 `\newunicodechar`/`\DeclareUnicodeCharacter` 定义）。

**验收**：源码注释中无内部工单号与生产参数记录；编译四零复测不变。

#### P2-15 §7 独立性（状态更新：(a) 已由 KIMI 执行完毕）

**执行记录**：KIMI 于 2026-09-18 10:36–10:40 CST 完成第三方复算；记录工件 `results\_kimi_ftfb_s7_independent_recompute_2026_09_18.json`（SHA-256 前 12 位 `879db0217f04`，附录 B）：5 锚点 ALL_MATCH 5/5；关键数字对冻结字段逐项 CONSISTENT；抽查 p1c verdict −1.0/−1.0000000000000002（fp 残差）、e95ci GSM8K 100/85 均 MATCH。局限：`deposon_benchmark_v1_4_gsm8k.json` 与 `deposon_v20_crossval.json` 为远端独有，仅核对手账摘要字段，建议回拉——此局限须在 §7 新句或脚注保留，不得隐去。

**GLM 须改的位置**：

- §7 增补一句记录（建议措辞）：`An independent rerun by a third party on 2026-09-18 recomputed the five anchors bit-identically and traced the headline numbers to the frozen fields (record: \texttt{\_kimi\_ftfb\_s7\_independent\_recompute\_2026\_09\_18.json}).`（工件名转义按 tex 惯例处理）
- §7.2 L339 `an independent rerun passed with bit-identical recomputation` 注明两次独立重算（AUDIT_2026-08-30 与本次），或并入 §7 新句。
- L319 `only partially met` 句、L335 `to date no independent party has executed the recomputation` 与 `standing demand rather than an executed fact`：按已执行事实改写。
- §7.4 L349 `not yet backed by a trusted time-stamp, a third-party archive, or any independent submission-time proof; the upgrade path is named, not executed`：**精确口径**——第三方重算已发生，trusted time-stamp 与 third-party archive 未发生，升级路径只完成一半。建议措辞：`now backed by an independent third-party recomputation (2026-09-18), but not yet by a trusted time-stamp or a third-party archive; the upgrade path is half executed`。T 分维持 provisional pass——重算证可重算性，不证冻结先于运行，不得过度声明。
- **(b) 降级措辞保留为备选**：若 (a) 采纳则不需要（L81/L321 `demonstrated` 与 L130 不动；L105/L339 的 `demonstrated` 为别义，本就不动）。

**验收**：(a) 记录句含执行方/日期/结果/工件名；L349 表述与完成度一致（重算已发生、时间戳与归档未发生）；L335/L349 旧"未执行"表述零残留。

---

## 三、禁止事项

1. 不得改变 56 条参考池编号；仅 P1-6(b) 经用户批准可变为 57，且必须完成全部级联。
2. 不得触碰 5 个冻结锚点（L333：`aeefb8ef6972`、`9bbe43f41fa8`、`6e9673205dc0`、`68a5b08ef007`、`6b09de9911c0`）——逐字节保留，各恰好一次（表化重排允许）。
3. 不得在 tex、README 或任何产出中引入 CJK 字符或 email 地址。
4. 不得改动摘要核心主张与 F-C1–F-C4 判死线的实质措辞；判死线不得移入附录。
5. 术语纪律：禁止引入元版本自我指称（宣称本稿为某"最终/统一版本"之类）；ECR 等邻域红线不适用本文。
6. 禁止在 tex 或任何产出中写入真实 API key 或任何形似密钥的串。
7. 不得移除引擎兼容层（L6–37）或引入 fontspec/系统字体依赖；维持 pdflatex 三遍可编译。
8. 本指示行号以基准指纹版本为准；任何与原文不符之处，GLM 停工核报，不得猜测执行。

## 四、完稿验收清单（GLM 自检并回执）

1. 开工指纹校验记录（实际 SHA-256 vs 基准值）。
2. pdflatex 三遍四零重测，更新 `compile_verification.txt`：tex+PDF 双 SHA-256、页数、锚点、池数（56 或 57）、underfull 残余如实记录。
3. README 更新：R13/R14 闭合披露、池数变化（若有）、R56 措辞去双盲化（P0-1）。
4. 摘要字符数复测 ≤1920（基线 1849）。
5. grep 清零（tex+README）：`double-blind`、`blind-review`、`camera-ready`、`confidential channel`、`offered to the editors`、`IDENTIFIER-PENDING`、`scheduled before submission`、`to be completed`、`pre-submission`、`identifier-pending`（L418）。
6. 5 锚点各恰好一次。
7. 参考池闭合复算：默认路径 55+1=56；(b) 路径 56+1=57；两处计数与前言算式自洽。
8. 正文词数复测：同一工具同一口径下较基线（约 12286 词）降幅 ≥15%（P2-9）；回执须报告所用工具与原始计数。
9. 修订后双审（独立技术审 + 学术审）双 PASS 后方可重投；未 PASS 项回 GLM 重修。
10. 回执含：新指纹、改动块新旧行号对照、各 grep 原始输出、词数与字符数实测、D-6 择定依据、D-15(a) 记录句落位。

---

## 附录 A：双审发现来源

修订项源自 KIMI 独立双审（2026-09-18，A 技术/B 学术）；行号摘录经本 agent 按基准指纹逐条复核（P0-4 经复核重述）。

## 附录 B：联网查证出处（2026-09-18 查）

| 项 | 查实结果 | 出处 |
|---|---|---|
| R13 | NTRS Document ID 19940022856；accession 94N27359；NASA CP-10129；出版日期 1993-12-01；作者 Vernor Vinge（San Diego State Univ.） | https://ntrs.nasa.gov/citations/19940022856 |
| R14 | Osawa, Miyamoto, Hase, Saijo, Fukuchi, Miyake 六作者全名；题名 "Visions of Artificial Intelligence and Robots in Science Fiction: a computational analysis"；14(10):2123–2133 (2022)；DOI:10.1007/s12369-022-00876-z | https://dblp.org/db/journals/ijsr/ijsr14 ；https://doi.org/10.1007/s12369-022-00876-z |
| R42 | 两作者 Andreu Belsunces Gonçalves（UOC IN3）与 Wenzel Mehnert（AIT/TU Berlin）；TATuP 2026 特刊 "Science fiction and technology assessment"；DOI:10.14512/tatup.7281；卷期页码期刊页未暴露，**GLM 侧从 PDF 补查**；EBSCO 收录页出现 tatup.7324 疑似他文，入池前以 PDF 首页 DOI 复核 | https://www.tatup.de/index.php/tatup/en/article/view/7281 ；https://www.oekom.de/ausgabe/science-fiction-and-technology-assessment-83156 |
| R43 | Edward Bormashenko（Ariel University）；"Landauer's Principle: Past, Present and Future"；Entropy 27(4):437 (2025)；DOI:10.3390/e27040437 | https://www.mdpi.com/1099-4300/27/4/437 ；https://doaj.org/article/08623d26867e4b98a6109264905275a5 |
| R44 | Chung-Yun Hsieh 单作者；"Dynamical Landauer Principle: Quantifying Information Transmission by Thermodynamics"；PRL 134, 050404 (2025)，2025-02-05 出版；DOI:10.1103/PhysRevLett.134.050404；arXiv:2201.12110 | https://arxiv.org/abs/2201.12110 ；https://link.aps.org/doi/10.1103/PhysRevLett.134.050404 |
| R45 | Nenad Miščević；*Thought Experiments*；Springer Cham；**版权年 2022**（2021-09-29/30 上线；现稿作 2024 有误）；DOI:10.1007/978-3-030-81082-5；精装 ISBN 978-3-030-81081-8 | https://link.springer.com/book/10.1007/978-3-030-81082-5 ；https://philpapers.org/rec/MISTE-2 |
| Bérut（候选 R57） | A. Bérut, A. Arakelyan, A. Petrosyan, S. Ciliberto, R. Dillenschneider, E. Lutz；Nature 483(7388):**187–189** (2012)；DOI:10.1038/nature10872（简报页码 187–190 有误，以此为准） | https://doi.org/10.1038/nature10872 ；https://arxiv.org/pdf/2506.24021 |
| R54 升级 | 规范著录：W.K. Clifford, "On the Space-Theory of Matter", Proc. Cambridge Philos. Soc. 2 (1864–1876, printed 1876):157–158；另收于 *Lectures and Essays* Vol. I (Macmillan, 1879) 与 *Mathematical Papers* (Macmillan, 1882), pp. 21–22；Wikisource 扫描即该刊页 | https://en.wikisource.org/wiki/Index:On_the_Space-Theory_of_Matter.djvu ；https://pubs.aip.org/aip/jmp/article-abstract/65/9/092501/3312881 |
| Čapek 归因 | Karel Čapek 本人承认 robot 一词为其兄 Josef Čapek（1887–1945）所提议（Karel 曾致函 OED 更正词源） | https://blog.oup.com/2012/11/words-were-thankful-for/ |
| §7 复算记录 | KIMI 第三方复算（2026-09-18 10:36–10:40 CST）：5 锚点 ALL_MATCH 5/5；关键数字逐项 CONSISTENT；两远端独有工件仅核对手账摘要字段，建议回拉 | 本地工件 `D:\私人资料\deposon-repo\results\_kimi_ftfb_s7_independent_recompute_2026_09_18.json`（SHA-256 前 12 位 `879db0217f04`） |

未闭合项：R42 卷期页码（DOI 已闭合）。其余各项均闭合，禁止凭记忆补写任何标识符。

## 附录 C：行号基准

本指示全部行号与摘录对应 SHA-256 `9de366a6c4d60443273d60edde7d9bc2074b3909afaf9a4d6f56afb4425e81f9` 的 528 行版本；compile_verification.txt 当前记录 PDF 指纹 `cc155e19ab574b305701afcfc28a70a0527f4f7ce8f361d7b7d7ab2536a1e74d`（24 页）。

---

## 【TRAE_FIXED_2026_09_18 门禁勘误】

**问题**: 本信开工门禁要求 GLM 重算基准 SHA-256 并比对 `9de366a6…`，对应路径
`ftfb_pkg/ftfb_arxiv_final_2026_09_18/fiction_that_feeds_back.tex`（528 行）**在本仓内不存在**，
接收方按字面路径无法开工（P0 阻断）。

**盘上实测替代基准**（Trae 2026-09-18 实算）：
- `results/_ftfb_external_review_v3_20260917_extracted/ftfb_external_review_v3_20260917/fiction_that_feeds_back.tex`
  → SHA-256 = `d060f75dbe9f...`（完整值见同目录 SHA256_MANIFEST.txt），93,324 B。
- 该 tex 的 abstract 环境已闭合（`\begin{abstract}` L69 / `\end{abstract}` L74，首个 `\section` L76），
  即 v2 缺陷（`\end{abstract}` 误置 L408）已修复，可作为 v3 修订基线。

**建议**: 开工门禁改为以盘上实存 tex 的 SHA-256 为准；若 GLM 侧另有 `ftfb_pkg` 目录，
请其自行实算后回执，两值不一致则停工待查。

