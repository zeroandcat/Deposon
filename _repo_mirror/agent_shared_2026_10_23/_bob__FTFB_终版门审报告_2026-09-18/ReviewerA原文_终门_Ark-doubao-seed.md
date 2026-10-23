# Reviewer A 终门评审原文（arXiv 上传前最后一关）

- 通路代号：Ark-coding-plan
- 模型：doubao-seed-2-1-pro-260915
- 会话：单轮独立会话（不与 Reviewer B 共享任何上下文）
- 框架：沿 R2 增强评审框架；唯一框架性调整＝上传定位口径（实名上传，双盲维改为 anon 自洽＋token 零泄漏），已在提示词显式声明
- 请求参数：temperature=0.4, max_tokens=16000, attempt=1, 耗时431.1s
- token 用量：prompt=64497, completion=24988
- finish_reason=stop

---

# arXiv 上传前终门结构化学术审计报告
## 1. 总表
| 维度 | 判定 | 🔴Major 问题数 | 🟡Minor 问题数 |
|---|---|---|---|
| 维度一：背景与文献 | PASS | 0 | 0 |
| 维度二：方法与可证伪承诺 | PASS | 0 | 0 |
| 维度三：创新声明与归属 | PASS | 0 | 0 |
| 维度四：写作与内部一致性＋上传定位合规 | PASS | 0 | 2 |
| 总体 | PASS | 0 | 2 |

---

## 2. 逐维详审
### 维度一：背景与文献
【结论】PASS
【定位与证据】
1. 池闭合与计数规则：
   > L60: "The reference pool is closed: fifty-six items, cited by pool number [R01]–[R56]; pool numbers count entries, not works — [R12] carries two primary texts under one entry because they anchor the same lexical item. Fifty-three entries were verified against primary records, one ([R56]) is the authors' own companion study, anonymized for double-blind review (title, authors, and identifiers withheld, restored at camera-ready, offered to reviewers through the confidential channel declared in §7.1) and attested by its authors rather than independently verified, and two ([R13], [R14]) carry unstable identifier snapshots"
   > C32: "Reference pool itemized entries : 56"；C33: "Unique Rnn. labels in PDF text layer : 56"
2. Helmholtz R55 落版质量：
   > L68: "Helmholtz's public case for the empirical standing of geometrical axioms: on the empirical hypothesis, axioms "can be inferred from facts of experience and so established, or if, when tested by experience, they are perhaps to be rejected"; measurements that "confirm empirically the axiom of parallels" leave the measure of curvature of our space "thus far to be indistinguishable from zero," and whether it is exactly zero "remains, however, a question" [R55]"
   > L395: "R55. H. Helmholtz, "On the Origin and Significance of Geometrical Axioms" (lecture to the Docenten Verein, Heidelberg, 1870), in *Popular Lectures on Scientific Subjects*, Second Series, trans. E. Atkinson, London: Longmans, Green, and Co., 1908; full text: Project Gutenberg eBook no. 77725 (released 2026-01-17), retrieved and verified 2026-09-17."
3. 史学口径稳妥性：
   > L60: "Uniqueness-flavored statements — including the statement that no integrated treatment of the four channels exists — are made strictly relative to our three-line search, completed on 2026-09-16 and disclosed here: [...] The record's limits are inherited by every statement made relative to it: it is a single-engine, non-systematic sweep, not a multi-database survey, so the uniqueness statements say what this search returned, not what the literature at large contains."
   > L184: "The anthologies that frame the modern hard-SF canon [R36] exemplify the tradition these statements describe; their framing is used here as paraphrase, not quotation — the anthology's full text was not captured in the verification pass, so [R36] carries no direct quotation anywhere in this paper, and the limit is flagged rather than papered over."
