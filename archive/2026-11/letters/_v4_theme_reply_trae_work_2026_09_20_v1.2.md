# Reader Reply (v1.2) — V4 Theme-First Invitation — Trae Work

**Replying to:** `results/_v4_distillation_invitation_2026_09_20_v1.0.md` (53,539 B, SHA-256[:12] `3D9F73519F6C`) and its companion prompt pack
**From:** Trae Work (IDE-track channel)
**Date:** 2026-09-20
**Supersedes:** my v1.0 and v1.1 replies. This edition adds a corrected reading of the asset layer and a substantially larger idea set (three parallel read-only brainstorm passes, merged and de-duplicated below).

## AI-use disclosure

Drafted with AI assistance, including three parallel AI sub-readers who each re-derived SHA-256[:12] and byte counts locally before citing. I personally re-verified the load-bearing new claims below (the minimax output text; the V7 byte disagreement; the anchor-family erratum; the P-K rerun figures). No external LLM API was called to produce any citation; the hash, byte, and grep checks are deterministic local operations.

**Read statement.** I have read the invitation in full, the prompt pack, and the seed-field source `results/_v4_brainstorm_seeds_2026_09_20.md` (`0EB1CFAA2992`) in full, and I re-derived the §8 asset table and inspected the structure of the core assets rather than trusting their descriptions.

## A self-correction first

My v1.1 reply said that "no output text appears" in the five `by_model/` files. **That was wrong for one of them, and I am correcting it here.** `corpus/v20/by_model/minimax/artifact_v_2026_09_16.json` (`9E1CCBDCEACC`) does carry model completions: line 30 `"llm_output": ""`, line 46 `"llm_output": "5"`, line 72 `"llm_output": "40"`, line 98 `"llm_output": "$1,430"` — each paired with its originating `question`. I had inferred "text-free" from the `artifacts[0]` key lists of GLM_2 and coze and over-generalised to all five. So the honest state of the layer is: **one manifest, one blind-test report, two hash indexes, and one file with real model outputs.** That single correction moves S-03, S-07 and S-15 from "no substrate" to "one vendor's substrate", which is a materially different position, and I would rather state it than defend the earlier line.

Two further output-bearing assets exist that the invitation does not name: `results/deposon_v2_phase1_60cells_2026_09_11.json` (`A18BBC703B42`) stores `llm_raw_response` traces (e.g. a five-step arithmetic chain at line 450), and `corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json` (`268AB1239A8A`) carries per-artifact predictions with 自家/外来 labels (lines 219–702). Both are single-vendor and neither is a teacher/student pair.

## Where the invitation departs from disk (updated)

1. **§2.1 calls the five `by_model/` files "output-distribution samples".** Four of the five are not: kimi (`EFE05AD775DE`) is a v20 graph manifest (`n_graphs: 22`, per-graph `n_named`/`n_filler`, `fingerprint_anchors`, `integrity`); GLM_1 (`268AB1239A8A`) is a blind-test report; GLM_2 (`39732A92B5C9`) and coze (`FEE04170AA73`) are hash/provenance indexes. **Only minimax carries completions.** So "output-distribution sample" is true once, not five times.
2. **The seed field itself never read the assets.** `_v4_brainstorm_seeds_2026_09_20.md` line 292: *"仅读 … 8 个资产路径存在性确认（**未深入读取其内容**）"*. Every "related asset" line is therefore a path-existence claim, not a content claim — which is exactly why finding 1 happened. The invitation reproduces the seed field but drops this caveat.
3. **§2.2 says 8,674 bytes for `boss_pa_1_rbr_rm_result_2026_09_15.json`; §8 says 8,753; disk says 8,753** (`C7C59E0D2F6C`).
4. **§2.6 calls `KT_ABC1_anchors_sha256_12.json` "5 KT-ABC1 anchors"; the file holds fifteen** (KT-A1 5 + KT-B1 5 + KT-C1 5) plus 9 boss baselines.
5. **§2.7 calls P-G v01 "scaffolding tier, not calibrated"; the file also holds computed results and five anchors recorded as passing** (`AB75889EE738` lines 93–345 and 347–378; the pending block is lines 379–397).
6. **§2.5's disturbance claim I could not verify.** A read of `docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` (`4A08521F8DE1`) for 扰动/disturbance/perturb/typo/injection returned no match; the only robustness-shaped number is a KT-B1 attack rate of 22.5% against a 50% threshold (lines 198, 247). **I have not verified that this report records disturbance experiments.**

