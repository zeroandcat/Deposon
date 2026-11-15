# dsh-plugin-deposon

**A DeepSeek Harness (dsh) plugin**: a pre-registered experiment harness for
probing LLM **memory and selection behavior**, installable and usable from
inside [dsh](https://github.com/deepseek-ai/deepseek-harness). Frozen
criteria, self-contained readings packages, a dual-review evidence chain,
and **Lean + Python dual implementations** of the gate arithmetic.

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

## Install as a dsh plugin

This repository follows the [dsh](https://github.com/deepseek-ai/deepseek-harness)
plugin conventions (`dsh-plugin-<name>` repository naming, the `dsh-plugin`
topic for discoverability, an npm package declaring `dsh.bundle.patch`, and a
Cordis `apply(ctx, config)` entry):

```bash
# from a running dsh agent / Web UI plugin manager:
dsh plugin add https://github.com/zeroandcat/dsh-plugin-deposon

# or from a local clone (path: spec):
dsh plugin add path:./dsh-plugin-deposon
```

Once installed, the plugin mounts as bundle entry `deposon` (see
`cordis.patch.yml`) and exposes the gates self-test as an agent-callable
surface (`deposon_gate_check` / `/deposon-gate-check`). Configuration keys
(`python`, `timeoutMs`) are consumed via the patch config or `DEPOSON_*`
environment variables.

Desk-level install verification (no network beyond GitHub): `npm pack
--dry-run` (packaged bundle integrity), `git ls-remote` (the reachability
precheck dsh's plugin manager runs before installing), and
`node tests/test_plugin_load.mjs` (loads the plugin on a mock Cordis context
and actually invokes the tool body — 14 checks, includes running the gates
self-test).

> Preview-era note: dsh is a developer preview with announced
> compatibility-breaking changes. The `apply` contract, bundle declaration,
> and config consumption here are the stable surface; agent-tool registration
> probes known API shapes defensively.

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
| `plugin/` | dsh plugin entry (Cordis `apply(ctx, config)`) |
| `cordis.patch.yml` | dsh bundle declaration (profile patch consumed by dsh plugin manager) |
| `package.json` | npm package: dsh plugin metadata (`dsh.bundle.patch`, `engines.dsh`) |
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
@misc{dsh-plugin-deposon,
  title  = {dsh-plugin-deposon: a pre-registered memory-probe experiment harness as a DeepSeek Harness plugin},
  note   = {v0.x preview; joint readings of model x harness; recompute-from-package},
  year   = {2026},
  url    = {https://github.com/zeroandcat/dsh-plugin-deposon}
}
```
