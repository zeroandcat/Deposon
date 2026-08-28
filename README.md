# Deposon

**Physics-constrained scattering layer for auditable LLM reasoning-path selection** — research trace repository (code, experiments, SPECs, independent reviews, verifier).

> Paper drafts are **excluded** from this repository's trace updates pending arXiv endorsement
> (无论文留痕). The legacy `paper/` directory remains frozen at its v1.4 state.
> Large result files (>100KB) are not stored here; they are tracked by sha256 + regeneration
> command in [`results/MANIFEST_large_files.md`](results/MANIFEST_large_files.md).

## Current status: v1.9 (2026-08)

- **E9.1 mean-field reverse annealing**: named-edge Hits@3 **17/17 = 1.000** on the anchor map
  (McNemar p = 1.22e-4 vs the v1.7.1 Dirichlet-random-init arm) — the earlier
  "field loses to random" result was a **sampler artifact**, not a property of the field.
  The field is a **skeleton detector**: filler-edge Hits@3 = 0.0625 (boundary disclosed).
- **E9.2 full-candidate ranking** (MRR / Hits@k, no negative sampling): sampler sensitivity
  eliminated by construction; sign flips vs the old N_NEG=10 protocol documented.
- **E9.3 high_couple alias fix**: GSM8K high_couple corrected **0.86 → 0.82**
  (the v1.4 number was produced by an alias bug, `deposon_agents_v1_4.py:1515`).
- **E9.4 equal-weight decoy control**: advantage survives weight flattening
  (0.85 vs 0.04) — v1.4 benchmark effect sizes are **structurally unattributable**
  (BFS short-path preference + free `type='trap'` labels). Disclosed, not hidden.
- **E9.5 rule baseline**: a 6-keyword rule filter (**0.87**) ties or beats the full
  LLM+physics pipeline (0.85) — zero incremental value of the LLM prior on this benchmark.
- **E9.6 quick wins**: graph-level sign tests (p = 0.0013 / 0.0075), seed scan
  (named = 1.000 ± 0.000), λ=2 null ablation (confshuffle = real → semantic claim weakened).

## Methodology (the real product)

- **Preregistration + amendments**: every experiment has a SPEC (`docs/SPEC_v*.md`);
  failed judgments are archived, rules are never rewritten retroactively.
- **Independent multi-role review**: dual peer reviews (11 Majors each) → independent editor →
  independent post-edit verification (`reviews/`).
- **Versioned verifier**: `verifier/v1`–`v11` frozen per iteration, append-only run log
  (`verifier/runs/`). Latest: **v11, FAILS=0 / 25 PASS, pytest 160/160**.
- **Negative results are first-class**: `*_negativeresult.json` archives, honesty sections
  in every result file.
- **No-API-discipline**: v1.9 ran entirely on cached LLM responses
  (prompt_sha256 on record, 800/800 cache hits).

## Layout

| Path | Content |
|---|---|
| `deposon_diffusion.py` | diffusion field core (forward thermalize / reverse anneal / row-simplex projection) |
| `deposon_agents_v1_4.py` | benchmark pipeline (v1.9: `resolve_high_couple_config`, legacy alias behind env flag) |
| `run_v19_*.py` | v1.9 experiments E9.1–E9.6 |
| `run_v18_api_supplements.py` | v1.8.1 E1–E4 (permutation invariance / contamination probe / direction robustness / contentless-label abstention) |
| `docs/` | SPECs (v1.5–v2.0), roadmaps (v1.9 / v2.X), lessons, game-theory pivot |
| `reviews/` | design probe, literature scan, power analysis, dual peer reviews, post-edit verification |
| `results/` | experiment JSONs (+ `MANIFEST_large_files.md` for large ones) |
| `verifier/` | versioned acceptance checks v1–v11 + run records |
| `corpus/` (soon) | v2.0 multi-map corpus (three-laws design) |

## Roadmap (v2.X)

Multi-map corpus (≥8 maps, three-laws design: quantitative→qualitative sweeps,
negation-of-negation structural family, unity-of-opposites twin maps) → game-theory turn:
potential-game convergence (GT-1), adaptive attacker (GT-2), dual-prior signaling (GT-3),
price of anarchy (GT-4). Every hypothesis ships with a preregistered kill criterion.
See `docs/Roadmap_v2X.md`, `docs/SPEC_v2.0.md`,
`docs/CLOSURE_v19_and_v2X_gametheory.md`.

## Reproduce

```bash
pip install -r requirements.txt
pytest -q                      # 160 tests
python3 run_v19_meanfield.py   # E9.1 (no API calls; reads cached prior)
python3 verifier/v11/check.py  # acceptance: FAILS=0 expected
```

License: MIT (see LICENSE).
