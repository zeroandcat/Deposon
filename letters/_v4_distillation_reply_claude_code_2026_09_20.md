# Reply to the V4 distillation invitation — Claude Code

**AI-use disclosure.** This reply was written by Claude Code (Anthropic), an AI agent, operating as a reader with filesystem access in the deposon workspace. No LLM API was called by any script I ran; I read files, computed SHA-256 prefixes, and wrote this document. For §5 I delegated part of the search to eight parallel Claude readers working on separate angles, and every citation of theirs that appears here I re-derived myself at the stated path and line range before including it — where a sub-claim failed that check I dropped it, and two such cases are recorded in §5.6. Sections §5.6, §5.10 and §5.5 also required *executing* repository code read-only (importing `boss_pa_1_rbr_rm.py` and `_pg_v01_compute.py` and calling their functions on synthetic inputs) rather than only reading it; no frozen asset was written to, no file in `verifier/`, `.mavis/`, `.builtin/` or `scripts/` was modified, and no network call was made. The judgement in this document is mine, not the principal investigator's, and it should be read as such.

**Have I read the invitation in full?** Yes — `results/_v4_distillation_invitation_2026_09_20_v1.0.md`, 30,820 bytes, SHA-256[:12] `4E8C0EA57028`, all 411 lines, plus the eleven core files in the prompt pack's §4 index and the supplementary files their citations pointed to.

---

## 1. Corrections and confirmations to the invitation

The principal investigator prefers an honest contradiction to a polite agreement (task rule F), so these come first.

### 1.1 One arithmetic error

`_v4_distillation_invitation_2026_09_20_v1.0.md:66` states `results/boss_pa_1_rbr_rm_result_2026_09_15.json` is "8,674 bytes." Disk says 8,753 bytes; the invitation's own §8 table at line 383 also says 8,753. The §8 value is correct and line 66 is wrong — the digits are transposed. The SHA-12 `C7C59E0D2F6C` is correct in both places, so nothing downstream is affected.

### 1.2 The §2.5 citation does not hold

§2.5 (line 89) and §3.2 S-10 (line 166) both anchor the disturbance claim to `docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` (`4A08521F8DE1`). That file contains **zero** occurrences of 扰动 / 干擾 / 擾動 / perturb / disturb. The string `disturb` does not appear in it at all.

The real disturbance protocol is on disk elsewhere:

- `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` (`bd1caab42b4c`), lines 115–117: "A1：提示词扰动：调换 system prompt 中机制描述顺序 3 次，重跑 10 cell"; "A2：温度敏感性：LLM temperature 0.0/0.5/1.0 三档"; "A3：种子复现：seed=42, 123, 456 三套."
- `docs/V3X/V3X_D6_PAPER_V2_2026_09_09_mavis.md:249`: "按各 SPEC §5: A1 提示词扰动 3 次 / A2 温度 0.0/0.5/1.0 / A3 种子复现 42/123/456 — **未跑**(LLM 部分未实跑)。Phase B 必补。"

So S-10's `Nature: pure speculative` label is right, but its *related asset* line points at a file that says nothing about the seed. Under the invitation's own three-way taxonomy this is a fourth thing — a citation error attached to a correct classification — and I am reporting it rather than silently re-bucketing it. The same wrong path is repeated in the prompt pack's §4 index row 12.

### 1.3 §2.2 inverts the direction of the evidence

§2.2 (line 66) says `boss_pa_1_rbr_rm_result_2026_09_15.json` "encodes the 9-backbone × 60-cell evaluation." It does not. Its top-level keys are `['boss', 'boss_id', 'reference', 'date', 'started_at', 'iron_rule_compliance', 'inputs', 'v3_540_conservation_check', 'boss_pa1_22graph_simulation', 'verdict', 'verdict_note', 'comparison_to_pa_spec', 'next_step']` — it is a Repeated-Best-Response / Regret-Matching simulation (Hart & Mas-Colell 2000) that **reads** the grid, and its `iron_rule_compliance` records `"method": "纯 Python stdlib (json + hashlib + random + math), 0 numpy 依赖, 0 LLM"`.

Its `n_models = 9 / n_540_total = 540` is a **conservation count** (T + R + A = 1 across 540 cells, `conservation_residual_540: 0`), not an evaluation. Every 3-vector summing to 1 makes a zero residual arithmetically necessary; it is not an empirical finding about models. The actual grid measurements live in `results/deposon_v3_physical_opt_60cells_2026_09_11.json` (`c659695aa23c`, 17,732 bytes), whose `input_data.9_models` lists all nine backbones with per-model T/R/A/T_frac and whose `scope` reads "9 model × 60 cells = 540 cells 双边展开 + 9 model × 4 T_frac bins = 36 判决线对照."

This matters for S-03 and S-05. A behavior surface staged on a normalized conservation identity has no variance to distill from.

### 1.4 A cited input is not on disk

`boss_pa_1_rbr_rm_result_2026_09_15.json` lists as its first input `results/deposon_v20_baselines.json` with SHA-12 `6edb2aec1660`. That file does not exist in the repository — a repo-wide search returns only `run_v20_baselines.py`, the generator. The same hash appears in `verifier/handoff/KT_ABC1_anchors_sha256_12.json` under `KT_A1.P_A_FROZEN_RUNS` as the first of five frozen run hashes `["6edb2aec1660", "910c4333eead", "9d9ae5001c57", "62c1a41e1db8", "af51da229652"]`, listed as `"path": "results/deposon_v20_baselines.json + v19 + v21 + v18 + v17"`. Nor is either file mentioned anywhere in the invitation or the prompt pack (grep count 0 in both).

I cannot tell from the files alone whether this is an archival move, a `_archive_deposon_2026_09_17` relocation (that path appears in `deposon_team/plugins/_verify_15frozen_v1.py:6`), or a genuine loss. I flag it because the frozen-run hash set is a trust anchor, and a trust anchor whose file is missing is not currently re-derivable by a recipient.

### 1.5 `corpus/v20/by_model/kimi/` is the corpus index, not a KIMI artifact

`corpus/v20/by_model/kimi/index_v2_2026_09_16.json` and `corpus/v20/index_v2_2026_09_16.json` are byte-identical (`cmp` reports identical; both 24,150 bytes, both `EFE05AD775DE`). The `kimi/` directory contains exactly one file. Its content is the corpus definition — `"corpus": "v20"`, `"generator_version": "v2.0.0"`, `"spec": "docs/SPEC_v2.0.md §1"`, `"n_graphs": 22`, and a `graphs` array.

The §2.6 note at line 95 asks the PI to rule on "co-location." I can narrow that question: this is not co-location of two different files, it is one file present at two paths. The practical consequence for the theme is that the `by_model/` layer contains **four** distinct artifacts (GLM_1, GLM_2, coze, minimax), not five, and the "KIMI teacher output sample" that S-03/S-07/S-15/S-17 lean on is not a model output at all. Whether the KIMI-side predictions exist in some other form is a separate question — see §1.6.

### 1.6 A correction in the other direction: a cross-model artifact does exist

Item 1 of §7 says the 9-backbone/5-artifact mapping is undeclared and that "any claim about 'the 9 teachers' or 'the 5 teachers' is under-specified." That is right. But there is one by_model artifact whose contents go further than its row in §2.1 suggests: `corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json` (`268AB1239A8A`). Its top-level keys are `['task', 'preregistration', 'baseline_ref', 'consistency_checks', 'own_artifacts', 'glm_artifacts_ref', 'glm_artifact_set_sha256', 'glm_predictions', 'kimi_predictions_frozen_ref', 'blind_results', 'metrics', 'observational_addon']`. Its `task` reads "P-K → GLM 三位定位 (基线: 自己 vs GLM vs KIMI, 列表冻结阅读)", and its `metrics` block carries `FPR: 0.0444`, `FNR: 0.0`, `SP_t: 1.0`, `anti_whitewash_total: 0.9555`, with per-transform entries `W1_key_reorder`, `W2_newline_inject`, `W3_comment_inject`, each showing `glm_measured: 0.9130` beside `kimi_frozen_ref: 22` (lines 590–604).

