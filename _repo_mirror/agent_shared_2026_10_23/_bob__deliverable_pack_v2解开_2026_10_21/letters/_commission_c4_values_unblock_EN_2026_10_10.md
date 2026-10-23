# Commission (unblock resolution) — C4 inputs for the P-B V0 distortion bound · third transmission

> **Status**: draft · prepared by the main agent (parent session) on 2026-10-10 at the PI's direction, for PI review and release decision (addressee to be designated by the PI).
> **Lineage (C4-values solicitation)**: first commission `letters/_commission_c4_values_EN_2026_10_10.md` (`a397621085d6`, 56,217 B); first reply `letters/_codex_theory_derivation_reply_2026_09_30.md` (`7558eb1a5e34`); second reply `letters/_codex_c4_values_reply_2026_10_10.md` (`8e4972352291`, 13,378 B — formal non-availability, `null` for all 15 cells and all 5 family slots, with per-item blockers); follow-up commission `letters/_commission_c4_values_followup_EN_2026_10_10.md` (`abe0652ab00f`, 7,583 B); follow-up reply `letters/_codex_c4_values_followup_reply_2026_10_10.md` (`97a35f8ae94c`, 4,490 B — supplies no new values; records that the open questions at the C4 correction register §4-a need rulings before that answer can change).
> **Purpose of this transmission**: to resolve those open questions (the unblock requirements) and thereby clear the way for the four C4 inputs. This document (i) authorizes origination of the missing content; (ii) specifies the derivation-chain evidence requirements; (iii) answers whether C4.9 applies ahead of the missing content; (iv) re-solicits the four inputs as sourced values.
> **Contains no reply outline** (per PI ruling of 2026-09-24: commissioning materials do not pre-structure the addressee's reply). Structure, level of detail and style remain for the addressee to decide; the requirements below are delivery-format and evidence requirements only.
> **Hard boundary**: this document commissions *inputs*, not a verdict. It modifies no repository document; it adjudicates nothing; nothing in it is adopted until the PI so rules. All cited rules (including C4.9) are cited as recorded, not altered.

---

## §0 What this transmission does (one paragraph)

The three open questions recorded at the C4 correction register (`61b139efd0ef` §4-a) — (i) the boundary between an admissible derivation and self-drafted/substitute content, (ii) the derivation-chain evidence requirements, and (iii) whether C4.9 applies before the missing content is supplied — are resolved below as they pertain to this solicitation (§1–§3). On that basis the four C4 inputs of the P-B V0 distortion bound are re-solicited as sourced values: `u*(a_t)` (T-1), `L(M,T)` (T-2), `U(M,T)` (T-3), `max_u(T)` (T-4). Each item may be **supplied** from an identified source, or the addressee may **stand as the authorizing source** and **originate** it, subject to §2. Partial answers remain acceptable (§2.5, §7).

## §1 Origination authorization (open question ①)

1.1 The addressee is **authorized to originate** the missing content for the four inputs — that is, to define and supply, as the source, the items recorded as missing in the follow-up commission §2: the payoff function `u` for the task outcomes (including payoff scale, units/range, and its applicability across all 15 cells); sourced definitions and cell applicability for both IC capacity and mechanism identifiability; a mechanism convergence condition together with its mapping to a numeric `U` and its cell applicability; and the five family-indexed `max_u` values on the same specified payoff scale.

1.2 Where an item comes from another source, name the giver/venue. Where the addressee originates it, the attribution must say so (e.g., "originated by the addressee under this commission"). Content originated under this authorization stands as **source content** for these inputs — it is not a substitute or an unsourced filler.

1.3 This authorization concerns the four inputs above. It changes no pre-registered rule, no threshold, and no wording (C4.9 included); it settles, for this solicitation, the standing of content originated under it.

## §2 Derivation-chain evidence requirements (open question ②)

Every item supplied or originated under this transmission must carry the following evidence bundle at delivery:

2.1 **Source attribution** — giver/venue per §1.2; where the addressee stands as source, use the canonical source-declaration form as recorded at `61b139efd0ef` §2.3/§6.2 (theory-side source declaration with giver/venue; the historical wording there remains unmodified). No un-attributed content.

2.2 **Derivation chain** — basis (the inputs, definitions and prior results relied on), assumptions (stated explicitly), and derivation steps, at a level of detail that permits an independent reader to follow and check the path from basis to result. Outside results relied on must be identified precisely.

2.3 **Explicit definitions** — every symbol, scale, unit and constant used must be defined in the delivered text; no orphan constants, no placeholders, no TODOs, no undefined symbols. (This mirrors the pre-registered C4.8 recomputability requirement: a third party can recompute `D(M,T)` from the delivered text alone.)

2.4 **Applicability declaration** — per cell for T-1/T-2/T-3 (5 task families T1–T5 × 3 mechanisms M1–M3 = 15 cells) and per family for T-4 (5 family-indexed entries), stating for each item where it applies and where it does not.

2.5 **Separation of supplied and non-supplied parts** — items that cannot be supplied or originated are to be marked as such, item by item, with reasons. Missing items are **not** to be replaced by estimates, substitutes, or self-authored formulas (C4.9 zeroing discipline, carried).

*(These are delivery-format and evidence requirements only; they do not prescribe the structure or content of the reply, per the standing "no reply outline" ruling.)*

## §3 C4.9 applicability question (open question ③) — answered

3.1 **Answered: C4.9 does not stand ahead of this solicitation as a blocking condition.** Its zeroing rule bars *un-sourced filling* — estimates, substitutes, or self-authored formulas used in place of a missing item. Content originated by the authorized source under this transmission, delivered with the §2 evidence bundle, is sourced content and is not barred by it. The applicability question therefore does not require the missing content to be in place before it is supplied.

3.2 **What is unchanged**: the C4.9 wording is cited as recorded, not altered; and for any item not yet delivered, the on-disk registered status (`任一项缺失 ⇒ 不可算 + γ`, `4185bdad6df5` §2.4.2, line C4.9) remains as registered — a status marker on the project side, not a bar to this solicitation. Upon delivery of an item along the acceptance path below, that item leaves the missing set.

3.3 **Not adjudicated here**: acceptance, grading and adoption of any delivered value remain with the project side (PI / verdict-keeper); delivery is not adoption.

## §4 Re-solicitation — the four inputs (requested outcome)

4.1 Supply, or stand as the authorizing source and originate (per §1): `u*(a_t)` (T-1, with payoff scale/units/range and the 15-cell applicability) · `L(M,T)` (T-2, with the IC-capacity and mechanism-identifiability definitions and their applicability) · `U(M,T)` (T-3, with the convergence condition and its mapping to a numeric `U`) · `max_u(T)` (T-4, five family-indexed values on the same specified payoff scale, source attached per family).

4.2 These will be registered as the addressee's **proposed true values** (true-value suggestions) for the C4 items. They enter the project's pre-registered acceptance list (`4185bdad6df5` §2.4.2, items C4.2–C4.5 and C4.8) before any adoption; adoption and any correctness adjudication remain with the PI / project side.

4.3 Partial deliveries are acceptable and will be registered per part (§2.5).

## §5 Qualifications carried from the prior record (so they are not mis-read)

5.1 `U` is necessary but not sufficient: other missing inputs (`ε`; M1 internal parameters) lie outside these four asks; "U removes the U-dependent blocker" — not "U closes the line".

5.2 "Five numbers, not one universal constant" concerns family indexing and attribution; it does not state that the five numerical values must differ.

## §6 Material references (all in the local repository; fingerprints measured 2026-10-10)

| # | Item | Path | SHA-12 | Bytes |
|---|---|---|---|---|
| 1 | P-B V0 spec | `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | `423c84de20d5` | 15,457 |
| 2 | First commission | `letters/_commission_c4_values_EN_2026_10_10.md` | `a397621085d6` | 56,217 |
| 3 | First reply — construction rule / values boundary | `letters/_codex_theory_derivation_reply_2026_09_30.md` | `7558eb1a5e34` | 71,002 |
| 4 | Second reply — formal non-availability | `letters/_codex_c4_values_reply_2026_10_10.md` | `8e4972352291` | 13,378 |
| 5 | Follow-up commission | `letters/_commission_c4_values_followup_EN_2026_10_10.md` | `abe0652ab00f` | 7,583 |
| 6 | Follow-up reply | `letters/_codex_c4_values_followup_reply_2026_10_10.md` | `97a35f8ae94c` | 4,490 |
| 7 | C4 correction register (canonical declaration; §4-a open questions) | `results/_c4_theory_source_caliber_correction_2026_09_30.md` | `61b139efd0ef` | 25,022 |
| 8 | Frozen acceptance list & zeroing rule (pre-registration) | `results/_v5_item21_rerun_conditions_prereg_2026_09_28.md` | `4185bdad6df5` | 31,429 |
| 9 | Bayesian-baseline design | `results/_bayesian_baseline_design_2026_10_10.md` | `7e181a167702` | 29,783 |

## §7 Delivery format & attribution (carried)

- Giver/venue and applicability on every value or definition (§2.1, §2.4).
- Partial answers acceptable; mark each part separately (§2.5).
- No need to re-derive anything recorded as already delivered in the prior record; no requirement to accept prior conclusions. Your reply is your own.

## §8 Boundary

This draft: modifies no repository document; makes no adjudication for the PI or the verdict-keeper; changes no threshold and no pre-registered wording (C4.9 included); is not adopted automatically; supplies no value, formula, outline or verdict. Its addressee and release decision remain with the PI. Fingerprint (SHA-256 / SHA-12 / byte count) is reported with delivery, outside this file.