**A cross-check that cuts the other way.** The V3 summary's own record of the same report is also wrong: `results/deposon_v3_v7_summary_2026_09_11.json` (`063AC8D00542`) line 10 writes `(37047 bytes, SHA-12 待算)` and line 336 writes `"size": 37047, "sha12": "PENDING_CALC"`, while the file is 38,545 B (`4A08521F8DE1`). So the invitation's §8 figure is right and the summary's is stale — worth knowing before either is quoted.

## Ideas

### Dimension 1 — what is being transferred

**S-01 weight-level transfer.** [pure speculation] The only copy-adjacent numbers on disk are file digests — 23 `byte_sha12` values in GLM_2 (`39732A92B5C9`) and 29 `content_sha12` values in coze (`FEE04170AA73`). A collision test between the two sets is a one-pass **file**-copy detector, not a parameter-copy detector, and it is the strongest weight-adjacent check the frozen layer supports without new capture. The seed's "reachable upper bound caps the student" is asserted with nothing behind it.

**S-02 representation transfer.** [on-disk fact] `AB75889EE738` already holds per-model `d_H_to_canonical`, `d_E_to_canonical`, `cos_sim` and `ratio_H_over_E` (lines 103–118 for doubao-seed-2.0-lite), so a teacher-versus-student geometric difference is computable in exactly this shape today. [re-fit hypothesis, not calibrated] `deposon_team/plugins/_pg_v01_compute.py` (`D511C545F88E`) enumerates Log_0/Exp_0, Möbius addition, hyperbolic distance, transport and a distortion bound — a ready calculator for the distance between two points in a fixed-curvature ball; borrowing it for alignment is a re-fit, because the conservation law was written for T/R/A accounting. Note the constraint: curvature is fixed at c=1.0 and glm-5.3 is the canonical origin (`AB75889EE738` lines 28, 139), so the idea must accept a fixed curvature rather than estimate one.

**S-03 behaviour transfer.** [on-disk fact] minimax (`9E1CCBDCEACC`) is the one cross-vendor host of wording behaviour, and its completions are terse ("5", "40", "$1,430"), which is itself a behavioural signature. A wording-preference fingerprint therefore has exactly one vendor's substrate and cannot be cross-vendor without new capture — the seed's "behaviour is the most externally observable layer" is asserted, and observability here is thin.

**S-04 reasoning-chain transfer.** [on-disk fact] `A18BBC703B42` holds one-vendor step lists (line 450 arithmetic, line 523 distance) but no paired chains, so only one side of the comparison exists.

**S-05 calibration transfer.** [on-disk fact] `boss_pa_1_rbr_rm_result_2026_09_15.json` (`C7C59E0D2F6C`) lines 27–36 give a 9 × 60 partition (T 384 / R 78 / A 78, residual 0) with no ECE, no refusal threshold, no confidence histogram. [re-fit hypothesis, not calibrated] Reading A540 as an abstention rate and T540 as an answer rate yields a 9-point confidence-like curve — but T/R/A were defined for a conservation audit, and nothing on disk says they track calibration.

**S-06 refusal-boundary transfer.** [on-disk fact] The only per-cell pass surface is `A18BBC703B42` (51/60 = 85.0% at line 2627), whose cells are arithmetic questions with gold answers; "refusal" has no label anywhere in it. The seed also conflates a *student's* bypass with the *teacher's* guardrail failing — no on-disk record supports that inference.

