# ③ 段移动映射表（旧路径 → 新路径）· 2026-10-22

- 依据：PI 2026-10-22 20:15 卡答裁四（`ask_f1959ef42c84738879aa025f`）逐字「**是，B ＝ 第二项；映射表与移动一次走完 283 件**」；落账件 `pi_rulings\_pi_card_answers_register_2026_10_22_v235.md`
- 源：勘查件 `_reorg_survey_and_disposition_2026_10_22.md`（`cbd85f8c5522`）§4-1 之 315 行中，拟去处为「归档区」与「sub」者
- 本表行数：**283**（拟 283；其中 **4 件已因裁三去重复而先删** ⇒ 实可移 279）
- 目标容器（各一，沿既有 `_movedout_*` 惯例 ＋ 扁平化命名沿 `_c514_remote_blobs_*` 体例）：
  - 归档区：`〔归档区〕\_movedout_2026_10_22\<扁平名>`（`/` 与 `\` 皆替为 `___`）
  - sub：`deposon-sub\_movedin_2026_10_22\<扁平名>`
- **执行前实测**：目标撞名 **0**／源缺 **0**／批内同目标重名 **0**
- 通道：文件**移动**（非删除）；本表即移动之唯一凭据，亦为幽灵登记之「旧→新」源

## §1 逐件（279 行）

| # | SHA-12 | bytes | 去处 | 旧路径（仓根相对） | 新路径 |
|--:|:--|--:|:--|:--|:--|
| 1 | `106e8667be2d` | 72704 | 归档区 | `results/_exp04_h_contrast_readings_2026_10_10.json` | `〔归档件引用·未上传:results____exp04_h_contrast_readings_2026_10_10.json〕` |
| 2 | `e87937d55471` | 65507 | 归档区 | `results/_k_v3df_0_1_four_readings_2026_10_09.json` | `〔归档件引用·未上传:results____k_v3df_0_1_four_readings_2026_10_09.json〕` |
| 3 | `4a9b6c5e47af` | 61109 | 归档区 | `results/_runface_vs_shape_multidim_reading_2026_10_20.json` | `〔归档件引用·未上传:results____runface_vs_shape_multidim_reading_2026_10_20.json〕` |
| 4 | `f6f172820c97` | 51716 | 归档区 | `results/deposon_volcengine_worker_c_2026_09_10.json` | `〔归档件引用·未上传:results___deposon_volcengine_worker_c_2026_09_10.json〕` |
| 5 | `b1eb668377ce` | 49338 | 归档区 | `results/deposon_volcengine_worker_b_2026_09_10.json` | `〔归档件引用·未上传:results___deposon_volcengine_worker_b_2026_09_10.json〕` |
| 6 | `e3dae2a4bbc2` | 35011 | 归档区 | `results/_v4_track2_multimodel_rerun_2026_09_23.json` | `〔归档件引用·未上传:results____v4_track2_multimodel_rerun_2026_09_23.json〕` |
| 7 | `f06313373fc6` | 21629 | 归档区 | `results/_ge01_prereg_5anchor_v2.json` | `〔归档件引用·未上传:results____ge01_prereg_5anchor_v2.json〕` |
| 8 | `33ad1c01f745` | 20398 | 归档区 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` | `〔归档件引用·未上传:results___deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json〕` |
| 9 | `c43a84c70935` | 16043 | 归档区 | `results/_pa_harness_anchor_value_update_v2.json` | `〔归档件引用·未上传:results____pa_harness_anchor_value_update_v2.json〕` |
| 10 | `218ef1a99f97` | 11703 | 归档区 | `results/deposon_volcengine_minimax_m3_30cells_2026_09_10.py` | `〔归档件引用·未上传:results___deposon_volcengine_minimax_m3_30cells_2026_09_10.py〕` |
| 11 | `66be80ab4b81` | 11446 | 归档区 | `results/_s4_substrate_grid_availability_2026_10_08.json` | `〔归档件引用·未上传:results____s4_substrate_grid_availability_2026_10_08.json〕` |
| 12 | `4b020eb04605` | 10701 | 归档区 | `results/_ge01_prereg_5anchor.json` | `〔归档件引用·未上传:results____ge01_prereg_5anchor.json〕` |
| 13 | `2a7749da7c4d` | 9996 | 归档区 | `results/c5_b_group_fix_readings_2026_10_01.json` | `〔归档件引用·未上传:results___c5_b_group_fix_readings_2026_10_01.json〕` |
| 14 | `47177cab0303` | 9527 | 归档区 | `results/_v5_item21_anchor_recompute_2026_09_28.json` | `〔归档件引用·未上传:results____v5_item21_anchor_recompute_2026_09_28.json〕` |
| 15 | `1665f367b2c4` | 9068 | 归档区 | `results/_v4_pi_cot_v2_result.json` | `〔归档件引用·未上传:results____v4_pi_cot_v2_result.json〕` |
| 16 | `a3ca05aec6fb` | 8112 | 归档区 | `results/deposon_volcengine_glm_latest_5cells_2026_09_10.py` | `〔归档件引用·未上传:results___deposon_volcengine_glm_latest_5cells_2026_09_10.py〕` |
| 17 | `821465001819` | 5876 | 归档区 | `results/_v4_pi_cot_v2_ruleset.json` | `〔归档件引用·未上传:results____v4_pi_cot_v2_ruleset.json〕` |
| 18 | `83c35597af81` | 4895 | 归档区 | `results/deposon_volcengine_glm_latest_5cells_2026_09_10.json` | `〔归档件引用·未上传:results___deposon_volcengine_glm_latest_5cells_2026_09_10.json〕` |
| 19 | `1ded6731cc27` | 2398383 | 归档区 | `results/deposon_v2_phase3_strip_embeddings_2026_09_11.json` | `〔归档件引用·未上传:results___deposon_v2_phase3_strip_embeddings_2026_09_11.json〕` |
| 20 | `9fcb6b243e0d` | 656572 | 归档区 | `results/deposon_benchmark_v1_3_details.json` | `〔归档件引用·未上传:results___deposon_benchmark_v1_3_details.json〕` |
| 21 | `ca71aa6858e1` | 631644 | 归档区 | `results/deposon_v20_corpus_eval.json` | `〔归档件引用·未上传:results___deposon_v20_corpus_eval.json〕` |
| 22 | `25f745609658` | 612511 | 归档区 | `corpus/v20_caption_surface/_v41_flash_rag_caption_embs.bak.json` | `〔归档件引用·未上传:corpus___v20_caption_surface____v41_flash_rag_caption_embs.bak.json〕` |
| 23 | `c16d1768d1ca` | 519387 | 归档区 | `results/deposon_v15_diffusion.json` | `〔归档件引用·未上传:results___deposon_v15_diffusion.json〕` |
| 24 | `00ee97c82dcc` | 416460 | 归档区 | `results/deposon_v15_diffusion_maxpath_negativeresult.json` | `〔归档件引用·未上传:results___deposon_v15_diffusion_maxpath_negativeresult.json〕` |
| 25 | `910c4333eead` | 409104 | 归档区 | `results/deposon_v19_benchmark_fixes.json` | `〔归档件引用·未上传:results___deposon_v19_benchmark_fixes.json〕` |
| 26 | `a63ebea7b29a` | 235779 | 归档区 | `results/deposon_benchmark_v1_4_strategyqa_details.json` | `〔归档件引用·未上传:results___deposon_benchmark_v1_4_strategyqa_details.json〕` |
| 27 | `39f79fce7cdb` | 208350 | 归档区 | `results/deposon_benchmark_v1_4_gsm8k_details.json` | `〔归档件引用·未上传:results___deposon_benchmark_v1_4_gsm8k_details.json〕` |
| 28 | `9f88a212a77c` | 204441 | 归档区 | `results/deposon_d_fix2_metric_verify_9m60c_2026_09_15.json` | `〔归档件引用·未上传:results___deposon_d_fix2_metric_verify_9m60c_2026_09_15.json〕` |
| 29 | `3b1c881c4594` | 132875 | 归档区 | `audits_outliers.json` | `〔归档件引用·未上传:audits_outliers.json〕` |
| 30 | `a2ae7997ee67` | 123331 | 归档区 | `results/deposon_v20_gt2b.json` | `〔归档件引用·未上传:results___deposon_v20_gt2b.json〕` |
| 31 | `2e55c53be25d` | 111710 | 归档区 | `results/deposon_openrouter_5model_rag_30cells_2026_09_10.json` | `〔归档件引用·未上传:results___deposon_openrouter_5model_rag_30cells_2026_09_10.json〕` |
| 32 | `701ad291a714` | 106317 | 归档区 | `results/deposon_v17_fixed_sampler.json` | `〔归档件引用·未上传:results___deposon_v17_fixed_sampler.json〕` |
| 33 | `af51da229652` | 106164 | 归档区 | `results/deposon_v17_fusion_fix.json` | `〔归档件引用·未上传:results___deposon_v17_fusion_fix.json〕` |
| 34 | `556086d9e3bc` | 106125 | 归档区 | `results/deposon_v17_fusion_fix_tieartifact_negativeresult.json` | `〔归档件引用·未上传:results___deposon_v17_fusion_fix_tieartifact_negativeresult.json〕` |
| 35 | `a18bbc703b42` | 85508 | 归档区 | `results/deposon_v2_phase1_60cells_2026_09_11.json` | `〔归档件引用·未上传:results___deposon_v2_phase1_60cells_2026_09_11.json〕` |
| 36 | `62c1a41e1db8` | 80624 | 归档区 | `results/deposon_v18_api_supplements.json` | `〔归档件引用·未上传:results___deposon_v18_api_supplements.json〕` |
| 37 | `ab0c2eaff0d1` | 75964 | 归档区 | `results/deposon_dpath_cross_modal_2026_09_10.json` | `〔归档件引用·未上传:results___deposon_dpath_cross_modal_2026_09_10.json〕` |
| 38 | `fca14c5735dd` | 72647 | 归档区 | `results/deposon_v20_gt5.json` | `〔归档件引用·未上传:results___deposon_v20_gt5.json〕` |
| 39 | `9d9ae5001c57` | 69204 | 归档区 | `results/deposon_v21_gtformal.json` | `〔归档件引用·未上传:results___deposon_v21_gtformal.json〕` |
| 40 | `04b90b638bdc` | 65105 | 归档区 | `results/deposon_v20_gt6.json` | `〔归档件引用·未上传:results___deposon_v20_gt6.json〕` |
| 41 | `2907006dbe48` | 56425 | 归档区 | `results/deposon_v20_gt5b.json` | `〔归档件引用·未上传:results___deposon_v20_gt5b.json〕` |
| 42 | `108da40d5d4e` | 44443 | 归档区 | `results/deposon_v19_meanfield.json` | `〔归档件引用·未上传:results___deposon_v19_meanfield.json〕` |
| 43 | `fbbfd3ef3890` | 42458 | 归档区 | `results/deposon_v19_fullrank.json` | `〔归档件引用·未上传:results___deposon_v19_fullrank.json〕` |
| 44 | `c17b31ae4f3b` | 39974 | 归档区 | `results/deposon_v16_llm_prior.json` | `〔归档件引用·未上传:results___deposon_v16_llm_prior.json〕` |
| 45 | `4a08521f8de1` | 38545 | 归档区 | `docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` | `〔归档件引用·未上传:docs___V3X___V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md〕` |
| 46 | `283dbc8c5b63` | 35718 | 归档区 | `results/deposon_v20_bigquiz_eval.json` | `〔归档件引用·未上传:results___deposon_v20_bigquiz_eval.json〕` |
| 47 | `f119f2f30287` | 34393 | 归档区 | `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC.md` | `〔归档件引用·未上传:docs___V3X___P_D_FINGERPRINT_V0_3_SPEC.md〕` |
| 48 | `fcb5105df0b6` | 33829 | 归档区 | `results/deposon_pf_d1_full_9m5c_2026_09_15.json` | `〔归档件引用·未上传:results___deposon_pf_d1_full_9m5c_2026_09_15.json〕` |
| 49 | `4ec04d3d7d8c` | 32995 | 归档区 | `results/deposon_volcengine_glm_latest_30cells_v2_2026_09_10.json` | `〔归档件引用·未上传:results___deposon_volcengine_glm_latest_30cells_v2_2026_09_10.json〕` |
| 50 | `70ea38d5b9c0` | 28449 | 归档区 | `reviews/literature_scan_v19.md` | `〔归档件引用·未上传:reviews___literature_scan_v19.md〕` |
| 51 | `509dcee3b139` | 27311 | 归档区 | `results/deposon_pf_implementation_2026_09_11.json` | `〔归档件引用·未上传:results___deposon_pf_implementation_2026_09_11.json〕` |
| 52 | `506810017d34` | 25464 | 归档区 | `results/deposon_volcengine_worker_a_2026_09_10.json` | `〔归档件引用·未上传:results___deposon_volcengine_worker_a_2026_09_10.json〕` |
| 53 | `063ac8d00542` | 25049 | 归档区 | `results/deposon_v3_v7_summary_2026_09_11.json` | `〔归档件引用·未上传:results___deposon_v3_v7_summary_2026_09_11.json〕` |
| 54 | `0a8ed127d6de` | 24435 | 归档区 | `results/deposon_v42_v2_miss_rate_curve_2026_09_16.json` | `〔归档件引用·未上传:results___deposon_v42_v2_miss_rate_curve_2026_09_16.json〕` |
| 55 | `efe05ad775de` | 24150 | 归档区 | `corpus/v20/index_v2_2026_09_16.json` | `〔归档件引用·未上传:corpus___v20___index_v2_2026_09_16.json〕` |
| 56 | `fbb7677b9cd5` | 23472 | 归档区 | `results/deposon_volcengine_minimax_m3_30cells_2026_09_10.json` | `〔归档件引用·未上传:results___deposon_volcengine_minimax_m3_30cells_2026_09_10.json〕` |
| 57 | `03c8baa18d93` | 23042 | 归档区 | `docs/REFACTOR_v2.md` | `〔归档件引用·未上传:docs___REFACTOR_v2.md〕` |
| 58 | `5149f5cafcf9` | 23034 | 归档区 | `results/deposon_volcengine_seed_code_30cells_2026_09_10.json` | `〔归档件引用·未上传:results___deposon_volcengine_seed_code_30cells_2026_09_10.json〕` |
| 59 | `9194ee703218` | 22623 | 归档区 | `results/deposon_v20_quiz_eval.json` | `〔归档件引用·未上传:results___deposon_v20_quiz_eval.json〕` |
| 60 | `b2046af03610` | 20408 | 归档区 | `results/deposon_pc_d1_d3_2026_09_15.json` | `〔归档件引用·未上传:results___deposon_pc_d1_d3_2026_09_15.json〕` |
| 61 | `fae79888344b` | 20280 | 归档区 | `results/deposon_volcengine_worker_d_2026_09_10.json` | `〔归档件引用·未上传:results___deposon_volcengine_worker_d_2026_09_10.json〕` |
| 62 | `977fe1b48f75` | 19751 | 归档区 | `docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md` | `〔归档件引用·未上传:docs___V3X___P_A_D1_D3_REPORT_2026_09_15.md〕` |
| 63 | `e262e9d684fe` | 19327 | 归档区 | `reviews/post_edit_verification_v19.md` | `〔归档件引用·未上传:reviews___post_edit_verification_v19.md〕` |
| 64 | `aeefb8ef6972` | 19100 | 归档区 | `docs/GT_FORMALIZATION_v1.md` | `〔归档件引用·未上传:docs___GT_FORMALIZATION_v1.md〕` |
| 65 | `56401317e62b` | 18592 | 归档区 | `results/deposon_deepseek_v41_flash_30cells_v3_2026_09_10.json` | `〔归档件引用·未上传:results___deposon_deepseek_v41_flash_30cells_v3_2026_09_10.json〕` |
| 66 | `ea38ee252701` | 18290 | 归档区 | `results/deposon_gpt6_teamorouter_30cells_2026_09_10.json` | `〔归档件引用·未上传:results___deposon_gpt6_teamorouter_30cells_2026_09_10.json〕` |
| 67 | `b5873afb9d29` | 18104 | 归档区 | `results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json` | `〔归档件引用·未上传:results___deposon_p_d_b3_merkle_22_caption_2026_09_16.json〕` |
| 68 | `896589b673ec` | 17925 | 归档区 | `results/deposon_v20_gt7.json` | `〔归档件引用·未上传:results___deposon_v20_gt7.json〕` |
| 69 | `c659695aa23c` | 17732 | 归档区 | `results/deposon_v3_physical_opt_60cells_2026_09_11.json` | `〔归档件引用·未上传:results___deposon_v3_physical_opt_60cells_2026_09_11.json〕` |
| 70 | `27f9bd5cc260` | 17591 | 归档区 | `results/deposon_v3_physical_opt_2026_09_11.json` | `〔归档件引用·未上传:results___deposon_v3_physical_opt_2026_09_11.json〕` |
| 71 | `594d7a8d3de8` | 17085 | 归档区 | `results/deposon_pe_d1_d3_2026_09_15.json` | `〔归档件引用·未上传:results___deposon_pe_d1_d3_2026_09_15.json〕` |
| 72 | `f39412103366` | 17053 | 归档区 | `results/_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json` | `〔归档件引用·未上传:results____v3x_experiments_2026_09_16___v3x_experiments_results_2026_09_16.json〕` |
| 73 | `6edb2aec1660` | 16987 | 归档区 | `results/deposon_v20_baselines.json` | `〔归档件引用·未上传:results___deposon_v20_baselines.json〕` |
| 74 | `2836605ca12f` | 16896 | 归档区 | `results/deposon_v17_multigraph.json` | `〔归档件引用·未上传:results___deposon_v17_multigraph.json〕` |
| 75 | `6f3c550cec13` | 16876 | 归档区 | `docs/V3X/P_E_DOUBAN_EMBEDDING_V0_SPEC.md` | `〔归档件引用·未上传:docs___V3X___P_E_DOUBAN_EMBEDDING_V0_SPEC.md〕` |
| 76 | `523b5941c30c` | 16835 | 归档区 | `results/_v3x_p_l_v3_mistral_large_2512_20260917_115049.json` | `〔归档件引用·未上传:results____v3x_p_l_v3_mistral_large_2512_20260917_115049.json〕` |
| 77 | `67162ab18f9a` | 15721 | 归档区 | `reviews/review_coach_v2X_draft_r2.md` | `〔归档件引用·未上传:reviews___review_coach_v2X_draft_r2.md〕` |
| 78 | `e221792715f8` | 15604 | 归档区 | `results/deposon_pa_d1_d3_2026_09_15.json` | `〔归档件引用·未上传:results___deposon_pa_d1_d3_2026_09_15.json〕` |
| 79 | `c41f1717310e` | 13967 | 归档区 | `reviews/design_probe_v19.md` | `〔归档件引用·未上传:reviews___design_probe_v19.md〕` |
| 80 | `dfbcc5d6fc34` | 13775 | 归档区 | `corpus/v20_caption_surface/_p_d_v03_22caption_verification_20260917_163757.json` | `〔归档件引用·未上传:corpus___v20_caption_surface____p_d_v03_22caption_verification_20260917_163757.json〕` |
| 81 | `4e4a17d43adf` | 13562 | 归档区 | `results/deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json` | `〔归档件引用·未上传:results___deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json〕` |
| 82 | `79c7321056b8` | 13419 | 归档区 | `docs/V3X/P_C_D1_D3_REPORT_2026_09_15.md` | `〔归档件引用·未上传:docs___V3X___P_C_D1_D3_REPORT_2026_09_15.md〕` |
| 83 | `6a2656878745` | 12798 | 归档区 | `corpus/v20/strip_captions_22.json` | `〔归档件引用·未上传:corpus___v20___strip_captions_22.json〕` |
| 84 | `2f0765a1d39d` | 12501 | 归档区 | `docs/V3X/P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md` | `〔归档件引用·未上传:docs___V3X___P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md〕` |
| 85 | `ab75889ee738` | 11512 | 归档区 | `results/deposon_pg_v01_9m60c_2026_09_15.json` | `〔归档件引用·未上传:results___deposon_pg_v01_9m60c_2026_09_15.json〕` |
| 86 | `baef94e393de` | 11478 | 归档区 | `docs/V3X/KT_B1_REWORK_REPORT_2026_09_10.md` | `〔归档件引用·未上传:docs___V3X___KT_B1_REWORK_REPORT_2026_09_10.md〕` |
| 87 | `576eaf8d7431` | 11341 | 归档区 | `results/deposon_p_k_cross_subject_fingerprint_blind_test_2026_09_16.json` | `〔归档件引用·未上传:results___deposon_p_k_cross_subject_fingerprint_blind_test_2026_09_16.json〕` |
| 88 | `de450c0beffa` | 11296 | 归档区 | `docs/PAPER_BRIEF.md` | `〔归档件引用·未上传:docs___PAPER_BRIEF.md〕` |
| 89 | `5bebb5e1d329` | 11295 | 归档区 | `reviews/review_coach_v2X_outline.md` | `〔归档件引用·未上传:reviews___review_coach_v2X_outline.md〕` |
| 90 | `116d193b1607` | 10476 | 归档区 | `paper/v2/outline_v2X.md` | `〔归档件引用·未上传:paper___v2___outline_v2X.md〕` |
| 91 | `7fb001add973` | 10114 | 归档区 | `paper/v2/related_work_v2X.md` | `〔归档件引用·未上传:paper___v2___related_work_v2X.md〕` |
| 92 | `3fa0ff2c8c08` | 10096 | 归档区 | `results/deposon_game_theory_eval_2026_09_10.json` | `〔归档件引用·未上传:results___deposon_game_theory_eval_2026_09_10.json〕` |
| 93 | `0c49f2d36088` | 9979 | 归档区 | `reviews/post_draft_verification_v2X.md` | `〔归档件引用·未上传:reviews___post_draft_verification_v2X.md〕` |
| 94 | `ad0e445714d9` | 9850 | 归档区 | `docs/SPEC_v1.8.md` | `〔归档件引用·未上传:docs___SPEC_v1.8.md〕` |
| 95 | `956183753a2e` | 9809 | 归档区 | `docs/Findings_GT8B.md` | `〔归档件引用·未上传:docs___Findings_GT8B.md〕` |
| 96 | `0f36aaeeda6f` | 9191 | 归档区 | `docs/SYNTHESIS_mind_game.md` | `〔归档件引用·未上传:docs___SYNTHESIS_mind_game.md〕` |
| 97 | `20bc4288e0de` | 9176 | 归档区 | `results/deposon_v16_paired_stats.json` | `〔归档件引用·未上传:results___deposon_v16_paired_stats.json〕` |
| 98 | `d6f233d73c45` | 9098 | 归档区 | `results/boss_pa_3_replicator_dynamics_result_2026_09_15.json` | `〔归档件引用·未上传:results___boss_pa_3_replicator_dynamics_result_2026_09_15.json〕` |
| 99 | `664e7cc05aec` | 9076 | 归档区 | `results/_p_l_p_c_finite_size_scaling_2026_09_16/p_l_p_c_finite_size_scaling_results_2026_09_16.json` | `〔归档件引用·未上传:results____p_l_p_c_finite_size_scaling_2026_09_16___p_l_p_c_finite_size_scaling_results_2026_09_16.json〕` |
| 100 | `84323775a212` | 9065 | 归档区 | `docs/CLOSURE_v19_and_v2X_gametheory.md` | `〔归档件引用·未上传:docs___CLOSURE_v19_and_v2X_gametheory.md〕` |
| 101 | `56ecef878539` | 8840 | 归档区 | `reviews/experiment_design_v19.md` | `〔归档件引用·未上传:reviews___experiment_design_v19.md〕` |
| 102 | `c7c59e0d2f6c` | 8753 | 归档区 | `results/boss_pa_1_rbr_rm_result_2026_09_15.json` | `〔归档件引用·未上传:results___boss_pa_1_rbr_rm_result_2026_09_15.json〕` |
| 103 | `76479b7a5ed6` | 8404 | 归档区 | `results/deposon_v20_crossval.json` | `〔归档件引用·未上传:results___deposon_v20_crossval.json〕` |
| 104 | `35b676773243` | 7844 | 归档区 | `results/deposon_v20_gt3.json` | `〔归档件引用·未上传:results___deposon_v20_gt3.json〕` |
| 105 | `1ec7aba6afd8` | 7842 | 归档区 | `results/deposon_v19_quickwins.json` | `〔归档件引用·未上传:results___deposon_v19_quickwins.json〕` |
| 106 | `5c76137d6430` | 7530 | 归档区 | `results/boss_pa_2_potential_game_result_2026_09_15.json` | `〔归档件引用·未上传:results___boss_pa_2_potential_game_result_2026_09_15.json〕` |
| 107 | `3545c01e1291` | 7486 | 归档区 | `docs/SPEC_GT8B.md` | `〔归档件引用·未上传:docs___SPEC_GT8B.md〕` |
| 108 | `4f827071b0b8` | 7398 | 归档区 | `audits_dataset_health.json` | `〔归档件引用·未上传:audits_dataset_health.json〕` |
| 109 | `3ecb285db3d8` | 7338 | 归档区 | `reviews/review_realign_v2X.md` | `〔归档件引用·未上传:reviews___review_realign_v2X.md〕` |
| 110 | `8423ffe266af` | 7335 | 归档区 | `corpus/v20/index.json` | `〔归档件引用·未上传:corpus___v20___index.json〕` |
| 111 | `94fd018b5cc8` | 7101 | 归档区 | `results/deposon_v20_cot_quiz.json` | `〔归档件引用·未上传:results___deposon_v20_cot_quiz.json〕` |
| 112 | `67d1d8342060` | 6886 | 归档区 | `reviews/data/t2c_advlink.csv` | `〔归档件引用·未上传:reviews___data___t2c_advlink.csv〕` |
| 113 | `0b7893196d0b` | 6796 | 归档区 | `results/deposon_v20_photonics.json` | `〔归档件引用·未上传:results___deposon_v20_photonics.json〕` |
| 114 | `19555b7d9d43` | 6750 | 归档区 | `reviews/data/t2_linkpred.csv` | `〔归档件引用·未上传:reviews___data___t2_linkpred.csv〕` |
| 115 | `f48c9f09a3b4` | 6731 | 归档区 | `reviews/data/t3b_verifiable.csv` | `〔归档件引用·未上传:reviews___data___t3b_verifiable.csv〕` |
| 116 | `6e8b6e4730a8` | 6680 | 归档区 | `reviews/data/t3_mechdesign.csv` | `〔归档件引用·未上传:reviews___data___t3_mechdesign.csv〕` |
| 117 | `8ba9fada9ead` | 6567 | 归档区 | `reviews/data/t4_poa.csv` | `〔归档件引用·未上传:reviews___data___t4_poa.csv〕` |
| 118 | `67867e752f47` | 6488 | 归档区 | `results/deposon_risk3_seff_decision_2026_09_11.json` | `〔归档件引用·未上传:results___deposon_risk3_seff_decision_2026_09_11.json〕` |
| 119 | `0c3ede881fb1` | 6466 | 归档区 | `results/deposon_volcengine_glm_latest_5cells_v2_2026_09_10.json` | `〔归档件引用·未上传:results___deposon_volcengine_glm_latest_5cells_v2_2026_09_10.json〕` |
| 120 | `9466fdbf9c95` | 6351 | 归档区 | `results/deposon_cpath_simulation_2026_09_10.json` | `〔归档件引用·未上传:results___deposon_cpath_simulation_2026_09_10.json〕` |
| 121 | `fab607f0e180` | 6345 | 归档区 | `docs/Findings_GT_FORMAL.md` | `〔归档件引用·未上传:docs___Findings_GT_FORMAL.md〕` |
| 122 | `6b09de9911c0` | 6326 | 归档区 | `docs/SPEC_GT8C.md` | `〔归档件引用·未上传:docs___SPEC_GT8C.md〕` |
| 123 | `968776002868` | 6080 | 归档区 | `docs/simple_baseline_failure_analysis.md` | `〔归档件引用·未上传:docs___simple_baseline_failure_analysis.md〕` |
| 124 | `5b95d06e66b0` | 6079 | 归档区 | `results/deposon_v15_diffusion_summary.json` | `〔归档件引用·未上传:results___deposon_v15_diffusion_summary.json〕` |
| 125 | `1e4c065da058` | 5916 | 归档区 | `results/_p_o_stranger_verification_2026_09_16/p_o_stranger_verification_results_2026_09_16.json` | `〔归档件引用·未上传:results____p_o_stranger_verification_2026_09_16___p_o_stranger_verification_results_2026_09_16.json〕` |
| 126 | `64f0a3772c12` | 5860 | 归档区 | `docs/REF_VERIFICATION_v2.md` | `〔归档件引用·未上传:docs___REF_VERIFICATION_v2.md〕` |
| 127 | `c50ff98a95cc` | 5566 | 归档区 | `reviews/data/t1c_loglinear.csv` | `〔归档件引用·未上传:reviews___data___t1c_loglinear.csv〕` |
| 128 | `6de8f0e651c4` | 5520 | 归档区 | `reviews/data/t2b_linkpred.csv` | `〔归档件引用·未上传:reviews___data___t2b_linkpred.csv〕` |
| 129 | `82016e695f48` | 5450 | 归档区 | `reviews/data/t1b_classics.csv` | `〔归档件引用·未上传:reviews___data___t1b_classics.csv〕` |
| 130 | `2b88948dca19` | 5396 | 归档区 | `results/deposon_v20_gt8.json` | `〔归档件引用·未上传:results___deposon_v20_gt8.json〕` |
| 131 | `5749ce2c5bf7` | 5377 | 归档区 | `reviews/data/t2d_hiding.csv` | `〔归档件引用·未上传:reviews___data___t2d_hiding.csv〕` |
| 132 | `432ec337d586` | 5369 | 归档区 | `docs/SPEC_GT3.md` | `〔归档件引用·未上传:docs___SPEC_GT3.md〕` |
| 133 | `bac61d51fd20` | 5333 | 归档区 | `docs/SPEC_v2.0.md` | `〔归档件引用·未上传:docs___SPEC_v2.0.md〕` |
| 134 | `fbcb60cf5102` | 5266 | 归档区 | `results/_p_m_attack_surface_cost_2026_09_16/p_m_attack_surface_cost_results_2026_09_16.json` | `〔归档件引用·未上传:results____p_m_attack_surface_cost_2026_09_16___p_m_attack_surface_cost_results_2026_09_16.json〕` |
| 135 | `cf7682348617` | 5212 | 归档区 | `results/deposon_v2_phase4_f4_2026_09_11.json` | `〔归档件引用·未上传:results___deposon_v2_phase4_f4_2026_09_11.json〕` |
| 136 | `110607514753` | 5056 | 归档区 | `docs/space_release_log.json` | `〔归档件引用·未上传:docs___space_release_log.json〕` |
| 137 | `5864bbe5adae` | 5012 | 归档区 | `docs/Findings_v2.0_corrections.md` | `〔归档件引用·未上传:docs___Findings_v2.0_corrections.md〕` |
| 138 | `e6045f0920ec` | 4932 | 归档区 | `corpus/v20/S4.json` | `〔归档件引用·未上传:corpus___v20___S4.json〕` |
| 139 | `58ab335ca341` | 4894 | 归档区 | `results/deposon_volcengine_9model_30cells_2026_09_10.json` | `〔归档件引用·未上传:results___deposon_volcengine_9model_30cells_2026_09_10.json〕` |
| 140 | `e110a020954f` | 4833 | 归档区 | `reviews/data/t1_potential.csv` | `〔归档件引用·未上传:reviews___data___t1_potential.csv〕` |
| 141 | `3e3a5014cb0e` | 4743 | 归档区 | `docs/SPEC_v2.0_amendment1.md` | `〔归档件引用·未上传:docs___SPEC_v2.0_amendment1.md〕` |
| 142 | `c165cd33a362` | 4587 | 归档区 | `docs/V3X/PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md` | `〔归档件引用·未上传:docs___V3X___PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md〕` |
| 143 | `32d26cb09568` | 4566 | 归档区 | `docs/Findings_v2.0_crossval.md` | `〔归档件引用·未上传:docs___Findings_v2.0_crossval.md〕` |
| 144 | `c4b774c8e34c` | 4559 | 归档区 | `results/deposon_volcengine_22caption_embedding_2026_09_10.json` | `〔归档件引用·未上传:results___deposon_volcengine_22caption_embedding_2026_09_10.json〕` |
| 145 | `9158f54ec248` | 4377 | 归档区 | `docs/Findings_v2.0_photonics.md` | `〔归档件引用·未上传:docs___Findings_v2.0_photonics.md〕` |
| 146 | `7e5dc4b045d8` | 4364 | 归档区 | `docs/Findings_v2.0.md` | `〔归档件引用·未上传:docs___Findings_v2.0.md〕` |
| 147 | `2dc8ca9e36c1` | 4336 | 归档区 | `results/deposon_risk1_02940_decision_2026_09_11.json` | `〔归档件引用·未上传:results___deposon_risk1_02940_decision_2026_09_11.json〕` |
| 148 | `12e0de4bb103` | 4329 | 归档区 | `corpus/v20/L_historical_causality.json` | `〔归档件引用·未上传:corpus___v20___L_historical_causality.json〕` |
| 149 | `704e2fd0d021` | 4296 | 归档区 | `corpus/v20/S6_n60.json` | `〔归档件引用·未上传:corpus___v20___S6_n60.json〕` |
| 150 | `088f28524a1d` | 4276 | 归档区 | `results/_p_n_curvature_potential_coupling_2026_09_16/p_n_curvature_potential_coupling_results_2026_09_16.json` | `〔归档件引用·未上传:results____p_n_curvature_potential_coupling_2026_09_16___p_n_curvature_potential_coupling_results_2026_09_16.json〕` |
| 151 | `edf6f4465ead` | 4181 | 归档区 | `docs/SPEC_GT8.md` | `〔归档件引用·未上传:docs___SPEC_GT8.md〕` |
| 152 | `8b1a9e5113bb` | 4167 | 归档区 | `reviews/data/t1d_pagerank.csv` | `〔归档件引用·未上传:reviews___data___t1d_pagerank.csv〕` |
| 153 | `01c492a97b98` | 4123 | 归档区 | `corpus/v20/S2_n60.json` | `〔归档件引用·未上传:corpus___v20___S2_n60.json〕` |
| 154 | `584de37ebec1` | 4122 | 归档区 | `corpus/v20/S1_n60.json` | `〔归档件引用·未上传:corpus___v20___S1_n60.json〕` |
| 155 | `cf4a882160e1` | 4066 | 归档区 | `results/deposon_risk2_canonical5_decision_2026_09_11.json` | `〔归档件引用·未上传:results___deposon_risk2_canonical5_decision_2026_09_11.json〕` |
| 156 | `25f90f106451` | 4035 | 归档区 | `docs/variant_params_table.md` | `〔归档件引用·未上传:docs___variant_params_table.md〕` |
| 157 | `ff0ef9131fdd` | 3920 | 归档区 | `corpus/v20/L_algorithm_process.json` | `〔归档件引用·未上传:corpus___v20___L_algorithm_process.json〕` |
| 158 | `32ca32c00da4` | 3898 | 归档区 | `corpus/v20/L_project_management.json` | `〔归档件引用·未上传:corpus___v20___L_project_management.json〕` |
| 159 | `869c0071fbc2` | 3890 | 归档区 | `docs/Findings_GT8.md` | `〔归档件引用·未上传:docs___Findings_GT8.md〕` |
| 160 | `ff9ff3177c06` | 3847 | 归档区 | `RELEASE_v1.4.0.md` | `〔归档件引用·未上传:RELEASE_v1.4.0.md〕` |
| 161 | `f44636f5f72f` | 3827 | 归档区 | `results/deposon_gpt6_teamorouter_2026_09_10.json` | `〔归档件引用·未上传:results___deposon_gpt6_teamorouter_2026_09_10.json〕` |
| 162 | `497b9c2d6746` | 3803 | 归档区 | `results/deposon_v20_gt.json` | `〔归档件引用·未上传:results___deposon_v20_gt.json〕` |
| 163 | `afe975606d40` | 3761 | 归档区 | `results/_p_l_real_data_collapse_2026_09_16/p_l_real_data_collapse_results_v2_2026_09_16.json` | `〔归档件引用·未上传:results____p_l_real_data_collapse_2026_09_16___p_l_real_data_collapse_results_v2_2026_09_16.json〕` |
| 164 | `77b0c1466dc0` | 3699 | 归档区 | `corpus/v20/L_geography_world.json` | `〔归档件引用·未上传:corpus___v20___L_geography_world.json〕` |
| 165 | `bf0a2b544a74` | 3691 | 归档区 | `reviews/data/t3e_commit.csv` | `〔归档件引用·未上传:reviews___data___t3e_commit.csv〕` |
| 166 | `36c714eabe3b` | 3642 | 归档区 | `docs/Findings_v2.0_boss.md` | `〔归档件引用·未上传:docs___Findings_v2.0_boss.md〕` |
| 167 | `a7f479793f01` | 3563 | 归档区 | `docs/Findings_v2.0_hardening.md` | `〔归档件引用·未上传:docs___Findings_v2.0_hardening.md〕` |
| 168 | `0c7ad5235ae9` | 3562 | 归档区 | `corpus/v20/L_biological_taxonomy.json` | `〔归档件引用·未上传:corpus___v20___L_biological_taxonomy.json〕` |
| 169 | `8933d61b180a` | 3553 | 归档区 | `results/boss_pc_2_real_transverse_ising_2026_09_15.json` | `〔归档件引用·未上传:results___boss_pc_2_real_transverse_ising_2026_09_15.json〕` |
| 170 | `43731392b581` | 3456 | 归档区 | `docs/Findings_v2.0_skills.md` | `〔归档件引用·未上传:docs___Findings_v2.0_skills.md〕` |
| 171 | `8b7574b25336` | 3411 | 归档区 | `results/deposon_gsm8k_stratified.json` | `〔归档件引用·未上传:results___deposon_gsm8k_stratified.json〕` |
| 172 | `49028967ad57` | 3405 | 归档区 | `reviews/data/t3d_llmmd.csv` | `〔归档件引用·未上传:reviews___data___t3d_llmmd.csv〕` |
| 173 | `d8780859d310` | 3397 | 归档区 | `corpus/v20/L_physics_concepts.json` | `〔归档件引用·未上传:corpus___v20___L_physics_concepts.json〕` |
| 174 | `51b271548835` | 3356 | 归档区 | `docs/BASELINE_REGISTRY.md` | `〔归档件引用·未上传:docs___BASELINE_REGISTRY.md〕` |
| 175 | `e6cc74f9917d` | 3322 | 归档区 | `docs/Findings_GT2B.md` | `〔归档件引用·未上传:docs___Findings_GT2B.md〕` |
| 176 | `01d9c95ea690` | 3320 | 归档区 | `corpus/v20/S6.json` | `〔归档件引用·未上传:corpus___v20___S6.json〕` |
| 177 | `4b10f9cae09f` | 3319 | 归档区 | `corpus/v20/S5.json` | `〔归档件引用·未上传:corpus___v20___S5.json〕` |
| 178 | `68a5b08ef007` | 3318 | 归档区 | `docs/SPEC_GT2B.md` | `〔归档件引用·未上传:docs___SPEC_GT2B.md〕` |
| 179 | `d4ed18152dc0` | 3291 | 归档区 | `docs/Findings_v2.0_bigquiz.md` | `〔归档件引用·未上传:docs___Findings_v2.0_bigquiz.md〕` |
| 180 | `58bb0a7d2e46` | 3175 | 归档区 | `corpus/v20/S2_n45.json` | `〔归档件引用·未上传:corpus___v20___S2_n45.json〕` |
| 181 | `52b4d6e52ae9` | 3171 | 归档区 | `corpus/v20/S1_n45.json` | `〔归档件引用·未上传:corpus___v20___S1_n45.json〕` |
| 182 | `82eb64151f2b` | 3112 | 归档区 | `results/deposon_benchmark_v1_3_traps.json` | `〔归档件引用·未上传:results___deposon_benchmark_v1_3_traps.json〕` |
| 183 | `55428f6bd848` | 3041 | 归档区 | `results/deposon_g1_mindmap_demo.json` | `〔归档件引用·未上传:results___deposon_g1_mindmap_demo.json〕` |
| 184 | `9b16fa802ef8` | 2864 | 归档区 | `results/deposon_v20_gt8c.json` | `〔归档件引用·未上传:results___deposon_v20_gt8c.json〕` |
| 185 | `f36667e5b5b8` | 2782 | 归档区 | `results/deposon_g2_boltzmann_pathintegral_rewrite.json` | `〔归档件引用·未上传:results___deposon_g2_boltzmann_pathintegral_rewrite.json〕` |
| 186 | `5cd6269d7baf` | 2741 | 归档区 | `results/deposon_benchmark_v1_4_gsm8k.json` | `〔归档件引用·未上传:results___deposon_benchmark_v1_4_gsm8k.json〕` |
| 187 | `6339ea4e500c` | 2706 | 归档区 | `results/deposon_v20_gt8b.json` | `〔归档件引用·未上传:results___deposon_v20_gt8b.json〕` |
| 188 | `8d02fbadd277` | 2676 | 归档区 | `corpus/v20/S6_n35.json` | `〔归档件引用·未上传:corpus___v20___S6_n35.json〕` |
| 189 | `4f3242b2a661` | 2632 | 归档区 | `docs/Findings_GT3.md` | `〔归档件引用·未上传:docs___Findings_GT3.md〕` |
| 190 | `8df31c95b1fc` | 2557 | 归档区 | `corpus/v20/all.json` | `〔归档件引用·未上传:corpus___v20___all.json〕` |
| 191 | `f035043bfddd` | 2521 | 归档区 | `corpus/v20/S1_n35.json` | `〔归档件引用·未上传:corpus___v20___S1_n35.json〕` |
| 192 | `a18b5d0d4485` | 2495 | 归档区 | `paper/FIGURE_LANGUAGE_POLICY.md` | `〔归档件引用·未上传:paper___FIGURE_LANGUAGE_POLICY.md〕` |
| 193 | `e20a1bbeaee7` | 2480 | 归档区 | `corpus/v20/S2_n35.json` | `〔归档件引用·未上传:corpus___v20___S2_n35.json〕` |
| 194 | `43d9ce160fc8` | 2460 | 归档区 | `results/boss_pc_1_real_2d_ising_2026_09_15.json` | `〔归档件引用·未上传:results___boss_pc_1_real_2d_ising_2026_09_15.json〕` |
| 195 | `94b5398be76c` | 2364 | 归档区 | `results/boss_pc_3_real_reservoir_2026_09_15.json` | `〔归档件引用·未上传:results___boss_pc_3_real_reservoir_2026_09_15.json〕` |
| 196 | `3b6879ab2440` | 2297 | 归档区 | `corpus/v20/S3.json` | `〔归档件引用·未上传:corpus___v20___S3.json〕` |
| 197 | `9347add72401` | 2245 | 归档区 | `results/deposon_benchmark_v1_3_simple.json` | `〔归档件引用·未上传:results___deposon_benchmark_v1_3_simple.json〕` |
| 198 | `b1f6c5aa4de6` | 2234 | 归档区 | `corpus/v20/S2.json` | `〔归档件引用·未上传:corpus___v20___S2.json〕` |
| 199 | `9fd0f3399ab3` | 2204 | 归档区 | `results/deposon_g2_boltzmann_pathintegral.json` | `〔归档件引用·未上传:results___deposon_g2_boltzmann_pathintegral.json〕` |
| 200 | `59c2113b7c71` | 2059 | 归档区 | `results/_v3x_p_k_verify_2026_09_16/v3x_p_k_verify_results_2026_09_16.json` | `〔归档件引用·未上传:results____v3x_p_k_verify_2026_09_16___v3x_p_k_verify_results_2026_09_16.json〕` |
| 201 | `a4b12d1cfedc` | 2042 | 归档区 | `results/_p_m_real_separation_2026_09_16/p_m_real_separation_results_2026_09_16.json` | `〔归档件引用·未上传:results____p_m_real_separation_2026_09_16___p_m_real_separation_results_2026_09_16.json〕` |
| 202 | `2628f74421f2` | 1875 | 归档区 | `reviews/data/t2e_nettack.csv` | `〔归档件引用·未上传:reviews___data___t2e_nettack.csv〕` |
| 203 | `a1ef105b0269` | 1768 | 归档区 | `results/deposon_v20_fastcheck.json` | `〔归档件引用·未上传:results___deposon_v20_fastcheck.json〕` |
| 204 | `4a0689892c1b` | 1724 | 归档区 | `corpus/v20/S6_n20.json` | `〔归档件引用·未上传:corpus___v20___S6_n20.json〕` |
| 205 | `7474fc258375` | 1724 | 归档区 | `reviews/independent_review_20260823.md` | `〔归档件引用·未上传:reviews___independent_review_20260823.md〕` |
| 206 | `b51fd24586b3` | 1691 | 归档区 | `results/deposon_benchmark_v1_4_strategyqa.json` | `〔归档件引用·未上传:results___deposon_benchmark_v1_4_strategyqa.json〕` |
| 207 | `a9ad1de618f5` | 1669 | 归档区 | `results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json` | `〔归档件引用·未上传:results____p_j_convergence_basin_2026_09_16___p_j_convergence_basin_results_2026_09_16.json〕` |
| 208 | `553c90aa3ba6` | 1610 | 归档区 | `audits_security.json` | `〔归档件引用·未上传:audits_security.json〕` |
| 209 | `bfc9d38c8c0f` | 1537 | 归档区 | `corpus/v20/S2_n20.json` | `〔归档件引用·未上传:corpus___v20___S2_n20.json〕` |
| 210 | `a890c56f7705` | 1512 | 归档区 | `corpus/v20/S1.json` | `〔归档件引用·未上传:corpus___v20___S1.json〕` |
| 211 | `928bcfbdb7c3` | 1496 | 归档区 | `results/deposon_v22_e95ci.json` | `〔归档件引用·未上传:results___deposon_v22_e95ci.json〕` |
| 212 | `676eb83edc27` | 1303 | 归档区 | `results/deposon_v20_familyl_ingest.json` | `〔归档件引用·未上传:results___deposon_v20_familyl_ingest.json〕` |
| 213 | `f0d2c9d2a39b` | 1271 | 归档区 | `reviews/data/t2f_waniek.csv` | `〔归档件引用·未上传:reviews___data___t2f_waniek.csv〕` |
| 214 | `d74d6b39d1b0` | 1265 | 归档区 | `results/boss_pc_3_a3_clipping_2026_09_15.json` | `〔归档件引用·未上传:results___boss_pc_3_a3_clipping_2026_09_15.json〕` |
| 215 | `6a703b06f0fe` | 1085 | 归档区 | `LICENSE` | `〔归档件引用·未上传:LICENSE〕` |
| 216 | `e934819ee9ed` | 1043 | 归档区 | `results/_p_i_real_labels_2026_09_16/p_i_real_labels_results_2026_09_16.json` | `〔归档件引用·未上传:results____p_i_real_labels_2026_09_16___p_i_real_labels_results_2026_09_16.json〕` |
| 217 | `5a880678c386` | 1024 | 归档区 | `results/boss_pc_2_a2_fitting_2026_09_15.json` | `〔归档件引用·未上传:results___boss_pc_2_a2_fitting_2026_09_15.json〕` |
| 218 | `4b11b1bd8ada` | 1018 | 归档区 | `results/deposon_v20_gt8c_ingest.json` | `〔归档件引用·未上传:results___deposon_v20_gt8c_ingest.json〕` |
| 219 | `d21912a05d79` | 1017 | 归档区 | `results/boss_pc_1_a1_resampling_2026_09_15.json` | `〔归档件引用·未上传:results___boss_pc_1_a1_resampling_2026_09_15.json〕` |
| 220 | `aa077cc1725e` | 986 | 归档区 | `results/deposon_v20_gt8b_ingest.json` | `〔归档件引用·未上传:results___deposon_v20_gt8b_ingest.json〕` |
| 221 | `b9b65c568842` | 915 | 归档区 | `results/deposon_v20_vector_audit.json` | `〔归档件引用·未上传:results___deposon_v20_vector_audit.json〕` |
| 222 | `2bed4de3a57c` | 763 | 归档区 | `results/deposon_v22_p1c.json` | `〔归档件引用·未上传:results___deposon_v22_p1c.json〕` |
| 223 | `ab3045b2c6d9` | 27 | 归档区 | `requirements.txt` | `〔归档件引用·未上传:requirements.txt〕` |
| 224 | `5741ac6af12a` | 1137664 | sub | `results/.tmp/_s14_session_scan_out_2026_10_21.md` | `〔幽灵引用·未上传:results___.tmp____s14_session_scan_out_2026_10_21.md〕` |
| 225 | `dd49e6612dbe` | 480977 | sub | `results/.tmp/_s14_anchorchain_2026_10_21.md` | `〔幽灵引用·未上传:results___.tmp____s14_anchorchain_2026_10_21.md〕` |
| 226 | `2e523f11e8c2` | 419151 | sub | `results/.tmp/_audit_s13_conv_out_2026_10_20.txt` | `〔幽灵引用·未上传:results___.tmp____audit_s13_conv_out_2026_10_20.txt〕` |
| 227 | `2faed7996933` | 177579 | sub | `results/.tmp/_s14_main_events2_2026_10_21.md` | `〔幽灵引用·未上传:results___.tmp____s14_main_events2_2026_10_21.md〕` |
| 228 | `71e52e6aa470` | 153751 | sub | `results/.tmp/_s14_cards_full_2026_10_21.md` | `〔幽灵引用·未上传:results___.tmp____s14_cards_full_2026_10_21.md〕` |
| 229 | `4b10cb45fd44` | 96411 | sub | `results/.tmp/_s14_main_session_slice_2026_10_21.md` | `〔幽灵引用·未上传:results___.tmp____s14_main_session_slice_2026_10_21.md〕` |
| 230 | `c285e696fce1` | 83701 | sub | `results/.tmp/_audit_s12_heads_out_2026_10_19.txt` | `〔幽灵引用·未上传:results___.tmp____audit_s12_heads_out_2026_10_19.txt〕` |
| 231 | `11af4e96c034` | 77994 | sub | `results/.tmp/_s16_body_2026_10_21.md` | `〔幽灵引用·未上传:results___.tmp____s16_body_2026_10_21.md〕` |
| 232 | `258115c22f32` | 55575 | sub | `results/.tmp/_s15_body_2026_10_21.md` | `〔幽灵引用·未上传:results___.tmp____s15_body_2026_10_21.md〕` |
| 233 | `758ad1bac2e6` | 51542 | sub | `results/.tmp/_s13_body_2026_10_20.md` | `〔幽灵引用·未上传:results___.tmp____s13_body_2026_10_20.md〕` |
| 234 | `8f184f097720` | 42088 | sub | `results/.tmp/_s14_disk_scan_out_t2.md` | `〔幽灵引用·未上传:results___.tmp____s14_disk_scan_out_t2.md〕` |
| 235 | `53fadc8fc515` | 40930 | sub | `results/.tmp/_s14_instrument_out_2026_10_21.md` | `〔幽灵引用·未上传:results___.tmp____s14_instrument_out_2026_10_21.md〕` |
| 236 | `ebea307102a1` | 40199 | sub | `results/.tmp/_s12_body_2026_10_19.md` | `〔幽灵引用·未上传:results___.tmp____s12_body_2026_10_19.md〕` |
| 237 | `4893e543556f` | 38541 | sub | `results/.tmp/_s14_body_2026_10_21.md` | `〔幽灵引用·未上传:results___.tmp____s14_body_2026_10_21.md〕` |
| 238 | `cd3435aecb60` | 26640 | sub | `results/.tmp/_s14_anchorchain2_2026_10_21.md` | `〔幽灵引用·未上传:results___.tmp____s14_anchorchain2_2026_10_21.md〕` |
| 239 | `5c4f0d43ada4` | 25045 | sub | `results/.tmp/_s14_final_measure_2026_10_21.md` | `〔幽灵引用·未上传:results___.tmp____s14_final_measure_2026_10_21.md〕` |
| 240 | `f3b199fa0deb` | 19178 | sub | `results/.tmp/_audit_s13_final_out_2026_10_20.txt` | `〔幽灵引用·未上传:results___.tmp____audit_s13_final_out_2026_10_20.txt〕` |
| 241 | `9063b4326cec` | 13754 | sub | `results/.tmp/_audit_s13_anchors_out_2026_10_20.txt` | `〔幽灵引用·未上传:results___.tmp____audit_s13_anchors_out_2026_10_20.txt〕` |
| 242 | `c53201f4bae4` | 12829 | sub | `results/.tmp/_audit_s12_refined_2026_10_19.py` | `〔幽灵引用·未上传:results___.tmp____audit_s12_refined_2026_10_19.py〕` |
| 243 | `eeb9f79522b0` | 12723 | sub | `results/.tmp/_audit_s13_anchors_2026_10_20.py` | `〔幽灵引用·未上传:results___.tmp____audit_s13_anchors_2026_10_20.py〕` |
| 244 | `b925b0c48d58` | 9441 | sub | `results/.tmp/_s16_append_2026_10_21.md` | `〔幽灵引用·未上传:results___.tmp____s16_append_2026_10_21.md〕` |
| 245 | `036b4a749f95` | 8898 | sub | `results/.tmp/_audit_s13_final_2026_10_20.py` | `〔幽灵引用·未上传:results___.tmp____audit_s13_final_2026_10_20.py〕` |
| 246 | `16ee96876c4a` | 8779 | sub | `results/.tmp/_audit_s12_refined_out_2026_10_19.txt` | `〔幽灵引用·未上传:results___.tmp____audit_s12_refined_out_2026_10_19.txt〕` |
| 247 | `4402eb22f4ad` | 8769 | sub | `results/.tmp/_s14_append_2026_10_21.py` | `〔幽灵引用·未上传:results___.tmp____s14_append_2026_10_21.py〕` |
| 248 | `6a2dc54827b7` | 8367 | sub | `results/.tmp/_audit_s12_keyscan_2026_10_19.py` | `〔幽灵引用·未上传:results___.tmp____audit_s12_keyscan_2026_10_19.py〕` |
| 249 | `6c9463882c9f` | 7115 | sub | `results/.tmp/_s14_anchor2_2026_10_21.py` | `〔幽灵引用·未上传:results___.tmp____s14_anchor2_2026_10_21.py〕` |
| 250 | `aa7fa6ff4255` | 6950 | sub | `results/.tmp/_audit_s12_keyscan_out_2026_10_19.txt` | `〔幽灵引用·未上传:results___.tmp____audit_s12_keyscan_out_2026_10_19.txt〕` |
| 251 | `e0dc2e74ff62` | 5872 | sub | `results/.tmp/_s14_final_measure_2026_10_21.py` | `〔幽灵引用·未上传:results___.tmp____s14_final_measure_2026_10_21.py〕` |
| 252 | `5a74e4bdea89` | 4975 | sub | `results/.tmp/_s13_7_body_2026_10_20.md` | `〔幽灵引用·未上传:results___.tmp____s13_7_body_2026_10_20.md〕` |
| 253 | `8c8b9d995f05` | 4924 | sub | `results/.tmp/_audit_s13_scan_2026_10_20.py` | `〔幽灵引用·未上传:results___.tmp____audit_s13_scan_2026_10_20.py〕` |
| 254 | `e80e4fe4aa0f` | 4754 | sub | `results/.tmp/_s12_7_body_2026_10_19.md` | `〔幽灵引用·未上传:results___.tmp____s12_7_body_2026_10_19.md〕` |
| 255 | `6eb1a23daf22` | 4550 | sub | `results/.tmp/_s14_instrument_2026_10_21.py` | `〔幽灵引用·未上传:results___.tmp____s14_instrument_2026_10_21.py〕` |
| 256 | `de8d0b8a76b0` | 4313 | sub | `results/.tmp/_s14_disk_scan_out_t1.md` | `〔幽灵引用·未上传:results___.tmp____s14_disk_scan_out_t1.md〕` |
| 257 | `d80719c6d092` | 4247 | sub | `results/.tmp/_s14_anchorchain_2026_10_21.py` | `〔幽灵引用·未上传:results___.tmp____s14_anchorchain_2026_10_21.py〕` |
| 258 | `e93a45e23469` | 4080 | sub | `results/.tmp/_s14_session_scan2_2026_10_21.py` | `〔幽灵引用·未上传:results___.tmp____s14_session_scan2_2026_10_21.py〕` |
| 259 | `a4cc5099940c` | 3618 | sub | `results/.tmp/_s14_session_scan_2026_10_21.py` | `〔幽灵引用·未上传:results___.tmp____s14_session_scan_2026_10_21.py〕` |
| 260 | `b4a1c8d6a3d9` | 3520 | sub | `results/.tmp/_audit_s13_append_2026_10_20.py` | `〔幽灵引用·未上传:results___.tmp____audit_s13_append_2026_10_20.py〕` |
| 261 | `e3aca88d382f` | 3116 | sub | `results/.tmp/_audit_s12_append_2026_10_19.py` | `〔幽灵引用·未上传:results___.tmp____audit_s12_append_2026_10_19.py〕` |
| 262 | `b4f7569705a8` | 3057 | sub | `results/.tmp/_audit_s12_keyclass_2026_10_19.py` | `〔幽灵引用·未上传:results___.tmp____audit_s12_keyclass_2026_10_19.py〕` |
| 263 | `854019e4b7d3` | 2982 | sub | `results/.tmp/_s14_disk_scan_2026_10_21.py` | `〔幽灵引用·未上传:results___.tmp____s14_disk_scan_2026_10_21.py〕` |
| 264 | `31bcc0f213c0` | 2958 | sub | `results/.tmp/_s14_msgdist_2026_10_21.py` | `〔幽灵引用·未上传:results___.tmp____s14_msgdist_2026_10_21.py〕` |
| 265 | `faa86d3f25bc` | 2814 | sub | `results/.tmp/_audit_s12_heads_2026_10_19.py` | `〔幽灵引用·未上传:results___.tmp____audit_s12_heads_2026_10_19.py〕` |
| 266 | `e19a994d3f9b` | 2767 | sub | `results/.tmp/_audit_s12_scan_2026_10_19.py` | `〔幽灵引用·未上传:results___.tmp____audit_s12_scan_2026_10_19.py〕` |
| 267 | `ffc34fee17b2` | 2739 | sub | `results/.tmp/_audit_final_2026_10_19.py` | `〔幽灵引用·未上传:results___.tmp____audit_final_2026_10_19.py〕` |
| 268 | `0c75fb83c89d` | 2668 | sub | `results/.tmp/_s14_events2_2026_10_21.py` | `〔幽灵引用·未上传:results___.tmp____s14_events2_2026_10_21.py〕` |
| 269 | `8161b1da2340` | 2459 | sub | `results/.tmp/_s15_append_2026_10_21.md` | `〔幽灵引用·未上传:results___.tmp____s15_append_2026_10_21.md〕` |
| 270 | `953abd8121f7` | 2395 | sub | `results/.tmp/_audit_s13_7_append_2026_10_20.py` | `〔幽灵引用·未上传:results___.tmp____audit_s13_7_append_2026_10_20.py〕` |
| 271 | `dc3a10abbc2b` | 1792 | sub | `results/.tmp/_audit_s13_main_heads_2026_10_20.txt` | `〔幽灵引用·未上传:results___.tmp____audit_s13_main_heads_2026_10_20.txt〕` |
| 272 | `0f95bd681cf6` | 1587 | sub | `results/.tmp/_s14_cards_full_2026_10_21.py` | `〔幽灵引用·未上传:results___.tmp____s14_cards_full_2026_10_21.py〕` |
| 273 | `67d8df4dcc34` | 1505 | sub | `results/.tmp/_s14_append_report_2026_10_21.md` | `〔幽灵引用·未上传:results___.tmp____s14_append_report_2026_10_21.md〕` |
| 274 | `21d7e6e9fdbc` | 1385 | sub | `results/.tmp/_audit_s12_keyclass_2026_10_19.txt` | `〔幽灵引用·未上传:results___.tmp____audit_s12_keyclass_2026_10_19.txt〕` |
| 275 | `107a9ed5090a` | 880 | sub | `results/.tmp/_audit_bom_cr_2026_10_19.py` | `〔幽灵引用·未上传:results___.tmp____audit_bom_cr_2026_10_19.py〕` |
| 276 | `893914b4ef10` | 704 | sub | `results/.tmp/_audit_tail_2026_10_19.py` | `〔幽灵引用·未上传:results___.tmp____audit_tail_2026_10_19.py〕` |
| 277 | `6b0da8b7ce9b` | 675 | sub | `results/.tmp/_s14_msgdist_2026_10_21.md` | `〔幽灵引用·未上传:results___.tmp____s14_msgdist_2026_10_21.md〕` |
| 278 | `67bcc0955f22` | 611 | sub | `results/.tmp/_audit_s13_main_heads_2026_10_20.py` | `〔幽灵引用·未上传:results___.tmp____audit_s13_main_heads_2026_10_20.py〕` |
| 279 | `1e5b4e17e616` | 289 | sub | `results/.tmp/_s14_main_events_2026_10_21.md` | `〔幽灵引用·未上传:results___.tmp____s14_main_events_2026_10_21.md〕` |

