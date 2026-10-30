# `KD-H2` 锚链勘误登记件（v1 · append-only · 2026-10-20）

> **件别**：登记件（勘误体例·复用先例二）｜**棒别**：`evidence-auditor`（数据修订/资产处置·原 anchor-guard／corpus-keep／d7-pusher 三职统合）｜**授权面**：PI `v153-Q2` 采认之 `KD-H2` 处置面（**乙→甲之甲**）
> **观测时点**：2026-10-20 **14:07–14:28**（UTC+8）｜**落盘时点**：2026-10-20 14:28 之后
> **路径**：`〔幽灵引用·未上传:_kd_h2_anchor_chain_erratum_2026_10_20.md〕`
> **体例先例（复用）**：`results\_commission_v04_ghost_reference_erratum_2026_10_18.md`（本棒自测 `482eca247fa7`·37,518 B）＋`results\_ge01_spec_anchor_erratum_2026_10_14.md`（本棒自测 `2eeb522748ca`·18,129 B）

> ### 纪律声明（本件之自我约束·逐条可核）
> ⛔ **0** 回改／移动／删除任何既有件之一字（append-only·本件为**单立新件**）｜⛔ **0** 跑实验｜⛔ **0** LLM 调用｜⛔ **0** 读 `key`/`.env`｜⛔ **0** 经手 PAT｜⛔ **0** 联网（含写向）｜⛔ **0** 触仓外归档区**写**面（**只读面合规**）｜⛔ **0** 落五终判（pass·af·kd·fail·give-up）｜⛔ **0** 闭 `KD-H2`（**闭之判定权属 PI／verdict-keeper**）｜⛔ **0** 宣告段毕｜⛔ **0** 代 PI 裁｜⛔ **0** 借「口径」之名行改数之实（**计数口径差 ≠ 事实矛盾 ≠ 阈值调整**）。
> 凡引指纹**皆本棒自测**（工具：PowerShell 5.1 `Get-FileHash -Algorithm SHA256` → 前 12 位；**⛔ 0** 用内建 `hash()`（随机化·跨进程不稳定）；**⛔ 0** 用 `hashlib`／`Get-FileHash` 之外之任何哈希实现）。

---

## §0 本件之元数据·仪器面·停手闸

### §0-1 停手闸（落盘前实测）

| 项 | 结果 | 证据 |
|---|---|---|
| glob `results/*kd_h2_anchor_chain*` | **0 命中** | ripgrep glob·`path=〔本地路径已脱敏〕` |
| `Test-Path` 目标件 | **False** | 目标 `results\_kd_h2_anchor_chain_erratum_2026_10_20.md` 落盘前不存在 |
| 结论 | **闸开·可落盘** | 有则停手报回之条件未触发 |

### §0-2 仪器面（本棒自测·全部指针）

| # | 件（角色） | 本棒实测 SHA-12 | 字节 | 备注 |
|---|---|---|---:|---|
| I1 | `verifier/handoff/KT_ABC1_anchors_sha256_12.json`（权威锚表·读乙） | `03c6c01f3697` | 6,680 | 仓内·`metadata.date` ＝ **2026-09-09** |
| I2 | `deposon_team/plugins/_verify_15frozen.py`（冻结仪器·读甲之源） | `efae9274962e` | 3,905 | 76 行·**BOM=True** |
| I3 | `deposon_team/plugins/_verify_pg_v0.py`（第二冻结仪器） | `cdd3415ad993` | 3,978 | 87 行·**BOM=True** |
| I4 | `results/_deposon_full_history_sub_2026_10_19.md`（对照版） | `a572747a2001` | 45,958 | 其 §5／§6／§8 之读数·本件部分照录 |
| I5 | `results/_h5_session_census_2026_10_19_part2.md`（普查件 part2） | `105413bee0ba` | 451,607 | 其 §15-2 之读数·本件部分照录·**部分由本棒复算覆盖** |
| I6 | `results/_kd_h1_h7_disposition_draft_2026_10_20.md`（处置拟案） | `42ea79ea3f06` | 72,915 | 其 §2 之 `C2` 口径面与甲／乙／丙／丁候选面 |
| I7 | `verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json`（**派生补丁 JSON**·本棒新增定位） | `da517c115f3c` | 5,049 | sub 区与归档区各一份·**逐件同哈希**（SAME_IDENTITY） |
| I8 | `results/_harness_anchor_reconcile_register_2026_10_16.md`（harness reconcile 登记件） | `4de10aad8f0b` | 26,023 | 载 `P_A_HARNESS` 三层漂移链 |
| I9 | `results/_t5_anchor_drift_authorized_register_2026_10_15.md`（T5 漂移授权登记件） | `1308662a369a` | 11,553 | `drift_class: legal_rework` |
| I10 | `results/_ge01_5anchor_json_register_2026_10_14.md`（GE01 5 锚登记件） | `65000a1ac5bc` | 31,882 | 载锚④ 漂移·`KD-R6` 未闭 |
| I11 | `results/_ge01_prereg_5anchor_v2_lock_register_2026_10_15.md`（v2 锁记件） | `ed3b544d33a6` | 17,808 | 落款 `evidence-auditor · 2026-10-15` |
| I12 | `〔归档区〕/verify_archive_backup/_verify_15frozen.py`（归档侧第一仪器·异仪器） | `c196aa7709ef` | 3,883 | 67 行·**BOM=False**·**无 `REPO_BASE`/`ARCHIVE_BASE` 常量** |

### §0-3 仪器自审记录（**测量仪器自身即误差源**·本棒之两次自纠）

📌 **诚实交代**：本棒之复算仪器在落盘前出过两次自身错误，**均先修仪器、未动任何在册文本**：

| 仪器缺陷 | 现象 | 处置 |
|---|---|---|
| 变量名大小写不敏感自撞（`$A` 与 `$a` 同变量） | 首轮「冻结仪器复刻」输出仅 2 行且路径退化为首字符（`d`／`3`） | 改用互不撞名之变量（`$list16`／`$item`）后重跑，得正确 16 行 |
| 格式串占位符个数错（4 占位 3 参） | BOSS 区段穷举首轮抛 `FormatError` | 改为 3 占位后重跑，得全 9 行 |

⇒ **两处错误皆在「本棒自出之读数」侧，未污染任何既有件**（⛔ 0 回改他人件一字）。此即「**审计工具先审自己**」之自律面。

---

## §1 锚链之沿革面（各锚现态·观测时点 **2026-10-20 14:07–14:28**·指纹本棒自测）

### §1-0 锚域之口径（`C2` 面·**两集合并列·⛔ 0 互比**）

