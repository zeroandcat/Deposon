# claude 子代理回复 · C4 理论推导面只读扫描（转供落档 · 2026-09-30）

> **来源**：claude 子代理（PI 2026-09-30 转供粘贴）。转供原件＝本机 runtime assets `21-39-59-433-asset_20260930-213959-433_6e6d6aaee0c4_5c7b477a-pasted-text.txt`（26,611 B / `6e6d6aaee0c4`）。
> **性质**：外部方**只读扫描回复**（对象＝本库 `deposon-repo`，自报 1,575 件）。本件为**落档件**；分隔线后正文＝转供文本**逐字**（0 改字；LF · UTF-8 无 BOM，与原一致）。
> **落档方**：Mavis（root session `mvs_bbeb804b1a6a41109be740636eed1709`）。署名如实：产出＝claude 侧；落档 0 顶他方名头；**0 认可其全部结论**——引用先核。
> **落档抽核（本仓即时实测）**：harness 4 族实例化（T5 缺）✅｜T3·T4 各 2 选项 ✅｜P_B「≈500 calls」与 P_A「=300 calls」并存 ✅｜`boss_pa_1_rbr_rm.py` L219–222 注释逐字属实 ✅｜`paper/deposon_paper_final_cn.md` L92 ECR 定义行属实 ✅。⚠️ 一处引用对不上盘：所引 `letters/_commission_glm_theory_derivation_EN_2026_09_30.md` **本仓 0 命中**（待核；或系中文 GLM 版／codex EN 版之混称）。
> **状态**：待复核（PI）；本件 0 触发任何后续动作。

---

## Scope and method

Read-only scan of `_repo_mirror` (1,575 files: 495 `.py`, 599 `.md`, 385 `.json`). No file was created, modified, or deleted. Every quote below is verbatim from disk; line numbers are as reported by `grep -n`/`sed -n`. Where I report "0 hits" I name the pattern and the directories covered. Repeated hits inside `.tmp/`, `__pycache__/`, `.scratch_*/`, and `.git/` are excluded throughout and flagged where they matter.

---

## 1. The four primitives: named, never defined

**Verdict: does not exist.** Zero on-disk definitions. All four appear only as *names inside a requirement sentence*, or as shorthand citations of that same sentence.

The entire on-disk substance of the four primitives is two lines in one file — `_repo_mirror/docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md:75-76`:

```
- **下界 L(M, T)**：LLM 信息瓶颈下的最低可能失真（由 IC 容量 + 机制可辨识性推出）
- **上界 U(M, T)**：机制可承受的最高失真（机制收敛性条件推出）
```

Those two parentheticals are the whole of it. Nothing on disk states what an IC capacity *is* for this system, what quantity identifiability names, what the convergence condition is, or what the information bottleneck is under an LLM.

Per-pattern counts (repo-wide, `grep -rn` excluding the noisy dirs above):

| Pattern | Hits | Where they are |
|---|---|---|
| `IC 容量` | 19 | 7 files, all quoting the L(M,T) line above |
| `信息瓶颈` | 9 | 8 files; 2 are *unrelated* prior art, 6 are restatements of the same line |
| `机制可辨识性` | 13 | 7 files, same line |
| `收敛性条件` | 15 | 7 files, same line |
| `max_u` | 49 | 13 files, all citing the formula — see §2 |
| `IC容量` (no space) | **0** | — |
| `information capacity` | **0** | — |
| `信息容量` | **0** | — |

Three independent findings make this conclusive rather than merely suggestive:

**(a) The English commission letter restates the primitives as things still to be supplied.** `_repo_mirror/letters/_commission_codex_theory_derivation_EN_2026_09_30.md:302`:

```
- **0 new external identifiers**: this letter **adds 0** external proper nouns / literature numbers / theorem names that we have not measured; `u*` / `D(M,T)` / `max_u` / `L` / `U` / IC capacity and the like are **all quoted at the literal wording of the on-disk spec**.
```

That is the repo stating in its own words that "IC capacity" is a quotation of spec wording, not a definition it holds.

