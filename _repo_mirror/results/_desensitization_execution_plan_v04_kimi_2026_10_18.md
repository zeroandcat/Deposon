# 脱敏执行方案（KIMI  upload-side · v0.4 轮 P0-3 命中 53 件）｜ 2026-10-18

> 依据：PI 卡 `ask_49c507b84a1831e89f233a0d` Q4 之裁（2026-10-18 10:31:41.880 生效）——**「沿 R2 体例脱敏后推（本地原件不动·远端持脱敏版——须新立脱敏执行面）」**。
> 效力：🔴 **本方案 ＝ 候 PI 核准**；PI 核准前 ⛔ 0 执行脱敏件之推送；53 件 ⛔ 0 入上传面（登记面禁令遵守中）。
> 体例：R2 先例件 `results/_upload_side_desensitized_remote_sha_letter_kimi_2026_10_12.md`（SHA-12 `fcb0a673ee5c`／74,043 B，本地在盘）。

---

## A1 ｜ 脱敏规则表（逐字段 · 可机械执行 · 逐条无歧义）

**词条之标识口径**：⛔ 本件 **0 载任何词条明文**（本件自身须过 P0-3 门禁）；每词以 **标签 ＋ UTF-8 字节长 ＋ 词条字符串之 SHA-256 前 12 位大写（SHA-12）** 唯一标识。**词条明文之权威本 ＝ 本地 R2 先例件 `fcb0a673ee5c` 之「映射口径」行（0 上传）**；执行侧按指纹对词执行，复核侧以指纹验词。

| 规则 | 源词条（标签 ｜ UTF-8 字节长 ｜ 词条 SHA-12） | 匹配语义 | 替换为 |
|:-:|---|---|---|
| **R-01** | T-01 ｜ 9 B ｜ `99238B67F359` | 字面子串（区分大小写） | `〔当事人W〕` |
| **R-02** | T-02 ｜ 9 B ｜ `D575FEB32C20` | 字面子串（区分大小写） | `〔W老师〕` |
| **R-03** | T-03 ｜ 6 B ｜ `81B430B69643` | 字面子串（区分大小写） | `〔IM〕` |
| **R-04** | T-04 ｜ 6 B ｜ `2A82E52F9257` | 字面子串（**不**区分大小写，含全大写／首字母大写等一切变体） | `〔IM〕` |
| **R-05** | T-05 ｜ 12 B ｜ `96C8BCCD40E0` | 字面子串（区分大小写） | `〔高校R〕` |
| **R-06** | T-06 ｜ 6 B ｜ `57B69D0A1A37` | 字面子串（区分大小写） | `〔高校R〕` |
| **R-07** | T-07 ｜ 3 B ｜ `A1EB9D48634F` | **词界锚定** `\b`（区分大小写——⛔ 0 命中 STRUCTURE 之类内嵌串） | `〔高校R〕` |
| **R-08** | T-08 ｜ 6 B ｜ `3F9EF925E25F` | 字面子串（不区分大小写） | `〔高校R〕` |
| **R-09** | T-09 ｜ 6 B ｜ `D8FD408600A4` | 字面子串（区分大小写） | `〔机构G〕` |
| **R-10** | T-10 ｜ 7 B ｜ `E63D0EB5CE48` | 字面子串（不区分大小写） | `〔机构G〕` |
| **R-11** | ark 语境 UUID（`[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`，小写十六进制 · 词界锚定） | **逐行**处理：仅当行含 `ark`（不区分大小写）时替换该行内匹配 | `〔密钥已脱敏〕` |

**执行序**：R-01→R-11 顺序施加（长串先行的防御序已内含于规则设计：T-01/T-02、T-05/T-06 互不重叠，顺序无关结果等价）；R-11 仅施加于门禁标记之 1 件（`pi_rulings/_pi_card_answers_register_2026_10_17_v72.md`）。

