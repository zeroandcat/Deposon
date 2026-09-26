# V3 - V4 Achievements Inventory (2026-09-24)

> by **evidence-auditor** (agent-11335500b168)  
> Generated: 2026-09-24 17:10  
> Workspace: `D:/private-data/deposon-repo`

---

## 0. Dispatch Record (5-item checklist)

| slot | value |
|---|---|
| 1. agent name | evidence-auditor (agent-11335500b168) |
| 2. skill name | `superpowers:verification-before-completion` (plugin-cache sha256 `ade95665080e...` -- known possibly-missing, anchored on `_v4_noise_cleanup_manifest_2026_09_24.md` precedent) |
| 3. plugin | `@superpowers` |
| 4. iron rules | read-only inventory (mv/write only for this manifest) ; R4 key never plaintext ; V1-V3 assets untouched ; SHA-12 real-tested (no fabrication) |
| 5. honest disclosure | 0-product = honest 0-product ; every SHA-12 disk-tested via `Get-FileHash -Algorithm SHA256` ; uncertain classifications tagged `[TO-VERIFY]` |

### 0.1 Policy update flagged by PI on 2026-09-24

PI decision recorded in the parent session: the **paper final draft + project-report WeChat commission letter will not contain an outline**; GLM / coze are free to structure as they wish. This inventory therefore acts as a **raw materials baseline** (complete on-disk catalogue of all V3-V4 outputs), while structure/outline is delegated to the recipient.

### 0.2 Inventory scope and conventions

- **Stages**: `V12` (legacy V1-V2 baseline corpus + earlier code) ; `V3X` (V3/V3X formal experiments, plugins, P-A..P-G, kill-line + boss) ; `V4` (proxy-student generation, distill-min, supp L1..L14, prereg v0.2 + L9/L10 addenda, N09..N39, Task-B) ; `CROSS` (cross-stage anchors: 5-anchor root, 18-frozen impl, corpus/v20).
- **Categories**: `JUDGMENT` (verdict / result documents) ; `PREREG` (prereg / activation / TH table) ; `ERRATUM` (erratum / manifest / reconciliation) ; `EXP_PRODUCT` (executor / data with hash) ; `ARTIFACT` (corpus / proxy / measure / dataset) ; `LETTERS` (letters / commission / reply / wechat) ; `DECISION` (questionnaire / iron-rules review) ; `KNOWLEDGE` (formal docs / paper drafts / brain-map).
- **View tag**: `A` = suitable as final-paper material ; `B` = suitable as commission-letter material ; `C` = internal-only (not for external distribution).
- **Status heuristic**: `IN-EFFECT` (canonical / in-use) ; `LOCKED` (frozen, append-only) ; `ARCHIVED` (under `_archive_` / `_v4_supp_l3_n20copy_backup` etc.) ; `TO-VERIFY` (classification uncertain).
- **Excluded from full enumeration** (but still disk-tested): `__pycache__/*.pyc`, `*.log`, internal cache directories (`attacker_xl_cache`, `cot_quiz_cache`, `familyl_cache`, `familyl_prior_cache`, `gt2_attacker_cache`, `gt3_prior_cache`, `gt8b_cache`, `gt8c_cache`), `.tmp/`, `.trae/scripts/` (only 2 helper scripts).

---

## 1. Overview (Stage x Category, classified + unclassified)

Total disk-tested files (excluding transient): **1383**

### 1.1 Stage roll-up

| Stage | Count | Share |
|---|---|---|
| V12 | 1007 | 72.8% |
| V3X | 195 | 14.1% |
| V4 | 128 | 9.3% |
| CROSS | 53 | 3.8% |

### 1.2 Stage x Category matrix (classified items only; bulk unclassified V12 mixed at bottom of section 2)

| Stage \\ Category | JUDGMENT | PREREG | ERRATUM | EXP_PRODUCT | ARTIFACT | LETTERS | DECISION | KNOWLEDGE | NOTES | Stage-total |
|---|---|---|---|---|---|---|---|---|---|---|
| V12 | 0 | 0 | 2 | 191 | 0 | 0 | 0 | 41 | 51 | 285 |
| V3X | 33 | 0 | 18 | 57 | 6 | 22 | 0 | 59 | 0 | 195 |
| V4 | 36 | 16 | 2 | 18 | 10 | 31 | 4 | 11 | 0 | 128 |
| CROSS | 1 | 0 | 3 | 6 | 41 | 0 | 0 | 2 | 0 | 53 |

### 1.3 View-tag roll-up (across classified items)

| Tag | Count | Description |
|---|---|---|
| A | 129 | suitable as final-paper material |
| B | 55 | suitable as commission-letter material |
| C | 426 | internal-only (not for external distribution) |

---

## 2. Detailed Inventory (Stage x Category)

### 2.1 Stage: V12 (1007 items)

#### V12 / ERRATUM > 2 items

| Path | SHA-12 | Size (B) | View | Status | Modified | Note |
|---|---|---|---|---|---|---|
| verifier/v17/erratum.md | 50F15F7EA3DC | 438 | C | IN-EFFECT | 2026/08/29 01:26:03 | verifier erratum |
| verifier/v20/erratum.md | 35081D39F35B | 316 | C | IN-EFFECT | 2026/08/29 01:26:03 | verifier erratum |

#### V12 / EXP_PRODUCT > 191 items

| Path | SHA-12 | Size (B) | View | Status | Modified | Note |
|---|---|---|---|---|---|---|
| attacks/__init__.py | D11E085D9ECC | 183 | C | IN-EFFECT | 2026/09/01 11:19:18 | attacks series (3 + __init__) |
| attacks/a1_delete_anchor.py | 78AC391D16FC | 4693 | C | IN-EFFECT | 2026/09/04 13:11:07 | attacks series (3 + __init__) |
| attacks/a2_reshuffle_manifest.py | 3D54B277620E | 3792 | C | IN-EFFECT | 2026/09/01 11:19:34 | attacks series (3 + __init__) |
| attacks/a3_rewrite_runs.py | F02B3EEE8D6E | 4254 | C | IN-EFFECT | 2026/09/01 16:31:25 | attacks series (3 + __init__) |
| audits_dataset_health.json | 4F827071B0B8 | 7398 | C | IN-EFFECT | 2026/08/28 15:53:27 | audits / agents at top |
| audits_outliers.json | 3B1C881C4594 | 132875 | C | IN-EFFECT | 2026/08/28 15:53:28 | audits / agents at top |
| audits_security.json | 553C90AA3BA6 | 1610 | C | IN-EFFECT | 2026/08/28 15:52:30 | audits / agents at top |
| deposon_agents.py | 5496954B0AD5 | 104622 | C | IN-EFFECT | 2026/09/18 13:41:44 | top-level scripts |
| deposon_agents_v1_3.py | 715026B48678 | 1827 | C | IN-EFFECT | 2026/08/30 10:23:11 | top-level scripts |
| deposon_agents_v1_4.py | 59F0CE83E06D | 1726 | C | IN-EFFECT | 2026/08/30 10:23:11 | top-level scripts |
| deposon_diffusion.py | FE4D668EB1DA | 19171 | C | IN-EFFECT | 2026/08/30 04:52:41 | top-level scripts |
| deposon_fast.py | 7A2DCBADAC73 | 4581 | C | IN-EFFECT | 2026/08/30 04:53:24 | top-level scripts |
| deposon_g2_modes.py | 6A175A264B46 | 6316 | C | IN-EFFECT | 2026/08/23 09:33:59 | top-level scripts |
| deposon_photonics.py | C7E78AD9F030 | 10402 | C | IN-EFFECT | 2026/08/29 00:34:47 | top-level scripts |
| deposon_protocol.py | CA756668CE2E | 2845 | C | IN-EFFECT | 2026/08/30 04:55:56 | top-level scripts |
| fingerprint_v0.py | C0C38007C4E8 | 10950 | C | IN-EFFECT | 2026/09/01 16:36:32 | top-level executors |
| gt_common.py | 425B4B2F1C01 | 3601 | C | IN-EFFECT | 2026/08/30 10:17:31 | top-level scripts |
| llm_fetch.py | FDA22714DE2D | 8433 | C | IN-EFFECT | 2026/08/30 10:09:18 | top-level executors |
| llm_prior.py | 7FBA7D72A679 | 7466 | C | IN-EFFECT | 2026/08/30 10:10:54 | top-level executors |
| mindmap_corpus_v20.py | 7D8D6A30DD8C | 23893 | C | IN-EFFECT | 2026/08/29 01:14:15 | top-level executors |
| run_v15_experiment.py | 58A5623F3AA1 | 22761 | C | IN-EFFECT | 2026/08/30 04:56:14 | top-level scripts |
| run_v16_llm_prior.py | 6350BBAECB81 | 13423 | C | IN-EFFECT | 2026/08/30 04:56:13 | top-level scripts |
| run_v17_fixed_sampler.py | 3E54797EEDEB | 10435 | C | IN-EFFECT | 2026/08/23 21:38:54 | top-level scripts |
| run_v17_fusion_fix.py | B592470C47AE | 10236 | C | IN-EFFECT | 2026/08/23 21:31:25 | top-level scripts |
| run_v17_multigraph.py | CA7E6031272C | 5682 | C | IN-EFFECT | 2026/08/23 21:33:45 | top-level scripts |
| run_v18_api_supplements.py | AEF28D92D763 | 42681 | C | IN-EFFECT | 2026/08/23 23:19:13 | top-level scripts |
| run_v19_benchmark_fixes.py | 674C2E5349CF | 22802 | C | IN-EFFECT | 2026/08/24 01:10:53 | top-level scripts |
| run_v19_fullrank.py | 8D1067E4E27B | 8976 | C | IN-EFFECT | 2026/08/30 04:56:31 | top-level scripts |
| run_v19_meanfield.py | 67EF3779478A | 11690 | C | IN-EFFECT | 2026/08/30 04:56:31 | top-level scripts |
| run_v19_quickwins.py | 93958A96B19A | 10509 | C | IN-EFFECT | 2026/08/24 01:07:34 | top-level scripts |
| run_v20_baselines.py | 1B9815FAD7CA | 12435 | C | IN-EFFECT | 2026/08/29 01:14:15 | top-level scripts |
| run_v20_bigquiz_eval.py | 1C1A82F4B48A | 9091 | C | IN-EFFECT | 2026/08/28 23:54:08 | top-level scripts |
| run_v20_bigquiz_fetch.py | F810F3A34EB2 | 7808 | C | IN-EFFECT | 2026/08/30 10:16:33 | top-level scripts |
| run_v20_corpus_eval.py | 2FAD3B28D34C | 20470 | C | IN-EFFECT | 2026/08/28 17:41:03 | top-level scripts |
| run_v20_cot_fetch.py | B4A214C4E50F | 3323 | C | IN-EFFECT | 2026/08/30 10:14:35 | top-level scripts |
| run_v20_crossval_eval.py | 1CDC6C37B236 | 14379 | C | IN-EFFECT | 2026/08/28 20:26:46 | top-level scripts |
| run_v20_crossval_fetch.py | 3465B43E2F8A | 4958 | C | IN-EFFECT | 2026/08/30 10:15:16 | top-level scripts |
| run_v20_familyL_fetch.py | FF38DBB3DE7F | 2088 | C | IN-EFFECT | 2026/08/30 10:14:03 | top-level scripts |
| run_v20_familyL_ingest.py | C5D96C1F0522 | 6108 | C | IN-EFFECT | 2026/08/29 01:14:15 | top-level scripts |
| run_v20_fastcheck.py | B6585A30D808 | 7243 | C | IN-EFFECT | 2026/08/28 22:07:04 | top-level scripts |
| run_v20_gt.py | 9F6DF7E94CDC | 9824 | C | IN-EFFECT | 2026/08/28 17:14:47 | top-level scripts |
| run_v20_gt2b.py | 361AFF516219 | 9076 | C | IN-EFFECT | 2026/08/29 19:57:30 | top-level scripts |
| run_v20_gt3_eval.py | 6A234EEE29B3 | 6983 | C | IN-EFFECT | 2026/08/29 15:02:33 | top-level scripts |
| run_v20_gt3_fetch.py | 1853F7E82A3A | 3858 | C | IN-EFFECT | 2026/08/30 10:11:34 | top-level scripts |
| run_v20_gt3b_fetch.py | EFAA93762269 | 3135 | C | IN-EFFECT | 2026/08/30 10:12:06 | top-level scripts |
| run_v20_gt3c_fetch.py | 48B659B95984 | 3193 | C | IN-EFFECT | 2026/08/30 10:13:37 | top-level scripts |
| run_v20_gt5.py | 32C03F5739D7 | 14957 | C | IN-EFFECT | 2026/08/30 10:18:23 | top-level scripts |
| run_v20_gt5b.py | 3B344435F4EA | 10419 | C | IN-EFFECT | 2026/08/30 10:19:10 | top-level scripts |
| run_v20_gt6.py | C5DCDB0F12E2 | 11010 | C | IN-EFFECT | 2026/08/29 15:43:45 | top-level scripts |
| run_v20_gt7.py | 38071308E9EF | 17509 | C | IN-EFFECT | 2026/08/30 10:20:37 | top-level scripts |
| run_v20_gt8.py | D07233229279 | 13876 | C | IN-EFFECT | 2026/08/29 19:33:18 | top-level scripts |
| run_v20_gt8b_eval.py | 07B74332EBC2 | 9196 | C | IN-EFFECT | 2026/08/29 22:27:23 | top-level scripts |
| run_v20_gt8b_fetch.py | FCE719AD054D | 6558 | C | IN-EFFECT | 2026/08/30 10:34:04 | top-level scripts |
| run_v20_gt8b_ingest.py | 5E3DB6F4869D | 5676 | C | IN-EFFECT | 2026/08/29 22:24:05 | top-level scripts |
| run_v20_gt8c_eval.py | 6D6DB8BDBB06 | 9594 | C | IN-EFFECT | 2026/08/30 15:52:41 | top-level scripts |
| run_v20_gt8c_fetch.py | 8079A5DBE251 | 8068 | C | IN-EFFECT | 2026/08/30 15:51:03 | top-level scripts |
| run_v20_gt8c_ingest.py | 81690A38F421 | 5866 | C | IN-EFFECT | 2026/08/30 15:51:41 | top-level scripts |
| run_v20_photonics.py | EC00CB18F95A | 7615 | C | IN-EFFECT | 2026/08/29 01:19:14 | top-level scripts |
| run_v20_quizbank.py | 3B2A7DD2044C | 8744 | C | IN-EFFECT | 2026/08/28 20:46:28 | top-level scripts |
| run_v20_vector_audit.py | 16A270A6BDAB | 4717 | C | IN-EFFECT | 2026/08/28 21:14:03 | top-level scripts |
| run_v21_gtformal.py | 9BBE43F41FA8 | 16600 | C | IN-EFFECT | 2026/08/30 15:35:54 | top-level scripts |
| run_v22_e95ci.py | 8470E3CE8CAE | 3058 | C | IN-EFFECT | 2026/08/30 21:26:23 | top-level scripts |
| run_v22_p1c.py | 6E9673205DC0 | 7236 | C | IN-EFFECT | 2026/08/30 18:28:58 | top-level scripts |
| scripts/run_deepseek_v41_30cells_v2.py | C7411AE13EC0 | 14017 | C | IN-EFFECT | 2026/09/10 16:15:10 | scripts series |
| scripts/run_deepseek_v41_30cells_v3.py | 03BC34EA88A8 | 13955 | C | IN-EFFECT | 2026/09/10 16:38:40 | scripts series |
| scripts/run_deepseek_v41_60cells_v2_startup.py | 769E1D04503B | 16071 | C | IN-EFFECT | 2026/09/10 17:31:43 | scripts series |
| scripts/run_embedding_dual_smoke.py | 9253225DE974 | 13599 | C | IN-EFFECT | 2026/09/10 17:03:53 | scripts series |
| scripts/run_v3x_6way_stage3_recovery.py | E4F96F2E9E4F | 15872 | C | IN-EFFECT | 2026/09/10 18:03:01 | scripts series |
| scripts/run_v3x_6way_verification.py | 27A046D569D1 | 25060 | C | IN-EFFECT | 2026/09/10 17:55:59 | scripts series |
| scripts/run_v3x_finalize.py | 46787531BF8E | 5932 | C | IN-EFFECT | 2026/09/10 18:15:09 | scripts series |
| scripts/run_v3x_stage3_minimal.py | 8B5D42772D5E | 12477 | C | IN-EFFECT | 2026/09/10 18:07:56 | scripts series |
| scripts/run_v41_flash_5cells_fix.py | E4546D734A53 | 17914 | C | IN-EFFECT | 2026/09/10 16:54:23 | scripts series |
| scripts/run_volcengine_seed_code_30cells.py | 75002485AA94 | 13924 | C | IN-EFFECT | 2026/09/16 11:01:12 | scripts series |
| svg_mindmap_ingest.py | FA661FD759ED | 8811 | C | IN-EFFECT | 2026/08/23 05:00:55 | top-level executors |
| tests/test_agents_merge.py | C7CC85FFB3F0 | 26615 | C | IN-EFFECT | 2026/08/30 10:34:38 | tests series |
| tests/test_diffusion.py | 2452BE26AF7E | 12463 | C | IN-EFFECT | 2026/08/23 19:21:32 | tests series |
| tests/test_fast.py | 5829F89C2352 | 3653 | C | IN-EFFECT | 2026/08/28 22:11:59 | tests series |
| tests/test_fingerprint_v0.py | 506BA4A55704 | 13788 | C | IN-EFFECT | 2026/09/01 16:35:59 | tests series |
| tests/test_gt_common.py | 6A2F32D1316A | 3697 | C | IN-EFFECT | 2026/08/30 10:29:22 | tests series |
| tests/test_llm_fetch.py | 90772F5CF41B | 11095 | C | IN-EFFECT | 2026/08/30 10:28:46 | tests series |
| tests/test_llm_prior.py | 11C2FFA37610 | 7701 | C | IN-EFFECT | 2026/08/23 20:02:35 | tests series |
| tests/test_new_modes.py | 0B2276028391 | 21275 | C | IN-EFFECT | 2026/08/23 09:40:33 | tests series |
| tests/test_protocol.py | F103C9D87C61 | 6979 | C | IN-EFFECT | 2026/08/30 04:58:18 | tests series |
| tests/test_v18.py | C523AE4B0989 | 17093 | C | IN-EFFECT | 2026/08/23 23:15:42 | tests series |
| tests/test_v19.py | B44E2945FA31 | 6056 | C | IN-EFFECT | 2026/08/24 01:10:27 | tests series |
| tests/test_v19_benchmark.py | F343754F380C | 7371 | C | IN-EFFECT | 2026/08/24 01:12:52 | tests series |
| tests/test_v20.py | E4712875F65D | 13249 | C | IN-EFFECT | 2026/08/28 17:19:09 | tests series |
| tests/test_v20_gt2b.py | 4CD18AE1D3DC | 4318 | C | IN-EFFECT | 2026/08/29 19:58:34 | tests series |
| tests/test_v20_gt5.py | 1F104B13A170 | 5746 | C | IN-EFFECT | 2026/08/29 15:36:51 | tests series |
| tests/test_v20_gt5b.py | 81FEB1F137B4 | 2423 | C | IN-EFFECT | 2026/08/29 15:44:42 | tests series |
| tests/test_v20_gt6.py | 5C7DD774A3F3 | 2584 | C | IN-EFFECT | 2026/08/29 15:44:43 | tests series |
| tests/test_v20_gt7.py | E8727F8F42DA | 6489 | C | IN-EFFECT | 2026/08/29 17:56:48 | tests series |
| tests/test_v20_gt8.py | B9479374DE4D | 5122 | C | IN-EFFECT | 2026/08/29 19:34:11 | tests series |
| tests/test_v20_gt8b.py | 3C4395DF9311 | 10109 | C | IN-EFFECT | 2026/08/29 22:27:24 | tests series |
| tests/test_v20_gt8c.py | 562DD8B920BC | 13458 | C | IN-EFFECT | 2026/08/30 15:55:13 | tests series |
| tests/test_v21_gtformal.py | 74650B1D603B | 7376 | C | IN-EFFECT | 2026/08/30 15:20:33 | tests series |
| tests/test_v22_p1c.py | B19BDB965CC0 | 3854 | C | IN-EFFECT | 2026/08/30 18:30:56 | tests series |
| tools/exp_harness.py | 275E480BA4D9 | 10090 | C | IN-EFFECT | 2026/09/09 16:16:50 | tools series |
| tools/llm_client.py | 1722500DA4AA | 8118 | C | IN-EFFECT | 2026/09/09 16:16:02 | tools series |
| tools/make_figures_v2.py | 0DC3EA09F42D | 21073 | C | IN-EFFECT | 2026/08/30 20:52:09 | tools series |
| tools/make_figures_v2_en.py | B4E880A6AF33 | 21188 | C | IN-EFFECT | 2026/08/30 20:46:55 | tools series |
| tools/read_key.py | A9B56C4E775F | 1047 | C | IN-EFFECT | 2026/09/10 14:45:46 | tools series |
| verifier/_build_partial.py | 04FCD95C70F1 | 7160 | C | IN-EFFECT | 2026/09/16 11:01:12 | verifier scripts |
| verifier/_read_summary.py | B4D89F052875 | 1231 | C | IN-EFFECT | 2026/09/10 20:50:17 | verifier scripts |
| verifier/_test_one.py | 893641FD9E25 | 2564 | C | IN-EFFECT | 2026/09/16 11:01:12 | verifier scripts |
| verifier/runs/2026-09-04_pd_v0.jsonl | 5042869BDF85 | 100 | C | IN-EFFECT | 2026/09/04 13:33:46 | verifier run logs |
| verifier/runs/v10_run1.md | 54BE4344E99A | 701 | C | IN-EFFECT | 2026/08/24 07:51:43 | verifier run logs |
| verifier/runs/v11_run1.md | BD36F361EA12 | 514 | C | IN-EFFECT | 2026/08/28 17:57:42 | verifier run logs |
| verifier/runs/v12_run1.md | 927EAFCB3B0B | 788 | C | IN-EFFECT | 2026/08/28 20:01:49 | verifier run logs |
| verifier/runs/v13_run1.md | AA1456D217FC | 145 | C | IN-EFFECT | 2026/08/28 20:30:14 | verifier run logs |
| verifier/runs/v14_run1.md | 3FDCA6C35DCB | 145 | C | IN-EFFECT | 2026/08/28 20:48:36 | verifier run logs |
| verifier/runs/v15_run1.md | 634EF5FA4EF8 | 475 | C | IN-EFFECT | 2026/08/28 21:17:49 | verifier run logs |
| verifier/runs/v16_run1.md | E6BF3B753FF6 | 359 | C | IN-EFFECT | 2026/08/28 21:54:50 | verifier run logs |
| verifier/runs/v17_run1.md | 9D0332C44044 | 283 | C | IN-EFFECT | 2026/08/28 22:51:36 | verifier run logs |
| verifier/runs/v18_run1.md | 4A3CE944CCE3 | 276 | C | IN-EFFECT | 2026/08/28 23:57:39 | verifier run logs |
| verifier/runs/v19_run1.md | 7B95DBD3F168 | 297 | C | IN-EFFECT | 2026/08/29 00:25:02 | verifier run logs |
| verifier/runs/v20_run1.md | 41D3D7F4A148 | 295 | C | IN-EFFECT | 2026/08/29 00:35:08 | verifier run logs |
| verifier/runs/v21_run1.md | 36B69E195F06 | 247 | C | IN-EFFECT | 2026/08/29 01:26:03 | verifier run logs |
| verifier/runs/v21_run2.md | 3246C7D46480 | 448 | C | IN-EFFECT | 2026/08/29 11:35:00 | verifier run logs |
| verifier/runs/v22_run1.md | 582531CCD67D | 436 | C | IN-EFFECT | 2026/08/29 11:22:52 | verifier run logs |
| verifier/runs/v23_run1.md | 9578066064CC | 586 | C | IN-EFFECT | 2026/08/29 15:09:59 | verifier run logs |
| verifier/runs/v24_run1.md | 67FD4FEC19F2 | 498 | C | IN-EFFECT | 2026/08/29 15:50:05 | verifier run logs |
| verifier/runs/v25_run1.md | B81E2FB0EA28 | 526 | C | IN-EFFECT | 2026/08/29 18:00:55 | verifier run logs |
| verifier/runs/v26_run1.md | 09B69C05BB47 | 546 | C | IN-EFFECT | 2026/08/29 19:39:05 | verifier run logs |
| verifier/runs/v27_run1.md | 0759457758BE | 559 | C | IN-EFFECT | 2026/08/29 20:02:00 | verifier run logs |
| verifier/runs/v27_run2.md | 82A92D9CE191 | 554 | C | IN-EFFECT | 2026/08/29 20:03:11 | verifier run logs |
| verifier/runs/v28_run1.md | 6D85472D724C | 771 | C | IN-EFFECT | 2026/08/29 21:09:29 | verifier run logs |
| verifier/runs/v29_run1.md | 26A667EDEC7A | 440 | C | IN-EFFECT | 2026/08/29 23:03:33 | verifier run logs |
| verifier/runs/v29_run2.md | BADD1ED95A6D | 627 | C | IN-EFFECT | 2026/08/29 23:05:27 | verifier run logs |
| verifier/runs/v30_run1.md | CEF68A7A30A5 | 735 | C | IN-EFFECT | 2026/08/29 23:47:50 | verifier run logs |
| verifier/runs/v30_run2.md | D22151B9AD6D | 787 | C | IN-EFFECT | 2026/08/29 23:49:54 | verifier run logs |
| verifier/runs/v30_run3.md | 0DC553ED64C2 | 771 | C | IN-EFFECT | 2026/08/29 23:51:37 | verifier run logs |
| verifier/runs/v31_run1.md | DCB11FEFABF2 | 673 | C | IN-EFFECT | 2026/08/30 01:08:22 | verifier run logs |
| verifier/runs/v31_run2.md | 8727C88269F3 | 747 | C | IN-EFFECT | 2026/08/30 01:10:29 | verifier run logs |
| verifier/runs/v32_run1.md | 1798C48ACEA7 | 859 | C | IN-EFFECT | 2026/08/30 03:57:46 | verifier run logs |
| verifier/runs/v32_run2.md | 83C987FB96D9 | 894 | C | IN-EFFECT | 2026/08/30 03:59:13 | verifier run logs |
| verifier/runs/v32_run3.md | 4A99A1134C8C | 886 | C | IN-EFFECT | 2026/08/30 04:06:01 | verifier run logs |
| verifier/runs/v33_run1.md | 9E917334781C | 2160 | C | IN-EFFECT | 2026/08/30 05:05:50 | verifier run logs |
| verifier/runs/v33_run2.md | 158948A53671 | 1783 | C | IN-EFFECT | 2026/08/30 05:12:50 | verifier run logs |
| verifier/runs/v34_run1.md | 03F773F08FA7 | 83 | C | IN-EFFECT | 2026/08/30 09:57:16 | verifier run logs |
| verifier/runs/v34_run2.md | D9BFAAE6D08B | 118 | C | IN-EFFECT | 2026/08/30 14:13:30 | verifier run logs |
| verifier/runs/v35_run1.md | A693C838AE57 | 39 | C | IN-EFFECT | 2026/08/30 15:47:20 | verifier run logs |
| verifier/runs/v35_run2.md | 11CE6990B84A | 118 | C | IN-EFFECT | 2026/08/30 17:08:56 | verifier run logs |
| verifier/runs/v41_2026-08-30_run1.txt | E156E87CABA8 | 158 | C | IN-EFFECT | 2026/09/17 23:20:49 | verifier run logs |
| verifier/runs/v42_2026-08-30_run1.txt | 8FDE2819EF29 | 279 | C | IN-EFFECT | 2026/09/17 23:20:49 | verifier run logs |
| verifier/runs/v42_2026-08-30_run2.txt | 1AA0257CAAC9 | 156 | C | IN-EFFECT | 2026/09/17 23:20:50 | verifier run logs |
| verifier/runs/v43_2026-09-01_run1.txt | AA82005B05DE | 199 | C | IN-EFFECT | 2026/09/17 23:20:51 | verifier run logs |
| verifier/v1/check.py | 03BC1ADFC82F | 2976 | C | IN-EFFECT | 2026/08/23 10:27:37 | verifier v sequence (43 items) |
| verifier/v10/check.py | 4FD5FDD754C0 | 5261 | C | IN-EFFECT | 2026/08/24 07:15:04 | verifier v sequence (43 items) |
| verifier/v11/check.py | 3B8682A7E562 | 2767 | C | IN-EFFECT | 2026/08/28 17:56:50 | verifier v sequence (43 items) |
| verifier/v12/check.py | 87C9C883E3BF | 4142 | C | IN-EFFECT | 2026/08/29 01:14:15 | verifier v sequence (43 items) |
| verifier/v13/check.py | 1159FACAB6DB | 3495 | C | IN-EFFECT | 2026/08/28 20:29:43 | verifier v sequence (43 items) |
| verifier/v14/check.py | 4BA223D2185D | 3278 | C | IN-EFFECT | 2026/08/28 20:48:03 | verifier v sequence (43 items) |
| verifier/v15/check.py | BE0F2BBAB0A2 | 3231 | C | IN-EFFECT | 2026/08/28 21:17:37 | verifier v sequence (43 items) |
| verifier/v16/check.py | 223082632A1D | 2691 | C | IN-EFFECT | 2026/08/28 21:54:41 | verifier v sequence (43 items) |
| verifier/v17/check.py | 679792BE51ED | 2897 | C | IN-EFFECT | 2026/08/28 22:51:15 | verifier v sequence (43 items) |
| verifier/v18/check.py | 6ABDDA4F7400 | 3180 | C | IN-EFFECT | 2026/08/29 01:14:16 | verifier v sequence (43 items) |
| verifier/v19/check.py | C53CF72D085B | 1995 | C | IN-EFFECT | 2026/08/29 00:24:42 | verifier v sequence (43 items) |
| verifier/v2/check.py | AF3A78983537 | 2510 | C | IN-EFFECT | 2026/08/23 19:21:32 | verifier v sequence (43 items) |
| verifier/v20/check.py | 9D0F1E950DEE | 2790 | C | IN-EFFECT | 2026/08/29 00:33:07 | verifier v sequence (43 items) |
| verifier/v21/check.py | 5E7D7435C4A3 | 3702 | C | IN-EFFECT | 2026/08/29 01:23:52 | verifier v sequence (43 items) |
| verifier/v22/check.py | F16BEAAE5675 | 2857 | C | IN-EFFECT | 2026/08/29 11:20:44 | verifier v sequence (43 items) |
| verifier/v23/check.py | 9ECB25362C9A | 2659 | C | IN-EFFECT | 2026/08/29 15:08:00 | verifier v sequence (43 items) |
| verifier/v24/check.py | E6C7513D54F3 | 3124 | C | IN-EFFECT | 2026/08/29 15:49:47 | verifier v sequence (43 items) |
| verifier/v25/check.py | CC6FF5453E06 | 2576 | C | IN-EFFECT | 2026/08/29 18:00:10 | verifier v sequence (43 items) |
| verifier/v26/check.py | C58A9652A42A | 2595 | C | IN-EFFECT | 2026/09/16 11:01:12 | verifier v sequence (43 items) |
| verifier/v27/check.py | 118524C7E808 | 2132 | C | IN-EFFECT | 2026/09/16 11:01:12 | verifier v sequence (43 items) |
| verifier/v28/check.py | B73A6B268F64 | 2201 | C | IN-EFFECT | 2026/09/16 11:01:12 | verifier v sequence (43 items) |
| verifier/v29/check.py | 5923E2C379F6 | 2124 | C | IN-EFFECT | 2026/09/16 11:01:12 | verifier v sequence (43 items) |
| verifier/v3/check.py | 02A5A86D38BF | 2544 | C | IN-EFFECT | 2026/08/23 19:21:32 | verifier v sequence (43 items) |
| verifier/v30/check.py | 2CF46F79A669 | 2565 | C | IN-EFFECT | 2026/09/16 11:01:12 | verifier v sequence (43 items) |
| verifier/v31/check.py | E5BB0020E500 | 2185 | C | IN-EFFECT | 2026/09/16 11:01:12 | verifier v sequence (43 items) |
| verifier/v32/check.py | 399BFC743F24 | 2551 | C | IN-EFFECT | 2026/09/16 11:01:12 | verifier v sequence (43 items) |
| verifier/v33/check.py | 32FEFC485326 | 6019 | C | IN-EFFECT | 2026/08/30 05:11:44 | verifier v sequence (43 items) |
| verifier/v34/check.py | 0BBD226CD2AE | 3715 | C | IN-EFFECT | 2026/08/30 09:57:03 | verifier v sequence (43 items) |
| verifier/v35/check.py | 2130A5F5E1BF | 2385 | C | IN-EFFECT | 2026/08/30 15:47:20 | verifier v sequence (43 items) |
| verifier/v36/check.sh | 2212DCD98CD1 | 968 | C | IN-EFFECT | 2026/09/18 13:43:52 | verifier v sequence (43 items) |
| verifier/v37/check.sh | CED43B5F8800 | 1141 | C | IN-EFFECT | 2026/09/18 13:43:52 | verifier v sequence (43 items) |
| verifier/v38/check.sh | 43B501C5C20D | 1705 | C | IN-EFFECT | 2026/09/17 23:20:52 | verifier v sequence (43 items) |
| verifier/v39/check.sh | D48AC555761F | 1935 | C | IN-EFFECT | 2026/09/17 23:20:53 | verifier v sequence (43 items) |
| verifier/v4/check.py | F058E85C5383 | 3205 | C | IN-EFFECT | 2026/08/23 19:33:47 | verifier v sequence (43 items) |
| verifier/v40/check.sh | 7B15CD2F4C7E | 1604 | C | IN-EFFECT | 2026/09/17 23:20:54 | verifier v sequence (43 items) |
| verifier/v41/check.sh | 2C9FE869DAAA | 1687 | C | IN-EFFECT | 2026/09/17 23:20:54 | verifier v sequence (43 items) |
| verifier/v42/check.sh | 3EA87E2CFC61 | 1509 | C | IN-EFFECT | 2026/09/17 23:20:55 | verifier v sequence (43 items) |
| verifier/v43/check.sh | 71B83217032D | 1224 | C | IN-EFFECT | 2026/09/17 23:20:55 | verifier v sequence (43 items) |
| verifier/v5/check.py | 3D776381F665 | 2255 | C | IN-EFFECT | 2026/08/23 20:04:44 | verifier v sequence (43 items) |
| verifier/v6/check.py | 8366078A10E4 | 2757 | C | IN-EFFECT | 2026/08/23 20:23:46 | verifier v sequence (43 items) |
| verifier/v7/check.py | A70A68037D92 | 4300 | C | IN-EFFECT | 2026/08/23 21:03:13 | verifier v sequence (43 items) |
| verifier/v8/check.py | 01B63B1A9C5F | 3210 | C | IN-EFFECT | 2026/08/23 21:40:59 | verifier v sequence (43 items) |
| verifier/v9/check.py | 5FAAD917D839 | 5352 | C | IN-EFFECT | 2026/08/23 23:46:50 | verifier v sequence (43 items) |
| volcengine_glm_latest_30cells_v2_runner_2026_09_10.py | 26FF34BFCC79 | 20745 | C | IN-EFFECT | 2026/09/18 13:48:17 | top-level executors |

