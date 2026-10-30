# Outbound Commission — the two still-missing external inputs for the `T5` face · deposon project · **DRAFT · PENDING PI REVIEW AND RELEASE**

> **This file's own full path** (outward letters carry their own path so that the file can be forwarded by copying it): `〔本地路径已脱敏〕` · **encoding**: UTF-8 without BOM · pure LF · final byte `0x0A` · 📌 **this file's own SHA-12 / bytes are reported back with the delivery receipt, not written into the file** (writing a fingerprint into the file that it fingerprints is self-referential; the self-reference loop does not enter the file).
> **To**: 〔commissioned party — **to be ruled by the PI at release**; this letter names none〕 · **From**: the Mavis team, **evidence-auditor** (deposon evidence-chain lane · `agent-11335500b168`) · **Commissioning party**: the deposon project PI · **Date**: 2026-10-23.
> **Status**: 📄 **DRAFT · pending PI review and release** — ⛔ **0 sent / 0 pushed / 0 forwarded / 0 external contact / 0 credential handled / 0 PI review performed on the PI's behalf / 0 verdict recorded / 0 KD closed / 0 phase declared complete**; the review, the release, the channel and the choice of the commissioned party all belong to the PI; **the commissioned party is required to take no action whatsoever before release**.
> **Authority anchor (verbatim)**: ① PI card answer of 2026-10-23, `ask_0c74420e06a7baa8442d557f` **Q4** (register face: `pi_rulings\_pi_card_answers_register_2026_10_23_v252.md`, `6993f1a00838`, 5,015 B) verbatim: 「**？给不了，盘上核查+联网+预实验，如实在无法得出则外派委托**」 = "**I cannot supply them; on-disk check + online + pre-experiment; if it genuinely cannot be derived, then dispatch a commission**". ② Its boundary clause 4 verbatim: 「**⚠ 外派之界**：外派**须先有「三路已尽」之证**；出件形态为**委托草案**（⛔ **0** 代发、⛔ **0** 经手凭据），状态「待 PI 核准」。」 = "**the boundary of dispatch**: a commission requires prior evidence that all three routes are exhausted; the artifact form is a **commission draft** (⛔ **0** sending on the PI's behalf, ⛔ **0** handling credentials); status '**pending PI approval**'." ③ PI ruling conveyed with this lane's drafting order of 2026-10-23: 「**可出草案，核准归 PI**」 = "**a draft may be produced; the approval belongs to the PI**".
> **Source of this commission**: `results\work\process\_t5_inputs_three_track_2026_10_23.md` (52,945 B · SHA-12 `7709625c6779` · **measured in this drafting session**) §8 — the fallback-commission clauses. This file is the separately created EN commission draft contemplated by that plan's §8-④; ⛔ **0 modification / 0 movement / 0 renaming / 0 deletion of one character of that plan or of any other existing file**; ⛔ **0 new directory**. ⚠ The drafting order cited the plan under `results\evidence\register\`; the **measured** path is the one written above and the **fingerprint matches the order's declared fingerprint** (52,945 B / `7709625c6779`) ⇒ this is a **path-record discrepancy, not a content discrepancy**. ⚠ That plan carries 2 × U+FFFD at its L233 (PI ruled: repair by a **separate erratum file**); **this letter does not touch that file**, and no part of this letter relies on that line's content.
> **What this letter transmits (and does not)**: it carries a **structural paraphrase only** of our material face — field names, cell counts, and the *kind* of constraint each cell carries — and **no** repository file, no code, no dataset, no row-level values, no prompt or observation text, no credential, and no personal information. ⛔ **0 private repository file is transmitted**; ⛔ **0 credential is transmitted or handled**; ⛔ **0 experiment run**; ⛔ **0 network access**; ⛔ **0 model or API call**; ⛔ **0 file outside the workspace read**; ⛔ **0 LLM call**.
---

## §1 Purpose

**To the commissioned party (whose name the PI rules at release — see §6 OQ-1):**

We are asking you to act as an **independent out-of-source input face** for one measurement face of a research project (`deposon`). The face is called **`T5`**; it is a decision-theoretic construction whose **structure is complete on our side and whose numbers are missing**.

**The material face, in structure only.** `T5` consists of **20 decision cells**. Each cell carries one observation record with four fields — a `prompt` (a short natural-language task statement), `options` (the actions available; **exactly 4 per cell**), `correct` (the reference key), and `value` (the realised payoff table, one number per action). The 20 cells instantiate **17 distinct scenarios** — three pairs of cells share a payoff table. Our runs use **3 seeds (42 / 123 / 456)**, and the `value` content is byte-identical across them. The `prompt` of a cell states, among other things, an **aggregate budget constraint** on the actions of that cell (e.g. "cap = 3 units", "grid limit 3 units", "shelf life 3 rounds"; a typical cell also states "only 3 steps may be spent"). No cell states how much **any individual action** consumes.

