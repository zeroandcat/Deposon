# DEEMPHASIS SHA Drift Register — 批B6b（⑥b 子批：results/ 判定链/工件/底账/归档 88 件）

- 执行日：2026-10-06（CST）｜执行人：鲍勃-实验分析师（代 KIMI，PAT 推送）
- 开工 HEAD：`afd39a5`（⑥a 后）｜基线 tag：`deemph-baseline-20261006`
- 现场枚举（附录 C 分 token 正确口径）：`results/` 并集＝**88 件**。与信载 §3.6 ⑥b 桶计数 100 差 12 件，**根因＝批⑤ B-3 回写连带清零**（`_mirror_manifest.json`、`_movedout_manifest_2026_09_21.json`、`_archive_manifest_2026_09_20.json`、`_archive_manifest_deposon_sub_2026_09_23.json`、`_ghostref_copy_log_2026_09_23.json`、`_kimi_push_v3_manifest_batch5/14_*.json`、`_v3_v4_achievements_inventory{,_3dir}`、`_v3_v4_ghostref_reconciliation`、`_v4_maindir_cleanup_manifest_v2/moves_ledger_v6`、`_v5_sub_artifact_ledger_history_r3/r4` 等，基线 token 仅为 wechat 路径字面，批⑤回写后清零——非漂移非范围变动，全程在 B5 表 2 台账可溯）。基线 tag 上 `results/` 并集实测 93 件 − 批③④⑤替换清零 19 件 ＝ 74（混合枚举污染版）→ 正确口径（分 token）88 件；93 vs 信载 100 的 7 件差为信载规划口径微差（全仓 229 并集实测与信载精确一致，见 B6a/操作清单）
- 红线自检：R1 判定链读数 0 触动（numstat 全对称；判定词行成对只替人名）／R2 0 历史改写／R3 0 凭据

## 替换统计（§2 口径）

- 王老师×132→外部顾问；WeChat×98/wechat×31/微信×1→线上（叙述形）
- 实名+机构整串消化×1：`_coze_paper_v1_draft_2026_09_17.md`「中国人民大学高瓴人工智能学院王子贺老师」→「外部合作导师〔匿名〕」
- 王子贺×2→外部合作导师〔匿名〕（文献方向叙述）
- 路径形×50（可逆推）：D3_WECHAT_MIDTERM_2026_09_09_actual×6（悬空引用，目标不在仓）；_v4_commission_wechat_report_coze×38（letters/ 目标不在仓）；WANG_TEACHER_PROGRESS_REPORT_2026_09_11.md×6（仓外件名引用）
- 英文名形：Wang-teacher×4→external advisor（catalog 描述列）
- 合计 319 处替换

## R1/存疑保留项（不替换，报备）

- **保护键名×12**：`no_OpenRouter_TeamoRouter_V41Flash_GPT6_agent_plan_WeChatAPI`（`boss_pa_*`/`deposon_*`/`skill_*` 等 JSON/脚本判定键）——判定链机器读数面，按 R1 红线 0 触动保留，是否改键名待 PI 拍板（涉 verifier 脚本兼容）
- **Renmin 存疑×2**：`_glm_five_items_suggestion_table_2026_10_01.md` 已发表件元数据「School of Chemistry and Life Resources, Renmin University of China」（arXiv 2609.09001 Comments 栏单位字面）——该件自身标注「⚠️ 涉可识别信息，是否照录由 PI 按 H8 定」，按 §2 细则存疑保留报备

## 逐件 pre/post SHA-256