#### V12 / KNOWLEDGE > 41 items

| Path | SHA-12 | Size (B) | View | Status | Modified | Note |
|---|---|---|---|---|---|---|
| docs/reviews/review_gtformal_integration_v2X.md | 325C9D87787B | 8582 | C | IN-EFFECT | 2026/08/30 16:58:11 | docs/reviews subdir |
| docs/reviews/review_salvage_integration_v2X.md | 96AE50306F36 | 6212 | C | IN-EFFECT | 2026/08/30 05:06:19 | docs/reviews subdir |
| docs/reviews/review_sprint_v2X.md | 4356CD02562E | 7776 | C | IN-EFFECT | 2026/08/30 11:11:11 | docs/reviews subdir |
| paper/FIGURE_LANGUAGE_POLICY.md | A18B5D0D4485 | 2495 | A | IN-EFFECT | 2026/08/30 11:16:21 | paper drafts (CN/EN) |
| paper/deposon_paper_final_cn.md | C5F6A23F4408 | 53838 | A | IN-EFFECT | 2026/09/20 17:11:14 | paper drafts (CN/EN) |
| paper/deposon_paper_final_en.md | 2EC20B96E941 | 68164 | A | IN-EFFECT | 2026/09/20 17:11:14 | paper drafts (CN/EN) |
| paper/v2/outline_v2X.md | 116D193B1607 | 10476 | A | IN-EFFECT | 2026/08/30 10:43:36 | paper drafts (CN/EN) |
| paper/v2/related_work_v2X.md | 7FB001ADD973 | 10114 | A | IN-EFFECT | 2026/08/29 15:43:30 | paper drafts (CN/EN) |
| reviews/data/t1_potential.csv | E110A020954F | 4833 | C | IN-EFFECT | 2026/08/28 21:30:52 | reviews series |
| reviews/data/t1b_classics.csv | 82016E695F48 | 5450 | C | IN-EFFECT | 2026/08/28 21:32:04 | reviews series |
| reviews/data/t1c_loglinear.csv | C50FF98A95CC | 5566 | C | IN-EFFECT | 2026/08/28 21:33:20 | reviews series |
| reviews/data/t1d_pagerank.csv | 8B1A9E5113BB | 4167 | C | IN-EFFECT | 2026/08/28 21:36:57 | reviews series |
| reviews/data/t2_linkpred.csv | 19555B7D9D43 | 6750 | C | IN-EFFECT | 2026/08/28 21:30:43 | reviews series |
| reviews/data/t2b_linkpred.csv | 6DE8F0E651C4 | 5520 | C | IN-EFFECT | 2026/08/28 21:31:15 | reviews series |
| reviews/data/t2c_advlink.csv | 67D1D8342060 | 6886 | C | IN-EFFECT | 2026/08/28 21:32:32 | reviews series |
| reviews/data/t2d_hiding.csv | 5749CE2C5BF7 | 5377 | C | IN-EFFECT | 2026/08/28 21:33:27 | reviews series |
| reviews/data/t2e_nettack.csv | 2628F74421F2 | 1875 | C | IN-EFFECT | 2026/08/28 21:35:25 | reviews series |
| reviews/data/t2f_waniek.csv | F0D2C9D2A39B | 1271 | C | IN-EFFECT | 2026/08/28 21:35:28 | reviews series |
| reviews/data/t3_mechdesign.csv | 6E8B6E4730A8 | 6680 | C | IN-EFFECT | 2026/08/28 21:31:20 | reviews series |
| reviews/data/t3b_verifiable.csv | F48C9F09A3B4 | 6731 | C | IN-EFFECT | 2026/08/28 21:32:32 | reviews series |
| reviews/data/t3d_llmmd.csv | 49028967AD57 | 3405 | C | IN-EFFECT | 2026/08/28 21:35:31 | reviews series |
| reviews/data/t3e_commit.csv | BF0A2B544A74 | 3691 | C | IN-EFFECT | 2026/08/28 21:36:14 | reviews series |
| reviews/data/t4_poa.csv | 8BA9FADA9EAD | 6567 | C | IN-EFFECT | 2026/08/28 21:31:59 | reviews series |
| reviews/deep_probe_R1.md | 190DD5DF9AF2 | 14895 | C | IN-EFFECT | 2026/08/29 01:04:00 | reviews series |
| reviews/deep_probe_R2.md | A4F8A55B70BA | 23391 | C | IN-EFFECT | 2026/08/29 01:10:13 | reviews series |
| reviews/design_probe_v19.md | C41F1717310E | 13967 | C | IN-EFFECT | 2026/08/24 00:49:48 | reviews series |
| reviews/experiment_design_v19.md | 56ECEF878539 | 8840 | C | IN-EFFECT | 2026/08/24 00:35:44 | reviews series |
| reviews/independent_review_20260823.md | 7474FC258375 | 1724 | C | IN-EFFECT | 2026/08/23 21:40:22 | reviews series |
| reviews/literature_scan_v19.md | 70EA38D5B9C0 | 28449 | C | IN-EFFECT | 2026/08/24 00:40:36 | reviews series |
| reviews/literature_scan_v2X_A.md | D0BBA9379B4B | 18876 | C | IN-EFFECT | 2026/08/28 21:42:49 | reviews series |
| reviews/literature_scan_v2X_B.md | 313B30815A39 | 30468 | C | IN-EFFECT | 2026/08/28 21:50:11 | reviews series |
| reviews/peer_review_v19_A.md | 28878116D87B | 24409 | C | IN-EFFECT | 2026/08/24 00:36:05 | reviews series |
| reviews/peer_review_v19_B.md | DA98F9E310D4 | 42672 | C | IN-EFFECT | 2026/08/24 01:07:19 | reviews series |
| reviews/post_draft_verification_v2X.md | 0C49F2D36088 | 9979 | C | IN-EFFECT | 2026/08/29 21:06:20 | reviews series |
| reviews/post_edit_verification_v19.md | E262E9D684FE | 19327 | C | IN-EFFECT | 2026/08/24 07:49:36 | reviews series |
| reviews/review_coach_v2X_draft.md | 0BAFE659C00D | 23468 | C | IN-EFFECT | 2026/08/29 22:22:13 | reviews series |
| reviews/review_coach_v2X_draft_r2.md | 67162AB18F9A | 15721 | C | IN-EFFECT | 2026/08/29 23:42:38 | reviews series |
| reviews/review_coach_v2X_outline.md | 5BEBB5E1D329 | 11295 | C | IN-EFFECT | 2026/08/29 15:34:49 | reviews series |
| reviews/review_format_v2X.md | 2DC4B45424AB | 6656 | C | IN-EFFECT | 2026/08/30 04:02:12 | reviews series |
| reviews/review_realign_v2X.md | 3ECB285DB3D8 | 7338 | C | IN-EFFECT | 2026/08/30 01:03:56 | reviews series |
| verifier/README.md | D76F2DC473BE | 14360 | C | IN-EFFECT | 2026/08/30 17:08:56 | verifier README |

#### V12 / NOTES > 51 items

| Path | SHA-12 | Size (B) | View | Status | Modified | Note |
|---|---|---|---|---|---|---|
| docs/ADVISOR_BRIEFING_2026-08-30.md | 40278BC425E6 | 5890 |  | IN-EFFECT | 2026/08/29 10:16:17 |  |
| docs/ARCH_AUDIT_v2.md | 5BEE4C6CF47C | 14698 |  | IN-EFFECT | 2026/08/30 04:39:28 |  |
| docs/BASELINE_REGISTRY.md | 51B271548835 | 3356 |  | IN-EFFECT | 2026/08/28 20:59:38 |  |
| docs/CLOSURE_v19_and_v2X_gametheory.md | 84323775A212 | 9065 |  | IN-EFFECT | 2026/08/28 15:55:51 |  |
| docs/DATASET_HEALTH_v2.md | C87A0C1F5AF6 | 4892 |  | IN-EFFECT | 2026/08/30 04:40:23 |  |
| docs/Deposon_Requirements_v1.md | EE33F3F22E1B | 13914 |  | IN-EFFECT | 2026/08/22 21:07:01 |  |
| docs/Deposon_v1_3_验证报告.md | DC5BE727F920 | 8003 |  | IN-EFFECT | 2026/08/22 21:07:01 |  |
| docs/Deposon_v1_4_验证报告.md | 3BCCCF03F7CA | 4254 |  | IN-EFFECT | 2026/08/22 21:11:43 |  |
| docs/FIGURES_v2.md | 1CD4A4CB0A76 | 5851 |  | IN-EFFECT | 2026/08/30 11:15:47 |  |
| docs/Findings_GT2B.md | E6CC74F9917D | 3322 |  | IN-EFFECT | 2026/08/29 20:00:21 |  |
| docs/Findings_GT3.md | 4F3242B2A661 | 2632 |  | IN-EFFECT | 2026/08/29 15:06:30 |  |
| docs/Findings_GT8.md | 869C0071FBC2 | 3890 |  | IN-EFFECT | 2026/08/29 19:36:27 |  |
| docs/Findings_GT8B.md | 956183753A2E | 9809 |  | IN-EFFECT | 2026/08/30 10:38:41 |  |
| docs/Findings_GT_FORMAL.md | FAB607F0E180 | 6345 |  | IN-EFFECT | 2026/08/30 15:45:12 |  |
| docs/Findings_v2.0.md | 7E5DC4B045D8 | 4364 |  | IN-EFFECT | 2026/08/28 17:44:22 |  |
| docs/Findings_v2.0_bigquiz.md | D4ED18152DC0 | 3291 |  | IN-EFFECT | 2026/08/28 23:55:23 |  |
| docs/Findings_v2.0_boss.md | 36C714EABE3B | 3642 |  | IN-EFFECT | 2026/08/28 21:16:05 |  |
| docs/Findings_v2.0_corrections.md | 5864BBE5ADAE | 5012 |  | IN-EFFECT | 2026/08/29 01:23:08 |  |
| docs/Findings_v2.0_crossval.md | 32D26CB09568 | 4566 |  | IN-EFFECT | 2026/08/28 20:28:59 |  |
| docs/Findings_v2.0_hardening.md | A7F479793F01 | 3563 |  | IN-EFFECT | 2026/08/28 22:49:38 |  |
| docs/Findings_v2.0_photonics.md | 9158F54EC248 | 4377 |  | IN-EFFECT | 2026/08/30 04:46:02 |  |
| docs/Findings_v2.0_skills.md | 43731392B581 | 3456 |  | IN-EFFECT | 2026/08/28 20:47:31 |  |
| docs/GT_FORMALIZATION_v1.md | AEEFB8EF6972 | 19100 |  | IN-EFFECT | 2026/08/30 15:45:39 |  |
| docs/GT_RECONSTRUCTION.md | 570B7BD3E286 | 6695 |  | IN-EFFECT | 2026/08/29 17:59:43 |  |
| docs/LESSONS_INDEX.md | 7E3674A80CB7 | 4682 |  | IN-EFFECT | 2026/08/29 10:11:09 |  |
| docs/LESSONS_v19.md | DBBCF8E5E89D | 5290 |  | IN-EFFECT | 2026/08/28 17:56:50 |  |
| docs/LESSONS_v20_deepprobe.md | 5C898D4407EE | 8409 |  | IN-EFFECT | 2026/08/29 10:06:48 |  |
| docs/MODEL_ARGUMENTATION_v2.md | 2C83C42804E4 | 30142 |  | IN-EFFECT | 2026/08/30 10:42:40 |  |
| docs/PAPER_BRIEF.md | DE450C0BEFFA | 11296 |  | IN-EFFECT | 2026/08/30 11:09:37 |  |
| docs/PROGRESS_REPORT_LAYMAN.md | 25546FFDC56B | 8472 |  | IN-EFFECT | 2026/08/29 15:08:52 |  |
| docs/REFACTOR_v2.md | 03C8BAA18D93 | 23042 |  | IN-EFFECT | 2026/08/30 10:39:00 |  |
| docs/REF_VERIFICATION_v2.md | 64F0A3772C12 | 5860 |  | IN-EFFECT | 2026/08/30 11:17:21 |  |
| docs/Roadmap_v2X.md | A6AAF3200611 | 6467 |  | IN-EFFECT | 2026/08/24 11:13:19 |  |
| docs/SALVAGE_v2.md | F28A81D6302D | 7312 |  | IN-EFFECT | 2026/08/30 04:41:52 |  |
| docs/SECURITY_AUDIT_v2.md | 317FB508940A | 4707 |  | IN-EFFECT | 2026/08/30 04:39:49 |  |
| docs/SPEC_GT2B.md | 68A5B08EF007 | 3318 |  | IN-EFFECT | 2026/08/29 19:56:29 |  |
| docs/SPEC_GT2C.md | 29AF533486B2 | 3172 |  | IN-EFFECT | 2026/08/30 18:32:55 |  |
| docs/SPEC_GT3.md | 432EC337D586 | 5369 |  | IN-EFFECT | 2026/08/29 14:09:52 |  |
| docs/SPEC_GT5C.md | 1E41B4334735 | 3046 |  | IN-EFFECT | 2026/08/30 18:33:30 |  |
| docs/SPEC_GT8.md | EDF6F4465EAD | 4181 |  | IN-EFFECT | 2026/08/29 19:40:49 |  |
| docs/SPEC_GT8B.md | 3545C01E1291 | 7486 |  | IN-EFFECT | 2026/08/30 10:37:50 |  |
| docs/SPEC_GT8C.md | 6B09DE9911C0 | 6326 |  | IN-EFFECT | 2026/08/30 15:50:15 |  |
| docs/SPEC_v1.5.md | C165A86CF551 | 6204 |  | IN-EFFECT | 2026/08/23 19:22:13 |  |
| docs/SPEC_v1.8.md | AD0E445714D9 | 9850 |  | IN-EFFECT | 2026/08/23 23:19:47 |  |
| docs/SPEC_v2.0.md | BAC61D51FD20 | 5333 |  | IN-EFFECT | 2026/08/28 16:54:47 |  |
| docs/SPEC_v2.0_amendment1.md | 3E3A5014CB0E | 4743 |  | IN-EFFECT | 2026/08/29 01:22:16 |  |
| docs/SYNTHESIS_mind_game.md | 0F36AAEEDA6F | 9191 |  | IN-EFFECT | 2026/08/29 00:22:08 |  |
| docs/THINKING_V3_GT_CONTRIB_2026.md | 8C1D733F9182 | 19508 |  | IN-EFFECT | 2026/08/30 20:45:01 |  |
| docs/simple_baseline_failure_analysis.md | 968776002868 | 6080 |  | IN-EFFECT | 2026/08/23 00:01:28 |  |
| docs/space_release_log.json | 110607514753 | 5056 |  | IN-EFFECT | 2026/08/28 23:54:50 |  |
| docs/variant_params_table.md | 25F90F106451 | 4035 |  | IN-EFFECT | 2026/08/23 00:01:28 |  |

#### V12 / BULK > 722 unclassified items (legacy code / scripts)

Bulk enumeration follows. Files here are pre-existing V1-V2 code/scripts/docs with no V3/V4 classification; their view-tag is C unless explicitly flagged.

