# V4 Experiment Design Invitation

**Large-Model Distillation, Reverse-Distillation, and Anti-Distillation — A One-Week Hook-Finding Pre-Screen Built on V1–V3 Assets**

**Document type:** Open invitation letter / experimental-design proposal (draft, version 0.2, 2026-09-20)
**Status:** Pre-circulation draft, awaiting recipient and host review
**Audience:** KIMI-K3 (凝子-agent), two Trae tracks (Trae code, Trae IDE), GLM, coze, plus newly invited VS, workbuddy, and 豆包工作
**Authorship:** Drafted by `doc-writer` (Mavis 8-agent team, deposon). Human principal investigator retains final approval and is the sole accountable author. AI is not an author.
**Confidentiality classification:** Open invitation. No unpublished manuscripts, peer-review material, sensitive or restricted data, PHI, proprietary content, or source documents are transmitted. Recipients receive the proposal only.

> **Revision banner — v0.2 (2026-09-20).** v0.1 → v0.2 is a **factual-correction patch**, not a content re-design. Five P0 issues (F1, F2, F4, A1, A2) were identified against the disk ground truth and remediated; v0.1 is preserved unmodified.
>
> 1. **P0-1 (A1) — `by_model/` directory names.** Four mentions of `corpus/v20/by_model/{KIMI, GLM_1, GLM_2, coze, M3}` corrected to the disk-truth `corpus/v20/by_model/{kimi, GLM_1, GLM_2, coze, minimax}` (lowercase `kimi`, lowercase `minimax` instead of `M3`). Affects §1.1, §2.1, §2.7, §5.2.
> 2. **P0-2 (A2) — V2 frozen-stack layering declaration.** A new sentence is added at §1.1 and §5.2 making explicit that V2 has two non-overlapping frozen layers: (i) the **9-backbone × 60-cell evaluation grid** (`results/boss_pa_1_rbr_rm_result_2026_09_15.json:27-29` n_models=9, n_540_total=540) at the model layer, and (ii) the **5 `by_model/` blind-test artifacts** (`corpus/v20/by_model/{kimi, GLM_1, GLM_2, coze, minimax}`) at the cross-vendor corpus layer. Track 1's stability denominator is the 5-artifact set; the 9-backbone grid is not a Track 1 input. §2.1's "three of the five frozen artifacts" is sharpened to "three of the five `by_model/` blind-test artifacts".
> 3. **P0-3 (F1) — V3 4-path verdict table.** The §5.3 table (and the §1.1 cross-reference) is rewritten against `results/deposon_v3_v7_summary_2026_09_11.json` and `results/d7_5anchor_60cells_9model_verdict_2026_09_18.json`: P-A **PASS** (26-cell / 2-model equilibrium-band; key_evidence "2 model 0.867 + V2 60 cells 86.67%"), P-C **DEAD** (R²=0.0007; same root as D7 `FAIL_H0 (幂律死)`), P-E **GRAY** (9 model 距 (1,0,0) [0.17, 0.62]; T-A corr -0.81), P-F **TRIGGERED** (verifiable-audit; D_fix2 sub-items `8+1+0 PARTIAL_PASS`). v0.1's `51/60` (a V2 phase-1 single-backbone doubao-seed-2.0-lite dpath) and `45/45` (a P-K closed-source 9m×5c audit cell) are scrubbed because they belong to other experiments, not the V3 V7 terminal verdicts.
> 4. **P0-4 (F2) — three embedding-frame artifact existence.** §2.4 (and the §0.2 / §4.1 / §2.1 cross-references) are re-honest: the Poincaré-distance frame has a **scaffolding-tier** artifact only (`deposon_team/plugins/_pg_v01_compute.py:424-443`, status `SCAFFOLDING (PRE-REGISTRATION, 等 D5 launch)`, `verdict_pending=true`; landing confirmed in `results/deposon_pg_v01_9m60c_2026_09_15.json:379-396`; 5 P-G anchor SHA-12 already computed at `:347-377`), and V4 makes **no calibrated-curvature claim** (`POINCARE_C = 1.0` is the V0 spec placeholder). The `observer-effect` and `Bell-inequality` frames have **no V1–V3 artifact on disk**; they are brainstorming seeds only. v0.1's "V4 reuses these frames" line is softened to "1 frame on scaffolding tier + 2 frames brainstorming-only".
> 5. **P0-5 (F4) — V3 终稿 version identifier.** All 8 mentions of `V3 终稿 R5` are corrected to **`V7`** (first occurrence written out as `V7 (docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md + results/deposon_v3_v7_summary_2026_09_11.json)`). The repository contains no `R5` file, manifest, or version marker; V7 is the authoritative V3-terminal-report version.
>
> **Untouched, listed at the end as `[待 PI 裁定]`:** the `21 caption-fingerprint pairs` figure (disk `corpus/v20/strip_captions_22.json` contains 22 captions). This patch does **not** rename that count; the principal investigator must decide whether the v0.1 figure or the disk figure is the canonical one.

---

## §0 Title and Abstract

### 0.1 Title

> **V4 Experiment Design: Large-Model Distillation, Reverse-Distillation, and Anti-Distillation on the deposon V1–V3 Asset Stack**

### 0.2 Abstract (three-part)

**Background.** The deposon program has, over V1 (FTFB, arXiv-anonymous 12-page double-blind), V2 (deposon v2, 9 backbone × 60 cells), and V3 (V3X one-week go/no-go, 4-path terminal verdicts on P-A / P-C / P-E / P-F plus P-L v3 three-state), accumulated a frozen, hash-anchored asset stack. Existing analyses have largely focused on *one* direction: either fitting a known hypothesis to the cells, or scoring backbones against an external rubric. None of the three V-tiers has examined whether the *distributional structure* of the cells, the *extracted mode set* of the responses, or the *defensive posture* against third-party extraction can be made operational as a reusable hook-finding pre-screen.

