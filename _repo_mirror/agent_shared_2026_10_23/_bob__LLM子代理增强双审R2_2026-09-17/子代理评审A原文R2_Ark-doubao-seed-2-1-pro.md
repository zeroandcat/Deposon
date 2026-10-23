# Reviewer A 增强框架评审原文（R2 轮子代理评审）

- 通路代号：Ark-coding-plan
- 模型：doubao-seed-2-1-pro-260915
- 会话：单轮独立会话（不与 Reviewer B 共享任何上下文；与 R1 轮会话亦无共享）
- 框架：KIMI/Coze 方法论＋联网所学（见《增强评审框架说明》）；材料/模型/参数与 R1 轮完全一致，框架为唯一变量
- 请求参数：temperature=0.4, max_tokens=16000, attempt=1, 耗时830.3s
- token 用量：prompt=52092, completion=29341
- finish_reason=stop

---

# 审稿人 A 结构化学术审计报告

## 1. 总表

| 维度 | 结论 | 问题计数 |
|---|---|---|
| 维度一：背景与文献 | GRAY | 🔴 Major 3；🟡 Minor 3 |
| 维度二：方法与可证伪承诺 | GRAY | 🔴 Major 6；🟡 Minor 4 |
| 维度三：创新声明与归属 | GRAY | 🔴 Major 1；🟡 Minor 1 |
| 维度四：写作、内部一致性与双盲合规 | FAIL | 🔴 Major 2（含阻断级 1）；🟡 Minor 3 |
| **总体** | **GRAY：论文有明确贡献，但存在可修复的实质缺陷，建议 Major Revision** | **阻断级 1；🔴 Major 12；🟡 Minor 11** |

---

## 2. 逐维详审

### 维度一：背景与文献

【结论】GRAY

【定位与证据】

1. **编号文献池的闭合性在 `[Rnn]` 层面成立，但不是无条件成立。**

   - L60：“The reference pool is closed: fifty-four items, cited by pool number [R01]–[R54]; fifty-two entries were verified against primary records…”
   - L316：“The reference list is the closed pool of fifty-four items, cited in the text by pool number [R01]–[R54].”
   - 实测编号条目数：R01–R15 为 15 条，R16–R29 为 14 条，R30–R39 为 10 条，R40–R41 为 2 条，R42–R45 为 4 条，R46–R52 为 7 条，R53–R54 为 2 条，合计 54 条。
   - C54：“[PASS] C1-54条全列: References 列表 54 条；缺失=无 多余=无”。
   - C55：“[PASS] C2-指针全覆盖: 正文引用 54/54；未在正文引用=无；正文有而未列=无”。

   **实测：声明值 54 → 编号文献实测 54；编号闭合为材料内可证。** 但正文另有两个非 `[Rnn]` 形式的自引占位，见维度三。

2. **Helmholtz 是一个被用于历史论证、但在文献池中完全缺席的一手人物。**

   - L68：“the physical speculation they carried from the start — the habilitation lecture in which Riemann…[R53]; Clifford’s proposal…[R54]; Helmholtz’s public case for the empirical standing of geometrical axioms — remained speculation, never an adopted physical theory.”
   - Riemann 与 Clifford 分别由 R53、R54 支持；Helmholtz 后无任何 `[Rnn]`，R01–R54 中也没有 Helmholtz 条目。

   **实测：声明存在 Helmholtz“public case” → 正文无引证、文献池无条目；材料内可证为支撑缺口。**

3. **“formal fiction”的定义与 Riemann 文本中的物理指向存在张力。**

   - L68：“We use ‘formal fiction’ in exactly this sense — a self-consistent symbolic system with no intended physical referent at the time of its construction”。
   - 同段所引 Riemann 却“seeks the ground of spatial metric relations outside space, ‘in binding forces which act upon it,’ and hands the open end to ‘the domain of another science, of physic’”。

   论文确实承认这些构造“carried from the start”物理猜测，但“no intended physical referent”仍显得过强，至少需要更精细地区分“未被物理理论采用”与“构造时完全没有物理指向”。

