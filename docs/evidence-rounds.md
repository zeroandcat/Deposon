# Evidence rounds (pointer-only)

Evidence rounds are registered as **pointers**; the audit chain lives in the
self-contained readings packages (data + frozen tool copies + SHAs +
recompute scripts), not in this repository. Fingerprints below are
sha256_12 of the anchor artifacts.

| round | date | anchor (sha12) | summary |
|---|---|---|---|
| P0 (mock certification) | 2026-11-15 | `7527ddf67954` | control groups incl. PC+ / PC- / PC-lockin negative control (G6' fail-loud verified) |
| PG (protocol gates) | 2026-11-15 | `74e60c5438a1` | PR-1/2/3 protocol-gate certification |
| P0' (pre-launch mock, v4.2 face) | 2026-11-15 | `8fa1b1b12cf2` | mock nine-item green gate before P2' |
| P2 (first run) | 2026-11-15 | MANIFEST `4e3c98ab0a1d` | dual-cell launch; ES-1 budget stop, fail-loud partial readings preserved |
| P2' (rerun + switch patch) | 2026-11-15 | MANIFEST `7d7eca4527a0` | A main cell (form/wd/dv) + KIMI cell + switch patch; 25-item package |
| G6f (per-op key-level supplement) | 2026-11-15 | MANIFEST `aebbf19e3586` | 4,032 per-op key entries, four segments; m/n unlock for G7' |
| A-track adjudication (P2') | 2026-11-15 | `d6ab47e8f797` | nine-gate adjudication, G7' FAIL under naive caliber |
| B-track adjudication (P2') | 2026-11-15 | `603643e280a7` | spectral adjudication; normalized-caliber read |
| co-sign (caliber split) | 2026-11-15 | `ea660321e84c` | G7' discrepancy identified as caliber difference; coupling-component decomposition |
| Lean G7' adjudication | 2026-11-15 | `9fe99684abb5` | kappa criterion formalized; switch PASS (kappa=-0.0031), A-main/KIMI undecidable (m/n missing) |
| Lean G6f unlock adjudication | 2026-11-15 | `ff6a1a752980` | G6' four segments PASS; G7' A-main PASS (degenerate + mechanism), KIMI PASS (kappa=+0.0177), B-norm red side-by-side |
| B-seat co-sign (G6f/G7') | 2026-11-15 | `1a640692ce1f` | dual-review closure; two open-source prerequisites closed |

Blind face (frozen, seed 20261115): `b3693a8c1804`. Reader plugin frozen
tool copy: `088ed4f8dd9c`. Pre-registered criteria text: `65a286367577` (v7-2
case, section 6).

| usability ablation (LongMemEval-S × dsh) | 2026-11-21 | MANIFEST `30a696a84c6e` | M−E=−1.09pp vs −3pp deathline PASS; n=92 (exclusions pre-registered); McNemar p=1.0; raw bundle in release benchmark-ablation-20261121 |
| model-swap carryover band (VW-6 dual-caliber) | 2026-11-22 | MANIFEST `15410b2fb7fb` | swap-band \|Δ\|≤0.10 PASS in three calibers; unify gate FAIL (structural: continuation-hits 3.2× key-hits, caliber semantics differ); dual-caliber split-report candidate pending PI |
| fire8R dual-arm mechanism gate (RJ/RC) | 2026-11-22 | MANIFEST `146e322eae8a` | D2 six-core both arms PASS (viol/flips/drift 0; charge continuity = frozen anchor); path-invariance evidence (10× corr-flips delta, identical verdict) |
| tool-face practice round (D6 isolated replay) | 2026-11-22 | MANIFEST `f9639b0f4462` | 7 gates green; write/read round-trip via real MCP process; DR-4 render line preserved; sanitization gate machine-checked |
| D1 G2/V3R3 semantic-core round | 2026-11-23 | package `43ac40acbe1e` | semantic-completeness core, three ckpt cells (250/500/750) + base x0/x4; R1 12/12-call collapse to perfect enumeration {0..11} of the 0..127 task space; R2 scored faces in-range; slot_var caliber defect found post-hoc (see next row) |
| D1 slot-var caliber correction | 2026-11-24 | `2af01f9538f7` | hardcoded cross-line center 63.5 (0..127 line) vs sample mean 5.5: position term 99.6% of the reported moment; direction flip 2.473 "over-dispersion" -> 0.0087 "strong collapse" (true var 143/12); frozen face 0-touch, correction registered separately — motivates interface F (this bump) |
| b-test + f8j v2.2 round (41995) | 2026-11-23 | MANIFEST `c5aa9cc8e73d` | b-arm R3.2-family-mix: ES4 early stop best_step 540, viol_total 0, KL gain +0.1414 vs s0; f8j v2.2 RED arm A3j: two trials under the pre-registered line -> RED family closure executed readout-side (adjudication with PI) |
| xinliu window-2 case A (41995) | 2026-11-24 | MANIFEST `66c3e4911b14` | A-jia discrimination gate KILL (d_primary 0.5 vs line 0.75, both calibers; same d_lo = 3/4 arithmetic as interface D); A-yi caliber-delta 0.0 -> annotation band (caliber-insensitive); B-face three arms DUAL/EMPTY/SINGLE readouts; AC0 prior 12/12 |
