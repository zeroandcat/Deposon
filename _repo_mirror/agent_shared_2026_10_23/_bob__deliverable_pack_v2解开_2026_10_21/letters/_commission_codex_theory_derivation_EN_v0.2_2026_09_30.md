# Commission: Theory Derivation — C4 Theory Inputs, P-B Distortion Bound V0 · English version for codex · **V0.2 (refresh · the executor is ruled = codex)**

> **To**: codex (the **theory derivation party**; **the PI ruled on 2026-09-30 that the executor is codex** — 择定卡 `ask_da8ce88762c1f39cb62e95f4` q1「执行方择定＝codex（英文版）」, and that landing was confirmed by `ask_ead0d2f7dc818155041ee0cb` q1「按此稿落」. This version is therefore addressed to you **as the ruled executor**, and the declaration your product must carry names **you** as the source — see §3.5. The same task exists in Chinese as `letters/_commission_glm_theory_derivation_2026_09_30.md`, which was addressed to GLM; **that route was not chosen** and that document is retained on file for comparison only, 0 bytes changed (§11))
> **From**: doc-writer (`agent-0032834a3e04`, deposon drafting lane) | **Commissioning party**: the deposon project PI
> **Date**: 2026-09-30
> **Version**: **v0.2** · **v0.1 is superseded by v0.2** · v0.1 = `letters/_commission_codex_theory_derivation_EN_2026_09_30.md` (`af50969bebe2`, 66,754 B, 401 lines) — **0 bytes changed by this version**, retained as the historical record. The change history v0.1 → v0.2 is in §9 item 16
> **Status**: 🚫 **draft · pending PI review and release** (⛔ **0 sent / 0 pushed / 0 forwarded**; the moment of release is the moment the commission takes effect, and it takes effect and locks at that moment). ⚠️ **Everything v0.1 left open is now closed by the PI's 2026-09-30 rulings** (who the executor is; how the source name lands) ⇒ **this version is complete as written and is ready for review-and-release**; nothing in it waits on a further decision
> **Why this letter exists (honestly stated)**: we have a **kill-line** that cannot be landed, because the four theory-side inputs of a preregistered distortion measure have not arrived (§0.1). On 2026-09-30 the PI ruled that the source of the theory bound is a derivation by a named outside party, that this task is to be commissioned in English, and then **chose the executor: codex**; the source name in the canonical declaration was **updated to the actual executor accordingly**. This letter is that commission: **the same task, the same task surface, the same material ledger** as the Chinese version, recast in English for the executor the PI chose, carrying the canonical declaration as it now stands on disk. ⛔ **It still decides nothing on our own authority**: it does not adjudicate the open boundary of §3.3, it does not decide whether a cut-point is reasonable, and it does not decide whether your product is adopted — adoption is the PI's call through our process
> **Chinese counterpart**: `letters/_commission_glm_theory_derivation_2026_09_30.md` (`344f5b9e0b08`, 32,472 B, 285 lines — **re-measured 2026-09-30, unchanged**) — the Chinese version of the same task, addressed to GLM. Per the established counterpart rule (precedent: `letters/_v5_rj5_external_rederive_request_EN_2026_09_28.md` §7), **in the event of any discrepancy, the Chinese original together with the upstream documents as measured on disk governs**; the discrepancy is to be registered in the erratum chain, not silently reconciled. That document is **0-touched (0 bytes changed)** by this version
> **Evidence level of the PI's rulings (honest, E-C transcription)**: the questionnaire records behind these rulings are **not on disk** —— a filename scan for questionnaire record artifacts returns **0 files**; the ids `ask_3b8a6489fb38917e42a69ecd` (the first ruling), `ask_da8ce88762c1f39cb62e95f4` (the executor choice) and `ask_ead0d2f7dc818155041ee0cb` (the landing confirmation) occur in this repository **only inside our own documents**, as citations and transcriptions (23 / 15 / 12 occurrences across 6 / 6 / 5 files respectively, measured 2026-09-30). ⇒ **This letter does not pose as the original questionnaire record.** The rulings are nevertheless **independently corroborated by the current state of the on-disk documents** (see §3.1), so the citation here does not rest on the transcription alone
> **Ledger (4 documents, read-only; measured on this machine 2026-09-30, this session)**: ① acquisition request `results/_v5_theory_input_acquisition_request_2026_09_29.md` (**current `83afc4802fe7`**, 10,691 B, 116 lines) ② supplement `results/_theory_input_request_supplement_2026_09_29.md` (**current `c966e7b605af`**, 48,190 B, 431 lines; contains the PI's 2026-09-30 adoption register §8) ③ spec `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` (**current `423c84de20d5`**, 15,457 B, 177 lines; ⚠️ the two registered older values `bb7ca9838150` and `8aba2837bc6a` are stale — see §2.8) ④ **C4 caliber-correction register** `results/_c4_theory_source_caliber_correction_2026_09_30.md` (**current `246344c5f215`**, 20,165 B, 189 lines; **whose §2.3 carries the new canonical C4.7 declaration text — the one your delivery is to adopt**)
> **Style anchors**: `letters/_v5_rj5_external_rederive_request_EN_2026_09_28.md` (`498215a9ec7d`, 51,013 B, 415 lines, the English external-derivation precedent, including the anti-downgrade clause) and the codex reply to it (`c706e69d00fc`, 27,835 B, **out-of-repository**, at `〔本机用户目录〕\codex-workspace\rj5_reply_2026_09_29\` —— **re-measured 2026-09-30 and still identical**; a reader of this letter **cannot** verify it from this repository) — the model-declaration precedent followed here
> **This letter does not write**: any GitHub URL, any GLM model name / version, any key or credential. The source name 「codex 推导」 is **carried verbatim from the register's canonical text** (a PI-ruled wording we did not draft)
> **Encoding**: UTF-8 without BOM · LF. **The fingerprint is not written into this file** (measured after landing, reported with the receipt)

---

## §0 The main line and the hard constraints

### §0.1 The main line (one paragraph)

We have a **kill-line** hanging in mid-air: a preregistered distortion measure `D(M, T)` together with its theoretical lower and upper bounds `L(M,T)` / `U(M,T)`, whose **four theory-side inputs have not arrived to this day** (`u*(a_t)`, `L`, `U`, the `max_u` normalization caliber) — which makes the measure **not computable in mathematics** and the kill-line impossible to land. On 2026-09-30 the PI ruled that **the source of the theory bound is a derivation by a named outside party** (the source name was first recorded as GLM, and has since been **updated to the actual executor: derivation by codex**); on the same day the PI ruled that this commission is to be recast in English for codex, and then **chose the executor: codex**. This letter commissions **you**, the ruled executor, to **derive** those four inputs, and the declaration your product must carry names **you** as the source (§3.5).

**This commission contains no reply outline** (PI ruling of 2026-09-24: commissioning materials contain no outline; the addressee is left free to develop it): the structure, the level of detail, the derivation path and the writing style are **all for you to decide**. We give only **what shape is wanted**, **what it is for**, **the hard constraints**, and **the full material ledger** (§2 quotes our on-disk wording item by item, enough for you to judge applicability, with 0 need for you to go and look anything up — unless you have CLI access and prefer to read the originals, see §4.2).

### §0.2 Hard constraints (non-negotiable; violation = stop work and report)

| # | Hard constraint |
|---|---|
| **H1** | **0 keys**: 0 into the prompt, 0 into JSON, 0 into logs, 0 into any deliverable, 0 restatement (alongside the spec §9 "key safety" line and the R4 rule) |
| **H2** | **Honest attribution · 0 impersonation**: the reply is issued **under your own name (codex)**; ⛔ 0 use of the name of worker / verdict-keeper / evidence-auditor / protocol-keeper / doc-writer / Trae code / COZE / KIMI / GLM / 〔W老师〕 or any other party; ⛔ 0 certify any of our **pre-existing conclusions** under your own name |
| **H3** | **0 touching our existing documents**: all ledger documents of §6 are **read-only** — 0 modification, 0 overwrite, 0 deletion; this commission and the reply **0 modify** any existing verdict, preregistration, anchor document or erratum chain |
| **H4** | **0 self-filled gaps** (the zeroing discipline): if any item is missing ⇒ we judge "**not computable + γ**"; ⛔ **0 fill it with an estimated value / a substitute value / a self-invented formula** (following the already-in-force wording of C4.9) |
| **H5** | **0 unsourced placeholder formulas**: every deliverable **carries its own source attribution** (**who gave it / where it comes from**); ⛔ 0 unsourced placeholder formulas (following the already-in-force wording of C4.7, plus the house convention of a declaration line inside the deliverable) |
| **H6** | **0 unauthorized threshold changes**: every cut-point listed in this letter (`2.0` / `0.3` / `1.5` / `1.8` / `0.1` / `±5%` / `10k resamples` / `>30%` / `>40%` / `>0.2`) is **carried at our existing on-disk wording, not one character altered**; ⛔ 0 create, 0 adjust, 0 replace on grounds of "being more reasonable" |
| **H7** | **0 fabrication**: where a derivation skips a step, **write the skip down explicitly**; where a source cannot be obtained, **write `null`** and attach the list of channels already searched — "I could not find it" is a qualified reply; "let me guess one" is not |
| **H8** | **0 automatic effect**: the reply is **not automatically adopted**, does not automatically land in any position, does not automatically amend the spec; whether it is adopted, and when, is decided by **the PI + our adoption process** |
| **H9** | **0 half-side conclusions**: ⛔ 0 report only the favourable half on the grounds of "U is missing" or "coverage is insufficient" |

---

## §1 Task surface: what shape is wanted (T-1 ~ T-4 · **at the request document's own standard · 0 content drafted on your behalf**)

> ⭐ **This section fills in 0 content**: it states only "what shape is wanted". ⛔ **It does not state "what the content is"**, and ⛔ it pre-fills no expression, no numerical value, no per-cell coverage value and no attribution. The four rows below are **carried from** the acquisition request **`83afc4802fe7`** §3 (0 rewritten, 0 added, 0 deleted; the T-1 ~ T-4 wording was re-verified line by line on 2026-09-30 and is unchanged), rendered into English here so that this letter is executable on its own.

| # | Item requested | Our existing on-disk basis | **Shape required (what you are to give)** |
|---:|---|---|---|
| **T-1** | **The payoff `u*(a_t)` of the theoretically optimal decision** | spec §3.4: 「`u*(a_t)`: **理论最优决策的支付**」 = "the payoff of the theoretically optimal decision" | Required: **(a) a definition or a construction rule** (the domain of `a_t` and the reachability assumption) **(b)** the **comparability premise** with `u(a_t)` (the same normalization) **(c)** if it depends on mechanism-internal quantities (IC capacity / identifiability / convergence conditions), **that quantity's expression or a computable definition must be given** |
| **T-2** | **The theoretical lower bound `L(M, T)`** | spec §3.5: 「**下界 L(M, T)**：LLM 信息瓶颈下的**最低可能失真**（由 **IC 容量 + 机制可辨识性**推出）」 = "**lower bound L(M, T)**: the minimum possible distortion under the LLM information bottleneck (derived from **IC capacity + mechanism identifiability**)" | Required: **the expression + the definition of IC capacity + the identifiability criterion** |
| **T-3** | **The theoretical upper bound `U(M, T)`** | spec §3.5: 「**上界 U(M, T)**：**机制可承受的最高失真**（**机制收敛性条件**推出）」 = "**upper bound U(M, T)**: the highest distortion the mechanism can withstand (derived from **the mechanism's convergence condition**)" | Required: **the expression + the convergence condition**. ⚠️ **`U` is the direct input to the kill decision** (see §2.3) ⇒ **its absence blocks the entire kill-line** |
| **T-4** | **The normalization constant `max_u` caliber** | spec §3.4: 「`max_u`: **支付上界（任务族归一化常数）**」 = "`max_u`: the payoff upper bound (the task-family normalization constant)" | Required: **the normalization rule** (what value is taken per task family T / whether it varies with T). ⚠️ **`max_u` sits in the denominator ⇒ the caliber directly changes the order of magnitude of `D(M,T)`** |

### §1.1 Three acceptance-layer sub-clauses (attached to the four items; they take effect **together with** the table above, and do not replace it)

> The three rows below are carried from the supplement **`c966e7b605af`** §8.4 (added by the PI's 2026-09-30 adoption ⑤; **0 rewrite of the existing wording of T-1 ~ T-4**; the three formal clause wordings below were **re-read at their on-disk lines L344 / L354 / L363 on 2026-09-30 and are unchanged**). **Conjunctive (AND)**: if any clause is missing, **0 downgrade, 0 exemption**.

| Clause | Attached to | **Formal clause wording (verbatim, Chinese) + English rendering** |
|---|---|---|
| **A** | T-1 | **`u*(a_t)` 交付件须含「来源标注（给出人 / 出处）」＋「适用范围声明」；适用范围声明须就 5 任务族 T1 – T5 × 3 机制 M1 – M3 逐格标注该式之覆盖情况（逐格标注，0 以整句概括替代）。**<br>EN: "The `u*(a_t)` deliverable must contain a source attribution (who gave it / where it comes from) and a scope-of-applicability declaration; the scope declaration must annotate, cell by cell, the coverage of that expression across the 5 task families T1 – T5 × 3 mechanisms M1 – M3 (cell by cell; 0 substitution of a whole-sentence generalization)." |
| **B** | T-2 / T-3 | **`L(M,T)`（附 T-2）与 `U(M,T)`（附 T-3）交付件须逐项含「来源标注（给出人 / 出处）」；推出依据分别为 IC 容量 ＋ 机制可辨识性（T-2）、机制收敛性条件（T-3），该两项依据已列于 T-2 / T-3，本条款 0 重复其要求、仅补其逐项来源标注。**<br>EN: "The `L(M,T)` (attached to T-2) and `U(M,T)` (attached to T-3) deliverables must each contain a source attribution (who gave it / where it comes from); the bases of derivation are respectively IC capacity + mechanism identifiability (T-2) and the mechanism convergence condition (T-3); those two bases are already listed under T-2 / T-3, and this clause 0 repeats their requirement and only adds their item-by-item source attribution." |
| **C** | T-4 | **`max_u` 交付件须「逐任务族 T1 – T5 逐格给出取值 ＋ 逐格来源」：即 T-4 所问「归一化规则」须落为逐任务族逐格给值 ＋ 逐格来源；0 只给统一常数而 0 给逐格值，0 只给规则而 0 给值。**<br>EN: "The `max_u` deliverable must give a value cell by cell for each task family T1 – T5 plus a per-cell source: that is, the "normalization rule" asked for in T-4 must land as per-task-family, per-cell values plus per-cell sources; 0 giving only a single constant with 0 per-cell values, 0 giving only a rule with 0 values." |

> 📌 **The cell-count convention**: the number "15" is simply the **arithmetic expansion of 5 × 3**, **0 new tiering, 0 new cut-point**.

### §1.2 Delivery form

| Item | Requirement (at our on-disk wording) |
|---|---|
| **Form** | **1-page theory** (spec verbatim: 「需…给 1-page theory 落地」 = "needs a 1-page theory to land it") — ⛔ the length is a **reference scale, not a format straitjacket**; if some derivation exceeds 1 page, **state clearly what exceeds it — 0 deleting derivation steps in order to compress the length** |
| **Landing** | spec verbatim: 「落到 `tools/distortion_calculator.py`」 = "lands in `tools/distortion_calculator.py`" ⇒ **the landing is dispatched by the PI / our execution lane**; ⛔ **your side 0 creates that file for us, 0 writes code on our behalf** |
| **0 variants** | ⛔ 0 asked to rewrite the spec, 0 asked to add cells, 0 asked to extend the task families (**0 using the theory input as a pretext to widen scope**) |

---

## §2 Background and use (**the full material ledger · everything quoted from our on-disk wording**)

> This section is for you to judge what properties these four inputs must satisfy and what they will be used for. **It is all quotation**; we **endorse the correctness of none of it**, and **hint at no particular theoretical form**.

### §2.1 What this measure is doing (spec §1 / §3.1 – §3.3, literal points, rendered into English)

- **Objective**: V0 answers "**when an LLM player replaces a Bayesian player, does the total distortion `D(M, T)` of the deposon three-channel scattering mechanism fall within the [theoretical lower bound, theoretical upper bound] interval**".
- **Core question**: **how much extra distortion does the LLM player's bounded rationality cause?** The baseline is the Bayesian player (knows the mechanism + the payoffs ⇒ **distortion = 0**); V0 measures the LLM player's **distortion multiplier** relative to that baseline: D multiplier = D_LLM / D_Bayesian (value **≥ 1**).
- **Players**: the LLM player = **Doubao + DeepSeek** (sharing `llm_client.py` with P-A); the Bayesian baseline player = the **theoretically optimal response calculator** (knows the mechanism + the payoffs ⇒ distortion = 0); **unified decision space: choose 1 of 4**.
- **Mechanisms (M, three)**: **M1** Deposon T+R+A three-channel (ported from the deposon scattering layer) | **M2** pure Greedy (no field, no conservation constraint) | **M3** Random baseline (uniform sampling of the decision).
- **Task families (T, five)**: **T1** GSM8K-style multi-step arithmetic (n=20) | **T2** StrategyQA-style implicit reasoning (n=20) | **T3** synthetic traps (n=20) | **T4** custom minimal game (n=10, with an explicit Nash equilibrium point) | **T5** low-resource game (n=20, only 3 steps of reasoning per decision, a minimal-information situation).
- **Scale**: total cells = 3 mechanisms × 5 task families × 33 decisions/task ≈ **500 calls**.

### §2.2 The distortion measure `D(M, T)` and the distortion multiplier (spec §3.4 / §4.1, verbatim)

```
D(M, T) = E_π[ Σ_t |u*(a_t) - u(a_t)| / max_u ]
```

- `u*(a_t)`: the payoff of the theoretically optimal decision　　- `u(a_t)`: the payoff of the actual player's decision　　- `max_u`: the payoff upper bound (task-family normalization constant)
- distortion multiplier = `D_LLM(M, T) / max(D_Bayesian(M, T), ε)`; `distortion_multiplier(M, T) = D_LLM(M, T) / max(D_Bayesian(M, T), ε)`; across (M, T): mean + 95% bootstrap CI (**10k resamples**).

> ⚠️ The numerator contains `u*(a_t)` (**the pointwise value of the theoretically optimal payoff**) ⇒ **without T-1 the numerator is not computable ⇒ structurally not computable**; the denominator contains `max_u` ⇒ **the T-4 caliber directly sets the order of magnitude**.

### §2.3 The kill-line (spec §1 / §4.3, verbatim · **preregistered, frozen**)

- **H0 (kill)**: distortion multiplier ≥ **2.0×** (the LLM player introduces 2× distortion, the mechanism is not viable)
- **H1 (closure)**: distortion multiplier ≤ **1.5×** (the LLM player introduces ≤ 50% distortion, the mechanism is commercially usable)

```python
def kill_decision(mean_mult, ci_lo, ci_hi, theory_U_hit_rate):
    if mean_mult >= 2.0 or theory_U_hit_rate >= 0.3:
        return "FAIL_H0"  # 机制不可行 或 30%+ cell 超理论界
    elif mean_mult <= 1.5 and ci_hi <= 1.8 and theory_U_hit_rate <= 0.1:
        return "PASS_H1"  # 机制可商用
    else:
        return "GRAY"  # 1.5 < mean < 2.0 或 CI 跨边界
```

> ⚠️ **`theory_U_hit_rate` depends directly on `U(M,T)`** ⇒ **without U, 0 adjudication lands**. The cut-points `2.0` / `0.3` / `1.5` / `1.8` / `0.1` are **carried at their existing wording**, ⛔ 0 suggested changes — **even if you think some cut-point is unreasonable: that is our PI's adjudication surface, not the object of this commission.**

### §2.4 Sub-metrics and anti-attack (spec §4.2 / §5, verbatim)

- **theory lower-bound hit rate**: the share of cells with D_LLM ≤ L(M, T)　　- **theory upper-bound violation rate**: the share of cells with D_LLM > U(M, T)　　- **task-family specific**: mean computed per T, to identify the easiest / hardest task　　- **mechanism specific**: mean computed per M, comparing three-channel scattering vs greedy vs random in relative distortion
- **A1: theory-bound adversarial test** —— re-run 10 cells with a **deliberately wrong theory-bound formula** and see whether the kill decision flips (**>30% flips ⇒ report "the theory bound is unstable"**)
- **A2**: re-run with the T1–T5 order permuted; a distortion-multiplier change **> 40%** ⇒ report "task-family order sensitive"　　**A3**: three seeds, seed=42, 123, 456; std/mean **> 0.2** ⇒ report "seed sensitive"

> 📌 **A1 presupposes "that a true theory bound exists"** ⇒ your `L` / `U` will be **used directly as an attack surface** (written deliberately wrong, to see whether the kill decision flips) ⇒ **the robustness of your derivation is directly relevant to our kill-line**.

### §2.5 Reproduction protocol (spec §6, verbatim · independent-copy audit)

1. copy the repository to `/tmp/deposon_pb_audit_<timestamp>/`
2. read `verifier/handoff/P_B_V0_anchors_sha256_12.json` and verify the 5 anchors
3. pick 1 cell (e.g. M1×T1) and re-run **100 decisions × 5 seeds = 500 calls**
4. verify the distortion multiplier is within **± 5%** of the original value
5. any exceedance ⇒ **withdraw the entire V0**

> 📌 **What this means for you**: `D(M,T)` will be **recomputed by a third party from the literal wording you deliver** (following the C4.8 recomputability clause) ⇒ ⛔ the deliverable **0 contains placeholders / TODO / undefined symbols**; **every symbol must be computable by a third party from the literal wording**.

### §2.6 Where it is stuck right now (blocker text · verbatim)

- spec verbatim: 「**D1 启动阻塞**：本 spec 的"理论最优响应"与"理论失真界"公式需…给 1-page theory 落地。spec 框架已就绪，**等理论输入即可激活 v0 全部 cell**。」 = "**D1 start-up blocker**: the 'theoretically optimal response' and 'theoretical distortion bound' formulas of this spec need a 1-page theory to land them. The spec framework is ready; **once the theory input arrives, all V0 cells can be activated**." (spec L3; the ellipsis marks the elided clause 「〔W老师〕 D1 〔IM〕」, the source wording retired by the caliber change of §3.1 — the retirement changed 0 the state this sentence reports)
- spec verbatim: 「**D1…未给理论公式 → 整 V0 阻塞**，v3x 子代理无法继续」 = "**D1 … theory formula not given → the entire V0 is blocked**, the v3x sub-agent cannot continue" (spec L138; same marked elision)
- upstream register (`results/_v3_recheck_21_rescript_2026_09_27.md` = `04f6ecd482b9` §14.2 Z-74 + Y-59, **transcribed via the acquisition request §2**): 「**deposon 侧 `D(M,T)` 结构性不可算**：核心理论输入 `u*(a_t)` 与**理论界 L/U 未交付**」 = "on the deposon side `D(M,T)` is **structurally not computable**: the core theory inputs `u*(a_t)` and the **theory bounds L/U have not been delivered**"

### §2.7 Current-state snapshot (honest · measured on our machine 2026-09-30, re-verified for this version)

| Item | Current state |
|---|---|
| `tools/distortion_calculator.py` | ❌ **0 hits on disk** (a recursive filename search over the repository returns nothing; **re-run for v0.2, still 0**) |
| `verifier/handoff/P_B_V0_anchors_sha256_12.json` | ❌ **0 hits on disk** (**re-run for v0.2, still 0**) |
| Adjudication-surface state | ⏳ **0 of nine items complete** ⇒ following C4.9, the state "**not computable + γ**" is **in the triggered state**. ⚠️ **The grading of the "not computable + γ" level belongs to our verdict-keeper**; this letter 0 adjudicates and 0 performs the γ registration |
| **Guard against mis-citation** | `verifier/handoff/KT_ABC1_anchors_sha256_12.json` (`03c6c01f3697`, 6,680 B, 188 lines, measured) **is not** the P-B 5-anchor document (it belongs to the KT-ABC1 family) |

> ⚠️ **How to read the two "0 hits" rows honestly**: they are the conclusion of a **filename search surface**, **not a universal negation of existence** —— no full content-hash scan of the repository was performed. If you have CLI access, you may re-run the check yourself; if you do not, take the two rows as quoted statements of ours, **not as a claim you have verified**.

### §2.8 ⚠️ Ledger fingerprint drift (honest register · if you verify against an older fingerprint it will not match)

| Document | Older registered values (still on file, historical) | **Current on-disk state (measured 2026-09-30, this drafting session)** | What moved it, and what did not |
|---|---|---|---|
| `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | `bb7ca9838150` / 7,126 B (registration moment) → `8aba2837bc6a` / 11,189 B (after the first caliber-annotation layer) | **`423c84de20d5` / 15,457 B / 177 lines** | Two **append-only** annotation layers were added on 2026-09-30: the caliber-change notes (7 points) and then the **source-name update notes (6 points, now at L6 / L73 / L81 / L141 / L160 / L177)**. **The original text is unaltered in both** ⇒ this is **"a registered value lagging behind the final on-disk state", not "the content was changed"**; the current state governs. ⚠️ **Line numbers move when lines are appended**: the §9 main-caliber block that v0.1 cited as L152–157 is now **L156–162** (the two decisive lines at **L158–159**, the name-update note at **L160**) — the wording is identical, the position is not. Every formula, cut-point and quoted line in §2.2 / §2.3 / §2.4 / §2.5 / §2.6 was **re-read line by line for v0.2 and is unchanged** |
| `results/_c4_theory_source_caliber_correction_2026_09_30.md` | `f5583ecfe436` / 17,026 B (v0.1's value) | **`246344c5f215` / 20,165 B / 189 lines** | The register itself received the **name-update layer as an append**: §1's layer at **L20–L27** and §2.3's layer at **L120–L126**. The pre-existing text (including the first canonical text at L117) is **0 rewritten**. ⭐ **§2.3's new canonical declaration text is what your delivery must carry** (§3.5) |
| `results/_v5_theory_input_acquisition_request_2026_09_29.md` | `56c52db3f22a` / 10,212 B / 114 lines | **`83afc4802fe7` / 10,691 B / 116 lines** | An **append-only** annotation at **L27** updates the spec anchor recorded in that document's table, on the PI's 择定卡 q3「追加入注更新」. ⛔ **That recorded value (`8aba2837bc6a` / 11,189 B) is itself now stale** relative to the spec's current state above —— **this letter 0 modifies that document** (H3), so we register the staleness here for the PI to rule on |
| `results/_theory_input_request_supplement_2026_09_29.md` | `d225c6086e57` / 47,731 B / 429 lines | **`c966e7b605af` / 48,190 B / 431 lines** | An **append-only** block was added on 2026-09-30 (the PI-adoption landing section §8 and its own append-only sign-off). **The clauses A / B / C that bind you are at L344 / L354 / L363 and were re-read for v0.2: unchanged** |

> ⚠️ **Two honest cautions on this table**: (i) **a parallel rod was still appending to these documents while this letter was being drafted** ⇒ the values above are true **as of the measurement**, and the PI should re-check them at the moment of release; (ii) the register's own §2.1 table still lists the **first** layer's post-change values (`8aba2837bc6a` / 11,189 B for the spec), which the second layer has moved again ⇒ **registered values inside our own documents can lag; the on-disk state governs, and 0 document was edited by this letter to hide that**.

---

## §3 Caliber and adoption path

### §3.1 The new caliber (PI 2026-09-30 · iron-rule level · **two layers, both landed**)

**Layer 1 — the source of the theory bound (PI 2026-09-30, merged questionnaire `ask_3b8a6489fb38917e42a69ecd` q1)**:

> **Source of the theory bound = derivation by the named outside party** (PI 2026-09-30 adoption, q1「改：以 GLM 推导为准充作理论界」 = "change: take the named party's derivation as the theory bound", the option's own wording including 「铁律级：连带改 spec §9、C4.7 来源标注与论文口径；**本选即视为明示**」 = "iron-rule level: concurrently amend spec §9, the C4.7 source attribution and the paper caliber; **this choice counts as an explicit statement**").

That ruling wording is **independently corroborated by the current state of the spec** (verbatim, spec **L156–L162**):

- **What is retired (defined verbatim)**: the **source attribution "given by 〔W老师〕"** ⇒ changed to a derivation by the named party. ⚠️ **The original spec lines still read 「GLM 推导」 on disk** —— that is deliberate: the living document was annotated, **0 rewritten**; the retirement and what remains in force are defined in the annotation block, not by editing the original line.
- **What remains in force (⛔ not lifted by the source change)**: the constraint **"not self-created within P-B" = 0 self-invented / 0 self-drafted formulas**, which **continues in force under the zeroing discipline**. ⛔ This source change **grants 0 additional authority and takes away 0 authority** (the register's name-update layer repeats this: ⛔ 0 扩权 / 0 收权, ⛔ 0 改 C4.9 字面).
- **The adjacent line "do not redo 〔W老师〕's existing work"**: **unaffected this time** (that line constrains the redoing of that person's existing work, **not the source attribution of the theory bound**).

**Layer 2 — the source name updated to the actual executor (PI 2026-09-30, 择定卡 `ask_da8ce88762c1f39cb62e95f4` q1 / q2; landing confirmed by `ask_ead0d2f7dc818155041ee0cb` q1「按此稿落」)**:

> **The source name is updated to the actual executor = derivation by codex.** The former literal wording 「GLM 推导」 is **retained as history, 0 rewritten**, and is **0 longer the name to be used in a delivery**; the new canonical text is **the only wording subsequent deliverables may carry** (§3.5). ⛔ **Only the name changed**: 0 threshold touched, 0 new cut-point, 0 change to the C4.9 zeroing discipline, 0 change to the open boundary item of §3.3.

Both layers are **verified on disk, not merely transcribed**: the name-update layer is present in the register (§1 L20–L27, §2.3 L120–L126) and in the spec at **6 points** (L6 / L73 / L81 / L141 / L160 / L177), each an appended note stating that the name is updated per the actual executor, with the executor choice and the landing confirmation cited by id.

> ⭐ **What this means for you directly**: **the source is your derivation, but the "0 self-drafting" constraint did not change** — a derivation delivered by you is a **commissioned theory-bound source**, not something we may take as an unsourced placeholder formula. Therefore **H4 (0 self-filling) and H5 (0 unsourced placeholders) apply to you unchanged**. The name question that v0.1 left open is now closed and works in your favour: the canonical declaration and the actual executor are **the same name** ⇒ **0 attribution mismatch** (this is exactly what H2 exists to prevent).

### §3.2 The connected update surface (already annotated by our parallel rods · **0 labour for you**)

| Surface | Current state |
|---|---|
| spec §0 header / §3.5 heading / §3.5 last line / §8 L138 / §9 main-caliber block / §10 D1 row | ✅ annotated "source retired ⇒ derivation by the named party", **the original text is unaltered, history preserved**; ✅ **and each of the 6 points carries the source-name update note** (L6 / L73 / L81 / L141 / L160 / L177) |
| spec §9 main-caliber line | ✅ annotated (defining verbatim what is retired and what remains in force, see above), plus the name-update note covering the 2 name mentions in that block (L160) |
| **Erratum document** | ✅ **landed and extended**: `results/_c4_theory_source_caliber_correction_2026_09_30.md` (**`246344c5f215` / 20,165 B / 189 lines**) —— the **sole correction layer**; **status: pending PI review**. ⭐ **Its §2.3 carries the new canonical C4.7 declaration text (for your deliverable to follow)** ⇒ see §3.3 Gate 1 |
| C4.7 source attribution | ✅ **the new canonical declaration text is fixed** (register §2.3, name-update layer, verbatim) ⇒ your deliverable **carries that declaration alongside it** |
| Acquisition request | ✅ **append-only annotation** (L27) updating the spec anchor recorded in its table; the recorded value is now one layer behind the spec's current state (registered in §2.8, ⛔ 0 modified by this letter) |
| Two further annotated living documents (**informational, not part of your task's ledger**) | ✅ the same source-name update landed in `docs/V3X/KT_B1_SPEC_V0.1.md` (measured `0397b757362f` / 39,206 B) and `README_V4_2026_09_29.md` (measured `a6f88fb6e325` / 58,635 B) —— cited here only so that the update surface is **complete rather than selective**; you need 0 open them |
| Paper caliber | ⏳ a connected surface, handled by us (**out of scope of this commission**; the landing point = cite the register §2.3 new canonical text when new material is drafted) |

### §3.3 The adoption path (the three gates your product must pass · **already in force, 0 dependence on your arrival**)

| Gate | Clause | What it means for you at delivery |
|---|---|---|
| **Gate 1** | **C4.7 compliance declaration** (a declaration line inside the deliverable) | Every deliverable **carries**, verbatim, the new canonical declaration text of §3.5 below (register §2.3) **plus a verifiable source attribution (who gave it / where it comes from)**. ⛔ 0 create a separate standalone declaration file (house convention: **a declaration line inside the deliverable**) |
| **Gate 2** | **C4.9 zeroing discipline** (the reading rule) | If any item is missing ⇒ we judge "**not computable + γ**"; ⛔ 0 fill it with an estimated value / a substitute value / a self-invented formula |
| **Gate 3** | **C4.8 recomputability** (at the acceptance moment) | A third party can recompute `D(M,T)` **from the literal wording of what you deliver**; ⛔ the deliverable 0 contains placeholders / TODO / undefined symbols |

> ⭐ **Three separations (please keep them distinct)**: **delivery ≠ effect ≠ reversal of an existing ruling** —— your reply is **not automatically adopted**, **does not automatically land anywhere**, and **0 retrospectively changes any existing ruling of ours** (H8). **Whether it is adopted is the PI's call; the grading belongs to our verdict-keeper.**

> ⚠️ **One boundary for which we have no explicit PI statement and which we therefore do not interpret on the PI's behalf (register §4-a, registered as-is; the name-update layer explicitly did 0 adjudicate it)**: **under what conditions a product of a "derivation by the named party" counts as a "derivation" and under what conditions it falls into "self-drafted / substitute"**, and **what the verifiability requirement on the derivation chain (basis · assumptions · steps) actually is** —— **both await the PI's explicit statement**. ⚠️ **Until that boundary is settled, the safest delivery posture is: write out the basis, the assumptions and the source of every step in full** (going beyond is fine; ⛔ leaving blanks is not), so that your product **stands under any of the possible readings**. This letter **0 interprets that boundary on the PI's behalf**. (Note: the register's §4-a text still carries the former source name in its own wording — that document is **0 rewritten**; the name-update layer updated the delivery name, not this open item.)

### §3.4 No-conflation declaration (three easily-confused things, separated one by one)

| Matter | State |
|---|---|
| **Source of the theory bound** | ✅ ruled by the PI, and the source name **updated to the actual executor**: **derivation by codex** (register §1 / §2.3, **effective 2026-09-30**). The former literal wording 「理论界来源 ＝ GLM 推导」 is **history, 0 rewritten**, and is **0 longer a delivery name** |
| **Whether the theory content has arrived** | ❌ **not arrived** —— arrival is **a different thing**, and is not automatically satisfied by a change of source or by naming an executor (the annotations in the spec retain the wording "theory not yet arrived ⇒ the entire V0 is blocked" unchanged, and the register states it explicitly: ⚠️「来源已改」⛔ 0 等于「理论已到位」) |
| **The state of the "〔W老师〕 line"** | ⏳ **left on paper, 0 new action** (register §4-b): the **supply** side of the theory bound is **de-linked** (it no longer points to that line), but **the state of that line itself is unchanged** ⇒ **this does not mean** that line has been closed, abandoned, or completed in any respect |

### §3.5 ⭐ The canonical declaration you must carry (Gate 1's text · **already ruled — the item v0.1 left open is closed**)

The canonical declaration text that Gate 1 requires your product to carry reads, **verbatim as it now stands on disk** (register §2.3, the 2026-09-30 name-update layer; the identical text also appears in the register's §1):

> 「**理论界来源 ＝ codex 推导（PI 2026-09-30 采认；来源名按实际执行方更新——执行方择定＝codex，`ask_da8ce88762c1f39cb62e95f4` q1／q2；原字面「GLM 推导」历史留痕、0 回改）；0 自创 / 0 自拟公式，沿 C4.9 归零纪律**」＋**可核来源标注（给出人 / 出处）**

Our English rendering (a translation; **the Chinese above governs**): "Source of the theory bound = derivation by codex (PI adoption 2026-09-30; the source name is updated to the actual executor —— executor chosen = codex, `ask_da8ce88762c1f39cb62e95f4` q1 / q2; the former literal wording 'derivation by GLM' is retained as history and is 0 rewritten); 0 self-invented / 0 self-drafted formulas, per the C4.9 zeroing discipline" + a verifiable source attribution (who gave it / where it comes from).

> 📌 **One line of history, for readers who meet the older wording**: v0.1 left open how the source name would land, given that the canonical text then named GLM. The PI ruled on 2026-09-30 to **update the name to the actual executor** (executor chosen = codex) and confirmed that landing. The former literal wording remains on disk as history, **0 rewritten**, and is **0 longer a delivery name**.

**What this means for your delivery, concretely**: carry the text above, and the verifiable source attribution is **you** (codex) —— **one name throughout**, no mismatch between the declaration and the actual deriving party, which is exactly what the honest-attribution clause (H2) requires.

---

## §4 Reply requirements

### §4.1 Item by item (**T-1 / T-2 / T-3 / T-4 + clauses A / B / C — six items, one answer each**)

1. **Answer item by item**: T-1, T-2, T-3 and T-4 are **each answered independently**; clauses A / B / C each attach to their corresponding T item. ⛔ 0 substituting a single summary for the item-by-item answers.
2. **Recomputability first**: give every symbol its definition and its dimension / range; a third party can compute it from the literal wording (§2.5's reproduction protocol will use your wording). Where a step is skipped, **write the skip down** (H7).
3. **⭐ The derivation chain must be checkable** (**for our adoption process to audit line by line**): please **list the key steps and their bases one by one** —— for each step, state **"which assumption / which basis / which source this step used"**. ⛔ **0 conclusion-only delivery**; ⛔ 0 passing over a step with "obviously / easily proved / similarly obtainable" and 0 expansion; ⛔ 0 compressing several steps into one sentence. **Where the basis is insufficient, write plainly: "here I used an additional assumption X (not given in the task statement)"** —— **declaring an assumption costs you nothing; a hidden assumption is the risk** (a hidden one may be judged "self-drafted" and thereby trigger the zeroing discipline). **The level of detail of your derivation chain is for you to decide; our only requirement is that it can be audited line by line.**
4. **Provenance discipline**: wherever you cite external theory / literature / a theorem ⇒ give a **verifiable source** (verbatim + locating information: equation number / page / section); **if it cannot be obtained, write `null`** and attach **the list of channels already searched**. ⛔ 0 fabricating literature numbers or theorem names; ⛔ 0 filling in from memory.
5. **If it is unobtainable, say so**: if an item is unobtainable under your conditions, plainly write "**unobtainable + the channels already searched + what is still missing**" —— **"I could not find it" is a qualified reply; "let me guess one" is not**, and **inventing one would directly trigger our zeroing discipline** (H4 / H7).
6. **Honest attribution · declare the model actually used (anti-downgrade clause, mandatory)**: the reply is issued **under your own name (codex)** and **must state the model / version actually used in producing it**. If your reply was produced through a **gateway, proxy, router or reseller**, or is **otherwise not traceable to a specific model build**, the reply **must state, in a clearly marked block, the model name and the full version identifier actually used** (the vendor prefix and the dated or numeric build string exactly as the serving endpoint reports it), together with the serving endpoint host, the model string requested at the endpoint, and the date of the call. If the reply is **not** model-produced, write that explicitly instead. A reply that omits this declaration, or that we find on reception to have been served by a model other than the one declared, **will be registered as an unverifiable reply and will not be entered into our evidence chain**; we compare the declaration against the model metadata recorded at forwarding time. This clause exists because a reply that silently downgrades to a weaker model would be misleading; declaring the model costs the addressee little, while an undeclared downgrade misleads.
   - Minimum acceptable declaration block (you may add anything further):

     ```text
     Model actually used:  <vendor/model-name + full version or build identifier>
     Serving endpoint:     <host[:port]>
     Model string requested at the endpoint: <exactly what was requested>
     Date of the call:     <YYYY-MM-DD HH:MM TZ>
     If not model-produced, write: "Not produced by a language model" + a one-line description of the method.
     ```

   - For reference, the codex reply to our 2026-09-28 external-derivation commission (`c706e69d00fc`, out-of-repository, re-measured 2026-09-30 and unchanged) declared as follows — including the rows it could **not** fill, which is the correct handling of a field the model genuinely cannot see: 「Session identity supplied to this assistant: Codex, based on GPT-6. / Exact model actually served, vendor-qualified build/version: unavailable to this assistant. / Serving endpoint host[:port]: unavailable to this assistant. / Exact request.model string: unavailable to this assistant. / Work date: 2026-09-29, Asia/Shanghai (UTC+08:00).」 Note: that declaration is **our reading of a file on disk, not a claim by you**; if you know the model actually serving this session, declare the real values.
   - ⛔ **The drafting side does not fill this in on your behalf either.** Where the PI's canonical source for any model/version wording is the PI's own github, a value you cannot verify is written as unverifiable, **not** as a plausible guess.
7. **Boundary declaration (please attach it)**: state plainly that your reply **0 represents any modification of our existing documents**, **0 represents an adjudication made on our behalf**, and **0 has already been adopted by us**.
8. **Fingerprint**: the reply **carries its own SHA-12** (`sha256(whole-file bytes)[:12]`, lowercase) + byte count + line count (following the established reply convention: structured + recomputable). **0 writing your own fingerprint into the file to create a self-reference.**
9. **0 outline**: ⛔ this commission **does not require particular sections and 0 prescribes a layout** —— structure and level of detail are for you to decide (PI ruling of 2026-09-24). Suggested name: `letters/_codex_theory_derivation_reply_<YYYY_MM_DD>.md` (to be fixed by the PI at forwarding time).

### §4.2 How to work from this letter (both execution forms are covered on purpose)

This letter is written to be **self-contained**: §1 (the task surface, including clauses A/B/C), §2 (the background and use) and §3 (the caliber and adoption path) carry **everything needed to execute the task**, so the two execution forms differ only in how you consume the evidence:

| Execution form | What you need | What this letter gives you |
|---|---|---|
| **codex CLI with access to the repository** | you can open the originals yourself | §6 cites every source document in **three forms — file name + SHA-12 + (path)** ⇒ you may read the originals directly, and the SHA-12 lets you prove you read the same bytes we did |
| **codex chat without repository access** | you have only what is in the letter | the inlined material of §1–§3 is enough to execute the task; §6's SHA-12 values let you **cross-check against documents the PI attaches**, and the Chinese original of the same task (`344f5b9e0b08`) is available if the PI attaches it |

⚠️ **Honest caveat about the two forms**: the upstream documents (spec / request / supplement / correction register) are **written in Chinese**; the English renderings in §1–§3 are **our translations**, produced so that a chat-side executor is not blocked by the language. **In any conflict between an English rendering here and the Chinese original on disk, the Chinese original governs** (H3 · the counterpart rule in the header). If you have repository access, **read the Chinese originals for anything that must be reproduced exactly** —— in particular the formal clause wording of §1.1 and the canonical declaration of §3.5, which are given in Chinese verbatim precisely so that they can be copied without translation drift.

---

## §5 The caliber of this commission's materials (**self-description · so that you can audit how we work**)

| Item | Our practice |
|---|---|
| **0 reply outline** | ✅ **no structural outline is attached**; structure / level of detail / writing style are left to you (PI ruling of 2026-09-24) |
| **The main line is stated** | ✅ §0.1 states in one paragraph "what is wanted and why it is stuck"; §0.2 lists the hard constraints one by one (**no outline ≠ not stating the main line**) |
| **Material given in full** | ✅ §2 gives the full background (D(M,T) / mechanisms and task families / kill-line / sub-metrics and anti-attack / reproduction protocol / blocker text / current-state snapshot), **all quoted at our on-disk wording**, so that you need not go looking |
| **0 buried mines** | ⚠️ the fingerprint drift of §2.8, the "0 hits on disk" of §2.7 and the three easily-confused matters of §3.4 are **all placed in front of you honestly**, nothing hidden |
| **0 drafting on your behalf** | ⛔ 0 drafting an expression for `u*(a_t)`, 0 drafting an L/U formula, 0 drafting a `max_u` value, 0 suggesting an approximate substitute, 0 pre-filling per-cell coverage values, 0 preset attribution / source |

---

## §6 Evidence-document index (three-form citation: file name + SHA-12 + path; the full text of each is inlined above where it is needed)

| # | Document | SHA-12 (measured on our machine, 2026-09-30, this session) | Bytes / lines | Path and how to open |
|---|---|---|---|---|
| 1 | `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | **`423c84de20d5`** (⚠️ the registered older values `bb7ca9838150` and `8aba2837bc6a` are stale — see §2.8) | 15,457 B / 177 lines | `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` —— **the spec proper**: §1 objective and kill-line / §2 anchors / §3.1–§3.3 players · mechanisms · task families / **§3.4 the distortion measure** / **§3.5 the theory bounds (with the C4 caliber annotations and the source-name update notes)** / §4 metrics and kill adjudication / §5 anti-attack / **§6 reproduction protocol** / §8 failure modes / §9 the iron rules (incl. the annotated §9 main-caliber block at L156–162) |
| 2 | `results/_v5_theory_input_acquisition_request_2026_09_29.md` | **`83afc4802fe7`** (⚠️ the registered older value `56c52db3f22a` is stale) | 10,691 B / 116 lines | `results/_v5_theory_input_acquisition_request_2026_09_29.md` —— **the acquisition request (the requesting standard)**: **§3 "what is wanted", T-1 ~ T-4, carried verbatim** / §3.1 delivery form / §4 the uses U-1 ~ U-5 / §5 the forwarding surface / §7 open items (+ the 2026-09-30 append-only anchor note at L27) |
| 3 | `results/_theory_input_request_supplement_2026_09_29.md` | **`c966e7b605af`** (⚠️ the registered older value `d225c6086e57` is stale) | 48,190 B / 431 lines | `results/_theory_input_request_supplement_2026_09_29.md` —— **the supplement (contains the PI's 2026-09-30 adoption register)**: §1.2 the five-item difference specification / **§8.4 the three acceptance-layer clauses (A/B/C) at L344 / L354 / L363** / §8.5 C4.7 · C4.9 already in force / §8.6 the three-state landing |
| 4 | `results/_c4_theory_source_caliber_correction_2026_09_30.md` | **`246344c5f215`** (⚠️ the registered older value `f5583ecfe436` is stale) | 20,165 B / 189 lines | `results/_c4_theory_source_caliber_correction_2026_09_30.md` —— **the C4 caliber-correction register (the sole correction layer · pending PI review)**: §1 the changed item (new caliber and effective date) + **the 2026-09-30 name-update layer at L20–L27** / §2.1 the annotated living documents / **§2.3 ⭐ the new canonical C4.7 declaration text (the one you must carry), name-update layer at L120–L126** / §4-a ~ §4-d the open items |
| 5 | `results/_v3_recheck_21_rescript_2026_09_27.md` | `04f6ecd482b9` (unchanged since v0.1) | 14,618 B / 167 lines | `results/_v3_recheck_21_rescript_2026_09_27.md` —— **the H2-32 upstream source** (§14.2 Z-74 + Y-59 = "D(M,T) structurally not computable"). ⚠️ **the drafting side of this letter did not open its body text**; that sentence is **transcribed via the acquisition request §2** (see §2.6) and is already inlined there for you |
| — | `letters/_commission_glm_theory_derivation_2026_09_30.md` | `344f5b9e0b08` (re-measured, unchanged) | 32,472 B / 285 lines | `letters/_commission_glm_theory_derivation_2026_09_30.md` —— **the Chinese version of this very commission, addressed to GLM**; same task, same material, 0-touched by this letter. **That executor route was not chosen** (see §11) |
| — | `letters/_commission_codex_theory_derivation_EN_2026_09_30.md` | `af50969bebe2` | 66,754 B / 401 lines | **v0.1 of this very letter —— superseded by v0.2, 0 bytes changed.** Listed so that the version chain is traceable; 0 action needed from you |
| — | `letters/_v5_rj5_external_rederive_request_EN_2026_09_28.md` | `498215a9ec7d` | 51,013 B / 415 lines | the English external-derivation precedent (style anchor, incl. the anti-downgrade clause) |
| — | `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | `03c6c01f3697` | 6,680 B / 188 lines | cited **only to prevent mis-citation**: this is **not** the P-B 5-anchor document |
| — | `〔本机用户目录〕\codex-workspace\rj5_reply_2026_09_29\_v5_rj5_external_rederive_reply_codex_2026_09_29.md` | `c706e69d00fc` | 27,835 B | ⚠️ **out-of-repository** (re-measured 2026-09-30, unchanged) —— the codex reply to the 2026-09-28 commission, quoted in §4.1 item 6; **you cannot verify it from this repository** |

> 📌 The index gives **fingerprints and paths in three forms**; where a document's full text is needed for the task, it is **already inlined above** (§1, §2, §3). **This commission does not require you to open the originals** —— §6 exists so that, if you *do* have access, you can read them and prove the bytes you read are the bytes we cite.
> 📌 **Measurement conventions (stated so that a mismatch is not misread as tampering)**: SHA-12 = `sha256(whole-file bytes).hexdigest()[:12]`, lowercase; bytes = whole-file size; **lines = LF count** (a trailing newline terminates the last line). ⚠️ `KT_ABC1_anchors_sha256_12.json` is **CRLF-formatted on disk** (188 CRLF pairs), which is a line-ending convention difference, not a content difference. The **older fingerprints in the second column's ⚠️ notes are historical registration values**, retained so you can tell "a registered value lags" from "the content changed" (see §2.8).

---

## §7 Deadline and status

- **Suggested reply deadline**: **7 working days** (relaxed relative to the external-derivation precedent, because this commission carries recomputability and per-cell annotation requirements). ⚠️ **This is a suggestion and carries no binding force**; if you need longer, **please say so in advance**; ⛔ 0 going silently overdue.
- **⛔ Prerequisite**: this document is **pending PI review and release**; **the commission takes effect only upon release**. Before release **you need take no action**.
- **Statement on absence of blockers**: if an item is blocked on our side for a channel / caliber reason that the PI has not yet opened, **report it honestly**; ⛔ 0 fabricating substitute documents, 0 setting a temporary caliber of your own.

---

## §8 Boundaries (strictly observed · kept on both sides, the drafting side and the addressee's)

- **0 touching existing documents**: all documents in §6 are **read-only**; ⛔ 0 modifying, 0 overwriting, 0 deleting any existing document (including the spec, the request, the supplement, the verdict chain, the anchor documents and the erratum chain).
- **0 unauthorized threshold changes**: every cut-point of §2.3 / §2.4 is **carried at its existing wording**; ⛔ 0 created, 0 adjusted.
- **0 new external identifiers**: this letter **adds 0** external proper nouns / literature numbers / theorem names that we have not measured; `u*` / `D(M,T)` / `max_u` / `L` / `U` / IC capacity and the like are **all quoted at the literal wording of the on-disk spec**.
- **0 merging of derived data**: ⛔ 0 adding / 0 merging / 0 rewriting any existing JSON.
- **Keys**: this commission is unrelated to any API key; ⛔ no reply shall contain a plaintext key (H1).
- **0 killing, 0 re-grading, 0 substitution of adjudication**: this letter **issues no verdict**; ⛔ 0 changing the spec's kill-line, 0 performing the γ registration, 0 choosing on the PI's behalf.
- **Attribution boundary**: the **drafter of this letter = the Mavis team doc-writer** (`agent-0032834a3e04`); the **commissioning party = the PI**; the **theory derivation party = the executor the PI chose ＝ codex** (this version is addressed to codex). The three **0 impersonate one another** (H2).
- **Registration method**: your conclusions will be registered into our evidence / erratum chain **in quoted form**, and **shall not be used to certify our pre-existing conclusions under your name**.

---

## §9 Honest declaration for this letter (failures & limitations · drafting side)

1. **The PI's questionnaire records are not on disk (honest, E-C)**: a filename scan for questionnaire record artifacts returns **0 files**, so no original record of the rulings behind §3.1 exists on disk; the three ids occur in this repository **only inside our own documents** as citations and transcriptions (23 / 15 / 12 occurrences, measured). ⇒ this letter **does not pose as the original questionnaire record**. **Mitigation**: both rulings are **independently corroborated by on-disk state** —— by the **register's name-update layer** (`246344c5f215` §1 L20–L27 and §2.3 L120–L126, re-read for v0.2) and by the **spec's 6 appended name-update notes** (L6 / L73 / L81 / L141 / L160 / L177) ⇒ the citation does not rest on the transcription alone. ⚠️ **v0.1 stated this more strongly than the measurement supports** (it wrote that a full-repository search for the id "returns 0", whereas the id does occur in 6 of our documents); **v0.2 states the measured fact** — see item 16
2. **⚠️ Ledger fingerprint drift (already happened, and it continued between v0.1 and v0.2 · to be reported to the PI / the evidence chain)**: the spec, the correction register, the acquisition request and the supplement were **all appended to again on 2026-09-30** after v0.1 was measured, moving four of the fingerprints this letter cites (the full old→new table is §2.8). A line-by-line re-check shows the spec's and the register's **original text is unaltered — pure appends** (the source-name update notes) ⇒ this is **"a registered value lagging behind the final on-disk state", not "the content was changed"**; this letter re-computed and cites the **final state** (§2.8 / §6). ⚠️ **Registered values inside our own documents now lag in the other direction too**: the request's appended note (L27) records the spec as `8aba2837bc6a` / 11,189 B, and the register's §2.1 table lists the same first-layer values —— both are one layer behind the spec's current state. ⛔ **This letter 0 modifies any document to fix that** (H3); we register it for the PI to rule on. ⚠️ **Parallel rods were still writing to disk during drafting** ⇒ **before release, the PI should re-check whether the values carried here are still the latest.** (v0.1's item 2 recorded the earlier generation of this drift: `bb7ca9838150` → `8aba2837bc6a` / `f5583ecfe436`; that history stands.)
3. **Documents not opened (honest)**: `04f6ecd482b9` (the H2-32 source document) was **not opened in the body** by this drafting session; its §14.2 sentence is **transcribed via the acquisition request §2**, and only its fingerprint / bytes / line count were measured. `4185bdad6df5` (the C-4 preregistration document) is cited **only through second-hand citation** by the supplement and the request and its **body was not opened** —— for v0.2 its fingerprint / bytes / lines **were measured and match the second-hand value** (`4185bdad6df5` / 31,429 B / 335 lines) ⇒ the **number is verified, the text is not read**, and 0 quotation from its body appears anywhere in this letter. The C4 register `246344c5f215` was **read in sections** (§1 / §2.1 / §2.2 / §2.3 / §4 / §5, in full for §1–§4) ⇒ ⛔ **0 claim of a line-by-line full read of the whole register**. The two informational living documents named in §3.2 were **measured, not read**.
4. **No experiment run / no network / no API**: this drafting session ⛔ 0 ran any experiment, ⛔ 0 accessed the network, ⛔ 0 called any LLM or API, ⛔ 0 read any key. Everything in this letter is **either a verbatim transcription of on-disk documents or a reading of source lines**.
5. **What was checked and what was not (for this version)**: this session **did re-measure** all SHA-12 values, byte counts and line counts in §6 (SHA-256, lowercase, first 12 hex characters; byte counts by whole-file size; line counts by LF) across **9 in-repository files, the 2 informational files of §3.2, and the second-hand-cited preregistration file of item 3**, and **did re-verify by direct line reading**: the spec sections actually quoted here (§1 / §3.4 / §3.5 / §4.1 / §4.2 / §4.3 / §5 / §6 / §8 / §9, including the new name-update notes at L6 / L73 / L81 / L141 / L160 / L177), the **register's §1 name-update layer and §2.3 new canonical text** (the text quoted in §3.5 was compared character by character against the on-disk line), the **supplement's clauses A / B / C at L344 / L354 / L363**, and the request's appended note at L27. This session **did not** check the full text of the spec line by line, and **did not** inspect the actual contents of the `tools/` and `verifier/` directories (the "0 hits" of §2.7 is a **filename-search conclusion**, **not a universal negation of existence** —— no full content SHA scan was performed; the `KT_ABC1` file's existence and fingerprint **were** measured). The out-of-repository file `c706e69d00fc` was **confirmed present and unchanged on our machine**; it is **outside this repository** and a recipient of this letter cannot verify it from here.
6. **Skill and fallback (honest)**: the work order **did not name** a skill ⇒ this session **0 loaded any skill**; the discipline anchor = the work order's wording + **v0.1 of this very letter** + the layout of the other letters on disk (the Chinese GLM version `344f5b9e0b08` + the English R-J5 precedent `498215a9ec7d` + the codex reply `c706e69d00fc`) + the FTFB core. **0 fabrication of skill instructions.**
7. **0 outline (the PI's explicit ruling of 2026-09-24)**: this commission **contains no reply outline** and prescribes no reply sections and no layout (§4.1 item 9); the material is given in full and the structure is for you to decide. ⚠️ **0 outline = structural freedom, ≠ not stating the main line** —— the main line (§0.1) and the hard constraints (§0.2) are stated.
8. **0 presupposition of the answer**: this letter ⛔ **hints at no concrete form** of `u*` / `L` / `U` / `max_u`, gives no candidate values, weights nothing, ranks nothing; the equation `D(M,T)` and the cut-points are **entirely quoted at the on-disk wording** and are not our assertions.
9. **Open items 0 adjudicated (left honestly blank)**: the matters the C4 register §4-a lists as **awaiting the PI's explicit statement** (under what conditions a product of the named party's derivation counts as a "derivation" and when it falls into "self-drafted / substitute"; what the verifiability requirement on the derivation chain is; whether the nine-item C4.2 ~ C4.5 "theory content not arrived" state still triggers C4.9 "not computable + γ") —— this letter **0 interprets, 0 adjudicates on the PI's behalf**; the name-update layer explicitly left §4-a unadjudicated. The only posture it recommends is the one that is safest for you under any reading: **write out the basis, the assumptions and the source of every step** (§4.1 item 3, §3.3's closing note). (v0.1's closing sentence of this item referred to the executor-naming question of its §3.5; **that question is now ruled** — see item 16.)
10. **Naming note**: this document **deliberately carries no phase-number prefix** (such as `_v5_`): the authority to enable / use a phase or version name (V3 / V4 / V5 …) belongs to the PI, and ⛔ the drafting side neither enables one nor carries forward an unauthorized phase name. The `v0.2` in this file's name is the **document version assigned by the work order** (v0.1 → v0.2), 0 a phase name. ⚠️ Note that the ledger document names quoted in this letter **do** carry such prefixes —— those are **existing on-disk names, quoted verbatim, 0 adopted by this letter**.
11. **The executor question is now decided (supersedes v0.1's item 11)**: the PI chose the executor on 2026-09-30 —— **codex** (择定卡 `ask_da8ce88762c1f39cb62e95f4` q1, landing confirmed by `ask_ead0d2f7dc818155041ee0cb` q1). ⛔ This letter still **0 decides** whether any cut-point is reasonable, 0 decides whether your product is adopted, and 0 interprets the PI's authorization boundary of §3.3 —— those remain PI adjudication surfaces. (v0.1 wrote that the executor question was 0 decided; **that state has ended**, and the change is registered in item 16 rather than left as a silent edit.)
12. **The deadline is a suggestion**: the "7 working days" of §7 is a **suggested value with no binding force** (⛔ 0 creating any threshold effect); the PI may set another deadline at release.
13. **Version (superseded by item 16)**: v0.1 (`af50969bebe2` / 66,754 B / 401 lines) was a new first version; **this v0.2 does not overwrite it** (0 bytes changed, verified after landing) and the Chinese original `344f5b9e0b08` is likewise **0-touched**.
14. **Rendering convention (so that the style is not misread)**: this letter keeps the house convention of writing **"0"** before a noun to mean **"not a single" / "none"** (e.g. 0 keys = no key at all; 0 fabrication = nothing fabricated). This is a literal carry-over from the Chinese original and is **not** the number zero in a mathematical expression. **All digits inside formulas, numerical tables, hashes and bibliographic entries are carried verbatim and never form part of this convention.** Chinese technical terms are given verbatim in Chinese **at their first substantial appearance**, with an English rendering attached, so that nothing is lost in translation and nothing is invented.
15. **This is a translation and re-cast, not a re-derivation**: no new theory was introduced; every formula, hash, numerical value, cut-point and verbatim quotation is carried at the on-disk wording of the upstream documents. Where the source is Chinese, the Chinese original is retained alongside the English. **No term was invented.** ⚠️ The English renderings of the Chinese upstream documents are **our translations**; the Chinese originals govern (§4.2, and the counterpart rule in the header).
16. **⭐ v0.1 → v0.2 change history (what changed, item by item · v0.1 is superseded by v0.2)**: (1) **the executor is ruled** ＝ codex, and the source name in the canonical declaration is **updated to the actual executor**; the canonical declaration you must carry is now the register's **new text** (§3.5), and the item v0.1 left open is **closed**; (2) **the canonical name update is landed on disk** and is cited from the register (§1 / §2.3) and the spec (6 appended notes), 0 transcribed-only; (3) **the anchor chain was re-measured** and all values in §2.8 / §6 updated, with the drift registered honestly; (4) **§3.5 was closed** (the three-way open addendum is replaced by the ruled state, with one line of history); (5) the header, §2.8, §3.1–§3.3, §6, §9 and §10 were updated accordingly, and §11 carries the status line on the unchosen route. **Two small corrections are also registered here, rather than made silently**: (a) **v0.1's evidence-level statement about the questionnaire id was too strong** — it said a full-repository search "returns 0", whereas the id in fact occurs in 6 of our documents; v0.2 states the measured fact (0 record artifacts on disk; the id appears only inside our own documents) — this is a **correction of an inaccurate statement, in the direction of more modesty, not less**; (b) **v0.1's clauses B and C in §1.1 were quoted with a half-width `+` where the on-disk wording uses the full-width `＋`** (v0.1's clause A was already correct) ⇒ **v0.2 restores the on-disk characters** so that the "verbatim" claim is literally true; **the clause content is unchanged**. ⛔ **No internal routing or attempt history is recorded in this letter** — that belongs to our internal channel, not to an external commission.
17. **The four main bodies are carried from v0.1 unchanged in content**: §0's hard constraints, §1's task surface, §2's material ledger, §4's reply requirements, §7's deadline and §8's boundaries are **not rewritten**; what changed in them is limited to **anchor fingerprints** (so that no stale value is cited), the **source-name ruling statement in §0.1**, the **fidelity restoration of §1.1's two clause quotes**, and the **re-measured "0 hits" rows of §2.7**.

---

## §10 Consistency statement, zero-product declaration and the version chain (closing section)

**Consistency statement.** This file `letters/_commission_codex_theory_derivation_EN_v0.2_2026_09_30.md` is **v0.2** of the English commission, for **the executor the PI chose (codex)**, of the same task as the Chinese commission `letters/_commission_glm_theory_derivation_2026_09_30.md` (`344f5b9e0b08`, 32,472 B, 285 lines, re-measured 2026-09-30; **0-touched by this letter**). The task surface (T-1 ~ T-4 and clauses A / B / C), the background ledger (§2), the hard constraints (H1 – H9), the three adoption gates and the cut-points are carried at the same content as the Chinese version. **The structural correspondence is 1:1, with the following differences, all registered here rather than reconciled silently:**

| # | Difference | Why | Direction of authority |
|---:|---|---|---|
| 1 | **Executor named in the address** and in H2 / §8 is **codex**, and **that is now the PI's ruling, not an open choice** (v0.1 left the choice open) | the PI chose the executor on 2026-09-30 and the source name was updated accordingly | the PI's ruling governs; see §3.5 |
| 2 | **The canonical declaration carried by Gate 1 names codex** (v0.1 carried the wording naming GLM and registered a three-way open item about it) | the PI ruled the source name to follow the actual executor, and the landing was confirmed | **PI-side caliber act**, already landed on disk; the drafting side 0 chose and still 0 chooses |
| 3 | **§4.1 item 6 carries the full anti-downgrade declaration block** (endpoint, requested model string, call date) | following the English R-J5 precedent §6 item 9, which the codex reply answered in practice; the Chinese GLM version requires the model to be declared but states no minimum block | the stricter clause governs; the Chinese version is **0-touched** |
| 4 | **§11 local-path dependency audit of the Chinese GLM version** (status line added for v0.2) | the PI's premise is that GLM cannot reach local paths; that route was **not chosen**, so the audit is retained as a file-based comparison record only | read-only audit; **the Chinese GLM version is 0 bytes changed** |
| 5 | **English renderings** of the Chinese upstream text, with the Chinese retained verbatim at every substantial technical passage | the letter must be executable in chat form without repository access | **the Chinese originals govern** in any conflict |
| 6 | **v0.1 of this same letter is cited in §6 as a superseded version** (`af50969bebe2`, 0 bytes changed) | the version chain must be traceable by fingerprint | the drafting side; ⛔ 0 overwrite |

**Zero-product declaration (drafting side).** This letter is a **re-cast into English of an existing Chinese commissioning document, plus the registered additions of §3.5 / §4.1 item 6 / §11, and — in v0.2 — the closure of the executor-naming item and the re-measured anchor chain**. It produced **0 new experiments**, **0 new numerical readings**, **0 new literature identifiers**, **0 new JSON or other derived data**, **0 modification of any existing document** (the Chinese GLM version, v0.1 and all ledger documents are **0 bytes changed**), **0 change to any threshold**, and **0 verdict**. Nothing in this letter was inferred, estimated, reconstructed or completed on the addressee's behalf; no theory content was drafted, no L/U/u\*(a_t) expression was proposed, and no `max_u` value was supplied. **No external call of any kind was made**: 0 LLM calls, 0 URLs fetched, 0 API keys read or written, 0 network access; the measurements are local `Get-FileHash` / line reads over files on disk.

**§10.1 SHA-12 of this file.** SHA-12 is defined as `hashlib.sha256(whole-file bytes).hexdigest()[:12]`, lowercase. A file cannot contain its own hash, so the measured SHA-12 of this file is reported **outside** the file, alongside its delivery. **Stated rather than claimed: this file contains no self-hash placeholder filled in after the fact, and no hash value in this letter was written without measurement.**

---

## §11 Appendix (read-only audit): the local-path dependency surface of the Chinese GLM version, and what would have needed adapting had GLM been chosen

> **Status of this appendix (updated for v0.2)**: a **read-only audit performed on `344f5b9e0b08` (32,472 B, 285 lines, measured 2026-09-30)**. ⛔ **That document is 0 bytes changed by this audit and by this letter.** The PI **chose the executor = codex** on 2026-09-30, so **the GLM route was not chosen**; this appendix is **retained on file as a comparison record only** (留档对照), and **nothing here was re-done, re-run or re-verified for the unchosen route**. The byte and line figures quoted inside §11.3 are **as measured at v0.1 time**; two of the documents they describe (the spec and the C4 register) have since been appended to (see §2.8) ⇒ those two rows' figures are **historical**, while the audit's conclusion is unaffected, because the Chinese version's inlining state is unchanged (0 bytes changed).
> **0 recommendation on which executor to choose** —— and none is needed now: the PI has ruled.

### §11.1 The premise, stated precisely

The PI's premise is "**GLM cannot reach our local paths**". Taking that premise as given, the surface to audit is: **every place where the Chinese GLM version requires, points at, or invites the reader to open a location that only exists on our machine.** The audit below distinguishes **hard dependencies** (the addressee is asked to open something) from **soft mentions** (a path is named descriptively, with no reading expected) and from **landing conventions** (where the reply is expected to be filed).

### §11.2 Per-location list

| # | Location in `344f5b9e0b08` | What it points at | Kind | What the addressee is actually asked to do |
|---:|---|---|---|---|
| 1 | header, 底账 line | 4 documents, named with repo-relative paths (`results/…`, `docs/V3X/…`) + SHA-12 | soft mention | nothing is required to be opened here; the four documents are the ledger whose substance is quoted in §1–§3 |
| 2 | header, 体例锚 line | 2 letters (`letters/…`) | soft mention | style anchors only; 0 reading required for the task |
| 3 | §1.2 "落位" row | `tools/distortion_calculator.py` | landing convention | ⛔ the addressee is explicitly told **0 create this file, 0 write code** ⇒ not a read dependency; but it presumes the reply is filed **inside our repository** |
| 4 | §2.5 reproduction protocol (5 steps) | `/tmp/deposon_pb_audit_<timestamp>/`, `verifier/handoff/P_B_V0_anchors_sha256_12.json` | soft mention | descriptive of what **our** third-party auditor will do, not what the addressee must run; the anchors JSON is in fact **0 hits on disk** today |
| 5 | §2.7 current-state snapshot (3 rows) | `tools/distortion_calculator.py`, `verifier/handoff/P_B_V0_anchors_sha256_12.json`, `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | soft mention | the two "0 hits" rows are **our** measured claims; a reader without repository access **cannot verify them** |
| 6 | §2.8 fingerprint drift table | the spec and the C4 register, by name | soft mention | states that verification against the old fingerprint will not match — but the reader **cannot perform the verification** without the files |
| 7 | §3.2 "勘误件" row + §3.3 Gate 1 | the C4 register, by name; its §2.3 canonical text is **quoted in-line** | mixed | the canonical text **is** in-lined (so the task can be done), but the **surrounding §1 / §2.1 / §4-a ~ §4-d is not** |
| 8 | §4.1 item 9 | `letters/_glm_theory_derivation_reply_<YYYY_MM_DD>.md` | landing convention | presumes the reply is **filed into our repository**; a chat-based executor returns text, not a filed document |
| 9 | **§6 evidence-document index — the central dependency** | 5 documents with SHA-12 / bytes / lines and a "how to open" column, closing with 「正文全文请按需调阅原件」 = "for the full text of each, please consult the originals as needed" | **hard dependency** | ⛔ **this is the line the premise bites on**: the Chinese version tells the addressee to go and read the originals for the full text, which an executor without repository access cannot do |

### §11.3 Per-document gap analysis (of the five ledger documents: what is in-lined, and what is not) · **figures as measured at v0.1 time; see the status note above**

| Ledger document | Size (as measured at v0.1) | In-lined in the Chinese version? | Gap that remains for a reader without repository access |
|---|---|---|---|
| spec `8aba2837bc6a` | 11,189 B / 171 lines *(now `423c84de20d5`, 15,457 B / 177 lines — appended to since; the inlining state below is unchanged)* | largely yes: §1 / §3.1–§3.3 / §3.4 / §3.5 / §4.1 / §4.2 / §4.3 / §5 / §6 are all quoted or rendered | **§2 the 5-anchor table**, **§8 failure modes**, and the **§9 iron-rule lines** (the key-safety line that H1 cites by name) are **pointed at but not in-lined** |
| request `56c52db3f22a` | 10,212 B / 114 lines *(now `83afc4802fe7`, 10,691 B / 116 lines — appended to since)* | yes for the task surface: §3 T-1 ~ T-4 verbatim, §3.1 delivery form; the uses U-1 ~ U-5 appear as consequences inside §2.2 / §2.3 | §5 forwarding surface and §7 open items are **0 in-lined**; these are administrative, not theory-bearing |
| supplement `d225c6086e57` | **47,731 B / 429 lines** *(now `c966e7b605af`, 48,190 B / 431 lines — appended to since)* | partly: **§8.4 clauses A / B / C are in-lined verbatim**; the consequences of C4.9 are summarized in H4 and Gate 2 | ⚠️ **the largest gap**: **§8.5 C4.7 · C4.9 "already in force"** is cited by H4 / H5 / Gate 2 by section number but its **literal wording is never quoted**, and **§8.6 the three-state landing** is not in-lined. A reader without repository access is pointed at a rule they are being bound by but cannot read |
| C4 register `f5583ecfe436` | 17,026 B / 172 lines *(now `246344c5f215`, 20,165 B / 189 lines — the name-update layer was appended; **§2.3's canonical text was replaced in effect by the new canonical text, which the Chinese version does not carry**)* | **§2.3 the canonical declaration is in-lined verbatim** (at v0.1 time it was the former wording; the **new** canonical text is carried by this English version's §3.5, ⛔ 0 written into the Chinese one) | §1 / §2.1 / §4-b ~ §4-d are **0 in-lined**; these are register/administrative, with §4-b bearing on the 〔W老师〕 line's state |
| H2-32 rescript `04f6ecd482b9` | 14,618 B / 167 lines (unchanged) | **yes** —— the drafter never opened it; its one sentence is transcribed second-hand and **in-lined verbatim** in §2.6 | **no gap**: it is not a dependency at all |

### §11.4 Adaptation checklist **had GLM been chosen** (suggestions only · ⛔ 0 applied to the Chinese version · **now historical, since that route was not chosen**)

Ordered by how much they would have blocked a GLM execution:

| Priority | Suggestion | Why |
|---:|---|---|
| **1** | **In-line or attach supplement §8.5** (the literal wording of C4.7 and C4.9) and **§8.6** | H4 / H5 / Gate 2 all bind the addressee by citing a section whose text is never quoted; this is the single largest content gap (48,190 B, 431 lines as of v0.2) |
| **2** | **Attach the four ledger documents as attachments to the letter** (or a condensed pack of the sections listed in §11.3) | this is what makes §6's "please consult the originals" fulfillable, and it also makes the SHA-12 values in §2.8 / §6 verifiable by hash |
| **3** | **Add the full anti-downgrade declaration block** (model / endpoint / requested model string / call date) as a minimum, as this English version does at §4.1 item 6 | the Chinese version requires the model to be declared but states no minimum block; if GLM is served through a gateway, the "model actually used" is exactly the field most likely to be filled in loosely |
| **4** | **In-line the spec §9 lines H1 cites** (the key-safety line) and **§2 the 5-anchor table** | H1 cites §9 by name; the 5-anchor table is the concrete object of the C4.6 anchor question |
| **5** | **Settle the reply-landing convention** | `letters/_glm_theory_derivation_reply_<YYYY_MM_DD>.md` presumes a filed document; a chat-based executor returns text, so the PI would need to state where the reply is filed and under what name |
| **6** | **State explicitly that the two "0 hits" rows need not be verified by the addressee** | a reader without repository access cannot check them; the rows are our measured claims, not their obligation |
| **7** | ~~Consider whether the §3.5 executor-naming addendum also applies~~ **closed by the PI's ruling** | the PI ruled the source name to follow the actual executor and chose codex ⇒ the item is settled on the register's side; this English version carries the ruled text |

**What would NOT have needed adapting** (stated so that the comparison is not one-sided): the task surface, the hard constraints, the kill-line, the cut-points, the three adoption gates and the boundary section are all **content-complete within the letter** already; a GLM executor could have performed the derivation task from the Chinese letter as it stood, **except** for the items ranked 1–4 above.

---

**Status**: 🚫 **draft · pending PI review and release**; takes effect and locks at that moment. All items that v0.1 left open are closed by the PI's 2026-09-30 rulings ⇒ **ready for review-and-release as written**.

**Issued by | the Mavis team doc-writer (`agent-0032834a3e04`) | 2026-09-30 · v0.2 (v0.1 `af50969bebe2` superseded, 0 bytes changed)** | 0 sent / 0 pushed / 0 forwarded / 0 modification of existing documents / 0 drafting of theory content / 0 keys / 0 network | the SHA-12 (+ bytes / lines) of this file are measured after landing and reported with the delivery receipt (**not written into this file**)
