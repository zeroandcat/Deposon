# Reviewer A 独立评审原文（子代理评审）

- 通路代号：Ark-coding-plan
- 模型：doubao-seed-2-1-pro-260915
- 会话：单轮独立会话（不与 Reviewer B 共享任何上下文）
- 请求参数：temperature=0.4, max_tokens=16000, attempt=1, 耗时769.4s
- token 用量：prompt=51629, completion=26233
- finish_reason=stop

---

# 独立外审 Pass 1 四维审计报告

## 审计步骤

1. 以材料自带行号锁定证据：论文正文用 `Ln=`，TeX 源用 `Tn=`，编译记录用 `Cn=`。
2. 分别审计历史背景、方法论、创新归属、双盲文本与元数据。
3. 明确区分三层对象：渲染 PDF/PDF 元数据、TeX 源、仅供编译核验的审计记录。
4. 仅依据本次提供的材料判断，不引入外部事实。

---

## 维度1：背景

【结论】**GRAY**

### 【定位与证据】

1. **文献池总体封闭、可核查，且正文与参考文献一一对应**

   - L60：  
     > “The reference pool is closed: fifty-four items, cited by pool number [R01]–[R54]; fifty-two entries were verified against primary records, two ([R13], [R14]) carry unstable identifier snapshots…”
   - C54：  
     > “[PASS] C1-54条全列: References 列表 54 条；缺失=无 多余=无”
   - C55：  
     > “[PASS] C2-指针全覆盖: 正文引用 54/54；未在正文引用=无；正文有而未列=无”

2. **主要历史链条基本有锚点**

   - 非欧几何与相对论：L70 引用 Walter [R01]：  
     > “The scholarly record of how one such language was taken up by physics is documented in detail by Walter [R01].”
   - Einstein 对纯粹几何与应用几何的区分有参与者文本：L76：  
     > “Einstein's 1921 lecture ‘Geometry and Experience’, published the following year [R02], is the participant testimony for how the join was made…”
   - Brown–Norton 思想实验争论明确引用双方：L98：  
     > “On the realist side, Brown [R04] holds…”；“On the eliminativist side, Norton [R05] holds…”
   - 熵回路的 Shannon、Jaynes、Landauer 三个箭头分别有 [R09]、[R08]、[R10]，见 L128。
   - Contact–wormhole 链条同时有自我陈述与原始论文：L150：  
     > “the novelist's inquiry to a physicist … is the documented hinge of the case [R41], and the answer became the published analysis of traversable wormholes by Morris and Thorne [R11].”
   - 硬科幻标准来自参考工具书并承认定义困难：L184：  
     > “The same entry concedes that a rigorous definition of the category may be impossible [R37].”

3. **“形式小说”定义与 Riemann、Clifford 例证之间存在张力**

   - L68 一方面定义：  
     > “We use ‘formal fiction’ in exactly this sense — a self-consistent symbolic system with no intended physical referent at the time of its construction”
   - 同一段又引用 Riemann 与 Clifford 的明确物理思辨：  
     > Riemann “seeks the ground of spatial metric relations outside space, ‘in binding forces which act upon it’”；Clifford 提出空间曲率变化即 “‘what really happens in that phenomenon which we call the motion of matter’” [R54]。

4. **个别历史断言缺少池内直接引证**

   - L68 提到：  
     > “Helmholtz's public case for the empirical standing of geometrical axioms — remained speculation, never an adopted physical theory.”  
     该句未给 Helmholtz 对应参考文献。
   - L128 的关键年代判断：  
     > “Statistical mechanics had given entropy a statistical reading over microstates from its nineteenth-century foundations — roughly seventy years before the information-theoretic definition”  
     未引用十九世纪统计力学原始文献或通史文献；该判断又是 Channel III 的 T 检查降级依据，见 L140。
   - L156 声称：  
     > “the Oxford English Dictionary's earliest recorded attestation of robotics falls in Asimov's 1941 story ‘Liar!’ [R12].”  
     但 R12 条目中只有作品信息及括号说明，OED 本身未作为独立池条目出现，见 L331。

5. **两条文献识别信息尚未完成，但作者已主动标记**

   - L332：R13 标注 “[IDENTIFIER-PENDING]”。
   - L333：R14 标注 “[IDENTIFIER-PENDING]”。

6. **Channel III 的“进入工程”表述略有历史摩擦**

   - L126/L136 称抽象量 “travel into engineering”。
   - 但 R09 的出处本身是 L328：  
     > “C.E. Shannon, Bell Syst. Tech. J. 27:379–423, 1948”  
     即 Shannon 定义发表于工程技术期刊。论文真正能稳固支持的是“抽象量在工程中扩展并以可测代价返回物理”，而不是从工程领域之外“进入工程”。