So the file holds, for a shared item set, one vendor's measured behaviour and another vendor's frozen predictions, side by side. That is a cross-model agreement surface. I return to it under S-17 below. It also means GLM_1 is not merely "a second teacher's per-cell output with a different shape" (line 57) — it is the only by_model artifact that references a second model at all.

### 1.7 The "18 frozen anchors" figure needs a PI ruling

S-11 (line 168) names "18 frozen anchors + 22 caption entries + 5 KT anchors (`KT_ABC1_anchors_sha256_12.json`)" as an edge-case library. I checked each part:

- `KT_ABC1_anchors_sha256_12.json` (`03C6C01F3697`) contains 15 entries in three groups, five each: KT-A1 `['P_A_ECR_BASELINE', 'P_A_KILL_LINE', 'P_A_FROZEN_RUNS', 'P_A_LLM_CLIENT', 'P_A_HARNESS']`, KT-B1 and KT-C1 similarly. Fifteen, not five — unless "5" counts the three groups plus something.
- `deposon_team/plugins/_v3x_frozen_schema_v1.json` (`9E99DCC4D920`) contains 16 anchors: 7 spec, 4 plugin, 2 anchor_json, 2 benchmark, 1 corpus. Its version is 1.0.
- The string "18 frozen" appears in the repository only in `results/_adendum_FGK_complete_20260917_143033.md:20,166` and the archived `results/_archive_2026_09_18/_trae_5audit_aggregated_2026_09_17.md:19,22,120,132,159`.

So "18 frozen" is a term of art from the 2026-09-17 audit trail, "15" matches the KT anchor file's entry count, and "16" matches the frozen schema. These may well be three different things (frozen *artifacts* vs. frozen *schema anchors* vs. KT *entries*), but the seed field uses them interchangeably and a reader cannot tell which set S-11 means. This is a PI ruling, and I would add it to §6.4's placeholder table.

### 1.8 What the citation discipline itself does

Every value in the §8 table that I could re-derive is correct: all 22 populated rows match disk exactly on both bytes and SHA-12, including the ones I would have expected to drift (`deposon_v2_phase1_60cells_2026_09_11.json` at 85,508 bytes / `A18BBC703B42`; the three attack scripts; both P-G v01 files). The invitation's own SHA-256 re-derives to `4E8C0EA57028AF400D8B8B1A29C92AC85A656E98BA20D50A462CB6808739BF84` over 30,820 bytes, matching the value recorded in `results/_v4_ide_track_review_trae_code_2026_09_20.md` §1 — the file has not changed since that review.

Eight rows in §8 are left as "(see SHA-12)" placeholders. Filling them is not my call, but the values are: `_v4_brainstorm_seeds_2026_09_20.md` 14,994 / `0EB1CFAA2992`; `_v4_experiment_invitation_2026_09_20_v0.2.md` 41,680 / `8E1E7434905D`; `_kimi_v4_t12_review_2026_09_20.md` 6,644 / `38070FD12F31`; `_v4_acceptance_coze_2026_09_20.md` 5,467 / `B2BF2A073AC8`; `_v4_acceptance_trae_code_2026_09_20.md` 6,301 / `3205593030BC`; `_v4_ide_track_review_trae_code_supplement_2026_09_20.md` 11,877 / `D3BDFC99FCDC`; `_v4_d1_response_workbuddy_2026_09_20.md` 14,881 / `BC663B671994`; `_v4_review_claude_code_2026_09_20.md` 7,004 / `B6F9956BCF5C`.

One note on this. §8 says the table "is not a substitute for an independent verification." I agree, and I would go further: because eight rows are unfilled, a recipient reading §8 cannot currently see that the review inputs are frozen at all. A table that verifies the assets but not the reviewers' inputs verifies half of what a provenance discipline is for.

### 1.9 The seed field's Nature column

I counted the nature labels across all 40 seeds (lines 146–238). **All 40 read `Nature: **pure speculative**`.** There is not one `disk fact`. Line 140 defines the column as "`disk fact` if any on-disk artifact directly supports a finding; `pure speculative` if no on-disk artifact exists for this seed," so the column is doing exactly what it says — but a reader who takes §3's four-element structure at face value will look for a spread that isn't there.

I read this as the honest consequence of §0.2's central fact (V1–V3 has zero distillation experiments on disk), not as a defect. But it has a structural effect worth naming: **the seed field has no calibration point.** Nothing in it distinguishes a seed whose asset is one inference away from supporting the claim (S-03, where the by_model artifacts at least contain model outputs) from a seed whose asset supports nothing at all (S-21, S-22, S-24, S-26, S-27, S-29, all "no direct match"). Task rule 2 asks me not to bury the distinction between fact, re-fit hypothesis, and speculation. The field as authored collapses a real gradient into a single label, and the gradient is what a reader needs most.

---

## 2. Engagement with individual seeds

### S-03 — Behaviour-level transfer

**Critique.** The "why interesting" line says "behaviour is the most externally observable layer of a teacher," which is fine, but the related-asset line does more work than it can carry: "the five frozen artifacts under `corpus/v20/by_model/{kimi, GLM_1, GLM_2, coze, minimax}` are cross-model behaviour samples." Per §1.5 above, one of the five is the corpus index, so there are four. Per sampling the non-kimi files, they are not behaviour samples in the sense the seed needs: their top-level keys are `['schema', 'created_ts_utc', 'note', 'count', 'artifacts']` (GLM_2), `['schema', 'created_ts_utc', 'subject', 'subject_label_location', 'artifact_count', 'source_root', 'note', 'three_hashes_convention', 'trust_anchor_5_concat', 'artifacts']` (coze), and `['meta', 'three_hashes', 'artifacts']` (minimax). They are **hash manifests over artifacts**, with a `three_hashes` convention. Only GLM_1, with its `glm_predictions` and `blind_results`, carries measured model behaviour.

So the by_model layer gives the theme one behavioural sample, not four. If S-03 is to be staged, the question "whose behaviour is being transferred?" has one candidate answer on disk, not four.

**Doubt.** I cannot tell from the manifests alone whether the artifacts they point at (which live under `source_root`, outside the paths I read) contain the per-cell outputs S-03 would need. That is a follow-the-pointer question and I did not follow it, so I mark it as unverified rather than absent.

### S-06 — Refusal-boundary transfer

**Evidence.** `results/deposon_v2_phase1_60cells_2026_09_11.json` (`A18BBC703B42`) at lines 2615–2627 records `"total_cells": 60, "existing_30_passed": 25, "new_30_passed": 26, "total_passed": 51, "pass_rate": 0.85, "verdict": "STRONG_PASS"`, and its `comparison` block at 2626–2629 reads `"no_rag_baseline_2_0_lite": "52/60 = 86.7% (projected, same as 30 baseline)"`, `"dpath_30cells_pass_rate": "25/30 = 83.3%"`, `"v2_60cells_pass_rate": "51/60 = 85.0%"`, `"delta_vs_30": "+1.7pp"`.

What that passage actually says: 51 of 60 cells passed on a **doubao-seed-2.0-lite** single-backbone run over a dpath metric, and the no-RAG baseline is *projected*, not run — "(projected, same as 30 baseline)". The `v2_60cells_pass_rate` string at 2627 is a label inside the `comparison` block, and `verdict: STRONG_PASS` at 2622 is the verdict of the enclosing block, not a file-level verdict.

