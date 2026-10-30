# Reviewer B 独立评审原文（子代理评审）

- 通路代号：OpenRouter
- 模型：x-ai/grok-4.6
- 会话：单轮独立会话（不与 Reviewer A 共享任何上下文）
- 请求参数：temperature=0.4, max_tokens=16000, attempt=1, 耗时247.6s
- token 用量：prompt=47686, completion=14131
- finish_reason=stop

---

# 五维审计报告（Pass 2 / 双盲外审）

审稿范围仅限本次提供的 `PAPER_MD`、`PAPER_TEX`、`COMPILE_CV`。未对冻结 JSON / 机密仓库做外部复算；凡涉及“记录是否真实存在”，只评价正文口径与材料内互证，不臆测材料外事实。

---

## 维度一：结果

【结论】PASS

【定位与证据】

L237–L239：

> The adjudication layer is frozen before runs as pure verdict functions with published SHA-256 anchors, given as twelve-character prefixes: GT_FORMALIZATION_v1.md aeefb8ef6972; run_v21_gtformal.py 9bbe43f41fa8; run_v22_p1c.py 6e9673205dc0; SPEC_GT2B.md 68a5b08ef007; SPEC_GT8C.md 6b09de9911c0 (frozen handoff artifact, field preregistration_anchors_sha256_12). Every key number below maps to a frozen field; hand-copying is forbidden by the artifact's own protocol.

> The conservation identity survives audit: the maximum per-path deviation across all variants and benchmarks is 2.220446049250313×10⁻¹⁶ — the scale of double-precision machine epsilon, against an implementation tolerance of 10⁻⁶ — closed (pre-registered) (results/anon_benchmark_v1_4_gsm8k.json · physics_audit.t_plus_r_plus_a_max_deviation). The quantified coordination reading lands at median ECR = 4/3 over the 17 finite-valued graphs, with coverage of 20 of 22 graphs — three graphs read Infinity, two graphs lack arm data, both disclosed as-is (frozen handoff artifact, field headline_results.GT4_ECR). The dynamical tier dies: the kill protocol is systematic in its graph sampling (61 graphs in five families) and complete at the state level (all 6,760 states of the 338-task corpus, 20 steps each — frozen handoff artifact, field headline_results.enumeration_scope), and all three formalized dynamical-equivalence propositions are falsified — P1a: maximum deviation 0.8569, an O(1) gap that does not vanish with step size; T-P1b: minimum directional cosine −1.0; T-P1c: killed on both lines, with an 81-point grid over τ∈[0,4] reaching minimum cosine −1.0 at the best global τ and per-state optimal τ∗ again reaching −1.0, the per-state τ∗ median being 0 (frozen handoff artifact, field headline_results.P1a_P1b_T_P1c; source results results/anon_v22_p1c.json · verdict.min_cos_at_best_global_tau and verdict.min_cos_per_state_best_tau; measured fields for P1a and T-P1b in results/anon_v21_gtformal.json · verdict.P1a_deviation.max_dev_inf and verdict.T_P1b.min_cosine). The potential-game reading is downgraded accordingly, to approximate (cyclic-graph median residual 0.669; frozen handoff artifact, field headline_results.P2).

L247：

> On real benchmarks the layer is indistinguishable from a trivial six-keyword rule filter reading nothing beyond label strings — on GSM8K the filter scores 0.87 against the layer's 0.85 (McNemar p=0.5), on StrategyQA 0.899 against 0.899 (p=1.0) — and at these sample sizes the detectable-difference threshold is roughly ±10 percentage points, so smaller increments are not excluded — disclosed as-is (frozen handoff artifact, field headline_results.E9_5_power_honest; artifact results/anon_v22_e95ci.json). Plain chain-of-thought significantly outperforms the layer on GSM8K, 0.97 versus 0.85 (results/anon_benchmark_v1_4_gsm8k.json · cot_baseline_accuracy and unified_accuracy). Fusion with a semantic prior dilutes rather than helps: physics 0.484→0.452 and historical 0.783→0.739 at the λ=0.5 convex combination (results/anon_v20_crossval.json · per-graph fields prior_arm_eval.<graph>.hybrid_norm@0.5). None of these numbers is massaged out of the record.

L136 / L140–L142（§4 定量口径）：

> An abstract quantity, defined over an idealized object by a datable act, can enter engineering by formal analogy and flow back into physics at a measurable cost; every arrow in the circuit has an anchor, and the channel claims no priority of the abstract over the physical.

> Scoped pass: arrow-level dating holds; the channel-level priority claim is downgraded, and the channel is labeled abstract-quantity/formal-analogy accordingly.