**What we were asked to produce.** Three "key inputs" for this face were specified: **①** the ingredients of a per-cell **belief** `π(·|obs_t)` over a hidden state `s` (prior / likelihood / state space); **②** an **"action → occupancy"** mapping, from which a **restricted feasible set** `Feas(obs_t)` is derived; **③** a revised pre-registration (`prereg v1.1`).

**③ is not part of this commission** (§5): its missing pieces are a PI action surface (a calibration the PI must state in one line, a base-surface choice, and an approval), not an external supply surface. **① and ② are the two we are asking you for.** We pursued both internally along three parallel routes — an exhaustive on-disk sweep (three retrieval radii, per-route evidence on file), an online literature pass (four sources per input, each with a locator and a retrieval timestamp), and a pre-experiment that derived candidate constructions and measured them — and **all three routes came back empty for both inputs**. This letter is the fallback the PI authorised: **a commission draft, pending PI approval** (§6).

**Why ① is missing — the precise reason.** Our material carries **only realised payoffs**: what was obtained under the action that was taken. It carries **no counterfactual payoff kernel** `v(s,a)` — what would have been obtained *had the world been in state `s`* and action `a` been taken. The consequence is structural, not a failure of search: a belief distribution built over our own material can only **re-weight one and the same payoff table**, so the maximising action is **unchanged for every posterior**. The missing object is therefore **not "the weights of the belief"** — it is **the state space plus a counterfactual payoff kernel**. We measured this on seven candidate belief constructions (point mass, uniform over 17 scenarios, two family-restricted uniforms, a tilted prior, and two two-state priors): **none of them passed both structural gates we are held to** (at least 2 cells whose maximising action differs from the reference key, and a non-degenerate input field), and the single construction that did move the argmax did so only by **deliberately tilting toward** three scenario pairs that happen to share one action label — a difference produced **to pass the gate**, not to carry information.

**Why ② is missing — the precise reason.** Each cell's `prompt` states an **aggregate** constraint ("cap = 3 units") and never a **per-action** consumption. So no per-action occupancy quantity exists on our side, and every occupancy table we could build locally in order to pass the structural gates came out as a **monotone restatement of the payoff values** — i.e. it carried **no information beyond the payoff table** and its apparent success was an artefact of the rule that generated it. The one locally "grounded" reading — taking consumption off the size words in the scenario labels ("full load", "half load", …) — covered **0 of the 20 cells**, because those words appear in only 7 of the 17 scenarios and no scenario contains size words for all 4 of its actions.

**What we ask of you.** Supply the two input packages specified in §2, each **complete, with provenance, and with your own certification** of the criteria in §3. We ask for **inputs, not verdicts**: everything you deliver is checked against mechanical criteria by us, and **delivery ≠ adoption** — the choice among admissible forms, and any adoption, belongs to the PI. **Honest note:** a fully compliant delivery does **not** guarantee that the resulting measurement will show discriminative power; it makes the measurement **possible**. We are buying the input, not the outcome.

---

## §2 Deliverables

### §2.0 How the delivery is packaged

Two **packages**, one per input (§2.1, §2.2). Each package = **one Markdown file** (the specification-facing narrative: definitions, formulas, provenance in prose, your own certification) **+ CSV sidecars** (the machine-readable tables, one CSV per table, fixed names). Naming convention (proposed; the PI may fix the slug at release):

| Package | Markdown file | CSV sidecars (one per table) |
|:--|:--|:--|
| **A — belief** | `T5_input_A_belief_<Slug>_2026_10_23.md` | `T5_input_A_belief_<Slug>_2026_10_23_states.csv` · `…_cell_grouping.csv` · `…_counterfactual_payoff.csv` · `…_prior.csv` · `…_likelihood_posterior.csv` · `…_provenance.csv` |
| **B — occupancy** | `T5_input_B_occupancy_<Slug>_2026_10_23.md` | `T5_input_B_occupancy_<Slug>_2026_10_23_occupancy_table.csv` · `…_grounding_basis.csv` · `…_feasibility_rule.csv` |

`<Slug>` = a short ASCII handle of the commissioned party, chosen by the PI at release. Cell ids are `t_01` … `t_20`; action ids are `a_1` … `a_4` (position within `options`); state ids are `s_01` … `s_k`. **The mapping from `cell_id` to our prompts and to our scenarios is ours, not yours** — you must keep your own cell numbering **stable across all of your files** and must state the grouping (which cells instantiate the same scenario) in the `cell_grouping` table.

### §2.1 Package A — the belief `π(·|obs_t)` (three artifacts, **none omissible**)

