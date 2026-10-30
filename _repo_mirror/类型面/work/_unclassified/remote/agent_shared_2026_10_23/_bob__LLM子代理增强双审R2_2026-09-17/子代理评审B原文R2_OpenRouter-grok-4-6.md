# Reviewer B 增强框架评审原文（R2 轮子代理评审）

- 通路代号：OpenRouter
- 模型：x-ai/grok-4.6
- 会话：单轮独立会话（不与 Reviewer A 共享任何上下文；与 R1 轮会话亦无共享）
- 框架：KIMI/Coze 方法论＋联网所学（见《增强评审框架说明》）；材料/模型/参数与 R1 轮完全一致，框架为唯一变量
- 请求参数：temperature=0.4, max_tokens=16000, attempt=2, 耗时282.1s
- token 用量：prompt=48189, completion=16413
- finish_reason=stop

---

# 法证式核查报告（审稿人 B）

材料范围：PAPER_MD（L9–L391）、PAPER_TEX（T1–T511）、COMPILE_CV（C1–C135）。所有论断回锚原文；材料外事实不臆测。证据分层：渲染层 / 源层 / 可识别性。

---

## 1. 总表

| 维度 | 判定 | 🔴Major | 🟡Minor |
|---|---|---|---|
| 维度一【结果】 | PASS | 0 | 1 |
| 维度二【讨论】 | GRAY | 2 | 2 |
| 维度三【局限】 | GRAY | 0 | 2 |
| 维度四【五锚不变式】 | PASS | 0 | 0 |
| 维度五【可复现性】 | GRAY | 1 | 2 |
| **总体** | **GRAY** | **3** | **7** |

---

## 2. 逐维详审

### 维度一【结果】

**【结论】** PASS

**【定位与证据】**

守恒与容差（§7.1）：

> L239: "The conservation identity survives audit: the maximum per-path deviation across all variants and benchmarks is 2.220446049250313×10⁻¹⁶ — the scale of double-precision machine epsilon, against an implementation tolerance of 10⁻⁶ — closed (pre-registered) (results/anon_benchmark_v1_4_gsm8k.json · physics_audit.t_plus_r_plus_a_max_deviation)."

对应 TeX：T326 逐字同值、同 field path。

ECR 与覆盖：

> L239: "median ECR = 4/3 over the 17 finite-valued graphs, with coverage of 20 of 22 graphs — three graphs read Infinity, two graphs lack arm data, both disclosed as-is (frozen handoff artifact, field headline_results.GT4_ECR)."

枚举范围与判死线：

> L239: "61 graphs in five families" / "all 6,760 states of the 338-task corpus, 20 steps each" / "P1a: maximum deviation 0.8569" / "T-P1b: minimum directional cosine −1.0" / "T-P1c: killed on both lines, with an 81-point grid over τ∈[0,4] reaching minimum cosine −1.0" / "cyclic-graph median residual 0.669"

滤波对照与 McNemar（§7.3，由 §7.1 链条的负面结果延伸）：

> L247: "on GSM8K the filter scores 0.87 against the layer's 0.85 (McNemar p=0.5), on StrategyQA 0.899 against 0.899 (p=1.0)" / "detectable-difference threshold is roughly ±10 percentage points" / "0.97 versus 0.85" / "physics 0.484→0.452 and historical 0.783→0.739 at the λ=0.5 convex combination"

Channel III 定量口径（§4）：

> L128: "H = -Σ p·log p" / "kT·ln2 per bit"
> L140: "Scoped pass: arrow-level dating holds; the channel-level priority claim is downgraded"

预登记与负面结果：

> L243: "The three falsifications are the pipeline working as designed, not a failure of it."
> L44: "Out of scope: the claim never invokes indispensability, so the check has no target (the §7 instance, whose claim rests on executability)."

**【分析】**

材料内可复算项全部闭合：338×20=6,760（材料内可证）；17 有限值 + 3 个 Infinity = 20，再加 2 个缺臂 = 22（材料内可证）；2.220446049250313×10⁻¹⁶ 与文内“double-precision machine epsilon”口径一致（材料内可证，未独立跑浮点实现）；τ∈[0,4] 的 81 点网格与步长 0.05 的闭包算术相容（材料内可证为算术可能，网格本身需外部核验）。MD/TEX 关键数字逐字一致。负面结果（P1a/T-P1b/T-P1c 全杀、能力层与六关键词滤波不可分、融合稀释、功效阈值 ±10 pp）按预登记叙事完整披露，未把 scoped pass / indeterminate 改写成全票通过。Channel III 主动降级 channel-level T，与 F-C2 的供给级口径相容。

