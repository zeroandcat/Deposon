# FTFB 双审修复 · 逐项修复说明（第一阶段：内容层）

- **修复对象**：`查理_FTFB全稿双审修复版_2026-09-16.md`（新链头，未覆盖旧版）
- **基线**：`查理_第二作FTFB全稿修正版_2026-09-16.md`，SHA-256 `5e6f433be2d6…44d7514`（与外审包 md 逐位一致）
- **新链头 SHA-256**：`bf35c37f5264…8ad535`（368 行；基线 361 行）
- **审稿依据**：双审三件（Reviewer A 内容审 / Reviewer B 技术审 / 综合报告），行号均指新链头文件
- **纪律执行**：见文末「纪律自检」；全部引用编号与 References 表未动（References 节与基线逐字节一致）

---

## ①【阻断级】§7 可复算性缺口声明（对应 Reviewer A 5.1；综合报告阻断第 1 条）

**位置**：§7.1 E 段末尾（行 231）

**旧句**：`The frozen handoff artifact is available as an anonymized pointer, with the public repository link deferred to the camera-ready version.`

**新句**：`Availability, stated for the blind-review version: the complete frozen repository and the full SHA-256 digests — not only the twelve-character prefixes printed above — are provided to the editors and reviewers through a confidential channel, per double-blind discipline, and the public pointer is deferred to camera-ready. A reviewer working from the public text alone therefore cannot execute the recomputation that M4 asks of a third party, and this paper does not claim otherwise: during review, M4's third-party recomputation runs through the confidential channel or not at all. The gap is stated here, at the point where it applies, rather than left for the reader to discover. What the public text carries now are the field paths — where each number lives in the record — and the anchors the record must match when it opens.`

**要点**：显式承认审稿期 M4 第三方重算缺口（保密通道或不可执行），不再以「anonymized pointer」修辞带过。

**同步校准 1**（§6.4，行 215）：在「verdict function must be executable by a third party who did not build the system」后追加——
`One calibration belongs with the requirement rather than in a footnote: executable is a standing demand, not a report of who has executed. … The requirement is therefore only partially met while the paper is under review, and the limit is stated in §7.1, where it applies.`

**同步校准 2**（§8.3 审计词汇句，行 271）：
旧：`a reasoning claim is auditable when a third party can recompute it from the frozen record alone`
新：`a reasoning claim is auditable when a third party that holds the record can recompute it from the record alone, so that availability of the record to the auditing party is itself part of auditability … For the §7 instance, that availability runs through the confidential channel declared in §7.1 until camera-ready.`

**同步校准 3**（摘要末句，行 5）：
旧：`Every claim is stated to be checkable by a third party.`
新：`Every claim is stated to be checkable by a third party, subject to the blind-review availability limits declared for the engineering record.`

---

## ②【阻断级】双盲匿名化：deposon 专名与 keep-the-books 匿名自引（对应 Reviewer A 9.2(b)；综合报告阻断第 3 条）

**§7 标题**（行 219）：`## 7. Case Study: The Deposon Instance` → `## 7. Case Study: An Anonymized Engineering Instance`

**§7 开篇**（行 221）：
旧：`This section examines one documented artifact — the deposon project — on the same footing…`
新：`This section examines one documented artifact — an engineering project whose identity is anonymized for review and restored at camera-ready — … The anonymization covers the project's name, the name of its fictitious entity, and the project-name tokens inside artifact basenames (replaced below by the marker "anon"); full names, path prefixes, and the public pointer are restored at camera-ready. It touches no anchor digest, no number, and no field-path semantics…`

**专名与工件名替换**（§7 全节，共 6 处 basename、2 处专名）：
- `the deposon — a fictitious scattering entity` → `a fictitious scattering entity (named in the setting; the name is anonymized here)`（行 225）
- `a two-parameter deposon state` → `a two-parameter state of that entity`（行 227）
- `results/deposon_benchmark_v1_4_gsm8k.json` → `results/anon_benchmark_v1_4_gsm8k.json`（×2：行 231、239）
- `results/deposon_v21_gtformal.json` / `deposon_v22_p1c.json` / `deposon_v22_e95ci.json` / `deposon_v20_crossval.json` → `anon_` 同名替换（行 231、239）
- **五锚 SHA（aeefb8ef6972 / 9bbe43f41fa8 / 6e9673205dc0 / 68a5b08ef007 / 6b09de9911c0）与全部数字、字段路径语义不动**（已逐一核验 1:1 保真）

