# Six-family linkage (preview.5 interface E)

The iteration-candidate families (pre-registered in the experiment-line
planning doc, 2026-11-22 §2.2) map to this repository's adjudication and
readings interfaces below. This table is **pointer-only**: audit chains live
in the self-contained readings packages, not here. `gates/family_linkage.py`
validates structural consistency (ids, file references, anchor formats) in
CI; it never fabricates pointers — a `pending` status row is a honest
"not yet linked" marker.

| fid | family | in-repo interface | pointer row | status |
|---|---|---|---|---|
| f1 | fire8 RED three-arm follow-up (ES5-bacc custodial vs 300-step dose) | `gates/judgment_v11.py` three-band adjudication; evidence-rounds row `fire8R` | fire8R 48-piece readings package anchor in `docs/evidence-rounds.md` | linked |
| f2 | A8 w500/w600 platform continuation (PW-1 marginal-gain deathline) | `gates/judgment_v11.py` three-band adjudication (reference band: marginal-gain readings) | pending (A8 w600 terminal readings package delivered 2026-11-22; row on next bump) | pending |
| f3 | describability reverse-solve engineering | `gates/judgment_strictness.py` judge-strictness gauge (calibration face for the solve-judge) | pending | pending |
| f4 | E-2 / E-3 restart candidates (R2 perm derivative line) | `gates/judgment_v11.py` measure-locator gate (key-level locator discipline) | pending | pending |
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
