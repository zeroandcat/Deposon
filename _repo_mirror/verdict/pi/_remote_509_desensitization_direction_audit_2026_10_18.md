# 远端 commit 739a7daf 之「脱敏方向」全量审计（2026-10-18）

> 📌 **本件性质**：**证据链审计件（登记面）** —— 对 GitHub 公开仓 `zeroandcat/Deposon` 之 commit `739a7daf533b6ead320667d924ab0884c9614edc` 的补丁面做**脱敏方向**全量核验。
> ⛔ **0 判档**（未出 `pass`／`af`／`kd`／`fail`／`give-up` 五终判之任一）｜⛔ **0 闭任何既有项**｜⛔ **0 宣告任何段毕**｜⛔ **0 跑实验／0 跑 executor／0 新观测入账**｜⛔ **0 代裁／0 代 PI 给值**｜⛔ **0 改实验结论本体**。
> ⛔ **0 写远端**（全程仅匿名只读 GET）｜**0 用 PAT**｜⛔ **0 读 key／0 读 `.env`**（**R4**）。
> ⛔ **0 回改／0 移动／0 删除任何本地既有件**（既有件触动数 ＝ **0**，见 §11-3）｜⛔ **0 触归档区**（`〔归档件引用·未上传:〔归档区〕〕` 之目录项：**0 读／0 写／0 列目录**）｜⛔ **0 触** `〔本地他区引用·未上传:GLM〕`。
> ⚠️ **本件含敏感字面**（`本地仓根`、`〔本地绝对路径·脱敏略:Administrator〕` 等）—— 系「记录被引入公开仓之字面为何」之**必要载体**，非泄指面扩散；⛔ **0 含任何凭据／密钥字面**（见 §11-1 实测）。
> ⚠️ **清单中之文件名为逐字照录之路径证据**；文件名内偶然出现的英文词（含与五终判同形之词）**不构成本件任何判定**。

| 项 | 值 |
| :-- | :-- |
| 出件 | **evidence-auditor（证据链审计官）**（`agent-11335500b168`，分支会话 `mvs_f72b800ba69a4a84ad53207d3bafe9ac`） |
| 日期 | 2026-10-18 |
| 审计对象 | 公开仓 `zeroandcat/Deposon` · commit `739a7daf533b6ead320667d924ab0884c9614edc` |
| commit 时间 | 2026-10-18T08:50:08Z（author ＝ committer ＝ `zeroandcat`） |
| commit message | `overwrite: 509 desensitized + groupA 2 (rulings FRC cai-7+cai-8 2026-10-18; batch ruling, P0 passed)` |
| parent | `9ec782b2b1b5944c2f66c6f18d608c9df4ffefbc`（2026-10-18T08:49:58Z · 56 件 · message `upload: supplemental batch-3 tier-bing 56 files …`） |
| tree | `b74a427f7adcb95e3a05287da43e77a85d41e796` |
| diff stat | **+2,456 ／ −2,128** ｜ **354 件**（`status` 全为 `modified`，**0 added／0 removed／0 renamed**） |
| 现 HEAD | `713f2f318854728db29f7574fecce5864513d9eb`（2026-10-18T08:59:42Z）—— 比被审 commit 晚 **9 分 34 秒** |
| 本件 | `results/_remote_509_desensitization_direction_audit_2026_10_18.md`（新名新建 · 0 覆写） |
| 版式 | UTF-8 **无 BOM** · **纯 LF（CR ＝ 0）** |

# §0 一语结论（详证见下）

**该 commit 名义为「509 desensitized（已脱敏）」，实测方向与名义相反：354 件中 335 件（94.6%）为「占位符 → 敏感字面」之**反脱敏**（脱敏被撤销、真实本机路径与真实人名被写入公开仓）；仅 13 件为正向脱敏、2 件混杂、4 件与脱敏无关。**

且至现 HEAD（`713f2f31…`，晚 9 分半），抽核之 B 类代表件**仍载**敏感字面，且其 git blob SHA 与本 commit 清单**逐位一致** ⇒ 事后**未**被清理。

# §1 停手闸（落盘前实测）

- 交付路径 `results/_remote_509_desensitization_direction_audit_2026_10_18.md`：`Test-Path` ＝ **`False`**
- 全仓递归 glob `*509_desensitization*` ＝ **0 命中**
- ⇒ **0 覆写任何既有件**；本件系**新名新建**。

# §2 覆盖与方法（每法之覆盖面如实标注）

### §2-1 两法并用
| 法 | 覆盖 | 说明 |
| :-- | :-- | :-- |
| **法一：patch 逐行配对** | **352 件**（354 − 2） | 取 GitHub commits API 之 `files[].patch`，拆 `-`／`+` 行，按**同序配对**（第 i 条删除行 ↔ 第 i 条新增行）判方向 |
| **法二：blob 对拍** | **2 件** | GitHub 对超限／二进制件**不返回 `patch` 字段**；此 2 件改以 contents API 取 parent 与本 commit 两版字节，本地整文件计数并逐行集合差分 |

⇒ **全量 354 件 100% 有覆盖**，**0 件**因 patch 截断而无判。

### §2-2 方向判定规则（配对级）
| 判据（单对删除行 → 新增行） | 归类 |
| :-- | :-- |
| 新增行含**真实字面**（本机路径／真实人名）且删除行无 | **B 反脱敏** |
| 新增行含**强占位符**（`〔…〕`）且删除行无 | **A 正脱敏** |
| 两者**同时**成立 | **C 混杂** |
| 皆不成立 | 中性对（不计入方向） |

文件级归类：含 B 对且含 A 对或 C 对 ⇒ **C**；仅 B 对 ⇒ **B**；仅 A 对 ⇒ **A**；全中性且全文件净值为 0 ⇒ **D**；**0 配对**（纯新增）改用全文件净占位/字面差回退判定。

### §2-3 令牌集（脱敏方向之判据面）
| 类 | 令牌 | 性质 |
| :-- | :-- | :-- |
| 强占位符 | `〔…〕`（U+3014／U+3015）、`_september_workspace` | 脱敏件 |
| 弱占位符 | `EXTERNAL_ADVISOR`／`external_advisor`／`外部顾问`、`online`／`线上` | 泛称／平台指示词（本审计中作「被替换者」，本身不判方向） |
| 真实字面 | `本地仓根…`、`〔本地绝对路径·脱敏略:Administrator�〕��`、`〔本地绝对路径·脱敏略:Administrator�〕��`、`WANG_TEACHER`／`wang_teacher` | 敏感字面 |
| 人名占位符 | `〔W老师〕`／`〔〔W老师〕〕`／`〔W老师〕` | 占位符**内含可识别人名** ⇒ 计为「弱脱敏」，单列计数 |

### §2-4 API 用量自节（全程匿名只读 GET，**0 PAT、0 写操作**）
| 用途 | 请求数 | 端点 |
| :-- | :-- | :-- |
| commit 元数据（含 files·patch，分页 per_page=100） | 5 | `/repos/zeroandcat/Deposon/commits/739a7daf…` |
| 现 HEAD 确认 | 1 | `/repos/zeroandcat/Deposon/commits?per_page=1` |
| parent 元数据（对账用） | 1 | `/repos/zeroandcat/Deposon/commits/9ec782b2…` |
| 2 件 NOPATCH 之 parent／本 commit blob | 4 | `/repos/zeroandcat/Deposon/contents/…?ref=…` |
| HEAD 抽核 4 件 blob | 4 | `/repos/zeroandcat/Deposon/contents/…?ref=713f2f31…` |
| **合计** | **15** | 全部 `GET`；**0 POST/PUT/PATCH/DELETE** |

# §3 计数总表

| 类 | 定义 | 件数 | 占比 |
| :-- | :-- | --: | --: |
| **A 正脱敏** | 敏感字面 → 占位符 | **13** | 3.7% |
| **B 反脱敏** | 占位符 → 敏感字面 | **335** | **94.6%** |
| **C 混杂** | 同件内两方向并存 | **2** | 0.6% |
| **D 无涉** | 改动与脱敏无关 | **4** | 1.1% |
| **合计** | | **354** | 100% |

