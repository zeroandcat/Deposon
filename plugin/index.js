// dsh-plugin-deposon — Cordis plugin entry for DeepSeek Harness (dsh).
//
// Everything-is-a-plugin contract: this module named-exports `apply(ctx, config)`.
// When the Cordis loader mounts the bundle entry declared in cordis.patch.yml,
// it calls `apply` with a context through which the plugin registers what it
// contributes. The plugin exposes the deposon pre-registered gates self-test
// (pure arithmetic, no external data, no network) as an agent-callable surface.
//
// Preview-era note: dsh is in developer preview with announced breaking
// changes. Tool-registration APIs are probed defensively across known shapes;
// the Cordis `apply` contract and config consumption are the stable surface.

import { spawn } from 'node:child_process'
import { fileURLToPath } from 'node:url'
import path from 'node:path'

export const name = 'dsh-plugin-deposon'

export const usage = `
deposon memory-probe harness for dsh:
- deposon-gate-check / deposon_gate_check: run the pre-registered gates
  arithmetic self-test (tests/test_gates.py — pure math, no external data).
Configuration (via cordis.patch.yml config or DEPOSON_* env):
- python: interpreter to use (default "python3", env DEPOSON_PYTHON)
- timeoutMs: self-test timeout in ms (default 120000, env DEPOSON_TIMEOUT_MS)
`.trim()

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')

export function apply(ctx, config = {}) {
  const env = process.env
  const opts = {
    python: config.python ?? env.DEPOSON_PYTHON ?? 'python3',
    timeoutMs: Number(config.timeoutMs ?? env.DEPOSON_TIMEOUT_MS ?? 120000),
    script: config.script ?? path.join(ROOT, 'tests', 'test_gates.py'),
  }

  const registered = []

  // Tool body: spawn the gates self-test and return a structured result.
  function gateCheck() {
    return new Promise((resolve) => {
      const child = spawn(opts.python, [opts.script], {
        cwd: ROOT,
        stdio: ['ignore', 'pipe', 'pipe'],
      })
      let out = ''
      let err = ''
      const timer = setTimeout(() => {
        child.kill('SIGKILL')
      }, opts.timeoutMs)
      child.stdout.on('data', (d) => { out += d })
      child.stderr.on('data', (d) => { err += d })
      child.on('error', (e) => {
        clearTimeout(timer)
        resolve({ ok: false, error: `spawn failed: ${e?.message ?? e}` })
      })
      child.on('close', (code, signal) => {
        clearTimeout(timer)
        resolve({
          ok: code === 0,
          exitCode: code,
          signal: signal ?? null,
          command: `${opts.python} ${opts.script}`,
          stdoutTail: out.slice(-4000),
          stderrTail: err.slice(-2000),
        })
      })
    })
  }

  // Surface 1 — Cordis command (Koishi-lineage standard): /deposon-gate-check
  try {
    if (typeof ctx.command === 'function') {
      const cmd = ctx.command(
        'deposon-gate-check',
        'run the deposon pre-registered gates arithmetic self-test (pure math, no external data)',
      )
      if (cmd && typeof cmd.action === 'function') {
        cmd.action(() => gateCheck())
        registered.push('ctx.command#deposon-gate-check')
      }
    }
  } catch (e) {
    ctx?.logger?.warn?.(`deposon: command registration skipped: ${e?.message ?? e}`)
  }

  // Surface 2 — dsh agent-tool APIs (preview-era variance: probe known shapes).
  for (const key of ['tool', 'tools', 'agentTools']) {
    try {
      const surface = ctx?.[key]
      if (!surface) continue
      const spec = {
        name: 'deposon_gate_check',
        description: 'Run the deposon pre-registered gates arithmetic self-test (pure math, no external data, no network)',
        invoke: () => gateCheck(),
      }
      if (typeof surface.add === 'function') {
        surface.add(spec)
        registered.push(`ctx.${key}.add#deposon_gate_check`)
        break
      }
      if (typeof surface.register === 'function') {
        surface.register(spec)
        registered.push(`ctx.${key}.register#deposon_gate_check`)
        break
      }
    } catch (e) {
      // defensive: preview-era API drift must not break plugin load
    }
  }

  // Lifecycle: observable evidence that the bundle mounted.
  try {
    ctx.on?.('ready', () => {
      ctx.logger?.info?.(
        `dsh-plugin-deposon mounted (surfaces: ${registered.join(', ') || 'none'})`,
      )
    })
  } catch (e) { /* lifecycle optional */ }

  return { root: ROOT, registered, gateCheck }
}
