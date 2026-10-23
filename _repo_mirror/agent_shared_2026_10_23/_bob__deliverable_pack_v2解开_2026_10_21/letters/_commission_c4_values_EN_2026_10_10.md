# Commission: The Four C4 Values — `u*(a_t)` / `L` / `U` / `max_u` — P-B Distortion Bound V0 · English version · **v0.1 (draft · pending PI review and release · addressee not yet ruled)**

> **To**: ⏳ **NOT YET RULED — the addressee is an open PI surface (see §7).** This letter is written to be **addressee-neutral**: it names no party as the recipient and assigns no party the task. ⛔ **The drafting side has not chosen, and does not choose, who receives it.** Options are listed at §7 **as exits for the PI to pick from**, with the state of each honestly noted; picking one is the PI's act alone. (For contrast: the 2026-09-30 predecessor commission `8b15f0957e0f` named its executor; **that was a PI ruling of that date and it is not carried forward as a default here**.)
> **From**: doc-writer (`agent-0032834a3e04`, deposon drafting lane) | **Commissioning party**: the deposon project PI
> **Date**: 2026-10-10
> **Version**: **v0.1** — first version; ⛔ **not** a successor to any prior C4 letter (it commissions a **different task surface** — see §3).
> **Status**: 🚫 **draft · pending PI review and release** (⛔ **0 sent / 0 pushed / 0 forwarded / 0 addressed**; the commission takes effect and locks at the moment of release). ⚠️ **Two PI surfaces are open on it** — who receives it (§7) and whether it goes out at all (§7 exit 0). Nothing in it waits on a further decision; what waits is the PI's own two calls.
> **Authority anchor**: PI 2026-10-10「轮41」card (`ask_38cfeded4238be5321e93cef`), EXP-05 E1 answer, verbatim: 「**外派英文委托稿**」 = "**dispatch an English commission draft**". ⚠️ **Evidence level, stated honestly (E-C transcription)**: as with the 2026-09-30 rulings this letter cites, **the questionnaire record itself is not on disk** — a filename scan for questionnaire record artifacts returns **0 files**, and the id above occurs in this repository only inside our own documents as citation/transcription ⇒ **this letter does not pose as the original record**. The anchor is therefore a **work-order transcription**, and the PI should confirm it at release.
> **What this letter exists for (honestly stated, one paragraph)**: a preregistered distortion measure `D(M, T)` and its theory bounds are **not computable**, because the **four values** they need — `u*(a_t)`, `L`, `U`, `max_u` — have never arrived. On 2026-09-30 the PI ruled that the theory bound's source is a derivation by a named outside party, and that party was commissioned in English. That commission came back on 2026-09-30 with a **substantial, honest, fully sourced answer — and its central finding was negative**: 「**构造规则可导 / 取值不可导**」 = "**the construction rule is derivable; the values are not derivable**". Since then the four values have **not** arrived, and on 2026-10-10 the PI was asked, at `EXP-05` exit E1, how to resolve it. The PI's answer was to **commission the values themselves, in English, from outside**. This letter is that commission. ⛔ **It decides nothing on our own authority**: it does not fill any value, does not judge whether the existing answer was good, does not decide who should answer it, and does not decide whether the answer will be adopted — adoption is the PI's call through our process.
> **The single most important sentence in this letter**: ⭐ **a reply that says "I cannot supply these values, and here is precisely why" is a complete, acceptable, expected answer** (§1.3). The previous commission produced one, and we are not asking anyone to pretend otherwise. **What we cannot accept is a guess wearing the clothes of a value** — the zeroing discipline (H4) forbids it, and a fabricated value would corrupt a frozen kill-line. ⛔ **This letter contains no reply outline** (PI ruling of 2026-09-24: commissioning materials contain no outline; the addressee is left free to develop the answer) — see H11.
> **Ledger (measured on this machine 2026-10-10, this drafting session · read-only)**: ① spec `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` (**`423c84de20d5`**, 15,457 B, 177 lines) ② the 2026-09-30 commission `letters/_commission_codex_theory_derivation_EN_v0.2_2026_09_30.md` (**`8b15f0957e0f`**, 82,016 B, 418 lines) ③ **the reply to it** `letters/_codex_theory_derivation_reply_2026_09_30.md` (**`7558eb1a5e34`**, 71,002 B, 981 lines) ④ C4 caliber-correction register `results/_c4_theory_source_caliber_correction_2026_09_30.md` (**`61b139efd0ef`**, 25,022 B, 238 lines) ⑤ preregistration `results/_v5_item21_rerun_conditions_prereg_2026_09_28.md` (**`4185bdad6df5`**, 31,429 B, 335 lines) ⑥ the EXP-05 judgment that raised this exit `results/_exp05_missing_true_disposition_judgment_2026_10_10.md` (**`e8e1e63a11db`**, 25,552 B, 192 lines). **Full three-form index at §6.**
> **⚠️ Ledger drift, registered up front (honest)**: v0.2 cited the C4 register as `246344c5f215` / 20,165 B / 189 lines; **the current on-disk state is `61b139efd0ef` / 25,022 B / 238 lines** — it has been appended to twice since. The canonical declaration text v0.2 quoted **was re-read at its current lines and is unchanged** (§5.2). ⛔ **This letter modifies nothing to hide the drift** (H3).
> **This letter does not write**: any GitHub URL, any model name/version, any key or credential, any value, any formula for `L`/`U`/`max_u`, any numerical fill of any cell. The source name 「codex 推导」 is **carried verbatim from the register's canonical text** (a PI-ruled wording we did not draft).
> **Encoding**: UTF-8 without BOM · LF. **The fingerprint is not written into this file** (measured after landing, reported with the receipt).

---

## §0 The main line and the hard constraints

### §0.1 The main line (one paragraph)

A preregistered distortion measure `D(M, T)` with theory bounds `L(M,T)` / `U(M,T)` is **frozen and not computable**: its numerator needs `u*(a_t)` (the payoff of the theoretically optimal decision) and its denominator needs `max_u` (a task-family normalization constant), and its adjudication needs `U(M,T)`. All four are **named on disk and defined nowhere**. On 2026-09-30 an outside derivation party was commissioned in English to supply them; it returned a **complete and honest answer whose result was that the construction rules are derivable from the existing literals but the values are not** — the payoff function `u` itself has no definition, scale, unit or range anywhere on disk, and three further quantities (`IC 容量`, `机制可辨识性`, `机制收敛性条件`) are named inside one parenthetical and never defined. That answer has stood for ten days and the four values have not arrived. **This letter commissions the four values themselves** — either as values with a verifiable per-value source and a per-cell applicability declaration, **or** as an explicit, reasoned statement that they cannot be supplied, and what would be required to make them obtainable. Both are complete answers. A guessed value is not an answer and is forbidden.

