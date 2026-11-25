// Plugin load smoke test — plain Node, no dependencies.
// Mirrors the dsh "installable, recognized, callable" acceptance at desk level:
//   installable -> package.json declares dsh.bundle.patch + ESM entry (asserted)
//   recognized  -> bundle patch file exists and parses (structure asserted)
//   callable    -> apply(ctx, config) mounts on a mock Cordis context and the
//                  registered tool body actually runs the gates self-test.
// preview.10 thermo face: the mock context carries the dsh-native registries
// (`ctx.tools.register`, `ctx.systemPrompt.section/context`); the test asserts the
// belief block injection, tool-schema parity against the live MCP `tools/list`, and a
// real ledger round trip (write -> read -> audit -> settle close -> phantom limb).
import { readFileSync, mkdtempSync, rmSync } from 'node:fs'
import os from 'node:os'
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
const PATCH_KEYS = ['python', 'timeoutMs', 'ledger', 'lang', 'belief', 'brief', 'footer', 'thermo', 'toolTimeoutMs']
check(
  'bundle patch carries the thermo face config keys',
  PATCH_KEYS.every((k) => new RegExp(`^\\s+${k}:`, 'm').test(patch)),
)

// --- callable (mock Cordis context) ---------------------------------------
const mod = await import(path.join(ROOT, 'plugin', 'index.js'))
check('named export apply(ctx, config) exists', typeof mod.apply === 'function')
check('named export name is dsh-plugin-deposon', mod.name === 'dsh-plugin-deposon')

const logs = []
const events = {}
const commands = {}
const tools = []
const dshTools = []
const sections = []
const contexts = []
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
  tools: { register: (def) => dshTools.push(def) },
  systemPrompt: {
    section: (s) => sections.push(s),
    context: (c) => contexts.push(c),
  },
  on: (ev, fn) => { (events[ev] ??= []).push(fn) },
  logger: { info: (m) => logs.push(m), warn: (m) => logs.push(m) },
}

const tmpd = mkdtempSync(path.join(os.tmpdir(), 'deposon-plugin-'))
const ledger = path.join(tmpd, 'ledger.jsonl')
const config = {
  python: process.env.DEPOSON_PYTHON ?? 'python3',
  timeoutMs: 300000,
  ledger,
  lang: 'zh',
}
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

// --- thermo face (preview.10) ----------------------------------------------
const THERMO_NAMES = [
  'deposon_memory_write',
  'deposon_memory_read',
  'deposon_thermo_audit',
  'deposon_thermo_settle',
]
const def = (name) => dshTools.find((d) => d.name === name)
const text = async (name, args) => {
  const d = def(name)
  if (!d) throw new Error(`tool not registered: ${name}`)
  const value = await d.execute(args ?? {}, { signal: new AbortController().signal })
  return d.output.render(args ?? {}, value).map((b) => b.text).join('\n')
}

check(
  'gate_check untouched (still the only ctx.tool.add entry, same description)',
  tools.length === 1 &&
    tools[0].name === 'deposon_gate_check' &&
    tools[0].description.startsWith('Run the deposon pre-registered gates arithmetic self-test'),
)
check(
  'thermo tools registered through ctx.tools.register (4/4)',
  THERMO_NAMES.every((n) => handle.registered.includes(`ctx.tools.register#${n}`)) &&
    dshTools.map((d) => d.name).join(',') === THERMO_NAMES.join(','),
)
check(
  'thermo face config consumed (ledger path, lang)',
  handle.thermo.ledger === ledger && handle.thermo.lang === 'zh',
)

// belief block: injected as a system-prompt section, single text source, 0 memory data
const zhText = readFileSync(path.join(ROOT, 'mcp', 'phantom_limb.zh.txt'), 'utf8')
const beliefSection = sections.find((s) => s.name === 'deposon:phantom-belief')
check(
  'belief block injected as system-prompt section (text = mcp/phantom_limb.zh.txt, interpolate off)',
  !!beliefSection &&
    typeof beliefSection.text === 'string' &&
    beliefSection.text === zhText &&
    beliefSection.interpolate === false &&
    typeof beliefSection.order === 'number',
)
check(
  'belief block states the organ, the phantom limb and the self-settling ledger (0 memory data)',
  !!beliefSection &&
    beliefSection.text.includes('活水记忆层') &&
    beliefSection.text.includes('⟨幻肢⟩') &&
    beliefSection.text.includes('自解帐本') &&
    beliefSection.text.includes('deposon_thermo_audit') &&
    !/已散失·不可复原（曾 \d+ 字/.test(beliefSection.text),
)
check(
  'counts-only brief registered as runtime context (empty until a ledger exists)',
  contexts.length === 1 &&
    contexts[0].name === 'deposon:thermo-brief' &&
    contexts[0].required === false &&
    contexts[0].text() === '',
)
check(
  'human commands registered (deposon-belief, deposon-thermo-audit)',
  handle.registered.includes('ctx.command#deposon-belief') &&
    handle.registered.includes('ctx.command#deposon-thermo-audit') &&
    commands['deposon-belief'].fn() === zhText,
)

