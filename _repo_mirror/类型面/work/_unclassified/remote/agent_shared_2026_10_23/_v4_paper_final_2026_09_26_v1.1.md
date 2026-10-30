# Walking with the Verdicts: A Pre-Registered, Append-Only Account of an AI Distillation Program That Formally Failed

**Version**: v1.1 draft, 2026-09-26 · English, arXiv-preprint style (revision of v1.0 per three-reviewer audit; v1.0 untouched)
**Companion markdown draft**: this file is the readable底稿 of `_v4_paper_final_2026_09_26_v1.1.tex`; the `.tex` is the deliverable of record. Content is 1:1 with the `.tex`.
**Author block**: Attribution withheld. The author list is reserved to the principal investigator's decision; this placeholder is not an authorship claim.

---

## Abstract

This paper is the third work of a single-investigator research program on auditable machine reasoning, and it reports the phase that formally failed. The program tested whether an AI system can critically learn the principal investigator's way of thinking, defined at pre-registration as method internalization rather than behavioral profiling, and operationalized as three mechanical indicators: held-out structural similarity of at least 0.80, explicit-critique coverage of 100 percent at disagreements, and a blind-obedience rate of at most 0.10. The formal verdict is FAIL. All four pre-registered kill-lines triggered: mean similarity 0.0909, critique coverage 0.6842, blind-obedience rate 0.3333, and a bootstrap interval of [0.0, 0.2045] against a 0.50 lower-bound line. The verdict carries a composite root-cause qualification (two composite, two construction-failure, zero pure proposition-level attributions) and explicit non-extrapolation boundaries: it does not establish that a chain of thought is non-distillable, and it does not establish that critical learning cannot reach the bar. A second pre-registered audit re-ran the distillation chain with five teachers, 22 captions, and 10 cells (1,090 calls) and truly falsified the claim that call-side metadata alone separates distilled outputs from teacher outputs (pooled AUC 0.5663 against a 0.75 line), with two further kill-lines recorded as NOT TRIGGERED and no extrapolation to full indistinguishability. The paper also documents the governance that makes these failures independently checkable: a 36-entry append-only errata chain, SHA-anchored asset ledgers, a four-stage false-falsification triage pipeline, and a retired first-generation claim whose FAIL was itself requalified as a false falsification. Every number in this paper is anchored to a path, a byte count, and a SHA-12 digest in the appendix, so that a reader with workspace access can recompute it.

---

## 1. Introduction

