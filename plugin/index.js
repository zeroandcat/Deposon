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
import { existsSync, mkdirSync, readFileSync, statSync } from 'node:fs'
import os from 'node:os'
import { fileURLToPath } from 'node:url'
import path from 'node:path'

export const name = 'dsh-plugin-deposon'

export const usage = `
deposon memory-probe harness for dsh:
- deposon-gate-check / deposon_gate_check: run the pre-registered gates
  arithmetic self-test (tests/test_gates.py — pure math, no external data).
- thermo face (preview.10, living-water memory + phantom limb):
  tools deposon_memory_write / deposon_memory_read / deposon_thermo_audit /
  deposon_thermo_settle (forwarded to mcp/mcp_server.py over stdio JSON-RPC);
  commands deposon-belief (print the belief block) and deposon-thermo-audit;
  the phantom-limb belief block is injected as a system-prompt section and a
  counts-only brief (live rows / phantom limbs) as runtime context.
Configuration (via cordis.patch.yml config or DEPOSON_* env):
- python: interpreter to use (default "python3", env DEPOSON_PYTHON)
- timeoutMs: self-test timeout in ms (default 120000, env DEPOSON_TIMEOUT_MS)
- ledger: ledger path (default ~/.deposon/ledger.jsonl, env DEPOSON_LEDGER)
- lang: belief block language zh|en|both (default zh, env DEPOSON_PL_LANG)
- belief: inject the belief block (default true, env DEPOSON_BELIEF)
- brief: counts-only runtime context (default true, env DEPOSON_THERMO_BRIEF)
- footer: thermodynamic footer on write/read receipts (default true, env DEPOSON_THERMO_FOOTER)
- thermo: thermodynamic parameters as a JSON string (env DEPOSON_THERMO)
- toolTimeoutMs: per MCP request timeout in ms (default 60000, env DEPOSON_TOOL_TIMEOUT_MS)
`.trim()

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')

// ---------------------------------------------------------------------------
// Thermo face (preview.10): living-water memory organ + phantom-limb belief block.
//
// Single source of truth = mcp/mcp_server.py (stdio JSON-RPC 2.0, line-delimited).
// The plugin hosts it as a lazily spawned child and forwards every tool call to
// it, so the model sees exactly the MCP tool surface and one ledger semantics
// (gate, dissipation, phantom lines, self-settling conservation core). The
// static THERMO_TOOLS mirror of the server's TOOLS_SPEC is kept in parity by
// tests/test_plugin_load.mjs (live tools/list deep-equal).
// ---------------------------------------------------------------------------
const MCP_SERVER = path.join(ROOT, 'mcp', 'mcp_server.py')
const THERMO_CLI = path.join(ROOT, 'mcp', 'thermo_cli.py')
const MCP_PROTOCOL = '2024-11-05'
const BELIEF_SECTION = 'deposon:phantom-belief'
const BRIEF_CONTEXT = 'deposon:thermo-brief'
// dsh-system-prompt section orders: MCP_SERVERS 3100, TOOLS_SDK 5000; runtime
// contexts: SUBAGENT_DELEGATION 120, HARNESS_SOURCE 200 (see @deepseek-ai/dsh-system-prompt).
const BELIEF_ORDER = 3150
const BRIEF_ORDER = 130

const THERMO_TOOLS = [
  {
    name: 'deposon_memory_write',
    description:
      '凝子场凝华：向活水记忆账本写入一条记忆（key 点分层级定位·text 渲染位文本）。' +
      '追加式落盘·外置承载·换模不丢；同键重写＝旧版本散失（留幻肢）。',
    inputSchema: {
      type: 'object',
      properties: {
        key: { type: 'string', description: '条目键·点分层级（如 habit.morning）' },
        text: { type: 'string', description: '条目文本（渲染位内容）' },
      },
      required: ['key', 'text'],
    },
  },
  {
    name: 'deposon_memory_read',
    description:
      '凝子场检索：按键前缀回读活水记忆·返回渲染位文本（每行『key: text』）。' +
      '门只透射最相关的至多 k 条（其余被拒＝熵输出·自付㶲散失）；已散失的记忆以' +
      '『⟨幻肢⟩』行回射（可感不可复原）。0 原始账本注入（DR-4）。回执带热力学脚注。',
    inputSchema: {
      type: 'object',
      properties: {
        prefix: { type: 'string', description: '键前缀过滤（空串＝全账本）' },
        k: { type: 'integer', description: '门预算：至多透射的条数（缺省 8）' },
      },
      required: ['prefix'],
    },
  },
  {
    name: 'deposon_thermo_audit',
    description:
      'deposon 热力学审计（只读）：四账 Φ/R/D/U·守恒核·耗散通道利用率·散失成因·耗散选择性。' +
      '账本自检·不依赖外部对账。',
    inputSchema: {
      type: 'object',
      properties: {
        format: { type: 'string', enum: ['text', 'json'], description: '缺省 text' },
      },
    },
  },
  {
    name: 'deposon_thermo_settle',
    description:
      'deposon 结算（自解帐本）：物化期衰减＋视界散热（久未透射的记忆散失留幻肢）·' +
      '守恒核自检·落结算快照。close=true 为单元终核：全部在场记忆散失·U=0。',
    inputSchema: {
      type: 'object',
      properties: {
        close: { type: 'boolean', description: '单元终核（缺省 false）' },
      },
    },
  },
]

