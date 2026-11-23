# Slot-space caliber gauge (preview.7 interface F, judgment-line v1.3 candidate)

Executable face: `gates/slot_space_caliber.py` (library + self-test gate,
exit code 0 = ALL PASS). Vectors: `mocks/slot_space_vectors.json`
(published-vector style, exact fractions, zero network). Python-only face
by design (same precedent as `gates/judgment_strictness.py`); a Lean mirror
of the moment-decomposition identity is a follow-up candidate, not part of
this bump.

## Motivation (published readings)

Judgment-line v1.1 pins the measure locator (a judgment must declare its
measure and granularity), but a **reused statistic can still carry a
stowaway constant from another line's granularity**. The published case
(D1 G2/V3R3 round, correction registered 2026-11-24):

- a slot-dispersion statistic `slot_var` was reused verbatim from a probe
  line whose task slot space is 0..127 — whose uniform mean 63.5 was
  hardcoded as the center;
- the receiving line's observed slots collapsed to the perfect
  enumeration `{0..11}` (sample mean 5.5, inside the 0..127 space);
- the reported "variance" 3375.9 was 99.6% position term
  `(mean - c)^2 = (5.5 - 63.5)^2 = 3364`; the true variance was
  `143/12 = 11.9167`;
- the normalized ratio flipped **direction**: 2.473 ("over-dispersion")
  -> `143/16383 = 0.0087` ("strong collapse").

The identity `E[(x - c)^2] = Var(x) + (mean - c)^2` is the
machine-checkable decomposition: a second moment around a declared center
is only a dispersion reading when the position term does not dominate it.

## Interface F: slot-space caliber

A reported slot-dispersion statistic must be recomputable from the raw
slot observations plus the center and slot space it declares. The gauge
recomputes, as exact rationals:

- `var_true = E[(x - mean)^2]` — sample-mean centered (the dispersion);
- `pos_term = (mean - c)^2` — the center-offset artifact;
- `moment = E[(x - c)^2]` — what the reported statistic actually was;
- `share = pos_term / moment` — position-term dominance.

Checks:

- **F1 center-caliber (primary band, adjudicates)**: `share <= 1/2`
  (inclusive) the dispersion reading STANDS; `share > 1/2` INVALID — the
  reported statistic is majority center-offset, not dispersion, and must
  be recomputed;
- **F2 slot-space membership (primary band, adjudicates)**: every
  observed slot lies in `[0, space_hi]`; a violation INVALID (the declared
  space does not contain the observations);
- **F3 ratio caliber (reference, never adjudicates)**: the normalized
  ratio uses `var_true` over the uniform-space variance
  `((space_hi+1)^2 - 1)/12`; the defective-face ratio (moment in the
  numerator) is recomputed side-by-side and reported — direction-flip
  evidence, never an adjudication basis.

Degenerate cases: `n = 0` INCONCLUSIVE (never a silent pass);
`moment = 0` `share := 0` (perfectly at-center). Malformed slots fail
loud (`ValueError`), not silently skipped.

## Vector anchors (exact fractions)

| vector | expected | verdict |
|---|---|---|
| d1_r1_enumeration | share = 40368/40511; var_true = 143/12; moment = 40511/12; ratio_true = 143/16383; ratio_defective = 40511/16383 | INVALID (position term 99.6%) |
| f8j_v73frozen_call04 | share = 27/44764; var_true = 44737/48; mean = 257/4 | VALID (caliber appropriate in the 0..127 line) |
| boundary_share_half | share = 1/2 | VALID (inclusive edge) |
| just_over_half | share = 9/13 | INVALID |
| out_of_space_member | slot 128 outside 0..127 | INVALID (membership band) |

Rounding faces of the D1 anchor match the registered correction file
(2af01f9538f7) exactly: moment 3375.9 at 1dp, defective ratio 2.473 at
3dp, true ratio 0.008729 at 6dp. Boundary inclusivity, empty-set and
at-center degenerates, malformed-slot fail-loud, and the
reference-band-never-adjudicates rule are asserted by the self-test
(9/9).

## Discipline (cross-line reuse)

Any statistic copied across experiment lines must re-check its granularity
caliber before reuse (here: slot space 0..127 vs the collapsed 0..11
support, and the stowaway center constant). This is the same family as
the flattened-unit mis-read rejected by the v1.1 measure locator — the
unit survives, the center does not. The frozen readings face of the
affected round stays untouched (0-modification); corrections register as
separate files anchored to the package fingerprint.