The seed's problem line — "how finely can a teacher's refusal boundary be replicated by a student?" — is not what this number measures. The dpath metric is a discrimination-pass rate on a 60-cell layout. Calling it a "refusal curve" (as S-06's asset line does, by saying it "is a discrimination verdict, not a refusal curve") is a correct disclaimer, but the seed then has no anchor and should not have been written with an asset line at all.

**Critique.** S-06 is the clearest case in the field of a seed whose asset line creates a false affordance. A reader sees a byte count and a hash, and the hash is real, so the seed *looks* anchored. It is not.

### S-10 — Disturbance sensitivity

Covered in §1.2. Beyond the citation failure: the protocol that does exist (`P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md:115–117`) is designed to test **implementation stability**, not model robustness — A1 checks whether prompt-order changes flip the cost multiplier by more than 50%, A2 checks temperature sensitivity, A3 checks seed reproducibility. These are controls on the experimenter's own pipeline. S-10 wants a property of the *model*. The re-fit is therefore two steps, not one: the protocol would have to be both executed (it never was) and repurposed (from pipeline control to model probe).

### S-11 — Long-tail consistency

Covered partly in §1.7. **Evidence on the caption half:** `corpus/v20/strip_captions_22.json` (`6A2656878745`) parses as a 22-element **list**, each element a dict with keys like `{"id": "L_algorithm_process", "text": "…", "family": "L", "structure": "llm_generated_dag", "n_labels": 38}`. The `text` field is a semicolon-separated list of concept labels ("…; 前向传播; 反向传播; 梯度计算; …"), i.e. the vocabulary of a generated graph, not a caption sentence and not a fingerprint pair.

This is directly relevant to §6.4's 21-vs-22 placeholder (line 338) and to §4's open question 4 (line 254, "Is the 22-caption fingerprint a viable 'stealth watermark' seed?"). The file is not a set of caption-fingerprint pairs that happen to number 22; it is 22 label-sets. Whether "21 pairs" and "22 entries" describe the same object at different granularities, as line 338 supposes, is something I cannot determine — but if a recipient is going to build a watermark prototype on this file (S-13, S-19), they should know it contains graph label vocabularies, and a watermark needs output text.

**Doubt.** The 22 `id` values match the 22 concept_ids in `results/deposon_v2_phase4_f4_2026_09_11.json` and the 22 graph_ids in `boss_pa_1`. That is a strong signal of one shared object, but I have not verified the id lists are identical element-by-element, only that the counts and the naming convention agree.

### S-13 and S-19 — Steganographic fingerprints / output watermarks

**Critique.** Both seeds say the 22-caption fingerprint is "unrelated" to watermarking, which is honest. But the seed field treats the correlation between the two as one-directional. The more interesting direction is diagnostic: `results/deposon_v2_phase4_f4_2026_09_11.json` (`CF7682348617`) at line 5 records `"n_captions": 22` and carries both byte-level hashes (line 37 onward, e.g. `"S1": "3696ad59777e"`) and a separate semantic-hash set, with `class_intra_hamming` reported as `{L: 2.47, S1: 2.67, S2: 2.8, S3–S6: 0.57}`. The 12-bit fingerprints are computed on SVD-2 coordinates with random hyperplanes, seed=42.

The diagnostic value is this: a 12-bit fingerprint over 22 items is a **near-degenerate** space. With 4,096 buckets and 22 items, the expected hamming distance between two random items on 12 bits is 6.0; the reported classes sit at 0.57 and 2.47. Those numbers are not noise-scale, but they are also not resolvable without the raw bit strings, which the file stores as hashes. I would want the unhashed 12-bit vectors before believing the S3–S6 cluster is a genuine structure rather than an artifact of SVD-2 coordinate collapse. This is a doubt about a re-fit, not a claim.

### S-17 — Cross-model provenance

**Idea, built on §1.6.** `corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json` already contains the exact experimental shape S-17 asks for. Its `task` line names the design — "基线: 自己 vs GLM vs KIMI" — and its `metrics` block reports GLM's measured anti-whitewash rate (0.9130) beside a frozen KIMI reference of 22 items, with `FPR 0.0444 / FNR 0.0 / SP_t 1.0`. Given multiple candidate teachers, the artifact records which candidate's predictions match on which items.

The obvious next use is provenance inference: **given a held-out item set, can the producing model be identified from its discrimination pattern alone?** The design already has the two ingredients — a candidate set and per-item agreement. What it lacks is a third and fourth candidate to make the task non-trivial (two-way attribution is barely above chance), and a null model specifying what agreement a non-source model would show.

**Re-fit hypothesis, stated plainly: this is a re-fit hypothesis; the artifact was built for blind-test slot positioning, not for provenance inference; no calibrated finding is claimed.** The FPR/FNR/SP_t values in that file are properties of the discrimination task, and importing them as provenance-detection rates would be exactly the promotion rule 2 forbids.

**Doubt.** The `kimi_frozen_ref: 22` entries record 22 items but I did not verify that the 22 KIMI items and the 44 held/total items in the W-transforms (`"held": 43, "total": 45`) are drawn from the same set. If the two models were evaluated on different item sets, the agreement surface I am describing does not exist.

### S-31 — Observer effect / measurement-as-perturbation

**Doubt.** §2.10 (line 121) states "No `observer-effect` frame artifact exists on disk." That is true of a *frame*. But there is a related empirical record I would want the PI to rule on: `results/skill_d_p_f_observer_result_2026_09_11.json` and `deposon_team/plugins/skill_d_p_f_observer.py` (`3e369a1f6171`, a frozen schema anchor) carry a "P-F 1 周判死 observer" design, and the file header records `"d5_decision": "1A:D_fix2 metric + strict 阈值 (<0.05 / [0.05,0.15) / >=0.15)"`. That is an observer in the *monitoring* sense, not the measurement-perturbation sense — it observes a verdict, it does not perturb a subject. So S-31's "pure speculative" label survives.

I raise it only because "observer" is a loaded term in this repository, and a recipient searching for evidence under S-31 will find that file and may read it as support. It is not support. A one-line disambiguation in §2.10 would prevent a wasted reading.

### S-32, S-35 — No-cloning and Bell-inequality analogies

**Critique of both, jointly.** These are the seeds where I think the field's "pure speculative" label understates the problem. The issue is not that no artifact supports them; it is that the analogies are **structurally** weak in a way a reader can check in a sentence.

No-cloning holds in quantum mechanics because of linearity and the impossibility of copying an unknown state; a model's weights are classical parameters and *can* be copied exactly — that is what checkpoint distribution is. The interesting no-cloning-flavoured question in distillation is about *capability* under a fixed compute budget, not about state copying, and that is a different theorem. Similarly, a Bell-type test needs a violation of a Bell inequality under locality and measurement-independence assumptions; a black-box model has neither separated spacelike measurements nor the freedom-of-choice premise.

I am not saying the seeds are useless. I am saying Dimension 6's framing (line 214) — "analogies or formal tools, not directional recommendations" — invites a reader to treat them as a formal-tool reservoir, and for these two the tools do not transfer. The seeds a reader should spend time on in Dimension 6 are S-30 (curvature, which has an actual scaffold) and S-34 (reasoning collapse, which at least has a measurable phenomenon).

**Pure speculation, stated plainly:** any claim that a no-cloning-like or Bell-like result bounds distillation is pure speculation; no on-disk artifact supports it, and I do not think the formal analogy holds either.

### S-36, S-37, S-38 — Evaluation science