【分析】
- 引用池完全闭合：R01–R56 连续无缺号，所有正文引用的池号均有对应条目，计数 56 与编译记录一致，「53 项原始验证+1 项作者自证+2 项待补标识符」的拆分逻辑自洽；
- R55 的直引内容与公开的 Atkinson 译本来源对应，题录信息完整、核验日期明确，落版质量符合要求；
- 所有史学断言均有对应锚点，唯一性声明严格限定在已完成的单引擎搜索范围内，未捕获的史料均如实标注，无超出证据支撑的断言，史学口径稳妥。

---

### 维度二：方法与可证伪承诺
【结论】PASS
【定位与证据】
1. 三检查与 D 处置字典：
   > L44: "The D check returns one of four dispositions, and the dictionary is stated once here so that every later table reads against it. **Partial pass**: the pool contains positive evidence of non-uniqueness, and the claim is downgraded to the supply level (Channel I). **Unresolved by design**: the check pits live positions against each other and the claim is worded to be invariant under either resolution (Channel II). **Indeterminate**: the pool contains no study that could run the check (Channels III and IV). **Out of scope**: the claim never invokes indispensability, so the check has no target (the §7 instance, whose claim rests on executability)."
2. F-C1–F-C4 操作化：
   > L33–36: 每条判死线均有明确 Operational reading（如 F-C1："Operational reading: for each pair of channel types, at least one scored flagship case must return a differing grade on at least one of T, D, or R; the condition triggers when some pair returns identical grade profiles across all scored flagship cases of both types."）
   > L310: "The falsifiability conditions are re-recorded here, in substance unchanged from §1.2, operational readings included."
3. M4 进口声明与 structural parallel 口径：
   > L184: "Row M4 is declared rather than smuggled in: the genre's distilled record contains no freeze-before-the-run demand, so M4's criterion is imported from the pre-registration and third-party-recomputation literature ([R47]–[R50]) rather than mapped from the genre, and the diegetic-prototype record ([R32], [R33]) is carried in that row as motivation, not as the criterion's source."
   > L200: "The table claims a constructed structural parallel — row-wise pairing of criteria with shared failure modes — and nothing stronger; the word isomorphism is reserved in this paper for the formula-level identity of Channel III, and no row-to-row isomorphism is claimed here."
4. 证据分档规则：
   > L46: "Two evidence tiers appear in this paper and are never mixed. [...] mixing would be an evidence operation — a historical claim borrowing the authority of an adjudication verdict, or a verdict product borrowing the authority of an anchor — and it never happens; porting, in §6 and §8, is a criteria operation — the checks and mapping rows are carried across tiers and re-instantiated at the receiving tier's own evidential grade, so the criteria travel while the evidence grades stay separate."
【分析】
- 三检查定义清晰，D 的四种处置字典明确，后续所有章节的评分均严格对应字典要求，无逻辑矛盾；
- 四条判死线均完成操作化，触发条件可被第三方直接验证，§9.3 的镜像内容与 §1.2 完全一致，符合预注册承诺；
- M4 行的进口来源、动机与判据的边界明确，无伪造流派来源的问题；映射的「constructed structural parallel」口径清晰，未夸大到等价定理或同构的程度；
- 历史证据层与预注册裁决层的边界明确，所有跨层操作均为准则移植，无证据权威混用的问题，方法框架的可证伪性完全达标。

---

### 维度三：创新声明与归属
【结论】PASS
【定位与证据】
1. 贡献声明：
   > L52–56: 明确列出五项贡献，每项均对应具体章节，且标注了证据等级（如第二项 "each channel an anchored application whose claims are stated at the supply level its checks support"）。
2. 让步与降级：
   > L21: "The reverse direction — machine worldviews feeding back into the sciences — is not asserted anywhere in this paper. It is set up as an open question with named criteria (§8)"
   > L225: "demonstrated on one artifact on the given benchmarks at the stated statistical power (§7.3), not as a general working methodology."
   > L239: "are offered to the editors and reviewers through a confidential channel [...] is not claimed to have occurred, and to date no independent party has executed the recomputation [...] M4's third-party recomputation is a standing demand rather than an executed fact"
   > L253: "The instance is therefore scored T as a provisional pass — the anchor is author-attested, of lesser independence than the historical rows, and not yet backed by a trusted time-stamp, a third-party archive, or any independent submission-time proof"
