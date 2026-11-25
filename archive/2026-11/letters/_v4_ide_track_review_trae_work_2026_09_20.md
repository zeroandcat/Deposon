# V4 IDE-Track Review — Trae Work

> **Attribution (2026-09-20, corrected).** Authored by **Trae Work**. Renamed from `_v4_ide_track_review_trae_code_2026_09_20.md` on 2026-09-20. No substantive content changed.

**Responding to:** `results/_v4_experiment_invitation_2026_09_20.md` (draft v0.1)
**Track scope (per §7.2):** Track 1 (distillation / mode-set) + Track 2 (reverse-distillation / reverse-attribution)
**Review lens:** reproducibility in the IDE environment
**Reviewer:** Trae Work (IDE-track recipient)
**Date:** 2026-09-20
**Boundary:** read-only review. No frozen asset modified. No key, endpoint, or secret in this file.

---

## §0 One-line verdict

Track 1 and Track 2 are **well-scoped but not yet IDE-reproducible**: the frozen inputs they depend on are not addressable as written, and both tracks rely on an embedding + collapse protocol that the invitation does not freeze. I verified the 5 KT SHA-12 placeholders (all 5 correct) and cleared the no-key check (0 hits); the remaining blockers are path-exactness and protocol-freezing, both fixable without touching any frozen asset.

## §1 Environment self-check (recomputable evidence)

| Check | Result |
|---|---|
| Invitation SHA-256 | `4E8C0EA57028AF400D8B8B1A29C92AC85A656E98BA20D50A462CB6808739BF84` |
| Invitation SHA-12 / size | `4E8C0EA57028` / 30,820 bytes |
| No-key scan (§7 铁律): `api_key` / `sk-` / `gpt-` / `claude-` / `ark-` | **0 / 0 / 0 / 0 / 0 hits → PASS** |
| §6 five KT SHA-12 vs actual frozen files | **all 5 verified** (see §1.1) |
| Actual `corpus/v20/by_model/` dirs | `coze`, `GLM_1`, `GLM_2`, `kimi`, `minimax` |

### 1.1 §6 SHA-12 verification (resolves §9 item 3, partially)

| Anchor | Invitation §6 | Actual file SHA-12 | Match |
|---|---|---|---|
| KT_A1 | `78b71d404366` | `78B71D404366` | ✓ |
| KT_B1 | `0410ca0fbdae` | `0410CA0FBDAE` | ✓ |
| KT_C1 | `59d8f56347d5` | `59D8F56347D5` | ✓ |
| KT_D0 | `cce8e9a1b00e` | `CCE8E9A1B00E` | ✓ |
| KT_ABC1_anchors | `03c6c01f3697` | `03C6C01F3697` | ✓ |

Verified read-only against `docs/V3X/KT_{A1,B1,C1,D0}_SPEC_V0.1.md` and `verifier/handoff/KT_ABC1_anchors_sha256_12.json`. The five placeholders in §6 are correct as written; the only residual is the §5.4 R5 SHA (still a placeholder).

## §2 Track 1 (mode-set) — IDE reproducibility blockers

- **B1 · path notation does not resolve (blocking).** §5.2 / §2.1 write `corpus/v20/by_model/{KIMI, GLM_1, GLM_2, coze, M3}`. The real directories are `{kimi, GLM_1, GLM_2, coze, minimax}` — `KIMI` is lowercase `kimi`, and `M3` is `minimax`. A literal glob from the invitation returns 2 of 5. **Fix:** restate as `corpus/v20/by_model/{kimi,GLM_1,GLM_2,coze,minimax}/`.
- **B2 · per-artifact filenames are non-uniform (blocking for a glob).** The five artifacts are `kimi/index_v2_2026_09_16.json`, `GLM_1/three_way_glm_slot_blind_test_2026_09_16.json`, `GLM_2/glm_artifact_v_2026_09_16.json`, `coze/coze_artifact_v_2026_09_16.json`, `minimax/artifact_v_2026_09_16.json`. There is no single filename pattern. **Fix:** freeze an explicit 5-path list (or a per-dir filename map) in the mode-set protocol.
- **B3 · "mode" and "high-density region" are undefined (blocking).** §2.1 step 2 defines stability by "appears in ≥3 of 5 artifacts, ≥3 of 21 pairs, ≥3 of 18 anchors" but never defines the mode estimator (density model, bandwidth, threshold). Two IDE runs with different defaults will produce different mode sets — the invitation's own reproducibility claim (§2.1 Output) does not hold without a frozen estimator. **Fix:** freeze the estimator as a pure function (same discipline as `_verify_15frozen.py`): input = frozen JSON, output = mode set, with all hyperparameters pinned.
- **B4 · the "21 caption-fingerprint pairs" are not addressable (blocking).** §5.5 cites 21 frozen pairs, but no artifact matching `*caption*fingerprint*` exists in the repo; the nearest is `corpus/v20/strip_captions_22.json` (22 captions). This is both a missing-path and a **21-vs-22 count discrepancy**. **Fix:** supply the exact 21-pair path and reconcile the count before Track 1 runs (otherwise the "≥3 of 21" rule is undefined).
- **B5 · GLM_1 artifact semantics unclear (non-blocking).** `GLM_1/three_way_glm_slot_blind_test_2026_09_16.json` is a blind-test report, not an `artifact_v` file like the others. Confirm whether it is a valid mode-set input or a substitute.

