# Commission (theory-input solicitation) — deposon Project / P-B `T-2` (`null-L`) and `T-3` (`null-U`) · for the **copilot agent**

> **Status**: **draft** · prepared by the project's main agent on 2026-10-17 at the PI's direction, **for PI review and release decision** (release is the PI's). The project side does **not** transmit this letter itself; once approved it is filed in `letters/` and passed out by the PI.
> **Direction of record (verbatim)**: PI, 2026-10-17 (≈14:54 CST): 「**现在解决 T-2/T-3，没有委托怎么可能 GLM 面会有动作**」.
> **Addressee change (verbatim)**: PI, 2026-10-17 (≈15:09 CST): 「**本次委托 grok，copilot agent**」——此令改前令所定之受托方。本件为改令后**分立封之一**，姊妹封 ＝ `letters/_commission_t2_t3_theory_inputs_grok_2026_10_17.md`（**内容同构、各署其抬头**）。前令所据之 GLM 面草稿 `letters/_commission_t2_t3_theory_inputs_2026_10_17.md`（SHA-12 `393d71e51fbf`）**0 回改**，原样留痕。
> **This commission contains no reply outline** (PI standing ruling of 2026-09-24: commissioning materials do not pre-structure the addressee's reply). Everything below is a *specification of what is wanted* and *delivery-format and evidence requirements only*. Structure, level of detail and style remain yours.
> **Hard boundary**: this document commissions **inputs**, not a verdict. It modifies no repository document; it adjudicates nothing; it changes no threshold and no pre-registered wording; nothing in it is adopted until the PI so rules. **Delivery is not adoption.**

---

## §0 What this transmission does (one paragraph)

Dear copilot agent,

We are asking you, as an **independent external theory source**, to help us close two theory inputs that are still carried as `null` on our registry: `L(M,T)` (item `T-2`, the lower bound) and `U(M,T)` (item `T-3`, the upper bound). Our own theory-side work has reached a **framework** but **no value**: the conditional-minimum and conditional-tolerance derivations exist, and the per-cell blockers are itemised and audited, but every one of the fifteen cells (`3 mechanisms × 5 task families`) still reads `null-L` / `null-U` for want of an instantiated observation law and policy class, or an instantiated convergence certificate and its bridge to regret. **Please deliver — or, under §1, originate — those fifteen `L` cells and fifteen `U` cells, or state, cell by cell and with reasons, why a cell cannot be given.** We already hold an external proposal on one of these faces; you are free to accept it, reject it, correct it, or replace it (see §2.3 and §6).

## §1 Origination authorisation (what you may and may not source)

1.1 You are **authorised to originate** the missing content for `T-2` and `T-3` — that is, to define and supply, **as the source**: the finite observation law `Q(z|x)` and state distribution with a per-cell acceptance-key assignment and an admissible policy class matching the instance; the mechanism-specific transition law, convergence target, certificate, and the proved bridge from regret `D` to the certificate's tolerated perturbation; and, per cell, a value or closed form for `L(M,T)` / `U(M,T)` or an explicit statement that the cell cannot be given.

1.2 Where an item comes from somewhere else, name the giver/venue. Where you originate it, the attribution must say so (e.g. "originated by the addressee under this commission"). Content originated under this authorisation stands as **source content** for these two inputs — it is not a substitute or unsourced filler.

1.3 **Correctness and adoption remain with the project side** (PI / verdict-keeper). Delivery is not adoption, and a delivered value is registered as your **proposed true value** pending acceptance. This mirrors the standing precedent for the sibling inputs `T-1` / `T-4`.

1.4 This authorisation concerns `T-2` and `T-3` only. It changes no pre-registered rule, no threshold, no wording, and no historical record.

1.5 **What origination does not license.** Do not fill a missing item with an estimate, a stand-in drawn from another protocol, a calibrated or historically replayed figure, or a number reverse-engineered to make a verdict come out. An honest `null` with a reason is a **complete delivery** for that cell, and is preferred by us over an unfounded number (§5.3).

## §2 The state of play, as recorded (verbatim where quoted)

### 2.1 The `T-2` / `T-3` blockers on record

From our theory-side reply of 2026-10-10 (SHA-12 `a975c7990cd8`):

- "**Numerical T-2 minima and convergence-derived T-3 tolerances remain `null`.**" (line 14)
- "For each T-2/T-3 cell, **value source: none**." (line 76)
- "`null-L` means the observation law and admissible policy class have not been instantiated. `null-U` means no mechanism-specific convergence certificate and its connection to regret have been established. **These are reasons for absent values, not numerical substitutes.**" (line 56)
- The instantiation condition, verbatim: "To instantiate T-2, supply those finite laws and keys plus evidence that the actual information and policy restrictions match, **or derive the appropriate sequential minimum instead**." (line 103)
- The `null-U` blockers, verbatim: "M1 needs a defined transition law, a convergence target and certificate, and a proved connection between this regret and the disturbances the certificate tolerates. **"Greedy" does not specify M2's dynamics or convergence target.** For M3, **a stationary uniform sampling distribution is different from convergence of an individual action sequence**; choosing the former as "convergence" would not establish mechanism tolerance." (line 111)
- A reference point that is **not** a candidate: "This is a result for that specified random policy, **not** a convergence tolerance **nor automatically the information-constrained minimum**." (line 113) — i.e. `D(M3,T) = 3H/4` is a self-check on units, and may serve neither as `L` nor as `U`.

### 2.2 The registry specification you are asked to instantiate

Our internal solicitation form of 2026-10-14 (SHA-12 `21abb5173b87`) already specifies both items, including the five-level criteria that define what counts as a solution, the options for each unresolved choice, and the prerequisite list. **We are not restating its content here — it is the specification.** Key anchors, for orientation only:

- `T-2` five levels: **L-甲 (law)** the complete finite table of `Q(z|x)` plus `p(x)` · **L-乙 (class)** the admitted policy class's full rule list and class ID, each rule annotated as to whether the five assumptions hold on the target cell · **L-丙 (expression)** the expression of `L` must be *consistent with* the class of L-乙, not merely formula-correct, otherwise a corresponding sequential minimum must be derived · **L-丁 (value)** a number or closed form bound to the six-tuple `(value, observation-law ID, policy-class ID, key-face ID, H, cell)` · **L-戊 (anti-degeneracy)** cells landing on "structural zero" must be *registered* as structural zero, and units must agree with the `3H/4` reference.
- `T-3` five levels: **U-甲 (law)** an explicit transition law `F` with **non-empty** state `S_t` and numeric parameter domains, for **each** mechanism · **U-乙 (certificate)** a convergence target plus a **finitely-checkable** certificate · **U-丙 (bridge)** a **proven** mapping from regret `D` to the perturbation the certificate tolerates, with direction and tightness · **U-丁 (value)** a value bound to the five-tuple `(value, certificate ID, state-process ID, perturbation-map ID, cell)` · **U-戊 (anti-degeneracy / non-vacuity)** `U` must be identifiable and provably not vacuously large.
- Open choices left to you: for `T-2`, which observation-law option (甲/乙/丙) and which policy class (`Π_full` / `Π_fin` / `Π_seq`); for `T-3`, which convergence anchor (甲/乙/丙) and the definition of the state process.

### 2.3 An external proposal already on our books — you are not required to accept it

A reply from another external face (2026-10-15, SHA-12 `44311ade19de`) does propose values for both items, and our own audit of it (SHA-12 `793986174b23`) records both what survives recomputation and what does not. **Neither the proposal nor its audit is adopted.** We give you this because a second independent assessment is worth more than a first one that has already been contested:

- `T-2`: under a relaxation R-L1 it preregisters a noisy `M1` observation channel and admits the 256 observation-to-action maps, giving `L(M1,T) = 3g_aether / [(1-η) + η·g_couple + 4·g_aether] · H`, evaluated at constructor defaults as **`3/14 · H`**; `M2` registered as structural zero.
  - **Audit, `F3`**: the arithmetic is confirmed, but the closed form **holds only for 4-choice, binary-value families**; recomputed per family it gives `7/29` for `T3` and `1/12` for `T4`. The reply's own summary states it without that qualifier. **Scope too broad.**
  - **Audit, `F4` / `X3`**: the parameters `η = 0.5`, `g_couple = 1.0`, `g_aether = 0.1` are **constructor defaults, not preregistered frozen values**. The value holds only on an unfrozen premise.
- `T-3`: under route 乙 it proposes a dissipative recursion `S_{t+1} = (1-γ)S_t + γ·1{A_t ∉ K_t}` with certificate `E[S̄_H] ≤ τ_cert`, yielding `U = H·τ_cert / [1 - (1-γ)^H]`.
  - **Audit, `F6`**: the form is confirmed compatible and consistent with `0 ≤ L ≤ D ≤ U ≤ H`.

**You may take these as starting points, as things to correct, or as things to ignore.** You are not required to re-derive anything already on our record, and you are not required to accept any prior conclusion. Your reply is your own.

### 2.4 Project-side diagnoses that bind whatever you deliver

Recorded on our sourcing face of 2026-10-15 (SHA-12 `bcb0d60fdd2d`); each is a caution we ask you to respect, not a conclusion we ask you to reproduce:

- **S-1** — ⛔ adopt no `L`/`U` value on the strength of route A (all artifact) or route B (no records); the recommendation on record is to **maintain `null`**.
- **S-2** — `D(M3,T) = 3H/4` is a **dimensional self-check only**; ⛔ as `L`, ⛔ as `U`.
- **S-3** — where `M2` has `D ≡ 0` (structural zero), its `U` is to be **registered, not assigned**.
- **S-4** — the `T4` observation law is **constructively degenerate** (no shuffle); any zero-valued `L` for `T4` is therefore a **constructive artifact**.
- **S-5** — the "optimal" rule of `Π_fin` **always equals the majority-label rate**; a `T-2` evaluated on the present experiment surface would be **measuring the imbalance of `p(x)`, not IC capacity**.
- **S-6** — for the `U` bridge, performative-prediction convergence / tight-lower-bound results are registered as a **methodological anchor**, not as a value.

## §3 Task `T-2` — requested delivery

Deliver, **per cell**, for each of the 15 cells `{M1, M2, M3} × {T1..T5}`:

1. a finite observation law `Q(z|x)` (entries non-negative, rows summing to 1, zero-weight terms contributing 0) together with the state distribution `p(x)` — **stated as a design specification, not as an estimate from measurement**, unless you can point at the evidence for the estimate;
2. the **acceptance-key assignment** per cell, i.e. which actions the criterion accepts at each decision, and the number `H` of decisions your value assumes;
3. the **admissible policy class** you optimise over, with its ID and rule list, annotated per cell as to whether the five assumptions hold there;
4. the **value or closed form** for `L(M,T)`, or the **corresponding sequential / conditional minimum** if the class in (3) is not the one a closed-form proof assumes;
5. your **self-declaration** against levels L-甲 … L-戊, level by level.

Three specific things we want addressed rather than assumed:

- **Mechanism-specific policy classes.** A single policy class applied to all 15 cells is exactly what we are trying to escape. Please instantiate the admissible class **separately for each mechanism** — in particular where the mechanism's own dynamics constrain or dictate the policy (a constrained `M1`, a forced uniform `M3`), the admissible class differs and the closed form does not transfer automatically. Say which class applies to which mechanism, and why.
- **`M1` full-information exposure.** On our harness, `M1` and `M2` read the ground-truth key directly, so their observation channel is effectively the noiseless identity channel and their `L` degenerates to **structural zero** across 10 of 15 cells. Do not silently deliver a non-zero number for these cells. Either register the structural zero, or state the design change that would make the channel non-degenerate and price it.
- **Evidential status of the observation law.** There are zero LLM observation records on our disk, so any `Q(z|x)` you supply is a **stipulation by design**. Label it as such, and carry the observation-law ID in the binding tuple — a `T-2` value without its observation-law ID is not recomputable.

## §4 Task `T-3` — requested delivery

Deliver, **per cell**, for the same 15 cells:

1. the **transition law** `S_{t+1} = F(S_t, A_t, ξ_t)` with **non-empty** state `S_t` and explicit numeric domains for every parameter — for **each** mechanism separately;
2. the **convergence target** (fixed point or stationary distribution) and a **finitely-checkable certificate** of convergence;
3. the **proved mapping** from regret `D` to the perturbation the certificate tolerates, **with direction and tightness** stated;
4. the **value or closed form** for `U(M,T)` bound to the five-tuple, or an explicit statement that the cell cannot be given;
5. your **self-declaration** against levels U-甲 … U-戊.

Mechanism-specific convergence, in the terms our record already uses:

- **`M1`** — needs a defined transition law, a convergence target and certificate, and the proved connection between this regret and the disturbances the certificate tolerates.
- **`M2`** — the label "Greedy" does **not** by itself specify a dynamics or a convergence target. Please state the dynamics you assume for "pure Greedy", and what it converges to; if that is not well-posed without further definition, say so rather than choosing a target for it.
- **`M3`** — a **stationary uniform sampling distribution is different from convergence of an individual action sequence**. Choosing the former and calling it "convergence" would not establish a mechanism tolerance. Please state which of the two you mean, and justify the choice.

Two further cautions from our record: where a mechanism's `D ≡ 0`, **any** `U` would be admissible and assigning one would be fabrication — register it instead (S-3). And do not import a threshold from a different protocol's convergence certificate without proving the cross-protocol mapping; a bounded mistake count does not prove a state process converges, and the bridge is the whole of `U-丙`.

## §5 Evidence, delivery and attribution requirements

### 5.1 Per-cell evidence bundle

Every item supplied or originated under this transmission must carry, at delivery:

1. **Source attribution** — giver/venue; where you stand as source, say so explicitly. Our canonical theory-side source-declaration form is at the correction register of 2026-09-30 (SHA-12 `61b139efd0ef`, line 122), whose source-name slot is updated **by the actual executing party** at delivery — we do not pre-fill it, and the historical wording there stands unmodified.
2. **Derivation chain** — basis (inputs, definitions and prior results relied on), assumptions (stated explicitly, not buried), and steps at a detail level that lets an independent reader follow and check the path from basis to result. Outside results relied on must be identified precisely.
3. **Explicit definitions** — every symbol, scale, unit and constant defined in the delivered text; no orphan constants, no placeholders, no undefined symbols. A third party must be able to recompute `L(M,T)` / `U(M,T)` from your delivered text alone.
4. **Applicability declaration** — per cell for `T-2` and `T-3` (15 cells each), stating where the item applies and where it does not.
5. **Self-declaration** against the five levels (§2.2), level by level, per cell.

### 5.2 Fingerprint receipt

With the delivery, report the fingerprint of each delivered file as **path + SHA-12 + byte count + line count** (SHA-256, first 12 hex, lowercase; `hashlib.sha256`, not a language built-in `hash()`). Fingerprints are reported **with** the delivery, outside the delivered files.

### 5.3 Separation of supplied and non-supplied parts

Mark every cell you cannot supply, item by item, **with its reason**. A cell left `null` with a stated reason is a complete delivery for that cell and does not disqualify the rest. Missing items are **not** to be replaced by estimates, substitutes, or self-authored formulas standing in for them.

### 5.4 Model and tool disclosure

State the exact model (name/version) used, your serving endpoint if known, and any tool calls made. If an exact build identifier is not exposed to you, say that plainly rather than approximating it. This is a standing requirement on our external collaborators. **Confirm that you are the addressee named on the header**: a prior reply on this project merely restated the header without confirming its own identity, and that was recorded as a compliance defect — restating the header is not a confirmation.

## §6 Standing constraints (please respect in your reply)

1. **Kill-lines are frozen before measurement.** Any recommendation requiring a retroactive change to a frozen threshold must be flagged as such, not smuggled in. Our kill-lines are cited in §8 and are not yours to move.
2. **Dimension discipline.** Do not equate quantities of different dimensions. A bounded mistake count does **not** prove convergence of a state process; a rate-scale quantity does **not** transfer to a count-scale one unlabelled; an upper bound on payoff alone is not a bound of 1 on a normalised difference.
3. **Anti-degeneracy.** Where a candidate is structurally zero, vacuously large, or trivially equal to a label prior, **register it as degenerate** rather than presenting it as a solution.
4. **No adopted conclusions.** Nothing on our record is adopted, including the items in §2.3. Do not treat any prior proposal, audit finding, or "preferred" route as settled.
5. **Credentials.** Do not read, request, handle or record any key or credential. Credentials are injected on the project side and are never written into any artefact, log, or delivery. Analysis only: **do not execute, modify, or upload anything on our behalf.**
6. **No invention of external references.** Cite only sources you can identify precisely; if unsure, say so.

## §7 Reply form and channel

1. A structured written reply addressing `T-2` and `T-3` in that order, carrying a per-cell table across all 15 cells for each, and **ending each of the two items with a one-line verdict**: *derivable (with value/rule)* / *derivable-with-relaxation (name the relaxation)* / *underivable as stated (obstruction)*.
2. Model, endpoint and tool disclosure per §5.4.
3. Checkable references only; mark anything you could not verify.
4. Fingerprint receipt per §5.2.
5. **Deadline**: **[PI to fill — not set by this draft]**. (The scheduling on record is a *suggestion* face only, carrying a 0-adjudication marker; the deadline itself is the PI's to set.)
6. Delivery channel: **hand the reply to the PI**, who will file it — we do not transmit on your behalf and you need not reach any endpoint yourself. A reply counts as **received for our registry** when a reply artefact is present **either** in the repository's `letters/` **or** under `〔本地资料区〕\GLM` (our stable delivery surface; the other location may be swept at any time), **and** it carries the **per-cell delivery table for both `T-2` and `T-3`**, **and** the **out-of-file fingerprint receipt** (SHA-12 / bytes / line count) required by §5.2. Our `C5` item (G-D03 adjudication, receipt-in-place) is judged mechanically on that artefact's presence. The artefact must state **which addressee it answers** — grok or copilot agent — so the registry can attribute the receipt per face; an unattributable receipt cannot be counted against `C5`.
7. Please do **not** execute, modify, or upload anything on our behalf; analysis and written derivation only.

## §8 Material references (all local repository; fingerprints measured 2026-10-17)

| # | Item | Path | SHA-12 | Bytes |
|---|---|---|---|---|
| 1 | P-B V0 spec (sole source of the `D`, `L`, `U` definitions; §3.2 mechanisms, §3.4 metric, §3.5 bounds, §4 kill-lines, §5 A1) | `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | `423c84de20d5` | 15,457 |
| 2 | `T-2`/`T-3` solicitation form — **the specification to instantiate** (five levels, 甲/乙/丙 options, prerequisites, prohibitions) | `results/_t2_t3_value_request_form_2026_10_14.md` | `21abb5173b87` | 15,054 |
| 3 | `T-2`/`T-3` sourcing face (diagnoses S-1 … S-6, §2.4 above) | `results/_t2_t3_value_sourcing_2026_10_15.md` | `bcb0d60fdd2d` | 24,658 |
| 4 | `T-2`/`T-3` null-resolution design (entity source of #2) | `results/_ge01_t2_t3_null_resolution_design_2026_10_13.md` | `c2af59477178` | 43,820 |
| 5 | Theory-side reply 2026-10-10 — **the blockers and the instantiation condition, quoted in §2.1** | `letters/_codex_c4_values_unblock_reply_2026_10_10.md` | `a975c7990cd8` | 21,486 |
| 6 | Sibling-input commission (precedent for §1 origination authorisation and §5 evidence bundle) | `letters/_commission_c4_values_unblock_EN_2026_10_10.md` | `fde64a863b09` | 10,244 |
| 7 | External reply 2026-10-15 (§2.3 proposal) | `letters/REPLY_FROM_GEMINI4_GE01_THEORY_INPUTS_2026_10_15.md` | `44311ade19de` | 44,520 |
| 8 | Audit of #7 (§2.3 findings `F3`/`F4`/`F6`/`X3`) | `results/_gemini4_reply_verification_register_2026_10_15.md` | `793986174b23` | 33,393 |
| 9 | Original theory-input acquisition request (the parent solicitation; 5 open items) | `results/_v5_theory_input_acquisition_request_2026_09_29.md` | `19099ecb3c46` | 10,751 |
| 10 | Theory-side source-declaration canonical form (§5.1 item 1) | `results/_c4_theory_source_caliber_correction_2026_09_30.md` | `61b139efd0ef` | 25,022 |
| 11 | Harness (mechanism implementations; `M1`/`M2` key exposure, `T4` no-shuffle) | `tools/exp_harness.py` | `026575ff3829` | 41,428 |
| 12 | Distortion calculator (metric, guard, `kill_decision`) | `tools/distortion_calculator.py` | `410a12482eef` | 40,611 |

**Two fingerprint notes, so you are not misled.** (a) For #1 we measured `423c84de20d5` / 15,457 B on this disk; a retrieved specification pack records the same path as `aab9d78ada2d` / 15,549 B. The two differ; that pack's own rule is to recompute against the on-disk final state, and the value we cite is our own measurement of the copy in this repository. (b) Line references into #11 in prior external material do **not** match this on-disk copy (audit item `X4` records a 7/7 mismatch); we therefore cite #11 by fingerprint only. Please verify against the file itself rather than against any quoted line numbers.

## §9 Boundary of this draft

This draft modifies no repository document; makes no adjudication for the PI or the verdict-keeper; changes no threshold and no pre-registered wording; supplies no value, formula, outline or verdict; and is **not adopted automatically**. The origination authorisation in §1 takes effect **only upon the PI's release of this letter**. The release decision and the deadline are the PI's. Fingerprints (SHA-12 / byte count / line count) are reported with delivery, outside this file.

With thanks,

**PI** — deposon project
(drafted by the project's main agent at PI's instruction; dispatch only after PI approval)
