# Walking with the Verdicts, Keeping the Books: A Five-Line Audit Coordinate System and a Pre-Registered Distillation Program That Formally Failed

**Version**: v0.4 draft (assembled complete draft, md; the v0.4 registration round of 2026-09-28 registers the externally issued re-adjudication record and its evidence carriers, a version-pending deprecation declaration, and a signoff dual-fingerprint note, all in the registration layer with the main text otherwise unchanged, registered in Appendix C), English, arXiv-preprint style
**Working title**: architecture-blueprint candidate 1 of 3; the final title is reserved to the principal investigator (PI)
**Paper scope**: this paper delivers the front matter, Section 1, Part I (Sections 2–8, the coordinate-system zone, merged in full from the unpublished survey source), Part II (Sections 9–16, the verdict-chain zone, migrated from the V4-line source with frozen numbers and literal verdicts), Part III (Sections 17–24, the synthesis zone), the unified references, and Appendices A–C.
**Author block**: Attribution withheld. The author list is reserved to the principal investigator's decision; this placeholder is not an authorship claim.

---

**Literature and claim conventions (merged draft, working).** The coordinate-system material merged as Part I (Sections 2–8) originates in a survey manuscript that was never submitted for publication and will not be submitted; this merged draft is its only public carrier, and its verified reference base of 61 entries (60 external entries plus one disclosed self-citation to the program's first work) is carried into this draft. Bracketed citation numbers follow a single unified first-appearance sequence across the paper: the survey source's 61-entry sequence, with the three V4-line-source entries inserted at their first appearances, renumbered document-wide at assembly. Evidence strength is labeled throughout in three tiers, closed (pre-registered), consistency, motivation only, plus a scope marker; the tier conventions are defined in Section 3.2. Verdict wording (FAIL, hit, TRIGGERED, NOT TRIGGERED, composite qualification) is carried literally from the frozen verdict artifacts; every verdict number in Part II is anchored to a path, a byte count, and a SHA-12 digest in Appendix A of this draft. Two measured-value corrections carried from the independent re-verification of 2026-09-27 (its evidence file is anchored in Appendix A alongside the merged-draft input anchors) are written into the text and annotated inline as drafted errata-chain family E-37 (Sections 13.3 and 14.2, and the Appendix B K-N26-2 row); the errata chain itself is frozen at v19 (E-1 through E-36) and is not modified by this draft. The survey's self-references ("this survey") in Part I refer to the merged survey material of Sections 2–8. For double-blind safety, attribution is withheld throughout, real-name elements of the survey source are not carried into this draft, and the frozen digests of all cited artifacts are unaffected.

---

## Abstract

The third work of a single-investigator program on auditable machine reasoning, this paper merges its two remaining lines into one account. The first is a five-line audit coordinate system for claims about LLM reasoning: auditability as third-party recomputability at stated cost, falsifiability as executability of pre-registered verdicts, and bookkeeping as the commitment-execution-verification loop. Five research lines are surveyed in a uniform template, with failure modes and negative results as first-class content; the assembled five-line by six-attribute matrix shows one sparse column, commitment timing: no line records a run-level, pre-registered verdict protocol. The second is the verdict-anchored record of the distillation phase that formally failed. The registered claim, that an AI system can critically learn the principal investigator's way of thinking, was pre-registered with three mechanical indicators and four kill-lines; all four triggered (mean held-out similarity 0.0909, critique coverage 0.6842, blind-obedience rate 0.3333, bootstrap interval [0.0, 0.2045]), and the FAIL carries a composite root-cause qualification and enumerated non-extrapolation boundaries. A four-stage false-falsification triage pipeline separated construction failure from proposition-level falsification before any falsification was filed; a five-teacher re-run truly falsified the claim that call-side metadata separates distilled outputs from teacher outputs (pooled AUC 0.5663 against a 0.75 line). A 36-entry append-only errata chain, SHA-anchored ledgers, and literal verdict wording make every recorded number independently recomputable. The synthesis maps the failed phase onto the matrix: the verdict chain is a program-level instance of the column the survey found empty. The phase is open at writing time; this draft reports the recorded state and closes nothing.

**Keywords**: auditability; falsifiability; pre-registration; chain-of-thought; verification; reproducibility; distillation; negative results; survey

---

## 1. Introduction

### 1.1 From performance to bookkeeping

Research on the reasoning of large language models organized its first era around performance, and on those terms it succeeded: chain-of-thought prompting gave multi-step problems an explicit intermediate structure [1], and benchmark scores rose with each new organization of the reasoning process. What a benchmark score certifies, however, is an aggregate behavioral claim under a stated protocol, an average over items, seeds, and grading rules, and not the reasoning itself. Two lines of evidence then separated the visible steps from the computation that produced them. The first showed that models do not always say what they think: prompted biases propagate into the answers while the emitted chains rationalize those answers after the fact [2]. The second showed that faithfulness is not a free byproduct of explanation but a quantity that must be measured, by perturbing the emitted chain and testing whether the answer actually depends on it [3]. Once the explanation is separated from the computation, a score computed over the explanation certifies even less than a score over the answer.

The response documented on the survey side of this paper is a regrouping of the reliability frontier from performance claims to audit infrastructure: claims about reasoning that leave behind a frozen record a third party can recompute. The program's first work, an auditable scattering layer over reasoning paths, closes with a sentence that this paper adopts as the axis of its whole coordinate system: "[it] is not more accurate, but it keeps the books, and the books can be recomputed step by step by any third party with double-precision arithmetic" [4]. On the recomputable-books axis, the ledger, not the score, is the unit of trust: what is claimed, what record supports the claim, and what it would cost a stranger to recheck. A claim is on-axis when its support is recomputable by a third party with stated resources; a claim is off-axis when its support is a score, a demonstration, or an assertion.

Why this regrouping now, in three words: scale, replication, incentives. Frontier training runs cannot be re-executed by any single third party; evaluation-based claims have repeatedly lost their support to leakage and reproducibility failures; and score-driven incentives select for claims that are cheap to produce and expensive to check. All three pressures push in the same direction, toward records rather than assertions, and Section 2 develops their historical antecedents. The same pressures motivate the paper's other line, reported in Part II: a research phase that binds its own claims to pre-registered verdicts and treats a formal FAIL as a result to be filed, not a narrative to be managed.

### 1.2 Two lines of one program

This paper is the third work of the program. The first work built an auditable, conservation-guaranteed, game-theoretically tested scattering layer over LLM reasoning paths and fixed the program's evidence conventions (companion study (first work): *An Auditable, Conservation-Guaranteed, Game-Theoretically Tested Scattering Layer over LLM Reasoning Paths*; on-disk anchor `paper/deposon_paper_final_en.md`, 68,164 B, SHA-12 `2EC20B96E941`, measured 2026-09-26; publication identifiers, if any, are per the principal investigator's authoritative records; the work is entered as the first case study in Section 18.1). The second work argued, historically and formally, that fiction feeds back into machine worldviews (companion study (second work): *Fiction That Feeds Back: From Non-Euclidean Geometry to Machine Worldviews*, 23 pp.; submitted to arXiv and, as of the writing day (2026-09-27), on hold; on-disk anchor `results/_archive_2026_09_20/fiction_that_feeds_back.pdf`, 356,123 B, SHA-12 `2D9EDC8C7303`, measured 2026-09-26, writing-day freeze; a revised edition of the second work (its revision R4) was completed on the PI's side on 2026-09-27 and is ready for resubmission to arXiv—this fact is recorded here without predicting the hold's outcome or the resubmission's acceptance; this digest will change when the revised edition is archived, and the citation will be upgraded to the formal arXiv record upon public release). The third work, this paper, merges the program's two remaining lines into a single account: a five-line survey of audit infrastructure for LLM-reasoning claims, developed as an unpublished manuscript and merged in full as Part I, and the verdict-anchored record of the program's V3–V4 distillation phase, which formally failed, migrated as Part II.

The survey side covers claims about LLM reasoning, that is, multi-step generation organized into explicit or implicit intermediate structure (chains, decompositions, search trees, agent traces), and the infrastructure that makes such claims checkable. Five lines, each with a literature of its own, populate the axis:

| Line | Unit of account | Entry points |
|---|---|---|
| L1 Process verification | individual reasoning steps | [5, 6] |
| L2 Chain-of-thought faithfulness | the explanation–computation relation | [2, 3] |
| L3 Evaluation integrity | the evaluation artifact itself | [7, 8] |
| L4 Game-theoretic verification | the incentive structure of verification | [9, 10] |
| L5 Conservation and physical priors | conserved quantities, physical invariants | [11, 12, 13] |

The entry points are each line's classic anchors; the extensions of 2023–2026, including monitoring-era faithfulness evidence, contamination forensics, decentralized and bonded verification, and formal and zero-knowledge verification, enter at their positions in Sections 5–8. Two neighboring territories are deliberately out of scope: training-time documentation practices as such, and policy-level AI governance, neither of which takes the reasoning artifact itself as the audited unit.

The positioning argument can be stated plainly. The adjacent-survey record consists of sub-line surveys, four corners of it: reasoning-chain verification [14]; verification design for test-time scaling, from the verifier-as-reward-model performance perspective [15]; the reliability of LLM-as-a-judge evaluation [16]; and the evaluation of LLMs broadly [17]. Within the verified base, and as of a completed novelty search (2026-09-15, multi-engine, query families recorded in the availability section of the assembled draft), no survey was located that organizes the literature around third-party recomputability across the five lines. The claim is stated in the paper's falsifiable register: it remains falsifiable by a single find, and the day one appears, this document regrades itself to a sub-line survey.

The verdict-chain side reports a pre-registered program phase. The phase began from a question recorded in the program's first-year assets, *how should AI think?*, and the claim under test inherited it: whether an AI system can critically learn the principal investigator's way of thinking, defined at pre-registration as method internalization rather than behavioral profiling. The claim was operationalized as three mechanical indicators (held-out structural similarity, explicit-critique coverage at disagreements, and a blind-obedience rate) with pre-registered thresholds and four kill-lines, a verdict-keeper role that adjudicates without running experiments, and an independent verifier role that signs off on the verdict process; the phase was made falsifiable in the preregistration-revolution sense [18] and under the discipline that a claim is killed before it can be believed [19]. The result is a formal FAIL, reported without softening. The program's own rule, set by the PI on 2026-09-23 and recorded in the verdict documents, is that *honesty equals not misleading*: reporting numbers is "mechanical honesty" and is not sufficient; a verdict must co-present its root-cause distribution and its construction-doubt boundaries, and the verdict wording itself (FAIL, hit, composite qualification, NOT TRIGGERED) must be carried literally. On the evaluation side, game-theoretic analyses of LLM self-judging and human-aligned evaluation [20] sharpen what is at stake when a verdict must be trusted. Section 16 states the full discipline as this paper's writing rules.

### 1.3 Contributions

(i) **Operational definitions and a three-axis taxonomy** (Section 3): auditability as third-party recomputability at stated cost, falsifiability as executability of pre-registered verdicts, and bookkeeping as the commitment–execution–verification loop; an organization axis (five lines L1–L5), an attribute axis (six attributes ①–⑥), and a strength axis (three evidence tiers plus a scope marker), with mutual-exclusion and coverage arguments for the six attributes.

(ii) **A five-line survey in a uniform template** (Sections 4–8): each line surveyed as problems and mechanisms, evidence and failure modes, and matrix-row facts, with failure modes and negative results reported as first-class content.

(iii) **The assembled matrix and cross-line lessons** (Sections 17 and 19): pre-registered kills as trust infrastructure; the economics of verification cost; the recursion bottom of audit stacks; the escrow × capability-claim combination documented as unsystematized; and the sparsity observation, that across the surveyed base no line records a run-level, pre-registered verdict protocol.

(iv) **A verdict-anchored governance trail** for a single-investigator program (Sections 9 and 10): pre-registered kill-lines, literal verdicts, a 36-entry append-only errata chain (E-1 through E-36, accumulated across three append rounds v17/v18/v19), and SHA-anchored asset ledgers (path, byte count, SHA-12) that extend the first work's three-tier evidence conventions into full-chain reproducibility.

(v) **The negative-results core of the V4 phase** (Sections 11–15): the formal FAIL verdict of the critical-learning claim, with all four kill-lines triggered, a composite root-cause qualification, and explicit non-extrapolation boundaries; the N-26 true audit, which falsified the metadata-separability proposition (pooled AUC 0.5663 against a 0.75 line, K-N26-1 and K-N26-3 NOT TRIGGERED); the GLM_2 two-tier record; and the retired first-generation claim, whose v1 FAIL was requalified in the errata chain as a false falsification.

(vi) **A false-falsification triage pipeline** (Section 13): probe, correct, expand, truly adjudicate (T1 → T1.5 → T1.5r2 → N-26), separating construction failure from proposition-level falsification before any falsification is filed, and preserving every standing verdict at every stage.

(vii) **Case studies under full parity and the synthesis map** (Sections 17 and 18): the program's artifacts entered into the same matrix at the same register as the external lines, the first work as a five-line case study and the V4 chain as a program-level instance of exactly the commitment-timing column the survey found empty.

(viii) **The audit outlook** (Section 20): machine worldviews and AI scientists as the next claimants needing books, with open problems stated in the paper's own register, and the V4 phase's open boundary stated as open.

### 1.4 Roadmap

Part I (Sections 2–8) carries the coordinate system: Section 2 gives the historical motivation; Section 3 the concepts and taxonomy; Sections 4–8 the five lines. Part II (Sections 9–16) carries the verdict chain of the V3–V4 phase: the four principles and the practice trail (Section 9), verdict-anchored governance (Section 10), the claims and their adjudication (Sections 11–15), and the writing rules and evidence tiers the chain obeyed (Section 16). Part III (Sections 17–24) synthesizes: the V4 chain mapped onto the five-line matrix (Section 17), case studies under full parity (Section 18), cross-line lessons revisited (Section 19), the outlook (Section 20), limitations (Section 21), data availability and provenance (Section 22), the AI-use disclosure (Section 23), and the conclusion (Section 24). Appendix A anchors every internal asset by path, byte count, and SHA-12; Appendix B carries the kill-line tables literally; Appendix C registers the merge provenance and the interpretation registry. The phase recorded in Part II is open at writing time (2026-09-27); this draft reports the recorded state and closes nothing.

---
# Part I · The Coordinate System

*Provenance: merged in full from the program's unpublished survey manuscript; section numbers and bracketed citation tokens carry that source's numbering (see the conventions above). The survey's self-references ("this survey") refer to the merged survey material of Sections 2-8.*

## 2. Historical motivation: fiction and formal systems feeding back into science

The survey's organization axis did not appear from nowhere. Three episodes in the history of science show formal or fictional systems, built without empirical commitment, flowing back into empirical science, and in each episode the hinge was the same: someone kept the books. This section states the pattern, reads the contemporary drivers as its recurrence, and closes with the falsifiability debate as it stands inside machine learning itself. The program's second companion work (Section 1) develops this loop at full length; its submission status and on-disk anchor are stated there.

### 2.1 Three anchors and the loop pattern

**Non-Euclidean geometry.** Between 1829 (Lobachevsky) and 1854 (Riemann), internally consistent geometries were constructed that denied Euclid's parallel postulate. For roughly half a century they remained, in effect, fiction: formally sound, empirically unclaimed. Gauss reportedly withheld publication for fear of ridicule, and the systems were widely read as logical curiosities rather than candidate descriptions of physical space. Poincaré observed in 1902 that one geometry cannot be more *true* than another, only more *convenient*—the fictional-system attitude, stated as a principle. The loop closed in 1915–1919: general relativity took Riemannian geometry as its language, and the light-deflection measurements put the package into falsifiable contact with the world. What was actually falsified was the incumbent, Euclid-as-physics. The operational residue is permanent; curved-space geometry is now an engineering instrument. The historical scholarship on this geometry–physics interface is documented in [21].

**Boltzmann entropy.** In 1877 Boltzmann attached entropy to a count of microstates, and the probabilistic reading was attacked in its day as an unwarranted fiction—dice games inside physical law. The loop ran long and closed twice. Shannon's 1948 measure of information has the same functional form as Boltzmann's entropy; Jaynes's 1957 recast of statistical mechanics as maximum-entropy inference made the probabilistic fiction into an explicit epistemic calculus applicable across domains [22]; Wigner's 1960 essay named the reverse puzzle, mathematics' "unreasonable effectiveness" in the natural sciences [23]; and Landauer's 1961 principle (erasing one bit dissipates at least kT·ln2) closed the circuit physically: the fictional quantity turned out to be physical [24]. The operational residue is twofold. Information theory became an engineering discipline, and every recomputation this survey discusses acquired a physical floor: rechecking a ledger itself costs energy.

**Robotics.** The word *robot* entered circulation from Čapek's 1920 play *R.U.R.*—a fiction. *Robotics* was coined by Asimov in 1941, also in fiction. Both became the ontology of a real engineering discipline: the discipline's objects, roles, and failure modes are named in vocabulary supplied by fiction before the engineering existed. The scholarship on this exchange is active. Field research examines how fictional and imagined robots structure real human–robot relations and the discipline's self-understanding, particularly in Japan [25]; the deliberate engineering use of fiction as a design method has been systematized as science-fiction prototyping [26]; and fictionality has become a method in innovation research more broadly [27]. The loop in its linguistic form: a fictional coinage supplies the ontology; the engineering discipline supplies the falsifiable claims (real robots fail real tests); the vocabulary survives as the field's working language.

**The loop pattern.** All three anchors exhibit one circuit. (i) An internally consistent system is built without empirical commitment—fiction or formalism. (ii) It is put into falsifiable correspondence with a domain, and somewhere it is actually falsified—or the incumbent assumption it challenges is. (iii) What survives leaves operational residue: methods, vocabulary, invariants. The hinge of the circuit is (ii), and the hinge of (ii) is bookkeeping. On this reading, falsifiability is not a property fictional systems acquire spontaneously; it is infrastructure that someone builds and maintains: a registered prediction, a frozen rule, an external witness. We state the corollary in the survey's own register: a kill protocol is the boundary between hard science fiction and fantasy. A fictional system that pre-registers what would count against it has entered the loop; a fictional system that cannot be killed by any observation has not. The falsifiability debate has since entered machine learning scholarship directly, and §2.3 takes it up.

### 2.2 Contemporary drivers

**Scale.** Frontier models and their training sets exceed any single party's recomputation capacity. The training run cannot be re-executed by a third party at reasonable cost, so behavioral claims rest on evaluations—claims whose support is, at best, a protocol description and a score. The trust geometry inverts: when direct recomputation of the artifact is impossible, the only checkable thing left is the record kept around the artifact.

**Replication.** The audit vacuum has measurable costs. A systematic audit of leakage in machine-learning-based science found information improperly shared between training and evaluation to be widespread, with a taxonomy for spotting it [7]—each leakage instance is a claim whose support did not exist. The reproducibility program—checklists, code and data submission, reporting standards—institutionalized bookkeeping as social infrastructure at a major venue [8]. Both works are audit-infrastructure papers in the strict sense: their subject is survivable claims, not better models.

**Incentives.** When scores are the currency, claims optimize toward scores. Uncheckable claims are cheaper to produce than checkable ones, so the equilibrium drifts toward uncheckable claims (Goodhart-type pressure, present in every measurement-driven field). The concern is the field's own, and it has a lineage: the self-criticism tradition begins with Wagstaff's demand that machine-learning claims connect to measurable consequence [28], and Lipton and Steinhardt's diagnosis gave the incentive distortion its canonical three-symptom reading [29]. The countermeasure is not exhortation but pricing: make the checkable claim the one that pays—by making verification cheap (attribute ③), by making retroactive support visible as such (attribute ⑤), and by making kills reportable without reputational collapse (the register this survey practices).

**Consequence.** The LLM-era need is ledgers, not only scores. A score is a claim; a ledger is a recomputable support. The five lines surveyed next are the places where this consequence is already being worked out—mostly without reference to each other, which is precisely why a shared taxonomy is worth building.

### 2.3 Falsifiability inside machine learning

The philosophical question did not stay in philosophy. Nielson reads machine learning's self-understanding against Popper directly—induction, falsificationism, and what it would mean for a learner's claims to be falsifiable rather than merely fit [30]. Buchholz and Raidl take the complementary route: a falsificationist methodological account of artificial neural networks, asking what ANN research would look like if its claims were organized around refutation rather than accumulation [31]. Both are argument papers, tiered motivation only under the survey's conventions; what they supply is vocabulary and a live question, not measurements.

The survey's position on that question is deliberately thin, and we state it once. The operational reading of §3.1 (verdict executability) is weaker than either Popperian logical falsifiability or its machine-learning-internal adaptations, and it is independent of their outcomes: it asks only whether the bookkeeping around a claim permits mechanical killing. If the philosophical program succeeds—whatever success turns out to mean for it—the operational reading is unchanged; if it fails, the operational reading is still the engineering practice this survey documents across five lines. The historical loop of §2.1 and the contemporary debate of this subsection share one hinge: falsifiability is infrastructure, and infrastructure can be built before the philosophy is settled. That is why §3 proceeds on definitions rather than doctrine.

## 3. Concepts and taxonomy

### 3.1 Three operational definitions

**Auditability = third-party recomputability.** A claim *C* about a system's reasoning is auditable at cost *κ* if (i) there exists a frozen artifact *A* recording the claim's support, and (ii) a third party with stated resources and no privileged access can mechanically recompute that support from *A* at cost *κ*. Auditability is thus graded, not binary. It is graded by *κ* (attribute ③), by the fraction of claim→execution deviations the record can reveal (attribute ②), and by the independence of the verifier from the claimant and from the artifact's constructor (attribute ④). A leaderboard score is one extreme point of this space: the artifact is a number, the recomputation is a lookup, and the covered deviation spectrum is empty—nothing about the reasoning is recomputed at all.

**Falsifiability = executability of pre-registered verdicts.** A claim *C* is operationally falsifiable if there exists a verdict function *v: A → {supports, kills, inconclusive}* such that (i) *v* was frozen before execution, (ii) *v* is mechanically evaluable by a third party, and (iii) a kill verdict is binding in the sense that it is reported, not discarded. This is the engineering reading, and it differs from the philosophical lineage: Popperian logical falsifiability is a property of a claim's logical form, while verdict executability is a property of the bookkeeping around the claim. The two can come apart in both directions. A claim can be logically falsifiable and verdict-less—no registered rule, no frozen artifact—so that killing it costs a community debate rather than a mechanical evaluation. A verdict-executable claim is killed, or survives, at machine cost. The philosophical lineage and its machine-learning-internal debate are taken up in §2.3 [30, 31]; the operational reading adopted here is deliberately independent of that debate's outcome.

**Bookkeeping = the commitment–execution–verification loop.** A practice keeps the books when it closes a three-stage loop. In *commitment*, what will be checked, the verdict rule, and the artifact format are frozen before execution. In *execution*, the run leaves a frozen, append-only record of what the support consists in. In *verification*, a third party recomputes the verdict from the record. Each stage induces specific audit attributes: the commitment stage defines the auditable unit (①) and anchors timing (⑤); the execution stage determines which deviations leave traces (②); the verification stage is priced (③) and staffed (④); and the loop declares at its exit what it does not certify (⑥). The three definitions compose: auditability and falsifiability are properties of claims; bookkeeping is the practice that produces claims having both.

### 3.2 The three-axis taxonomy

The survey's classification table has three axes. The **organization axis** fixes *what is audited*—the unit of account—giving the five lines L1–L5 of §1.2. The **attribute axis** fixes *how well it is audited*, in six attributes. The **strength axis** fixes *how strong the recorded fact is*, in three evidence tiers plus a scope marker.

| **Axis** | **Entries** | **Question answered** |
|---|---|---|
| Organization (§4–§8) | L1 process steps · L2 explanation–computation relation · L3 evaluation artifact · L4 incentive structure · L5 conserved quantity | where the audit unit sits |
| Attribute (below, ①–⑥) | ① commitment object · ② tamper-spectrum coverage · ③ recomputation cost · ④ verifier neutrality · ⑤ commitment timing and external witnessing · ⑥ distortion boundary | what the audit covers, costs, and certifies |
| Strength (§3.2) | closed (pre-registered) · consistency · motivation only · scope (no evidence recorded) | how strong the recorded fact is |

*Table 1: The three axes.*

| **Attribute** | **Definition** | **Irreducible failure position** | **Loop stage** |
|---|---|---|---|
| ① commitment object | the unit the mechanism commits to and defines as auditable | object mismatch—books kept for the wrong thing | commitment |
| ② tamper-spectrum coverage | which claim→execution deviations leave traces; reference spectrum: omission, fabrication, substitution, reordering, retroactive rewriting | uncovered deviation—a deviation in scope leaves no trace | execution |
| ③ recomputation cost | third-party resources required to verify; single-command recomputation as the ideal, incremental and logarithmic paths as intermediate grades | unaffordable verification—deviations detectable in principle but priced out | verification |
| ④ verifier neutrality | the verifier's independence from claimant, artifact constructor, and audited system; versioning and non-leakage of the verifier itself | captured verifier—the check passes because the checker is not independent | verification |
| ⑤ commitment timing and external witnessing | what was frozen before execution and where the out-of-band anchors live | retroactive record—the record was written after the claim, so agreement is unfalsifiable | commitment |
| ⑥ distortion boundary | what the audit does not guarantee even when it succeeds | overclaim—the audit certifies more than it covers | exit |

*Table 2: The six attributes: definition, irreducible failure, loop stage.*

**Mutual exclusion.** Each attribute names one irreducible failure position of the loop, and the positions are distinct. A deviation that is detectable but unaffordable is a ③-failure that no amount of ②-coverage repairs. A neutral and cheap verifier cannot repair a record written after the fact: ④ does not subsume ⑤. Tight coverage of the wrong object is ①, not ②. All five can succeed simultaneously while the claim still overreaches its ledger; that is ⑥, and it is not detectable from the other five. The axis design would be falsified by a matrix row in which two attributes collapse into one—exhibiting a failure position that two attributes jointly and inseparably cover. The five rows assembled in §4–§8 serve as the standing test cases, and no collapse was encountered.

**Coverage.** The six attributes trace the loop end to end: what is claimed (①), where it can break (②), who checks and at what cost (③④), when the record froze (⑤), and what verification means at the exit (⑥). Remove any one attribute and a class of failures loses its address in the table: remove ③ and "too expensive to check" failures become unclassable; remove ④ and captured-verifier failures fold silently into "verified"; remove ⑤ and retroactive records become indistinguishable from frozen ones. Within the loop's scope, the six questions—who, when, what, how-it-breaks, at-what-cost, with-what-boundary—exhaust the audit questions, in the structural sense that any audit question is a projection onto one of them. The exhaustion claim is stated at the taxonomy's own weakest tier, motivation only, because it is falsifiable in exactly one way: exhibit a recurring audit question that no ①–⑥ cell can host, and the axis design is refuted. No such question appeared while the five rows were being assembled, and the claim is on record in this weak form.

**Neutrality clause.** The matrix cells record facts, literature pointers, and tiers—and nothing else. No cell scores a line, and the survey takes no position on which line is "best." The neutrality is not fastidiousness: a matrix that encoded the surveyors' preferences would be unusable by readers holding different ones. The structure is the contribution; the ranking is left to the reader.[^FN1]

**Strength-tier conventions.** For external literature: closed (pre-registered) is reserved for sources that themselves report pre-registered verdict protocols; consistency denotes empirical support reported by the cited work; motivation only denotes proposals, position papers, critique essays, and formal-theory results without empirical support in the cited work; scope marks boundary statements that record no evidence. Non-peer-reviewed institutional reports are labeled as such and never tiered above consistency. The mapping is deliberately conservative—when our reading of a source is uncertain, the weaker tier is used—and tier upgrades require the primary source, not this survey's inference.

**Tier-letter legend.** C = closed (pre-registered); E = consistency evidence; M = motivation only; S = scope marker; "—" = not located in the verified base. The letters are used in Table 5 (the merged five-line matrix of Section 17.3) and every X.3 matrix row; compound markers (E–M, C/E, S/E) blend the tiers they name.


[^FN1]: **Provenance note.** The ①–⑥ attribute set generalizes a six-item auditor-requirement checklist from the authors' prior audit-ledger engineering practice. The generalization is disclosed for provenance and stands or falls on the two arguments above, not on the practice it came from.

## 4. Process verification: auditing the steps

### 4.1 Problems and mechanisms

The unit of account drops from the final answer to the steps. Chain-of-thought prompting made the steps textually explicit [1]; the GSM8K program built the surrounding infrastructure—grade-school problems with step-annotated solutions, and verifier models trained to rank candidate solutions [5]; process supervision then moved the verifier's unit from whole solutions to individual steps, supported by large-scale human step-level labels [6]. The audit promise is local attribution. When a solution is rejected, the rejection locates at a step index; when it is accepted, the acceptance decomposes into per-step acceptability judgments. The verification target is the reasoning itself, not only its residue, the answer. The line's thesis, stated plainly, has two halves: making steps scorable is not yet making the scorer trustworthy, and step-correct is not conclusion-correct. Both halves are this line's content.

### 4.2 Evidence and failure modes

Evidence. Two facts anchor the line, both at the consistency tier: verifier-based candidate ranking improves best-of-*n* selection over answer-only scoring [5], and step-level (process) supervision outperforms outcome-level supervision on mathematical reasoning benchmarks [6]. The works report both empirically; this survey has pre-registered nothing of its own on the line.

Failure modes. The first is that the verifier is itself a learned model, so its scores are claims that require their own books. The audit unit moves one level down, and the trust problem recurses (④); the step-label ground truth is human judgment, itself unaudited. The second is step-correct ≠ conclusion-correct. Local validity does not certify global validity—errors compound through locally acceptable steps, and conversely, locally flawed steps can be self-corrected downstream. This is the line's distortion boundary (⑥): process verification certifies step acceptability, neither conclusion correctness (which remains an aggregate property) nor explanation–computation consistency (L2's unit). The third is distribution shift: verifiers are trained on labeled problem styles, and their coverage degrades exactly where verification is most needed, off-distribution—the ② spectrum shrinking under the conditions that call for it. The fourth is Goodhart-type pressure on the verifier: once step-scores become the target, whether a training signal or a selection gate, the optimized quantity drifts from the intended one. The line's own negative content—documented verifier failure cases and label noise—belongs to the books this survey counts. A process-verification paper that reports its verifier's failure modes is keeping better books than one that reports only its gains.