4. **新颖性检索被用来给唯一性声明设限，但检索协议本身不可复算。**

   - L60：“made strictly relative to our three-line search completed on 2026-09-16”。
   - L212：“To the extent of our three-line search completed on 2026-09-16, the mapping has not been stated as a structural isomorphism with a portable pipeline”。
   - 正文未给出三条检索式、数据库、筛选规则或检索结果集。

   **实测：存在“three-line search”声明 → 无检索式和复现协议；材料内不可证。**

5. **部分文献的书目强度不足或仍处于待完成状态。**

   - L332：R13 标注“[IDENTIFIER-PENDING]”。
   - L333：R14 标注“[IDENTIFIER-PENDING]”。
   - L390：R53 的“German original locator…(title verified, text not captured)”。
   - L391：R54 为“Wikisource transcription”，并仅注明“page categorized ‘1876 works’”。
   - L373：R42 仅有作者姓、题名、刊名和年份，缺少卷期、页码或 DOI。

【分析】

论文的核心历史案例并非泛泛而谈：Channel I 有 Walter 与 Einstein，Channel II 有 Brown/Norton/Nersessian/Suárez，Channel IV 有 Morris–Thorne、Thorne 自述和词汇记录；作者也明确承认案例研究不是系统历史。这种克制是优点。

但维度一存在三个实质问题：

- Helmholtz 被用来支撑 19 世纪几何物理推测的历史链，却没有任何文献锚点，直接违反论文自设的历史引证标准。
- Riemann 一边被定义为“无物理指称”，一边又被引述为主动把几何度量交予物理学，形式主义史学口径需要降格或重新解释。
- 新颖性声明虽然加了“相对于三条检索”的闸门，但检索式不存在，第三方面对的是一个不可复算的闸门。

R13/R14 已被显式标记，不构成隐瞒；R53/R54 也提供了 URL 和捕获日期。但它们的书目强度参差不齐，尤其 R54 依赖 Wikisource、R53 未捕获德文原文，不宜与独立出版商版本或档案馆一手文本完全等权。

---

### 维度二：方法与可证伪承诺

【结论】GRAY

【定位与证据】

1. **M4 行的范畴对应不成立。**

   - L197：Hard-SF 侧为“Narrative artifacts can carry engineering commitments; the diegetic prototype has documented instances [R32], [R33]”；AI 侧为“Adjudication procedure pre-registered, recomputable by a third party…”；共享失败模式为“Changing the rules after the fact”。
   - L184 从硬科幻标准中蒸馏出的是四项：“internal consistency, no supernatural checks, continuity with known science, and checkability of the world’s claims by observers inside the world”。

   M4 左侧并不是硬科幻文本的“硬度标准”，而是叙事人工物影响工程实践的经验性存在声明；R32/R33 也是电影咨询与实验室互动研究，不是预注册或裁决规则。左侧没有“先冻结规则、后看结果”的结构，因此与右侧预注册程序不构成同行对应。

2. **“structural isomorphism”的措辞强度超过表中证据。**

   - L200：“The table claims structural isomorphism — row-by-row shared form and shared failure modes — and nothing stronger. It is not an equivalence theorem”。
   - L225：“The hard-SF criteria and the falsifiability criteria of AI research claims are structurally isomorphic under the mapping M1–M5”。
   - L249：工程实例“is structurally isomorphic to the Channel I pattern”。

   作者已否认这是等价定理，值得肯定；但“row-by-row shared form”仍是强形式断言。M4 失败后，M2、M5 也主要是解释性平行而非形式同构：例如“世界内观察者可检查”并不自动等于“实验前定义 kill line 的外部可证伪性”。

3. **类型学层面的 F-C1–F-C4 缺少可执行阈值。**

   - L33：F-C1 的结果是“the four-way typology is weakened”。
   - L34：F-C2 的结果是“that channel is downgraded”。
   - L36：F-C4 要求新案例不能“without ambiguity”，否则类型学“is ad hoc”。
   - L35：F-C3 使用“systematically leave no kill line to hang”，但未定义案例数、任务类别或判定阈值。

   这些条件作为研究纲领有启发性，但“weakened / downgraded / ambiguous / systematically”均未操作化。真正具备具体 kill line 的是 §7 工程案例，而不是整个类型学。

