# 标准化双盲评审表 — FTFB 外审第二轮（RB-1）

**Reviewer codename:** RB-1
**Date:** 2026-09-17
**Manuscript:** *Fiction That Feeds Back: From Non-Euclidean Geometry to Machine Worldviews*
**评审依据：** `fiction_that_feeds_back_source.md`（权威全文，行号锚点皆指此文件）；`fiction_that_feeds_back.tex`（排版源，用于排版与一致性核查）；PDF 为补充件，未使用。
**评审视角（编者指派的强调透镜，非范围限制）：** quantitative methodology / AI evaluation / reproducibility & verification engineering。全程离线评审，未做任何外部检索。

---

## A. Reviewer summary（≤200 词，含阅读完整性声明）

**阅读完整性声明：** `fiction_that_feeds_back_source.md` 全文恰为 **378 行**（第 378 行为池条目 R52，文件至此结束）；本人已自第 1 行至第 378 行完整通读，并通读了全部 503 行 tex 源。

本文是立场论文，主张：fiction 不是证据，而是 exact sciences 中反复出现、可检验的输入——四条通道（formal / controlled / quantitative / narrative）在三项检验（T temporal priority、D dispensability、R operative residue）下分离；machine worldviews 是否开启 reverse channel，须以同一组可证伪判据裁决。支持手段：§2–§5 以带日期锚点的案例逐通道打分，D 依四档 disposition dictionary 降级至 supply level；§6 给出 hard-SF 硬度判据与 AI 主张可证伪判据的 M1–M5 结构同构映射及 S–F–P–E 四阶段 pipeline；§7 以一个匿名化、mid-strength 的工程实例端到端执行该 pipeline，公布冻结 SHA-256 前缀、按 field path 引用全部数字，并完整披露三项 pre-registered 命题被证伪的负结果；§9 将判据反施于论文自身并自认选择效应等局限。我的结论：论证的证据配给纪律与自我披露达罕见水准，历史层锚点真可复核；§7 在盲审期内对第三方不可执行（作者已直言），M4 映射行存在一处定义域内部张力，ECR 等头部指标未在文中定义。建议 Minor Revision。

## B. Significance & originality — **4/5**

论文自评的核心贡献是 criteria apparatus（§1.3 贡献 1，md 44、50）：三项检验（md 32–34）、D 的四档处置词典（md 36）、两层证据分级与 mixing/porting 边界（md 38）、四条可证伪条件 F-C1–F-C4（md 25–28）。该装置在虚构—科学反馈研究中的确是新的，且其第二用途——把 hard-SF 判据映射为 AI 主张裁决判据（M1–M5，md 186–190）并配 S–F–P–E pipeline（md 210–213），在真实工程件上端到端执行（§7）——把 pre-registration 与 falsifiability 规范文献（[R47]–[R52]）转成可移植操作协议，对 AI 评审实践有现实意义；reverse channel 的裁决议程（§8.3，md 265–269）恰落在 AI-Scientist 类系统兴起（md 259–261）的时点上，问题设置及时。未给 5 的原因：四通道的历史读法按论文自述 "close to what the field already holds"（md 50），增量在装置而非史论；工程实例仅一件且自评 mid-strength（md 241），不承载规模性结论（md 298）；新颖性声明受限于已声明的检索（md 52、204），第二轮 novelty check 尚未执行——声明诚实，但上限受限。

## C. Soundness of argument & evidence — **4/5**

