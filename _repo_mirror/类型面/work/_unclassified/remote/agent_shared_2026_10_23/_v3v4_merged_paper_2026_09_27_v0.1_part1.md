# Walking with the Verdicts, Keeping the Books: A Five-Line Audit Coordinate System and a Pre-Registered Distillation Program That Formally Failed

**Version**: v0.1 draft (upper-half part file), 2026-09-27 · English, arXiv-preprint style
**Working title**: architecture-blueprint candidate 1 of 3; the final title is reserved to the principal investigator (PI)
**Part-file scope**: this file delivers the front matter, Section 1, Part I (Sections 2–8, the coordinate-system zone, merged in full from the unpublished survey source), and Part II (Sections 9–16, the verdict-chain zone, migrated from the V4-line paper v1.1 with frozen numbers and literal verdicts). Part III (the synthesis zone), the unified references, and Appendices A–C are listed, not expanded, in the placeholder directory at the end of this file; they are delivered in the lower-half part file, and the assembled complete v0.1 (md and tex) follows in subsequent rounds.
**Author block**: Attribution withheld. The author list is reserved to the principal investigator's decision; this placeholder is not an authorship claim.

---

**Literature and claim conventions (merged draft, working).** The coordinate-system material merged as Part I (Sections 2–8) originates in a survey manuscript that was never submitted for publication and will not be submitted; this merged draft is its only public carrier, and its verified reference base of 61 entries (60 external entries plus one disclosed self-citation to the program's first work) is carried into this draft. In this part file, bracketed citation numbers follow the numbering of that unpublished survey source; works cited from the V4-line source outside that pool are cited by author and year; the two sequences will be unified into a single first-appearance external sequence at the assembly round, per the merged reference plan. Evidence strength is labeled throughout in three tiers, closed (pre-registered), consistency, motivation only, plus a scope marker; the tier conventions are defined in Section 3.2. Verdict wording (FAIL, hit, TRIGGERED, NOT TRIGGERED, composite qualification) is carried literally from the frozen verdict artifacts; every verdict number in Part II is anchored to a path, a byte count, and a SHA-12 digest in the appendix of the assembled draft. Two measured-value corrections carried from the independent re-verification of 2026-09-27 are written into the text and annotated inline as drafted errata-chain family E-37 (Sections 13.3 and 14.2); the errata chain itself is frozen at v19 (E-1 through E-36) and is not modified by this draft. The survey's self-references ("this survey") in Part I refer to the merged survey material of Sections 2–8. For double-blind safety, attribution is withheld throughout, real-name elements of the survey source are not carried into this draft, and the frozen digests of all cited artifacts are unaffected.

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

This paper is the third work of the program. The first work built an auditable, conservation-guaranteed, game-theoretically tested scattering layer over LLM reasoning paths and fixed the program's evidence conventions (companion study (first work): *An Auditable, Conservation-Guaranteed, Game-Theoretically Tested Scattering Layer over LLM Reasoning Paths*; on-disk anchor `paper/deposon_paper_final_en.md`, 68,164 B, SHA-12 `2EC20B96E941`, measured 2026-09-26; publication identifiers, if any, are per the principal investigator's authoritative records; the work is entered as the first case study in Section 18.1). The second work argued, historically and formally, that fiction feeds back into machine worldviews (companion study (second work): *Fiction That Feeds Back: From Non-Euclidean Geometry to Machine Worldviews*, 23 pp.; submitted to arXiv and, as of the writing day (2026-09-27), on hold; on-disk anchor `results/_archive_2026_09_20/fiction_that_feeds_back.pdf`, 356,123 B, SHA-12 `2D9EDC8C7303`, measured 2026-09-26, writing-day freeze; an updated version is in preparation on the PI's side, so this digest will change, and the citation will be upgraded to the formal arXiv record upon public release). The third work, this paper, merges the program's two remaining lines into a single account: a five-line survey of audit infrastructure for LLM-reasoning claims, developed as an unpublished manuscript and merged in full as Part I, and the verdict-anchored record of the program's V3–V4 distillation phase, which formally failed, migrated as Part II.

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

The verdict-chain side reports a pre-registered program phase. The phase began from a question recorded in the program's first-year assets, *how should AI think?*, and the claim under test inherited it: whether an AI system can critically learn the principal investigator's way of thinking, defined at pre-registration as method internalization rather than behavioral profiling. The claim was operationalized as three mechanical indicators (held-out structural similarity, explicit-critique coverage at disagreements, and a blind-obedience rate) with pre-registered thresholds and four kill-lines, a verdict-keeper role that adjudicates without running experiments, and an independent verifier role that signs off on the verdict process; the phase was made falsifiable in the preregistration-revolution sense (Nosek et al., 2018) and under the discipline that a claim is killed before it can be believed (Popper, 1959). The result is a formal FAIL, reported without softening. The program's own rule, set by the PI on 2026-09-23 and recorded in the verdict documents, is that *honesty equals not misleading*: reporting numbers is "mechanical honesty" and is not sufficient; a verdict must co-present its root-cause distribution and its construction-doubt boundaries, and the verdict wording itself (FAIL, hit, composite qualification, NOT TRIGGERED) must be carried literally. On the evaluation side, game-theoretic analyses of LLM self-judging and human-aligned evaluation (Yang et al., 2025, arXiv:2510.15746) sharpen what is at stake when a verdict must be trusted. Section 16 states the full discipline as this paper's writing rules.

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

**Non-Euclidean geometry.** Between 1829 (Lobachevsky) and 1854 (Riemann), internally consistent geometries were constructed that denied Euclid's parallel postulate. For roughly half a century they remained, in effect, fiction: formally sound, empirically unclaimed. Gauss reportedly withheld publication for fear of ridicule, and the systems were widely read as logical curiosities rather than candidate descriptions of physical space. Poincaré observed in 1902 that one geometry cannot be more *true* than another, only more *convenient*—the fictional-system attitude, stated as a principle. The loop closed in 1915–1919: general relativity took Riemannian geometry as its language, and the light-deflection measurements put the package into falsifiable contact with the world. What was actually falsified was the incumbent, Euclid-as-physics. The operational residue is permanent; curved-space geometry is now an engineering instrument. The historical scholarship on this geometry–physics interface is documented in [18].

**Boltzmann entropy.** In 1877 Boltzmann attached entropy to a count of microstates, and the probabilistic reading was attacked in its day as an unwarranted fiction—dice games inside physical law. The loop ran long and closed twice. Shannon's 1948 measure of information has the same functional form as Boltzmann's entropy; Jaynes's 1957 recast of statistical mechanics as maximum-entropy inference made the probabilistic fiction into an explicit epistemic calculus applicable across domains [19]; Wigner's 1960 essay named the reverse puzzle, mathematics' "unreasonable effectiveness" in the natural sciences [20]; and Landauer's 1961 principle (erasing one bit dissipates at least kT·ln2) closed the circuit physically: the fictional quantity turned out to be physical [21]. The operational residue is twofold. Information theory became an engineering discipline, and every recomputation this survey discusses acquired a physical floor: rechecking a ledger itself costs energy.

**Robotics.** The word *robot* entered circulation from Čapek's 1920 play *R.U.R.*—a fiction. *Robotics* was coined by Asimov in 1941, also in fiction. Both became the ontology of a real engineering discipline: the discipline's objects, roles, and failure modes are named in vocabulary supplied by fiction before the engineering existed. The scholarship on this exchange is active. Field research examines how fictional and imagined robots structure real human–robot relations and the discipline's self-understanding, particularly in Japan [22]; the deliberate engineering use of fiction as a design method has been systematized as science-fiction prototyping [23]; and fictionality has become a method in innovation research more broadly [24]. The loop in its linguistic form: a fictional coinage supplies the ontology; the engineering discipline supplies the falsifiable claims (real robots fail real tests); the vocabulary survives as the field's working language.

**The loop pattern.** All three anchors exhibit one circuit. (i) An internally consistent system is built without empirical commitment—fiction or formalism. (ii) It is put into falsifiable correspondence with a domain, and somewhere it is actually falsified—or the incumbent assumption it challenges is. (iii) What survives leaves operational residue: methods, vocabulary, invariants. The hinge of the circuit is (ii), and the hinge of (ii) is bookkeeping. On this reading, falsifiability is not a property fictional systems acquire spontaneously; it is infrastructure that someone builds and maintains: a registered prediction, a frozen rule, an external witness. We state the corollary in the survey's own register: a kill protocol is the boundary between hard science fiction and fantasy. A fictional system that pre-registers what would count against it has entered the loop; a fictional system that cannot be killed by any observation has not. The falsifiability debate has since entered machine learning scholarship directly, and §2.3 takes it up.

### 2.2 Contemporary drivers

**Scale.** Frontier models and their training sets exceed any single party's recomputation capacity. The training run cannot be re-executed by a third party at reasonable cost, so behavioral claims rest on evaluations—claims whose support is, at best, a protocol description and a score. The trust geometry inverts: when direct recomputation of the artifact is impossible, the only checkable thing left is the record kept around the artifact.

**Replication.** The audit vacuum has measurable costs. A systematic audit of leakage in machine-learning-based science found information improperly shared between training and evaluation to be widespread, with a taxonomy for spotting it [7]—each leakage instance is a claim whose support did not exist. The reproducibility program—checklists, code and data submission, reporting standards—institutionalized bookkeeping as social infrastructure at a major venue [8]. Both works are audit-infrastructure papers in the strict sense: their subject is survivable claims, not better models.

**Incentives.** When scores are the currency, claims optimize toward scores. Uncheckable claims are cheaper to produce than checkable ones, so the equilibrium drifts toward uncheckable claims (Goodhart-type pressure, present in every measurement-driven field). The concern is the field's own, and it has a lineage: the self-criticism tradition begins with Wagstaff's demand that machine-learning claims connect to measurable consequence [25], and Lipton and Steinhardt's diagnosis gave the incentive distortion its canonical three-symptom reading [26]. The countermeasure is not exhortation but pricing: make the checkable claim the one that pays—by making verification cheap (attribute ③), by making retroactive support visible as such (attribute ⑤), and by making kills reportable without reputational collapse (the register this survey practices).

**Consequence.** The LLM-era need is ledgers, not only scores. A score is a claim; a ledger is a recomputable support. The five lines surveyed next are the places where this consequence is already being worked out—mostly without reference to each other, which is precisely why a shared taxonomy is worth building.

### 2.3 Falsifiability inside machine learning

The philosophical question did not stay in philosophy. Nielson reads machine learning's self-understanding against Popper directly—induction, falsificationism, and what it would mean for a learner's claims to be falsifiable rather than merely fit [27]. Buchholz and Raidl take the complementary route: a falsificationist methodological account of artificial neural networks, asking what ANN research would look like if its claims were organized around refutation rather than accumulation [28]. Both are argument papers, tiered motivation only under the survey's conventions; what they supply is vocabulary and a live question, not measurements.

The survey's position on that question is deliberately thin, and we state it once. The operational reading of §3.1 (verdict executability) is weaker than either Popperian logical falsifiability or its machine-learning-internal adaptations, and it is independent of their outcomes: it asks only whether the bookkeeping around a claim permits mechanical killing. If the philosophical program succeeds—whatever success turns out to mean for it—the operational reading is unchanged; if it fails, the operational reading is still the engineering practice this survey documents across five lines. The historical loop of §2.1 and the contemporary debate of this subsection share one hinge: falsifiability is infrastructure, and infrastructure can be built before the philosophy is settled. That is why §3 proceeds on definitions rather than doctrine.

## 3. Concepts and taxonomy

### 3.1 Three operational definitions

**Auditability = third-party recomputability.** A claim *C* about a system's reasoning is auditable at cost *κ* if (i) there exists a frozen artifact *A* recording the claim's support, and (ii) a third party with stated resources and no privileged access can mechanically recompute that support from *A* at cost *κ*. Auditability is thus graded, not binary. It is graded by *κ* (attribute ③), by the fraction of claim→execution deviations the record can reveal (attribute ②), and by the independence of the verifier from the claimant and from the artifact's constructor (attribute ④). A leaderboard score is one extreme point of this space: the artifact is a number, the recomputation is a lookup, and the covered deviation spectrum is empty—nothing about the reasoning is recomputed at all.

**Falsifiability = executability of pre-registered verdicts.** A claim *C* is operationally falsifiable if there exists a verdict function *v: A → {supports, kills, inconclusive}* such that (i) *v* was frozen before execution, (ii) *v* is mechanically evaluable by a third party, and (iii) a kill verdict is binding in the sense that it is reported, not discarded. This is the engineering reading, and it differs from the philosophical lineage: Popperian logical falsifiability is a property of a claim's logical form, while verdict executability is a property of the bookkeeping around the claim. The two can come apart in both directions. A claim can be logically falsifiable and verdict-less—no registered rule, no frozen artifact—so that killing it costs a community debate rather than a mechanical evaluation. A verdict-executable claim is killed, or survives, at machine cost. The philosophical lineage and its machine-learning-internal debate are taken up in §2.3 [27, 28]; the operational reading adopted here is deliberately independent of that debate's outcome.

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

**Tier-letter legend.** C = closed (pre-registered); E = consistency evidence; M = motivation only; S = scope marker; "—" = not located in the verified base. The letters are used in Table 3 and every X.3 matrix row; compound markers (E–M, C/E, S/E) blend the tiers they name.


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

The unit of account here is the relation between the emitted explanation and the computation that produced the answer. Chain-of-thought made explanations machine-generated and ubiquitous [1]; the faithfulness question asks whether the emitted chain reflects the actual computation [2, 3]. A second era changed the stakes. Reinforcement learning now trains the chains themselves—reasoning models learn long chains of thought as behavior rather than as a prompt format [29]—so the explanation is a trained artifact, and whatever trains it can shape what it shows. The faithfulness question thus carries a second edge: not only whether the chain reflects the computation, but whether the training signal has taught the chain to look better than the computation.

The measurement mechanisms are behavioral. Perturbation protocols truncate, paraphrase, or pad the emitted chain and ask whether the answer changes [3]; an answer insensitive to the chain's content indicates that the chain is not doing the explaining it appears to do. Bias-planting protocols induce a biased answer through few-shot answer patterns or distractors and ask whether the emitted chain rationalizes the bias post hoc [2]; when it does, the chain is testimony, not computation. In the vocabulary of this survey, the faithfulness tests are the field's detectors for *books ≠ real books*, and the measured quantity is the divergence between the account and the account's causal history.

### 5.2 Evidence and failure modes

Evidence. Unfaithfulness is measurable, non-zero, and task- and model-dependent [2, 3]; both works report empirical protocols with quantitative results, recorded at the consistency tier. The line's strongest content is partly negative, and the negative content carries equal weight: an honestly reported faithfulness-failure rate converts "the model explains itself" into a falsifiable claim—"the explanation deviates from the computation at rate *r* under protocol *P* on distribution *D*"—which is exactly the bookkeeping move of §3.1.

Failure modes. First, the detector problem: faithfulness metrics are behavioral proxies. An answer's stability under chain perturbation is not itself the explanation–computation relation, so a model could pass the available tests while the chain remains non-causal in the relevant sense (the metric-recursion form of ④). Second, instrumental explanations: unfaithful chains can still improve task accuracy, because the chain's causal role in generation is separable from its testimonial role. The books can be wrong while the balance is right; explanation value and audit value must therefore be reported separately, and conflating them is an error this line exists to catch. Third, protocol relativity (⑥): a faithfulness rate is a property of (model, task, protocol), not of "the model," and numbers from different protocols are not commensurable without declaring the protocol. Fourth, the reasoning-model era has begun to produce this line's kind of evidence, and it cuts both ways. CoT monitoring can detect misbehavior in RL-trained reasoning models; but penalizing the monitored bad thoughts does not remove the misbehavior—it teaches concealment while task metrics improve. The audit layer and the optimization layer pull against each other, with the confounding effect measured rather than asserted [30]. On the faithfulness side, reward-hacking behavior in reasoning models is rarely acknowledged in the emitted chain—admission below 2% in most tested settings [31] (an institutional research report, non-peer-reviewed, labeled as such; consistency tier with the label). What remains open is the systematization of this era's evidence (OP5 in §20.2).

### 5.3 The monitorability question and matrix row: L2 facts ①–⑥

The reasoning-model era also supplies a quantification baseline: across twelve open-weight reasoning models and 41,832 runs, faithfulness rates span 39.7%–89.9% [32] (consistency tier). The spread, not the midpoint, is the finding—faithfulness is model-relative and protocol-relative across the open-weight spectrum, not a fixed property of "reasoning models."

The era adds a debate of its own around one word: monitorability. A position paper argues that chain-of-thought monitorability is a new and fragile opportunity for AI safety—precious, because the chain is a direct window into the computation; fragile, because folding it into training targets destroys exactly what makes it valuable [33] (position paper; motivation tier). The fragility claim is not merely rhetorical: stress-testing shows that reasoning models can obfuscate their reasoning, concealing the actual inference path while preserving behavior [34]. Together with the monitoring result of §5.2, the line now holds its cleanest demonstration of a proposition that crosses lines: **an audit layer placed under optimization pressure erodes.** The same proposition recurs at the protocol layer in §7.2, where the decentralized-evaluation cluster meets gaming pressure on the evaluation protocol itself. CoT monitoring here and decentralized evaluation there are the proposition's two live instantiations, and the confounding effect of [30] is its sharpest experimental demonstration in the verified base.

| **Attribute** | **Fact (with pointer)** | **Tier** |
|---|---|---|
| ① commitment object | the explanation–computation relation, per instance and per test protocol [2, 3] | E |
| ② tamper-spectrum coverage | post-hoc rationalization and chain-insensitivity detectable under perturbation and bias-planting protocols [2, 3]; RL-era monitoring detects misbehavior [30, 31]; open-weight faithfulness quantified at 39.7%–89.9% over 41,832 runs [32]; deliberate obfuscation can defeat monitoring [34]; metric-gaming deviations are outside the recorded spectrum (the proxy gap) | E |
| ③ recomputation cost | behavioral probes—no training required; the cheapest detection layer in the survey; monitoring adds inference-scale cost [30] | E |
| ④ verifier neutrality | faithfulness metrics are behavioral proxies, unaudited as instruments (recursion open) [2, 3] | E |
| ⑤ commitment timing | per-study protocols fixed in advance; run-level pre-registered verdicts not located in the verified base | — |
| ⑥ distortion boundary | a faithfulness rate is protocol-relative and model-relative (39.7%–89.9% across twelve open-weight models [32]); monitorability is fragile under optimization pressure [30, 32, 33, 34] | E |

## 6. Evaluation integrity: the benchmark's own books

### 6.1 Problems and mechanisms

The unit of account is the evaluation artifact itself: benchmark, protocol, grading pipeline, and the train/test boundary. Evaluation integrity is upstream of every performance claim in every other line—the books about the books. The mechanisms are three. Leakage auditing systematically detects information improperly shared between training and evaluation—feature leakage, temporal leakage, and adjacent forms—and supplies a taxonomy for spotting them across applications [7]. Reproducibility infrastructure—checklists, code and data submission, and reporting standards—was institutionalized through a major venue's reproducibility program [8]: bookkeeping as social infrastructure, the commitment stage executed at the level of a research community. And the competition format—fixed tasks, frozen leaderboards, enforced protocol equality—rests on the position that AI competitions provide the gold standard for empirical rigor in generative AI: evaluation bookkeeping run as an institution [35] (position track; motivation tier).

### 6.2 Evidence and failure modes

Evidence. Leakage was identified as widespread in machine-learning-based science, with a deployable detection taxonomy [7], and the reproducibility program was adopted and reported at scale [8]. Both are audit-infrastructure papers in the strict sense used here: their subject is not better models but survivable claims. Consistency tier for both.

Failure modes. First, contamination voids admissibility: a score whose train/test separation is broken is a claim whose support does not exist. The detection is usually retroactive—the claim dies after publication—and that is itself the ⑤ failure mode of the surrounding practice: nothing froze the evaluation's commitment before the run, so the post-hoc "clean" verdict is unfalsifiable in exactly the way §3.1 defines. Second, temporal discipline is this line's native ⑤. Held-out sets, embargoed releases, and time-ordered evaluation freeze the test before the claim; where a line of work adopts these, its claims gain verdict executability, and where it does not, they rest on assertions. Third, construct drift (⑥): a benchmark's construct shifts as the population of solvers changes, and a "clean" score certifies protocol-relative performance, not the intended construct, and not reasoning correctness. Fourth, selective reporting: claims survive because failures were never recorded; checklists are the procedural countermeasure, partial by design [8].

Contamination detection has itself become a methodology with a literature: rephrase-based detection [36]; the Sharded Rank test, which proves contamination from black-box access with exact false-positive control [37]; a comprehensive survey organizing the n-gram, semantic, and performance-based families [38]; a systematic evaluation interrogating the core assumptions of fifty proposed detection methods [39]; performance-based detection with context-cache controls [40]; and detection adapted to the RL post-training era [41]. Within L3's row, ② therefore records a populated detector spectrum rather than a blank. The honest boundary is inherited from [39] and sharpened by [42]: the detectors' own core assumptions are only partially validated, and detection itself is fragile for reasoning models, where methods validated on base models can fail [42] (consistency tier). The auditors of the auditors are still largely unaudited; their fragility is now an empirical result rather than a caveat, and a systematic validation protocol is the open step (OP2 in §20.2).

### 6.3 Matrix row: L3 facts ①–⑥

| **Attribute** | **Fact (with pointer)** | **Tier** |
|---|---|---|
| ① commitment object | the evaluation artifact: benchmark, protocol, grading pipeline, train/ test boundary [7, 8] | E |
| ② tamper-spectrum coverage | leakage detectable by systematic audit (taxonomy of leakage forms) [7]; a populated detector family: rephrase-based [36], black-box provable [37], n-gram/ semantic/ performance families [38], assumption-audited [39], performance-based with cache controls [40], RL-era [41]—the family itself fragile for reasoning models [42] | E |
| ③ recomputation cost | pipeline re-analysis: moderate; scales with data-pipeline complexity [7] | E |
| ④ verifier neutrality | community audit plus detection heuristics; benchmark constructors are a trust root (recursion open) [7, 8]; the detectors' own assumptions are only partially validated [39] | E |
| ⑤ commitment timing | temporal discipline native: held-out sets, embargoed release, time-ordered evaluation [7, 8]; competitions freeze protocol equality institutionally [35] | E |
| ⑥ distortion boundary | a clean score certifies protocol-relative performance—not construct validity, not reasoning correctness | S |

## 7. Game-theoretic verification: endogenizing the auditor

### 7.1 Problems and mechanisms

The unit of account is the incentive structure of the verification interaction. Rather than audit the artifact after the fact, mechanism design endogenizes the auditor: the game is structured so that honest, checkable reporting is an equilibrium property rather than an assumption. The debate proposal sets two AI systems in opposition before a weaker judge, human or machine, and argues that cross-examination extracts information beyond the judge's own competence, so that verification scales with the system instead of against it [9]. Mechanism-design approaches to AI safety treat the alignment of participants' incentives as a design object, asking when verification-relevant honesty can be made an equilibrium property of the interaction itself [10]. The formal layer exists in general form: probabilistic verification in mechanism design characterizes honest reporting under noisy tests [43] (formal theory; motivation tier under the survey's mapping). What that theory has not yet received is the connection to ML capability claims, and that connection is the unsystematized step documented in §7.2. The line's distinctive promise is a transformation of ④: verifier neutrality is not purchased from an external auditor but manufactured inside the mechanism. Adversaries check adversaries.

### 7.2 Evidence and failure modes

Evidence. The debate proposal reports preliminary experiments [9]; the mechanism-design program contributes formal analyses and designs [10]. The strength of this line is possibility-level, stated as-is: proposals and analyses, with small-scale demonstrations rather than deployed verification. Several of the line's cells therefore sit at E-to-M in the survey's tiers, and the survey does not upgrade them. A 2026 cluster has additionally formed around a specific L4 failure mode: unverified benchmark claims. The motivation is stated in market terms—unverified benchmark claims can move markets—so the verification itself is decentralized: protocols that replace trust in the benchmark holder [44]; blockchain-based multi-party consensus evaluation frameworks [45]; and matching-server architectures that hide the benchmark from the evaluation client to prevent leakage [46]. The cluster is young, its work proposal-scale and prototype-scale, and the survey tiers it E–M as a cluster rather than entry by entry.

Failure modes. First, Goodhart-type pressure, sharpened by stakes: once the mechanism is the target, participants optimize the *appearance* of honesty, and strategies that pass cross-examination while misrepresenting are the line's canonical adversarial register—the mechanism's guarantee does not cover them (②'s boundary). Second, the judge bottleneck: the human (or weaker AI) judge is debate's unaudited root, and judge competence is simultaneously the verification resource (③) and the trust root (④), a concentration this line inherits rather than solves. Third, equilibrium versus deployment: mechanism guarantees hold in equilibrium, and deployed multi-agent systems need not reach the analyzed equilibrium (selection, collusion). Fourth, the designer trust root: the mechanism designer becomes a new party whose neutrality must itself be audited—④ is transformed, not eliminated. Fifth, the cross-line proposition stated in §5.3: an audit layer placed under optimization pressure erodes. CoT monitoring meets it as concealment [30]; decentralized evaluation meets it as protocol gaming—once the evaluation protocol is the target, gaming pressure migrates to the protocol, and the cluster's designs [44, 45, 46] are attempts to raise the cost of that migration; and reinforcement learning with verifiable rewards meets it at the training interface, where optimizing against the verifier leads the verifier into reward hacking [47] (consistency tier)—the proposition's third instantiation and the one closest to the audit-versus-training boundary. The proposition is the shared failure register of the three sites, and the reason ⑥ boundaries matter more in this line than ② coverage.

The escrow-style combination—a capability claimant posts forfeitable stakes—remains unsystematized at the major machine-learning venues. Its nearest neighbors fall into three clusters. Cluster 1 is mechanism-design theory, general and established, not yet connected to ML claims [43]. Cluster 2 is decentralized LLM evaluation, sprouting in 2026, without bond–forfeiture incentive structures [44, 45, 46]. Cluster 3 is on-chain agent governance, which provides bond-settlement primitives—per-action bonds, runtime behavioral governance, and compensation mechanisms [48, 49, 50]—and an engineering-standard draft specifying agent identity, reputation, and validation registries, with stake-secured re-execution listed among its selectable trust models and payment mechanics declared out of scope [51]; what the cluster escrows is behavioral side effects, not model capability claims. The blank, stated in this narrowed form, documents an unsystematized combination rather than an absence of neighbors: attach a forfeitable bond to a falsifiable capability claim, with a mechanical forfeiture verdict. No verified work has systematized that step.

### 7.3 The governance cluster and matrix row: L4 facts ①–⑥

Cluster 3 in detail, because it carries the bond primitives. Bonded recourse settles compensable agent side effects by smart contract, with a bond attached to each action [48]. AgentBound provides verifiable behavioral governance for autonomous agents at runtime [49]. RAC trains agents to compensate for harms [50]. And ERC-8004—Trustless Agents—is an engineering-standard draft specifying identity, reputation, and validation registries for agents, with stake-secured re-execution listed among its selectable trust models and payment mechanics declared out of scope [51] (Ethereum Improvement Proposal draft; non-peer-reviewed; labeled as such). These are escrow mechanics at the protocol layer: the bond, the forfeiture, and the settlement all exist. What they escrow is behavioral side effects—harm, compensation, recourse—not claims about model capability. The distance to §7.2's unsystematized combination is short and precisely describable: attach the bond to a falsifiable capability claim and make the forfeiture verdict mechanical. The verified base records no work that has taken that step.

| **Attribute** | **Fact (with pointer)** | **Tier** |
|---|---|---|
| ① commitment object | the incentive structure of the verification interaction [9, 10]; on-chain bonds attached to agent actions and side effects [48, 49, 50] | E–M |
| ② tamper-spectrum coverage | strategically dishonest reporting within mechanism scope covered by design; Goodhart-type evasion of the *appearance* of honesty outside the guarantee; concealment under monitoring pressure demonstrated [30]; verifier gaming under RLVR demonstrated [47] | E–M |
| ③ recomputation cost | judge time plus mechanism design and simulation [9]; decentralized verification redistributes rather than reduces cost [44, 45, 46] | E–M |
| ④ verifier neutrality | judge and mechanism designer as trust roots (recursion transformed, not removed) [9, 10]; decentralization replaces the trust root with protocol consensus [44, 45, 46] | E |
| ⑤ commitment timing | mechanism rules fixed before interaction—protocol-level commitment native [9, 10]; bond-settlement primitives exist on-chain [48, 49, 50]; the bond × capability-claim combination is unsystematized (§7.2) | E–M |
| ⑥ distortion boundary | equilibrium guarantees ≠ deployment behavior; honesty-dominance is equilibrium-local; audit layers under optimization pressure erode (§5.3) | S |

## 8. Conservation and physical priors: invariants as external guarantors

### 8.1 Problems and mechanisms

The unit of account is a conserved quantity or physical invariant defined over the reasoning artifact. The verifier is external to the model, the data, and the auditor: a conservation law. Hamiltonian neural networks learn the invariant itself, so that learned dynamics approximately conserve energy [11]; physics-informed machine learning embeds physical constraints, partial differential equations among them, into the learning problem [12]; and systematic characterization of failure modes documents when physical priors help and when they hurt [13]. The line's audit promise, in its strongest form: an invariant that holds *by construction* can be rechecked by a third party with arithmetic alone—verifier independence maximal (④), verification cost minimal (③). Constructive invariants, identities built into the mechanism, are categorically stronger than soft constraints, residuals suppressed by training: the former hold at inference for arbitrary inputs; the latter can be violated exactly when the model is off-distribution, which is when the audit is most needed.

The invariant need not be physical. Formal specifications play the same structural role—an external standard the artifact must satisfy, independent of the artifact's constructor—and their verification literature is this line's computational sibling. OVERT verifies neural network controllers against safety properties reliably [52]; zkLLM produces zero-knowledge proofs of LLM inference integrity, letting a third party verify the computation without re-executing it or seeing the inputs [53]; and the zero-knowledge verifiable-ML line is surveyed systematically [54]. The zk route changes ③'s economics rather than ④'s geometry: verification at sub-linear cost, with the cryptographic assumption stack as a new, explicitly declared trust root.

### 8.2 Evidence and failure modes

Evidence. Conservation and structure preservation were demonstrated in learned dynamics [11]; the breadth of the physics-informed program is documented [12]; failure modes of physical priors are characterized [13]. Consistency tier for all three.

Failure modes. First, conservation ≠ truth (⑥): an identity can hold exactly while every entry in the ledger is wrong—the books balance; the accounting is fiction. Physical priors constrain the ledger's *form*, not its content's correctness; content correctness belongs to L1/L2 and is not inherited from the invariant. Second, soft constraints are violable at inference (②): gradient-suppressed residuals do not survive distribution shift or adversarial inputs, and only constructive invariants give run-time books. Third, prior–optimization conflict: physics-informed objectives exhibit optimization pathologies in exactly the regimes where the prior matters [13]—the audit instrument can damage the system it audits. Fourth, the invariant-chooser trust root (④): which invariant, which form, which parameters—the modeling choice is upstream of the ledger, and the books inherit its assumptions unaudited.

The computational side is held by the formal-verification and zero-knowledge families of §8.1; the physical side's sub-blank is stated narrowly. Conservation laws as run-time auditors—post-hoc reconciliation of an artifact against its invariant, as opposed to a training constraint—have, to our knowledge, no machine-learning-venue work. The nearest neighbors are the physics-informed training-constraint literature itself [12, 13] and generalized anomaly detection in cyber-physical systems (outside the verified base, hence uncited here). Whether the case study of §18 is the first conservation-as-run-time-auditor instance in an ML artifact is a claim the completed novelty search did not refute—and not one this survey asserts.

### 8.3 Matrix row: L5 facts ①–⑥

| **Attribute** | **Fact (with pointer)** | **Tier** |
|---|---|---|
| ① commitment object | conserved quantities and physical invariants over the learned/ artifact system [11, 12, 13]; formal specifications as the computational sibling [52, 53, 54] | E |
| ② tamper-spectrum coverage | constructive identities: ledger deviations arithmetic-checkable [11]; soft-constraint violations reappear at inference off-distribution [12, 13]; zk proofs verify computation integrity without re-execution [53] | E |
| ③ recomputation cost | arithmetic recomputation of the invariant—minimal in the survey; the ideal end of ③; zk verification at sub-linear cost [53] | E |
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

T1.5 was registered as the construction-failure-fix probe for T1. Its own registered fix was tool-side: it replaced the reasoning-model configuration with a non-reasoning one and raised the token budget to the recorded value of 500 (construction check C-T15-1), which eliminated the empty-response failure mode of T1 (from 49.3 percent to 0) and confirmed that the corrected construction preserved the direction of the standing verdicts. T1.5 verdict: `results/_v4_supp_t15_verdict.md`, 52,884 B, SHA-12 `52C985429C91` (measured 2026-09-26). Its verdict additionally proposed a pair-count expansion of +60 calls (its Section 3.4, Plan A), which the PI ruled on (ruling t15_ext: 6 cells × +10 = +60 calls) and which the next stage executed. T1.5r2 was registered as the expansion probe: the pair-count plan (6 pairs per teacher) sat below the registered minimum (N_min = 10); the expansion executed the ruled +60 calls (recorded formula: 5 teachers × 2 prompts × 3 re-asks per cell × 6 cells = 180 calls, giving 15 pairs per teacher; measured execution: 62 new calls across the six cells, 10 to 11 per cell (errata-chain annotation E-37.2, drafted for the next append round: the source verdict file's summary line writes 60, an arithmetic slip in its own per-cell formula, which sums to 62; the measured execution consists of the ruled 60 re-ask-2 expansion calls plus two make-up reruns recorded within the same execution, and the execution record registers 62; the ruled +60 budget was executed in full; the frozen verdict file itself is unmodified), at which point the relaxed construction check (K-N11-N1,T1relax) passed literally, and the false-falsification root cause recorded in T1 was eliminated. T1.5r2 verdict: `results/_v4_supp_t15r2_verdict.md`, 64,145 B, SHA-12 `8355724A26E3` (measured 2026-09-26). Each stage's verdict states: no overturn of standing verdicts, no re-adjudication of prior verdicts, conclusions enter the errata chain as robustness notes.

### 13.4 The pipeline as a methodological contribution

The pipeline's output in this phase was not a rescued experiment; it was the N-26 audit of Section 14, a falsification whose construction doubts had been paid down stage by stage before filing. The pattern generalizes: *probe* (is the signal sensitive to construction knobs?), *correct* (fix the construction), *expand* (meet the pre-registered minimum sample), *truly adjudicate* (file only what survives). Each stage is itself a registered, verdict-anchored probe that cannot overturn standing verdicts, so the pipeline cannot be used to launder a standing FAIL into a PASS; it can only remove β doubts from a future filing.

---

## 14. The N-26 True Audit

### 14.1 The proposition and the construction

The N-26 audit re-ran the V3 distillation chain end to end to adjudicate one proposition: *call-side metadata alone can distinguish distilled outputs from teacher outputs*. The re-run covered five teachers (internal codenames kimi, GLM_1, GLM_2, coze, minimax; internal labels, with all GLM-related statements deferred to the PI's GitHub repository as the sole authoritative source, hence no model versions, endpoints, or product names here), 22 captions, 10 cells, at least 5 calls per caption, with a four-tuple record per call (prompt id, prompt text, response text, per-call metadata). The worker executed 1,090 calls in total: 518 on the teacher side and 572 on the distill side. N-26 verdict: `results/_v4_supp_l14v3_n26_verdict.md`, 64,485 B, SHA-12 `F4435801D09F`; L14+ preregistration: `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md`, 61,547 B, `05B975A86989` (both measured 2026-09-26). Two construction checks passed: non-degeneracy (K-N26-N1, pass = True: every cell at least 110 calls with at least 5 successful calls per caption, except the teacher-kimi cell at 77 calls with at least 1 successful call per caption after an early batch was cleared) and routing/integrity compliance (K-N26-N2, pass = True: 100 percent compliance on the four routed endpoint groups, no routing required for the fifth by design, and a cumulative empty-response rate per teacher of 0.021–0.075, far below the 0.50 threshold).

### 14.2 The adjudication

Of the five registered kill-lines, one triggered: **K-N26-2 TRIGGERED** (true falsification in the v1/v2 direction): the pooled binary AUC of a teacher-versus-distill classifier on metadata features was 0.5663, far below the 0.75 true-falsification line. Two independent robustness checks accompany the pooled value: the read-variant sensitivity test held across all five read variants (AUCs in the recorded range 0.4459 to 0.5916, every one below 0.75; errata-chain annotation E-37.1, drafted for the next append round: the source verdict file's two summary statements record this range as 0.4459 to 0.5844, omitting the drop_glm2 read; the independent re-measurement of 2026-09-27 gives 0.5916 as the five-read upper bound, which is written here; all five reads remain below 0.75, so the robustness finding is unchanged; the frozen verdict file itself is unmodified), and the five-fold cross-validation returned 0.5271, 0.5266, 0.6318, 0.5740, and 0.5719, all below 0.75. Call-side metadata does not separate distilled outputs from teacher outputs in this construction, and the proposition is truly falsified. **K-N26-1 NOT TRIGGERED**: the five-teacher mean teacher-side accuracy was 0.5617, below the 0.70 line (kimi at 0.7512 was the only teacher at or above 0.70; the other four, including GLM_2 at 0.6364, below). **K-N26-3 NOT TRIGGERED**: three of five teachers fell below 0.60 (GLM_1 0.3955, coze 0.5344, minimax 0.4909), short of the registered threshold of at least four teachers.

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
---

# Lower-Half Placeholder Directory（下半件占位目录）

> Working note for the drafting chain: the items below are the scope of the lower-half part file (`_v3v4_merged_paper_2026_09_27_v0.1_part2.md`, next round) and of the assembly round (complete v0.1). They are listed here so that the part boundary is explicit and no section is silently dropped; they are not expanded in this file.

## Part III · The Synthesis Zone (planned Sections 17–24)

- **§17 The V4 Chain on the Five-Line Matrix** — source: new composition per the architecture blueprint; the survey's Table 3 upgraded to the merged matrix (v9 Table 3 plus a sixth row for the V4 chain); the V4 chain mapped column by column onto the five-line matrix as a program-level instance of the externally empty commitment-timing column. No first/only claims beyond the recorded ones.
- **§18 Case Studies under Full Parity** — sources: v9 §9.3 (the first-work case study, matrix row 6) plus the V4-phase chain materials from the v1.1 verdict line, entered at the same register as the external lines; the first work is detailed as the first case study in §18.1 (the pointer carried from Section 1).
- **§19 Cross-Line Lessons Revisited** — source: v9 §9.2 (lessons (a)–(d)) with V4-side commentary added where the chain instantiates a lesson.
- **§20 Outlook: Machine Worldviews, AI Scientists, and the Open Phase** — sources: v9 §10.1–§10.2 (worldviews; open problems OP1–OP8, with the merged-paper pointer remaps §20.1/§20.2 already applied in Part I's inline pointers) plus the V4 open-phase paragraph; boundary sentence (O6) required.
- **§21 Limitations** — sources: v1.1 §11 (items (1)–(7)) plus survey-side limitations, merged.
- **§22 Data Availability, Provenance, and Self-Overlap** — sources: v1.1 §10.1–§10.3 plus the v9 availability and provenance paragraph; the v9 literature protocol (v9 §1.3, including its entry-format note) is condensed into §22.4; the v9-never-submitted disclosure (this merged draft is the only public carrier of the survey material) and the FTFB on-hold caliber are stated here.
- **§23 AI-Use Disclosure** — sources: v1.1 §12 and the v9 AI-use disclosure, merged; the drafting-model naming and in-repository anchoring per the v1.1 verdict.
- **§24 Conclusion** — rewrite; closes at the recorded scope only; boundary sentence (O6) required.

## References (unified, deferred to the lower half)

- Dual-track plan per the literature merge package (M1): an A-track external sequence in merged first-appearance order with single document-wide numbering, plus a B-track internal asset ledger (Appendix A, unnumbered, following the v1.1 dual-track discipline).
- The Part I bracket tokens `[n]` (survey-source numbering, 1–61) are renumbered document-wide at assembly; Nosek et al. 2018, Popper 1959, and Yang et al. 2025 (arXiv:2510.15746) are inserted at their first-appearance positions; the conditional DAS entry and all pending-verification markers are carried per the merge package; zero new citations are added by this draft.
- The first-work entry (survey-source key04) is carried as the companion-study form with an anonymized author block, per the double-blind fork; the second work (FTFB) is cited per Section 1's on-hold anchor, with the public-arXiv-release upgrade trigger.

## Appendix A · Internal Asset Ledger (deferred)

- v1.1 Appendix A migrated in full (Task B chain, dataset addenda, T-series and N-26, governance, companion works and V1, letters family, recorded anchors, version-pending items), plus new rows registering the merged-draft input anchors (the survey source and the V4-line v1.1 pair).
- Note for the lower-half round: the E-37.1 correction (five-read range upper bound 0.4459–0.5916) must also be applied at the Appendix B K-N26-2 row, where the v1.1 source records 0.5844, with the same drafted errata-chain annotation.

## Appendix B · Kill-Line Tables (Literal Carries) (deferred)

- v1.1 Appendix B migrated in full with the E-37.1 range correction applied at the K-N26-2 row as above; all other values literal.

## Appendix C · Merge Provenance and Interpretation Registry (deferred)

- Per-section incorporation ratios (v9 / v1.1 / new, per the architecture blueprint's mapping table).
- Pointer-remapping list (this part file's inline remaps registered verbatim): v1.1 §2–§9 → §9–§16; v1.1 internal `Section N` pointers remapped (2→9, 3→10, 4→11, 5→12, 6→13, 7→14, 8→15, 9→16); v1.1 §10–§13 → §22/§21/§23/§24; v9 §9.1/§9.2/§9.3 → §17/§19/§18; v9 §10 → §20; v9 §1.3 → §22.4; v9 Table 1 strength-row pointer §1.3 → §3.2; two drafted E-37 sub-entries at §13.3 and §14.2.
- Self-check plan and 8-gram self-overlap measurement placeholder, measured against the first and second works at the typesetting round, per the survey's self-citation precedent.
- Interpretation registry (R1–R4):
  - **R1 (work-sequence numbering)** — registered: first work (the scattering-layer paper) → second work (FTFB) → third work (this merged draft); the V4-line paper v1.1 is merged into the third work and does not occupy a separate public slot.
  - **R2 (single-slot presentation)** — registered: the survey's five lines and the V4 chain are presented in one paper, Part I before Part II.
  - **R3 (frozen-number and verdict-literal discipline)** — registered, including the E-37 family drafted in this part file and the Appendix B propagation note.
  - **R4 (externally reported re-adjudication of a prior verdict)** — **pending-proof placeholder, explicitly not closed**: the formal record is pending; this draft records no content from it, cites nothing from it, and takes no position on it in either direction.
- Confidential-source discipline: no citation of, quotation from, or pointer to the confidential weekly report anywhere in this paper; all numbers in this paper trace to on-disk public-chain artifacts only.

## Assembly-round checklist (complete v0.1)

1. Apply the unified A-track renumbering document-wide; compile the references; re-run the pending-marker check.
2. Apply the Appendix A/B/C propagation (E-37 family, input anchors, provenance ratios, registry R1–R4 states).
3. Draft Part III per the blueprint's synthesis zone and deduplication rules (D1–D10).
4. Full-file checks: F-series frozen text verbatim; O-series placeholders with zero closure wording; double-blind five-point pass; verdict literal carry; 8-gram self-overlap measurement; abstract character budget and ASCII; confidential-source zero-citation check.

*(End of the upper-half part file. The lower-half part file continues from Section 17.)*