**keep-the-books 匿名自引规范化**（§6.2 Anonymous interface，行 194）：
旧：`…is systematized, under the name *keep the books*, in an archived companion study… It is cited here anonymously, and the public pointer is deferred to the camera-ready version, per double-blind discipline.`
新：`…is systematized in an archived companion study of auditability and falsifiability in LLM-reasoning research [self-citation removed for double-blind review; restored at camera-ready]. The row itself is this paper's formalization, as the provenance note below states; what it inherits from the companion study is the freeze protocol and the recomputability standard, described here only to that extent.`

**同步**（§8.3，行 271）：`…in the archived companion study already cited anonymously in §6.2` → `…in the companion study whose self-citation is removed for double-blind review (§6.2)`。

**R-4 说明**：五锚在双盲版保持裸文件名（不带 `docs/` 前缀），路径前缀归 camera-ready 口径，已并入 §7 开篇「full names, path prefixes, and the public pointer are restored at camera-ready」一句。

---

## ③【重大】[R38]/[R39] 判据归因修正（对应 Reviewer A 4.1/8.1；综合报告重大第 4 条）

**位置**：§6.2 映射表（行 184–190）＋归因段（行 196）

**表头**：`AI-claim criterion (pool source)` → `AI-claim criterion (provenance stated per row)`

**M1/M3/M4/M5 单元格**（M2 不动）：
旧（M4 例）：`Adjudication procedure pre-registered, recomputable by a third party [R38], [R39]`
新（M4 例）：`Adjudication procedure pre-registered, recomputable by a third party — this paper's formalization, prompted by the failure modes documented in [R38], [R39]`
（M1/M3 同式，仅引 [R38]；M5 同 M4。）

**归因段**（行 196）：
旧：`The mapping draws its claim–evidence and anchoring criteria (M1, M3, M4) from the former, and its no-future-capability and pre-registration criteria (M2, M4, M5) from the latter. Neither source states the mapping; both state the failure modes the mapping catches.`
新：`A provenance declaration is owed here and made plainly: of the AI-side criteria, only M2's no-future-capability demand restates a concern one of these sources states directly — the speculation critique of [R39] in criterion form. The claim–evidence, anchoring, pre-registration, and kill-line criteria of rows M1, M3, M4, and M5 are this paper's formalization, prompted by the failure modes those two sources document; neither source states these criteria themselves, and nothing in this paper attributes them to either. The primary literature for pre-registration and falsifiability criteria is under a scheduled verification pass, and will be cited in place before submission. The failure modes are theirs; the criteria that catch them are this paper's.`

**要点**：显式声明两文不含这些判据本身；原始文献留待阿兰补检后下轮入池（本轮 References 与 45 条编号不动）。

---

## ④【重大】F-C2 重写：删除被挖空的 dispensability 分支（对应 Reviewer A 3.1；综合报告重大第 5 条）

**位置**：§1.2（行 26）；§9.3 复记（行 302）同步

**旧句**：`If the flagship case of any channel is shown to have a dispensable fictional input, or to fail the temporal check, that channel is downgraded.`

**新句**：`If the flagship case of any channel fails the temporal check — the dated priority of the fictional input collapses — or cannot sustain even the supply-level claim, leaving no operative residue behind, that channel is downgraded. A demonstrated dispensable input is not a downgrade trigger under this condition: the channel claims are stated at the supply level, so a fiction-free account of the same development would re-confirm the grading rather than refute the claim.`

**§9.3 复记同步**（行 302）：`F-C2: if a flagship case loses its anchor — a dispensable fictional input, a failed temporal check — its channel is downgraded.` → `F-C2: if a flagship case fails the temporal check, or cannot sustain even the supply-level claim — no dated priority, no operative residue — its channel is downgraded.`

**要点**：dispensability 分支在 supply 级口径下必然「假触发」，删除并改述为「连 supply/residue 也站不住则降级」；删除理由在原位一句话说明，不留悬挂。

---

## ⑤【重大】「decidable」名实对齐＋贡献排序调整（对应 Reviewer A 1.1、2.3；综合报告重大第 6 条）

**Thesis 句两处逐字同步**（摘要行 5 ＋ §1.2 行 19，脚本核验去斜杠后逐字一致、全文恰出现 2 次）：
旧：`…but it is a recurrent, decidable input to the exact sciences…`
新：`…but it is a recurrent, checkable input to the exact sciences…`

