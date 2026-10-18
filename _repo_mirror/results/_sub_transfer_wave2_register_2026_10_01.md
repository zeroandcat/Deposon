# sub 方向转移 · 第二波执行登记件（2026-10-01 · 「需裁」清单重估）

- **棒别**：sub 方向转移第二波执行棒（**worker**）· parent 派工（2026-10-01 晚）
- **出证方**：**worker**（本棒实际执行者）。⛔ 0 冒充 PI / doc-writer / verdict-keeper / verifier / Mavis 团队 / Trae code / KIMI / GLM / coze 等任一他棒或受托方。
- **本件性质**：**执行登记件 ＋ 重估表**（非预登记件、非判定件、非实验结果件）。
- **件名**：`results/_sub_transfer_wave2_register_2026_10_01.md`（**新名 · 无 `_vN_` 阶段前缀**）
- **版式**：UTF-8 无 BOM · LF
- **纪律**：0 编造｜0 代裁｜R4（**0 读 key／0 读 `.env`／0 落盘凭据**）｜SHA-12 一律 `sha256[:12]` **小写**
- **落盘前撞名实测**：`Test-Path results\_sub_transfer_wave2_register_2026_10_01.md` ⇒ **False**；全仓递归同名 **0 命中**；`results/*sub_transfer*` 近名 2 件（`_sub_transfer_candidates_`／`_sub_transfer_execution_register_`，**0 同名**）⇒ **0 覆写**
- **产出**：**1 件即停**（本件为唯一新增件）

---

## §0 PI 语境照录（L1 · parent 转录）

> PI 2026-10-01 晚逐字：「**还能移吗？注意 sub 和 repo 在 kimi 上传时是等价的，合为同一分区——也因此能移入那么多非核心文件——且要避免撞名**。」

**语义更新（本棒据此执行）**：

| 项 | 更新后口径 |
|---|---|
| **分区等价** | `sub` ≡ `repo`，kimi 上传时**合为同一分区** ⇒ 转移＝**纯组织性／可逆／不损上传范围** |
| **引用面判据** | 枚举面（`baseline_pre/post`・WT2 TSV・上传台账）**不计**权威引用面（PI 甲・不计，沿用）；只算【repo（除 `.tmp`／`__pycache__`）＋ sub】之**实体点名** |
| **新约束** | **合并分区撞名核**：移前须核 ① 目标路径 0 存在 ② repo＋sub 合并面**不新造同名冲突** |
| **四硬杠（不变）** | ① 冻结勘误链按名点名 ② PI 上传口径外发信按名点名 ③ 取证链证据引用 ④ R4 敏感 ⇒ **仍不可移·留候** |
| **低风险判据** | 实质引用面 **0**，或**仅自引用／已迁件互引** ⇒ 执行移动；**存疑者保持留候**并在本件列明 |

---

## §1 逐项重估表（「需裁」17 件 ＋ 2 目录）

**权威面**＝ **1,956 件**（repo ＋ sub，排除 `.tmp`／`__pycache__`）。**重估结果：移 1 件 ／ 留候 16 件 ＋ 2 目录（6 件）。**

### §1.1 执行移动（低风险 · 1 件）

| # | 路径 | SHA-12／字节 | 实质引用 | 移前依据 | 落位 |
|---:|---|---|---:|---|---|
| 1 | `deposon_team/plugins/_v4_wide_s2_scan_2026_09_27.py` | `c2cc22b27047`／4,000 | **0** | 仅 2 处点名：① `sub:…/v4_wide_2026_09_27/_v4_wide_s3_keyscan_2026_09_27.py` ＝ **第一波已迁件互引**；② `results/_sub_transfer_execution_register_2026_10_01.md` ＝ **本团队自产件**（第一波登记件 §5 连带提示）。**0 他方实体引用** ⇒ 合「仅自引用／已迁件互引」 | `sub/tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/` |

> ⭐ **附带效益**：`s2_scan` 与其被引之 `s3_keyscan` 现**同落一个 sub 子目录**，第一波登记件 §5 所记「悬空引用」**自然消解**（0 回改任何件）。

### §1.2 留候（16 件）

