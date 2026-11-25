# FTFB × WORLDVIEW 比对备忘（2026-09-18）

撰写：查理-论文主笔。派单：群管理员 2026-09-18 17:51。纪律执行情况：两件对象文件只读零改动（本备忘为唯一新增文件）；全部判断基于文本实证、逐条可回锚；WORLDVIEW 中查不到对应的内容一律标「无对应」。

## 〇、对象与指纹（核验记录）

| 对象 | 位置 | 规模 | 指纹 |
|---|---|---|---|
| FTFB R3 返修稿 | shared/查理_FTFB_R3返修稿_2026-09-18.tex | 606 行 / 98,972 B | SHA-256 前 12 位 `51f4e0c8a0f8`；与 戴夫_FTFB_R3排版重打包_2026-09-18/fiction_that_feeds_back.tex **逐字节同哈希**（同源确认，非近似） |
| FTFB 元数据 | 同重打包目录 arxiv_metadata.txt | 45 行 | 题名 *Fiction That Feeds Back: From Non-Euclidean Geometry to Machine Worldviews*；作者 Qihao Yuan；cs.AI(primary)·physics.hist-ph·cs.CY；CC BY 4.0；24 页；摘要 1846 字符 |
| WORLDVIEW | shared/WORLDVIEW_GEOMETRY_LOOP_2026_github_fetch.md | 85 行 / 10,327 B | SHA-256 前 12 位 `1568b3dfe5ae`（与派单所报一致）；**正文无署名作者**（文本实证，全文无作者行/署名标记） |

下文锚记：F=L** 为 FTFB tex 行号（两份同源 tex 行号一致）；W=L** 为 WORLDVIEW 行号。

## 一、定位与体裁（维度①）

- **体裁自declare**：F 摘要 L75 "This position paper"，§1.3(i) L132 "a position paper with an intellectual-historical core; its historical sections are case studies, not a systematic history"。W L5 "本文是立场声明（position statement），不是经验论文"。→ 两文**都自我定位为立场文体**，差异在 F 立场之下挂了硬证据装置（56 条闭池、两级证据 tier、字段路径表），W 立场之下只挂两个事实锚（arXiv 号＋仓库，W L82–85）。
- **claim 类型**：F 的 claim 是判据化的（thesis 句 L91 以三查/四通道/可证伪条件框死，F-C1–F-C4 L97–102 附操作化读法，且明言 "claims re-examinability for its historical claims and falsifiability only for its pre-registered ones" L93）。W 的 claim 是宣言化的（L17 命题句无操作化读法；判死线 L66–68 只有触发条件描述，无样本量/计数规则/裁决协议前置——对照 F F-C3 的操作化标准 L100 "in every case of a sample whose size, source, and counting rule are fixed in the adjudication protocol before the run"）。
- **判死口径**：F 是协议级（冻结判据＋第三方可执行，L315 "the kill line must be defined before the experiment runs"）；W 是立场级（L64 "我们照 deposon 的规矩，给回路命题本身登记判死线"，但未给三条线配裁决协议）。**呼应点**：两文都把「为自己配判死线」当作立场文体的资格条件——F L§9.3 "A paper about kill lines that withheld its own would fail M5"；W L64 "一个立场声明若不为自己配置判死标准，就只是修辞"。
- **匿名策略**：F §7 实例全匿名（L330 "identity is anonymized in this edition"，public pointer deferred，L494 availability terms）＋R56 匿名（L132/L573）。W 反向：点名 deposon、arXiv:2609.09001、GitHub 仓库（W L51/L82/L85）。

## 二、重叠清单（维度②＋③一致项＋④重叠）

