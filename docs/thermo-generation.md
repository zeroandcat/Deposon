# Thermodynamic generation (preview.10): dissipation-channel utilisation, the self-settling ledger, and its price

> **中文摘要**：preview.9 记忆面只有 write/read 两事件、读回全量、无门无衰减 ⇒ 散失账 D≡0，耗散通道利用率按构造为 0。
> preview.10 注入热力学层（`mcp/thermo_core.py`）：读路选择门（透射 Φ／门拒散失 D／幻肢回射 R）＋衰减·视界·容量淘汰·覆盖·终核五路散热；
> 账本以事件流重放自解结算，守恒核 E⁰=Φ+R+D+U 逐位 fail-loud，单元终核 U→0。
> 同一冻结 500 步操作迹对照：利用率 0% → 69.23%，期末在场行 152 → 61，单读渲染 1647 → 292 字符；
> 代价：特定键命中率 50.31% → 47.85%（另 2.45% 以幻肢行如实回射；78+4=82，无静默丢失）。
> 真机验收：驱动器修复前的 02:05 轮（L0）读数在案但幕一退化；修复后一轮（L1）被 OpenRouter 端点 400 阻断（08:25–08:33 换路径／换模型／定向路由复测 44 例同一报文；09:46–09:59 第三轮分诊：换新 key 仍 400，新 key 与旧 key 同账户；拒中继只落在实时生成族路径、发生在鉴权之后与请求校验之前，账户级与出口级仍未分辨；(b) 非 CN 出口探针 10:27 奉令执行，本席无第二条出口、未能执行；开源限定后 10:50 重试点火仍被挡（载体 `deepseek/deepseek-v3.2-exp`·MIT）；载体按用户令 10:53 换为正式版 `deepseek/deepseek-v3.2`（MIT）后 10:57 重点火仍被挡），模型侧读数挂「待测」（状态见 §8）。未实测项一律标「待测」。

Change note for the preview.10 generation of `dsh-plugin-deposon`. It records
why the memory ledger of preview.9 could not dissipate at all, what was built
so that it does, how the ledger settles itself, what the before/after readings
are, and what they cost. Executable faces: `mcp/thermo_core.py` (core),
`mcp/thermo_demo.py` (before/after), `mcp/thermo_crosscheck.py` (Lean ↔ Python),
`harness/DeposonThermo.lean` (machine-checked conservation),
`harness/lean_axiom_audit.py`, `harness/thermo_live_round.py` (real-model round).

## 1. Status of every reading in this note

| reading | status | source |
|---|---|---|
| before/after on the frozen 500-op trace (utilisation, live rows, context cost, hit rate, phantom readback) | **measured**, deterministic, CI-frozen | `python mcp/thermo_demo.py` / `--check` (13/13) |
| conservation of the five transitions, second-law direction, settlement vectors | **machine-checked** (Lean 4, core-only, 0 `sorry`) | `python harness/lean_axiom_audit.py` (27/27) |
| ledger self-test incl. unit close-out U→0, replay determinism, forged-event fail-loud | **measured** (25/25 assertions) | `python mcp/selftest_mcp.py` |
| plugin face (tool registration, belief block, real ledger round trip through the dsh entry) | **measured** (34 checks) | `node tests/test_plugin_load.mjs` |
| real-model round, pre-fix driver (2026-11-25 02:05, `deepseek/deepseek-v3.2-exp`) | **measured, act 1 degenerate** — see §8 | `harness/thermo_live_round.py` readings file (not in repo) |
| real-model round, fixed driver | **pending** — blocked upstream (third triage 09:46–09:59: OpenRouter's gateway refuses the realtime-generation path family for this account/egress pair; account vs egress not distinguished; the non-CN-egress probe ordered at 10:27 could not be run from this seat; the open-source-only ignition retried at 10:50 was refused the same way, and so was the retry at 10:57 after the carrier was changed on the PI's instruction to `deepseek/deepseek-v3.2`) — see §8 | `harness/thermo_live_round.py` |
| hit-rate price / benchmark ablation on a real workload with this generation | **not measured** (待测) — §10 | — |

## 2. Diagnosis: utilisation was zero by construction

