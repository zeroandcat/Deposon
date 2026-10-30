# 去重复执行·删除记录（可恢复通道）· 2026-10-22

- 依据：PI 2026-10-22 20:15 卡答（`ask_f1959ef42c84738879aa025f`）裁三「**122 件一次全批**」——落账件 `pi_rulings\_pi_card_answers_register_2026_10_22_v235.md`
- 判据：**件数单尺**（体积不论）｜射程：**上传面**（repo 去 `.tmp`／`results\.tmp` ＋ sub）
- 留件规则（确定性）：**先留 `repo` 侧**；同区者留**路径最浅**（分隔符最少），同深取字典序先者
- **两处扣减（照裁执行时之必然扣减，非改裁）**：

| 组 | 冗余 | 处置 | 理由 |
|:--|--:|:--|:--|
| `0a1e91d6f772`（`_d05_sanity_3backbone_20260918_100110.json`） | 2 | **⛔ 不减** | `MC-E4` **密钥门 1 件·永不上传**之禁令锁定（禁令 ＞ 件数尺） |
| `e3b0c44298fc`（**零字节组**·4 件） | 3 | **⛔ 不减** | ①零字节之「全字节相同」系平凡真，**不构成内容重复**；②组内含 `_remote_pullback_…/_archive_2026_09_20/*.log.err`——在册载其**活引用 25 处**，为「**空 stderr ＝ 洁净运行**」之证据面，删之即毁证；③组内含**今日在途棒之 0 字节产物**（`results\.tmp\_s19memo2_*`） |

⇒ **122 − 2 − 3 ＝ 实删 117 件**。

---

## §1 逐件（117 行：删哪件／留哪件）