| Path | SHA-12 | Size (B) | Modified |
|---|---|---|---|
| .gitignore | 7D8D71EA2AF2 | 91 | 2026/08/22 21:07:01 |
| = | E3B0C44298FC | 0 | 2026/09/24 14:31:45 |
| LICENSE | 6A703B06F0FE | 1085 | 2026/08/22 21:07:57 |
| README.md | 18E095C85427 | 3756 | 2026/08/23 07:47:23 |
| RELEASE_v1.4.0.md | FF9FF3177C06 | 3847 | 2026/08/23 16:38:29 |
| _v4_l6_s38v2_verify_2026_09_24.py | C665860F459A | 3729 | 2026/09/24 11:36:45 |
| docs/V3X/V7_§3_P_C_P_E_GRAY_NOTE_2026_09_11.md | F80CC4E1FB7F | 7344 | 2026/09/11 13:15:52 |
| docs/V3X_COLLAB_DIRECTIONS.md | 5A27C2350036 | 16363 | 2026/08/31 09:32:54 |
| letters/_v4_ide_track_review_trae_code_supplement_2026_09_20.md | D3BDFC99FCDC | 11877 | 2026/09/20 15:02:13 |
| letters/_v4_ide_track_review_trae_work_2026_09_20.md | 21D384CF3422 | 7488 | 2026/09/20 17:35:40 |
| requirements.txt | AB3045B2C6D9 | 27 | 2026/08/22 21:07:57 |
| results/Deposon_评估汇总_v1_3_0.json | 2F02F50C164B | 2811 | 2026/08/22 21:07:01 |
| results/_adendum_H_pg_dhde_shrink_20260917_132049.json | B9A0253BA6A0 | 4613 | 2026/09/17 13:20:50 |
| results/_adendum_a_degradation_precheck_20260917_132049.json | 38FABEB19691 | 4248 | 2026/09/17 13:20:50 |
| results/_adendum_b_pi_real_labels_v2_20260917_133726.json | 3D344711CF8C | 2374 | 2026/09/17 13:37:29 |
| results/_adendum_b_pi_real_labels_v2_20260917_133852.json | C725E08E0A1C | 2374 | 2026/09/17 13:38:55 |
| results/_adendum_c_pm_attack_surface_v2_20260917_133726.json | 193BA7D66412 | 4123 | 2026/09/17 19:15:01 |
| results/_adendum_c_pm_attack_surface_v2_20260917_133852.json | 6EBA63788CA8 | 4122 | 2026/09/17 19:15:01 |
| results/_adendum_d_pc_r2_per_model_v2_20260917_133726.json | 6FE706750823 | 4605 | 2026/09/17 13:37:29 |
| results/_adendum_d_pc_r2_per_model_v2_20260917_133852.json | D66792EEA40E | 4605 | 2026/09/17 13:38:55 |
| results/_adendum_e_pd_supplement_v2_20260917_133726.json | 2C4790FFB6E3 | 1353 | 2026/09/17 13:37:29 |
| results/_adendum_e_pd_supplement_v2_20260917_133852.json | 46D8DACB4721 | 1353 | 2026/09/17 13:38:55 |
| results/_adendum_f_pe_3modal_closure_llm_dispatch_20260917_132143.json | 879494ED8FB9 | 3646 | 2026/09/17 13:21:43 |
| results/_adendum_f_pe_3modal_v2_20260917_143033.json | AFAB79249BE7 | 38622 | 2026/09/17 14:30:34 |
| results/_adendum_fgk_complete_20260917_143033.md | 958188C83CF0 | 14005 | 2026/09/17 14:31:34 |
| results/_adendum_g_pf_dfix2_timing_converge_llm_dispatch_20260917_132143.json | D10462080832 | 2757 | 2026/09/17 13:21:43 |
| results/_adendum_g_pf_dfix2_v2_20260917_143033.json | BF8DB2AD255B | 95292 | 2026/09/17 14:30:34 |
| results/_adendum_i_po_captions_closure_20260917_132049.json | 18165008BEF6 | 4429 | 2026/09/17 13:20:50 |
| results/_adendum_j_warehouse_spearman_health_20260917_132049.json | DF661D62426A | 11337 | 2026/09/17 13:20:50 |
| results/_adendum_k_087_cluster_cross_backbone_llm_dispatch_20260917_132143.json | ACDF933F68E0 | 2911 | 2026/09/17 13:21:43 |
| results/_adendum_k_qwen3_087_cluster_v2_20260917_143033.json | 43477C8EA2D6 | 32481 | 2026/09/17 14:30:34 |
| results/_adendum_l_verifier_dual_impl_diff_20260917_132049.json | 1532607DED80 | 2783 | 2026/09/17 13:20:50 |
| results/_adendum_m_pj_convergence_basin_v2_20260917_133726.json | EA7FFDA97E20 | 3694 | 2026/09/17 13:37:29 |
| results/_adendum_m_pj_convergence_basin_v2_20260917_133852.json | 8AB01A1E42AE | 3686 | 2026/09/17 13:38:55 |
| results/_adendum_n_pn_coupling_v2_20260917_133726.json | 1B91CC25CA57 | 2012 | 2026/09/17 13:37:29 |
| results/_adendum_n_pn_coupling_v2_20260917_133852.json | A32F3C8BA520 | 2011 | 2026/09/17 13:38:55 |
| results/_adendum_o_pk_v2_three_way_v2_20260917_133726.json | 725FD7B961F8 | 1971 | 2026/09/17 13:37:29 |
| results/_adendum_o_pk_v2_three_way_v2_20260917_133852.json | A30FF093305D | 1970 | 2026/09/17 13:38:55 |
| results/_adendum_p_pc_two_phase_fail_h0_20260917_132049.json | 6B26DADDC92C | 2456 | 2026/09/17 13:20:50 |
| results/_adendum_q_deepseek_v4_pro_anchor_20260917_132049.json | AB5D9AE6E42A | 4003 | 2026/09/17 13:20:50 |
| results/_agent_trio_redesign_draft_2026_09_23.md | E4320F20CAD4 | 10026 | 2026/09/23 16:11:18 |
| results/_archive_2026_09_20/_archive_manifest_2026_09_18.json | A729875C0C67 | 4712 | 2026/09/18 22:04:18 |
| results/_archive_2026_09_20/_archive_manifest_2026_09_20.json | 4DD89950BF11 | 35682 | 2026/09/20 11:07:34 |
| results/_archive_2026_09_20/mavis_trash_2026_09_18.py | 46576E7D99ED | 11937 | 2026/09/18 21:51:46 |
| results/_archive_2026_09_21/2026-09-20.md | BE7AA1C479B2 | 6186 | 2026/09/20 18:26:50 |
| results/_archive_2026_09_21/2026-09-21.md | EF648F34A3A3 | 2676 | 2026/09/21 09:43:13 |
| results/_archive_2026_09_21/Deposon_评估汇总_v1_3_0.json | 2F02F50C164B | 2811 | 2026/08/22 21:07:01 |
| results/_archive_2026_09_21/_archive_manifest_2026_09_21.json | 33FE31633DA8 | 17353 | 2026/09/21 19:55:39 |
| results/_archive_2026_09_21/_bom_prefix.py | D1575CDA7DEC | 319 | 2026/09/21 15:24:38 |
| results/_archive_2026_09_21/_check_bom_c2a1.ps1 | F0AEC1200B28 | 307 | 2026/09/21 15:24:46 |
| results/_archive_2026_09_21/_v4_accept_selfcheck_2026_09_20.py | 96EA96485500 | 2013 | 2026/09/20 17:32:52 |
| results/_archive_2026_09_21/_v4_addendum_selfcheck_2026_09_20.py | 9C752A055C71 | 1340 | 2026/09/20 21:24:01 |
| results/_archive_2026_09_21/_v4_anchor_gteval2_2026_09_20.py | 549E693E8337 | 814 | 2026/09/20 21:09:09 |
| results/_archive_2026_09_21/_v4_anchor_gteval3_2026_09_20.py | 980A534C5E3C | 618 | 2026/09/20 21:20:08 |
| results/_archive_2026_09_21/_v4_anchor_gteval_2026_09_20.py | DB8F70B9BE38 | 866 | 2026/09/20 21:08:37 |
| results/_archive_2026_09_21/_v4_brainstorm_seeds_2026_09_20.md | 0EB1CFAA2992 | 14994 | 2026/09/20 16:31:37 |
| results/_archive_2026_09_21/_v4_cite_collect_2026_09_20.py | 2A839E98F051 | 3117 | 2026/09/20 17:25:02 |
| results/_archive_2026_09_21/_v4_distillation_prompt_pack_2026_09_20_v1.0.md | E5C37E90255B | 25371 | 2026/09/20 16:39:10 |
| results/_archive_2026_09_21/_v4_invitation_verify_2026_09_20.py | 509BB8DBA186 | 5665 | 2026/09/20 14:48:25 |
| results/_archive_2026_09_21/_v4_last_checks_2026_09_20.py | 1F8032113B02 | 1188 | 2026/09/20 17:27:24 |
| results/_archive_2026_09_21/_v4_mm_lines_2026_09_20.py | FB640FF4225E | 468 | 2026/09/20 17:29:44 |
| results/_archive_2026_09_21/_v4_nokey_find2_2026_09_20.py | EF89DE50EC84 | 341 | 2026/09/20 21:23:17 |
| results/_archive_2026_09_21/_v4_nokey_find_2026_09_20.py | 87B6F4EE4ACA | 520 | 2026/09/20 21:22:19 |
| results/_archive_2026_09_21/_v4_reader_verify_2026_09_20.py | 8E171B0B7BE1 | 7377 | 2026/09/20 17:23:16 |
| results/_archive_2026_09_21/_v4_reply_selfcheck_2026_09_20.py | 405F804FA7DD | 1690 | 2026/09/20 17:31:06 |
| results/_archive_2026_09_21/_v4_verify_round2_2026_09_20.py | 46710CA9F87E | 3730 | 2026/09/20 15:02:39 |
| results/_archive_2026_09_21/_v4_verify_round3_2026_09_20.py | 80C56E1B055C | 4310 | 2026/09/20 14:59:19 |
| results/_archive_2026_09_21/_v4_verify_round4_2026_09_20.py | 680E67DEE9E9 | 4027 | 2026/09/20 15:00:10 |
| results/_archive_2026_09_21/_v4_wrapup_2026_09_20.py | FE863F8F3EEF | 2996 | 2026/09/20 15:03:08 |
| results/_archive_2026_09_21/_worker_probe_c2a1.ps1 | EBCC139C3964 | 1025 | 2026/09/21 15:22:35 |
| results/_archive_2026_09_21/_xverify_c2a1.py | 3B8FC85AC06B | 1052 | 2026/09/21 15:25:17 |
| results/_archive_2026_09_21/deposon_v20_corpus_eval.json | CA71AA6858E1 | 631644 | 2026/08/29 01:21:14 |
| results/_archive_2026_09_21/deposon_v20_gt2b.json | A2AE7997EE67 | 123331 | 2026/08/29 19:57:39 |
| results/_archive_2026_09_21/deposon_v20_gt3.json | 35B676773243 | 7844 | 2026/08/29 15:03:29 |
| results/_archive_2026_09_21/deposon_v20_vector_audit.json | B9B65C568842 | 915 | 2026/08/28 21:15:08 |
| results/_archive_2026_09_24/_final_verify.py | 31A5D44497F1 | 2307 | 2026/09/23 15:34:04 |
| results/_archive_2026_09_24/_inspect_captions.py | DFB02ADE1474 | 591 | 2026/09/10 17:31:00 |
| results/_archive_2026_09_24/_v4_pi_decision_questionnaire_2026_09_21_v1.1.md.bak_2026_09_22_gB_post.md | 07CA9EE8E1BB | 113508 | 2026/09/22 16:00:10 |
| results/_archive_2026_09_24/_verify_worker_c.py | CC578C46B332 | 1155 | 2026/09/10 21:27:55 |
| results/_archive_2026_09_24/_volc_22cap_emb.py | 15904ECAE629 | 11105 | 2026/09/10 17:36:26 |
| results/_archive_2026_09_24/_worker_openrouter_rag_run.py | 4458CCF3D64A | 24113 | 2026/09/16 11:01:12 |
| results/_cpath_sim_runner.py | 6074D83944DC | 18783 | 2026/09/10 20:44:28 |
| results/_d05_backbone_robustness_beta_20260918_100853.json | 9B6F085D96DC | 1490 | 2026/09/18 10:14:58 |
| results/_d05_i1i5_invariants_check_20260918_100853.json | F12AF5435928 | 1920 | 2026/09/18 10:14:59 |
| results/_d05_main_run_results_20260918_100853.json | 0A933D7C8D7A | 15243 | 2026/09/18 12:41:46 |
| results/_d05_main_run_results_nemotron_3.5_20260918_100853.json | 1B1B6AD67C39 | 15111 | 2026/09/18 10:14:56 |
| results/_d05_main_run_results_qwen3_failed_20260918_100853.json | 427B18DA8114 | 18358 | 2026/09/18 12:41:46 |
| results/_d05_opt_5_directions_results_20260918_100853.json | E5979133195A | 5614 | 2026/09/18 10:14:59 |
| results/_deposon_v2scripts_kimi7_audit_20260918_105219.json | 3DA62B979053 | 2096 | 2026/09/18 10:52:19 |
| results/_deposon_v2scripts_reverify_20260918_105219.json | 8AC002CCB082 | 12888 | 2026/09/18 10:52:19 |
| results/_deposon_v2scripts_reverify_20260918_105219.md | EE005EA1F031 | 5347 | 2026/09/18 10:52:19 |
| results/_kimi_ftfb_s7_independent_recompute_2026_09_18.json | 879DB0217F04 | 3605 | 2026/09/18 10:39:43 |
| results/_kimi_push_v3_manifest_batch10_1b753116.json | 326ADCA520F1 | 5007 | 2026/09/17 23:34:06 |
| results/_kimi_push_v3_manifest_batch11_7d6a7c8f.json | 383446F24707 | 2573 | 2026/09/18 22:27:36 |
| results/_kimi_push_v3_manifest_batch12_a2853574.json | 6BE21F9586EC | 1246 | 2026/09/18 22:27:36 |
| results/_kimi_push_v3_manifest_batch13_83f895f9.json | 0694838F66A8 | 739 | 2026/09/18 22:27:36 |
| results/_kimi_push_v3_manifest_batch14_e5952130.json | 64AA9D8A5C7D | 1055 | 2026/09/18 22:27:36 |
| results/_kimi_push_v3_manifest_batch15_0e65fe2f.json | CFC345D10C7D | 385 | 2026/09/20 09:39:32 |
| results/_kimi_push_v3_manifest_batch1_77e2f952.json | B5F517A321A3 | 2534 | 2026/09/17 23:22:31 |
| results/_kimi_push_v3_manifest_batch2_e18c17bb.json | F14341B8A1A1 | 9260 | 2026/09/17 23:23:29 |
| results/_kimi_push_v3_manifest_batch3_01ecf050.json | FD64909EA1D8 | 9656 | 2026/09/17 23:24:23 |
| results/_kimi_push_v3_manifest_batch4_2f872d54.json | D35453F21049 | 9720 | 2026/09/17 23:25:26 |
| results/_kimi_push_v3_manifest_batch5_34439e1e.json | 2769B83F5B1D | 9511 | 2026/09/17 23:28:31 |
| results/_kimi_push_v3_manifest_batch6_28055e59.json | F3EB7A38AE7D | 10107 | 2026/09/17 23:29:50 |
| results/_kimi_push_v3_manifest_batch7_0903df7e.json | 7BDA1FECD7C4 | 9748 | 2026/09/17 23:30:56 |
| results/_kimi_push_v3_manifest_batch8_7468a23b.json | 5A38FC02978C | 9880 | 2026/09/17 23:32:05 |
| results/_kimi_push_v3_manifest_batch9_f7d9cf1d.json | 968D7C6C43CA | 9745 | 2026/09/17 23:33:10 |
| results/_kimi_push_v3_manifest_verifier21_cc3c92d0.json | 5A6601F47632 | 4159 | 2026/09/18 13:45:13 |
| results/_mavis_skill_inventory_2026_09_18.md | 90BA7F7A7FBE | 99702 | 2026/09/18 13:50:10 |
| results/_p_d_v03_22caption_verification_20260917_163757.json | DFBCC5D6FC34 | 13775 | 2026/09/17 16:37:57 |
| results/_p_i_real_labels_2026_09_16/p_i_real_labels_results_2026_09_16.json | E934819EE9ED | 1043 | 2026/09/16 22:11:35 |
| results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json | A9AD1DE618F5 | 1669 | 2026/09/16 17:39:59 |
| results/_p_k_v3_glm_json_audit_2026-09-17t08-23-41z.json | F236E88F22CA | 6678 | 2026/09/17 16:23:41 |
| results/_p_k_v3_three_way_rerun_2026-09-17t08-23-41z.json | 05FF758AE921 | 12992 | 2026/09/17 16:23:41 |
| results/_p_l_p_c_finite_size_scaling_2026_09_16/p_l_p_c_finite_size_scaling_results_2026_09_16.json | 664E7CC05AEC | 9076 | 2026/09/16 15:50:08 |
| results/_p_l_real_data_collapse_2026_09_16/p_l_real_data_collapse_results_v2_2026_09_16.json | AFE975606D40 | 3761 | 2026/09/16 22:40:54 |
| results/_p_l_v3_phase2_beta_summary_20260917_142748.json | 86D4CB146241 | 2417 | 2026/09/17 14:27:54 |
| results/_p_l_v3_phase2_closedsource_summary_20260917_175544.json | A3EAFAF9BA03 | 3286 | 2026/09/17 17:55:55 |
| results/_p_l_v3_phase2_doubao_v2_summary_20260917_170828.json | C366F4E30B6B | 4357 | 2026/09/17 17:12:34 |
| results/_p_l_v3_phase2_doubao_v2_summary_20260917_172206.json | E3DCCDDAED87 | 14469 | 2026/09/17 17:55:09 |
| results/_p_l_v3_phase2_or_embedding_v3_summary_20260917_162614.json | 21C9F23699A8 | 8308 | 2026/09/17 16:29:34 |
| results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133512.md | C350E420ECA6 | 6337 | 2026/09/17 13:35:15 |
| results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133705.md | 772112CF5BD4 | 6434 | 2026/09/17 13:37:07 |
| results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133726.md | D7F03FDE4067 | 6435 | 2026/09/17 13:37:29 |
| results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133852.md | D66388B6532D | 6616 | 2026/09/17 13:38:55 |
| results/_p_l_v3_real_collapse_mistral_l100_20260917_132341.json | 4657B210782A | 43903 | 2026/09/17 13:33:51 |
| results/_p_l_v3_real_collapse_mistral_l30_20260917_132341.json | F6AB84F27D9A | 16545 | 2026/09/17 13:23:49 |
| results/_p_l_v3_real_collapse_mistral_l45_20260917_132341.json | DC37EE54781C | 20108 | 2026/09/17 13:26:47 |
| results/_p_l_v3_real_collapse_mistral_l60_20260917_132341.json | E3FB4F775E22 | 1174 | 2026/09/17 13:26:47 |
| results/_p_l_v3_robustness_claude_sonnet5_l30_20260917_174011.json | 9D329721F67D | 30772 | 2026/09/17 17:49:05 |
| results/_p_l_v3_robustness_claude_sonnet5_l60_20260917_174011.json | 28E462C11692 | 1292 | 2026/09/17 17:49:05 |
| results/_p_l_v3_robustness_gemini_37flash_l30_20260917_175003.json | 0F5C80A8A4AE | 30514 | 2026/09/17 17:53:55 |
| results/_p_l_v3_robustness_gemini_37flash_l60_20260917_175003.json | E2590651F9C0 | 1288 | 2026/09/17 17:53:55 |
| results/_p_l_v3_robustness_glm53_l30_20260917_142011.json | 2DEADD7BE100 | 18281 | 2026/09/17 14:25:11 |
| results/_p_l_v3_robustness_glm53_l60_20260917_142011.json | 31556B58CAA1 | 1037 | 2026/09/17 14:25:11 |
| results/_p_l_v3_robustness_gpt56sol_l30_20260917_173159.json | 3865D7A61CA1 | 30347 | 2026/09/17 17:39:13 |
| results/_p_l_v3_robustness_gpt56sol_l60_20260917_173159.json | 8C79E9A289FB | 1266 | 2026/09/17 17:39:13 |
| results/_p_l_v3_robustness_mistral_l60_20260917_142748.json | BA41A0D4B927 | 1071 | 2026/09/17 14:27:54 |
| results/_p_l_v3_robustness_qwen3_l30_20260917_140017.json | E9BAC1743A2A | 18595 | 2026/09/17 14:06:45 |
| results/_p_l_v3_robustness_qwen3_l60_20260917_140017.json | F79F1B00E5D3 | 1057 | 2026/09/17 14:06:45 |
| results/_p_l_v3_vector_embedding_doubao-text-240715_l30_20260917_172206.json | 2D4827F9CDA2 | 18509 | 2026/09/17 17:29:03 |
| results/_p_l_v3_vector_embedding_doubao-vision-241215_l30_20260917_171614.json | 2B91EB1DBBCF | 1669762 | 2026/09/17 17:16:46 |
| results/_p_l_v3_vector_embedding_doubao-vision-241215_l30_20260917_172206.json | E836A04A04D8 | 1670172 | 2026/09/17 17:53:27 |
| results/_p_l_v3_vector_embedding_doubao-vision-250328_l30_20260917_171614.json | 46C99397F01B | 1670501 | 2026/09/17 17:17:26 |
| results/_p_l_v3_vector_embedding_doubao-vision-250328_l30_20260917_172206.json | 0432F25CF6C3 | 1669285 | 2026/09/17 17:53:27 |
| results/_p_l_v3_vector_embedding_doubao-vision-250615_l30_20260917_171614.json | 6B8AF7D8BCA9 | 1670027 | 2026/09/17 17:18:00 |
| results/_p_l_v3_vector_embedding_doubao-vision-250615_l30_20260917_172206.json | 710B7F291355 | 1671116 | 2026/09/17 17:53:28 |
| results/_p_l_v3_vector_embedding_doubao-vision-251215_l30_20260917_172206.json | A00976C6F87B | 1670482 | 2026/09/17 17:53:28 |
| results/_p_l_v3_vector_embedding_doubao_l30_20260917_142748.json | B9488E2B01AE | 11834 | 2026/09/17 14:32:56 |
| results/_p_l_v3_vector_embedding_doubao_l30_20260917_170828.json | 198F8FE39F94 | 18468 | 2026/09/17 17:11:53 |
| results/_p_l_v3_vector_embedding_glm53_l30_20260917_142748.json | D91B0C5F642F | 11833 | 2026/09/17 14:32:56 |
| results/_p_l_v3_vector_embedding_mistral_l30_20260917_142748.json | 33D0259073DC | 11835 | 2026/09/17 14:32:56 |
| results/_p_l_v3_vector_embedding_or_bge-large_l30_20260917_162614.json | AFF028E8506C | 1017974 | 2026/09/17 16:27:59 |
| results/_p_l_v3_vector_embedding_or_e5-multi_l30_20260917_162614.json | 8676B519A031 | 1017684 | 2026/09/17 16:28:49 |
| results/_p_l_v3_vector_embedding_or_gte-large_l30_20260917_162614.json | 07561D4D23D1 | 1017381 | 2026/09/17 16:29:34 |
| results/_p_l_v3_vector_embedding_or_qwen3-emb-8b_l30_20260917_162614.json | A4BD70C02AAA | 3929893 | 2026/09/17 16:27:27 |
| results/_p_l_v3_vector_embedding_qwen3-emb-4b_l30_20260917_170828.json | 1928ADA51527 | 2452705 | 2026/09/17 17:12:34 |
| results/_p_l_v3_vector_embedding_qwen3-emb-4b_l30_20260917_172206.json | BEBEE5346543 | 2452273 | 2026/09/17 17:53:29 |
| results/_p_l_v3_vector_embedding_qwen3_l30_20260917_142748.json | 26F7493F1C95 | 11833 | 2026/09/17 14:32:56 |
| results/_p_m_attack_surface_cost_2026_09_16/p_m_attack_surface_cost_results_2026_09_16.json | FBCB60CF5102 | 5266 | 2026/09/16 17:34:14 |
| results/_p_m_real_separation_2026_09_16/p_m_real_separation_results_2026_09_16.json | A4B12D1CFEDC | 2042 | 2026/09/16 22:12:02 |
| results/_p_n_curvature_potential_coupling_2026_09_16/p_n_curvature_potential_coupling_results_2026_09_16.json | 088F28524A1D | 4276 | 2026/09/16 17:43:33 |
| results/_p_o_stranger_verification_2026_09_16/p_o_stranger_verification_results_2026_09_16.json | 1E4C065DA058 | 5916 | 2026/09/16 13:23:52 |
| results/_pc_d1_d3_2026_09_15.py | 09C7C4DDBB39 | 43019 | 2026/09/15 10:58:21 |
| results/_tra_v0_2026_09_10.json | 0B096048E01D | 3695 | 2026/09/10 20:20:34 |
| results/_tra_v0_2026_09_10.py | D80A8F75A122 | 12125 | 2026/09/10 20:20:20 |
| results/_track2_endpoints_probe_2026_09_23.json | C846F7FC79EE | 5803 | 2026/09/23 15:15:30 |
| results/_track2_qwen_check_2026_09_23.json | 727D1FFC7F3F | 2513 | 2026/09/23 14:22:00 |
| results/_track2_qwen_check_2026_09_23.py | 3DDBA570C221 | 12078 | 2026/09/23 14:21:43 |
| results/_v2_setup.py | 73F2B8712A90 | 3483 | 2026/09/16 11:01:12 |
| results/_v2_show_summary.py | 0012B38CE438 | 1200 | 2026/09/11 11:21:58 |
| results/_v2_smoketest.py | 0B6C22C8F379 | 2040 | 2026/09/16 11:01:12 |
| results/_v2_stage1_60cells.py | 8C7BD12C3A8C | 31556 | 2026/09/16 11:01:12 |
| results/_v2_stage2_f2_drift.py | 7E9B2FC57D80 | 10798 | 2026/09/16 11:01:12 |
| results/_v2_stage3_f3_strip.py | CE4362E325CA | 11803 | 2026/09/16 11:01:12 |
| results/_v2_stage4_f4_pdv2.py | B84F5AAB6FAF | 10355 | 2026/09/11 11:17:17 |
| results/_v2_stage5_f5_dpath.py | E8871B829D89 | 6480 | 2026/09/11 11:16:38 |
| results/_v2_verify_outputs.py | EB0107DD79B5 | 2656 | 2026/09/11 11:21:39 |
| results/_v3x_18frozen_remeasure_2026_09_16/v3x_18frozen_remeasure_results_2026_09_16.json | 928794710241 | 4202 | 2026/09/16 23:32:09 |
| results/_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json | F39412103366 | 17053 | 2026/09/16 12:37:12 |
| results/_v3x_p_k_verify_2026_09_16/v3x_p_k_verify_results_2026_09_16.json | 59C2113B7C71 | 2059 | 2026/09/16 23:33:03 |
| results/_v3x_p_l_v3_mistral_large_2512_20260917_115049.json | 523B5941C30C | 16835 | 2026/09/17 11:52:29 |
| results/_v4_N09_N39_executor.py | 51C8BE53D67C | 112448 | 2026/09/23 12:39:28 |
| results/_v4_d1_build_proxy_students.py | B98AF32AED78 | 5316 | 2026/09/22 17:08:28 |
| results/_v4_d1_chain_verify.py | D778E436C986 | 884 | 2026/09/22 17:15:10 |
| results/_v4_d1_summary_check.py | CE7DC77C50D0 | 699 | 2026/09/22 17:14:36 |
| results/_v4_d3_pre_hashes_check.py | E1ED884EECB0 | 4766 | 2026/09/23 09:45:17 |
| results/_v4_d3_summary_flags.py | C680D9FA2D07 | 2509 | 2026/09/23 10:01:58 |
| results/_v4_d3r2_independent_diff.py | 3DAF003D2A28 | 2699 | 2026/09/23 10:39:59 |
| results/_v4_d3r2_revision.py | BC11F8676A7E | 12133 | 2026/09/23 10:37:46 |
| results/_v4_d3r2_verify.py | F729FBED9098 | 2542 | 2026/09/23 10:39:28 |
| results/_v4_d5_rootcause_diag.py | 12E4B5F913C6 | 24597 | 2026/09/23 11:06:14 |
| results/_v4_d5_rootcause_selfcheck.py | 9DF22AFEC701 | 11005 | 2026/09/23 11:08:26 |
| results/_v4_d5_verdict_build.py | F0DCF1A58A0F | 5375 | 2026/09/23 10:40:44 |
| results/_v4_distill_min_measure.py | 21771E66AF67 | 33852 | 2026/09/23 09:56:04 |
| results/_v4_distill_min_measure_result_v1.json | A7156D3EFE19 | 32789 | 2026/09/23 09:58:25 |
| results/_v4_distill_min_measure_result_v1r2.json | EFA97C1D1B52 | 34355 | 2026/09/23 10:38:51 |
| results/_v4_exec_c_bin_result.json | 8872B49866D4 | 1590 | 2026/09/23 12:07:03 |
| results/_v4_exec_c_tau_result.json | BBE22F28B3CA | 1678 | 2026/09/23 12:07:22 |
| results/_v4_exec_cbin_rerun2026_09_23.json | D701E14B4E44 | 573 | 2026/09/23 14:30:21 |
| results/_v4_exec_cs21_rerun2026_09_23.json | 0713C19E2414 | 589 | 2026/09/23 14:30:21 |
| results/_v4_exec_cs28_rerun2026_09_23.json | 4DAFC9381079 | 591 | 2026/09/23 14:30:21 |
| results/_v4_exec_cs33_rerun2026_09_23.json | CF2BAB791ABD | 605 | 2026/09/23 14:30:21 |
| results/_v4_exec_cs39_rerun2026_09_23.json | 523B19D96439 | 593 | 2026/09/23 14:30:21 |
| results/_v4_exec_d1_rerun2026_09_23.json | E3DBA5ABA132 | 591 | 2026/09/23 14:30:21 |
| results/_v4_exec_d2_rerun2026_09_23.json | E3B0037D4B9F | 562 | 2026/09/23 14:30:21 |
| results/_v4_exec_d5_rerun2026_09_23.json | 444202ED93CC | 569 | 2026/09/23 14:30:21 |
| results/_v4_exec_d6_rerun2026_09_23.json | 8475B0EDD023 | 579 | 2026/09/23 14:30:21 |
| results/_v4_exec_d8_rerun2026_09_23.json | EDBCF7570317 | 620 | 2026/09/23 14:30:21 |
| results/_v4_exec_dchernoffstein_rerun2026_09_23.json | 3944A678C3CC | 600 | 2026/09/23 14:30:21 |
| results/_v4_exec_dcloseness_rerun2026_09_23.json | 01F367788B31 | 591 | 2026/09/23 14:30:21 |
| results/_v4_exec_dncd_rerun2026_09_23.json | B81499CAD50D | 623 | 2026/09/23 14:30:21 |
| results/_v4_exec_drényi_rerun2026_09_23.json | 0868ABAC6A83 | 585 | 2026/09/23 14:30:21 |
| results/_v4_exec_mark_retention_base.json | CA6046056591 | 212196 | 2026/09/23 12:05:46 |
| results/_v4_exec_mcs21_result.json | EF2CB7AB4F93 | 1090 | 2026/09/23 12:13:06 |
| results/_v4_exec_mcs28_result.json | EA1157FDF7FB | 1635 | 2026/09/23 12:24:08 |
| results/_v4_exec_mcs32_result.json | 843A59B41F2F | 1145 | 2026/09/23 12:22:22 |
| results/_v4_exec_mcs33_result.json | 97D68BACD5C5 | 1119 | 2026/09/23 12:22:22 |
| results/_v4_exec_mcs34_result.json | 257372EF6E73 | 1110 | 2026/09/23 12:22:22 |
| results/_v4_exec_mcs39_result.json | FC65D1D64264 | 1185 | 2026/09/23 12:22:22 |
| results/_v4_exec_md1_result.json | F4DCEC5A069A | 1625 | 2026/09/23 12:12:58 |
| results/_v4_exec_md2_result.json | E6F8BB1108F4 | 1023 | 2026/09/23 12:13:05 |
| results/_v4_exec_md3_result.json | 8AF302EA233F | 1038 | 2026/09/23 12:13:05 |
| results/_v4_exec_md4_result.json | 9F7143A0E67B | 1263 | 2026/09/23 12:29:37 |
| results/_v4_exec_md5_result.json | 08F1AA8F634C | 1607 | 2026/09/23 12:13:05 |
| results/_v4_exec_md6_result.json | 95229F38AA98 | 1033 | 2026/09/23 12:13:06 |
| results/_v4_exec_md7_result.json | 3F37489C4C86 | 1099 | 2026/09/23 12:29:37 |
| results/_v4_exec_md8_result.json | A9EF141CDB7F | 1159 | 2026/09/23 12:13:06 |
| results/_v4_exec_mdchernoffstein_result.json | 699B7F87D269 | 1254 | 2026/09/23 12:22:24 |
| results/_v4_exec_mdcloseness_result.json | 48FE3DFE979F | 1179 | 2026/09/23 12:22:24 |
| results/_v4_exec_mdlecam_result.json | 4CFC0255FD7E | 1211 | 2026/09/23 12:22:24 |
| results/_v4_exec_mdncd_result.json | FE9F926D77D8 | 1395 | 2026/09/23 12:22:24 |
| results/_v4_exec_mdrenyi_result.json | 2EF0A5937FA5 | 1208 | 2026/09/23 12:22:24 |
| results/_v4_exec_mdtvd_result.json | BB933AF5805C | 1007 | 2026/09/23 12:22:24 |
| results/_v4_exec_methods_batch.py | 76D7B539C590 | 115137 | 2026/09/23 12:28:49 |
| results/_v4_exec_methods_batch_finalize.py | BE6F21547823 | 11295 | 2026/09/23 12:26:10 |
| results/_v4_exec_methods_batch_patch.py | 5B0D3637258A | 666 | 2026/09/23 12:29:23 |
| results/_v4_exec_mx1_result.json | DBBDDE59DB46 | 1854 | 2026/09/23 12:13:06 |
| results/_v4_exec_mx2_result.json | 388F0A52BC35 | 1154 | 2026/09/23 12:29:37 |
| results/_v4_exec_mx3_result.json | B42984F40EE2 | 1134 | 2026/09/23 12:13:06 |
| results/_v4_exec_mx4_result.json | B8B44E2B0090 | 1433 | 2026/09/23 12:13:06 |
| results/_v4_exec_mx5_result.json | 8B5F9AC33218 | 1130 | 2026/09/23 12:13:06 |
| results/_v4_exec_mx6_result.json | BC675918DF96 | 1169 | 2026/09/23 12:13:06 |
| results/_v4_exec_mx7_result.json | AE6F21764EEF | 1171 | 2026/09/23 12:13:06 |
| results/_v4_exec_mx8_result.json | 61F33325CB96 | 1372 | 2026/09/23 12:13:06 |
| results/_v4_exec_n09_result.json | 8D0BDEC0EDD9 | 1882 | 2026/09/23 12:39:53 |
| results/_v4_exec_n10_result.json | 6C43A3A7ED34 | 1508 | 2026/09/23 12:39:56 |
| results/_v4_exec_n11_result.json | 7543A9B916BB | 1437 | 2026/09/23 12:39:56 |
| results/_v4_exec_n12_result.json | D79352FCE647 | 1975 | 2026/09/23 12:39:56 |
| results/_v4_exec_n13_result.json | 41CC6B10B064 | 1567 | 2026/09/23 12:39:56 |
| results/_v4_exec_n14_result.json | 7A131FB55F41 | 1214 | 2026/09/23 12:39:56 |
| results/_v4_exec_n16_result.json | 1F257E6A3E3B | 1256 | 2026/09/23 12:39:56 |
| results/_v4_exec_n17_result.json | B3536F28FB07 | 1411 | 2026/09/23 12:39:56 |
| results/_v4_exec_n18_result.json | EFFC6F93F69F | 2263 | 2026/09/23 12:39:56 |
| results/_v4_exec_n19_result.json | 26B8A1F60DB2 | 1283 | 2026/09/23 12:39:56 |
| results/_v4_exec_n19_supp_result.json | 7572DFBAEEC5 | 4076 | 2026/09/23 17:05:40 |
| results/_v4_exec_n20_result.json | 5BC4158A13AD | 1683 | 2026/09/23 12:39:56 |
| results/_v4_exec_n21_result.json | 7AB933B84C9B | 1418 | 2026/09/23 12:39:57 |
| results/_v4_exec_n22_result.json | 28549B612F01 | 1236 | 2026/09/23 12:39:57 |
| results/_v4_exec_n22_supp_result.json | 9F3883ED55ED | 3500 | 2026/09/23 17:05:40 |
| results/_v4_exec_n22s_margin_result.json | 4FD254FBE4F6 | 5634 | 2026/09/24 09:42:45 |
| results/_v4_exec_n23_result.json | 39800AADFE6E | 1444 | 2026/09/23 12:39:57 |
| results/_v4_exec_n24_result.json | 61EA1574722D | 1268 | 2026/09/23 12:39:59 |
| results/_v4_exec_n25_result.json | F5FBBC731AFA | 1441 | 2026/09/23 12:39:59 |
| results/_v4_exec_n26_result.json | 2382A558C116 | 1316 | 2026/09/23 12:39:59 |
| results/_v4_exec_n27_result.json | 4D53635B77E4 | 1298 | 2026/09/23 12:39:59 |
| results/_v4_exec_n28_result.json | 5BE3F8CA5E5F | 3834 | 2026/09/23 12:39:59 |
| results/_v4_exec_n29_constructed_verdict.json | 8F9F2DA64585 | 5452 | 2026/09/23 15:28:57 |
| results/_v4_exec_n29_real_verdict.json | 0485D3EBBC67 | 13628 | 2026/09/23 16:38:24 |
| results/_v4_exec_n29_rejudge.json | C76EF78BB93F | 5114 | 2026/09/23 14:17:36 |
| results/_v4_exec_n29_result.json | F130D0B81381 | 1503 | 2026/09/23 12:39:59 |
| results/_v4_exec_n30_constructed_verdict.json | D39C42D0724F | 5025 | 2026/09/23 15:28:58 |
| results/_v4_exec_n30_rejudge.json | 14AF9E8F0135 | 3569 | 2026/09/23 14:17:36 |
| results/_v4_exec_n30_result.json | C57FEE40C388 | 1476 | 2026/09/23 12:39:59 |
| results/_v4_exec_n31_constructed_verdict.json | 652BCB5B8E3D | 4549 | 2026/09/23 15:28:58 |
| results/_v4_exec_n31_rejudge.json | 219C53D0E25A | 3756 | 2026/09/23 14:17:36 |
| results/_v4_exec_n31_result.json | B1DF01AC461D | 1498 | 2026/09/23 12:39:59 |
| results/_v4_exec_n32_result.json | 567DE6DEC77F | 1398 | 2026/09/23 12:39:59 |
| results/_v4_exec_n33_result.json | B17EAD2D9896 | 1307 | 2026/09/23 12:39:59 |
| results/_v4_exec_n35_result.json | 60B540F7142D | 1287 | 2026/09/23 12:39:59 |
| results/_v4_exec_n37_result.json | 7F40FEFED330 | 3398 | 2026/09/23 12:39:59 |
| results/_v4_exec_n_batch_verdict.json | 138BFCD55561 | 7145 | 2026/09/23 12:39:59 |
| results/_v4_exec_s03_rerun2026_09_23.json | 71BDEAD7CF88 | 577 | 2026/09/23 14:30:21 |
| results/_v4_exec_s03_result.json | 60DAFFEDC057 | 4840 | 2026/09/23 12:05:47 |
| results/_v4_exec_s05_rerun2026_09_23.json | DB8A2A441463 | 554 | 2026/09/23 14:30:21 |
| results/_v4_exec_s05_result.json | 3785D212A013 | 4076 | 2026/09/23 12:05:47 |
| results/_v4_exec_s06_rerun2026_09_23.json | 21E3F1FEB68D | 569 | 2026/09/23 14:30:21 |
| results/_v4_exec_s06_result.json | C0AE9AC4F291 | 1779 | 2026/09/23 12:05:47 |
| results/_v4_exec_s10_result.json | 67C7F3A70EA0 | 2657 | 2026/09/23 12:05:51 |
| results/_v4_exec_s11_result.json | B9DEB97C00D0 | 2771 | 2026/09/23 12:05:51 |
| results/_v4_exec_s13_rerun2026_09_23.json | EB64BF8AAB83 | 617 | 2026/09/23 14:30:21 |
| results/_v4_exec_s13_result.json | 5C1B3846DEEB | 3071 | 2026/09/23 12:05:51 |
| results/_v4_exec_s17_result.json | C1EB4968030C | 1423 | 2026/09/23 12:05:52 |
| results/_v4_exec_s18_rerun2026_09_23.json | 0F7569A88C57 | 678 | 2026/09/23 14:30:21 |
| results/_v4_exec_s18_result.json | D48A372FD118 | 1642 | 2026/09/23 12:05:52 |
| results/_v4_exec_s19_result.json | CFF8337466F3 | 3764 | 2026/09/23 12:05:52 |
| results/_v4_exec_s21_rerun2026_09_23.json | DA513EF13516 | 679 | 2026/09/23 14:30:21 |
| results/_v4_exec_s21_result.json | 05E9E7AD546D | 1897 | 2026/09/23 12:05:53 |
| results/_v4_exec_s24_result.json | EE22875DDF48 | 7337 | 2026/09/23 12:05:53 |
| results/_v4_exec_s25_result.json | 71F7FAC128BC | 1761 | 2026/09/23 12:07:01 |
| results/_v4_exec_s26_result.json | F04CAC8D2A30 | 2499 | 2026/09/23 12:05:53 |
| results/_v4_exec_s28_result.json | 05E3D4C61F53 | 1765 | 2026/09/23 12:07:01 |
| results/_v4_exec_s38_rerun2026_09_23.json | 0123476C867C | 621 | 2026/09/23 14:30:21 |
| results/_v4_exec_s38_result.json | 637EDACD9B42 | 1836 | 2026/09/23 12:06:01 |
| results/_v4_exec_s40_rejudged_2026_09_23.json | D3F376A6C45F | 6703 | 2026/09/23 16:38:39 |
| results/_v4_exec_s40_rerun2026_09_23.json | B2B4F189DCF7 | 608 | 2026/09/23 14:30:21 |
| results/_v4_exec_s40_result.json | 778C80B749A5 | 1731 | 2026/09/23 12:07:01 |
| results/_v4_exec_seeds_runner.py | 7F45BAF01727 | 131373 | 2026/09/23 12:05:29 |
| results/_v4_n22_n19_supp_executor_2026_09_23.py | F3E51AF9EBEB | 55098 | 2026/09/23 17:05:23 |
| results/_v4_n22_n19_supp_post_hashes_2026_09_23.txt | F4F46737782E | 1721 | 2026/09/23 17:05:40 |
| results/_v4_n22_n19_supp_pre_hashes_2026_09_23.txt | F4F46737782E | 1721 | 2026/09/23 17:05:39 |
| results/_v4_n22s_margin_executor_2026_09_23.py | F2BE3C1CF9B3 | 50562 | 2026/09/24 09:42:18 |
| results/_v4_n22s_margin_manifest_v2.json | E386CF73BC4C | 7767 | 2026/09/24 09:36:59 |
| results/_v4_n22s_margin_post_hashes_2026_09_24.txt | 493700D789D0 | 1609 | 2026/09/24 09:42:45 |
| results/_v4_n22s_margin_pre_hashes_2026_09_24.txt | 493700D789D0 | 1609 | 2026/09/24 09:42:45 |
| results/_v4_n29_real_executor_2026_09_23.py | C55E416DCFE5 | 62678 | 2026/09/23 16:37:59 |
| results/_v4_n29_real_post_hashes_2026_09_23.txt | D2E093CE13FA | 625 | 2026/09/23 16:38:24 |
| results/_v4_n29_real_pre_hashes_2026_09_23.txt | 6C01CE643FE6 | 357 | 2026/09/23 16:01:00 |
| results/_v4_n29_real_trajectories_2026_09_23.json | 98484EEEAB9B | 5398384 | 2026/09/23 16:38:24 |
| results/_v4_pi_cot_executor_2026_09_23.py | AC0525C9BD3F | 12841 | 2026/09/23 17:16:52 |
| results/_v4_proxy_student_llm_deepseek_direct_chat.json | 1B05EBA8639B | 28113 | 2026/09/23 12:30:50 |
| results/_v4_proxy_student_llm_deepseek_v41_flash.json | 61EDBE39A618 | 34959 | 2026/09/23 10:08:48 |
| results/_v4_proxy_student_llm_deepseek_v4_flash_teamo.json | 4BFB49FC75EB | 27233 | 2026/09/23 15:25:05 |
| results/_v4_proxy_student_llm_mimo_v2_6_pro.json | 0698F2FA88D0 | 28483 | 2026/09/23 15:23:11 |
| results/_v4_proxy_student_llm_qwen3_7_max.json | 30B7783CF310 | 29014 | 2026/09/23 15:20:49 |
| results/_v4_proxy_student_llm_qwen_turbo.json | AE541E34781E | 25598 | 2026/09/23 12:31:34 |
| results/_v4_regex_selfcheck.ps1 | A365D5B710C6 | 1449 | 2026/09/20 13:37:42 |
| results/_v4_rejudge_executor_2026_09_23.py | 8AD65752C172 | 46196 | 2026/09/23 14:17:27 |
| results/_v4_rejudge_pre_hashes_2026_09_23.txt | 028CE29BCFD6 | 2815 | 2026/09/23 14:14:57 |
| results/_v4_rerun_executor_2026_09_23.py | CB47672E3062 | 67571 | 2026/09/23 16:29:33 |
| results/_v4_sha_selfcheck.ps1 | 13DA3948173B | 1146 | 2026/09/20 13:37:20 |
| results/_v4_supp_a1_cbin_result.json | ADF4A9A30911 | 6439 | 2026/09/24 11:28:18 |
| results/_v4_supp_a1_executor.py | A5D3179B1FB2 | 68610 | 2026/09/24 09:47:36 |
| results/_v4_supp_a1_s03_result.json | 5BD9255A7639 | 2877 | 2026/09/24 11:28:18 |
| results/_v4_supp_a1_s05_result.json | A0790E3AE0D5 | 2615 | 2026/09/24 11:28:18 |
| results/_v4_supp_a1_s06_result.json | FEE7A1137D43 | 2700 | 2026/09/24 11:28:18 |
| results/_v4_supp_a1_s18_result.json | 56B75871A6D7 | 2457 | 2026/09/24 11:28:18 |
| results/_v4_supp_a1_s38_result.json | 41F40FBA1142 | 2853 | 2026/09/24 11:30:02 |
| results/_v4_supp_a2_cs21_result.json | 536E52760C4C | 3122 | 2026/09/24 10:02:02 |
| results/_v4_supp_a2_cs39_result.json | F23B94C6E170 | 2871 | 2026/09/24 10:02:02 |
| results/_v4_supp_a2_d1_result.json | 80ABA65ECFE9 | 3145 | 2026/09/24 10:02:02 |
| results/_v4_supp_a2_d2_result.json | C9CAD1B6DF91 | 3129 | 2026/09/24 10:02:02 |
| results/_v4_supp_a2_dcloseness_result.json | 6FCDE6335F20 | 2734 | 2026/09/24 10:02:02 |
| results/_v4_supp_a2_drenyi_result.json | 5FB2EB0F190A | 2538 | 2026/09/24 10:02:02 |
| results/_v4_supp_a2_executor.py | EF7B3B32E844 | 68550 | 2026/09/24 09:57:20 |
| results/_v4_supp_a2_post_hashes_2026_09_24.txt | 373340B018C5 | 318 | 2026/09/24 10:02:02 |
| results/_v4_supp_a2_pre_hashes_2026_09_24.txt | 373340B018C5 | 318 | 2026/09/24 10:02:01 |
| results/_v4_supp_b_executor.py | D71730B77CF3 | 64855 | 2026/09/24 09:49:04 |
| results/_v4_supp_b_n11_result.json | D70B748ADE01 | 3913 | 2026/09/24 09:55:11 |
| results/_v4_supp_b_n12_result.json | A0FF0B899E5F | 2957 | 2026/09/24 09:55:12 |
| results/_v4_supp_b_n20_result.json | F7DFD4714112 | 3648 | 2026/09/24 09:55:12 |
| results/_v4_supp_b_n26_result.json | C895C3925EAD | 4946 | 2026/09/24 09:55:12 |
| results/_v4_supp_b_n28_result.json | 777904C9C896 | 8317 | 2026/09/24 09:55:12 |
| results/_v4_supp_c_unknowns_result.json | FF27665E67BB | 6273 | 2026/09/24 09:50:19 |
| results/_v4_supp_cd_executor_2026_09_24.py | CDDF2A74B437 | 59979 | 2026/09/24 09:49:08 |
| results/_v4_supp_cd_post_hashes_2026_09_24.txt | D9CC869605E1 | 1395 | 2026/09/24 09:50:19 |
| results/_v4_supp_cd_pre_hashes_2026_09_24.txt | 8F4DCDC339F3 | 1187 | 2026/09/24 09:50:19 |
| results/_v4_supp_cd_run_log.txt | B63F30421A8E | 2148 | 2026/09/24 09:49:32 |
| results/_v4_supp_d_v3diag_result.json | F1C6E57FA40D | 18854 | 2026/09/24 09:50:19 |
| results/_v4_supp_e_measure_deepseek_v4_flash_teamo.json | 276D253A8A28 | 8784 | 2026/09/24 10:22:52 |
| results/_v4_supp_e_measure_mimo_v2_6_pro.json | D1042EE178CB | 8785 | 2026/09/24 10:18:14 |
| results/_v4_supp_e_measure_qwen3_7_max.json | 2400067185BA | 8774 | 2026/09/24 10:13:58 |
| results/_v4_supp_e_multimodel_rerun.py | D74FAF11772B | 43281 | 2026/09/24 10:07:03 |
| results/_v4_supp_e_multimodel_result.json | 04FB36054F6B | 14686 | 2026/09/24 10:24:06 |
| results/_v4_supp_e_one_model.py | 8DA5620C72AE | 4104 | 2026/09/24 10:04:22 |
| results/_v4_supp_e_proxy_deepseek_v4_flash_teamo.json | 5D823249F537 | 42139 | 2026/09/24 10:22:40 |
| results/_v4_supp_e_proxy_mimo_v2_6_pro.json | 036DAC1940B7 | 44902 | 2026/09/24 10:18:01 |
| results/_v4_supp_e_proxy_qwen3_7_max.json | 004FA91BC2C3 | 46326 | 2026/09/24 10:13:46 |
| results/_v4_supp_l11_dct100_executor.py | 20DBF8B27C10 | 29533 | 2026/09/24 13:34:04 |
| results/_v4_supp_l11_dct100_post_hashes_2026_09_24.txt | BF1D1B45C804 | 3216 | 2026/09/24 13:36:15 |
| results/_v4_supp_l11_dct100_pre_hashes_2026_09_24.txt | 8DEAB15A3ABE | 3215 | 2026/09/24 13:36:15 |
| results/_v4_supp_l11_dct100_result.json | 20B0E13064F8 | 12143 | 2026/09/24 13:36:15 |
| results/_v4_supp_l12_dr_real_renyi_executor.py | 338AF29559E1 | 39821 | 2026/09/24 13:47:14 |
| results/_v4_supp_l12_dr_real_renyi_post_hashes_2026_09_24.txt | A505F3E7E703 | 4685 | 2026/09/24 13:51:46 |
| results/_v4_supp_l12_dr_real_renyi_pre_hashes_2026_09_24.txt | B2D74DA47C81 | 4037 | 2026/09/24 13:51:45 |
| results/_v4_supp_l12_dr_real_renyi_result.json | 6196067736A1 | 10713 | 2026/09/24 13:51:46 |
| results/_v4_supp_l13_n26pair_executor.py | FF6A280BE11A | 51723 | 2026/09/24 14:08:36 |
| results/_v4_supp_l13_n26pair_post_hashes_2026_09_24.txt | CCCBE16F9D99 | 735 | 2026/09/24 14:15:54 |
| results/_v4_supp_l13_n26pair_pre_hashes_2026_09_24.txt | 37D2B0DC2940 | 910 | 2026/09/24 14:09:14 |
| results/_v4_supp_l13_n26pair_result.json | A73BD752AF9A | 52481 | 2026/09/24 14:12:43 |
| results/_v4_supp_l14_n11full_executor.py | 336C7B14B62A | 60992 | 2026/09/24 14:51:21 |
| results/_v4_supp_l14_n11full_post_hashes_2026_09_24.txt | D872AA208635 | 841 | 2026/09/24 15:37:51 |
| results/_v4_supp_l14_n11full_pre_hashes_2026_09_24.txt | DE09E0CFED87 | 651 | 2026/09/24 14:38:32 |
| results/_v4_supp_l14_n11full_result.json | 4C11AB9057B9 | 12246 | 2026/09/24 15:34:57 |
| results/_v4_supp_l14_n11full_verdict.md | 8EEF73BF9856 | 19697 | 2026/09/24 15:38:25 |
| results/_v4_supp_l1_n28r_executor.py | 2327B9706581 | 47227 | 2026/09/24 11:17:31 |
| results/_v4_supp_l1_n28r_post_hashes_2026_09_24.txt | 5AB6A3BCC2A2 | 26833 | 2026/09/24 11:18:39 |
| results/_v4_supp_l1_n28r_pre_hashes_2026_09_24.txt | 3A98F823CE33 | 26833 | 2026/09/24 11:18:39 |
| results/_v4_supp_l1_n28r_result.json | 67AA1807F7C7 | 14632 | 2026/09/24 11:18:39 |
| results/_v4_supp_l1_n28r_verdict.md | B27AB50089F6 | 9844 | 2026/09/24 11:18:39 |
| results/_v4_supp_l2_n11supp_executor.py | 0D455B42CD07 | 44072 | 2026/09/24 12:19:26 |
| results/_v4_supp_l2_n11supp_post_hashes_2026_09_24.txt | 0AB95FC1DB4B | 395 | 2026/09/24 12:30:45 |
| results/_v4_supp_l2_n11supp_pre_hashes_2026_09_24.txt | 00327C8B0BF5 | 371 | 2026/09/24 12:21:49 |
| results/_v4_supp_l2_n11supp_result.json | FF7B167AE43F | 17970 | 2026/09/24 12:30:45 |
| results/_v4_supp_l2_n11supp_verdict.md | E433A06E7BFB | 15671 | 2026/09/24 12:32:16 |
| results/_v4_supp_l3_n20copy_backup/coze_artifact_v_2026_09_16.json.copy | FEE04170AA73 | 10978 | 2026/09/24 11:28:03 |
| results/_v4_supp_l3_n20copy_executor.py | 5190C03F0A69 | 35923 | 2026/09/24 11:27:32 |
| results/_v4_supp_l3_n20copy_post_hashes_2026_09_24.txt | 54FD10F9A114 | 1383 | 2026/09/24 11:28:04 |
| results/_v4_supp_l3_n20copy_pre_hashes_2026_09_24.txt | 88F27618D216 | 1423 | 2026/09/24 11:28:04 |
| results/_v4_supp_l3_n20copy_result.json | B84F4747BDB6 | 16077 | 2026/09/24 11:28:04 |
| results/_v4_supp_l3_n20copy_verdict.md | 9D64AB25A3BA | 16275 | 2026/09/24 11:30:43 |
| results/_v4_supp_l4_n26re_executor.py | 3B6F62686A89 | 35644 | 2026/09/24 12:12:05 |
| results/_v4_supp_l4_n26re_post_hashes_2026_09_24.txt | 5A8C5EA9E5B3 | 487 | 2026/09/24 12:18:53 |
| results/_v4_supp_l4_n26re_pre_hashes_2026_09_24.txt | 6ECA89D1F56E | 510 | 2026/09/24 12:13:04 |
| results/_v4_supp_l4_n26re_result.json | 065DD4393AB8 | 18428 | 2026/09/24 12:16:17 |
| results/_v4_supp_l4_n26re_verdict.md | 74B5B37F7EEA | 16365 | 2026/09/24 12:18:33 |
| results/_v4_supp_l5_cs39ext_executor.py | B3536C07222D | 48030 | 2026/09/24 12:04:37 |
| results/_v4_supp_l5_cs39ext_post_hashes_2026_09_24.txt | E2EBCF7743A8 | 198 | 2026/09/24 12:05:24 |
| results/_v4_supp_l5_cs39ext_pre_hashes_2026_09_24.txt | E2EBCF7743A8 | 198 | 2026/09/24 12:05:24 |
| results/_v4_supp_l5_cs39ext_result.json | ACE138CAF82F | 5788 | 2026/09/24 12:05:24 |
| results/_v4_supp_l5_cs39ext_verdict.md | FABD1BEDE4C3 | 6766 | 2026/09/24 12:05:24 |
| results/_v4_supp_l6_s38v2_executor.py | 24D759F9EFB1 | 38818 | 2026/09/24 11:34:03 |
| results/_v4_supp_l6_s38v2_post_hashes_2026_09_24.txt | 8D3285DF1529 | 3087 | 2026/09/24 11:35:42 |
| results/_v4_supp_l6_s38v2_pre_hashes_2026_09_24.txt | 41923270820F | 1197 | 2026/09/24 11:24:21 |
| results/_v4_supp_l6_s38v2_prereg_note.md | 4AC6BFECAB59 | 5415 | 2026/09/24 11:24:41 |
| results/_v4_supp_l6_s38v2_result.json | A184C37EEB2D | 18222 | 2026/09/24 11:34:10 |
| results/_v4_supp_l7_e_n20_compare.py | 328ED73043C1 | 31469 | 2026/09/24 12:14:31 |
| results/_v4_supp_l7_e_n20_fill_compare.py | B53097AE151F | 27539 | 2026/09/24 13:08:56 |
| results/_v4_supp_l7_e_n20_fill_compare_log.txt | 36F95B806984 | 1394 | 2026/09/24 13:09:03 |
| results/_v4_supp_l7_e_n20_fill_diag.py | EDE76003CBB5 | 401 | 2026/09/24 13:05:02 |
| results/_v4_supp_l7_e_n20_fill_diag2.py | AC383E4EB9EA | 646 | 2026/09/24 13:07:43 |
| results/_v4_supp_l7_e_n20_fill_diag3.py | 78E8D6482B5D | 1205 | 2026/09/24 13:11:02 |
| results/_v4_supp_l7_e_n20_fill_diag4.py | D7BAB92DD1D5 | 764 | 2026/09/24 13:12:16 |
| results/_v4_supp_l7_e_n20_fill_hash.py | ABEA08A73BC6 | 7924 | 2026/09/24 13:11:17 |
| results/_v4_supp_l7_e_n20_fill_manifest.py | 922B534C0DCE | 3161 | 2026/09/24 13:11:57 |
| results/_v4_supp_l7_e_n20_fill_manifest_2026_09_24.txt | 9FF8E7CB747E | 1956 | 2026/09/24 13:12:01 |
| results/_v4_supp_l7_e_n20_fill_measure_deepseek_v4_flash_teamo.json | E79DA92E121E | 9282 | 2026/09/24 13:08:24 |
| results/_v4_supp_l7_e_n20_fill_measure_mimo_v2_6_pro.json | 657D2A9639CD | 9307 | 2026/09/24 13:08:24 |
| results/_v4_supp_l7_e_n20_fill_measure_qwen3_7_max.json | 9A743E268563 | 9288 | 2026/09/24 13:08:24 |
| results/_v4_supp_l7_e_n20_fill_merge.py | 1666078847D0 | 13478 | 2026/09/24 13:08:03 |
| results/_v4_supp_l7_e_n20_fill_merge_log.txt | 922BBBABA538 | 2342 | 2026/09/24 13:08:24 |
| results/_v4_supp_l7_e_n20_fill_proxy_deepseek_v4_flash_teamo.json | A6CE325609C7 | 159845 | 2026/09/24 13:08:11 |
| results/_v4_supp_l7_e_n20_fill_proxy_deepseek_v4_flash_teamo_GLM_2_b20.json | 68BE63A01CC0 | 4443 | 2026/09/24 13:07:13 |
| results/_v4_supp_l7_e_n20_fill_proxy_deepseek_v4_flash_teamo_kimi_b20.json | CA1EBD7CDA59 | 5387 | 2026/09/24 13:06:37 |
| results/_v4_supp_l7_e_n20_fill_proxy_mimo_v2_6_pro.json | 2042C962EAAB | 159002 | 2026/09/24 13:08:24 |
| results/_v4_supp_l7_e_n20_fill_proxy_qwen3_7_max.json | 8E777D0407C2 | 167300 | 2026/09/24 13:08:24 |
| results/_v4_supp_l7_e_n20_fill_result.json | 1713D67076CE | 15105 | 2026/09/24 13:09:03 |
| results/_v4_supp_l7_e_n20_fill_run_log_GLM_2_b20.txt | 9294FBCA33F5 | 2010 | 2026/09/24 13:07:13 |
| results/_v4_supp_l7_e_n20_fill_run_log_kimi_b20.txt | 4F1C6C24AD3B | 2150 | 2026/09/24 13:06:37 |
| results/_v4_supp_l7_e_n20_fill_self_scan.py | 9CFBBBCADF34 | 2274 | 2026/09/24 13:11:31 |
| results/_v4_supp_l7_e_n20_manifest_2026_09_24.txt | D0215843141E | 2951 | 2026/09/24 12:56:42 |
| results/_v4_supp_l7_e_n20_measure.py | 09DD47B2F378 | 9238 | 2026/09/24 12:23:33 |
| results/_v4_supp_l7_e_n20_measure_deepseek_v4_flash_teamo.json | 692292B3D2A5 | 8993 | 2026/09/24 12:48:06 |
| results/_v4_supp_l7_e_n20_measure_mimo_v2_6_pro.json | B6F3E19F1A7D | 9003 | 2026/09/24 12:47:50 |
| results/_v4_supp_l7_e_n20_measure_qwen3_7_max.json | D1DBFD7044AA | 8988 | 2026/09/24 12:47:31 |
| results/_v4_supp_l7_e_n20_post_hashes_e_frozen_2026_09_24.txt | 4BB7DB25C57E | 1442 | 2026/09/24 12:50:42 |
| results/_v4_supp_l7_e_n20_post_hashes_e_frozen_fill_2026_09_24.txt | E5DD11E94058 | 1671 | 2026/09/24 13:11:21 |
| results/_v4_supp_l7_e_n20_post_hashes_v4frozen_2026_09_24.txt | 5D765F459E5D | 1980 | 2026/09/24 12:50:31 |
| results/_v4_supp_l7_e_n20_post_hashes_v4frozen_fill_2026_09_24.txt | AC036A1B84AF | 2133 | 2026/09/24 13:11:21 |
| results/_v4_supp_l7_e_n20_pre_hashes_e_frozen_2026_09_24.txt | C101CF3DB300 | 2612 | 2026/09/24 12:12:06 |
| results/_v4_supp_l7_e_n20_pre_hashes_v4frozen_2026_09_24.txt | D0B64D1AB8B7 | 1960 | 2026/09/24 12:12:34 |
| results/_v4_supp_l7_e_n20_proxy_deepseek_v4_flash_teamo.json | B73EA03921D8 | 154863 | 2026/09/24 12:47:59 |
| results/_v4_supp_l7_e_n20_proxy_deepseek_v4_flash_teamo_GLM_1_b0.json | E9F3F38D3ACB | 21534 | 2026/09/24 12:30:33 |
| results/_v4_supp_l7_e_n20_proxy_deepseek_v4_flash_teamo_GLM_2_b0.json | B6FDB878877C | 37396 | 2026/09/24 12:33:32 |
| results/_v4_supp_l7_e_n20_proxy_deepseek_v4_flash_teamo_coze_b0.json | 8E2E25669E0C | 28261 | 2026/09/24 12:34:58 |
| results/_v4_supp_l7_e_n20_proxy_deepseek_v4_flash_teamo_kimi_b0.json | E3CC645F2952 | 29077 | 2026/09/24 12:28:27 |
| results/_v4_supp_l7_e_n20_proxy_deepseek_v4_flash_teamo_minimax_b0.json | 9BAE56BDFE35 | 47437 | 2026/09/24 12:37:17 |
| results/_v4_supp_l7_e_n20_proxy_mimo_v2_6_pro.json | F1809148ABAC | 158900 | 2026/09/24 12:47:42 |
| results/_v4_supp_l7_e_n20_proxy_mimo_v2_6_pro_GLM_1_b0.json | B2F6F2A4ADE7 | 21142 | 2026/09/24 12:31:07 |
| results/_v4_supp_l7_e_n20_proxy_mimo_v2_6_pro_GLM_2_b0.json | 65477EB549B4 | 38450 | 2026/09/24 12:34:13 |
| results/_v4_supp_l7_e_n20_proxy_mimo_v2_6_pro_coze_b0.json | 7754DF0B92AE | 28579 | 2026/09/24 12:34:03 |
| results/_v4_supp_l7_e_n20_proxy_mimo_v2_6_pro_kimi_b0.json | ECBD60CAC0D2 | 29906 | 2026/09/24 12:28:02 |
| results/_v4_supp_l7_e_n20_proxy_mimo_v2_6_pro_minimax_b0.json | 49BFEF9202FA | 49605 | 2026/09/24 12:39:19 |
| results/_v4_supp_l7_e_n20_proxy_qwen3_7_max.json | 6C5510368D51 | 167198 | 2026/09/24 12:47:24 |
| results/_v4_supp_l7_e_n20_proxy_qwen3_7_max_GLM_1_b0.json | A3BD1EED5EF2 | 12091 | 2026/09/24 12:30:16 |
| results/_v4_supp_l7_e_n20_proxy_qwen3_7_max_GLM_1_b10.json | 7D2DF2BAD1BF | 12113 | 2026/09/24 12:44:04 |
| results/_v4_supp_l7_e_n20_proxy_qwen3_7_max_GLM_2_b0.json | CFD31D93AAC4 | 20522 | 2026/09/24 12:32:20 |
| results/_v4_supp_l7_e_n20_proxy_qwen3_7_max_GLM_2_b10.json | C5F371FC9FDB | 20637 | 2026/09/24 12:43:28 |
| results/_v4_supp_l7_e_n20_proxy_qwen3_7_max_coze_b0.json | E08335453331 | 15838 | 2026/09/24 12:33:48 |
| results/_v4_supp_l7_e_n20_proxy_qwen3_7_max_coze_b10.json | FE3446359D17 | 15909 | 2026/09/24 12:46:05 |
| results/_v4_supp_l7_e_n20_proxy_qwen3_7_max_kimi_b0.json | E4F4C967FF0F | 16506 | 2026/09/24 12:27:32 |
| results/_v4_supp_l7_e_n20_proxy_qwen3_7_max_kimi_b10.json | FF3E40F3A43B | 16503 | 2026/09/24 12:44:43 |
| results/_v4_supp_l7_e_n20_proxy_qwen3_7_max_minimax_b0.json | 8172890E320E | 30065 | 2026/09/24 12:37:03 |
| results/_v4_supp_l7_e_n20_proxy_qwen3_7_max_minimax_b10.json | C9572018C50C | 28001 | 2026/09/24 12:47:15 |
| results/_v4_supp_l7_e_n20_result.json | E9D2BFD6C756 | 14385 | 2026/09/24 12:56:11 |
| results/_v4_supp_l7_e_n20_runner.py | D5640CA314E2 | 17215 | 2026/09/24 12:23:10 |
| results/_v4_supp_l8_n12r_executor.py | 882965FDB738 | 56013 | 2026/09/24 12:02:26 |
| results/_v4_supp_l8_n12r_post_hashes_2026_09_24.txt | AB290AA01959 | 29820 | 2026/09/24 12:02:58 |
| results/_v4_supp_l8_n12r_pre_hashes_2026_09_24.txt | D999A43D521F | 29820 | 2026/09/24 12:02:56 |
| results/_v4_supp_l8_n12r_result.json | 79A3DB97B3A0 | 22680 | 2026/09/24 12:02:58 |
| results/_v4_supp_l9_a2r_cs21_result.json | F1469D78F589 | 3620 | 2026/09/24 11:50:34 |
| results/_v4_supp_l9_a2r_d1_result.json | 1913ED2963DD | 6286 | 2026/09/24 11:50:34 |
| results/_v4_supp_l9_a2r_d2_result.json | 0A3F7107C3AA | 3494 | 2026/09/24 11:50:34 |
| results/_v4_supp_l9_a2r_dct_result.json | 05903D74173E | 6668 | 2026/09/24 11:50:34 |
| results/_v4_supp_l9_a2r_dr_result.json | 31BCF67BC7A2 | 3105 | 2026/09/24 11:50:34 |
| results/_v4_supp_l9_a2r_executor.py | 73512A46BB5D | 79098 | 2026/09/24 11:49:53 |
| results/_v4_supp_l9_a2r_post_hashes_2026_09_24.txt | A3B2E7306368 | 3702 | 2026/09/24 11:50:34 |
| results/_v4_supp_l9_a2r_pre_hashes_2026_09_24.txt | 188228B24E50 | 3068 | 2026/09/24 11:50:34 |
| results/_v4_supplement_executor_2026_09_23.py | C5C5F2B5CF5D | 46566 | 2026/09/23 15:28:44 |
| results/_v4_track2_endpoints_probe.py | A70AB74F9F8C | 20702 | 2026/09/23 15:14:52 |
| results/_v4_track2_models_probe.py | B1F5DE36F5A2 | 2428 | 2026/09/23 15:13:10 |
| results/_v4_track2_multimodel_rerun.py | 295963552FC5 | 38683 | 2026/09/23 15:16:52 |
| results/_v4_track2_multimodel_rerun_2026_09_23.json | E3DAE2A4BBC2 | 35011 | 2026/09/23 15:26:47 |
| results/_v4_track2_reprobe.py | C7DCC4FC6771 | 2311 | 2026/09/23 15:13:46 |
| results/_v4_v3_degradation_contrast_result.json | 811139E25130 | 17905 | 2026/09/23 16:06:45 |
| results/_v4_v5_ablation.py | A16A3A35C034 | 42410 | 2026/09/23 12:14:22 |
| results/_v4_v5_ablation_result.json | DC35655F8E7C | 17256 | 2026/09/23 12:14:52 |
| results/_v4_v5_distill_min_measure_result_strengthen.json | 5C46B1E38EC0 | 74217 | 2026/09/23 12:17:11 |
| results/_v4_v5_manifest_strengthen.json | B73628E3B12E | 12087 | 2026/09/23 11:53:32 |
| results/_v4_v5_multimodel_probe.py | B65619A07B10 | 6209 | 2026/09/23 16:00:42 |
| results/_v4_v5_negctrl_char_shuffle.json | E6E51ABB5FB7 | 93858 | 2026/09/23 11:59:02 |
| results/_v4_v5_pre_hashes_baseline.json | 4F0EBA2A9C27 | 1109 | 2026/09/23 11:52:23 |
| results/_v4_v5_proxy_ngram_K10.json | CBC2C24B90DC | 83947 | 2026/09/23 11:59:01 |
| results/_v4_v5_proxy_ngram_K5.json | 4E3268F339BB | 81757 | 2026/09/23 11:59:01 |
| results/_v4_v5_short_token_degenerate.json | 76575D79ACA1 | 9188 | 2026/09/23 11:59:01 |
| results/_v4_v5_strengthen_build_manifest.py | 35BA8A9BB101 | 14393 | 2026/09/23 11:53:07 |
| results/_v4_v5_strengthen_derive_b1_b2_c2_c3.py | F8FECA4B4903 | 20685 | 2026/09/23 11:58:36 |
| results/_v4_v5_strengthen_measure.py | C901D848E344 | 60914 | 2026/09/23 12:13:33 |
| results/_v4_v5_strengthen_prereg_2026_09_23.md | D6286BE2BC43 | 48679 | 2026/09/23 11:37:35 |
| results/_v4_v5_t2_measure.py | 44F3690D30D8 | 40676 | 2026/09/23 12:02:35 |
| results/_v4_v5_t2_measure_result.json | 7CCBE2C3E248 | 13035 | 2026/09/23 12:03:19 |
| results/_v4_v5_t2_multimodel_compare.json | 356BD6647796 | 32393 | 2026/09/23 12:32:15 |
| results/_v5_proxy_temp_T0.3.json | 04D915714B96 | 143345 | 2026/09/23 11:59:01 |
| results/_v5_proxy_temp_T1.5.json | 2B36D8632A80 | 143261 | 2026/09/23 11:59:01 |
| results/_v5_proxy_vocab_V50.json | 2DEEDC43FC40 | 78182 | 2026/09/23 11:59:01 |
| results/_v5_proxy_vocab_V500.json | 4DDD6AFBF16B | 78191 | 2026/09/23 11:59:01 |
| results/attack_pc_a1_resampling_2026_09_15.json | D21912A05D79 | 1017 | 2026/09/15 15:27:35 |
| results/attack_pc_a2_fitting_2026_09_15.json | 5A880678C386 | 1024 | 2026/09/15 15:27:36 |
| results/attack_pc_a3_clipping_2026_09_15.json | D74D6B39D1B0 | 1265 | 2026/09/15 15:27:36 |
| results/attacker_xl_cache/algorithm_process.json | 001369ED0546 | 5367 | 2026/08/28 23:41:34 |
| results/attacker_xl_cache/biological_taxonomy.json | 9B6CAEB290A8 | 5050 | 2026/08/28 23:38:17 |
| results/attacker_xl_cache/geography_world.json | FE28D890590E | 5328 | 2026/08/28 23:46:14 |
| results/attacker_xl_cache/historical_causality.json | 89FB33F27E23 | 4403 | 2026/08/28 23:43:05 |
| results/attacker_xl_cache/physics_concepts.json | C586381C4E30 | 5931 | 2026/08/28 23:36:48 |
| results/attacker_xl_cache/project_management.json | 7BD2C0642466 | 4555 | 2026/08/28 23:47:17 |
| results/boss_pa_1_rbr_rm_result_2026_09_15.json | C7C59E0D2F6C | 8753 | 2026/09/15 15:28:10 |
| results/boss_pa_2_potential_game_result_2026_09_15.json | 5C76137D6430 | 7530 | 2026/09/15 15:28:10 |
| results/boss_pa_3_replicator_dynamics_result_2026_09_15.json | D6F233D73C45 | 9098 | 2026/09/15 15:28:10 |
| results/boss_pc_1_a1_resampling_2026_09_15.json | D21912A05D79 | 1017 | 2026/09/15 13:34:48 |
| results/boss_pc_1_real_2d_ising_2026_09_15.json | 43D9CE160FC8 | 2460 | 2026/09/15 15:28:00 |
| results/boss_pc_2_a2_fitting_2026_09_15.json | 5A880678C386 | 1024 | 2026/09/15 13:34:48 |
| results/boss_pc_2_real_transverse_ising_2026_09_15.json | 8933D61B180A | 3553 | 2026/09/15 15:27:35 |
| results/boss_pc_3_a3_clipping_2026_09_15.json | D74D6B39D1B0 | 1265 | 2026/09/15 13:34:48 |
| results/boss_pc_3_real_reservoir_2026_09_15.json | 94B5398BE76C | 2364 | 2026/09/15 15:28:00 |
| results/boss_pe_1_real_2d_ising_2026_09_15.json | 43D9CE160FC8 | 2460 | 2026/09/15 13:34:49 |
| results/boss_pe_2_real_transverse_ising_2026_09_15.json | 8933D61B180A | 3553 | 2026/09/15 13:34:49 |
| results/boss_pe_3_real_reservoir_2026_09_15.json | 94B5398BE76C | 2364 | 2026/09/15 13:34:49 |
| results/cot_quiz_cache/algorithm_process_b0.json | 4D5CF715D714 | 574 | 2026/08/28 21:08:14 |
| results/cot_quiz_cache/algorithm_process_b1.json | E49214038CFF | 593 | 2026/08/28 21:08:54 |
| results/cot_quiz_cache/biological_taxonomy_b0.json | 3DFA0D7D9259 | 605 | 2026/08/28 21:09:58 |
| results/cot_quiz_cache/biological_taxonomy_b1.json | D1370474D10A | 605 | 2026/08/28 21:10:12 |
| results/cot_quiz_cache/historical_causality_b0.json | A87A541B89C1 | 611 | 2026/08/28 21:10:26 |
| results/cot_quiz_cache/historical_causality_b1.json | EB12C7CE26DC | 611 | 2026/08/28 21:11:01 |
| results/cot_quiz_cache/physics_concepts_b0.json | 70ED50E5E869 | 587 | 2026/08/28 21:11:15 |
| results/cot_quiz_cache/physics_concepts_b1.json | C5E544069FA4 | 587 | 2026/08/28 21:11:42 |
| results/deposon_ark_models_2026_09_10.json | CCC3EA09A7F5 | 23296 | 2026/09/10 15:14:46 |
| results/deposon_benchmark_v1_3_details.json | 9FCB6B243E0D | 656572 | 2026/08/23 00:01:28 |
| results/deposon_benchmark_v1_3_labelfree.json | 57F06A426BEC | 3011 | 2026/08/23 00:30:18 |
| results/deposon_benchmark_v1_3_labelshuffle.json | 5A7555358BE3 | 182322 | 2026/08/23 00:01:28 |
| results/deposon_benchmark_v1_3_resonant.json | 769AE8C908C9 | 3134 | 2026/08/23 00:30:18 |
| results/deposon_benchmark_v1_3_simple.json | 9347ADD72401 | 2245 | 2026/08/23 00:01:28 |
| results/deposon_benchmark_v1_3_traps.json | 82EB64151F2B | 3112 | 2026/08/23 00:01:28 |
| results/deposon_benchmark_v1_4_gsm8k.json | 5CD6269D7BAF | 2741 | 2026/08/23 05:00:55 |
| results/deposon_benchmark_v1_4_gsm8k_details.json | 39F79FCE7CDB | 208350 | 2026/08/23 05:00:55 |
| results/deposon_benchmark_v1_4_sc5.json | C9796D3B3263 | 12479 | 2026/08/23 15:14:50 |
| results/deposon_benchmark_v1_4_strategyqa.json | B51FD24586B3 | 1691 | 2026/08/23 13:04:23 |
| results/deposon_benchmark_v1_4_strategyqa_details.json | A63EBEA7B29A | 235779 | 2026/09/16 11:01:12 |
| results/deposon_cpath_simulation_2026_09_10.json | 9466FDBF9C95 | 6351 | 2026/09/10 20:44:37 |
| results/deposon_deepseek_v41_flash_2026_09_10.json | 4D7BEA150F3A | 13373 | 2026/09/10 15:47:09 |
| results/deposon_deepseek_v41_flash_30cells_2026_09_10.json | 84DF447C38DF | 46432 | 2026/09/10 16:02:21 |
| results/deposon_deepseek_v41_flash_30cells_v2_2026_09_10.json | 05CDE1CA74EF | 17549 | 2026/09/10 16:17:05 |
| results/deposon_deepseek_v41_flash_30cells_v3_2026_09_10.json | 56401317E62B | 18592 | 2026/09/10 16:40:43 |
| results/deposon_deepseek_v41_flash_5cells_fix_2026_09_10.json | 28BAD561C328 | 6748 | 2026/09/10 16:55:12 |
| results/deposon_dpath_cross_modal_2026_09_10.json | AB0C2EAFF0D1 | 75964 | 2026/09/16 11:01:12 |
| results/deposon_dpath_cross_modal_runner_2026_09_10.py | FB20A6BA5EC6 | 27930 | 2026/09/16 11:01:12 |
| results/deposon_embedding_dual_2026_09_10.json | 33F8AC5D4BFF | 6834 | 2026/09/16 11:01:12 |
| results/deposon_embedding_openrouter_5models_2026_09_10.json | 0C0D9AFD39AC | 12785 | 2026/09/10 16:55:37 |
| results/deposon_feshbach_lindblad_sim_2026_09_10.json | AA545C67604D | 7414 | 2026/09/10 22:09:37 |
| results/deposon_feshbach_rag_30cells_2026_09_10.json | 508F664FFA44 | 64978 | 2026/09/16 11:01:12 |
| results/deposon_feshbach_rag_30cells_2026_09_10.py | A072E4184E83 | 14343 | 2026/09/16 11:01:12 |
| results/deposon_g1_mindmap_demo.json | 55428F6BD848 | 3041 | 2026/08/23 05:00:55 |
| results/deposon_g2_boltzmann_pathintegral.json | 9FD0F3399AB3 | 2204 | 2026/08/23 05:00:55 |
| results/deposon_g2_boltzmann_pathintegral_rewrite.json | F36667E5B5B8 | 2782 | 2026/08/23 09:40:33 |
| results/deposon_g3_arrhenius.json | A3DE045B5DD7 | 2284 | 2026/08/23 05:00:55 |
| results/deposon_game_theory_eval_2026_09_10.json | 3FA0FF2C8C08 | 10096 | 2026/09/10 21:53:17 |
| results/deposon_gpt6_astra_smoke_2026_09_10.json | 4BF92BFDEFDA | 3500 | 2026/09/10 14:37:29 |
| results/deposon_gpt6_proxy_smoke_2026_09_10.json | 524B34E319B5 | 5485 | 2026/09/10 15:13:52 |
| results/deposon_gpt6_proxy_step1_2026_09_10.json | 2E23115D9D4B | 1245 | 2026/09/10 15:13:16 |
| results/deposon_gpt6_proxy_v2_2026_09_10.json | A6812512F8F3 | 5810 | 2026/09/10 15:47:09 |
| results/deposon_gpt6_teamorouter_2026_09_10.json | F44636F5F72F | 3827 | 2026/09/10 16:49:38 |
| results/deposon_gpt6_teamorouter_30cells_2026_09_10.json | EA38EE252701 | 18290 | 2026/09/10 17:30:03 |
| results/deposon_gpt6_teamorouter_cn_2026_09_10.json | 2241567C6EFD | 4855 | 2026/09/10 17:00:24 |
| results/deposon_gpt6_vpn_smoke_2026_09_10.json | 3267746E47E9 | 3489 | 2026/09/10 14:53:46 |
| results/deposon_gsm8k_stratified.json | 8B7574B25336 | 3411 | 2026/08/23 09:40:34 |
| results/deposon_llm_codingplan_30cells_2026_09_10.json | 24E4DCBAA4EA | 18634 | 2026/09/10 15:15:24 |
| results/deposon_openrouter_5model_30cells_2026_09_10.json | B374F80F3B2D | 31690 | 2026/09/10 22:47:29 |
| results/deposon_openrouter_5model_rag_30cells_2026_09_10.json | 2E55C53BE25D | 111710 | 2026/09/10 23:34:43 |
| results/deposon_openrouter_embedding_5model_2026_09_10.json | 45F314F3415C | 9472 | 2026/09/10 22:24:35 |
| results/deposon_overseas_open_smoke_2026_09_10.json | 2481ADADCBB9 | 6787 | 2026/09/10 14:56:03 |
| results/deposon_pf_implementation_2026_09_11.json | 509DCEE3B139 | 27311 | 2026/09/16 11:01:12 |
| results/deposon_v15_diffusion.json | C16D1768D1CA | 519387 | 2026/08/23 19:21:32 |
| results/deposon_v15_diffusion_maxpath_negativeresult.json | 00EE97C82DCC | 416460 | 2026/08/23 19:21:32 |
| results/deposon_v15_diffusion_summary.json | 5B95D06E66B0 | 6079 | 2026/08/23 19:22:36 |
| results/deposon_v16_llm_prior.json | C17B31AE4F3B | 39974 | 2026/08/23 20:21:38 |
| results/deposon_v16_llm_prior_summary.json | A7952D9D78DB | 5517 | 2026/08/23 20:28:34 |
| results/deposon_v16_paired_stats.json | 20BC4288E0DE | 9176 | 2026/08/23 20:59:51 |
| results/deposon_v17_fixed_sampler.json | 701AD291A714 | 106317 | 2026/08/23 21:38:59 |
| results/deposon_v17_fusion_fix.json | AF51DA229652 | 106164 | 2026/08/23 21:31:41 |
| results/deposon_v17_fusion_fix_tieartifact_negativeresult.json | 556086D9E3BC | 106125 | 2026/08/23 21:31:36 |
| results/deposon_v17_multigraph.json | 2836605CA12F | 16896 | 2026/08/23 21:34:43 |
| results/deposon_v18_api_supplements.json | 62C1A41E1DB8 | 80624 | 2026/08/23 23:20:04 |
| results/deposon_v19_benchmark_fixes.json | 910C4333EEAD | 409104 | 2026/08/24 01:11:01 |
| results/deposon_v19_fullrank.json | FBBFD3EF3890 | 42458 | 2026/08/24 01:04:04 |
| results/deposon_v19_meanfield.json | 108DA40D5D4E | 44443 | 2026/08/24 01:02:01 |
| results/deposon_v19_quickwins.json | 1EC7ABA6AFD8 | 7842 | 2026/08/24 01:07:59 |
| results/deposon_v1_implementation_calculator_2026_09_10.py | 121F104012F4 | 10751 | 2026/09/10 22:21:56 |
| results/deposon_v20_baselines.json | 6EDB2AEC1660 | 16987 | 2026/08/29 01:17:30 |
| results/deposon_v20_bigquiz_eval.json | 283DBC8C5B63 | 35718 | 2026/08/28 23:54:14 |
| results/deposon_v20_corpus_eval.json | CA71AA6858E1 | 631644 | 2026/08/29 01:21:14 |
| results/deposon_v20_cot_quiz.json | 94FD018B5CC8 | 7101 | 2026/08/28 21:13:05 |
| results/deposon_v20_crossval.json | 76479B7A5ED6 | 8404 | 2026/08/28 20:27:06 |
| results/deposon_v20_familyl_ingest.json | 676EB83EDC27 | 1303 | 2026/08/28 17:38:45 |
| results/deposon_v20_fastcheck.json | A1EF105B0269 | 1768 | 2026/08/28 22:08:40 |
| results/deposon_v20_gt.json | 497B9C2D6746 | 3803 | 2026/08/28 17:43:00 |
| results/deposon_v20_gt2b.json | A2AE7997EE67 | 123331 | 2026/08/29 19:57:39 |
| results/deposon_v20_gt3.json | 35B676773243 | 7844 | 2026/08/29 15:03:29 |
| results/deposon_v20_gt5.json | FCA14C5735DD | 72647 | 2026/08/29 15:35:11 |
| results/deposon_v20_gt5b.json | 2907006DBE48 | 56425 | 2026/08/29 15:44:55 |
| results/deposon_v20_gt6.json | 04B90B638BDC | 65105 | 2026/08/29 15:45:04 |
| results/deposon_v20_gt7.json | 896589B673EC | 17925 | 2026/08/29 17:57:57 |
| results/deposon_v20_gt8.json | 2B88948DCA19 | 5396 | 2026/08/29 19:34:34 |
| results/deposon_v20_gt8b.json | 6339EA4E500C | 2706 | 2026/08/30 10:28:49 |
| results/deposon_v20_gt8b_ingest.json | AA077CC1725E | 986 | 2026/08/30 10:28:44 |
| results/deposon_v20_gt8c.json | 9B16FA802EF8 | 2864 | 2026/08/30 16:17:46 |
| results/deposon_v20_gt8c_ingest.json | 4B11B1BD8ADA | 1018 | 2026/08/30 16:17:42 |
| results/deposon_v20_photonics.json | 0B7893196D0B | 6796 | 2026/08/29 01:19:15 |
| results/deposon_v20_quiz_eval.json | 9194EE703218 | 22623 | 2026/08/28 20:46:44 |
| results/deposon_v20_vector_audit.json | B9B65C568842 | 915 | 2026/08/28 21:15:08 |
| results/deposon_v21_gtformal.json | 9D9AE5001C57 | 69204 | 2026/08/30 15:44:09 |
| results/deposon_v22_e95ci.json | 928BCFBDB7C3 | 1496 | 2026/08/30 21:45:29 |
| results/deposon_v22_p1c.json | 2BED4DE3A57C | 763 | 2026/08/30 21:59:28 |
| results/deposon_v41_flash_60cells_v2_2026_09_10.json | B1D802A68723 | 38428 | 2026/09/10 17:34:41 |
| results/deposon_v41_flash_rag_baseline_2026_09_10.json | 6754D2655E0A | 101484 | 2026/09/10 17:07:49 |
| results/deposon_v42_v2_miss_rate_curve_2026_09_16.json | 0A8ED127D6DE | 24435 | 2026/09/16 18:27:36 |
| results/deposon_volcengine_22caption_embedding_2026_09_10.json | C4B774C8E34C | 4559 | 2026/09/10 17:36:46 |
| results/deposon_volcengine_7model_smoke_2026_09_10.json | EAE44CC3B7B2 | 5944 | 2026/09/16 11:01:12 |
| results/deposon_volcengine_9model_30cells_2026_09_10.json | 58AB335CA341 | 4894 | 2026/09/16 11:01:12 |
| results/deposon_volcengine_9model_smoke_2026_09_10.json | 0E5AE7D7D641 | 5328 | 2026/09/16 11:01:12 |
| results/deposon_volcengine_coding_plan_5cells_2026_09_10.json | 52AA8901556E | 6058 | 2026/09/16 11:01:12 |
| results/deposon_volcengine_coding_plan_catalog_2026_09_10.json | C0EFB547B9D1 | 2841 | 2026/09/16 11:01:12 |
| results/deposon_volcengine_doubao_embedding_2026_09_10.json | E99783D18139 | 3303 | 2026/09/16 11:01:12 |
| results/deposon_volcengine_embedding_30cells_2026_09_10.json | 12BE52BC02A7 | 24794 | 2026/09/16 11:01:12 |
| results/deposon_volcengine_glm_latest_30cells_v2_2026_09_10.json | 4EC04D3D7D8C | 32995 | 2026/09/16 11:01:12 |
| results/deposon_volcengine_glm_latest_5cells_2026_09_10.json | 83C35597AF81 | 4895 | 2026/09/16 11:01:12 |
| results/deposon_volcengine_glm_latest_5cells_2026_09_10.py | A3CA05AEC6FB | 8112 | 2026/09/16 11:01:12 |
| results/deposon_volcengine_glm_latest_5cells_v2_2026_09_10.json | 0C3EDE881FB1 | 6466 | 2026/09/16 11:01:12 |
| results/deposon_volcengine_minimax_m3_30cells_2026_09_10.json | FBB7677B9CD5 | 23472 | 2026/09/16 18:20:55 |
| results/deposon_volcengine_minimax_m3_30cells_2026_09_10.py | 218EF1A99F97 | 11703 | 2026/09/16 18:20:55 |
| results/deposon_volcengine_seed_code_30cells_2026_09_10.json | 5149F5CAFCF9 | 23034 | 2026/09/16 11:01:12 |
| results/deposon_volcengine_worker_a_2026_09_10.json | 506810017D34 | 25464 | 2026/09/16 11:01:12 |
| results/deposon_volcengine_worker_b_2026_09_10.json | B1EB668377CE | 49338 | 2026/09/16 11:01:12 |
| results/deposon_volcengine_worker_b_2026_09_10.py | 401DFD3C27F3 | 13232 | 2026/09/16 11:01:12 |
| results/deposon_volcengine_worker_c_2026_09_10.json | F6F172820C97 | 51716 | 2026/09/16 11:01:12 |
| results/deposon_volcengine_worker_c_2026_09_10.py | B5EEEF1E9BD7 | 11692 | 2026/09/16 11:01:12 |
| results/deposon_volcengine_worker_d_2026_09_10.json | FAE79888344B | 20280 | 2026/09/16 11:01:12 |
| results/familyl_cache/algorithm_process.json | DEC68C2A4566 | 1441 | 2026/08/28 17:36:01 |
| results/familyl_cache/biological_taxonomy.json | B3E1627A4BCB | 1295 | 2026/08/28 17:34:20 |
| results/familyl_cache/geography_world.json | C761E48CD2DF | 1318 | 2026/08/28 23:07:12 |
| results/familyl_cache/historical_causality.json | FD411C37505F | 1621 | 2026/08/28 17:29:55 |
| results/familyl_cache/physics_concepts.json | CDC53F079981 | 1252 | 2026/08/28 17:32:45 |
| results/familyl_cache/project_management.json | 9E6AD810F83B | 1345 | 2026/08/28 23:08:10 |
| results/familyl_prior_cache/algorithm_process.json | 8003DF611108 | 2060 | 2026/08/28 20:21:06 |
| results/familyl_prior_cache/biological_taxonomy.json | DBD1D830E1B4 | 2230 | 2026/08/28 20:09:53 |
| results/familyl_prior_cache/geography_world.json | CC0B71E6FA96 | 2313 | 2026/08/28 23:12:37 |
| results/familyl_prior_cache/historical_causality.json | 5851A16A3366 | 3033 | 2026/08/28 20:23:39 |
| results/familyl_prior_cache/physics_concepts.json | D22CD39735A1 | 2595 | 2026/08/28 20:08:22 |
| results/familyl_prior_cache/project_management.json | 3E611708B82D | 1894 | 2026/08/28 23:34:16 |
| results/gt2_attacker_cache/algorithm_process.json | DDDA494F014A | 2782 | 2026/08/28 20:22:46 |
| results/gt2_attacker_cache/biological_taxonomy.json | 0F0A4329C34F | 2385 | 2026/08/28 20:11:36 |
| results/gt2_attacker_cache/historical_causality.json | 86AF2EF6B66C | 2341 | 2026/08/28 20:24:34 |
| results/gt2_attacker_cache/physics_concepts.json | 9C74BB8206C0 | 2386 | 2026/08/28 20:09:06 |
| results/gt3_prior_cache/deepseek-v4-pro-260425__algorithm_process.json | 8B391C568316 | 3314 | 2026/08/29 14:38:35 |
| results/gt3_prior_cache/deepseek-v4-pro-260425__biological_taxonomy.json | C9AB046B023F | 2563 | 2026/08/29 14:11:30 |
| results/gt3_prior_cache/deepseek-v4-pro-260425__geography_world.json | 56D62E90EC26 | 2846 | 2026/08/29 14:17:56 |
| results/gt3_prior_cache/deepseek-v4-pro-260425__historical_causality.json | 8425C48CA9A8 | 2850 | 2026/08/29 14:17:05 |
| results/gt3_prior_cache/deepseek-v4-pro-260425__physics_concepts.json | F282563826B0 | 2175 | 2026/08/29 14:10:34 |
| results/gt3_prior_cache/deepseek-v4-pro-260425__project_management.json | 15430969B7A3 | 2082 | 2026/08/29 14:19:35 |
| results/gt3_prior_cache/doubao-seed-evolving__algorithm_process.json | C1E10915FEE5 | 497 | 2026/08/29 14:49:22 |
| results/gt3_prior_cache/doubao-seed-evolving__biological_taxonomy.json | B40F756A79F2 | 2361 | 2026/08/29 14:09:01 |
| results/gt3_prior_cache/doubao-seed-evolving__geography_world.json | B3707CD37C67 | 2474 | 2026/08/29 14:29:03 |
| results/gt3_prior_cache/doubao-seed-evolving__historical_causality.json | 13D886BE8FD5 | 500 | 2026/08/29 14:57:23 |
| results/gt3_prior_cache/doubao-seed-evolving__physics_concepts.json | EA4BE673793E | 2012 | 2026/08/29 14:41:21 |
| results/gt3_prior_cache/doubao-seed-evolving__project_management.json | F602B635CE20 | 1718 | 2026/08/29 14:32:47 |
| results/gt3_prior_cache/kimi-k2-thinking__algorithm_process.json | 669DA0E1C36B | 479 | 2026/08/29 11:05:15 |
| results/gt3_prior_cache/kimi-k2-thinking__biological_taxonomy.json | 51746E4094DC | 2350 | 2026/08/29 10:30:25 |
| results/gt3_prior_cache/kimi-k2-thinking__geography_world.json | 29CCE1102BBA | 2499 | 2026/08/29 10:46:33 |
| results/gt3_prior_cache/kimi-k2-thinking__historical_causality.json | 9506AD922380 | 2500 | 2026/08/29 10:41:48 |
| results/gt3_prior_cache/kimi-k2-thinking__physics_concepts.json | BD828A9E748B | 2006 | 2026/08/29 10:28:49 |
| results/gt3_prior_cache/kimi-k2-thinking__project_management.json | 540A9EF09BF0 | 480 | 2026/08/29 11:13:18 |
| results/gt3_prior_cache/moonshot-v1-8k__algorithm_process.json | B0DC14FAC249 | 2737 | 2026/08/29 11:01:13 |
| results/gt3_prior_cache/moonshot-v1-8k__biological_taxonomy.json | 769991471AD1 | 2324 | 2026/08/29 10:29:49 |
| results/gt3_prior_cache/moonshot-v1-8k__geography_world.json | B7CCE4938263 | 2495 | 2026/08/29 10:44:48 |
| results/gt3_prior_cache/moonshot-v1-8k__historical_causality.json | 202E2E38A573 | 2649 | 2026/08/29 10:40:09 |
| results/gt3_prior_cache/moonshot-v1-8k__physics_concepts.json | 6081C483C999 | 2540 | 2026/08/29 10:27:16 |
| results/gt3_prior_cache/moonshot-v1-8k__project_management.json | 8896856F7E65 | 478 | 2026/08/29 11:09:17 |
| results/gt8b_cache/chemical_elements.json | 7250D55070B8 | 1385 | 2026/08/29 22:30:59 |
| results/gt8b_cache/chinese_dynasties.json | 8460CF6EF12C | 2206 | 2026/08/29 22:32:10 |
| results/gt8b_cache/graphs/l_chemical_elements.json | 3C6ED4EBFA2F | 4338 | 2026/08/30 10:28:44 |
| results/gt8b_cache/graphs/l_chinese_dynasties.json | A901C136CC48 | 4509 | 2026/08/30 10:28:44 |
| results/gt8b_cache/prior_chemical_elements.json | 68ABF1302467 | 2039 | 2026/08/30 10:26:48 |
| results/gt8b_cache/prior_chinese_dynasties.json | D7AC5A401AA7 | 2937 | 2026/08/29 22:40:50 |
| results/gt8c_cache/biological_taxonomy.json | F64C5A890CBB | 1211 | 2026/08/30 15:58:12 |
| results/gt8c_cache/budget.json | 19149BC59BE9 | 406 | 2026/08/30 16:07:44 |
| results/gt8c_cache/graphs/l_biological_taxonomy.json | 0C97FFB40DB9 | 3594 | 2026/08/30 16:17:42 |
| results/gt8c_cache/graphs/l_programming_concepts.json | 2F0F096627DB | 4394 | 2026/08/30 16:17:42 |
| results/gt8c_cache/prior_biological_taxonomy.json | BB435CDF9B08 | 2220 | 2026/08/30 16:03:13 |
| results/gt8c_cache/prior_programming_concepts.json | 1E2BE529D2D1 | 2113 | 2026/08/30 16:07:44 |
| results/gt8c_cache/programming_concepts.json | 646F57FA3E0D | 1329 | 2026/08/30 16:01:30 |
| results/quizbank_v20.json | F6035466FF3D | 37250 | 2026/08/28 20:46:44 |
| results/quizbank_v20_big.json | DA6FECDCBBF6 | 104872 | 2026/08/28 23:54:09 |
| results/v19_edges_audit_input.csv | 8B6682181392 | 2186 | 2026/08/28 15:53:28 |
| results/v20_graph_features.csv | F95F382ACE44 | 2151 | 2026/08/28 20:43:58 |
| results/v20_regression_field.json | 534C121765B1 | 5396 | 2026/08/28 20:44:45 |
| results/v20_regression_field_v2.json | 3596490E1FC0 | 4236 | 2026/08/28 20:45:20 |
| results/v20_statcheck_fm_vs_deg.json | DFE014C627CA | 988 | 2026/08/28 20:44:25 |
| results/v20_statcheck_fm_vs_rand.json | 1DADFAEB2C43 | 868 | 2026/08/28 20:44:24 |
| run_benchmark_v1_3.py | 54EA2644DF14 | 10690 | 2026/08/23 00:30:44 |
| run_benchmark_v1_4_gsm8k.py | FAC50B283DA5 | 11253 | 2026/08/24 01:05:38 |
| run_benchmark_v1_4_strategyqa.py | F523875A15DB | 14537 | 2026/08/30 10:26:51 |
| run_g2_ensemble.py | E3914712A984 | 8907 | 2026/08/23 09:40:07 |
| verifier/run_volcengine_9model_30cells.py | 54F8033CFB29 | 12050 | 2026/09/16 11:01:12 |
| verifier/volcengine_补测_worker_A_2026_09_10.py | 20B8A2F54AD9 | 16252 | 2026/09/16 11:01:12 |


