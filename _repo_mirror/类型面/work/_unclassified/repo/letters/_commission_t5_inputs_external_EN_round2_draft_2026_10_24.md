# Outbound Commission — Round 2 for the two still-missing external inputs on the `T5` face · deposon project · **DRAFT · PENDING PI REVIEW AND RELEASE**

> **This file's own full path** (outward letters carry their own path so that the file can be forwarded by copying it): `〔本地路径已脱敏〕` · **encoding**: UTF-8 without BOM · pure LF · final byte `0x0A` · 📌 **this file's own SHA-12 / byte count are reported with the delivery receipt, not written into the file** (a fingerprint written into the file it fingerprints is self-referential; the self-reference loop does not enter the file).
> **To**: the commissioned party of record — **the party that returned the round-1 reply**; this letter **names no party**, and the channel, the party and the release remain the PI's. **From**: the Mavis team, **evidence-auditor** lane (deposon evidence-chain lane) · **Commissioning party**: the deposon project PI · **Date**: 2026-10-24.
> **Status**: 📄 **DRAFT · pending PI review and release** — ⛔ **0 sent / 0 pushed / 0 forwarded / 0 external contact / 0 credential handled / 0 PI review performed on the PI's behalf / 0 verdict recorded / 0 KD closed / 0 phase declared complete / 0 gate declared achieved / 0 decision taken on whether to send**; the review, the release, the channel and the transmission of the attachment all belong to the PI; **the commissioned party is required to take no action whatsoever before release**.
> **Authority anchor (verbatim)**: ① PI card answers of 2026-10-24, card `ask_e98a5eab74bfc2e56a42613b`, register face `pi_rulings\_pi_card_answers_register_2026_10_24_v267.md` (3,752 B · SHA-12 `87dc4d121046`, measured in this drafting session) — **four answers, verbatim**: 「**取 3A：盲式接地＋我方核（荐）**」 = *"take 3A: blind grounding plus verification on our side"* (§1 of this letter)｜「**我方做（荐）**」 = *"the requesting side does it"* (OI-1, §2)｜「**我方算脱敏摘要（荐）**」 = *"the requesting side computes the desensitized digest"* (OI-2, §2)｜「**不采纳，只入册（荐）**」 = *"not adopted, registered only"* (§0). ② The same register §2-1, verbatim: 「**裁定**：**盲式外部接地**——受托方在**不见 `correct`／`value`** 之条件下构造；**`argmax ≠ correct` 之核对由我方**（持原值者）完成。」 ③ The same register §2-2-3, verbatim: 「**二者皆须材料在盘**（T5 之 20 格定义、`correct`／`value`、情境配对应）。若材料不在盘，则**⛔0 编造**，须如实报缺。」 — the material was found on disk and the digest was computed on it (the digest's own §0 records that verification, with a positive control). ④ The same register §2-3-1, verbatim: 「**回函不采纳为交付**；**只入册**」 = *"the reply is not adopted as a delivery; it is registered only."*
> **Source of this round-2 commission**: the round-1 commission `letters\_commission_t5_inputs_external_EN_draft_2026_10_23.md` (41,134 B · SHA-12 `47d913439e89`) · the round-1 reply `REPLY_TO_COMMISSION_T5_INPUTS_EXTERNAL_EN_2026_10_23.md` (31,050 B · SHA-12 `727d85d20aff`, held outside this repository) · the reply register `results\work\process\_t5_reply_from_codex_register_2026_10_23.md` (4,484 B · SHA-12 `c51b4b844603`) · the desensitized digest `results\work\process\_t5_desensitized_pack_2026_10_24.md` (31,937 B · SHA-12 `90a5e34e1ae6`). ⛔ **0 modification of one character of any existing file**; ⛔ **0 new directory**; ⛔ **0 movement / renaming / deletion**; this letter is **1 new file** and nothing else was written.
> **What this letter transmits (and does not)**: it transmits a **manifest of a desensitized digest** — file names, byte counts, SHA-12 fingerprints, and the mapping of digest sections onto acceptance criteria — and **not** the digest's body. ⛔ The digest is a **separate attachment**, transmitted only at the PI's release; ⛔ **0 repository file is transmitted with this letter**; ⛔ **0 credential is transmitted or handled**; ⛔ **0 experiment run**; ⛔ **0 network access**; ⛔ **0 model or API call**; ⛔ **0 LLM call**; ⛔ **0 read of any archived area's contents** (the archived area was acknowledged by name and fingerprint only).
> **Drafting-lane registration (truthful, written as fact — not as a claim that no skill applies)**: **agent**: `worker` (session `mvs_bba4bfafb46846fb83b6a1e7a370c215`) · **skills carried in this session** — each listed with the path, byte count and SHA-12 **measured live in this lane**: `folder-cleanup-assistant` (`〔本地路径已脱敏〕`, 4,470 B, SHA-12 `9c5b1d8b8b8e`)｜`markdown-mermaid-writing` (`〔本地路径已脱敏〕`, 14,888 B, SHA-12 `edfa23bfc413`)｜`docx` (`〔本地路径已脱敏〕`, 20,084 B, SHA-12 `cfbabd72b1ae`). ⚠ **0 of these skill bodies was loaded or executed in this session** — the deliverable was produced with the desktop file tools `read` / `write` / `grep` / `glob` and `bash` (PowerShell 5.1) for the byte-level self-check. This sentence records what **was** and **was not** exercised; it is not a "no skill needed" claim.
> 📌 **Codes in plain words, once, for the reader** — `T5` = the decision-theoretic measurement face this project is stuck on｜`correct` = the reference key of a cell (which action is right)｜`value` = the realised payoff table of a cell (what was obtained under the action taken)｜`OI-1` / `OI-2` / `OI-3` = the three open items the round-1 reply raised for the PI｜`3A` = the ruling "blind external grounding + requesting-side verification"｜`A1-*` / `A2-*` = the twenty acceptance criteria of Packages A and B｜`C-1` / `OQ-3` = our desensitization boundary and the digest release question｜`Feas` = the restricted feasible set derived from an occupancy table｜`argmax` = the action with the highest value.

---

## §0 Status of round 1

**Round 1 is closed on our side; this letter is round 2 and it changes the request, not the boundary.**

### §0-1 What happened in round 1

| Item | State |
|:--|:--|
| Round-1 commission | `letters\_commission_t5_inputs_external_EN_draft_2026_10_23.md` (41,134 B · SHA-12 `47d913439e89`) · approved by the PI as a draft (register face `results\work\process\_t5_reply_from_codex_register_2026_10_23.md`, §3) · released · answered |
| Round-1 reply | `〔本地路径已脱敏〕` (31,050 B · SHA-12 `727d85d20aff`) · **registered**, **not adopted** |
| Reply register | `results\work\process\_t5_reply_from_codex_register_2026_10_23.md` (4,484 B · SHA-12 `c51b4b844603`) |
| PI ruling on the three open items | `pi_rulings\_pi_card_answers_register_2026_10_24_v267.md` (3,752 B · SHA-12 `87dc4d121046`) — **`OI-1` / `OI-2` / `OI-3` / adoption all ruled** |
| Desensitized digest | `results\work\process\_t5_desensitized_pack_2026_10_24.md` (31,937 B · SHA-12 `90a5e34e1ae6`) — the three pieces listed in §2 |

⚠ **Where the reply sits**: the reply file is **outside this repository** (it was written in the party's own workspace). Our register records it **by name and fingerprint only** and does **not** fold it into this tree's root inventory. It is cited here by name and fingerprint in the same manner.

### §0-2 Status of the round-1 reply: **registered, not adopted**

Three independent texts say the same thing, and they are mutually consistent:

1. **The reply says so itself** (§0 of the reply, verbatim): *"Delivery is not adoption."* — and its closing line: *"This reply performs 0 modifications to the `deposon` repository, handles 0 credentials, conducts 0 probes or scans of the requesting side's repository/harness/data, and fabricates 0 stand-in CSV tables."*
2. **Our register says so** (§3, verbatim): 「**采纳** | **未采纳**（回函明载「delivery is not adoption」）」.
3. **The PI ruled it** (`pi_rulings\_pi_card_answers_register_2026_10_24_v267.md` §2-3, verbatim): 「**回函不采纳为交付**；**只入册**」 = *"the reply is not adopted as a delivery; it is registered only."*

📌 **Read together:** "registered" means the reply and its substance are **on the record** and remain citable. "Not adopted" means **nothing in it has entered our construction** — it is **not** an input, **not** a candidate arm, **not** a fallback that may be revived silently. A later round may revisit adoption **only on the PI's ruling**, and the PI has explicitly deferred that: 「**待 OI-1／OI-2／OI-3 解后，另轮再议采纳**」.

### §0-3 Why it was not adopted — and what exactly we carry forward

**The reason.** The round-1 reply is a **specification-level** reply: it delivered the **formal shape** of the two packages (`A-1` … `A-4` and `B-1` … `B-2`), a workable **formulation skeleton** (state space `S`, counterfactual kernel `v(s,a)`, a prior/likelihood observation model, a feasibility predicate), a 20-item self-audit, and three open items — but it **instantiated no numbers at all**. It said so itself and we concur with its reading: under our desensitization boundary the numeric instance of the 20 × 4 tables was not constructible from the abstract interface alone, and any table it had written there would have been **fabricated**. Its refusal to fabricate is behaviour we commend; its formulas are **structure**, not **content**. The PI's ruling follows exactly this reasoning.

**What we therefore carry forward from the reply — structure only.** These five things survive into this letter:

| # | Carried forward | Where it lands in this letter |
|:-:|:--|:--|
| **S-1** | The **two-package decomposition** and the artifact labels `A-1` … `A-4` / `B-1` … `B-2` — a belief is unusable without a state space **and** a counterfactual kernel **and** a prior/likelihood; an occupancy table is unusable without the feasibility predicate that consumes it | §3 preamble |
| **S-2** | The **formulation skeleton** (finite enumerable `S`; `v(s,a)` with an explicit `NOT_IN_RANGE` handling rule; a prior/likelihood observation model with provenance; a per-cell coverage rule; a budget predicate with a stated binding rule) | §3, criterion by criterion |
| **S-3** | The **fixed CSV column schemas** of round 1 | §5 |
| **S-4** | The **20 acceptance criteria** of round 1, unchanged in substance | §3 |
| **S-5** | The **honest-partial-delivery convention**: for every criterion, either "holds" with the supporting computation, or "does not hold" with the failing item named | §3 preamble, §5, §6 |

**What we do not carry forward — no ungrounded number.** The reply also proposed **illustrative numeric choices** of its own (an example prior vector, example dispersion figures, an example multi-level occupancy scale). **None of them is adopted, none is transmitted to you, and none may be treated as a starting point that we endorse.** They are the reply's own construction choices, not quantities read off any material of ours; a number that is neither ours nor yours carries no provenance and cannot enter a delivery that we may recompute. ⛔ **0 numbers from the round-1 reply are quoted in this letter** — deliberately, so that you cannot mistake them for given inputs. **Build your own construction from the digest in §2.** If your independent construction happens to coincide with one of the reply's illustrative choices, that is coincidence and carries no weight either way.

**What this round changes.** Round 1 asked for a specification under an abstraction that was, by construction, insufficient to produce one. The three open items are now **resolved**: the material we withheld is now available **in desensitized form** (§2), and the `A1-6` / `A2-6` conflict is **resolved by a PI ruling** (§1). Round 2 is therefore a request for the **same two packages, now instantiated** — not a new question, and not a larger one.

⚠ **One thing has not changed: delivery is still not adoption.** See §0-2 and §6. Nothing in this letter promises that a compliant delivery will be used, that the measurement will succeed, or that any arm will be chosen.

---

## §1 The ruling on `OI-3` — Option 3A

**The ruling is Option 3A — blind external grounding + requesting-side verification of `A1-6` / `A2-6`.**

### §1-1 The ruling, verbatim, and what it resolves

**PI card answer** (card `ask_e98a5eab74bfc2e56a42613b`, 2026-10-24, register face `pi_rulings\_pi_card_answers_register_2026_10_24_v267.md` §1, row `oi3_conflict`, **verbatim**):

> 「**取 3A：盲式接地＋我方核（荐）**」 = *"**take 3A: blind grounding + verification on our side**"*

**The same register's reading of that answer** (§2-1, verbatim):

> 「**裁定**：**盲式外部接地**——受托方在**不见 `correct`／`value`** 之条件下构造；**`argmax ≠ correct` 之核对由我方**（持原值者）完成。」

**And the register records where the conflict came from** — it was **our** drafting inconsistency, not a defect of yours (§2-1, verbatim):

> 「⚠ **该冲突系我拟稿之不自洽**（C-1 与 A1-6/A2-6 并存）——本件登记为**我方之误**，非受托方之缺。」 = *"the conflict was an inconsistency in our own drafting (C-1 and A1-6/A2-6 coexisting) — recorded as our error, not as a gap of the commissioned party."*

📌 **What is therefore resolved:** Option 3B (desensitized **ordinal rank digest** — publishing the payoff rank of `a_1 … a_4` so that you could self-certify `A1-6` / `A2-6` numerically) is **not** adopted and **will not** be sent. No rank digest, no per-cell ordinal information, no answer key of any kind. The `OI-3` conflict is **closed by this ruling**; you do not need to answer it.

### §1-2 The four operating rules of Option 3A

These four rules **are** the commissioning instruction. They are binding, and they replace whatever round 1 said on the same point.

**(a) — Blind construction.**
You construct **without ever touching `correct` or `value`**. Not the reference key, not the payoff numbers, not their order, not their aggregate dispersion, not a hash of them, not a rank of them — **neither directly, nor indirectly, nor by any form you request or reconstruct.** The material you receive in §2 is desensitized precisely so that this condition can hold; §4 lists what remains withheld. This is not a courtesy to us: **the blind condition is what makes your construction evidence of grounding rather than an artefact of fitting.** A construction tuned against the key is worthless to us, and a delivery that shows signs of having seen the key is rejected (§6).

**(b) — Requesting-side verification.**
**We** hold `correct` and `value`. On receipt of your delivery, **we** independently compute, for every cell, whether `argmax_a E_{s∼π}[v(s,a)] ≠ correct` (`A1-6`) and whether `argmax_{b∈Feas} v(b) ≠ correct` (`A2-6`), and we report the result. **You are not asked to certify `A1-6` / `A2-6`, and you must not claim to have certified them.** Concretely, in your delivery: state for these two criteria **"not certifiable by the commissioned party under 3A — verification reserved to the requesting side"**, together with the per-cell computation **inputs** that let us perform the check ourselves. A self-certification of `A1-6` / `A2-6` is **not** what we need, and asserting one would be evidence that the blind condition was broken.

**(c) — Full reproducibility inputs and algorithm steps.**
Your delivery must carry **everything we need to recompute your construction independently** — i.e. all reproducible inputs and all algorithm steps, not just the resulting tables. Concretely, this means: every value's **derivation recipe and assumptions**; every formula in executable form (formula or pseudocode sufficient to recompute); every **parameter** (prior weights, likelihood form, state semantics, unit conversions, level scales, thresholds, the exact predicates of the feasibility rule); and the **provenance** of each external input (locator + retrieval timestamp, per round 1 §2.3). If we cannot recompute a number from what you delivered, that number does not count as delivered. This rule is what makes (b) possible — our verification is only as good as your reproduction material.

**(d) — Named gaps; ⛔ no zero-fill, no mean-fill.**
If, in the blind state, you **cannot determine** a particular cell — because the digest does not carry the grounding you would need, or because the semantic features are insufficient to separate the actions, or because your construction admits no non-degenerate assignment for that cell — then you must **name that cell and name what you lack**: the cell id, the specific quantity or feature that is missing, and the consequence for the criteria that depend on it. ⛔ **0 filling with zero.** ⛔ **0 filling with a mean, a median, a default, a placeholder, or any imputation.** ⛔ **0 silently dropping the cell.** ⛔ **0 reporting a filled-in cell as "obtained."** A named gap is a **usable** answer for us (it tells us what to measure or release next); a quietly filled cell is not, and it is a rejected delivery (§6). This rule is the direct continuation of the round-1 cross-cutting rule 2 (honest partial delivery beats a complete-looking one) and it is **not** a relaxation of it.

### §1-3 What changes for the twenty criteria, in one line each

Only two criteria change hands; the other eighteen keep their round-1 wording and their round-1 sense.

| Criterion | Round 1 | Round 2 |
|:--|:--|:--|
| `A1-6` | commissioned party certifies a priori, on its own delivered data | **requesting-side verification** — you deliver the computation inputs and the per-cell list; **we** compare against `correct` |
| `A2-6` | commissioned party certifies a priori, on its own delivered data | **requesting-side verification** — you deliver the computation inputs and the per-cell list; **we** compare against `correct` |
| `A1-1` … `A1-5`, `A1-7` … `A1-10`, `A2-1` … `A2-5`, `A2-7` … `A2-10` | as written | **unchanged in substance**; §3 states, criterion by criterion, what this round's delivery must contain for it to be checkable — now that the digest of §2 is in hand |

📌 **What this ruling does not do.** It does not relax any criterion, and it does not lower a threshold. `A1-6` and `A2-6` remain **exactly as hard**: at least 2 cells must show `argmax ≠ correct`. The change is **only** who performs the comparison — because under 3A you cannot, and under our old letter you would have had to see the key to do it, which would have made the criterion self-defeating. The `A1-6` ∧ `A1-7` and `A2-4` ∧ `A2-5` ∧ `A2-6` ∧ `A2-7` conjunctions of round 1 §3.3 rule 3 **still stand in full**.

---

## §2 The `OI-1` / `OI-2` files are ready

**The three desensitized pieces are ready and are attached to this commission as a separate file.** Below is the manifest only — **file names, byte counts and fingerprints**. ⛔ **The body of the digest is not copied into this letter**; you receive it as the attachment named in §2-1, and the attachment is the authoritative text.

### §2-1 The attachment — one carrier file, three pieces

The three pieces are carried in **one** file on our side, so the manifest is stated at two levels: the **carrier** (as it sits in our repository) and the **pieces** (measured section slices inside it).

| Item | Identifier | BYTES | SHA-12 | What it is |
|:--|:--|--:|:--|:--|
| **Carrier** | `results\work\process\_t5_desensitized_pack_2026_10_24.md` | **31,937** | **`90a5e34e1ae6`** | The whole desensitized pack as it sits in our repository (front matter + the three pieces + our internal section + our own byte self-certification) |
| **Piece 1** | `§OI-1a` — 20 cells → 17 scenarios, pairing table | **4,872** | **`8b36a8f2c2c5`** | The cell ↔ scenario mapping and the three shared-payoff-table cell pairs |
| **Piece 2** | `§OI-1b` — per-cell budget digest | **4,706** | **`63eb88aaf9fd`** | Per-cell budget type / value / unit / step limit / semantic note code, plus the aggregate budget statistics |
| **Piece 3** | `§OI-2` — the desensitized label digest: `§OI-2-0` separation declaration, `§OI-2-A` grounding payload, `§OI-2-B` calibration cell, `§OI-2-C` aggregate non-original facts, `§OI-2-E` the pack's own limits | **7,443** (the `§OI-2` block: `§OI-2-0` + `A` + `B` + `C`) + **1,911** (`§OI-2-E`) | **`f8e6da88965a`** (`§OI-2-0`+`A`+`B`+`C`) + **`98100f207996`** (`§OI-2-E`) | Scenario labels, the action-label set per scenario, one calibration cell, and the aggregate-layer facts that are not original values |
| **⚠ Not for you** | `§OI-2-D` | 3,543 | `43c11fad5ff1` | **Our internal section — excised from the attachment.** It carries aggregate `value` statistics and our own tool audit. It is marked 🔴 in the source and is **not** released. |

📌 **Fingerprints are of the slices as measured in our repository, 2026-10-24, by SHA-256 (first 12 hex digits) over the exact byte range of the section.** All measurements are reproducible by the method we state in §5-3.

### §2-2 The attachment you actually receive — the excised carrier

⚠ **The attachment is the carrier with `§OI-2-D` removed in full.** That section is ours, and it is not yours. Measured on the concatenation of the releasable sections in file order (`§OI-1a` + `§OI-1b` + `§OI-2-0`/`A`/`B`/`C` + `§OI-2-E`):

| Property | Measured value |
|:--|:--|
| BYTES | **18,932** |
| SHA-12 | **`593ce2b7cf43`** |
| Lines (LF) | **169** |
| CR / U+FFFD | **0 / 0** |

📌 **What is in the released concatenation, exactly:** `§OI-1a`, `§OI-1b`, `§OI-2-0` + `§OI-2-A` + `§OI-2-B` + `§OI-2-C`, `§OI-2-E`. 📌 **What is not:** `§OI-2-D` (internal, excised) **and** the carrier's own front matter (`§0` — our authorisation and material-verification narrative) and its closing byte self-certification section, which are ours and are not released.

📌 **Two honest notes on this number.** First, `593ce2b7cf43` is the fingerprint of the **concatenation**, not of a file that exists today — the excised file is cut at release time, by whoever the PI authorizes, and **its own fingerprint must be re-measured after the cut** (a real cut may differ from this concatenation in trailing-newline handling and in whether the front matter is re-added). We therefore give you **two** kinds of number deliberately: the **slice** fingerprints in §2-1, which are exact, and the **concatenation** fingerprint above, which is exact for the byte sequence we measured but is a **pre-cut** value. ⛔ **0 pre-declared fingerprint for a file not yet cut.** Second, the **absence** of `§OI-2-D` is not an oversight — please read `§OI-2-E` (§OI-2-E of the attachment), which is the source's own statement of its limits, and §4 below.

### §2-3 Which piece answers which open item and which criterion

This is the mapping you need; it is the direct answer to your round-1 open items `OI-1` and `OI-2`.

| Your open item | What you asked for | Which piece answers it | Which criteria it unlocks |
|:--|:--|:--|:--|
| **`OI-1`** | the 20-cell → 17-scenario **pairing table** | **Piece 1** (`§OI-1a`) | **`A1-10`**, **`A2-10`** (same-cell pairing) — your `cell_grouping.csv` now has an authoritative source and no longer has to be guessed; it also stabilises `A2-1`/`A2-3` per-cell bookkeeping |
| **`OI-1`** | the **desensitized budget digest** | **Piece 2** (`§OI-1b`) | **`A2-2`** (consistency with each cell's total constraint is now checkable cell by cell, against a stated cap, unit and step limit) + **`A2-10`** (same-cell pairing) + **`OQ-6`** (the granularity anchor is **necessary**, not optional — see the unit note in §3.2 `A2-2`) |
| **`OI-2`** | the **desensitized label digest** (`OQ-3`) | **Piece 3** (`§OI-2-A`) | the grounding route for **`A2-1`** (each occupancy value now has a `semantic_feature` and a `material_basis` instead of `none`) and for `B-1`'s non-restatement requirement; it also constrains the design of **`A1-2`** / **`A1-3`** — the source states that the state space and the counterfactual kernel **must** be designed against the label-overlap structure recorded in `§OI-2-C` |
| **`OI-2`** | the **calibration cell** (`OQ-6`, the granularity anchor) | **Piece 3** (`§OI-2-B`) | fixes the unit and granularity of `occupancy[t][a]` for every other cell — without it, "units" means something different in each party; the anchor's **occupancy column is deliberately left blank for you to fill** |
| — | the aggregate-layer facts (non-original) | **Piece 3** (`§OI-2-C`) | informs `A1-3` (integrand defined over the whole domain), `A2-7` (non-degeneracy of the occupancy field) and the §3-2 `A1-6`/`A2-6` verification the **requesting side** will run |

### §2-4 What the digest does **not** give you

Stated here so that nothing in the attachment surprises you later: the digest carries **no `correct` assignment, no `value` number, no ordered `options` tuple, and no prompt prose**. It carries the **labels** (scenario labels and action-label sets), the **budget parameters**, and a **small set of aggregate structural facts**. Read `§OI-2-0` and `§OI-2-E` in the attachment for the source's own precise wording on this point — including its explicit statement that publishing the action labels necessarily publishes the *literal text* of the reference key while still withholding **which action is the reference in which cell**, and that we do **not** claim the reference is unguessable.

⚠ **One instruction that travels with the attachment:** the action-label sets are presented in **sorted (lexicographic) order, deliberately not in the material's recorded order** — because in the recorded order the reference label would be positionally identifiable. **Do not attempt to reconstruct the recorded order, and do not treat the presented order as a natural order.** Any such reconstruction attempt is a rediscovery of `correct`, which voids the blind condition (§1-2 (a)) and is a rejected delivery (§6).

---

## §3 Acceptance criteria for this round

**The twenty criteria of round 1 stand unchanged in substance.** Each row below states what must hold and, in the third column, **what this round's delivery must contain for it to be checkable** — i.e. how the digest of §2 unblocks it, or what is newly expected of you.

⚠ **One structural note first.** The two packages are still what round 1 defined, and the reason for their shape is still the reason: a belief without a counterfactual kernel is a re-weighting of a single payoff table (the maximising action then does not move for any posterior), and an occupancy table without the feasibility predicate that consumes it would leave the predicate to be authored by us — and a predicate we author is not admissible input on our side. So:

- **Package A** — three artifacts, none omissible, and they must arrive **together**: **`A-1`** the state space `S` (finite, enumerated, per-element semantics and provenance); **`A-2`** the counterfactual payoff kernel `v(s,a)` (a registered numeric value for every pair, **or** an explicit `NOT_IN_RANGE` entry **with its handling rule**; ⛔ no blanks, no "TBD", no bare "n/a"); **`A-3`** the prior and likelihood with their provenance and the non-self-authorship disclaimer; **`A-4`** the per-cell coverage statement (which elements of `S` are live in that cell and by what rule).
- **Package B** — two artifacts, and they must arrive **in the same delivery**: **`B-1`** the per-cell × per-action occupancy table `occupancy[t][a]` (80 values, unit stated, a grounding basis per value); **`B-2`** the derivation rule "occupancy → `Feas`" (the exact predicate, including any combinatorial rule and how each cell's aggregate constraint binds and is reconciled).

### §3.1 Package A — criteria `A1-1` … `A1-10`

| ID | What must hold | This round's satisfaction condition — what your delivery must contain |
|:--|:--|:--|
| `A1-1` | **State space on record and enumerable** — `S` is finite; each element is individually identifiable in your document; the support of `π(·\|obs_t)` is a subset of `S`, checkable **per cell**. | Enumerate `S` with per-element semantics and provenance. ⚠ **Design against the overlap structure that Piece 3's `§OI-2-C` records**: across the 17 scenarios only 3 of the 136 scenario pairs share any action label at all (and they share exactly one label), while the remaining 133 pairs are fully disjoint. A state space **spanning scenarios** therefore leaves `v(s,a)` undefined for most actions in **14 of 17** scenarios. Either scope `S` per cell / per scenario, or state your `NOT_IN_RANGE` disposition for the pairs that do not exist. State per cell that the support of your posterior is a subset of `S`. |
| `A1-2` | **Normalisation** — per cell, `Σ_{s∈S} π(s\|obs_t) = 1` (numerical tolerance ≤ `1e-9`; **the tolerance value must be written in the document**). | Per-cell posterior sums in `likelihood_posterior.csv` (`cell_posterior_sum`, `tolerance`), and the tolerance **written out in the Markdown**. The per-cell observation features are now derivable: Piece 2 gives each cell's constraint family and semantic note code, so the likelihood's conditioning variable is **nameable per cell** rather than guessed. ⚠ The source states that the state space and the kernel design **must** be read against the overlap structure in `§OI-2-C` (see `A1-3`) — a posterior over a state space whose kernel is undefined on most actions cannot be normalised into something meaningful. |
| `A1-3` | **Integrand defined over the whole domain** — for **every** cell `t`, **every** `a ∈ options(t)` and **every** `s ∈ S`, `v(s,a)` has a registered value; a pair with no definition must be **explicitly recorded as "not in integrable range" with a disposition**; ⛔ no blanks. | The `counterfactual_payoff` table with `integrable_status` and `handling_note`; no row omitted. The label digest makes the domain **knowable**: the action-label set of each scenario is given, so which pairs do not exist is a fact you can state rather than a gap you must paper over. A pair that exists only in the realised table is still a pair you must address. |
| `A1-4` | **The expectation is computable, per cell and per action** — `E_{s∼π}[v(s,a)]` computable for **all** cells × **all** actions; no "not obtained" cell. | Either the computed matrix in the Markdown, or the rule plus inputs sufficient to recompute it (§1-2 (c)). A rule plus inputs is acceptable **only** if the inputs are delivered — a rule with undelivered inputs is a failed criterion. |
| `A1-5` | **Non-empty key** — the selected action set `K_t` is non-empty in **every** cell; **violating cells = 0**, reported cell by cell (⛔ "not obtained" may not be reported as "0 violations"). | The per-cell count of violations, cell by cell, for all 20 cells. |
| `A1-6` | **Structural guarantee of discriminative power (a priori)** — in the construction surface, **at least 2 cells** whose `argmax_a E_{s∼π}[v(s,a)]` differs from `correct`; if this fails, that construction may not enter measurement at all. | ⚠ **CHANGED — the requesting side verifies.** You do **not** certify this criterion. You deliver: (i) the per-cell `argmax_a E_{s∼π}[v(s,a)]` **as a list of action labels**, computed on your delivered data; (ii) every input needed for us to recompute that list independently; and (iii) the literal statement that **the criterion is not certifiable by the commissioned party under 3A, and the comparison against `correct` is reserved to the requesting side.** ⛔ **Do not assert that you have certified `A1-6`, and do not guess which action is `correct`** — an assertion here would itself be evidence that the blind condition was broken (§1-2 (a), §6). |
| `A1-7` | **Non-degeneracy, field by field** — for each input field of the construction: `n_distinct` / min / max / std; **any input field with `n_distinct ≤ 3` raises a degeneracy alarm**. | The field-level statistics for **every** input field. ⚠ Note that some fields of the *material* are degenerate by construction and must not be mistaken for degenerate **constructs**: the budget value has `n_distinct = 1` across all 20 cells and the step limit is constant — so a construction that merely re-expresses the budget as an input field trips the alarm mechanically. Your input fields must carry information the material does not already carry. |
| `A1-8` | **`std` reported in both readings** — population (denominator `n`) **and** sample (denominator `n−1`), side by side; ⛔ choosing one reading. | Both values, per field, side by side. |
| `A1-9` | **Attribution and disclaimer on file** — the delivery carries a **source** field and a **disclaimer** field, and the disclaimer that the belief is **not self-authored by the requesting side** is on file. | The `provenance` table including the disclaimer text. Plus, new this round: an explicit statement of your **blindness** — that you did not receive, and did not seek, the reference key or the realised payoffs. |
| `A1-10` | **Same-cell pairing** — your per-cell correspondence does **not** alter the cell ↔ scenario mapping: readings still land on the same 20 cells, the same seeds, the same `H` domain, with both readings of `H` carried side by side. | **Now checkable against an authority.** Your `cell_grouping.csv` must agree with **Piece 1** (`§OI-1a`) cell by cell — including the three cell pairs that share a payoff table. State that your cell numbering is stable and complete (20 cells), list the 3 seeds (**42 / 123 / 456**), and carry **both readings of the `H` domain** side by side, as round 1 required. |

### §3.2 Package B — criteria `A2-1` … `A2-10`

| ID | What must hold | This round's satisfaction condition — what your delivery must contain |
|:--|:--|:--|
| `A2-1` | **`Feas` domain / range on record** — every cell gives the **per-action selection or rejection** within `options(t)` **together with its reason item** (the occupancy value, or a semantic commitment). | The `occupancy_table` + `grounding_basis` tables, and the per-action outcome implied by your rule. **The grounding is now possible**: each action label is given (Piece 3, `§OI-2-A`), so `semantic_feature` and `material_basis` can carry a real basis instead of `none`. ⛔ The occupancy values must **not** be a monotone restatement of the payoff values — a table whose ordering is isomorphic to the payoff ordering carries no information beyond the payoff table and is **rejected on sight**. |
| `A2-2` | **Consistency with the cell's total constraint** — for each cell, the feasibility predicate over occupancy combinations is **checkable cell by cell** against that cell's stated total budget; **contradictory cells = 0**. | **Now checkable cell by cell**: Piece 2 (`§OI-1b`) states, for each of the 20 cells, the budget type, value, unit, the constraint phrase, the step limit and the semantic note code. Your `feasibility_rule` table must bind each rule to the budget it applies to, and the per-cell check must show **0 contradictory cells**. ⚠ Two facts from Piece 2 that bear directly on this criterion: **(i)** the budget **unit is not commensurable across scenarios** — four different unit kinds occur (units / days / rounds / hours) — so a rule that silently treats "units" as one dimension is wrong; **(ii)** the step limit is a **separate** dimension from the aggregate budget and your predicate must bind both where the cell states both. |
| `A2-3` | **`Feas` computable per cell** — `\|Feas(obs_t)\|` computable in **all** cells and reported cell by cell (also the gap against `\|options(t)\|`, which is 4). | Per-cell counts and the gap against 4, for all 20 cells. |
| `A2-4` | **Genuine narrowing** — the number of cells with `\|Feas(obs_t)\| < \|options(t)\|` is **≥ 1** (measured denominator = 4), **and** the number of cells in which `Feas` equals `options` is **0**. Both halves are required. | The two counts, **separately**. ⚠ The second half is the strict one: **every one of the 20 cells must exclude at least one action** (`1 ≤ \|Feas(obs_t)\| ≤ 3` throughout). If any cell keeps all 4 options, this criterion fails. |
| `A2-5` | **Non-empty key** — `K_t ≠ ∅` in **every** cell; violating cells = 0. | The per-cell count of violations. |
| `A2-6` | **Structural guarantee of discriminative power (a priori)** — **at least 2 cells** whose `argmax_{b∈Feas} v(b)` differs from `correct`. | ⚠ **CHANGED — the requesting side verifies.** You do **not** certify this criterion. You deliver: (i) the per-cell `argmax_{b∈Feas} v(b)` **as a list of action labels**; (ii) the occupancy table and the predicate in full, so that we can recompute the feasible set and the maximiser ourselves; and (iii) the literal statement that **the criterion is not certifiable by the commissioned party under 3A**. ⛔ Do not assert a certification; do not guess the reference key. |
| `A2-7` | **Non-degeneracy of the input field** — report `n_distinct` / min / max / std of the **occupancy quantity**; any input field with `n_distinct ≤ 3` raises a degeneracy alarm. | The statistics for the occupancy field. ⚠ As under `A1-7`: the budget value's own `n_distinct` is **1** across all 20 cells, so occupancy values derived by re-expressing the budget would trip the alarm mechanically. Your occupancy field must be a genuine consumption scale, distinct from the budget. |
| `A2-8` | ⚠ **Caliber item — open on our side.** Our working reading: the input field is the **numeric occupancy value**, and the binary feasibility indicator is a **derived readout**. ⛔ If the only input field were the binary indicator, its `n_distinct` = 2 ≤ 3 and the degeneracy gate would fire automatically ⇒ that form is not admissible without a caliber ruling. **Please deliver the numeric occupancy values.** | Unchanged and **still not yours to resolve**: deliver the **numeric** occupancy values; do not adjudicate the caliber, and do not substitute the binary indicator for the numeric field. |
| `A2-9` | ⚠ **`std` in both readings**, and the scope of the degeneracy gate is **not** prejudged on our side — population and sample side by side; ⛔ choosing one reading. | Unchanged: both values, per field, side by side. |
| `A2-10` | **Same-cell pairing** — the same 20 cells, the same seeds (42 / 123 / 456), the same `H` domain, both readings of `H` side by side. | The same statement as in `A1-10`, and the same check against **Piece 1**. |

### §3.3 The cross-cutting rules (carried over, with the one change the 3A ruling forces)

1. **Each criterion must be addressed.** For every identifier above, your delivery states either "holds" **with the supporting computation**, or "does not hold" **with the failing item named**. ⛔ No criterion left unaddressed; ⛔ "not applicable" must be justified in one line.
2. **Honest partial delivery is preferred over a complete-looking one.** If a criterion cannot be met, say which one and why. A delivery that states its own gap is **usable**; a delivery that quietly fails a criterion is not, and neither is one that manufactures a value in order to pass a gate. **A "built-to-pass" construction is a rejected delivery**, even when it passes every gate. ⚠ This is the rule behind §1-2 (d): a named gap is a usable answer; a filled-in gap is not.
3. **The hardest requirement, stated plainly.** `A1-6` and `A1-7` must be satisfiable **simultaneously** (and `A2-4`, `A2-5`, `A2-6`, `A2-7` likewise); `A1-3` and `A2-2` must hold outright. **If your construction cannot satisfy them together, tell us rather than bending one of them** — that answer is itself decision-relevant for the PI. ⚠ Under 3A, "satisfiable simultaneously" means the *construction* must permit the check to succeed; you are not asked to demonstrate that it does, and you may not claim it.
4. **Your certification is yours; our check is the arbiter.** We recompute every statistic from the delivered CSVs. ⛔ A claimed statistic that does not recompute is treated as a failed criterion. **Under 3A this rule extends to the two changed criteria**: we recompute the `argmax` lists and compare them against the reference key ourselves (§1-2 (b)).
5. **Nothing here is an adoption.** Passing every criterion makes your input *admissible*; it does not make it *chosen*. That decision belongs to the PI, on our report.

### §3.4 One thing we ask you **not** to do

⛔ **Do not report a criterion as satisfied by reference to the digest.** The digest is **desensitized and partly aggregate**; it is a **grounding substrate**, not a source of answers. In particular, the aggregate structural facts in Piece 3 (`§OI-2-C`) describe the **shape** of the reference key and the realised payoffs (cardinalities, distinctness counts, the cross-scenario overlap structure) without disclosing which action is the reference in which cell. Using those facts to *infer* the reference assignment would be **the blind condition failing**, not a use of the material — and it voids the delivery (§6).

---

## §4 What we will NOT provide

**The desensitization boundary is unchanged from round 1.** Round 2 widens *what we give you as grounding* (§2) and it narrows *who verifies* (§1) — it does **not** widen what we disclose. The boundary is `C-1` (no repository file, no row-level values, no prompt text) together with `OQ-3` (the label digest carries labels, not values), and it is maintained in full.

### §4-1 What we will NOT provide — the explicit list

| # | Not provided | Why, stated plainly |
|:-:|:--|:--|
| **N-1** | **The reference key `correct`** — not per cell, not aggregated, not hashed, not ranked, not in any form. | The blind condition (§1-2 (a)). Disclosing it would make `A1-6` / `A2-6` self-certifying and therefore meaningless as evidence of grounding. |
| **N-2** | **The realised payoff values `value`** — no per-cell numbers, no aggregate statistics of them, no dispersion figures, no ordering. | Same reason. Note that the aggregate `value` statistics exist in our internal section of the digest; that section is **excised** (§2-1). |
| **N-3** | **The ordinal rank digest** (Option 3B) — the payoff rank of `a_1 … a_4`, or the `correct` index. | The PI chose **3A**, not 3B (§1-1). Under 3A you construct blind; under 3B you would construct against a rank, which is the contamination 3A exists to avoid. |
| **N-4** | **The recorded order of the action labels** (the order in which the material wrote them). | The recorded order would make the reference key positionally identifiable. The digest therefore presents the labels **sorted**, and §2-4 tells you not to reconstruct the recorded order. |
| **N-5** | **The ordered `options` tuple for any seed** — i.e. the shuffled label order. | It varies with the seed and, combined with the reference key's constant position, forms a re-identification channel. |
| **N-6** | **The prose of the prompts** — the sentence frames, the question wording, the scenario ordinals. | `C-1`. The digest carries the **parameters** visible in the prompts (budget type, value, unit, step limit, semantic note code) and the **labels**; not the prose. |
| **N-7** | **Any repository file, code, harness, dataset, or row-level record** — including the file our digest was computed from. | `C-1`. ⛔ **0 private repository file is transmitted with this commission or its attachment.** The digest is a **derived, desensitized summary**, not an extract. |
| **N-8** | **Any credential** — API keys, tokens, passwords, private repository URLs, internal access paths, session or run identifiers, the internal roster. | `C-2`. ⛔ **0 credentials transmitted; 0 credentials handled.** |
| **N-9** | **Any personal information** — the name, contact detail or identifier of the PI, any team member, any reviewer, or any person represented in the material; no unpublished third-party data. | `C-3`. Refer to us by role ("the requesting side"). If your method needs a judgement about a person, describe the **semantic feature** you use instead. |
| **N-10** | **The internal section of the digest** (`§OI-2-D`) and our internal working papers. | Internal by its own routing. It is excised from the attachment (§2-1). |
| **N-11** | **Any of the illustrative numbers that appeared in the round-1 reply** (the example prior vector, the example dispersion figures, the example occupancy scale). | They were the reply's own construction choices, not quantities read off our material (§0-3). **0 of them is adopted and none is transmitted.** Build your own from the digest. |
| **N-12** | **Any calibration of the measurement** — the one-line calibration of the discriminative quantity, the choice between the two base surfaces, and any approval of a pre-registration. | `N-5` of round 1. Those are a **PI action surface**; a commission cannot discharge them, so they are not part of this commission. |
| **N-13** | **Any statement of which construction we will adopt**, any ranking of admissible forms, any arm recommendation from us. | `N-2` of round 1. That is the PI's call on our report. Your comparison of your own candidates is welcome as information; a recommendation is not a deliverable. |
| **N-14** | **A guarantee of use, or of success.** | `N-6` of round 1. We are buying an input, not an outcome. A compliant delivery still leaves the measurement to be run and judged. |
| **N-15** | **A second opinion sought outside this commission**, or any quotation of this letter or the attachment to anyone. | `C-5`, `C-9`. One-to-one channel; the commission and its abstract interface are internal research material. |

### §4-2 The honest edge of the digest — stated by us, not by you

Two properties of the attachment are ours to declare, and we declare them here rather than let you find them:

1. **The reference key's literal text necessarily appears in the attachment.** The digest publishes the action labels, and the reference key is one of the action labels — so its *literal* occurs in the file. What the digest withholds is the **assignment** (which label is the reference in which cell) and the **recorded order** that would expose it. 📌 **Our guarantee is "no assignment and no recorded order", not "the literal does not occur".** The source says the same in its own words; we read it as being in your interest that you hear this from us.
2. **Publishing labels raises the prior of guessing the reference key.** Semantics plus a scenario label can make the plausible reference guessable. We do **not** claim the reference is unguessable. We do claim that the **construction remains blind**, because the construction is what we adopt or reject — and the check that matters (`A1-6` / `A2-6`) is run by us, on our side, with the key. 📌 **This is an honest limit of the 3A route, not a defect of your delivery.**

### §4-3 The constraints of round 1 that remain in force

Everything in round 1 §4 still binds, with `C-1` read as restated in §4-1 and §2. In short, and unchanged:

- ⛔ **No action on our side, no access to our systems** (`C-4`): you have **no write access** to anything of ours; do not modify, move, rename, delete or create anything on our side; do not run, clone or invoke our harness or any experiment of ours; do not call any model or API on our behalf; do not read, scan or probe any local path, host or repository of ours; do not attempt to authenticate to anything of ours.
- ⛔ **Text-only delivery** (`C-6`): Markdown and CSV only; no executables, binaries, notebooks, macros or archives; no embedded objects; no links to a location holding our material; every CSV readable as plain UTF-8 text.
- ⛔ **Lawful sources only** (`C-8`): public literature, your own derivations, your own prior work; nothing behind access control; no long copyrighted text — short quotation with a locator; every source carries a locator and a retrieval timestamp.
- ⛔ **Before release, do nothing** (`C-10`): this is a **draft pending PI approval**; on our side ⛔ 0 sent / 0 pushed / 0 forwarded / 0 external contact; **you are required to take no action whatsoever** until the PI releases this letter, names the party and opens the channel.

### §4-4 What we do ask of you, in one line

Construct the two packages, blind, from the digest, with every input and algorithm step delivered so that we can recompute; name every gap you cannot fill (§1-2 (d)); and state the twenty criteria one by one, with the two changed ones handed to us rather than claimed.

---

## §5 Delivery format

### §5-1 File names and packaging

**Two packages, one per input (§3 preamble).** Each package = **one Markdown file** (the specification-facing narrative: definitions, formulas, provenance in prose, your own certification) **plus CSV sidecars** (one CSV per table, fixed names).

| Package | Markdown file | CSV sidecars (one per table) |
|:--|:--|:--|
| **A — belief** | `T5_input_A_belief_<Slug>_2026_10_24.md` | `T5_input_A_belief_<Slug>_2026_10_24_states.csv` · `…_cell_grouping.csv` · `…_counterfactual_payoff.csv` · `…_prior.csv` · `…_likelihood_posterior.csv` · `…_provenance.csv` |
| **B — occupancy** | `T5_input_B_occupancy_<Slug>_2026_10_24.md` | `T5_input_B_occupancy_<Slug>_2026_10_24_occupancy_table.csv` · `…_grounding_basis.csv` · `…_feasibility_rule.csv` |

`<Slug>` = a short ASCII handle of the commissioned party, **fixed by the PI at release**. 📌 The date in the file names is the **round-2 date (2026-10-24)**; round 1 used 2026-10-23. Cell ids are `t_01` … `t_20`; action ids are `a_1` … `a_4` (position within `options`); state ids are `s_01` … `s_k` — **your own** numbering, stable across all of your files. **The mapping from `cell_id` to our prompts and to our scenarios is ours, not yours** — it is now fixed for you by **Piece 1** (§2-3); you must not alter it, and your `cell_grouping` table must agree with it.

### §5-2 Column schemas (fixed — unchanged from round 1)

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

### §5-3 Encoding, and the self-attestation we require of every file

**Encoding — identical for every delivered file (Markdown and CSV alike):**

| Property | Required value |
|:--|:--|
| Character encoding | **UTF-8, without BOM** (no `EF BB BF` prefix) |
| Line endings | **LF only** (pure; ⛔ **0** CR bytes anywhere in the file) |
| Final byte | **`0x0A`** |
| Trailing blank lines | **0** — the file ends with a single newline, no extra empty lines |
| Strict UTF-8 decoding | must succeed with **no** replacement characters |

**CSV rules (as in round 1):** comma delimiter; **one** header row; fixed column order as listed above; decimal point; **no** thousands separators; **no empty cell anywhere** — use the literal token `NOT_IN_RANGE` where a value does not exist and explain its handling in the adjacent `handling_note` / `note` column; no formulas; no merged rows; ISO dates (`YYYY-MM-DD`) and ISO-8601 timestamps with an explicit offset.

**Markdown rules (as in round 1):** the section labels **`A-1` … `A-4`** and **`B-1` … `B-2`** must appear as headings, so we can check each artifact against its criterion one by one; every numeric table must also appear in the corresponding CSV (**the CSV is authoritative for values; the Markdown is authoritative for prose**).

**Provenance (as in round 1):** every external source cited with a **locator** (URL / DOI / document id) **and a retrieval timestamp**; every number that is your own derivation must have its **derivation recipe and assumptions** written down. ⛔ **No number without a stated origin.**

**Self-attestation — required in your reply text, outside the files.** For **every** file you deliver, report:

| # | Attestation item | Required |
|:-:|:--|:--|
| 1 | **BYTES** | the exact byte count of the file as delivered |
| 2 | **SHA-12** | the first 12 hex digits of the file's **SHA-256** (over the exact bytes delivered) |
| 3 | **LF count** | the number of LF bytes (= line count, given the file ends with a single `0x0A`) |
| 4 | **BOM** | `0` (no BOM) |
| 5 | **CR** | `0` (pure LF) |
| 6 | **U+FFFD count** | **must be 0** — a replacement character anywhere is a defect, not a warning |
| 7 | **Final byte** | `0x0A` |

⛔ **Do not write your own file's SHA-12 inside that file** — report it outside, in your reply text (round 1 §2.3).

### §5-4 Size discipline — the line-count cap

⛔ **Deliver only the files listed in §5-1, plus your reply text.** No unsolicited extra documents, no appendices of background reading, no "while I was at it" tables.

| Bound | Limit | Note |
|:--|:--|:--|
| **Lines per delivered file** | **≤ 2,000 LF** | Applies to **each** Markdown file and **each** CSV sidecar, individually |
| **Lines per package (Markdown + its CSVs together)** | **≤ 6,000 LF** | Applies to Package A and to Package B, each taken on its own |
| **Lines in the whole delivery** | **≤ 12,000 LF** | All 11 files together, plus your reply text |
| **Files** | **11** (2 Markdown + 9 CSV) | Plus your reply text |

📌 **Why the cap is stated this way.** A delivery that exceeds a bound is not rejected for its length — it is **returned unread**, because an over-long delivery cannot be checked against twenty criteria. If your construction genuinely needs more room than these bounds allow, the correct move is to say so in your reply (round 1 §4 `C-1`: state it as an open item; do not treat the request as a blocker you must solve by guessing) and to deliver **the subset that fits, with the remainder named as a gap** (§1-2 (d)). ⛔ **Compressing the content to fit is not a workaround** — a compressed delivery that drops a criterion is a failed criterion (§3.3 rule 1).

### §5-5 The delivery receipt — the format of your reply

Your reply is a **text** reply accompanying the files. It must contain, in this order:

**§R-1 · The file table** — one row per delivered file, with the seven attestation items of §5-3 as columns:

| file name | BYTES | SHA-12 | LF count | BOM | CR | U+FFFD | final byte |
|:--|--:|:--|--:|--:|--:|--:|:--:|
| `T5_input_A_belief_<Slug>_2026_10_24.md` | … | … | … | 0 | 0 | 0 | `0x0A` |

**§R-2 · The twenty-criterion statement** — one row per criterion `A1-1` … `A1-10`, `A2-1` … `A2-10`, each stating either "**holds**" with the supporting computation, or "**does not hold**" with the failing item named (round 1 §3.3 rule 1). For `A1-6` and `A2-6` the statement is the 3A form of §3: the per-cell `argmax` list as action labels, plus the literal reservation of the comparison against `correct` to the requesting side.

**§R-3 · The reproducibility bundle** — every input and algorithm step needed to recompute your construction (§1-2 (c)): parameters, formulas in executable form, unit conversions, level scales, thresholds, and the provenance of each external input.

**§R-4 · The named-gaps list** — every cell you could not determine, with what you lack and what it affects (§1-2 (d)). If there are none, say so explicitly; ⛔ **0 zero-fill, 0 mean-fill, 0 imputation.**

**§R-5 · The blind-construction attestation** — a statement that you did not receive and did not seek the reference key or the realised payoffs, that you did not attempt to reconstruct the recorded order of the action labels, and that your construction was not tuned against the key.

**§R-6 · The non-adoption acknowledgement** — the acknowledgment that **delivery is not adoption**: this delivery carries no claim of acceptance, and the choice among admissible forms belongs to the PI.

**§R-7 · Any open items** — anything you judge you need beyond this letter's material and the attachment, stated as an open item for the PI (round 1 §4 `C-1`). ⛔ Do not treat the request as a blocker you must solve by guessing.

### §5-6 The channel

One-to-one, through the channel the PI opens with this commission (`C-5`). ⛔ Do not forward this letter or the attachment; do not contact third parties about it; do not seek a second opinion outside the commission; do not quote either to anyone. 📌 **Until the PI releases this letter, names the party and opens the channel, you take no action whatsoever** (`C-10`).

---

## §6 Rejection criteria

**What follows is the rejection list. It is derived from round 1 §3.3 rule 2 and from §1-2 (d) of this letter; it is not a new standard introduced now.**

### §6-1 The governing rule, quoted

Round 1 §3.3 rule 2, verbatim:

> *"Honest partial delivery is preferred over a complete-looking one. If a criterion cannot be met, say which one and why — a delivery that states its own gap is **usable**; a delivery that quietly fails a criterion is not, and neither is one that manufactures a value in order to pass a gate. **A 'built-to-pass' construction is a rejected delivery**, even when it passes every gate."*

**"Built-to-pass" means: a value, a table, a rule or a certification whose purpose is to make a check come out the way the check wants to come out, rather than to carry information.** The test is not whether the numbers are wrong — a built-to-pass construction is usually numerically flawless. The test is **what the number is for**: if producing it required knowledge of, alignment with, or tuning against something it was not supposed to know, it is built-to-pass.

### §6-2 What will be rejected — the enumerated list

| # | A delivery is rejected if it … | Why it is the same defect |
|:-:|:--|:--|
| **R-1** | **manufactures a value to pass a gate** — fills a number chosen for its effect on a check rather than on its grounding. | Round 1 §3.3 rule 2, verbatim. The paradigm case is an occupancy or kernel value chosen so that a maximiser moves. |
| **R-2** | **fills a gap it could not fill, with zero, a mean, a median, a default, or any imputation** — or drops the cell silently, or reports a filled cell as "obtained". | §1-2 (d). ⛔ **0 zero-fill.** ⛔ **0 mean-fill.** A named gap is a **usable** answer; a filled one is a rejected delivery. |
| **R-3** | **asserts that `A1-6` or `A2-6` holds**, or otherwise claims to have compared its maximiser against the reference key. | Under 3A you cannot perform that comparison. An assertion here is evidence that the blind condition was broken (§1-2 (a)). The required form is the per-cell `argmax` list plus the explicit reservation of the comparison to the requesting side (§3.1 `A1-6`, §3.2 `A2-6`). |
| **R-4** | **reconstructs, guesses or infers the reference key** — including by restoring the **recorded order** of the action labels, by exploiting the aggregate facts in Piece 3 (`§OI-2-C`), or by using semantic plausibility as a proxy for the key and tuning against it. | The blind condition (§1-2 (a)). Tuning against an inferred key is contamination **even when the inference was indirect** — the construction is then fitted to the answer it was not supposed to know. |
| **R-5** | **returns an occupancy table that is a monotone restatement of the payoff values** — i.e. whose ordering is isomorphic to the payoff ordering. | Round 1 §2.2 `B-1`: such a table carries no information beyond the payoff table, and its apparent success is an artefact of the rule that generated it. **Rejected on sight.** |
| **R-6** | **returns the format illustration unchanged, or fills it with stand-in numbers that were invented to fill it.** | Round 1 §2.5, verbatim: *"returning this illustration unchanged, or filling it with stand-in numbers that were invented to fill it, is a rejected delivery — the same defect as a table built to pass a gate."* |
| **R-7** | **reports a criterion as satisfied without the computation that supports it**, or leaves a criterion unaddressed, or writes "not applicable" without a one-line justification. | Round 1 §3.3 rules 1 and 4: a claimed statistic that does not recompute is treated as a failed criterion. |
| **R-8** | **delivers a number whose origin is not stated** — no derivation recipe, no assumptions, no locator, no retrieval timestamp. | Round 1 §2.3: ⛔ no number without a stated origin. |
| **R-9** | **fails the mechanical format** — wrong file names, wrong column order, empty cells, a `NOT_IN_RANGE` token without its handling rule, a BOM, a CR byte, a non-`0x0A` final byte, a U+FFFD anywhere, or a file whose reported fingerprint does not match its bytes. | §5-3. A file whose attestation does not match its bytes is treated as an unattested delivery. |
| **R-10** | **exceeds the size bounds** of §5-4 (per file, per package, in total, or in file count). | §5-4: an over-long delivery cannot be checked against twenty criteria; it is returned unread. |
| **R-11** | **includes unsolicited extra documents**, or any executable, archive, notebook, macro, embedded object, or link to a location holding our material. | Round 1 §2.3 size discipline and `C-6` (text-only delivery). |
| **R-12** | **handles a credential, reads, scans or probes any path, host or repository of ours, modifies anything on our side, or calls any model or API on our behalf.** | `C-2`, `C-4`. |
| **R-13** | **contacts a third party about this commission, forwards it, or quotes it.** | `C-5`, `C-9`. |
| **R-14** | **states or implies that its delivery has been accepted, adopted or published** by us. | `C-7`. Delivery is not adoption (§0-2, §5-5 `§R-6`). |

### §6-3 What is **not** a reason for rejection — so that you do not over-correct

We state these explicitly, because a delivery that is too cautious is as useless to us as one that is too confident:

| # | **Not** a rejection reason | Why |
|:-:|:--|:--|
| **NR-1** | **A delivery that does not meet every criterion.** | A delivery that names its gaps is **usable** (§6-1). We would rather receive an honest partial delivery than a complete-looking one. What is rejected is the **quiet failure**, not the honest gap. |
| **NR-2** | **A "does not hold" verdict on a criterion, with the failing item named.** | That is a required answer, not a failure to deliver. |
| **NR-3** | **A construction that turns out not to be the one we would have chosen.** | Adoption is the PI's call (§0-2, §4-1 `N-13`). Your job is to supply an admissible input, not to match a private preference of ours. |
| **NR-4** | **A state space or kernel scoped differently from the one you might have guessed we wanted.** | The criteria are mechanical and in-register; your construction is yours. |
| **NR-5** | **A named gap in a cell, where you state what you lack.** | §1-2 (d). This is the **prescribed** behaviour under this ruling. |

### §6-4 The one-line version

**Build it blind, show your work, name your gaps, and let us do the checking.** Everything else in this letter is detail.