**核查通过的强项。** §1.2 的 D 处置词典（md 36）与五个计分行逐一吻合：Channel I partial pass（md 81）、II unresolved by design（md 109）、III indeterminate（md 133）、IV indeterminate（md 167）、§7 out of scope（md 245），主表（md 285–290）照录；层级隔离（md 38）全文成立——§2–§5 未借 §7 裁决权威，§6/§8 仅为 criteria porting（md 170、273），§7 开篇重申层级归属（md 221）。可离线复核的算术全部自洽：ECR 的 17 finite + 3 Infinity + 2 no-arm = 22、coverage 20/22 可复原（md 231）；338×20 = 6,760（md 231）；池分组 15+14+10+2+4+7 = 52（md 310–370），R01–R52 全部在正文出现；"roughly seventy years" 口径一致（md 120、132、287）；2.220446049250313×10⁻¹⁶ 恰为双精度 machine epsilon（2⁻⁵²），与 "the scale of double-precision machine epsilon" 相符（md 231）。§7 负结果披露（md 231、235、239）在 AI 评估文献中属上乘。

**问题（均可修，按严重度排序）。**
1. **M4 行的定义域张力（中等）。** §6.1 声明映射 "inherits exactly these four demands and nothing else"（md 176：[R37]×2 + [R36]×2），但 M4 左列是 "Narrative artifacts can carry engineering commitments; the diegetic prototype has documented instances [R32], [R33]"（md 189）——S&TS 文献的描述性实践命题，非四项类型判据之一。Method claim 的 kill condition（"if any row's two ends fail to share form and failure mode under inspection"，md 217）使该行的形式一致性成为承重件，而左列的"规范判据"（M1/M2/M3/M5）与"实践记录"（M4）形态不同，"row-by-row shared form"（md 192）在 M4 上最弱。修法：将 M4 显式标注为 enforcement/motivation row，或修订 md 176 的 "nothing else" 句。
2. **通道级可证伪性被结构性钝化（中等，论文已自认）。** F-C2 明言 demonstrated dispensability 不是降级触发（md 26），§9.2 又承认案例按 anchorability + residue 入池、T/R 通过部分是选择产物（md 298）。两者叠加意味着现有池上通道级 kill line 几乎不可触发：T 崩塌与 R 缺失被入池标准排除，D 被 supply-level 措辞吸收。Thesis 句 "four channels ... separate under three checks"（md 19）的 "separate" 目前主要靠 D 词典标签与 §4 时序让步承载：主表中 I 与 II 仅 D 标签不同、III 与 IV 仅 T 的 scoped 与否不同（md 285–288）。建议明示 F-C1 所需的 profile 距离，并正面说明 III/IV 近同构为何不触发 F-C1。
3. **守恒通过的可能同义反复（待作者澄清）。** F 阶段称 "constructive identity T+R+A=1 for arbitrary parameters"（md 227）。若 A 为残差定义（A := 1−T−R），则 "conservation identity survives audit"（md 231）是定义性检查而非经验通过；pass 与 kills "at the same freeze level"（md 235）在冻结层面成立，但信息量层面两者不同类。请澄清 A 的参数化方式。
4. **"independent rerun" 未按自身标准刻画（轻）。** §7.2 称 "an independent rerun passed with bit-identical recomputation"（md 235），而 §7.4 对锚点严格区分 author-attested 与独立锚（md 245）。复跑者与构建者的关系未说明——若为同项目成员，"independent" 过强。
5. **锚点归属小误（轻）。** §5.4 将 self-statement anchor 引作 [R11]（md 160），T 检验同（md 166）；但按 §5.1 的两锚结构，自述文档是 [R41]（md 142 "the documented hinge of the case [R41]"），[R11] 是 primary-source anchor（md 144）。请核对。
6. **主表加注与 "nothing is re-scored"（轻）。** §9.1 声明 "nothing is re-scored"（md 281），但表中为 Channel I 的 T/R 与 Channel III 的 R 添加 "(strong)"（md 285、287），而分节评分只写 "Pass"（md 80、82、134）。加注有正文依据（md 64、132），但应声明注记来源。

综合：证据—主张配给纪律罕见地严格，问题集中在一处映射行定义域、通道级证伪的触发条件、以及若干可一句话修复的精确性滑点。4/5。

## D. Literature coverage & citation accuracy — **4/5**

