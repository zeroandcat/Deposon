#!/usr/bin/env node
// quickcheck.mjs — one-shot fetch-and-run entry (preview.9).
// Runs from the installed package root regardless of the caller's cwd:
// packaging integrity + every gate self-test + the MCP ledger self-test + the
// dsh plugin-load smoke. Zero network beyond the initial npm git fetch.
// Exit 0 only if every step passes. Python: $DEPOSON_PYTHON, else python3/python.
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import path from "node:path";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
process.chdir(root);

function has(cmd) { return spawnSync(cmd, ["--version"], { stdio: "ignore" }).status === 0; }
const PY = process.env.DEPOSON_PYTHON || (has("python3") ? "python3" : "python");

const quiet = process.argv.includes("--quiet");
const steps = [
  ["packaging integrity (npm pack --dry-run)", "npm", ["pack", "--dry-run"], true],
  ["compile all Python sources", PY, ["-m", "compileall", "-q", "harness", "gates", "mocks", "scripts", "tests"], true],
  ["gate arithmetic self-test (incl. preview.5/7/8/9 interfaces)", PY, ["tests/test_gates.py"]],
  ["judgment-line v1.1 interfaces", PY, ["gates/judgment_v11.py"]],
  ["judge-strictness gauge", PY, ["gates/judgment_strictness.py"]],
  ["six-family linkage", PY, ["gates/family_linkage.py"]],
  ["slot-space caliber gauge", PY, ["gates/slot_space_caliber.py"]],
  ["slot-space caliber Lean mirror cross-check", PY, ["gates/slot_space_crosscheck.py"]],
  ["f3 judge calibration face", PY, ["gates/descrev_calibration.py"]],
  ["readings-package completeness validator", PY, ["gates/readout_completeness.py"]],
  ["memory harness MCP self-test (stdio)", PY, ["mcp/selftest_mcp.py"]],
  ["ledger dual-implementation cross-check", PY, ["mcp/ledger_crosscheck.py"]],
  ["dsh plugin load smoke (mock Cordis context)", process.execPath, ["tests/test_plugin_load.mjs"]],
];

let failed = 0;
for (const [name, cmd, args, hideStdout] of steps) {
  const t0 = Date.now();
  const r = spawnSync(cmd, args, { encoding: "utf8", env: process.env, cwd: root });
  const ok = r.status === 0;
  if (!ok) failed += 1;
  const tail = (r.stdout + "\n" + r.stderr).trim().split("\n").filter(Boolean);
  const last = hideStdout ? "" : "  | " + tail[tail.length - 1].slice(0, 140);
  console.log(`${ok ? "PASS" : "FAIL"} ${name} (${((Date.now() - t0) / 1000).toFixed(1)}s)${last}`);
  if (!ok && !quiet) console.log((r.stdout + "\n" + r.stderr).split("\n").slice(-25).join("\n"));
}
console.log(`QUICKCHECK: ${failed === 0 ? "ALL PASS" : "FAILED (" + failed + ")"}` + ` (${steps.length} steps, ${root})`);
process.exit(failed === 0 ? 0 : 1);
