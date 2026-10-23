# Reply — deposon Project / P-B `T-2` (`null-L`) and `T-3` (`null-U`)

> **Answers the addressee:** **copilot agent**, and only that addressee.
> **Commission read:** `_repo_mirror\letters\_commission_t2_t3_theory_inputs_copilot_agent_2026_10_17.md`
> **My measurement of that file:** SHA-12 `385003e41ce2`, 23,919 bytes, 176 lines (`hashlib.sha256`, newline-terminated line count).
> **This file is the reply.** It modifies no repository document, adjudicates nothing, moves no kill-line, and fills no project value form. Delivery is not adoption. No numerical proposed true value is offered for any of the 30 cells.

## 0. Identity, model, endpoint, tools

I am the addressee named on the commission header: **copilot agent**. I am not the grok addressee of the sister letter `letters/_commission_t2_t3_theory_inputs_grok_2026_10_17.md`. Restating the header is not this confirmation; this sentence is.

I am an AI assistant using Copilot SDK in VS Code.

```text
Exact serving model / version / build identifier: not exposed to this session. I will not approximate one.
Serving endpoint: not exposed to this session.
request.model string: not exposed to this session.
Date: 2026-10-17 (Asia/Shanghai). Exact request clock at the host is not exposed beyond the session date.
```

Tool calls used to prepare this reply:

1. Read-only inspection of the commission and of the local files listed in §7.
2. `hashlib.sha256` fingerprints of those files (first 12 hex characters, lowercase).
3. One read-only extraction of the 17 `T4` game tuples from `tools/exp_harness.py`, to check that each game's unique `value` argmax equals its `correct` field. That extraction did not call `ExperimentHarness`, did not sample decisions, and did not read a credential.

Not done: no experiment, no harness run, no write into `deposon-repo`, no upload, no credential read, no web retrieval, no literature search. I do not cite any paper I did not retrieve.

## 1. Source declaration

The commission points to a canonical source-declaration form at `results/_c4_theory_source_caliber_correction_2026_09_30.md`, SHA-12 `61b139efd0ef`, line 122. I searched the repository for that filename and for `*source_caliber*` / `*c4_theory_source*` and **did not find the file**. I therefore cannot verify that SHA-12 or that line, and I will not invent the form.

A workspace copy of the 2026-10-10 unblock reply quotes a declaration and attributes it to that path. I treat the following as a quotation from that reply, not as a verified reading of the missing file:

> 「理论界来源 ＝ codex 推导（PI 2026-09-30 采认；来源名按实际执行方更新——执行方择定＝codex，`ask_da8ce88762c1f39cb62e95f4` q1／q2；原字面「GLM 推导」历史留痕、0 回改）；0 自创 / 0 自拟公式，沿 C4.9 归零纪律」

**Executing party for this delivery, filling the source-name slot the commission leaves to the actual party:** copilot agent.

**Giver / venue for every registration, definition, and conditional expression originated below:** copilot agent, originated by the addressee under this commission; venue: this reply, 2026-10-17. No outside theorem is used. The algebra is written out. Where an expression is only a correction of another face's special case, that face is named and the expression is not adopted.

## 2. What this reply does with the 2026-10-15 proposal

I read the T-2/T-3 section of `REPLY_FROM_GEMINI4_GE01_THEORY_INPUTS_2026_10_15.md` (SHA-12 `44311ade19de`). I do not treat it, or the commission's audit summary of it, as settled.