**(b) The two English renderings — `convergence condition` (3 hits) and `identifiability` (4 hits) — occur *only* in letters, never in a definition.** `identifiability` appears in `letters/_commission_codex_theory_derivation_EN_2026_09_30.md` and `letters/_v4_d1_response_workbuddy_2026_09_20.md`; `convergence condition` appears only in the commission letter. No `.py` file, no results JSON, and no spec defines either.

**(c) The C-4 acceptance ledger records all four as undelivered.** `_repo_mirror/results/_forgotten_recovery_register_2026_09_29.md:167-171` — C4.2 `u*(a_t)` "⛔ 0 交付 / ❌ **未交付**", C4.3 `L(M,T)` "❌ **未交付**", C4.4 `U(M,T)` "❌ **未交付**", C4.5 `max_u` "❌ **未交付**". And L200 assigns responsibility: "⇒ ⭐ **责任方 ＝ 素材提供方 / PI**".

One nuance the search does surface, relevant to distinguishing "definition" from "name": the *acceptance criteria* for these four exist in full. `letters/_commission_glm_theory_derivation_2026_09_30.md:46` specifies what a `u*(a_t)` deliverable must contain — "(a) 定义式或构造规则 … (b) 可比性前提（同一归一化）(c) 若依赖机制内部量（IC 容量 / 可辨识性 / 收敛性条件），须给出该量的表达式或可计算定义". The repo therefore has a precise *specification of the missing artifact* and no *artifact*. The register says this explicitly at `results/_theory_input_request_supplement_2026_09_29.md:406`:

```
| **9 项齐备之诚实界定** | ⚠️ §2.2 态 2 之「九项齐备」＝ **需求单 / 规格层面九项均有规格与验收口径**（含 §8.4 三条追加子条款）⇒ ⭐ **0 等于「交付物齐备」、0 等于「理论内容到位」**：C4.1 / C4.6 **盘上仍 0 命中**；`u*(a_t)` / L / U / `max_u` 内容 **仍 0 到位** |
```

Search exhaustiveness: patterns above run repo-wide over all extensions; `identifiability`, `information bottleneck`, and `convergence condition` additionally checked against `docs/`, `letters/`, `results/`, `paper/`, `tools/`, `deposon_team/`, and all root `*.py`. The two unrelated `信息瓶颈` hits (`docs/V3X/P_C_P_E_V0_1_VERIFICATION_2026_09_12.md`, `docs/V3X/V7_§3_P_C_P_E_GRAY_NOTE_2026_09_11.md`, `letters/LETTER_FROM_TRAE_2026_09_11.md`) use the term in the ordinary information-theory sense about LLM prompt compression; none connects it to `L(M,T)`.

---

## 2. `max_u`: the formula is quoted 49 times; no value exists

**Verdict: does not exist.** No payoff table, payoff scale, utility encoding, normalization constant, or per-task-family payoff definition fixing `max_u` exists anywhere on disk.

`max_u` occurs in exactly 13 non-noise files. Every occurrence is one of three things: the literal formula, the literal spec gloss, or a register entry recording that the value is missing.

The gloss, verbatim at `_repo_mirror/docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md:66`:

```
- `max_u`: 支付上界（任务族归一化常数）
```

That is a *category label* ("the payoff upper bound (the task-family normalization constant)"), not a value and not a rule. `docs/V3X/KT_B1_SPEC_V0.1.md:160` re-quotes the formula:

```
  D(M, T) = E_π[ Σ_t |u*(a_t) - u(a_t)| / max_u ]
```

and supplies no `max_u` either.

**The decisive evidence is the harness itself.** `_repo_mirror/tools/exp_harness.py` (10,090 B, 281 lines) is the only experimental implementation and it carries no payoff scale at all. Its per-task-family `value` dicts are the sole numeric encoding on disk:

- `GSM8KTask` (L153): `'value': {o: 1.0 if o == str(correct) else 0.0 for o in options}` — binary
- `StrategyQATask` (L180): same binary pattern
- `TrapTask` (L202): `'value': {o: 1.0 if o == correct else 0.5 for o in options}` — binary-ish
- `Matrix2x2Task` (L215-220): the *only* genuine numeric payoff matrix in the repo:
  ```python
  payoff = {
      ('Cooperate', 'Cooperate'): (3, 3),
      ('Cooperate', 'Defect'): (0, 5),
      ('Defect', 'Cooperate'): (5, 0),
      ('Defect', 'Defect'): (1, 1)
  }
  ```
  used at L229 as `'value': {o: payoff[(o, 'Defect')][0] for o in options}`