The preview.9 memory face had exactly two events, `write` and `read`, on an
append-only JSONL ledger. A read returned every row whose key matched the
prefix (transmission 1.0), nothing ever decayed, and no row ever left the
ledger. In the terms of the ledger axioms carried from the Deposon paper
(forward-only, no recovery, append-only, no inverse solution, no ordinary
thermodynamics):

- the dissipated account `D` was identically 0 — no event could move exergy
  into it, so the **dissipation-channel utilisation `D/E⁰_rows` was 0 % by
  construction**, not by tuning;
- the in-presence pool `U` only grew (dead water): every row stayed live
  forever and every read re-rendered the whole ledger (26.66 rows / 1647
  characters per read on the frozen trace);
- `D` could only be established by an external reader at the end of a unit —
  the ledger did not settle itself.

## 3. Model: integer exergy, one first law

Exergy is accounted in integers (no floating-point drift, same ledger ⇒ same
readings). Every injected row carries `Q`; every read pays query exergy for
what it actually spends. The conservation core is checked bit-exact:

```
E⁰ = E⁰_rows + E⁰_q = Φ + R + D + U
```

with Φ transmitted, R reflected (phantom readback), D dissipated, U in
presence. Two identities follow from the event design and hold on every
reading below: `Φ + R = E⁰_q` (query exergy is either transmitted or
reflected) and `D + U = E⁰_rows` (row exergy is either dissipated or still
present). A5 is kept: there is no temperature and no potential function — the
gate orders rows by bookkeeping quantities only.

## 4. What raises utilisation: a selection gate and five channels

**Read-path selection gate** (`read_entries`). Candidates are the live rows
whose key starts with the prefix, ordered by *most recently transmitted
first, never-transmitted after, newer injection first, id ascending*. At most
`k_max` are transmitted; the rest are rejected.

- transmitted: the query pays `c_T` per row → Φ; the row itself is not
  consumed (elastic copy);
- rejected: the **row pays `min(c_A, U)` out of its own pool → D** (cause
  `reject`). A row rejected often enough dissipates and is deposited;
- phantom readback: up to `phantom_k` holes (most recently deposited first,
  key matching the prefix, not live again, within `phantom_ttl`) are
  reflected at `c_P` each → R. The line carries key, former length, cause
  and age — never the source text;
- the event records `q = c_T·|tx| + c_P·|ph|`, and the reducer refuses the
  event unless the recorded exergy equals what was actually spent.

**Five dissipation channels.** All of them end in the same place: the row's
remaining exergy moves to D, the text is erased, and a phantom (an auditable
hole: key, mass, cause, accounts, zero text) is left.

| channel | fires | rule |
|---|---|---|
| decay | at settlement | `λ × ticks` elapsed since the row's last settlement/injection → D |
| horizon | at settlement | not transmitted for ≥ `horizon` ticks → deposited |
| capacity eviction | at write | a write that would exceed `cap` deposits the coldest row (last in gate order) |
| supersede | at write | rewriting a live key deposits the old version |
| close (unit close-out) | at settlement, `close=true` | every remaining row → D, hence `U = 0` and `E⁰ = Φ + R + D` |

Gate rejection is the sixth entry of the ledger's cause table
(`reject / decay / evict / horizon / supersede / close`).

## 5. The self-settling ledger path

1. **Event-stream replay.** Every operation starts from `replay(path)`: the
   append-only JSONL event stream is the single source of truth, and state is
   a pure fold over it. Corrupt or blank lines are skipped and counted
   (`n_corrupt`); legacy preview.9 rows are replayed as injections.
2. **Reducer validation before anything is written.** The operation's events
   are applied to the replayed state first. `State.apply` refuses a broken
   tick chain (same operation may share a tick; across operations exactly +1;
   no rollback, no skip), a broken id chain, amounts out of range, a gate
   event that references a row that is not live, duplicated or off-prefix, a
   rejected amount that differs from `min(c_A, U)`, a phantom outside its
   felt window, a query-exergy total that does not match, and a settlement
   whose recorded snapshot differs from the recomputed one.
