# External Commission Letter — deposon Project / G-E01 Theory-Input Face (for **Gemini 4**)




## §1 Purpose

Dear Gemini 4,

We are the deposon project team. We are commissioning an **independent external analysis** of a theory-input face of our preregistered experiment series **G-E01** (game-theoretic evaluation harness, "P-B" face: 4 task families × 3 mechanisms × H decisions per cell, with frozen kill-lines fixed *before* any measurement — our core discipline, FTFB).

We ask for your analysis on **four tasks** (T1–T4 below). For each, we give the exact state of play, the frozen constraints, and what we cannot settle internally. **Please answer only what you can justify**; where a value cannot be justified, say so explicitly and state what evidence would be needed — an honest "indeterminate" is strictly preferred over an unfounded number.

## §2 Standing constraints (please respect in your reply)

1. **Kill-lines are frozen before measurement.** Any recommendation that requires changing a frozen threshold retroactively must be flagged as such, not smuggled in.
2. **Reproducibility.** Give derivations, not just conclusions. Cite only sources you can identify precisely (no fabricated references; if unsure, say so).
3. **Model disclosure.** State the exact model (name/version) used for your reply, per our standing convention for external collaborators.
4. **Dimension discipline.** Do not equate quantities of different dimensions (e.g., a bounded mistake count does *not* prove convergence of a state process).
5. **Anti-degeneracy.** Where a candidate value is degenerate (e.g., structurally zero, vacuously large, or trivially equal to a label prior), register it as degenerate rather than presenting it as a solution.

## §3 Task T1 — ε\* for the kill-line track

We run a **dual-ε distortion calculator** (PI-ratified): the *self-check track* is fixed at **ε = 0.1**; the *kill-line track* takes **ε\***. The kill-line track's ε\* is **not yet fixed in prereg** (our internal item BL-2).

- **Ask**: recommend a value (or a principled selection rule) for ε\*, with justification. State explicitly: sensitivity of any verdict to your choice; whether ε\* should differ from the self-check 0.1 and why; and the failure mode if ε\* is chosen too small / too large.
- **Context**: our current experiment (Task T3 below) reports only the raw error rate `D` (rejected-decision rate), precisely *because* ε was not fixed. Your recommendation will be locked into prereg before the next run.

## §4 Task T2 — null-L / null-U (theory inputs `T-2` / `T-3`)

Two theory inputs remain `null` after exhaustive internal work (two routes each; both routes judged "0 levels achieved" by our registry). We need an independent assessment of **whether either is derivable at all under our constraints, and if so, along which construction**.

**T-2 (`null-L`)** — the exact minimal expression of distortion under information restriction. Our five-level acceptance criteria (translated from our frozen registry; each level must hold simultaneously):

- **L-1 (law)**: complete finite table of the observation law `Q(z|x)` (cells non-negative, rows sum to 1, zero-weight terms contribute 0), plus the complete table of `p(x)`.
- **L-2 (class)**: complete rule list + class ID of the admitted strategy class, with each rule annotated whether the five assumptions hold on the target cell.
- **L-3 (expression)**: the expression of `L` must be consistent with the strategy class of L-2 (not merely "formula-correct"); otherwise a corresponding sequential minimum must be derived.
- **L-4 (value)**: a number or closed form for `L(M,T)`, bound to the 6-tuple `(value, observation-law ID, strategy-class ID, key-face ID, H, cell)`.
- **L-5 (anti-degeneracy)**: cells landing on "structural zero" must be *registered* as structural zero, not presented as solutions; dimension must agree with the reference point `3H/4` (see below).

Internal state: 0 LLM observation records on disk (observation law can only be given *by design*); M1/M2 mechanisms read `context['value']` directly (full information) ⇒ 10/15 cells are structural zeros; `Π_full` minimum is unreachable for real LLM rule families. Reference point: `D(M3,T) = 3H/4` — **may serve only as a sanity check, never as L or U**.

