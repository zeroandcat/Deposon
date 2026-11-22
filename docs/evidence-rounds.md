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
