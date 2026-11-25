# Reply to the Outbound Commission for the Five η-Construction Values

**Status:** Independent candidate proposal for PI review only. Delivery is not adoption. This reply does not rule on the η mode, alter any registered wording or threshold, run an experiment, or take any action in the deposon repository.

## 1. Proposed candidate set

The proposals below are conditional on the construction using the independent-parameter mode `ET-I`. They are one jointly chosen set, not five independently optimized numbers.

| Requested tier | Candidate | Domain and distinctness check | Short rationale |
| :-- | --: | :-- | :-- |
| `η-2` | `0.25` | In `[0,1]`, below `0.5`, and distinct from the other proposed η values | An interior lower-than-default direction tier; not a value inferred from the cited low-exploration study. |
| `η-3` | `0.75` | In `[0,1]`; distinct from `0.5`, `0.25`, and `0.90` | An interior upper-side comparison point, separated from the default and the other proposed tiers. |
| `η-4` | `0.90` | In `[0,1]`; distinct from `0.5`, `0.25`, and `0.75` | A high, but non-endpoint, comparison point. |
| `GC-4` | `0.50` | Nonnegative and distinct from `1.0`, `2.0`, and `0.2` | A positive interior value distinct from the listed default and boundary literals. |
| `GA-4` | `0.50` | Nonnegative and distinct from `0.1`, `0`, and `2.0` | A positive uniform-floor candidate, avoiding the zero-floor condition of `GA-2`. |

These numbers are **engineering-design candidates only**. Their spacing is intended to provide distinct interior comparison points while avoiding the listed endpoints and anchors. The spacing is not calibrated from measured outcomes, literature effect sizes, or a parameter-sensitivity study. The values of `g_couple` and `g_aether` retain their respective construction roles; their numerical equality here does not assert that their meanings or effects are interchangeable.

If the PI selects `ET-D1` or `ET-D2` instead of `ET-I`, `η-2` / `η-3` / `η-4` would not be independent input values. This reply does not choose among those modes.

## 2. Joint tier set and construction check

Using the tier assignments in the commission, the resulting proposed triples are:

| Tier | `η` | `g_couple` | `g_aether` |
| :-- | --: | --: | --: |
| `ETAC-D1` | `0.50` | `1.0` | `0.1` |
| `ETAC-D2` | `0.25` | `2.0` | `0` |
| `ETAC-D3` | `0.75` | `0.2` | `2.0` |
| `ETAC-D4` | `0.90` | `0.50` | `0.50` |

On the per-parameter counting caliber requested by the commission:

- η-axis values are `{0.50, 0.25, 0.75, 0.90}`: four distinct values.
- `g_couple` values are `{1.0, 2.0, 0.2, 0.50}`: four distinct values.
- `g_aether` values are `{0.1, 0, 2.0, 0.50}`: four distinct values.
- Each listed value is in its stated domain, and each triple is distinct from the other triples.

For the supplied construction

```text
w(o) = (1 - η) · 1{v(o) = best} + η · g_couple · (v(o) / best) + g_aether
P(o) = w(o) / Σ_o w(o)     if the sum is positive
```

the four proposed best-option weights, assuming `best > 0` and `v(best) = best`, are respectively `1.10`, `1.25`, `2.40`, and `1.05`. For any cell with `0 ≤ v(o) ≤ best` and `best > 0`, all terms are nonnegative. The best-option weight is positive for each proposed triple, so `Σ_o w(o) > 0` for any nonempty option set containing a best option. Thus the formula is valid under those stated payoff conditions.

This is an algebraic, conditional check, **not a cell-by-cell certification**: the commission does not provide the payoff arrays or all cell inputs. In particular, where `best = 0`, `v(o)/best` is undefined. The commission describes the harness behavior for the excluded `T4_2x2#04` cell, but does not provide enough evidence here to certify handling in every other applicable cell. No alternative zero-best behavior is proposed; the relevant registered construction and cell scope must govern.

## 3. Degeneracy disclosure

The proposed constants do not by themselves establish whether any actual cell produces an indicator-only, one-hot, or otherwise idle/degenerate distribution; that depends on its payoff values and cell-specific handling.

One data-dependent risk is explicit for `ETAC-D2`: because its uniform floor is `g_aether = 0`, every non-best option with `v(o) = 0` has weight zero. If all non-best options in a cell have zero payoff, this triple yields a one-hot distribution on the best option. I cannot determine from the supplied commission whether that condition occurs in any eligible cell. The positive floors in the other three listed triples prevent zero weights for cells where their formula applies, but do not rule out uniform or otherwise non-discriminating distributions for particular payoff arrays.

No distribution-shape conclusion, measured reading, or experiment result is claimed.

## 4. Evidential face for each proposed value

