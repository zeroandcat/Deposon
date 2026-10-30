# Task: Derive and land the theory bound (D1) for P-B distortion V0

You are working inside a local repository. Start by reading the specification:

`docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md`

The spec defines an experiment that measures the distortion `D(M,T)` of an LLM player against a Bayesian baseline, over 3 mechanisms x 5 task families. Two things are still missing and both are your deliverable: the **theory bound** (lower bound `L(M,T)` and upper bound `U(M,T)`), and the **four quantities** that the distortion formula needs.

## 1. What already exists

Distortion formula (spec §3.4):

```
D(M,T) = E_pi[ sum_t |u*(a_t) - u(a_t)| / max_u ]
```

where
- `u*(a_t)` = payoff of the theoretically optimal decision,
- `u(a_t)` = payoff of the actual player's decision,
- `max_u` = payoff upper bound, the per-task-family normalizing constant.

Mechanisms (spec §3.2): `M1` = Deposon T+R+A three-channel; `M2` = pure greedy; `M3` = random baseline.

Task families (spec §3.3): `T1` GSM8K-style, n=20; `T2` StrategyQA-style, n=20; `T3` synthetic trap, n=20; `T4` minimal custom game, n=10 with an explicit Nash equilibrium; `T5` low-resource game, n=20.

Derived metrics (spec §4): main metric is the distortion multiplier `D_LLM(M,T) / max(D_Bayesian(M,T), eps)`; secondary metrics are the lower-bound hit rate, the upper-bound violation rate, and per-task-family / per-mechanism means.

## 2. Frozen kill-lines — DO NOT CHANGE THESE

Spec §1 pre-registers them and they are frozen:
- `H0` (kill): distortion multiplier >= 2.0x
- `H1` (close): distortion multiplier <= 1.5x

Spec §4.3 additionally uses `theory_U_hit_rate >= 0.3` (FAIL_H0) and `<= 0.1` (PASS_H1).

If your derivation implies any of these thresholds is wrong, do **not** adjust it. Write a section titled `KILL-LINE CONFLICT` that states which threshold, why, and what would follow — then continue with the derivation under the frozen thresholds.

## 3. What you must produce

1. **A closed-form or computable definition of `L(M,T)`** — the lowest possible distortion under an LLM information bottleneck, motivated from information capacity plus mechanism identifiability. Give the argument, list every assumption, and say what empirical quantity each symbol maps to.
2. **A closed-form or computable definition of `U(M,T)`** — the highest distortion the mechanism can tolerate, motivated from mechanism convergence conditions. Same requirements.
3. **The four quantities for every cell.** There are 15 cells (3 mechanisms x 5 task families). For each cell give `u*(a_t)`, `L`, `U`, `max_u`. Note that `u*(a_t)` is generally a **rule** rather than a single number, because it depends on the realized task instance — state the rule, and state how it reduces to a number for a given instance.
4. **A landing** in code: something that computes `L`, `U`, `u*`, `max_u` and the distortion multiplier, fitting the existing calculator's interface.

## 4. Hard constraints

**4.1 Do not modify the anchored file in place.**
Spec §2 registers `P_B_DISTORTION_CALC` as the SHA-256 of `tools/distortion_calculator.py` (currently `ae7ff6e0bac5`, 50,896 bytes), and spec §2 also states: *any anchor drift => the whole V0 is retracted*. Therefore:

- Do **not** edit `tools/distortion_calculator.py` in place.
- Write your implementation as a **new sibling module** (e.g. `tools/distortion_bound_d1.py`).
- Provide the integration as a **proposed patch shown in your report**, not applied. Applying it is a separate decision that belongs to the project owner, because it would drift the anchor.

**4.2 Do not invent citations.**
If a bound rests on a named theorem, name it only if you can state it correctly **and** it is standard. Otherwise derive it yourself and label it `DERIVED HERE (no external citation)`.

**4.3 Tag every quantity with exactly one status.**

- `DERIVED` — you derived it here, and the derivation is in your report.
- `CITED` — a standard named result; give its name and its conditions of applicability.
- `NOT_DERIVABLE` — the specification is insufficient. Say **exactly** what is missing and what would unblock it.

Never fill a gap with a plausible number. A cell whose constants are `NOT_DERIVABLE` is an acceptable outcome; a cell with a guessed number is not.

**4.4 No floating-point hedging.**
Where an inequality decides a kill, state it so it can be evaluated exactly.

**4.5 All output in English.**

## 5. Deliverables — write exactly these

1. `docs/V3X/P_B_V0_D1_THEORY_BOUND.md`
   - The derivation of `L` and `U`; the rule for `u*(a_t)`; the definition of `max_u`.
   - Every assumption, stated explicitly.
   - A per-cell table of the four quantities for all 15 cells, each with a status tag.
   - A section `WHAT I COULD NOT DERIVE` listing every `NOT_DERIVABLE` item and what would unblock it.
   - A section `KILL-LINE CONFLICT` (may be empty).
   - A section `ANCHOR NOTE` restating that the anchored file was not modified, with its measured byte size and SHA-256 prefix.

2. `docs/V3X/P_B_V0_D1_CONSTANTS.json`
   Machine-readable. One entry per (mechanism, task family) cell, containing the four quantities and their status tags.

3. `tools/distortion_bound_d1.py`
   The implementation, as a new module. Expose at minimum a function with this shape:

   ```python
   def distortion(mechanism: str, task_family: str, records: list[dict]) -> float: ...
   def theory_bounds(mechanism: str, task_family: str) -> tuple[float, float]: ...
   ```

   Read `tools/distortion_calculator.py` first so your module fits its conventions (naming, units, error handling). If its interface conflicts with what the spec requires, **report the conflict** rather than silently diverging.

## 6. Self-check before you report

Answer each of these explicitly in your final message:

- Do all 15 cells have all four quantities present and status-tagged?
- Is every `CITED` item named, with its conditions of applicability?
- Is there any number without a derivation path? If so, it belongs in `NOT_DERIVABLE` — move it.
- Does `tools/distortion_bound_d1.py` import cleanly, and does it return a finite value on a synthetic input of 3 records?
- Was `tools/distortion_calculator.py` left byte-identical? Report its measured size and SHA-256 prefix to prove it.

## 7. Report format

Finish with a short report containing, in this order:

1. What you produced (three paths, with byte sizes).
2. The derivation of `L` and `U` in one paragraph each.
3. The count of cells by status: how many fully `DERIVED`, how many contain a `CITED` component, how many contain any `NOT_DERIVABLE` item.
4. `WHAT I COULD NOT DERIVE` — summarized.
5. `KILL-LINE CONFLICT` — empty or itemized.
6. The proposed patch to `tools/distortion_calculator.py`, shown as a diff and **not applied**.
7. The measured byte size and SHA-256 prefix of `tools/distortion_calculator.py`, to prove it was untouched.

Be concise. Correctness and explicit gaps are worth more than completeness here.