4. **Channel III 的公式同一性表述过强。**

   - L134：“The isomorphism of formula: the same expression, H = -Σ p·log p, governs the abstract ensemble and the physical distribution — not a similar expression, the same one.”
   - L128：Shannon 的量指称“an ensemble of messages, an object with no mass, no location, and no temperature”。
   - L142：物理化后的 residue 是“an operative quantity with units, prices, and experimental tests”。

   论文自己的叙述已经显示：信息熵无量纲，物理统计熵带有物理单位和常数约定，Landauer 价格又引入 kT。更稳妥的说法应是“同一泛函形式，差一个正乘法常数、对数底和单位约定”，而不是“the same one”。

5. **预注册冻结是 author-attested，尚不等于论文所要求的 external anchor。**

   - L220：P 阶段产物是“a frozen adjudication function with an external anchor, fixed before any run”。
   - L237：“The adjudication layer is frozen before runs as pure verdict functions with published SHA-256 anchors, given as twelve-character prefixes”。
   - L253：“this is an author-attested freeze. A digest can attest that the artifact was not altered after the fact; it cannot by itself attest to a party that did not build the system that the freeze preceded the runs”。

   论文对局限披露得非常充分，但哈希摘要本身不提供受信时间戳；若仓库和历史由作者控制，它不能独立证明“冻结先于运行”。主表 L297 直接记为“Pass”仍偏强，至少应写成“provisional/author-attested pass”。

6. **§7 的数字在文本内部基本自洽，但当前审计包无法独立复算。**

   - L239：median ECR 基于“17 finite-valued graphs”，同时“coverage of 20 of 22 graphs — three graphs read Infinity, two graphs lack arm data”。
   - 材料内算术：17 个有限值 + 3 个 Infinity = 20，再加 2 个缺 arm 数据 = 22，口径一致。
   - C51 仅证明五个哈希前缀在交付文本中各出现一次：“aeefb8ef6972:1…6b09de9911c0:1”。
   - L239：“A reviewer working from the public text alone therefore cannot execute the recomputation that M4 asks of a third party”。

   **实测：字段路径、计数和哈希出现次数为材料内可证；数值是否来自所声称的冻结记录、冻结是否先于实验，需外部/保密工件核验。** 不能因为论文给出字段路径就推定数据为真，也不能因为当前包无法复算而推定造假。

7. **跨 backbone 与普遍性总体上有节制，但少数措辞仍偏宽。**

   - L249：“its magnitude is not comparable to the non-Euclidean case, and nothing in this paper claims otherwise”。
   - L306：“no prevalence claim is made anywhere in this paper”。
   - L257：§8“is not an empirical claim, and it makes no prediction”。
   - L225 仍称四阶段流水线“ports the former into the latter as working methodology”。
   - L247：“the capability channel reads zero”，同段又承认“smaller increments are not excluded”。

   论文没有明确声称跨 backbone 普遍有效，也没有断言反向通道已存在；这一点处理得当。但一个 mid-strength、作者自建、两个基准上的案例最多支持“one worked example”，“working methodology”与“reads zero”应进一步限定为“在该工件、基准和检验功效下未检出”。

【分析】

T/R/D 三检查和 D 的四类 disposition 是有价值的审计语言；§7 把负面结果完整摊开，也显著强于只展示成功案例的方法论文。但本维度的核心问题是：论文最形式化的词——“structural isomorphism”“pre-registered”“external anchor”“falsifiability”——在若干关键点上比实际证据更强。

尤其是 M4：它既是映射表的一行，又承担流水线 P 阶段的理论来源。若 M4 不成立，作者仍可保留预注册阶段，但必须承认那是从 preregistration/reproducibility 文献独立组装的方法，而不是从硬科幻标准逐行移植而来。

---