T326 / T334：与上引 §7.1 / §7.3 数值、字段路径一致（守恒偏差、ECR、6760/338/20、P1a 0.8569、余弦 −1.0、残差 0.669、McNemar p、滤波对照、融合稀释）。

【分析】

工程实例内部算术自洽：`338 × 20 = 6,760`；`17` 个有限值图 + `3` 个 Infinity + `2` 个缺臂 = `22`，覆盖 `20/22` 恰为去掉缺臂后的集合；守恒最大偏差 `2.220446049250313×10⁻¹⁶` 与正文“double-precision machine epsilon”及容差 `10⁻⁶` 同向，判定为 pre-registered closed。动力学三条命题均给出可对照的杀线读数（O(1) 偏差、余弦 −1.0、τ 网格双线击穿），并与“dynamical tier dies / potential-game downgraded to approximate”对齐。滤波对照、CoT 反超、融合稀释均原样给出，负面结果未粉饰。

§4 不宣称抽象量优先于物理熵，T 分被显式降为 scoped pass，与“七十 years”的编年口径一致；H 公式与 Landauer `kT·ln2` 作为具名公式/价格出现，不与 §7 实验数混用。MD 与 TEX 对应段落数值无分叉。

保留点（不构成 FAIL）：本次材料不含 `results/anon_*.json`，故不能对字段做字节级复算；McNemar 未给出 n（但已给 ±10pp 可检测阈值）。另，L134 称 Shannon 与物理分布是 “not a similar expression, the same one”，而热力学侧通常差因子 k / 对数底，属修辞过满，但频道主张本身已降级，且不进入 §7 预登记杀线。综合：定量口径自洽、杀线对应关系在文本层成立、负面结果如实呈现。

---

## 维度二：讨论

【结论】PASS

【定位与证据】

L170–L176 / L178（§5，主张停在供给层）：

> Narrative fiction both supplies vocabulary and sets agendas; the evidence is graded by anchor type, and every grade has an anchor.

> the flagship case is one case; the vocabulary is supply, not necessity; the quantitative tier measures association, not mechanism.

> We do not assert the strength or the direction of the association here

L247–L249（§7.3，未做跨 backbone / 普遍性宣称）：

> the capability channel reads zero.

> its magnitude is not comparable to the non-Euclidean case, and nothing in this paper claims otherwise.

> No uniqueness claim is made about the instance; the positioning is exactly "engineering-grade, mid-strength."

L253（§7.4）与 L291–L297（§9.1 master table）对读：

> The instance therefore passes T and R on the pre-registered tier, T on an author-attested anchor of lesser independence than the historical rows, with D out of scope

> Pipeline instance (§7) | Pass (author-attested freeze; pre-registered tier — §7.4) | Out of scope (no indispensability claim) | Pass

L293–L296 与 §2–§5 分档一致：Channel I `Partial pass`；II `Unresolved by design`；III `Scoped pass` / `Indeterminate`；IV `Pass` / `Indeterminate`。

L300：

> §8 asserts no empirical claim; F-C3 is an agenda condition, not a pending verdict

【分析】

§5 把旗舰案例限制为“one case”、词汇为供给、定量层为关联而非机制，未从单例推出规律。§7.3 明确 capability=0、量级不可比、非独特性，正文未见跨 backbone 稳健性或普遍性主张。§9.1 声明 “nothing is re-scored”，分档与 §2–§5、§7.4 逐行可对上；反向通道整行 N/A，与 §8 范围声明一致。

轻微张力：L243 写 “an artifact whose falsifiable claims all died under pre-registered functions”，而同节及 L239 已记录守恒恒等式 **通过**。若“falsifiable claims”含守恒审计，则该句过满；更合理的读法是专指三条动力学等价命题。此为修辞不严谨，尚未把讨论整体推离结果支持范围，故不降为 GRAY。

---

## 维度三：局限

【结论】PASS

【定位与证据】

L306（§9.2 四条局限 + 两条边界）：

> Selection effect: the four channels are visible because their cases left anchors; feedback that left no record is invisible to this method, and the typology is a typology of the documented. The same effect reaches the scores: T and R pass in every scored row of §9.1 partly because the cases were selected for anchorability and for leaving residue … Scale: each channel carries a small number of flagship cases, and the pipeline has one engineering-grade instance; no prevalence claim is made anywhere in this paper. Magnitude: structural isomorphism to the non-Euclidean pattern does not make the engineering instance comparable to it in scale, and §7.3 declines the comparison. Tiers: the historical tier and the pre-registered tier are different instruments, and nothing in §2–§5 borrows the authority of §7's. Two boundary conditions close the list: the reference pool is closed at fifty-four items … and the novelty statements rest on the three-line search completed on 2026-09-16

