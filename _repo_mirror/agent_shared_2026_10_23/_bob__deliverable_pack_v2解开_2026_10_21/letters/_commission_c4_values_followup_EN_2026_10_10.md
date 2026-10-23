# Commission (follow-up) — C4 inputs for the P-B V0 distortion bound · second solicitation

> **Status**: draft · prepared by the main agent (parent session) on 2026-10-10, for PI review and release decision (addressee to be designated by the PI).
> **Lineage**: follows the first commission `letters/_commission_c4_values_EN_2026_10_10.md` (SHA-12 `a397621085d6`, 56,217 B) and the two replies recorded for it — `letters/_codex_theory_derivation_reply_2026_09_30.md` (`7558eb1a5e34`: construction rule derivable / values not derivable) and `letters/_codex_c4_values_reply_2026_10_10.md` (`8e4972352291`, 13,378 B: formal non-availability — `null` for all 15 cells and all 5 family slots, with per-item blockers).
> **Purpose of this follow-up**: the recorded replies established **what is missing and what would make the values obtainable**. This solicitation puts that sharpened specification to a second-wave source.
> **Contains no reply outline** (per PI ruling of 2026-09-24: commissioning materials do not pre-structure the addressee's reply). Structure, level of detail, derivation path and style are for the addressee to decide.
> **Hard boundary**: this document commissions *inputs*, not a verdict. It modifies no repository document; it adjudicates nothing; nothing in it is adopted until the PI so rules.

---

## §0 What this commission asks (one paragraph)

Supply — or stand as the authorizing source for — the four C4 inputs of the P-B V0 distortion bound: `u*(a_t)` (T-1), `L(M,T)` (T-2), `U(M,T)` (T-3), `max_u(T)` (T-4), **as sourced values with source attribution and applicability**. The previously recorded boundary ("construction rule derivable / values not derivable") stands only until a source supplies the missing definitions listed in §2. If you cannot supply or authorize any part of these as a source, a **formal non-availability answer with reasons is an accepted reply form** (§1b).

## §1 The two accepted reply forms

**(a) Values** — per-cell / per-family values, each with a **source attribution** (who gave it / where it comes from) and an **applicability declaration**:
- T-1 / T-2 / T-3: cell by cell across **5 task families (T1–T5) × 3 mechanisms (M1–M3) = 15 cells**;
- T-4: family by family (5 family-indexed entries).

**(b) Non-availability** — an explicit statement that no computable, sourced value exists in the material, naming: which of the four inputs is blocked; why; and what would unblock it. (This was the accepted form of the prior reply.)

⛔ Harness rule carried from the first commission and the frozen pre-registration: absent definitions may not be replaced by estimates, substitutes, or self-authored formulas (C4.9 zeroing discipline).

## §2 What the prior replies recorded as missing (do not re-derive the gap)

1. **T-1 · `u*(a_t)`** — no payoff function `u`, its scale, units/range, or per-family value on disk; M1 additionally lacks mechanism-internal parameterization for any value depending on it.
2. **T-2 · `L(M,T)`** — the named bases (**IC capacity**, **mechanism identifiability**) have no on-disk definitions, expressions, criteria, or values.
3. **T-3 · `U(M,T)`** — the named basis (**mechanism convergence condition**) is named but not defined; there is no value-producing map to a numeric `U`.
4. **T-4 · `max_u(T)`** — defined only as a payoff upper bound normalized by task family; with the payoff scale absent, no family-specific bound is computable.

**⇒ To unblock:** an **authorized source** must (i) define `u` for the task outcomes — including payoff scale, units/range, and applicability across all 15 cells; (ii) supply sourced definitions and cell applicability for both `IC capacity` and mechanism identifiability; (iii) supply a convergence condition together with its mapping to a numeric `U` and its cell applicability; (iv) supply the five family-indexed `max_u` values on the same specified payoff scale, with the source attached per family. These are **missing inputs** — not formulas for the addressee to invent — unless the addressee itself is willing to stand as the authorizing source for some part, in which case the attribution must say so.

## §3 What is already delivered (do not re-derive)

- **Construction rule + 15-cell coverage** for T-1; **T-4 caliber + five family slots**; **source attributions** — as recorded in the prior replies (`7558eb1a5e34`; carried forward and re-cited in `8e4972352291`).
- **Canonical source declaration** (theory-side source = a named-party derivation; the original "GLM derivation" wording is historical and unmodified; 0 self-authored / 0 self-invented formulas; crackable source attribution with giver/venue) — as recorded in the C4 correction register `61b139efd0ef`.

## §4 Two qualifications carried from the prior reply (so they are not mis-read)

1. **`U` is necessary but not sufficient**: other missing inputs (`ε`; M1 internal parameters) lie outside these four asks; even all four values would not by themselves make the kill-line landable. "U removes the U-dependent blocker" — not "U closes the line".
2. **"Five numbers, not one universal constant"** concerns *family indexing and attribution*: the spec calls `max_u` a task-family normalization constant and requires five family entries; it does not state that the five numerical values must differ.

## §5 What this document does NOT contain / do

- No reply outline; no pre-filled value; no formula; no verdict; no adjudication.
- It makes no claim about whether, when, or by whom the first commission was released; addressing and release belong to the PI, and the first commission's own on-disk record remains as-is (unmodified).

## §6 Material references (for the addressee; all in the local repository)

| # | Item | Path | SHA-12 | Bytes |
|---|---|---|---|---|
| 1 | P-B V0 spec | `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | `423c84de20d5` | — |
| 2 | First commission (v0.2-style, 367 lines) | `letters/_commission_c4_values_EN_2026_10_10.md` | `a397621085d6` | 56,217 |
| 3 | Second reply — formal non-availability | `letters/_codex_c4_values_reply_2026_10_10.md` | `8e4972352291` | 13,378 |
| 4 | First reply — construction rule / values boundary | `letters/_codex_theory_derivation_reply_2026_09_30.md` | `7558eb1a5e34` | — |
| 5 | C4 correction register (canonical declaration) | `results/_c4_theory_source_caliber_correction_2026_09_30.md` | `61b139efd0ef` | — |
| 6 | Frozen zeroing rule (pre-registration) | `results/_v5_item21_rerun_conditions_prereg_2026_09_28.md` | `4185bdad6df5` | — |
| 7 | Bayesian-baseline design (same payoff for both arms; construction left to PI) | `results/_bayesian_baseline_design_2026_10_10.md` | `7e181a167702` | — |

## §7 Delivery-format & attribution requirements (carried)

- Every value or definition supplied must carry **giver/venue** and **applicability** (per-cell for T-1–T-3; per-family for T-4).
- **Partial answers are acceptable**: if part of the four can be supplied and part cannot, mark each part separately; partial replies will be registered as such.
- No need to re-derive anything listed in §3; no requirement to accept prior conclusions. Your reply is your own.

## §8 Boundary

This draft: modifies no repository document; makes no adjudication for the PI or the verdict-keeper; changes no threshold; is not adopted automatically; supplies no value, formula, outline, or verdict. Its addressee and release decision remain with the PI. Fingerprint (SHA-256 / SHA-12 / byte count) is reported with delivery, outside this file.