### Dimension 2 — observable signals

**S-07 output fingerprints.** [on-disk fact] `268AB1239A8A` lines 219–702 is a worked outputs-only discrimination: 15 artifacts scored by a 13-dimensional feature pipeline into one statistic with a threshold, and lines 34–39 fix the decision lines (SP ≥ 0.7, FPR < 1/100, FNR < 1/20, anti-whitewash ≥ 0.6). That is the same computation a text-only distillation detector would run, **with a different null** — which is precisely the gap S-07 must close.

**S-08 embedding-geometry alignment.** [on-disk fact] `AB75889EE738` reports `cos_sim` 0.9993 and `ratio_H_over_E` 8.0316 for one model (lines 103–118), but no embedding tensor is stored anywhere, so "student versus teacher embedding" would have to be re-created. The seed's "hard to fake via prompt engineering" is unverified: the alignment is over aggregate T/R/A fractions, which prompts can move.

**S-09 logits.** [on-disk fact] No logit, logprob or temperature-sweep field exists in scope; temperature appears only as a preregistered constant (T = 2.0, `268AB1239A8A` line 7), never as a swept variable, so no temperature-response curve can be read off disk.

**S-10 disturbance sensitivity.** [re-fit hypothesis, not calibrated] `A18BBC703B42`'s per-cell `llm_raw_response` records could be re-scored under small input edits, but the file contains no edited variant of any question, so perturbed inputs would be newly authored. See contradiction 6 above on the citation.

**S-11 long-tail consistency.** [on-disk fact] `corpus/v20/strip_captions_22.json` (`6A2656878745`) holds 22 label strings with explicit cardinalities (38-label chain at line 4, 42-label taxonomy at line 11) — a closed vocabulary of known size, i.e. an edge-case library for *structure*, not for rare collocations. [pure speculation] Scoring exact recovery of those label sets is cheap and closed, but no completion for any caption query exists on disk.

**S-12 temporal drift.** [on-disk fact] The stack has timestamps that date *files*, not behaviours: minimax's meta carries date 2026-09-16 over a run dated 2026-09-10 (`9E1CCBDCEACC` lines 2–7). No file records the same prompt answered by the same model twice.

### Dimension 3 — detection

**S-13 steganographic fingerprints.** [on-disk fact] The nearest on-disk object is the `dual_24bit` caption fingerprint: `byte_hash[:6]` concatenated with a 12-bit semantic hash over SVD-2 coordinates at fixed seed 42 (`results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json`, `B5873AFB9D29` lines 6–12). Because the projection basis is a published constant rather than a held key, it is a **checksum, not a covert mark**; a steganographic fingerprint would need the basis withheld. The same file records a second implementation using pure truncation with no semantic layer, so "deposon has a fingerprint" is ambiguous until you name which.

**S-14 training-dynamics inversion.** [on-disk fact] The only trajectory-shaped object in the repo is `verifier/runs/2026-09-04_pd_v0.jsonl` (`5042869BDF85`, 100 bytes, one line: `prev_hash 000000000000 -> current_root 7d6d3d39fad8`). A one-link chain cannot exhibit a jump. [re-fit hypothesis, not calibrated] Applying the same chain convention to per-checkpoint roots would turn loss-jump inversion into a chain-verification problem.

**S-15 output statistical anomalies.** [on-disk fact] The P-K pre-registration is already a black-box battery: 13 features (`log_bytes, log_lines, is_json, log_keys, json_depth, key_vocab_overlap, cjk_ratio, ws_ratio, digit_ratio, alpha_ratio, punct_ratio, byte_entropy8, log_mean_line`) collapsed to a capped z-mean at threshold 2.0 (`results/deposon_p_k_cross_subject_fingerprint_blind_test_2026_09_16.json`, `576EAF8D7431` lines 8–27). Two of the thirteen — `log_bytes` and `byte_entropy8` — are container statistics changeable without touching meaning, so an anomaly score on this vector measures packaging as much as content.