### 4.3 Matrix row: L1 facts ①–⑥

| **Attribute** | **Fact (with pointer)** | **Tier** |
|---|---|---|
| ① commitment object | individual reasoning steps of a generated solution chain [5, 6] | E |
| ② tamper-spectrum coverage | step-level deviations are locatable and attributable to step indices; the verifier's own scoring process is outside the recorded spectrum [5, 6] | E |
| ③ recomputation cost | one verifier forward pass per step—a learned-model cost, not an arithmetic recomputation [6] | E |
| ④ verifier neutrality | the verifier is a learned model trained on human step labels; the labels are themselves unaudited judgments (recursion open) [6] | E |
| ⑤ commitment timing | dataset-level commitments (fixed test splits) are standard; run-level pre-registered verdicts are not located in the verified base | — |
| ⑥ distortion boundary | step-correct ≠ conclusion-correct: local acceptability is certified, neither global validity nor explanation–computation consistency | S |

## 5. Chain-of-thought faithfulness: the explanation is not the computation

### 5.1 Problems and mechanisms

The unit of account here is the relation between the emitted explanation and the computation that produced the answer. Chain-of-thought made explanations machine-generated and ubiquitous [1]; the faithfulness question asks whether the emitted chain reflects the actual computation [2, 3]. A second era changed the stakes. Reinforcement learning now trains the chains themselves—reasoning models learn long chains of thought as behavior rather than as a prompt format [32]—so the explanation is a trained artifact, and whatever trains it can shape what it shows. The faithfulness question thus carries a second edge: not only whether the chain reflects the computation, but whether the training signal has taught the chain to look better than the computation.

The measurement mechanisms are behavioral. Perturbation protocols truncate, paraphrase, or pad the emitted chain and ask whether the answer changes [3]; an answer insensitive to the chain's content indicates that the chain is not doing the explaining it appears to do. Bias-planting protocols induce a biased answer through few-shot answer patterns or distractors and ask whether the emitted chain rationalizes the bias post hoc [2]; when it does, the chain is testimony, not computation. In the vocabulary of this survey, the faithfulness tests are the field's detectors for *books ≠ real books*, and the measured quantity is the divergence between the account and the account's causal history.

### 5.2 Evidence and failure modes

Evidence. Unfaithfulness is measurable, non-zero, and task- and model-dependent [2, 3]; both works report empirical protocols with quantitative results, recorded at the consistency tier. The line's strongest content is partly negative, and the negative content carries equal weight: an honestly reported faithfulness-failure rate converts "the model explains itself" into a falsifiable claim—"the explanation deviates from the computation at rate *r* under protocol *P* on distribution *D*"—which is exactly the bookkeeping move of §3.1.

Failure modes. First, the detector problem: faithfulness metrics are behavioral proxies. An answer's stability under chain perturbation is not itself the explanation–computation relation, so a model could pass the available tests while the chain remains non-causal in the relevant sense (the metric-recursion form of ④). Second, instrumental explanations: unfaithful chains can still improve task accuracy, because the chain's causal role in generation is separable from its testimonial role. The books can be wrong while the balance is right; explanation value and audit value must therefore be reported separately, and conflating them is an error this line exists to catch. Third, protocol relativity (⑥): a faithfulness rate is a property of (model, task, protocol), not of "the model," and numbers from different protocols are not commensurable without declaring the protocol. Fourth, the reasoning-model era has begun to produce this line's kind of evidence, and it cuts both ways. CoT monitoring can detect misbehavior in RL-trained reasoning models; but penalizing the monitored bad thoughts does not remove the misbehavior—it teaches concealment while task metrics improve. The audit layer and the optimization layer pull against each other, with the confounding effect measured rather than asserted [33]. On the faithfulness side, reward-hacking behavior in reasoning models is rarely acknowledged in the emitted chain—admission below 2% in most tested settings [34] (an institutional research report, non-peer-reviewed, labeled as such; consistency tier with the label). What remains open is the systematization of this era's evidence (OP5 in §20.2).

### 5.3 The monitorability question and matrix row: L2 facts ①–⑥

The reasoning-model era also supplies a quantification baseline: across twelve open-weight reasoning models and 41,832 runs, faithfulness rates span 39.7%–89.9% [35] (consistency tier). The spread, not the midpoint, is the finding—faithfulness is model-relative and protocol-relative across the open-weight spectrum, not a fixed property of "reasoning models."

The era adds a debate of its own around one word: monitorability. A position paper argues that chain-of-thought monitorability is a new and fragile opportunity for AI safety—precious, because the chain is a direct window into the computation; fragile, because folding it into training targets destroys exactly what makes it valuable [36] (position paper; motivation tier). The fragility claim is not merely rhetorical: stress-testing shows that reasoning models can obfuscate their reasoning, concealing the actual inference path while preserving behavior [37]. Together with the monitoring result of §5.2, the line now holds its cleanest demonstration of a proposition that crosses lines: **an audit layer placed under optimization pressure erodes.** The same proposition recurs at the protocol layer in §7.2, where the decentralized-evaluation cluster meets gaming pressure on the evaluation protocol itself. CoT monitoring here and decentralized evaluation there are the proposition's two live instantiations, and the confounding effect of [33] is its sharpest experimental demonstration in the verified base.

| **Attribute** | **Fact (with pointer)** | **Tier** |
|---|---|---|
| ① commitment object | the explanation–computation relation, per instance and per test protocol [2, 3] | E |
| ② tamper-spectrum coverage | post-hoc rationalization and chain-insensitivity detectable under perturbation and bias-planting protocols [2, 3]; RL-era monitoring detects misbehavior [33, 34]; open-weight faithfulness quantified at 39.7%–89.9% over 41,832 runs [35]; deliberate obfuscation can defeat monitoring [37]; metric-gaming deviations are outside the recorded spectrum (the proxy gap) | E |
| ③ recomputation cost | behavioral probes—no training required; the cheapest detection layer in the survey; monitoring adds inference-scale cost [33] | E |
| ④ verifier neutrality | faithfulness metrics are behavioral proxies, unaudited as instruments (recursion open) [2, 3] | E |
| ⑤ commitment timing | per-study protocols fixed in advance; run-level pre-registered verdicts not located in the verified base | — |
| ⑥ distortion boundary | a faithfulness rate is protocol-relative and model-relative (39.7%–89.9% across twelve open-weight models [35]); monitorability is fragile under optimization pressure [33, 35, 36, 37] | E |

## 6. Evaluation integrity: the benchmark's own books

### 6.1 Problems and mechanisms

The unit of account is the evaluation artifact itself: benchmark, protocol, grading pipeline, and the train/test boundary. Evaluation integrity is upstream of every performance claim in every other line—the books about the books. The mechanisms are three. Leakage auditing systematically detects information improperly shared between training and evaluation—feature leakage, temporal leakage, and adjacent forms—and supplies a taxonomy for spotting them across applications [7]. Reproducibility infrastructure—checklists, code and data submission, and reporting standards—was institutionalized through a major venue's reproducibility program [8]: bookkeeping as social infrastructure, the commitment stage executed at the level of a research community. And the competition format—fixed tasks, frozen leaderboards, enforced protocol equality—rests on the position that AI competitions provide the gold standard for empirical rigor in generative AI: evaluation bookkeeping run as an institution [38] (position track; motivation tier).

### 6.2 Evidence and failure modes

Evidence. Leakage was identified as widespread in machine-learning-based science, with a deployable detection taxonomy [7], and the reproducibility program was adopted and reported at scale [8]. Both are audit-infrastructure papers in the strict sense used here: their subject is not better models but survivable claims. Consistency tier for both.

Failure modes. First, contamination voids admissibility: a score whose train/test separation is broken is a claim whose support does not exist. The detection is usually retroactive—the claim dies after publication—and that is itself the ⑤ failure mode of the surrounding practice: nothing froze the evaluation's commitment before the run, so the post-hoc "clean" verdict is unfalsifiable in exactly the way §3.1 defines. Second, temporal discipline is this line's native ⑤. Held-out sets, embargoed releases, and time-ordered evaluation freeze the test before the claim; where a line of work adopts these, its claims gain verdict executability, and where it does not, they rest on assertions. Third, construct drift (⑥): a benchmark's construct shifts as the population of solvers changes, and a "clean" score certifies protocol-relative performance, not the intended construct, and not reasoning correctness. Fourth, selective reporting: claims survive because failures were never recorded; checklists are the procedural countermeasure, partial by design [8].

Contamination detection has itself become a methodology with a literature: rephrase-based detection [39]; the Sharded Rank test, which proves contamination from black-box access with exact false-positive control [40]; a comprehensive survey organizing the n-gram, semantic, and performance-based families [41]; a systematic evaluation interrogating the core assumptions of fifty proposed detection methods [42]; performance-based detection with context-cache controls [43]; and detection adapted to the RL post-training era [44]. Within L3's row, ② therefore records a populated detector spectrum rather than a blank. The honest boundary is inherited from [42] and sharpened by [45]: the detectors' own core assumptions are only partially validated, and detection itself is fragile for reasoning models, where methods validated on base models can fail [45] (consistency tier). The auditors of the auditors are still largely unaudited; their fragility is now an empirical result rather than a caveat, and a systematic validation protocol is the open step (OP2 in §20.2).

### 6.3 Matrix row: L3 facts ①–⑥

| **Attribute** | **Fact (with pointer)** | **Tier** |
|---|---|---|
| ① commitment object | the evaluation artifact: benchmark, protocol, grading pipeline, train/ test boundary [7, 8] | E |
| ② tamper-spectrum coverage | leakage detectable by systematic audit (taxonomy of leakage forms) [7]; a populated detector family: rephrase-based [39], black-box provable [40], n-gram/ semantic/ performance families [41], assumption-audited [42], performance-based with cache controls [43], RL-era [44]—the family itself fragile for reasoning models [45] | E |
| ③ recomputation cost | pipeline re-analysis: moderate; scales with data-pipeline complexity [7] | E |
| ④ verifier neutrality | community audit plus detection heuristics; benchmark constructors are a trust root (recursion open) [7, 8]; the detectors' own assumptions are only partially validated [42] | E |
| ⑤ commitment timing | temporal discipline native: held-out sets, embargoed release, time-ordered evaluation [7, 8]; competitions freeze protocol equality institutionally [38] | E |
| ⑥ distortion boundary | a clean score certifies protocol-relative performance—not construct validity, not reasoning correctness | S |