| ID | Artifact | What it must contain |
|:--|:--|:--|
| **A-1** | **State space `S`** | A **finite** set, enumerated; **per element**: what world state the element denotes (semantics), and where the element comes from. Your elements must be **individually identifiable** in your own document (we cannot use an unnamed or implicit state set). State explicitly that the support of your posterior is **a subset of `S`**, per cell. |
| **A-2** | **Counterfactual payoff kernel `v(s,a)`** | For **every** `s ∈ S` and **every** action `a` that can occur in the relevant cell: a **registered numeric value** (unit/dimension stated), **or** an explicit `NOT_IN_RANGE` entry **with its handling rule** (what the computation does with that pair). ⛔ No blanks, no "TBD", no bare "n/a". A pair that exists only in the realised table is still a pair you must address. |
| **A-3** | **Prior and likelihood** | How the per-cell belief is obtained: the **prior** (or — if you use an ambiguity-set form instead of point values — its **moment conditions / ambiguity-set definition**, together with a statement that point priors are then not available); the **likelihood** (or the **observation model** from which it is computed); the **provenance** of each (see the `provenance` table: locator, kind, retrieval timestamp); and an **explicit disclaimer** that the belief is **not self-authored by the requesting side** (this is an attribution requirement on our side, and your disclaimer is what discharges it). |
| **A-4** | **Per-cell coverage statement** | For each of the 20 cells: which elements of `S` are **live** in that cell and **why** (the rule that maps an observation to a subset of `S`), so that the per-cell posterior is reconstructible without asking us anything. |

⚠ **Form of A-1 … A-3 is fixed**: the three must arrive **together**. A belief without a counterfactual kernel is unusable for us (it is a re-weighting of a single table — see §1); a kernel without a state space is unusable; a state space without a prior/likelihood and its provenance is unattributable.

### §2.2 Package B — the "action → occupancy" mapping (two artifacts, **must arrive together**)

| ID | Artifact | What it must contain |
|:--|:--|:--|
| **B-1** | **Per-cell × per-action occupancy table** `occupancy[t][a]` | A numeric value for **every** cell (`t_01` … `t_20`) and **every** action (`a_1` … `a_4`) — i.e. **80 values**, unit/dimension stated, plus a **grounding basis** per value (see the `grounding_basis` table: which semantic feature the value comes from, and which material it was read off). ⚠ **The values must not be a monotone restatement of the payoff values.** A table whose ordering is isomorphic to the payoff ordering carries no information beyond the payoff table and is **rejected on sight** — see §1 and §3. |
| **B-2** | **The derivation rule "occupancy → `Feas`"** | The **exact predicate** (formula or pseudocode) that turns an occupancy table plus a cell's budget constraint into the restricted feasible set `Feas(obs_t)`, including any **combinatorial rule** if the constraint binds across a set of actions rather than one, and including how each cell's **aggregate** constraint (e.g. "cap = 3 units") binds and is reconciled. |

⚠ **B-1 alone is not acceptable**: without B-2 we would have to author the feasibility predicate ourselves, and a predicate we author is not admissible input on our side — it would make the whole construction a self-authored one. The two must arrive **in the same delivery**.

📌 **Optional alternative (clearly labelled, does not replace B-1 + B-2)**: if you believe a **lighter** form is defensible — a per-cell `Feas` table together with a **semantic argument** for why that set is a genuine restriction rather than an answer key — you may add it as a **separate, explicitly labelled** section (`ALTERNATIVE — lighter form`). It will be treated as a **different candidate**, not as a substitute, and its narrowing claim is **not** mechanically checkable against the budget constraint, so it will be adjudicated separately.

### §2.3 File formats (all files)

- **Encoding**: UTF-8 **without BOM**; **LF** line endings; **final byte `0x0A`**; no trailing blank lines beyond the final newline.
- **CSV**: comma delimiter; **one** header row; fixed column order **as listed in §2.4**; decimal point; **no** thousands separators; **no empty cell anywhere** — use the literal token `NOT_IN_RANGE` where a value does not exist, and explain its handling in the adjacent `handling_note` / `note` column; no formulas; no merged rows; ISO dates (`YYYY-MM-DD`) and ISO-8601 timestamps with an explicit offset.
- **Markdown**: the section labels **A-1 … A-4** / **B-1 … B-2** must appear as headings, so that we can check each artifact against its criterion one by one; every numeric table must also appear in the corresponding CSV (the CSV is authoritative for values; the Markdown is authoritative for prose).
- **Provenance**: every external source cited with a **locator** (URL / DOI / document id) **and a retrieval timestamp**; every number that is your own derivation must have its **derivation recipe and assumptions** written down. ⛔ No number without a stated origin.
- **Fingerprints**: ⛔ **do not write your own file's SHA-12 inside that file**; report the SHA-12 and byte count of each delivered file **in your reply text**, outside the files.
- **Size discipline**: deliver **only** the files listed in §2.0–§2.4, plus your reply text. ⛔ No unsolicited extra documents, no appendices of background reading.
- We do **not** prescribe the structure, the level of detail, or the writing style of your prose beyond the labels and the formats above — that is yours.