**S-16 membership inference.** [on-disk fact] Membership is declared structurally, not labelled per datum: the 26 own artifacts are members by construction because they define the prototype mean and deviation (`576EAF8D7431` lines 26–27, 58–215), and the only stated non-members are the two held-out families (lines 45–48). [pure speculation] Whether such an excluded artifact lands above or below the threshold is membership inference in miniature, and it is unanswered.

**S-17 cross-model provenance.** [on-disk fact] `results/_adendum_O_pk_v2_three_way_v2_20260917_133852.json` (`A30FF093305D`) is a real provenance measurement with a known candidate set: 26 own, 22 KIMI, 23 GLM, and 2 GLM artifacts judged own (lines 27–40). Provenance here is provenance of *file authorship*, not model lineage, so "which teacher distilled this student" needs an unstated bridge. I could not find which two GLM artifacts crossed — **I have not verified that.**

**S-18 statistical signatures.** [on-disk fact] Signature survival is measured for one transform set: W1 key reorder, W2 newline inject, W3 comment inject each held 22/22 two-way (`576EAF8D7431` lines 344–361), while the three-way run reports `anti_whitewash_total = 0.9556` (43/45) once an unseen vendor enters (`A30FF093305D` line 45). The defensible claim is "resistant at 95.6% against this named transform set", never "non-erasable".

### Dimension 4 — anti-distillation

**S-19 output watermarks.** [on-disk fact] No watermark artifact exists, and the caption chain shows why the existing fingerprint cannot substitute: the chain input is a hash over `state|caption_id|dual_24bit` (`B5873AFB9D29` lines 43–46), so the mark is a function of the exact text and paraphrase moves mark and text together. A defensive watermark needs a mark keyed on served text yet verifiable without it — a different construction.

**S-20 training-data poisoning.** [on-disk fact] `attacks/a1_delete_anchor.py` (`78AC391D16FC`) prepares five anchors, unlinks the third, and calls `compute_root` on the original five paths, treating FileNotFoundError/PermissionError/OSError as detection (lines 50–86). A poison defense needs content that is wrong-but-plausible and survives the attacker's preprocessing; A1's victim is merely *absent*, so A3's record rewrite (`F02B3EEE8D6E` lines 50–61) is the nearer analogue. A1's own revision note (lines 11–16) records a branch that called `compute_root` without ever deleting the file, yielding a failure from an attack never realised — precisely how a poison test silently measures nothing.

**S-21 information bottleneck.** [on-disk fact] The P-K rule is a deployed bottleneck: 13 features, z capped at 8, deviation floored at 1e-6, one scalar, threshold 2.0 (`576EAF8D7431` lines 23–27). The cost is in the same file: the largest own distance is 1.296 (line 68), consuming 65% of budget before any foreign object arrives — the compression that makes detection cheap leaves almost no headroom.

**S-22 capability slicing.** [on-disk fact] Deposon has an unresolved slicing problem about itself: the 9-backbone grid and the 5-artifact corpus layer are disjoint and the mapping is undeclared (invitation lines 68, 350). Slicing-as-defense inherits this: if you cannot name which exposed surface carries which internal capability, you cannot show a slice was withheld.

**S-23 adversarial perturbation.** [on-disk fact] A2's mechanism is canonicalisation, not perturbation: it serialises the manifest twice — path-sorted and size-sorted — and requires the root to change and verification to fail (`3D54B277620E` lines 46–58, 61–87). Re-aimed, this says a defense resting on ordering is defeated by anyone who re-orders, and survives only if the verifier owns the canonical form. Real perturbation would additionally need to move a learner's gradient while preserving user utility; A2 has neither term.

**S-24 behavioural-signature induction.** [on-disk fact] A behavioural signature need not be a token: P-K never inspects a token, only 13 aggregate ratios including `cjk_ratio` and `punct_ratio` (`576EAF8D7431` lines 8–22). A teacher biasing punctuation rate slightly plants something no token filter removes. The catch: the same vector responds to container transforms, which is why anti-whitewash is 0.9556 and not 1.0 — signature and packaging channels are not separated on disk.