1. **双向回路命题家族**。F L85 "a two-way loop between fiction and the exact sciences… the reverse direction — machine worldviews feeding back into the sciences — is not asserted"；W L17 命题句。两文都主张「虚构/世界观 ↔ 科学·AI」双向，且**都拒绝断言反向已成立**（F L93；W L47 "实例数为零"）。
2. **非欧几何先例与「形式在先」次序**。F L140–144（Riemann/Clifford/Helmholtz 引文链 [R53]–[R55]；L142 "the physics arrived later and found the language available"；L144 "the language precedes the empirical joining"）；W L23–27（想象→建构→征用三步；L25 明写"第三步才是**征用**：近一个世纪后，爱因斯坦在广义相对论中让物理空间实际住进了非欧几何"）。次序结构同构；**人物线不同**：F 走 Riemann–Clifford–Helmholtz–Walter–Einstein(1921 讲座 [R02])，W 走罗巴切夫斯基/鲍耶→爱因斯坦（grep 证 F 全文无 "Lobachevsky/Bolyai/罗巴切夫斯基"，NONE）。
3. **「价值不依赖征用」**。W L27 "罗巴切夫斯基空间在被爱因斯坦采用之前，就已经是有尊严的数学……探索价值不依赖征用结果——这是本文全部论证的地基"；F L162 "available, adopted, and consequential — not indispensable"（D 检查降级到 supply 层）。功能同构（都把价值/主张从「被采用」上解耦），表述语域不同（尊严/价值 vs supply-level 纪律）。
4. **硬科幻＝公理纪律、账必须对平**。W L33 "给一组散射过程配上守恒账，每一笔能量收支都必须对平——这就是 deposon 的设定方式"、L35 "设定是公理而非装饰，推论必须闭合，不允许在情节需要时偷偷改账"；F §6 映射表 M1 "Internal consistency: the world's books run no deficit"（表在 F L286–300 区段）＋§7 S 阶段 L336（守恒 bookkeeping identity）。「books/账本」意象两文同源。
5. **预登记判死协议（不许挪门柱）**。W L55 "先登记判死标准，再跑实验，不允许事后挪动球门"；F §6.4 P 阶段 L313（frozen adjudication function with SHA-256 anchors）＋L315 kill line 前定义。概念同构；F 侧有工程实现（5 个 SHA-256 锚前缀表，F L344–360 区段 Table tab:anchors），W 侧无对应。
6. **自我判死（立场文体自己挂判死线）**。F F-C1–F-C4（L97–102）＋§9.3 复录；W 三条回路判死线（L66–68）。结构呼应（都自我登记判死线），内容不同（F 打在类型学/通道/反向渠道上；W 打在十年追溯/可居住率/穷举新颖性上——F 无时间盒判死线，grep "decade/ten year" NONE）。
7. **反向腿零实例、如实标注**。F L93 "we do not claim that the reverse channel exists"；§8.3 declaration sentence。W L47 "反向……目前实例数为零——尚未有任何虚构世界观公理变体被征用进 AI 表征或度量……一条腿实证＋一条腿宣言"。
8. **阴性结果即资产；存活可信因为同协议杀了其余**。W L5 "所有阴性结果照实呈现，不做任何拔高"、L60 "这些阴性结果不削弱实例的地位，反而是它的核心证据……deposon 的守恒账之所以可信，恰恰因为同一协议杀死了它的动力学等价部分"；F L381 "Negative results are disclosed here as assets"＋"Because verdict functions are frozen before their runs, the conservation pass and the dynamical kills stand at the same freeze level, and the pass cannot be read as the product of a lenient protocol"。**这是两文最深的论证同构句对**（措辞不同）。
9. **同一工程实例（共享判死指纹）**。F §7 匿名实例 ≡ W §五 deposon（arXiv:2609.09001）。指纹证据：0.8569、min cos −1.0、τ∈[0,4] 81 档、2.2e-16、T+R+A=1、P1a/P1b/T-P1c、E9.5 打平、E9.6 阴性，逐项见下表。
10. **W 的「可居住」定义与 F 的正结果要素(iii)呼应**。W L37 "一个公理变体可居住 := 它的至少一条推论在预登记判死协议下存活"；F §8.3 L431 区段正结果四要素之 (iii) "it survives a pre-registered kill attempt"。核心判定同构；F 无「可居住/住进现实」术语（无对应）。

### 事实一致性逐项对账（维度③，两文共享事实主张）

