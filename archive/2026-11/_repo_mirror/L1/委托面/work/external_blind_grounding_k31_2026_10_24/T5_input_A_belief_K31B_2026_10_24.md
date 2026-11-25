# T5 Input Package A — Blind Independent Grounding (Honest Partial)

Date: 2026-10-24
Commissioned-party handle: K31B
Scope: A-V (counterfactual kernel), with the state-space, prior/likelihood, and per-cell coverage faces needed to interpret it.

## 0 Delivery status and blind boundary

This is an honest partial delivery, not a numerical counterfactual kernel.

The eight supplied files were read and fingerprinted. The round-2 desensitized attachment itself was not among them: only its manifest and section descriptions were supplied. Consequently, no per-cell action-label table, calibration-cell body, or authoritative cell-to-scenario table was available to this lane. This statement is scoped to the eight supplied files; it is not a claim about what exists elsewhere.

No reference key or realised payoff was received or sought. No hash, rank, aggregate statistic, recorded action order, or positional proxy for them was used. No value was tuned against a key or against an inferred key.

`NOT_IN_RANGE` in the CSVs is a non-numeric domain/gap marker. It is never zero, a mean, a median, a default, an imputed value, or an obtained measurement. `UNOBTAINED` is not an empty set and is not a zero-violation result.

## A-1 State space S

No grounded finite state space can be enumerated from the supplied material. `..._states.csv` therefore contains its schema and no fabricated state rows. Gap `G-AS-ALL` affects A1-1 and every downstream expectation.

A usable future state table must provide, for every state, an individual identifier, world-state semantics, and provenance. It must also provide the observation-to-state coverage rule for each cell. A generic state invented merely to make a posterior defined would not satisfy that requirement.

The formal coverage requirement, delivered as a rule rather than as a fabricated state set, is:

```text
S_t = { s in S : coverage_rule(obs_t, s) = true }
require S_t finite and S_t subset_of S
require posterior_support_t subset_of S_t
```

Public structural source: Poupart and Boutilier, *Value-Directed Belief State Approximation for POMDPs*, https://arxiv.org/abs/1301.3887, retrieved 2026-10-24T16:22:04.154+08:00. This source supports the belief-state formalism; it supplies no T5 state identity or numeric value.

## A-2 Counterfactual payoff kernel v(s,a)

`..._counterfactual_payoff.csv` contains 80 explicit records, one for every `t_01 ... t_20` by `a_1 ... a_4` pair. Every record has `state_id = NOT_IN_RANGE`, `v_value = NOT_IN_RANGE`, and a named handling rule. The state identifier is not fabricated merely to complete the tuple.

The exact handling rule for every record is:

```text
if state identity or payoff semantics/unit is unavailable:
    mark the pair NOT_IN_RANGE
    do not include the pair in an integral
    do not replace it by zero or by any imputation
    mark E_t(a) UNOBTAINED; never drop the pair and renormalize
```

Thus the delivery does not claim A1-3 or A1-4. The records name the undefined domain; they do not constitute 80 numerical payoffs.

If the missing grounded inputs are later supplied, the only computation to perform is:

```text
E_t(a) = sum_{s in S_t} posterior_t(s) * v_t(s,a)
K_t = { a in options_t : E_t(a) = max_{b in options_t} E_t(b) }
```

This formula is not executed here because its required numeric inputs are absent. No per-cell argmax list is guessed.

## A-3 Prior and likelihood

No numeric point prior, ambiguity moments, likelihood, or posterior is obtained. The prior and likelihood CSVs contain one named gap record per cell; they do not contain probability values.

The reserved normalisation tolerance is `1e-9`, taken from the acceptance criterion. It is a parameter for any future valid posterior, not a claim that a posterior currently sums to one. `cell_posterior_sum = NOT_IN_RANGE` throughout.

For a future complete input, the recomputation rule is:

```text
unnormalised_t(s) = prior_t(s) * likelihood_t(obs_t | s)
Z_t = sum_{s in S_t} unnormalised_t(s)
if Z_t <= 0 or any required input is missing:
    posterior_t = UNOBTAINED
else:
    posterior_t(s) = unnormalised_t(s) / Z_t
    require abs(sum_s posterior_t(s) - 1) <= 1e-9
```

Structural sources: https://arxiv.org/abs/1301.3887 and https://arxiv.org/abs/1906.05988, both retrieved 2026-10-24T16:22:04.154+08:00. The latter supports ambiguity-set reasoning only when a model family and its moment constraints are known; those inputs are not supplied here.

Attribution disclaimer: the requesting side did not author the commissioned party's belief construction. Equally, this delivery does not claim that a usable belief has been authored by anyone. The exact provenance rows and the blind attestation are in `..._provenance.csv`.

## A-4 Per-cell observation coverage

All 20 cells are named in `..._likelihood_posterior.csv`; none has a fabricated live-state support. The current coverage result for every cell is `UNOBTAINED`, because the observation features and state-coverage rule are missing. This is not 20 empty supports and not 20 zero-violation results.

`..._cell_grouping.csv` preserves the limited pairing evidence that is present in supplied D-02: `(t_01,t_18)`, `(t_02,t_19)`, and `(t_03,t_20)` are known to share scenario material. The actual scenario identifiers and the remaining authoritative mapping are not supplied, so `scenario_group_id` remains `NOT_IN_RANGE`; no new grouping identity is invented.

The registered run metadata are stated without choosing between the two H readings:

- cells: `t_01 ... t_20`; seeds: `42`, `123`, `456`;
- reading H_design: the design domain has 20 cells;
- reading H_unachieved: T5 has no achieved H value;
- both readings remain on file and no conclusion is drawn from either one alone.

## Reproduction and gap map

The full source list and retrieval timestamps are in `..._provenance.csv`. The algorithm to reproduce a future completed construction is exactly A-3 followed by A-2. Before computing, verify that every required pair is numeric and that the cell's unit is declared; otherwise stop at the named gap and do not emit an expectation or argmax.

Named gaps, with compact but exact expansion rules:

- `G-AS-ALL`: no grounded state elements; affects A1-1, A1-2, A1-3, A1-4, A1-5, A1-7, A1-8.
- `G-AV-t_XX-a_Y`, for `XX=01..20` and `Y=1..4`: 80 undefined counterfactual records; each lacks state identity, action-state payoff semantics, and unit. The individual rows are in the counterfactual CSV.
- `G-AP-t_XX`, for `XX=01..20`: no prior, observation model, likelihood, posterior, or normalised sum; affects A1-2 and A1-4.
- `G-PAIR-t_XX`, for `XX=01..20`: authoritative scenario mapping missing; the three known shared pairs above are preserved but do not complete the mapping; affects A1-10.

No criterion depending on these gaps is reported as satisfied. In particular, A1-6 is **not certifiable by the commissioned party under 3A — verification reserved to the requesting side**; the per-cell maximizer inputs and argmax list are not obtained, so this reservation is not presented as a substitute for them.