| # | 路径 | SHA-12／字节 | 实体引用数 | 留候依据（点名引用方） |
|---:|---|---|---:|---|
| 2 | `results/_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py` | `215db16a0556`／92,915 | 6 | `_v4_exec_surface_switch_2026_09_28.md`（**PI 拍板切换登记**）、`_v4_checkpoint_atomic_and_pycache_2026_09_28.md`、`letters/TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md`、`_skill_*_2026_09_30` ×2 |
| 3 | `results/_v4_supp_t15_executor_r2_atomic_2026_09_28.py` | `9e89e021ea03`／70,056 | 10 | 同上 ＋ `_v5_checkpoint_tail3_revision_2026_09_29.md`（**取证链**）、`_v4_supp_t15{,r2}_executor_r0_atomic_2026_09_29.py` ×2 |
| 4 | `results/_v3_recheck_26b_executor_r2_2026_09_28.py` | `0808af6212c5`／52,272 | **16** | 今日件 `_v3_recheck_26b_verdict{,_prep}_2026_10_01.md`、后继 `_v3_recheck_26b_executor_r3_2026_09_29.py` ＋ r3 结果、3 件 V5 登记、`_cleanup_round2`／`_wrapup_cleanup` 体例源 |
| 5 | `results/_v4_gamma_r1_prereg_2026_09_28.md` | `c9da8678cf2b`／33,489 | 15 | `letters/_v5_rj5_external_rederive_request{,_EN}_2026_09_28.md`（**两封外发委托函**）、`_v5_sub_artifact_ledger{,_history_r5}`（**取证链**）、`_v4_gamma_r1_exec`、`_v4_rj5_rederive_2026_09_28.md` |
| 6 | `results/_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md` | `c64146c4ccac`／23,152 | **25** | **5 代 dualtrack 线索册**（v0.1–v0.5，**今日件**）、12 件 `_v4_commission_*` 委托线、v2／v2p1 后继、`_v5_sub_artifact_ledger_history_r2`（取证链） |
| 7 | `results/_skill_reference_update_and_user_surface_survey_2026_09_30.md` | `cb7b7ec9ebcd`／60,621 | **46** | `_fake_verdict_reverify_sixitem_ledger_2026_09_30.md`（**取证链**）、`_sub_artifact_ledger_history_r5`、`_external_letters_two_generation_values_note_2026_10_01.md`、7 件 V4 邀请/主题函、13 件 skill 面登记 |
| 8 | `deposon_team/plugins/_v4_wide_s1_inventory_2026_09_27.py` | `145ae518f5f0`／1,669 | 1 | `letters/_v4_wide_walkthrough_reply_trae_code_2026_09_27.md`（**对外回函实体引用**，非枚举面） |
| 9 | `deposon_team/plugins/_v4_wide_s7_fix_2026_09_27.py` | `fc200e5f343d`／6,101 | 1 | `results/_v4_noise_cleanup_manifest_v4_2026_09_27.md` |
| 10 | `deposon_team/plugins/_v4_wide_s9_final_2026_09_27.py` | `aef86f53cc0e`／3,399 | 1 | 同上 |
| 11 | `deposon_team/plugins/_v4_wt_s0_verify_2026_09_27.py` | `4dcb81343577`／8,462 | 2 | `letters/_v4_walkthrough_bugfix_reply_trae_code_2026_09_27.md` ＋ 族内 `_v4_wt_s6_final` |
| 12 | `deposon_team/plugins/_v4_wt_s2_b1diff_2026_09_27.py` | `b61cb447f306`／2,015 | 2 | 同上 |
| 13 | `deposon_team/plugins/_v4_wt_s2_b1recheck_2026_09_27.py` | `e643ac7f9718`／5,650 | 2 | 同上 |
| 14 | `deposon_team/plugins/_v4_wt_s4_b4verify_2026_09_27.py` | `5e1ec533de1f`／2,595 | 2 | 同上 |
| 15 | `deposon_team/plugins/_v4_wt_s4b_b4recompute_2026_09_27.py` | `edcdfda20f91`／4,174 | 2 | 同上 |
| 16 | `deposon_team/plugins/_v4_wt_s4c_regonly_2026_09_27.py` | `20f265761280`／3,900 | 2 | 同上 |
| 17 | `deposon_team/plugins/_v4_wt_s6_final_2026_09_27.py` | `653077d03468`／3,435 | 2 | 同上 ＋ 族内 6 件互引 |

### §1.3 留候（2 目录／6 件）—— **硬杠命中，非仅存疑**

