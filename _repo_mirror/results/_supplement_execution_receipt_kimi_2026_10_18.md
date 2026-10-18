# 补函（v0.4-SCDU）执行回执 ｜ 删除 293 ＋ 覆盖 10 ＋ 组B 0 覆盖 ｜ KIMI ｜ 2026-10-18

- 委托源件：`letters/_supplement_consolidated_desensitized_upload_2026_10_18.md`（补函 · 合卷为一 · PI 核准「脱敏方案核准，面④-3 可删，面②/面③启动」「补传与删除一批」）
- 覆盖面授权：卡 `ask_2b400459ab7333ac4c06f9bd` Q1 `opt2`（2026-10-18 12:15:44.013 UTC+8）——组A 9 件单件覆盖 ＋ `#16` 直覆；组B 6 件（#8 #9 #10 #11 #13 #14）维持 0 覆盖
- 执行棒：KIMI（上传执行）｜执行日：2026-10-18｜全部 ref 更新 fast-forward、逐件独立 commit、0 force

## 0 执行总览与 HEAD 链

| 时点 | HEAD | 事件 |
|---|---|---|
| 序 0 基线 | `7a5093f939b5e69d9b50e94a94cb2a7d74691bf8` | live HEAD 复测 0 漂移（与上轮终态同） |
| 删除面毕 | `3af4695f09d7bbfc8a1cc5250cf17ac6348291a2` | 293 件逐件独立 commit 删除毕 |
| 覆盖面毕（本轮终态） | `bd89e1ffffe06afa172d746c1a27b3faa456ff70` | 10 件逐件独立 commit 覆盖毕 |

**结果**：删除 293/293（failed=0）✅ ｜ 删后总验 298 路径 0 命中 ✅ ｜ S3 面 25 条 0 在位 ✅ ｜ 碰撞 16 件删间 0 漂移 ✅ ｜ 覆盖 10/10（覆后内容逐字节＝本地）✅ ｜ 组B 6 件 0 覆盖确认 ✅

**如实交代（commit message 两式并存）**：删除 commit message 之 `path=` 段，第 1–36 件（执行序）为**远端全路径式**（`path=_september_workspace/<rel>`），第 37–293 件起为**仓内路径式**（`path=<rel>`）——系本棒对 PI「路径改仓内路径」之初读为 message 格式面并即改；其后 PI 澄清「我是说#16」指 `tools/exp_harness.py` 文件实体之 L108/L109。commit message 不可回改，**两式并录、如实登记**，0 折腾回退。抽查实证：第 1 件 `path=_september_workspace/.tmp/_aggregate_10cells.py`、第 36 件 `path=_september_workspace/.tmp/_docwriter_wt2_enum_final_2026_09_30.tsv`、第 37 件 `path=.tmp/_e3536.txt`、第 293 件 `path=docs/DATASET_HEALTH_v2.md`。覆盖面 10 件 message 自始为仓内路径式。

---

# 甲 ｜ 删除面回执（R-S1 ～ R-S6）

## R-S1 序 0 基线复核

- live HEAD ＝ `7a5093f939b5e69d9b50e94a94cb2a7d74691bf8`（`head_moved=False`，与上轮终态 `7a5093f9…` 同一）
- 全树 blobs 3,739（`truncated=False`）；293 留候路径 match=293／sha_diff=0／absent=0；碰撞 16 件 0 漂移
- `.gitignore` 复验：顶层 105 B ✅；`_september_workspace/.gitignore` 仍 91 B 旧版（KD-REV18-2 复验登记——**只报不改，处置归 PI**）

## R-S2 删前去重对账

- 照录补函三数：302 件次 ／ 298 路径 ／ 288 内容；本轮执行 293 件（余 5 件前轮已删，见 R-S4 注）
- 面计数（298 路径之 faces 分布）：`A1` 2 ｜ `A2` 1 ｜ `A3` 213 ｜ `A4` 3 ｜ `S3` 25 ｜ `S5` 58

## R-S3 「先拉回后删除」之前置成就（293/293，0 留候）

- **279 件**：本地区三源（repo／sub／归档区）既有副本之内容 SHA 与远端逐件相符——副本在手，删除无损
- **14 件**：本地无相符副本（weak 13 ＋ none 1，含 `docs/V3X/D3_ONLINE_MIDTERM_TEMPLATE.md`），**删前已逐件拉回**至归档区独立子目录（0 覆写），拉回核验 14/14 verified=True：

