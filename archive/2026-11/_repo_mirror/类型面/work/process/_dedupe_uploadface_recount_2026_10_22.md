# 去重复族按「件数尺」重判（上传面）——本代理直算 · 2026-10-22

- 件性质：**核实 ＋ 候选处置**（⛔ 0 移动／0 删除／0 改名／0 回改既有件）
- 观测时点：**2026-10-22 19:26:27**（本代理直算）
- 判据：**件数单尺**（PI 2026-10-22 17:5x 逐字「因为有Agent与RAG，体积不是大问题，文件数才是」）⇒ ⛔ 0 以体积为任何理由
- 射程：**上传面**＝`deposon-repo`（排除 `.tmp\` 与 `results\.tmp\`）＋ `deposon-sub`。归档区不上传（PI 18:0x 逐字），**不在射程**
- 器：Python 3 `os.walk` 全量 ＋ `hashlib.sha256` **全字节**判重（非 SHA-12 前缀、非「同尺寸即判重」）
- 执行权：**⛔ 0 本件执行**——减件须 PI 逐单令，且走可恢复通道

---

## §0 摘要（一屏自足）

| 项 | 读数 |
|:--|--:|
| 上传面扫描件数 | **4058** |
| 重复组数 | **111** |
| 涉重件数 | **233** |
| **冗余件数（可减上界）** | **122** |
| 其中跨区组（repo↔sub） | **95 组** |
| 其中 `repo` 内组 | **13 组** |
| 其中 `sub` 内组 | **3 组** |
| 零字节重复组 | **1 组／4 件** |
| **禁令面涉及组** | **1 组**（见 §4-2） |

### 与在册三数之对照（⛔ 0 择一、三读并陈）

| 源 | 组数 | 件数 | 口径差异（本代理判读） |
|:--|--:|--:|:--|
| 勘查件 `cbd85f8c5522` §2-1 | 99 | 204 | 含 `.tmp\`（**非上传面**）⇒ 与本节不可直接比 |
| `_bloat_inventory` `3c55ea8be914` §2-1 | 118 | 270 | 同上，且判重口径未载明 |
| 规则件 `ccf5483ccb8b` 之「去重复 −1,157」 | — | 1,157 | **量级远超**上二者；其口径未载，疑含归档区或采用「同名即判重」⇒ **⛔ 0 采信，挂账候核** |
| **本件（上传面·全字节）** | **111** | **233（冗余 122）** | 射程最窄、口径最严 ⇒ 可核 |

📌 **关键结构性事实**：按 ③ 规则件之**镜像区去重规则**（同 SHA-256 者**只传一次**），上传面内之重复件**本就不产生额外上传量**。⇒ **删它们不减上传量，只减本地件数**——恰合 PI 之件数尺。二者不冲突。

---

## §1 立准（旧账逐字 ＋ 判据变更）

**旧账（勘查件 `cbd85f8c5522` §2-1「噪声·重复副本」行）之判据与结论**，逐字要点：

> 「**噪声·重复副本** ｜ **保留** ｜ 204（99 组）｜ 冗余 10,161,132 ｜ 字节全同之族（SHA-12 相同）｜ **99 组逐组实测皆有活引用（0 组零引用）⇒ 删任一侧即生幽灵**；且「同字节异名」本身即复现性之据 ⇒ **删除面 ＝ 0**」

**该结论之基座已失效**——PI 2026-10-22 三令：

1. **件数单尺**（17:5x）：「因为有Agent与RAG，体积不是大问题，文件数才是」⇒ 「省 10,161,132 B」**不成理由**。
2. **「生幽灵」不再是否决项**：新尺下幽灵**可登记**（留「旧路径→新路径」映射表）⇒ 旧判「删面 ＝ 0」**不成立**。
3. **归档区不上传**（18:0x）⇒ 只算上传面。

---

## §2 证器（射程·时点·仪器自审）

| 项 | 内容 |
|:--|:--|
| 扫描根 | `〔本地路径已脱敏〕`（排除 `.tmp\`／`results\.tmp\`）＋ `〔本地路径已脱敏〕` |
| 命中件数 | **4058** |
| 判重口径 | **全字节 `sha256` 相同**（⛔ 0 用 SHA-12 前缀；⛔ 0 用「同尺寸即判重」） |
| 未入射程 | 归档区（不上传）／`GLM` 面（仅计数）／`.tmp` 与 `results\.tmp`（工作面，非上传面） |
| **仪器自审** | ①零字节件单列（`sha256` 空串 `e3b0c44298fc`）——零字节「重复」**非内容重复**，须另判；②`_remote_pullback_*` 与 `_september_workspace` 之命中原为**远端拉回副本**，其「重复」具物证属性，**另标**；③本件**未测活引用面**（见 §6-1） |

---

## §3 逐组表（111 组·按 n 降序）

| # | SHA-12 | n | bytes | 路径（区:相对） | 禁令标记 |
|--:|:--|--:|--:|:--|:--|
| 1 | `e3b0c44298fc` | 4 | 0 | repo:results/.tmp/_s19memo2_compactions_2026_10_22.md ｜ repo:results/.tmp/_s19memo2_dispatch2_2026_10_22.md ｜ repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/gpt6_30cells_run.log.err ｜ repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/volcengine_glm_latest_30cells_v2_run_2026_09_10.log.err | 远端拉回副本（物证面） |
| 2 | `dfb02ade1474` | 3 | 591 | repo:corpus/v20_caption_surface/_inspect_captions.py ｜ sub:results/_inspect_captions.py ｜ sub:results/_archive_2026_09_24/_inspect_captions.py | — |
| 3 | `25f745609658` | 3 | 612511 | repo:corpus/v20_caption_surface/_v41_flash_rag_caption_embs.bak.json ｜ repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_v41_flash_rag_caption_embs.bak.json ｜ sub:results/_archive_2026_09_20/_v41_flash_rag_caption_embs.bak.json | 远端拉回副本（物证面） |
| 4 | `d21912a05d79` | 3 | 1017 | repo:results/boss_pc_1_a1_resampling_2026_09_15.json ｜ sub:results/attack_pc_a1_resampling_2026_09_15.json ｜ sub:results/boss_pc_1_a1_resampling_2026_09_15.json | — |
| 5 | `43d9ce160fc8` | 3 | 2460 | repo:results/boss_pc_1_real_2d_ising_2026_09_15.json ｜ repo:results/boss_pe_1_real_2d_ising_2026_09_15.json ｜ sub:results/boss_pc_1_real_2d_ising_2026_09_15.json | — |
| 6 | `8933d61b180a` | 3 | 3553 | repo:results/boss_pc_2_real_transverse_ising_2026_09_15.json ｜ repo:results/boss_pe_2_real_transverse_ising_2026_09_15.json ｜ sub:results/boss_pc_2_real_transverse_ising_2026_09_15.json | — |
| 7 | `94b5398be76c` | 3 | 2364 | repo:results/boss_pc_3_real_reservoir_2026_09_15.json ｜ repo:results/boss_pe_3_real_reservoir_2026_09_15.json ｜ sub:results/boss_pc_3_real_reservoir_2026_09_15.json | — |
| 8 | `6cbb8ba01bfb` | 3 | 15409 | repo:results/_s4_heldout_sampling_seedprime_items_2026_10_10.json ｜ repo:results/_d9_e2e_backup_2026_10_13/_s4_heldout_sampling_seedprime_items_2026_10_10.json ｜ repo:results/_d9_e2e_rerun_backup_2026_10_13/_s4_heldout_sampling_seedprime_items_2026_10_10.json | — |
| 9 | `0a1e91d6f772` | 3 | 2292 | repo:_remote_pullback_2026_10_17/results/_d05_sanity_3backbone_20260918_100110.json ｜ repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json ｜ sub:results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json | MC-E4 密钥门 1 件（永不上传）、远端拉回副本（物证面） |
| 10 | `1fc5f3ab3f93` | 3 | 2022 | sub:.trae/audit/compile_evidence/compile_runner.ps1 ｜ sub:.trae/audit/compile_evidence/v2pre_h1h3_20260909/compile_runner.ps1 ｜ sub:.trae/audit/compile_evidence/v2_overfull_fix_20260909/compile_runner.ps1 | — |
| 11 | `efe05ad775de` | 2 | 24150 | repo:corpus/v20/index_v2_2026_09_16.json ｜ repo:corpus/v20/by_model/kimi/index_v2_2026_09_16.json | — |
| 12 | `6a2656878745` | 2 | 12798 | repo:corpus/v20/strip_captions_22.json ｜ repo:corpus/v20_caption_surface/strip_captions_22.json | — |
| 13 | `9e1ccbdceacc` | 2 | 25347 | repo:corpus/v20/by_model/minimax/artifact_v_2026_09_16.json ｜ sub:deposon_team/products/minimax_artifact_v_2026_09_16.json | — |
| 14 | `d2cd7acb29a1` | 2 | 18596 | repo:corpus/v20_caption_surface/_p_d_b3_merkle_22caption_runner_2026_09_16.py ｜ sub:deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_09_16.py | — |
| 15 | `dfbcc5d6fc34` | 2 | 13775 | repo:corpus/v20_caption_surface/_p_d_v03_22caption_verification_20260917_163757.json ｜ sub:results/_p_d_v03_22caption_verification_20260917_163757.json | — |
| 16 | `c7c59e0d2f6c` | 2 | 8753 | repo:results/boss_pa_1_rbr_rm_result_2026_09_15.json ｜ sub:results/boss_pa_1_rbr_rm_result_2026_09_15.json | — |
| 17 | `5c76137d6430` | 2 | 7530 | repo:results/boss_pa_2_potential_game_result_2026_09_15.json ｜ sub:results/boss_pa_2_potential_game_result_2026_09_15.json | — |
| 18 | `d6f233d73c45` | 2 | 9098 | repo:results/boss_pa_3_replicator_dynamics_result_2026_09_15.json ｜ sub:results/boss_pa_3_replicator_dynamics_result_2026_09_15.json | — |
| 19 | `5a880678c386` | 2 | 1024 | repo:results/boss_pc_2_a2_fitting_2026_09_15.json ｜ sub:results/attack_pc_a2_fitting_2026_09_15.json | — |
| 20 | `d74d6b39d1b0` | 2 | 1265 | repo:results/boss_pc_3_a3_clipping_2026_09_15.json ｜ sub:results/attack_pc_a3_clipping_2026_09_15.json | — |
| 21 | `4505cca79c15` | 2 | 2456 | repo:results/d7_5anchor_60cells_9model_verdict_2026_09_18.json ｜ sub:results/d7_5anchor_60cells_9model_verdict_2026_09_18.json | — |
| 22 | `55428f6bd848` | 2 | 3041 | repo:results/deposon_g1_mindmap_demo.json ｜ repo:results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/deposon_g1_mindmap_demo.json | — |
| 23 | `ca71aa6858e1` | 2 | 631644 | repo:results/deposon_v20_corpus_eval.json ｜ sub:results/_archive_2026_09_21/deposon_v20_corpus_eval.json | — |
| 24 | `a2ae7997ee67` | 2 | 123331 | repo:results/deposon_v20_gt2b.json ｜ sub:results/_archive_2026_09_21/deposon_v20_gt2b.json | — |
| 25 | `35b676773243` | 2 | 7844 | repo:results/deposon_v20_gt3.json ｜ sub:results/_archive_2026_09_21/deposon_v20_gt3.json | — |
| 26 | `b9b65c568842` | 2 | 915 | repo:results/deposon_v20_vector_audit.json ｜ sub:results/_archive_2026_09_21/deposon_v20_vector_audit.json | — |
| 27 | `218ef1a99f97` | 2 | 11703 | repo:results/deposon_volcengine_minimax_m3_30cells_2026_09_10.py ｜ sub:results/deposon_volcengine_minimax_m3_30cells_2026_09_10.py | — |
| 28 | `a7dff824ed56` | 2 | 22877 | repo:results/_s3_d1fill_recount_2026_10_01.md ｜ repo:results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_s3_d1fill_recount_2026_10_01.md | — |
| 29 | `5777a07c608a` | 2 | 43130 | repo:results/_s4_heldout_sampling_seedthird_items_2026_10_11.json ｜ repo:results/_d9_e2e_backup_2026_10_13/_s4_heldout_sampling_seedthird_items_2026_10_11.json | — |
| 30 | `784f042bf93d` | 2 | 22646 | repo:results/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md ｜ repo:results/_d9_e2e_backup_2026_10_13/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md | — |
| 31 | `839fb5452578` | 2 | 16099 | repo:results/_s5doubleprime_five_lines_readings_2026_10_11.json ｜ repo:results/_d9_e2e_backup_2026_10_13/_s5doubleprime_five_lines_readings_2026_10_11.json | — |
| 32 | `079108c62a82` | 2 | 21049 | repo:results/_stage3_trigger_readings_items_2026_10_11.json ｜ repo:results/_d9_e2e_backup_2026_10_13/_stage3_trigger_readings_items_2026_10_11.json | — |
| 33 | `62fb594be3f9` | 2 | 32371 | repo:results/_t1_substrate_gap_census_2026_10_01.md ｜ repo:results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_t1_substrate_gap_census_2026_10_01.md | — |
| 34 | `ef5a40554960` | 2 | 46836 | repo:results/_v3_s_prereg_v1_2026_09_27.md ｜ repo:results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_v3_s_prereg_v1_2026_09_27.md | — |
| 35 | `c68076c88140` | 2 | 26253 | repo:results/_v5_gt8_lowarm_result_2026_09_29.json ｜ sub:results/_v5_gt8_lowarm_result_2026_09_29_cb132cd5.json | — |
| 36 | `25141de92c50` | 2 | 7188 | repo:results/_xiang14_third_reissue_registration_2026_10_13.md ｜ sub:results/_xiang14_third_reissue_registration_2026_10_13.md | — |
| 37 | `d0b7467fa01c` | 2 | 52787 | repo:results/.tmp/_s18memo_append_2026_10_22.md ｜ repo:results/.tmp/_s18memo_body_2026_10_22.md | — |
| 38 | `15904ecae629` | 2 | 11105 | repo:results/_archive_2026_09_24/_volc_22cap_emb.py ｜ sub:results/_volc_22cap_emb.py | — |
| 39 | `dc9cb0e02922` | 2 | 28370 | repo:results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_d1_ruling_and_s3_transition_2026_10_01.md ｜ sub:results/_d1_ruling_and_s3_transition_2026_10_01.md | — |
| 40 | `693eefdd7a82` | 2 | 32296 | repo:results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_kv3s_3_2_terminal_verdict_2026_10_01.md ｜ sub:results/_kv3s_3_2_terminal_verdict_2026_10_01.md | — |
| 41 | `303bf7c6f34d` | 2 | 28762 | repo:results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_s3_d1_rulings_supplement_register_2026_10_01.md ｜ sub:results/_s3_d1_rulings_supplement_register_2026_10_01.md | — |
| 42 | `a9ad1de618f5` | 2 | 1669 | repo:results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json ｜ sub:results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json | — |
| 43 | `4bdec2683f06` | 2 | 22105 | repo:verifier/audit/conservation.py ｜ sub:_archive_deposon_2026_09_17/verifier/audit/conservation.py | — |
| 44 | `57f06a426bec` | 2 | 3011 | repo:_remote_pullback_2026_10_17/results/deposon_benchmark_v1_3_labelfree.json ｜ sub:results/deposon_benchmark_v1_3_labelfree.json | 远端拉回副本（物证面） |
| 45 | `769ae8c908c9` | 2 | 3134 | repo:_remote_pullback_2026_10_17/results/deposon_benchmark_v1_3_resonant.json ｜ sub:results/deposon_benchmark_v1_3_resonant.json | 远端拉回副本（物证面） |
| 46 | `c9796d3b3263` | 2 | 12479 | repo:_remote_pullback_2026_10_17/results/deposon_benchmark_v1_4_sc5.json ｜ sub:results/deposon_benchmark_v1_4_sc5.json | 远端拉回副本（物证面） |
| 47 | `a3de045b5dd7` | 2 | 2284 | repo:_remote_pullback_2026_10_17/results/deposon_g3_arrhenius.json ｜ sub:results/deposon_g3_arrhenius.json | 远端拉回副本（物证面） |
| 48 | `a7952d9d78db` | 2 | 5517 | repo:_remote_pullback_2026_10_17/results/deposon_v16_llm_prior_summary.json ｜ sub:results/deposon_v16_llm_prior_summary.json | 远端拉回副本（物证面） |
| 49 | `5f16be89efc5` | 2 | 938 | repo:_remote_pullback_2026_10_17/results/llm_prior_cache.json ｜ sub:results/llm_prior_cache.json | 远端拉回副本（物证面） |
| 50 | `d3f72f67977d` | 2 | 639 | repo:_remote_pullback_2026_10_17/results/llm_prior_cache_v18_contamination.json ｜ sub:results/llm_prior_cache_v18_contamination.json | 远端拉回副本（物证面） |
| 51 | `7c0d169ef164` | 2 | 512 | repo:_remote_pullback_2026_10_17/results/llm_prior_cache_v18_contentless.json ｜ sub:results/llm_prior_cache_v18_contentless.json | 远端拉回副本（物证面） |
| 52 | `023f936f80fb` | 2 | 2168 | repo:_remote_pullback_2026_10_17/results/llm_prior_cache_v18_direction.json ｜ sub:results/llm_prior_cache_v18_direction.json | 远端拉回副本（物证面） |
| 53 | `8dce6d7618a2` | 2 | 1925 | repo:_remote_pullback_2026_10_17/results/llm_prior_cache_v18_labelshuffle.json ｜ sub:results/llm_prior_cache_v18_labelshuffle.json | 远端拉回副本（物证面） |
| 54 | `8b6682181392` | 2 | 2186 | repo:_remote_pullback_2026_10_17/results/v19_edges_audit_input.csv ｜ sub:results/v19_edges_audit_input.csv | 远端拉回副本（物证面） |
| 55 | `f95f382ace44` | 2 | 2151 | repo:_remote_pullback_2026_10_17/results/v20_graph_features.csv ｜ sub:results/v20_graph_features.csv | 远端拉回副本（物证面） |
| 56 | `3596490e1fc0` | 2 | 4236 | repo:_remote_pullback_2026_10_17/results/v20_regression_field_v2.json ｜ sub:results/v20_regression_field_v2.json | 远端拉回副本（物证面） |
| 57 | `dfe014c627ca` | 2 | 988 | repo:_remote_pullback_2026_10_17/results/v20_statcheck_fm_vs_deg.json ｜ sub:results/v20_statcheck_fm_vs_deg.json | 远端拉回副本（物证面） |
| 58 | `1dadfaeb2c43` | 2 | 868 | repo:_remote_pullback_2026_10_17/results/v20_statcheck_fm_vs_rand.json ｜ sub:results/v20_statcheck_fm_vs_rand.json | 远端拉回副本（物证面） |
| 59 | `4af67e6cbe71` | 2 | 3449 | repo:_remote_pullback_2026_10_17/results/_trae_anchor_18_audit_20260917_193000.md ｜ sub:results/_archive_2026_09_18/_trae_anchor_18_audit_20260917_193000.md | 远端拉回副本（物证面） |
| 60 | `f2a655cd5e54` | 2 | 3467 | repo:_remote_pullback_2026_10_17/results/_trae_corpus_5_audit_20260917_193000.md ｜ sub:results/_archive_2026_09_18/_trae_corpus_5_audit_20260917_193000.md | 远端拉回副本（物证面） |
| 61 | `3184b30b7b0d` | 2 | 4253 | repo:_remote_pullback_2026_10_17/results/_trae_d7_v1_audit_20260917_190000.json ｜ sub:results/_archive_2026_09_18/_trae_d7_v1_audit_20260917_190000.json | 远端拉回副本（物证面） |
| 62 | `8ece24be6b8a` | 2 | 3281 | repo:_remote_pullback_2026_10_17/results/_trae_kimi_push_v3_audit_20260917_193000.md ｜ sub:results/_archive_2026_09_18/_trae_kimi_push_v3_audit_20260917_193000.md | 远端拉回副本（物证面） |
| 63 | `c5598b13c139` | 2 | 17363 | repo:_remote_pullback_2026_10_17/_september_workspace/deposon_team/verifier/v42_v2_2026_09_16.py ｜ sub:deposon_team/verifier/v42_v2_2026_09_16.py | 远端拉回副本（物证面） |
| 64 | `483602856618` | 2 | 1879 | repo:_remote_pullback_2026_10_17/_september_workspace/deposon_team/verifier/v42_v2_baseline_2026_09_16.json ｜ sub:deposon_team/verifier/v42_v2_baseline_2026_09_16.json | 远端拉回副本（物证面） |
| 65 | `b471190e579c` | 2 | 770 | repo:_remote_pullback_2026_10_17/_september_workspace/deposon_team/verifier/v42_v2_runs_2026_09_16.jsonl ｜ sub:deposon_team/verifier/v42_v2_runs_2026_09_16.jsonl | 远端拉回副本（物证面） |
| 66 | `a82881653520` | 2 | 465366 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_coze_online_v4_d7format_2026_09_26.pdf ｜ sub:results/_coze_〔IM〕_v4_d7format_2026_09_26.pdf | 远端拉回副本（物证面） |
| 67 | `2efdc3d7741d` | 2 | 3624 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_coze_paper_v1_summary_2026_09_17.md ｜ sub:results/_coze_paper_v1_summary_2026_09_17.md | 远端拉回副本（物证面） |
| 68 | `463fc7575663` | 2 | 9663 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/compile_verification.txt ｜ sub:results/_archive_2026_09_20/compile_verification.txt | 远端拉回副本（物证面） |
| 69 | `2d9edc8c7303` | 2 | 356123 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/fiction_that_feeds_back.pdf ｜ sub:results/_archive_2026_09_20/fiction_that_feeds_back.pdf | 远端拉回副本（物证面） |
| 70 | `543479649b3e` | 2 | 84388 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/fiction_that_feeds_back_source.md ｜ sub:results/_archive_2026_09_20/fiction_that_feeds_back_source.md | 远端拉回副本（物证面） |
| 71 | `ae07f5551e87` | 2 | 2637 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/p_i_curvature_audit_probe_results_2026_09_16.json ｜ sub:results/_archive_2026_09_20/p_i_curvature_audit_probe_results_2026_09_16.json | 远端拉回副本（物证面） |
| 72 | `fd38a2a1ea05` | 2 | 7617 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_content_A1_glm51.md ｜ sub:results/_archive_2026_09_20/review_content_A1_glm51.md | 远端拉回副本（物证面） |
| 73 | `a964defb923d` | 2 | 24843 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_content_A2_kimik3.md ｜ sub:results/_archive_2026_09_20/review_content_A2_kimik3.md | 远端拉回副本（物证面） |
| 74 | `0d36d7cd0589` | 2 | 30494 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_tech_B1_dsv4pro.md ｜ sub:results/_archive_2026_09_20/review_tech_B1_dsv4pro.md | 远端拉回副本（物证面） |
| 75 | `fe80bad08eef` | 2 | 13726 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_tech_B2_grok46.md ｜ sub:results/_archive_2026_09_20/review_tech_B2_grok46.md | 远端拉回副本（物证面） |
| 76 | `416dda94cb63` | 2 | 552 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/SHA256_MANIFEST.txt ｜ sub:results/_archive_2026_09_20/SHA256_MANIFEST.txt | 远端拉回副本（物证面） |
| 77 | `a729875c0c67` | 2 | 4712 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_archive_manifest_2026_09_18.json ｜ sub:results/_archive_2026_09_20/_archive_manifest_2026_09_18.json | 远端拉回副本（物证面） |
| 78 | `adc99e04ac53` | 2 | 454307 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_coze_online_v3_d7format_2026_09_18.pdf ｜ sub:results/_archive_2026_09_20/_coze_〔IM〕_v3_d7format_2026_09_18.pdf | 远端拉回副本（物证面） |
| 79 | `f3d4ec483599` | 2 | 41446 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_main_runner_2026_09_18.py ｜ sub:results/_archive_2026_09_20/_d05_main_runner_2026_09_18.py | 远端拉回副本（物证面） |
| 80 | `7a5be4aef9ac` | 2 | 13694 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_md_report_only_2026_09_18.py ｜ sub:results/_archive_2026_09_20/_d05_md_report_only_2026_09_18.py | 远端拉回副本（物证面） |
| 81 | `41bea33b9492` | 2 | 2088 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918.log ｜ sub:results/_archive_2026_09_20/_d05_sanity_3backbone_20260918.log | 远端拉回副本（物证面） |
| 82 | `0b7e50a8a036` | 2 | 2938 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_verify_sha_2026_09_18.py ｜ sub:results/_archive_2026_09_20/_d05_verify_sha_2026_09_18.py | 远端拉回副本（物证面） |
| 83 | `18984b04c45e` | 2 | 34134 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_deposon_v2scripts_reverify_worker_2026_09_18.py ｜ sub:results/_archive_2026_09_20/_deposon_v2scripts_reverify_worker_2026_09_18.py | 远端拉回副本（物证面） |
| 84 | `0769f60a0504` | 2 | 2678 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_final_sha_2026_09_18.py ｜ sub:results/_archive_2026_09_20/_final_sha_2026_09_18.py | 远端拉回副本（物证面） |
| 85 | `81bb1751be4c` | 2 | 4100 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch2_2026_09_18.py ｜ sub:results/_archive_2026_09_20/_fix_batch2_2026_09_18.py | 远端拉回副本（物证面） |
| 86 | `01e63e488ce2` | 2 | 3207 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch3_2026_09_18.py ｜ sub:results/_archive_2026_09_20/_fix_batch3_2026_09_18.py | 远端拉回副本（物证面） |
| 87 | `2efcd5ff42f1` | 2 | 8225 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch4_2026_09_18.py ｜ sub:results/_archive_2026_09_20/_fix_batch4_2026_09_18.py | 远端拉回副本（物证面） |
| 88 | `1c59e7b803fe` | 2 | 2214 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch6_2026_09_18.py ｜ sub:results/_archive_2026_09_20/_fix_batch6_2026_09_18.py | 远端拉回副本（物证面） |
| 89 | `389283c51275` | 2 | 4261 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch7_2026_09_18.py ｜ sub:results/_archive_2026_09_20/_fix_batch7_2026_09_18.py | 远端拉回副本（物证面） |
| 90 | `5057ccf97d6b` | 2 | 2249 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch8_2026_09_18.py ｜ sub:results/_archive_2026_09_20/_fix_batch8_2026_09_18.py | 远端拉回副本（物证面） |
| 91 | `2c2cc3ff542a` | 2 | 3524 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_d05_rescue_2026_09_18.py ｜ sub:results/_archive_2026_09_20/_fix_d05_rescue_2026_09_18.py | 远端拉回副本（物证面） |
| 92 | `3de722dc9e39` | 2 | 26990 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_glm_ftfb_deep_revision_2026_09_18.md ｜ sub:results/_archive_2026_09_20/_letter_to_glm_ftfb_deep_revision_2026_09_18.md | 远端拉回副本（物证面） |
| 93 | `f2934e5279e6` | 2 | 9717 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_mavis_full_mirror_request_2026_09_17.md ｜ sub:results/_archive_2026_09_20/_letter_to_mavis_full_mirror_request_2026_09_17.md | 远端拉回副本（物证面） |
| 94 | `49dde3059959` | 2 | 1393 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_doubao_4versions_diff_2026_09_17.json ｜ sub:results/_archive_2026_09_20/_probe_doubao_4versions_diff_2026_09_17.json | 远端拉回副本（物证面） |
| 95 | `93527eb7b2f7` | 2 | 2720 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_doubao_4versions_diff_2026_09_17.py ｜ sub:results/_archive_2026_09_20/_probe_doubao_4versions_diff_2026_09_17.py | 远端拉回副本（物证面） |
| 96 | `9bcfe80c0dd0` | 2 | 2371 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_doubao_emb_direct_2026_09_17.py ｜ sub:results/_archive_2026_09_20/_probe_doubao_emb_direct_2026_09_17.py | 远端拉回副本（物证面） |
| 97 | `f2818fc2ddff` | 2 | 2589 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_doubao_emb_via_proxy_2026_09_17.py ｜ sub:results/_archive_2026_09_20/_probe_doubao_emb_via_proxy_2026_09_17.py | 远端拉回副本（物证面） |
| 98 | `dce965058076` | 2 | 2841 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_teamo_via_proxy.py ｜ sub:results/_archive_2026_09_20/_probe_teamo_via_proxy.py | 远端拉回副本（物证面） |
| 99 | `e05555deb611` | 2 | 12919 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_i_curvature_audit_probe_runner_2026_09_16.py ｜ sub:results/_archive_2026_09_20/_p_i_curvature_audit_probe_runner_2026_09_16.py | 远端拉回副本（物证面） |
| 100 | `268225ccbb76` | 2 | 4397 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_reviewer_a_audit_tmp.py ｜ sub:results/_archive_2026_09_20/_reviewer_a_audit_tmp.py | 远端拉回副本（物证面） |
| 101 | `e11319f32dc5` | 2 | 2187 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_sanity_openai_more.py ｜ sub:results/_archive_2026_09_20/_sanity_openai_more.py | 远端拉回副本（物证面） |
| 102 | `63eb0a0aa102` | 2 | 2119 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_sanity_teamo_one.py ｜ sub:results/_archive_2026_09_20/_sanity_teamo_one.py | 远端拉回副本（物证面） |
| 103 | `888d02cd1443` | 2 | 3540 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_sanity_teamo_three.py ｜ sub:results/_archive_2026_09_20/_sanity_teamo_three.py | 远端拉回副本（物证面） |
| 104 | `4181a24c9ca1` | 2 | 277 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_teamorouter_smoke_tmp.json ｜ sub:results/_archive_2026_09_20/_teamorouter_smoke_tmp.json | 远端拉回副本（物证面） |
| 105 | `264f2bf5a3f2` | 2 | 6687 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_temp_volc_test.py ｜ sub:results/_archive_2026_09_20/_temp_volc_test.py | 远端拉回副本（物证面） |
| 106 | `0c9addf4a70f` | 2 | 675 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_tmp_inspect_22cap.py ｜ sub:results/_archive_2026_09_20/_tmp_inspect_22cap.py | 远端拉回副本（物证面） |
| 107 | `048ebc99177c` | 2 | 1029 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_tmp_inspect_5model.py ｜ sub:results/_archive_2026_09_20/_tmp_inspect_5model.py | 远端拉回副本（物证面） |
| 108 | `b0e2673f4a56` | 2 | 88584 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_v41_flash_rag_partial.bak.json ｜ sub:results/_archive_2026_09_20/_v41_flash_rag_partial.bak.json | 远端拉回副本（物证面） |
| 109 | `6952b3b02b96` | 2 | 8419 | repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/戴夫_FTFB双审包简报v3_2026-09-17.md ｜ sub:results/_archive_2026_09_20/戴夫_FTFB双审包简报v3_2026-09-17.md | 远端拉回副本（物证面） |
| 110 | `befdd577adce` | 2 | 1141 | sub:.trae/audit/compile_evidence/extract_tars.py ｜ sub:.trae/audit/compile_evidence/v2pre_h1h3_20260909/extract_tars.py | — |
| 111 | `4458ccf3d64a` | 2 | 24113 | sub:results/_worker_openrouter_rag_run.py ｜ sub:results/_archive_2026_09_24/_worker_openrouter_rag_run.py | — |

---

## §4 可减性判定

### §4-1 三类之判定（逐类给规则·⛔ 0 逐件代判）

| 类 | 组数 | 冗余件 | 留哪一件（确定性规则） | 判定 |
|:--|--:|--:|:--|:--|
| **跨区（repo↔sub）** | 95 | 102 | **留 `repo` 侧**（主仓为正身）、删 `sub` 侧副本；repo 侧同组多件时留**路径最浅**者 | **候选可减** |
| **`repo` 内同区** | 13 | 17 | 留**路径最浅**者（深度少者优先；同深度取字典序先者） | **候选可减** |
| **`sub` 内同区** | 3 | 3 | 同上 | **候选可减** |
| **零字节组** | 1 | 3 | 留 1 件（或全删——零字节无内容可失） | **候选可减**，⚠ 含 2 件为**今日在途棒之 0 字节产物**，宜俟该棒毕 |
| **禁令面涉及** | 1 | 2 | **⛔ 0 减** | **不可减** |

### §4-2 禁令面涉及（**先查惯例之产物·此为本节最要紧处**）

**`0a1e91d6f772`（2,292 B／n=3）＝ `_d05_sanity_3backbone_20260918_100110.json`**

- 该件即 **`MC-E4`「密钥门 1 件」**——在册禁令明载「**严禁 13 件永不上传**：dataset 隐私面 10 ＋ `results/_archive_2026_09_20/` 2 ＋ **密钥门剔除 1（`_d05_sanity_3backbone_20260918_100110.json`，2,292 B / `0a1e91d6f772`）**」（源：`letters\_commission_kimi_upload_2026_10_01_v0.2.md` 之 H4；`..._2026_10_18_v0.4_draft.md` 同表）。
- ⇒ **禁令锁定·⛔ 0 减**（其 n=3 全在 `_remote_pullback_2026_10_17\` 之拉回面，属**物证副本**，删任一即损证）。
- ⛔ 本代理**0 断言**该组是否另有在册「删除面」授权——已见 `..._2026_10_18_v0.4_draft.md` §9 载「密钥门件之远端两处残留已入删除面」，然**本地副本之去留未在其射程**，**归 PI**。

**全仓禁令核查之结论**：111 组中**仅此 1 组**触及在册禁令（`letters/` 全区 0 上传之面**0 组命中**；内部真册 0 组命中）。

---

## §5 汇总净减

| 项 | 件数 |
|:--|--:|
| 冗余件（上界） | **122** |
| **禁令锁定·⛔ 0 减** | **2**（`0a1e91d6f772` 之 3 件中留 1 ⇒ 冗余 2 件全锁） |
| **候选可减（上界）** | **120** |
| 其中跨区 | 102 |
| 其中 repo 内 | 17 |
| 其中 sub 内 | 3 |
| 其中零字节 | 3（⚠ 含 2 件在途） |

**与旧账「删面 ＝ 0」之差**：旧账判 0，本件判**候选 120 件**。差之根因**不是**事实变了，而是**判据换了**——旧账以「删之生幽灵」为否决（引用尺），本件以「件数为负担」为准（件数尺），且幽灵可登记故不再否决。

⚠ **本件之「可减」为候选级**：**活引用面未测**（见 §6-1），故未逐组核「删后须补几处旧→新登记」。⛔ 0 以本表充执行清单。

---

## §6 老实交代（⛔ 0 软化）

1. **活引用面未测**：本件只做**去重普查**，未对 233 件涉重件逐件测其路径式／裸名式引用数。⇒ 删后须登记之「旧→新」条数**未得**。此为最大限制。
2. **棒三试皆空，本件系主代理直算**：原派 evidence-auditor 之棒一 fail（`net::ERR_CONNECTION_RESET`）、一 canceled、一「succeeded 而盘上无件」（`succeeded≠落盘`）⇒ 主代理自建普查器直算。故本件**无子棒之独立复核**，其数字**须视为单一实现**。
3. **仪器仅单实现**：判重只跑一支脚本，未做跨实现（如 PowerShell `Get-FileHash`）交叉。
4. **`.tmp` 与 `results\.tmp` 全排除**：彼处亦有大量重复（旧账 99 组 204 件即含之），然**非上传面**，故不入本件；⇒ 旧账与本件之数**不可直接相减**。
5. **零字节之判**：零字节件之「全字节相同」系平凡真（空串哈希唯一），**不构成内容重复**；本件仅登记，⛔ 0 断言其可删性（其中 2 件为今日在途棒产物）。
6. **「禁令我已查」之射程**：本件检索之禁令源为 `letters\_commission_kimi_upload_*`（v0.2／v0.3／v0.4_draft）与 `letters\_internal_true_clue_book_2026_10_12.md`、`letters\_commission_coze_〔IM〕_closeout_pack_2026_10_12.md`。**⛔ 0 断言此为全量**——他处（如 `_commission_kimi_supplemental_sync_2026_10_18_draft.md` 之 `MC-E4`／`MC-E5`／`KD-SSC-*`）另有禁令面，本件**未逐面展开**。

---

*件止。主代理 mavis 直算 · 2026-10-22 19:26:27 · 0 移／0 删／0 改名／0 回改／0 联网／0 读凭据／0 落终判／0 代裁。*