52 条闭池按用途分组（md 310–370），与 §1.3(ii) 的核验声明吻合（50 verified + 2 identifier-pending = 52，md 52）。[R13]/[R14] 的 [IDENTIFIER-PENDING] 处理是范本式的：正文声明（md 52）、文献表前置说明（md 308）、条目级标注并以卷期页锚定（md 324–325）——按表单指引不计为错误。§6.2 的 provenance declaration（md 196）将"本文的形式化"、[R38]/[R39] 的 failure modes、[R46]–[R52] 的方法论原始文献三层分清，引用实践高于通行标准。离线可核条目与原始记录一致（含 R01 Walter 文集章节、R02 Einstein 1921/1922、R10 Landauer 1961、R11 Morris–Thorne 1988、R29 Kapoor & Narayanan 2023、R47 Nosek 2018、R50 Stodden 2016 等）。离线无法核验的：R42–R45（2024–2026 年新条目）、R15，以及两条元数据注记——R26 的标题沿革（md 340）与 R28 的作者三元组 "C. Si, N. Yang, T. Hashimoto"（md 342，此项我离线记忆中无法确认，建议优先复核）；均不据此刻为错误，建议在论文自行排期的 pre-submission verification round 复核。闭池设计下可补强的相邻文献（属建议非缺失）：§3.1 的 Brown–Norton 之争通常还引 Kuhn "A Function for Thought Experiments"（第三经典立场）；模型/理想化文献在 [R07] 之外可补 Frigg–Hartmann 一线；§5 的 agenda-setting 可与 narrative economics 对话。4/5。

## E. Clarity & presentation — **4/5**

术语先定义后使用（md 32–38），表格与正文互引一致（§7.4 引 §9.1，md 245 与 md 281）；主张—证据配给的可读性高于同类立场论文。代价：长句密度高（md 196 的 provenance 段、md 231 的 E 段一段承载约十五个数字，宜拆分）；md 221 的匿名化声明句同时断言 "every field path ... unchanged" 与 "basename tokens replaced by 'anon'"，"field path" 一词未定义导致两论断字面紧张，需一句澄清；md 231 的 ECR 覆盖算术需读者自行复原（17+3+2=22），宜显式给出。排版源存在结构性缺陷：`fiction_that_feeds_back.tex` 中 `\begin{abstract}`（tex 第 69 行）迟至第 409 行才闭合，§1–§9.3 全部嵌于 abstract 环境内（article 类下正文将以 `\small` + quotation 缩进排版，"Abstract" 标题下出现整部正文；20 页 PDF 的页数与 `\small` 排版相容），`\section*{References}`（tex 第 411 行）才回到正常版式——应在下次编译前修复。4/5。

## F. Verifiability & reproducibility — **3/5**

分层评估。**历史层：真可复核。** 锚点是公开、带日期的一手文献与词典记录（md 80、148–150、166），第三方可独立再检——兑现了 "re-examinability"（md 21）。**工程层（盲审期）：对第三方实际不可验证，论文对此直言不讳。** 公开文本仅携带 12 字符 SHA-256 前缀（md 229）与 field path（md 231）；无公开 repo、无公开全摘要、无外部时间戳，故锚点匹配、字段解析、数字复算在盲审期均不可执行——论文明说 "A reviewer working from the public text alone therefore cannot execute the recomputation that M4 asks of a third party, and this paper does not claim otherwise"（md 231），并在 §6.4 预先校准 "the requirement is therefore only partially met while the paper is under review"（md 215）。冻结时序为 author-attested（md 245 明言 "it buys verifiability, not independence"）。但 §6.4 P 阶段要求的 "external anchor"（md 212、267）由作者自发布的前缀充当，"external" 之"外"未兑现为独立时间戳（公开注册库或 trusted timestamping）——这是装置定义与实例之间的一处实质落差。12 字符前缀（48 bit）作为保密渠道内全摘要的对照符足够；camera-ready 公开指针应随附完整 64 位十六进制摘要，否则发表后公众核验止步于前缀。本评审包未获保密渠道工件（见 N），故对 §7 的评估限于公开文本的内部一致性与已声明限制，非复算。综合：延迟验证架构（field path + 前缀 + camera-ready 指针）设计合理、声明诚实，但当期第三方可验证性为零、锚点外部性弱于其名——3/5。