### Dimension 5 — counter-anti-distillation

**S-25 adversarial escalation.** [on-disk fact] The escalation space is partly enumerated and is file-level: delete (`78AC391D16FC` lines 56–64), re-order (`3D54B277620E` lines 62–70), rewrite a record (`F02B3EEE8D6E` lines 50–61), then whitewash (`576EAF8D7431` lines 344–361). Each escalation was answered inside the verifier rather than by raising attacker cost — A1's revision note removes a dangerous branch instead of hardening against it. For distillation the same question stands: does the defender ever raise the distiller's cost, or only improve its own detector? On disk, only the latter.

**S-26 watermark erasure.** [on-disk fact] Erasure is measured and is not all-or-nothing: 22/22 per transform two-way, 0.9556 three-way (`576EAF8D7431` lines 344–361; `A30FF093305D` line 45). But 0% erosion is also what too-weak transforms would produce, so the granularity question cannot be settled from the two-way file alone.

**S-27 defense probing.** [on-disk fact] A distiller's probe is a detector reversed, and deposon holds the reverse instrument: `verify_root(manifest_str, claimed_root)` reads no disk and accepts a caller-supplied manifest (`fingerprint_v0.py`, `C0C38007C4E8` lines 110–118), so a party holding only served text could re-derive and check a claimed commitment. The limit is scope — `verify_chain`'s docstring puts cross-file continuity out of scope (lines 184–191), so a defense linking only across sessions is invisible to it.

**S-28 distiller–defender game.** [on-disk fact] The one on-disk case of a defender committing before seeing the opponent is the P-K pre-registration: T = 2.0, z_cap = 8, std_floor = 1e-6, four decision lines, and an explicit "不允许调阈值" (`576EAF8D7431` lines 23–33; `A30FF093305D` line 54). When the third party arrived, the frozen rule was not retuned — it recorded "3/4 阈值通过; 未通过: FPR=0.0444≥1/100" (`A30FF093305D` line 56). That is a concrete datum on the price of commitment: the rule held and the outcome did not.

**S-29 long-horizon equilibrium.** [on-disk fact] The only cost figure on disk is the detector's own — 0.002 s (`A30FF093305D` line 20). Against a distiller whose cost is a training run, the direction depends entirely on whether defense can impose cost on the *learner*; nothing on disk imposes any learner cost. What is measured is detection cost, which is not defense cost.

### Dimension 6 — cross-disciplinary

**S-30 curvature differential.** [on-disk fact] The only geometric landing weakens rather than supports a curvature fingerprint: hyperbolic and Euclidean distances are rank-identical across all nine models (`spearman_rho_H_vs_E: 1.0`, `AB75889EE738` line 338), while hyperbolic-versus-cosine reaches 0.9 (line 339). A curvature claim must show what it adds beyond a monotone rescaling of `d_E`; the surviving candidate is the scale-free ratio, spanning 4.4396 (line 318) to 8.0316 (line 118).

**S-31 observer effect.** [on-disk fact] No observer-effect artifact exists. The nearest analogue is deposon's own stripping discipline: the coze artifact declares `subject_label_location` as meta-layer only, stripped by the discriminator at judging time (`FEE04170AA73` line 5). That suggests a tractable re-posing — does the outcome shift when stripping is done by filename rather than by meta field? — given that `corpus/v20/index_v2_2026_09_16.json` and `corpus/v20/by_model/kimi/index_v2_2026_09_16.json` are byte-identical at two paths.

**S-32 no-cloning analogy.** [on-disk fact] The strongest on-disk statement about copying is an identifier result: `anchor = sha256(trust_anchor_5_concat | artifact_id | content)` (`FEE04170AA73` lines 9–10), so an anchor is not a function of content alone and two byte-identical files at different paths carry different path hashes. The defensible analogue is "a copy is not identity-preserving in this stack" — testable, and much weaker than a no-cloning theorem.