本维不升 GRAY 的原因：定量口径自洽、判死线与披露齐全；“审稿可复算”的缺口已在 §7.1 显式声明，属维度五而非维度一的数据自相矛盾。唯一 🟡：McNemar p 与 ECR=4/3 的真值无法在三份材料内重算（需外部核验），但不构成文内守恒失败。

---

### 维度二【讨论】

**【结论】** GRAY

**【定位与证据】**

Master table 与正文分档：

> L293–L297 与 T387–T391：Channel I Partial pass / II Unresolved by design / III Scoped pass + Indeterminate / IV Indeterminate / §7 Out of scope + author-attested freeze。
> L89、L117、L140–L141、L175、L253 的分节评分与 L293–L297 一致（材料内可证）。

映射主张：

> L200: "The table claims structural isomorphism — row-by-row shared form and shared failure modes — and nothing stronger. It is not an equivalence theorem"
> L225: "The hard-SF criteria and the falsifiability criteria of AI research claims are structurally isomorphic under the mapping M1–M5"
> L13（Abstract）: "A mapping (M1–M5) shows that the hardness criteria of hard science fiction and the falsifiability criteria of AI research claims are structurally isomorphic"

M4 行：

> L197 / T279: "M4 | Narrative artifacts can carry engineering commitments; the diegetic prototype has documented instances [R32], [R33] | Adjudication procedure pre-registered, recomputable by a third party — this paper's formalization ... | Changing the rules after the fact"

四条“hard”需求 vs 五行映射：

> L184: "this paper distills four working demands for \"hard\": internal consistency, no supernatural checks, continuity with known science, and checkability of the world's claims by observers inside the world."

自设削弱条件：

> L225 / L310: "The claim weakens if any row's two ends fail to share form and failure mode under inspection"

跨 backbone / 量级：

> L249: "its magnitude is not comparable to the non-Euclidean case, and nothing in this paper claims otherwise"
> L306: "no prevalence claim is made anywhere in this paper"
> L247: "the capability channel reads zero" 随即限定 "indistinguishable from a trivial six-keyword rule filter" 与 "±10 percentage points"

Channel III 的另一“isomorphism”：

> L134: "The isomorphism of formula: the same expression, H = -Σ p·log p, governs the abstract ensemble and the physical distribution — not a similar expression, the same one."

**【分析】**

Master table 分档与 §2–§5、§7.4 宣称一致，D 的四词词典（L44）被执行，未把 Indeterminate 写成 Partial pass，也未把 reverse channel 写成待决实证——这是讨论层的诚实资产。

GRAY 来自两处实质性错位。（1）M4：左列是 Kirby 式 diegetic prototype（叙事人工物承载工程承诺），右列是预注册/第三方可复算；共享失败模式 “Changing the rules after the fact” 并不能从 [R32]/[R33] 的单元格内容形式地推出。M1–M3、M5 与 §6.1 四条 hard 需求大致对齐，M4 是第五行外加项，范畴对应不成立（或仅在“承诺一经写下不可事后改写”的隐喻层成立）。这直接触发论文自设的方法主张削弱条件（L225），属元声明自反。（2）“structural isomorphism”：Channel III 的公式同一是强证据；§6/摘要把它用在五行类比配对上，强度不匹配。摘要（L13）比正文“nothing stronger / not an equivalence theorem”（L200）更满。§7.3 对 Channel I 再一次使用同一短语，造成三义共用。

（e）跨 backbone / 普遍性：正文明确拒绝量级对比与 prevalence，§8 保持议程而非实证——主结论未超出证据。“reads zero” 与功效阈值并置，属局部修辞过冲，不构成普遍性宣称。

---

### 维度三【局限】

**【结论】** GRAY

**【定位与证据】**

