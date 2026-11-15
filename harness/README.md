# Launcher family

This directory hosts the launch-family entry points:

| file | generation | notes |
|---|---|---|
| `p2p_launch_v3_exec.py` | v3 | first P2' launch (12-slot fill-in format) |
| `p2p_launch_v4_1_exec.py` | v4.1 | rerun launcher (A main cell + KIMI cell) |
| `p2p_launch_v4_2_switch_patch_exec.py` | v4.2 | switch-segment patch launch |
| `g6f_launch_exec.py` | G6f | per-op key-level supplement launch |

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