**与门禁扫描器之同语义声明**：本规则族之匹配语义与 v0.4 P0-3 门禁扫描器逐条一致（CN 六词（T-01／T-02／T-03／T-05／T-06／T-09）＝`str.count` 子串；T-04／T-08／T-10＝不区分大小写子串；T-07＝`\b` 词界；ark-uuid＝ark 行锚定 UUID）⇒ 替换后之复扫归零 ＝ 门禁口径之归零。

## A2 ｜ 不可逆性之证

1. **原串销毁式替换**：全部规则为「原字符串 → 占位符」之单向替换；脱敏件中**原词条之字节 0 残留**（双口径复扫实证，见 A4-①）。由脱敏件文本本身**无任何信息可重建原词条**。
2. **对应关系之不可反推**：53 件中治理登记族所载之映射对应句（形如「明文 ↔ 占位符」之登记行），经替换后**两侧皆成占位符**（形如「〔W老师〕 ↔ 〔W老师〕」）——对应关系之信息内容在远端件中**归空**，⛔ 不可由远端件反推映射。
3. **⛔ 0 可逆机制**：全程 0 加密、0 编码、0 对照表上传；占位符为通用角色标签（人物／机构／平台类属词），不携带可解码信息。
4. **唯一可逆之径 ＝ 本地原件**：原件 53 件 0 改动留存本地两区（A5 自证），恢复之可能性仅存于本地，与远端无涉——此正为 R2 体例之本义。

## A3 ｜ 逐件回执（53 件）

- 指纹口径：`orig` ＝ 本地原件 SHA-12；`desen` ＝ 脱敏副本 SHA-12 ＋ git blob sha1；`提交指纹` ＝ 远端 blob sha1——🔴 **推送前不存在**，依 R2 先例于推送后之《上传侧回函》补全（本方案先载 orig／desen／规则面）。
- 脱敏副本落点：执行侧工作区 `_r4_desensitized/<rel>`（本地原件 0 触碰）。

