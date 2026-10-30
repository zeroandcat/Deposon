# 幽灵引用登记件（2026-10-21）

- 自路径：`〔幽灵引用·未上传:_ghost_reference_register_2026_10_21.md〕`
- 生成时点：2026-10-21 23:5x（本棒观测时点）
- 仪器：①四区全量 SHA-256 索引（`deposon-repo` 全域＋`deposon-sub`＋`GLM`＋`〔归档区〕`——实测 **48,084 件／26,840 个唯一 SHA-12**）；②「指纹＋所载字节」成对抽取式（`([0-9a-f]{12})…([0-9][0-9,]{2,9})\s*B`——依本仓引证惯例：指纹后随以所载字节）
- 扫描面：**469 件**（`pi_rulings\` 全 233 件 ＋ `results\` 根层自 2026-10-19 起 236 件）
- 索引之落盘（证据件·可复核）：`.tmp\_cleanup_sha_prefix_index_4zone_2026_10_21.txt`（4,008,208 B·`SHA-12 路径` 逐行；四区之 26,840 唯一 SHA-12 全列）
- 口径：**只判「在盘与否」**（可实测）——⛔ 0 判其为「灭失」／⛔ 0 判其内容／⛔ 0 改任何原引一字／⛔ 0 落五终判

## 1. 判定式与总表

判定分三档（仪器同一，仅结论面之三态）：

| 档 | 义（白话） | 件数 |
|---|---|---|
| OK | 指纹在四区在盘，且实体字节＝所载字节 | 782 |
| MISS | 指纹于四区（48,084 件）**0 命中** | 182 |
| SIZE-MISMATCH | 指纹在盘，然实体字节 ≠ 所载字节 | 2 |

候选对（指纹＋字节）共 **966**。

## 2. A 类：PI 点名之四件（逐条登记）

四件皆**真幽灵**（四区 0 在盘）。引用件数为全类型扫描（`md/json/txt/py/tsv/jsonl` 共 6,657 件）之实测。

| 指纹 | 所载字节 | 引用件数 | 引用之要（具名引用面） | 四区在盘 |
|---|---|---|---|---|
| `4228142806c5` | 22,733 B | 51 | `_batch7_deliberation_judgment_2026_10_13.md`／`_batch11_deliberation_judgment_2026_10_14.md`／`_bob_*_2026_10_12.md`（2 件）／`_c5_split_into_c5a_c5b_2026_10_17.md`／`_gd03_caliber_note_2026_10_20.md`／`_gd03_divergence_deliberation(_v2)_2026_10_21.md`／`_ge01_*`（4 件）／`pi_rulings v198/v199/v227` | **0** |
| `fddc14e6da27` | 15,264 B | 17 | `pi_rulings v214`（§4 指认面）／`_ge03_ge04_definition_deliberation_2026_10_21.md`／`_stage1_prereq_wave1_evidence_2026_10_20.md`／`_v172_adoption_effect_2026_10_20.md` | **0** |
| `4fa15c554d93` | 33,403 B | 14 | `_cluster_j_glm_62_adjudication_2026_10_19.md`（F-1 之「在仓实测同值」）／`_glm_unique_reply_117_triage_2026_10_19.md`／`_ge03_ge04_definition_deliberation_2026_10_21.md` | **0** |
| `cf04fc2f39db` | 14,904 B | 16 | `_ge03_ge04_definition_deliberation_2026_10_21.md`／`_stage1_prereq_wave1_evidence_2026_10_20.md`／`_r5_spec_pack_retrieved_2026_10_13\鲍勃…规格包.md` | **0** |

### A 类之三条要点（只述事实，不断其因）

1. **`4228142806c5`（《待裁项团队决议》本体·22,733 B／200 L）**：四区 0 在盘，与 `_batch11_deliberation_judgment` 之 KD-4（已知缺陷项）「全仓 2,158 件哈希扫描 0 命中」及 `_gd03_divergence_deliberation` 之「四盘面 MISS」同值。
2. **`4fa15c554d93`（Gemini4 `GE01` 理论输入回函之核验登记件·33,403 B）**：`_cluster_j_glm_62_adjudication_2026_10_19.md` L155 载「在仓实测同值（L212 逐字）」——然**今日四区 0 在盘** ⇒ 该「在仓实测」之表述**于本棒观测时点不可复现**（成因为何——移动／删除／名称不符——**未判**，⛔ 0 断言）。
3. **`fddc14e6da27`（爱丽丝_仓态进展与前置事实核查·15,264 B）**：与 `pi_rulings v214`-Q2 之「三面 0 实存（真缺件）」同值；`v214` 已明「其字面之核以转引层为据」。

## 3. B 类：引用 ≥3 次之 MISS（17 件）

| 指纹 | 所载字节 | 引用件数 | 首引件 |
|---|---|---|---|
| `fed0262d707a` | 11,639 B | 11 | `_gd03_divergence_deliberation_v2_2026_10_21.md` |
| `2befe7fc55bc` | 3,646 B | 11 | `_gd03_divergence_deliberation_v2_2026_10_21.md` |
| `ba5d1f3fc594` | 78,621 B | 6 | `_ablation_reading_2026_10_20.md` |
| `6512c6843d11` | 110,211 B | 6 | `_s2_confirmation_parenthesis_correction_note_2026_10_21.md` |
| `56c52db3f22a` | 10,212 B | 6 | `_pi_card_answers_register_2026_10_17_v46.md` |
| `275e480ba4d9` | 10,090 B | 5 | `_pi_card_answers_register_2026_10_14_v2.md` |
| `43a30e29b2be` | 2,672 B | 4 | `_eta_construct_c1_c16_recommendation_2026_10_20.md` |
| `da9b793fc73f` | 134,043 B | 4 | `_root_session_history_memo_main_2026_10_14.md` |
| `94c50da0bdd0` | 49,991 B | 4 | `_pi_card_answers_register_2026_10_20_v153.md` |
| `6bfa7b210a80` | 64,233 B | 3 | `_register_face_errata_2026_10_20.md` |
| `811793e86d7d` | 44,001 B | 3 | `_v164_adoption_effect_2026_10_20.md` |
| `d6e5f8a4c440` | 52,276 B | 3 | `_pi_card_answers_register_2026_10_17_v87.md` |
| `648bd68a2dbc` | 187,404 B | 3 | `_deposon_full_history_sub_2026_10_19.md` |
| `e269c707b0ca` | 160,603 B | 3 | `_pi_card_answers_register_2026_10_18_v99.md` |
| `d378062d508a` | 3,098,723 B | 3 | `_fake_kd_p3_readjudication_2026_10_21.md` |
| `a7c03b4a4006` | 38,393 B | 3 | `_pi_card_answers_register_2026_10_16_v41.md` |
| `92d7a9b8b877` | 316,601 B | 3 | `_kd_family_census_2026_10_20.md` |

## 4. C 类：引用 ≤2 次之 MISS（161 件）

| 指纹 | 所载字节 | 引用件数 | 首引件 |
|---|---|---|---|
| `d4da2693d309` | 230,027 B | 2 | `_v180_v182_adoption_effect_2026_10_21.md` |
| `da09c2142eca` | 184,418 B | 2 | `_glm_new_gaps_directive_effect_2026_10_19.md` |
| `57025a20f6e2` | 66,836 B | 2 | `_pi_card_answers_register_2026_10_17_v55.md` |
| `431ecdbd747e` | 244,512 B | 2 | `_root_session_history_memo_main_2026_10_14.md` |
| `62d03f6b5dfc` | 17,844 B | 2 | `_ge01_freeze_flow_execution_2026_10_20.md` |
| `1e2bb799db18` | 218,236 B | 2 | `_kd_h1_h7_disposition_draft_2026_10_20.md` |
| `2fbb82e6c7b4` | 145,838 B | 2 | `_pi_card_answers_register_2026_10_18_v99.md` |
| `809ab0c4164e` | 223,691 B | 2 | `_gd03_divergence_deliberation_v2_2026_10_21.md` |
| `1c6f9de452fd` | 117,027 B | 2 | `_pi_decision_backlog_consolidated_2026_10_21.md` |
| `24d06bf17b67` | 200,934 B | 2 | `_kd_history_pack_adjudication_2026_10_19.md` |
| `01883f894f49` | 38,110 B | 2 | `_cluster_k_eta_blockers_adjudication_2026_10_19.md` |
| `0e2b1cc71dfb` | 39,872 B | 2 | `_stage1_prereq_wave1_evidence_2026_10_20.md` |
| `5d7993240f75` | 4,101 B | 2 | `_o1_transcription_face_erratum_2026_10_20.md` |
| `2aa0fe91b2ec` | 98,393 B | 2 | `_c7_naming_deliberation_2026_10_21.md` |
| `b38ac3dfc867` | 2,763 B | 2 | `_root_session_history_memo_main_2026_10_14.md` |
| `27cb200220e0` | 45,548 B | 2 | `_harness_42b_drift_semantics_2026_10_19.md` |
| `8f911e5d6cee` | 38,383 B | 2 | `_eta_main_run_register_2026_10_20.md` |
| `2a50c9e0e3e5` | 184,364 B | 2 | `_independent_review_history_gaps_kd_2026_10_19_sub.md` |
| `169bbdb28759` | 2,895 B | 2 | `_fake_kd_p4_reversal_adjudication_2026_10_21.md` |
| `6d976fe9bba0` | 454 B | 2 | `_fake_kd_p4_reversal_adjudication_2026_10_21.md` |
| `18ee5064d9f2` | 37,888 B | 2 | `_pi_card_answers_register_2026_10_16_v41.md` |
| `1195c612de2a` | 40,106 B | 2 | `_pi_card_answers_register_2026_10_18_v98.md` |
| `fc74d20f0ca8` | 34,539 B | 2 | `_pi_card_answers_register_2026_10_17_v85.md` |
| `2833f89d623b` | 66,561 B | 2 | `_pi_card_answers_register_2026_10_18_v99.md` |
| `83fdfd910b91` | 73,478 B | 2 | `_pi_decision_backlog_consolidated_2026_10_21.md` |
| `e12ff3b17bd7` | 39,513 B | 2 | `_pi_card_answers_register_2026_10_17_v74.md` |
| `3deb8194a671` | 2,737 B | 2 | `_root_session_history_memo_main_2026_10_14.md` |
| `6f644de761a3` | 216,105 B | 2 | `_kd_h1_h7_disposition_draft_2026_10_20.md` |
| `7a097d7802d1` | 15,708 B | 2 | `_pi_card_answers_register_2026_10_16_v32.md` |
| `398e51a233ef` | 89,304 B | 2 | `_pi_decision_backlog_consolidated_2026_10_21.md` |
| `216f736d624e` | 90,822 B | 2 | `_t4t5_layer1_application_2026_10_21.md` |
| `5c7cbfec8a92` | 97,778 B | 1 | `_v155_adoption_effect_2026_10_20.md` |
| `301e682f04ce` | 143,469 B | 1 | `_v143_v144_adoption_effect_2026_10_19.md` |
| `0789214e950e` | 125,071 B | 1 | `_v150_adoption_effect_2026_10_20.md` |
| `143121c7e120` | 62,410 B | 1 | `_pi_card_answers_register_2026_10_17_v46.md` |
| `552aa383c51f` | 223,841 B | 1 | `_v180_v182_adoption_effect_2026_10_21.md` |
| `e86608904586` | 366 B | 1 | `_fake_kd_p3_readjudication_2026_10_21.md` |
| `132a5c1e25ed` | 46,985 B | 1 | `_stage1_experiment_gap_inventory_2026_10_19.md` |
| `55b6f19e3c1f` | 1,959 B | 1 | `_fake_kd_p3_readjudication_2026_10_21.md` |
| `2cba7dee5225` | 454 B | 1 | `_fake_kd_p3_readjudication_2026_10_21.md` |
| `1d1ab1f1d4f5` | 14,775 B | 1 | `_kd_h5_session_history_pilot_1of10_2026_10_20.md` |
| `f3838e36b897` | 149,295 B | 1 | `_v145_adoption_effect_2026_10_20.md` |
| `040f6bc886a4` | 30,290 B | 1 | `_pi_card_answers_register_2026_10_17_v69.md` |
| `82c90a7c4d69` | 6,646 B | 1 | `_fake_kd_p4_reversal_errata_2026_10_21.md` |
| `3d988cb71ee4` | 44,442 B | 1 | `_pi_card_answers_register_2026_10_17_v75.md` |
| `0487b78ad851` | 48,432 B | 1 | `_pi_card_answers_register_2026_10_17_v69.md` |
| `6d710fb5679d` | 182,719 B | 1 | `_independent_review_history_gaps_kd_2026_10_19_sub.md` |
| `cd8441417cae` | 62,487 B | 1 | `_pi_card_answers_register_2026_10_16_v35.md` |
| `59d9f421f5a6` | 67,074 B | 1 | `_pi_card_answers_register_2026_10_16_v36.md` |
| `087a18ec37d0` | 72,926 B | 1 | `_pi_card_answers_register_2026_10_17_v46.md` |
| `21f5284adcdc` | 132,833 B | 1 | `_root_session_history_memo_main_2026_10_14.md` |
| `517075064e45` | 62,558 B | 1 | `_v176_v179_adoption_effect_2026_10_21.md` |
| `10baaefe26fd` | 34,978 B | 1 | `_pi_card_answers_register_2026_10_17_v68.md` |
| `bead4fccb740` | 200,159 B | 1 | `_v143_v144_adoption_effect_2026_10_19.md` |
| `6d4cc73e617f` | 39,177 B | 1 | `_pi_card_answers_register_2026_10_16_v42.md` |
| `4b792e20f34f` | 115,416 B | 1 | `_v154_adoption_effect_2026_10_20.md` |
| `fa5145d90fe4` | 215,131 B | 1 | `_kd_history_pack_adjudication_2026_10_19.md` |
| `6f1fb2b43c30` | 3,422 B | 1 | `_glm_reply_pack_intake_verification_2026_10_19.md` |
| `2fc0385e55db` | 89,720 B | 1 | `_independent_review_history_gaps_kd_2026_10_19_sub.md` |
| `3da8e31baade` | 454 B | 1 | `_fake_kd_p3_readjudication_2026_10_21.md` |
| `304347705aa5` | 3,057 B | 1 | `_fake_kd_p3_readjudication_2026_10_21.md` |
| `5c6d558fa400` | 635,733 B | 1 | `_h5_session_census_2026_10_19_part2.md` |
| `da2f2dd35fb7` | 65,953 B | 1 | `_kd_mda8_f1_two_senses_adjudication_2026_10_19.md` |
| `abd08ec2150d` | 260,084 B | 1 | `_root_session_history_memo_main_2026_10_14.md` |
| `3bd65a80adc4` | 47,967 B | 1 | `_cluster_j_glm_62_adjudication_2026_10_19.md` |
| `66ad4ead0fa3` | 172,724 B | 1 | `_root_session_history_memo_main_2026_10_14.md` |
| `b7adb5afb0e9` | 1,424 B | 1 | `_pi_card_answers_register_2026_10_21_v197.md` |
| `266fceadec42` | 72,704 B | 1 | `_stage1_gap_exhaustive_audit_2026_10_20.md` |
| `614cbcdb9ff2` | 43,522 B | 1 | `_kd_eta_selection_verdict_2026_10_20.md` |
| `5e7c6bf0bf8b` | 3,425 B | 1 | `_glm_reply_pack_intake_verification_2026_10_19.md` |
| `8f06c5f70790` | 775,577 B | 1 | `_kd_eta_main_run_verdict_2026_10_20.md` |
| `7c4d9e7e4520` | 3,646 B | 1 | `_v176_v179_adoption_effect_2026_10_21.md` |
| `9845154a984c` | 68,553 B | 1 | `_pi_card_answers_register_2026_10_21_v188.md` |
| `ed9a552ae6cd` | 4,876 B | 1 | `_fake_kd_p4_reversal_errata_2026_10_21.md` |
| `12f5acb11e9c` | 165,599 B | 1 | `_root_session_history_memo_main_2026_10_14.md` |
| `4ff033ec583d` | 168,666 B | 1 | `_v145_adoption_effect_2026_10_20.md` |
| `3092bd586f82` | 128,498 B | 1 | `_v152_adoption_effect_2026_10_20.md` |
| `e17942840ef9` | 78,018 B | 1 | `_v155_adoption_effect_2026_10_20.md` |
| `25b01b5a6081` | 54,064 B | 1 | `_kd_h5_session_history_domain_caliber_2026_10_20.md` |
| `62f0a9df8e44` | 31,324 B | 1 | `_v146_adoption_effect_2026_10_20.md` |
| `d42071620490` | 26,609 B | 1 | `_root_session_history_memo_main_2026_10_14.md` |
| `3ebd023879a5` | 84,135 B | 1 | `_v157_adoption_effect_2026_10_20.md` |
| `69508d1965e9` | 107,084 B | 1 | `_v166_adoption_effect_2026_10_20.md` |
| `1e15e7611597` | 115,240 B | 1 | `_v159_adoption_effect_2026_10_20.md` |
| `27e6c78a56ee` | 4,022 B | 1 | `_v151_adoption_effect_2026_10_20.md` |
| `b36625682501` | 120,259 B | 1 | `_root_session_history_memo_main_2026_10_14.md` |
| `bd33065703be` | 124,295 B | 1 | `_v150_adoption_effect_2026_10_20.md` |
| `52cc36328a4b` | 39,872 B | 1 | `_v172_adoption_effect_2026_10_20.md` |
| `0a53046bc52d` | 44,064 B | 1 | `_harness_42b_drift_semantics_2026_10_19.md` |
| `a8c0349f4e42` | 277 B | 1 | `_fake_kd_p3_readjudication_2026_10_21.md` |
| `2bac80dfb235` | 2,093 B | 1 | `_fake_kd_p3_readjudication_2026_10_21.md` |
| `b32ca40ec123` | 15,707 B | 1 | `_pi_card_answers_register_2026_10_18_v104.md` |
| `c3ce2bb53af1` | 28,097 B | 1 | `_pi_card_answers_register_2026_10_17_v56.md` |
| `d357b3b05776` | 1,382,964 B | 1 | `_eta_preexp_run_register_2026_10_20.md` |
| `0f933318d5a1` | 137,346 B | 1 | `_v169_adoption_effect_2026_10_20.md` |
| `ae7226f9671a` | 43,692 B | 1 | `_h_exact_enum_killline_prereg_2026_10_21.md` |
| `e01b6a3bfb3c` | 3,320 B | 1 | `_kd_identified_defect_attribution_caliber_2026_10_20.md` |
| `129223e7c433` | 26,292 B | 1 | `_pi_card_answers_register_2026_10_16_v41.md` |
| `ea78431b6a89` | 349,714 B | 1 | `_ablation_reading_2026_10_20.md` |
| `33478e048831` | 165,732 B | 1 | `_v153_adoption_effect_2026_10_20.md` |
| `52772769c459` | 366 B | 1 | `_fake_kd_p3_readjudication_2026_10_21.md` |
| `9399019d4f8e` | 168,605 B | 1 | `_glm_reply_pack_intake_verification_2026_10_19.md` |
| `509e17caa955` | 228,636 B | 1 | `_v180_v182_adoption_effect_2026_10_21.md` |
| `eb5e7433c255` | 48,115 B | 1 | `_pi_card_answers_register_2026_10_18_v98.md` |
| `5c6d558fa400` | 652,755 B | 1 | `_kd_h5_session_history_pilot_1of10_2026_10_20.md` |
| `88acbcfd828a` | 173,497 B | 1 | `_v153_adoption_effect_2026_10_20.md` |
| `54272d42f5c9` | 11,639 B | 1 | `_v176_v179_adoption_effect_2026_10_21.md` |
| `1e46ab68a335` | 2,553 B | 1 | `_v146_adoption_effect_2026_10_20.md` |
| `f19b45ca5335` | 70,189 B | 1 | `_kd_h1_h7_disposition_draft_2026_10_20.md` |
| `16ef897639c4` | 72,934 B | 1 | `_pi_card_answers_register_2026_10_17_v46.md` |
| `789a11aa9a2a` | 177,334 B | 1 | `_root_session_history_memo_main_2026_10_14.md` |
| `46c8c95a7a4f` | 222,463 B | 1 | `_v155_adoption_effect_2026_10_20.md` |
| `b552c38f6b2d` | 60,655 B | 1 | `_pi_card_answers_register_2026_10_17_v47.md` |
| `fc5f722a09f5` | 454 B | 1 | `_fake_kd_p3_readjudication_2026_10_21.md` |
| `d1d86cb6a33e` | 74,935 B | 1 | `_v149_adoption_effect_2026_10_20.md` |
| `31cf2891cf21` | 87,389 B | 1 | `_v155_adoption_effect_2026_10_20.md` |
| `ad24d5c8e2c6` | 2,096 B | 1 | `_fake_kd_p3_readjudication_2026_10_21.md` |
| `130d42ffbef2` | 54,499 B | 1 | `_kd_h5_session_history_domain_caliber_2026_10_20.md` |
| `fe6909a580f4` | 53,612 B | 1 | `_pi_decision_backlog_consolidated_2026_10_21.md` |
| `2696af62e3ee` | 12,742 B | 1 | `_root_session_history_memo_main_2026_10_14.md` |
| `b7fa15fa25c1` | 170,921 B | 1 | `_root_session_history_memo_main_2026_10_14.md` |
| `b2e2d53b3c16` | 39,007 B | 1 | `_pi_decision_backlog_consolidated_2026_10_21.md` |
| `ca71c02589e7` | 60,649 B | 1 | `_pi_card_answers_register_2026_10_17_v47.md` |
| `9a0d8b5ec2a0` | 91,102 B | 1 | `_pi_card_answers_register_2026_10_17_v46.md` |
| `3f7f3b76ee19` | 114,115 B | 1 | `_pi_card_answers_register_2026_10_17_v51.md` |
| `f71ae4210f50` | 9,385 B | 1 | `_glm_reply_pack_intake_verification_2026_10_19.md` |
| `b440f527eb54` | 10,090 B | 1 | `_harness_42b_drift_semantics_2026_10_19.md` |
| `3670568a585a` | 7,557 B | 1 | `_kd_epw3_crw3_ffrep1_adjudication_2026_10_19.md` |
| `9143181f395a` | 1,906 B | 1 | `_fake_kd_p3_readjudication_2026_10_21.md` |
| `9935be2c6552` | 46,884 B | 1 | `_pi_card_answers_register_2026_10_17_v68.md` |
| `f616e00cf299` | 94,447 B | 1 | `_pi_card_answers_register_2026_10_17_v46.md` |
| `d80cf1804e80` | 3,883 B | 1 | `_v159_adoption_effect_2026_10_20.md` |
| `45d343b998f0` | 22,498 B | 1 | `_pi_card_answers_register_2026_10_18_v98.md` |
| `ff1950e09388` | 59,342 B | 1 | `_glm_reply_pack_intake_verification_2026_10_19.md` |
| `f52d6d66c131` | 54,474 B | 1 | `_kd_h5_session_history_domain_caliber_2026_10_20.md` |
| `c6a91d35843e` | 5,920 B | 1 | `_deposon_full_history_sub_2026_10_19.md` |
| `128b4167afd5` | 215,227 B | 1 | `_v180_v182_adoption_effect_2026_10_21.md` |
| `4217ad8c1381` | 219,360 B | 1 | `_v153_adoption_effect_2026_10_20.md` |
| `680a7ce4cf08` | 148,103 B | 1 | `_v153_adoption_effect_2026_10_20.md` |
| `e0b891f01a6b` | 25,159 B | 1 | `_pi_card_answers_register_2026_10_16_v32.md` |
| `2ea190308493` | 52,974 B | 1 | `_pi_card_answers_register_2026_10_16_v31.md` |
| `7d1482b239c7` | 50,344 B | 1 | `_pi_card_answers_register_2026_10_16_v31.md` |
| `1307a6c44fbe` | 518 B | 1 | `_fake_kd_p4_reversal_errata_2026_10_21.md` |
| `354e51cfe6d4` | 45,778 B | 1 | `_pi_card_answers_register_2026_10_20_supplement_4cards.md` |
| `3124456ce940` | 93,555 B | 1 | `_fake_kd_p4_reversal_errata_2026_10_21.md` |
| `bead4fccb740` | 199,159 B | 1 | `_kd_history_pack_adjudication_2026_10_19.md` |
| `debf0de9ac50` | 1,004,131 B | 1 | `_kd_h5_session_history_pilot_1of10_2026_10_20.md` |
| `7e1e2209a013` | 3,971 B | 1 | `_v151_adoption_effect_2026_10_20.md` |
| `fb90fd5e6988` | 36,612 B | 1 | `_kd_eta_selection_verdict_2026_10_20.md` |
| `6cb324e4c646` | 70,534 B | 1 | `_kd_h1_h7_disposition_draft_2026_10_20.md` |
| `2764e9e0cf8b` | 84,694 B | 1 | `_v156_adoption_effect_2026_10_20.md` |
| `aa2968356e41` | 59,426 B | 1 | `_pi_card_answers_register_2026_10_17_v46.md` |
| `193f22f69988` | 3,365 B | 1 | `_fake_kd_p3_readjudication_2026_10_21.md` |
| `5fe01006406f` | 84,676 B | 1 | `_v155_adoption_effect_2026_10_20.md` |
| `12ab21c73db8` | 150,494 B | 1 | `_root_session_history_memo_main_2026_10_14.md` |
| `3f1ce14b0f10` | 140,072 B | 1 | `_root_session_history_memo_main_2026_10_14.md` |
| `a1a4f4e1e64e` | 119,961 B | 1 | `_v150_adoption_effect_2026_10_20.md` |
| `192bd0e58826` | 110,673 B | 1 | `_v150_adoption_effect_2026_10_20.md` |
| `d2cadc7e7c23` | 5,253 B | 1 | `_v159_adoption_effect_2026_10_20.md` |
| `64a86ad94490` | 16,644 B | 1 | `_glm_reply_pack_intake_verification_2026_10_19.md` |
| `0423aecb53ec` | 366 B | 1 | `_fake_kd_p3_readjudication_2026_10_21.md` |

## 5. SIZE-MISMATCH（2 件）

| 指纹 | 所载字节 | 实体字节 | 实体路径 | 引用件数 |
|---|---|---|---|---|
| `1442a1296936` | 423,375 B | 510,810 B | `\results\_root_session_history_memo_2026_10_14.md` | 1 |
| `b32ca40ec103` | 15,707 B | 26,832 B | `\.tmp\pk_body1.md` | 1 |

- `1442a1296936`：所载 423,375 B vs 实体 510,810 B——引用面为 `_root_session_history_memo_2026_10_14.md`（该件后续有追加之迹，字节增长**可解释**；⛔ 0 断言其因，只记数值差）。
- `b32ca40ec103`：所载 15,707 B vs 实体 26,832 B；而 C 类另有 `b32ca40ec123`（所载同 15,707 B）——两串**仅一指之差**（`ec103` / `ec123`）⇒ **疑为转录之笔误族**（⚠ 未判，只列并置）。

## 6. 本棒删除而生之新增幽灵（15 件·自报）

本棒依「清噪声」删去 `.tmp\__pycache__\` 之 15 件 `.pyc`（Python 字节码缓存；源 `.py` 全部在盘，可再生）——其名于 133 件 md 中被引用（逐名 1–23 处）⇒ 删除后该 15 个**名**成新幽灵（内容面无损：字节码可由源重生成）。逐件见 `_cleanup_noise_register_2026_10_21.md` §3；恢复通道＝`mavis-trash`（可恢复）。

## 7. 处置（逐条）

1. **一律只登记**：⛔ 0 改原引一字、⛔ 0 补引、⛔ 0 删除引用处（沿「勘正件拉平·⛔ 0 回改正文」之体例）。
2. **A 类**：其四件之在盘性＝**事实登记**；其为「真缺件（外部未交付）」抑或「名称不符／他处」＝**未判**（两读并置，⛔ 0 择一）。
3. **B／C 类**：本棒之判定射程止于「四区 0 命中」——**⛔ 0 断其不存在**（另有会话库／远端面不在扫描面内）；凡须消解者，归「设法辨明」之列（派专棒或俟 PI 给件）。
4. **MISMATCH**：只记数值差，⛔ 0 判孰为真（原件与引用面皆不回改）。
5. 一切**⛔ 0 联网**（远端面未测——其测归 PI 之径）。
A '
A 

1. 扫描面限于 `pi_rulings\` 全 ＋ `results\` 根层 10-19 起——`results\` 之 1,180 件更早件与 `.tmp\` 3,460 件**未入本轮成对抽取**（其内之幽灵引用未扫，⛔ 0 视为「无」）。
2. 判定依赖「指纹＋字节」成对式 ⇒ **只载字节之引**（如「`abcdef123456`·N B」）方入扫；纯指纹引或纯名引**不入**（故 182 为**下界**，非全数）。
3. 四区索引含 `.tmp` 与归档区 ⇒ 「0 命中」之射程**已含**工作面与归档区；会话库（session storage）与远端面**不在内**。
4. 逐件引用数系 md/json/txt/py 全类型文本匹配（Ordinal）；⛔ 0 判引用之效力（引≠采认）。
5. 一切数值系本棒实测；⛔ 0 沿用他件自报之数（除已注「同值」者，其同值亦经本棒复核）。

*件止。执行棒（`mavis`·deposon 执行面）· 2026-10-21 · 载体之三（幽灵引用）。⛔ 0 回改既有件 · ⛔ 0 移 · ⛔ 0 代裁 · ⛔ 0 落终判。*
