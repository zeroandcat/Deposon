# 去重复执行·删除记录 **r2**（禁令优先重算）· 2026-10-22

- 依据：PI 20:15 卡答（`ask_f1959ef42c84738879aa025f`）裁三「122 件一次全批」＋ 裁一「判据全核（含硬禁止类）」
- 前置记录：`results\_dedupe_delete_manifest_2026_10_22.md`（`efd647e91cac`／117 件·**未执行**）——本 r2 **取代其执行面**，该件**保留为快照·⛔0 回改**
- 判据：件数单尺｜射程：**上传面**，而 **HF 件依裁一不在上传面** ⇒ **不进本射程**

## §0 为何 r2（两处扣减·**皆先于执行写明**）

| 扣减 | 件数 | 理由 |
|:--|--:|:--|
| 禁令锁定组 `0a1e91d6f772`（密钥门 `_d05_sanity_3backbone`） | 2 | `MC-E4` 永不上传·禁令锁定 |
| 零字节组 `e3b0c44298fc`（4 件） | 3 | 零字节非内容重复；组内含 `_remote_pullback` 之 `.err`（在册活引用 25 处·「空 stderr ＝ 洁净运行」之证）；且含今日在途棒之 0 字节产物 |
| **HF 面路径（43 条）** | **43** | **裁一核准硬禁止类 ⇒ HF 件不在上传面**（HF-A `letters/` 43 条中命中者／HF-B `_archive_2026_09_20`／HF-G 具名 2 件）⇒ 其「重复」**不属上传面之件数问题**，且 HF-B 为 **MC-E4 隐私面之列名面**，删之恐毁证 |
| **合计扣减** | **48** | **122 − 48 ＝ 实删 74 件** |

⚠ **r1（`efd647e91cac`）之 117 件清单含有 43 件 HF 面件**——本代理在取出待删路径后**逐路径复核**始发现，**于执行前拦下**。r1 未执行任何删除。

## §1 逐件（74 行）

