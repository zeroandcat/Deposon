# HANDOFF — point-in-time handoff (2026-11-27, morning register)

**Purpose.** A cold-start handoff for any new session (human or agent). It is
overwritten in place per window; the round ledger is the git history. The
aligned baseline table lives in the "Status" section of `README.md`.

## 1. What changed in the last window (2026-11-27 morning)

- **Experiment.** The two-host three-arm chain (A → C → B) completed on both
  hosts (six arms, exit 0, guard v6 0 ALERT, automatic shutdown executed after
  the chain). The morning data pull and the readings-validator pass are done;
  verdicts are registered as-is: main gate G-A2 not passed (probe hits 0/256 on
  both executor arms; zero-count-arm upper bound 0.011634; McNemar p = 1), G-A3
  and G-B not passed, the never-written negative control clean, the structural
  (true dual-binding) positions all pass with the R-observation readings
  bit-identical across hosts; G-C1 out-of-band, registered in parallel to the
  confirmation rounds (re-judgement requires a new criteria freeze, pending).
- **Plugin.** Release tag `v0.1.0-preview.11` (`5efc158`, CI green) stays the
  stable point. The development frontier is `9219e78` (preview.12) on
  `b/organ-v311-preview11`: the update/upgrade path, the ledger-era handshake
  server half, lazy executor imports, re-pinned self-tests and the README
  "Update / upgrade" section — local-commit-only; its push and any tag
  movement await a project-owner decision.
- **Manuscript.** rev4.17 (`2c8252f`) frozen as FREEZE v13 at the branch tip
  `dea75bc` of branch `private/v5preR3` (public repository
  `zeroandcat/Deposon`, 77 commits, `main` untouched); not merged into `main`
  (unrelated histories — editorial decision pending).
- **Docs.** The three repositories' README/handoff are aligned to this
  baseline; the companion-plugin sections follow the compatibility draft
  (draft blob `72b8a1f8e85e0d7c`).

## 2. Open items (decisions pending — no action without an order)

1. **Merging the manuscript branch into `main`** of the public repository: the
   two histories are unrelated; a merge would conflict on three root files
   (`.gitignore`, `LICENSE`, `README.md`) and needs an editorial decision.
2. **Plugin**: pushing the development frontier `9219e78` (preview.12) and any
   tag movement — pending a project-owner decision; the tag stays at
   preview.11 until then. The published branch additionally carries docs-only
   register commits above `6110448`; merging them with the frontier touches
   disjoint files.
3. **G-C1 re-judgement** requires a new criteria freeze event (v1.3) —
   pending; the current verdicts are registered as-is, no gate tuning.
4. **Internal identifiers** that ride along with evidence documents on the
   published manuscript branch are tracked for neutralisation in a follow-up
   commit. The repositories contain no credentials.

## 3. How to verify the baseline offline

Fetch the release tag or the development frontier — from the plugin repository
or from a bundle — and check the pinned sha256 values listed in `README.md` →
Status. Readings data never enters this repository (artifacts policy).