L44 / L109（D 的裁决力上限，写入主张而非藏在附录）：

> none of them is a verdict of indispensability; no channel in this paper claims one.

L223 / T310（评审期 M4 仅部分满足）：

> The requirement is therefore only partially met while the paper is under review, and the limit is stated in §7.1, where it applies.

L239 / L253（作者自证冻结弱于独立锚；公开文本不可执行第三方复算）：

> A reviewer working from the public text alone therefore cannot execute the recomputation that M4 asks of a third party, and this paper does not claim otherwise

> A digest can attest that the artifact was not altered after the fact; it cannot by itself attest to a party that did not build the system that the freeze preceded the runs

L60 / L316（标识符未完成条目）：

> two ([R13], [R14]) carry unstable identifier snapshots

【分析】

自披露覆盖了本材料内最主要的已知弱点：选择效应对 T/R 的污染、单实例/无流行率、量级不可比、两套证据阶不混用、闭池、新颖性检索日期门、D 从不宣称不可缺、评审期第三方可执行性缺口、锚的独立性上限、R13/R14 标识符待补。与正文其他位置的自我降级（Channel I supply-level、Channel III 非 fiction proper、论文自打分 T partial / D partial / R pending）同向，未发现“材料内已坐实、却在 §9.2 系统性隐瞒”的硬伤。

未单列、但属轻微应加强处：L243 “independent rerun” 未定义独立于作者还是仅第二双手，与 L223 “built and run by its own authors” 并置时独立性偏弱；Helmholtz 在 L68 无池编号，而 Riemann/Clifford 有 [R53]/[R54]。这些不足以否定局限节的诚实性。

---

## 维度四：五锚不变式

【结论】PASS

【定位与证据】

L237（PAPER_MD，预登记语境，五锚并列一次）：

> published SHA-256 anchors, given as twelve-character prefixes: GT_FORMALIZATION_v1.md aeefb8ef6972; run_v21_gtformal.py 9bbe43f41fa8; run_v22_p1c.py 6e9673205dc0; SPEC_GT2B.md 68a5b08ef007; SPEC_GT8C.md 6b09de9911c0 (frozen handoff artifact, field preregistration_anchors_sha256_12)

T324（PAPER_TEX，同一预登记句，文件名加 `\allowbreak`，十二位前缀未改）：

> published SHA-256 anchors, given as twelve-character prefixes: `GT_FORMALIZATION_v1.md` aeefb8ef6972; `run_v21_gtformal.py` 9bbe43f41fa8; `run_v22_p1c.py` 6e9673205dc0; `SPEC_GT2B.md` 68a5b08ef007; `SPEC_GT8C.md` 6b09de9911c0 (frozen handoff artifact, field `preregistration_anchors_sha256_12`)

C51 / C64 / C105–C106（COMPILE_CV 互证）：

> [PASS] S4-五锚不变式: aeefb8ef6972:1 9bbe43f41fa8:1 6e9673205dc0:1 68a5b08ef007:1 6b09de9911c0:1

> [PASS] G5-五锚哈希串: aeefb8ef6972→p[15] 9bbe43f41fa8→p[15] 6e9673205dc0→p[15] 68a5b08ef007→p[15] 6b09de9911c0→p[15]

> 五锚哈希串（aeefb8ef6972/9bbe43f41fa8/6e9673205dc0/68a5b08ef007/6b09de9911c0）：各恰 1 次，全部 p15

【分析】

在所供 PAPER_MD 与 PAPER_TEX 正文中，五个 SHA-12 前缀均只出现于 §7.1 预登记冻结句，上下文同为 “frozen before runs as pure verdict functions”。COMPILE_CV 的 S4 计数为各 1 次，G5 页面级落在 p15，与 TEX 该段位置互证。匿名化声明（L229）称匿名化 “touches no anchor digest”，与五锚在 MD/TEX 中保持原串一致。不变式成立。

---

## 维度五：可复现性

【结论】PASS

【定位与证据】

L62 / L229：

> every number in this paper is either bibliographic … or an experimental number cited by field path into the frozen record examined in §7.

> every number is cited by its field path into the frozen record.

L239 字段路径链（节选，完整链见维度一引文）：

> results/anon_benchmark_v1_4_gsm8k.json · physics_audit.t_plus_r_plus_a_max_deviation

> headline_results.GT4_ECR

> headline_results.enumeration_scope

> headline_results.P1a_P1b_T_P1c

> results/anon_v22_p1c.json · verdict.min_cos_at_best_global_tau and verdict.min_cos_per_state_best_tau

