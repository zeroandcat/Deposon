# deposon-harness

A pre-registered experiment harness for probing LLM **memory and
selection behavior**: frozen criteria, self-contained readings packages,
a dual-review evidence chain, and **Lean + Python dual implementations**
of the gate arithmetic.

What makes this harness unusual:

- **Pre-registered criteria, frozen before every run.** Gate definitions,
  thresholds, and failure paths are written down first; no post-hoc
  calibration inside a round. Negative controls must fail loud.
- **Self-contained readings packages.** Every round ships a package that a
  third party can recompute from the package alone: MANIFEST with content
  hashes, frozen criteria and tool copies, per-op ledgers, logs, and a
  recompute script. If a number cannot be recomputed, it is not a reading.
- **Dual implementations of the gates.** Gate arithmetic exists as Python
  (execution) and as Lean 4 theorems (machine-checked adjudication,
  core-only, zero sorry debt); the two are cross-checked per round.
- **Joint readings.** Readings are a joint product of model x harness;
  every report line carries the locked-baseline self-check line
  (models / seed / frozen faces / tool hashes).

## Status: v0.x preview

**This is an early preview.** Expect compatibility-breaking changes without
notice. The core chain runner module is staged for a following release; the
recompute path is fully functional. No public verdict claims are made from
this repository until the terminal review of the experiment series.

## Quickstart (recompute)

```bash
# with a readings package directory at hand:
READINGS_PACKAGE_DIR=/path/to/readings-package python scripts/g6f_recalc.py
# gate arithmetic self-test (pure math, no data needed):
python tests/test_gates.py
```

## Repository layout

| path | content |
|---|---|
| `harness/` | launch-family entry points (env-parameterized) |
| `frozen/` | frozen faces (blind K_h mapping, seed) |
| `gates/` | gate specifications: Lean + Python dual implementations |
| `mocks/` | mock certifications incl. PC-lockin negative control |
| `scripts/` | recompute script family |
| `docs/` | evidence-round pointers, locked-baseline spec, package spec, alignment map |
| `BENCHMARK.md` | gate table & joint-readings disclosure |
| `SAFETY.md` | run-safety clauses (PR-1/2/3, stop-loss semantics) |

Readings data never enters this repository (artifacts policy, see
`.gitignore` and `CONTRIBUTING.md`).

## Documentation

- [BENCHMARK.md](BENCHMARK.md) - gates, formalized criteria, plugin validity
- [SAFETY.md](SAFETY.md) - protection clauses & stop-loss semantics
- [CONTRIBUTING.md](CONTRIBUTING.md) - ground rules for contributions
- [README.zh.md](README.zh.md) - Chinese README (中文说明)
- [docs/](docs/) - evidence rounds, specs, alignment map

## License

MIT. (Apache-2.0 kept as a recorded fallback option.)

## Citation

```bibtex
@misc{deposon-harness,
  title  = {deposon-harness: a pre-registered memory-probe experiment harness},
  note   = {v0.x preview; joint readings of model x harness; recompute-from-package},
  year   = {2026},
  url    = {https://github.com/zeroandcat/deposon-harness}
}
```