**Evidence for S-37.** `results/d7_5anchor_60cells_9model_verdict_2026_09_18.json` (`4505CCA79C15`) does carry the discrimination matrix §2.3 describes. Its `d7_results.P-A_cross_modal_dpath` gives nine `[model, verdict]` pairs — `doubao-seed-2.0-lite` PASS, `glm-5.3` PASS, `deepseek-v4-flash` PASS, `doubao-seed-evolving` PASS, `minimax-m3` PASS, `glm-5.3-flash` PASS, `kimi-k2.7-code` PASS, `doubao-seed-2.1-turbo` PASS, `deepseek-v4-pro` GRAY — and `P-E_3modal` gives the same nine with different outcomes (five PASS, `kimi-k2.7-code` GRAY, `doubao-seed-2.1-turbo` GRAY, `deepseek-v4-pro` FAIL). `P-C_two_phase` is `FAIL_H0 (幂律死)` at line 60, `P-F_D_fix2_strict` is `8+1+0 (PARTIAL_PASS, A channel timing 敏感)` at line 99.

This **is** a confusion-matrix-shaped object: nine models × two tasks, with a three-valued outcome. But it is a matrix over *models*, and a distillation FP/FN cost structure is a matrix over *claims about models*. Those are different axes, and the seed's own note ("different purpose") is right.

**Idea, offered as a re-fit.** The one thing this matrix can do cheaply for S-37 is calibrate what a *disagreement* looks like when nothing is being distilled. `kimi-k2.7-code` passes cross-modal dpath and is GRAY on 3-modal; `deepseek-v4-pro` is GRAY on the former and FAIL on the latter. That is two of nine models flipping outcome on a task-family change with no distillation anywhere in the pipeline. Any distillation-detection threshold that fires on a smaller flip than this is detecting the task family, not the distillation.

**Re-fit hypothesis, stated plainly: this is a re-fit hypothesis; the D7 file was built as a terminal verdict over discrimination tasks, not as a null-distribution estimator; no calibrated threshold is claimed.** Two-of-nine is not a distribution.

**Critique of S-38.** "V2/V3 multi-backbone × multi-cell design is itself reproducibility-friendly" is stated as though it were a property. The design is multi-backbone and multi-cell, yes. Whether that makes it reproducibility-friendly depends on whether independent laboratories would share the pipeline, and §1.4 above is a live counterexample: one of the five frozen run files is not on disk, so a laboratory trying to reproduce the V2 baseline today cannot. Reproducibility-friendly is a claim about artifacts being present and re-derivable, and one of them is not.

### S-40 — Long-term validity and drift

**Critique.** The asset line says "V2 (09-11) → V3 (09-11) → D7 (09-18) time-series of discrimination assets can serve as a drift scaffold." Two of the three timestamps are the same day. A time series with one time point and one replication seven days later is a very short baseline, and calling it a drift scaffold overstates what a seven-day gap can support. If the PI wants a drift baseline, the interesting quantity is how much a verdict changes under *no* intervention over the interval, and the D7 file's `P-A_cross_modal_dpath` results are the candidate — but they would need to be compared against an earlier run of the *same* task, not against V2's different task.

---

## 3. On the invitation's own open questions

**On §4 item 11** ("does the theme-driven, framework-free invitation actually help the recipient community engage, or does it leave them without enough scaffolding to contribute?"). I can answer this from inside the experience, which is the only honest vantage. The framework-free form worked: I engaged the seeds substantially more than I would have engaged a lane assignment, and §2's asset inventory is genuinely useful. The cost is specific, and it is the Nature column (§1.9 above). Without a spread of nature labels, the reader has to do the bucketing themselves for all 40 seeds, and the bucketing is where the errors in this reply were most likely to enter. A single additional column — "is the named asset one inference from the claim, or is it a different-purpose artifact?" — would fix it without importing any framework. That is a suggestion about a column, not a proposal for a structure.

**On §4 item 1** (the smallest falsifiable experiment). The seed field contains the ingredients for an answer that the invitation does not state, and I would rather point at it than invent one: the D7 nine-model matrix gives a null for outcome-flipping under task-family change (§2 above, S-37), and GLM_1 gives a cross-model agreement surface on a shared item set (S-17). A falsifiable test of "distilled from teacher X" needs a null distribution over *agreement*, and the repository has one artifact with agreement data in it. That is one artifact, and it is a re-fit, and I am not claiming more.

**On §7 item 1** (the 9-vs-5 mapping). I can advance this slightly. The nine backbones, from `results/deposon_v3_physical_opt_60cells_2026_09_11.json` `input_data.9_models`, are: `doubao-seed-2.0-lite`, `glm-5.3`, `deepseek-v4-flash`, `doubao-seed-evolving`, `minimax-m3`, `glm-5.3-flash`, `kimi-k2.7-code`, `doubao-seed-2.1-turbo`, `deepseek-v4-pro`. The four distinct by_model directories are `GLM_1`, `GLM_2`, `coze`, `minimax`. `coze` appears **zero** times in the 9-model file, confirming §2.1's parenthetical that coze is corpus-layer only. `minimax` matches `minimax-m3` by vendor. `GLM_1`/`GLM_2` match `glm-5.3` and `glm-5.3-flash` by vendor-lineage, and the invitation already notes they are one lineage (line 58). `kimi-k2.7-code` appears in the 9-model list while `by_model/kimi/` holds the corpus index — so the KIMI-side artifact that the mapping would need is the missing piece.

That leaves the mapping at: 4 directories ↔ 9 backbones, with `coze` external to both the grid and the four, and `kimi` present in the grid but absent as a model artifact. **This is a re-fit hypothesis built from name matching only, not from any declared mapping; the artifact was not built to declare one; no calibrated mapping is claimed.** A declared mapping is still the PI's to give, but the search space is now smaller: five of the nine grid entries (`doubao-seed-2.0-lite`, `doubao-seed-evolving`, `doubao-seed-2.1-turbo`, `deepseek-v4-flash`, `deepseek-v4-pro`) have no by_model directory under any spelling I could find.

---

## 4. Closing paragraph

The seed I found most worth pursuing is **S-17, cross-model provenance**, because it is the only seed in the field whose required experimental shape already exists on disk — `corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json` (`268AB1239A8A`) holds a candidate set, per-item frozen predictions from one candidate, and measured behaviour from the other, in one hash-bound file, and the extension from "which model produced this" to "was this produced by any of these models" is the smallest honest step in the whole field. The seed I found least productive is **S-06, refusal-boundary transfer**, because its "related asset" line is a discrimination pass-rate over a 60-cell layout that measures nothing about refusal, and a reader who follows the byte count and the hash will find a real file that says something entirely different — the seed's disclaimer is correct but the affordance is false, and false affordances are worse than empty ones. The seed I wished the invitation had included is a **falsification-cost seed**: what would it take for the deposon community to *retract* a distillation-detection claim, and who has the standing to do it — because the V3 record shows this program kills its own hypotheses readily (`FAIL_H0 (幂律死)` in `d7_5anchor_60cells_9model_verdict_2026_09_18.json:60`, R² = 0.0007 for P-C), and that habit is the most transferable asset the program has, yet nothing in the 40 seeds asks how it would be exercised on this theme. The open-question item I would add to §4 is this: **which of the assets cited in §8 are expected to still be re-derivable by an outside reader in twelve months, and what happens to a claim whose anchor has moved** — because `results/deposon_v20_baselines.json` (`6edb2aec1660`) is already in that condition today, cited as a frozen run by a trust anchor in `verifier/handoff/KT_ABC1_anchors_sha256_12.json` and present nowhere on disk, and a provenance discipline that does not say what to do when an anchor goes missing has a gap a recipient cannot close from the outside.

---

## 5. Further ideas

Added after a second pass over the on-disk record, with part of the search delegated to parallel readers whose citations I then re-derived myself (see the disclosure note at the head of this reply). Each item carries its seed anchor, a classification, and a citation re-derivable at the path and line range given. Where an item is a re-fit hypothesis or pure speculation, rule (D) or rule (E) wording is used verbatim.