**No outline ≠ not stating the main line.** The main line (§0.1) and the hard constraints (§0.2) are stated; the shape is given (§1); the material is given in full (§2). The **structure, level of detail, derivation path and writing style of the answer are entirely yours to decide** (H11).

### §0.2 Hard constraints (non-negotiable; violation = stop work and report)

| # | Hard constraint |
|---|---|
| **H1** | **0 keys**: 0 into the prompt, 0 into JSON, 0 into logs, 0 into any deliverable, 0 restatement (alongside the spec §9 "key safety" line and the R4 rule) |
| **H2** | **Honest attribution · 0 impersonation**: the reply is issued **under your own name**; ⛔ 0 use of the name of worker / verdict-keeper / evidence-auditor / protocol-keeper / doc-writer / verifier / any commissioned party or outside party; ⛔ 0 certify any of our **pre-existing conclusions** under your own name |
| **H3** | **0 touching our existing documents**: all ledger documents of §6 are **read-only** — 0 modification, 0 overwrite, 0 deletion, 0 rename; this commission and the reply **0 modify** any existing spec, preregistration, register, verdict or erratum chain |
| **H4** | **0 self-filled gaps** (the zeroing discipline, in force and unchanged): if any item is missing ⇒ we judge "**not computable + γ**"; ⛔ **0 fill it with an estimated value / a substitute value / a self-invented formula** (prereg `4185bdad6df5` §2.4.2 C4.9, verbatim: 「任一项缺失 ⇒ deposon 侧判**「不可算 + γ」**；**0 以估计值 / 替代值 / 自拟公式填充**」). ⚠️ **This binds you exactly as it bound the previous party** — being an outside derivation party does not grant any exemption (register §1.2 item 1, unchanged) |
| **H5** | **0 unsourced placeholder**: every value you deliver **carries its own source attribution (who gave it / where it comes from)**; ⛔ 0 unsourced placeholder values, 0 values typed in "just to fill the cell" |
| **H6** | **0 unauthorized threshold changes**: every cut-point listed in this letter (`2.0` / `0.3` / `1.5` / `1.8` / `0.1` / `±5%` / `10k resamples` / `>30%` / `>40%` / `>0.2`) is **carried at our existing on-disk wording, not one character altered**; ⛔ 0 create, 0 adjust, 0 replace on grounds of "being more reasonable" |
| **H7** | **0 fabrication**: where a derivation or a source skips a step, **write the skip down explicitly**; where a source cannot be obtained, **write `null`** and attach the list of channels already searched — "I could not find it" is a qualified reply; "let me guess one" is not. ⛔ 0 fabricating literature numbers or theorem names; ⛔ 0 filling in from memory |
| **H8** | **0 automatic effect**: the reply is **not automatically adopted**, does not automatically land in any position, does not automatically amend the spec or any preregistration; whether it is adopted, and when, is decided by **the PI + our adoption process** |
| **H9** | **0 half-side conclusions**: ⛔ 0 report only the favourable half — e.g. 0 report that `max_u` cancels out (§2.7) **without** reporting that `U` does not, or report the tractable cells **without** the blocked ones |
| **H10** | ⭐ **0 re-request of what is already delivered**: §1.3 states, item by item, **what the 2026-09-30 reply already established**. ⛔ **Do not re-derive, re-litigate or re-request those parts** — they are in the public record and we do not want them re-argued. Your work is the **remainder**. (If you believe an already-delivered part is **wrong**, that is a legitimate reply — but it must be argued on its merits, with a source, and be visibly marked as a challenge rather than a restatement.) |
| **H11** | **0 outline**: ⛔ this commission **prescribes no reply sections and no layout** (PI ruling of 2026-09-24). §1 gives **what shape is wanted**, ⛔ **not what the content is**. We pre-fill no value, no formula, no per-cell answer and no attribution |

---

## §1 Task surface: what shape is wanted (four values · **0 content drafted on your behalf**)

> ⭐ **This section fills in 0 content**: it states only "what shape is wanted". ⛔ **It does not state "what the values are"** — we do not have them, which is the entire reason this letter exists. ⛔ It pre-fills no expression, no numerical value, no per-cell coverage value and no attribution. The four rows are **carried from** the existing preregistered task surface (spec §3.4 / §3.5) and from the acceptance clauses of the 2026-09-30 commission, **0 rewritten, 0 added, 0 deleted** — rendered into English here so that this letter is executable on its own.

### §1.1 The four values, item by item (**shape required per item**)

| # | Value requested | Our existing on-disk basis (verbatim) | **Shape required (what you are to give)** |
|---:|---|---|---|
| **T-1** | **The payoff `u*(a_t)` of the theoretically optimal decision** | spec §3.4: 「`u*(a_t)`: **理论最优决策的支付**」 = "the payoff of the theoretically optimal decision" | Required **per cell**: a value, or a per-cell explicit `null` + the reason that cell is null + the source of the value where one exists. ⚠️ **The grid is 5 task families × 3 mechanisms = 15 cells, annotated cell by cell — 0 substituting a whole-sentence generalization.** ⚠️ **If you supply any `u*` value, the payoff function `u` itself must be supplied with it** (§2.6 F-1): a value without a scale is not a value |
| **T-2** | **The lower bound `L(M, T)`** | spec §3.5: 「**下界 L(M, T)**：LLM 信息瓶颈下的**最低可能失真**（由 **IC 容量 + 机制可辨识性**推出）」 = "**lower bound L(M, T)**: the minimum possible distortion under the LLM information bottleneck (derived from **IC capacity + mechanism identifiability**)" | Required **per cell**: a value, or a per-cell explicit `null` + reason + source. If a value is given, **the definitions of `IC 容量` and `机制可辨识性` that it was computed under must be given with it** (§2.6 F-3) — a bound without its functional is not computable by a third party |
| **T-3** | **The upper bound `U(M, T)`** | spec §3.5: 「**上界 U(M, T)**：**机制可承受的最高失真**（**机制收敛性条件**推出）」 = "**upper bound U(M, T)**: the highest distortion the mechanism can withstand (derived from **the mechanism's convergence condition**)" | Required **per cell**: a value, or a per-cell explicit `null` + reason + source. If a value is given, **the convergence condition** must be given with it. ⚠️ **`U` is the direct input to the kill decision** (§2.5) ⇒ **its absence blocks the entire kill-line, and its presence would unblock it** — this is the highest-consequence item in this letter |
| **T-4** | **The normalization constant `max_u`** | spec §3.4: 「`max_u`: **支付上界（任务族归一化常数）**」 = "`max_u`: the payoff upper bound (the task-family normalization constant)" | Required: **five numbers, one per task family T1 – T5, plus a per-cell source** — the literal scopes the constant to the task family, so a single universal constant is **excluded by the spec itself**. ⛔ 0 giving only a rule with 0 values; ⛔ 0 giving only a single constant. ⚠️ **Note the measured finding that `max_u` cancels exactly out of the primary multiplier** (§2.7 result 2) — that does **not** make T-4 optional: it reaches the verdict through `U`'s scale |