**Objective.** V4 proposes a three-track experiment — **distillation** (extracting stable mode sets from large and/or multi-backbone outputs), **reverse-distillation** (inferring the originating distribution from a distilled output), and **anti-distillation** (a new dimension, defined by the human principal investigator) — to convert the existing V1–V3 frozen asset stack into a one-week hook-finding pre-screen (V3.X style) for downstream research directions.

**Methods.** V4 inherits the V1–V3 frozen artifacts (verified SHA-12 manifests, 21 caption-fingerprint pairs [count `[待 PI 裁定]` — disk `corpus/v20/strip_captions_22.json` shows 22; see Revision Notes], 5 KT anchors), the V1 FTFB arXiv-anonymous 12-page structure, and the V2 nine-backbone × 60-cell grid. It adds three new tracks that re-use the existing embedding probes (Poincaré-distance frame on **scaffolding tier**, observer-effect and Bell-inequality frames as **brainstorming-only** seeds) and the V7 (V3 terminal report) re-measure. The one-week pre-screen follows the V3.X template: PASS / FAIL / PARTIAL / GRAY verdicts per track, three recipient checkpoints (D1 / D3 / D5), 〔IM〕-only collaboration cadence (~5–10 min/week per recipient).

**Expected outcome.** A reusable three-track hook-finding engine that any of the five+ recipients can run on their own backbones, with the option to extend to a six-month single-paper study if all three tracks reach PASS or PARTIAL with coherent inter-track evidence.

---

## §1 Introduction

### 1.1 What V1–V3 already gives us

The deposon program has run three full iterations, each producing a frozen, hash-bound asset stack that V4 may re-use without modification:

- **V1 — FTFB, arXiv-anonymous 12-page double-blind.** A finished paper draft suitable for double-blind submission. V4 inherits the section structure (Introduction → Related Work → Method → Experiments → Discussion → Limitations) and the citation style, but does not inherit V1's substantive results, because V4's central object is the *distributional* structure, not the per-cell score.
- **V2 — deposon v2, two non-overlapping frozen layers.** V2 carries **two disjoint frozen layers**, which V4 must read but never mix or merge:
  - *Model-layer (evaluation grid).* `results/boss_pa_1_rbr_rm_result_2026_09_15.json:27-29` records `n_models=9`, `n_540_total=540` — a 9-backbone × 60-cell evaluation grid.
  - *Corpus-layer (blind-test artifacts).* Five frozen artifacts at `corpus/v20/by_model/{kimi, GLM_1, GLM_2, coze, minimax}`. (Note: `coze` is in the 5-artifact corpus layer but is **not** one of the 9 evaluation-grid backbones; the two layers are disjoint, not nested.)
  - Both layers are **read-only** in V4. V4 reads their aggregate distributions and reproduces their per-cell hashes; V4 does not modify, rescore, merge, or re-derive any of them. Track 1's stability rule uses the 5-artifact corpus layer as its denominator; the 9-backbone grid is not a Track 1 input. (See §5.2.)
- **V3 — V7 (V3X one-week go/no-go, four-path terminal verdict).** The terminal version of the V3 report is **V7**: `docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` plus `results/deposon_v3_v7_summary_2026_09_11.json`. The 4-path terminal verdicts per the V7 summary and `results/d7_5anchor_60cells_9model_verdict_2026_09_18.json`: **P-A PASS** (26-cell / 2-model equilibrium-band; key_evidence "2 model 0.867 + V2 60 cells 86.67%"), **P-C DEAD** (R²=0.0007; same root as D7 row `FAIL_H0 (幂律死)` at `d7_5anchor_60cells_9model_verdict_2026_09_18.json:60`), **P-E GRAY** (9 model 距 (1,0,0) [0.17, 0.62]; T-A corr -0.81), **P-F TRIGGERED** (verifiable-audit; D_fix2 sub-items `8+1+0 PARTIAL_PASS` per `d7_5anchor_60cells_9model_verdict_2026_09_18.json:99-100`). P-L v3 remains three-state: size-scaling FAIL, cross-backbone PASS, P-K FPR 4.4% GRAY. V4 inherits the verdict template and the recipient-checkpoint cadence, not the substantive judgments themselves, because V4's tracks ask different questions.

### 1.2 Why a V4 hook-finding pre-screen

V3.X is, by the principal investigator's 2026-09-04 framing, a *hook-finding engine*: a service that scans candidate research directions and returns a one-week go/no-go signal. V1–V3 have, in aggregate, produced a frozen asset stack that has not yet been re-used as the *input* to such an engine. V4's purpose is to take that frozen stack as input and produce, for the first time, a *distillation-aware* pre-screen: one that knows what the cells "look like" when distilled, what they "look like" when the distillation is reversed, and what posture the cells can take against a third-party extractor.

### 1.3 The three tracks

V4 defines three tracks, in this order:

1. **Distillation (forward).** Given the V1–V3 frozen outputs, extract a stable mode set: a small, reproducible subset of "shapes" that re-appear across backbones, across caption fingerprints, and across the 18 frozen anchors. The mode set is *not* a per-cell score; it is a distributional summary.
2. **Reverse-distillation.** Given a distilled output (a student, a mode set, or a downstream model's report), infer the originating distribution: which backbones, which fingerprints, which 18-anchor subset is most consistent with the observed output. This is the inverse direction; we are explicit about its assumptions.
3. **Anti-distillation (new dimension, user-defined).** This is the third track. The principal investigator will define the specific mechanism; the recipient community is invited to contribute the *operational definition*. Anti-distillation in this proposal is a placeholder slot. It is not a fourth post-claim in §3, and it is not a fourth frozen anchor in §6. (See §2.3 and §7.3.)

### 1.4 Who is being invited

V4 invites a deliberately broad set of recipients (see §7). Two design constraints shape the recipient list:

- **Diversity of model families.** KIMI-K3, two Trae tracks, GLM, coze, plus newly invited VS, workbuddy, and 豆包工作 span at least three vendor lineages and three deployment surfaces (closed API, IDE-embedded, workplace-bundled).
- **Diversity of review surface.** Some recipients are best suited to paper-track review (KIMI-K3, GLM, coze), some to IDE-track review (Trae code, Trae IDE), some to workplace-bundle review (workbuddy, 豆包工作), and some to a wider brainstorming role (VS). The five+ recipients are not interchangeable; each is asked for a specific contribution. (See §7.2.)

### 1.5 What V4 explicitly does not do

- V4 does **not** modify any of the 18 frozen anchors, 21 caption fingerprints [count `[待 PI 裁定]` — see Revision Notes], 5 V2 `by_model/` blind-test artifacts, or any frozen V1–V3 file. V4 reads them; V4 does not write them.
- V4 does **not** modify the deposon v0/v01 frozen stack. (No P-G v0/v01 touch.)
- V4 does **not** write to any plugin spec, verifier, Mavis-internal, Trae-IDE cache, or 5 锚 JSON.
- V4 does **not** define the specific anti-distillation mechanism. The third track is a placeholder; the principal investigator supplies the operational definition.
- V4 does **not** adjust any threshold, rescore any cell, or merge any derived JSON into the 5 frozen anchors.
- V4 does **not** send any API key, secret, model endpoint, or proprietary prompt to any external service.

---

## §2 Methods / Experimental Design

### 2.1 Track 1 — Distillation (forward)

**Objective.** From the V1–V3 frozen outputs (V2 nine-backbone × 60-cell grid; V7 18-frozen-anchor re-measure; V1 12-page structure), extract a *stable mode set*: a small, reproducible subset of "shapes" that re-appear across backbones, caption fingerprints, and the 18 frozen anchors.

**Inputs (read-only).**

- `corpus/v20/by_model/{kimi, GLM_1, GLM_2, coze, minimax}` — five frozen V2 cross-vendor blind-test artifacts (corpus layer; disjoint from the 9-backbone evaluation grid, see §1.1).
- 21 caption-fingerprint pairs [count `[待 PI 裁定]`, see Revision Notes] — frozen, double-fingerprinted (see §5.3).
- 18 frozen anchors — frozen, hash-anchored (see §5.4).
- V7 4-path terminal verdict table — P-A / P-C / P-E / P-F outcomes.
- P-L v3 three-state table — size-scaling / cross-backbone / P-K FPR.

**Procedure (high level).**

1. For each frozen artifact, compute a per-cell embedding using the available embedding probes (Poincaré-distance frame on **scaffolding tier**; observer-effect and Bell-inequality frames as brainstorming seeds only — see §2.4 / P0-4). V4 does not introduce a new embedding protocol.
2. Across backbones, identify the mode set as the intersection of high-density regions. A mode is "stable" if it appears in **at least three of the five `by_model/` blind-test artifacts** (corpus layer), in at least three of the 21 caption-fingerprint pairs [count `[待 PI 裁定]`], and in at least three of the 18 frozen anchors.
3. Record the mode set in a new V4-only artifact, *separate* from the V1–V3 frozen stack. V4's mode set is V4's own; it is not merged into the 5 frozen V2 artifacts or the 5 锚 JSON.

**Output.** A V4 mode-set table (delivered to recipients as a separate Markdown / JSON file under a non-frozen path). The mode set is reproducible: given the same frozen inputs, the same protocol yields the same mode set.

**Failure modes.** A mode set that is too small (≤ 2 modes) signals that the frozen assets are too homogeneous to support distillation; V4 reports this as FAIL_DISTILLATION_HOMOGENEOUS. A mode set that is too large (one mode per cell) signals that the frozen assets are too heterogeneous; V4 reports this as FAIL_DISTILLATION_FRAGMENTED.

### 2.2 Track 2 — Reverse-distillation

**Objective.** Given a distilled output (a student model, a mode-set report, or a downstream model's verdict), infer which of the V1–V3 frozen inputs is most consistent with the observed output.

**Inputs.** The V4 mode-set table (Track 1 output) plus the same V1–V3 frozen inputs as Track 1.

**Procedure (high level).**

1. For a candidate distilled output, compute the same per-cell embedding used in Track 1.
2. Compare against the V4 mode set using a divergence metric. The default is symmetric KL on the per-cell embedding distributions, following the V3 Bell-inequality frame (a brainstorming-only seed in V4; see §2.4); alternative divergences are recorded but not promoted to the primary metric without principal-investigator approval.
3. Attribute the distilled output to the frozen input (backbone × caption × anchor) whose mode set is closest under the divergence.

**Output.** A reverse-attribution table that, for each candidate distilled output, names the most consistent frozen input and the divergence value. The table is V4's own; it does not modify any frozen input.

**Failure modes.** A reverse-attribution that is uniform across all frozen inputs signals that the distilled output is not informative; V4 reports FAIL_REVERSE_INFORMATIVE. A reverse-attribution that always picks the same frozen input signals that the mode set has a single dominant mode; V4 reports FAIL_REVERSE_DOMINANT.

### 2.3 Track 3 — Anti-distillation (placeholder, user-defined)

**Status.** This is a placeholder track. The principal investigator will define the specific mechanism. Recipients are invited to contribute the operational definition, the failure modes, and the success criteria.

**Why this track exists.** Distillation and reverse-distillation are both *passive*: they assume the frozen inputs are available for reading. Anti-distillation is the *defensive* counterpart: it asks what posture the frozen inputs can take against a third-party extractor that does not have read access. The deposon program has not yet defined this posture; V4 opens the slot.

**Default scope (subject to principal-investigator revision).** Anti-distillation in V4 is constrained to:

- *operate on* the V1–V3 frozen inputs (read-only);
- *output* a defensive posture table (V4's own, separate from the frozen stack);
- *not modify* any frozen anchor, caption fingerprint, V2 artifact, or 5 锚 JSON;
- *not introduce* a new API key, secret, or proprietary prompt.

**Definition of what successful anti-distillation looks like.** To be specified by the principal investigator. The recipient community is invited to propose the operational definition; proposals are not commitments.

### 2.4 Embedding probes (re-used, with on-disk existence notes)

V4 reuses the embedding frames from V1–V3 in the following **explicitly non-uniform** way; no new embedding protocol is introduced.

- **Poincaré-distance frame — scaffolding tier.** A Poincaré-frame artifact exists at `deposon_team/plugins/_pg_v01_compute.py:424-443` with three `BOSS_PG_*` slots, each `status="SCAFFOLDING (PRE-REGISTRATION, 等 D5 launch)"` and `verdict_pending=true`. Landing confirmed at `results/deposon_pg_v01_9m60c_2026_09_15.json:379-396`; the 5 P-G anchor SHA-12 values are already computed at `:347-377`. **V4 makes no calibrated-curvature claim** — the value `POINCARE_C = 1.0` is the V0 spec placeholder, not a V2/V3 calibrated value. V4 reuses only what is on disk at scaffolding tier; V4 does not recalibrate, and V4 does not assert a specific curvature.
- **Observer-effect frame — brainstorming seed only.** No V1–V3 artifact for this frame exists on disk. Mentioned in invitation / review / verify documents as a brainstorming direction. V4 invokes it as a brainstorming seed and explicitly tags "no on-disk artifact at v0.2".
- **Bell-inequality frame — brainstorming seed only.** No V1–V3 artifact for this frame exists on disk. Same posture as observer-effect. V4 invokes it as a brainstorming seed and explicitly tags "no on-disk artifact at v0.2".

Net: at v0.2 V4 reuses **1 frame on scaffolding tier + 2 frames brainstorming-only**.

### 2.5 Cross-discipline integration (placeholder, brainstorming-only)

The principal investigator invites cross-discipline integration as a brainstorming contribution, not a method commitment. Candidate frames include:

- non-Euclidean geometry (Poincaré-distance frame on scaffolding tier per §2.4; no new geometry introduced);
- observer effect (brainstorming seed only per §2.4; no new observer introduced);
- quantum-domain analogues (Bell-inequality frame as brainstorming seed per §2.4; no new quantum protocol introduced);
- other disciplines (recipients are invited to propose; proposals are not commitments).

V4 does not commit to a cross-discipline structure in this draft. The list above is a *seed* for the recipient brainstorming round, not a method.

### 2.6 Recipient checkpoints and verdict cadence

V4 follows the V3.X one-week template:

- **D1.** Recipient receives the V4 mode-set table (Track 1) and the reverse-attribution procedure (Track 2). Recipient flags any issue that would invalidate Track 1 or Track 2.
- **D3.** Recipient receives the Track 1 + Track 2 preliminary outputs. Recipient runs the reverse-attribution on a held-out candidate and reports divergence.
- **D5.** Recipient receives the Track 3 placeholder, the cross-discipline seed list, and the final V4 verdict template. Recipient returns PASS / FAIL / PARTIAL / GRAY on each of the three tracks.

Each recipient is asked to spend ~5–10 minutes per checkpoint. 〔IM〕-only cadence.

### 2.7 What is frozen vs. what is V4-only

| Class | Frozen (read-only in V4) | V4-only (V4 owns, separate from frozen) |
|---|---|---|
| V2 artifacts (5, corpus layer) | `corpus/v20/by_model/{kimi, GLM_1, GLM_2, coze, minimax}` | — |
| V2 evaluation grid (9 backbone × 60 cell, model layer) | `results/boss_pa_1_rbr_rm_result_2026_09_15.json` (`n_models=9`, `n_540_total=540`) | — |
| Caption fingerprints | 21 frozen pairs [count `[待 PI 裁定]`, see Revision Notes] | — |
| Anchors | 18 frozen anchors | — |
| V7 (V3 terminal) verdict | P-A PASS / P-C DEAD / P-E GRAY / P-F TRIGGERED + P-L v3 three-state | — |
| V1 paper structure | 12-page double-blind scaffold | — |
| Mode set | — | V4 mode-set table |
| Reverse attribution | — | V4 reverse-attribution table |
| Anti-distillation posture | — | V4 defensive-posture table (placeholder) |
| Cross-discipline seed | — | V4 seed list (brainstorming-only) |

---

## §3 Expected Outcomes

### 3.1 Per-track verdict template

Each track returns one of four verdicts, following the V3.X template:

- **PASS.** The track reproduces on the frozen inputs and yields a stable, attributable output.
- **FAIL.** The track does not reproduce, or yields an uninformative output.
- **PARTIAL.** The track reproduces on a subset; the subset is named.
- **GRAY.** The track reproduces but the verdict is ambiguous; the ambiguity is named.

### 3.2 Cross-track verdict

V4's overall verdict is the conjunction of the three track verdicts:

- **V4 = PASS** iff all three tracks are PASS or PARTIAL with coherent inter-track evidence.
- **V4 = FAIL** iff any track is FAIL and the FAIL cannot be reconciled with the others.
- **V4 = GRAY** otherwise.

The conjunction rule is the same as V3.X; V4 does not introduce a new rule.

### 3.3 Decision rule for downstream commitment

If V4 reaches PASS or GRAY-with-actionable-evidence, the principal investigator may, at their sole discretion, propose a six-month single-paper study. V4 is not a commitment to a six-month study; V4 is a one-week pre-screen. The six-month study is a *possible* downstream phase, not a V4 deliverable.

### 3.4 What V4 does not promise

- V4 does not promise a paper. V4 promises a one-week pre-screen.
- V4 does not promise a six-month study. V4 promises a verdict that *may* trigger a six-month study, at the principal investigator's discretion.
- V4 does not promise any specific anti-distillation outcome. Track 3 is a placeholder.
- V4 does not promise any specific cross-discipline structure. The seed list is brainstorming-only.

---

## §4 Discussion

### 4.1 What is new in V4, and what is reused

**New.**

- The three-track structure (distillation / reverse-distillation / anti-distillation).
- The reverse-attribution procedure (Track 2 is genuinely new; Track 1 is the distillation analogue of V3's verdict work; Track 3 is the placeholder).
- The cross-discipline seed list (brainstorming-only, no commitment).

**Reused.**

- V1 12-page structure (paper scaffolding, not substantive results).
- V2 two-layer frozen stack: 9-backbone × 60-cell model-layer grid + 5 `by_model/` corpus-layer blind-test artifacts (read-only inputs; the two layers are disjoint and not merged, see §1.1).
- V7 (V3 terminal) 18-frozen-anchor re-measure (read-only inputs).
- V3.X verdict template (PASS / FAIL / PARTIAL / GRAY).
- V3.X recipient-checkpoint cadence (D1 / D3 / D5, ~5–10 min/week per recipient, 〔IM〕-only).
- Embedding frames: Poincaré-distance on **scaffolding tier** only; observer-effect and Bell-inequality as **brainstorming seeds only** (§2.4). No calibrated-curvature claim.

### 4.2 What is intentionally out of scope

- Any modification of frozen inputs (§5).
- Any introduction of a new embedding protocol (§2.4).
- Any introduction of a new verdict rule (§3.2).
- Any operational definition of anti-distillation (§2.3).
- Any commitment to a cross-discipline structure (§2.5).
- Any six-month single-paper deliverable (§3.3).

### 4.3 Risks and limits

- **Frozen-asset homogeneity.** If the V1–V3 frozen inputs are too homogeneous, Track 1 fails with FAIL_DISTILLATION_HOMOGENEOUS.
- **Frozen-asset heterogeneity.** If the frozen inputs are too heterogeneous, Track 1 fails with FAIL_DISTILLATION_FRAGMENTED.
- **Distillation asymmetry.** Reverse-distillation (Track 2) may not be the unique inverse of distillation (Track 1); V4 acknowledges this and names the divergence metric explicitly.
- **Anti-distillation under-specification.** Track 3 is a placeholder; until the principal investigator defines the mechanism, Track 3 has no failure mode beyond "undefined".
- **Cross-discipline over-commitment.** The seed list in §2.5 is brainstorming-only; recipients are asked not to treat it as a method commitment.
- **Embedding-frame honesty.** V4 invokes 3 embedding frames but only 1 (Poincaré) has any on-disk artifact, and that one is **scaffolding tier** (`verdict_pending=true`); V4 must not over-claim reuse of the other two (§2.4).

### 4.4 Recipient diversity and brainstorming role

The five+ recipients are not interchangeable. §7 names the specific contribution asked of each. The recipient list is intentionally broad: the principal investigator values cross-vendor and cross-deployment-surface diversity, and explicitly invites brainstorming contributions from VS, workbuddy, and 豆包工作 alongside the paper-track and IDE-track contributions from the others.

---

## §5 Available Assets (V1–V3, frozen, read-only)

### 5.1 V1 — FTFB, arXiv-anonymous 12-page double-blind

- **Form.** A finished paper draft, 12 pages, double-blind style.
- **Reuse in V4.** Section structure (Introduction → Related Work → Method → Experiments → Discussion → Limitations) and citation style. V4 does not reuse V1's substantive results.

### 5.2 V2 — deposon v2, two non-overlapping frozen layers (frozen)

- **Model-layer (evaluation grid).** `results/boss_pa_1_rbr_rm_result_2026_09_15.json:27-29` records `n_models=9`, `n_540_total=540` — a 9-backbone × 60-cell evaluation grid. Read-only.
- **Corpus-layer (blind-test artifacts).** **Five frozen artifacts** at `corpus/v20/by_model/{kimi, GLM_1, GLM_2, coze, minimax}`. Note: `coze` is in this 5-artifact corpus layer but is **not** one of the 9 evaluation-grid backbones. The two layers are disjoint. Read-only.
- **Reuse in V4.** Aggregate distributions and per-cell hashes, from each layer within its own scope. V4 does not modify, rescore, or merge any of them; V4 does not collapse the two layers into a single set.

### 5.3 V7 (V3 terminal) — V3X one-week go/no-go, 4-path terminal verdict (frozen)

- **Verdict table** (per `results/deposon_v3_v7_summary_2026_09_11.json` + `results/d7_5anchor_60cells_9model_verdict_2026_09_18.json`):
  - **P-A: PASS** — 26-cell / 2-model equilibrium-band; key_evidence "2 model 0.867 + V2 60 cells 86.67%".
  - **P-C: DEAD** — R² = 0.0007. Same root as D7 row `FAIL_H0 (幂律死)` (`d7_5anchor_60cells_9model_verdict_2026_09_18.json:60`); the semantic tag is identical.
  - **P-E: GRAY** — 9 model 距 (1, 0, 0) [0.17, 0.62]; T-A corr -0.81.
  - **P-F: TRIGGERED** — verifiable-audit; D_fix2 sub-items score `8 + 1 + 0 PARTIAL_PASS` (`d7_5anchor_60cells_9model_verdict_2026_09_18.json:99-100`).
- **P-L v3 three-state.**
  - Size-scaling FAIL.
  - Cross-backbone PASS.
  - P-K FPR 4.4% GRAY.
- **Reuse in V4.** Verdict template (PASS / FAIL / PARTIAL / GRAY) and recipient-checkpoint cadence (D1 / D3 / D5). V4 does not reuse the substantive judgments themselves.

### 5.4 V7 (V3 terminal report) SHA pointer (frozen)

- **Provenance pointer.** The authoritative V3-terminal-report files are `docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` + `results/deposon_v3_v7_summary_2026_09_11.json`. V4 does not recalculate any SHA; V4 only cites these paths.
- **Reuse in V4.** Provenance pointer only.

### 5.5 Caption fingerprints (21 frozen — count `[待 PI 裁定]`)

- **21 caption-fingerprint pairs**, double-fingerprinted. **Note:** the on-disk file `corpus/v20/strip_captions_22.json` contains 22 captions. v0.2 retains the v0.1 figure of 21 because no principal-investigator ruling exists yet; see Revision Notes §"Open Items".
- **Reuse in V4.** Mode-set identification (Track 1) and reverse-attribution (Track 2). V4 reads the fingerprints; V4 does not modify them.

### 5.6 Anchors (18 frozen, plus 5 KT anchors)

- **18 frozen anchors**, hash-anchored.
- **5 KT anchors (see §6).**
- **Reuse in V4.** Mode-set identification (Track 1) and reverse-attribution (Track 2). V4 reads the anchors; V4 does not modify them.

### 5.7 Plugin spec, verifier, Mavis-internal, Trae-IDE cache, and 5 锚 JSON (frozen, out of V4 scope)

V4 does not read, write, or modify any of the following:

- 4 plugin specs.
- verifier/ subtree.
- Mavis-internal files (outside the deposon-repo workspace).
- Trae-IDE cache (`〔本机用户目录〕\.trae-cn\...`).
- 5 锚 JSON manifest.

These are listed for completeness only; V4 has no operation against them.

---

## §6 Five KT Anchors (frozen, read-only)

The five KT anchors are the canonical hash-bound references for V1–V3. V4 cites them; V4 does not modify them.

| Anchor ID | SHA-12 (placeholder; verify from V7 manifest) | Scope |
|---|---|---|
| KT_A1 | `78b71d404366` | P-A 60 cells 85.0% |
| KT_C1 | `59d8f56347d5` | P-C R²=0.1986 / 0.2670 |
| KT_D0 | `cce8e9a1b00e` | P-D main anchor |
| KT_B1 | `0410ca0fbdae` | P-B 1-week go/no-go |
| KT_ABC1_anchors | `03c6c01f3697` | 5-anchor composite |

> **Note.** The SHA-12 values above are reproduced from the deposon working manifest. The principal investigator is asked to verify each SHA-12 against the V3-terminal-report V7 manifest before V4 circulation. V4 does not recalculate.

---

## §7 Recipients and Collaboration Mode

### 7.1 Collaboration mode (universal)

- **Cadence.** 〔IM〕-only. ~5–10 minutes per recipient per checkpoint. Three checkpoints: D1, D3, D5.
- **Boundary.** Mavis (the agent team) does not push, fetch, or auto-message. All V4 communication is initiated by the principal investigator or by the recipient.
- **Authorship.** AI is not an author. The principal investigator is the sole accountable author. Recipients are acknowledged for their contributions, not listed as authors.
- **Confidentiality.** This invitation is open. No unpublished manuscripts, peer-review material, sensitive data, PHI, proprietary content, or source documents are transmitted.
- **Disclosure.** V4 uses AI-assisted drafting (Mavis `doc-writer`, with `scientific-research-workflows:scientific-writing` and `academic-paper-assistant:academic-paper-polish` skills, both from Mavis plugin-cache). The principal investigator retains final approval and is the sole accountable author. Disclosure follows ICMJE's January 2026 Recommendations.

### 7.2 Recipient list and asked contribution

| Recipient | Track | Asked contribution |
|---|---|---|
| **KIMI-K3 (凝子-agent)** | Track 1 + Track 2 | Paper-track review of the mode-set table and the reverse-attribution procedure. KIMI-K3 is the long-running paper-track reviewer across V1–V3. |
| **Trae code** | Track 1 + Track 2 | IDE-track review of the mode-set table and the reverse-attribution procedure, with attention to reproducibility in the IDE environment. |
| **Trae IDE** | Track 1 + Track 2 + Track 3 | IDE-track review, with a specific ask on Track 3 (anti-distillation) given Trae IDE's exposure to third-party extractor surfaces. |
| **GLM** | Track 1 + Track 2 | Paper-track review following the KIMI-K3 → GLM 委托信 thread. GLM is asked for a cross-vendor check on the mode-set table. |
| **coze** | Track 1 + Track 2 | Paper-track review of the 〔IM〕-deliverable form of the mode-set table. coze is asked for surface-format feedback only. |
| **VS** (newly invited) | Track 3 + cross-discipline seed | Brainstorming-only contribution. VS is asked for a wider cross-discipline seed list, not a method commitment. |
| **workbuddy** (newly invited) | Track 3 + cross-discipline seed | Workplace-bundle review. workbuddy is asked whether the V4 mode-set table is consumable inside a workplace-bundle deployment. |
| **豆包工作** (newly invited) | Track 3 + cross-discipline seed | Workplace-bundle review (different vendor lineage from workbuddy). 豆包工作 is asked the same consumability question. |

### 7.3 What is *not* asked of recipients

- Recipients are **not** asked to define the anti-distillation mechanism. The principal investigator will define it; recipients are asked only to comment on the placeholder (§2.3).
- Recipients are **not** asked to modify any frozen asset. Recipients may read the frozen assets (under the principal investigator's existing sharing rules); recipients may not modify them.
- Recipients are **not** asked to run new experiments on the deposon frozen stack. V4 is a pre-screen; running new experiments is a downstream phase, not a V4 deliverable.
- Recipients are **not** asked to commit to authorship. Authorship is reserved for the principal investigator; recipients are acknowledged.

### 7.4 Recipient-specific output format

- **Paper-track recipients (KIMI-K3, GLM, coze).** Markdown response, ~200–500 words per checkpoint, attached to the existing deposon 〔IM〕 thread or paper-track channel.
- **IDE-track recipients (Trae code, Trae IDE).** Inline IDE comment or short Markdown, attached to the existing deposon IDE-track channel.
- **Brainstorming recipients (VS).** Free-form Markdown, no length constraint, attached to the brainstorming channel.
- **Workplace-bundle recipients (workbuddy, 豆包工作).** Short Markdown or chat-message, attached to the workplace-bundle channel.

---

## §8 Authorship, AI Disclosure, and Approval

### 8.1 Authorship

- **Sole accountable author.** The human principal investigator.
- **AI contribution.** Drafting assistance by Mavis `doc-writer`, using `scientific-research-workflows:scientific-writing` (sha256 `611965fcb...`) and `academic-paper-assistant:academic-paper-polish` (sha256 `01afed67...`), both loaded from Mavis plugin-cache. AI is not an author.
- **Recipient contributions.** Acknowledged, not authorship. CRediT roles to be assigned at the principal investigator's discretion.

### 8.2 AI disclosure (per ICMJE January 2026)

> This invitation letter and the underlying V4 design proposal were drafted with AI-assisted drafting support (Mavis `doc-writer`, with `scientific-research-workflows:scientific-writing` and `academic-paper-assistant:academic-paper-polish` skills, both from Mavis plugin-cache, sha256 `611965fcb...` and `01afed67...` respectively). The human principal investigator reviewed and retains final approval of all content. AI is not an author and does not meet ICMJE authorship criteria. All factual claims, frozen-asset references, SHA-12 placeholders, and recipient-specific asks are subject to verification by the principal investigator against the V1–V3 frozen manifests before circulation.

### 8.3 Approval boundary

Only the principal investigator may:

- modify this invitation letter;
- verify the SHA-12 placeholders against the V7 (V3-terminal) manifest;
- define the anti-distillation mechanism (§2.3);
- approve recipient-list additions or removals;
- set V4 to "circulation-ready";
- initiate the D1 / D3 / D5 checkpoints;
- promote V4 to a six-month single-paper study.

Mavis `doc-writer` and other Mavis agents may not perform any of the above.

---

## §9 Unresolved Issues (intentionally listed, not paper prose)

The following items are unresolved at draft time and are listed for the principal investigator's attention:

1. **Anti-distillation mechanism (§2.3).** Placeholder; awaiting principal-investigator definition.
2. **Cross-discipline seed list (§2.5).** Brainstorming-only; awaiting recipient proposals.
3. **SHA-12 verification (§6).** Placeholders reproduced from working manifest; awaiting verification against V3-terminal-report V7 manifest.
4. **V3-terminal-report provenance (§5.4).** Pointer is locked to V7 (`docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` + `results/deposon_v3_v7_summary_2026_09_11.json`); awaiting principal-investigator confirmation.
5. **Recipient contact channel (§7).** 〔IM〕-only cadence confirmed in principle; specific channel IDs to be supplied by the principal investigator.
6. **Authorship of any downstream six-month study (§3.3).** Reserved to the principal investigator; not committed in V4.

---

## §10 Reporting-Guideline Coverage (non-scoring, recorded for transparency)

| Guideline topic | Status |
|---|---|
| Background and motivation | addressed (§1) |
| Limitations of existing work | addressed (§1.1, §1.2) |
| Proposed solution | addressed (§1.3, §2) |
| Methods as performed | addressed (§2.1–§2.4) |
| Recipient-checkpoint cadence | addressed (§2.6) |
| Frozen vs. V4-only distinction | addressed (§2.7, §5) |
| Expected outcomes | addressed (§3) |
| Decision rule for downstream | addressed (§3.3) |
| Risks and limits | addressed (§4.3) |
| Authorship and disclosure | addressed (§8) |
| Unresolved issues | addressed (§9) |
| Confidentiality classification | addressed (front matter, §7.1) |

This coverage list is non-scoring. It does not certify compliance, completeness, or acceptance. The principal investigator is asked to verify each item against the actual manuscript before circulation.

---

## §11 Bundled Skill Provenance (for transparency)

| Skill | Plugin | Mavis plugin-cache SHA-256 (top-12) | Path |
|---|---|---|---|
| `scientific-writing` | `@scientific-research-workflows` | `611965fcb...` | `〔本机用户目录〕\.minimax\v2\plugin-cache\official\sha256-tree-v1-611965fcb6208a5dbeb28d594ad7ca0f8b1f8fd62fc33c189e56a50e49db19cb\skills\scientific-writing\SKILL.md` |
| `academic-paper-polish` | `@academic-paper-assistant` | `01afed67...` | `〔本机用户目录〕\.minimax\v2\plugin-cache\official\sha256-tree-v1-01afed6776375edeb642ee7bae9effb127332c571572768c2d329b56c6c87e53\skills\academic-paper-polish\SKILL.md` |

Trae IDE cache (`〔本机用户目录〕\.trae-cn\...`) is *not* referenced. Mavis plugin-cache is the authoritative source.

---

## §12 Draft Banner

> **Draft, version 0.2, 2026-09-20.** Not circulation-ready. The principal investigator is asked to verify §5.4 (V7 / V3-terminal SHA pointer), §6 (5 KT SHA-12 placeholders), §7.5 (recipient channel IDs), §2.3 (anti-distillation mechanism), and the Open-Items list at end of file (caption-fingerprint count, scaffold-tier Poincaré verdict) before this letter is sent to any recipient. Mavis `doc-writer` is not authorized to remove this banner.

---

## §13 Revision Notes / Open Items (v0.2-only, not paper prose)

The following items are recorded for the principal investigator's attention as part of the v0.1 → v0.2 patch. They are intentionally not corrected inside the body without PI ruling.

| ID | Item | Status | Action owner |
|---|---|---|---|
| OPN-1 | **Caption-fingerprint count.** v0.1 / v0.2 body uses `21 caption-fingerprint pairs`; disk `corpus/v20/strip_captions_22.json` contains **22** captions. v0.1 → v0.2 does **not** rename this count. | `[待 PI 裁定]` | Principal investigator |
| OPN-2 | **Poincaré-distance calibrated value.** v0.1 said `the curvature is the V2 / V3 calibrated value`. v0.2 makes no calibrated-curvature claim; `POINCARE_C = 1.0` is the V0 spec placeholder. The Poincaré-frame artifact is **scaffolding tier** (`verdict_pending=true`); whether the curvature becomes a calibrated value depends on the D5 launch outcome. | `[待 PI 确认]` (Poincaré scaffold promotion to verdict) | Principal investigator |
| OPN-3 | **Observer-effect / Bell-inequality frames.** Tagged as brainstorming-only in v0.2. Whether either ever becomes a disk artifact is open. | `[待 PI 确认]` | Principal investigator |
| OPN-4 | **D7 verdict mapping.** v0.2 records P-C as `DEAD` with the same root as D7 row `FAIL_H0 (幂律死)`. The exact line-by-line mapping of P-C = DEAD ↔ D7 FAIL_H0 (幂律死) is recorded in the body; whether an additional D7 row joins this set is open. | `[待 PI 确认]` | Principal investigator |
| OPN-5 | **P-F TRIGGERED / D_fix2 8+1+0.** v0.2 records P-F as TRIGGERED and D_fix2 sub-items as `8+1+0 PARTIAL_PASS`. Whether the composite V4 verdict for P-F inherits the `8+1+0 PARTIAL_PASS` directly, or whether the principal investigator prefers a single tag, is open. | `[待 PI 确认]` | Principal investigator |
| OPN-6 | **5 KT SHA-12 values (§6).** Reproduced from the deposon working manifest; verification against the V7 manifest is requested in §6 / §9 / §12 but not yet done by `doc-writer`. | `[待 PI 验证]` | Principal investigator |
| OPN-7 | **Recipient channel IDs (§7.5 referenced from §12).** Not yet supplied by the principal investigator; v0.2 only confirms 〔IM〕-only cadence in principle. | `[待 PI 补充]` | Principal investigator |

---

*End of V4 Experiment Design Invitation, draft v0.2.*


<!-- appended-note:2026-09-30 skill 引用面复核（PI 派工第④项 · 0 删改历史字面） -->

> **附注（2026-09-30 追加 · 非原件内容）**
> 本件原引用字面**逐字保留、0 删改**；本附注**只增不改**。
>
> - **原引用面**：L344,380,385,439,441,442,444（出现 9 处）· Disclosure 段：scientific-research-workflows:scientific-writing + academic-paper-assistant
> - **2026-09-30 只读复核**：原引用字面**2026-09-30 仍成立**（写死路径逐字在位、树哈希同目录名、关键 `SKILL.md` SHA-12 对得上）⇒ **无过期值可改**，故仅追加注记、**不就地更新**
> - **当前三段式锚**（plugin:skill + 树哈希前 12 + SKILL.md SHA-12 + 定位方式）：scientific-research-workflows:scientific-writing · 树 `611965fcb620` · `SKILL.md` SHA-12 `31f4fb3c0df5` / 13,047 B（实体直读）
> - **对外件口径**：本件为**已对外发出件**。路径与树哈希写死之陈旧风险（起因件建议 A1）**仍成立**——建议后续对外件改记 plugin:skill 名，路径与哈希只在内部登记件记实测值。本附注**仅供内部对账，未随原件对外发出**。
> - **执行件**：`results/_skill_reference_update_and_user_surface_survey_2026_09_30.md` · 出件 **worker**（本棒）· **0 删改本件任何既有字节**