> L306: "Selection effect: the four channels are visible because their cases left anchors" / "T and R pass in every scored row of §9.1 partly because the cases were selected for anchorability"
> L306: "Scale: each channel carries a small number of flagship cases, and the pipeline has one engineering-grade instance; no prevalence claim"
> L306: "Magnitude: structural isomorphism to the non-Euclidean pattern does not make the engineering instance comparable to it in scale"
> L253: "this is an author-attested freeze" / "it buys verifiability, not independence"
> L239: "A reviewer working from the public text alone therefore cannot execute the recomputation that M4 asks of a third party, and this paper does not claim otherwise"
> L60 / L316: 闭池 54；[R13]、[R14] IDENTIFIER-PENDING
> L68: Helmholtz 与 Riemann [R53]、Clifford [R54] 并列，但 Helmholtz 无池号

**【分析】**

§9.2 对选择效应、T/R 循环、单实例、量级、两套证据层级、闭池与新颖性门的披露是充分且少见地自我降级的。§7.4 对 author-attested 的认识论上限写得很清楚。这不是“不诚实”。

GRAY 是因为材料内已可见、却未写入局限清单的弱点：（i）闭池+“historical claim must be anchorable”（L40）协议下，Helmholtz 作为与 R53/R54 并列的一手历史陈述没有池条目（见议题 a）；（ii）§7.2 “independent rerun” / “second pair of hands”（L243）并未在局限中澄清其非第三方地位，易与 M4 的 third-party 标准混淆。两者均未达到 🔴（未推翻主结果），但对照论文自设的锚点纪律，披露不完整。

---

### 维度四【五锚不变式】

**【结论】** PASS

**【定位与证据】**

五枚 SHA-12（声明）：

> L237 / T324: "GT_FORMALIZATION_v1.md aeefb8ef6972; run_v21_gtformal.py 9bbe43f41fa8; run_v22_p1c.py 6e9673205dc0; SPEC_GT2B.md 68a5b08ef007; SPEC_GT8C.md 6b09de9911c0"

COMPILE_CV 互证：

> C51: "[PASS] S4-五锚不变式: aeefb8ef6972:1 9bbe43f41fa8:1 6e9673205dc0:1 68a5b08ef007:1 6b09de9911c0:1"
> C64 / C105–C106: 各恰 1 次，全部 PDF p15

冻结与 author-attested：

> L253 / T340: "this is an author-attested freeze. A digest can attest that the artifact was not altered after the fact; it cannot by itself attest to a party that did not build the system that the freeze preceded the runs"
> L297 / T391: "Pass (author-attested freeze; pre-registered tier — §7.4)"

**【分析】**

实测（材料内可证）：MD 正文每枚哈希 1 次（L237 清单；其后仅回指 “five anchors above”）；TEX 每枚 1 次（T324）；CV 断言每枚 1 次且页面级同页。三方一致。冻结被明确标为 author-attested 而非独立时间戳，master table 未把该行写成与 [R01]/[R02] 同级的 “strong; primary texts”。本维通过。哈希原像是否等于所述文件，需外部核验，不在本维材料内可证范围。

---

### 维度五【可复现性】

**【结论】** GRAY

**【定位与证据】**

Field-path 链：

> L239 / T326: `physics_audit.t_plus_r_plus_a_max_deviation`；`headline_results.GT4_ECR`；`headline_results.enumeration_scope`；`headline_results.P1a_P1b_T_P1c`；`verdict.min_cos_at_best_global_tau`；`verdict.P1a_deviation.max_dev_inf`；`headline_results.P2`；`headline_results.E9_5_power_honest` 等。

第三方通道：

> L239: "the complete frozen repository and the full SHA-256 digests — not only the twelve-character prefixes printed above — are provided to the editors and reviewers through a confidential channel"
> L223 / T310: "The requirement is therefore only partially met while the paper is under review, and the limit is stated in §7.1"

预注册层：

> L237: "The adjudication layer is frozen before runs as pure verdict functions with published SHA-256 anchors"
> L29: "\"Decidable\" is reserved in this paper for the pre-registered tier (§6–§7)"

闭池与编译记录：

> L60: "fifty-four items, cited by pool number [R01]–[R54]"
> C54–C55: "References 列表 54 条" / "正文引用 54/54"
> C99: "首现序（md 正文）：R01, R54, R13, ..."