Those three scales — `{0,1}`, `{0.5,1}`, and a `[0,5]` prisoner's-dilemma matrix — are mutually incommensurable across task families, which is precisely what `max_u` ("任务族归一化常数") would have to reconcile. Nothing reconciles them.

**What the harness actually emits.** `ExperimentHarness.run()` at L259-266 writes records with keys `mechanism`, `task_family`, `decision_idx`, `decision`, `correct`, `is_correct`. The full record vocabulary is:

```
                        'mechanism': mech.name(),
                        'task_family': task_fam.name(),
                        'decision_idx': i,
                        'decision': decision,
                        'correct': p['correct'],
                        'is_correct': is_correct
```

There is **no `payoff`, no `score`, no `utility`, no `value` field in any output record.** The `value` dict is consumed inside `choose()` and discarded. Consequently `u(a_t)` — the actual player's payoff, the other half of the numerator — is not merely unnormalized; *it is never materialized on disk in any form*. `is_correct` is a boolean, and a boolean cannot support the `|u*(a_t) − u(a_t)|` difference.

`tools/llm_client.py` (8,118 B, 209 lines) adds nothing: `decide(self, prompt: str, options: list[str], temperature: float = 0.0) -> str` returns an option string, `max_tokens: 50`, and the entire numeric surface is absent — grep for `payoff`, `score`, `utility`, `value`, `归一化`, `max_u` across the file returns 0 hits.

**Resolution attempt 2 (data files).** Repo-wide search of `results/` for `payoff`, `支付`, `收益`, `score`, `normaliz`, `归一化` finds no candidate `max_u`. The nearest hits are unrelated: `results/deposon_3risk_v0_fixes_2026_09_11.json:124` holds a normalization for a *different* quantity (`S_eff(E) = ||(T,R,A)||/E * (1 + 0.05*log(E))`), and `results/deposon_benchmark_v1_3_details.json` `best_score: 1.0` is a per-item accuracy field.

The registers confirm there is nothing to find. `results/_forgotten_recovery_register_2026_09_29.md:171` records C4.5 `max_u` as "⛔ 0 交付 | ❌ **未交付**", and L185 audits the closest-named artifact — `deposon_team/plugins/_v3r1p1_21_ktb1_distortion_2026_09_27.py` — as "`max_u` **0**｜`D(M,T)` **0**｜`P_B_DISTORTION_CALC` **0**｜`2026-09-11` **0**" with the rule "缺 `max_u` 归一化项 ⇒ **不构成 `D(M,T)=…` 的可核实现**".

Search exhaustiveness: `max_u` repo-wide (13 non-noise files, all 49 lines individually inspected); `payoff`/`utility`/`score`/`normaliz`/`归一化`/`支付`/`收益` across `results/`; full read of `tools/exp_harness.py` and `tools/llm_client.py`; the five files in `tools/` are `exp_harness.py`, `llm_client.py`, `make_figures_v2.py`, `make_figures_v2_en.py`, `read_key.py` — no payoff/normalization module among them.

---

## 3. ECR baseline: formula found, but not where the anchor points

**Verdict: exists — but only in `paper/`, and the anchor's own referent does not contain it.**

The operational definition is at `_repo_mirror/paper/deposon_paper_final_cn.md:92`:

```
**GT-4 分布级协调比 ECR（受限一致，口径限定随行）**：操作化定义 ECR=field_mean/max(自利臂)，自利臂集 {random, degree}（预登记的 llm_prior 臂在族 S 不可得，分母只可能更小、ECR 只可能偏大，如实披露）。主报全 17 张有限值图口径：median ECR=1.333 > 1.2 预登记线；族 S 子集 13 张有限值图 median 1.5 作为补充口径并列；3 张 ECR=∞ 图按既定处理规则单独计数、不入中位数（自利臂 named=0 而场>0）。
```

English counterpart at `paper/deposon_paper_final_en.md:91`: "the operational definition is ECR=field_mean/max(self-interested arm), with self-interested arm set {random, degree}".