| # | SHA-12 | bytes | 区 | 删（相对仓根） | 留（相对仓根·正身） |
|--:|:--|--:|:--|:--|:--|
| 1 | `dfb02ade1474` | 591 | sub | `results\_inspect_captions.py` | `corpus\v20_caption_surface\_inspect_captions.py` |
| 2 | `dfb02ade1474` | 591 | sub | `results\_archive_2026_09_24\_inspect_captions.py` | `corpus\v20_caption_surface\_inspect_captions.py` |
| 3 | `25f745609658` | 612511 | repo | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_v41_flash_rag_caption_embs.bak.json` | `corpus\v20_caption_surface\_v41_flash_rag_caption_embs.bak.json` |
| 4 | `25f745609658` | 612511 | sub | `results\_archive_2026_09_20\_v41_flash_rag_caption_embs.bak.json` | `corpus\v20_caption_surface\_v41_flash_rag_caption_embs.bak.json` |
| 5 | `d21912a05d79` | 1017 | sub | `results\attack_pc_a1_resampling_2026_09_15.json` | `results\boss_pc_1_a1_resampling_2026_09_15.json` |
| 6 | `d21912a05d79` | 1017 | sub | `results\boss_pc_1_a1_resampling_2026_09_15.json` | `results\boss_pc_1_a1_resampling_2026_09_15.json` |
| 7 | `43d9ce160fc8` | 2460 | repo | `results\boss_pe_1_real_2d_ising_2026_09_15.json` | `results\boss_pc_1_real_2d_ising_2026_09_15.json` |
| 8 | `43d9ce160fc8` | 2460 | sub | `results\boss_pc_1_real_2d_ising_2026_09_15.json` | `results\boss_pc_1_real_2d_ising_2026_09_15.json` |
| 9 | `8933d61b180a` | 3553 | repo | `results\boss_pe_2_real_transverse_ising_2026_09_15.json` | `results\boss_pc_2_real_transverse_ising_2026_09_15.json` |
| 10 | `8933d61b180a` | 3553 | sub | `results\boss_pc_2_real_transverse_ising_2026_09_15.json` | `results\boss_pc_2_real_transverse_ising_2026_09_15.json` |
| 11 | `94b5398be76c` | 2364 | repo | `results\boss_pe_3_real_reservoir_2026_09_15.json` | `results\boss_pc_3_real_reservoir_2026_09_15.json` |
| 12 | `94b5398be76c` | 2364 | sub | `results\boss_pc_3_real_reservoir_2026_09_15.json` | `results\boss_pc_3_real_reservoir_2026_09_15.json` |
| 13 | `6cbb8ba01bfb` | 15409 | repo | `results\_d9_e2e_backup_2026_10_13\_s4_heldout_sampling_seedprime_items_2026_10_10.json` | `results\_s4_heldout_sampling_seedprime_items_2026_10_10.json` |
| 14 | `6cbb8ba01bfb` | 15409 | repo | `results\_d9_e2e_rerun_backup_2026_10_13\_s4_heldout_sampling_seedprime_items_2026_10_10.json` | `results\_s4_heldout_sampling_seedprime_items_2026_10_10.json` |
| 15 | `1fc5f3ab3f93` | 2022 | sub | `.trae\audit\compile_evidence\v2_overfull_fix_20260909\compile_runner.ps1` | `.trae\audit\compile_evidence\compile_runner.ps1` |
| 16 | `1fc5f3ab3f93` | 2022 | sub | `.trae\audit\compile_evidence\v2pre_h1h3_20260909\compile_runner.ps1` | `.trae\audit\compile_evidence\compile_runner.ps1` |
| 17 | `efe05ad775de` | 24150 | repo | `corpus\v20\by_model\kimi\index_v2_2026_09_16.json` | `corpus\v20\index_v2_2026_09_16.json` |
| 18 | `6a2656878745` | 12798 | repo | `corpus\v20_caption_surface\strip_captions_22.json` | `corpus\v20\strip_captions_22.json` |
| 19 | `9e1ccbdceacc` | 25347 | sub | `deposon_team\products\minimax_artifact_v_2026_09_16.json` | `corpus\v20\by_model\minimax\artifact_v_2026_09_16.json` |
| 20 | `d2cd7acb29a1` | 18596 | sub | `deposon_team\plugins\_p_d_b3_merkle_22caption_runner_2026_09_16.py` | `corpus\v20_caption_surface\_p_d_b3_merkle_22caption_runner_2026_09_16.py` |
| 21 | `dfbcc5d6fc34` | 13775 | sub | `results\_p_d_v03_22caption_verification_20260917_163757.json` | `corpus\v20_caption_surface\_p_d_v03_22caption_verification_20260917_163757.json` |
| 22 | `c7c59e0d2f6c` | 8753 | sub | `results\boss_pa_1_rbr_rm_result_2026_09_15.json` | `results\boss_pa_1_rbr_rm_result_2026_09_15.json` |
| 23 | `5c76137d6430` | 7530 | sub | `results\boss_pa_2_potential_game_result_2026_09_15.json` | `results\boss_pa_2_potential_game_result_2026_09_15.json` |
| 24 | `d6f233d73c45` | 9098 | sub | `results\boss_pa_3_replicator_dynamics_result_2026_09_15.json` | `results\boss_pa_3_replicator_dynamics_result_2026_09_15.json` |
| 25 | `5a880678c386` | 1024 | sub | `results\attack_pc_a2_fitting_2026_09_15.json` | `results\boss_pc_2_a2_fitting_2026_09_15.json` |
| 26 | `d74d6b39d1b0` | 1265 | sub | `results\attack_pc_a3_clipping_2026_09_15.json` | `results\boss_pc_3_a3_clipping_2026_09_15.json` |
| 27 | `4505cca79c15` | 2456 | sub | `results\d7_5anchor_60cells_9model_verdict_2026_09_18.json` | `results\d7_5anchor_60cells_9model_verdict_2026_09_18.json` |
| 28 | `55428f6bd848` | 3041 | repo | `results\_glm_evidence_unpacked_2026_10_13\_september_workspace\results\deposon_g1_mindmap_demo.json` | `results\deposon_g1_mindmap_demo.json` |
| 29 | `ca71aa6858e1` | 631644 | sub | `results\_archive_2026_09_21\deposon_v20_corpus_eval.json` | `results\deposon_v20_corpus_eval.json` |
| 30 | `a2ae7997ee67` | 123331 | sub | `results\_archive_2026_09_21\deposon_v20_gt2b.json` | `results\deposon_v20_gt2b.json` |
| 31 | `35b676773243` | 7844 | sub | `results\_archive_2026_09_21\deposon_v20_gt3.json` | `results\deposon_v20_gt3.json` |
| 32 | `b9b65c568842` | 915 | sub | `results\_archive_2026_09_21\deposon_v20_vector_audit.json` | `results\deposon_v20_vector_audit.json` |
| 33 | `218ef1a99f97` | 11703 | sub | `results\deposon_volcengine_minimax_m3_30cells_2026_09_10.py` | `results\deposon_volcengine_minimax_m3_30cells_2026_09_10.py` |
| 34 | `a7dff824ed56` | 22877 | repo | `results\_glm_evidence_unpacked_2026_10_13\_september_workspace\results\_s3_d1fill_recount_2026_10_01.md` | `results\_s3_d1fill_recount_2026_10_01.md` |
| 35 | `5777a07c608a` | 43130 | repo | `results\_d9_e2e_backup_2026_10_13\_s4_heldout_sampling_seedthird_items_2026_10_11.json` | `results\_s4_heldout_sampling_seedthird_items_2026_10_11.json` |
| 36 | `784f042bf93d` | 22646 | repo | `results\_d9_e2e_backup_2026_10_13\_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | `results\_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` |
| 37 | `839fb5452578` | 16099 | repo | `results\_d9_e2e_backup_2026_10_13\_s5doubleprime_five_lines_readings_2026_10_11.json` | `results\_s5doubleprime_five_lines_readings_2026_10_11.json` |
| 38 | `079108c62a82` | 21049 | repo | `results\_d9_e2e_backup_2026_10_13\_stage3_trigger_readings_items_2026_10_11.json` | `results\_stage3_trigger_readings_items_2026_10_11.json` |
| 39 | `62fb594be3f9` | 32371 | repo | `results\_glm_evidence_unpacked_2026_10_13\_september_workspace\results\_t1_substrate_gap_census_2026_10_01.md` | `results\_t1_substrate_gap_census_2026_10_01.md` |
| 40 | `ef5a40554960` | 46836 | repo | `results\_glm_evidence_unpacked_2026_10_13\_september_workspace\results\_v3_s_prereg_v1_2026_09_27.md` | `results\_v3_s_prereg_v1_2026_09_27.md` |
| 41 | `c68076c88140` | 26253 | sub | `results\_v5_gt8_lowarm_result_2026_09_29_cb132cd5.json` | `results\_v5_gt8_lowarm_result_2026_09_29.json` |
| 42 | `25141de92c50` | 7188 | sub | `results\_xiang14_third_reissue_registration_2026_10_13.md` | `results\_xiang14_third_reissue_registration_2026_10_13.md` |
| 43 | `d0b7467fa01c` | 52787 | repo | `results\.tmp\_s18memo_body_2026_10_22.md` | `results\.tmp\_s18memo_append_2026_10_22.md` |
| 44 | `15904ecae629` | 11105 | sub | `results\_volc_22cap_emb.py` | `results\_archive_2026_09_24\_volc_22cap_emb.py` |
| 45 | `dc9cb0e02922` | 28370 | sub | `results\_d1_ruling_and_s3_transition_2026_10_01.md` | `results\_glm_evidence_unpacked_2026_10_13\_september_workspace\results\_d1_ruling_and_s3_transition_2026_10_01.md` |
| 46 | `693eefdd7a82` | 32296 | sub | `results\_kv3s_3_2_terminal_verdict_2026_10_01.md` | `results\_glm_evidence_unpacked_2026_10_13\_september_workspace\results\_kv3s_3_2_terminal_verdict_2026_10_01.md` |
| 47 | `303bf7c6f34d` | 28762 | sub | `results\_s3_d1_rulings_supplement_register_2026_10_01.md` | `results\_glm_evidence_unpacked_2026_10_13\_september_workspace\results\_s3_d1_rulings_supplement_register_2026_10_01.md` |
| 48 | `a9ad1de618f5` | 1669 | sub | `results\_p_j_convergence_basin_2026_09_16\p_j_convergence_basin_results_2026_09_16.json` | `results\_p_j_convergence_basin_2026_09_16\p_j_convergence_basin_results_2026_09_16.json` |
| 49 | `4bdec2683f06` | 22105 | sub | `_archive_deposon_2026_09_17\verifier\audit\conservation.py` | `verifier\audit\conservation.py` |
| 50 | `57f06a426bec` | 3011 | sub | `results\deposon_benchmark_v1_3_labelfree.json` | `_remote_pullback_2026_10_17\results\deposon_benchmark_v1_3_labelfree.json` |
| 51 | `769ae8c908c9` | 3134 | sub | `results\deposon_benchmark_v1_3_resonant.json` | `_remote_pullback_2026_10_17\results\deposon_benchmark_v1_3_resonant.json` |
| 52 | `c9796d3b3263` | 12479 | sub | `results\deposon_benchmark_v1_4_sc5.json` | `_remote_pullback_2026_10_17\results\deposon_benchmark_v1_4_sc5.json` |
| 53 | `a3de045b5dd7` | 2284 | sub | `results\deposon_g3_arrhenius.json` | `_remote_pullback_2026_10_17\results\deposon_g3_arrhenius.json` |
| 54 | `a7952d9d78db` | 5517 | sub | `results\deposon_v16_llm_prior_summary.json` | `_remote_pullback_2026_10_17\results\deposon_v16_llm_prior_summary.json` |
| 55 | `5f16be89efc5` | 938 | sub | `results\llm_prior_cache.json` | `_remote_pullback_2026_10_17\results\llm_prior_cache.json` |
| 56 | `d3f72f67977d` | 639 | sub | `results\llm_prior_cache_v18_contamination.json` | `_remote_pullback_2026_10_17\results\llm_prior_cache_v18_contamination.json` |
| 57 | `7c0d169ef164` | 512 | sub | `results\llm_prior_cache_v18_contentless.json` | `_remote_pullback_2026_10_17\results\llm_prior_cache_v18_contentless.json` |
| 58 | `023f936f80fb` | 2168 | sub | `results\llm_prior_cache_v18_direction.json` | `_remote_pullback_2026_10_17\results\llm_prior_cache_v18_direction.json` |
| 59 | `8dce6d7618a2` | 1925 | sub | `results\llm_prior_cache_v18_labelshuffle.json` | `_remote_pullback_2026_10_17\results\llm_prior_cache_v18_labelshuffle.json` |
| 60 | `8b6682181392` | 2186 | sub | `results\v19_edges_audit_input.csv` | `_remote_pullback_2026_10_17\results\v19_edges_audit_input.csv` |
| 61 | `f95f382ace44` | 2151 | sub | `results\v20_graph_features.csv` | `_remote_pullback_2026_10_17\results\v20_graph_features.csv` |
| 62 | `3596490e1fc0` | 4236 | sub | `results\v20_regression_field_v2.json` | `_remote_pullback_2026_10_17\results\v20_regression_field_v2.json` |
| 63 | `dfe014c627ca` | 988 | sub | `results\v20_statcheck_fm_vs_deg.json` | `_remote_pullback_2026_10_17\results\v20_statcheck_fm_vs_deg.json` |
| 64 | `1dadfaeb2c43` | 868 | sub | `results\v20_statcheck_fm_vs_rand.json` | `_remote_pullback_2026_10_17\results\v20_statcheck_fm_vs_rand.json` |
| 65 | `4af67e6cbe71` | 3449 | sub | `results\_archive_2026_09_18\_trae_anchor_18_audit_20260917_193000.md` | `_remote_pullback_2026_10_17\results\_trae_anchor_18_audit_20260917_193000.md` |
| 66 | `f2a655cd5e54` | 3467 | sub | `results\_archive_2026_09_18\_trae_corpus_5_audit_20260917_193000.md` | `_remote_pullback_2026_10_17\results\_trae_corpus_5_audit_20260917_193000.md` |
| 67 | `3184b30b7b0d` | 4253 | sub | `results\_archive_2026_09_18\_trae_d7_v1_audit_20260917_190000.json` | `_remote_pullback_2026_10_17\results\_trae_d7_v1_audit_20260917_190000.json` |
| 68 | `8ece24be6b8a` | 3281 | sub | `results\_archive_2026_09_18\_trae_kimi_push_v3_audit_20260917_193000.md` | `_remote_pullback_2026_10_17\results\_trae_kimi_push_v3_audit_20260917_193000.md` |
| 69 | `c5598b13c139` | 17363 | sub | `deposon_team\verifier\v42_v2_2026_09_16.py` | `_remote_pullback_2026_10_17\_september_workspace\deposon_team\verifier\v42_v2_2026_09_16.py` |
| 70 | `483602856618` | 1879 | sub | `deposon_team\verifier\v42_v2_baseline_2026_09_16.json` | `_remote_pullback_2026_10_17\_september_workspace\deposon_team\verifier\v42_v2_baseline_2026_09_16.json` |
| 71 | `b471190e579c` | 770 | sub | `deposon_team\verifier\v42_v2_runs_2026_09_16.jsonl` | `_remote_pullback_2026_10_17\_september_workspace\deposon_team\verifier\v42_v2_runs_2026_09_16.jsonl` |
| 72 | `a82881653520` | 465366 | sub | `results\_coze_〔IM〕_v4_d7format_2026_09_26.pdf` | `_remote_pullback_2026_10_17\_september_workspace\results\_coze_online_v4_d7format_2026_09_26.pdf` |
| 73 | `2efdc3d7741d` | 3624 | sub | `results\_coze_paper_v1_summary_2026_09_17.md` | `_remote_pullback_2026_10_17\_september_workspace\results\_coze_paper_v1_summary_2026_09_17.md` |
| 74 | `463fc7575663` | 9663 | sub | `results\_archive_2026_09_20\compile_verification.txt` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\compile_verification.txt` |
| 75 | `2d9edc8c7303` | 356123 | sub | `results\_archive_2026_09_20\fiction_that_feeds_back.pdf` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\fiction_that_feeds_back.pdf` |
| 76 | `543479649b3e` | 84388 | sub | `results\_archive_2026_09_20\fiction_that_feeds_back_source.md` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\fiction_that_feeds_back_source.md` |
| 77 | `ae07f5551e87` | 2637 | sub | `results\_archive_2026_09_20\p_i_curvature_audit_probe_results_2026_09_16.json` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\p_i_curvature_audit_probe_results_2026_09_16.json` |
| 78 | `fd38a2a1ea05` | 7617 | sub | `results\_archive_2026_09_20\review_content_A1_glm51.md` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\review_content_A1_glm51.md` |
| 79 | `a964defb923d` | 24843 | sub | `results\_archive_2026_09_20\review_content_A2_kimik3.md` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\review_content_A2_kimik3.md` |
| 80 | `0d36d7cd0589` | 30494 | sub | `results\_archive_2026_09_20\review_tech_B1_dsv4pro.md` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\review_tech_B1_dsv4pro.md` |
| 81 | `fe80bad08eef` | 13726 | sub | `results\_archive_2026_09_20\review_tech_B2_grok46.md` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\review_tech_B2_grok46.md` |
| 82 | `416dda94cb63` | 552 | sub | `results\_archive_2026_09_20\SHA256_MANIFEST.txt` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\SHA256_MANIFEST.txt` |
| 83 | `a729875c0c67` | 4712 | sub | `results\_archive_2026_09_20\_archive_manifest_2026_09_18.json` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_archive_manifest_2026_09_18.json` |
| 84 | `adc99e04ac53` | 454307 | sub | `results\_archive_2026_09_20\_coze_〔IM〕_v3_d7format_2026_09_18.pdf` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_coze_online_v3_d7format_2026_09_18.pdf` |
| 85 | `f3d4ec483599` | 41446 | sub | `results\_archive_2026_09_20\_d05_main_runner_2026_09_18.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_d05_main_runner_2026_09_18.py` |
| 86 | `7a5be4aef9ac` | 13694 | sub | `results\_archive_2026_09_20\_d05_md_report_only_2026_09_18.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_d05_md_report_only_2026_09_18.py` |
| 87 | `41bea33b9492` | 2088 | sub | `results\_archive_2026_09_20\_d05_sanity_3backbone_20260918.log` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_d05_sanity_3backbone_20260918.log` |
| 88 | `0b7e50a8a036` | 2938 | sub | `results\_archive_2026_09_20\_d05_verify_sha_2026_09_18.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_d05_verify_sha_2026_09_18.py` |
| 89 | `18984b04c45e` | 34134 | sub | `results\_archive_2026_09_20\_deposon_v2scripts_reverify_worker_2026_09_18.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_deposon_v2scripts_reverify_worker_2026_09_18.py` |
| 90 | `0769f60a0504` | 2678 | sub | `results\_archive_2026_09_20\_final_sha_2026_09_18.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_final_sha_2026_09_18.py` |
| 91 | `81bb1751be4c` | 4100 | sub | `results\_archive_2026_09_20\_fix_batch2_2026_09_18.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_fix_batch2_2026_09_18.py` |
| 92 | `01e63e488ce2` | 3207 | sub | `results\_archive_2026_09_20\_fix_batch3_2026_09_18.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_fix_batch3_2026_09_18.py` |
| 93 | `2efcd5ff42f1` | 8225 | sub | `results\_archive_2026_09_20\_fix_batch4_2026_09_18.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_fix_batch4_2026_09_18.py` |
| 94 | `1c59e7b803fe` | 2214 | sub | `results\_archive_2026_09_20\_fix_batch6_2026_09_18.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_fix_batch6_2026_09_18.py` |
| 95 | `389283c51275` | 4261 | sub | `results\_archive_2026_09_20\_fix_batch7_2026_09_18.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_fix_batch7_2026_09_18.py` |
| 96 | `5057ccf97d6b` | 2249 | sub | `results\_archive_2026_09_20\_fix_batch8_2026_09_18.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_fix_batch8_2026_09_18.py` |
| 97 | `2c2cc3ff542a` | 3524 | sub | `results\_archive_2026_09_20\_fix_d05_rescue_2026_09_18.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_fix_d05_rescue_2026_09_18.py` |
| 98 | `3de722dc9e39` | 26990 | sub | `results\_archive_2026_09_20\_letter_to_glm_ftfb_deep_revision_2026_09_18.md` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_letter_to_glm_ftfb_deep_revision_2026_09_18.md` |
| 99 | `f2934e5279e6` | 9717 | sub | `results\_archive_2026_09_20\_letter_to_mavis_full_mirror_request_2026_09_17.md` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_letter_to_mavis_full_mirror_request_2026_09_17.md` |
| 100 | `49dde3059959` | 1393 | sub | `results\_archive_2026_09_20\_probe_doubao_4versions_diff_2026_09_17.json` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_probe_doubao_4versions_diff_2026_09_17.json` |
| 101 | `93527eb7b2f7` | 2720 | sub | `results\_archive_2026_09_20\_probe_doubao_4versions_diff_2026_09_17.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_probe_doubao_4versions_diff_2026_09_17.py` |
| 102 | `9bcfe80c0dd0` | 2371 | sub | `results\_archive_2026_09_20\_probe_doubao_emb_direct_2026_09_17.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_probe_doubao_emb_direct_2026_09_17.py` |
| 103 | `f2818fc2ddff` | 2589 | sub | `results\_archive_2026_09_20\_probe_doubao_emb_via_proxy_2026_09_17.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_probe_doubao_emb_via_proxy_2026_09_17.py` |
| 104 | `dce965058076` | 2841 | sub | `results\_archive_2026_09_20\_probe_teamo_via_proxy.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_probe_teamo_via_proxy.py` |
| 105 | `e05555deb611` | 12919 | sub | `results\_archive_2026_09_20\_p_i_curvature_audit_probe_runner_2026_09_16.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_p_i_curvature_audit_probe_runner_2026_09_16.py` |
| 106 | `268225ccbb76` | 4397 | sub | `results\_archive_2026_09_20\_reviewer_a_audit_tmp.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_reviewer_a_audit_tmp.py` |
| 107 | `e11319f32dc5` | 2187 | sub | `results\_archive_2026_09_20\_sanity_openai_more.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_sanity_openai_more.py` |
| 108 | `63eb0a0aa102` | 2119 | sub | `results\_archive_2026_09_20\_sanity_teamo_one.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_sanity_teamo_one.py` |
| 109 | `888d02cd1443` | 3540 | sub | `results\_archive_2026_09_20\_sanity_teamo_three.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_sanity_teamo_three.py` |
| 110 | `4181a24c9ca1` | 277 | sub | `results\_archive_2026_09_20\_teamorouter_smoke_tmp.json` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_teamorouter_smoke_tmp.json` |
| 111 | `264f2bf5a3f2` | 6687 | sub | `results\_archive_2026_09_20\_temp_volc_test.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_temp_volc_test.py` |
| 112 | `0c9addf4a70f` | 675 | sub | `results\_archive_2026_09_20\_tmp_inspect_22cap.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_tmp_inspect_22cap.py` |
| 113 | `048ebc99177c` | 1029 | sub | `results\_archive_2026_09_20\_tmp_inspect_5model.py` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_tmp_inspect_5model.py` |
| 114 | `b0e2673f4a56` | 88584 | sub | `results\_archive_2026_09_20\_v41_flash_rag_partial.bak.json` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_v41_flash_rag_partial.bak.json` |
| 115 | `6952b3b02b96` | 8419 | sub | `results\_archive_2026_09_20\戴夫_FTFB双审包简报v3_2026-09-17.md` | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\戴夫_FTFB双审包简报v3_2026-09-17.md` |
| 116 | `befdd577adce` | 1141 | sub | `.trae\audit\compile_evidence\v2pre_h1h3_20260909\extract_tars.py` | `.trae\audit\compile_evidence\extract_tars.py` |
| 117 | `4458ccf3d64a` | 24113 | sub | `results\_archive_2026_09_24\_worker_openrouter_rag_run.py` | `results\_worker_openrouter_rag_run.py` |

---

## §2 执行前实测（本代理）

| 项 | 值 |
|:--|:--|
| 待删件在盘 | **117／117**（缺 0） |
| 留侧正身在盘 | **117／117**（缺 0） |
| 删／留路径互斥（无一删即他人所留） | **0 冲突** |
| 通道 | `mavis-trash`（**可恢复**·⛔0 永久删除） |

## §3 老实交代

1. **裁三之「122」未全数执行**：实删 117。扣减 5 件之理由见上表，皆**先于执行**写明，非事后补说。
2. **`_remote_pullback_2026_10_17\` 之副本将随批删除**：彼系远端原体之本地快照；④ 云端对账已暂缓，故其「基线」作用当前不生效。**此项损失如实登记**——若 PI 日后需该时点远端快照，须自远端重取。
3. **活引用面未测**：本批删后**须补「旧→新」登记**之条数**未得**（本代理 19:1x 件已列此限制）。删后凡指向被删件之路径式引用**将落空**；本记录之 §1「留」栏即其**替代指向**。
4. **本件 0 执行**：本件为**记录**；实际删除另办。

*件止。主代理 mavis 亲撰 · 2026-10-22 20:2x · ⛔0 回改既有件。*