> results/anon_v21_gtformal.json · verdict.P1a_deviation.max_dev_inf and verdict.T_P1b.min_cosine

> headline_results.P2

L247 续链：

> headline_results.E9_5_power_honest; artifact results/anon_v22_e95ci.json

> results/anon_benchmark_v1_4_gsm8k.json · cot_baseline_accuracy and unified_accuracy

> results/anon_v20_crossval.json · per-graph fields prior_arm_eval.<graph>.hybrid_norm@0.5

L239 / T326（第三方通道与限制，未把公开文本说成可执行）：

> the complete frozen repository and the full SHA-256 digests — not only the twelve-character prefixes printed above — are provided to the editors and reviewers through a confidential channel, per double-blind discipline, and the public pointer is deferred to camera-ready. A reviewer working from the public text alone therefore cannot execute the recomputation that M4 asks of a third party, and this paper does not claim otherwise: during review, M4's third-party recomputation runs through the confidential channel or not at all.

L223：

> executable is a standing demand, not a report of who has executed. … public executability is deferred to camera-ready.

L253（预登记层证据能买到什么、买不到什么）：

> The five published anchor prefixes date the formalization and the verdict functions to before the runs they adjudicate, on the artifact's own attestation, and the master table records the difference in standing.

【分析】

正文对 §7 每个关键数字都给出 `results/anon_*.json` 或 `headline_results.*` 路径，禁止手抄的协议与“数字必须指向冻结字段”的元规则一致；占位符 `<graph>` 标了 per-graph 语义，仍可追溯到具体键模式。第三方复算被明确分成：公开文本不可执行；编辑/审稿人走 confidential channel；camera-ready 再公开指针。这与 M4“第三方可复算”的规范需求之间的缺口写在适用点（§7.1），而非藏到脚注。预登记层公开证据是 SHA-12 前缀 + 字段路径 + 作者自证时序；全文同时写明完整 SHA-256 与仓库不在公开文本、时序独立性不能由摘要单独证明——声明与所供证据等级匹配，没有把“可验证未被事后篡改”说成“可向非建造者独立证明冻结先于运行”。

本次三份材料不含冻结仓，故本审计不能确认路径在字节层可解析；该限制已被论文自身声明，不构成“宣称与证据不匹配”。

---

## 总评

整体印象：这是一篇自我约束明显强于常见 position paper 的稿件。主张分层（历史可再检查 vs 预登记可证伪）、D 的四处 disposition 词典、master table 与分节评分一致、工程实例把守恒通过与动力学击穿、滤波/CoT/融合负面结果并列写出，并主动收窄反向通道与量级类比。五锚在 MD/TEX/编译记录三方计数为 1，编译门禁记录全绿。五维均判 PASS，不等于没有可改的毛刺。

**问题清单（含轻微）**

1. **修辞与结果不完全贴合（轻微）** — L243 “falsifiable claims all died” 与 L239 守恒恒等式 closed/pass 并置，易被读成全杀；建议改成专指三条动力学命题。
2. **§4 “the same one” 过满（轻微）** — L134 称 H 与物理分布是同一表达式而非相似式；热力学侧通常含 k 与对数底差异。频道主张已降级，但不妨改回 “identity of form”。
3. **McNemar 缺样本量表（轻微）** — L247 给出 p=0.5 / p=1.0 与 ±10pp 阈值，未给 n；不影响“无显著差异”方向，但复算对照表会不完整。
4. **“independent rerun” 独立性未定义（轻微，局限未单列）** — L243 vs L223 作者自建自跑；§9.2 未点明第二双手是否外部。
5. **Helmholtz 无池编号（轻微）** — L68 与已补的 [R53]/[R54] 不对称。
6. **COMPILE_CV 首现序与 PAPER_MD 不完全同构（记录层轻微）** — C99 作 `R01, R54, R13, …`，而正文 L60 已出现 `[R13], [R14], [R42]` 等，早于 L70 的 [R01]。不影响五锚与 54 条覆盖（C54–C55 仍为 54/54），但“首现序”字段不可当作正文指针证据。
7. **公开可复现性按设计不完整（已披露，非隐瞒）** — 评审期 M4 只经 confidential channel；本审计材料无 JSON，故字段路径的字节级存在性仍待该通道验证。
8. **排版 Underfull 已披露、不入内容门禁** — C73/C82–C87，badness 三处，Overfull 为零；与五维无关。

未发现数据自相矛盾到足以推翻 §7 预登记叙事、master table 分档造假、五锚重复/缺失、或把反向通道/跨 backbone 稳健性写成已证结论的情形。