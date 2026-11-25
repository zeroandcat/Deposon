AI-use disclosure: AI assistance was used to read and cross-check the local commission and evidence, and to draft this reply. No experiment or external literature search was performed.

I read the full 367-line commission, SHA-12 `a397621085d6`, at `_repo_mirror\letters\_commission_c4_values_EN_2026_10_10.md`.

```text
Model actually used: Codex; this session identifies itself as based on GPT-6. The exact serving model/build identifier is unavailable to this assistant.
Serving endpoint: unavailable to this assistant.
Model string requested at the endpoint: unavailable to this assistant.
Date of the call: 2026-10-10, Asia/Shanghai; exact request time unavailable.
Verification status: model/build, endpoint, and request.model cannot be independently matched from this session; compare with forwarding metadata.
```

**Reply: C4 values**

I cannot supply sourced values for T-1 through T-4 from the current on-disk material. I therefore enter `null` for every requested cell and family slot. This is the commission's expressly accepted non-availability answer, not a proposed value, formula, verdict, or adoption request. It follows the zeroing rule: absent definitions cannot be replaced by estimates or self-authored theory.

The response below addresses only the missing values. The previous reply already delivered T-1's construction rule and 15-cell coverage, T-4's caliber and five family slots, and the source attributions; I do not reproduce or re-derive those results. Its recorded finding remains “construction rule derivable / values not derivable” ([prior reply, SHA-12 `7558eb1a5e34`](_repo_mirror/letters/_codex_theory_derivation_reply_2026_09_30.md:155), line 155).

**Per-cell status**

`null` means no computable, sourced value was found in the cited material. “Value source: none” is intentional; the citations identify the on-disk definition and the documented missing input, not a source for a value that does not exist. Evidence keys are expanded below with exact paths, SHA-12 values, and line citations. The table lists all 5 task families × 3 mechanisms as requested.

| Cell | T-1 `u*(a_t)` | T-2 `L(M,T)` | T-3 `U(M,T)` | T-4 `max_u(T)` |
|---|---|---|---|---|
| M1 × T1 | `null` [S1, R1, R3] | `null` [S2, R2] | `null` [S3, R2] | `null` [S1, R4] |
| M1 × T2 | `null` [S1, R1, R3] | `null` [S2, R2] | `null` [S3, R2] | `null` [S1, R4] |
| M1 × T3 | `null` [S1, R1, R3] | `null` [S2, R2] | `null` [S3, R2] | `null` [S1, R4] |
| M1 × T4 | `null` [S1, R1, R3] | `null` [S2, R2] | `null` [S3, R2] | `null` [S1, R4] |
| M1 × T5 | `null` [S1, R1, R3] | `null` [S2, R2] | `null` [S3, R2] | `null` [S1, R4] |
| M2 × T1 | `null` [S1, R1] | `null` [S2, R2] | `null` [S3, R2] | `null` [S1, R4] |
| M2 × T2 | `null` [S1, R1] | `null` [S2, R2] | `null` [S3, R2] | `null` [S1, R4] |
| M2 × T3 | `null` [S1, R1] | `null` [S2, R2] | `null` [S3, R2] | `null` [S1, R4] |
| M2 × T4 | `null` [S1, R1] | `null` [S2, R2] | `null` [S3, R2] | `null` [S1, R4] |
| M2 × T5 | `null` [S1, R1] | `null` [S2, R2] | `null` [S3, R2] | `null` [S1, R4] |
| M3 × T1 | `null` [S1, R1] | `null` [S2, R2] | `null` [S3, R2] | `null` [S1, R4] |
| M3 × T2 | `null` [S1, R1] | `null` [S2, R2] | `null` [S3, R2] | `null` [S1, R4] |
| M3 × T3 | `null` [S1, R1] | `null` [S2, R2] | `null` [S3, R2] | `null` [S1, R4] |
| M3 × T4 | `null` [S1, R1] | `null` [S2, R2] | `null` [S3, R2] | `null` [S1, R4] |
| M3 × T5 | `null` [S1, R1] | `null` [S2, R2] | `null` [S3, R2] | `null` [S1, R4] |

For T-4 the repeated entry is one family-indexed slot shown on each of that family's three mechanism cells, because the spec indexes `max_u` by task family, not by mechanism. Its value source is absent in all five families. The task-family scope requires five attributed entries; it does not establish that the five numerical values must differ.

