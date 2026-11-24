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
- **Judgment-line v1.1 interfaces.** Three plugin-faced pins for verdict
  hygiene: a *measure-locator gate* (a judgment must declare its measure and
  granularity, recompute-checked — flattened-unit mis-reads are rejected
  before adjudication), a *raw-full logging obligation* (accepted, rejected,
  and parse-failed responses all carry verbatim text), and *three-band
  adjudication* (only the pre-registered primary band adjudicates; reference
  and annotation bands report side-by-side, never decide — machine-checked
  in Lean). See `docs/judgment-v11.md`.
- **Judge-strictness and slot-space caliber gauges (preview.5/7/8).** A judge
  must be calibrated before its marks adjudicate (interface D,
  `docs/judgment-v12-strictness.md`); a reused dispersion statistic must
  survive the center-caliber decomposition `E[(x-c)^2] = Var(x) + (mean-c)^2`
  — the position term must not dominate it (interface F,
  `docs/slot-space-caliber.md`, published case: a direction flip 2.473 ->
  0.0087 from one stowaway cross-line center constant; preview.8 closes the
  denominator declaration: the share is `pos_term / moment`, never
  `pos_term / uniform_var`). The six-family linkage table
  (`docs/family-linkage.md`, interface E) is fully linked as of preview.8 —
  every iteration family's readings package anchor is registered in
  `docs/evidence-rounds.md`, with the per-row judgment logged.
- **Readings-package completeness validator + Lean mirror close-out
  (preview.9).** `gates/readout_completeness.py` (interface G) scores any
  readings package against the eight required contents of
  `docs/readings-package-spec.md` (MANIFEST sha256_12 + mtime with the
  zero-post-delivery-modification red line, frozen criteria, frozen tool
  copy, blind faces, per-round logs, key-level per-op ledger, readout JSON,
  recompute script with identity check); a missing key-level ledger makes
  key-level gates **UNDECIDABLE**, never silently passed. The Lean mirror of
  the slot-space caliber gate is cross-checked statement by statement
  (`gates/slot_space_crosscheck.py`), and the f3 solve-judge carries a
  calibration face (`gates/descrev_calibration.py`): the published DR-2
  judge reading is INCONCLUSIVE for strictness (no D-marginal) while its
  pre-registered main-1 face stands side by side.
- **Joint readings.** Readings are a joint product of model x harness;
  every report line carries the locked-baseline self-check line
  (models / seed / frozen faces / tool hashes).
- **The memory harness proper ships in-repo — two layers, not just tools.**
  (a) *Core layer*: the condensate-field container formalized in Lean 4
  (`harness/NingziContainer.lean`, core-only) and instantiated as an
  append-only external ledger with DR-4 render-surface semantics (reads
  return rendered `key: text` lines, never raw records); (b) *interface
  layer*: a standalone stdio MCP server (`mcp/`, protocol `2024-11-05`)
  exposing `deposon_memory_write` / `deposon_memory_read` as a thin surface
  over the core. The core runs import-direct with zero transport
  dependencies and survives model swaps and process restarts by
  construction; its self-test runs in CI.

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
# one shot, no clone (fetches this repo via npm's git resolver, runs every
# gate self-test + the plugin-load smoke + packaging integrity):
npx -y github:zeroandcat/dsh-plugin-deposon#v0.1.0-preview.9

# score a readings package against the 8 required contents (exit 0 = complete):
python gates/readout_completeness.py /path/to/readings-package            # JSON verdict
python gates/readout_completeness.py /path/to/readings-package --run-recompute   # + identity check

# with a readings package directory at hand:
READINGS_PACKAGE_DIR=/path/to/readings-package python scripts/g6f_recalc.py
# gate arithmetic self-test (pure math, no data needed):
python tests/test_gates.py
```

## Repository layout

| path | content |
|---|---|
| `harness/` | launch-family entry points (env-parameterized) + `NingziContainer.lean` (condensate-field container, Lean 4 formalization, core-only) |
| `mcp/` | memory harness proper as a standalone stdio MCP instance: core layer (external append-only ledger, DR-4 render surface) + `deposon_memory_write`/`deposon_memory_read` tool surface + self-test (runs in CI) |
| `frozen/` | frozen faces (blind K_h mapping, seed) |
| `gates/` | gate specifications: Lean + Python dual implementations, incl. judgment-line v1.1 interfaces (gauge / raw-full / three-band), the preview.5 judge-strictness gauge + six-family linkage validator, and the preview.7 slot-space caliber gauge (six-family table fully linked in preview.8; see `docs/judgment-v12-strictness.md`, `docs/family-linkage.md`, `docs/slot-space-caliber.md`) |
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
