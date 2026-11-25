# V4 Invitation — Formal Acceptance (Trae code) · v1.1

**To:** Principal Investigator, deposon V4 (via the deposon IDE-track channel)
**Re:** `results/_v4_experiment_invitation_2026_09_20.md` (draft v0.1)
**From:** Trae code (IDE-track recipient)
**Date:** 2026-09-20
**Revision:** v1.1 — supersedes v1.0 (`10bbf6c96200`); adds the factual-layer blockers F1–F6 from the companion supplement
**Boundary:** read-only. No frozen asset modified. No key, secret, or endpoint in this file.

---

## §1 Acceptance

Trae code **accepts** the V4 experiment-design invitation.

- **Assigned tracks (§7.2):** Track 1 (distillation / mode-set) + Track 2 (reverse-distillation / reverse-attribution).
- **Assigned lens (§7.2):** IDE-track review, with attention to reproducibility in the IDE environment.
- **Output form (§7.4):** short Markdown / inline IDE comment on the deposon IDE-track channel.

Acceptance is given in principle and is **unconditional as to participation**. It takes effect for the D1/D3/D5 cadence once the invitation reaches "circulation-ready" (§8.3); the current draft is explicitly marked "not circulation-ready" (§12).

## §2 Scope acknowledged

**Asked of Trae code.** IDE-track review of (a) the V4 mode-set table and (b) the reverse-attribution procedure, with a reproducibility focus.

**Not asked (§7.3) — understood and accepted.**

- Not asked to define the anti-distillation mechanism (§2.3) — that is the PI's call; I will comment on the placeholder only.
- Not asked to modify any frozen asset.
- Not asked to run new experiments on the frozen stack.
- Not asked to commit to authorship.

## §3 Boundary commitments

- **Frozen assets:** read-only. I will not modify any of the 18 frozen anchors, caption fingerprints, 5 V2 artifacts, 5 锚 JSON, plugin specs, verifier subtree, or Trae-IDE cache (§1.5, §5.7). Verified at acceptance time: 14/14 spot-checked frozen SHAs unchanged.
- **No-key:** no API key, secret, endpoint, or proprietary prompt will appear in any Trae code output (§1.5). Self-scan of this round's outputs: 0 hits across 7 patterns.
- **Cadence:** 〔IM〕-only; ~5–10 minutes per checkpoint; D1 / D3 / D5 (§2.6, §7.1). I will not push, fetch, or auto-message.
- **Authorship:** AI is not an author. My contributions are acknowledged, not authorship (§8.1). CRediT assignment is at the PI's discretion.

## §4 Blockers submitted with acceptance (reproducibility gates, not objections)

Two review artifacts are on file; the blockers below are their union.

- Companion review: `results/_v4_ide_track_review_trae_code_2026_09_20.md` — **B1–B8** (path / estimator / metric / encoding layer)
- Companion supplement: `results/_v4_ide_track_review_trae_code_supplement_2026_09_20.md` — **F1–F6** (factual-claims layer)

### 4.1 B-series (reproducibility layer)

| # | Blocker |
|---|---|
| B1 | §5.2/§2.1 write `{KIMI, GLM_1, GLM_2, coze, M3}`; real dirs are `{kimi, GLM_1, GLM_2, coze, minimax}` |
| B2 | No single glob resolves the 5 V2 artifacts (non-uniform filenames) |
| B3 | "mode" / "high-density region" and the "≥3 of 5 / 3 of 21 / 3 of 18" rule are not frozen as a pure function |
| B4 | "21 caption-fingerprint pairs" not addressable; nearest artifact is `corpus/v20/strip_captions_22.json` (**22** items) |
| B5 | `GLM_1/three_way_glm_slot_blind_test…json` is a blind-test report, not an `artifact_v` file — confirm it is a valid mode-set input |
| B6 | §2.2 symmetric KL is undefined on continuous embeddings without a frozen binning/KDE |
| B7 | Track 2 cascades from Track 1's unfrozen embedding |
| B8 | §2.2 attribution tie-break and minimum margin unspecified |
| §4 | `_v4_sha_selfcheck.ps1` / `_v4_regex_selfcheck.ps1` can report a **false clean** under Windows PowerShell 5.1 (Chinese path literal parsed as ANSI → 0-byte read → 0 hits) |

### 4.2 F-series (factual-claims layer — new in v1.1)

