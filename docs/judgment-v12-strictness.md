# Judge-strictness gauge (preview.5 interface D, judgment-line v1.2 candidate)

Executable face: `gates/judgment_strictness.py` (library + self-test gate,
exit code 0 = ALL PASS). Vectors: `mocks/judgment_strictness_vectors.json`
(published-vector style, exact fractions, zero network). Python-only face
by design (same precedent as `gates/g6f_p0_gate.py`); a Lean mirror is a
follow-up candidate, not part of this bump.

## Motivation (published readings)

Judgment-line v1.1 pins WHERE a reading sits (measure locator), WHAT was
logged (raw-full), and WHICH band adjudicates (three-band). It does not pin
whether the **judge itself can discriminate**. Two published readings mark
the two ends of the strictness axis:

- the 150/150 constant-marks probe (zero discrimination, "too loose" first
  reading, 2026-11-22) — a constant judge lands at chance `d = 1/2`;
- chance-level discrimination at the opportunity band (VW-3 e16 0.5156).

## Interface D: strictness calibration

A judge must be calibrated on a pre-registered contrast-vector set before
any of its marks adjudicate:

- **pairs** carry only a class (`S` same-source / `D` different-source) and
  the judge's mark (`same` / `different`); nothing else is read;
- **primary band (adjudicates)**: discrimination `d = (tp+tn)/n` over exact
  rationals; the pre-registered line `d_lo = 3/4` is inclusive; `d < d_lo`
  is KILL; empty calibration is INCONCLUSIVE (never a silent pass);
- **reference band (never adjudicates)**: loose-bias `lam = fd/(tp+fd)`
  and strict-bias `sig = fs/(tn+fs)`;
- **annotation band (never adjudicates)**: `lam >= 1/10` flags `too_loose`,
  `sig >= 1/10` flags `too_strict`.

## Vector anchors (exact fractions)

| vector | expected | verdict |
|---|---|---|
| all_same_150 | d = 1/2, lam = 1 | KILL (constant marks = chance) |
| chance_76_of_151 | d = 76/151 | KILL |
| healthy_137_of_151 | d = 137/151, lam = 7/76, sig = 7/80 | PASS |
| boundary_exact | d = 114/152 = 3/4 | PASS (inclusive edge) |
| boundary_minus_one | d = 113/152 | KILL |
| all_different | d = 76/151, sig = 1 | KILL |

Boundary semantics (`ge_boundary_inclusive`), empty-set fail-loud
(`INCONCLUSIVE`, not PASS), malformed-pair fail-loud, and the
primary-band-only adjudication rule are asserted by the self-test (7/7).

## Companion interface E: six-family linkage

`gates/family_linkage.py` + `docs/family-linkage.md` pin which in-repo
interface each pre-registered iteration family's readings pass through,
with honest `pending` markers for not-yet-linked pointer rows. The
validator checks structural consistency (six ids exactly once, closed
status vocabulary, referenced files exist, pending/linked discipline) in
CI — it never fabricates pointers.