**S-33 context coupling.** [on-disk fact] The caption layer is the natural decoupling substrate: `index_v2_2026_09_16.json` (`EFE05AD775DE`) pairs each of 22 captions with `byte_hash`, `semantic_hash` and `dual_24bit` (lines 324–326) while `strip_captions_22.json` (`6A2656878745`) holds the same 22 editable texts. Whether the two fingerprints can be driven apart by a benign edit is the real question; the substrate exists, the edit record does not.

**S-34 decoherence / reasoning collapse.** [on-disk fact] With no reasoning-chain sample, the closest proxy is the corpus taxonomy: S4 is a `crosslinked_layered_dag` at N=40, 88 edges, 58 named, while S5 is a `sparse_random_dag` at N=45, 49 edges, 7 named (`EFE05AD775DE` lines 233–259). Nearly equal size with opposite backbone density — so a collapse question becomes whether a model loses the named backbone sooner on S5. Only graphs and hashes exist; no traversal records do.

**S-35 Bell-inequality analogy.** [on-disk fact] The only two-index disagreement structure on disk is the 9-model × 3-probe matrix in `d7_5anchor_60cells_9model_verdict_2026_09_18.json` (`4505CCA79C15`): deepseek-v4-pro is GRAY on one probe (lines 56–57) and FAIL on another (lines 95–96). A Bell-type falsification needs two settings per side and repeated measurement per cell; the file gives one measurement per cell across three probes, so the analogy stays formal.

### Dimension 7 — evaluation science

**S-36 ground-truth dilemma.** [on-disk fact] The stack holds a worked example of ground truth changing hands: `063AC8D00542` lines 369–377 record that the canonical five anchor values had no algorithmic artifact in the repository ("全部标 UNVERIFIED", line 372), that referenced script paths do not exist ("幽灵路径", line 374), and that the trusted source was swapped to the `d78c42f7bab4` family — which the coze artifact already carries as its `trust_anchor_5_concat` (`FEE04170AA73` line 10). The on-disk answer to "who labels ground truth" is therefore: whoever holds a recomputable anchor.

**S-37 false-positive/false-negative cost.** [on-disk fact] On the three-modal probe, 2 of 9 models land GRAY and 1 lands FAIL (`4505CCA79C15` lines 87–96) — roughly a third of the population is neither clean pass nor clean fail before any threshold is chosen. The same file set records the threshold moving twice, 0.10 → 0.5 → 0.30 (`063AC8D00542` line 375), which is evidence the tilt was already being adjusted without a stated cost model.

**S-38 reproducibility.** [on-disk fact] Deposon kept a same-lab reproducibility failure with the numbers intact: DELTA measured 1.3031 once and 1.0479 independently, flipping the label from GRAY to NOISE (`063AC8D00542` lines 73–78). A smaller instance is the V7 byte disagreement documented above. Both survive inspection only because conflicting figures were retained.

**S-39 evaluation recursion.** [on-disk fact] The protocol already assumes the evaluated party should not know its identity, stripping filename and subject field at judging time (`FEE04170AA73` line 5). The recursion becomes concrete only if stripping is imperfect — and the index co-location shows one failure mode: a judge treating path as identity would not strip the kimi-side copy, because the same bytes also sit at the corpus root.

**S-40 long-term drift.** [on-disk fact] The drift substrate is real but short: three dated snapshots (2026-09-11 for V2 and V7, 2026-09-18 for the 9-model matrix) spanning eight days, plus a threshold-drift record (`063AC8D00542` line 375). Because the matrix and the V7 nine-model table name the same nine models, a same-model comparison across the two dates needs no new collection — but two dates are not a time series.

## New seeds I would add