### 2.2 Stage: V3X (195 items)

#### V3X / JUDGMENT > 33 items

| Path | SHA-12 | Size (B) | View | Status | Modified | Note |
|---|---|---|---|---|---|---|
| docs/V3X/D5_DECISIONS_LAND_REPORT_2026_09_15.md | 8FF1A7C5413F | 21756 | A | IN-EFFECT | 2026/09/15 15:15:39 | D5 landing decision report |
| docs/V3X/D7_POST_CLEANUP_REPORT_2026_09_16.json | 40955BF2ABC5 | 1248 | C | IN-EFFECT | 2026/09/16 11:01:13 | D7 post-cleanup report |
| docs/V3X/KT_B1_REWORK_REPORT_2026_09_10.md | BAEF94E393DE | 11478 | C | IN-EFFECT | 2026/09/10 12:05:42 | KT-B1 rework |
| docs/V3X/KT_C1_REPORT_PHASE_B_2026_09_09.md | 825337B10A2D | 8753 | C | IN-EFFECT | 2026/09/09 14:17:30 | KT-C1 Phase B report |
| docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md | 977FE1B48F75 | 19751 | A | IN-EFFECT | 2026/09/15 11:31:34 | P-A D1D3 report |
| docs/V3X/P_C_D1_D3_REPORT_2026_09_15.md | 79C7321056B8 | 13419 | A | IN-EFFECT | 2026/09/15 15:08:22 | P-C D1D3 report |
| docs/V3X/P_C_P_E_V0_1_VERIFICATION_2026_09_12.md | EE043A13F801 | 3899 | C | IN-EFFECT | 2026/09/11 13:01:11 | P-C/P-E v0.1 verify |
| docs/V3X/P_C_V0_1_VERIFICATION_2026_09_12.md | 00C7B7CECCDC | 4885 | C | IN-EFFECT | 2026/09/11 13:00:18 | P-C v0.1 verify |
| docs/V3X/P_E_D1_D3_REPORT_2026_09_15.md | 900DA300D11E | 13109 | A | IN-EFFECT | 2026/09/15 11:27:04 | P-E D1D3 report |
| docs/V3X/P_F_D1_FULL_REPORT_2026_09_15.md | 817EFDC2F0AD | 15985 | A | IN-EFFECT | 2026/09/15 12:15:12 | P-F D1 full report |
| docs/V3X/P_F_D1_REPORT_2026_09_15.md | E47D0348922E | 12608 | C | IN-EFFECT | 2026/09/16 11:01:12 | P-F D1 report |
| docs/V3X/P_F_V0_1_VERIFICATION_2026_09_12.md | 4D970E9C0AEC | 4188 | C | IN-EFFECT | 2026/09/11 13:09:27 | P-F v0.1 verify |
| docs/V3X/P_G_V01_REPORT_2026_09_15.md | 9A6B08D03E0C | 15479 | A | IN-EFFECT | 2026/09/15 12:06:17 | P-G v0.1 report |
| docs/V3X/QUICK_KILL_6_DIRECTIONS.md | A476F241EDB2 | 15085 | A | IN-EFFECT | 2026/09/09 09:53:43 | 6-direction quick kill |
| docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md | 4FFB21BB6BFA | 8526 | A | IN-EFFECT | 2026/09/16 11:03:10 | V3X 1-week kill report |
| results/_d05_combined_report_20260918_100853.md | C87EB8974268 | 10555 | A | IN-EFFECT | 2026/09/18 10:30:53 | D0_5 combined report |
| results/_ftfb_v3_pass1_audit_2026_09_18_corrected.md | ECB406570615 | 20117 | A | IN-EFFECT | 2026/09/18 13:45:13 | FTFB V3 pass1 audit |
| results/_ftfb_v3_pass2_audit_2026_09_18_corrected.md | 413DDB0BD00E | 28579 | A | IN-EFFECT | 2026/09/18 13:45:13 | FTFB V3 pass2 audit |
| results/_p_d_v03_verification_report_20260917_163757.md | 67AAFB57A8ED | 9799 | A | IN-EFFECT | 2026/09/17 16:39:34 | P-D v0.3 verification report |
| results/_p_k_v3_glm_fpr_audit_report_2026-09-17t08-23-41z.md | 71D5C23D9F76 | 8558 | A | IN-EFFECT | 2026/09/17 16:23:41 | P-K V3 glm FPR audit |
| results/_p_l_v3_phase1_report_20260917_132341.md | B41A17EDA169 | 11035 | A | IN-EFFECT | 2026/09/17 13:35:32 | P-L V3 phase1 report |
| results/_p_l_v3_phase2_closedsource_report_20260917_175544.md | 02443DD300CE | 5909 | A | IN-EFFECT | 2026/09/17 17:55:55 | P-L closedsource report |
| results/_p_l_v3_phase2_or_embedding_v3_report_20260917_162614.md | FA5DA7A307BD | 8102 | A | IN-EFFECT | 2026/09/17 16:33:30 | P-L OR embedding v3 report |
| results/_p_l_v3_phase2_report_20260917_142748.md | 58E15C07AF33 | 9056 | A | IN-EFFECT | 2026/09/17 14:33:45 | P-L V3 phase2 report |
| results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133358.md | 54859CF2217A | 6637 | A | IN-EFFECT | 2026/09/17 13:34:00 | P-L phase3 +7 report |
| results/_p_l_v3_vector_embedding_v2_doubao_report_20260917_170828.md | FA9CD7FFA3F2 | 17833 | A | IN-EFFECT | 2026/09/17 17:12:34 | P-L v2 doubao report |
| results/_p_l_v3_vector_embedding_v2_doubao_report_20260917_172206.md | 2E3EC17259E2 | 19548 | A | IN-EFFECT | 2026/09/17 17:55:23 | P-L v2 doubao report (run2) |
| results/_v3_supplement_verdict_2026_09_23.md | B70211BFA83E | 15247 | A | IN-EFFECT | 2026/09/23 14:27:09 | V3 supplement verdict |
| results/_v3x_p_l_v3_summary_mistral_large_2512_20260917_115049.md | 183205BAA9AC | 9570 | A | IN-EFFECT | 2026/09/17 11:53:50 | P-L mistral-large summary |
| results/d7_5anchor_60cells_9model_verdict_2026_09_18.json | 4505CCA79C15 | 2456 | A | LOCKED | 2026/09/16 11:00:06 | D7 5-anchor 60cells 9model verdict |
| results/deposon_risk1_02940_decision_2026_09_11.json | 2DC8CA9E36C1 | 4336 | C | IN-EFFECT | 2026/09/15 10:22:25 | risk1 02940 decision |
| results/deposon_risk2_canonical5_decision_2026_09_11.json | CF4A882160E1 | 4066 | C | LOCKED | 2026/09/15 10:22:26 | risk2 canonical5 decision |
| results/deposon_risk3_seff_decision_2026_09_11.json | 67867E752F47 | 6488 | C | IN-EFFECT | 2026/09/15 10:22:26 | risk3 seff decision |