### §1.2 Three acceptance-layer clauses (attached to the four items; conjunctive — if any is missing, **0 downgrade, 0 exemption**)

| Clause | Attached to | Requirement |
|---|---|---|
| **A** | T-1 | **Source attribution (who gave it / where it comes from) + a scope-of-applicability declaration**, the latter annotating **cell by cell** the coverage of the value/formula across **T1 – T5 × M1 – M3** (cell by cell; 0 substituting a whole-sentence generalization). Carried from the supplement's clause A, 0 reworded |
| **B** | T-2 / T-3 | **Item-by-item source attribution** for `L` and `U`; the bases of derivation are respectively `IC 容量 + 机制可辨识性` (T-2) and `机制收敛性条件` (T-3). ⚠️ **Where a basis is named but undefined on disk, saying so plainly is the required behaviour** (§2.6 F-3) — ⛔ 0 supplying a definition of `IC 容量` and presenting it as ours |
| **C** | T-4 | **Per-task-family values + per-cell sources** for T1 – T5: ⛔ 0 only a uniform constant with 0 per-family values, 0 only a rule with 0 values |

> 📌 **The cell-count convention**: the number "15" is the arithmetic expansion of **5 × 3** — **0 new tiering, 0 new cut-point**.

### §1.3 ⭐ What the previous answer already established (**do not re-derive this** · H10)

The 2026-09-30 commission produced a complete reply. Its own summary table, transcribed, is the honest baseline for what remains:

| Input | Source attribution | Applicability scope | Expression / caliber | **Values** | Blocking gap (its words) |
|---|---|---|---|---|---|
| **T-1** `u*(a_t)` | ✓ 3 literals | ✓ 15/15 cells | ✓ construction rule | **✗** | `u` undefined |
| **T-2** `L(M,T)` | ✓ per item | ✓ | ✗ | **✗** | `IC 容量` / identifiability undefined |
| **T-3** `U(M,T)` | ✓ per item | ✓ | ✗ | **✗** | convergence condition undefined — **and this blocks the verdict** |
| **T-4** `max_u` | ✓ per family | ✓ 5/5 families | ✓ caliber + 5 constraints | **✗** | upstream `u` — but **cancels out of the multiplier** |

**Already delivered, and therefore out of scope for you**: T-1's construction rule and its 15/15 per-cell coverage grid; T-4's caliber plus the five constraints any candidate value must satisfy (the **shape** of an admissible answer — five numbers, one per family); the source attributions for all four. ⭐ **The remainder — the entire content of this commission — is the `取值` column: four ✗.**

**The prior party's own summary of its result, verbatim**: 「**构造规则可导 / 取值不可导**」 = "**the construction rule is derivable; the values are not derivable**"; and, on the comparability precondition, 「**不可满足 in values**」 = "**not satisfiable in values**".

### §1.4 ⭐ The two acceptable answers (both complete; neither is a dodge)

> ⚠️ **We state this explicitly because the honest answer is likely to be the second one, and we do not want a qualified negative result mistaken for a failed commission.**

| Answer | What it consists of | How we treat it |
|---|---|---|
| **① Values** | The four values, per-cell as §1.1 requires, each with a **verifiable source attribution** and each carrying whatever definition it depends on (`u`, `IC 容量`, `机制可辨识性`, `机制收敛性条件`) | Registered for PI adjudication through our adoption process (§5). ⛔ Not automatically adopted (H8) |
| **② Explicit non-availability** | A plain statement that the values **cannot be supplied**, **the reason why**, **the basis for that reason**, and **what would have to change for them to become obtainable** (e.g. which upstream definition is missing, who could supply it) | **A complete answer.** It converts an open-ended non-arrival into a **bounded, actionable, closable** statement — which is precisely what an unclosed external line has been unable to produce for ten days |

⛔ **What is not an acceptable answer**: a value with no source; a value "estimated" or "reasonable"; a value carried over from an adjacent quantity; a formula that fills the gap without naming what it assumes; a partial answer presented as complete; a half-side answer (H9).

---

## §2 Background and use (**the full material ledger · everything quoted from our on-disk wording**)

> This section is for you to judge what properties these four values must satisfy and what they will be used for. **It is all quotation**; we **endorse the correctness of none of it**, and **hint at no particular form or value**.

### §2.1 What this measure is doing (spec §1 / §3.1 – §3.3, literal points, rendered into English)

- **Objective**: V0 answers "when an LLM player replaces a Bayesian player, does the total distortion `D(M, T)` of the deposon three-channel scattering mechanism fall within the [theoretical lower bound, theoretical upper bound] interval".
- **Core question**: how much extra distortion does the LLM player's bounded rationality cause? The baseline is the Bayesian player (knows the mechanism + the payoffs ⇒ **distortion = 0**); V0 measures the LLM player's **distortion multiplier** relative to that baseline: D multiplier = `D_LLM / D_Bayesian` (value **≥ 1**).
- **Players**: the LLM player = **Doubao + DeepSeek**; the Bayesian baseline player = the theoretically optimal response calculator (knows the mechanism + the payoffs ⇒ distortion = 0); **unified decision space: choose 1 of 4**.
- **Mechanisms (M, three)**: **M1** Deposon T+R+A three-channel (ported from the deposon scattering layer) | **M2** pure Greedy (no field, no conservation constraint) | **M3** Random baseline (uniform sampling of the decision).
- **Task families (T, five)**: **T1** GSM8K-style multi-step arithmetic (n=20) | **T2** StrategyQA-style implicit reasoning (n=20) | **T3** synthetic traps (n=20) | **T4** custom minimal game (n=10, with an explicit Nash equilibrium point) | **T5** low-resource game (n=20, only 3 steps of reasoning per decision, a minimal-information situation).
- **Scale**: total cells = 3 mechanisms × 5 task families × 33 decisions/task ≈ **500 calls**.

### §2.2 The measure and the multiplier (spec §3.4 / §4.1, verbatim)

```
D(M, T) = E_π[ Σ_t |u*(a_t) - u(a_t)| / max_u ]
```

