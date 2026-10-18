# DEEMPHASIS SHA Drift Register — 批B5（文件名级改名 10 件＋路径锚同批原子回写）

- 执行日：2026-10-06（CST）｜执行人：鲍勃-实验分析师（代 KIMI，PAT 推送）
- 授权链：PI 2026-10-06 群内指令（视同委托信 §9 签字生效）→ 群管理员派单（22:19 续作授权）
- 开工 HEAD：`dacb5f7`（批④后）｜基线 tag：`deemph-baseline-20261006`
- 红线自检：R1 判定链读数 0 触动（manifest/JSON 仅 path 类字段 basename 替换、SHA 读数与判定词 0 触动；锚卫脚本 `_audit_secret_2026_09_20_anchor_guard.py` 仅路径串替换、判定逻辑 0 触动，沿信载附录 B-3 尾注口径）／R2 git 历史 0 改写（仅追加 commit）／R3 0 凭据
- 10 件新名与 `git ls-files` 全仓 0 同名冲突（2026-10-05 信载实测＋本日 mv 实操验证）

## 表 1：改名件（git mv，§3.5 映射）

| # | 旧路径 | 新路径 | 改前 SHA-256 | 改后 SHA-256 | 动作 |
|---|---|---|---|---|---|
| 1 | `_september_workspace/docs/V3X/D3_WECHAT_MIDTERM_TEMPLATE.md` | `_september_workspace/docs/V3X/D3_ONLINE_MIDTERM_TEMPLATE.md` | `574d5a79e363d353af1f1985cec5a03c3641f9c49825b27d25583a25f87e455f` | `b3e00ba108a1dc63c050705dab3ae8092682c549febac9d349a1c9cf32d116cf` | rename+content |
| 2 | `_september_workspace/docs/V3X/D7_WANG_TEACHER_WECHAT_PUSH_REQUIREMENTS_2026_09_18.md` | `_september_workspace/docs/V3X/D7_EXTERNAL_ADVISOR_ONLINE_PUSH_REQUIREMENTS_2026_09_18.md` | `935cb6ee356652430bdd3841c1e5bd6a496b14b499e0b44af78f1cae4b8973f6` | `244b76b690f010629bc95f8adf667b722092d02f34f14dfb688bf38310c96d0f` | rename+content |
| 3 | `_september_workspace/results/_archive_2026_09_20/LETTER_TO_WANG_TEACHER_2026_09_18_FINAL.md` | `_september_workspace/results/_archive_2026_09_20/LETTER_TO_EXTERNAL_ADVISOR_2026_09_18_FINAL.md` | `643d636feae949ae56b382c5ff6742255c8213a5e06610b8bec209d7e16cd7ec` | `ff37f39264bc059e6216166979547c4dc97524e3e5e0fe30f91d71a6ccf5897d` | rename only (content done in B4) |
| 4 | `_september_workspace/results/_archive_2026_09_20/_coze_wechat_v3_d7format_2026_09_18.pdf` | `_september_workspace/results/_archive_2026_09_20/_coze_online_v3_d7format_2026_09_18.pdf` | `adc99e04ac532ec887dbbad31bce3dee532f6cfd36da8e585530b5f9b109d703` | `adc99e04ac532ec887dbbad31bce3dee532f6cfd36da8e585530b5f9b109d703` | rename only (PDF binary) |
| 5 | `_september_workspace/results/_archive_2026_09_20/_letter_to_coze_wechat_v2_2026_09_18.md` | `_september_workspace/results/_archive_2026_09_20/_letter_to_coze_online_v2_2026_09_18.md` | `b32cd6da5ec4cbf59b970ebaa8ac7f15e0cf2cc3df61e550acd536d11b5badb6` | `dc3e56adc3fc7be642a8feb25b365dfced7cbebc29bc868a3b408de8e6205444` | rename+self-ref 3 literals |
| 6 | `_september_workspace/results/_coze_wechat_v3_2026_09_18.md` | `_september_workspace/results/_coze_online_v3_2026_09_18.md` | `229d76e1b86fa59b0f875804d89709a1cb4f6e123d5334e196b70224cd829c78` | `53c9c1ab2d123d1b5d495892635fc9728a8602c7e108452f17cabc78455f0f61` | rename+content |
| 7 | `_september_workspace/results/_coze_wechat_v3_d7format_2026_09_18.md` | `_september_workspace/results/_coze_online_v3_d7format_2026_09_18.md` | `905544775aee00e62d879693ac204f02750178376a12fbf539b5d6c5430918c2` | `debe3761c565e0ee5a14247f96db30b122ec337dd60c279b88b2c665fbf9eca9` | rename+content |
| 8 | `_september_workspace/results/_coze_wechat_v3_final_2026_09_18.md` | `_september_workspace/results/_coze_online_v3_final_2026_09_18.md` | `deee45f45c5ddab1e7fb151c38ce0756cf0435039da0082fb2b7f53a80f8c10a` | `36439bc12bbad73d4be14d5bc2b858e6f55e58dc5e20966af91c81ae25ae8f3e` | rename+content |
| 9 | `_september_workspace/results/_coze_wechat_v4_d7format_2026_09_26.pdf` | `_september_workspace/results/_coze_online_v4_d7format_2026_09_26.pdf` | `a828816535206680a454e50ed747eba300b1128734e23c3b9f300713d136a4c3` | `a828816535206680a454e50ed747eba300b1128734e23c3b9f300713d136a4c3` | rename only (PDF binary) |
| 10 | `_september_workspace/results/_d7_wang_teacher_wechat_publish_v1_20260918.md` | `_september_workspace/results/_d7_external_advisor_online_publish_v1_20260918.md` | `f4d5b755736af4fc78363bf87fce5db421d9927adbbaa5457e8b064ab465ca01` | `788fbdd8c12fad72ba113d7b9dafe1c1b6ace18de331579dfea79d7933c3cacb` | rename+content |

