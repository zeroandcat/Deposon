# Benchmark & gates

This harness evaluates LLM **memory-probe behavior** under a pre-registered
protocol: a candidate list of 128 numbered keys, a frozen blind subset K_h
(32 keys; low half k<64: 13, high half k>=64: 19; seed 20261115), 12-slot
fill-in rounds (each call fills 12 mutually distinct candidate keys), and
instruction-minimal-difference interventions delivered through the operation
payload rather than instruction text.

## Joint readings disclosure

**Every reading is a joint reading of the model under test and this
harness.** Reports must carry the harness configuration alongside model
names (see the locked-baseline self-check line in `docs/locked-baseline.md`).
Raw scores without a harness pointer are not results.

## Gate table (pre-registered; frozen before each run)

| gate | criterion (pre-registered form) |
|---|---|
| G1 | K_h hit share vs pre-registered opportunity band around the 0.25 chance level |
| G2 | stripping invariant: rescued / parse-failed operations excluded from both numerator and denominator |
| G3 | constant-column rejection (constant columns must not produce a reading) |
| G4 | per-tier failure classification (INVALID / ES-x / FAIL_partial taxonomy, fail-loud) |
| G5 | T_fp_cc cardinality bound |
| PG | protocol gates PR-1 / PR-2 / PR-3 (see SAFETY.md) |
| 6th | forged-state detection: bit-exact state verification against the external ledger |
| G6' | granularity: per-call distinct keys >= 11/12; chain repeat_rate <= 5% |
| G7' | member decoupling: coupling component kappa = P(low half \| K_h hit) - m*nL/(m*nL+n*nH), \|kappa\| <= 0.10 |
| G8' | instruction minimal-difference: dv==wd (intervention via op payload, not instruction text) |

### On G7' (coupling component, formalized)

The registered intent of G7' is to detect **coupling between K_h membership
and ordinal position beyond a model's general display-position preference**
(which is tolerated by design). The formalized statistic kappa corrects for
the op half-distribution (expectation correction):

- kappa = 0 exactly at the 2x2 independence equation a*n*nH = b*m*nL
  (machine-checked; `gates/G7p_decoupling.lean`, theorem `kappa_zero_iff_indep`).
- The naive caliber P(low|K_h hit) - nL/(nL+nH) has zero expectation only
  under a uniform op half-distribution (machine-checked iff, same file) and
  fires on perfectly decoupled models otherwise; it is reported for
  continuity but does not adjudicate.
- The normalized ratio caliber (per-half rate vs composition density) shares
  the zero-locus but a different denominator; it additionally senses
  within-half density deviations and is reported side-by-side.

The negative control (single-key lock-in, PC-lockin) must fail loud on G6'
(mock certification in `mocks/`).

### Reader-plugin empirical validity

The read-side plugin (V4b read-side, frozen tool copy sha
`088ed4f8dd9c`) was verified for triple consistency (plugin readings vs
harness records vs per-call logs) in evidence round P2'. Pointer:
`docs/evidence-rounds.md`.

## Evidence rounds & recompute

Evidence rounds are pointer-only: `docs/evidence-rounds.md`. Self-contained
readings packages (data + frozen tool copies + SHAs + recompute scripts)
are the audit chain; the recompute path is `scripts/` + `gates/` +
`frozen/` + a readings package. CI never requires external data.

## Usability ablation (LongMemEval-S × dsh shell × teamorouter)

Pre-registered deathline: plugin-usable iff M − E ≥ −3pp (acc on n=92
excluded-adjusted set; exclusions pre-registered: 2 static PI rulings +
6 same-family double-403 auto-exclusions, ledger persisted).

| arm | acc | n |
|---|---|---|
| M (memory plugin on) | 0.0652 | 92 |
| E (enabling baseline) | 0.0761 | 92 |

**M − E = −1.09pp ≥ −3pp ⇒ PASS (usability confirmed).**
McNemar exact b=2, c=3, p=1.0 (no significant paired difference).
Ledger coverage 0.7283 (67/92); read/write paths exercised; no recall
rewrites. Build cost 67,393.9 tok/question, 599.2 s/question (gateway
window). Full audit chain: readings package (12-file manifest, sha12
fingerprints, recompute script `recompute_ablation.py`, raw_full.tar.gz
1,236 artifacts) — evidence round pointer, not bundled.

Note: gain note position (+5pp) not reached; marginal-cost readings as
registered. Judgment-free reporting; final read belongs to A-track + PI.
