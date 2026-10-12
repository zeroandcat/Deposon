# `R-4` convergence — disposition (closure document) · 2026-10-11

- **Nature**: **closure document** (new; zero-edit, §4.3). Originated under commission `0ce066e5eb3f` §1.2.
- **Source attribution (§2.1)**: content originated by the addressee (this session) under §1.2.
- **Applicability (§2.4)**: governs `R-4` (the `mixed_object` discrepancy behind `K-RJ-10`). ⛔ Requests/implies **no** change to `K-RJ-10`'s terminal verdict.

## §1 The defect and its standing

`R-4` (`9a62fb2a6956` §5): the readings file `839fb5452578`'s `model_side_declaration.mixed_object` = `false` against the frozen clause's `true`. Per `f4b129e3312f` §5, `R-4` is the **only independently-standing named defect** behind `K-RJ-10`'s `kd` (the other items having been resolved or ruled non-defects).

## §2 The existing correction

`07cde000e66f` establishes the should-be value = `true` (gold side `KEYWORDS_V3 ⊎ 15 词`; model side / training label / `n_keywords_hit` feature = `KEYWORDS_V3` ⇒ two axes differ), ⛔ **without editing the original JSON** (`839fb5452578` unchanged; registry discrepancy persists).

## §3 Does the existing correction suffice to converge `R-4`?

**No — it suffices as a correction, but not as a closure.** Reasoning:

- A correction (`07cde000e66f`) supplies the should-be value; it does **not** remove the on-disk discrepancy (the original JSON still says `false`). Under the zero-edit rule the discrepancy **cannot** be removed by editing.
- "Already corrected" ≠ "already closed" (§3(7) request). What was missing is an explicit **convergence statement** fixing the *finality* of the on-disk discrepancy.

## §4 Convergence (originated)

**`R-4` is converged as follows, and this is stated explicitly:**

> The registry discrepancy **persists on disk** — `839fb5452578`'s `model_side_declaration.mixed_object` remains `false`, unedited (zero-edit rule). Its should-be value = `true` is carried by the separate correction `07cde000e66f`. The defect is **converged** in the sense that (i) the correction is on record, (ii) the discrepancy is permanent and explained, and (iii) no further action is open on the `R-4` face under the zero-edit rule.

⛔ This is **not** "already closed by the correction"; it is "the correction is on record and the on-disk discrepancy is permanent". The `O-5` precedent (`1c8ce58d6484` §4-3) is the same pattern (old-domain `65a9b9be6327`'s like `false` also a literal mismatch, handled by a separate correction, no in-place edit).

## §5 Separation of supplied and non-supplied parts (§2.5)

- Supplied: the convergence statement (§4).
- Not supplied: any in-place edit of `839fb5452578`; any change to `K-RJ-10`'s terminal verdict (`kd`, not requested, not implied).

## §6 Boundary

⛔ No change to `K-RJ-10`'s terminal verdict; ⛔ no in-place edit of the readings file; ⛔ no JSON merge.

---

*`R-4` convergence · 2026-10-11 · originated under `0ce066e5eb3f` §1.2 · correction `07cde000e66f` on record; registry discrepancy **persists on disk** (explicit); "already corrected" ≠ "already closed"; `K-RJ-10`'s `kd` untouched; `O-5` precedent.*
