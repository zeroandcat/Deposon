# Thermodynamic generation (preview.10): dissipation-channel utilisation, the self-settling ledger, and its price

> **中文摘要**：preview.9 记忆面只有 write/read 两事件、读回全量、无门无衰减 ⇒ 散失账 D≡0，耗散通道利用率按构造为 0。
> preview.10 注入热力学层（`mcp/thermo_core.py`）：读路选择门（透射 Φ／门拒散失 D／幻肢回射 R）＋衰减·视界·容量淘汰·覆盖·终核五路散热；
> 账本以事件流重放自解结算，守恒核 E⁰=Φ+R+D+U 逐位 fail-loud，单元终核 U→0。
> 同一冻结 500 步操作迹对照：利用率 0% → 69.23%，期末在场行 152 → 61，单读渲染 1647 → 292 字符；
> 代价：特定键命中率 50.31% → 47.85%（另 2.45% 以幻肢行如实回射；78+4=82，无静默丢失）。
> 真机验收：驱动器修复前的 02:05 轮（L0）读数在案但幕一退化；修复后一轮（L1）被 OpenRouter 端点 400 阻断（08:25–08:33 换路径／换模型／定向路由复测 44 例同一报文；09:46–09:59 第三轮分诊：换新 key 仍 400，新 key 与旧 key 同账户；拒中继只落在实时生成族路径、发生在鉴权之后与请求校验之前，账户级与出口级仍未分辨；(b) 非 CN 出口探针 10:27 奉令执行，本席无第二条出口、未能执行；开源限定后 10:50 重试点火仍被挡（载体 `deepseek/deepseek-v3.2-exp`·MIT）；载体按用户令 10:53 换为正式版 `deepseek/deepseek-v3.2`（MIT）后 10:57 重点火仍被挡；再按用户令 11:23 换为官网广场最新一档开源模型 `xiaomi/mimo-v2.6-flash-mopd`（2026-11-23 发布·MIT）后 11:26 重点火仍被挡），模型侧读数挂「待测」（状态见 §8）。未实测项一律标「待测」。

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
| real-model round, fixed driver | **pending** — blocked upstream (third triage 09:46–09:59: OpenRouter's gateway refuses the realtime-generation path family for this account/egress pair; account vs egress not distinguished; the non-CN-egress probe ordered at 10:27 could not be run from this seat; the open-source-only ignition retried at 10:50 was refused the same way, and so were the retry at 10:57 after the carrier was changed on the PI's instruction to `deepseek/deepseek-v3.2` and the retry at 11:26 after it was renewed to the newest open-source model on the website's list, `xiaomi/mimo-v2.6-flash-mopd`) — see §8 | `harness/thermo_live_round.py` |
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

**Carrier renewed on the PI's instruction (11:23: a recently released or
updated open-source model from the website's current list; done 11:24–11:26
+08:00): the ignition is refused a third time, byte for byte — still
BLOCKED.**

- The list, from the website: its "Newest" view, rendered through a channel
  outside this sandbox at 11:24, starts with Upstage Solar Pro 4 Contributor
  and Solar Mini 4.5 (Nov 24; proprietary), Xiaomi MiMo-V2.6-Flash-MOPD (Nov
  23), Thinking Machines Inkling 2 Mini and RadixArk DaisyRose 27B (Nov 21),
  then embedding, decision, speech and video models (Nov 20–17), Gemini 4
  Neon (Nov 18; closed) and Pixtral Large 2502 — listed Nov 20 but, in the
  site's own words, "the February 2025 version". The API's `created` field
  (472 models at 11:24:21, cached 5 s) served only to shortlist.
- Rule, stated before choosing: a text-generation model on that view; released
  or updated recently by the model's own date, not the listing date;
  open-source (weights downloadable, license declared); tool calling. The
  newest tier is Nov 21–24 and holds three open-source models — MiMo (Nov 23,
  MIT), Inkling 2 Mini and DaisyRose 27B (Nov 21, both Apache-2.0). The
  newest of them is the carrier.