**T-3 (`null-U`)** — mechanism-specific convergence tolerance. Our five-level criteria: explicit transition law `F` with non-empty state `S_t` and parameter domains (U-1); a convergence target plus a finitely-checkable certificate (U-2); a *proven* mapping from regret `D` to the certificate's tolerated perturbation, with direction and tightness (U-3); a value bound to the 5-tuple `(value, certificate ID, state-process ID, perturbation-map ID, cell)` (U-4); identifiability + non-vacuity (U-5).

Internal state: our P-B harness's three mechanisms are **memoryless per decision** (no state process) ⇒ no convergence certificate can refer to anything (our route-甲 verdict: "structurally unsolvable"). Route-乙 (redefine "mechanism" via the deposon field dynamics) and route-丙 (three mechanisms as perturbation source + an existing certificate from a *different* protocol, a 22-graph game) each require a definition-level revision.

- **Ask**: for each of T-2 / T-3 — is the target derivable under our stated constraints? If yes, give the construction and which of our five levels it satisfies; if no, give the obstruction and the *minimal* constraint relaxation that would make it derivable. Please engage our route options (甲/乙/丙) explicitly rather than proposing an unrelated frame.

## §5 Task T3 — independent review of our dual-readout experiment (M-41)

We completed a "strip vs. no-strip" dual-readout experiment (50/60 cells collected). Key results and diagnosed defects, for your independent review:

- Readouts (rejected-decision rate `R`): no-strip global `1/10`; strip-C2 `4/45` (Δ −1/90); strip-C3 `4/35` (Δ +1/70); strip-C1 `1/10` (Δ 0). Base arm `R_base ≡ 0` in all arms.
- Diagnosed defects (verified in code): **(a)** the base arm is an *oracle* — the `value` field encodes the correct key in every family, so the greedy baseline cannot discriminate anything; **(b)** the `T3_Trap` family prompt is *undecidable* ("Trap scenario N (type=cost). Which option?" with contentless labels `['Option A','Option B']`; the model cannot extract the answer — we deliberately did **not** "fix" the prompt, to keep the treatment uncontaminated); **(c)** survivorship confound: all 10 no-action cells fall inside C1/C2, so the strip-C3 arm silently loses those cells from its denominator; |ΔR| ≤ 0.0143, the same order as the confound ⇒ the experiment alone cannot support choosing what/how-many to strip, or one- vs two-sided tests.
- **Ask**: (i) do you concur with the three diagnoses, or do you see a reading we missed? (ii) recommendations on our open items — BL-3 (baseline saturation/oracle fix), BL-4 (making the trap family answerable without contaminating the treatment), BL-5 (running 3 seed-pairs for confidence), and any kill-line you would freeze *before* such a rerun.

## §6 Task T4 — derivation guidance for `u*(a_t)` and `L`/`U` (D1 theory input)

Our G-E01 theory input `u*(a_t)` plus the `L`/`U` pair (T-2/T-3 above) blocks the run sequence.

- **Ask**: a derivation path (or a verdict of underivability) for `u*(a_t)` consistent with the mechanism definitions you see in T3 (full-information M1/M2, uniform-forced M3, memoryless decisions), and how `u*` should interact with the `L`/`U` you assess in T2. If the honest answer is "underivable as stated", please identify the smallest missing definition.

## §7 Deliverable and reply form

1. A structured written reply addressing T1–T4 in order, each ending with a one-line verdict: **derivable (with value/rule) / derivable-with-relaxation (name it) / underivable (obstruction)**.
2. Exact model name/version used, and any tool calls made.
3. Checkable references only; mark anything you could not verify.
4. Proposed deadline: **[PI to fill — 建议一周沿 V3.X 判死节奏，候 PI 定]**.
5. Please do **not** execute, modify, or upload anything on our behalf; analysis only.

With thanks,
**PI** — deposon project
(drafted by the project's main agent at PI's instruction; dispatch only after PI approval)

---
