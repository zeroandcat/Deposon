# Kill-Lines Before Experiments: A Dual-Track, Pre-Registered Negative-Results Report on Game-Theoretic Validation (V3) and Chain-of-Thought Critical Learning (V4) in the Deposon Project

> **Draft status (to be stripped at submission).** Working draft of 2026-10-12, prepared under the project's external-caliber commission line (v0.6 series). Author block, affiliation literals, and submission logistics are withheld pending the PI's final review; this draft contains no author, institution, funding, or acknowledgment identifiers. Target vehicle: arXiv preprint, cs.AI primary classification, no journal template and no designated submission target. All verdict literals, thresholds, counts, and fingerprints are transcribed without modification from the project's sealed on-repo artifacts; every evidence anchor cited in the text is listed with path, sha256[:12], and byte count in Appendix A. Dividing lines marked "DIVERGENCE" report registered unresolved dual readings and are not resolved anywhere in this draft.
> **Version history.** v0.1 (2026-10-12): initial full draft. v0.2 (2026-10-12): §7.5 slots filled from the supplementary literature scan + References additions [R42]–[R53] (the only changes from v0.1; made while the three-way review was reading v0.1, leaving two v0.1 statements stale by design). v0.3 (2026-10-12): all seventeen review items disposed (six medium, nine low, two advisory — including the two stale statements); first-author-grade upgrade pass (self-sufficiency of internal-facing phrasings, full-anchor re-verification to 65 measured, table numbering, notation and language polish). Verdict literals, thresholds, and counts are unchanged throughout; the v0.3 registration fixes are limited to the E19 path correction, the E20 dual-value registration (drift row C-26), the R19 base-literal restoration, the KD gloss in §1, and the N-26 criterion row's literal restoration.

**Authors:** [withheld in this draft — pending PI finalization]

**Subject classes:** cs.AI (primary); cs.GT; cs.CL

---

## Abstract