| # | SHA-12 | bytes | 区 | 删（相对仓根） | 留（正身） |
|--:|:--|--:|:--|:--|:--|
| 1 | `dfb02ade1474` | 591 | sub | `results\_inspect_captions.py` | `corpus\v20_caption_surface\_inspect_captions.py` |
| 2 | `dfb02ade1474` | 591 | sub | `results\_archive_2026_09_24\_inspect_captions.py` | `corpus\v20_caption_surface\_inspect_captions.py` |
| 3 | `25f745609658` | 612511 | repo | `_remote_pullback_2026_10_17\_september_workspace\results\_archive_2026_09_20\_v41_flash_rag_caption_embs.bak.json` | `corpus\v20_caption_surface\_v41_flash_rag_caption_embs.bak.json` |
| 4 | `d21912a05d79` | 1017 | sub | `results\attack_pc_a1_resampling_2026_09_15.json` | `results\boss_pc_1_a1_resampling_2026_09_15.json` |
| 5 | `d21912a05d79` | 1017 | sub | `results\boss_pc_1_a1_resampling_2026_09_15.json` | `results\boss_pc_1_a1_resampling_2026_09_15.json` |
| 6 | `43d9ce160fc8` | 2460 | repo | `results\boss_pe_1_real_2d_ising_2026_09_15.json` | `results\boss_pc_1_real_2d_ising_2026_09_15.json` |
| 7 | `43d9ce160fc8` | 2460 | sub | `results\boss_pc_1_real_2d_ising_2026_09_15.json` | `results\boss_pc_1_real_2d_ising_2026_09_15.json` |
| 8 | `8933d61b180a` | 3553 | repo | `results\boss_pe_2_real_transverse_ising_2026_09_15.json` | `results\boss_pc_2_real_transverse_ising_2026_09_15.json` |
| 9 | `8933d61b180a` | 3553 | sub | `results\boss_pc_2_real_transverse_ising_2026_09_15.json` | `results\boss_pc_2_real_transverse_ising_2026_09_15.json` |
| 10 | `94b5398be76c` | 2364 | repo | `results\boss_pe_3_real_reservoir_2026_09_15.json` | `results\boss_pc_3_real_reservoir_2026_09_15.json` |
| 11 | `94b5398be76c` | 2364 | sub | `results\boss_pc_3_real_reservoir_2026_09_15.json` | `results\boss_pc_3_real_reservoir_2026_09_15.json` |
| 12 | `6cbb8ba01bfb` | 15409 | repo | `results\_d9_e2e_backup_2026_10_13\_s4_heldout_sampling_seedprime_items_2026_10_10.json` | `results\_s4_heldout_sampling_seedprime_items_2026_10_10.json` |
| 13 | `6cbb8ba01bfb` | 15409 | repo | `results\_d9_e2e_rerun_backup_2026_10_13\_s4_heldout_sampling_seedprime_items_2026_10_10.json` | `results\_s4_heldout_sampling_seedprime_items_2026_10_10.json` |
| 14 | `1fc5f3ab3f93` | 2022 | sub | `.trae\audit\compile_evidence\v2_overfull_fix_20260909\compile_runner.ps1` | `.trae\audit\compile_evidence\compile_runner.ps1` |
| 15 | `1fc5f3ab3f93` | 2022 | sub | `.trae\audit\compile_evidence\v2pre_h1h3_20260909\compile_runner.ps1` | `.trae\audit\compile_evidence\compile_runner.ps1` |
| 16 | `efe05ad775de` | 24150 | repo | `corpus\v20\by_model\kimi\index_v2_2026_09_16.json` | `corpus\v20\index_v2_2026_09_16.json` |
| 17 | `6a2656878745` | 12798 | repo | `corpus\v20_caption_surface\strip_captions_22.json` | `corpus\v20\strip_captions_22.json` |
| 18 | `9e1ccbdceacc` | 25347 | sub | `deposon_team\products\minimax_artifact_v_2026_09_16.json` | `corpus\v20\by_model\minimax\artifact_v_2026_09_16.json` |
| 19 | `d2cd7acb29a1` | 18596 | sub | `deposon_team\plugins\_p_d_b3_merkle_22caption_runner_2026_09_16.py` | `corpus\v20_caption_surface\_p_d_b3_merkle_22caption_runner_2026_09_16.py` |
| 20 | `dfbcc5d6fc34` | 13775 | sub | `results\_p_d_v03_22caption_verification_20260917_163757.json` | `corpus\v20_caption_surface\_p_d_v03_22caption_verification_20260917_163757.json` |
| 21 | `c7c59e0d2f6c` | 8753 | sub | `results\boss_pa_1_rbr_rm_result_2026_09_15.json` | `results\boss_pa_1_rbr_rm_result_2026_09_15.json` |
| 22 | `5c76137d6430` | 7530 | sub | `results\boss_pa_2_potential_game_result_2026_09_15.json` | `results\boss_pa_2_potential_game_result_2026_09_15.json` |
| 23 | `d6f233d73c45` | 9098 | sub | `results\boss_pa_3_replicator_dynamics_result_2026_09_15.json` | `results\boss_pa_3_replicator_dynamics_result_2026_09_15.json` |
| 24 | `5a880678c386` | 1024 | sub | `results\attack_pc_a2_fitting_2026_09_15.json` | `results\boss_pc_2_a2_fitting_2026_09_15.json` |
| 25 | `d74d6b39d1b0` | 1265 | sub | `results\attack_pc_a3_clipping_2026_09_15.json` | `results\boss_pc_3_a3_clipping_2026_09_15.json` |
| 26 | `4505cca79c15` | 2456 | sub | `results\d7_5anchor_60cells_9model_verdict_2026_09_18.json` | `results\d7_5anchor_60cells_9model_verdict_2026_09_18.json` |
| 27 | `55428f6bd848` | 3041 | repo | `results\_glm_evidence_unpacked_2026_10_13\_september_workspace\results\deposon_g1_mindmap_demo.json` | `results\deposon_g1_mindmap_demo.json` |
| 28 | `ca71aa6858e1` | 631644 | sub | `results\_archive_2026_09_21\deposon_v20_corpus_eval.json` | `results\deposon_v20_corpus_eval.json` |
| 29 | `a2ae7997ee67` | 123331 | sub | `results\_archive_2026_09_21\deposon_v20_gt2b.json` | `results\deposon_v20_gt2b.json` |
| 30 | `35b676773243` | 7844 | sub | `results\_archive_2026_09_21\deposon_v20_gt3.json` | `results\deposon_v20_gt3.json` |
| 31 | `b9b65c568842` | 915 | sub | `results\_archive_2026_09_21\deposon_v20_vector_audit.json` | `results\deposon_v20_vector_audit.json` |
| 32 | `218ef1a99f97` | 11703 | sub | `results\deposon_volcengine_minimax_m3_30cells_2026_09_10.py` | `results\deposon_volcengine_minimax_m3_30cells_2026_09_10.py` |
| 33 | `a7dff824ed56` | 22877 | repo | `results\_glm_evidence_unpacked_2026_10_13\_september_workspace\results\_s3_d1fill_recount_2026_10_01.md` | `results\_s3_d1fill_recount_2026_10_01.md` |
| 34 | `5777a07c608a` | 43130 | repo | `results\_d9_e2e_backup_2026_10_13\_s4_heldout_sampling_seedthird_items_2026_10_11.json` | `results\_s4_heldout_sampling_seedthird_items_2026_10_11.json` |
| 35 | `784f042bf93d` | 22646 | repo | `results\_d9_e2e_backup_2026_10_13\_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | `results\_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` |
| 36 | `839fb5452578` | 16099 | repo | `results\_d9_e2e_backup_2026_10_13\_s5doubleprime_five_lines_readings_2026_10_11.json` | `results\_s5doubleprime_five_lines_readings_2026_10_11.json` |
| 37 | `079108c62a82` | 21049 | repo | `results\_d9_e2e_backup_2026_10_13\_stage3_trigger_readings_items_2026_10_11.json` | `results\_stage3_trigger_readings_items_2026_10_11.json` |
| 38 | `62fb594be3f9` | 32371 | repo | `results\_glm_evidence_unpacked_2026_10_13\_september_workspace\results\_t1_substrate_gap_census_2026_10_01.md` | `results\_t1_substrate_gap_census_2026_10_01.md` |
| 39 | `ef5a40554960` | 46836 | repo | `results\_glm_evidence_unpacked_2026_10_13\_september_workspace\results\_v3_s_prereg_v1_2026_09_27.md` | `results\_v3_s_prereg_v1_2026_09_27.md` |
| 40 | `c68076c88140` | 26253 | sub | `results\_v5_gt8_lowarm_result_2026_09_29_cb132cd5.json` | `results\_v5_gt8_lowarm_result_2026_09_29.json` |
| 41 | `25141de92c50` | 7188 | sub | `results\_xiang14_third_reissue_registration_2026_10_13.md` | `results\_xiang14_third_reissue_registration_2026_10_13.md` |
| 42 | `d0b7467fa01c` | 52787 | repo | `results\.tmp\_s18memo_body_2026_10_22.md` | `results\.tmp\_s18memo_append_2026_10_22.md` |
| 43 | `15904ecae629` | 11105 | sub | `results\_volc_22cap_emb.py` | `results\_archive_2026_09_24\_volc_22cap_emb.py` |
| 44 | `dc9cb0e02922` | 28370 | sub | `results\_d1_ruling_and_s3_transition_2026_10_01.md` | `results\_glm_evidence_unpacked_2026_10_13\_september_workspace\results\_d1_ruling_and_s3_transition_2026_10_01.md` |
| 45 | `693eefdd7a82` | 32296 | sub | `results\_kv3s_3_2_terminal_verdict_2026_10_01.md` | `results\_glm_evidence_unpacked_2026_10_13\_september_workspace\results\_kv3s_3_2_terminal_verdict_2026_10_01.md` |
| 46 | `303bf7c6f34d` | 28762 | sub | `results\_s3_d1_rulings_supplement_register_2026_10_01.md` | `results\_glm_evidence_unpacked_2026_10_13\_september_workspace\results\_s3_d1_rulings_supplement_register_2026_10_01.md` |
| 47 | `a9ad1de618f5` | 1669 | sub | `results\_p_j_convergence_basin_2026_09_16\p_j_convergence_basin_results_2026_09_16.json` | `results\_p_j_convergence_basin_2026_09_16\p_j_convergence_basin_results_2026_09_16.json` |
| 48 | `4bdec2683f06` | 22105 | sub | `_archive_deposon_2026_09_17\verifier\audit\conservation.py` | `verifier\audit\conservation.py` |
| 49 | `57f06a426bec` | 3011 | sub | `results\deposon_benchmark_v1_3_labelfree.json` | `_remote_pullback_2026_10_17\results\deposon_benchmark_v1_3_labelfree.json` |
| 50 | `769ae8c908c9` | 3134 | sub | `results\deposon_benchmark_v1_3_resonant.json` | `_remote_pullback_2026_10_17\results\deposon_benchmark_v1_3_resonant.json` |
| 51 | `c9796d3b3263` | 12479 | sub | `results\deposon_benchmark_v1_4_sc5.json` | `_remote_pullback_2026_10_17\results\deposon_benchmark_v1_4_sc5.json` |
| 52 | `a3de045b5dd7` | 2284 | sub | `results\deposon_g3_arrhenius.json` | `_remote_pullback_2026_10_17\results\deposon_g3_arrhenius.json` |
| 53 | `a7952d9d78db` | 5517 | sub | `results\deposon_v16_llm_prior_summary.json` | `_remote_pullback_2026_10_17\results\deposon_v16_llm_prior_summary.json` |
| 54 | `5f16be89efc5` | 938 | sub | `results\llm_prior_cache.json` | `_remote_pullback_2026_10_17\results\llm_prior_cache.json` |
| 55 | `d3f72f67977d` | 639 | sub | `results\llm_prior_cache_v18_contamination.json` | `_remote_pullback_2026_10_17\results\llm_prior_cache_v18_contamination.json` |
| 56 | `7c0d169ef164` | 512 | sub | `results\llm_prior_cache_v18_contentless.json` | `_remote_pullback_2026_10_17\results\llm_prior_cache_v18_contentless.json` |
| 57 | `023f936f80fb` | 2168 | sub | `results\llm_prior_cache_v18_direction.json` | `_remote_pullback_2026_10_17\results\llm_prior_cache_v18_direction.json` |
| 58 | `8dce6d7618a2` | 1925 | sub | `results\llm_prior_cache_v18_labelshuffle.json` | `_remote_pullback_2026_10_17\results\llm_prior_cache_v18_labelshuffle.json` |
| 59 | `8b6682181392` | 2186 | sub | `results\v19_edges_audit_input.csv` | `_remote_pullback_2026_10_17\results\v19_edges_audit_input.csv` |
| 60 | `f95f382ace44` | 2151 | sub | `results\v20_graph_features.csv` | `_remote_pullback_2026_10_17\results\v20_graph_features.csv` |
| 61 | `3596490e1fc0` | 4236 | sub | `results\v20_regression_field_v2.json` | `_remote_pullback_2026_10_17\results\v20_regression_field_v2.json` |
| 62 | `dfe014c627ca` | 988 | sub | `results\v20_statcheck_fm_vs_deg.json` | `_remote_pullback_2026_10_17\results\v20_statcheck_fm_vs_deg.json` |
| 63 | `1dadfaeb2c43` | 868 | sub | `results\v20_statcheck_fm_vs_rand.json` | `_remote_pullback_2026_10_17\results\v20_statcheck_fm_vs_rand.json` |
| 64 | `4af67e6cbe71` | 3449 | sub | `results\_archive_2026_09_18\_trae_anchor_18_audit_20260917_193000.md` | `_remote_pullback_2026_10_17\results\_trae_anchor_18_audit_20260917_193000.md` |
| 65 | `f2a655cd5e54` | 3467 | sub | `results\_archive_2026_09_18\_trae_corpus_5_audit_20260917_193000.md` | `_remote_pullback_2026_10_17\results\_trae_corpus_5_audit_20260917_193000.md` |
| 66 | `3184b30b7b0d` | 4253 | sub | `results\_archive_2026_09_18\_trae_d7_v1_audit_20260917_190000.json` | `_remote_pullback_2026_10_17\results\_trae_d7_v1_audit_20260917_190000.json` |
| 67 | `8ece24be6b8a` | 3281 | sub | `results\_archive_2026_09_18\_trae_kimi_push_v3_audit_20260917_193000.md` | `_remote_pullback_2026_10_17\results\_trae_kimi_push_v3_audit_20260917_193000.md` |
| 68 | `c5598b13c139` | 17363 | sub | `deposon_team\verifier\v42_v2_2026_09_16.py` | `_remote_pullback_2026_10_17\_september_workspace\deposon_team\verifier\v42_v2_2026_09_16.py` |
| 69 | `483602856618` | 1879 | sub | `deposon_team\verifier\v42_v2_baseline_2026_09_16.json` | `_remote_pullback_2026_10_17\_september_workspace\deposon_team\verifier\v42_v2_baseline_2026_09_16.json` |
| 70 | `b471190e579c` | 770 | sub | `deposon_team\verifier\v42_v2_runs_2026_09_16.jsonl` | `_remote_pullback_2026_10_17\_september_workspace\deposon_team\verifier\v42_v2_runs_2026_09_16.jsonl` |
| 71 | `a82881653520` | 465366 | sub | `results\_coze_〔IM〕_v4_d7format_2026_09_26.pdf` | `_remote_pullback_2026_10_17\_september_workspace\results\_coze_online_v4_d7format_2026_09_26.pdf` |
| 72 | `2efdc3d7741d` | 3624 | sub | `results\_coze_paper_v1_summary_2026_09_17.md` | `_remote_pullback_2026_10_17\_september_workspace\results\_coze_paper_v1_summary_2026_09_17.md` |
| 73 | `befdd577adce` | 1141 | sub | `.trae\audit\compile_evidence\v2pre_h1h3_20260909\extract_tars.py` | `.trae\audit\compile_evidence\extract_tars.py` |
| 74 | `4458ccf3d64a` | 24113 | sub | `results\_archive_2026_09_24\_worker_openrouter_rag_run.py` | `results\_worker_openrouter_rag_run.py` |

## §2 执行前实测

| 项 | 值 |
|:--|:--|
| 待删在盘 | **74／74**（缺 0） |
| 留侧正身在盘 | **74／74**（缺 0） |
| 删／留互斥 | **0 冲突** |
| 分区 | repo **17**／sub **57** |
| 通道 | `mavis-trash`（可恢复） |

## §3 老实交代

1. **裁三之 122 未全数执行**，实删 74；三处扣减皆**先于执行**列明（禁令锁 2／零字节 3／HF 面 43）。
2. **HF 面之重复件本可减而今回不减**：若 PI 另裁「HF 面亦要减重复」，则须**逐件核其禁令性质**后另批，⛔0 由本代理径行。
3. **活引用面未测**：删后须补「旧→新」登记之条数未得；本 §1「留」栏即替代指向。
4. **`_remote_pullback_2026_10_17\` 之副本随批删除**——彼为远端原体之本地快照，④ 已暂缓故其基线作用当前不生效；若日后需该时点快照，须自远端重取。

*件止。主代理 mavis 亲撰 · 2026-10-22 20:3x · PURE-APPEND 新件。*

---

## §4 执行回执（本代理亲办 · 2026-10-22 20:4x）

| 项 | 值 |
|:--|:--|
| 计划删（含 `results\\.tmp\\` 之 1 件） | 74 件 |
| **实际执行** | **73 件**（剔除 `results\\.tmp\\_s18memo_body_2026_10_22.md`——**工作面·非上传面**，不属本射程） |
| 分区 | repo **16** ／ sub **57** |
| 通道 | `mavis-trash`（**可恢复**）；**两批 ＋ 1 件补删**，逐件回执 |
| **删后复扫：仍在其位** | **0 件** ✅ |
| **留侧正身缺失** | **0 件** ✅（66 个不同正身全在） |
| **sub 区件数** | 1,276 → **1,219**（**−57**，与分区计数逐位吻合 ✅） |
| 删除执行中之一漏 | `sub\\results\\_archive_2026_09_24\\_worker_openrouter_rag_run.py` 于批二未获回执 ⇒ **单独补删并复扫确认**（已不在位） |

### §4-1 与裁三之数差（如实）

| 项 | 件数 |
|:--|--:|
| PI 裁三之数（冗余上界） | **122** |
| − 禁令锁定组（密钥门 `0a1e91d6f772`） | −2 |
| − 零字节组（`e3b0c44298fc`，4 件） | −3 |
| − **HF 面路径**（裁一核准硬禁止类 ⇒ **HF 件不在上传面**） | −43 |
| − `results\\.tmp\\` 工作面件 | −1 |
| **＝ 实删** | **73** |

⛔ **0 永久删除**——全部在回收站，可恢复。

### §4-2 教训（**本日第五例同族病**）

r1 之 117 件清单**已含有 43 件 HF 面件**（其中 `sub\\results\\_archive_2026_09_20\\` 即 `MC-E4` 隐私面之列名面）——若照 r1 执行，将**删掉禁令面之件**。

📌 **拦下之因**：取出待删路径后**逐路径复核**（非抽检），发现 40 余条落于 `_archive_2026_09_20`。

📌 **可用判据**：**裁一（判据全核·含硬禁止类）与裁三（去重复）须连读**——HF 件依裁一**不在上传面**，故**不属**裁三「上传面去重复」之射程；**两裁不连读即会误删禁令面**。凡多裁并颁，须先核**裁与裁之间的集合包含关系**，再执行。

---

*补录止。主代理 mavis 亲撰 · 2026-10-22 20:4x · PURE-APPEND。*