源层痕迹（议题 d）：

> T42: "% F8: \\url 允许在连字符后断行（R37 长条目 Underfull 根因）"
> T47 / T56–T58: 中文注释
> C3: "生成者：戴夫-格式专家"
> C8: "shared/鲍勃_FTFB全稿R2修订版_2026-09-17.md"
> C26: "查理_FTFB全稿文献合并版"
> C53 / C71: PDF `CJK字符=0`；`/Author=""`
> T63–T64: `\author{}` `\date{}`

**【分析】**

Field-path 在公开文本中完整到“打开记录后应对哪一字段”；论文没有假装公开文本已满足 M4 的第三方可执行性——这是如实性加分。GRAY 来自：（1）预注册层的时间先后是 author-attested，公开文本无法复算（论文已说，但与摘要 “Every claim is stated to be checkable by a third party, subject to the blind-review availability limits” 的可执行边界完全依赖于机密通道是否真实送达，需外部核验）；（2）COMPILE_CV 的 md 首现序与 PAPER_MD 不符（见法证总表），说明验证记录本身有口径误差；（3）双盲须分层——渲染层 PASS，源层 TeX 中文注释与 CV 工作流昵称构成可识别性信号（无姓名 token ≠ 不可识别）。

---

## 法证总表

| # | 声明项 | 声明值 | 实测值 | 判定 | 证据与方法 | 可证性 |
|---|---|---|---|---|---|---|
| 1 | 五锚 SHA-12 在 MD 出现次数 | 各 1（L237 清单） | aeefb8ef6972, 9bbe43f41fa8, 6e9673205dc0, 68a5b08ef007, 6b09de9911c0 各恰好 1 次 | PASS | 对 PAPER_MD 全文精确字符串计数 | 材料内可证 |
| 2 | 五锚在 TEX 出现次数 | 各 1（T324） | 同上五串各 1 次 | PASS | 对 PAPER_TEX 精确计数 | 材料内可证 |
| 3 | 五锚与 CV 互证 | S4 各 :1；G5 均 p15 | C51/C64/C105–C106 与 MD/TEX 五串集合相等 | PASS | 三方集合比对 | 材料内可证（PDF 页码依 CV，未持 PDF） |
| 4 | 锚值 MD=TEX=CV | 五前缀相同 | 三处逐字相同 | PASS | 逐字比对 | 材料内可证 |
| 5 | 闭池规模 | 54，[R01]–[R54] | 列表 R01–R15(15)+R16–R29(14)+R30–R39(10)+R40–R41(2)+R42–R45(4)+R46–R52(7)+R53–R54(2)=54 | PASS | 条目计数 | 材料内可证 |
| 6 | CV 引用闭合 | 列表 54、正文 54/54 | C54–C55 自报 54/54；MD 引用块含 R01–R54 | PASS（CV 自报与列表计数一致） | 计数；未做 PDF 文本层独立扫描 | 列表规模材料内可证；PDF 覆盖依 CV |
| 7 | `\author{}` / `\date{}` | 均空（双盲） | T63–T64 空；C53/C68/C114 空 | PASS | 源与 CV 交叉 | 材料内可证 |
| 8 | PDF /Author | `""` | C53、C69、C115 一致 | PASS | 依 CV；未持 PDF | 需外部核验（本会话无 PDF） |
| 9 | 守恒偏差数字 MD=TEX | 2.220446049250313×10⁻¹⁶ | L239 = T326 | PASS | 逐字 | 材料内可证 |
| 10 | 338-task × 20 steps = 6,760 | 文内并列给出 | 338×20=6760 | PASS | 算术 | 材料内可证 |
| 11 | ECR 覆盖 17+3+2=22 | 17 finite；20/22；3 Infinity；2 缺臂 | 17+3=20，20+2=22 | PASS | 算术 | 材料内可证 |
| 12 | τ 网格 81 点、τ∈[0,4] | 81-point grid | 若 Δτ=0.05 则 4/0.05+1=81，算术相容 | 口径性偏差（相容但非唯一） | 算术反推 | 网格真值需外部核验 |
| 13 | Master table vs §2–§5/§7.4 | “nothing is re-scored”（L289） | I/II/III/IV/§7 的 T/D/R 标签与分节逐项相同 | PASS | 表–文对照 | 材料内可证 |
| 14 | McNemar / 滤波数字 MD=TEX | 0.87/0.85 p=0.5；0.899 p=1.0 等 | L247 = T334 | PASS | 逐字 | 材料内可证；p 值真值需外部核验 |
| 15 | Channel III 公式 | H = -Σ p·log p；kT·ln2 | MD L128/L134 与 TEX T199/T205 一致 | PASS | 逐字 | 材料内可证 |
| 16 | Helmholtz 池号 | 闭池凡历史主张应可锚（L40、L60） | L68 有 Helmholtz 无 [Rnn]；Riemann/Clifford 有 [R53]/[R54] | FAIL（相对闭池协议） | 命名实体 vs 池列表 | 材料内可证 |
| 17 | CV md 首现序 | C99: R01, R54, R13, …, R53, R02 | MD 正文首引为 L68 [R53] 然后 [R54] 然后 L70 [R01] | FAIL | 首现扫描 | 材料内可证 |
| 18 | 渲染层 CJK | C53/C71 CJK=0 | 依 CV；TEX 注释含中文（T42/T47/T56–T58） | 口径性偏差（PDF vs 源层） | 分层：CV 指 PDF 文本层；源层有 CJK | PDF 需外部核验；源层材料内可证 |
| 19 | 身份 token 扫描表 | deposon 等 =0（C53/C67） | 论文 MD/TEX 正文未出现该表内 token | PASS（就该词表） | 词表匹配 | 材料内可证；词表外昵称见 #20 |
| 20 | 工作流昵称 | 双盲 D1–D6 过门（C78） | CV 含「戴夫」「鲍勃」「查理」及中文文件名（C3/C8/C26）；论文正文无 | 口径性偏差 | 分层：论文渲染层无；CV 源层有 | 材料内可证 |
| 21 | 五锚文件原像 / 实验真值 | 冻结记录与 field 值 | 材料无仓库、无 JSON | 无法核验 | 缺工件 | 需外部核验 |
| 22 | 交付 SHA（CV [1]） | md/tex/pdf 全量指纹 | 本会话无二进制，不能重算 SHA-256 | 无法核验 | 缺文件 | 需外部核验 |

