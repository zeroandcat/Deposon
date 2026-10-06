# DEEMPHASIS SHA Drift Register — 批B6c（⑥c 子批：其余核心并集 50 件）

- 执行日：2026-10-06（CST）｜执行人：鲍勃-实验分析师（代 KIMI，PAT 推送）
- 开工 HEAD：`75cfae8`（⑥b 后）｜基线 tag：`deemph-baseline-20261006`
- 现场枚举（附录 C 分 token 口径）：_september_workspace 其他＋主树 docs/ 2 件＝**50 件**。与信载 §3.6 ⑥c 桶计数 54 差 4 件，根因＝批⑤ B-3 回写连带清零（`_mirror_manifest.json`、`_movedout_manifest_2026_09_21.json`、`.tmp/verif_doubt6/baseline_pre.json`、`deposon_team/_designs/` 系列中 token 仅为路径字面者）；主树 results/ 2 件（`_trae_d7_v1_audit`、`_trae_paper_8ch_双审`）亦经批⑤回写清零退出。非漂移非范围变动，B5 表 2 台账可溯。
- 红线自检：R1 判定链读数 0 触动（判定键/检查串/打印标签/LaTeX 引用面按保护机制保留；numstat 对称）／R2 0 历史改写／R3 0 凭据

## 替换统计（§2 口径）

- 王老师×57→外部顾问；WeChat×63/wechat×21→线上（叙述形）
- 王子贺×21→外部合作导师〔匿名〕（含 `docs/V3X_COLLAB_DIRECTIONS.md` L1 提案标题）
- 代码检查串（§2 表内）：mentions_wangzihe×2→mentions_external_mentor（`compare_versions.py` 键名）
- 路径形×44：_v4_commission_wechat_report_coze×44→online（可逆推）
- 机构形（主树 2 件）：`THINKING_V3_GT_CONTRIB_2026.md`「单位：中国人民大学高瓴人工智能学院」→「匿名合作机构」、「人大 AI 之夏」→「匿名合作机构 AI 之夏」；`V3X_COLLAB_DIRECTIONS.md`「（人大高瓴，…）」→「（匿名合作机构，…）」
- 合计 209 处替换

## R1/存疑/表外保留项（不替换，报备 PI）

- **判定链机器面**（`compare_versions.py`）：`'王子贺' in text` 检查串×1、`'中国人民大学' in text`＋`'化学与生命资源' in text`＋`'Renmin University' in text` 检查串、`has_ruc_chem` 键、L160 打印标签「袁祺皓/RUC chem」（含表外人名袁祺皓）——判定逻辑 0 触动
- **LaTeX 文献引用面**：`School of Chemistry and Life Resources, Renmin University of China`×2（`compare_versions.py` L784/794、`_md_to_tex.py`）——已发表件（arXiv 2609.09001）Comments 栏单位字面
- **存疑保留**：`_glm_five_items_suggestion_table_2026_10_01.md` Renmin×2（该件自标「是否照录由 PI 按 H8 定」）
- **JSON 判定键×12**：`no_OpenRouter_TeamoRouter_V41Flash_GPT6_agent_plan_WeChatAPI`（boss_pa_*/deposon_*/skill_* 等判定键，R1 读数面）
- **表外变体**：`THINKING_V3_GT_CONTRIB_2026.md` L58-59 王老师履历行（清华 IIIS、导师唐平中、姚期智、准聘助理教授→副教授）——§2 表外信息，整段匿名化方案待 PI 拍板
- **PDF 二进制**：`fiction_that_feeds_back.pdf` 内 RUC 字节命中——PDF 文本层无法经文本替换处理，待 PI 决定
- **排除项**：`paper/deposon_paper_v1.md`（人民大学＝PI 自身单位行）——§2 排除 0 触动

## 全仓残差终算（附录 C 口径，B6c commit 前工作区实测）