| 目标件 | 改前 SHA-256 | 改后 SHA-256 |
|---|---|---|
| `_september_workspace/results/_archive_2026_09_18/_trae_5audit_aggregated_2026_09_17.md` | `43265e4bf2bef6d7ac19a6b1714be4eb3c2f8bb8759ed1ebbfea25802f96c63f` | `4063f9a1882ccb9d3c6ff9b3a5fb8dbc92ddceccfaa8938a45afe4c1ec6fa783` |
| `_september_workspace/results/_archive_2026_09_18/_trae_code_improvement_v2_2026_09_18.md` | `86a243d90e8aceef58eed2f01b1df28830f3d22deeae7e82f4d1eefbf07c4c6e` | `cd56db6ad62a800649469f210c4357553f2e423c6e4028b643d33663d5971740` |
| `_september_workspace/results/_archive_2026_09_20/REVIEWER_B_TMP_RERUN_2026_09_15.md` | `8cd736ba9f9188c516a981dcb3147a6a3f99f7a29b92236fbd3e7e707c357dd2` | `ceb8f595a9112b5cc27521591ff31de0b3ad7be04bb014ebfcadd8071605dd39` |
| `_september_workspace/results/_archive_2026_09_20/_coze_paper_v1_双审报告_2026_09_17.md` | `c3de25e6df57c19536082c16ed79ed1aeee6caa84724b746d1465a42080a391d` | `dc761bd8b85d77f1b6a2fa0ac7fb1c8f5bb1444fef1829e94b904cbf86b5d065` |
| `_september_workspace/results/_archive_2026_09_20/_ftfb_pass2_results_limitations_audit_2026_09_17.md` | `cfab992cf9391bd09d965408ded4e5c6c6cbac396874cc324436ab93e0452464` | `5610a549e1167502110e377e1f5fca501fa93a7df0c1cfc6e9b19c7069d32d1e` |
| `_september_workspace/results/_archive_2026_09_20/ftfb_pass1_background_methodology_audit_2026_09_17.md` | `70bd41d9722dfda16657314ffb69eff9b0e332cddf11fd963c4a9371315fe168` | `7243192d86be815bef9e5137ea7220f1b12a896c4ae9d6e1608fbbd7abdb078a` |
| `_september_workspace/results/_archive_2026_09_24/_v4_pi_decision_questionnaire_2026_09_21_v1.1.md.bak_2026_09_22_gB_post.md` | `07ca9ee8e1bbc21c1294e7da809bb238def8c024bfa98e3f25612c36bd607861` | `6b45fba92db85f19ef74299c8bd92a53bd3aa656ad255ba431ab08292f477e77` |
| `_september_workspace/results/_archive_manifest_non_upload_2026_09_23.json` | `b899103853ca8132f7f7dfa11b4c7cf250ba2828357b837a598918306313e86d` | `e0edc34ead9a23b4557e99583041adafecc0dfbb57438e65c9a447faf883a37c` |
| `_september_workspace/results/_archive_manifest_non_upload_v2_2026_09_28.json` | `84eef669234bb1c4bea93d207ac19c94a9c19fa53c2fe11a3bd783828cda0c15` | `31e2f3ff9bdbd6621cfe7d2b706cd173effe6a52549434bc5bad4e4b5962ffac` |
| `_september_workspace/results/_archive_manifest_non_upload_v3_2026_09_28.json` | `a2e4c5a9b71302cf3e62a19e541e4b941d5266b3bbe8879115c4db21d9cfa42f` | `ac3a79b0ac8b2575031c4109cf44bb7b35ee5a59d61018a5b825aaa75ee5262f` |
| `_september_workspace/results/_clearance_evening_round_register_2026_09_29.md` | `9c5543961e27570349c17b5d4a9ed1bf9d617ead8b5aa526bc55d01604972793` | `db068fdaa8fb56f6b054e74df34a072a07e9b56203bcfe48df5c3d734b66561b` |
| `_september_workspace/results/_coze_paper_v1_draft_2026_09_17.md` | `c08e7abf5ee3601f8e19ffc8a28e6f27dd58e7d1984b950802b1074ca1b486cb` | `d7ad63adbcf2bc8417ef61446410596429a5f28dc3eeb09a8c78cf956661185b` |
| `_september_workspace/results/_d8_boundary_revision_register_2026_09_30.md` | `b46370bb9e3bac693ad24a599a3feb78bf68a7866055c40cda3d66e1c8a79413` | `fb095e3588d8c43b83395f1760ebd2cec224de428f9686bed4c57a4eda347c34` |
| `_september_workspace/results/_d8_dup_overlap_disposal_2026_09_30.md` | `de8691727842108f1a87cb2e4f940181785485cfbbfb9ba0003f2448f4a5c2a2` | `9ab24979e288954ec7969094c72b16283e9b930c6a88d391fedcfe5ed872e6af` |
| `_september_workspace/results/_d8_supplement_open_questions_2026_09_30.md` | `579b375e95085799c544bda2026b492bea47e6dfa54e627929d85f350fa76b12` | `2b8d5ada375c914a98616548c6acc54ac9e7a659ce74fa60619f5e1ea2e45a33` |
| `_september_workspace/results/_forgotten_recovery_register_2026_09_29.md` | `d78be896bcb6a843b15d6932477bc0ab5b5d97540f55fd1fd3ce170c82e7c185` | `4a32765ed9999fc45fa7c2e2bc152c6d453d6656b4efc5a4f38bcdbe64cff002` |
| `_september_workspace/results/_ftfb_v3_pass1_audit_2026_09_18_corrected.md` | `ecb4065706151e7fefdb6f28b93e3f5125d31af918b1d306037b82d335e568de` | `2a943e753126bd342e56e313a76d60229306b2ac147e48f3fb007f571db40854` |
| `_september_workspace/results/_ftfb_v3_pass2_audit_2026_09_18_corrected.md` | `413ddb0bd00e873481194a6cde398d8bd24953b188389661cde2bebe6ce9458d` | `945b04e067ba4ad7d47344dfc7c6047e1aa2cec3296c26ac327eef9bdd60d5b0` |
| `_september_workspace/results/_glm_five_items_suggestion_table_2026_10_01.md` | `f2b1359be37d6b7cc27f4676149c1295334c28ab32a18df95fe09472ed978982` | `f2b1359be37d6b7cc27f4676149c1295334c28ab32a18df95fe09472ed978982` |
| `_september_workspace/results/_glm_response_v2_template_2026_09_18.md` | `972401e056f6da8207c7aeb9a0cc74b3735158cc465c9f98b4c23ab25e09e63d` | `0474099e4c3473d5b39e574a6925c6927eef8fccfe62d7b81c04b0bbdf6f2bf4` |
| `_september_workspace/results/_p_k_v3_glm_fpr_audit_report_2026-09-17T08-23-41Z.md` | `71d5c23d9f760f7a155f3387318e3cd2410b79799b9150b80f9ec13f4183c5bd` | `43c6d01a71af42d9dfc168a04bbe309f99288d5aac3ab39a016f19d10a4b7abb` |
| `_september_workspace/results/_p_l_v3_phase1_report_20260917_132341.md` | `b41a17eda169dd32d98285561f3b2b07c84aa8bddd55e8ca5dd46b9e28934c0e` | `2f178ae14a9cbe0c008fc205ace68f97d0ab1ecc444a23841ac3ed8d17bb04c6` |
| `_september_workspace/results/_p_l_v3_phase2_report_20260917_142748.md` | `58e15c07af3381fc03aae60652aefd8c494015f9efd9b75f9e228d5042621638` | `37372b5da56d1cdf7a76b784be3ee18339f30602541d521302e9b0dce13b1a93` |
| `_september_workspace/results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133358.md` | `54859cf2217a207a3d64d16e84eac061ce37a7d0322eb32093bed2311b7e7f04` | `9daff333ef906df37fc896b484680cc22d4fb03dc8ab13456301a7f42b40a8a4` |
| `_september_workspace/results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133512.md` | `c350e420eca6869bab0ab4225aa9e1531c9636eecb577c179bfd339b680c8509` | `3514cdbedaea10fecf5c04f8fcda59eea9e750d83e3c393c746f7fa292ecfa11` |
| `_september_workspace/results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133705.md` | `772112cf5bd416a9ff44cb7fe1525fd617a29668d4a6ed0f5503e02699bdfc53` | `94a5eb881a0788af39730220e2750dc3096f8aa6af612b31f6756672bfc228c0` |
| `_september_workspace/results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133726.md` | `d7f03fde4067ae887fce3d370197fd6cc138b9794e0eb74ecbadd0aed80e75ba` | `29c17850bfbf3dd950e2355bac85faf852bb31ba89ca2d013c9d006805f16218` |
| `_september_workspace/results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133852.md` | `d66388b6532d6f63701070730fb3cae29989b7dbbe5c737f7e38514f0ba51b51` | `4278fc571f3046eded9980cbb81a122360cdd387af35d45d8e6f1f9f26bd3a42` |
| `_september_workspace/results/_pc_d1_d3_2026_09_15.py` | `09c7c4ddbb394e2a78485a2e121ffc3fdb1ca1e6adcf720106297be8e5ed5016` | `3131e5b0519d928a4cfa2fbd304073c88aba2dcfeb0efa42c9c7428409da1768` |
| `_september_workspace/results/_plan_v3_pending_verify_2026_09_30.md` | `7374004d6075bbbb4ee293b6ad4e9da6f068e1aee5828159cb90252b865ae14c` | `83b9968c885aa8e489adf9230e2412eb80ab76ff370c71939358dd889a9a4057` |
| `_september_workspace/results/_v3_recheck_21_rescript_2026_09_27.md` | `04f6ecd482b9561b284eff5d95ccbc124bb971f749eae153f24a0b5944d111aa` | `481dad5b3e4c0bcddce5ccfdeb41a4fe042339837402e0877bbc9eb3fe5e11e7` |
| `_september_workspace/results/_v3_recheck_21_result_2026_09_27.json` | `354ae9c14fe2f0dbc493fbb93d59bc557e39ddae6451c251e0e31c8c4f12b72a` | `1aa1e69a60d9ee6656fc7a681c1daa933df323df43e265f7ceaaf4dbcc65ae90` |
| `_september_workspace/results/_v3_recheck_prereg_v1p1_2026_09_27.md` | `bcc3cee23e8276d33e1c9077b27b1544ff32a07608432a8b0d7138cca6585a8a` | `83857a3e3b569d14f6c78bc19ebe4e8e4fe41cfdbafcf4707a2679568c6a2559` |
| `_september_workspace/results/_v3_v4_achievements_inventory_2026_09_24.md` | `4322da59b8161bda25f8c5a719f06213cde944fee4c88903398d96aaf73ab5d7` | `9ac36fc16c105761b0d2aecc71634f0ba21fb04e929bc4478a25eb35ebbcf304` |
| `_september_workspace/results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | `8483f9b18d704dce949d39f72cb1207ff49ac170e0189b76e494906e7ef48eca` | `60e3dff38283e73bc42b82c2e4d9ced748c173df2c899ab93283f91cc6d09451` |
| `_september_workspace/results/_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md` | `c64146c4ccacfb190eed325c7dfb9c8ff149ae89d6b5315c487c96e58e842709` | `d2a432f36a7e9bc078a6aac7233b1aaa02ee0ee9443a823b834529c992bf3189` |
| `_september_workspace/results/_v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md` | `24c64cc239077f3a07077d3529d619e19f25798f18b0e9663f0f2292dbf933a9` | `894c7abb45f0a1c0626e3ab544f9ea8b4f19d778cdfee24d2941bc937662dc29` |
| `_september_workspace/results/_v3x_d0_5_aggregation_2026_09_17.md` | `ddf0d1aa96d2920a0311b89dba414f3d63e86cfbf653b166f3a1144f5456c5ca` | `91cf5292a5a914d811ba10185a38d8549ab1107682f7468b8680db3a0ac19dda` |
| `_september_workspace/results/_v3x_d0_5_experiment_invitation_2026_09_17.md` | `d8f2b99aa5270a7e91eec05e8e6d68b5a9c0290c9a2bbc6b6a2436da5f8f90e2` | `5b3e0b0d286ba18925e37db5f9e779f5f6a5cae1275b488769648033aa4c949b` |
| `_september_workspace/results/_v3x_d0_5_proposal_coze_2026_09_17.md` | `759c25b21ed416fb0e87f2630f4361370a774171f88f7da4ad41c495d81d8b85` | `41eb405548e14d8d712d10d07947c7032bdaefdb56a2e5fc9f9b62366bd86b03` |
| `_september_workspace/results/_v3x_p_l_v3_external_spec_2026_09_17.md` | `6a5b6eb635f0443dbc74a26ef967ec2902763f61fd1f8e21d97c8b5d8988acf1` | `8085394f514149d3380a00a7ac29c9a869340b7e73ac6c6a5a3aa6320f339fe5` |
| `_september_workspace/results/_v3x_p_l_v3_summary_mistral_large_2512_20260917_115049.md` | `183205baa9ac946b0ef6cdc997a70923887792ad24c4484880ddfca40479eaf6` | `7ca77db1194db426a3e26c75ddce4b7cb4effaaf663db9da63f1932b98aeba37` |
| `_september_workspace/results/_v4_design_integration_2026_09_21_v1.1.md` | `fb5656993071abc2809d6ceab1990603999ac05a0943105dd8dd2e4e97546aca` | `463d4405763c2930c4bd4636661bc09211f7fe8093ecf58b9350650daa04d893` |
| `_september_workspace/results/_v4_gA1_experiment_outline_2026_09_22.md` | `f4a6bdd43962be9c40b5271fe511f71235e198ff7cda7b3b1bb1caeaff2da1e3` | `20a5f23f700445c38ff67b1fad6342892cd8d2a6425baf9edb921a3e3b1ceaf5` |
| `_september_workspace/results/_v4_gA1_terminology_draft_2026_09_22.md` | `0a2caf0a2bd2063c8fd92f8616032985a25dbf6b10e7ca66f4c83f65e6a76102` | `4f3287bc5b986cd411a8c78fcd01dce5121d68b67f8d86e3e8bf75b7ac9e00d8` |
| `_september_workspace/results/_v4_gA3_seeds_judgment_draft_2026_09_22.md` | `9119bb791dc16dd102ab4b7a36077f910aeef140ef8246a981a1dfe2001d7997` | `e451cbff8638aad7a0698c11736cda28651fbc1824a5b1aa9db995a16c998011` |
| `_september_workspace/results/_v4_group_b_explore_subs_integration_2026_09_22.md` | `588b45430e88732b739dec5b073e5f13c5b49d713d6f546b0e690fcc32d730e7` | `c93221cb34db995a1c690587de500599e1b12288bcbf8935a5efb2caa53e6c37` |
| `_september_workspace/results/_v4_maindir_cleanup_manifest_2026_09_24.md` | `32cc61d394f21dd45f626f362e232482fdcd7242343c977b08000fe94f17acb0` | `a3d16ef2b9d3f883f823e416e91889609386f2bef203147b426077503fdb451f` |
| `_september_workspace/results/_v4_maindir_cleanup_moves_ledger_v3_2026_09_24.md` | `8f5136e176b8c27a4e2b7441bcd1cef9f4324c19161203a3cc8bbd2f25539c4d` | `a151c41f639b8b238da6458c3e5b80dab23da9e89cedea2214a6e3344ad3dc73` |
| `_september_workspace/results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` | `cfdfbd121d247235430a6463cb5b1b8b39b039e03a16903aca1f66b913125f34` | `2f00429ed2d8d29109af6198e51bb8693d2ac48e2ceb2c343d3069d42929cdd4` |
| `_september_workspace/results/_v4_maindir_count_monitor_2026_09_27.md` | `722c8b6f62d5882539741c2bb89030affbe90a9f3eed428a0155a400fd5011e2` | `17dfd981ce9873a3777b019d45c35778c54a05ccfbe86e02ea111469a0429abe` |
| `_september_workspace/results/_v4_pi_cot_v3_questionnaire_v2_d8_2026_09_28.md` | `238077d25919cf34da254a5aed15d03a79454e21d14cd55aca6eed7f588f6355` | `1a14d222d9a7036dd4daf8b4131e729a09924c4c2e2808d67b558c4fbe447406` |
| `_september_workspace/results/_v4_trae_remaining_audit_2026_09_28.md` | `1a8648083228ae1c43e603c11e07404afc52c2c29d5f7b1449a356d4989f770b` | `86a46c7968e1d17a0ac558b67b545a939cf6fd216e30e1206482d2a24382d364` |
| `_september_workspace/results/_v5_b12_verify_pack_q1_q3_q4_2026_09_29.md` | `698262e6fe8b429cc77260283113753316d4a014ee15a4c6252fae0d37a555b2` | `426646c7f6272eae8e61b3dd3892fad9c0ff20749191220b118999a6e4f6fe4c` |
| `_september_workspace/results/_v5_clearance_mr11_doc_calibration_2026_09_29.md` | `c4bce5a5e8be57305cbf536dabfbbc2e0aec5e5b5b8becc1aeeab9ceaa5ecd0d` | `f089703300db26f5aea42d746bfa03acd491777397ea9d9c480b153e8c54b929` |
| `_september_workspace/results/_v5_clearance_o15_ready_pack_2026_09_29.md` | `618e5990b3e5b8d32e136b3b6697ab3502b0e3ef6b66014ee86a5b0047fe278f` | `cf925f58a98acf3ba7b499d878fe87cd7babd1fd2d556e71aab6f2cbadaee543` |
| `_september_workspace/results/_v5_confirm_b11_decisions_register_2026_09_29.md` | `07e9fe512da5c340391bbf5c62ffa875cb7af95e310355812b901b54eba8483b` | `2d2b5cd6dc91e7134737572d913665fcbfd4c25949ae48100284987aea229b58` |
| `_september_workspace/results/_v5_confirm_b3_decisions_register_2026_09_29.md` | `4dbb11c219fc9d046f09f88d703c9ebdd8b698c97cf4e5e78ef0a03e9372c28b` | `2580683f178096b905d87954cdba08b1bfb578995b9eb45dcf015e784fa1d609` |
| `_september_workspace/results/_v5_confirm_b8_decisions_register_2026_09_29.md` | `62e8639075c0b6f044b6bbc313b0ec1122c230760f686cd3c416d3859b609359` | `f34ebab20e4adff2a297a24a7754c27494a2528031e91846b08cb4017d7c8e01` |
| `_september_workspace/results/_v5_item21_rerun_conditions_prereg_2026_09_28.md` | `4185bdad6df5e662b973a6428c91f16404cbc6d831f7572c7ca390738ad08538` | `550b84c76771759e8dcd5fca02c79f7d8f6693c37e3319cd799a10abc554b33e` |
| `_september_workspace/results/_v5_item21_verdict_2026_09_28.md` | `de274bd38955be2f0b80c388d9909a9af2ff6cbde5fb245477a7a00e502d166c` | `10de142ad0a31b2beed7fd9f9083eb8d2420316b068324f5de5e1bd0a64769bd` |
| `_september_workspace/results/_v5_paper_remedy_r1_pledge_2026_09_29.md` | `0ac0d59fec3c1fd2b5d2fc8cb5a06f0e6cfc8fbad61f5fc95058055d43347c1b` | `2f9a1fcfe53c761c69416a6fca8468161b499033674244882a765370b2bcc127` |
| `_september_workspace/results/_v5_paper_remedy_r2_r4_sourcetrace_2026_09_29.md` | `d3bb1ddc179ee54c1038b4518e232806d9a4b794d0730a1338c463f9fc842d0f` | `2079151bf48d7cb6087916708d7d587c63c7443bf3d1c73740d1759530e2889b` |
| `_september_workspace/results/_v5_r4_residual_merged_catalogue_2026_09_29.md` | `0c4bbd26ea55207bd5cc36325aa4c0f5a1427b0fba4de78b89a7f4a73a11a89d` | `3ecdf8515d7eb9e06dbb70a27f2111f22c442488caf67478350d4963ac1e7f3b` |
| `_september_workspace/results/_v5_sub_artifact_ledger_history_r1_2026_09_29.md` | `535b3c2ad1020e5ec148056a8cc5d01a8b81f6f9f78efac6e90a502381604dff` | `e2e8beb1b51171ad86397598086fc71e7bc03749152cc1184acac2502f647732` |
| `_september_workspace/results/_v5_sub_artifact_ledger_history_r2_2026_09_29.md` | `82a5e7f4dac4a27519c764d9008c6a0c0a925c9da4214bb028476bc916774f10` | `6e3455abac0bbf8c049fdb5bcb65d1bd06fb58e672b2f8e1dab1b38781c636c5` |
| `_september_workspace/results/_v5_sub_artifact_ledger_history_r3_2026_09_29.md` | `edb37f70d3e4c82bdcfe948a7d5ddd61ec3e029fda60bb2e5b75c776e4a21e7d` | `f6916dd2ed9c5edcfecc339b33f08d4929fbf385dfda2fc9b0c9cdc5f2a04f41` |
| `_september_workspace/results/_v5_sub_artifact_ledger_history_r4_2026_09_29.md` | `a72fa505ea9ad10e3cc7530024ac08c051e84dd620b44fd11393767b68d088bf` | `812d211662ad95328af01ed70cae46647f4761408d8a4566e8ef6a12d3618838` |
| `_september_workspace/results/_v5_t1_decisions_register_2026_09_29.md` | `7dd7dd3fb721efb8cecc143175d5f5175da75ed604ec6c93e07478a207f1ca50` | `5cbec889c4b6a8118868cd141b3068bed74ab039d56b7ced77fd4b78e7999739` |
| `_september_workspace/results/_v5_v4_proposal_23item_merged_catalogue_2026_09_29.md` | `79bcff089f2170ce6262065de2d0c8c4cbeb53cafc8cbd597a08b043fc3f8ec1` | `e0a76f7ac3ff7f0ee2fbe431c33b5765fccc64bf680f306e7f744ab797267240` |
| `_september_workspace/results/boss_pa_1_rbr_rm_result_2026_09_15.json` | `c7c59e0d2f6c88473dd143b904b5a42993afc2437cd1bc7de5f219389aadce4e` | `c7c59e0d2f6c88473dd143b904b5a42993afc2437cd1bc7de5f219389aadce4e` |
| `_september_workspace/results/boss_pa_2_potential_game_result_2026_09_15.json` | `5c76137d64305e6154943c8a155de6558bdc0302e10ec436760e86e80fda8927` | `5c76137d64305e6154943c8a155de6558bdc0302e10ec436760e86e80fda8927` |
| `_september_workspace/results/boss_pa_3_replicator_dynamics_result_2026_09_15.json` | `d6f233d73c458fe47309587ede984478eaa07e6d25a653abbdb54bedc1dacd99` | `d6f233d73c458fe47309587ede984478eaa07e6d25a653abbdb54bedc1dacd99` |
| `_september_workspace/results/deposon_3risk_v0_fixes_2026_09_11.json` | `d87c0327a6fb4db5b119fe85b183cf1280233ec0de884087f76281213c1dc9da` | `b6f5d0a562d907c405eb5f7c4aacf76765df7012daca26fad58272f8fc574fe3` |
| `_september_workspace/results/deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json` | `4e4a17d43adfa9d81ad9ec9617cb42405e1863164f1ac3c568c762b5024a81b2` | `1eccce315e9a619d262c56a04a7d83514e18d0810376687bc4cddbef283fcb0c` |
| `_september_workspace/results/deposon_pa_d1_d3_2026_09_15.json` | `e221792715f8cb91caca9860e90b21509550e5796c336607a6b0accd5e9e37c0` | `937c4de3adb847ee90ea84e4869eac2aa40311a11929364142a56b2421be0d0e` |
| `_september_workspace/results/deposon_pc_d1_d3_2026_09_15.json` | `b2046af03610e8981a9d44bb54e724d8b398400c6751de1e5df98b1d971c5079` | `3d54afcf64ff1de443dbd5f8911dfdfe8dd23fb43a14b6e22b74f5e0b013e7cd` |
| `_september_workspace/results/deposon_pe_d1_d3_2026_09_15.json` | `594d7a8d3de81b5744e8b39f41626459e5cbfd824e338f1f28a1054722b685ec` | `5155f085beaa81d21eddbc1c03e0410babbd08212ee487fc06b299c5e2d8e286` |
| `_september_workspace/results/deposon_pf_d1_2026_09_15.json` | `12791772814e206ccc28aec2ec1e243210aedbf8b2b51c195b3d0b18611e6653` | `12791772814e206ccc28aec2ec1e243210aedbf8b2b51c195b3d0b18611e6653` |
| `_september_workspace/results/deposon_pf_d1_full_9m5c_2026_09_15.json` | `fcb5105df0b67fc9d3dbc80f6fbeee6bfdc31ce8add33aacfb77f1c470caf38c` | `c034de6ebe3f4f54407380bb658de461a12dcc5d5d80981b652108a09fb1e0e9` |
| `_september_workspace/results/deposon_pf_implementation_2026_09_11.json` | `509dcee3b139726619b54581de6af4000e180b26c5861b271a4ef906cd399e58` | `490c9c47851933c4c1f8c0cbdfaf51f469fb7b286297597aadd04038f07c88b5` |
| `_september_workspace/results/deposon_pg_v01_9m60c_2026_09_15.json` | `ab75889ee738a49a4c7b71b51d63b976ca8d2246b4fc122b487396f5a4f56352` | `c172144e57cd119a6ac5152e7a873cca09aa870a06482dae583aa4e5db4a3c05` |
| `_september_workspace/results/deposon_v3_physical_opt_60cells_2026_09_11.json` | `c659695aa23cfee016eeeece6bc1faa2ede9d64f5a7766c80a4282bfa63d15ce` | `aad65efd548b8d08fc35ecd4073d8b2553ce314896436f279e48840a78af1c20` |
| `_september_workspace/results/deposon_v3_v7_summary_2026_09_11.json` | `063ac8d00542a6e5dd843785442f8f8a367e5ad9343dd3135bb2ccb1154c2c2f` | `3c3c6752a56fa34d435254b4d42427a9493cd2203fe17f1e0eac3cb8efa988bb` |
| `_september_workspace/results/skill_a_p_a_60cells_result_2026_09_11.json` | `f4a210d69220b76f579f0d5d2e3600bbe0e2ea4ecfb1b1099713be31fb463917` | `f4a210d69220b76f579f0d5d2e3600bbe0e2ea4ecfb1b1099713be31fb463917` |
| `_september_workspace/results/skill_b_p_c_alpha_beta_result_2026_09_11.json` | `b921002e4dfb24fb3ec4c88b36d63be0613f26c467da33f758fc5cc343d58db4` | `b921002e4dfb24fb3ec4c88b36d63be0613f26c467da33f758fc5cc343d58db4` |
| `_september_workspace/results/skill_c_p_e_3modality_result_2026_09_11.json` | `470425a8c77de1a02763281797dfcf52c5286022392c61705845f4036dce9dcd` | `470425a8c77de1a02763281797dfcf52c5286022392c61705845f4036dce9dcd` |
| `_september_workspace/results/skill_d_p_f_observer_result_2026_09_11.json` | `0207c01b9562e6f5e59dac047a2a866ef84452063997bef0440bf12159e752d6` | `a8b8687e08cd514bcbd0e94120b7fca736c082ead5f1e46f4a8debe1631bb10c` |