| # | rel（仓内相对路径） | 区 | orig SHA-12 | desen SHA-12 | desen git sha1 | 规则触发 |
|--:|---|:-:|---|---|---|---|
| 1 | `pi_rulings/_pi_card_answers_register_2026_10_17_v46.md` | REPO | `3B5E35EEBCBD` | `A6A0B549135B` | `62910e2b2dff04ba7310d3f5974c6837c1a313a8` | R-02×4·R-04×4 |
| 2 | `pi_rulings/_pi_card_answers_register_2026_10_17_v54.md` | REPO | `B45C83999E9F` | `49166F021361` | `6396645627f1ce60292b0e4ea670b6479c0a4ef7` | R-04×1 |
| 3 | `pi_rulings/_pi_card_answers_register_2026_10_17_v72.md` | REPO | `EAA2535DE267` | `7C7646EFB8DA` | `fcc9e3a4ac13b92092dfda3738cc3ff060b9cd43` | R-11×1 |
| 4 | `pi_rulings/_pi_card_answers_register_2026_10_17_v80.md` | REPO | `A40F5698A1DA` | `DB736F06E310` | `6188dbda5e778e391e72752088a388b5bd9c887f` | R-04×1 |
| 5 | `pi_rulings/_pi_card_answers_register_2026_10_17_v81.md` | REPO | `816A5414A86A` | `4C9DD19B452B` | `c68062107ee4382af9c629bdfe530633003c47ea` | R-04×2 |
| 6 | `pi_rulings/_pi_card_answers_register_2026_10_17_v82.md` | REPO | `79DD0FDF23C9` | `C2496683A4DD` | `b43ea3881756db051f5aca1e8555d92845b8dcfc` | R-04×1 |
| 7 | `pi_rulings/_pi_card_answers_register_2026_10_17_v83.md` | REPO | `E2A67AA39BDD` | `0F1FAE595158` | `1b916be2cd26bb5332c866c2b1dd0760be241df7` | R-04×1 |
| 8 | `pi_rulings/_pi_card_answers_register_2026_10_17_v85.md` | REPO | `C54C4580BAA2` | `B5F692ED7141` | `75fb0b94f1710c0cde2bdec893c74a4f487098d2` | R-04×1 |
| 9 | `pi_rulings/_pi_card_answers_register_2026_10_17_v86.md` | REPO | `19821507B5B2` | `C44E784573BB` | `8f44312eeae734a2fd960f4c5da14aae308d9809` | R-04×1 |
| 10 | `pi_rulings/_pi_card_answers_register_2026_10_17_v87.md` | REPO | `346456D03425` | `23E15CFA434D` | `0e617b1f4efc2d13c0f4ba7d4cf2eac1b6f6c80a` | R-04×1 |
| 11 | `results/_achievements_inventory_full_2026_10_09.md` | REPO | `DD3E9806A369` | `E5B507FBF6D6` | `acb25540ac2243963a132aac39efa3bd6c08ae07` | R-04×14 |
| 12 | `results/_batch8_deliberation_judgment_2026_10_14.md` | REPO | `A68B2971B8E1` | `55EF5902B0A2` | `3305435b7d677f6aeab2c49eb4dd8476e6b207e2` | R-02×4 |
| 13 | `results/_batch9_deliberation_judgment_2026_10_14.md` | REPO | `A93CD166A83B` | `4D215A96CAE5` | `37a49fbe40b035e874b8330d6b21f5519afdc6e4` | R-02×1·R-04×1 |
| 14 | `results/_clue_side_dual_and_glm_commission_open_register_2026_10_12.md` | REPO | `35BC0F1135CD` | `FF9780E9642A` | `3e6459931d3f050943b8d20d1ed7cb2f7789e631` | R-01×1·R-02×1·R-03×1·R-04×1·R-05×1·R-06×1·R-07×1·R-08×1·R-09×1·R-10×1 |
| 15 | `results/_collision_baseline_update_and_disposition_2026_10_17.md` | REPO | `F4F0FDC9915D` | `5B762A71AF4D` | `47f13ee7d3ba99092ba1a963f08de52649b196c0` | R-02×3·R-03×2·R-04×3 |
| 16 | `results/_gate1_five_zero_recheck_glm_scope_2026_10_13.md` | REPO | `2F27ACF42897` | `375565613CE9` | `0819ac19f2e1e9c36521cf3c3e06c1f1f480f162` | R-04×3 |
| 17 | `results/_gate_one_reopened_and_stage2_rejection_register_2026_10_12.md` | REPO | `B2F6F55E76B7` | `65ED4DBF4DD4` | `bcdfdbb0940af279705fd39c08460bcea963cbec` | R-04×1 |
| 18 | `results/_ge01_d1_theory_input_disposition_2026_10_14.md` | REPO | `657FE57C8CBD` | `A0F6CBE4463E` | `df3149a13a5dca91491703b7d1256b5f40deb8ad` | R-02×3·R-04×1 |
| 19 | `results/_ge01_d1_theory_input_sourcing_design_2026_10_14.md` | REPO | `F9B8A276A941` | `B9FB19898F97` | `8427f472ce392c9253cbb8a4dc54b76886c56119` | R-02×12·R-04×5 |
| 20 | `results/_ge01_spec_anchor_erratum_2026_10_14.md` | REPO | `2EEB522748CA` | `14A32196F194` | `f0c93a1f65c22cf3858d54e16886383222a8ef54` | R-02×1·R-04×1 |
| 21 | `results/_ge01_unblock_progress_2026_10_14.md` | REPO | `893EDDF769A6` | `2ADF698DB3A1` | `ed36772f3efee7e9558ae691dfb2cb58d40f15a1` | R-02×1 |
| 22 | `results/_github_suspect_rulings_effect_2026_10_17.md` | REPO | `F49079F46C2B` | `6891F243D57C` | `a732da6d363ada8383a6a0621cdfd849832ffbfb` | R-04×1 |
| 23 | `results/_itemH_fingerprint_provenance_2026_10_12.md` | SUB | `BACBEE9A158F` | `FC30451414ED` | `d5f27db26e9a50da63fc5963c2aa2c2fd460deb4` | R-02×3 |
| 24 | `results/_kd1_preexp_contrast_2026_10_17.md` | REPO | `351D18D74934` | `3248C8EF7CB8` | `e15cac5d6ab494822d3a54cc64db9f73b23fe903` | R-02×1 |
| 25 | `results/_kd_s3b1_kd1_n7_rulings_effect_2026_10_17.md` | REPO | `E09780D24A7A` | `A744ABC3E29C` | `1507a17b2448212d5652472a5c4f51dc328ca575` | R-02×1 |
| 26 | `results/_kd_s3b1_verdict_2026_10_17.md` | REPO | `ED36D0171672` | `B6C8798C7157` | `9172d0748ed3dcb07494e7d3a563ab7a00fa3966` | R-02×4 |
| 27 | `results/_kt_a1_anchor_drift_root_cause_2026_10_14.md` | REPO | `BA19AB186747` | `CDC60AE03D6F` | `4e262d90f4cac86ca155d219ed789130453e60de` | R-02×3·R-04×2 |
| 28 | `results/_kt_a1_v0_lineage_corrigendum_2026_10_14.md` | REPO | `E2C35C2AC858` | `8102FADEC97D` | `b85cd41cbd73f3a748661f168309e8569688f738` | R-02×1·R-04×1 |
| 29 | `results/_noncore_upload_caliber_draft_2026_10_17.md` | REPO | `3AC146A3F8E5` | `55F01B9B55CE` | `ca6633580c8c4fbde5cac25b325a1eb156e2a032` | R-02×2·R-04×2 |
| 30 | `results/_noncore_upload_caliber_effect_register_2026_10_17.md` | REPO | `F007DA0A98D6` | `B5F91A850DB1` | `4b72a49b92219cb0e397062dbb8837e09b47f680` | R-02×1·R-04×1 |
| 31 | `results/_p0_scan_2026_10_12.json` | REPO | `224B7FC0DCDF` | `4D9405510B47` | `8f3a3743c8ac1cb0ff1cb9ee92da483f24e5ce8b` | R-01×2·R-02×6·R-03×2·R-04×7·R-05×1·R-06×2·R-07×3·R-09×2 |
| 32 | `results/_pi_batch_rulings_and_gate1_definition_register_2026_10_12.md` | REPO | `37876A02AD17` | `F625EDED06F7` | `8dc82b7c3c0f3d1bf40d1f0e8c1f5e79f9435961` | R-04×1 |
| 33 | `results/_pre_execution_report_kimi_2026_10_12.md` | REPO | `799FBFC334A7` | `E49EC4B3C8EE` | `70b0915abdbc9fd3d393bbf621396eb2e611613f` | R-01×2·R-02×6·R-03×2·R-04×8·R-05×1·R-06×2·R-07×3·R-09×2 |
| 34 | `results/_pulled_back_P_B_DISTORTION_BOUND_V0_SPEC_2026_10_13.md` | SUB | `BB7CA9838150` | `52CB264FB7ED` | `e90fe5903e28700bb4c2b29a43daa167d116d155` | R-02×10·R-04×5 |
| 35 | `results/_r2_build_manifest_2026_10_12.json` | REPO | `303DB70B37F6` | `4165E37F571A` | `5b89369890ee1d1144d2f8b56fe90e3bd0121e9d` | R-01×17·R-02×124·R-03×11·R-04×159·R-05×3·R-06×9·R-07×4·R-08×2·R-09×10 |
| 36 | `results/_r2_execution_receipt_kimi_2026_10_12.md` | REPO | `4EFCCB8DF379` | `EB35A1730DC0` | `4cc87c0abd0b0ad4b93f1fabb07b7587d207f568` | R-01×2·R-02×2·R-03×2·R-04×3·R-05×2·R-06×2·R-07×2·R-08×2·R-09×2·R-10×1 |
| 37 | `results/_r5_spec_pack_retrieval_register_2026_10_13.md` | REPO | `D7EF2C8E56BB` | `5EBB0A37CEEA` | `e9d4379d24b3b2cebdda1c6cc55ba7d717026b3b` | R-03×2·R-04×1 |
| 38 | `results/_r5_spec_pack_retrieved_2026_10_13/鲍勃_minimax实验委托规格包_2026_10_12.md.asset.json` | SUB | `5CA1AA500FD8` | `31B82BB08614` | `2d360c03f4d19c35dd5e92f50bf5228b71318cf7` | R-04×1 |
| 39 | `results/_root_session_history_memo_2026_10_14.md` | REPO | `2833F89D623B` | `2531409F1E2D` | `066c6f031ba0e09f00443bf3b01d5a2d5279dccf` | R-02×3·R-04×4·R-05×1 |
| 40 | `results/_root_session_history_memo_main_2026_10_14.md` | REPO | `12AB21C73DB8` | `66B2DDDDC68A` | `eff469b4255cadd0d634c7fe014e2b74b7ca8391` | R-02×4·R-04×3 |
| 41 | `results/_stage3_completion_and_stage4_open_register_2026_10_12.md` | REPO | `E2F4AD9E1360` | `31BC1FAA6B49` | `6b412b2a8c5a51f1f116fa823de2c1579fbf7c11` | R-02×2 |
| 42 | `results/_stage3_r2_cleanup_register_2026_10_18.md` | REPO | `D6B1DC8F8A02` | `6F1A281F59CD` | `c703e9611da8ba9441c38cedc22689cb549bf7e9` | R-04×4 |
| 43 | `results/_supplement_to_500_design_review_2026_10_16.md` | REPO | `7A2D83148969` | `028BE165720A` | `4133b3599fd37698f0ba6c4e064da626c71cbe8a` | R-02×1 |
| 44 | `results/_temp_cleanup_register_2026_10_13.md` | REPO | `89CBDF1EEFAB` | `7F4E5EC3C968` | `22fde9ae557bb8276951e8627a2880c84e098988` | R-03×1 |
| 45 | `results/_trae_issues_batch3_six_items_draft_2026_10_12.md` | REPO | `2153C41A8CFF` | `1646FA447AF0` | `79bddad30c1dcacc61b6f2ba583c2cef75cf720f` | R-02×1 |
| 46 | `results/_trae_issues_disposition_schedule_2026_10_12.md` | REPO | `57B9DCCA2630` | `C4F3744B4EFE` | `ab901b9a72ef3e7bc20f479eb34b4b774fd96ef8` | R-04×6 |
| 47 | `results/_two_items_alternative_deliberation_judgment_2026_10_13.md` | REPO | `F2CDAAD477F6` | `C874F805CF9D` | `f6b73a4b8228682b8d3f8666cad69dd5e1899c83` | R-04×2 |
| 48 | `results/_unclosed_47_direct_clear_b_tier_register_2026_10_13.md` | REPO | `0CF3FABA8C21` | `92AED6446F4C` | `20cedf10c2f5a656b37baf99c99cbb1c3f910d8d` | R-04×3 |
| 49 | `results/_unclosed_47_pi_give_draft_2026_10_13.md` | REPO | `31D66920001C` | `E741719CDBAE` | `a401d4a2b4d586650f42e12150e8ffa60d30a7cd` | R-04×1 |
| 50 | `results/_upload_execution_receipt_kimi_2026_10_12.md` | REPO | `639303213CE3` | `BEA6D4B8D531` | `fa634919ff9e93d08878e6ec0a66aef3d0338701` | R-01×1·R-02×1·R-03×1·R-04×1·R-05×1·R-06×1·R-07×1·R-08×1·R-09×1·R-10×1 |
| 51 | `results/_upload_side_desensitized_remote_sha_letter_kimi_2026_10_12.md` | REPO | `FCB0A673EE5C` | `1E53D8F455DF` | `c8331b3a63c0206c5604b49dd469ccdfed0647fa` | R-01×18·R-02×125·R-03×12·R-04×160·R-05×4·R-06×10·R-07×5·R-08×3·R-09×11·R-10×1 |
| 52 | `results/_v5_handover_guide_project_initiation_2026_10_12.md` | REPO | `DDDF7B0A7221` | `7DE72DC50D5C` | `fc1fac3d98987f6c2e3660d6e7cd47ca66a82a54` | R-04×1 |
| 53 | `results/_zone_balance_inventory_2026_10_13.md` | REPO | `4A7CFA13C79E` | `346D13A43F57` | `48ea4e6774c30e46fc41bfeeb9654a67c230ced6` | R-04×30 |