## §2 与「339 行」之关系

原拟之「339 行」＝ **283 件可移（227 归档／56 sub）＋ 56 件垃圾候选**。其中：

| 项 | 件数 | 现状 |
|:--|--:|:--|
| 垃圾候选 | 56 | **26 件已经 PI 16:52 裁、已于 17:0x 可恢复删除**；余 **30 件按裁保留**（含 `.gitignore`／`LICENSE`／镜像与拉回副本）⇒ **不入本表** |
| 可移件（归档区） | 227 | 本表 **223** 行（缺 3 件：已因去重复而删） |
| 可移件（sub） | 56 | 本表 **56** 行（缺 1 件：已因去重复而删） |
| **本表合计** | — | **279** |

## §3 老实交代

1. **本表非 339 行**：339 系「可移 283 ＋ 垃圾 56」之合；垃圾 56 之去留已由裁三与 16:52 之裁处理，**不属移动面**。⛔ 0 以本表充 339。
2. **4 件源缺**：`corpus/v20_caption_surface/strip_captions_22.json`、`results/boss_pe_1_real_2d_ising_2026_09_15.json`、`_boss_pe_2_real_transverse_ising_2026_09_15.json`、`_boss_pe_3_real_reservoir_2026_09_15.json`——皆系**裁三一次全批所删之重复件**。其「移」已由「删」达成（件数净减同效），**如实登记**。
3. **禁令面命中 1 件**：`audits_dataset_health.json`（加严② dataset 族）。其**移入归档区恰为移出上传面**，与禁令**同向**，故纳入移动。
4. **移动即改路径** ⇒ 其原有之路径式引用将落空；本表「旧→新」两栏即**幽灵登记之载荷**。