/** Model-facing text of one MCP tools/call result (text blocks joined by newline). */
function extractText(result) {
  const content = Array.isArray(result?.content) ? result.content : []
  return content
    .filter((c) => c && c.type === 'text' && typeof c.text === 'string')
    .map((c) => c.text)
    .join('\n')
}

/** Minimal stdio JSON-RPC client for the condensate-field MCP server (lazy spawn). */
class McpStdio {
  constructor(opts) {
    this.opts = opts
    this.child = null
    this.buf = ''
    this.errTail = ''
    this.pending = new Map()
    this.nextId = 1
    this.starting = null
  }

  get alive() {
    return !!(this.child && this.child.exitCode === null && !this.child.killed)
  }

  async start() {
    if (this.alive) return
    if (this.starting) return this.starting
    this.starting = (async () => {
      const child = spawn(this.opts.cmd, this.opts.args, {
        cwd: this.opts.cwd,
        stdio: ['pipe', 'pipe', 'pipe'],
        env: this.opts.env,
      })
      this.child = child
      child.stdout.setEncoding('utf8')
      child.stdout.on('data', (d) => this._onData(d))
      child.stderr.setEncoding('utf8')
      child.stderr.on('data', (d) => { this.errTail = (this.errTail + d).slice(-2000) })
      // A write after the child died surfaces on stdin; the exit handler rejects pending.
      child.stdin.on('error', () => {})
      child.on('error', (e) => this._fail(new Error(`deposon mcp spawn failed: ${e?.message ?? e}`)))
      child.on('exit', (code, signal) =>
        this._fail(new Error(`deposon mcp server exited (code=${code}, signal=${signal})`)))
      await this.request('initialize', {
        protocolVersion: MCP_PROTOCOL,
        capabilities: {},
        clientInfo: { name: 'dsh-plugin-deposon', version: '0.1.0-preview.10' },
      })
      this.notify('notifications/initialized')
    })()
    try {
      await this.starting
    } finally {
      this.starting = null
    }
  }

  _onData(d) {
    this.buf += d
    let i
    while ((i = this.buf.indexOf('\n')) >= 0) {
      const line = this.buf.slice(0, i).trim()
      this.buf = this.buf.slice(i + 1)
      if (!line) continue
      let msg
      try { msg = JSON.parse(line) } catch { continue }
      const id = msg?.id
      if (id === undefined || id === null) continue // server-side notification
      const p = this.pending.get(id)
      if (!p) continue
      this.pending.delete(id)
      clearTimeout(p.timer)
      if (msg.error) {
        p.reject(new Error(`deposon mcp ${p.method}: ${msg.error.message ?? JSON.stringify(msg.error)}`))
      } else {
        p.resolve(msg.result)
      }
    }
  }

  _fail(err) {
    const pending = [...this.pending.values()]
    this.pending.clear()
    for (const p of pending) {
      clearTimeout(p.timer)
      p.reject(err)
    }
  }

  request(method, params) {
    return new Promise((resolve, reject) => {
      const id = this.nextId++
      const timer = setTimeout(() => {
        this.pending.delete(id)
        reject(new Error(`deposon mcp ${method}: timeout after ${this.opts.timeoutMs}ms`))
      }, this.opts.timeoutMs)
      this.pending.set(id, { resolve, reject, timer, method })
      try {
        this.child.stdin.write(JSON.stringify({ jsonrpc: '2.0', id, method, params }) + '\n')
      } catch (e) {
        clearTimeout(timer)
        this.pending.delete(id)
        reject(new Error(`deposon mcp ${method}: write failed (${e?.message ?? e})`))
      }
    })
  }

  notify(method, params) {
    try {
      this.child?.stdin.write(JSON.stringify({ jsonrpc: '2.0', method, params }) + '\n')
    } catch { /* server tolerates a missed notification */ }
  }