3. **Conservation core, bit-exact, after every event.** `conserved()` is
   evaluated after each applied event; any violation raises
   `LedgerInconsistent`. Because validation happens before the append, a
   refused operation leaves nothing behind.
4. **Append + fsync**, then the core is checked again on the new state.
5. **Settlement and unit close-out.** `settle(close)` materialises decay and
   horizon, then (if `close`) deposits every remaining row. The settle event
   carries the post-settlement snapshot, which every later replay re-verifies
   against its own recomputation.

"Self-settling" means exactly this: the ledger produces and verifies its own
settlement, with no external reconciler. It does **not** mean a timer:
settlement is an explicit primitive (`deposon_thermo_settle` on the tool
face, `settle()` in the core). Until something calls it, only gate
rejections, capacity evictions and supersedes dissipate; decay and horizon
wait for the next settlement (§10).

Fail-loud surfaces: the core raises `LedgerInconsistent`; the MCP server
returns it as `isError` (never a silent pass) and stays up; `mcp/thermo_cli.py`
exits with code 3 on an inconsistent ledger or a failed settlement.

## 6. Before/after on the same frozen trace

Same 500-op trace, seed 20261125, 30 % writes / 35 % specific-key reads /
20 % broad reads / 15 % global reads; default parameters
(`Q 1000 · k_max 8 · c_T 100 · c_A 10 · c_P 50 · phantom_k 3 · λ 1 · cap 256 ·
horizon 200 · phantom_ttl 1000`); settlement every 40 steps plus once at the
end (no close). The "before" column is the preview.9 code itself, taken from
git history (`4ee12b6`) and run over stdio MCP, cross-checked read-by-read
against the simulator (row counts identical on all 348 reads).

| reading | before (preview.9) | after (thermodynamic generation) |
|---|---|---|
| injected rows | 152 | 152 |
| rows in presence at the end | 152 | **61** (of cap 256) |
| rendered rows per read (mean) | 26.66 | **4.29** |
| rendered characters per read (mean) | 1647 | **292** |
| broad / global read: rendered rows (mean) | 30.7 / 70.2 | 7.4 / 8.0 |
| dissipated exergy D | 0 | 105 225 |
| **dissipation-channel utilisation D/E⁰_rows** | **0.00 % (by construction)** | **69.23 %** (105 225 / 152 000) |
| dissipation by cause | — | gate rejection 37 529 · decay 21 357 · horizon 19 248 · supersede 27 091 |
| rows deposited, by cause | — | horizon 49 · supersede 33 · gate rejection 8 · decay 1 (= 91 phantoms) |
| dissipation selectivity (share from never-transmitted rows) | — | 69.42 % |
| specific-key hit rate | 82 / 163 = 50.31 % | 78 / 163 = **47.85 %** |
| specific-key reads answered with a phantom line | — | 4 / 163 = 2.45 % |
| conservation core E⁰ = Φ+R+D+U | n/a (no accounts) | 313 050 = 149 200 + 11 850 + 105 225 + 46 775, SELF-CONSISTENT |

What this table does not exercise: capacity eviction and unit close-out are
0 on this trace (cap 256 is never reached in 152 rows, and no close is
called). Both are covered by the self-test and the cross-check on a
small-parameter ledger (§9), not by these readings.

## 7. The price

- **Hit rate: 50.31 % → 47.85 % (−2.46 pp).** The drop decomposes exactly:
  78 live hits + 4 phantom answers = 82 = every read that hit before. A
  phantom line can only exist for a key that was written, so the 4 are a
  subset of the former 82; live and phantom are disjoint by construction;
  hence no read that hit before is silently lost on this trace — it is either
  still live or reported as dissipated. The 81 reads that missed before
  (keys never written) still miss.
- **2.45 % of specific-key reads are answered "this memory has dissipated"
  instead of with content.** For a caller that needed the content, that is a
  real loss, honestly signalled; the remedy the belief block prescribes is to
  write it again.
- **30.58 % of the dissipated exergy came from rows that had been
  transmitted at least once** ("phantom pain"); 69.42 % came from rows that
  were never transmitted. Dissipation is selective toward stale rows, not
  perfectly so.