### 维度三：创新声明与归属

【结论】GRAY

【定位与证据】

1. **贡献列表清楚，且主动把装置置于案例读法之前。**

   - L50：“The paper makes five contributions, ordered by what the checks can carry rather than by narrative precedence.”
   - L52–L56 依次列出 criterion apparatus、four-channel application、M1–M5 mapping、engineering instance、reverse-channel adjudication agenda。
   - L58：“the paper asks to be credited with the checks that produced the grades, not with the sweep of the channels.”

2. **M1–M5 的来源归属总体细致。**

   - L204：“of the AI-side criteria, only M2’s no-future-capability demand restates a concern one of these sources states directly”。
   - 同段说明 M1 来自 Toulmin、M4 来自 preregistration/Registered Reports/NeurIPS reproducibility 等、M5 来自 Popper 与 Leavitt–Morcos；并声明“M3’s anchoring criterion claims no pool original”。

3. **封闭文献池被两个自引占位打破。**

   - L60/L316 声明全部引用以 `[R01]–[R54]` 进行。
   - L202：“an archived companion study of auditability and falsifiability in LLM-reasoning research [self-citation removed for double-blind review; restored at camera-ready]”。
   - L279：“is systematized in the companion study whose self-citation is removed for double-blind review (§6.2)”。

   这两个位置实际引用了一项外部研究，但它没有匿名编号、没有进入 R 池，也没有可供审稿人核查的书目记录。C55 的“正文引用 54/54”只扫描 `[Rnn]` 形态，不能覆盖这种占位引用。

4. **新颖性声明有闸门，但闸门尚未完成。**

   - L60：“a second-round novelty check is scheduled before submission, and those statements carry that gate”。
   - L306：新颖性陈述依赖“the three-line search completed on 2026-09-16, with the second-round check scheduled before submission”。

【分析】

论文对“哪些标准是自己的形式化、哪些只是由 R38/R39 的失败模式激发”作了少见清楚的区分，避免把 Toulmin、Popper、preregistration 文献的既有贡献反向占为己有。这一方面基本可信。

主要问题是 companion study 的双盲处理与封闭池声明相互冲突。双盲并不要求删除学术归属；常见做法是提供作者匿名的参考文献条目和保密全文。当前写法使审稿人无法判断：

- M4 的 freeze protocol 有多少来自 companion study；
- §7 工件与 companion study 是否同一研究；
- 本论文相对于该已归档研究的新增贡献究竟是什么。

这不是指作者必然过度归属，而是双盲状态下创新边界不可核查。

---

### 维度四：写作、内部一致性与双盲合规

【结论】FAIL（分层结论：渲染层 PASS；TeX 源层 GRAY；编译/构建记录层若随审包分发则 FAIL）

【定位与证据】

1. **渲染层双盲措施基本完备。**

   - T63–T64：`\author{}` 与 `\date{}` 均为空。
   - T43：hyperref 选项为 `pdfauthor={}`。
   - C68：“[PASS] D2-作者/日期栏: \author{}/\date{} 均空；无致谢节”。
   - C69：“D3-PDF元数据: /Author=“”；Creator=“LaTeX with hyperref””。
   - C71：“D5-CJK文本层: PDF 文本层 CJK 字符 0”。
   - C72：“D6-邮箱零命中: 全文邮箱=无”。

2. **TeX 源层存在 CJK 注释和内部工作流痕迹。**

   - T42：“% F8: \url 允许在连字符后断行（R37 长条目 Underfull 根因）”
   - T47：“% F7: 节/小节标题 raggedright…”
   - T56–58：包含“F10（申报）”“改词被禁、microtype 不可用”等中文内部排版说明。

   这些注释没有直接出现法定姓名，但暴露了中文工作环境、内部 F 编号流程和排版决策。

