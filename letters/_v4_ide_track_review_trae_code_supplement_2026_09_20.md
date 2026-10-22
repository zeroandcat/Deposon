# V4 IDE-Track Review — Trae code · **Supplement** (factual-claims verification)

**Responding to:** `results/_v4_experiment_invitation_2026_09_20.md` (draft v0.1)
**Companion to:** `results/_v4_ide_track_review_trae_code_2026_09_20.md` (B1–B8, path/estimator/encoding layer)
**Scope of this supplement:** the **factual-claims layer** — the invitation's statements *about* the frozen V1–V3 asset stack. The companion review verified paths, SHA-12s, and the no-key gate; it did **not** verify the §5.3 verdict table, the §1.1 page count, the §2.4 embedding-frame availability, or the §5.4 R5 pointer.
**Reviewer:** Trae code (IDE-track recipient) · **Date:** 2026-09-20
**Boundary:** read-only. No frozen asset modified. No key, secret, or endpoint in this file. All claims below are machine-verified against disk (0 LLM).

---

## §0 Verdict

The invitation's **hash layer is sound** (§6 five KT SHA-12s verified correct; no-key gate clean) and its **reproducibility gaps are well-identified** by the companion review. But its **descriptive layer is materially inaccurate in five places**, three of which misstate the V3 terminal verdicts that V4's own framing depends on (§3.2 cross-track conjunction, §5.3 reuse). These are correctable in the text without touching any frozen asset — but they must be corrected before circulation, because recipients who check the verdict table against the frozen records will find the invitation's numbers do not exist.

**Severity: 3 × P0 (verdict misstatements), 2 × P1 (asset description), 1 × P2 (pointer).**

## §1 What the companion review covered vs. what this supplement adds

| Layer | Companion review | This supplement |
|---|---|---|
| Path resolution (by_model dirs, filenames) | ✅ B1, B2 | confirms |
| Mode estimator / thresholds freezing | ✅ B3 | — |
| Caption pair count (21 vs 22) | ✅ B4 | confirms |
| Track 2 metric (symmetric KL) | ✅ B6, B7 | — |
| Self-check script encoding | ✅ §4 | — |
| §6 KT SHA-12 correctness | ✅ §1.1 (5/5) | confirms |
| **§5.3 V3 verdict table** | ❌ not checked | **§2.1 below** |
| **§1.1 FTFB page count** | ❌ not checked | **§2.2** |
| **§2.4 embedding-frame availability** | ❌ not checked | **§2.3** |
| **§5.4 R5 pointer** | ⚠️ called it "placeholder" only | **§2.4** |
| **§5.2 V2 asset conflation** | ❌ not checked | **§2.5** |
| **09-20 archive move (asset paths shifted)** | ❌ not checked | **§3** |

## §2 Machine-verified findings

### 2.1 🔴 P0 — §5.3 verdict table: three of four P-verdicts do not match the frozen records

| Invitation §5.3 / §6 | Disk evidence | Verdict |
|---|---|---|
| **P-A PASS at 51/60** | `deposon_game_theory_eval_2026_09_10.json`: `"P-A": "PASS (2 models in [0.80, 0.90] equilibrium band; both 26/30 exact)"`. `deposon_v3_v7_summary_2026_09_11.json`: `"P-A": "GRAY (-1.7pp vs no-RAG, 5 embedding 全 NOISE)"` and `"26-cell 均衡稳定化 (2 model 0.867 PASS + V2 60 cells 86.67% 双主线)"`. **`51/60` does not appear in the game-theory record at all**; `51/60 = 85.0%` is `v2_phase1_60cells` `"v2_60cells_pass_rate"` — the **dpath/V2-phase1** number, not P-A. | ❌ **misattributed** (P-A is a 26-cell/2-model equilibrium-band PASS; the 51/60 belongs to a different asset) |
| **P-C FAIL_H0** | `d7_5anchor_60cells_9model_verdict_2026_09_18.json`: `"P-C_two_phase": "FAIL_H0 (幂律死)"` ✓ — **but** `v7_summary` records `"P-C": "STRONG_PASS (7 阶段全程 0 违反)"`. Two different layers (P-C main vs P-C_two_phase sub-experiment). | ⚠️ **correct but layer-ambiguous** — invitation cites one without noting the other |
| **P-E PARTIAL_PASS** | `game_theory_eval`: `"P-E": "GRAY (T-A anti-correlate; 3D T/R/A not a clean scattering field)"`. `v7_summary`: `"P-E": "NOISE (6 embedding 全 NOISE)"` and `"散射场 (GRAY, 3D 不干净…)"`. **`PARTIAL_PASS` appears nowhere for P-E.** | ❌ **wrong** (P-E is GRAY, not PARTIAL_PASS) |
| **P-F PASS at 45/45** | `d7_5anchor_60cells_9model_verdict_2026_09_18.json`: `"P-F_D_fix2_strict": "8+1+0 (PARTIAL_PASS, A channel timing 敏感)"` / `"P-F_D_fix2_loose": "8+1+0 (PARTIAL_PASS)"`. `skill_d_p_f_observer_result_2026_09_11.json` contains no `45/45`. The number **45** appears in the **P-K** GLM JSON audit (45 GLM JSONs), not P-F. | ❌ **wrong** (P-F D_fix2 is 8+1+0 PARTIAL_PASS; 45/45 has no on-disk basis) |