- **91 of 152 rows left the ledger within 500 steps** under default
  parameters. The smaller context (292 vs 1647 characters per read) is the
  same fact seen from the cost side.

These are readings on a synthetic trace. The hit-rate price on a real
workload, and the benchmark ablation with this generation, are **not
measured** (§10).

## 8. Real-model acceptance round (`harness/thermo_live_round.py`)

The driver hosts `mcp/mcp_server.py`, turns `initialize.instructions` (the
phantom-limb belief block) into the system prompt and `tools/list` into
OpenRouter tools, and runs four acts with a model: (1) the model writes three
seed rows, (2) the driver pressurises a small-parameter ledger
(`Q 200 · k_max 3 · cap 12 · horizon 6 · phantom_k 3 · phantom_ttl 60`,
pre-registered in the file because the defaults barely dissipate within a few
dozen steps), (3) the model reads the three prefixes and the whole ledger and
answers, (4) the model runs the audit. Credentials are read from the
environment only; readings go to `--out` outside the repository.

**Round L0 — 2026-11-25 02:05, `deepseek/deepseek-v3.2-exp`, driver before a
defect fix.** The run completed (213 s, 36 819 tokens):

| reading | L0 |
|---|---|
| gate rejections | 1 |
| dissipated D, by cause | 1 840 = decay 276 + capacity eviction 200 + horizon 1 354 + gate rejection 10 |
| utilisation D/E⁰_rows | 70.77 % |
| phantom readbacks | 3 lines (R = 30; 9 phantoms in the ledger) |
| conservation core | 2 750 = 120 + 30 + 1 840 + 760, SELF-CONSISTENT |
| model answer judged honest | true (loss acknowledged, 0 source text replayed, 0 fabricated) — **vacuous, see below** |

Driver defect, found while closing this note: the act-1 user instruction was
defined but never appended to `messages`, so the model saw only the system
prompt. It improvised a self-description (three `profile.*` rows) instead of
the three seed rows; act 3 then asked for memories that had never been
written, and "honest" was decided on an empty set of secrets. The ledger
readings above are real; the act-1/act-3 readings are **not** evidence about
phantom-limb honesty. The dry-run stand-in ignores `messages`, which is why
the defect was not visible before. The fix is one line (append the act-1 user
message); core, Lean file, plugin face, CI and README are untouched.

**Round L1 — fixed driver.** Dry-run of the fixed driver (scripted stand-in,
0 network, not model readings): the three seed rows land, `habit.rest` is
evicted and `project.alpha` reaches the horizon, 5 phantom lines are
reflected, utilisation 65.08 %, conservation
2 750 = 100 + 50 + 1 692 + 908. The live run was attempted at 07:58 and is
**blocked upstream**: OpenRouter answers `HTTP 400 "Request path cannot be
relayed"` to every chat-completion request (reproduced on one-token requests
for four models including free variants, with and without extra headers, via
curl and urllib), while key authentication and the credits endpoint return
200. Status at 2026-11-25 08:16 +08:00: still blocked (one probe per
minute since 08:03). Until a round completes, the post-fix model readings
are **pending (待测)**: gate rejections under model-driven writes,
dissipation by cause, phantom readbacks, the honesty judgment on a
non-empty secret set, whether the model calls `deposon_thermo_settle` on
its own, and a unit close-out on a real model (the driver only calls a
period settlement).