| # | 仓内路径 | bytes | 拉回落点 |
|--:|---|--:|---|
| 1 | `docs/V3X/D7_ONE_PAGE_SUMMARY_TEMPLATE.md` | 5,862 | `…\_remote_delete_face_pullback_2026_10_18_kimi_supplement14\docs\V3X\D7_ONE_PAGE_SUMMARY_TEMPLATE.md` |
| 2 | `results/_archive_2026_09_24/_v4_pi_decision_questionnaire_2026_09_21_v1.1.md.bak_2026_09_22_gB_post.md` | 113,424 | `…\_remote_delete_face_pullback_2026_10_18_kimi_supplement14\results\_archive_2026_09_24\_v4_pi_decision_questionnaire_2026_09_21_v1.1.md.bak_2026_09_22_gB_post.md` |
| 3 | `results/_g10_threshold_closed_domain_judgment_2026_10_11.md` | 55,667 | `…\_remote_delete_face_pullback_2026_10_18_kimi_supplement14\results\_g10_threshold_closed_domain_judgment_2026_10_11.md` |
| 4 | `results/_ghostref_copy_log_2026_09_23.json` | 120,810 | `…\_remote_delete_face_pullback_2026_10_18_kimi_supplement14\results\_ghostref_copy_log_2026_09_23.json` |
| 5 | `results/_glm_response_v2_template_2026_09_18.md` | 44,133 | `…\_remote_delete_face_pullback_2026_10_18_kimi_supplement14\results\_glm_response_v2_template_2026_09_18.md` |
| 6 | `results/_round56_idx_sc1_temp_deletion_deviation_note_2026_10_10.md` | 8,143 | `…\_remote_delete_face_pullback_2026_10_18_kimi_supplement14\results\_round56_idx_sc1_temp_deletion_deviation_note_2026_10_10.md` |
| 7 | `results/_stage3_1_register_fingerprint_placeholder_erratum_2026_10_12.md` | 4,475 | `…\_remote_delete_face_pullback_2026_10_18_kimi_supplement14\results\_stage3_1_register_fingerprint_placeholder_erratum_2026_10_12.md` |
| 8 | `results/_t1_qwen_temp_sweep_executor_2026_10_09.py` | 32,393 | `…\_remote_delete_face_pullback_2026_10_18_kimi_supplement14\results\_t1_qwen_temp_sweep_executor_2026_10_09.py` |
| 9 | `results/_t1_qwen_temp_sweep_r2_exec_register_2026_10_09.md` | 23,683 | `…\_remote_delete_face_pullback_2026_10_18_kimi_supplement14\results\_t1_qwen_temp_sweep_r2_exec_register_2026_10_09.md` |
| 10 | `results/_t1_qwen_temp_sweep_r2_executor_2026_10_09.py` | 53,180 | `…\_remote_delete_face_pullback_2026_10_18_kimi_supplement14\results\_t1_qwen_temp_sweep_r2_executor_2026_10_09.py` |
| 11 | `results/_t1_qwen_temp_sweep_r2_result_2026_10_09.json` | 58,665 | `…\_remote_delete_face_pullback_2026_10_18_kimi_supplement14\results\_t1_qwen_temp_sweep_r2_result_2026_10_09.json` |
| 12 | `results/_t1_qwen_temp_sweep_verdict_2026_10_09.md` | 21,652 | `…\_remote_delete_face_pullback_2026_10_18_kimi_supplement14\results\_t1_qwen_temp_sweep_verdict_2026_10_09.md` |
| 13 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v4_tmp_cleanup_2026_09_28.md` | 5,122 | `…\_remote_delete_face_pullback_2026_10_18_kimi_supplement14\tmp_movedout_2026_10_09\uncertain_release_2026_09\_v4_tmp_cleanup_2026_09_28.md` |
| 14 | `docs/V3X/D3_ONLINE_MIDTERM_TEMPLATE.md` | 4,397 | `…\_remote_delete_face_pullback_2026_10_18_kimi_supplement14\docs\V3X\D3_ONLINE_MIDTERM_TEMPLATE.md` |

落点根：`〔本地归档区〕\_remote_delete_face_pullback_2026_10_18_kimi_supplement14\`（独立子目录 · 0 覆写既有归档）

## R-S4 逐件删除证据（293 件全表）

删后总验：live HEAD `3af4695f09d7bbfc8a1cc5250cf17ac6348291a2` 全树重取（blobs 3,446 · truncated=False），298 路径（本轮 293 ＋ 前轮 5）**0 命中**。前轮已删 5 件：`results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json`、`results/_archive_2026_09_20/gpt6_30cells_run.log.err`、`results/_archive_2026_09_20/volcengine_glm_latest_30cells_v2_run_2026_09_10.log.err`、`results/_v4_supp_l14v3_batch2_r2_models_probe.err.log`、`results/_d05_sanity_3backbone_20260918_100110.json`

| # | 仓内路径（远端＝`_september_workspace/<rel>`；根级件径同） | faces | 删前 blob SHA-12 | bytes | commit-12 |
|--:|---|---:|---|--:|---|
| 1 | `.tmp/_aggregate_10cells.py` | A3 | `e1a1631d04c5` | 3,009 | `3aacc03484d9` |
| 2 | `.tmp/_aggregate_10cells_v2.py` | A3 | `dde3583101e5` | 5,131 | `6646c592fb32` |
| 3 | `.tmp/_aggregate_10cells_v3.py` | A3 | `b747e865f962` | 2,969 | `6c6ceb50bec7` |
| 4 | `.tmp/_aggregate_10cells_v4.py` | A3 | `509f3fdba386` | 2,454 | `1c38afe2f3c4` |
| 5 | `.tmp/_audit3b.txt` | A3 | `e992573fbe2f` | 50,554 | `bcd7e73a57a3` |
| 6 | `.tmp/_audit_part3_out.txt` | A3 | `0c62f640ffcf` | 5,195 | `daf2e2760fca` |
| 7 | `.tmp/_audit_part4.txt` | A3 | `43a8ce00dc25` | 14,826 | `7518e88cec4a` |
| 8 | `.tmp/_b12_q1_refs_2026_09_29.py` | A3 | `7cefb4ba8dc3` | 4,890 | `c7deb6f758fa` |
| 9 | `.tmp/_b12_q1_timeslice_2026_09_29.py` | A3 | `72b68a58571a` | 798 | `4da6b0e7308f` |
| 10 | `.tmp/_b12_q4_adjacent_2026_09_29.py` | A3 | `5acda04b5429` | 5,709 | `ec3bf2f14e34` |
| 11 | `.tmp/_b12_q4_anchor_probe_2026_09_29.py` | A3 | `e639d79f3a82` | 4,142 | `a1afbeefb6b5` |
| 12 | `.tmp/_b12_q4_exact_2026_09_29.py` | A3 | `7fc5c5a60075` | 7,140 | `796299ccadb5` |
| 13 | `.tmp/_b12_q4_formcand_2026_09_29.py` | A3 | `a165000be31f` | 6,510 | `98103909553a` |
| 14 | `.tmp/_b12_tables_2026_09_29.py` | A3 | `69494189752d` | 1,907 | `179854e9e2c9` |
| 15 | `.tmp/_c5_b_prestate_baseline.json` | A3 | `ca0b3b81b7ce` | 1,543 | `8927f7e3a1a5` |
| 16 | `.tmp/_c5_feasibility_probe.py` | A3 | `309a3f0e7a09` | 1,036 | `0544ac64d703` |
| 17 | `.tmp/_check_kimi_sides.py` | A3 | `eabc35e9087a` | 1,459 | `817567721c41` |
| 18 | `.tmp/_compute_metrics.py` | A3 | `17da548d7319` | 7,752 | `877aa9c2a981` |
| 19 | `.tmp/_compute_metrics_v2.py` | A3 | `b6e931642af4` | 8,017 | `20288ce8af1a` |
| 20 | `.tmp/_cpatomic_dump_pyc_2026_09_28.py` | A3 | `f48a7b3ee422` | 468 | `f87fe1856e88` |
| 21 | `.tmp/_cpatomic_keyscan_2026_09_28.json` | A3 | `ddb27880cb79` | 2,672 | `6148a4d56b6c` |
| 22 | `.tmp/_cpatomic_keyscan_2026_09_28.py` | A3 | `bb4a13c7a700` | 3,074 | `131ce78626a5` |
| 23 | `.tmp/_cpatomic_make_fix_2026_09_28.py` | A3 | `9314fdf5ebd7` | 7,796 | `70b09e3bf2f3` |
| 24 | `.tmp/_cpatomic_patch_manifest_2026_09_28.json` | A3 | `79d2d3cf9c12` | 357 | `e7a937b555f1` |
| 25 | `.tmp/_cpatomic_pycache_post_2026_09_28.json` | A3 | `66a057896f09` | 6,476 | `29c5792a72ba` |
| 26 | `.tmp/_cpatomic_pycache_post_2026_09_28.py` | A3 | `16d2e4b20bc1` | 5,164 | `7ecaae9d458b` |
| 27 | `.tmp/_cpatomic_pycache_pre_2026_09_28.json` | A3 | `6dd00db4ba4f` | 10,772 | `7d0acd6440cb` |
| 28 | `.tmp/_cpatomic_pycache_pre_2026_09_28.py` | A3 | `0bd4d69d5ed5` | 3,912 | `6ff6c9d507bd` |
| 29 | `.tmp/_cpatomic_register_2026_09_28.json` | A3 | `13b028f782d7` | 29,361 | `98a3540e4dce` |
| 30 | `.tmp/_cpatomic_register_2026_09_28.py` | A3 | `b7b15766e9b1` | 6,322 | `1b50b08530fa` |
| 31 | `.tmp/_cpatomic_verify_2026_09_28.json` | A3 | `0b0a6883ab57` | 3,144 | `ebdf7a3a7962` |
| 32 | `.tmp/_cpatomic_verify_2026_09_28.py` | A3 | `5437c6a9d6c1` | 11,036 | `4bc833353076` |
| 33 | `.tmp/_d4_relabel_run1.log` | A3 | `974578688ea3` | 1,158 | `e1376132083a` |
| 34 | `.tmp/_diff21_anchor_drift.py` | A3 | `cc97495dfb46` | 960 | `6213984422b8` |
| 35 | `.tmp/_diff21_anchor_drift.txt` | A3 | `d55669326b31` | 20,994 | `ea95cd870ddd` |
| 36 | `.tmp/_docwriter_wt2_enum_final_2026_09_30.tsv` | A3 | `57f620eaca69` | 66,339 | `1ff19afefb5b` |
| 37 | `.tmp/_e3536.txt` | A3 | `1d0ed76deb8b` | 2,248 | `270d620036a1` |
| 38 | `.tmp/_e47_docwriter_count.py` | A3 | `9ab3cf67a432` | 1,124 | `950f93d0a9d4` |
| 39 | `.tmp/_e48_apply.py` | A3 | `841b83636d65` | 2,329 | `c71a2831383f` |
| 40 | `.tmp/_e48_c1.md` | A3 | `5f8667592152` | 5,039 | `484c6f925f23` |
| 41 | `.tmp/_e48_c2.md` | A3 | `7af140c886b7` | 5,966 | `37869b65d809` |
| 42 | `.tmp/_e48_c3.md` | A3 | `83706e76a67c` | 6,563 | `aa88e4d58193` |
| 43 | `.tmp/_e48_c4.md` | A3 | `8aa72c80bbf8` | 21,710 | `315a0850cdb8` |
| 44 | `.tmp/_e48_c5.md` | A3 | `86c14d68154c` | 1,686 | `6fc7d3931044` |
| 45 | `.tmp/_e48_docwriter_chain.py` | A3 | `20d929b85e09` | 2,550 | `255fa4040c80` |
| 46 | `.tmp/_e48_docwriter_enum.py` | A3 | `6c28a787fc97` | 1,248 | `72daf6223808` |
| 47 | `.tmp/_e48_docwriter_hash.py` | A3 | `e0601c6df74f` | 2,578 | `322ea30656b1` |
| 48 | `.tmp/_e48_docwriter_hash2.py` | A3 | `8d094945fb22` | 1,229 | `8ea5f8afae25` |
| 49 | `.tmp/_e48_probe_register.py` | A3 | `fcc75970daa1` | 873 | `e310d0f34d42` |
| 50 | `.tmp/_e49_c1.md` | A3 | `457b83c42f3d` | 13,607 | `5eb70737191d` |
| 51 | `.tmp/_e49_c2.md` | A3 | `4a124466a1da` | 17,872 | `cf06b5f54185` |
| 52 | `.tmp/_e50_c1.md` | A3 | `f94990aef3b4` | 16,236 | `8dbae21d4eae` |
| 53 | `.tmp/_e50_c2.md` | A3 | `ce129294776f` | 17,220 | `d5c8e33ac072` |
| 54 | `.tmp/_en_final_2026_09_28.py` | A3 | `79b6566290c2` | 2,369 | `f91db5974eb8` |
| 55 | `.tmp/_en_verify2_2026_09_28.py` | A3 | `5ab36dc862a5` | 1,870 | `b1fde3fa431d` |
| 56 | `.tmp/_en_verify3_2026_09_28.py` | A3 | `1b5fd9ed2a51` | 1,638 | `2a3fe852c97c` |
| 57 | `.tmp/_en_verify4_2026_09_28.py` | A3 | `abf4a09b897d` | 1,484 | `2d8997a9ec6b` |
| 58 | `.tmp/_en_verify_2026_09_28.py` | A3 | `0191bd6e8c2d` | 6,071 | `a6215972fef2` |
| 59 | `.tmp/_execswitch_verify_2026_09_28.py` | A3 | `584015ddcd11` | 3,501 | `590d63384772` |
| 60 | `.tmp/_final_check.py` | A3 | `ca85aea58147` | 1,562 | `0a00688ac31c` |
| 61 | `.tmp/_final_sha.py` | A3 | `859ce3ca4928` | 1,435 | `ef853f764395` |
| 62 | `.tmp/_final_sha.txt` | A3 | `19615837a94f` | 611 | `77444321727b` |
| 63 | `.tmp/_gaps.txt` | A3 | `4af923ea421a` | 435 | `8b2d242b0c83` |
| 64 | `.tmp/_gaps2.txt` | A3 | `57855e19a280` | 2,377 | `cee46a86017f` |
| 65 | `.tmp/_hash21.py` | A3 | `e5ec28d56b04` | 944 | `bfb374fb8ea9` |
| 66 | `.tmp/_inspect_10cells.py` | A3 | `3fade1e7f765` | 2,460 | `7baffdc2aa9a` |
| 67 | `.tmp/_inspect_batch4_rounds.py` | A3 | `e24baeebd832` | 898 | `d8b9c38f1d10` |
| 68 | `.tmp/_l14v3_aggregated_10cells.json` | A3 | `74e9b4667bad` | 634,458 | `44afda519df3` |
| 69 | `.tmp/_l14v3_aggregated_10cells_v2.json` | A3 | `b412df2c3d70` | 243 | `00a35fc5ec33` |
| 70 | `.tmp/_l14v3_aggregated_10cells_v3.json` | A3 | `b412df2c3d70` | 243 | `e39dc3460018` |
| 71 | `.tmp/_l14v3_aggregated_10cells_v4.json` | A3 | `c254c3e3d5fd` | 2,233,138 | `a97a0db22a62` |
| 72 | `.tmp/_l14v3_n26_metrics.json` | A3 | `8e3b4ad1ffc6` | 1,445 | `d5056090efa0` |
| 73 | `.tmp/_l14v3_n26_metrics_v2.json` | A3 | `faf22d4872ad` | 2,579 | `28dfe052933b` |
| 74 | `.tmp/_l14v3_sensitivity_v2.json` | A3 | `daac269ece6a` | 2,292 | `5a54e8f799f6` |
| 75 | `.tmp/_n1_n2_check.py` | A3 | `446456760fe3` | 1,628 | `9d0c56ec1982` |
| 76 | `.tmp/_patch21_emit.py` | A3 | `7e05748bc4b0` | 17,106 | `e3f816702596` |
| 77 | `.tmp/_patch21_make.py` | A3 | `47a9c9fad721` | 8,807 | `c5d2de462a02` |
| 78 | `.tmp/_patch21_run.py` | A3 | `7aad941f9485` | 3,866 | `0db7be0fe547` |
| 79 | `.tmp/_pc.py` | A3 | `b339f37d1993` | 431 | `86d3dd7ef7a7` |
| 80 | `.tmp/_pk_probe.py` | A3 | `5764d36c72c6` | 398 | `cbd42e694fb8` |
| 81 | `.tmp/_pk_probe2.py` | A3 | `014d8db934ca` | 352 | `524f0db7abe4` |
| 82 | `.tmp/_pk_probe3.py` | A3 | `bbb51498524e` | 462 | `7399b9ff21cb` |
| 83 | `.tmp/_pk_probe4.py` | A3 | `bb056f3ef908` | 176 | `d0a54d8a9c6a` |
| 84 | `.tmp/_pk_probe5.py` | A3 | `2a0884a182a6` | 338 | `6624e44049b8` |
| 85 | `.tmp/_pk_probe6.py` | A3 | `5d4f6dc5cb43` | 257 | `35011de1d928` |
| 86 | `.tmp/_pk_probe7.py` | A3 | `fa9fb4874ad6` | 1,636 | `11380f9df5bd` |
| 87 | `.tmp/_pk_probe8.py` | A3 | `905953d35f0a` | 1,636 | `3fa2aac04729` |
| 88 | `.tmp/_pk_sha_scan.py` | A3 | `e42d45d2d61f` | 599 | `e61654aef81f` |
| 89 | `.tmp/_pkf34_f3.py` | A3 | `910ca28c22fb` | 3,068 | `7a727d348e6e` |
| 90 | `.tmp/_pkf34_f34.py` | A3 | `020b1e1f8278` | 4,282 | `cabebb13a0f1` |
| 91 | `.tmp/_pkf34_f3b.py` | A3 | `96a1c1645b1b` | 2,703 | `f7ef3328ea71` |
| 92 | `.tmp/_pkf34_f4.py` | A3 | `c8eccce0733a` | 3,958 | `4b52d3a6d7fc` |
| 93 | `.tmp/_pkf34_f4b.py` | A3 | `f4636107380a` | 4,401 | `9268c01fa94a` |
| 94 | `.tmp/_pkf34_f4c.py` | A3 | `e5daeda4fdb7` | 3,045 | `2f9d6c9b7a38` |
| 95 | `.tmp/_pkf34_f4d.py` | A3 | `a423da2f3226` | 3,686 | `0c694079b862` |
| 96 | `.tmp/_pkf34_final.py` | A3 | `07046a502a45` | 5,903 | `b0059f7b5e99` |
| 97 | `.tmp/_pkf34_nd.py` | A3 | `90db18676749` | 2,537 | `9c80afbc37a3` |
| 98 | `.tmp/_pkf34_probe1.py` | A3 | `384056a5f1e8` | 633 | `0e20c8b1ec79` |
| 99 | `.tmp/_pkf34_probe2.py` | A3 | `2c9b2eb91b8d` | 604 | `eb06b6da03cf` |
| 100 | `.tmp/_pkf34_v12.py` | A3 | `276b959b5413` | 5,639 | `d51a459fa20a` |
| 101 | `.tmp/_postcheck_v16_alt.py` | A3 | `a4e0cf8c4298` | 1,282 | `52036f77995e` |
| 102 | `.tmp/_postcheck_v16_alt_stdout.txt` | A3 | `48de61d702ac` | 1,558 | `1d47720a4199` |
| 103 | `.tmp/_postcheck_v16_sha.py` | A3 | `a56d16f7b008` | 1,391 | `3053d2e576e5` |
| 104 | `.tmp/_precheck_v15_tail.ps1` | A3 | `745cfb35ed36` | 505 | `a4f76b6c74d7` |
| 105 | `.tmp/_probe21.py` | A3 | `58f4a31aefc2` | 564 | `8e641fad4002` |
| 106 | `.tmp/_probe21_fields.py` | A3 | `f2d18d779682` | 2,876 | `e241db6b7745` |
| 107 | `.tmp/_r10.py` | A3 | `e8192a81d3d5` | 1,525 | `983fb938611b` |
| 108 | `.tmp/_r10.txt` | A3 | `1a4da74b9f68` | 3,867 | `9c5d351481c3` |
| 109 | `.tmp/_r11_ctx.txt` | A3 | `79732c90c8a4` | 4,106 | `657123a04df6` |
| 110 | `.tmp/_r1_alarm_test.py` | A3 | `f84d0c6de951` | 2,297 | `8ff5e0105026` |
| 111 | `.tmp/_r1_scratch_bom.json` | A3+S5 | `ce2eb62d8e53` | 17 | `8f9938ae43a1` |
| 112 | `.tmp/_r1_scratch_corrupt_a.json` | A3+S5 | `98a98d1ad5fb` | 15 | `c5e94671cec8` |
| 113 | `.tmp/_r1_scratch_good.json` | A3+S5 | `6c61612aff4c` | 14 | `63b496d8f05a` |
| 114 | `.tmp/_r3_header_fix_2026_09_28.py` | A3 | `4b6afbfa9964` | 3,280 | `6d7bbdc81561` |
| 115 | `.tmp/_r3_verify_2026_09_28.py` | A3 | `9bff630d3493` | 5,494 | `8be469b05e5e` |
| 116 | `.tmp/_r4_cleanup_worker_keycount_2026_09_29.py` | A3 | `7d79c2edb86c` | 1,909 | `4045112e6166` |
| 117 | `.tmp/_r4_cleanup_worker_keyscan_2026_09_29.py` | A3 | `2ac93d8110c3` | 3,561 | `9a91af13661e` |
| 118 | `.tmp/_r4_cleanup_worker_keyscan_results_2026_09_29.json` | A3 | `ed90d28bb0bd` | 75 | `a2c11919b819` |
| 119 | `.tmp/_r4_cleanup_worker_nearmiss_2026_09_29.py` | A3 | `0e189cc246cf` | 1,382 | `7547676c4e4f` |
| 120 | `.tmp/_r4_cleanup_worker_scan_2026_09_29.py` | A3 | `22a7def760e3` | 2,411 | `530d054998a4` |
| 121 | `.tmp/_r4_cleanup_worker_shape_2026_09_29.py` | A3 | `a65632b4c30b` | 1,110 | `807a33de3fc3` |
| 122 | `.tmp/_r4_key_scan_2026_09_24.py` | A3 | `26b5b81a2534` | 3,743 | `f0e928beca38` |
| 123 | `.tmp/_r4_key_scan_r1_files_2026_09_27.json` | A3 | `439e68738f93` | 2,313 | `5e25e0431bfc` |
| 124 | `.tmp/_r4_key_scan_r1_files_2026_09_27.py` | A3 | `69e69cbc51f0` | 4,079 | `bc8d660dc37f` |
| 125 | `.tmp/_r4_key_scan_results_2026_09_24.json` | A3 | `898e7cb3f1fc` | 1,014 | `55d7f6a1e428` |
| 126 | `.tmp/_r6_evidence.py` | A3 | `239cad89b5c5` | 2,525 | `df592309cce7` |
| 127 | `.tmp/_r6_evidence.txt` | A3 | `d94143c77e96` | 30,834 | `9f85f6d057ab` |
| 128 | `.tmp/_recheck_r1_run1.log` | A3 | `9dd120c96a34` | 2,486 | `114c466124e3` |
| 129 | `.tmp/_recheck_r1_runA.log` | A3 | `eeb137ee0997` | 2,634 | `90824245f2e2` |
| 130 | `.tmp/_recheck_r1_runB.log` | A3 | `eeb137ee0997` | 2,634 | `79dd4b4a87e1` |
| 131 | `.tmp/_recheck_r1_runC.log` | A3 | `ddd32d5b8398` | 2,568 | `8fd37c8bedb6` |
| 132 | `.tmp/_recheck_r1_runD.log` | A3 | `ddd32d5b8398` | 2,568 | `7fc561351cb1` |
| 133 | `.tmp/_rj5_convention_check_2026_09_27.out.json` | A3 | `77ccf7e3f367` | 8,983 | `cad1f3e03642` |
| 134 | `.tmp/_rj5_convention_check_2026_09_27.py` | A3 | `11f90ecb2e98` | 8,018 | `c1e8170c962d` |
| 135 | `.tmp/_rj5_mapping_test_2026_09_27.out.txt` | A3 | `3a2decf0d8cf` | 1,384 | `0804046920d3` |
| 136 | `.tmp/_rj5_mapping_test_2026_09_27.py` | A3 | `24177ad1b147` | 5,968 | `c9bd76d9dc10` |
| 137 | `.tmp/_run2.py` | A3 | `4d3ddbee1789` | 4,366 | `8d87e4447ef3` |
| 138 | `.tmp/_run_d4_relabel_addendum.py` | A3 | `7b7382214f1a` | 17,550 | `fd13418f5b9e` |
| 139 | `.tmp/_run_d6_addendum_2026_09_28.py` | A3 | `fb299dc324fa` | 23,204 | `e212bce6f24c` |
| 140 | `.tmp/_run_d6b_addendum_2026_09_28.py` | A3 | `f6b98a7c4462` | 31,468 | `c2de9490d779` |
| 141 | `.tmp/_run_d8_addendum_2026_09_30.py` | A3 | `e158e353d448` | 107,959 | `ab909b47f848` |
| 142 | `.tmp/_run_d8_bhalf_addendum_2026_09_30.py` | A3 | `359b86c6902e` | 40,576 | `9c86c582c827` |
| 143 | `.tmp/_run_day_inventory_table_2026_09_27.py` | A3 | `338b864817b6` | 2,763 | `5475398bceb3` |
| 144 | `.tmp/_run_final.py` | A3 | `2113bef8bb10` | 26,654 | `d5dfe1f283bb` |
| 145 | `.tmp/_run_final_selfscan_2026_09_27.py` | A3 | `c25987bd31ff` | 1,358 | `184c47ba8d2a` |
| 146 | `.tmp/_run_frozen_0touch_verify_2026_09_27.py` | A3 | `76698ca84d3a` | 2,309 | `2315c626e486` |
| 147 | `.tmp/_run_output.log` | A3 | `5365182c8f1c` | 1,420 | `d9ee609f4101` |
| 148 | `.tmp/_run_recheck_r1.py` | A3 | `1b151e8de4f8` | 34,895 | `a5062a4d914e` |
| 149 | `.tmp/_run_result_v3.py` | A3 | `f716c0c35939` | 3,304 | `19501a3ce320` |
| 150 | `.tmp/_run_v3r1_relabel.py` | A3 | `7aaa1b5d521f` | 30,875 | `6a2c2cfd77bd` |
| 151 | `.tmp/_sensitivity.py` | A3 | `f106f9ba9f59` | 5,954 | `7587f5ac27e4` |
| 152 | `.tmp/_sha12_check.ps1` | A3 | `ff37c2fc6e2a` | 697 | `53ea9970d512` |
| 153 | `.tmp/_sha12_check2.ps1` | A3 | `2e7c6ec8f6aa` | 691 | `53656c42da28` |
| 154 | `.tmp/_t15_inspect.py` | A3 | `a8210b5b9676` | 2,728 | `fd9ddbe324c9` |
| 155 | `.tmp/_t15_inspect2.py` | A3 | `617e253d881a` | 1,942 | `8a9637d3d2a0` |
| 156 | `.tmp/_t15_inspect3.py` | A3 | `8d6241e65c3d` | 1,890 | `347c767a718f` |
| 157 | `.tmp/_t15_inspect3_out.txt` | A3 | `f8808795aad0` | 1,588 | `aa3b18afd7af` |
| 158 | `.tmp/_t15_inspect4.py` | A3 | `2402a61a60f2` | 2,756 | `1957e9387f72` |
| 159 | `.tmp/_t15_inspect4_out.txt` | A3 | `622ae907e666` | 3,057 | `6e9c7d9c5f46` |
| 160 | `.tmp/_t15_inspect5.py` | A3 | `42328dc97335` | 2,712 | `5ab230db4550` |
| 161 | `.tmp/_t15_inspect5_out.txt` | A3 | `06b00b56614a` | 933 | `08469d1fb3eb` |
| 162 | `.tmp/_t15_inspect6.py` | A3 | `471962695262` | 1,234 | `c0fa4f010a0e` |
| 163 | `.tmp/_t15_inspect6_out.txt` | A3 | `39267bbc3ea0` | 6,659 | `b93a17c64feb` |
| 164 | `.tmp/_t15_inspect7.py` | A3 | `30e47d32a770` | 3,880 | `e6bcc77790a9` |
| 165 | `.tmp/_t15_inspect7_out.txt` | A3 | `8979135365bd` | 3,647 | `b5d6139f573b` |
| 166 | `.tmp/_t15_percell.py` | A3 | `6affb9b13b25` | 596 | `640b62ce9b37` |
| 167 | `.tmp/_t15_percell.txt` | A3 | `50c3f87b8ca2` | 491 | `bc9eafb5bf77` |
| 168 | `.tmp/_t15_percell_out.txt` | A3 | `248e83a89852` | 772 | `186b4a6c71a5` |
| 169 | `.tmp/_t15_probe_log.json` | A3 | `dce3ac9f916d` | 718 | `c249f7a09f0a` |
| 170 | `.tmp/_t15_records.json` | A3 | `8f373879f400` | 96,443 | `12110bb61ab1` |
| 171 | `.tmp/_t15_update_result.py` | A3 | `01693e7d0247` | 9,226 | `c895409e968f` |
| 172 | `.tmp/_t15r2_checkpoint_warn.jsonl` | A3 | `dd348b05a666` | 914 | `3e5a8a7e7032` |
| 173 | `.tmp/_t15r2_inspect.py` | A3 | `40679de7627a` | 3,730 | `69e38722dbfb` |
| 174 | `.tmp/_t15r2_verify.py` | A3 | `0df51a7e4e63` | 6,737 | `28bbcff53e5d` |
| 175 | `.tmp/_tail3_atomic_landing_check_2026_09_29.py` | A3 | `5b1af280bf83` | 2,699 | `898a5beb2690` |
| 176 | `.tmp/_tail3_atomic_make_2026_09_29.json` | A3 | `2624d4f8f34f` | 19,595 | `0af710cf1eef` |
| 177 | `.tmp/_tail3_atomic_make_2026_09_29.py` | A3 | `3140b222ec01` | 17,272 | `f6908a189333` |
| 178 | `.tmp/_tail3_atomic_refs_2026_09_29.json` | A3 | `9dbe95f45ee0` | 5,784 | `2eb41ec8d3e2` |
| 179 | `.tmp/_tail3_atomic_refs_2026_09_29.py` | A3 | `65b5f8e82a58` | 2,636 | `704ff8780898` |
| 180 | `.tmp/_tail3_atomic_verify_2026_09_29.json` | A3 | `3faa1bc953fb` | 11,116 | `2fc73d644f55` |
| 181 | `.tmp/_tail3_atomic_verify_2026_09_29.py` | A3 | `df27b83f1dd2` | 21,338 | `4c7ff94163a0` |
| 182 | `.tmp/_tail_only.py` | A3 | `ed0122a7e3ac` | 436 | `53135702050b` |
| 183 | `.tmp/_trae_audit_part1.py` | A3 | `c768bc661623` | 5,510 | `9c61a9c338a2` |
| 184 | `.tmp/_trae_audit_part2.py` | A3 | `3b088784aca1` | 3,632 | `b9930af0dfa4` |
| 185 | `.tmp/_trae_audit_part3.py` | A3 | `6a409f23309c` | 8,617 | `d7108663b6f1` |
| 186 | `.tmp/_trae_audit_part3b.py` | A3 | `13511b18379a` | 7,662 | `0100a7f4c3f6` |
| 187 | `.tmp/_trae_audit_part4.py` | A3 | `7f2fba38c479` | 7,173 | `3e41a2c28b17` |
| 188 | `.tmp/_v16_full_decoded.txt` | A3 | `8afc120c47f0` | 174,424 | `f37bd42cd678` |
| 189 | `.tmp/_v16_tail_dump.txt` | A3 | `8afc120c47f0` | 174,424 | `45185158a8f0` |
| 190 | `.tmp/_v16_tail_only.txt` | A3 | `40a94d0d129f` | 3,471 | `cc6c30fe4503` |
| 191 | `.tmp/_v3r1_diag.json` | A3 | `c78e5368c61f` | 5,699 | `4dc94009e2da` |
| 192 | `.tmp/_v3r1_run1.log` | A3 | `6d08fef6755f` | 5,062 | `de8ad26b54c8` |
| 193 | `.tmp/_v3r1_run2.log` | A3 | `58a557cb0426` | 2,066 | `24e1969b5e45` |
| 194 | `.tmp/_v5_c5_b_clause4_consistency_check.py` | A3 | `4658e9ff764d` | 6,528 | `58ce60c11ed9` |
| 195 | `.tmp/_v5_c5_b_fetch_raw_embeddings.py` | A3 | `13004c626ba2` | 9,476 | `060da13ce763` |
| 196 | `.tmp/_v5_item21_anchor_driver.py` | A3 | `f17e527cfa4f` | 5,401 | `fe55a6133d21` |
| 197 | `.tmp/_v5_item21_patch.diff` | A3 | `9ce076070280` | 19,685 | `893d283024c2` |
| 198 | `.tmp/_v5_item21_patched_b1_semA_none_default.py` | A3 | `2d02d5547f4f` | 16,768 | `73ba04b3ae71` |
| 199 | `.tmp/_v5_item21_patched_b1_semB_none_skip.py` | A3 | `05353829c864` | 16,829 | `935801fcae82` |
| 200 | `.tmp/_v5_item21_patched_b2_semA_none_default.py` | A3 | `53b844a9e184` | 16,036 | `1fabd981724f` |
| 201 | `.tmp/_v5_item21_patched_b2_semB_none_skip.py` | A3 | `73a7d1558159` | 16,097 | `4e8ad6650b28` |
| 202 | `.tmp/_v5_item21_patched_b3_semA_none_default.py` | A3 | `df9efa13fa0a` | 15,778 | `9c8eb11f3e3e` |
| 203 | `.tmp/_v5_item21_patched_b3_semB_none_skip.py` | A3 | `ea7df8d6c21b` | 15,839 | `bb6858cae9f6` |
| 204 | `.tmp/_v5_loadcorpus_verify_2026_09_29.py` | A3 | `c111c4ea2aab` | 8,798 | `aa5a34a44f7e` |
| 205 | `.tmp/_v5_qwen_retry_candidates_20260929.py` | A3 | `222239e99b8a` | 1,689 | `ba6b414cf529` |
| 206 | `.tmp/_v5_qwen_retry_introspect_20260929.py` | A3 | `ec11b2b73f30` | 3,149 | `1b6acae668c1` |
| 207 | `.tmp/_verdict_keeper_sha_helper.ps1` | A3 | `f2e18d5bf156` | 679 | `19808ebc14cf` |
| 208 | `.tmp/_verify_d8_addendum_2026_09_30.py` | A3 | `9f970f8226df` | 4,900 | `42c95e41e08a` |
| 209 | `.tmp/_verify_tail.py` | A3 | `f167216d15f7` | 733 | `2e7a3238cd9b` |
| 210 | `.tmp/_verify_two_pieces_2026_09_30.py` | A3 | `87a802ea14b2` | 4,739 | `bf5488dd3e03` |
| 211 | `.tmp/f2_branch_fix_transform_2026_09_29.py` | A3 | `89b3dce63800` | 18,152 | `6147078b74be` |
| 212 | `.tmp/f2_branch_selftest_2026_09_29.py` | A3 | `fc239a38f5bd` | 7,377 | `ecd789f3b87b` |
| 213 | `.tmp/verif_doubt6/baseline_pre.json` | A3 | `faf21d9c274e` | 95,139 | `f1c47aa6b61c` |
| 214 | `_tmp_degen.py` | S5 | `b23f3a0d442a` | 719 | `0b2b0d5f284b` |
| 215 | `_tmp_v1_recompute.py` | S5 | `3f107092cef8` | 9,819 | `408508b1adc9` |
| 216 | `_tmp_v2_redesign.py` | S5 | `e94639d36c20` | 13,762 | `b30e20ade70f` |
| 217 | `_tmp_verify.py` | S5 | `65332b2e2112` | 384 | `a73c0df7b7c6` |
| 218 | `audits_dataset_health.json` | S3 | `4a33af111f0f` | 7,398 | `cf6ef1c7e631` |
| 219 | `corpus/v20_caption_surface/_v41_flash_rag_caption_embs.bak.json` | S5 | `cfd8b638f42d` | 612,511 | `21ffca2f540f` |
| 220 | `docs/DATASET_HEALTH_v2.md` | S3 | `db57fcae77b1` | 4,892 | `745af537d3ee` |
| 221 | `docs/V3X/D3_ONLINE_MIDTERM_TEMPLATE.md` | S5 | `a0ea7fd3795d` | 4,397 | `9975e2d58fe2` |
| 222 | `docs/V3X/D7_ONE_PAGE_SUMMARY_TEMPLATE.md` | S5 | `223297c38fb6` | 5,862 | `71a17c0f1d74` |
| 223 | `results/_archive_2026_09_20/REVIEWER_B_TMP_RERUN_2026_09_15.md` | S5 | `3ef2e8075f1b` | 21,654 | `eb4c98ffcb95` |
| 224 | `results/_archive_2026_09_20/_audit_temp_inspect_minimax_m3.py.bak` | S5 | `96bb0a05de8b` | 1,171 | `6e559468d5c3` |
| 225 | `results/_archive_2026_09_20/_audit_temp_inspect_workers.py.bak` | S5 | `843afd0baa41` | 1,158 | `37dcb976fef4` |
| 226 | `results/_archive_2026_09_20/_audit_temp_stage1_tra_breakdown.py.bak` | S5 | `e96ad684b886` | 18,023 | `317fce89d2ca` |
| 227 | `results/_archive_2026_09_20/_openrouter_emb_runner.bak.note` | S5 | `af0744ae0a65` | 5 | `2b3ede460692` |
| 228 | `results/_archive_2026_09_20/_reviewer_a_audit_tmp.py` | S5 | `328c8ae04f63` | 4,397 | `132b55b0d9a0` |
| 229 | `results/_archive_2026_09_20/_teamorouter_smoke_tmp.json` | S5 | `1ad387806df3` | 277 | `40b7cd9f5a01` |
| 230 | `results/_archive_2026_09_20/_temp_volc_test.py` | S5 | `55dea38ae84b` | 6,687 | `bb482f9ed22e` |
| 231 | `results/_archive_2026_09_20/_tmp_inspect_22cap.py` | S5 | `fb642fd29028` | 675 | `36e5f69d7fd5` |
| 232 | `results/_archive_2026_09_20/_tmp_inspect_5model.py` | S5 | `1bb17e5de63d` | 1,029 | `97f604b07e92` |
| 233 | `results/_archive_2026_09_20/_tmp_probe_archive` | S5 | `4edd37d18fbc` | 1,270 | `2c005210d113` |
| 234 | `results/_archive_2026_09_20/_v41_flash_rag_caption_embs.bak.json` | S5 | `cfd8b638f42d` | 612,511 | `e82e31e2ef6a` |
| 235 | `results/_archive_2026_09_20/_v41_flash_rag_partial.bak.json` | S5 | `889558f0e014` | 88,584 | `49ae49495cbd` |
| 236 | `results/_archive_2026_09_24/_v4_pi_decision_questionnaire_2026_09_21_v1.1.md.bak_2026_09_22_gB_post.md` | S5 | `a7a80c786fa2` | 113,424 | `9a4dc287feba` |
| 237 | `results/_g10_threshold_closed_domain_judgment_2026_10_11.md` | S5 | `1397dbcbeafe` | 55,667 | `621c2ed0fa75` |
| 238 | `results/_g5_displacement_threshold_c_approval_effect_and_trigger_eval_2026_10_10.md` | S5 | `2eb998b23b93` | 33,880 | `85355676c64e` |
| 239 | `results/_g5_displacement_threshold_draft_2026_10_10.md` | S5 | `910f0bf4bb5f` | 25,619 | `17f02e853e30` |
| 240 | `results/_ghostref_copy_log_2026_09_23.json` | S5 | `be98a7b238b0` | 120,810 | `32e7b06a0de3` |
| 241 | `results/_glm_response_v2_template_2026_09_18.md` | S5 | `9da3d432a134` | 44,133 | `7c5703fad696` |
| 242 | `results/_round23_26_threshold_review_effect_register_2026_10_10.md` | S5 | `d228cf0906d6` | 47,297 | `2e9050c3f167` |
| 243 | `results/_round56_idx_sc1_temp_deletion_deviation_note_2026_10_10.md` | S5 | `9aabb430172f` | 8,143 | `c68024ab09ee` |
| 244 | `results/_s4_v31_regen_gold_items_2026_10_10.json` | S5 | `c4a10b4cfe31` | 36,830 | `fcadc56979ce` |
| 245 | `results/_s4_v31_regen_gold_register_2026_10_10.md` | S5 | `3a539beb90ec` | 27,133 | `90a3a3ab7e5f` |
| 246 | `results/_stage3_1_register_fingerprint_placeholder_erratum_2026_10_12.md` | S5 | `1842e1b1dd01` | 4,475 | `9ae2477984a2` |
| 247 | `results/_t1_prereg_revision_qwen_temp_sweep_2026_10_09.md` | S5 | `6cf8666d955b` | 16,994 | `79eb335f5141` |
| 248 | `results/_t1_prereg_revision_temp_axis_exp2_2026_10_09.md` | S5 | `fbaf34a68c17` | 34,217 | `30a251208318` |
| 249 | `results/_t1_qwen_temp_sweep_exec_register_2026_10_09.md` | S5 | `cfc0fdf8d212` | 17,341 | `be9bb0180152` |
| 250 | `results/_t1_qwen_temp_sweep_executor_2026_10_09.py` | S5 | `a87adc2ed532` | 32,393 | `0d5aefaf6750` |
| 251 | `results/_t1_qwen_temp_sweep_r2_exec_register_2026_10_09.md` | S5 | `b633a675c9de` | 23,683 | `6d68adfda98a` |
| 252 | `results/_t1_qwen_temp_sweep_r2_executor_2026_10_09.py` | S5 | `ff15ac539b98` | 53,180 | `c1da8d161c0b` |
| 253 | `results/_t1_qwen_temp_sweep_r2_result_2026_10_09.json` | S5 | `308419654ed7` | 58,665 | `87126807e3dc` |
| 254 | `results/_t1_qwen_temp_sweep_r2_verdict_2026_10_09.md` | S5 | `b741fa6b165a` | 42,817 | `c2082c4fed57` |
| 255 | `results/_t1_qwen_temp_sweep_verdict_2026_10_09.md` | S5 | `d1905830b2bd` | 21,652 | `bca7d63d539f` |
| 256 | `results/_t1_temp_axis_new_experiment_design_2026_10_09.md` | S5 | `846f4d14836f` | 41,392 | `723cbec6ab10` |
| 257 | `results/_t1_temp_axis_retirement_consolidation_2026_10_10.md` | S5 | `b07c62634e54` | 20,308 | `e8b3b3672f10` |
| 258 | `results/_t1_temp_axis_retirement_judgment_2026_10_10.md` | S5 | `5832a5c071d0` | 27,384 | `a61e113bebe9` |
| 259 | `results/_tmp_disposal_register_2026_10_10.md` | S5 | `4b2d2c2b8125` | 20,812 | `14f708509f62` |
| 260 | `results/_v3_s_phrasetemplate_prereg_v1_2026_09_27.md` | S5 | `40784ebff5bd` | 33,932 | `23217908421f` |
| 261 | `results/_v3r1_threshold_final_path_judgment_2026_10_10.md` | S5 | `1d2d82bd994e` | 39,653 | `cc1d6f2291f9` |
| 262 | `results/_v3r1_threshold_path4_draft_2026_10_10.md` | S5 | `487781f03f7f` | 39,077 | `5657b35ebbef` |
| 263 | `results/_v3r1_threshold_restatement_design_2026_10_10.md` | S5 | `f2d7b875aa42` | 33,847 | `c0acb218eeed` |
| 264 | `results/_v4_pi_cot_v2_dataset.json` | S3 | `fc0a48202902` | 12,672 | `f1c2c373e75c` |
| 265 | `results/_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | S3 | `f91692efd347` | 4,103 | `f4c5f4a22084` |
| 266 | `results/_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json` | S3 | `11548fa9c347` | 6,132 | `12af91501ec7` |
| 267 | `results/_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json` | S3 | `4de634e0ad8e` | 7,566 | `7e30fcba407e` |
| 268 | `results/_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json` | S3 | `bbabf547f6df` | 6,666 | `31d60405eed5` |
| 269 | `results/_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json` | S3 | `2c84943121fb` | 7,668 | `28f99be89b44` |
| 270 | `results/_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json` | S3 | `65ad8aacb53d` | 10,257 | `fbe1a96a83cb` |
| 271 | `results/_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json` | S3 | `f59b97601d73` | 11,589 | `201eb40b2352` |
| 272 | `results/_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json` | S3 | `95fff0a09d87` | 14,722 | `4c6eb02b13cf` |
| 273 | `results/_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | S3 | `5cb3a1cbb369` | 19,615 | `d8e01c25f6f3` |
| 274 | `results/_v4_pi_cot_v3_dataset.json` | S3 | `8c0300e90060` | 16,025 | `8b80f93d9e0b` |
| 275 | `results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json` | S3 | `fc04fe9be042` | 20,194 | `61ef6bff9528` |
| 276 | `results/_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json` | S3 | `570275c1731a` | 18,714 | `c6e0d6b59168` |
| 277 | `results/_v4_pi_cot_v3_dataset_addendum_d5_2026_09_27.json` | S3 | `1f1904c9d786` | 16,587 | `bb6fca155a19` |
| 278 | `results/_v4_pi_cot_v3_dataset_addendum_d6_2026_09_28.json` | S3 | `b60f81e8f595` | 19,214 | `aa5ce1f96c08` |
| 279 | `results/_v4_pi_cot_v3_dataset_addendum_d6b_2026_09_28.json` | S3 | `d0b2e5bfd237` | 27,009 | `8aa37037ef39` |
| 280 | `results/_v4_pi_cot_v3_dataset_addendum_d8_bhalf_2026_09_30.json` | S3 | `945e2a9c7605` | 58,581 | `a2b13900ae28` |
| 281 | `results/_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json` | S3 | `66362bf125e7` | 374,072 | `b036ee4c13be` |
| 282 | `results/_v4_pi_cot_v3_dataset_addendum_s3_d1fill_2026_10_01.json` | A2+S3 | `0e2301038e1c` | 46,909 | `0662a9fc6168` |
| 283 | `results/_v4_pi_cot_v3_dataset_addendum_s3_d7_2026_09_29.json` | S3 | `07f910b7397a` | 17,252 | `b6a22e6cf890` |
| 284 | `results/_v4_pi_cot_v3_dataset_v1p3_2026_09_27.json` | S3 | `4004f2c5eec3` | 12,975 | `3ae72acad66e` |
| 285 | `results/_v4_supp_t15r2_methodology_template.md` | S5 | `9427c4c42c97` | 17,411 | `c187916dc13e` |
| 286 | `results/_v4_tmp_cleanup_2026_09_28.md` | S5 | `aa3a94399724` | 5,131 | `43f4077e993e` |
| 287 | `results/_v5_proxy_temp_T0.3.json` | S5 | `794b2b55de0f` | 143,345 | `1d4962b3755f` |
| 288 | `results/_v5_proxy_temp_T1.5.json` | S5 | `29aaabc97a4b` | 143,261 | `a84c51c3b216` |
| 289 | `tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/_old_corpus_view.py` | S5 | `c3f0ec7ba9fb` | 23,893 | `88dc7d8a51d5` |
| 290 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v4_tmp_cleanup_2026_09_28.md` | S5 | `a2c177ec2bfe` | 5,122 | `cbdf8e990781` |
| 291 | `verifier/handoff/KT_ABC1_anchors_sha256_12.root_session_11318B.bak_2026_09_23.json` | S5 | `a2b148ab39e8` | 11,318 | `933c6ce3e1e8` |
| 292 | `audits_dataset_health.json` | S3 | `4a33af111f0f` | 7,398 | `9c9f26ae1b9e` |
| 293 | `docs/DATASET_HEALTH_v2.md` | S3 | `db57fcae77b1` | 4,892 | `3af4695f09d7` |