### 【分析】

论文没有单设名为 “Background” 的第二节；实际 §2 是第一个历史案例，背景文献分布在 §1–§6。就材料本身看，文献池并非装饰：54 条文献全部进入正文，核心案例、争论双方和方法论来源均有引用，且作者反复限制主张强度，例如承认历史部分是 case studies rather than systematic history、不统计流行率、不断言反向通道存在。

但背景层仍有局部不严谨：

- “无预期物理指称对象”的定义与 Riemann、Clifford 明显的物理思辨意图存在张力。更稳妥的说法应是“形成时尚无被采纳的物理理论或经验协调”，而非完全“no intended physical referent”。
- Helmholtz、十九世纪统计力学、OED 词源记录三处直接断言缺少与作者自身锚点标准相匹配的引用。
- R13、R14 识别信息未完成虽已披露，但当前送审稿的可核验性仍不完整。

这些问题是局部补证和概念收紧问题，尚不足以否定全部历史叙述，因此判 **GRAY**，而非 FAIL。

---

## 维度2：方法

【结论】**GRAY**

### 【定位与证据】

1. **三检查与 D 的四档处置字典有明确规定**

   - L40：  
     > “**T (temporal priority).** The fictional input must precede the scientific use it is credited with…”
   - L41：  
     > “**D (dispensability).** An account of the same scientific development that omits the fictional input must be visibly less parsimonious.”
   - L42：  
     > “**R (operative residue).** The encounter must leave an operative residue — a vocabulary, a quantity, an agenda item, or a formal system…”
   - L44 明确区分：  
     > “**Partial pass**…”；“**Unresolved by design**…”；“**Indeterminate**…”；“**Out of scope**…”

2. **两层证据制度边界清楚**

   - L46：  
     > “Two evidence tiers appear in this paper and are never mixed.”  
     并区分 mixing 是证据权威借用，porting 是标准迁移。

3. **主表实际评分高度集中，通道之间并非都由三检查清楚分离**

   - Channel I：Pass / Partial pass / Pass，L293。
   - Channel II：Pass / Unresolved by design / Pass，L294。
   - Channel III：Scoped pass / Indeterminate / Pass，L295。
   - Channel IV：Pass / Indeterminate / Pass，L296。

4. **M4 与“硬科幻标准”的对应存在范畴错配**

   - L184 从硬科幻条目中提炼出的是四项：  
     > “internal consistency, no supernatural checks, continuity with known science, and checkability of the world's claims by observers inside the world.”
   - 但映射表有五行。M4 左侧为 L197：  
     > “Narrative artifacts can carry engineering commitments; the diegetic prototype has documented instances [R32], [R33]”
   - 其右侧则是：  
     > “Adjudication procedure pre-registered, recomputable by a third party…”
   - 共享失败模式为：  
     > “Changing the rules after the fact”

   左侧是叙事人工物影响工程实践的文献事实，并不是 R37 所定义的“硬”标准；它本身也不直接对应“事后改规则”。

5. **“结构同构”主张被作者主动弱化，但若干行仍更像定性类比**

   - L200：  
     > “The table claims structural isomorphism — row-by-row shared form and shared failure modes — and nothing stronger. It is not an equivalence theorem…”
   - M2 将“no supernatural checks”映射到 “No appeals to undelivered future capability”，L195。
   - M5 将虚构世界内部观察者可检查性映射到实验前定义 kill line，L198。两者都涉及可检验性，但作者权威、世界约束和外部实验反驳之间仍有重大语义差异。

6. **四阶段流水线规范清楚，但工程实例对“外部锚点”和第三方复核的满足是有限的**

   - L220 规范要求：  
     > “Product: a frozen adjudication function with an external anchor, fixed before any run.”
   - L223 要求：  
     > “the verdict function must be executable by a third party who did not build the system.”
   - §7 实际只有哈希前缀和作者方冻结协议：L237：  
     > “The adjudication layer is frozen before runs as pure verdict functions with published SHA-256 anchors, given as twelve-character prefixes…”
   - 作者明确承认公开文本不足以复核：L239：  
     > “A reviewer working from the public text alone therefore cannot execute the recomputation that M4 asks of a third party…”
   - L253 进一步承认：  
     > “this is an author-attested freeze… it buys verifiability, not independence.”

