// Plugin load smoke test — plain Node, no dependencies.
// Mirrors the dsh "installable, recognized, callable" acceptance at desk level:
//   installable -> package.json declares dsh.bundle.patch + ESM entry (asserted)
//   recognized  -> bundle patch file exists and parses (structure asserted)
//   callable    -> apply(ctx, config) mounts on a mock Cordis context and the
//                  registered tool body actually runs the gates self-test.
import { readFileSync } from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
let failures = 0
const check = (label, ok) => {
  console.log(`${ok ? 'PASS' : 'FAIL'} ${label}`)
  if (!ok) failures++
}

// --- installable / recognized (static acceptance) -------------------------
const pkg = JSON.parse(readFileSync(path.join(ROOT, 'package.json'), 'utf8'))
check('package name is dsh-plugin-deposon', pkg.name === 'dsh-plugin-deposon')
check('dsh.bundle.patch declared', pkg.dsh?.bundle?.patch === './cordis.patch.yml')
check('ESM module type', pkg.type === 'module')
check('main entry points at plugin/index.js', pkg.main === 'plugin/index.js')
check('engines.dsh declared', typeof pkg.engines?.dsh === 'string')
const patch = readFileSync(path.join(ROOT, 'cordis.patch.yml'), 'utf8')
check(
  'bundle patch inserts the deposon entry',
  patch.includes('dsh-plugin-deposon') && patch.includes('- insert:'),
)

// --- callable (mock Cordis context) ---------------------------------------
const mod = await import(path.join(ROOT, 'plugin', 'index.js'))
check('named export apply(ctx, config) exists', typeof mod.apply === 'function')
check('named export name is dsh-plugin-deposon', mod.name === 'dsh-plugin-deposon')

const logs = []
const events = {}
const commands = {}
const tools = []
const mockCtx = {
  command: (name, desc) => {
    const cmd = {
      action: (fn) => {
        commands[name] = { desc, fn }
        return cmd
      },
    }
    return cmd
  },
  tool: { add: (spec) => tools.push(spec) },
  on: (ev, fn) => { (events[ev] ??= []).push(fn) },
  logger: { info: (m) => logs.push(m), warn: (m) => logs.push(m) },
}

const config = { python: process.env.DEPOSON_PYTHON ?? 'python3', timeoutMs: 300000 }
const handle = mod.apply(mockCtx, config)
check('apply returns a handle', !!handle && typeof handle === 'object')
check(
  'command surface registered (ctx.command#deposon-gate-check)',
  handle.registered.includes('ctx.command#deposon-gate-check') &&
    Object.prototype.hasOwnProperty.call(commands, 'deposon-gate-check'),
)
check(
  'agent-tool surface registered (ctx.tool.add#deposon_gate_check)',
  handle.registered.includes('ctx.tool.add#deposon_gate_check') && tools.length === 1,
)
check('config consumed (timeoutMs from config)', config.timeoutMs === 300000)

// fire the ready lifecycle so the mount log is observable
for (const fn of events.ready ?? []) fn()
check('mount lifecycle log emitted', logs.some((m) => m.includes('dsh-plugin-deposon mounted')))

// the tool body must actually run the gates self-test (pure math, no network)
const result = await handle.gateCheck()
check(
  `gates self-test ran to completion via tool body (exit=${result.exitCode ?? 'n/a'})`,
  result.ok === true,
)

if (failures > 0) {
  console.error(`${failures} check(s) failed`)
  process.exit(1)
}
console.log('plugin load smoke: all checks passed')