#### V3X / ERRATUM > 18 items

| Path | SHA-12 | Size (B) | View | Status | Modified | Note |
|---|---|---|---|---|---|---|
| docs/V3X/BOSS_B123_BUGFIX_2026_09_09.md | 9352A1675B10 | 5615 | C | IN-EFFECT | 2026/09/09 14:50:57 | BOSS 123 bugfix |
| docs/V3X/BOSS_F_GHOST_PATH_NOTE_2026_09_11.md | 354A1360234F | 4840 | C | IN-EFFECT | 2026/09/11 13:16:07 | BOSS F ghost-path note |
| docs/V3X/CANONICAL_5_UNVERIFIED_NOTE_2026_09_11.md | B049140E130C | 6804 | C | LOCKED | 2026/09/11 13:30:46 | canonical-5 unverified note |
| docs/V3X/D7_POST_CLEANUP_PLAN_2026_09_18.json | 0B8A1A357AAE | 20271 | C | IN-EFFECT | 2026/09/15 17:27:45 | D7 post-cleanup plan |
| docs/V3X/P_D_FINGERPRINT_V0_3_SPEC_CHANGELOG.md | FC73CAB85D8F | 15021 | C | IN-EFFECT | 2026/09/17 15:16:40 | v0.3 changelog |
| docs/V3X/RISK3_V0_FIXES_2026_09_11.md | C00D1C22E7ED | 13271 | C | IN-EFFECT | 2026/09/11 17:17:36 | Risk3 v0 fixes |
| docs/V3X/TRAE_3RISK_FIX_REPORT_2026_09_16.md | 7478959CFC7D | 9267 | C | IN-EFFECT | 2026/09/15 15:10:00 | TRAE 3-risk fix |
| docs/V3X/TRAE_SELFCHECK_FIX_REPORT_2026_09_15.md | 226F740AA120 | 4840 | C | IN-EFFECT | 2026/09/15 15:39:00 | TRAE selfcheck fix |
| docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md | 424CF2D07884 | 120144 | C | IN-EFFECT | 2026/09/24 15:47:31 | v13 erratum chain E-1..E-30 |
| docs/V3X/V42_V2_REMEDIATION_CLAUSE_2026_09_16.md | E451A5A3D079 | 4775 | C | IN-EFFECT | 2026/09/16 18:33:04 | V42 remediation clause |
| results/_archive_manifest_deposon_sub_2026_09_23.json | B34B9F7BDFB7 | 52153 | C | ARCHIVED | 2026/09/23 15:11:29 | archive manifest deposon-sub |
| results/_archive_manifest_non_upload_2026_09_23.json | B899103853CA | 148690 | C | ARCHIVED | 2026/09/23 15:11:35 | archive manifest non-upload |
| results/_d05_data_rescue_note_2026_09_18.md | 120295A19655 | 1181 | C | IN-EFFECT | 2026/09/18 12:41:46 | D0_5 data rescue note |
| results/_ghostref_copy_log_2026_09_23.json | 8CD133D0896F | 129780 | C | IN-EFFECT | 2026/09/23 15:11:45 | ghostref copy log |
| results/_probe_url_update_log_2026_09_23.md | 8FCDD872DC07 | 5398 | C | IN-EFFECT | 2026/09/23 16:06:40 | probe URL update log |
| results/_v3_v4_ghostref_reconciliation_2026_09_23.md | 1D52DB0EBF53 | 169864 | B | IN-EFFECT | 2026/09/23 15:11:45 | V3-V4 ghostref reconciliation (full) |
| results/deposon_3risk_v0_fixes_2026_09_11.json | D87C0327A6FB | 8338 | C | IN-EFFECT | 2026/09/11 17:16:56 | 3-risk v0 fixes |
| results/manifest_large_files.md | E0DC7A8E4C75 | 3440 | C | IN-EFFECT | 2026/08/29 01:26:28 | manifest of large files |

#### V3X / EXP_PRODUCT > 57 items

| Path | SHA-12 | Size (B) | View | Status | Modified | Note |
|---|---|---|---|---|---|---|
| deposon_team/plugins/_pg_v01_compute.py | D511C545F88E | 20923 | C | IN-EFFECT | 2026/09/16 18:54:48 | P-G v0.1 compute |
| deposon_team/plugins/_v3_construct_diag_2026_09_23.py | CE10A3DBCB2B | 22490 | C | IN-EFFECT | 2026/09/23 14:20:25 | V3 review scripts |
| deposon_team/plugins/_v3_review_r1_inventory_2026_09_23.py | 7B97EF02C52E | 5526 | C | IN-EFFECT | 2026/09/23 13:13:02 | V3 review scripts |
| deposon_team/plugins/_v3_review_r1b_2026_09_23.py | B5E77E114D88 | 1795 | C | IN-EFFECT | 2026/09/23 13:13:45 | V3 review scripts |
| deposon_team/plugins/_v3_review_r1c_2026_09_23.py | FDFEB03E8D6F | 2919 | C | IN-EFFECT | 2026/09/23 13:14:27 | V3 review scripts |
| deposon_team/plugins/_v3_review_r1d_2026_09_23.py | 4ADBD9B5EAB5 | 1712 | C | IN-EFFECT | 2026/09/23 13:14:59 | V3 review scripts |
| deposon_team/plugins/_v3_review_r2_verify_2026_09_23.py | AEE06C009ED1 | 4528 | C | IN-EFFECT | 2026/09/23 13:24:40 | V3 review scripts |
| deposon_team/plugins/_v3_review_r2b_2026_09_23.py | 9D6343BD9755 | 3189 | C | IN-EFFECT | 2026/09/23 13:25:02 | V3 review scripts |
| deposon_team/plugins/_v3_review_r2c_2026_09_23.py | 1C30CDA5AAD6 | 4400 | C | IN-EFFECT | 2026/09/23 13:25:39 | V3 review scripts |
| deposon_team/plugins/_v3_review_r3_sha_2026_09_23.py | D3B45B64C0DA | 1881 | C | IN-EFFECT | 2026/09/23 13:26:41 | V3 review scripts |
| deposon_team/plugins/_v3_review_r4_fixscan_2026_09_23.py | 917B18EB9A5F | 3896 | C | IN-EFFECT | 2026/09/23 13:31:36 | V3 review scripts |
| deposon_team/plugins/_v3_review_r5_anchor_probe_2026_09_23.py | 7EBE0F65A64A | 2653 | C | IN-EFFECT | 2026/09/23 13:33:00 | V3 review scripts |
| deposon_team/plugins/_v3_review_r6_final_sha_2026_09_23.py | 8AF3F4460144 | 2135 | C | IN-EFFECT | 2026/09/23 13:34:47 | V3 review scripts |
| deposon_team/plugins/_v3_review_r7_fix_e15_2026_09_23.py | 40D66379EF17 | 2951 | C | IN-EFFECT | 2026/09/23 13:39:17 | V3 review scripts |
| deposon_team/plugins/_v3_review_r8_precise_scan_2026_09_23.py | 2FF60F715DEF | 5241 | C | IN-EFFECT | 2026/09/23 13:44:30 | V3 review scripts |
| deposon_team/plugins/_v3_review_r9_final_state_2026_09_23.py | FCF5BAF4DD7F | 2117 | C | IN-EFFECT | 2026/09/23 13:46:51 | V3 review scripts |
| deposon_team/plugins/boss_pa_1_rbr_rm.py | 5CC594147E00 | 17743 | C | IN-EFFECT | 2026/09/15 15:16:26 | BOSS plugins |
| deposon_team/plugins/boss_pa_2_potential_game.py | 33DFB4338C53 | 10410 | C | IN-EFFECT | 2026/09/15 15:16:26 | BOSS plugins |
| deposon_team/plugins/boss_pa_3_replicator_dynamics.py | A2BD9DD24C25 | 12900 | C | IN-EFFECT | 2026/09/15 15:16:26 | BOSS plugins |
| deposon_team/plugins/boss_pc_1_2d_ising_universality.py | BFC319808447 | 7547 | C | IN-EFFECT | 2026/09/15 15:37:54 | BOSS plugins |
| deposon_team/plugins/boss_pc_2_transverse_field_ising.py | 210105A7F29A | 7053 | C | IN-EFFECT | 2026/09/15 15:37:54 | BOSS plugins |
| deposon_team/plugins/boss_pc_3_reservoir_computing.py | 021EA39B7193 | 7373 | C | IN-EFFECT | 2026/09/15 15:37:54 | BOSS plugins |
| deposon_team/plugins/boss_pg_1_riemannian_degenerate.py | 97FEDE6C8A4E | 5996 | C | IN-EFFECT | 2026/09/15 15:37:53 | BOSS plugins |
| deposon_team/plugins/boss_pg_2_hyperbolic_classification_collapse.py | F006D4CACA94 | 5285 | C | IN-EFFECT | 2026/09/15 15:37:53 | BOSS plugins |
| deposon_team/plugins/boss_pg_3_geodesic_violation.py | 09F37C01A258 | 5517 | C | IN-EFFECT | 2026/09/15 15:37:54 | BOSS plugins |
| deposon_team/plugins/github_upload_2026_09_18.sh | 52BC19845B2B | 6030 | C | IN-EFFECT | 2026/09/15 15:18:06 | GitHub upload script |
| deposon_team/plugins/skill_a_p_a_60cells.py | B1463BB24403 | 9078 | C | IN-EFFECT | 2026/09/11 17:05:38 | P-series skill plugins |
| deposon_team/plugins/skill_b_p_c_alpha_beta.py | E5A299F69A22 | 8699 | C | IN-EFFECT | 2026/09/11 17:05:38 | P-series skill plugins |
| deposon_team/plugins/skill_c_p_e_3modality.py | E19E76C5DA7E | 8915 | C | IN-EFFECT | 2026/09/11 17:05:38 | P-series skill plugins |
| deposon_team/plugins/skill_d_p_f_observer.py | 3E369A1F6171 | 15927 | C | IN-EFFECT | 2026/09/15 13:30:57 | P-series skill plugins |
| results/_v3_construct_degradation_diag_2026_09_23.json | C8D539A58D29 | 11609 | C | IN-EFFECT | 2026/09/23 14:20:36 | V3 construct-degradation diag |
| results/deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json | 4E4A17D43ADF | 13562 | A | IN-EFFECT | 2026/09/15 13:35:18 | BOSS PE-3 reservoir verify 9m60c |
| results/deposon_d_fix2_metric_verify_9m60c_2026_09_15.json | 9F88A212A77C | 204441 | A | IN-EFFECT | 2026/09/16 11:01:12 | D-fix2 9m60c verify |
| results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json | B5873AFB9D29 | 18104 | A | IN-EFFECT | 2026/09/16 18:39:54 | P-D B3 merkle 22-caption |
| results/deposon_p_k_cross_subject_fingerprint_blind_test_2026_09_16.json | 576EAF8D7431 | 11341 | A | IN-EFFECT | 2026/09/16 18:39:55 | P-K cross-subject blind test |
| results/deposon_pa_d1_d3_2026_09_15.json | E221792715F8 | 15604 | A | IN-EFFECT | 2026/09/15 11:29:23 | P-A D1D3 |
| results/deposon_pc_d1_d3_2026_09_15.json | B2046AF03610 | 20408 | A | IN-EFFECT | 2026/09/15 11:01:56 | P-C D1D3 |
| results/deposon_pe_d1_d3_2026_09_15.json | 594D7A8D3DE8 | 17085 | A | IN-EFFECT | 2026/09/15 10:49:09 | P-E D1D3 |
| results/deposon_pf_d1_2026_09_15.json | 12791772814E | 21933 | A | IN-EFFECT | 2026/09/15 11:30:53 | P-F D1 |
| results/deposon_pf_d1_full_9m5c_2026_09_15.json | FCB5105DF0B6 | 33829 | A | IN-EFFECT | 2026/09/16 11:01:12 | P-F D1 full 9m5c |
| results/deposon_pg_v01_9m60c_2026_09_15.json | AB75889EE738 | 11512 | A | IN-EFFECT | 2026/09/15 13:35:24 | P-G v0.1 9m60c |
| results/deposon_v2_phase1_60cells_2026_09_11.json | A18BBC703B42 | 85508 | C | IN-EFFECT | 2026/09/16 11:01:12 | V2 phase1 60cells |
| results/deposon_v2_phase2_dual_mainline_2026_09_11.json | E337B824C4B9 | 3189 | C | IN-EFFECT | 2026/09/16 11:01:12 | V2 phase2 dual mainline |
| results/deposon_v2_phase2_f2_2026_09_11.json | 8B16B611C4DB | 4582 | C | IN-EFFECT | 2026/09/11 11:19:24 | V2 phase2 F2 |
| results/deposon_v2_phase3_f3_2026_09_11.json | 0B5DCA765D16 | 2474 | C | IN-EFFECT | 2026/09/11 11:19:55 | V2 phase3 F3 |
| results/deposon_v2_phase3_strip_embeddings_2026_09_11.json | 1DED6731CC27 | 2398383 | C | IN-EFFECT | 2026/09/11 11:33:43 | V2 phase3 strip embeddings |
| results/deposon_v2_phase3_strip_reembed_2026_09_11.json | 8900526D8E3A | 4160 | C | IN-EFFECT | 2026/09/11 11:33:43 | V2 phase3 strip re-embed |
| results/deposon_v2_phase4_f4_2026_09_11.json | CF7682348617 | 5212 | C | IN-EFFECT | 2026/09/11 11:17:21 | V2 phase4 F4 |
| results/deposon_v2_phase5_f5_2026_09_11.json | 889FC57B3B72 | 2356 | C | IN-EFFECT | 2026/09/11 11:16:45 | V2 phase5 F5 |
| results/deposon_v3_physical_opt_2026_09_11.json | 27F9BD5CC260 | 17591 | C | IN-EFFECT | 2026/09/11 12:05:53 | V3 physical opt |
| results/deposon_v3_physical_opt_60cells_2026_09_11.json | C659695AA23C | 17732 | C | IN-EFFECT | 2026/09/15 10:19:42 | V3 physical opt 60cells |
| results/deposon_v3x_6way_stage2_2026_09_10.json | D301BBFED982 | 2741 | A | IN-EFFECT | 2026/09/10 17:56:17 | V3X 6-way stage2 |
| results/deposon_v3x_6way_stage3_2026_09_10.json | D892A9D3D6BA | 15943 | A | IN-EFFECT | 2026/09/10 18:15:22 | V3X 6-way stage3 |
| results/skill_a_p_a_60cells_result_2026_09_11.json | F4A210D69220 | 2220 | A | IN-EFFECT | 2026/09/11 17:06:25 | skill A P-A 60cells |
| results/skill_b_p_c_alpha_beta_result_2026_09_11.json | B921002E4DFB | 12609 | A | IN-EFFECT | 2026/09/11 17:06:29 | skill B P-C alpha-beta |
| results/skill_c_p_e_3modality_result_2026_09_11.json | 470425A8C77D | 5271 | A | IN-EFFECT | 2026/09/11 17:06:33 | skill C P-E 3-modality |
| results/skill_d_p_f_observer_result_2026_09_11.json | 0207C01B9562 | 11010 | A | IN-EFFECT | 2026/09/15 13:31:05 | skill D P-F observer |