7. **通道类型存在潜在交叠**

   - L36 的 F-C4 要求新案例能无歧义分入四类：  
     > “If new cases cannot be classified without ambiguity into one of the four forms under the same three checks, the typology is ad hoc.”
   - 但 Contact/wormhole 案例始于叙事小说，最终产生可推导、可检验的物理论文，L150；它同时表现出 Channel IV 的议程设置和 Channel II 的可翻译性。
   - §7 的世界建构首先是 narrative setting，随后又成为 formal system，L233–L235。论文没有说明多标签情形如何处理。

### 【分析】

方法论的优点很突出：三检查有字典、D 的不同停止理由被区分、历史证据与预裁决证据不混用、反向通道被处理为可失败议程而非既成事实，§7 也完整披露负面结果。

但核心方法仍有三处保留：

1. **M4 不只是“弱化”问题，而是映射表的范畴问题。** 它来自 diegetic prototype 文献，不是硬科幻“硬度”标准；却被放入 M1–M5 的 hardness isomorphism 中。作者可将其改标为“流水线桥接条件”，或补充真正对应的硬科幻标准。
2. **“structural isomorphism”措辞偏强。** M1、M3 较稳，M2、M4、M5 更接近规范性类比。除非给出独立的相似性判分或编码程序，否则建议改为“qualitative operational mapping”。
3. **预注册实例的独立性不足。** SHA-256 能证明内容完整性，但若没有外部时间戳或第三方托管记录，单凭作者协议不能独立证明“冻结先于运行”。作者已诚实降级为 author-attested freeze，这是可信度问题上的重要自我限制。

此外，D 检查中的 “visibly less parsimonious” 没有形式化测度；不过作者通过四档处置承认其历史裁决力有限，因此不构成欺骗性缺陷。综合判 **GRAY**。

---

## 维度3：创新声明

【结论】**PASS**

### 【定位与证据】

1. **贡献排序克制，不把历史案例的广泛知识据为己有**

   - L58：  
     > “the apparatus (1) is what this paper would be missed for, while the channel readings (2) are its first application and are graded at the supply level by design — readings at that level are close to what the field already holds, and the paper asks to be credited with the checks that produced the grades, not with the sweep of the channels.”

2. **硬科幻标准的提炼与本文形式化之间归属清楚**

   - L184：  
     > “this paper distills four working demands for ‘hard’…”；“the distillation is this paper's, and the table below marks, row by row, which phrasings are the entry's record and which are this paper's formalization.”

3. **AI 侧标准的来源逐项交代**

   - L204：  
     > “of the AI-side criteria, only M2's no-future-capability demand restates a concern one of these sources states directly — the speculation critique of [R39] in criterion form.”
   - 同段：  
     > “The claim–evidence, anchoring, pre-registration, and kill-line criteria of rows M1, M3, M4, and M5 are this paper's formalization…”
   - 同段还说明：  
     > “M3's anchoring criterion claims no pool original; it is this paper's formalization outright.”

4. **方法原创物均有上游文献定位**

   - M1 的 claim–support 对应 Toulmin [R46]，L204。
   - M4 的预注册与复核分别引用 [R47]–[R50]，L197、L204。
   - M5 的可证伪性引用 Popper [R51] 与机器学习可证伪性研究 [R52]，L198、L204。

5. **新颖性声明受搜索时间和二次检查约束**

   - L60：  
     > “Uniqueness-flavored statements … are made strictly relative to our three-line search completed on 2026-09-16; a second-round novelty check is scheduled before submission…”
   - L212：  
     > “To the extent of our three-line search completed on 2026-09-16, the mapping has not been stated as a structural isomorphism with a portable pipeline…”

6. **匿名伴生研究的边界也有说明**

   - L202：  
     > “The row itself is this paper's formalization… what it inherits from the companion study is the freeze protocol and the recomputability standard…”
   - L279 再次说明审计词汇来自伴生研究，且自引已为双盲移除。

7. **工程实例和反向通道均无过度宣称**

   - L249：  
     > “its magnitude is not comparable to the non-Euclidean case, and nothing in this paper claims otherwise.”；“No uniqueness claim is made about the instance…”
   - L257：  
     > “This section is an open-question agenda. It is not an empirical claim, and it makes no prediction…”

### 【分析】

创新归属是全文处理最谨慎的部分。论文没有把硬科幻标准、Toulmin 论证结构、预注册、可复现性或 Popper 可证伪性冒充为新发明；它主张拥有的是组合性装置、四通道评分、映射表和流水线形式化。对最接近的 R42，也明确界定为互补而非竞争。