## G. Research integrity — **5/5**

AI 披露句明确（"The drafting model is GLM"，并声明全部数字由作者核验、逐条映射 field path，md 304）；双盲自洽：自引移除并声明（md 194、271）、实例匿名化且限定作用域（md 221）、tex 的 PDF 元数据与作者块为空（tex 43、61–64，编译注释亦不含身份信息）；负结果全量披露并作为资产呈现（md 231、235、239）；论文将自身判据反施于己并接受不利评分（self-score T partial / D partial / R pending，md 294；选择效应自认 md 298；kill lines 自录 md 302）；引用 provenance 三层分清（md 196）。唯一瑕疵是 §7.2 "independent rerun" 的独立性未刻画（md 235）——属精确性缺口而非隐瞒，且论文已在 md 245 对同类问题建立了诚实标准。5/5。

## H. Overall recommendation score — **7/10**

这是一部把可证伪性当作写作纪律而非口号的立场论文：判据、分级、kill lines 与自评构成少数我能逐行复核其执行的内洽系统。扣分集中于 M4 行与 §6.1 声明的定义域张力、通道级证伪在现有池上的低可触发性、以及 §7 在盲审期内对第三方的不可执行（虽已直言）——均为可修文本项而非结构性缺陷。

## I. Recommendation

- [x] **Minor Revision**

理由：全部发现的问题有界、可修、无需新实验——M4 行重标注或修订一句声明（md 176/189）、ECR 与图组群的文中定义（md 227–231、239）、锚点 "external" 的兑现方案（md 212/229/245）、复跑独立性的刻画（md 235）、若干措辞与排版修复（md 221、281、tex 69/409）；identifier-pending 完成与 novelty check 已由论文自行排期（md 52）。

## J. Strengths（≥3，均带锚）

1. **评分装置的行级可执行一致性。** D 的四档 disposition dictionary 在 §1.2 一次性声明（md 36）后，五个计分行无一例外按词典落位（md 81、109、133、167、245），主表（md 285–290）与分节评分逐格对应——一套 rubric 的执行可由审稿人逐行复核，这在评分系统设计中并不多见。
2. **证据层级的纪律。** 两层证据（historical / pre-registered adjudication）与 mixing/porting 边界在 §1.2 声明（md 38）并全文维持：§2–§5 从不借 §7 裁决之威，§6/§8 只携判据过层并在接收层重实例化（md 170、273），§7 开篇即重申（md 221）。
3. **负结果披露的完整度。** §7.1 三项 pre-registered 命题全部被证伪并按预冻结协议报告（md 231）；§7.3 披露 capability channel 读零、±10pp 功效上限、CoT 基线显著更优、先验融合反而稀释（md 239）；§7.2 以 "Death is the point"（md 233–235）将 kill 作为 pipeline 的正常产出——"negative results disclosed in full"（md 5、47）是兑现的。
4. **自我适用与自我限制。** §9.1 对论文自身打分并接受不利结果（md 294），§9.2 承认 T/R 通过部分为选择效应（md 298），§7.4 承认冻结锚 "buys verifiability, not independence"（md 245）——论文对自身主张的降级与对历史案例同样严格。
5. **数字纪律与内部算术自洽。** §7 全部数字以 field path 引用冻结记录（md 229、231）；可离线复核的算术与数值全部吻合（17+3+2=22；338×20=6,760；2⁻⁵² machine epsilon；池分组求和 52；CoT 0.97 对 0.85 的 12pp 差与其 ±10pp 可检阈值自洽，md 239）。

## K. Weaknesses（≥3，均带锚）

