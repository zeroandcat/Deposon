# Reader Reply (v1.1) — V4 Theme-First Invitation — Trae Work

**Replying to:** `results/_v4_distillation_invitation_2026_09_20_v1.0.md` (53,539 B, SHA-256[:12] `3D9F73519F6C`) and its companion prompt pack (`results/_v4_distillation_prompt_pack_2026_09_20_v1.0.md`)
**From:** Trae Work (IDE-track channel)
**Date:** 2026-09-20
**Supersedes:** my v1.0 reply, `results/_v4_theme_reply_trae_work_2026_09_20.md` (deeper seed coverage; same discipline)

## AI-use disclosure

This reply was drafted with AI assistance, and the citations were produced by AI-executed **read-only** local operations (file reads, byte counts, SHA-256 re-derivation, JSON key inspection, line-numbered greps). No external LLM API was called to produce any citation; the hash and byte checks are deterministic local computations. The ideas, critiques, and doubts are AI-drafted on the basis of those reads and are offered for the principal investigator to accept, edit, or discard.

**Read statement.** I have read the invitation in full (all nine sections), the companion prompt pack, and the seed-field source `results/_v4_brainstorm_seeds_2026_09_20.md` (14,994 B, SHA-256[:12] `0EB1CFAA2992`) in full, and I re-derived the §8 asset table and inspected the structure of the core assets rather than trusting their descriptions.

## Where the invitation departs from disk

**1. §2.1 calls the five `by_model/` files "output-distribution samples"; on disk none of them is one.** §2.1 (invitation lines 54–60) gives each of the five a contribution line describing a vendor "output-distribution sample" usable as "one teacher's per-cell output". What is actually in them:

- `corpus/v20/by_model/kimi/index_v2_2026_09_16.json` (`EFE05AD775DE`) is a **v20 graph-corpus manifest**: keys `corpus, generator_version, spec, named_filler_rule, n_graphs, graphs[], captions, fingerprint_anchors, index_v2_meta, integrity, n_captions`, with `"n_graphs": 22` and per-graph records `graph_id, family, structure, N, n_edges, n_named, n_filler, source, target, seed, sha256, file` (that file, lines 1–21).
- `corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json` (`268AB1239A8A`) is a **blind-test report**: keys include `blind_results, glm_predictions, kimi_predictions_frozen_ref, metrics, consistency_checks, overall_verdict`.
- `corpus/v20/by_model/GLM_2/glm_artifact_v_2026_09_16.json` (`39732A92B5C9`), `corpus/v20/by_model/coze/coze_artifact_v_2026_09_16.json` (`FEE04170AA73`) and `corpus/v20/by_model/minimax/artifact_v_2026_09_16.json` (`9E1CCBDCEACC`) are **hash/provenance indexes**: their `artifacts[0]` entries carry only `artifact_id, byte_sha12, n_bytes, origin, slice_rule, source_path, struct_signature, triple_hash` (GLM_2 adds `provenance, token_lines_dropped`; coze instead carries `anchor_sha12, content_sha12, path_sha12, rel_path`). **No output text appears in these entries.**

This bears directly on S-03, S-07, S-15 and S-17, whose "related asset" line names this layer (seeds file lines 24, 52, 104, 116). The honest mitigation — not a rescue — is that each index entry carries a `source_path`; the outputs may live at those targets. I did **not** follow them, so I cannot say whether output text is there.

**2. The seed field itself discloses that its asset attributions were made without reading the assets.** `results/_v4_brainstorm_seeds_2026_09_20.md` line 292 states: *"仅读 1 份 skill 文档头部 + 8 个资产路径存在性确认（**未深入读取其内容**——协作方引用细节需自行二次核对）"*. So every "相关资产" line in the seed field is a **path-existence claim, not a content claim**. This is consistent with finding 1: the seeds were written from an inventory, and the inventory's descriptions do not survive contact with the files. The invitation reproduces the seed field verbatim but does not carry this caveat forward.

**3. §2.2 and §8 give two byte counts for one file.** §2.2 (line 66) writes `boss_pa_1_rbr_rm_result_2026_09_15.json` as **8,674 bytes**; §8 (line 383) writes **8,753**. Disk says **8,753** (SHA-12 `C7C59E0D2F6C`). §2.2 is the typo.