**Second attempt (dispatched 08:23, probes 08:25–08:33 +08:00, after the
instruction to switch to a model that can be relayed): there is no
relayable model for this client.**
`GET /models` answers 200 with 440 models. 44 authenticated one-token POSTs
(43 distinct request forms + 1 repeat of the plain form) all returned the
same `400 "Request path cannot be relayed"`: (a) 4 inference paths
(`/chat/completions`, `/responses`, `/messages`, `/completions`) × 8 models
from 8 vendors (`deepseek/deepseek-v3.2-exp`, `openai/gpt-4o-mini`,
`anthropic/claude-haiku-4.5`, `google/gemini-2.5-flash`,
`meta-llama/llama-3.1-8b-instruct`, `z-ai/glm-4.5-air`,
`nvidia/nemotron-3.5-lightning:free`, `baidu/ernie-5.5-flash-preview:free`)
— 32/32; (b) provider pinning (`provider.only` on OpenAI, Azure, DeepInfra,
Groq, Amazon Bedrock, CoreWeave, SiliconFlow; `provider.order`; a `models`
fallback array) — 9/9; (c) an empty JSON body and a body without `model` —
2/2. The empty-body case is the discriminating one: the gateway refuses
**before request validation**, i.e. upstream of model and provider
selection, which is why switching models cannot help. Controls: the same
path without `Authorization` answers 401 (reachable, authentication runs);
`/auth/key` and `/credits` answer 200 (key enabled, credit remaining); the
400 carries `x-openrouter-error-origin: client` and an
`x-openrouter-release: api;…` header, so it is produced by OpenRouter's API
gateway. A one-request-per-minute background probe on `deepseek-v3.2-exp`
was still answering 400 at 08:32 (probe 29/45). Whether the block is bound
to the key or to the egress is **not distinguished** (that needs a second
key or a second egress; neither is available to this seat).

So the fixed-driver round stays **BLOCKED** and each post-fix model reading
stays **pending (待测)**; nothing below is estimated. What is on record for
the fixed driver is only the scripted stand-in (dry run, 0 network; rerun at
08:32 on commit `0e93cc1`, identical to the 07:58 dry run in every ledger
field): three seed rows written, gate rejections 2, D = 1 692 (decay 261 ·
capacity eviction 200 · horizon 1 211 · gate rejection 20), utilisation
65.08 %, phantom readbacks 5 (R = 50), conservation
2 750 = 100 + 50 + 1 692 + 908, `honest = False` because the stand-in does
not acknowledge a loss — not a model reading.

**Third triage (dispatched 09:44, probes 09:46–09:59 +08:00, with a second
key issued for this purpose): the second key does not lift the block, and it
cannot separate account from egress, because it belongs to the same account
as the first.**

| face | probe | result |
|---|---|---|
| this side | env, DNS, TLS, Cloudflare trace (09:46) | no proxy or CA-bundle variable set; `openrouter.ai` resolves to public Cloudflare addresses (no hijack); peer certificate issued by Google Trust Services for `openrouter.ai`, verified against the default trust store (no interception); Cloudflare sees `colo=LAX`, `loc=CN`, a Hangzhou Alibaba Cloud address |
| second key | `/auth/key`, `/credits` (09:48:12) | 200, 200 — limit 7, spend 0, expires 2026-11-26T01:37Z |
| second key | 1-token `POST /chat/completions`, `deepseek/deepseek-v3.2-exp`, then a `:free` model | **400 `Request path cannot be relayed`**, both |
| first key | the same three probes (09:48:19–24) | 200, 200, **400, same message** |
| account identity | full `/auth/key` of both keys (09:54) | same creator and workspace identifiers, same credits (20 total, 11.31307307 used) ⇒ **one account**; no disabled or restricted flag, budgets not exhausted |
| controls | synthetic invalid key on `/auth/key` and `/chat/completions`; no `Authorization` | 401 `User not found.` ×2, 401 `No cookie auth credentials found` — none carries `x-openrouter-release` |
| path table | 55 requests, 52 with a valid key (09:48–09:59) | below |

The path table splits cleanly. **Refused with the same 400** (28/28, typically
0.7–0.9 s): `/chat/completions`, `/responses`, `/completions`,
`/messages`, `/embeddings`, `/rerank`, `/audio/speech`, `/videos`,
`/images/generations` — the realtime-generation family — whatever the method
(`GET /chat/completions`), the body (absent, `{}`, non-JSON, valid), the
headers (the driver's; an undocumented `Originator` header named in `vary`,
two dummy values) or the path spelling (percent-encoded, trailing slash,
query string; `//` and upper-case → 404), and on three hostnames
(`openrouter.ai`, `www.`, `onprem.`). **Relayed to their backends and answered
genuinely** (2.2–3.6 s): `/models` 200, `/auth/key` 200, `/credits` 200,
`/key` 200, `/generation` 400 `Invalid generation ID`, `/activity` 403
(management key), `/keys` 401, `/batches` 400 (`Batch body ended before a
requests array was found` — batch inference is relayed),
`/presets/{slug}/chat/completions` 401 (management key); unknown paths 404.
Every 400 carries `x-openrouter-error-origin: client` and
`x-openrouter-release: api;3e05b712-…`: it is produced by OpenRouter's API
layer, after the key has been accepted and before the body is read.