| # | 目录 | 件数／字节 | 判据 | 结论 |
|---:|---|---:|---|---|
| 18 | `results/_v3_recheck_08c_preexp_data/` | 3／199,587 | **目录 token 在合并面 23 处命中**，其中 **`docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（冻结勘误链）按名点名** ⇒ **硬杠①** | **不可移·留候** |
| 19 | `results/_v3_s_phrasetemplate_preexp_data/` | 3／86,909 | **目录 token 16 处命中**，**同样含冻结勘误链** ⇒ **硬杠①** | **不可移·留候** |

> ⚠️ **第一波盘点精度修正（如实登记）**：盘点件 §2.4 第 21 行曾将此 2 目录记为「**需 PI 裁**·表面引用数 396/103/405 不可直接采信（同名兄弟件 token 碰撞）·须先逐路径人工核」。本波以**目录 token 直查**（可靠判据）复算，结论**升级为硬杠命中**——两目录**均被冻结勘误链点名**，故非「存疑待核」而是**确定不可移**。盘点件原判**方向正确**（未误列为可移），此处**上收精度**。

---

## §2 移动清单（逐件移前／移后）

- **动作窗口**：`2026-10-01 19:56:26` → `19:56:26`（**单批 1 件，0 并行**）
- **方式**：`shutil.move`（**移动非复制** ⇒ 源 0 存在、可逆、0 覆盖）

| # | 源 | SHA-12（移前＝移后） | 字节 | 移前 mtime | 目标 | `src_gone` | `sha_match` | `size_match` |
|---:|---|---|---:|---|---|:--:|:--:|:--:|
| 1 | `D:\私人资料\deposon-repo\deposon_team\plugins\_v4_wide_s2_scan_2026_09_27.py` | `c2cc22b27047` | 4,000 | 2026-09-27 20:19:13 | `D:\私人资料\deposon-sub\tmp_movedout_2026_10_01\process_scripts\v4_wide_2026_09_27\_v4_wide_s2_scan_2026_09_27.py` | ✅ | ✅ | ✅ |

**`bad=0`｜移动 1 件／4,000 B。**

### §2.1 落位索引

| 源路径 | 目标路径 | SHA-12 | 字节 | 入库时点 |
|---|---|---|---:|---|
| `…\deposon-repo\deposon_team\plugins\_v4_wide_s2_scan_2026_09_27.py` | `…\deposon-sub\tmp_movedout_2026_10_01\process_scripts\v4_wide_2026_09_27\_v4_wide_s2_scan_2026_09_27.py` | `c2cc22b27047` | 4,000 | 2026-10-01 19:56:26 |

### §2.2 拉回路径（可逆）

`D:\私人资料\deposon-sub\tmp_movedout_2026_10_01\process_scripts\v4_wide_2026_09_27\` → `D:\私人资料\deposon-repo\deposon_team\plugins\`
（单文件反向移动即可；复原后 SHA-12 应为 `c2cc22b27047`／4,000 B）

### §2.3 落位后族内共位实测

`v4_wide_2026_09_27/` 现 **8 件**（第一波 7 ＋ 本波 1）：`s1b_inv2`、**`s2_scan`**、`s3`、`s3b_uuidctx`、`s3c_keydetail`、`s4_verify`、`s6_unrefscan`、`s8_fix3`。

---

## §3 合并分区撞名面核（PI 新约束）

### §3.1 第一波 10 件 ＋ 本波 1 件之撞名核（**新建冲突 0**）

| 波次 | 件 | 合并分区（repo＋sub）同名副本数 | 结论 |
|---|---|---:|---|
| 第一波 | `README_V1_LEGACY.md` | **1** | ✅ UNIQUE |
| 第一波 | `_v4_wide_s1b_inv2_2026_09_27.py` | **1** | ✅ UNIQUE |
| 第一波 | `_v4_wide_s3_keyscan_2026_09_27.py` | **1** | ✅ UNIQUE |
| 第一波 | `_v4_wide_s3b_uuidctx_2026_09_27.py` | **1** | ✅ UNIQUE |
| 第一波 | `_v4_wide_s3c_keydetail_2026_09_27.py` | **1** | ✅ UNIQUE |
| 第一波 | `_v4_wide_s4_verify_2026_09_27.py` | **1** | ✅ UNIQUE |
| 第一波 | `_v4_wide_s6_unrefscan_2026_09_27.py` | **1** | ✅ UNIQUE |
| 第一波 | `_v4_wide_s8_fix3_2026_09_27.py` | **1** | ✅ UNIQUE |
| 第一波 | `_v4_wt_s5_verify_2026_09_27.py` | **1** | ✅ UNIQUE |
| 第一波 | `volcengine_补测_worker_A_2026_09_10.py` | **1** | ✅ UNIQUE |
| **本波** | `_v4_wide_s2_scan_2026_09_27.py` | **1** | ✅ UNIQUE |

> **第一波 10 件之合并分区撞名面核结论：11/11 件（含本波）合并分区均唯一，0 新造同名冲突。**（注：`README_V1_LEGACY.md` 虽与历史根 README **字节级同源**，但旧根 README 已于 09-30 被现行 `README.md` 取代，故合并面**无同名副本**。）

### §3.2 既存同名面如实登记（**非本两波所造 · 0 处置**）

合并分区（repo＋sub，实测 **1,956 件**）现存 **64 个 basename 有多副本**。高关注者：

| basename | 副本数 | 说明 |
|---|---:|---|
| `check.py` | **35** | `verifier/v26`–`v43` 逐版本同名，版本目录区分 |
| `check.sh` | 8 | `verifier/v36`–`v43` |
| `executor_2026_09_27.py` | 5 | 5 个 V3 执行器目录内同名（**即第一波盘点 §2.4 第 21 行 token 碰撞之源**） |
| `COMPILE_SUMMARY.txt`／`compile_runner.ps1` | 4／4 | 构建面 |
| `_inspect_captions.py` | 3 | `corpus/v20_caption_surface/` ＋ `results/_archive_2026_09_24/` 等 |
| `erratum.md` | 2 | **建议 PI 留意**：同名双份，活跃/冻结归属未核 |
| `boss_p{a,b,c,e}_*`、`_v3x_*`、`deposon_volcengine_*`、`deposon_feshbach_*` 等 | 各 2 | 多为 `results/_archive_2026_09_24/` 与活跃面并存 |

⇒ 本两波**未新增任何同名冲突**；上列既存面**0 处置、如实登记**（处置权归 PI）。

---

## §4 目录终态实测

| 目录 | 本波前 | 本波后 | 说明 |
|---|---:|---:|---|
| `deposon-repo\deposon_team\plugins\` | 77 件 | **76 件** | −1 ＝ 本波 `s2_scan` ✅ |
| `deposon-sub\tmp_movedout_2026_10_01\` | 11 件 | **12 件** | ＋1；既有件 **0 触动** ✅ |

---

## §5 纪律自证

| 项 | 状态 |
|---|---|
| **仅触「需裁」清单内件** | 移动 1 件（`s2_scan`，清单内第 8 项）；「不可动」48 件 **0 触动**；`docs/V3X/` 0 触动 |
| **四硬杠保持** | 冻结勘误链／PI 上传口径外发信／取证链／R4 敏感命中者**全部留候**，含 §1.3 两预实验数据目录 |
| **⛔ 0 删除 0 联网** | 全棒 0 删除、0 trash、0 网络请求 |
| **⛔ 0 回改既有件** | 全仓只读（除 1 件移动）⇒ 依据件与前两波登记件 SHA-12 复核一致（见 §5.1） |
| **0 读敏感内容** | 本波 0 读任一被评估件之内容（仅字节流复算指纹）；R4 敏感件 0 读 |
| **署名如实** | 出证方 ＝ **worker** |
| **命名合规** | 本件名无 `_vN_` 阶段前缀；落位子目录沿既有惯例，**非新增阶段名** |
| **探针落盘** | 全部脚本落 `%TEMP%`，**0 落盘仓内**、0 进交付面 |

### §5.1 0 回改复核（实测）

| 件 | 字节 | SHA-12 实测 | 与登记值 | 结论 |
|---|---:|---|---|:--:|
| `results/_sub_transfer_candidates_2026_10_01.md` | 21,796 | `2f61c0aa2a2b` | `2f61c0aa2a2b` | **一致 ⇒ 0 回改** ✅ |
| `results/_sub_transfer_execution_register_2026_10_01.md`（第一波登记） | 13,377 | `c41013a975e0` | `c41013a975e0` | **一致 ⇒ 0 回改** ✅ |
| `results/_cleanup_round2_register_2026_09_29.md` | 36,245 | `ee47a2ec49f4` | `ee47a2ec49f4` | **一致 ⇒ 0 回改** ✅ |
| `results/_cleanup_round_2026_10_01.md` | 27,477 | `0db6e5d6146c` | `0db6e5d6146c` | **一致 ⇒ 0 回改** ✅ |

---

## §6 落盘自证

| 项 | 值 |
|---|---|
| 路径 | `results/_sub_transfer_wave2_register_2026_10_01.md`（**新名 · 无版本前缀**） |
| 版式 | **UTF-8 无 BOM · LF** |
| 产出件数 | **1 件即停**（本件为唯一新增件） |
| 派生件 | **0 JSON · 0 脚本 · 0 仓内临时件** |
| 既有件触动 | **0**（除 §2 明列 1 件移动） |
| 自核 | SHA-12／字节／行数 **见交付回执** |

---

**落款**：**worker** · 2026-10-01｜**重估 17 件 ＋ 2 目录：移 1 件／4,000 B（1/1 OK · bad=0）· 留候 16 件 ＋ 2 目录（硬杠命中）**｜0 删除 0 联网 0 回改既有件 · R4 0 读 key · 0 派工 · **产出 1 件即停**｜**待 PI 复核：§3.2 既存同名面 64 组（`erratum.md` 双份尤宜留意）、§1.2 留候 16 件是否放宽「1 处对外回函引用」判准、§1.3 精度上收（两预实验目录 ＝ 硬杠命中）**