- Carrier `xiaomi/mimo-v2.6-flash-mopd`: the site's model page (same channel,
  11:25) says "Released Nov 23, 2026", links the weights, lists one provider
  (Featherless; 98.07 % uptime, availability 95.71 % over three days), a
  1 048 576-token context, and "accepts `tools` and `tool_choice`". On the
  model hub (11:25, through its mirror): `license: mit` on the card and in
  the README, 131 weight shards, not gated; the repository carries no
  separate `LICENSE` file, which is noted rather than glossed over. Its
  README calls it "the MOPD upgrade of the MiMo-V2.6-Flash-RL checkpoint",
  whose added distillation pass "reduces repeated tool calls in agentic
  workflows" — the failure the degenerate first act of round L0 showed.
- Pre-ignition probe, 11:25:53: egress `loc=CN`, `/auth/key` 200, **400
  `Request path cannot be relayed`**. Ignition attempt, exactly one
  (11:25:59–11:26:00): refused at the first model call; the driver's stderr
  has the same sha12 as with the two carriers before it (`d96ab9b7438e`).
- The background probe was moved again (v2 stopped at 11:24:14 after 14/14
  refusals; v3 started at 11:26:11 with the new carrier and was refused on
  its first probe).

So the round stays **BLOCKED**: S1–S13 pending, S14 BLOCKED, S16
`xiaomi/mimo-v2.6-flash-mopd` (MIT), S16b true, S17 true — nothing
estimated. Three carriers in one morning have drawn the same refusal; the
carrier is not the cause.

**OpenSDK detour and the "no new machine" rule on the PI's instruction
(11:37; done 11:41–11:59 +08:00): every official SDK is refused byte for
byte, the two GPU servers are powered off, and this sandbox has no GPU —
still BLOCKED; one round was additionally run through a local 0.6B carrier
on the sandbox CPU (0 cloud calls) as a pipeline exercise, outside the
pre-registration.**

- The two instructions (11:37:39): (1) retry through "OpenSDK" instead of
  hand-built REST; (2) do not rent a new machine — use the existing two
  servers and model resources, locally where possible with 0 cloud calls.
  Neither touches the verified code: the driver file is unchanged (sha12
  `e4bd79583ce8`, printed by the local wrapper at every start of this
  window).
- Four official SDKs, installed into the agent's private area only (never
  into the repository): `openai` 7.64.0 and `@openrouter/sdk` 1.5.139 (npm,
  Node v24.18.0); `openai` 3.59.0 and `openrouter` 1.3.211 (PyPI, Python
  3.12.13, httpx 0.28.1 — the default index timed out at 150 s, the TUNA
  mirror served them at 11:44:30). The key was passed through the
  environment only and read by the SDKs; both request logs redact
  `Authorization` and contain 0 occurrences of the key (`grep -c` = 0 on
  both, in the private area and in the delivery copy).
- Generation family, eight requests (11:45:02–11:46:01 +08:00), one row
  each; base URL `https://openrouter.ai/api/v1`, model
  `xiaomi/mimo-v2.6-flash-mopd`, one-token prompts. Every one: **400
  `{"error":{"message":"Request path cannot be relayed","code":400}}`**,
  `x-openrouter-release: api;3e05b712-d9f7-4400-993a-7cb63338fd89`,
  `x-openrouter-error-origin: client`, Cloudflare PoP `LAX`. The SDK
  requests differ from the hand-built ones on the wire — `User-Agent:
  OpenAI/JS 7.64.0`, `OpenAI/Python 3.59.0` and `speakeasy-sdk/…`, the
  `x-stainless-*` telemetry headers, another body serialisation (the
  OpenRouter SDK adds `"stream":false` and orders its keys), and the
  Responses path besides `/chat/completions` — and none of it changes the
  answer, which is also the answer the 11:25:53 raw probe got, on the same
  gateway release.