**4. §2.6 describes `KT_ABC1_anchors_sha256_12.json` as "5 KT-ABC1 anchors"; the file holds fifteen anchor records.** `verifier/handoff/KT_ABC1_anchors_sha256_12.json` (6,680 B, `03C6C01F3697`) has `anchors.KT-A1` (5 entries), `anchors.KT-B1` (5) and `anchors.KT-C1` (5), plus a `boss_baselines` block of 9 (that file, lines 13–188). If "5" is meant to denote the five-value `P_A_FROZEN_RUNS` array (line 33–39), the invitation should say so; as written, "5 anchors" undercounts the file's content.

**5. §2.7 calls P-G v01 "scaffolding tier, not calibrated"; the file also contains computed results and five anchors marked as passing.** `results/deposon_pg_v01_9m60c_2026_09_15.json` (`AB75889EE738`) does carry `P_G_3_BOSS_scaffolding` with `status: "SCAFFOLDING (PRE-REGISTRATION, 等 D5 launch)"` and `verdict_pending: true` (lines 379–397) — but it also carries a fully computed 9-model × 60-cell transport block with real per-model `d_H_to_canonical`, `d_E_to_canonical`, `cos_sim` (lines 93–345), and `P_G_5_anchors_v01_real` where each of five anchors has a real `sha12` and a `"verdict": "PASS"` (lines 347–378). "Scaffolding, not calibrated" describes the BOSS sub-block, not the file.

## Seed engagement

### S-08 / S-30 / S-02 — geometry, and a statistic that is 1.0 by construction

**Critique.** S-08's "why interesting" says geometric alignment "难靠 prompt 工程伪造" (seeds line 57). But the one geometric number on disk that looks like a correlation is degenerate. `deposon_pg_v01_9m60c_2026_09_15.json` line 338 records `"spearman_rho_H_vs_E": 1.0`. Reading the per-model pairs (lines 114–115, 139–140, 164–165, 189–190, 214–215, 239–240, 264–265, 289–290, 314–315): `d_H_to_canonical` = 0.0, 0.2675, 0.6519, 0.7955, 0.9075, 1.1981, 1.5726, 1.9127, 2.2003 and `d_E_to_canonical` = 0.0, 0.0333, 0.1054, 0.1375, 0.1667, 0.2427, 0.2868, 0.4014, 0.4956 — the second sequence is strictly increasing in the first, so the rank orders are identical and Spearman is exactly 1.0 regardless of any geometric content. A seed that borrows this frame inherits a number that cannot distinguish geometry from ordering. The companion figure `spearman_rho_H_vs_cos: 0.9` (line 339) is *not* 1.0 and is therefore the only one of the two that carries information. [on-disk fact + critique]

**Doubt.** I cannot tell from this file alone whether the near-monotonicity is a property of the 9 models or of how the two distances are defined from the same `(T_frac, A_frac)` pair; the PI must rule.

### S-11 — "18 anchors + 22 captions" as an edge-case library

**Evidence.** `corpus/v20/strip_captions_22.json` (`6A2656878745`) parses to **22** array entries, each with `id, text, family, structure, n_labels` (e.g. `L_algorithm_process`, 38 labels; `L_biological_taxonomy`, family `L`, `structure: llm_generated_dag`). These are **structured label graphs**, i.e. the corpus's node/edge vocabulary, not a long-tail *fact* set. [on-disk fact]

**Critique.** S-11's asset line (seeds line 76) calls this an "边角案例库" for long-tail consistency. A graph corpus of 22 domain taxonomies is a plausible edge-case library for *structure*, but "long-tail fact" and "rare collocation" (S-11's own wording) are different objects. [critique]

### S-17 — cross-model provenance

**Evidence.** Of the five cited artifacts, exactly one contains model-produced content: `corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json` (`268AB1239A8A`) holds `glm_predictions`, `kimi_predictions_frozen_ref`, `metrics` and `overall_verdict` — a genuine "which producer said what, and did the judge agree" record. [on-disk fact]

**Idea.** That is the closest thing on disk to a known-candidate attribution substrate, which is what S-17 wants. But it is a **discrimination** record (producer vs. judge agreement), not an attribution of a *student* to a *teacher*. Borrowing it for provenance is a re-fit hypothesis; the artifact was not built for this purpose; no calibrated finding is claimed. [re-fit hypothesis, not calibrated]

### S-05 / S-06 / S-37 — calibration, refusal, and cost structure

**Evidence.** `results/boss_pa_1_rbr_rm_result_2026_09_15.json` (`C7C59E0D2F6C`, 8,753 B) records `"n_models": 9` and `"n_540_total": 540` at lines 28–29 — a 9 × 60 discrimination grid of transmit/reflect/absorb counts. `results/deposon_v2_phase1_60cells_2026_09_11.json` (`A18BBC703B42`) records `"v2_60cells_pass_rate": "51/60 = 85.0%"` at line 2627. Neither carries an expected-calibration-error curve, a refusal threshold, or a false-positive/false-negative cost matrix. [on-disk fact]