📌 **本件之口径前提**（照录处置拟案 §0-5 之 `C2` 与 §2-2 之乙径）：「冻结锚」之域**未被 PI 择定**，故本件**两集合并列出**（读甲 16 锚／读乙 15 条），并**增设第三区段**（锚表 `boss_baselines` 9 条·**此前两读皆未覆盖**·本棒补测）。

⇒ **本件的一切计数**皆按「集合名＋口径」分列，**⛔ 0 将三者互相替代或合并**（**计数口径差 ≠ 事实矛盾**）。

| 集合 | 来源 | 条数 | 展开实体行 | 本件简称 |
|---|---|---:|---:|---|
| 甲 | `I2` 之 `files_15`（**名实差：名 15·实载 16**） | **16** | 16 | **读甲** |
| 乙 | `I1` 之 `anchors` 区段 | **15** | 19（一锚五值） | **读乙** |
| 丙 | `I1` 之 `boss_baselines` 区段（**本棒新增覆盖面**） | **9** | 9 | **读丙** |

### §1-1 读甲（16 锚）逐件现态

**查找域（本棒）**：`repo` → `sub` → `nula`（归档区）→ `sub\_archive`；**判定以「实件是否存在且哈希与登记值相符」为准**。

| # | 相对路径 | 登记 SHA-12 | 实测 SHA-12（本棒） | 字节 | mtime | 落位 | 判定 |
|---:|---|---|---|---:|---|---|:--:|
| 1 | `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | `03c6c01f3697` | `03c6c01f3697` | 6,680 | 2026-09-09 13:19:32 | repo | **MATCH** |
| 2 | `docs/V3X/KT_A1_SPEC_V0.1.md` | `78b71d404366` | `78b71d404366` | 29,570 | 2026-09-09 13:42:23 | sub | **MATCH** |
| 3 | `docs/V3X/KT_B1_SPEC_V0.1.md` | `0410ca0fbdae` | **`0397b757362f`** | 39,206 | **2026-09-30 20:36:32** | sub | 🔴 **MISMATCH** |
| 4 | `docs/V3X/KT_C1_SPEC_V0.1.md` | `59d8f56347d5` | `59d8f56347d5` | 31,241 | 2026-09-09 13:42:23 | sub | **MATCH** |
| 5 | `docs/V3X/KT_D0_SPEC_V0.1.md` | `cce8e9a1b00e` | `cce8e9a1b00e` | 20,927 | 2026-09-09 13:42:24 | sub | **MATCH** |
| 6 | `docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md` | `b10fae0da66d` | `b10fae0da66d` | 6,375 | 2026-09-11 12:15:55 | sub | **MATCH** |
| 7 | `results/deposon_v19_benchmark_fixes.json` | `910c4333eead` | `910c4333eead` | 409,104 | 2026-08-24 01:11:01 | repo | **MATCH** |
| 8 | `results/deposon_v21_gtformal.json` | `9d9ae5001c57` | `9d9ae5001c57` | 69,204 | 2026-08-30 15:44:09 | repo | **MATCH** |
| 9 | `corpus/v20/index.json` | `8423ffe266af` | `8423ffe266af` | 7,335 | 2026-08-28 23:53:05 | repo | **MATCH** |
| 10 | `verifier/handoff/P_F_PREDECISION_2026_09_09.json` | `b41c98bf90cc` | `b41c98bf90cc` | 3,680 | 2026-09-09 13:50:15 | sub ＋ nula | **MATCH**（**SAME_IDENTITY×2**） |
| 11 | `docs/V3X/P_F_SPEC_V0.md` | `de90faf362c5` | `de90faf362c5` | 19,804 | 2026-09-09 13:50:05 | sub | **MATCH** |
| 12 | `docs/V3X/P_F_RESEARCH_2026_09_09.md` | `98085df7811a` | `98085df7811a` | 17,603 | 2026-09-09 13:49:14 | sub | **MATCH** |
| 13 | `deposon_team/plugins/skill_a_p_a_60cells.py` | `b1463bb24403` | `b1463bb24403` | 9,078 | 2026-09-11 17:05:38 | repo | **MATCH** |
| 14 | `deposon_team/plugins/skill_b_p_c_alpha_beta.py` | `e5a299f69a22` | `e5a299f69a22` | 8,699 | 2026-09-11 17:05:38 | repo | **MATCH** |
| 15 | `deposon_team/plugins/skill_c_p_e_3modality.py` | `e19e76c5da7e` | `e19e76c5da7e` | 8,915 | 2026-09-11 17:05:38 | repo | **MATCH** |
| 16 | `deposon_team/plugins/skill_d_p_f_observer.py` | `3e369a1f6171` | `3e369a1f6171` | 15,927 | 2026-09-15 13:30:57 | repo | **MATCH** |

> **读甲合计（本棒实测）**：**MATCH 15 ／ MISMATCH 1 ／ MISSING 0** —— 与对照版 `I4` §5-1 之逐件表（15／1／0）**逐位一致**（含 MISMATCH 行之登记值·实测值·字节·落位）。
> **落位分布之差（口径差·非事实差）**：本棒查找序得 **repo 8 ／ sub 8**；对照版记 **repo 8 ／ sub 7 ／ archive 1**。差异**仅在第 10 行**（`P_F_PREDECISION_2026_09_09.json`）：本棒实测其实体**在 sub 区与归档区各一份且逐件同哈希**（`b41c98bf90cc`·3,680 B）⇒ **落位归属之别（同一实体之双处镜像）·⛔ 0 当作「多一锚」计**（**SAME_IDENTITY·防重复计数**）。

### §1-2 读乙（15 条·展开 19 实体行）逐件现态

#### §1-2-1 仓内命中面（13 行）

| 锚名 | 组 | 登记路径 | 登记 SHA-12 | 实测 SHA-12 | 字节 | mtime | 落位 | 判定 |
|---|---|---|---|---|---:|---|---|:--:|
| `P_A_ECR_BASELINE` | KT-A1 | `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` | `bd1caab42b4c` | `bd1caab42b4c` | 10,351 | 2026-09-09 10:05:24 | sub | **MATCH** |
| `P_A_KILL_LINE` | KT-A1 | 同上（同件两锚） | `bd1caab42b4c` | `bd1caab42b4c` | 10,351 | 2026-09-09 10:05:24 | sub | **MATCH** |
| `P_A_FROZEN_RUNS[1/5]` | KT-A1 | `results/deposon_v20_baselines.json` | `6edb2aec1660` | `6edb2aec1660` | 16,987 | 2026-08-29 01:17:30 | repo | **MATCH** |
| `P_A_FROZEN_RUNS[2/5]` | KT-A1 | `results/deposon_v19_benchmark_fixes.json` | `910c4333eead` | `910c4333eead` | 409,104 | 2026-08-24 01:11:01 | repo | **MATCH** |
| `P_A_FROZEN_RUNS[3/5]` | KT-A1 | `results/deposon_v21_gtformal.json` | `9d9ae5001c57` | `9d9ae5001c57` | 69,204 | 2026-08-30 15:44:09 | repo | **MATCH** |
| `P_A_FROZEN_RUNS[4/5]` | KT-A1 | `results/deposon_v18_api_supplements.json` | `62c1a41e1db8` | `62c1a41e1db8` | 80,624 | 2026-08-23 23:20:04 | repo | **MATCH** |
| `P_A_FROZEN_RUNS[5/5]` | KT-A1 | `results/deposon_v17_fusion_fix.json` | `af51da229652` | `af51da229652` | 106,164 | 2026-08-23 21:31:41 | repo | **MATCH** |
| `P_A_LLM_CLIENT` | KT-A1 | `tools/llm_client.py` | `055e874ea5c1` | **`1722500da4aa`** | 8,118 | 2026-09-09 16:16:02 | repo | 🔴 **MISMATCH** |
| `P_A_HARNESS` | KT-A1 | `tools/exp_harness.py` | `9f383935c00c` | **`ce64b9b97489`** | 45,590 | **2026-10-18 13:20:34** | repo | 🔴 **MISMATCH** |
| `KT_B1_V19_BENCHMARK` | KT-B1 | `results/deposon_v19_benchmark_fixes.json` | `910c4333eead` | `910c4333eead` | 409,104 | 2026-08-24 01:11:01 | repo | **MATCH** |
| `KT_B1_KILL_LINE` | KT-B1 | `verifier/kill_lines/kt_b1_kill_decision.py` | `9f351078e5bf` | `9f351078e5bf` | 2,781 | 2026-09-09 13:17:24 | repo | **MATCH** |
| `KT_B1_AUDIT_FUNCTION` | KT-B1 | `verifier/audit/conservation.py` | `3aa661cfbab5` | **`4bdec2683f06`** | 22,105 | 2026-09-10 09:29:22 | repo＋sub＋nula | 🔴 **MISMATCH**（SAME_IDENTITY×3） |
| `KT_C1_V21_FROZEN` | KT-C1 | `results/deposon_v21_gtformal.json` | `9d9ae5001c57` | `9d9ae5001c57` | 69,204 | 2026-08-30 15:44:09 | repo | **MATCH** |

#### §1-2-2 登记路径在仓内 0 命中、而实件在仓外之面（6 行·**本棒核心新增观测**）

| 锚名 | 组 | 登记路径（仓相对） | 实件所在区（**仓外**） | 登记 SHA-12 | 实测 SHA-12 | 字节 | mtime | 判定 | 分支 |
|---|---|---|---|---|---|---:|---|:--:|---|
| `KT_C1_KILL_LINE` | KT-C1 | `docs/V3X/KT_C1_SPEC_V0.md` | `〔归档区〕\docs\V3X\` | `77b49c0f8b54` | `77b49c0f8b54` | 17,940 | 2026-09-09 11:14:23 | **MATCH** | `GHOST_REF_OUTSIDE`（同相对路径·内容同一） |
| `KT_C1_LOGLOG_FIT` | KT-C1 | `.mavis/scripts/kt_c1/kt_c1_loglog_fit.py` | `nula\scripts\scripts\kt_c1\` | `7df20f7b3084` | `7df20f7b3084` | 3,837 | 2026-09-09 13:16:53 | **MATCH** | `GHOST_REF_OUTSIDE`＋**路径登记失效** |
| `KT_C1_ETA_SCAN` | KT-C1 | `.mavis/scripts/kt_c1/eta_scan.py` | `nula\scripts\scripts\kt_c1\` | `b7e3c3717d11` | `b7e3c3717d11` | 1,910 | 2026-09-09 13:18:45 | **MATCH** | `GHOST_REF_OUTSIDE`＋**路径登记失效** |
| `KT_C1_HARNESS` | KT-C1 | `.mavis/scripts/kt_c1/harness.py` | `nula\scripts\scripts\kt_c1\` | `8488425898fb` | `8488425898fb` | 2,061 | 2026-09-09 13:18:49 | **MATCH** | `GHOST_REF_OUTSIDE`＋**路径登记失效** |
| `KT_B1_ATTACK_BANK` | KT-B1 | `.mavis/scripts/kt_b1/attacker.py` | `nula\scripts\scripts\kt_b1\` | `4b37a40cc984` | **`dc78f9a89b1c`** | 10,320 | 2026-09-09 16:17:32 | 🔴 **MISMATCH** | `GHOST_REF_OUTSIDE`＋**内容已变** |
| `KT_B1_HARNESS` | KT-B1 | `.mavis/scripts/kt_b1/harness.py` | `nula\scripts\scripts\kt_b1\` | `39dacb572f2e` | **`3bcd1b03e4fd`** | 7,557 | 2026-09-09 16:18:06 | 🔴 **MISMATCH** | `GHOST_REF_OUTSIDE`＋**内容已变** |

> **读乙合计（本棒实测·四区查找域）**：**MATCH 10 ／ MISMATCH 5 ／ MISSING_FILE 0**（以 15 条计）。
> 📌 **与普查件 `I5` §15-2 之读数之差（本棒新观测）**：普查件（2026-10-19）记 **MATCH 4 ／ MISMATCH 3 ／ MISSING_FILE 8**；本棒（2026-10-20·四区域）记 **MATCH 10 ／ MISMATCH 5 ／ MISSING_FILE 0**。
> ⇒ **普查件之 8 条 `MISSING_FILE`，在本棒之四区查找域下 0 条为真缺件**：其中 **6 条实件在盘且内容与登记值逐位相符**（`P_A_ECR_BASELINE`／`P_A_KILL_LINE`／`KT_C1_KILL_LINE`／`KT_C1_LOGLOG_FIT`／`KT_C1_ETA_SCAN`／`KT_C1_HARNESS`），**2 条实件在盘但内容已变**（`KT_B1_ATTACK_BANK`／`KT_B1_HARNESS`）。
> ⇒ **判读（⛔ 0 断言普查件之失误成因）**：二者之差**与「查找域口径」一致**（普查件之域未及 sub 区与归档区）⇒ 本件仅登记**读数之时点与域之差**，**⛔ 0 判定其失误·⛔ 0 改判其在册读数·⛔ 0 立新 KD**。

### §1-3 读丙（锚表 `boss_baselines` 9 条·**此前两读皆未覆盖·本棒补测**）

| 锚名 | 组 | 登记路径 | 实件所在区（**全部仓外**） | 登记 SHA-12 | 实测 SHA-12 | 字节 | mtime | 判定 |
|---|---|---|---|---|---|---:|---|:--:|
| `BOSS-A1 RBR/RM` | KT-A1 | `.mavis/scripts/kt_a1/boss_a1_rbr_rm.py` | `nula\scripts\scripts\kt_a1\` | `91a62de1fa50` | `91a62de1fa50` | 20,538 | 2026-09-09 11:54:08 | **MATCH** |
| `BOSS-A2 Potential Game` | KT-A1 | `.mavis/scripts/kt_a1/boss_a2_potential_game.py` | 同上 | `b6339d9f2435` | `b6339d9f2435` | 13,475 | 2026-09-09 11:54:08 | **MATCH** |
| `BOSS-A3 Replicator Dynamics` | KT-A1 | `.mavis/scripts/kt_a1/boss_a3_replicator_dynamics.py` | 同上 | `27d04f1e3b3e` | `27d04f1e3b3e` | 14,417 | 2026-09-09 11:54:08 | **MATCH** |
| `BOSS-B1 Sinkhorn OT` | KT-B1 | `.mavis/scripts/kt_b1/boss_b1_sinkhorn_ot.py` | `nula\scripts\scripts\kt_b1\` | `19325960b8be` | **`7c2b41c008a5`** | 16,404 | **2026-09-10 10:04:29** | 🔴 **MISMATCH**（+1,448 B） |
| `BOSS-B2 KD` | KT-B1 | `.mavis/scripts/kt_b1/boss_b2_kd.py` | 同上 | `1781ea2f742d` | **`8c6e98034005`** | 15,677 | **2026-09-10 10:04:29** | 🔴 **MISMATCH**（+1,453 B） |
| `BOSS-B3 LLMLingua` | KT-B1 | `.mavis/scripts/kt_b1/boss_b3_llmlingua.py` | 同上 | `c0b55e0385a4` | **`2ded5cf0e863`** | 15,389 | **2026-09-10 10:04:29** | 🔴 **MISMATCH**（+1,423 B） |
| `BOSS-C1 2D Ising` | KT-C1 | `.mavis/scripts/kt_c1/boss_c1_2d_ising.py` | `nula\scripts\scripts\kt_c1\` | `d47722a1123a` | `d47722a1123a` | 3,226 | 2026-09-09 13:18:09 | **MATCH** |
| `BOSS-C2 Transverse Ising` | KT-C1 | `.mavis/scripts/kt_c1/boss_c2_transverse_ising.py` | 同上 | `ce2196c90cbc` | `ce2196c90cbc` | 2,325 | 2026-09-09 13:18:11 | **MATCH** |
| `BOSS-C3 Reservoir` | KT-C1 | `.mavis/scripts/kt_c1/boss_c3_reservoir.py` | 同上 | `506d85c37e11` | `506d85c37e11` | 2,399 | 2026-09-09 13:18:13 | **MATCH** |

> **读丙合计**：**MATCH 6 ／ MISMATCH 3 ／ MISSING_FILE 0**。
> 📌 **观测**：B 族三件之 mtime **同刻**（2026-09-10 10:04:29）且增量**同向近等**（+1,448／+1,453／+1,423 B）⇒ **同族同刻之同一改动面**之形；**⛔ 0 断言成因**（⛔ 0 断为篡改·⛔ 0 断为正常演进·⛔ 0 断为某一机制）——**登记为待裁面**。

### §1-4 沿革注记（各 MISMATCH 锚之三代链与登记件覆盖状况）

| 锚 | 登记值 | 现值（mtime） | 沿革链 | 在册 reconcile／漂移载体 | 沿革登记完备性 |
|---|---|---|---|---|---|
| `KT_B1_SPEC_V0.1.md`（读甲#3） | `0410ca0fbdae` | `0397b757362f`（09-30 20:36:32） | 旧值实体**在盘**：`〔归档区〕\results\_remote_version_freeze_2026_09_26\KT_B1_SPEC_V0.1.md`（`0410ca0fbdae`·35,688 B）；现件 ＋ **+9 行**「〔2026-09-30 口径变更 · C4〕」「〔2026-09-30 补注 · 来源名更新〕」注记（**照录对照版 §5-2·原文一字未删改·⛔ 本棒 0 复算 diff**）；另见**第三值** `4790680c80c1`·39,385 B（pullback 区 `docs__V3X__KT_B1_SPEC_V0.1.md`） | ⛔ 本棒检索**未见**专任「重锚登记件」 | ⚠ **未排除**对照版 §5-2「读法乙」之条件（*若无重锚登记件，则属锚链断裂*） |
| `P_A_LLM_CLIENT` | `055e874ea5c1` | `1722500da4aa`（09-09 16:16:02） | OLD（5 锚 JSON）→ **09-15 派生补丁 NEW** → 现值（**与 NEW 逐位相符**） | **有**：`I7`（`da517c115f3c`·`patch_status: PENDING`）＋ GE01 族（`I10`／`I11`·载锚④ 漂移·`KD-R6` 未闭） | ✅ **漂移已登记**；惟 **5 锚 JSON 自身未重锚**（`03c6c01f3697` 至今仍载 OLD 值） |
| `P_A_HARNESS` | `9f383935c00c` | `ce64b9b97489`（10-18 13:20:34） | **四层链**：`9f383935c00c` →（09-15 裁 `DRIFT_AUTHORIZED`）→ `275e480ba4d9`(10,090 B) →（T5 补造）→ `7957bac14455`(13,342 B) →（T3 可答化）→ `7a097d7802d1`(15,708 B) →（**10-18 变动**）→ `ce64b9b97489`(45,590 B) | **前三层有**：`I9`（T5 漂移授权·`legal_rework`）＋ `I8`（harness reconcile·自载「现值」＝ `7a097d7802d1`） | ⚠ **最末一层（10-18 之变动）无对应在册登记**——`I8` 之「现值」字段**已过期** |
| `KT_B1_AUDIT_FUNCTION` | `3aa661cfbab5` | `4bdec2683f06`（09-10 09:29:22） | 旧值实体**未在四区寻得**（0 命中）；现值**三处副本逐件同哈希**（repo／sub\_archive／nula） | **有**：冻结仪器注释载「Q2 PATCH_5ANCHOR_RECONCILE 提及 V0=4bdec2683f06」＋ `V3X_PATCH_5ANCHOR_RECONCILE_V2_2026_09_17`（sub 区＋pullback 副本）＋仓内 `.tmp\hfr_scan_b_items.json` 载「P-4 于归档区命中并已回拉（`4bdec2683f06`·22,105 B）」 | ✅ **漂移已登记**（惟旧登记值实体不在盘） |
| `KT_B1_ATTACK_BANK` | `4b37a40cc984` | `dc78f9a89b1c`（09-09 16:17:32） | 锚表落盘（09-09 **13:19:32**）→ 漂移于同日 **16:17:32**（登记时点值**正确**·漂移在其后 3 小时） | ⛔ 本棒检索（**repo 域完成·sub 域中止**）**未见**覆盖该值之 reconcile 登记件 | ⚠ **未见登记**（检索面有限·如实登记） |
| `KT_B1_HARNESS` | `39dacb572f2e` | `3bcd1b03e4fd`（09-09 16:18:06） | 同上（漂移于锚表落盘后 2 分 59 秒） | ⛔ 同上 | ⚠ **未见登记**（检索面有限） |
| `BOSS-B1/B2/B3` | `19325960b8be`／`1781ea2f742d`／`c0b55e0385a4` | `7c2b41c008a5`／`8c6e98034005`／`2ded5cf0e863`（**09-10 10:04:29 同刻**） | 同族同刻之同向增量（约 +1.4 KB×3） | ⛔ 本棒**未见** | ⚠ **未见登记·成因⛔ 0 断言** |

### §1-5 落位映射规则之实测（**归档扁平化之实证**）

📌 锚表之 13 条登记路径以 `.mavis/scripts/kt_{a1,b1,c1}/…` 为前缀；仓内 `.mavis` 之实存内容（`repo\.mavis\scripts\`）**仅余** `kt_a1\test_persist.txt`／`test_write.txt`／`kt_b1\fix_safe_float.py`／`kt_c1\test_write.txt` 及 `cleanup511\` 族——**锚表所指之 13 件皆不在仓内**。
⇒ **实存面**：`〔归档区〕\scripts\scripts\kt_{a1,b1,c1}\…`。
⇒ **映射规则（由逐位相符反证·非推测）**：`.mavis/scripts/kt_X/Y` → `scripts/scripts/kt_X/Y`（归档扁平化时以 `scripts` 替 `.mavis` 之层级）。**反证之锚**：`KT_C1_LOGLOG_FIT`（`7df20f7b3084`·✓）＋`KT_C1_ETA_SCAN`（`b7e3c3717d11`·✓）＋`KT_C1_HARNESS`（`8488425898fb`·✓）＋`BOSS-C1/C2/C3`（三件✓）＝ **7 件逐位相符**；**同规则下** `KT_B1_ATTACK_BANK`／`KT_B1_HARNESS` 虽落同式路径，但哈希**不符**（见 §1-4）⇒ **路径迁位 ≠ 内容同一**，两者须分判。

### §1-6 现态小结（三读之计数并列表·**⛔ 0 互比**）

| 读 | 本棒实测（2026-10-20·四区域） | 在册前读 | 差之性质 |
|---|---|---|---|
| **读甲**（16 锚） | **MATCH 15 ／ MISMATCH 1 ／ MISSING 0** | 对照版 `I4` §5-1（10-19 18:59:23）＝ **15／1／0** | ✅ **逐位一致** |
| **读乙**（15 条） | **MATCH 10 ／ MISMATCH 5 ／ MISSING_FILE 0** | 普查件 `I5` §15-2（10-19 21:12–21:53）＝ **MATCH 4 ／ MISMATCH 3 ／ MISSING_FILE 8** | ⚠ **差**：8 条 `MISSING_FILE` 之实件**本棒皆在盘**（6 同一·2 已变）⇒ **域／时点差**，**⛔ 0 视作矛盾·⛔ 0 以新读替换旧读** |
| **读丙**（9 条） | **MATCH 6 ／ MISMATCH 3 ／ MISSING_FILE 0** | **0 在读**（此前两读皆未覆盖此区段） | 📌 **覆盖面扩展·非口径变更** |

> **实体级总计（本棒）**：读甲 16 ＋ 读乙 19 ＋ 读丙 9 ＝ **44 行实体**；其中 **仓内命中 13 行**（读乙）＋ **仓外实件 31 行**；**真缺件 0 行**（**⚠ 仅在本棒之四区查找域下成立·见 §5 诚实边界**）。

---

## §2 断链面（`ARCHIVE_BASE` 常量之现值与指向面）

### §2-1 常量现值（本棒逐字回读·两仪器同值）

| 仪器 | 行位 | 常量 | 现值（本棒逐字回读） |
|---|---|---|---|
| `I2` `_verify_15frozen.py` | **L11–L12** | `REPO_BASE` / `ARCHIVE_BASE` | `REPO_BASE = r'〔本地路径已脱敏〕'`｜**`ARCHIVE_BASE = r'〔本地路径已脱敏〕'`** |
| `I3` `_verify_pg_v0.py` | **L5–L6** | 同名常量 | **同值逐字相同**（`ARCHIVE_BASE = r'〔本地路径已脱敏〕'`） |
| `I12` 归档侧 `_verify_15frozen.py` | — | — | **无 `REPO_BASE`／`ARCHIVE_BASE` 常量**（67 行版·走仓内相对路径） |

> 📌 **口径提示**：`I2` 变量名 `files_15` **实载 16 条**（**名实差**）⇒「15 frozen」之语与其承载之 16 锚**字面不符**，本件一律以「**读甲 16 锚**」称之。

### §2-2 指向面之实况（本棒 `Test-Path` 实测）

| 区 | 路径 | `Test-Path` | 实存 |
|---|---|:--:|---|
| 常量所指 | `〔本地路径已脱敏〕` | 🔴 **False** | **0 件**（**断链**） |
| 同名目录（他区） | `〔幽灵引用·未上传:_archive_deposon_2026_09_17〕` | **True** | **1 件**：`verifier\audit\conservation.py`·22,105 B·`4bdec2683f06` |
| 归档区（他名） | `〔归档区〕` | **True** | 39,716+ 件（其内含 `.mavis`／`tools`／`verifier`／`docs`／`results` 等） |

### §2-3 断链之**可观测后果**（本棒新增实测·**仪器复刻**）

📌 **法**：**⛔ 0 执行**该二脚本（本任务 ⛔ 0 跑实验）；本棒**复刻其 `resolve()` 逻辑**（`repo` → `ARCHIVE_BASE`，命中即取），对其 16 锚逐件复算：

> **仪器复刻结果：OK = 8 ／ FAIL = 8**（8 条为 `FAIL(MISSING)`：`KT_A1_SPEC_V0.1.md`／`KT_B1_SPEC_V0.1.md`／`KT_C1_SPEC_V0.1.md`／`KT_D0_SPEC_V0.1.md`／`P_F_V0_1_UPGRADE_2026_09_11.md`／`P_F_PREDECISION_2026_09_09.json`／`P_F_SPEC_V0.md`／`P_F_RESEARCH_2026_09_09.md`）
> ⇒ **该脚本末行之 `0-touch declaration` 今日复刻值为 `FAIL`**（其自身口径下）。
> ⇒ **成因（可核·非推测）**：该 8 条锚之实体**在 `deposon-sub` 区**，而仪器之 `resolve()` **只知 `repo` 与已断链之 `ARCHIVE_BASE`**——**8/16 之锚于仪器视野外**。
> ⇒ **判读**：**断链之实害非「常量失效」本身，乃「冻结核验仪器今日已不能完成其自身任务」**（16 锚中半数在仪器外）。此即「**测量仪器自身即误差源**」之实证面：**引用「16/16 PASS」之前须先声明所用仪器与所用域**。

### §2-4 幽灵引用对账（三方比对·五分支判定）

| # | 被引路径／常量 | 引自 | 盘上实况（本棒实测） | 分支 |
|---:|---|---|---|:--:|
| G1 | `〔本地路径已脱敏〕`（`ARCHIVE_BASE`） | `I2:12`、`I3:6` | `Test-Path=False`；同名目录实存于 sub 区（1 件） | **GHOST_REF_OUTSIDE**（实件在他区） |
| G2 | `results\.evidence_backup_2026_09_30` | `〔归档区〕\ARCHIVE_INDEX.md` §2.1/§3.1（照录 `I4`） | 本棒实测 **repo／sub／nula 三区 `results\` 下皆 `Test-Path=False`**；归档侧实存于 `_movedout_scratch_2026_09_30\evidence_backup_2026_09_30\` | **GHOST_REF_OUTSIDE** |
| G3 | `results\.evidence_backup_2026_09_28` | 同上 §2.1/§3.2 | 同上 **三区皆 False**；归档侧 `_movedout_scratch_2026_09_30\evidence_backup_2026_09_28\` 实存：**4 件**（`runtime-state.sqlite`·474,656,768 B·SHA-256 前 12 位 **`4a7a2a55184a`**·`‑shm`·32,768 B·`‑wal`·0 B·`tracking-2026-09-27.json`·9,722 B） | **GHOST_REF_OUTSIDE** |
| G4 | 锚表 13 条 `.mavis/scripts/…` 登记路径 | `I1` | 仓内 0 命中；实件在归档区 `scripts/scripts/…`（映射见 §1-5） | **GHOST_REF_OUTSIDE**（13 条中 9 条内容同一·2 条已变·2 条见读丙） |

> 📌 **计数口径差之登记**：对照版 `I4` §6-G3 转录「2 件／474,666,490 B」；本棒实测 **4 件／474,699,258 B**。二者之差＝**是否计入 sqlite 边车文件**（`‑shm` 32,768 B ＋ `‑wal` 0 B）——**计数口径差·非事实矛盾**；且对照版所述之 sqlite **SHA-256 前 12 位 `4a7a2a55184a` 本棒逐位复核相符**。

### §2-5 资产缺陷登记（**只登记·frozen 内不代修·⛔ 0 代修**）

| # | 缺陷 | 位置·证据（本棒自测） | 影响面 |
|---:|---|---|---|
| A-1 | **引用路径非 repo 相对路径**（仓外绝对依赖） | `I2:11-12`、`I3:5-6` 之 `REPO_BASE`／`ARCHIVE_BASE` 硬编码绝对路径 | 换机／换区即失效；见 §2-2 |
| A-2 | **UTF-8 BOM** | `I2` **BOM=True**（首字节 `EF BB BF`·76 行）｜`I3` **BOM=True**（87 行）｜归档侧 `I12` **BOM=False** | 与全项目「UTF-8 无 BOM」体例相悖；⛔ 本棒 0 代修 |
| A-3 | **同名异仪器**（**二处·非一处**） | ① `_verify_pg_v0.py`：仓内 `cdd3415ad993`·3,978 B·87 行·**BOM=True·有 fallback** ↔ 归档 `e004327ffb74`·4,172 B·82 行·**BOM=False·无 fallback**；② `_verify_15frozen.py`：仓内 `efae9274962e`·3,905 B·76 行·**BOM=True·有 `ARCHIVE_BASE` 常量** ↔ 归档 `c196aa7709ef`·3,883 B·67 行·**BOM=False·无该常量** | **测量仪器自身分歧** ⇒「0 触动 PASS/FAIL」之结论**依赖所选仪器**；引用前须先声明用哪一件 |
| A-4 | **乱码注释（编码损坏）** | `I2` 第 40 行：`user 鎷嶆澘 strict 闃堝€艰惤`（归档侧 `I12` 之头部注释**整段乱码**） | 注释不可读；损毁可读证据 |
| A-5 | **名实差** | `I2` 之变量名 `files_15` 实载 **16** 条 | 「15 frozen」之语与承载体字面不符；易致计数口径漂移 |
| A-6 | **锚表之 `path` 字段已失效**（**本棒新增**） | `I1` 之 13 条登记路径在仓内 **0 命中**（实件在归档区·映射见 §1-5） | 凡以锚表 `path` 之引用作仓内定位者**必致 0 命中** |

---

## §3 两锚表之口径差登记（**对象集之异·⛔ 0 互比**）

### §3-1 对象集之异（路径级对照·照录拟案 `N3` 之面并由本棒复算支撑）

| 项 | 读甲（`I2` 之 `files_15`） | 读乙（`I1` 之 `anchors`） | 读丙（`I1` 之 `boss_baselines`） |
|---|---|---|---|
| 条数 | **16** | **15**（展开 19 实体行） | **9** |
| 覆盖对象 | frozen 链之 16 锚（含 2 锚 JSON 自身之一、spec 族、plugin 族、语料索引、run JSON 族） | KT-A1/B1/C1 三族之 15 锚（含 P-A 三锚、run JSON 五件、tool 两件、kill_line 三件、D2 实现五件） | 三族之 9 个 BOSS baseline 实现件 |
| 登记时点 | 09-16／09-17（`I2` 头部「FROZEN POLICY (2026-09-16)」＋「2026-09-17 update」） | **2026-09-09**（`metadata.date`） | 2026-09-09（同表） |
| 落位现实 | 主仓已不持多数：repo 8／sub 8（对照版记 archive 1） | 仓内 13 行·仓外 6 行 | **9/9 在仓外** |
| **路径级交集** | — | **仅 2 件**：`results/deposon_v19_benchmark_fixes.json`／`results/deposon_v21_gtformal.json` | 0 件 |

### §3-2 三读之计数并列表（**⛔ 0 互比·⛔ 0 合并·⛔ 0 互替**）

| 读 | 集合大小 | MATCH | MISMATCH | MISSING_FILE | 在册前读 | 互比之禁 |
|---|---:|---:|---:|---:|---|---|
| 读甲 | 16 | 15 | 1 | 0 | 15／1／0（同） | ⛔ 0 与读乙之 4／3／8 并列为「同一物之两读」 |
| 读乙 | 15 | 10 | 5 | 0 | 4／3／8 | ⛔ 0 与读甲之 15／1／0 互替 |
| 读丙 | 9 | 6 | 3 | 0 | —（前两读未覆盖） | ⛔ 0 与读甲／读乙合并为单一「锚链健康度」 |

> 📌 **判读纪律（FTFB 之内核）**：**计数口径差 ≠ 事实矛盾 ≠ 阈值调整**。三读之对象集**互有差**（交集仅 2 件），故其计数**不构成对同一物之竞争性测量**；**⛔ 0 以新读替换旧读·⛔ 0 以读数不合预期为改判之理由·⛔ 0 借「口径」之名行改数之实**。

### §3-3 本棒第三读之定位（**⛔ 0 替代前两读**）

📌 本棒之读数系**「现态登记」**，**非**「替代性复算」：① 域不同（前两读之域**未载明**；本棒域＝repo→sub→nula→sub\_archive·**明示**）；② 仪器不同（前两读各自之仪器**未载明**；本棒仪器＝`Get-FileHash`·**明示**）；③ 时点不同（10-19 → **10-20 14:07–14:28**）。
⇒ **⛔ 0 主张本读为「更正确」之读**；本读之价值在于**把「域·仪器·时点」三要素显式化**，使后续引用**可复核、可复现、可追责**。

---

## §4 修复径之建议面（**⛔ 0 代修·⛔ 0 闭 `KD-H2`**）

### §4-1 候选径

| 候选 | 内容 | 成本面 | 本棒之处置与理由 |
|---|---|---|---|
| **甲**（已交付） | **本件**——锚链勘误登记件（沿革＋断链＋口径差＋修复径建议） | 低–中（单件·0 实验·0 联网·0 归档区写动） | ✅ **本棒已交付**；体例复用先例二 |
| **乙** | 先立「**锚域口径固化件**」（`C2`）——两集合并列＋「计数口径差 ≠ 事实矛盾」纪律 | 最低（单件·0 测量） | 📌 **仍为不可省之第一径**——本件因 `C2` 未裁而**只能并列登记**；**若 PI 择定锚域，本件之读数方可归位**（**本件⛔ 0 闭此面**） |
| **丙** | 代修 `I2`／`I3` 之 `ARCHIVE_BASE` 硬编码绝对路径（换区 fallback・或纳入 sub 区） | 中 | 🔴 **⛔ 0 派**：① 脚本面属他棒权限；② **仓外归档区之写／动须逐单 PI 令**；③ R5（frozen 只追加）⇒ **本棒⛔ 0 代修**（仅登记于 §2-5 A-1） |
| **丁** | 派 `verifier` 作「**统一仪器·统一锚域**」之全量复算 | 中（一次全量哈希复算） | 📌 **本棒实测已提供「可复算之域与仪器之明示样本」**；**丁不能替代乙**（域未定义则单读无意义） |
| **戊**（**本棒新增建议**） | 立「**锚表 `path` 字段失效**」专项登记（13 条登记路径之仓内 0 命中＋归档区落位映射规则＋`I1` 之 `path` 字段自 2026-10-20 起**不可作仓内定位依据**） | 低（单件·0 测量·⛔ 0 改锚表一字） | 📌 **建议**：此面若不登记，则后续凡以锚表 `path` 定位者**必致 0 命中**（本棒已实测 13/13 0 命中）⇒ 该面乃**引用面之失效公告**，与 `KD-H2` 之「漂移／断链」**分属两事** |
| **己**（**本棒新增建议**） | 立「**冻结仪器之今日可用性**」登记（`I2`／`I3` 按自身口径复刻＝**OK 8／FAIL 8**·`0-touch declaration=FAIL`；归档侧异仪器 `I12` 无该常量） | 低（单件·0 测量·⛔ 0 执行脚本） | 📌 **建议**：凡引用「16/16 PASS」者**须先声明仪器与域**（本棒已证：按仪器自身口径今日为 8/16） |
| **庚** | **闭 `KD-H2`** | — | 🔴 **⛔ 0 闭**——**闭之判定权属 PI／verdict-keeper**；本件仅登记**待裁面**（沿革未登记者 4 锚·域未裁·路径失效面未登记） |

### §4-2 候 PI 裁之最小问题

1. **锚域之最终口径**：读甲 16 锚 ／ 读乙 15 条 ／ 两者并列＋读丙 9 条（覆盖面扩展）——择其一或并列？
2. **是否立「戊」**（锚表 `path` 字段失效之专项登记）？
3. **是否立「己」**（冻结仪器今日可用性之登记；及「引用 16/16 PASS 须先声明仪器与域」之纪律）？
4. **`P_A_HARNESS` 第四层漂移**（`ce64b9b97489`·10-18 13:20:34）**在册登记件之缺位**——是否追认其登记面？（**涉运行语义之等价性判断·本棒⛔ 0 判·⛔ 0 触其字节**）
5. **`KT_B1_ATTACK_BANK`／`KT_B1_HARNESS` 之漂移**（仓外实件·哈希已变·本棒检索未见在册 reconcile 载体）——是否立登记？
6. **BOSS-B 族三件同刻同向增量**（09-10 10:04:29）——**成因面**是否另派核？（本棒⛔ 0 断言成因）
7. **是否派「丁」**（统一仪器·统一锚域之全量复算）？若派，须在**乙之后**（否则仍为「换一读法重测」之嫌）。

### §4-3 本件之边界声明

- **构造面 vs 真实面**：本件射程 ＝ **本棒四区查找域 × 44 行实体 × 观测时点 2026-10-20 14:07–14:28**；⛔ **0 外推**为「全仓一切锚面皆已核」。
- **本件⛔ 0 触**：仓外归档区**写**面（只读）、`key`/`.env`、PAT、联网（含写向）、实验、LLM、既有件之一字。
- **本件⛔ 0 判**：`KD-H2` 之闭与不闭、漂移之成因、注册值之重锚与否、锚域之最终择定——**皆候 PI／verdict-keeper**。
- **本件⛔ 0 改判**对照版 `I4` 与普查件 `I5` 之在册读数——**两者与本棒之差皆按「域／时点差」登记**，不作成因判定。

---

## §5 诚实边界（读数分级·未覆盖面·⛔ 0 以「未查」充「无缺陷」）

| 级别 | 面 | 说明 |
|---|---|---|
| **本棒自测**（可复核） | 读甲 16 锚 ＋ 读乙 19 实体 ＋ 读丙 9 实体＝ **44 行**之 SHA-12／字节／mtime／落位；`ARCHIVE_BASE` 之 `Test-Path`；仪器复刻（16 锚 × 2 仪器）；`G2`／`G3` 之三区 `Test-Path`；G3 归档侧 4 件逐件哈希；I1–I12 之指纹；本件自身之字节与编码 | 复算命令与域**皆在本件载明**，他人可同域复现 |
| **照录**（他件自报·本棒未复算） | 对照版 §5-2 之 **+9 行 C4 diff**（逐行「原文一字未删改」之断言）；普查件 §15-1 之 V1/V2 冻结产物链 5/5 MATCH；对照版 §6 之 G4–G8 | 📌 照录层·⛔ 0 充本棒自测 |
| **本棒实测但未复算** | `KT_B1_SPEC_V0.1.md` 三值并存之内容关系（`0410ca0fbdae`／`0397b757362f`／`4790680c80c1`） | 仅作**三值并存**之登记，⛔ 0 断其演进关系 |
| **未覆盖面**（如实登记） | ① **异名副本**：本棒之实体定位为**文件名级精确匹配**（+ 登记相对路径级），**异名副本 0 覆盖**；② **全库 SHA-256 反查**：⛔ 0 做（成本面无穷）；③ **锚件之内容语义**：⛔ 0 读以核语义（⛔ 0 触 `tools/llm_client.py` 等件之字节内容——**仅哈希**）；④ **远端 GitHub 面**：⛔ 0 联网；⑤ **会话存储面**：⛔ 0 读；⑥ **`.tmp` 拉回区之全量**：仅核 `KT_B1_SPEC_V0.1.md` 一件；⑦ **reconcile 检索**：**repo 域完成·sub 域中止**（本棒主动终止）⇒ sub 区或另有承载登记件者，**本棒⛔ 0 断言「无登记」** | |
| **⛔ 0 断言** | 「8 条 MISSING_FILE 皆真缺」／「X 锚无登记件」／「BOSS-B 三件系篡改」／「`P_A_HARNESS` 四层语义等价」／「锚链已断／未断」 | 全部**只登记为待裁面** |

---

## §6 指纹总表（本棒自测·2026-10-20 14:07–14:28）

| # | 件 | SHA-12 | 字节 |
|---|---|---|---:|
| 1 | `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | `03c6c01f3697` | 6,680 |
| 2 | `deposon_team/plugins/_verify_15frozen.py` | `efae9274962e` | 3,905 |
| 3 | `deposon_team/plugins/_verify_pg_v0.py` | `cdd3415ad993` | 3,978 |
| 4 | `results/_deposon_full_history_sub_2026_10_19.md` | `a572747a2001` | 45,958 |
| 5 | `results/_h5_session_census_2026_10_19_part2.md` | `105413bee0ba` | 451,607 |
| 6 | `results/_kd_h1_h7_disposition_draft_2026_10_20.md` | `42ea79ea3f06` | 72,915 |
| 7 | `verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json` | `da517c115f3c` | 5,049 |
| 8 | `results/_harness_anchor_reconcile_register_2026_10_16.md` | `4de10aad8f0b` | 26,023 |
| 9 | `results/_t5_anchor_drift_authorized_register_2026_10_15.md` | `1308662a369a` | 11,553 |
| 10 | `results/_ge01_5anchor_json_register_2026_10_14.md` | `65000a1ac5bc` | 31,882 |
| 11 | `results/_ge01_prereg_5anchor_v2_lock_register_2026_10_15.md` | `ed3b544d33a6` | 17,808 |
| 12 | `〔归档区〕/verify_archive_backup/_verify_15frozen.py` | `c196aa7709ef` | 3,883 |
| 13 | `〔归档区〕/verify_archive_backup/_verify_pg_v0.py` | `e004327ffb74` | 4,172 |
| 14 | `results/_commission_v04_ghost_reference_erratum_2026_10_18.md` | `482eca247fa7` | 37,518 |
| 15 | `results/_ge01_spec_anchor_erratum_2026_10_14.md` | `2eeb522748ca` | 18,129 |