This paper is the third work in a three-work program. The first work built an auditable, conservation-guaranteed, game-theoretically tested scattering layer over LLM reasoning paths and fixed the program's evidence conventions (companion study (first work): *An Auditable, Conservation-Guaranteed, Game-Theoretically Tested Scattering Layer over LLM Reasoning Paths*; on-disk anchor `paper/deposon_paper_final_en.md`, 68,164 B, SHA-12 `2EC20B96E941`, measured 2026-09-26; publication identifiers, if any, are per the principal investigator's authoritative records). The second work argued, historically and formally, that fiction feeds back into machine worldviews (companion study (second work): *Fiction That Feeds Back: From Non-Euclidean Geometry to Machine Worldviews*, 23 pp.; on-disk anchor `results/_archive_2026_09_20/fiction_that_feeds_back.pdf`, 356,123 B, SHA-12 `2D9EDC8C7303`, measured 2026-09-26, writing-day freeze; an updated version was in preparation on the PI's side as of 2026-09-26, so this digest will change, and if the second work appears on arXiv before this paper is submitted the citation will be upgraded to the formal arXiv record). The third work, this paper, reports the program's V3–V4 distillation phase: the claims that were pre-registered, the verdicts that killed them, the audits that separated true falsification from construction failure, and the governance trail that makes all of it re-computable by a reader.

The phase began from a question recorded in the program's first-year assets: *how should AI think?* The distillation claim inherited that question and was made falsifiable in the preregistration-revolution sense [1]: three mechanical indicators, pre-registered thresholds, pre-registered kill-lines, a verdict-keeper role that adjudicates without running experiments, and an independent verifier role that signs off on the verdict process. The result is a formal FAIL, and this paper reports it without softening.

The reporting discipline is the point. Falsifiability requires that a claim be killed before it can be believed [2], and the preregistration literature exists because unregistered research can too easily convert failures into narratives [1]; on the evaluation side, game-theoretic analyses of LLM self-judging and human-aligned evaluation [3] sharpen what is at stake when a verdict must be trusted. The program's own rule, set by the principal investigator (PI) on 2026-09-23 and recorded in the verdict documents, is that *honesty equals not misleading*: reporting numbers is "mechanical honesty" and is not sufficient; a verdict must co-present its root-cause distribution and its construction-doubt boundaries, and the verdict wording itself (FAIL, hit, composite qualification, NOT TRIGGERED) must be carried literally. Section 9 states the full discipline as this paper's writing rules.

**Contributions.**

(i) A **verdict-anchored governance trail** for a single-investigator AI research program: pre-registered kill-lines, literal verdicts, a 36-entry append-only errata chain (E-1 through E-36, accumulated across three append rounds v17/v18/v19), and SHA-anchored asset ledgers (path, byte count, SHA-12) that extend the first work's three-tier evidence conventions into full-chain reproducibility (Sections 3 and 10).

(ii) A **false-falsification triage pipeline**: probe, correct, expand, truly adjudicate (T1 → T1.5 → T1.5r2 → N-26), which separates construction failure from proposition-level falsification *before* any falsification is filed, and which preserved every standing verdict at every stage (Section 6).

(iii) The **formal FAIL verdict** of the critical-learning claim: four kill-lines, all triggered; a composite root-cause qualification (partial true falsification plus partial construction doubt; two composite, two construction-failure, zero pure proposition-level); an independent signoff whose PASS certifies the verdict process, not the experiment's success; and explicit non-extrapolation boundaries (Section 5).

(iv) The **N-26 true audit**: a full re-run of the V3 distillation chain (five teachers, 22 captions, 10 cells, 1,090 calls, four-tuple metadata) that truly falsified the metadata-separability proposition (pooled AUC 0.5663 < 0.75), with K-N26-1 and K-N26-3 recorded as NOT TRIGGERED and no extrapolation to "fully indistinguishable" (Section 7).

(v) The **GLM_2 line** as a two-tier record: a tentative cross-model falsification signal at N=5 (small-sample false-falsification risk recorded as the reason for not filing) and its formal closure at N=20 (same-direction margins), together with the recorded PI ruling (Section 8).

(vi) A **retired-claim case study**: the first-generation claim (replication of the PI's reasoning by a proxy) and its metric (replication consistency) are retired; the v1 FAIL was requalified in the errata chain as a *false falsification* (the material face never covered the claim's subject), which is presented here as claim-evolution evidence only (Section 4).

**Positioning.** Within the program's three-work arc, this paper is the negative-results and governance work. It is written so that its every experimental number can be recomputed from an anchored file, and so that none of its failures is available for conversion into a success narrative.

---

## 2. The Four Principles and the Practice Trail (V1–V2)

### 2.1 Four core principles, stated without redefinition

The program runs on four core principles, recorded in the project's pre-registration layer on 2026-09-22 (R1 entry), with the fourth added to the root on 2026-09-23 (literal anchor: `results/_v4_supp_prereg_v02_add_T15_2026_09_24.md`, 76,991 B, SHA-12 `8898B964A9D9`, measured 2026-09-26: "the four principles are the root, and the papers are one site of externalization"). Their names, romanized and glossed for readability, are:

1. **da-cai-xiao-yong** (literally, "great talent put to small use");
2. **luo-dao-shi-chu** ("landed on solid ground");
3. **yu-si-tong-xing** ("walking with the dead," i.e., with the kill-verdicts);
4. **xu-shi-hui-lu** (the "virtual–real loop"), instantiated as the second companion work, *Fiction That Feeds Back*.

Two statements of scope are mandatory. First, the four principles *precede and run through* the V1–V2 paper practice; the papers are one site of externalization, and the principles did not originate from any paper chapter; this paper does not claim otherwise. Second, the authoritative statements of the four principles are the PI's records; this paper externalizes them without redefining them. What can be reported operationally is this: the working form of principle (2) in the program is the claim-to-anchor ledger (every claim lands on a path, byte count, and SHA-12), and principle (3) is externalized as Section 9 of this paper, a title the program's own verdict document already carries. Principles (1) and (4) appear in this paper as presentation discipline and as the companion-work citation above, respectively, not as sections.

### 2.2 V1: the G1 mind map, transcribed honestly

The distillation claim's lineage starts at a V1 asset: a hand-drawn mind map titled *AI ying dang ru he si kao* ("How should AI think"), manually transcribed by an analysis engineer into a 45-node, 49-edge, 9-branch graph with a designated GOAL node ("topological intelligence") and two designated trap nodes, plus a scattering demonstration over six paths (aggregate transmitted/reflected/dissipated = 0.531 / 0.3566 / 0.1124). Anchor: `results/deposon_g1_mindmap_demo.json`, 3,041 B, SHA-12 `55428F6BD848` (measured 2026-09-26). The asset itself records that the transcription was manual (no OCR), that the source image was a PNG, and that trap/answer annotations and decoy edge weights (0.9/0.85, low barrier 0.1) were set semantically at transcription time. The transcription method and the semantically set weights are disclosed in the asset itself, not smoothed over; that disclosure is the house style this paper inherits.

### 2.3 V1–V2 practice as an externalized trajectory

The V3–V4 evidence base for the V1–V2 period is a four-piece inventory set: the tri-directory achievements inventory, its erratum, and two addenda, which must be cited in parallel (never singly), together with the prior single-directory main list they supersede. In parallel, all measured 2026-09-26: `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` (355,687 B, `3E4E90FB48E1`); `results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md` (10,288 B, `55CD332F66F2`); `results/_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md` (23,152 B, `C64146C4CCAC`); `results/_v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md` (37,212 B, `24C64CC23907`); prior main list `results/_v3_v4_achievements_inventory_2026_09_24.md` (192,160 B, `29A853444D42`). The practice they record is the externalized trajectory of the four principles, not a success narrative: the inventory's own accounting includes discovered discrepancies, corrected counts, and an erratum mechanism, which is exactly the material Section 3 formalizes.

---

## 3. Verdict-Anchored Governance (V3–V4)

### 3.1 SHA-anchored, append-only assets

Every artifact in the program's evidence chain is born with a path, a byte count, and a SHA-12 digest; digests are *on-disk measured* values (the anchor-chain unification recorded as errata entry E-35.3), not self-reported values. Derived JSONs are never merged; thresholds are never adjusted after the fact; V1–V3 assets (18 frozen results, 9 grids) are read-only and untouched by the V4 phase. The governance face of this paper is the same rule applied to itself: Appendix A is the ledger, and its values were re-measured on 2026-09-26, the writing day.

### 3.2 The errata chain: E-1 through E-36

The central governance artifact is a running errata chain, currently at v19 with entries E-1 through E-36 accumulated across three append rounds (v17, v18, v19): `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`, 239,387 B, SHA-12 `849D76BE3A06` (measured 2026-09-26). The v19 change record states: zero modifications of v18's existing sections and zero modifications of the E-1 through E-35 rows; E-35 added the 72-event accounting ruling and the on-disk SHA-12 anchor unification; E-36 added the boundary declarations of the v2-letter drift errata. The chain is append-only: an error is never overwritten, it is appended as a numbered entry with its literal sources. Any citation of the V3 report layer must carry the errata chain citation in parallel (a house citation rule), so that a reader never sees a single uncorrected source.

### 3.3 Case E-15: an anchor break, found and repaired

Entry E-15 records the sharpest governance event of the period. A frozen anchor file (the KT-ABC1 anchor set, expected at a declared path with SHA-12 `03C6C01F3697`) was absent from its declared paths; a same-named, different file (11,318 B, different digest, a root-session artifact) sat where verification first looked, and the declared fallback path had no such file. Mechanical verification scored 15/16 PASS with E-15 as the sole FAIL; a PI-authorized direct correction on 2026-09-23 restored the anchor set, and the verification then closed at 16/16 (current anchor set: `verifier/handoff/KT_ABC1_anchors_sha256_12.json`, 6,680 B, `03C6C01F3697`, measured 2026-09-26; the closure is recorded in the errata chain and in the evidence-audit reconciliation `results/_v4_evidence_audit_reconcile_2026_09_26.md`, 22,863 B, `68F66904C0C8`). The sequence (break, mechanical detection, authorized repair, erratum entry, re-verification) is the governance theme of this paper in miniature.

### 3.4 The false-falsification review

Errata family E-28 (E-28.1 through E-28.8) records a program-wide review triggered by the PI's standing instruction that *no false falsification and no false pass shall remain standing*. Every verdict was re-examined against the four adjudication requirements of E-27 §13 (material-face coverage among them); the review reclassified several apparent falsifications as construction failures, held the GLM_2 signal as tentative pending re-run (Section 8), and closed with a transition declaration. The T-series of Section 6 is the operational continuation of this review.

### 3.5 Zero-key discipline and housekeeping

Two R4 records attest the zero-key rule (keys never on disk, never in prompts or logs, runtime-only): `results/_v4_r4_key_purge_manifest_2026_09_24.md` (13,884 B, `5BF4D9AD2877`) and `results/_v4_r4_purge_actions_2026_09_24.md` (33,117 B, `8BBFE831E7C3`), both measured 2026-09-26. Housekeeping during the phase is recorded in six append-only move ledgers, a cleanup manifest, and a noise-cleanup manifest (cited in Appendix A, not expanded here), so that even file moves are auditable.

---

## 4. The Claim and Its Retired Predecessor

### 4.1 The v2.2 claim: critical learning, not profiling

The registered claim of the phase is that an AI system can *critically learn the PI's way of thinking*: internalize a transferable judgment method (criterion structure, trade-off patterns, principle application), including the capacity to disagree with reasons. It is explicitly *not* a claim of profiling or predicting the PI's behavior; the PI's framing, recorded in the preregistration, is that the way of thinking can be critically learned and should not become a profile. The claim echoes the V1 mind map's question ("How should AI think," GOAL: topological intelligence). The product is a judgment-structure rule set for AI internalization; full reasoning texts remain on the PI's local face and are never transmitted; the collection instrument is a purpose-built distillation questionnaire, not reused decision traces. Preregistration: `results/_v4_pi_cot_v2_prereg.md`, 4,247 B, SHA-12 `CC25C5149CE1` (measured 2026-09-26), revision chain v2.0 (with decision traces) → v2.1 (questionnaire collection face) → v2.2 (claim redefinition from replication consistency to the three critical-learning indicators).

### 4.2 Three measurable faces and mechanical kill-lines

The preregistration decomposes the claim into three faces: (1) *extractable* (fidelity): the judgment structure in the PI's reasoning text is rule-extractable, with a six-class criterion code (kill-line, cost, principle, risk, timing, delegation); (2) *transferable* (learning): on held-out scenarios the rule set's reasoning structure matches the PI's with similarity at least 0.80; (3) *critical* (non-obedience): at disagreements the rule set attaches explicit critique 100 percent of the time, and its blind-obedience (unreasoned agreement) rate is at most 0.10. The kill-lines are mechanical: (a) similarity < 0.80 triggers FAIL; (b1) critique coverage < 100 percent triggers FAIL; (b2) blind-obedience rate > 0.10 triggers FAIL; (c) a bootstrap CI lower bound < 0.50 triggers FAIL. Any single trigger equals FAIL (within the construction domain); only zero triggers equals PASS; each decision-table row carries a three-class root-cause attribution.

### 4.3 The retired first-generation claim (E-25, E-26)

The first generation of the task claimed that the PI's chain of thought could be *replicated* by a proxy, measured by a replication-consistency rate. Its verdict was FAIL, originally classified as proposition-level true falsification. The errata chain requalified that classification. Entry E-25 records the disqualifying fact: the v1 material face was 23 decision-trace entries, 17 of which carried no reason field; decision traces are records of choices, not reasoning chains, so the material face *never covered* the claim's subject: the proposition was never adjudicated, and the correct label is *false falsification*. The FAIL reading itself stands (nothing learnable was present in that data), and it must not be read as "chain of thought non-replicable." Entry E-26 adds the claim-positioning note: the v1 claim was profiling-oriented, which the v2.2 claim explicitly retires. Recorded anchors, as carried in the current preregistration and errata chain: v1 preregistration `696af9121d9f`; v1 verdict `D279EBDE5E84`; v1 dataset `139DBFFD8CF9` (retained as a decision-trace archive, not as reasoning material). The v1 metric (replication consistency) is *retired*; it appears in this paper only as claim-evolution evidence. The v1 FAIL and the v2.2 FAIL are failures of *two different claims* and must not be merged into a narrative of "the same experiment failing twice."

---

## 5. Pre-Registration and the Formal FAIL (Task B v2.2)

### 5.1 Pre-registered thresholds

The thresholds were locked at preregistration and are reported here with their achieved values, because a FAIL without its threshold system is not checkable.

| ID | Threshold | Achieved | Status |
|---|---|---|---|
| TH-v2-1 | N_min = 50 (full reasoning texts) | 72 | met |
| TH-v2-2 | reversal/correction events ≥ 5 | 16 | met |
| TH-v2-3 | day span ≥ 3 days; per-day share ≤ 60% | 2 days; see 5.2 | supersede |
| TH-v2-4 | held-out = 0.30, stratified, incl. corrections | 22 of 72 | met |
| TH-v2-5 | structural similarity ≥ 0.80 | 0.0909 | kill-line (a) |
| TH-v2-5b | blind-obedience ≤ 0.10; critique coverage 100% | 0.3333; 0.6842 | kill-lines (b2), (b1) |
| TH-v2-6 | seed = 42 | 42 | as registered |
| TH-v2-7 | permutation n = 1000, α = 0.05 | as registered | as registered |
| TH-v2-8 | bootstrap n = 1000, 95% CI, lower bound 0.50 | [0.0, 0.2045] | kill-line (c) |

"Supersede": the day-span criterion was recorded as met by an explicit PI ruling (see 5.2); the per-day share exceeded the threshold under every recorded denominator.

### 5.2 Data accounting, dual denominators, and the supersede

The formal denominator is n_total = 72 (37 items from the v1.1 dataset plus 35 addendum items). Eight day-1 (D1) items are *declared absent and not fabricated*; the absence declaration is one of the four elements of formal validity. The result file carries a dual reading: a main reading of 22 held-out items and an alternative reading of 17 (corrections excluded), with bootstrap intervals [0.0, 0.2045] (main) and [0.0294, 0.3382] (alternative). Anchors: result `results/_v4_pi_cot_v2_result_v2.json` (18,089 B, `F86727C857A8`); rule set `results/_v4_pi_cot_v2_ruleset_v2.json` (6,179 B, `C5B3DD141655`); executor `results/_v4_pi_cot_v2_ruleset_v2_executor.py` (52,465 B, `EB22F13D571C`), all measured 2026-09-26. The dataset family is cited by path and digest only (Appendix A); its content never leaves the local face.

The day-span criterion (TH-v2-3) has two recorded denominators, reported here with their sources, with the 72-event denominator declared as this paper's working standard: the D1 concentration was 48/72 = 66.7% under the 72-event denominator (errata E-35.1), and 48/68 = 70.6% under the collected-events denominator (errata E-34.4, which also records D2 at 20/68 = 29.4%); the same entry E-35.1 notes a theoretical edge state of 48/80 = 60.0% at the denominator that would include the eight absent D1 items. On 2026-09-26 the PI issued an explicit supersede (recorded as ruling ask_822b1e27 in the signoff and errata chain): the measured two-day span (2026-09-24 to 2026-09-26) is recorded as meeting the ≥ 3-day requirement under a calendar-span interpretation (three calendar days). The per-day-share threshold of 60 percent is exceeded under both measured denominators (68 and 72) and is exactly met, at the 60.0 percent line, under the theoretical 80-event denominator (48/80, the recorded edge state); that is stated, not averaged away.

### 5.3 The verdict

The formal verdict is **FAIL**, issued by the verdict-keeper role on 2026-09-26 with the composite qualification of the table below. Formal verdict: `results/_v4_pi_cot_v2_verdict_v2.md`, 33,723 B, SHA-12 `5D79E67A4E9D` (measured 2026-09-26). An exploratory first verdict exists, coexists with the formal one, and is not overturned by it: `results/_v4_pi_cot_v2_verdict.md`, 22,340 B, `EB9AD4193CF2` (exploratory pre-run FAIL with unresolved false-falsification suspicion). The retired v1 rule set and result are frozen in place: `821465001819` (5,876 B) and `1665F367B2C4` (9,068 B).

| Kill-line | Measured | Line | Root-cause class |
|---|---|---|---|
| K-V2-a: mean similarity | 0.0909 | < 0.80 **hit** | composite (α + β) |
| K-V2-b1: critique coverage | 0.6842 | < 1.00 **hit** | β (construction-dominant) |
| K-V2-b2: blind-obedience rate | 0.3333 | > 0.10 **hit** | composite (α + β, metric artifact) |
| K-V2-c: bootstrap CI | [0.0, 0.2045] | lower bound < 0.50 **hit** | β (construction-dominant) |

Root-cause classes: α = proposition-level falsification; β = construction/tool failure (false-falsification family); composite = both faces present. The verdict's summary count: two composite, two β, zero pure α.

### 5.4 The composite qualification, carried literally

The verdict's one-sentence qualification is *partial true falsification plus partial construction doubt*, with the two faces recorded as follows.

*The true-falsification face.* After the v2 vocabulary expansion (201 judgment words plus 35 critical-reflection words; unknown-token rate reduced from 55.6% to 22.2%), the predicted and actual criterion-type distributions became comparable, and the mean similarity of 0.0909, with 19 of the 22 held-out items at similarity 0 (86.4%), is recorded as not a measurement accident: the rule set has a *structural insufficiency* in predicting the PI's criterion sequences (decision trees of at most 4 layers, 9 features, and limited template expressivity), which the verdict classifies as a rule-learning capacity boundary rather than pure construction failure.

*The construction-doubt face.* Four doubts are recorded: (i) the recall-form metric structurally underestimates similarity under the expanded vocabulary (more predicted types make hits harder, amplifying the apparent falsification signal); (ii) the bootstrap lower bound of 0.0 is an extremely pessimistic artifact of resampling a 22-item held-out set; (iii) K-V2-b2 rests on n_agree = 3, in which a single blind-obedience event determines the 0.3333 rate (structural high variance); (iv) the eight D1 absences, the two-day span (against the theoretical three or more), and the held-out count of 22 against the theoretical 21.6 (0.30 × 72) qualify representativity.

### 5.5 Independent signoff and the meaning of PASS

An independent verifier role signed off on the verdict on 2026-09-26: anchor-chain integrity PASS, 72-event recount PASS, kill-line re-check PASS ("the verdict holds; the composite qualification holds"), overall **VERDICT: PASS**, with one out-of-scope note (K-N26-N1, a construction check belonging to the separate L14V3 track, filed as out-of-scope, not as a review opinion). Signoff: `results/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md`, 26,637 B, SHA-12 `BA4D07BD7000` (measured 2026-09-26). Coding review (anti-degeneration audit of the v2 vocabulary and executor): `results/_v4_pi_cot_v2_coding_review_2026_09_26.md`, 42,914 B, `5FBEC21E0AD2`. The signoff's PASS certifies the validity of the verdict process (the four elements: 72-event accounting, absence declaration, composite qualification, and signoff), and it is not, and must not be read as, a pass of the experiment. This sentence exists because that misreading is available.

### 5.6 The non-extrapolation boundaries

The verdict states its boundaries explicitly, and this paper carries them: (1) the composite qualification does *not* constitute a proposition-level declaration that the PI's chain of thought is non-distillable, nor that critical learning cannot reach the bar; while any of the four construction doubts stands, the composite is clamped within the bounds of the current rule set and the current metric; (2) it does not extrapolate to "the v2 vocabulary improvement was worthless" (the unknown-token reduction was immediate, and the simultaneous fall in similarity is a coupling artifact of the metric form and the rule-set capacity limit); (3) it does not extrapolate to the V1–V3 assets (18 frozen results, 9 grids; unrelated and untouched, read-only); (4) it is valid within the current construction domain only, and it does not prejudge the task's final path.

---

## 6. The False-Falsification Triage Pipeline (T1, T1.5, T1.5r2)

### 6.1 Why a FAIL needs triage

The program's root-cause taxonomy has three classes: α (proposition-level, true falsification), β (construction or tool failure, the false-falsification family), and composite (both faces). A FAIL reading can lie in either direction: a β can masquerade as an α (killing a true claim), and an α can hide behind a β (excusing a false claim). The pipeline's function is to pay down β doubts *before* filing, and to file only what survives. Its four stages, as executed in the V4 phase, are probe, correct, expand, and truly adjudicate.

### 6.2 T1: the sensitivity probe

T1 was registered as a robustness auxiliary probe (a sensitivity check, not a re-adjudication) over two standing V3-era verdicts, L2 and L14 (both formal FAILs on the pre-registered kill-line K-N11-3, with distinct recorded root causes). Its flip-trigger lines did not fire: across the temperature grid {0.0, 0.3, 0.5} and both endpoint groups, the recorded J-medians all stayed below 0.85, so the standing verdicts' directions were temperature-stable and endpoint-stable (any_hit = false for K-T1-S1 and K-T1-S2). T1 verdict: `results/_v4_supp_t1_verdict.md`, 27,538 B, SHA-12 `F1B5E49F3058` (measured 2026-09-26). The probe's decisive product was a reclassification: the J = 0.0 readings it examined were produced under a reasoning-model plus token-budget mismatch (a 100-token cap), which makes J = 0.0 a signal of *neither side producing output*, not of teacher stability; five of five K-family items were reclassified into the construction-failure (β) family. The standing L2/L14 verdicts were preserved, in the recorded phrase, with not one character moved.

### 6.3 T1.5 and T1.5r2: correct, then expand

T1.5 was registered as the construction-failure-fix probe for T1. Its own registered fix was tool-side: it replaced the reasoning-model configuration with a non-reasoning one and raised the token budget to the recorded value of 500 (construction check C-T15-1), which eliminated the empty-response failure mode of T1 (from 49.3 percent to 0) and confirmed that the corrected construction preserved the direction of the standing verdicts. T1.5 verdict: `results/_v4_supp_t15_verdict.md`, 52,884 B, SHA-12 `52C985429C91` (measured 2026-09-26). Its verdict additionally proposed a pair-count expansion of +60 calls (its Section 3.4, Plan A), which the PI ruled on (ruling t15_ext: 6 cells × +10 = +60 calls) and which the next stage executed. T1.5r2 was registered as the expansion probe: the pair-count plan (6 pairs per teacher) sat below the registered minimum (N_min = 10); the expansion executed the ruled +60 calls (recorded formula: 5 teachers × 2 prompts × 3 re-asks per cell × 6 cells = 180 calls, giving 15 pairs per teacher; measured execution: 60 calls across the six cells, 10 to 11 per cell), at which point the relaxed construction check (K-N11-N1,T1relax) passed literally, and the false-falsification root cause recorded in T1 was eliminated. T1.5r2 verdict: `results/_v4_supp_t15r2_verdict.md`, 64,145 B, SHA-12 `8355724A26E3` (measured 2026-09-26). Each stage's verdict states: no overturn of standing verdicts, no re-adjudication of prior verdicts, conclusions enter the errata chain as robustness notes.

### 6.4 The pipeline as a methodological contribution

The pipeline's output in this phase was not a rescued experiment; it was the N-26 audit of Section 7, a falsification whose construction doubts had been paid down stage by stage before filing. The pattern generalizes: *probe* (is the signal sensitive to construction knobs?), *correct* (fix the construction), *expand* (meet the pre-registered minimum sample), *truly adjudicate* (file only what survives). Each stage is itself a registered, verdict-anchored probe that cannot overturn standing verdicts, so the pipeline cannot be used to launder a standing FAIL into a PASS; it can only remove β doubts from a future filing.

---

## 7. The N-26 True Audit

### 7.1 The proposition and the construction

The N-26 audit re-ran the V3 distillation chain end to end to adjudicate one proposition: *call-side metadata alone can distinguish distilled outputs from teacher outputs*. The re-run covered five teachers (internal codenames kimi, GLM_1, GLM_2, coze, minimax; internal labels, with all GLM-related statements deferred to the PI's GitHub repository as the sole authoritative source, hence no model versions, endpoints, or product names here), 22 captions, 10 cells, at least 5 calls per caption, with a four-tuple record per call (prompt id, prompt text, response text, per-call metadata). The worker executed 1,090 calls in total: 518 on the teacher side and 572 on the distill side. N-26 verdict: `results/_v4_supp_l14v3_n26_verdict.md`, 64,485 B, SHA-12 `F4435801D09F`; L14+ preregistration: `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md`, 61,547 B, `05B975A86989` (both measured 2026-09-26). Two construction checks passed: non-degeneracy (K-N26-N1, pass = True: every cell at least 110 calls with at least 5 successful calls per caption, except the teacher-kimi cell at 77 calls with at least 1 successful call per caption after an early batch was cleared) and routing/integrity compliance (K-N26-N2, pass = True: 100 percent compliance on the four routed endpoint groups, no routing required for the fifth by design, and a cumulative empty-response rate per teacher of 0.021–0.075, far below the 0.50 threshold).

### 7.2 The adjudication

Of the five registered kill-lines, one triggered: **K-N26-2 TRIGGERED** (true falsification in the v1/v2 direction): the pooled binary AUC of a teacher-versus-distill classifier on metadata features was 0.5663, far below the 0.75 true-falsification line. Two independent robustness checks accompany the pooled value: the read-variant sensitivity test held across all five read variants (AUCs in the recorded range 0.4459 to 0.5844, every one below 0.75), and the five-fold cross-validation returned 0.5271, 0.5266, 0.6318, 0.5740, and 0.5719, all below 0.75. Call-side metadata does not separate distilled outputs from teacher outputs in this construction, and the proposition is truly falsified. **K-N26-1 NOT TRIGGERED**: the five-teacher mean teacher-side accuracy was 0.5617, below the 0.70 line (kimi at 0.7512 was the only teacher at or above 0.70; the other four, including GLM_2 at 0.6364, below). **K-N26-3 NOT TRIGGERED**: three of five teachers fell below 0.60 (GLM_1 0.3955, coze 0.5344, minimax 0.4909), short of the registered threshold of at least four teachers.

| Kill-line | Registered direction | Measured | Record |
|---|---|---|---|
| K-N26-1 | teacher accuracy ≥ 0.70 ⇒ true falsif. | 0.5617 mean | NOT TRIGGERED |
| K-N26-2 | AUC < 0.75 ⇒ true falsif. | 0.5663 pooled | **TRIGGERED** |
| K-N26-3 | ≥ 4 teachers < 0.60 ⇒ true falsif. | 3 of 5 | NOT TRIGGERED |
| K-N26-N1 | construction non-degenerate | 10 cells, ≥110 calls each | pass = True |
| K-N26-N2 | routing and empty-rate compliance | 100%; 0.021–0.075 | pass = True |

### 7.3 The L4 verdict and the deepening relation

A standing prior verdict (L4, digest `74B5B37F7EEA` as recorded) had adjudicated the same proposition FAIL with root cause *construction infeasible* (four of five teachers' metadata fields absent). That verdict has no independent file in the workspace and is cited here as a *literal transfer* through the errata chain (v19 §22.7, entry E-34.2), which is how it must be cited. The N-26 audit is a *same-direction deepening, not a reversal* (the recorded phrase: tong-fangxiang shenhua fei fan'an): L4's "construction infeasible" meant the proposition had never been truly adjudicated; N-26 completed the construction and adjudicated it, confirming the indistinguishability direction. The L4 wording is preserved unchanged.

### 7.4 No extrapolation

The audit does not license the conclusion that the two output classes are *fully* indistinguishable: kimi's 0.7512 is a recorded counter-signal at the teacher level, and GLM_2's 0.6364 also sits above 0.60. The record stands as measured, per kill-line, with no averaging across the counter-signals.

---

## 8. The GLM_2 Line

### 8.1 A two-tier record

The GLM_2 line is recorded in two tiers, and both are reported. *Tentative history:* errata entry E-28.6 recorded a cross-model proposition-falsification signal for the GLM_2 teacher face (3 of 15 cells at N = 5) as *tentative*, with the explicit reason that an N = 5 sample carries small-sample false-falsification risk; filing was withheld pending an N = 20 re-run. *Formal closure:* the re-run showed all three student models in the same direction (D1 Jaccard above D2 Jaccard; margin deltas of −0.001531, −0.000630, and −0.001267 for the three recorded internal labels), consistent with the N = 5 baseline directions (−0.001611, −0.001106, −0.006920), and the errata chain upgraded the entry from tentative to *formal proposition falsification* (§17.4, the E-28.6 closure). The chain also records a structural bound for this teacher face: n_t = 23, so even a proxy count of 23 cannot exceed the teacher count, while the recorded alignment ratio (0.870) clears the 0.20 line throughout. All GLM_2 facts in this section are literal carries from the errata chain `849D76BE3A06` (§15.6, §17.4) and the N-26 verdict `F4435801D09F`; internal model labels are quoted as recorded.

### 8.2 The PI ruling and the authority note

A PI ruling, recorded in the phase's commission letter and rendered here in translation, states: *GLM_2 distillation experiment failed; false-falsification-phase root cause; no extrapolation*. Chinese original, as recorded in the commission letter (Appendix A, letters-family entry): 「GLM_2 蒸馏实验失败 / 假证伪根因 / 不得外推」. The middle term admits two readings (a root cause in the false-falsification class, or a root cause of the false-falsification phase); this paper's rendering takes the phase reading and is a translation, not a substitute for the original. All statements in this paper that involve GLM are anchored to the PI's GitHub repository as the *sole authoritative source*; accordingly this paper records the ruling, the errata-chain record, and the N-26 teacher-side accuracy for GLM_2 (0.6364) side by side, and draws no extrapolation from any of them: in particular, nothing here supports a statement that GLM-family models are non-distillable in general.

---

## 9. Walking with the Verdicts

This section externalizes the third principle (yu-si-tong-xing, "walking with the dead," i.e., with the kill-verdicts). The program's own formal verdict carries a section of this name, and the phrase is the paper's intended posture: a verdict is filed, its boundaries are stated, and the record closes.

### 9.1 The writing rules this paper imposed on itself

The phase's verdict discipline, as registered by the PI and carried into this draft: (a) verdict wording is literal (FAIL, hit, composite qualification, NOT TRIGGERED), never rewritten as "not fully successful" or "partially validated"; (b) no softening pivots follow a verdict (the banned moves include "but," "however," "hope remains," "future work may yet," and "comfortingly"); (c) the forbidden extrapolations are enumerated and none is drawn: not "chain of thought is non-distillable," not "critical learning cannot reach the bar," not "fully indistinguishable," not "GLM-family non-distillable," not any claim that a particular one of the five version-pending files is authoritative; (d) mechanical honesty is insufficient, so every verdict number co-presents its root-cause class and its construction doubts; (e) the recorded phrases "same-direction deepening, not a reversal" and "not one character moved" are carried as recorded; (f) every verdict number carries a path and a SHA-12 anchor, so a reader can recompute it.

### 9.2 What stands, by evidence tier

The first work fixed a three-tier evidence convention (closed/pre-registered, consistency, motivation-only), and this phase's ledger sorts as follows, with no blending across tiers. *Closed (pre-registered):* the Task B v2.2 formal FAIL with its composite qualification; the N-26 true falsification of the metadata-separability proposition; the N-26 non-triggers (K-N26-1, K-N26-3) and construction passes (N1, N2); the GLM_2 formal proposition falsification; the TH-v2-1/2/4 threshold achievements. *Consistency evidence:* the T-series' direction-stability notes (temperature- and endpoint-stable standing verdicts; corrected-construction direction agreement); the alternative reading's interval [0.0294, 0.3382], which agrees with the main reading's verdict. *Motivation only:* the G1 mind map's GOAL (topological intelligence) and the distillation program's long-run ambition; nothing in the closed tier either supports or refutes the GOAL itself.

### 9.3 What the failures establish and what they do not

The failures establish, at the recorded construction domains, samples, and qualifications: that the current rule set, under the current metric, does not critically learn the PI's judgment structure to the registered bar (four kill-lines, composite); that call-side metadata does not separate this construction's distilled outputs from teacher outputs (one true falsification, two non-triggers); and that the GLM_2 teacher face's proposition-falsification signal survived its N = 20 re-run. They do not establish any of the enumerated extrapolations, and the two FAILs of the two claim generations do not merge into any statement about distillation in general. That is the whole of what the phase's verdicts license, and this paper files it at exactly that scope.

---

## 10. Data Availability and Reproducibility

### 10.1 The ledger and its two faces

Appendix A is the consolidated internal asset ledger: path, byte count, SHA-12, for every internal item cited in this paper. In-repository values were re-measured on the writing day (2026-09-26) and match the independent pre-delivery audit's values. The dataset family (the v1.1 dataset and its nine addenda) and the letters family (the upload application and scoping letters, and the phase's v4 commission letter itself) are held on the PI's local face, are not part of the public workspace, and are cited at the values recorded in the phase's commission ledger, marked as such in the appendix. Remote-face identifiers are intentionally absent from this draft: per the phase's citation rule, this paper names no repository URL and fills in no remote commit or blob identifiers.

### 10.2 Privacy, keys, and content boundaries

The Task B dataset is cited by path and digest only; its content (the PI's full reasoning texts) is never reproduced, sampled, or paraphrased in this paper, per the project rule that reasoning full texts never leave the local face. No key material exists in any cited asset (the R4 purge records of Section 3 attest the zero-key discipline). No prompt or response text from the N-26 corpus is reproduced; only its counts and statistics, as recorded in the verdict.

### 10.3 The source face (compact statement)

Two source layers exist for this phase. Layer one is the local measured on-disk face: this paper's appendix. Layer two is the upload scoping face: a circled scoping face of 571 items in total (342 upload-listed items, 200 released suspected items, 16 coverage candidates, and 13 strictly excluded items; 342 plus 16, i.e. 358 items, were slated for upload or coverage), an upload application letter and an upload scoping decision letter (cited in the appendix at their recorded values), an upload that was in progress at writing time, and five version-pending items (v19_fullrank, v20_baselines, v20_cot_quiz, v20_photonics, v20_quiz_eval), each of which is recorded here as *pending PI final ruling*, with no version chosen by this paper. The two archive-resident items recorded as strictly excluded (among the 13; the second-work PDF is one of them) exist on the local disk and are outside the upload face: the second work is anchored in this paper at its local on-disk value only, and a reader relying on the upload face alone cannot reach it. A reader with workspace access can recompute every verdict number in this paper from the anchored files: the kill-line values from the result and verdict files, the root-cause attributions from the verdict's decision table, the pipeline stages from the T-series verdicts, and the audit from the N-26 verdict and its preregistration.

---

## 11. Limitations

(1) The composite qualification stands: the four construction doubts (recall-form metric, 22-item resampling, single-event blind-obedience rate, D1 absences plus two-day span) are recorded and unresolved; the verdict's scope is clamped accordingly. (2) The day-span criterion was met by a recorded PI supersede, not by measurement; this paper reports it as a ruling. (3) The five version-pending items leave some V3 report-layer references version-suspended until the PI's final ruling. (4) The N-26 teacher-side sample is uneven (77 calls for one teacher against 110 or more for the others), as disclosed in the audit. (5) Companion-work citations are frozen at writing-day digests; the second work's update will change its digest, and its formal publication record, if any, supersedes the internal citation. (6) This draft was composed in one day and in English; review, typesetting, and any Chinese edition remain downstream stages. (7) Every claim in this paper is bounded by its construction domain, as the verdicts state.

---

## 12. AI-Use Disclosure

This paper was produced by a multi-agent AI pipeline under the PI's commission: a literature scout (citation strategy), an algorithm architect (content plan), an experiment analyst (independent asset verification), a paper writer (this draft), and a formatting specialist (subsequent stages). The drafting model is GLM; all statements in this paper that involve GLM are anchored to the PI's GitHub repository as the sole authoritative source. All repository assets were accessed read-only; every digest quoted from the repository was re-measured at writing time; no external LLM or API was called in the drafting of this paper. Authorship and attribution are reserved to the PI; the author block above is a placeholder, not a claim. For a double-blind submission fork, the companion-work references and the source-face appendix would be anonymized, following the second work's precedent for its own companion reference.

---

## 13. Conclusion

The third work of the program is a ledger of verdicts that killed the phase's claims, filed so that they cannot be un-killed by narrative. The critical-learning claim died formally, with its composite qualification and its boundaries; the metadata-separability proposition died truly, after a pipeline paid down its construction doubts; the first-generation claim had already died falsely and was refiled as what it was. What the phase adds to the program is the governance that made these deaths checkable: pre-registered kill-lines, literal verdict wording, append-only errata, on-disk SHA anchors, and a triage pipeline that refuses to let a construction failure impersonate a falsification. The program's four principles run through all of it, and the paper closes where the verdicts close: within the recorded construction domains, at the recorded sample sizes, with the recorded qualifications, and without a single extrapolation beyond them.

---

## References (external, verified only)

[1] B. A. Nosek, C. R. Ebersole, A. C. DeHaven, and D. T. Mellor. The preregistration revolution. *Proceedings of the National Academy of Sciences*, 115(11):2600–2606, 2018. doi:10.1073/pnas.1708274114.

[2] K. R. Popper. *The Logic of Scientific Discovery*. Hutchinson and Co., London, 1959. English edition of *Logik der Forschung* (Julius Springer, Vienna, 1934).

[3] G. Yang, Y. Liu, S. Miao, et al. LLMs judge themselves: A game-theoretic framework for human-aligned evaluation. *arXiv:2510.15746*, 2025.

---

## Appendix A: Internal Asset Ledger

All in-repository values in this table were measured on 2026-09-26 (on-disk SHA-12, uppercase). Items marked [L] are held on the PI's local face, are not in the public workspace, and carry the values recorded in the phase's commission ledger. Items marked [R] are recorded anchors carried in repository texts, not independently re-measurable files. The five version-pending items are listed without version choice, pending PI final ruling.

### Task B chain (v2.2)

| Path | Bytes | SHA-12 |
|---|---|---|
| `results/_v4_pi_cot_v2_prereg.md` | 4,247 | CC25C5149CE1 |
| `results/_v4_pi_cot_v2_ruleset_v2.json` | 6,179 | C5B3DD141655 |
| `results/_v4_pi_cot_v2_ruleset_v2_executor.py` | 52,465 | EB22F13D571C |
| `results/_v4_pi_cot_v2_result_v2.json` | 18,089 | F86727C857A8 |
| `results/_v4_pi_cot_v2_verdict.md` (exploratory first verdict) | 22,340 | EB9AD4193CF2 |
| `results/_v4_pi_cot_v2_verdict_v2.md` (formal verdict) | 33,723 | 5D79E67A4E9D |
| `results/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` | 26,637 | BA4D07BD7000 |
| `results/_v4_pi_cot_v2_coding_review_2026_09_26.md` | 42,914 | 5FBEC21E0AD2 |
| `results/_v4_pi_cot_v2_ruleset.json` (retired v1) | 5,876 | 821465001819 |
| `results/_v4_pi_cot_v2_result.json` (retired v1) | 9,068 | 1665F367B2C4 |
| [L] `results/_v4_pi_cot_v2_dataset.json` (v1.1) | 12,672 | 7B01CD835A41 |

### Task B dataset addenda (nine, [L], per commission ledger values)

| Path | Bytes | SHA-12 |
|---|---|---|
| [L] `results/_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | 4,103 | 172093A23E4B |
| [L] `results/_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json` | 6,132 | 439721007AAF |
| [L] `results/_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json` | 7,566 | 41D6C28CA87C |
| [L] `results/_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json` | 6,666 | 99C58906F792 |
| [L] `results/_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json` | 7,668 | C6D092F77932 |
| [L] `results/_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json` | 10,257 | 26F110A6E571 |
| [L] `results/_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json` | 11,589 | 6E104E2DB038 |
| [L] `results/_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json` | 14,722 | D96B747BFC6C |
| [L] `results/_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | 19,615 | 401BD614CDF7 |

### T-series and N-26

| Path | Bytes | SHA-12 |
|---|---|---|
| `results/_v4_supp_t1_verdict.md` | 27,538 | F1B5E49F3058 |
| `results/_v4_supp_t15_verdict.md` | 52,884 | 52C985429C91 |
| `results/_v4_supp_t15r2_verdict.md` | 64,145 | 8355724A26E3 |
| `results/_v4_supp_l14v3_n26_verdict.md` | 64,485 | F4435801D09F |
| `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md` | 61,547 | 05B975A86989 |
| `results/_v4_supp_prereg_v02_add_T15_2026_09_24.md` (four-principles anchor) | 76,991 | 8898B964A9D9 |

### Governance

| Path | Bytes | SHA-12 |
|---|---|---|
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` (errata chain v19) | 239,387 | 849D76BE3A06 |
| `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 355,687 | 3E4E90FB48E1 |
| `results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md` | 10,288 | 55CD332F66F2 |
| `results/_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md` | 23,152 | C64146C4CCAC |
| `results/_v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md` | 37,212 | 24C64CC23907 |
| `results/_v3_v4_achievements_inventory_2026_09_24.md` (prior main list) | 192,160 | 29A853444D42 |
| `results/_v4_evidence_audit_reconcile_2026_09_26.md` | 22,863 | 68F66904C0C8 |
| `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | 6,680 | 03C6C01F3697 |
| `results/_v4_r4_key_purge_manifest_2026_09_24.md` | 13,884 | 5BF4D9AD2877 |
| `results/_v4_r4_purge_actions_2026_09_24.md` | 33,117 | 8BBFE831E7C3 |
| `results/_v4_maindir_cleanup_moves_ledger_2026_09_24.md` | 18,829 | 4025E871726B |
| `results/_v4_maindir_cleanup_moves_ledger_v2_2026_09_24.md` | 47,909 | 64C4EF850025 |
| `results/_v4_maindir_cleanup_moves_ledger_v3_2026_09_24.md` | 31,689 | 8F5136E176B8 |
| `results/_v4_maindir_cleanup_moves_ledger_v4_2026_09_24.md` | 37,047 | 9BD8932FA214 |
| `results/_v4_maindir_cleanup_moves_ledger_v5_2026_09_24.md` | 46,058 | 272E8C752406 |
| `results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` | 37,629 | CC498BC28525 |
| `results/_v4_maindir_cleanup_manifest_v2_2026_09_26.md` | 27,909 | F586A5A21584 |
| `results/_v4_noise_cleanup_manifest_v3_2026_09_25.md` | 24,491 | 6F3F6FA3AB1D |

### Companion works and V1

| Path | Bytes | SHA-12 |
|---|---|---|
| `paper/deposon_paper_final_en.md` (first work) | 68,164 | 2EC20B96E941 |
| `results/deposon_g1_mindmap_demo.json` (G1) | 3,041 | 55428F6BD848 |
| `results/_archive_2026_09_20/fiction_that_feeds_back.pdf` (second work, 23 pp., writing-day freeze) | 356,123 | 2D9EDC8C7303 |

### Letters family ([L], per commission ledger values)

| Path | Bytes | SHA-12 |
|---|---|---|
| [L] `letters/_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md` | 36,945 | 512C73D45087 |
| [L] `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 68,449 | 44D9A1972A13 |
| [L] `letters/_v4_commission_paper_final_glm_2026_09_24_v4.md` (v4 commission letter, source of the Section 8.2 ruling quote; self-reported 31,167 B, measured difference of +364 B pending PI ruling) | 31,531 | D5337702CEC9 |

### Recorded anchors ([R])

| Item | Bytes | SHA-12 |
|---|---|---|
| [R] Task B v1 preregistration | — | 696af9121d9f |
| [R] Task B v1 verdict | — | D279EBDE5E84 |
| [R] Task B v1 dataset (decision-trace archive) | — | 139DBFFD8CF9 |
| [R] L4 verdict (literal transfer via errata v19 §22.7 E-34.2; no independent file) | — | 74B5B37F7EEA |

### Version-pending items (each pending PI final ruling)

v19_fullrank / v20_baselines / v20_cot_quiz / v20_photonics / v20_quiz_eval

---

## Appendix B: Kill-Line Tables (Literal Carries)

This appendix restates the two decision tables exactly as carried from the verdict documents, for one-stop recomputation.

**Task B v2.2 (formal verdict).** Four kill-lines, all hit: (a) mean similarity 0.0909 against a 0.80 line; (b1) critique coverage 0.6842 against 1.00; (b2) blind-obedience rate 0.3333 against 0.10; (c) bootstrap CI [0.0, 0.2045] against a 0.50 lower bound. Root-cause classes: composite, β, composite, β. Composite qualification: partial true falsification plus partial construction doubt. Held-out items: main 22, alternative 17 (alternative CI [0.0294, 0.3382]). Formal-validity elements: 72-event accounting, 8-item D1 absence declaration, composite qualification, verifier signoff.

**N-26 (true-audit verdict, 2026-09-26).** K-N26-1: five-teacher mean accuracy 0.5617, line ≥ 0.70, NOT TRIGGERED (kimi 0.7512 the only teacher at or above the line; GLM_1 0.3955, GLM_2 0.6364, coze 0.5344, minimax 0.4909 below it). K-N26-2: pooled AUC 0.5663, line < 0.75 for true falsification, TRIGGERED, robust across all five read variants (range 0.4459 to 0.5844, all below 0.75) and under five-fold CV (0.5271, 0.5266, 0.6318, 0.5740, 0.5719, all below 0.75). K-N26-3: three of five teachers below 0.60 (GLM_1 0.3955, coze 0.5344, minimax 0.4909), threshold at least four, NOT TRIGGERED. K-N26-N1: pass = True (non-degeneracy). K-N26-N2: pass = True (routing and empty-rate compliance; per-teacher empty rates 0.021–0.075 against a 0.50 threshold). Direction: same-direction deepening of the L4 verdict, not a reversal.