| 事实项 | WORLDVIEW（锚） | FTFB（锚） | 判定 |
|---|---|---|---|
| 守恒账闭合精度 | "机器精度 2.2e-16"（L57、L83） | "2.220446049250313×10⁻¹⁶ — the scale of double-precision machine epsilon, against an implementation tolerance of 10⁻⁶"（F L349） | **一致**（W 为截断表示；W 未提容差 10⁻⁶，单方省略非冲突） |
| P1a 死因 | "O(1) 偏差（max dev = 0.8569）"（L58、L84） | "P1a: maximum deviation 0.8569, an O(1) gap that does not vanish with step size"（F L355） | **一致** |
| P1b 死因 | "穷举集上的过冲（min cos = −1.0，方向完全相反）"，标签 "P1b"（L58、L84） | "T-P1b: minimum directional cosine −1.0"（F L355） | **一致**；标签差：W 写 P1b、F 写 T-P1b |
| T-P1c 死因 | "τ∈[0,4] 的 81 档扫描仅对应 T-P1c 的判死，无任何拯救余地"（L58、L84） | "an 81-point grid over τ∈[0,4] reaches minimum cosine −1.0 at the best global τ, the per-state optimal τ∗ again reaches −1.0, and the per-state τ∗ median is 0"（F L355） | **一致**（F 多给 τ∗ 中位数 0） |
| E9.5 六关键词基线 | "E9.5 与提案方法打平"（L60、L83） | "a trivial six-keyword rule filter… 0.87 against 0.85 (McNemar p=0.5), on StrategyQA 0.899 against 0.899 (p=1.0)"（F L387） | **一致**（W 无数字） |
| E9.6 融合稀释 | "E9.6 为阴性"（L60、L83） | "Fusion with a semantic prior dilutes rather than helps: physics 0.484→0.452 and historical 0.783→0.739 at the λ=0.5"（F L387） | **一致** |
| E9.4 等权对照 | 两处列名（L60、L83）**均未给结果** | **全文无对应**（grep 证：tex 中 "E9" 仅出现于字段路径 `E9_5_power_honest`，F L396 表行） | **单方缺失＋单方未报结果**（见差异清单 D-8） |
| 实例角色定位 | "deposon 实例化的是中间环节——对虚构几何执行可居住性检验——而非反向的完成"（L47）；"正向已可由 deposon 式工序展示"（L47） | 实例＝四段流水线端到端执行（F Method claim L317 "demonstrated on one artifact on the given benchmarks at the stated statistical power"） | **不矛盾**（同一实例在两文各自框架中角色不同：回路中间环节 vs 流水线实例） |
| 预登记属性 | "预登记判死协议"（L55） | 冻结裁决函数＋SHA-256 锚（F L344–360）＋T 为 provisional pass（作者自证冻结，F L405–410 §7.4 与 Appendix "Anchor standing"） | **一致**；F 更细（披露了锚的独立性局限，W 无对应） |

**冲突判定：两文共享的全部事实性数字与判死叙述，无一例数值或口径冲突。** W 对 deposon 的关系表述与 F 自身内容在事实层自洽；W 补充的词源/史前史/仓库/arXiv 号（L53、L85、L82）在 F 中因匿名化设计而无对应，属披露策略差异而非矛盾。

## 三、冲突清单（严格意义：零事实冲突；以下为措辞级张力，需校准）

1. **首例性强度不对齐**。W L5/L11/L51 三处称 deposon 为 "the first complete instance / 第一个完整实例 / 首个完整实例"，收束 L76 "第一株有产量记录的作物"；F L404–405 "no uniqueness claim is made about the instance — the positioning is exactly 'engineering-grade, mid-strength'"。F 侧明示弃权首例性，W 侧断言首例性。对象虽不同（回路实例 vs 流水线实例），并读时同一实例一边 "first" 一边 "no firstness claim"，**需校准**。
2. **「同构」用词**。W L60 "与非欧几何的命运**同构**"；F §6.2（表后段）"``isomorphism'' is reserved for the formula-level identity of Channel III, and no row-to-row isomorphism is claimed here"＋§7.3(ii) "runs structurally parallel to the Channel I pattern — but its magnitude is not comparable to the non-Euclidean case, and nothing in this paper claims otherwise"。W 用「同构」处 F 刻意降格为「结构平行＋量级不可比」。**需校准**（建议 W 改「结构平行/命运相似」或加量级限定）。
3. **「可直接征用」vs「尚未被征用」**。W L83 "构成**可直接征用**的正证据"；F §7.3(iii) "third-party adoption of the formal language by a community that did not build it; **that adoption has not occurred**"。逻辑上不矛盾（可用性≠已用性），并列呈现时强度观感不一致。**建议统一为「可征用但尚未被征用」式表述**。
4. **「承载真实的计算过程」易误读为能力主张**。W L57 "这组虚构的守恒律被证明可以承载真实的计算过程"；F §7.3(i) L387 "the capability channel shows no detectable difference at the stated power… indistinguishable from a trivial six-keyword rule filter"。按 W 自身可居住定义（L37 "可居住的推论进入了真实计算过程"）应读作「账本在真实计算过程中成立」＝F 的审计通道口径；但 W 该句未带能力通道限定（E9.5 打平在同段 L60 才出现）。**易误读措辞，建议加限定**。
5. **数字精度口径**。W "2.2e-16"（两处）vs F 冻结记录全精度 2.220446049250313×10⁻¹⁶。非冲突，但 W 若要与之引用的 arXiv:2609.09001 及 F 侧冻结口径对表，建议升全精度或注明截断。

## 四、差异清单（维度⑤：单方持有主张）