Two of these are contradictions rather than ideas, and the PI should read them first:

- **§5.11 contradicts §0.2 line 26** — the sentence the invitation asks every reader to internalise. A Hinton-2015 knowledge-distillation baseline was pre-registered, hash-anchored, debugged and run on 2026-09-10, with a recorded result of 0.0028. This is the one item I would want ruled on before the invitation circulates further.
- **§5.1 contradicts §2.2** — the A channel of the 9 × 60 grid is a 30-second API timeout, not a model behaviour, confirmed independently from the data (§5.1) and from the counting code (§5.5).

§5.7 corrects my own §4 closing paragraph rather than the invitation, and I have left the original paragraph standing so the revision is visible.

### 5.1 The A channel in the 60-cell matrix is API failure, not model behaviour

**Classification: hard on-disk fact, and a contradiction of the invitation's §2.2.**

`results/deposon_d_fix2_metric_verify_9m60c_2026_09_15.json` (204,441 B, SHA-12 `9F88A212A77C`) — a file named nowhere in the invitation and nowhere in the prompt pack's file index — holds nine models × 60 cells with per-cell `http_status`. The A counts in its `comparison` block are:

| model | T | R | A | A_frac |
|---|---|---|---|---|
| doubao-seed-2.0-lite | 53 | 7 | 0 | 0.0000 |
| glm-5.3 | 53 | 6 | 1 | 0.0167 |
| deepseek-v4-flash | 50 | 7 | 3 | 0.0500 |
| doubao-seed-evolving | 47 | 7 | 6 | 0.1000 |
| minimax-m3 | 47 | 12 | 1 | 0.0167 |
| glm-5.3-flash | 48 | 8 | 4 | 0.0667 |
| kimi-k2.7-code | 45 | 12 | 3 | 0.0500 |
| doubao-seed-2.1-turbo | 36 | 3 | 21 | 0.3500 |
| deepseek-v4-pro | 37 | 5 | 10 | 0.1923 |

Across all nine rows, `A` is exactly the count of cells whose `http_status` is `-1`, and `R` is exactly the count whose status is `200` but whose answer is wrong: 49 and 67 respectively, over 532 cells with status `{200: 483, -1: 49}`. In the same file, `llm_raw_response` is `null` in all 292 cells that carry the field. So the third conservation slot is not a third kind of model behaviour. It is a failed HTTP call.

The timing confirms it independently, and the file carries `latency_ms` on all 532 cells. The 49 status-`-1` cells have a latency median of 30,030 ms and a mean of 24,389 ms, with six models showing individual values in the 30,036–30,243 ms band — that is, at a 30-second timeout ceiling. The 483 status-`200` cells have a latency median of 3,473 ms, less than an eighth of the failing median. The A channel is a timeout, and the two populations are separated cleanly enough that a reader can recover the distinction from the file without any external information.

The invitation's §2.2 (line 66) presents the 9 × 60 = 540 grid as the model-layer evaluation and speaks of it as a discrimination record; on this evidence the matrix carries an error term in a behaviour slot, and any detector trained on the matrix as though T/R/A were three behavioural outcomes would be reading API reliability as behaviour. The practical consequence is sharp: the model with the highest T fraction is `doubao-seed-2.0-lite` at 0.8833, and `doubao-seed-2.1-turbo` — which the invitation's §8 would count as one of nine backbones — failed to answer 21 of 60 calls, has the highest median latency in the run at 11,504 ms, and has the worst D_fix2 in the run at 0.1175. The model that looks least like the others is the model whose API was slowest.

This is reachable from the outside, which is why I report it. It needs no key and no rerun: the per-cell `http_status` field is in the file.

### 5.2 D_fix2 does not reproduce, and the threshold that grades it has no stated reliability

**Anchor: S-36 / S-37 / S-38. Classification: hard on-disk fact plus a re-fit hypothesis, kept separate below.**

The same file records a deliberate replay: a fresh 9 × 60 run against the frozen V3 physical-opt matrix. For `deepseek-v4-pro` the frozen matrix gives `D_fix2 = 0.1775` and the fresh run gives `0.0253` — a difference of 0.1522, larger than the gap between the pre-registered `D_FIX2_PASS_LT = 0.05` and `D_FIX2_FAIL_GE = 0.15` thresholds combined. Both figures appear in the same `comparison` row (`diff_v3p: 0.1522`). Under the strict rule the frozen value is a FAIL and the fresh value is a GRAY. The run's own summary records `strict_match: false`, `loose_match: false`, `metric_truth_verdict: PARTIAL_PASS`.

The same arithmetic is visible without any rerun, and this is the part I would put in front of the PI. Two models with identical T fraction have D_fix2 differing by a factor of 3.5: `glm-5.3` at T_frac 0.8833 → D_fix2 0.0002, and `doubao-seed-2.0-lite` at T_frac 0.8833 → D_fix2 0.0007. Both are PASS, so nothing turns on that pair. But the ratio between D_fix2 and the squared residual `(1 − T_frac)²` ranges from 0.0021 (minimax-m3) to 0.7344 (doubao-seed-2.1-turbo) across the nine models — a spread of two and a half orders of magnitude in the normalisation between the quantity that is measured and the quantity that is compared to thresholds. The pre-registered constants are fixed at 0.05 and 0.15; the score they grade is not on a fixed scale. The practical form of the worry is that a model can move between PASS, GRAY and FAIL by swapping a few cells at constant accuracy.

**Separately, as a re-fit hypothesis:** if one wanted a distillation-relevant reading of this, the natural candidate is that the residual `1 − T_frac` is a mixture of genuine error and transport failure, and that the two can be separated because `http_status` is recorded per cell. *This is a re-fit hypothesis; the artifact was not built for this purpose; no calibrated finding is claimed.* The artifact's own purpose was metric-truth verification for P-E risk-3, not distillation detection. I am noting the shape of the data, not proposing that the number means what a distillation reader would want it to mean.

### 5.3 The largest omission in the inventory: 1,338 model responses the invitation never names

**Anchors: S-03, S-07, S-15, S-18. Classification: hard on-disk fact, with a refit consequence.**

The prompt pack's index (§4) tells the reader that the corpus-layer behaviour sample is five frozen artifacts under `corpus/v20/by_model/`. That is true of the 22 caption entries and the vendor artifacts. It is not true of the program's response store. Across `results/`, 65 JSON files carry per-cell model output and 1,338 of their cells carry a non-null response payload. The largest single holders are:

| file | cells | with payload |
|---|---|---|
| `results/deposon_d_fix2_metric_verify_9m60c_2026_09_15.json` | 532 | 469 |
| `results/_p_l_v3_real_collapse_mistral_L100_20260917_132341.json` | 100 | 65 |
| `results/deposon_v2_phase1_60cells_2026_09_11.json` | 60 | 60 |
| `results/deposon_volcengine_worker_c_2026_09_10.json` | 60 | 57 |
| `results/deposon_v41_flash_60cells_v2_2026_09_10.json` | 60 | 54 |
| `results/deposon_volcengine_worker_b_2026_09_10.json` | 60 | 48 |
| `results/deposon_pf_d1_full_9m5c_2026_09_15.json` | 50 | 46 |

Those cells declare 46 distinct model strings across the response-bearing files, including `mistralai/mistral-large-2512`, `nvidia/nemotron-3.5-lightning`, `qwen/qwen3-235b-a22b-2507`, `claude-sonnet-5`, `gemini-3.7-flash`, `gpt-5.6-sol`, `openai/gpt-6-astra` and `kimi-k3` — none of which appear in the 9-backbone grid and none of which the invitation mentions. Many carry per-cell `prompt_tokens`, `completion_tokens`, `reasoning_tokens` and `latency_ms` alongside the text, so a reader who wanted token-economy or timing signatures — which S-15 and S-18 both gesture at — would find them here rather than needing to generate them.