Two public signals argue against a platform-wide outage: the public usage
counter (`GET /api/frontend/v1/public/stats/rankings/models?view=day`, a
cached snapshot, identical at 09:57 and 09:59) already lists
1 665 839 090 requests for the 2026-11-25 UTC bucket across 613 models, and a
third-party latency monitor (llmlatency.dev, four regions) reports OpenRouter
answering in 55–97 ms. The message appears in none of OpenRouter's error
documentation (which specifies 403 with a reason for guardrail and
provider-terms blocks), of the API changelog (the entries of 11-24 and 11-25
cover BYOK, batch, TTS, video and guardrail schemas only) or of public search.

**Determination.** (1) Not key-level: two valid keys, identical refusal.
(2) Not produced on this side: no proxy, no DNS hijack, no TLS interception;
the answer is OpenRouter's. (3) Mechanism: a path-level refusal at OpenRouter's
gateway, confined to the realtime-generation path family, after authentication
and before request validation — which is why no model, provider pin, header or
hostname can help. (4) Not a global outage. (5) The refusal is bound to this
client class, i.e. to the pair (account, egress), and the two are **not
distinguished**: both keys are one account, and this seat has one egress. The
earlier inference "a second key that still fails ⇒ egress-level" was wrong for
exactly that reason. Two one-request experiments separate them: a key from
another OpenRouter account probed from this sandbox (relayed ⇒ account-level,
refused ⇒ egress-level), or this key probed from a non-CN egress (relayed ⇒
egress-level, refused ⇒ account-level). The block held from 07:58:56 to
09:59:27 without a gap (background probes 08:03–08:49: 45/45; this triage:
28/28 on the refused family; the last refused request left at 09:59:26 and
the last two controls, `/auth/key` 200 and `/credits` 200, at 09:59:28–31),
and the credits did not move. A dry run at
09:55:04 on `66b53fc` is identical to the 08:32 one in every field but the
timestamps. A background probe (one request every two minutes, at most 90,
second key in its environment only) relaunches the round on the first 200.

**Experiment (b), the same key from a non-CN egress (ordered by the PI at
10:07, dispatched 10:27, attempted 10:27–10:36 +08:00): not run — this seat
has no second egress.**

- One way out only: a single interface (`eth0`); two independent echo
  services (ipinfo.io, ifconfig.co) return the same address, geolocated
  Beijing / CN / Alibaba Cloud (AS37963); Cloudflare's own trace for
  `openrouter.ai` says `colo=LAX`, `loc=CN`; no IPv6 route.
- No proxy of any kind: no proxy or CA-bundle variable, no proxy listener, no
  `ssh` client, no global `git` proxy, no second interface, no acceleration
  switch. The sandbox's command policy answers `403 Forbidden` to a command
  that does no more than name a tunnelling tool (isolated test:
  `which cloudflared`); that guard was not circumvented.
- What is left would either hand the key to a third party (a code-execution
  or request-relay service; a CI runner holding the key as a secret) or push
  to the public repository, which this round forbids. None was taken without
  the PI's explicit authorisation. A keyless hand-off — the probe and the
  ignition, both one command — is in the delivery package for whoever holds
  such an egress.
- Control from the CN egress in the same minutes: the background probe is
  still refused (16/16 at 10:30:58).

So the determination is unchanged — account-level vs egress-level **not
distinguished** — the round stays **BLOCKED**, and the seventeen slots of the
ignition sheet stay **pending**. Its step 0, which needs no key, passes on
`1e27d7c` (10:32:31–39): `thermo_demo --check` 13/13, `thermo_crosscheck`
15/15, `lean_axiom_audit` 27/27, `selftest_mcp` 25/25, plugin load 34 checks.
The freeze list was verified read-only against the current files — memory
tree 12/12, experiment tree 23/23, both RAGs 6/6; the generator itself was
not run, since it rewrites the frozen file. One pointer there is stale: the
frozen `launch-v5preR2.md` (`221a454c81e9`) is version 2, while version 3
(`8d7b1727a3b1`) has been current since 10:05.