- 净化域（排除 6 个漂移登记件台账注记）：**王老师 0／微信 0／人大 0／高瓴 0**；王子贺 1（判定检查串）；wechat 12（判定键）；RUC 1（判定打印标签）；Renmin 6（LaTeX×2＋存疑×2＋检查串×2）；Gaoling 0（全仓 1 处在登记件注记）
- 全仓（含登记件注记）：王老师 8／王子贺 11／微信 6／wechat 55／人大 4／高瓴 5／人民大学 3／RUC 2／Renmin 9／Gaoling 1
- 与信载 §5.4「批⑥后残差＝排除项域」目标一致：剩余全部为排除项（paper/）、判定链保护面、存疑报备面、登记件台账注记，均已逐项列明供 PI 验收拍板

## 逐件 pre/post SHA-256

| 目标件 | 改前 SHA-256 | 改后 SHA-256 |
|---|---|---|
| `_september_workspace/.tmp/_audit3b.txt` | `e64565a2b1808ad576caf9490792f625509959a88a3e5360b59e7196ece65bac` | `599b8c4240921a5752020108fd5014d720f83f9f031742b66654393ca7379b23` |
| `_september_workspace/.tmp/_audit_part3_out.txt` | `85a9d9861d38eef3ed1d7ddfc12ba05e9c635db70d110b8a2af55ad80eb04cb4` | `448098227c2af61dd178c6e22524023c6dde123c3fb616aaf1739b08306b0e3f` |
| `_september_workspace/.tmp/_audit_part4.txt` | `def27c1c35116943cc5f4a60225fdd1d3362a4d013fbdaca74df07620b11733c` | `c1f48194bc26525c07868ba891ad51a432c1bb7bb401a9157d7b85bc05aea6f3` |
| `_september_workspace/.tmp/_gaps2.txt` | `4d899338b548d265b7f98df25892a8d165e047acc546b4888aaefe1cc064f413` | `1846738bf3c31ec743cb3342c204bac217cdd85d761eb08038b12a758f5f7f3a` |
| `_september_workspace/.tmp/_r6_evidence.py` | `4de12a4f441bd8189dc01acf964f60286aaae51b17a29c0263e0b11a1077cdae` | `841c2fef5f6b982a72b852149eeac59dc57e238a9b925f0a75a642ee0077c88f` |
| `_september_workspace/.tmp/_r6_evidence.txt` | `eaed8c0a509e6ca294ae56d4975766c776ff39cfff49930db3f4eba2aab81a55` | `08e32d8fb43c550d44e2d3e71aa5b692dad74b524036f5e3dba99c5122087a90` |
| `_september_workspace/.tmp/_trae_audit_part3.py` | `f4c9940043115a20bf760f646d72bc170c9d82fe64892d25d67a7cf7bcafaa69` | `28dd569cf3ac7fdf796e8de4ac165d4a0ef49508b1f6b9478a4d3bbe49d72275` |
| `_september_workspace/.tmp/_trae_audit_part3b.py` | `c1a9a6c3c17ab68b4244a709d54ff9406a4c31a0b4ec1795e19293259aa3101d` | `0f7518749f64729dd64234a93e718734f4f785ceb536bdfbbbe4cd98ab15d111` |
| `_september_workspace/.tmp/_trae_audit_part4.py` | `bc8d4721bf3baf2f9ce1073045bb29162ae95b068480ce0e7639f7c62e45058e` | `a3338cb969b605fd20be2f187c3c48cce308880c61a555ba4300fd25dd0f9c38` |
| `_september_workspace/.tmp/verif_doubt6/baseline_pre.json` | `5e6f7b3b71e4571cee1c088f2a5b728eea33511b5f0171cb4e4e850e78a3d116` | `e67239f270583a1f084f813d2ebf06bfbe97d09ce6abb86b166347b595cba39a` |
| `_september_workspace/.trae/audit/compare_versions.py` | `03e22a91bc0c1160dfad8ab54870dd73c25ea76e463499a28bb570f90c3ea5ef` | `f4e9b7f50e6d2db46a9a322474a4ff11fa7960f789007a58c5abb02453f74556` |
| `_september_workspace/.trae/scripts/_md_to_tex.py` | `f55da6fe7aea49a268ec18eb1d7bc584a2c7d73da3ea530e79023eb2ed9c97af` | `c1caa4f436184b298e0ae445dd1fe5ed1f3648302ce18df44ac7776ca9c71532` |
| `_september_workspace/.trae/scripts/_verify_tex.py` | `3b977bb8a7159632141aa31fd1b304dbdd41cee92fe372fe78494ecbb58f24bd` | `88330dc5a54238774020e70e4e5a8787927a348840d4207d196a1760b8295368` |
| `_september_workspace/_p_l_v3_phase1_finalize_2026_09_17.py` | `cf8fd1178ab1de5e4514190d8d82c4baa1a9ce01623c151301af3f9dbe57afe0` | `293367888ceb7fb79df7611dbf088c7d207e4a5d2c8ab92519acb67412fa6117` |
| `_september_workspace/_p_l_v3_phase1_runner_2026_09_17.py` | `d5e74a98c44bcc595cc54a530e8374d69953156961f2ae6bc6b2ff85565c823d` | `1e61287f52b28667ca831445b039219413e407fbf86d5971fb3d6e6a520fb63c` |
| `_september_workspace/_p_l_v3_phase2_finalize_2026_09_17.py` | `eaa04c5713d6fb7677ad9425d13df35ec06781fc666765a5ab0ef1328bf1f32e` | `ff0b88b76ec959c6fdc5148e9d07a159ba0ab595ec258f2ceed3035133ef722d` |
| `_september_workspace/deposon_team/_designs/D7_PRE_DISPATCH_EXECUTION_REPORT_2026_09_16.md` | `3fbc7f4dfd229839c7ac0e41ed94ce6f3592004b4245212160df2ab0c510e354` | `a936a4e5f66af306a6771e561feb75a6635402fa5c83be605314671f2ff95730` |
| `_september_workspace/deposon_team/_designs/DELEGATION_CONFIGS_FOR_USER_B_2026_09_16.md` | `23bb7d39bf58a1cd4328a47e799733a71eb754dc512f78ac7fc447f436b2c8b4` | `3707dbc6ba5325dd1f20003977e71f70d5e8a6713f5f68dfcdcacaac7008b70b` |
| `_september_workspace/deposon_team/_designs/EXTERNAL_AGENT_PROMPTS_2026_09_16.md` | `6a7b0c20a133469dde8111c11ccaf99fd3bdbe46457b05795c2a873024e8b755` | `4f6334a2d4c530683555ee8752abef881410f3b2346b933c7e501a25ddf48b2c` |
| `_september_workspace/deposon_team/_designs/V3X_CLOSURE_REPORT_REQUIREMENTS_FOR_EXTERNAL_AGENT.md` | `01af28f3fda3ba062223eb320e221a8bdc2f683b44d66b18632d0fa14e6f5739` | `fbf8712f019a1bd3060606c0056afa45d8245f62847cc37534dd4353ad102824` |
| `_september_workspace/deposon_team/_designs/V3X_FULL_CLOSEOUT_REPORT_2026_09_16.md` | `6d56b453d931cca435a0b8ebf73e9265f3d4cd3176f5d619f8237038b7c592d6` | `ea254b17008a8a9b588913e1d24a4844af6d45c0fa053187f6c551a8ac0fbc51` |
| `_september_workspace/deposon_team/_designs/V3X_KIMI_7_DIRECTIONS_FULL_ACCEPT_2026_09_16.md` | `eecbe2b1341d37a34a048eee702626c09f523cef685c63e8968eb82a930fa04a` | `ef58c0276cd074a7815f5b9ff11207deebdc463092e9b5fb8ab25d681788605a` |
| `_september_workspace/deposon_team/_designs/V3X_PATCH_5ANCHOR_RECONCILE_V2_2026_09_17.md` | `c41c1d6aa7945a8083e7fcc95a9afe58ce3e5f0e733b607aaebeb23ef0a4e382` | `e4a9bc76de742ef49eb121a85ec8b57c1b3a67f1a1ad708be798264939a3d67d` |
| `_september_workspace/deposon_team/_designs/V3X_TEAM_IMPROVEMENT_PLAN_2026_09_16.md` | `11cd57800bd618f2cf5a41e6e75b1883e0f197ad63504e4c24732bd8ac988c70` | `9e48864c574258c032a9fbbe20013e294fdec741a98751805819905bcc5e0755` |
| `_september_workspace/deposon_team/_designs/v3x_dispatch_log_2026_09_16.md` | `85c3a5cfd84dc75524213e379594fdeb265b0ffcc1f9f3da5f68a2fafa5c13a7` | `9a5a1d80f9685cf4f26bf478c9043e74ec24e7040f3f146a3f2acda42fd1dd1d` |
| `_september_workspace/deposon_team/plugins/_d7_post_anchor_rotation_remediation_2026_09_16.py` | `821fd0b19eb399479b91e704ab37a4a06cd3bcf59ca0b4774b340011d88391e3` | `ef091fd7becdc16d4361fe4073fe319dba090ba06fb0cf29a5fb1a5250a163f7` |
| `_september_workspace/deposon_team/plugins/_pg_v01_compute.py` | `d511c545f88e5a0cc78335d693831ce60f67e1d1e5576bb0b9c45836e9c36380` | `b4f49f225f668a2e55d5aaf58a73992016881a701e166dc6d61d20c54cc1c961` |
| `_september_workspace/deposon_team/plugins/_v3r1p1_21_ktb1_distortion_2026_09_27.py` | `f7b61f041c0bd52f6808b00caf92fdd171d911c72f470f13f3bbd59c8f09b97b` | `2d81e6951133aa59773e661dc68d2cb69640f39aa099a72ec3d4c8f2abc2a54f` |
| `_september_workspace/deposon_team/plugins/_v3x_experiments_runner_2026_09_16.py` | `0fac09bec7c41dd1a76822d9a0dc6aa039a5ab6e790f58cf8dd1e88a36aa3ca5` | `f8c5b12a5cf103f3fc4479976467b5603a0a3f9593abee60cac834f9d7118f77` |
| `_september_workspace/deposon_team/plugins/boss_pa_1_rbr_rm.py` | `5cc594147e001903d429f08da675d8bc575f5f2c3ecfc97aad3f11cab1cf0b12` | `67edba3613b3a5a575b73257870f1fc769ac3d9be4c5c745af5262ea6883e5f9` |
| `_september_workspace/deposon_team/plugins/boss_pa_2_potential_game.py` | `33dfb4338c5346710d73b510b8008dba390fd147c76f279cd35718419f233986` | `adb60d27f570961a293d9c274b37c2b52fa9a1a6976d055ca85a274b058cba43` |
| `_september_workspace/deposon_team/plugins/boss_pa_3_replicator_dynamics.py` | `a2bd9dd24c25280bb1f218dfb78d7fe3615c4c1de6aa18f714f3c539ebc475c7` | `6a298033eae38823cdf5ca774afbc188b8989b2e8a9c939bc649ac2f87cabd1b` |
| `_september_workspace/deposon_team/plugins/boss_pg_1_riemannian_degenerate.py` | `97fede6c8a4ecafc3182b4e61df3ad9f9888eb4bac4b1e7842e46aa4b048acb7` | `aa33b5394768256401d0dd27560d6e5989bc14602e03529a2e2f493aa585b29c` |
| `_september_workspace/deposon_team/plugins/boss_pg_2_hyperbolic_classification_collapse.py` | `f006d4caca94eeee2b29578a56cd8d16cb207e5f62ee7b668062c880a342897b` | `61e07090eddb97a56ef3a77c8c7d991b90e01f930ff4ab7d93e743e0ba2a5cd3` |
| `_september_workspace/deposon_team/plugins/boss_pg_3_geodesic_violation.py` | `09f37c01a258c2676c264f034d85e4ec9b97e850b7d8954fd8196dba55ddde87` | `3aae2246868fee81911965ae4462949ca8580644cf37b99ddbacde24211352c6` |
| `_september_workspace/deposon_team/plugins/fix_boss_naming_2026_09_16.py` | `21ad055e7e062877b9e2f96186d6c1b8693b5460d0adfda21c7b471c83473206` | `4b5bbd6da1c2b1285e67e7495db893ddf17f1f229a218fe22d79ec87ba0dbe6b` |
| `_september_workspace/deposon_team/plugins/git_commit_msg_2026_09_18.txt` | `b2841d12a44441913b79b54f5d99b6093577cb65a8433ca9916805054cc1756b` | `ac186ac9fff235f466861e8c63d6f35ddfb20619dd16641ba6f7e37c9ba2f1af` |
| `_september_workspace/deposon_team/plugins/runner_pa_d1_d3.py` | `1b9578eadc14e5f8d1bcae870a0336dbd41454b5bed487853330ca7240a2ef71` | `8a8029a58d1ce9e08467b9f1dc2b89849cde304a4ffb752ae160686bfbeb73a1` |
| `_september_workspace/deposon_team/plugins/skill_a_p_a_60cells.py` | `b1463bb24403aecefecbae7a1042e423c44eb46bd455faf651b1d118f4ea16a9` | `149cb3d74c275e5418a10f5c3705f120fa157e54891512a7faecf3f0530decd6` |
| `_september_workspace/deposon_team/plugins/skill_b_p_c_alpha_beta.py` | `e5a299f69a222951ad24e966082b28d48f0624ab4eb20a6636f0f1e8f86cf7da` | `7b9d049ef4d8651baf30884c10ba6a4b7b804303206d1cc111e611b65ad5b0e3` |
| `_september_workspace/deposon_team/plugins/skill_c_p_e_3modality.py` | `e19e76c5da7edda8f0a638a89a87c17b6f8ad9ba9cf990b91dec3607ae6d8b8d` | `a850b67bccf34ef5b806197eacd6f421436cc2c5f63ac1699b1df55e096712d8` |
| `_september_workspace/deposon_team/plugins/skill_d_p_f_observer.py` | `3e369a1f61716918dacea6becdadf373b069ef565ed2df726fe7263b7e12d0c0` | `f57a936c58fd3b54efb3bee410080e35cb74f3b84a2b21dc170d196c18957baa` |
| `_september_workspace/verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json` | `da517c115f3c4b73b0a9cb7990676bfc82d4524f8b097f439002972811f04a75` | `316060a6f000b00974703866476a16129dde0446a84fd3eb4048a3b435fb6795` |
| `_september_workspace/verifier/handoff/P_F_PREDECISION_2026_09_09.json` | `b41c98bf90ccd1ae740e5f8aa9b34485df56ac2c427d9261aa845870b94364d1` | `58db4c5f63017d1e1f58569429792953fdabad2a9e9fe05102c53b645d8f1c1d` |
| `_september_workspace/verifier/handoff/P_F_PREDECISION_2026_09_11_V0.1.json` | `312d635e62591e2813bb4cd7b500f0f6da9accf347c30c7d55b3f06e0ffb29a8` | `a8d9640c25e9e6fad863ac0ec605a246a29e69385a9c032cf68d0e5cb2fdb13b` |
| `_september_workspace/verifier/v36/check.sh` | `2212dcd98cd1dff5ca8a61f6b83c09575508be4392bf4011d44713c238829f56` | `1123a1c9be338b08971b14d876ed64579c0e66a3c1c8d01aae2053ef9d577e7d` |
| `_september_workspace/verifier/v41/check.sh` | `2c9fe869daaa873447a62b7e52c01dd3511f7709ebdb5b95e86279c7e8405333` | `7f3fb35ead433bd9ebb129a35bf9740a1a88ee1269ba3754447901997f620b9e` |
| `_september_workspace/volcengine_glm_latest_30cells_v2_runner_2026_09_10.py` | `26ff34bfcc79592aac43526137bf7c96d3f8ba15a186b7a228650c99f3fd2a9c` | `f6a6d92600ae372e7ab84e89fa4b1245d68f38492cb84b5e105bb0bcb77a08c9` |
| `docs/THINKING_V3_GT_CONTRIB_2026.md` | `8c1d733f9182dac4f84508f7e981924681849a6580facddaa7ca615d452c8bd8` | `b04c39175ede7f4f3bd2a8fc2b83739ebc6b312cf6bbc350372beea35d1f5a57` |
| `docs/V3X_COLLAB_DIRECTIONS.md` | `5a27c2350036038d38b26683b8ccfef72035c6b477ab6eb489713d39a19f6db8` | `b95448b5fd84f6f8e163bb6ccb8d4eb171bb1b141270fec4f5acd522e374ec19` |
