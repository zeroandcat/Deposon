# Thermodynamic generation (preview.10): dissipation-channel utilisation, the self-settling ledger, and its price

> **中文摘要**：preview.9 记忆面只有 write/read 两事件、读回全量、无门无衰减 ⇒ 散失账 D≡0，耗散通道利用率按构造为 0。
> preview.10 注入热力学层（`mcp/thermo_core.py`）：读路选择门（透射 Φ／门拒散失 D／幻肢回射 R）＋衰减·视界·容量淘汰·覆盖·终核五路散热；
> 账本以事件流重放自解结算，守恒核 E⁰=Φ+R+D+U 逐位 fail-loud，单元终核 U→0。
> 同一冻结 500 步操作迹对照：利用率 0% → 69.23%，期末在场行 152 → 61，单读渲染 1647 → 292 字符；
> 代价：特定键命中率 50.31% → 47.85%（另 2.45% 以幻肢行如实回射；78+4=82，无静默丢失）。
> 真机验收：驱动器修复前的 02:05 轮（L0）读数在案但幕一退化；修复后一轮（L1）被 OpenRouter 端点 400 阻断（08:25–08:33 换路径／换模型／定向路由复测 44 例同一报文），模型侧读数挂「待测」（状态见 §8）。未实测项一律标「待测」。

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
| real-model round, fixed driver | **pending** — blocked upstream at the time of writing — see §8 | `harness/thermo_live_round.py` |
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