// tool-schema parity against the live MCP server (drift guard for the static mirror)
const live = await handle.thermo.client.listTools()
const liveTools = live.tools ?? []
check(
  'static tool mirror == live MCP tools/list (names, descriptions, input schemas)',
  liveTools.length === THERMO_NAMES.length &&
    liveTools.every((t) => {
      const d = def(t.name)
      return d && d.description === t.description && JSON.stringify(d.parameters) === JSON.stringify(t.inputSchema)
    }),
)

// real ledger round trip through the plugin's tool bodies
const w1 = await text('deposon_memory_write', { key: 'user.drink', text: '咖啡·不加糖' })
const w2 = await text('deposon_memory_write', { key: 'habit.rest', text: '23 点前睡' })
const w3 = await text('deposon_memory_write', { key: 'project.alpha', text: '周四周审' })
check(
  'write x3 lands (append-only ledger, receipts carry the thermodynamic footer)',
  [w1, w2, w3].every((t) => t.includes('耗散通道利用率')) && (await text('deposon_memory_read', { prefix: 'user.' })).includes('user.drink: 咖啡·不加糖'),
)
const all = await text('deposon_memory_read', { prefix: '' })
check('read all renders exactly the 3 live rows (key: text lines)', ['user.drink:', 'habit.rest:', 'project.alpha:'].every((k) => all.split('\n').some((l) => l.startsWith(k))))
const auditJson = JSON.parse(await text('deposon_thermo_audit', { format: 'json' }))
check(
  'audit (json): self-consistent conservation core, 3 live rows, 0 dissipation yet',
  auditJson.verdict === 'SELF-CONSISTENT' &&
    auditJson.live_rows === 3 &&
    auditJson.E0 === auditJson.phi + auditJson.R + auditJson.D + auditJson.U &&
    auditJson.D === 0,
)
const auditText = await text('deposon_thermo_audit', {})
check(
  'audit (text): verdict + four accounts + utilisation line',
  auditText.includes('自洽（E⁰=Φ+R+D+U 逐位成立）') && auditText.includes('＋ R 0 ＋ D 0 ＋ U') &&
    auditText.includes('耗散通道利用率 D/E⁰行') && /调用账 读 2 · 透射 4 · 拒绝 0/.test(auditText),
)
const closed = await text('deposon_thermo_settle', { close: true })
const after = JSON.parse(await text('deposon_thermo_audit', { format: 'json' }))
check(
  'settle close: unit close-out, U=0, E0 = Φ+R+D, self-settled (no external reconciliation)',
  closed.includes('单元终核') && after.U === 0 && after.live_rows === 0 &&
    after.E0 === after.phi + after.R + after.D && after.verdict === 'SELF-CONSISTENT' &&
    after.D_by.close > 0,
)
const phantom = await text('deposon_memory_read', { prefix: 'user.' })
check(
  'phantom limb: dissipated memory is reflected as ⟨幻肢⟩ (felt, 0 source text replayed)',
  phantom.includes('⟨幻肢⟩') && phantom.includes('已散失') && !phantom.includes('咖啡'),
)
const replant = await text('deposon_memory_write', { key: 'user.drink', text: '茶·热' })
const reread = await text('deposon_memory_read', { prefix: 'user.' })
check(
  're-plant after dissipation: new row live, same-key phantom shadowed',
  replant.includes('user.drink') && reread.includes('user.drink: 茶·热') && !reread.includes('咖啡'),
)
// the brief is refreshed asynchronously (child spawn) — poll briefly for the cache
for (let i = 0; i < 50 && contexts[0].text() === ''; i++) await new Promise((r) => setTimeout(r, 100))
check(
  'runtime context brief refreshed after tool calls (counts only, no row text)',
  /幻肢/.test(contexts[0].text()) && !contexts[0].text().includes('茶'),
)
check(
  'deposon-thermo-audit command returns the audit text',
  (await commands['deposon-thermo-audit'].fn()).includes('耗散通道利用率'),
)

// error path: MCP isError (bad argument / unknown tool) surfaces as a thrown error in
// the dsh tool body (fail-loud, never silently passes)
let threw = ''
try {
  await def('deposon_thermo_settle').execute({ close: 'not-a-bool' }, { signal: new AbortController().signal })
} catch (e) { threw = e?.message ?? String(e) }
const unknown = await handle.thermo.call('deposon_no_such_tool', {})
check(
  'MCP isError never silently passes (bad close arg throws; unknown tool -> isError)',
  threw.includes('close 须为布尔') && unknown.isError === true && unknown.content?.[0]?.text?.includes('未知工具'),
)

// dispose stops the hosted MCP child
const childBefore = handle.thermo.client.child
for (const fn of events.dispose ?? []) fn()
check(
  'dispose stops the hosted MCP server child',
  !!childBefore && handle.thermo.client.child === null,
)
handle.thermo.stop()
rmSync(tmpd, { recursive: true, force: true })

if (failures > 0) {
  console.error(`${failures} check(s) failed`)
  process.exit(1)
}
console.log('plugin load smoke: all checks passed')
