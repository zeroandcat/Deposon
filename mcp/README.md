# condensate-field MCP instance (memory harness proper)

A standalone stdio instance of the condensate-field memory container: **the
memory harness proper, not just agent-facing tools.**

## Layering

| Layer | Files | Runs |
|---|---|---|
| **Core (harness proper)** | `mcp_server.py` primitives `write_entry` / `read_entries` | `import`-direct, zero transport dependencies |
| **Interface (MCP surface)** | `mcp_server.py` JSON-RPC dispatch | stdio, one JSON object per line, MCP `2024-11-05` |

The core layer is the container itself: an external append-only JSONL ledger
(fsync'd, corruption-tolerant) plus the DR-4 render-surface semantics —
`read` returns rendered `key: text` lines only, never the raw ledger record
(no timestamps, no JSON). The MCP tool surface is a thin interface over it.

## Tools

| Tool | Arguments | Effect |
|---|---|---|
| `deposon_memory_write` | `{key, text}` | Append one entry to the external ledger |
| `deposon_memory_read`  | `{prefix}`   | Read back rendered lines for keys with the given prefix |

## Run

```
python3 mcp/mcp_server.py          # stdio JSON-RPC server (no args, no network)
```

Ledger location defaults to `mcp/ledger.jsonl` (git-ignored via `*.jsonl`);
override with the `CONDENSATE_LEDGER` environment variable. The ledger is the
persistence substrate: entries survive model swaps and process restarts
(model-independent "in-register" memory).

## Self-test

```
python3 mcp/selftest_mcp.py        # zero network, zero credentials
```

Segment 0 exercises the core layer directly (import, no transport); segments
1-3 exercise the MCP surface (`initialize` / `tools/list` / `tools/call`);
the strong-survival check terminates and restarts the server process and
verifies identical readback (write 3 -> restart -> read 3/3 identical ->
append 2 -> read 5/5). This self-test also runs in CI.