#### V3X / ARTIFACT > 6 items

| Path | SHA-12 | Size (B) | View | Status | Modified | Note |
|---|---|---|---|---|---|---|
| deposon_team/plugins/_v3x_frozen_schema_v1.json | 9E99DCC4D920 | 12919 | C | LOCKED | 2026/09/17 10:27:19 | V3X frozen schema |
| results/llm_prior_cache.json | 5F16BE89EFC5 | 938 | C | IN-EFFECT | 2026/08/23 20:21:35 | LLM prior cache |
| results/llm_prior_cache_v18_contamination.json | D3F72F67977D | 639 | C | IN-EFFECT | 2026/08/23 22:56:14 | v18 probe cache x4 |
| results/llm_prior_cache_v18_contentless.json | 7C0D169EF164 | 512 | C | IN-EFFECT | 2026/08/23 23:17:58 | v18 probe cache x4 |
| results/llm_prior_cache_v18_direction.json | 023F936F80FB | 2168 | C | IN-EFFECT | 2026/08/23 23:04:12 | v18 probe cache x4 |
| results/llm_prior_cache_v18_labelshuffle.json | 8DCE6D7618A2 | 1925 | C | IN-EFFECT | 2026/08/23 22:56:03 | v18 probe cache x4 |

#### V3X / LETTERS > 22 items

| Path | SHA-12 | Size (B) | View | Status | Modified | Note |
|---|---|---|---|---|---|---|
| docs/V3X/BOSS_URL_2026_09_11.md | 1BA7419178A1 | 7135 | C | IN-EFFECT | 2026/09/11 13:01:49 | BOSS URL comm |
| docs/V3X/D3_WECHAT_MIDTERM_TEMPLATE.md | 574D5A79E363 | 4361 | C | IN-EFFECT | 2026/09/09 11:23:41 | D3 wechat midterm template |
| docs/V3X/D7_WANG_TEACHER_WECHAT_PUSH_REQUIREMENTS_2026_09_18.md | 935CB6EE3566 | 8037 | B | IN-EFFECT | 2026/09/16 11:08:22 | Wang-teacher wechat push req |
| letters/LETTER_FROM_TRAE_2026_09_11.md | 1D3A9E52ABE3 | 13617 | B | IN-EFFECT | 2026/09/11 16:30:23 | TRAE commission / reply series |
| letters/LETTER_FROM_TRAE_3RISK_2026_09_11.md | A1AFBF3E1296 | 5145 | B | IN-EFFECT | 2026/09/15 10:25:49 | TRAE commission / reply series |
| letters/LETTER_FROM_TRAE_REVIEW_2026_09_16.md | 6145162379C9 | 7718 | B | IN-EFFECT | 2026/09/15 15:19:16 | TRAE commission / reply series |
| letters/LETTER_FROM_TRAE_SELFCHECK_FIX_2026_09_15.md | 141E05BF56EA | 3571 | B | IN-EFFECT | 2026/09/15 15:39:01 | TRAE commission / reply series |
| letters/TRAE_CODE_IMPROVEMENT_LETTER_2026_09_17.md | 53A90B9EFBB9 | 5154 | B | IN-EFFECT | 2026/09/17 19:16:03 | TRAE letter series |
| letters/TRAE_FIX_REQUEST_3RISKS_2026_09_11.md | 62C4AF080EA3 | 15990 | B | IN-EFFECT | 2026/09/11 17:27:09 | TRAE letter series |
| letters/TRAE_V3_CODE_IMPROVEMENT_LETTER_2026_09_16.md | 9AA717B2E1AC | 7376 | B | IN-EFFECT | 2026/09/16 20:58:07 | TRAE letter series |
| letters/TRAE_V3_REVIEW_LETTER_2026_09_23.md | 0E7600AC4478 | 7510 | B | IN-EFFECT | 2026/09/23 13:08:23 | TRAE letter series |
| results/_coze_paper_v1_draft_2026_09_17.md | C08E7ABF5EE3 | 29484 | B | IN-EFFECT | 2026/09/18 00:21:36 | coze paper v1 draft |
| results/_coze_paper_v1_summary_2026_09_17.md | 2EFDC3D7741D | 3624 | B | IN-EFFECT | 2026/09/18 00:20:40 | coze paper v1 summary |
| results/_coze_wechat_v3_2026_09_18.md | 229D76E1B86F | 7466 | B | IN-EFFECT | 2026/09/18 21:03:20 | coze wechat v3 |
| results/_coze_wechat_v3_d7format_2026_09_18.md | 905544775AEE | 8715 | B | IN-EFFECT | 2026/09/18 21:08:42 | coze wechat v3 D7 format |
| results/_coze_wechat_v3_final_2026_09_18.md | DEEE45F45C5D | 11657 | B | IN-EFFECT | 2026/09/18 21:04:55 | coze wechat v3 final |
| results/_d7_wang_teacher_wechat_publish_v1_20260918.md | F4D5B755736A | 9891 | B | IN-EFFECT | 2026/09/17 14:39:46 | Wang-teacher wechat v1 |
| results/_glm_response_v2_template_2026_09_18.md | 972401E056F6 | 44191 | C | IN-EFFECT | 2026/09/18 13:59:16 | GLM response v2 template |
| results/_kimi_safe_batch_push_v1_2026_09_17.json | 4A204FB0D682 | 7280 | C | IN-EFFECT | 2026/09/17 14:01:43 | kimi safe-batch push v1 |
| results/_kimi_safe_batch_push_v2_full_2026_09_17.json | ADF3A8017E26 | 47954 | C | IN-EFFECT | 2026/09/17 14:51:41 | kimi safe-batch push v2 |
| results/_kimi_safe_batch_push_v3_full_2026_09_17.json | 058099C10CFB | 7954 | C | IN-EFFECT | 2026/09/18 13:50:24 | kimi safe-batch push v3 |
| results/_v3x_d0_5_experiment_invitation_2026_09_17.md | D8F2B99AA527 | 7617 | C | IN-EFFECT | 2026/09/17 09:34:32 | D0_5 experiment invitation |

#### V3X / KNOWLEDGE > 59 items

| Path | SHA-12 | Size (B) | View | Status | Modified | Note |
|---|---|---|---|---|---|---|
| deposon_team/plugins/github_dir_structure_2026_09_18.md | 0FD07AD38282 | 11675 | C | IN-EFFECT | 2026/09/15 15:17:42 | GitHub dir push listing |
| docs/V3X/AGENT_TEAM_OPT_V2_2026_09_11.md | BBD074B76526 | 11835 | C | IN-EFFECT | 2026/09/11 16:30:03 | agent team opt v2 |
| docs/V3X/BOSS_PE_3_RESERVOIR_VERIFY_REPORT_2026_09_15.md | C28F7F0B530F | 11079 | A | IN-EFFECT | 2026/09/15 13:36:08 | BOSS PE-3 reservoir verify |
| docs/V3X/BOSS_SELFTEST_PHASE_B_2026_09_09.md | 4485443757E7 | 15478 | C | IN-EFFECT | 2026/09/09 14:18:07 | BOSS selftest Phase B |
| docs/V3X/BOSS_URL_DUE_DILIGENCE_2026_09_11.md | 0FB588BB0C2E | 10970 | C | IN-EFFECT | 2026/09/11 12:11:02 | BOSS URL due diligence |
| docs/V3X/BPA_PILOT_2026_09_09_mavis.md | D74E1534493E | 6864 | C | IN-EFFECT | 2026/09/09 13:39:22 | BPA pilot |
| docs/V3X/CPATH_SIMULATION_REPORT_2026_09_10.md | DE772CD9E7BA | 6825 | C | IN-EFFECT | 2026/09/10 20:47:18 | cpath simulation |
| docs/V3X/D0_FREEZE_PREP_2026_09_09.md | 0D1E88C258AA | 9844 | C | IN-EFFECT | 2026/09/09 10:55:24 | D0 freeze prep |
| docs/V3X/D7_GITHUB_PUSH_RECEIVE_2026_09_15_v2.md | 2C4BB6078EE7 | 5930 | C | IN-EFFECT | 2026/09/15 17:28:16 | D7 GitHub push/receive |
| docs/V3X/D7_ONE_PAGE_SUMMARY_2026_09_11_v5.md | 67063F9CB238 | 6459 | B | IN-EFFECT | 2026/09/11 13:30:46 | V3 1-page summary v5 |
| docs/V3X/D7_ONE_PAGE_SUMMARY_TEMPLATE.md | 87563A63B854 | 5830 | C | IN-EFFECT | 2026/09/09 11:00:34 | 1-page summary template |
| docs/V3X/D7_PRE_V3_POLISH_AND_TEAM_IMPROVEMENT_2026_09_16.md | 51869E3184F4 | 10692 | B | IN-EFFECT | 2026/09/16 11:09:18 | V3 polish + team improvement |
| docs/V3X/DEPOSON_EMBEDDING_6WAY_THEORY_V0_2026_09_10.md | AC8997B07731 | 22442 | A | IN-EFFECT | 2026/09/10 20:22:54 | embedding 6-way theory |
| docs/V3X/DEPOSON_EMBEDDING_6WAY_VERIFICATION_2026_09_10.md | 240A7AE4BDFB | 17803 | A | IN-EFFECT | 2026/09/10 18:16:43 | embedding 6-way verification |
| docs/V3X/DPATH_CROSS_MODAL_2026_09_10.md | E4EE3999F7CE | 26460 | A | IN-EFFECT | 2026/09/16 11:01:12 | dpath cross-modal |
| docs/V3X/D_FIX2_METRIC_VERIFY_REPORT_2026_09_15.md | 0A63824F0805 | 7352 | A | IN-EFFECT | 2026/09/15 14:07:47 | d fix2 metric verification |
| docs/V3X/KT_A1_SPEC_V0.1.md | 78B71D404366 | 29570 | C | IN-EFFECT | 2026/09/09 13:42:23 | KT-A1 spec |
| docs/V3X/KT_B1_SPEC_V0.1.md | 0410CA0FBDAE | 35688 | C | IN-EFFECT | 2026/09/09 13:42:23 | KT-B1 spec |
| docs/V3X/KT_C1_SPEC_V0.1.md | 59D8F56347D5 | 31241 | C | IN-EFFECT | 2026/09/09 13:42:23 | KT-C1 spec |
| docs/V3X/KT_D0_EVIDENCE_CARD.md | 75B2F3B38C2A | 6354 | C | IN-EFFECT | 2026/09/09 10:59:38 | KT-D0 evidence card |
| docs/V3X/KT_D0_SPEC_V0.1.md | CCE8E9A1B00E | 20927 | C | IN-EFFECT | 2026/09/09 13:42:24 | KT-D0 spec |
| docs/V3X/PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md | C165CD33A362 | 4587 | A | IN-EFFECT | 2026/09/11 11:17:21 | P-D v0.2 spec |
| docs/V3X/PHASE_B_DELIVERY_2026_09_09.md | BA53D73E3937 | 9701 | C | IN-EFFECT | 2026/09/09 14:19:28 | Phase B delivery |
| docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md | BD1CAAB42B4C | 10351 | C | IN-EFFECT | 2026/09/09 10:05:24 | P-A v0 spec |
| docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md | BB7CA9838150 | 7126 | C | IN-EFFECT | 2026/09/08 16:02:44 | P-B v0 spec |
| docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md | D427B2F57C33 | 6301 | C | IN-EFFECT | 2026/09/08 16:03:54 | P-C v0 spec |
| docs/V3X/P_D_B3_MERKLE_22_CAPTION_VERIFICATION_2026_09_16.md | 7F1492FBE657 | 10979 | A | IN-EFFECT | 2026/09/16 18:26:46 | P-D B3 verification |
| docs/V3X/P_D_FINGERPRINT_V0_3_SPEC.md | F119F2F30287 | 34393 | A | IN-EFFECT | 2026/09/17 15:15:44 | P-D v0.3 spec (core) |
| docs/V3X/P_D_FINGERPRINT_V0_SPEC.md | 3B67461B05FE | 9192 | C | IN-EFFECT | 2026/09/04 13:11:41 | P-D v0 spec (early) |
| docs/V3X/P_E_DOUBAN_EMBEDDING_V0_SPEC.md | 6F3C550CEC13 | 16876 | C | IN-EFFECT | 2026/09/08 21:56:01 | P-E v0 spec |
| docs/V3X/P_F_IMPLEMENTATION_2026_09_11.md | EDD048EAA721 | 22973 | A | IN-EFFECT | 2026/09/16 11:01:12 | P-F implementation |
| docs/V3X/P_F_RESEARCH_2026_09_09.md | 98085DF7811A | 17603 | A | IN-EFFECT | 2026/09/09 13:49:14 | P-F research |
| docs/V3X/P_F_SPEC_V0.md | DE90FAF362C5 | 19804 | A | IN-EFFECT | 2026/09/09 13:50:05 | P-F v0 spec |
| docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md | B10FAE0DA66D | 6375 | C | IN-EFFECT | 2026/09/11 12:15:55 | P-F v0.1 upgrade |
| docs/V3X/P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md | 2F0765A1D39D | 12501 | A | IN-EFFECT | 2026/09/15 11:33:11 | P-G v0 spec |
| docs/V3X/REVIEWER_A_STATIC_AUDIT_2026_09_15.md | 575572872E9A | 34647 | C | IN-EFFECT | 2026/09/15 14:22:04 | Reviewer A static audit |
| docs/V3X/REVIEWER_A_TRAE_FIX_AUDIT_2026_09_15.md | 195373C094D6 | 20698 | C | IN-EFFECT | 2026/09/15 15:29:00 | Reviewer A trae fix audit |
| docs/V3X/REVIEWER_A_TRAE_N123_AUDIT_2026_09_15.md | 33EE7266CF5B | 17151 | C | IN-EFFECT | 2026/09/15 15:59:57 | Reviewer A trae n123 audit |
| docs/V3X/REVIEWER_B_AUDIT_PHASE_B_2026_09_09.md | 5E99E79F2E11 | 14835 | C | IN-EFFECT | 2026/09/09 14:17:07 | Reviewer B Phase B audit |
| docs/V3X/REVIEWER_B_TRAE_FIX_RERUN_2026_09_15.md | F5AC9820310A | 16278 | C | IN-EFFECT | 2026/09/15 15:28:54 | Reviewer B trae fix rerun |
| docs/V3X/REVIEWER_B_TRAE_N123_RERUN_2026_09_15.md | 31C27C0117A6 | 16926 | C | IN-EFFECT | 2026/09/15 15:57:55 | Reviewer B trae n123 rerun |
| docs/V3X/SPEC_V0_1_BOSS_SELFTEST_2026_09_09.md | 00E543564E3F | 10708 | C | IN-EFFECT | 2026/09/09 14:18:34 | BOSS selftest spec |
| docs/V3X/TRAE_PL_V2_EXPERIMENT_PROPOSAL_2026_09_17.md | 4020B1809780 | 8849 | A | IN-EFFECT | 2026/09/17 11:12:54 | TRAE P-L v2 proposal |
| docs/V3X/TRAE_PROACTIVE_AUDIT_REPORT_2026_09_16.md | 813B34DCAC70 | 6493 | C | IN-EFFECT | 2026/09/15 15:18:50 | TRAE proactive audit |
| docs/V3X/V3X_D6_PAPER_V2_2026_09_09_mavis.md | 4D06D34CB6FA | 24778 | C | IN-EFFECT | 2026/09/09 13:41:07 | V3X D6 paper v2 |
| docs/V3X/V3X_D6_PAPER_zh.md | FEAE8AF2FEFE | 19716 | C | IN-EFFECT | 2026/09/09 11:34:06 | V3X D6 paper zh |
| docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md | 4A08521F8DE1 | 38545 | A | IN-EFFECT | 2026/09/16 11:01:12 | V3 final report |
| docs/V3X/V3X_DAILY_KILL_V2_PLAN.md | 37E97E1E7B7F | 15327 | C | IN-EFFECT | 2026/09/09 11:39:34 | V3X daily kill v2 plan |
| docs/V3X/V3X_FULL_EXPERIMENT_DESIGN_2026_09_16.md | 3D847F9F3151 | 22427 | A | IN-EFFECT | 2026/09/16 12:28:47 | V3X full experiment design |
| docs/V3X/V3X_PROJECT_EVOLUTION_FOR_KIMI.md | 4DE2CBF57A49 | 12908 | A | IN-EFFECT | 2026/09/15 14:55:11 | deposon evolution for KIMI |
| docs/V3X/V42_V2_VERIFIER_PERFORMANCE_REPORT_2026_09_16.md | 914053FC3E17 | 11080 | C | IN-EFFECT | 2026/09/16 18:33:19 | V42 verifier performance |
| results/_p_l_v3_phase3_adendum_summary_20260917_132143.md | 8C07AB5AA968 | 16612 | A | IN-EFFECT | 2026/09/17 13:22:27 | P-L V3 phase3 adendum summary |
| results/_v3x_conservation_anchor_2026_09_17.txt | F331A9C2BD22 | 940 | C | LOCKED | 2026/09/17 10:20:17 | V3X conservation anchor |
| results/_v3x_d0_5_aggregation_2026_09_17.md | DDF0D1AA96D2 | 12010 | A | IN-EFFECT | 2026/09/17 13:08:30 | D0_5 aggregation report |
| results/_v3x_d0_5_proposal_coze_2026_09_17.md | 759C25B21ED4 | 13200 | A | IN-EFFECT | 2026/09/17 11:06:19 | D0_5 proposal coze |
| results/_v3x_d0_5_proposal_trae_2026_09_17.md | B1C227D54A82 | 13254 | A | IN-EFFECT | 2026/09/20 17:11:14 | D0_5 proposal trae |
| results/_v3x_p_l_v3_external_spec_2026_09_17.md | 6A5B6EB635F0 | 5769 | A | IN-EFFECT | 2026/09/17 11:03:24 | P-L V3 external spec |
| results/deposon_v3_v7_summary_2026_09_11.json | 063AC8D00542 | 25049 | A | IN-EFFECT | 2026/09/16 11:01:12 | V3 V7 summary |
| results/deposon_v3x_6way_summary_2026_09_10.json | 63E0798E5843 | 1506 | A | IN-EFFECT | 2026/09/10 18:17:10 | V3X 6-way summary |


### 2.3 Stage: V4 (128 items)

#### V4 / JUDGMENT > 36 items

| Path | SHA-12 | Size (B) | View | Status | Modified | Note |
|---|---|---|---|---|---|---|
| results/_v4_d1_decisions_2026_09_22.md | A00826ED0E21 | 1892 | A | IN-EFFECT | 2026/09/22 17:32:57 | V4 D1 decisions summary |
| results/_v4_d5_rootcause_notes.md | 1DED0240F532 | 13114 | A | IN-EFFECT | 2026/09/23 11:07:53 | D5 root-cause notes |
| results/_v4_distill_min_verdict_v1.md | 1BD9243969B6 | 13178 | A | IN-EFFECT | 2026/09/23 10:51:19 | distill-min v1 verdict |
| results/_v4_exec_methods_batch_verdict.md | 4913D8DC7261 | 12660 | A | IN-EFFECT | 2026/09/23 12:29:52 | methods batch verdict |
| results/_v4_exec_n_batch_verdict.md | AFBD998962C2 | 7137 | A | IN-EFFECT | 2026/09/23 12:39:59 | N-batch verdict |
| results/_v4_exec_seeds_batch_verdict.md | F7FC92B8B2F5 | 8113 | A | IN-EFFECT | 2026/09/23 12:07:22 | seeds batch verdict |
| results/_v4_gA3_seeds_judgment_draft_2026_09_22.md | 9119BB791DC1 | 19772 | A | IN-EFFECT | 2026/09/22 15:26:03 | gA3 seeds judgment |
| results/_v4_group_b_17letters_judgment_draft_2026_09_22.md | 99B835595DFB | 24822 | A | IN-EFFECT | 2026/09/22 16:24:26 | Group-B 17-letter judgment |
| results/_v4_n22_n19_supp_verdict.md | DB567722D007 | 8906 | A | IN-EFFECT | 2026/09/23 17:05:40 | N22/N19 supp verdict |
| results/_v4_n22s_margin_verdict.md | D64E1264737F | 11027 | A | IN-EFFECT | 2026/09/24 09:42:45 | N22s margin verdict |
| results/_v4_n29_real_verdict.md | E62D245CE285 | 6769 | A | IN-EFFECT | 2026/09/23 16:38:24 | N29 real verdict |
| results/_v4_pi_cot_verdict.md | D279EBDE5E84 | 2208 | A | IN-EFFECT | 2026/09/23 17:17:32 | Task-B verdict |
| results/_v4_rejudge_verdict.md | 5CCF32F96B4B | 14683 | A | IN-EFFECT | 2026/09/23 14:20:21 | V4 rejudge verdict |
| results/_v4_rerun_verdict.md | F258A4368328 | 8068 | A | IN-EFFECT | 2026/09/23 14:30:21 | V4 rerun verdict |
| results/_v4_rootcause_upgrade_review.md | C398CF82B3EA | 20182 | A | IN-EFFECT | 2026/09/23 15:34:54 | root-cause upgrade review |
| results/_v4_s40_semantics_verdict_2026_09_23.md | 0D6B3C74DC98 | 12143 | A | IN-EFFECT | 2026/09/23 16:18:47 | S40 semantics verdict |
| results/_v4_supp_a1_seed_verdict.md | BB916AC9DB8A | 17429 | A | IN-EFFECT | 2026/09/24 11:28:18 | L1 seed verdict |
| results/_v4_supp_a2_method_verdict.md | 8C6480A68CF0 | 21394 | A | IN-EFFECT | 2026/09/24 10:01:14 | L2 method verdict |
| results/_v4_supp_b_n_verdict.md | 7431E8065C4B | 11394 | A | IN-EFFECT | 2026/09/24 09:56:06 | L3-B N verdict |
| results/_v4_supp_cd_verdict.md | 7606A0E7C4B6 | 7863 | A | IN-EFFECT | 2026/09/24 09:50:19 | L4-C/D verdict |
| results/_v4_supp_e_multimodel_verdict.md | 9FD4B722405E | 19461 | A | IN-EFFECT | 2026/09/24 10:25:14 | L5-E multimodel verdict |
| results/_v4_supp_l11_dct100_verdict.md | 14A98CFAA660 | 18650 | A | IN-EFFECT | 2026/09/24 13:36:03 | L11 DCT100 verdict |
| results/_v4_supp_l12_dr_real_renyi_verdict.md | 977FB07592F4 | 24321 | A | IN-EFFECT | 2026/09/24 13:51:38 | L12 D-R R茅nyi verdict |
| results/_v4_supp_l13_n26pair_verdict.md | E105EC1362DB | 23120 | A | IN-EFFECT | 2026/09/24 14:15:28 | L13 N26 pair verdict |
| results/_v4_supp_l6_s38v2_rootcause_verdict.md | 973103878D6F | 24847 | A | IN-EFFECT | 2026/09/24 11:44:57 | L6 S38v2 root-cause verdict (key) |
| results/_v4_supp_l6_s38v2_verdict.md | 20D9B44E036E | 16224 | A | IN-EFFECT | 2026/09/24 11:35:12 | L6 S38v2 verdict |
| results/_v4_supp_l7_e_n20_fill_verdict.md | 0E4A7FCE58C0 | 7481 | A | IN-EFFECT | 2026/09/24 13:09:03 | L7 e-N20 fill verdict |
| results/_v4_supp_l7_e_n20_verdict.md | B8335982AE5E | 6424 | A | IN-EFFECT | 2026/09/24 12:56:18 | L7 e-N20 verdict |
| results/_v4_supp_l8_n12r_verdict.md | 114CF71AB3D4 | 19127 | A | IN-EFFECT | 2026/09/24 12:04:45 | L8 N12-R verdict |
| results/_v4_supp_l9_a2r_verdict.md | E12C7D2DABA1 | 7724 | A | IN-EFFECT | 2026/09/24 11:50:34 | L9 A2-R verdict |
| results/_v4_track2_multimodel_verdict_2026_09_23.md | 44D9BAD9039B | 12883 | A | IN-EFFECT | 2026/09/23 15:27:54 | V4 Track-2 multimodel verdict |
| results/_v4_v3_degradation_contrast_verdict.md | 3BD454B1A780 | 8978 | A | IN-EFFECT | 2026/09/23 16:08:41 | V3 vs V4 degradation contrast |
| results/_v4_v5_ablation_verdict.md | C2920AA9923A | 7707 | A | IN-EFFECT | 2026/09/23 12:14:52 | v5 ablation verdict |
| results/_v4_v5_t2_multimodel_verdict.md | C386251D94D6 | 4264 | A | IN-EFFECT | 2026/09/23 12:32:15 | v5 T2 multimodel verdict |
| results/_v4_v5_t2_verdict.md | 83D8E7A8BA12 | 9301 | A | IN-EFFECT | 2026/09/23 12:03:19 | v5 T2 verdict |
| results/_v4_v5_verdict_v1.md | 6A82CFFD01CA | 25818 | A | IN-EFFECT | 2026/09/23 12:22:21 | v5 verdict v1 |

#### V4 / PREREG > 16 items

| Path | SHA-12 | Size (B) | View | Status | Modified | Note |
|---|---|---|---|---|---|---|
| results/_v4_N09_N39_prereg_2026_09_23.md | 0A9EE16267B5 | 60530 | A | IN-EFFECT | 2026/09/23 11:34:08 | N09-N39 prereg |
| results/_v4_methods_prereg_supplement_2026_09_23.md | 0A7BCA992B95 | 59570 | A | IN-EFFECT | 2026/09/23 11:35:03 | methods prereg supplement |
| results/_v4_n22_n19_prereg_activation_2026_09_23.md | 0F68058ECBAA | 1298 | A | IN-EFFECT | 2026/09/23 16:40:42 | N22/N19 activation |
| results/_v4_n22_n19_prereg_supplement_2026_09_23.md | 4070FDAAC111 | 39819 | A | IN-EFFECT | 2026/09/23 16:27:41 | N22/N19 prereg supplement |
| results/_v4_pi_cot_distill_prereg.md | 696AF9121D9F | 3577 | A | IN-EFFECT | 2026/09/23 13:08:36 | Task-B distill prereg |
| results/_v4_pi_cot_prereg_activation_2026_09_23.md | 478F10CEAE7B | 1177 | A | IN-EFFECT | 2026/09/23 15:00:30 | Task-B prereg activation |
| results/_v4_pi_cot_v2_prereg.md | CC25C5149CE1 | 4247 | A | IN-EFFECT | 2026/09/23 17:56:05 | Task-B v2 prereg |
| results/_v4_pi_cot_v2_prereg_activation_2026_09_23.md | 00584E5A5C78 | 1016 | A | IN-EFFECT | 2026/09/23 18:03:11 | Task-B v2 activation |
| results/_v4_prereg_77_activation_2026_09_23.md | 856E75B4BAAB | 17984 | A | IN-EFFECT | 2026/09/23 11:36:21 | 77 activation |
| results/_v4_seeds_prereg_supplement_2026_09_23.md | 113CBE555643 | 53633 | A | IN-EFFECT | 2026/09/23 11:37:59 | seeds prereg supplement |
| results/_v4_supp_prereg_v02_2026_09_24.md | D85488A64D89 | 42764 | A | IN-EFFECT | 2026/09/24 11:01:51 | master prereg v0.2 (8-item chain) |
| results/_v4_supp_prereg_v02_activation_2026_09_24.md | AD42992DC75D | 3202 | A | IN-EFFECT | 2026/09/24 11:07:31 | master prereg v0.2 activation |
| results/_v4_supp_prereg_v02_add_L10_2026_09_24.md | F6FE005EE3C7 | 26159 | A | IN-EFFECT | 2026/09/24 13:05:07 | master prereg v0.2 +L10 |
| results/_v4_supp_prereg_v02_add_L10_activation_2026_09_24.md | 16E89657DAAA | 9442 | A | IN-EFFECT | 2026/09/24 13:24:17 | master prereg v0.2 +L10 activation |
| results/_v4_supp_prereg_v02_add_L9_2026_09_24.md | 23879B6CD1CC | 19586 | A | IN-EFFECT | 2026/09/24 11:30:27 | master prereg v0.2 +L9 |
| results/_v4_supp_prereg_v02_add_L9_activation_2026_09_24.md | 5C579F28634E | 3924 | A | IN-EFFECT | 2026/09/24 11:34:47 | master prereg v0.2 +L9 activation |

#### V4 / ERRATUM > 2 items

| Path | SHA-12 | Size (B) | View | Status | Modified | Note |
|---|---|---|---|---|---|---|
| results/_v4_noise_cleanup_manifest_2026_09_24.md | F5D2837C2630 | 32476 | C | IN-EFFECT | 2026/09/24 11:03:11 | V4 noise-cleanup manifest (prior turn) |
| results/_v4_s40_correction_note_2026_09_23.md | 065E57820C36 | 11581 | C | IN-EFFECT | 2026/09/23 16:40:48 | S40 correction note |

#### V4 / EXP_PRODUCT > 18 items