- `u*(a_t)`: the payoff of the theoretically optimal decision　　- `u(a_t)`: the payoff of the actual player's decision　　- `max_u`: the payoff upper bound (task-family normalization constant)
- distortion multiplier = `D_LLM(M, T) / max(D_Bayesian(M, T), ε)`; across (M, T): mean + 95% bootstrap CI (**10k resamples**).

> ⚠️ The numerator contains `u*(a_t)` ⇒ **without T-1 the numerator is not computable ⇒ structurally not computable**; the denominator contains `max_u` ⇒ its caliber sets the order of magnitude.

### §2.3 The kill-line (spec §1 / §4.3, verbatim · **preregistered, frozen**)

- **H0 (kill)**: distortion multiplier ≥ **2.0×** (the mechanism is not viable)
- **H1 (closure)**: distortion multiplier ≤ **1.5×** (the mechanism is commercially usable)

```python
def kill_decision(mean_mult, ci_lo, ci_hi, theory_U_hit_rate):
    if mean_mult >= 2.0 or theory_U_hit_rate >= 0.3:
        return "FAIL_H0"
    elif mean_mult <= 1.5 and ci_hi <= 1.8 and theory_U_hit_rate <= 0.1:
        return "PASS_H1"
    else:
        return "GRAY"
```

> ⚠️ **`theory_U_hit_rate` depends directly on `U(M,T)`** ⇒ **without U, 0 adjudication lands**. The cut-points `2.0` / `0.3` / `1.5` / `1.8` / `0.1` are **carried at their existing wording**, ⛔ 0 suggested changes — **even if you think a cut-point is unreasonable: that is our PI's adjudication surface, not the object of this commission.**

### §2.4 Sub-metrics and anti-attack (spec §4.2 / §5, verbatim)

- **theory lower-bound hit rate**: share of cells with `D_LLM ≤ L(M, T)`　　- **theory upper-bound violation rate**: share of cells with `D_LLM > U(M, T)`　　- **task-family specific**: mean per T　　- **mechanism specific**: mean per M
- **A1: theory-bound adversarial test** —— re-run 10 cells with a **deliberately wrong theory-bound formula** and see whether the kill decision flips (**>30% flips ⇒ report "the theory bound is unstable"**)
- **A2**: re-run with the T1–T5 order permuted; a multiplier change **> 40%** ⇒ report "task-family order sensitive"　　**A3**: three seeds (42, 123, 456); std/mean **> 0.2** ⇒ report "seed sensitive"

> 📌 **A1 presupposes "that a true theory bound exists"** ⇒ any `L`/`U` delivered **will be used directly as an attack surface** (written deliberately wrong, to see whether the kill decision flips) ⇒ the robustness of what you deliver is directly relevant to our kill-line.

### §2.5 Reproduction protocol (spec §6, verbatim · independent-copy audit)

1. copy the repository to `/tmp/deposon_pb_audit_<timestamp>/`
2. read the P-B V0 anchors file and verify the 5 anchors
3. pick 1 cell (e.g. M1×T1) and re-run **100 decisions × 5 seeds = 500 calls**
4. verify the distortion multiplier is within **± 5%** of the original value
5. any exceedance ⇒ **withdraw the entire V0**

> 📌 **What this means for you**: `D(M,T)` will be **recomputed by a third party from the literal wording you deliver** ⇒ ⛔ the deliverable **0 contains placeholders / TODO / undefined symbols**; **every symbol must be computable by a third party from the literal wording**.

### §2.6 ⚠️ Where it is stuck right now — the four blocking defects (this is the honest current state)

These are the **measured** findings of the 2026-09-30 reply. They are reproduced here because **they are the reason the values cannot simply be computed by us**, and because a correct answer to this commission must engage with them.

| # | Defect (the reply's own words) | Why it blocks |
|---|---|---|
| **F-1** | **`u`, the payoff function, is never defined anywhere on disk** — **「最上游缺陷」** = the most upstream defect | Used at spec L61/L64/L65/L66; **0 scale, 0 unit, 0 range, 0 per-family value** found by a repo-wide sweep. **Every one of the four inputs is a functional of `u`** ⇒ T-1's values, T-4's values and both bounds' scales are all undefined because `u` is |
| **F-2** | **`ε` is never defined, and the kill line is a function of it** — **「判死线级」** | On the spec's own baseline definition, `D_Bayesian = 0` identically ⇒ `max(0, ε) = ε` in **all 15 cells** ⇒ the multiplier is `D_LLM / ε` with `ε` free ⇒ **both terminal branches of `kill_decision` are reachable by choice of an undefined constant, with the experiment held fixed** |
| **F-3** | **`IC 容量`, `机制可辨识性`, `机制收敛性条件`: named, never defined** | Every occurrence on disk is a quotation of the spec's own L75/L76 sentence ⇒ **0 definitions, 0 expressions, 0 values, 0 criteria** ⇒ the bounds cannot be evaluated even in principle |
| **F-4** | **The `max_u` value slot**, plus the cancellation that limits its consequence | The shape is determined (five numbers); the values are absent because `u` is |

> ⚠️ **F-1 and F-2 are the load-bearing ones.** F-1 blocks the values this commission asks for; **F-2 is not in this commission's scope but we register it because it affects how any delivered value would be used** — a fully correct set of four values would still not, by itself, make the kill-line decidable. ⛔ **This letter does not ask you to fix `ε`**; it mentions it only so that your answer is not read as a promise that the kill-line becomes landable.

### §2.7 The three results the previous reply actually derived (so that you build on them, not around them)

1. **`D_Bayesian = 0` forces `max(D_Bayesian, ε) = ε` in all 15 cells** ⇒ the multiplier is `D_LLM / ε` ⇒ the kill line is a function of an undefined constant before it is a function of the LLM.
2. **`max_u` cancels exactly out of the primary multiplier** ⇒ T-4's absence blocks no part of the multiplier; it reaches the verdict only through `U`'s scale.
3. **`L` is inert on the verdict; `U` is its sole theoretical argument** ⇒ **T-3 blocks the kill decision, T-2 does not**, and `L(M,T) = 0` exactly where the mechanism is identifiable is the one cell-level acceptance test an eventual `L` formula must pass.

> ⭐ **Why §2.7 is here**: result 2 is the kind of finding that could be misread as "T-4 is optional" and result 3 as "T-2 is optional". **Neither is a licence to skip an item** — §1.1 asks for all four. We cite them so your answer is built on the existing record rather than re-deriving it (H10).

### §2.8 Where this sits in our process (context, so the answer is proportionate)