---

## 3. 问题清单

### 阻断级

无。未发现存在性造假、 compulsory 合规硬伤、或渲染层作者身份泄漏。数据真值因缺冻结仓库而无法核验，不等于已证伪。

### 🔴Major

**M-1　M4 行范畴对应不成立，触发论文自设的方法主张削弱条件。**  
定位：L197 / T279；自设条件 L225、L310。  
证据：Hard-SF 单元格为 “Narrative artifacts can carry engineering commitments; the diegetic prototype has documented instances [R32], [R33]”；AI 单元格为 “Adjudication procedure pre-registered, recomputable by a third party”；失败模式 “Changing the rules after the fact”。§6.1 只蒸馏四条 hard 需求（L184），M4 不在其中。  
可执行修改：重写 M4 左列，使之与“冻结规则/不可事后改判”同构（或把 M4 降为 pipeline 的 P 阶段注释而非映射行）；按 L225 同步削弱 Abstract/Method claim 中的 “structurally isomorphic”。

**M-2　“structural isomorphism” 强度与证据不匹配（元声明自反）。**  
定位：L13、L200、L225、L249；对照 Channel III L134。  
证据：正文承认 “nothing stronger” “not an equivalence theorem”，但摘要与 Method claim 仍用 “are structurally isomorphic”；同一文中该词还表示公式同一（L134）与 Channel I 模式类比（L249）。M4 已使 “row-by-row shared form” 不能成立。  
可执行修改：摘要改为 “row-wise pairing of failure modes” 或 “operational analogy”；保留 “isomorphism” 仅给 Channel III 的同一表达式；§7.3 改用 “pattern-level parallel”。