**仅 FTFB 有（WORLDVIEW 无对应）：**
- D-1 四通道类型学（formal/controlled/quantitative/narrative）与 T/D/R 三查＋D 的四档处置字典（F L106–116）。
- D-2 56 条闭池、逐条核验记录、两级证据 tier 与 mixing/porting 边界（F L114、L132、Appendix L486）。W 无参考文献装置。
- D-3 M1–M5 映射表（含 M4 import 声明与逐行 failure-mode 配对）与 S/F/P/E 四段流水线（F §6）。W 只到「变换公理＋严格推演」的一般方法论，无映射、无 failure mode。
- D-4 实例的完整工程证据链：5 个 SHA-256 锚前缀、字段路径索引表、61 图/6,760 态穷举范围、ECR 中位数 4/3 与 20/22 覆盖、势博弈降级 0.669、CoT 0.97 vs 0.85、±10pp 功效声明、第三方重算记录 `879db0217f04`（F L344–400）。W 全部无对应（只有摘要级数字）。
- D-5 反向渠道的可操作裁决议程：freezable/anchored/killable 三条件、正结果四要素 (i)–(iv)、F-C3 操作化读法（F §8.3）。W 的反向腿只有先例论证＋宣言。
- D-6 AI 披露段（GLM 起草、机器评审多轮、机器第三方重算，F §9.3 末 "The drafting model is GLM…"）。W 无对应。
- D-7 历史案例链：思想实验 Brown/Norton、熵 Shannon/Jaynes/Landauer、虫洞 Sagan/Thorne、robot/singularity 词汇锚（F §3–§5）。W 无对应。

**仅 WORLDVIEW 有（FTFB 无对应）：**
- D-8 E9.4 等权对照的**存在本身**（W L60、L83 列名；F 全文缺席——但注意 W 亦未报其结果，两文各缺一半：F 缺条目，W 缺结论）。
- D-9 「世界观-几何回路」命名与 AI↔硬科幻 的方向定义：W 正向＝AI→硬科幻（批量生成/一致性检查/穷举搜索，"科幻的供给侧被改变了" L41）；F 正向＝fiction→science 四通道。两文回路方向集合不同，仅「虚构/世界观→科学·AI」一向重叠；且 F 反向目标 "the sciences"（F L85）宽于 W 的 "AI 的认知与表征空间"（W L17）。
- D-10 罗巴切夫斯基/鲍耶点名与「想象→建构→征用」三步命名法（W L23–25；F grep 证 NONE）。
- D-11 「可能性空间的几何学」「硬科幻是 AI 的几何学预科」「实验田/播种/绝收/称重」隐喻系统（W L29–35、L45、L76）。
- D-12 「可居住」操作定义与「住进现实」术语（W L37）。F 最近概念是 R residue 与 §8.3(iii)，但无该术语。
- D-13 LLM 推理路径本体论刻画（"高维、离散、带耗散、无度量"）与「信息几何/transformer 表征几何只度量既有表征、缺为耗散离散路径发明新本体的方法论缺口」论证（W L43）。F 无对应（F §8.1 走 world-model 文献线 [R16]–[R22]，grep "information geometry/metricless" NONE；注意 F 的 "dissipation" 仅出现于 §7 三通道能量律的 A 通道，与 W 的「带耗散推理路径」是不同概念，勿混）。
- D-14 三条回路判死线：十年追溯线、可居住率线、穷举新颖性线（W L66–68）。
- D-15 deposon 词源（源自 deposition）与仿生→仿物理「公理切换」史前史（W L53）。F 匿名化，无对应（by design）。
- D-16 公开指针：GitHub 仓库 github.com/zeroandcat/Deposon（W L85）。F public pointer deferred（F L494）。

**分工边界评估**：总体清晰——F＝判据装置＋带证据链的实例（协议级）；W＝回路命题宣言（立场级）。两文在「非欧先例、公理纪律、预登记判死、自我判死、阴性即资产」五处共享骨架，但 F 侧始终是这些概念的**操作化版本**，W 侧是**宣言版本**，未见同一主张以同等强度重复占位。需要互相校准的措辞即冲突清单 1–5。

## 五、风险清单（维度④：文本/引用重叠与披露风险）