3. **编译记录包含工作流昵称与本地路径。**

   - C3：“生成者：戴夫-格式专家 | 2026-09-17”。
   - C8：“shared/鲍勃_FTFB全稿R2修订版_2026-09-17.md（416 行）”。
   - C26：“上一链头（查理_FTFB全稿文献合并版，SHA 76eef1dd…）”。

   “戴夫”“鲍勃”“查理”是昵称而非法定姓名，但它们是持久化的角色/人员指纹；若编译记录随双盲审包分发，已经超出“无作者姓名”的最低要求。是否能据此实际识别到个人需外部核验，但“无姓名 token”不等于“不可识别”。

4. **匿名化声明与工件 basename 不一致。**

   - T316：“The anonymization covers the project’s name, the name of its fictitious entity, and the project-name tokens inside artifact basenames (replaced below by the marker ‘anon’)”。
   - T324 仍列出 `GT_FORMALIZATION_v1.md`、`run_v21_gtformal.py`、`run_v22_p1c.py`、`SPEC_GT2B.md`、`SPEC_GT8C.md`。

   若 `GT/gt` 是项目名 token，则匿名化声明被自身文本推翻；若 GT 只是“ground truth”的通用缩写，也需明确说明，因为 `SPEC_GT2B`、`GT8C` 看起来像项目专名指纹。

5. **十二个字符的哈希前缀本身也是内容指纹。**

   - T324 公布五个十二位 SHA-256 前缀。
   - T326：“the public pointer is deferred to camera-ready”。

   不公开展开仓库 URL 并不能自动保证匿名：若工件曾公开或被代码搜索索引，哈希前缀可能反查到仓库。是否实际可查需外部核验。

6. **源注释与编译记录中的 badness 数值不一致。**

   - T56：“残余 badness 1092/1331 两行”。
   - C73：“lines 324-325 badness 2103; lines 467-468 badness 5548; lines 467-468 badness 1990”。

   这不影响 PDF 正文，但说明源中残留了过期的试排注释。

7. **若干计数与措辞口径需要收紧。**

   - T430 的 R12 同时包含“K. Čapek, R.U.R., 1920”和“I. Asimov, ‘Liar!’, 1941”，但全文按 54 个编号条目计数；需说明 R12 是一个编号条目还是两个作品。
   - L55 称工程案例“with its negative results disclosed in full”，而 L239 说明完整仓库和完整摘要在审稿期仅通过保密渠道提供。
   - L237 称“published SHA-256 anchors”，但公开文本只有十二位前缀，公开指针延迟到 camera-ready。

【分析】

PDF 渲染层的双盲技术处理相当仔细：作者栏、日期栏、PDF metadata、邮箱、批注和 CJK 文本层均通过检查。但双盲审计必须分三层判断：

- **渲染层：PASS。** 当前 PDF 文本没有直接身份泄露。
- **TeX 源层：GRAY。** CJK 注释不直接点名，但暴露语言社区和内部流程。
- **编译记录层：FAIL（若随审包提供）。** “戴夫/鲍勃/查理”与路径构成人员或工作流指纹。

此外，GT token 与哈希前缀说明论文自己的匿名化口径尚未完全执行。编译记录 C78 的“全门禁 PASS”只能证明 PDF/文本层门禁通过，不能证明源 tarball、构建日志或内容指纹不可识别。

---

## 3. 问题清单

### 阻断级

- **B01｜源层与构建记录的双盲合规问题**
  - **定位**：T42、T47、T56–58；C3、C8、C26。
  - **证据**：T42 有中文注释“F8: \url 允许在连字符后断线…”；C3 为“生成者：戴夫-格式专家”；C8 路径含“鲍勃_FTFB全稿R2修订版”；C26 含“查理_FTFB全稿文献合并版”。
  - **建议**：投稿版 TeX 全部注释剥离或转成中性英文，编译记录不得随双盲审包分发；重新生成不含人员昵称、本地路径和内部链头的干净构建日志。

### 🔴 Major

1. **M01｜Helmholtz 历史断言无锚点**
   - **定位**：L68；参考文献 L320–L391。
   - **证据**：“Helmholtz’s public case for the empirical standing of geometrical axioms — remained speculation, never an adopted physical theory.” 该句无引证，池中无 Helmholtz 条目。
   - **建议**：补入 Helmholtz 一手文本及可靠研究文献，或删除该专名断言、改用已获支撑的 Riemann–Clifford 链。