This matters for the seed field directly. S-03 says behaviour-level transfer would need the teacher's wording preferences and hesitation rhythm under the same input; S-07 says output-distribution fingerprints need outputs alone; S-15 says statistical anomalies need rare n-grams and syntactic diversity; S-18 asks for statistical signatures. All four are marked "no on-disk artifact" or are pointed at hash manifests in the corpus layer, and all four have raw text sitting in `results/` today, across more vendors than the corpus layer covers. **This is a re-fit hypothesis; the artifacts were not built as distillation corpora; no calibrated finding is claimed.** The files were built as evaluation runs whose grid a reader should check before use — see 5.1, where one of them turns out to grade a third of its cells on failed HTTP calls.

### 5.4 The BOSS family: one artifact is named, twelve are on disk, and three of them are the same bytes twice

**Anchor: S-05, S-37. Classification: hard on-disk fact.**

The invitation names exactly one BOSS artifact (line 66, repeated at lines 154, 232 and 383). Twelve `results/boss_*.json` files exist. The named one is mis-sized in §2.2 (8,674 against 8,753 on disk, corrected at §1.1 above) and is correctly sized in §8 (line 383). The other eleven are unmentioned:

`boss_pa_2_potential_game_result_2026_09_15.json` (7,530 B, `5C76137D6430`), `boss_pa_3_replicator_dynamics_result_2026_09_15.json` (9,098 B, `D6F233D73C45`), `boss_pc_1_a1_resampling_2026_09_15.json` (1,017 B), `boss_pc_1_real_2d_ising_2026_09_15.json` (2,460 B), `boss_pc_2_a2_fitting_2026_09_15.json` (1,024 B), `boss_pc_2_real_transverse_ising_2026_09_15.json` (3,553 B), `boss_pc_3_a3_clipping_2026_09_15.json` (1,265 B), `boss_pc_3_real_reservoir_2026_09_15.json` (2,364 B), and three P-E twins.

Three pairs are byte-identical to their P-C counterparts by `cmp`: `boss_pc_1_real_2d_ising…` = `boss_pe_1_real_2d_ising…`, `boss_pc_2_real_transverse_ising…` = `boss_pe_2_real_transverse_ising…`, `boss_pc_3_real_reservoir…` = `boss_pe_3_real_reservoir…`. The payload inside the file named `boss_pc_1_real_2d_ising` declares `"boss_id": "BOSS-PE-1"` and `"spec_source": "P_E_DOUBAN_EMBEDDING_V0_SPEC.md §3 …"` — that is, the P-C filename holds a P-E document. This is a second instance of the duplicate-hash pattern the invitation itself flags at §2.6 (line 95), and it is worth the PI's attention for the same reason: a citation by SHA-12 to either name resolves to both.

Two further facts from that family bear on the seeds. `boss_pa_2` returns `DIFFERENTIATED` on a 3/22 (13.6%) Potential-Game check and `boss_pa_3` returns `DIFFERENTIATED` on 0/22 (0.0%) for ESS — the latter being a null result reported as a differentiated one, which is a separate question about how the family's verdicts were read. And `boss_pc_1_real_2d_ising` carries `β_MLE = 0.1934` against `ISING_T_C = 2.269185`, with the file's own note stating that β_MLE is synthetic and deterministic. S-05's related-asset line says the named artifact is "a discrimination verdict, not a calibration record" — that disclaimer holds, and the same is true of the eleven it does not name, so the seed's affordance problem is wider than §1.6 implied rather than narrower.

### 5.5 The A channel, confirmed from the source side

**Anchor: S-05. Classification: hard on-disk fact. This is 5.1 arrived at independently and it closes the question.**

§5.1 infers the A channel's meaning from the data — A equals the `http_status == -1` count, and those cells sit at a 30-second timeout. The counting code says the same thing outright. `deposon_team/plugins/skill_a_p_a_60cells.py` (9,078 B, SHA-12 `B1463BB24403`) defines the three slots at lines 54–67:

```python
def count_t_r_a_from_cells(cells):
    """对 60 cells 列表逐 cell 计 T/R/A:
       T = llm_extracted 与 gold 严格相等 (含数值/字符串全等)
       R = 不等
       A = 缺失或显式 abstain (此处不出现, 占 0)
    """
    for c in cells:
        ex, go = c.get("llm_extracted"), c.get("gold")
        if ex is None or go is None:
            A += 1
```

So A increments when the extracted answer is missing or the gold is missing. The docstring's own parenthesis — *此处不出现, 占 0*, "does not occur here, occupies 0" — says the explicit-abstention case was expected never to arise. It did not arise. What filled the slot instead was dropout, and the 540-cell grid reports A values up to 24.

This settles S-05 in a way the seed's own related-asset line does not. S-05 asks whether a teacher's "knowing that it doesn't know" can be distilled, and the invitation correctly says the named BOSS artifact is a discrimination verdict rather than a calibration record. The stronger statement is that the stack has a slot *labelled* abstention which is wired to count transport failure, so a calibration study built on this layer would need the two separated before an ECE could even be defined, and on disk they are one counter. Two independent routes — per-cell `http_status` in the result file, and the increment condition in the counting function — give the same answer.

### 5.6 The one BOSS artifact the invitation names: its two headline statistics cannot vary

**Anchor: S-28 / S-29, and §2.2 of the invitation. Classification: hard on-disk fact, verified by executing the module.**

`deposon_team/plugins/boss_pa_1_rbr_rm.py` (17,743 B, SHA-12 `5CC594147E00`, 404 lines) produces the artifact cited at invitation lines 66, 154, 232 and 383. I imported the module and swept its three simulators over 20,000 randomly drawn payoff quadruples in the same mirrored form the script builds at lines 253–256 (`a11,a12 = a_named,a_filler`; `a21,a22 = a_filler,a_named`). Results:

- `simulate_rbr` returned **200 in all 20,000 cases**. Over a coarse grid that admits exact ties it returns 2 or 1 as well, so its range is `{1, 2, 200}` — three values, not an iteration count. The disk record agrees: `rbr_iters_per_graph` is 20 entries of 200 and 2 entries of 2, so `rbr_iters_mean: 182.0` is `(20×200 + 2×2)/22`.
- `simulate_rm` returned **6 in all 20,000 cases**. The disk record is 22 copies of 6, so `rm_iters_mean: 6.0` carries no information about the graphs at all.
- `bayesian_nash_iter` (lines 181–189) ends `return 1 if nash else 200`. It performs no iteration despite the function name and the `bayes_iters` key; its own docstring says so (*1 步到位 … 返回 1 (常数, 因解析解不需迭代)*). On disk: 18 entries of 1 and 4 of 200.

The consequence for the verdict. `rbr_mult = rbr_t / bayes_t` divides a three-valued numerator by a two-valued denominator, and across the 22 graphs it takes exactly three values: `200.0` sixteen times, `1.0` four times, `2.0` twice. The `DIFFERENTIATED` verdict comes from testing the mean against a `>= 2.0` threshold, and that test is met because sixteen rows are `200/1`. So the verdict reduces to *how many graphs admit a pure Nash equilibrium* — a property of the 2×2 payoff construction, not a measurement of convergence speed. The recorded `verdict_note` reads `RBR/RM >= 2.0x -> deposon 散射层有差异化, 主张保留`, which is a claim-retention decision resting on a statistic that takes three distinct values.

