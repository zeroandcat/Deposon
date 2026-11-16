#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# ledger_crosscheck.py — dual-implementation cross-check of the ledger core.
# ----------------------------------------------------------------------------
# Lean side   : harness/CondensateLedger.lean (T1-T6, machine-checked,
#               lean 4.15.0 core-only, 0 sorry).
# Python side : mcp_server.py core primitives (write_entry / read_entries) and
#               the MCP dispatch render path.
# This script runs concrete vectors through the Python core and asserts the
# same six properties. Zero network, zero credentials; uses a throwaway
# temporary ledger (removed on exit).
# Usage: python3 mcp/ledger_crosscheck.py   (exit 0 = ALL PASS)
# ============================================================================
import os, sys, json, shutil, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def tool_call(module, name, args):
    """Invoke one MCP tools/call through the real dispatch (render path)."""
    req = {"jsonrpc": "2.0", "id": 1, "method": "tools/call",
           "params": {"name": name, "arguments": args}}
    out = module.handle(req)
    if "error" in out:
        raise RuntimeError("tool error: %s" % out["error"])
    return out["result"]


def main():
    tmpdir = tempfile.mkdtemp(prefix="condensate_ledger_xcheck_")
    ledger = os.path.join(tmpdir, "ledger.jsonl")
    # CONDENSATE_LEDGER must be set before importing mcp_server (module-level
    # path resolution).
    os.environ["CONDENSATE_LEDGER"] = ledger
    import mcp_server as core

    ok = True

    def check(name, cond):
        nonlocal ok
        print("  [%s] %s" % ("PASS" if cond else "FAIL", name))
        ok = ok and bool(cond)

    try:
        # ---- T2 prelude: empty ledger reads cleanly -----------------------
        hits0, _ = core.read_entries("")
        check("T2-pre empty read ok", hits0 == [])

        # ---- T1: write visibility (fresh writes visible under prefix) -----
        core.write_entry("alpha.beta", "hello")
        core.write_entry("alpha.gamma", "world")
        core.write_entry("other.delta", "x")
        r1, _ = core.read_entries("alpha.")
        check("T1 fresh writes visible under prefix",
              [h["key"] for h in r1] == ["alpha.beta", "alpha.gamma"])

        # ---- T6: prefix-filter soundness -----------------------------------
        check("T6 every hit key carries the prefix",
              all(h["key"].startswith("alpha.") for h in r1))
        rn, _ = core.read_entries("zzz.")
        check("T6 non-matching prefix yields no hits", rn == [])

        # ---- T2: read monotonicity (appends never remove earlier hits) ----
        rendered_before = ["%s: %s" % (h["key"], h["text"]) for h in r1]
        core.write_entry("alpha.delta", "more")
        r2, _ = core.read_entries("alpha.")
        rendered_after = ["%s: %s" % (h["key"], h["text"]) for h in r2]
        check("T2 monotone (prior hits survive appends)",
              all(x in rendered_after for x in rendered_before))

        # ---- T3: corrupt lines tolerated and invisible ---------------------
        snap_before, _ = core.read_entries("")
        with open(ledger, "a", encoding="utf-8") as f:
            f.write("{this line is not valid json\n")   # corrupt line
            f.write("\n")                                # blank line
        snap_after, _ = core.read_entries("")
        check("T3 corrupt/blank lines skipped, read unaffected",
              snap_before == snap_after)

        # ---- T5 + T4: DR-4 render surface via the real dispatch path -------
        marker = "TS-MARKER-XYZ-DO-NOT-RENDER"
        with open(ledger, "a", encoding="utf-8") as f:
            f.write(json.dumps({"key": "dr4.probe", "text": "surface",
                                "ts": marker}, ensure_ascii=False) + "\n")
        res = tool_call(core, "deposon_memory_read", {"prefix": "dr4."})
        blob = "\n".join(part["text"] for part in res.get("content", []))
        check("T5 DR-4 metadata (ts) absent from render surface",
              marker not in blob)
        check("T4 render surface is exactly `key: text` lines",
              "dr4.probe: surface" in blob and "{" not in blob and "]" not in blob)

        print("ledger_crosscheck:", "ALL PASS" if ok else "FAIL")
        return 0 if ok else 1
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