2. **M02｜“formal fiction”定义与 Riemann 的物理指向冲突**
   - **定位**：L68。
   - **证据**：论文定义“no intended physical referent”，同段又引 Riemann “in binding forces which act upon it” 和 “the domain of another science, of physic”。
   - **建议**：把定义改为“构造时未被既有物理理论采纳/协调”，并明确 Riemann 的物理猜测不被算作已实现物理指称。

3. **M03｜新颖性检索不可复算**
   - **定位**：L60、L212。
   - **证据**：“three-line search completed on 2026-09-16”，但未给检索式、数据库、筛选规则和结果集。
   - **建议**：附录列出三条检索式、数据库/日期/纳入排除规则，或把所有唯一性声明进一步降格为非系统性文献印象。

4. **M04｜M4 行范畴对应失败**
   - **定位**：L197；并见 L184。
   - **证据**：左侧“Narrative artifacts can carry engineering commitments; the diegetic prototype…”对应右侧“Adjudication procedure pre-registered, recomputable by a third party”。
   - **建议**：重写 M4，使左侧真正成为硬科幻世界的预承诺/规则固定标准；若找不到对应标准，就把 R32/R33 移为动机文献，并承认 P 阶段来自预注册文献而非硬科幻标准。

5. **M05｜“structural isomorphism”声明过强**
   - **定位**：L200、L225、L249。
   - **证据**：“row-by-row shared form and shared failure modes”；“structurally isomorphic under the mapping M1–M5”。
   - **建议**：在 M4 修复前，将“structural isomorphism”降为“constructed structural parallel/analogy”，并把工程实例中的同构说法改为“parallel”。

6. **M06｜F-C1–F-C4 缺少类型学层面的判定阈值**
   - **定位**：L33–L36。
   - **证据**：“weakened”“downgraded”“without ambiguity”“systematically”均无数量或程序阈值。
   - **建议**：为每一条 kill line 指定独立测试集、分类人数/歧义率、时间锚点失败条件和 reverse-channel 的最小证据组合。

7. **M07｜信息熵与物理熵“same expression”表述不准确**
   - **定位**：L128、L134、L142。
   - **证据**：“not a similar expression, the same one”，但论文同时区分无量纲消息系综和带 units, prices, experimental tests 的物理量。
   - **建议**：改为“same functional form up to a positive multiplicative constant, log base, and physical units”。

8. **M08｜author-attested freeze 不足以无保留支持 external anchor / pre-registered**
   - **定位**：L220、L237、L253、L297。
   - **证据**：L253 承认“A digest…cannot by itself attest…that the freeze preceded the runs”，但主表仍记“Pass”。
   - **建议**：补充受信时间戳、第三方归档或保密仓库的独立提交时间证明；在此之前将 T 改记为“provisional pass (author-attested)”。

9. **M09｜§7 核心工程记录在当前审计材料中不可独立复算**
   - **定位**：L237–243；C51。
   - **证据**：论文只给字段路径和十二个字符哈希前缀；L239 承认“A reviewer working from the public text alone therefore cannot execute the recomputation”。
   - **建议**：编辑确认保密冻结仓库、完整摘要和运行说明已提供给审稿人；若无法提供，则 §7 只能作为叙述性案例，不能作为已审证的端到端执行。

10. **M10｜自引占位破坏封闭文献池和归属边界**
    - **定位**：L60、L202、L279、L316。
    - **证据**：文献池声明为 `[R01]–[R54]`，正文却出现“[self-citation removed for double-blind review; restored at camera-ready]”。
    - **建议**：增加作者匿名的编号参考文献及保密可获取版本，并更新 54 条计数；或删除对该 companion study 的实质性依赖，仅保留不构成优先权主张的方法说明。