## R-S5 `S3` 隐私面专项核验

- `S3` 面 25 条（属 293 之内）：删后总验独立核验 **25/25 0 在位**（全树 0 命中）
- 声明：`E4`「永不上传」禁令**存续**——本轮仅删除远端在位件，0 读作风险已除之解禁；隐私面实体 0 再上传、0 内容转述

## R-S6 `S5` 面之执行与 0 断言

- `S5` 面 58 件（属 293 之内）已随本轮删除，逐件证据＝R-S4 全表之 `S5` 行
- 「125 件不可复原」之面：本棒 **0 断言**（不实证、不否认）；执行面仅以 293 路径表为据

---

# 乙 ｜ 覆盖面回执（10 件逐件 ＋ 组B 0 覆盖）

## 乙-1 逐件覆盖对照（覆前 → 覆后）

| # | 仓内路径（远端＝`_september_workspace/<rel>`） | 区 | 覆前 SHA-12 ／ bytes ／ 行 | 覆后 SHA-12 ／ bytes ／ 行 | commit-12 | 逐字节＝本地 |
|--:|---|:-:|---|---|---|---|
| #1 | `results/_kd_19_ambiguous_tags_rejudge_rewrite_register_2026_10_10.md` | SUB | `d15d568263ea` ／ 29,664 ／ 230 | `18a9f0bc6409` ／ 29,664 ／ 230 | `fc869a6facaa` | ✅ |
| #2 | `results/_kd_heteronym_classification_disposition_2026_10_09.md` | SUB | `b599603f8215` ／ 29,761 ／ 311 | `ac32249b79c9` ／ 29,761 ／ 311 | `3593b07d34cc` | ✅ |
| #3 | `results/_kd_resolvability_and_optional_experiments_2026_10_09.md` | SUB | `23b1ac0af9e5` ／ 70,328 ／ 476 | `a69fcae9ce3d` ／ 70,328 ／ 476 | `4decef802ed6` | ✅ |
| #4 | `results/_kd_writing_convention_guidance_2026_10_09.md` | REPO | `31344dc9a77d` ／ 20,179 ／ 193 | `f1c7d5d987c7` ／ 20,179 ／ 193 | `5e9db2ee1684` | ✅ |
| #5 | `results/_kv3s_3_2_terminal_verdict_2026_10_01.md` | SUB | `e59531f06223` ／ 32,296 ／ 307 | `826ea32705ed` ／ 32,296 ／ 307 | `ae34d7d9949a` | ✅ |
| #6 | `results/_mini_round_6_7_settlement_register_2026_10_01.md` | SUB | `12c3be4c2a40` ／ 68,053 ／ 434 | `518b209d97b4` ／ 68,053 ／ 434 | `4421b776ecb0` | ✅ |
| #7 | `results/_s3_d1_rulings_supplement_register_2026_10_01.md` | SUB | `17ba92d24cd4` ／ 28,762 ／ 280 | `d60dadddb99c` ／ 28,762 ／ 280 | `9cab7eea36fb` | ✅ |
| #12 | `results/_t1_substrate_gap_precondition_2026_10_01.md` | REPO | `62d7d7c4bee9` ／ 22,196 ／ 203 | `8ec92ab97e47` ／ 22,196 ／ 203 | `b8292dfebc4a` | ✅ |
| #15 | `results/_verdict_pack_d_prep_2026_10_01.md` | SUB | `de93624ff635` ／ 49,471 ／ 429 | `2c441b0d9326` ／ 49,471 ／ 429 | `70a503001787` | ✅ |
| #16 | `tools/exp_harness.py` | REPO | `b440f527eb54` ／ 10,090 ／ 280 | `ffe1669dbf40` ／ 45,590 ／ 803 | `bd89e1ffffe0` | ✅ |

