# Launcher family

This directory hosts the launch-family entry points and the in-repo
core formalization of the memory harness:

| file | generation | notes |
|---|---|---|
| `p2p_launch_v3_exec.py` | v3 | first P2' launch (12-slot fill-in format) |
| `p2p_launch_v4_1_exec.py` | v4.1 | rerun launcher (A main cell + KIMI cell) |
| `p2p_launch_v4_2_switch_patch_exec.py` | v4.2 | switch-segment patch launch |
| `g6f_launch_exec.py` | G6f | per-op key-level supplement launch |
| `NingziContainer.lean` | core | condensate-field container formalization (Lean 4, core-only, zero mathlib; cliff/fairness theorems) |
| `CondensateLedger.lean` | core | machine-checked semantics of the ledger core, T1–T6 (Lean 4, core-only, no `sorry`; dual-implementation cross-check: `mcp/ledger_crosscheck.py`) |
| `DeposonThermo.lean` | core (preview.10) | thermodynamic ledger conservation: per-transition first law `e0 = phi + refl + diss + us.sum` (inject / dissipate / transmit / reflect / deposit), second-law direction anchor (`diss` monotone), pool monotonicity, hand-computed settlement vector (`settle_close`, `settle_conserved`, by `decide`, axiom-free) — 15 theorems, one `#print axioms` each, axioms ⊆ {propext, Quot.sound}, no `sorryAx`; `lean_axiom_audit.py` audits the compile log; dual-implementation cross-check: `mcp/thermo_crosscheck.py` |

Notes:

- All paths are environment-parameterized in this public release
  (`HARNESS_LIB_PATH`, `HARNESS_GLOBAL_BASELINE`, `HARNESS_GLOBAL_GUARDRAIL`,
  budget caps via the launcher config). No absolute paths, no credentials.
- The core chain runner module is not yet included in this v0.x preview; it
  is staged for a following release. The recompute path (`scripts/` +
  `gates/` + `frozen/` + a readings package) is fully functional without it.
- Per-round frozen tool copies (byte-identical, hash-anchored in each
  MANIFEST) live in the readings packages, not here; this directory is the
  living release form of the launchers.