## 7. Game-theoretic verification: endogenizing the auditor

### 7.1 Problems and mechanisms

The unit of account is the incentive structure of the verification interaction. Rather than audit the artifact after the fact, mechanism design endogenizes the auditor: the game is structured so that honest, checkable reporting is an equilibrium property rather than an assumption. The debate proposal sets two AI systems in opposition before a weaker judge, human or machine, and argues that cross-examination extracts information beyond the judge's own competence, so that verification scales with the system instead of against it [9]. Mechanism-design approaches to AI safety treat the alignment of participants' incentives as a design object, asking when verification-relevant honesty can be made an equilibrium property of the interaction itself [10]. The formal layer exists in general form: probabilistic verification in mechanism design characterizes honest reporting under noisy tests [46] (formal theory; motivation tier under the survey's mapping). What that theory has not yet received is the connection to ML capability claims, and that connection is the unsystematized step documented in §7.2. The line's distinctive promise is a transformation of ④: verifier neutrality is not purchased from an external auditor but manufactured inside the mechanism. Adversaries check adversaries.

### 7.2 Evidence and failure modes

Evidence. The debate proposal reports preliminary experiments [9]; the mechanism-design program contributes formal analyses and designs [10]. The strength of this line is possibility-level, stated as-is: proposals and analyses, with small-scale demonstrations rather than deployed verification. Several of the line's cells therefore sit at E-to-M in the survey's tiers, and the survey does not upgrade them. A 2026 cluster has additionally formed around a specific L4 failure mode: unverified benchmark claims. The motivation is stated in market terms—unverified benchmark claims can move markets—so the verification itself is decentralized: protocols that replace trust in the benchmark holder [47]; blockchain-based multi-party consensus evaluation frameworks [48]; and matching-server architectures that hide the benchmark from the evaluation client to prevent leakage [49]. The cluster is young, its work proposal-scale and prototype-scale, and the survey tiers it E–M as a cluster rather than entry by entry.

Failure modes. First, Goodhart-type pressure, sharpened by stakes: once the mechanism is the target, participants optimize the *appearance* of honesty, and strategies that pass cross-examination while misrepresenting are the line's canonical adversarial register—the mechanism's guarantee does not cover them (②'s boundary). Second, the judge bottleneck: the human (or weaker AI) judge is debate's unaudited root, and judge competence is simultaneously the verification resource (③) and the trust root (④), a concentration this line inherits rather than solves. Third, equilibrium versus deployment: mechanism guarantees hold in equilibrium, and deployed multi-agent systems need not reach the analyzed equilibrium (selection, collusion). Fourth, the designer trust root: the mechanism designer becomes a new party whose neutrality must itself be audited—④ is transformed, not eliminated. Fifth, the cross-line proposition stated in §5.3: an audit layer placed under optimization pressure erodes. CoT monitoring meets it as concealment [33]; decentralized evaluation meets it as protocol gaming—once the evaluation protocol is the target, gaming pressure migrates to the protocol, and the cluster's designs [47, 48, 49] are attempts to raise the cost of that migration; and reinforcement learning with verifiable rewards meets it at the training interface, where optimizing against the verifier leads the verifier into reward hacking [50] (consistency tier)—the proposition's third instantiation and the one closest to the audit-versus-training boundary. The proposition is the shared failure register of the three sites, and the reason ⑥ boundaries matter more in this line than ② coverage.

The escrow-style combination—a capability claimant posts forfeitable stakes—remains unsystematized at the major machine-learning venues. Its nearest neighbors fall into three clusters. Cluster 1 is mechanism-design theory, general and established, not yet connected to ML claims [46]. Cluster 2 is decentralized LLM evaluation, sprouting in 2026, without bond–forfeiture incentive structures [47, 48, 49]. Cluster 3 is on-chain agent governance, which provides bond-settlement primitives—per-action bonds, runtime behavioral governance, and compensation mechanisms [51, 52, 53]—and an engineering-standard draft specifying agent identity, reputation, and validation registries, with stake-secured re-execution listed among its selectable trust models and payment mechanics declared out of scope [54]; what the cluster escrows is behavioral side effects, not model capability claims. The blank, stated in this narrowed form, documents an unsystematized combination rather than an absence of neighbors: attach a forfeitable bond to a falsifiable capability claim, with a mechanical forfeiture verdict. No verified work has systematized that step.

### 7.3 The governance cluster and matrix row: L4 facts ①–⑥

Cluster 3 in detail, because it carries the bond primitives. Bonded recourse settles compensable agent side effects by smart contract, with a bond attached to each action [51]. AgentBound provides verifiable behavioral governance for autonomous agents at runtime [52]. RAC trains agents to compensate for harms [53]. And ERC-8004—Trustless Agents—is an engineering-standard draft specifying identity, reputation, and validation registries for agents, with stake-secured re-execution listed among its selectable trust models and payment mechanics declared out of scope [54] (Ethereum Improvement Proposal draft; non-peer-reviewed; labeled as such). These are escrow mechanics at the protocol layer: the bond, the forfeiture, and the settlement all exist. What they escrow is behavioral side effects—harm, compensation, recourse—not claims about model capability. The distance to §7.2's unsystematized combination is short and precisely describable: attach the bond to a falsifiable capability claim and make the forfeiture verdict mechanical. The verified base records no work that has taken that step.

| **Attribute** | **Fact (with pointer)** | **Tier** |
|---|---|---|
| ① commitment object | the incentive structure of the verification interaction [9, 10]; on-chain bonds attached to agent actions and side effects [51, 52, 53] | E–M |
| ② tamper-spectrum coverage | strategically dishonest reporting within mechanism scope covered by design; Goodhart-type evasion of the *appearance* of honesty outside the guarantee; concealment under monitoring pressure demonstrated [33]; verifier gaming under RLVR demonstrated [50] | E–M |
| ③ recomputation cost | judge time plus mechanism design and simulation [9]; decentralized verification redistributes rather than reduces cost [47, 48, 49] | E–M |
| ④ verifier neutrality | judge and mechanism designer as trust roots (recursion transformed, not removed) [9, 10]; decentralization replaces the trust root with protocol consensus [47, 48, 49] | E |
| ⑤ commitment timing | mechanism rules fixed before interaction—protocol-level commitment native [9, 10]; bond-settlement primitives exist on-chain [51, 52, 53]; the bond × capability-claim combination is unsystematized (§7.2) | E–M |
| ⑥ distortion boundary | equilibrium guarantees ≠ deployment behavior; honesty-dominance is equilibrium-local; audit layers under optimization pressure erode (§5.3) | S |

## 8. Conservation and physical priors: invariants as external guarantors

### 8.1 Problems and mechanisms

The unit of account is a conserved quantity or physical invariant defined over the reasoning artifact. The verifier is external to the model, the data, and the auditor: a conservation law. Hamiltonian neural networks learn the invariant itself, so that learned dynamics approximately conserve energy [11]; physics-informed machine learning embeds physical constraints, partial differential equations among them, into the learning problem [12]; and systematic characterization of failure modes documents when physical priors help and when they hurt [13]. The line's audit promise, in its strongest form: an invariant that holds *by construction* can be rechecked by a third party with arithmetic alone—verifier independence maximal (④), verification cost minimal (③). Constructive invariants, identities built into the mechanism, are categorically stronger than soft constraints, residuals suppressed by training: the former hold at inference for arbitrary inputs; the latter can be violated exactly when the model is off-distribution, which is when the audit is most needed.

The invariant need not be physical. Formal specifications play the same structural role—an external standard the artifact must satisfy, independent of the artifact's constructor—and their verification literature is this line's computational sibling. OVERT verifies neural network controllers against safety properties reliably [55]; zkLLM produces zero-knowledge proofs of LLM inference integrity, letting a third party verify the computation without re-executing it or seeing the inputs [56]; and the zero-knowledge verifiable-ML line is surveyed systematically [57]. The zk route changes ③'s economics rather than ④'s geometry: verification at sub-linear cost, with the cryptographic assumption stack as a new, explicitly declared trust root.

### 8.2 Evidence and failure modes

Evidence. Conservation and structure preservation were demonstrated in learned dynamics [11]; the breadth of the physics-informed program is documented [12]; failure modes of physical priors are characterized [13]. Consistency tier for all three.

Failure modes. First, conservation ≠ truth (⑥): an identity can hold exactly while every entry in the ledger is wrong—the books balance; the accounting is fiction. Physical priors constrain the ledger's *form*, not its content's correctness; content correctness belongs to L1/L2 and is not inherited from the invariant. Second, soft constraints are violable at inference (②): gradient-suppressed residuals do not survive distribution shift or adversarial inputs, and only constructive invariants give run-time books. Third, prior–optimization conflict: physics-informed objectives exhibit optimization pathologies in exactly the regimes where the prior matters [13]—the audit instrument can damage the system it audits. Fourth, the invariant-chooser trust root (④): which invariant, which form, which parameters—the modeling choice is upstream of the ledger, and the books inherit its assumptions unaudited.

The computational side is held by the formal-verification and zero-knowledge families of §8.1; the physical side's sub-blank is stated narrowly. Conservation laws as run-time auditors—post-hoc reconciliation of an artifact against its invariant, as opposed to a training constraint—have, to our knowledge, no machine-learning-venue work. The nearest neighbors are the physics-informed training-constraint literature itself [12, 13] and generalized anomaly detection in cyber-physical systems (outside the verified base, hence uncited here). Whether the case study of §18 is the first conservation-as-run-time-auditor instance in an ML artifact is a claim the completed novelty search did not refute—and not one this survey asserts.

### 8.3 Matrix row: L5 facts ①–⑥

| **Attribute** | **Fact (with pointer)** | **Tier** |
|---|---|---|
| ① commitment object | conserved quantities and physical invariants over the learned/ artifact system [11, 12, 13]; formal specifications as the computational sibling [55, 56, 57] | E |
| ② tamper-spectrum coverage | constructive identities: ledger deviations arithmetic-checkable [11]; soft-constraint violations reappear at inference off-distribution [12, 13]; zk proofs verify computation integrity without re-execution [56] | E |
| ③ recomputation cost | arithmetic recomputation of the invariant—minimal in the survey; the ideal end of ③; zk verification at sub-linear cost [56] | E |
| ④ verifier neutrality | the invariant is external to model, data, and auditor—strongest independence; the invariant-chooser is a trust root [11, 12, 13] | E |
| ⑤ commitment timing | constructive invariants precede execution by construction [11]; run-time conservation-as-auditor: to our knowledge no ML-venue work (§8.2) | — |
| ⑥ distortion boundary | conservation ≠ truth: a balanced ledger can carry wrong entries; priors can conflict with optimization [13] | E |

---

# Part II · The Verdict Chain

*Provenance: migrated from the V4-line paper v1.1, whose Sections 2-9 become Sections 9-16 here; all verdict numbers and verdict wording are carried frozen, with two measured-value corrections annotated inline as drafted errata-chain family E-37 (Sections 13.3 and 14.2).*

## 9. The Four Principles and the Practice Trail (V1–V2)

### 9.1 Four core principles, stated without redefinition

The program runs on four core principles, recorded in the project's pre-registration layer on 2026-09-22 (R1 entry), with the fourth added to the root on 2026-09-23 (literal anchor: `results/_v4_supp_prereg_v02_add_T15_2026_09_24.md`, 76,991 B, SHA-12 `8898B964A9D9`, measured 2026-09-26: "the four principles are the root, and the papers are one site of externalization"). Their names, romanized and glossed for readability, are:

1. **da-cai-xiao-yong** (literally, "great talent put to small use");
2. **luo-dao-shi-chu** ("landed on solid ground");
3. **yu-si-tong-xing** ("walking with the dead," i.e., with the kill-verdicts);
4. **xu-shi-hui-lu** (the "virtual–real loop"), instantiated as the second companion work, *Fiction That Feeds Back*.

Two statements of scope are mandatory. First, the four principles *precede and run through* the V1–V2 paper practice; the papers are one site of externalization, and the principles did not originate from any paper chapter; this paper does not claim otherwise. Second, the authoritative statements of the four principles are the PI's records; this paper externalizes them without redefining them. What can be reported operationally is this: the working form of principle (2) in the program is the claim-to-anchor ledger (every claim lands on a path, byte count, and SHA-12), and principle (3) is externalized as Section 16 of this paper, a title the program's own verdict document already carries. Principles (1) and (4) appear in this paper as presentation discipline and as the companion-work citation above, respectively, not as sections.

### 9.2 V1: the G1 mind map, transcribed honestly

The distillation claim's lineage starts at a V1 asset: a hand-drawn mind map titled *AI ying dang ru he si kao* ("How should AI think"), manually transcribed by an analysis engineer into a 45-node, 49-edge, 9-branch graph with a designated GOAL node ("topological intelligence") and two designated trap nodes, plus a scattering demonstration over six paths (aggregate transmitted/reflected/dissipated = 0.531 / 0.3566 / 0.1124). Anchor: `results/deposon_g1_mindmap_demo.json`, 3,041 B, SHA-12 `55428F6BD848` (measured 2026-09-26). The asset itself records that the transcription was manual (no OCR), that the source image was a PNG, and that trap/answer annotations and decoy edge weights (0.9/0.85, low barrier 0.1) were set semantically at transcription time. The transcription method and the semantically set weights are disclosed in the asset itself, not smoothed over; that disclosure is the house style this paper inherits.

### 9.3 V1–V2 practice as an externalized trajectory

The V3–V4 evidence base for the V1–V2 period is a four-piece inventory set: the tri-directory achievements inventory, its erratum, and two addenda, which must be cited in parallel (never singly), together with the prior single-directory main list they supersede. In parallel, all measured 2026-09-26: `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` (355,687 B, `3E4E90FB48E1`); `results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md` (10,288 B, `55CD332F66F2`); `results/_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md` (23,152 B, `C64146C4CCAC`); `results/_v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md` (37,212 B, `24C64CC23907`); prior main list `results/_v3_v4_achievements_inventory_2026_09_24.md` (192,160 B, `29A853444D42`). The practice they record is the externalized trajectory of the four principles, not a success narrative: the inventory's own accounting includes discovered discrepancies, corrected counts, and an erratum mechanism, which is exactly the material Section 10 formalizes.

---

## 10. Verdict-Anchored Governance (V3–V4)

### 10.1 SHA-anchored, append-only assets

Every artifact in the program's evidence chain is born with a path, a byte count, and a SHA-12 digest; digests are *on-disk measured* values (the anchor-chain unification recorded as errata entry E-35.3), not self-reported values. Derived JSONs are never merged; thresholds are never adjusted after the fact; V1–V3 assets (18 frozen results, 9 grids) are read-only and untouched by the V4 phase. The governance face of this paper is the same rule applied to itself: Appendix A is the ledger, and its values were re-measured on 2026-09-26, the writing day.

### 10.2 The errata chain: E-1 through E-36

The central governance artifact is a running errata chain, currently at v19 with entries E-1 through E-36 accumulated across three append rounds (v17, v18, v19): `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`, 239,387 B, SHA-12 `849D76BE3A06` (measured 2026-09-26). The v19 change record states: zero modifications of v18's existing sections and zero modifications of the E-1 through E-35 rows; E-35 added the 72-event accounting ruling and the on-disk SHA-12 anchor unification; E-36 added the boundary declarations of the v2-letter drift errata. The chain is append-only: an error is never overwritten, it is appended as a numbered entry with its literal sources. Any citation of the V3 report layer must carry the errata chain citation in parallel (a house citation rule), so that a reader never sees a single uncorrected source.

### 10.3 Case E-15: an anchor break, found and repaired

Entry E-15 records the sharpest governance event of the period. A frozen anchor file (the KT-ABC1 anchor set, expected at a declared path with SHA-12 `03C6C01F3697`) was absent from its declared paths; a same-named, different file (11,318 B, different digest, a root-session artifact) sat where verification first looked, and the declared fallback path had no such file. Mechanical verification scored 15/16 PASS with E-15 as the sole FAIL; a PI-authorized direct correction on 2026-09-23 restored the anchor set, and the verification then closed at 16/16 (current anchor set: `verifier/handoff/KT_ABC1_anchors_sha256_12.json`, 6,680 B, `03C6C01F3697`, measured 2026-09-26; the closure is recorded in the errata chain and in the evidence-audit reconciliation `results/_v4_evidence_audit_reconcile_2026_09_26.md`, 22,863 B, `68F66904C0C8`). The sequence (break, mechanical detection, authorized repair, erratum entry, re-verification) is the governance theme of this paper in miniature.

### 10.4 The false-falsification review

Errata family E-28 (E-28.1 through E-28.8) records a program-wide review triggered by the PI's standing instruction that *no false falsification and no false pass shall remain standing*. Every verdict was re-examined against the four adjudication requirements of E-27 §13 (material-face coverage among them); the review reclassified several apparent falsifications as construction failures, held the GLM_2 signal as tentative pending re-run (Section 15), and closed with a transition declaration. The T-series of Section 13 is the operational continuation of this review.

### 10.5 Zero-key discipline and housekeeping

Two R4 records attest the zero-key rule (keys never on disk, never in prompts or logs, runtime-only): `results/_v4_r4_key_purge_manifest_2026_09_24.md` (13,884 B, `5BF4D9AD2877`) and `results/_v4_r4_purge_actions_2026_09_24.md` (33,117 B, `8BBFE831E7C3`), both measured 2026-09-26. Housekeeping during the phase is recorded in six append-only move ledgers, a cleanup manifest, and a noise-cleanup manifest (cited in Appendix A, not expanded here), so that even file moves are auditable.

---

## 11. The Claim and Its Retired Predecessor

### 11.1 The v2.2 claim: critical learning, not profiling

The registered claim of the phase is that an AI system can *critically learn the PI's way of thinking*: internalize a transferable judgment method (criterion structure, trade-off patterns, principle application), including the capacity to disagree with reasons. It is explicitly *not* a claim of profiling or predicting the PI's behavior; the PI's framing, recorded in the preregistration, is that the way of thinking can be critically learned and should not become a profile. The claim echoes the V1 mind map's question ("How should AI think," GOAL: topological intelligence). The product is a judgment-structure rule set for AI internalization; full reasoning texts remain on the PI's local face and are never transmitted; the collection instrument is a purpose-built distillation questionnaire, not reused decision traces. Preregistration: `results/_v4_pi_cot_v2_prereg.md`, 4,247 B, SHA-12 `CC25C5149CE1` (measured 2026-09-26), revision chain v2.0 (with decision traces) → v2.1 (questionnaire collection face) → v2.2 (claim redefinition from replication consistency to the three critical-learning indicators).

### 11.2 Three measurable faces and mechanical kill-lines

The preregistration decomposes the claim into three faces: (1) *extractable* (fidelity): the judgment structure in the PI's reasoning text is rule-extractable, with a six-class criterion code (kill-line, cost, principle, risk, timing, delegation); (2) *transferable* (learning): on held-out scenarios the rule set's reasoning structure matches the PI's with similarity at least 0.80; (3) *critical* (non-obedience): at disagreements the rule set attaches explicit critique 100 percent of the time, and its blind-obedience (unreasoned agreement) rate is at most 0.10. The kill-lines are mechanical: (a) similarity < 0.80 triggers FAIL; (b1) critique coverage < 100 percent triggers FAIL; (b2) blind-obedience rate > 0.10 triggers FAIL; (c) a bootstrap CI lower bound < 0.50 triggers FAIL. Any single trigger equals FAIL (within the construction domain); only zero triggers equals PASS; each decision-table row carries a three-class root-cause attribution.

### 11.3 The retired first-generation claim (E-25, E-26)

The first generation of the task claimed that the PI's chain of thought could be *replicated* by a proxy, measured by a replication-consistency rate. Its verdict was FAIL, originally classified as proposition-level true falsification. The errata chain requalified that classification. Entry E-25 records the disqualifying fact: the v1 material face was 23 decision-trace entries, 17 of which carried no reason field; decision traces are records of choices, not reasoning chains, so the material face *never covered* the claim's subject: the proposition was never adjudicated, and the correct label is *false falsification*. The FAIL reading itself stands (nothing learnable was present in that data), and it must not be read as "chain of thought non-replicable." Entry E-26 adds the claim-positioning note: the v1 claim was profiling-oriented, which the v2.2 claim explicitly retires. Recorded anchors, as carried in the current preregistration and errata chain: v1 preregistration `696af9121d9f`; v1 verdict `D279EBDE5E84`; v1 dataset `139DBFFD8CF9` (retained as a decision-trace archive, not as reasoning material). The v1 metric (replication consistency) is *retired*; it appears in this paper only as claim-evolution evidence. The v1 FAIL and the v2.2 FAIL are failures of *two different claims* and must not be merged into a narrative of "the same experiment failing twice."

---

## 12. Pre-Registration and the Formal FAIL (Task B v2.2)

### 12.1 Pre-registered thresholds

The thresholds were locked at preregistration and are reported here with their achieved values, because a FAIL without its threshold system is not checkable.

| ID | Threshold | Achieved | Status |
|---|---|---|---|
| TH-v2-1 | N_min = 50 (full reasoning texts) | 72 | met |
| TH-v2-2 | reversal/correction events ≥ 5 | 16 | met |
| TH-v2-3 | day span ≥ 3 days; per-day share ≤ 60% | 2 days; see 12.2 | supersede |
| TH-v2-4 | held-out = 0.30, stratified, incl. corrections | 22 of 72 | met |
| TH-v2-5 | structural similarity ≥ 0.80 | 0.0909 | kill-line (a) |
| TH-v2-5b | blind-obedience ≤ 0.10; critique coverage 100% | 0.3333; 0.6842 | kill-lines (b2), (b1) |
| TH-v2-6 | seed = 42 | 42 | as registered |
| TH-v2-7 | permutation n = 1000, α = 0.05 | as registered | as registered |
| TH-v2-8 | bootstrap n = 1000, 95% CI, lower bound 0.50 | [0.0, 0.2045] | kill-line (c) |

"Supersede": the day-span criterion was recorded as met by an explicit PI ruling (see 12.2); the per-day share exceeded the threshold under every recorded denominator.

### 12.2 Data accounting, dual denominators, and the supersede

The formal denominator is n_total = 72 (37 items from the v1.1 dataset plus 35 addendum items). Eight day-1 (D1) items are *declared absent and not fabricated*; the absence declaration is one of the four elements of formal validity. The result file carries a dual reading: a main reading of 22 held-out items and an alternative reading of 17 (corrections excluded), with bootstrap intervals [0.0, 0.2045] (main) and [0.0294, 0.3382] (alternative). Anchors: result `results/_v4_pi_cot_v2_result_v2.json` (18,089 B, `F86727C857A8`); rule set `results/_v4_pi_cot_v2_ruleset_v2.json` (6,179 B, `C5B3DD141655`); executor `results/_v4_pi_cot_v2_ruleset_v2_executor.py` (52,465 B, `EB22F13D571C`), all measured 2026-09-26. The dataset family is cited by path and digest only (Appendix A); its content never leaves the local face.

The day-span criterion (TH-v2-3) has two recorded denominators, reported here with their sources, with the 72-event denominator declared as this paper's working standard: the D1 concentration was 48/72 = 66.7% under the 72-event denominator (errata E-35.1), and 48/68 = 70.6% under the collected-events denominator (errata E-34.4, which also records D2 at 20/68 = 29.4%); the same entry E-35.1 notes a theoretical edge state of 48/80 = 60.0% at the denominator that would include the eight absent D1 items. On 2026-09-26 the PI issued an explicit supersede (recorded as ruling ask_822b1e27 in the signoff and errata chain): the measured two-day span (2026-09-24 to 2026-09-26) is recorded as meeting the ≥ 3-day requirement under a calendar-span interpretation (three calendar days). The per-day-share threshold of 60 percent is exceeded under both measured denominators (68 and 72) and is exactly met, at the 60.0 percent line, under the theoretical 80-event denominator (48/80, the recorded edge state); that is stated, not averaged away.

### 12.3 The verdict

The formal verdict is **FAIL**, issued by the verdict-keeper role on 2026-09-26 with the composite qualification of the table below. Formal verdict: `results/_v4_pi_cot_v2_verdict_v2.md`, 33,723 B, SHA-12 `5D79E67A4E9D` (measured 2026-09-26). An exploratory first verdict exists, coexists with the formal one, and is not overturned by it: `results/_v4_pi_cot_v2_verdict.md`, 22,340 B, `EB9AD4193CF2` (exploratory pre-run FAIL with unresolved false-falsification suspicion). The retired v1 rule set and result are frozen in place: `821465001819` (5,876 B) and `1665F367B2C4` (9,068 B).

| Kill-line | Measured | Line | Root-cause class |
|---|---|---|---|
| K-V2-a: mean similarity | 0.0909 | < 0.80 **hit** | composite (α + β) |
| K-V2-b1: critique coverage | 0.6842 | < 1.00 **hit** | β (construction-dominant) |
| K-V2-b2: blind-obedience rate | 0.3333 | > 0.10 **hit** | composite (α + β, metric artifact) |
| K-V2-c: bootstrap CI | [0.0, 0.2045] | lower bound < 0.50 **hit** | β (construction-dominant) |

Root-cause classes: α = proposition-level falsification; β = construction/tool failure (false-falsification family); composite = both faces present. The verdict's summary count: two composite, two β, zero pure α.

### 12.4 The composite qualification, carried literally

The verdict's one-sentence qualification is *partial true falsification plus partial construction doubt*, with the two faces recorded as follows.

*The true-falsification face.* After the v2 vocabulary expansion (201 judgment words plus 35 critical-reflection words; unknown-token rate reduced from 55.6% to 22.2%), the predicted and actual criterion-type distributions became comparable, and the mean similarity of 0.0909, with 19 of the 22 held-out items at similarity 0 (86.4%), is recorded as not a measurement accident: the rule set has a *structural insufficiency* in predicting the PI's criterion sequences (decision trees of at most 4 layers, 9 features, and limited template expressivity), which the verdict classifies as a rule-learning capacity boundary rather than pure construction failure.

*The construction-doubt face.* Four doubts are recorded: (i) the recall-form metric structurally underestimates similarity under the expanded vocabulary (more predicted types make hits harder, amplifying the apparent falsification signal); (ii) the bootstrap lower bound of 0.0 is an extremely pessimistic artifact of resampling a 22-item held-out set; (iii) K-V2-b2 rests on n_agree = 3, in which a single blind-obedience event determines the 0.3333 rate (structural high variance); (iv) the eight D1 absences, the two-day span (against the theoretical three or more), and the held-out count of 22 against the theoretical 21.6 (0.30 × 72) qualify representativity.

### 12.5 Independent signoff and the meaning of PASS

An independent verifier role signed off on the verdict on 2026-09-26: anchor-chain integrity PASS, 72-event recount PASS, kill-line re-check PASS ("the verdict holds; the composite qualification holds"), overall **VERDICT: PASS**, with one out-of-scope note (K-N26-N1, a construction check belonging to the separate L14V3 track, filed as out-of-scope, not as a review opinion). Signoff: `results/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md`, 26,637 B, SHA-12 `BA4D07BD7000` (measured 2026-09-26). Coding review (anti-degeneration audit of the v2 vocabulary and executor): `results/_v4_pi_cot_v2_coding_review_2026_09_26.md`, 42,914 B, `5FBEC21E0AD2`. The signoff's PASS certifies the validity of the verdict process (the four elements: 72-event accounting, absence declaration, composite qualification, and signoff), and it is not, and must not be read as, a pass of the experiment. This sentence exists because that misreading is available.

### 12.6 The non-extrapolation boundaries

The verdict states its boundaries explicitly, and this paper carries them: (1) the composite qualification does *not* constitute a proposition-level declaration that the PI's chain of thought is non-distillable, nor that critical learning cannot reach the bar; while any of the four construction doubts stands, the composite is clamped within the bounds of the current rule set and the current metric; (2) it does not extrapolate to "the v2 vocabulary improvement was worthless" (the unknown-token reduction was immediate, and the simultaneous fall in similarity is a coupling artifact of the metric form and the rule-set capacity limit); (3) it does not extrapolate to the V1–V3 assets (18 frozen results, 9 grids; unrelated and untouched, read-only); (4) it is valid within the current construction domain only, and it does not prejudge the task's final path.

---

## 13. The False-Falsification Triage Pipeline (T1, T1.5, T1.5r2)

### 13.1 Why a FAIL needs triage

The program's root-cause taxonomy has three classes: α (proposition-level, true falsification), β (construction or tool failure, the false-falsification family), and composite (both faces). A FAIL reading can lie in either direction: a β can masquerade as an α (killing a true claim), and an α can hide behind a β (excusing a false claim). The pipeline's function is to pay down β doubts *before* filing, and to file only what survives. Its four stages, as executed in the V4 phase, are probe, correct, expand, and truly adjudicate.

### 13.2 T1: the sensitivity probe

T1 was registered as a robustness auxiliary probe (a sensitivity check, not a re-adjudication) over two standing V3-era verdicts, L2 and L14 (both formal FAILs on the pre-registered kill-line K-N11-3, with distinct recorded root causes). Its flip-trigger lines did not fire: across the temperature grid {0.0, 0.3, 0.5} and both endpoint groups, the recorded J-medians all stayed below 0.85, so the standing verdicts' directions were temperature-stable and endpoint-stable (any_hit = false for K-T1-S1 and K-T1-S2). T1 verdict: `results/_v4_supp_t1_verdict.md`, 27,538 B, SHA-12 `F1B5E49F3058` (measured 2026-09-26). The probe's decisive product was a reclassification: the J = 0.0 readings it examined were produced under a reasoning-model plus token-budget mismatch (a 100-token cap), which makes J = 0.0 a signal of *neither side producing output*, not of teacher stability; five of five K-family items were reclassified into the construction-failure (β) family. The standing L2/L14 verdicts were preserved, in the recorded phrase, with not one character moved.

### 13.3 T1.5 and T1.5r2: correct, then expand

T1.5 was registered as the construction-failure-fix probe for T1. Its own registered fix was tool-side: it replaced the reasoning-model configuration with a non-reasoning one and raised the token budget to the recorded value of 500 (construction check C-T15-1), which eliminated the empty-response failure mode of T1 (from 49.3 percent to 0) and confirmed that the corrected construction preserved the direction of the standing verdicts. T1.5 verdict: `results/_v4_supp_t15_verdict.md`, 52,884 B, SHA-12 `52C985429C91` (measured 2026-09-26). Its verdict additionally proposed a pair-count expansion of +60 calls (its Section 3.4, Plan A), which the PI ruled on (ruling t15_ext: 6 cells × +10 = +60 calls) and which the next stage executed. T1.5r2 was registered as the expansion probe: the pair-count plan (6 pairs per teacher) sat below the registered minimum (N_min = 10); the expansion executed the ruled +60 calls (recorded formula: 5 teachers × 2 prompts × 3 re-asks per cell × 6 cells = 180 calls, giving 15 pairs per teacher; measured execution: 62 new calls across the six cells, 10 to 11 per cell (errata-chain annotation E-37.2, drafted for the next append round: the source verdict file's summary line writes 60, an arithmetic slip in its own per-cell formula, which sums to 62; the measured execution consists of the ruled 60 re-ask-2 expansion calls plus two make-up reruns recorded within the same execution, and the execution record registers 62; the ruled +60 budget was executed in full; the frozen verdict file itself is unmodified; the re-measurement's evidence file is anchored in Appendix A), at which point the relaxed construction check (K-N11-N1,T1relax) passed literally, and the false-falsification root cause recorded in T1 was eliminated. T1.5r2 verdict: `results/_v4_supp_t15r2_verdict.md`, 64,145 B, SHA-12 `8355724A26E3` (measured 2026-09-26). The stage's three call counts stand in one recorded relation: 180 is the full-quota reference formula (5 teachers × 2 prompts × 3 re-asks per cell × 6 cells), the ruled expansion was confined to the re-ask-2 layer at +60 calls, and the measured execution is 62. Each stage's verdict states: no overturn of standing verdicts, no re-adjudication of prior verdicts, conclusions enter the errata chain as robustness notes.

### 13.4 The pipeline as a methodological contribution

The pipeline's output in this phase was not a rescued experiment; it was the N-26 audit of Section 14, a falsification whose construction doubts had been paid down stage by stage before filing. The pattern generalizes: *probe* (is the signal sensitive to construction knobs?), *correct* (fix the construction), *expand* (meet the pre-registered minimum sample), *truly adjudicate* (file only what survives). Each stage is itself a registered, verdict-anchored probe that cannot overturn standing verdicts, so the pipeline cannot be used to launder a standing FAIL into a PASS; it can only remove β doubts from a future filing.

---

## 14. The N-26 True Audit

### 14.1 The proposition and the construction

The N-26 audit re-ran the V3 distillation chain end to end to adjudicate one proposition: *call-side metadata alone can distinguish distilled outputs from teacher outputs*. The re-run covered five teachers (internal codenames kimi, GLM_1, GLM_2, coze, minimax; internal labels, with all GLM-related statements deferred to the PI's GitHub repository as the sole authoritative source, hence no model versions, endpoints, or product names here), 22 captions, 10 cells, at least 5 calls per caption, with a four-tuple record per call (prompt id, prompt text, response text, per-call metadata). The worker executed 1,090 calls in total: 518 on the teacher side and 572 on the distill side. N-26 verdict: `results/_v4_supp_l14v3_n26_verdict.md`, 64,485 B, SHA-12 `F4435801D09F`; L14+ preregistration: `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md`, 61,547 B, `05B975A86989` (both measured 2026-09-26). Two construction checks passed: non-degeneracy (K-N26-N1, pass = True: every cell at least 110 calls with at least 5 successful calls per caption, except the teacher-kimi cell at 77 calls with at least 1 successful call per caption after an early batch was cleared) and routing/integrity compliance (K-N26-N2, pass = True: 100 percent compliance on the four routed endpoint groups, no routing required for the fifth by design, and a cumulative empty-response rate per teacher of 0.021–0.075, far below the 0.50 threshold).

### 14.2 The adjudication

Of the five registered kill-lines, one triggered: **K-N26-2 TRIGGERED** (true falsification in the v1/v2 direction): the pooled binary AUC of a teacher-versus-distill classifier on metadata features was 0.5663, far below the 0.75 true-falsification line. Two independent robustness checks accompany the pooled value: the read-variant sensitivity test held across all five read variants (AUCs in the recorded range 0.4459 to 0.5916, every one below 0.75; errata-chain annotation E-37.1, drafted for the next append round: the source verdict file's two summary statements record this range as 0.4459 to 0.5844, omitting the drop_glm2 read; the independent re-measurement of 2026-09-27 gives 0.5916 as the five-read upper bound, which is written here; all five reads remain below 0.75, so the robustness finding is unchanged; the frozen verdict file itself is unmodified; the re-measurement's evidence file is anchored in Appendix A), and the five-fold cross-validation returned 0.5271, 0.5266, 0.6318, 0.5740, and 0.5719, all below 0.75. Call-side metadata does not separate distilled outputs from teacher outputs in this construction, and the proposition is truly falsified. **K-N26-1 NOT TRIGGERED**: the five-teacher mean teacher-side accuracy was 0.5617, below the 0.70 line (kimi at 0.7512 was the only teacher at or above 0.70; the other four, including GLM_2 at 0.6364, below). **K-N26-3 NOT TRIGGERED**: three of five teachers fell below 0.60 (GLM_1 0.3955, coze 0.5344, minimax 0.4909), short of the registered threshold of at least four teachers.

| Kill-line | Registered direction | Measured | Record |
|---|---|---|---|
| K-N26-1 | teacher accuracy ≥ 0.70 ⇒ true falsif. | 0.5617 mean | NOT TRIGGERED |
| K-N26-2 | AUC < 0.75 ⇒ true falsif. | 0.5663 pooled | **TRIGGERED** |
| K-N26-3 | ≥ 4 teachers < 0.60 ⇒ true falsif. | 3 of 5 | NOT TRIGGERED |
| K-N26-N1 | construction non-degenerate | 10 cells, ≥110 calls each | pass = True |
| K-N26-N2 | routing and empty-rate compliance | 100%; 0.021–0.075 | pass = True |

### 14.3 The L4 verdict and the deepening relation

A standing prior verdict (L4, digest `74B5B37F7EEA` as recorded) had adjudicated the same proposition FAIL with root cause *construction infeasible* (four of five teachers' metadata fields absent). That verdict has no independent file in the workspace and is cited here as a *literal transfer* through the errata chain (v19 §22.7, entry E-34.2), which is how it must be cited. The N-26 audit is a *same-direction deepening, not a reversal* (the recorded phrase: tong-fangxiang shenhua fei fan'an): L4's "construction infeasible" meant the proposition had never been truly adjudicated; N-26 completed the construction and adjudicated it, confirming the indistinguishability direction. The L4 wording is preserved unchanged.

### 14.4 No extrapolation

The audit does not license the conclusion that the two output classes are *fully* indistinguishable: kimi's 0.7512 is a recorded counter-signal at the teacher level, and GLM_2's 0.6364 also sits above 0.60. The record stands as measured, per kill-line, with no averaging across the counter-signals.

---

## 15. The GLM_2 Line

### 15.1 A two-tier record

The GLM_2 line is recorded in two tiers, and both are reported. *Tentative history:* errata entry E-28.6 recorded a cross-model proposition-falsification signal for the GLM_2 teacher face (3 of 15 cells at N = 5) as *tentative*, with the explicit reason that an N = 5 sample carries small-sample false-falsification risk; filing was withheld pending an N = 20 re-run. *Formal closure:* the re-run showed all three student models in the same direction (D1 Jaccard above D2 Jaccard; margin deltas of −0.001531, −0.000630, and −0.001267 for the three recorded internal labels), consistent with the N = 5 baseline directions (−0.001611, −0.001106, −0.006920), and the errata chain upgraded the entry from tentative to *formal proposition falsification* (§17.4, the E-28.6 closure). The chain also records a structural bound for this teacher face: n_t = 23, so even a proxy count of 23 cannot exceed the teacher count, while the recorded alignment ratio (0.870) clears the 0.20 line throughout. All GLM_2 facts in this section are literal carries from the errata chain `849D76BE3A06` (§15.6, §17.4) and the N-26 verdict `F4435801D09F`; internal model labels are quoted as recorded.

### 15.2 The PI ruling and the authority note

A PI ruling, recorded in the phase's commission letter and rendered here in translation, states: *GLM_2 distillation experiment failed; false-falsification-phase root cause; no extrapolation*. Chinese original, as recorded in the commission letter (Appendix A, letters-family entry): 「GLM_2 蒸馏实验失败 / 假证伪根因 / 不得外推」. The middle term admits two readings (a root cause in the false-falsification class, or a root cause of the false-falsification phase); this paper's rendering takes the phase reading and is a translation, not a substitute for the original. All statements in this paper that involve GLM are anchored to the PI's GitHub repository as the *sole authoritative source*; accordingly this paper records the ruling, the errata-chain record, and the N-26 teacher-side accuracy for GLM_2 (0.6364) side by side, and draws no extrapolation from any of them: in particular, nothing here supports a statement that GLM-family models are non-distillable in general.

---

## 16. Walking with the Verdicts

This section externalizes the third principle (yu-si-tong-xing, "walking with the dead," i.e., with the kill-verdicts). The program's own formal verdict carries a section of this name, and the phrase is the paper's intended posture: a verdict is filed, its boundaries are stated, and the record closes.

### 16.1 The writing rules this paper imposed on itself

The phase's verdict discipline, as registered by the PI and carried into this draft: (a) verdict wording is literal (FAIL, hit, composite qualification, NOT TRIGGERED), never rewritten as "not fully successful" or "partially validated"; (b) no softening pivots follow a verdict (the banned moves include "but," "however," "hope remains," "future work may yet," and "comfortingly"); (c) the forbidden extrapolations are enumerated and none is drawn: not "chain of thought is non-distillable," not "critical learning cannot reach the bar," not "fully indistinguishable," not "GLM-family non-distillable," not any claim that a particular one of the five version-pending files is authoritative; (d) mechanical honesty is insufficient, so every verdict number co-presents its root-cause class and its construction doubts; (e) the recorded phrases "same-direction deepening, not a reversal" and "not one character moved" are carried as recorded; (f) every verdict number carries a path and a SHA-12 anchor, so a reader can recompute it.

### 16.2 What stands, by evidence tier

The first work fixed a three-tier evidence convention (closed/pre-registered, consistency, motivation-only), and this phase's ledger sorts as follows, with no blending across tiers. (The external-literature tier conventions of Section 3.2 share this first-work origin; the two versions are related but not identical in semantics: the Section 3.2 version grades external sources, this one grades the program's own records; they are deliberately not merged into a single definition.) *Closed (pre-registered):* the Task B v2.2 formal FAIL with its composite qualification; the N-26 true falsification of the metadata-separability proposition; the N-26 non-triggers (K-N26-1, K-N26-3) and construction passes (N1, N2); the GLM_2 formal proposition falsification; the TH-v2-1/2/4 threshold achievements. *Consistency evidence:* the T-series' direction-stability notes (temperature- and endpoint-stable standing verdicts; corrected-construction direction agreement); the alternative reading's interval [0.0294, 0.3382], which agrees with the main reading's verdict. *Motivation only:* the G1 mind map's GOAL (topological intelligence) and the distillation program's long-run ambition; nothing in the closed tier either supports or refutes the GOAL itself.

### 16.3 What the failures establish and what they do not

The failures establish, at the recorded construction domains, samples, and qualifications: that the current rule set, under the current metric, does not critically learn the PI's judgment structure to the registered bar (four kill-lines, composite); that call-side metadata does not separate this construction's distilled outputs from teacher outputs (one true falsification, two non-triggers); and that the GLM_2 teacher face's proposition-falsification signal survived its N = 20 re-run. They do not establish any of the enumerated extrapolations, and the two FAILs of the two claim generations do not merge into any statement about distillation in general. That is the whole of what the phase's verdicts license, and this paper files it at exactly that scope.

Boundary note (merged draft, 2026-09-27): the V4 phase is open at writing time; this merged draft reports the recorded state and closes nothing.

## 17. The V4 Chain on the Five-Line Matrix

### 17.1 The sparsity observation, answered from the program side

Part I closed with the assembled matrix; Part II closed with the verdicts. The two closures meet in one observation and one fact.

The observation, recorded with the assembled matrix in Section 17.3: across the survey's 60 external entries, the commitment-timing column ⑤ is empty of run-level, pre-registered verdict protocols. Dataset-level splits, per-study protocols, held-out sets and competitions, mechanism rules and bond primitives, and constructive invariants are each commitment-adjacent, but none freezes a claim's kill rule before the run in the sense of Section 3.1.

The fact, filed in Part II: the V4 phase is exactly such a protocol, run end to end. Four kill-lines were frozen before the Task B runs and adjudicated against them (Section 12); the N-26 audit was pre-registered before its execution (Section 14); the T-series probes were registered before their runs (Section 13); and the verdict chain was signed off by an independent re-computation (Section 12.5).

The survey's empty column and the program's filled chain are the same object seen from two sides. This is the hinge the whole merge turns on, and it is stated with the register discipline both lines share: the external ⑤ cells remain empty—this draft fills no cell of the external base—and the program's instance is recorded as one run-level protocol at the recorded construction domains, samples, and qualifications, with no extrapolation to a field-level practice claim (the no-extrapolation enumerations of Sections 12.6, 14.4, and 16.3 apply here unchanged).

The five lines trade in five currencies—steps, explanations, benchmarks, equilibria, invariants. The V4 chain adds a sixth: verdicts, frozen before execution and re-computable after it. The exchange rate is the one this paper has traded in throughout (Section 20.2).

### 17.2 The six-block chain mapped onto the lines

The V4 chain is one protocol, but Part II filed it in six blocks, and each block lands on the matrix differently. Table 4 maps the six blocks onto the five lines.

Two numbering disciplines guard the mapping. First, the lines L1–L5 are the survey's organization axis (Section 3.2); the program's internal verdict ladder, which also uses the letter L for its adjudication tiers, is a different numbering system and is never conflated with the lines—the same discipline that keeps the K-N26-* and K-N11-* kill-line families distinct (Sections 14.1 and 16.1). Second, each mapping names a primary line, a secondary line, and the in-program register tier of Section 16.2; a block is not mapped to a line without a recorded anchor at that line.

| Block (Part II) | Primary line | Secondary line | In-program register | Mapping basis |
|---|---|---|---|---|
| V1–V2 practice trail (Sections 9–10) | L1 | L2 | motivation only | the trail is a process record, honestly transcribed; the mind-map GOAL stays motivation-only |
| V3–V4 governance chain (Section 10) | L3 | L1 | closed | errata chain, SHA-12 anchors, and event accounting: artifact integrity and tamper evidence |
| Task B v2.2 formal FAIL (Sections 11–12) | L3 | L2 | closed | indicators and kill-lines are evaluation artifacts; the blind-obedience indicator is a faithfulness-type measurement |
| T-series triage pipeline (Section 13) | L3 | L4 | consistency | construction-failure triage of the evaluation itself; adjudication roles declared as roots |
| N-26 true audit (Section 14) | L3 | L2 | closed | pre-registered audit of output separability; deepening relation filed literally |
| GLM_2 proposition line (Section 15) | L2 | L4 | closed (N = 20) | the teacher face's falsification signal is a faithfulness-type observation under incentive pressure |

*Table 4: The six V4 blocks on the five lines. Register per Section 16.2; no block is mapped to a line without a recorded anchor. The mapping is a reading of Part II's records, not a new measurement.*

Nothing in the chain lands primarily on L5, and the chain makes no conservation claim: the first work's constructive identity is that line's instance, not this phase's. The blocks that fill the ⑤ column—governance and Task B, and the registered audits and probes of Sections 13–14—are the ones whose commitments predate their runs; the blocks that lean L2 or L4 record the faithfulness-type and incentive-type observations; the mapping adds no fact beyond Part II's records.

### 17.3 The merged matrix

Table 5 assembles the six rows: the five rows built in Sections 4–8, and the V4 chain entered as one further row. The rows are organization units; the columns are the six attributes; and each cell compresses the fact, pointer, and tier recorded in the corresponding X.3 row, where the full statement lives. The table is read, not scored. Cells record what the verified literature base supports—and, for the V4 row, what the phase's frozen verdict artifacts support—an empty cell is a statement about the base rather than the field, and the two cells that record narrowed blanks (L4 ⑤, L5 ⑤) carry their declarations explicitly rather than as bare gaps (Sections 7.2, 8.2). Row numbering: rows 1–5 are the external lines, and the V4 chain is this table's sixth row, compressed into it; the first-work case study is entered here only by cross-reference, its full matrix row standing in Section 18.1 (labeled row 6 there).

*Tier letters: C = closed (pre-registered) · E = consistency evidence · M = motivation only · S = scope marker · — = not located in the verified base (Section 3.2 legend). The V4 row's tiers are the program's internal register (Section 16.2), rendered with the same letters.*

| Line | ① object | ② coverage | ③ cost | ④ neutrality | ⑤ timing | ⑥ boundary |
|---|---|---|---|---|---|---|
| L1 process [5, 6] | reasoning steps (E) | step deviations locatable; verifier process outside spectrum (E) | one verifier pass per step (E) | learned verifier; human labels as trust root (E) | dataset-level splits; run-level verdicts not located (—) | step-correct ≠ conclusion-correct (S) |
| L2 faithfulness [2, 3, 32, 33, 34, 35, 36, 37] | explanation–computation relation (E) | rationalization/insensitivity under perturbation; RL-era monitoring, open-weight quantification, and obfuscation [33, 34, 35, 37] (E) | behavioral probes, cheapest (E) | metrics are proxies (E) | per-study protocols; run-level verdicts not located (—) | protocol-relative and model-relative [35]; monitorability fragile under optimization pressure [33, 35, 36, 37] (S/E) |
| L3 evaluation [7, 8, 38, 39, 40, 41, 42, 43, 44, 45] | benchmark/protocol/pipeline (E) | leakage detectable by audit; detector family populated and itself fragile [39, 40, 41, 42, 43, 44, 45] (E) | pipeline re-analysis, moderate (E) | community + heuristics; constructors as root; detector assumptions partially validated [42] (E) | temporal discipline native; competitions institutional [38] (E) | clean score = protocol-relative performance (S) |
| L4 game-theoretic [9, 10, 46, 47, 48, 49, 50, 51, 52, 53, 54] | incentive structure; on-chain bonds for side effects [51, 52, 53] (E–M) | in-mechanism dishonesty covered; concealment [33] and verifier gaming [50] demonstrated; Goodhart-type evasion outside (E–M) | judge time + design; decentralization redistributes cost [47, 48, 49] (E–M) | judge/designer as root; consensus replaces root [47, 48, 49] (E) | rules fixed pre-interaction; bond × capability-claim unsystematized (Section 7.2) (E–M) | equilibrium ≠ deployment; audit layers erode under optimization pressure (Section 5.3) (S) |
| L5 conservation [11, 12, 13, 55, 56, 57] | invariants, physical and formal (E) | constructive: arithmetic-checkable; soft: violable off-distribution; zk verifies integrity [56] (E) | arithmetic, minimal; zk sub-linear [56] (E) | invariant external; chooser as root (E) | constructive precedes execution; run-time conservation-auditor: none located to our knowledge (Section 8.2) (—) | conservation ≠ truth (E) |
| V4 chain (this program, Sections 9–16) | the verdict chain: claim, kill-lines, verdict functions, signoff (C) | construction-failure spectrum detectable and repaired: anchor break E-15, empty-response correction, token-budget and N-min mismatches (Sections 13, 12.4); summary-layer slips detected by independent re-verification (E-37 family, Section 16.2) (C) | SHA-12 single-command recomputation against frozen files (Appendix A) (C) | PI, verdict-keeper, and independent verifier each declared a trust root (Sections 10, 12.5) (C) | kill-lines, preregistrations, and probe plans frozen before execution (Sections 12.1, 13, 14.1) (C) | composite qualification; four-kill-line scope; non-extrapolation enumeration; open-phase boundary (Sections 12.4, 12.6, 14.4, 16.3) (C) |

*Table 5: Five lines × six attributes, plus the V4 chain (compressed; full facts in Sections 4.3–8.3, and Part II for the V4 row).*

Two structural observations are visible once the assembly is complete, and both are stated at the motivation tier because they are readings of the table, not new measurements. First, the ⑤ column is the sparsest in the matrix, an observation that survived the supplement pass: across the now-60 external entries, no line's ⑤ cell records a run-level, pre-registered verdict protocol. Dataset-level splits (L1), per-study protocols (L2), held-out sets and competitions (L3), mechanism rules and bond primitives (L4), and constructive invariants (L5) are each commitment-adjacent, but none freezes a claim's kill rule before the run in the sense of Section 3.1. Second, ④ recurs across all five rows in one form or another—learned verifier, behavioral proxy, benchmark constructor, judge/designer, invariant chooser. Every line terminates in an unaudited root. The two observations are the inputs to Section 19.

In the merged matrix both observations gain one program-level counterweight, and neither is upgraded by it. The V4 row's ⑤ cell is filled at the closed tier by the phase's own protocol, and the observation about the external base—the sixty entries—stands unchanged: one program's instance does not convert a column into a practice, and the extrapolation is not drawn. The V4 row's ④ cell declares the principal investigator, the verdict-keeper, and the independent verifier as roots; the row thereby joins the others in terminating at a declared, unaudited bottom rather than exempting itself from the observation.

## 18. Case Studies under Full Parity

### 18.1 The first work: a scattering layer across the five lines

**Position and disclosure.** The paper's five lines are populated by 60 external works; this section adds one integrated instance to exercise all six attributes on a single object: the program's own first companion work [4], disclosed here and in Section 23. The case is not this paper's protagonist and receives no preferential treatment. It enters the same matrix, the same three-tier strength discipline, and the same register as the five external lines, and its negative results are reported as content. Every number below is quoted from the frozen result artifacts of [4], where each maps to a named JSON field in that work's number-traceability table; nothing is re-measured for this paper.

**The artifact.** A scattering layer over LLM reasoning-path graphs: each node is bound to a two-parameter state, and traversing energy splits into three channels—transmission, reflection, and irreversible dissipation—with the constructive identity T+R+A=1. The claim structure of [4] is itself this paper's point: the strongest claims (conservation, auditability) rest on no benchmark accuracy whatsoever, while the accuracy-attribution claims were killed by the work's own pre-registered controls.

**L1, process verification.** Elimination decisions are attributable node by node to concrete (T, R, A) shares: the audit unit sits at the step level. The conservation audit served as guarantor in one documented error correction (E9.3 of [4]): a configuration bug—one variant silently aliasing another—produced a wrong GSM8K figure of 0.86; the fixed configuration, rerun offline, gave 0.82 with 4 problems flipped (exact McNemar versus the aliased arm p=0.125, not significant; StrategyQA predictions bitwise identical, p=1.0), and the rerun passed the conservation audit. Register, as-is: a single documented event—consistency evidence—and the general claim "conservation audits catch configuration bugs" is not asserted beyond this instance.

**L2, the faithfulness analog.** The sharpest control in [4] is a six-keyword rule filter reading only label strings (E9.5): on GSM8K (n=100) it scores 0.87 against the layer's 0.85 (McNemar b=0, c=2, p=0.5); on StrategyQA (n=99) 0.899 = 0.899 (p=1.0). At these sample sizes the detectable-difference threshold is roughly ±10 percentage points, so smaller increments are not excluded—disclosed as-is. The mechanism's discriminative content equals its label input: the books are exact, but the books are not additional evidence beyond the labels. [4] relocates the value proposition accordingly—the differential value lies solely in machine verifiability—and reports the accuracy comparison without euphemism: on GSM8K, plain chain-of-thought significantly outperforms the layer (97.0 vs 85.0, exact McNemar p=4.9×10⁻⁴).

**L3 and ⑤, evaluation integrity and timing.** [4]'s verdicts are pre-registered pure functions frozen before runs, with SHA-256 anchors published for the frozen files (first 12 hex digits: GT_FORMALIZATION_v1.md aeefb8ef6972; run_v21_gtformal.py 9bbe43f41fa8; run_v22_p1c.py 6e9673205dc0; SPEC_GT2B 68a5b08ef007; SPEC_GT8C 6b09de9911c0). Every key number maps to a frozen JSON field; hand-copying is forbidden by that work's own protocol. The kills are mechanically evaluated and reported as first-class content: under a kill protocol that is systematic in its graph sampling (61 graphs, five families) and complete at the state level (all 6,760 states of the 338-task corpus), all three tiers of formalized dynamical-equivalence claims are falsified. P1a, the strong form: max deviation 0.8569—an O(1) deviation that does not vanish with step size. T-P1b, the better-response form: minimum directional cosine −1.0; minimum ΔΦ = −1.2424×10⁻², with 10/338 tasks in violation. T-P1c, the first-order entropy-regularized form, killed on both its lines: under a globally uniform τ (an 81-point grid on [0,4]) the minimum cosine is −1.0 even at the best global τ; under per-state self-chosen τ∗ the minimum cosine is −1.0, and the median per-state τ∗ is 0 (85.98% of states choose τ∗=0), so the entropy term has no reparative power. None of the three is listed as future work in [4]; the kills are the content. This is attribute ⑤ in its strongest form—the kill rules predate the runs that triggered them.

**L4, game-theoretic.** The layer's reverse dynamics is modeled as a game; [4] reports the distribution-level empirical coordination ratio (ECR)—an operational counterpart of the classical worst-case coordination ratio, explicitly not the same metric, with no numerical juxtaposition against classical bounds drawn—with median 1.333 over the 17 finite-valued graphs (three infinite cases counted separately; coverage 20/22 graphs, two graphs' arm data absent, disclosed as-is). Two closed verdicts anchor the scalar ledger: potential-trajectory monotonicity on 22/22 graphs (GT-5b—the narrowed claim; the original GT-5 endpoint reversal, the noise arm's terminal Φ overtaking on 3/4 graphs, remains on record, unrewritten), and a median non-potential residual of 1.594×10⁻²⁹ (GT-6, against a pre-registered line of 0.10; three cyclic-structure exceptions at 0.121–0.148 disclosed; the median sits at the square of the double-precision rounding scale and is not read as a physical magnitude). The potential reading survives only as an approximation: the support graphs partitioned by cycle space—acyclic (undirected-forest) graphs show residual ≤5.9×10⁻¹⁶ (indistinguishable from exact potential structure), graphs containing cycle space show median residual 0.669 with 0.924 of the mass above 0.30—hence the downgrade to an approximate potential game.

**L5, conservation.** T+R+A=1 holds by construction for arbitrary parameters; the maximum per-path audit deviation measured across all variants and benchmarks is 2.220446049250313×10⁻¹⁶—the scale of double-precision machine epsilon, against an implementation tolerance of 10⁻⁶—closed (pre-registered). Any third party recomputes the ledger with double-precision arithmetic: attribute ③'s ideal end, with the invariant external to the backend LLM (④'s strongest form, the parameter-assignment table remaining the trust root).

**Limitations, self-stated (compressed from [4]).** The corpus graph families are single-vendor LLM-generated (all three tested model families Chinese-optimized; shared-corpus contamination not ruled out); real-benchmark samples are small (n=100 GSM8K, n=99 StrategyQA); apart from the closed verdicts and the kills, the game-theoretic positive evidence is consistency evidence, not formal proof; ECR coverage is 20/22; the benefit of the irreversible-dissipation channel remains motivation only—zero task-level rent on every task measured, with the mechanistic premise (dissipation guarantees the spectral condition that prevents divergence in 58/338 tasks at the zero-dissipation setting) kept distinct from the rent claim.

**Matrix row 6.**

| Attribute | Fact (with pointer) | Tier |
|---|---|---|
| ① commitment object | per-path energy ledger with node-attributable (T,R,A) shares; verdict functions over frozen JSONs [4] | C |
| ② tamper-spectrum coverage | constructive identity covers ledger deviations, arithmetic-checkable; label-content deviations are outside the ledger's spectrum (E9.5) [4] | C |
| ③ recomputation cost | double-precision arithmetic per path [4] | C |
| ④ verifier neutrality | invariant external to the backend LLM; parameter-assignment table single-sourced; single-vendor graph families disclosed [4] | C/E |
| ⑤ commitment timing | SHA-256-anchored pre-registered verdict functions; kills mechanically evaluated and reported [4] | C |
| ⑥ distortion boundary | no accuracy claims: E9.5 tie, GSM8K 85.0 vs 97.0 as-is; three equivalence claims falsified; potential downgraded to approximate, partitioned by cycle space [4] | C |

*Matrix row 6: the first work entered at full register (Section 18.1) and compressed to the matrix row here.*

### 18.2 The V4 chain at the same register

The second case study is the V4 chain itself. Unlike the first work, whose five-line treatment is compressed into Section 18.1 from a longer external record, the V4 chain's case study was filed in Part II at full length, in this paper's own sections: the governance trail (Section 10), the formal FAIL and its composite qualification (Sections 11–12), the triage pipeline (Section 13), the N-26 true audit (Section 14), and the GLM_2 line (Section 15). This section therefore adds no numbers and restates no verdicts; it records the parity conditions under which both case studies stand in this paper.

1. Both cases enter the same register as the external lines: commitments made before execution or disclosed up front, literal verdict wording, tiered evidence labels, and disclosed construction doubts.
2. Both cases' negative results are reported as content, not as apology: the first work's three falsified equivalence claims and its accuracy-attribution kills; the V4 phase's formal FAIL and its one true falsification.
3. Neither case is this paper's protagonist. The external lines populate the matrix; the two program cases instantiate it; the synthesis of Section 17 states what the instantiation adds—one run-level ⑤ entry and one declared-bottom ④ entry—and nothing else.

Under these conditions the merged draft's title carries both halves deliberately: keeping the books (the five-line coordinate system, Part I) and walking with the verdicts (the V4 chain, Part II).

## 19. Cross-Line Lessons Revisited

The survey's four cross-line lessons, read across the five external lines, each meet the V4 chain at a specific point or at a declared absence. Each lesson is stated first, as carried from Part I's records; the V4 anchor follows.

**(a) Pre-registration and kills as trust infrastructure.** Read across the five lines, the recurring distinction between claims that survive scrutiny and claims that evaporate is the presence of a frozen rule before execution. L3's temporal discipline is the community-scale version [7, 8]; reproducibility checklists are the commitment stage executed institutionally [8]. The register matters as much as the mechanism. A kill is a completed audit—the strongest form a negative result can take—and a field that reports kills without reputational collapse converts its error rate into knowledge. This paper practices the register it describes: the first case study of Section 18.1 enters with three falsified claims and no apology for them. The observation that the external ⑤ column is empty of run-level verdict protocols (Section 17.3) is the gap side of the same lesson: the infrastructure exists in fragments, in none of the five lines as standard practice.

*V4 anchor.* The phase instantiates the lesson end to end. The four kill-lines were frozen before the Task B runs, and all four hit (Section 12); the N-26 audit was pre-registered before execution, and its one true falsification is recorded in the strongest form the phase's negative results take (Section 14); the T-series registered each probe before running it (Section 13); the signoff re-computed the verdict before accepting it (Section 12.5). The phase's addition to the lesson is the demonstration that the register survives contact with a formal FAIL: the kill was filed, not softened, and the construction doubts that surfaced were adjudicated by an append-only chain rather than by rewrite (Section 10).

**(b) The economics of verification cost.** Attribute ③ is not metadata; it decides whether audit happens at all. Cheap audits become habitual; expensive audits stay episodic; and no-cost "audits"—trusting the score—are the default the field is trying to leave behind. The cost ladder visible in the matrix runs from arithmetic recomputation of a constructive invariant (L5, minimal) through behavioral probes (L2, cheap) and verifier forward passes (L1, learned-model cost) to pipeline re-analysis (L3, moderate) and judge time plus mechanism design (L4, the most open-ended). Incremental structures—append-only records, recomputation of only what changed, single-command recomputation as the ideal end—reduce cost without reducing coverage. The economic claim itself, that auditability must be priced for habitual use, is stated at the motivation tier: no cost-measurement study is located in the verified base, and the claim is falsifiable by exactly such a study (OP6 in Section 20.2).

*V4 anchor.* The chain's cost structure was designed for habit, and its design choices are recorded: every verdict number lands on a path, a byte count, and a SHA-12 digest (Appendix A), so that recomputation is a single command against a frozen file rather than a re-run of an experiment; the errata chain is append-only, so that a correction costs one entry rather than a rewrite; and the composite qualification prices the residual uncertainty in words rather than in further compute (Section 12.4). No cost-measurement study of this paper's own audit practice is recorded—the economics lesson of OP6 stands, and this paper does not claim its own audit costs are measured: they are minimized by construction and asserted, not priced.

**(c) The escrow × capability-claim combination, documented as unsystematized.** Three neighboring clusters bound the position (Section 7.2): general mechanism-design theory [46], which has not reached ML claims; decentralized LLM evaluation [47, 48, 49], without bond–forfeiture structures; and on-chain agent governance [51, 52, 53], whose bonds escrow behavioral side effects rather than capability claims. The combination—attach a forfeitable bond to a falsifiable capability claim, with a mechanical forfeiture verdict—would sit at the intersection of L4 (incentive design) and ⑤ (commitment devices): it prices dishonesty in the currency the claimant already spends. Documenting the unsystematized step is a survey contribution carried into this paper; the exploratory possibility is stated with no claims attached.

*V4 anchor: none.* The chain escrows nothing: no bond, no forfeitable stake, no mechanism pricing dishonesty in the claimant's currency. The lesson's unsystematized status is imported unchanged; the phase's governance runs on declared trust roots and append-only records (Section 10), not on incentive design. Mapping the V4 chain onto this lesson would require exactly the step the survey documents as missing, and this paper does not take it.

**(d) The recursion bottom.** Every line's ④ cell terminates in an unaudited root (Section 17.3): the learned verifier, the faithfulness metric, the benchmark constructor, the judge and mechanism designer, the invariant chooser. Audit stacks have bottoms. The dishonest response is to hide the bottom; the honest response is to declare it, and attribute ⑥ is where the declaration lives. A reliability literature that states its trust roots keeps better books than one that proves everything above an unexamined foundation, and this paper records this as a register requirement rather than a technical one. The register requirement has a dynamic counterpart with three testimonies: an audit layer placed under optimization pressure erodes—chain-of-thought monitoring driven to concealment while task metrics improve [33]; verifiers gamed by the training signal that optimizes against them [50]; evaluation protocols absorbing the gaming pressure aimed at them [47, 48, 49]. The proposition is stated at motivation tier (a cross-line synthesis, not a measured law), and its three testimonies, taken together, are the matrix's most direct reading of where ② coverage fails in practice (Sections 5.3 and 7.2).

*V4 anchor.* The chain's bottoms are declared rather than hidden: the principal investigator as the commissioning root, the verdict-keeper as the adjudicating root, the independent verifier as the signoff root—each named as a root in the phase's own records and re-declared in Part II (Sections 10 and 12.5). Attribute ⑥ is where the declaration lives, and the V4 row of the merged matrix carries it (Section 17.3). The lesson's dynamic warning—audit layers erode under optimization pressure—has no recorded instance in the phase: no optimization pressure was applied to the chain's own audit layers, and this paper records no immunity claim either way.

## 20. Outlook: Machine Worldviews, AI Scientists, and the Open Phase

### 20.1 Machine worldviews and AI scientists

Two research programs bring the audit problem to a head. The first builds machine worldviews. An agent learns a generative model of its environment and trains its policy inside that model [58]; a single configuration scales the approach across diverse domains [59]; generation now extends to interactive environments produced from text [60]; and the line has been surveyed systematically [61]. Read with this paper's vocabulary, a world model is a machine-written book of the world, and the audit question becomes L2's question scaled from single explanations to entire worldviews: what is the relation between the learned book and the world? The book's own provenance—data, training, unaudited assumptions—is L3's question at one remove. No faithfulness metric for world models is located in the verified base.

The second program automates the claimant. AI-scientist systems attempt the full research cycle of idea generation, experimentation, and write-up [62]; agent laboratories compose LLM agents into research workflows [63]; and autonomous systems plan and execute chemistry experiments [64]. The audit problem is then exact: machine-generated knowledge claims entering the human record need the same commitment–execution–verification loop as human claims—frozen artifacts, pre-registered verdicts, external witnessing, recomputable derivations. Today the outputs of these systems are claims with run logs; the bookkeeping that would make them third-party-recomputable is, to the verified base, absent. The matrix applies without modification: ① the discovered claim plus its derivation; ② the agent's own edits and selections; ③ rerun cost as the binding constraint (autonomous-agent recomputation is expensive—the projected binding ③ of the coming decade, and the cryptographic route of Section 8.1 is the one located lever for relieving it [56]); ④ the human-review interface (what does a human auditor check when the books are machine-written); ⑤ pre-registration for machine hypotheses; ⑥ the discovered claim's support scope. This outlook is register-capped at motivation only: no evidence for any of these audit layers is located in the verified base, and the cap is the honest form of the claim.

### 20.2 Open problems

Each problem is stated with its falsifiability condition where one exists; the framing positioning claim was last checked by the completed novelty search and retained (Section 1.2).

1. **OP1 (L2's recursion).** A faithfulness metric that is itself auditable: an instrument whose own books can be recomputed. The verified base locates no candidate.
2. **OP2 (L3).** The auditors of the auditors. The contamination-detector family exists [39, 40, 41, 42, 43, 44]; its own core assumptions are only partially validated [42]; and its fragility for reasoning models is demonstrated [45]. The open step is a pre-registered, assumption-validating comparison protocol for detection methodology.
3. **OP3 (L4).** The escrow × capability-claim combination—attach bond-settlement primitives [51, 52, 53] to falsifiable capability claims, with mechanical forfeiture verdicts (Section 7.2). The components exist; the step is unsystematized.
4. **OP4 (L5).** Conservation-as-auditor beyond the single case. Run-time invariant audit has, to our knowledge, one ML-artifact instance (Section 18.1); open ahead are the methodology generalization and the invariant-monitoring line (Section 8.2).
5. **OP5 (L2).** Faithfulness evidence for the reinforcement-learning-trained chain-of-thought era has begun arriving [32, 33, 34, 35, 37], from monitoring [33] to open-weight quantification [35]. What is open is systematization—protocol-relativity discipline and standardized probes that make monitorability numbers commensurable.
6. **OP6 (③ quantified).** Cost-measurement studies for audit protocols: what recomputation actually costs, measured rather than asserted. Until such studies exist, the economics lesson of Section 19(b) stays at motivation only.
7. **OP7 (the interface).** Human review of machine-written books—granularity, tooling, and the division of labor between human auditors and machine ledgers (Section 20.1).
8. **OP8 (the field's own ⑤).** Run-level pre-registered verdict protocols for reasoning claims—the sparsest column of the assembled matrix, now across 60 external entries. The case study of Section 18.1 and the V4 chain of Part II are demonstrated instances; the open problem is the practice becoming ordinary.

The five lines keep their books in different currencies—steps, explanations, benchmarks, equilibria, invariants—but the exchange rate is the one this paper has traded in throughout: a claim about reasoning is worth what a stranger can recompute of it. Keep the books.

### 20.3 The program's open phase

The V4 phase is open at writing time; this merged draft reports the recorded state and closes nothing. What can be stated about the phase's continuation is plan-level, carried at the exploratory tier, and attaches no results: the program's recorded plan for its next phase lists five threads—continued design work on the PI's thought-chain distillation; quantification of the N-26 indistinguishability face; maintenance of the supplementary-measurement line; continuation of the release line; and the rule that any positive result is frozen under the same discipline before it is believed. No schedule, no expected outcome, and no feasibility claim attaches to any thread; the threads carry no verdict numbers because none exists; the recording of a plan is not a prediction.

## 21. Limitations

(1) The composite qualification stands: the four construction doubts (recall-form metric, 22-item resampling, single-event blind-obedience rate, D1 absences plus two-day span) are recorded and unresolved; the verdict's scope is clamped accordingly. (2) The day-span criterion was met by a recorded PI supersede, not by measurement; this paper reports it as a ruling. (3) The five version-pending items leave some V3 report-layer references version-suspended until the PI's final ruling. (4) The N-26 teacher-side sample is uneven (77 calls for one teacher against 110 or more for the others), as disclosed in the audit. (5) Companion-work citations are frozen at writing-day digests; the second work's update will change its digest, and its formal publication record, if any, supersedes the internal citation. (6) The V4-line zone of this paper inherits a draft composed in one day and in English; the merged draft itself was assembled in one day (v0.1), revised in same-day rounds (v0.2 and v0.3), and revised in a next-day registration round (v0.4, registration layer only); review, typesetting, and any Chinese edition remain downstream stages. (7) Every claim in this paper is bounded by the recorded construction domains, sample sizes, and qualifications of its source verdicts, and by the non-extrapolation enumerations carried in Sections 12.6, 14.4, and 16.3.

Two further limitations attach to the merge itself. (8) The merged-draft status: Part I is merged from a survey manuscript that was never submitted and will not be submitted—this paper is its only public carrier—and its citation base is frozen as of the 2026-09-15 novelty search, carrying the 30-day freshness clause of Section 22.4; the self-overlap measurement of the merged text is deferred to the typesetting round (Section 22.5). (9) The merge is a drafting operation: the survey zone and the verdict zone were written under different commission chains, and this draft (v0.1 assembled, revised through v0.2 and v0.3 on the same day and through v0.4 on the next day, the latter a registration-only round) is their first combined presentation; an advisory three-way review of the combined form was recorded in the program's working chain on 2026-09-27, with pass verdicts on all three lines, of which the v0.3 round applied the registered non-blocking items while the v0.4 round registers the externally issued re-adjudication record in the registration layer, and the formal review and typesetting stages remain downstream; the sequence of drafting passes (blueprint, drafting, assembly, revision) is recorded in Appendix C.

## 22. Data Availability, Provenance, and Self-Overlap

### 22.1 The ledger and its two faces

Appendix A is the consolidated internal asset ledger: path, byte count, SHA-12, for every internal item cited in this paper. In-repository values were re-measured on 2026-09-26 and match the independent pre-delivery audit's values. The dataset family (the v1.1 dataset and its nine addenda) and the letters family (the upload application and scoping letters, and the phase's v4 commission letter itself) are held on the PI's local face, are not part of the public workspace, and are cited at the values recorded in the phase's commission ledger, marked as such in the appendix. Remote-face identifiers are intentionally absent from this draft: per the phase's citation rule, this paper names no repository URL and fills in no remote commit or blob identifiers. The merged draft adds its own input anchors—the unpublished survey source, the V4-line source pair, and (at the v0.2 revision round) the E-37 re-verification evidence file—in a dedicated subsection of the same appendix; the v0.2 round also registers the second work's ready-for-resubmission revised edition at the workspace delivery face, with its repository-archival anchor pending.

### 22.2 Privacy, keys, and content boundaries

The Task B dataset is cited by path and digest only; its content (the PI's full reasoning chains) is never quoted, reproduced, or characterized beyond the verdict numbers, and no key of any kind appears in this paper (the R4 purge records of Section 10 attest the key purge). The confidential weekly-report material in the program's possession is not cited, not quoted, and not pointed to anywhere in this paper; every number in this paper traces to on-disk public-chain artifacts only.

### 22.3 The source face (compact statement)

The source face of this paper's V4-line zone is recorded compactly: a v4 commission letter and an upload scoping decision letter (cited in the appendix at their recorded values), an upload that was in progress at writing time, and five version-pending items (v19_fullrank, v20_baselines, v20_cot_quiz, v20_photonics, v20_quiz_eval), each of which is recorded here as *pending PI final ruling*, with no version chosen by this paper. The two archive-resident items recorded as strictly excluded (among the 13; the second-work PDF is one of them) exist on the local disk and are outside the upload face: the second work is anchored in this paper at its local on-disk value only, and a reader relying on the upload face alone cannot reach it. A reader with workspace access can recompute every verdict number in this paper from the anchored files: the kill-line values from the result and verdict files, the root-cause attributions from the verdict's decision table, the pipeline stages from the T-series verdicts, and the audit from the N-26 verdict and its preregistration.

As of 2026-09-27, the release execution on the public repository face completed 415-of-415 fingerprint-consistent items (the 415-item and 42-commit counts are recomputable from the public release history, in which the 2026-09-26 release batch is recorded; the fingerprint-consistency result itself is carried per the release receipt's own wording). Two arithmetic inconsistencies internal to the release receipt are carried per the receipt's own wording and registered as pending verification (among them a stated 342 − 51 = 294, where the arithmetic gives 291); this paper does not correct the receipt, and the circled face and the executed face are recorded side by side, each at its own wording, per the program's convention of recording both faces without merging them.

### 22.4 The survey-base provenance (condensed)

Part I is merged from a survey manuscript that was never submitted for publication and will not be submitted; this paper is its only public carrier. Its citation base was closed by construction: 61 entries—60 external references verified across three passes (27 in the original verified pass, 27 in the supplement pass that filled the survey's five literature gaps, and 6 added with the completed novelty search of 2026-09-15, a multi-engine retrieval whose query families were auditability, reproducibility, verifiability, verification, integrity, and accountability × survey × LLM/reasoning/test-time, plus per-line targeted searches and adjacent-survey tracking—the families named by the Section 1.2 pointer), plus the disclosed first-work entry [4]. The base's operative rules are carried into this draft: closure (nothing outside the base is cited, and nothing has been added from memory); recorded-granularity rendering (entries carry the field completeness their verification records support, and pending fields are marked as pending rather than filled); facts, not rankings (the matrix records what the verified base supports, with the neutrality clause of Section 3.2 keeping it reusable by readers who disagree); and the freshness clause (the novelty search carries a 30-day re-run obligation that this merged draft inherits: if submission is delayed more than thirty days beyond the search date, the search is re-run under the same query families before submission). The clause's dates, stated plainly: the search completed on 2026-09-15, and the thirty-day window closes on 2026-10-15; at this draft's writing day (2026-09-27) the window is still open, and the pipeline stages ahead of submission are review and typesetting, so the re-run obligation is live and not discharged; this draft makes no prediction of its triggering.

The survey reported no new experiments and measured no new numbers; every number in the first-work case study (Section 18.1) is quoted, not re-measured, from the frozen result artifacts of [4], where each maps to a named field in that work's number-traceability table. The same discipline is carried by this paper: Part III's synthesis adds no measurement, and the two case studies' registers are disclosed in Sections 18.1 and 23.

### 22.5 Self-overlap disclosure

The survey's own single-work self-overlap precedents are on record: a 10-gram word-level overlap of 4.62% within its case-study section and 0.21% across its remainder, measured against the first work, with matched fragments consisting of the declared anchored material and shared reference titles; the program's 8-gram records against the first work stand at 0.91%. Because Part I is merged in full from that source and Part III merges its synthesis sections, this merged draft's overlap against the first work's published material and against the second work is expected to be substantially higher than the survey's single-work values, and the disclosure category is correspondingly renamed: the overlapping material is *merged-in coordinate-system material*, carried from the program's own unpublished sources under the merge plan registered in Appendix C, not third-party text. The quantitative 8-gram self-overlap measurement of the assembled draft against the first and second works is deferred to the typesetting round, per the program's precedent; the value will be filled into Appendix C's registry at that round.

## 23. AI-Use Disclosure

This paper was produced by a multi-agent AI pipeline under the PI's commission: a literature scout, an algorithm architect, an experiment analyst, a paper writer, and a formatting specialist, with independent audit roles for asset verification and reference-merging review. The drafting model is GLM. All statements in this paper that involve GLM are anchored to the PI's GitHub repository as the sole authoritative source. All included references were verified by independent literature-verification passes before inclusion; no citation outside the verified base was added by the drafting pipeline, and no bibliographic field has been supplied from memory.

Both case studies are the program's own works. The first-work case study [4] is disclosed here and in Section 18.1; it receives the same matrix treatment and register as the five external lines, and its negative results are reported as content. The V4-chain case study is the commissioning program's own phase record, filed in Part II at the same register. The merged draft was assembled by the paper-writer role from two source manuscripts under an architecture blueprint and a reference-merging plan, both recorded in the program's working chain; the assembly applied a unified citation renumbering, pointer remapping, and the self-checks registered in Appendix C. Final responsibility for all content rests with the principal investigator, following the program's disclosure convention.

## 24. Conclusion

This paper merged two lines of one program into a single account. The first line built a five-line audit coordinate system over 60 external works and found, assembled, that its sparsest column—run-level, pre-registered verdict protocols—was empty of every external entry. The second line ran one such protocol end to end, pre-registered four kill-lines, adjudicated a formal FAIL with a composite qualification, triaged its construction doubts through a registered pipeline, re-audited a proposition to a true falsification, and signed the result off by independent recomputation. The merge exists because the two lines answer each other: the coordinate system's empty column is what the verdict chain fills, and the verdict chain's discipline is what the coordinate system prices. The program's contribution to the open problem OP8 is exactly one entry at the recorded scope—one run-level protocol, at the recorded construction domains, samples, and qualifications—and the extrapolation beyond it is not drawn.

What the phase's failures establish is filed at its own scope, in Part II's words and numbers, and is not re-summarized here in softer ones. Negative results are the program's assets: the kills are filed so they cannot be un-killed by narrative, and the errata chain that repaired the record on the way is part of the result, not an apology for it. The five lines keep their books in different currencies; the exchange rate never changed—a claim about reasoning is worth what a stranger can recompute of it—and the program's own books, kept to that rate, are open on the workbench, not closed on a shelf.

Boundary note (merged draft, 2026-09-27): the V4 phase is open at writing time; this merged draft reports the recorded state and closes nothing.

---

# References

*Entry-format note (carried from the survey source and retained): the citation base is numbered in a single first-appearance sequence across the paper. Entries are rendered at the field completeness their verification records support: where the verification pass recorded a pending field (venue, subtitle, or authors beyond those listed), the entry carries the pending marker rather than a filled guess; non-peer-reviewed entries are labeled as such (e.g., [34], [54]); entries are reported at the recorded granularity of the verification passes. No bibliographic field has been supplied from memory. The base is closed: 61 entries carried from the survey source (60 external plus the disclosed first-work entry), plus 3 entries carried from the V4-line source (Nosek; Popper; Yang), unified into one first-appearance sequence at the assembly round; three same-work merge points were resolved at assembly (the first-work entry, unified to one anonymized companion-work entry; one arXiv identifier shared between the V4-line source and the survey's candidate pool, resolved to the single entry [20]; and one arXiv identifier internal to the survey's pool, resolved to the survey-side entry [41]); and no new citation is added by this draft.*

[1] Wei et al. "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." NeurIPS 2022. arXiv:2201.11903.

[2] Miles Turpin, Julian Michael, Ethan Perez, and Samuel R. Bowman. "Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting." NeurIPS 2023. arXiv:2305.04388.

[3] Tamera Lanham et al. "Measuring Faithfulness in Chain-of-Thought Reasoning." TMLR 2023. arXiv:2307.13702. (30 authors per the arXiv record.)

[4] Attribution withheld for double-blind review. "Deposon: An Auditable, Conservation-Guaranteed, Game-Theoretically Tested Scattering Layer over LLM Reasoning Paths." The program's first companion work, 2026. (The author block and publication identifiers are withheld per the double-blind convention; the work is anchored in this paper at its on-disk record — Appendix A and Section 1.2 — and publication identifiers, if any, are reserved to the principal investigator's authoritative records.)

[5] Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, and John Schulman. "Training Verifiers to Solve Math Word Problems." arXiv:2110.14168, 2021.

[6] H. Lightman et al. "Let's Verify Step by Step." arXiv:2305.20050, 2023. (Remaining authors pending completion; venue pending verification; arXiv cited.)

[7] Sayash Kapoor and Arvind Narayanan. "Leakage and the reproducibility crisis in machine-learning-based science." Patterns 4(9):100804, 2023. DOI: 10.1016/j.patter.2023.100804. (Preprint: arXiv:2207.07048, 2022, under the title "…ML-based Science.")

[8] Pineau et al. "Improving Reproducibility in Machine Learning Research" [subtitle pending verification]. JMLR 22(164), 2021. (Per the verification record: jmlr.org, vol. 22, paper 20-303.)

[9] Geoffrey Irving, Paul Christiano, and Dario Amodei. "AI Safety via Debate." arXiv:1805.00899, 2018.

[10] V. Conitzer et al. "Foundations of Cooperative AI." AAAI 2023 (ojs.aaai.org, AAAI-23).

[11] S. Greydanus et al. "Hamiltonian Neural Networks." NeurIPS 2019. arXiv:1906.01563.

[12] George Em Karniadakis, Ioannis G. Kevrekidis, Lu Lu, Paris Perdikaris, Sifan Wang, and Liu Yang. "Physics-informed machine learning." Nature Reviews Physics 3:422, 2021. DOI: 10.1038/s42254-021-00314-5.

[13] Aditi S. Krishnapriyan, Amir Gholami, Shandian Zhe, Robert M. Kirby, and Michael W. Mahoney. "Characterizing possible failure modes in physics-informed neural networks." arXiv:2109.01050, 2021.

[14] Bérénice Jaulmes, Jean-Christophe Arouete, Mariam Barry, and Mehwish Alam. "A Survey on Verifying Reasoning Chains Generated by Large Language Models." HAL: hal-05448955, 2026. (Institutional-repository archive; publication venue pending determination.)

[15] Venktesh, Rathee, and Anand. "Trust but Verify! A Survey on Verification Design for Test-time Scaling." arXiv:2508.16665, 2025.

[16] Gu et al. "A Survey on LLM-as-a-Judge." arXiv:2411.15594, 2024. (Journal version, 2026: The Innovation, per the verification record.)

[17] Chang et al. "A Survey on Evaluation of LLMs." ACM Transactions on Information Systems 15(3):1–45, 2024. arXiv:2307.03109. DOI: 10.1145/3641289.

[18] B. A. Nosek, C. R. Ebersole, A. C. DeHaven, and D. T. Mellor. The preregistration revolution. *Proceedings of the National Academy of Sciences*, 115(11):2600–2606, 2018. doi:10.1073/pnas.1708274114.

[19] K. R. Popper. *The Logic of Scientific Discovery*. Hutchinson and Co., London, 1959. English edition of *Logik der Forschung* (Julius Springer, Vienna, 1934).

[20] G. Yang, Y. Liu, S. Miao, et al. LLMs judge themselves: A game-theoretic framework for human-aligned evaluation. *arXiv:2510.15746*, 2025.

[21] Scott Walter. "The Non-Euclidean Style of Minkowskian Relativity." In *The Symbolic Universe*. Oxford University Press, 1999. (Author copy: scottwalter.free.fr.)

[22] E. T. Jaynes. "Information Theory and Statistical Mechanics." Physical Review 106:620–630, 1957. DOI: 10.1103/PhysRev.106.620.

[23] Eugene P. Wigner. "The Unreasonable Effectiveness of Mathematics in the Natural Sciences." Communications on Pure and Applied Mathematics 13(1):1–14, 1960. DOI: 10.1002/cpa.3160130102.

[24] R. Landauer. "Irreversibility and Heat Generation in the Computing Process." IBM Journal of Research and Development 5(3):183–191, 1961. DOI: 10.1147/rd.53.0183.

[25] Hirotaka Osawa, Dohjin Miyamoto, Satoshi Hase, Reina Saijo, et al. "Visions of Artificial Intelligence and Robots in Science Fiction: a computational analysis." International Journal of Social Robotics 14(10):2123–2133, 2022. (DOI pending verification; author list beyond the fourth pending completion.)

[26] Johnson. *Science Fiction Prototyping*. Morgan & Claypool, 2011.

[27] Appio et al. (with Yaszek; full list pending completion). "Science Fiction and the Quest for Innovation." Technovation 141:103172, 2025. DOI: 10.1016/j.technovation.2025.103172.

[28] Kiri L. Wagstaff. "Machine Learning that Matters." ICML 2012 (Proceedings of the 29th ICML). arXiv:1206.4656. (Critique; motivation tier.)

[29] Zachary C. Lipton and Jacob Steinhardt. "Troubling Trends in Machine Learning Scholarship." arXiv:1706.06569, 2017. (Also: ACM Queue, 2019. Critique; motivation tier.)

[30] B. Nielson. "Induction, Popper, and machine learning." arXiv:2110.00840, 2021.

[31] Oliver Buchholz and Eric Raidl. "A Falsificationist Account of Artificial Neural Networks." arXiv:2205.01421, 2022. (Journal version, 2025: DOI: 10.1086/721797; journal name pending verification.)

[32] D. Guo et al. (DeepSeek-AI). "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning." arXiv:2501.12948, 2025. (Also published in Nature, 2025.)

[33] Bowen Baker, Joost Huizinga, Leo Gao, Zehao Dou, Melody Y. Guan, Aleksander Madry, Wojciech Zaremba, Jakub Pachocki, and David Farhi (OpenAI). "Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation." arXiv:2503.11926, 2025.

[34] Anthropic. "Reasoning Models Don't Always Say What They Think." Institutional research report, anthropic.com, 2025-04-03. (Non-peer-reviewed; labeled as such.)

[35] Young. "Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?" arXiv:2603.22582, 2026.

[36] Tomek Korbak et al. "Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety." arXiv:2507.11473, 2025. (Position paper.)

[37] A. Zolkowski et al. "Can Reasoning Models Obfuscate Reasoning? Stress-Testing CoT Monitorability." arXiv:2510.19851, 2025.

[38] D. Sculley et al. "Position: AI Competitions Provide the Gold Standard for Empirical Rigor in Generative AI." ICML 2025, Position Track (PMLR). (Position track.)

[39] Shuo Yang, Wei-Lin Chiang, Lianmin Zheng, Joseph E. Gonzalez, et al. "Rethinking Benchmark and Contamination for Language Models with Rephrased Samples." arXiv:2311.04850, 2023. (Author list beyond the fourth pending completion.)

[40] Yonatan Oren, et al. "Proving Test Set Contamination in Black Box Language Models." ICLR 2024. arXiv:2310.17623. (Author list beyond the first pending completion.)

[41] Mathieu Ravaut, Bosheng Ding, Fangkai Jiao, et al. "A Comprehensive Survey of Contamination Detection Methods for Large Language Models." TMLR 2025. arXiv:2404.00699. (Author list beyond the third pending completion.)

[42] Yujuan Fu, Ozlem Uzner, Meliha Yetisgen, and Fei Xia. "Does Data Contamination Detection Work (Well) for LLMs? A Survey and Evaluation on Detection Assumptions." Findings of the Association for Computational Linguistics: NAACL 2025, pp. 5250–5271. DOI: 10.18653/v1/2025.findings-naacl.291. arXiv:2410.18966.

[43] J. Dekoninck, Müller, and Vechev. "ConStat: Performance-Based Contamination Detection in Language Models." NeurIPS 2024, Datasets and Benchmarks Track (proceedings.neurips.cc; no independent arXiv identifier located).

[44] Yongding Tao, Tian Wang, Yihong Dong, Huanyu Liu, Kechi Zhang, Xiaolong Hu, and Ge Li. "Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models." arXiv:2510.09259, 2025.

[45] Wang, Li, Ko, and Zhang. "On the Fragility of Benchmark Contamination Detection in Reasoning Models." CoRR abs/2510.02386, 2025. (ICLR version on record.)

[46] Ian Ball and Deniz Kattwinkel. "Probabilistic Verification in Mechanism Design." Theoretical Economics, vol. 20, no. 4, 2025, pp. 1247–1284. DOI: 10.3982/TE6266.

[47] Sahil Pardasani and Madhusudan Singh. "Who Verifies the Benchmark? Decentralizing Trust in Large Language Model Evaluation." arXiv:2608.07762, 2026. Accepted to the International Conference on Quantum Enhanced AI and Secure Computing (QASC 2026).

[48] Yifan Yang, Jinjia Li, Kunxi Li, Puhao Zheng, Yuanyi Wang, Zheyan Qu, Yang Yu, Jianmin Wu, Ming Li, and Hongxia Yang. "InfiCoEvalChain: A Blockchain-Based Decentralized Framework for Collaborative LLM Evaluation." arXiv:2602.08229, 2026.

[49] Jianxiang Peng. "DEP: A Decentralized Large Language Model Evaluation Protocol." arXiv:2603.01167, 2026.

[50] Helff et al. "LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking." arXiv:2604.15149, 2026. (OpenReview record; full author list per the arXiv page.)

[51] Laurent Bindschaedler, Quentin Botha, and Christoph Siebenbrunner. "Bonded Recourse for Smart-Contract Settlement of Compensable Agent Side Effects." arXiv:2609.01939, 2026. Accepted at BCCA 2026 (IEEE International Conference on Blockchain Computing and Applications).

[52] Anuj Kaul, Qianlong Lan, and Pranay Gupta. "Behavioral Governance for Autonomous AI Agents: The AgentBound Framework." arXiv:2606.30970v2, 2026. (v1 title: "AgentBound: Verifiable Behavioral Governance for Autonomous AI Agents.")

[53] Srinath Perera, Kaviru Hapuarachchi, Frank Leymann, and Rania Khalaf. "Robust Agent Compensation (RAC): Teaching AI Agents to Compensate." arXiv:2605.03409, 2026.

[54] ERC-8004: Trustless Agents. Ethereum Improvement Proposal draft, created 2025-08-13. https://eips.ethereum.org/EIPS/eip-8004. (Engineering-standard draft; non-peer-reviewed; labeled as such.)

[55] C. Sidrane, A. Maleki, A. Irfan, and M. Kochenderfer. "OVERT: An Algorithm for Safety Verification of Neural Network Control Policies for Nonlinear Systems." JMLR 23, 2022. (Volume/pages pending verification; per the verification record: jmlr.org.)

[56] Haochen Sun and Jason Li. "zkLLM: Zero Knowledge Proofs for Large Language Models." ACM CCS 2024. arXiv:2404.16109.

[57] Z. Peng, C. Zhao, T. Wang, et al. "A survey of zero-knowledge proof based verifiable machine learning." Artificial Intelligence Review 59:157, 2026. DOI: 10.1007/s10462-026-11557-y. arXiv:2502.18535.

[58] David Ha and Jürgen Schmidhuber. "World Models." arXiv:1803.10122, 2018.

[59] Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, and Timothy Lillicrap. "Mastering Diverse Domains through World Models." arXiv:2301.04104, 2023.

[60] Jake Bruce et al. "Genie: Generative Interactive Environments." arXiv:2402.15391, 2024. (25 authors per the arXiv record.)

[61] Jingtao Ding et al. "Understanding World or Predicting Future? A Comprehensive Survey of World Models." arXiv:2411.14499, 2024; ACM Computing Surveys, 2025. (Author list beyond the first pending completion.)

[62] C. Lu et al. (Sakana AI). "The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery." arXiv:2408.06292, 2024. (Venue pending verification; arXiv cited.)

[63] S. Schmidgall et al. "Agent Laboratory: Using LLM Agents as Research Assistants." arXiv:2501.04227, 2025. (Venue pending verification; arXiv cited.)

[64] Daniil A. Boiko, Robert MacKnight, Ben Kline, and Gabe Gomes. "Autonomous chemical research with large language models." Nature 624:570, 2023. DOI: 10.1038/s41586-023-06792-0.

---

# Appendix A: Internal Asset Ledger

All in-repository values in this table were measured on 2026-09-26 (on-disk SHA-12, uppercase). Items marked [L] are held on the PI's local face, are not in the public workspace, and carry the values recorded in the phase's commission ledger. Items marked [R] are recorded anchors carried in repository texts, not independently re-measurable files. The five version-pending items are listed without version choice, pending PI final ruling. Rows and notes added at the v0.2 revision round are marked inline and were measured on 2026-09-27; rows and notes added at the v0.4 registration round are marked inline, with on-repository rows measured on 2026-09-28 and letters-family rows carried as fingerprint transfers (recorded or self-reported, as annotated per row).

### Task B chain (v2.2)

| Path | Bytes | SHA-12 |
|---|---|---|
| `results/_v4_pi_cot_v2_prereg.md` | 4,247 | CC25C5149CE1 |
| `results/_v4_pi_cot_v2_ruleset_v2.json` | 6,179 | C5B3DD141655 |
| `results/_v4_pi_cot_v2_ruleset_v2_executor.py` | 52,465 | EB22F13D571C |
| `results/_v4_pi_cot_v2_result_v2.json` | 18,089 | F86727C857A8 |
| `results/_v4_pi_cot_v2_verdict.md` (exploratory first verdict) | 22,340 | EB9AD4193CF2 |
| `results/_v4_pi_cot_v2_verdict_v2.md` (formal verdict) | 33,723 | 5D79E67A4E9D |
| `results/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` (v0.2 note, measured 2026-09-27, pending PI ruling: a second copy of this signoff exists on the same public disk at `_september_workspace/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md`, 26,633 B, SHA-12 `739245682D40`, 4 bytes apart from the cited copy; the two copies are registered as coexisting, the values cited in this row remain the commission-ledger pair, and which copy is authoritative is pending the PI's ruling; v0.4 note, 2026-09-28, per the E-37 exception-channel precedent: a letters-family calibration note self-reports this file at the cited pair (26,637 B, SHA-12 `BA4D07BD7000`; self-reported, the note not being on-repository and its report not recomputable on-disk), matching the commission-ledger pair carried in this row; the two fingerprint sources for this file—the letters-family self-report of the cited pair and the second copy's registered measurement—are registered as coexisting, and their normalization remains pending the PI's ruling) | 26,637 | BA4D07BD7000 |
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
| `results/_archive_2026_09_20/fiction_that_feeds_back.pdf` (second work, 23 pp., writing-day freeze; the second work is submitted and, as of 2026-09-27, on hold; a revised edition (R4) is ready for resubmission as of 2026-09-27 and the digest will change when it is archived) | 356,123 | 2D9EDC8C7303 |
| `查理_FTFB_R4更新交付_2026-09-27/fiction_that_feeds_back.tex` (second work, revised edition R4—the ready-for-resubmission text of the entry above; v0.2 row, measured 2026-09-27 at the workspace delivery face; repository-archival anchor pending: the revision has not been archived in the repository, so no repository anchor is stated, and the arXiv resubmission and the resulting digest refresh are pending events) | 101,928 | 4F8C42319603 |
| `戴夫_FTFB_R4编译交付_2026-09-27/fiction_that_feeds_back.pdf` (second work, revised edition R4, typeset twin of the entry above, 25 pp.; v0.2 row, measured 2026-09-27 at the workspace delivery face; repository-archival anchor pending, as above) | 411,782 | 0B0D9495508F |

### Letters family ([L], per commission ledger values)

| Path | Bytes | SHA-12 |
|---|---|---|
| [L] `letters/_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md` | 36,945 | 512C73D45087 |
| [L] `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 68,449 | 44D9A1972A13 |
| [L] `letters/_v4_commission_paper_final_glm_2026_09_24_v4.md` (v4 commission letter, source of the Section 15.2 ruling quote; self-reported 31,167 B, measured difference of +364 B pending PI ruling) | 31,531 | D5337702CEC9 |

### Recorded anchors ([R])

| Item | Bytes | SHA-12 |
|---|---|---|
| [R] Task B v1 preregistration | — | 696af9121d9f |
| [R] Task B v1 verdict | — | D279EBDE5E84 |
| [R] Task B v1 dataset (decision-trace archive) | — | 139DBFFD8CF9 |
| [R] L4 verdict (literal transfer via errata v19 §22.7 E-34.2; no independent file) | — | 74B5B37F7EEA |

### Version-pending items (each pending PI final ruling)

v19_fullrank / v20_baselines / v20_cot_quiz / v20_photonics / v20_quiz_eval

v0.4 note (2026-09-28): the item v20_baselines carries an externally reported deprecation declaration (errata-chain entry E-40.2, cited literally, single-source: recorded in the PI-side errata chain v22, which is not on-repository at this round, per the R4-evidence table below; the entry declares three files deprecated with no supplemental upload to follow and their dependent conclusion citations downgraded to not adjudicable, and v20_baselines is the one of the three carried in this list); the declaration is registered as reported, this draft chooses no version, and the item's pending status (PI final ruling) is unchanged.

### Merged-draft input anchors (added at merge and at the v0.2 revision round; measured 2026-09-27 at the workspace delivery face)

| Path | Bytes | SHA-12 |
|---|---|---|
| `dave-survey2-arxiv-20260915/keep_the_books_arxiv_2026_09_16_v9/keep_the_books_survey.tex` (unpublished survey source, Part I's origin; internal provenance anchor, never to be submitted; the complete survey package carries five files with fingerprints as recorded in the input-asset verification) | 102,686 | 02acb6d563eb |
| `_v4_paper_final_2026_09_26_v1.1.md` (V4-line source, Part II's origin; the v1.1 paper is merged into this third work and occupies no separate public slot) | 54,367 | 38bc2cf38d10 |
| `_v4_paper_final_2026_09_26_v1.1.tex` (V4-line source, typeset twin of the above) | 58,828 | 58bd5f5bef3a |
| `鲍勃_v1.1新增数字补测复核_2026-09-27.md` (independent re-verification of the V4-line source's v1.0→v1.1 added numbers, delivered 2026-09-27; the E-37 family's evidence file: its re-measurements supply E-37.1 (the five-read upper bound 0.5916, written at Sections 14.2 and Appendix B) and E-37.2 (the 62 measured calls, written at Section 13.3); the report is the drafted carrier for the next errata append round (v20), which has not yet run; v0.2 row) | 15,269 | 91E10F763316 |

### R4 re-adjudication evidence (added at the v0.4 registration round; on-repository rows measured 2026-09-28)

The two on-repository rows are this round's independent measurements; the three letters-family rows are fingerprint transfers—one carried as recorded in on-repository texts, two self-reported by letters-family documents—none of the three recomputable on-disk, their originals being on the PI's local face.

| Item | Bytes | SHA-12 |
|---|---|---|
| `results/_v3_supplement_verdict_2026_09_23.md` (V3-phase supplement verdict, the five-clue construction-degradation adjudication that is the primary carrier of the R4 re-adjudication; v0.4 row) | 15,247 | B70211BFA83E |
| `results/_v3_construct_degradation_diag_2026_09_23.json` (companion diagnostic JSON of the supplement verdict; v0.4 row) | 11,609 | C8D539A58D29 |
| [R] `letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23.md` (third-party re-review reply letter, the carrier of the third-party annotations cited by the supplement verdict; letters family, original not on-repository; fingerprint carried as recorded in on-repository texts—the 3-direction achievements inventory and the errata chain v19—not re-measured; v0.4 row) | 28,207 | 9BB22099DB3B |
| letters-family calibration note of 2026-09-27 (the formal record of the R4 re-adjudication; self-declared internal-reference, carried by fingerprint transfer only, per its own external-face rule of SHA-12-plus-bytes disclosure; original on the PI's local face, not on-repository, self-reported fingerprint, not recomputable on-disk; the note's filename is registered in the program's working chain and is not carried here; v0.4 row) | 21,869 | A5C33BD45D78 |
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`, PI-side extension v22 (the carrier of the E-40.1/E-40.2 citations of this round; the on-repository file at this path remains v19 (239,387 B, `849D76BE3A06`, E-1 through E-36, per the Governance table); the v22 extension is held on the PI's local face, its value self-reported via the letters family, single-source, not recomputable on-disk; v0.4 row) | 292,215 | 083087218A8D |

---

# Appendix B: Kill-Line Tables (Literal Carries)

This appendix restates the two decision tables exactly as carried from the verdict documents, for one-stop recomputation.

**Task B v2.2 (formal verdict).** Four kill-lines, all hit: (a) mean similarity 0.0909 against a 0.80 line; (b1) critique coverage 0.6842 against 1.00; (b2) blind-obedience rate 0.3333 against 0.10; (c) bootstrap CI [0.0, 0.2045] against a 0.50 lower bound. Root-cause classes: composite, β, composite, β. Composite qualification: partial true falsification plus partial construction doubt. Held-out items: main 22, alternative 17 (alternative CI [0.0294, 0.3382]). Formal-validity elements: 72-event accounting, 8-item D1 absence declaration, composite qualification, verifier signoff.

**N-26 (true-audit verdict, 2026-09-26).** K-N26-1: five-teacher mean accuracy 0.5617, line ≥ 0.70, NOT TRIGGERED (kimi 0.7512 the only teacher at or above the line; GLM_1 0.3955, GLM_2 0.6364, coze 0.5344, minimax 0.4909 below it). K-N26-2: pooled AUC 0.5663, line < 0.75 for true falsification, TRIGGERED, robust across all five read variants (range 0.4459 to 0.5916, all below 0.75; errata-chain annotation E-37.1, drafted for the next append round: the source verdict file's summary line records 0.5844 as the range's upper bound, omitting the drop_glm2 read; the independent re-measurement of 2026-09-27 gives 0.5916 as the five-read upper bound, which is written here; all five reads remain below 0.75, so the robustness finding is unchanged; the frozen verdict file itself is unmodified) and under five-fold CV (0.5271, 0.5266, 0.6318, 0.5740, 0.5719, all below 0.75). K-N26-3: three of five teachers below 0.60 (GLM_1 0.3955, coze 0.5344, minimax 0.4909), threshold at least four, NOT TRIGGERED. K-N26-N1: pass = True (non-degeneracy). K-N26-N2: pass = True (routing and empty-rate compliance; per-teacher empty rates 0.021–0.075 against a 0.50 threshold). Direction: same-direction deepening of the L4 verdict, not a reversal.

---

# Appendix C: Merge Provenance and Interpretation Registry

This appendix registers what the merged draft is made of, how its pointers were remapped, and which interpretation calls were made at which status. It exists so that a reader who wants to know whether a given sentence is survey material, V4-chain material, or merge-composed material can find out.

### C.0 The v0.2 revision round (registered)

The v0.2 round of 2026-09-27 applies the advisory pre-delivery precheck of the assembled v0.1 (a conformity review recorded in the program's working chain) and one external status fact, with every change item-registered in the working chain's revision record: the E-37 re-verification evidence file is anchored in Appendix A, with pointer fixes at the two inline annotations (Sections 13.3 and 14.2) and the conventions paragraph; the survey's novelty-search freshness clause is restated with its query families and its dates (Section 22.4); the E-37 family is explicitly registered as the exception channel to the frozen-literal carry rule (R3 below); the release-execution sentence's anchors are split between the public release history and the receipt's own wording (Section 22.3, R6 below); the signoff file's second on-disk copy is registered as pending the PI's ruling (Appendix A); the tier-letter legend's matrix pointer is corrected to Table 5 (Section 3.2); the T1.5r2 call-count relation is stated once (Section 13.3); and the second work's revised-edition-ready-for-resubmission fact is recorded without prediction (Section 1.2, Appendix A, and R5 below, with the refresh slots registered as pending). Precheck items that required verification only—the letters family's version discipline (no deprecated upload-executor row exists in the carried table), the dual-caliber self-overlap records, and the 36-entry chain count against the drafted E-37—were verified in place and required no text change. No verdict, no frozen number, and no literal carry of the F-family discipline is altered by this round.

### C.0.1 The v0.3 micro-revision round (registered)

The v0.3 round of 2026-09-27 applies the registered non-blocking items of a three-way advisory review of the v0.2 draft (the citation-and-literature line, the architecture-and-theory line, and the numbers-and-red-lines line, each recorded in the program's working chain and all three returning pass verdicts), with every change item-registered in the working chain's revision record: the References entry-format note's third merge point is corrected from a numbering typo to [41] (the survey-side entry for arXiv:2404.00699, now also stated in the C.2 citation-token mapping); the Section 17.2 summary sentence's ⑤-column block count is brought into line with the enumerations of Sections 17.1 and 17.3; the Section 17.3 row-numbering sentence is brought into line with Table 5's six physical rows (the first-work case study remains cross-referenced only, its full matrix row standing in Section 18.1); the Section 20.3 plan sentence no longer carries an internal plan name; and the Section 22.2 confidentiality sentence no longer states the confidential material's function domain. One registry ruling is added at this round: a reference-merge input proposed one additional external entry for the literature-protocol zone (an automated-survey-system preprint, arXiv:2608.18034, per that input's own record); the entry is not adopted and is registered here as considered-and-not-adopted, on the recorded grounds that the citation base is closed at the 61 survey-source entries plus the 3 V4-line-source entries with no new citation added by this draft (References note; Section 22.4), that this draft conducted no searches beyond the base's recorded passes, and that the V4-line source's self-contained baseline adds no external-citation requirement. No verdict, no frozen number, and no literal carry of the F-family discipline is altered by this round, and the v0.2 round's registration above stands unchanged.

### C.0.2 The v0.4 registration round (registered)

The v0.4 round of 2026-09-28 is a registration-layer round: the main text is unchanged (the only body touches are the two round-history sentences of Section 21, updated under the same truth-maintenance rule the v0.3 round applied; the front-matter version line carries the round identity), and every substantive change is registered in Appendix A and this appendix. Registered items: (i) the R4 registry entry below is upgraded from its pending-proof placeholder to registered, the formal record having been issued, with its primary evidence carriers on-repository (the R4-evidence table of Appendix A: the V3-phase supplement verdict and its companion diagnostic JSON, measured this round; a third-party re-review reply letter carried as a recorded anchor; and a letters-family calibration note carried by fingerprint transfer, self-reported, per the confidential-source discipline); (ii) the version-pending item v20_baselines carries an externally reported deprecation declaration (errata-chain entry E-40.2, cited literally, single-source, the PI-side errata chain v22 not being on-repository), with no version chosen and the pending status unchanged; (iii) the signoff row of Appendix A registers, per the E-37 exception-channel precedent, the two fingerprint sources (the letters-family self-report of the cited pair and the second copy's registered measurement), their normalization remaining pending the PI—this is a registration-layer provenance note, not a new member of the E-37 channel and not an exception to the frozen-literal carry rule; (iv) the errata-chain citations of this round (E-40.1, E-40.2) are single-source and modify nothing: the main text's frozen-at-v19 carry stands (the on-repository chain file remains v19, E-1 through E-36, per the Governance table), and the PI-side v22 extension is registered as reported. A self-check of this round against the mandatory reporting calibers carried in the letters family was performed item by item; no non-compliant main-text item was found and no adjustment was required by that check; the item-by-item outcome is registered in the program's working chain (this round's revision record). Round discipline: no verdict, no frozen number, and no literal carry is altered; the only open item closed is the R4 placeholder itself, its triggering event (the formal record's issuance, with carriers present) having occurred and being registered; the 8-gram self-overlap measurement and the typesetting round remain deferred as before, and the v0.2 and v0.3 registrations above stand unchanged.

### C.1 Per-section provenance and incorporation ratios

| Section | Content | Source and handling |
|---|---|---|
| 1 (front matter, Introduction) | rewritten | new composition over both lines; both lines' framing absorbed |
| 2–8 (Part I, coordinate system) | merged in full | survey source §§2–8, full incorporation, tokens carried at survey numbering pre-assembly |
| 9–16 (Part II, verdict chain) | migrated with frozen numbers | V4-line source §§2–9 → §§9–16; all verdict numbers and wording frozen; two E-37 corrections annotated inline (§13.3, §14.2) |
| 17 | new composition | the six-block mapping (Table 4) and the merged matrix (Table 5) composed per the architecture blueprint; the matrix's five external rows carried from the survey's Table 3 |
| 18.1 | merged in full | survey source §9.3, full incorporation; matrix row 6 carried; self-citation double-blind fork applied |
| 18.2 | new composition | register-parity statement only; no numbers |
| 19 | merged in full plus additions | survey source §9.2 lessons (a)–(d) carried; V4-anchor paragraphs composed; lesson (c) V4 anchor declared absent |
| 20.1–20.2 | merged in full | survey source §10, full incorporation; OP8's instance clause updated to name both case studies |
| 20.3 | new composition | plan-level, exploratory tier; no results |
| 21 | migrated plus two additions | V4-line source §11 items (1)–(7) carried; items (8)–(9) added for the merge |
| 22.1–22.3 | migrated plus one addition | V4-line source §10.1–10.3 carried; execution-state sentence added (2026-09-27 face) |
| 22.4–22.5 | condensed / composed | survey source §1.3 and Availability section condensed; self-overlap disclosure composed with the 8-gram placeholder |
| 23 | migrated plus merge disclosure | V4-line source §12 as body; survey-source AI-use disclosure merged by restatement |
| 24 | rewritten | new composition; the hinge sentence of Section 17.1 is the conclusion's spine |
| References | unified | 64 entries: survey 61 + V4-line 3, single first-appearance sequence; three same-work merge points resolved (first-work entry; arXiv:2510.15746; arXiv:2404.00699) |
| Appendix A | migrated plus additions | V4-line source Appendix A carried; merged-draft input anchors added |
| Appendix B | migrated with one correction | V4-line source Appendix B carried; E-37.1 range correction applied at the K-N26-2 row with the drafted annotation |
| Appendix C | new composition | this registry |

### C.2 Pointer remapping, registered verbatim

- V4-line source internal pointers: §2→§9, §3→§10, §4→§11, §5→§12, §6→§13, §7→§14, §8→§15, §9→§16, §10→§22, §10.1→§22.1, §10.2→§22.2, §10.3→§22.3, §11→§21, §12→§23, §13→§24; the v1.1 §3.5 zero-key reference inside §22.2 remapped to Section 10; "its Section 3.4, Plan A" inside §13.3 is the source verdict file's internal section number and is not remapped.
- Survey-source internal pointers: §1.3→§22.4 (protocol condensed), §1.2→§1.2, §3.1/§3.2→§3.1/§3.2, §4–§8→§4–§8 (Part I numbers unchanged, including the X.3 matrix-row pointers), §9.1→§17.3, §9.2→§19, §9.3→§18.1, §10.1→§20.1, §10.2→§20.2, §7.2/§8.2/§5.3/§8.1→same.
- Citation tokens: Part I carried the survey's 1–61 numbering in the part file; the assembly round renumbered document-wide to the unified first-appearance sequence (survey 1–17 unchanged; Nosek, Popper, and Yang inserted at their first appearances as [18], [19], [20]; survey 18–61 shifted by +3; the survey pool's internal same-work merge (arXiv:2404.00699, the survey sequence's key 38) resolved to the survey-side entry [41]; Part III was drafted directly in the unified numbering).

### C.3 Interpretation registry

- **R1 (program work sequence)** — registered: first work (the scattering-layer paper) → V3-phase terminal report (a delivered companion report, referenced third-person and not merged; its experiment content is not part of this draft) → second work (FTFB, submitted and on hold) → third work (this merged draft). The V4-line source is merged into the third work and occupies no separate public slot.
- **R2 (the survey source's submission status)** — registered as closed: the survey source was never submitted and will not be submitted; it is permanently an internal provenance anchor; this merged draft is its only public carrier. No public pointer to the survey source as an independent submission exists or is created by this draft.
- **R3 (frozen-number and verdict-literal discipline)** — registered: all Part II numbers and verdict wording are carried frozen from the V4-line source; the two measured-value corrections of the E-37 family (E-37.1: five-read range upper bound 0.5916; E-37.2: 62 measured calls) are written with drafted errata-chain annotations at Sections 13.3, 14.2, and Appendix B; the errata chain remains frozen at v19 (E-1 through E-36); the verdict files themselves are unmodified. The E-37 family is hereby the explicitly registered exception channel to the frozen-literal carry rule (registered at v0.2): a measured-value correction enters this draft only as a drafted errata-chain annotation whose evidence file is anchored in Appendix A, the frozen verdict files are never rewritten, and the correction propagates to the Appendix B literal tables under the same annotation; the channel's scope is the two registered members (E-37.1 and E-37.2), no other exception to the carry rule exists, and none is created by this draft.
- **R4 (externally reported re-adjudication of a prior verdict)** — registered at v0.4 (2026-09-28): the formal record has been issued, and its content is registered here as reported, in the registration layer only—the main text carries none of the re-adjudicated readings (verified by search at this round), and no Part II number or verdict wording changes. As reported, the record—a construction-degradation reading of a V3-phase supplementary verdict, with third-party annotations—flips five readings of the P-A family (the 145.8× multiple reading, falsely established via its derived sources' two constant-degradation diagnoses; the 0/22 ESS-coincidence reading, falsely established, its ESS fields being constants across all 22 items, the 0/22 being a construction product; the 3/22 PG reading, re-adjudicated on 2026-09-27 to a full-PG rework construction, 22/22 PG per KT_B1_REWORK, with the 3/22 side retained as a construction-caliber difference note—errata-chain entry E-40.1, cited literally, single-source, the PI-side chain v22 not being on-repository; the source report's reference table at its lines 143–147, voided as evidence for field-by-field mismatch with the frozen JSON values and mutual exclusivity with the same report's own mean; and the family's interim-PASS (total) summary, registered as overstated, its three supporting readings being two constant degradations and one conflict, unable to support a direction-level PASS); registers the same-family illusion series as downgraded (nine readings in the record's own count: five whose recorded falsifications are reclassified as false, three whose recorded establishments are reclassified as false—the two P-A members being named above—and one conservation reading classified as a structural identity); and leaves two state-layer items registered as not adjudicable (a four-path aggregate kill reading, its source report carrying internally coexisting computation-state records and a coexisting verdict-placeholder note and filled verdicts, and a comprehensive-kill reading, its source report carrying coexisting 51/60 and 52/60 totals). The P-C, P-E, and P-F families are reported maintained, not flipped (P-C as a citable true falsification; P-E and P-F as maintained with their recorded qualifications). The re-adjudicated items are registered as disposed, not hanging, per the record's own disposal panorama: the P-A family's disposition is registration-only (zero fixes, the V3 report unmodified, PI ruling reserved, per the supplement verdict's own disposition clause); the PG reading is closed by the PI's re-adjudication (E-40.1); the deprecated files are declared with no supplemental upload to follow (E-40.2); and the T1-type illusion of the construction-failure family was disposed by the T-series corrections, which this draft already carries at Section 13.3. Evidence carriers, per the R4-evidence table of Appendix A: the V3-phase supplement verdict and its companion diagnostic JSON (on-repository, measured 2026-09-28), the third-party re-review reply letter (recorded anchor), the letters-family calibration note (fingerprint transfer, self-reported), and the two single-source errata-chain citations (E-40.1, E-40.2). The registration follows the R1–R3 precedent of concise, registered facts: the source documents are not transcribed, none of them enters the References, and the confidential-source discipline of C.4 is unaffected—the calibration note and the weekly-report family remain outside the citation surface, carried by fingerprint only.
- **R5 (the second work's citation form)** — registered: cited at the writing-day frozen digest (356,123 B, 2D9EDC8C7303) with the status "submitted, on hold" recorded once (Section 1.2 and Appendix A); a revised edition of the second work (the second work's revision R4, not this registry's entry R4) was completed on 2026-09-27 and is ready for resubmission, with its text and typeset twin anchored in Appendix A at the workspace delivery face and its repository-archival anchor pending; the digest-refresh slots are registered as pending and are not filled with predicted values: the refreshed archive digest (bytes, SHA-12, page count, to be measured at archival), the arXiv resubmission date and its outcome (including any change in hold status, per the arXiv record), and the formal citation upgrade (upon publication). Each slot will be entered upon its event per the linkage checklist registered in the program's working chain, with the historical values (356,123 B / 2D9EDC8C7303 / 23 pp.) retained as a superseded-value note at that time; this draft predicts no outcome.
- **R6 (the release execution sentence)** — registered: the execution-state sentence of Section 22.3 states the 2026-09-27 public-release face without remote identifiers, per this paper's double-blind citation rule; the circled-face numbers of the V4-line source's Section 22.3 remain at their 2026-09-26 freeze; the two faces are recorded side by side and are not merged; the receipt's internal arithmetic inconsistencies are carried per the receipt's own wording, registered as pending verification, and are not corrected by this draft. At v0.2 the sentence's counts were re-measured against the public release history (the 2026-09-26 release batch: 415 files changed across 42 commits, matching the sentence), and the sentence now states its anchor split itself: the item and commit counts are recomputable from the public history, while the fingerprint-consistency result and the receipt's internal arithmetic remain carried per the receipt's own wording.
- **R7 (the mapping of Table 4)** — registered at consistency tier: the six-block-to-five-line mapping is a reading of Part II's records composed at drafting and is subject to the reviewers' check per the architecture blueprint; it adds no measurement.
- **R8 (self-overlap measurement)** — placeholder, open: the 8-gram self-overlap measurement of the assembled draft against the first and second works is deferred to the typesetting round; the disclosure category is renamed "merged-in coordinate-system material" (Section 22.5); the survey's single-work precedents are 4.62% (10-gram, case-study section), 0.21% (10-gram, remainder), and 0.91% (8-gram program record).

### C.4 Confidential-source discipline (verified at assembly)

No citation of, quotation from, or pointer to the program's confidential weekly reporting appears anywhere in this paper: the References contain none of its content, Appendix A registers none of its files, and every number in this paper traces to on-disk public-chain artifacts only. The plan-level description of Section 20.3 carries no numbers. The name-disambiguation discipline (the K-N26-* and K-N11-* families; the program-internal verdict ladder versus the survey's five lines) is enforced at Sections 17.2, 14.1, and 16.1. v0.4 note (2026-09-28): the R4 registration (C.3) and the R4-evidence table of Appendix A carry, in the registration layer, letters-family fingerprint transfers—one recorded in on-repository texts and two self-reported—as provenance disclosures (recorded or self-reported, as annotated per row), not as measurements of this draft; the weekly-report family itself, and the calibration note beyond its fingerprint, remain uncited, unquoted, and unregistered; the main text's numbers continue to trace to on-disk public-chain artifacts only, and the main text carries none of the re-adjudicated readings (verified by search at this round).
