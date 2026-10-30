# T5 Input Package B — Blind Independent Grounding (Honest Partial)

Date: 2026-10-24
Commissioned-party handle: K31B
Scope: B-O (numeric action occupancy) and B-F (constraint operator, initial state, combination rule, and separate step-limit binding).

## 0 Delivery status

B-F is delivered as an executable rule family with a named initial-state reading. B-O is not numerically obtained: the supplied files do not include the per-cell action-label/semantic payload or the calibration-cell body needed to measure 80 occupancies. The occupancy CSV therefore contains only its schema; the grounding-basis CSV names every one of the 80 missing cell-action quantities. No binary indicator is substituted for occupancy and no payoff-derived scale is used.

## B-1 Occupancy and unit calibration

### B-1.1 What a unit means

The following are unit definitions, not occupancy measurements:

- `unit` (scenario resource quantum): one indivisible quantum of the resource named by that cell. Its physical identity and conversion to any external measurement are not supplied. It is not commensurable with a quantum from another scenario.
- `hour`: exactly 3600 seconds when used as a duration. NIST Guide to the SI, Appendix B.9, Time, https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b9, retrieved 2026-10-24T16:22:04.154+08:00.
- `day`: exactly 86400 seconds when used as a duration; this is not a claim about a calendar date or a sidereal day. Same NIST source and retrieval timestamp.
- `round`: one complete decision cycle in the scenario. The cycle's start/end and any duration conversion require the scenario definition; neither is supplied, so no seconds conversion is made.
- `step`: one atomic action selection in the model. This is a model-count unit, not a physical-time unit. The separate step limit is not merged with resource occupancy.

These definitions calibrate dimensions only. They cannot manufacture an action's numerical resource consumption.

### B-1.2 Required future measurement recipe

For each cell-action pair, an admissible future occupancy row must record: the action's semantic resource feature; an independently measured or citable source quantity; the raw unit; the exact conversion to the cell unit; source locator and retrieval timestamp. Values must not be derived from payoff, payoff order, action position, or a desired feasible set. If those inputs are absent, the result is a named gap, not a number.

The 80 gap identifiers are `G-BO-t_XX-a_Y`, for `XX=01..20` and `Y=1..4`. Each is individually present in `..._grounding_basis.csv`. A2-7/A2-9 statistics are not computed on an empty numeric field and are not reported as zero.

## B-2 Occupancy to Feas, with B-F initial state

### B-2.1 Named reading of “initial value”

The adopted reading is **operator initial state first, with combination-rule initialisation as a companion**. It is not a claim that real-world initial quantities have been independently measured. The basis is that the task asks for an executable constraint operator and its binding to a separate step limit; the starting point must therefore be defined before any action is taken.

For each cell, `k=0` means immediately before the first action:

```text
B_t = 3                         # model aggregate parameter, transcribed from supplied D-02 §6-2
H_t = 3 steps                   # model step limit from the same supplied material
r_t_0 = B_t                     # remaining resource at the start
h_t_0 = H_t                     # remaining steps at the start
n_t_0 = 0 actions               # no action has occurred; definitional, not zero-fill
```

The per-cell physical/resource unit of `B_t` and `r_t_0` is `NOT_IN_RANGE`, because the actual budget-digest body was not supplied. The numeric 3 is not independently measured and is not offered as a real-world initial quantity; it is a model parameter from the supplied document. If the commission requires even model parameters to have independent measurement, then `G-BF-BUDGET-ALL` applies and the numerical part of B-F does not hold.

All 20 initial-state rows are in `..._constraint_initialization.csv`, with sources and retrieval timestamp.

### B-2.2 Exact executable predicate

```text
function FEAS(t, k, occupancy_table):
    if occupancy_table[t] is missing or unit_of(B_t) is NOT_IN_RANGE:
        return UNOBTAINED              # not the empty set
    require unit_of(occupancy_t) == unit_of(r_t_k) == unit_of(B_t)
    return { a in options_t : occupancy_t[a] <= r_t_k and h_t_k >= 1 }

function UPDATE(t, k, selected_action):
    require selected_action in FEAS(t, k, occupancy_table)
    r_t_(k+1) = r_t_k - occupancy_t[selected_action]
    h_t_(k+1) = h_t_k - 1
    n_t_(k+1) = n_t_k + 1
    return (r_t_(k+1), h_t_(k+1), n_t_(k+1))
```

The resource cap and the step limit are separate dimensions. Resource arithmetic is forbidden across unlike units. If the predicate is `UNOBTAINED`, no feasible-set cardinality, nonempty-key result, narrowing count, or maximizer is produced.

Structural sources for capacity/load reasoning: Tampubolon, Ceribasic, and Boche, https://arxiv.org/abs/2002.06080; Rasulkhani and Chow, https://arxiv.org/abs/1711.11230 (DOI `10.1016/j.trb.2019.04.008`), both retrieved 2026-10-24T16:22:04.154+08:00. They support the rule form, not any T5 weight.

### B-2.3 Action combination rule

The adopted model is atomic selection: exactly one action is selected at a decision point; a multi-action bundle within one cell is not introduced. Across a sequence `(a_1,...,a_m)`, resource use is additive and the step count is the sequence length:

```text
sequence_feasible((a_1,...,a_m), B_t, H_t) iff
    every prefix satisfies FEAS at its own k
    and sum_{k=1..m} occupancy_t[a_k] <= B_t
    and m <= H_t
```

The prefix condition prevents a sequence from using later resources earlier. Atomic resource selection is structurally consistent with Zeiler, https://arxiv.org/abs/2505.06390, retrieved 2026-10-24T16:22:04.154+08:00. This citation supports the atomic model form only.

## Named gaps and non-results

- `G-BO-t_XX-a_Y` (`XX=01..20`, `Y=1..4`): 80 numeric occupancies and their semantic/material bases are not obtained; affects A2-1, A2-2, A2-3, A2-4, A2-5, A2-7, A2-8, A2-9, and the requesting-side A2-6 computation.
- `G-BF-UNIT-t_XX` (`XX=01..20`): each cell's actual resource unit is not obtained; arithmetic must stop at the named gap.
- `G-FEAS-t_XX` (`XX=01..20`): no feasible-set membership or cardinality is obtained because its required occupancy input is missing. This is not an empty feasible set.
- `G-CALIBRATION-CELL-BODY`: the calibration cell was described in the round-2 manifest but its body was not supplied, so no granularity anchor was available.
- `G-BF-BUDGET-ALL`: conditional on a reading that requires independent measurement even for the model budget parameter, the transcribed `B_t=3` does not meet that stronger requirement.

A2-6 is **not certifiable by the commissioned party under 3A — verification reserved to the requesting side**. The occupancy table needed for its feasible maximizers is not obtained; this reservation is not a substitute for the missing outputs.

## Reproduction

Read `..._feasibility_rule.csv` together with `..._constraint_initialization.csv`. Initialise at `k=0`, then iterate FEAS and UPDATE only after all required occupancy and unit inputs are numeric and dimensionally compatible. For any missing input, stop at the named gap and return `UNOBTAINED`; never interpret that result as an empty feasible set, a zero violation, or a valid argmax. No experiment or model/API call was run for this delivery.