**§1.2 定义段重写**（行 21）：
旧：`The word "decidable" carries its ordinary methodological sense: the contribution credited to a fictional input must be confirmable or refutable by named checks, not by taste.`
新（两档边界）：`The word "checkable" carries its ordinary methodological sense: the contribution credited to a fictional input must be confirmable or criticizable by named checks, not by taste. The word's force differs by tier, and the difference is declared here rather than smoothed over. "Decidable" is reserved in this paper for the pre-registered tier (§6–§7), where a kill line is fixed before the run and the verdict is recomputable; the thesis sentence deliberately does not use it. On the historical tier (§2–§5), a checkable claim is one a third party can re-examine against dated anchors, and the D check there has a bounded adjudicative power that the scores record rather than conceal: in most rows it returns a partial pass, an indeterminate, or an unresolved-by-design, because the counterfactual study the check would need is rarely in the pool. The paper claims re-examinability for its historical claims and falsifiability only for its pre-registered ones, and the master table (§9.1) is graded to that split.`

**§8.3 两处 "decidable"（行 249、265）保留不动**：均为预注册层语境（反向通道判定议程），与 §1.2 的保留义声明一致，歧义已由两档拆分消除。

**贡献排序调整**（§1.3，行 42–50）：四项改为五项，判据装置升为第 1 主贡献、四通道降为第 2「装置的应用」：
新增排序理由句：`The order is itself a graded claim, and the reason is worth one sentence: the apparatus (1) is what this paper would be missed for, while the channel readings (2) are its first application and are graded at the supply level by design — readings at that level are close to what the field already holds, and the paper asks to be credited with the checks that produced the grades, not with the sweep of the channels.`
**给理由**（响应 A 2.3）：supply 级通道读法接近学界既有共识，若仍列首贡献，外审极易以「主张弱、近常识」攻其立意；判据装置（三检查＋两档＋词典＋映射）才是可防御的增量，故升主；摘要叙述结构未动（叙述流不含贡献序号）。

---

## ⑥【重大】Channel III 熵通道降级＋T 检查对真实时序重跑（对应 Reviewer A 2.1；综合报告重大第 6 条）

**§4 标题**（行 114）：`A Fictional Quantity Becomes an Engineering Quantity` → `An Abstract Quantity Becomes an Engineering Quantity`

**摘要与 §4.1 归类改述**：
- 摘要（行 5）：`entropy as a fictional quantity that entered engineering by isomorphism` → `entropy as an abstract quantity, defined over an idealized object, that entered engineering by formal analogy`
- §4.1（行 118）整段重写：`The fiction here is not a story but a definitional act` → `The input is a definitional act… The channel is classified accordingly as abstract-quantity/formal-analogy rather than fiction proper, and one fact settles the classification: statistical mechanics had given entropy a statistical reading over microstates long before the quantity was defined over message ensembles, so the physical quantity is the elder of the two and the channel cannot claim that the abstract preceded the physical.`
- §4.1 例证段（行 120）：`The definitional act is the fictional step` → `The definitional act is the abstracting step`；并前置时序事实：`roughly seventy years before the information-theoretic definition, a precedence the T score below is graded against rather than around.`
- §4.2 Channel claim（行 128）：`A fictional quantity can enter engineering by isomorphism` → `An abstract quantity, defined over an idealized object by a datable act, can enter engineering by formal analogy … and the channel claims no priority of the abstract over the physical.`

**T 检查重跑记分**（§4.2，行 132）：
旧：`Each arrow is dated by its primary publication [R08], [R09], [R10]. This is the best-dated of the four channels. **Pass.**`
新：`*T (temporal priority), scored against the real chronology.* … The channel-level demand — the input preceding the scientific use credited to it — does not survive the chronology: statistical mechanics had given entropy a statistical reading over microstates roughly seventy years before Shannon's definitional act… **Scoped pass: arrow-level dating holds; the channel-level priority claim is downgraded, and the channel is labeled abstract-quantity/formal-analogy accordingly.**`

**「best-dated」修正**：全称级「best-dated of the four channels」删除；保留范围受限用法「at the arrow level, the best-dated material in this paper」（行 132）。

**§9.1 主表同步**（行 287）：行标签 `Channel III — quantitative` → `Channel III — abstract quantity`；T 单元格 → `Scoped pass — arrows publication-dated [R08]–[R10]; channel-level priority downgraded (statistical entropy predates the definition by roughly seventy years)`。§4.2 收尾段（行 136）与「Three patterns」段（行 292）同步改口径。