### §2.4 Column schemas (fixed)

**Package A CSVs**

| File | Columns (in this order) |
|:--|:--|
| `…_states.csv` | `state_id, state_semantics, source_note` |
| `…_cell_grouping.csv` | `cell_id, scenario_group_id, scenario_note` |
| `…_counterfactual_payoff.csv` | `state_id, cell_id, action_id, v_value, unit, integrable_status, handling_note` |
| `…_prior.csv` | `cell_id, state_id, prior_value, prior_kind, source_locator` |
| `…_likelihood_posterior.csv` | `cell_id, state_id, likelihood_value, observation_model, posterior_value, cell_posterior_sum, tolerance` |
| `…_provenance.csv` | `artifact_id, source_locator, source_kind, retrieved_at, disclaimer_text` |

**Package B CSVs**

| File | Columns (in this order) |
|:--|:--|
| `…_occupancy_table.csv` | `cell_id, action_id, occupancy_value, unit` |
| `…_grounding_basis.csv` | `cell_id, action_id, semantic_feature, material_basis, note` |
| `…_feasibility_rule.csv` | `rule_id, predicate, applies_to_cells, budget_binding, handling_note` |

### §2.5 Format illustration (**generic placeholders — not our data**)

The table below shows the **shape only**. Every bracketed token is a placeholder; ⛔ **returning this illustration unchanged, or filling it with stand-in numbers that were invented to fill it, is a rejected delivery** — the same defect as a table built to pass a gate.

```
cell_id | action_id | occupancy_value | unit
t_01    | a_1       | <units>        | <unit>
t_01    | a_2       | <units>        | <unit>
…       | …         | …              | …
```

---

## §3 Acceptance criteria

The criteria below are **our in-register mechanical criteria**, quoted here by identifier so that you can check your delivery against them one by one. They are **not** our invention and **not** negotiable inside this commission. ⚠ Two of them are **caliber items that are still open on our side** (`A2-8`, `A2-9`); where that is the case we say so, and we do not ask you to resolve them.

### §3.1 Package A — criteria `A1-1` … `A1-10`

| ID | What must hold | What you must include so that we can check it |
|:--|:--|:--|
| `A1-1` | **State space on record and enumerable** — `S` is finite; each element is individually identifiable in your document; the support of `π(·\|obs_t)` is a subset of `S`, checkable **per cell**. | The `states` table; an explicit per-cell statement of which `s` are live (A-4). |
| `A1-2` | **Normalisation** — per cell, `Σ_{s∈S} π(s\|obs_t) = 1` (numerical tolerance ≤ `1e-9`; **the tolerance value must be written in the document**). | Per-cell posterior sums in `likelihood_posterior.csv` (columns `cell_posterior_sum`, `tolerance`). |
| `A1-3` | **Integrand defined over the whole domain** — for **every** cell `t`, **every** `a ∈ options(t)` and **every** `s ∈ S`, `v(s,a)` has a registered value; a pair with no definition must be **explicitly recorded as "not in integrable range" with a disposition**; ⛔ no blanks. | The `counterfactual_payoff` table with `integrable_status` and `handling_note`; no row omitted. |
| `A1-4` | **The expectation is computable, per cell and per action** — `E_{s∼π}[v(s,a)]` computable for **all** cells × **all** actions; no "not obtained" cell. | Either the computed matrix in the Markdown, or the rule + inputs sufficient to recompute it. |
| `A1-5` | **Non-empty key** — the selected action set `K_t` is non-empty in **every** cell; **violating cells = 0**, reported cell by cell (⛔ "not obtained" may not be reported as "0 violations"). | The per-cell count of violations. |
| `A1-6` | **Structural guarantee of discriminative power (a priori)** — in the construction surface, **at least 2 cells** whose `argmax_a E_{s∼π}[v(s,a)]` differs from `correct`; if this fails, that construction may not enter measurement at all. | Your own a-priori certification, computed on your delivered data, with the per-cell list. |
| `A1-7` | **Non-degeneracy, field by field** — for each input field of the construction: `n_distinct` / min / max / std; **any input field with `n_distinct ≤ 3` raises a degeneracy alarm**. | The field-level statistics for every input field. |
| `A1-8` | **`std` reported in both readings** — population (denominator `n`) **and** sample (denominator `n−1`), side by side; ⛔ choosing one reading. | Both values, per field. |
| `A1-9` | **Attribution and disclaimer on file** — the delivery carries a **source** field and a **disclaimer** field, and the disclaimer that the belief is **not self-authored by the requesting side** is on file. | The `provenance` table, including the disclaimer text. |
| `A1-10` | **Same-cell pairing** — your per-cell correspondence does **not** alter the cell ↔ scenario mapping: readings still land on the same 20 cells, the same seeds, the same `H` domain, with both readings of `H` carried side by side. | A statement that your cell numbering is stable and complete (20 cells, the 3 seeds listed above, and the scenario grouping). |