## A4 ｜ 验收判据（逐条已自检 · 读数照录）

| # | 判据 | 自检结果 |
|:-:|---|---|
| ① | **密钥正则 0 命中**（ghp_／github_pat_／sk-／xox-／AKIA，带长度锚） | ✅ 脱敏件 53/53 **0 命中**（主扫＋独立第二扫双口径）｜ 注：独立第二扫初版以裸字节 `sk-` 命中「disk-tested」1 处，已判为误报并以带长度锚正则复测 0 命中 |
| ② | **映射不可逆性之核验方法** | 方法：对脱敏件施加门禁同语义扫描族 ＋ 多重独立变体（子串／词界／大小写全组合）须全零；且对应关系句两侧占位符化（人工抽查 v46 件 8 处命中行确认）。结果：✅ 全零（见下） |
| ③ | **逐件回执之完整性核对** | ✅ 53 行全字段非空（提交指纹列除外——推送后方存在）；规则触发计数与门禁命中计数**逐词 1:1 相符**（R-01×43／R-02×331／R-03×36／R-04×450／R-05×14／R-06×27／R-07×19／R-08×9／R-09×29／R-10×4／R-11×1） |
| ④ | **原件 0 改动之自证** | ✅ 构建前后两轮复哈希，53/53 原件 SHA-12 与备战在册值**逐位相符**（`orig` 列即实测值） |