| case | SDK | request | sent | answered | HTTP | latency | release / error-origin / PoP | answer |
|---|---|---|---|---|---|---|---|---|
| N1 | openai 7.64.0 (js) | POST `/chat/completions` | 11:45:02 | 11:45:03 | 400 | 836 ms | 3e05b712-d9f7-4400-993a-7cb63338fd89 / client / LAX | `Request path cannot be relayed`, code 400 |
| N2 | openai 7.64.0 (js) | POST `/chat/completions` | 11:47:06 | 11:47:07 | 400 | 963 ms | 3e05b712-d9f7-4400-993a-7cb63338fd89 / client / LAX | `Request path cannot be relayed`, code 400 |
| N3 | openai 7.64.0 (js) | POST `/responses` | 11:45:03 | 11:45:04 | 400 | 268 ms | 3e05b712-d9f7-4400-993a-7cb63338fd89 / client / LAX | `Request path cannot be relayed`, code 400 |
| N4 | @openrouter/sdk 1.5.139 | POST `/chat/completions` | 11:45:04 | 11:45:05 | 400 | 961 ms | 3e05b712-d9f7-4400-993a-7cb63338fd89 / client / LAX | `Request path cannot be relayed`, code 400 |
| N5 | openai 7.64.0 (js) | GET `/models` | 11:45:05 | 11:45:06 | 200 | 979 ms | — / — / LAX | model list, 440 entries |
| N6 | @openrouter/sdk 1.5.139 | GET `/credits` | 11:45:06 | 11:45:06 | 200 | 299 ms | 3e05b712-d9f7-4400-993a-7cb63338fd89 / — / LAX | `total_credits 20`, `total_usage 11.31307307` |
| P1 | openai 3.59.0 (py) | POST `/chat/completions` | 11:45:57 | 11:45:58 | 400 | 1735 ms | 3e05b712-d9f7-4400-993a-7cb63338fd89 / client / LAX | `Request path cannot be relayed`, code 400 |
| P2 | openai 3.59.0 (py) | POST `/chat/completions` | 11:45:58 | 11:45:59 | 400 | 800 ms | 3e05b712-d9f7-4400-993a-7cb63338fd89 / client / LAX | `Request path cannot be relayed`, code 400 |
| P3 | openai 3.59.0 (py) | POST `/responses` | 11:45:59 | 11:46:00 | 400 | 798 ms | 3e05b712-d9f7-4400-993a-7cb63338fd89 / client / LAX | `Request path cannot be relayed`, code 400 |
| P4 | openrouter 1.3.211 (py) | POST `/chat/completions` | 11:46:00 | 11:46:01 | 400 | 784 ms | 3e05b712-d9f7-4400-993a-7cb63338fd89 / client / LAX | `Request path cannot be relayed`, code 400 |
| P5 | openai 3.59.0 (py) | GET `/models` | 11:46:01 | 11:46:03 | 200 | 1596 ms | — / — / LAX | model list, 440 entries |
| P6 | openrouter 1.3.211 (py) | GET `/credits` | 11:47:33 | 11:47:33 | 200 | 737 ms | 3e05b712-d9f7-4400-993a-7cb63338fd89 / — / LAX | `total_credits 20`, `total_usage 11.31307307` |

  N2 drew no server response at all on its first attempt (11:45:03, a
  connection error inside the SDK); it was repeated at 11:47:06 and is
  listed once, at the repeated attempt.
- Read family, four controls through the same SDKs and the same key: `GET
  /models` 200 (440 entries; openai-js and openai-py) and `GET /credits`
  200 (`total_credits 20`, `total_usage 11.31307307`; both OpenRouter
  SDKs). Authentication, routing and TLS through the SDK channel are
  therefore intact; only the generation family is refused, as in the third
  triage.
- Two probe defects are kept and marked as such. The first run of the Node
  matrix (11:44:27) logged every request as "Connection error" because its
  logging hook consumed the request body before forwarding it — a defect
  of the probe, not a reading; the file is kept as
  `node_matrix.attempt1_invalid.jsonl`. In the Python matrix a wrong method
  name (`credits.get`) produced three `AttributeError` rows (11:46:03–09)
  before the corrected call at 11:47:33; they carry no HTTP traffic.
- The ignition was not launched a fourth time through the SDKs: the driver
  speaks hand-built REST, and the two cases that mirror its headers exactly
  (N2, P2) were refused, so a fourth launch could only have reproduced the
  11:25:59 refusal. Background probe v3 kept its cadence: probes 1–11
  (11:26:12–11:46:21), all 400.
- The two servers are powered off: TCP to their SSH gateway
  (`connect.nmb1.seetacloud.com`, 116.136.52.182, ports 17068 and 41995) is
  refused outright — `[Errno 111] Connection refused` at 11:41:10 (0.08 s /
  1.12 s) and again at 11:56:55 (1.15 s / 1.24 s). Last known from the
  records of 11-24, not live: both a single RTX 4090 with 24 GB; 17068 a
  125 GB data disk holding the 4B runs (`4b_w3` ckpt 250/500/750, LoRA
  `pathb`/`w2`) and the 0.6B lineage; 41995 a 50 GB data disk holding the
  0.6B family runs. Where the Qwen3-4B base weights live, and whether any
  vLLM or Ollama is installed, were not verified live. A read-only
  inventory script is ready and takes about a minute once the machines are
  on. Nothing was rented and no instance was created; switching the two
  machines on is the PI's action in the console.