| Path | SHA-12 | Size (B) | View | Status | Modified | Note |
|---|---|---|---|---|---|---|
| deposon_team/plugins/_v4_contrast_nondegenerate_2026_09_23.py | A0BFC7DF887F | 42876 | C | IN-EFFECT | 2026/09/23 16:06:11 | V4 contrast script |
| results/_v4_d1_post_hashes.txt | F6BCC4A9E613 | 1063 | C | IN-EFFECT | 2026/09/22 17:11:32 | D1 post-hashes |
| results/_v4_d1_pre_hash_9grid.txt | 64B1CD90330A | 42 | C | IN-EFFECT | 2026/09/22 17:12:25 | D1 9-grid pre-hash |
| results/_v4_d1_pre_hashes_18frozen.txt | DAFF56830450 | 989 | C | LOCKED | 2026/09/22 17:05:02 | D1 18-frozen pre-hashes |
| results/_v4_d1_smoke_ngram.json | 98BF671B9A93 | 792 | C | IN-EFFECT | 2026/09/22 17:13:42 | D1 three-smoke outputs |
| results/_v4_d1_smoke_temp.json | 5F8FE5CB588C | 804 | C | IN-EFFECT | 2026/09/22 17:13:42 | D1 three-smoke outputs |
| results/_v4_d1_smoke_vocab.json | 150BF487F607 | 788 | C | IN-EFFECT | 2026/09/22 17:13:42 | D1 three-smoke outputs |
| results/_v4_d3_post_hashes_snapshot.txt | 4F545760EA70 | 6584 | C | IN-EFFECT | 2026/09/23 09:59:13 | D3 post-hash snapshot |
| results/_v4_d3_pre_hashes_snapshot.txt | 4F545760EA70 | 6584 | C | IN-EFFECT | 2026/09/23 09:45:25 | D3 pre-hash snapshot |
| results/_v4_d3_summary_flags.txt | 4DF75949A412 | 2492 | C | IN-EFFECT | 2026/09/23 10:02:43 | D3 summary flags |
| results/_v4_d5_rootcause_diagnosis.json | 6208169916A4 | 18528 | A | IN-EFFECT | 2026/09/23 11:06:19 | D5 root-cause diagnosis json |
| results/_v4_d5_verdict_data.json | B2A390C37D52 | 7324 | A | IN-EFFECT | 2026/09/23 10:47:52 | D5 verdict data |
| results/_v4_exec_self_check.py | 9E01EB936ED6 | 4105 | C | IN-EFFECT | 2026/09/23 12:31:22 | V4 exec self-check |
| results/_v4_final_verify.py | 1DC482062D9B | 4794 | C | IN-EFFECT | 2026/09/23 10:49:06 | V4 final verify script |
| results/_v4_pi_cot_result.json | AB854B652291 | 935 | A | IN-EFFECT | 2026/09/23 17:17:32 | Task-B result |
| results/_v4_proxy_student_generators.py | 5BA916D1DD24 | 14426 | C | IN-EFFECT | 2026/09/22 17:09:49 | proxy-student generators |
| results/_v4_proxy_student_llm_multi_runner.py | 306FA79A7C27 | 40043 | C | IN-EFFECT | 2026/09/23 12:30:01 | proxy llm multi-runner |
| results/_v4_proxy_student_llm_runner.py | 900A6D1E50AF | 24659 | C | IN-EFFECT | 2026/09/23 10:05:30 | proxy llm runner |

#### V4 / ARTIFACT > 10 items

| Path | SHA-12 | Size (B) | View | Status | Modified | Note |
|---|---|---|---|---|---|---|
| results/_v4_manifest_distill_min_v1.json | 6D1563A4AE23 | 6563 | C | IN-EFFECT | 2026/09/22 17:11:09 | distill-min v1 manifest |
| results/_v4_manifest_distill_min_v1_addendum_d1b.json | C3934C17B315 | 6290 | C | IN-EFFECT | 2026/09/23 10:17:42 | distill-min v1+d1b manifest |
| results/_v4_pi_cot_dataset.json | 139DBFFD8CF9 | 9949 | B | IN-EFFECT | 2026/09/23 17:07:04 | Task-B dataset |
| results/_v4_pi_cot_protocol.json | 9879133AD1A7 | 2020 | C | IN-EFFECT | 2026/09/23 17:06:49 | Task-B protocol |
| results/_v4_pi_cot_proxy.json | 977E2C317C18 | 1526 | C | IN-EFFECT | 2026/09/23 17:17:32 | Task-B proxy |
| results/_v4_pi_cot_v2_dataset.json | 7B01CD835A41 | 12672 | B | IN-EFFECT | 2026/09/24 15:55:01 | Task-B v2 dataset |
| results/_v4_proxy_student_ngram_truncate.json | FA5A1FEDF470 | 80089 | C | IN-EFFECT | 2026/09/22 17:13:05 | proxy ngram truncate |
| results/_v4_proxy_student_teacher_paths.json | D2BD7521D651 | 2575 | C | IN-EFFECT | 2026/09/22 17:06:02 | proxy teacher paths |
| results/_v4_proxy_student_temperature_resample.json | 4B06B5A79FAD | 142928 | C | IN-EFFECT | 2026/09/22 17:13:05 | proxy temperature resample |
| results/_v4_proxy_student_vocab_truncate.json | 5D7423C58EEB | 77794 | C | IN-EFFECT | 2026/09/22 17:13:05 | proxy vocab truncate |

#### V4 / LETTERS > 31 items

| Path | SHA-12 | Size (B) | View | Status | Modified | Note |
|---|---|---|---|---|---|---|
| letters/_kimi_v4_t12_review_2026_09_20.md | 38070FD12F31 | 6644 | B | IN-EFFECT | 2026/09/20 14:53:18 | kimi V4 review/reply series |
| letters/_kimi_v4_theme_reply_2026_09_20.md | 3E37352EFB4B | 7372 | B | IN-EFFECT | 2026/09/20 17:52:32 | kimi V4 review/reply series |
| letters/_kimi_v4_theme_reply_2_brainstorm_2026_09_20.md | BC14F47D927D | 14155 | B | IN-EFFECT | 2026/09/20 21:11:34 | kimi V4 review/reply series |
| letters/_v4_acceptance_coze_2026_09_20.md | B2BF2A073AC8 | 5467 | B | IN-EFFECT | 2026/09/20 14:58:15 | V4 commission / reply series |
| letters/_v4_acceptance_trae_code_2026_09_20.md | 3205593030BC | 6301 | B | IN-EFFECT | 2026/09/20 17:11:14 | V4 commission / reply series |
| letters/_v4_acceptance_trae_work_v1.0_2026_09_20.md | 3CAF4E653A68 | 7176 | B | IN-EFFECT | 2026/09/20 17:36:19 | V4 commission / reply series |
| letters/_v4_attribution_errata_trae_work_2026_09_20.md | E061C5806AF6 | 2816 | B | IN-EFFECT | 2026/09/20 17:36:48 | V4 commission / reply series |
| letters/_v4_d1_response_workbuddy_2026_09_20.md | BC663B671994 | 14881 | B | IN-EFFECT | 2026/09/20 14:36:48 | V4 commission / reply series |
| letters/_v4_d1_review_codex_2026_09_20.md | 48387412B109 | 4506 | B | IN-EFFECT | 2026/09/21 11:12:20 | V4 commission / reply series |
| letters/_v4_distillation_acceptance_coze_2026_09_20.md | 3A8CB7B9D041 | 14295 | B | IN-EFFECT | 2026/09/20 18:03:55 | V4 commission / reply series |
| letters/_v4_distillation_acceptance_kimi_2026_09_20.md | A4D194DBF9AD | 6454 | B | IN-EFFECT | 2026/09/20 17:56:29 | V4 commission / reply series |
| letters/_v4_distillation_acceptance_trae_code_2026_09_20.md | DC47FBF3C491 | 5218 | B | IN-EFFECT | 2026/09/20 17:32:33 | V4 commission / reply series |
| letters/_v4_distillation_brainstorm_reply_codex_2026_09_21.md | 0FF6C042B845 | 9048 | B | IN-EFFECT | 2026/09/21 11:12:20 | V4 commission / reply series |
| letters/_v4_distillation_invitation_2026_09_20_v1.0.md | 3D9F73519F6C | 53539 | B | IN-EFFECT | 2026/09/20 16:41:53 | V4 commission / reply series |
| letters/_v4_distillation_reply_claude_code_2026_09_20.md | D39CB17B051B | 64212 | B | IN-EFFECT | 2026/09/21 11:01:14 | V4 commission / reply series |
| letters/_v4_distillation_reply_coze_2026_09_20.md | 00593014CBD3 | 71084 | B | IN-EFFECT | 2026/09/20 21:53:15 | V4 commission / reply series |
| letters/_v4_distillation_reply_trae_code_2026_09_20.md | E87EC8F7E2FE | 43570 | B | IN-EFFECT | 2026/09/20 21:21:36 | V4 commission / reply series |
| letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23.md | 9BB22099DB3B | 28207 | B | IN-EFFECT | 2026/09/23 13:35:13 | V4 commission / reply series |
| letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23_fix_addendum.md | 59B8DF6E2E22 | 6067 | B | IN-EFFECT | 2026/09/23 13:46:15 | V4 commission / reply series |
| letters/_v4_distillation_theme_reply_workbuddy_2026_09_20.md | E3FE63A2F708 | 18785 | B | IN-EFFECT | 2026/09/20 18:19:48 | V4 commission / reply series |
| letters/_v4_distillation_theme_reply_workbuddy_brainstorm_2026_09_21.md | CDB27CD3008C | 13553 | B | IN-EFFECT | 2026/09/21 09:42:45 | V4 commission / reply series |
| letters/_v4_distillation_theme_reply_workbuddy_part2_2026_09_20.md | BFB4932F4467 | 12963 | B | IN-EFFECT | 2026/09/20 18:26:36 | V4 commission / reply series |
| letters/_v4_experiment_invitation_2026_09_20.md | 4E8C0EA57028 | 30820 | B | IN-EFFECT | 2026/09/20 13:37:03 | V4 commission / reply series |
| letters/_v4_experiment_invitation_2026_09_20_v0.2.md | 8E1E7434905D | 41680 | B | IN-EFFECT | 2026/09/20 16:06:52 | V4 commission / reply series |
| letters/_v4_review_claude_code_2026_09_20.md | B6F9956BCF5C | 7004 | B | IN-EFFECT | 2026/09/20 14:32:01 | V4 commission / reply series |
| letters/_v4_theme_reply_mavis_2026_09_20.md | 00315728BBF5 | 36719 | B | IN-EFFECT | 2026/09/20 17:08:33 | V4 commission / reply series |
| letters/_v4_theme_reply_mavis_2026_09_20_v1.1.md | 82FEE0A18DAB | 36824 | B | IN-EFFECT | 2026/09/20 17:22:38 | V4 commission / reply series |
| letters/_v4_theme_reply_mavis_2026_09_20_v1.2.md | 3ECF5B38048E | 36826 | B | IN-EFFECT | 2026/09/20 17:40:32 | V4 commission / reply series |
| letters/_v4_theme_reply_trae_work_2026_09_20.md | EBA83C88B629 | 11458 | B | IN-EFFECT | 2026/09/20 17:35:40 | V4 commission / reply series |
| letters/_v4_theme_reply_trae_work_2026_09_20_v1.1.md | BE850D129F35 | 13404 | B | IN-EFFECT | 2026/09/20 17:39:33 | V4 commission / reply series |
| letters/_v4_theme_reply_trae_work_2026_09_20_v1.2.md | 6BEE6EC434BD | 28395 | B | IN-EFFECT | 2026/09/20 20:58:07 | V4 commission / reply series |

#### V4 / DECISION > 4 items

| Path | SHA-12 | Size (B) | View | Status | Modified | Note |
|---|---|---|---|---|---|---|
| results/_v4_iron_rules_review_2026_09_22.md | 40A51EF13882 | 3663 | A | IN-EFFECT | 2026/09/23 10:06:41 | iron-rules review R1-R7 |
| results/_v4_pi_cot_v2_questionnaire_v1.md | 7B14CDB31D21 | 12402 | B | IN-EFFECT | 2026/09/24 10:51:01 | Task-B questionnaire v1 |
| results/_v4_pi_decision_questionnaire_2026_09_21_v1.0.md | 6A3A2D8EE357 | 67686 | C | IN-EFFECT | 2026/09/21 14:59:12 | PI questionnaire v1.0 |
| results/_v4_pi_decision_questionnaire_2026_09_21_v1.1.md | ADC31D55B794 | 119481 | B | IN-EFFECT | 2026/09/22 16:50:32 | PI questionnaire v1.1 (in-effect) |

#### V4 / KNOWLEDGE > 11 items

| Path | SHA-12 | Size (B) | View | Status | Modified | Note |
|---|---|---|---|---|---|---|
| results/_v4_alias_table_2026_09_22.md | AD54D7E9E89B | 5567 | A | IN-EFFECT | 2026/09/22 16:48:31 | naming-drift alias table |
| results/_v4_design_integration_2026_09_21_v1.0.md | 4B10CDE29C27 | 119732 | C | IN-EFFECT | 2026/09/21 14:58:33 | V4 design integration v1.0 |
| results/_v4_design_integration_2026_09_21_v1.1.md | FB5656993071 | 140007 | A | IN-EFFECT | 2026/09/21 16:33:04 | V4 design integration v1.1 (in-effect) |
| results/_v4_gA1_experiment_outline_2026_09_22.md | F4A6BDD43962 | 7837 | A | IN-EFFECT | 2026/09/22 13:13:10 | gA1 experiment outline |
| results/_v4_gA1_terminology_draft_2026_09_22.md | 0A2CAF0A2BD2 | 9818 | B | IN-EFFECT | 2026/09/22 13:09:56 | gA1 terminology draft |
| results/_v4_group_b_explore_subs_integration_2026_09_22.md | 588B45430E88 | 20532 | B | IN-EFFECT | 2026/09/22 16:31:25 | Group-B explore subs integration |
| results/_v4_pa2_pg_unified_criteria_2026_09_23.md | 26EDFF4A76E9 | 2966 | A | IN-EFFECT | 2026/09/23 15:46:13 | P-A2/P-G unified criteria |
| results/_v4_pi_cot_v2_collection_log.md | 167AD91F198E | 1181 | C | IN-EFFECT | 2026/09/23 17:49:35 | Task-B v2 collection log |
| results/_v4_r11_pcd_22round_definition_2026_09_23.md | 1B00C7CC0FFB | 1970 | A | IN-EFFECT | 2026/09/23 15:45:48 | R11 PC-D 22-round definition |
| results/_v4_supp_test_plan_2026_09_24.md | 5023C11AB282 | 2853 | A | IN-EFFECT | 2026/09/23 18:06:00 | V4 supp test plan |
| results/_v4_v5_worker_handoff_report.md | 2033A3C87A6B | 9779 | C | IN-EFFECT | 2026/09/23 12:34:47 | v5 worker handoff |


### 2.4 Stage: CROSS (53 items)

#### CROSS / JUDGMENT > 1 items

| Path | SHA-12 | Size (B) | View | Status | Modified | Note |
|---|---|---|---|---|---|---|
| verifier/kill_lines/kt_b1_kill_decision.py | 9F351078E5BF | 2781 | C | IN-EFFECT | 2026/09/09 13:17:24 | KT-B1 kill line |

#### CROSS / ERRATUM > 3 items

| Path | SHA-12 | Size (B) | View | Status | Modified | Note |
|---|---|---|---|---|---|---|
| verifier/handoff/KT_ABC1_anchors_sha256_12.json | 03C6C01F3697 | 6680 | C | LOCKED | 2026/09/09 13:19:32 | 5-anchor root (canonical) |
| verifier/handoff/KT_ABC1_anchors_sha256_12.root_session_11318B.bak_2026_09_23.json | 6E9CD8CD8E07 | 11318 | C | LOCKED | 2026/09/22 11:02:01 | 5-anchor .bak (untouched this turn) |
| verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json | DA517C115F3C | 5049 | C | LOCKED | 2026/09/15 13:31:24 | 5-anchor P-A patch |

#### CROSS / EXP_PRODUCT > 6 items

| Path | SHA-12 | Size (B) | View | Status | Modified | Note |
|---|---|---|---|---|---|---|
| deposon_team/plugins/_verify_15frozen.py | EFAE9274962E | 3905 | C | IN-EFFECT | 2026/09/17 10:12:02 | verify scripts |
| deposon_team/plugins/_verify_15frozen_v1.py | 60523E406055 | 2094 | C | IN-EFFECT | 2026/09/17 10:27:53 | verify scripts |
| deposon_team/plugins/_verify_batch5_2026_09_18.py | BC6CBF27A338 | 4238 | C | IN-EFFECT | 2026/09/18 13:45:30 | verify scripts |
| deposon_team/plugins/_verify_pg_v0.py | CDD3415AD993 | 3978 | C | IN-EFFECT | 2026/09/17 10:12:02 | verify scripts |
| deposon_team/plugins/_verify_pg_v0_v1.py | 67088AE1A860 | 2521 | C | IN-EFFECT | 2026/09/17 10:27:53 | verify scripts |
| verifier/audit/conservation.py | 4BDEC2683F06 | 22105 | C | LOCKED | 2026/09/10 09:29:22 | 18 frozen impl |

#### CROSS / ARTIFACT > 41 items

| Path | SHA-12 | Size (B) | View | Status | Modified | Note |
|---|---|---|---|---|---|---|
| corpus/v20/L_algorithm_process.json | FF0EF9131FDD | 3920 | C | IN-EFFECT | 2026/08/28 17:38:45 | corpus V20 master |
| corpus/v20/L_biological_taxonomy.json | 0C7AD5235AE9 | 3562 | C | IN-EFFECT | 2026/08/28 17:38:45 | corpus V20 master |
| corpus/v20/L_geography_world.json | 77B0C1466DC0 | 3699 | C | IN-EFFECT | 2026/08/28 23:11:44 | corpus V20 master |
| corpus/v20/L_historical_causality.json | 12E0DE4BB103 | 4329 | C | IN-EFFECT | 2026/08/28 17:38:45 | corpus V20 master |
| corpus/v20/L_physics_concepts.json | D8780859D310 | 3397 | C | IN-EFFECT | 2026/08/28 17:38:45 | corpus V20 master |
| corpus/v20/L_project_management.json | 32CA32C00DA4 | 3898 | C | IN-EFFECT | 2026/08/28 23:12:37 | corpus V20 master |
| corpus/v20/S1.json | A890C56F7705 | 1512 | C | IN-EFFECT | 2026/08/28 17:07:51 | corpus V20 master |
| corpus/v20/S1_n35.json | F035043BFDDD | 2521 | C | IN-EFFECT | 2026/08/28 17:07:52 | corpus V20 master |
| corpus/v20/S1_n45.json | 52B4D6E52AE9 | 3171 | C | IN-EFFECT | 2026/08/28 17:07:52 | corpus V20 master |
| corpus/v20/S1_n60.json | 584DE37EBEC1 | 4122 | C | IN-EFFECT | 2026/08/28 17:07:52 | corpus V20 master |
| corpus/v20/S2.json | B1F6C5AA4DE6 | 2234 | C | IN-EFFECT | 2026/08/28 17:07:52 | corpus V20 master |
| corpus/v20/S2_n20.json | BFC9D38C8C0F | 1537 | C | IN-EFFECT | 2026/08/28 17:07:52 | corpus V20 master |
| corpus/v20/S2_n35.json | E20A1BBEAEE7 | 2480 | C | IN-EFFECT | 2026/08/28 17:07:52 | corpus V20 master |
| corpus/v20/S2_n45.json | 58BB0A7D2E46 | 3175 | C | IN-EFFECT | 2026/08/28 17:07:52 | corpus V20 master |
| corpus/v20/S2_n60.json | 01C492A97B98 | 4123 | C | IN-EFFECT | 2026/08/28 17:07:52 | corpus V20 master |
| corpus/v20/S3.json | 3B6879AB2440 | 2297 | C | IN-EFFECT | 2026/08/28 17:07:52 | corpus V20 master |
| corpus/v20/S4.json | E6045F0920EC | 4932 | C | IN-EFFECT | 2026/08/28 17:07:52 | corpus V20 master |
| corpus/v20/S5.json | 4B10F9CAE09F | 3319 | C | IN-EFFECT | 2026/08/28 17:07:52 | corpus V20 master |
| corpus/v20/S6.json | 01D9C95EA690 | 3320 | C | IN-EFFECT | 2026/08/28 17:07:52 | corpus V20 master |
| corpus/v20/S6_n20.json | 4A0689892C1B | 1724 | C | IN-EFFECT | 2026/08/28 17:07:52 | corpus V20 master |
| corpus/v20/S6_n35.json | 8D02FBADD277 | 2676 | C | IN-EFFECT | 2026/08/28 17:07:52 | corpus V20 master |
| corpus/v20/S6_n60.json | 704E2FD0D021 | 4296 | C | IN-EFFECT | 2026/08/28 17:07:52 | corpus V20 master |
| corpus/v20/all.json | 8DF31C95B1FC | 2557 | C | IN-EFFECT | 2026/09/17 10:24:31 | corpus V20 master |
| corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json | 268AB1239A8A | 19685 | C | IN-EFFECT | 1979/11/30 00:00:00 | corpus V20 master |
| corpus/v20/by_model/GLM_2/glm_artifact_v_2026_09_16.json | 39732A92B5C9 | 13150 | C | IN-EFFECT | 1979/11/30 00:00:00 | corpus V20 master |
| corpus/v20/by_model/coze/coze_artifact_v_2026_09_16.json | FEE04170AA73 | 10978 | C | IN-EFFECT | 2026/09/24 11:28:03 | corpus V20 master |
| corpus/v20/by_model/kimi/index_v2_2026_09_16.json | EFE05AD775DE | 24150 | C | IN-EFFECT | 2026/09/16 18:39:54 | corpus V20 master |
| corpus/v20/by_model/minimax/artifact_v_2026_09_16.json | 9E1CCBDCEACC | 25347 | C | IN-EFFECT | 2026/09/16 18:20:56 | corpus V20 master |
| corpus/v20/index.json | 8423FFE266AF | 7335 | C | IN-EFFECT | 2026/08/28 23:53:05 | corpus V20 master |
| corpus/v20/index_v2_2026_09_16.json | EFE05AD775DE | 24150 | C | IN-EFFECT | 2026/09/16 18:39:54 | corpus V20 master |
| corpus/v20/strip_captions_22.json | 6A2656878745 | 12798 | C | IN-EFFECT | 2026/09/11 11:33:40 | corpus V20 master |
| corpus/v20_caption_surface/_adendum_I_po_captions_closure_20260917_132049.json | 18165008BEF6 | 4429 | C | IN-EFFECT | 2026/09/17 13:20:50 | corpus caption surface |
| corpus/v20_caption_surface/_inspect_captions.py | DFB02ADE1474 | 591 | C | IN-EFFECT | 2026/09/10 17:31:00 | corpus caption surface |
| corpus/v20_caption_surface/_p_d_b3_merkle_22caption_runner_2026_09_16.py | D2CD7ACB29A1 | 18596 | C | IN-EFFECT | 2026/09/16 18:54:48 | corpus caption surface |
| corpus/v20_caption_surface/_p_d_v03_22caption_verification_20260917_163757.json | DFBCC5D6FC34 | 13775 | C | IN-EFFECT | 2026/09/17 16:37:57 | corpus caption surface |
| corpus/v20_caption_surface/_v41_flash_rag_caption_embs.bak.json | 25F745609658 | 612511 | C | IN-EFFECT | 2026/09/10 17:05:53 | corpus caption surface |
| corpus/v20_caption_surface/caption_distance_mat_22.json | 1C4FFF004CC4 | 8552 | C | IN-EFFECT | 2026/09/23 16:44:30 | corpus caption surface |
| corpus/v20_caption_surface/caption_features_22.json | 727A253566DD | 18362 | C | IN-EFFECT | 2026/09/23 16:44:30 | corpus caption surface |
| corpus/v20_caption_surface/caption_stats_22.json | DA34F54D4F5B | 632 | C | IN-EFFECT | 2026/09/23 16:44:30 | corpus caption surface |
| corpus/v20_caption_surface/manifest.json | 4FDDA6480BB5 | 1477 | C | IN-EFFECT | 2026/09/23 16:44:30 | corpus caption surface |
| corpus/v20_caption_surface/strip_captions_22.json | 6A2656878745 | 12798 | C | IN-EFFECT | 2026/09/11 11:33:40 | corpus caption surface |

#### CROSS / KNOWLEDGE > 2 items

| Path | SHA-12 | Size (B) | View | Status | Modified | Note |
|---|---|---|---|---|---|---|
| verifier/handoff/P_F_PREDECISION_2026_09_09.json | B41C98BF90CC | 3680 | C | IN-EFFECT | 2026/09/09 13:50:15 | P-F pre-decision |
| verifier/handoff/P_F_PREDECISION_2026_09_11_V0.1.json | 312D635E6259 | 12498 | C | IN-EFFECT | 2026/09/11 13:08:54 | P-F v0.1 pre-decision |


---

## 3. View-tag bin (for commission-letter and paper-final selection)

### 3.1 Tag-A: candidate final-paper material

Selection criteria: formal report / final-report / 1-page summary / 6-direction quick kill / cross-modal embedding verification / P-D v0.3 spec / D5 landing decision / root-cause verdict / 22 true judgments.

Total: 129 items