3. R56 归属边界：
   > L202: "cited here as the anonymized pool entry [R56]: [...] attested by the authors of this paper rather than independently verified (§1.3(ii)). The row itself is this paper's formalization, as the provenance note below states; its criteria stand on the open literature ([R47]–[R50]) with or without that entry, and what the entry supplies is a worked systematization of the freeze protocol and the recomputability standard, described here only to that extent."
【分析】
- 五项贡献声明均有对应内容支撑，未夸大研究的覆盖范围或强度；
- 所有可能涉及过度承诺的内容均完成降级：反向通道仅作为开放议程，未断言存在；工程方法仅限定为单工件演示，未推广为通用方法论；保密渠道仅声明 offer，未声称已被接收或执行；时间锚点明确为作者自证的临时通过，未借用独立锚点的权威性；
- R56 的归属边界清晰：明确为作者自有工作，仅提供流程的系统化演示，映射的核心判据均来自公开文献，未将未独立验证的 R56 内容作为核心学术支撑，不存在归属不清或剽窃问题。

---

### 维度四：写作与内部一致性＋上传定位合规
【结论】PASS
【定位与证据】
1. 术语一致性：
   全文除 §4 公式层面使用 "isomorphism" 外，所有跨领域比较的表述均统一为 "structural parallel"；"third party""independent" 等术语除一处内部核验表述外，均统一指外部独立主体；§7 的 "anon""GT" 术语均有明确范围说明。
2. 计数口径一致性：
   - 摘要字符数：> M16: "Length: 1849 characters / 266 words -- within the arXiv metadata 1920-character limit (margin 71)"，L13、T81、M12 的摘要内容逐字一致；
   - 池计数：正文 §1.3、§9.2、参考文献卷首均统一为 56 项，与编译记录一致；
   - 其他计数：> M7: "24 pages, 2 tables, no figures" 与 C10「24 pages」、论文实际内容一致；搜索查询数拆分 23+14+27=64，逻辑自洽。
3. §7 匿名机制自洽性：
   > L229: "The anonymization covers the project's name, the name of its fictitious entity, and the project-name tokens inside artifact basenames (replaced below by the marker "anon"); [...] The token "GT" that remains inside some artifact basenames below is the field-generic abbreviation of "ground truth," not a project-name token"
   §7 内所有项目名相关的基名均已替换为 anon，仅保留 GT 缩写，与声明范围完全一致。
4. 工作流 token 零泄漏：
   > C36: "Workflow/identity tokens (internal list, not reproduced): 0 hits"
   PAPER_TEX、COMPILE_CV、METADATA 中均无内部昵称、本地路径、团队工件名、评审平台代号等泄漏内容；仅有的作者实名、GLM 起草模型披露均为合规内容。
【分析】
- 核心术语使用基本统一，仅存在一处 "independent rerun" 的表述易与外部独立主体混淆，属于微小笔误；
- 所有核心计数口径（池数、页数、表数、搜索拆分）均互证一致，摘要内容在正文、TeX 源、元数据中完全统一；仅作者自行列出的分句字符数累加与总字符数存在 4 的偏差，属于不影响合规的计数笔误；
- §7 的匿名化机制声明与实际落版内容完全一致，GT 的边界说明清晰，不存在匿名范围不符的问题；
- 所有上传材料中无工作流内部 token 泄漏，实名作者、公开元数据均符合 arXiv 实名上传的定位要求，无合规问题。

---