### §3.2 Package B — criteria `A2-1` … `A2-10`

| ID | What must hold | What you must include so that we can check it |
|:--|:--|:--|
| `A2-1` | **`Feas` domain / range on record** — every cell gives the **per-action selection or rejection** within `options(t)` **together with its reason item** (the occupancy value, or a semantic commitment). | The `occupancy_table` + `grounding_basis` tables, and the per-action outcome implied by your rule. |
| `A2-2` | **Consistency with the cell's total constraint** — for each cell, the feasibility predicate over occupancy combinations is **checkable cell by cell** against that cell's stated total budget; **contradictory cells = 0**. | The `feasibility_rule` table, with the budget each rule binds to. |
| `A2-3` | **`Feas` computable per cell** — `\|Feas(obs_t)\|` computable in **all** cells and reported cell by cell (also the gap against `\|options(t)\|`, which is 4). | Per-cell counts. |
| `A2-4` | **Genuine narrowing** — the number of cells with `\|Feas(obs_t)\| < \|options(t)\|` is **≥ 1** (measured denominator = 4), **and** the number of cells in which `Feas` equals `options` is **0**. Both halves are required. | The two counts, separately. |
| `A2-5` | **Non-empty key** — `K_t ≠ ∅` in **every** cell; violating cells = 0. | The per-cell count of violations. |
| `A2-6` | **Structural guarantee of discriminative power (a priori)** — **at least 2 cells** whose `argmax_{b∈Feas} v(b)` differs from `correct`. | Your own a-priori certification, with the per-cell list. |
| `A2-7` | **Non-degeneracy of the input field** — report `n_distinct` / min / max / std of the **occupancy quantity**; any input field with `n_distinct ≤ 3` raises a degeneracy alarm. | The statistics for the occupancy field. |
| `A2-8` | ⚠ **Caliber item — open on our side.** Our working reading: the input field is the **numeric occupancy value**, and the binary feasibility indicator is a **derived readout**. ⛔ If the only input field were the binary indicator, its `n_distinct` = 2 ≤ 3 and the degeneracy gate would fire automatically ⇒ that form is not admissible without a caliber ruling. **Please deliver the numeric occupancy values.** | The numeric values; you do not need to resolve the caliber. |
| `A2-9` | ⚠ **`std` in both readings**, and the scope of the degeneracy gate is **not** prejudged on our side — population and sample side by side; ⛔ choosing one reading. | Both values, per field. |
| `A2-10` | **Same-cell pairing** — the same 20 cells, the same seeds (42 / 123 / 456), the same `H` domain, both readings of `H` side by side. | The same statement as in `A1-10`. |

### §3.3 Cross-cutting rules for the delivery

1. **Each criterion must be addressed.** For every identifier above, your delivery states either "holds" **with the supporting computation**, or "does not hold" **with the failing item named**. ⛔ No criterion left unaddressed; ⛔ "not applicable" must be justified in one line.
2. **Honest partial delivery is preferred over a complete-looking one.** If a criterion cannot be met, say which one and why — a delivery that states its own gap is **usable**; a delivery that quietly fails a criterion is not, and neither is one that manufactures a value in order to pass a gate. **A "built-to-pass" construction is a rejected delivery**, even when it passes every gate.
3. **The hardest requirement, stated plainly.** `A1-6` and `A1-7` must be satisfiable **simultaneously** (and `A2-4`, `A2-5`, `A2-6`, `A2-7` likewise); `A1-3` and `A2-2` must hold outright. This is why our own constructions failed. **If your construction cannot satisfy them together, tell us rather than bending one of them** — that answer is itself decision-relevant for the PI.
4. **Your certification is yours; our check is the arbiter.** We recompute every statistic from the delivered CSVs. ⛔ A claimed statistic that does not recompute is treated as a failed criterion.
5. **Nothing here is an adoption.** Passing every criterion makes your input *admissible*; it does not make it *chosen*. That decision belongs to the PI, on our report.

---

## §4 Constraints