> **本件自身**：落盘后**独立亲测回读**（`Get-FileHash` SHA-256 前 12 位／字节／`BOM=False`／`CR=0`·纯 LF／UTF-8 严格解码通过）之实测值载于**交付回执**——**自指指纹不可内嵌于本件**（内嵌即改其自身指纹·悖论）。

---

## §7 落款

- **棒别**：`evidence-auditor`（数据修订／资产处置）｜**隶属**：`deposon` 仓 `〔本地路径已脱敏〕`
- **授权面**：PI `v153-Q2` 采认之 `KD-H2` 处置面（**乙→甲之甲**）——**仅立「锚链勘误登记件」一件**
- **观测窗**：2026-10-20 14:07–14:28（UTC+8）｜**工具**：PowerShell 5.1 `Get-FileHash -Algorithm SHA256`（前 12 位）＋ `Test-Path` ＋ 文件名级递归穷举（`-Filter` 精确名）
- **体例**：复用先例二（幽灵引用勘误登记件／spec 锚勘正件）·**append-only·单立新件·⛔ 0 回改任何在册件一字**
- **开口态**：`KD-H2` 🔴 **仍开口**（沿革未登记者 4 锚·锚域未裁·路径失效面未登记·仪器可用性未登记）｜⛔ 本件 **0** 闭 · ⛔ **0** 落五终判 · ⛔ **0** 代 PI 裁
- **诚实交代**：本件之全部指纹**皆本棒自测**；凡标「照录」者**本棒未复算**；凡标「未见登记」者**⛔ 0 断言不存在**（检索面有限·见 §5）
