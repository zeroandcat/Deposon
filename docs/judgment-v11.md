# Judgment-line v1.1 interfaces (gauge / raw-full / three-band)

Executable face: `gates/judgment_v11.py` (library + self-test gate, exit code
0 = ALL PASS). Machine-checked face: `gates/judgment_v11.lean` (Lean 4
core-only, zero sorry; compiled in the four-step chain). Vectors:
`mocks/judgment_v11_vectors.json` (published-vector style, exact fractions,
zero network).

These three interfaces pin the judgment-line semantics that the experiment
series carries between rounds:

## A. Measure-locator discrimination (gauge gate)

A judgment must declare **which measure at which granularity** it computed.
The registry pins the pre-registered locator per measure id; the gate
(a) accepts a judgment only if its declared granularity matches the
registered locator, and (b) recomputes the value from the declared vectors
(exact rational arithmetic) and requires equality.

Design rationale: flattening a key-level selection measure to token level
rewrites both numerator and denominator non-uniformly (152 keys x 16 tokens
= 2432 units), so the mis-read value drifts — far enough to flip verdicts
in both directions at a kill-line boundary. The gauge gate rejects the
mis-calibrated judgment **before** adjudication; the mirrored flip vectors
(`flattened_would_kill` / `flattened_would_pass`) demonstrate both
directions. Lean face: `flatten_len_uniform`,
`token_as_key_population_mismatch` (2432 ≠ 152 as a decided fact).

## B. Raw-full logging obligation

Every response record — **accepted, gate-rejected, and parse-failed alike** —
must carry the verbatim response text (`raw_full`), of which `raw_head` is a
prefix. The checker validates the obligation declaration (all three
dispositions covered) and every record (non-empty, prefix-consistent),
failing loud per record with an index and disposition.

Design rationale: a head-only log cannot answer *where* an unparseable
response went wrong (line overflow vs. duplicated slot); the exact failure
position is only recomputable from the full text. Lean face:
`headonly_record_breaks_obligation`,
`full_coverage_three_dispositions_holds`,
`non_prefix_head_breaks_obligation` (character-code `List Nat` modeling —
`String.isPrefixOf` reduces through the `String.Iterator`/`UInt32` layer
which does not close under kernel reduction; same modeling posture as
Rat -> cross-multiplication on `Nat`).

## C. Three-band adjudication

`adjudicate(prereg, readings)` returns three bands with distinct semantics:

1. **Primary band** — the only band that adjudicates. Kill line is an exact
   rational comparison with an inclusive boundary (`ge`: value at the line
   => KILL; missing value => INCONCLUSIVE, degenerate segments carry zero
   contrast information).
2. **Reference band** — reported side-by-side, never adjudicates.
   Machine-checked: `verdict_indep_of_refs` / `verdict_indep_of_anns`
   (changing reference/annotation inputs cannot change the verdict).
3. **Annotation band** — threshold-triggered flags (e.g. gate-cost
   displacement), reported and never adjudicating.

Boundary semantics are machine-checked (`ge_boundary_inclusive`,
cross-multiplied on `Nat`), and the four vector anchors
(`v11_keylevel_below_line` / `at_line` / `flattened_would_kill` /
`flattened_would_pass`) are decided in Lean and asserted in Python against
the same fractions.

## Self-test

- `python gates/judgment_v11.py` — 14/14 gate checks (library face, used by CI)
- `python tests/test_gates.py` — includes the gate via importlib plus
  hand-checked fraction anchors
- `lean gates/judgment_v11.lean` — compiles clean; `#print axioms` ledger
  at end of file (zero sorryAx; standard `propext`/`Quot.sound` only on
  the list-length lemmas)
