# Invitation: A Theme-First Inquiry into LLM Distillation, Reverse-Distillation, and Anti-Distillation — Built on the deposon V1–V3 Asset Stack

**Document type:** Theme-driven invitation (theme only; no framework, no track structure, no checkpoints, no scheduling, no recipient assignments)
**Version:** v1.0 — first V4 "重制" (rebuild) edition
**Date:** 2026-09-20
**Drafted by:** `doc-writer` (Mavis 8-agent team, deposon workspace). Human principal investigator retains final approval and is the sole accountable author. AI is not an author.
**Confidentiality classification:** Open invitation. No unpublished manuscripts, peer-review material, sensitive or restricted data, PHI, proprietary content, or source documents are transmitted in this file. Recipients receive only the invitation and the prompt pack.
**Boundary:** read-only against V1–V3 assets. No frozen artifact modified. No API key, secret, model endpoint, or proprietary prompt appears in this file.

---

## §0 Title and Abstract

### 0.1 Title

> **Inviting a Theme-First Inquiry into LLM Distillation, Reverse-Distillation, and Anti-Distillation on the deposon V1–V3 Asset Stack**

### 0.2 Abstract

The deposon program has, over V1 (FTFB, arXiv-anonymous 12-page double-blind), V2 (deposon v2, a 9-backbone × 60-cell evaluation grid plus five frozen cross-vendor blind-test artifacts), and V3 (the V7 four-path terminal report covering P-A / P-C / P-E / P-F, plus P-L v3 three-state), accumulated a frozen, hash-anchored asset stack. None of the three V-tiers has examined whether the **distributional structure** of the cells, the **extracted mode set** of the responses, or the **defensive posture** against third-party extraction can be made operational as a reusable hook-finding service.