---

## ⑦【重大】§8.3 承重类比改述＋§7.4 T 锚降为 author-attested（对应 Reviewer A 6.1、5.2；综合报告重大第 6 条）

**§8.3 反向通道条件 (i)**（行 269）：
旧：`(i) it is traceable to the machine's internal model — the fictional input, in this paper's terms;`
新：`(i) it is traceable to the machine's internal model — an input this paper treats as fiction-analogous rather than as a fictional input: whether a learned world model counts as a fiction in the sense of §2–§5 is a definitional question this paper does not settle, and the agenda does not lean on the answer;`

**§7.4 T 锚改标 author-attested freeze**（行 245）：
旧：`anchored by the frozen record itself, the strongest anchor this tier offers. … the temporal ordering the check demands is recorded by the artifact itself, not by testimony.`
新：`anchored by the frozen record, with the anchor's standing stated plainly: this is an author-attested freeze. A digest can attest that the artifact was not altered after the fact; it cannot by itself attest to a party that did not build the system that the freeze preceded the runs — that ordering is recorded by the artifact and its protocol, both of which are the builders' own. The anchor is therefore the strongest the pre-registered tier can offer from inside the record, and weaker than the independent anchors — dictionary records, primary texts, dated publications — that carry the historical channels: it buys verifiability, not independence. … The instance therefore passes T and R on the pre-registered tier, T on an author-attested anchor of lesser independence than the historical rows…`

**§9.1 主表同步**（行 289）：`Pass (artifact-dated; pre-registered tier)` → `Pass (author-attested freeze; pre-registered tier — §7.4)`；「Three patterns」段同步注明与独立锚的强度差。

---

## ⑧【重大】D 处置词典统一＋§9 自我指涉名实相符＋§9.2 selection effect 落实到句（对应 Reviewer A 5.3、7.1、2.2；综合报告重大第 7/8 条相关）

**D 词典**（§1.2 新增段，行 36）：`The D check returns one of four dispositions, and the dictionary is stated once here… **Partial pass**…(Channel I). **Unresolved by design**…(Channel II). **Indeterminate**…(Channels III and IV). **Out of scope**: the claim never invokes indispensability, so the check has no target (the §7 instance, whose claim rests on executability). The four labels state different reasons the check stops short of a verdict…`

**「同一理由两样标签」消除**：§7.4（行 245）旧句 `with D out of scope by the same reasoning as Channel II's grading` 删除，改挂词典：`D is out of scope per the disposition dictionary of §1.2`；§9.1 表 D 单元格（行 289）补 `Out of scope (no indispensability claim)`。

**§9 自我指涉对齐**（行 277 开篇 ＋ 行 294 新增段）：
开篇旧：`This closing section scores the paper's own claims on the paper's own checks, states the limitations, and re-records the kill lines.`
开篇新：`This closing section scores the paper's cases on the paper's own checks (§9.1), turns the same checks on the paper's own thesis, states the limitations (§9.2), and re-records the kill lines (§9.3).`
新增 `**The paper on its own checks.**` 段（行 294）：对论文自身论点真正跑一遍三检查，结论如实：`The paper's self-score is therefore T partial (the pre-commitment is narrow), D partial (downgraded to supply), R pending.` ——「Criteria Turned on Themselves」自此名实相符。

**§9.2 selection effect 落实到句**（行 298）：
旧：`Selection effect: the four channels are visible because their cases left anchors; feedback that left no record is invisible to this method, and the typology is a typology of the documented.`
新增续句：`The same effect reaches the scores: T and R pass in every scored row of §9.1 partly because the cases were selected for anchorability and for leaving residue — a case with no dated priority or no residue would not have entered the pool — so the uniform T and R passes are, in part, a product of case selection rather than an independent finding about the world. D, which the cases were not selected to pass, is where the selection pressure shows least, and the scores show it.`

---

## ⑨【重大】§1.2 delimitation 与 §8/§9.1 主表口径对齐＋mixing/porting 边界（对应 Reviewer A 9.1；综合报告重大第 8 条相关）

**§9.1 主表末行**（行 290）：
旧：`| Reverse channel (§8) | Pending — hangs on F-C3 | Pending | Pending |`
新：`| Reverse channel (§8) | Not applicable — §8 asserts no empirical claim; F-C3 is an agenda condition, not a pending verdict | Not applicable | Not applicable |`
「Three patterns」段（行 292）末句同步：`The last row is not a score: §8 makes no empirical claim, so its cells read not applicable rather than pending… The row is retained so the table records the boundary of what is scored.`