**Basis and item-specific blockers**

- **T-1:** No value can be evaluated without the payoff function `u` and its scale, unit, and range. The spec names `u*(a_t)` as a payoff but supplies no payoff function. The prior reply reports a repository-wide sweep that found no payoff scale, unit, range, or per-family value. The current Bayesian-baseline design adds a requirement that both arms use the same payoff construction and leaves that construction for PI decision; it does not supply one. For M1 cells, the prior reply also records that the mechanism's field and conservation constraint lack parameterization. No cell-specific `u*` values or payoff function can therefore be attributed.
- **T-2:** The spec names `IC capacity` and mechanism identifiability as the bases for `L`, but the prior reply reports that these terms have no definitions, expressions, criteria, or values on disk. Without those bases and the payoff scale, no cell-specific lower bound is computable or sourceable.
- **T-3:** The spec names a mechanism convergence condition as the basis for `U`, but does not state that condition's definition or a value-producing map. The prior reply records no definition, expression, or value for it. Without the payoff scale and a sourced, cell-applicable convergence condition, every `U` entry remains null.
- **T-4:** `max_u` is defined only as a payoff upper bound normalized by task family. Since `u` and its scale are absent, no family-specific upper bound can be computed. I do not infer values from task labels, sample counts, Nash terminology, or any adjacent metric.

**Evidence key**

- **C1 — requested cell and family shapes:** [commission, SHA-12 `a397621085d6`](_repo_mirror/letters/_commission_c4_values_EN_2026_10_10.md:52), lines 52–55. T-1, T-2, and T-3 require per-cell values or nulls with reasons and sources; T-4 asks for five family values with per-cell sources.
- **C2 — accepted non-availability answer:** [commission, SHA-12 `a397621085d6`](_repo_mirror/letters/_commission_c4_values_EN_2026_10_10.md:82), lines 82–91. Explicit non-availability with reasons, basis, and what would unblock it is complete; guesses and substitute formulas are rejected.
- **S1 — task/mechanism and payoff literals:** [spec, SHA-12 `423c84de20d5`](_repo_mirror/docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md:42), lines 42–66. The spec names the task families, mechanisms, and payoff symbols/normalizer; it contains no payoff function or numerical value in those definitions.
- **S2 — lower-bound literal:** [spec, SHA-12 `423c84de20d5`](_repo_mirror/docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md:70), lines 70–76. It names `IC capacity` and mechanism identifiability for `L`.
- **S3 — upper-bound literal:** [spec, SHA-12 `423c84de20d5`](_repo_mirror/docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md:75), line 76. It names a mechanism convergence condition for `U`.
- **R1 — payoff gap and search already recorded:** [prior reply, SHA-12 `7558eb1a5e34`](_repo_mirror/letters/_codex_theory_derivation_reply_2026_09_30.md:731), lines 731, 733, 735–738. It reports a repo-wide search over `支付`, `奖励`, `reward`, `准确率`, `归一`, `0/1`, and `纳什`; it found no payoff scale, unit, range, or per-family value and records that all four inputs depend on `u`.
- **R2 — missing bound bases:** [prior reply, SHA-12 `7558eb1a5e34`](_repo_mirror/letters/_codex_theory_derivation_reply_2026_09_30.md:771), lines 771, 774, 776, 784. It reports the three named bases as undefined and says the bounds cannot be evaluated from them.
- **R3 — M1-specific gap in prior T-1 coverage:** [prior reply, SHA-12 `7558eb1a5e34`](_repo_mirror/letters/_codex_theory_derivation_reply_2026_09_30.md:292), lines 292, 311–314. This is carried from the prior answer and is not re-derived here.
- **R4 — prior T-4 family nulls:** [prior reply, SHA-12 `7558eb1a5e34`](_repo_mirror/letters/_codex_theory_derivation_reply_2026_09_30.md:629), lines 629, 631–641. It records five family-indexed nulls and the upstream `u` gap.
- **P1 — frozen C4 zeroing rule:** [preregistration, SHA-12 `4185bdad6df5`](_repo_mirror/results/_v5_item21_rerun_conditions_prereg_2026_09_28.md:221), lines 221, 225–234. A missing item is not computable and may not be filled with an estimate, substitute, or self-invented formula.
- **B1 — current Bayesian-baseline design:** [design draft, SHA-12 `7e181a167702`](_repo_mirror/results/_bayesian_baseline_design_2026_10_10.md:86), lines 86, 93–97. It requires both arms to share one payoff construction and leaves that choice with the PI; it supplies no payoff function or scale. This full 232-line draft was read for this reply.
- **G1 — canonical source declaration:** [C4 correction register, SHA-12 `61b139efd0ef`](_repo_mirror/results/_c4_theory_source_caliber_correction_2026_09_30.md:120), lines 120–126. The register records the PI's 2026-09-30 source-name ruling and the still-open derivation boundary. The questionnaire itself was not read; I cite the on-disk register, not an unavailable original record.