注：组A 9 件覆后 SHA 与碰撞登记之本地指纹逐件相符；唯一差异面（锚件指纹字面 `dc9cb0e02922`／28,370 对远端旧引 `66f900b7598b`／28,352）已随覆盖对齐双区现态。KD-25 域级保留照录——本地 115 件引旧指纹之域级处置**归 PI**，本棒仅执行授权之 9 件单件覆盖。

## 乙-2 `#16 tools/exp_harness.py` 专项（PI 括注之警之实体消解）

- 覆前：远端 09-20 镜像版（`b440f527eb54` ／ 10,090 B ／ 280 行）
- 覆后：本地当前版 V0.2→V0.6 全块（`ffe1669dbf40` ／ 45,590 B ／ 803 行），内容逐字节＝本地
- **PI 令「路径改仓内路径」之执行**：L108/L109 之机-specific 绝对路径已改写为锚定文件位之仓内相对径——

```python
V20_PATH = str(Path(__file__).resolve().parent.parent / 'results' / 'deposon_v20_baselines.json')
V21_PATH = str(Path(__file__).resolve().parent.parent / 'results' / 'deposon_v21_gtformal.json')
```

- 验证：`py_compile` 通过；全文件绝对路径正则（`〔本机路径〕/`｜`〔本机路径〕/`｜机主目录字面）**0 命中**；`V20_PATH`／`V21_PATH` 全文件仅定义行、0 他处引用（类型保持 `str`，运行语义不变；本地原件同步更新为此版）
- 故 PI 括注之警「#16 直覆将绝对路径推入上传面」之**实体已消解**（覆后版不含绝对路径）——⛔ 0 宣称免责，仅登记实体面