**Why this matters for V4.** §3.2 makes the V4 overall verdict a conjunction of track verdicts *"the same as V3.X"* — so V4 inherits V3's verdict semantics. If the invitation's own statement of the V3 verdicts is wrong in 3 of 4 rows, the template V4 claims to inherit is mis-stated at the point of inheritance. (P-A/P-C/P-E/P-F here also conflicts with the PI's own D7 letter, which recorded P-L v3 = P1+P3 FAIL + P2 PASS and the Adendum distribution 11+2+1+2+1=17.)

### 2.2 🟡 P1 — §1.1 "V1 — FTFB, arXiv-anonymous **12-page** double-blind"

Disk: the FTFB typeset PDF (v3) is **23 pages** (`/Type /Page` = 23 after FlateDecode stream decompression; 356,123 B, sha12 `2d9edc8c7303`), and the v2 defective build was 20 pages. **No 12-page FTFB artifact exists in the repo.** (§1.1 also says V4 "does not inherit V1's substantive results" — fine — but the page count is simply wrong.)

### 2.3 🔴 P0 — §2.4 "V4 reuses the three embedding frames": two of the three have **no artifact on disk**

| Frame | Disk evidence | Verdict |
|---|---|---|
| **Poincaré-distance** | `results/deposon_pg_v01_9m60c_2026_09_15.json` → `"poincare_curvature_c": 1.0`, `"spearman_rho_H_vs_E": 1.0` | ⚠️ exists, **but** |
| **Observer-effect** | Repo-wide scan (`*.py` / `*.json` / `*.md` under plugins, results, _designs): the token `observer_effect` appears **only in my own verification script**. No implementation, no artifact. | ❌ **absent** |
| **Bell-inequality** | Repo-wide scan: `CHSH` = 0 implementation hits; `inequality` hits are the invitation itself + an unrelated P-M attack-surface file. | ❌ **absent** |

**And the Poincaré frame's own status is scaffolding, not calibrated:** `P_G_3_BOSS_scaffolding` in the same JSON records `"status": "SCAFFOLDING (PRE-REGISTRATION, 等 D5 launch)"` with `"verdict_pending": true`, and `P_G_5_anchors_v01_real` still carries the **placeholder** values (`230b5caee415`, `dcbcf2b8d45f`, `2c1f572aa2bf`) alongside computed `sha12` — i.e. the P-G anchors were never promoted from seed-placeholder to file-real (consistent with my 2026-09-18 finding that the 5 P-G anchors are `sha256("P_G_V0_PLACEHOLDER_{id}_2026_09_15")[:12]` seeds). `next_steps` records the P-G V0.1 → V1 upgrade as **awaiting a D5 decision that has not been made**.

→ §2.4's "the curvature is the V2/V3 **calibrated** value. V4 reuses the value; V4 does not recalibrate" **overstates**: there is one algorithm-defined constant (`Mobius(c=1)`) on a scaffolding tier, and two of the three named frames have no artifact to reuse. Track 1 cannot "reuse" what does not exist.

### 2.4 🟡 P1 — §5.4 "V3 终稿 R5 (frozen)" is a dangling pointer

No file whose name contains `R5` exists anywhere in `docs/`, `results/`, or `deposon_team/`; the V3 final report on disk is `docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` (**V7**, not R5) and its text contains no `R5`. The invitation asks the PI to "confirm the SHA-12 from the V3 终稿 R5 manifest" — there is no R5 manifest to confirm against.

### 2.5 🟡 P1 — §5.2 conflates two distinct frozen assets

§5.2 heads the section "V2 — deposon v2, **nine-backbone × 60-cell grid** (frozen)" and then lists "**five** frozen artifacts at `corpus/v20/by_model/…`". These are two different assets: the 9-backbone × 60-cell aggregate is `results/deposon_v3_physical_opt_60cells_2026_09_11.json` (sha12 `c659695aa23c`), whereas the five `by_model/` artifacts are the **P-K cross-subject blind-test** set (5 producers). V4's Track 1 reads the five by_model artifacts, so the mislabel is not fatal — but "nine-backbone × 60-cell grid" should not be the heading of the five-artifact list.

### 2.6 ✅ Confirmed correct (so the PI need not re-check these)

- **§6 five KT SHA-12s** — all 5 verified byte-exact (`78b71d404366` / `0410ca0fbdae` / `59d8f56347d5` / `cce8e9a1b00e` / `03c6c01f3697`). §9 item 3 is resolved for the anchors.
- **§8.1 / §11 skill provenance** — `sha256-tree-v1-611965fcb…` is a real Mavis plugin-cache tree containing **9** skills (`peer-review`, `scientific-writing`, `experimental-design`, `hypothesis-generation`, `scholar-evaluation`, `scientific-brainstorming`, `statistical-analysis`, `statistical-power`, `uncertainty-and-units`). Citing `scientific-writing` from the same tree that previously supplied `peer-review` is legitimate — the tree hash is the package hash, not the skill hash. **No discrepancy.**
- **No-key gate** — clean (independently reproduced by the companion review).

## §3 Asset-path impact of the 2026-09-20 archive move

`results/_archive_2026_09_20/` (created 2026-09-20) now holds **100+ files**, including the entire FTFB three-piece set (`fiction_that_feeds_back.{pdf,tex,md}` + `戴夫_FTFB双审包简报v3…`) and the prior V3-round letters/audits. Consequences for V4:

1. **§5.1's FTFB references** must point at the archived location, not `results/…` root.
2. I re-verified that the move was **content-preserving**: every 2026-09-18 fix artifact I produced is SHA-**PRESERVED** in the archive (e.g. `_deposon_v2scripts_reverify_worker` `18984b04c45e`, `_d05_verify_sha` `0b7e50a8a036`, `_fix_d05_rescue` `2c2cc3ff542a`, `_coze_paper_v1_双审报告` `c3de25e6df57`, `_letter_to_glm_ftfb_deep_revision` `3de722dc9e39`, `戴夫_FTFB双审包简报v3` `6952b3b02b96`). The archive did not corrupt any of them.
3. **Any D1 re-verification** of "the frozen inputs are untouched" should state that a repo-level archive move occurred on 09-20, so a recipient comparing paths (not hashes) does not misread the move as a modification.

## §4 Supplement fix list for the PI (factual layer)

| # | Sev | Fix |
|---|---|---|
| F1 | P0 | §5.3: correct the verdict table against the frozen records — P-A → 26-cell/2-model equilibrium-band PASS (and note `v7_summary` grades it GRAY); P-E → **GRAY**, not PARTIAL_PASS; P-F → **8+1+0 PARTIAL_PASS (D_fix2)**, not 45/45. Remove `51/60` from P-A (it is the V2-phase1 dpath number). |
| F2 | P0 | §2.4: either (a) supply the artifacts for the observer-effect and Bell-inequality frames, or (b) restate the section as "one frame (Poincaré, scaffolding tier, `c=1`) is available; the other two are aspirational". Do not claim V4 "reuses" frames that have no implementation. |
| F3 | P1 | §1.1: correct "12-page" → 23-page (v3 build). |
| F4 | P1 | §5.4: either locate the R5 artifact or drop the "V3 终稿 R5 (frozen)" row (the on-disk V3 final is V7). |
| F5 | P1 | §5.2: separate the "9-backbone × 60-cell aggregate" (`deposon_v3_physical_opt_60cells…`) from the "five `by_model/` blind-test artifacts"; do not use the former as the heading of the latter. |
| F6 | P2 | §5.1 / §3: repoint FTFB references to `results/_archive_2026_09_20/`; add a one-line note that a content-preserving repo archive move occurred on 2026-09-20. |

*(The companion review's B1–B8 — paths, mode estimator, KL metric, caption 21-vs-22, self-check encoding — remain open and are not repeated here.)*

## §5 Boundary declaration

Read-only. No frozen anchor, caption fingerprint, V2 artifact, or 5 锚 JSON was modified; every SHA-12 above was computed by **reading** the files. No API key, secret, endpoint, or proprietary prompt appears in this file. All findings are reproducible by the PI with a plain `sha256` + `json.loads` + `grep` pass over the paths cited.

*Trae code — V4 IDE-track review supplement, 2026-09-20. Contributions acknowledged, not authorship.*


<!-- appended-note:2026-09-30 skill 引用面复核（PI 派工第④项 · 0 删改历史字面） -->

> **附注（2026-09-30 追加 · 非原件内容）**
> 本件原引用字面**逐字保留、0 删改**；本附注**只增不改**。
>
> - **原引用面**：L74（出现 2 处）· §8.1/§11 skill provenance：sha256-tree-v1-611965fcb… + 9-skill 明细
> - **2026-09-30 只读复核**：原引用字面**2026-09-30 仍成立**（写死路径逐字在位、树哈希同目录名、关键 `SKILL.md` SHA-12 对得上）⇒ **无过期值可改**，故仅追加注记、**不就地更新**
> - **当前三段式锚**（plugin:skill + 树哈希前 12 + SKILL.md SHA-12 + 定位方式）：树 ``611965fcb620`` + ``peer-review`` / ``SKILL.md`` SHA-12 ``fed0262d707a`` / 11,639 B
> - **对外件口径**：本件为**已对外发出件**。路径与树哈希写死之陈旧风险（起因件建议 A1）**仍成立**——建议后续对外件改记 plugin:skill 名，路径与哈希只在内部登记件记实测值。本附注**仅供内部对账，未随原件对外发出**。
> - **树哈希口径**：树哈希 = **打包哈希**，**不是** SKILL.md 哈希；两者不可混用（起因件建议 A4）。
> - **执行件**：`results/_skill_reference_update_and_user_surface_survey_2026_09_30.md` · 出件 **worker**（本棒）· **0 删改本件任何既有字节**