No external publication is used to derive any of the five numerical candidates. The commission itself expressly warns against transferring numerical values from the cited studies across task families. The candidates are transparent design choices constrained by that commission, not literature-backed estimates.

| Tier and candidate | Source identifier and time point | Authority level | Quoted face | Relation and scope |
| :-- | :-- | :-- | :-- | :-- |
| `η-2 = 0.25` | Commission supplied by the PI: `〔本地路径已脱敏〕`, §2 Item-1; dated 2026-10-20. | The commission is the source of the constraint, not an external authority grading for the proposed number. The numerical choice is an ungraded design proposal. | “`η < 0.5`”; “`η ≤ 1`”; “`η ≥ 0`” | The constraints support the domain and direction only; they do not entail `0.25`. The number is a proposed interior point, not an extrapolation from L2. |
| `η-3 = 0.75` | Same commission, §2 Item-1; dated 2026-10-20. | Same: constraint source only; proposed number ungraded. | “`0 ≤ η ≤ 1`”; “must be distinct from `η-1`＝`0.5`, `η-2`, `η-4`” | The constraints support the domain and distinctness only; they do not entail `0.75`. The number is a proposed upper-side interior comparison point. |
| `η-4 = 0.90` | Same commission, §2 Item-1; dated 2026-10-20. | Same: constraint source only; proposed number ungraded. | “`0 ≤ η ≤ 1`”; “must be distinct from `η-1`＝`0.5`, `η-2`, `η-3`” | The constraints support the domain and distinctness only; they do not entail `0.90`. The number is a proposed high interior comparison point. |
| `GC-4 = 0.50` | Same commission, §2 Item-1; dated 2026-10-20. | Same: constraint source only; proposed number ungraded. | “`g_couple ≥ 0`”; “must be distinct from `GC-1`＝`1.0`, `GC-2`＝`2.0`, `GC-3`＝`0.2`” | The constraints support nonnegativity and distinctness only; they do not entail `0.50`. The number is a proposed positive interior point. |
| `GA-4 = 0.50` | Same commission, §2 Item-1; dated 2026-10-20. | Same: constraint source only; proposed number ungraded. | “`g_aether ≥ 0`”; “must be distinct from `GA-1`＝`0.1`, `GA-2`＝`0`, `GA-3`＝`2.0`” | The constraints support nonnegativity and distinctness only; they do not entail `0.50`. The positive value is intended to avoid a zero uniform floor in this proposed tier, not to claim an empirically optimal floor. |

The source path above is transcribed from the commission. I have not independently opened the underlying repository or verified its cited registry documents. The six literature entries reproduced in the commission are not treated as independent verification, nor as grounds for these numerical values. No external references were searched or verified for this reply, and no external numerical evidence is relied upon or claimed.

## 5. Self-certification summary

| Item | Result |
| :-- | :-- |
| Domain compliance | **Yes**, for the proposed values and stated domains. |
| Per-axis distinctness | **Yes**, relative to all three other values on each axis, using the commission's per-parameter caliber. |
| Construction validity | **Conditional algebraic check only** for nonnegative payoffs with `best > 0`; see §2. **Not cell-by-cell certified** because the payoff arrays and complete cell-specific zero-best behavior were not supplied. |
| Degeneracy disclosure | **Data-dependent and unresolved**. `ETAC-D2` can be one-hot where all non-best payoffs are zero; other cell-specific distribution shapes cannot be assessed without the data. |

## 6. Limitations and boundaries

- These are proposed candidate values, not adopted values or a ruling on the PI's behalf.
- The three η values depend on the PI selecting `ET-I`; if a derived η mode is selected, this three-value proposal is inapplicable.
- No external numerical evidence is relied upon or claimed. Literature mentioned in the commission is not being used to infer a value.
- No experiment, pre-experiment reading, criterion calculation, or repository change was performed.
- The frozen kill-lines, thresholds, registered wording, and existing conclusions are not changed by this reply.
- The design rationale may be inadequate if the intended payoff scale or expected sensitivity differs from the assumptions stated above. The candidate set should be assessed against the actual cell data and the already-frozen selection procedure before any adoption.

## 7. Model and tools

- **Agent name / nominal layer:** Copilot assistant in VS Code.
- **Exact model name and version:** Not exposed to this session; not inferred.
- **Serving endpoint:** Not exposed.
- **Tools used:** Workspace file-reading tool (`view`) to read the supplied commission; file-editing tool (`apply_patch`) to create this reply in the separate current workspace; local PowerShell for the reply's delivery fingerprint.
- **External browsing, experiments, and repository writes:** None.

## 8. Delivery boundary

This reply is a written candidate derivation only. It does not choose a commissioned party, establish a deadline or channel, upload or forward anything, or perform any action on the deposon project or its repository.