This V4 "重制" edition is **theme-driven and framework-free**. The theme is the three-way knot of *large-model distillation* (what is being transferred from a teacher to a student), *reverse-distillation* (how a third party can detect, attribute, or undo the transfer), and *anti-distillation / distillation-defense* (the teacher's own posture against unwanted extraction). It is **not** a partitioned experiment, **not** a sequenced plan, **not** a recipient-assignment matrix, and **not** a scheduled-experiment layout. The principal investigator has explicitly chosen to set aside all such frameworks for this rebuild; what is preserved is the theme, the seed field, the asset inventory, and an open invitation to the seven existing recipient communities (KIMI-K3, two Trae tracks, GLM, coze, VS, workbuddy, 豆包工作) plus any new collaborator who finds the question worth their time.

The motivation for a **theme-first, framework-free** rebuild is empirical, not stylistic. The deposon V0.2 invitation (`results/_v4_experiment_invitation_2026_09_20_v0.2.md`) already shipped a three-lane structure with a three-meeting-point sequence and per-recipient lane assignments; it received nine independent reviews between 2026-09-20 morning and afternoon, of which at least four surfaced *invalidate-level* blockers (B-series from Trae code; R-series from KIMI-K3; F-series from the Trae code factual-claims supplement; and Claude Code's first-two-lane *GRAY* finding from an independent SHA-12 re-derivation). The framework had become the object of debate, not the theme. This rebuild returns the theme to center.

The single most important on-disk fact this invitation asks every reader to internalise: **V1–V3 has zero distillation, reverse-distillation, or anti-distillation experiments on disk.** What V1–V3 has is a frozen, hash-bound evaluation stack on *which* any distillation-themed inquiry can be staged. Whether the theme becomes a service, a paper, a benchmark, or remains an open question is for the principal investigator and the recipient community to settle later — **not** in this document.

---

## §1 Why this theme, now

Three reasons converge to make *LLM distillation / reverse-distillation / anti-distillation* the theme that should sit on top of the deposon V1–V3 stack, with **no surrounding framework** attached.

**Reason 1 — The theme is structurally adjacent to what V1–V3 already measures, but no V-tier has measured it directly.** V2's 9-backbone × 60-cell grid, the V7 four-path terminal verdicts (P-A / P-C / P-E / P-F), and the five frozen cross-vendor blind-test artifacts are *outputs*. Distillation, by construction, is the question of what can be inferred or extracted from outputs (forward distillation), what can be inferred back from a student (reverse-distillation), and what a teacher can do to make that inference harder (anti-distillation). The theme sits one layer above V1–V3; it asks "what is *in* these outputs, *about* these outputs, and *against* the use of these outputs by a third party?" It is therefore a hook, not a duplication.

**Reason 2 — The reverse and defense directions are real-world questions that have no off-the-shelf answer.** Forward distillation is a well-studied topic in the public literature (logit-based, hidden-state-based, attention-based, sequence-level). Reverse-distillation, treated as a third-party attribution problem on a closed API, is *not* — it is the structural inverse of distillation and inherits none of its mathematical tractability. Anti-distillation / distillation-defense is even more open: output watermarking, training-data poisoning, capability slicing, and information-bottleneck restraint each have small literatures, but the comparative cost-effectiveness across them, the game-theoretic interaction between distiller and defender, and the long-horizon drift problem are all open. A theme-only invitation allows these open sub-questions to surface without forcing a prematurely chosen sub-direction.

**Reason 3 — The V0.2 framework absorbed the reviewer attention and prevented the theme from being discussed.** Nine reviewers between 2026-09-20 morning and afternoon focused on path correction (B1, F1), estimator specification (B3, R2), metric definition (B6, R5), assignment scope (B7, S4 from coze, Claude Code's Track-1 9-vs-5 finding), and reproduction gates (B8, R7, R8). Almost none of this reviewer energy went to *what the theme is for, what counts as an answer, or what evidence would falsify a claim about distillation detection.* A theme-first rebuild invites that missing discussion back in.

What the theme is **not**: it is not a request to produce a model, a benchmark, a leaderboard, a service tier, a paper draft, a co-author list, or a roadmap. It is a request to think alongside the principal investigator about one question, in whatever form the recipient finds honest.

---

## §2 What V1–V3 already gives us

The deposon program has run three full iterations, each producing a frozen, hash-bound asset stack. V4 is **read-only** against this stack — no asset is modified, merged, re-evaluated, or re-anchored. What follows is an inventory of *what is on disk and what role it can play in a distillation-themed inquiry*, not a use commitment.

The inventory is grouped by what each artifact can plausibly *contribute to the theme*. Where the inventory lists a contribution that exceeds what the artifact was originally built for, that is flagged as a **re-fit hypothesis** and is **not** a calibrated finding.

### 2.1 Cross-vendor output-distribution baseline (5 frozen artifacts, V2 corpus layer)

Five frozen artifacts live under `corpus/v20/by_model/`, one per vendor, with non-uniform filenames (a fact the reviewers flagged as B2). Each is a frozen, hash-bound cross-vendor blind-test record.

| Path | Bytes | SHA-256 (first 12) | What it can plausibly contribute to the distillation theme |
|---|---|---|---|
| `corpus/v20/by_model/kimi/index_v2_2026_09_16.json` | 24,150 | `EFE05AD775DE` | A KIMI-vendor output-distribution sample; usable as one teacher's per-cell output for a forward-distillation hypothesis (S-03, S-07, S-15). |
| `corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json` | 19,685 | `268AB1239A8A` | A GLM blind-test record; the filename indicates a **three-way slot test** rather than an `artifact_v_*.json` form — flagging this for the PI (`[待 PI 裁定]`); usable as a second teacher's per-cell output but with a *different shape than the other four* (B5). |
| `corpus/v20/by_model/GLM_2/glm_artifact_v_2026_09_16.json` | 13,150 | `39732A92B5C9` | A second GLM-family artifact; same lineage as `GLM_1` so not an independent teacher for stability-counting purposes (R1 from the n/a-mirror concern). |
| `corpus/v20/by_model/coze/coze_artifact_v_2026_09_16.json` | 10,978 | `FEE04170AA73` | A coze-vendor output-distribution sample; coze is **not** in the 9-backbone evaluation grid (it's a corpus-layer artifact only). |
| `corpus/v20/by_model/minimax/artifact_v_2026_09_16.json` | 25,347 | `9E1CCBDCEACC` | A fifth vendor's output-distribution sample (vendor is a placeholder; the literal on-disk name is `minimax`, not `M3`). |

**What this layer can give the theme (re-fit hypothesis, not calibrated):** a fixed, hash-bound, multi-vendor output-distribution baseline against which *any* of the following could in principle be studied — output-distribution fingerprinting (S-07), behavioral signature extraction (S-03), statistical-anomaly baseline (S-15), cross-model provenance inference (S-17). **What this layer cannot give the theme:** ground-truth labels for "this output was distilled from teacher X" — these artifacts were built for blind-test discrimination, not distillation labelling (the bottom-of-table mapping in the seed field calls this out explicitly).

### 2.2 9-backbone × 60-cell evaluation grid (V2 model layer)

`results/boss_pa_1_rbr_rm_result_2026_09_15.json` (8,674 bytes, SHA-12 `C7C59E0D2F6C`) encodes the 9-backbone × 60-cell evaluation, recording `n_models = 9` and `n_540_total = 540`. The grid is the **model-layer** evaluation frozen at V2.

**Re-fit hypothesis (not calibrated):** the per-cell measurements across 9 backbones × 60 cells could in principle be treated as a 540-point "behavior signal" surface, on which a distillation-of-behavior study (S-03) might be staged. **The 9-backbone grid and the 5-artifact corpus layer are disjoint** (Claude Code's §2 finding confirmed this from independent SHA-12 re-derivation). Which of the 9 backbones map to which of the 5 `by_model/` artifacts is **not** declared on disk (`[待 PI 裁定]`).

### 2.3 V7 four-path terminal verdict table (P-A / P-C / P-E / P-F)

`results/deposon_v3_v7_summary_2026_09_11.json` (25,049 bytes, SHA-12 `063AC8D00542`) and `results/d7_5anchor_60cells_9model_verdict_2026_09_18.json` (2,456 bytes, SHA-12 `4505CCA79C15`) carry the V3 terminal report. The 4-path terminal verdicts as recorded on disk (per the Trae code supplement's §2.1 machine-verified re-read):

- **P-A PASS** — `26-cell / 2-model equilibrium-band; key_evidence "2 model 0.867 + V2 60 cells 86.67%"`. The `51/60 = 85.0%` number is `v2_phase1_60cells` (a V2 phase-1 single-backbone doubao-seed-2.0-lite dpath metric, not a P-A value). This was misattributed in V0.1.
- **P-C DEAD** — `R² = 0.0007`, same root as D7 row `FAIL_H0 (幂律死)`.
- **P-E GRAY** — `9 model 距 (1,0,0) ∈ [0.17, 0.62]; T-A corr −0.81`.
- **P-F TRIGGERED** — `verifiable-audit; D_fix2 sub-items 8+1+0 PARTIAL_PASS`.

**Re-fit hypothesis (not calibrated):** the four-path verdict table is, structurally, a teacher-against-anchor dataset — the same shape a distillation-detection benchmark would need (S-04, S-37). Whether the table's anchor cells can be re-used for distillation detection is **not** established. P-L v3 (size-scaling FAIL / cross-backbone PASS / P-K FPR 4.4% GRAY) is similarly structured but not yet assessed against the theme.

### 2.4 60-cell STRONG_PASS rate (V2 single-backbone; see `deposon_v2_phase1_60cells_2026_09_11.json`)

`results/deposon_v2_phase1_60cells_2026_09_11.json` (85,508 bytes, SHA-12 `A18BBC703B42`) records `v2_60cells_pass_rate = 51/60 = 85.0% STRONG_PASS`. The remaining phase-2 / phase-4 files (`results/deposon_v2_phase2_dual_mainline_2026_09_11.json`, 3,189 bytes, SHA-12 `E337B824C4B9`; `results/deposon_v2_phase4_f4_2026_09_11.json`, 5,212 bytes, SHA-12 `CF7682348617`) carry additional dual-mainline and F4 sub-verdicts.

**Re-fit hypothesis (not calibrated):** a 60-cell STRONG_PASS rate is, structurally, the kind of single-backbone robustness surface on which a robustness-curve-after-distillation study (S-10) could be staged. Whether the rate is preserved, attenuated, or amplified under a forward-distillation hypothesis is **not** established on disk.

### 2.5 Disturbance-experiment record (V3 V7 final report)

`docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` (38,545 bytes, SHA-12 `4A08521F8DE1`) is the V7 final report. It records disturbance experiments as part of the discrimination task. **The disturbance targets are discrimination, not distillation** — re-using them as distillation probes is a re-fit hypothesis (S-10), not a calibrated finding.

### 2.6 Anchor set, caption set, frozen schema

- `verifier/handoff/KT_ABC1_anchors_sha256_12.json` (6,680 bytes, SHA-12 `03C6C01F3697`) — 5 KT-ABC1 anchors; usable as a hard-case reservoir (S-11).
- `verifier/handoff/P_F_PREDECISION_2026_09_11_V0.1.json` (12,498 bytes, SHA-12 `312D635E6259`) — pre-decision record for P-F; not a distilled-output sample.
- `corpus/v20/index_v2_2026_09_16.json` (24,150 bytes, SHA-12 `EFE05AD775DE`) — the v2 index; **note that this hash matches the kimi artifact's hash** above, which the reviewers flagged as a co-location of files with identical SHA-12 prefixes; the PI must decide whether the index is intentionally co-located with the kimi artifact or whether this is a path-management issue (`[待 PI 裁定]`).
- `corpus/v20/strip_captions_22.json` (12,798 bytes, SHA-12 `6A2656878745`) — **22** caption entries, not 21. The V0.1 invitation's "21 caption-fingerprint pairs" figure was inaccurate (Trae code's B4 and the supplement's confirmation); the on-disk count is 22.

### 2.7 Non-Euclidean curvature scaffolding (P-G v01)

- `results/deposon_pg_v01_9m60c_2026_09_15.json` (11,512 bytes, SHA-12 `AB75889EE738`) — P-G v01 landing; carries `verdict_pending = true`.
- `deposon_team/plugins/_pg_v01_compute.py` (20,923 bytes, SHA-12 `D511C545F88E`) — P-G v01 compute scaffold; carries `status = SCAFFOLDING (PRE-REGISTRATION, 等 D5 launch)` per the V0.1 v0.2 patch notes.

**This is the only V1–V3 asset that touches a non-Euclidean / geometric frame.** It is **scaffolding tier, not calibrated**. It can in principle be borrowed as a geometry-tool scaffold (S-07, S-08, S-30) but the scaffolding verdict is *not* a calibrated curvature claim, and **no calibrated curvature finding transfers from P-G v01 to a distillation-themed inquiry** (the V0.2 patch's P0-4 closed this explicitly).

### 2.8 Attack-subdirectory code

- `attacks/a1_delete_anchor.py` (4,693 bytes, SHA-12 `78AC391D16FC`)
- `attacks/a2_reshuffle_manifest.py` (3,792 bytes, SHA-12 `3D54B277620E`)
- `attacks/a3_rewrite_runs.py` (4,254 bytes, SHA-12 `F02B3EEE8D6E`)

These were built for discrimination attacks, not distillation defense (S-20, S-23). Re-using them for distillation-defense is a re-fit hypothesis, not a calibrated finding.

### 2.9 Frozen schema and verifier subtree

- `deposon_team/plugins/_v3x_frozen_schema_v1.json` (12,919 bytes, SHA-12 `9E99DCC4D920`) — frozen schema; **read-only, not modified by V4**.
- `verifier/handoff/…` — verifier subtree; **read-only, not modified by V4**.

### 2.10 What is *not* on disk (must be stated, not concealed)

- **No V1–V3 distillation, reverse-distillation, or anti-distillation experiment asset exists on disk.** V4 is the first deposon V-tier to address the theme at all.
- **No `observer-effect` frame artifact exists on disk.** The S-31 seed (and the related S-39) are pure speculation.
- **No `Bell-inequality` frame artifact exists on disk.** The S-35 seed is pure speculation.
- **No quantum no-cloning frame artifact exists on disk.** The S-32 seed is pure speculation.
- **No logit-level artifact exists on disk.** Deposon does not store per-token logit histories (S-09 is therefore a black-box-only question by default).
- **No training-curve artifact exists on disk.** The S-14 (training-dynamics inversion) seed is therefore a theoretical question, not an empirical one.

The bottom line: V1–V3 gives the theme a fixed, hash-bound evaluation surface (5 vendor outputs, 9 backbones × 60 cells, 4-path terminal verdicts, 22 captions, ~600 edges/anchors). V1–V3 does **not** give the theme any distillation, reverse-distillation, or anti-distillation empirical results of its own.

---

## §3 The brainstorm seed field (40 seeds, 7 dimensions, no framework)

The seed field reproduced below is the **only** prescriptive content this invitation ships. It is the brainstorm seed field authored on 2026-09-20 by a worker (0 LLM, file at `results/_v4_brainstorm_seeds_2026_09_20.md`). The seeds are presented **without ranking, scoring, or selection**. Every seed is one of: (a) a question that the on-disk V1–V3 assets can in principle inform, or (b) a pure-speculation seed with no on-disk anchor.

Every seed carries four elements, as authored:

1. **Problem** — what is the question, in one sentence.
2. **Why interesting** — what makes the question non-trivial.
3. **Related asset** — the V1–V3 artifact (if any) that could in principle be relevant. If "no direct match," it is so stated.
4. **Nature** — `disk fact` if any on-disk artifact directly supports a finding; `pure speculative` if no on-disk artifact exists for this seed.

The seeds are presented in the original 7-dimension grouping. Dimensions are *themes*, not *tracks*: this is a re-statement of the no-framework principle. The dimension labels are the author's organising frame for the brainstorm, not a deposon-side decision structure.

### 3.1 Dimension 1 — Distillation, considered as "what is being transferred"

**S-01 Weight-level transfer.** Problem: how much can the weights themselves be "copied" (parameter copy / LoRA extraction / distillation initialisation)? Why interesting: the reachable upper bound caps the student's capability. Related asset: V1–V3 has no distillation asset. Nature: **pure speculative**.

**S-02 Representation-level transfer.** Problem: how much of the teacher's latent-space geometry (embeddings, manifolds, distances) is preserved in the student? Why interesting: representation preservation is a *geometric* path to capability preservation, distinct from the weight path. Related asset: P-G v01 (`_pg_v01_compute.py` + `deposon_pg_v01_9m60c_2026_09_15.json`) is a non-Euclidean-curvature scaffold, **scaffolding tier, verdict_pending=true**, usable as a geometry scaffold but not as a calibrated finding. Nature: **pure speculative** (scaffold borrowing only).

**S-03 Behaviour-level transfer.** Problem: how completely can the teacher's behaviour fingerprint (wording preferences, hesitation rhythm, under the same input) be migrated? Why interesting: behaviour is the most externally observable layer of a teacher. Related asset: the five frozen artifacts under `corpus/v20/by_model/{kimi, GLM_1, GLM_2, coze, minimax}` are cross-model behaviour samples (V20 use is blind-test discrimination, not distillation). Nature: **pure speculative**.

**S-04 Reasoning-chain transfer.** Problem: can a teacher's CoT / scratchpad / reflection steps be replicated to the point of indistinguishability? Why interesting: reasoning chains are "internal monologue," the hardest to copy and the easiest to leave a trace in. Related asset: `deposon_v3_v7_summary_2026_09_11.json` is a verdict, not a reasoning-chain sample. Nature: **pure speculative**.

**S-05 Calibration and confidence transfer.** Problem: can a teacher's "knowing that it doesn't know" (ECE, refusal thresholds, confidence distributions) be distilled? Why interesting: differential calibration transfer makes a model "confidently wrong." Related asset: `boss_pa_1_rbr_rm_result_2026_09_15.json` (9 backbone × 60 cell = 540) is a discrimination verdict, not a calibration record. Nature: **pure speculative**.

**S-06 Refusal-boundary transfer.** Problem: how finely can a teacher's refusal boundary be replicated by a student? Why interesting: being bypassed is equivalent to the teacher's guardrail failing. Related asset: `deposon_v2_phase1_60cells_2026_09_11.json` (51/60 = 85.0% STRONG_PASS) is a discrimination verdict, not a refusal curve. Nature: **pure speculative**.

### 3.2 Dimension 2 — Observable signals, considered as "how do we know distillation happened"

**S-07 Output-distribution fingerprints.** Problem: from outputs alone (no weights, no logits), how reliably can a "distilled product" be identified? Why interesting: third-party detectors usually only have API text. Related asset: `corpus/v20/by_model/` 5 frozen artifacts can serve as baseline output-distribution references. Nature: **pure speculative**.

**S-08 Embedding-geometry alignment.** Problem: can the geometric alignment of a student's embedding with a teacher's be used as evidence of distillation? Why interesting: geometric alignment is hard to fake via prompt engineering. Related asset: P-G v01 curvature experiment can serve as a curvature-computation scaffold. Nature: **pure speculative** (scaffold borrowing).

**S-09 Logit shifts and temperature response.** Problem: when logits are accessible, can logit shifts and temperature curves differentiate distilled from original models? Why interesting: logits are finer-grained than text; temperature response is non-linear. Related asset: deposon does **not** store logit-level artifacts. Nature: **pure speculative**.

**S-10 Disturbance sensitivity.** Problem: are distilled models' responses to input disturbances (typos, token injection, template switching) "more like" the teacher's? Why interesting: robustness-curve convergence is a *cost* of distillation. Related asset: `docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` disturbance experiments target the discrimination task. Nature: **pure speculative**.

**S-11 Long-tail consistency.** Problem: can long-tail-fact consistency (low-frequency entities, rare collocations, edge-case instructions) serve as a distillation-depth proxy? Why interesting: long-tail is the hardest to cover and the hardest to fake in reverse. Related asset: 18 frozen anchors + 22 caption entries + 5 KT anchors (`KT_ABC1_anchors_sha256_12.json`) form an edge-case library, **used for discrimination stability**, not distillation depth. Nature: **pure speculative** (asset reuse, different purpose).

**S-12 Temporal correlation and pattern drift.** Problem: does a distilled model preserve the teacher's "patterns" at a specific time (old wording, old knowledge-cutoff, old defaults)? Why interesting: temporal fingerprints are signals that "leak unintentionally." Related asset: **no direct match**. Nature: **pure speculative**.

### 3.3 Dimension 3 — Reverse-distillation (the detection side)

**S-13 Steganographic fingerprints.** Problem: can a teacher plant statistically measurable, human-imperceptible fingerprints in its outputs? Why interesting: such fingerprints are an "active line of defence" for detection. Related asset: the 22-caption fingerprint is a discrimination fingerprint, **not** an output-watermark fingerprint. Nature: **pure speculative**.

**S-14 Training-dynamics inversion.** Problem: can a student's training curve (loss jumps, reward drift, capability time-series) be inverted to infer the teacher's source? Why interesting: training dynamics are the hardest to erase "archaeological layer." Related asset: `d7_5anchor_60cells_9model_verdict_2026_09_18.json` is a terminal verdict, not a training-dynamics record. Nature: **pure speculative**.

**S-15 Output statistical anomalies.** Problem: on which statistics is a distilled model "anomalous" — rare n-grams, syntactic diversity, perplexity long-tails? Why interesting: easy to measure, weight-independent, a black-box entry point. Related asset: `corpus/v20/by_model/` provides statistical-baseline samples. Nature: **pure speculative**.

**S-16 Membership inference.** Problem: can a single datum be tested for whether it was used to distill a given student? Why interesting: the strongest but most expensive detection tool. Related asset: **no direct match**. Nature: **pure speculative**.

**S-17 Cross-model provenance.** Problem: given multiple candidate teachers, can the student be attributed to one (or a mix)? Why interesting: detection's "granular" layer — not only "whether," but "from whom." Related asset: the 5-model blind-test artifact structure is the natural prototype for a "known teacher candidate" setup. Nature: **pure speculative**.

**S-18 Statistical signatures of distillation traces.** Problem: are there signatures "almost impossible to produce by independent training" (specific token preferences, residual temperature)? Why interesting: signatures are the hardest evidence but also the easiest to evade. Related asset: **no direct match**. Nature: **pure speculative**.

### 3.4 Dimension 4 — Anti-distillation / distillation-defense (the protection side)

**S-19 Output watermarks.** Problem: can output watermarks raise the cost of distillation without significantly degrading generation quality? Why interesting: an "active weapon," but in tension with generation quality. Related asset: the 22-caption fingerprint and the watermark technology stack are unrelated. Nature: **pure speculative**.

**S-20 Training-data poisoning.** Problem: can planting "trap samples" in public data cause a distiller to unknowingly damage itself? Why interesting: "fight poison with poison," but ethics/legal boundaries are sensitive. Related asset: `attacks/` directory contains attack assets, **for discrimination, not for distillation defense**, requiring independent assessment. Nature: **pure speculative**.

**S-21 Information bottleneck.** Problem: can a teacher actively limit the "information" of its outputs so that any distillation learns less? Why interesting: a "self-weakness" anti-distillation idea, with the cost of real capability loss. Related asset: **no direct match**. Nature: **pure speculative**.

**S-22 Capability isolation / sub-model slicing.** Problem: can a teacher be sliced into multiple "capability sub-slices," called on demand rather than fully exposed? Why interesting: structural defense — relying on "not letting you see the whole" rather than "adding perturbations." Related asset: **no direct match**. Nature: **pure speculative**.

**S-23 Adversarial perturbation.** Problem: can carefully designed adversarial perturbations in a teacher's outputs disrupt distillation convergence? Why interesting: moving the "adversarial-example" idea from discrimination to defense. Related asset: `attacks/` is for discrimination, not distillation defense. Nature: **pure speculative**.

**S-24 Behavioural-signature induction.** Problem: can a teacher "bury" behavioural signatures in normal outputs (occasional fixed-phrase citations) such that a distiller cannot erase them without damaging the overall behaviour? Why interesting: signature induction is "behavioural watermarking," harder to erase than token watermarks. Related asset: **no direct match**. Nature: **pure speculative**.

### 3.5 Dimension 5 — Counter-anti-distillation (when defense is bypassed)

**S-25 Adversarial escalation.** Problem: how does a distiller upgrade in the face of defense — fine-tuning cleanup, adversarial training, cross-teacher mixing? Why interesting: game-theoretic exploration of the "opponent's strategy space." Related asset: **no direct match**. Nature: **pure speculative**.

**S-26 Watermark erasure.** Problem: can watermarks be "losslessly" erased? At what granularity are they truly non-erasable? Why interesting: determines whether watermarks are worth a long-horizon defense line. Related asset: **no direct match**. Nature: **pure speculative**.

**S-27 Defense probing.** Problem: can a distiller probe "is there anti-distillation defense behind this API" before deciding to distill? Why interesting: probing is itself at the front of attack-defense. Related asset: **no direct match**. Nature: **pure speculative**.

**S-28 Distiller-defender game.** Problem: when both sides continuously learn the other's strategy, do they converge to an equilibrium or cycle through escalating rounds? Why interesting: a compound problem of game theory + reinforcement learning. Related asset: **no direct match**. Nature: **pure speculative**.

**S-29 Long-horizon equilibrium.** Problem: on a 5-year scale, does the "cost-benefit" of distillation and anti-distillation move toward one side? Why interesting: determines whether the direction is "the more defense, the cheaper" or "the more defense, the more expensive." Related asset: **no direct match**. Nature: **pure speculative**.

### 3.6 Dimension 6 — Cross-disciplinary seeds (one of several optional layers; not steered toward or away from)

> This section's seeds are **analogies or formal tools**, not directional recommendations. Any seed in this section can be picked up, modified, or dropped.

**S-30 Hyperbolic geometry / curvature differential.** Problem: can the latent-space curvature difference between a teacher and a student serve as a geometric fingerprint of distillation depth? Why interesting: curvature is a non-Euclidean invariant, robust to weight perturbation. Related asset: P-G v01 is a non-Euclidean-curvature scaffold (**scaffolding tier, verdict_pending=true**). Nature: **pure speculative** (scaffold borrowing).

**S-31 Observer effect / measurement-as-perturbation.** Problem: does the act of detecting distillation change the behated model's behaviour? Why interesting: detection is "perturb," not "read" — ground truth is hard to stabilise. Related asset: **no observer-effect frame artifact on disk**. Nature: **pure speculative**.

**S-32 No-cloning-theorem analogy.** Problem: can a formalisation analogous to quantum no-cloning be given for "a teacher cannot be exactly copied"? Why interesting: if it holds, distillation can only "approximate" — that boundary is itself a defense resource. Related asset: **no direct match**. Nature: **pure speculative**.

**S-33 Entanglement / context coupling.** Problem: can a teacher's multi-turn / retrieval / tool-use capability be decoupled and distilled? Why interesting: coupled capabilities are the "hard bone" of distillation. Related asset: **no direct match**. Nature: **pure speculative**.

**S-34 Decoherence / reasoning collapse.** Problem: in long-chain reasoning, does a distilled model "collapse" to local solutions more easily? Why interesting: decoherence is a potential weakness in reasoning robustness. Related asset: V7 verdict is a discrimination verdict; reasoning-chain samples have no direct asset. Nature: **pure speculative**.

**S-35 Bell-inequality analogy.** Problem: is there a "Bell-type" test that can falsify the "independent training" hypothesis under a black box? Why interesting: pushes "was it distilled?" from empirical discrimination to formal discrimination. Related asset: **no Bell-inequality frame artifact on disk**. Nature: **pure speculative**.

### 3.7 Dimension 7 — Evaluation science (the ground-truth problem for distillation detection)

**S-36 The ground-truth dilemma.** Problem: who labels the GT for distillation detection — the teacher themselves, the distiller themselves, a third-party auditor? Why interesting: the three parties have different motivations; GT is not unique. Related asset: V2/V3 STRONG_PASS / DEAD / GRAY / TRIGGERED are deposon's own discrimination GT, *a different problem* from distillation-detection GT. Nature: **pure speculative**.

**S-37 False-positive / false-negative cost structure.** Problem: what is the cost structure of mistaking "independent training" for "distilled" (false positive) versus missing it (false negative)? Why interesting: determines the direction of optimal-threshold tilt. Related asset: D7 verdict + `boss_pa_1_rbr_rm_result_2026_09_15.json` 9-backbone × 60-cell = 540 give a discrimination-matrix backbone, **different purpose**. Nature: **pure speculative**.

**S-38 Reproducibility / cross-laboratory consistency.** Problem: do different laboratories with different pipelines reproduce the same experiment with consistent results? Why interesting: reproducibility is the filter for "real signal vs. spurious signal." Related asset: V2/V3 multi-backbone × multi-cell design is itself reproducibility-friendly. Nature: **pure speculative**.

**S-39 Evaluation-of-the-evaluated recursion.** Problem: when the evaluated model knows "it is being evaluated," is the evaluation still valid? Why interesting: recursive game-theory turns detection into a time-varying problem. Related asset: **no direct match**. Nature: **pure speculative**.

**S-40 Long-term validity and drift.** Problem: are detection signals that work today still valid tomorrow? Why interesting: determines whether distillation detection is a "one-shot study" or a "continuing service." Related asset: V2 (09-11) → V3 (09-11) → D7 (09-18) time-series of discrimination assets can serve as a drift scaffold. Nature: **pure speculative** (asset reuse, different purpose).

### 3.8 What the seed field is, and is not

The seed field is a *prompt for thought*, not a research design. It does **not** order the seeds (no seed is "more important than" any other; the dimensional grouping is the author's organising choice, not a deposon-side decision). It does **not** select seeds (no seed is "picked for inclusion"; recipients may pick any subset, all, or none). It is **not** a coverage claim (the seven dimensions do not partition the theme; they overlap with each other and leave gaps). It is **not** an evidence base (each seed's "related asset" line names a *candidate* asset, with the nature of the support flagged).

Recipients are invited to engage with any subset of the seeds — to challenge, refine, extend, replace, or set aside any of them. The principal investigator will decide, later and separately, whether any of the resulting material becomes a service, a paper, a benchmark, or remains an open question.

---

## §4 Open questions

The following questions are *not* seeds (they are not productive research directions) and *not* commitments (they do not pre-decide the designer). They are *open questions the rebuild leaves on the table*, and the principal investigator invites the recipient community to surface their own additions or replacements. No ordering is implied.

1. **What is the smallest, falsifiable experiment that can distinguish "distilled from teacher X" from "trained independently on similar data"?** This is the *minimum* claim a distillation-detection benchmark would need to support. The reviewers flagged multiple blockers (R5 from KIMI-K3 on divergence definitions; B6 from Trae code on binning/KDE) that any answer would have to overcome.
3. **Can the V1–V3 evaluation grid be treated as a *student*-side signal surface at all?** The grid is a *teacher-side* evaluation; treating it as a student-side signal surface requires a hypothesis about what a distilled student would look like that has no current on-disk support.
4. **Is the 22-caption fingerprint a viable "stealth watermark" seed?** The 22-caption fingerprint was built for discrimination, not for output-watermarking (S-13, S-19). Re-using it as an output-watermark prototype is a re-fit hypothesis, not a calibrated finding.
5. **What would a *reverse*-distillation claim even look like, given that deposon's artifacts are teacher-side and have no student-side ground truth?** This is the GT dilemma (S-36). Any distillation-themed experiment must declare its GT source.
7. **Does the theme have a defensible scope that excludes the cross-disciplinary seeds (Dimension 6)**? Or is the analogy space (curvature, observer effect, no-cloning, Bell) part of the theme's natural vocabulary? This is a *scope* question, not a *priority* question, and the principal investigator will decide it.
9. **Which of the 40 seeds are *productive* questions and which are *non-productive*?** Productivity here means: would a concrete, falsifiable experiment that falsifies the question also falsify a substantive claim? The principal investigator does not pre-judge this for any seed.
11. **Does the *theme-driven, framework-free* invitation actually help the recipient community engage, or does it leave them without enough scaffolding to contribute?** This is a question about the invitation itself, and the principal investigator invites honest answers.

The list is open. Recipients may add, replace, or reorder any item, with the understanding that "open question" status is conferred by the principal investigator, not by the recipient.

---

## §5 Recipients and what is asked

This section names the recipient communities the principal investigator intends to invite. It does **not** assign work lanes, checkpoints, schedules, output formats beyond "Markdown reply on the recipient's natural channel," or hours-per-week budgets.

### 5.1 Recipients (named communities; **no assignments**)

- **KIMI-K3** (paper-track reviewer across V1–V3, 凝子-agent)
- **Trae code** (IDE-track reviewer)
- **Trae IDE** (IDE-track reviewer)
- **GLM** (paper-track reviewer)
- **coze** (paper-track reviewer)
- **VS** (wider-brainstorming reviewer)
- **workbuddy** (workplace-bundle reviewer)
- **豆包工作** (workplace-bundle reviewer)
- **Any new collaborator** who reads this invitation and finds a question worth their time

### 5.2 What is asked of every recipient

- **Ideas.** What is the most important question in the seed field that the on-disk V1–V3 stack could in principle inform? What is the most important question that no on-disk stack could inform? The recipient may pick any subset of the 40 seeds, all, or none.
- **Evidence.** Does any on-disk V1–V3 artifact directly support or refute a specific seed's "why interesting" line? Recipients are asked to cite by **path + SHA-12 prefix + line range**, and to flag (in the same reply) any citation that, on closer reading, does not hold.
- **Critique.** Does any seed in the seed field fail its own "why interesting" frame? Does the seed field systematically over- or under-weight any direction? Does the open-question list miss the asker? Recipients are asked to name the seed or question, the line of critique, and (where possible) the on-disk artifact that supports the critique.
- **Doubt.** Recipients are explicitly invited to express *uncertainty* and to mark their own contributions as such. A seed the recipient picks may turn out to be unproductive; a citation the recipient offers may turn out to be wrong; a critique the recipient offers may turn out to be misplaced. The principal investigator prefers an honest "I am unsure" over a confident "this is right."

### 5.3 What is **not** asked of any recipient

- No recipient is asked to modify any V1–V3 frozen asset.
- No recipient is asked to write or run code against any V1–V3 frozen asset.
- No recipient is asked to produce a paper draft, a benchmark, a leaderboard, a model, or a service.
- No recipient is asked to commit to a co-authorship list or a deliverable schedule.
- No recipient is asked to disclose, format, or channel proprietary prompts, model endpoints, or anything that resembles an API key or token.

### 5.4 Reply channels (recipient's own choice; no prescribed format)

The principal investigator accepts replies in:

- Markdown attached to the deposon paper-track channel (KIMI-K3, GLM, coze).
- Markdown attached to the deposon IDE-track channel (Trae code, Trae IDE).
- Markdown attached to the deposon workplace-bundle channel (workbuddy, 豆包工作).
- A wider-brainstorming reply (VS).
- Any new channel a recipient proposes.

There is no prescribed length, no prescribed structure, no prescribed verdict, and no prescribed evidence format beyond "cite by path + SHA-12 prefix when citing."

---

## §6 Authorship, AI use, and disclosure

### 6.1 Authorship

The sole accountable author of this invitation is the human principal investigator. AI contributions are acknowledged, not authorship. **AI is not an author.** CRediT role assignment is at the principal investigator's discretion.

### 6.2 AI use

This invitation was drafted by `doc-writer` (Mavis 8-agent team) under the following AI-use boundaries:

- No LLM API was called in the drafting of this document.
- No external URL was fetched in the drafting of this document.
- No proprietary prompt, model endpoint, API key, or token appears in this document.
- Two skill documents were read for writing-craft guidance: `academic-paper-polish` and `scientific-writing`, both from the Mavis plugin-cache, neither invoked as a model.

The brainstorming seed field (§3) was authored on 2026-09-20 by a worker under the same boundary discipline and is reproduced here under the same authorship boundary.

### 6.3 Recipient-side AI disclosure

Any recipient whose reply contains AI-assisted content is asked to disclose that fact at the top of their reply. The disclosure should name the AI tool used and the purpose (e.g., "drafting language only" / "structural ideation only"). Recipients are asked **not** to fabricate AI-disclosure claims — if a recipient's reply contains no AI-assisted content, the disclosure may say so plainly.

### 6.4 Uncertain proper nouns — placeholders held open for PI ruling

The following proper nouns appear in this invitation or its supporting seed file, but the principal investigator has not, in writing, confirmed a canonical form for each. Recipients are asked to read placeholders as placeholders:

| Placeholder | Used for | Status |
|---|---|---|
| `KIMI-K3` | The paper-track reviewer agent whose public product name is `KIMI-K3` per the v0.1/v0.2 invitation and the 凝子-agent note. **The on-disk API endpoint is `kimi-for-coding` (per the principal investigator's 2026-09-08 rule) — these two names refer to the same model family but are not the same string. The principal investigator must rule on whether this invitation should write `KIMI-K3` (public) or a different placeholder.** | `[待 PI 裁定]` |
| `M3` / `minimax` | The fifth `by_model/` directory, literally named `minimax` on disk, occasionally written `M3` in V0.1 prose. The principal investigator must rule on which name is canonical in deposon-side prose. | `[待 PI 裁定]` |
| `21 caption-fingerprint pairs` / `22 captions` | The on-disk count is **22** (file `corpus/v20/strip_captions_22.json`). The V0.1 invitation wrote "21 caption-fingerprint pairs." The principal investigator must rule on whether the canonical figure is 21 (caption-fingerprint *pairs*) or 22 (caption *entries*). | `[待 PI 裁定]` |
| `P-G v01` | The P-G v01 non-Euclidean-curvature scaffold. The on-disk compute file is `_pg_v01_compute.py` and the on-disk landing is `deposon_pg_v01_9m60c_2026_09_15.json`. The principal investigator has not confirmed a public project code name; `P-G v01` is the deposon-side shorthand. | `[待 PI 裁定]` |
| `V7` / `R5` | The V3 terminal-report version identifier. On disk: `docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` (V7). No `R5` exists on disk. The principal investigator must rule on whether deposon-side prose should ever mention `R5`. | `[待 PI 裁定]` |

The principal investigator's ruling on these placeholders will be incorporated in a later revision. Until then, recipients are asked to read each placeholder as the on-disk artefact it points to.

---

## §7 Unresolved items

This section names items the rebuild leaves explicitly unresolved. The principal investigator invites corrections, additions, and replacements.

1. **The 9-backbone / 5-artifact mapping (Claude Code §2 finding).** V1–V3's evaluation grid is 9-backbone × 60 cells. The `corpus/v20/by_model/` layer is 5 artifacts. The reviewer community has not been told which of the 9 backbones map to which of the 5 artifacts, and on disk the mapping is not declared. **Until the principal investigator declares a mapping, any claim about "the 9 teachers" or "the 5 teachers" is under-specified.** `[待 PI 裁定]`
2. **The 21-vs-22 caption count (B4).** The on-disk count is 22 (`corpus/v20/strip_captions_22.json`). The V0.1 prose said "21 caption-fingerprint pairs." The two numbers describe different things (entries vs. pairs). The principal investigator must rule on which is the canonical figure for deposon-side prose. `[待 PI 裁定]`
3. **The `M3` / `minimax` directory name (B1, F1).** The on-disk name is `minimax`. V0.1 prose wrote `M3`. The principal investigator must rule on the canonical prose name. `[待 PI 裁定]`
4. **The KIMI public-vs-API naming.** On disk: `kimi-for-coding` is the API endpoint (per the principal investigator's 2026-09-08 rule). In deposon-side prose: `KIMI-K3` is the public product name. The two are not the same string. The principal investigator must rule on whether prose should write `KIMI-K3`, `kimi-for-coding`, or another form. `[待 PI 裁定]`
5. **The `V7` / `R5` version identifier (F4).** On disk: V7. The principal investigator must rule on whether deposon-side prose should ever write `R5`. `[待 PI 裁定]`
6. **The P-G v01 verdict_pending status.** P-G v01 is **scaffolding tier, verdict_pending=true**. The principal investigator must rule on whether deposon-side prose may treat P-G v01 as anything other than a scaffold.
8. **The `_v4_experiment_invitation_2026_09_20_v0.2.md` lineage.** This rebuild is *not* a successor-version of v0.2 in the strict semantic-versioning sense. v0.1 and v0.2 are framework-bearing proposals; v1.0 is a theme-first rebuild. The principal investigator must rule on whether v1.0 is to be cited as a successor to v0.2 or as a parallel document. `[待 PI 裁定]`
10. **The seed-field's cross-disciplinary seeds (Dimension 6).** The author of the seed field has flagged Dimension 6 as "optional; not steered toward or away from." The principal investigator must rule on whether the cross-disciplinary seeds are in-scope, out-of-scope, or in-scope-as-analogy-only.
12. **The non-framework principle itself.** This rebuild is framework-free by the principal investigator's instruction. A future revision may decide that *some* scaffolding (a small list of named sub-questions, a small set of candidate GTs, a small set of falsification criteria) would help the recipient community engage. The principal investigator must rule on whether the framework-free principle holds for V4's lifetime or only for this initial rebuild. `[待 PI 裁定]`
14. **The recipient list (§5.1).** The principal investigator has named 8 existing recipient communities plus "any new collaborator." A future revision may add, retire, or merge recipients. Recipients who would like to be added or removed are invited to say so directly.
16. **The reviewer-burndown. ** The V0.2 framework absorbed nine independent reviewer responses (KIMI-K3 R1–R11; Trae code B1–B8; Trae code supplement F1–F6; coze S1–S4; workbuddy S1+; Claude Code §1–§3; VS; 豆包工作). Each of those responses contained a *theme-level* observation buried inside a *framework-level* critique. The principal investigator may wish to recover the theme-level observations explicitly; this rebuild does not do so, because doing so would re-import the framework the rebuild has set aside. The recovery, if any, will be a separate document. `[待 PI 裁定]`

This list is open. The principal investigator invites additions, corrections, and replacements.

---

## §8 Asset verification table

The following table records, for every V1–V3 asset cited in this invitation, the on-disk path, the on-disk byte count (measured at 2026-09-20, this session), and the first 12 hex characters of the SHA-256 hash (measured at the same time). Recipients may re-derive these values at any time; this table is not a substitute for an independent verification.

| Path | Bytes | SHA-256[:12] | Cited in |
|---|---|---|---|
| `_repo_mirror\corpus\v20\by_model\kimi\index_v2_2026_09_16.json` | 24,150 | `EFE05AD775DE` | §2.1, §3.1 S-03/S-07/S-15/S-17, §3.6 S-30 (cross-ref) |
| `_repo_mirror\corpus\v20\by_model\GLM_1\three_way_glm_slot_blind_test_2026_09_16.json` | 19,685 | `268AB1239A8A` | §2.1, §3.1 S-03/S-07/S-15/S-17 |
| `_repo_mirror\corpus\v20\by_model\GLM_2\glm_artifact_v_2026_09_16.json` | 13,150 | `39732A92B5C9` | §2.1, §3.1 S-03/S-07/S-15/S-17 |
| `_repo_mirror\corpus\v20\by_model\coze\coze_artifact_v_2026_09_16.json` | 10,978 | `FEE04170AA73` | §2.1, §3.1 S-03/S-07/S-15/S-17 |
| `_repo_mirror\corpus\v20\by_model\minimax\artifact_v_2026_09_16.json` | 25,347 | `9E1CCBDCEACC` | §2.1, §3.1 S-03/S-07/S-15/S-17 |
| `_repo_mirror\results\deposon_v2_phase1_60cells_2026_09_11.json` | 85,508 | `A18BBC703B42` | §2.4, §3.1 S-06, §3.7 S-37 |
| `_repo_mirror\results\deposon_v2_phase2_dual_mainline_2026_09_11.json` | 3,189 | `E337B824C4B9` | §2.4 |
| `_repo_mirror\results\deposon_v2_phase4_f4_2026_09_11.json` | 5,212 | `CF7682348617` | §2.4 |
| `_repo_mirror\results\deposon_v3_v7_summary_2026_09_11.json` | 25,049 | `063AC8D00542` | §2.3, §3.1 S-04/S-37 |
| `_repo_mirror\docs\V3X\V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` | 38,545 | `4A08521F8DE1` | §2.5, §3.2 S-10 |
| `_repo_mirror\results\d7_5anchor_60cells_9model_verdict_2026_09_18.json` | 2,456 | `4505CCA79C15` | §2.3, §3.3 S-14, §3.7 S-37 |
| `_repo_mirror\results\boss_pa_1_rbr_rm_result_2026_09_15.json` | 8,753 | `C7C59E0D2F6C` | §2.2, §3.1 S-05, §3.7 S-37 |
| `_repo_mirror\results\deposon_pg_v01_9m60c_2026_09_15.json` | 11,512 | `AB75889EE738` | §2.7, §3.1 S-02, §3.2 S-08, §3.6 S-30 |
| `_repo_mirror\deposon_team\plugins\_pg_v01_compute.py` | 20,923 | `D511C545F88E` | §2.7, §3.1 S-02, §3.2 S-08, §3.6 S-30 |
| `_repo_mirror\deposon_team\plugins\_v3x_frozen_schema_v1.json` | 12,919 | `9E99DCC4D920` | §2.9 |
| `_repo_mirror\verifier\handoff\KT_ABC1_anchors_sha256_12.json` | 6,680 | `03C6C01F3697` | §2.6, §3.2 S-11 |
| `_repo_mirror\verifier\handoff\P_F_PREDECISION_2026_09_11_V0.1.json` | 12,498 | `312D635E6259` | §2.6 |
| `_repo_mirror\corpus\v20\index_v2_2026_09_16.json` | 24,150 | `EFE05AD775DE` | §2.6 (note: same SHA-12 prefix as `corpus/v20/by_model/kimi/index_v2_2026_09_16.json`; flagged for PI ruling) |
| `_repo_mirror\corpus\v20\strip_captions_22.json` | 12,798 | `6A2656878745` | §2.6, §3.2 S-11, §3.3 S-13, §3.4 S-19 |
| `_repo_mirror\attacks\a1_delete_anchor.py` | 4,693 | `78AC391D16FC` | §2.8, §3.4 S-20/S-23 |
| `_repo_mirror\attacks\a2_reshuffle_manifest.py` | 3,792 | `3D54B277620E` | §2.8, §3.4 S-20/S-23 |
| `_repo_mirror\attacks\a3_rewrite_runs.py` | 4,254 | `F02B3EEE8D6E` | §2.8, §3.4 S-20/S-23 |
| `_repo_mirror\results\_v4_brainstorm_seeds_2026_09_20.md` | (see SHA-12) | (seed source; this section's seed field is reproduced from this file, not modified) | §3 |
| `_repo_mirror\results\_v4_experiment_invitation_2026_09_20_v0.2.md` | (see SHA-12) | (historical reference only; framework discarded) | §0.2, §1, §7 |
| `_repo_mirror\results\_kimi_v4_t12_review_2026_09_20.md` | (see SHA-12) | (recipient review input) | §1 |
| `_repo_mirror\results\_v4_acceptance_coze_2026_09_20.md` | (see SHA-12) | (recipient review input) | §1 |
| `_repo_mirror\results\_v4_acceptance_trae_code_2026_09_20.md` | (see SHA-12) | (recipient review input) | §1 |
| `_repo_mirror\results\_v4_ide_track_review_trae_code_supplement_2026_09_20.md` | (see SHA-12) | (recipient review input) | §1, §2.3 |
| `_repo_mirror\results\_v4_d1_response_workbuddy_2026_09_20.md` | (see SHA-12) | (recipient review input) | §1 |
| `_repo_mirror\results\_v4_review_claude_code_2026_09_20.md` | (see SHA-12) | (recipient review input) | §1, §2.2, §7.1 |

**No on-disk artifact corresponds to:** observer-effect frames (S-31); Bell-inequality frames (S-35); quantum no-cloning frames (S-32); training-curve records (S-14); logit-level records (S-09); output-watermark artifacts (S-13, S-19); per-byte distillation / reverse-distillation / anti-distillation findings (any V1–V3 V-tier). These are pure-speculation seeds, **not** re-fit hypotheses.

---

## §9 Closing note

This invitation ends with a single sentence: the deposon V1–V3 asset stack is real, the theme is real, the seed field is real, and the principal investigator's instruction is to invite thought rather than prescribe work. Recipients who find the theme worth their time are warmly invited to reply on their natural channel. Recipients who do not are warmly invited to set this invitation aside. No recipient owes the principal investigator an answer in either direction.

— `doc-writer`, Mavis 8-agent team, deposon workspace, 2026-09-20.

<!-- appended-note:2026-09-30 skill 引用面复核（PI 派工第④项 · 0 删改历史字面） -->

> **附注（2026-09-30 追加 · 非原件内容）**
> 本件原引用字面**逐字保留、0 删改**；本附注**只增不改**。
>
> - **原引用面**：L322（出现 1 处）· 「both from the Mavis plugin-cache」无哈希字面
> - **2026-09-30 只读复核**：原引用字面**2026-09-30 仍成立**（写死路径逐字在位、树哈希同目录名、关键 `SKILL.md` SHA-12 对得上）⇒ **无过期值可改**，故仅追加注记、**不就地更新**
> - **当前三段式锚**（plugin:skill + 树哈希前 12 + SKILL.md SHA-12 + 定位方式）：``academic-paper-polish`` · 树 ``01afed677637`` · ``SKILL.md`` SHA-12 ``23d90731e1fe`` / 7,095 B
> - **对外件口径**：本件为**已对外发出件**。路径与树哈希写死之陈旧风险（起因件建议 A1）**仍成立**——建议后续对外件改记 plugin:skill 名，路径与哈希只在内部登记件记实测值。本附注**仅供内部对账，未随原件对外发出**。
> - **执行件**：`results/_skill_reference_update_and_user_surface_survey_2026_09_30.md` · 出件 **worker**（本棒）· **0 删改本件任何既有字节**