**mixing/porting 一句话划界**（§1.2 两档段末，行 38）：
`The boundary between mixing and porting is drawn in one sentence: mixing would be an evidence operation — a historical claim borrowing the authority of an adjudication verdict, or a verdict product borrowing the authority of an anchor — and it never happens; porting, in §6 and §8, is a criteria operation — the checks and mapping rows are carried across tiers and re-instantiated at the receiving tier's own evidential grade, so the criteria travel while the evidence grades stay separate.`

---

## ⑩【次要】字段路径精确化与核验措辞对齐（对应 Reviewer B R-1/R-2/R-4；Reviewer A 8.4；综合报告次要第 7 条）

**R-1**（§7.1 E，行 231）：`P1a_deviation.max_dev_inf` → `verdict.P1a_deviation.max_dev_inf`（与 JSON 实际结构一致；`verdict.T_P1b.min_cosine` 原本已带前缀，不动）。

**R-2**（§7.3(i)，行 239）：
旧：`(results/anon_v20_crossval.json · hybrid_lambda_convex=0.5 per-graph fields)`
新：`(results/anon_v20_crossval.json · per-graph fields prior_arm_eval.<graph>.hybrid_norm@0.5)`（λ=0.5 仍在正文以自然语言表述，配置常量字段名不再误作数据字段。）

**R-4**：`docs/` 前缀属 camera-ready 版口径，随②并入 §7 开篇注记处理（裸文件名＋路径前缀 camera-ready 恢复）。

**§1.3(ii)**（行 52）：
旧：`every entry was verified against primary records, and two entries carry unstable identifier snapshots, flagged in the reference list and to be completed before submission.`
新：`forty-three entries were verified against primary records; two ([R13], [R14]) carry unstable identifier snapshots — anchored by primary-source descriptors, flagged in the reference list, and to be completed in the pre-submission verification round — and the four entries added at the second-round verification pass ([R42]–[R45]) carry that pass as their verification record.`

**同步**：§9 AI 披露（行 304）补 `with the two identifier-pending entries flagged in §1.3(ii)`；§9.2 边界条件（行 298）`forty-five verified items` → `forty-five items (verification status as declared in §1.3(ii))`（消除本轮新引入的口径冲突）。

---

## 纪律自检（脚本核验，非目测）

| 项 | 结果 |
|---|---|
| 基线 SHA 核对 | `5e6f433be2d6…` 逐位一致后才动手 |
| thesis 句两处逐字同步 | 摘要＝§1.2（去斜杠后逐字一致），全文恰出现 2 次 |
| References 节 | 与基线逐字节相同（45 条编号与表不动） |
| 引用闭环 | 正文引用无删除，新增复引均为既有 [Rnn]（R38/R39/R08/R10/R13/R14/R42/R45）；R01–R45 全部仍在正文出现 |
| 关键数字保真 | 2.220446049250313 / 0.8569 / 4/3 / 0.484→0.452 / 0.783→0.739 / 0.97 / 0.85(×2) / 0.899 / 6,760 / 0.669 全部 1:1（含计数） |
| 五锚 SHA | 五个 12 位前缀逐一在场、未改动 |
| 负面结果披露 | §7.1 E／§7.2／§7.3 全部负面数字与「disclosed as-is / assets」措辞完整保留，未削弱 |
| 残留扫描 | deposon / Deposon / keep the books / fictional quantity / Pending / cited here anonymously 全部 0 命中；best-dated 仅存范围受限用法 |
| decidable 去向 | 仅存 §1.2 保留义声明（"Decidable" 大写定义处）＋§8.3 预注册层两处，与两档拆分一致 |
| 红线 | first/only 扫描均为普通序数/范围限定用法，无优先权主张；无档位/元表述新增 |

## 本轮未动（留待下轮）

1. **排版层**（戴夫）：2 处 markdown `#` 残留＋PDF 首页标题重复＋R-3——按派单归下轮重排。
2. **文献层**（阿兰并行补检）：R38/R39 之外的预注册/可证伪原始文献、R14/R36/R37 三类引用待核——入池后合并（正文已留「scheduled verification pass」接口句）。
3. **Reviewer A 未派单项**：F-C1/F-C4 强度（3.2/3.3）、F-C3 元条件性质（6.2）、「structural isomorphism」措辞（4.2）、反例缺一个 Fail 案例（8.5）——不在本轮派单范围，未动。
