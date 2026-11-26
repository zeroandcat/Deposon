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
- **Thermodynamic ledger + phantom limb (preview.10).** The memory ledger
  now carries a thermodynamic layer (`mcp/thermo_core.py`): every injected
  row holds integer exergy that is attributed to exactly four accounts — Φ
  (transmitted), R (reflected), D (dissipated), U (in presence) — with the
  conservation core `E⁰ = Φ + R + D + U` checked fail-loud after every
  operation and the settlement being a pure event-stream replay (**self-
  settling, no external reconciler**). Reads pass a gate: accepted rows are
  transmitted, rejected rows pay their own exergy into D (entropy output),
  and dissipated memory is reflected as `⟨幻肢⟩` phantom-limb lines (felt,
  never recovered, zero source text replayed). The dissipation channel
  utilisation `D / E⁰_rows` moves from 0 % by construction to 69.23 % on
  the frozen 500-op trace (decay / horizon / evict / supersede / gate
  rejection), the price being a 50.31 % -> 47.85 % specific-key hit rate
  (another 2.45 % honestly reflected as phantom lines). The Lean mirror
  `harness/DeposonThermo.lean` machine-checks conservation per transition
  (15 theorems, 0 sorry, axioms ⊆ {propext, Quot.sound}; per-theorem
  `#print axioms` audited by `harness/lean_axiom_audit.py`), cross-checked
  against the Python core on the same hand-computed settlement vector
  (`mcp/thermo_crosscheck.py`). The dsh plugin face hosts the MCP server
  and injects the phantom-limb belief block as a system-prompt section
  (protocol text only, zero memory data). See `docs/thermo-generation.md`.

## Status: v0.x preview — aligned baseline (2026-11-27, morning register)

**This is an early preview.** Expect compatibility-breaking changes without
notice. The core chain runner module is staged for a following release; the
recompute path is fully functional. No public verdict claims are made from
this repository until the terminal review of the experiment series; negative
results are registered as-is (no gate tuning, no re-run to fill).

The project's three repositories are aligned on one baseline:

| Component | Baseline | Where |
|---|---|---|
| Release (stable) | tag `v0.1.0-preview.11` → commit `5efc158` (CI green; the commit the paper's Access section cites) | the plugin repository `zeroandcat/dsh-plugin-deposon` |
| Development frontier | commit `9219e78` (preview.12) on branch `b/organ-v311-preview11`, on top of `6110448` (executor-integrated driver `harness/deepen_r33.py`, CPU self-test `harness/selftest_p3_driver.py`, horizon slot calculator `harness/horizon_slot_calc_v2.py`; verified code unchanged, diff 0 bytes): adds the update/upgrade path, the ledger-era handshake server half, lazy executor imports and re-pinned self-tests; the README "Update / upgrade" section ships with it; local-commit-only — its push and any tag movement await a project-owner decision | the plugin repository |
| Pinned ignition components | `irreversible_executor.py` `d2189f2c4f1e585e` · `thermo_core.py` `f47d4ab7700c4533` · executor self-test, pinned copy `62cb86c40a805b56` · Lean companion `IrreversibleDeposon.lean` `0decb3a4059fd9e4` (58 theorems) | the plugin repository / registered in the criteria file |
| Experiment criteria | `criteria_v3` v1.2 frozen (`9d10c2b3b4c577f7`) plus the numeric backfill v1.2.1 (`horizon.value = 12`, `46e057711035e9b3`); gates G-C1 / G-A2 / G-A3 / G-B; validator verdicts registered 2026-11-27 morning (see Experiment status) | registered in the experiment receipt packs; not stored in this repository |
| Manuscript | revision 4.17 (commit `2c8252f`, tex `582031697650be00`, 530 lines, 30 pages) of the v5preR3 manuscript, frozen as FREEZE v13 at the branch tip `dea75bc`, on branch `private/v5preR3` of the public repository `zeroandcat/Deposon` (77 commits; not merged into that repository's `main` — unrelated histories, editorial decision pending) | the public repository |
| Experiment status | the two-host three-arm chain (A: executor + honest signal · B: executor + inverse signal · C: frozen / legacy backend) completed on both hosts (six arms, exit 0, guard 0 ALERT, automatic shutdown after the chain); the readings validator (criteria v1.2.1) verdicts are registered as-is: main gate G-A2 not passed (probe hits 0/256 on both executor arms — negative result), G-A3 / G-B not passed, the structural (true dual-binding) positions all pass, G-C1 out-of-band and registered in parallel to the confirmation rounds (re-judgement requires a new criteria freeze, pending); same seed replicated across hosts (probe hits 0 on all six machine-arms) | — |
| dsh compatibility | implemented in the development frontier `9219e78` (preview.12): `node plugin/update.mjs selfcheck|plan|apply|rollback` under the four-pillar contract (version single-source, capped engines ranges, additive-only config, append-only ledger data never migrated, code-face rollback snapshots); the MCP server self-reports its ledger era (`initialize` → `era` / `executorConfigDigest`), era mismatch fail-louds (anti crosstalk) | the plugin repository |

Point-in-time handoff: [HANDOFF.md](HANDOFF.md).

> **Companion plugin (dsh)**: the memory-probe harness ships as a DeepSeek Harness
> plugin — [`zeroandcat/dsh-plugin-deposon`](https://github.com/zeroandcat/dsh-plugin-deposon)
> (tag `v0.1.0-preview.11`, branch `b/organ-v311-preview11` ahead at `9219e78` = preview.12,
> local-commit-only). Install: `dsh plugin add https://github.com/zeroandcat/dsh-plugin-deposon`;
> update/upgrade follows the four-pillar contract (`node plugin/update.mjs plan|apply|rollback` —
> version single-source, capped engines ranges, additive-only config, append-only ledger data
> never migrated, code-face rollback snapshots). The MCP server self-reports its ledger era
> (`initialize` → `era: "executor" | "preview.10"`); era mismatch fail-louds (anti crosstalk).

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

**Thermo face (preview.10).** The same bundle entry hosts the memory organ:
the living-water tools `deposon_memory_write` / `deposon_memory_read`, the
self-settling `deposon_thermo_audit` (read-only) and `deposon_thermo_settle`
(`close=true` = unit close-out, U→0) are forwarded to `mcp/mcp_server.py`
over stdio JSON-RPC (one lazily spawned child, respawned if it exits); the
phantom-limb belief block (`mcp/phantom_limb.zh.txt` / `.en.txt`, protocol
text only) is injected as a system-prompt section and a counts-only brief
(live rows / phantom limbs) as runtime context; `/deposon-belief` prints the
block, `/deposon-thermo-audit` runs the audit. Every write/read receipt
carries a thermodynamic footer (Φ / R / D / U · dissipation utilisation).
Configuration keys: `ledger` (default `~/.deposon/ledger.jsonl`, survives
model swaps), `lang` (`zh|en|both`), `belief`, `brief`, `footer`, `thermo`
(JSON parameter override), `toolTimeoutMs`; env overrides
`DEPOSON_LEDGER`, `DEPOSON_PL_LANG`, `DEPOSON_BELIEF`,
`DEPOSON_THERMO_BRIEF`, `DEPOSON_THERMO_FOOTER`, `DEPOSON_THERMO`,
`DEPOSON_TOOL_TIMEOUT_MS`. The gate-check surface is untouched.

Desk-level install verification (no network beyond GitHub): `npm pack
--dry-run` (packaged bundle integrity), `git ls-remote` (the reachability
precheck dsh's plugin manager runs before installing), and
`node tests/test_plugin_load.mjs` (loads the plugin on a mock Cordis context
carrying the dsh-native `ctx.tools.register` / `ctx.systemPrompt` registries,
asserts tool-schema parity against the live MCP `tools/list`, and actually
invokes the tool bodies — 34 checks, including a real ledger round trip
write → read → audit → settle close → phantom limb, and running the gates
self-test).

> Preview-era note: dsh is a developer preview with announced
> compatibility-breaking changes. The `apply` contract, bundle declaration,
> and config consumption here are the stable surface; agent-tool registration
> probes known API shapes defensively.

## Quickstart (recompute)

```bash
# one shot, no clone (fetches this repo via npm's git resolver, runs every
# gate self-test + the plugin-load smoke + packaging integrity):
npx -y github:zeroandcat/dsh-plugin-deposon#v0.1.0-preview.10

# score a readings package against the 8 required contents (exit 0 = complete):
python gates/readout_completeness.py /path/to/readings-package            # JSON verdict
python gates/readout_completeness.py /path/to/readings-package --run-recompute   # + identity check

# with a readings package directory at hand:
READINGS_PACKAGE_DIR=/path/to/readings-package python scripts/g6f_recalc.py
# gate arithmetic self-test (pure math, no data needed):
python tests/test_gates.py

# thermodynamic ledger (preview.10): before/after on the same frozen 500-op trace
# (utilisation 0 % -> 69.23 %, hit rate 50.31 % -> 47.85 %, phantom lines 2.45 %):
python mcp/thermo_demo.py
# Lean <-> Python conservation cross-check on the hand-computed settlement vector:
python mcp/thermo_crosscheck.py
# per-theorem axiom audit (compiles DeposonThermo.lean when `lean` is on PATH):
python harness/lean_axiom_audit.py
```

## Repository layout

| path | content |
|---|---|
| `harness/` | launch-family entry points (env-parameterized) + `NingziContainer.lean` (condensate-field container, Lean 4 formalization, core-only) + `DeposonThermo.lean` (thermodynamic ledger conservation, 15 theorems, per-theorem `#print axioms`; `lean_axiom_audit.py` audits the compile log) |
| `mcp/` | memory harness proper as a standalone stdio MCP instance: core layer (external append-only ledger, DR-4 render surface) + thermodynamic layer (`thermo_core.py`: four-account exergy, gate, phantom limb, self-settling) + `deposon_memory_write`/`deposon_memory_read`/`deposon_thermo_audit`/`deposon_thermo_settle` tool surface + phantom-limb belief block (`phantom_limb.*.txt`) + `thermo_cli.py` + before/after demo (`thermo_demo.py`) + self-test and cross-checks (all run in CI) |
| `plugin/` | dsh plugin entry (Cordis `apply(ctx, config)`): gate-check surface + thermo face (hosts the MCP server over stdio, registers the four tools on `ctx.tools`, injects the belief block on `ctx.systemPrompt`) |
| `frozen/` | frozen faces (blind K_h mapping, seed) |
| `gates/` | gate specifications: Lean + Python dual implementations, incl. judgment-line v1.1 interfaces (gauge / raw-full / three-band), the preview.5 judge-strictness gauge + six-family linkage validator, and the preview.7 slot-space caliber gauge (six-family table fully linked in preview.8; see `docs/judgment-v12-strictness.md`, `docs/family-linkage.md`, `docs/slot-space-caliber.md`) |
| `cordis.patch.yml` | dsh bundle declaration (profile patch consumed by dsh plugin manager) |
| `package.json` | npm package: dsh plugin metadata (`dsh.bundle.patch`, `engines.dsh`) |
| `mocks/` | mock certifications incl. PC-lockin negative control |
| `scripts/` | recompute script family |
| `docs/` | evidence-round pointers, locked-baseline spec, package spec, alignment map, thermodynamic-generation change note (`thermo-generation.md`) |
| `BENCHMARK.md` | gate table & joint-readings disclosure |
| `SAFETY.md` | run-safety clauses (PR-1/2/3, stop-loss semantics) |

Readings data never enters this repository (artifacts policy, see
`.gitignore` and `CONTRIBUTING.md`).

## Documentation

- [BENCHMARK.md](BENCHMARK.md) - gates, formalized criteria, plugin validity
- [SAFETY.md](SAFETY.md) - protection clauses & stop-loss semantics
- [CONTRIBUTING.md](CONTRIBUTING.md) - ground rules for contributions
- [README.zh.md](README.zh.md) - Chinese README (中文说明)
- [HANDOFF.md](HANDOFF.md) - point-in-time handoff (2026-11-27)
- [docs/thermo-generation.md](docs/thermo-generation.md) - preview.10 change note: dissipation-channel utilisation, self-settling ledger path, the hit-rate price and phantom-limb readback
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