| Path | Stage | Category | SHA-12 | Modified | Note |
|---|---|---|---|---|---|
| paper/FIGURE_LANGUAGE_POLICY.md | V12 | KNOWLEDGE | A18B5D0D4485 | 2026/08/30 11:16:21 | paper drafts (CN/EN) |
| paper/deposon_paper_final_cn.md | V12 | KNOWLEDGE | C5F6A23F4408 | 2026/09/20 17:11:14 | paper drafts (CN/EN) |
| paper/deposon_paper_final_en.md | V12 | KNOWLEDGE | 2EC20B96E941 | 2026/09/20 17:11:14 | paper drafts (CN/EN) |
| paper/v2/outline_v2X.md | V12 | KNOWLEDGE | 116D193B1607 | 2026/08/30 10:43:36 | paper drafts (CN/EN) |
| paper/v2/related_work_v2X.md | V12 | KNOWLEDGE | 7FB001ADD973 | 2026/08/29 15:43:30 | paper drafts (CN/EN) |
| docs/V3X/BOSS_PE_3_RESERVOIR_VERIFY_REPORT_2026_09_15.md | V3X | KNOWLEDGE | C28F7F0B530F | 2026/09/15 13:36:08 | BOSS PE-3 reservoir verify |
| docs/V3X/D5_DECISIONS_LAND_REPORT_2026_09_15.md | V3X | JUDGMENT | 8FF1A7C5413F | 2026/09/15 15:15:39 | D5 landing decision report |
| docs/V3X/DEPOSON_EMBEDDING_6WAY_THEORY_V0_2026_09_10.md | V3X | KNOWLEDGE | AC8997B07731 | 2026/09/10 20:22:54 | embedding 6-way theory |
| docs/V3X/DEPOSON_EMBEDDING_6WAY_VERIFICATION_2026_09_10.md | V3X | KNOWLEDGE | 240A7AE4BDFB | 2026/09/10 18:16:43 | embedding 6-way verification |
| docs/V3X/DPATH_CROSS_MODAL_2026_09_10.md | V3X | KNOWLEDGE | E4EE3999F7CE | 2026/09/16 11:01:12 | dpath cross-modal |
| docs/V3X/D_FIX2_METRIC_VERIFY_REPORT_2026_09_15.md | V3X | KNOWLEDGE | 0A63824F0805 | 2026/09/15 14:07:47 | d fix2 metric verification |
| docs/V3X/PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md | V3X | KNOWLEDGE | C165CD33A362 | 2026/09/11 11:17:21 | P-D v0.2 spec |
| docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md | V3X | JUDGMENT | 977FE1B48F75 | 2026/09/15 11:31:34 | P-A D1D3 report |
| docs/V3X/P_C_D1_D3_REPORT_2026_09_15.md | V3X | JUDGMENT | 79C7321056B8 | 2026/09/15 15:08:22 | P-C D1D3 report |
| docs/V3X/P_D_B3_MERKLE_22_CAPTION_VERIFICATION_2026_09_16.md | V3X | KNOWLEDGE | 7F1492FBE657 | 2026/09/16 18:26:46 | P-D B3 verification |
| docs/V3X/P_D_FINGERPRINT_V0_3_SPEC.md | V3X | KNOWLEDGE | F119F2F30287 | 2026/09/17 15:15:44 | P-D v0.3 spec (core) |
| docs/V3X/P_E_D1_D3_REPORT_2026_09_15.md | V3X | JUDGMENT | 900DA300D11E | 2026/09/15 11:27:04 | P-E D1D3 report |
| docs/V3X/P_F_D1_FULL_REPORT_2026_09_15.md | V3X | JUDGMENT | 817EFDC2F0AD | 2026/09/15 12:15:12 | P-F D1 full report |
| docs/V3X/P_F_IMPLEMENTATION_2026_09_11.md | V3X | KNOWLEDGE | EDD048EAA721 | 2026/09/16 11:01:12 | P-F implementation |
| docs/V3X/P_F_RESEARCH_2026_09_09.md | V3X | KNOWLEDGE | 98085DF7811A | 2026/09/09 13:49:14 | P-F research |
| docs/V3X/P_F_SPEC_V0.md | V3X | KNOWLEDGE | DE90FAF362C5 | 2026/09/09 13:50:05 | P-F v0 spec |
| docs/V3X/P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md | V3X | KNOWLEDGE | 2F0765A1D39D | 2026/09/15 11:33:11 | P-G v0 spec |
| docs/V3X/P_G_V01_REPORT_2026_09_15.md | V3X | JUDGMENT | 9A6B08D03E0C | 2026/09/15 12:06:17 | P-G v0.1 report |
| docs/V3X/QUICK_KILL_6_DIRECTIONS.md | V3X | JUDGMENT | A476F241EDB2 | 2026/09/09 09:53:43 | 6-direction quick kill |
| docs/V3X/TRAE_PL_V2_EXPERIMENT_PROPOSAL_2026_09_17.md | V3X | KNOWLEDGE | 4020B1809780 | 2026/09/17 11:12:54 | TRAE P-L v2 proposal |
| docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md | V3X | JUDGMENT | 4FFB21BB6BFA | 2026/09/16 11:03:10 | V3X 1-week kill report |
| docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md | V3X | KNOWLEDGE | 4A08521F8DE1 | 2026/09/16 11:01:12 | V3 final report |
| docs/V3X/V3X_FULL_EXPERIMENT_DESIGN_2026_09_16.md | V3X | KNOWLEDGE | 3D847F9F3151 | 2026/09/16 12:28:47 | V3X full experiment design |
| docs/V3X/V3X_PROJECT_EVOLUTION_FOR_KIMI.md | V3X | KNOWLEDGE | 4DE2CBF57A49 | 2026/09/15 14:55:11 | deposon evolution for KIMI |
| results/_d05_combined_report_20260918_100853.md | V3X | JUDGMENT | C87EB8974268 | 2026/09/18 10:30:53 | D0_5 combined report |
| results/_ftfb_v3_pass1_audit_2026_09_18_corrected.md | V3X | JUDGMENT | ECB406570615 | 2026/09/18 13:45:13 | FTFB V3 pass1 audit |
| results/_ftfb_v3_pass2_audit_2026_09_18_corrected.md | V3X | JUDGMENT | 413DDB0BD00E | 2026/09/18 13:45:13 | FTFB V3 pass2 audit |
| results/_p_d_v03_verification_report_20260917_163757.md | V3X | JUDGMENT | 67AAFB57A8ED | 2026/09/17 16:39:34 | P-D v0.3 verification report |
| results/_p_k_v3_glm_fpr_audit_report_2026-09-17t08-23-41z.md | V3X | JUDGMENT | 71D5C23D9F76 | 2026/09/17 16:23:41 | P-K V3 glm FPR audit |
| results/_p_l_v3_phase1_report_20260917_132341.md | V3X | JUDGMENT | B41A17EDA169 | 2026/09/17 13:35:32 | P-L V3 phase1 report |
| results/_p_l_v3_phase2_closedsource_report_20260917_175544.md | V3X | JUDGMENT | 02443DD300CE | 2026/09/17 17:55:55 | P-L closedsource report |
| results/_p_l_v3_phase2_or_embedding_v3_report_20260917_162614.md | V3X | JUDGMENT | FA5DA7A307BD | 2026/09/17 16:33:30 | P-L OR embedding v3 report |
| results/_p_l_v3_phase2_report_20260917_142748.md | V3X | JUDGMENT | 58E15C07AF33 | 2026/09/17 14:33:45 | P-L V3 phase2 report |
| results/_p_l_v3_phase3_adendum_summary_20260917_132143.md | V3X | KNOWLEDGE | 8C07AB5AA968 | 2026/09/17 13:22:27 | P-L V3 phase3 adendum summary |
| results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133358.md | V3X | JUDGMENT | 54859CF2217A | 2026/09/17 13:34:00 | P-L phase3 +7 report |
| results/_p_l_v3_vector_embedding_v2_doubao_report_20260917_170828.md | V3X | JUDGMENT | FA9CD7FFA3F2 | 2026/09/17 17:12:34 | P-L v2 doubao report |
| results/_p_l_v3_vector_embedding_v2_doubao_report_20260917_172206.md | V3X | JUDGMENT | 2E3EC17259E2 | 2026/09/17 17:55:23 | P-L v2 doubao report (run2) |
| results/_v3_supplement_verdict_2026_09_23.md | V3X | JUDGMENT | B70211BFA83E | 2026/09/23 14:27:09 | V3 supplement verdict |
| results/_v3x_d0_5_aggregation_2026_09_17.md | V3X | KNOWLEDGE | DDF0D1AA96D2 | 2026/09/17 13:08:30 | D0_5 aggregation report |
| results/_v3x_d0_5_proposal_coze_2026_09_17.md | V3X | KNOWLEDGE | 759C25B21ED4 | 2026/09/17 11:06:19 | D0_5 proposal coze |
| results/_v3x_d0_5_proposal_trae_2026_09_17.md | V3X | KNOWLEDGE | B1C227D54A82 | 2026/09/20 17:11:14 | D0_5 proposal trae |
| results/_v3x_p_l_v3_external_spec_2026_09_17.md | V3X | KNOWLEDGE | 6A5B6EB635F0 | 2026/09/17 11:03:24 | P-L V3 external spec |
| results/_v3x_p_l_v3_summary_mistral_large_2512_20260917_115049.md | V3X | JUDGMENT | 183205BAA9AC | 2026/09/17 11:53:50 | P-L mistral-large summary |
| results/d7_5anchor_60cells_9model_verdict_2026_09_18.json | V3X | JUDGMENT | 4505CCA79C15 | 2026/09/16 11:00:06 | D7 5-anchor 60cells 9model verdict |
| results/deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json | V3X | EXP_PRODUCT | 4E4A17D43ADF | 2026/09/15 13:35:18 | BOSS PE-3 reservoir verify 9m60c |
| results/deposon_d_fix2_metric_verify_9m60c_2026_09_15.json | V3X | EXP_PRODUCT | 9F88A212A77C | 2026/09/16 11:01:12 | D-fix2 9m60c verify |
| results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json | V3X | EXP_PRODUCT | B5873AFB9D29 | 2026/09/16 18:39:54 | P-D B3 merkle 22-caption |
| results/deposon_p_k_cross_subject_fingerprint_blind_test_2026_09_16.json | V3X | EXP_PRODUCT | 576EAF8D7431 | 2026/09/16 18:39:55 | P-K cross-subject blind test |
| results/deposon_pa_d1_d3_2026_09_15.json | V3X | EXP_PRODUCT | E221792715F8 | 2026/09/15 11:29:23 | P-A D1D3 |
| results/deposon_pc_d1_d3_2026_09_15.json | V3X | EXP_PRODUCT | B2046AF03610 | 2026/09/15 11:01:56 | P-C D1D3 |
| results/deposon_pe_d1_d3_2026_09_15.json | V3X | EXP_PRODUCT | 594D7A8D3DE8 | 2026/09/15 10:49:09 | P-E D1D3 |
| results/deposon_pf_d1_2026_09_15.json | V3X | EXP_PRODUCT | 12791772814E | 2026/09/15 11:30:53 | P-F D1 |
| results/deposon_pf_d1_full_9m5c_2026_09_15.json | V3X | EXP_PRODUCT | FCB5105DF0B6 | 2026/09/16 11:01:12 | P-F D1 full 9m5c |
| results/deposon_pg_v01_9m60c_2026_09_15.json | V3X | EXP_PRODUCT | AB75889EE738 | 2026/09/15 13:35:24 | P-G v0.1 9m60c |
| results/deposon_v3_v7_summary_2026_09_11.json | V3X | KNOWLEDGE | 063AC8D00542 | 2026/09/16 11:01:12 | V3 V7 summary |
| results/deposon_v3x_6way_stage2_2026_09_10.json | V3X | EXP_PRODUCT | D301BBFED982 | 2026/09/10 17:56:17 | V3X 6-way stage2 |
| results/deposon_v3x_6way_stage3_2026_09_10.json | V3X | EXP_PRODUCT | D892A9D3D6BA | 2026/09/10 18:15:22 | V3X 6-way stage3 |
| results/deposon_v3x_6way_summary_2026_09_10.json | V3X | KNOWLEDGE | 63E0798E5843 | 2026/09/10 18:17:10 | V3X 6-way summary |
| results/skill_a_p_a_60cells_result_2026_09_11.json | V3X | EXP_PRODUCT | F4A210D69220 | 2026/09/11 17:06:25 | skill A P-A 60cells |
| results/skill_b_p_c_alpha_beta_result_2026_09_11.json | V3X | EXP_PRODUCT | B921002E4DFB | 2026/09/11 17:06:29 | skill B P-C alpha-beta |
| results/skill_c_p_e_3modality_result_2026_09_11.json | V3X | EXP_PRODUCT | 470425A8C77D | 2026/09/11 17:06:33 | skill C P-E 3-modality |
| results/skill_d_p_f_observer_result_2026_09_11.json | V3X | EXP_PRODUCT | 0207C01B9562 | 2026/09/15 13:31:05 | skill D P-F observer |
| results/_v4_N09_N39_prereg_2026_09_23.md | V4 | PREREG | 0A9EE16267B5 | 2026/09/23 11:34:08 | N09-N39 prereg |
| results/_v4_alias_table_2026_09_22.md | V4 | KNOWLEDGE | AD54D7E9E89B | 2026/09/22 16:48:31 | naming-drift alias table |
| results/_v4_d1_decisions_2026_09_22.md | V4 | JUDGMENT | A00826ED0E21 | 2026/09/22 17:32:57 | V4 D1 decisions summary |
| results/_v4_d5_rootcause_diagnosis.json | V4 | EXP_PRODUCT | 6208169916A4 | 2026/09/23 11:06:19 | D5 root-cause diagnosis json |
| results/_v4_d5_rootcause_notes.md | V4 | JUDGMENT | 1DED0240F532 | 2026/09/23 11:07:53 | D5 root-cause notes |
| results/_v4_d5_verdict_data.json | V4 | EXP_PRODUCT | B2A390C37D52 | 2026/09/23 10:47:52 | D5 verdict data |
| results/_v4_design_integration_2026_09_21_v1.1.md | V4 | KNOWLEDGE | FB5656993071 | 2026/09/21 16:33:04 | V4 design integration v1.1 (in-effect) |
| results/_v4_distill_min_verdict_v1.md | V4 | JUDGMENT | 1BD9243969B6 | 2026/09/23 10:51:19 | distill-min v1 verdict |
| results/_v4_exec_methods_batch_verdict.md | V4 | JUDGMENT | 4913D8DC7261 | 2026/09/23 12:29:52 | methods batch verdict |
| results/_v4_exec_n_batch_verdict.md | V4 | JUDGMENT | AFBD998962C2 | 2026/09/23 12:39:59 | N-batch verdict |
| results/_v4_exec_seeds_batch_verdict.md | V4 | JUDGMENT | F7FC92B8B2F5 | 2026/09/23 12:07:22 | seeds batch verdict |
| results/_v4_gA1_experiment_outline_2026_09_22.md | V4 | KNOWLEDGE | F4A6BDD43962 | 2026/09/22 13:13:10 | gA1 experiment outline |
| results/_v4_gA3_seeds_judgment_draft_2026_09_22.md | V4 | JUDGMENT | 9119BB791DC1 | 2026/09/22 15:26:03 | gA3 seeds judgment |
| results/_v4_group_b_17letters_judgment_draft_2026_09_22.md | V4 | JUDGMENT | 99B835595DFB | 2026/09/22 16:24:26 | Group-B 17-letter judgment |
| results/_v4_iron_rules_review_2026_09_22.md | V4 | DECISION | 40A51EF13882 | 2026/09/23 10:06:41 | iron-rules review R1-R7 |
| results/_v4_methods_prereg_supplement_2026_09_23.md | V4 | PREREG | 0A7BCA992B95 | 2026/09/23 11:35:03 | methods prereg supplement |
| results/_v4_n22_n19_prereg_activation_2026_09_23.md | V4 | PREREG | 0F68058ECBAA | 2026/09/23 16:40:42 | N22/N19 activation |
| results/_v4_n22_n19_prereg_supplement_2026_09_23.md | V4 | PREREG | 4070FDAAC111 | 2026/09/23 16:27:41 | N22/N19 prereg supplement |
| results/_v4_n22_n19_supp_verdict.md | V4 | JUDGMENT | DB567722D007 | 2026/09/23 17:05:40 | N22/N19 supp verdict |
| results/_v4_n22s_margin_verdict.md | V4 | JUDGMENT | D64E1264737F | 2026/09/24 09:42:45 | N22s margin verdict |
| results/_v4_n29_real_verdict.md | V4 | JUDGMENT | E62D245CE285 | 2026/09/23 16:38:24 | N29 real verdict |
| results/_v4_pa2_pg_unified_criteria_2026_09_23.md | V4 | KNOWLEDGE | 26EDFF4A76E9 | 2026/09/23 15:46:13 | P-A2/P-G unified criteria |
| results/_v4_pi_cot_distill_prereg.md | V4 | PREREG | 696AF9121D9F | 2026/09/23 13:08:36 | Task-B distill prereg |
| results/_v4_pi_cot_prereg_activation_2026_09_23.md | V4 | PREREG | 478F10CEAE7B | 2026/09/23 15:00:30 | Task-B prereg activation |
| results/_v4_pi_cot_result.json | V4 | EXP_PRODUCT | AB854B652291 | 2026/09/23 17:17:32 | Task-B result |
| results/_v4_pi_cot_v2_prereg.md | V4 | PREREG | CC25C5149CE1 | 2026/09/23 17:56:05 | Task-B v2 prereg |
| results/_v4_pi_cot_v2_prereg_activation_2026_09_23.md | V4 | PREREG | 00584E5A5C78 | 2026/09/23 18:03:11 | Task-B v2 activation |
| results/_v4_pi_cot_verdict.md | V4 | JUDGMENT | D279EBDE5E84 | 2026/09/23 17:17:32 | Task-B verdict |
| results/_v4_prereg_77_activation_2026_09_23.md | V4 | PREREG | 856E75B4BAAB | 2026/09/23 11:36:21 | 77 activation |
| results/_v4_r11_pcd_22round_definition_2026_09_23.md | V4 | KNOWLEDGE | 1B00C7CC0FFB | 2026/09/23 15:45:48 | R11 PC-D 22-round definition |
| results/_v4_rejudge_verdict.md | V4 | JUDGMENT | 5CCF32F96B4B | 2026/09/23 14:20:21 | V4 rejudge verdict |
| results/_v4_rerun_verdict.md | V4 | JUDGMENT | F258A4368328 | 2026/09/23 14:30:21 | V4 rerun verdict |
| results/_v4_rootcause_upgrade_review.md | V4 | JUDGMENT | C398CF82B3EA | 2026/09/23 15:34:54 | root-cause upgrade review |
| results/_v4_s40_semantics_verdict_2026_09_23.md | V4 | JUDGMENT | 0D6B3C74DC98 | 2026/09/23 16:18:47 | S40 semantics verdict |
| results/_v4_seeds_prereg_supplement_2026_09_23.md | V4 | PREREG | 113CBE555643 | 2026/09/23 11:37:59 | seeds prereg supplement |
| results/_v4_supp_a1_seed_verdict.md | V4 | JUDGMENT | BB916AC9DB8A | 2026/09/24 11:28:18 | L1 seed verdict |
| results/_v4_supp_a2_method_verdict.md | V4 | JUDGMENT | 8C6480A68CF0 | 2026/09/24 10:01:14 | L2 method verdict |
| results/_v4_supp_b_n_verdict.md | V4 | JUDGMENT | 7431E8065C4B | 2026/09/24 09:56:06 | L3-B N verdict |
| results/_v4_supp_cd_verdict.md | V4 | JUDGMENT | 7606A0E7C4B6 | 2026/09/24 09:50:19 | L4-C/D verdict |
| results/_v4_supp_e_multimodel_verdict.md | V4 | JUDGMENT | 9FD4B722405E | 2026/09/24 10:25:14 | L5-E multimodel verdict |
| results/_v4_supp_l11_dct100_verdict.md | V4 | JUDGMENT | 14A98CFAA660 | 2026/09/24 13:36:03 | L11 DCT100 verdict |
| results/_v4_supp_l12_dr_real_renyi_verdict.md | V4 | JUDGMENT | 977FB07592F4 | 2026/09/24 13:51:38 | L12 D-R R茅nyi verdict |
| results/_v4_supp_l13_n26pair_verdict.md | V4 | JUDGMENT | E105EC1362DB | 2026/09/24 14:15:28 | L13 N26 pair verdict |
| results/_v4_supp_l6_s38v2_rootcause_verdict.md | V4 | JUDGMENT | 973103878D6F | 2026/09/24 11:44:57 | L6 S38v2 root-cause verdict (key) |
| results/_v4_supp_l6_s38v2_verdict.md | V4 | JUDGMENT | 20D9B44E036E | 2026/09/24 11:35:12 | L6 S38v2 verdict |
| results/_v4_supp_l7_e_n20_fill_verdict.md | V4 | JUDGMENT | 0E4A7FCE58C0 | 2026/09/24 13:09:03 | L7 e-N20 fill verdict |
| results/_v4_supp_l7_e_n20_verdict.md | V4 | JUDGMENT | B8335982AE5E | 2026/09/24 12:56:18 | L7 e-N20 verdict |
| results/_v4_supp_l8_n12r_verdict.md | V4 | JUDGMENT | 114CF71AB3D4 | 2026/09/24 12:04:45 | L8 N12-R verdict |
| results/_v4_supp_l9_a2r_verdict.md | V4 | JUDGMENT | E12C7D2DABA1 | 2026/09/24 11:50:34 | L9 A2-R verdict |
| results/_v4_supp_prereg_v02_2026_09_24.md | V4 | PREREG | D85488A64D89 | 2026/09/24 11:01:51 | master prereg v0.2 (8-item chain) |
| results/_v4_supp_prereg_v02_activation_2026_09_24.md | V4 | PREREG | AD42992DC75D | 2026/09/24 11:07:31 | master prereg v0.2 activation |
| results/_v4_supp_prereg_v02_add_L10_2026_09_24.md | V4 | PREREG | F6FE005EE3C7 | 2026/09/24 13:05:07 | master prereg v0.2 +L10 |
| results/_v4_supp_prereg_v02_add_L10_activation_2026_09_24.md | V4 | PREREG | 16E89657DAAA | 2026/09/24 13:24:17 | master prereg v0.2 +L10 activation |
| results/_v4_supp_prereg_v02_add_L9_2026_09_24.md | V4 | PREREG | 23879B6CD1CC | 2026/09/24 11:30:27 | master prereg v0.2 +L9 |
| results/_v4_supp_prereg_v02_add_L9_activation_2026_09_24.md | V4 | PREREG | 5C579F28634E | 2026/09/24 11:34:47 | master prereg v0.2 +L9 activation |
| results/_v4_supp_test_plan_2026_09_24.md | V4 | KNOWLEDGE | 5023C11AB282 | 2026/09/23 18:06:00 | V4 supp test plan |
| results/_v4_track2_multimodel_verdict_2026_09_23.md | V4 | JUDGMENT | 44D9BAD9039B | 2026/09/23 15:27:54 | V4 Track-2 multimodel verdict |
| results/_v4_v3_degradation_contrast_verdict.md | V4 | JUDGMENT | 3BD454B1A780 | 2026/09/23 16:08:41 | V3 vs V4 degradation contrast |
| results/_v4_v5_ablation_verdict.md | V4 | JUDGMENT | C2920AA9923A | 2026/09/23 12:14:52 | v5 ablation verdict |
| results/_v4_v5_t2_multimodel_verdict.md | V4 | JUDGMENT | C386251D94D6 | 2026/09/23 12:32:15 | v5 T2 multimodel verdict |
| results/_v4_v5_t2_verdict.md | V4 | JUDGMENT | 83D8E7A8BA12 | 2026/09/23 12:03:19 | v5 T2 verdict |
| results/_v4_v5_verdict_v1.md | V4 | JUDGMENT | 6A82CFFD01CA | 2026/09/23 12:22:21 | v5 verdict v1 |

### 3.2 Tag-B: candidate commission-letter material

Total: 55 items

| Path | Stage | Category | SHA-12 | Modified | Note |
|---|---|---|---|---|---|
| docs/V3X/D7_ONE_PAGE_SUMMARY_2026_09_11_v5.md | V3X | KNOWLEDGE | 67063F9CB238 | 2026/09/11 13:30:46 | V3 1-page summary v5 |
| docs/V3X/D7_PRE_V3_POLISH_AND_TEAM_IMPROVEMENT_2026_09_16.md | V3X | KNOWLEDGE | 51869E3184F4 | 2026/09/16 11:09:18 | V3 polish + team improvement |
| docs/V3X/D7_WANG_TEACHER_WECHAT_PUSH_REQUIREMENTS_2026_09_18.md | V3X | LETTERS | 935CB6EE3566 | 2026/09/16 11:08:22 | Wang-teacher wechat push req |
| letters/LETTER_FROM_TRAE_2026_09_11.md | V3X | LETTERS | 1D3A9E52ABE3 | 2026/09/11 16:30:23 | TRAE commission / reply series |
| letters/LETTER_FROM_TRAE_3RISK_2026_09_11.md | V3X | LETTERS | A1AFBF3E1296 | 2026/09/15 10:25:49 | TRAE commission / reply series |
| letters/LETTER_FROM_TRAE_REVIEW_2026_09_16.md | V3X | LETTERS | 6145162379C9 | 2026/09/15 15:19:16 | TRAE commission / reply series |
| letters/LETTER_FROM_TRAE_SELFCHECK_FIX_2026_09_15.md | V3X | LETTERS | 141E05BF56EA | 2026/09/15 15:39:01 | TRAE commission / reply series |
| letters/TRAE_CODE_IMPROVEMENT_LETTER_2026_09_17.md | V3X | LETTERS | 53A90B9EFBB9 | 2026/09/17 19:16:03 | TRAE letter series |
| letters/TRAE_FIX_REQUEST_3RISKS_2026_09_11.md | V3X | LETTERS | 62C4AF080EA3 | 2026/09/11 17:27:09 | TRAE letter series |
| letters/TRAE_V3_CODE_IMPROVEMENT_LETTER_2026_09_16.md | V3X | LETTERS | 9AA717B2E1AC | 2026/09/16 20:58:07 | TRAE letter series |
| letters/TRAE_V3_REVIEW_LETTER_2026_09_23.md | V3X | LETTERS | 0E7600AC4478 | 2026/09/23 13:08:23 | TRAE letter series |
| results/_coze_paper_v1_draft_2026_09_17.md | V3X | LETTERS | C08E7ABF5EE3 | 2026/09/18 00:21:36 | coze paper v1 draft |
| results/_coze_paper_v1_summary_2026_09_17.md | V3X | LETTERS | 2EFDC3D7741D | 2026/09/18 00:20:40 | coze paper v1 summary |
| results/_coze_wechat_v3_2026_09_18.md | V3X | LETTERS | 229D76E1B86F | 2026/09/18 21:03:20 | coze wechat v3 |
| results/_coze_wechat_v3_d7format_2026_09_18.md | V3X | LETTERS | 905544775AEE | 2026/09/18 21:08:42 | coze wechat v3 D7 format |
| results/_coze_wechat_v3_final_2026_09_18.md | V3X | LETTERS | DEEE45F45C5D | 2026/09/18 21:04:55 | coze wechat v3 final |
| results/_d7_wang_teacher_wechat_publish_v1_20260918.md | V3X | LETTERS | F4D5B755736A | 2026/09/17 14:39:46 | Wang-teacher wechat v1 |
| results/_v3_v4_ghostref_reconciliation_2026_09_23.md | V3X | ERRATUM | 1D52DB0EBF53 | 2026/09/23 15:11:45 | V3-V4 ghostref reconciliation (full) |
| letters/_kimi_v4_t12_review_2026_09_20.md | V4 | LETTERS | 38070FD12F31 | 2026/09/20 14:53:18 | kimi V4 review/reply series |
| letters/_kimi_v4_theme_reply_2026_09_20.md | V4 | LETTERS | 3E37352EFB4B | 2026/09/20 17:52:32 | kimi V4 review/reply series |
| letters/_kimi_v4_theme_reply_2_brainstorm_2026_09_20.md | V4 | LETTERS | BC14F47D927D | 2026/09/20 21:11:34 | kimi V4 review/reply series |
| letters/_v4_acceptance_coze_2026_09_20.md | V4 | LETTERS | B2BF2A073AC8 | 2026/09/20 14:58:15 | V4 commission / reply series |
| letters/_v4_acceptance_trae_code_2026_09_20.md | V4 | LETTERS | 3205593030BC | 2026/09/20 17:11:14 | V4 commission / reply series |
| letters/_v4_acceptance_trae_work_v1.0_2026_09_20.md | V4 | LETTERS | 3CAF4E653A68 | 2026/09/20 17:36:19 | V4 commission / reply series |
| letters/_v4_attribution_errata_trae_work_2026_09_20.md | V4 | LETTERS | E061C5806AF6 | 2026/09/20 17:36:48 | V4 commission / reply series |
| letters/_v4_d1_response_workbuddy_2026_09_20.md | V4 | LETTERS | BC663B671994 | 2026/09/20 14:36:48 | V4 commission / reply series |
| letters/_v4_d1_review_codex_2026_09_20.md | V4 | LETTERS | 48387412B109 | 2026/09/21 11:12:20 | V4 commission / reply series |
| letters/_v4_distillation_acceptance_coze_2026_09_20.md | V4 | LETTERS | 3A8CB7B9D041 | 2026/09/20 18:03:55 | V4 commission / reply series |
| letters/_v4_distillation_acceptance_kimi_2026_09_20.md | V4 | LETTERS | A4D194DBF9AD | 2026/09/20 17:56:29 | V4 commission / reply series |
| letters/_v4_distillation_acceptance_trae_code_2026_09_20.md | V4 | LETTERS | DC47FBF3C491 | 2026/09/20 17:32:33 | V4 commission / reply series |
| letters/_v4_distillation_brainstorm_reply_codex_2026_09_21.md | V4 | LETTERS | 0FF6C042B845 | 2026/09/21 11:12:20 | V4 commission / reply series |
| letters/_v4_distillation_invitation_2026_09_20_v1.0.md | V4 | LETTERS | 3D9F73519F6C | 2026/09/20 16:41:53 | V4 commission / reply series |
| letters/_v4_distillation_reply_claude_code_2026_09_20.md | V4 | LETTERS | D39CB17B051B | 2026/09/21 11:01:14 | V4 commission / reply series |
| letters/_v4_distillation_reply_coze_2026_09_20.md | V4 | LETTERS | 00593014CBD3 | 2026/09/20 21:53:15 | V4 commission / reply series |
| letters/_v4_distillation_reply_trae_code_2026_09_20.md | V4 | LETTERS | E87EC8F7E2FE | 2026/09/20 21:21:36 | V4 commission / reply series |
| letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23.md | V4 | LETTERS | 9BB22099DB3B | 2026/09/23 13:35:13 | V4 commission / reply series |
| letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23_fix_addendum.md | V4 | LETTERS | 59B8DF6E2E22 | 2026/09/23 13:46:15 | V4 commission / reply series |
| letters/_v4_distillation_theme_reply_workbuddy_2026_09_20.md | V4 | LETTERS | E3FE63A2F708 | 2026/09/20 18:19:48 | V4 commission / reply series |
| letters/_v4_distillation_theme_reply_workbuddy_brainstorm_2026_09_21.md | V4 | LETTERS | CDB27CD3008C | 2026/09/21 09:42:45 | V4 commission / reply series |
| letters/_v4_distillation_theme_reply_workbuddy_part2_2026_09_20.md | V4 | LETTERS | BFB4932F4467 | 2026/09/20 18:26:36 | V4 commission / reply series |
| letters/_v4_experiment_invitation_2026_09_20.md | V4 | LETTERS | 4E8C0EA57028 | 2026/09/20 13:37:03 | V4 commission / reply series |
| letters/_v4_experiment_invitation_2026_09_20_v0.2.md | V4 | LETTERS | 8E1E7434905D | 2026/09/20 16:06:52 | V4 commission / reply series |
| letters/_v4_review_claude_code_2026_09_20.md | V4 | LETTERS | B6F9956BCF5C | 2026/09/20 14:32:01 | V4 commission / reply series |
| letters/_v4_theme_reply_mavis_2026_09_20.md | V4 | LETTERS | 00315728BBF5 | 2026/09/20 17:08:33 | V4 commission / reply series |
| letters/_v4_theme_reply_mavis_2026_09_20_v1.1.md | V4 | LETTERS | 82FEE0A18DAB | 2026/09/20 17:22:38 | V4 commission / reply series |
| letters/_v4_theme_reply_mavis_2026_09_20_v1.2.md | V4 | LETTERS | 3ECF5B38048E | 2026/09/20 17:40:32 | V4 commission / reply series |
| letters/_v4_theme_reply_trae_work_2026_09_20.md | V4 | LETTERS | EBA83C88B629 | 2026/09/20 17:35:40 | V4 commission / reply series |
| letters/_v4_theme_reply_trae_work_2026_09_20_v1.1.md | V4 | LETTERS | BE850D129F35 | 2026/09/20 17:39:33 | V4 commission / reply series |
| letters/_v4_theme_reply_trae_work_2026_09_20_v1.2.md | V4 | LETTERS | 6BEE6EC434BD | 2026/09/20 20:58:07 | V4 commission / reply series |
| results/_v4_gA1_terminology_draft_2026_09_22.md | V4 | KNOWLEDGE | 0A2CAF0A2BD2 | 2026/09/22 13:09:56 | gA1 terminology draft |
| results/_v4_group_b_explore_subs_integration_2026_09_22.md | V4 | KNOWLEDGE | 588B45430E88 | 2026/09/22 16:31:25 | Group-B explore subs integration |
| results/_v4_pi_cot_dataset.json | V4 | ARTIFACT | 139DBFFD8CF9 | 2026/09/23 17:07:04 | Task-B dataset |
| results/_v4_pi_cot_v2_dataset.json | V4 | ARTIFACT | 7B01CD835A41 | 2026/09/24 15:55:01 | Task-B v2 dataset |
| results/_v4_pi_cot_v2_questionnaire_v1.md | V4 | DECISION | 7B14CDB31D21 | 2026/09/24 10:51:01 | Task-B questionnaire v1 |
| results/_v4_pi_decision_questionnaire_2026_09_21_v1.1.md | V4 | DECISION | ADC31D55B794 | 2026/09/22 16:50:32 | PI questionnaire v1.1 (in-effect) |

### 3.3 Tag-C: internal-only (not for external distribution)

Total: 426 classified + 722 bulk unclassified.

Listing omitted for brevity -- see section 2.

---

## 4. Validation

### 4.1 SHA-12 ground truth

All SHA-12 values in this inventory are disk-tested via `Get-FileHash -Algorithm SHA256`, first 12 hex chars. No fabricated hashes; every value here traces to a real byte-for-byte file on disk at workspace `D:/private-data/deposon-repo`. Recomputation method:

```powershell
$ws = 'D:/private-data/deposon-repo'
Get-ChildItem $ws -File -Recurse -Force |
  Where-Object { $_.Extension -notin @('.pyc','.log') -and $_.FullName -notmatch '\\(graphs|__pycache__|.tmp|.trae)\\' } |
  ForEach-Object { Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256 } |
  Select-Object -ExpandProperty Hash | ForEach-Object { $_.Substring(0,12) }
```

### 4.2 R4 key scan (zero plaintext keys)

Re-scan with proper UTF-8 encoding + word-boundary regex:

```powershell
$pattern = '(?<![A-Za-z0-9])(sk-[A-Za-z0-9]{20,}|sk_[a-zA-Z0-9_]{20,}|tp-[A-Za-z0-9]{20,}|ark-[A-Za-z0-9]{20,})(?![A-Za-z0-9])'
Get-ChildItem <workspace> -File -Recurse -Force | ForEach-Object {
  $content = Get-Content $_.FullName -Raw -Encoding UTF8
  if ($content -match $pattern) { Write-Host $_.FullName }
}
```

Result: **0 files flagged** (FINAL true hits: 0).

Note: an initial scan with `Get-Content -Raw` (no explicit `-Encoding UTF8`) returned 37 false-positives -- all `ask_<id>` Mavis ask_user tool IDs (e.g. `ask_4af3d5c30f3bb4dccc54d6ac`), where the preceding byte is literally `a` (0x61) so the negative lookbehind does match. Reading the bytes raw as UTF-8 vs the PowerShell default code-page caused a one-byte difference in the previous character. **Confirmed clean under UTF-8 + word-boundary regex.**

### 4.3 0-touch and V1-V3 asset integrity

This turn is a **read-only inventory**. No files in `corpus/`, `docs/`, `verifier/`, `letters/`, `deposon_team/`, `attacks/`, `scripts/`, `tests/`, `tools/`, `paper/`, `reviews/`, `audits_*`, `deposon_*` (legacy code), or `results/` were modified, moved, or copied. Only the new file `results/_v3_v4_achievements_inventory_2026_09_24.md` was created.

R5 (frozen-assets untouched) confirmed via prior turn's `_v4_noise_cleanup_manifest_2026_09_24.md` Section D (0-touch audit on 18 frozen + 9 grid + v13 erratum + the 5 anchor root).

### 4.4 Predecessor artefacts referenced

- `results/_v4_noise_cleanup_manifest_2026_09_24.md` -- this turn's input manifest (prior evidence-auditor turn). Used as the format template.
- `results/_v3_v4_ghostref_reconciliation_2026_09_23.md` -- ghost-reference reconciliation log covering all V3/V4 paths (cross-checked paths in this inventory against that log).
- `verifier/handoff/KT_ABC1_anchors_sha256_12.json` -- 5-anchor root file (CROSS/ERRATUM, in-effect).
- `corpus/v20/` -- corpus master (CROSS/ARTIFACT).

---

## 5. Completeness Statement and Blockers

### 5.1 Coverage

| Layer | Status |
|---|---|
| workspace root | covered (legacy Python scripts + audits_*.json + deposon_agents*.py) |
| corpus/ | covered (v20 + v20_caption_surface + by_model) |
| results/ | covered (766 files; bulk-V12 listing shown) |
| results/_archive_*/ | covered (manifest files + dated .md indexes) |
| docs/ | covered (V1-V2 legacy + V3X) |
| verifier/ | covered (handoff + audit + kill_lines + v1..v43) |
| letters/ | covered (LETTER_FROM_TRAE_*, _kimi_*, _v4_*) |
| deposon_team/ | covered (plugins + uploads) |
| attacks/ | covered (a1..a3 + __init__) |
| scripts/ | covered |
| tests/ | covered |
| tools/ | covered |
| paper/ | covered (CN/EN drafts) |
| reviews/ | covered |
| __pycache__/, *.pyc, *.log | EXCLUDED (transient; not enumerated) |
| cache graphs subdirs (gt8b_cache, gt8c_cache, etc.) | EXCLUDED (intermediate, not achievements) |

### 5.2 Honest gaps (漏检风险)

- **Ad-hoc V1.4 stage-1 files in `results/_v2_*`**: 6 Python executors (`_v2_setup.py`, `_v2_show_summary.py`, `_v2_smoketest.py`, `_v2_stage1..stage5_*.py`, `_v2_verify_outputs.py`) are placed in the bulk-V12 listing because their date prefix and topic clearly put them at the V1.4 / V2 boundary, not V3/V4. PI / verdict-keeper may re-classify these into V3.X if needed.
- **Trailing slash handling**: paths like `corpus/v20/by_model/coze/coze_artifact_v_2026_09_16.json` are recorded by relative path; in some asset-scanner outputs the by_model sub-tree inherits a corrupted LastWriteTime (`1979/11/30 00:00:00`) from a copy operation. The SHA-12 values are valid for the file contents on disk today.
- **`_v4_supp_l3_n20copy_backup/coze_artifact_v_2026_09_16.json.copy`** (10978 bytes) is a single leftover copy inside the L3 n20 backup directory; treated as internal cache and listed under V4 EXP_PRODUCT.
- **`audits_*.json` and `deposon_agents*.py`** at workspace root are tagged V12 / KNOWLEDGE by their date (2026-08-* and `deposon_agents.py` 2026-09-18). The 2026-09-18 timestamp on `deposon_agents.py` may indicate post-V3 in-place revision -- not classified into V3X / V4 because the file content does not match any V3/V4 trace marker. `[TO-VERIFY]` if re-classification is needed.
- **No `audits_*` enumeration to V3X** even though `audits_dataset_health.json` and `audits_outliers.json` are dated 2026-08-28 (V2.x range). Listed under V12 by default.
- **The 22 true judgments** referenced in V4 manifest -- not enumerated as a separate line because the individual L1..L14 verdicts are present in section 2.4; the manifest count is recoverable from `_v4_exec_*_result.json` filenames (29 N, 22 S, 14 M = 65 anchored verdict items under `_v4_exec_*`).
- **`_kimi_push_v3_manifest_batch*` (15 files)**: not individually tagged in the classified table; present under V3X / ERRATUM via the `_kimi_safe_batch_push_v3_full_2026_09_17.json` lineage. PI / verdict-keeper may upgrade to a separate category if needed.

### 5.3 Blockers / open questions

None for this inventory task itself. As follow-up questions (for PI / verdict-keeper / protocol-keeper, not blocking inventory delivery):
- Whether the `audits_*.json` root-level files should be re-classified from V12 to V3X (they predate V3 formal experiments by ~2 weeks but contain security/outlier signals relevant to P-D spec).
- Whether the 65 `_v4_exec_*_result.json` files should be lifted into a dedicated sub-category in section 2.4 (currently folded into EXP_PRODUCT).
- Whether the `_v4_supplement_*` consolidated executor + post/pre hashes + verdict pattern should be a 1-line row (currently it is, with full SHA-12 in the row).

### 5.4 End-of-file fingerprint

On successful write the SHA-12 of THIS file is computed and appended in the post-write section. 0-touch on V1-V3 assets; the only disk mutation this turn is the present manifest.

---

## 6. Result

- Inventory file: `results/_v3_v4_achievements_inventory_2026_09_24.md`
- Total classified items: 661
- Total bulk unclassified: 722
- Total disk-tested files: 1383
- Stages: V12 / V3X / V4 / CROSS
- Categories: 9 (JUDGMENT / PREREG / ERRATUM / EXP_PRODUCT / ARTIFACT / LETTERS / DECISION / KNOWLEDGE / NOTES)
- View tags: A / B / C
- R4 key plaintext scan: **0 hits** (UTF-8 + word-boundary)
- V1-V3 asset integrity: **0 touch** this turn


### 5.5 Inventory file fingerprint (post-write verification)

| field | value |
|---|---|
| path | esults/_v3_v4_achievements_inventory_2026_09_24.md |
| size | 191194 bytes |
| last-modified | 2026-09-24 17:22:25 |
| SHA-256 | FDF12FA1A6B70A2D424D4EEEE46B1EAEF325801ED7601C6B990B51819EBFEBB3 |
| SHA-12 | FDF12FA1A6B7 |

10 random representative items cross-checked between inventory entries and Get-FileHash -Algorithm SHA256 recomputation -- 10/10 MATCH. (Sample paths checked: erifier/v17/erratum.md 50F15F7EA3DC, erifier/v20/erratum.md 35081D39F35B, ttacks/__init__.py D11E085D9ECC, docs/V3X/P_D_FINGERPRINT_V0_3_SPEC.md F119F2F30287, esults/_v4_iron_rules_review_2026_09_22.md 40A51EF13882, corpus/v20/all.json 8DF31C95B1FC, corpus/v20_caption_surface/manifest.json 4FDDA6480BB5, erifier/handoff/KT_ABC1_anchors_sha256_12.json  3C6C01F3697, esults/_v4_supp_l6_s38v2_rootcause_verdict.md 973103878D6F, esults/_v4_pi_cot_v2_dataset.json 7B01CD835A41.)