**C-1 · No repository file is transmitted, and none may be requested.** This letter carries a **structural paraphrase only** — field names, cell counts, the *kind* of constraint each cell carries, and the seeds we use. It carries **no** repository file, **no** code, **no** harness, **no** dataset, **no** row-level values, **no** prompt or observation text. ⛔ **0 private repository file is transmitted with this commission.** ⛔ Do **not** ask us for the repository, for file extracts, for raw prompt text, or for the payoff values; ⛔ if you judge that you need more than this letter's abstraction, **state that as an open item in your reply** and we will put it to the PI — do not treat the request as a blocker you must solve by guessing.

**C-2 · No credentials, of any kind.** ⛔ **0 credentials transmitted** by this letter, and ⛔ **0 credentials handled**. Do not request, quote, echo, store, or include: API keys, tokens, passwords, private repository URLs, internal access paths, session or run identifiers, or the internal roster. ⛔ If a step of your work would require a credential, **stop at that step** and report the requirement as an open item; a step that needs our credential is not yours to take.

**C-3 · No personal information.** ⛔ Do not include in your delivery or your reply the name, contact detail, or any identifier of the PI, of any team member, of any reviewer, or of any person represented in our material; ⛔ no unpublished third-party data; ⛔ no private personal data of any kind. Refer to us by role ("the requesting side"). If your method requires a human judgement about a person, describe the **semantic feature** you use rather than the person.

**C-4 · No action on our side, and no access to our systems.** You have **no write access** to anything of ours. ⛔ Do not modify, move, rename, delete, or create anything on our side; ⛔ do not attempt to run, clone, or invoke our harness or any experiment of ours; ⛔ do not call any model or API on our behalf; ⛔ do not read, scan, or probe any local path, host, or repository of ours; ⛔ do not attempt to authenticate to anything of ours.

**C-5 · One-to-one channel.** Address your reply through the channel the PI opens with this commission. ⛔ Do not forward this letter, do not contact third parties about it, and do not seek a second opinion outside the commission; ⛔ do not quote this letter to anyone.

**C-6 · Text-only delivery.** Deliver **text only** — Markdown and CSV. ⛔ No executable attachments (no scripts, binaries, notebooks, macros, archives); ⛔ no links to a location that holds our material; ⛔ no embedded objects. Every CSV must be readable as plain UTF-8 text.

**C-7 · No adoption implied.** ⛔ Do not state or imply that your delivery has been accepted, adopted, or published by us, and ⛔ do not represent a criterion as satisfied without the computation that supports it.

**C-8 · Lawful sources only.** Use only sources you may lawfully access (public literature, your own derivations, your own prior work). ⛔ Do not access anything behind access control; ⛔ do not reproduce long copyrighted text — short quotation with a locator is enough; ⛔ every source must carry a locator and a retrieval timestamp (§2.3).

**C-9 · Confidentiality of the commission itself.** Treat this letter and its abstract interface as internal research material. ⛔ Do not republish it, and ⛔ if you describe the construction in your own work, describe the **abstract interface only**, not the letter.

**C-10 · Before release, do nothing.** This commission is a **draft pending PI approval**. ⛔ **0 sent / 0 pushed / 0 forwarded / 0 external contact** on our side; the commissioned party is required to **take no action whatsoever** until the PI releases this letter, names the party, and opens the channel.

---

## §5 Non-goals

What this commission explicitly does **not** ask for:

| # | Not asked | Why it is stated |
|:-:|:--|:--|
| **N-1** | **Adjudicating our criteria or our kill-lines.** | The criteria in §3 are ours to apply. You supply inputs and certify; we check; the PI rules. ⛔ Please do not argue our criteria into or out of existence. |
| **N-2** | **Choosing, or recommending, a construction arm**, or telling us which admissible form we should adopt. | That is the PI's call on our report. Your comparison of your own candidates is welcome as information, but a recommendation is not a deliverable. |
| **N-3** | **Running or reproducing any experiment of ours** (no harness, no re-run of our measurements, no attempt to obtain our raw numbers). | The measurement face is ours to run; a commission for inputs is not a commission to run. See also C-4. |
| **N-4** | **Changing anything on our side** — no file, no threshold, no pre-registration wording, no existing conclusion, no "correction" of our material. | We modify nothing on the strength of a delivery without the PI's ruling, and the PI has not ruled on anything here. |
| **N-5** | **Drafting the third input (`prereg v1.1`).** | Its three missing pieces are a **PI action surface** — a one-line calibration of the discriminative quantity, a choice between two base surfaces (a 17-scenario surface or a 5-scenario surface), and an approval. A commission cannot discharge any of them, so we are **not** sending this to you. If you wish to note relevant practice, that is welcome as commentary, but it is **not** a deliverable. |
| **N-6** | **Any promise that your input will be used**, or that the resulting measurement will succeed or show discriminative power. | We are buying an input, not an outcome; a compliant delivery still leaves the measurement to be run and judged. |
| **N-7** | **A review of our design, our material, or our past results.** | No critique was requested; unsolicited critique is out of scope (though a note that something in our brief looks wrong is welcome and will be reported). |
| **N-8** | **A literature review as an end in itself.** | Literature may be cited **only** as the provenance of a delivered number, or as the grounding basis of an occupancy value. A bibliography with no numbers attached to it is not a deliverable. |
| **N-9** | **A prescribed structure or wording for your prose.** | We fix the file names, the labels, the columns and the encoding; the argument, the depth and the style are yours. |
| **N-10** | **Handling credentials, the channel, or the release.** | All three are the PI's. See C-2, C-5, C-10. |
| **N-11** | **Resolving our open internal caliber items** (`A2-8`, `A2-9`, and the two readings of the `H` domain). | They are internal rulings; we do not delegate them and we do not want a foreign ruling smuggled in as data. |