  async callTool(name, args) {
    await this.start()
    return this.request('tools/call', { name, arguments: args ?? {} })
  }

  async listTools() {
    await this.start()
    return this.request('tools/list', {})
  }

  stop() {
    const c = this.child
    this.child = null
    this._fail(new Error('deposon mcp client stopped'))
    try { c?.kill() } catch { /* already gone */ }
  }
}

/** Phantom-limb belief block — read from mcp/phantom_limb.{zh,en}.txt (single text source with the MCP face). */
function beliefText(lang) {
  const read = (l) => readFileSync(path.join(ROOT, 'mcp', `phantom_limb.${l}.txt`), 'utf8')
  if (lang === 'both') return read('zh').trimEnd() + '\n\n' + read('en')
  if (lang === 'zh' || lang === 'en') return read(lang)
  throw new Error(`DEPOSON_PL_LANG must be zh|en|both, got ${JSON.stringify(lang)}`)
}

function flagOn(value, fallback) {
  if (value === undefined || value === null) return fallback
  if (typeof value === 'boolean') return value
  return !['0', 'false', 'no', 'off'].includes(String(value).toLowerCase())
}

/** dsh ToolDefinition mirroring the official MCP bridge shape (content array, isError -> throw). */
function toolDefinition(spec, invoke) {
  return {
    name: spec.name,
    description: spec.description,
    parameters: spec.inputSchema,
    output: {
      schema: {
        type: 'object',
        properties: { content: { type: 'array', items: {} } },
        required: ['content'],
        additionalProperties: false,
      },
      render: (_args, value) => [{ type: 'text', text: extractText(value) }],
    },
    async execute(args) {
      const a = (typeof args === 'object' && args !== null && !Array.isArray(args)) ? args : {}
      const res = await invoke(a)
      if (res && res.isError) throw new Error(extractText(res) || `${spec.name} failed`)
      return { content: Array.isArray(res?.content) ? res.content : [] }
    },
  }
}

function registerThermoTool(ctx, spec, invoke, registered) {
  // (a) dsh native registry: ctx.tools.register(ToolDefinition)
  const tools = ctx?.tools
  if (tools && typeof tools.register === 'function') {
    try {
      tools.register(toolDefinition(spec, invoke))
      registered.push(`ctx.tools.register#${spec.name}`)
      return
    } catch (e) {
      ctx?.logger?.warn?.(`deposon: tools.register skipped for ${spec.name}: ${e?.message ?? e}`)
    }
  }
  // (b) preview-era variance (same probe order as gate_check): .add / .register with invoke spec
  for (const key of ['tool', 'tools', 'agentTools']) {
    const surface = ctx?.[key]
    if (!surface) continue
    try {
      const probe = {
        name: spec.name,
        description: spec.description,
        parameters: spec.inputSchema,
        inputSchema: spec.inputSchema,
        invoke,
      }
      if (typeof surface.add === 'function') {
        surface.add(probe)
        registered.push(`ctx.${key}.add#${spec.name}`)
        return
      }
      if (typeof surface.register === 'function') {
        surface.register(probe)
        registered.push(`ctx.${key}.register#${spec.name}`)
        return
      }
    } catch (e) {
      // defensive: preview-era API drift must not break plugin load
    }
  }
}