## 表 2：路径锚回写件（B-3 引用件，旧 basename→新 basename 最小替换；本日实测引用面与 B-3 逐件闭合）

| 引用件 | 改前 SHA-256 | 改后 SHA-256 |
|---|---|---|
| `_september_workspace/.tmp/verif_doubt6/baseline_pre.json` | `8406cb842cac30a1e428df4401c3c10c8af7fb693771b441be4e86493bb6dd19` | `5e6f7b3b71e4571cee1c088f2a5b728eea33511b5f0171cb4e4e850e78a3d116` |
| `_september_workspace/_mirror_manifest.json` | `93ed929c27cfc18da1934f4b16b8fda36901dca1c641e0ae7af677b87e384050` | `e4548dc95e27a2f8361566fecc8c7319311ed4845ba5ae7bc9945bd383bdceaa` |
| `_september_workspace/_movedout_manifest_2026_09_21.json` | `d1ee21f3f6ae8fe3544bb515115c3fa40096794a7b2855ec0a5fbaab035c9fe5` | `dbd3077d7f7b8f6213819ff508cdfe6306a35cc2bc25774556d580f656cc2551` |
| `_september_workspace/deposon_team/_designs/V3X_CLOSURE_REPORT_REQUIREMENTS_FOR_EXTERNAL_AGENT.md` | `2185433b1f32bd5ccc32102bf7c0324ffd4040f753169edb3523ad7997412227` | `01af28f3fda3ba062223eb320e221a8bdc2f683b44d66b18632d0fa14e6f5739` |
| `_september_workspace/deposon_team/_designs/V3X_FULL_CLOSEOUT_REPORT_2026_09_16.md` | `95925a56259762c5cf88c57711c90e8e5c6a4f679d98923a642740e0deadda05` | `6d56b453d931cca435a0b8ebf73e9265f3d4cd3176f5d619f8237038b7c592d6` |
| `_september_workspace/docs/V3X/D0_FREEZE_PREP_2026_09_09.md` | `0d1e88c258aa1ea746adbf6372367b0d0720a81b25f2a7cfea2e0f9003c264be` | `ecfe3cf4df436946ef123c73c6c6b7645132aa65478eca8ba1bf5d71576610e8` |
| `_september_workspace/docs/V3X/D7_PRE_V3_POLISH_AND_TEAM_IMPROVEMENT_2026_09_16.md` | `51869e3184f4e39eabcb377404cab86303269ca22d93f0788f22258a2c6205e8` | `ba5cd63303d233f88adbc73d8e95abe6bbd52587bd526156329605066abe5511` |
| `_september_workspace/docs/V3X/V3X_D6_PAPER_V2_2026_09_09_mavis.md` | `4d06d34cb6fadd3875737128ef742097807eb48fb117cee16dc22d776f92b04c` | `4b2c22fb735fc33b963e4e8d58aeb0c868c45f6629769330e47150ced9fca985` |
| `_september_workspace/docs/V3X/V3X_D6_PAPER_zh.md` | `feae8af2fefe8fcbb619558a27fef8f2602e104991bcee7efd1fb9b8d84b2dc8` | `f806c2d96e85aa67e93700e1e671d9aab48e1bc8c9b547666f9f334fb83e48a5` |
| `_september_workspace/docs/V3X/V3X_FULL_EXPERIMENT_DESIGN_2026_09_16.md` | `3d847f9f3151e6c7ebf75330c4dc8c8199aa78e2c94c7e4794e4455ea0853b4a` | `54782e20fe06b565cd55754bf4f1f129248769d2673b6b05367bc6954f80c34f` |
| `_september_workspace/results/_archive_2026_09_18/_trae_code_improvement_v2_2026_09_18.md` | `e151e48ab4b450e6fc63a6080919fdfe5214b5d94b1e6bde8dcd370b6d332460` | `86a243d90e8aceef58eed2f01b1df28830f3d22deeae7e82f4d1eefbf07c4c6e` |
| `_september_workspace/results/_archive_2026_09_18/_trae_d7_v1_audit_20260917_190000.md` | `e240ca712be6e25df3bf04024d609f1995cf4b5e7c988477f44ffac917caba62` | `41c142eab4a1d4e342e0a59d998849e60207efa669de6b2e9eaf2daf737c6f75` |
| `_september_workspace/results/_archive_2026_09_18/_trae_paper_8ch_双审_20260917_200000.md` | `bec666969ffc5e7f07ca88992bb71d2095871dab38dcbab93ef734091827e35a` | `145abbb9c365f67c5e6480d99d31a5b51b062fa3d01e874f9fa61620d4bfc661` |
| `_september_workspace/results/_archive_2026_09_20/_archive_manifest_2026_09_20.json` | `4dd89950bf11b5a6cb187ee9e46c62781883a5ebf5dff4c578645eaf46ddd1ae` | `84187488203d3d56a54ad0d8702fe378af69356d405ced8d27fb72fa3b027548` |
| `_september_workspace/results/_archive_2026_09_20/_audit_secret_2026_09_20_anchor_guard.py` | `19b4174f6339878c4d4a3d663498f2822b1591c973bbf245204b0487064d1942` | `780a8adae5e8f4d2cffe6188fb47cc3f96e9b4ae104a6f7deff9d57a896a2eb7` |
| `_september_workspace/results/_archive_2026_09_20/_letter_to_kimi_upload_requirements_2026_09_18.md` | `005456125d1be02638d3f89df92e8d322fb408566d8dab7b27675149ed310af6` | `8b22a026f30b430734b742ebfe0b786076398979475ad94236437a6983419eb3` |
| `_september_workspace/results/_archive_manifest_deposon_sub_2026_09_23.json` | `b34b9f7bdfb7ce9b5457b14d0bdb387ef98e2d1758358a4d93998741314d9144` | `0cc79ff91a1285a05f8214b7e5d126157e2ea9b7150c59b8564019835e5ae51e` |
| `_september_workspace/results/_ghostref_copy_log_2026_09_23.json` | `8cd133d0896f11fa365cc73379388accea06b50fe02678b4667f6436990fb6a4` | `64dfc25adf3d3d3662e786a6e70ba62e43dad8d4a8dc0f5cb9e1db1988ad395c` |
| `_september_workspace/results/_kimi_push_v3_manifest_batch14_e5952130.json` | `64aa9d8a5c7df379026fade8e7650780c2af0d38921cb0b1411580ca7919d361` | `54bd7e0195cacf5948424cd82f3c7cb54233aa6f802ab4de207aa0440abebe3e` |
| `_september_workspace/results/_kimi_push_v3_manifest_batch5_34439e1e.json` | `2769b83f5b1dfb84c828fd4ec3211a0056dc09509a08918578e71c7de0a4ffe6` | `9880b95fada3bfb59b29a5b30ab612543bb783fa21984d2ac1175375b9476b1c` |
| `_september_workspace/results/_kimi_safe_batch_push_v2_full_2026_09_17.json` | `adf3a8017e260225a63df98f6b5827cd71d17acbef4225ba0259c842c82fac25` | `7886dbcd353b7817a0c7fedb9e305ab3f066d3bc6fd6115c1d1a4e5b35d67d31` |
| `_september_workspace/results/_theory_input_request_supplement_2026_09_29.md` | `cd2f23b3b7afc08633151f92ab1450dc03c034746e113f404ddda0ca94acd706` | `20c4979626b249d1254f94af4ddbf981c5d982b5daf8ac383ca6263059b35e5a` |
| `_september_workspace/results/_v3_v4_achievements_inventory_2026_09_24.md` | `965db22e913051f89d1a4d76321d9b4602889664764394cd17cc275a9bf4eb93` | `4322da59b8161bda25f8c5a719f06213cde944fee4c88903398d96aaf73ab5d7` |
| `_september_workspace/results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | `df7e9cd3925161e66781dd61502f059de64fac99e3bbd3ff63abed61779f423a` | `8483f9b18d704dce949d39f72cb1207ff49ac170e0189b76e494906e7ef48eca` |
| `_september_workspace/results/_v3_v4_ghostref_reconciliation_2026_09_23.md` | `1d52db0ebf53d3a93955e678f23966fe9670b388a45dfd3f2b987b7bb4aa363a` | `64594f5feb9e1d306fdfbdc187b7385c8936661712983142d7bd2a839cd9c42d` |
| `_september_workspace/results/_v4_maindir_cleanup_manifest_v2_2026_09_26.md` | `f586a5a215847a47fb322c0df712810f30b47a084be39f2b9dd47029c65bcd9c` | `1cc1e187102e9e838757ff197f75e10000d92910916fdc439ec6d429547c3531` |
| `_september_workspace/results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` | `cc498bc285253b8f7f547540a5f5e47881594e4e688788f20736a1fdc78bba84` | `cfdfbd121d247235430a6463cb5b1b8b39b039e03a16903aca1f66b913125f34` |
| `_september_workspace/results/_v4_maindir_count_monitor_2026_09_27.md` | `71e9cc179bec9f37defacc1381729747caadf284944893f43a3dbf9fc65a414b` | `722c8b6f62d5882539741c2bb89030affbe90a9f3eed428a0155a400fd5011e2` |
| `_september_workspace/results/_v5_confirm_b8_decisions_register_2026_09_29.md` | `6862659ff9000c3c0727eb0c78209b13ef53a3af2a6b7b2618ee2f1110160b3a` | `62e8639075c0b6f044b6bbc313b0ec1122c230760f686cd3c416d3859b609359` |
| `_september_workspace/results/_v5_paper_remedy_r1_pledge_2026_09_29.md` | `816cb91d4611b2d93d02f65c66da6254332e8b6dbd44d6e0a2ed226694fda688` | `0ac0d59fec3c1fd2b5d2fc8cb5a06f0e6cfc8fbad61f5fc95058055d43347c1b` |
| `_september_workspace/results/_v5_paper_remedy_r2_r4_sourcetrace_2026_09_29.md` | `29da2ca8932ff3ce04e5ceb455ba50dbbacf6b660740974dc2b4fc15cfa47fbe` | `d3bb1ddc179ee54c1038b4518e232806d9a4b794d0730a1338c463f9fc842d0f` |
| `_september_workspace/results/_v5_sub_artifact_ledger_history_r2_2026_09_29.md` | `5ff7784db145db391c3cf492a1782f8920c286d8697651a80f8763b2951bd08c` | `82a5e7f4dac4a27519c764d9008c6a0c0a925c9da4214bb028476bc916774f10` |
| `_september_workspace/results/_v5_sub_artifact_ledger_history_r3_2026_09_29.md` | `e04a46b02d136b40847d30daf7ec591c77552e20319ae099b26b22bf4275eb35` | `edb37f70d3e4c82bdcfe948a7d5ddd61ec3e029fda60bb2e5b75c776e4a21e7d` |
| `_september_workspace/results/_v5_sub_artifact_ledger_history_r4_2026_09_29.md` | `b6b8be476a73384b8f891d702ba3757d6c39c2e0a9bae7a1f8d8b8e5416931f1` | `a72fa505ea9ad10e3cc7530024ac08c051e84dd620b44fd11393767b68d088bf` |
| `_september_workspace/results/_v5_v4_proposal_23item_merged_catalogue_sourceverify_2026_09_29.md` | `ac0d6f19f06cb4df5a3879c5c622fd4811e2440609fcb83776b5c7022a1c3557` | `ef9a0c8de6f1d956062ae670196573994d5ce4bfdf8cdce065d54b76c5eb4976` |
| `results/_trae_d7_v1_audit_20260917_190000.md` | `e240ca712be6e25df3bf04024d609f1995cf4b5e7c988477f44ffac917caba62` | `41c142eab4a1d4e342e0a59d998849e60207efa669de6b2e9eaf2daf737c6f75` |
| `results/_trae_paper_8ch_双审_20260917_200000.md` | `bec666969ffc5e7f07ca88992bb71d2095871dab38dcbab93ef734091827e35a` | `145abbb9c365f67c5e6480d99d31a5b51b062fa3d01e874f9fa61620d4bfc661` |

- 责注：按委托信 §4.2 指纹锚规则**不回写** SHA 读数，原值以 git 历史与本登记件为准；本批引用件回写仅动 path 类字面。
- 表外变体登记（§2 细则 3 报备）：`_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` L84 出现通配简写 `_d7_wang_*`（指代 #10 旧名族，非表内 `wang_teacher` 原形），本批未替换、留批⑥路径形归口或验收拍板。
- 内容件路径形归口（同批④ #9 口径，可逆推）：`_coze_online_v3_2026_09_18.md` L132 `count_wechat.py`→`count_online.py`（仓外临时脚本名，无悬空）；3 件通配形 `_coze_wechat_v3_*`→`_coze_online_v3_*`（`_v4_maindir_cleanup_manifest_v2`/`_v4_maindir_cleanup_moves_ledger_v6`/`_v5_sub_artifact_ledger_history_r2`）。
- 6 件内容件替换统计（叙述形 §2）：王老师 37（含连叙「王老师 WeChat 顾问」→「外部线上顾问」×2：D7 L19、publish L191）＋微信 12＋WeChat 36＋王子贺 2（L16 实名+「人大高瓴」连用整体消化为「外部合作导师〔匿名〕」；L56 分形）＋人大高瓴连用 1；各件替换后残差全 0（复验 2026-10-06）。
- 批⑤后全仓残差（附录 C 口径实测）：王老师 434／王子贺 43／微信 36／wechat 469／人大 9／高瓴 10／RUC 1／Renmin 6／Gaoling 0。与信载 §5.4 期望值（420/42/35/568）差异根因：① B4/B5 登记件自身含 token 计数注记（王老师+2、王子贺+1、微信+1）；② 回写减量实测≈150 处 basename wechat 字面，远超规划估算 34 处（期望链 568 的规划基数）；③ 登记件为验收要件、不参与替换。以本实测值＋批⑥后终算为准（信载 §5.4 尾注口径）。