---

## §6 Open questions for the PI

📌 These are the points this drafting lane **cannot decide** and has **not** decided. Each carries a **recommendation and its reason**, so that the PI can rule on the merits rather than on a bare question. **This lane rules nothing here**; the PI's ruling is recorded in the release note.

**OQ-1 · Which commissioned party, and one party or several?** *(白话：派给谁做，派一家还是几家。)*
- Candidate faces follow the registry precedents of the T2/T3 commission family (GLM / codex / copilot agent / grok face — the precedent envelopes are in `letters/`). **This letter names none.**
- **Recommendation: one party for both packages**, with a second party engaged **only if** the first reply fails to self-certify the completeness criteria (`A1-1`…`A1-3`, `A2-1`…`A2-2`).
- **Reason:** the two packages rest on one material face and one vocabulary of states and of grounding; splitting them across parties invites inconsistent grounding between the belief and the occupancy — the exact defect class this commission exists to repair. A single party also keeps one cell ↔ scenario grouping coherent across both packages.

**OQ-2 · Which form of Package A is admissible — the full three-artifact form only, or may a "direct expected-value table" shortcut be accepted as a fallback?** *(白话：信念那包，是只收全三件，还是也收"直接给期望值表"的简版作退路。)*
- **Recommendation: the full form (state space + counterfactual kernel + prior/likelihood) as primary; the shortcut admissible only if explicitly labelled a fallback and not used for the degeneracy check until the caliber question is ruled.**
- **Reason:** under the shortcut the per-cell belief field itself is not on file, so `A1-7`'s target field is undefined — an internal caliber item (a candidate for the PI or `verdict-keeper`). Labelling the fallback keeps the route open without pre-empting that ruling.

**OQ-3 · Which grounding route for Package B — a desensitized label digest, or a grounding protocol that we instantiate locally?** *(白话：占用量表怎么"接地"——给对方一份脱敏标签摘要，还是让对方只给规则、由我们本地填。)*
- **Recommendation: release a desensitized label digest** — scenario labels and action labels per cell, **no payoff values, no prompt text, no personal data**.
- **Reason:** (a) the occupancy values are then grounded **at the source**; (b) it avoids the ambiguity that a table we instantiate ourselves could be read as a **self-authored** table, which our in-register rules exclude as a candidate path; (c) labels alone sit comfortably inside the desensitization boundary already set for this letter (§4 C-1, C-3).
- If the PI prefers the protocol route, the PI also has to rule whether our local instantiation counts as self-authorship. **This lane does not decide that.**

**OQ-4 · Deadline, and are partial deliveries acceptable?** *(白话：回件期限；只交一半行不行。)*
- **Recommendation: accept a partial delivery with reasons, and let the two packages carry different deadlines.**
- **Reason:** a complete Package A already unblocks one of the two constructions; an all-or-nothing rule risks losing both. An explicit "this package is not delivered, for these reasons" is a **usable** answer for the PI's decision face; a silent gap is not.

**OQ-5 · Should the caliber item `A2-8` be pre-ruled before release?** *(白话：退化门查哪个字段（数值占用量 vs 二值可行指示）——是否先裁再发。)*
- **Recommendation: yes — state the working reading in the release note** (input field = the **numeric occupancy value**; the binary feasibility indicator = a derived readout).
- **Reason:** the letter already asks for the numeric values; without the ruling on our side, a delivery that also carries a binary indicator could be read two ways — and on the binary reading the degeneracy gate fires automatically (`n_distinct` = 2 ≤ 3). A pre-ruling removes an avoidable late abort. This is a request that the PI pre-rule, **not** a request that this lane decide.

**OQ-6 · Is a single calibration cell enough as a granularity anchor?** *(白话：是否附一个脱敏"标定格"（4 个动作标签＋其占用值＋预算约束）来统一粒度。)*
- **Recommendation: yes — one desensitized calibration cell**, alongside OQ-3's digest (or instead of it, if the PI prefers minimal exposure).
- **Reason:** without any anchor, "units" means something different in each party, and the deliverable stops being comparable; one cell's labels and one budget constraint carry almost no information while fixing the granularity of the quantity.