## §3 Track 2 (reverse-attribution) — IDE reproducibility blockers

- **B6 · symmetric KL is undefined on continuous embeddings (blocking).** §2.2 step 2 sets the primary metric to "symmetric KL on the per-cell embedding distributions." KL requires a common support and a density; on continuous per-cell embeddings it is only defined after freezing a discretization (binning) or a density estimator (KDE bandwidth). Without that, two IDE runs compute different divergences and the attribution table is not comparable. **Fix:** either freeze binning/KDE as a pure function, or switch the primary metric to one with a closed form on continuous points (e.g., sliced-Wasserstein), recording the choice.
- **B7 · Track 2 inherits Track 1's unfrozen embedding (cascading, blocking).** §2.2 step 1 says "the same per-cell embedding used in Track 1," but Track 1's embedding protocol is not frozen (B3). Reverse-attribution cannot be reproducible while its input protocol is not.
- **B8 · tie-breaking and attribution threshold unspecified (non-blocking).** §2.2 step 3 "attribute to the closest mode set" has no rule for near-ties or a minimum margin; add a stated tie-break + margin so the table is deterministic.

## §4 IDE-environment tooling finding (independent of Track 1/2)

The shipped self-check script `results/_v4_sha_selfcheck.ps1` **silently reports a false clean** when invoked as `powershell -File` on Windows PowerShell 5.1: its hardcoded Chinese path literal is parsed as ANSI, corrupting `本地仓根...` into mojibake, so `Get-FileHash` fails, `Get-Item` reports **0 bytes**, and all five no-key patterns report **0 hits** — the same numbers a genuinely clean file would produce. (Reproduced this run.) `_v4_regex_selfcheck.ps1` adds UTF-8 console guards but still carries the same Chinese literal. **Fix:** save the scripts as UTF-8 **with BOM**, or build paths from `$PSScriptRoot`, and fail loudly (non-zero exit) when the file cannot be read. This matters because these scripts are the V4 no-key / frozen-marker evidence gate.

## §5 Minimal fix list for the PI (IDE-track)

1. Restate §5.2 / §2.1 paths as `corpus/v20/by_model/{kimi,GLM_1,GLM_2,coze,minimax}/` and freeze the 5 explicit filenames (B1, B2).
2. Freeze the mode estimator + hyperparameters as a pure function, and the stability thresholds' rationale (B3).
3. Supply the exact 21-pair caption-fingerprint path and reconcile 21 vs 22 (B4).
4. Freeze the Track 2 divergence (binning/KDE or a closed-form metric) + tie-break rule (B6, B8).
5. Fix the self-check scripts' encoding so the no-key gate cannot false-pass (§4).
6. Optional: confirm GLM_1's blind-test JSON is a valid mode-set input (B5).

## §6 Boundary declaration

Read-only review. No frozen anchor, caption fingerprint, V2 artifact, or 5 锚 JSON was modified. No API key, secret, endpoint, or proprietary prompt appears in this file. The §6 SHA-12 verification was performed by reading the frozen files, not writing them.

*Trae Work — IDE-track review, 2026-09-20. Contributions acknowledged, not authorship.*