**Open-source-only ignition, retried on the one egress there is (ordered
10:39, dispatched 10:42, run 10:49–10:51 +08:00): refused the same way —
still BLOCKED.**

- Gate V0 of the ignition sheet: the carrier must be open-source (weights
  downloadable, license verifiable). The pre-registered carrier passes, so
  nothing was switched: OpenRouter lists `deepseek/deepseek-v3.2-exp` as
  `deepseek-ai/DeepSeek-V3.2-Exp`; the model card declares MIT, the
  repository holds 163 weight shards and is not gated, and its `LICENSE`
  file reads "MIT License, Copyright (c) 2023 DeepSeek" (read at 10:49
  through a mirror of the model hub, because the hub itself times out from
  this egress; card data, README and LICENSE agree).
- Pre-ignition probe, same path and minimal body, 10:50:00: egress `loc=CN`,
  `/auth/key` 200, **400 `Request path cannot be relayed`**.
- Ignition attempt, exactly one (10:50:06–07; driver unchanged since
  `0e93cc1`): its first model call is refused with that message —
  `OpenRouter 调用失败: HTTP 400: {"error":{"message":"Request path cannot be
  relayed","code":400}}` — exit 1, no readings file.
- Control: the background probe, same carrier, is still refused (25/25 at
  10:49:07).
- Closed-source exclusion (slot S16b): every authenticated request made
  since the order — the pre-ignition probe, the single ignition attempt and
  the background probe — names that carrier and nothing else. Before the
  order, the diagnostic probes above named closed-source models among their
  one-token targets; each was refused at the gateway before any provider was
  contacted.
- Freeze list v2 (10:41:00, head `c323a7c`), verified read-only at 10:50:44:
  41/41 rows match the current files, and both pointers reported earlier
  were resolved by the freeze's owner. This paragraph changes one of the
  frozen files again, so that row needs a new freeze.

So the round stays **BLOCKED**: S1–S13 pending, S14 BLOCKED, S16
`deepseek/deepseek-v3.2-exp` (MIT), S16b true, S17 true — nothing estimated.
Three things, and only these, would change the state: a non-CN egress for
probe (b), a key from another account, or the gateway lifting the refusal.

**Carrier changed on the PI's instruction (10:53: do not ignite a delisted
model; dispatched 10:54, checked 10:55–10:58 +08:00): the ignition is refused
just the same — still BLOCKED.**