**配对级操作数**（法一覆盖之 352 件）：正向配对 **81** ｜ 反向配对 **1,068** ｜ 混杂配对 **2**。

# §4 B 类（反脱敏）逐件清单 —— 335 件

> 格式：`序号 | 仓内相对路径 | 配对级 B/A/C/中性 | 未配对行 | 全文件净（占位−字面）`
> 前 333 件由 patch 配对判定；末 2 件（标 `blob-diff`）因 GitHub 未返回 `patch` 字段，改以 parent／本 commit 双 blob 对拍判定（证据见 §4-1）。

| 1 | `_repo_mirror/.trae/scripts/_arxiv_renumber.py` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 2 | `_repo_mirror/.trae/scripts/_md_to_tex.py` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 3 | `_repo_mirror/.trae/scripts/_verify_tex.py` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 4 | `_repo_mirror/_p_l_v3_phase1_finalize_2026_09_17.py` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 5 | `_repo_mirror/_p_l_v3_phase1_runner_2026_09_17.py` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 6 | `_repo_mirror/_p_l_v3_phase2_finalize_2026_09_17.py` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 7 | `_repo_mirror/corpus/v20_caption_surface/_inspect_captions.py` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 8 | `_repo_mirror/deposon_team/_designs/DELEGATION_CONFIGS_FOR_USER_B_2026_09_16.md` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-8 |
| 9 | `_repo_mirror/deposon_team/_designs/v3x_dispatch_log_2026_09_16.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 10 | `_repo_mirror/deposon_team/plugins/_d7_post_anchor_rotation_remediation_2026_09_16.py` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 11 | `_repo_mirror/deposon_team/plugins/_pg_v01_compute.py` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 12 | `_repo_mirror/deposon_team/plugins/_tdf_s1_2026_10_12.py` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 13 | `_repo_mirror/deposon_team/plugins/_tdf_s1b_2026_10_12.py` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 14 | `_repo_mirror/deposon_team/plugins/_tdf_s1c_2026_10_12.py` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 15 | `_repo_mirror/deposon_team/plugins/_tdf_s2_apply_2026_10_12.py` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 16 | `_repo_mirror/deposon_team/plugins/_tdf_s3_jumps_2026_10_12.py` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 17 | `_repo_mirror/deposon_team/plugins/_tdf_s3b_2026_10_12.py` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 18 | `_repo_mirror/deposon_team/plugins/_tdf_s4_final_2026_10_12.py` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 19 | `_repo_mirror/deposon_team/plugins/_v3r1p1_21_ktb1_distortion_2026_09_27.py` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 20 | `_repo_mirror/deposon_team/plugins/_v3x_experiments_runner_2026_09_16.py` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 21 | `_repo_mirror/deposon_team/plugins/boss_pa_1_rbr_rm.py` | pairs A/B/C/none=0/5/0/0 | unpaired=0 | agg=-10 |
| 22 | `_repo_mirror/deposon_team/plugins/boss_pa_2_potential_game.py` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-8 |
| 23 | `_repo_mirror/deposon_team/plugins/boss_pa_3_replicator_dynamics.py` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-8 |
| 24 | `_repo_mirror/deposon_team/plugins/fix_boss_naming_2026_09_16.py` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 25 | `_repo_mirror/deposon_team/plugins/runner_pa_d1_d3.py` | pairs A/B/C/none=0/7/0/0 | unpaired=0 | agg=-14 |
| 26 | `_repo_mirror/deposon_team/plugins/skill_a_p_a_60cells.py` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-8 |
| 27 | `_repo_mirror/deposon_team/plugins/skill_b_p_c_alpha_beta.py` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 28 | `_repo_mirror/deposon_team/plugins/skill_c_p_e_3modality.py` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-8 |
| 29 | `_repo_mirror/deposon_team/plugins/skill_d_p_f_observer.py` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-8 |
| 30 | `_repo_mirror/docs/V3X/AGENT_TEAM_OPT_V2_2026_09_11.md` | pairs A/B/C/none=0/0/0/1 | unpaired=0 | agg=-1 |
| 31 | `_repo_mirror/docs/V3X/DEPOSON_EMBEDDING_6WAY_THEORY_V0_2026_09_10.md` | pairs A/B/C/none=0/5/0/0 | unpaired=0 | agg=-10 |
| 32 | `_repo_mirror/docs/V3X/KT_A1_SPEC_V0.1.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 33 | `_repo_mirror/docs/V3X/KT_B1_SPEC_V0.1.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 34 | `_repo_mirror/docs/V3X/KT_C1_SPEC_V0.1.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 35 | `_repo_mirror/docs/V3X/KT_D0_SPEC_V0.1.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 36 | `_repo_mirror/docs/V3X/P_E_DOUBAN_EMBEDDING_V0_SPEC.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 37 | `_repo_mirror/docs/V3X/P_F_D1_FULL_REPORT_2026_09_15.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 38 | `_repo_mirror/docs/V3X/P_F_SPEC_V0.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 39 | `_repo_mirror/docs/V3X/REVIEWER_A_STATIC_AUDIT_2026_09_15.md` | pairs A/B/C/none=0/9/0/0 | unpaired=0 | agg=-18 |
| 40 | `_repo_mirror/docs/V3X/REVIEWER_A_TRAE_FIX_AUDIT_2026_09_15.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 41 | `_repo_mirror/docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | pairs A/B/C/none=0/38/0/2 | unpaired=0 | agg=-94 |
| 42 | `_repo_mirror/docs/V3X/V3X_D6_PAPER_zh.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 43 | `_repo_mirror/README_V4_2026_09_29.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-8 |
| 44 | `_repo_mirror/results/_a02_excluded_items_idx_collection_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 45 | `_repo_mirror/results/_alt_delib_pkg3_two_judgments_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 46 | `_repo_mirror/results/_archive_2026_09_18/_trae_code_improvement_v2_2026_09_18.md` | pairs A/B/C/none=0/13/0/0 | unpaired=0 | agg=-26 |
| 47 | `_repo_mirror/results/_archive_2026_09_18/_trae_d7_v1_audit_20260917_190000.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 48 | `_repo_mirror/results/_archive_2026_09_20/_d05_sanity_3backbone_2026_09_18.py` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 49 | `_repo_mirror/results/_archive_2026_09_24/_inspect_captions.py` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 50 | `_repo_mirror/results/_archive_2026_09_24/_verify_worker_c.py` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 51 | `_repo_mirror/results/_archive_2026_09_24/_volc_22cap_emb.py` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 52 | `_repo_mirror/results/_archive_2026_09_24/_worker_openrouter_rag_run.py` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 53 | `_repo_mirror/results/_archive_ledger_rectification_register_2026_10_09.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 54 | `_repo_mirror/results/_archive_manifest_deposon_sub_2026_09_23.json` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 55 | `_repo_mirror/results/_archive_manifest_non_upload_2026_09_23.json` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 56 | `_repo_mirror/results/_archive_manifest_non_upload_v2_2026_09_28.json` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 57 | `_repo_mirror/results/_archive_manifest_non_upload_v3_2026_09_28.json` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 58 | `_repo_mirror/results/_axis1_three_recomputations_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 59 | `_repo_mirror/results/_b01_new_key_classification_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 60 | `_repo_mirror/results/_b01_new_key_residue_judgment_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 61 | `_repo_mirror/results/_b01_p_counting_recompute_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 62 | `_repo_mirror/results/_b01_recompute_authorization_supplement_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 63 | `_repo_mirror/results/_b01_recompute_sec4_2_erratum_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 64 | `_repo_mirror/results/_b14_audit_f2f3_closure_register_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 65 | `_repo_mirror/results/_b14_vk_evidence_audit_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 66 | `_repo_mirror/results/_c_component4_d2d3_gap_judgment_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 67 | `_repo_mirror/results/_c_component4_three_items_judgment_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 68 | `_repo_mirror/results/_c2_criterion_third_tier_draft_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 69 | `_repo_mirror/results/_c4_math_corrections_downstream_erratum_2026_10_10.md` | pairs A/B/C/none=0/5/0/0 | unpaired=0 | agg=-12 |
| 70 | `_repo_mirror/results/_c4_math_corrections_E1_E2_execution_erratum_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 71 | `_repo_mirror/results/_c4_unblock_reply_independent_review_2026_10_10.md` | pairs A/B/C/none=0/1/0/1 | unpaired=0 | agg=-3 |
| 72 | `_repo_mirror/results/_c8_c2_disposition_register_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 73 | `_repo_mirror/results/_charlie_delivery_register_2026_10_08.md` | pairs A/B/C/none=0/10/0/0 | unpaired=0 | agg=-20 |
| 74 | `_repo_mirror/results/_chd_construction_domain_declaration_draft_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 75 | `_repo_mirror/results/_cleanup_round_2026_10_08.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 76 | `_repo_mirror/results/_clearance_round_1_register_2026_10_08.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 77 | `_repo_mirror/results/_codex_c4_unblock_reply_adoption_register_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 78 | `_repo_mirror/results/_codex_c4_values_followup_reply_intake_register_2026_10_10.md` | pairs A/B/C/none=0/9/0/0 | unpaired=0 | agg=-24 |
| 79 | `_repo_mirror/results/_codex_c4_values_reply_intake_register_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 80 | `_repo_mirror/results/_codex_c4_values_unblock_reply_intake_register_2026_10_10.md` | pairs A/B/C/none=0/6/0/1 | unpaired=0 | agg=-17 |
| 81 | `_repo_mirror/results/_commission_closeout_erratum_and_supplement_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 82 | `_repo_mirror/results/_e2_glm2_distill_side_receipt_register_2026_10_09.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 83 | `_repo_mirror/results/_e4_lineage_conflict_correction_2026_10_11.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 84 | `_repo_mirror/results/_e6_j5_semantics_conflict_judgment_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 85 | `_repo_mirror/results/_e6_j5_semantics_erratum_note_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 86 | `_repo_mirror/results/_e6_n_distinct_judge_types_recompute_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 87 | `_repo_mirror/results/_e6_th_v3_19_residual_exits_judgment_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 88 | `_repo_mirror/results/_ea_audit_batch_vk_2026_10_09.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 89 | `_repo_mirror/results/_eps_ls_semantics_judgment_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 90 | `_repo_mirror/results/_executor_prereg_docstring_correction_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 91 | `_repo_mirror/results/_executor_prereg_vs_impl_equivalence_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 92 | `_repo_mirror/results/_exp05_negative_probe_rescan_2026_10_10.md` | pairs A/B/C/none=0/5/0/0 | unpaired=0 | agg=-10 |
| 93 | `_repo_mirror/results/_exp08_s4_prompt_face_register_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 94 | `_repo_mirror/results/_f3_definition_deep_judgment_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 95 | `_repo_mirror/results/_f3_new_definition_draft_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 96 | `_repo_mirror/results/_f3f4_exit_drafts_2026_10_11.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 97 | `_repo_mirror/results/_f4_direction1_domain_effectivity_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 98 | `_repo_mirror/results/_f4_direction1_prereq_check_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 99 | `_repo_mirror/results/_f4_direction1_seed_and_domain_draft_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 100 | `_repo_mirror/results/_five_items_effectivity_register_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 101 | `_repo_mirror/results/_five_pending_items_drafts_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 102 | `_repo_mirror/results/_five_stage_chain_design_reconstruction_2026_10_12.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 103 | `_repo_mirror/results/_forgotten_recovery_register_2026_09_29.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 104 | `_repo_mirror/results/_forgotten_recovery_register_2026_10_08.md` | pairs A/B/C/none=0/6/0/0 | unpaired=0 | agg=-12 |
| 105 | `_repo_mirror/results/_four_items_execution_batch_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 106 | `_repo_mirror/results/_fp3_anchor_and_krj_restrament_register_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 107 | `_repo_mirror/results/_ftfb_order_judgment_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 108 | `_repo_mirror/results/_ftfb_v3_pass2_audit_2026_09_18_corrected.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 109 | `_repo_mirror/results/_g11_krj4_effectivity_register_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 110 | `_repo_mirror/results/_g4_e3_definition_ruling_material_2026_10_09.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 111 | `_repo_mirror/results/_g4_reproduction_execution_register_2026_10_09.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 112 | `_repo_mirror/results/_g4_residual_probe_2026_10_08.md` | pairs A/B/C/none=0/5/0/0 | unpaired=0 | agg=-10 |
| 113 | `_repo_mirror/results/_g5_ccp_execution_prereqs_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 114 | `_repo_mirror/results/_g5_ccp_p0_verification_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 115 | `_repo_mirror/results/_g5_ccp_seed_designation_revision_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 116 | `_repo_mirror/results/_g5_krj9_denominator_reconciliation_judgment_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 117 | `_repo_mirror/results/_g5_rejudgment_c_applicability_recheck_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 118 | `_repo_mirror/results/_g5_rejudgment_construction_change_plan_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 119 | `_repo_mirror/results/_g5_rejudgment_construction_question_judgment_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 120 | `_repo_mirror/results/_g5_x4_dual_axis_interpretation_judgment_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 121 | `_repo_mirror/results/_g9_read_b_effectivity_register_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-4 |
| 122 | `_repo_mirror/results/_gate_one_declared_adoption_register_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 123 | `_repo_mirror/results/_gate_one_pi_endorsement_register_2026_10_12.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 124 | `_repo_mirror/results/_j2_identifier_coupling_judgment_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 125 | `_repo_mirror/results/_j2_kj4_disposition_register_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 126 | `_repo_mirror/results/_k_v3df_0_1_four_readings_2026_10_09.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 127 | `_repo_mirror/results/_k_v3df_0_1_readings_verdict_2026_10_09.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 128 | `_repo_mirror/results/_kd_doc1_correction_adoption_register_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 129 | `_repo_mirror/results/_kimi_safe_batch_push_v2_full_2026_09_17.json` | pairs A/B/C/none=0/79/0/0 | unpaired=0 | agg=-158 |
| 130 | `_repo_mirror/results/_kj1_abc_choice_judgment_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 131 | `_repo_mirror/results/_kj1_eps_ls_effectivity_register_2026_10_11.md` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-8 |
| 132 | `_repo_mirror/results/_kj1_judgment_premise_correction_2026_10_11.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 133 | `_repo_mirror/results/_kj1_sc1_premise_correction_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 134 | `_repo_mirror/results/_kj4_e4_unification_judgment_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 135 | `_repo_mirror/results/_krj_all_five_verdicts_rewrite_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 136 | `_repo_mirror/results/_krj_all_terminal_verdicts_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 137 | `_repo_mirror/results/_krj_cond4_effectivity_declaration_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 138 | `_repo_mirror/results/_krj_five_verdicts_adjudication_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 139 | `_repo_mirror/results/_krj_pi_picks_adoption_krj6_revise_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 140 | `_repo_mirror/results/_krj10_reverdict_after_r4_convergence_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 141 | `_repo_mirror/results/_krj10_terminal_verdict_closure_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 142 | `_repo_mirror/results/_krj4_trj1_adjudication_judgment_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 143 | `_repo_mirror/results/_krj4_trj1_pick_and_pass_verdict_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 144 | `_repo_mirror/results/_krj5_final_disposition_verdict_2026_10_11.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 145 | `_repo_mirror/results/_krj5_subject_scope_judgment_2026_10_11.md` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-8 |
| 146 | `_repo_mirror/results/_krj5d_third_tier_effectivity_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 147 | `_repo_mirror/results/_krj9_scope_clarification_draft_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 148 | `_repo_mirror/results/_letters_archive_register_2026_10_01.md` | pairs A/B/C/none=0/9/0/0 | unpaired=0 | agg=-18 |
| 149 | `_repo_mirror/results/_lim_aperiod_adoption_and_label_correction_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 150 | `_repo_mirror/results/_lim_aperiod_restatement_third_domain_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 151 | `_repo_mirror/results/_limb_reading_verdict_kv3s33_2026_10_01.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 152 | `_repo_mirror/results/_md_trigger_prereg_effectivity_2026_10_11.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 153 | `_repo_mirror/results/_misformed_commission_drafts_deletion_register_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 154 | `_repo_mirror/results/_overnight_delivery_index_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-6 |
| 155 | `_repo_mirror/results/_p_k_v3_glm_fpr_audit_report_2026-09-17T08-23-41Z.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 156 | `_repo_mirror/results/_p_refresh_registration_preliminary_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 157 | `_repo_mirror/results/_p_refresh_s0_judgment_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 158 | `_repo_mirror/results/_p_refresh_scope_judgment_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 159 | `_repo_mirror/results/_pc_d1_d3_2026_09_15.py` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 160 | `_repo_mirror/results/_pending_pi_items_drafts_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 161 | `_repo_mirror/results/_pending_rulings_drafts_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 162 | `_repo_mirror/results/_pending_supply_search_receipt_2026_10_08.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 163 | `_repo_mirror/results/_pi_card_123_adoption_and_gate_one_request_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 164 | `_repo_mirror/results/_pi_effectivity_declaration_register_2026_10_11.md` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-8 |
| 165 | `_repo_mirror/results/_plan_v3_pending_verify_2026_09_30.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 166 | `_repo_mirror/results/_pre_exec_report_kimi_2026_09_30.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 167 | `_repo_mirror/results/_pre_execution_report_kimi_2026_10_01.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 168 | `_repo_mirror/results/_q2_scope_vs_revision_judgment_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 169 | `_repo_mirror/results/_q3_c1c4_l282_transposition_fix_applied_note_2026_10_09.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 170 | `_repo_mirror/results/_q3_c1c4_l282_transposition_fix_executor_2026_10_09.py` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 171 | `_repo_mirror/results/_questionnaire_cards_intake_register_2026_10_09.md` | pairs A/B/C/none=0/6/0/1 | unpaired=0 | agg=-14 |
| 172 | `_repo_mirror/results/_questionnaire_cards_intake_register_supplement_10_2026_10_10.md` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-8 |
| 173 | `_repo_mirror/results/_questionnaire_cards_intake_register_supplement_11_2026_10_10.md` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-8 |
| 174 | `_repo_mirror/results/_questionnaire_cards_intake_register_supplement_12_2026_10_10.md` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-8 |
| 175 | `_repo_mirror/results/_questionnaire_cards_intake_register_supplement_13_2026_10_11.md` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-8 |
| 176 | `_repo_mirror/results/_questionnaire_cards_intake_register_supplement_14_2026_10_11.md` | pairs A/B/C/none=0/5/0/0 | unpaired=0 | agg=-10 |
| 177 | `_repo_mirror/results/_questionnaire_cards_intake_register_supplement_15_2026_10_11.md` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-8 |
| 178 | `_repo_mirror/results/_questionnaire_cards_intake_register_supplement_2_2026_10_10.md` | pairs A/B/C/none=0/1/0/1 | unpaired=0 | agg=-3 |
| 179 | `_repo_mirror/results/_questionnaire_cards_intake_register_supplement_2026_10_09.md` | pairs A/B/C/none=0/1/0/1 | unpaired=0 | agg=-3 |
| 180 | `_repo_mirror/results/_questionnaire_cards_intake_register_supplement_3_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 181 | `_repo_mirror/results/_questionnaire_cards_intake_register_supplement_5_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 182 | `_repo_mirror/results/_questionnaire_cards_intake_register_supplement_6_2026_10_10.md` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-8 |
| 183 | `_repo_mirror/results/_questionnaire_cards_intake_register_supplement_7_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 184 | `_repo_mirror/results/_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 185 | `_repo_mirror/results/_questionnaire_cards_intake_register_supplement_8_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 186 | `_repo_mirror/results/_questionnaire_cards_intake_register_supplement_9_2026_10_10.md` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-8 |
| 187 | `_repo_mirror/results/_r_pair_addendum_2026_10_09.json` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 188 | `_repo_mirror/results/_receipt_disposition_register_2026_10_08.md` | pairs A/B/C/none=0/8/0/0 | unpaired=0 | agg=-16 |
| 189 | `_repo_mirror/results/_register3_bytes_erratum_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 190 | `_repo_mirror/results/_repo_full_inventory_catalogue_2026_10_12.md` | pairs A/B/C/none=0/8/0/0 | unpaired=0 | agg=-18 |
| 191 | `_repo_mirror/results/_repo_post_cleanup_snapshot_2026_10_12.md` | pairs A/B/C/none=0/7/0/0 | unpaired=0 | agg=-14 |
| 192 | `_repo_mirror/results/_round53_rejudge_prereg_freeze_effectivity_register_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 193 | `_repo_mirror/results/_round53_th_v3_19_landfall_schema_effectivity_register_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 194 | `_repo_mirror/results/_round54_g5_dispositions_register_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 195 | `_repo_mirror/results/_round55_dispositions_register_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 196 | `_repo_mirror/results/_round56_ad8fix_effectivity_register_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 197 | `_repo_mirror/results/_round56_b01_followup_disposition_plan_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 198 | `_repo_mirror/results/_round56_direct_adoptions_register_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 199 | `_repo_mirror/results/_round56_g2_enable_and_v1_rule_register_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 200 | `_repo_mirror/results/_round56_gu_backdoor_exclusion_revision_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 201 | `_repo_mirror/results/_round56_idx_sc1_resolution_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 202 | `_repo_mirror/results/_round56_n10_erratum_register_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 203 | `_repo_mirror/results/_round56_pending_questions_compilation_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 204 | `_repo_mirror/results/_round56_pending_questions_compilation_supplement_note_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 205 | `_repo_mirror/results/_round56_registration_supplement_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 206 | `_repo_mirror/results/_round56_review_effectivity_register_2026_10_10.md` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-10 |
| 207 | `_repo_mirror/results/_round56_review_effectivity_register_3_2026_10_10.md` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-10 |
| 208 | `_repo_mirror/results/_round56_review_effectivity_register_4_2026_10_11.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 209 | `_repo_mirror/results/_round56_review_effectivity_register_5_2026_10_11.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 210 | `_repo_mirror/results/_round56_review_effectivity_register_6_2026_10_11.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 211 | `_repo_mirror/results/_round56_sc4_nstar_inconsistency_erratum_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 212 | `_repo_mirror/results/_round56_shortname_backfill_note_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 213 | `_repo_mirror/results/_round56_terminal_boundary_effectivity_register_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 214 | `_repo_mirror/results/_round56_th3_coverage_line_effectivity_register_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 215 | `_repo_mirror/results/_round56_th4_two_field_reporting_resolution_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 216 | `_repo_mirror/results/_round56_typeb_backfill_register_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 217 | `_repo_mirror/results/_round56_typeb_form_draft_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 218 | `_repo_mirror/results/_round56_typeb_implementation_register_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 219 | `_repo_mirror/results/_round56_v4_kd_row_correction_revision_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 220 | `_repo_mirror/results/_round56a_dispositions_register_2026_10_10.md` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-8 |
| 221 | `_repo_mirror/results/_round56c_card_id_erratum_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-8 |
| 222 | `_repo_mirror/results/_round56c_d23_ad5_judgment_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 223 | `_repo_mirror/results/_round56r8_dispositions_register_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 224 | `_repo_mirror/results/_round56r9r10_dispositions_register_2026_10_10.md` | pairs A/B/C/none=0/5/0/0 | unpaired=0 | agg=-10 |
| 225 | `_repo_mirror/results/_s1prime_trigger_caliber_reevaluation_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 226 | `_repo_mirror/results/_s2prime_krj3_applicability_recheck_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 227 | `_repo_mirror/results/_s3prime_alert_disposition_judgment_2026_10_11.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 228 | `_repo_mirror/results/_s3prime_degeneracy_selfcert_2026_10_11.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 229 | `_repo_mirror/results/_s3prime_recompute_after_supplement_2026_10_11.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 230 | `_repo_mirror/results/_s4_corpus_scope_hard_constraint_judgment_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 231 | `_repo_mirror/results/_s4_heldout_sampling_seed42_items_register_2026_10_09.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 232 | `_repo_mirror/results/_s4_heldout_sampling_seed42_register_2026_10_09.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 233 | `_repo_mirror/results/_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` | pairs A/B/C/none=0/1/0/4 | unpaired=1 | agg=-1 |
| 234 | `_repo_mirror/results/_s4_heldout_sampling_seedprime_items_register_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 235 | `_repo_mirror/results/_s4_heldout_sampling_seedthird_extractor_2026_10_11.py` | pairs A/B/C/none=0/1/0/10 | unpaired=1 | agg=-1 |
| 236 | `_repo_mirror/results/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 237 | `_repo_mirror/results/_s4_heldout_seedprime_verification_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 238 | `_repo_mirror/results/_s4_open_questions_addendum_2026_10_09.json` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 239 | `_repo_mirror/results/_s4_seedprime_inheldout_recompute_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 240 | `_repo_mirror/results/_s4_seedprime_seq_t1_only_supplement_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 241 | `_repo_mirror/results/_s4_source_wave_mapping_registration_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 242 | `_repo_mirror/results/_s4_substrate_topup_addendum_2026_10_09.json` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 243 | `_repo_mirror/results/_s4prime_five_lines_readings_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 244 | `_repo_mirror/results/_s5prime_double_lim_a_and_item_registers_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 245 | `_repo_mirror/results/_s5prime_lim_a_and_item_registers_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 246 | `_repo_mirror/results/_s6doubleprime_terminal_verdicts_2026_10_11.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 247 | `_repo_mirror/results/_s6doubleprime_verdict_supplement_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 248 | `_repo_mirror/results/_s6prime_terminal_verdicts_2026_10_11.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 249 | `_repo_mirror/results/_s7doubleprime_verification_2026_10_11.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 250 | `_repo_mirror/results/_s7doubleprime_verification_erratum_2026_10_11.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 251 | `_repo_mirror/results/_s7prime_findings_erratum_2026_10_11.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 252 | `_repo_mirror/results/_s7prime_prereq_and_verification_2026_10_11.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 253 | `_repo_mirror/results/_seed_double_criterion_draft_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 254 | `_repo_mirror/results/_seed_double_identifier_final_judgment_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 255 | `_repo_mirror/results/_seed_double_identifier_finalization_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 256 | `_repo_mirror/results/_seed_double_rule_judgment_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 257 | `_repo_mirror/results/_seven_gap_closures_adoption_register_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 258 | `_repo_mirror/results/_stage_sequence_violation_register_2026_10_12.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 259 | `_repo_mirror/results/_stage1_independent_gate_review_2026_10_12.md` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-8 |
| 260 | `_repo_mirror/results/_stage1_tail_caliber_unification_register_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 261 | `_repo_mirror/results/_stage2_trae_reply_acceptance_register_2026_10_12.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 262 | `_repo_mirror/results/_stage3_1_bulk_reorg_completion_register_2026_10_12.md` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-9 |
| 263 | `_repo_mirror/results/_stage3_extraction_verification_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 264 | `_repo_mirror/results/_stage3_open_and_mandate_register_2026_10_12.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 265 | `_repo_mirror/results/_stage3_readings_verification_2026_10_11.md` | pairs A/B/C/none=0/3/0/1 | unpaired=0 | agg=-7 |
| 266 | `_repo_mirror/results/_stage3_trigger_readings_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 267 | `_repo_mirror/results/_stage3_trigger_recheck_2026_10_11.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 268 | `_repo_mirror/results/_suspect17_release_move_register_2026_10_09.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-6 |
| 269 | `_repo_mirror/results/_t1_exp2_activation_supplement_2026_10_09.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 270 | `_repo_mirror/results/_t1_exp2_executor_2026_10_09.py` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 271 | `_repo_mirror/results/_t1_gate_closure_and_recompute_verdict_2026_10_01.md` | pairs A/B/C/none=0/1/0/11 | unpaired=0 | agg=-2 |
| 272 | `_repo_mirror/results/_three_pending_items_drafts_2026_10_11.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 273 | `_repo_mirror/results/_three_pending_items_effectivity_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 274 | `_repo_mirror/results/_thv3_15_parallel_seed_double_note_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 275 | `_repo_mirror/results/_trigger_denominator_caliber_judgment_2026_10_11.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 276 | `_repo_mirror/results/_trj_w1_downstream_erratum_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 277 | `_repo_mirror/results/_trj_w1_verification_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 278 | `_repo_mirror/results/_typeb_m_caliber_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 279 | `_repo_mirror/results/_typeb_m_definition_judgment_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 280 | `_repo_mirror/results/_typeb_m_registration_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 281 | `_repo_mirror/results/_u_cf_category_caliber_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 282 | `_repo_mirror/results/_u_cf_reclassification_2026_10_10.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 283 | `_repo_mirror/results/_u_closure_execution_register_2026_10_09.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-6 |
| 284 | `_repo_mirror/results/_u04_1_exemption_precondition_verification_2026_10_09.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 285 | `_repo_mirror/results/_u3_carrier_qid_verification_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 286 | `_repo_mirror/results/_u5b_p_counting_resolution_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 287 | `_repo_mirror/results/_u6_negative_delta_compatibility_2026_10_11.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 288 | `_repo_mirror/results/_upload_guard_mirror_pair_2026_10_08.md` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-10 |
| 289 | `_repo_mirror/results/_v3_recheck_08c_preexp_data/rescript_2026_09_27.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 290 | `_repo_mirror/results/_v3_recheck_21_result_2026_09_27.json` | pairs A/B/C/none=0/7/0/0 | unpaired=0 | agg=-14 |
| 291 | `_repo_mirror/results/_v3_recheck_prereg_v1p1_2026_09_27.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-8 |
| 292 | `_repo_mirror/results/_v3_s_phrasetemplate_preexp_data/rescript_2026_09_27.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 293 | `_repo_mirror/results/_v3_v4_achievements_inventory_2026_09_24.md` | pairs A/B/C/none=0/0/0/3 | unpaired=0 | agg=-3 |
| 294 | `_repo_mirror/results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | pairs A/B/C/none=0/0/0/6 | unpaired=0 | agg=-12 |
| 295 | `_repo_mirror/results/_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md` | pairs A/B/C/none=0/6/0/0 | unpaired=0 | agg=-12 |
| 296 | `_repo_mirror/results/_v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-8 |
| 297 | `_repo_mirror/results/_v4_closeout_account_reconciliation_2026_10_12.md` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-8 |
| 298 | `_repo_mirror/results/_v4_closeout_bulk_reorganize_register_2026_10_12.md` | pairs n/a (blob-diff) | n/a | -1644 |
| 299 | `_repo_mirror/results/_v4_closeout_moves_and_cleanup_register_2026_10_12.md` | pairs A/B/C/none=0/3/0/1 | unpaired=0 | agg=-7 |
| 300 | `_repo_mirror/results/_v4_design_integration_2026_09_21_v1.1.md` | pairs A/B/C/none=0/5/0/0 | unpaired=0 | agg=-14 |
| 301 | `_repo_mirror/results/_v4_gA1_terminology_draft_2026_09_22.md` | pairs A/B/C/none=0/3/0/0 | unpaired=0 | agg=-8 |
| 302 | `_repo_mirror/results/_v4_group_b_explore_subs_integration_2026_09_22.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 303 | `_repo_mirror/results/_v4_maindir_cleanup_manifest_2026_09_24.md` | pairs A/B/C/none=0/6/0/0 | unpaired=0 | agg=-12 |
| 304 | `_repo_mirror/results/_v4_maindir_cleanup_manifest_v2_2026_09_26.md` | pairs A/B/C/none=0/6/0/0 | unpaired=0 | agg=-12 |
| 305 | `_repo_mirror/results/_v4_maindir_cleanup_moves_ledger_v3_2026_09_24.md` | pairs A/B/C/none=0/9/0/0 | unpaired=0 | agg=-24 |
| 306 | `_repo_mirror/results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` | pairs A/B/C/none=0/6/0/0 | unpaired=0 | agg=-12 |
| 307 | `_repo_mirror/results/_v4_maindir_count_monitor_2026_09_27.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 308 | `_repo_mirror/results/_v4_trae_remaining_audit_2026_09_28.md` | pairs A/B/C/none=0/4/0/0 | unpaired=0 | agg=-8 |
| 309 | `_repo_mirror/results/_v5_b12_verify_pack_q1_q3_q4_2026_09_29.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 310 | `_repo_mirror/results/_v5_confirm_b8_decisions_register_2026_09_29.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 311 | `_repo_mirror/results/_v5_paper_remedy_r1_pledge_2026_09_29.md` | pairs A/B/C/none=0/6/0/0 | unpaired=0 | agg=-14 |
| 312 | `_repo_mirror/results/_v5_paper_remedy_r2_r4_sourcetrace_2026_09_29.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-6 |
| 313 | `_repo_mirror/results/_v5_r4_residual_merged_catalogue_2026_09_29.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-13 |
| 314 | `_repo_mirror/results/_v5_sub_artifact_ledger_history_r1_2026_09_29.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 315 | `_repo_mirror/results/_v5_sub_artifact_ledger_history_r3_2026_09_29.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 316 | `_repo_mirror/results/_v5_sub_artifact_ledger_history_r4_2026_09_29.md` | pairs A/B/C/none=0/16/0/1 | unpaired=0 | agg=-37 |
| 317 | `_repo_mirror/results/_v5_t1_decisions_register_2026_09_29.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 318 | `_repo_mirror/results/_vk_current_counting_face_2026_10_10.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 319 | `_repo_mirror/results/_vk_face_category_erratum_2026_10_11.md` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 320 | `_repo_mirror/results/_zero_reading_judgment_2026_10_10.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 321 | `_repo_mirror/results/deposon_pf_d1_full_9m5c_2026_09_15.json` | pairs A/B/C/none=0/8/0/0 | unpaired=0 | agg=-16 |
| 322 | `_repo_mirror/results/deposon_pf_implementation_2026_09_11.json` | pairs A/B/C/none=0/5/0/0 | unpaired=0 | agg=-10 |
| 323 | `_repo_mirror/results/deposon_v3_v7_summary_2026_09_11.json` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 324 | `_repo_mirror/tmp_movedout_2026_09_28/_cleanup_classify_2026_09_28.py` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 325 | `_repo_mirror/tmp_movedout_2026_09_28/_cleanup_classify_out_2026_09_28.txt` | pairs A/B/C/none=0/135/0/0 | unpaired=0 | agg=-270 |
| 326 | `_repo_mirror/tmp_movedout_2026_09_28/_cleanup_probe_2026_09_28.py` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 327 | `_repo_mirror/tmp_movedout_2026_09_28/_cleanup_probe_out_2026_09_28.txt` | pairs n/a (blob-diff) | n/a | -1 |
| 328 | `_repo_mirror/tmp_movedout_2026_09_28/_cleanup_resolve_2026_09_28.py` | pairs A/B/C/none=0/2/0/0 | unpaired=0 | agg=-4 |
| 329 | `_repo_mirror/tmp_movedout_2026_09_28/_cleanup_transfer_scan_2026_09_28.py` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-2 |
| 330 | `_repo_mirror/tmp_movedout_2026_10_09/uncertain_release_2026_09/_asset_recount_2026_09_30.md` | pairs A/B/C/none=0/6/0/0 | unpaired=0 | agg=-16 |
| 331 | `_repo_mirror/tmp_movedout_2026_10_09/uncertain_release_2026_09/_letter_review_bob_w3_commission_2026_09_30.md` | pairs A/B/C/none=0/6/0/0 | unpaired=0 | agg=-14 |
| 332 | `_repo_mirror/tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b14_r3_anchor_retrieval_2026_09_29.md` | pairs A/B/C/none=0/9/0/3 | unpaired=0 | agg=-25 |
| 333 | `_repo_mirror/tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b17_three_caliber_fixation_2026_09_29.md` | pairs A/B/C/none=0/1/0/0 | unpaired=0 | agg=-8 |
| 334 | `_repo_mirror/tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_glm_charlie_reread_ac74a04efeb2_2026_09_29.md` | pairs A/B/C/none=0/6/0/0 | unpaired=0 | agg=-12 |
| 335 | `_repo_mirror/volcengine_glm_latest_30cells_v2_runner_2026_09_10.py` | pairs A/B/C/none=0/7/0/0 | unpaired=0 | agg=-14 |

### §4-1 两件 `blob-diff` 件之逐项证据（git blob SHA 全 IDENTITY=MATCH）
| 件 | parent blob（字节） | 本 commit blob（字节） | 强占位符 前→后 | 真实字面 前→后 | 唯一变动行 |
| :-- | :-- | :-- | :-- | :-- | --: |
| `_repo_mirror/results/_v4_closeout_bulk_reorganize_register_2026_10_12.md` | `87a2ff256873e42d832ce32a4ef5427c0a192318`（184,936 B） | `2b36d3874b4d84ed7b05918e2ede0d50de9c7b60`（197,287 B） | **1,649 → 2** | **0 → 1,646** | **911** |
| `_repo_mirror/tmp_movedout_2026_09_28/_cleanup_probe_out_2026_09_28.txt` | `c4c89193db5212d7cdd7a2843a2b5d37f241bda9`（12,359 B） | `75429a79bae4d1f5f0ba95e2109142a8a4f22265`（12,367 B） | **2 → 1** | **0 → 1** | **1** |

大件之抽样逐行证据（parent 侧 → 本 commit 侧）：
- `| 23 | `+"`_september_workspace/.tmp/_e3536.txt`"+` | … |` → `| 672 | `+"`〔幽灵引用·原件已缺席·未上传:�〕��`"+` | … |`
- `| 124 | `+"`_september_workspace/results/_d1_backfill_conflict_trace_2026_10_01.md`"+` |` → `| 3 | `+"`〔幽灵引用·原件已缺席·未上传:deposon_3risk_v0_fixes_2026_09_11.json〕`"+` |`
- 小件：`- MISS: path:    _september_workspace/results/_v4_pi_cot_v3_result_v3.json` → `+ MISS: path:    _repo_mirror/readout/final/_v4_pi_cot_v3_result_v3.json`

⇒ 该二件**同向**，计入 B 类。

# §5 C 类（混杂）逐件清单与配对证据 —— 2 件

### §5-1 `_repo_mirror/_movedout_manifest_2026_09_21.json`（配对 A=10 ／ B=2 ／ C=2）
| # | 删除行（parent） | 新增行（本 commit） | 判定 |
| --: | :-- | :-- | :-- |
| 0,1,2,3 | `…_coze_online_v3_d7format_2026_09_18.pdf` ／ `…_letter_to_coze_online_v2_2026_09_18.md`（src ＋ dst） | `…_coze_〔IM〕_v3_d7format…` ／ `…_letter_to_coze_〔IM〕_v2…` | A |
| 4,5 | `LETTER_TO_EXTERNAL_ADVISOR_2026_09_18_FINAL.md`（src ＋ dst） | `LETTER_TO_WANG_TEACHER_2026_09_18_FINAL.md` | **B** |
| 6–11 | `…_coze_online_v3…`（src ＋ dst） | `…_coze_〔IM〕_v3…` | A |
| 12,13 | `_d7_external_advisor_online_publish_v1_20260918.md`（src ＋ dst） | `_d7_wang_teacher_〔IM〕_publish_v1_20260918.md` | **C（同一行兼 A＋B）** |

⇒ **同件内正脱敏（10 对）与反脱敏（2 对）并存**：文件名之 IM 平台指示词被占位化（正确），而**受托方代号被替换为真实姓名代号 `WANG_TEACHER`（错误）**。

### §5-2 `_repo_mirror/results/_questionnaire_cards_intake_register_supplement_4_2026_10_10.md`（配对 A=2 ／ B=1）
- B 对：`- **来源**：运行时库 `+"`〔本机用户目录〕/.minimax/v2/sqlite/runtime-state.sqlite`"+` …` → `+ … `+"`〔本地绝对路径·脱敏略:runtime-state.sqlite〕`"+` …`
- A 对 ×2：该件登记行内 `〔…〕` 占位符之保持/新增（新增占位符、0 新增字面）

⇒ 归 C（混杂）。

# §6 A 类（正脱敏）逐件清单 —— 13 件

| # | 仓内相对路径 | 配对 A/B/C/中性 | 方向摘要 |
| --: | :-- | :-- | :-- |
| 1 | `_repo_mirror/results/_archive_2026_09_20/_audit_secret_2026_09_20_anchor_guard.py` | pairs A/B/C/none=4/0/0/0 | 平台指示词／泛称 → 强占位符 `〔IM〕`／`〔W老师〕` |
| 2 | `_repo_mirror/results/_archive_2026_09_20/_coze_paper_v1_双审报告_2026_09_17.md` | pairs A/B/C/none=6/0/0/0 | 平台指示词／泛称 → 强占位符 `〔IM〕`／`〔W老师〕` |
| 3 | `_repo_mirror/results/_archive_2026_09_20/_ftfb_pass2_results_limitations_audit_2026_09_17.md` | pairs A/B/C/none=1/0/0/0 | 平台指示词／泛称 → 强占位符 `〔IM〕`／`〔W老师〕` |
| 4 | `_repo_mirror/results/_archive_2026_09_20/_letter_to_coze_paper_v1_委托_2026_09_17.md` | pairs A/B/C/none=14/0/0/0 | 平台指示词／泛称 → 强占位符 `〔IM〕`／`〔W老师〕` |
| 5 | `_repo_mirror/results/_archive_2026_09_20/_letter_to_kimi_push_v3_final_2026_09_17.md` | pairs A/B/C/none=2/0/0/0 | 平台指示词／泛称 → 强占位符 `〔IM〕`／`〔W老师〕` |
| 6 | `_repo_mirror/results/_archive_2026_09_20/_letter_to_kimi_push_v3_final_v2_2026_09_17.md` | pairs A/B/C/none=2/0/0/0 | 平台指示词／泛称 → 强占位符 `〔IM〕`／`〔W老师〕` |
| 7 | `_repo_mirror/results/_archive_2026_09_20/_letter_to_kimi_push_v3_委托_2026_09_17.md` | pairs A/B/C/none=3/0/0/0 | 平台指示词／泛称 → 强占位符 `〔IM〕`／`〔W老师〕` |
| 8 | `_repo_mirror/results/_archive_2026_09_20/_letter_to_kimi_upload_requirements_2026_09_18.md` | pairs A/B/C/none=6/0/0/0 | 平台指示词／泛称 → 强占位符 `〔IM〕`／`〔W老师〕` |
| 9 | `_repo_mirror/results/_archive_2026_09_20/_letter_to_trae_code_2026_09_17_final.md` | pairs A/B/C/none=8/0/0/0 | 平台指示词／泛称 → 强占位符 `〔IM〕`／`〔W老师〕` |
| 10 | `_repo_mirror/results/_archive_2026_09_20/ftfb_pass1_background_methodology_audit_2026_09_17.md` | pairs A/B/C/none=1/0/0/0 | 平台指示词／泛称 → 强占位符 `〔IM〕`／`〔W老师〕` |
| 11 | `_repo_mirror/results/_archive_2026_09_20/LETTER_TO_KIMI_GITHUB_UPLOAD_2026_09_18.md` | pairs A/B/C/none=4/0/0/0 | 平台指示词／泛称 → 强占位符 `〔IM〕`／`〔W老师〕` |
| 12 | `_repo_mirror/results/_archive_2026_09_20/LETTER_TO_TRAE_2026_09_11.md` | pairs A/B/C/none=16/0/0/0 | 平台指示词／泛称 → 强占位符 `〔IM〕`／`〔W老师〕` |
| 13 | `_repo_mirror/results/_archive_2026_09_20/LETTER_TO_TRAE_REVIEW_2026_09_16.md` | pairs A/B/C/none=2/0/0/0 | 平台指示词／泛称 → 强占位符 `〔IM〕`／`〔W老师〕` |

⚠️ **诚实标注**：A 类之中，`〔W老师〕` 虽为方括号占位符，**其内含可识别人名**（姓氏＋称谓）⇒ 属**弱脱敏**（自「泛称」变为「具名占位」）。全 commit 此类占位符 **新增 65 ／ 删除 10 ／ 净 +55**。

> A 类之全量方向均为：`coze_online`／`线上` → `〔IM〕`（正脱敏）；`外部顾问` → `〔W老师〕`（弱脱敏，见上）。

# §7 D 类（与脱敏无关）—— 4 件及其实际改动性质

| # | 仓内相对路径 | 改动 | 实际性质（逐字核读） |
| --: | :-- | :-- | :-- |
| 1 | `_repo_mirror/results/_d1_backfill_intake_verdict_2026_10_01.md` | +7/−7 | **纯指纹改写**：所引件之 SHA-12 由 `66f900b7598b` 全量替换为 `dc9cb0e02922`（连带字节数 28,352 → 28,370） |
| 2 | `_repo_mirror/results/_mini_round_5_decisions_register_2026_10_01.md` | +6/−6 | 同上（同一指纹改写之第二处登记） |
| 3 | `_repo_mirror/results/_v3_recheck_05_result_2026_09_28.json` | +5/−5 | **非脱敏之数据改**：4 处 `path` 增仓目录前缀（`results/…` → `deposon-repo/results/…`、`deposon-sub/results/…`）＋ **1 处布尔值翻转** `"exists": false` → `true` |
| 4 | `_repo_mirror/results/_root_session_history_memo_2026_10_14.md` | **+326/−0** | **纯追加**（子棒版备忘录 §7 补录）：新增行中强占位符 0、弱占位符 0、真实字面 **0**；所含 36 处 `「」` 为**中文引号**（非占位符，先前误判之源已修正，见 §12-1） |

⚠️ **登记（不作判定）**：第 3 件之 `"exists": false → true` 系**事实性断言之翻转**，发生于一件自称「desensitized」的 commit 之内；本审计**只登记不改判**，其正确性属他棒（verifier／worker）之面。

# §8 敏感字面类别计数（全 commit 新增行面）

| 类别 | 令牌 | 删除 | 新增 | **净增** |
| :-- | :-- | --: | --: | --: |
| 本机路径·工作区根 | `本地仓根…` | 2 | **937** | **+935** |
| 本机路径·用户目录 | `〔本地绝对路径·脱敏略:Administrator�〕��` | 0 | **177** | **+177** |
| 本机路径·另一盘用户目录 | `〔本地绝对路径·脱敏略:Administrator�〕��` | 0 | **2** | **+2** |
| 人名·真实姓名代号 | `WANG_TEACHER`／`wang_teacher` | 8 | **12** | **+4** |
| 人名·具名占位符 | `〔W老师〕`／`〔〔W老师〕〕`／`〔W老师〕` | 10 | 65 | **+55**（弱脱敏，另计） |
| **真实字面合计** | | **10** | **1,126** | **+1,116** |
| 占位符·仓根 | `_september_workspace` | **533** | 3 | **−530** |
| 占位符·方括号 | `〔…〕` | **644** | 152 | **−492** |
| 占位符·受托方代号 | `EXTERNAL_ADVISOR` | **4** | 0 | **−4** |
| **占位符合计** | | **1,301**（含弱占位） | **155** | **−1,146** |

**方向净值**：占位符净减 **1,146** 处、真实字面净增 **1,116** 处 ⇒ **脱敏面被净撤销**。

**凭据面（R4）**：全 commit 新增行经 `sk-`／`tp-`／`ark-`／`Authorization: Bearer`／`API_KEY=`／手机号／邮箱 七类形态扫描 ＝ **0 命中** ⇒ 本 commit **未**引入任何凭据字面。

# §9 现 HEAD 抽核（B 类代表件是否仍载字面）

| 仓内相对路径 | HEAD blob SHA（API 返值） | 本机复算 git blob SHA | 同一性 | 内容 SHA-12 | 敏感字面实测 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `_repo_mirror/.trae/scripts/_arxiv_renumber.py` | `941186a880ebf97ab0924820b38bc930741ed241` | `941186a880ebf97ab0924820b38bc930741ed241` | **MATCH** | `F488AD141EF9` | `本地仓根` ×**1** |
| `_repo_mirror/deposon_team/plugins/_pg_v01_compute.py` | `c70f833f9014066e6f36fd64e2ffd3b14b69a050` | `c70f833f9014066e6f36fd64e2ffd3b14b69a050` | **MATCH** | `08381F5F892B` | `本地仓根` ×**1** |
| `_repo_mirror/README_V4_2026_09_29.md` | `714dc17f8f5c64dec2ac221a044c68e02c97695f` | `714dc17f8f5c64dec2ac221a044c68e02c97695f` | **MATCH** | `65B34C52A085` | `本地仓根` ×1、`〔本地绝对路径·脱敏略:Administrator〕` ×2、`〔本地绝对路径·脱敏略:Administrator〕` ×1 |
| `_repo_mirror/results/_three_pending_items_drafts_2026_10_11.md` | `41c763713c1a6b88d6dd914f0ebca3c54a50eba9` | `41c763713c1a6b88d6dd914f0ebca3c54a50eba9` | **MATCH** | `8995859E5A76` | `本地仓根` ×**3** |

**要点**：
1. 四件之 git blob SHA 与被审 commit `739a7daf…` 的 `files[].sha` **逐位一致** ⇒ 该 commit 之后至 HEAD（晚 9 分半）**未**再被清理。
2. 身份校验方式：以本机所取字节复算 `sha1("blob " + len + NUL + bytes)`，与 contents API 返值比对 ⇒ **4/4 MATCH**（非仅凭 URL 断言）。
3. 交叉佐证：`_three_pending_items_drafts_2026_10_11.md` 之内容 SHA-12 ＝ `8995859E5A76`，与仓内他件正文所载该草案件之指纹**逐位相符** ⇒ 本审计之 SHA-12 口径与仓内既有口径一致。

# §10 与 commit message「509 desensitized」之对账

**结论：不相符 —— 且「509」无法由本 commit 之任何可测口径复现。**

| 可测口径 | 实测值 | 与 509 之关系 |
| :-- | --: | :-- |
| 涉及文件数 | **354** | ≠ 509 |
| 新增行／删除行 | 2,456 ／ 2,128 | ≠ 509 |
| 真实字面引入处数 | **1,126** | ≠ 509 |
| 占位符移除处数 | **1,301** | ≠ 509 |
| 反向配对数 | **1,068** | ≠ 509 |
| 正向配对数 | **81** | ≠ 509 |
| B 类件数 | **335** | ≠ 509 |

补充：parent commit `9ec782b2…`（早 10 秒、56 件）之 message 亦**不含**「509」，远端证据面**0** 处可解释该数字之来源 ⇒ 如实登记为**来源不可考**（⛔ 0 推测其含义、0 编造工作单来源）。

**名义与实测之相抵**：message 称 `desensitized`（已脱敏），而实测 **94.6% 之文件为脱敏撤销**，**净结果＝向公开仓引入 1,116 处敏感字面**。二者**直接相抵**，且相抵面为**后者**。

# §11 本件之自证

### §11-1 key 形态自扫（落盘后实测）
对本件全文扫描 `sk-*`／`tp-*`／`ark-*`／`Authorization: Bearer`／`API_KEY=`／手机号／邮箱 七类形态 ⇒ **0 命中**（详见回执）。

### §11-2 字节级自报（落盘后本人实测）
| 项 | 值 |
| :-- | :-- |
| SHA-256(全文字节) 前 12 位 | **（见回执；⛔ 0 内嵌自身指纹）** |
| 字节数 | **（见回执）** |
| BOM | **0** |
| CR（CRLF） | **0**（纯 LF） |
| U+FFFD 替换字符 | **0** |

### §11-3 既有件触动
本棒写入动作 ＝ **仅本件 1 件新名新建**；⛔ 0 编辑／0 覆写／0 追加／0 改名／0 移动／0 删除任何既有件 ⇒ **既有件触动数 ＝ 0**。
临时面（commit JSON 缓存、判定脚本、HEAD/blob 副本）落于系统临时目录 `%TEMP%\deposon_audit_739a7d\`，**⛔ 0 落于工作区**、⛔ 0 落于归档区、⛔ 0 落于 `〔本地他区引用·未上传:GLM〕`。

# §12 仪器缺陷登记（本审计测量仪器自身之误差源 · 6 处 · 均已修正并复算）

> 依「测量仪器自身即误差源」：审计工具先审自己 —— 下列缺陷**均为本审计自产之判定器**，修正后**全量重跑**，正文所有数字均出自修正后之运行。

| # | 缺陷 | 现象 | 修正 | 对结论之影响 |
| --: | :-- | :-- | :-- | :-- |
| 1 | 函数名 `CP` 撞内建 alias `cp`（Copy-Item） | 脚本报「找不到路径」 | 改名 `ToStr` | 无（未产数据） |
| 2 | `New-Object X(arg)` 缺空格 | 解析错 | 改先赋变量再构造 | 无（未产数据） |
| 3 | **PS 变量大小写不敏感**：`foreach ($t in $T)` 使 token 表 `$T` 被循环变量覆写 | 自第 2 件起遍历的是单个元素，模式变空串 ⇒ 全文匹配 19.9 万次；**伪得 B=285** | 变量改名 + 表结构断言（元素数 ＝ 3、模式非空） | **有**：首轮 B=285 系伪计数，已作废 |
| 4 | 明细串中 `$delta:A` 被解析为**作用域限定变量** | A 类明细数字与字母丢失 | 改 `$($delta):A` | 无（仅显示层；计数走独立变量） |
| 5 | **括号码位取错**：`〔〕` 误取 U+300C/300D（`「」`） | 强占位符对真实数据 **0 命中**；探针样本与仪器同错 ⇒ 自洽而失真 | 改 U+3014/U+3015 | **有**：曾致 A 类漏判、A 配对 ＝ 0；修正后 A ＝ 13、C ＝ 2 |
| 6 | `[regex]::Escape` 将 `〔(王|W)老师〕` 内嵌 alternation 一并转义 | 人名面计数误为 0 | 改为 `(?:王\|W)` 手工组装 | **有**：修正后人名占位净 **+55** |

**诚实自陈**：缺陷 3 与 5 均曾产出**方向性错误**的中间结果（B=285／A ＝ 0）。二者均由「对拍真实数据」而非「信任仪器」而被发现。若仅采首轮输出，本审计将给出**实质错误**之结论。

# §13 诚实限制（failures & limitations · 0 掩饰）

1. **覆盖**：354/354 件 100% 有方向判定（法一 352 ＋ 法二 2）。**0 件**无判。
2. **配对假设**：法一以「同序删除行 ↔ 同序新增行」配对。此假设在**纯 1:1 行替换**之 patch 上成立（本 commit 352 件中绝大多数如此，`additions` 与 `deletions` 相等）；若某件存在增删不等之插入/删除，**该件之内中性对可能被误配**。**中性对不参与方向归类**，故此类误配**不会**凭空造出 A 或 B，但**理论上可能掩盖**一处的真实方向。
3. **令牌集边界**：方向判定之完备性**取决于令牌集**。本审计覆盖 `〔…〕`／`_september_workspace`／`EXTERNAL_ADVISOR`／`外部顾问`／`online`／`线上`／本机路径／`WANG_TEACHER`／`〔W老师〕`。**若存在本审计未列入之敏感令牌，其替换方向 0 被计入** —— 惟 §8 之 catch-all 面（绝对路径／Administrator／IP／邮箱／手机号／凭据七形态）于全 commit 新增行**仅**回得绝对路径与 Administrator 二类，且二者均已计入 B 类，故**未覆盖之敏感字面之风险低**，但**不为 0**。
4. **HEAD 抽核为抽样**（4 件 ／ 335 件 B 类 ＝ 1.2%），非全量。抽样之 4 件**全部**仍载字面且 blob SHA 未变。
5. **只读**：本审计⛔ 未修改远端任何内容 ⇒ 公开仓现状未被本审计改变；反脱敏事实**仍然成立且持续**。
6. **不涉判定**：本件⛔ 不对「该 commit 是否合规」「是否应回滚」「PI 之裁」作任何判定 —— 此属 verifier／PI 之面。
7. **`D:` 与 `C:` 盘符字面**系 PI 本机结构，属**已发生之暴露事实**；本审计仅**记录与计数**，⛔ 0 代拟处置方案。

---

**（本件止）**