匿名伴生研究在盲审版本中无法由读者核验，这会影响 M4 来源的可审计性；但文本明确只继承 freeze protocol 与 recomputability standard，没有把伴生研究的全部成果据为己有。这是盲审造成的可验证性限制，不是归属不当。

维度2所指出的是映射是否足够成立的问题；维度3关注的是“谁提出了什么”，在该问题上本文边界清晰、无剽窃或过度让渡。判 **PASS**。

---

## 维度4：双盲合规

【结论】**GRAY**

> 说明：**渲染 PDF 与 PDF 元数据层面基本合规**；但按题面同时审计正式 TeX 源与编译记录，源注释和审计附件中存在 CJK/工作流昵称等卫生问题，因此整体给 GRAY，而非 FAIL。

### 【定位与证据】

| 检查项 | token / 字段 | 命中情况与定位 | 判断 |
|---|---|---|---|
| `\author{}` | 作者字段 | T63：`\author{}`；C68：“`\author{}`/`\date{}` 均空” | 未命中身份 |
| `\date{}` | 日期字段 | T64：`\date{}` | 未命中身份 |
| PDF author 元数据 | `/Author` | T43：`pdfauthor={}`；C69：“/Author=`""`” | 合规 |
| PDF 工具元数据 | Creator | C69：`Creator="LaTeX with hyperref"` | 通用工具链，无身份 |
| 标题元数据 | `/Title` | T43 仅含论文标题 | 不暴露作者 |
| 致谢/资助 | `acknowledg`, `funded by`, `grant no` | C113：tex 全文零命中；C68：“无致谢节” | 未命中 |
| ORCID/GitHub | `orcid`, `github` | C113：零命中 | 未命中 |
| 邮箱 | 邮箱模式 | C72：“全文邮箱=无”；C119：“全文邮箱零命中” | 未命中 |
| 指定身份 token | `deposon`, `keep-the-books`, `zhipu`, `智谱`, `清言`, `〔用户U〕`, `〔用户U〕` | C53、C113 均为 0 | 未命中 |
| 自引 | companion study | T287、T366：`[self-citation removed for double-blind review; restored at camera-ready]` | 已匿名 |
| 工程项目名 | project/entity name | T316：项目名、虚构实体名、basename 中项目 token 已匿名；结果路径使用 `anon`，T326 | 基本合规 |
| 残留项目缩写 | `GT` | T324 保留 `GT_FORMALIZATION_v1.md`、`run_v21_gtformal.py`、`SPEC_GT2B.md`、`SPEC_GT8C.md` | 低度残留风险 |
| PDF 批注/附件 | Annots | C70：“PDF 无注释/附件” | 合规 |
| PDF 文本层 CJK | 中/日/韩字符 | C71：“PDF 文本层 CJK 字符 0” | 渲染正文合规 |
| TeX 源注释 CJK | 中文注释 | T42、T47、T56–T58 含中文生产注释 | 源层卫生问题 |
| 编译记录 CJK/昵称 | `戴夫`、`鲍勃`、`查理` | C3、C8、C26 | 仅审计记录命中 |
| AI 工具披露 | `GLM` | T409：“The drafting model is GLM.” | 模型名，非作者身份 |

### 需特别说明的命中

1. **TeX 源中有中文注释，但不进入 PDF 文本层**

   - T42：  
     `% F8: \url 允许在连字符后断行（R37 长条目 Underfull 根因）`
   - T47：  
     `% F7: 节/小节标题 raggedright（标准惯例；仅换行标题受影响——消除 §8 两行标题的两端拉伸，字形零变化）`
   - T56–58 也有中文排版说明。

   这些注释不含姓名或机构，但如果 TeX 源直接提供给审稿人，会构成语言背景线索和内部生产流程线索。

2. **COMPILE_CV 含工作流昵称与中文文件路径，但编译记录声称它们未进入交付 PDF/TeX**

   - C3：`生成者：戴夫-格式专家`
   - C8：`shared/鲍勃_FTFB全稿R2修订版_2026-09-17.md`
   - C26：`查理_FTFB全稿文献合并版`
   - C24–25 声明 `'修订版说明'/'逐条对照表'/'META_REVIEW_REPORT'/'REVIEW_RB'/'编辑工件'` 在交付 tex/PDF 中零命中。

   因此这些是**审计附件层命中**，不是渲染论文命中；前提是 COMPILE_CV 不随送审论文发给审稿人。

3. **工程文件名中的 `GT` 未被匿名化**

   T324 保留多个 `GT` 标签。若 `GT` 是项目或虚构实体缩写，而非通用 “ground truth” 缩写，可能成为可识别 token。论文未解释其含义。

