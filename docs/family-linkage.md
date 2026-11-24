# Six-family linkage (preview.5 interface E; all six rows linked as of preview.8)

The iteration-candidate families (pre-registered in the experiment-line
planning doc, 2026-11-22 §2.2) map to this repository's adjudication and
readings interfaces below. This table is **pointer-only**: audit chains live
in the self-contained readings packages, not here. `gates/family_linkage.py`
validates structural consistency (ids, file references, anchor formats) in
CI; it never fabricates pointers — a `pending` status row is a honest
"not yet linked" marker. The three `pending` rows left after preview.7
(f2/f3/f4) were judged row by row in preview.8 (log at the bottom); all six
are now `linked`, and the `pending` vocabulary stays for future families.

| fid | family | in-repo interface | pointer row | status |
|---|---|---|---|---|
| f1 | fire8 RED three-arm follow-up (ES5-bacc custodial vs 300-step dose) | `gates/judgment_v11.py` three-band adjudication; evidence-rounds row `fire8R` | fire8R 48-piece readings package anchor in `docs/evidence-rounds.md` | linked |
| f2 | A8 w500/w600 platform continuation (PW-1 marginal-gain deathline) | `gates/judgment_v11.py` three-band adjudication (reference band: marginal-gain readings) | A8 w600 readings package (verdict / train-summary / gates anchors, s0 = w500 verdict) registered in `docs/evidence-rounds.md` | linked |
| f3 | describability reverse-solve engineering | `gates/judgment_strictness.py` judge-strictness gauge; calibration face `gates/descrev_calibration.py` (preview.9: DR-2 -> INCONCLUSIVE / ZERO_CONTRAST, main-1 face reported side by side) | N9 DR-2 readings package (MANIFEST anchor + readout/stats/status anchors) registered in `docs/evidence-rounds.md` | linked |
| f4 | E-2 / E-3 restart candidates (R2 perm derivative line) | `gates/judgment_v11.py` measure-locator gate (key-level locator discipline) | E-2 R2 readings package (MANIFEST anchor) registered in `docs/evidence-rounds.md`; E-3 not launched, no pointer | linked |
| f5 | Lean L4-L9 rear-window theorem debt | `gates/judgment_v11.lean` core-only zero-sorry chain (style precedent for L4-L9 face) | L4-L9 implementation packages shared 2026-11-22 (four lean files, 50 theorems) | linked |
| f6 | plugin iteration candidates (this preview line) | `gates/judgment_strictness.py` + `gates/family_linkage.py` (this gate) | this bump | linked |

## Reading-discipline notes

- Family rows never adjudicate experiment outcomes; they only pin **which
  interface a family's readings pass through** and where the audit pointer
  lives. Verdicts remain pre-registered per launch (deathline freeze face,
  0-change discipline).
- A `pending` pointer row is upgraded to `linked` only when the readings
  package anchor (sha12) is registered in `docs/evidence-rounds.md` — never
  by editing this table alone (the validator checks anchor format but cannot
  check anchor truth; that stays with the readings packages).

## Per-row linkage judgment (preview.8)

Upgrade rule applied per row: anchor registered in `docs/evidence-rounds.md`
first, table second. Anchors were re-measured locally on 2026-11-24 before
registration (zero modification of any readings package).

- **f2 -> linked.** The A8 w600 terminal readings package is on record
  (verdict `be22957b3d94`, train_summary `43bedb9fd8f4`, gates `178415a408ab`;
  the private pull and the shared copy are byte-identical); the A-track
  judgment and the B-seat dual review both passed. The PW-1 outcome (PASS,
  platform confirmed, 700 window not opened) is registered as read; the
  plateau semantics stay with the PI's final read (0 adjudication here).
  Record-alignment note: the two review files cite `d6dd8c9bfb55` next to
  the verdict file name — that value is the sha12 of the terminal-account
  markdown; the verdict JSON itself measures `be22957b3d94`, which is what
  the evidence-rounds row carries.
- **f3 -> calibration face (preview.9).** Running the DR-2 attributions
  through `gates/descrev_calibration.py` gives `INCONCLUSIVE /
  ZERO_CONTRAST`: every probe has exactly one computable face (S=4, D=0),
  so the judge has no D-marginal and cannot be scored for strictness; the
  pre-registered main-1 face (acc >= threshold) is reported side by side
  and is never replaced by the calibration verdict.
- **f3 -> linked.** The N9 DR-2 (describability reverse-solve, second
  iteration) readings package is on record: MANIFEST anchor `12acb114f695`,
  with readout / stats / status anchors re-measured and equal to the B-seat
  values (5/5); the B-seat review passed with 0 blocking. DR-1 readings are
  untouched (stats byte-identical across DR-1 and DR-2), so the pointer names
  the DR-2 package as the current anchor.
- **f4 -> linked (E-2 only).** The E-2 R2 restart readings package is on
  record (MANIFEST `313a25eec630`, 15 files); the B-seat review passed and
  the A-track / B-seat dual review is closed. Its main judgment is "not met"
  (R-C BAcc +1.605pp under the 5pp frozen line) and is registered as read —
  a failed round still ships its package and still counts as a linked
  pointer. The B-seat boundary note is carried as is: the package holds no
  taskset answer-key face (server-side pointer), so true-value recomputation
  from the package alone is bounded. E-3 has not been launched and has no
  readings, so no pointer exists for it; the row is linked by E-2 alone.