| # | Sev | Blocker |
|---|---|---|
| F1 | P0 | §5.3 verdict table misstates 3 of 4 rows: **P-A** is a 26-cell / 2-model equilibrium-band PASS (`51/60 = 85.0%` is the V2-phase1 dpath number, not P-A); **P-E** is **GRAY**, not PARTIAL_PASS; **P-F** is **8+1+0 PARTIAL_PASS (D_fix2)**, not `45/45` (45 appears only in the P-K GLM JSON audit) |
| F2 | P0 | §2.4 claims V4 "reuses the three embedding frames": **observer-effect and Bell-inequality have no artifact on disk**; the Poincaré frame exists only on a **scaffolding** tier (`P_G_3_BOSS…` status "SCAFFOLDING…等 D5 launch", `verdict_pending: true`, P-G anchors still carrying placeholder values) — "calibrated value" overstates |
| F3 | P1 | §1.1 "FTFB, arXiv-anonymous **12-page**" — the typeset FTFB is **23 pages** (v3; v2 was 20); no 12-page artifact exists |
| F4 | P1 | §5.4 "V3 终稿 **R5** (frozen)" is a **dangling pointer** — no R5 file exists; the on-disk V3 final is **V7** |
| F5 | P1 | §5.2 uses "nine-backbone × 60-cell grid" as the heading of the **five `by_model/` blind-test artifacts** — two distinct assets conflated |
| F6 | P2 | §5.1 FTFB references predate the content-preserving 2026-09-20 archive move to `results/_archive_2026_09_20/` |

**Verified correct at acceptance time (no PI re-check needed):** §6 five KT SHA-12s (5/5 byte-exact); §8.1/§11 skill provenance (`sha256-tree-v1-611965fcb…` is a real 9-skill tree containing both `peer-review` and `scientific-writing`); no-key gate (0 hits, independently reproduced). **§9 item 3 is therefore resolved for the five anchors.**

## §5 What Trae code will deliver

| Checkpoint | Deliverable |
|---|---|
| **D1** | Flag any issue that would invalidate Track 1 or Track 2 (incl. re-check of B1–B8 and F1–F6 after the PI's fixes). |
| **D3** | Run the reverse-attribution procedure on a held-out candidate; report the divergence value and any reproducibility failure. |
| **D5** | Return PASS / FAIL / PARTIAL / GRAY on Track 1 and Track 2 (and comment on the Track 3 placeholder only, not define it). |

## §6 Declaration

This acceptance modifies no frozen asset and transmits no key, secret, endpoint, or proprietary content. All SHA-12s cited above were computed by reading the files. Trae code participates as an acknowledged contributor, not an author.

*Trae code — accepting the V4 invitation (v1.1), 2026-09-20.*


<!-- appended-note:2026-09-30 skill 引用面复核（PI 派工第④项 · 0 删改历史字面） -->

> **附注（2026-09-30 追加 · 非原件内容）**
> 本件原引用字面**逐字保留、0 删改**；本附注**只增不改**。
>
> - **原引用面**：L72（出现 1 处）· §8.1/§11 skill provenance：sha256-tree-v1-61196…（验收口径「树哈希≠skill 哈希」）
> - **2026-09-30 只读复核**：原引用字面**2026-09-30 仍成立**（写死路径逐字在位、树哈希同目录名、关键 `SKILL.md` SHA-12 对得上）⇒ **无过期值可改**，故仅追加注记、**不就地更新**
> - **当前三段式锚**（plugin:skill + 树哈希前 12 + SKILL.md SHA-12 + 定位方式）：树 ``611965fcb620`` 全值 ``611965fcb6208a5dbeb28d594ad7ca0f8b1f8fd62fc33c189e56a50e49db19cb``（本棒实测同值）
> - **对外件口径**：本件为**已对外发出件**。路径与树哈希写死之陈旧风险（起因件建议 A1）**仍成立**——建议后续对外件改记 plugin:skill 名，路径与哈希只在内部登记件记实测值。本附注**仅供内部对账，未随原件对外发出**。
> - **树哈希口径**：树哈希 = **打包哈希**，**不是** SKILL.md 哈希；两者不可混用（起因件建议 A4）。
> - **执行件**：`results/_skill_reference_update_and_user_surface_survey_2026_09_30.md` · 出件 **worker**（本棒）· **0 删改本件任何既有字节**