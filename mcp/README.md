# condensate-field MCP instance (memory harness proper)

A standalone stdio instance of the condensate-field memory container: **the
memory harness proper, not just agent-facing tools.** Since preview.10
(phantom-limb generation) the container carries a thermodynamic layer.

## Layering

| Layer | Files | Runs |
|---|---|---|
| **Core (harness proper)** | `mcp_server.py` primitives `write_entry` / `read_entries` / `thermo_audit` / `thermo_settle` over `thermo_core.ThermoLedger` | `import`-direct, zero transport dependencies |
| **Thermodynamic core** | `thermo_core.py` — integer exergy per row, four accounts Φ / R / D / U, gate, five dissipation paths, phantom limb, self-settling replay | pure Python 3.7+ stdlib, deterministic |
| **Phantom-limb belief block** | `phantom_limb.py` + `phantom_limb.zh.txt` / `phantom_limb.en.txt` (protocol text only, zero memory data) | injected via `initialize.instructions`, tool descriptions, receipts; the dsh plugin face reads the same text files |
| **Interface (MCP surface)** | `mcp_server.py` JSON-RPC dispatch | stdio, one JSON object per line, MCP `2024-11-05` |
| **Command face** | `thermo_cli.py` (`audit` / `settle [--close]` / `brief` / `belief`) | CLI, exit 0 = self-consistent, 3 = fail-loud |

The core layer is the container itself: an external append-only JSONL ledger
(fsync'd, corruption-tolerant) plus the DR-4 render-surface semantics —
`read` returns rendered `key: text` lines only, never the raw ledger record
(no timestamps, no JSON). The MCP tool surface is a thin interface over it.

## Thermodynamic ledger (preview.10)

Every injected row holds integer exergy `Q`; every read spends query exergy.
The first law is attribution conservation, checked fail-loud after every
operation: `E⁰ = Φ + R + D + U` (injected + queried = transmitted + reflected
+ dissipated + in presence). Settlement is a pure replay of the event stream
(**self-settling**: no external reconciler; a forged or out-of-bounds event
raises `LedgerInconsistent`). Dissipation paths: gate rejection (the rejected
row pays `c_A` from its own `U`), period decay (`λ·Δtick` materialised at
settle), capacity eviction (coldest row), horizon (no transmit for `horizon`
ticks), supersede (same-key rewrite), unit close-out (`close=true`, `U→0`).
A dissipated row leaves a **phantom limb** (`⟨幻肢⟩` line: existed, now gone,
unrecoverable; key name / mass / cause / account only, zero source text)
which is reflected on reads for `phantom_ttl` ticks.

## Tools

| Tool | Arguments | Effect |
|---|---|---|
| `deposon_memory_write` | `{key, text}` | Append one entry (same-key rewrite dissipates the old version, leaving a phantom) |
| `deposon_memory_read`  | `{prefix, k?}`  | Gate: transmit at most `k` most relevant rows (others pay their own exergy into D); reflect up to `phantom_k` phantom lines; receipt carries the thermodynamic footer |
| `deposon_thermo_audit` | `{format?: text\|json}` | Read-only: four accounts, conservation core, dissipation utilisation `D/E⁰_rows`, causes, selectivity, call ledger |
| `deposon_thermo_settle` | `{close?: bool}` | Materialise decay + horizon dissipation, snapshot self-check; `close=true` = unit close-out (`U=0`) |

## Run

```
python3 mcp/mcp_server.py          # stdio JSON-RPC server (no args, no network)
python3 mcp/thermo_cli.py audit    # thermodynamic audit of the ledger
python3 mcp/thermo_cli.py settle --close   # unit close-out
```

Ledger location defaults to `mcp/ledger.jsonl` (git-ignored via `*.jsonl`);
override with the `CONDENSATE_LEDGER` environment variable (the dsh plugin
face defaults to `~/.deposon/ledger.jsonl`). Parameters: `DEPOSON_THERMO`
(JSON object over `thermo_core.DEFAULTS`). Footers: `DEPOSON_THERMO_FOOTER`.
Belief block language: `DEPOSON_PL_LANG` (`zh|en|both`). The ledger is the
persistence substrate: entries survive model swaps and process restarts.

## Self-test and cross-checks

```
python3 mcp/selftest_mcp.py        # zero network, zero credentials (25 assertions)
python3 mcp/ledger_crosscheck.py   # Lean CondensateLedger T1-T6 vs Python core
python3 mcp/thermo_crosscheck.py   # Lean DeposonThermo vs Python core (settlement vector)
python3 mcp/thermo_demo.py --check # frozen 500-op trace: utilisation 0 -> 69.23 %, hit 50.31 -> 47.85 %
```

Segment 0 exercises the core layer directly (import, no transport); segments
1-3 exercise the MCP surface (`initialize` / `tools/list` / `tools/call`);
the strong-survival check terminates and restarts the server process and
verifies identical readback (write 3 -> restart -> read 3/3 identical ->
append 2 -> read 5/5). Segments 5-7 cover the thermodynamic layer (gate
budget / rejection / phantom readback / settle / close-out / re-plant;
decay, horizon, supersede, eviction, replay determinism, forged-event
fail-loud; belief-block injection with zero data replay). All run in CI.