function makeThermoFace(ctx, config, base) {
  const env = process.env
  const ledger = config.ledger ?? env.DEPOSON_LEDGER ?? path.join(os.homedir(), '.deposon', 'ledger.jsonl')
  const lang = config.lang ?? env.DEPOSON_PL_LANG ?? 'zh'
  const beliefOn = flagOn(config.belief ?? env.DEPOSON_BELIEF, true)
  const briefOn = flagOn(config.brief ?? env.DEPOSON_THERMO_BRIEF, true)
  const footerOn = flagOn(config.footer ?? env.DEPOSON_THERMO_FOOTER, true)
  const thermo = config.thermo ?? env.DEPOSON_THERMO ?? null
  const timeoutMs = Number(config.toolTimeoutMs ?? env.DEPOSON_TOOL_TIMEOUT_MS ?? 60000)
  const registered = base.registered

  const childEnv = {
    ...env,
    PYTHONIOENCODING: 'utf-8',
    CONDENSATE_LEDGER: ledger,
    DEPOSON_PL_LANG: lang,
    DEPOSON_THERMO_FOOTER: footerOn ? '1' : '0',
  }
  if (thermo) childEnv.DEPOSON_THERMO = typeof thermo === 'string' ? thermo : JSON.stringify(thermo)
  else delete childEnv.DEPOSON_THERMO
  try { mkdirSync(path.dirname(ledger), { recursive: true }) } catch { /* dir may already exist */ }

  const client = new McpStdio({ cmd: base.python, args: [MCP_SERVER], cwd: ROOT, env: childEnv, timeoutMs })

  // Counts-only runtime context (live rows / phantom limbs): cached text refreshed
  // asynchronously after tool calls (never blocks prompt assembly on a child process).
  let briefCache = ''
  let refreshing = false
  function refreshBrief() {
    if (!briefOn || refreshing) return
    try {
      if (!existsSync(ledger) || statSync(ledger).size === 0) return
    } catch { return }
    refreshing = true
    const child = spawn(base.python, [THERMO_CLI, 'brief'], {
      cwd: ROOT,
      stdio: ['ignore', 'pipe', 'ignore'],
      env: childEnv,
    })
    let out = ''
    child.stdout.setEncoding('utf8')
    child.stdout.on('data', (d) => { out += d })
    child.on('error', () => { refreshing = false })
    child.on('close', () => {
      refreshing = false
      const t = out.trim()
      if (t) briefCache = t
    })
  }

  const invoke = (name) => async (args) => {
    const res = await client.callTool(name, args)
    refreshBrief()
    return res
  }
  for (const spec of THERMO_TOOLS) registerThermoTool(ctx, spec, invoke(spec.name), registered)

  // Phantom-limb belief block as a system-prompt section (0 memory data: protocol text only).
  let belief = null
  if (beliefOn) {
    belief = beliefText(lang)
    const sp = ctx?.systemPrompt
    if (sp && typeof sp.section === 'function') {
      try {
        sp.section({ name: BELIEF_SECTION, order: BELIEF_ORDER, text: belief, interpolate: false })
        registered.push(`ctx.systemPrompt.section#${BELIEF_SECTION}`)
      } catch (e) {
        ctx?.logger?.warn?.(`deposon: system-prompt section skipped: ${e?.message ?? e}`)
      }
    }
  }
  if (briefOn) {
    const sp = ctx?.systemPrompt
    if (sp && typeof sp.context === 'function') {
      try {
        sp.context({ name: BRIEF_CONTEXT, order: BRIEF_ORDER, text: () => briefCache, interpolate: false, required: false })
        registered.push(`ctx.systemPrompt.context#${BRIEF_CONTEXT}`)
      } catch (e) {
        ctx?.logger?.warn?.(`deposon: system-prompt context skipped: ${e?.message ?? e}`)
      }
    }
  }

  // Human-facing commands: print the belief block / run the read-only audit.
  try {
    if (typeof ctx.command === 'function') {
      if (beliefOn) {
        const cmd = ctx.command('deposon-belief', 'print the deposon phantom-limb belief block injected into the system prompt')
        if (cmd && typeof cmd.action === 'function') {
          cmd.action(() => beliefText(lang))
          registered.push('ctx.command#deposon-belief')
        }
      }
      const cmd = ctx.command('deposon-thermo-audit', 'read-only thermodynamic audit of the deposon living-water ledger (self-settling, no external reconciliation)')
      if (cmd && typeof cmd.action === 'function') {
        cmd.action(() => client.callTool('deposon_thermo_audit', { format: 'text' }).then((r) => extractText(r)))
        registered.push('ctx.command#deposon-thermo-audit')
      }
    }
  } catch (e) {
    ctx?.logger?.warn?.(`deposon: thermo command registration skipped: ${e?.message ?? e}`)
  }

  // Prime the counts-only brief once the harness is up; stop the child on dispose.
  try { ctx.on?.('ready', refreshBrief) } catch { /* lifecycle optional */ }
  try { ctx.on?.('dispose', () => client.stop()) } catch { /* lifecycle optional */ }

  return {
    client,
    ledger,
    lang,
    belief,
    tools: THERMO_TOOLS.map((t) => t.name),
    brief: () => briefCache,
    call: (name, args) => client.callTool(name, args),
    stop: () => client.stop(),
  }
}

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

  // Surface 3 — thermo face (preview.10): living-water memory tools + phantom-limb
  // belief block + self-settling audit/settle, forwarded to mcp/mcp_server.py.
  // gate_check above is intentionally untouched.
  const thermo = makeThermoFace(ctx, config, { python: opts.python, registered })

  // Lifecycle: observable evidence that the bundle mounted.
  try {
    ctx.on?.('ready', () => {
      ctx.logger?.info?.(
        `dsh-plugin-deposon mounted (surfaces: ${registered.join(', ') || 'none'})`,
      )
    })
  } catch (e) { /* lifecycle optional */ }

  return { root: ROOT, registered, gateCheck, thermo }
}