## 3. R1+R2 合并清单 18 项逐项验收表
| 项号 | 验收结论 | 证据 |
|---|---|---|
| ① | 已落实 | PAPER_MD L60 明确池计数为 56、R56 为匿名自引条目；L202 标注 R56 池号；L396 有对应条目；COMPILE_CV C32-C33 验证池条目共 56，池闭合与计数更新完成。 |
| ② | 已落实 | PAPER_MD L184 明确 M4 判据进口自预注册文献、而非映射自硬科幻流派；L197 M4 左右格分别标注 "imported, not mapped""an import per the left cell"，来源边界清晰。 |
| ③ | 已落实 | 全文仅 §4 公式层面使用 "isomorphism"，其余所有跨领域比较均统一为 "structural parallel"，L200 明确保留 isomorphism 用法的范围，降级全部完成。 |
| ④ | 已落实 | PAPER_MD L239 明确保密渠道为 "offered" 而非已提供、无第三方独立复算、M4 复算为 standing demand；L13 摘要对应降格表述，边界明确。 |
| ⑤ | 已落实 | PAPER_MD L68 新增 Helmholtz 直引并标注 [R55]；L395 R55 题录完整、来源与核验日期清晰，一手入池完成。 |
| ⑥ | 已落实 | PAPER_MD L253 将 T 评分降级为 "provisional pass"，明确无第三方时间戳/存档证明；L297 总表对应更新；L237 将 "published SHA-256" 改为 "printed prefixes"，降级到位。 |
| ⑦ | 已落实 | PAPER_MD L60 完整披露三行搜索的 64 组查询构成、单引擎属性与局限；L212、L306 同步更新引用口径，协议公开完成。 |
| ⑧ | 已落实 | PAPER_MD L134 将熵公式表述更新为 "same functional form up to multiplicative constant and logarithm base"；L144 对应调整表述，口径校准完成。 |
| ⑨ | 已落实 | PAPER_MD L229 明确 GT 为 ground truth 通用缩写、不属于项目 token，不改名以避免破坏哈希锚点，范围澄清完成。 |
| ⑩ | 已落实 | PAPER_MD L33–36 每条 F-C 均补充操作化读法；L310 镜像内容与 §1.2 完全一致，阈值操作化完成。 |
| ⑪ | 已落实 | PAPER_MD L68 将 formal fiction 定义校准为「构造时未被任何物理理论采用/协调的自洽符号系统」，同时保留 Riemann 主动寻求物理应用的意图记录，口径校准完成。 |
| ⑫ | 已落实 | PAPER_MD L184 明确 R36 仅作为释义使用、无直接引语，如实标注全文未捕获的限制，表述合规。 |
| ⑬ | 已落实 | R13/R14 保留 [IDENTIFIER-PENDING] 标注，R42 无 DOI 如实标注，R53/R54 按捕获粒度落版，符合「宁缺毋滥」的声明。 |
| ⑭ | 已落实 | PAPER_MD L247 将 "reads zero" 改为 "shows no detectable difference at the stated power"；L225 将通用方法论主张收窄为单工件演示，收窄完成。 |
| ⑮ | 已落实 | PAPER_MD L60、L316 均明确「池号计条目而非作品，R12 含两个文本但仅占一个条目」的计数规则，说明到位。 |
| ⑯ | 已落实 | 摘要映射句的「constructed structural parallel」「one row an import」表述与 §6.2 口径完全一致；摘要末句的保密、临时评分表述与 §7.1 对齐，口径统一。 |
| ⑰ | 已落实 | PAPER_MD L312 完整披露 GLM 的使用范围、AI 参与的所有环节，明确作者承担全部责任，披露如实完整。 |
| ⑱ | 已落实 | PAPER_MD L13 摘要首句与 L27 §1.2 核心主张逐字完全一致，修订说明确认脚本验证通过，一致性达标。 |

---