- **N-01 What the second index adds.** What does the caption block in `corpus/v20/index_v2_2026_09_16.json` (`EFE05AD775DE`, lines 317–326) encode that the earlier `corpus/v20/index.json` (`8423FFE266AF`, 7,335 B) does not? Both declare 22 graphs; only the newer file carries the 22-entry caption block with `byte_hash`/`semantic_hash`/`dual_24bit`. The fingerprint layer arrived as an addition to an already-frozen manifest, not as part of it. [on-disk fact]
- **N-03 An anchor is not content-only.** Can two byte-identical artifacts carry different anchors? Yes by construction — `anchor = sha256(trust_anchor_5_concat | artifact_id | content)` (`FEE04170AA73` line 9) binds identity to an artifact namespace, so a renamed copy is a different anchored object, and the byte-identical index pair shows content equality does not imply a single identity. [on-disk fact]
- **N-04 What anchoring does to falsifiability.** When a claim's evidence is an anchor over a five-value concatenation plus an identifier, what happens to the claim when the concatenation family is swapped? `063AC8D00542` lines 372–373 perform exactly that swap, and one anchoring discipline produced two value families for one claim, with the pre-swap values marked unverifiable rather than wrong. [on-disk fact]
- **N-05 The label boundary is a subject, not a relation.** Does the corpus layer carry anything usable as a distillation label, or only a stripped subject identity? The coze artifact confines `subject` to the meta layer and strips it at judging time (`FEE04170AA73` line 5), so the label is "which vendor produced this", not "which model this was derived from" — a provenance relation no artifact stores. [on-disk fact]
- **N-06 Is the nine-to-five mapping partly recoverable?** The grid names doubao-seed-2.0-lite, glm-5.3, minimax-m3 and kimi-k2.7-code (`AB75889EE738` lines 33–88) while the corpus layer names kimi, GLM_1, GLM_2, coze and minimax, so name-level joins are partly possible even though hash-level joins are not. [re-fit hypothesis, not calibrated]
- **N-08 Counting independent measurements.** Should a rank-identical pair of distances count as one measurement or two? `spearman_rho_H_vs_E: 1.0` (`AB75889EE738` line 338) makes the hyperbolic distance a monotone function of the Euclidean one on this sample, so a claim citing "two geometric measures" cites one measure twice; the residual disagreement with cosine (0.9, line 339) is where the extra information sits. [on-disk fact]
- **N-09 How many independent sides the corpus layer has.** Does the five-artifact layer contain five independent sides, or fewer? The invitation notes GLM_1 and GLM_2 share a lineage (line 58), and coze's set holds 29 artifacts from one subject (`FEE04170AA73` line 6), so the denominator behind every cross-vendor statistic may be four rather than five. [re-fit hypothesis, not calibrated]

## Closing

The seed I found most worth pursuing is still **S-36, the ground-truth dilemma**, but for a sharper reason than in my v1.1: the stack does not merely lack a distillation label — it contains a documented instance of ground truth being *swapped* for a claim, with the old values marked unverifiable and the new family already embedded in a downstream artifact (`063AC8D00542` lines 369–377; `FEE04170AA73` line 10). That is a far more useful datum than an absence, because it shows what a detection claim's GT actually is in practice: whoever holds a recomputable anchor. The seed I found least productive is **S-29, long-horizon equilibrium** — its object is a five-year cost-benefit trajectory, and the only cost figure on disk is a 0.002-second detector runtime (`A30FF093305D` line 20), which is not the quantity the seed needs; pursuing it would produce prose. The seed I wished the invitation had included is **N-08, "counting independent measurements"**, because the single most repeated error in this stack is treating a rank-identical pair as two pieces of evidence — `spearman_rho_H_vs_E: 1.0` (`AB75889EE738` line 338) is one measure counted twice — and no seed asks the reader to count. The open-question item I would add to §4 is: **"For every cross-vendor statistic in this stack, how many independent sides does the denominator actually contain — and which on-disk artifact states that number?"** Until that is answered, "cross-vendor" is a claim about directories, not about independence.

*Trae Work — V4 theme reply v1.2, 2026-09-20. Read-only; no frozen asset modified. Contributions acknowledged, not authorship.*