**What it measures.** Not a cost or effort ratio — the paper's name is "empirical coordination ratio" and the metric is `field_mean / max(random, degree)` on named Hits@3, i.e. the field arm's top-3 retrieval score divided by the best of two self-interested baselines, aggregated as a per-graph median. `paper/deposon_paper_final_cn.md:82` frames it as "ECR 是经典 worst-case PoA（Koutsoupias & Papadimitriou 口径 [10]，Roughgarden & Tardos 仿射拥塞 PoA=4/3 界 [11]）的分布级操作化对应物，非同一度量".

**What `1.333` means — and it is exactly 4/3.** The value is not an approximation of 4/3; it *is* 4/3, arising as the median of the frozen per-graph ratios. I recomputed this from `_repo_mirror/results/deposon_v20_gt.json`. `verdict.poa_per_graph_finite` holds 17 finite values; sorted, the 9th (the median of 17) is `S6_n60 = 1.3333333333333333`, and `statistics.median` over the 17 returns `1.3333333333333333`. The four `S6*` graphs and `S6` all sit at exactly 4/3, so the median lands there by construction. Stored `median_poa` (L132) matches. `n_poa_inf` is 3, corroborating the paper's "3 张 ECR=∞ 图 … 不入中位数", and `n_poa_undefined` accounts for the two unevaluated domains.

The paper is explicit that this coincidence is not evidence — `paper/deposon_paper_final_cn.md:92`:

```
且不与 4/3 等任何经典 worst-case 界做数值并置——度量不同，数值接近不构成证据。
```

**Two on-disk problems worth flagging.**

*(i) The anchor points at a section that does not contain ECR.* `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md:48` reads:

```
| `P_A_ECR_BASELINE` | 本文 §3 ECR=1.333 基线 | SHA-256 全文 → 前 12 位 | `ecr_median=1.333` |
```

But P_A §3 contains §3.2 mechanisms, §3.3 task families, and §3.4 convergence criteria (ε-Nash ε=0.01, max 50 rounds) — **no ECR formula appears in that file at all.** I read `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` (10,351 B, 172 lines) in full; the string `ECR` occurs only in the anchor table and in the §1 framing line 32. The identical self-referential pattern recurs in `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md:26` and `docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md:23`, all saying "本文 §3 ECR=1.333 基线" with no definition in §3.

*(ii) The one place in `deposon_team/` that claims to implement the ECR anchor mis-states it, then abandons the mis-statement.* `deposon_team/plugins/boss_pa_1_rbr_rm.py:219-222`:

```python
# ---------- deposon ECR baseline (P_A_ECR_BASELINE 锚) ----------
# 沿 P-A V0 spec §3: ecr_median=1.333 = (T+R+A) median
# 也可计算: 60 cells T=51, R=9 -> T/R = 5.67, T/(T+R) = 0.85
# 此处用 v3 数据 T_frac60 mean = 0.7111 作为 deposon "ECR" 等价物
```

`(T+R+A)` is identically 1 by the conservation identity, so its median cannot be 1.333; the comment is wrong on its face. The code then sets the "等价物" to `T_frac60_mean = 0.7111` (emitted at L354 as `"P_A_ECR_BASELINE": "1.333 (锚 bd1caab42b4c, 沿 P-A V0 spec §3)"` and printed at L371) — a value that is neither 1.333 nor the ECR. The genuine ECR is defined only in `paper/`.

One further disambiguation, since §... — the string `1.333` also appears in an unrelated file: `results/_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json:152` has `"d_h_straight": 1.3335000000000004`, a hyperbolic-distance quantity with no relation to ECR.

Search exhaustiveness: `ECR` repo-wide across `.md`/`.py`, filtered to definition-bearing lines; `ecr_median` and `1.333*` across `.json`; full reads of both `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` and `paper/deposon_paper_final_cn.md` §3 region; recomputation of the median directly from `results/deposon_v20_gt.json`.

---

## 4. Prior derivation artifacts: the two named plugins compute a fallback and explicitly refuse to derive

**Verdict: no draft of `u*`, `L`, `U`, or `max_u` exists. Both files disclaim computation rather than attempt it.** I read both in full.

**`deposon_team/plugins/_v3n_ktb1_distortion_bound_2026_09_27.py`** (13,055 B, 244 lines). This holds the single most explicit on-disk non-computability declaration, `L23-27` verbatim:

```
2. P-B V0 spec §7 列的 5 锚之一 `tools/distortion_calculator.py`(D1 由 data 实现)**本仓不存在**;
   tools/ 下仅 exp_harness.py / llm_client.py / make_figures_v2*.py / read_key.py。
3. 故原始 D(M,T)=E_pi[sum_t |u*(a_t)-u(a_t)|/max_u] 失真度**无法在仓内复算**(u*/u/max_u
   无实现载体)。本件执行 KT_B1_REWORK §六.2 写明的 fallback 测法(从 v19 守恒残差反向估计),
   这是仓内唯一有字面依据的真测路径; 0 新设阈值。
```

What it *does* compute: the fallback, `measured_bound = graded["max_deviation"]` from `verifier/audit/conservation.py` over `results/deposon_v19_benchmark_fixes.json`, yielding 2^-52 (2.22e-16). That is a conservation residual, not a distortion. No formula for `u*`, `L`, `U`, or `max_u` appears anywhere in the file. Its output JSON, `results/_v3_n_ktb1_distortion_bound_data_2026_09_27.json`, carries a top-level key literally named **`missing_assets_registered`** — the file is a *register of missing assets*, keyed by `"exists": false`, listing `tools/distortion_calculator.py` ("P-B V0 §7 五锚之一 (D1 由 data 实现) 本仓缺失", `anchor_sha12: "n/a"`). I verified independently: `grep -c max_u` and `grep -c 'u\*'` against that JSON both return 0.

**`deposon_team/plugins/_v3r1p1_21_ktb1_distortion_2026_09_27.py`** (30,672 B). **The exact non-computability declaration is at L184-190:**

```python
        "deposon_side": {
            "computable": False,
            "reason": ("tools/distortion_calculator.py 本仓 + 仓外按名全扫 0 命中；"
                       "核心理论输入 u*(a_t) 与理论界 L/U 未交付（bb7ca9838150 §3.5/§8/§9："
                       "理论界由〔W老师〕给定、不在 P-B 内自创）⇒ 逆向重建须自创理论 = 违 §9"),
            "proposal_A3_ruling": "不可行 + γ（提案 A-3，PI 已照案采纳）",
            "fallback_condition_A4": "PI 不允仓外只读或回填件跑不动 ⇒ 面 2 判不可算 + γ",
            "reverse_rebuild_attempted": False,
        },
```

Note `"reverse_rebuild_attempted": False` — the file records that reverse reconstruction was *not* attempted, and gives the reason: attempting it would require inventing theory, which violates the §9 rule. Instead it substitutes a non-identity axis at `L452`:

```
    "kou_jing": "非恒等 D_dec 决策轴（提案 B 冻结算式；0 使用 T/R/A、0 使用 u*）",
```

and caps its own conclusions at `L502`: `"conclusion_ceiling_frozen": ("分面结论；deposon 侧 D(M,T) 真值不可算 ⇒ 不得升级为" "「deposon 优于/不优于 OT·KD·LLMLingua」的跨面结论")`.

**The reason no draft exists is that a repo-wide rule forbids one.** `letters/_commission_glm_theory_derivation_2026_09_30.md:274` and the EN twin `:320` both carry:

```
8. **0 预设答案**：本函 ⛔ **0 暗示任何 `u*` / `L` / `U` / `max_u` 的具体形式**、0 给出候选值、0 加权、0 排序
```

and the commissions themselves are *requests to a third party* to derive the four inputs — they are not derivations. Related ledger entries: `results/_v3_recheck_21_rescript_2026_09_27.md:61`, `results/_v3_recheck_21_result_2026_09_27.json:257` and `:1624`, `results/_v3_recheck_prereg_v1p1_2026_09_27.md:185`, `results/_v3_n_recheck_llm_verdict_2026_09_27.md:120`, `results/_v5_closing_register_r2_2026_09_28.md:179`.