- This sandbox: 2 vCPUs (Xeon Platinum; AVX2 and AVX-512F, no BF16 or AMX
  instructions), 4 GB RAM, 30 GB disk (16 GB free), no GPU (`nvidia-smi`
  absent, no `/dev/nvidia*`), `torch 2.15.0+cpu`, `transformers 5.22.2`,
  no model server installed and no weights on disk (the hub cache held only
  the Qwen2.5-0.5B-Instruct tokenizer). The model hub is reachable through
  its mirror only (card endpoints 200, search 403; the direct site times
  out).
- Local-carrier pipeline, built outside the repository: `local_server.py`
  (an OpenAI-compatible `/v1/chat/completions` on 127.0.0.1 — chat template
  with tools, greedy decoding, thinking switched off, `<tool_call>` blocks
  parsed into tool calls, one log line per request) and `run_local.py`
  (imports the driver file unmodified, overrides only the `API_URL`
  constant, puts a placeholder string in the credential slot and passes
  every argument through). Weights: `Qwen/Qwen3-0.6B` — the mirror's card
  at 11:48:55 reads created 2025-04-27, `license: apache-2.0`, not gated,
  one safetensors shard (1 503 300 328 B), `LICENSE` file present —
  downloaded 11:49–11:50. Measured on two threads in fp32: load 9–14 s,
  RSS 2.7–2.8 GB, prefill 12.76 ms per prompt token (1 720 tokens in
  21.95 s), decode 1.88 tokens/s; bf16 was slower still (no BF16
  instructions) and was not used.
- The round through the local carrier (launched 11:56:00, finished 11:59:29,
  exit 0, 208 s, six requests to the local server, 7 302 prompt and 306
  completion tokens, cost 0): the model wrote exactly the three seed rows
  in the first act (`user.drink`, `habit.rest`, `project.alpha`; three
  write calls in one reply), the driver's pressure produced D = 1 672
  (decay 261, evict 200, horizon 1 211) with eight phantoms felt, the
  first law closed (2 620 = 20 + 0 + 1 672 + 928, U being the exergy of the
  five rows still live), gate rejections 0, utilisation A 64.31 %, and the
  fourth act called `deposon_thermo_audit` once. But in the third act the
  model called **no read tool at all**: it answered "found user.: … (lost)"
  for all three prefixes out of its own context, so no phantom line ever
  reached it — `phantom_lines_in_tool_results` is empty, n_ph = 0, R = 0,
  and the `honest = true` is a value on an empty set, reported here as
  degenerate rather than as a pass. The carrier can write and audit but
  does not retrieve; that is a property of a 0.6B model, not of the ledger.
  It is **not** round L1: the carrier is outside the pre-registration, older
  than the "recently released" tier the PI set at 11:23, and about forty
  times smaller than the registered model. No slot above is filled from it;
  whether it is entered in the record as a separate local round is the PI's
  call. What it does show is that the 0-cloud-call path is real end to end
  — driver unmodified, local server, ledger, readings file — and only needs
  a carrier of the registered size class on the two 4090 servers.
- So the round stays **BLOCKED**: S1–S13 pending, S14 BLOCKED, S16
  `xiaomi/mimo-v2.6-flash-mopd` (MIT), S16b true, S17 true — nothing
  estimated. A fourth carrier would not change this, and neither would an
  SDK; what would change it is unchanged: a non-CN egress, a key from
  another account, the gateway lifting the refusal — or the PI switching
  the two 4090 servers on for a local carrier of the registered size class.