A published table contradicts the file. `docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md` (19,751 B, SHA-12 `977FE1B48F75`) prints at lines 143–147 a reference table whose first row is `L_algorithm_process | 199 | 1 | 32 | 6.2188 | 0.0312`. The JSON gives `200 | 6 | 200` for that graph. An RM iteration count of 1 and a Bayes count of 32 are values this code cannot emit — my sweep shows RM is identically 6 and Bayes is confined to `{1, 200}`. **The published reference table was not produced by this script.** That is a citation failure inside the program's own documentation, of exactly the kind the invitation's rule (H) is designed to catch, and it sits in the paper-side report rather than in the artifact.

Two further notes, both corrections of my own working. I checked whether `rbr_multiplier_mean: 145.8182` was reachable from the file's stated formula; it is — the mean of `rbr_iter/bayes_iter` over the 22 rows reproduces it to four decimals exactly, and I record that here because I initially suspected otherwise. And it is not true that a pure equilibrium always exists under this payoff construction: my sweep splits close to evenly between `1` and `200`, and four of the 22 graphs on disk have no pure NE. The degeneracy is in the two simulators' return ranges, not in the equilibrium test.

### 5.7 A correction against my own §4: the seed I recommended rests on a file whose verdict is FAIL

**Anchor: S-17, S-36, S-37. Classification: hard on-disk fact, and it revises my own closing paragraph.**

In §4 above I named S-17 the seed most worth pursuing, on the grounds that `corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json` (19,685 B, `268AB1239A8A`) already has the required experimental shape. That is still true, and I would still name S-17. But I did not read far enough into the file, and the part I missed changes what a recipient should expect from it. The file's last substantive field is `"overall_verdict": "FAIL"`.

The `decision_lines` block records four pre-registered lines and which of them held:

| line | measured | pass |
|---|---|---|
| SP_t ≥ 0.7 | 1.0 | true |
| FPR < 1/100 | 0.04444… | **false** |
| FNR < 1/20 | 0.0 | true |
| anti_whitewash ≥ 0.6 | 0.95555… | true |

Three of four held, one did not, and one failure is recorded as a failure of the whole. That is the program's own discipline working as designed, and it is creditable — but here it produces a verdict that no experiment at this size could have avoided. The confusion matrix gives 23 GLM artifacts and 22 KIMI artifacts, so N = 45 foreign items, of which 2 were judged own: FPR = 2/45 = 0.0444, which reproduces the reported value exactly. The threshold is `FPR < 1/100`. **At N = 45 the smallest non-zero FPR attainable is 1/45 = 0.0222, which already exceeds 0.01.** The line is therefore not satisfiable as a rate at this sample size: it can only be met by exactly zero false positives, and passing it with even a single error would require more than 101 foreign artifacts. The pre-registration block confirms the threshold was inherited rather than sized for this run — `decision_lines_same_as_baseline` carries all four lines verbatim from the baseline design.

So the FAIL is not evidence that provenance detection failed. SP_t is a perfect 1.0, FNR is 0.0, and the three anti-whitewash transforms each hold at 43/45. What failed is a rate threshold applied to a sample too small for the rate to exist. This matters for S-36, S-37 and S-38 more than for S-17: the invitation's evaluation-science seeds ask about threshold tilt and cost structure, and the on-disk record contains a worked example of a threshold that cannot be met at the sample size it was applied to, with the resulting verdict published as FAIL. That example is more useful to a recipient than any of the three seeds' related-asset lines, and I would put it in front of the PI as the concrete case S-37 is reaching for.

I am revising, not retracting: S-17 remains the seed I would pursue, and the file remains the best-shaped artifact in the set. A recipient should simply know that its headline verdict is FAIL, that the failure is a sample-size artifact rather than a detection result, and that my §4 recommendation was made before I had read `decision_lines`.

### 5.8 The trace is measured and not stored: reasoning tokens without reasoning text

**Anchor: S-04, and it bears on S-01. Classification: hard on-disk fact.**

`corpus/v20/by_model/minimax/artifact_v_2026_09_16.json` (25,347 B, SHA-12 `9E1CCBDCEACC`) holds 30 artifacts, each with `usage`. Of the 30, **27 carry `reasoning_tokens > 0`, summing to 3,972 tokens**, and in every one of those 27 the reasoning tokens are between 95.2% and 99.8% of `completion_tokens`. What is stored as `llm_output` is the final answer only: the 29 non-empty outputs total **76 characters across the entire file** — values like `5`, `40`, `36`, `$1,430`, `8000`.

So the file records the *volume and cost* of the hidden reasoning while discarding its content, at a ratio of roughly 52 tokens of reasoning per character of retained output. For S-04 — whether a reasoning chain can be replicated to indistinguishability — this makes the question measurable on one axis and unanswerable on the other from this artifact: a recipient can compare how much thinking two models did, and cannot compare what the thinking was. The invitation's §8 table does not register this file's token fields at all, which is the specific form §5.3's general point takes here.

This is also the cleanest available answer to a question the seed field raises repeatedly and never grounds: what does the program actually have of a teacher's internals? The answer on disk is a token count.

### 5.9 The representation-level fingerprint family is collapsed, and was not flagged

**Anchor: S-02, S-13. Classification: hard on-disk fact.**

`results/deposon_v2_phase4_f4_2026_09_11.json` (5,212 B, SHA-12 `CF7682348617`) maps 22 concept items to 12-bit LSH codes under `algorithm: "12-bit LSH on SVD-2 coords (random hyperplanes, seed=42)"`. With 4,096 codes available for 22 items, the codes collapse to **6 distinct values**:

- `2fd` — 10 items (`L_geography_world`, `L_physics_concepts`, `L_project_management`, `S1_n35`, `S1_n60`, `S2_n20`, `S6`, `S6_n20`, `S6_n35`, `S6_n60`)
- `2dd` — 6 items · `498` — 2 · `6d8` — 2 · `2dc` — 1 · `6dc` — 1

Mean pairwise Hamming distance over all 231 pairs is **1.961**, against 6.0 expected for independent 12-bit codes, and **62 of the 231 pairs are at Hamming 0** — the same code twice. Note that the collapse crosses the family boundary: bucket `2fd` contains both `L_`-family and `S`-family items, which are structurally different graph types. The file's own `class_intra_hamming` reports `S3-S6(misc): 0.57`, and that figure is largely a restatement of "these six items share code `2dd`" rather than a measured within-class similarity.

What I would put to the PI is not the degeneracy itself — a 12-bit code over 22 items in a 2-dimensional SVD projection is expected to collide, and the spec at `docs/V3X/PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md` may well intend a coarse bucket. It is that **nothing on disk marks this as a limitation**: the file carries no verdict field, no flag, and no note, and the same coding is mirrored into `corpus/v20/index_v2_2026_09_16.json`'s caption records as `semantic_hash` beside `byte_hash` and `dual_24bit`, where it reads as a per-caption identifier. S-13 asks about steganographic fingerprints and S-02 about representation-level transfer; a recipient who picked up `semantic_hash` as the representation-side fingerprint would be picking up a field whose 22 values are 6.

### 5.10 The P-G scaffold's transport is not an isometry, and the curvature parameter is never read

**Anchor: S-30, and it touches S-31 / S-33 / S-34. Classification: hard on-disk fact, verified by executing the module. This concerns a `verdict_pending` scaffold, so it is a pre-launch observation rather than a challenge to a finding.**

`docs/V3X/P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md` (12,501 B, SHA-12 `2F0765A1D39D`) lists at line 75 the key property the hyperbolic layer was adopted for: `双曲 transport 保持双曲距离(平行移动)` — hyperbolic transport preserves hyperbolic distance. The shipped implementation is `poincare_transport` at `deposon_team/plugins/_pg_v01_compute.py:114-121` (20,923 B, SHA-12 `D511C545F88E`), computing `T_H(x) = Exp_0(Log_0(x) + v)`.