**Independent confirmation of the anchor's absence:** `find . -name "*distortion_calculator*"` returns nothing — 0 files on disk — while `grep -rn "distortion_calculator"` returns 85 textual references. The five-anchor file `verifier/handoff/P_B_V0_anchors_sha256_12.json` does not exist either (`results/_v5_closing_register_r2_2026_09_28.md:174` records "**`False`（0 命中）**"); the adjacent `verifier/handoff/KT_ABC1_anchors_sha256_12.json` is a different anchor family and contains none of the five P-B anchor keys.

Search exhaustiveness: full reads of both plugins; `u*(`, `max_u`, `L(M`, `U(M`, `D(M,T)`, `P_B_DISTORTION_CALC` across all `.py`/`.md`/`.json`; `find` for `*distortion_calculator*`; `Test-Path`-equivalent existence checks on both handoff anchor files.

---

## 5. Task families and mechanisms: the richest on-disk description, and its limits

**Verdict: partially exists — names plus terse parameters for T1-T5 and M1-M3, and executable code for only T1-T4 and M1-M3.** T5 has no operational content at all.

**The best on-disk description of the task families** is `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md:50-54`, which is also the *complete* one:

```
- **T1：GSM8K 风格多步算术**（n=20）
- **T2：StrategyQA 风格隐式推理**（n=20）
- **T3：合成陷阱**（n=20）
- **T4：自定义最小博弈**（n=10，明确纳什均衡点）
- **T5：低资源博弈**（n=20，每决策只给 3 步推理，最小信息情境）
```

That is one line plus a parenthetical per family. The only other substantive statement anywhere is `letters/_commission_glm_theory_derivation_EN_2026_09_30.md:84`, which adds "the 5 task families T1 – T5 × 3 mechanisms M1 – M3". `T5` gets no more detail than the line above: repo-wide, the only other hits are `docs/V3X/KT_B1_SPEC_V0.1.md:168` ("T5 低资源博弈"), `docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md:46` (the bare list item "5. 低资源博弈"), and the GLM letter restatement at `:83`. **T5 exists as a four-character label and one clause.** (All other `T5`-prefixed grep hits are false positives — `T540`, a 540-cell transmission sum in `boss_pa_1_rbr_rm.py:214` and `skill_a_p_a_60cells.py:110`.)

**The 4-choice decision space.** Best statement, `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md:40`:

```
- **统一决策空间**：4 选 1（与 deposon 概念图同结构）
```

and `tools/llm_client.py:7`: `- 4 选 1 决策(GSM8K / StrategyQA / 合成陷阱 / 2x2 矩阵)`.

The honest answer to "do the 4-choice decisions carry numeric payoffs" is **no, and not all families even have 4 choices.** In `tools/exp_harness.py`, T1 and T2 emit 4 options, but **T3 emits 2** (`TrapTask.generate_prompts`, L195: `options = ['Option A', 'Option B']`) and **T4 emits 2** (L224: `options = ['Cooperate', 'Defect']`). The "4 选 1" framing holds for half the implemented families. There is no payoff attached to the decisions: the only numeric field is the `value` dict, whose values are `1.0/0.0` (T1, T2), `1.0/0.5` (T3), and the prisoner's-dilemma `payoff[(o, 'Defect')][0]` (T4)—and as established in §2, none of it reaches the output records.

**Mechanisms M1/M2/M3.** Spec, `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md:44-46`:

```
- **M1：Deposon T+R+A 三通道**（移植 deposon 散射层）
- **M2：纯 Greedy 贪心**（无场，无守恒约束）
- **M3：Random 随机基线**（均匀采样决策）
```

What they concretely compute, from `tools/exp_harness.py`:

- **M1** (L61-94) — the only substantive one. Three named channels compose a weight per option:
  ```python
                  t = 1.0 if v == best else 0.0          # 透射: 最优直达
                  r = (v / best) if best > 0 else 0.0    # 反射: 价值耦合(归一化)
                  a = self.g_aether                       # 耗散: 均匀底
                  weights.append((1.0 - self.eta) * t + self.eta * self.g_couple * r + a)
  ```
  then samples via roulette (L88-94). It accepts `eta=0.5, g_couple=1.0, g_aether=0.1`. Worth noting for anyone reusing this: because the harness's `value` dicts are binary or binary-ish, `r = v/best` collapses to `{0,1}` or `{0.5,1}` — so the "反射耦合" channel carries almost no discriminating signal on the actual task families.