The EXP-05 judgment that raised this exit classified the two missing P-B artifacts as **"execution state not reached"** rather than "asset damage", found **0 live reading depends on them**, and registered the blocking single point as **the four C4 values**, whose supply is **not on the deposon side**. Its exit E1 asks, in terms: **"are the four values supplied by the PI, or is that external line explicitly closed?"** — and records that the derivation line is **exhausted** (the reply's own 「取值不可导」). ⛔ **This letter does not answer that question and does not prejudge it**; it is the instrument the PI's answer created, and the answer to it remains the PI's.

---

## §3 ⭐ Differences from the 2026-09-30 commission (`8b15f0957e0f`) — **item by item, honestly**

> Registered here rather than left as a silent rewrite. Every difference below is a **task-surface** difference, not a re-writing of the same commission.

| # | In the 2026-09-30 commission (`8b15f0957e0f`) | **In this letter** | Why |
|---:|---|---|---|
| 1 | Task = **derive** the four inputs (expressions, construction rules, definitions) | Task = **supply the four values** | the derivation line returned and self-reported the values as not derivable; the PI's 2026-10-10 answer is to commission the values themselves |
| 2 | Addressed to a **named executor** (ruled 2026-09-30) | ⏳ **addressee not ruled** — §7 lists exits, the drafting side chooses none (§7) | the PI's E1 answer authorizes an English commission; **it does not name a recipient**, and naming one is a PI act |
| 3 | T-1 ~ T-4 asked as "definition / expression / rule" | T-1 ~ T-4 asked as "**value, per cell, or per-cell explicit null + reason + source**" | same four items, different face of the same item |
| 4 | Three clauses A/B/C requiring **coverage + source annotation** | Same clauses, **carried unchanged**, applied to **values** rather than to coverage | the acceptance layer is not re-invented for the new face |
| 5 | Acceptance-layer premise: a complete reply would carry all four items | **Two acceptable answers, named up front**: values **or** an explicit reasoned non-availability with what would unblock it (§1.4) | the honest outcome is likely the second; an unstated alternative reads as an unmet commission |
| 6 | H1 – H9 | **H1 – H11** — H1–H9 **carried unchanged**; **H10** (0 re-request of what is delivered) and **H11** (0 outline) **added**, because the new task makes both salient | see §0.2 |
| 7 | Carried the 2026-09-30 canonical declaration naming the then-ruled executor | **Carries the current canonical declaration as it stands on disk** (§5.2) and **0 asserts that any recipient is that named party** — §7 is open | the declaration names a source for the theory bound; **this letter does not presume the addressee is that source**, and says so rather than implying it |
| 8 | Ledger = spec / request / supplement / register | Ledger = spec / prior commission / **prior reply** / register / prereg / **EXP-05 judgment** (§6) | the prior reply and the judgment are the two documents that define what is left |
| 9 | Reply deadline **7 working days** (a suggestion) | ⏳ **0 proposed deadline** — the deadline is a PI call at release | the drafting side 0 creates a schedule commitment for an unreleased, unrecipiented letter |
| 10 | (n/a) | **§1.3 "already delivered, do not re-derive" table** (H10) | prevents the wasted re-litigation that a fresh commissioning of a partly-answered task invites |

> 📌 **What is unchanged**: the four items, the three clauses, the hard constraints H1–H9, the kill-line, the cut-points, the three adoption gates, the boundaries, and the rule that this letter decides nothing on our own authority.

---

## §4 Reply requirements

### §4.1 Item by item (**T-1 / T-2 / T-3 / T-4 + clauses A / B / C — one answer each**)

1. **Answer item by item**: each T item is **answered independently**; clauses A / B / C each attach to their item. ⛔ 0 substituting a single summary for the item-by-item answers.
2. **Per cell, not per document**: where §1.1 asks for per-cell values, the answer is **per cell** — including the cells you cannot fill, which are answered with `null` + reason. ⛔ 0 dropping the unfillable cells silently.
3. **Recomputability first**: give every symbol its definition and its dimension / range; a third party must be able to compute from the literal wording (§2.5). Where a step is skipped, **write the skip down** (H7).
4. ⭐ **The derivation chain must be checkable**: **list the key steps and their bases one by one** —— for each step, state **"which assumption / which basis / which source this step used"**. ⛔ **0 conclusion-only delivery**; ⛔ 0 passing over a step with "obviously / similarly obtainable"; ⛔ 0 compressing several steps into one sentence. **Where the basis is insufficient, write plainly: "here I used an additional assumption X (not given in the task statement)"** —— **declaring an assumption costs you nothing; a hidden assumption is the risk** (a hidden one may be judged "self-drafted" and thereby trigger the zeroing discipline).
5. **Provenance discipline**: wherever you cite external theory / literature / a theorem ⇒ give a **verifiable source** (verbatim + locating information: equation number / page / section); **if it cannot be obtained, write `null`** and attach **the list of channels already searched**. ⛔ 0 fabricating literature numbers or theorem names; ⛔ 0 filling in from memory.
6. **If unobtainable, say so, completely**: 「**unobtainable + the channels already searched + what is still missing + what would unblock it**」 (§1.4 answer ②). **"I could not find it" is a qualified reply; "let me guess one" is not**, and inventing one would directly trigger our zeroing discipline (H4/H7).
7. **Honest attribution · declare the model actually used (anti-downgrade clause, mandatory)**: the reply is issued **under your own name** and **must state the model / version actually used in producing it**. If your reply was produced through a **gateway, proxy, router or reseller**, or is **otherwise not traceable to a specific model build**, the reply **must state, in a clearly marked block, the model name and the full version identifier actually used** (the vendor prefix and the dated or numeric build string exactly as the serving endpoint reports it), together with the serving endpoint host, the model string requested at the endpoint, and the date of the call. If the reply is **not** model-produced, write that explicitly instead. A reply that omits this declaration, or that we find on reception to have been served by a model other than the one declared, **will be registered as an unverifiable reply and will not be entered into our evidence chain**; we compare the declaration against the model metadata recorded at forwarding time. This clause exists because a reply that silently downgrades to a weaker model would be misleading.
   - Minimum acceptable declaration block (you may add anything further):

     ```text
     Model actually used:  <vendor/model-name + full version or build identifier>
     Serving endpoint:     <host[:port]>
     Model string requested at the endpoint: <exactly what was requested>
     Date of the call:     <YYYY-MM-DD HH:MM TZ>
     If not model-produced, write: "Not produced by a language model" + a one-line description of the method.
     ```

   - ⛔ **The drafting side does not fill this in on your behalf either.** A value you cannot verify is written as unverifiable, **not** as a plausible guess.
8. **Boundary declaration (please attach it)**: state plainly that your reply **0 represents any modification of our existing documents**, **0 represents an adjudication made on our behalf**, and **0 has already been adopted by us**.
9. **Fingerprint**: the reply **carries its own SHA-12** (`sha256(whole-file bytes)[:12]`, lowercase) + byte count + line count (structured + recomputable). **0 writing your own fingerprint into the file to create a self-reference.**
10. **0 outline**: ⛔ this commission **does not require particular sections and 0 prescribes a layout** (PI ruling of 2026-09-24) — structure and level of detail are for you to decide. Suggested name: `letters/_<your_party>_c4_values_reply_<YYYY_MM_DD>.md` (to be fixed by the PI at forwarding time).

### §4.2 How to work from this letter (both execution forms are covered on purpose)

This letter is written to be **self-contained**: §1 (the task surface), §2 (the background, the blocking defects and what the prior reply already established) and §5 (the caliber and adoption path) carry **everything needed to execute the task**.

| Execution form | What you need | What this letter gives you |
|---|---|---|
| **A party with access to the repository** | you can open the originals yourself | §6 cites every source document in **three forms — file name + SHA-12 + path** ⇒ you may read the originals and prove you read the same bytes we did |
| **A party without repository access** | you have only what is in the letter | the inlined material of §1–§2 is enough; §6's SHA-12 values let you **cross-check against documents the PI attaches**; **the prior reply is available for attachment** if the PI chooses to send it |

⚠️ **Honest caveat**: the upstream documents (spec / prereg / register / prior reply) are **partly written in Chinese**; the English renderings in §1–§2 are **our translations**. **In any conflict between an English rendering here and the Chinese original on disk, the Chinese original governs** (H3). If you have repository access, **read the Chinese originals for anything that must be reproduced exactly**.

---

## §5 Caliber and adoption path

### §5.1 The three gates any delivered value must pass (**already in force, 0 dependence on your arrival**)

| Gate | Clause | What it means at delivery |
|---|---|---|
| **Gate 1** | **C4.7 compliance declaration** (a declaration line inside the deliverable) | Every deliverable **carries**, verbatim, the canonical declaration text of §5.2 **plus a verifiable source attribution (who gave it / where it comes from)**. ⛔ 0 create a separate standalone declaration file |
| **Gate 2** | **C4.9 zeroing discipline** (the reading rule) | If any item is missing ⇒ we judge "**not computable + γ**"; ⛔ 0 fill it with an estimated value / a substitute value / a self-invented formula (H4) |
| **Gate 3** | **C4.8 recomputability** (at the acceptance moment) | A third party can recompute `D(M,T)` **from the literal wording of what you deliver**; ⛔ 0 placeholders / TODO / undefined symbols |

> ⭐ **Three separations**: **delivery ≠ effect ≠ reversal of an existing ruling** —— your reply is **not automatically adopted**, **does not automatically land anywhere**, and **0 retrospectively changes any existing ruling of ours** (H8).

### §5.2 The canonical declaration text as it stands on disk today

Carried **verbatim** from the C4 register §2.3 name-update layer (current state `61b139efd0ef`, re-read at its current line for this letter; **the original GLM wording remains on disk as history, 0 rewritten**):

> 「**理论界来源 ＝ codex 推导（PI 2026-09-30 采认；来源名按实际执行方更新——执行方择定＝codex，`ask_da8ce88762c1f39cb62e95f4` q1／q2；原字面「GLM 推导」历史留痕、0 回改）；0 自创 / 0 自拟公式，沿 C4.9 归零纪律**」＋**可核来源标注（给出人 / 出处）**

Our English rendering (a translation; **the Chinese above governs**): "Source of the theory bound = derivation by codex (PI adoption 2026-09-30; the source name is updated to the actual executor —— executor chosen = codex, `ask_da8ce88762c1f39cb62e95f4` q1 / q2; the former literal wording 'derivation by GLM' is retained as history and is 0 rewritten); 0 self-invented / 0 self-drafted formulas, per the C4.9 zeroing discipline" + a verifiable source attribution.

> ⚠️ **Read this declaration carefully before you use it.** It records **where the theory bound's source was ruled to come from on 2026-09-30**. **This letter does not presume that you are that party** (§7 is open) and does not ask you to adopt that name. What it asks is that **if you supply theory content, it carry a source attribution of its own** and that the **0 self-invention / 0 self-drafting constraint bind you unchanged** —— that constraint **never depended on who the executor was**: a commissioned value is **not** thereby an unsourced placeholder. If you are the named party, the declaration and the actual source are the same name and **0 attribution mismatch** arises.

### §5.3 No-conflation declaration (three easily-confused things, kept apart)

| Matter | State |
|---|---|
| **Source of the theory bound** | ✅ ruled on 2026-09-30; the source name was updated to the actual executor. **The prior reply exercised that role and has returned** |
| **Whether the theory content has arrived** | ❌ **the values have not arrived** —— arrival is a **different thing**, and is not satisfied by a change of source, by naming an executor, or by a delivered construction rule. ⚠️「来源已改」⛔ 0 等于「理论已到位」 |
| **Whether a *second* external line is being opened** | ⏳ **open** —— this letter is a draft for it; whether it is sent, and to whom, are PI surfaces (§7) |

### §5.4 Open item we do not interpret on the PI's behalf

⚠️ **Under what conditions a product of a named party's derivation counts as a "derivation" and when it falls into "self-drafted / substitute", and what the verifiability requirement on a derivation chain actually is —— both await the PI's explicit statement** (register §4-a, registered as-is; the name-update layer explicitly did 0 adjudicate it). **This letter 0 interprets that boundary.** The only posture that is safest under any reading is the one §4.1 item 4 already requires: **write out the basis, the assumptions and the source of every step** —— going beyond is fine; ⛔ leaving blanks is not.

---

## §6 Evidence-document index (three-form citation: file name + SHA-12 + path)

> **All values below were measured on our machine on 2026-10-10, in this drafting session** (`Get-FileHash -Algorithm SHA256`, lowercase, first 12 hex characters; bytes = whole-file size; lines = LF count).

| # | Document | SHA-12 (measured 2026-10-10) | Bytes / lines | Path and what is in it |
|---|---|---|---|---|
| 1 | `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | **`423c84de20d5`** | 15,457 B / 177 lines | **the spec proper**: §1 objective and kill-line / §2 anchors / §3.1–§3.3 players · mechanisms · task families / **§3.4 the measure (L61–L66)** / **§3.5 the theory bounds (L75–L76)** / §4 metrics and kill adjudication / §5 anti-attack / §6 reproduction protocol / §8 failure modes / §9 the iron rules (incl. the annotated main-caliber block) |
| 2 | `letters/_commission_codex_theory_derivation_EN_v0.2_2026_09_30.md` | **`8b15f0957e0f`** | 82,016 B / 418 lines | **the 2026-09-30 commission** (derivation task, English) —— the style anchor for this letter; §1 T-1~T-4 + clauses A/B/C, §2 the material ledger, §4 reply requirements |
| 3 | `letters/_codex_theory_derivation_reply_2026_09_30.md` | **`7558eb1a5e34`** | 71,002 B / 981 lines | ⭐ **the reply to #2** —— **the single most important document for this commission**: its §1.1/§1.4 (T-1 construction rule + 15/15 coverage), §4.2 (T-4 caliber + M-1…M-5), §5 F-1…F-11 (**the blocking defects**), §6 (**the delivered/not-delivered table transcribed at §1.3**) |
| 4 | `results/_c4_theory_source_caliber_correction_2026_09_30.md` | **`61b139efd0ef`** (⚠️ v0.2 cited `246344c5f215` / 20,165 B / 189 lines — **stale**, appended to twice since; the canonical text quoted in §5.2 was re-read and is unchanged) | 25,022 B / 238 lines | **the C4 caliber-correction register (the sole correction layer)**: §1 the changed item + the name-update layer / §2.3 ⭐ the canonical declaration text / §4-a the open derivation-boundary item |
| 5 | `results/_v5_item21_rerun_conditions_prereg_2026_09_28.md` | **`4185bdad6df5`** | 31,429 B / 335 lines | **the preregistration**: §2.4.2 **C4.8 recomputability / C4.9 zeroing discipline** (the clauses this letter binds by, quoted at H4 / H5) / the C4 acceptance rows |
| 6 | `results/_exp05_missing_true_disposition_judgment_2026_10_10.md` | **`e8e1e63a11db`** | 25,552 B / 192 lines | **the judgment that raised this exit**: §1 the measured fact baseline / §4 the recommendation / **§7 the exit table — E1 is the four C4 values, "supplied by the PI or the external line explicitly closed"; 0 on the deposon side** |
| — | `results/_c4_reply_intake_acceptance_register_2026_10_01.md` | `91e3d7a03155` | 23,591 B / 285 lines | **the intake/acceptance register of the prior reply** (PI 2026-10-01 Q2: 「采认入库（明账＋发现）；上游定义**挂账候续推**」) ⇒ **the state of the prior reply is "accepted into the ledger, upstream definitions carried as an open account"** — ⛔ acceptance ≠ the values having arrived |
| — | `letters/_c4_theory_scan_reply_claude_code_2026_09_30.md` | `2166b37e5d2a` | 27,894 B / 299 lines | an **independent read-only scan** of the same theory-input surface by another outside party (transferred to file on 2026-09-30). **Cited for completeness, not for instruction**: it independently reached the same headline ("the four primitives: named, never defined"). ⛔ **This letter adopts none of its conclusions** |
| — | `results/_five_terminal_judgments_ruling_2026_10_10.md` | `9e96d0a1ba12` | 27,315 B / 193 lines | **the five-terminal-verdict caliber ruling of 2026-10-10** —— relevant to §11 only |
| — | `results/_bayesian_baseline_design_2026_10_10.md` | `7e181a167702` | 29,783 B / 232 lines | a same-day design draft on the **Bayesian baseline** for a different leg. ⛔ **It does not define the payoff scale `u`** (its only payoff statements are constraints on two arms sharing one payoff construction) ⇒ **it does not close F-1**, and this letter does not treat it as closing anything |

> 📌 **Measurement convention**: SHA-12 = `sha256(whole-file bytes).hexdigest()[:12]`, lowercase; bytes = whole-file size; **lines = LF count**. All nine in-repository files above were measured as **UTF-8 without BOM, LF (0 CRLF pairs)** on 2026-10-10.
> 📌 ⚠️ **If you verify against a fingerprint carried in an earlier letter and it does not match**: that is **"a registered value lagging behind the final on-disk state"**, not tampering. **The on-disk state governs.** ⛔ **No document was edited by this letter to hide that** (H3).

---

## §7 ⏳ Addressee and release — **an open PI surface · the drafting side chooses nothing**

> **Stated plainly: this letter names no recipient, and the drafting side has no authority to name one.** The PI's 2026-10-10 answer authorized an **English commission draft**; it did not name a recipient, and a commission without a recipient is a draft. Below are the exits, **listed for the PI to pick from or to replace entirely**.

| Exit | Option | State as measured (honest, 0 recommendation) |
|:-:|---|---|
| **0** | **Do not send at all** | A live option: E1's own wording pairs "PI supplies them" with "**or the external line is explicitly closed**" ⇒ closing the line is a legitimate outcome of E1, and this draft would then be **a record of the option that was declined**, not a wasted effort |
| **A** | **The party named in the canonical declaration** | It delivered the 2026-09-30 derivation and reported the values not derivable. ⚠️ **Its own answer is the reason this letter exists** ⇒ re-addressing it is a second request on the same party, which it may decline |
| **B** | **A different outside theory party** | None named on disk as available for theory derivation. ⛔ The drafting side **0 invents a party** and 0 asserts any party is reachable |
| **C** | **The PI themself, as the source of the values** | E1's own first reading is "the four values are supplied by the PI" ⇒ this letter, if addressed to the PI, becomes the **specification of what supplying them would mean** rather than an external request |
| **D** | **A human theory source** | ⚠️ **Recorded here only as a category.** ⛔ **No personal name is carried into this document**: the on-disk correspondence about the previously-recorded supply line contains personal identifiers, and the project's standing anonymization practice (executed on the public repository, 2026-10-06) means those literals are **not reproduced in outward-facing material**. ⛔ The drafting side neither nominates nor rules on any person |

**What this letter therefore is**: a **recipient-neutral, self-contained English specification of the four C4 values**, complete against the material ledger, ready for the PI to address. ⛔ **It has not been sent, and sending it is the PI's act.**

---

## §8 Boundaries (strictly observed · kept on both sides)

- **0 touching existing documents**: all documents in §6 are **read-only**; ⛔ 0 modifying, 0 overwriting, 0 deleting, 0 renaming any existing document.
- **0 unauthorized threshold changes**: every cut-point of §2.3 / §2.4 is **carried at its existing wording**; ⛔ 0 created, 0 adjusted.
- **0 new external identifiers**: this letter **adds 0** external proper nouns / literature numbers / theorem names that we have not measured.
- **0 merging of derived data**: ⛔ 0 adding / 0 merging / 0 rewriting any existing JSON.
- **Keys**: unrelated to any API key; ⛔ no reply shall contain a plaintext key (H1).
- **0 killing, 0 re-grading, 0 substitution of adjudication**: this letter **issues no verdict**; ⛔ 0 changing the spec's kill-line, ⛔ 0 performing any γ registration, ⛔ 0 judging the prior reply, ⛔ 0 choosing on the PI's behalf.
- **Anonymization discipline**: ⛔ 0 carrying personal identifiers of any previously-recorded supply line into this outward-facing document (see §7 exit D).
- **Attribution boundary**: the **drafter = the Mavis team doc-writer** (`agent-0032834a3e04`); the **commissioning party = the PI**; the **value source = whoever the PI rules to addressee this** — **unnamed here**. The three **0 impersonate one another** (H2).

---

## §9 Honest declaration for this letter (failures & limitations · drafting side)

1. **The PI's authorization anchor is a transcription, not a record**: the questionnaire record behind 「外派英文委托稿」 is **not on disk** (0 record artifacts by filename scan) ⇒ this letter **does not pose as the original record**; the PI should confirm the anchor at release.
2. **The addressee is not ruled** (§7). This letter is complete against the material ledger but **cannot be sent as it stands** ⇒ ⛔ **no claim that a commission is in force**.
3. **Two upstream quantities are registered but out of this commission's scope**: `ε` (F-2) and the mechanism-internal parameters of M1. Even a complete set of four values would **not by itself** make the kill-line landable; this letter states that rather than letting a delivered answer be read as a promise.
4. **Documents opened vs measured**: this session **read in the body** the spec's quoted sections (L61–L66, L75–L76, the kill-line, the reproduction protocol), the C4 register's §1 / §2.3 / §4 layers, and the prior reply's §1.1 / §1.4 / §2 / §4.2 / §5 / §6; it **measured** (fingerprint / bytes / lines / encoding) without a line-by-line body read: the 2026-09-30 commission's remaining sections, the preregistration's non-quoted sections, and the judgment's non-§7 sections ⇒ ⛔ **0 claim of a full read of those documents**.
5. **A same-day document was checked and does not help**: the Bayesian-baseline design draft (`7e181a167702`) was searched for a payoff-scale definition and **0 found** ⇒ F-1 stands as of this measurement. ⛔ **0 extrapolation beyond the repository search surface performed.**
6. **No experiment / no network / no API**: ⛔ 0 experiment run, ⛔ 0 network access, ⛔ 0 LLM or API call, ⛔ 0 key read. Everything here is a transcription of on-disk documents or a reading of source lines, plus local `Get-FileHash` / `Test-Path` / `grep` / `read`.
7. **Skill and fallback (honest)**: the work order **did not name** a skill ⇒ **0 skill loaded**; the discipline anchor = the work order's wording + **the 2026-09-30 commission on disk** (`8b15f0957e0f`, read in full) + the prior reply's structure + the FTFB core. ⛔ **0 fabrication of skill instructions.**
8. **0 outline**: this commission contains **no reply outline** and prescribes no reply sections (H11); the shape is given, the content is not.
9. **0 presupposition of the answer**: this letter ⛔ **hints at no value, no formula and no preferred outcome**; it names the previous party's negative result as a **fact about the record**, and it names the non-availability answer as acceptable **because it is the honest one**, ⛔ **not** because a negative answer is preferred.
10. **Naming**: this document carries **no phase-number prefix**; the `v0.1` is a **document version**, 0 a phase name. ⚠️ Ledger document names quoted above **do** carry such prefixes — those are **existing on-disk names, quoted verbatim, 0 adopted**.
11. **Rendering convention**: this letter keeps the house convention of writing **"0"** before a noun to mean **"not a single" / "none"** (0 keys = no key at all). ⛔ **It is not the number zero in a mathematical expression**; all digits inside formulas, tables, hashes and quotations are carried verbatim and never form part of this convention.
12. **This is a specification, not a derivation**: no new theory was introduced; every formula, hash, cut-point and quotation is carried at the on-disk wording of upstream documents. ⛔ **No term was invented.** Where the source is Chinese, the Chinese original is retained alongside the English.

---

## §10 Consistency statement, zero-product declaration and the version chain

**Consistency statement.** This file `letters/_commission_c4_values_EN_2026_10_10.md` is **v0.1** of a **recipient-neutral English commission for the four C4 values**, structurally parallel to the 2026-09-30 derivation commission `8b15f0957e0f` and differing from it in exactly the ten registered ways of §3. It **0 reuses** that letter's addressee ruling, **0 inherits** its executor name, and **0 asserts** that any party is the theory-bound source.

**Zero-product declaration (drafting side).** This letter produced **0 new experiments**, **0 new numerical readings**, **0 new literature identifiers**, **0 new JSON or other derived data**, **0 modification of any existing document**, **0 change to any threshold**, **0 verdict**, and **0 addressee decision**. Nothing was inferred, estimated, reconstructed or completed on any party's behalf: **no value was drafted, no formula for `L`/`U`/`max_u` was proposed, no cell was pre-filled, no attribution was pre-set.** **No external call of any kind was made**: 0 LLM calls, 0 URLs fetched, 0 API keys read or written, 0 network access.

**§10.1 SHA-12 of this file.** SHA-12 is defined as `sha256(whole-file bytes).hexdigest()[:12]`, lowercase. A file cannot contain its own hash, so the measured SHA-12 of this file is reported **outside** the file, alongside its delivery. **Stated rather than claimed: this file contains no self-hash placeholder filled in after the fact, and no hash value in this letter was written without measurement.**

---

## §11 One note on what happens if the answer is "I cannot supply these values"

> Carried **verbatim** and **0 expanded**, so that a reader knows the disposition exists **without** this letter pre-deciding anything about it.

PI ruling of 2026-10-10 (the five-terminal-verdict caliber, registered in `results/_five_terminal_judgments_ruling_2026_10_10.md`, `9e96d0a1ba12`, item N-04, PI's words): 「**实在无法给料，可判 KD**」 = "**if it is genuinely impossible to supply the material, KD may be judged**".

⚠️ **What this letter does not do with that note**: it does **not** treat that ruling as applying to this commission's outcome, it does **not** predict any judgment, and it does **not** state what would follow. ⛔ The choice of any disposition, and the grading of any result, belong to the PI and our verdict lane — **not to the drafting side, and not to whoever answers this letter.**

---

**Status**: 🚫 **draft · pending PI review and release**; **addressee not ruled (§7)**; takes effect and locks at the moment of release and addressing.

**Issued by | the Mavis team doc-writer (`agent-0032834a3e04`) | 2026-10-10 · v0.1** | 0 sent / 0 pushed / 0 forwarded / 0 addressed / 0 modification of existing documents / 0 drafting of any value or formula / 0 keys / 0 network | the SHA-12 (+ bytes / lines) of this file are measured after landing and reported with the delivery receipt (**not written into this file**)
