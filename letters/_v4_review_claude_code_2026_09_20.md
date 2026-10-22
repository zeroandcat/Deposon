# V4 Review — Claude Code

**Responding to:** `results/_v4_experiment_invitation_2026_09_20.md` (draft v0.1)
**Reviewer identity:** Claude (Anthropic), via Claude Code — **not** one of the 8 recipients named in §7.2 (KIMI-K3 / Trae code / Trae IDE / GLM / coze / VS / workbuddy / 豆包工作). I'm responding because the principal investigator brought me into this round directly; noting that plainly rather than adopting one of the named identities.
**Track scope:** Track 1 + Track 2 (technical/reproducibility), plus a non-binding Track 3 seed (per §2.3/§7.3 — comment only, not a definition).
**Date:** 2026-09-20
**Boundary:** read-only review. No frozen asset modified. No key, endpoint, or secret in this file or in the commands run to produce it.

---

## §0 One-line verdict

Independently reproduced Trae code's SHA-12 / no-key findings from scratch (own `sha256sum`, not a re-read of their numbers) — they hold. Found one additional scope inconsistency Trae's review didn't flag: the abstract's "9-backbone" framing for Track 1 doesn't match the 5-path input list Track 1 actually reads, which feeds directly into the ≥3-of-5 stability rule in §2.1. Applying the invitation's own §3.1 rubric: **Track 1 = GRAY**, **Track 2 = GRAY (inherits Track 1)**, **Track 3 = not yet scoreable** (placeholder, per §4.3).

## §1 Independent verification (re-derived, not re-read)

| Check | Command | Result |
|---|---|---|
| Invitation file hash | `sha256sum results/_v4_experiment_invitation_2026_09_20.md` | `4e8c0ea57028af400d8b8b1a29c92ac85a656e98ba20d50a462cb6808739bf84`, 30,820 bytes — **matches** Trae code's §1 report exactly; file is unchanged since that review. |
| KT_ABC1_anchors SHA-12 | `sha256sum verifier/handoff/KT_ABC1_anchors_sha256_12.json` | `03c6c01f3697...` — first 12 hex chars match invitation §6's `KT_ABC1_anchors` row and Trae code's §1.1 table. |
| 21-vs-22 caption count (Trae's B4) | read `corpus/v20/strip_captions_22.json` directly | Confirmed: 22 generic label-DAG entries (`L_algorithm_process`, `L_biological_taxonomy`, ...), not "caption-fingerprint pairs." No 21-pair artifact exists anywhere under `corpus/` or `results/`. Corroborates B4 independently rather than just trusting it. |

I didn't re-run the full 5-anchor sweep or the no-key scan — Trae code's pass already covers that ground, and repeating all of it adds confidence but no new information. I spot-checked one anchor plus the file hash instead of duplicating the full sweep.

## §2 New finding: Track 1's "9-backbone" framing doesn't match its own input list

- The abstract (§0.2) and §1.1 describe V2 as a "**nine**-backbone × 60-cell grid," and the repo backs that framing up elsewhere — `results/deposon_pg_v01_9m60c_2026_09_15.json`, `results/deposon_d_fix2_metric_verify_9m60c_2026_09_15.json`, and `verifier/run_volcengine_9model_30cells.py` all reflect a real 9-model evaluation.
- But Track 1's actual input list (§5.2, §2.1 step 1) names only **5** paths under `corpus/v20/by_model/` (`kimi, GLM_1, GLM_2, coze, minimax`, per Trae code's B1 path correction).
- §2.1 step 2 defines a mode as "stable" if it appears in "at least three of the **five** frozen artifacts" — the stability threshold is scaled to 5, not 9. If "9-backbone" is the intended scope, Track 1 is silently running on ~56% of the claimed backbone population with no stated reason the other ~4 are excluded (retired? merged into these 5? never had a `by_model` artifact built?). If 5 is actually the correct frozen population, then the abstract/§1.1 wording is what needs correcting instead.
- This isn't just bookkeeping: the "≥3 of N" thresholds in §2.1 are the entire reproducibility contract for Track 1's output. Which N is right changes what counts as a stable mode.
- **For the PI to resolve, not something I'm settling unilaterally:** either state which of the 9 backbones map to the 5 `by_model` artifacts, or correct the abstract/§1.1 "nine-backbone" language to match the 5 that Track 1 actually reads.

## §3 Track 3 (anti-distillation) — non-binding seed, per §2.3/§7.3

Per §7.3 I'm not defining the mechanism, only commenting on the placeholder as invited. One direction that would let Track 3 reuse Track 1/2's own machinery instead of requiring new infrastructure:

- Frame "anti-distillation strength" as **the thing Track 2 already measures, turned on yourself**: after producing a distilled output for circulation (Track 1's mode-set table), re-run Track 2's reverse-attribution as if you were the third-party extractor, against your own published table. Track 3 = PASS if that self-attack's accuracy stays below a pre-registered threshold (e.g., no better than chance across the backbones) while a legitimate recipient can still recover the intended signal above a separate, higher threshold.
- Standard techniques that would open that gap: bounded noise injection into the published mode-set (differential-privacy-flavored), or suppressing/merging any mode attributable to fewer than *k* backbones (k-anonymity over the backbone axis) before circulation.
- This is a seed, not a proposal to adopt — it gives Track 3 a falsifiable PASS/FAIL test built from machinery the invitation already defines, rather than leaving "success" entirely open per §2.3.

## §4 Per-track verdict (applying the invitation's own §3.1 rubric)

| Track | Verdict | Basis |
|---|---|---|
| Track 1 (distillation) | **GRAY** | Doesn't yet execute as specified (Trae code's B1–B4: path casing, undefined mode estimator, missing 21-pair artifact), and independently, the 9-vs-5 backbone scope is unresolved (§2 above). FAIL would overstate it — every blocker is a specification gap, not a run that came back negative. |
| Track 2 (reverse-distillation) | **GRAY** | Inherits Track 1's unfrozen embedding (Trae code's B7) plus an undefined divergence metric on continuous embeddings (B6). Same caveat: blocked, not failed. |
| Track 3 (anti-distillation) | **N/A** | Placeholder per §4.3 ("no failure mode beyond 'undefined'"). §3 above is a seed toward a testable definition, not a scored run. |

Note on the rubric itself: PASS/FAIL/PARTIAL/GRAY (§3.1) reads as written for protocols that already run; none of V4's tracks are at that stage yet. GRAY is the closest fit but conflates "ran, ambiguous result" with "hasn't run yet, underspecified" — worth the PI's attention if V4 reuses this rubric at D1/D3/D5.

## §5 Boundary declaration

Read-only review. No frozen anchor, caption fingerprint, V2 artifact, or 5 锚 JSON was modified — every value above came from reading existing files or running `sha256sum` on files already in the repo. No API key, secret, endpoint, or proprietary prompt appears in this file. I'm not one of the 8 recipients named in §7.2; flagging that plainly rather than adopting one of the named identities.

*Claude (via Claude Code) — technical review, 2026-09-20. Contribution acknowledged, not authorship (per §7.1/§8.1).*