**M-3　预注册层“第三方可复算”在公开文本中不可执行，而 M4/摘要仍把可检查性写成主张的一部分（边界已声明，但仍与方法行不完全对齐）。**  
定位：L13 “Every claim is stated to be checkable by a third party, subject to the blind-review availability limits”；L197 M4 右列；L239 机密通道。  
证据：论文正确写明 “A reviewer working from the public text alone therefore cannot execute the recomputation that M4 asks”（L239），故不是隐瞒；但 M4 把 “recomputable by a third party” 写成映射行的 AI 侧准则，公开审稿副本无法兑现该行。  
可执行修改：M4 右列与摘要改为 “recomputable given the record, with review-time availability via confidential channel / public at camera-ready”；避免让未持机密包的审稿人面对一条自己无法执行的准则。

### 🟡Minor

**m-1　Helmholtz 一手文本在闭池中的处置不对称。**  
定位：L68 / T135；对照 L60 闭池声明、L40 T 检查、R53/R54（L388–L391）。  
证据：Riemann、Clifford 有池号与检索日期；Helmholtz “public case for the empirical standing of geometrical axioms” 无 [Rnn]、无题录。  
修改：补一条 Helmholtz 池条目（或从 §2.1 删除该并列，改为不依赖一手锚的史学转述并标明二手来源）。

**m-2　摘要对 isomorphism 的表述强于 §6.2 的限定句。**  
定位：L13 vs L200。  
修改：摘要与 L200 对齐。

**m-3　“capability channel reads zero” 与功效阈值措辞冲突。**  
定位：L247。  
证据：同句给出 McNemar 不可分与 “±10 percentage points, so smaller increments are not excluded”。  
修改：改为 “no detectable capability increment at this sample size（threshold ≈ ±10 pp）”。

**m-4　“independent rerun” 未分级。**  
定位：L243。  
证据：“independent rerun” / “second pair of hands” 与 §7.4 author-attested、M4 third-party 并置，未说明是否团队内复跑。  
修改：改为 “in-team second-operator rerun” 或给出与建造者分离的证据。

**m-5　源层中文注释与 CV 工作流昵称的双盲分层未披露。**  
定位：T42、T47、T56–T58；C3、C8、C26。对照 C53 渲染层 CJK=0、T63–T64 空作者。  
证据：渲染层无 CJK、无作者；源层 TeX 注释为中文；CV 含「戴夫」「鲍勃」「查理」。无姓名 token ≠ 不可识别。  
修改：送审 TeX 剥离中文注释；CV 若进入审稿包则匿名化昵称与路径；在局限中写明“渲染层已盲、源层生产痕迹另计”。

**m-6　COMPILE_CV 首现序与 MD 不符。**  
定位：C99 vs L68–L70。  
证据：MD 首引 [R53]→[R54]→[R01]；CV 写 R01, R54, …, R53。  
修改：重跑首现扫描或更正记录；勿把错误首现序当作门禁通过证据。

**m-7　Channel III “isomorphism of formula” 与 §6 “structural isomorphism” 术语碰撞。**  
定位：L134 vs L200。  
修改：前者保留 “identity of expression”；后者不用 isomorphism。

---

## 4. 修改优先级

| 档 | 条目 | 位置 | 一句话改法 |
|---|---|---|---|
| **P0** | M4 范畴对应 | L197 / T279；L225 | 重写左列使与预注册同构，或删行并按自设条件削弱 method claim |
| **P0** | isomorphism 措辞 | L13、L200、L225、L249 | 摘要/方法改为 shared failure-mode pairing；isomorphism 仅保留给 H 公式 |
| **P1** | Helmholtz 闭池缺口 | L68；References | 补池条目或降为有出处的二手转述 |
| **P1** | 公开文本 vs M4 可执行性 | L13、L197、L239 | 把 third-party recomputation 明确绑在机密通道/camera-ready |
| **P1** | 源层双盲 | T42 等；送审包 | 剥离 TeX 中文注释；CV 不入审或匿名化昵称路径 |
| **P2** | “reads zero” | L247 | 改为 undetectable at stated power |
| **P2** | independent rerun | L243 | 标明 in-team vs third-party |
| **P2** | CV 首现序 | C99 | 按 MD 重扫 |
| **P2** | 术语分流 | L134 / L200 | formula identity vs mapping analogy |

---

## 5. 总体判定

**建议级：Major Revision**

（若编辑认为映射表可在小修内改写、不要求新实验，可降为 Minor Revision；本审计按论文自设 kill line——“if any row's two ends fail to share form … the method claim weakens”——把 M4/isomorphism 计为必须改的方法主张，故维持 Major。）