We report the outcomes and the reporting discipline of two research tracks of the Deposon project: **V3**, the game-theory track (validation of the *deposon* three-channel scattering mechanism for LLM players under pre-registered kill-lines and a distortion-bound specification), and **V4**, the distillation track (critical learning of the project PI's chain of thought — methodology internalization, explicitly not profiling). Both tracks terminated with predominantly negative or blocked verdicts, and we report them at their literal face value: in the V3 judgment set, the five-case GT family closes as 1 FAIL (claim level, kill direction) plus 5 construction-face PASS legs with 0 KD; case #26b is FAIL with root cause registered as fake falsification (criterion face); cases #35 v2 and v3 are FAIL on both legs with fake-falsification attribution; the C5 B-group claim is FAIL (fake falsification, construction/material face); the P-J/P-M/P-C degeneration families all close KD; and the P-B distortion-bound experiment remains blocked in full because a pre-registered theory input (D1) is not in place. In the V4 judgment set, Task B closes FAIL in each of its v1 (exploratory), v2 (formal), and v3 (formal) rounds — 4/4 kill-lines hit at v2, 5/6 at v3 — with root-cause attribution shifting from pure construction failure to composite attribution while the FAIL persists across corrections; the N-26 teacher-metadata study triggers a real-falsification kill-line (pooled AUC 0.5663 < 0.75); the S3 substrate gate closes PASS/PASS/KD; and a six-model cross-control closes 6/6 FAIL, all attributed to construction-layer failure. Beyond the verdicts themselves, the paper's central methodological claim is the **kill-line protocol** that produced them: three-state verdicts (PASS/FAIL/KD) only; thresholds frozen before execution and never amended; a mandatory root-cause triage separating *real falsification* from *fake falsification* (instrument, construction, criterion, or caliber failure) and from mixed causes; bidirectional extrapolation bans (a fake-falsified claim is not written off as dead, and a construction-face PASS is not promoted to the proposition face); dual-read reporting with zero resolution of registered divergences; role separation between line-setting, execution, verdict closure, and evidence audit; and append-only errata. The protocol is exercised on itself in a closing case study: a tool-issued "kill" verdict was forensically attributed to a hash-labeling mislabeling mechanism, classified as fake falsification at the tool face, and re-registered from *killed* to *restored* by root-cause classification rather than by result softening. We argue that this discipline — negative results reported with falsifiable provenance, literal verdicts, and explicit attribution of *why* an experiment failed — is a transferable contribution for LLM-agent research, where unverified positive claims and softened negative claims are both common failure modes.

**Keywords:** negative results; pre-registration; kill-lines; falsifiability; LLM agents; game theory; mechanism validation; chain-of-thought distillation; honest reporting

---

## 1 Introduction

### 1.1 The reporting problem

Empirical research on large-language-model (LLM) agents has a verification problem and a softening problem. The verification problem: claims are frequently not reproducible from inspectable artifacts, and the chain from measurement to conclusion is not auditable after the fact. The softening problem: when an experiment fails, the failure is often reported as "preliminary", as "insufficient evidence", or with hedged connectives ("however, the approach may still..."), which preserves the appearance of a live research program while discarding the information content of the failure — namely, *what exactly failed, at which layer, and with what root cause*.

This paper reports a project that took the opposite position at every joint. The Deposon project pre-registers **kill-lines** (decision thresholds with an explicit FAIL semantics) before execution, freezes them, executes, and closes each case into a sealed three-state verdict — PASS, FAIL, or KD (known defects) — with a mandatory **root-cause triage** that distinguishes *real falsification* (the proposition-level claim is falsified) from *fake falsification* (the instrument, construction, criterion, or caliber failed while the proposition remained untested) and from mixed causes. The project's own formulation of the discipline is "判死不软化" — a kill is not softened — coupled with "诚实的根因是不误导" (the honest root cause does not mislead; mechanical honesty is not sufficient). Two **extrapolation bans** run in both directions: a fake-falsified claim must not be written off as "the proposition is dead", and a construction-face PASS must not be promoted to a claim about the real face.

### 1.2 The two tracks

The project's PI-designated track frame (which we preserve verbatim; the identifiers V1–V4 are track names, not stage numbers of this paper) is: V1 = the mind-map line; V2 = the game-theoretic explanation; V1+V2 = an arXiv preprint (arXiv:2609.09001, v1, no peer-review record — existence registered in §2); **V3 = the game-theory main line**, and **V4 = the distillation main line**. This paper covers V3 and V4.

**V3** asks whether the *deposon* mechanism — a T+R+A three-channel scattering mechanism that replaces Bayesian players with LLM players in a potential-game framework — can be validated under pre-registered distortion bounds: when LLM players replace Bayesian players, does the total distortion D(M,T) fall inside a pre-registered [lower, upper] theoretical bound interval, with a pre-registered kill-line at a distortion multiplier of 2.0×? The theory interface needed to run the bound experiment at all is itself tracked as a first-class object with a readiness state, and we report its blocked status as a result, not as an inconvenience.

**V4** asks whether an AI system can *critically learn* the project PI's way of thinking — extract the criterion structure from the PI's recorded judgment events, transfer it to held-out scenarios, and disagree with the PI with explicit critique rather than blind agreement. The track's pre-registered claim is falsifiable on three measurable faces (structural similarity, critique coverage, blind-obedience rate) with locked thresholds; an earlier "reproduction-consistency" framing is registered as a deprecated profiling-style caliber and does not appear as a claim anywhere in this paper.

### 1.3 What this paper contributes

1. **A dual-track negative-results report with literal verdicts.** Every judgment case is reported at its sealed literal face value — including FAIL, KD, kill-direction, fake-falsification attributions, and blocked states — with the original verdict literals, the pre-registered thresholds, the key readings, the root-cause classification, and the registered dual readings, each anchored to an on-repository artifact identified by path, sha256[:12], and byte count (Appendix A). Registered divergences are reported in pairs and left unresolved (Appendix C).
2. **The kill-line protocol as a transferable methodology.** Section 3 specifies the protocol as a set of eleven institutional rules (three-state verdicts; freeze-before-execute; chronology as a falsifiability element; root-cause triage with a four-element real-falsification test; bidirectional extrapolation bans; no-softening; nature isolation between collection-face and verdict-face lines; role separation; append-only errata; a time-layered verdict vocabulary; external-statement locks embedded in the verdict files themselves).
3. **Honesty discipline exercised on the verdict chain itself.** Section 6 reports the project's fake-verdict case: a tool-issued kill verdict that was itself forensically audited, attributed to a hash-labeling mislabeling mechanism, classified as fake falsification at the tool face, and re-registered from *killed* to *restored*. The case demonstrates that verdicts are falsifiable artifacts and that the protocol's honesty discipline applies to its own outputs.
4. **A reporting posture for LLM-agent research.** Section 8 argues, from the case set, that the epistemically valuable unit of a negative result is the *verdict + root cause + extrapolation boundary* triple, and that root-cause triage is what separates a falsification from a construction failure — a distinction without which both positive and negative LLM-agent claims are unauditable.

### 1.4 What this paper does not claim

Consistent with the protocol's extrapolation bans: no construction-face PASS in this paper is promoted to any proposition-face claim; no fake-falsification FAIL is written off as a dead proposition; the V4 FAILs are construction-domain-limited and support no statement in either direction about whether the PI's chain of thought is distillable; and the N-26 real-falsification trigger supports no "completely indistinguishable" claim (one endpoint's 0.7512 accuracy is co-reported verbatim). The paper makes no claim about any proposition-level question that its sealed verdicts do not decide.

---

## 2 Project lineage, terminology, and reporting caliber

### 2.1 Lineage and prior artifacts (existence registration)

The project's public lineage, registered per the external caliber:

| Artifact | Registration (literal) | Status in this paper |
|---|---|---|
| V1+V2 arXiv preprint | arXiv:2609.09001, **v1 only**; 23 pages / 5 figures; DOI 10.48550/arXiv.2609.09001; CC BY 4.0; **0 peer-review / 0 acceptance record**; code repository github.com/zeroandcat/Deposon (external statements defer to the PI's GitHub as the sole authoritative source) | Cited as an arXiv preprint; its abstract and contents are not reproduced or characterized here (not read for this draft) |
| G1 mind-map anchor | `results/deposon_g1_mindmap_demo.json` · sha256[:12] `55428f6bd848` · 3,041 B — registered as a JSON *anchor* for the G1 "how should an AI think" mind-map; the JSON is explicitly **not** the mind-map body itself | Cited as the anchor that the V4 v2.2 pre-registration itself cites [E60] |
| FTFB (fiction-type prior work) | `results/_archive_2026_09_20/fiction_that_feeds_back.pdf` · `2d9edc8c7303` · 356,123 B · 23 pages (side files `.tex` `d060f75dbe9f` · 93,324 B; `_source.md` `543479649b3e` · 84,388 B) | **Existence registration only.** Per the project's read-before-cite rule the PDF must be read before any content citation; it was not read for this draft, and no statement about its contents is made. A registered divergence between the commission letter's "remote not directly retrievable" and the mirror clone's on-disk presence is reported unresolved in Appendix C |
| Four core principles | The project registers four core principles that **precede and run through** the V1–V2 preprint practice (they are not described as originating in the preprint's chapters) | Framing mention only |

Lineage note: the project's paper-family files in the repository (`paper/deposon_paper_final_en.md` · `2ec20b96e941` · 68,164 B; `paper/references.bib` · `f5a6a850e203` · 14,914 B; `paper/v2/related_work_v2X.md` · `7fb001add973` · 10,114 B) serve this draft as the reusable reference base for §7; their readings and entry lists are transcribed, not re-verified entry-by-entry here (§7.5, §9).

### 2.2 Terminology discipline (as applied in this draft)

- **Track names.** "V3" and "V4" are the PI-designated main-line names, used exactly as registered; they are not version numbers of this paper, and no other stage name is coined.
- **Publication status.** The V1+V2 artifact is described only as an *arXiv preprint* (v1, no peer-review record). Nowhere does this draft use "published", "accepted", or "peer-reviewed" language.
- **Verdict literals.** Verdict literals from the sealed files are quoted as-is (mixed Chinese/English literals are quoted verbatim with a bracketed gloss); translations are marked as glosses. No softening connective is attached to any verdict statement (§3, rule 7).
- **Entity and privacy discipline.** No individual names, institutional names, credentials, internal session identifiers, internal agent rosters, or dataset-internal fields appear anywhere in this draft. Desensitized literals in source files are quoted, never restored. Model/endpoint names appear only as recorded in the verdict artifacts (e.g., the `kimi` endpoint, the `qwen`/`qwen_plan` endpoints, recorded as "qwen_plan (qwen3.7-max token-plan endpoint)"); model identities that could not be verified against the repository record are left to the PI ("以 PI 为准"), never filled from memory.
- **Counts.** Counts are reported with their measurement time points; stale registered counts are cited only as historical-time-point values (Appendix B, §B.3).
- **Verdict vocabulary time layering.** All judgment cases reported in this paper are 2026-10-01 or earlier and are quoted in the original three-state vocabulary (PASS/FAIL/KD). The five-terminal vocabulary introduced by PI ruling on 2026-10-10 (pass / af / kd / fail / give-up) governs later verdict faces and is reported as a protocol evolution in §3 (rule 11); no post-10-01 verdict face is covered in this draft.

### 2.3 Evidence and citation conventions

Every reading in this paper traces to an on-repository artifact cited as **path + sha256[:12] + byte count**, in the compact form [E**nn**] resolved in Appendix A. Provenance is layered: readings were transcribed through a drafting-side verification layer (the project's internal working briefs of 2026-10-12, which measured their anchors at clone HEAD `f44996fbfd9f386299442924f70585bb20d935fc`, 2026-10-12 12:36:59 +0800, matching the registration-time HEAD of the project's upload-side registration inventory — a 461-file register of remote git blob sha1 values); that layer is disclosed for provenance only and is not needed to check this paper, since every reading resolves to the repository artifacts of Appendix A. For this draft itself, 65 anchors were independently re-measured (63 matched; two registered divergences — the E20 runner copy and the S3 backfill rule draft — are co-reported with 0 adjudication; the review-side measurements, taken at a later clone HEAD, are registered in the same way). Two hash domains are kept strictly separate and never interconverted: local sha256[:12] (file content) and remote git blob sha1 (40 hex); where only a remote-registered value exists, it is quoted as a registered value with 0 local recomputation masquerade (e.g., the C4 acceptance register: remote blob sha1 `21ad9581c0ec…`, 33,728 B, transcribed from the registered inventory). Repository paths are given relative to the repository root; `results/` and `docs/` under `_september_workspace/` are the mirror-clone locations corresponding to the registered remote paths.

---

## 3 The kill-line protocol

The protocol below is the project-wide institutional rule set under which every judgment case in §4–§5 was closed. It is stated here as twelve rules, each evidenced by the sealed artifacts (rule-by-rule anchors in Appendix A; formulation transcribed from the protocol's threshold-literal unique source [E22] and the verdict files' self-discipline sections).

**Rule 1 — Three-state verdicts only.** Every branch endpoint of a judgment case terminates in exactly one of PASS / FAIL / KD. No "unclear", "UNVERIFIED", "PARTIAL", or "GRAY" state may serve as a terminal verdict; a registered "unclear" is, by PI ruling, an *expanded* KD and must be co-reported as such.

**Rule 2 — Freeze before execution; effective-locked; no post-freeze amendment.** Kill-lines are pre-registered and frozen *before* the experiment runs; once effective they lock, and after freezing they are not changed. Thresholds (`TH-*`, `K-*`) are never adjusted, replaced, or "improved"; each verdict file verifies `new_thresholds_added = 0` case-by-case (the GT family verdict measures this per case: all zero [E01]).

**Rule 3 — Freeze chronology as a falsifiability element.** The pre-registration's file timestamp must precede the executor's creation timestamp, which must precede the result's timestamp. Example (measured, #35 v2 [E06]): pre-registration 2026-09-28 22:22:11 < executor 2026-09-29 12:17:10 < result 2026-09-29 12:27:24 — the registered literal is "the kill-line was frozen approximately 14 hours before the experiment" (a value derived from the registered timestamps: 13 h 54 min 59 s). Inverted chronology would defeat the pre-registration's evidentiary force.

**Rule 4 — Root-cause triad attached to every verdict row.** Each verdict row carries a root-cause classification: *real falsification* (proposition-face layer), *fake falsification* (failure of the instrument, construction, measurement, criterion, or caliber — with the failure point localized and recomputable), *mixed*, or *unclear*.

**Rule 5 — The four-element test for real falsification.** A FAIL is classified as *real falsification* only if all four elements hold: ① the kill-line was frozen first (effective at the semantic layer); ② the construction is non-identical/non-degenerate; ③ the material face covers what the claim requires; ④ the measurement has discriminative power. Absent any element, the FAIL is not a proposition-level falsification.

**Rule 6 — Bidirectional extrapolation bans.** If the root cause is fake falsification, the failure is written as "instrument/construction failure" and is **not** written as "the proposition is dead". Symmetrically, a construction-face PASS is **not** extrapolated to the real face — and a construction-face FAIL is likewise not converted into any direction of proposition-face conclusion.

**Rule 7 — No softening.** The banned softening vocabulary is explicit: "but / however / there is still hope / not excluded / insufficient evidence / pending further verification / preliminary / roughly"-class connectives are not attached to verdict statements. The registered formulation is that the honest root cause must not mislead — mechanical honesty is not sufficient.

**Rule 8 — Nature isolation.** Collection-face attainment lines (`ok` booleans — did the collection protocol reach its sampling requirements?) are kept out of the FAIL tally; verdict-face hit lines (`hit` booleans — did a criterion fire?) are kept in it. The two are never mixed [E21].

**Rule 9 — Execution ≠ verdict; role separation.** Line-setting (protocol-keeper) → execution (worker) → verdict closure (verdict-keeper) → chain audit (evidence-auditor / verifier) are separated roles. Verdict files run no experiments, modify no data, merge no derived JSON, read no credentials, and impersonate no other role; hashes cited inside a verdict file are measured by the verdicting role itself; a file's self-referential SHA-12 is never self-written (to avoid the self-reference paradox).

**Rule 10 — Append-only errata.** Living documents are corrected by append-only errata notes (original lines untouched). Record files and code products are never retro-edited: history is retained and discrepancies are registered.

**Rule 11 — Time-layered verdict vocabulary.** By PI ruling of 2026-10-10, verdict faces *after* 2026-10-01 use a five-terminal vocabulary — `pass`, `af` (artifact-free), `kd` (known defects), `fail`, `give-up` — with non-five-terminal outcomes counted as hung items rather than verdicts, and an overlap priority `af > kd > give-up`. Verdict faces on or before 2026-10-01 (all cases in this paper) keep their original literals.

**Rule 12 — External-statement locks.** Sealed verdict files embed a *uniquely permitted sentence* plus a forbidden-statements list for external use. When this paper quotes a case's conclusion, it stays inside the permitted sentence; the forbidden lists are reproduced where they bind (e.g., #35 v3's five forbidden statements, §4.4.4). Pairwise co-reporting is mandatory where registered (v2/v3 paired verdicts; GT-5 with GT-5b; GT-4 with the GT-1 leg).

---

## 4 V3: game-theoretic validation of the deposon mechanism

### 4.1 The mechanism and the distortion-bound specification

The V3 main line's registered definition is: the game-theory main line — the deposon mechanism / kill-lines / theory-bound chain (P-A/B/C, #21/C4, GT verification, etc.). The mechanism's core question form (transcribed from the P-B distortion-bound V0 specification [E23]):

> When LLM players replace Bayesian players, does the total distortion D(M,T) of the deposon three-channel scattering mechanism (T+R+A channels) fall inside the interval [theoretical lower bound, theoretical upper bound]? The baseline is the Bayesian player (known mechanism + payoffs ⇒ distortion = 0); the measured object is the LLM player's **distortion multiplier** relative to baseline, D_LLM / D_Bayesian (value ≥ 1).

*Table 1 — the P-B specification's pre-registered, frozen kill-lines [E23]:*

| Line | Literal | Meaning |
|---|---|---|
| H0 (kill) | distortion multiplier ≥ 2.0× | the LLM player introduces 2× distortion; mechanism infeasible |
| H1 (closure) | distortion multiplier ≤ 1.5× | ≤ 50% added distortion; mechanism commercially viable |
| GRAY | 1.5 < multiplier < 2.0, or CI crossing a boundary | specification-literal zone; under Rule 1 no GRAY state serves as a terminal verdict |

The specification anchors itself to five frozen artifacts (pre-registered: any ≥ 1 anchor drift ⇒ the whole V0 is retracted): the ECR baseline (`ecr_median = 1.333`); the GT kill-decision family (10 rulings); five frozen run JSONs; the LLM client; the distortion calculator. The experiment face is 3 mechanisms (M1 = deposon T+R+A three channels; M2 = greedy; M3 = random) × 5 task families × ≈ 33 decisions per task ≈ 500 calls, with output = an N=500 distortion-multiplier table with 95% bootstrap CI, 3×5 mechanism×family sub-tables, and theoretical bound curves [E23].

### 4.2 Theory-interface readiness (three assets, tracked as first-class states)

The distortion-bound experiment cannot run until its theory interface is in place; the project tracks the interface's readiness as a result, not a footnote.

**(a) P-B V0: blocked.** The D1 theory input (the "theoretical optimal response" and "theoretical distortion bound" formulas the spec requires) is not in place ⇒ the whole V0 remains blocked; the status literal is unchanged [E23]. A companion acquisition request [E26] registers what is being requested (u*(a_t) plus the bounds L/U), with three standing prohibitions: no self-authored theory content, no proxy theoretical-bound values, no inferred u*(a_t) expressions; five items are reserved to the PI.

**(b) C4: source corrected, theory still not in place.** The C4 caliber-correction record [E24] registers a three-layer attribution history for the theory bounds' source: the old (now-obsolete) literal ("bounds given by an external theory party"); an intermediate literal (a derivation source adopted by the PI on 2026-09-30); and the current canonical (a codex derivation; the old canonical line is preserved unmodified as historical record). The record's own status boundary is quoted verbatim: **"source changed ≠ theory in place"**. The C4.9 zero-fill discipline remains in force (0 estimated values / 0 substitute values / 0 self-invented formulas); of C4's nine readiness items, the calculator artifact and the five-anchor JSON are not on disk ⇒ nine items not assembled ⇒ C4.9's "not computable + γ" trigger state is maintained; the record's self-registered status is *pending PI review*. An acceptance register (remote blob sha1 `21ad9581c0ec…`, 33,728 B; transcribed from the registered inventory, 0 local read) registers one reply as accepted and a second reply as outside coverage ⇒ the second reply's acceptance status remains not-accepted (the registered face's own literal,「维持『0 已采认』」, is ambiguous as to its referent; the reading here follows the register's structure, in which the first reply is recorded as accepted and the second as outside coverage); an upstream definition item is hung. **DIVERGENCE:** the P-B specification's byte size has three registered readings (15,457 local-registered / 11,189 / 7,126 historical registrations; the mirror-clone copy measures 15,549 B after desensitization) — reported unresolved, 0 adjudication.

**(c) T-1 gate: closed ≠ released.** The T-1 gate is the "materials do not cover the claim" anti-degradation gate for the construction face, defined in the protocol-face threshold-literal unique source [E22] §2.7. Its closure verdict [E21] registers: the baseline gap readings (main reading −19 / alternative reading −13); three gap faces **all closed** (the acceptance conditions were converted to: D1 back-collection fully ingested + D5 continuation fully ingested + recomputation on top); and a per-line kill-line ruling on the recomputed substrate (Table 2).

*Table 2 — T-1 gate closure: per-line rulings [E21] (thresholds quoted verbatim from the pre-registration; 0 recomputation by the verdict role; the worker's dual-implementation cross-recomputation and the caliber-A accounting-domain file are quoted as the computation sources):*

| Line | Criterion literal | Reading | Verdict |
|---|---|---|---|
| K-V3S-3-1 | cross-day ≥ 5 (distinct calendar days) | 7 days (whole-event-domain n_after = 186 caliber) | **PASS** (domain divergence unresolved — Appendix C) |
| K-V3S-3-2 | single-day share ≤ 60% (0 reuse of the old 56.5%) | 0.516129 (96/186) | **PASS** |
| K-V3S-3-3, front | N ≥ 50 | 186 (four readings 186/180/74/77, minimum 74) | **PASS** |
| K-V3S-3-3, back | corrections/reversals ≥ 5 | reading 1 (7+0−6) < 5; the sole blocking face is that the reading authority is not in place (the attainment reading location is the S4 segment; the K-V3S-4 reading face has 0 files on disk) | **KD** |
| K-V3S-3-3, whole line | conjunction | front half cannot lift the whole line, back half cannot press the whole line, no folding into a single FAIL (γ-VK-1: a conjunction cannot be assigned a boolean) | **KD** |
| TH-v2-1 | N_min = 50 | 74 (caliber-A accounting domain) | **PASS** |

Six readings are co-reported (main reading adopted; an alternative reading over the old accounting domain yielding 3 days ⇒ FAIL is *not adopted but reported* — the domain divergence remains undecided, reserved to the PI/protocol layer; an R-β reading with denominator 180 / 6 days / 0.533333 and an R-γ gate-face reading are reported without divergence; an R-RUN reading over the v3 formal lock domain of 77 is KD because its per-day composition has no on-disk registration and is not to be derived; an old-value reading of 56.5% is rejected by the pre-registration's own literal "0 reuse of the old 56.5%") [E21]. Robustness registration: K-V3S-3-1 is domain-sensitive (3 days vs 7 days); K-V3S-3-2 is caliber-insensitive (0.5000–0.5362, all ≤ 0.60); K-V3S-3-3 front is domain-insensitive (74–186). The closure verdict states its own boundary verbatim: **closure ≠ release** — it does not declare the T-1 gate released; release would require (i) a PI-side confirmation separating "gate closed" from "run-ban lifted", (ii) a K-V3S-3-4 lock-freeze file on disk, and (iii) a Q-2 three-caliber registration merge, all outside the verdict file's authority and evidence base.

### 4.3 The V3 judgment set at a glance

*Table 3 — sealed verdicts (all original literals; all faces on or before 2026-10-01):*

| Case | Sealed verdict (literal face) | Root cause (registered) | Anchor |
|---|---|---|---|
| GT family (5 cases) | 1 FAIL (gt5: claim level, kill direction) + 5 legs PASS (gt6 / gt8 / gt5b / GT-4 / GT-1 leg — all construction-face only) + 0 KD | gt5: ③ mixed (sole new judgment) | [E01][E02][E03] |
| #26b (K-V3R-26 literal-gap) | file-level FAIL (tier 3: original annotation maintained) | fake falsification (criterion face / caliber face) | [E04][E05] |
| #35 v2 (GT2b field immunity, expanded matrix) | α-leg FAIL / β-leg FAIL / composite claim FAIL (paired registration, no conjunction masking) | fake falsification (α: C0+C1+C3; β: C0+C2+C4; composite: C0 on both legs) | [E06][E07] |
| #35 v3 (C0 collinearity correction, A-case 2 full cross) | claim-level FAIL | fake falsification ×3 (α leg, β leg, composite) | [E08][E09][E10] |
| C5 B group (SVD-3 coordinate collapse, post-fix re-run) | K-V3DF-0-1 FAIL; 0-2 / 5-1 / 5-2 / 5-3 / 9-1/9-2/9-3 PASS; claim total FAIL | fake falsification ×2 (construction / material face) | [E12][E13] |
| P-J / P-M / P-C degeneration families | all three families KD; face level 8 faces = KD 4 + PASS 4; 19 lines = PASS 12 + FAIL 1 + KD 6 | P-J: fake falsification; P-M: fake falsification; P-C: not computable ⇒ KD | [E14][E15] |
| #32 CPATH (with-RAG live rerun) | not a three-state verdict face: a supplementary live-run registration file | not applicable | [E16][E17][E18] |
| Fake-verdict case | tool-issued kill re-registered as **restored** (已复原) per PI ruling | fake falsification (tool face: hash-label mislabeling mechanism) | [E27]–[E31] |

### 4.4 Case notes

#### 4.4.1 GT family (five cases, one verdict file)

Authorization chain: pre-registration (protocol-keeper) [E02] → executor file (worker) [E03] plus eight execution files → verdict file (verdict-keeper) [E01]. Summary table (transcribed): 5 cases = 1 FAIL (gt5, kill direction) + 5 legs PASS (gt6, gt8, gt5b, GT-4, GT-1 — all covering the construction face only) + 0 KD.

- **gt5 — FAIL.** Original verdict literal: `inconclusive_preregistered_undefined_band`; sealed verdict: FAIL (claim level, kill direction; A-leg PASS / B-leg FAIL); root cause ③ mixed — the sole new judgment in the family. Key readings: material-face coverage 4/22 = 18.2% (the construction face contains 4 graphs: S6, L_physics_concepts, L_biological_taxonomy, L_algorithm_process, out of a 22-graph corpus; the other 18 graphs were not judged and the pre-registration's §9 bans extrapolation); the B-leg literal is a universal proposition ("all graphs"); the four gap values are mutually distinct and the sign criterion is 4/4 self-consistent; of three violations, two have tiny magnitudes — `L_algorithm_process` −0.00077 is 1/397.7 of `S6` −0.30659 (the load is almost entirely in the S6 graph). Root cause, two layers (transcribed): construction-face layer, B-leg = real falsification (root-cause triad class ①: the reading/tool faces show no failure — the Φ definition, tolerance, endpoint-gap formula, corpus, and code are all untouched, with 0 evidence of reading error; the failure follows the kill-line's own literal); proposition-face layer: element ③ unmet + element ④ asymmetric (the Rule 5 four-element test) ⇒ registered root cause = ③ mixed. Dual reading: the classification is consistent with the v2 mandated literal K-V5R3-GT5-4; the classification *basis* differs between the two readings, and both are registered side by side.
- **gt6 — PASS (construction face), sealed.** Original literal `potential_game_explanation_complete`. Readings: `median_r = 1.593752188031628e-29` (static caliber) < 0.1; the trajectory-integral caliber `median_r = 3.203342048593724e-28` also falls on the PASS side; the band [0.1, 0.3] was never hit as-run; the fallback branch ② was not triggered; `new_thresholds_added = 0`.
- **gt8 — PASS (construction face), sealed.** Original literal `supports_H_GT8`. As-run: 2 pairs, #conc = 2, #rev = 0; expanded face: 4 pairs, #conc = 4, #rev = 0, #tied = 0, n_pairs = 4 ⇒ v2 verdict PASS (4 pairs); the pair-count expansion is a construction-type scale parameter, not a threshold. γ-21 is registered (hung, P-10): the two newly added low-arm same-value pairs leave the independence item unremediated; no re-run was performed this round (a re-run would require a new pre-registration).
- **gt5b — PASS (construction face), sealed.** Original literal `supports_narrowed_monotonicity`. Readings: `frac = 1.0` (22/22, the mathematical ceiling) ⇒ the band is structurally unreachable as-run ⇒ PASS as originally registered; the S4 sentinel gate passes (`n_distinct = 5`) ⇒ no KD and the denominator stays 22; the `meanfield_monotone_rate` field is binary-degenerate (`n_distinct = 1`) ⇒ that field's own gate is KD with no separate verdict tier. GT-5 and GT-5b are two verdicts co-reported; neither substitutes for the other.
- **GT-4 — PASS (construction face), sealed.** Original literal `field_coordination_value_supported`. Readings: `median_poa = 1.3333333333333333 > 1.2`; `n_poa_inf = 3`; `n_poa_undefined = 0`; finite values n = 17 (the verdict file's independent recomputation agrees); latent band (1.05, 1.2]. Mandatory bias disclosure (transcribed): the self-interest set is degenerate ⇒ PoA is biased toward the PASS side (not offset against the kill direction this round; the ③ mixed clause was not activated); the median is discontinuous.
- **GT-1 leg — PASS (construction face), sealed.** Original literal `supports_potential_game_framework`. Reading: `0.1 < 0.4 − 0.2 = 0.2` (strictly holds) **and** `20 ≥ 15` ⇒ both conditions met, 0 undefined band. GT-4 and the GT-1 leg are two verdicts, co-reported, 0 substitution.

Discipline readings [E01]: `new_thresholds_added = 0` per case; the five historical JSONs [E32] and the pre-registration and execution files are byte-untouched; the γ register holds 23 items (20 closed / 1 default-tier on file / 2+ pending decision); pending items P-1…P-11 (5 executed / 2 decided pending landing / 4 still pending — 2026-09-29 time point). **DIVERGENCE (drift registration):** `docs/GT_RECONSTRUCTION.md` is registered at `570b7bd3e286` / 6,695 B in the line-setting file but measures `cff15d000d47` / 13,424 B on disk — drift caused by another role's action (γ-16), reported as registered.

#### 4.4.2 #26b (K-V3R-26 literal gap)

Sealed verdict [E04]: file-level verdict = **FAIL (tier 3: original annotation maintained)** — the tier-3 literal is "FAIL (i.e., the original annotation is maintained) ⇒ no re-classification action; the original report's bytes are untouched". Key readings: the three-ontology summary verdicts are FAIL across all three ontologies; `same_direction = true`; `hit_tier_all_same = true`; the hit tier is 3× "tier 3"; all three ontologies' `rates` have n ≥ 8 with mutually distinct `n_distinct` (O1 min/max = 0.0132/0.0173; O3 = 0.33899999999999997/0.3557; O5 = 17.9501/72.0337); `n_distinct = 9/8/9`; `std > 0` across the board; `c4_in_process_full_recompute_identical = true`.

Root cause [E04]: **fake falsification (criterion face / caliber face)** — element ① (the semantic layer) is not satisfied ⇒ the real-falsification elements are incomplete ⇒ the case may not be classified as real falsification; elements ②③④ hold ⇒ the failure is not on the reading/construction side ⇒ the classification is fake falsification rather than unclear (the root cause is localized line-by-line by on-disk code and readings, and is recomputable).

Dual readings (a genuine divergence, co-reported) [E04]: **M1** (main reading: criterion-first + mechanism recomputability) ⇒ FAIL; **R1** (alternative reading: pure K-V3R-26 literal) ⇒ the three ontologies PASS, file tier 1 — M1 and R1 are a genuine file-level divergence (FAIL vs PASS). R1 is not adopted, on the registered ground that the literal in question self-declares as a placeholder in pre-registration v1 (L152/L274/L8/L217) with no on-disk effective-freeze trace, and an ineffective literal cannot overturn a PI-registered effective ruling; **R2** (acknowledging the PI's 23:01 retroactive confirmation) ⇒ FAIL, 0 divergence; **R3** (excluding the D0 re-tier face) ⇒ PASS, as historical D0-corroboration only. The full discretion is listed for the PI/verifier to overturn independently. Four hung items (Q1–Q4): authorization fact-layer evidence is not on disk in any form (substituting a transcription for the original would fabricate the evidence chain; substituting a presumption for authorization would exceed authority).

#### 4.4.3 #35 v2 (GT2b field immunity, expanded matrix)

Sealed verdict [E06]: α-leg **FAIL** / β-leg **FAIL** / composite claim **FAIL** (both legs registered as a pair; no conjunction masking). Key readings: α leg (cross-T stability, denominator 12 cells): IMMUNE 2 / NOT_IMMUNE 10 — not immune = 6 cells at T=3 (6/6 seeds) + 4 cells at T=2 (seeds 20260828/29/30/33); β leg (cross-arm margin, 18 cells): PASS 15 / BELOW_TOL 3 (20260828_T1 at 0.025; 20260829_T1 at the 0.05 knife-edge; 20260833_T1 at 0.025 — all three at T=1). Freeze chronology: pre-registration 2026-09-28 22:22:11 < executor 2026-09-29 12:17:10 < result 12:27:24 ⇒ the registered literal is "the kill-line was frozen approximately 14 hours before the experiment; post-freeze changes: 0" (derived from the timestamps: 13 h 54 min 59 s).

Root cause [E06]: **fake falsification** (α leg: C0+C1+C3; β leg: C0+C2+C4; composite: the C0 family on both legs). The registered statement of what was falsified: "the falsified object is the construction-face cross-T stability criterion / cross-arm attainment criterion — not the proposition face." Mechanism-level root causes (transcribed): C0 (raising T ⇒ fewer decoys ⇒ `field_mean` rises monotonically; 6/6 seeds give exactly 1.000 at T=3; the four T=2 cells give α = 0.075/0.150/0.175/0.200); C1 (structurally identical cells at T=3: 1 gold + 3 traps + 0 decoys ⇒ `field_mean` is identically 1.000, 6/6 cells × 4 domains = 24/24, zero variance); C2 (the T=1 = 1-trap + 2-decoy tier: the margin lands on 1–2 items out of 40, and the threshold of 2 items = twice the granularity of 0.025 ⇒ the β-leg T=1 FAIL sits at the resolution floor); C3 (coverage: 4 domains); C4 (a `-inf` mechanism: trap labels are not in the graph node set ⇒ `field_mean` is set to −∞ ⇒ "not deceived" is a mechanism result of the ranking object domain, not equivalent to semantic recognition capability).

Dual readings [E06]: ① an M1-vs-R1 *root-cause* divergence (M1 = fake falsification; R1 = real falsification) resolved by the registered discretion "mechanism-recomputable evidence takes priority over a pure literal reading", with both readings listed in full for independent overturn; ② a sensitivity reading R2 that removes the six C1 structurally-identical cells (α leg, denominator 6 cells: NOT_IMMUNE 4 / IMMUNE 2; β leg, denominator 12 cells: PASS 9 / BELOW_TOL 3) ⇒ both legs remain FAIL, 0 divergence — the terminal state is robust to the C1 exclusion; ③ the α knife-edge cell `seed20260832_T2` with α = 0.04999999999999993 (mathematically exactly 0.05) is in the same IMMUNE tier under both the literal and mathematical calibers, and the 10 not-immune cells stand independently ⇒ removing or keeping the cell does not change α FAIL; ④ the β knife-edge `20260829_T1` is counted BELOW_TOL by the literal caliber, and the other two cells stand independently ⇒ β FAIL does not depend on the knife-edge handling.

#### 4.4.4 #35 v3 (C0 collinearity correction, A-case 2 full cross)

Sealed verdict [E08]: **claim-level verdict = FAIL** (no fourth state, no fuzzy state). The verdict file's uniquely permitted external sentence is quoted verbatim:

> "On the v3 construction face (6 seeds × 3 T × 2 D × 4 domains × 40 items × 3 arms, option count 3–6 varying by cell), both the α leg and the β leg fall FAIL; the claim-level verdict = FAIL; attribution = fake falsification (construction/sampling-face causes)."

Key readings [E08]: α leg (within-column cross-T stability, denominator 24 cells = 6 seeds × 2 D columns × T∈{2,3}): IMMUNE 8 / NOT_IMMUNE 16; β leg (cross-arm margin, 36 cells): PASS 28 / BELOW_TOL 8 (spread across three (T, D) layers: T1_D1 3, T1_D2 3, T3_D2 2); both legs registered as a pair with no conjunction masking; the independent recomputation file [E10] matches 21/21 (0 rewrites); chronology: freeze registration 14:13:01 < executor 14:21:40 < result 14:29:52 (0 inversions).

Root-cause counts (transcribed) [E08]: real falsification 0 / **fake falsification 3** (α leg, β leg, composite) / mixed 0 / unclear 0. Mechanism-level: **C0 is resolved** (the item-bank layer's 36/36 cells have `n_decoys == D` independent of T); C1's structurally-identical cells are unreachable (`D ≥ 1` ⇒ no D=0-type cells exist; the 36 cells' `field_mean` maximum is 0.725); **C4 fully retained, 0 release** (A-case 2 did not touch it; the 4-domain intersection is 0; all 2,880 trap positions in the 36 cells are set to −∞); C5 sampling-implementation differences.

Effectivity dispute and conditional blank (co-reported, unresolved) [E08][E11]: the batch-9 decisions register [E11] is internally self-contradictory (its §1.1 records "effective" while lines 11/197 still read "pending review"); the verdict file does not reconcile this. The ruling: the line-setting precondition holds *at the registration layer* ⇒ it does not block the verdict's closure (three criteria: ≥ 2 independent on-disk locations; 0 chronological inversion; 0 newly created criterion text — all criteria are existing K-* references, and the precondition dispute does not change the verdict outcome). The registered conditional blank is quoted verbatim: **if the PI retroactively rules that the batch-9 register does not constitute a valid effectivity registration ⇒ this file's verdict must be re-ruled as KD** (K-V5R2-35-AR5), as a new-evidence/new-verdict-file matter with 0 retroactive rewriting.

Co-reporting mandate [E08]: v2 is not overturned; any external statement must present the pair — "v2 paired verdict = FAIL (root cause fake falsification, bytes untouched)" / "v3 paired verdict = FAIL (root cause fake falsification)". The verdict file's five forbidden statements are reproduced as binding: ① 0 "the GT2b proposition is falsified / the proposition is dead"; ② 0 "the GT2b proposition holds / field immunity is proven"; ③ 0 cross-face consistency claims; ④ 0 use of the as-run legacy parity face to support rulings; ⑤ 0 extrapolating this FAIL to "the decoupled T effect really exists" or "does not exist" — **this FAIL supports no proposition-face conclusion in either direction.**

#### 4.4.5 C5 B group (SVD-3 coordinate collapse, post-fix re-run)

Sealed verdict [E12]: K-V3DF-0-1 (reading face) **FAIL**; K-V3DF-0-2 (original-file-untouched gate) PASS; K-V3DF-5-1 (post-fix four-reading set) PASS; K-V3DF-5-2 (Hamming expected reference) PASS; K-V3DF-5-3 (cross-seed non-degeneration control) PASS; K-V3DF-9-1/9-2/9-3 (full-chain reverification) PASS; the C5 B-group claim total = **FAIL (fake falsification: construction/material face)**. Key readings: the post-fix construction gives codewords 9 / zero pairs 50 / tightest within-class tier 1.33, *systematically worse* than the uniform-random control group (codewords 20 / zero pairs 2); the Hamming mean moves 1.961 → 3.026; the K-V3DF-0-1 reading face reports no `min`/`max`/`std`. The verdict-keeper independently recomputed 14 items (0 reuse of self-reported values). Root-cause counts: real 0 / **fake 2** / mixed 0 / unclear 0.

Anti-misleading locks (transcribed from the verdict file [E12]): the K-V3DF-5-1 PASS means only "the four readings are reported completely and correctly" — it does **not** mean "fixed"; 0 statements that "C5 is fixed / the collapse is resolved / discrimination is restored"; 0 statements that "the SVD-3 coordinate-collapse proposition is dead" — the root cause is fake falsification, the proposition is not falsified, and this construction did not solve it; 0 use of the Hamming mean 1.961 → 3.026 as a "discrimination improvement" claim (a code-length confound, listed in the halt report's §3.3); 0 statements that "0 degeneration alarms = gate passed" (the 0-1 line requires the min/max/std faces; unreported = "the gate was not run", not "the gate passed"). Four unclosed items are registered (a protocol-version carrier gap → PI; a `dual_hex_width` exemption already ruled with a literal revision requiring PI filing; a difference-registry reading confirmed in place; the min/max/std non-reporting → worker + verifier).

#### 4.4.6 P-J / P-M / P-C degeneration families

Sealed verdict [E14]: **all three families close KD at the family level** (P-J = KD / P-M = KD / P-C = KD; 0 PASS + 0 FAIL at family level); face level: 8 faces = KD 4 + PASS 4; the 19 `K-PJPC-*` lines: PASS 12 + **FAIL 1** + KD 6 (the sole FAIL is K-PJPC-0-1). Key readings: the K-PJPC-0-1 FAIL targets **role-1's "self-certification complete / no missing items / `达标: true` declaration — not its numeric readings** — the numeric face's 41/41 sequences recompute identically, 0 deviation, 0 tolerance relaxation (five 1-ULP differences were each proactively self-registered by role 1 ⇒ 0 concealment on the honesty face); coverage: the input face is 0-covered on 4 of 6 faces (P-J new construction on O1/O3/O5; P-C new construction on one face); 11 upstream input fields (8 distinct) have 0 hits in role-1's file.

Root causes [E14]: P-J = ② fake falsification; P-M = ② fake falsification; P-C = 0 real, 0 fake ⇒ **not computable ⇒ KD**. Role-2's overall FAIL stands, 0 retro-edit; attribution γ-10 (fake falsification, self-certification-layer failure). Dual reading (transcribed): the legacy tier-2 verdict is 0-covered, 0-revoked, 0-retroactively-accepted — three legs co-reported + literal co-reference mapping + the alternative reading likewise yields 0 overturns; "unclear" does not serve as a fourth state (per the batch-4 ruling: unclear = expanded KD, co-reported). Unresolved and untouched items: the `matrix.operator` attribution is reserved to the PI (R-01); a registration-mismatch file's KD (material not computable) carries 0 attribution and 0 retro-edit, transferred to the evidence-auditor + R-04; the P-I/P-L members are untouched (PI batch 5 ruling: 0 separate establishment, 0 merging, 0 mixed tallying); 0 self-invented rules (7 items without existing-criterion coverage are all reserved to the PI).

#### 4.4.7 #32 CPATH (with-RAG live rerun)

This case is a **supplementary live-run registration file, not a three-state verdict face** [E16]; it is included for completeness of the V3 record. Trigger and scope: an API-key recovery plus quota reset plus a PI release (per the "#32 rerun" line of the V4 README [E65]); 30 cells (gsm8k 15 + strategyqa 15); the baseline cells' prompts are exactly 2 lines ⇒ the runner splice face holds; `svd2_coords` covers the strip's 22/22 ids with no missing items; the products are a runner copy [E20] (4 changes vs the upstream runner) and a live-rerun data file [E19]. Dual reading (transcribed): the no-RAG face has two calibers — the gsm8k 15 cells re-judged by the same extractor read **80.0% vs the stored original 73.3%** (two calibers co-reported, 0 selection). Six unresolved items are registered verbatim (extractor body unlocated; two empty responses' upstream cause unlocated with 0 cause assertion — only a usage-based fact statement; the svd2 sign caliber not unified between the report and the runner, 0 ruling on which side is authoritative; the release-action literal not in the input list; the #32 status field not updated in the prior verdict, which is 0-modified with the update location pending PI; cost not recomputed, with 0 restatement of design-time estimates). The prior verdict [E17] and the 2026-09-10 simulation report [E18] are byte-untouched.

### 4.5 Registered divergences of the V3 face (unresolved, co-reported)

Appendix C consolidates the divergence register. The V3-face entries include: the K-V3S-3-1 domain divergence (main reading 7 days PASS vs old-accounting-domain 3 days ⇒ FAIL, undecided, reserved to the PI/protocol layer — the verdict file pre-registers no softened phrasing for that contingency); the R-RUN domain (per-day composition unregistered ⇒ KD, no derivation); the #35 v3 effectivity dispute with its conditional KD blank; the #26b M1-vs-R1 FAIL-vs-PASS file-level divergence; a three-caliber count 77/74/62 with 0 selection; the `matrix.operator` attribution; a gate-one authoritative-distribution attribution (two distributions swapped, undecided); a legacy paper-file two-reading discrepancy (registered `8baa9854b3f7` / 239,700 B vs a third-party self-report `fd39cf811232` / 236,425 B / 1,396 lines — attribution 0 asserted: line-ending style, encoding, version, and carrier are all possible); two anchor-value two-reading items; the C5 unclosed items; and the fact that 39 entries without `event_id` cannot have their distinctness verified ⇒ "186 = 186 distinct entries" is not decidable (the T-1 verdict file's own honest-accounting item 9).

---

## 5 V4: critical learning of the PI's chain of thought (distillation track)

### 5.1 The goal, and the anti-profiling boundary

The V4 main line is the distillation track, whose registered subject family is the "PI chain-of-thought distillation" line (pi_cot / D1–D8 / S3 / S4 / Task B). The track's goal statement is transcribed from the v2.2 pre-registration [E33], which is the goal's authoritative literal:

> Distillation = the AI critically learning the PI's way of thinking (methodology internalization) — not PI profiling / behavior prediction (PI's own characterization, translated from the registered original 「我的思维方式可以被 AI 批判性学习……不应是给我做画像」: "my way of thinking can be critically learned by an AI … it should not be turned into a profile of me"). The product is a transferable judgment-method rule set (criterion structure / tradeoff patterns / principle application), for the AI to internalize for critical use.

Boundary declarations (transcribed from [E33] §7): no prediction of the PI's behavior; no personal model exported outward; the product is a method rule set for AI internalization; full reasoning texts are a privacy face and stay local only; no LLM-based collection; no credentials involved; effective-locked, not re-opened.

**Caliber history (mandatory disclosure, to prevent the deprecated caliber from re-entering use).** The track's v1 measured a "reproduction-consistency rate" — a profiling-style caliber, now deprecated, with the registered revision chain: v2.0 (with decision traces) → v2.1 (collection face = a purpose-built distillation questionnaire) → v2.2 (claim re-definition: profiling-style reproduction-consistency rate → critical-learning tripartite criteria). The v1 anchors are registered as `696af9121d9f` (pre-registration) and `D279EBDE5E84` (verdict; re-attributed to fake falsification on the material face, with a claim-positioning deviation note) — transcribed values, 0 direct read for this draft. Any occurrence of the "reproduction-consistency rate" caliber in historical citation is accompanied by a note that the caliber is deprecated.

### 5.2 The falsifiable claim and pre-registered thresholds

The falsifiable claim (transcribed from [E33] §2): from N ≥ 50 cross-day PI judgment events, a learned rule set is evaluated on held-out data; (i) structural similarity ≥ 0.80; (ii) disagreement-critique coverage 100%; (iii) blind-obedience rate ≤ 0.10. Any criterion unmet = the critical-learning claim fails. The measurement triad (*Table 5*, pre-registration literal [E33] §1):

| Face | Definition (pre-registration literal) | Concept |
|---|---|---|
| ① Extractability (fidelity) | criterion structure in reasoning texts is rule-extractable (deterministic 6-class criterion-type coding: kill-line / cost / principle / risk / timing / delegation) | structural similarity |
| ② Transferability (learning) | the rule set's reasoning structure on held-out scenes reaches similarity ≥ 0.80 against the PI's (criterion-type sequence alignment rate) | learning effect |
| ③ Criticality (non-blind-obedience) | at every rule-set-vs-PI disagreement, an explicit critique reason is attached (coverage 100%); blind-obedience rate (agreement without reason) ≤ 0.10 | the mechanizable definition of "critical learning" |

Kill-lines (v2.2 §4, transcribed): (a) structural similarity < 0.80 → FAIL; (b) critique coverage < 1.00 or blind-obedience > 0.10 → FAIL; (c) bootstrap CI (n=1000, seed=42) lower bound < 0.50 → FAIL. Any branch firing ⇒ FAIL (**limited to the construction domain**); none firing ⇒ PASS. Every verdict row carries a root-cause classification.

*Table 4 — pre-registered thresholds (quoted verbatim; 0 adjustment, 0 substitution — the protocol's threshold-literal unique source is [E22]):*

| Line | Literal | Line | Literal |
|---|---|---|---|
| TH-v2-1 | N_min = 50 (full reasoning collected) | TH-v2-5b | blind-obedience 0.10; critique coverage 1.00 |
| TH-v2-2 | corrections/reversal events ≥ 5 | TH-v2-6 | seed = 42 |
| TH-v2-3 | cross-day ≥ 3 days, single-day share ≤ 60% | TH-v2-7 | permutation n = 1000, α = 0.05 |
| TH-v2-4 | held-out = 0.30, stratified incl. corrections | TH-v2-8 | bootstrap n = 1000, CI 95%, lower bound 0.50 |
| TH-v2-5 | structural-similarity threshold = 0.80 | | |

The v3 pre-registration (Task B v3) adds five thresholds, TH-v3-10…14, with the same freeze discipline: structural-similarity threshold 0.65 (caliber A), 0.55 (caliber B), critique coverage 1.00, blind-obedience 0.10, bootstrap CI lower bound 0.40, plus a sentinel dual-caliber consistency line.

### 5.3 Collection protocol and substrate

**Protocol (transcribed from the collection questionnaire's §0, six rules [E47]).** 1–2 questions per elicitation round; cross-day ≥ 3 days with single-day share ≤ 60%; total N ≥ 50 judgment events with full reasoning text as a mandatory collection item (the PI may answer "skip reasoning", recorded as null — no forced answering); each event is one option (judgment direction) plus one sentence of reasoning; events land in a dedicated dataset JSON with fields {event_id, date, q_id, scene_tag, judge_type (6-class code), option_chosen, reasoning_full, is_correction, weight}; reversal pairs (R-series: R1a/R1b …) re-ask a slightly varied same-scene question with ≥ 1-day separation against memory effects — a direction change is recorded as a correction/reversal event; held-out 0.30 stratified including corrections; full reasoning texts are a privacy face (local-only, never into prompts to external LLMs).

*Table 6 — collection waves D1–D8 (transcribed from the T-SUP-2 closeout recompute [E50] §3.2; all values are on-disk final-state measurements, 0 use of stale pre-estimates):*

| Calendar day | Entries | Share | Composition |
|---|---|---|---|
| 2026-09-24 | 40 | 22.2% | v1.1 main set 37 + reinforcement 3 (D1) |
| 2026-09-26 | 32 | 17.8% | D2 five waves 20 + D3 three-read 12 |
| 2026-09-27 | 7 | 3.9% | d4 5 + d5 2 (D4/D5) |
| 2026-09-28 | 4 | 2.2% | d6 2 + d6b 2 (D6) |
| 2026-09-29 | 1 | 0.6% | d7 (DF6-4, S3→D7 wave; the source of the 5th distinct day) |
| 2026-09-30 | 96 | 53.3% | D8 main 93 + b-half 3 |
| **Total** | **180** | 100% | **distinct days = 6** |

**DIVERGENCE (date-caliber):** an independent rescan of the ledger under an "any date string" reading (including metadata dates such as `created`) counts 11 days, vs the event-`date`-field reading of 6 days — two readings co-registered, neither replacing the other [E50].

**The D8 main wave is a pure question file (0 answered)**: "80 questions presented at once for the PI to answer in batch (file-based or in sub-batches)" [E48]. Its §1 carries the protocol-compliance mapping (six rules, literal-unchanged, each mapped); its §4 is the R-series reversal-pair index (R9/R10/R11, with the b-half flagged D9+ next-day); it reuses neither the 50-question bank nor any D-wave-used question face (§7's no-fabrication declaration). A registered divergence on this file's fingerprint: the current disk copy measures 53,583 B (after a 2026-10-06 anonymization batch and a 2026-10-12 correction wave, +2 B of desensitization/path-level adjustment; question-face readings unchanged), vs the 2026-10-01-time registered value of 53,581 B — both registered; the remote-registered value is blob sha1 `de3da25bc7a8…` / 53,583 B [E48]. A supplementary 8-question open-ended wave [E49] was registered under the PI's 2026-09-30 rulings (T-D8-1 caliber: the on-disk count of 83 existing + 80 batch = 163, four short of the 167 substrate floor; T-D8-2: option B = a supplementary collection wave, all open-ended, thought-oriented (题性：思考型), high-efficiency distillation questions; 6–8 range taking 8 as anti-loss margin).

**Closeout verification (transcribed from [E50]):** present 19 / absent 0 / mismatch 3 — V-02 (two question ids revised at a boundary, a label drift with content identical, verbatim-identical anchor registered); V-12 (the R-series pairs' actual separation was 0 days, not meeting the ≥ 1-day interval); V-18 (a ledger SHA registration vs measurement mismatch — five values coexisting at different time points, 0 attribution, 0 reconciliation). Counting rules M-1…M-6 (including: relabeled/metadata files are not counted into N; a main-file b-half placeholder plus its actual answer count as one event, 0 double counting). The correction-event count carries a registered three-reading divergence — `is_correction=true` counts 7; `correction_confirmed=true` counts 2; a pair-closure reading counts ≥ 5 with fields `None` — 2↔7, undecided at this layer (the S3 verdict later expands this to seven readings, §5.4.3).

**Privacy discipline (binding on this paper as well):** dataset reasoning full texts are never uploaded, exported, or pasted into any paper; dataset JSONs are cited by path + SHA-12 + byte count only ([E51]–[E54]); no credentials, internal session ids, or internal agent rosters appear anywhere; model and endpoint names are quoted per the public on-record literals; the teacher-side entity list is not expanded.

### 5.4 The V4 judgment set

*Table 7 — sealed verdicts (all original literals; all faces on or before 2026-10-01):*

| Case | Sealed verdict (literal face) | Root cause (registered) | Anchor |
|---|---|---|---|
| Task B v1 | FAIL (exploratory) | construction-failure family (fake-falsification suspicion unexcluded) | [E34] |
| Task B v2 (formal) | `FAIL (formal v2, 正式判定)` | composite: 2 compound (partial α+β) + 2 β + 0 pure α | [E35][E36] |
| Task B v3 (formal) | FAIL (formal v3) — 5/6 kill-lines hit, all FAIL; sentinel not triggered | 3 compound + 2 β dominant + 1 sentinel PASS + 0 pure α | [E37][E38] |
| N-26 (L14 v3, teacher metadata) | K-N26-2 TRIGGERED (real-falsification line); whole-case direction = real-falsification direction | real-falsification elements ①②③④ all satisfied | [E39] |
| S3 segment (collection-face criteria) | K-V3S-3-1 PASS / K-V3S-3-2 PASS / K-V3S-3-3 back-half KD ⇒ whole-line KD | unclear (0 fake, 0 real — readings straddle) | [E40][E41] |
| T1 → T1.5 → T1.5r2 (sensitivity probe chain) | three verdicts with the same literal PASS on K-T1-S3, carrying three different registered root-cause tiers | T1: false robustness (construction-failure family); T1.5: true robustness (repair effective); T1.5r2: true robustness + root cause eliminated | [E43][E44][E45] |
| Track 2 (multi-model cross check) | "6/6 models 5/5 all FAIL; 6/6 all belong to tool-or-construction-layer failure" | construction-layer failure, cross-robust across 6 models × 5 teachers | [E46] |
| Fake-verdict case | tool-issued kill re-registered as restored (已复原) per PI ruling | fake falsification (tool face) | [E27]–[E31] |

#### 5.4.1 Task B v1 → v2 → v3 (the formal verdict chain)

**v1 — FAIL (exploratory).** The v1 verdict [E34] closed the first run as FAIL (exploratory) with the fake-falsification suspicion unexcluded (construction-failure family). The v1 caliber (reproduction-consistency rate) is deprecated (§5.1); the verdict itself remains sealed as a historical record.

**v2 — FAIL (formal).** The v2 verdict's literal is `FAIL (formal v2, 正式判定)` — the formal-verdict tier was released by the PI, and the day-span attainment was superseded by a registered 3-day reading [E35]. All four kill-lines fired (*Table 8*):

| Line | Criterion | Main reading (n) | Alternative reading (n) | Verdict |
|---|---|---|---|---|
| K-V2-a | structural similarity ≥ 0.80 | 0.0909 (n=22 held-out) | 0.1618 (n=17) | FAIL |
| K-V2-b1 | critique coverage ≥ 1.00 | 0.6842 (n_div=19 / n_crit=13) | 0.6923 | FAIL |
| K-V2-b2 | blind-obedience ≤ 0.10 | 0.3333 (n_agree=3 / n_blind=1) | 0.0 | FAIL |
| K-V2-c | bootstrap CI lower bound ≥ 0.50 | CI [0.0, 0.2045] (n=1000) | [0.0294, 0.3382] | FAIL |

Auxiliary readings (transcribed): permutation p = 0.7912; the UNK (no-criterion-available) rate fell 55.6% (40/72) → 22.2% (16/72); the v1 run hit 3 lines, the v2 run hit 4. Root cause: composite attribution = 2 compound (partial α+β) + 2 β + 0 pure α. A registered anomaly is reported with the verdict: the UNK rate improved while similarity, blind-obedience, and the permutation p all worsened — read as construction failure masking an insufficient real-falsification signal. A signoff file [E36] verified the anchor-chain integrity (PASS; addendum SHA drift: empty).

**v3 — FAIL (formal).** The v3 verdict [E37] closed the track after two registered *dissolutions* were implemented and landed: dissolution A (expressiveness ceiling raised: decision tree depth ≤4 → ≤6; features 9 → 12; full-sequence and phrase patterns added) and dissolution B (measurement replaced by a dual-caliber pair — a Needleman–Wunsch-alignment structural similarity and a normalized Levenshtein-based similarity, co-reported with 0 cherry-picking). Five of six kill-lines fired (*Table 9*):

| Line | Criterion | Main reading (n) | Alternative reading (n) | Verdict |
|---|---|---|---|---|
| K-V3-A | NW structural similarity ≥ 0.65 | 0.4534 (n=23) | 0.5127 (n=18) | FAIL |
| K-V3-A' | NLED structural similarity ≥ 0.55 | 0.2754 | 0.2963 | FAIL |
| K-V3-B | critique coverage ≥ 1.00 | 0.4286 (n_div=14 / n_crit=6) | 0.3636 | FAIL |
| K-V3-C | blind-obedience ≤ 0.10 | 0.2222 (n_agree=9 / n_blind=2) | 0.2857 | FAIL |
| K-V3-D | bootstrap CI lower bound ≥ 0.40 | CI [0.3217, 0.5870] | [0.3722, 0.6611] | FAIL |
| K-V3-E | sentinel: dual-caliber direction consistency | direction_consistent = True | — | not triggered |

Auxiliary readings (transcribed): permutation p = 0.0160 (significant — the rule set does carry learnable structure); on the 23 held-out items, 4 items reached similarity 1.0 and another 4 reached 0.5/0.6 (partial-match signals); the substrate accounting is 77 RUN + 8 D1 missing-fill = 85 (64 v2 on-disk + 8 post-v2 + 5 D4), cross-day 3 days. Root cause: 3 compound + 2 β dominant + 1 sentinel PASS + 0 pure α. The verdict's registered interpretation: after the construction face was corrected, the real-falsification signal was exposed and the composite attribution deepened — the construction face was explicitly displaced and **the FAIL remains**. Extrapolation ban (quoted): the FAIL is construction-domain-limited; it is not extrapolated to "the PI's chain of thought is not distillable". A signoff file [E38] includes the R5 privacy check (a 6-file literal scan).

**The chain's co-reporting mandate.** The three verdicts are frozen side-by-side with 0 overturning: v1 mechanical binary (real/fake) → v2 composite attribution → v3 construction displaced, FAIL persists. *Table 10 — the v1→v3 registered evolution (each column's values anchored to the corresponding verdict file [E34][E35][E37]):*

| Metric | v1 | v2 | v3 |
|---|---|---|---|
| UNK rate | 55.6% | 22.2% | — |
| structural similarity | (deprecated caliber) | 0.0909 | NW 0.4534 / NLED 0.2754 |
| critique coverage | (deprecated caliber) | 0.6842 | 0.4286 |
| blind-obedience | (deprecated caliber) | 0.3333 | 0.2222 |
| permutation p | 0.2937 | 0.7912 | 0.0160 |
| kill-lines hit | 3 | 4 | 5/6 |
| root-cause composition | 3β + 1 untriggered | 2 compound + 2β | 3 compound + 2β + sentinel PASS |

The v1 values are quoted here only as the registered chain's historical columns, each carrying the deprecated-caliber note of §5.1.

#### 5.4.2 N-26 (L14 v3: teacher-metadata indistinguishability)

The N-26 verdict [E39] closes a supplementary live-verification of whether a teacher-side model can be identified from collected metadata features. Sealed readings (*Table 11*, transcribed):

| Line | Criterion literal | Reading | Verdict |
|---|---|---|---|
| K-N26-1 | teacher accuracy (5-teacher mean) ≥ 0.70 → hit = real-falsification line | mean 0.5617 < 0.70 (the `kimi` endpoint's 0.7512 is the sole ≥ 0.70 item; the other four endpoints all < 0.70) | not triggered (weakly maintains the v1/v2 direction) |
| K-N26-2 | pooled AUC ≥ 0.75 | 0.5663; 5-fold CV 0.5266–0.6318 (five-read sensitivity, all < 0.75) | **TRIGGERED** (real falsification) |
| K-N26-3 | ≥ 4 teacher endpoints with accuracy < 0.60 | 3/5 | not triggered |
| K-N26-N1/N2 | construction non-degeneration / tun compliance | pass = True (10 cells all paired) | PASS |

Direction (transcribed): the whole-case direction = **real-falsification direction** (metadata indistinguishability empirically supported along the v1/v2 direction); the prior L4 verdict's literal "FAIL · construction infeasible · 4/5 teacher metadata missing" is quoted verbatim with 0 overturn. Reproduction face: a whole-chain rerun (5 teachers × 22 captions × ≥ 5 calls × bidirectional ⇒ ≥ 1,100 calls; measured 1,090 calls = 99%+ of the lower bound; one teacher endpoint's 77 calls = a registered gap disclosed by the worker, read as not a construction failure); stratified 5-fold cross-validation with a linear discriminator over 6 metadata features. Root cause: the real-falsification four elements ①②③④ are all satisfied. Expression boundary (binding): the endpoint identities are quoted as recorded in the verdict file; the teacher-side entity list is not expanded here; the `kimi` 0.7512 single strong item is reported with the verdict's own no-extrapolation note — 0 "completely indistinguishable" conclusions.

#### 5.4.3 S3 segment (collection-face criteria on the substrate)

The S3 verdict [E40] closes the S3 segment (data three-in-one landing: D1 backfill 8 + D6 wave + the pre-existing substrate). Sealed rulings (*Table 12*):

| Line | Criterion | Reading (registered) | Verdict |
|---|---|---|---|
| K-V3S-3-1 | cross-day ≥ 5 | 6 days (six readings consistent at 6; alternative readings 11/13, all ≥ 5; margin +1) | **PASS** |
| K-V3S-3-2 | single-day share ≤ 60% | 0.5000–0.5333 (six readings, all ≤ 0.60; tightest margin 0.0667; 0 reuse of the old 56.5%) | **PASS** |
| K-V3S-3-3, front | N ≥ 50 | 160–180 (five readings; margin ≥ +110) | **PASS** |
| K-V3S-3-3, back | corrections/reversals ≥ 5 | seven readings (2/5/7/8/11/16) straddling the threshold; ruled path: field face ⇒ 7; 35 entries missing `is_correction` (incl. 6 R*b halves); missing-field backfill rule 0-defined (a draft exists, pending PI) | **KD** |
| whole line | conjunction | not assignable as a boolean | **KD** |

Root-cause counts: real 0 / fake 0 / KD 1 / PASS 3. The root cause for the back-half KD is registered as *unclear* — 0 fake (no FAIL face), 0 real (readings straddle the threshold), elements ②③④ unmet. Sensitivity registrations (transcribed): the thin-day sensitivity (2 of 6 days are thin: 09-28 with 4 entries, 09-29 with 1, 2.8% of the total; an alternative reading removing both ⇒ 4 days ⇒ FAIL — the flip threshold is removing 2 thin days; thin-day removal is not a pre-registered caliber, 0 rule invention, main reading adopted); the single-day share's tightest reading 0.5333 is dominated by the 09-30 wave (96 entries); reverse sensitivity: +13 entries on 09-30 (96 → 109) with N growing to 193 ⇒ 109/193 = 0.5648, still ≤ 0.60; in the separate scenario where N stays 180 and the 09-30 count reaches 108 ⇒ 108/180 = 0.6000 exactly at the knife-edge; the 0.60 cutoff sits 0.0667 from the tightest reading, and the S4 expansion requires recomputation. Boundary statements (quoted): the K-V3S-3-4 wordlist-expansion criterion is the verdict-face hit line (critique coverage 1.00) — its lock state is unverified ⇒ 0 judgment; collection-face PASS = "collection-face criteria attained under the pre-registered literal", carrying 0 proposition-face claim (distillation/transferability). Registered fingerprint note: the current disk copy (35,037 B) differs from the 2026-10-01 registered value (35,022 B) by a 2026-10-12 correction-wave overwrite (KD-glossary unification); the verdict tier and readings are unchanged [E40]. A registered ceiling transcription (0 direct read of the source): the project's clue ledger registers K-V3S-3-4 as "structurally unreachable on this substrate (ceiling 0.7143 main / 0.6000 alternative)" — carried here with the transcription mark.

**S3–T-1 relationship (reported without reconciliation).** The T-1 gate closure verdict [E21] (§4.2c) and the S3 verdict [E40] both rule on the shared collection substrate under different domains: the T-1 recompute uses the whole-event domain (n_after = 186, 7 days, 0.516129 = 96/186), and the S3 verdict uses the S3-domain accounting (180 entries, 6 days, 0.5000–0.5333). Both are sealed verdict artifacts with their own anchors; the reading differences between the two files are reported here side by side, 0 reconciliation.

#### 5.4.4 T1 → T1.5 → T1.5r2 (a sensitivity-probe chain; same literal, three qualities)

This chain probes the *interpretation* of a literal PASS under three different constructions — the track's own registered demonstration that a measurement reading must carry its root-cause attribution before entering any paper:

- **T1 [E43].** The verdict is PASS (judgment robust) on the temperature-flip line (no cell hit; J-median all < 0.85 across 4 endpoints × dimensions × 3 temperature cells) — with the verdict's own attribution reversal: the K-T1-S3 literal PASS is registered as **false robustness**, a construction-failure-family artifact (49.3% empty responses + 72.1% empty–empty pairs ⇒ J = 0.0 mainly from "both empty" agreement, not from true judgment agreement; a reasoning model under a max_tokens = 100 budget mismatch). The real-falsification elements ②③④ were lost. A companion line's 12 cells all FAIL on sample insufficiency.
- **T1.5 [E44].** After the construction was fixed (non-reasoning endpoint; the token budget raised), K-T1-S3 = PASS, registered as **true robustness**: same-caption J = 1.0 and cross-caption J = 0.0 = content divergence (normal model behavior), plus a T1-verdict information-correction note.
- **T1.5r2 [E45].** K-T1-S3 = PASS registered as **true robustness** (pair expansion 6 → 15 per teacher ≥ N_min = 10; real-falsification elements ①②③④ all satisfied); n_empty_responses = 0 (vs T1's 49.3%); readings: same-caption J median 0.75–1.0 (L2) / 0.5–0.5556 (L14); cross-caption J = 0.0; pooled J = 0.0 (cross-caption dominated, as in T1.5). Two companion lines close FAIL with real-falsification attributions (an endpoint's inherent variance; a literal sample floor) — prior verdicts untouched.

The registered reading of the chain (per the three verdict files' root-cause tiers, [E43][E44][E45]): "same literal PASS with a three-stage qualitative evolution" — T1 false robustness (construction-failure family) → T1.5 true robustness → T1.5r2 true robustness + root-cause elimination confirmed; J = 0.0 has completely different semantics under different constructions (empty–empty agreement vs content divergence), so **measurement readings must carry root-cause attribution before entering a paper**. A point-bar literal registered in the project's clue ledger ("cross-day 2-day attainment supersede chain tail") is not present in the verdict files — carried here with a 0-direct-read mark.

#### 5.4.5 Track 2 (multi-model cross check)

Sealed verdict [E46], literal: **"6/6 models 5/5 all FAIL; 6/6 all belong to tool-or-construction-layer failure"** — with the verdict's own statement: "it is not the proposition that was falsified; it is the construction layer that failed (n_in_context = 2 / n_calls = 3 / proxy n = 3 / teacher-side n ≥ 23 — sample and control insufficiency)." Key readings: a 6-model × 5-teacher dual cross (15 legs); the root-cause classifier's three literal branches (degenerate pair-distance; zero difference between arms; proxy/teacher ratio < 0.20) — 6/6 models each hit one branch; a model-upgrade control did not overturn the verdict (the `qwen` endpoint upgraded to the `qwen_plan` endpoint, recorded as the qwen3.7-max token-plan endpoint, maintains FAIL with the same root cause). The registered basis: multi-model × multi-teacher dual-cross stable reproduction of "same construction, different model, unchanged root cause" = the kill basis — cross-robustness evidence for the construction-layer attribution of the negative result.

### 5.5 Deferred and open faces of the V4 track (status registrations, 0 adjudication)

- **S4 segment (deferred, unfrozen).** Criteria registered but not frozen (unfrozen_pending_PI): held-out 0.30 stratified inclusion of corrections; substrate ≥ 150 and held-out ≥ 50 ⇒ self-consistency floor substrate ≥ 167; ≥ 5 days + single-day ≤ 60% recomputed on the S4 substrate; status: a three-line inconsistency conflict is registered (P-S4-1), 0 freeze before a PI ruling; a codebook-collapse risk is registered for the stratification (23 → 50+ cells, empty-cell risk). This segment is **not executed**; attainment readings located in S4 are reported by upstream verdicts as blocked, not judged.
- **K-V3S-3-4 lock state (unjudged).** The wordlist-expansion criterion's lock state is unverified ⇒ 0 judgment (§5.4.3).
- **Missing-field backfill rule (draft, pending PI).** A draft exists [E56], pending PI approval; 0 application.
- **Registered superseded values (0 reuse).** The v3 dataset's registration-time values (N = 85 / 3 days / 56.5%) are superseded by the S3 recompute (180 / 6 days / 0.5000–0.5333); a registered difference face between the v3 dataset's N = 85 and the S3 measurement N = 180 is carried with 0 reconciliation (two accountings coexist).
- **Cross-track collection dependence.** The T-1 gate closure (§4.2c) depended on the D1/D5 collection waves of this track — the two tracks share a substrate; the sharing is reported, not reconciled.

---

## 6 Auditing the verdict chain itself: the fake-verdict case

The project's honesty discipline is not only a rule set for producing verdicts; it was applied to a verdict-producing tool when the tool itself generated a false kill. This section is the paper's core institutional case; its artifacts are [E27]–[E31].

**What happened.** A tool output raised a hash alert, and a "kill" (判死) registration was issued on that basis. A forensics file [E28] attributed the alert's mechanism: the tool computed hashes with a SHA-1 implementation while carrying a hardcoded label reading "SHA-256 first 16" — a hash-label mislabeling mechanism; the alert was a false alarm. The forensics face preserved the drafting role's original command line and restored it.

**How it was closed.** Per a PI ruling, the original "tool kill" registration was re-registered from 判死 (kill) to **已复原 (restored)** [E27] — six items registered verbatim, with the action tier changed by registration from "kill" to "restored". A re-verification pass [E31] re-ran the affected chain.

**What the re-registration did not do.** It did not soften any result: the withdrawal was *by root-cause classification* (fake falsification — tool face), not by re-evaluating the outcome; every original line is retained; the correction is append-only.

**The backfill (registered).** A six-item ledger backfill under a registered plan: the pre-backfill ledger measured 38,299 B / 352 lines (LF); the backfill executed 15 hit-file checks → 10 append-erratum operations / 5 skips, each registered. Two of the five skips are *protective*: two self-referential-prefix files correctly stated their own fingerprints, and appending would have broken their self-reference — the PI's registered ruling: "skip ≠ omission". The backfill's discipline statements (transcribed): 0 deletion or modification of any existing line (append-only); 0 overwrite (a four-way name-collision check); a certification-tool drift corrected via end-append; read-only backups executed; 0 network / 0 external LLM / 0 API; no credential ever in plaintext.

**Why this case matters.** The kill-line protocol treats *verdicts* as falsifiable artifacts with their own production chain, and it extends the same three-state + root-cause + no-softening machinery to the verdict chain itself. A false kill produced by a mislabeled hash is registered, root-caused, and re-registered as restored — with the tool's failure localized, recomputable, and separated from any proposition-face conclusion. The case demonstrates that the honesty discipline is institutional rather than aspirational: the mechanism that would have buried an inconvenient negative result (a tool's authoritative-looking kill) is the same mechanism that surfaces its own false alarms.

---

## 7 Related work

This section's V3-facing and genre-facing entries are drawn from the project's verified reference base — the repository's BibTeX ledger [E58] (37 entries, cross-checked per its header note) and the prior manuscript's unified external reference system [E57] (62 entries, with verification annotations registered in [E62]) — transcribed here in the base's own registered form. Entry-level re-verification was not performed for this draft (§9). The V4-facing subsection fills the slots reserved in v0.1 from the supplementary literature scan, with two slots still pending (§7.5).

### 7.1 Game theory, potential games, and price of anarchy

The deposon mechanism's validation frame sits in the potential-games lineage: potential games [R1] and congestion games [R2], population best-response dynamics [R3], flow decompositions of games [R4], and graphon limits of large games [R5]. The price-of-anarchy instrumentation used in the GT-4 case descends from the original PoA bound line [R10][R11] (affine congestion PoA = 4/3) and its later variants [R12], with a distribution-level PoA precedent [R13] closest in spirit to the project's distribution-level reporting. Algorithmic-game-theory and mechanism-design verification contexts [R14][R15][R16][R17] frame the audit/security-adjacent uses the project's V2 explanation engaged with. A graphon-games entry [R5] is the registered closest formal neighbor for the "field" (potential-function best-response limit) positioning statement of the V2 lineage [E59].

### 7.2 LLM reasoning, its fragility, and its measurement

The V3 track's measured object is an LLM player's distortion relative to a Bayesian baseline, so the chain-of-thought capability literature [R20][R21] and its prompt-level extensions (tree-structured deliberation [R22], self-consistency [R23]) define the capability ceiling the mechanism assumes. The fragility evidence family frames why verdicts with construction-layer root causes need to be kept separate from proposition-face conclusions: symbolic-math perturbation fragility [R24], complete reasoning breakdown on simple tasks [R25], unfaithful chain-of-thought explanations [R26], and stated-vs-actual reasoning divergence [R27]. The Reversal Curse entry [R28] is the registered reference point for the project's direction-consistency readings. A statistical-testing classic [R29] anchors the paired-comparison conventions the verdicts use.

### 7.3 Negative results and reporting norms

The genre this paper belongs to — pre-registered, root-caused negative results with explicitly bounded claims — aligns with the reporting-norms family: troubling trends in ML reporting [R30], reporting standards for evaluation [R31], the perpetual-replication question [R32], inconsistent evaluation practices [R33], underspecification and unpredictable failures [R34], multi-agent emergent-communication negative results [R35], spurious "emergent abilities" as measurement artifacts [R36], and retrieval-augmentation failure modes [R37]. The project's kill-line protocol is a concrete instantiation of this family at the level of an individual research project's internal governance: freeze thresholds first (pre-registration), classify failures by root cause, ban bidirectional extrapolation, and co-report divergent readings.

### 7.4 LLM semantic priors and knowledge-graph completion (V2 lineage)

The GT-4 field-coordination-value and semantic-prior instrumentation descends from the LLM-KGC lineage: in-context KGC with retrieved neighbors [R38], LLM-based KGC [R39], softer-task semantic-prior probing [R40], and grammar-constrained knowledge generation [R41]. The prior manuscript's positioning statements [E59] register the empirical-gap anchors (distribution-level PoA; direction-consistency readings) against this lineage.

### 7.5 Distillation and chain-of-thought learning (V4 face) — slots filled in v0.2

The v0.1 draft of this subsection reserved five slots pending the supplementary literature scan; this version merges the scan's directly-reusable entries [R42]–[R53] (twelve further scan entries registered as "pending verification" are not merged — reserved for PI disposition; 0 placeholder attributions are invented for them). The repository-blank registration stands, re-verified for this draft: a full-text search of the repository's literature-bearing faces — `paper/` and `reviews/` at both the repository root and the workspace mirror, and `docs/` at the repository root — for `distill`, `distillation`, `teacher`, `student model`, and `Hinton` returned **0 hits** (a reader can repeat this search on the public repository; the workspace's internal V3X design directory contains incidental non-bibliographic uses of some of these words — design-document prose, not reference entries). The entries below are the scan's new acquisitions, not repository holdings. Anchor provenance is marked in the References preamble (entries whose anchors this draft completed by its own retrieval are marked †).

**[SLOT-V4-RW-1 — knowledge-distillation lineage: filled.]** The founding anchor [R42] (soft labels / dark knowledge and the temperature parameter; the source of the teacher–student paradigm) is the genealogical starting point of the V4 track's name. The project's use of "distillation" is a track name with a registered meaning that differs from the classical teacher–student compression lineage: any teacher–student statement in this paper takes the classical definition as its point of departure for drawing the boundary — the V4 track's measured object is a rule set's critical internalization of a judgment methodology (§5.1), not a smaller model reproducing a larger model's output distribution.

**[SLOT-V4-RW-2 — chain-of-thought / reasoning distillation: filled.]** The "learning the way of thinking, not the answers" lineage. Distilling step-by-step [R43] trains small models with teacher-generated natural-language rationales as intermediate supervision — "learning reasons rather than labels" — the nearest-neighbor precedent for the V4 track's motivation (the teacher's output is a reasoning basis, not a final answer). The reasoning-teachers entry [R44] names the paradigm in which the teacher provides chain-of-thought and the student acquires reasoning capability; the V4 track's teacher–student division of labor is positioned against it. The Orca program [R45] scales progressive learning from complex explanation traces (imitation of the reasoning process rather than the output alone) — the large-scale contrast case for the "learning the way of thinking" positioning. The on-policy family [R46] trains the student on its own generated distribution with teacher feedback targeted at the student's own mistakes — the closest external neighbor to the track's student-side criticality: the student does not statically imitate the teacher's static outputs; it learns where it itself errs. The registered difference for [R46] is stated with the citation: in that line the teacher is a model and the object is task performance; in the V4 track the teacher is a human expert's judgment events (§5.3) and the success criteria include criticality — non-blind-obedience as a first-class kill-line (TH-v2-5b) — not task accuracy alone.

**[SLOT-V4-RW-3 — expert-judgment elicitation and capture: remains pending.]** The supplementary scan registered no directly-reusable entries for this face; the slot stays open. The collection protocol of §5.3 remains the project's own registered instrument, with 0 external lineage claimed for it.

**[SLOT-V4-RW-4 — criticality and adherence measurement: filled.]** The imperfect-teacher entry [R47] frames the distillation dilemma under an imperfect teacher ("learn or not learn", as a unified framework) — the direct external anchor for the track's student-critical, non-blind methodology, and a comparison frame for the blind-obedience metric. The sycophancy benchmark [R48] is the main external reference frame for the blind-obedience construct, with the registered direction distinction attached to the citation: that line measures model-toward-user pandering; the V4 track measures student-toward-teacher blind obedience — different direction, same mechanism family. The sycophancy-measurement critique [R49] (existing measurements conflate related behaviors and lack operational definitions) is external support for the methodological stance of §3 and §5.2: adherence metrics require operational definitions frozen before measurement.

**[SLOT-V4-RW-5 — behavioral profiling and its limits: remains pending.]** The supplementary scan registered no directly-reusable entries for this face; the slot stays open. The anti-profiling boundary (§5.1) stands as a registered project constraint independently of the slot's status.

**Cross-face additions (V3×V4 positioning; merged with this subsection per the scan's cross face).** The rational-players entry [R50] systematically tests LLM rationality in game-theoretic tasks — the benchmark anchor for game-theory-as-lens-for-LLM-evaluation, with the registered division of labor: that line tests strategic rationality; this paper's V3 track tests the validation of a mechanism's distortion bounds with LLM players (§4.1). The Alympics framework [R51] provides game-theory arenas for LLM agents — the engineering precedent for structuring LLM behavior under game-theoretic frameworks. The strategic-behavior study [R52] reports LLM behavior under incentive structures — external evidence in the same lineage as the V3 track's use of game structure to explain LLM behavior. The pre-registration entry [R53] argues for freezing hypotheses and criteria before running and reporting outcomes as-found, including negative results — the most direct external anchor for the kill-line protocol's methodological family (§3).

**Registered not-found statements (transcribed from the supplementary scan; 0 fabrication).** (1) A dedicated literature pairing pre-registered decision rules / kill-lines with LLM evaluation was not found — the protocol's methodological differentiation is stated as such, with [R53] (pre-registration in predictive modeling) and [R49] (measurement critique) as the nearest neighbors. (2) A direct combination of distillation and game-theoretic validation was not found; the two tracks' respective literatures are rich and their intersection is not. (3) "Critical distillation" as a term has no established literature; this paper's usage is the project's registered self-coined term ("critical learning", §5.1), defined in-text with 0 attribution to an existing literature.

---

## 8 Discussion: what these negative results mean, and what they do not

**The register of outcomes.** Across the two tracks, the sealed record is: V3 — gt5 FAIL (root cause: mixed); #26b FAIL (fake falsification); #35 v2 and v3 FAIL (fake falsification); C5 claim FAIL (fake falsification); P-J/P-M/P-C KD; the P-B distortion-bound experiment blocked on a missing theory input; five construction-face PASS legs in the GT family; a T-1 gate closed with an unresolved domain divergence. V4 — Task B v1/v2/v3 FAIL (with the root-cause composition shifting from construction-dominated to compound); N-26's real-falsification direction on the metadata-indistinguishability line; S3 PASS/PASS/KD; a six-model cross check placing the failure in the construction layer with cross-robust evidence; S4 deferred and unfrozen.

**What the FAILs mean.** Under the protocol's root-cause discipline, a FAIL with a fake-falsification root cause is a *finding about the experiment*, stated as such, with the failure point localized and recomputable. It is not a finding about the proposition. This is the paper's central methodological claim: negative results become scientifically usable when their production chain is auditable and their root cause is classified, and they become misleading when either condition fails. The #35 family is the cleanest demonstration: the v2 construction was improved to dissolve a registered confound (C0), the v3 re-run still closed FAIL, and the verdict file itself locks the external statement to a sentence that names the construction face and forbids both "the proposition is dead" and "the proposition holds".

**What the FAILs do not mean (the extrapolation bans as an epistemic boundary).** The bidirectional bans (Rule 6) cut both ways, and the paper reports them as load-bearing: Task B's FAIL chain is construction-domain-limited and is not extrapolated to "the PI's chain of thought is not distillable"; N-26's real-falsification line does not license "completely indistinguishable"; C5's FAIL does not license "the coordinate-collapse proposition is dead"; and symmetrically, no construction-face PASS — gt6, gt8, gt5b, GT-4, GT-1, the T-1 gate closure, S3's two PASS limbs, T1.5r2's robustness — is extrapolated to any real-face claim.

**The verdict is not the reading.** The T1 → T1.5 → T1.5r2 chain shows that a literal PASS can be a construction-failure artifact (T1: 49.3% empty responses producing J = 0.0 as empty–empty agreement), and the same literal can carry three different root-cause tiers across three constructions. The registered lesson is a reporting rule this paper adopts wholesale: no measurement reading enters the text without its root-cause attribution.

**Honesty as an institutional mechanism, not a disposition.** The fake-verdict case (§6) closes the loop: the protocol's machinery (three-state verdicts, root-cause classification, append-only correction, role separation) was applied to the verdict chain itself when a tool produced a false kill, and the re-registration went through the same root-cause path (fake falsification, tool face) rather than any softening path. The case is the paper's answer to the question a skeptical reader will ask of any negative-results report: *what happens when your own instrumentation produces the result you are least disposed to publish?* The registered answer: it gets forensically attributed, re-registered as restored, and reported in the register anyway.

---

## 9 Limitations and honest accounting

1. **This is a draft, not a peer-reviewed artifact.** The target vehicle is an arXiv preprint (v1 lineage precedent: 0 peer-review record); this draft has had no external review. The prior preprint's abstract and negative-results face were not read for this draft (existence registered only), so no cross-artifact consistency claim is made between this draft and that preprint's content.
2. **Transcription layer.** All case readings were transcribed through the project's internal verification layer (the 2026-10-12 working briefs), each anchored to sealed on-repository artifacts; 65 anchors were independently re-measured for this draft itself (63 matched; two registered divergences — the E20 runner copy (drift row C-26) and the S3 missing-field backfill rule draft (registered `2e77a13e51f1` vs measured `8496a53d183a` / 35,827 B) — are co-reported with 0 adjudication), and the remainder carry the layer's registered values with 0 re-measurement here. Where a fingerprint has multiple registered readings (the D8 questionnaire, the S3 verdict, the P-B specification, the #32 runner copy), the readings are co-reported (Appendix C).
3. **Two FTFB/artifact faces unread.** The FTFB prior artifact [E61] and the arXiv preprint PDF are registered by existence and fingerprint only; per the read-before-cite rule, 0 content claims are made about either.
4. **V4-facing related work is partially filled.** The supplementary literature scan's directly-reusable entries fill slots 1, 2, and 4 plus the cross face (§7.5); slots 3 and 5 remain pending (the scan registered no directly-usable entries for those faces, and none are fabricated for them), and the scan's twelve pending-verification entries are reserved for PI disposition.
5. **Coverage boundary.** The judgment set covered here is the verification layer's registered case set. The repository registers additional judgment artifacts not covered in this draft (a P-1 re-run family registered in the project's clue ledger; the pre-10-01 verdict faces outside that layer's scope), and post-2026-10-01 verdict faces (the five-terminal-vocabulary era) are outside this draft's coverage.
6. **Count discipline.** Counts are quoted with their time points; the repository's historical three-directory counts are registered as 2026-09-26-era values and are not used as current values anywhere in this draft.
7. **Unreconciled divergences remain unreconciled.** Appendix C lists the divergence register; none is resolved in this draft, and several are explicitly reserved to the PI (the K-V3S-3-1 domain priority; the #35 v3 effectivity ruling; the three-caliber count).
8. **Authorship, affiliation, and acknowledgment literals are withheld** pending the PI's final review; no funding source is named.
9. **The S3/T-1 domain difference** (180 vs 186 entries; 6 vs 7 days) is reported side by side with 0 reconciliation; the 39 entries lacking `event_id` make distinctness unverifiable, per the T-1 verdict's own honest-accounting register.

---

## 10 Conclusion

The Deposon project set out to validate a game-theoretic mechanism against LLM players (V3) and to distill a human expert's way of thinking into an AI-usable rule set (V4). Both tracks closed predominantly negative — a FAIL register spanning claim-level verdicts, formal distillation verdicts, and a real-falsification direction on one supplementary line — with the mechanism-level distortion-bound experiment blocked on a missing theory input and the held-out distillation segment deferred. The paper's contribution is the register itself, together with the protocol that makes it trustworthy: kill-lines frozen before experiments; three-state verdicts with mandatory root-cause triage; bidirectional extrapolation bans; divergent readings co-reported without resolution; role-separated, append-only, hash-anchored evidence chains; and a demonstrated willingness to apply the same machinery to the verdict chain when it produces a false kill. Negative results are where a falsifiable program proves it was falsifiable; the discipline that produces them honestly is the result this paper reports.

---

## References

*(V3-facing and genre-facing entries are transcribed from the project's verified reference base [E57][E58][E62] in the base's registered form; full bibliographic strings live in the base. Entries [R1]–[R41] are the v0.1 base, unchanged. The v0.2 additions [R42]–[R53] merge the supplementary literature scan's directly-reusable entries (scan registered 2026-10-12, with its own two-source verification standard); values marked † were completed by this draft's own web retrieval on 2026-10-12, each cross-checked against at least one official page — an arXiv abstract page, the ACL Anthology, a publisher site, or the paper's official repository — with 0 memory fills; unmarked values carry the scan's registered anchors as-is. The scan's twelve "pending-verification" entries contribute no entries here.)*

- [R1] Monderer & Shapley, GEB 1996 (potential games).
- [R2] Rosenthal 1973 (congestion games).
- [R3] Sandholm 2010 (population best-response dynamics).
- [R4] Candogan et al., MOR 2011 (flow decomposition of games).
- [R5] Parise & Ozdaglar, Econometrica 2023 (graphon limits).
- [R6] Jackson & Wolinsky 1996.
- [R7] Fabrikant et al. 2003.
- [R8] Ma et al., TCS 2014.
- [R9] Waniek et al., Nat. Hum. Behav. 2018, and Stackelberg edge hiding 2023.
- [R10] Koutsoupias & Papadimitriou 1999.
- [R11] Roughgarden & Tardos 2002 (affine congestion PoA = 4/3).
- [R12] Christodoulou et al. 2014.
- [R13] Benita 2020 (distribution-level PoA precedent).
- [R14] Conitzer & Sandholm 2006.
- [R15] Dekel et al. 2010.
- [R16] Hardt et al. 2016.
- [R17] Dütting et al., WWW 2024.
- [R18] Raji et al. 2020.
- [R19] Jia et al. 2021 (Proof-of-Learning).
- [R20] Wei et al., "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models," NeurIPS 2022 (eprint 2201.11903).
- [R21] Kojima et al., "Large Language Models are Zero-Shot Reasoners," NeurIPS 2022.
- [R22] Yao et al., "Tree of Thoughts: Deliberate Problem Solving with Large Language Models," NeurIPS 2023.
- [R23] Wang et al., "Self-Consistency Improves Chain of Thought Reasoning in Language Models," ICLR 2023.
- [R24] Mirzadeh et al., "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models," ICLR 2025 (eprint 2410.05229).
- [R25] Nezhurina et al., "Alice in Wonderland: Simple Tasks Showing Complete Reasoning Breakdown in State-of-the-Art Large Language Models," arXiv preprint 2406.02061, 2024.
- [R26] Lanham et al., "Measuring Faithfulness in Chain-of-Thought Reasoning," TMLR 2023.
- [R27] Turpin et al., "Language Models Don't Always Say What They Think," NeurIPS 2023.
- [R28] Berglund et al., ICLR 2024 (Reversal Curse).
- [R29] McNemar 1947 (statistical note on the comparison of paired proportions).
- [R30] Lipton & Steinhardt, CACM 2019.
- [R31] Dodge et al., EMNLP 2019.
- [R32] Recht, ICML 2019.
- [R33] Tevet & Berant, EACL 2021.
- [R34] D'Amour et al., JMLR 2022.
- [R35] Lazaridou et al., NeurIPS 2021.
- [R36] Schaeffer et al., NeurIPS 2023.
- [R37] Mallen et al., ACL 2023.
- [R38] KICGPT, Findings of EMNLP 2023.
- [R39] KG-LLM / Yao et al., ICASSP 2025.
- [R40] Wadhwa et al., ACL 2023.
- [R41] MKGL, NeurIPS 2024.
- [R42] Hinton, Vinyals & Dean, "Distilling the Knowledge in a Neural Network," arXiv:1503.02531, 2015.
- [R43] Hsieh, C.-Y., et al., "Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes," Findings of ACL 2023.
- [R44] Ho, Schmid & Yun, "Large Language Models Are Reasoning Teachers," ACL 2023 (arXiv:2212.10071†; arXiv ID completed by retrieval).
- [R45] Mukherjee, S., et al., "Orca: Progressive Learning from Complex Explanation Traces of GPT-4," arXiv:2306.02707, 2023.
- [R46] Agarwal, R., Vieillard, N., et al., "On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes," ICLR 2024 (arXiv:2306.13649; poster year completed by retrieval†).
- [R47] Zhou, Y., & Ai, W., "Teaching-Assistant-in-the-Loop: Improving Knowledge Distillation from Imperfect Teacher Models in Low-Budget Scenarios," Findings of ACL 2024, 2024.findings-acl.17 (full title and author list completed by retrieval†; the scan's short title "Improving Knowledge Distillation from Imperfect Teacher" is a truncation of it).
- [R48] Sharma, M., Tong, M., et al., "Towards Understanding Sycophancy in Language Models," ICLR 2024 (arXiv:2310.13548†; arXiv ID completed by retrieval).
- [R49] Batzner, J., "Sycophancy Claims about Language Models: The Missing Human-in-the-Loop," ICLR 2025 Workshop on Bidirectional Human-AI Alignment (tiny paper) (arXiv:2512.00656†; arXiv ID and full title completed by retrieval; the scan's title "…The Missing Measurement" is a short form of it).
- [R50] Fan, C., et al., "Can Large Language Models Serve as Rational Players in Game-Theoretic Tasks?," AAAI 2024 (arXiv:2312.05488).
- [R51] Mao, S., et al., "ALYMPICS: LLM Agents Meet Game Theory," ACL 2025.
- [R52] Lorè, N., et al., "Strategic behavior of large language models and the role of incentives," Scientific Reports, 2024, article 18490 (arXiv:2309.05898†; volume completed by retrieval).
- [R53] Hofman, J. M., et al., "Pre-registration for Predictive Modeling," arXiv:2311.18807, 2023.

---

## Appendix A — Evidence ledger (path + sha256[:12] + bytes)

**Conventions.** Paths beginning `results/`, `docs/`, `reviews/`, `README_V4` are relative to `_september_workspace/` (the mirror-clone location of the registered remote paths); paths beginning `paper/` are relative to the repository root. "✔" marks anchors independently re-measured for this draft (2026-10-12, at clone HEAD `f44996fbfd9f386299442924f70585bb20d935fc`; 65 anchors re-measured, 63 matched, and 2 registered divergences — E20 and E56, both co-reported with 0 adjudication; the review-side measurements were taken at a later clone HEAD (`72c5839…`, per the V3 review's registration), and all drift-class anchors are dual-registered so that a reader re-measuring at any later HEAD can compare against both values). Values without ✔ are registered measurements transcribed with 0 re-measurement. The remote-registered column carries git blob sha1 (40-hex, truncated here) values only where they are the sole available anchor; local sha256 and remote blob sha1 are never interconverted. Readings in the body text were produced through a drafting-side verification layer (the project's internal working briefs of 2026-10-12, which measured their anchors at the same HEAD); that layer is not part of the repository and is not needed to check this paper — every reading resolves to the repository files listed here, and the layering is disclosed for provenance only.

| # | Path | sha256[:12] | Bytes | Note |
|---|---|---|---|---|
| E01 | `results/_v5_gt_verdict_2026_09_29.md` | `45648b0ec940` | 57,227 | ✔ GT five-case verdict |
| E02 | `results/_v5_gt5_gt6_gt8_gt5b_gt_prereg_2026_09_28.md` | `2505ff5d203f` | 63,447 | ✔ GT pre-registration |
| E03 | `results/_v5_gt_exec_2026_09_29.md` | `9a679f43f796` | 27,701 | ✔ GT executor file |
| E04 | `results/_v3_recheck_26b_verdict_2026_10_01.md` | `8bbecb15b28b` | 26,309 | ✔ #26b verdict |
| E05 | `results/_v3_recheck_26b_verdict_prep_2026_10_01.md` | `3aab3f7660fc` | 36,133 | ✔ #26b verdict-prep |
| E06 | `results/_v5_item35_v2_verdict_2026_09_29.md` | `b59bef293712` | 26,232 | ✔ #35 v2 verdict |
| E07 | `results/_v5_item35_prereg_v2_2026_09_28.md` | `1fb2419c6e96` | 35,633 | ✔ #35 v2 pre-registration |
| E08 | `results/_v5_item35_v3_collinear_verdict_2026_10_01.md` | `363cce3dae59` | 38,266 | ✔ #35 v3 verdict |
| E09 | `results/_v5_item35_v3_collinear_prereg_2026_09_29.md` | `873652fd39dd` | 42,504 | ✔ #35 v3 line-setting file |
| E10 | `results/_v5_item35_v3_collinear_recompute_2026_10_01.json` | `a210e2c41275` | 49,682 | ✔ #35 v3 independent recompute |
| E11 | `results/_v5_confirm_b9_decisions_register_2026_09_29.md` | `8c510cda6014` | 17,008 | ✔ #35 v3 verdict §0 cited file |
| E12 | `results/c5_b_group_verdict_2026_10_01.md` | `3fbf6b38a383` | 30,118 | ✔ C5 B-group verdict (on-disk final; the first draft's self-report `c2b90999a788`/29,815 B superseded per the self-fingerprint rule) |
| E13 | `results/_v5_v3_deg_fix_prereg_2026_09_29.md` | `98286cc1aec7` | 41,622 | ✔ C5 pre-registration |
| E14 | `results/_v5_pjpm_pc_verdict_bang3_2026_09_29.md` | `1814f9590f0f` | 41,566 | ✔ P-J/P-M/P-C verdict |
| E15 | `results/_v5_pjpm_pc_deg_prereg_2026_09_29.md` | `989ee2bce660` | 59,446 | ✔ P-J/P-M/P-C pre-registration (PI-reviewed effective) |
| E16 | `results/_v3n_cpath_live_rerun_verdict_2026_10_01.md` | `a91efbfec3d0` | 16,409 | ✔ #32 live-rerun registration file |
| E17 | `results/_v3_n_recheck_llm_verdict_2026_09_27.md` | `426cfe18cf65` | 21,332 | ✔ #32 prior verdict (byte-untouched) |
| E18 | `docs/V3X/CPATH_SIMULATION_REPORT_2026_09_10.md` | `de772cd9e7ba` | 6,825 | ✔ 2026-09-10 simulation report |
| E19 | `results/_v3_n_cpath_live_data_2026_09_27.json` | `25374af92f88` | 12,711 | ✔ #32 live data (path corrected in v0.3: the v0.1/v0.2 form `_v3n_cpath_live_data…` was a one-character path typo; the values were unchanged and are verified at the correct path) |
| E20 | `deposon_team/plugins/_v3n_cpath_live_rerun_2026_10_01.py` | current `7d8d26174ce9` | 22,133 | ✔ #32 runner copy — **dual-value registration**: the verdict file's in-file registration (10-01) reads `3e932a5409b5` / 20,831 B; the current disk copy (measured for this draft, 2026-10-12; the reviews measured the same value) reads `7d8d26174ce9` / 22,133 B (drift +1,302 B, attributed to a post-registration append; the registered value is not a fabrication — it appears in four on-disk files; drift row C-26) |
| E21 | `results/_t1_gate_closure_and_recompute_verdict_2026_10_01.md` | `caf20d1fa538` | 72,926 | ✔ T-1 gate closure verdict |
| E22 | `results/_v3_s_prereg_v1_2026_09_27.md` | `ef5a40554960` | 46,836 | ✔ protocol-face threshold-literal unique source |
| E23 | `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | clone `aab9d78ada2d` | 15,549 | ✔ P-B spec (clone, desensitized; local original `423c84de20d5` / 15,457 B; two further historical size registrations co-exist — Appendix C) |
| E24 | `results/_c4_theory_source_caliber_correction_2026_09_30.md` | clone `1f058d9cb7a8` | 25,138 | ✔ C4 caliber correction (clone; local original `61b139efd0ef` / 25,022 B) |
| E25 | `results/_c4_reply_intake_acceptance_register_2026_10_01.md` | remote blob sha1 `21ad9581c0ec…` | 33,728 | 0 local read; remote-registered value transcribed from the 461-file inventory |
| E26 | `results/_v5_theory_input_acquisition_request_2026_09_29.md` | clone `19099ecb3c46` | 10,751 | ✔ theory-input acquisition request (clone; local original `83afc4802fe7` / 10,691 B) |
| E27 | `results/_fake_verdict_reverify_sixitem_ledger_2026_09_30.md` | `41d7b76ea4d6` | 40,957 | ✔ fake-verdict re-review six-item ledger |
| E28 | `results/_v5_fake_verdict_forensics_2026_09_28.md` | `1b135d8b1e08` | 35,870 | ✔ forensics file |
| E29 | `results/_v5_fake_verdict_session_log_2026_09_28.md` | `132bfa0c02f5` | 18,877 | ✔ session log |
| E30 | `results/_v5_fake_verdict_v1x_prereg_2026_09_28.md` | `088085d6c90d` | 28,484 | ✔ v1.x pre-registration |
| E31 | `results/_fake_verdict_session_log_reverify_2026_09_30.md` | `c14094bdf815` | 25,953 | ✔ re-verification session log |
| E32 | `results/deposon_v20_gt5.json` / `_gt6.json` / `_gt8.json` / `_gt5b.json` / `_gt.json` | `fca14c5735dd` / `04b90b638bdc` / `2b88948dca19` / `2907006dbe48` / `497b9c2d6746` | 72,647 / 65,105 / 5,396 / 56,425 / 3,803 | ✔ GT historical JSONs (byte-untouched) |
| E33 | `results/_v4_pi_cot_v2_prereg.md` | `cc25c5149ce1` | 4,247 | ✔ Task B v2.2 pre-registration (goal + triad + TH-COT-v2) |
| E34 | `results/_v4_pi_cot_v2_verdict.md` | `eb9ad4193cf2` | 22,340 | ✔ Task B v1 verdict (exploratory; the file's name carries the v2 family prefix — the v1 verdict per the track record) |
| E35 | `results/_v4_pi_cot_v2_verdict_v2.md` | `5d79e67a4e9d` | 33,723 | ✔ Task B v2 verdict |
| E36 | `results/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` | `ba4d07bd7000` | 26,637 | ✔ v2 signoff |
| E37 | `results/_v4_pi_cot_v3_verdict_v3.md` | `bb44fdc7ab0f` | 53,751 | ✔ Task B v3 verdict |
| E38 | `results/_v4_pi_cot_v3_verdict_v3_signoff_2026_09_27.md` | `41d29f4deb70` | 42,157 | ✔ v3 signoff |
| E39 | `results/_v4_supp_l14v3_n26_verdict.md` | `df6453d57f8a` | 65,978 | ✔ N-26 verdict (an older registration of 64,485 B co-exists, difference registered) |
| E40 | `results/_s3_kv3s_3_verdict_2026_10_01.md` | `e394bb6b5ddf` | 35,037 | ✔ S3 verdict (10-01 registered `b3ea36a24dcf` / 35,022 B; 2026-10-12 correction-wave overwrite, verdict tier and readings unchanged) |
| E41 | `results/_s3_kv3s_3_full_recompute_2026_10_01.md` | `b0123f161c10` | 22,183 | ✔ S3 recompute/materials file |
| E42 | `results/_v3_s3_collection_brief_2026_09_28.md` | `d5ba1161e37f` | 19,045 | ✔ S3 collection brief (S3-F1 loader defect; ceiling readings) |
| E43 | `results/_v4_supp_t1_verdict.md` | `0ad42625f333` | 29,106 | ✔ T1 verdict |
| E44 | `results/_v4_supp_t15_verdict.md` | `3cb5c2f59961` | 54,377 | ✔ T1.5 verdict |
| E45 | `results/_v4_supp_t15r2_verdict.md` | `963725dbd82a` | 65,638 | ✔ T1.5r2 verdict |
| E46 | `results/_v4_track2_multimodel_verdict_2026_09_23.md` | `44d9bad9039b` | 12,883 | ✔ Track 2 multi-model verdict |
| E47 | `results/_v4_pi_cot_v2_questionnaire_v1.md` | `7b14cdb31d21` | 12,402 | ✔ collection questionnaire v1 (§0 six rules) |
| E48 | `results/_v4_pi_cot_v3_questionnaire_v2_d8_2026_09_28.md` | `7656be1d287f` | 53,583 | ✔ D8 main questionnaire (10-01 registered `238077d25919` / 53,581 B; remote blob sha1 `de3da25bc7a8…` / 53,583 B) |
| E49 | `results/_d8_supplement_open_questions_2026_09_30.md` | `aa07872e4cab` | 24,835 | ✔ SQ supplement (10-01 registered `579b375e9508` / 24,833 B; remote blob sha1 `0da60b9a1de6…` / 24,835 B) |
| E50 | `results/_d8_closeout_protocol_recompute_2026_09_30.md` | `57aba2cd26a6` | 31,007 | ✔ T-SUP-2 closeout recompute |
| E51 | `results/_v4_pi_cot_v3_dataset.json` | `5118f5b44f17` | 16,025 | ✔ v3 dataset (privacy face: path + SHA + bytes only) |
| E52 | `results/_v4_pi_cot_v2_dataset.json` | `7b01cd835a41` | 12,672 | ✔ v2 dataset (privacy face) |
| E53 | `results/_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json` | `769ef8b71462` | 374,072 | ✔ D8/SQ addendum (privacy face: fingerprint-only verification) |
| E54 | `results/_v4_pi_cot_v3_dataset_addendum_s3_d1fill_2026_10_01.json` | `b9026cbf5ca2` | 46,909 | ✔ S3/D1-fill addendum (A11 privacy face: 0 read, 0 content claims) |
| E55 | `results/_d8_collection_ledger_2026_09_30.md` | `031dd8429048` | 20,290 | ✔ collection ledger (original-wording preservation) |
| E56 | `results/_s3_missing_field_backfill_rule_draft_2026_10_01.md` | registered `2e77a13e51f1`; this draft's measurement `8496a53d183a` | 35,827 | **divergence registered** (registered-value vs 2026-10-12 measurement; 0 adjudication; draft pending PI in any case) |
| E57 | `paper/deposon_paper_final_en.md` | `2ec20b96e941` | 68,164 | ✔ prior EN manuscript (reference base; head + References read for this draft) |
| E58 | `paper/references.bib` | `f5a6a850e203` | 14,914 | ✔ BibTeX ledger, 37 entries |
| E59 | `paper/v2/related_work_v2X.md` | `7fb001add973` | 10,114 | ✔ related-work positioning statements |
| E60 | `results/deposon_g1_mindmap_demo.json` | `55428f6bd848` | 3,041 | ✔ G1 mind-map anchor (dual-address same fingerprint; a `.json` anchor, not the mind-map body itself) |
| E61 | `results/_archive_2026_09_20/fiction_that_feeds_back.pdf` | `2d9edc8c7303` | 356,123 | ✔ FTFB prior artifact, 23 pages — existence registration only, 0 content citation (read-before-cite rule); a registered divergence exists between the commission materials ("remote not directly accessible; attachment required") and the clone mirror's presence of the file — co-reported, 0 adjudication |
| E62 | `docs/REF_VERIFICATION_v2.md` | `64f0a3772c12` | 5,860 | ✔ reference verification record (2026-08-30: [21] corrected; [52]–[59] verified) |
| E63 | `reviews/literature_scan_v2X_A.md` | `d0bba9379b4b` | 18,876 | ✔ literature scan A (40 entries, cluster-level use only) |
| E64 | `reviews/literature_scan_v2X_B.md` | `313b30815a39` | 30,468 | ✔ literature scan B (41 entries vs a self-declared 40 — discrepancy registered, 0 adjudication; cluster-level use only) |
| E65 | `README_V4_2026_09_29.md` | `15648ca22a00` | 58,646 | ✔ V4 README — the "#32 rerun" release record cited in §4.4.7 (added in v0.3) |

**Lineage anchors registered by existence only (0 content citation).** The V1+V2 arXiv preprint: arXiv:2609.09001, v1 only (no v2), 0 peer-review / 0 acceptance record, 23 pages / 5 figures, DOI 10.48550/arXiv.2609.09001, CC BY 4.0, code repository `github.com/zeroandcat/Deposon` (external statements defer to the PI's GitHub as the sole authoritative source); the preprint's abstract and negative-results face were not read for this draft. The unit/affiliation literal is pending the PI's final review (default: 0 transcription). The four core principles registered in the project's commission materials (which precede and run through the V1–V2 publication practice, not originating from its chapters) are not elaborated here.

---

## Appendix B — Verdict vocabulary, terminology compliance, and hard-constraint mapping

### B.1 Verdict vocabulary time layering

All judgment cases in this paper are 2026-10-01-or-earlier faces, quoted in the original three-state vocabulary (PASS / FAIL / KD). The five-terminal vocabulary introduced by the PI on 2026-10-10 (`pass / af (artifact-free) / kd (known defects) / fail / give-up`; overlap priority `af > kd > give-up`; non-five-terminal outcomes count as hung items, not verdicts) governs verdict faces after 2026-10-01 and is reported here only as a protocol evolution (Rule 11). No post-10-01 verdict face is covered in this draft.

### B.2 Terminology compliance summary (the 17-item register, applied)

1. The V1+V2 artifact is described only as an "arXiv preprint" (v1, 0 peer-review record); 0 occurrences of "published / accepted / merged / peer-review passed".
2. Target vehicle: arXiv preprint, cs.AI primary classification; 0 journal template, 0 designated submission target, 0 claim of any submission intent.
3. The prior preprint's abstract and negative-results face: existence registration only.
4. Unit/affiliation literals: pending PI final review; 0 transcription; the author block is a placeholder.
5. Track names V1–V4 are used exactly as PI-designated main-line names; 0 use as ordinary stage numbers; 0 new stage names coined.
6. The four core principles are registered as preceding and running through the V1–V2 publication practice; 0 statement that they originate from the V1–V2 paper chapters.
7. The FTFB artifact is registered by fingerprint only; 0 content description (read-before-cite rule); its side files (`.tex` / `_source.md`) are neither cited nor used as structural templates.
8. Dataset/privacy faces: reasoning full texts 0 quoted; dataset JSONs cited by path + SHA-12 + bytes only.
9. All existing files were read-only for this draft; 0 modification, 0 renaming, 0 relocation.
10. Counts are quoted with time points; the historical three-directory counts are not used as current values.
11. Desensitized entity literals: 0 restoration; mapping literals are not reproduced; the desensitization-relevant entity families are not named at all.
12. 0 fabrication of remote sha1 / path / file counts / clauses; unexecuted actions are marked "not executed"; 0 claims of upload/push/remote-write/receipt.
13. Third-party conclusions are quoted in quotation form; 0 use of any drafting-collaboration agent identity as an attribution name; agent identities do not appear in the paper.
14. 0 delivery-channel instructions; no archive-zone material; 0 credential handling.
15. Verdict vocabulary per the time layering of B.1.
16. Conclusions are checkable (path + SHA-12 + bytes); negative conclusions carry root causes; divergences are co-reported; gaps are stated; fingerprints are self-checked without self-reference (this draft's own fingerprint is not written into the draft).
17. Internal sensitive faces (including the teacher face) are not transcribed anywhere in this draft.

### B.3 Hard-constraint compliance (H1–H12 of the commission letter)

H1 (0 secrets/credentials/session ids/agent rosters/personal information) — compliant; H2 (attribution by quotation; 0 impersonation) — compliant; H3 (0 fabrication; read-before-cite; "not found → pending PI" is the accepted form) — compliant (FTFB and the arXiv PDF are the two unread faces, marked as such); H4 (0 outline, 0 structural constraints — structure is this draft's own design) — compliant; H5 (kill verdicts unsoftened; the banned connective list is not attached to any verdict statement) — compliant; H6 (bidirectional extrapolation bans enforced at every FAIL and every construction-face PASS) — compliant; H7 (0 threshold adjustment; all TH-*/K-* literals quoted from the pre-registrations) — compliant; H8 (privacy faces: path + SHA-12 + bytes only) — compliant; H9 (0 automatic effectivity; nothing in this draft takes effect by itself; adoption is the PI's action) — compliant; H10 (counting discipline; D1-tier counts used with time points; 0 stale counts as current values) — compliant; H11 (0 half-conclusions; all registered divergences co-reported) — compliant; H12 (0 touching of existing files; this draft is a newly created file) — compliant.

---

## Appendix C — Divergence register (consolidated; all entries unresolved, 0 adjudication)

| # | Face | Reading A | Reading B (…) | Status |
|---|---|---|---|---|
| C-1 | K-V3S-3-1 measurement domain | whole-event domain: 7 days ⇒ PASS | old accounting domain: 3 days ⇒ FAIL | undecided, reserved to PI/protocol; the verdict file pre-registers no softened phrasing for the FAIL contingency |
| C-2 | S3 vs T-1 substrate accounting | T-1 recompute: n_after = 186 / 7 days / 0.516129 | S3 verdict: 180 entries / 6 days / 0.5000–0.5333 | two sealed verdict artifacts, different domains, co-reported |
| C-3 | #35 v3 effectivity | batch-9 register §1.1 "effective" | batch-9 register L11/L197 "pending review" | internal self-contradiction, 0 reconciliation; conditional blank: a PI re-ruling ⇒ verdict re-ruled KD |
| C-4 | #26b file-level verdict | M1 (main reading) FAIL | R1 (pure literal) PASS | genuine divergence, co-reported; R1 not adopted (placeholder literal, no effective-freeze trace) |
| C-5 | three-caliber count | 77 | 74 / 62 | 0 selection |
| C-6 | `matrix.operator` attribution | — | — | reserved to PI (R-01) |
| C-7 | D7 gate-one authoritative distribution | distribution A | distribution B (swapped) | authority undecided (U-7) |
| C-8 | legacy paper-file fingerprint | `8baa9854b3f7` / 239,700 B | third-party self-report `fd39cf811232` / 236,425 B / 1,396 lines | attribution 0 asserted (line-ending/encoding/version/carrier all possible) |
| C-9 | B-8 F4 anchor value / B-9 two strings | reading 1 | reading 2 | not verified, registered as pending PI |
| C-10 | C5 unclosed items | U-V04-01 protocol-version carrier gap | §4.4 min/max/std unreported | registered (→ PI; → worker + verifier) |
| C-11 | 39 entries without `event_id` | "186 = 186 distinct entries" | — | not decidable (T-1 verdict's honest-accounting item 9) |
| C-12 | P-B spec byte size | local original 15,457 | 11,189 / 7,126 historical; clone 15,549 | drift registered, 0 adjudication |
| C-13 | `docs/GT_RECONSTRUCTION.md` | line-setting file registration `570b7bd3e286` / 6,695 B | on-disk measurement `cff15d000d47` / 13,424 B | drift by another role (γ-16), registered |
| C-14 | D8 questionnaire fingerprint | 10-01 registered `238077d25919` / 53,581 B | current disk / remote `7656be1d287f` / 53,583 B | anonymization + correction waves; question-face readings unchanged |
| C-15 | SQ supplement fingerprint | 10-01 registered `579b375e9508` / 24,833 B | current / remote `aa07872e4cab` / 24,835 B | same as C-14 |
| C-16 | S3 verdict fingerprint | 10-01 registered `b3ea36a24dcf` / 35,022 B | current `e394bb6b5ddf` / 35,037 B | 2026-10-12 correction wave; verdict tier and readings unchanged |
| C-17 | N-26 verdict size | older registration 64,485 B | current 65,978 B | difference registered |
| C-18 | S3 backfill-rule draft fingerprint | brief-registered `2e77a13e51f1` | this draft's measurement `8496a53d183a` / 35,827 B | divergence registered, 0 adjudication; draft pending PI in any case |
| C-19 | FTFB remote direct accessibility | commission materials: "not directly accessible; attachment required" | clone mirror: file present | 0 adjudication; content unread either way |
| C-20 | literature-scan B entry count | self-declared 40 | counted 41 | registered, 0 adjudication |
| C-21 | ledger date caliber | event-date field: 6 days | any-date-string rescan: 11 days | two readings co-registered, 0 replacement |
| C-22 | correction-event count | `is_correction=true`: 7 | `correction_confirmed=true`: 2; pair-closure: ≥ 5 (fields `None`) | later expanded by the S3 verdict to seven readings ⇒ KD; 2↔7 undecided at the collection layer |
| C-23 | #32 no-RAG dual caliber | same-extractor re-judged 80.0% | stored original 73.3% | co-reported, 0 selection |
| C-24 | #32 svd2 sign caliber | report §2 | runner literal (one sign convention apart) | 0 ruling on which side is authoritative |
| C-25 | two upload-registration waves | 461-file inventory @ `f44996fb…` | 830-file ledger @ `fb0ee996…` | two waves, 0 mixed use; full mapping not established (267-entry intersection registered) |
| C-26 | #32 runner-copy fingerprint (E20) | verdict-file in-file registration (10-01): `3e932a5409b5` / 20,831 B | current disk (measured 2026-10-12, this draft and the reviews): `7d8d26174ce9` / 22,133 B | drift +1,302 B, attributed to a post-registration append; the registered value appears in four on-disk files (not a fabrication); dual-value registration, 0 adjudication |

---

*End of draft. Prepared 2026-10-12 by the paper's drafting seat (identity withheld per the anonymous-draft convention); all content follows the project's external caliber (v0.6 series); this file's own fingerprint is measured after writing and reported in the delivery note, not written into the file.*