| Piece | Disposition | Reason |
|---|---|---|
| On-disk `M1`/`M2` information minimum is a structural zero, to be registered rather than sold as a solution | **Accepted as a registration, not as a solved value** | Re-derived in §3 from the harness call `mech.choose(p['options'], p)`. The context dict contains `value` and `correct`. |
| `L(M1,T) = 3/14 · H` at `η=0.5`, `g_couple=1`, `g_aether=0.1`, offered for the `M1` cells | **Rejected** | Special case of one policy's error rate, not the spec's information-constrained minimum; holds only for 4 options with values `{1,0,0,0}`; the three parameters are constructor defaults, not frozen values. Arithmetic of that special case is confirmed in §3.5 and then not used. |
| `M2` left as structural zero under that relaxation | **Accepted as a registration** | Same key exposure. Assigning `0` as a solution would fail anti-degeneracy. |
| `3H/4` as an `M3` boundary inside an `L` delivery | **Rejected as `L` and as `U`** | It is the expected rejection count of one uniform policy under a 4-choice singleton key. The harness is not uniformly 4-choice. |
| Route 甲: memoryless harness, `U` underivable | **Accepted as the on-disk obstruction** | `choose` carries no `S_t`. |
| Route 乙 formula `U = H·τ_cert / [1-(1-γ)^H]`, claimed necessary and sufficient for all timings | **Rejected as a cell value; the displayed equality is not an iff** | It is a sufficient condition for one stipulated average-state certificate, tight only in a restricted mass range. `γ` and `τ_cert` are free. The state is not the harness. Counterexample in §4.4. |
| Route 丙: import a certificate from another protocol | **Rejected** | No cross-protocol map is proved here. I import no numeric threshold. |
| `τ_cert ∈ (0, 3/4)` | **Rejected** | `3/4` is the 4-choice self-check rate. Using it as a parameter domain is not a proof. |

## 3. `T-2` — `L(M,T)`

### 3.1 The object the spec names

From `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` (SHA-12 `423c84de20d5`), which I read in full:

```text
D(M, T) = E_π[ Σ_t |u*(a_t) - u(a_t)| / max_u ]
L(M, T) = lowest possible distortion under the LLM information bottleneck,
          to be derived from IC capacity and mechanism identifiability
U(M, T) = highest distortion the mechanism can tolerate,
          to be derived from a mechanism convergence condition
```

`max_u` is a task-family normalization constant. The spec does not freeze its numeric value, does not freeze `H`, and does not supply `Q(z|x)`.

A later calculator header (`tools/distortion_calculator.py`, SHA-12 `410a12482eef`) records a binary indicator track `u ∈ {0,1}` and `max_u = 1`, attributed there to a draft. I read that header. I did not read the function bodies, and I do not adopt the draft. The harness `value` maps are not binary on `T3`, `T4`, or `T5`. Any number that assumes one scoring for all five families is out of scope until a scoring is frozen. I use two readings below only as conditional statements, and I do not choose between them:

- **Indicator reading** (not adopted): loss `1` if the chosen action is not the generator's `correct` label, else `0`.
- **Value-gap reading** (the spec's written ratio, still not a frozen `max_u`): `u` is the `value` entry, `u*` is the max of those entries. The ratio is `0` when the chosen action attains the max, for any finite nonzero `max_u`.

### 3.2 What the harness actually passes to a mechanism

Verified against `tools/exp_harness.py`, SHA-12 `026575ff3829`, 41,428 bytes, 733 lines. Line numbers below are from this copy. Prior external line numbers are not used.

`ExperimentHarness.run` calls `mech.choose(p['options'], p)`. The second argument is the whole prompt dict. On the coded generators that dict includes `prompt`, `options`, `correct`, and `value`. `scatter_weight` is read in `DeposonMechanism.choose` and is not set by any generator in this file (`random.shuffle` occurs in `T1`, `T2`, `T3`, and `T5` only; `T4` has no shuffle). `llm_client` is stored and is not called by `run`.

So the information available at the `choose` call is not an LLM observation record. It includes the acceptance label and the payoff map. There is no finite table on disk of an LLM's intermediate observation `z`. I did not find one in the files I read, and I will not estimate one.

### 3.3 Two different minima, which must not be collapsed

**Class `Π_ctx`.** Every map from the context dict to an option in `options`. This class contains the rule "return `context['correct']`" and the rule "return an argmax of `context['value']`".

Under the indicator reading, the first rule has loss `0` on every generator instance. Under the value-gap reading, the second rule has loss `0` on every generator instance I checked (next paragraph). The information-constrained minimum of `Π_ctx` is therefore `0` on all 15 cells. That zero is **key exposure**. It is not an IC-capacity bound, and it is not a solution. It is registered as a structural zero.

The check that `value`'s unique argmax equals `correct`:

- `T1`: `value` is `1` on the correct string and `0` on the others. Unique.
- `T2`: `value` is `1` on the label and `0` on `Yes`/`No`/`Maybe`/`Always` otherwise. Unique. Options are shuffled; the value map is not.
- `T3`: `value` is `1.0` on `correct` and `0.5` on the other option. Unique.
- `T4`: 17 games extracted from this file. All 17 have a unique `value` argmax, and it equals `correct`. Two games have 3 options (`Mixed` appended); the other 15 have 2. No shuffle.
- `T5`: `correct = max(payoff)`, and the four payoffs in each coded scenario are pairwise distinct. Unique. Options are shuffled; `M1`/`M2` do not need the shuffle because they read `value`.

**Class `Π_M1`, `Π_M2`, `Π_M3`.** These are the singleton classes of the coded `choose` methods. Their "minimum" is a policy evaluation, not the minimum over `Π_ctx`, and not the spec's IC minimum.

- `Π_M2` = {argmax of `value`, first maximum in option order}. On the generators above the argmax is unique and equals `correct`, so this policy's loss is `0` under both readings, for every seed and every `H`. Realized `D(M2, T) ≡ 0` on the coded surface. That is still a structural zero, not an IC solution.
- `Π_M1` = {the T+R+A weight sampler in `DeposonMechanism.choose`, used because `scatter_weight` is absent}. This policy can select a non-argmax. Its expected loss is positive for the usual parameter region. That positive number is `D` of this policy. It is not `L`.
- `Π_M3` = {uniform `random.choice(options)`}. This policy ignores context. Its expected indicator loss is `1 - 1/n_t` when exactly one option is accepted and `n_t = |options|`. That is `D` of this policy. The commission forbids using it as `L` or as `U`.

The five assumptions of the 2026-10-10 conditional minimum (fixed `H`; laws exogenous to actions; `Z_t` contains everything the rule sees; every map from `Z_t` to an action is admissible; actions do not change later information or rewards) are the assumptions stated in that reply, which I read. I did not open the null-resolution design, so I am not attesting to a line numbered 91 there.

| Assumption | On this harness |
|---|---|
| Fixed `H` | Fails all 15 cells. Spec §3.3 writes family sizes 20/20/20/10/20 and also "≈33" decisions per task. `run` defaults to 25. `T5.generate_prompts` defaults to 20. No value is frozen, so I bind none. |
| Exogenous laws | The generators do not depend on previous actions. This holds for the coded task law. It does not supply the missing `Q`. |
| `Z_t` is everything the rule sees | For a rule called as `choose(options, p)`, `Z_t` includes `correct` and `value`. That is the identity channel on the key. |
| Every map from `Z_t` is admissible | Holds for `Π_ctx` only. Fails for `Π_M1`, `Π_M2`, and `Π_M3`, which are singletons dictated by the mechanism. A closed form proved for `Π_ctx` does not transfer to those singletons. |
| No action-to-future-information feedback | Holds on the memoryless harness. It would fail for a state process that fed `S_t` back into later observations. I do not add that process. |

### 3.4 Why withholding `value` still does not price a cell

A design change that removes `value` and `correct` from the object passed to `choose` would remove this particular identity channel. I state that change and do not price it.

It is not sufficient for a non-degenerate IC minimum over all maps from the remaining prompt:

- `T1`: the prompt contains the arithmetic expression. A map that evaluates it attains indicator loss `0`.
- `T3`: the prompt contains `type={trap}`, and `t3_answer` is a deterministic function of that type.
- `T4`: the prompt contains the game name and the payoff table. There is no shuffle. Option order is a function of the game id.
- `T5`: the numeric payoffs are not in the prompt text, but each scenario title in the coded list determines a fixed payoff table. A memorizing map from title to action attains loss `0` over the unrestricted class.
- `T2`: I did not read every question string. The generator binds each prompt to a label in a fixed table and shuffles four labels. Over all functions of a finite prompt set with a deterministic label, the unrestricted minimum is again `0` if each prompt has one label. I do not need the question text to see that this is memorization, not a measured capacity.

A non-degenerate `L` in the spec's sense needs a capacity restriction that is not "all functions of the prompt" and not "the coded mechanism." No such finite rule list, with the five assumptions annotated as holding, is on the files I read. The surface class that ignores prompt content and uses only position or lexical form measures the label prior, not IC capacity. I did not re-run that probe and I adopt none of its frequencies. I will not invent a bit budget, a template-rule list, or a channel frequency table. An invented channel would be a stand-in. The commission prefers a null with a reason.

### 3.5 Correction of the `3/14 · H` special case — not a delivered value

When `scatter_weight` is absent and `best = max value > 0`, the coded `M1` weight is

```text
w(o) = (1 - η) · 1{v(o) = best} + η · g_couple · (v(o) / best) + g_aether
P(o) = w(o) / Σ_o w(o)     if the sum is positive
```

`η`, `g_couple`, and `g_aether` are constructor defaults `0.5`, `1.0`, and `0.1`. They are not frozen. I do not evaluate a cell at those defaults.

If there are 4 options, one with value `1` and three with value `0`, then

```text
w* = (1 - η) + η · g_couple + g_aether
w0 = g_aether
P(miss) = 3 · g_aether / ((1 - η) + η · g_couple + 4 · g_aether)
```

At the defaults, `w* = 1.1`, `w0 = 0.1`, total `1.4`, `P(miss) = 0.3/1.4 = 3/14`. That arithmetic is right. It is the indicator error rate of this one sampler on that one value pattern. It is also the error rate of the identity map on a single draw from that sampler. Either reading is a policy evaluation under a stipulated channel. Neither is `L(M,T)` for a cell, and the pattern is not the harness pattern outside `T1` and `T2`.

Scope, still not a cell value:

- `T3` has 2 options, values `1.0` and `0.5`. Then `w* = (1-η)+η·g_couple+g_aether` and `w_other = 0.5·η·g_couple+g_aether`. At the defaults, `P(select other) = 0.35/1.45 = 7/29`. Under the indicator reading the per-decision loss is `7/29`. Under the value-gap reading with `max_u = 1` it is `(1/2)·(7/29) = 7/58`. I deliver neither.
- A 2-option pattern with values `{1,0}` would give `P(miss) = g_aether / ((1-η)+η·g_couple+2·g_aether)`, which is `1/12` at the defaults. `T4` is not that pattern. Fifteen `T4` games have cardinal values; `T4-N05` has `best = 0`, so the code takes the `best > 0` branch as false, sets every reflection term to `0`, and puts transmission only on `Mixed`.
- `T5` has four distinct positive payoffs. The weights depend on `v/best`. The 4-choice zero-distractor formula does not apply.

`H` remains unbound, so even a legitimate per-decision rate would not become a count-scale `L`.

### 3.6 Per-cell delivery, all 15 cells

Observation-law ID for every row: `Q-harness-ctx-026575ff3829` — the context dict actually passed to `choose` on this file. That law is a design fact of the code, not an estimate from LLM records.

Policy-class IDs: `Π_ctx`, `Π_M1`, `Π_M2`, `Π_M3` as defined in §3.3.

Key-face ID: `K-unfrozen`. The generator field `correct` is not a PI-frozen key schedule. `H` is unbound, so the six-tuple required for a value cannot be completed. No row binds a number.

Level key: **fail** = that level is not achieved for a solution; **reg** = the anti-degeneracy registration is done and is not a solution.

| Cell | Delivery | Class whose minimum is 0 | Class that must not be relabeled `L` | L-甲 | L-乙 | L-丙 | L-丁 | L-戊 |
|---|---|---|---|---|---|---|---|---|
| M1×T1 | Registered structural zero. Non-degenerate `L` not given. | `Π_ctx` | `Π_M1` (4-choice binary sampler; its error rate is `D`, not `L`) | fail | fail | fail | fail | reg |
| M1×T2 | Registered structural zero. Non-degenerate `L` not given. | `Π_ctx` | `Π_M1` (same sampler; label set is 4-choice binary) | fail | fail | fail | fail | reg |
| M1×T3 | Registered structural zero. Non-degenerate `L` not given. | `Π_ctx` | `Π_M1` (2 options, values 1.0 and 0.5; not the 4-choice formula) | fail | fail | fail | fail | reg |
| M1×T4 | Registered structural zero. Non-degenerate `L` not given. | `Π_ctx` | `Π_M1` (2 or 3 options, cardinal values, no shuffle; `T4-N05` has `best=0`) | fail | fail | fail | fail | reg |
| M1×T5 | Registered structural zero. Non-degenerate `L` not given. | `Π_ctx` | `Π_M1` (4 distinct positive payoffs; zero-distractor formula does not apply) | fail | fail | fail | fail | reg |
| M2×T1 | Registered structural zero. Non-degenerate `L` not given. | `Π_ctx` and `Π_M2` | Do not report `0` as a solved bound | fail | fail | fail | fail | reg |
| M2×T2 | Registered structural zero. Non-degenerate `L` not given. | `Π_ctx` and `Π_M2` | Do not report `0` as a solved bound | fail | fail | fail | fail | reg |
| M2×T3 | Registered structural zero. Non-degenerate `L` not given. | `Π_ctx` and `Π_M2` | Do not report `0` as a solved bound | fail | fail | fail | fail | reg |
| M2×T4 | Registered structural zero. Non-degenerate `L` not given. | `Π_ctx` and `Π_M2` | Do not report `0` as a solved bound. No-shuffle position is not an IC law. | fail | fail | fail | fail | reg |
| M2×T5 | Registered structural zero. Non-degenerate `L` not given. | `Π_ctx` and `Π_M2` | Do not report `0` as a solved bound | fail | fail | fail | fail | reg |
| M3×T1 | Not given. | `Π_ctx` is a structural zero and is not a solution. `Π_M3` is uniform on 4 options. | `3H/4` is a self-check of that uniform policy under a singleton key, not `L`. | fail | fail | fail | fail | reg |
| M3×T2 | Not given. | Same split. | Same. `n=4`. `3H/4` is not `L`. | fail | fail | fail | fail | reg |
| M3×T3 | Not given. | Same split. | Uniform on 2 options. Indicator self-check is `H/2` if the key is singleton, not `3H/4`, and still not `L`. | fail | fail | fail | fail | reg |
| M3×T4 | Not given. | Same split. | No shuffle. `n=2` on 15 games and `n=3` on 2 games, cycled by `i mod 17`. No single `3H/4`. Not `L`. | fail | fail | fail | fail | reg |
| M3×T5 | Not given. | Same split. | Uniform on 4 options. `3H/4` is not `L`. Prompt memorization over `Π_ctx` is a different structural zero. | fail | fail | fail | fail | reg |

L-甲 fails because the required object is a finite IC observation table, and the only complete law I can state is the degenerate context channel. L-乙 fails because no admissible class both matches the mechanism and satisfies the five assumptions on the cell. L-丙 fails because the `Π_ctx` expression is the constant `0`, which is the degeneracy, and the sampler expression is not that class's minimum. L-丁 fails because no six-tuple is bound. L-戊 is the registration itself.

**`T-2` verdict: underivable as stated (obstruction: the on-disk observation available to `choose` is the key-bearing context, so the information-constrained minimum is a structural zero and not an IC-capacity solution; the mechanism singletons are policy evaluations, not that minimum; no non-degenerate finite `Q`, frozen key face, frozen `H`, or matching policy class is instantiated; `3/14·H` is rejected).**

## 4. `T-3` — `U(M,T)`

### 4.1 On-disk obstruction

`DeposonMechanism.choose`, `GreedyMechanism.choose`, and `RandomMechanism.choose` are functions of the current arguments only. No field of those classes stores `S_t`. `run` does not pass a state from decision `t` to decision `t+1`. The option sampler in `M3` is uniform on the current option list by construction of `random.choice`. That stationary sampling law is not convergence of an action sequence. I will not call it a certificate.

A count bound `0 ≤ D ≤ H` under the indicator reading, if `H` were frozen, would still not be a convergence tolerance. A bounded mistake count does not prove that a state process converges. I do not set `U = H`. That assignment would be vacuously large.

I do not import a threshold, an `ε`, or a certificate from any other protocol. I did not retrieve the performative-prediction papers named in the sourcing note, and I do not use them as a value or as a numerical anchor.

### 4.2 `M2`: register `U`, do not assign it

Under both readings in §3.1, the coded `M2` policy has loss `0` on every instance the generators emit. So `D(M2, T) ≡ 0` on `T1`–`T5` for any `H`, as a property of the code, not as a measurement from a run I executed.

If the inequality to be certified is `D ≤ U`, every `U ≥ 0` satisfies it when `D ≡ 0`. `U` is not identified. Assigning one would be fabrication. This registration is per cell, not a number.

This does not extend to `M1` or `M3`. Their coded policies do not have identically zero loss. Their `U` fails for a different reason: there is no state and no bridge.

### 4.3 What I will not originate as a cell value

The commission allows an originated transition law. An originated law that is not the harness is a definitional revision of "mechanism." I can write the algebra of one such revision and show that it still does not bind a cell. I do not propose it as `U(M,T)`.

Originated objects, all unbound, all not the harness:

```text
state-process ID:  SP-copilot-2026-10-17-not-harness
certificate ID:    C-avg-unbound
perturbation-map ID: BR-sufficient-not-iff
```

Let `γ ∈ (0,1)` and `τ ∈ (0,1]` be symbols, not chosen numbers. Let `ℓ_k ∈ [0,1]` be a per-decision normalized loss, `k = 0,…,H-1`, and let `D = Σ_k ℓ_k`. The assumption `ℓ_k ≤ 1` is an extra stipulation. It is not proved for `T4`/`T5` under `max_u = 1`, because those `value` gaps can exceed `1`. Let `S_0 = 0` and

```text
S_{t+1} = (1 - γ) S_t + γ ℓ_t
```

Unrolling,

```text
S_t = γ Σ_{k=0}^{t-1} (1-γ)^{t-1-k} ℓ_k
Σ_{t=1}^{H} S_t = Σ_{k=0}^{H-1} (1 - (1-γ)^{H-k}) ℓ_k
```

The coefficient of `ℓ_k` in the sum is `1 - (1-γ)^{H-k}`. It is largest at `k = 0`, where it equals `1 - (1-γ)^H`, and smallest at `k = H-1`, where it equals `γ`.

Define the average `S̄_H = (1/H) Σ_{t=1}^{H} S_t`. The certificate `S̄_H ≤ τ` for every timing of a given `D` is a universal claim. A sufficient condition is obtained by pretending every unit of `D` sits on the largest coefficient:

```text
D ≤ H · τ / (1 - (1-γ)^H)
```

That is the displayed Route 乙 formula. It is sufficient. It is not necessary, and it is not tight for every `D`, because only the first coordinate has the maximum coefficient. For `D > 1` the worst timing must spill onto strictly smaller coefficients when `γ ∈ (0,1)` and `H > 1`.

### 4.4 Counterexample to the iff claim

Take `H = 2`, `γ = 1/2`, `τ = 1/2`. Then `1 - (1-γ)^H = 3/4`, and the formula returns

```text
U = 2 · (1/2) / (3/4) = 4/3
```

Coefficients in `Σ S` are `3/4` at `k = 0` and `1/2` at `k = 1`. Put mass `1` on `k = 0` and `1/3` on `k = 1` (total `D = 4/3`):

```text
Σ S = 3/4 + (1/2)·(1/3) = 11/12
S̄_2 = (11/12)/2 = 11/24 < 1/2
```

The certificate still holds at the formula's claimed bound, so that bound is not the exact tolerance. The tight robust total, filling the larger coefficient first, solves `3/4 + (1/2)·x = 1` with `x ≤ 1`, hence `x = 1/2` and `D = 3/2`, which is strictly larger than `4/3`.

The same formula can exceed `H`. Whenever `τ > 1 - (1-γ)^H`, the displayed expression is larger than `H`. A tolerance above the indicator domain of `D` is not an identified same-scale bound. I will not cap `τ` by `3/4` to hide that.

Direction, stated so it cannot be swapped: the formula is a sufficient robust tolerance for the average-state certificate under worst-case timing. It is not the tolerance for the terminal state `S_H` (whose largest coefficient is `γ`, on the last step). It is not necessary. It is not a property of `M1`, `M2`, or `M3` as coded.

### 4.5 Per-cell delivery, all 15 cells

No row binds `(value, certificate ID, state-process ID, perturbation-map ID, cell)` to a number. The IDs in §4.3 name an unbound illustration, not a cell certificate.

| Cell | Delivery | Why `U` is not assigned | U-甲 | U-乙 | U-丙 | U-丁 | U-戊 |
|---|---|---|---|---|---|---|---|
| M1×T1 | Not given. | Memoryless `choose`. No transition, no target, no bridge. Domain bound `H` would be vacuous. Sampler error is `D`, not `U`. | fail | fail | fail | fail | fail |
| M1×T2 | Not given. | Same. | fail | fail | fail | fail | fail |
| M1×T3 | Not given. | Same. 2-option value pattern does not create a state. | fail | fail | fail | fail | fail |
| M1×T4 | Not given. | Same. No-shuffle and cardinal payoffs do not create a state. | fail | fail | fail | fail | fail |
| M1×T5 | Not given. | Same. | fail | fail | fail | fail | fail |
| M2×T1 | Registered, not assigned. | `D ≡ 0` under §3.1 on the coded policy, so every `U ≥ 0` satisfies `D ≤ U`. | fail | fail | fail | fail | reg |
| M2×T2 | Registered, not assigned. | Same. | fail | fail | fail | fail | reg |
| M2×T3 | Registered, not assigned. | Same. | fail | fail | fail | fail | reg |
| M2×T4 | Registered, not assigned. | Same. Unique value argmax equals `correct` on all 17 games. | fail | fail | fail | fail | reg |
| M2×T5 | Registered, not assigned. | Same. | fail | fail | fail | fail | reg |
| M3×T1 | Not given. | Uniform sampling is not sequence convergence. `3H/4` is not `U`. | fail | fail | fail | fail | fail |
| M3×T2 | Not given. | Same. | fail | fail | fail | fail | fail |
| M3×T3 | Not given. | Same. `H/2` self-check is not `U`. | fail | fail | fail | fail | fail |
| M3×T4 | Not given. | Same. Option count is 2 or 3. No single chance rate is `U`. | fail | fail | fail | fail | fail |
| M3×T5 | Not given. | Same. `3H/4` is not `U`. | fail | fail | fail | fail | fail |

**`T-3` verdict: underivable as stated (obstruction: the three coded mechanisms are memoryless, so there is no transition law, no convergence target, and no proved bridge from `D` to a tolerated perturbation; `M2` has `D ≡ 0` on the coded surface, so any `U` would be unidentifiable and is registered rather than assigned; the Route 乙 closed form is a sufficient condition on a state process that is not the harness, is not an iff, and is not a cell value).**

## 5. Constraints I am not moving

The kill-lines in the spec are not mine. I do not recommend a retroactive change to `kill_decision`, to `2.0`, to `1.5`, to `1.8`, or to the `0.3` / `0.1` hit-rate cuts. Because I deliver no `U`, I also deliver no `theory_U_hit_rate`. That is an absent input, not a proposed edit.

I do not equate a mistake count with convergence, a rate with a count, or an unbound symbolic expression with a cell value. I do not use `D(M3) = 3H/4` as `L` or as `U`. I do not use constructor defaults as frozen parameters. I do not close `R-8`, open a run, or write into the project's value form.

## 6. Recompute notes

A third party can check the following from this text and from `exp_harness.py` at SHA-12 `026575ff3829`, without adopting any cell value:

1. `run` passes the full prompt dict into `choose`.
2. `M2` returns the first argmax of `value`. On `T1`, `T2`, `T3`, and `T5` that argmax is `correct` by the generator expressions. On `T4`, extract the 17 tuples and compare, as I did: 17/17 unique matches.
3. The 4-choice zero-distractor weight ratio reduces to `3·g_aether / ((1-η)+η·g_couple+4·g_aether)`, and the defaults give `3/14`. Then refuse it as a cell value for the reasons in §3.5.
4. The average-state unroll in §4.3, and the `H=2`, `γ=1/2`, `τ=1/2` counterexample: formula `4/3`, actual worst-case average at that total `11/24 < 1/2`, tight robust total `3/2`.

## 7. Files I read, with fingerprints I computed

| File | SHA-12 | Bytes | Lines | How used |
|---|---|---:|---:|---|
| `letters/_commission_t2_t3_theory_inputs_copilot_agent_2026_10_17.md` | `385003e41ce2` | 23919 | 176 | Commission. Read in full. |
| `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | `423c84de20d5` | 15457 | 177 | Spec. Read in full. Matches the commission's on-disk measurement, not the other pack's `aab9d78ada2d`. |
| `results/_t2_t3_value_request_form_2026_10_14.md` | `21abb5173b87` | 15054 | 172 | Five-level criteria and empty value form. Read in full. |
| `results/_t2_t3_value_sourcing_2026_10_15.md` | `bcb0d60fdd2d` | 24658 | 246 | Read through the S-1–S-6 register. Did not adopt its frequencies or its recommendation as a premise. My null is re-derived. |
| `tools/exp_harness.py` | `026575ff3829` | 41428 | 733 | Mechanisms, generators, `run`. Read those parts. T4 tuples extracted. |
| `tools/distortion_calculator.py` | `410a12482eef` | 40611 | 861 | Header and constants only. Function bodies not reviewed. |
| Workspace `REPLY_FROM_GEMINI4_GE01_THEORY_INPUTS_2026_10_15.md` | `44311ade19de` | 44520 | 266 | T-2/T-3 section read and rejected as a value. Same SHA-12 the commission cites for the letters copy. |
| Workspace `c4_values_reply_2026_10_10/_codex_c4_values_unblock_reply_2026_10_10.md` | `a975c7990cd8` | 21486 | 143 | Conditional minimum, `null-L` / `null-U` blockers, `3H/4` self-check. Read. |

Not found: `results/_c4_theory_source_caliber_correction_2026_09_30.md`. Not opened: the null-resolution design, the audit register, and the sister grok commission. I do not rely on them.

The fingerprint of **this reply** is not written in this file. It is reported with the delivery, outside this file.