- **12:21–12:50, both servers booted without a GPU; their egress measured.**
  The two instances came up without a card at 12:10:45 / 12:10:52 (PID 1
  start) and were inventoried read-only over the key path
  (`connect.nmb1.seetacloud.com:17068`, `:41995`; no credential written or
  echoed). Both egresses are **CN** (12:26): Cloudflare trace `loc=CN`,
  `colo=LAX`; ipinfo "Hohhot, Inner Mongolia, AS4837 CHINA UNICOM China169
  Backbone"; ip-api "China / China Unicom" (egress IPs kept as sha12 only).
  The non-CN-egress probe was therefore **not** run on the servers and the
  key was not sent to them — these two machines cannot test the refusal
  away. Keyless reachability from both: `GET /models` 200, `POST
  /chat/completions` without a key 401. A client new to the project
  (`openrouter/`, TypeScript, official `@openrouter/sdk` 1.5.139, key read
  from `OPENROUTER_API_KEY` only; new files, verified code untouched) was
  run from the CN egress: read path `GET /credits` 200 (12:41:08);
  generation 400 "Request path cannot be relayed", release
  `api;3e05b712-d9f7-4400-993a-7cb63338fd89`, `x-openrouter-error-origin:
  client`, PoP LAX — in both runs (12:41:08 and 12:42:43). Three of the
  eight requests in the four runs met a transport-level `fetch failed`
  (classified `NETWORK`, retryable). An invalid key gives 401 "User not
  found." with no release header (12:41:05). Nothing estimated; S1–S13
  stay pending, S14 BLOCKED.
- **Correction to the handoff probe.** `or_noncn_probe_v3.py` (delivered
  11:2x) carries a file path where the model slug belongs, in its `MODEL`
  default (three places), so the pre-ignition probe record of 11:25:53
  logged a path in its `model` field. The refusal precedes model parsing,
  so that probe's 400 verdict stands; the record's model field does not. A
  corrected `or_noncn_probe_v4.py` (only those three places changed;
  self-tested with no key → exit 3, with a dummy key → the request body
  carries the slug) is in the delivery package; the delivered v3 is left
  as it was.
- **Experiment preparation on the two servers (CPU stand-in, no GPU).**
  The verified code tree `1e27d7c` (`git archive`, 72 files) and Bob's
  stand-in harness (a path-patched copy; diff in the package) were placed
  under `/root/autodl-tmp/prep_eg_1125/` on both. The four D0 gates pass on
  both (`thermo_demo --check` 13/13, crosscheck 15/15, selftest 25/25,
  live-round `--dry-run`), and the seven CPU blocks plus a 20-seed ×
  k_max ∈ {1, 2, 4, 8} extension of D4b ran to completion (17068
  12:34:29–12:43:13, 41995 12:34:29–12:41:22). Against a snapshot
  (12:46:22) of Bob's readings every non-environment, non-timing leaf is
  bit-identical: 10,140 leaves equal, 0 reading differences. Timing under
  the 0.5-core no-GPU quota differs and is reported as such (D1 original
  arm at N = 1000: 48.19 s and 36.60 s, against 20.27 s on two cores). The
  Qwen3-4B weights on 17068 match the hub revision `1cfa9a72…` (three LFS
  sha256 values plus `config.json` and the index; Apache-2.0); 41995 has
  no 4B weights. No GPU arm exists yet (the E-G1–E-G3 ledger, the E-G4
  learnable gate), so a GPU boot now would idle: not switched on.
- **OpenRouter integration delivered (13:00 dispatch).** The client built
  at 12:35–12:50 (`openrouter/`, commit `28bf95b`) had not reached the
  group before the previous round timed out; it was re-verified at 13:02:30
  (build rc 0, stand-in tests 8/8) and delivered in batches from 13:02
  (code, README, evidence, private-repo commit record; local branch
  `private/v5preR2`, not pushed). The website's model page rendered at
  13:03 still lists the carrier (released Nov 23 2026, one provider,
  3-day uptime 100 %, availability 95.71 %); the rendered page shows no
  licence field, the licence name (MIT) comes from the hub card. A third
  three-condition run at 13:03:57–13:04:01 with the key taken from the
  watch process's environment (not typed, not written): no key → exit 3;
  invalid key → 401 "User not found." (no release header) on generation
  and a transport `fetch failed` on the read path; real key → `GET
  /credits` 200 (20 / 11.313) and generation 400 "Request path cannot be
  relayed", the same release `api;3e05b712…`, origin `client`, PoP LAX.
  The watch probe v3 (120 s) logged 49/49 refusals up to 13:03:03. 429 and
  5xx are covered by stand-in cases only; no live reading exists for them.
  Round BLOCKED, nothing estimated.

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