1. **M4 行与自身定义域声明相抵（中等）。** §6.1："the mapping below inherits exactly these four demands and nothing else"（md 176）；但 M4 左列为 diegetic prototype 的实践记录（[R32]/[R33]，md 189），非四判据之一——映射表中唯一一行左列为描述性命题，而 method claim 的 kill condition（md 217）恰承重于 "row-by-row shared form"。**怎么改：** 将 M4 显式定位为 enforcement row（其 genre 侧是映射动机而非类型判据），或修订 md 176 的 "nothing else" 句。
2. **通道级证伪的可触发性趋零（中等）。** F-C2 豁免 demonstrated dispensability（md 26）＋入池即要求 anchorability 与 residue（md 298）⇒ 现有池上 T 崩塌与 R 缺失被构造性排除，D 被 supply-level 措辞吸收；主表显示 I/II 仅差 D 标签、III/IV 仅差 T scoping（md 285–288），"separate under three checks"（md 19）的分离度很薄。**怎么改：** 明示 F-C1 的触发阈值（何为 "same profile"），正面处理 III/IV 近同构为何不触发 F-C1；或将 thesis 的 "separate" 弱化为 "classified"。
3. **盲审期第三方可验证性为零、锚点外部性名实落差（中等）。** 公开文本无 repo、无全摘要、无独立时间戳（md 229、231）；P 阶段要求的 "external anchor"（md 212）由作者自发布前缀充当，冻结时序仅为 author-attested（md 245）。**怎么改：** camera-ready 公开指针随附全摘要，并采用公开时间戳/注册库使冻结时序不再自证；在 §7.4 写明 "external" 的兑现方式。
4. **头部指标未在文中定义。** ECR 仅被命名为 "the distribution-level metric"（md 227），其计算式以及 22 图 ECR 组、61 图五族 kill 采样组、per-graph crossval 字段三者的关系（md 231、239）均未说明——按论文自身 checkability 标准，头部指标的定义应在公开文本内。**怎么改：** §7.1 增一段 ECR 定义与组群关系。
5. **自身精确性标准的若干滑点（轻）。** md 221 同句内 "every field path ... unchanged" 与 "basename tokens replaced by 'anon'" 需以定义消歧；md 281 "nothing is re-scored" 与 md 285/287 的 "(strong)" 加注未声明；md 231 字段名 "P1a_P1b_T_P1c" 与命题名 "P1a, T-P1b, T-P1c" 的前缀不对称未注记；md 160/166 的 self-statement anchor 池编号疑应为 [R41]（见 C-5）；tex 第 69/409 行 abstract 环境错位（见 E）。

## L. Specific comments（行级）

1. md 5（Abstract）末句的可用性限定语准确，保留。
2. md 26（F-C2）：建议补一句承认通道级有效 kill 收缩为 T 崩塌或 R 缺失，故 F-C1/F-C4 承载类型学的可证伪性。
3. md 148/323：措辞 "entered the language through Čapek's play" 已规避词源归属问题（通常归 Josef Čapek）；R12 可在 camera-ready 补一注完备词源记录。非错误。
4. md 160/166：self-statement anchor 的池编号与 md 142–144 的两锚结构不一致，请核对（应为 [R41]；若 [R11] 文内确有自述性致谢，请注明依据）。
5. md 176 vs 189：见 K-1。
6. md 196：provenance 段信息完整但过长，可拆分；内容无需改动。
7. md 215："executable is a standing demand, not a report of who has executed"——示范性的自我校准句，保留。
8. md 221：建议改为 "the in-record field names are unchanged; repository path prefixes and basename tokens are anonymized" 一类显式表述。
9. md 227–231：给出 ECR 定义与组群关系；17+3+2=22 的划分显式写出。
10. md 229：camera-ready 应随公开指针发布完整 64 位摘要（12 字符前缀不足以支持发表后公众核验）；并核认字段名 "P1a_P1b_T_P1c" 的逐字保真（若为记录原名，加一注即可，以符 "hand-copying is forbidden" 的自设纪律）。
11. md 231："indistinguishable from a trivial six-keyword rule filter" 建议改为 "not distinguishable at these sample sizes"——同段 ±10pp 功效声明（md 239）已实质修复此语，措辞应同步收敛。
12. md 231：E 段单段约十五个数字与七个 field path，建议按三项结果分段。
13. md 235：复跑独立性刻画（见 C-4 与问题 M-3）。
14. md 239：StrategyQA 上 McNemar p=1.0 若非舍入即意味着零不一致对（两组预测完全相同）——这是值得明说的强结论，请确认并写明。
15. md 281/285/287：为 "(strong)" 加注补一句来源声明（"强度注记取自各节锚点层级"）。
16. md 294：self-score 的 R "pending" 合理；历史通道的 R 通过以"残留存续至今"为据，两者不对称但可辩护，无需改动。
17. tex 69/409/411：`\end{abstract}` 错位——正文全部嵌入 abstract 环境，下次编译前必须修复。
18. tex 421–433 等：多条 DOI 末尾悬置 `\allowbreak`，无害但不整洁，顺手清理。