**总评分（10 分制）**

| 分项 | 分 |
|---|---|
| 原创性 | 8 |
| 方法论 | 6 |
| 结果与论证 | 7 |
| 写作与一致性 | 8 |
| **综合** | **7.3** |

**给作者的建设性总评**

这是一篇在自我约束上远高于常见 position paper 的稿：D 的四词词典被执行，Channel III 主动降级 T，§7 把三次杀死、滤波不可分和功效上限当作资产写出，author-attested freeze 没有被包装成独立时间戳，master table 与分节评分一致，五锚在 md/tex/cv 三处计数闭合。这些不是装饰，是这篇稿真正可被引用的贡献。

需要改的是方法主张与证据的对齐，而且是你们自己写下的对齐标准。M4 左列（diegetic prototype）与右列（pre-registration）不共享形式；“structural isomorphism” 在公式同一、五行类比、Channel I 模式之间串用，摘要比 §6.2 的限定句更满。按 §6.4/§9.3，这应当削弱 method claim，而不是靠 “nothing stronger” 一句把摘要保住。Helmholtz 在 R2 已为 Riemann/Clifford 补锚的背景下仍无池号，是闭池协议的小缺口，补一条即可。双盲请按三层写：PDF 已盲；TeX 中文注释与编译记录里的工作流昵称是源层/可识别性层，不要用“无姓名 token”代替“不可识别”。

改完 M4 与术语、补 Helmholtz、把公开文本的可复算边界写进映射表，这篇稿的核心装置（三检查、两层级、负面结果、反向通道议程）是站得住的。不要再加普遍性或第二套 backbone；把现有 kill line 执行完，比再开一条 channel 更符合你们自己的论文。

---

## 重点议题（a–f）明确判断

**(a) Helmholtz 一手文本在文献池中的处置是否妥当？**  
**不妥当（🟡，非阻断）。** L68 将其与已入池的 Riemann [R53]、Clifford [R54] 并列为一手“physical speculation”，但闭池 54 条无 Helmholtz 题录，也无 T 检查所需的 primary-text 锚。Channel I 的 T 评分并不依赖该句（L88 只用 [R01]、[R02]），故不推翻 §2 结论，但违反自身“pool is closed / historical claims anchorable”协议。

**(b) §6 映射中 M4 行的范畴对应是否成立？**  
**不成立。** 左列是叙事人工物/diegetic prototype（[R32],[R33]），右列是预注册与第三方复算，失败模式“事后改规则”不能从左列单元格推出；且 M4 不在 §6.1 蒸馏的四条 hard 需求之内。

**(c) Channel III/§6 的 "structural isomorphism" 类措辞强度与证据是否匹配？**  
**Channel III 匹配，§6/摘要不匹配。** L134 “the same expression, H = -Σ p·log p … not a similar expression, the same one” 与证据同级；L13/L225 把五行类比称作 structurally isomorphic，被 M4 与“not an equivalence theorem”（L200）同时削弱。

**(d) TeX 源中文注释与编译记录工作流昵称的双盲影响？**  
**分层：渲染层 PASS；源层 GRAY；可识别性 GRAY。** PDF/作者栏：T63–T64 空，C53 CJK=0、/Author=""（渲染层）。源层：T42/T47/T56–T58 中文注释；CV C3/C8/C26「戴夫」「鲍勃」「查理」及中文路径。无姓名 token（D1 词表零命中）≠ 不可识别。若 CV 不入审稿包，影响限于 TeX 注释。

**(e) 讨论层对跨 backbone / 普遍性的表述是否超出证据？**  
**主表述未超出；局部修辞略超。** L249/L306 明确拒绝量级比较与 prevalence；§8 为议程。L247 “capability channel reads zero” 在已披露 ±10 pp 功效时过冲。

**(f) 预注册冻结的 "author-attested" 性质及其披露是否充分？**  
**披露充分（PASS），认识论地位仍弱于历史行（已在表中记录）。** L253/T340 与 L297 写明 digest 不能向非建造者证明 freeze 先于 runs；未把该锚写成 dictionary/primary-text 级。充分性不等于可独立核验（法证总表 #21）。