- **M2** (L103-108) — `return max(options, key=lambda o: values.get(o, 0))`. A one-line argmax.
- **M3** (L117-118) — `return random.choice(options)`. A one-line uniform draw.

The conservation identity `T+R+A=1` is **not enforced or checked anywhere in the harness** — `weights` are a weighted mixture (they sum to 1 only because of the roulette normalization at L85), and grep for `T+R+A` across `tools/` returns nothing. The three-channel vocabulary of the spec maps onto three terms in a mixture over decision options, not onto the physical channels whose conservation the paper audits.

**Two specification/implementation gaps** that matter if the task families are being counted on:

1. **The harness instantiates 4 families, not 5.** `tools/exp_harness.py:247`:
   ```python
           self.task_families = [GSM8KTask(), StrategyQATask(), TrapTask(), Matrix2x2Task()]
   ```
   T5 is absent from the code entirely, and so is absent from any 300-cell run. The docstring at L6-9 confirms the intent: "4 任务族: T1 GSM8K 风格 / T2 StrategyQA 风格 / T3 合成陷阱 / T4 2x2 矩阵 … 总 cell = 3 × 4 × 25 = 300 cells".
2. **Two incompatible cell budgets are on disk.** `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md:56` states "总 cell = 3 机制 × 5 任务族 × 33 决策/任务 ≈ 500 calls", while `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md:74-81` states "总 cell = 3 机制 × 4 任务族 × 25 决策/任务 = 300 calls" — and 3×5×33 = 495, not 500. The implemented harness matches neither exactly (3×4×25 = 300 cells, but from `run(n_decisions=25)` rather than a spec-declared count).

One **name collision** to be careful with: the anchor `P_B_DISTORTION_CALC` is defined as `tools/distortion_calculator.py` at `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md:30`, but the adjacent spec `docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md:7` anchors a *different* object also described as "（**D1 由 data 实现**）" — `tools/scaling_probe.py`, which likewise does not exist in `tools/`. Both specs use the same D1-by-data phrase for two distinct missing files.

Search exhaustiveness: full read of `tools/exp_harness.py`; `T5`/`T1`/`T2`/`T3`/`T4` and `低资源` repo-wide across `.py`/`.md`/`.json` with noise dirs excluded; M1/M2/M3 keywords (`DeposonMechanism`, `GreedyMechanism`, `RandomMechanism`, `T+R+A`) across `tools/`, `deposon_team/`, `docs/`; `ls -1 tools/` to confirm the tool inventory.

---

## Bottom line

The distortion measure is on disk as *formula, glosses, thresholds, and a full acceptance checklist* — and nothing else. Four specific absences:

1. `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md:75-76` names IC capacity, mechanism identifiability, convergence conditions, and information bottleneck in one parenthetical each, and no file anywhere defines any of the four. The English renderings (`information capacity`, `convergence condition`, `identifiability`) appear only in letters quoting that line.
2. `tools/exp_harness.py` has per-family `value` scales of `{0,1}`, `{0.5,1}`, and a `[0,5]` prisoner's-dilemma matrix, emits no payoff/score/utility field, and therefore never materializes `u(a_t)` — so `max_u` has nothing to normalize and there is no candidate value for it on disk.
3. The ECR formula exists exactly once, at `paper/deposon_paper_final_cn.md:92` (`ECR=field_mean/max(自利臂)`, arms `{random, degree}`, named Hits@3); the value `1.333` is literally 4/3 and arises as the 9th of 17 sorted per-graph ratios in `results/deposon_v20_gt.json` — verified by recomputation. Three specs anchor "本文 §3 ECR=1.333 基线" at a §3 that contains no ECR, and `deposon_team/plugins/boss_pa_1_rbr_rm.py:219-222` mislabels it as `(T+R+A) median` before substituting an unrelated `0.7111`.
4. Both plugins the user named explicitly declare the metric non-computable (`_v3n_…:25`, `_v3r1p1_…:186`), record `reverse_rebuild_attempted: False`, and carry a `missing_assets_registered` ledger rather than any draft. The repo's §9 rule and its repeated "0 代拟" clause explain why: drafting these four inputs is forbidden by the project's own discipline, so no partial derivation should be expected to appear — the absence is policy-consistent, not an oversight.