## 4. 修订引入新问题专项扫描
### 4.1 摘要削减后主张与可证伪条件完整性
对照 R4 削减说明，削减严格执行「不动核心主张、三检验、可证伪条件、贡献声明」的要求：
- 首主张句逐字保留，与 §1.2 完全一致；
- 三检验表述、反向通道「未断言+议程化+判死线」的可证伪框架完整；
- 映射的进口声明、单工件限定、负面结果披露、保密渠道降格等核心内容均未缺失；
仅存在分句计数笔误，不影响核心内容完整性，无主张夸大问题。
### 4.2 R55/R56 入池后引用池闭合
- 池号 R01–R56 连续无缺号，所有正文引用均有对应条目，无断号、错引；
- 池计数 56 在所有材料中完全统一，验证状态拆分逻辑自洽；
- R55/R56 的引用位置与条目标注的适用章节完全对应，无错配；
引用池完全闭合，计数口径无冲突。
### 4.3 信息行落版一致性
逐字段核对所有公开元数据：标题、作者、主题分类、许可证、页数/表数/图数、利益冲突、日期均在 METADATA、论文正文、编译记录中完全匹配，无落版冲突。
### 4.4 B01 修复后源层卫生
- 无内部昵称、本地路径、团队工件号、内部评审代号等敏感 token 泄漏，GLM 为公开的模型披露，不属于内部敏感信息；
- TeX 注释仅保留通用排版修复标记，无内部修订流程的敏感痕迹；编译记录为中性公开版本；
- R56 的匿名状态为作者主动声明的 camera-ready 前保留，符合其配套工作可能在双盲评审的实际场景，不属于卫生问题；
源层卫生完全符合要求。

---

## 5. 问题清单
### 阻断级（上传前必须解决）
无。
### 🔴 Major 问题
无。
### 🟡 Minor 问题
1. **定位**：REVISION_NOTES N193
   **证据**：原文记载「后 **1849**（分句实测 375＋52＋440＋549＋117＋312）」，材料内可复算分句累加值为 1845，与总字符数声明相差 4，为作者计数笔误，不影响摘要合规性（实际字符仍远低于 1920 上限）。
   **修改建议**：调整分句统计值（如将最后一个分句的 312 修正为 316），或直接删除分句计数的冗余表述。
2. **定位**：PAPER_MD L243（PAPER_TEX T339）
   **证据**：原文表述为 "At the audit level, an independent rerun passed with bit-identical recomputation [...] — the books were not merely kept but re-kept by a second pair of hands." 全文其他语境下的 "independent" 均指独立于作者团队的外部主体，此处核验实际为团队内部未参与原开发的成员完成的审计，术语使用易引发「已完成外部独立验证」的误解。
   **修改建议**：将 "an independent rerun" 修改为 "an internal independent rerun by a team member uninvolved in the original build"，明确区分内部核验与外部复算。

---

## 6. 终门判定
### 判据核对
1. P0 残留：R2 原 P0 四项要求（源层卫生、自引占位修复、M4 重写与 isomorphism 降级、保密记录降格）均 100% 闭环，无 P0 残留；
2. R2 Major 闭环：所有 R2 提出的 Major 问题均已修复，唯一挂限项为第二轮查新，作者已明确将所有唯一性声明严格限定在已完成的三行搜索范围内，如实披露了挂限状态，符合「如实挂限」要求；
3. 新增阻断问题：本次修订未引入任何阻断级硬伤，仅有的 2 项 Minor 问题不影响核心学术内容与合规性。
### 终判：**PASS**
Minor 问题可在后续 camera-ready 版本修正，不阻塞本次 arXiv 实名上传。

---

## 7. 总体判定
### 建议级：Accept（同意直接上传 arXiv）
### 评分（10 分制）
| 维度 | 得分 |
|---|---|
| 原创性 | 8/10 |
| 方法论 | 9/10 |
| 结果与论证 | 8/10 |
| 写作与一致性 | 8/10 |
### 总评
这是一篇元自反性极强、学术约束极为规范的跨学科位置论文，核心贡献是整合提出了可操作、可证伪的小说向精确科学输入的三检查评估框架与四通道类型学，构建了硬科幻准则到 AI 研究主张裁决的结构化映射，并通过 4 个锚定充分的历史案例与 1 个完整披露负面结果的中等级工程案例完成了框架的端到端演示。全文所有可能涉及过度承诺的主张均主动降级，未验证的史料、未完成的查新、未公开的工件均如实挂限，无夸大、无剽窃、无合规硬伤，完全符合 arXiv 实名预印本的上传要求，仅有的两处微小笔误不影响核心价值，建议直接通过终门验收。