11. **M11｜GT/gt token 与哈希前缀构成残余匿名指纹**
    - **定位**：T316、T324、T326。
    - **证据**：匿名化声明称项目名 token 已替换为 `anon`，但 basename 仍含 `GT_FORMALIZATION`、`gtformal`、`SPEC_GT2B`、`SPEC_GT8C`。
    - **建议**：将所有 GT/gt 文件名统一替换为中性标签并向编辑保存密映射；评估哈希前缀是否可被公开搜索反查，必要时仅向编辑提供完整摘要。

### 🟡 Minor

1. **m01｜R13/R14 仍处于 identifier-pending 状态**
   - **定位**：L332–L333。
   - **证据**：两条均标注“[IDENTIFIER-PENDING]”，L60 称将在“pre-submission verification round”完成。
   - **建议**：若当前已是外审版本，补全稳定标识符或访问路径；否则明确标注这是投稿前草稿而非提交版。

2. **m02｜R53/R54 的一手文本强度需说明**
   - **定位**：L390–L391。
   - **证据**：R53 “German original…title verified, text not captured”；R54 为“Wikisource transcription”。
   - **建议**：注明使用的是英译转录本/网络转录本，而非原始出版本；尽可能补充档案馆或出版商稳定链接。

3. **m03｜R42 书目信息过简**
   - **定位**：L373。
   - **证据**：仅有作者姓、题名、刊名、年份和“open access”。
   - **建议**：补全卷期、页码、DOI 或稳定 URL。

4. **m04｜Channel III 是否属于“fiction”通道需在题首层面说清**
   - **定位**：L13、L126。
   - **证据**：摘要称 four channels of fiction-to-science feedback；L126 却说该输入“is an abstraction rather than a fiction in the story sense”。
   - **建议**：在摘要或 thesis 中写成“fiction and fiction-analogous idealized/abstract inputs”。

5. **m05｜“capability channel reads zero”措辞超过统计功效**
   - **定位**：L247。
   - **证据**：同段承认“smaller increments are not excluded”。
   - **建议**：改为“no detectable capability gain at the stated ±10 percentage-point threshold”。

6. **m06｜“independent rerun”的独立性含义不清**
   - **定位**：L243、L253。
   - **证据**：L243 称“an independent rerun passed”，L253 又强调整体仍是作者自证冻结。
   - **建议**：说明重跑者是否属于作者团队、是否预先看到规格，以及其独立程度。

7. **m07｜单一工程实例对“working methodology”的支持范围应收窄**
   - **定位**：L225、L249、L306。
   - **证据**：论文已限制 magnitude 和 prevalence，但 L225 仍称“as working methodology”。
   - **建议**：改为“provides one worked example of the methodology on a single artifact”，避免被读成跨任务或跨 backbone 验证。

8. **m08｜第二轮新颖性检查尚未完成**
   - **定位**：L60、L306。
   - **证据**：“a second-round novelty check is scheduled before submission”。
   - **建议**：投稿前完成并更新声明；若未完成，删除或弱化所有近唯一性表述。

9. **m09｜TeX 中残留过期 F10 排版注释**
   - **定位**：T56–58；C73。
   - **证据**：T56 写“badness 1092/1331”，C73 实际披露 2103、5548、1990。
   - **建议**：删除过期注释或更新为最终编译数值。

10. **m10｜“published”与“disclosed in full”需限定**
    - **定位**：L55、L237、L239。
    - **证据**：完整仓库和 full SHA-256 digests 在审稿期通过保密渠道提供，公开指针延迟。
    - **建议**：改为“reviewer-available through a confidential channel; public release at camera-ready”。

11. **m11｜R12 的编号条目与作品数口径不一致**
    - **定位**：L331/T430。
    - **证据**：一个 R12 编号下列出 Čapek 1920 与 Asimov 1941 两个作品。
    - **建议**：说明 54 是编号池条目数而非作品数，或拆成 R12a/R12b 并重新计数。

---

## 4. 修改优先级

