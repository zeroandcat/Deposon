# Deposon

**An auditable, conservation-guaranteed, game-theoretically tested scattering layer over LLM reasoning paths.**

📄 **Paper: [arXiv:2609.09001](https://arxiv.org/abs/2609.09001)** — final CN/EN manuscripts in `paper/`
(此前“无论文留痕（pending arXiv endorsement）”的限制已于 arXiv 上线后解除).

> Large result files (>100KB) are not stored here; they are tracked by sha256 + regeneration
> command in [`results/MANIFEST_large_files.md`](results/MANIFEST_large_files.md).
> Figures (PNG) are generated locally via `tools/make_figures_v2*.py` and are not tracked.

## What this is

Multi-step LLM reasoning lacks a machine-recheckable ledger: discarded reasoning paths leave no
auditable record. The Deposon scattering layer binds each node of an LLM-generated
concept-decomposition graph to a two-parameter state; paths undergo three-channel scattering —
transmission, reflection, irreversible dissipation — obeying **T+R+A=1** for arbitrary parameters,
with a maximum per-path energy-audit deviation of **2.2e-16** (machine epsilon).

## Final results (three evidence tiers, reported honestly)

- **Closed (pre-registered)**: on synthetic trap benchmarks the path-filtering gain is decisive —
  unified reaches **100%** vs a decoy-capture baseline at 7%/10%; verdict functions were frozen
  before execution (`docs/GT_FORMALIZATION_v1.md`, SHA-256 anchors below).
- **Consistency evidence**: modeling the reverse dynamics as a potential game on the graph, we
  evidence an auditable scalar's monotonicity and near-gradientness and quantify the **empirical
  coordination ratio (ECR, median 4/3, 20/22 graphs)**.
- **Motivation only / negative results**:
  - On real benchmarks the layer is indistinguishable from a trivial six-keyword rule filter
    (GSM8K 0.87 ≥ 0.85; StrategyQA 0.899 = 0.899) — power-honest CIs (unpaired Newcombe):
    GSM8K −2pp [−11.8, +7.8]pp, StrategyQA 0pp [−8.8, +8.8]pp (`results/deposon_v22_e95ci.json`).
    The claim is sharpened to: *the differential value lies solely in machine verifiability*.
  - Fusion with a semantic prior never improves (0.484 → 0.452); the apparent λ=2 gain is an
    anti-field artifact. Any fusion gain must be nonlinear.
  - **All three formalized dynamical-equivalence propositions are falsified** under the
    pre-registered kill protocol: P1a (max dev 0.8569, O(1) not O(lr²) at operating points),
    P1b (min cos overshoot), T-P1c (entropy-regularized mirror-ascent: τ∈[0,4], 81-point frozen
    grid, min cos = **−1.0**, per-state τ* median = 0) — see `run_v21_gtformal.py`,
    `run_v22_p1c.py`, frozen verdicts in `results/deposon_v21_gtformal.json` /
    `results/deposon_v22_p1c.json`. The potential-game claim is downgraded to *approximate*
    (cyclic-graph median residual 0.669).

## Methodology (the real product)

- **Preregistration with hash anchors**: verdict pure functions frozen before runs; SHA-256 (first
  12) on record — `docs/GT_FORMALIZATION_v1.md`=aeefb8ef6972, `run_v21_gtformal.py`=9bbe43f41fa8,
  `run_v22_p1c.py`=6e9673205dc0, `docs/SPEC_GT2B.md`=68a5b08ef007, `docs/SPEC_GT8C.md`=6b09de9911c0.
- **Kill criteria are first-class**: every hypothesis ships with a preregistered kill line;
  killed claims are archived, never rewritten retroactively ("与死同行").
- **Versioned verifier**: `verifier/v1`–`v43`, append-only run log including failed runs
  (`verifier/runs/`).
- **Independent multi-role review**: dual peer reviews → independent editor → post-edit
  verification (`reviews/`, `docs/reviews/`).
- **Audit != grep**: the first true re-execution audit re-ran the v22 scripts in an isolated copy
  and diffed frozen JSONs bit-for-bit (only wall-clock differs).

## Layout

| Path | Content |
|---|---|
| `deposon_diffusion.py` | diffusion field core (forward thermalize / reverse anneal / row-simplex projection) |
| `deposon_agents*.py` | benchmark pipelines |
| `run_v21_gtformal.py` / `run_v22_*.py` | GT-formal kill tests (P1a/P1b/P2/P3) and T-P1c / E9.5-CI |
| `run_v15`–`run_v20_*` | earlier experiment waves (each with SPEC in `docs/`) |
| `docs/` | SPECs, findings, lessons, roadmaps, `V3X_COLLAB_DIRECTIONS.md`, `PAPER_BRIEF.md` |
| `paper/` | **final CN/EN manuscripts (arXiv:2609.09001)** + frozen v1 legacy |
| `results/` | frozen experiment JSONs (+ large-file manifest) |
| `tests/` | 398 tests (`pytest -q`) |
| `verifier/` | versioned acceptance checks v1–v43 + append-only run records |

## Reproduce

```bash
pip install -r requirements.txt
pytest -q                        # 398 tests
python3 run_v21_gtformal.py      # GT-formal kill tests (no API calls; frozen seed)
python3 run_v22_p1c.py           # T-P1c kill test -> verdict: killed
python3 run_v22_e95ci.py         # E9.5 power-honest CIs
bash verifier/v43/check.sh       # latest acceptance gate
```

## Roadmap (V3.X, collaboration-oriented)

`docs/V3X_COLLAB_DIRECTIONS.md`: P-A equilibrium-transition stabilization cost >
P-B verifiable declarations > P-D auditable-ledger fingerprint protocol > P-C two-phase
structure — each with mechanical kill lines.

License: MIT (see LICENSE).