**双扫纪律之如实登记**：主扫（构建脚本内嵌校验族）53/53 归零；独立第二扫（0 共享正则对象之三重实现）53/53 归零。构建过程曾出两起**过杀**缺陷并已修正重建：R-07 初版未锚词界误伤 STRUCTURE 内嵌串（2 件 5 处）、R-11 初版未锚 ark 行误毁 13 处合法登记 UUID——修正后规则触发与门禁计数 1:1，副本已全量重建。

## A5 ｜ 本地原件 0 改动之自证

- 53 件原件遍布两区（REPO 50／SUB 3），构建脚本仅读不写；构建后逐件复哈希 53/53 与备战在册 SHA-12 逐位相符（见 A3 表 `orig` 列）。
- 归档区 `〔本地归档区〕` 本轮 0 读 0 写 0 列目录。

## A6 ｜ 体例遵循声明（R2）与异同

- **所循体例 ＝ R2**：映射词表、占位符集、「本地原件不动·远端持脱敏版」之格局、上传侧回函补全提交指纹之回执体例，皆沿先例件 `fcb0a673ee5c`。
- **异**：①流程——R2 为单委托内构建即推；v0.4 依 Q4 之裁**方案先行、PI 核准后推送**（本件即方案）。②规则锚定——R-07 词界、R-11 ark 行锚，本轮以门禁扫描器同语义明文化（R2 未载此节）。③双扫纪律——本轮以两件 0 共享实现之扫描脚本互证归零并如实登记过杀修正史。

## 候 PI 核准事项

1. 核准本方案 ⇒ KIMI 于上传面末批以脱敏副本推送 53 件（目标 `_september_workspace/<rel>`），推送后出具《上传侧回函》补全逐件提交指纹（远端 blob sha1）。
2. 若 PI 对任一规则／回执有裁改，KIMI 按裁重建对应副本并复扫后再候。

0 密钥明文、0 PAT 片段、0 推理文本引用、0 词条明文。