**Critique.** S-05, S-06 and S-37 each cite these as structurally adjacent (seeds lines 36, 42, 254). "Structurally adjacent" is fair; "related asset" overstates, because the *quantity* the seed needs — calibration error, refusal boundary, cost asymmetry — is not the quantity the artifact stores (a three-way count per model). [critique]

### S-10 — disturbance sensitivity

**Evidence.** `docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` (38,545 B, `4A08521F8DE1`) records disturbance experiments (per invitation §2.5, line 89). I did not read that file's body in this pass, so I state only what the invitation and the seeds file assert, and mark the rest as unverified. **I have not verified this citation.** [doubt]

**Idea.** If the disturbance perturbations are re-applied to a distilled student and to its teacher, "does the student's robustness curve converge to the teacher's" becomes a measurable question with an existing perturbation set. That is a re-fit hypothesis; the perturbations were built for discrimination; no calibrated finding is claimed. [re-fit hypothesis, not calibrated]

### S-14 — training-dynamics inversion

**Critique.** S-14 is the least tractable seed on this stack. Its cited asset, `results/d7_5anchor_60cells_9model_verdict_2026_09_18.json` (2,456 B, `4505CCA79C15`), contains only terminal verdict strings — `"P-C_two_phase": "FAIL_H0 (幂律死)"` (line 60), `"P-F_D_fix2_strict": "8+1+0 (PARTIAL_PASS, A channel timing 敏感)"` (line 99) — with no loss curve, no reward trace, no capability time-series. Deposon stores no training dynamics anywhere (§2.10, line 125). A seed whose object is "the hardest-to-erase archaeological layer" has zero observability here. [on-disk fact + critique]

### S-09 — logits

**Evidence.** Confirmed by absence and by my own inspection: §2.10 (line 124) states no logit-level artifact exists, and nothing in the §8 table contradicts it. I found no logit record. [on-disk fact]

### S-36 — the ground-truth dilemma

**Evidence.** The deposon verdicts are discrimination verdicts over a discrimination task: `results/deposon_v3_v7_summary_2026_09_11.json` (`063AC8D00542`) records, at lines 258–263, terminal strings for P-A / P-B / P-C / P-D / P-E, and `d7_5anchor_60cells_9model_verdict_2026_09_18.json` records the 9-model matrix at lines 21–102. Nothing in either is a distillation label. [on-disk fact]

**Idea.** S-36 is not a downstream nuisance; it is the load-bearing wall. The invitation's §2.3 (line 79) already concedes the GT is "a different problem". What it does not say is that the three candidate labellers in S-36 — teacher, distiller, third-party auditor — are not three ways of writing the same label; they are three *incompatible* labels, because each has a different incentive to call the same output "distilled" or "independent". A detection claim's GT is therefore an *institutional* choice before it is a technical one. [idea]

## Closing

The seed I found most worth pursuing is **S-36, the ground-truth dilemma**, because the stack answers it by absence and that answer reorders the rest: if no cited artifact carries model output text and none carries a distillation label, then the detection seeds (S-07, S-15, S-17, S-18) are blocked on a GT-and-substrate question before they are methods questions — and the seed field's own line 292 admits the assets were never read, so the inventory cannot be used to argue otherwise. The seed I found least productive is **S-14, training-dynamics inversion**: its object has zero observability on this stack (no loss curve, no reward trace anywhere), so pursuing it produces prose rather than evidence. The seed I wished the invitation had included is one about **what the v20 graph-corpus manifest itself encodes** — 22 graphs, 38–42 nodes, a named-vs-filler edge split, `fingerprint_anchors`, an `integrity` block — since that manifest, not an output distribution, is what the "five vendor artifacts" mostly are, and an inquiry into what models *emit* has to start from what the stack actually stores. The open-question item I would add to §4 is: **"Which on-disk artifact, if any, contains model output text — as opposed to hashes, paths, and terminal verdicts — and if none does, which of the 40 seeds are addressable at all without stepping outside the frozen stack?"** Until that is answered, some of the seed field is live and some of it is decoration, and the invitation cannot tell the reader which is which.

*Trae Work — V4 theme reply v1.1, 2026-09-20. Read-only; no frozen asset modified. Contributions acknowledged, not authorship.*