4. **参考文献中的人名不构成违规**

   Einstein、Thorne、Sagan、Popper 等均为正常被引文献作者；未发现未匿名的作者自引条目。

### 【分析】

就送审 PDF 而言，双盲处理相当完整：无作者块、无日期、无致谢、无资助、无邮箱、无 ORCID/GitHub、无 PDF author、无批注、无 CJK 渲染字符，自引也已整体移除。

但如果审计对象包括正式 TeX 源和编译附件，则有三项应清理：

1. 删除或英译 T42、T47、T56–T58 的中文源注释；
2. 确保 COMPILE_CV 仅由编辑/编译方留存，不进入审稿材料包；
3. 复核 `GT` 是否属于项目名，若是则替换或明确说明其为非识别性通用缩写。

这些问题不构成直接身份暴露，故不判 FAIL；但正式源文件中确有非正文 CJK 与内部痕迹，因此整体判 **GRAY**。

---

## 总评

### 总体印象

这是一篇方法论自觉度很高的跨学科位置论文。其最强项是：

- 主张层级克制，不断言小说为科学证据、不断言小说不可或缺、不断言反向通道已存在；
- 三检查、D 处置字典、历史层/预注册层的边界写得清楚；
- 创新归属与上游文献区分细致；
- 工程实例披露负面结果，没有用预注册形式包装成功学；
- 渲染 PDF 的双盲处理基本完整。

但当前版本仍需中修，主要问题不在写作或文献数量，而在若干核心概念与方法主张需要收紧。

### 完整问题清单

| 编号 | 严重度 | 问题 | 定位 | 建议 |
|---|---:|---|---|---|
| 1 | 中 | M4 左侧是 diegetic prototype 文献，不是硬科幻“硬度”标准；五行表与四项硬标准不完全对应 | L184、L197 | 将 M4 改标为桥接/流水线条件，或补充真正的硬科幻对应标准 |
| 2 | 中 | “structural isomorphism”对 M2、M4、M5 偏强，部分行更像定性类比 | L195、L197–L200 | 改为“qualitative operational mapping”，或给出独立相似性判准 |
| 3 | 中 | §7 的预注册缺少公开、独立时间戳；第三方复核仅通过保密通道 | L220、L237、L239、L253 | 提供外部托管时间戳，或将当前实例称为 internally frozen / author-attested freeze |
| 4 | 中 | “formal fiction”定义与 Riemann、Clifford 的物理思辨意图冲突 | L68 | 将“no intended physical referent”收紧为“no adopted physical application/empirical coordination” |
| 5 | 低-中 | 四通道存在交叠，缺少多标签或优先级规则；wormhole 与 §7 均可同时落入多类 | L36、L150、L233–L235、L293–L297 | 增加分类决策程序或允许主通道/次通道标签 |
| 6 | 低-中 | Helmholtz、十九世纪统计力学、OED 记录缺少直接池内锚点 | L68、L128、L156、L331 | 补原始/二手来源，或降低断言强度 |
| 7 | 低 | Shannon 量“进入工程”的表述与其发表于 Bell System Technical Journal 存在摩擦 | L126、L136、L328 | 改为“在工程中扩展并返回物理” |
| 8 | 低 | R13、R14 识别信息未完成 | L60、L332–L333 | 投稿前补全 DOI/NTRS/稳定 URL |
| 9 | 低 | D 检查的“parsimonious”无操作性测度 | L41、L44 | 可保持定性，但应更明确这是历史解释学比较而非形式测度 |
| 10 | 低 | F-C3 中 “systematically leave no kill line” 未规定数量、比例或领域范围 | L35、L275 | 在反向通道议程中设定最低样本或判定规则 |
| 11 | 低 | TeX 源含中文注释 | T42、T47、T56–T58 | 源文件送审前删除或英译 |
| 12 | 低 | 编译记录含 `戴夫`、`鲍勃`、`查理` 等工作流昵称 | C3、C8、C26 | 编译记录仅限编辑侧留存 |
| 13 | 低 | `GT` 系列文件名可能残留项目识别性 | T324 | 若为项目缩写则替换；若为 ground truth 则说明 |

### 最终分级

- **维度1 背景：GRAY**
- **维度2 方法：GRAY**
- **维度3 创新声明：PASS**
- **维度4 双盲合规：GRAY**

无一维构成 FAIL，但方法层的 M4 映射、预注册独立性，以及背景层的“形式小说”定义和补证问题，应在下一轮修订中优先处理。