*件止。主代理 mavis 亲撰 · 2026-10-22 20:5x · 0 移动（本表为凭据，执行另办）。*

---

## §4 执行回执（本代理亲办 · 2026-10-22 21:0x）

| 项 | 值 |
|:--|:--|
| 计划行数 | **279**（223 归档区／56 sub） |
| **实际移动** | **279**（**0 失败**） |
| 归档区容器 | `〔归档区〕\_movedout_2026_10_22\` → **223 件** ✅ |
| sub 容器 | `deposon-sub\_movedin_2026_10_22\` → **56 件** ✅ |
| **逐件完整性** | 移前 ／ 移后 **各算 SHA-256**，**279／279 全等**（0 变化） ✅ |
| **源侧残留** | **0 件** ✅ |
| **目标缺失** | **0 件** ✅ |
| 通道 | 文件**移动**（非删除）；⛔ 0 删除任何件 |

### §4-1 移动后之件数

| 区 | 件数 |
|:--|--:|
| `deposon-repo`（去根 `.tmp`） | **−223**（自 2,626 降至 2,403 量级；以实测为准） |
| `deposon-sub` | **1,219 → 1,275**（＋56，含新容器） |
| 归档区 | **＋223**（新容器 `_movedout_2026_10_22`） |

⇒ **sub 与 repo 之件数差自 1,453 缩至约 1,128**（沿 PI「repo 与 sub 件数差不多」之方向，尚未齐平）。

### §4-2 老实交代

1. **本表之「新路径」已全部落地**：§1 之 279 行「新路径」栏即**现值**，可据以查址。
2. **幽灵面**：279 件之原路径现已失效 ⇒ **凡以路径式引用彼等者，皆已成幽灵**。本表「旧→新」两栏即**登记载荷**；⛔ 0 声称已逐处改指（活引用面未测）。
3. **建目录 2 个**：`_movedout_2026_10_22`（归档区）／`_movedin_2026_10_22`（sub）——依裁四之移动授权所必需，沿既有 `_movedout_*` 惯例命名。
4. **4 件未移**：已因裁三去重复先删，见 §3-2。
5. **⛔ 0 回改**本表 §1 之任何行；执行面以本 §4 为准。

---

*补录止。主代理 mavis 亲撰 · 2026-10-22 21:0x · PURE-APPEND。*