## 乙-3 组B 6 件 0 覆盖之确认

| # | 仓内路径 | 终态远端 SHA-12 | 与基线相符 |
|--:|---|---|---|
| #8 | `results/_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` | `d03126028128` | ✅ 0 覆盖 |
| #9 | `results/_s4_heldout_sampling_seedthird_extractor_2026_10_11.py` | `1b1f027db264` | ✅ 0 覆盖 |
| #10 | `results/_s4prime_readings_runner_2026_10_11.py` | `1ea332165702` | ✅ 0 覆盖 |
| #11 | `results/_s5doubleprime_five_lines_runner_2026_10_11.py` | `93d13cd8a5fa` | ✅ 0 覆盖 |
| #13 | `results/_v3_recheck_05_executor_2026_09_28.py` | `01b8e0ccd990` | ✅ 0 覆盖 |
| #14 | `results/_v3_recheck_05_result_2026_09_28.json` | `948ae3ece224` | ✅ 0 覆盖 |

---

# 丙 ｜ 后续面回执（本棒名下）

## 丙-1 8 件第三方漂移 rel 补列全

- `results/` 下 6 件：`results/_experiment_execution_plan_v1_1_funnel5_adopted_2026_10_18.md` ｜ `results/_pi_dual_ruling_register_ge02_acceptance_ge01_readiness_2026_10_12.md` ｜ `results/_repo_state_auth_refresh_register_2026_10_18.md` ｜ `results/_v5_spec_prereq_reference_archive_2026_10_18.md` ｜ `results/verify_ge02_acceptance.py` ｜ `results/verify_ge02_acceptance_results.json`
- `letters/_bob_minimax_delegation_reply_third_supplement_2026_10_12.md`
- `paper/deposon_paper_unique_thread_v10_2026_10_18.md`