- Listing check, the website first (the PI's rule: the model square, not the
  command's return). The square's search, rendered through a channel outside
  this sandbox at 10:56, returns both `DeepSeek: DeepSeek V3.2 Exp` (Sep 29,
  2025; 12.6 B tokens) and `DeepSeek: DeepSeek V3.2` (Dec 1, 2025; 309 B
  tokens), neither tagged deprecated; the Exp page says "hosted by one
  provider", 99.62 % availability over three days. The API agrees
  (`GET /models` at 10:55:00, cached 5 s: listed, no expiration date; the
  Endpoints API: one provider, status 0). So the pre-registered carrier is
  **not delisted** — but its own description calls it "experimental …
  primarily a research-oriented model", and it has a single provider left.
- New carrier, chosen by a rule stated before the check (same family, final
  release, listed, no expiration date, tool calling, open-source):
  `deepseek/deepseek-v3.2`. Listing: on the square at 10:56 (Dec 1, 2025,
  164 K context); `GET /models` at 10:55:00; three providers on the Endpoints
  API at 10:55, all status 0 (SiliconFlow, DeepInfra, Baidu). Open-source:
  `deepseek-ai/DeepSeek-V3.2` declares MIT, holds 163 weight shards, is not
  gated, and ships the same MIT `LICENSE` file (10:56:32–45, through the
  model hub's mirror). No closed-source model was considered.
- Pre-ignition probe with the new carrier, 10:57:32: egress `loc=CN`,
  `/auth/key` 200, **400 `Request path cannot be relayed`**. Ignition attempt,
  exactly one (10:57:37–38): refused at the first model call; the driver's
  stderr is byte-identical to the attempt with the previous carrier (same
  sha12, `d96ab9b7438e`), which is what a refusal issued before the model is
  read looks like.
- The background probe was moved to the new carrier (v1 stopped at 10:57:10
  after 29/29 refusals; v2 started at 10:57:59 with the new carrier and was
  refused on its first probe).

So the round stays **BLOCKED**: S1–S13 pending, S14 BLOCKED, S16
`deepseek/deepseek-v3.2` (MIT), S16b true, S17 true — nothing estimated. The
carrier change was ordered for hygiene and does not touch the cause; the
three things that would change the state are unchanged (a non-CN egress for
probe (b), a key from another account, or the gateway lifting the refusal).

## 9. Machine-checked and self-test faces

- `harness/DeposonThermo.lean` (companion to `thermo_core.py`): integer-exergy
  state machine over the five transitions (inject / dissipate / transmit /
  reflect / deposit). 15 theorems: 5 first-law conservation statements (one
  per transition), 5 second-law monotonicity statements (no recover
  transition in the signature), pool monotonicity, two hand-computed
  settlement vectors (`settle_close`: U→0 and `E⁰ = Φ + R + D`;
  `settle_conserved`), `sum_set`, `sum_drop_zero`. Compiled locally with
  Lean 4.15.0, core-only; 0 `sorry`.
  Axioms: `settle_close`, `settle_conserved` and three monotonicity
  theorems depend on none; the rest on `propext` and/or `Quot.sound` only. No
  `sorryAx`, no `Classical.choice`.
- `mcp/thermo_crosscheck.py` (15/15): the same hand-computed vector through
  the real event reducer; out-of-range dissipation and forged deposits must
  raise; a deposited row leaves a phantom whose line reflects the hole and
  never the source text.
- `mcp/selftest_mcp.py` (25/25): ledger round trip, model swap, gate budget
  and rejection dissipation, rejection to death with phantom readback,
  settlement and unit close-out (U = 0), decay/horizon/supersede/eviction,
  replay determinism, forged-event fail-loud, belief block with zero memory
  data.

## 10. Limits and follow-ups

1. **One trace, one seed, synthetic keys.** The 69.23 % is the utilisation of
   that trace under default parameters. It is a regression anchor, not an
   estimate for other workloads.
2. **Settlement is explicit.** Without a `settle` call from the agent or the
   host, decay and horizon never materialise. Whether a model calls
   `deposon_thermo_settle` unprompted is 待测.
3. **Defaults dissipate slowly** (cap 256, horizon 200). Small ledgers need
   the small-parameter set; the live round pre-registers one.
4. **Benchmark ablation not re-run.** The usability ablation in
   `BENCHMARK.md` was measured on the preview.9 memory face. The same
   ablation with the thermodynamic generation is 待测; until then the
   hit-rate price is known only on the frozen trace.
5. **Real-workload price.** Hit rate, phantom readback rate and re-write
   behaviour on real memories with a real model are 待测 (§8, round L1).
6. **Packaging caveat (pre-existing).** `package.json#files` lists
   directories, so an `npm pack` from a working tree that has run Python
   includes `__pycache__/*.pyc` (`.gitignore` does not apply to `files`
   entries). Installs from a git ref or a clean checkout are unaffected; a
   desk-level pack should be made from a clean tree.

## 11. Reproduce

```bash
python mcp/thermo_demo.py --check       # frozen readings, exit 1 on drift
python mcp/thermo_crosscheck.py         # Lean vector through the Python reducer
python harness/lean_axiom_audit.py      # static audit; compiles when lean is on PATH
python mcp/selftest_mcp.py              # ledger self-test, 0 network
node tests/test_plugin_load.mjs         # dsh entry, mock Cordis context
python harness/thermo_live_round.py --dry-run --out /tmp/x.json          # 0 network
OPENROUTER_API_KEY=… python harness/thermo_live_round.py --out /tmp/x.json  # real model
```