1. **引用交集＝空集**。W 的引用面仅有 arXiv:2609.09001＋GitHub 仓库（W L82、L85），无参考文献列表；F 为 56 条闭池 [R01]–[R56]。**零重合**。注意结构性原因：W 所引的 2609.09001 正是 F §7 匿名实例本身——F 不能在不破匿名的条件下把它入池（当前以正文对象处理而非引文），故此空集是设计结果而非巧合。
2. **措辞级逐字重合：未发现**。两文主体语言不同（F 英文，W 中文＋英文摘要）；最接近的平行句对（W L60 ↔ F L381 同构论证句；W EN 摘要 L11 "its conservation ledger survived a pre-registered falsification protocol while its dynamical-equivalence part was killed" ↔ F §7 "The conservation identity survives audit… The dynamical tier dies"）均为同义异词。
3. **查重/自我重叠风险（若两文同上 arXiv 或同作者公开）**：风险不在文本而在**骨架与指纹**——共享的非欧先例论证骨架＋同一实例的全部判死指纹数字（0.8569 / −1.0 / 81 档 / 2.2e-16 / E9.5 / E9.6）。文本相似度工具对数字指纹串敏感，同作者两文会被判「未披露自我重叠」。**证据边界（零推断）**：W 正文未署作者，无法从文本确证两文作者关系；F 署名 Qihao Yuan，且 F 的 R56 匿名条目为 "authors' companion study"，W 并非 R56（W 未提 Keep the Books survey，R56 是另一件）。W 的 GitHub 公开时间在拉取文本中无记载，无法与 F 的池截止（2026-09-16 三线检索，F Appendix）排先后。
4. **自引披露建议**：(a) 若两文同作者，W 应在性质声明或事实锚处加引 FTFB 并披露两文关系（判据版/宣言版分工）；F 在 revised version 恢复实例身份时，应把 W 纳入相关工作定位——特别因为 F 的最近邻论述只有 [R42]（F L132 "The closest dialogue partner that search returned [R42]"），而 W 是一个比 [R42] 更近的同骨架立场文本；F 的 novelty 声明均以 2026-09-16 三线检索为界（F Appendix），W 若在此之前已公开，则该论述需补 W 的定位。(b) 若不同作者，两文的骨架重叠将构成**优先权问题**而非自引问题，更需要互引与分工声明。
5. **匿名连坐风险（最实质的一项）**：F §7 实例匿名化（"to be restored in a revised version"，F L330）的实效会被 W 的公开存在直接击穿——W 点名 deposon＋arXiv:2609.09001＋仓库，且其判死数字与 F §7 逐项相同。任何同时读到两文的读者（包括双盲审稿人）可用 0.8569/−1.0/81 档/E9.5/E9.6 指纹唯一反查 F §7 实例＝deposon＝公开作者的项目，进而绕过 F 的作者匿名（若投双盲评审版）。R56 匿名条目不受影响（W 未提该 survey）。**建议**：F 投双盲评审版本前，评估 W 的公开时间与可检索性；或在 W 侧对实例描述做降指纹处理——后者涉及 W 改动，超出本备忘权限，仅提示给管理员裁量。
6. **元数据一致性**：F 的 arxiv_metadata.txt 与 tex 内部声明（题名/作者/subjects/license/日期，tex L43、L60–67 vs metadata 全字段）逐项一致，无内部冲突；W 无元数据装置（GitHub fetch 文档），无对应可比项。

## 六、结论

1. **事实层零冲突**：两文共享的 deposon 判死叙述（守恒 2.2e-16 存活、P1a 0.8569、P1b −1.0、T-P1c 81 档、E9.5 打平、E9.6 阴性）逐项对账一致；唯一的不对称是 E9.4（W 列名不报果，F 全文缺席）与精度截断（2.2e-16）。
2. **概念层高度重叠、强度分层**：五处共享骨架（非欧先例、公理纪律、预登记判死、自我判死、阴性即资产）在 F 侧均为操作化/协议化版本，在 W 侧为宣言版本；未发现同一主张以同等强度在两文重复占位。
3. **文本层零逐字重合、引用层零交集**；查重风险集中在骨架＋数字指纹，而非文本拷贝。
4. **分工边界总体清晰**（判据装置＋证据链实例 vs 回路命题宣言），但有 5 处措辞需校准：首例性、「同构」、「可直接征用」、「承载真实的计算过程」、数字精度。
5. **最实质的风险是披露策略而非学术内容**：互不引用的同骨架两文＋W 公开实例身份，会连坐削弱 F §7 匿名化的实效，并在同作者情形下构成未披露自我重叠。建议的管理动作：(a) 校准上列 5 处措辞；(b) 在 F revised version 与 W 之间建立互引/分工声明；(c) F 投双盲版前专项评估 W 的公开时间与指纹暴露面。

（本备忘基于两件对象文件的全文通读＋grep 机械核验；所有「无对应」结论均有检索记录支撑：FTFB 侧 Lobachevsky/Bolyai/NONE、E9.4/NONE、2609.09001/NONE、deposon/NONE、information geometry/NONE、decade/NONE；WORLDVIEW 侧 FTFB 提及/NONE、署名/NONE、E9.4 结果/未报。）