## 丙-2 KD-REV18-9 时点差澄清

- `aca25bc7` 时点「53 件 0 推送」为真；`877e59c0`（11:37:53）后 53 件落位——**两函皆无失**，差在快照时点。如实登记，0 翻案

## 丙-3 登记事项

- KD-REV18-2 复验：`_september_workspace/.gitignore` 仍 91 B 旧版（顶层 105 B 已新）——只报不改，处置归 PI
- commit message 两式并存（见 §0 如实交代）
- KD-25 域级保留照录（115 件，处置归 PI）；KD-24 `#5`／`#7` 之 `_glm_evidence_unpacked_2026_10_13/` 内同名副本不在本轮授权射程，0 触碰

---

# 门禁与纪律自证

- 0 密钥明文 ｜ 0 PAT 片段 ｜ 0 推理文本引用 ｜ 0 词条明文（本回执主体落盘前经门禁正则族自检 0 命中）
- 凭据径：PAT 仅走进程环境变量，0 落盘、0 打印、0 入 commit／message／文稿
- ref 更新全 fast-forward（force=false）；逐件独立 commit；race 重基 0 发生至终
- 路径表述：本回执路径列以**仓内路径**为主，远端＝`_september_workspace/<rel>`（KD-23 之勘之体例）

*回执毕 ｜ KIMI（上传执行棒）｜ 2026-10-18 ｜ 0 代裁 · 0 闭 KD · 0 落五终判*