**OQ-7 · Release channel and file set — same channel as the precedent EN commissions, and one file or two?** *(白话：走哪条通道发；英文一件还是另立中文件。)*
- **Recommendation: one file, through the same channel as the precedent EN commissions** (the PI's own channel to the chosen party), with **no separate Chinese sister file** — the Chinese comparison at the end of this file is for the PI's review, and a second file would double the version-tracking surface for no gain.
- **Reason:** one file means one fingerprint to verify, one artifact to release, and one place where the status line lives.

---

## 中文对照（供 PI 复核；英文为正文，本段仅供快速对读）

本件系 `T5` 面「三样关键输入」中**仍缺之两样**的**英文外派委托草案**，状态**待 PI 核准·⛔0 代发**（PI 已裁「可出草案，核准归 PI」）。其源件为 `results\work\process\_t5_inputs_three_track_2026_10_23.md`（52,945 B／`7709625c6779`，本棒当轮实测；派工单所载路径 `results\evidence\register\` 与实测路径**不符而指纹逐位相符** ⇒ 属**路径记录之偏差、非内容偏差**；该件 L233 之 2 处 U+FFFD **本棒未动**，PI 已裁「修·另立勘误件」）。**为何外派**：样①（信念分布之所需）之缺**非「权重未搜到」而是结构性的**——素材面只载**已实现** payoff 表、不载反事实核 `v(s,a)`，故任何后验皆**只重加权同一张表**、argmax 不变；样②（动作→占用）之缺**非「表未搜到」而是载体缺失**——`prompt` 只给**总额型约束**（`cap = 3 units` 一类）、**0 给逐动作占用量**，而本地能过机械门者**必为 payoff 之单调重述**（撞在册「为过门而造」之禁），唯一「有接地」读法覆盖 **0/20 格**；样③（`prereg v1.1`）**不列入外派**——其缺为 **PI 动作面**（`C-R3` 之明定、基面之裁、核准），外派承接无意义。**所请交付**：**包 A（信念）三件物**（状态空间 `S` ＋ 反事实核 `v(s,a)` ＋ 先验/似然**及来源与免责**，缺一不可）；**包 B（占用）两件物**（逐格×逐动作占用量表 ＋ 「占用→`Feas`」之确切判式，**须同批给**——只给占用表则判式仍须我方自拟，撞禁）；二包均附**格式与命名约定**（Markdown ＋ 固定名 CSV sidecar、UTF-8 无 BOM、纯 LF、末字节 `0x0A`）。**验收判据**照录在册机械判准 `A1-1`…`A1-10`／`A2-1`…`A2-10`（`A1-6`∧`A1-7`、及 `A2-4`∧`A2-5`∧`A2-6`∧`A2-7` 须**同取**，`A1-3`／`A2-2` 须成立；`A2-8`／`A2-9` 为**在册未裁之口径项**）。**约束**：⛔0 传仓内私有件（本件仅传**结构性转述**：四键名、格数、约束之种类、种子）、⛔0 传凭据、⛔0 涉个人信息、⛔0 触我方系统、⛔0 送达（PI 核准前受托方 0 动作）。**非所请**：⛔0 代裁、⛔0 择臂、⛔0 跑实验、⛔0 改我方任何件、⛔0 起草 `prereg v1.1`、⛔0 承诺被采。**候 PI 裁 7 条（各附推荐项）**：①派谁/一家还是几家（荐：一家包两包，续派仅在完整性判准不过时）；②信念包是否收「直给期望值表」简版作退路（荐：全三件为主、简版仅作标注退路且不施于退化门）；③占用表接地之径（荐：放**脱敏标签摘要**——只给标签、无 payoff 值、无 prompt 文本；替代径「只给规则由我方本地填」有「是否构成自拟」之待裁）；④期限与部分交付（荐：许部分交付、两包可异期）；⑤是否先裁 `A2-8`（荐：先裁，免后abort）；⑥是否附一脱敏标定格以统一粒度（荐：附一格）；⑦通道与件数（荐：沿英文先例之通道、**只发此一件**，中文对照留在件内不另立中文件）。**本棒之诚实交代**：草案之**两包可行性未实测**——包 A 是否有外部可得的反事实核、包 B 是否有外部可得的接地占用量，**均属未知**；本棒⛔0 联网、⛔0 跑实验、⛔0 造数，故**不保证**受托方能交；本件所保者唯「所请之形可核、判据照录、界不越」。

T5 外派委托·英文草案 · 已落盘 · 呈 PI 核准