| 优先级 | 条目 | 位置 | 一句话改法 |
|---|---|---|---|
| **P0 必改** | B01：清理源层与构建记录 | T42/T47/T56–58；C3/C8/C26 | 剥离 TeX 注释，禁止含昵称和本地路径的编译记录进入双盲审包。 |
| **P0 必改** | M11：处理 GT token 与哈希指纹 | T316、T324、T326 | 中性化全部文件名并评估哈希前缀的可搜索性，敏感映射仅交编辑保存。 |
| **P0 必改** | M10：解决自引与封闭池冲突 | L202、L279 | 以匿名编号参考文献纳入 companion study，或移除对其的实质性优先权依赖。 |
| **P0 必改** | M09：确认 §7 保密记录可审 | §7.1、编辑材料 | 向审稿人提供冻结仓库、完整摘要和复算说明；做不到则降格 §7 证据地位。 |
| **P0 必改** | M04/M05：修复映射核心声明 | L197、L200、L225 | 重写 M4；在未证明逐行同构前将“structural isomorphism”降为“structural parallel”。 |
| **P1 应改** | M01：补 Helmholtz 锚点 | L68 | 加入一手 Helmholtz 文献和二手研究，或删除该断言。 |
| **P1 应改** | M02：校准 formal fiction 史观 | L68 | 区分“未被物理理论采用”和“完全无物理指称”。 |
| **P1 应改** | M07：修正熵公式同一性 | L134 | 明确常数、对数底和单位约定，只声称同一泛函形式。 |
| **P1 应改** | M08：补强冻结独立性 | §7.1、§7.4、§9.1 | 加入第三方时间戳，或将 T 改为 author-attested provisional pass。 |
| **P1 应改** | M06：操作化 F-C 条件 | §1.2、§9.3 | 为 weakened/downgraded/systematically/ambiguous 设定可复算程序阈值。 |
| **P1 应改** | M03：公开检索协议 | §1.3、§6.3、§9.2 | 列出三条检索式、数据库、日期和筛选规则。 |
| **P1 应改** | m05/m07：收窄能力与普遍性措辞 | §6.4、§7.3 | 明确只是在给定基准、功效和单一 artifact 上的 worked example。 |
| **P2 建议** | m01/m02/m03：完善书目信息 | R13/R14/R42/R53/R54 | 补全标识符、稳定链接和转录本性质说明。 |
| **P2 建议** | m04：调整 thesis 口径 | 摘要、§1.2、§4 | 将四通道表述为 fiction 与 fiction-analogous abstract inputs。 |
| **P2 建议** | m09：清理过期注释 | T56–58 | 删除或更新旧 badness 数值。 |
| **P2 建议** | m10：限定公开性措辞 | 摘要、§7.1 | 把“published/full disclosure”改为审稿期保密可得。 |
| **P2 建议** | m11：统一计数口径 | R12、§1.3 | 声明编号条目数与作品数的区别。 |

---

## 5. 总体判定

**建议级：Major Revision**

| 评分项 | 分数（10 分制） |
|---|---:|
| 原创性 | 8 |
| 方法论 | 5 |
| 结果与论证 | 6 |
| 写作与一致性 | 7 |

这篇论文有真实的智识雄心：它没有把科幻与科学的关系停留在趣闻或赞美上，而是试图建立 T/R/D 检查、证据分档、映射表、预注册流水线和反向通道的死亡条件。§7 对负面结果、能力零增益和 author-attested freeze 的披露尤其值得肯定，说明作者理解“可证伪”不应只是修辞。

但当前版本还不能直接接受：M4 行不构成可靠的范畴对应，因而“structural isomorphism”和整条 P 阶段的硬科幻来源被削弱；类型学 kill lines 仍多为定性措辞；§7 的冻结与复算独立性在当前材料中无法验证；Helmholtz 断言和检索协议也未达到论文自设的引证标准。双盲方面，PDF 渲染层干净，但源注释和编译记录中的昵称、路径、GT token 与哈希前缀必须在投稿前清理。

这些问题大多不是方向性错误，而是证据强度、术语强度和投稿卫生问题。若作者能修复 M4、补足独立冻结证据、收窄同构措辞并清理双盲材料，论文有潜力成为一篇有价值的跨学科方法学立场论文。