**Canonical declaration carried from the register**

> 「理论界来源 ＝ codex 推导（PI 2026-09-30 采认；来源名按实际执行方更新——执行方择定＝codex，`ask_da8ce88762c1f39cb62e95f4` q1／q2；原字面「GLM 推导」历史留痕、0 回改）；0 自创 / 0 自拟公式，沿 C4.9 归零纪律」＋可核来源标注（给出人 / 出处）

This reproduces the canonical wording at [C4 correction register, SHA-12 `61b139efd0ef`](_repo_mirror/results/_c4_theory_source_caliber_correction_2026_09_30.md:122), as required by [commission, SHA-12 `a397621085d6`](_repo_mirror/letters/_commission_c4_values_EN_2026_10_10.md:247), lines 247 and 255–261. The source attribution here is to the register and commission for the declaration text; it is not a claim that this reply supplies theory values, authored the prior derivation, or resolves the register's open boundary about what counts as derivation versus self-drafted content.

**What would make the values obtainable**

1. An authorized source must define `u` for the task outcomes, including the payoff scale and units/range, and identify its applicability across all 15 cells. M1 additionally needs its mechanism-internal parameterization for any value that depends on it.
2. T-2 needs sourced definitions and cell applicability for both `IC capacity` and mechanism identifiability.
3. T-3 needs a sourced convergence condition, its mapping to a numeric `U`, and its applicability to each mechanism/task cell.
4. T-4 needs the five family-indexed `max_u` values on the same specified payoff scale, with the source attached to each family and its three cells.

These are missing inputs, not formulas proposed by me. The earlier reply's construction rules and constraints remain the delivered record; no value is inferred from them. The local evidence search used for this reply was the complete commission, the cited spec definitions, the cited prior-reply findings, the current C4 register and preregistration clauses, and a full read of the same-day Bayesian-baseline design. The prior reply's broader repository search is cited as a previously recorded search, not represented as a new search I performed. I made no external literature search because an external general theory cannot identify this project's payoff function or mechanism-specific inputs without a project source.

**Two qualifications to the commission's wording**

- The commission says that the presence of `U` would unblock the entire kill-line, but also records that `ε` and M1's internal parameters are outside this request and that even all four values would not by themselves make the kill-line landable. Read consistently, `U` is necessary to remove the `U`-dependent blocker; its presence alone is not sufficient to make terminal adjudication executable. Sources: [commission, SHA-12 `a397621085d6`](_repo_mirror/letters/_commission_c4_values_EN_2026_10_10.md:54), lines 54, 165, 332; [spec, SHA-12 `423c84de20d5`](_repo_mirror/docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md:68), lines 68–69.
- “Five numbers, not one universal constant” is a sound requirement about the answer's family indexing and attribution. The phrase “a single universal constant is excluded by the spec itself” should not be read as requiring five unequal numerical values: the spec calls `max_u` a task-family normalization constant, which requires five family entries, but does not say their values must differ. Sources: [commission, SHA-12 `a397621085d6`](_repo_mirror/letters/_commission_c4_values_EN_2026_10_10.md:55), line 55; [spec, SHA-12 `423c84de20d5`](_repo_mirror/docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md:66), line 66.

**Boundary**

This reply modifies no existing repository document, makes no adjudication for the PI or verdict-keeper, changes no threshold, and is not adopted automatically. I supply no value, formula, experiment, or verdict. The commission itself remains a draft with its addressee and release decision open to the PI.

**Fingerprint**

SHA-12, byte count, and line count are reported with delivery, outside this file. This file does not contain its own fingerprint.