## M. Questions to authors（≤5）

1. **M4 行的定位。** M4 左列（md 189）是 diegetic prototype 的实践命题，不在 §6.1 采纳的四项类型判据（md 176）之内；在 method claim 的 kill condition（md 217）之下，请说明 M4 两端 "share form" 的确切含义，或重新标注该行（enforcement row / motivation row）。
2. **A 通道的参数化。** "constructive identity T+R+A=1 for arbitrary parameters"（md 227）中，A 是独立参数化还是残差定义（A := 1−T−R）？若是残差，"conservation identity survives audit"（md 231）属定义性检查，请注明——这决定该项 pass 的信息量归类。
3. **复跑的独立性。** §7.2 的 "independent rerun ... bit-identical"（md 235）：执行者与构建者何关系？bit-identical 复算在何种硬件/软件栈上成立？请按 §7.4 对锚点所用的同一独立性词汇（md 245）刻画。
4. **ECR 与组群。** 请给出 ECR 的计算定义，并说明 22 图组（ECR）、61 图五族组（kill 采样）、per-graph crossval 字段（md 231、239）三者的关系；同时确认 StrategyQA p=1.0 的含义（零不一致对还是舍入）。
5. **锚点外部性的兑现。** P 阶段要求 "external anchor"（md 212、267），而 §7 的锚点是作者自发布的前缀（md 229），冻结时序为 author-attested（md 245）。camera-ready 是否会采用公开时间戳/注册库（如 OSF 式预注册或 trusted timestamping）使 "external" 名副其实？

## N. Confidential notes to the editor

1. **保密渠道工件未随包提供。** §7.1 声明完整冻结库与全摘要 "are provided to the editors and reviewers through a confidential channel"（md 231），但本评审包（packet_RB1）未包含该工件。因此本评审对 §7 的评估限于公开文本的内部一致性与已声明限制，未执行 M4 所要求的第三方复算。若编辑部希望本轮即行复算，请另行分发工件（或其只读镜像）；若已有分发安排，建议在送审包中向审稿人明示获取方式。
2. 排版源存在 abstract 环境错位（tex 69/409），会实质影响 20 页 PDF 的版式（正文在 abstract 块内以 `\small` 排版），建议修复后再进入下一轮。
3. 本人在评审过程中未遇到任何作者身份信息，未尝试任何 de-anonymization，亦未对匿名的 §7 实例做任何外部检索（全程离线）。

## O. Declarations

- I have no conflict of interest with this work: **[x] yes**
- I did not attempt to de-anonymize the authors: **[x] yes**
- I will maintain confidentiality of this review: **[x] yes**
- Reviewer codename: **RB-1**  Date: **2026-09-17**