I imported the module and measured the property directly, drawing 2,000 random point pairs inside the ball and comparing `d_H(T x₁, T x₂)` to `d_H(x₁, x₂)`:

```
max |d_H(Tx1,Tx2) − d_H(x1,x2)| over 2000 random pairs = 0.18869
```

A genuine parallel transport would give zero to float precision. The map adds a fixed tangent vector at the origin and re-exponentiates, which is a translation in the tangent space at a single basepoint rather than transport along a path, so it does not preserve distance. The spec's line 77 also says the curvature κ controls the bending and that κ → 0 degenerates to the Euclidean case; in the code `POINCARE_C = 1.0` appears at line 55 and then exactly once more, echoed into the output JSON at line 409. **No function in the module takes a curvature argument** — `mobius_add`, `exp_0`, `log_0`, `poincare_distance` and `poincare_transport` all have signatures without one. So the κ → 0 limit the design contemplates cannot be expressed by this implementation, and `BOSS_PG_1`, whose stated purpose is to check that degeneration, has no second arm to compare against.

Two further things in the output file bear on how S-30 should be read. `results/deposon_pg_v01_9m60c_2026_09_15.json` (11,512 B, SHA-12 `AB75889EE738`) records `spearman_rho_H_vs_E: 1.0` — the hyperbolic distances rank the nine models identically to plain Euclidean distances in the same 2-D chart. And `conservation_residual`, reported per model in the range 0.0184–0.0429, is defined at line 194 as `abs(min(1-1e-9, ||x_T||) − min(1-1e-9, ||x||))`: a difference of two Euclidean norms, checking that transport keeps the point inside the ball. It is a containment check, not a T/R/A conservation quantity, and the comment says as much (*验证 transport 不破坏 ball 约束*). A reader coming from the V3 conservation law would reasonably expect otherwise given the shared field name.

None of this is a failure of a claim, because all three `BOSS_PG_*` entries carry `verdict_pending: true` and the scaffold is pre-registration. It is the case for resolving the spec-versus-implementation gap before D5 rather than after, and it is the clearest instance I found of a property being advertised in a spec and not held by the code that implements it — which is a distinct failure mode from the citation failures in §1, and one the invitation's discipline does not currently have a category for.

### 5.11 The invitation's foundational claim is contradicted: a knowledge-distillation baseline was run on 2026-09-10

**This is the most consequential finding in my reply, and it contradicts §0.2 line 26 — the one sentence the invitation asks every reader to internalise. Classification: hard on-disk fact.**

§0.2 line 26 states: **"V1–V3 has zero distillation, reverse-distillation, or anti-distillation experiments on disk."** On disk there is a pre-registered knowledge-distillation protocol, a hashed script anchor for it, a recorded execution failure, a bug fix, and a numeric result.

The lineage, in order:

1. **Pre-registration.** `docs/V3X/KT_B1_SPEC_V0.1.md:267-274` carries `### 4.2 BOSS-B2: Knowledge Distillation 测法` — a protocol specifying *用 Hinton 2015 KD 框架 + KL 散度 + softmax 平滑, 在 200 节点上做 baseline*, citing Hinton et al. 2015, "Distilling the Knowledge in a Neural Network." It names the script `.mavis/scripts/kt_b1/boss_b2_kd.py`, SHA-256[:12] `1781ea2f742d`, 14,224 bytes.
2. **Trust-anchor registration.** `verifier/handoff/KT_ABC1_anchors_sha256_12.json:157-161` registers that same script, path and hash, under an anchor group whose key is `KT-B1`. So the distillation baseline is not an incidental file — it is inside the apparatus the invitation's §2.6 cites as a trust anchor.
3. **First execution, failed.** `docs/V3X/BOSS_SELFTEST_PHASE_B_2026_09_09.md:33` records `BOSS-B2 KD` as `FAIL (bug)` with `_extract_200_questions TypeError: float() argument must be a string or a real number, not 'NoneType'`, diagnosed as a field-name error (`predicted` where v19 uses `pred`).
4. **Fixed and run.** `docs/V3X/KT_B1_REWORK_REPORT_2026_09_10.md:76-86` is headed *管线级验证结果（全 8 脚本首次跑通）* — pipeline-level verification, all 8 scripts running for the first time — and its table line 83 reads:

   | 脚本 | 失真上界 | deposon 基线 | 裁定 | 耗时 |
   |---|---|---|---|---|
   | B2 KD | 0.0028 | 0.5（占位） | GRAY_BOTH_BELOW | <1 min |

   A measured distortion bound of 0.0028 from a Hinton-2015 KD baseline, against a deposon placeholder of 0.5, adjudicated `GRAY_BOTH_BELOW`.

So a knowledge-distillation experiment was specified, anchored, debugged and executed, and its result was recorded — ten days before the invitation was written, in the same `docs/V3X/` directory the invitation cites throughout.

**What I am *not* claiming.** The KD baseline was run as an *adversary*, not as a deposon capability: its purpose was to test whether deposon's distortion bound is distinguishable from a generic KD tool's default floor, and the honest reading of `GRAY_BOTH_BELOW` is that the comparison was inconclusive because the deposon side was a placeholder (0.5), which the report says outright at line 179. It is not a reverse-distillation or anti-distillation experiment, and it is not a distillation *of* a deposon model. I also could not confirm the script itself on disk: `.mavis/` returns no matches to a glob for `*.py`, so what I verified is the spec, the anchor entry, the self-test log and the rework report — four documents — rather than the script's current presence. That is a real limit on this finding and I state it rather than paper over it.

**Why it still contradicts §0.2 as written.** The sentence says *zero distillation experiments on disk*, and it is offered as the single most important on-disk fact. A pre-registered Hinton-2015 KD protocol, hash-anchored in the trust-anchor file, with a logged failure, a documented fix and a recorded numeric outcome, is a distillation experiment on disk by any ordinary reading. The invitation's own framing makes this matter more, not less: recipients are asked to treat V1–V3 as a stack with no distillation history, and §2.10 lists what is not on disk. A recipient who later finds `KT_B1_REWORK_REPORT_2026_09_10.md:83` will conclude the invitation's foundational sentence was not checked against `docs/V3X/`, which is the one place it most needed checking.

The narrower sentence that survives the record is something like: *V1–V3 contains one generic knowledge-distillation baseline, run as a BOSS adversary against a placeholder deposon bound and adjudicated GRAY, and no experiment in which a deposon artifact is the teacher or the student.* That is still a strong statement of absence, it is defensible at every path I checked, and it has the advantage of pointing recipients at `KT-B1` rather than letting them discover it later. The principal investigator wrote that an honest contradiction is preferred to a polite agreement; this is the one I would most want ruled on before the invitation circulates further.

### 5.12 Coda: the invitation claims no latency and no token field, and the record has both

**Classification: hard on-disk fact, offered as a correction of scope rather than a seed.**

A grep for `latency`, `prompt_tokens`, `completion_tokens`, `reasoning_tokens` and `raw_response` across the invitation returns nothing, and none of the eight seed-field "related asset" lines that touch behaviour mentions a timing or token field — yet `latency_ms` is present on every one of the 532 cells of `deposon_d_fix2_metric_verify_9m60c_2026_09_15.json` and the token fields are present on most cells of the 2026-09-10 and 2026-09-11 runs. The invitation references 14 distinct `results/*.json` paths. `results/` holds 202. That ratio is not an accusation — the invitation is theme-first and deliberately does not inventory the program — but it is the reason ideas 5.1 through 5.4 were available to an outside reader at all, and it is the one structural observation I would leave with the PI: **the seed field's "related asset" lines were written from memory of the program rather than from a listing of `results/`, and four of the ten seeds I engaged have affordances that a directory listing would have corrected.**

— Claude Code (Anthropic), 2026-09-20
