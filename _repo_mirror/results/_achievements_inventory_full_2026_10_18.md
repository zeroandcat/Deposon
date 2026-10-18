# V3–V4 全量成果清单 v3.0（五段链 ③段-②R2 · **整理后时点**）

> **版本**：v3.0（全量清单件 · **整理后**）｜**取代关系**：⛔ **0 取代 0 回改**任何既有件——本件系**另立新件**，与 v2.0 族（`results/_achievements_inventory_full_2026_10_09.md`，`dd3e9806a369`）**并存**，凡口径冲突以本件为准
> **体例**：**沿 v2.0 逐字承袭**（节序 · 字段 schema · 类别判据 · 排序口径 **0 创新**）；凡新增面一律以 **§11 append 节**承载并注明 🆕 **新增**
> **出件方**：**doc-writer（agent-0032834a3e04）**｜**实测时点**：**2026-10-18 01:05:00 (+08:00)**｜**件路径**：`results/_achievements_inventory_full_2026_10_18.md`
> **命名**：沿 parent 派工单给定路径逐字；**落前占位实测** `Test-Path` ＝ `False`、`results\*achievements_inventory_full*2026_10_18*` glob ＝ **0 命中**（唯一命中为 10-09 旧件，**异名**）
> **状态**：🟡 **本件 0 宣告任何闭/开/段之毕**（含 ③段之毕 · ①毕）｜⛔ **0 落五终判**（`pass`／`af`／`kd`／`fail`／`give-up` 均**非本件之权**；§11-KD 之「新出 KD 登记」系**缺陷登记**非**实验终判**）｜⛔ **0 代 PI 裁**
> **版式**：UTF-8 无 BOM · 纯 LF · 落盘后**独立亲测回读**＋字节级自核（SHA-12／bytes／BOM／CRLF／U+FFFD）

---

## §0 · 一句话结论

两区（`deposon-repo` ＋ `deposon-sub`）整理后实测共 **5,558 件、合计 249,823,914 bytes**（REPO **4,282 件 / 189,657,496 bytes**；SUB **1,276 件 / 60,166,418 bytes**；`os.walk` **遍历错误 0**）；**全件逐件展开**（含 `.tmp/` 面 **2,268 件**——**偏离 v2.0「`.tmp` 仅汇总」之惯例**，理由见 §2.2）；**今晚增量面**（mtime ≥ **2026-10-17 18:00:00**）**689 件**，逐件附 SHA-12；**整理映射面**（清走 **96** · 净转移 **141** · 回退 **25**）经本棒**盘上逐件复核**，结果见 §3。

📌 **计数为时点事实**：实测期间两区**无并发写入**（本棒实测：mtime 晚于整理登记件落盘时点之件 **0 件**）⇒ 本件计数以 **2026-10-18 01:05:00** 为准，**0 回溯校正**。

## §1 · 授权与底本

### §1.1 授权来源（逐条）

| # | 授权源 | 原文要点 | 本件之执行 |
| :-:|:--|:--|:--|
| 1 | **PI 段序令（2026-10-17 23:03:18.216）** | 「直接三段含整理文件夹且无需确认」 | 本棒 ＝ **立全清单**之棒；整理已由 ③段-R2 毕（§3 逐件复核）|
| 2 | **次序铁律**（2026-10-12 先例 · `dd3e9806a369` §1.1 第 3 行登记「先完整全量得整理文件夹再立全清单」） | 整理 → 再立全清单 | 本件严格后置于整理；⛔ 0 与整理并跑 |
| 3 | parent 派工单（自包含） | ①体例沿 v2.0 ②全量实测（`os.walk` ＋ 断言遍历错误 0）③今晚增量面专列 ④整理映射面并入注记 ⑤⛔ 触归档区／GLM ⑥⛔ 移动/删除/重命名 ⑦新出 KD 逐条登记（域 `KD-INV`） | 逐项落为 §2／§4／§7／§3／§10／§11-KD |

### §1.2 底本（**全部经本棒 `sha256` 逐件复核**；⛔ 0 目视沿用派工单转录值）

| 角色 | 相对路径 | SHA-12（实测） | bytes（实测） | mtime（实测） | 与派工单转录值 |
|:--|:--|:--|--:|:--|:--|
| **体例底本（v2.0）** | `results/_achievements_inventory_full_2026_10_09.md` | `dd3e9806a369` | 372,318 | 2026-10-12 03:20:49 | ✅ 逐字一致 |
| **整理映射底本** | `results/_stage3_r2_cleanup_register_2026_10_18.md` | `d6b1dc8f8a02` | 62,885 | 2026-10-18 00:58:56 | ✅ 逐字一致 |

## §2 · 惯例回查结果（回查证据在案，⛔ 0 按最窄义自拟）

### §2.1 两区范围与禁触区（**沿 v2.0 §2.1 逐字承袭**）

| 标签 | 绝对路径 | 本棒处置 |
|:--|:--|:--|
| MAIN | `D:\私人资料\deposon-repo` | ✅ 全量实测逐件（§4.1）|
| SUB | `D:\私人资料\deposon-sub` | ✅ 全量实测逐件（§4.2）|
| ARCHIVE | `D:\私人资料\_non_upload_local_archive` | ⛔ **本棒 0 读 0 写 0 列目录 0 入清单** ⇒ **未核得（禁触区）**，见 §9-N-1 |
| GLM | `D:\私人资料\GLM` | ⛔ **本棒 0 触**（派工单明列）|

### §2.2 「全件枚举逐件附 SHA-12」vs v2.0「`.tmp` 仅汇总」—— **已查惯例，本件按派工单明令取前者（偏离已登记）**

**回查证据**：v2.0（`dd3e9806a369`）§2.3 逐字——「`.tmp/` 面 **441 件 / 11,375,518 bytes 不逐件展开**，仅于 §4.1 出汇总表」；同节复述 v1.0 族 3dir 件 §0.3 之「transient/internal-only files appear in the count roll-up only」。

**本件处置（⚠ 偏离，如实登记）**：parent 派工单明令「两区**全件枚举**…**逐件**：路径／bytes／mtime／SHA-12」⇒ 本件对 `.tmp/` 面 **2,268 件亦逐件展开**，并**同时**保留分目录汇总（§4.1/§4.2 逐目录分布表）。

⚠ **偏离登记（§11-A-2 登记）**：此系**对 v2.0 惯例之主动偏离**，权源为**派工单明令**而非本棒自拟；⛔ **0 改写 v2.0 一字**（v2.0 之惯例面原样存续）。

### §2.3 命名惯例与落前占位（**沿 v2.0 §2.4 承袭 ＋ 本棒实测**）

| 项 | 实测 |
|:--|:--|
| 目标路径 | `results\_achievements_inventory_full_2026_10_18.md` |
| `Test-Path` | **`False`** ✅ |
| `glob results\*achievements_inventory_full*` | **1** 命中＝`_achievements_inventory_full_2026_10_09.md`（**异名**，⛔ 0 覆盖）|
| 命名惯例 | 沿 `results/` 成果族**一律带日期戳**之既有惯例（v2.0 §2.4 逐字）|

### §2.4 类别判据（**沿 v2.0 §4 逐字承袭**）

**判据**：`成果面`（`results/`、`letters/`、`docs/`、`paper/`、`deposon_team/`、`reviews/`、`scripts/`、`tests/`、`tools/`、`verifier/`、`corpus/`、`attacks/`、`.trae/`、`.mavis/`、`pi_rulings/`、`_remote_pullback_2026_10_17/`、`.vscode/`、根散件、`tmp_movedout_*`）／`噪声面`（`.tmp/`，依 §2.3 **本件仍逐件展开**）

**排序**：区 → 目录 → 相对路径（小写稳定序）。**SHA-12** ＝ SHA-256 前 12 位，**全部由本棒实测**。

⚠ **判据之扩充登记**：整理后新增顶层面 `pi_rulings/`、`_remote_pullback_2026_10_17/`、`.vscode/` 三者**不在 v2.0 之枚举内** ⇒ 本件按 v2.0 之**兜底原则**（「`.tmp/` 之外皆实质成果面」）判为**成果面**，并于 §11-A-1 登记；⛔ 0 断言其归属权威。

### §2.5 余歧义汇总（0 沉默略过）

| # | 歧义 | 已查惯例 | 余留 | 本件处置 |
|:-:|:--|:--|:--|:--|
| A-1 | 「今晚」之时间窗切点 | 派工单仅给「2026-10-17 晚至 18 凌晨」之**定性**描述 | **切点未定** | 取 **mtime ≥ 2026-10-17 18:00:00** 之显式工作切面，**同时**并列 10-17 全日读数（§7.1），⛔ 0 断言其即 PI 之意 → **KD-INV-04** |
| A-2 | 「B-11 回收件」之指代 | 派工单未给文件名 | **未决** | 两区按 `b11` 关键字**唯一命中** 1 件 ⇒ 采认之并登记为**消歧未决** → **KD-INV-03** |
| A-3 | 「生效落账/设计/验真/登记件」之四型边界 | 派工单未给判据词表 | **未决** | 本件⛔ **0 按语义分类**，改以**目录面 ＋ 件名逐字**双列（§7.2），四型归属**留 PI 判** |
| A-4 | 清走 96 件之「可恢复」性 | 登记件 §3-3 载 `$I`/`$R` 验道 96/96 | **本棒未核得** | 本棒⛔ **0 触回收站** ⇒ 沿用登记件验道登记，自身仅核得「已离原位」→ **KD-INV-05** |

## §3 · 整理映射面（③段-R2 清走／转移／回退 · **本棒盘上逐件复核**）

### §3.1 整理登记件之终态账 vs 本棒实测

| 面 | 整理后（登记件 §2 · 动作完成时点） | 本棒实测（2026-10-18 01:05:00） | 件数差 | 字节差 |
|:--|--:|--:|--:|--:|
| REPO 件数 | 4,280 | **4,282** | **+2**（登记件＋其生成脚本 2 件，登记件 §2 末已自报）| —— |
| REPO bytes | 189,574,034 | **189,657,496** | —— | **+83,462**（构成见 §8 **D-1**）|
| SUB 件数 | 1,276 | **1,276** | **0** ✅ | —— |
| SUB bytes | 60,166,418 | **60,166,418** | —— | **0** ✅ **逐字节吻合** |
| 合计 件数 | 5,556 | **5,558** | +2 | —— |
| 合计 bytes | 249,740,452 | **249,823,914** | —— | +83,462 |
| 件数比 repo:sub | 3.354:1（登记件） | **3.356:1** | —— | 登记件自报落盘后 **3.356:1** ✅ **吻合** |

### §3.2 清走 **96** 件（判据 **89** ＋ 本棒自清 **7**）—— 🟢 **已入回收站 · 可恢复**（沿登记件验道登记）

| 项 | 本棒实测 |
|:--|:--|
| 判据四型清走 | **89 件**（REPO 35／SUB 54，拆分与登记件 §3 之「repo 35 件／sub 54 件」**一致**）|
| 本棒自清（E 同判据） | **7 件** |
| **已离原位（两区 0 命中）** | 判据 **89 / 89** ✅｜自清 **7 / 7** ✅ |
| 仍在原位者 | **0** ✅ |
| 通道 | 回收站 `$I`/`$R` 成对，**验道 96/96**（**登记件 §3-3 登记值，本棒沿用**）|
| ⛔ 本棒 | **0 触回收站**、⛔ 0 恢复、⛔ 0 永久删 ⇒ 「可恢复」之**实存性本棒未核得**（§9-N-2）|

**逐件（判据 89 件）**

| # | 型 | 路径（相对两区根） | 区 | bytes | SHA-12（本棒复核） | 本棒复核 |
| --: | :-: | :-- | :-: | --: | :-- | :-: |
| 1 | A | `.tmp/_m5_k5_net.err` | REPO | 0 | `e3b0c44298fc` | ✅ 已离原位 |
| 2 | A | `.tmp/_m5_k5_scan.err` | REPO | 0 | `e3b0c44298fc` | ✅ 已离原位 |
| 3 | A | `.tmp/_recheck_r1_runA.log` | REPO | 2,634 | `68c85cf076d1` | ✅ 已离原位 |
| 4 | A | `.tmp/_recheck_r1_runB.log` | REPO | 2,634 | `68c85cf076d1` | ✅ 已离原位 |
| 5 | A | `.tmp/_recheck_r1_runC.log` | REPO | 2,568 | `b15384cff9f0` | ✅ 已离原位 |
| 6 | A | `.tmp/_recheck_r1_runD.log` | REPO | 2,568 | `b15384cff9f0` | ✅ 已离原位 |
| 7 | A | `.tmp/_rj5_convention_check_2026_09_27.out.json` | REPO | 8,983 | `c88e4ba1a4ce` | ✅ 已离原位 |
| 8 | A | `.tmp/_t1_gap_implA_2026_10_01.py` | REPO | 4,468 | `c5d1dc7badcd` | ✅ 已离原位 |
| 9 | A | `.tmp/_t1_gap_implB_2026_10_01.ps1` | REPO | 5,735 | `19aebfd44310` | ✅ 已离原位 |
| 10 | A | `.tmp/_v5_item21_patched_b1_semA_none_default.py` | REPO | 16,768 | `ceb33de660fd` | ✅ 已离原位 |
| 11 | A | `.tmp/_v5_item21_patched_b1_semB_none_skip.py` | REPO | 16,829 | `be0208abaffa` | ✅ 已离原位 |
| 12 | A | `.tmp/_v5_item21_patched_b2_semA_none_default.py` | REPO | 16,036 | `801ee31e8bdc` | ✅ 已离原位 |
| 13 | A | `.tmp/_v5_item21_patched_b2_semB_none_skip.py` | REPO | 16,097 | `8293535673dc` | ✅ 已离原位 |
| 14 | A | `.tmp/_v5_item21_patched_b3_semA_none_default.py` | REPO | 15,778 | `9d8a4a875b62` | ✅ 已离原位 |
| 15 | A | `.tmp/_v5_item21_patched_b3_semB_none_skip.py` | REPO | 15,839 | `8df8e94724ff` | ✅ 已离原位 |
| 16 | A | `.tmp/ref_exp_harness_OLD_2026_10_15.py` | REPO | 13,342 | `7957bac14455` | ✅ 已离原位 |
| 17 | A | `.tmp/t3_harness_diff_2026_10_15.diff` | REPO | 3,463 | `0f8532aefdff` | ✅ 已离原位 |
| 18 | A | `.tmp/t5_harness_diff_2026_10_15.diff` | REPO | 4,043 | `6f1e9689201b` | ✅ 已离原位 |
| 19 | A | `.tmp/t5_prefix_T1T4_digest_2026_10_15.json` | REPO | 400 | `9eb43782b73c` | ✅ 已离原位 |
| 20 | A | `corpus/v20_caption_surface/_adendum_I_po_captions_closure_20260917_132049.json` | REPO | 4,429 | `18165008bef6` | ✅ 已离原位 |
| 21 | A | `letters/LETTER_TO_GEMINI4_GE01_THEORY_INPUTS_2026_10_15.md` | REPO | 8,361 | `70fe266e87d6` | ✅ 已离原位 |
| 22 | A | `results/_d9_e2e_rerun_backup_2026_10_13/_s4_heldout_sampling_seedthird_items_2026_10_11.json` | REPO | 43,130 | `5777a07c608a` | ✅ 已离原位 |
| 23 | A | `results/_d9_e2e_rerun_backup_2026_10_13/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | REPO | 22,646 | `784f042bf93d` | ✅ 已离原位 |
| 24 | A | `results/_d9_e2e_rerun_backup_2026_10_13/_s5doubleprime_five_lines_readings_2026_10_11.json` | REPO | 16,099 | `839fb5452578` | ✅ 已离原位 |
| 25 | A | `results/_d9_e2e_rerun_backup_2026_10_13/_stage3_trigger_readings_items_2026_10_11.json` | REPO | 21,049 | `079108c62a82` | ✅ 已离原位 |
| 26 | A | `results/_d9_e2e_rerun_backup_2026_10_13/_v3_recheck_05_result_2026_09_28.json` | REPO | 450,751 | `81460acbb4f9` | ✅ 已离原位 |
| 27 | A | `results/_family_e_q_type_refresh_exec_2026_10_14.md` | REPO | 28,259 | `71f5a0769dab` | ✅ 已离原位 |
| 28 | A | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_criterion_application_scope_prereg_2026_10_01.md` | REPO | 50,322 | `c4e3338619c6` | ✅ 已离原位 |
| 29 | A | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_day_close_register_2026_10_01.md` | REPO | 33,115 | `6dbac1d1bcd6` | ✅ 已离原位 |
| 30 | A | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_n7_mutual_exclusion_determination_2026_10_01.md` | REPO | 40,169 | `b6bdf807cb27` | ✅ 已离原位 |
| 31 | A | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_proxy_signoff_execution_register_2026_10_01.md` | REPO | 20,766 | `b6e5e15b70e5` | ✅ 已离原位 |
| 32 | A | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_s3_closeout_convergence_2026_10_01.md` | REPO | 42,443 | `bb62b5c174da` | ✅ 已离原位 |
| 33 | A | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_s3_kv3s_3_verdict_2026_10_01.md` | REPO | 35,037 | `e394bb6b5ddf` | ✅ 已离原位 |
| 34 | A | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_s3_missing_field_backfill_rule_effective_2026_10_01.md` | REPO | 52,469 | `1450057b0819` | ✅ 已离原位 |
| 35 | A | `results/_p4_pulled_back_conservation.py_2026_10_12` | REPO | 22,105 | `4bdec2683f06` | ✅ 已离原位 |
| 36 | A | `sub/.trae/audit/compile_evidence/v2pre_h1h3_20260909/COMPILE_SUMMARY.txt` | SUB | 1,693 | `1bad41b3929f` | ✅ 已离原位 |
| 37 | A | `sub/results/Deposon_评估汇总_v1_3_0.json` | SUB | 2,811 | `2f02f50c164b` | ✅ 已离原位 |
| 38 | A | `sub/results/_archive_2026_09_20/LETTER_TO_TRAE_FIX_SELFCHECK_2026_09_15.md` | SUB | 7,855 | `c0d629df69d8` | ✅ 已离原位 |
| 39 | A | `sub/results/_archive_2026_09_20/TRAE_CODE_FIX_LIST_2026_09_18.md` | SUB | 9,343 | `ace3c6b390cb` | ✅ 已离原位 |
| 40 | A | `sub/results/_archive_2026_09_20/TRAE_DAILY_AUDIT_LETTER_2026_09_18.md` | SUB | 11,575 | `0011b7924dfb` | ✅ 已离原位 |
| 41 | A | `sub/results/_archive_2026_09_20/TRAE_FIX_RECEIPT_2026_09_18.md` | SUB | 4,784 | `2e6a31af5e4b` | ✅ 已离原位 |
| 42 | A | `sub/results/_archive_2026_09_20/_openrouter_emb_runner.bak.note` | SUB | 5 | `f01a374e9c81` | ✅ 已离原位 |
| 43 | A | `sub/results/_archive_2026_09_20/_tmp_probe_archive` | SUB | 1,270 | `a6689025804c` | ✅ 已离原位 |
| 44 | A | `sub/results/_archive_2026_09_20/fiction_that_feeds_back.tex` | SUB | 93,324 | `d060f75dbe9f` | ✅ 已离原位 |
| 45 | A | `sub/results/_archive_2026_09_20/review_content_A1_dsv4pro.md` | SUB | 20,082 | `5198a7059c06` | ✅ 已离原位 |
| 46 | A | `sub/results/_archive_2026_09_20/review_tech_B1_grok46.md` | SUB | 18,923 | `09784ff172b3` | ✅ 已离原位 |
| 47 | A | `sub/results/_archive_2026_09_20/review_tech_B2_qwen3max.md` | SUB | 8,098 | `8d00c6d4a242` | ✅ 已离原位 |
| 48 | A | `sub/results/_archive_2026_09_21/Deposon_评估汇总_v1_3_0.json` | SUB | 2,811 | `2f02f50c164b` | ✅ 已离原位 |
| 49 | A | `sub/results/_p_i_real_labels_2026_09_16/p_i_real_labels_results_2026_09_16.json` | SUB | 1,043 | `e934819ee9ed` | ✅ 已离原位 |
| 50 | A | `sub/results/_p_l_p_c_finite_size_scaling_2026_09_16/p_l_p_c_finite_size_scaling_results_2026_09_16.json` | SUB | 9,076 | `664e7cc05aec` | ✅ 已离原位 |
| 51 | A | `sub/results/_p_l_real_data_collapse_2026_09_16/p_l_real_data_collapse_results_v2_2026_09_16.json` | SUB | 3,761 | `afe975606d40` | ✅ 已离原位 |
| 52 | A | `sub/results/_p_m_attack_surface_cost_2026_09_16/p_m_attack_surface_cost_results_2026_09_16.json` | SUB | 5,266 | `fbcb60cf5102` | ✅ 已离原位 |
| 53 | A | `sub/results/_p_m_real_separation_2026_09_16/p_m_real_separation_results_2026_09_16.json` | SUB | 2,042 | `a4b12d1cfedc` | ✅ 已离原位 |
| 54 | A | `sub/results/_p_n_curvature_potential_coupling_2026_09_16/p_n_curvature_potential_coupling_results_2026_09_16.json` | SUB | 4,276 | `088f28524a1d` | ✅ 已离原位 |
| 55 | A | `sub/results/_p_o_stranger_verification_2026_09_16/p_o_stranger_verification_results_2026_09_16.json` | SUB | 5,916 | `1e4c065da058` | ✅ 已离原位 |
| 56 | A | `sub/results/_tra_v0_2026_09_10.py` | SUB | 12,125 | `d80a8f75a122` | ✅ 已离原位 |
| 57 | A | `sub/results/_v2_setup.py._moved_20260924_1830.py` | SUB | 3,483 | `73f2b8712a90` | ✅ 已离原位 |
| 58 | A | `sub/results/_v2_show_summary.py._moved_20260924_1830.py` | SUB | 1,200 | `0012b38ce438` | ✅ 已离原位 |
| 59 | A | `sub/results/_v2_smoketest.py._moved_20260924_1830.py` | SUB | 2,040 | `0b6c22c8f379` | ✅ 已离原位 |
| 60 | A | `sub/results/_v2_stage1_60cells.py._moved_20260924_1830.py` | SUB | 31,556 | `8c7bd12c3a8c` | ✅ 已离原位 |
| 61 | A | `sub/results/_v2_stage2_f2_drift.py._moved_20260924_1830.py` | SUB | 10,798 | `7e9b2fc57d80` | ✅ 已离原位 |
| 62 | A | `sub/results/_v2_stage3_f3_strip.py._moved_20260924_1830.py` | SUB | 11,803 | `ce4362e325ca` | ✅ 已离原位 |
| 63 | A | `sub/results/_v2_stage4_f4_pdv2.py._moved_20260924_1830.py` | SUB | 10,355 | `b84f5aab6faf` | ✅ 已离原位 |
| 64 | A | `sub/results/_v2_stage5_f5_dpath.py._moved_20260924_1830.py` | SUB | 6,480 | `e8871b829d89` | ✅ 已离原位 |
| 65 | A | `sub/results/_v2_verify_outputs.py._moved_20260924_1830.py` | SUB | 2,656 | `eb0107dd79b5` | ✅ 已离原位 |
| 66 | A | `sub/results/_v3x_18frozen_remeasure_2026_09_16/v3x_18frozen_remeasure_results_2026_09_16.json` | SUB | 4,202 | `928794710241` | ✅ 已离原位 |
| 67 | A | `sub/results/_v3x_conservation_anchor_2026_09_17.txt` | SUB | 940 | `f331a9c2bd22` | ✅ 已离原位 |
| 68 | A | `sub/results/_v3x_d0_5_aggregation_2026_09_17.md` | SUB | 12,010 | `ddf0d1aa96d2` | ✅ 已离原位 |
| 69 | A | `sub/results/_v3x_d0_5_experiment_invitation_2026_09_17.md` | SUB | 7,617 | `d8f2b99aa527` | ✅ 已离原位 |
| 70 | A | `sub/results/_v3x_d0_5_proposal_coze_2026_09_17.md` | SUB | 13,200 | `759c25b21ed4` | ✅ 已离原位 |
| 71 | A | `sub/results/_v3x_d0_5_proposal_trae_2026_09_17.md` | SUB | 13,254 | `b1c227d54a82` | ✅ 已离原位 |
| 72 | A | `sub/results/_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json` | SUB | 17,053 | `f39412103366` | ✅ 已离原位 |
| 73 | A | `sub/results/_v3x_p_k_verify_2026_09_16/v3x_p_k_verify_results_2026_09_16.json` | SUB | 2,059 | `59c2113b7c71` | ✅ 已离原位 |
| 74 | A | `sub/results/_v3x_p_l_v3_external_spec_2026_09_17.md` | SUB | 5,769 | `6a5b6eb635f0` | ✅ 已离原位 |
| 75 | A | `sub/results/_v3x_p_l_v3_mistral_large_2512_20260917_115049.json` | SUB | 16,835 | `523b5941c30c` | ✅ 已离原位 |
| 76 | A | `sub/results/_v3x_p_l_v3_summary_mistral_large_2512_20260917_115049.md` | SUB | 9,570 | `183205baa9ac` | ✅ 已离原位 |
| 77 | A | `sub/results/boss_pc_2_a2_fitting_2026_09_15.json` | SUB | 1,024 | `5a880678c386` | ✅ 已离原位 |
| 78 | A | `sub/results/boss_pc_3_a3_clipping_2026_09_15.json` | SUB | 1,265 | `d74d6b39d1b0` | ✅ 已离原位 |
| 79 | A | `sub/results/boss_pe_1_real_2d_ising_2026_09_15.json` | SUB | 2,460 | `43d9ce160fc8` | ✅ 已离原位 |
| 80 | A | `sub/results/boss_pe_2_real_transverse_ising_2026_09_15.json` | SUB | 3,553 | `8933d61b180a` | ✅ 已离原位 |
| 81 | A | `sub/results/boss_pe_3_real_reservoir_2026_09_15.json` | SUB | 2,364 | `94b5398be76c` | ✅ 已离原位 |
| 82 | A | `sub/results/deposon_dpath_cross_modal_runner_2026_09_10.py` | SUB | 27,930 | `fb20a6ba5ec6` | ✅ 已离原位 |
| 83 | A | `sub/results/deposon_feshbach_rag_30cells_2026_09_10.py` | SUB | 14,343 | `a072e4184e83` | ✅ 已离原位 |
| 84 | A | `sub/results/deposon_v1_implementation_calculator_2026_09_10.py` | SUB | 10,751 | `121f104012f4` | ✅ 已离原位 |
| 85 | A | `sub/results/deposon_volcengine_glm_latest_5cells_2026_09_10.py` | SUB | 8,112 | `a3ca05aec6fb` | ✅ 已离原位 |
| 86 | A | `sub/results/deposon_volcengine_worker_b_2026_09_10.py` | SUB | 13,232 | `401dfd3c27f3` | ✅ 已离原位 |
| 87 | A | `sub/results/deposon_volcengine_worker_c_2026_09_10.py` | SUB | 11,692 | `b5eeef1e9bd7` | ✅ 已离原位 |
| 88 | A | `sub/tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/mindmap_corpus_v20.py.orig_7d8d6a30dd8c.bak` | SUB | 23,893 | `7d8d6a30dd8c` | ✅ 已离原位 |
| 89 | A | `sub/tmp_movedout_2026_10_01/process_scripts/volcengine_补测_worker_A_2026_09_10.py` | SUB | 16,252 | `20b8a2f54ad9` | ✅ 已离原位 |

**逐件（自清 7 件）**

| # | 路径（相对两区根） | bytes | 本棒复核 |
| --: | :-- | --: | :-: |
| 1 | `_r2_tool_01_inventory.json` | （已离原位）| ✅ 两区 0 命中 |
| 2 | `_r2_tool_04_classes.json` | （已离原位）| ✅ 两区 0 命中 |
| 3 | `_r2_tool_04b_channels.json` | （已离原位）| ✅ 两区 0 命中 |
| 4 | `_r2_tool_07_xferpool.json` | （已离原位）| ✅ 两区 0 命中 |
| 5 | `_r2_tool_10_plan2.json` | （已离原位）| ✅ 两区 0 命中 |
| 6 | `_r2_tool_11_channels.json` | （已离原位）| ✅ 两区 0 命中 |
| 7 | `_r2_tool_12_plan3.json` | （已离原位）| ✅ 两区 0 命中 |

### §3.3 净转移 **141** 件（repo→sub · 逐件 SHA 复算 ＋ 盘上在位复核）

| 项 | 本棒实测 |
|:--|:--|
| 净转移件数 | **141**（与登记件 §4-1 行数**一致**）|
| **新路径在 SUB 且 SHA-12＋bytes 双一致** | **141 / 141** ✅ |
| **旧路径仍在 REPO** | **0** ✅ |
| 方向 | repo→sub（sub→repo **0** 件，沿登记件 §4 之射程）|
| 目标路径规则 | 保持相对结构 `deposon-sub/<原相对路径>` |

**逐件（旧路径 → 新路径 · 本棒复核）**

| # | 旧路径（repo 相对） | 新路径（sub 相对） | bytes | SHA-12 | 本棒复核 |
| --: | :-- | :-- | --: | :-- | :-: |
| 1 | `docs/ADVISOR_BRIEFING_2026-08-30.md` | `docs/ADVISOR_BRIEFING_2026-08-30.md` | 5,890 | `40278bc425e6` | ✅ 新在位·旧已离位 |
| 2 | `docs/ARCH_AUDIT_v2.md` | `docs/ARCH_AUDIT_v2.md` | 14,698 | `5bee4c6cf47c` | ✅ 新在位·旧已离位 |
| 3 | `docs/DATASET_HEALTH_v2.md` | `docs/DATASET_HEALTH_v2.md` | 4,892 | `c87a0c1f5af6` | ✅ 新在位·旧已离位 |
| 4 | `docs/Deposon_Requirements_v1.md` | `docs/Deposon_Requirements_v1.md` | 13,914 | `ee33f3f22e1b` | ✅ 新在位·旧已离位 |
| 5 | `docs/Deposon_v1_3_验证报告.md` | `docs/Deposon_v1_3_验证报告.md` | 8,003 | `dc5be727f920` | ✅ 新在位·旧已离位 |
| 6 | `docs/Deposon_v1_4_验证报告.md` | `docs/Deposon_v1_4_验证报告.md` | 4,254 | `3bcccf03f7ca` | ✅ 新在位·旧已离位 |
| 7 | `docs/FIGURES_v2.md` | `docs/FIGURES_v2.md` | 5,851 | `1cd4a4cb0a76` | ✅ 新在位·旧已离位 |
| 8 | `docs/LESSONS_INDEX.md` | `docs/LESSONS_INDEX.md` | 4,682 | `7e3674a80cb7` | ✅ 新在位·旧已离位 |
| 9 | `docs/LESSONS_v19.md` | `docs/LESSONS_v19.md` | 5,290 | `dbbcf8e5e89d` | ✅ 新在位·旧已离位 |
| 10 | `docs/LESSONS_v20_deepprobe.md` | `docs/LESSONS_v20_deepprobe.md` | 8,409 | `5c898d4407ee` | ✅ 新在位·旧已离位 |
| 11 | `docs/MODEL_ARGUMENTATION_v2.md` | `docs/MODEL_ARGUMENTATION_v2.md` | 30,142 | `2c83c42804e4` | ✅ 新在位·旧已离位 |
| 12 | `docs/PROGRESS_REPORT_LAYMAN.md` | `docs/PROGRESS_REPORT_LAYMAN.md` | 8,472 | `25546ffdc56b` | ✅ 新在位·旧已离位 |
| 13 | `docs/Roadmap_v2X.md` | `docs/Roadmap_v2X.md` | 6,467 | `a6aaf3200611` | ✅ 新在位·旧已离位 |
| 14 | `docs/SALVAGE_v2.md` | `docs/SALVAGE_v2.md` | 7,312 | `f28a81d6302d` | ✅ 新在位·旧已离位 |
| 15 | `docs/SECURITY_AUDIT_v2.md` | `docs/SECURITY_AUDIT_v2.md` | 4,707 | `317fb508940a` | ✅ 新在位·旧已离位 |
| 16 | `docs/SPEC_GT2C.md` | `docs/SPEC_GT2C.md` | 3,172 | `29af533486b2` | ✅ 新在位·旧已离位 |
| 17 | `docs/SPEC_GT5C.md` | `docs/SPEC_GT5C.md` | 3,046 | `1e41b4334735` | ✅ 新在位·旧已离位 |
| 18 | `docs/SPEC_v1.5.md` | `docs/SPEC_v1.5.md` | 6,204 | `c165a86cf551` | ✅ 新在位·旧已离位 |
| 19 | `docs/THINKING_V3_GT_CONTRIB_2026.md` | `docs/THINKING_V3_GT_CONTRIB_2026.md` | 19,508 | `8c1d733f9182` | ✅ 新在位·旧已离位 |
| 20 | `docs/V3X/AGENT_TEAM_OPT_V2_2026_09_11.md` | `docs/V3X/AGENT_TEAM_OPT_V2_2026_09_11.md` | 11,835 | `bbd074b76526` | ✅ 新在位·旧已离位 |
| 21 | `docs/V3X/BOSS_B123_BUGFIX_2026_09_09.md` | `docs/V3X/BOSS_B123_BUGFIX_2026_09_09.md` | 5,615 | `9352a1675b10` | ✅ 新在位·旧已离位 |
| 22 | `docs/V3X/BOSS_F_GHOST_PATH_NOTE_2026_09_11.md` | `docs/V3X/BOSS_F_GHOST_PATH_NOTE_2026_09_11.md` | 4,840 | `354a1360234f` | ✅ 新在位·旧已离位 |
| 23 | `docs/V3X/BOSS_PE_3_RESERVOIR_VERIFY_REPORT_2026_09_15.md` | `docs/V3X/BOSS_PE_3_RESERVOIR_VERIFY_REPORT_2026_09_15.md` | 11,079 | `c28f7f0b530f` | ✅ 新在位·旧已离位 |
| 24 | `docs/V3X/BOSS_SELFTEST_PHASE_B_2026_09_09.md` | `docs/V3X/BOSS_SELFTEST_PHASE_B_2026_09_09.md` | 15,478 | `4485443757e7` | ✅ 新在位·旧已离位 |
| 25 | `docs/V3X/BOSS_URL_2026_09_11.md` | `docs/V3X/BOSS_URL_2026_09_11.md` | 7,135 | `1ba7419178a1` | ✅ 新在位·旧已离位 |
| 26 | `docs/V3X/BOSS_URL_DUE_DILIGENCE_2026_09_11.md` | `docs/V3X/BOSS_URL_DUE_DILIGENCE_2026_09_11.md` | 10,970 | `0fb588bb0c2e` | ✅ 新在位·旧已离位 |
| 27 | `docs/V3X/BPA_PILOT_2026_09_09_mavis.md` | `docs/V3X/BPA_PILOT_2026_09_09_mavis.md` | 6,864 | `d74e1534493e` | ✅ 新在位·旧已离位 |
| 28 | `docs/V3X/CANONICAL_5_UNVERIFIED_NOTE_2026_09_11.md` | `docs/V3X/CANONICAL_5_UNVERIFIED_NOTE_2026_09_11.md` | 6,804 | `b049140e130c` | ✅ 新在位·旧已离位 |
| 29 | `docs/V3X/CPATH_SIMULATION_REPORT_2026_09_10.md` | `docs/V3X/CPATH_SIMULATION_REPORT_2026_09_10.md` | 6,825 | `de772cd9e7ba` | ✅ 新在位·旧已离位 |
| 30 | `docs/V3X/D0_FREEZE_PREP_2026_09_09.md` | `docs/V3X/D0_FREEZE_PREP_2026_09_09.md` | 9,844 | `0d1e88c258aa` | ✅ 新在位·旧已离位 |
| 31 | `docs/V3X/D3_〔IM〕_MIDTERM_TEMPLATE.md` | `docs/V3X/D3_〔IM〕_MIDTERM_TEMPLATE.md` | 4,361 | `574d5a79e363` | ✅ 新在位·旧已离位 |
| 32 | `docs/V3X/D5_DECISIONS_LAND_REPORT_2026_09_15.md` | `docs/V3X/D5_DECISIONS_LAND_REPORT_2026_09_15.md` | 21,756 | `8ff1a7c5413f` | ✅ 新在位·旧已离位 |
| 33 | `docs/V3X/D7_GITHUB_PUSH_RECEIVE_2026_09_15_v2.md` | `docs/V3X/D7_GITHUB_PUSH_RECEIVE_2026_09_15_v2.md` | 5,930 | `2c4bb6078ee7` | ✅ 新在位·旧已离位 |
| 34 | `docs/V3X/D7_ONE_PAGE_SUMMARY_2026_09_11_v5.md` | `docs/V3X/D7_ONE_PAGE_SUMMARY_2026_09_11_v5.md` | 6,459 | `67063f9cb238` | ✅ 新在位·旧已离位 |
| 35 | `docs/V3X/D7_ONE_PAGE_SUMMARY_TEMPLATE.md` | `docs/V3X/D7_ONE_PAGE_SUMMARY_TEMPLATE.md` | 5,830 | `87563a63b854` | ✅ 新在位·旧已离位 |
| 36 | `docs/V3X/D7_POST_CLEANUP_PLAN_2026_09_18.json` | `docs/V3X/D7_POST_CLEANUP_PLAN_2026_09_18.json` | 20,271 | `0b8a1a357aae` | ✅ 新在位·旧已离位 |
| 37 | `docs/V3X/D7_POST_CLEANUP_REPORT_2026_09_16.json` | `docs/V3X/D7_POST_CLEANUP_REPORT_2026_09_16.json` | 1,248 | `40955bf2abc5` | ✅ 新在位·旧已离位 |
| 38 | `docs/V3X/D7_PRE_V3_POLISH_AND_TEAM_IMPROVEMENT_2026_09_16.md` | `docs/V3X/D7_PRE_V3_POLISH_AND_TEAM_IMPROVEMENT_2026_09_16.md` | 10,692 | `51869e3184f4` | ✅ 新在位·旧已离位 |
| 39 | `docs/V3X/D7_WANG_TEACHER_〔IM〕_PUSH_REQUIREMENTS_2026_09_18.md` | `docs/V3X/D7_WANG_TEACHER_〔IM〕_PUSH_REQUIREMENTS_2026_09_18.md` | 8,037 | `935cb6ee3566` | ✅ 新在位·旧已离位 |
| 40 | `docs/V3X/DEPOSON_EMBEDDING_6WAY_THEORY_V0_2026_09_10.md` | `docs/V3X/DEPOSON_EMBEDDING_6WAY_THEORY_V0_2026_09_10.md` | 22,442 | `ac8997b07731` | ✅ 新在位·旧已离位 |
| 41 | `docs/V3X/DEPOSON_EMBEDDING_6WAY_VERIFICATION_2026_09_10.md` | `docs/V3X/DEPOSON_EMBEDDING_6WAY_VERIFICATION_2026_09_10.md` | 17,803 | `240a7ae4bdfb` | ✅ 新在位·旧已离位 |
| 42 | `docs/V3X/DPATH_CROSS_MODAL_2026_09_10.md` | `docs/V3X/DPATH_CROSS_MODAL_2026_09_10.md` | 26,460 | `e4ee3999f7ce` | ✅ 新在位·旧已离位 |
| 43 | `docs/V3X/D_FIX2_METRIC_VERIFY_REPORT_2026_09_15.md` | `docs/V3X/D_FIX2_METRIC_VERIFY_REPORT_2026_09_15.md` | 7,352 | `0a63824f0805` | ✅ 新在位·旧已离位 |
| 44 | `docs/V3X/KT_A1_SPEC_V0.1.md` | `docs/V3X/KT_A1_SPEC_V0.1.md` | 29,570 | `78b71d404366` | ✅ 新在位·旧已离位 |
| 45 | `docs/V3X/KT_B1_SPEC_V0.1.md` | `docs/V3X/KT_B1_SPEC_V0.1.md` | 39,206 | `0397b757362f` | ✅ 新在位·旧已离位 |
| 46 | `docs/V3X/KT_C1_REPORT_PHASE_B_2026_09_09.md` | `docs/V3X/KT_C1_REPORT_PHASE_B_2026_09_09.md` | 8,753 | `825337b10a2d` | ✅ 新在位·旧已离位 |
| 47 | `docs/V3X/KT_C1_SPEC_V0.1.md` | `docs/V3X/KT_C1_SPEC_V0.1.md` | 31,241 | `59d8f56347d5` | ✅ 新在位·旧已离位 |
| 48 | `docs/V3X/KT_D0_EVIDENCE_CARD.md` | `docs/V3X/KT_D0_EVIDENCE_CARD.md` | 6,354 | `75b2f3b38c2a` | ✅ 新在位·旧已离位 |
| 49 | `docs/V3X/KT_D0_SPEC_V0.1.md` | `docs/V3X/KT_D0_SPEC_V0.1.md` | 20,927 | `cce8e9a1b00e` | ✅ 新在位·旧已离位 |
| 50 | `docs/V3X/PHASE_B_DELIVERY_2026_09_09.md` | `docs/V3X/PHASE_B_DELIVERY_2026_09_09.md` | 9,701 | `ba53d73e3937` | ✅ 新在位·旧已离位 |
| 51 | `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` | `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` | 10,351 | `bd1caab42b4c` | ✅ 新在位·旧已离位 |
| 52 | `docs/V3X/P_C_P_E_V0_1_VERIFICATION_2026_09_12.md` | `docs/V3X/P_C_P_E_V0_1_VERIFICATION_2026_09_12.md` | 3,899 | `ee043a13f801` | ✅ 新在位·旧已离位 |
| 53 | `docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md` | `docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md` | 6,301 | `d427b2f57c33` | ✅ 新在位·旧已离位 |
| 54 | `docs/V3X/P_C_V0_1_VERIFICATION_2026_09_12.md` | `docs/V3X/P_C_V0_1_VERIFICATION_2026_09_12.md` | 4,885 | `00c7b7ceccdc` | ✅ 新在位·旧已离位 |
| 55 | `docs/V3X/P_D_B3_MERKLE_22_CAPTION_VERIFICATION_2026_09_16.md` | `docs/V3X/P_D_B3_MERKLE_22_CAPTION_VERIFICATION_2026_09_16.md` | 10,979 | `7f1492fbe657` | ✅ 新在位·旧已离位 |
| 56 | `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC_CHANGELOG.md` | `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC_CHANGELOG.md` | 15,021 | `fc73cab85d8f` | ✅ 新在位·旧已离位 |
| 57 | `docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md` | `docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md` | 34,367 | `c13449101ab3` | ✅ 新在位·旧已离位 |
| 58 | `docs/V3X/P_D_FINGERPRINT_V0_SPEC.md` | `docs/V3X/P_D_FINGERPRINT_V0_SPEC.md` | 9,192 | `3b67461b05fe` | ✅ 新在位·旧已离位 |
| 59 | `docs/V3X/P_E_D1_D3_REPORT_2026_09_15.md` | `docs/V3X/P_E_D1_D3_REPORT_2026_09_15.md` | 13,109 | `900da300d11e` | ✅ 新在位·旧已离位 |
| 60 | `docs/V3X/P_F_D1_FULL_REPORT_2026_09_15.md` | `docs/V3X/P_F_D1_FULL_REPORT_2026_09_15.md` | 15,985 | `817efdc2f0ad` | ✅ 新在位·旧已离位 |
| 61 | `docs/V3X/P_F_D1_REPORT_2026_09_15.md` | `docs/V3X/P_F_D1_REPORT_2026_09_15.md` | 12,608 | `e47d0348922e` | ✅ 新在位·旧已离位 |
| 62 | `docs/V3X/P_F_IMPLEMENTATION_2026_09_11.md` | `docs/V3X/P_F_IMPLEMENTATION_2026_09_11.md` | 22,973 | `edd048eaa721` | ✅ 新在位·旧已离位 |
| 63 | `docs/V3X/P_F_RESEARCH_2026_09_09.md` | `docs/V3X/P_F_RESEARCH_2026_09_09.md` | 17,603 | `98085df7811a` | ✅ 新在位·旧已离位 |
| 64 | `docs/V3X/P_F_SPEC_V0.md` | `docs/V3X/P_F_SPEC_V0.md` | 19,804 | `de90faf362c5` | ✅ 新在位·旧已离位 |
| 65 | `docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md` | `docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md` | 6,375 | `b10fae0da66d` | ✅ 新在位·旧已离位 |
| 66 | `docs/V3X/P_F_V0_1_VERIFICATION_2026_09_12.md` | `docs/V3X/P_F_V0_1_VERIFICATION_2026_09_12.md` | 4,188 | `4d970e9c0aec` | ✅ 新在位·旧已离位 |
| 67 | `docs/V3X/P_G_V01_REPORT_2026_09_15.md` | `docs/V3X/P_G_V01_REPORT_2026_09_15.md` | 15,479 | `9a6b08d03e0c` | ✅ 新在位·旧已离位 |
| 68 | `docs/V3X/QUICK_KILL_6_DIRECTIONS.md` | `docs/V3X/QUICK_KILL_6_DIRECTIONS.md` | 15,085 | `a476f241edb2` | ✅ 新在位·旧已离位 |
| 69 | `docs/V3X/REVIEWER_A_STATIC_AUDIT_2026_09_15.md` | `docs/V3X/REVIEWER_A_STATIC_AUDIT_2026_09_15.md` | 34,647 | `575572872e9a` | ✅ 新在位·旧已离位 |
| 70 | `docs/V3X/REVIEWER_A_TRAE_FIX_AUDIT_2026_09_15.md` | `docs/V3X/REVIEWER_A_TRAE_FIX_AUDIT_2026_09_15.md` | 20,698 | `195373c094d6` | ✅ 新在位·旧已离位 |
| 71 | `docs/V3X/REVIEWER_A_TRAE_N123_AUDIT_2026_09_15.md` | `docs/V3X/REVIEWER_A_TRAE_N123_AUDIT_2026_09_15.md` | 17,151 | `33ee7266cf5b` | ✅ 新在位·旧已离位 |
| 72 | `docs/V3X/REVIEWER_B_AUDIT_PHASE_B_2026_09_09.md` | `docs/V3X/REVIEWER_B_AUDIT_PHASE_B_2026_09_09.md` | 14,835 | `5e99e79f2e11` | ✅ 新在位·旧已离位 |
| 73 | `docs/V3X/REVIEWER_B_TRAE_FIX_RERUN_2026_09_15.md` | `docs/V3X/REVIEWER_B_TRAE_FIX_RERUN_2026_09_15.md` | 16,278 | `f5ac9820310a` | ✅ 新在位·旧已离位 |
| 74 | `docs/V3X/REVIEWER_B_TRAE_N123_RERUN_2026_09_15.md` | `docs/V3X/REVIEWER_B_TRAE_N123_RERUN_2026_09_15.md` | 16,926 | `31c27c0117a6` | ✅ 新在位·旧已离位 |
| 75 | `docs/V3X/RISK3_V0_FIXES_2026_09_11.md` | `docs/V3X/RISK3_V0_FIXES_2026_09_11.md` | 13,271 | `c00d1c22e7ed` | ✅ 新在位·旧已离位 |
| 76 | `docs/V3X/SPEC_V0_1_BOSS_SELFTEST_2026_09_09.md` | `docs/V3X/SPEC_V0_1_BOSS_SELFTEST_2026_09_09.md` | 10,708 | `00e543564e3f` | ✅ 新在位·旧已离位 |
| 77 | `docs/V3X/TRAE_3RISK_FIX_REPORT_2026_09_16.md` | `docs/V3X/TRAE_3RISK_FIX_REPORT_2026_09_16.md` | 9,267 | `7478959cfc7d` | ✅ 新在位·旧已离位 |
| 78 | `docs/V3X/TRAE_PL_V2_EXPERIMENT_PROPOSAL_2026_09_17.md` | `docs/V3X/TRAE_PL_V2_EXPERIMENT_PROPOSAL_2026_09_17.md` | 8,849 | `4020b1809780` | ✅ 新在位·旧已离位 |
| 79 | `docs/V3X/TRAE_PROACTIVE_AUDIT_REPORT_2026_09_16.md` | `docs/V3X/TRAE_PROACTIVE_AUDIT_REPORT_2026_09_16.md` | 6,493 | `813b34dcac70` | ✅ 新在位·旧已离位 |
| 80 | `docs/V3X/TRAE_SELFCHECK_FIX_REPORT_2026_09_15.md` | `docs/V3X/TRAE_SELFCHECK_FIX_REPORT_2026_09_15.md` | 4,840 | `226f740aa120` | ✅ 新在位·旧已离位 |
| 81 | `docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md` | `docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md` | 8,526 | `4ffb21bb6bfa` | ✅ 新在位·旧已离位 |
| 82 | `docs/V3X/V3X_D6_PAPER_V2_2026_09_09_mavis.md` | `docs/V3X/V3X_D6_PAPER_V2_2026_09_09_mavis.md` | 24,778 | `4d06d34cb6fa` | ✅ 新在位·旧已离位 |
| 83 | `docs/V3X/V3X_D6_PAPER_zh.md` | `docs/V3X/V3X_D6_PAPER_zh.md` | 19,716 | `feae8af2fefe` | ✅ 新在位·旧已离位 |
| 84 | `docs/V3X/V3X_DAILY_KILL_V2_PLAN.md` | `docs/V3X/V3X_DAILY_KILL_V2_PLAN.md` | 15,327 | `37e97e1e7b7f` | ✅ 新在位·旧已离位 |
| 85 | `docs/V3X/V3X_FULL_EXPERIMENT_DESIGN_2026_09_16.md` | `docs/V3X/V3X_FULL_EXPERIMENT_DESIGN_2026_09_16.md` | 22,427 | `3d847f9f3151` | ✅ 新在位·旧已离位 |
| 86 | `docs/V3X/V3X_PROJECT_EVOLUTION_FOR_KIMI.md` | `docs/V3X/V3X_PROJECT_EVOLUTION_FOR_KIMI.md` | 12,908 | `4de2cbf57a49` | ✅ 新在位·旧已离位 |
| 87 | `docs/V3X/V42_V2_REMEDIATION_CLAUSE_2026_09_16.md` | `docs/V3X/V42_V2_REMEDIATION_CLAUSE_2026_09_16.md` | 4,775 | `e451a5a3d079` | ✅ 新在位·旧已离位 |
| 88 | `docs/V3X/V42_V2_VERIFIER_PERFORMANCE_REPORT_2026_09_16.md` | `docs/V3X/V42_V2_VERIFIER_PERFORMANCE_REPORT_2026_09_16.md` | 11,080 | `914053fc3e17` | ✅ 新在位·旧已离位 |
| 89 | `docs/V3X/V7_§3_P_C_P_E_GRAY_NOTE_2026_09_11.md` | `docs/V3X/V7_§3_P_C_P_E_GRAY_NOTE_2026_09_11.md` | 7,344 | `f80cc4e1fb7f` | ✅ 新在位·旧已离位 |
| 90 | `docs/V3X_COLLAB_DIRECTIONS.md` | `docs/V3X_COLLAB_DIRECTIONS.md` | 16,363 | `5a27c2350036` | ✅ 新在位·旧已离位 |
| 91 | `docs/reviews/review_gtformal_integration_v2X.md` | `docs/reviews/review_gtformal_integration_v2X.md` | 8,582 | `325c9d87787b` | ✅ 新在位·旧已离位 |
| 92 | `docs/reviews/review_salvage_integration_v2X.md` | `docs/reviews/review_salvage_integration_v2X.md` | 6,212 | `96ae50306f36` | ✅ 新在位·旧已离位 |
| 93 | `docs/reviews/review_sprint_v2X.md` | `docs/reviews/review_sprint_v2X.md` | 7,776 | `4356cd02562e` | ✅ 新在位·旧已离位 |
| 94 | `results/_batch12_deliberation_judgment_2026_10_14.md` | `results/_batch12_deliberation_judgment_2026_10_14.md` | 39,448 | `8218a8777192` | ✅ 新在位·旧已离位 |
| 95 | `results/_family_e_q_type_conflict_resolution_2026_10_14.md` | `results/_family_e_q_type_conflict_resolution_2026_10_14.md` | 19,640 | `dd5547b8e8c7` | ✅ 新在位·旧已离位 |
| 96 | `results/_ge01_H_enumeration_and_lock_2026_10_13.md` | `results/_ge01_H_enumeration_and_lock_2026_10_13.md` | 28,522 | `4c5860342d7f` | ✅ 新在位·旧已离位 |
| 97 | `results/_ge01_H_enumeration_round2_2026_10_13.md` | `results/_ge01_H_enumeration_round2_2026_10_13.md` | 37,191 | `ff2afb7a634b` | ✅ 新在位·旧已离位 |
| 98 | `results/_ge01_prereg_5anchor_v3_lock_register_2026_10_15.md` | `results/_ge01_prereg_5anchor_v3_lock_register_2026_10_15.md` | 17,885 | `deea2ccb2643` | ✅ 新在位·旧已离位 |
| 99 | `results/_itemH_fingerprint_provenance_2026_10_12.md` | `results/_itemH_fingerprint_provenance_2026_10_12.md` | 22,752 | `bacbee9a158f` | ✅ 新在位·旧已离位 |
| 100 | `results/_itemH_nonclade_and_hangings_register_2026_10_12.md` | `results/_itemH_nonclade_and_hangings_register_2026_10_12.md` | 13,223 | `37ea7f65a8d6` | ✅ 新在位·旧已离位 |
| 101 | `results/_l3_deferred_items_immediate_disposition_register_2026_10_13.md` | `results/_l3_deferred_items_immediate_disposition_register_2026_10_13.md` | 33,958 | `92e410f45256` | ✅ 新在位·旧已离位 |
| 102 | `results/_m3_glm29_adoption_register_2026_10_13.md` | `results/_m3_glm29_adoption_register_2026_10_13.md` | 23,309 | `6aff3c459ca0` | ✅ 新在位·旧已离位 |
| 103 | `results/_m5_rejudgment_and_dual_value_register_2026_10_14.md` | `results/_m5_rejudgment_and_dual_value_register_2026_10_14.md` | 16,093 | `4b72fbe08ce2` | ✅ 新在位·旧已离位 |
| 104 | `results/_mq_rollout_v7_effect_register_2026_10_14.md` | `results/_mq_rollout_v7_effect_register_2026_10_14.md` | 15,538 | `a709ff7b48de` | ✅ 新在位·旧已离位 |
| 105 | `results/_mq_rollout_v8_effect_register_2026_10_14.md` | `results/_mq_rollout_v8_effect_register_2026_10_14.md` | 14,621 | `5f32931507bb` | ✅ 新在位·旧已离位 |
| 106 | `results/_numbering_face_signature_effect_2026_10_13.md` | `results/_numbering_face_signature_effect_2026_10_13.md` | 11,273 | `6a7f0a1890a4` | ✅ 新在位·旧已离位 |
| 107 | `results/_numbering_family_count_corrigendum_2026_10_14.md` | `results/_numbering_family_count_corrigendum_2026_10_14.md` | 19,812 | `9baf2ea2e9cb` | ✅ 新在位·旧已离位 |
| 108 | `results/_numbering_raw_residual_461_variants_corrigendum_2026_10_14.md` | `results/_numbering_raw_residual_461_variants_corrigendum_2026_10_14.md` | 5,239 | `33feb734ca80` | ✅ 新在位·旧已离位 |
| 109 | `results/_p3_candidate3_supplement_register_2026_10_13.md` | `results/_p3_candidate3_supplement_register_2026_10_13.md` | 22,448 | `b7f725de2d95` | ✅ 新在位·旧已离位 |
| 110 | `results/_pi_give_a_class_pilot_design_2026_10_14.md` | `results/_pi_give_a_class_pilot_design_2026_10_14.md` | 103,140 | `5ec0638e9498` | ✅ 新在位·旧已离位 |
| 111 | `results/_pulled_back_P_B_DISTORTION_BOUND_V0_SPEC_2026_10_13.md` | `results/_pulled_back_P_B_DISTORTION_BOUND_V0_SPEC_2026_10_13.md` | 7,126 | `bb7ca9838150` | ✅ 新在位·旧已离位 |
| 112 | `results/_r5_spec_pack_retrieved_2026_10_13/鲍勃_minimax实验委托规格包_2026_10_12.md.asset.json` | `results/_r5_spec_pack_retrieved_2026_10_13/鲍勃_minimax实验委托规格包_2026_10_12.md.asset.json` | 1,037 | `5ca1aa500fd8` | ✅ 新在位·旧已离位 |
| 113 | `results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md` | `results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md` | 21,309 | `843e42ef4d2a` | ✅ 新在位·旧已离位 |
| 114 | `results/_v4_supp_prereg_v02_add_T15_activation_2026_09_24.md` | `results/_v4_supp_prereg_v02_add_T15_activation_2026_09_24.md` | 20,751 | `443efb39804a` | ✅ 新在位·旧已离位 |
| 115 | `results/_v4_supp_prereg_v02_add_T1_activation_2026_09_24.md` | `results/_v4_supp_prereg_v02_add_T1_activation_2026_09_24.md` | 14,234 | `79936b630015` | ✅ 新在位·旧已离位 |
| 116 | `results/_v5_gt8_lowarm_resultA_cb132cd5_2026_09_29.json` | `results/_v5_gt8_lowarm_resultA_cb132cd5_2026_09_29.json` | 28,638 | `24b0d5eda48a` | ✅ 新在位·旧已离位 |
| 117 | `results/_w1_stage2_premise_stale_register_2026_10_14.md` | `results/_w1_stage2_premise_stale_register_2026_10_14.md` | 8,326 | `a7e14145e1c8` | ✅ 新在位·旧已离位 |
| 118 | `results/_xiang14_third_reissue_registration_2026_10_13.md` | `results/_xiang14_third_reissue_registration_2026_10_13.md` | 7,188 | `25141de92c50` | ✅ 新在位·旧已离位 |
| 119 | `reviews/deep_probe_R1.md` | `reviews/deep_probe_R1.md` | 14,895 | `190dd5df9af2` | ✅ 新在位·旧已离位 |
| 120 | `reviews/deep_probe_R2.md` | `reviews/deep_probe_R2.md` | 23,391 | `a4f8a55b70ba` | ✅ 新在位·旧已离位 |
| 121 | `reviews/literature_scan_v2X_A.md` | `reviews/literature_scan_v2X_A.md` | 18,876 | `d0bba9379b4b` | ✅ 新在位·旧已离位 |
| 122 | `reviews/literature_scan_v2X_B.md` | `reviews/literature_scan_v2X_B.md` | 30,468 | `313b30815a39` | ✅ 新在位·旧已离位 |
| 123 | `reviews/peer_review_v19_A.md` | `reviews/peer_review_v19_A.md` | 24,409 | `28878116d87b` | ✅ 新在位·旧已离位 |
| 124 | `reviews/peer_review_v19_B.md` | `reviews/peer_review_v19_B.md` | 42,672 | `da98f9e310d4` | ✅ 新在位·旧已离位 |
| 125 | `reviews/review_coach_v2X_draft.md` | `reviews/review_coach_v2X_draft.md` | 23,468 | `0bafe659c00d` | ✅ 新在位·旧已离位 |
| 126 | `reviews/review_format_v2X.md` | `reviews/review_format_v2X.md` | 6,656 | `2dc4b45424ab` | ✅ 新在位·旧已离位 |
| 127 | `verifier/README.md` | `verifier/README.md` | 14,360 | `d76f2dc473be` | ✅ 新在位·旧已离位 |
| 128 | `verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json` | `verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json` | 5,049 | `da517c115f3c` | ✅ 新在位·旧已离位 |
| 129 | `verifier/handoff/P_A_V0_anchors_sha256_12.json` | `verifier/handoff/P_A_V0_anchors_sha256_12.json` | 7,796 | `c4f029f780d8` | ✅ 新在位·旧已离位 |
| 130 | `verifier/handoff/P_F_PREDECISION_2026_09_09.json` | `verifier/handoff/P_F_PREDECISION_2026_09_09.json` | 3,680 | `b41c98bf90cc` | ✅ 新在位·旧已离位 |
| 131 | `verifier/kill_lines/GT_kill_line_carrier_v0.md` | `verifier/kill_lines/GT_kill_line_carrier_v0.md` | 16,486 | `0f65a42e7a34` | ✅ 新在位·旧已离位 |
| 132 | `verifier/kill_lines/GT_kill_line_carrier_v1.md` | `verifier/kill_lines/GT_kill_line_carrier_v1.md` | 18,905 | `9e09214cf088` | ✅ 新在位·旧已离位 |
| 133 | `verifier/runs/20260823T022721Z.log` | `verifier/runs/20260823T022721Z.log` | 7 | `cf205dbb8cea` | ✅ 新在位·旧已离位 |
| 134 | `verifier/runs/20260823T130229Z.log` | `verifier/runs/20260823T130229Z.log` | 839 | `1af06784d975` | ✅ 新在位·旧已离位 |
| 135 | `verifier/runs/20260823T130254Z.log` | `verifier/runs/20260823T130254Z.log` | 839 | `8316e03518f2` | ✅ 新在位·旧已离位 |
| 136 | `verifier/runs/20260823T130326Z.log` | `verifier/runs/20260823T130326Z.log` | 819 | `e8698e422d69` | ✅ 新在位·旧已离位 |
| 137 | `verifier/runs/20260823T130405Z.log` | `verifier/runs/20260823T130405Z.log` | 576 | `d6071ff9493e` | ✅ 新在位·旧已离位 |
| 138 | `verifier/runs/20260823T131053Z.log` | `verifier/runs/20260823T131053Z.log` | 911 | `94e578649599` | ✅ 新在位·旧已离位 |
| 139 | `verifier/runs/20260823T134128Z.log` | `verifier/runs/20260823T134128Z.log` | 910 | `6cf95aade825` | ✅ 新在位·旧已离位 |
| 140 | `verifier/runs/20260823T134305Z.log` | `verifier/runs/20260823T134305Z.log` | 972 | `c9ae2079fc1f` | ✅ 新在位·旧已离位 |
| 141 | `verifier/runs/20260823T154658Z.log` | `verifier/runs/20260823T154658Z.log` | 1,536 | `1fca45290883` | ✅ 新在位·旧已离位 |

📌 **并入注记规则（承派工单第 ④ 项）**：凡本清单（§4.2）列及而被转移之件，**一律以该表所列新路径为准**，其原 repo 路径**以本表为唯一权威映射**（沿登记件 §4-3「文本引用面…§4-1 映射表即为旧路径→新路径之权威改写依据」）；§4.2 之 `†` 标记即指向本表。

### §3.4 回退 **25** 件（检出活代码功能引用 · 已复原原位）

| 项 | 本棒实测 |
|:--|:--|
| 回退件数 | **25**（与登记件 §4-2 行数**一致**）|
| **已在 REPO 原位** | **25 / 25** ✅ |
| **仍在 SUB** | **0** ✅ |
| 回退原因 | 活代码功能引用（登记件 §4-2：`verifier/*/check.py` 之 `read_text()` 等）|
| 残余功能断链 | 登记件载 **0**；⛔ 本棒 0 复算（纯勘察棒）|

**逐件（新路径 → 旧路径 · 已复原）**

| # | 回退件（repo 相对 · 已复原） | 原曾转出至 | 本棒复核 |
| --: | :-- | :-- | :-: |
| 1 | `docs/BASELINE_REGISTRY.md` | `sub/docs/BASELINE_REGISTRY.md` | ✅ REPO 在位·SUB 0 残留 |
| 2 | `docs/CLOSURE_v19_and_v2X_gametheory.md` | `sub/docs/CLOSURE_v19_and_v2X_gametheory.md` | ✅ REPO 在位·SUB 0 残留 |
| 3 | `docs/Findings_GT2B.md` | `sub/docs/Findings_GT2B.md` | ✅ REPO 在位·SUB 0 残留 |
| 4 | `docs/Findings_GT3.md` | `sub/docs/Findings_GT3.md` | ✅ REPO 在位·SUB 0 残留 |
| 5 | `docs/Findings_GT8.md` | `sub/docs/Findings_GT8.md` | ✅ REPO 在位·SUB 0 残留 |
| 6 | `docs/Findings_GT8B.md` | `sub/docs/Findings_GT8B.md` | ✅ REPO 在位·SUB 0 残留 |
| 7 | `docs/Findings_v2.0.md` | `sub/docs/Findings_v2.0.md` | ✅ REPO 在位·SUB 0 残留 |
| 8 | `docs/Findings_v2.0_bigquiz.md` | `sub/docs/Findings_v2.0_bigquiz.md` | ✅ REPO 在位·SUB 0 残留 |
| 9 | `docs/Findings_v2.0_boss.md` | `sub/docs/Findings_v2.0_boss.md` | ✅ REPO 在位·SUB 0 残留 |
| 10 | `docs/Findings_v2.0_corrections.md` | `sub/docs/Findings_v2.0_corrections.md` | ✅ REPO 在位·SUB 0 残留 |
| 11 | `docs/Findings_v2.0_crossval.md` | `sub/docs/Findings_v2.0_crossval.md` | ✅ REPO 在位·SUB 0 残留 |
| 12 | `docs/Findings_v2.0_hardening.md` | `sub/docs/Findings_v2.0_hardening.md` | ✅ REPO 在位·SUB 0 残留 |
| 13 | `docs/Findings_v2.0_photonics.md` | `sub/docs/Findings_v2.0_photonics.md` | ✅ REPO 在位·SUB 0 残留 |
| 14 | `docs/Findings_v2.0_skills.md` | `sub/docs/Findings_v2.0_skills.md` | ✅ REPO 在位·SUB 0 残留 |
| 15 | `docs/SPEC_GT3.md` | `sub/docs/SPEC_GT3.md` | ✅ REPO 在位·SUB 0 残留 |
| 16 | `docs/SPEC_GT8B.md` | `sub/docs/SPEC_GT8B.md` | ✅ REPO 在位·SUB 0 残留 |
| 17 | `docs/SPEC_v1.8.md` | `sub/docs/SPEC_v1.8.md` | ✅ REPO 在位·SUB 0 残留 |
| 18 | `docs/SPEC_v2.0.md` | `sub/docs/SPEC_v2.0.md` | ✅ REPO 在位·SUB 0 残留 |
| 19 | `docs/SPEC_v2.0_amendment1.md` | `sub/docs/SPEC_v2.0_amendment1.md` | ✅ REPO 在位·SUB 0 残留 |
| 20 | `docs/SYNTHESIS_mind_game.md` | `sub/docs/SYNTHESIS_mind_game.md` | ✅ REPO 在位·SUB 0 残留 |
| 21 | `reviews/post_draft_verification_v2X.md` | `sub/reviews/post_draft_verification_v2X.md` | ✅ REPO 在位·SUB 0 残留 |
| 22 | `reviews/review_coach_v2X_draft_r2.md` | `sub/reviews/review_coach_v2X_draft_r2.md` | ✅ REPO 在位·SUB 0 残留 |
| 23 | `reviews/review_coach_v2X_outline.md` | `sub/reviews/review_coach_v2X_outline.md` | ✅ REPO 在位·SUB 0 残留 |
| 24 | `reviews/review_realign_v2X.md` | `sub/reviews/review_realign_v2X.md` | ✅ REPO 在位·SUB 0 残留 |
| 25 | `verifier/handoff/KT_ABC1_anchors_sha256_12.root_session_11318B.bak_2026_09_23.json` | `sub/verifier/handoff/KT_ABC1_anchors_sha256_12.root_session_11318B.bak_2026_09_23.json` | ✅ REPO 在位·SUB 0 残留 |

## §4 · 逐件表（相对路径 ／ bytes ／ mtime ／ SHA-12 ／ 类别）

### §4.0 汇总

| 区 | 路径 | 件数 | bytes | 末次 mtime |
|:--|:--|--:|--:|:--|
| REPO | `D:\私人资料\deposon-repo` | **4,282** | **189,657,496** | 2026-10-18 00:58:56 |
| SUB | `D:\私人资料\deposon-sub` | **1,276** | **60,166,418** | 2026-10-15 13:01:46 |
| **合计** | —— | **5,558** | **249,823,914** | —— |

**分区 · 类别**

| 区 | 成果面（件／bytes） | 噪声面 `.tmp/`（件／bytes） |
|:--|--:|--:|
| REPO | 2,014 / 67,496,712 | 2,268 / 122,160,784 |
| SUB | 1,276 / 60,166,418 | **0 / 0** |

📌 **分型（md／py／json／其他）汇总见 §11-A-3（🆕 新增面）**；**两区计数多读并列见 §5**；**今晚增量面见 §7**。

### §4.1 区 `D:\私人资料\deposon-repo`（4,282 件 ／ 189,657,496 bytes）

**逐目录分布**

| 目录 | 件数 | bytes | 类别 |
|:--|--:|--:|:--|
| `.mavis/scripts/cleanup511/` | 15 | 397,015 | 成果面 |
| `.mavis/scripts/cleanup511/__pycache__/` | 1 | 10,525 | 成果面 |
| `.mavis/scripts/kt_a1/` | 2 | 19 | 成果面 |
| `.mavis/scripts/kt_b1/` | 1 | 966 | 成果面 |
| `.mavis/scripts/kt_c1/` | 1 | 7 | 成果面 |
| `.tmp/` | 1,544 | 82,937,292 | 噪声面 |
| `.tmp/__pycache__/` | 10 | 332,580 | 成果面 |
| `.tmp/_pre_mod/` | 1 | 36,217 | 成果面 |
| `.tmp/gh_survey_r2/` | 14 | 553,115 | 成果面 |
| `.tmp/whitelist_backup_2026_10_17/` | 698 | 38,265,363 | 成果面 |
| `.tmp/whitelist_backup_2026_10_17/_pre_mod/` | 1 | 36,217 | 成果面 |
| `.trae/scripts/` | 2 | 34,781 | 成果面 |
| `.vscode/` | 1 | 41 | 成果面 |
| `_remote_pullback_2026_10_17/_september_workspace/deposon_team/verifier/` | 3 | 20,012 | 成果面 |
| `_remote_pullback_2026_10_17/_september_workspace/results/` | 6 | 526,364 | 成果面 |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/` | 136 | 2,765,684 | 成果面 |
| `_remote_pullback_2026_10_17/_september_workspace/verifier/` | 1 | 16,252 | 成果面 |
| `_remote_pullback_2026_10_17/letters/` | 1 | 27,835 | 成果面 |
| `_remote_pullback_2026_10_17/results/` | 26 | 80,271 | 成果面 |
| `_remote_pullback_2026_10_17/results/attacker_xl_cache/` | 6 | 30,507 | 成果面 |
| `_remote_pullback_2026_10_17/results/familyL_cache/` | 6 | 8,278 | 成果面 |
| `_remote_pullback_2026_10_17/results/familyL_prior_cache/` | 6 | 14,131 | 成果面 |
| `_remote_pullback_2026_10_17/results/gt2_attacker_cache/` | 4 | 9,898 | 成果面 |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/` | 24 | 48,941 | 成果面 |
| `attacks/` | 4 | 12,922 | 成果面 |
| `corpus/v20/` | 28 | 166,342 | 成果面 |
| `corpus/v20/by_model/coze/` | 1 | 10,978 | 成果面 |
| `corpus/v20/by_model/GLM_1/` | 1 | 19,685 | 成果面 |
| `corpus/v20/by_model/GLM_2/` | 1 | 13,150 | 成果面 |
| `corpus/v20/by_model/kimi/` | 1 | 24,150 | 成果面 |
| `corpus/v20/by_model/minimax/` | 1 | 25,347 | 成果面 |
| `corpus/v20_caption_surface/` | 9 | 687,294 | 成果面 |
| `deposon_team/plugins/` | 88 | 1,253,491 | 成果面 |
| `docs/` | 32 | 214,380 | 成果面 |
| `docs/V3X/` | 10 | 1,024,558 | 成果面 |
| `letters/` | 115 | 3,587,300 | 成果面 |
| `paper/` | 3 | 124,497 | 成果面 |
| `paper/v2/` | 2 | 20,590 | 成果面 |
| `pi_rulings/` | 93 | 2,905,081 | 成果面 |
| `results/` | 1,039 | 48,035,800 | 成果面 |
| `results/_archive_2026-10-12/exec_artifacts/` | 14 | 119,341 | 成果面 |
| `results/_archive_2026-10-12/pycache_sink/deposon_team_plugins_pycache/` | 3 | 216,752 | 成果面 |
| `results/_archive_2026-10-12/pycache_sink/results_pycache/` | 5 | 312,650 | 成果面 |
| `results/_archive_2026-10-12/superseded_variants/` | 1 | 5,088 | 成果面 |
| `results/_archive_2026-10-14/voided/` | 2 | 64,419 | 成果面 |
| `results/_archive_2026_09_24/` | 7 | 136,395 | 成果面 |
| `results/_d9_e2e_backup_2026_10_13/` | 6 | 569,034 | 成果面 |
| `results/_d9_e2e_rerun_backup_2026_10_13/` | 1 | 15,409 | 成果面 |
| `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/` | 9 | 323,800 | 成果面 |
| `results/_p_i_real_labels_2026_09_16/` | 1 | 1,043 | 成果面 |
| `results/_p_j_convergence_basin_2026_09_16/` | 1 | 1,669 | 成果面 |
| `results/_p_l_p_c_finite_size_scaling_2026_09_16/` | 1 | 9,076 | 成果面 |
| `results/_p_l_real_data_collapse_2026_09_16/` | 1 | 3,761 | 成果面 |
| `results/_p_m_attack_surface_cost_2026_09_16/` | 1 | 5,266 | 成果面 |
| `results/_p_m_real_separation_2026_09_16/` | 1 | 2,042 | 成果面 |
| `results/_p_n_curvature_potential_coupling_2026_09_16/` | 1 | 4,276 | 成果面 |
| `results/_p_o_stranger_verification_2026_09_16/` | 1 | 5,916 | 成果面 |
| `results/_r5_spec_pack_retrieved_2026_10_13/` | 1 | 14,758 | 成果面 |
| `results/_v3_recheck_08b_executor/` | 3 | 150,454 | 成果面 |
| `results/_v3_recheck_08c_preexp_data/` | 4 | 202,840 | 成果面 |
| `results/_v3_s1_executor/` | 3 | 97,165 | 成果面 |
| `results/_v3_s2_executor/` | 3 | 161,183 | 成果面 |
| `results/_v3_s3_wordexpand_data/` | 5 | 159,875 | 成果面 |
| `results/_v3_s_phrasetemplate_preexp_data/` | 3 | 89,973 | 成果面 |
| `results/_v3x_18frozen_remeasure_2026_09_16/` | 1 | 4,202 | 成果面 |
| `results/_v3x_experiments_2026_09_16/` | 1 | 17,053 | 成果面 |
| `results/_v3x_p_k_verify_2026_09_16/` | 1 | 2,059 | 成果面 |
| `reviews/` | 9 | 116,640 | 成果面 |
| `reviews/data/` | 15 | 74,769 | 成果面 |
| `scripts/` | 10 | 148,821 | 成果面 |
| `tests/` | 23 | 212,514 | 成果面 |
| `tools/` | 6 | 147,870 | 成果面 |
| `tools/__pycache__/` | 3 | 118,597 | 成果面 |
| `tools/_archive_purge_2026_10_17/` | 13 | 526,885 | 成果面 |
| `tools/_archive_purge_2026_10_17/__pycache__/` | 1 | 5,826 | 成果面 |
| `verifier/` | 6 | 34,727 | 成果面 |
| `verifier/audit/` | 1 | 22,105 | 成果面 |
| `verifier/audit/__pycache__/` | 1 | 27,641 | 成果面 |
| `verifier/handoff/` | 3 | 30,496 | 成果面 |
| `verifier/kill_lines/` | 1 | 2,781 | 成果面 |
| `verifier/runs/` | 48 | 24,065 | 成果面 |
| `verifier/v1/` | 1 | 2,976 | 成果面 |
| `verifier/v10/` | 1 | 5,261 | 成果面 |
| `verifier/v11/` | 1 | 2,767 | 成果面 |
| `verifier/v12/` | 1 | 4,142 | 成果面 |
| `verifier/v13/` | 1 | 3,495 | 成果面 |
| `verifier/v14/` | 1 | 3,278 | 成果面 |
| `verifier/v15/` | 1 | 3,231 | 成果面 |
| `verifier/v16/` | 1 | 2,691 | 成果面 |
| `verifier/v17/` | 2 | 3,335 | 成果面 |
| `verifier/v18/` | 1 | 3,180 | 成果面 |
| `verifier/v19/` | 1 | 1,995 | 成果面 |
| `verifier/v2/` | 1 | 2,510 | 成果面 |
| `verifier/v20/` | 2 | 3,106 | 成果面 |
| `verifier/v21/` | 1 | 3,702 | 成果面 |
| `verifier/v22/` | 1 | 2,857 | 成果面 |
| `verifier/v23/` | 1 | 2,659 | 成果面 |
| `verifier/v24/` | 1 | 3,124 | 成果面 |
| `verifier/v25/` | 1 | 2,576 | 成果面 |
| `verifier/v26/` | 1 | 2,595 | 成果面 |
| `verifier/v27/` | 1 | 2,132 | 成果面 |
| `verifier/v28/` | 1 | 2,201 | 成果面 |
| `verifier/v29/` | 1 | 2,124 | 成果面 |
| `verifier/v3/` | 1 | 2,544 | 成果面 |
| `verifier/v30/` | 1 | 2,565 | 成果面 |
| `verifier/v31/` | 1 | 2,185 | 成果面 |
| `verifier/v32/` | 1 | 2,551 | 成果面 |
| `verifier/v33/` | 1 | 6,019 | 成果面 |
| `verifier/v34/` | 1 | 3,715 | 成果面 |
| `verifier/v35/` | 1 | 2,385 | 成果面 |
| `verifier/v36/` | 1 | 968 | 成果面 |
| `verifier/v37/` | 1 | 1,141 | 成果面 |
| `verifier/v38/` | 1 | 1,705 | 成果面 |
| `verifier/v39/` | 1 | 1,935 | 成果面 |
| `verifier/v4/` | 1 | 3,205 | 成果面 |
| `verifier/v40/` | 1 | 1,604 | 成果面 |
| `verifier/v41/` | 1 | 1,687 | 成果面 |
| `verifier/v42/` | 1 | 1,509 | 成果面 |
| `verifier/v43/` | 1 | 1,224 | 成果面 |
| `verifier/v5/` | 1 | 2,255 | 成果面 |
| `verifier/v6/` | 1 | 2,757 | 成果面 |
| `verifier/v7/` | 1 | 4,300 | 成果面 |
| `verifier/v8/` | 1 | 3,210 | 成果面 |
| `verifier/v9/` | 1 | 5,352 | 成果面 |
| `（根散件）/` | 78 | 1,069,631 | 成果面 |

**逐件（4,282 件）**

| # | 相对路径 | bytes | mtime | SHA-12 | 类别 |
| --: | :-- | --: | :-- | :-- | :-: |
| 1 | `.gitignore` | 105 | 2026-10-17 10:25:25 | `61576ba9caa7` | 成果面 |
| 2 | `.mavis/scripts/cleanup511/__pycache__/recycle_exec.cpython-314.pyc` | 10,525 | 2026-10-17 10:16:44 | `1bdd614f1f02` | 成果面 |
| 3 | `.mavis/scripts/cleanup511/audit_manifest.py` | 2,091 | 2026-10-17 10:13:22 | `02e196e2c667` | 成果面 |
| 4 | `.mavis/scripts/cleanup511/audit_manifest2.py` | 3,453 | 2026-10-17 10:13:49 | `8cebb1cd14ae` | 成果面 |
| 5 | `.mavis/scripts/cleanup511/audit_manifest3.py` | 2,119 | 2026-10-17 10:14:48 | `588c821490ce` | 成果面 |
| 6 | `.mavis/scripts/cleanup511/batch_exec.py` | 5,963 | 2026-10-17 10:17:31 | `26c99e9a0c42` | 成果面 |
| 7 | `.mavis/scripts/cleanup511/debug_i.py` | 1,466 | 2026-10-17 10:20:18 | `a73a6885b4ba` | 成果面 |
| 8 | `.mavis/scripts/cleanup511/exec_list.json` | 85,898 | 2026-10-17 10:16:14 | `570b1509e16d` | 成果面 |
| 9 | `.mavis/scripts/cleanup511/exec_report.json` | 251,947 | 2026-10-17 10:17:59 | `eaddc07479ab` | 成果面 |
| 10 | `.mavis/scripts/cleanup511/final_sweep.py` | 3,502 | 2026-10-17 10:19:53 | `c271feb2b853` | 成果面 |
| 11 | `.mavis/scripts/cleanup511/finalize.py` | 3,570 | 2026-10-17 10:16:04 | `224bda85007b` | 成果面 |
| 12 | `.mavis/scripts/cleanup511/make_register.py` | 13,920 | 2026-10-17 10:24:18 | `45416c09e419` | 成果面 |
| 13 | `.mavis/scripts/cleanup511/reconcile_probe.py` | 1,934 | 2026-10-17 10:16:55 | `32bb7912b613` | 成果面 |
| 14 | `.mavis/scripts/cleanup511/recycle_exec.py` | 6,489 | 2026-10-17 10:16:32 | `c93fc1c27fea` | 成果面 |
| 15 | `.mavis/scripts/cleanup511/spot_check.py` | 2,238 | 2026-10-17 10:21:02 | `10ced278e75f` | 成果面 |
| 16 | `.mavis/scripts/cleanup511/survey511.py` | 10,678 | 2026-10-17 10:25:25 | `5e9672a15d4e` | 成果面 |
| 17 | `.mavis/scripts/cleanup511/verify_dirs.py` | 1,747 | 2026-10-17 10:18:56 | `84fd486f0dcb` | 成果面 |
| 18 | `.mavis/scripts/kt_a1/test_persist.txt` | 15 | 2026-09-24 22:30:25 | `2898abb5082b` | 成果面 |
| 19 | `.mavis/scripts/kt_a1/test_write.txt` | 4 | 2026-09-24 22:27:23 | `9f86d081884c` | 成果面 |
| 20 | `.mavis/scripts/kt_b1/fix_safe_float.py` | 966 | 2026-09-24 22:23:52 | `4420543e60a4` | 成果面 |
| 21 | `.mavis/scripts/kt_c1/test_write.txt` | 7 | 2026-09-24 22:29:06 | `85d443e165bb` | 成果面 |
| 22 | `.tmp/_26b_verdict_prep_hashcheck_2026_10_01.py` | 3,842 | 2026-10-01 08:54:44 | `6927c9462f41` | 噪声面 |
| 23 | `.tmp/_26b_verdict_prep_literalcheck_2026_10_01.py` | 4,378 | 2026-10-01 08:55:50 | `50fe799b0a2e` | 噪声面 |
| 24 | `.tmp/_26b_verdict_prep_validate_2026_10_01.py` | 4,640 | 2026-10-01 08:57:57 | `494cca45b873` | 噪声面 |
| 25 | `.tmp/_659_compact.txt` | 155,628 | 2026-10-14 02:36:23 | `795862c09a40` | 噪声面 |
| 26 | `.tmp/_659_overlap_digest.txt` | 239,157 | 2026-10-14 02:35:09 | `4f20b8085fb9` | 噪声面 |
| 27 | `.tmp/_659_report_gen.py` | 27,457 | 2026-10-14 02:40:26 | `cd4b8ed56b2c` | 噪声面 |
| 28 | `.tmp/__pycache__/exp_harness_pre_2026_10_17.cpython-314.pyc` | 40,144 | 2026-10-17 23:30:50 | `27b60f271b37` | 噪声面 |
| 29 | `.tmp/__pycache__/kdm413_rm_analyze_2026_10_17.cpython-314.pyc` | 38,485 | 2026-10-17 20:46:46 | `4ddbd6ab89e7` | 噪声面 |
| 30 | `.tmp/__pycache__/kdm413_rm_collect_2026_10_17.cpython-314.pyc` | 26,778 | 2026-10-17 20:46:46 | `aa2e0beac0ef` | 噪声面 |
| 31 | `.tmp/__pycache__/kdm413_rm_freeze_2026_10_17.cpython-314.pyc` | 15,653 | 2026-10-17 20:46:46 | `e4b1ec3de237` | 噪声面 |
| 32 | `.tmp/__pycache__/kdm413_rm_preflight_2026_10_17.cpython-314.pyc` | 13,515 | 2026-10-17 20:46:46 | `04a796b10c0a` | 噪声面 |
| 33 | `.tmp/__pycache__/kdm413_rm_verify_2026_10_17.cpython-314.pyc` | 7,353 | 2026-10-17 20:46:46 | `72289e06bf62` | 噪声面 |
| 34 | `.tmp/__pycache__/kdm413_rm_write_doc_2026_10_17.cpython-314.pyc` | 49,347 | 2026-10-17 20:46:46 | `a4d2003024b7` | 噪声面 |
| 35 | `.tmp/__pycache__/refonly161_r2_build_register.cpython-314.pyc` | 59,155 | 2026-10-17 16:41:41 | `064013615cc2` | 噪声面 |
| 36 | `.tmp/__pycache__/refonly161_r2_probe.cpython-314.pyc` | 38,319 | 2026-10-17 16:34:16 | `2d9d5a83dc4e` | 噪声面 |
| 37 | `.tmp/__pycache__/ritt_remeasure_collect_2026_10_17.cpython-314.pyc` | 43,831 | 2026-10-17 19:54:38 | `8823a3df0a45` | 噪声面 |
| 38 | `.tmp/_abc_diff_2026_10_10.py` | 6,620 | 2026-10-10 12:23:35 | `6d6733f0e5c2` | 噪声面 |
| 39 | `.tmp/_abc_final_2026_10_10.py` | 7,329 | 2026-10-10 12:26:39 | `15b4de4fdff6` | 噪声面 |
| 40 | `.tmp/_abc_h1h2_2026_10_10.py` | 7,889 | 2026-10-10 12:25:31 | `16f19bad301f` | 噪声面 |
| 41 | `.tmp/_abc_readings_reprocheck_2026_10_10.py` | 9,491 | 2026-10-10 12:23:04 | `0ec2a2bf3bab` | 噪声面 |
| 42 | `.tmp/_abc_readings_reprocheck_out_2026_10_10.json` | 78,436 | 2026-10-10 12:23:11 | `2f9aa16b63ca` | 噪声面 |
| 43 | `.tmp/_abc_rfd_2026_10_10.py` | 5,938 | 2026-10-10 12:26:11 | `39268ca6adff` | 噪声面 |
| 44 | `.tmp/_aggregate_10cells.py` | 3,009 | 2026-09-26 17:42:04 | `3bdc6250d0f2` | 噪声面 |
| 45 | `.tmp/_aggregate_10cells_v2.py` | 5,131 | 2026-09-26 17:45:07 | `af1b7f09f74d` | 噪声面 |
| 46 | `.tmp/_aggregate_10cells_v3.py` | 2,969 | 2026-09-26 17:45:22 | `04b127d80bf0` | 噪声面 |
| 47 | `.tmp/_aggregate_10cells_v4.py` | 2,454 | 2026-09-26 17:45:58 | `f99a3765c3c3` | 噪声面 |
| 48 | `.tmp/_append_intake_supplement_6_tail.py` | 9,335 | 2026-10-10 15:09:46 | `c3339682d68c` | 噪声面 |
| 49 | `.tmp/_audit3b.txt` | 50,554 | 2026-09-28 15:20:27 | `e64565a2b180` | 噪声面 |
| 50 | `.tmp/_audit_part3_out.txt` | 5,195 | 2026-09-28 15:18:03 | `85a9d9861d38` | 噪声面 |
| 51 | `.tmp/_audit_part4.txt` | 14,826 | 2026-09-28 15:23:04 | `def27c1c3511` | 噪声面 |
| 52 | `.tmp/_b11_extract.txt` | 6,654 | 2026-10-17 22:55:42 | `71d70be96c9c` | 噪声面 |
| 53 | `.tmp/_b11_g86_L93_raw.txt` | 874 | 2026-10-17 23:51:51 | `b210d5c92bb1` | 噪声面 |
| 54 | `.tmp/_b11_g86_L94_raw.txt` | 5,843 | 2026-10-17 23:51:51 | `196227473fab` | 噪声面 |
| 55 | `.tmp/_b11_g86_L95_raw.txt` | 524 | 2026-10-17 23:51:51 | `522c3ee187b9` | 噪声面 |
| 56 | `.tmp/_b11_g86_L98_raw.txt` | 11,039 | 2026-10-17 23:51:51 | `403f30fffb4c` | 噪声面 |
| 57 | `.tmp/_b11_hit_g000000000086--ctx_12888aab-113d-47d8-9c0b-1d2b0733ab2e.jsonl.txt` | 1,903 | 2026-10-17 22:58:03 | `83d0741f85ca` | 噪声面 |
| 58 | `.tmp/_b11_hit_g000000000087--ctx_182027ab-822e-4907-977e-40e6dac53569.jsonl.txt` | 1,901 | 2026-10-17 22:58:03 | `505eca298c39` | 噪声面 |
| 59 | `.tmp/_b11_hit_messages.jsonl.txt` | 1,903 | 2026-10-17 22:57:55 | `83d0741f85ca` | 噪声面 |
| 60 | `.tmp/_b11_probe.txt` | 889 | 2026-10-17 22:55:00 | `c771f4ced820` | 噪声面 |
| 61 | `.tmp/_b11_q9_card_definition.txt` | 5,364 | 2026-10-17 23:58:21 | `1b0b8b61feb5` | 噪声面 |
| 62 | `.tmp/_b11_q9_response_verbatim.txt` | 10,599 | 2026-10-17 23:52:38 | `126a2f454747` | 噪声面 |
| 63 | `.tmp/_b11_register_writer.py` | 9,423 | 2026-10-18 00:01:47 | `45d150c5f8ed` | 噪声面 |
| 64 | `.tmp/_b12_q1_refs_2026_09_29.py` | 4,890 | 2026-09-29 16:24:08 | `86b2d9b7b7bd` | 噪声面 |
| 65 | `.tmp/_b12_q1_timeslice_2026_09_29.py` | 798 | 2026-09-29 16:30:07 | `bacf6379b9bf` | 噪声面 |
| 66 | `.tmp/_b12_q4_adjacent_2026_09_29.py` | 5,709 | 2026-09-29 16:27:42 | `61cbc9965896` | 噪声面 |
| 67 | `.tmp/_b12_q4_exact_2026_09_29.py` | 7,140 | 2026-09-29 16:26:54 | `79eba6136d83` | 噪声面 |
| 68 | `.tmp/_b12_q4_formcand_2026_09_29.py` | 6,510 | 2026-09-29 16:22:21 | `f58f388996d4` | 噪声面 |
| 69 | `.tmp/_b12_tables_2026_09_29.py` | 1,907 | 2026-09-29 16:30:30 | `10db58be72cf` | 噪声面 |
| 70 | `.tmp/_build_5anchor_json_draft.py` | 34,455 | 2026-10-14 16:29:28 | `391e7a1be0e5` | 噪声面 |
| 71 | `.tmp/_build_5anchor_json_v1.py` | 11,627 | 2026-10-14 17:52:06 | `56c459492ecf` | 噪声面 |
| 72 | `.tmp/_build_intake_supplement_6.py` | 13,094 | 2026-10-10 15:09:02 | `6336456853ae` | 噪声面 |
| 73 | `.tmp/_build_receipt_supplement_6.py` | 11,430 | 2026-10-12 22:24:56 | `20c44c665b4f` | 噪声面 |
| 74 | `.tmp/_c5_b3_rewalk_postcheck_2026_10_01.py` | 2,249 | 2026-10-01 09:44:01 | `aca7dad6ddfa` | 噪声面 |
| 75 | `.tmp/_c5_b3_rewalk_precheck_2026_10_01.py` | 2,035 | 2026-10-01 09:43:19 | `4aad531a2ddb` | 噪声面 |
| 76 | `.tmp/_c5_b3_rewalk_utf8check_2026_10_01.py` | 925 | 2026-10-01 09:44:11 | `5488ff2db11f` | 噪声面 |
| 77 | `.tmp/_c5_b_group_fix_readings_2026_10_09.py` | 12,289 | 2026-10-09 13:38:56 | `b6855b38acc2` | 噪声面 |
| 78 | `.tmp/_c5_feasibility_probe.py` | 1,036 | 2026-09-29 13:22:43 | `d730612b0c9a` | 噪声面 |
| 79 | `.tmp/_canonical_census.py` | 4,382 | 2026-10-14 14:03:57 | `36b7af564c56` | 噪声面 |
| 80 | `.tmp/_canonical_lines.json` | 15,033 | 2026-10-14 14:06:49 | `9b0997fc7e52` | 噪声面 |
| 81 | `.tmp/_canonical_lines.py` | 3,354 | 2026-10-14 14:06:35 | `08aa8638a0b2` | 噪声面 |
| 82 | `.tmp/_carrier_probe.py` | 398 | 2026-10-16 22:51:48 | `f6c27c4dfd13` | 噪声面 |
| 83 | `.tmp/_check_escape.py` | 332 | 2026-10-14 00:12:36 | `5f026b0baf39` | 噪声面 |
| 84 | `.tmp/_check_kimi_sides.py` | 1,459 | 2026-09-26 17:44:36 | `4f3291959a6d` | 噪声面 |
| 85 | `.tmp/_ci_gap_fill_alt_bc_aper_prime_2026_10_09.py` | 20,997 | 2026-10-09 17:42:45 | `b0cf9baba64b` | 噪声面 |
| 86 | `.tmp/_cleanup_r2_cleanlist.json` | 810 | 2026-10-17 11:42:16 | `ce71dda28157` | 噪声面 |
| 87 | `.tmp/_cleanup_r2_exec.py` | 7,884 | 2026-10-17 11:43:04 | `a2029c340ac5` | 噪声面 |
| 88 | `.tmp/_cleanup_r2_exec_journal.json` | 10,327 | 2026-10-17 11:43:44 | `cd636cb64813` | 噪声面 |
| 89 | `.tmp/_cleanup_r2_plus83_cleanlist.json` | 2,068 | 2026-10-17 11:58:10 | `524acfe71d12` | 噪声面 |
| 90 | `.tmp/_cleanup_r2_plus83_exec.py` | 7,604 | 2026-10-17 11:57:25 | `3079669ee4a4` | 噪声面 |
| 91 | `.tmp/_cleanup_r2_plus83_exec_journal.json` | 22,089 | 2026-10-17 11:59:19 | `d103c2064aa6` | 噪声面 |
| 92 | `.tmp/_cleanup_r2_plus83_postcheck.json` | 17,173 | 2026-10-17 11:59:42 | `4523a24dbb5e` | 噪声面 |
| 93 | `.tmp/_cleanup_r2_plus83_postcheck.py` | 3,979 | 2026-10-17 11:59:34 | `1b15a8180ac7` | 噪声面 |
| 94 | `.tmp/_cleanup_r2_plus83_report.py` | 22,508 | 2026-10-17 12:02:27 | `23bc89ff6222` | 噪声面 |
| 95 | `.tmp/_cleanup_r2_postcheck.json` | 6,652 | 2026-10-17 11:44:18 | `720b25650bcd` | 噪声面 |
| 96 | `.tmp/_cleanup_r2_postcheck.py` | 4,585 | 2026-10-17 11:44:09 | `cfd60493f18d` | 噪声面 |
| 97 | `.tmp/_cleanup_r2_report.py` | 24,300 | 2026-10-17 11:47:33 | `b6e6d0dcf0ee` | 噪声面 |
| 98 | `.tmp/_cleanup_r2_scan.py` | 11,507 | 2026-10-17 11:27:45 | `60d6d3d37076` | 噪声面 |
| 99 | `.tmp/_cleanup_r2_scan2.py` | 12,112 | 2026-10-17 11:32:24 | `7019c7b8d728` | 噪声面 |
| 100 | `.tmp/_cleanup_r2_scan3.py` | 12,389 | 2026-10-17 11:38:52 | `46b7b8230e86` | 噪声面 |
| 101 | `.tmp/_cleanup_r2_scan4.py` | 11,086 | 2026-10-17 11:56:16 | `0558ce9a0702` | 噪声面 |
| 102 | `.tmp/_cleanup_r2_scan4_out.json` | 562,033 | 2026-10-17 11:57:56 | `7a95315032ee` | 噪声面 |
| 103 | `.tmp/_cleanup_r2_scan_out.json` | 758,995 | 2026-10-17 11:40:50 | `3b107c078490` | 噪声面 |
| 104 | `.tmp/_compute_metrics.py` | 7,752 | 2026-09-26 17:43:45 | `ae2b0142b09e` | 噪声面 |
| 105 | `.tmp/_compute_metrics_v2.py` | 8,017 | 2026-09-26 17:46:18 | `0620ef317e8a` | 噪声面 |
| 106 | `.tmp/_corrupt_ge01_readiness_firstwrite_2026_10_13.md` | 31,745 | 2026-10-13 23:39:50 | `3a240806c2d3` | 噪声面 |
| 107 | `.tmp/_cpatomic_dump_pyc_2026_09_28.py` | 468 | 2026-09-28 15:53:57 | `d7c9ac28b096` | 噪声面 |
| 108 | `.tmp/_cpatomic_keyscan_2026_09_28.py` | 3,074 | 2026-09-28 15:52:04 | `393a8d3fa68f` | 噪声面 |
| 109 | `.tmp/_cpatomic_make_fix_2026_09_28.py` | 7,796 | 2026-09-28 15:45:51 | `76c822b640a0` | 噪声面 |
| 110 | `.tmp/_cpatomic_pycache_post_2026_09_28.py` | 5,164 | 2026-09-28 15:51:22 | `171b2a31c0e1` | 噪声面 |
| 111 | `.tmp/_cpatomic_pycache_pre_2026_09_28.py` | 3,912 | 2026-09-28 15:42:15 | `b86619676bf4` | 噪声面 |
| 112 | `.tmp/_cpatomic_register_2026_09_28.json` | 29,361 | 2026-09-28 15:52:46 | `b68d7ff817bb` | 噪声面 |
| 113 | `.tmp/_cpatomic_register_2026_09_28.py` | 6,322 | 2026-09-28 15:52:32 | `98fe9fa24e80` | 噪声面 |
| 114 | `.tmp/_cpatomic_verify_2026_09_28.py` | 11,036 | 2026-09-28 15:49:14 | `85139011457c` | 噪声面 |
| 115 | `.tmp/_crosscheck_messages_35_48.py` | 1,608 | 2026-10-10 15:10:47 | `dcfe48359488` | 噪声面 |
| 116 | `.tmp/_d05_b_coincidence_checks_2026_10_10.py` | 22,078 | 2026-10-10 12:08:37 | `c1fc428d450c` | 噪声面 |
| 117 | `.tmp/_d05_caliber_2026_10_10.py` | 8,011 | 2026-10-10 12:42:22 | `65cb84529cb2` | 噪声面 |
| 118 | `.tmp/_d05_instrument_audit.py` | 5,948 | 2026-10-10 11:58:15 | `edfa99486954` | 噪声面 |
| 119 | `.tmp/_d05_s4only_2026_10_10.py` | 3,438 | 2026-10-10 12:42:55 | `802069e2c06e` | 噪声面 |
| 120 | `.tmp/_d05_three_checks_recheck_2026_10_10.py` | 11,134 | 2026-10-10 12:41:16 | `fc1201cb71e7` | 噪声面 |
| 121 | `.tmp/_d05_three_checks_recheck_out_2026_10_10.json` | 3,622 | 2026-10-10 12:41:33 | `4eb425260682` | 噪声面 |
| 122 | `.tmp/_dfam_corr_src_2026_10_12.md` | 33,471 | 2026-10-12 17:50:24 | `12da29eb102c` | 噪声面 |
| 123 | `.tmp/_diff21_anchor_drift.py` | 960 | 2026-09-28 20:17:33 | `de2a99cf1999` | 噪声面 |
| 124 | `.tmp/_docwriter_night_headers.txt` | 52,370 | 2026-10-14 01:43:30 | `729875e7999e` | 噪声面 |
| 125 | `.tmp/_docwriter_night_measure.json` | 22,679 | 2026-10-14 01:41:55 | `f5bacfac3f1c` | 噪声面 |
| 126 | `.tmp/_docwriter_q4_l117_append_block.md` | 4,857 | 2026-10-01 09:18:25 | `7c7d633047e4` | 噪声面 |
| 127 | `.tmp/_docwriter_recheck.py` | 2,374 | 2026-10-14 01:44:00 | `54b522e4e2fe` | 噪声面 |
| 128 | `.tmp/_docwriter_write_handover.py` | 49,400 | 2026-10-14 01:48:38 | `a553d705a482` | 噪声面 |
| 129 | `.tmp/_dump_dkb3_records2_2026_10_10.py` | 1,366 | 2026-10-10 10:12:37 | `e71d1e81da64` | 噪声面 |
| 130 | `.tmp/_dump_dkb3_records_2026_10_10.py` | 1,781 | 2026-10-10 10:11:13 | `144b204237bf` | 噪声面 |
| 131 | `.tmp/_dup_name_diff_content_scan2_2026_10_08.py` | 7,547 | 2026-10-08 17:21:02 | `b3fe206ef866` | 噪声面 |
| 132 | `.tmp/_dup_name_diff_content_scan_2026_10_08.py` | 4,519 | 2026-10-08 17:10:41 | `675cc3136e70` | 噪声面 |
| 133 | `.tmp/_dw_abs_scan.json` | 56,306 | 2026-10-14 15:40:27 | `5c584826ed16` | 噪声面 |
| 134 | `.tmp/_e47_docwriter_count.py` | 1,124 | 2026-09-28 15:44:30 | `33cc563b9471` | 噪声面 |
| 135 | `.tmp/_e48_apply.py` | 2,329 | 2026-09-28 16:17:15 | `d4e6f0934e5f` | 噪声面 |
| 136 | `.tmp/_e48_c1.md` | 5,039 | 2026-09-28 16:13:39 | `c2a814a90330` | 噪声面 |
| 137 | `.tmp/_e48_c2.md` | 5,966 | 2026-09-28 16:14:09 | `4d3cae4cbcc0` | 噪声面 |
| 138 | `.tmp/_e48_c3.md` | 6,563 | 2026-09-28 16:14:52 | `769c71475404` | 噪声面 |
| 139 | `.tmp/_e48_c4.md` | 21,710 | 2026-09-28 16:16:37 | `8143d01ca0e1` | 噪声面 |
| 140 | `.tmp/_e48_c5.md` | 1,686 | 2026-09-28 16:16:51 | `2f7ab971f691` | 噪声面 |
| 141 | `.tmp/_e48_docwriter_chain.py` | 2,550 | 2026-09-28 16:15:13 | `da5e16e02b7d` | 噪声面 |
| 142 | `.tmp/_e48_docwriter_enum.py` | 1,248 | 2026-09-28 16:13:06 | `80bad142f13d` | 噪声面 |
| 143 | `.tmp/_e48_docwriter_hash.py` | 2,578 | 2026-09-28 16:08:02 | `4656b3b734c5` | 噪声面 |
| 144 | `.tmp/_e48_docwriter_hash2.py` | 1,229 | 2026-09-28 16:11:52 | `9a3c5b05e29e` | 噪声面 |
| 145 | `.tmp/_e48_probe_register.py` | 873 | 2026-09-28 16:10:10 | `d92f74712dab` | 噪声面 |
| 146 | `.tmp/_e49_c1.md` | 13,607 | 2026-09-29 13:13:15 | `1e6e30d4ce4d` | 噪声面 |
| 147 | `.tmp/_e49_c2.md` | 17,872 | 2026-09-29 13:14:18 | `11beaed14ea7` | 噪声面 |
| 148 | `.tmp/_e6_alt_permp_closure_analysis_2026_10_10.py` | 2,736 | 2026-10-10 15:02:17 | `affabef74de4` | 噪声面 |
| 149 | `.tmp/_e6_alt_permp_closure_runner_2026_10_10.py` | 9,985 | 2026-10-10 14:59:42 | `9bb254aa58a9` | 噪声面 |
| 150 | `.tmp/_e6_ndjt_recompute_2026_10_10.py` | 5,064 | 2026-10-10 14:58:57 | `59c2d618305f` | 噪声面 |
| 151 | `.tmp/_e_q_doc.md` | 28,259 | 2026-10-14 14:10:48 | `71f5a0769dab` | 噪声面 |
| 152 | `.tmp/_e_q_exec.json` | 6,161 | 2026-10-14 14:07:09 | `d4bd8c92201f` | 噪声面 |
| 153 | `.tmp/_e_q_exec.txt` | 0 | 2026-10-14 14:07:09 | `e3b0c44298fc` | 噪声面 |
| 154 | `.tmp/_ea_179_domain_retest_2026_10_09.py` | 2,814 | 2026-10-09 21:39:22 | `9309e4977b22` | 噪声面 |
| 155 | `.tmp/_ecr_pa_a0_recompute_2026_10_15.py` | 8,804 | 2026-10-15 09:51:27 | `92e204d66c84` | 噪声面 |
| 156 | `.tmp/_ecr_pa_register_src_2026_10_15.md` | 15,707 | 2026-10-15 09:56:56 | `2c7c202aafec` | 噪声面 |
| 157 | `.tmp/_en_final_2026_09_28.py` | 2,369 | 2026-09-28 18:46:57 | `97a05aace5a8` | 噪声面 |
| 158 | `.tmp/_en_verify2_2026_09_28.py` | 1,870 | 2026-09-28 18:44:24 | `7e84e75cb838` | 噪声面 |
| 159 | `.tmp/_en_verify3_2026_09_28.py` | 1,638 | 2026-09-28 18:45:03 | `658292cce916` | 噪声面 |
| 160 | `.tmp/_en_verify4_2026_09_28.py` | 1,484 | 2026-09-28 18:45:30 | `7eaeb9b4ba48` | 噪声面 |
| 161 | `.tmp/_en_verify_2026_09_28.py` | 6,071 | 2026-09-28 18:43:13 | `51d9410d459b` | 噪声面 |
| 162 | `.tmp/_execswitch_verify_2026_09_28.py` | 3,501 | 2026-09-28 16:58:51 | `0814f3c2d7ab` | 噪声面 |
| 163 | `.tmp/_final.py` | 2,201 | 2026-10-16 19:34:50 | `bd48f803b81e` | 噪声面 |
| 164 | `.tmp/_final_check.py` | 1,562 | 2026-09-26 17:50:19 | `ee7f008d36cb` | 噪声面 |
| 165 | `.tmp/_final_sha.py` | 1,435 | 2026-09-28 15:25:11 | `8ea91ad82b9d` | 噪声面 |
| 166 | `.tmp/_final_verify.py` | 2,457 | 2026-10-16 23:02:32 | `88aad6650405` | 噪声面 |
| 167 | `.tmp/_frc_content.md` | 37,604 | 2026-10-17 20:30:39 | `0fd3788e2d3b` | 噪声面 |
| 168 | `.tmp/_frc_write.py` | 1,495 | 2026-10-17 20:30:49 | `1136d247a7c6` | 噪声面 |
| 169 | `.tmp/_full.py` | 2,757 | 2026-10-16 19:31:47 | `4f033025e960` | 噪声面 |
| 170 | `.tmp/_ge01_g7_register_build.py` | 33,147 | 2026-10-14 20:31:19 | `7731337a516d` | 噪声面 |
| 171 | `.tmp/_ge01_g7_register_measure.py` | 5,090 | 2026-10-14 20:28:56 | `5c3454c88a92` | 噪声面 |
| 172 | `.tmp/_gh_tree.txt` | 341,814 | 2026-10-12 14:21:54 | `823cfbb23a03` | 噪声面 |
| 173 | `.tmp/_h_census_worker.json` | 10,037,568 | 2026-10-14 00:01:18 | `22531e8519b2` | 噪声面 |
| 174 | `.tmp/_h_census_worker.py` | 5,639 | 2026-10-13 23:59:47 | `7f858d86f865` | 噪声面 |
| 175 | `.tmp/_hash21.py` | 944 | 2026-09-28 20:05:13 | `0d5335f0ac54` | 噪声面 |
| 176 | `.tmp/_inspect_10cells.py` | 2,460 | 2026-09-26 17:40:36 | `919f8f4e8ad2` | 噪声面 |
| 177 | `.tmp/_inspect_batch4_rounds.py` | 898 | 2026-09-26 17:41:44 | `bf479a2667df` | 噪声面 |
| 178 | `.tmp/_intake_cards_35_48_extract.py` | 3,416 | 2026-10-10 15:07:41 | `74cca5bda270` | 噪声面 |
| 179 | `.tmp/_iscp_dual_impl_2026_10_09.py` | 2,974 | 2026-10-09 14:43:36 | `8734f4326d5a` | 噪声面 |
| 180 | `.tmp/_item35_v3_collinear_recompute_2026_10_01.py` | 16,493 | 2026-10-01 08:55:30 | `c8d859cbb69e` | 噪声面 |
| 181 | `.tmp/_kd04_c_den_exec_2026_10_10.py` | 21,430 | 2026-10-10 11:42:44 | `419f9f691e63` | 噪声面 |
| 182 | `.tmp/_keyscan.py` | 787 | 2026-10-16 19:33:27 | `77f120aa42da` | 噪声面 |
| 183 | `.tmp/_kv3s43_diag_2026_10_09.py` | 614 | 2026-10-09 14:24:04 | `398ebf6f33e0` | 噪声面 |
| 184 | `.tmp/_lit_log.txt` | 8,733 | 2026-10-15 10:46:33 | `b062da7b654a` | 噪声面 |
| 185 | `.tmp/_m5_k5_net.json` | 92,060 | 2026-10-13 23:34:23 | `9d7fe894a26b` | 噪声面 |
| 186 | `.tmp/_m5_k5_net.py` | 3,173 | 2026-10-13 23:33:24 | `ec944f9178ea` | 噪声面 |
| 187 | `.tmp/_m5_k5_net2.json` | 952,252 | 2026-10-13 23:37:07 | `b2bc158e7499` | 噪声面 |
| 188 | `.tmp/_m5_k5_scan.json` | 9,530 | 2026-10-13 23:34:49 | `ebf1ad76dc8a` | 噪声面 |
| 189 | `.tmp/_m5_k5_scan.py` | 3,541 | 2026-10-13 23:33:23 | `f5245072750f` | 噪声面 |
| 190 | `.tmp/_m5_reaudit_archive.py` | 1,405 | 2026-10-14 10:14:40 | `54540d871fb7` | 噪声面 |
| 191 | `.tmp/_m5_reaudit_archive_out.json` | 654 | 2026-10-14 10:15:31 | `e3542ccb4d3e` | 噪声面 |
| 192 | `.tmp/_m5_reaudit_detail.py` | 2,276 | 2026-10-14 10:11:40 | `f43d192a9726` | 噪声面 |
| 193 | `.tmp/_m5_reaudit_detail.txt` | 9,214 | 2026-10-14 10:11:55 | `8c117d51fc64` | 噪声面 |
| 194 | `.tmp/_m5_reaudit_probe.py` | 4,469 | 2026-10-14 10:09:04 | `5b005dd13f95` | 噪声面 |
| 195 | `.tmp/_mk_voided_reloc_register.py` | 13,003 | 2026-10-14 00:49:59 | `7c2d2f6955d0` | 噪声面 |
| 196 | `.tmp/_n1_n2_check.py` | 1,628 | 2026-09-26 17:46:43 | `71f3f53a6eed` | 噪声面 |
| 197 | `.tmp/_ofc_s1_inventory.json` | 216,695 | 2026-10-12 11:57:41 | `c2858312798b` | 噪声面 |
| 198 | `.tmp/_ofc_s1b_inventory.json` | 336,955 | 2026-10-12 11:59:42 | `a28f35879008` | 噪声面 |
| 199 | `.tmp/_patch21_emit.py` | 17,106 | 2026-09-28 20:26:10 | `1d3c8aea6bad` | 噪声面 |
| 200 | `.tmp/_patch21_make.py` | 8,807 | 2026-09-28 20:20:05 | `b6cfdfaf80fa` | 噪声面 |
| 201 | `.tmp/_patch21_run.py` | 3,866 | 2026-09-28 20:20:37 | `6333d9256716` | 噪声面 |
| 202 | `.tmp/_pc.py` | 431 | 2026-09-26 22:16:09 | `7c59c7e80d50` | 噪声面 |
| 203 | `.tmp/_pi_card_answers_register_2026_10_17_v59.md` | 40,214 | 2026-10-17 16:53:53 | `65a67ae80d14` | 噪声面 |
| 204 | `.tmp/_pk_probe.py` | 398 | 2026-09-27 20:26:47 | `6d79ba939526` | 噪声面 |
| 205 | `.tmp/_pk_sha_scan.py` | 599 | 2026-09-29 18:32:20 | `df460eaec619` | 噪声面 |
| 206 | `.tmp/_pkf34_f3.py` | 3,068 | 2026-09-28 15:12:48 | `389b3fdecd29` | 噪声面 |
| 207 | `.tmp/_pkf34_f34.py` | 4,282 | 2026-09-28 15:19:40 | `a972a0383cf4` | 噪声面 |
| 208 | `.tmp/_pkf34_f3b.py` | 2,703 | 2026-09-28 15:14:55 | `e1bcbf3897d8` | 噪声面 |
| 209 | `.tmp/_pkf34_f4.py` | 3,958 | 2026-09-28 15:15:32 | `880a69b9cf29` | 噪声面 |
| 210 | `.tmp/_pkf34_f4b.py` | 4,401 | 2026-09-28 15:16:34 | `e97f6ee41bec` | 噪声面 |
| 211 | `.tmp/_pkf34_f4c.py` | 3,045 | 2026-09-28 15:18:35 | `c758efa2a529` | 噪声面 |
| 212 | `.tmp/_pkf34_f4d.py` | 3,686 | 2026-09-28 15:21:17 | `fb565a667edc` | 噪声面 |
| 213 | `.tmp/_pkf34_final.py` | 5,903 | 2026-09-28 15:22:31 | `4b6140aaa618` | 噪声面 |
| 214 | `.tmp/_pkf34_nd.py` | 2,537 | 2026-09-28 15:24:13 | `527883f7ebb8` | 噪声面 |
| 215 | `.tmp/_pkf34_v12.py` | 5,639 | 2026-09-28 15:23:28 | `c650b0c20eee` | 噪声面 |
| 216 | `.tmp/_postcheck_v16_alt.py` | 1,282 | 2026-09-26 16:52:45 | `4d485d7a4d91` | 噪声面 |
| 217 | `.tmp/_postcheck_v16_alt_stdout.txt` | 1,558 | 2026-09-26 16:52:55 | `f116b23fa967` | 噪声面 |
| 218 | `.tmp/_postcheck_v16_sha.py` | 1,391 | 2026-09-26 16:51:40 | `46759ba2b8e5` | 噪声面 |
| 219 | `.tmp/_pre_mod/exp_harness_pre.py` | 36,217 | 2026-10-16 16:16:29 | `d5c8d676bb5b` | 噪声面 |
| 220 | `.tmp/_precheck.py` | 2,234 | 2026-10-16 19:31:15 | `cf7f2432f616` | 噪声面 |
| 221 | `.tmp/_precheck_v15_tail.ps1` | 505 | 2026-09-26 16:50:30 | `e94d8011bbf4` | 噪声面 |
| 222 | `.tmp/_probe21.py` | 564 | 2026-09-28 20:02:53 | `5a40370032b3` | 噪声面 |
| 223 | `.tmp/_r10.py` | 1,525 | 2026-09-28 15:24:35 | `1b012cd12a00` | 噪声面 |
| 224 | `.tmp/_r1_alarm_test.py` | 2,297 | 2026-09-28 15:14:54 | `c44a09297f1a` | 噪声面 |
| 225 | `.tmp/_r2_body.md` | 63,091 | 2026-10-14 02:50:00 | `1dbe20a3ba1c` | 噪声面 |
| 226 | `.tmp/_r2_tool_01_inventory.py` | 2,498 | 2026-10-18 00:17:08 | `99ee7cb1ebae` | 噪声面 |
| 227 | `.tmp/_r2_tool_02_breakdown.py` | 2,074 | 2026-10-18 00:17:34 | `ed316d1d905e` | 噪声面 |
| 228 | `.tmp/_r2_tool_03_refindex.json` | 9,700,261 | 2026-10-18 00:20:08 | `aa05d398bb1d` | 噪声面 |
| 229 | `.tmp/_r2_tool_03_refindex.py` | 4,440 | 2026-10-18 00:19:24 | `32bd762657ba` | 噪声面 |
| 230 | `.tmp/_r2_tool_04_classes.py` | 4,920 | 2026-10-18 00:20:37 | `055797145699` | 噪声面 |
| 231 | `.tmp/_r2_tool_04b_channels.py` | 4,355 | 2026-10-18 00:21:25 | `8dc5c887150d` | 噪声面 |
| 232 | `.tmp/_r2_tool_05_dirs.py` | 2,836 | 2026-10-18 00:23:00 | `f1d5f54866f6` | 噪声面 |
| 233 | `.tmp/_r2_tool_06_pools.json` | 44,972 | 2026-10-18 00:24:14 | `a7917e01e553` | 噪声面 |
| 234 | `.tmp/_r2_tool_06_pools.py` | 4,538 | 2026-10-18 00:23:59 | `38cfc44ab456` | 噪声面 |
| 235 | `.tmp/_r2_tool_07_xferpool.py` | 3,070 | 2026-10-18 00:24:48 | `968db8e49af5` | 噪声面 |
| 236 | `.tmp/_r2_tool_08_dups.py` | 3,454 | 2026-10-18 00:25:59 | `9e2bf8865936` | 噪声面 |
| 237 | `.tmp/_r2_tool_09_plan.json` | 55,738 | 2026-10-18 00:27:10 | `333492128e31` | 噪声面 |
| 238 | `.tmp/_r2_tool_09_plan.py` | 6,517 | 2026-10-18 00:27:01 | `3e7f88cb9eb8` | 噪声面 |
| 239 | `.tmp/_r2_tool_10_plan2.py` | 8,115 | 2026-10-18 00:28:19 | `1e4c0eaf09ff` | 噪声面 |
| 240 | `.tmp/_r2_tool_11_channels.py` | 4,801 | 2026-10-18 00:30:46 | `3c8a51b1473f` | 噪声面 |
| 241 | `.tmp/_r2_tool_12_plan3.py` | 5,757 | 2026-10-18 00:32:48 | `8ab6bb0dd570` | 噪声面 |
| 242 | `.tmp/_r2_tool_13_check.py` | 2,424 | 2026-10-18 00:33:17 | `cd966d2cd422` | 噪声面 |
| 243 | `.tmp/_r2_tool_14_plan4.json` | 51,836 | 2026-10-18 00:34:56 | `b7942c0a75f1` | 噪声面 |
| 244 | `.tmp/_r2_tool_14_plan4.py` | 5,689 | 2026-10-18 00:34:47 | `97c00a613313` | 噪声面 |
| 245 | `.tmp/_r2_tool_15_gates.py` | 4,692 | 2026-10-18 00:35:32 | `71f1b4e2b0bb` | 噪声面 |
| 246 | `.tmp/_r2_tool_16_sample.json` | 56 | 2026-10-18 00:38:50 | `66f49919660b` | 噪声面 |
| 247 | `.tmp/_r2_tool_16_sample_verify.json` | 3,167 | 2026-10-18 00:39:04 | `0132123c23c8` | 噪声面 |
| 248 | `.tmp/_r2_tool_16_trashverify.py` | 3,466 | 2026-10-18 00:38:58 | `a47e89c1ed5c` | 噪声面 |
| 249 | `.tmp/_r2_tool_17_rest.json` | 8,649 | 2026-10-18 00:39:18 | `bb1d12223740` | 噪声面 |
| 250 | `.tmp/_r2_tool_18_twins.json` | 27,063 | 2026-10-18 00:39:37 | `7467783c6d4f` | 噪声面 |
| 251 | `.tmp/_r2_tool_19_trashverify.json` | 66,439 | 2026-10-18 00:47:59 | `5ff0887b086c` | 噪声面 |
| 252 | `.tmp/_r2_tool_20_xfer.json` | 66,273 | 2026-10-18 00:48:19 | `2c06c1d70839` | 噪声面 |
| 253 | `.tmp/_r2_tool_20_xfer.py` | 2,548 | 2026-10-18 00:48:12 | `2082a9a876e2` | 噪声面 |
| 254 | `.tmp/_r2_tool_21_post.json` | 949 | 2026-10-18 00:58:32 | `794217ca0f3a` | 噪声面 |
| 255 | `.tmp/_r2_tool_21_post.py` | 1,862 | 2026-10-18 00:48:34 | `660a666da351` | 噪声面 |
| 256 | `.tmp/_r2_tool_22_selfclean.json` | 464 | 2026-10-18 00:50:08 | `4e4212c74d61` | 噪声面 |
| 257 | `.tmp/_r2_tool_22_selfclean_verify.json` | 35,483 | 2026-10-18 00:50:08 | `3fc18c9d09e9` | 噪声面 |
| 258 | `.tmp/_r2_tool_23_nolink.json` | 90,951 | 2026-10-18 00:52:35 | `5accec1e55d7` | 噪声面 |
| 259 | `.tmp/_r2_tool_23_nolink.py` | 2,040 | 2026-10-18 00:52:28 | `12632e36d05f` | 噪声面 |
| 260 | `.tmp/_r2_tool_24_funcref.json` | 8,346 | 2026-10-18 00:53:27 | `74101ab98d63` | 噪声面 |
| 261 | `.tmp/_r2_tool_25_restore.json` | 392,957 | 2026-10-18 00:55:08 | `e8cabb5339c2` | 噪声面 |
| 262 | `.tmp/_r2_tool_25_restore.py` | 4,227 | 2026-10-18 00:54:42 | `fa2ee5026d9c` | 噪声面 |
| 263 | `.tmp/_r2_tool_26_genregister.py` | 20,579 | 2026-10-18 00:57:06 | `e013fac3d234` | 噪声面 |
| 264 | `.tmp/_r3_header_fix_2026_09_28.py` | 3,280 | 2026-09-28 17:24:56 | `6f8cec0fe006` | 噪声面 |
| 265 | `.tmp/_r3_verify_2026_09_28.py` | 5,494 | 2026-09-28 17:26:33 | `721e52f9d55f` | 噪声面 |
| 266 | `.tmp/_r4_cleanup_worker_keycount_2026_09_29.py` | 1,909 | 2026-09-29 14:08:03 | `ca0cbafed00b` | 噪声面 |
| 267 | `.tmp/_r4_cleanup_worker_keyscan_2026_09_29.py` | 3,561 | 2026-09-29 14:10:46 | `01e1ac2ef239` | 噪声面 |
| 268 | `.tmp/_r4_cleanup_worker_nearmiss_2026_09_29.py` | 1,382 | 2026-09-29 14:08:35 | `22336cc16500` | 噪声面 |
| 269 | `.tmp/_r4_cleanup_worker_scan_2026_09_29.py` | 2,411 | 2026-09-29 14:04:31 | `af404c489392` | 噪声面 |
| 270 | `.tmp/_r4_cleanup_worker_shape_2026_09_29.py` | 1,110 | 2026-09-29 14:08:58 | `f7f6313edce8` | 噪声面 |
| 271 | `.tmp/_r4_key_scan_2026_09_24.py` | 3,743 | 2026-09-24 18:50:23 | `c782d1a18092` | 噪声面 |
| 272 | `.tmp/_r4_key_scan_r1_files_2026_09_27.py` | 4,079 | 2026-09-27 17:07:38 | `cec4c1f3ff9c` | 噪声面 |
| 273 | `.tmp/_r5_write_register_2026_10_13.py` | 25,902 | 2026-10-14 00:31:16 | `139c8a7316db` | 噪声面 |
| 274 | `.tmp/_r6_evidence.py` | 2,525 | 2026-09-28 15:19:39 | `4de12a4f441b` | 噪声面 |
| 275 | `.tmp/_recheck_r1_run1.log` | 2,486 | 2026-09-27 17:03:26 | `80b338a0e9ad` | 噪声面 |
| 276 | `.tmp/_rj5_convention_check_2026_09_27.py` | 8,018 | 2026-09-27 17:21:32 | `5dbb93b3c5e5` | 噪声面 |
| 277 | `.tmp/_rj5_mapping_test_2026_09_27.py` | 5,968 | 2026-09-27 17:26:43 | `75ff70d87bd7` | 噪声面 |
| 278 | `.tmp/_rp4_fields.py` | 433 | 2026-10-09 14:14:54 | `1d112ab8f3b4` | 噪声面 |
| 279 | `.tmp/_rp_addendum_build_2026_10_09.py` | 30,375 | 2026-10-09 16:45:20 | `c4e8b75d656b` | 噪声面 |
| 280 | `.tmp/_rp_verify_2026_10_09.py` | 3,282 | 2026-10-09 16:46:36 | `e0adae15fc26` | 噪声面 |
| 281 | `.tmp/_rpd_neighbors_2026_10_09.py` | 1,286 | 2026-10-09 12:35:20 | `28cfa9466ea3` | 噪声面 |
| 282 | `.tmp/_rpd_reuse_strict_2026_10_09.py` | 4,746 | 2026-10-09 12:35:42 | `4557b47b7361` | 噪声面 |
| 283 | `.tmp/_rpd_verify_landed_2026_10_09.py` | 6,335 | 2026-10-09 12:38:16 | `912a2b8066f1` | 噪声面 |
| 284 | `.tmp/_rpp_deliverable_staged_2026_10_17.md` | 30,617 | 2026-10-17 22:19:34 | `7e693b27c1f7` | 噪声面 |
| 285 | `.tmp/_run2.py` | 4,366 | 2026-09-27 12:58:13 | `8acbf24342d1` | 噪声面 |
| 286 | `.tmp/_run_d4_relabel_addendum.py` | 17,550 | 2026-09-27 17:04:03 | `620eabf853af` | 噪声面 |
| 287 | `.tmp/_run_d6_addendum_2026_09_28.py` | 23,204 | 2026-09-28 13:46:23 | `e472ea36ed08` | 噪声面 |
| 288 | `.tmp/_run_d6b_addendum_2026_09_28.py` | 31,468 | 2026-09-28 14:59:58 | `f0a4e919eeaa` | 噪声面 |
| 289 | `.tmp/_run_d8_addendum_2026_09_30.py` | 107,959 | 2026-09-30 16:17:55 | `7ce330b3e5ae` | 噪声面 |
| 290 | `.tmp/_run_d8_bhalf_addendum_2026_09_30.py` | 40,576 | 2026-09-30 16:21:44 | `90fa2c443529` | 噪声面 |
| 291 | `.tmp/_run_day_inventory_table_2026_09_27.py` | 2,763 | 2026-09-27 18:06:59 | `329bf2b66422` | 噪声面 |
| 292 | `.tmp/_run_final.py` | 26,654 | 2026-09-27 13:03:49 | `75d466add5d5` | 噪声面 |
| 293 | `.tmp/_run_final_selfscan_2026_09_27.py` | 1,358 | 2026-09-27 18:10:35 | `cf5c5c7684bb` | 噪声面 |
| 294 | `.tmp/_run_frozen_0touch_verify_2026_09_27.py` | 2,309 | 2026-09-27 18:05:45 | `48246f41e7d3` | 噪声面 |
| 295 | `.tmp/_run_recheck_r1.py` | 34,895 | 2026-09-27 17:09:39 | `a76ec3a2340e` | 噪声面 |
| 296 | `.tmp/_run_result_v3.py` | 3,304 | 2026-09-27 12:58:01 | `83cd4414f404` | 噪声面 |
| 297 | `.tmp/_run_v3r1_relabel.py` | 30,875 | 2026-09-27 17:46:57 | `55d06ce42b3d` | 噪声面 |
| 298 | `.tmp/_s3_f1_loader_fix_recompute_2026_10_08.py` | 21,231 | 2026-10-08 16:57:51 | `e39e4ae7d6ed` | 噪声面 |
| 299 | `.tmp/_s3_faces.txt` | 72 | 2026-10-17 21:08:16 | `a99b4dea153d` | 噪声面 |
| 300 | `.tmp/_s3_paths.txt` | 1,809 | 2026-10-17 21:09:46 | `1e60e98469fd` | 噪声面 |
| 301 | `.tmp/_s3_probe2.txt` | 956 | 2026-10-17 21:08:16 | `623d848bab37` | 噪声面 |
| 302 | `.tmp/_s3_probe3.txt` | 88 | 2026-10-17 21:09:46 | `865f7971b4c2` | 噪声面 |
| 303 | `.tmp/_s3_probe_out.txt` | 1,358 | 2026-10-17 21:07:28 | `9071c5ea6c2f` | 噪声面 |
| 304 | `.tmp/_s4_freeze_count_crosscheck2_2026_10_09.py` | 3,920 | 2026-10-09 14:12:07 | `15fa4d155fc9` | 噪声面 |
| 305 | `.tmp/_s4_freeze_count_crosscheck3_2026_10_09.py` | 4,041 | 2026-10-09 14:12:34 | `ee420dfd57e6` | 噪声面 |
| 306 | `.tmp/_s4_freeze_count_crosscheck_2026_10_09.py` | 3,463 | 2026-10-09 14:11:12 | `856e6ab48dae` | 噪声面 |
| 307 | `.tmp/_s4_seedprime_seq_t1_supplement_2026_10_11.py` | 31,705 | 2026-10-11 00:50:21 | `3a9db2126e4f` | 噪声面 |
| 308 | `.tmp/_s4_topup_addendum_builder_2026_10_09.py` | 21,122 | 2026-10-09 13:53:01 | `b9987c7a8d5f` | 噪声面 |
| 309 | `.tmp/_s4_tree_construct_exec_2026_10_10.py` | 34,265 | 2026-10-10 09:51:36 | `4cbd10b61aae` | 噪声面 |
| 310 | `.tmp/_s4f2_dbg.py` | 431 | 2026-10-09 15:33:21 | `5159c9c30180` | 噪声面 |
| 311 | `.tmp/_s4f2_face_probe_2026_10_09.py` | 14,896 | 2026-10-09 15:33:39 | `62e04248d122` | 噪声面 |
| 312 | `.tmp/_s4f2_patch.py` | 2,740 | 2026-10-09 15:30:03 | `b79a7073099d` | 噪声面 |
| 313 | `.tmp/_s4f2_patch2.py` | 421 | 2026-10-09 15:31:07 | `045bd90b237a` | 噪声面 |
| 314 | `.tmp/_s4f2_patch3.py` | 815 | 2026-10-09 15:31:52 | `6d57ff4ce76c` | 噪声面 |
| 315 | `.tmp/_s4f2_patch4.py` | 565 | 2026-10-09 15:32:23 | `7d85756a841d` | 噪声面 |
| 316 | `.tmp/_s4f2_scanner_selftest.py` | 1,819 | 2026-10-09 15:31:23 | `5b6fd262f785` | 噪声面 |
| 317 | `.tmp/_s4fs_auxdate_2026_10_09.py` | 1,877 | 2026-10-09 15:29:05 | `637e936d8bc7` | 噪声面 |
| 318 | `.tmp/_s4fs_selfreport_2026_10_09.py` | 432 | 2026-10-09 15:32:06 | `485071c7dd5e` | 噪声面 |
| 319 | `.tmp/_s4fs_yitable_2026_10_09.py` | 1,634 | 2026-10-09 15:29:34 | `2bf7fd0ef5dc` | 噪声面 |
| 320 | `.tmp/_s4oq_addendum_struct_2026_10_09.py` | 843 | 2026-10-09 14:25:17 | `67652acdf681` | 噪声面 |
| 321 | `.tmp/_s4oq_build_baseline_2026_10_09.py` | 3,501 | 2026-10-09 13:29:27 | `3cf28fe89611` | 噪声面 |
| 322 | `.tmp/_s4oq_build_draft_2026_10_09.py` | 8,719 | 2026-10-09 14:28:47 | `0797d19dcaf3` | 噪声面 |
| 323 | `.tmp/_s4oq_cellmap_2026_10_09.py` | 1,734 | 2026-10-09 13:30:29 | `c07589f292e1` | 噪声面 |
| 324 | `.tmp/_s4oq_final_verify_2026_10_09.py` | 959 | 2026-10-09 14:31:04 | `944a4f7006c8` | 噪声面 |
| 325 | `.tmp/_s4oq_forward_2026_10_09.py` | 3,482 | 2026-10-09 14:28:05 | `43e72c62587d` | 噪声面 |
| 326 | `.tmp/_s4oq_grid_cmp_2026_10_09.py` | 1,601 | 2026-10-09 14:26:50 | `f00865587d6a` | 噪声面 |
| 327 | `.tmp/_s4oq_grid_diag_2026_10_09.py` | 1,553 | 2026-10-09 14:26:34 | `082e8b8b7bc4` | 噪声面 |
| 328 | `.tmp/_s4oq_grid_recompute_2026_10_09.py` | 2,394 | 2026-10-09 14:26:19 | `afb613f5ced1` | 噪声面 |
| 329 | `.tmp/_s4oq_keyscan_2026_10_09.py` | 573 | 2026-10-09 13:29:42 | `c9f94c812f7f` | 噪声面 |
| 330 | `.tmp/_s4oq_recompute_2026_10_09.py` | 3,202 | 2026-10-09 14:29:39 | `07cdec653345` | 噪声面 |
| 331 | `.tmp/_s4oq_reuse_check_2026_10_09.py` | 6,712 | 2026-10-09 13:29:55 | `952c76c5b103` | 噪声面 |
| 332 | `.tmp/_s4oq_reuse_v2_2026_10_09.py` | 6,293 | 2026-10-09 13:30:18 | `bc0f200edd1e` | 噪声面 |
| 333 | `.tmp/_s4oq_skel_2026_10_09.py` | 466 | 2026-10-09 14:27:26 | `73fc780b4849` | 噪声面 |
| 334 | `.tmp/_s4oq_slug_opt_2026_10_09.py` | 4,636 | 2026-10-09 13:30:50 | `77d696b1690d` | 噪声面 |
| 335 | `.tmp/_s4oq_slug_search2_2026_10_09.py` | 5,258 | 2026-10-09 13:31:17 | `fe6f7044ec4e` | 噪声面 |
| 336 | `.tmp/_s4oq_variants_2026_10_09.py` | 1,233 | 2026-10-09 14:27:35 | `ccbbb499e19a` | 噪声面 |
| 337 | `.tmp/_s4oq_verify_addendum_2026_10_09.py` | 2,252 | 2026-10-09 14:29:27 | `419c15a7a2c5` | 噪声面 |
| 338 | `.tmp/_s4oq_write_addendum_2026_10_09.py` | 11,886 | 2026-10-09 14:29:16 | `63e61afa6517` | 噪声面 |
| 339 | `.tmp/_s4td_cell_map_2026_10_09.py` | 3,642 | 2026-10-09 10:57:41 | `6665669d858d` | 噪声面 |
| 340 | `.tmp/_s4td_floor_bound_2026_10_09.py` | 4,378 | 2026-10-09 10:57:16 | `ad95b6d5e9b9` | 噪声面 |
| 341 | `.tmp/_s4td_reuse_and_bound_2026_10_09.py` | 8,765 | 2026-10-09 10:56:36 | `af6fdc892f60` | 噪声面 |
| 342 | `.tmp/_s4td_slug_search_2026_10_09.py` | 4,657 | 2026-10-09 10:55:52 | `ce5529ec7516` | 噪声面 |
| 343 | `.tmp/_s5dp_five_lines_runner_third_2026_10_11.py` | 31,138 | 2026-10-11 18:12:11 | `9de3c08e3863` | 噪声面 |
| 344 | `.tmp/_sensitivity.py` | 5,954 | 2026-09-26 17:47:02 | `8aacafa48f9c` | 噪声面 |
| 345 | `.tmp/_sha12_check.ps1` | 697 | 2026-09-26 17:24:02 | `a4bfec107a77` | 噪声面 |
| 346 | `.tmp/_sha12_check2.ps1` | 691 | 2026-09-26 17:25:01 | `3e9174fb1e03` | 噪声面 |
| 347 | `.tmp/_stage3_r2_criteria_freeze_2026_10_18.md` | 9,971 | 2026-10-18 00:36:42 | `885ec7fb04dd` | 噪声面 |
| 348 | `.tmp/_strict3_writer_2026_10_17.py` | 41,981 | 2026-10-17 18:28:07 | `2efbf49ae4fe` | 噪声面 |
| 349 | `.tmp/_t15_inspect.py` | 2,728 | 2026-09-25 00:42:09 | `9877c9536e33` | 噪声面 |
| 350 | `.tmp/_t15_inspect2.py` | 1,942 | 2026-09-25 00:42:27 | `9a6b5bb328aa` | 噪声面 |
| 351 | `.tmp/_t15_inspect3.py` | 1,890 | 2026-09-25 00:43:08 | `d423ca72cb3c` | 噪声面 |
| 352 | `.tmp/_t15_inspect4.py` | 2,756 | 2026-09-25 00:43:48 | `069b7562f463` | 噪声面 |
| 353 | `.tmp/_t15_inspect5.py` | 2,712 | 2026-09-25 00:44:00 | `977753c193d2` | 噪声面 |
| 354 | `.tmp/_t15_inspect6.py` | 1,234 | 2026-09-25 00:44:53 | `eba3a29f6264` | 噪声面 |
| 355 | `.tmp/_t15_inspect7.py` | 3,880 | 2026-09-25 00:45:14 | `78dafdf124f7` | 噪声面 |
| 356 | `.tmp/_t15_percell.py` | 596 | 2026-09-25 00:45:42 | `c035476cfb41` | 噪声面 |
| 357 | `.tmp/_t15_probe_log.json` | 718 | 2026-09-24 23:58:16 | `94444963ff77` | 噪声面 |
| 358 | `.tmp/_t15_records.json` | 96,443 | 2026-09-25 00:41:37 | `8014af0e2b79` | 噪声面 |
| 359 | `.tmp/_t15_update_result.py` | 9,226 | 2026-09-25 00:44:30 | `ad66f242c6a1` | 噪声面 |
| 360 | `.tmp/_t15r2_inspect.py` | 3,730 | 2026-09-26 16:47:14 | `c58dc90fd86a` | 噪声面 |
| 361 | `.tmp/_t15r2_verify.py` | 6,737 | 2026-09-26 17:16:23 | `5267b4dee7dc` | 噪声面 |
| 362 | `.tmp/_t1_exp2_c_driver_2026_10_09.py` | 2,898 | 2026-10-09 22:22:58 | `5d474b7ceada` | 噪声面 |
| 363 | `.tmp/_t1_exp2_c_records.json` | 6,277,328 | 2026-10-10 02:31:55 | `f53681c7569a` | 噪声面 |
| 364 | `.tmp/_t1_exp2_calib_2026_10_09.json` | 611 | 2026-10-09 22:20:17 | `de09d4ee3721` | 噪声面 |
| 365 | `.tmp/_t1_exp2_d_readings.json` | 3,991 | 2026-10-09 22:45:37 | `2315f6823011` | 噪声面 |
| 366 | `.tmp/_t1_exp2_d_records.json` | 488,395 | 2026-10-09 22:44:11 | `aadba0c4f952` | 噪声面 |
| 367 | `.tmp/_t1_exp2_probe_log.json` | 760 | 2026-10-09 22:19:48 | `c6478415e2bf` | 噪声面 |
| 368 | `.tmp/_t1_exp2_selfcert.json` | 6,780 | 2026-10-09 22:19:29 | `d929eb9ae0b8` | 噪声面 |
| 369 | `.tmp/_t1_gap_domain_sweep_2026_10_01.py` | 2,502 | 2026-10-01 14:37:27 | `74d1ed439442` | 噪声面 |
| 370 | `.tmp/_t1_gap_postwrite_verify_2026_10_01.py` | 5,666 | 2026-10-01 14:40:48 | `33b4108f14a1` | 噪声面 |
| 371 | `.tmp/_t1_gap_snapshot_2026_10_01.py` | 2,588 | 2026-10-01 14:38:44 | `fd53258bd16f` | 噪声面 |
| 372 | `.tmp/_t1_qwen_temp_sweep_decomposition.py` | 1,981 | 2026-10-09 11:16:56 | `97a6520c7105` | 噪声面 |
| 373 | `.tmp/_t1_qwen_temp_sweep_dump_readings.py` | 1,137 | 2026-10-09 11:16:31 | `7e06567afc2a` | 噪声面 |
| 374 | `.tmp/_t1_qwen_temp_sweep_probe_log.json` | 445 | 2026-10-09 10:23:35 | `b5e4151af490` | 噪声面 |
| 375 | `.tmp/_t1_qwen_temp_sweep_r2_probe_log.json` | 739 | 2026-10-09 16:59:00 | `5182f6fdd9ef` | 噪声面 |
| 376 | `.tmp/_t1_qwen_temp_sweep_r2_records.json` | 1,795,870 | 2026-10-09 18:03:12 | `bb511e7b0baf` | 噪声面 |
| 377 | `.tmp/_t1_qwen_temp_sweep_r2_selfcert.json` | 6,353 | 2026-10-09 16:58:49 | `124051b56295` | 噪声面 |
| 378 | `.tmp/_t1_qwen_temp_sweep_readings.json` | 11,013 | 2026-10-09 11:15:36 | `e5e8f024e42e` | 噪声面 |
| 379 | `.tmp/_t1_qwen_temp_sweep_records.json` | 96,866 | 2026-10-09 11:15:00 | `5b51af62c640` | 噪声面 |
| 380 | `.tmp/_t1_qwen_temp_sweep_selfcert.json` | 3,866 | 2026-10-09 10:22:42 | `91c2505deef3` | 噪声面 |
| 381 | `.tmp/_t1_r2_calib_max_tokens_2026_10_09.json` | 3,305 | 2026-10-09 16:55:16 | `3f35aede29f6` | 噪声面 |
| 382 | `.tmp/_t1_r2_calib_max_tokens_2026_10_09.py` | 6,120 | 2026-10-09 16:52:24 | `7bbb0de0c00f` | 噪声面 |
| 383 | `.tmp/_t1_r2_run_driver_2026_10_09.py` | 2,749 | 2026-10-09 16:59:17 | `b71f4916bee1` | 噪声面 |
| 384 | `.tmp/_t1_r2_verify_2026_10_09.py` | 4,018 | 2026-10-09 16:59:55 | `3ce6d45cfbf7` | 噪声面 |
| 385 | `.tmp/_t1_verdict_probe_readonly.txt` | 4,655 | 2026-10-09 11:49:48 | `0e2df9ca7ab2` | 噪声面 |
| 386 | `.tmp/_t2_t3_lit_search.py` | 5,695 | 2026-10-15 10:44:35 | `0829d37e0cd8` | 噪声面 |
| 387 | `.tmp/_t2_t3_lit_search2.py` | 4,946 | 2026-10-15 10:46:58 | `c0caa8ba29f1` | 噪声面 |
| 388 | `.tmp/_t2_t3_lit_search2_out.json` | 29,596 | 2026-10-15 10:47:49 | `13ffff0d0b28` | 噪声面 |
| 389 | `.tmp/_t2_t3_lit_search_out.json` | 26,588 | 2026-10-15 10:46:33 | `cc70fac3d81b` | 噪声面 |
| 390 | `.tmp/_t2_t3_llm_probe.py` | 4,544 | 2026-10-15 10:42:47 | `5561f7af5662` | 噪声面 |
| 391 | `.tmp/_t2_t3_llm_probe_out.json` | 5,331 | 2026-10-15 10:43:15 | `993477af77db` | 噪声面 |
| 392 | `.tmp/_t2_t3_prex_a_route.py` | 10,166 | 2026-10-15 10:41:33 | `c25af5d2966b` | 噪声面 |
| 393 | `.tmp/_t2_t3_prex_a_route2.py` | 5,850 | 2026-10-15 10:42:24 | `0c44afba463a` | 噪声面 |
| 394 | `.tmp/_t2_t3_prex_a_route2_out.json` | 6,949 | 2026-10-15 10:42:30 | `63f37ba943c1` | 噪声面 |
| 395 | `.tmp/_t2_t3_prex_a_route_out.json` | 22,640 | 2026-10-15 10:41:50 | `3cad087a69c3` | 噪声面 |
| 396 | `.tmp/_tail3_atomic_landing_check_2026_09_29.py` | 2,699 | 2026-09-29 11:23:08 | `5c19cf8f29fb` | 噪声面 |
| 397 | `.tmp/_tail3_atomic_make_2026_09_29.py` | 17,272 | 2026-09-29 11:12:32 | `94d57549533b` | 噪声面 |
| 398 | `.tmp/_tail3_atomic_refs_2026_09_29.py` | 2,636 | 2026-09-29 11:18:36 | `4e8ea9bea948` | 噪声面 |
| 399 | `.tmp/_tail3_atomic_verify_2026_09_29.py` | 21,338 | 2026-09-29 11:17:43 | `8d12c9c9cb2d` | 噪声面 |
| 400 | `.tmp/_tail_only.py` | 436 | 2026-09-26 16:53:03 | `cf3bbd24b401` | 噪声面 |
| 401 | `.tmp/_trae_audit_part1.py` | 5,510 | 2026-09-28 15:16:16 | `ac67b341b56b` | 噪声面 |
| 402 | `.tmp/_trae_audit_part2.py` | 3,632 | 2026-09-28 15:16:42 | `9faaa564c3bc` | 噪声面 |
| 403 | `.tmp/_trae_audit_part3.py` | 8,617 | 2026-09-28 15:17:48 | `f4c994004311` | 噪声面 |
| 404 | `.tmp/_trae_audit_part3b.py` | 7,662 | 2026-09-28 15:18:57 | `c1a9a6c3c17a` | 噪声面 |
| 405 | `.tmp/_trae_audit_part4.py` | 7,173 | 2026-09-28 15:22:52 | `bc8d4721bf3b` | 噪声面 |
| 406 | `.tmp/_u_recalc.py` | 1,852 | 2026-10-16 19:30:48 | `59e57f08d2b9` | 噪声面 |
| 407 | `.tmp/_v412_contrib.py` | 1,040 | 2026-10-09 09:57:19 | `1085411b4896` | 噪声面 |
| 408 | `.tmp/_v412_material_scan.py` | 627 | 2026-10-09 09:55:00 | `f3493907cbe2` | 噪声面 |
| 409 | `.tmp/_v412_unique_scan.py` | 1,300 | 2026-10-09 09:57:37 | `b2e381f09828` | 噪声面 |
| 410 | `.tmp/_v5_c5_b_clause4_consistency_check.py` | 6,528 | 2026-09-29 13:42:09 | `56ad3329a3c7` | 噪声面 |
| 411 | `.tmp/_v5_c5_b_fetch_raw_embeddings.py` | 9,476 | 2026-09-29 13:39:27 | `8e4f2ae63de3` | 噪声面 |
| 412 | `.tmp/_v5_c5_b_fix_readings_2026_10_01.py` | 12,014 | 2026-10-01 09:24:51 | `191efa7fe0b6` | 噪声面 |
| 413 | `.tmp/_v5_item21_anchor_driver.py` | 5,401 | 2026-09-28 20:00:07 | `cb14f672dd1e` | 噪声面 |
| 414 | `.tmp/_v5_loadcorpus_verify_2026_09_29.py` | 8,798 | 2026-09-29 13:38:56 | `564e3575ab1d` | 噪声面 |
| 415 | `.tmp/_v5_qwen_retry_candidates_20260929.py` | 1,689 | 2026-09-29 11:09:26 | `f42600827cc3` | 噪声面 |
| 416 | `.tmp/_v5_qwen_retry_introspect_20260929.py` | 3,149 | 2026-09-29 11:08:54 | `117b64fc1d5b` | 噪声面 |
| 417 | `.tmp/_verdict_keeper_sha_helper.ps1` | 679 | 2026-09-25 01:28:00 | `bc11b03d3b84` | 噪声面 |
| 418 | `.tmp/_verify_d8_addendum_2026_09_30.py` | 4,900 | 2026-09-30 16:18:13 | `28de8c99c054` | 噪声面 |
| 419 | `.tmp/_verify_intake_supplement_6.py` | 3,678 | 2026-10-10 15:10:32 | `1fbb1bd1db6c` | 噪声面 |
| 420 | `.tmp/_verify_r32_card_2026_10_10.py` | 631 | 2026-10-10 10:30:11 | `61f99fc5fdb9` | 噪声面 |
| 421 | `.tmp/_verify_tail.py` | 733 | 2026-09-26 16:52:11 | `23198a6a0a9b` | 噪声面 |
| 422 | `.tmp/_verify_two_pieces_2026_09_30.py` | 4,739 | 2026-09-30 16:22:07 | `509afa876df0` | 噪声面 |
| 423 | `.tmp/_vk_pv02_recheck_a.py` | 4,188 | 2026-10-09 13:58:44 | `37d55bf0fba6` | 噪声面 |
| 424 | `.tmp/_vk_pv02_recheck_b.py` | 1,646 | 2026-10-09 13:59:19 | `fe0f10e38bb3` | 噪声面 |
| 425 | `.tmp/_vk_pv02_recheck_c.py` | 2,397 | 2026-10-09 13:59:48 | `7d35b715f8e2` | 噪声面 |
| 426 | `.tmp/_vk_pv02_recheck_d.py` | 982 | 2026-10-09 14:00:06 | `7ae7ed6bcd8a` | 噪声面 |
| 427 | `.tmp/_vk_pv02_recheck_e.py` | 1,742 | 2026-10-09 14:00:32 | `d925e60c1d3c` | 噪声面 |
| 428 | `.tmp/_vk_pv02_recheck_f.py` | 1,522 | 2026-10-09 14:00:45 | `c2e298ccebc6` | 噪声面 |
| 429 | `.tmp/_vk_pv02_recheck_g.py` | 2,269 | 2026-10-09 14:00:59 | `f237e1d2715f` | 噪声面 |
| 430 | `.tmp/_vk_q.py` | 519 | 2026-10-10 10:57:23 | `67364902116c` | 噪声面 |
| 431 | `.tmp/_vk_q2.py` | 540 | 2026-10-10 10:57:35 | `d5759d40dc43` | 噪声面 |
| 432 | `.tmp/_vk_q3.py` | 612 | 2026-10-10 10:57:46 | `a00cd309205f` | 噪声面 |
| 433 | `.tmp/_vk_q4.py` | 784 | 2026-10-10 10:58:01 | `defc3c53b7df` | 噪声面 |
| 434 | `.tmp/_vk_q5.py` | 1,246 | 2026-10-10 10:58:17 | `7b95307225ba` | 噪声面 |
| 435 | `.tmp/_vk_q6.py` | 811 | 2026-10-10 10:59:49 | `7da34dd24eb0` | 噪声面 |
| 436 | `.tmp/_vk_q7.py` | 1,331 | 2026-10-10 19:37:27 | `a6c525f88f11` | 噪声面 |
| 437 | `.tmp/_vk_q8.py` | 1,025 | 2026-10-10 19:37:42 | `5a81e5558c72` | 噪声面 |
| 438 | `.tmp/_vk_s4_topup_intake_recheck_2026_10_09.py` | 6,678 | 2026-10-09 13:58:59 | `a1d8047f1833` | 噪声面 |
| 439 | `.tmp/_vk_s4_topup_intake_recheck_2026_10_09.txt` | 7,098 | 2026-10-09 13:59:08 | `683501b8fb41` | 噪声面 |
| 440 | `.tmp/_w1_collect.py` | 19,559 | 2026-10-16 11:53:08 | `7c3155b2c370` | 噪声面 |
| 441 | `.tmp/_w1_drift_write.py` | 16,560 | 2026-10-16 11:55:50 | `44e026ae190d` | 噪声面 |
| 442 | `.tmp/_w1_freeze_write.py` | 24,351 | 2026-10-16 11:52:25 | `97211806b0d0` | 噪声面 |
| 443 | `.tmp/_w1_phaseB_write.py` | 31,303 | 2026-10-16 11:58:55 | `4e85afe94966` | 噪声面 |
| 444 | `.tmp/_w1_verify_final.py` | 7,944 | 2026-10-16 11:59:35 | `040c35e21bf2` | 噪声面 |
| 445 | `.tmp/_w5_9model_merge_2026_10_09.py` | 18,475 | 2026-10-09 12:08:13 | `afa52e90f332` | 噪声面 |
| 446 | `.tmp/_worker_write_ge01_unblock_progress.py` | 26,125 | 2026-10-14 14:13:26 | `7c18f854316c` | 噪声面 |
| 447 | `.tmp/_write_canonical_register.py` | 24,636 | 2026-10-14 14:09:17 | `867acc46aff9` | 噪声面 |
| 448 | `.tmp/_write_eps_grid_design.py` | 38,246 | 2026-10-14 00:13:04 | `df37b02f1c0f` | 噪声面 |
| 449 | `.tmp/_write_kd1.py` | 796 | 2026-10-17 19:23:16 | `7dff16b36a84` | 噪声面 |
| 450 | `.tmp/_write_predelete_caliber_draft.py` | 32,826 | 2026-10-17 11:07:54 | `82d7f9c628b6` | 噪声面 |
| 451 | `.tmp/af1_write.py` | 43,912 | 2026-10-17 22:01:21 | `f73224fcc6f3` | 噪声面 |
| 452 | `.tmp/af25_probe_a2_faceC.py` | 3,256 | 2026-10-17 22:28:04 | `dff12350bc1e` | 噪声面 |
| 453 | `.tmp/af25_probe_a2_out.txt` | 8,336 | 2026-10-17 22:28:08 | `29da375fa3f5` | 噪声面 |
| 454 | `.tmp/af25_probe_a_faceC.py` | 1,651 | 2026-10-17 22:27:29 | `c940c09aa738` | 噪声面 |
| 455 | `.tmp/af25_probe_a_out.txt` | 26,671 | 2026-10-17 22:27:35 | `e215b6329312` | 噪声面 |
| 456 | `.tmp/af25_probe_b2_facebeta.py` | 4,012 | 2026-10-17 22:28:59 | `fa728068bd6b` | 噪声面 |
| 457 | `.tmp/af25_probe_b2_out.txt` | 25,781 | 2026-10-17 22:29:03 | `0baba808d1b9` | 噪声面 |
| 458 | `.tmp/af25_probe_b_facebeta.py` | 3,665 | 2026-10-17 22:28:42 | `09a2765c4a80` | 噪声面 |
| 459 | `.tmp/af25_probe_b_out.txt` | 1,653 | 2026-10-17 22:28:47 | `871304ed72e8` | 噪声面 |
| 460 | `.tmp/af25_probe_c_full.py` | 6,472 | 2026-10-17 22:29:46 | `241a7353cfa0` | 噪声面 |
| 461 | `.tmp/af25_probe_c_out.txt` | 8,161 | 2026-10-17 22:29:52 | `ded64ecdf8a8` | 噪声面 |
| 462 | `.tmp/af25_stage.md` | 48,208 | 2026-10-17 22:33:15 | `b3c45b4e2ec0` | 噪声面 |
| 463 | `.tmp/af25_verify.out.txt` | 348 | 2026-10-17 22:33:29 | `1ec19034e29b` | 噪声面 |
| 464 | `.tmp/af25_verify.py` | 1,039 | 2026-10-17 22:33:23 | `717ba31e9dde` | 噪声面 |
| 465 | `.tmp/af25_write.py` | 564 | 2026-10-17 22:33:19 | `16367c426966` | 噪声面 |
| 466 | `.tmp/anch.py` | 1,484 | 2026-10-16 10:56:45 | `c05693efbb30` | 噪声面 |
| 467 | `.tmp/anch_v4_build.py` | 7,175 | 2026-10-16 20:18:44 | `adcae459701a` | 噪声面 |
| 468 | `.tmp/anch_v4_build_measurements.json` | 2,315 | 2026-10-16 20:19:51 | `5708226b943f` | 噪声面 |
| 469 | `.tmp/anch_v4_probe.py` | 2,662 | 2026-10-16 20:09:29 | `f47af093e3aa` | 噪声面 |
| 470 | `.tmp/archive_survey_agg.py` | 1,350 | 2026-10-17 11:27:16 | `ad3266a95dcb` | 噪声面 |
| 471 | `.tmp/archive_survey_bname.py` | 3,273 | 2026-10-17 11:30:33 | `7b49ea12862a` | 噪声面 |
| 472 | `.tmp/archive_survey_census.py` | 666 | 2026-10-17 11:38:55 | `0c4c92856779` | 噪声面 |
| 473 | `.tmp/archive_survey_census2.py` | 780 | 2026-10-17 11:39:09 | `2863f5edca41` | 噪声面 |
| 474 | `.tmp/archive_survey_cls.py` | 3,222 | 2026-10-17 11:30:00 | `af5ea6451daa` | 噪声面 |
| 475 | `.tmp/archive_survey_delta.py` | 2,418 | 2026-10-17 11:31:50 | `d93933439479` | 噪声面 |
| 476 | `.tmp/archive_survey_detail.py` | 2,037 | 2026-10-17 11:30:18 | `6f3a49063ed9` | 噪声面 |
| 477 | `.tmp/archive_survey_detail2.py` | 1,082 | 2026-10-17 11:31:33 | `cb14f491205a` | 噪声面 |
| 478 | `.tmp/archive_survey_dup2.py` | 1,173 | 2026-10-17 11:38:31 | `a605d5bee2da` | 噪声面 |
| 479 | `.tmp/archive_survey_final.py` | 4,476 | 2026-10-17 11:36:20 | `fb702d72ace1` | 噪声面 |
| 480 | `.tmp/archive_survey_growth.py` | 965 | 2026-10-17 11:32:12 | `2991633f9220` | 噪声面 |
| 481 | `.tmp/archive_survey_inventory.json` | 13,468,808 | 2026-10-17 11:27:05 | `ba67c25d9bc0` | 噪声面 |
| 482 | `.tmp/archive_survey_junk.py` | 2,388 | 2026-10-17 11:27:49 | `b2de070ee306` | 噪声面 |
| 483 | `.tmp/archive_survey_logs.py` | 1,057 | 2026-10-17 11:37:24 | `11de1121d9dd` | 噪声面 |
| 484 | `.tmp/archive_survey_outdupe.json` | 124,763 | 2026-10-17 11:36:01 | `2d34b098cd00` | 噪声面 |
| 485 | `.tmp/archive_survey_outdupe.py` | 2,049 | 2026-10-17 11:35:33 | `1bb8456d7b2a` | 噪声面 |
| 486 | `.tmp/archive_survey_overlap.py` | 2,656 | 2026-10-17 11:38:03 | `c796220a3581` | 噪声面 |
| 487 | `.tmp/archive_survey_refcov.py` | 4,130 | 2026-10-17 11:29:37 | `aa3ebf601719` | 噪声面 |
| 488 | `.tmp/archive_survey_refmatch.py` | 804 | 2026-10-17 11:29:11 | `ade2e0ddaeee` | 噪声面 |
| 489 | `.tmp/archive_survey_refs.json` | 37,192 | 2026-10-17 11:29:01 | `6baf07bf6fb7` | 噪声面 |
| 490 | `.tmp/archive_survey_refs.py` | 2,325 | 2026-10-17 11:28:55 | `8af591a26eef` | 噪声面 |
| 491 | `.tmp/archive_survey_scan.py` | 2,289 | 2026-10-17 11:25:02 | `d7f44430a18d` | 噪声面 |
| 492 | `.tmp/archive_survey_table.py` | 3,283 | 2026-10-17 11:37:44 | `1a55e3399ece` | 噪声面 |
| 493 | `.tmp/archive_survey_temp.py` | 3,230 | 2026-10-17 11:28:14 | `cc408de66a5c` | 噪声面 |
| 494 | `.tmp/archive_survey_temp2.py` | 2,823 | 2026-10-17 11:28:34 | `5f6559c1502c` | 噪声面 |
| 495 | `.tmp/archive_survey_xcheck.py` | 859 | 2026-10-17 11:39:22 | `2bfe5686b4a5` | 噪声面 |
| 496 | `.tmp/archive_survey_xcheck2.py` | 617 | 2026-10-17 11:39:35 | `a8a38a3163c6` | 噪声面 |
| 497 | `.tmp/archive_survey_xcheck3.py` | 463 | 2026-10-17 11:39:52 | `5f73ca212e96` | 噪声面 |
| 498 | `.tmp/archive_survey_xcheck4.py` | 699 | 2026-10-17 11:40:04 | `fa5e11991277` | 噪声面 |
| 499 | `.tmp/body_relabel.md` | 8,672 | 2026-10-14 22:09:33 | `2660d5ea717d` | 噪声面 |
| 500 | `.tmp/body_v6_effect.md` | 15,467 | 2026-10-14 22:09:01 | `d79637fee0ef` | 噪声面 |
| 501 | `.tmp/card_reloc_final_verify.py` | 3,310 | 2026-10-17 17:03:04 | `428af8319c91` | 噪声面 |
| 502 | `.tmp/card_reloc_m1_refscan_2026_10_17.json` | 75,250 | 2026-10-17 16:57:42 | `d5b976ed9a22` | 噪声面 |
| 503 | `.tmp/card_reloc_m1_scan.py` | 8,359 | 2026-10-17 16:57:29 | `d35fc23909a1` | 噪声面 |
| 504 | `.tmp/card_reloc_m2_mapping.py` | 12,730 | 2026-10-17 17:01:54 | `566a24c5936b` | 噪声面 |
| 505 | `.tmp/card_reloc_m345_move.py` | 5,292 | 2026-10-17 16:59:08 | `29b9cc61e3e4` | 噪声面 |
| 506 | `.tmp/card_reloc_m45_move_result_2026_10_17.json` | 3,615 | 2026-10-17 16:59:16 | `bf4d1abbd005` | 噪声面 |
| 507 | `.tmp/card_reloc_m67_register.py` | 22,968 | 2026-10-17 17:02:57 | `1c2c4b4f1066` | 噪声面 |
| 508 | `.tmp/card_reloc_selfreport_check.py` | 1,411 | 2026-10-17 17:01:37 | `addc678b699c` | 噪声面 |
| 509 | `.tmp/census.py` | 1,084 | 2026-10-16 10:57:59 | `b9eb39229abf` | 噪声面 |
| 510 | `.tmp/census2.py` | 673 | 2026-10-16 10:58:14 | `01468767b8cb` | 噪声面 |
| 511 | `.tmp/cg_write_2026_10_17.py` | 27,209 | 2026-10-17 16:25:14 | `731d2783d469` | 噪声面 |
| 512 | `.tmp/claude_spotcheck.py` | 4,136 | 2026-09-30 21:45:51 | `a78755b356b9` | 噪声面 |
| 513 | `.tmp/cleanup511_manifest_2026_10_17.json` | 1,754,609 | 2026-10-17 10:13:01 | `b7093a701856` | 噪声面 |
| 514 | `.tmp/collision_survey_diff.py` | 610 | 2026-10-17 10:10:29 | `aba3697dd5b9` | 噪声面 |
| 515 | `.tmp/collision_survey_hash.py` | 2,916 | 2026-10-17 10:07:57 | `0343236330c3` | 噪声面 |
| 516 | `.tmp/collision_survey_hashes.json` | 75,439 | 2026-10-17 10:07:58 | `0329afb1e9fc` | 噪声面 |
| 517 | `.tmp/collision_survey_inventory.json` | 37,588 | 2026-10-17 10:07:30 | `a4cd5b2fc5c8` | 噪声面 |
| 518 | `.tmp/collision_survey_inventory.py` | 3,941 | 2026-10-17 10:07:27 | `6ef67c3a4160` | 噪声面 |
| 519 | `.tmp/collision_survey_verify.py` | 2,378 | 2026-10-17 10:10:07 | `adb2b3a693a9` | 噪声面 |
| 520 | `.tmp/combo_llm_calls_2026_10_16.jsonl` | 59,626 | 2026-10-16 11:58:25 | `86f05646031b` | 噪声面 |
| 521 | `.tmp/combo_measurement_2026_10_16.json` | 121,779 | 2026-10-16 11:58:25 | `27609799e40e` | 噪声面 |
| 522 | `.tmp/d05_hash_index.py` | 1,004 | 2026-10-10 11:51:23 | `070b6f865eba` | 噪声面 |
| 523 | `.tmp/d1fill_anchor_snapshot.py` | 1,985 | 2026-10-01 13:39:20 | `15c0b0ade7ab` | 噪声面 |
| 524 | `.tmp/d1fill_recount_checks.py` | 2,336 | 2026-10-01 13:38:49 | `b8af087b5e1f` | 噪声面 |
| 525 | `.tmp/d1fill_recount_impl1.py` | 6,464 | 2026-10-01 13:35:55 | `bb30ad15c89b` | 噪声面 |
| 526 | `.tmp/d1fill_recount_impl2.ps1` | 6,132 | 2026-10-01 13:38:15 | `88411408e671` | 噪声面 |
| 527 | `.tmp/d64_probe1.py` | 2,221 | 2026-10-17 18:22:01 | `e7e74bfe920e` | 噪声面 |
| 528 | `.tmp/d64_scan.py` | 1,873 | 2026-10-17 18:22:36 | `5484e7b0b941` | 噪声面 |
| 529 | `.tmp/d64_time.py` | 1,220 | 2026-10-17 18:23:00 | `e2539091823a` | 噪声面 |
| 530 | `.tmp/d64_verify.out.txt` | 1,298 | 2026-10-17 18:26:14 | `2c6f3525290b` | 噪声面 |
| 531 | `.tmp/d64_verify.py` | 2,962 | 2026-10-17 18:26:08 | `96d1a19b71f2` | 噪声面 |
| 532 | `.tmp/d64_write.py` | 48,462 | 2026-10-17 18:25:44 | `4f8fa8459b5d` | 噪声面 |
| 533 | `.tmp/d65_probe1.py` | 3,589 | 2026-10-17 18:47:25 | `a6ad2cea883f` | 噪声面 |
| 534 | `.tmp/d65_probe2.out.txt` | 3,308 | 2026-10-17 18:47:57 | `520db5bf59ef` | 噪声面 |
| 535 | `.tmp/d65_probe2.py` | 1,813 | 2026-10-17 18:47:49 | `426977af0830` | 噪声面 |
| 536 | `.tmp/d65_probe3.out.txt` | 3,006 | 2026-10-17 18:49:45 | `39545068509b` | 噪声面 |
| 537 | `.tmp/d65_probe3.py` | 4,089 | 2026-10-17 18:49:36 | `1597a575153d` | 噪声面 |
| 538 | `.tmp/d65_probe4.out.txt` | 2,464 | 2026-10-17 18:50:26 | `c7de1a8044c0` | 噪声面 |
| 539 | `.tmp/d65_probe4.py` | 2,273 | 2026-10-17 18:50:15 | `54eba478ef4e` | 噪声面 |
| 540 | `.tmp/d65_verify.out.txt` | 5,922 | 2026-10-17 18:55:44 | `6a2c444b3b66` | 噪声面 |
| 541 | `.tmp/d65_verify.py` | 8,800 | 2026-10-17 18:55:38 | `7d5472188ed7` | 噪声面 |
| 542 | `.tmp/d65_write1.py` | 36,939 | 2026-10-17 18:52:21 | `d7c451d2638d` | 噪声面 |
| 543 | `.tmp/d65_write2.py` | 57,693 | 2026-10-17 18:55:13 | `65a872dd4fa6` | 噪声面 |
| 544 | `.tmp/d69_effect_rev1.md` | 35,878 | 2026-10-17 19:16:38 | `aa8ba7c13629` | 噪声面 |
| 545 | `.tmp/d69_effect_rev2.md` | 37,867 | 2026-10-17 19:20:04 | `aadbf65b1a1d` | 噪声面 |
| 546 | `.tmp/d69_final.out.txt` | 2,073 | 2026-10-17 19:22:10 | `359924630a53` | 噪声面 |
| 547 | `.tmp/d69_final.py` | 3,941 | 2026-10-17 19:20:18 | `8f0a1e82406c` | 噪声面 |
| 548 | `.tmp/d69_probe1.py` | 2,159 | 2026-10-17 19:10:58 | `140397edd7f3` | 噪声面 |
| 549 | `.tmp/d69_probe2.py` | 1,520 | 2026-10-17 19:11:56 | `b8fe0c9392c5` | 噪声面 |
| 550 | `.tmp/d69_probe3.py` | 1,459 | 2026-10-17 19:12:20 | `1437ced4cc3d` | 噪声面 |
| 551 | `.tmp/d69_probe4.py` | 2,596 | 2026-10-17 19:12:39 | `0f5e1543dadc` | 噪声面 |
| 552 | `.tmp/d69_v69_rev1.md` | 40,644 | 2026-10-17 19:16:38 | `c3621b68a0e7` | 噪声面 |
| 553 | `.tmp/d69_v69_rev2.md` | 44,203 | 2026-10-17 19:20:04 | `f85ec92d75bc` | 噪声面 |
| 554 | `.tmp/d69_verify.out.txt` | 2,646 | 2026-10-17 19:16:53 | `e42d7b6b61a2` | 噪声面 |
| 555 | `.tmp/d69_verify.py` | 3,364 | 2026-10-17 19:16:47 | `efbbf7cdb7d6` | 噪声面 |
| 556 | `.tmp/d69_verify2.out.txt` | 876 | 2026-10-17 19:17:35 | `c6288995ff7d` | 噪声面 |
| 557 | `.tmp/d69_verify2.py` | 2,098 | 2026-10-17 19:17:07 | `1e1a4c73e0ab` | 噪声面 |
| 558 | `.tmp/d69_write.py` | 85,582 | 2026-10-17 19:21:31 | `c3b6cf60889b` | 噪声面 |
| 559 | `.tmp/d70_append.py` | 1,034 | 2026-10-17 19:25:20 | `084cae736d8b` | 噪声面 |
| 560 | `.tmp/d70_apply.out.txt` | 1,480 | 2026-10-17 19:22:46 | `f5e64973a36e` | 噪声面 |
| 561 | `.tmp/d70_apply.py` | 1,747 | 2026-10-17 19:21:01 | `9b4cfc6dd058` | 噪声面 |
| 562 | `.tmp/d70_apply2.py` | 2,514 | 2026-10-17 19:22:03 | `6be489416e71` | 噪声面 |
| 563 | `.tmp/d70_apply3.out.txt` | 310 | 2026-10-17 19:23:13 | `9c24b079e119` | 噪声面 |
| 564 | `.tmp/d70_apply3.py` | 1,010 | 2026-10-17 19:23:13 | `fcc49b4487d7` | 噪声面 |
| 565 | `.tmp/d70_apply4.out.txt` | 212 | 2026-10-17 19:23:45 | `bec02e8ecf5d` | 噪声面 |
| 566 | `.tmp/d70_apply4.py` | 1,766 | 2026-10-17 19:23:44 | `8ca21abb7758` | 噪声面 |
| 567 | `.tmp/d70_drift.py` | 778 | 2026-10-17 19:24:19 | `2e43ebd92169` | 噪声面 |
| 568 | `.tmp/d70_drift_eff.md` | 2,202 | 2026-10-17 19:25:08 | `664759da9f10` | 噪声面 |
| 569 | `.tmp/d70_drift_v70.md` | 2,292 | 2026-10-17 19:25:01 | `79fc1550c7f5` | 噪声面 |
| 570 | `.tmp/d70_driftfix.out.txt` | 1,076 | 2026-10-17 19:24:52 | `88b996edce90` | 噪声面 |
| 571 | `.tmp/d70_driftfix.py` | 8,090 | 2026-10-17 19:24:52 | `e6b4593f36d9` | 噪声面 |
| 572 | `.tmp/d70_err_eff.md` | 5,873 | 2026-10-17 19:22:36 | `d463a8b475db` | 噪声面 |
| 573 | `.tmp/d70_err_v70.md` | 5,962 | 2026-10-17 19:22:17 | `5750451d0993` | 噪声面 |
| 574 | `.tmp/d70_final.out.txt` | 2,782 | 2026-10-17 19:23:58 | `125b1901bc58` | 噪声面 |
| 575 | `.tmp/d70_final.py` | 890 | 2026-10-17 19:23:25 | `426ac9b71216` | 噪声面 |
| 576 | `.tmp/d70_final2.py` | 2,166 | 2026-10-17 19:23:58 | `72167147ccca` | 噪声面 |
| 577 | `.tmp/d70_final_verify.out.txt` | 602 | 2026-10-17 19:25:20 | `33182aedc627` | 噪声面 |
| 578 | `.tmp/d70_fix_eff.json` | 10,500 | 2026-10-17 19:21:38 | `47de9f384117` | 噪声面 |
| 579 | `.tmp/d70_fix_eff2.json` | 3,201 | 2026-10-17 19:23:01 | `356307b76db2` | 噪声面 |
| 580 | `.tmp/d70_fix_v70.json` | 9,245 | 2026-10-17 19:21:19 | `c385466bca09` | 噪声面 |
| 581 | `.tmp/d70_patch1.out.txt` | 0 | 2026-10-17 19:20:44 | `e3b0c44298fc` | 噪声面 |
| 582 | `.tmp/d70_patch1.py` | 15,503 | 2026-10-17 19:20:35 | `fe0291239e63` | 噪声面 |
| 583 | `.tmp/d70_write.out.txt` | 3,464 | 2026-10-17 19:18:02 | `db2387d43824` | 噪声面 |
| 584 | `.tmp/d70_write.py` | 70,471 | 2026-10-17 19:17:47 | `33bed6a60c0e` | 噪声面 |
| 585 | `.tmp/d70_z.out.txt` | 554 | 2026-10-17 19:25:32 | `e8563956bb97` | 噪声面 |
| 586 | `.tmp/d70_z.py` | 1,607 | 2026-10-17 19:25:32 | `d600a30fd1ef` | 噪声面 |
| 587 | `.tmp/d71_check.py` | 2,058 | 2026-10-17 19:43:49 | `5434c5d33be3` | 噪声面 |
| 588 | `.tmp/d71_probe.out.txt` | 6,174 | 2026-10-17 19:37:17 | `74a4aeea6a9c` | 噪声面 |
| 589 | `.tmp/d71_probe.py` | 5,686 | 2026-10-17 19:37:08 | `0e58b81d7801` | 噪声面 |
| 590 | `.tmp/d71_write.out.txt` | 983 | 2026-10-17 19:42:40 | `0290b419b61b` | 噪声面 |
| 591 | `.tmp/d71_write.py` | 84,687 | 2026-10-17 19:42:33 | `eef47343f274` | 噪声面 |
| 592 | `.tmp/d79_body1.md` | 38,119 | 2026-10-17 21:06:12 | `283a697a7704` | 噪声面 |
| 593 | `.tmp/d79_body2.md` | 38,313 | 2026-10-17 21:07:43 | `e09cea31cd27` | 噪声面 |
| 594 | `.tmp/d79_errata.out.txt` | 448 | 2026-10-17 21:09:02 | `3150f9d42792` | 噪声面 |
| 595 | `.tmp/d79_errata.py` | 7,268 | 2026-10-17 21:08:51 | `2902df4038a6` | 噪声面 |
| 596 | `.tmp/d79_probe1.out.txt` | 1,634 | 2026-10-17 21:04:37 | `1729e0288f7c` | 噪声面 |
| 597 | `.tmp/d79_probe1.py` | 4,677 | 2026-10-17 21:04:26 | `43d3d288243e` | 噪声面 |
| 598 | `.tmp/d79_verify.out.txt` | 1,465 | 2026-10-17 21:09:18 | `27b7cd9da1d2` | 噪声面 |
| 599 | `.tmp/d79_verify.py` | 2,518 | 2026-10-17 21:08:09 | `89fd4a78115e` | 噪声面 |
| 600 | `.tmp/d79_write.out.txt` | 981 | 2026-10-17 21:07:57 | `dd0945bb002e` | 噪声面 |
| 601 | `.tmp/d79_write.py` | 3,087 | 2026-10-17 21:07:51 | `d9aa14af1712` | 噪声面 |
| 602 | `.tmp/d80_body1.md` | 33,430 | 2026-10-17 21:33:33 | `7919da0473d9` | 噪声面 |
| 603 | `.tmp/d80_body2.md` | 37,073 | 2026-10-17 21:39:30 | `9bd2c6df2834` | 噪声面 |
| 604 | `.tmp/d80_probe1.out.txt` | 4,403 | 2026-10-17 21:24:49 | `4486304a2bfa` | 噪声面 |
| 605 | `.tmp/d80_probe1.py` | 4,352 | 2026-10-17 21:24:36 | `c9a5a66c38bc` | 噪声面 |
| 606 | `.tmp/d80_probe2.out.txt` | 253 | 2026-10-17 21:25:44 | `e78bd94a67d7` | 噪声面 |
| 607 | `.tmp/d80_probe2.py` | 1,694 | 2026-10-17 21:25:37 | `dc813551824f` | 噪声面 |
| 608 | `.tmp/d80_probe3.out.txt` | 15,919 | 2026-10-17 21:26:12 | `bcd6b283cad8` | 噪声面 |
| 609 | `.tmp/d80_probe3.py` | 2,027 | 2026-10-17 21:26:03 | `32bc82072e7a` | 噪声面 |
| 610 | `.tmp/d80_probe4.out.txt` | 24,376 | 2026-10-17 21:27:11 | `ada6adbff256` | 噪声面 |
| 611 | `.tmp/d80_probe4.py` | 4,341 | 2026-10-17 21:26:59 | `0a92abc8a157` | 噪声面 |
| 612 | `.tmp/d80_probe5.out.txt` | 7,094 | 2026-10-17 21:28:40 | `d5fd34016b88` | 噪声面 |
| 613 | `.tmp/d80_probe5.py` | 2,043 | 2026-10-17 21:28:28 | `f0e418379708` | 噪声面 |
| 614 | `.tmp/d80_probe6.out.txt` | 3,279 | 2026-10-17 21:29:40 | `7e666918ad07` | 噪声面 |
| 615 | `.tmp/d80_probe6.py` | 3,429 | 2026-10-17 21:29:27 | `e6eec454bfa6` | 噪声面 |
| 616 | `.tmp/d80_probe7.out.txt` | 2,073 | 2026-10-17 21:30:27 | `51daafcaf88a` | 噪声面 |
| 617 | `.tmp/d80_probe7.py` | 2,347 | 2026-10-17 21:30:16 | `26728c05a689` | 噪声面 |
| 618 | `.tmp/d80_verify.out.txt` | 1,621 | 2026-10-17 21:40:56 | `6efa85285a43` | 噪声面 |
| 619 | `.tmp/d80_verify.py` | 3,047 | 2026-10-17 21:40:46 | `d8fde3291246` | 噪声面 |
| 620 | `.tmp/d80_write.py` | 5,163 | 2026-10-17 21:39:54 | `6c2bc5984da5` | 噪声面 |
| 621 | `.tmp/d81_body1.md` | 44,858 | 2026-10-17 21:56:04 | `1d65a4b9411a` | 噪声面 |
| 622 | `.tmp/d81_body2.md` | 37,061 | 2026-10-17 21:57:53 | `c17a5af0d0bd` | 噪声面 |
| 623 | `.tmp/d81_errata.py` | 6,851 | 2026-10-17 21:59:19 | `f28aa23fc2a5` | 噪声面 |
| 624 | `.tmp/d81_errata2.py` | 4,486 | 2026-10-17 22:00:35 | `954f3e7e6d2c` | 噪声面 |
| 625 | `.tmp/d81_errata2_console.txt` | 1,514 | 2026-10-17 22:00:42 | `eb813eec0a3a` | 噪声面 |
| 626 | `.tmp/d81_errata3.py` | 6,257 | 2026-10-17 22:01:09 | `3efa38c8d5f0` | 噪声面 |
| 627 | `.tmp/d81_errata_console.txt` | 642 | 2026-10-17 21:59:26 | `10de0cf0c48d` | 噪声面 |
| 628 | `.tmp/d81_probe0.py` | 1,032 | 2026-10-17 21:50:08 | `d1dddafb9696` | 噪声面 |
| 629 | `.tmp/d81_probe1.out.txt` | 3,530 | 2026-10-17 21:50:53 | `43449fe03dec` | 噪声面 |
| 630 | `.tmp/d81_probe1.py` | 2,458 | 2026-10-17 21:50:51 | `f611e4d4b137` | 噪声面 |
| 631 | `.tmp/d81_probe2.out.txt` | 5,538 | 2026-10-17 21:51:56 | `1e97cc3cadb2` | 噪声面 |
| 632 | `.tmp/d81_probe2.py` | 3,433 | 2026-10-17 21:51:51 | `afbca81fb239` | 噪声面 |
| 633 | `.tmp/d81_probe3.out.txt` | 1,124 | 2026-10-17 21:52:30 | `2b156bda3661` | 噪声面 |
| 634 | `.tmp/d81_probe3.py` | 2,556 | 2026-10-17 21:52:18 | `e497040f0890` | 噪声面 |
| 635 | `.tmp/d81_probe4.py` | 483 | 2026-10-17 21:53:05 | `dc7de42be926` | 噪声面 |
| 636 | `.tmp/d81_verify.out.txt` | 4,538 | 2026-10-17 21:59:26 | `afd531777546` | 噪声面 |
| 637 | `.tmp/d81_verify2.py` | 4,032 | 2026-10-17 21:58:28 | `e90d0bc3fc88` | 噪声面 |
| 638 | `.tmp/d81_verify_console.txt` | 354 | 2026-10-17 21:58:35 | `c09c6aa95525` | 噪声面 |
| 639 | `.tmp/d81_verify_final.out.txt` | 1,046 | 2026-10-17 22:01:16 | `20b6b0fe4238` | 噪声面 |
| 640 | `.tmp/d81_verify_readback_utf8.txt` | 3,426 | 2026-10-17 21:58:35 | `ebe50d99fa78` | 噪声面 |
| 641 | `.tmp/d81_write.py` | 3,489 | 2026-10-17 21:58:05 | `0750ff5e4618` | 噪声面 |
| 642 | `.tmp/d82_append.py` | 7,927 | 2026-10-17 22:14:50 | `9763517baf55` | 噪声面 |
| 643 | `.tmp/d82_append2.py` | 6,901 | 2026-10-17 22:15:57 | `7a1b66cb76a6` | 噪声面 |
| 644 | `.tmp/d82_body1.md` | 44,006 | 2026-10-17 22:11:09 | `90ce55bf3926` | 噪声面 |
| 645 | `.tmp/d82_body2.md` | 40,356 | 2026-10-17 22:12:27 | `e8c74076fde5` | 噪声面 |
| 646 | `.tmp/d82_probe1.out.txt` | 3,637 | 2026-10-17 22:08:26 | `309ed874b91a` | 噪声面 |
| 647 | `.tmp/d82_probe1.py` | 3,900 | 2026-10-17 22:08:15 | `8537496a6d35` | 噪声面 |
| 648 | `.tmp/d82_probe2.out.txt` | 1,824 | 2026-10-17 22:08:50 | `d881f2bdecbb` | 噪声面 |
| 649 | `.tmp/d82_probe2.py` | 3,776 | 2026-10-17 22:08:38 | `86c7c54ad6c9` | 噪声面 |
| 650 | `.tmp/d82_probe3.out.txt` | 969 | 2026-10-17 22:09:41 | `228f413de0a4` | 噪声面 |
| 651 | `.tmp/d82_probe3.py` | 1,855 | 2026-10-17 22:09:34 | `482213c42994` | 噪声面 |
| 652 | `.tmp/d82_probe4.out.txt` | 2,673 | 2026-10-17 22:13:06 | `f7784480363d` | 噪声面 |
| 653 | `.tmp/d82_probe4.py` | 1,172 | 2026-10-17 22:12:56 | `f8e57adb5dd8` | 噪声面 |
| 654 | `.tmp/d82_probe5.out.txt` | 840 | 2026-10-17 22:13:33 | `59215ac282e3` | 噪声面 |
| 655 | `.tmp/d82_probe5.py` | 1,468 | 2026-10-17 22:13:23 | `03e39c624034` | 噪声面 |
| 656 | `.tmp/d82_probe6.out.txt` | 570 | 2026-10-17 22:14:22 | `a2cf58b8c90d` | 噪声面 |
| 657 | `.tmp/d82_probe6.py` | 1,222 | 2026-10-17 22:14:14 | `b1b36288ce49` | 噪声面 |
| 658 | `.tmp/d82_probe7.out.txt` | 432 | 2026-10-17 22:15:10 | `4071dff45d63` | 噪声面 |
| 659 | `.tmp/d82_probe8.out.txt` | 571 | 2026-10-17 22:15:19 | `b14995d285a8` | 噪声面 |
| 660 | `.tmp/d82_probe9.out.txt` | 484 | 2026-10-17 22:15:40 | `c9240ede5a26` | 噪声面 |
| 661 | `.tmp/d82_probe9.py` | 1,475 | 2026-10-17 22:15:31 | `d3767bc9927c` | 噪声面 |
| 662 | `.tmp/d82_verify.out.txt` | 2,002 | 2026-10-17 22:12:47 | `579fc550f43a` | 噪声面 |
| 663 | `.tmp/d82_verify2.out.txt` | 2,093 | 2026-10-17 22:14:59 | `b16c168b7cae` | 噪声面 |
| 664 | `.tmp/d82_verify3.out.txt` | 1,312 | 2026-10-17 22:16:05 | `357991a4cf3f` | 噪声面 |
| 665 | `.tmp/d82_write.py` | 3,764 | 2026-10-17 22:12:39 | `1c5ffcb8bf3f` | 噪声面 |
| 666 | `.tmp/d83_body1.md` | 49,996 | 2026-10-17 22:30:12 | `e2a67aa39bdd` | 噪声面 |
| 667 | `.tmp/d83_body2.md` | 41,779 | 2026-10-17 22:32:02 | `faee80c8b051` | 噪声面 |
| 668 | `.tmp/d83_n7r_stage.md` | 35,057 | 2026-10-17 22:13:10 | `7a2133c810b1` | 噪声面 |
| 669 | `.tmp/d83_n7r_verify.out.txt` | 1,257 | 2026-10-17 22:13:36 | `b968a2beb941` | 噪声面 |
| 670 | `.tmp/d83_n7r_verify.py` | 1,998 | 2026-10-17 22:13:27 | `850343c11b1e` | 噪声面 |
| 671 | `.tmp/d83_n7r_write.py` | 729 | 2026-10-17 22:13:14 | `dd9f2f339180` | 噪声面 |
| 672 | `.tmp/d83_probe1.out.txt` | 5,736 | 2026-10-17 22:26:01 | `b3c0cce199c3` | 噪声面 |
| 673 | `.tmp/d83_probe1.py` | 3,623 | 2026-10-17 22:25:54 | `ac46a52ad100` | 噪声面 |
| 674 | `.tmp/d83_probe2.out.txt` | 7,806 | 2026-10-17 22:26:37 | `b8fdf1aff2bd` | 噪声面 |
| 675 | `.tmp/d83_probe2.py` | 4,946 | 2026-10-17 22:26:25 | `99fb523577b1` | 噪声面 |
| 676 | `.tmp/d83_probe3.out.txt` | 3,708 | 2026-10-17 22:27:51 | `2bca0aed0868` | 噪声面 |
| 677 | `.tmp/d83_probe3.py` | 2,371 | 2026-10-17 22:27:43 | `7647d1b8cd64` | 噪声面 |
| 678 | `.tmp/d83_probe4.out.txt` | 4,686 | 2026-10-17 22:30:37 | `b2cc6d88e3fc` | 噪声面 |
| 679 | `.tmp/d83_probe4.py` | 2,410 | 2026-10-17 22:30:31 | `c15116a74765` | 噪声面 |
| 680 | `.tmp/d83_probe5.out.txt` | 2,124 | 2026-10-17 22:32:37 | `cac81507a2f8` | 噪声面 |
| 681 | `.tmp/d83_probe5.py` | 1,578 | 2026-10-17 22:32:32 | `4bbdeefec2f5` | 噪声面 |
| 682 | `.tmp/d83_verify.out.txt` | 7,386 | 2026-10-17 22:32:23 | `d53b4e97cc8a` | 噪声面 |
| 683 | `.tmp/d83_write.py` | 5,535 | 2026-10-17 22:32:18 | `180d6eafd4ba` | 噪声面 |
| 684 | `.tmp/d84_body1.md` | 42,968 | 2026-10-17 22:43:54 | `c565669aadeb` | 噪声面 |
| 685 | `.tmp/d84_body2.md` | 40,560 | 2026-10-17 22:45:39 | `955222063aa0` | 噪声面 |
| 686 | `.tmp/d84_probe1.py` | 1,093 | 2026-10-17 22:39:24 | `1ca7c17c1dfd` | 噪声面 |
| 687 | `.tmp/d84_probe2.out.txt` | 5,550 | 2026-10-17 22:39:54 | `788a3be52720` | 噪声面 |
| 688 | `.tmp/d84_probe2.py` | 1,736 | 2026-10-17 22:39:53 | `d9e9b456a61e` | 噪声面 |
| 689 | `.tmp/d84_probe3.out.txt` | 2,352 | 2026-10-17 22:41:07 | `34ab920c00ca` | 噪声面 |
| 690 | `.tmp/d84_probe3.py` | 3,545 | 2026-10-17 22:41:01 | `0a84340e62e1` | 噪声面 |
| 691 | `.tmp/d84_probe4.out.txt` | 202 | 2026-10-17 22:46:35 | `0485e04f9d00` | 噪声面 |
| 692 | `.tmp/d84_probe4.py` | 593 | 2026-10-17 22:46:35 | `4171f2db822a` | 噪声面 |
| 693 | `.tmp/d84_probe5.out.txt` | 738 | 2026-10-17 22:46:50 | `9bcdbe126c0f` | 噪声面 |
| 694 | `.tmp/d84_probe5.py` | 650 | 2026-10-17 22:46:50 | `c789138c9dd7` | 噪声面 |
| 695 | `.tmp/d84_probe6.py` | 2,868 | 2026-10-17 22:47:07 | `d0aef4e644af` | 噪声面 |
| 696 | `.tmp/d84_probe7.py` | 998 | 2026-10-17 22:47:21 | `5fc6bde34580` | 噪声面 |
| 697 | `.tmp/d84_verify.out.txt` | 5,562 | 2026-10-17 22:47:21 | `eb58d1c1e572` | 噪声面 |
| 698 | `.tmp/d84_write.py` | 3,878 | 2026-10-17 22:46:00 | `29725492eea8` | 噪声面 |
| 699 | `.tmp/d85_append.out.txt` | 382 | 2026-10-17 23:12:28 | `234a0bce60e9` | 噪声面 |
| 700 | `.tmp/d85_append.py` | 4,607 | 2026-10-17 23:12:19 | `a23b1d3d5394` | 噪声面 |
| 701 | `.tmp/d85_body1.md` | 49,626 | 2026-10-17 23:10:23 | `80229d6489d1` | 噪声面 |
| 702 | `.tmp/d85_body2.md` | 26,187 | 2026-10-17 23:11:26 | `d08e5b7198b0` | 噪声面 |
| 703 | `.tmp/d85_carddef.txt` | 4,602 | 2026-10-17 23:05:23 | `d83bd231882a` | 噪声面 |
| 704 | `.tmp/d85_def.txt` | 0 | 2026-10-17 23:05:00 | `e3b0c44298fc` | 噪声面 |
| 705 | `.tmp/d85_fp2.txt` | 617 | 2026-10-17 23:06:32 | `feb0a03f50ff` | 噪声面 |
| 706 | `.tmp/d85_fp3.txt` | 461 | 2026-10-17 23:08:43 | `6f91932e7b96` | 噪声面 |
| 707 | `.tmp/d85_loc.txt` | 1,545 | 2026-10-17 23:06:16 | `458ded1a9b0d` | 噪声面 |
| 708 | `.tmp/d85_p1_def.txt` | 0 | 2026-10-17 23:04:03 | `e3b0c44298fc` | 噪声面 |
| 709 | `.tmp/d85_p1_raw.txt` | 15,655 | 2026-10-17 23:04:28 | `b3ad8f314965` | 噪声面 |
| 710 | `.tmp/d85_p1_resp.txt` | 0 | 2026-10-17 23:04:03 | `e3b0c44298fc` | 噪声面 |
| 711 | `.tmp/d85_p1_scan.txt` | 57 | 2026-10-17 23:04:03 | `3fa1793856fb` | 噪声面 |
| 712 | `.tmp/d85_p1_task.txt` | 0 | 2026-10-17 23:04:03 | `e3b0c44298fc` | 噪声面 |
| 713 | `.tmp/d85_p5.out.txt` | 2,562 | 2026-10-17 23:05:54 | `fc3584a325be` | 噪声面 |
| 714 | `.tmp/d85_p8.out.txt` | 1,800 | 2026-10-17 23:07:32 | `2db3a3f7d5ec` | 噪声面 |
| 715 | `.tmp/d85_p9.out.txt` | 1,437 | 2026-10-17 23:08:05 | `888446bbf546` | 噪声面 |
| 716 | `.tmp/d85_probe1.py` | 3,020 | 2026-10-17 23:03:42 | `7ebe64d0eff9` | 噪声面 |
| 717 | `.tmp/d85_probe2.py` | 1,355 | 2026-10-17 23:04:08 | `ee5ff4bf1217` | 噪声面 |
| 718 | `.tmp/d85_probe3.py` | 2,484 | 2026-10-17 23:04:51 | `9ff7b9930550` | 噪声面 |
| 719 | `.tmp/d85_probe4.py` | 2,254 | 2026-10-17 23:05:16 | `a68a9e4d0878` | 噪声面 |
| 720 | `.tmp/d85_probe5.py` | 3,587 | 2026-10-17 23:05:43 | `c3b40ac9f977` | 噪声面 |
| 721 | `.tmp/d85_probe6.py` | 2,055 | 2026-10-17 23:06:05 | `60968546ce49` | 噪声面 |
| 722 | `.tmp/d85_probe7.py` | 1,661 | 2026-10-17 23:06:26 | `9e452147d408` | 噪声面 |
| 723 | `.tmp/d85_probe8.py` | 5,860 | 2026-10-17 23:07:08 | `2f90bdfe9e91` | 噪声面 |
| 724 | `.tmp/d85_probe9.py` | 1,716 | 2026-10-17 23:07:53 | `c2151ef13c42` | 噪声面 |
| 725 | `.tmp/d85_receipt.txt` | 0 | 2026-10-17 23:06:13 | `e3b0c44298fc` | 噪声面 |
| 726 | `.tmp/d85_receipt_raw.txt` | 6,622 | 2026-10-17 23:06:32 | `9f4e5977991b` | 噪声面 |
| 727 | `.tmp/d85_resp.txt` | 27,816 | 2026-10-17 23:05:00 | `cb42f72162bf` | 噪声面 |
| 728 | `.tmp/d85_task.txt` | 2,677 | 2026-10-17 23:05:00 | `d23292c61928` | 噪声面 |
| 729 | `.tmp/d85_verify.out.txt` | 1,710 | 2026-10-17 23:12:42 | `50b4c76a9d71` | 噪声面 |
| 730 | `.tmp/d85_verify.py` | 2,525 | 2026-10-17 23:11:46 | `541e097fd55c` | 噪声面 |
| 731 | `.tmp/d85_write.out.txt` | 405 | 2026-10-17 23:11:39 | `abf861df8b1f` | 噪声面 |
| 732 | `.tmp/d85_write.py` | 1,329 | 2026-10-17 23:11:31 | `72777f36ee87` | 噪声面 |
| 733 | `.tmp/d86_errata.py` | 11,348 | 2026-10-17 23:10:43 | `73273d1a682d` | 噪声面 |
| 734 | `.tmp/d86_errata3.py` | 5,832 | 2026-10-17 23:11:40 | `4d66a25c1ab8` | 噪声面 |
| 735 | `.tmp/d86_final.py` | 1,766 | 2026-10-17 23:11:51 | `e2fddad09200` | 噪声面 |
| 736 | `.tmp/d86_probe1.out.txt` | 940 | 2026-10-17 23:04:09 | `1d91053b90d0` | 噪声面 |
| 737 | `.tmp/d86_probe1.py` | 887 | 2026-10-17 23:04:06 | `687a88b98c32` | 噪声面 |
| 738 | `.tmp/d86_probe2.py` | 439 | 2026-10-17 23:04:37 | `42858c42bad2` | 噪声面 |
| 739 | `.tmp/d86_probe3.py` | 620 | 2026-10-17 23:05:01 | `107975c87711` | 噪声面 |
| 740 | `.tmp/d86_probe4.py` | 2,234 | 2026-10-17 23:05:35 | `3595aecb1033` | 噪声面 |
| 741 | `.tmp/d86_probe5.py` | 1,358 | 2026-10-17 23:05:44 | `215c0504d46b` | 噪声面 |
| 742 | `.tmp/d86_verify.out.txt` | 2,341 | 2026-10-17 23:11:08 | `0fb8fb628de0` | 噪声面 |
| 743 | `.tmp/d86_verify.py` | 4,033 | 2026-10-17 23:09:23 | `17d12b4e58cf` | 噪声面 |
| 744 | `.tmp/d86_verify_print.txt` | 2,341 | 2026-10-17 23:11:08 | `0fb8fb628de0` | 噪声面 |
| 745 | `.tmp/d86_write1.py` | 36,576 | 2026-10-17 23:07:15 | `93c4fbc17cd3` | 噪声面 |
| 746 | `.tmp/d86_write2.py` | 46,018 | 2026-10-17 23:09:03 | `d4992eac401d` | 噪声面 |
| 747 | `.tmp/d87_append.py` | 5,167 | 2026-10-17 23:30:47 | `f89fa212b30e` | 噪声面 |
| 748 | `.tmp/d87_probe1.out.txt` | 2,897 | 2026-10-17 23:24:00 | `3e71ed35f65b` | 噪声面 |
| 749 | `.tmp/d87_probe1.py` | 4,968 | 2026-10-17 23:23:40 | `b18f260dd083` | 噪声面 |
| 750 | `.tmp/d87_probe2.out.txt` | 6,002 | 2026-10-17 23:24:40 | `e2709188e23e` | 噪声面 |
| 751 | `.tmp/d87_probe2.py` | 3,753 | 2026-10-17 23:24:33 | `dd13833989e7` | 噪声面 |
| 752 | `.tmp/d87_probe3.out.txt` | 384 | 2026-10-17 23:26:28 | `31d53b401e3a` | 噪声面 |
| 753 | `.tmp/d87_probe3.py` | 1,998 | 2026-10-17 23:26:13 | `73aa66b90d34` | 噪声面 |
| 754 | `.tmp/d87_write1.py` | 52,720 | 2026-10-17 23:28:20 | `df8d9c96c381` | 噪声面 |
| 755 | `.tmp/d88_errata.py` | 5,958 | 2026-10-17 23:36:40 | `ec473bd85ff6` | 噪声面 |
| 756 | `.tmp/d88_probe1.out.txt` | 3,694 | 2026-10-17 23:29:49 | `6298a859b828` | 噪声面 |
| 757 | `.tmp/d88_probe1.py` | 5,713 | 2026-10-17 23:29:13 | `ea8246bee209` | 噪声面 |
| 758 | `.tmp/d88_verify.out.txt` | 2,324 | 2026-10-17 23:36:49 | `dd29936a25a3` | 噪声面 |
| 759 | `.tmp/d88_verify.py` | 4,575 | 2026-10-17 23:35:32 | `635a18d72c3b` | 噪声面 |
| 760 | `.tmp/d88_write2.py` | 41,852 | 2026-10-17 23:32:13 | `a6c6d98da4fe` | 噪声面 |
| 761 | `.tmp/d88_write3.py` | 40,507 | 2026-10-17 23:33:31 | `6d9adcf449c9` | 噪声面 |
| 762 | `.tmp/d88_write4.py` | 51,411 | 2026-10-17 23:35:20 | `a1fc06af935c` | 噪声面 |
| 763 | `.tmp/d89_append1.py` | 7,403 | 2026-10-17 23:53:23 | `8989ad41e59a` | 噪声面 |
| 764 | `.tmp/d89_probe1.out.txt` | 2,841 | 2026-10-17 23:46:04 | `3a85f181e53a` | 噪声面 |
| 765 | `.tmp/d89_probe1.py` | 5,193 | 2026-10-17 23:45:51 | `4425c3b71380` | 噪声面 |
| 766 | `.tmp/d89_probe2.out.txt` | 1,030 | 2026-10-17 23:46:38 | `b6c333723b49` | 噪声面 |
| 767 | `.tmp/d89_probe2.py` | 1,571 | 2026-10-17 23:46:31 | `ef9d91d8e58d` | 噪声面 |
| 768 | `.tmp/d89_probe3.out.txt` | 408 | 2026-10-17 23:49:16 | `577c18f43443` | 噪声面 |
| 769 | `.tmp/d89_probe3.py` | 985 | 2026-10-17 23:49:08 | `abacf473e4d5` | 噪声面 |
| 770 | `.tmp/d89_verify.out.txt` | 1,040 | 2026-10-17 23:53:02 | `7b1984940f1a` | 噪声面 |
| 771 | `.tmp/d89_verify.py` | 5,657 | 2026-10-17 23:52:50 | `7edae96a586c` | 噪声面 |
| 772 | `.tmp/d89_verify2.out.txt` | 874 | 2026-10-17 23:53:52 | `ab13400e0adf` | 噪声面 |
| 773 | `.tmp/d89_verify2.py` | 2,421 | 2026-10-17 23:53:44 | `e0dd6709f262` | 噪声面 |
| 774 | `.tmp/d89_write1.py` | 47,836 | 2026-10-17 23:49:27 | `1149389b5c99` | 噪声面 |
| 775 | `.tmp/d89_write2.py` | 59,936 | 2026-10-17 23:51:57 | `07362bc6517b` | 噪声面 |
| 776 | `.tmp/diag.py` | 972 | 2026-10-13 23:40:22 | `db20dd0e6efb` | 噪声面 |
| 777 | `.tmp/diffcause.py` | 2,724 | 2026-10-10 13:47:39 | `2b24513cdf74` | 噪声面 |
| 778 | `.tmp/distortion_calculator_pre_410a12482eef.py` | 40,611 | 2026-10-17 23:55:51 | `410a12482eef` | 噪声面 |
| 779 | `.tmp/docwriter_c2_effect_census.json` | 36,157 | 2026-10-14 14:43:10 | `1ef99b1da14d` | 噪声面 |
| 780 | `.tmp/docwriter_c2_effect_census.py` | 5,518 | 2026-10-14 14:40:39 | `a8e52d7e9f8d` | 噪声面 |
| 781 | `.tmp/docwriter_c2_effect_table.py` | 1,400 | 2026-10-14 14:43:24 | `503230d1e7e3` | 噪声面 |
| 782 | `.tmp/docwriter_c2_effect_table.txt` | 21,554 | 2026-10-14 14:43:33 | `1b5382cc9936` | 噪声面 |
| 783 | `.tmp/docwriter_corrigenda_2026_10_17.py` | 46,559 | 2026-10-17 10:50:36 | `e45d54855a21` | 噪声面 |
| 784 | `.tmp/docwriter_sigsup.py` | 13,645 | 2026-10-13 23:21:32 | `d116fefd336c` | 噪声面 |
| 785 | `.tmp/docwriter_v41_probe.py` | 6,503 | 2026-10-16 22:58:22 | `210a07303fe7` | 噪声面 |
| 786 | `.tmp/docwriter_v41_scan2.json` | 4,066 | 2026-10-16 22:59:21 | `e988b26ba229` | 噪声面 |
| 787 | `.tmp/docwriter_v41_scan2.py` | 3,661 | 2026-10-16 22:59:13 | `e88316a0fc2c` | 噪声面 |
| 788 | `.tmp/docwriter_v42_scan.py` | 4,601 | 2026-10-16 23:30:38 | `93d9c4c5c927` | 噪声面 |
| 789 | `.tmp/docwriter_v42_scan_out.txt` | 5,267 | 2026-10-16 23:30:52 | `d1470a9eaea9` | 噪声面 |
| 790 | `.tmp/docwriter_v42_verify.py` | 4,858 | 2026-10-16 23:37:19 | `47c794a64dff` | 噪声面 |
| 791 | `.tmp/docwriter_v42_verify_out.txt` | 2,899 | 2026-10-16 23:39:28 | `c38b853adda1` | 噪声面 |
| 792 | `.tmp/docwriter_v43_fp.py` | 1,488 | 2026-10-16 23:42:47 | `000c7e036d9c` | 噪声面 |
| 793 | `.tmp/docwriter_v43_fp2.py` | 1,716 | 2026-10-16 23:45:17 | `87ef5d8aba15` | 噪声面 |
| 794 | `.tmp/docwriter_v43_fp_out.txt` | 2,420 | 2026-10-16 23:45:26 | `35a223091bbe` | 噪声面 |
| 795 | `.tmp/docwriter_v43_scan.py` | 2,061 | 2026-10-16 23:43:51 | `5356708d6a6f` | 噪声面 |
| 796 | `.tmp/docwriter_v43_scan_out.txt` | 2,353 | 2026-10-16 23:44:03 | `c80e849e7c99` | 噪声面 |
| 797 | `.tmp/docwriter_v43_verify.py` | 4,497 | 2026-10-16 23:49:29 | `2cf26203f12d` | 噪声面 |
| 798 | `.tmp/docwriter_v43_verify_out.txt` | 759 | 2026-10-16 23:51:42 | `c1d14e3d7e06` | 噪声面 |
| 799 | `.tmp/docwriter_v44_fp.py` | 2,485 | 2026-10-17 00:00:58 | `4c2e2a4a2ad2` | 噪声面 |
| 800 | `.tmp/docwriter_v44_fp_out.txt` | 1,601 | 2026-10-17 00:01:08 | `6ab1382d766e` | 噪声面 |
| 801 | `.tmp/docwriter_v44_fresh.py` | 2,319 | 2026-10-17 00:14:18 | `855298e666f6` | 噪声面 |
| 802 | `.tmp/docwriter_v44_fresh_out.txt` | 1,646 | 2026-10-17 00:14:49 | `6d7d8ad5c4ed` | 噪声面 |
| 803 | `.tmp/docwriter_v44_scan.py` | 3,822 | 2026-10-17 00:02:38 | `3cc9fa3130a4` | 噪声面 |
| 804 | `.tmp/docwriter_v44_scan_out.txt` | 2,290 | 2026-10-17 00:02:52 | `24663bc22391` | 噪声面 |
| 805 | `.tmp/docwriter_v45_scan.py` | 5,186 | 2026-10-17 10:09:32 | `c6703629a7b0` | 噪声面 |
| 806 | `.tmp/docwriter_v45_scan_out.txt` | 1,661 | 2026-10-17 10:09:05 | `28c06dd53ae4` | 噪声面 |
| 807 | `.tmp/docwriter_v45_scan_out_r1.txt` | 1,661 | 2026-10-17 10:09:05 | `28c06dd53ae4` | 噪声面 |
| 808 | `.tmp/docwriter_v45_scan_out_r2.txt` | 1,728 | 2026-10-17 10:09:57 | `ef49039e5d90` | 噪声面 |
| 809 | `.tmp/docwriter_v45_scan_r2.py` | 4,212 | 2026-10-17 10:09:43 | `189764eebc91` | 噪声面 |
| 810 | `.tmp/docwriter_v45_verify_out.txt` | 2,031 | 2026-10-17 10:14:37 | `e5a0fdfbc914` | 噪声面 |
| 811 | `.tmp/docwriter_v46_append.py` | 6,444 | 2026-10-17 10:36:36 | `b54caa79c6a8` | 噪声面 |
| 812 | `.tmp/docwriter_v46_append_out.txt` | 538 | 2026-10-17 10:36:45 | `83aa47866622` | 噪声面 |
| 813 | `.tmp/docwriter_v46_card_raw.py` | 1,652 | 2026-10-17 10:28:16 | `b8754c12612b` | 噪声面 |
| 814 | `.tmp/docwriter_v46_card_raw.txt` | 26 | 2026-10-17 10:28:26 | `e31064337198` | 噪声面 |
| 815 | `.tmp/docwriter_v46_erratum.py` | 1,824 | 2026-10-17 10:37:13 | `7065b3466c7a` | 噪声面 |
| 816 | `.tmp/docwriter_v46_fix_ph.py` | 2,218 | 2026-10-17 10:38:44 | `32b99214da7f` | 噪声面 |
| 817 | `.tmp/docwriter_v46_probe.py` | 8,174 | 2026-10-17 10:25:58 | `15d2a2cef38c` | 噪声面 |
| 818 | `.tmp/docwriter_v46_probe_out.txt` | 10,158 | 2026-10-17 10:26:08 | `45358bad9e37` | 噪声面 |
| 819 | `.tmp/docwriter_v46_timeshift.py` | 3,075 | 2026-10-17 10:37:45 | `b0a103b331c4` | 噪声面 |
| 820 | `.tmp/docwriter_v46_timeshift_out.txt` | 708 | 2026-10-17 10:37:51 | `4623d2f470da` | 噪声面 |
| 821 | `.tmp/docwriter_v46_verify.py` | 6,883 | 2026-10-17 10:33:28 | `7d657b923cf3` | 噪声面 |
| 822 | `.tmp/docwriter_v46_verify_out.txt` | 4,060 | 2026-10-17 10:33:35 | `8cfd547d1234` | 噪声面 |
| 823 | `.tmp/docwriter_v46_verify_r2.py` | 3,940 | 2026-10-17 10:33:56 | `98878b701653` | 噪声面 |
| 824 | `.tmp/docwriter_v46_verify_r2_out.txt` | 1,922 | 2026-10-17 10:34:02 | `ba403f690aec` | 噪声面 |
| 825 | `.tmp/docwriter_v47_append.py` | 8,974 | 2026-10-17 10:54:24 | `aba550f33736` | 噪声面 |
| 826 | `.tmp/docwriter_v47_final.py` | 2,199 | 2026-10-17 10:54:36 | `eebb06bdf036` | 噪声面 |
| 827 | `.tmp/docwriter_v47_verify.py` | 1,220 | 2026-10-17 10:53:57 | `9383724baaa4` | 噪声面 |
| 828 | `.tmp/docwriter_v47_write1.py` | 62,466 | 2026-10-17 10:51:19 | `8fa8d72c3a69` | 噪声面 |
| 829 | `.tmp/docwriter_v47_write2.py` | 48,627 | 2026-10-17 10:53:02 | `1ee1ee14ac3e` | 噪声面 |
| 830 | `.tmp/docwriter_v48_norm.py` | 12,880 | 2026-10-17 11:11:16 | `e39ea2ab2756` | 噪声面 |
| 831 | `.tmp/docwriter_v48_norm_out.txt` | 1,345 | 2026-10-17 11:11:23 | `3e380b5a6fd3` | 噪声面 |
| 832 | `.tmp/docwriter_v48_probe.py` | 4,448 | 2026-10-17 11:06:47 | `8dfd0f40cdb5` | 噪声面 |
| 833 | `.tmp/docwriter_v48_probe_out.txt` | 4,169 | 2026-10-17 11:06:55 | `48b1c4a81ad4` | 噪声面 |
| 834 | `.tmp/docwriter_v48_selfnote.py` | 2,566 | 2026-10-17 11:12:10 | `e72e478e416c` | 噪声面 |
| 835 | `.tmp/docwriter_v49_norm.py` | 16,740 | 2026-10-17 11:23:11 | `d1b3481335eb` | 噪声面 |
| 836 | `.tmp/docwriter_v49_norm_out.txt` | 2,055 | 2026-10-17 11:23:23 | `4cba4f8bfbfc` | 噪声面 |
| 837 | `.tmp/docwriter_v49_probe.py` | 4,806 | 2026-10-17 11:17:59 | `753b0ad48557` | 噪声面 |
| 838 | `.tmp/docwriter_v49_probe_out.txt` | 4,353 | 2026-10-17 11:18:12 | `c04bcaf87623` | 噪声面 |
| 839 | `.tmp/docwriter_v50_append.py` | 4,218 | 2026-10-17 11:59:27 | `5bbe9112a3c4` | 噪声面 |
| 840 | `.tmp/docwriter_v50_norm.py` | 4,561 | 2026-10-17 11:58:38 | `156a380d1de7` | 噪声面 |
| 841 | `.tmp/docwriter_v50_probe.py` | 5,272 | 2026-10-17 11:53:46 | `8df564629f96` | 噪声面 |
| 842 | `.tmp/docwriter_v50_probe_out.txt` | 4,632 | 2026-10-17 11:53:58 | `22bad1830ba9` | 噪声面 |
| 843 | `.tmp/docwriter_v51_addendum.py` | 1,460 | 2026-10-17 12:21:18 | `0e5e1e2abf4b` | 噪声面 |
| 844 | `.tmp/docwriter_v51_addendum_out.txt` | 2,622 | 2026-10-17 12:21:27 | `c485fccba12f` | 噪声面 |
| 845 | `.tmp/docwriter_v51_append.py` | 4,002 | 2026-10-17 12:32:46 | `852f5fb67df4` | 噪声面 |
| 846 | `.tmp/docwriter_v51_norm.py` | 103,286 | 2026-10-17 12:27:53 | `56a9b29c3e23` | 噪声面 |
| 847 | `.tmp/docwriter_v51_probe.py` | 8,038 | 2026-10-17 12:20:34 | `4e5e90584b1d` | 噪声面 |
| 848 | `.tmp/docwriter_v51_probe_out.txt` | 12,060 | 2026-10-17 12:20:50 | `6bca892e5e2b` | 噪声面 |
| 849 | `.tmp/docwriter_verify_v44.py` | 4,692 | 2026-10-17 00:21:12 | `19cfb64700a1` | 噪声面 |
| 850 | `.tmp/docwriter_verify_v44_out.txt` | 2,371 | 2026-10-17 00:21:24 | `f3d33d095a8a` | 噪声面 |
| 851 | `.tmp/docwriter_verify_v45.py` | 3,780 | 2026-10-17 10:13:59 | `92230e228d83` | 噪声面 |
| 852 | `.tmp/docwriter_write_effect_v43.py` | 27,715 | 2026-10-16 23:51:17 | `01098529c399` | 噪声面 |
| 853 | `.tmp/docwriter_write_v42.py` | 66,543 | 2026-10-16 23:36:36 | `5cc438f6338d` | 噪声面 |
| 854 | `.tmp/docwriter_write_v43.py` | 33,607 | 2026-10-16 23:48:08 | `d5e6390b900d` | 噪声面 |
| 855 | `.tmp/docwriter_write_v44.py` | 84,551 | 2026-10-17 00:17:25 | `54812b76573b` | 噪声面 |
| 856 | `.tmp/docwriter_write_v45.py` | 61,168 | 2026-10-17 10:13:35 | `af3a22741b2f` | 噪声面 |
| 857 | `.tmp/dscan_01.json` | 195,396 | 2026-10-14 02:19:15 | `bab5d4a367af` | 噪声面 |
| 858 | `.tmp/dscan_01.py` | 2,865 | 2026-10-14 02:19:06 | `a58735d65c3c` | 噪声面 |
| 859 | `.tmp/dscan_02.py` | 5,078 | 2026-10-14 02:21:33 | `1f6ffd7e0f47` | 噪声面 |
| 860 | `.tmp/dscan_03.py` | 5,360 | 2026-10-14 02:22:29 | `35711329ad8f` | 噪声面 |
| 861 | `.tmp/dscan_04.py` | 2,302 | 2026-10-14 02:23:08 | `43e661f72888` | 噪声面 |
| 862 | `.tmp/dscan_05.py` | 6,207 | 2026-10-14 02:23:59 | `966d9ce0df2d` | 噪声面 |
| 863 | `.tmp/dscan_06.py` | 1,845 | 2026-10-14 02:24:18 | `7c059d996778` | 噪声面 |
| 864 | `.tmp/dscan_07.py` | 1,074 | 2026-10-14 02:24:43 | `26897ce01079` | 噪声面 |
| 865 | `.tmp/dscan_08.py` | 2,370 | 2026-10-14 02:25:13 | `fc3c78d3f0e5` | 噪声面 |
| 866 | `.tmp/dscan_classified.json` | 47,129 | 2026-10-14 02:21:38 | `458a2e06a2d3` | 噪声面 |
| 867 | `.tmp/dscan_classified.txt` | 11,199 | 2026-10-14 02:21:38 | `2945d458f5a6` | 噪声面 |
| 868 | `.tmp/dscan_copycmp.txt` | 687 | 2026-10-14 02:21:02 | `3af905a1f5c4` | 噪声面 |
| 869 | `.tmp/dscan_families.txt` | 3,535 | 2026-10-14 02:23:16 | `3bc5960fa2bf` | 噪声面 |
| 870 | `.tmp/dscan_matrix.json` | 273,930 | 2026-10-14 02:24:09 | `875f08dd0648` | 噪声面 |
| 871 | `.tmp/dscan_matrix.txt` | 1,452 | 2026-10-14 02:24:09 | `a8d3aa0287b6` | 噪声面 |
| 872 | `.tmp/dscan_repo_dump.txt` | 24,326 | 2026-10-14 02:20:10 | `06d5da0d55ed` | 噪声面 |
| 873 | `.tmp/dscan_stats.txt` | 2,712 | 2026-10-14 02:24:24 | `b35fb0ebd75d` | 噪声面 |
| 874 | `.tmp/dscan_sub_dump.txt` | 94,170 | 2026-10-14 02:20:35 | `8c3f99c0b128` | 噪声面 |
| 875 | `.tmp/dscan_tables.md` | 56,191 | 2026-10-14 02:25:19 | `0a96d4720449` | 噪声面 |
| 876 | `.tmp/dscan_write_01.py` | 23,330 | 2026-10-14 02:26:16 | `71cbf839d36b` | 噪声面 |
| 877 | `.tmp/dscan_xcheck.txt` | 3,196 | 2026-10-14 02:22:35 | `57dcd8344683` | 噪声面 |
| 878 | `.tmp/dw52_r_errata.py` | 11,560 | 2026-10-17 14:22:05 | `415afeb20d85` | 噪声面 |
| 879 | `.tmp/dw52_r_final.py` | 4,295 | 2026-10-17 14:20:12 | `18020dd8fc50` | 噪声面 |
| 880 | `.tmp/dw52_r_final2.py` | 4,213 | 2026-10-17 14:22:39 | `ab16b8f0f1a4` | 噪声面 |
| 881 | `.tmp/dw52_r_final2_out.txt` | 8,078 | 2026-10-17 14:22:53 | `d745ab86a9ea` | 噪声面 |
| 882 | `.tmp/dw52_r_final_out.txt` | 5,216 | 2026-10-17 14:20:27 | `68d9067a6636` | 噪声面 |
| 883 | `.tmp/dw52_r_fix6.py` | 3,518 | 2026-10-17 14:17:32 | `1714dc8542ee` | 噪声面 |
| 884 | `.tmp/dw52_r_norm.py` | 1,413 | 2026-10-17 14:15:51 | `86ad684afb4b` | 噪声面 |
| 885 | `.tmp/dw52_r_probe1.py` | 2,183 | 2026-10-17 14:05:56 | `e3cb5ed912a0` | 噪声面 |
| 886 | `.tmp/dw52_r_probe2.py` | 2,767 | 2026-10-17 14:06:25 | `629b3f880066` | 噪声面 |
| 887 | `.tmp/dw52_r_probe3.py` | 3,905 | 2026-10-17 14:08:17 | `2afe00f1759b` | 噪声面 |
| 888 | `.tmp/dw52_r_probe3_out.txt` | 10,585 | 2026-10-17 14:08:58 | `fba3bacf42a3` | 噪声面 |
| 889 | `.tmp/dw52_r_r3probe.py` | 2,437 | 2026-10-17 14:20:56 | `f24aa16ce147` | 噪声面 |
| 890 | `.tmp/dw52_r_r3probe_out.txt` | 6,960 | 2026-10-17 14:21:17 | `ac070e24b6a4` | 噪声面 |
| 891 | `.tmp/dw52_r_write_effect.py` | 23,146 | 2026-10-17 14:19:25 | `38caa88650c4` | 噪声面 |
| 892 | `.tmp/dw52_r_write_v52.py` | 54,040 | 2026-10-17 14:14:14 | `757d34bfa17c` | 噪声面 |
| 893 | `.tmp/dw53_append_errata.py` | 2,511 | 2026-10-17 15:23:34 | `2f8a4e8e65f0` | 噪声面 |
| 894 | `.tmp/dw53_b11.py` | 963 | 2026-10-17 15:16:33 | `741e41ff787c` | 噪声面 |
| 895 | `.tmp/dw53_b11_out.txt` | 3,941 | 2026-10-17 15:16:33 | `4d7a36693b0c` | 噪声面 |
| 896 | `.tmp/dw53_final.py` | 3,067 | 2026-10-17 15:22:05 | `ccf618204dc0` | 噪声面 |
| 897 | `.tmp/dw53_final_out.txt` | 4,210 | 2026-10-17 15:22:06 | `3afecc30fda2` | 噪声面 |
| 898 | `.tmp/dw53_measure.py` | 2,870 | 2026-10-17 15:19:17 | `247f9c11f2cd` | 噪声面 |
| 899 | `.tmp/dw53_measure_out.txt` | 3,207 | 2026-10-17 15:19:17 | `ee341c7d5aaf` | 噪声面 |
| 900 | `.tmp/dw53_post.py` | 1,710 | 2026-10-17 15:24:08 | `f430f3911389` | 噪声面 |
| 901 | `.tmp/dw53_post_out.txt` | 2,651 | 2026-10-17 15:24:08 | `7507a8ae8a4d` | 噪声面 |
| 902 | `.tmp/dw53_probe_all.py` | 3,831 | 2026-10-17 15:16:18 | `3ee11992af61` | 噪声面 |
| 903 | `.tmp/dw53_probe_sha.py` | 1,006 | 2026-10-17 15:15:13 | `39cc5a83be41` | 噪声面 |
| 904 | `.tmp/dw53_r_write_effect.py` | 45,526 | 2026-10-17 15:21:18 | `1f69857d06d9` | 噪声面 |
| 905 | `.tmp/dw53_r_write_v53.py` | 52,505 | 2026-10-17 15:18:50 | `579b6d43786b` | 噪声面 |
| 906 | `.tmp/dw54_probe1.py` | 5,086 | 2026-10-17 15:52:55 | `a57de53e1d1a` | 噪声面 |
| 907 | `.tmp/dw54_probe1_out.txt` | 11,505 | 2026-10-17 15:53:04 | `884ef766a246` | 噪声面 |
| 908 | `.tmp/dw54_probe2.py` | 3,648 | 2026-10-17 15:53:43 | `cb19f34f9d8d` | 噪声面 |
| 909 | `.tmp/dw54_probe2_out.txt` | 11,801 | 2026-10-17 15:53:50 | `d0f63cdd7de2` | 噪声面 |
| 910 | `.tmp/dw54_probe3.py` | 5,727 | 2026-10-17 15:54:29 | `9a8b6cee887b` | 噪声面 |
| 911 | `.tmp/dw54_probe3_out.txt` | 9,739 | 2026-10-17 15:54:35 | `6d6edc7b2e32` | 噪声面 |
| 912 | `.tmp/dw54_probe4.py` | 3,610 | 2026-10-17 15:54:54 | `c139ae500683` | 噪声面 |
| 913 | `.tmp/dw54_probe4_out.txt` | 1,395 | 2026-10-17 15:55:02 | `237accc918fb` | 噪声面 |
| 914 | `.tmp/dw54_probe5.py` | 2,358 | 2026-10-17 15:55:14 | `12f359252930` | 噪声面 |
| 915 | `.tmp/dw54_probe5_out.txt` | 969 | 2026-10-17 15:55:23 | `e2df89bdcfdd` | 噪声面 |
| 916 | `.tmp/dw54_probe6.py` | 3,192 | 2026-10-17 15:56:19 | `23d3cf35a584` | 噪声面 |
| 917 | `.tmp/dw54_probe6_out.txt` | 5,829 | 2026-10-17 15:56:27 | `875d024bc9e5` | 噪声面 |
| 918 | `.tmp/dw54_probe7.py` | 6,996 | 2026-10-17 16:01:23 | `b0615a8f37ec` | 噪声面 |
| 919 | `.tmp/dw54_probe7_out.txt` | 4,310 | 2026-10-17 16:02:50 | `1b4c064b7e7e` | 噪声面 |
| 920 | `.tmp/dw54_probe7_tail.txt` | 1,363 | 2026-10-17 16:03:04 | `5daac7d6b92e` | 噪声面 |
| 921 | `.tmp/dw54_w_effect.py` | 46,212 | 2026-10-17 16:00:45 | `784b80952f08` | 噪声面 |
| 922 | `.tmp/dw54_w_errata.py` | 4,413 | 2026-10-17 16:02:08 | `c016e35d5ca1` | 噪声面 |
| 923 | `.tmp/dw54_w_errata3.py` | 4,966 | 2026-10-17 16:02:43 | `b5e0152a9cbb` | 噪声面 |
| 924 | `.tmp/dw54_w_v54.py` | 67,193 | 2026-10-17 15:58:51 | `812515b75122` | 噪声面 |
| 925 | `.tmp/dw55_probe.py` | 5,330 | 2026-10-17 15:59:47 | `c038a263191b` | 噪声面 |
| 926 | `.tmp/dw55_probe_out.txt` | 8,615 | 2026-10-17 15:59:58 | `abf58e0d3cb6` | 噪声面 |
| 927 | `.tmp/dw55_w_adopt.py` | 37,155 | 2026-10-17 16:04:33 | `72c172c18cd0` | 噪声面 |
| 928 | `.tmp/dw55_w_append.py` | 8,380 | 2026-10-17 16:05:26 | `52fb9722ea75` | 噪声面 |
| 929 | `.tmp/dw55_w_v55.py` | 50,945 | 2026-10-17 16:02:56 | `6d474cc82852` | 噪声面 |
| 930 | `.tmp/dw56_payload_c5effect.md` | 24,464 | 2026-10-17 16:18:18 | `91fe9a16059d` | 噪声面 |
| 931 | `.tmp/dw56_payload_v56.md` | 51,458 | 2026-10-17 16:17:22 | `d4c5d4988944` | 噪声面 |
| 932 | `.tmp/dw56_probe.py` | 5,880 | 2026-10-17 16:14:45 | `0a45438a3b6a` | 噪声面 |
| 933 | `.tmp/dw56_probe_out.txt` | 5,488 | 2026-10-17 16:15:00 | `944761608ffc` | 噪声面 |
| 934 | `.tmp/dw56_write.py` | 3,428 | 2026-10-17 16:18:30 | `16de51516bde` | 噪声面 |
| 935 | `.tmp/dw56_write_out.txt` | 3,212 | 2026-10-17 16:18:36 | `f016dc951b62` | 噪声面 |
| 936 | `.tmp/dw56r_append_s8.py` | 6,016 | 2026-10-17 16:28:22 | `4c6b0c87cccc` | 噪声面 |
| 937 | `.tmp/dw56r_probe_math.py` | 5,845 | 2026-10-17 16:23:40 | `88422479fd4e` | 噪声面 |
| 938 | `.tmp/dw56r_probe_math2.py` | 3,727 | 2026-10-17 16:24:30 | `57c8411a31b4` | 噪声面 |
| 939 | `.tmp/dw56r_probe_math3.py` | 3,155 | 2026-10-17 16:25:42 | `f49778d9c6b9` | 噪声面 |
| 940 | `.tmp/dw56r_probe_math_out.txt` | 1,947 | 2026-10-17 16:23:51 | `c03168cf32fd` | 噪声面 |
| 941 | `.tmp/dw56r_probe_math_out2.txt` | 2,848 | 2026-10-17 16:24:39 | `36c5db29174c` | 噪声面 |
| 942 | `.tmp/dw56r_probe_math_out3.txt` | 2,704 | 2026-10-17 16:25:50 | `0352807cd208` | 噪声面 |
| 943 | `.tmp/dw56r_write_audit.py` | 30,171 | 2026-10-17 16:27:43 | `9e42972aed7b` | 噪声面 |
| 944 | `.tmp/dw58_check.py` | 487 | 2026-10-17 16:38:44 | `a0f362810fe5` | 噪声面 |
| 945 | `.tmp/dw58_fix.py` | 427 | 2026-10-17 16:38:53 | `305689b44c17` | 噪声面 |
| 946 | `.tmp/dw58_payload_effect.md` | 22,894 | 2026-10-17 16:38:53 | `d34d769afaca` | 噪声面 |
| 947 | `.tmp/dw58_payload_v58.md` | 43,565 | 2026-10-17 16:37:38 | `e15de4a194e0` | 噪声面 |
| 948 | `.tmp/dw58_probe.py` | 5,468 | 2026-10-17 16:34:45 | `2f2a89e76ed6` | 噪声面 |
| 949 | `.tmp/dw58_probe_out.txt` | 6,109 | 2026-10-17 16:35:05 | `289b002e18cb` | 噪声面 |
| 950 | `.tmp/dw58_recheck.py` | 1,561 | 2026-10-17 16:39:38 | `7dc9f88dca97` | 噪声面 |
| 951 | `.tmp/dw58_verify.py` | 2,113 | 2026-10-17 16:39:03 | `52610c0e2710` | 噪声面 |
| 952 | `.tmp/dw58_write.py` | 1,827 | 2026-10-17 16:39:03 | `609d591cbdbe` | 噪声面 |
| 953 | `.tmp/dw59_probe1.py` | 1,305 | 2026-10-17 16:49:40 | `70673cfdde9b` | 噪声面 |
| 954 | `.tmp/dw59_probe2.py` | 3,101 | 2026-10-17 16:50:35 | `a05d70b8fb08` | 噪声面 |
| 955 | `.tmp/dw59_probe3.py` | 1,445 | 2026-10-17 16:54:10 | `d90828421c5e` | 噪声面 |
| 956 | `.tmp/dw59_verify.py` | 2,304 | 2026-10-17 16:56:17 | `a09fd3f0875c` | 噪声面 |
| 957 | `.tmp/dw59_write1.py` | 46,473 | 2026-10-17 16:55:57 | `94cde54945ee` | 噪声面 |
| 958 | `.tmp/dw59_write2.py` | 38,698 | 2026-10-17 16:54:55 | `e11ac7f80434` | 噪声面 |
| 959 | `.tmp/dw60_probe1.py` | 7,509 | 2026-10-17 17:02:46 | `a0ac672ef9c4` | 噪声面 |
| 960 | `.tmp/dw60_verify.py` | 5,897 | 2026-10-17 17:09:57 | `17c058defd6b` | 噪声面 |
| 961 | `.tmp/dw60_write1.py` | 50,445 | 2026-10-17 17:07:26 | `d09c0882ad38` | 噪声面 |
| 962 | `.tmp/dw60_write2.py` | 33,371 | 2026-10-17 17:09:29 | `c37d4cf3ba78` | 噪声面 |
| 963 | `.tmp/dw61_probe1.out.txt` | 4,747 | 2026-10-17 17:12:30 | `67ea224a54d0` | 噪声面 |
| 964 | `.tmp/dw61_probe1.py` | 6,160 | 2026-10-17 17:12:20 | `47177bc9455a` | 噪声面 |
| 965 | `.tmp/dw61_verify1.out.txt` | 3,416 | 2026-10-17 17:15:59 | `1d43b10221fa` | 噪声面 |
| 966 | `.tmp/dw61_verify1.py` | 5,105 | 2026-10-17 17:15:52 | `c83e875409cb` | 噪声面 |
| 967 | `.tmp/dw61_write1.py` | 40,197 | 2026-10-17 17:15:20 | `b8caf9664918` | 噪声面 |
| 968 | `.tmp/dw62_probe1.out.json` | 15,870 | 2026-10-17 17:36:32 | `57ada01beadc` | 噪声面 |
| 969 | `.tmp/dw62_probe1.py` | 7,703 | 2026-10-17 17:36:18 | `280733d42c12` | 噪声面 |
| 970 | `.tmp/dw62_verify1.out.txt` | 10,344 | 2026-10-17 17:44:04 | `c3c39aaafcb2` | 噪声面 |
| 971 | `.tmp/dw62_verify1.py` | 5,918 | 2026-10-17 17:43:56 | `6fab772b4f73` | 噪声面 |
| 972 | `.tmp/dw62_write1.py` | 45,978 | 2026-10-17 17:40:32 | `96bd1caf94c6` | 噪声面 |
| 973 | `.tmp/dw62_write2.py` | 32,352 | 2026-10-17 17:43:18 | `b99c768cff9d` | 噪声面 |
| 974 | `.tmp/dw63_probe_a.py` | 464 | 2026-10-17 17:52:21 | `1a9c69d9e493` | 噪声面 |
| 975 | `.tmp/dw63_probe_b.py` | 2,909 | 2026-10-17 17:52:57 | `3ef4960dbffc` | 噪声面 |
| 976 | `.tmp/dw63_probe_c.py` | 1,649 | 2026-10-17 17:53:13 | `92e29506f242` | 噪声面 |
| 977 | `.tmp/dw63_probe_d.py` | 1,997 | 2026-10-17 17:58:08 | `87b7ca70a4cc` | 噪声面 |
| 978 | `.tmp/dw63_probe_d_out.txt` | 1,710 | 2026-10-17 17:58:11 | `df066efd8178` | 噪声面 |
| 979 | `.tmp/dw63_probe_e.py` | 3,407 | 2026-10-17 17:58:48 | `a365f17d839d` | 噪声面 |
| 980 | `.tmp/dw63_probe_e_out.txt` | 1,515 | 2026-10-17 17:58:54 | `5d2792ccf1f8` | 噪声面 |
| 981 | `.tmp/dw63_probe_scan.py` | 2,095 | 2026-10-17 17:53:55 | `6e1853312bb8` | 噪声面 |
| 982 | `.tmp/dw63_probe_scan_out.txt` | 1,953 | 2026-10-17 17:53:59 | `7fab50203f97` | 噪声面 |
| 983 | `.tmp/dw63_verify.out.txt` | 3,168 | 2026-10-17 17:57:53 | `8ebf8dc97f1e` | 噪声面 |
| 984 | `.tmp/dw63_verify.py` | 4,771 | 2026-10-17 17:57:45 | `f0169eb7a436` | 噪声面 |
| 985 | `.tmp/dw63_verify_append1.out.txt` | 5,335 | 2026-10-17 18:00:47 | `8cba56d5cb6b` | 噪声面 |
| 986 | `.tmp/dw63_verify_append1.py` | 5,979 | 2026-10-17 18:00:34 | `ce52bcfbfc2b` | 噪声面 |
| 987 | `.tmp/dw63_write.py` | 87,918 | 2026-10-17 17:56:54 | `29897c0d2322` | 噪声面 |
| 988 | `.tmp/dw63_write_append1.py` | 42,008 | 2026-10-17 18:00:16 | `352000396c3c` | 噪声面 |
| 989 | `.tmp/dw66_diag.py` | 551 | 2026-10-17 18:56:56 | `1a48f593f24c` | 噪声面 |
| 990 | `.tmp/dw66_diag.txt` | 652 | 2026-10-17 18:56:56 | `fec7ddfa329d` | 噪声面 |
| 991 | `.tmp/dw66_diag2.py` | 378 | 2026-10-17 18:57:39 | `a8262c6dc57c` | 噪声面 |
| 992 | `.tmp/dw66_diag2.txt` | 957 | 2026-10-17 18:57:39 | `a70bb55e5f58` | 噪声面 |
| 993 | `.tmp/dw66_dir.py` | 627 | 2026-10-17 19:01:25 | `befd9129f0c6` | 噪声面 |
| 994 | `.tmp/dw66_dir.txt` | 5,734 | 2026-10-17 19:01:26 | `1fb97ad851b5` | 噪声面 |
| 995 | `.tmp/dw66_final.py` | 1,214 | 2026-10-17 19:02:07 | `43a2db55bdb8` | 噪声面 |
| 996 | `.tmp/dw66_final.txt` | 860 | 2026-10-17 19:02:07 | `4fb3ca55eea4` | 噪声面 |
| 997 | `.tmp/dw66_fix.py` | 692 | 2026-10-17 18:58:03 | `68cba4a108a3` | 噪声面 |
| 998 | `.tmp/dw66_fix2.py` | 1,120 | 2026-10-17 18:59:38 | `ac06906ed651` | 噪声面 |
| 999 | `.tmp/dw66_probe_a.py` | 1,239 | 2026-10-17 18:50:49 | `eb26c4d5deea` | 噪声面 |
| 1000 | `.tmp/dw66_probe_b.py` | 848 | 2026-10-17 18:51:08 | `90f88b6412fb` | 噪声面 |
| 1001 | `.tmp/dw66_probe_scan.py` | 1,537 | 2026-10-17 18:51:34 | `32d8fd5bf9d0` | 噪声面 |
| 1002 | `.tmp/dw66_probe_scan2.py` | 1,803 | 2026-10-17 18:51:52 | `be57aaa77ed7` | 噪声面 |
| 1003 | `.tmp/dw66_probe_scan_out.txt` | 1,217 | 2026-10-17 18:51:54 | `bbd0335e41c8` | 噪声面 |
| 1004 | `.tmp/dw66_recheck.out.txt` | 911 | 2026-10-17 18:59:23 | `4c44d3915202` | 噪声面 |
| 1005 | `.tmp/dw66_recheck.py` | 1,106 | 2026-10-17 18:59:16 | `8c860537dde9` | 噪声面 |
| 1006 | `.tmp/dw66_verify.out.txt` | 1,781 | 2026-10-17 18:58:33 | `6853deb4c67d` | 噪声面 |
| 1007 | `.tmp/dw66_verify.py` | 3,152 | 2026-10-17 18:58:26 | `41e9d50962f1` | 噪声面 |
| 1008 | `.tmp/dw66_verify2.out.txt` | 1,518 | 2026-10-17 18:58:53 | `ee4d38c06996` | 噪声面 |
| 1009 | `.tmp/dw66_verify2.py` | 1,529 | 2026-10-17 18:58:53 | `d6e8db9a0fd8` | 噪声面 |
| 1010 | `.tmp/dw66_verify3.out.txt` | 894 | 2026-10-17 19:00:59 | `255cdd522e5d` | 噪声面 |
| 1011 | `.tmp/dw66_verify3.py` | 1,452 | 2026-10-17 19:00:59 | `f15f0d441ceb` | 噪声面 |
| 1012 | `.tmp/dw66_write_append1.py` | 13,075 | 2026-10-17 19:00:42 | `aeb5c024e321` | 噪声面 |
| 1013 | `.tmp/dw66_write_append2.py` | 6,584 | 2026-10-17 19:01:57 | `627d4a59b169` | 噪声面 |
| 1014 | `.tmp/dw66_write_effect.py` | 36,495 | 2026-10-17 18:58:09 | `c80cde71954c` | 噪声面 |
| 1015 | `.tmp/dw66_write_v66.py` | 49,816 | 2026-10-17 18:54:32 | `ac42765cc15b` | 噪声面 |
| 1016 | `.tmp/dw67_probe_a.py` | 3,381 | 2026-10-17 18:56:54 | `ccffe9dd9be2` | 噪声面 |
| 1017 | `.tmp/dw67_probe_a_out.txt` | 2,464 | 2026-10-17 18:57:02 | `4480224ea3a3` | 噪声面 |
| 1018 | `.tmp/dw67_probe_b.py` | 3,557 | 2026-10-17 18:57:17 | `2ead05c573de` | 噪声面 |
| 1019 | `.tmp/dw67_probe_b_out.txt` | 1,684 | 2026-10-17 18:57:31 | `e7bbf74cece4` | 噪声面 |
| 1020 | `.tmp/dw67_probe_c.py` | 1,251 | 2026-10-17 18:57:39 | `9333c129be22` | 噪声面 |
| 1021 | `.tmp/dw67_probe_c_out.txt` | 2,987 | 2026-10-17 18:58:04 | `80b412b6f4e5` | 噪声面 |
| 1022 | `.tmp/dw67_verify.out.txt` | 2,116 | 2026-10-17 19:05:23 | `435a27e85d97` | 噪声面 |
| 1023 | `.tmp/dw67_verify.py` | 2,815 | 2026-10-17 19:05:17 | `94728ace730a` | 噪声面 |
| 1024 | `.tmp/dw67_write_effect.py` | 36,932 | 2026-10-17 19:05:13 | `3486db943f29` | 噪声面 |
| 1025 | `.tmp/dw67_write_v67.py` | 48,826 | 2026-10-17 19:04:51 | `6f384c2ff037` | 噪声面 |
| 1026 | `.tmp/dw68_final.out.txt` | 1,098 | 2026-10-17 19:14:23 | `4639d4ecd6f3` | 噪声面 |
| 1027 | `.tmp/dw68_final.py` | 2,672 | 2026-10-17 19:14:23 | `796442edbec1` | 噪声面 |
| 1028 | `.tmp/dw68_payload_effect.md` | 30,133 | 2026-10-17 19:13:42 | `cb1723499a25` | 噪声面 |
| 1029 | `.tmp/dw68_payload_v68.md` | 49,383 | 2026-10-17 19:13:42 | `d60379221f29` | 噪声面 |
| 1030 | `.tmp/dw68_probe_a.py` | 2,117 | 2026-10-17 19:04:04 | `cc7711e63ff0` | 噪声面 |
| 1031 | `.tmp/dw68_probe_b.py` | 1,106 | 2026-10-17 19:04:22 | `9b6977c86b12` | 噪声面 |
| 1032 | `.tmp/dw68_probe_c.py` | 1,134 | 2026-10-17 19:05:02 | `f05448b67087` | 噪声面 |
| 1033 | `.tmp/dw68_probe_d.py` | 1,854 | 2026-10-17 19:05:23 | `63f37c940db4` | 噪声面 |
| 1034 | `.tmp/dw68_probe_d_out.txt` | 1,668 | 2026-10-17 19:05:26 | `bd76566236ef` | 噪声面 |
| 1035 | `.tmp/dw68_verify.out.txt` | 1,945 | 2026-10-17 19:13:53 | `e11fc3b79e4b` | 噪声面 |
| 1036 | `.tmp/dw68_verify.py` | 3,523 | 2026-10-17 19:13:07 | `e4437867415a` | 噪声面 |
| 1037 | `.tmp/dw68_write.out.txt` | 4,027 | 2026-10-17 19:12:08 | `cb26534eb724` | 噪声面 |
| 1038 | `.tmp/dw68_write.py` | 5,299 | 2026-10-17 19:06:32 | `5307abebb39a` | 噪声面 |
| 1039 | `.tmp/dw720_calc_2026_10_16.py` | 1,797 | 2026-10-16 11:40:35 | `5da6bf2d700a` | 噪声面 |
| 1040 | `.tmp/dw720_probe_2026_10_16.py` | 1,450 | 2026-10-16 11:37:52 | `efdb4c877f3f` | 噪声面 |
| 1041 | `.tmp/dw720_verify_2026_10_16.py` | 3,909 | 2026-10-16 11:42:24 | `c90f9a64c3d8` | 噪声面 |
| 1042 | `.tmp/dw720_write_2026_10_16.py` | 29,681 | 2026-10-16 11:42:01 | `46e8be383b3c` | 噪声面 |
| 1043 | `.tmp/dw72_probe1.py` | 1,084 | 2026-10-17 19:43:10 | `127754f2b66a` | 噪声面 |
| 1044 | `.tmp/dw72_probe2.py` | 2,804 | 2026-10-17 19:44:07 | `b5d50e29f867` | 噪声面 |
| 1045 | `.tmp/dw72_probe3.py` | 2,073 | 2026-10-17 19:44:25 | `7cd02ec22927` | 噪声面 |
| 1046 | `.tmp/dw72_probe4.py` | 1,965 | 2026-10-17 19:44:56 | `a45fecd0442b` | 噪声面 |
| 1047 | `.tmp/dw72_verify.py` | 5,583 | 2026-10-17 19:51:07 | `dfcfbd97f541` | 噪声面 |
| 1048 | `.tmp/dw72_write1.py` | 34,422 | 2026-10-17 19:47:50 | `351b5b79205a` | 噪声面 |
| 1049 | `.tmp/dw72_write2.py` | 34,917 | 2026-10-17 19:50:26 | `1197bb550042` | 噪声面 |
| 1050 | `.tmp/dw74_probe1.out.txt` | 3,090 | 2026-10-17 19:57:12 | `a25f946975a5` | 噪声面 |
| 1051 | `.tmp/dw74_probe1.py` | 2,861 | 2026-10-17 19:57:02 | `bd4bc12aa50a` | 噪声面 |
| 1052 | `.tmp/dw74_probe2.out.txt` | 2,558 | 2026-10-17 19:57:53 | `3159fc4722ce` | 噪声面 |
| 1053 | `.tmp/dw74_probe2.py` | 3,312 | 2026-10-17 19:57:38 | `8434e940f7b6` | 噪声面 |
| 1054 | `.tmp/dw74_verify.out.txt` | 2,896 | 2026-10-17 20:01:45 | `acc64edbbf18` | 噪声面 |
| 1055 | `.tmp/dw74_verify.py` | 1,449 | 2026-10-17 20:01:10 | `f3deae6de211` | 噪声面 |
| 1056 | `.tmp/dw74_verify2.py` | 2,096 | 2026-10-17 20:01:40 | `a2ba7366fccb` | 噪声面 |
| 1057 | `.tmp/dw74_write.py` | 46,112 | 2026-10-17 20:00:56 | `105f5cd277c5` | 噪声面 |
| 1058 | `.tmp/dw74_勘误追加.py` | 2,829 | 2026-10-17 20:02:03 | `848e1ff5e9ca` | 噪声面 |
| 1059 | `.tmp/dw75_patch1.py` | 3,095 | 2026-10-17 20:14:33 | `a653f5054eec` | 噪声面 |
| 1060 | `.tmp/dw75_patch2.py` | 3,840 | 2026-10-17 20:15:03 | `cda17db939e3` | 噪声面 |
| 1061 | `.tmp/dw75_probe1.out.txt` | 8,690 | 2026-10-17 20:08:11 | `af26bc4323b7` | 噪声面 |
| 1062 | `.tmp/dw75_probe1.py` | 17 | 2026-10-17 20:08:11 | `4a309a6ca130` | 噪声面 |
| 1063 | `.tmp/dw75_probe2.out.txt` | 2,767 | 2026-10-17 20:08:37 | `8fb37805b2a1` | 噪声面 |
| 1064 | `.tmp/dw75_probe2.py` | 17 | 2026-10-17 20:08:37 | `1dcb180e74da` | 噪声面 |
| 1065 | `.tmp/dw75_probe3.out.txt` | 2,386 | 2026-10-17 20:09:04 | `c3e06067273b` | 噪声面 |
| 1066 | `.tmp/dw75_probe3.py` | 17 | 2026-10-17 20:09:04 | `091a7849c520` | 噪声面 |
| 1067 | `.tmp/dw75_probe4.out.txt` | 1,166 | 2026-10-17 20:14:20 | `3a334272ea39` | 噪声面 |
| 1068 | `.tmp/dw75_probe4.py` | 17 | 2026-10-17 20:14:20 | `00d9a33c228b` | 噪声面 |
| 1069 | `.tmp/dw75_run1.py` | 3,340 | 2026-10-17 20:07:50 | `6be91fbd5bae` | 噪声面 |
| 1070 | `.tmp/dw75_run2.py` | 4,174 | 2026-10-17 20:08:31 | `4eb1d28abe74` | 噪声面 |
| 1071 | `.tmp/dw75_run3.py` | 2,498 | 2026-10-17 20:08:52 | `46f946bb5762` | 噪声面 |
| 1072 | `.tmp/dw75_run4.py` | 1,757 | 2026-10-17 20:14:20 | `684d336e52ef` | 噪声面 |
| 1073 | `.tmp/dw75_verify.out.txt` | 1,511 | 2026-10-17 20:15:18 | `1ae1abd67e57` | 噪声面 |
| 1074 | `.tmp/dw75_verify.py` | 2,313 | 2026-10-17 20:13:45 | `9625fabf75f7` | 噪声面 |
| 1075 | `.tmp/dw75_write1.py` | 81,327 | 2026-10-17 20:13:31 | `abdbd55abe15` | 噪声面 |
| 1076 | `.tmp/dw76_cross.out.txt` | 182 | 2026-10-17 20:22:58 | `71c6005724cf` | 噪声面 |
| 1077 | `.tmp/dw76_cross.py` | 1,133 | 2026-10-17 20:22:58 | `8da3435cc701` | 噪声面 |
| 1078 | `.tmp/dw76_fffd.out.txt` | 363 | 2026-10-17 20:21:54 | `bfa97f2b6be8` | 噪声面 |
| 1079 | `.tmp/dw76_fffd.py` | 625 | 2026-10-17 20:21:54 | `c8d790d23b19` | 噪声面 |
| 1080 | `.tmp/dw76_probe0.py` | 1,420 | 2026-10-17 20:15:19 | `23db85bb14eb` | 噪声面 |
| 1081 | `.tmp/dw76_probe1.out.txt` | 3,948 | 2026-10-17 20:15:55 | `6a978acda0e7` | 噪声面 |
| 1082 | `.tmp/dw76_probe1.py` | 2,306 | 2026-10-17 20:15:49 | `c67167b4362e` | 噪声面 |
| 1083 | `.tmp/dw76_probe2.out.txt` | 198 | 2026-10-17 20:16:18 | `997dbed7dfaf` | 噪声面 |
| 1084 | `.tmp/dw76_probe2.py` | 647 | 2026-10-17 20:16:14 | `f5f386e64665` | 噪声面 |
| 1085 | `.tmp/dw76_probe3.out.txt` | 3,992 | 2026-10-17 20:17:08 | `e0ee21457eb4` | 噪声面 |
| 1086 | `.tmp/dw76_probe3.py` | 627 | 2026-10-17 20:17:08 | `d4c30827efef` | 噪声面 |
| 1087 | `.tmp/dw76_verify.out.txt` | 636 | 2026-10-17 20:22:36 | `8ab77576ed65` | 噪声面 |
| 1088 | `.tmp/dw76_verify.py` | 1,700 | 2026-10-17 20:21:34 | `0d472ee51177` | 噪声面 |
| 1089 | `.tmp/dw76_write1.py` | 50,812 | 2026-10-17 20:22:19 | `92518b3309a0` | 噪声面 |
| 1090 | `.tmp/dw76_write2.py` | 30,718 | 2026-10-17 20:22:26 | `d6153aeb2125` | 噪声面 |
| 1091 | `.tmp/dw77_probe0.out.txt` | 1,255 | 2026-10-17 20:38:58 | `16eaf3d90cc8` | 噪声面 |
| 1092 | `.tmp/dw77_probe0.py` | 3,578 | 2026-10-17 20:38:36 | `639aad9f614a` | 噪声面 |
| 1093 | `.tmp/dw77_probe1.out.txt` | 2,767 | 2026-10-17 20:39:33 | `e03a2ad13211` | 噪声面 |
| 1094 | `.tmp/dw77_probe1.py` | 4,652 | 2026-10-17 20:39:17 | `3a871fd4c0c1` | 噪声面 |
| 1095 | `.tmp/dw77_verify.out.txt` | 4,783 | 2026-10-17 20:44:11 | `2952a41c9c5f` | 噪声面 |
| 1096 | `.tmp/dw77_verify.py` | 4,621 | 2026-10-17 20:44:00 | `eef1343080f1` | 噪声面 |
| 1097 | `.tmp/dw77_write1.py` | 47,878 | 2026-10-17 20:41:47 | `f6b520547f46` | 噪声面 |
| 1098 | `.tmp/dw77_write2.py` | 51,765 | 2026-10-17 20:43:36 | `0efd4cf284e5` | 噪声面 |
| 1099 | `.tmp/dw78_append9.py` | 3,891 | 2026-10-17 20:51:02 | `e1e56d7077c4` | 噪声面 |
| 1100 | `.tmp/dw78_fix1.out.txt` | 448 | 2026-10-17 20:49:22 | `4c81fb2d558d` | 噪声面 |
| 1101 | `.tmp/dw78_fix1.py` | 1,014 | 2026-10-17 20:49:15 | `e15656cde162` | 噪声面 |
| 1102 | `.tmp/dw78_probe0.out.txt` | 2,065 | 2026-10-17 20:41:32 | `fada6ea8def6` | 噪声面 |
| 1103 | `.tmp/dw78_probe0.py` | 2,945 | 2026-10-17 20:41:23 | `38ca1cadc48a` | 噪声面 |
| 1104 | `.tmp/dw78_probe1.out.txt` | 2,360 | 2026-10-17 20:42:42 | `0318d077763b` | 噪声面 |
| 1105 | `.tmp/dw78_probe1.py` | 3,654 | 2026-10-17 20:42:28 | `627b3c9f1df4` | 噪声面 |
| 1106 | `.tmp/dw78_verify.out.txt` | 2,810 | 2026-10-17 20:49:53 | `e64fbb74c8f8` | 噪声面 |
| 1107 | `.tmp/dw78_verify.py` | 4,466 | 2026-10-17 20:49:43 | `fe803a37154a` | 噪声面 |
| 1108 | `.tmp/dw78_verify2.out.txt` | 205 | 2026-10-17 20:51:12 | `e0565d8a8908` | 噪声面 |
| 1109 | `.tmp/dw78_write1.py` | 58,317 | 2026-10-17 20:46:19 | `119c329d8f1a` | 噪声面 |
| 1110 | `.tmp/dw78_write2.py` | 42,033 | 2026-10-17 20:49:22 | `fdf660fefbe7` | 噪声面 |
| 1111 | `.tmp/dw_arm_erratum_write_2026_10_17.py` | 20,357 | 2026-10-17 17:05:06 | `9f85a58fc1bc` | 噪声面 |
| 1112 | `.tmp/dw_gh_lists_probe.py` | 4,775 | 2026-10-17 14:52:38 | `55c75c954916` | 噪声面 |
| 1113 | `.tmp/dw_gh_lists_probe2.py` | 4,371 | 2026-10-17 14:52:57 | `1f9b2ad5ea11` | 噪声面 |
| 1114 | `.tmp/dw_gh_lists_probe3.py` | 1,499 | 2026-10-17 14:53:41 | `5a1190f2522c` | 噪声面 |
| 1115 | `.tmp/dw_gh_lists_probe4.py` | 2,258 | 2026-10-17 14:54:53 | `9f35f821a0e9` | 噪声面 |
| 1116 | `.tmp/dw_gh_lists_probe_out.json` | 19,952 | 2026-10-17 14:52:43 | `0cae27484b57` | 噪声面 |
| 1117 | `.tmp/dw_gh_lists_probe_out2.json` | 63,023 | 2026-10-17 14:53:04 | `d9aa4b85ab65` | 噪声面 |
| 1118 | `.tmp/dw_gh_lists_probe_out3.json` | 67,512 | 2026-10-17 14:53:50 | `7a313e49dd4c` | 噪声面 |
| 1119 | `.tmp/dw_gh_two_lists_write.py` | 29,952 | 2026-10-17 14:57:42 | `9216594e0b15` | 噪声面 |
| 1120 | `.tmp/dw_kd4_write_2026_10_17.py` | 33,591 | 2026-10-17 16:54:24 | `c9d5937a7519` | 噪声面 |
| 1121 | `.tmp/ea_build.py` | 30,376 | 2026-10-13 21:21:46 | `8048ac40151e` | 噪声面 |
| 1122 | `.tmp/ea_files.json` | 191,599 | 2026-10-13 21:11:53 | `48b76f2549f3` | 噪声面 |
| 1123 | `.tmp/ea_fivezero_write1.py` | 46,983 | 2026-10-17 18:09:41 | `6253fe226a50` | 噪声面 |
| 1124 | `.tmp/ea_p2.py` | 1,030 | 2026-10-13 21:16:56 | `64fb6201dca9` | 噪声面 |
| 1125 | `.tmp/ea_scan1.py` | 1,005 | 2026-10-13 21:11:48 | `e21c9fca13d0` | 噪声面 |
| 1126 | `.tmp/ea_sha12.json` | 289,347 | 2026-10-13 21:12:14 | `381dd57aaca4` | 噪声面 |
| 1127 | `.tmp/err314h_write_2026_10_17.py` | 42,226 | 2026-10-17 16:12:44 | `16a77ff05fa0` | 噪声面 |
| 1128 | `.tmp/erratum_glm_wholepack_body.md` | 24,905 | 2026-10-14 12:57:34 | `0291002f749e` | 噪声面 |
| 1129 | `.tmp/esc36_write.py` | 29,232 | 2026-10-17 19:03:35 | `4dfb6a7ade55` | 噪声面 |
| 1130 | `.tmp/esc5_verdict_write_2026_10_17.py` | 27,843 | 2026-10-17 19:36:18 | `10573a36e3e9` | 噪声面 |
| 1131 | `.tmp/evauditor_one_finish_write.py` | 46,211 | 2026-10-17 00:22:44 | `c24967f8114e` | 噪声面 |
| 1132 | `.tmp/exp04_h_contrast_2026_10_10.py` | 14,333 | 2026-10-10 10:04:20 | `572f1b9c3927` | 噪声面 |
| 1133 | `.tmp/exp_harness_pre_2026_10_17.py` | 41,428 | 2026-10-17 23:26:06 | `026575ff3829` | 噪声面 |
| 1134 | `.tmp/f2_branch_fix_transform_2026_09_29.py` | 18,152 | 2026-09-29 22:53:30 | `0a970b156867` | 噪声面 |
| 1135 | `.tmp/f2_branch_selftest_2026_09_29.py` | 7,377 | 2026-09-29 22:54:26 | `68a927174a2e` | 噪声面 |
| 1136 | `.tmp/final_check.py` | 1,643 | 2026-10-15 16:54:29 | `8ee3ec5b71b5` | 噪声面 |
| 1137 | `.tmp/freeze_criterion_rewire_design_write_2026_10_17.py` | 42,900 | 2026-10-17 23:27:46 | `2d5ff7602580` | 噪声面 |
| 1138 | `.tmp/freeze_criterion_rewire_r2_append_2026_10_17.py` | 2,305 | 2026-10-17 23:55:37 | `91d5a0a69ba4` | 噪声面 |
| 1139 | `.tmp/freeze_criterion_rewire_r2_corr_2026_10_17.py` | 3,182 | 2026-10-17 23:56:20 | `d7e1c199ee85` | 噪声面 |
| 1140 | `.tmp/freeze_criterion_rewire_r2_deliverable_write_2026_10_17.py` | 49,730 | 2026-10-17 23:55:18 | `37b72b64800c` | 噪声面 |
| 1141 | `.tmp/freeze_criterion_rewire_r2_kill_freeze_2026_10_17.json` | 11,550 | 2026-10-17 23:48:24 | `2b4dafecf4d1` | 噪声面 |
| 1142 | `.tmp/freeze_criterion_rewire_r2_killfreeze_2026_10_17.py` | 8,049 | 2026-10-17 23:48:18 | `209587869f7a` | 噪声面 |
| 1143 | `.tmp/freeze_criterion_rewire_r2_llmcheck_2026_10_17.py` | 3,872 | 2026-10-17 23:51:34 | `ddd02b9013d0` | 噪声面 |
| 1144 | `.tmp/freeze_criterion_rewire_r2_llmcheck_out_2026_10_17.txt` | 1,623 | 2026-10-17 23:51:47 | `1cfa81eca602` | 噪声面 |
| 1145 | `.tmp/freeze_criterion_rewire_r2_probe_2026_10_17.py` | 22,764 | 2026-10-17 23:52:14 | `cb91e876ae7f` | 噪声面 |
| 1146 | `.tmp/freeze_criterion_rewire_r2_probe_out2_2026_10_17.txt` | 17,037 | 2026-10-17 23:52:22 | `9953747adec5` | 噪声面 |
| 1147 | `.tmp/freeze_criterion_rewire_r2_probe_out_2026_10_17.txt` | 15,494 | 2026-10-17 23:50:04 | `db80bdffe67a` | 噪声面 |
| 1148 | `.tmp/freeze_preexp_design_write_2026_10_17.py` | 42,362 | 2026-10-17 20:30:47 | `5a6fde945f71` | 噪声面 |
| 1149 | `.tmp/freeze_preexp_exec_fix_2026_10_17.py` | 1,930 | 2026-10-17 22:50:52 | `ba4a85d3e8d4` | 噪声面 |
| 1150 | `.tmp/freeze_preexp_exec_probe2_2026_10_17.py` | 8,979 | 2026-10-17 22:47:07 | `ccbab1572ae1` | 噪声面 |
| 1151 | `.tmp/freeze_preexp_exec_probe2_out_2026_10_17.md` | 5,158 | 2026-10-17 22:47:43 | `58fe8e2fb473` | 噪声面 |
| 1152 | `.tmp/freeze_preexp_exec_probe_2026_10_17.py` | 13,829 | 2026-10-17 22:46:23 | `388c731a0f61` | 噪声面 |
| 1153 | `.tmp/freeze_preexp_exec_probe_out_2026_10_17.md` | 8,593 | 2026-10-17 22:46:32 | `d146fc62162f` | 噪声面 |
| 1154 | `.tmp/freeze_preexp_exec_write_2026_10_17.py` | 36,066 | 2026-10-17 22:49:53 | `8409f2f74798` | 噪声面 |
| 1155 | `.tmp/gate_check.py` | 648 | 2026-10-09 17:24:02 | `abe7fbdb394b` | 噪声面 |
| 1156 | `.tmp/gate_check2.py` | 840 | 2026-10-09 17:24:17 | `7025ceceb766` | 噪声面 |
| 1157 | `.tmp/ge01.py` | 570 | 2026-10-16 10:56:58 | `4c0e9da2d583` | 噪声面 |
| 1158 | `.tmp/ge01_eps_grid_exec2_2026_10_16.json` | 53,903 | 2026-10-16 16:52:19 | `af1fcc0e8852` | 噪声面 |
| 1159 | `.tmp/ge01_eps_grid_exec2_2026_10_16.py` | 11,452 | 2026-10-16 16:51:17 | `9ef16d1b8525` | 噪声面 |
| 1160 | `.tmp/ge01_eps_grid_exec3_2026_10_16.py` | 3,580 | 2026-10-16 16:53:39 | `5225d7800544` | 噪声面 |
| 1161 | `.tmp/ge01_eps_grid_exec_2026_10_16.json` | 62,749 | 2026-10-16 16:48:31 | `45b233594ee9` | 噪声面 |
| 1162 | `.tmp/ge01_eps_grid_exec_2026_10_16.py` | 11,018 | 2026-10-16 16:48:21 | `ab5e001cb63b` | 噪声面 |
| 1163 | `.tmp/ge01_eps_grid_verify_2026_10_16.py` | 3,016 | 2026-10-16 16:57:00 | `4ff9d5a95dcf` | 噪声面 |
| 1164 | `.tmp/ge01_full_1494_adjudicate_2026_10_16.py` | 14,293 | 2026-10-16 22:52:31 | `8108e4c883ad` | 噪声面 |
| 1165 | `.tmp/ge01_full_1494_collect_2026_10_16.py` | 28,322 | 2026-10-16 22:39:35 | `039ebfca39b7` | 噪声面 |
| 1166 | `.tmp/ge01_full_1494_exec_r1_write_2026_10_16.py` | 43,129 | 2026-10-16 23:01:50 | `9e9e402893ef` | 噪声面 |
| 1167 | `.tmp/ge01_full_1494_freeze_2026_10_16.json` | 7,479 | 2026-10-16 22:38:20 | `8494390a274a` | 噪声面 |
| 1168 | `.tmp/ge01_full_1494_freeze_write_2026_10_16.py` | 23,781 | 2026-10-16 22:38:09 | `b89e0432ab97` | 噪声面 |
| 1169 | `.tmp/ge01_full_1494_llm_calls_2026_10_16.jsonl` | 235,298 | 2026-10-16 23:32:19 | `e922d168ab60` | 噪声面 |
| 1170 | `.tmp/ge01_full_1494_measurement_2026_10_16.json` | 547,703 | 2026-10-16 23:00:18 | `4054d1393b84` | 噪声面 |
| 1171 | `.tmp/ge01_full_1494_measurement_resume32_2026_10_16.json` | 570,852 | 2026-10-16 23:35:09 | `7ccc5f9e8b2c` | 噪声面 |
| 1172 | `.tmp/ge01_full_1494_precheck_2026_10_16.json` | 9,432 | 2026-10-16 22:17:14 | `bd6dd07ad1c3` | 噪声面 |
| 1173 | `.tmp/ge01_full_1494_precheck_2026_10_16.py` | 10,700 | 2026-10-16 22:16:48 | `cc34ab8552f9` | 噪声面 |
| 1174 | `.tmp/ge01_full_1494_probe_2026_10_16.py` | 3,199 | 2026-10-16 22:38:35 | `a38499e4d4a9` | 噪声面 |
| 1175 | `.tmp/ge01_full_1494_readout_2026_10_16.py` | 22,920 | 2026-10-16 22:59:58 | `59ed27635c6e` | 噪声面 |
| 1176 | `.tmp/ge01_full_1494_resume32_collect_2026_10_16.py` | 14,609 | 2026-10-16 23:31:45 | `9496620e32b2` | 噪声面 |
| 1177 | `.tmp/ge01_full_1494_resume32_precheck_2026_10_16.log` | 1,761 | 2026-10-16 23:30:47 | `ada7f41b8cb2` | 噪声面 |
| 1178 | `.tmp/ge01_full_1494_resume32_precheck_2026_10_16.py` | 6,122 | 2026-10-16 23:30:35 | `463532446b61` | 噪声面 |
| 1179 | `.tmp/ge01_full_1494_resume32_probe_2026_10_16.json` | 338 | 2026-10-16 23:32:01 | `579a7f8b6fe3` | 噪声面 |
| 1180 | `.tmp/ge01_full_1494_resume32_readout_2026_10_16.py` | 29,430 | 2026-10-16 23:34:47 | `de50589bd6c6` | 噪声面 |
| 1181 | `.tmp/ge01_full_1494_resume32_run_2026_10_16.log` | 1,033 | 2026-10-16 23:32:19 | `f655e7d9e3e0` | 噪声面 |
| 1182 | `.tmp/ge01_full_1494_resume32_stage_2026_10_16.json` | 7,574 | 2026-10-16 23:32:19 | `25d95a22bbb1` | 噪声面 |
| 1183 | `.tmp/ge01_full_1494_run_2026_10_16.log` | 14,810 | 2026-10-16 22:58:23 | `3e85eac1bf6a` | 噪声面 |
| 1184 | `.tmp/ge01_gate_0touch.py` | 4,538 | 2026-10-17 11:41:50 | `6efa3c7cf24f` | 噪声面 |
| 1185 | `.tmp/ge01_gate_index.py` | 3,095 | 2026-10-17 11:30:52 | `fc4ed5e7dea0` | 噪声面 |
| 1186 | `.tmp/ge01_gate_list.py` | 860 | 2026-10-17 11:41:08 | `73b666a6d791` | 噪声面 |
| 1187 | `.tmp/ge01_gate_measure.py` | 4,068 | 2026-10-17 11:36:36 | `c2cdebcb0bfc` | 噪声面 |
| 1188 | `.tmp/ge01_gate_probe.py` | 3,196 | 2026-10-17 11:32:40 | `82bf49985799` | 噪声面 |
| 1189 | `.tmp/ge01_gate_scan.py` | 1,955 | 2026-10-17 11:33:40 | `5f6212d13cb5` | 噪声面 |
| 1190 | `.tmp/ge01_gate_verify.py` | 3,042 | 2026-10-17 11:40:21 | `37d94f2bc789` | 噪声面 |
| 1191 | `.tmp/ge01_gate_verify_backup.py` | 3,042 | 2026-10-17 11:40:21 | `37d94f2bc789` | 噪声面 |
| 1192 | `.tmp/ge01_gate_write.py` | 82,875 | 2026-10-17 11:39:58 | `a661b2c7e5f0` | 噪声面 |
| 1193 | `.tmp/ge01_measure_list.json` | 2,435 | 2026-10-17 11:41:17 | `2eb41639edf4` | 噪声面 |
| 1194 | `.tmp/ge01_results_sha12.json` | 192,203 | 2026-10-17 11:31:03 | `97fb1089de90` | 噪声面 |
| 1195 | `.tmp/ge01_s3_keyscan_2026_10_16.py` | 1,730 | 2026-10-16 20:41:34 | `5f8a18033a99` | 噪声面 |
| 1196 | `.tmp/ge01_s3_vadj_recheck_2026_10_16.py` | 13,088 | 2026-10-16 20:40:00 | `91d3e1d91b58` | 噪声面 |
| 1197 | `.tmp/ge01_s3b_keyscan_2026_10_16.py` | 2,052 | 2026-10-16 21:21:34 | `b7743ec5a7ab` | 噪声面 |
| 1198 | `.tmp/ge01_s3b_v_exec_2026_10_16.py` | 6,410 | 2026-10-16 21:04:06 | `0df5d957a911` | 噪声面 |
| 1199 | `.tmp/ge01_s3b_v_exec_r1_2026_10_16.py` | 15,257 | 2026-10-16 21:17:43 | `4f525232efe4` | 噪声面 |
| 1200 | `.tmp/ge01_s3b_v_exec_r1_readings_2026_10_16.json` | 25,489 | 2026-10-16 21:18:00 | `1ec7c258c637` | 噪声面 |
| 1201 | `.tmp/ge01_s3b_v_exec_r1_supp_2026_10_16.py` | 5,199 | 2026-10-16 21:18:24 | `0646da5ccbe5` | 噪声面 |
| 1202 | `.tmp/ge01_s3b_v_exec_r1_write_2026_10_16.py` | 56,062 | 2026-10-16 21:23:10 | `359b768e7dc0` | 噪声面 |
| 1203 | `.tmp/ge02_build.py` | 24,774 | 2026-10-16 19:56:22 | `a10c57adf6b5` | 噪声面 |
| 1204 | `.tmp/ge02_recompute.py` | 1,347 | 2026-10-16 19:53:23 | `811d4a138788` | 噪声面 |
| 1205 | `.tmp/gen_supp3.py` | 15,813 | 2026-10-10 01:11:45 | `eb53c9ce140c` | 噪声面 |
| 1206 | `.tmp/gen_v35_uactive_2026_10_16.py` | 43,518 | 2026-10-16 21:17:03 | `628c99636f10` | 噪声面 |
| 1207 | `.tmp/gh_survey_r2/census.py` | 7,803 | 2026-10-17 15:36:49 | `2464dc2238de` | 噪声面 |
| 1208 | `.tmp/gh_survey_r2/finalize.py` | 3,368 | 2026-10-17 15:40:28 | `87bf54e53bb3` | 噪声面 |
| 1209 | `.tmp/gh_survey_r2/forensics.py` | 4,974 | 2026-10-17 15:37:24 | `542de3dcaa2b` | 噪声面 |
| 1210 | `.tmp/gh_survey_r2/local_match.json` | 130,915 | 2026-10-17 15:38:48 | `a98e74e8e2b3` | 噪声面 |
| 1211 | `.tmp/gh_survey_r2/localmatch.py` | 3,764 | 2026-10-17 15:38:17 | `1d584089ef90` | 噪声面 |
| 1212 | `.tmp/gh_survey_r2/localmatch2.py` | 3,281 | 2026-10-17 15:38:47 | `d09ad03f300f` | 噪声面 |
| 1213 | `.tmp/gh_survey_r2/mkregister.py` | 9,293 | 2026-10-17 15:57:32 | `a85a4535d439` | 噪声面 |
| 1214 | `.tmp/gh_survey_r2/proof.py` | 3,357 | 2026-10-17 15:38:03 | `a7d8cb3d3ba4` | 噪声面 |
| 1215 | `.tmp/gh_survey_r2/pullback.py` | 5,707 | 2026-10-17 15:53:59 | `759e5a7e69e9` | 噪声面 |
| 1216 | `.tmp/gh_survey_r2/pullback_result.json` | 108,498 | 2026-10-17 15:55:52 | `dc10a8c2cbdb` | 噪声面 |
| 1217 | `.tmp/gh_survey_r2/remote_face_census.json` | 52,383 | 2026-10-17 15:36:50 | `6e123f07aabd` | 噪声面 |
| 1218 | `.tmp/gh_survey_r2/s1_s8.py` | 3,232 | 2026-10-17 15:40:11 | `23966389fc2f` | 噪声面 |
| 1219 | `.tmp/gh_survey_r2/survey_r2_consolidated.json` | 215,148 | 2026-10-17 15:40:29 | `0a37bbd63bd5` | 噪声面 |
| 1220 | `.tmp/gh_survey_r2/walkcheck.py` | 1,392 | 2026-10-17 15:38:29 | `88bd62ed1451` | 噪声面 |
| 1221 | `.tmp/github_survey_tree.json` | 883,348 | 2026-10-17 11:56:19 | `c96081d4a790` | 噪声面 |
| 1222 | `.tmp/gitignore_sync_diag.py` | 2,515 | 2026-10-17 12:35:15 | `5f563b567570` | 噪声面 |
| 1223 | `.tmp/gitignore_sync_diag2.log` | 1,386 | 2026-10-17 12:41:07 | `8b3548a172d3` | 噪声面 |
| 1224 | `.tmp/gitignore_sync_diag2.py` | 2,785 | 2026-10-17 12:40:30 | `e36f9db320ad` | 噪声面 |
| 1225 | `.tmp/gitignore_sync_get.py` | 2,881 | 2026-10-17 12:30:47 | `2a78b01ebc05` | 噪声面 |
| 1226 | `.tmp/gitignore_sync_probe.log` | 2,462 | 2026-10-17 12:42:56 | `9fcd522eab41` | 噪声面 |
| 1227 | `.tmp/gitignore_sync_probe.py` | 3,443 | 2026-10-17 12:42:34 | `08faba9cbdaf` | 噪声面 |
| 1228 | `.tmp/gitignore_sync_read.py` | 2,987 | 2026-10-17 12:20:05 | `869aa6140743` | 噪声面 |
| 1229 | `.tmp/gitignore_sync_remote_old.txt` | 91 | 2026-10-17 12:42:55 | `7d8d71ea2af2` | 噪声面 |
| 1230 | `.tmp/gitignore_sync_remote_sha.txt` | 40 | 2026-10-17 12:42:55 | `cdf032945d98` | 噪声面 |
| 1231 | `.tmp/gts_fix.py` | 392 | 2026-10-17 20:30:34 | `fb44e889bce8` | 噪声面 |
| 1232 | `.tmp/gts_verify.py` | 986 | 2026-10-17 20:30:55 | `a7242e906204` | 噪声面 |
| 1233 | `.tmp/gts_write.py` | 38,639 | 2026-10-17 20:30:42 | `878a4597dda2` | 噪声面 |
| 1234 | `.tmp/h_src.py` | 727 | 2026-10-15 12:56:44 | `a4b8970b8b1f` | 噪声面 |
| 1235 | `.tmp/harness.py` | 687 | 2026-10-16 10:57:43 | `56e02c4878f4` | 噪声面 |
| 1236 | `.tmp/harness_mask_diffstat_2026_10_17.py` | 5,616 | 2026-10-17 23:34:07 | `6fe0a6d30555` | 噪声面 |
| 1237 | `.tmp/harness_mask_diffstat_out_2026_10_17.txt` | 2,337 | 2026-10-17 23:34:19 | `7db31c10646f` | 噪声面 |
| 1238 | `.tmp/harness_mask_freeze_write_2026_10_17.py` | 7,873 | 2026-10-17 23:28:09 | `079a280da225` | 噪声面 |
| 1239 | `.tmp/harness_mask_kill_freeze_2026_10_17.json` | 6,673 | 2026-10-17 23:28:19 | `5ecfe565fa1d` | 噪声面 |
| 1240 | `.tmp/harness_mask_validation_2026_10_17.py` | 15,806 | 2026-10-17 23:32:45 | `03f7a0b5e150` | 噪声面 |
| 1241 | `.tmp/harness_mask_validation_out_2026_10_17.txt` | 7,241 | 2026-10-17 23:32:56 | `ba3413b0d5a3` | 噪声面 |
| 1242 | `.tmp/k_v3df_0_1_four_readings_2026_10_09.py` | 50,232 | 2026-10-09 11:24:00 | `2e990644cc8d` | 噪声面 |
| 1243 | `.tmp/kd14_absorption_probe.py` | 1,358 | 2026-10-16 22:17:54 | `915c968f2d04` | 噪声面 |
| 1244 | `.tmp/kd14_carrier_probe.py` | 1,206 | 2026-10-16 22:17:00 | `758033c2a76b` | 噪声面 |
| 1245 | `.tmp/kd14_m4_corrected.py` | 932 | 2026-10-16 22:18:11 | `50c1c7d85616` | 噪声面 |
| 1246 | `.tmp/kd14_p2_kill_lines_freeze_2026_10_17.md` | 12,032 | 2026-10-17 23:48:55 | `aca85ea4727c` | 噪声面 |
| 1247 | `.tmp/kd14_p2_probe.py` | 15,574 | 2026-10-17 23:55:41 | `6f7ac21bdc3d` | 噪声面 |
| 1248 | `.tmp/kd14_p2_probe_out_2026_10_17.txt` | 6,858 | 2026-10-17 23:55:51 | `b74675107848` | 噪声面 |
| 1249 | `.tmp/kd14_p2_write1.py` | 15,489 | 2026-10-17 23:48:44 | `a493231d9229` | 噪声面 |
| 1250 | `.tmp/kd14_p2_write2.py` | 28,296 | 2026-10-17 23:59:10 | `ff9ab107b5f5` | 噪声面 |
| 1251 | `.tmp/kd1_body.md` | 27,149 | 2026-10-17 19:23:06 | `eb652774ffd9` | 噪声面 |
| 1252 | `.tmp/kd1_preexp_contrast_probe.py` | 7,910 | 2026-10-17 19:21:13 | `27f4aea260c6` | 噪声面 |
| 1253 | `.tmp/kd_flip_verify.out.txt` | 1,667 | 2026-10-17 21:38:59 | `6ce95e7fbc25` | 噪声面 |
| 1254 | `.tmp/kdb2_uaxis_content.md` | 25,669 | 2026-10-17 16:26:49 | `45e62039cee3` | 噪声面 |
| 1255 | `.tmp/kdb2_uaxis_write.py` | 3,245 | 2026-10-17 16:26:58 | `ef1c7def7bbb` | 噪声面 |
| 1256 | `.tmp/kdk45_final_check_2026_10_17.py` | 882 | 2026-10-17 20:17:51 | `cdfe7086f0df` | 噪声面 |
| 1257 | `.tmp/kdk45_r1_recompute_2026_10_17.json` | 9,111 | 2026-10-17 20:12:50 | `64c911198107` | 噪声面 |
| 1258 | `.tmp/kdk45_r1_recompute_2026_10_17.py` | 17,711 | 2026-10-17 20:12:42 | `77a392bb0d57` | 噪声面 |
| 1259 | `.tmp/kdk45_r3_m2t5_calls_2026_10_17.jsonl` | 2,232 | 2026-10-17 20:13:42 | `91db46a87830` | 噪声面 |
| 1260 | `.tmp/kdk45_r3_m2t5_measure_2026_10_17.py` | 12,351 | 2026-10-17 20:13:16 | `a34c6884a2ed` | 噪声面 |
| 1261 | `.tmp/kdk45_r3_m2t5_measurement_2026_10_17.json` | 7,470 | 2026-10-17 20:14:07 | `61f904cba24b` | 噪声面 |
| 1262 | `.tmp/kdk45_r3_verify_2026_10_17.py` | 4,039 | 2026-10-17 20:13:58 | `c07a79494a2d` | 噪声面 |
| 1263 | `.tmp/kdk45_write_doc_2026_10_17.py` | 31,791 | 2026-10-17 20:16:35 | `ed9ef1a61a56` | 噪声面 |
| 1264 | `.tmp/kdm413_rm_analysis_2026_10_17.json` | 100,764 | 2026-10-17 21:28:17 | `cf971276fb6b` | 噪声面 |
| 1265 | `.tmp/kdm413_rm_analyze_2026_10_17.py` | 30,209 | 2026-10-17 21:28:10 | `67861aa767e9` | 噪声面 |
| 1266 | `.tmp/kdm413_rm_caliber_decl_2026_10_17.json` | 4,334 | 2026-10-17 20:42:08 | `055eb047a2d0` | 噪声面 |
| 1267 | `.tmp/kdm413_rm_chain_2026_10_17.ps1` | 1,762 | 2026-10-17 20:50:06 | `13366e678e63` | 噪声面 |
| 1268 | `.tmp/kdm413_rm_collect_2026_10_17.out.txt` | 1,272 | 2026-10-17 20:47:03 | `cfdf83cc890e` | 噪声面 |
| 1269 | `.tmp/kdm413_rm_collect_2026_10_17.py` | 17,518 | 2026-10-17 20:42:40 | `5de96682284a` | 噪声面 |
| 1270 | `.tmp/kdm413_rm_collect_run2.out.txt` | 1,982 | 2026-10-17 21:26:13 | `96c5cea2b7eb` | 噪声面 |
| 1271 | `.tmp/kdm413_rm_freeze_2026_10_17.json` | 5,944 | 2026-10-17 20:42:08 | `a884b2cc02bd` | 噪声面 |
| 1272 | `.tmp/kdm413_rm_freeze_2026_10_17.py` | 14,868 | 2026-10-17 20:41:59 | `af97eed6a9f1` | 噪声面 |
| 1273 | `.tmp/kdm413_rm_llm_calls_2026_10_17.jsonl` | 613,571 | 2026-10-17 21:26:13 | `7f4cf2cd5f42` | 噪声面 |
| 1274 | `.tmp/kdm413_rm_post_2026_10_17.out.txt` | 142 | 2026-10-17 21:26:16 | `757c78a09738` | 噪声面 |
| 1275 | `.tmp/kdm413_rm_preflight_2026_10_17.json` | 5,212 | 2026-10-17 20:41:13 | `998c92f003b1` | 噪声面 |
| 1276 | `.tmp/kdm413_rm_preflight_2026_10_17.py` | 9,459 | 2026-10-17 20:41:03 | `4a2e00cb511b` | 噪声面 |
| 1277 | `.tmp/kdm413_rm_readings_2026_10_17.json` | 958,870 | 2026-10-17 21:26:13 | `e97160e999ed` | 噪声面 |
| 1278 | `.tmp/kdm413_rm_verify_2026_10_17.out.txt` | 1,853 | 2026-10-17 21:31:30 | `ebf0d9a78cbc` | 噪声面 |
| 1279 | `.tmp/kdm413_rm_verify_2026_10_17.py` | 3,361 | 2026-10-17 20:46:31 | `1e2822415675` | 噪声面 |
| 1280 | `.tmp/kdm413_rm_write_doc_2026_10_17.py` | 37,961 | 2026-10-17 21:31:07 | `7043404017ae` | 噪声面 |
| 1281 | `.tmp/klm413_reverdict_payload.md` | 61,667 | 2026-10-17 21:44:26 | `63625672139a` | 噪声面 |
| 1282 | `.tmp/klm41_2_bootstrap_ci_2026_10_16.json` | 12,373 | 2026-10-16 11:45:53 | `be99abcba9bf` | 噪声面 |
| 1283 | `.tmp/klm41_2_caliber_decl_2026_10_16.json` | 4,757 | 2026-10-16 11:40:55 | `6f0721d20c06` | 噪声面 |
| 1284 | `.tmp/klm41_2_caliber_decl_2026_10_16.py` | 10,466 | 2026-10-16 11:40:46 | `d9754474ad9a` | 噪声面 |
| 1285 | `.tmp/klm41_2_compute_ci_2026_10_16.py` | 14,398 | 2026-10-16 11:44:37 | `fb38b90df08f` | 噪声面 |
| 1286 | `.tmp/klm41_2_freeze_2026_10_16.json` | 3,211 | 2026-10-16 11:40:55 | `2a4453d9610b` | 噪声面 |
| 1287 | `.tmp/klm41_2_stratified_ci_2026_10_16.json` | 18,820 | 2026-10-16 11:48:56 | `67ae4f540e47` | 噪声面 |
| 1288 | `.tmp/klm41_2_stratified_ci_2026_10_16.py` | 8,819 | 2026-10-16 11:47:22 | `f29526bccea3` | 噪声面 |
| 1289 | `.tmp/klm41_2_verify_2026_10_16.json` | 2,906 | 2026-10-16 11:46:54 | `5ded5068566b` | 噪声面 |
| 1290 | `.tmp/klm41_2_verify_2026_10_16.py` | 10,976 | 2026-10-16 11:45:08 | `af0f38f33222` | 噪声面 |
| 1291 | `.tmp/klm41_2_write_doc_2026_10_16.py` | 48,391 | 2026-10-16 11:55:01 | `902dcf78f2b8` | 噪声面 |
| 1292 | `.tmp/klm41_3_ts_caliber_decl_2026_10_16.json` | 3,255 | 2026-10-16 19:30:34 | `96456529a485` | 噪声面 |
| 1293 | `.tmp/klm41_3_ts_collect_2026_10_16.py` | 23,196 | 2026-10-16 19:31:16 | `a28c4ba40940` | 噪声面 |
| 1294 | `.tmp/klm41_3_ts_freeze_2026_10_16.json` | 2,235 | 2026-10-16 19:30:34 | `25c021d29b1b` | 噪声面 |
| 1295 | `.tmp/klm41_3_ts_llm_calls_2026_10_16.jsonl` | 123,255 | 2026-10-16 19:38:58 | `595699b7ec44` | 噪声面 |
| 1296 | `.tmp/klm41_3_ts_measurement_2026_10_16.json` | 252,951 | 2026-10-16 19:38:58 | `211a49ca9941` | 噪声面 |
| 1297 | `.tmp/klm41_3_ts_preflight_2026_10_16.json` | 6,349 | 2026-10-16 19:30:07 | `d1fe0a6889be` | 噪声面 |
| 1298 | `.tmp/klm41_3_ts_preflight_2026_10_16.py` | 6,228 | 2026-10-16 19:29:59 | `c787c6d4e361` | 噪声面 |
| 1299 | `.tmp/klm41_3_ts_tables_2026_10_16.md` | 11,297 | 2026-10-16 19:40:18 | `54213bffc216` | 噪声面 |
| 1300 | `.tmp/klm41_3_ts_verify_2026_10_16.json` | 5,848 | 2026-10-16 19:39:52 | `8cf7bb595870` | 噪声面 |
| 1301 | `.tmp/klm41_3_verdict_write_2026_10_17.py` | 34,041 | 2026-10-17 18:25:02 | `d4c4d8b41569` | 噪声面 |
| 1302 | `.tmp/kro_extract.py` | 802 | 2026-10-09 17:22:02 | `b5731abae41f` | 噪声面 |
| 1303 | `.tmp/m08_enum_v2_2026_10_16.json` | 12,255 | 2026-10-16 16:09:19 | `c45cfc3ddc8d` | 噪声面 |
| 1304 | `.tmp/m08_llm_calls_2026_10_16.jsonl` | 1,360 | 2026-10-16 16:06:24 | `00799137a44f` | 噪声面 |
| 1305 | `.tmp/m08_r1_amend2_2026_10_16.json` | 1,296 | 2026-10-16 16:27:40 | `21ad2e7acd0b` | 噪声面 |
| 1306 | `.tmp/m08_r1_amend3_2026_10_16.json` | 3,034 | 2026-10-16 16:28:16 | `d77931c6d7a5` | 噪声面 |
| 1307 | `.tmp/m08_r1_amend_2026_10_16.json` | 1,204 | 2026-10-16 16:27:06 | `3c982068b276` | 噪声面 |
| 1308 | `.tmp/m08_r1_enum_2026_10_16.json` | 13,253 | 2026-10-16 16:19:00 | `361f67e37092` | 噪声面 |
| 1309 | `.tmp/m08_r1_enum_2026_10_16.py` | 16,318 | 2026-10-16 16:18:16 | `884b7161e053` | 噪声面 |
| 1310 | `.tmp/m08_r1_freeze_2026_10_16.json` | 7,655 | 2026-10-16 16:17:28 | `1a40d8046fdc` | 噪声面 |
| 1311 | `.tmp/m08_r1_freeze_2026_10_16.py` | 9,207 | 2026-10-16 16:17:22 | `8c6b5e0d3ebb` | 噪声面 |
| 1312 | `.tmp/m08_r1_llm_arm_2026_10_16.json` | 11,335 | 2026-10-16 16:21:18 | `19d93d77b46e` | 噪声面 |
| 1313 | `.tmp/m08_r1_llm_arm_2026_10_16.py` | 9,852 | 2026-10-16 16:20:53 | `987820693d06` | 噪声面 |
| 1314 | `.tmp/m08_r1_llm_calls_2026_10_16.jsonl` | 8,271 | 2026-10-16 16:21:18 | `0e8c9664b06d` | 噪声面 |
| 1315 | `.tmp/m08_r1_llm_calls_partial_pass1_2026_10_16.jsonl` | 8,230 | 2026-10-16 16:20:34 | `d30121ed7ebf` | 噪声面 |
| 1316 | `.tmp/m08_r1_llm_probe2_2026_10_16.json` | 1,805 | 2026-10-16 16:21:51 | `d2a8510b1322` | 噪声面 |
| 1317 | `.tmp/m08_r1_llm_probe2_2026_10_16.py` | 2,359 | 2026-10-16 16:21:41 | `190668eae9da` | 噪声面 |
| 1318 | `.tmp/m08_r1_probe_2026_10_16.json` | 3,752 | 2026-10-16 16:19:34 | `c2ba80ba548b` | 噪声面 |
| 1319 | `.tmp/m08_r1_probe_2026_10_16.py` | 4,739 | 2026-10-16 16:19:28 | `63f0234a7c89` | 噪声面 |
| 1320 | `.tmp/m08_r1_recompute_2026_10_16.json` | 2,072 | 2026-10-16 16:22:25 | `59ddca239f67` | 噪声面 |
| 1321 | `.tmp/m08_r1_recompute_2026_10_16.py` | 6,998 | 2026-10-16 16:22:14 | `305ee668612c` | 噪声面 |
| 1322 | `.tmp/m08_r1_srcsha_2026_10_16.json` | 8,851 | 2026-10-16 16:22:52 | `2074096a45e2` | 噪声面 |
| 1323 | `.tmp/m08_r1_srcsha_2026_10_16.py` | 3,697 | 2026-10-16 16:22:46 | `96ac0e7c23f6` | 噪声面 |
| 1324 | `.tmp/m08_r1_write_2026_10_16.py` | 58,218 | 2026-10-16 16:26:50 | `0a5d9e9f18d9` | 噪声面 |
| 1325 | `.tmp/m2_docwriter_write.py` | 23,214 | 2026-10-14 10:23:50 | `9842ca168062` | 噪声面 |
| 1326 | `.tmp/m2_write.py` | 24,159 | 2026-10-14 03:20:18 | `133387a21ec6` | 噪声面 |
| 1327 | `.tmp/m2verdict_downstream.py` | 2,240 | 2026-10-14 11:50:05 | `93c831a7fc0f` | 噪声面 |
| 1328 | `.tmp/m2verdict_meta.py` | 1,223 | 2026-10-14 11:49:30 | `c89599655807` | 噪声面 |
| 1329 | `.tmp/m2verdict_probe.py` | 4,493 | 2026-10-14 11:46:21 | `3a401ef46a00` | 噪声面 |
| 1330 | `.tmp/m2verdict_ruling.py` | 1,125 | 2026-10-14 11:51:41 | `841949136e81` | 噪声面 |
| 1331 | `.tmp/m41_dual_readout.py` | 6,471 | 2026-10-15 09:30:33 | `45f3d856efd8` | 噪声面 |
| 1332 | `.tmp/m41_endpoint_probe.py` | 1,520 | 2026-10-15 09:29:37 | `f9811a6eceba` | 噪声面 |
| 1333 | `.tmp/m41_fix_diag.json` | 1,034 | 2026-10-15 10:20:20 | `2e34378d0d2c` | 噪声面 |
| 1334 | `.tmp/m41_keyprobe.py` | 892 | 2026-10-15 00:12:19 | `10e08b837e05` | 噪声面 |
| 1335 | `.tmp/m41_keysurvey.py` | 1,296 | 2026-10-15 00:12:32 | `795daa633133` | 噪声面 |
| 1336 | `.tmp/m41_llm_calls.jsonl` | 642 | 2026-10-15 09:26:55 | `a1651f3d9303` | 噪声面 |
| 1337 | `.tmp/m41_mech_arms.json` | 1,252 | 2026-10-15 09:34:07 | `be1a8fce8660` | 噪声面 |
| 1338 | `.tmp/m41_mech_arms.py` | 3,731 | 2026-10-15 09:34:02 | `a92812ceae61` | 噪声面 |
| 1339 | `.tmp/m41_r15_collect_readout.py` | 13,324 | 2026-10-15 10:21:47 | `d4e882337b80` | 噪声面 |
| 1340 | `.tmp/m41_r15_llm_calls.jsonl` | 3,467 | 2026-10-15 10:22:52 | `7d0dbb58d53a` | 噪声面 |
| 1341 | `.tmp/m41_r15_readout.json` | 14,261 | 2026-10-15 10:22:52 | `33a4720bcafd` | 噪声面 |
| 1342 | `.tmp/m41_r15_verify.py` | 4,235 | 2026-10-15 10:23:40 | `f72545f959b4` | 噪声面 |
| 1343 | `.tmp/m41_rerun_llm_calls.jsonl` | 24,253 | 2026-10-15 10:07:00 | `19fa12f4e053` | 噪声面 |
| 1344 | `.tmp/m41_selfcheck.json` | 318 | 2026-10-15 09:39:44 | `d18a46a884f2` | 噪声面 |
| 1345 | `.tmp/m41_selfcheck.py` | 1,291 | 2026-10-15 09:13:31 | `5f066493fdbc` | 噪声面 |
| 1346 | `.tmp/m41_src_shas.py` | 1,138 | 2026-10-15 09:30:48 | `47a192be190a` | 噪声面 |
| 1347 | `.tmp/m41_src_shas.txt` | 420 | 2026-10-15 09:39:53 | `b2c58664cd51` | 噪声面 |
| 1348 | `.tmp/material_expansion_kill_freeze_2026_10_16.json` | 15,187 | 2026-10-16 15:33:54 | `03a628456f0b` | 噪声面 |
| 1349 | `.tmp/me_llm_calls_2026_10_16.jsonl` | 21,339 | 2026-10-16 15:38:54 | `fbdedcb0ef48` | 噪声面 |
| 1350 | `.tmp/me_measurement_2026_10_16.json` | 80,474 | 2026-10-16 15:38:54 | `ffdd4d8908de` | 噪声面 |
| 1351 | `.tmp/me_t4_resolve_2026_10_16.py` | 9,507 | 2026-10-16 15:46:44 | `71b0e9c8da44` | 噪声面 |
| 1352 | `.tmp/merge_gov_write.py` | 26,827 | 2026-10-17 23:05:51 | `7ad32ca275a1` | 噪声面 |
| 1353 | `.tmp/mq04_budget_calc_2026_10_15.json` | 5,436 | 2026-10-15 15:47:49 | `e8a5b2533ac2` | 噪声面 |
| 1354 | `.tmp/mq04_budget_calc_2026_10_15.py` | 6,803 | 2026-10-15 15:47:43 | `e5e4fcfd5e29` | 噪声面 |
| 1355 | `.tmp/mq04_nt_llm_calls_2026_10_15.jsonl` | 24,320 | 2026-10-15 15:43:24 | `734af9135441` | 噪声面 |
| 1356 | `.tmp/mq04_nt_measure_2026_10_15.py` | 14,503 | 2026-10-15 15:39:58 | `5e55c0ff27f8` | 噪声面 |
| 1357 | `.tmp/mq04_nt_measurement_2026_10_15.json` | 6,047 | 2026-10-15 15:43:24 | `956d35f25c70` | 噪声面 |
| 1358 | `.tmp/mq04_write_doc_2026_10_15.py` | 26,377 | 2026-10-15 15:49:02 | `7fb013086741` | 噪声面 |
| 1359 | `.tmp/ndv_stage.md` | 41,028 | 2026-10-17 22:16:30 | `0abaee4aeefb` | 噪声面 |
| 1360 | `.tmp/ndv_verify.out.txt` | 204 | 2026-10-17 22:16:42 | `8639d96ebab1` | 噪声面 |
| 1361 | `.tmp/ndv_write.py` | 1,303 | 2026-10-17 22:16:35 | `bb41a46309ba` | 噪声面 |
| 1362 | `.tmp/o81_ndistinct_probe.out.txt` | 3,794 | 2026-10-17 21:52:05 | `60b911e30775` | 噪声面 |
| 1363 | `.tmp/o81_ndistinct_probe.py` | 6,984 | 2026-10-17 21:51:57 | `d5e9dcf545ae` | 噪声面 |
| 1364 | `.tmp/o81_ndproof_write.py` | 26,006 | 2026-10-17 21:53:45 | `be3dba7376c5` | 噪声面 |
| 1365 | `.tmp/pa_block.py` | 345 | 2026-10-09 17:22:28 | `19ac8c59439b` | 噪声面 |
| 1366 | `.tmp/pk33q_body.md` | 26,976 | 2026-10-15 17:15:37 | `20ad5b45ba2c` | 噪声面 |
| 1367 | `.tmp/pk_afrules_body.md` | 39,994 | 2026-10-17 20:54:28 | `525ae85c1bbc` | 噪声面 |
| 1368 | `.tmp/pk_afrules_verify.py` | 1,727 | 2026-10-17 20:55:07 | `614990249944` | 噪声面 |
| 1369 | `.tmp/pk_afrules_write.py` | 2,196 | 2026-10-17 20:54:44 | `01d8dcba5d49` | 噪声面 |
| 1370 | `.tmp/pk_body1.md` | 26,832 | 2026-10-15 09:09:17 | `b32ca40ec103` | 噪声面 |
| 1371 | `.tmp/pk_body2.md` | 32,568 | 2026-10-15 09:10:46 | `75a818b2654f` | 噪声面 |
| 1372 | `.tmp/pk_carddir_chk.py` | 439 | 2026-10-17 16:48:18 | `26be180ab6a8` | 噪声面 |
| 1373 | `.tmp/pk_carddir_payload.md` | 26,682 | 2026-10-17 16:47:53 | `a694e5d55ce1` | 噪声面 |
| 1374 | `.tmp/pk_carddir_verify.py` | 1,172 | 2026-10-17 16:48:45 | `1668ce2c75ea` | 噪声面 |
| 1375 | `.tmp/pk_carddir_write.py` | 1,805 | 2026-10-17 16:48:03 | `ed586f3bc7bd` | 噪声面 |
| 1376 | `.tmp/pk_citcaliber_probe.py` | 3,564 | 2026-10-17 12:21:28 | `78df5735d745` | 噪声面 |
| 1377 | `.tmp/pk_citcaliber_probe_out.txt` | 5,440 | 2026-10-17 12:40:18 | `c9404d3d79fc` | 噪声面 |
| 1378 | `.tmp/pk_citcaliber_tally.py` | 3,122 | 2026-10-17 12:42:36 | `bc01dfd7745b` | 噪声面 |
| 1379 | `.tmp/pk_citcaliber_tally_out.txt` | 1,207 | 2026-10-17 12:43:09 | `9d9bb88a336f` | 噪声面 |
| 1380 | `.tmp/pk_lockv2_degeneracy_2026_10_15.json` | 2,583 | 2026-10-15 16:16:10 | `1106bb7d5c56` | 噪声面 |
| 1381 | `.tmp/pk_lockv2_degeneracy_2026_10_15.py` | 2,425 | 2026-10-15 16:16:03 | `e8067070c849` | 噪声面 |
| 1382 | `.tmp/pk_lockv2_verify_2026_10_15.json` | 4,691 | 2026-10-15 16:15:53 | `34cf77faf825` | 噪声面 |
| 1383 | `.tmp/pk_lockv2_verify_2026_10_15.py` | 3,784 | 2026-10-15 16:15:47 | `67795949087d` | 噪声面 |
| 1384 | `.tmp/pk_lockv2_write_2026_10_15.py` | 33,749 | 2026-10-15 16:17:43 | `440affa3e102` | 噪声面 |
| 1385 | `.tmp/pk_measure_01.py` | 1,510 | 2026-10-14 02:10:55 | `76af3ed43f2c` | 噪声面 |
| 1386 | `.tmp/pk_probe2_2026_10_16.py` | 1,140 | 2026-10-16 10:55:45 | `632e6dca295d` | 噪声面 |
| 1387 | `.tmp/pk_probe_2026_10_16.py` | 878 | 2026-10-16 10:54:43 | `809cf2066d48` | 噪声面 |
| 1388 | `.tmp/pk_refonly_tally.py` | 3,527 | 2026-10-17 14:05:55 | `5f7f31a20530` | 噪声面 |
| 1389 | `.tmp/pk_refonly_tally_out.json` | 182,956 | 2026-10-17 14:06:09 | `c69b9035e71b` | 噪声面 |
| 1390 | `.tmp/pk_refonly_write.py` | 43,408 | 2026-10-17 14:14:58 | `576e8d16e061` | 噪声面 |
| 1391 | `.tmp/pk_supp500_calc_2026_10_16.py` | 3,079 | 2026-10-16 10:57:34 | `5325e2e6bc00` | 噪声面 |
| 1392 | `.tmp/pk_t5lock_body_2026_10_15.md` | 46,621 | 2026-10-15 16:53:29 | `404d4fbeef40` | 噪声面 |
| 1393 | `.tmp/pk_t5lock_verify_2026_10_15.json` | 4,931 | 2026-10-15 16:49:54 | `0b9c36f612da` | 噪声面 |
| 1394 | `.tmp/pk_t5lock_verify_2026_10_15.py` | 5,559 | 2026-10-15 16:49:50 | `3f21b53443b4` | 噪声面 |
| 1395 | `.tmp/pk_t5lock_write_2026_10_15.py` | 3,938 | 2026-10-15 16:53:42 | `e80c26269446` | 噪声面 |
| 1396 | `.tmp/pk_write_budget210_2026_10_16.py` | 20,931 | 2026-10-16 11:04:19 | `0c65c2e859f9` | 噪声面 |
| 1397 | `.tmp/pk_write_citcaliber_draft.py` | 50,504 | 2026-10-17 13:21:30 | `436ecab60dcd` | 噪声面 |
| 1398 | `.tmp/pk_write_design_review_2026_10_16.py` | 47,618 | 2026-10-16 11:02:43 | `439fa0ae048d` | 噪声面 |
| 1399 | `.tmp/pool_search.py` | 2,127 | 2026-10-10 13:49:20 | `3245af3f3bbb` | 噪声面 |
| 1400 | `.tmp/prep.py` | 4,091 | 2026-10-10 13:51:46 | `e401c8e50f93` | 噪声面 |
| 1401 | `.tmp/probe2_out.txt` | 12,057 | 2026-10-13 23:34:58 | `f56d5b0b837c` | 噪声面 |
| 1402 | `.tmp/probe3_out.txt` | 41,096 | 2026-10-13 23:35:56 | `d2cef7709033` | 噪声面 |
| 1403 | `.tmp/psr_probe0.py` | 494 | 2026-10-17 22:42:27 | `24d04a775520` | 噪声面 |
| 1404 | `.tmp/psr_probe_beta0.py` | 880 | 2026-10-17 22:46:52 | `8a12501b53aa` | 噪声面 |
| 1405 | `.tmp/psr_probe_beta0_out.txt` | 1,948 | 2026-10-17 22:46:59 | `d27ac29d6f9a` | 噪声面 |
| 1406 | `.tmp/psr_probe_facebeta.py` | 11,087 | 2026-10-17 22:50:13 | `37ce6750bbbe` | 噪声面 |
| 1407 | `.tmp/psr_probe_facebeta_out.txt` | 7,179 | 2026-10-17 22:50:25 | `ef2106a43a79` | 噪声面 |
| 1408 | `.tmp/psr_probe_faceC.py` | 8,460 | 2026-10-17 22:46:01 | `62861c3c215d` | 噪声面 |
| 1409 | `.tmp/psr_probe_faceC_out.txt` | 10,012 | 2026-10-17 22:46:11 | `0396142b93cf` | 噪声面 |
| 1410 | `.tmp/psr_probe_faceC_seqB.py` | 2,306 | 2026-10-17 22:51:28 | `6565297a3dfe` | 噪声面 |
| 1411 | `.tmp/psr_probe_faceC_seqB_out.txt` | 2,104 | 2026-10-17 22:51:36 | `0de6ceade34b` | 噪声面 |
| 1412 | `.tmp/psr_stage.md` | 42,707 | 2026-10-17 22:56:01 | `cfcf430f306c` | 噪声面 |
| 1413 | `.tmp/psr_verify.out.txt` | 1,984 | 2026-10-17 22:56:42 | `44187fa25685` | 噪声面 |
| 1414 | `.tmp/psr_verify.py` | 2,290 | 2026-10-17 22:56:34 | `1b34212bbda4` | 噪声面 |
| 1415 | `.tmp/psr_write.py` | 738 | 2026-10-17 22:56:07 | `ffb5045608ce` | 噪声面 |
| 1416 | `.tmp/r3m2_disp_write.py` | 18,437 | 2026-10-14 11:37:24 | `988c2fee3ea2` | 噪声面 |
| 1417 | `.tmp/r461_layers.json` | 102,003 | 2026-10-14 02:35:00 | `fee35e10c208` | 噪声面 |
| 1418 | `.tmp/r461_write_01.py` | 19,104 | 2026-10-14 02:48:27 | `9030a50780da` | 噪声面 |
| 1419 | `.tmp/recheck2.py` | 2,282 | 2026-09-30 21:43:11 | `85c4cfa3eb46` | 噪声面 |
| 1420 | `.tmp/refonly161_build_register.py` | 20,024 | 2026-10-17 15:47:34 | `4755c9c8bb3c` | 噪声面 |
| 1421 | `.tmp/refonly161_parse.py` | 2,352 | 2026-10-17 14:51:52 | `8f9e491f7416` | 噪声面 |
| 1422 | `.tmp/refonly161_pool.json` | 38,044 | 2026-10-17 14:51:57 | `153406812a84` | 噪声面 |
| 1423 | `.tmp/refonly161_probe_log.txt` | 2,954 | 2026-10-17 15:46:41 | `f5d37f4432f6` | 噪声面 |
| 1424 | `.tmp/refonly161_probe_out.json` | 1,342,186 | 2026-10-17 15:46:41 | `a87f13960926` | 噪声面 |
| 1425 | `.tmp/refonly161_r2_build_register.py` | 38,697 | 2026-10-17 16:41:59 | `0a5da0f0e9a7` | 噪声面 |
| 1426 | `.tmp/refonly161_r2_build_register_part2.py` | 15,675 | 2026-10-17 16:40:27 | `d88a46c82e31` | 噪声面 |
| 1427 | `.tmp/refonly161_r2_out.json` | 2,029,558 | 2026-10-17 16:37:50 | `c47c6f4afddd` | 噪声面 |
| 1428 | `.tmp/refonly161_r2_probe.py` | 26,360 | 2026-10-17 16:34:09 | `c3171dc8cdf9` | 噪声面 |
| 1429 | `.tmp/refonly161_r2_rows.json` | 76,969 | 2026-10-17 16:38:09 | `02d63e5a9d99` | 噪声面 |
| 1430 | `.tmp/refonly161_r2_tally.py` | 3,717 | 2026-10-17 16:32:25 | `0e9d8bb2d42d` | 噪声面 |
| 1431 | `.tmp/refonly161_r2_tally2.py` | 4,796 | 2026-10-17 16:32:49 | `aa5e93bc0ac5` | 噪声面 |
| 1432 | `.tmp/refonly161_r2_verify_bytes.py` | 786 | 2026-10-17 16:42:44 | `f920377ad974` | 噪声面 |
| 1433 | `.tmp/refonly161_verify_probe.py` | 15,090 | 2026-10-17 15:44:00 | `b4bafa0860d1` | 噪声面 |
| 1434 | `.tmp/ritt_remeasure_collect_2026_10_17.py` | 33,524 | 2026-10-17 19:54:24 | `38b2cecb2d16` | 噪声面 |
| 1435 | `.tmp/ritt_remeasure_collect_log_2026_10_17.txt` | 10,627 | 2026-10-17 20:08:38 | `eac10421dcad` | 噪声面 |
| 1436 | `.tmp/ritt_remeasure_freeze_2026_10_17.json` | 6,636 | 2026-10-17 19:53:40 | `a41f38631fab` | 噪声面 |
| 1437 | `.tmp/ritt_remeasure_llm_calls_2026_10_17.jsonl` | 106,119 | 2026-10-17 20:08:38 | `3e68a203fa06` | 噪声面 |
| 1438 | `.tmp/ritt_remeasure_measurement_2026_10_17.json` | 325,531 | 2026-10-17 20:08:38 | `29bb4c4a8bca` | 噪声面 |
| 1439 | `.tmp/root45_s11s12_collect_2026_10_17.py` | 11,994 | 2026-10-17 20:13:02 | `09f11b997cf2` | 噪声面 |
| 1440 | `.tmp/root45_s11s12_freeze_2026_10_17.json` | 2,941 | 2026-10-17 20:12:47 | `a830d4e73af2` | 噪声面 |
| 1441 | `.tmp/root45_s11s12_freeze_write_2026_10_17.py` | 4,627 | 2026-10-17 20:12:38 | `ed818a87408f` | 噪声面 |
| 1442 | `.tmp/root45_s11s12_llm_calls_2026_10_17.jsonl` | 2,484 | 2026-10-17 20:13:22 | `d34cc2373f0f` | 噪声面 |
| 1443 | `.tmp/root45_s11s12_measurement_2026_10_17.json` | 8,661 | 2026-10-17 20:13:22 | `2ec5ad7ce1e9` | 噪声面 |
| 1444 | `.tmp/root45_write_2026_10_17.py` | 21,205 | 2026-10-17 20:15:36 | `3eb66353d385` | 噪声面 |
| 1445 | `.tmp/rpp_perseed_recalc_probe2_2026_10_17.py` | 7,794 | 2026-10-17 22:15:14 | `f89e484df372` | 噪声面 |
| 1446 | `.tmp/rpp_perseed_recalc_probe2_out_2026_10_17.txt` | 3,224 | 2026-10-17 22:15:22 | `c8cdcedc427b` | 噪声面 |
| 1447 | `.tmp/rpp_perseed_recalc_probe_2026_10_17.py` | 8,857 | 2026-10-17 22:12:11 | `3ad523e85535` | 噪声面 |
| 1448 | `.tmp/rpp_perseed_recalc_probe_out_2026_10_17.txt` | 5,706 | 2026-10-17 22:12:26 | `e0aa42ed95ab` | 噪声面 |
| 1449 | `.tmp/run_steps.py` | 2,756 | 2026-10-10 13:45:15 | `019f8405d4cf` | 噪声面 |
| 1450 | `.tmp/s3_recompute_pass4.py` | 4,439 | 2026-10-01 08:54:56 | `6f210893fcce` | 噪声面 |
| 1451 | `.tmp/s4_regen_runner.py` | 13,040 | 2026-10-10 13:43:59 | `70467364bdb1` | 噪声面 |
| 1452 | `.tmp/scan_classify_five_terminal_2026_10_10.py` | 7,603 | 2026-10-10 12:23:20 | `0b9b59083534` | 噪声面 |
| 1453 | `.tmp/scan_domain_five_terminal_2026_10_10.py` | 2,243 | 2026-10-10 12:21:53 | `732489dc3dbd` | 噪声面 |
| 1454 | `.tmp/scan_supplement_five_terminal_2026_10_10.py` | 6,010 | 2026-10-10 12:22:25 | `7c0a6d022104` | 噪声面 |
| 1455 | `.tmp/scope_scan.py` | 3,380 | 2026-10-10 13:48:55 | `07349acfe90f` | 噪声面 |
| 1456 | `.tmp/singlevar.py` | 1,515 | 2026-10-10 13:50:16 | `f0bba43af3e5` | 噪声面 |
| 1457 | `.tmp/t2_path_b_kill_freeze_2026_10_16.json` | 14,896 | 2026-10-16 16:13:35 | `3f3272100f62` | 噪声面 |
| 1458 | `.tmp/t2b_census_2026_10_16.py` | 3,041 | 2026-10-16 16:21:25 | `71f99afb9199` | 噪声面 |
| 1459 | `.tmp/t2b_derive_2026_10_16.py` | 7,964 | 2026-10-16 16:20:52 | `324165eb0c7d` | 噪声面 |
| 1460 | `.tmp/t2b_fetch_facts_2026_10_16.py` | 5,774 | 2026-10-16 16:10:08 | `0941558d024e` | 噪声面 |
| 1461 | `.tmp/t2b_freeze_2026_10_16.py` | 13,908 | 2026-10-16 16:06:21 | `575b796a2e6f` | 噪声面 |
| 1462 | `.tmp/t2b_freeze_v2_2026_10_16.py` | 17,044 | 2026-10-16 16:13:29 | `02a261b12f7b` | 噪声面 |
| 1463 | `.tmp/t2b_harness_pre_change_snapshot_2026_10_16.py` | 36,217 | 2026-10-16 16:16:22 | `d5c8d676bb5b` | 噪声面 |
| 1464 | `.tmp/t2b_impl_audit_2026_10_16.py` | 4,856 | 2026-10-16 16:15:06 | `e02a343246bd` | 噪声面 |
| 1465 | `.tmp/t2b_inspect_facts_2026_10_16.py` | 1,732 | 2026-10-16 16:00:37 | `de3c879e39f1` | 噪声面 |
| 1466 | `.tmp/t2b_llm_calls_2026_10_16.jsonl` | 5,317 | 2026-10-16 16:19:18 | `a54a3af46ba2` | 噪声面 |
| 1467 | `.tmp/t2b_measure_2026_10_16.py` | 15,547 | 2026-10-16 16:18:26 | `bd377372927c` | 噪声面 |
| 1468 | `.tmp/t2b_measurement_2026_10_16.json` | 25,796 | 2026-10-16 16:19:18 | `fe5db6defb09` | 噪声面 |
| 1469 | `.tmp/t2b_patch_harness_2026_10_16.py` | 7,065 | 2026-10-16 16:16:02 | `bac4775c5c44` | 噪声面 |
| 1470 | `.tmp/t2b_strategyqa_train_snapshot_2026_10_16.json` | 4,281,955 | 2026-10-16 16:07:40 | `728e28b7d6bd` | 噪声面 |
| 1471 | `.tmp/t3_baseline_procedure_probe.py` | 2,292 | 2026-10-15 17:19:37 | `b4c2a5e68dfa` | 噪声面 |
| 1472 | `.tmp/t3_baseline_procedure_probe_2026_10_15.json` | 1,332 | 2026-10-15 17:20:00 | `7ac600d45dcc` | 噪声面 |
| 1473 | `.tmp/t3_freeze_2026_10_15.json` | 7,436 | 2026-10-15 17:17:18 | `313f091718cc` | 噪声面 |
| 1474 | `.tmp/t3_nt_llm_calls_2026_10_15.jsonl` | 5,250 | 2026-10-15 17:21:54 | `0cb1decec878` | 噪声面 |
| 1475 | `.tmp/t3_nt_measure_2026_10_15.py` | 17,111 | 2026-10-15 17:21:07 | `35860b379b7a` | 噪声面 |
| 1476 | `.tmp/t3_nt_measurement_2026_10_15.json` | 19,576 | 2026-10-15 17:21:54 | `92f0dc763caf` | 噪声面 |
| 1477 | `.tmp/t3_nt_verify.py` | 6,657 | 2026-10-15 17:22:40 | `a1c38dc17d65` | 噪声面 |
| 1478 | `.tmp/t3_nt_verify_2026_10_15.json` | 3,885 | 2026-10-15 17:22:46 | `700de33ee255` | 噪声面 |
| 1479 | `.tmp/t3_postchange_equiv.py` | 5,975 | 2026-10-15 17:19:03 | `1e579de6033c` | 噪声面 |
| 1480 | `.tmp/t3_postchange_equiv_2026_10_15.json` | 3,904 | 2026-10-15 17:19:10 | `e8a97dc64a08` | 噪声面 |
| 1481 | `.tmp/t3_postchange_manifest_check_2026_10_15.json` | 2,135 | 2026-10-15 17:23:04 | `dbfae4d96b46` | 噪声面 |
| 1482 | `.tmp/t3_postcheck.py` | 3,129 | 2026-10-15 17:22:55 | `20c96933b00d` | 噪声面 |
| 1483 | `.tmp/t3_prechange_manifest_2026_10_15.json` | 76,683 | 2026-10-15 17:17:35 | `f1508ebe14e7` | 噪声面 |
| 1484 | `.tmp/t3_prove_minimal_increment_2026_10_15.json` | 433 | 2026-10-15 17:18:18 | `3f858f6958cd` | 噪声面 |
| 1485 | `.tmp/t3_prove_minimal_increment_2026_10_15.py` | 7,303 | 2026-10-15 17:18:11 | `1f39cf068862` | 噪声面 |
| 1486 | `.tmp/t3_repro_probe_ftfb_freeze_2026_10_16.json` | 2,936 | 2026-10-16 22:59:34 | `44761c404b86` | 噪声面 |
| 1487 | `.tmp/t3_repro_probe_llm_calls_2026_10_16.jsonl` | 7,441 | 2026-10-16 23:04:59 | `54ad4d2cd8bf` | 噪声面 |
| 1488 | `.tmp/t3_repro_probe_measure_2026_10_16.json` | 9,137 | 2026-10-16 23:04:59 | `31779f66c051` | 噪声面 |
| 1489 | `.tmp/t5_baseline_manifest_2026_10_15.json` | 99,724 | 2026-10-15 16:16:38 | `2d5ad82c0a63` | 噪声面 |
| 1490 | `.tmp/t5_kill_line_freeze_2026_10_15.json` | 3,183 | 2026-10-15 16:17:11 | `1910a62c1e9f` | 噪声面 |
| 1491 | `.tmp/t5_nt_llm_calls_2026_10_15.jsonl` | 7,258 | 2026-10-15 16:20:15 | `8e488d14bff6` | 噪声面 |
| 1492 | `.tmp/t5_nt_measure_2026_10_15.py` | 15,602 | 2026-10-15 16:18:23 | `c96c985d8e23` | 噪声面 |
| 1493 | `.tmp/t5_nt_measurement_2026_10_15.json` | 3,845 | 2026-10-15 16:20:15 | `674e95ecff03` | 噪声面 |
| 1494 | `.tmp/t5_prove_minimal_increment_2026_10_15.py` | 6,308 | 2026-10-15 16:21:07 | `65cec9c9788e` | 噪声面 |
| 1495 | `.tmp/t5_write_docs_2026_10_15.py` | 47,918 | 2026-10-15 16:25:36 | `f104bf4706e6` | 噪声面 |
| 1496 | `.tmp/tables.py` | 1,818 | 2026-10-10 13:52:29 | `02cc157b6d69` | 噪声面 |
| 1497 | `.tmp/three_seed_caliber_decl_2026_10_16.json` | 4,859 | 2026-10-16 10:59:50 | `5df309d557b0` | 噪声面 |
| 1498 | `.tmp/three_seed_caliber_decl_write_2026_10_16.py` | 7,242 | 2026-10-16 10:59:37 | `0776cbaf4410` | 噪声面 |
| 1499 | `.tmp/three_seed_collect_2026_10_16.py` | 28,520 | 2026-10-16 11:11:41 | `672d12ad9801` | 噪声面 |
| 1500 | `.tmp/three_seed_collect_log_2026_10_16.txt` | 16,230 | 2026-10-16 11:10:03 | `55c783261d18` | 噪声面 |
| 1501 | `.tmp/three_seed_freeze_2026_10_16.json` | 10,536 | 2026-10-16 10:58:59 | `46260e3b8426` | 噪声面 |
| 1502 | `.tmp/three_seed_freeze_write_2026_10_16.py` | 13,149 | 2026-10-16 10:58:50 | `db503b3de434` | 噪声面 |
| 1503 | `.tmp/three_seed_llm_calls_2026_10_16.jsonl` | 104,288 | 2026-10-16 11:10:03 | `5a8cbcf85aa7` | 噪声面 |
| 1504 | `.tmp/three_seed_measurement_2026_10_16.json` | 226,256 | 2026-10-16 11:12:10 | `ff5ed4b0e329` | 噪声面 |
| 1505 | `.tmp/three_seed_preflight_2026_10_16.py` | 5,661 | 2026-10-16 10:57:57 | `98e0e4ae7a73` | 噪声面 |
| 1506 | `.tmp/three_seed_verify_2026_10_16.json` | 3,205 | 2026-10-16 11:24:04 | `61e3d0bfa05d` | 噪声面 |
| 1507 | `.tmp/three_seed_verify_2026_10_16.py` | 13,402 | 2026-10-16 11:12:04 | `5c382ace9573` | 噪声面 |
| 1508 | `.tmp/three_seed_write_doc_2026_10_16.py` | 50,308 | 2026-10-16 11:23:38 | `f546bdd3630c` | 噪声面 |
| 1509 | `.tmp/u04_1_chain_verify.py` | 4,849 | 2026-10-09 17:22:54 | `13e573534692` | 噪声面 |
| 1510 | `.tmp/u04_1_dual_verify.py` | 3,228 | 2026-10-09 17:23:16 | `f5702456560f` | 噪声面 |
| 1511 | `.tmp/u04_1_make_data.py` | 19,773 | 2026-10-09 17:24:49 | `309ac58e049d` | 噪声面 |
| 1512 | `.tmp/u15_recheck_content.md` | 39,219 | 2026-10-17 16:20:31 | `71c6b834dd9d` | 噪声面 |
| 1513 | `.tmp/u15_recheck_write.py` | 4,947 | 2026-10-17 16:20:49 | `ef6f38b132fa` | 噪声面 |
| 1514 | `.tmp/u1889_final.py` | 3,327 | 2026-10-17 19:29:11 | `a3415c482849` | 噪声面 |
| 1515 | `.tmp/u1889_final2.py` | 3,744 | 2026-10-17 19:29:30 | `1a158989c112` | 噪声面 |
| 1516 | `.tmp/u1889_final_out.txt` | 1,683 | 2026-10-17 19:29:55 | `fc1f2b476a1a` | 噪声面 |
| 1517 | `.tmp/u1889_finalize.py` | 3,306 | 2026-10-17 19:28:55 | `81a3e8c0e8f3` | 噪声面 |
| 1518 | `.tmp/u1889_selfcheck.py` | 2,977 | 2026-10-17 19:28:34 | `f1880cef7fbb` | 噪声面 |
| 1519 | `.tmp/u1889_selfcheck_out.txt` | 1,619 | 2026-10-17 19:28:38 | `b141543b767c` | 噪声面 |
| 1520 | `.tmp/u1889_verify.py` | 477 | 2026-10-17 19:26:06 | `485b2498388b` | 噪声面 |
| 1521 | `.tmp/u1889_write.py` | 23,022 | 2026-10-17 19:27:55 | `41a3a95e0dc0` | 噪声面 |
| 1522 | `.tmp/u720_errata.py` | 4,360 | 2026-10-17 20:45:26 | `5ee4b22c9bdf` | 噪声面 |
| 1523 | `.tmp/u720_probe1.out.txt` | 2,397 | 2026-10-17 20:40:42 | `3aa862e204af` | 噪声面 |
| 1524 | `.tmp/u720_probe1.py` | 2,411 | 2026-10-17 20:40:41 | `663fab4c48d6` | 噪声面 |
| 1525 | `.tmp/u720_probe2.py` | 501 | 2026-10-17 20:41:37 | `ab9948ef7584` | 噪声面 |
| 1526 | `.tmp/u720_verify.py` | 2,038 | 2026-10-17 20:44:15 | `e05fd04ab2da` | 噪声面 |
| 1527 | `.tmp/u720_write.py` | 40,915 | 2026-10-17 20:45:03 | `9d2fd29d275d` | 噪声面 |
| 1528 | `.tmp/u_cluster1_write_2026_10_17.py` | 40,926 | 2026-10-17 18:36:58 | `4980f4d7e7af` | 噪声面 |
| 1529 | `.tmp/u_lock_recalc_probe_closedform.py` | 3,220 | 2026-10-17 19:06:20 | `d86d6a2a571d` | 噪声面 |
| 1530 | `.tmp/u_lock_recalc_probe_hashscan.py` | 1,284 | 2026-10-17 19:04:05 | `f44d4f11cbd8` | 噪声面 |
| 1531 | `.tmp/u_lock_recalc_verify.py` | 2,009 | 2026-10-17 19:11:44 | `6d9a0828458c` | 噪声面 |
| 1532 | `.tmp/u_lock_recalc_write.py` | 24,715 | 2026-10-17 19:10:39 | `8af7de4beb95` | 噪声面 |
| 1533 | `.tmp/verify_final.py` | 805 | 2026-10-14 22:15:42 | `904eb215f139` | 噪声面 |
| 1534 | `.tmp/verify_out.txt` | 4,276 | 2026-10-15 11:22:52 | `d90af351ea39` | 噪声面 |
| 1535 | `.tmp/verify_t3trap_bprime_2026_10_15.py` | 6,928 | 2026-10-15 17:19:40 | `a9e880243eab` | 噪声面 |
| 1536 | `.tmp/verify_v3.py` | 4,114 | 2026-10-15 13:00:22 | `26641521a307` | 噪声面 |
| 1537 | `.tmp/vk_161_reading_verdict_write.py` | 40,161 | 2026-10-17 16:11:32 | `eef597d306ee` | 噪声面 |
| 1538 | `.tmp/vk_denominator_2026_10_16.py` | 856 | 2026-10-16 16:50:40 | `d935b89bfa31` | 噪声面 |
| 1539 | `.tmp/vk_ext5_write_2026_10_17.py` | 61,083 | 2026-10-17 18:38:09 | `419557cf5ce0` | 噪声面 |
| 1540 | `.tmp/vk_fail_h0_readback_2026_10_17.txt` | 1,218 | 2026-10-17 18:27:09 | `c8df4d40dd29` | 噪声面 |
| 1541 | `.tmp/vk_fail_h0_verdict_write_2026_10_17.py` | 42,450 | 2026-10-17 18:26:48 | `5fec803e4c81` | 噪声面 |
| 1542 | `.tmp/vk_interval_arith_2026_10_16.py` | 1,273 | 2026-10-16 16:48:02 | `901d8df83bb3` | 噪声面 |
| 1543 | `.tmp/vk_kds3b1_write_2026_10_17.py` | 49,892 | 2026-10-17 19:22:36 | `c83a8b490d42` | 噪声面 |
| 1544 | `.tmp/vk_r2_reading_verdict_write.py` | 43,279 | 2026-10-17 17:04:35 | `b7f19f3c7bb0` | 噪声面 |
| 1545 | `.tmp/vk_v3df_0_1_agree.py` | 6,140 | 2026-10-09 12:02:48 | `84c090952894` | 噪声面 |
| 1546 | `.tmp/vk_v3df_0_1_coverage_gap.py` | 1,971 | 2026-10-09 12:01:06 | `df25000e7180` | 噪声面 |
| 1547 | `.tmp/vk_v3df_0_1_materiality.py` | 2,875 | 2026-10-09 12:01:29 | `b666b7a38082` | 噪声面 |
| 1548 | `.tmp/vk_v3df_0_1_verify_2026_10_09.py` | 14,347 | 2026-10-09 12:00:28 | `0e7cb9348a16` | 噪声面 |
| 1549 | `.tmp/vk_verify_2026_10_16.py` | 3,780 | 2026-10-16 13:57:57 | `6ad7edf03032` | 噪声面 |
| 1550 | `.tmp/vk_verify_interval_ceiling_2026_10_16.py` | 3,692 | 2026-10-16 16:53:20 | `18b0f12b2c66` | 噪声面 |
| 1551 | `.tmp/vk_write_2026_10_16.py` | 62,030 | 2026-10-16 13:57:37 | `2334a967a1d4` | 噪声面 |
| 1552 | `.tmp/vk_write_interval_ceiling_post_lock_2026_10_16.py` | 47,768 | 2026-10-16 16:52:55 | `3076d727e02c` | 噪声面 |
| 1553 | `.tmp/whitelist_backup_2026_10_17/_26b_verdict_prep_hashcheck_2026_10_01.py` | 3,842 | 2026-10-01 08:54:44 | `6927c9462f41` | 噪声面 |
| 1554 | `.tmp/whitelist_backup_2026_10_17/_26b_verdict_prep_literalcheck_2026_10_01.py` | 4,378 | 2026-10-01 08:55:50 | `50fe799b0a2e` | 噪声面 |
| 1555 | `.tmp/whitelist_backup_2026_10_17/_26b_verdict_prep_validate_2026_10_01.py` | 4,640 | 2026-10-01 08:57:57 | `494cca45b873` | 噪声面 |
| 1556 | `.tmp/whitelist_backup_2026_10_17/_659_compact.txt` | 155,628 | 2026-10-14 02:36:23 | `795862c09a40` | 噪声面 |
| 1557 | `.tmp/whitelist_backup_2026_10_17/_659_overlap_digest.txt` | 239,157 | 2026-10-14 02:35:09 | `4f20b8085fb9` | 噪声面 |
| 1558 | `.tmp/whitelist_backup_2026_10_17/_659_report_gen.py` | 27,457 | 2026-10-14 02:40:26 | `cd4b8ed56b2c` | 噪声面 |
| 1559 | `.tmp/whitelist_backup_2026_10_17/_abc_diff_2026_10_10.py` | 6,620 | 2026-10-10 12:23:35 | `6d6733f0e5c2` | 噪声面 |
| 1560 | `.tmp/whitelist_backup_2026_10_17/_abc_final_2026_10_10.py` | 7,329 | 2026-10-10 12:26:39 | `15b4de4fdff6` | 噪声面 |
| 1561 | `.tmp/whitelist_backup_2026_10_17/_abc_h1h2_2026_10_10.py` | 7,889 | 2026-10-10 12:25:31 | `16f19bad301f` | 噪声面 |
| 1562 | `.tmp/whitelist_backup_2026_10_17/_abc_readings_reprocheck_2026_10_10.py` | 9,491 | 2026-10-10 12:23:04 | `0ec2a2bf3bab` | 噪声面 |
| 1563 | `.tmp/whitelist_backup_2026_10_17/_abc_readings_reprocheck_out_2026_10_10.json` | 78,436 | 2026-10-10 12:23:11 | `2f9aa16b63ca` | 噪声面 |
| 1564 | `.tmp/whitelist_backup_2026_10_17/_abc_rfd_2026_10_10.py` | 5,938 | 2026-10-10 12:26:11 | `39268ca6adff` | 噪声面 |
| 1565 | `.tmp/whitelist_backup_2026_10_17/_aggregate_10cells.py` | 3,009 | 2026-09-26 17:42:04 | `3bdc6250d0f2` | 噪声面 |
| 1566 | `.tmp/whitelist_backup_2026_10_17/_aggregate_10cells_v2.py` | 5,131 | 2026-09-26 17:45:07 | `af1b7f09f74d` | 噪声面 |
| 1567 | `.tmp/whitelist_backup_2026_10_17/_aggregate_10cells_v3.py` | 2,969 | 2026-09-26 17:45:22 | `04b127d80bf0` | 噪声面 |
| 1568 | `.tmp/whitelist_backup_2026_10_17/_aggregate_10cells_v4.py` | 2,454 | 2026-09-26 17:45:58 | `f99a3765c3c3` | 噪声面 |
| 1569 | `.tmp/whitelist_backup_2026_10_17/_append_intake_supplement_6_tail.py` | 9,335 | 2026-10-10 15:09:46 | `c3339682d68c` | 噪声面 |
| 1570 | `.tmp/whitelist_backup_2026_10_17/_audit3b.txt` | 50,554 | 2026-09-28 15:20:27 | `e64565a2b180` | 噪声面 |
| 1571 | `.tmp/whitelist_backup_2026_10_17/_audit_part3_out.txt` | 5,195 | 2026-09-28 15:18:03 | `85a9d9861d38` | 噪声面 |
| 1572 | `.tmp/whitelist_backup_2026_10_17/_audit_part4.txt` | 14,826 | 2026-09-28 15:23:04 | `def27c1c3511` | 噪声面 |
| 1573 | `.tmp/whitelist_backup_2026_10_17/_b12_q1_refs_2026_09_29.py` | 4,890 | 2026-09-29 16:24:08 | `86b2d9b7b7bd` | 噪声面 |
| 1574 | `.tmp/whitelist_backup_2026_10_17/_b12_q1_timeslice_2026_09_29.py` | 798 | 2026-09-29 16:30:07 | `bacf6379b9bf` | 噪声面 |
| 1575 | `.tmp/whitelist_backup_2026_10_17/_b12_q4_adjacent_2026_09_29.py` | 5,709 | 2026-09-29 16:27:42 | `61cbc9965896` | 噪声面 |
| 1576 | `.tmp/whitelist_backup_2026_10_17/_b12_q4_exact_2026_09_29.py` | 7,140 | 2026-09-29 16:26:54 | `79eba6136d83` | 噪声面 |
| 1577 | `.tmp/whitelist_backup_2026_10_17/_b12_q4_formcand_2026_09_29.py` | 6,510 | 2026-09-29 16:22:21 | `f58f388996d4` | 噪声面 |
| 1578 | `.tmp/whitelist_backup_2026_10_17/_b12_tables_2026_09_29.py` | 1,907 | 2026-09-29 16:30:30 | `10db58be72cf` | 噪声面 |
| 1579 | `.tmp/whitelist_backup_2026_10_17/_build_5anchor_json_draft.py` | 34,455 | 2026-10-14 16:29:28 | `391e7a1be0e5` | 噪声面 |
| 1580 | `.tmp/whitelist_backup_2026_10_17/_build_5anchor_json_v1.py` | 11,627 | 2026-10-14 17:52:06 | `56c459492ecf` | 噪声面 |
| 1581 | `.tmp/whitelist_backup_2026_10_17/_build_intake_supplement_6.py` | 13,094 | 2026-10-10 15:09:02 | `6336456853ae` | 噪声面 |
| 1582 | `.tmp/whitelist_backup_2026_10_17/_build_receipt_supplement_6.py` | 11,430 | 2026-10-12 22:24:56 | `20c44c665b4f` | 噪声面 |
| 1583 | `.tmp/whitelist_backup_2026_10_17/_c5_b3_rewalk_postcheck_2026_10_01.py` | 2,249 | 2026-10-01 09:44:01 | `aca7dad6ddfa` | 噪声面 |
| 1584 | `.tmp/whitelist_backup_2026_10_17/_c5_b3_rewalk_precheck_2026_10_01.py` | 2,035 | 2026-10-01 09:43:19 | `4aad531a2ddb` | 噪声面 |
| 1585 | `.tmp/whitelist_backup_2026_10_17/_c5_b3_rewalk_utf8check_2026_10_01.py` | 925 | 2026-10-01 09:44:11 | `5488ff2db11f` | 噪声面 |
| 1586 | `.tmp/whitelist_backup_2026_10_17/_c5_b_group_fix_readings_2026_10_09.py` | 12,289 | 2026-10-09 13:38:56 | `b6855b38acc2` | 噪声面 |
| 1587 | `.tmp/whitelist_backup_2026_10_17/_c5_feasibility_probe.py` | 1,036 | 2026-09-29 13:22:43 | `d730612b0c9a` | 噪声面 |
| 1588 | `.tmp/whitelist_backup_2026_10_17/_canonical_census.py` | 4,382 | 2026-10-14 14:03:57 | `36b7af564c56` | 噪声面 |
| 1589 | `.tmp/whitelist_backup_2026_10_17/_canonical_lines.json` | 15,033 | 2026-10-14 14:06:49 | `9b0997fc7e52` | 噪声面 |
| 1590 | `.tmp/whitelist_backup_2026_10_17/_canonical_lines.py` | 3,354 | 2026-10-14 14:06:35 | `08aa8638a0b2` | 噪声面 |
| 1591 | `.tmp/whitelist_backup_2026_10_17/_check_escape.py` | 332 | 2026-10-14 00:12:36 | `5f026b0baf39` | 噪声面 |
| 1592 | `.tmp/whitelist_backup_2026_10_17/_check_kimi_sides.py` | 1,459 | 2026-09-26 17:44:36 | `4f3291959a6d` | 噪声面 |
| 1593 | `.tmp/whitelist_backup_2026_10_17/_ci_gap_fill_alt_bc_aper_prime_2026_10_09.py` | 20,997 | 2026-10-09 17:42:45 | `b0cf9baba64b` | 噪声面 |
| 1594 | `.tmp/whitelist_backup_2026_10_17/_cleanup_r2_cleanlist.json` | 810 | 2026-10-17 11:42:16 | `ce71dda28157` | 噪声面 |
| 1595 | `.tmp/whitelist_backup_2026_10_17/_cleanup_r2_exec.py` | 7,884 | 2026-10-17 11:43:04 | `a2029c340ac5` | 噪声面 |
| 1596 | `.tmp/whitelist_backup_2026_10_17/_cleanup_r2_exec_journal.json` | 10,327 | 2026-10-17 11:43:44 | `cd636cb64813` | 噪声面 |
| 1597 | `.tmp/whitelist_backup_2026_10_17/_cleanup_r2_postcheck.json` | 6,652 | 2026-10-17 11:44:18 | `720b25650bcd` | 噪声面 |
| 1598 | `.tmp/whitelist_backup_2026_10_17/_cleanup_r2_postcheck.py` | 4,585 | 2026-10-17 11:44:09 | `cfd60493f18d` | 噪声面 |
| 1599 | `.tmp/whitelist_backup_2026_10_17/_cleanup_r2_scan.py` | 11,507 | 2026-10-17 11:27:45 | `60d6d3d37076` | 噪声面 |
| 1600 | `.tmp/whitelist_backup_2026_10_17/_cleanup_r2_scan2.py` | 12,112 | 2026-10-17 11:32:24 | `7019c7b8d728` | 噪声面 |
| 1601 | `.tmp/whitelist_backup_2026_10_17/_cleanup_r2_scan3.py` | 12,389 | 2026-10-17 11:38:52 | `46b7b8230e86` | 噪声面 |
| 1602 | `.tmp/whitelist_backup_2026_10_17/_cleanup_r2_scan_out.json` | 758,995 | 2026-10-17 11:40:50 | `3b107c078490` | 噪声面 |
| 1603 | `.tmp/whitelist_backup_2026_10_17/_compute_metrics.py` | 7,752 | 2026-09-26 17:43:45 | `ae2b0142b09e` | 噪声面 |
| 1604 | `.tmp/whitelist_backup_2026_10_17/_compute_metrics_v2.py` | 8,017 | 2026-09-26 17:46:18 | `0620ef317e8a` | 噪声面 |
| 1605 | `.tmp/whitelist_backup_2026_10_17/_corrupt_ge01_readiness_firstwrite_2026_10_13.md` | 31,745 | 2026-10-13 23:39:50 | `3a240806c2d3` | 噪声面 |
| 1606 | `.tmp/whitelist_backup_2026_10_17/_cpatomic_dump_pyc_2026_09_28.py` | 468 | 2026-09-28 15:53:57 | `d7c9ac28b096` | 噪声面 |
| 1607 | `.tmp/whitelist_backup_2026_10_17/_cpatomic_keyscan_2026_09_28.py` | 3,074 | 2026-09-28 15:52:04 | `393a8d3fa68f` | 噪声面 |
| 1608 | `.tmp/whitelist_backup_2026_10_17/_cpatomic_make_fix_2026_09_28.py` | 7,796 | 2026-09-28 15:45:51 | `76c822b640a0` | 噪声面 |
| 1609 | `.tmp/whitelist_backup_2026_10_17/_cpatomic_pycache_post_2026_09_28.py` | 5,164 | 2026-09-28 15:51:22 | `171b2a31c0e1` | 噪声面 |
| 1610 | `.tmp/whitelist_backup_2026_10_17/_cpatomic_pycache_pre_2026_09_28.py` | 3,912 | 2026-09-28 15:42:15 | `b86619676bf4` | 噪声面 |
| 1611 | `.tmp/whitelist_backup_2026_10_17/_cpatomic_register_2026_09_28.json` | 29,361 | 2026-09-28 15:52:46 | `b68d7ff817bb` | 噪声面 |
| 1612 | `.tmp/whitelist_backup_2026_10_17/_cpatomic_register_2026_09_28.py` | 6,322 | 2026-09-28 15:52:32 | `98fe9fa24e80` | 噪声面 |
| 1613 | `.tmp/whitelist_backup_2026_10_17/_cpatomic_verify_2026_09_28.py` | 11,036 | 2026-09-28 15:49:14 | `85139011457c` | 噪声面 |
| 1614 | `.tmp/whitelist_backup_2026_10_17/_crosscheck_messages_35_48.py` | 1,608 | 2026-10-10 15:10:47 | `dcfe48359488` | 噪声面 |
| 1615 | `.tmp/whitelist_backup_2026_10_17/_d05_b_coincidence_checks_2026_10_10.py` | 22,078 | 2026-10-10 12:08:37 | `c1fc428d450c` | 噪声面 |
| 1616 | `.tmp/whitelist_backup_2026_10_17/_d05_caliber_2026_10_10.py` | 8,011 | 2026-10-10 12:42:22 | `65cb84529cb2` | 噪声面 |
| 1617 | `.tmp/whitelist_backup_2026_10_17/_d05_instrument_audit.py` | 5,948 | 2026-10-10 11:58:15 | `edfa99486954` | 噪声面 |
| 1618 | `.tmp/whitelist_backup_2026_10_17/_d05_s4only_2026_10_10.py` | 3,438 | 2026-10-10 12:42:55 | `802069e2c06e` | 噪声面 |
| 1619 | `.tmp/whitelist_backup_2026_10_17/_d05_three_checks_recheck_2026_10_10.py` | 11,134 | 2026-10-10 12:41:16 | `fc1201cb71e7` | 噪声面 |
| 1620 | `.tmp/whitelist_backup_2026_10_17/_d05_three_checks_recheck_out_2026_10_10.json` | 3,622 | 2026-10-10 12:41:33 | `4eb425260682` | 噪声面 |
| 1621 | `.tmp/whitelist_backup_2026_10_17/_dfam_corr_src_2026_10_12.md` | 33,471 | 2026-10-12 17:50:24 | `12da29eb102c` | 噪声面 |
| 1622 | `.tmp/whitelist_backup_2026_10_17/_diff21_anchor_drift.py` | 960 | 2026-09-28 20:17:33 | `de2a99cf1999` | 噪声面 |
| 1623 | `.tmp/whitelist_backup_2026_10_17/_docwriter_night_headers.txt` | 52,370 | 2026-10-14 01:43:30 | `729875e7999e` | 噪声面 |
| 1624 | `.tmp/whitelist_backup_2026_10_17/_docwriter_night_measure.json` | 22,679 | 2026-10-14 01:41:55 | `f5bacfac3f1c` | 噪声面 |
| 1625 | `.tmp/whitelist_backup_2026_10_17/_docwriter_q4_l117_append_block.md` | 4,857 | 2026-10-01 09:18:25 | `7c7d633047e4` | 噪声面 |
| 1626 | `.tmp/whitelist_backup_2026_10_17/_docwriter_recheck.py` | 2,374 | 2026-10-14 01:44:00 | `54b522e4e2fe` | 噪声面 |
| 1627 | `.tmp/whitelist_backup_2026_10_17/_docwriter_write_handover.py` | 49,400 | 2026-10-14 01:48:38 | `a553d705a482` | 噪声面 |
| 1628 | `.tmp/whitelist_backup_2026_10_17/_dump_dkb3_records2_2026_10_10.py` | 1,366 | 2026-10-10 10:12:37 | `e71d1e81da64` | 噪声面 |
| 1629 | `.tmp/whitelist_backup_2026_10_17/_dump_dkb3_records_2026_10_10.py` | 1,781 | 2026-10-10 10:11:13 | `144b204237bf` | 噪声面 |
| 1630 | `.tmp/whitelist_backup_2026_10_17/_dup_name_diff_content_scan2_2026_10_08.py` | 7,547 | 2026-10-08 17:21:02 | `b3fe206ef866` | 噪声面 |
| 1631 | `.tmp/whitelist_backup_2026_10_17/_dup_name_diff_content_scan_2026_10_08.py` | 4,519 | 2026-10-08 17:10:41 | `675cc3136e70` | 噪声面 |
| 1632 | `.tmp/whitelist_backup_2026_10_17/_dw_abs_scan.json` | 56,306 | 2026-10-14 15:40:27 | `5c584826ed16` | 噪声面 |
| 1633 | `.tmp/whitelist_backup_2026_10_17/_e47_docwriter_count.py` | 1,124 | 2026-09-28 15:44:30 | `33cc563b9471` | 噪声面 |
| 1634 | `.tmp/whitelist_backup_2026_10_17/_e48_apply.py` | 2,329 | 2026-09-28 16:17:15 | `d4e6f0934e5f` | 噪声面 |
| 1635 | `.tmp/whitelist_backup_2026_10_17/_e48_c1.md` | 5,039 | 2026-09-28 16:13:39 | `c2a814a90330` | 噪声面 |
| 1636 | `.tmp/whitelist_backup_2026_10_17/_e48_c2.md` | 5,966 | 2026-09-28 16:14:09 | `4d3cae4cbcc0` | 噪声面 |
| 1637 | `.tmp/whitelist_backup_2026_10_17/_e48_c3.md` | 6,563 | 2026-09-28 16:14:52 | `769c71475404` | 噪声面 |
| 1638 | `.tmp/whitelist_backup_2026_10_17/_e48_c4.md` | 21,710 | 2026-09-28 16:16:37 | `8143d01ca0e1` | 噪声面 |
| 1639 | `.tmp/whitelist_backup_2026_10_17/_e48_c5.md` | 1,686 | 2026-09-28 16:16:51 | `2f7ab971f691` | 噪声面 |
| 1640 | `.tmp/whitelist_backup_2026_10_17/_e48_docwriter_chain.py` | 2,550 | 2026-09-28 16:15:13 | `da5e16e02b7d` | 噪声面 |
| 1641 | `.tmp/whitelist_backup_2026_10_17/_e48_docwriter_enum.py` | 1,248 | 2026-09-28 16:13:06 | `80bad142f13d` | 噪声面 |
| 1642 | `.tmp/whitelist_backup_2026_10_17/_e48_docwriter_hash.py` | 2,578 | 2026-09-28 16:08:02 | `4656b3b734c5` | 噪声面 |
| 1643 | `.tmp/whitelist_backup_2026_10_17/_e48_docwriter_hash2.py` | 1,229 | 2026-09-28 16:11:52 | `9a3c5b05e29e` | 噪声面 |
| 1644 | `.tmp/whitelist_backup_2026_10_17/_e48_probe_register.py` | 873 | 2026-09-28 16:10:10 | `d92f74712dab` | 噪声面 |
| 1645 | `.tmp/whitelist_backup_2026_10_17/_e49_c1.md` | 13,607 | 2026-09-29 13:13:15 | `1e6e30d4ce4d` | 噪声面 |
| 1646 | `.tmp/whitelist_backup_2026_10_17/_e49_c2.md` | 17,872 | 2026-09-29 13:14:18 | `11beaed14ea7` | 噪声面 |
| 1647 | `.tmp/whitelist_backup_2026_10_17/_e6_alt_permp_closure_analysis_2026_10_10.py` | 2,736 | 2026-10-10 15:02:17 | `affabef74de4` | 噪声面 |
| 1648 | `.tmp/whitelist_backup_2026_10_17/_e6_alt_permp_closure_runner_2026_10_10.py` | 9,985 | 2026-10-10 14:59:42 | `9bb254aa58a9` | 噪声面 |
| 1649 | `.tmp/whitelist_backup_2026_10_17/_e6_ndjt_recompute_2026_10_10.py` | 5,064 | 2026-10-10 14:58:57 | `59c2d618305f` | 噪声面 |
| 1650 | `.tmp/whitelist_backup_2026_10_17/_e_q_doc.md` | 28,259 | 2026-10-14 14:10:48 | `71f5a0769dab` | 噪声面 |
| 1651 | `.tmp/whitelist_backup_2026_10_17/_e_q_exec.json` | 6,161 | 2026-10-14 14:07:09 | `d4bd8c92201f` | 噪声面 |
| 1652 | `.tmp/whitelist_backup_2026_10_17/_e_q_exec.txt` | 0 | 2026-10-14 14:07:09 | `e3b0c44298fc` | 噪声面 |
| 1653 | `.tmp/whitelist_backup_2026_10_17/_ea_179_domain_retest_2026_10_09.py` | 2,814 | 2026-10-09 21:39:22 | `9309e4977b22` | 噪声面 |
| 1654 | `.tmp/whitelist_backup_2026_10_17/_ecr_pa_a0_recompute_2026_10_15.py` | 8,804 | 2026-10-15 09:51:27 | `92e204d66c84` | 噪声面 |
| 1655 | `.tmp/whitelist_backup_2026_10_17/_ecr_pa_register_src_2026_10_15.md` | 15,707 | 2026-10-15 09:56:56 | `2c7c202aafec` | 噪声面 |
| 1656 | `.tmp/whitelist_backup_2026_10_17/_en_final_2026_09_28.py` | 2,369 | 2026-09-28 18:46:57 | `97a05aace5a8` | 噪声面 |
| 1657 | `.tmp/whitelist_backup_2026_10_17/_en_verify2_2026_09_28.py` | 1,870 | 2026-09-28 18:44:24 | `7e84e75cb838` | 噪声面 |
| 1658 | `.tmp/whitelist_backup_2026_10_17/_en_verify3_2026_09_28.py` | 1,638 | 2026-09-28 18:45:03 | `658292cce916` | 噪声面 |
| 1659 | `.tmp/whitelist_backup_2026_10_17/_en_verify4_2026_09_28.py` | 1,484 | 2026-09-28 18:45:30 | `7eaeb9b4ba48` | 噪声面 |
| 1660 | `.tmp/whitelist_backup_2026_10_17/_en_verify_2026_09_28.py` | 6,071 | 2026-09-28 18:43:13 | `51d9410d459b` | 噪声面 |
| 1661 | `.tmp/whitelist_backup_2026_10_17/_execswitch_verify_2026_09_28.py` | 3,501 | 2026-09-28 16:58:51 | `0814f3c2d7ab` | 噪声面 |
| 1662 | `.tmp/whitelist_backup_2026_10_17/_final_check.py` | 1,562 | 2026-09-26 17:50:19 | `ee7f008d36cb` | 噪声面 |
| 1663 | `.tmp/whitelist_backup_2026_10_17/_final_sha.py` | 1,435 | 2026-09-28 15:25:11 | `8ea91ad82b9d` | 噪声面 |
| 1664 | `.tmp/whitelist_backup_2026_10_17/_final_verify.py` | 2,457 | 2026-10-16 23:02:32 | `88aad6650405` | 噪声面 |
| 1665 | `.tmp/whitelist_backup_2026_10_17/_ge01_g7_register_build.py` | 33,147 | 2026-10-14 20:31:19 | `7731337a516d` | 噪声面 |
| 1666 | `.tmp/whitelist_backup_2026_10_17/_ge01_g7_register_measure.py` | 5,090 | 2026-10-14 20:28:56 | `5c3454c88a92` | 噪声面 |
| 1667 | `.tmp/whitelist_backup_2026_10_17/_gh_tree.txt` | 341,814 | 2026-10-12 14:21:54 | `823cfbb23a03` | 噪声面 |
| 1668 | `.tmp/whitelist_backup_2026_10_17/_h_census_worker.json` | 10,037,568 | 2026-10-14 00:01:18 | `22531e8519b2` | 噪声面 |
| 1669 | `.tmp/whitelist_backup_2026_10_17/_h_census_worker.py` | 5,639 | 2026-10-13 23:59:47 | `7f858d86f865` | 噪声面 |
| 1670 | `.tmp/whitelist_backup_2026_10_17/_hash21.py` | 944 | 2026-09-28 20:05:13 | `0d5335f0ac54` | 噪声面 |
| 1671 | `.tmp/whitelist_backup_2026_10_17/_inspect_10cells.py` | 2,460 | 2026-09-26 17:40:36 | `919f8f4e8ad2` | 噪声面 |
| 1672 | `.tmp/whitelist_backup_2026_10_17/_inspect_batch4_rounds.py` | 898 | 2026-09-26 17:41:44 | `bf479a2667df` | 噪声面 |
| 1673 | `.tmp/whitelist_backup_2026_10_17/_intake_cards_35_48_extract.py` | 3,416 | 2026-10-10 15:07:41 | `74cca5bda270` | 噪声面 |
| 1674 | `.tmp/whitelist_backup_2026_10_17/_iscp_dual_impl_2026_10_09.py` | 2,974 | 2026-10-09 14:43:36 | `8734f4326d5a` | 噪声面 |
| 1675 | `.tmp/whitelist_backup_2026_10_17/_item35_v3_collinear_recompute_2026_10_01.py` | 16,493 | 2026-10-01 08:55:30 | `c8d859cbb69e` | 噪声面 |
| 1676 | `.tmp/whitelist_backup_2026_10_17/_kd04_c_den_exec_2026_10_10.py` | 21,430 | 2026-10-10 11:42:44 | `419f9f691e63` | 噪声面 |
| 1677 | `.tmp/whitelist_backup_2026_10_17/_kv3s43_diag_2026_10_09.py` | 614 | 2026-10-09 14:24:04 | `398ebf6f33e0` | 噪声面 |
| 1678 | `.tmp/whitelist_backup_2026_10_17/_lit_log.txt` | 8,733 | 2026-10-15 10:46:33 | `b062da7b654a` | 噪声面 |
| 1679 | `.tmp/whitelist_backup_2026_10_17/_m5_k5_net.err` | 0 | 2026-10-13 23:34:17 | `e3b0c44298fc` | 噪声面 |
| 1680 | `.tmp/whitelist_backup_2026_10_17/_m5_k5_net.json` | 92,060 | 2026-10-13 23:34:23 | `9d7fe894a26b` | 噪声面 |
| 1681 | `.tmp/whitelist_backup_2026_10_17/_m5_k5_net.py` | 3,173 | 2026-10-13 23:33:24 | `ec944f9178ea` | 噪声面 |
| 1682 | `.tmp/whitelist_backup_2026_10_17/_m5_k5_net2.json` | 952,252 | 2026-10-13 23:37:07 | `b2bc158e7499` | 噪声面 |
| 1683 | `.tmp/whitelist_backup_2026_10_17/_m5_k5_scan.err` | 0 | 2026-10-13 23:33:38 | `e3b0c44298fc` | 噪声面 |
| 1684 | `.tmp/whitelist_backup_2026_10_17/_m5_k5_scan.json` | 9,530 | 2026-10-13 23:34:49 | `ebf1ad76dc8a` | 噪声面 |
| 1685 | `.tmp/whitelist_backup_2026_10_17/_m5_k5_scan.py` | 3,541 | 2026-10-13 23:33:23 | `f5245072750f` | 噪声面 |
| 1686 | `.tmp/whitelist_backup_2026_10_17/_m5_reaudit_archive.py` | 1,405 | 2026-10-14 10:14:40 | `54540d871fb7` | 噪声面 |
| 1687 | `.tmp/whitelist_backup_2026_10_17/_m5_reaudit_archive_out.json` | 654 | 2026-10-14 10:15:31 | `e3542ccb4d3e` | 噪声面 |
| 1688 | `.tmp/whitelist_backup_2026_10_17/_m5_reaudit_detail.py` | 2,276 | 2026-10-14 10:11:40 | `f43d192a9726` | 噪声面 |
| 1689 | `.tmp/whitelist_backup_2026_10_17/_m5_reaudit_detail.txt` | 9,214 | 2026-10-14 10:11:55 | `8c117d51fc64` | 噪声面 |
| 1690 | `.tmp/whitelist_backup_2026_10_17/_m5_reaudit_probe.py` | 4,469 | 2026-10-14 10:09:04 | `5b005dd13f95` | 噪声面 |
| 1691 | `.tmp/whitelist_backup_2026_10_17/_mk_voided_reloc_register.py` | 13,003 | 2026-10-14 00:49:59 | `7c2d2f6955d0` | 噪声面 |
| 1692 | `.tmp/whitelist_backup_2026_10_17/_n1_n2_check.py` | 1,628 | 2026-09-26 17:46:43 | `71f3f53a6eed` | 噪声面 |
| 1693 | `.tmp/whitelist_backup_2026_10_17/_ofc_s1_inventory.json` | 216,695 | 2026-10-12 11:57:41 | `c2858312798b` | 噪声面 |
| 1694 | `.tmp/whitelist_backup_2026_10_17/_ofc_s1b_inventory.json` | 336,955 | 2026-10-12 11:59:42 | `a28f35879008` | 噪声面 |
| 1695 | `.tmp/whitelist_backup_2026_10_17/_patch21_emit.py` | 17,106 | 2026-09-28 20:26:10 | `1d3c8aea6bad` | 噪声面 |
| 1696 | `.tmp/whitelist_backup_2026_10_17/_patch21_make.py` | 8,807 | 2026-09-28 20:20:05 | `b6cfdfaf80fa` | 噪声面 |
| 1697 | `.tmp/whitelist_backup_2026_10_17/_patch21_run.py` | 3,866 | 2026-09-28 20:20:37 | `6333d9256716` | 噪声面 |
| 1698 | `.tmp/whitelist_backup_2026_10_17/_pc.py` | 431 | 2026-09-26 22:16:09 | `7c59c7e80d50` | 噪声面 |
| 1699 | `.tmp/whitelist_backup_2026_10_17/_pk_probe.py` | 398 | 2026-09-27 20:26:47 | `6d79ba939526` | 噪声面 |
| 1700 | `.tmp/whitelist_backup_2026_10_17/_pk_sha_scan.py` | 599 | 2026-09-29 18:32:20 | `df460eaec619` | 噪声面 |
| 1701 | `.tmp/whitelist_backup_2026_10_17/_pkf34_f3.py` | 3,068 | 2026-09-28 15:12:48 | `389b3fdecd29` | 噪声面 |
| 1702 | `.tmp/whitelist_backup_2026_10_17/_pkf34_f34.py` | 4,282 | 2026-09-28 15:19:40 | `a972a0383cf4` | 噪声面 |
| 1703 | `.tmp/whitelist_backup_2026_10_17/_pkf34_f3b.py` | 2,703 | 2026-09-28 15:14:55 | `e1bcbf3897d8` | 噪声面 |
| 1704 | `.tmp/whitelist_backup_2026_10_17/_pkf34_f4.py` | 3,958 | 2026-09-28 15:15:32 | `880a69b9cf29` | 噪声面 |
| 1705 | `.tmp/whitelist_backup_2026_10_17/_pkf34_f4b.py` | 4,401 | 2026-09-28 15:16:34 | `e97f6ee41bec` | 噪声面 |
| 1706 | `.tmp/whitelist_backup_2026_10_17/_pkf34_f4c.py` | 3,045 | 2026-09-28 15:18:35 | `c758efa2a529` | 噪声面 |
| 1707 | `.tmp/whitelist_backup_2026_10_17/_pkf34_f4d.py` | 3,686 | 2026-09-28 15:21:17 | `fb565a667edc` | 噪声面 |
| 1708 | `.tmp/whitelist_backup_2026_10_17/_pkf34_final.py` | 5,903 | 2026-09-28 15:22:31 | `4b6140aaa618` | 噪声面 |
| 1709 | `.tmp/whitelist_backup_2026_10_17/_pkf34_nd.py` | 2,537 | 2026-09-28 15:24:13 | `527883f7ebb8` | 噪声面 |
| 1710 | `.tmp/whitelist_backup_2026_10_17/_pkf34_v12.py` | 5,639 | 2026-09-28 15:23:28 | `c650b0c20eee` | 噪声面 |
| 1711 | `.tmp/whitelist_backup_2026_10_17/_postcheck_v16_alt.py` | 1,282 | 2026-09-26 16:52:45 | `4d485d7a4d91` | 噪声面 |
| 1712 | `.tmp/whitelist_backup_2026_10_17/_postcheck_v16_alt_stdout.txt` | 1,558 | 2026-09-26 16:52:55 | `f116b23fa967` | 噪声面 |
| 1713 | `.tmp/whitelist_backup_2026_10_17/_postcheck_v16_sha.py` | 1,391 | 2026-09-26 16:51:40 | `46759ba2b8e5` | 噪声面 |
| 1714 | `.tmp/whitelist_backup_2026_10_17/_pre_mod/exp_harness_pre.py` | 36,217 | 2026-10-16 16:16:29 | `d5c8d676bb5b` | 噪声面 |
| 1715 | `.tmp/whitelist_backup_2026_10_17/_precheck_v15_tail.ps1` | 505 | 2026-09-26 16:50:30 | `e94d8011bbf4` | 噪声面 |
| 1716 | `.tmp/whitelist_backup_2026_10_17/_probe21.py` | 564 | 2026-09-28 20:02:53 | `5a40370032b3` | 噪声面 |
| 1717 | `.tmp/whitelist_backup_2026_10_17/_r10.py` | 1,525 | 2026-09-28 15:24:35 | `1b012cd12a00` | 噪声面 |
| 1718 | `.tmp/whitelist_backup_2026_10_17/_r1_alarm_test.py` | 2,297 | 2026-09-28 15:14:54 | `c44a09297f1a` | 噪声面 |
| 1719 | `.tmp/whitelist_backup_2026_10_17/_r2_body.md` | 63,091 | 2026-10-14 02:50:00 | `1dbe20a3ba1c` | 噪声面 |
| 1720 | `.tmp/whitelist_backup_2026_10_17/_r3_header_fix_2026_09_28.py` | 3,280 | 2026-09-28 17:24:56 | `6f8cec0fe006` | 噪声面 |
| 1721 | `.tmp/whitelist_backup_2026_10_17/_r3_verify_2026_09_28.py` | 5,494 | 2026-09-28 17:26:33 | `721e52f9d55f` | 噪声面 |
| 1722 | `.tmp/whitelist_backup_2026_10_17/_r4_cleanup_worker_keycount_2026_09_29.py` | 1,909 | 2026-09-29 14:08:03 | `ca0cbafed00b` | 噪声面 |
| 1723 | `.tmp/whitelist_backup_2026_10_17/_r4_cleanup_worker_keyscan_2026_09_29.py` | 3,561 | 2026-09-29 14:10:46 | `01e1ac2ef239` | 噪声面 |
| 1724 | `.tmp/whitelist_backup_2026_10_17/_r4_cleanup_worker_nearmiss_2026_09_29.py` | 1,382 | 2026-09-29 14:08:35 | `22336cc16500` | 噪声面 |
| 1725 | `.tmp/whitelist_backup_2026_10_17/_r4_cleanup_worker_scan_2026_09_29.py` | 2,411 | 2026-09-29 14:04:31 | `af404c489392` | 噪声面 |
| 1726 | `.tmp/whitelist_backup_2026_10_17/_r4_cleanup_worker_shape_2026_09_29.py` | 1,110 | 2026-09-29 14:08:58 | `f7f6313edce8` | 噪声面 |
| 1727 | `.tmp/whitelist_backup_2026_10_17/_r4_key_scan_2026_09_24.py` | 3,743 | 2026-09-24 18:50:23 | `c782d1a18092` | 噪声面 |
| 1728 | `.tmp/whitelist_backup_2026_10_17/_r4_key_scan_r1_files_2026_09_27.py` | 4,079 | 2026-09-27 17:07:38 | `cec4c1f3ff9c` | 噪声面 |
| 1729 | `.tmp/whitelist_backup_2026_10_17/_r5_write_register_2026_10_13.py` | 25,902 | 2026-10-14 00:31:16 | `139c8a7316db` | 噪声面 |
| 1730 | `.tmp/whitelist_backup_2026_10_17/_r6_evidence.py` | 2,525 | 2026-09-28 15:19:39 | `4de12a4f441b` | 噪声面 |
| 1731 | `.tmp/whitelist_backup_2026_10_17/_recheck_r1_run1.log` | 2,486 | 2026-09-27 17:03:26 | `80b338a0e9ad` | 噪声面 |
| 1732 | `.tmp/whitelist_backup_2026_10_17/_recheck_r1_runA.log` | 2,634 | 2026-09-27 17:06:49 | `68c85cf076d1` | 噪声面 |
| 1733 | `.tmp/whitelist_backup_2026_10_17/_recheck_r1_runB.log` | 2,634 | 2026-09-27 17:08:43 | `68c85cf076d1` | 噪声面 |
| 1734 | `.tmp/whitelist_backup_2026_10_17/_recheck_r1_runC.log` | 2,568 | 2026-09-27 17:11:24 | `b15384cff9f0` | 噪声面 |
| 1735 | `.tmp/whitelist_backup_2026_10_17/_recheck_r1_runD.log` | 2,568 | 2026-09-27 17:13:08 | `b15384cff9f0` | 噪声面 |
| 1736 | `.tmp/whitelist_backup_2026_10_17/_rj5_convention_check_2026_09_27.out.json` | 8,983 | 2026-09-27 17:21:39 | `c88e4ba1a4ce` | 噪声面 |
| 1737 | `.tmp/whitelist_backup_2026_10_17/_rj5_convention_check_2026_09_27.py` | 8,018 | 2026-09-27 17:21:32 | `5dbb93b3c5e5` | 噪声面 |
| 1738 | `.tmp/whitelist_backup_2026_10_17/_rj5_mapping_test_2026_09_27.py` | 5,968 | 2026-09-27 17:26:43 | `75ff70d87bd7` | 噪声面 |
| 1739 | `.tmp/whitelist_backup_2026_10_17/_rp4_fields.py` | 433 | 2026-10-09 14:14:54 | `1d112ab8f3b4` | 噪声面 |
| 1740 | `.tmp/whitelist_backup_2026_10_17/_rp_addendum_build_2026_10_09.py` | 30,375 | 2026-10-09 16:45:20 | `c4e8b75d656b` | 噪声面 |
| 1741 | `.tmp/whitelist_backup_2026_10_17/_rp_verify_2026_10_09.py` | 3,282 | 2026-10-09 16:46:36 | `e0adae15fc26` | 噪声面 |
| 1742 | `.tmp/whitelist_backup_2026_10_17/_rpd_neighbors_2026_10_09.py` | 1,286 | 2026-10-09 12:35:20 | `28cfa9466ea3` | 噪声面 |
| 1743 | `.tmp/whitelist_backup_2026_10_17/_rpd_reuse_strict_2026_10_09.py` | 4,746 | 2026-10-09 12:35:42 | `4557b47b7361` | 噪声面 |
| 1744 | `.tmp/whitelist_backup_2026_10_17/_rpd_verify_landed_2026_10_09.py` | 6,335 | 2026-10-09 12:38:16 | `912a2b8066f1` | 噪声面 |
| 1745 | `.tmp/whitelist_backup_2026_10_17/_run2.py` | 4,366 | 2026-09-27 12:58:13 | `8acbf24342d1` | 噪声面 |
| 1746 | `.tmp/whitelist_backup_2026_10_17/_run_d4_relabel_addendum.py` | 17,550 | 2026-09-27 17:04:03 | `620eabf853af` | 噪声面 |
| 1747 | `.tmp/whitelist_backup_2026_10_17/_run_d6_addendum_2026_09_28.py` | 23,204 | 2026-09-28 13:46:23 | `e472ea36ed08` | 噪声面 |
| 1748 | `.tmp/whitelist_backup_2026_10_17/_run_d6b_addendum_2026_09_28.py` | 31,468 | 2026-09-28 14:59:58 | `f0a4e919eeaa` | 噪声面 |
| 1749 | `.tmp/whitelist_backup_2026_10_17/_run_d8_addendum_2026_09_30.py` | 107,959 | 2026-09-30 16:17:55 | `7ce330b3e5ae` | 噪声面 |
| 1750 | `.tmp/whitelist_backup_2026_10_17/_run_d8_bhalf_addendum_2026_09_30.py` | 40,576 | 2026-09-30 16:21:44 | `90fa2c443529` | 噪声面 |
| 1751 | `.tmp/whitelist_backup_2026_10_17/_run_day_inventory_table_2026_09_27.py` | 2,763 | 2026-09-27 18:06:59 | `329bf2b66422` | 噪声面 |
| 1752 | `.tmp/whitelist_backup_2026_10_17/_run_final.py` | 26,654 | 2026-09-27 13:03:49 | `75d466add5d5` | 噪声面 |
| 1753 | `.tmp/whitelist_backup_2026_10_17/_run_final_selfscan_2026_09_27.py` | 1,358 | 2026-09-27 18:10:35 | `cf5c5c7684bb` | 噪声面 |
| 1754 | `.tmp/whitelist_backup_2026_10_17/_run_frozen_0touch_verify_2026_09_27.py` | 2,309 | 2026-09-27 18:05:45 | `48246f41e7d3` | 噪声面 |
| 1755 | `.tmp/whitelist_backup_2026_10_17/_run_recheck_r1.py` | 34,895 | 2026-09-27 17:09:39 | `a76ec3a2340e` | 噪声面 |
| 1756 | `.tmp/whitelist_backup_2026_10_17/_run_result_v3.py` | 3,304 | 2026-09-27 12:58:01 | `83cd4414f404` | 噪声面 |
| 1757 | `.tmp/whitelist_backup_2026_10_17/_run_v3r1_relabel.py` | 30,875 | 2026-09-27 17:46:57 | `55d06ce42b3d` | 噪声面 |
| 1758 | `.tmp/whitelist_backup_2026_10_17/_s3_f1_loader_fix_recompute_2026_10_08.py` | 21,231 | 2026-10-08 16:57:51 | `e39e4ae7d6ed` | 噪声面 |
| 1759 | `.tmp/whitelist_backup_2026_10_17/_s4_freeze_count_crosscheck2_2026_10_09.py` | 3,920 | 2026-10-09 14:12:07 | `15fa4d155fc9` | 噪声面 |
| 1760 | `.tmp/whitelist_backup_2026_10_17/_s4_freeze_count_crosscheck3_2026_10_09.py` | 4,041 | 2026-10-09 14:12:34 | `ee420dfd57e6` | 噪声面 |
| 1761 | `.tmp/whitelist_backup_2026_10_17/_s4_freeze_count_crosscheck_2026_10_09.py` | 3,463 | 2026-10-09 14:11:12 | `856e6ab48dae` | 噪声面 |
| 1762 | `.tmp/whitelist_backup_2026_10_17/_s4_seedprime_seq_t1_supplement_2026_10_11.py` | 31,705 | 2026-10-11 00:50:21 | `3a9db2126e4f` | 噪声面 |
| 1763 | `.tmp/whitelist_backup_2026_10_17/_s4_topup_addendum_builder_2026_10_09.py` | 21,122 | 2026-10-09 13:53:01 | `b9987c7a8d5f` | 噪声面 |
| 1764 | `.tmp/whitelist_backup_2026_10_17/_s4_tree_construct_exec_2026_10_10.py` | 34,265 | 2026-10-10 09:51:36 | `4cbd10b61aae` | 噪声面 |
| 1765 | `.tmp/whitelist_backup_2026_10_17/_s4f2_dbg.py` | 431 | 2026-10-09 15:33:21 | `5159c9c30180` | 噪声面 |
| 1766 | `.tmp/whitelist_backup_2026_10_17/_s4f2_face_probe_2026_10_09.py` | 14,896 | 2026-10-09 15:33:39 | `62e04248d122` | 噪声面 |
| 1767 | `.tmp/whitelist_backup_2026_10_17/_s4f2_patch.py` | 2,740 | 2026-10-09 15:30:03 | `b79a7073099d` | 噪声面 |
| 1768 | `.tmp/whitelist_backup_2026_10_17/_s4f2_patch2.py` | 421 | 2026-10-09 15:31:07 | `045bd90b237a` | 噪声面 |
| 1769 | `.tmp/whitelist_backup_2026_10_17/_s4f2_patch3.py` | 815 | 2026-10-09 15:31:52 | `6d57ff4ce76c` | 噪声面 |
| 1770 | `.tmp/whitelist_backup_2026_10_17/_s4f2_patch4.py` | 565 | 2026-10-09 15:32:23 | `7d85756a841d` | 噪声面 |
| 1771 | `.tmp/whitelist_backup_2026_10_17/_s4f2_scanner_selftest.py` | 1,819 | 2026-10-09 15:31:23 | `5b6fd262f785` | 噪声面 |
| 1772 | `.tmp/whitelist_backup_2026_10_17/_s4fs_auxdate_2026_10_09.py` | 1,877 | 2026-10-09 15:29:05 | `637e936d8bc7` | 噪声面 |
| 1773 | `.tmp/whitelist_backup_2026_10_17/_s4fs_selfreport_2026_10_09.py` | 432 | 2026-10-09 15:32:06 | `485071c7dd5e` | 噪声面 |
| 1774 | `.tmp/whitelist_backup_2026_10_17/_s4fs_yitable_2026_10_09.py` | 1,634 | 2026-10-09 15:29:34 | `2bf7fd0ef5dc` | 噪声面 |
| 1775 | `.tmp/whitelist_backup_2026_10_17/_s4oq_addendum_struct_2026_10_09.py` | 843 | 2026-10-09 14:25:17 | `67652acdf681` | 噪声面 |
| 1776 | `.tmp/whitelist_backup_2026_10_17/_s4oq_build_baseline_2026_10_09.py` | 3,501 | 2026-10-09 13:29:27 | `3cf28fe89611` | 噪声面 |
| 1777 | `.tmp/whitelist_backup_2026_10_17/_s4oq_build_draft_2026_10_09.py` | 8,719 | 2026-10-09 14:28:47 | `0797d19dcaf3` | 噪声面 |
| 1778 | `.tmp/whitelist_backup_2026_10_17/_s4oq_cellmap_2026_10_09.py` | 1,734 | 2026-10-09 13:30:29 | `c07589f292e1` | 噪声面 |
| 1779 | `.tmp/whitelist_backup_2026_10_17/_s4oq_final_verify_2026_10_09.py` | 959 | 2026-10-09 14:31:04 | `944a4f7006c8` | 噪声面 |
| 1780 | `.tmp/whitelist_backup_2026_10_17/_s4oq_forward_2026_10_09.py` | 3,482 | 2026-10-09 14:28:05 | `43e72c62587d` | 噪声面 |
| 1781 | `.tmp/whitelist_backup_2026_10_17/_s4oq_grid_cmp_2026_10_09.py` | 1,601 | 2026-10-09 14:26:50 | `f00865587d6a` | 噪声面 |
| 1782 | `.tmp/whitelist_backup_2026_10_17/_s4oq_grid_diag_2026_10_09.py` | 1,553 | 2026-10-09 14:26:34 | `082e8b8b7bc4` | 噪声面 |
| 1783 | `.tmp/whitelist_backup_2026_10_17/_s4oq_grid_recompute_2026_10_09.py` | 2,394 | 2026-10-09 14:26:19 | `afb613f5ced1` | 噪声面 |
| 1784 | `.tmp/whitelist_backup_2026_10_17/_s4oq_keyscan_2026_10_09.py` | 573 | 2026-10-09 13:29:42 | `c9f94c812f7f` | 噪声面 |
| 1785 | `.tmp/whitelist_backup_2026_10_17/_s4oq_recompute_2026_10_09.py` | 3,202 | 2026-10-09 14:29:39 | `07cdec653345` | 噪声面 |
| 1786 | `.tmp/whitelist_backup_2026_10_17/_s4oq_reuse_check_2026_10_09.py` | 6,712 | 2026-10-09 13:29:55 | `952c76c5b103` | 噪声面 |
| 1787 | `.tmp/whitelist_backup_2026_10_17/_s4oq_reuse_v2_2026_10_09.py` | 6,293 | 2026-10-09 13:30:18 | `bc0f200edd1e` | 噪声面 |
| 1788 | `.tmp/whitelist_backup_2026_10_17/_s4oq_skel_2026_10_09.py` | 466 | 2026-10-09 14:27:26 | `73fc780b4849` | 噪声面 |
| 1789 | `.tmp/whitelist_backup_2026_10_17/_s4oq_slug_opt_2026_10_09.py` | 4,636 | 2026-10-09 13:30:50 | `77d696b1690d` | 噪声面 |
| 1790 | `.tmp/whitelist_backup_2026_10_17/_s4oq_slug_search2_2026_10_09.py` | 5,258 | 2026-10-09 13:31:17 | `fe6f7044ec4e` | 噪声面 |
| 1791 | `.tmp/whitelist_backup_2026_10_17/_s4oq_variants_2026_10_09.py` | 1,233 | 2026-10-09 14:27:35 | `ccbbb499e19a` | 噪声面 |
| 1792 | `.tmp/whitelist_backup_2026_10_17/_s4oq_verify_addendum_2026_10_09.py` | 2,252 | 2026-10-09 14:29:27 | `419c15a7a2c5` | 噪声面 |
| 1793 | `.tmp/whitelist_backup_2026_10_17/_s4oq_write_addendum_2026_10_09.py` | 11,886 | 2026-10-09 14:29:16 | `63e61afa6517` | 噪声面 |
| 1794 | `.tmp/whitelist_backup_2026_10_17/_s4td_cell_map_2026_10_09.py` | 3,642 | 2026-10-09 10:57:41 | `6665669d858d` | 噪声面 |
| 1795 | `.tmp/whitelist_backup_2026_10_17/_s4td_floor_bound_2026_10_09.py` | 4,378 | 2026-10-09 10:57:16 | `ad95b6d5e9b9` | 噪声面 |
| 1796 | `.tmp/whitelist_backup_2026_10_17/_s4td_reuse_and_bound_2026_10_09.py` | 8,765 | 2026-10-09 10:56:36 | `af6fdc892f60` | 噪声面 |
| 1797 | `.tmp/whitelist_backup_2026_10_17/_s4td_slug_search_2026_10_09.py` | 4,657 | 2026-10-09 10:55:52 | `ce5529ec7516` | 噪声面 |
| 1798 | `.tmp/whitelist_backup_2026_10_17/_s5dp_five_lines_runner_third_2026_10_11.py` | 31,138 | 2026-10-11 18:12:11 | `9de3c08e3863` | 噪声面 |
| 1799 | `.tmp/whitelist_backup_2026_10_17/_sensitivity.py` | 5,954 | 2026-09-26 17:47:02 | `8aacafa48f9c` | 噪声面 |
| 1800 | `.tmp/whitelist_backup_2026_10_17/_sha12_check.ps1` | 697 | 2026-09-26 17:24:02 | `a4bfec107a77` | 噪声面 |
| 1801 | `.tmp/whitelist_backup_2026_10_17/_sha12_check2.ps1` | 691 | 2026-09-26 17:25:01 | `3e9174fb1e03` | 噪声面 |
| 1802 | `.tmp/whitelist_backup_2026_10_17/_t15_inspect.py` | 2,728 | 2026-09-25 00:42:09 | `9877c9536e33` | 噪声面 |
| 1803 | `.tmp/whitelist_backup_2026_10_17/_t15_inspect2.py` | 1,942 | 2026-09-25 00:42:27 | `9a6b5bb328aa` | 噪声面 |
| 1804 | `.tmp/whitelist_backup_2026_10_17/_t15_inspect3.py` | 1,890 | 2026-09-25 00:43:08 | `d423ca72cb3c` | 噪声面 |
| 1805 | `.tmp/whitelist_backup_2026_10_17/_t15_inspect4.py` | 2,756 | 2026-09-25 00:43:48 | `069b7562f463` | 噪声面 |
| 1806 | `.tmp/whitelist_backup_2026_10_17/_t15_inspect5.py` | 2,712 | 2026-09-25 00:44:00 | `977753c193d2` | 噪声面 |
| 1807 | `.tmp/whitelist_backup_2026_10_17/_t15_inspect6.py` | 1,234 | 2026-09-25 00:44:53 | `eba3a29f6264` | 噪声面 |
| 1808 | `.tmp/whitelist_backup_2026_10_17/_t15_inspect7.py` | 3,880 | 2026-09-25 00:45:14 | `78dafdf124f7` | 噪声面 |
| 1809 | `.tmp/whitelist_backup_2026_10_17/_t15_percell.py` | 596 | 2026-09-25 00:45:42 | `c035476cfb41` | 噪声面 |
| 1810 | `.tmp/whitelist_backup_2026_10_17/_t15_probe_log.json` | 718 | 2026-09-24 23:58:16 | `94444963ff77` | 噪声面 |
| 1811 | `.tmp/whitelist_backup_2026_10_17/_t15_records.json` | 96,443 | 2026-09-25 00:41:37 | `8014af0e2b79` | 噪声面 |
| 1812 | `.tmp/whitelist_backup_2026_10_17/_t15_update_result.py` | 9,226 | 2026-09-25 00:44:30 | `ad66f242c6a1` | 噪声面 |
| 1813 | `.tmp/whitelist_backup_2026_10_17/_t15r2_inspect.py` | 3,730 | 2026-09-26 16:47:14 | `c58dc90fd86a` | 噪声面 |
| 1814 | `.tmp/whitelist_backup_2026_10_17/_t15r2_verify.py` | 6,737 | 2026-09-26 17:16:23 | `5267b4dee7dc` | 噪声面 |
| 1815 | `.tmp/whitelist_backup_2026_10_17/_t1_exp2_c_driver_2026_10_09.py` | 2,898 | 2026-10-09 22:22:58 | `5d474b7ceada` | 噪声面 |
| 1816 | `.tmp/whitelist_backup_2026_10_17/_t1_exp2_c_records.json` | 6,277,328 | 2026-10-10 02:31:55 | `f53681c7569a` | 噪声面 |
| 1817 | `.tmp/whitelist_backup_2026_10_17/_t1_exp2_calib_2026_10_09.json` | 611 | 2026-10-09 22:20:17 | `de09d4ee3721` | 噪声面 |
| 1818 | `.tmp/whitelist_backup_2026_10_17/_t1_exp2_d_readings.json` | 3,991 | 2026-10-09 22:45:37 | `2315f6823011` | 噪声面 |
| 1819 | `.tmp/whitelist_backup_2026_10_17/_t1_exp2_d_records.json` | 488,395 | 2026-10-09 22:44:11 | `aadba0c4f952` | 噪声面 |
| 1820 | `.tmp/whitelist_backup_2026_10_17/_t1_exp2_probe_log.json` | 760 | 2026-10-09 22:19:48 | `c6478415e2bf` | 噪声面 |
| 1821 | `.tmp/whitelist_backup_2026_10_17/_t1_exp2_selfcert.json` | 6,780 | 2026-10-09 22:19:29 | `d929eb9ae0b8` | 噪声面 |
| 1822 | `.tmp/whitelist_backup_2026_10_17/_t1_gap_domain_sweep_2026_10_01.py` | 2,502 | 2026-10-01 14:37:27 | `74d1ed439442` | 噪声面 |
| 1823 | `.tmp/whitelist_backup_2026_10_17/_t1_gap_implA_2026_10_01.py` | 4,468 | 2026-10-01 14:35:01 | `c5d1dc7badcd` | 噪声面 |
| 1824 | `.tmp/whitelist_backup_2026_10_17/_t1_gap_implB_2026_10_01.ps1` | 5,735 | 2026-10-01 14:36:27 | `19aebfd44310` | 噪声面 |
| 1825 | `.tmp/whitelist_backup_2026_10_17/_t1_gap_postwrite_verify_2026_10_01.py` | 5,666 | 2026-10-01 14:40:48 | `33b4108f14a1` | 噪声面 |
| 1826 | `.tmp/whitelist_backup_2026_10_17/_t1_gap_snapshot_2026_10_01.py` | 2,588 | 2026-10-01 14:38:44 | `fd53258bd16f` | 噪声面 |
| 1827 | `.tmp/whitelist_backup_2026_10_17/_t1_qwen_temp_sweep_decomposition.py` | 1,981 | 2026-10-09 11:16:56 | `97a6520c7105` | 噪声面 |
| 1828 | `.tmp/whitelist_backup_2026_10_17/_t1_qwen_temp_sweep_dump_readings.py` | 1,137 | 2026-10-09 11:16:31 | `7e06567afc2a` | 噪声面 |
| 1829 | `.tmp/whitelist_backup_2026_10_17/_t1_qwen_temp_sweep_probe_log.json` | 445 | 2026-10-09 10:23:35 | `b5e4151af490` | 噪声面 |
| 1830 | `.tmp/whitelist_backup_2026_10_17/_t1_qwen_temp_sweep_r2_probe_log.json` | 739 | 2026-10-09 16:59:00 | `5182f6fdd9ef` | 噪声面 |
| 1831 | `.tmp/whitelist_backup_2026_10_17/_t1_qwen_temp_sweep_r2_records.json` | 1,795,870 | 2026-10-09 18:03:12 | `bb511e7b0baf` | 噪声面 |
| 1832 | `.tmp/whitelist_backup_2026_10_17/_t1_qwen_temp_sweep_r2_selfcert.json` | 6,353 | 2026-10-09 16:58:49 | `124051b56295` | 噪声面 |
| 1833 | `.tmp/whitelist_backup_2026_10_17/_t1_qwen_temp_sweep_readings.json` | 11,013 | 2026-10-09 11:15:36 | `e5e8f024e42e` | 噪声面 |
| 1834 | `.tmp/whitelist_backup_2026_10_17/_t1_qwen_temp_sweep_records.json` | 96,866 | 2026-10-09 11:15:00 | `5b51af62c640` | 噪声面 |
| 1835 | `.tmp/whitelist_backup_2026_10_17/_t1_qwen_temp_sweep_selfcert.json` | 3,866 | 2026-10-09 10:22:42 | `91c2505deef3` | 噪声面 |
| 1836 | `.tmp/whitelist_backup_2026_10_17/_t1_r2_calib_max_tokens_2026_10_09.json` | 3,305 | 2026-10-09 16:55:16 | `3f35aede29f6` | 噪声面 |
| 1837 | `.tmp/whitelist_backup_2026_10_17/_t1_r2_calib_max_tokens_2026_10_09.py` | 6,120 | 2026-10-09 16:52:24 | `7bbb0de0c00f` | 噪声面 |
| 1838 | `.tmp/whitelist_backup_2026_10_17/_t1_r2_run_driver_2026_10_09.py` | 2,749 | 2026-10-09 16:59:17 | `b71f4916bee1` | 噪声面 |
| 1839 | `.tmp/whitelist_backup_2026_10_17/_t1_r2_verify_2026_10_09.py` | 4,018 | 2026-10-09 16:59:55 | `3ce6d45cfbf7` | 噪声面 |
| 1840 | `.tmp/whitelist_backup_2026_10_17/_t1_verdict_probe_readonly.txt` | 4,655 | 2026-10-09 11:49:48 | `0e2df9ca7ab2` | 噪声面 |
| 1841 | `.tmp/whitelist_backup_2026_10_17/_t2_t3_lit_search.py` | 5,695 | 2026-10-15 10:44:35 | `0829d37e0cd8` | 噪声面 |
| 1842 | `.tmp/whitelist_backup_2026_10_17/_t2_t3_lit_search2.py` | 4,946 | 2026-10-15 10:46:58 | `c0caa8ba29f1` | 噪声面 |
| 1843 | `.tmp/whitelist_backup_2026_10_17/_t2_t3_lit_search2_out.json` | 29,596 | 2026-10-15 10:47:49 | `13ffff0d0b28` | 噪声面 |
| 1844 | `.tmp/whitelist_backup_2026_10_17/_t2_t3_lit_search_out.json` | 26,588 | 2026-10-15 10:46:33 | `cc70fac3d81b` | 噪声面 |
| 1845 | `.tmp/whitelist_backup_2026_10_17/_t2_t3_llm_probe.py` | 4,544 | 2026-10-15 10:42:47 | `5561f7af5662` | 噪声面 |
| 1846 | `.tmp/whitelist_backup_2026_10_17/_t2_t3_llm_probe_out.json` | 5,331 | 2026-10-15 10:43:15 | `993477af77db` | 噪声面 |
| 1847 | `.tmp/whitelist_backup_2026_10_17/_t2_t3_prex_a_route.py` | 10,166 | 2026-10-15 10:41:33 | `c25af5d2966b` | 噪声面 |
| 1848 | `.tmp/whitelist_backup_2026_10_17/_t2_t3_prex_a_route2.py` | 5,850 | 2026-10-15 10:42:24 | `0c44afba463a` | 噪声面 |
| 1849 | `.tmp/whitelist_backup_2026_10_17/_t2_t3_prex_a_route2_out.json` | 6,949 | 2026-10-15 10:42:30 | `63f37ba943c1` | 噪声面 |
| 1850 | `.tmp/whitelist_backup_2026_10_17/_t2_t3_prex_a_route_out.json` | 22,640 | 2026-10-15 10:41:50 | `3cad087a69c3` | 噪声面 |
| 1851 | `.tmp/whitelist_backup_2026_10_17/_tail3_atomic_landing_check_2026_09_29.py` | 2,699 | 2026-09-29 11:23:08 | `5c19cf8f29fb` | 噪声面 |
| 1852 | `.tmp/whitelist_backup_2026_10_17/_tail3_atomic_make_2026_09_29.py` | 17,272 | 2026-09-29 11:12:32 | `94d57549533b` | 噪声面 |
| 1853 | `.tmp/whitelist_backup_2026_10_17/_tail3_atomic_refs_2026_09_29.py` | 2,636 | 2026-09-29 11:18:36 | `4e8ea9bea948` | 噪声面 |
| 1854 | `.tmp/whitelist_backup_2026_10_17/_tail3_atomic_verify_2026_09_29.py` | 21,338 | 2026-09-29 11:17:43 | `8d12c9c9cb2d` | 噪声面 |
| 1855 | `.tmp/whitelist_backup_2026_10_17/_tail_only.py` | 436 | 2026-09-26 16:53:03 | `cf3bbd24b401` | 噪声面 |
| 1856 | `.tmp/whitelist_backup_2026_10_17/_trae_audit_part1.py` | 5,510 | 2026-09-28 15:16:16 | `ac67b341b56b` | 噪声面 |
| 1857 | `.tmp/whitelist_backup_2026_10_17/_trae_audit_part2.py` | 3,632 | 2026-09-28 15:16:42 | `9faaa564c3bc` | 噪声面 |
| 1858 | `.tmp/whitelist_backup_2026_10_17/_trae_audit_part3.py` | 8,617 | 2026-09-28 15:17:48 | `f4c994004311` | 噪声面 |
| 1859 | `.tmp/whitelist_backup_2026_10_17/_trae_audit_part3b.py` | 7,662 | 2026-09-28 15:18:57 | `c1a9a6c3c17a` | 噪声面 |
| 1860 | `.tmp/whitelist_backup_2026_10_17/_trae_audit_part4.py` | 7,173 | 2026-09-28 15:22:52 | `bc8d4721bf3b` | 噪声面 |
| 1861 | `.tmp/whitelist_backup_2026_10_17/_v412_contrib.py` | 1,040 | 2026-10-09 09:57:19 | `1085411b4896` | 噪声面 |
| 1862 | `.tmp/whitelist_backup_2026_10_17/_v412_material_scan.py` | 627 | 2026-10-09 09:55:00 | `f3493907cbe2` | 噪声面 |
| 1863 | `.tmp/whitelist_backup_2026_10_17/_v412_unique_scan.py` | 1,300 | 2026-10-09 09:57:37 | `b2e381f09828` | 噪声面 |
| 1864 | `.tmp/whitelist_backup_2026_10_17/_v5_c5_b_clause4_consistency_check.py` | 6,528 | 2026-09-29 13:42:09 | `56ad3329a3c7` | 噪声面 |
| 1865 | `.tmp/whitelist_backup_2026_10_17/_v5_c5_b_fetch_raw_embeddings.py` | 9,476 | 2026-09-29 13:39:27 | `8e4f2ae63de3` | 噪声面 |
| 1866 | `.tmp/whitelist_backup_2026_10_17/_v5_c5_b_fix_readings_2026_10_01.py` | 12,014 | 2026-10-01 09:24:51 | `191efa7fe0b6` | 噪声面 |
| 1867 | `.tmp/whitelist_backup_2026_10_17/_v5_item21_anchor_driver.py` | 5,401 | 2026-09-28 20:00:07 | `cb14f672dd1e` | 噪声面 |
| 1868 | `.tmp/whitelist_backup_2026_10_17/_v5_item21_patched_b1_semA_none_default.py` | 16,768 | 2026-09-28 20:20:12 | `ceb33de660fd` | 噪声面 |
| 1869 | `.tmp/whitelist_backup_2026_10_17/_v5_item21_patched_b1_semB_none_skip.py` | 16,829 | 2026-09-28 20:20:12 | `be0208abaffa` | 噪声面 |
| 1870 | `.tmp/whitelist_backup_2026_10_17/_v5_item21_patched_b2_semA_none_default.py` | 16,036 | 2026-09-28 20:20:12 | `801ee31e8bdc` | 噪声面 |
| 1871 | `.tmp/whitelist_backup_2026_10_17/_v5_item21_patched_b2_semB_none_skip.py` | 16,097 | 2026-09-28 20:20:12 | `8293535673dc` | 噪声面 |
| 1872 | `.tmp/whitelist_backup_2026_10_17/_v5_item21_patched_b3_semA_none_default.py` | 15,778 | 2026-09-28 20:20:12 | `9d8a4a875b62` | 噪声面 |
| 1873 | `.tmp/whitelist_backup_2026_10_17/_v5_item21_patched_b3_semB_none_skip.py` | 15,839 | 2026-09-28 20:20:12 | `8df8e94724ff` | 噪声面 |
| 1874 | `.tmp/whitelist_backup_2026_10_17/_v5_loadcorpus_verify_2026_09_29.py` | 8,798 | 2026-09-29 13:38:56 | `564e3575ab1d` | 噪声面 |
| 1875 | `.tmp/whitelist_backup_2026_10_17/_v5_qwen_retry_candidates_20260929.py` | 1,689 | 2026-09-29 11:09:26 | `f42600827cc3` | 噪声面 |
| 1876 | `.tmp/whitelist_backup_2026_10_17/_v5_qwen_retry_introspect_20260929.py` | 3,149 | 2026-09-29 11:08:54 | `117b64fc1d5b` | 噪声面 |
| 1877 | `.tmp/whitelist_backup_2026_10_17/_verdict_keeper_sha_helper.ps1` | 679 | 2026-09-25 01:28:00 | `bc11b03d3b84` | 噪声面 |
| 1878 | `.tmp/whitelist_backup_2026_10_17/_verify_d8_addendum_2026_09_30.py` | 4,900 | 2026-09-30 16:18:13 | `28de8c99c054` | 噪声面 |
| 1879 | `.tmp/whitelist_backup_2026_10_17/_verify_intake_supplement_6.py` | 3,678 | 2026-10-10 15:10:32 | `1fbb1bd1db6c` | 噪声面 |
| 1880 | `.tmp/whitelist_backup_2026_10_17/_verify_r32_card_2026_10_10.py` | 631 | 2026-10-10 10:30:11 | `61f99fc5fdb9` | 噪声面 |
| 1881 | `.tmp/whitelist_backup_2026_10_17/_verify_tail.py` | 733 | 2026-09-26 16:52:11 | `23198a6a0a9b` | 噪声面 |
| 1882 | `.tmp/whitelist_backup_2026_10_17/_verify_two_pieces_2026_09_30.py` | 4,739 | 2026-09-30 16:22:07 | `509afa876df0` | 噪声面 |
| 1883 | `.tmp/whitelist_backup_2026_10_17/_vk_pv02_recheck_a.py` | 4,188 | 2026-10-09 13:58:44 | `37d55bf0fba6` | 噪声面 |
| 1884 | `.tmp/whitelist_backup_2026_10_17/_vk_pv02_recheck_b.py` | 1,646 | 2026-10-09 13:59:19 | `fe0f10e38bb3` | 噪声面 |
| 1885 | `.tmp/whitelist_backup_2026_10_17/_vk_pv02_recheck_c.py` | 2,397 | 2026-10-09 13:59:48 | `7d35b715f8e2` | 噪声面 |
| 1886 | `.tmp/whitelist_backup_2026_10_17/_vk_pv02_recheck_d.py` | 982 | 2026-10-09 14:00:06 | `7ae7ed6bcd8a` | 噪声面 |
| 1887 | `.tmp/whitelist_backup_2026_10_17/_vk_pv02_recheck_e.py` | 1,742 | 2026-10-09 14:00:32 | `d925e60c1d3c` | 噪声面 |
| 1888 | `.tmp/whitelist_backup_2026_10_17/_vk_pv02_recheck_f.py` | 1,522 | 2026-10-09 14:00:45 | `c2e298ccebc6` | 噪声面 |
| 1889 | `.tmp/whitelist_backup_2026_10_17/_vk_pv02_recheck_g.py` | 2,269 | 2026-10-09 14:00:59 | `f237e1d2715f` | 噪声面 |
| 1890 | `.tmp/whitelist_backup_2026_10_17/_vk_q.py` | 519 | 2026-10-10 10:57:23 | `67364902116c` | 噪声面 |
| 1891 | `.tmp/whitelist_backup_2026_10_17/_vk_q2.py` | 540 | 2026-10-10 10:57:35 | `d5759d40dc43` | 噪声面 |
| 1892 | `.tmp/whitelist_backup_2026_10_17/_vk_q3.py` | 612 | 2026-10-10 10:57:46 | `a00cd309205f` | 噪声面 |
| 1893 | `.tmp/whitelist_backup_2026_10_17/_vk_q4.py` | 784 | 2026-10-10 10:58:01 | `defc3c53b7df` | 噪声面 |
| 1894 | `.tmp/whitelist_backup_2026_10_17/_vk_q5.py` | 1,246 | 2026-10-10 10:58:17 | `7b95307225ba` | 噪声面 |
| 1895 | `.tmp/whitelist_backup_2026_10_17/_vk_q6.py` | 811 | 2026-10-10 10:59:49 | `7da34dd24eb0` | 噪声面 |
| 1896 | `.tmp/whitelist_backup_2026_10_17/_vk_q7.py` | 1,331 | 2026-10-10 19:37:27 | `a6c525f88f11` | 噪声面 |
| 1897 | `.tmp/whitelist_backup_2026_10_17/_vk_q8.py` | 1,025 | 2026-10-10 19:37:42 | `5a81e5558c72` | 噪声面 |
| 1898 | `.tmp/whitelist_backup_2026_10_17/_vk_s4_topup_intake_recheck_2026_10_09.py` | 6,678 | 2026-10-09 13:58:59 | `a1d8047f1833` | 噪声面 |
| 1899 | `.tmp/whitelist_backup_2026_10_17/_vk_s4_topup_intake_recheck_2026_10_09.txt` | 7,098 | 2026-10-09 13:59:08 | `683501b8fb41` | 噪声面 |
| 1900 | `.tmp/whitelist_backup_2026_10_17/_w1_collect.py` | 19,559 | 2026-10-16 11:53:08 | `7c3155b2c370` | 噪声面 |
| 1901 | `.tmp/whitelist_backup_2026_10_17/_w1_drift_write.py` | 16,560 | 2026-10-16 11:55:50 | `44e026ae190d` | 噪声面 |
| 1902 | `.tmp/whitelist_backup_2026_10_17/_w1_freeze_write.py` | 24,351 | 2026-10-16 11:52:25 | `97211806b0d0` | 噪声面 |
| 1903 | `.tmp/whitelist_backup_2026_10_17/_w1_phaseB_write.py` | 31,303 | 2026-10-16 11:58:55 | `4e85afe94966` | 噪声面 |
| 1904 | `.tmp/whitelist_backup_2026_10_17/_w1_verify_final.py` | 7,944 | 2026-10-16 11:59:35 | `040c35e21bf2` | 噪声面 |
| 1905 | `.tmp/whitelist_backup_2026_10_17/_w5_9model_merge_2026_10_09.py` | 18,475 | 2026-10-09 12:08:13 | `afa52e90f332` | 噪声面 |
| 1906 | `.tmp/whitelist_backup_2026_10_17/_worker_write_ge01_unblock_progress.py` | 26,125 | 2026-10-14 14:13:26 | `7c18f854316c` | 噪声面 |
| 1907 | `.tmp/whitelist_backup_2026_10_17/_write_canonical_register.py` | 24,636 | 2026-10-14 14:09:17 | `867acc46aff9` | 噪声面 |
| 1908 | `.tmp/whitelist_backup_2026_10_17/_write_eps_grid_design.py` | 38,246 | 2026-10-14 00:13:04 | `df37b02f1c0f` | 噪声面 |
| 1909 | `.tmp/whitelist_backup_2026_10_17/_write_predelete_caliber_draft.py` | 32,826 | 2026-10-17 11:07:54 | `82d7f9c628b6` | 噪声面 |
| 1910 | `.tmp/whitelist_backup_2026_10_17/anch.py` | 1,484 | 2026-10-16 10:56:45 | `c05693efbb30` | 噪声面 |
| 1911 | `.tmp/whitelist_backup_2026_10_17/anch_v4_build.py` | 7,175 | 2026-10-16 20:18:44 | `adcae459701a` | 噪声面 |
| 1912 | `.tmp/whitelist_backup_2026_10_17/anch_v4_build_measurements.json` | 2,315 | 2026-10-16 20:19:51 | `5708226b943f` | 噪声面 |
| 1913 | `.tmp/whitelist_backup_2026_10_17/anch_v4_probe.py` | 2,662 | 2026-10-16 20:09:29 | `f47af093e3aa` | 噪声面 |
| 1914 | `.tmp/whitelist_backup_2026_10_17/archive_survey_census2.py` | 780 | 2026-10-17 11:39:09 | `2863f5edca41` | 噪声面 |
| 1915 | `.tmp/whitelist_backup_2026_10_17/body_relabel.md` | 8,672 | 2026-10-14 22:09:33 | `2660d5ea717d` | 噪声面 |
| 1916 | `.tmp/whitelist_backup_2026_10_17/body_v6_effect.md` | 15,467 | 2026-10-14 22:09:01 | `d79637fee0ef` | 噪声面 |
| 1917 | `.tmp/whitelist_backup_2026_10_17/claude_spotcheck.py` | 4,136 | 2026-09-30 21:45:51 | `a78755b356b9` | 噪声面 |
| 1918 | `.tmp/whitelist_backup_2026_10_17/cleanup511_manifest_2026_10_17.json` | 1,754,609 | 2026-10-17 10:13:01 | `b7093a701856` | 噪声面 |
| 1919 | `.tmp/whitelist_backup_2026_10_17/collision_survey_hashes.json` | 75,439 | 2026-10-17 10:07:58 | `0329afb1e9fc` | 噪声面 |
| 1920 | `.tmp/whitelist_backup_2026_10_17/collision_survey_inventory.json` | 37,588 | 2026-10-17 10:07:30 | `a4cd5b2fc5c8` | 噪声面 |
| 1921 | `.tmp/whitelist_backup_2026_10_17/combo_llm_calls_2026_10_16.jsonl` | 59,626 | 2026-10-16 11:58:25 | `86f05646031b` | 噪声面 |
| 1922 | `.tmp/whitelist_backup_2026_10_17/combo_measurement_2026_10_16.json` | 121,779 | 2026-10-16 11:58:25 | `27609799e40e` | 噪声面 |
| 1923 | `.tmp/whitelist_backup_2026_10_17/d05_hash_index.py` | 1,004 | 2026-10-10 11:51:23 | `070b6f865eba` | 噪声面 |
| 1924 | `.tmp/whitelist_backup_2026_10_17/d1fill_anchor_snapshot.py` | 1,985 | 2026-10-01 13:39:20 | `15c0b0ade7ab` | 噪声面 |
| 1925 | `.tmp/whitelist_backup_2026_10_17/d1fill_recount_checks.py` | 2,336 | 2026-10-01 13:38:49 | `b8af087b5e1f` | 噪声面 |
| 1926 | `.tmp/whitelist_backup_2026_10_17/d1fill_recount_impl1.py` | 6,464 | 2026-10-01 13:35:55 | `bb30ad15c89b` | 噪声面 |
| 1927 | `.tmp/whitelist_backup_2026_10_17/d1fill_recount_impl2.ps1` | 6,132 | 2026-10-01 13:38:15 | `88411408e671` | 噪声面 |
| 1928 | `.tmp/whitelist_backup_2026_10_17/diag.py` | 972 | 2026-10-13 23:40:22 | `db20dd0e6efb` | 噪声面 |
| 1929 | `.tmp/whitelist_backup_2026_10_17/diffcause.py` | 2,724 | 2026-10-10 13:47:39 | `2b24513cdf74` | 噪声面 |
| 1930 | `.tmp/whitelist_backup_2026_10_17/docwriter_c2_effect_census.json` | 36,157 | 2026-10-14 14:43:10 | `1ef99b1da14d` | 噪声面 |
| 1931 | `.tmp/whitelist_backup_2026_10_17/docwriter_c2_effect_census.py` | 5,518 | 2026-10-14 14:40:39 | `a8e52d7e9f8d` | 噪声面 |
| 1932 | `.tmp/whitelist_backup_2026_10_17/docwriter_c2_effect_table.py` | 1,400 | 2026-10-14 14:43:24 | `503230d1e7e3` | 噪声面 |
| 1933 | `.tmp/whitelist_backup_2026_10_17/docwriter_c2_effect_table.txt` | 21,554 | 2026-10-14 14:43:33 | `1b5382cc9936` | 噪声面 |
| 1934 | `.tmp/whitelist_backup_2026_10_17/docwriter_sigsup.py` | 13,645 | 2026-10-13 23:21:32 | `d116fefd336c` | 噪声面 |
| 1935 | `.tmp/whitelist_backup_2026_10_17/docwriter_v41_probe.py` | 6,503 | 2026-10-16 22:58:22 | `210a07303fe7` | 噪声面 |
| 1936 | `.tmp/whitelist_backup_2026_10_17/docwriter_v41_scan2.json` | 4,066 | 2026-10-16 22:59:21 | `e988b26ba229` | 噪声面 |
| 1937 | `.tmp/whitelist_backup_2026_10_17/docwriter_v41_scan2.py` | 3,661 | 2026-10-16 22:59:13 | `e88316a0fc2c` | 噪声面 |
| 1938 | `.tmp/whitelist_backup_2026_10_17/docwriter_v42_scan.py` | 4,601 | 2026-10-16 23:30:38 | `93d9c4c5c927` | 噪声面 |
| 1939 | `.tmp/whitelist_backup_2026_10_17/docwriter_v42_scan_out.txt` | 5,267 | 2026-10-16 23:30:52 | `d1470a9eaea9` | 噪声面 |
| 1940 | `.tmp/whitelist_backup_2026_10_17/docwriter_v42_verify.py` | 4,858 | 2026-10-16 23:37:19 | `47c794a64dff` | 噪声面 |
| 1941 | `.tmp/whitelist_backup_2026_10_17/docwriter_v42_verify_out.txt` | 2,899 | 2026-10-16 23:39:28 | `c38b853adda1` | 噪声面 |
| 1942 | `.tmp/whitelist_backup_2026_10_17/docwriter_v43_fp.py` | 1,488 | 2026-10-16 23:42:47 | `000c7e036d9c` | 噪声面 |
| 1943 | `.tmp/whitelist_backup_2026_10_17/docwriter_v43_fp2.py` | 1,716 | 2026-10-16 23:45:17 | `87ef5d8aba15` | 噪声面 |
| 1944 | `.tmp/whitelist_backup_2026_10_17/docwriter_v43_fp_out.txt` | 2,420 | 2026-10-16 23:45:26 | `35a223091bbe` | 噪声面 |
| 1945 | `.tmp/whitelist_backup_2026_10_17/docwriter_v43_scan.py` | 2,061 | 2026-10-16 23:43:51 | `5356708d6a6f` | 噪声面 |
| 1946 | `.tmp/whitelist_backup_2026_10_17/docwriter_v43_scan_out.txt` | 2,353 | 2026-10-16 23:44:03 | `c80e849e7c99` | 噪声面 |
| 1947 | `.tmp/whitelist_backup_2026_10_17/docwriter_v43_verify.py` | 4,497 | 2026-10-16 23:49:29 | `2cf26203f12d` | 噪声面 |
| 1948 | `.tmp/whitelist_backup_2026_10_17/docwriter_v43_verify_out.txt` | 759 | 2026-10-16 23:51:42 | `c1d14e3d7e06` | 噪声面 |
| 1949 | `.tmp/whitelist_backup_2026_10_17/docwriter_v44_fp.py` | 2,485 | 2026-10-17 00:00:58 | `4c2e2a4a2ad2` | 噪声面 |
| 1950 | `.tmp/whitelist_backup_2026_10_17/docwriter_v44_fp_out.txt` | 1,601 | 2026-10-17 00:01:08 | `6ab1382d766e` | 噪声面 |
| 1951 | `.tmp/whitelist_backup_2026_10_17/docwriter_v44_fresh.py` | 2,319 | 2026-10-17 00:14:18 | `855298e666f6` | 噪声面 |
| 1952 | `.tmp/whitelist_backup_2026_10_17/docwriter_v44_fresh_out.txt` | 1,646 | 2026-10-17 00:14:49 | `6d7d8ad5c4ed` | 噪声面 |
| 1953 | `.tmp/whitelist_backup_2026_10_17/docwriter_v44_scan.py` | 3,822 | 2026-10-17 00:02:38 | `3cc9fa3130a4` | 噪声面 |
| 1954 | `.tmp/whitelist_backup_2026_10_17/docwriter_v44_scan_out.txt` | 2,290 | 2026-10-17 00:02:52 | `24663bc22391` | 噪声面 |
| 1955 | `.tmp/whitelist_backup_2026_10_17/docwriter_v45_scan.py` | 5,186 | 2026-10-17 10:09:32 | `c6703629a7b0` | 噪声面 |
| 1956 | `.tmp/whitelist_backup_2026_10_17/docwriter_v45_scan_out.txt` | 1,661 | 2026-10-17 10:09:05 | `28c06dd53ae4` | 噪声面 |
| 1957 | `.tmp/whitelist_backup_2026_10_17/docwriter_v45_scan_out_r1.txt` | 1,661 | 2026-10-17 10:09:05 | `28c06dd53ae4` | 噪声面 |
| 1958 | `.tmp/whitelist_backup_2026_10_17/docwriter_v45_scan_out_r2.txt` | 1,728 | 2026-10-17 10:09:57 | `ef49039e5d90` | 噪声面 |
| 1959 | `.tmp/whitelist_backup_2026_10_17/docwriter_v45_scan_r2.py` | 4,212 | 2026-10-17 10:09:43 | `189764eebc91` | 噪声面 |
| 1960 | `.tmp/whitelist_backup_2026_10_17/docwriter_v45_verify_out.txt` | 2,031 | 2026-10-17 10:14:37 | `e5a0fdfbc914` | 噪声面 |
| 1961 | `.tmp/whitelist_backup_2026_10_17/docwriter_v46_card_raw.py` | 1,652 | 2026-10-17 10:28:16 | `b8754c12612b` | 噪声面 |
| 1962 | `.tmp/whitelist_backup_2026_10_17/docwriter_v46_card_raw.txt` | 26 | 2026-10-17 10:28:26 | `e31064337198` | 噪声面 |
| 1963 | `.tmp/whitelist_backup_2026_10_17/docwriter_v46_probe.py` | 8,174 | 2026-10-17 10:25:58 | `15d2a2cef38c` | 噪声面 |
| 1964 | `.tmp/whitelist_backup_2026_10_17/docwriter_v46_probe_out.txt` | 10,158 | 2026-10-17 10:26:08 | `45358bad9e37` | 噪声面 |
| 1965 | `.tmp/whitelist_backup_2026_10_17/docwriter_v46_timeshift_out.txt` | 708 | 2026-10-17 10:37:51 | `4623d2f470da` | 噪声面 |
| 1966 | `.tmp/whitelist_backup_2026_10_17/docwriter_v46_verify.py` | 6,883 | 2026-10-17 10:33:28 | `7d657b923cf3` | 噪声面 |
| 1967 | `.tmp/whitelist_backup_2026_10_17/docwriter_v46_verify_r2.py` | 3,940 | 2026-10-17 10:33:56 | `98878b701653` | 噪声面 |
| 1968 | `.tmp/whitelist_backup_2026_10_17/docwriter_v47_verify.py` | 1,220 | 2026-10-17 10:53:57 | `9383724baaa4` | 噪声面 |
| 1969 | `.tmp/whitelist_backup_2026_10_17/docwriter_v47_write1.py` | 62,466 | 2026-10-17 10:51:19 | `8fa8d72c3a69` | 噪声面 |
| 1970 | `.tmp/whitelist_backup_2026_10_17/docwriter_v47_write2.py` | 48,627 | 2026-10-17 10:53:02 | `1ee1ee14ac3e` | 噪声面 |
| 1971 | `.tmp/whitelist_backup_2026_10_17/docwriter_v48_norm.py` | 12,880 | 2026-10-17 11:11:16 | `e39ea2ab2756` | 噪声面 |
| 1972 | `.tmp/whitelist_backup_2026_10_17/docwriter_v48_probe.py` | 4,448 | 2026-10-17 11:06:47 | `8dfd0f40cdb5` | 噪声面 |
| 1973 | `.tmp/whitelist_backup_2026_10_17/docwriter_v48_probe_out.txt` | 4,169 | 2026-10-17 11:06:55 | `48b1c4a81ad4` | 噪声面 |
| 1974 | `.tmp/whitelist_backup_2026_10_17/docwriter_v49_norm.py` | 16,740 | 2026-10-17 11:23:11 | `d1b3481335eb` | 噪声面 |
| 1975 | `.tmp/whitelist_backup_2026_10_17/docwriter_v49_probe.py` | 4,806 | 2026-10-17 11:17:59 | `753b0ad48557` | 噪声面 |
| 1976 | `.tmp/whitelist_backup_2026_10_17/docwriter_v49_probe_out.txt` | 4,353 | 2026-10-17 11:18:12 | `c04bcaf87623` | 噪声面 |
| 1977 | `.tmp/whitelist_backup_2026_10_17/docwriter_verify_v44.py` | 4,692 | 2026-10-17 00:21:12 | `19cfb64700a1` | 噪声面 |
| 1978 | `.tmp/whitelist_backup_2026_10_17/docwriter_verify_v44_out.txt` | 2,371 | 2026-10-17 00:21:24 | `f3d33d095a8a` | 噪声面 |
| 1979 | `.tmp/whitelist_backup_2026_10_17/docwriter_verify_v45.py` | 3,780 | 2026-10-17 10:13:59 | `92230e228d83` | 噪声面 |
| 1980 | `.tmp/whitelist_backup_2026_10_17/docwriter_write_effect_v43.py` | 27,715 | 2026-10-16 23:51:17 | `01098529c399` | 噪声面 |
| 1981 | `.tmp/whitelist_backup_2026_10_17/docwriter_write_v42.py` | 66,543 | 2026-10-16 23:36:36 | `5cc438f6338d` | 噪声面 |
| 1982 | `.tmp/whitelist_backup_2026_10_17/docwriter_write_v43.py` | 33,607 | 2026-10-16 23:48:08 | `d5e6390b900d` | 噪声面 |
| 1983 | `.tmp/whitelist_backup_2026_10_17/docwriter_write_v44.py` | 84,551 | 2026-10-17 00:17:25 | `54812b76573b` | 噪声面 |
| 1984 | `.tmp/whitelist_backup_2026_10_17/docwriter_write_v45.py` | 61,168 | 2026-10-17 10:13:35 | `af3a22741b2f` | 噪声面 |
| 1985 | `.tmp/whitelist_backup_2026_10_17/dscan_01.json` | 195,396 | 2026-10-14 02:19:15 | `bab5d4a367af` | 噪声面 |
| 1986 | `.tmp/whitelist_backup_2026_10_17/dscan_01.py` | 2,865 | 2026-10-14 02:19:06 | `a58735d65c3c` | 噪声面 |
| 1987 | `.tmp/whitelist_backup_2026_10_17/dscan_02.py` | 5,078 | 2026-10-14 02:21:33 | `1f6ffd7e0f47` | 噪声面 |
| 1988 | `.tmp/whitelist_backup_2026_10_17/dscan_03.py` | 5,360 | 2026-10-14 02:22:29 | `35711329ad8f` | 噪声面 |
| 1989 | `.tmp/whitelist_backup_2026_10_17/dscan_04.py` | 2,302 | 2026-10-14 02:23:08 | `43e661f72888` | 噪声面 |
| 1990 | `.tmp/whitelist_backup_2026_10_17/dscan_05.py` | 6,207 | 2026-10-14 02:23:59 | `966d9ce0df2d` | 噪声面 |
| 1991 | `.tmp/whitelist_backup_2026_10_17/dscan_06.py` | 1,845 | 2026-10-14 02:24:18 | `7c059d996778` | 噪声面 |
| 1992 | `.tmp/whitelist_backup_2026_10_17/dscan_07.py` | 1,074 | 2026-10-14 02:24:43 | `26897ce01079` | 噪声面 |
| 1993 | `.tmp/whitelist_backup_2026_10_17/dscan_08.py` | 2,370 | 2026-10-14 02:25:13 | `fc3c78d3f0e5` | 噪声面 |
| 1994 | `.tmp/whitelist_backup_2026_10_17/dscan_classified.json` | 47,129 | 2026-10-14 02:21:38 | `458a2e06a2d3` | 噪声面 |
| 1995 | `.tmp/whitelist_backup_2026_10_17/dscan_classified.txt` | 11,199 | 2026-10-14 02:21:38 | `2945d458f5a6` | 噪声面 |
| 1996 | `.tmp/whitelist_backup_2026_10_17/dscan_copycmp.txt` | 687 | 2026-10-14 02:21:02 | `3af905a1f5c4` | 噪声面 |
| 1997 | `.tmp/whitelist_backup_2026_10_17/dscan_families.txt` | 3,535 | 2026-10-14 02:23:16 | `3bc5960fa2bf` | 噪声面 |
| 1998 | `.tmp/whitelist_backup_2026_10_17/dscan_matrix.json` | 273,930 | 2026-10-14 02:24:09 | `875f08dd0648` | 噪声面 |
| 1999 | `.tmp/whitelist_backup_2026_10_17/dscan_matrix.txt` | 1,452 | 2026-10-14 02:24:09 | `a8d3aa0287b6` | 噪声面 |
| 2000 | `.tmp/whitelist_backup_2026_10_17/dscan_repo_dump.txt` | 24,326 | 2026-10-14 02:20:10 | `06d5da0d55ed` | 噪声面 |
| 2001 | `.tmp/whitelist_backup_2026_10_17/dscan_stats.txt` | 2,712 | 2026-10-14 02:24:24 | `b35fb0ebd75d` | 噪声面 |
| 2002 | `.tmp/whitelist_backup_2026_10_17/dscan_sub_dump.txt` | 94,170 | 2026-10-14 02:20:35 | `8c3f99c0b128` | 噪声面 |
| 2003 | `.tmp/whitelist_backup_2026_10_17/dscan_tables.md` | 56,191 | 2026-10-14 02:25:19 | `0a96d4720449` | 噪声面 |
| 2004 | `.tmp/whitelist_backup_2026_10_17/dscan_write_01.py` | 23,330 | 2026-10-14 02:26:16 | `71cbf839d36b` | 噪声面 |
| 2005 | `.tmp/whitelist_backup_2026_10_17/dscan_xcheck.txt` | 3,196 | 2026-10-14 02:22:35 | `57dcd8344683` | 噪声面 |
| 2006 | `.tmp/whitelist_backup_2026_10_17/dw720_calc_2026_10_16.py` | 1,797 | 2026-10-16 11:40:35 | `5da6bf2d700a` | 噪声面 |
| 2007 | `.tmp/whitelist_backup_2026_10_17/dw720_probe_2026_10_16.py` | 1,450 | 2026-10-16 11:37:52 | `efdb4c877f3f` | 噪声面 |
| 2008 | `.tmp/whitelist_backup_2026_10_17/dw720_verify_2026_10_16.py` | 3,909 | 2026-10-16 11:42:24 | `c90f9a64c3d8` | 噪声面 |
| 2009 | `.tmp/whitelist_backup_2026_10_17/dw720_write_2026_10_16.py` | 29,681 | 2026-10-16 11:42:01 | `46e8be383b3c` | 噪声面 |
| 2010 | `.tmp/whitelist_backup_2026_10_17/ea_build.py` | 30,376 | 2026-10-13 21:21:46 | `8048ac40151e` | 噪声面 |
| 2011 | `.tmp/whitelist_backup_2026_10_17/ea_files.json` | 191,599 | 2026-10-13 21:11:53 | `48b76f2549f3` | 噪声面 |
| 2012 | `.tmp/whitelist_backup_2026_10_17/ea_p2.py` | 1,030 | 2026-10-13 21:16:56 | `64fb6201dca9` | 噪声面 |
| 2013 | `.tmp/whitelist_backup_2026_10_17/ea_scan1.py` | 1,005 | 2026-10-13 21:11:48 | `e21c9fca13d0` | 噪声面 |
| 2014 | `.tmp/whitelist_backup_2026_10_17/ea_sha12.json` | 289,347 | 2026-10-13 21:12:14 | `381dd57aaca4` | 噪声面 |
| 2015 | `.tmp/whitelist_backup_2026_10_17/erratum_glm_wholepack_body.md` | 24,905 | 2026-10-14 12:57:34 | `0291002f749e` | 噪声面 |
| 2016 | `.tmp/whitelist_backup_2026_10_17/evauditor_one_finish_write.py` | 46,211 | 2026-10-17 00:22:44 | `c24967f8114e` | 噪声面 |
| 2017 | `.tmp/whitelist_backup_2026_10_17/exp04_h_contrast_2026_10_10.py` | 14,333 | 2026-10-10 10:04:20 | `572f1b9c3927` | 噪声面 |
| 2018 | `.tmp/whitelist_backup_2026_10_17/f2_branch_fix_transform_2026_09_29.py` | 18,152 | 2026-09-29 22:53:30 | `0a970b156867` | 噪声面 |
| 2019 | `.tmp/whitelist_backup_2026_10_17/f2_branch_selftest_2026_09_29.py` | 7,377 | 2026-09-29 22:54:26 | `68a927174a2e` | 噪声面 |
| 2020 | `.tmp/whitelist_backup_2026_10_17/gate_check.py` | 648 | 2026-10-09 17:24:02 | `abe7fbdb394b` | 噪声面 |
| 2021 | `.tmp/whitelist_backup_2026_10_17/gate_check2.py` | 840 | 2026-10-09 17:24:17 | `7025ceceb766` | 噪声面 |
| 2022 | `.tmp/whitelist_backup_2026_10_17/ge01_eps_grid_exec2_2026_10_16.json` | 53,903 | 2026-10-16 16:52:19 | `af1fcc0e8852` | 噪声面 |
| 2023 | `.tmp/whitelist_backup_2026_10_17/ge01_eps_grid_exec2_2026_10_16.py` | 11,452 | 2026-10-16 16:51:17 | `9ef16d1b8525` | 噪声面 |
| 2024 | `.tmp/whitelist_backup_2026_10_17/ge01_eps_grid_exec3_2026_10_16.py` | 3,580 | 2026-10-16 16:53:39 | `5225d7800544` | 噪声面 |
| 2025 | `.tmp/whitelist_backup_2026_10_17/ge01_eps_grid_exec_2026_10_16.json` | 62,749 | 2026-10-16 16:48:31 | `45b233594ee9` | 噪声面 |
| 2026 | `.tmp/whitelist_backup_2026_10_17/ge01_eps_grid_exec_2026_10_16.py` | 11,018 | 2026-10-16 16:48:21 | `ab5e001cb63b` | 噪声面 |
| 2027 | `.tmp/whitelist_backup_2026_10_17/ge01_eps_grid_verify_2026_10_16.py` | 3,016 | 2026-10-16 16:57:00 | `4ff9d5a95dcf` | 噪声面 |
| 2028 | `.tmp/whitelist_backup_2026_10_17/ge01_full_1494_adjudicate_2026_10_16.py` | 14,293 | 2026-10-16 22:52:31 | `8108e4c883ad` | 噪声面 |
| 2029 | `.tmp/whitelist_backup_2026_10_17/ge01_full_1494_collect_2026_10_16.py` | 28,322 | 2026-10-16 22:39:35 | `039ebfca39b7` | 噪声面 |
| 2030 | `.tmp/whitelist_backup_2026_10_17/ge01_full_1494_exec_r1_write_2026_10_16.py` | 43,129 | 2026-10-16 23:01:50 | `9e9e402893ef` | 噪声面 |
| 2031 | `.tmp/whitelist_backup_2026_10_17/ge01_full_1494_freeze_2026_10_16.json` | 7,479 | 2026-10-16 22:38:20 | `8494390a274a` | 噪声面 |
| 2032 | `.tmp/whitelist_backup_2026_10_17/ge01_full_1494_freeze_write_2026_10_16.py` | 23,781 | 2026-10-16 22:38:09 | `b89e0432ab97` | 噪声面 |
| 2033 | `.tmp/whitelist_backup_2026_10_17/ge01_full_1494_llm_calls_2026_10_16.jsonl` | 235,298 | 2026-10-16 23:32:19 | `e922d168ab60` | 噪声面 |
| 2034 | `.tmp/whitelist_backup_2026_10_17/ge01_full_1494_measurement_2026_10_16.json` | 547,703 | 2026-10-16 23:00:18 | `4054d1393b84` | 噪声面 |
| 2035 | `.tmp/whitelist_backup_2026_10_17/ge01_full_1494_measurement_resume32_2026_10_16.json` | 570,852 | 2026-10-16 23:35:09 | `7ccc5f9e8b2c` | 噪声面 |
| 2036 | `.tmp/whitelist_backup_2026_10_17/ge01_full_1494_precheck_2026_10_16.json` | 9,432 | 2026-10-16 22:17:14 | `bd6dd07ad1c3` | 噪声面 |
| 2037 | `.tmp/whitelist_backup_2026_10_17/ge01_full_1494_precheck_2026_10_16.py` | 10,700 | 2026-10-16 22:16:48 | `cc34ab8552f9` | 噪声面 |
| 2038 | `.tmp/whitelist_backup_2026_10_17/ge01_full_1494_probe_2026_10_16.py` | 3,199 | 2026-10-16 22:38:35 | `a38499e4d4a9` | 噪声面 |
| 2039 | `.tmp/whitelist_backup_2026_10_17/ge01_full_1494_readout_2026_10_16.py` | 22,920 | 2026-10-16 22:59:58 | `59ed27635c6e` | 噪声面 |
| 2040 | `.tmp/whitelist_backup_2026_10_17/ge01_full_1494_resume32_collect_2026_10_16.py` | 14,609 | 2026-10-16 23:31:45 | `9496620e32b2` | 噪声面 |
| 2041 | `.tmp/whitelist_backup_2026_10_17/ge01_full_1494_resume32_precheck_2026_10_16.log` | 1,761 | 2026-10-16 23:30:47 | `ada7f41b8cb2` | 噪声面 |
| 2042 | `.tmp/whitelist_backup_2026_10_17/ge01_full_1494_resume32_precheck_2026_10_16.py` | 6,122 | 2026-10-16 23:30:35 | `463532446b61` | 噪声面 |
| 2043 | `.tmp/whitelist_backup_2026_10_17/ge01_full_1494_resume32_probe_2026_10_16.json` | 338 | 2026-10-16 23:32:01 | `579a7f8b6fe3` | 噪声面 |
| 2044 | `.tmp/whitelist_backup_2026_10_17/ge01_full_1494_resume32_readout_2026_10_16.py` | 29,430 | 2026-10-16 23:34:47 | `de50589bd6c6` | 噪声面 |
| 2045 | `.tmp/whitelist_backup_2026_10_17/ge01_full_1494_resume32_run_2026_10_16.log` | 1,033 | 2026-10-16 23:32:19 | `f655e7d9e3e0` | 噪声面 |
| 2046 | `.tmp/whitelist_backup_2026_10_17/ge01_full_1494_resume32_stage_2026_10_16.json` | 7,574 | 2026-10-16 23:32:19 | `25d95a22bbb1` | 噪声面 |
| 2047 | `.tmp/whitelist_backup_2026_10_17/ge01_full_1494_run_2026_10_16.log` | 14,810 | 2026-10-16 22:58:23 | `3e85eac1bf6a` | 噪声面 |
| 2048 | `.tmp/whitelist_backup_2026_10_17/ge01_gate_index.py` | 3,095 | 2026-10-17 11:30:52 | `fc4ed5e7dea0` | 噪声面 |
| 2049 | `.tmp/whitelist_backup_2026_10_17/ge01_gate_measure.py` | 4,068 | 2026-10-17 11:36:36 | `c2cdebcb0bfc` | 噪声面 |
| 2050 | `.tmp/whitelist_backup_2026_10_17/ge01_gate_probe.py` | 3,196 | 2026-10-17 11:32:40 | `82bf49985799` | 噪声面 |
| 2051 | `.tmp/whitelist_backup_2026_10_17/ge01_gate_scan.py` | 1,955 | 2026-10-17 11:33:40 | `5f6212d13cb5` | 噪声面 |
| 2052 | `.tmp/whitelist_backup_2026_10_17/ge01_gate_write.py` | 82,875 | 2026-10-17 11:39:58 | `a661b2c7e5f0` | 噪声面 |
| 2053 | `.tmp/whitelist_backup_2026_10_17/ge01_measure_list.json` | 2,435 | 2026-10-17 11:41:17 | `2eb41639edf4` | 噪声面 |
| 2054 | `.tmp/whitelist_backup_2026_10_17/ge01_results_sha12.json` | 192,203 | 2026-10-17 11:31:03 | `97fb1089de90` | 噪声面 |
| 2055 | `.tmp/whitelist_backup_2026_10_17/ge01_s3_keyscan_2026_10_16.py` | 1,730 | 2026-10-16 20:41:34 | `5f8a18033a99` | 噪声面 |
| 2056 | `.tmp/whitelist_backup_2026_10_17/ge01_s3_vadj_recheck_2026_10_16.py` | 13,088 | 2026-10-16 20:40:00 | `91d3e1d91b58` | 噪声面 |
| 2057 | `.tmp/whitelist_backup_2026_10_17/ge01_s3b_keyscan_2026_10_16.py` | 2,052 | 2026-10-16 21:21:34 | `b7743ec5a7ab` | 噪声面 |
| 2058 | `.tmp/whitelist_backup_2026_10_17/ge01_s3b_v_exec_2026_10_16.py` | 6,410 | 2026-10-16 21:04:06 | `0df5d957a911` | 噪声面 |
| 2059 | `.tmp/whitelist_backup_2026_10_17/ge01_s3b_v_exec_r1_2026_10_16.py` | 15,257 | 2026-10-16 21:17:43 | `4f525232efe4` | 噪声面 |
| 2060 | `.tmp/whitelist_backup_2026_10_17/ge01_s3b_v_exec_r1_readings_2026_10_16.json` | 25,489 | 2026-10-16 21:18:00 | `1ec7c258c637` | 噪声面 |
| 2061 | `.tmp/whitelist_backup_2026_10_17/ge01_s3b_v_exec_r1_supp_2026_10_16.py` | 5,199 | 2026-10-16 21:18:24 | `0646da5ccbe5` | 噪声面 |
| 2062 | `.tmp/whitelist_backup_2026_10_17/ge01_s3b_v_exec_r1_write_2026_10_16.py` | 56,062 | 2026-10-16 21:23:10 | `359b768e7dc0` | 噪声面 |
| 2063 | `.tmp/whitelist_backup_2026_10_17/ge02_build.py` | 24,774 | 2026-10-16 19:56:22 | `a10c57adf6b5` | 噪声面 |
| 2064 | `.tmp/whitelist_backup_2026_10_17/ge02_recompute.py` | 1,347 | 2026-10-16 19:53:23 | `811d4a138788` | 噪声面 |
| 2065 | `.tmp/whitelist_backup_2026_10_17/gen_supp3.py` | 15,813 | 2026-10-10 01:11:45 | `eb53c9ce140c` | 噪声面 |
| 2066 | `.tmp/whitelist_backup_2026_10_17/gen_v35_uactive_2026_10_16.py` | 43,518 | 2026-10-16 21:17:03 | `628c99636f10` | 噪声面 |
| 2067 | `.tmp/whitelist_backup_2026_10_17/h_src.py` | 727 | 2026-10-15 12:56:44 | `a4b8970b8b1f` | 噪声面 |
| 2068 | `.tmp/whitelist_backup_2026_10_17/harness.py` | 687 | 2026-10-16 10:57:43 | `56e02c4878f4` | 噪声面 |
| 2069 | `.tmp/whitelist_backup_2026_10_17/k_v3df_0_1_four_readings_2026_10_09.py` | 50,232 | 2026-10-09 11:24:00 | `2e990644cc8d` | 噪声面 |
| 2070 | `.tmp/whitelist_backup_2026_10_17/kd14_absorption_probe.py` | 1,358 | 2026-10-16 22:17:54 | `915c968f2d04` | 噪声面 |
| 2071 | `.tmp/whitelist_backup_2026_10_17/kd14_carrier_probe.py` | 1,206 | 2026-10-16 22:17:00 | `758033c2a76b` | 噪声面 |
| 2072 | `.tmp/whitelist_backup_2026_10_17/kd14_m4_corrected.py` | 932 | 2026-10-16 22:18:11 | `50c1c7d85616` | 噪声面 |
| 2073 | `.tmp/whitelist_backup_2026_10_17/klm41_2_bootstrap_ci_2026_10_16.json` | 12,373 | 2026-10-16 11:45:53 | `be99abcba9bf` | 噪声面 |
| 2074 | `.tmp/whitelist_backup_2026_10_17/klm41_2_caliber_decl_2026_10_16.json` | 4,757 | 2026-10-16 11:40:55 | `6f0721d20c06` | 噪声面 |
| 2075 | `.tmp/whitelist_backup_2026_10_17/klm41_2_caliber_decl_2026_10_16.py` | 10,466 | 2026-10-16 11:40:46 | `d9754474ad9a` | 噪声面 |
| 2076 | `.tmp/whitelist_backup_2026_10_17/klm41_2_compute_ci_2026_10_16.py` | 14,398 | 2026-10-16 11:44:37 | `fb38b90df08f` | 噪声面 |
| 2077 | `.tmp/whitelist_backup_2026_10_17/klm41_2_freeze_2026_10_16.json` | 3,211 | 2026-10-16 11:40:55 | `2a4453d9610b` | 噪声面 |
| 2078 | `.tmp/whitelist_backup_2026_10_17/klm41_2_stratified_ci_2026_10_16.json` | 18,820 | 2026-10-16 11:48:56 | `67ae4f540e47` | 噪声面 |
| 2079 | `.tmp/whitelist_backup_2026_10_17/klm41_2_stratified_ci_2026_10_16.py` | 8,819 | 2026-10-16 11:47:22 | `f29526bccea3` | 噪声面 |
| 2080 | `.tmp/whitelist_backup_2026_10_17/klm41_2_verify_2026_10_16.json` | 2,906 | 2026-10-16 11:46:54 | `5ded5068566b` | 噪声面 |
| 2081 | `.tmp/whitelist_backup_2026_10_17/klm41_2_verify_2026_10_16.py` | 10,976 | 2026-10-16 11:45:08 | `af0f38f33222` | 噪声面 |
| 2082 | `.tmp/whitelist_backup_2026_10_17/klm41_2_write_doc_2026_10_16.py` | 48,391 | 2026-10-16 11:55:01 | `902dcf78f2b8` | 噪声面 |
| 2083 | `.tmp/whitelist_backup_2026_10_17/klm41_3_ts_caliber_decl_2026_10_16.json` | 3,255 | 2026-10-16 19:30:34 | `96456529a485` | 噪声面 |
| 2084 | `.tmp/whitelist_backup_2026_10_17/klm41_3_ts_collect_2026_10_16.py` | 23,196 | 2026-10-16 19:31:16 | `a28c4ba40940` | 噪声面 |
| 2085 | `.tmp/whitelist_backup_2026_10_17/klm41_3_ts_freeze_2026_10_16.json` | 2,235 | 2026-10-16 19:30:34 | `25c021d29b1b` | 噪声面 |
| 2086 | `.tmp/whitelist_backup_2026_10_17/klm41_3_ts_llm_calls_2026_10_16.jsonl` | 123,255 | 2026-10-16 19:38:58 | `595699b7ec44` | 噪声面 |
| 2087 | `.tmp/whitelist_backup_2026_10_17/klm41_3_ts_measurement_2026_10_16.json` | 252,951 | 2026-10-16 19:38:58 | `211a49ca9941` | 噪声面 |
| 2088 | `.tmp/whitelist_backup_2026_10_17/klm41_3_ts_preflight_2026_10_16.json` | 6,349 | 2026-10-16 19:30:07 | `d1fe0a6889be` | 噪声面 |
| 2089 | `.tmp/whitelist_backup_2026_10_17/klm41_3_ts_preflight_2026_10_16.py` | 6,228 | 2026-10-16 19:29:59 | `c787c6d4e361` | 噪声面 |
| 2090 | `.tmp/whitelist_backup_2026_10_17/klm41_3_ts_tables_2026_10_16.md` | 11,297 | 2026-10-16 19:40:18 | `54213bffc216` | 噪声面 |
| 2091 | `.tmp/whitelist_backup_2026_10_17/klm41_3_ts_verify_2026_10_16.json` | 5,848 | 2026-10-16 19:39:52 | `8cf7bb595870` | 噪声面 |
| 2092 | `.tmp/whitelist_backup_2026_10_17/kro_extract.py` | 802 | 2026-10-09 17:22:02 | `b5731abae41f` | 噪声面 |
| 2093 | `.tmp/whitelist_backup_2026_10_17/m08_enum_v2_2026_10_16.json` | 12,255 | 2026-10-16 16:09:19 | `c45cfc3ddc8d` | 噪声面 |
| 2094 | `.tmp/whitelist_backup_2026_10_17/m08_r1_amend2_2026_10_16.json` | 1,296 | 2026-10-16 16:27:40 | `21ad2e7acd0b` | 噪声面 |
| 2095 | `.tmp/whitelist_backup_2026_10_17/m08_r1_amend3_2026_10_16.json` | 3,034 | 2026-10-16 16:28:16 | `d77931c6d7a5` | 噪声面 |
| 2096 | `.tmp/whitelist_backup_2026_10_17/m08_r1_amend_2026_10_16.json` | 1,204 | 2026-10-16 16:27:06 | `3c982068b276` | 噪声面 |
| 2097 | `.tmp/whitelist_backup_2026_10_17/m08_r1_enum_2026_10_16.json` | 13,253 | 2026-10-16 16:19:00 | `361f67e37092` | 噪声面 |
| 2098 | `.tmp/whitelist_backup_2026_10_17/m08_r1_enum_2026_10_16.py` | 16,318 | 2026-10-16 16:18:16 | `884b7161e053` | 噪声面 |
| 2099 | `.tmp/whitelist_backup_2026_10_17/m08_r1_freeze_2026_10_16.json` | 7,655 | 2026-10-16 16:17:28 | `1a40d8046fdc` | 噪声面 |
| 2100 | `.tmp/whitelist_backup_2026_10_17/m08_r1_freeze_2026_10_16.py` | 9,207 | 2026-10-16 16:17:22 | `8c6b5e0d3ebb` | 噪声面 |
| 2101 | `.tmp/whitelist_backup_2026_10_17/m08_r1_llm_arm_2026_10_16.json` | 11,335 | 2026-10-16 16:21:18 | `19d93d77b46e` | 噪声面 |
| 2102 | `.tmp/whitelist_backup_2026_10_17/m08_r1_llm_arm_2026_10_16.py` | 9,852 | 2026-10-16 16:20:53 | `987820693d06` | 噪声面 |
| 2103 | `.tmp/whitelist_backup_2026_10_17/m08_r1_llm_calls_2026_10_16.jsonl` | 8,271 | 2026-10-16 16:21:18 | `0e8c9664b06d` | 噪声面 |
| 2104 | `.tmp/whitelist_backup_2026_10_17/m08_r1_llm_calls_partial_pass1_2026_10_16.jsonl` | 8,230 | 2026-10-16 16:20:34 | `d30121ed7ebf` | 噪声面 |
| 2105 | `.tmp/whitelist_backup_2026_10_17/m08_r1_llm_probe2_2026_10_16.json` | 1,805 | 2026-10-16 16:21:51 | `d2a8510b1322` | 噪声面 |
| 2106 | `.tmp/whitelist_backup_2026_10_17/m08_r1_llm_probe2_2026_10_16.py` | 2,359 | 2026-10-16 16:21:41 | `190668eae9da` | 噪声面 |
| 2107 | `.tmp/whitelist_backup_2026_10_17/m08_r1_probe_2026_10_16.json` | 3,752 | 2026-10-16 16:19:34 | `c2ba80ba548b` | 噪声面 |
| 2108 | `.tmp/whitelist_backup_2026_10_17/m08_r1_probe_2026_10_16.py` | 4,739 | 2026-10-16 16:19:28 | `63f0234a7c89` | 噪声面 |
| 2109 | `.tmp/whitelist_backup_2026_10_17/m08_r1_recompute_2026_10_16.json` | 2,072 | 2026-10-16 16:22:25 | `59ddca239f67` | 噪声面 |
| 2110 | `.tmp/whitelist_backup_2026_10_17/m08_r1_recompute_2026_10_16.py` | 6,998 | 2026-10-16 16:22:14 | `305ee668612c` | 噪声面 |
| 2111 | `.tmp/whitelist_backup_2026_10_17/m08_r1_srcsha_2026_10_16.json` | 8,851 | 2026-10-16 16:22:52 | `2074096a45e2` | 噪声面 |
| 2112 | `.tmp/whitelist_backup_2026_10_17/m08_r1_srcsha_2026_10_16.py` | 3,697 | 2026-10-16 16:22:46 | `96ac0e7c23f6` | 噪声面 |
| 2113 | `.tmp/whitelist_backup_2026_10_17/m08_r1_write_2026_10_16.py` | 58,218 | 2026-10-16 16:26:50 | `0a5d9e9f18d9` | 噪声面 |
| 2114 | `.tmp/whitelist_backup_2026_10_17/m2_docwriter_write.py` | 23,214 | 2026-10-14 10:23:50 | `9842ca168062` | 噪声面 |
| 2115 | `.tmp/whitelist_backup_2026_10_17/m2_write.py` | 24,159 | 2026-10-14 03:20:18 | `133387a21ec6` | 噪声面 |
| 2116 | `.tmp/whitelist_backup_2026_10_17/m2verdict_downstream.py` | 2,240 | 2026-10-14 11:50:05 | `93c831a7fc0f` | 噪声面 |
| 2117 | `.tmp/whitelist_backup_2026_10_17/m2verdict_meta.py` | 1,223 | 2026-10-14 11:49:30 | `c89599655807` | 噪声面 |
| 2118 | `.tmp/whitelist_backup_2026_10_17/m2verdict_probe.py` | 4,493 | 2026-10-14 11:46:21 | `3a401ef46a00` | 噪声面 |
| 2119 | `.tmp/whitelist_backup_2026_10_17/m2verdict_ruling.py` | 1,125 | 2026-10-14 11:51:41 | `841949136e81` | 噪声面 |
| 2120 | `.tmp/whitelist_backup_2026_10_17/m41_dual_readout.py` | 6,471 | 2026-10-15 09:30:33 | `45f3d856efd8` | 噪声面 |
| 2121 | `.tmp/whitelist_backup_2026_10_17/m41_endpoint_probe.py` | 1,520 | 2026-10-15 09:29:37 | `f9811a6eceba` | 噪声面 |
| 2122 | `.tmp/whitelist_backup_2026_10_17/m41_fix_diag.json` | 1,034 | 2026-10-15 10:20:20 | `2e34378d0d2c` | 噪声面 |
| 2123 | `.tmp/whitelist_backup_2026_10_17/m41_keyprobe.py` | 892 | 2026-10-15 00:12:19 | `10e08b837e05` | 噪声面 |
| 2124 | `.tmp/whitelist_backup_2026_10_17/m41_keysurvey.py` | 1,296 | 2026-10-15 00:12:32 | `795daa633133` | 噪声面 |
| 2125 | `.tmp/whitelist_backup_2026_10_17/m41_llm_calls.jsonl` | 642 | 2026-10-15 09:26:55 | `a1651f3d9303` | 噪声面 |
| 2126 | `.tmp/whitelist_backup_2026_10_17/m41_mech_arms.json` | 1,252 | 2026-10-15 09:34:07 | `be1a8fce8660` | 噪声面 |
| 2127 | `.tmp/whitelist_backup_2026_10_17/m41_mech_arms.py` | 3,731 | 2026-10-15 09:34:02 | `a92812ceae61` | 噪声面 |
| 2128 | `.tmp/whitelist_backup_2026_10_17/m41_r15_collect_readout.py` | 13,324 | 2026-10-15 10:21:47 | `d4e882337b80` | 噪声面 |
| 2129 | `.tmp/whitelist_backup_2026_10_17/m41_r15_llm_calls.jsonl` | 3,467 | 2026-10-15 10:22:52 | `7d0dbb58d53a` | 噪声面 |
| 2130 | `.tmp/whitelist_backup_2026_10_17/m41_r15_readout.json` | 14,261 | 2026-10-15 10:22:52 | `33a4720bcafd` | 噪声面 |
| 2131 | `.tmp/whitelist_backup_2026_10_17/m41_r15_verify.py` | 4,235 | 2026-10-15 10:23:40 | `f72545f959b4` | 噪声面 |
| 2132 | `.tmp/whitelist_backup_2026_10_17/m41_rerun_llm_calls.jsonl` | 24,253 | 2026-10-15 10:07:00 | `19fa12f4e053` | 噪声面 |
| 2133 | `.tmp/whitelist_backup_2026_10_17/m41_selfcheck.json` | 318 | 2026-10-15 09:39:44 | `d18a46a884f2` | 噪声面 |
| 2134 | `.tmp/whitelist_backup_2026_10_17/m41_selfcheck.py` | 1,291 | 2026-10-15 09:13:31 | `5f066493fdbc` | 噪声面 |
| 2135 | `.tmp/whitelist_backup_2026_10_17/m41_src_shas.py` | 1,138 | 2026-10-15 09:30:48 | `47a192be190a` | 噪声面 |
| 2136 | `.tmp/whitelist_backup_2026_10_17/m41_src_shas.txt` | 420 | 2026-10-15 09:39:53 | `b2c58664cd51` | 噪声面 |
| 2137 | `.tmp/whitelist_backup_2026_10_17/material_expansion_kill_freeze_2026_10_16.json` | 15,187 | 2026-10-16 15:33:54 | `03a628456f0b` | 噪声面 |
| 2138 | `.tmp/whitelist_backup_2026_10_17/me_llm_calls_2026_10_16.jsonl` | 21,339 | 2026-10-16 15:38:54 | `fbdedcb0ef48` | 噪声面 |
| 2139 | `.tmp/whitelist_backup_2026_10_17/me_t4_resolve_2026_10_16.py` | 9,507 | 2026-10-16 15:46:44 | `71b0e9c8da44` | 噪声面 |
| 2140 | `.tmp/whitelist_backup_2026_10_17/mq04_budget_calc_2026_10_15.json` | 5,436 | 2026-10-15 15:47:49 | `e8a5b2533ac2` | 噪声面 |
| 2141 | `.tmp/whitelist_backup_2026_10_17/mq04_budget_calc_2026_10_15.py` | 6,803 | 2026-10-15 15:47:43 | `e5e4fcfd5e29` | 噪声面 |
| 2142 | `.tmp/whitelist_backup_2026_10_17/mq04_nt_llm_calls_2026_10_15.jsonl` | 24,320 | 2026-10-15 15:43:24 | `734af9135441` | 噪声面 |
| 2143 | `.tmp/whitelist_backup_2026_10_17/mq04_nt_measure_2026_10_15.py` | 14,503 | 2026-10-15 15:39:58 | `5e55c0ff27f8` | 噪声面 |
| 2144 | `.tmp/whitelist_backup_2026_10_17/mq04_nt_measurement_2026_10_15.json` | 6,047 | 2026-10-15 15:43:24 | `956d35f25c70` | 噪声面 |
| 2145 | `.tmp/whitelist_backup_2026_10_17/mq04_write_doc_2026_10_15.py` | 26,377 | 2026-10-15 15:49:02 | `7fb013086741` | 噪声面 |
| 2146 | `.tmp/whitelist_backup_2026_10_17/pa_block.py` | 345 | 2026-10-09 17:22:28 | `19ac8c59439b` | 噪声面 |
| 2147 | `.tmp/whitelist_backup_2026_10_17/pk33q_body.md` | 26,976 | 2026-10-15 17:15:37 | `20ad5b45ba2c` | 噪声面 |
| 2148 | `.tmp/whitelist_backup_2026_10_17/pk_body1.md` | 26,832 | 2026-10-15 09:09:17 | `b32ca40ec103` | 噪声面 |
| 2149 | `.tmp/whitelist_backup_2026_10_17/pk_body2.md` | 32,568 | 2026-10-15 09:10:46 | `75a818b2654f` | 噪声面 |
| 2150 | `.tmp/whitelist_backup_2026_10_17/pk_lockv2_degeneracy_2026_10_15.json` | 2,583 | 2026-10-15 16:16:10 | `1106bb7d5c56` | 噪声面 |
| 2151 | `.tmp/whitelist_backup_2026_10_17/pk_lockv2_degeneracy_2026_10_15.py` | 2,425 | 2026-10-15 16:16:03 | `e8067070c849` | 噪声面 |
| 2152 | `.tmp/whitelist_backup_2026_10_17/pk_lockv2_verify_2026_10_15.json` | 4,691 | 2026-10-15 16:15:53 | `34cf77faf825` | 噪声面 |
| 2153 | `.tmp/whitelist_backup_2026_10_17/pk_lockv2_verify_2026_10_15.py` | 3,784 | 2026-10-15 16:15:47 | `67795949087d` | 噪声面 |
| 2154 | `.tmp/whitelist_backup_2026_10_17/pk_lockv2_write_2026_10_15.py` | 33,749 | 2026-10-15 16:17:43 | `440affa3e102` | 噪声面 |
| 2155 | `.tmp/whitelist_backup_2026_10_17/pk_measure_01.py` | 1,510 | 2026-10-14 02:10:55 | `76af3ed43f2c` | 噪声面 |
| 2156 | `.tmp/whitelist_backup_2026_10_17/pk_probe2_2026_10_16.py` | 1,140 | 2026-10-16 10:55:45 | `632e6dca295d` | 噪声面 |
| 2157 | `.tmp/whitelist_backup_2026_10_17/pk_probe_2026_10_16.py` | 878 | 2026-10-16 10:54:43 | `809cf2066d48` | 噪声面 |
| 2158 | `.tmp/whitelist_backup_2026_10_17/pk_supp500_calc_2026_10_16.py` | 3,079 | 2026-10-16 10:57:34 | `5325e2e6bc00` | 噪声面 |
| 2159 | `.tmp/whitelist_backup_2026_10_17/pk_t5lock_body_2026_10_15.md` | 46,621 | 2026-10-15 16:53:29 | `404d4fbeef40` | 噪声面 |
| 2160 | `.tmp/whitelist_backup_2026_10_17/pk_t5lock_verify_2026_10_15.json` | 4,931 | 2026-10-15 16:49:54 | `0b9c36f612da` | 噪声面 |
| 2161 | `.tmp/whitelist_backup_2026_10_17/pk_t5lock_verify_2026_10_15.py` | 5,559 | 2026-10-15 16:49:50 | `3f21b53443b4` | 噪声面 |
| 2162 | `.tmp/whitelist_backup_2026_10_17/pk_t5lock_write_2026_10_15.py` | 3,938 | 2026-10-15 16:53:42 | `e80c26269446` | 噪声面 |
| 2163 | `.tmp/whitelist_backup_2026_10_17/pk_write_budget210_2026_10_16.py` | 20,931 | 2026-10-16 11:04:19 | `0c65c2e859f9` | 噪声面 |
| 2164 | `.tmp/whitelist_backup_2026_10_17/pk_write_design_review_2026_10_16.py` | 47,618 | 2026-10-16 11:02:43 | `439fa0ae048d` | 噪声面 |
| 2165 | `.tmp/whitelist_backup_2026_10_17/pool_search.py` | 2,127 | 2026-10-10 13:49:20 | `3245af3f3bbb` | 噪声面 |
| 2166 | `.tmp/whitelist_backup_2026_10_17/prep.py` | 4,091 | 2026-10-10 13:51:46 | `e401c8e50f93` | 噪声面 |
| 2167 | `.tmp/whitelist_backup_2026_10_17/probe3_out.txt` | 41,096 | 2026-10-13 23:35:56 | `d2cef7709033` | 噪声面 |
| 2168 | `.tmp/whitelist_backup_2026_10_17/r3m2_disp_write.py` | 18,437 | 2026-10-14 11:37:24 | `988c2fee3ea2` | 噪声面 |
| 2169 | `.tmp/whitelist_backup_2026_10_17/r461_layers.json` | 102,003 | 2026-10-14 02:35:00 | `fee35e10c208` | 噪声面 |
| 2170 | `.tmp/whitelist_backup_2026_10_17/r461_write_01.py` | 19,104 | 2026-10-14 02:48:27 | `9030a50780da` | 噪声面 |
| 2171 | `.tmp/whitelist_backup_2026_10_17/recheck2.py` | 2,282 | 2026-09-30 21:43:11 | `85c4cfa3eb46` | 噪声面 |
| 2172 | `.tmp/whitelist_backup_2026_10_17/ref_exp_harness_OLD_2026_10_15.py` | 13,342 | 2026-10-15 17:19:10 | `7957bac14455` | 噪声面 |
| 2173 | `.tmp/whitelist_backup_2026_10_17/run_steps.py` | 2,756 | 2026-10-10 13:45:15 | `019f8405d4cf` | 噪声面 |
| 2174 | `.tmp/whitelist_backup_2026_10_17/s3_recompute_pass4.py` | 4,439 | 2026-10-01 08:54:56 | `6f210893fcce` | 噪声面 |
| 2175 | `.tmp/whitelist_backup_2026_10_17/s4_regen_runner.py` | 13,040 | 2026-10-10 13:43:59 | `70467364bdb1` | 噪声面 |
| 2176 | `.tmp/whitelist_backup_2026_10_17/scan_classify_five_terminal_2026_10_10.py` | 7,603 | 2026-10-10 12:23:20 | `0b9b59083534` | 噪声面 |
| 2177 | `.tmp/whitelist_backup_2026_10_17/scan_domain_five_terminal_2026_10_10.py` | 2,243 | 2026-10-10 12:21:53 | `732489dc3dbd` | 噪声面 |
| 2178 | `.tmp/whitelist_backup_2026_10_17/scan_supplement_five_terminal_2026_10_10.py` | 6,010 | 2026-10-10 12:22:25 | `7c0a6d022104` | 噪声面 |
| 2179 | `.tmp/whitelist_backup_2026_10_17/scope_scan.py` | 3,380 | 2026-10-10 13:48:55 | `07349acfe90f` | 噪声面 |
| 2180 | `.tmp/whitelist_backup_2026_10_17/singlevar.py` | 1,515 | 2026-10-10 13:50:16 | `f0bba43af3e5` | 噪声面 |
| 2181 | `.tmp/whitelist_backup_2026_10_17/t2_path_b_kill_freeze_2026_10_16.json` | 14,896 | 2026-10-16 16:13:35 | `3f3272100f62` | 噪声面 |
| 2182 | `.tmp/whitelist_backup_2026_10_17/t2b_census_2026_10_16.py` | 3,041 | 2026-10-16 16:21:25 | `71f99afb9199` | 噪声面 |
| 2183 | `.tmp/whitelist_backup_2026_10_17/t2b_derive_2026_10_16.py` | 7,964 | 2026-10-16 16:20:52 | `324165eb0c7d` | 噪声面 |
| 2184 | `.tmp/whitelist_backup_2026_10_17/t2b_fetch_facts_2026_10_16.py` | 5,774 | 2026-10-16 16:10:08 | `0941558d024e` | 噪声面 |
| 2185 | `.tmp/whitelist_backup_2026_10_17/t2b_freeze_2026_10_16.py` | 13,908 | 2026-10-16 16:06:21 | `575b796a2e6f` | 噪声面 |
| 2186 | `.tmp/whitelist_backup_2026_10_17/t2b_freeze_v2_2026_10_16.py` | 17,044 | 2026-10-16 16:13:29 | `02a261b12f7b` | 噪声面 |
| 2187 | `.tmp/whitelist_backup_2026_10_17/t2b_harness_pre_change_snapshot_2026_10_16.py` | 36,217 | 2026-10-16 16:16:22 | `d5c8d676bb5b` | 噪声面 |
| 2188 | `.tmp/whitelist_backup_2026_10_17/t2b_impl_audit_2026_10_16.py` | 4,856 | 2026-10-16 16:15:06 | `e02a343246bd` | 噪声面 |
| 2189 | `.tmp/whitelist_backup_2026_10_17/t2b_inspect_facts_2026_10_16.py` | 1,732 | 2026-10-16 16:00:37 | `de3c879e39f1` | 噪声面 |
| 2190 | `.tmp/whitelist_backup_2026_10_17/t2b_llm_calls_2026_10_16.jsonl` | 5,317 | 2026-10-16 16:19:18 | `a54a3af46ba2` | 噪声面 |
| 2191 | `.tmp/whitelist_backup_2026_10_17/t2b_measure_2026_10_16.py` | 15,547 | 2026-10-16 16:18:26 | `bd377372927c` | 噪声面 |
| 2192 | `.tmp/whitelist_backup_2026_10_17/t2b_measurement_2026_10_16.json` | 25,796 | 2026-10-16 16:19:18 | `fe5db6defb09` | 噪声面 |
| 2193 | `.tmp/whitelist_backup_2026_10_17/t2b_patch_harness_2026_10_16.py` | 7,065 | 2026-10-16 16:16:02 | `bac4775c5c44` | 噪声面 |
| 2194 | `.tmp/whitelist_backup_2026_10_17/t2b_strategyqa_train_snapshot_2026_10_16.json` | 4,281,955 | 2026-10-16 16:07:40 | `728e28b7d6bd` | 噪声面 |
| 2195 | `.tmp/whitelist_backup_2026_10_17/t3_baseline_procedure_probe.py` | 2,292 | 2026-10-15 17:19:37 | `b4c2a5e68dfa` | 噪声面 |
| 2196 | `.tmp/whitelist_backup_2026_10_17/t3_baseline_procedure_probe_2026_10_15.json` | 1,332 | 2026-10-15 17:20:00 | `7ac600d45dcc` | 噪声面 |
| 2197 | `.tmp/whitelist_backup_2026_10_17/t3_freeze_2026_10_15.json` | 7,436 | 2026-10-15 17:17:18 | `313f091718cc` | 噪声面 |
| 2198 | `.tmp/whitelist_backup_2026_10_17/t3_harness_diff_2026_10_15.diff` | 3,463 | 2026-10-15 17:18:18 | `0f8532aefdff` | 噪声面 |
| 2199 | `.tmp/whitelist_backup_2026_10_17/t3_nt_llm_calls_2026_10_15.jsonl` | 5,250 | 2026-10-15 17:21:54 | `0cb1decec878` | 噪声面 |
| 2200 | `.tmp/whitelist_backup_2026_10_17/t3_nt_measure_2026_10_15.py` | 17,111 | 2026-10-15 17:21:07 | `35860b379b7a` | 噪声面 |
| 2201 | `.tmp/whitelist_backup_2026_10_17/t3_nt_measurement_2026_10_15.json` | 19,576 | 2026-10-15 17:21:54 | `92f0dc763caf` | 噪声面 |
| 2202 | `.tmp/whitelist_backup_2026_10_17/t3_nt_verify.py` | 6,657 | 2026-10-15 17:22:40 | `a1c38dc17d65` | 噪声面 |
| 2203 | `.tmp/whitelist_backup_2026_10_17/t3_nt_verify_2026_10_15.json` | 3,885 | 2026-10-15 17:22:46 | `700de33ee255` | 噪声面 |
| 2204 | `.tmp/whitelist_backup_2026_10_17/t3_postchange_equiv.py` | 5,975 | 2026-10-15 17:19:03 | `1e579de6033c` | 噪声面 |
| 2205 | `.tmp/whitelist_backup_2026_10_17/t3_postchange_equiv_2026_10_15.json` | 3,904 | 2026-10-15 17:19:10 | `e8a97dc64a08` | 噪声面 |
| 2206 | `.tmp/whitelist_backup_2026_10_17/t3_postchange_manifest_check_2026_10_15.json` | 2,135 | 2026-10-15 17:23:04 | `dbfae4d96b46` | 噪声面 |
| 2207 | `.tmp/whitelist_backup_2026_10_17/t3_postcheck.py` | 3,129 | 2026-10-15 17:22:55 | `20c96933b00d` | 噪声面 |
| 2208 | `.tmp/whitelist_backup_2026_10_17/t3_prechange_manifest_2026_10_15.json` | 76,683 | 2026-10-15 17:17:35 | `f1508ebe14e7` | 噪声面 |
| 2209 | `.tmp/whitelist_backup_2026_10_17/t3_prove_minimal_increment_2026_10_15.json` | 433 | 2026-10-15 17:18:18 | `3f858f6958cd` | 噪声面 |
| 2210 | `.tmp/whitelist_backup_2026_10_17/t3_prove_minimal_increment_2026_10_15.py` | 7,303 | 2026-10-15 17:18:11 | `1f39cf068862` | 噪声面 |
| 2211 | `.tmp/whitelist_backup_2026_10_17/t3_repro_probe_ftfb_freeze_2026_10_16.json` | 2,936 | 2026-10-16 22:59:34 | `44761c404b86` | 噪声面 |
| 2212 | `.tmp/whitelist_backup_2026_10_17/t3_repro_probe_llm_calls_2026_10_16.jsonl` | 7,441 | 2026-10-16 23:04:59 | `54ad4d2cd8bf` | 噪声面 |
| 2213 | `.tmp/whitelist_backup_2026_10_17/t3_repro_probe_measure_2026_10_16.json` | 9,137 | 2026-10-16 23:04:59 | `31779f66c051` | 噪声面 |
| 2214 | `.tmp/whitelist_backup_2026_10_17/t5_baseline_manifest_2026_10_15.json` | 99,724 | 2026-10-15 16:16:38 | `2d5ad82c0a63` | 噪声面 |
| 2215 | `.tmp/whitelist_backup_2026_10_17/t5_harness_diff_2026_10_15.diff` | 4,043 | 2026-10-15 16:21:14 | `6f1e9689201b` | 噪声面 |
| 2216 | `.tmp/whitelist_backup_2026_10_17/t5_kill_line_freeze_2026_10_15.json` | 3,183 | 2026-10-15 16:17:11 | `1910a62c1e9f` | 噪声面 |
| 2217 | `.tmp/whitelist_backup_2026_10_17/t5_nt_llm_calls_2026_10_15.jsonl` | 7,258 | 2026-10-15 16:20:15 | `8e488d14bff6` | 噪声面 |
| 2218 | `.tmp/whitelist_backup_2026_10_17/t5_nt_measure_2026_10_15.py` | 15,602 | 2026-10-15 16:18:23 | `c96c985d8e23` | 噪声面 |
| 2219 | `.tmp/whitelist_backup_2026_10_17/t5_nt_measurement_2026_10_15.json` | 3,845 | 2026-10-15 16:20:15 | `674e95ecff03` | 噪声面 |
| 2220 | `.tmp/whitelist_backup_2026_10_17/t5_prefix_T1T4_digest_2026_10_15.json` | 400 | 2026-10-15 16:16:57 | `9eb43782b73c` | 噪声面 |
| 2221 | `.tmp/whitelist_backup_2026_10_17/t5_prove_minimal_increment_2026_10_15.py` | 6,308 | 2026-10-15 16:21:07 | `65cec9c9788e` | 噪声面 |
| 2222 | `.tmp/whitelist_backup_2026_10_17/t5_write_docs_2026_10_15.py` | 47,918 | 2026-10-15 16:25:36 | `f104bf4706e6` | 噪声面 |
| 2223 | `.tmp/whitelist_backup_2026_10_17/tables.py` | 1,818 | 2026-10-10 13:52:29 | `02cc157b6d69` | 噪声面 |
| 2224 | `.tmp/whitelist_backup_2026_10_17/three_seed_caliber_decl_2026_10_16.json` | 4,859 | 2026-10-16 10:59:50 | `5df309d557b0` | 噪声面 |
| 2225 | `.tmp/whitelist_backup_2026_10_17/three_seed_collect_2026_10_16.py` | 28,520 | 2026-10-16 11:11:41 | `672d12ad9801` | 噪声面 |
| 2226 | `.tmp/whitelist_backup_2026_10_17/three_seed_collect_log_2026_10_16.txt` | 16,230 | 2026-10-16 11:10:03 | `55c783261d18` | 噪声面 |
| 2227 | `.tmp/whitelist_backup_2026_10_17/three_seed_freeze_2026_10_16.json` | 10,536 | 2026-10-16 10:58:59 | `46260e3b8426` | 噪声面 |
| 2228 | `.tmp/whitelist_backup_2026_10_17/three_seed_llm_calls_2026_10_16.jsonl` | 104,288 | 2026-10-16 11:10:03 | `5a8cbcf85aa7` | 噪声面 |
| 2229 | `.tmp/whitelist_backup_2026_10_17/three_seed_measurement_2026_10_16.json` | 226,256 | 2026-10-16 11:12:10 | `ff5ed4b0e329` | 噪声面 |
| 2230 | `.tmp/whitelist_backup_2026_10_17/three_seed_preflight_2026_10_16.py` | 5,661 | 2026-10-16 10:57:57 | `98e0e4ae7a73` | 噪声面 |
| 2231 | `.tmp/whitelist_backup_2026_10_17/three_seed_verify_2026_10_16.json` | 3,205 | 2026-10-16 11:24:04 | `61e3d0bfa05d` | 噪声面 |
| 2232 | `.tmp/whitelist_backup_2026_10_17/three_seed_verify_2026_10_16.py` | 13,402 | 2026-10-16 11:12:04 | `5c382ace9573` | 噪声面 |
| 2233 | `.tmp/whitelist_backup_2026_10_17/three_seed_write_doc_2026_10_16.py` | 50,308 | 2026-10-16 11:23:38 | `f546bdd3630c` | 噪声面 |
| 2234 | `.tmp/whitelist_backup_2026_10_17/u04_1_chain_verify.py` | 4,849 | 2026-10-09 17:22:54 | `13e573534692` | 噪声面 |
| 2235 | `.tmp/whitelist_backup_2026_10_17/u04_1_dual_verify.py` | 3,228 | 2026-10-09 17:23:16 | `f5702456560f` | 噪声面 |
| 2236 | `.tmp/whitelist_backup_2026_10_17/u04_1_make_data.py` | 19,773 | 2026-10-09 17:24:49 | `309ac58e049d` | 噪声面 |
| 2237 | `.tmp/whitelist_backup_2026_10_17/verify_final.py` | 805 | 2026-10-14 22:15:42 | `904eb215f139` | 噪声面 |
| 2238 | `.tmp/whitelist_backup_2026_10_17/verify_t3trap_bprime_2026_10_15.py` | 6,928 | 2026-10-15 17:19:40 | `a9e880243eab` | 噪声面 |
| 2239 | `.tmp/whitelist_backup_2026_10_17/vk_denominator_2026_10_16.py` | 856 | 2026-10-16 16:50:40 | `d935b89bfa31` | 噪声面 |
| 2240 | `.tmp/whitelist_backup_2026_10_17/vk_interval_arith_2026_10_16.py` | 1,273 | 2026-10-16 16:48:02 | `901d8df83bb3` | 噪声面 |
| 2241 | `.tmp/whitelist_backup_2026_10_17/vk_v3df_0_1_agree.py` | 6,140 | 2026-10-09 12:02:48 | `84c090952894` | 噪声面 |
| 2242 | `.tmp/whitelist_backup_2026_10_17/vk_v3df_0_1_coverage_gap.py` | 1,971 | 2026-10-09 12:01:06 | `df25000e7180` | 噪声面 |
| 2243 | `.tmp/whitelist_backup_2026_10_17/vk_v3df_0_1_materiality.py` | 2,875 | 2026-10-09 12:01:29 | `b666b7a38082` | 噪声面 |
| 2244 | `.tmp/whitelist_backup_2026_10_17/vk_v3df_0_1_verify_2026_10_09.py` | 14,347 | 2026-10-09 12:00:28 | `0e7cb9348a16` | 噪声面 |
| 2245 | `.tmp/whitelist_backup_2026_10_17/vk_verify_2026_10_16.py` | 3,780 | 2026-10-16 13:57:57 | `6ad7edf03032` | 噪声面 |
| 2246 | `.tmp/whitelist_backup_2026_10_17/vk_verify_interval_ceiling_2026_10_16.py` | 3,692 | 2026-10-16 16:53:20 | `18b0f12b2c66` | 噪声面 |
| 2247 | `.tmp/whitelist_backup_2026_10_17/vk_write_2026_10_16.py` | 62,030 | 2026-10-16 13:57:37 | `2334a967a1d4` | 噪声面 |
| 2248 | `.tmp/whitelist_backup_2026_10_17/vk_write_interval_ceiling_post_lock_2026_10_16.py` | 47,768 | 2026-10-16 16:52:55 | `3076d727e02c` | 噪声面 |
| 2249 | `.tmp/whitelist_backup_2026_10_17/write_items_json.py` | 4,388 | 2026-10-10 13:54:45 | `9dce7986e20d` | 噪声面 |
| 2250 | `.tmp/whitelist_backup_2026_10_17/write_summary_json.py` | 9,049 | 2026-10-10 13:56:04 | `6214ad3cdc2d` | 噪声面 |
| 2251 | `.tmp/whitelist_backup_2026_10_17/write_t3trap_bprime_2026_10_15.py` | 33,905 | 2026-10-15 17:19:32 | `ca5fc520f530` | 噪声面 |
| 2252 | `.tmp/wlbk_2026_10_17_backup.py` | 4,709 | 2026-10-17 11:57:09 | `478cc73615bc` | 噪声面 |
| 2253 | `.tmp/wlbk_2026_10_17_backup2.py` | 4,423 | 2026-10-17 12:04:10 | `e8b118a2bf06` | 噪声面 |
| 2254 | `.tmp/wlbk_2026_10_17_backup2_out.json` | 291,353 | 2026-10-17 12:04:21 | `bf56443cad2c` | 噪声面 |
| 2255 | `.tmp/wlbk_2026_10_17_backup_out.json` | 306,195 | 2026-10-17 11:57:32 | `08d47e831498` | 噪声面 |
| 2256 | `.tmp/wlbk_2026_10_17_calib.py` | 2,357 | 2026-10-17 11:58:47 | `30de28558f37` | 噪声面 |
| 2257 | `.tmp/wlbk_2026_10_17_calib_out.json` | 967 | 2026-10-17 11:58:53 | `ed2e5d811694` | 噪声面 |
| 2258 | `.tmp/wlbk_2026_10_17_scan.py` | 9,929 | 2026-10-17 11:55:44 | `aa6abcc62b9e` | 噪声面 |
| 2259 | `.tmp/wlbk_2026_10_17_scan_out.json` | 1,959,173 | 2026-10-17 11:56:01 | `dfd3205fb12a` | 噪声面 |
| 2260 | `.tmp/wlbk_2026_10_17_write_registers.py` | 46,263 | 2026-10-17 12:09:24 | `815fc6e600d8` | 噪声面 |
| 2261 | `.tmp/write_items_json.py` | 4,388 | 2026-10-10 13:54:45 | `9dce7986e20d` | 噪声面 |
| 2262 | `.tmp/write_summary_json.py` | 9,049 | 2026-10-10 13:56:04 | `6214ad3cdc2d` | 噪声面 |
| 2263 | `.tmp/write_t3trap_bprime_2026_10_15.py` | 33,905 | 2026-10-15 17:19:32 | `ca5fc520f530` | 噪声面 |
| 2264 | `.tmp/zerocall_e3_chk_readerrors.py` | 505 | 2026-10-17 17:20:38 | `fb9265b67853` | 噪声面 |
| 2265 | `.tmp/zerocall_e3_f5b.json` | 1,808 | 2026-10-17 17:22:17 | `85275f2242b3` | 噪声面 |
| 2266 | `.tmp/zerocall_e3_f5b.py` | 3,623 | 2026-10-17 17:22:03 | `3ecba898966b` | 噪声面 |
| 2267 | `.tmp/zerocall_e3_fidelity.py` | 2,300 | 2026-10-17 17:23:12 | `caa9d22695dc` | 噪声面 |
| 2268 | `.tmp/zerocall_e3_hop2.json` | 33,037 | 2026-10-17 17:18:29 | `1c6b883a6392` | 噪声面 |
| 2269 | `.tmp/zerocall_e3_hop2.md` | 11,016 | 2026-10-17 17:18:29 | `3a96ae0bd44c` | 噪声面 |
| 2270 | `.tmp/zerocall_e3_hop2.py` | 10,063 | 2026-10-17 17:18:14 | `d67d3e45bfda` | 噪声面 |
| 2271 | `.tmp/zerocall_e3_out.json` | 1,876,399 | 2026-10-17 17:15:18 | `4974f56d2b35` | 噪声面 |
| 2272 | `.tmp/zerocall_e3_prewrite.py` | 2,951 | 2026-10-17 17:24:23 | `883666683623` | 噪声面 |
| 2273 | `.tmp/zerocall_e3_probe.py` | 16,361 | 2026-10-17 17:14:11 | `68785c115f03` | 噪声面 |
| 2274 | `.tmp/zerocall_e3_summary.json` | 72,584 | 2026-10-17 17:22:42 | `1797d3e9e2f8` | 噪声面 |
| 2275 | `.tmp/zerocall_e3_summary.md` | 7,784 | 2026-10-17 17:22:42 | `59b9e8aadd87` | 噪声面 |
| 2276 | `.tmp/zerocall_e3_summary.py` | 5,300 | 2026-10-17 17:22:34 | `115e8e9e5d88` | 噪声面 |
| 2277 | `.tmp/zerocall_e3_sweeper.json` | 316,892 | 2026-10-17 17:19:47 | `40fcd9881663` | 噪声面 |
| 2278 | `.tmp/zerocall_e3_sweeper.md` | 157,994 | 2026-10-17 17:19:47 | `a181fdfd1dcb` | 噪声面 |
| 2279 | `.tmp/zerocall_e3_sweeper.py` | 7,238 | 2026-10-17 17:19:29 | `d6839f914fe0` | 噪声面 |
| 2280 | `.tmp/zerocall_e3_triage.json` | 29 | 2026-10-17 17:17:30 | `d77c2294859f` | 噪声面 |
| 2281 | `.tmp/zerocall_e3_triage.md` | 161 | 2026-10-17 17:17:30 | `fa8591787761` | 噪声面 |
| 2282 | `.tmp/zerocall_e3_triage.py` | 5,363 | 2026-10-17 17:16:36 | `22ee5f68d85b` | 噪声面 |
| 2283 | `.tmp/zerocall_e3_utf16.json` | 12,259 | 2026-10-17 17:24:04 | `6cf0d6c2a030` | 噪声面 |
| 2284 | `.tmp/zerocall_e3_utf16.py` | 1,022 | 2026-10-17 17:23:27 | `ba6d7250e0eb` | 噪声面 |
| 2285 | `.tmp/zerocall_e3_utf16_sweep.py` | 4,709 | 2026-10-17 17:23:55 | `a63bc647a4bc` | 噪声面 |
| 2286 | `.tmp/zerocall_e3_verify.py` | 1,559 | 2026-10-17 17:29:12 | `418fc668eef6` | 噪声面 |
| 2287 | `.tmp/zerocall_e3_write.py` | 34,887 | 2026-10-17 17:28:45 | `9f51adfef897` | 噪声面 |
| 2288 | `.tmp/zerocall_redef_body_2026_10_17.md` | 31,602 | 2026-10-17 17:41:29 | `f2bed1e98f62` | 噪声面 |
| 2289 | `.tmp/zerocall_redef_write_2026_10_17.py` | 2,556 | 2026-10-17 17:41:38 | `57449395f915` | 噪声面 |
| 2290 | `.trae/scripts/_arxiv_renumber.py` | 16,531 | 2026-09-09 14:14:27 | `f488ad141ef9` | 成果面 |
| 2291 | `.trae/scripts/_verify_tex.py` | 18,250 | 2026-09-09 14:14:27 | `3b977bb8a715` | 成果面 |
| 2292 | `.vscode/settings.json` | 41 | 2026-10-12 13:23:50 | `4ad2e86b6169` | 成果面 |
| 2293 | `_docwriter_sha_index_scratch.py` | 1,369 | 2026-10-13 21:57:53 | `5d14277b148f` | 成果面 |
| 2294 | `_kd_flip_anchor_scan.py` | 2,575 | 2026-10-17 21:31:33 | `9560a4fb4121` | 成果面 |
| 2295 | `_kd_flip_kdcensus.py` | 3,541 | 2026-10-17 21:34:10 | `ff11e0c650d8` | 成果面 |
| 2296 | `_kd_flip_verify.py` | 1,827 | 2026-10-17 21:38:33 | `5bbdc66e0855` | 成果面 |
| 2297 | `_kd_flip_write.py` | 38,829 | 2026-10-17 21:38:16 | `e3063681d015` | 成果面 |
| 2298 | `_remote_pullback_2026_10_17/_september_workspace/deposon_team/verifier/v42_v2_2026_09_16.py` | 17,363 | 2026-10-17 15:55:12 | `c5598b13c139` | 成果面 |
| 2299 | `_remote_pullback_2026_10_17/_september_workspace/deposon_team/verifier/v42_v2_baseline_2026_09_16.json` | 1,879 | 2026-10-17 15:55:12 | `483602856618` | 成果面 |
| 2300 | `_remote_pullback_2026_10_17/_september_workspace/deposon_team/verifier/v42_v2_runs_2026_09_16.jsonl` | 770 | 2026-10-17 15:55:13 | `b471190e579c` | 成果面 |
| 2301 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_archive_manifest_2026_09_18.json` | 4,712 | 2026-10-17 15:54:11 | `a729875c0c67` | 成果面 |
| 2302 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_archive_manifest_2026_09_20.json` | 35,690 | 2026-10-17 15:54:11 | `df133892691e` | 成果面 |
| 2303 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_audit_secret_2026_09_20_anchor_guard.py` | 6,433 | 2026-10-17 15:54:12 | `780a8adae5e8` | 成果面 |
| 2304 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_audit_temp_inspect_minimax_m3.py.bak` | 1,171 | 2026-10-17 15:54:12 | `dd92ca013774` | 成果面 |
| 2305 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_audit_temp_inspect_workers.py.bak` | 1,158 | 2026-10-17 15:54:12 | `772925b20bcc` | 成果面 |
| 2306 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_audit_temp_stage1_tra_breakdown.py.bak` | 18,023 | 2026-10-17 15:54:13 | `dfc4aa73e2fc` | 成果面 |
| 2307 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_coze_online_v3_d7format_2026_09_18.pdf` | 454,307 | 2026-10-17 15:54:14 | `adc99e04ac53` | 成果面 |
| 2308 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_coze_paper_v1_双审报告_2026_09_17.md` | 85,627 | 2026-10-17 15:54:14 | `dc761bd8b85d` | 成果面 |
| 2309 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_cpath_sim_run_2026_09_10.log` | 1,508 | 2026-10-17 15:54:15 | `6bfc5dde07a8` | 成果面 |
| 2310 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_main_runner_20260918.log` | 9,232 | 2026-10-17 15:54:15 | `b6657ba162b3` | 成果面 |
| 2311 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_main_runner_2026_09_18.py` | 41,446 | 2026-10-17 15:54:16 | `f3d4ec483599` | 成果面 |
| 2312 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_md_report_only_2026_09_18.py` | 13,694 | 2026-10-17 15:54:16 | `7a5be4aef9ac` | 成果面 |
| 2313 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918.log` | 2,088 | 2026-10-17 15:54:17 | `41bea33b9492` | 成果面 |
| 2314 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json` | 2,292 | 2026-10-17 15:54:18 | `0a1e91d6f772` | 成果面 |
| 2315 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_sanity_3backbone_2026_09_18.py` | 5,452 | 2026-10-17 15:54:18 | `c917f8fa142c` | 成果面 |
| 2316 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_verify_sha_2026_09_18.py` | 2,938 | 2026-10-17 15:54:19 | `0b7e50a8a036` | 成果面 |
| 2317 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_deposon_v2scripts_reverify_worker_2026_09_18.py` | 34,134 | 2026-10-17 15:54:19 | `18984b04c45e` | 成果面 |
| 2318 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_final_sha_2026_09_18.py` | 2,678 | 2026-10-17 15:54:20 | `0769f60a0504` | 成果面 |
| 2319 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch2_2026_09_18.py` | 4,100 | 2026-10-17 15:54:20 | `81bb1751be4c` | 成果面 |
| 2320 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch3_2026_09_18.py` | 3,207 | 2026-10-17 15:54:20 | `01e63e488ce2` | 成果面 |
| 2321 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch4_2026_09_18.py` | 8,225 | 2026-10-17 15:54:21 | `2efcd5ff42f1` | 成果面 |
| 2322 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch6_2026_09_18.py` | 2,214 | 2026-10-17 15:54:21 | `1c59e7b803fe` | 成果面 |
| 2323 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch7_2026_09_18.py` | 4,261 | 2026-10-17 15:54:22 | `389283c51275` | 成果面 |
| 2324 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch8_2026_09_18.py` | 2,249 | 2026-10-17 15:54:22 | `5057ccf97d6b` | 成果面 |
| 2325 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_d05_rescue_2026_09_18.py` | 3,524 | 2026-10-17 15:54:23 | `2c2cc3ff542a` | 成果面 |
| 2326 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_ftfb_pass2_results_limitations_audit_2026_09_17.md` | 11,390 | 2026-10-17 15:54:23 | `5610a549e116` | 成果面 |
| 2327 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_coze_online_v2_2026_09_18.md` | 18,611 | 2026-10-17 15:54:24 | `dc3e56adc3fc` | 成果面 |
| 2328 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_coze_paper_v1_委托_2026_09_17.md` | 12,813 | 2026-10-17 15:54:24 | `f4610b0bb47c` | 成果面 |
| 2329 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_glm_ftfb_deep_revision_2026_09_18.md` | 26,990 | 2026-10-17 15:54:25 | `3de722dc9e39` | 成果面 |
| 2330 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_kimi_push_v3_final_2026_09_17.md` | 10,307 | 2026-10-17 15:54:25 | `affe5eebf2e7` | 成果面 |
| 2331 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_kimi_push_v3_final_v2_2026_09_17.md` | 13,967 | 2026-10-17 15:54:25 | `6d95317f4355` | 成果面 |
| 2332 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_kimi_push_v3_委托_2026_09_17.md` | 13,592 | 2026-10-17 15:54:26 | `05f92d837412` | 成果面 |
| 2333 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_kimi_upload_requirements_2026_09_18.md` | 22,591 | 2026-10-17 15:54:26 | `8b22a026f30b` | 成果面 |
| 2334 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_mavis_full_mirror_request_2026_09_17.md` | 9,717 | 2026-10-17 15:54:27 | `f2934e5279e6` | 成果面 |
| 2335 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_trae_code_2026_09_17_final.md` | 10,702 | 2026-10-17 15:54:27 | `b75ba5c152b7` | 成果面 |
| 2336 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_openrouter_emb_runner.bak.note` | 5 | 2026-10-17 15:54:28 | `f01a374e9c81` | 成果面 |
| 2337 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_i_curvature_audit_probe_runner_2026_09_16.py` | 12,919 | 2026-10-17 15:54:28 | `e05555deb611` | 成果面 |
| 2338 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase1_finalize.log` | 1,184 | 2026-10-17 15:54:29 | `c2172607419e` | 成果面 |
| 2339 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase1_runner.log` | 8,202 | 2026-10-17 15:54:29 | `90ead4a9fba8` | 成果面 |
| 2340 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner.log` | 2,370 | 2026-10-17 15:54:29 | `37e1f9cc19d3` | 成果面 |
| 2341 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_171640.log` | 1,516 | 2026-10-17 15:54:30 | `77b62d39f474` | 成果面 |
| 2342 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_172440_gpt56sol.log` | 865 | 2026-10-17 15:54:30 | `fefdac35fa6e` | 成果面 |
| 2343 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_172928_gpt56sol.log` | 955 | 2026-10-17 15:54:31 | `ef172ad159b4` | 成果面 |
| 2344 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_173159_gpt56sol.log` | 2,765 | 2026-10-17 15:54:31 | `a6517028a720` | 成果面 |
| 2345 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_174011_claude_sonnet5.log` | 2,687 | 2026-10-17 15:54:32 | `0ffa261c5ed8` | 成果面 |
| 2346 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_175003_gemini_37flash.log` | 2,342 | 2026-10-17 15:54:32 | `0b61aadb4509` | 成果面 |
| 2347 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase2_finalize.log` | 2,712 | 2026-10-17 15:54:33 | `4a707293fada` | 成果面 |
| 2348 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase2_finalize_20260917_142748.log` | 1,224 | 2026-10-17 15:54:33 | `995bad3cce30` | 成果面 |
| 2349 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase2_glm53.log` | 2,542 | 2026-10-17 15:54:33 | `11f8ec231ead` | 成果面 |
| 2350 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase2_glm53_only_20260917_142011.log` | 1,140 | 2026-10-17 15:54:34 | `4c91156dc821` | 成果面 |
| 2351 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase2_or_embedding.err` | 530 | 2026-10-17 15:54:34 | `4346e7e916db` | 成果面 |
| 2352 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase2_or_embedding.log` | 564 | 2026-10-17 15:54:35 | `bb54209b0cdc` | 成果面 |
| 2353 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase2_or_embedding_v3_2026_09_17.console.log` | 10,102 | 2026-10-17 15:54:35 | `4056814f73dc` | 成果面 |
| 2354 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase2_probe.log` | 3,100 | 2026-10-17 15:54:36 | `b1128aa5441c` | 成果面 |
| 2355 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase2_probe_agent.log` | 6,760 | 2026-10-17 15:54:36 | `49765ca671d8` | 成果面 |
| 2356 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase2_probe_emb.log` | 2,046 | 2026-10-17 15:54:37 | `456a6bf39f9e` | 成果面 |
| 2357 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase2_probe_emb_proxy_v2.log` | 17,632 | 2026-10-17 15:54:37 | `b4d2803c6290` | 成果面 |
| 2358 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase2_probe_ext.log` | 4,992 | 2026-10-17 15:54:38 | `a72a38a9fb6f` | 成果面 |
| 2359 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase2_probe_gpt4o.log` | 3,462 | 2026-10-17 15:54:38 | `d9bf12a6f713` | 成果面 |
| 2360 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase2_runner.log` | 3,416 | 2026-10-17 15:54:39 | `9b4cdb0ec25b` | 成果面 |
| 2361 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase2_vector_emb_doubao_2026_09_17.console.log` | 6,134 | 2026-10-17 15:54:39 | `1f65ad49911c` | 成果面 |
| 2362 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_l_v3_phase2_vector_emb_doubao_2026_09_17.console2.log` | 2,925 | 2026-10-17 15:54:40 | `fcca7035073a` | 成果面 |
| 2363 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_doubao_4versions_diff_2026_09_17.json` | 1,393 | 2026-10-17 15:54:40 | `49dde3059959` | 成果面 |
| 2364 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_doubao_4versions_diff_2026_09_17.py` | 2,720 | 2026-10-17 15:54:41 | `93527eb7b2f7` | 成果面 |
| 2365 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_doubao_emb_direct_2026_09_17.py` | 2,371 | 2026-10-17 15:54:41 | `9bcfe80c0dd0` | 成果面 |
| 2366 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_doubao_emb_via_proxy_2026_09_17.py` | 2,589 | 2026-10-17 15:54:42 | `f2818fc2ddff` | 成果面 |
| 2367 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_teamo_via_proxy.log` | 4,526 | 2026-10-17 15:54:42 | `74badfd3270f` | 成果面 |
| 2368 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_teamo_via_proxy.py` | 2,841 | 2026-10-17 15:54:43 | `dce965058076` | 成果面 |
| 2369 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_reviewer_a_audit_tmp.py` | 4,397 | 2026-10-17 15:54:43 | `268225ccbb76` | 成果面 |
| 2370 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_sanity_openai_more.log` | 1,444 | 2026-10-17 15:54:44 | `c7db5599e6a5` | 成果面 |
| 2371 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_sanity_openai_more.py` | 2,187 | 2026-10-17 15:54:44 | `e11319f32dc5` | 成果面 |
| 2372 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_sanity_teamo_one.py` | 2,119 | 2026-10-17 15:54:45 | `63eb0a0aa102` | 成果面 |
| 2373 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_sanity_teamo_three.log` | 2,168 | 2026-10-17 15:54:45 | `e6e40a339ef7` | 成果面 |
| 2374 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_sanity_teamo_three.py` | 3,540 | 2026-10-17 15:54:45 | `888d02cd1443` | 成果面 |
| 2375 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_teamorouter_smoke_tmp.json` | 277 | 2026-10-17 15:54:46 | `4181a24c9ca1` | 成果面 |
| 2376 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_temp_volc_test.py` | 6,687 | 2026-10-17 15:54:46 | `264f2bf5a3f2` | 成果面 |
| 2377 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_test_3bb_vary.log` | 11,522 | 2026-10-17 15:54:47 | `699d751ced17` | 成果面 |
| 2378 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_tmp_inspect_22cap.py` | 675 | 2026-10-17 15:54:47 | `0c9addf4a70f` | 成果面 |
| 2379 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_tmp_inspect_5model.py` | 1,029 | 2026-10-17 15:54:48 | `048ebc99177c` | 成果面 |
| 2380 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_tmp_probe_archive` | 1,270 | 2026-10-17 15:54:48 | `a6689025804c` | 成果面 |
| 2381 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_v2_stage1_60cells.console.log` | 17,158 | 2026-10-17 15:54:49 | `cd7710002ff0` | 成果面 |
| 2382 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_v2_stage3_f3_strip.console.log` | 2,440 | 2026-10-17 15:54:49 | `0087364298e1` | 成果面 |
| 2383 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_v3x_6way_finalize.log` | 618 | 2026-10-17 15:54:49 | `1db3842e21e6` | 成果面 |
| 2384 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_v3x_6way_run.log` | 8,952 | 2026-10-17 15:54:50 | `0a2e66649663` | 成果面 |
| 2385 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_v3x_6way_stage3_minimal.log` | 1,678 | 2026-10-17 15:54:50 | `a8a69c85571c` | 成果面 |
| 2386 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_v3x_6way_stage3_recovery.log` | 2,242 | 2026-10-17 15:54:51 | `1758b615ebb1` | 成果面 |
| 2387 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_v41_flash_rag_baseline_run.log` | 17,456 | 2026-10-17 15:54:52 | `7b659fdc69c9` | 成果面 |
| 2388 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_v41_flash_rag_baseline_run.log.bak` | 6,106 | 2026-10-17 15:54:52 | `18b56e3d1c7b` | 成果面 |
| 2389 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_v41_flash_rag_caption_embs.bak.json` | 612,511 | 2026-10-17 15:54:53 | `25f745609658` | 成果面 |
| 2390 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_v41_flash_rag_partial.bak.json` | 88,584 | 2026-10-17 15:54:53 | `b0e2673f4a56` | 成果面 |
| 2391 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_volc_22cap_emb.log` | 9,068 | 2026-10-17 15:54:54 | `27cb6630ec37` | 成果面 |
| 2392 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_worker_openrouter_rag_run.log` | 6,476 | 2026-10-17 15:54:54 | `9a5603811f45` | 成果面 |
| 2393 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/compile_verification.txt` | 9,663 | 2026-10-17 15:54:54 | `463fc7575663` | 成果面 |
| 2394 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/deposon_d_fix2_metric_verify_9m60c_2026_09_15.log` | 24,634 | 2026-10-17 15:54:55 | `1eec8b03b30f` | 成果面 |
| 2395 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/deposon_deepseek_v41_flash_30cells_2026_09_10.log` | 6,514 | 2026-10-17 15:54:55 | `cbcecdec0fdb` | 成果面 |
| 2396 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/deposon_dpath_cross_modal_2026_09_10.log` | 8,885 | 2026-10-17 15:54:56 | `95298ca6d95e` | 成果面 |
| 2397 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/deposon_dpath_cross_modal_runner_2026_09_10.stdout.log` | 17,772 | 2026-10-17 15:54:56 | `388439eb8d17` | 成果面 |
| 2398 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/deposon_feshbach_rag_30cells_2026_09_10.log` | 6,887 | 2026-10-17 15:54:57 | `2e8564b94b02` | 成果面 |
| 2399 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/deposon_v2_phase1_60cells_2026_09_11.log` | 8,578 | 2026-10-17 15:54:57 | `b5169e715434` | 成果面 |
| 2400 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/deposon_v2_phase2_f2_2026_09_11.log` | 1,272 | 2026-10-17 15:54:58 | `c0fa485cd9fe` | 成果面 |
| 2401 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/deposon_v2_phase3_f3_2026_09_11.log` | 1,247 | 2026-10-17 15:54:58 | `3b61b7028cc8` | 成果面 |
| 2402 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/deposon_v2_phase4_f4_2026_09_11.log` | 1,064 | 2026-10-17 15:54:58 | `86812e1003e5` | 成果面 |
| 2403 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/deposon_v2_phase5_f5_2026_09_11.log` | 1,092 | 2026-10-17 15:54:59 | `af736aa656c7` | 成果面 |
| 2404 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/deposon_v41_flash_60cells_v2_2026_09_10.log` | 12,470 | 2026-10-17 15:54:59 | `ad7fafb3582b` | 成果面 |
| 2405 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/deposon_volcengine_minimax_m3_30cells_2026_09_10.log` | 3,444 | 2026-10-17 15:55:00 | `a0fc4423470c` | 成果面 |
| 2406 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/deposon_volcengine_seed_code_30cells_2026_09_10.log` | 7,342 | 2026-10-17 15:55:00 | `19f295ce9ff9` | 成果面 |
| 2407 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/deposon_volcengine_worker_b_2026_09_10.log` | 3,326 | 2026-10-17 15:55:01 | `5d40bdc3a0db` | 成果面 |
| 2408 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/deposon_volcengine_worker_c_2026_09_10.log` | 5,869 | 2026-10-17 15:55:01 | `e62cd7fd2a0e` | 成果面 |
| 2409 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/deposon_volcengine_worker_c_2026_09_10.run.log` | 12,070 | 2026-10-17 15:55:02 | `644425852b1a` | 成果面 |
| 2410 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/fiction_that_feeds_back.pdf` | 356,123 | 2026-10-17 15:55:02 | `2d9edc8c7303` | 成果面 |
| 2411 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/fiction_that_feeds_back.tex` | 93,324 | 2026-10-17 15:55:03 | `d060f75dbe9f` | 成果面 |
| 2412 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/fiction_that_feeds_back_source.md` | 84,388 | 2026-10-17 15:55:04 | `543479649b3e` | 成果面 |
| 2413 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/ftfb_pass1_background_methodology_audit_2026_09_17.md` | 8,257 | 2026-10-17 15:55:04 | `7243192d86be` | 成果面 |
| 2414 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/gpt6_30cells_run.log` | 4,220 | 2026-10-17 15:55:05 | `74bbc7dcf5aa` | 成果面 |
| 2415 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/gpt6_30cells_run.log.err` | 0 | 2026-10-17 15:55:05 | `e3b0c44298fc` | 成果面 |
| 2416 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/LETTER_TO_EXTERNAL_ADVISOR_2026_09_18_FINAL.md` | 10,586 | 2026-10-17 15:54:06 | `ff37f39264bc` | 成果面 |
| 2417 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/LETTER_TO_KIMI_GITHUB_UPLOAD_2026_09_18.md` | 13,295 | 2026-10-17 15:54:07 | `00e5d185ef74` | 成果面 |
| 2418 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/LETTER_TO_TRAE_2026_09_11.md` | 22,820 | 2026-10-17 15:54:07 | `b09251018102` | 成果面 |
| 2419 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/LETTER_TO_TRAE_FIX_SELFCHECK_2026_09_15.md` | 7,855 | 2026-10-17 15:54:08 | `c0d629df69d8` | 成果面 |
| 2420 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/LETTER_TO_TRAE_REVIEW_2026_09_16.md` | 12,671 | 2026-10-17 15:54:08 | `c086c84e04a6` | 成果面 |
| 2421 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/p_i_curvature_audit_probe_results_2026_09_16.json` | 2,637 | 2026-10-17 15:55:06 | `ae07f5551e87` | 成果面 |
| 2422 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_content_A1_dsv4pro.md` | 20,082 | 2026-10-17 15:55:06 | `5198a7059c06` | 成果面 |
| 2423 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_content_A1_glm51.md` | 7,617 | 2026-10-17 15:55:07 | `fd38a2a1ea05` | 成果面 |
| 2424 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_content_A2_kimik3.md` | 24,843 | 2026-10-17 15:55:07 | `a964defb923d` | 成果面 |
| 2425 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_tech_B1_dsv4pro.md` | 30,494 | 2026-10-17 15:55:08 | `0d36d7cd0589` | 成果面 |
| 2426 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_tech_B1_grok46.md` | 18,923 | 2026-10-17 15:55:08 | `09784ff172b3` | 成果面 |
| 2427 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_tech_B2_grok46.md` | 13,726 | 2026-10-17 15:55:09 | `fe80bad08eef` | 成果面 |
| 2428 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_tech_B2_qwen3max.md` | 8,098 | 2026-10-17 15:55:09 | `8d00c6d4a242` | 成果面 |
| 2429 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/REVIEWER_B_TMP_RERUN_2026_09_15.md` | 21,654 | 2026-10-17 15:54:09 | `ceb8f595a911` | 成果面 |
| 2430 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/SHA256_MANIFEST.txt` | 552 | 2026-10-17 15:54:09 | `416dda94cb63` | 成果面 |
| 2431 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/TRAE_CODE_FIX_LIST_2026_09_18.md` | 9,343 | 2026-10-17 15:54:09 | `ace3c6b390cb` | 成果面 |
| 2432 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/TRAE_DAILY_AUDIT_LETTER_2026_09_18.md` | 11,575 | 2026-10-17 15:54:10 | `0011b7924dfb` | 成果面 |
| 2433 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/TRAE_FIX_RECEIPT_2026_09_18.md` | 4,784 | 2026-10-17 15:54:10 | `2e6a31af5e4b` | 成果面 |
| 2434 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/volcengine_glm_latest_30cells_v2_run_2026_09_10.log` | 4,091 | 2026-10-17 15:55:10 | `d2f7840ebc51` | 成果面 |
| 2435 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/volcengine_glm_latest_30cells_v2_run_2026_09_10.log.err` | 0 | 2026-10-17 15:55:10 | `e3b0c44298fc` | 成果面 |
| 2436 | `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/戴夫_FTFB双审包简报v3_2026-09-17.md` | 8,419 | 2026-10-17 15:55:11 | `6952b3b02b96` | 成果面 |
| 2437 | `_remote_pullback_2026_10_17/_september_workspace/results/_coze_online_v3_2026_09_18.md` | 7,476 | 2026-10-17 15:55:14 | `53c9c1ab2d12` | 成果面 |
| 2438 | `_remote_pullback_2026_10_17/_september_workspace/results/_coze_online_v3_d7format_2026_09_18.md` | 8,727 | 2026-10-17 15:55:14 | `debe3761c565` | 成果面 |
| 2439 | `_remote_pullback_2026_10_17/_september_workspace/results/_coze_online_v3_final_2026_09_18.md` | 11,660 | 2026-10-17 15:55:15 | `36439bc12bba` | 成果面 |
| 2440 | `_remote_pullback_2026_10_17/_september_workspace/results/_coze_online_v4_d7format_2026_09_26.pdf` | 465,366 | 2026-10-17 15:55:16 | `a82881653520` | 成果面 |
| 2441 | `_remote_pullback_2026_10_17/_september_workspace/results/_coze_paper_v1_draft_2026_09_17.md` | 29,511 | 2026-10-17 15:55:16 | `2832800ceca6` | 成果面 |
| 2442 | `_remote_pullback_2026_10_17/_september_workspace/results/_coze_paper_v1_summary_2026_09_17.md` | 3,624 | 2026-10-17 15:55:17 | `2efdc3d7741d` | 成果面 |
| 2443 | `_remote_pullback_2026_10_17/_september_workspace/verifier/volcengine_补测_worker_A_2026_09_10.py` | 16,252 | 2026-10-17 15:55:13 | `20b8a2f54ad9` | 成果面 |
| 2444 | `_remote_pullback_2026_10_17/letters/_v5_rj5_external_rederive_reply_codex_2026_09_29.md` | 27,835 | 2026-10-17 15:55:11 | `c706e69d00fc` | 成果面 |
| 2445 | `_remote_pullback_2026_10_17/results/_d05_sanity_3backbone_20260918_100110.json` | 2,292 | 2026-10-17 15:55:18 | `0a1e91d6f772` | 成果面 |
| 2446 | `_remote_pullback_2026_10_17/results/_trae_anchor_18_audit_20260917_193000.md` | 3,449 | 2026-10-17 15:55:19 | `4af67e6cbe71` | 成果面 |
| 2447 | `_remote_pullback_2026_10_17/results/_trae_corpus_5_audit_20260917_193000.md` | 3,467 | 2026-10-17 15:55:19 | `f2a655cd5e54` | 成果面 |
| 2448 | `_remote_pullback_2026_10_17/results/_trae_d7_v1_audit_20260917_190000.json` | 4,253 | 2026-10-17 15:55:19 | `3184b30b7b0d` | 成果面 |
| 2449 | `_remote_pullback_2026_10_17/results/_trae_d7_v1_audit_20260917_190000.md` | 7,863 | 2026-10-17 15:55:20 | `41c142eab4a1` | 成果面 |
| 2450 | `_remote_pullback_2026_10_17/results/_trae_kimi_push_v3_audit_20260917_193000.md` | 3,281 | 2026-10-17 15:55:21 | `8ece24be6b8a` | 成果面 |
| 2451 | `_remote_pullback_2026_10_17/results/_trae_paper_8ch_双审_20260917_200000.md` | 4,044 | 2026-10-17 15:55:21 | `145abbb9c365` | 成果面 |
| 2452 | `_remote_pullback_2026_10_17/results/attacker_xl_cache/algorithm_process.json` | 5,353 | 2026-10-17 15:55:21 | `1878428d3c90` | 成果面 |
| 2453 | `_remote_pullback_2026_10_17/results/attacker_xl_cache/biological_taxonomy.json` | 5,036 | 2026-10-17 15:55:22 | `8e11c03b11cf` | 成果面 |
| 2454 | `_remote_pullback_2026_10_17/results/attacker_xl_cache/geography_world.json` | 5,314 | 2026-10-17 15:55:22 | `3977f0ab6a28` | 成果面 |
| 2455 | `_remote_pullback_2026_10_17/results/attacker_xl_cache/historical_causality.json` | 4,389 | 2026-10-17 15:55:23 | `9d4b5a29decf` | 成果面 |
| 2456 | `_remote_pullback_2026_10_17/results/attacker_xl_cache/physics_concepts.json` | 5,874 | 2026-10-17 15:55:23 | `9ca7c11860f6` | 成果面 |
| 2457 | `_remote_pullback_2026_10_17/results/attacker_xl_cache/project_management.json` | 4,541 | 2026-10-17 15:55:24 | `e19e1137258e` | 成果面 |
| 2458 | `_remote_pullback_2026_10_17/results/deposon_benchmark_v1_3_labelfree.json` | 3,011 | 2026-10-17 15:55:25 | `57f06a426bec` | 成果面 |
| 2459 | `_remote_pullback_2026_10_17/results/deposon_benchmark_v1_3_resonant.json` | 3,134 | 2026-10-17 15:55:25 | `769ae8c908c9` | 成果面 |
| 2460 | `_remote_pullback_2026_10_17/results/deposon_benchmark_v1_4_sc5.json` | 12,479 | 2026-10-17 15:55:25 | `c9796d3b3263` | 成果面 |
| 2461 | `_remote_pullback_2026_10_17/results/deposon_g3_arrhenius.json` | 2,284 | 2026-10-17 15:55:26 | `a3de045b5dd7` | 成果面 |
| 2462 | `_remote_pullback_2026_10_17/results/deposon_v16_llm_prior_summary.json` | 5,517 | 2026-10-17 15:55:26 | `a7952d9d78db` | 成果面 |
| 2463 | `_remote_pullback_2026_10_17/results/deposon_v20_familyL_ingest.json` | 1,304 | 2026-10-17 15:55:27 | `d7c2d9fee5b2` | 成果面 |
| 2464 | `_remote_pullback_2026_10_17/results/Deposon_评估汇总_v1_3_0.json` | 2,811 | 2026-10-17 15:55:17 | `2f02f50c164b` | 成果面 |
| 2465 | `_remote_pullback_2026_10_17/results/familyL_cache/algorithm_process.json` | 1,442 | 2026-10-17 15:55:27 | `611f346091b9` | 成果面 |
| 2466 | `_remote_pullback_2026_10_17/results/familyL_cache/biological_taxonomy.json` | 1,296 | 2026-10-17 15:55:28 | `1a6bf80e22ca` | 成果面 |
| 2467 | `_remote_pullback_2026_10_17/results/familyL_cache/geography_world.json` | 1,319 | 2026-10-17 15:55:28 | `d5afc69e2fb3` | 成果面 |
| 2468 | `_remote_pullback_2026_10_17/results/familyL_cache/historical_causality.json` | 1,622 | 2026-10-17 15:55:29 | `db30c0e7bd33` | 成果面 |
| 2469 | `_remote_pullback_2026_10_17/results/familyL_cache/physics_concepts.json` | 1,253 | 2026-10-17 15:55:29 | `9963951cf859` | 成果面 |
| 2470 | `_remote_pullback_2026_10_17/results/familyL_cache/project_management.json` | 1,346 | 2026-10-17 15:55:30 | `48faa9bf14fa` | 成果面 |
| 2471 | `_remote_pullback_2026_10_17/results/familyL_prior_cache/algorithm_process.json` | 2,061 | 2026-10-17 15:55:30 | `b302e5f54141` | 成果面 |
| 2472 | `_remote_pullback_2026_10_17/results/familyL_prior_cache/biological_taxonomy.json` | 2,231 | 2026-10-17 15:55:31 | `8014873eee66` | 成果面 |
| 2473 | `_remote_pullback_2026_10_17/results/familyL_prior_cache/geography_world.json` | 2,314 | 2026-10-17 15:55:31 | `7056a5298bff` | 成果面 |
| 2474 | `_remote_pullback_2026_10_17/results/familyL_prior_cache/historical_causality.json` | 3,034 | 2026-10-17 15:55:32 | `6e032f3a58ac` | 成果面 |
| 2475 | `_remote_pullback_2026_10_17/results/familyL_prior_cache/physics_concepts.json` | 2,596 | 2026-10-17 15:55:32 | `9eae1fa8fd7c` | 成果面 |
| 2476 | `_remote_pullback_2026_10_17/results/familyL_prior_cache/project_management.json` | 1,895 | 2026-10-17 15:55:32 | `3467c1985133` | 成果面 |
| 2477 | `_remote_pullback_2026_10_17/results/gt2_attacker_cache/algorithm_process.json` | 2,783 | 2026-10-17 15:55:33 | `7ad7b97486e8` | 成果面 |
| 2478 | `_remote_pullback_2026_10_17/results/gt2_attacker_cache/biological_taxonomy.json` | 2,386 | 2026-10-17 15:55:33 | `f7c9a3344c54` | 成果面 |
| 2479 | `_remote_pullback_2026_10_17/results/gt2_attacker_cache/historical_causality.json` | 2,342 | 2026-10-17 15:55:34 | `b9f8f472b2f9` | 成果面 |
| 2480 | `_remote_pullback_2026_10_17/results/gt2_attacker_cache/physics_concepts.json` | 2,387 | 2026-10-17 15:55:35 | `ec91290fbddc` | 成果面 |
| 2481 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/deepseek-v4-pro-260425__algorithm_process.json` | 3,315 | 2026-10-17 15:55:35 | `fb255ad93ec9` | 成果面 |
| 2482 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/deepseek-v4-pro-260425__biological_taxonomy.json` | 2,564 | 2026-10-17 15:55:35 | `d50690ff2279` | 成果面 |
| 2483 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/deepseek-v4-pro-260425__geography_world.json` | 2,847 | 2026-10-17 15:55:36 | `7830ece1d516` | 成果面 |
| 2484 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/deepseek-v4-pro-260425__historical_causality.json` | 2,851 | 2026-10-17 15:55:36 | `d556c647747d` | 成果面 |
| 2485 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/deepseek-v4-pro-260425__physics_concepts.json` | 2,176 | 2026-10-17 15:55:37 | `8bc5467ced92` | 成果面 |
| 2486 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/deepseek-v4-pro-260425__project_management.json` | 2,083 | 2026-10-17 15:55:38 | `23863deac9a3` | 成果面 |
| 2487 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/doubao-seed-evolving__algorithm_process.json` | 498 | 2026-10-17 15:55:38 | `3e0173feb34d` | 成果面 |
| 2488 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/doubao-seed-evolving__biological_taxonomy.json` | 2,362 | 2026-10-17 15:55:39 | `f6db5e6b980f` | 成果面 |
| 2489 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/doubao-seed-evolving__geography_world.json` | 2,475 | 2026-10-17 15:55:39 | `4925ec2a5ca1` | 成果面 |
| 2490 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/doubao-seed-evolving__historical_causality.json` | 501 | 2026-10-17 15:55:40 | `aedf8a050cb3` | 成果面 |
| 2491 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/doubao-seed-evolving__physics_concepts.json` | 2,013 | 2026-10-17 15:55:40 | `6dd47c33fb27` | 成果面 |
| 2492 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/doubao-seed-evolving__project_management.json` | 1,719 | 2026-10-17 15:55:40 | `ebae449cf921` | 成果面 |
| 2493 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/kimi-k2-thinking__algorithm_process.json` | 479 | 2026-10-17 15:55:41 | `669da0e1c36b` | 成果面 |
| 2494 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/kimi-k2-thinking__biological_taxonomy.json` | 2,350 | 2026-10-17 15:55:41 | `51746e4094dc` | 成果面 |
| 2495 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/kimi-k2-thinking__geography_world.json` | 2,499 | 2026-10-17 15:55:42 | `29cce1102bba` | 成果面 |
| 2496 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/kimi-k2-thinking__historical_causality.json` | 2,500 | 2026-10-17 15:55:42 | `9506ad922380` | 成果面 |
| 2497 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/kimi-k2-thinking__physics_concepts.json` | 2,006 | 2026-10-17 15:55:43 | `bd828a9e748b` | 成果面 |
| 2498 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/kimi-k2-thinking__project_management.json` | 480 | 2026-10-17 15:55:44 | `540a9ef09bf0` | 成果面 |
| 2499 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/moonshot-v1-8k__algorithm_process.json` | 2,737 | 2026-10-17 15:55:44 | `b0dc14fac249` | 成果面 |
| 2500 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/moonshot-v1-8k__biological_taxonomy.json` | 2,324 | 2026-10-17 15:55:45 | `769991471ad1` | 成果面 |
| 2501 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/moonshot-v1-8k__geography_world.json` | 2,495 | 2026-10-17 15:55:45 | `b7cce4938263` | 成果面 |
| 2502 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/moonshot-v1-8k__historical_causality.json` | 2,649 | 2026-10-17 15:55:46 | `202e2e38a573` | 成果面 |
| 2503 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/moonshot-v1-8k__physics_concepts.json` | 2,540 | 2026-10-17 15:55:46 | `6081c483c999` | 成果面 |
| 2504 | `_remote_pullback_2026_10_17/results/gt3_prior_cache/moonshot-v1-8k__project_management.json` | 478 | 2026-10-17 15:55:47 | `8896856f7e65` | 成果面 |
| 2505 | `_remote_pullback_2026_10_17/results/llm_prior_cache.json` | 938 | 2026-10-17 15:55:47 | `5f16be89efc5` | 成果面 |
| 2506 | `_remote_pullback_2026_10_17/results/llm_prior_cache_v18_contamination.json` | 639 | 2026-10-17 15:55:48 | `d3f72f67977d` | 成果面 |
| 2507 | `_remote_pullback_2026_10_17/results/llm_prior_cache_v18_contentless.json` | 512 | 2026-10-17 15:55:48 | `7c0d169ef164` | 成果面 |
| 2508 | `_remote_pullback_2026_10_17/results/llm_prior_cache_v18_direction.json` | 2,168 | 2026-10-17 15:55:49 | `023f936f80fb` | 成果面 |
| 2509 | `_remote_pullback_2026_10_17/results/llm_prior_cache_v18_direction_run1_malformed_archive.json` | 655 | 2026-10-17 15:55:49 | `d5526e712e99` | 成果面 |
| 2510 | `_remote_pullback_2026_10_17/results/llm_prior_cache_v18_labelshuffle.json` | 1,925 | 2026-10-17 15:55:50 | `8dce6d7618a2` | 成果面 |
| 2511 | `_remote_pullback_2026_10_17/results/MANIFEST_large_files.md` | 3,816 | 2026-10-17 15:55:18 | `b138fb94ca71` | 成果面 |
| 2512 | `_remote_pullback_2026_10_17/results/v19_edges_audit_input.csv` | 2,186 | 2026-10-17 15:55:50 | `8b6682181392` | 成果面 |
| 2513 | `_remote_pullback_2026_10_17/results/v20_graph_features.csv` | 2,151 | 2026-10-17 15:55:50 | `f95f382ace44` | 成果面 |
| 2514 | `_remote_pullback_2026_10_17/results/v20_regression_field_v2.json` | 4,236 | 2026-10-17 15:55:51 | `3596490e1fc0` | 成果面 |
| 2515 | `_remote_pullback_2026_10_17/results/v20_statcheck_fm_vs_deg.json` | 988 | 2026-10-17 15:55:51 | `dfe014c627ca` | 成果面 |
| 2516 | `_remote_pullback_2026_10_17/results/v20_statcheck_fm_vs_rand.json` | 868 | 2026-10-17 15:55:52 | `1dadfaeb2c43` | 成果面 |
| 2517 | `_u5_inventory_tmp.txt` | 512 | 2026-10-12 16:32:55 | `652fa403b4a0` | 成果面 |
| 2518 | `_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` | 26,633 | 2026-09-26 19:13:56 | `739245682d40` | 成果面 |
| 2519 | `_v5_gt_exec_2026_09_29.py` | 75,689 | 2026-09-29 11:17:03 | `eef7b446cc0e` | 成果面 |
| 2520 | `attacks/__init__.py` | 183 | 2026-09-01 11:19:18 | `d11e085d9ecc` | 成果面 |
| 2521 | `attacks/a1_delete_anchor.py` | 4,693 | 2026-09-04 13:11:07 | `78ac391d16fc` | 成果面 |
| 2522 | `attacks/a2_reshuffle_manifest.py` | 3,792 | 2026-09-01 11:19:34 | `3d54b277620e` | 成果面 |
| 2523 | `attacks/a3_rewrite_runs.py` | 4,254 | 2026-09-01 16:31:25 | `f02b3eee8d6e` | 成果面 |
| 2524 | `audits_dataset_health.json` | 7,398 | 2026-08-28 15:53:27 | `4f827071b0b8` | 成果面 |
| 2525 | `audits_outliers.json` | 132,875 | 2026-08-28 15:53:28 | `3b1c881c4594` | 成果面 |
| 2526 | `audits_security.json` | 1,610 | 2026-08-28 15:52:30 | `553c90aa3ba6` | 成果面 |
| 2527 | `corpus/v20/all.json` | 2,557 | 2026-09-17 10:24:31 | `8df31c95b1fc` | 成果面 |
| 2528 | `corpus/v20/by_model/coze/coze_artifact_v_2026_09_16.json` | 10,978 | 2026-09-24 11:28:03 | `fee04170aa73` | 成果面 |
| 2529 | `corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json` | 19,685 | 1979-11-30 00:00:00 | `268ab1239a8a` | 成果面 |
| 2530 | `corpus/v20/by_model/GLM_2/glm_artifact_v_2026_09_16.json` | 13,150 | 1979-11-30 00:00:00 | `39732a92b5c9` | 成果面 |
| 2531 | `corpus/v20/by_model/kimi/index_v2_2026_09_16.json` | 24,150 | 2026-09-16 18:39:54 | `efe05ad775de` | 成果面 |
| 2532 | `corpus/v20/by_model/minimax/artifact_v_2026_09_16.json` | 25,347 | 2026-09-16 18:20:56 | `9e1ccbdceacc` | 成果面 |
| 2533 | `corpus/v20/index.json` | 7,335 | 2026-08-28 23:53:05 | `8423ffe266af` | 成果面 |
| 2534 | `corpus/v20/index_v2_2026_09_16.json` | 24,150 | 2026-09-16 18:39:54 | `efe05ad775de` | 成果面 |
| 2535 | `corpus/v20/index_v3_2026_09_29.json` | 24,421 | 2026-10-01 09:43:44 | `3ba2449cf986` | 成果面 |
| 2536 | `corpus/v20/index_v3_2026_10_09.json` | 24,837 | 2026-10-09 13:39:49 | `74b27393574f` | 成果面 |
| 2537 | `corpus/v20/L_algorithm_process.json` | 3,920 | 2026-08-28 17:38:45 | `ff0ef9131fdd` | 成果面 |
| 2538 | `corpus/v20/L_biological_taxonomy.json` | 3,562 | 2026-08-28 17:38:45 | `0c7ad5235ae9` | 成果面 |
| 2539 | `corpus/v20/L_geography_world.json` | 3,699 | 2026-08-28 23:11:44 | `77b0c1466dc0` | 成果面 |
| 2540 | `corpus/v20/L_historical_causality.json` | 4,329 | 2026-08-28 17:38:45 | `12e0de4bb103` | 成果面 |
| 2541 | `corpus/v20/L_physics_concepts.json` | 3,397 | 2026-08-28 17:38:45 | `d8780859d310` | 成果面 |
| 2542 | `corpus/v20/L_project_management.json` | 3,898 | 2026-08-28 23:12:37 | `32ca32c00da4` | 成果面 |
| 2543 | `corpus/v20/S1.json` | 1,512 | 2026-08-28 17:07:51 | `a890c56f7705` | 成果面 |
| 2544 | `corpus/v20/S1_n35.json` | 2,521 | 2026-08-28 17:07:52 | `f035043bfddd` | 成果面 |
| 2545 | `corpus/v20/S1_n45.json` | 3,171 | 2026-08-28 17:07:52 | `52b4d6e52ae9` | 成果面 |
| 2546 | `corpus/v20/S1_n60.json` | 4,122 | 2026-08-28 17:07:52 | `584de37ebec1` | 成果面 |
| 2547 | `corpus/v20/S2.json` | 2,234 | 2026-08-28 17:07:52 | `b1f6c5aa4de6` | 成果面 |
| 2548 | `corpus/v20/S2_n20.json` | 1,537 | 2026-08-28 17:07:52 | `bfc9d38c8c0f` | 成果面 |
| 2549 | `corpus/v20/S2_n35.json` | 2,480 | 2026-08-28 17:07:52 | `e20a1bbeaee7` | 成果面 |
| 2550 | `corpus/v20/S2_n45.json` | 3,175 | 2026-08-28 17:07:52 | `58bb0a7d2e46` | 成果面 |
| 2551 | `corpus/v20/S2_n60.json` | 4,123 | 2026-08-28 17:07:52 | `01c492a97b98` | 成果面 |
| 2552 | `corpus/v20/S3.json` | 2,297 | 2026-08-28 17:07:52 | `3b6879ab2440` | 成果面 |
| 2553 | `corpus/v20/S4.json` | 4,932 | 2026-08-28 17:07:52 | `e6045f0920ec` | 成果面 |
| 2554 | `corpus/v20/S5.json` | 3,319 | 2026-08-28 17:07:52 | `4b10f9cae09f` | 成果面 |
| 2555 | `corpus/v20/S6.json` | 3,320 | 2026-08-28 17:07:52 | `01d9c95ea690` | 成果面 |
| 2556 | `corpus/v20/S6_n20.json` | 1,724 | 2026-08-28 17:07:52 | `4a0689892c1b` | 成果面 |
| 2557 | `corpus/v20/S6_n35.json` | 2,676 | 2026-08-28 17:07:52 | `8d02fbadd277` | 成果面 |
| 2558 | `corpus/v20/S6_n60.json` | 4,296 | 2026-08-28 17:07:52 | `704e2fd0d021` | 成果面 |
| 2559 | `corpus/v20/strip_captions_22.json` | 12,798 | 2026-09-11 11:33:40 | `6a2656878745` | 成果面 |
| 2560 | `corpus/v20_caption_surface/_inspect_captions.py` | 591 | 2026-09-10 17:31:00 | `dfb02ade1474` | 成果面 |
| 2561 | `corpus/v20_caption_surface/_p_d_b3_merkle_22caption_runner_2026_09_16.py` | 18,596 | 2026-09-16 18:54:48 | `d2cd7acb29a1` | 成果面 |
| 2562 | `corpus/v20_caption_surface/_p_d_v03_22caption_verification_20260917_163757.json` | 13,775 | 2026-09-17 16:37:57 | `dfbcc5d6fc34` | 成果面 |
| 2563 | `corpus/v20_caption_surface/_v41_flash_rag_caption_embs.bak.json` | 612,511 | 2026-09-10 17:05:53 | `25f745609658` | 成果面 |
| 2564 | `corpus/v20_caption_surface/caption_distance_mat_22.json` | 8,552 | 2026-09-23 16:44:30 | `1c4fff004cc4` | 成果面 |
| 2565 | `corpus/v20_caption_surface/caption_features_22.json` | 18,362 | 2026-09-23 16:44:30 | `727a253566dd` | 成果面 |
| 2566 | `corpus/v20_caption_surface/caption_stats_22.json` | 632 | 2026-09-23 16:44:30 | `da34f54d4f5b` | 成果面 |
| 2567 | `corpus/v20_caption_surface/manifest.json` | 1,477 | 2026-09-23 16:44:30 | `4fdda6480bb5` | 成果面 |
| 2568 | `corpus/v20_caption_surface/strip_captions_22.json` | 12,798 | 2026-09-11 11:33:40 | `6a2656878745` | 成果面 |
| 2569 | `deposon_agents.py` | 104,622 | 2026-09-18 13:41:44 | `5496954b0ad5` | 成果面 |
| 2570 | `deposon_agents_v1_3.py` | 1,827 | 2026-08-30 10:23:11 | `715026b48678` | 成果面 |
| 2571 | `deposon_agents_v1_4.py` | 1,726 | 2026-08-30 10:23:11 | `59f0ce83e06d` | 成果面 |
| 2572 | `deposon_diffusion.py` | 19,171 | 2026-08-30 04:52:41 | `fe4d668eb1da` | 成果面 |
| 2573 | `deposon_fast.py` | 4,581 | 2026-08-30 04:53:24 | `7a2dcbadac73` | 成果面 |
| 2574 | `deposon_g2_modes.py` | 6,316 | 2026-08-23 09:33:59 | `6a175a264b46` | 成果面 |
| 2575 | `deposon_photonics.py` | 10,402 | 2026-08-29 00:34:47 | `c7e78ad9f030` | 成果面 |
| 2576 | `deposon_protocol.py` | 2,845 | 2026-08-30 04:55:56 | `ca756668ce2e` | 成果面 |
| 2577 | `deposon_team/plugins/_dfr_s1_2026_10_12.py` | 5,327 | 2026-10-12 17:21:53 | `b003e57c14f7` | 成果面 |
| 2578 | `deposon_team/plugins/_dfr_s2_2026_10_12.py` | 4,499 | 2026-10-12 17:23:44 | `745c1a86c868` | 成果面 |
| 2579 | `deposon_team/plugins/_ofc_s1_2026_10_12.py` | 5,667 | 2026-10-12 11:55:57 | `bb7b9faa547a` | 成果面 |
| 2580 | `deposon_team/plugins/_ofc_s1b_2026_10_12.py` | 4,684 | 2026-10-12 11:58:39 | `0bf02827c1d9` | 成果面 |
| 2581 | `deposon_team/plugins/_ofc_s2_2026_10_12.py` | 3,960 | 2026-10-12 12:00:36 | `0ac81224ac7f` | 成果面 |
| 2582 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_fix_2026_10_10.py` | 33,994 | 2026-10-10 11:23:01 | `341b6726ac4e` | 成果面 |
| 2583 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_rename_2026_10_10.py` | 35,321 | 2026-10-10 11:23:01 | `cd43c41716f0` | 成果面 |
| 2584 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_selfverify_fix_2026_10_10.py` | 31,457 | 2026-10-10 10:50:15 | `041525fd05a2` | 成果面 |
| 2585 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py` | 20,322 | 2026-09-29 13:43:09 | `de16bc002198` | 成果面 |
| 2586 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py` | 21,826 | 2026-10-09 13:38:37 | `7c095c54fb99` | 成果面 |
| 2587 | `deposon_team/plugins/_pg_v01_compute.py` | 20,923 | 2026-09-16 18:54:48 | `d511c545f88e` | 成果面 |
| 2588 | `deposon_team/plugins/_tdf_s1_2026_10_12.py` | 5,856 | 2026-10-12 01:23:22 | `5f9ab0ad7bab` | 成果面 |
| 2589 | `deposon_team/plugins/_tdf_s1b_2026_10_12.py` | 8,064 | 2026-10-12 01:24:29 | `bebba19790c0` | 成果面 |
| 2590 | `deposon_team/plugins/_tdf_s1c_2026_10_12.py` | 7,485 | 2026-10-12 01:26:27 | `d8bd9c41194a` | 成果面 |
| 2591 | `deposon_team/plugins/_tdf_s2_apply_2026_10_12.py` | 10,899 | 2026-10-12 01:29:57 | `4bd6d16e20d7` | 成果面 |
| 2592 | `deposon_team/plugins/_tdf_s3_jumps_2026_10_12.py` | 676 | 2026-10-12 01:30:39 | `16f7e10ac78f` | 成果面 |
| 2593 | `deposon_team/plugins/_tdf_s3b_2026_10_12.py` | 1,229 | 2026-10-12 01:31:26 | `ccec66bb426e` | 成果面 |
| 2594 | `deposon_team/plugins/_tdf_s4_final_2026_10_12.py` | 2,695 | 2026-10-12 01:34:23 | `1df9a5d22e42` | 成果面 |
| 2595 | `deposon_team/plugins/_v3_construct_diag_2026_09_23.py` | 22,490 | 2026-09-23 14:20:25 | `ce10a3dbcb2b` | 成果面 |
| 2596 | `deposon_team/plugins/_v3_review_r1_inventory_2026_09_23.py` | 5,526 | 2026-09-23 13:13:02 | `7b97ef02c52e` | 成果面 |
| 2597 | `deposon_team/plugins/_v3_review_r1b_2026_09_23.py` | 1,795 | 2026-09-23 13:13:45 | `b5e77e114d88` | 成果面 |
| 2598 | `deposon_team/plugins/_v3_review_r1c_2026_09_23.py` | 2,919 | 2026-09-23 13:14:27 | `fdfeb03e8d6f` | 成果面 |
| 2599 | `deposon_team/plugins/_v3_review_r1d_2026_09_23.py` | 1,712 | 2026-09-23 13:14:59 | `4adbd9b5eab5` | 成果面 |
| 2600 | `deposon_team/plugins/_v3_review_r2_verify_2026_09_23.py` | 4,528 | 2026-09-23 13:24:40 | `aee06c009ed1` | 成果面 |
| 2601 | `deposon_team/plugins/_v3_review_r2b_2026_09_23.py` | 3,189 | 2026-09-23 13:25:02 | `9d6343bd9755` | 成果面 |
| 2602 | `deposon_team/plugins/_v3_review_r2c_2026_09_23.py` | 4,400 | 2026-09-23 13:25:39 | `1c30cda5aad6` | 成果面 |
| 2603 | `deposon_team/plugins/_v3_review_r3_sha_2026_09_23.py` | 1,881 | 2026-09-23 13:26:41 | `d3b45b64c0da` | 成果面 |
| 2604 | `deposon_team/plugins/_v3_review_r4_fixscan_2026_09_23.py` | 3,896 | 2026-09-23 13:31:36 | `917b18eb9a5f` | 成果面 |
| 2605 | `deposon_team/plugins/_v3_review_r5_anchor_probe_2026_09_23.py` | 2,653 | 2026-09-23 13:33:00 | `7ebe0f65a64a` | 成果面 |
| 2606 | `deposon_team/plugins/_v3_review_r6_final_sha_2026_09_23.py` | 2,135 | 2026-09-23 13:34:47 | `8af3f4460144` | 成果面 |
| 2607 | `deposon_team/plugins/_v3_review_r7_fix_e15_2026_09_23.py` | 2,951 | 2026-09-23 13:39:17 | `40d66379ef17` | 成果面 |
| 2608 | `deposon_team/plugins/_v3_review_r8_precise_scan_2026_09_23.py` | 5,241 | 2026-09-23 13:44:30 | `2ff60f715def` | 成果面 |
| 2609 | `deposon_team/plugins/_v3_review_r9_final_state_2026_09_23.py` | 2,117 | 2026-09-23 13:46:51 | `fcf5baf4dd7f` | 成果面 |
| 2610 | `deposon_team/plugins/_v3n_cpath_live_2026_09_27.py` | 19,823 | 2026-09-27 14:16:12 | `5248ba7ac21c` | 成果面 |
| 2611 | `deposon_team/plugins/_v3n_cpath_live_r1_2026_09_27.py` | 28,187 | 2026-09-27 20:54:38 | `321d39c7df41` | 成果面 |
| 2612 | `deposon_team/plugins/_v3n_cpath_live_rerun_2026_10_01.py` | 22,133 | 2026-10-01 14:02:02 | `7d8d26174ce9` | 成果面 |
| 2613 | `deposon_team/plugins/_v3n_ktb1_distortion_bound_2026_09_27.py` | 13,055 | 2026-09-27 14:16:59 | `5572ef4055a5` | 成果面 |
| 2614 | `deposon_team/plugins/_v3n_pg_boss_live_2026_09_27.py` | 14,223 | 2026-09-27 14:15:38 | `b6040d34f0ac` | 成果面 |
| 2615 | `deposon_team/plugins/_v3r1p1_21_ktb1_distortion_2026_09_27.py` | 30,672 | 2026-09-27 16:35:23 | `f7b61f041c0b` | 成果面 |
| 2616 | `deposon_team/plugins/_v3r1p1_35_gt2b_bankseed_2026_09_27.py` | 26,734 | 2026-09-27 16:23:05 | `62353279cd0c` | 成果面 |
| 2617 | `deposon_team/plugins/_v3x_frozen_schema_v1.json` | 12,919 | 2026-09-17 10:27:19 | `9e99dcc4d920` | 成果面 |
| 2618 | `deposon_team/plugins/_v4_contrast_nondegenerate_2026_09_23.py` | 42,876 | 2026-09-23 16:06:11 | `a0bfc7df887f` | 成果面 |
| 2619 | `deposon_team/plugins/_v4_wide_s1_inventory_2026_09_27.py` | 1,669 | 2026-09-27 20:18:35 | `145ae518f5f0` | 成果面 |
| 2620 | `deposon_team/plugins/_v4_wide_s5_prescan_2026_09_27.py` | 2,839 | 2026-09-27 20:25:46 | `724964301582` | 成果面 |
| 2621 | `deposon_team/plugins/_v4_wt_apply_b4_2026_09_27.py` | 6,113 | 2026-09-27 20:10:30 | `fd0a08029841` | 成果面 |
| 2622 | `deposon_team/plugins/_v4_wt_s0_verify_2026_09_27.py` | 8,462 | 2026-09-27 20:02:03 | `4dcb81343577` | 成果面 |
| 2623 | `deposon_team/plugins/_v4_wt_s2_b1diff_2026_09_27.py` | 2,015 | 2026-09-27 20:02:28 | `b61cb447f306` | 成果面 |
| 2624 | `deposon_team/plugins/_v4_wt_s2_b1recheck_2026_09_27.py` | 5,650 | 2026-09-27 20:03:23 | `e643ac7f9718` | 成果面 |
| 2625 | `deposon_team/plugins/_v4_wt_s3_b2probe_2026_09_27.py` | 6,089 | 2026-09-27 20:08:43 | `a5db027adac5` | 成果面 |
| 2626 | `deposon_team/plugins/_v4_wt_s3b_b2confirm_2026_09_27.py` | 3,604 | 2026-09-27 20:09:01 | `7aaf6f21d459` | 成果面 |
| 2627 | `deposon_team/plugins/_v4_wt_s4_b4verify_2026_09_27.py` | 2,595 | 2026-09-27 20:09:38 | `5e1ec533de1f` | 成果面 |
| 2628 | `deposon_team/plugins/_v4_wt_s4b_b4recompute_2026_09_27.py` | 4,174 | 2026-09-27 20:09:59 | `edcdfda20f91` | 成果面 |
| 2629 | `deposon_team/plugins/_v4_wt_s4c_regonly_2026_09_27.py` | 3,900 | 2026-09-27 20:10:57 | `20f265761280` | 成果面 |
| 2630 | `deposon_team/plugins/_v4_wt_s6_final_2026_09_27.py` | 3,435 | 2026-09-27 20:13:00 | `653077d03468` | 成果面 |
| 2631 | `deposon_team/plugins/_v5_gt8_lowarm_2026_09_29.py` | 57,033 | 2026-09-29 15:28:35 | `9b21988afff7` | 成果面 |
| 2632 | `deposon_team/plugins/_v5_gt8_lowarm_setA_2026_09_29.py` | 43,224 | 2026-09-29 15:27:05 | `f72f062f6b67` | 成果面 |
| 2633 | `deposon_team/plugins/_v5_gt8_lowarm_seta_verify_2026_09_29.py` | 15,553 | 2026-09-29 15:33:15 | `bed2d444c196` | 成果面 |
| 2634 | `deposon_team/plugins/_v5_item21_strategyqa_realias_2026_09_29.py` | 25,482 | 2026-09-29 16:15:43 | `aaaae1f02815` | 成果面 |
| 2635 | `deposon_team/plugins/_v5_item35_v2_matrix_2026_09_29.py` | 44,777 | 2026-09-29 12:23:55 | `ef73f9b90afc` | 成果面 |
| 2636 | `deposon_team/plugins/_v5_item35_v3_collinear_2026_09_29.py` | 63,376 | 2026-09-29 14:21:40 | `7115928822a1` | 成果面 |
| 2637 | `deposon_team/plugins/_v5_pp1_pattern_fix_2026_09_29.py` | 22,544 | 2026-09-29 17:31:40 | `e3cf9d552f30` | 成果面 |
| 2638 | `deposon_team/plugins/_v5_wa_s2_2026_09_30.py` | 5,812 | 2026-09-30 19:03:02 | `88cd82e65627` | 成果面 |
| 2639 | `deposon_team/plugins/_v5_wa_s4_2026_09_30.py` | 2,063 | 2026-09-30 19:07:54 | `2e7743dd8139` | 成果面 |
| 2640 | `deposon_team/plugins/_v5r_s40_rerun_executor_fix_2026_09_29.py` | 17,665 | 2026-09-29 19:19:06 | `a4ae5d5f19c8` | 成果面 |
| 2641 | `deposon_team/plugins/_verify_15frozen.py` | 3,905 | 2026-09-17 10:12:02 | `efae9274962e` | 成果面 |
| 2642 | `deposon_team/plugins/_verify_15frozen_v1.py` | 2,094 | 2026-09-17 10:27:53 | `60523e406055` | 成果面 |
| 2643 | `deposon_team/plugins/_verify_batch5_2026_09_18.py` | 4,238 | 2026-09-18 13:45:30 | `bc6cbf27a338` | 成果面 |
| 2644 | `deposon_team/plugins/_verify_pg_v0.py` | 3,978 | 2026-09-17 10:12:02 | `cdd3415ad993` | 成果面 |
| 2645 | `deposon_team/plugins/_verify_pg_v0_v1.py` | 2,521 | 2026-09-17 10:27:53 | `67088ae1a860` | 成果面 |
| 2646 | `deposon_team/plugins/boss_pa_1_rbr_rm.py` | 17,743 | 2026-09-15 15:16:26 | `5cc594147e00` | 成果面 |
| 2647 | `deposon_team/plugins/boss_pa_1_rbr_rm_v3df_ab_alpha_2026_10_09.py` | 45,777 | 2026-10-09 22:54:53 | `06016f90fd3a` | 成果面 |
| 2648 | `deposon_team/plugins/boss_pa_1_rbr_rm_v3df_ab_beta_2026_10_09.py` | 47,580 | 2026-10-09 22:59:41 | `3524e454d8ed` | 成果面 |
| 2649 | `deposon_team/plugins/boss_pa_1_rbr_rm_v3df_c1c4_2026_09_29.py` | 61,102 | 2026-09-29 12:05:45 | `7761f2c339e6` | 成果面 |
| 2650 | `deposon_team/plugins/boss_pa_1_rbr_rm_v3df_p1_reopen_2026_09_29.py` | 91,135 | 2026-09-29 13:40:58 | `77724bce0c06` | 成果面 |
| 2651 | `deposon_team/plugins/boss_pa_2_potential_game.py` | 10,410 | 2026-09-15 15:16:26 | `33dfb4338c53` | 成果面 |
| 2652 | `deposon_team/plugins/boss_pa_3_replicator_dynamics.py` | 12,900 | 2026-09-15 15:16:26 | `a2bd9dd24c25` | 成果面 |
| 2653 | `deposon_team/plugins/boss_pc_1_2d_ising_universality.py` | 7,547 | 2026-09-15 15:37:54 | `bfc319808447` | 成果面 |
| 2654 | `deposon_team/plugins/boss_pc_2_transverse_field_ising.py` | 7,053 | 2026-09-15 15:37:54 | `210105a7f29a` | 成果面 |
| 2655 | `deposon_team/plugins/boss_pc_3_reservoir_computing.py` | 7,373 | 2026-09-15 15:37:54 | `021ea39b7193` | 成果面 |
| 2656 | `deposon_team/plugins/boss_pg_1_riemannian_degenerate.py` | 5,996 | 2026-09-15 15:37:53 | `97fede6c8a4e` | 成果面 |
| 2657 | `deposon_team/plugins/boss_pg_2_hyperbolic_classification_collapse.py` | 5,285 | 2026-09-15 15:37:53 | `f006d4caca94` | 成果面 |
| 2658 | `deposon_team/plugins/boss_pg_3_geodesic_violation.py` | 5,517 | 2026-09-15 15:37:54 | `09f37c01a258` | 成果面 |
| 2659 | `deposon_team/plugins/github_dir_structure_2026_09_18.md` | 11,675 | 2026-09-15 15:17:42 | `0fd07ad38282` | 成果面 |
| 2660 | `deposon_team/plugins/github_upload_2026_09_18.sh` | 6,030 | 2026-09-15 15:18:06 | `52bc19845b2b` | 成果面 |
| 2661 | `deposon_team/plugins/skill_a_p_a_60cells.py` | 9,078 | 2026-09-11 17:05:38 | `b1463bb24403` | 成果面 |
| 2662 | `deposon_team/plugins/skill_b_p_c_alpha_beta.py` | 8,699 | 2026-09-11 17:05:38 | `e5a299f69a22` | 成果面 |
| 2663 | `deposon_team/plugins/skill_c_p_e_3modality.py` | 8,915 | 2026-09-11 17:05:38 | `e19e76c5da7e` | 成果面 |
| 2664 | `deposon_team/plugins/skill_d_p_f_observer.py` | 15,927 | 2026-09-15 13:30:57 | `3e369a1f6171` | 成果面 |
| 2665 | `docs/BASELINE_REGISTRY.md` | 3,356 | 2026-08-28 20:59:38 | `51b271548835` | 成果面 |
| 2666 | `docs/CLOSURE_v19_and_v2X_gametheory.md` | 9,065 | 2026-08-28 15:55:51 | `84323775a212` | 成果面 |
| 2667 | `docs/Findings_GT2B.md` | 3,322 | 2026-08-29 20:00:21 | `e6cc74f9917d` | 成果面 |
| 2668 | `docs/Findings_GT3.md` | 2,632 | 2026-08-29 15:06:30 | `4f3242b2a661` | 成果面 |
| 2669 | `docs/Findings_GT8.md` | 3,890 | 2026-08-29 19:36:27 | `869c0071fbc2` | 成果面 |
| 2670 | `docs/Findings_GT8B.md` | 9,809 | 2026-08-30 10:38:41 | `956183753a2e` | 成果面 |
| 2671 | `docs/Findings_GT_FORMAL.md` | 6,345 | 2026-08-30 15:45:12 | `fab607f0e180` | 成果面 |
| 2672 | `docs/Findings_v2.0.md` | 4,364 | 2026-08-28 17:44:22 | `7e5dc4b045d8` | 成果面 |
| 2673 | `docs/Findings_v2.0_bigquiz.md` | 3,291 | 2026-08-28 23:55:23 | `d4ed18152dc0` | 成果面 |
| 2674 | `docs/Findings_v2.0_boss.md` | 3,642 | 2026-08-28 21:16:05 | `36c714eabe3b` | 成果面 |
| 2675 | `docs/Findings_v2.0_corrections.md` | 5,012 | 2026-08-29 01:23:08 | `5864bbe5adae` | 成果面 |
| 2676 | `docs/Findings_v2.0_crossval.md` | 4,566 | 2026-08-28 20:28:59 | `32d26cb09568` | 成果面 |
| 2677 | `docs/Findings_v2.0_hardening.md` | 3,563 | 2026-08-28 22:49:38 | `a7f479793f01` | 成果面 |
| 2678 | `docs/Findings_v2.0_photonics.md` | 4,377 | 2026-08-30 04:46:02 | `9158f54ec248` | 成果面 |
| 2679 | `docs/Findings_v2.0_skills.md` | 3,456 | 2026-08-28 20:47:31 | `43731392b581` | 成果面 |
| 2680 | `docs/GT_FORMALIZATION_v1.md` | 19,100 | 2026-08-30 15:45:39 | `aeefb8ef6972` | 成果面 |
| 2681 | `docs/GT_RECONSTRUCTION.md` | 13,424 | 2026-09-28 22:57:17 | `cff15d000d47` | 成果面 |
| 2682 | `docs/PAPER_BRIEF.md` | 11,296 | 2026-08-30 11:09:37 | `de450c0beffa` | 成果面 |
| 2683 | `docs/REF_VERIFICATION_v2.md` | 5,860 | 2026-08-30 11:17:21 | `64f0a3772c12` | 成果面 |
| 2684 | `docs/REFACTOR_v2.md` | 23,042 | 2026-08-30 10:39:00 | `03c8baa18d93` | 成果面 |
| 2685 | `docs/simple_baseline_failure_analysis.md` | 6,080 | 2026-08-23 00:01:28 | `968776002868` | 成果面 |
| 2686 | `docs/space_release_log.json` | 5,056 | 2026-08-28 23:54:50 | `110607514753` | 成果面 |
| 2687 | `docs/SPEC_GT2B.md` | 3,318 | 2026-08-29 19:56:29 | `68a5b08ef007` | 成果面 |
| 2688 | `docs/SPEC_GT3.md` | 5,369 | 2026-08-29 14:09:52 | `432ec337d586` | 成果面 |
| 2689 | `docs/SPEC_GT8.md` | 4,181 | 2026-08-29 19:40:49 | `edf6f4465ead` | 成果面 |
| 2690 | `docs/SPEC_GT8B.md` | 7,486 | 2026-08-30 10:37:50 | `3545c01e1291` | 成果面 |
| 2691 | `docs/SPEC_GT8C.md` | 6,326 | 2026-08-30 15:50:15 | `6b09de9911c0` | 成果面 |
| 2692 | `docs/SPEC_v1.8.md` | 9,850 | 2026-08-23 23:19:47 | `ad0e445714d9` | 成果面 |
| 2693 | `docs/SPEC_v2.0.md` | 5,333 | 2026-08-28 16:54:47 | `bac61d51fd20` | 成果面 |
| 2694 | `docs/SPEC_v2.0_amendment1.md` | 4,743 | 2026-08-29 01:22:16 | `3e3a5014cb0e` | 成果面 |
| 2695 | `docs/SYNTHESIS_mind_game.md` | 9,191 | 2026-08-29 00:22:08 | `0f36aaeeda6f` | 成果面 |
| 2696 | `docs/V3X/KT_B1_REWORK_REPORT_2026_09_10.md` | 11,478 | 2026-09-10 12:05:42 | `baef94e393de` | 成果面 |
| 2697 | `docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md` | 19,751 | 2026-09-15 11:31:34 | `977fe1b48f75` | 成果面 |
| 2698 | `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | 15,457 | 2026-09-30 20:36:51 | `423c84de20d5` | 成果面 |
| 2699 | `docs/V3X/P_C_D1_D3_REPORT_2026_09_15.md` | 13,419 | 2026-09-15 15:08:22 | `79c7321056b8` | 成果面 |
| 2700 | `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC.md` | 34,393 | 2026-09-17 15:15:44 | `f119f2f30287` | 成果面 |
| 2701 | `docs/V3X/P_E_DOUBAN_EMBEDDING_V0_SPEC.md` | 16,876 | 2026-09-08 21:56:01 | `6f3c550cec13` | 成果面 |
| 2702 | `docs/V3X/P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md` | 12,501 | 2026-09-15 11:33:11 | `2f0765a1d39d` | 成果面 |
| 2703 | `docs/V3X/PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md` | 4,587 | 2026-09-11 11:17:21 | `c165cd33a362` | 成果面 |
| 2704 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 857,551 | 2026-09-29 19:42:49 | `41f5f1689d09` | 成果面 |
| 2705 | `docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` | 38,545 | 2026-09-16 11:01:12 | `4a08521f8de1` | 成果面 |
| 2706 | `docs/variant_params_table.md` | 4,035 | 2026-08-23 00:01:28 | `25f90f106451` | 成果面 |
| 2707 | `fingerprint_v0.py` | 10,950 | 2026-09-01 16:36:32 | `c0c38007c4e8` | 成果面 |
| 2708 | `gt_common.py` | 3,601 | 2026-08-30 10:17:31 | `425b4b2f1c01` | 成果面 |
| 2709 | `letters/_alignment_reply_crossface_three_items_2026_10_12.md` | 7,892 | 2026-10-12 20:44:03 | `08b036588198` | 成果面 |
| 2710 | `letters/_c4_theory_scan_reply_claude_code_2026_09_30.md` | 27,894 | 2026-09-30 21:51:00 | `2166b37e5d2a` | 成果面 |
| 2711 | `letters/_claude_pending_pi_gaps_closeout_reply_2026_10_11.md` | 22,064 | 2026-10-11 23:40:53 | `f4defae83553` | 成果面 |
| 2712 | `letters/_codex_c4_values_followup_reply_2026_10_10.md` | 4,490 | 2026-10-10 16:02:26 | `97a35f8ae94c` | 成果面 |
| 2713 | `letters/_codex_c4_values_reply_2026_10_10.md` | 13,378 | 2026-10-10 13:49:24 | `8e4972352291` | 成果面 |
| 2714 | `letters/_codex_c4_values_unblock_reply_2026_10_10.md` | 21,486 | 2026-10-10 17:35:08 | `a975c7990cd8` | 成果面 |
| 2715 | `letters/_codex_theory_derivation_reply_2026_09_30.md` | 71,002 | 2026-09-30 23:52:12 | `7558eb1a5e34` | 成果面 |
| 2716 | `letters/_commission_c4_values_EN_2026_10_10.md` | 56,217 | 2026-10-10 13:14:46 | `a397621085d6` | 成果面 |
| 2717 | `letters/_commission_c4_values_EN_differences_exits_note_2026_10_10.md` | 7,817 | 2026-10-10 13:15:32 | `b20f25a66267` | 成果面 |
| 2718 | `letters/_commission_c4_values_followup_EN_2026_10_10.md` | 7,583 | 2026-10-10 14:31:49 | `abe0652ab00f` | 成果面 |
| 2719 | `letters/_commission_c4_values_unblock_EN_2026_10_10.md` | 10,244 | 2026-10-10 17:17:35 | `fde64a863b09` | 成果面 |
| 2720 | `letters/_commission_c4_values_unblock_EN_differences_exits_note_2026_10_10.md` | 3,139 | 2026-10-10 17:17:46 | `1c769e28f8f5` | 成果面 |
| 2721 | `letters/_commission_closeout_pack_paper_2026_10_09_v0.1.md` | 31,838 | 2026-10-12 10:22:09 | `60e41b588d36` | 成果面 |
| 2722 | `letters/_commission_codex_theory_derivation_EN_2026_09_30.md` | 66,754 | 2026-09-30 19:58:54 | `af50969bebe2` | 成果面 |
| 2723 | `letters/_commission_codex_theory_derivation_EN_v0.2_2026_09_30.md` | 82,016 | 2026-09-30 21:55:05 | `8b15f0957e0f` | 成果面 |
| 2724 | `letters/_commission_coze_〔IM〕_closeout_pack_2026_10_12.md` | 26,816 | 2026-10-12 21:18:56 | `7818cfe2d226` | 成果面 |
| 2725 | `letters/_commission_glm_dualtrack_paper_addendum_v0.2_2026_10_01.md` | 53,344 | 2026-10-01 21:19:36 | `758e1ef3de27` | 成果面 |
| 2726 | `letters/_commission_glm_dualtrack_paper_v0.5_2026_10_01.md` | 42,807 | 2026-10-01 11:48:26 | `d1650b14d89c` | 成果面 |
| 2727 | `letters/_commission_glm_dualtrack_paper_v0.6_2026_10_12.md` | 56,360 | 2026-10-12 13:49:53 | `6d1b14983555` | 成果面 |
| 2728 | `letters/_commission_glm_theory_derivation_2026_09_30.md` | 32,472 | 2026-09-30 19:49:06 | `344f5b9e0b08` | 成果面 |
| 2729 | `letters/_commission_kimi_upload_2026_10_01_v0.2.md` | 35,421 | 2026-10-01 20:38:35 | `a77f7d509285` | 成果面 |
| 2730 | `letters/_commission_kimi_upload_with_d7_2026_10_09_v0.3.md` | 36,763 | 2026-10-12 09:59:43 | `ae00f6fee19e` | 成果面 |
| 2731 | `letters/_commission_pending_pi_gaps_closeout_EN_2026_10_11.md` | 22,685 | 2026-10-11 22:27:45 | `0ce066e5eb3f` | 成果面 |
| 2732 | `letters/_commission_t2_t3_theory_inputs_2026_10_17.md` | 22,746 | 2026-10-17 15:05:39 | `393d71e51fbf` | 成果面 |
| 2733 | `letters/_commission_t2_t3_theory_inputs_copilot_agent_2026_10_17.md` | 23,919 | 2026-10-17 15:15:10 | `385003e41ce2` | 成果面 |
| 2734 | `letters/_commission_t2_t3_theory_inputs_grok_2026_10_17.md` | 23,906 | 2026-10-17 15:15:10 | `6922929bfda8` | 成果面 |
| 2735 | `letters/_commission_trae_dfamily_original_text_request_2026_10_12.md` | 13,767 | 2026-10-12 16:02:26 | `23bd2366e798` | 成果面 |
| 2736 | `letters/_commission_trae_direct_fix_2026_10_09_v0.1.md` | 37,262 | 2026-10-12 01:16:25 | `c50822b41539` | 成果面 |
| 2737 | `letters/_commission_trae_direct_fix_oct_full_coverage_2026_10_12.md` | 46,077 | 2026-10-12 03:18:02 | `60751abbeb3b` | 成果面 |
| 2738 | `letters/_dualtrack_paper_clue_book_v0.5_2026_10_01.md` | 109,614 | 2026-10-01 11:50:06 | `0fd7a26fc339` | 成果面 |
| 2739 | `letters/_dualtrack_paper_clue_book_v0.6_local_remote_2026_10_12.md` | 81,707 | 2026-10-12 13:57:59 | `8b2a6380edf1` | 成果面 |
| 2740 | `letters/_glm_commission_reply_request_2026_10_13.md` | 22,328 | 2026-10-13 09:31:53 | `2992b3917050` | 成果面 |
| 2741 | `letters/_internal_true_clue_book_2026_10_12.md` | 408,329 | 2026-10-12 14:25:59 | `355ea3c09461` | 成果面 |
| 2742 | `letters/_kimi_v4_t12_review_2026_09_20.md` | 6,644 | 2026-09-20 14:53:18 | `38070fd12f31` | 成果面 |
| 2743 | `letters/_kimi_v4_theme_reply_2026_09_20.md` | 7,372 | 2026-09-20 17:52:32 | `3e37352efb4b` | 成果面 |
| 2744 | `letters/_kimi_v4_theme_reply_2_brainstorm_2026_09_20.md` | 14,155 | 2026-09-20 21:11:34 | `bc14f47d927d` | 成果面 |
| 2745 | `letters/_letter_to_pi_upload_application_approval_2026_09_26.md` | 23,368 | 2026-09-26 21:29:31 | `76d0b60e6bdc` | 成果面 |
| 2746 | `letters/_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md` | 36,945 | 2026-09-26 20:45:07 | `512c73d45087` | 成果面 |
| 2747 | `letters/_letter_to_pi_upload_application_supplement_2026_09_26.md` | 9,151 | 2026-09-26 21:28:18 | `5346a361801b` | 成果面 |
| 2748 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 68,449 | 2026-09-26 21:07:20 | `44d9a1972a13` | 成果面 |
| 2749 | `letters/_minimax_feedback_log_bloat_2026_09_29.md` | 13,361 | 2026-09-29 22:56:25 | `79ff4043169a` | 成果面 |
| 2750 | `letters/_oct_full_coverage_reply_trae_code_2026_10_12.md` | 23,978 | 2026-10-12 12:31:43 | `d11d75ba6236` | 成果面 |
| 2751 | `letters/_trae_dfamily_original_text_reply_2026_10_12.md` | 48,304 | 2026-10-12 17:32:26 | `ce91320d4f28` | 成果面 |
| 2752 | `letters/_trae_direct_fix_reply_trae_code_2026_10_12.md` | 21,379 | 2026-10-12 01:34:03 | `f37ebc80d1df` | 成果面 |
| 2753 | `letters/_v3_calibration_change_note_for_coze_glm_2026_09_27.md` | 42,948 | 2026-09-27 20:43:21 | `dda07ad77910` | 成果面 |
| 2754 | `letters/_v3_recheck_indep_judgment_request_2026_09_27.md` | 22,702 | 2026-09-27 16:18:21 | `2c486c1791d5` | 成果面 |
| 2755 | `letters/_v4_acceptance_coze_2026_09_20.md` | 5,467 | 2026-09-20 14:58:15 | `b2bf2a073ac8` | 成果面 |
| 2756 | `letters/_v4_acceptance_trae_code_2026_09_20.md` | 7,746 | 2026-09-30 16:14:47 | `3e2f1c84e86d` | 成果面 |
| 2757 | `letters/_v4_acceptance_trae_work_v1.0_2026_09_20.md` | 7,176 | 2026-09-20 17:36:19 | `3caf4e653a68` | 成果面 |
| 2758 | `letters/_v4_attribution_errata_trae_work_2026_09_20.md` | 2,816 | 2026-09-20 17:36:48 | `e061c5806af6` | 成果面 |
| 2759 | `letters/_v4_commission_inventory_anchor_note_2026_09_29.md` | 2,655 | 2026-09-29 13:25:03 | `849f8eba5bf0` | 成果面 |
| 2760 | `letters/_v4_commission_kimi_fullupload_w3_2026_09_30.md` | 16,404 | 2026-09-30 19:41:29 | `84c2f4aa9691` | 成果面 |
| 2761 | `letters/_v4_commission_paper_final_glm_2026_09_24.md` | 10,515 | 2026-09-24 18:55:43 | `53a425fe1bd2` | 成果面 |
| 2762 | `letters/_v4_commission_paper_final_glm_2026_09_24_v2.md` | 13,749 | 2026-09-24 20:05:57 | `f3b3e13a0f1b` | 成果面 |
| 2763 | `letters/_v4_commission_paper_final_glm_2026_09_24_v3.md` | 20,989 | 2026-09-26 19:19:09 | `614df9879696` | 成果面 |
| 2764 | `letters/_v4_commission_paper_final_glm_2026_09_24_v4.md` | 31,531 | 2026-09-26 21:25:21 | `d5337702cec9` | 成果面 |
| 2765 | `letters/_v4_commission_upload_channel_authorization_2026_09_26.md` | 26,937 | 2026-09-26 19:50:59 | `5e5479bfc453` | 成果面 |
| 2766 | `letters/_v4_commission_upload_channel_authorization_reply_kimi_2026_09_26.md` | 11,575 | 2026-09-26 20:04:44 | `f8f4ae2e7b9b` | 成果面 |
| 2767 | `letters/_v4_commission_upload_executor_2026_09_24.md` | 13,012 | 2026-09-24 18:56:08 | `adfa7dd03f76` | 成果面 |
| 2768 | `letters/_v4_commission_upload_executor_2026_09_24_v2.md` | 16,894 | 2026-09-24 20:05:57 | `ff2154ce182d` | 成果面 |
| 2769 | `letters/_v4_commission_upload_executor_2026_09_24_v3.md` | 25,091 | 2026-09-26 19:20:04 | `c20d4f58f5c8` | 成果面 |
| 2770 | `letters/_v4_commission_upload_executor_reply_v3_2026_09_24.md` | 9,848 | 2026-09-26 19:35:40 | `50592e36ecad` | 成果面 |
| 2771 | `letters/_v4_commission_upload_executor_reply_v3_exec_2026_09_26.md` | 4,471 | 2026-09-26 19:53:10 | `631bb517f79d` | 成果面 |
| 2772 | `letters/_v4_commission_〔IM〕_report_coze_2026_09_24.md` | 7,197 | 2026-09-24 18:55:26 | `15f8227308bc` | 成果面 |
| 2773 | `letters/_v4_commission_〔IM〕_report_coze_2026_09_24_v2.md` | 10,599 | 2026-09-24 20:05:56 | `389c51e70d19` | 成果面 |
| 2774 | `letters/_v4_commission_〔IM〕_report_coze_2026_09_24_v3.md` | 13,898 | 2026-09-26 19:19:29 | `e5b63d181b15` | 成果面 |
| 2775 | `letters/_v4_commission_〔IM〕_report_coze_2026_09_24_v4.md` | 21,433 | 2026-09-26 21:25:16 | `802c705e1469` | 成果面 |
| 2776 | `letters/_v4_commission_〔IM〕_report_coze_reply_v4_2026_09_24.md` | 16,471 | 2026-09-26 22:20:19 | `c60dfd7c0f45` | 成果面 |
| 2777 | `letters/_v4_d1_response_workbuddy_2026_09_20.md` | 14,881 | 2026-09-20 14:36:48 | `bc663b671994` | 成果面 |
| 2778 | `letters/_v4_d1_review_codex_2026_09_20.md` | 4,506 | 2026-09-21 11:12:20 | `48387412b109` | 成果面 |
| 2779 | `letters/_v4_distillation_acceptance_coze_2026_09_20.md` | 14,295 | 2026-09-20 18:03:55 | `3a8cb7b9d041` | 成果面 |
| 2780 | `letters/_v4_distillation_acceptance_kimi_2026_09_20.md` | 6,454 | 2026-09-20 17:56:29 | `a4d194dbf9ad` | 成果面 |
| 2781 | `letters/_v4_distillation_acceptance_trae_code_2026_09_20.md` | 5,218 | 2026-09-20 17:32:33 | `dc47fbf3c491` | 成果面 |
| 2782 | `letters/_v4_distillation_brainstorm_reply_codex_2026_09_21.md` | 9,048 | 2026-09-21 11:12:20 | `0ff6c042b845` | 成果面 |
| 2783 | `letters/_v4_distillation_invitation_2026_09_20_v1.0.md` | 54,784 | 2026-09-30 16:14:47 | `e4b00fa97d03` | 成果面 |
| 2784 | `letters/_v4_distillation_reply_claude_code_2026_09_20.md` | 64,212 | 2026-09-21 11:01:14 | `d39cb17b051b` | 成果面 |
| 2785 | `letters/_v4_distillation_reply_coze_2026_09_20.md` | 71,084 | 2026-09-20 21:53:15 | `00593014cbd3` | 成果面 |
| 2786 | `letters/_v4_distillation_reply_trae_code_2026_09_20.md` | 43,570 | 2026-09-20 21:21:36 | `e87ec8f7e2fe` | 成果面 |
| 2787 | `letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23.md` | 28,207 | 2026-09-23 13:35:13 | `9bb22099db3b` | 成果面 |
| 2788 | `letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23_fix_addendum.md` | 6,067 | 2026-09-23 13:46:15 | `59b8df6e2e22` | 成果面 |
| 2789 | `letters/_v4_distillation_theme_reply_workbuddy_2026_09_20.md` | 18,785 | 2026-09-20 18:19:48 | `e3fe63a2f708` | 成果面 |
| 2790 | `letters/_v4_distillation_theme_reply_workbuddy_brainstorm_2026_09_21.md` | 13,553 | 2026-09-21 09:42:45 | `cdb27cd3008c` | 成果面 |
| 2791 | `letters/_v4_distillation_theme_reply_workbuddy_part2_2026_09_20.md` | 12,963 | 2026-09-20 18:26:36 | `bfb4932f4467` | 成果面 |
| 2792 | `letters/_v4_experiment_invitation_2026_09_20.md` | 32,164 | 2026-09-30 16:14:47 | `20f8242de6ca` | 成果面 |
| 2793 | `letters/_v4_experiment_invitation_2026_09_20_v0.2.md` | 43,024 | 2026-09-30 16:14:47 | `72fc2e7fb098` | 成果面 |
| 2794 | `letters/_v4_ide_track_review_trae_code_supplement_2026_09_20.md` | 13,263 | 2026-09-30 16:14:47 | `f88e429717aa` | 成果面 |
| 2795 | `letters/_v4_ide_track_review_trae_work_2026_09_20.md` | 7,488 | 2026-09-20 17:35:40 | `21d384cf3422` | 成果面 |
| 2796 | `letters/_v4_review_claude_code_2026_09_20.md` | 7,004 | 2026-09-20 14:32:01 | `b6f9956bcf5c` | 成果面 |
| 2797 | `letters/_v4_theme_reply_mavis_2026_09_20.md` | 37,980 | 2026-09-30 16:14:47 | `5d932d7085cd` | 成果面 |
| 2798 | `letters/_v4_theme_reply_mavis_2026_09_20_v1.1.md` | 38,085 | 2026-09-30 16:14:47 | `5c61f61f1f7e` | 成果面 |
| 2799 | `letters/_v4_theme_reply_mavis_2026_09_20_v1.2.md` | 38,087 | 2026-09-30 16:14:47 | `f1d73c82511d` | 成果面 |
| 2800 | `letters/_v4_theme_reply_trae_work_2026_09_20.md` | 11,458 | 2026-09-20 17:35:40 | `eba83c88b629` | 成果面 |
| 2801 | `letters/_v4_theme_reply_trae_work_2026_09_20_v1.1.md` | 13,404 | 2026-09-20 17:39:33 | `be850d129f35` | 成果面 |
| 2802 | `letters/_v4_theme_reply_trae_work_2026_09_20_v1.2.md` | 28,395 | 2026-09-20 20:58:07 | `6bee6ec434bd` | 成果面 |
| 2803 | `letters/_v4_walkthrough_bugfix_reply_trae_code_2026_09_27.md` | 60,139 | 2026-09-27 20:13:23 | `f86b8b6c8ed2` | 成果面 |
| 2804 | `letters/_v4_wide_walkthrough_reply_trae_code_2026_09_27.md` | 20,610 | 2026-09-27 20:28:20 | `9a98abf3119a` | 成果面 |
| 2805 | `letters/_v5_rj5_external_rederive_request_2026_09_28.md` | 31,381 | 2026-09-28 18:22:06 | `cfd58ae66463` | 成果面 |
| 2806 | `letters/_v5_rj5_external_rederive_request_EN_2026_09_28.md` | 51,013 | 2026-09-28 18:47:14 | `498215a9ec7d` | 成果面 |
| 2807 | `letters/_walkthrough_bugfix_audit_reply_trae_code_2026_09_30.md` | 15,606 | 2026-09-30 19:07:36 | `5bfc26bbaa41` | 成果面 |
| 2808 | `letters/LETTER_FROM_TRAE_2026_09_11.md` | 13,617 | 2026-09-11 16:30:23 | `1d3a9e52abe3` | 成果面 |
| 2809 | `letters/LETTER_FROM_TRAE_3RISK_2026_09_11.md` | 5,145 | 2026-09-15 10:25:49 | `a1afbf3e1296` | 成果面 |
| 2810 | `letters/LETTER_FROM_TRAE_REVIEW_2026_09_16.md` | 7,718 | 2026-09-15 15:19:16 | `6145162379c9` | 成果面 |
| 2811 | `letters/LETTER_FROM_TRAE_SELFCHECK_FIX_2026_09_15.md` | 3,571 | 2026-09-15 15:39:01 | `141e05bf56ea` | 成果面 |
| 2812 | `letters/RECEIPT_COPILOT_AGENT_T2_T3_2026_10_17.txt` | 529 | 2026-10-17 15:54:08 | `1cd576e3c826` | 成果面 |
| 2813 | `letters/REPLY_FROM_COPILOT_AGENT_T2_T3_THEORY_INPUTS_2026_10_17.md` | 30,459 | 2026-10-17 15:54:08 | `597caf8ba5bc` | 成果面 |
| 2814 | `letters/REPLY_FROM_GEMINI4_GE01_THEORY_INPUTS_2026_10_15.md` | 44,520 | 2026-10-15 12:15:38 | `44311ade19de` | 成果面 |
| 2815 | `letters/TRAE_CODE_IMPROVEMENT_LETTER_2026_09_17.md` | 5,154 | 2026-09-17 19:16:03 | `53a90b9efbb9` | 成果面 |
| 2816 | `letters/TRAE_FIX_REQUEST_3RISKS_2026_09_11.md` | 15,990 | 2026-09-11 17:27:09 | `62c4af080ea3` | 成果面 |
| 2817 | `letters/TRAE_V3_CODE_IMPROVEMENT_LETTER_2026_09_16.md` | 7,376 | 2026-09-16 20:58:07 | `9aa717b2e1ac` | 成果面 |
| 2818 | `letters/TRAE_V3_REVIEW_LETTER_2026_09_23.md` | 7,510 | 2026-09-23 13:08:23 | `0e7600ac4478` | 成果面 |
| 2819 | `letters/TRAE_V4_WALKTHROUGH_BUGFIX_REQUEST_2026_09_27.md` | 105,136 | 2026-09-27 19:20:37 | `6ac3cb09567b` | 成果面 |
| 2820 | `letters/TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md` | 101,560 | 2026-09-30 18:05:24 | `e17412088546` | 成果面 |
| 2821 | `letters/verify_c4_originated_math.py` | 4,115 | 2026-10-10 17:30:17 | `3042cf59448e` | 成果面 |
| 2822 | `letters/查理_deposon双主线论文终稿_2026-10-01_v0.3.md` | 239,700 | 2026-10-10 21:21:41 | `8baa9854b3f7` | 成果面 |
| 2823 | `letters/查理_glm_dualtrack_paper_sole_letter_2026_10_01.md` | 13,105 | 2026-10-02 00:19:43 | `3c5059319ffe` | 成果面 |
| 2824 | `LICENSE` | 1,085 | 2026-08-22 21:07:57 | `6a703b06f0fe` | 成果面 |
| 2825 | `llm_fetch.py` | 8,433 | 2026-08-30 10:09:18 | `fda22714de2d` | 成果面 |
| 2826 | `llm_prior.py` | 7,466 | 2026-08-30 10:10:54 | `7fba7d72a679` | 成果面 |
| 2827 | `mindmap_corpus_v20.py` | 25,791 | 2026-09-29 12:06:04 | `e77e7f3455e0` | 成果面 |
| 2828 | `paper/deposon_paper_final_cn.md` | 53,838 | 2026-09-20 17:11:14 | `c5f6a23f4408` | 成果面 |
| 2829 | `paper/deposon_paper_final_en.md` | 68,164 | 2026-09-20 17:11:14 | `2ec20b96e941` | 成果面 |
| 2830 | `paper/FIGURE_LANGUAGE_POLICY.md` | 2,495 | 2026-08-30 11:16:21 | `a18b5d0d4485` | 成果面 |
| 2831 | `paper/v2/outline_v2X.md` | 10,476 | 2026-08-30 10:43:36 | `116d193b1607` | 成果面 |
| 2832 | `paper/v2/related_work_v2X.md` | 10,114 | 2026-08-29 15:43:30 | `7fb001add973` | 成果面 |
| 2833 | `pi_rulings/_pi_card_answers_register_2026_10_13.md` | 5,707 | 2026-10-14 00:13:48 | `10a74ce8901d` | 成果面 |
| 2834 | `pi_rulings/_pi_card_answers_register_2026_10_14.md` | 5,529 | 2026-10-14 20:57:43 | `bc9680a5d39a` | 成果面 |
| 2835 | `pi_rulings/_pi_card_answers_register_2026_10_14_b11_recovery.md` | 13,812 | 2026-10-18 00:02:40 | `d224a7380071` | 成果面 |
| 2836 | `pi_rulings/_pi_card_answers_register_2026_10_14_v2.md` | 5,968 | 2026-10-14 21:15:04 | `ee392ef4a69a` | 成果面 |
| 2837 | `pi_rulings/_pi_card_answers_register_2026_10_14_v3.md` | 5,664 | 2026-10-14 21:30:03 | `59e8a7be4c05` | 成果面 |
| 2838 | `pi_rulings/_pi_card_answers_register_2026_10_14_v4.md` | 5,010 | 2026-10-14 21:41:45 | `7838b3300596` | 成果面 |
| 2839 | `pi_rulings/_pi_card_answers_register_2026_10_14_v5.md` | 5,643 | 2026-10-14 21:53:10 | `3587e46b45c3` | 成果面 |
| 2840 | `pi_rulings/_pi_card_answers_register_2026_10_14_v6.md` | 5,469 | 2026-10-14 22:02:43 | `7e95b053e249` | 成果面 |
| 2841 | `pi_rulings/_pi_card_answers_register_2026_10_14_v7.md` | 5,851 | 2026-10-14 22:12:13 | `d114b7576b78` | 成果面 |
| 2842 | `pi_rulings/_pi_card_answers_register_2026_10_14_v8.md` | 5,252 | 2026-10-14 22:41:48 | `58d1c527e228` | 成果面 |
| 2843 | `pi_rulings/_pi_card_answers_register_2026_10_14_v9.md` | 4,071 | 2026-10-14 23:15:40 | `64450a287abd` | 成果面 |
| 2844 | `pi_rulings/_pi_card_answers_register_2026_10_15_v10.md` | 6,132 | 2026-10-15 09:39:21 | `57b4d493789a` | 成果面 |
| 2845 | `pi_rulings/_pi_card_answers_register_2026_10_15_v11.md` | 4,577 | 2026-10-15 10:02:55 | `30408490f37e` | 成果面 |
| 2846 | `pi_rulings/_pi_card_answers_register_2026_10_15_v12.md` | 6,081 | 2026-10-15 11:03:46 | `97111fee4410` | 成果面 |
| 2847 | `pi_rulings/_pi_card_answers_register_2026_10_15_v13.md` | 3,661 | 2026-10-15 12:53:08 | `693181b9354b` | 成果面 |
| 2848 | `pi_rulings/_pi_card_answers_register_2026_10_15_v14.md` | 5,805 | 2026-10-15 14:37:19 | `ac3b580defbb` | 成果面 |
| 2849 | `pi_rulings/_pi_card_answers_register_2026_10_15_v15.md` | 4,531 | 2026-10-15 15:14:09 | `c6c1e9fe17ad` | 成果面 |
| 2850 | `pi_rulings/_pi_card_answers_register_2026_10_15_v16.md` | 5,070 | 2026-10-15 16:05:21 | `b8036d12e28f` | 成果面 |
| 2851 | `pi_rulings/_pi_card_answers_register_2026_10_15_v17.md` | 4,140 | 2026-10-15 16:41:15 | `bc3041ec2cbc` | 成果面 |
| 2852 | `pi_rulings/_pi_card_answers_register_2026_10_15_v18.md` | 4,670 | 2026-10-15 17:06:55 | `318d176e027c` | 成果面 |
| 2853 | `pi_rulings/_pi_card_answers_register_2026_10_16_v19.md` | 4,773 | 2026-10-16 10:50:16 | `e1f9b3d07eef` | 成果面 |
| 2854 | `pi_rulings/_pi_card_answers_register_2026_10_16_v20.md` | 6,075 | 2026-10-16 11:32:01 | `44aa59715d21` | 成果面 |
| 2855 | `pi_rulings/_pi_card_answers_register_2026_10_16_v21.md` | 3,210 | 2026-10-16 11:41:27 | `4b72c0b23504` | 成果面 |
| 2856 | `pi_rulings/_pi_card_answers_register_2026_10_16_v22.md` | 5,629 | 2026-10-16 13:43:01 | `e8d476480244` | 成果面 |
| 2857 | `pi_rulings/_pi_card_answers_register_2026_10_16_v23.md` | 4,889 | 2026-10-16 14:23:19 | `a2a883a6be8e` | 成果面 |
| 2858 | `pi_rulings/_pi_card_answers_register_2026_10_16_v24.md` | 3,985 | 2026-10-16 15:04:12 | `e18bb149018d` | 成果面 |
| 2859 | `pi_rulings/_pi_card_answers_register_2026_10_16_v25.md` | 5,400 | 2026-10-16 15:16:39 | `b682e95fba5e` | 成果面 |
| 2860 | `pi_rulings/_pi_card_answers_register_2026_10_16_v26.md` | 4,338 | 2026-10-16 15:55:54 | `bcd9598a243a` | 成果面 |
| 2861 | `pi_rulings/_pi_card_answers_register_2026_10_16_v27.md` | 10,776 | 2026-10-16 19:22:10 | `6cdb2bc823f9` | 成果面 |
| 2862 | `pi_rulings/_pi_card_answers_register_2026_10_16_v28.md` | 11,627 | 2026-10-16 19:32:50 | `87aea4811290` | 成果面 |
| 2863 | `pi_rulings/_pi_card_answers_register_2026_10_16_v29.md` | 16,960 | 2026-10-16 19:45:45 | `bfcc14f8a4ce` | 成果面 |
| 2864 | `pi_rulings/_pi_card_answers_register_2026_10_16_v30.md` | 24,832 | 2026-10-16 20:01:01 | `1c11cc165d27` | 成果面 |
| 2865 | `pi_rulings/_pi_card_answers_register_2026_10_16_v31.md` | 26,239 | 2026-10-16 20:19:06 | `ad53416b5f10` | 成果面 |
| 2866 | `pi_rulings/_pi_card_answers_register_2026_10_16_v32.md` | 31,156 | 2026-10-16 20:24:30 | `c20d77f3b79c` | 成果面 |
| 2867 | `pi_rulings/_pi_card_answers_register_2026_10_16_v33.md` | 18,077 | 2026-10-16 20:25:45 | `a03c20e88d66` | 成果面 |
| 2868 | `pi_rulings/_pi_card_answers_register_2026_10_16_v34.md` | 21,659 | 2026-10-16 20:53:06 | `f4ebae2d17e7` | 成果面 |
| 2869 | `pi_rulings/_pi_card_answers_register_2026_10_16_v35.md` | 19,575 | 2026-10-16 21:17:15 | `6ff343861b29` | 成果面 |
| 2870 | `pi_rulings/_pi_card_answers_register_2026_10_16_v36.md` | 26,950 | 2026-10-16 21:38:38 | `371a3c19b734` | 成果面 |
| 2871 | `pi_rulings/_pi_card_answers_register_2026_10_16_v37.md` | 25,891 | 2026-10-16 21:41:50 | `8d46bd80c654` | 成果面 |
| 2872 | `pi_rulings/_pi_card_answers_register_2026_10_16_v38.md` | 23,104 | 2026-10-16 22:02:03 | `db7b9f80bdd1` | 成果面 |
| 2873 | `pi_rulings/_pi_card_answers_register_2026_10_16_v39.md` | 20,508 | 2026-10-16 22:18:26 | `8ce18e4b5eab` | 成果面 |
| 2874 | `pi_rulings/_pi_card_answers_register_2026_10_16_v40.md` | 26,768 | 2026-10-16 22:40:00 | `8f8ba225a558` | 成果面 |
| 2875 | `pi_rulings/_pi_card_answers_register_2026_10_16_v41.md` | 41,175 | 2026-10-16 23:14:03 | `1e75eecc1657` | 成果面 |
| 2876 | `pi_rulings/_pi_card_answers_register_2026_10_16_v42.md` | 41,612 | 2026-10-16 23:39:16 | `57d938ea80dc` | 成果面 |
| 2877 | `pi_rulings/_pi_card_answers_register_2026_10_16_v43.md` | 33,335 | 2026-10-16 23:49:16 | `c5d5d0c24041` | 成果面 |
| 2878 | `pi_rulings/_pi_card_answers_register_2026_10_16_v44.md` | 45,596 | 2026-10-17 00:17:54 | `996331734904` | 成果面 |
| 2879 | `pi_rulings/_pi_card_answers_register_2026_10_17_v45.md` | 61,355 | 2026-10-17 10:14:30 | `fb444970452c` | 成果面 |
| 2880 | `pi_rulings/_pi_card_answers_register_2026_10_17_v46.md` | 64,372 | 2026-10-17 10:38:06 | `3b5e35eebcbd` | 成果面 |
| 2881 | `pi_rulings/_pi_card_answers_register_2026_10_17_v47.md` | 65,046 | 2026-10-17 10:54:30 | `6731d5533709` | 成果面 |
| 2882 | `pi_rulings/_pi_card_answers_register_2026_10_17_v48.md` | 63,119 | 2026-10-17 11:12:18 | `876f0e5dc38d` | 成果面 |
| 2883 | `pi_rulings/_pi_card_answers_register_2026_10_17_v49.md` | 58,978 | 2026-10-17 11:23:23 | `2367979d60a4` | 成果面 |
| 2884 | `pi_rulings/_pi_card_answers_register_2026_10_17_v50.md` | 87,647 | 2026-10-17 11:59:35 | `188ac0656715` | 成果面 |
| 2885 | `pi_rulings/_pi_card_answers_register_2026_10_17_v51.md` | 106,355 | 2026-10-17 12:33:27 | `ffa1cd08b98b` | 成果面 |
| 2886 | `pi_rulings/_pi_card_answers_register_2026_10_17_v52.md` | 61,157 | 2026-10-17 14:22:21 | `511d3518aa15` | 成果面 |
| 2887 | `pi_rulings/_pi_card_answers_register_2026_10_17_v53.md` | 51,621 | 2026-10-17 15:19:00 | `4c2d5c66f52b` | 成果面 |
| 2888 | `pi_rulings/_pi_card_answers_register_2026_10_17_v54.md` | 72,379 | 2026-10-17 16:02:50 | `b45c83999e9f` | 成果面 |
| 2889 | `pi_rulings/_pi_card_answers_register_2026_10_17_v55.md` | 54,188 | 2026-10-17 16:05:37 | `84f6c4bfdb07` | 成果面 |
| 2890 | `pi_rulings/_pi_card_answers_register_2026_10_17_v56.md` | 51,458 | 2026-10-17 16:18:36 | `d4c5d4988944` | 成果面 |
| 2891 | `pi_rulings/_pi_card_answers_register_2026_10_17_v58.md` | 43,565 | 2026-10-17 16:39:11 | `e15de4a194e0` | 成果面 |
| 2892 | `pi_rulings/_pi_card_answers_register_2026_10_17_v59.md` | 46,878 | 2026-10-17 16:56:45 | `313f1e970c44` | 成果面 |
| 2893 | `pi_rulings/_pi_card_answers_register_2026_10_17_v60.md` | 49,651 | 2026-10-17 17:09:35 | `480e73634145` | 成果面 |
| 2894 | `pi_rulings/_pi_card_answers_register_2026_10_17_v61.md` | 39,769 | 2026-10-17 17:15:26 | `8e41cd9eb3b8` | 成果面 |
| 2895 | `pi_rulings/_pi_card_answers_register_2026_10_17_v62.md` | 45,153 | 2026-10-17 17:40:39 | `2be4cd9e9539` | 成果面 |
| 2896 | `pi_rulings/_pi_card_answers_register_2026_10_17_v63.md` | 53,821 | 2026-10-17 17:57:09 | `8def4b31c700` | 成果面 |
| 2897 | `pi_rulings/_pi_card_answers_register_2026_10_17_v63_append1.md` | 23,862 | 2026-10-17 18:00:22 | `e566cff9ce9d` | 成果面 |
| 2898 | `pi_rulings/_pi_card_answers_register_2026_10_17_v64.md` | 48,215 | 2026-10-17 18:25:57 | `02db93851600` | 成果面 |
| 2899 | `pi_rulings/_pi_card_answers_register_2026_10_17_v65.md` | 34,862 | 2026-10-17 18:52:29 | `361a513b41b2` | 成果面 |
| 2900 | `pi_rulings/_pi_card_answers_register_2026_10_17_v66.md` | 48,278 | 2026-10-17 18:54:37 | `97b754e4bef8` | 成果面 |
| 2901 | `pi_rulings/_pi_card_answers_register_2026_10_17_v66_append1.md` | 12,310 | 2026-10-17 19:00:43 | `9cff8adbde16` | 成果面 |
| 2902 | `pi_rulings/_pi_card_answers_register_2026_10_17_v66_append2.md` | 5,927 | 2026-10-17 19:01:58 | `9d4151dc3053` | 成果面 |
| 2903 | `pi_rulings/_pi_card_answers_register_2026_10_17_v67.md` | 46,839 | 2026-10-17 19:05:01 | `75b5841a3dfb` | 成果面 |
| 2904 | `pi_rulings/_pi_card_answers_register_2026_10_17_v68.md` | 49,343 | 2026-10-17 19:13:53 | `da9d5195687a` | 成果面 |
| 2905 | `pi_rulings/_pi_card_answers_register_2026_10_17_v69.md` | 45,882 | 2026-10-17 19:22:09 | `ff190f0b1f44` | 成果面 |
| 2906 | `pi_rulings/_pi_card_answers_register_2026_10_17_v70.md` | 41,056 | 2026-10-17 19:25:20 | `8674655fc387` | 成果面 |
| 2907 | `pi_rulings/_pi_card_answers_register_2026_10_17_v71.md` | 31,504 | 2026-10-17 19:42:40 | `ea23ee2068dd` | 成果面 |
| 2908 | `pi_rulings/_pi_card_answers_register_2026_10_17_v72.md` | 33,695 | 2026-10-17 19:47:57 | `eaa2535de267` | 成果面 |
| 2909 | `pi_rulings/_pi_card_answers_register_2026_10_17_v73.md` | 40,176 | 2026-10-17 19:58:04 | `82d6c06b3a0f` | 成果面 |
| 2910 | `pi_rulings/_pi_card_answers_register_2026_10_17_v74.md` | 47,243 | 2026-10-17 20:02:09 | `f86dbb713d53` | 成果面 |
| 2911 | `pi_rulings/_pi_card_answers_register_2026_10_17_v75.md` | 45,643 | 2026-10-17 20:15:17 | `1119913b66e4` | 成果面 |
| 2912 | `pi_rulings/_pi_card_answers_register_2026_10_17_v76.md` | 49,490 | 2026-10-17 20:22:36 | `724b41bf7b46` | 成果面 |
| 2913 | `pi_rulings/_pi_card_answers_register_2026_10_17_v77.md` | 47,239 | 2026-10-17 20:41:55 | `904c4fc1ce40` | 成果面 |
| 2914 | `pi_rulings/_pi_card_answers_register_2026_10_17_v78.md` | 57,896 | 2026-10-17 20:46:30 | `11b378afa490` | 成果面 |
| 2915 | `pi_rulings/_pi_card_answers_register_2026_10_17_v79.md` | 38,119 | 2026-10-17 21:07:57 | `283a697a7704` | 成果面 |
| 2916 | `pi_rulings/_pi_card_answers_register_2026_10_17_v80.md` | 33,777 | 2026-10-17 21:40:30 | `a40f5698a1da` | 成果面 |
| 2917 | `pi_rulings/_pi_card_answers_register_2026_10_17_v81.md` | 51,667 | 2026-10-17 22:01:16 | `816a5414a86a` | 成果面 |
| 2918 | `pi_rulings/_pi_card_answers_register_2026_10_17_v82.md` | 47,749 | 2026-10-17 22:16:05 | `79dd0fdf23c9` | 成果面 |
| 2919 | `pi_rulings/_pi_card_answers_register_2026_10_17_v83.md` | 49,996 | 2026-10-17 22:32:23 | `e2a67aa39bdd` | 成果面 |
| 2920 | `pi_rulings/_pi_card_answers_register_2026_10_17_v84.md` | 42,968 | 2026-10-17 22:46:10 | `c565669aadeb` | 成果面 |
| 2921 | `pi_rulings/_pi_card_answers_register_2026_10_17_v85.md` | 51,362 | 2026-10-17 23:12:28 | `c54c4580baa2` | 成果面 |
| 2922 | `pi_rulings/_pi_card_answers_register_2026_10_17_v86.md` | 39,039 | 2026-10-17 23:10:53 | `19821507b5b2` | 成果面 |
| 2923 | `pi_rulings/_pi_card_answers_register_2026_10_17_v87.md` | 56,899 | 2026-10-17 23:35:48 | `346456d03425` | 成果面 |
| 2924 | `pi_rulings/_pi_card_answers_register_2026_10_17_v88.md` | 39,767 | 2026-10-17 23:35:48 | `061380c8a9fb` | 成果面 |
| 2925 | `pi_rulings/_pi_card_answers_register_2026_10_17_v89.md` | 50,984 | 2026-10-17 23:53:38 | `b0f09b01f774` | 成果面 |
| 2926 | `README.md` | 7,279 | 2026-09-30 23:53:17 | `a80b3db006a5` | 成果面 |
| 2927 | `README_V4_2026_09_29.md` | 58,635 | 2026-09-30 20:36:18 | `a6f88fb6e325` | 成果面 |
| 2928 | `RELEASE_v1.4.0.md` | 3,847 | 2026-08-23 16:38:29 | `ff9ff3177c06` | 成果面 |
| 2929 | `requirements.txt` | 27 | 2026-08-22 21:07:57 | `ab3045b2c6d9` | 成果面 |
| 2930 | `results/_9model_full_merge_from_4workers_2026_10_09.json` | 19,337 | 2026-10-09 12:08:37 | `32aa0618a9d7` | 成果面 |
| 2931 | `results/_achievements_inventory_full_2026_10_09.md` | 372,318 | 2026-10-12 03:20:49 | `dd3e9806a369` | 成果面 |
| 2932 | `results/_af1_attribution_verdict_2026_10_17.md` | 43,259 | 2026-10-17 22:02:25 | `d6d8c488fc33` | 成果面 |
| 2933 | `results/_af2_5_proof_2026_10_17.md` | 48,208 | 2026-10-17 22:33:28 | `b3c45b4e2ec0` | 成果面 |
| 2934 | `results/_af2_proof_and_grain_scope_effect_2026_10_17.md` | 41,779 | 2026-10-17 22:32:23 | `faee80c8b051` | 成果面 |
| 2935 | `results/_af_complete_landing_effect_2026_10_17.md` | 54,092 | 2026-10-17 23:11:41 | `14e4181c5b69` | 成果面 |
| 2936 | `results/_af_entity_rules_2026_10_17.md` | 39,994 | 2026-10-17 20:54:54 | `525ae85c1bbc` | 成果面 |
| 2937 | `results/_af_flip要件消解_rulings_effect_2026_10_17.md` | 45,096 | 2026-10-17 22:16:05 | `dc5ee48e1f53` | 成果面 |
| 2938 | `results/_af_landing_n7_and_two_cells_effect_2026_10_17.md` | 40,560 | 2026-10-17 22:46:10 | `955222063aa0` | 成果面 |
| 2939 | `results/_af_rules_approval_effect_2026_10_17.md` | 43,731 | 2026-10-17 21:09:02 | `ce0a2847ad4e` | 成果面 |
| 2940 | `results/_anchor_drift_authorized_adoption_2026_10_16.md` | 25,026 | 2026-10-16 19:49:01 | `306b2cd2e0b6` | 成果面 |
| 2941 | `results/_anchor_status_naming_note_2026_10_16.md` | 11,716 | 2026-10-16 19:32:50 | `d042dd66e3c7` | 成果面 |
| 2942 | `results/_anchor_value_update_and_l261_patch_migration_register_2026_10_16.md` | 17,521 | 2026-10-16 11:43:54 | `3f75ce7b3f3f` | 成果面 |
| 2943 | `results/_anti_degradation_mechanism_2026_10_14.md` | 7,658 | 2026-10-14 23:48:56 | `8e0a33e77751` | 成果面 |
| 2944 | `results/_approval_card_four_rulings_effect_2026_10_17.md` | 50,703 | 2026-10-17 20:43:49 | `8e1b7d6ae996` | 成果面 |
| 2945 | `results/_archive_2026-10-12/exec_artifacts/_exp06_1009fix_build_2026_10_10.py` | 29,412 | 2026-10-10 11:22:20 | `e5acb3c0bca2` | 成果面 |
| 2946 | `results/_archive_2026-10-12/exec_artifacts/_exp06_1009fix_lnref2_2026_10_10.py` | 1,505 | 2026-10-10 11:20:46 | `3ff21d556306` | 成果面 |
| 2947 | `results/_archive_2026-10-12/exec_artifacts/_exp06_1009fix_lnref_2026_10_10.py` | 1,508 | 2026-10-10 11:20:15 | `9c7096147878` | 成果面 |
| 2948 | `results/_archive_2026-10-12/exec_artifacts/_exp06_1009fix_verify_2026_10_10.py` | 7,817 | 2026-10-10 11:17:16 | `47fdf9673acc` | 成果面 |
| 2949 | `results/_archive_2026-10-12/exec_artifacts/_exp06_fixcopy_verify_probe_2026_10_10.py` | 3,598 | 2026-10-10 10:49:23 | `680b6893f9f7` | 成果面 |
| 2950 | `results/_archive_2026-10-12/exec_artifacts/c5_guard_minmaxstd_2026_10_01.py` | 15,009 | 2026-10-01 10:14:05 | `d74ff478993c` | 成果面 |
| 2951 | `results/_archive_2026-10-12/exec_artifacts/e4_axis2_crosscheck_2026_10_10.py` | 3,607 | 2026-10-10 15:00:27 | `fbf93a534b99` | 成果面 |
| 2952 | `results/_archive_2026-10-12/exec_artifacts/e4_axis2_denominator_recheck_2026_10_10.py` | 3,833 | 2026-10-10 15:00:04 | `5944efd3b68e` | 成果面 |
| 2953 | `results/_archive_2026-10-12/exec_artifacts/e4_axis2_final_validation_2026_10_10.py` | 6,489 | 2026-10-10 15:01:06 | `8d2211f8ac91` | 成果面 |
| 2954 | `results/_archive_2026-10-12/exec_artifacts/e4_axis2_hit_unchanged_probe_2026_10_10.py` | 2,629 | 2026-10-10 15:02:27 | `fc5d6bde78ad` | 成果面 |
| 2955 | `results/_archive_2026-10-12/exec_artifacts/e4_axis2_v11_displacement_run_2026_10_10.py` | 10,617 | 2026-10-10 14:59:32 | `a950ae064fde` | 成果面 |
| 2956 | `results/_archive_2026-10-12/exec_artifacts/exp06_independent_json_gen_2026_10_10.py` | 21,560 | 2026-10-10 10:31:30 | `5ce8f89c9396` | 成果面 |
| 2957 | `results/_archive_2026-10-12/exec_artifacts/exp06_supplement_probe_2026_10_10.py` | 7,438 | 2026-10-10 10:30:11 | `97076c37afa7` | 成果面 |
| 2958 | `results/_archive_2026-10-12/exec_artifacts/scan_five_terminal_2026_10_10.py` | 4,319 | 2026-10-10 12:21:36 | `7200487fdab1` | 成果面 |
| 2959 | `results/_archive_2026-10-12/pycache_sink/deposon_team_plugins_pycache/boss_pa_1_rbr_rm_v3df_ab_alpha_2026_10_09.cpython-314.pyc` | 55,784 | 2026-10-09 23:25:55 | `f96453ebead6` | 成果面 |
| 2960 | `results/_archive_2026-10-12/pycache_sink/deposon_team_plugins_pycache/boss_pa_1_rbr_rm_v3df_ab_beta_2026_10_09.cpython-314.pyc` | 57,022 | 2026-10-09 23:25:21 | `80a752cca163` | 成果面 |
| 2961 | `results/_archive_2026-10-12/pycache_sink/deposon_team_plugins_pycache/boss_pa_1_rbr_rm_v3df_p1_reopen_2026_09_29.cpython-314.pyc` | 103,946 | 2026-10-10 10:03:53 | `74467bb37f95` | 成果面 |
| 2962 | `results/_archive_2026-10-12/pycache_sink/results_pycache/_s4prime_five_lines_runner_2026_10_11.cpython-314.pyc` | 43,685 | 2026-10-11 16:51:05 | `f4194cc5a522` | 成果面 |
| 2963 | `results/_archive_2026-10-12/pycache_sink/results_pycache/_s5doubleprime_five_lines_runner_2026_10_11.cpython-314.pyc` | 44,952 | 2026-10-11 20:32:37 | `9fc3e2152679` | 成果面 |
| 2964 | `results/_archive_2026-10-12/pycache_sink/results_pycache/_t1_exp2_executor_2026_10_09.cpython-314.pyc` | 87,302 | 2026-10-09 22:50:42 | `346595df084c` | 成果面 |
| 2965 | `results/_archive_2026-10-12/pycache_sink/results_pycache/_v4_pi_cot_v3_ruleset_v3_executor.cpython-314.pyc` | 67,081 | 2026-10-09 17:34:40 | `08d4b51c45c6` | 成果面 |
| 2966 | `results/_archive_2026-10-12/pycache_sink/results_pycache/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.cpython-314.pyc` | 69,630 | 2026-10-09 17:43:14 | `e7ab1adbf898` | 成果面 |
| 2967 | `results/_archive_2026-10-12/superseded_variants/_card23_readout_utf8.txts` | 5,088 | 2026-10-10 00:37:18 | `4aa127d1dc62` | 成果面 |
| 2968 | `results/_archive_2026-10-14/voided/_four_class_backtrace_inventory_2026_10_13.md` | 29,156 | 2026-10-13 21:20:54 | `cc45240386e8` | 成果面 |
| 2969 | `results/_archive_2026-10-14/voided/_ge01_epsilon_sensitivity_grid_design_2026_10_13.md` | 35,263 | 2026-10-14 00:11:49 | `fc08d248a6bf` | 成果面 |
| 2970 | `results/_archive_2026_09_24/_final_verify.py._moved_20260924_1830` | 2,279 | 2026-09-24 13:37:46 | `db4428293040` | 成果面 |
| 2971 | `results/_archive_2026_09_24/_l11_run1.json` | 12,143 | 2026-09-24 13:34:09 | `20b0e13064f8` | 成果面 |
| 2972 | `results/_archive_2026_09_24/_l14_checkpoint.json` | 10,963 | 2026-09-24 14:56:40 | `91b582672b49` | 成果面 |
| 2973 | `results/_archive_2026_09_24/_l14_records.json` | 50,957 | 2026-09-24 15:34:57 | `8f6fcf027149` | 成果面 |
| 2974 | `results/_archive_2026_09_24/_volc_22cap_emb.py` | 11,105 | 2026-09-10 17:36:26 | `15904ecae629` | 成果面 |
| 2975 | `results/_archive_2026_09_24/l14_runner_v2.py` | 23,056 | 2026-09-24 15:07:26 | `acf1cd6ccbd4` | 成果面 |
| 2976 | `results/_archive_2026_09_24/l14_runner_v2_r1_atomic_2026_09_29.py` | 25,892 | 2026-09-29 11:12:41 | `b1923528ab84` | 成果面 |
| 2977 | `results/_archive_manifest_deposon_sub_2026_09_23.json` | 52,153 | 2026-09-23 15:11:29 | `b34b9f7bdfb7` | 成果面 |
| 2978 | `results/_archive_manifest_non_upload_2026_09_23.json` | 148,690 | 2026-09-23 15:11:35 | `b899103853ca` | 成果面 |
| 2979 | `results/_archive_whitelist_purge_exec_register_2026_10_17.md` | 99,775 | 2026-10-17 12:29:41 | `9a68efcd5ceb` | 成果面 |
| 2980 | `results/_archive_zone_exception_g2_extension_register_2026_10_12.md` | 4,151 | 2026-10-12 23:23:44 | `7ae0c25f072f` | 成果面 |
| 2981 | `results/_archive_zone_exception_grant_register_2026_10_12.md` | 5,750 | 2026-10-12 22:55:00 | `f09279fbb11c` | 成果面 |
| 2982 | `results/_archive_zone_exception_p4_extension_register_2026_10_12.md` | 3,945 | 2026-10-13 00:00:18 | `64da1d988121` | 成果面 |
| 2983 | `results/_archive_zone_scan_violation_register_2026_10_12.md` | 5,723 | 2026-10-12 21:05:39 | `9391d1293f9b` | 成果面 |
| 2984 | `results/_archive_zone_write_clause_corrigendum_2026_10_17.md` | 13,526 | 2026-10-17 10:50:42 | `074a6f256655` | 成果面 |
| 2985 | `results/_b0_sixty_items_location_list_2026_10_13.md` | 33,046 | 2026-10-13 21:57:15 | `7c1f8a704f83` | 成果面 |
| 2986 | `results/_b4_alternative_deliberation_judgment_2026_10_12.md` | 14,233 | 2026-10-12 22:13:16 | `f050e5aff611` | 成果面 |
| 2987 | `results/_b4_source_fix_and_reissue_register_2026_10_12.md` | 11,168 | 2026-10-12 22:27:50 | `622097d3b964` | 成果面 |
| 2988 | `results/_b_tier_five_subitems_draft_2026_10_14.md` | 37,605 | 2026-10-14 02:14:14 | `3adfa261bab9` | 成果面 |
| 2989 | `results/_batch10_deliberation_judgment_2026_10_14.md` | 32,458 | 2026-10-14 11:19:13 | `f1e9d439b04d` | 成果面 |
| 2990 | `results/_batch11_deliberation_judgment_2026_10_14.md` | 25,153 | 2026-10-14 14:51:15 | `70b50503a32e` | 成果面 |
| 2991 | `results/_batch1_d4_d5_b1_errata_2026_10_12.md` | 22,871 | 2026-10-12 15:09:38 | `5193321dbe61` | 成果面 |
| 2992 | `results/_batch3_closure_register_2026_10_12.md` | 22,896 | 2026-10-12 21:10:09 | `69c459496a5b` | 成果面 |
| 2993 | `results/_batch3_residuals_disposition_register_2026_10_12.md` | 6,278 | 2026-10-12 22:03:07 | `ca31b01643d5` | 成果面 |
| 2994 | `results/_batch5_deliberation_judgment_2026_10_13.md` | 46,325 | 2026-10-13 22:19:26 | `a1ad238879ad` | 成果面 |
| 2995 | `results/_batch6_deliberation_judgment_2026_10_13.md` | 29,421 | 2026-10-13 22:50:27 | `a41332378c56` | 成果面 |
| 2996 | `results/_batch7_deliberation_judgment_2026_10_13.md` | 28,728 | 2026-10-14 00:12:17 | `36f70c0a844c` | 成果面 |
| 2997 | `results/_batch8_deliberation_judgment_2026_10_14.md` | 49,012 | 2026-10-14 00:52:15 | `a68b2971b8e1` | 成果面 |
| 2998 | `results/_batch9_deliberation_judgment_2026_10_14.md` | 36,623 | 2026-10-14 01:15:44 | `a93cd166a83b` | 成果面 |
| 2999 | `results/_batch_approval_merged_rollout_design_2026_10_14.md` | 83,822 | 2026-10-14 17:15:19 | `5078ebf4ac4c` | 成果面 |
| 3000 | `results/_bayesian_baseline_design_2026_10_10.md` | 29,783 | 2026-10-10 02:45:24 | `7e181a167702` | 成果面 |
| 3001 | `results/_bd_fixes_summary_2026_10_12.md` | 28,935 | 2026-10-12 17:50:24 | `3db40bac2267` | 成果面 |
| 3002 | `results/_bob_commission_acceptance_and_r4_waiver_register_2026_10_12.md` | 9,028 | 2026-10-12 20:42:37 | `e11d563b66dc` | 成果面 |
| 3003 | `results/_bob_minimax_commission_family_intake_register_2026_10_12.md` | 15,408 | 2026-10-12 20:32:36 | `e6f2b94620bf` | 成果面 |
| 3004 | `results/_budget_210_actual_evidence_register_2026_10_16.md` | 19,542 | 2026-10-16 11:04:27 | `daf7ee522707` | 成果面 |
| 3005 | `results/_budget_720_authorized_actual_register_2026_10_16.md` | 28,062 | 2026-10-16 11:42:11 | `da3c031e0dd6` | 成果面 |
| 3006 | `results/_c1_u5_ruling_register_2026_10_12.md` | 15,499 | 2026-10-12 17:01:19 | `2c3f48e111cc` | 成果面 |
| 3007 | `results/_c1c4_ab_alpha_pilot_result_2026_10_09.json` | 104,225 | 2026-10-09 22:55:04 | `bc7c35707b78` | 成果面 |
| 3008 | `results/_c1c4_ab_beta_pilot_result_2026_10_09.json` | 109,879 | 2026-10-09 22:59:59 | `fd72ebf836e1` | 成果面 |
| 3009 | `results/_c1c4_input_gap_fill_plan_2026_10_09.md` | 35,635 | 2026-10-09 17:27:41 | `9f5675633e03` | 成果面 |
| 3010 | `results/_c4_rejection_axis_reconciliation_judgment_2026_10_12.md` | 37,908 | 2026-10-12 17:10:11 | `f1ca2c59bed9` | 成果面 |
| 3011 | `results/_c4_scope_ruling_and_d1_requalification_register_2026_10_12.md` | 29,510 | 2026-10-12 17:32:00 | `b28540b999a6` | 成果面 |
| 3012 | `results/_c5_both_pillars_closed_effect_2026_10_17.md` | 24,464 | 2026-10-17 16:18:36 | `91fe9a16059d` | 成果面 |
| 3013 | `results/_c5_split_into_c5a_c5b_2026_10_17.md` | 28,902 | 2026-10-17 15:21:56 | `c9e304e43274` | 成果面 |
| 3014 | `results/_c5b_closure_verdict_2026_10_17.md` | 26,218 | 2026-10-17 16:04:06 | `660555b9b6be` | 成果面 |
| 3015 | `results/_c7_remote_timeline_correction_register_2026_10_14.md` | 10,314 | 2026-10-14 21:21:55 | `99703cba855f` | 成果面 |
| 3016 | `results/_canonical_face_scope_corrigendum_2026_10_16.md` | 14,502 | 2026-10-16 21:42:29 | `1b45571bddca` | 成果面 |
| 3017 | `results/_card_register_dir_verdict_2026_10_17.md` | 26,682 | 2026-10-17 16:48:10 | `a694e5d55ce1` | 成果面 |
| 3018 | `results/_card_register_relocation_mapping_2026_10_17.md` | 17,871 | 2026-10-17 17:02:03 | `ff69e7517f8d` | 成果面 |
| 3019 | `results/_card_register_relocation_register_2026_10_17.md` | 28,415 | 2026-10-17 17:02:49 | `8ca4b2d7320b` | 成果面 |
| 3020 | `results/_census_543_to_256_correction_2026_10_14.md` | 5,435 | 2026-10-14 21:06:17 | `b154a961c27f` | 成果面 |
| 3021 | `results/_census_exit_four_rulings_effect_2026_10_17.md` | 44,267 | 2026-10-17 20:51:12 | `ac0928f38b85` | 成果面 |
| 3022 | `results/_census_text_exec_inconsistency_register_2026_10_14.md` | 5,634 | 2026-10-14 21:06:17 | `55cd847688b3` | 成果面 |
| 3023 | `results/_chd_construction_domain_declaration_draft_2026_10_10.md` | 34,948 | 2026-10-10 23:35:41 | `17cf0d59cd7b` | 成果面 |
| 3024 | `results/_ci_gap_fill_alt_bc_aper_prime_2026_10_09.json` | 23,272 | 2026-10-09 17:43:45 | `f729a6a03a9e` | 成果面 |
| 3025 | `results/_citation_corrigenda_volume_2026_10_17.md` | 68,731 | 2026-10-17 11:34:33 | `7c20c38c501d` | 成果面 |
| 3026 | `results/_citation_no_utility_caliber_draft_2026_10_17.md` | 49,332 | 2026-10-17 13:22:41 | `536a3064ad38` | 成果面 |
| 3027 | `results/_classification_tree_anchor_erratum_2026_10_13.md` | 24,616 | 2026-10-13 21:35:42 | `781d6d106cb6` | 成果面 |
| 3028 | `results/_cleanup511_exec_register_2026_10_17.md` | 59,310 | 2026-10-17 10:24:27 | `36290316e075` | 成果面 |
| 3029 | `results/_cleanup_exec_register_2026_10_15.md` | 36,349 | 2026-10-15 10:27:29 | `d53036b01062` | 成果面 |
| 3030 | `results/_cleanup_inventory_2026_10_15.md` | 124,617 | 2026-10-15 10:24:17 | `9194110cb3f3` | 成果面 |
| 3031 | `results/_cleanup_r2_plus83_exec_register_2026_10_17.md` | 22,779 | 2026-10-17 12:02:35 | `e0492696dd12` | 成果面 |
| 3032 | `results/_cleanup_r2_repo_sub_exec_register_2026_10_17.md` | 21,686 | 2026-10-17 11:47:28 | `c6f89b961d14` | 成果面 |
| 3033 | `results/_clearance_evening_round_register_2026_09_29.md` | 18,201 | 2026-09-29 22:49:26 | `9c5543961e27` | 成果面 |
| 3034 | `results/_closeout_bucket_refresh_2026_10_09.md` | 28,851 | 2026-10-12 03:27:25 | `688fbbc3aa6b` | 成果面 |
| 3035 | `results/_closing_round_8_decisions_register_2026_10_09.md` | 2,151 | 2026-10-09 10:12:53 | `a28a478e14a8` | 成果面 |
| 3036 | `results/_clue_book_v06_backfill_and_dual_version_register_2026_10_12.md` | 12,839 | 2026-10-12 14:07:12 | `a0f72c702470` | 成果面 |
| 3037 | `results/_clue_side_dual_and_glm_commission_open_register_2026_10_12.md` | 14,446 | 2026-10-12 13:44:56 | `35bc0f1135cd` | 成果面 |
| 3038 | `results/_collision_196_2026_10_12.json` | 42,490 | 2026-10-12 10:44:48 | `3c95da787454` | 成果面 |
| 3039 | `results/_collision_baseline_update_and_disposition_2026_10_17.md` | 26,197 | 2026-10-17 10:38:53 | `f4f0fdc9915d` | 成果面 |
| 3040 | `results/_compound_numbering_census_2026_10_13.md` | 38,268 | 2026-10-13 21:07:56 | `956d19e4e670` | 成果面 |
| 3041 | `results/_continued_three_rulings_effect_2026_10_17.md` | 38,440 | 2026-10-17 16:56:04 | `4397d1a16805` | 成果面 |
| 3042 | `results/_copilot_agent_t2_t3_reply_register_2026_10_17.md` | 16,863 | 2026-10-17 15:46:16 | `1767d8fb075d` | 成果面 |
| 3043 | `results/_copilot_eq_grok_clarification_register_2026_10_17.md` | 25,694 | 2026-10-17 16:25:23 | `4d3f76687155` | 成果面 |
| 3044 | `results/_copilot_eq_grok_rulings_effect_2026_10_17.md` | 22,894 | 2026-10-17 16:39:11 | `d34d769afaca` | 成果面 |
| 3045 | `results/_copilot_reply_adoption_effect_2026_10_17.md` | 39,705 | 2026-10-17 16:05:37 | `4a89f8d3ddda` | 成果面 |
| 3046 | `results/_corpus_index_citation_surface_annotation_2026_10_12.md` | 28,951 | 2026-10-12 21:18:57 | `402b1f2754e9` | 成果面 |
| 3047 | `results/_count_chain_independent_review_2026_10_13.md` | 30,624 | 2026-10-13 21:36:35 | `8e8abcb0d323` | 成果面 |
| 3048 | `results/_counting_ban_release_channel_2026_10_16.md` | 16,740 | 2026-10-16 19:55:32 | `4b117aa1ceeb` | 成果面 |
| 3049 | `results/_cpath_e3_sign_normalization_2026_10_01.md` | 19,740 | 2026-10-01 14:06:32 | `e67ebccc82c9` | 成果面 |
| 3050 | `results/_criterion_application_scope_prereg_2026_10_01.md` | 50,322 | 2026-10-01 16:02:40 | `c4e3338619c6` | 成果面 |
| 3051 | `results/_d05_b_coincidence_checks_exec_2026_10_10.md` | 21,061 | 2026-10-10 12:10:50 | `840fbf08caf4` | 成果面 |
| 3052 | `results/_d05_b_coincidence_checks_exec_readings_2026_10_10.json` | 13,960 | 2026-10-10 12:08:44 | `586c435d1f15` | 成果面 |
| 3053 | `results/_d15_d16_caliber_and_authority_register_2026_10_12.md` | 18,397 | 2026-10-12 21:35:38 | `62604e6d6f06` | 成果面 |
| 3054 | `results/_d1_ab_deliberation_judgment_2026_10_15.md` | 46,542 | 2026-10-15 14:52:50 | `88c2af72ff7b` | 成果面 |
| 3055 | `results/_d1_backfill_intake_verdict_2026_10_01.md` | 42,115 | 2026-10-14 14:07:09 | `42a3858976f2` | 成果面 |
| 3056 | `results/_d1_c_effect_register_2026_10_15.md` | 30,686 | 2026-10-15 15:41:24 | `1bbfa5f33a61` | 成果面 |
| 3057 | `results/_d1d2_and_guide_adoption_supplement_2026_10_12.md` | 18,881 | 2026-10-12 16:32:13 | `4c60dcbec07f` | 成果面 |
| 3058 | `results/_d2_bytes_column_annotation_register_2026_10_13.md` | 8,269 | 2026-10-14 22:55:15 | `d1d0e9947d4c` | 成果面 |
| 3059 | `results/_d2_d6_erratum_and_annotation_register_2026_10_12.md` | 22,698 | 2026-10-12 21:34:18 | `d9da4f54482e` | 成果面 |
| 3060 | `results/_d6_l171_timeblock_restatement_register_2026_10_13.md` | 8,306 | 2026-10-14 22:55:15 | `8839995131a1` | 成果面 |
| 3061 | `results/_d8_boundary_revision_register_2026_09_30.md` | 32,406 | 2026-09-30 14:00:09 | `b46370bb9e3b` | 成果面 |
| 3062 | `results/_d8_collection_ledger_2026_09_30.md` | 20,290 | 2026-09-30 16:42:14 | `031dd8429048` | 成果面 |
| 3063 | `results/_d8_supplement_open_questions_2026_09_30.md` | 24,833 | 2026-09-30 13:14:41 | `579b375e9508` | 成果面 |
| 3064 | `results/_d9_base_reissue_2026_10_13.md` | 47,738 | 2026-10-13 23:24:08 | `c7bb38f60ffe` | 成果面 |
| 3065 | `results/_d9_e2e_backup_2026_10_13/_s4_heldout_sampling_seedprime_items_2026_10_10.json` | 15,409 | 2026-10-10 23:07:39 | `6cbb8ba01bfb` | 成果面 |
| 3066 | `results/_d9_e2e_backup_2026_10_13/_s4_heldout_sampling_seedthird_items_2026_10_11.json` | 43,130 | 2026-10-11 16:03:31 | `5777a07c608a` | 成果面 |
| 3067 | `results/_d9_e2e_backup_2026_10_13/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | 22,646 | 2026-10-11 16:03:31 | `784f042bf93d` | 成果面 |
| 3068 | `results/_d9_e2e_backup_2026_10_13/_s5doubleprime_five_lines_readings_2026_10_11.json` | 16,099 | 2026-10-11 18:14:08 | `839fb5452578` | 成果面 |
| 3069 | `results/_d9_e2e_backup_2026_10_13/_stage3_trigger_readings_items_2026_10_11.json` | 21,049 | 2026-10-11 16:52:40 | `079108c62a82` | 成果面 |
| 3070 | `results/_d9_e2e_backup_2026_10_13/_v3_recheck_05_result_2026_09_28.json` | 450,701 | 2026-09-28 13:28:21 | `f63b36b75a51` | 成果面 |
| 3071 | `results/_d9_e2e_disposition_and_f4_closure_register_2026_10_13.md` | 22,149 | 2026-10-13 09:36:44 | `467b7c10b466` | 成果面 |
| 3072 | `results/_d9_e2e_rerun_backup_2026_10_13/_s4_heldout_sampling_seedprime_items_2026_10_10.json` | 15,409 | 2026-10-13 00:35:32 | `6cbb8ba01bfb` | 成果面 |
| 3073 | `results/_d9_e2e_rerun_for_p2_2026_10_13.md` | 26,404 | 2026-10-13 22:12:48 | `064c27e3b756` | 成果面 |
| 3074 | `results/_d9_e2e_run_register_2026_10_13.md` | 12,581 | 2026-10-13 00:25:47 | `af22751858d1` | 成果面 |
| 3075 | `results/_d9_e2e_run_register_v2_2026_10_13.md` | 26,904 | 2026-10-13 00:37:49 | `72a2a0c90985` | 成果面 |
| 3076 | `results/_d9_h2_r1files_repair_register_2026_10_13.md` | 14,026 | 2026-10-13 00:17:54 | `ef3317e5dbb3` | 成果面 |
| 3077 | `results/_d9_independent_review_2026_10_12.md` | 22,644 | 2026-10-12 23:37:47 | `732cfae29bbc` | 成果面 |
| 3078 | `results/_d9_relpath_map_mojibake_defect_register_2026_10_12.md` | 5,930 | 2026-10-12 17:01:51 | `0ec673877e14` | 成果面 |
| 3079 | `results/_d9_relpath_rewrite_map_2026_10_12.md` | 21,352 | 2026-10-12 16:16:20 | `c3167a531e0e` | 成果面 |
| 3080 | `results/_d9_relpath_rewrite_map_v2_2026_10_12.md` | 28,112 | 2026-10-12 17:03:14 | `d6ff7e9b4bd6` | 成果面 |
| 3081 | `results/_d9_residual_repair_register_2026_10_12.md` | 14,927 | 2026-10-12 23:55:01 | `cddb7a196473` | 成果面 |
| 3082 | `results/_d9_rewrite_execution_register_2026_10_12.md` | 20,432 | 2026-10-12 16:36:12 | `0ea7852c4511` | 成果面 |
| 3083 | `results/_d9_runner_input_relpath_erratum_2026_10_12.md` | 23,592 | 2026-10-12 15:27:24 | `7395034a09aa` | 成果面 |
| 3084 | `results/_d_dimension_canonical_coexistence_note_2026_10_16.md` | 8,941 | 2026-10-16 19:22:10 | `a9485534ff5b` | 成果面 |
| 3085 | `results/_dangling_630_adoption_and_283_corrigendum_2026_10_17.md` | 18,524 | 2026-10-17 10:50:42 | `2ce9301be94f` | 成果面 |
| 3086 | `results/_dangling_630_remediation_list_2026_10_17.md` | 120,723 | 2026-10-17 10:18:20 | `5bc372de9a84` | 成果面 |
| 3087 | `results/_degradation_reversal_guide_dual_adoption_register_2026_10_12.md` | 11,191 | 2026-10-12 16:15:13 | `65e7c9c521ba` | 成果面 |
| 3088 | `results/_degradation_reversal_guide_kimi_2026_10_12.md` | 7,408 | 2026-10-12 10:47:11 | `11f8422fc0f9` | 成果面 |
| 3089 | `results/_deliverables_verification_and_v5_handover_pending_2026_10_12.md` | 12,636 | 2026-10-12 13:06:58 | `a4fd656650a4` | 成果面 |
| 3090 | `results/_discipline_scope_review_and_harm_audit_2026_10_13.md` | 6,081 | 2026-10-13 23:41:49 | `58572775ecd1` | 成果面 |
| 3091 | `results/_discipline_scope_review_corrigendum_2026_10_13.md` | 2,546 | 2026-10-13 23:46:56 | `bd343010ae3f` | 成果面 |
| 3092 | `results/_duplicate_name_six_items_attribution_register_2026_10_12.md` | 8,476 | 2026-10-12 21:08:08 | `42788a70a913` | 成果面 |
| 3093 | `results/_erratum_3_14H_caliber_impact_2026_10_17.md` | 41,388 | 2026-10-17 16:12:54 | `6aab999b02ac` | 成果面 |
| 3094 | `results/_erratum_arm_label_transcription_2026_10_17.md` | 19,052 | 2026-10-17 17:05:14 | `45452ccac4ac` | 成果面 |
| 3095 | `results/_erratum_refonly_draft_alias_found_2026_10_17.md` | 5,639 | 2026-10-17 14:38:04 | `198126e7ef6e` | 成果面 |
| 3096 | `results/_esc3_esc6_resolution_2026_10_17.md` | 28,717 | 2026-10-17 19:03:44 | `509e52734292` | 成果面 |
| 3097 | `results/_esc5_adoption_and_ritt_remeasure_effect_2026_10_17.md` | 34,206 | 2026-10-17 19:50:36 | `e550e344a258` | 成果面 |
| 3098 | `results/_esc5_verdict_2026_10_17.md` | 27,258 | 2026-10-17 19:36:24 | `d970bb175672` | 成果面 |
| 3099 | `results/_exp04_h_contrast_readings_2026_10_10.json` | 72,704 | 2026-10-10 10:05:05 | `106e8667be2d` | 成果面 |
| 3100 | `results/_exp04_h_contrast_readings_2026_10_10.md` | 17,386 | 2026-10-10 10:06:54 | `ac571bfe4d1d` | 成果面 |
| 3101 | `results/_exp06_independent_check_2026_10_10.json` | 20,480 | 2026-10-10 10:31:42 | `4c36c376ab9c` | 成果面 |
| 3102 | `results/_exp06_selfverified_renaming_note_2026_10_10.md` | 34,554 | 2026-10-10 11:25:56 | `8b4ec41a37dd` | 成果面 |
| 3103 | `results/_exp06_selfverified_runner_fix_note_2026_10_10.md` | 17,052 | 2026-10-10 10:51:43 | `247398b687e6` | 成果面 |
| 3104 | `results/_exp06_supplement_four_gaps_2026_10_10.md` | 26,519 | 2026-10-10 10:33:13 | `9f86cc5be8e9` | 成果面 |
| 3105 | `results/_ext5_verdict_2026_10_17.md` | 63,647 | 2026-10-17 18:39:47 | `80a81bd525d4` | 成果面 |
| 3106 | `results/_external_commission_gemini4_ge01_theory_inputs_2026_10_15_dispatch.md` | 8,361 | 2026-10-15 11:21:48 | `70fe266e87d6` | 成果面 |
| 3107 | `results/_external_commission_gemini4_ge01_theory_inputs_2026_10_15_draft.md` | 10,085 | 2026-10-15 11:14:07 | `904828e7553f` | 成果面 |
| 3108 | `results/_f12_kd_disposition_register_2026_10_15.md` | 12,661 | 2026-10-15 10:20:26 | `9c0427685a19` | 成果面 |
| 3109 | `results/_f2_branch_fix_register_2026_09_29.md` | 22,940 | 2026-09-29 22:57:03 | `a0cab58c032e` | 成果面 |
| 3110 | `results/_f2_closeout_note_2026_09_29.md` | 16,317 | 2026-09-29 23:05:32 | `1599cb99abf3` | 成果面 |
| 3111 | `results/_f4_direction1_domain_effectivity_2026_10_11.md` | 40,301 | 2026-10-11 14:05:56 | `fd4ec7559342` | 成果面 |
| 3112 | `results/_face_r_coexist_verdict_2026_10_17.md` | 37,604 | 2026-10-17 20:30:56 | `0fd3788e2d3b` | 成果面 |
| 3113 | `results/_fail_h0_verdict_2026_10_17.md` | 41,481 | 2026-10-17 18:26:55 | `c8794d87b4b6` | 成果面 |
| 3114 | `results/_fake_verdict_reverify_sixitem_ledger_2026_09_30.md` | 40,957 | 2026-09-30 17:25:45 | `41d7b76ea4d6` | 成果面 |
| 3115 | `results/_family_de_stale_refresh_matrix_2026_10_14.md` | 78,861 | 2026-10-14 02:26:22 | `7d67b6af125a` | 成果面 |
| 3116 | `results/_family_de_stale_refresh_repo_exec_2026_10_14.md` | 31,151 | 2026-10-14 12:57:58 | `55155ec5f430` | 成果面 |
| 3117 | `results/_family_de_stale_refresh_sub_exec_2026_10_14.md` | 31,813 | 2026-10-14 11:47:48 | `c7d20b3c18ba` | 成果面 |
| 3118 | `results/_five_terminal_judgments_ruling_2026_10_10.md` | 27,315 | 2026-10-10 12:28:00 | `9e96d0a1ba12` | 成果面 |
| 3119 | `results/_fiveverdict_census_2026_10_17.md` | 31,237 | 2026-10-17 20:23:57 | `0b9512c6b68b` | 成果面 |
| 3120 | `results/_fivezero_final_audit_2026_10_17.md` | 46,339 | 2026-10-17 18:09:49 | `95118aa704db` | 成果面 |
| 3121 | `results/_forgotten_recovery_register_2026_10_08.md` | 34,287 | 2026-10-08 16:33:10 | `c981347cffad` | 成果面 |
| 3122 | `results/_four_class_backtrace_inventory_2026_10_13_r1.md` | 29,809 | 2026-10-13 21:21:52 | `1b28a9467567` | 成果面 |
| 3123 | `results/_four_items_alternative_deliberation_judgment_2026_10_13.md` | 44,728 | 2026-10-13 21:50:06 | `0b5bb95a86d7` | 成果面 |
| 3124 | `results/_freeze_criterion_rewire_design_2026_10_17.md` | 42,399 | 2026-10-17 23:28:26 | `02c385de48ac` | 成果面 |
| 3125 | `results/_freeze_face_four_rulings_effect_2026_10_17.md` | 41,068 | 2026-10-17 23:35:48 | `1e512ea146d3` | 成果面 |
| 3126 | `results/_freeze_preexp_design_2026_10_17.md` | 40,906 | 2026-10-17 20:30:58 | `d52a5d94a002` | 成果面 |
| 3127 | `results/_freeze_preexp_exec_2026_10_17.md` | 34,681 | 2026-10-17 22:51:01 | `547da6852c98` | 成果面 |
| 3128 | `results/_freeze_preexp_exec_r2_2026_10_17.md` | 52,887 | 2026-10-17 23:56:27 | `fd3656a22b1c` | 成果面 |
| 3129 | `results/_freeze_rewire_approval_effect_2026_10_17.md` | 62,895 | 2026-10-17 23:53:38 | `8fc84dd44b6b` | 成果面 |
| 3130 | `results/_g1_archive_zone_search_register_2026_10_12.md` | 14,175 | 2026-10-12 22:58:47 | `3f293b8c5444` | 成果面 |
| 3131 | `results/_g1_closure_register_2026_10_12.md` | 20,423 | 2026-10-12 23:07:23 | `10bd066ab5bf` | 成果面 |
| 3132 | `results/_g2_residual_cause_register_2026_10_12.md` | 26,134 | 2026-10-12 23:28:46 | `e6b881562420` | 成果面 |
| 3133 | `results/_g5_ccp_execution_prereqs_2026_10_10.md` | 32,815 | 2026-10-10 18:52:37 | `ab1a07ae2fd1` | 成果面 |
| 3134 | `results/_g5_ccp_seed_designation_revision_2026_10_10.md` | 20,979 | 2026-10-10 19:15:26 | `b53f40abb90b` | 成果面 |
| 3135 | `results/_g5_rejudgment_construction_change_plan_2026_10_10.md` | 57,004 | 2026-10-10 18:22:43 | `fa0001a6dd0a` | 成果面 |
| 3136 | `results/_gamma_taucert_scope_delimitation_2026_10_17.md` | 37,104 | 2026-10-17 20:30:50 | `7374c29a8d4e` | 成果面 |
| 3137 | `results/_gamma_taucert_sourcing_2026_10_15.md` | 34,667 | 2026-10-15 15:47:25 | `6630447e5ec7` | 成果面 |
| 3138 | `results/_gap10_four_rulings_effect_2026_10_17.md` | 35,339 | 2026-10-17 19:05:22 | `b5596dd2abbb` | 成果面 |
| 3139 | `results/_gate1_count_defect_erratum_2026_10_13.md` | 23,027 | 2026-10-13 17:07:58 | `41bfe0a7c58d` | 成果面 |
| 3140 | `results/_gate1_five_zero_recheck_2026_10_12.md` | 20,330 | 2026-10-12 22:14:32 | `9c70140c7b02` | 成果面 |
| 3141 | `results/_gate1_five_zero_recheck_glm_scope_2026_10_13.md` | 34,647 | 2026-10-13 00:30:21 | `2f27acf42897` | 成果面 |
| 3142 | `results/_gate1_gap_residuals_adoption_register_2026_10_12.md` | 30,908 | 2026-10-12 16:18:12 | `b84b9808fc71` | 成果面 |
| 3143 | `results/_gate1_gap_three_items_disposition_2026_10_12.md` | 36,087 | 2026-10-12 15:33:02 | `5cf848421c2b` | 成果面 |
| 3144 | `results/_gate1_glm_reply_integration_register_2026_10_13.md` | 41,753 | 2026-10-13 15:41:05 | `16198528bc26` | 成果面 |
| 3145 | `results/_gate1_scope_inclusion_glm_commission_register_2026_10_13.md` | 5,016 | 2026-10-13 00:26:38 | `236d08c0b70d` | 成果面 |
| 3146 | `results/_gate1_unclosed_classification_tree_2026_10_13.md` | 50,305 | 2026-10-13 16:36:09 | `0b33e0528bc2` | 成果面 |
| 3147 | `results/_gate1_unclosed_writeoff_register_2026_10_13.md` | 25,318 | 2026-10-13 17:07:49 | `5cea0cc0148c` | 成果面 |
| 3148 | `results/_gate_one_registers_erratum_distribution_and_path_2026_10_12.md` | 13,901 | 2026-10-12 03:21:02 | `69ac4fb16a4f` | 成果面 |
| 3149 | `results/_gate_one_reopened_and_stage2_rejection_register_2026_10_12.md` | 8,644 | 2026-10-12 14:52:56 | `b2f6f55e76b7` | 成果面 |
| 3150 | `results/_ge01_5anchor_json_approval_register_2026_10_14.md` | 29,776 | 2026-10-14 16:45:12 | `d9b30c816e2c` | 成果面 |
| 3151 | `results/_ge01_5anchor_json_draft_2026_10_14.md` | 33,387 | 2026-10-14 16:29:37 | `9898a19d9a1d` | 成果面 |
| 3152 | `results/_ge01_5anchor_json_register_2026_10_14.md` | 31,882 | 2026-10-14 20:32:36 | `65000a1ac5bc` | 成果面 |
| 3153 | `results/_ge01_ab_pilot_selection_design_draft_2026_10_13.md` | 45,790 | 2026-10-13 16:21:38 | `ca89332e6f18` | 成果面 |
| 3154 | `results/_ge01_c2_canonical_effect_register_2026_10_14.md` | 27,902 | 2026-10-14 15:04:51 | `b92a7830d38a` | 成果面 |
| 3155 | `results/_ge01_c3_gaps_disposition_2026_10_14.md` | 33,390 | 2026-10-14 14:49:07 | `0e796a657868` | 成果面 |
| 3156 | `results/_ge01_c5_disposition_register_2026_10_14.md` | 16,314 | 2026-10-14 15:14:23 | `181aa4d580a1` | 成果面 |
| 3157 | `results/_ge01_calculator_rebuild_design_2026_10_14.md` | 46,007 | 2026-10-14 02:48:57 | `8ab699f017c8` | 成果面 |
| 3158 | `results/_ge01_calculator_rebuild_register_2026_10_14.md` | 31,515 | 2026-10-14 16:05:46 | `0bb909c36108` | 成果面 |
| 3159 | `results/_ge01_d1_theory_input_disposition_2026_10_14.md` | 36,272 | 2026-10-14 16:34:23 | `657fe57c8cbd` | 成果面 |
| 3160 | `results/_ge01_d1_theory_input_sourcing_design_2026_10_14.md` | 38,222 | 2026-10-14 15:17:07 | `f9b8a276a941` | 成果面 |
| 3161 | `results/_ge01_ecr_anchor_convergence_deliberation_2026_10_14.md` | 26,832 | 2026-10-15 09:09:28 | `b32ca40ec103` | 成果面 |
| 3162 | `results/_ge01_ecr_anchor_effect_register_2026_10_15.md` | 15,707 | 2026-10-15 09:57:40 | `2c7c202aafec` | 成果面 |
| 3163 | `results/_ge01_ecr_anchor_sourcing_design_2026_10_14.md` | 41,324 | 2026-10-14 20:43:21 | `d4b43c58c847` | 成果面 |
| 3164 | `results/_ge01_ecr_baseline_invalid_register_2026_10_14.md` | 22,796 | 2026-10-14 17:07:09 | `dcdfe7c0bd09` | 成果面 |
| 3165 | `results/_ge01_epsilon_grid_exec_register_2026_10_16.md` | 45,389 | 2026-10-16 16:56:48 | `f8de4abb5e12` | 成果面 |
| 3166 | `results/_ge01_epsilon_sensitivity_grid_design_r1_2026_10_13.md` | 35,956 | 2026-10-14 00:13:17 | `7551c47d3ece` | 成果面 |
| 3167 | `results/_ge01_frozen_runs_on_disk_erratum_2026_10_13.md` | 22,559 | 2026-10-13 23:52:05 | `6aa7fb58b270` | 成果面 |
| 3168 | `results/_ge01_full_1494_exec_2026_10_16.md` | 32,363 | 2026-10-16 22:19:51 | `e0efc8501305` | 成果面 |
| 3169 | `results/_ge01_full_1494_exec_r1_2026_10_16.md` | 46,115 | 2026-10-16 23:02:10 | `515128a23182` | 成果面 |
| 3170 | `results/_ge01_full_1494_freeze_2026_10_16.md` | 14,129 | 2026-10-16 22:38:20 | `171d1b6d5725` | 成果面 |
| 3171 | `results/_ge01_full_1494_resume32_register_2026_10_16.md` | 41,003 | 2026-10-16 23:41:15 | `ae4b90375fe7` | 成果面 |
| 3172 | `results/_ge01_gt_kill_family_byte_stream_effect_register_2026_10_14.md` | 29,189 | 2026-10-14 20:30:44 | `e631795149eb` | 成果面 |
| 3173 | `results/_ge01_gt_kill_family_carrier_construction_draft_2026_10_14.md` | 32,568 | 2026-10-15 09:10:57 | `75a818b2654f` | 成果面 |
| 3174 | `results/_ge01_gt_kill_family_generation_design_2026_10_14.md` | 32,857 | 2026-10-14 15:19:59 | `6ede1d7a2616` | 成果面 |
| 3175 | `results/_ge01_gt_kill_family_member_table_register_2026_10_14.md` | 28,470 | 2026-10-14 16:32:20 | `ccf1071ce431` | 成果面 |
| 3176 | `results/_ge01_launch_gate_recheck_2026_10_17.md` | 82,206 | 2026-10-17 11:40:09 | `de8fd5291962` | 成果面 |
| 3177 | `results/_ge01_numeric_literature_search_2026_10_14.md` | 28,399 | 2026-10-14 01:44:04 | `f868822c6fc1` | 成果面 |
| 3178 | `results/_ge01_prereg_5anchor.json` | 10,701 | 2026-10-14 17:52:13 | `4b020eb04605` | 成果面 |
| 3179 | `results/_ge01_prereg_5anchor_v2.json` | 21,629 | 2026-10-15 11:21:14 | `f06313373fc6` | 成果面 |
| 3180 | `results/_ge01_prereg_5anchor_v2_lock_register_2026_10_15.md` | 17,808 | 2026-10-15 11:22:24 | `ed3b544d33a6` | 成果面 |
| 3181 | `results/_ge01_prereg_5anchor_v3.json` | 35,911 | 2026-10-15 13:00:07 | `0c269b9558da` | 成果面 |
| 3182 | `results/_ge01_prereg_prelexp_selection_design_v2_2026_10_13.md` | 46,864 | 2026-10-14 00:05:38 | `6fc11dacaf24` | 成果面 |
| 3183 | `results/_ge01_prereg_seven_requirements_draft_2026_10_13.md` | 39,337 | 2026-10-13 15:57:45 | `0a031a9795a9` | 成果面 |
| 3184 | `results/_ge01_readiness_after_prereg_effect_2026_10_13.md` | 31,736 | 2026-10-13 23:40:59 | `5a72c931148a` | 成果面 |
| 3185 | `results/_ge01_s3_v_adjudicable_recheck_2026_10_16.md` | 51,621 | 2026-10-16 20:45:18 | `3873af2cce4f` | 成果面 |
| 3186 | `results/_ge01_s3b_v_exec_2026_10_16.md` | 54,012 | 2026-10-16 21:23:27 | `89b3be872de8` | 成果面 |
| 3187 | `results/_ge01_spec_anchor_canonical_register_2026_10_14.md` | 22,828 | 2026-10-14 14:09:36 | `fb73dc317eb5` | 成果面 |
| 3188 | `results/_ge01_spec_anchor_erratum_2026_10_14.md` | 18,129 | 2026-10-14 01:14:52 | `2eeb522748ca` | 成果面 |
| 3189 | `results/_ge01_t2_t3_null_resolution_design_2026_10_13.md` | 43,820 | 2026-10-14 00:30:49 | `c2af59477178` | 成果面 |
| 3190 | `results/_ge01_unblock_effect_register_2026_10_14.md` | 24,534 | 2026-10-14 16:47:54 | `277a6f9e4d94` | 成果面 |
| 3191 | `results/_ge01_unblock_progress_2026_10_14.md` | 25,315 | 2026-10-14 14:14:00 | `893eddf769a6` | 成果面 |
| 3192 | `results/_ge02_anchor_landing_build_register_2026_10_16.md` | 15,311 | 2026-10-16 19:57:09 | `629567744899` | 成果面 |
| 3193 | `results/_ge02_anchor_landing_effect_register_2026_10_16.md` | 18,441 | 2026-10-16 20:17:44 | `5347521e5add` | 成果面 |
| 3194 | `results/_gemini4_reply_verification_register_2026_10_15.md` | 33,393 | 2026-10-15 14:11:26 | `793986174b23` | 成果面 |
| 3195 | `results/_ghostref_copy_log_2026_09_23.json` | 129,780 | 2026-09-23 15:11:45 | `8cd133d0896f` | 成果面 |
| 3196 | `results/_github_delete_and_suspect_lists_2026_10_17.md` | 29,338 | 2026-10-17 14:57:48 | `0a350e4e5bac` | 成果面 |
| 3197 | `results/_github_suspect_rulings_effect_2026_10_17.md` | 51,654 | 2026-10-17 16:02:50 | `f49079f46c2b` | 成果面 |
| 3198 | `results/_gitignore_rx_fix_adoption_register_2026_10_17.md` | 13,078 | 2026-10-17 10:50:42 | `277bfe56b9ee` | 成果面 |
| 3199 | `results/_gitignore_rx_fix_drift_register_2026_10_17.md` | 11,747 | 2026-10-17 10:32:40 | `bbb98cd5e9ce` | 成果面 |
| 3200 | `results/_glm_crossface_item4_register_2026_10_13.md` | 5,345 | 2026-10-13 15:52:03 | `2d8d5e8c58be` | 成果面 |
| 3201 | `results/_glm_delivery_face_disposition_register_2026_10_13.md` | 16,662 | 2026-10-13 23:13:28 | `4d9f84d04cae` | 成果面 |
| 3202 | `results/_glm_delivery_pack_verification_2026_10_14.md` | 12,580 | 2026-10-14 15:26:16 | `a2d1a9187ee9` | 成果面 |
| 3203 | `results/_glm_evidence_pack_unpack_register_2026_10_13.md` | 28,909 | 2026-10-13 16:02:16 | `5762be8a68f8` | 成果面 |
| 3204 | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_d1_ruling_and_s3_transition_2026_10_01.md` | 28,370 | 2026-10-13 15:56:54 | `dc9cb0e02922` | 成果面 |
| 3205 | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_kv3s_3_2_terminal_verdict_2026_10_01.md` | 32,296 | 2026-10-14 14:07:09 | `693eefdd7a82` | 成果面 |
| 3206 | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_limb_reading_verdict_kv3s33_2026_10_01.md` | 56,321 | 2026-10-13 15:56:54 | `4aba41f67db5` | 成果面 |
| 3207 | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_s3_d1_rulings_supplement_register_2026_10_01.md` | 28,762 | 2026-10-14 14:07:09 | `303bf7c6f34d` | 成果面 |
| 3208 | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_s3_d1fill_recount_2026_10_01.md` | 22,877 | 2026-10-13 15:56:54 | `a7dff824ed56` | 成果面 |
| 3209 | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_t1_gate_closure_and_recompute_verdict_2026_10_01.md` | 72,926 | 2026-10-14 14:07:09 | `087a18ec37d0` | 成果面 |
| 3210 | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_t1_substrate_gap_census_2026_10_01.md` | 32,371 | 2026-10-13 15:56:54 | `62fb594be3f9` | 成果面 |
| 3211 | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_v3_s_prereg_v1_2026_09_27.md` | 46,836 | 2026-10-13 15:56:54 | `ef5a40554960` | 成果面 |
| 3212 | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/deposon_g1_mindmap_demo.json` | 3,041 | 2026-10-13 15:56:54 | `55428f6bd848` | 成果面 |
| 3213 | `results/_glm_wholepack_irreproducible_erratum_2026_10_14.md` | 24,905 | 2026-10-14 12:57:51 | `0291002f749e` | 成果面 |
| 3214 | `results/_gt_kill_family_carrier_draft_register_2026_10_15.md` | 22,501 | 2026-10-15 09:50:09 | `d8c41976ef1b` | 成果面 |
| 3215 | `results/_gt_kill_line_carrier_effect_register_2026_10_15.md` | 25,941 | 2026-10-15 11:12:43 | `e40f060fa3a3` | 成果面 |
| 3216 | `results/_h_budget_measurement_exec_2026_10_15.md` | 25,705 | 2026-10-15 15:49:09 | `c5a58305876a` | 成果面 |
| 3217 | `results/_h_three_domain_naming_caliber_2026_10_16.md` | 24,576 | 2026-10-16 15:11:45 | `4370b5fc5758` | 成果面 |
| 3218 | `results/_harness_anchor_reconcile_register_2026_10_16.md` | 26,023 | 2026-10-16 11:00:45 | `4de10aad8f0b` | 成果面 |
| 3219 | `results/_harness_mask_correct_value_validation_2026_10_17.md` | 21,741 | 2026-10-17 23:36:19 | `b7d638ebef6e` | 成果面 |
| 3220 | `results/_interval_420_600_upper_bound_deliberation_2026_10_16.md` | 34,256 | 2026-10-16 13:57:41 | `4d2c65968311` | 成果面 |
| 3221 | `results/_interval_ceiling_post_lock_deliberation_2026_10_16.md` | 46,687 | 2026-10-16 16:53:10 | `fce2f69802b9` | 成果面 |
| 3222 | `results/_interval_range_post_lock_note_2026_10_16.md` | 16,253 | 2026-10-16 19:32:50 | `21737d3a40d5` | 成果面 |
| 3223 | `results/_is_corr_pair_caliber_revision_proposal_2026_10_09.md` | 33,497 | 2026-10-09 14:46:03 | `084c7d20067f` | 成果面 |
| 3224 | `results/_judgement_criteria_reference_only_no_utility_draft_2026_10_17.md` | 42,968 | 2026-10-17 14:16:06 | `f5bad2e2ff00` | 成果面 |
| 3225 | `results/_k_v3df_0_1_four_readings_2026_10_09.json` | 65,507 | 2026-10-09 11:24:10 | `e87937d55471` | 成果面 |
| 3226 | `results/_k_v3df_0_1_four_readings_2026_10_09.md` | 46,522 | 2026-10-09 11:24:10 | `53c28ca1ae3d` | 成果面 |
| 3227 | `results/_k_v3s_4_3_frozen_recompute_2026_10_09.md` | 26,674 | 2026-10-09 14:27:36 | `1c1494083255` | 成果面 |
| 3228 | `results/_kd04_c_denominator_expansion_readings_2026_10_10.json` | 23,314 | 2026-10-10 11:44:09 | `249009e6a0cc` | 成果面 |
| 3229 | `results/_kd04_c_denominator_killline_prereg_2026_10_10.md` | 24,527 | 2026-10-10 11:27:33 | `8f2025e9de6f` | 成果面 |
| 3230 | `results/_kd13_ecr_anchor_binding_deliberation_2026_10_15.md` | 32,067 | 2026-10-15 11:46:36 | `99b578a1be2c` | 成果面 |
| 3231 | `results/_kd14_null_u_carrier_deliberation_2026_10_16.md` | 35,608 | 2026-10-16 22:20:08 | `0a6279970446` | 成果面 |
| 3232 | `results/_kd14_null_u_carrier_effect_register_2026_10_16.md` | 24,828 | 2026-10-16 22:40:00 | `141816a6aec9` | 成果面 |
| 3233 | `results/_kd1_preexp_contrast_2026_10_17.md` | 27,149 | 2026-10-17 19:23:16 | `351d18d74934` | 成果面 |
| 3234 | `results/_kd4_adoption_and_caliber_pack_effect_2026_10_17.md` | 32,577 | 2026-10-17 17:09:35 | `ce1604dfd251` | 成果面 |
| 3235 | `results/_kd4_homology_verdict_2026_10_17.md` | 32,823 | 2026-10-17 16:54:31 | `1992b9d359a8` | 成果面 |
| 3236 | `results/_kd_11_12_resolution_register_2026_10_16.md` | 18,606 | 2026-10-16 20:52:09 | `807932c7e1c8` | 成果面 |
| 3237 | `results/_kd_13_9_3_closure_register_2026_10_16.md` | 19,461 | 2026-10-16 22:19:45 | `410f885430a4` | 成果面 |
| 3238 | `results/_kd_2_4_6_caliber_note_2026_10_16.md` | 20,497 | 2026-10-16 21:38:38 | `0fd67a2075b7` | 成果面 |
| 3239 | `results/_kd_flip_census_2026_10_17.md` | 38,344 | 2026-10-17 21:38:25 | `cbb42aae0865` | 成果面 |
| 3240 | `results/_kd_gap_resolution_rulings_effect_2026_10_17.md` | 38,813 | 2026-10-17 20:15:17 | `10e40a51c9c1` | 成果面 |
| 3241 | `results/_kd_gap_survey_2026_10_17.md` | 45,716 | 2026-10-17 20:01:00 | `592a50470e76` | 成果面 |
| 3242 | `results/_kd_ge01_eps4_scope_escalation_note_2026_10_16.md` | 26,411 | 2026-10-16 23:36:54 | `731144fbda94` | 成果面 |
| 3243 | `results/_kd_h5_h6_recheck_2026_10_14.md` | 22,205 | 2026-10-14 02:00:49 | `d9459768e058` | 成果面 |
| 3244 | `results/_kd_s3_2_3_corrigendum_2026_10_16.md` | 26,395 | 2026-10-16 21:26:56 | `5c4fd13640f4` | 成果面 |
| 3245 | `results/_kd_s3b1_kd1_n7_rulings_effect_2026_10_17.md` | 49,252 | 2026-10-17 19:42:40 | `e09780d24a7a` | 成果面 |
| 3246 | `results/_kd_s3b1_verdict_2026_10_17.md` | 45,846 | 2026-10-17 19:22:50 | `ed36d0171672` | 成果面 |
| 3247 | `results/_kd_s3b5_kd1_esc36_batch_lock_effect_2026_10_17.md` | 48,246 | 2026-10-17 19:25:20 | `3ecf179b83a1` | 成果面 |
| 3248 | `results/_kd_u1_u4_rulings_effect_2026_10_17.md` | 30,072 | 2026-10-17 19:13:53 | `4500a4715f3b` | 成果面 |
| 3249 | `results/_kd_u5_u6_s3b4_rulings_effect_2026_10_17.md` | 38,534 | 2026-10-17 19:22:09 | `85702808df0c` | 成果面 |
| 3250 | `results/_kd_u6_readside_rewire_validation_2026_10_17.md` | 24,961 | 2026-10-17 23:59:20 | `751205f0368f` | 成果面 |
| 3251 | `results/_kd_unambiguous_meaning_ruling_2026_10_10.md` | 24,898 | 2026-10-10 11:36:58 | `f22ede7226d2` | 成果面 |
| 3252 | `results/_kd_writing_convention_guidance_2026_10_09.md` | 20,179 | 2026-10-14 12:55:36 | `f47031323865` | 成果面 |
| 3253 | `results/_kdb2r2_kd14_merge_governance_2026_10_17.md` | 26,107 | 2026-10-17 23:05:58 | `4fdadf27b70c` | 成果面 |
| 3254 | `results/_kdb2r3_u13_rulings_effect_2026_10_17.md` | 35,207 | 2026-10-17 18:58:09 | `688424929409` | 成果面 |
| 3255 | `results/_kdk45_remeasure_2026_10_17.md` | 31,662 | 2026-10-17 20:17:26 | `25ff6e4f31bc` | 成果面 |
| 3256 | `results/_kill_line_field_value_sourcing_2026_10_15.md` | 19,471 | 2026-10-15 11:42:48 | `e5615b993000` | 成果面 |
| 3257 | `results/_killface_v1_design_draft_2026_10_16.md` | 62,353 | 2026-10-16 19:25:57 | `890e923b0f9d` | 成果面 |
| 3258 | `results/_killface_v1_effect_register_2026_10_16.md` | 21,872 | 2026-10-16 19:46:45 | `98aabe87ae11` | 成果面 |
| 3259 | `results/_kl_m41_3_remeasure_2026_10_17.md` | 36,936 | 2026-10-17 21:31:30 | `20a1ce111547` | 成果面 |
| 3260 | `results/_kl_m41_3_reverdict_2026_10_17.md` | 61,667 | 2026-10-17 21:44:34 | `63625672139a` | 成果面 |
| 3261 | `results/_kl_m41_3_reverdict_adoption_effect_2026_10_17.md` | 38,651 | 2026-10-17 21:59:26 | `27545e411171` | 成果面 |
| 3262 | `results/_kl_m41_3_three_seed_exec_2026_10_16.md` | 41,140 | 2026-10-16 19:43:13 | `3e13344783b0` | 成果面 |
| 3263 | `results/_kl_m41_3_verdict_2026_10_17.md` | 33,138 | 2026-10-17 18:25:11 | `5dc4e089f458` | 成果面 |
| 3264 | `results/_klm41_2_bootstrap_ci_exec_2026_10_16.md` | 45,192 | 2026-10-16 11:55:08 | `a467a77d895f` | 成果面 |
| 3265 | `results/_krj3_kd_registry_correction_2026_10_12.md` | 16,648 | 2026-10-12 17:33:16 | `4d514147670a` | 成果面 |
| 3266 | `results/_kt_a1_anchor_drift_root_cause_2026_10_14.md` | 37,430 | 2026-10-14 02:26:53 | `ba19ab186747` | 成果面 |
| 3267 | `results/_kt_a1_v0_lineage_corrigendum_2026_10_14.md` | 31,849 | 2026-10-14 02:09:08 | `e2c35c2ac858` | 成果面 |
| 3268 | `results/_kv3s_4_4_rejudge_2026_10_09.md` | 42,687 | 2026-10-09 23:10:27 | `bc397d5099dd` | 成果面 |
| 3269 | `results/_l266_face_label_note_2026_10_16.md` | 15,074 | 2026-10-16 21:42:58 | `ca2e941d89ff` | 成果面 |
| 3270 | `results/_leftover_minor_adoptions_register_2026_10_12.md` | 13,565 | 2026-10-12 17:31:31 | `e18e620e22c5` | 成果面 |
| 3271 | `results/_log_purge_register_2026_10_13.md` | 8,855 | 2026-10-13 11:56:19 | `d0d5ba7a7cde` | 成果面 |
| 3272 | `results/_log_purge_v2_execution_register_2026_10_13.md` | 6,671 | 2026-10-13 13:20:59 | `13f959934b3a` | 成果面 |
| 3273 | `results/_log_retention_policy_register_2026_10_13.md` | 7,055 | 2026-10-13 13:34:21 | `a44f903ea331` | 成果面 |
| 3274 | `results/_log_retention_purge_2026_10_13.py` | 9,401 | 2026-10-13 13:50:47 | `8527db8d0ef7` | 成果面 |
| 3275 | `results/_m08_boundary_caliber_c1_c8_effect_2026_10_16.md` | 16,630 | 2026-10-16 19:32:50 | `608572ded536` | 成果面 |
| 3276 | `results/_m08_measured_enumeration_exec_2026_10_16.md` | 45,462 | 2026-10-16 16:28:16 | `4513f841234e` | 成果面 |
| 3277 | `results/_m2_c_tier_corrigendum_2026_10_14.md` | 17,212 | 2026-10-14 10:56:32 | `f621f836aa86` | 成果面 |
| 3278 | `results/_m2_kd_disposition_2026_10_14.md` | 21,750 | 2026-10-14 10:24:37 | `810e20778e6c` | 成果面 |
| 3279 | `results/_m2_terminal_verdict_effect_register_2026_10_14.md` | 31,647 | 2026-10-14 13:00:11 | `17fd10488da0` | 成果面 |
| 3280 | `results/_m3_disposition_v_eps_star_register_2026_10_16.md` | 23,452 | 2026-10-16 21:38:38 | `fd452e0cb8c0` | 成果面 |
| 3281 | `results/_m41_double_readout_contrast_exec_2026_10_14.md` | 17,009 | 2026-10-15 09:39:38 | `04f2920e259a` | 成果面 |
| 3282 | `results/_m41_double_readout_contrast_exec_2026_10_15.md` | 23,855 | 2026-10-15 10:27:45 | `b9feb5df8d44` | 成果面 |
| 3283 | `results/_m41_verdict_kd_effect_register_2026_10_15.md` | 23,630 | 2026-10-15 11:11:34 | `f54e8a10acde` | 成果面 |
| 3284 | `results/_m44_status_enum_backfill_design_2026_10_16.md` | 51,650 | 2026-10-16 16:55:23 | `e17dde9e2547` | 成果面 |
| 3285 | `results/_m5_k5_network_verification_register_2026_10_13.md` | 23,309 | 2026-10-13 23:42:07 | `7a4b2695c1d5` | 成果面 |
| 3286 | `results/_m5_reattribution_recommendation_2026_10_14.md` | 22,700 | 2026-10-14 10:18:35 | `0c9641e512e4` | 成果面 |
| 3287 | `results/_main_count_caliber_lock_2026_10_16.md` | 14,055 | 2026-10-16 19:48:07 | `6f1a253db9bd` | 成果面 |
| 3288 | `results/_material_expansion_build_exec_2026_10_16.md` | 35,966 | 2026-10-16 15:47:16 | `6ca1c64c2c44` | 成果面 |
| 3289 | `results/_material_expansion_drift_authorized_register_2026_10_16.md` | 15,044 | 2026-10-16 15:47:16 | `edf98dc7da62` | 成果面 |
| 3290 | `results/_material_expansion_sourcing_2026_10_16.md` | 31,814 | 2026-10-16 14:50:08 | `afd1c0517a43` | 成果面 |
| 3291 | `results/_material_expansion_verdict_kd_effect_register_2026_10_16.md` | 35,655 | 2026-10-16 16:02:24 | `42a0b3aeff96` | 成果面 |
| 3292 | `results/_material_root45_remeasure_2026_10_17.md` | 19,477 | 2026-10-17 20:15:44 | `f2a5c4330112` | 成果面 |
| 3293 | `results/_md_trigger_prereg_effectivity_2026_10_11.md` | 41,636 | 2026-10-11 14:03:16 | `5d8cd0d1676f` | 成果面 |
| 3294 | `results/_memory_errata_register_2026_10_14.md` | 10,701 | 2026-10-14 23:39:14 | `dbe9d0b16d14` | 成果面 |
| 3295 | `results/_merge_govern_approval_and_eps1_release_effect_2026_10_17.md` | 55,555 | 2026-10-17 23:36:49 | `58727d1eec71` | 成果面 |
| 3296 | `results/_mq19_item6_caption_restatement_2026_10_15.md` | 10,795 | 2026-10-15 10:20:26 | `656b2324d598` | 成果面 |
| 3297 | `results/_mq19_item6_f12_archive_recompute_2026_10_14.md` | 65,549 | 2026-10-14 21:19:18 | `0dfd3c886020` | 成果面 |
| 3298 | `results/_mq20_errata_register_2026_10_14.md` | 11,441 | 2026-10-14 21:36:02 | `8bb4bbc28c16` | 成果面 |
| 3299 | `results/_mq_rollout_v1_effect_register_2026_10_14.md` | 14,924 | 2026-10-14 21:06:17 | `3bd1942ec154` | 成果面 |
| 3300 | `results/_mq_rollout_v2_effect_register_2026_10_14.md` | 15,336 | 2026-10-14 21:20:47 | `652da23484e2` | 成果面 |
| 3301 | `results/_mq_rollout_v3_effect_register_2026_10_14.md` | 9,649 | 2026-10-14 21:36:02 | `66536311243d` | 成果面 |
| 3302 | `results/_mq_rollout_v4_effect_register_2026_10_14.md` | 24,423 | 2026-10-14 21:48:16 | `5f33f74e947d` | 成果面 |
| 3303 | `results/_mq_rollout_v5_effect_register_2026_10_14.md` | 15,119 | 2026-10-14 21:58:06 | `591e432c1635` | 成果面 |
| 3304 | `results/_mq_rollout_v6_effect_register_2026_10_14.md` | 15,467 | 2026-10-14 22:10:08 | `d79637fee0ef` | 成果面 |
| 3305 | `results/_mq_rollout_v9_effect_register_2026_10_14.md` | 29,389 | 2026-10-14 23:25:26 | `aa4e8d0554e2` | 成果面 |
| 3306 | `results/_n2_clause_transcription_supplement_2026_10_12.md` | 16,192 | 2026-10-12 23:09:19 | `ad8f0d542290` | 成果面 |
| 3307 | `results/_n2_equivalence_verification_register_2026_10_12.md` | 29,081 | 2026-10-12 23:30:17 | `1987d48234a3` | 成果面 |
| 3308 | `results/_n3_o5_terminal_effect_register_2026_10_16.md` | 35,944 | 2026-10-16 20:25:45 | `7414869866ad` | 成果面 |
| 3309 | `results/_n3_o5_terminal_verdict_2026_10_16.md` | 39,037 | 2026-10-16 20:05:26 | `88df2c228eae` | 成果面 |
| 3310 | `results/_n7_af_relocation_register_2026_10_17.md` | 35,057 | 2026-10-17 22:13:21 | `7a2133c810b1` | 成果面 |
| 3311 | `results/_n_distinct_grain_verdict_2026_10_17.md` | 41,028 | 2026-10-17 22:16:42 | `0abaee4aeefb` | 成果面 |
| 3312 | `results/_n_distinct_proof_2026_10_17.md` | 24,241 | 2026-10-17 21:53:53 | `2b538eba112a` | 成果面 |
| 3313 | `results/_naming_ruling_note_2026_09_29.md` | 7,843 | 2026-09-29 21:18:08 | `57024f2cd30a` | 成果面 |
| 3314 | `results/_night_mode_adoption_and_registry_2026_10_14.md` | 52,722 | 2026-10-14 01:20:11 | `d632879256c7` | 成果面 |
| 3315 | `results/_night_mode_adoption_corrigendum_2026_10_14.md` | 22,026 | 2026-10-14 01:32:27 | `28c61a3d98b0` | 成果面 |
| 3316 | `results/_night_mode_adoption_relabel_register_2026_10_14.md` | 8,672 | 2026-10-14 22:10:08 | `2660d5ea717d` | 成果面 |
| 3317 | `results/_night_outputs_adoption_register_2026_10_16.md` | 8,476 | 2026-10-16 19:22:10 | `837685c9ef64` | 成果面 |
| 3318 | `results/_night_shift_handover_2026_10_14.md` | 48,375 | 2026-10-14 01:48:48 | `c3d766464634` | 成果面 |
| 3319 | `results/_night_shift_handover_2026_10_14_r2.md` | 63,091 | 2026-10-14 02:50:08 | `1dbe20a3ba1c` | 成果面 |
| 3320 | `results/_no_backup_ruling_and_report_caliber_effect_2026_10_17.md` | 53,634 | 2026-10-17 11:23:23 | `bd748afec4f8` | 成果面 |
| 3321 | `results/_noncore_upload_caliber_draft_2026_10_17.md` | 29,489 | 2026-10-17 10:34:39 | `3ac146a3f8e5` | 成果面 |
| 3322 | `results/_noncore_upload_caliber_effect_register_2026_10_17.md` | 50,419 | 2026-10-17 10:54:30 | `f007da0a98d6` | 成果面 |
| 3323 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 55,605 | 2026-10-10 02:54:17 | `f4e145b090b1` | 成果面 |
| 3324 | `results/_null_u_aggregation_caliber_draft_2026_10_16.md` | 21,751 | 2026-10-16 19:57:20 | `e9afc12ec10d` | 成果面 |
| 3325 | `results/_null_u_aggregation_effect_register_2026_10_16.md` | 17,142 | 2026-10-16 20:17:24 | `7af0b66a68a1` | 成果面 |
| 3326 | `results/_numbering_659_overlap_semantic_review_2026_10_14.md` | 209,219 | 2026-10-14 02:40:32 | `c98d310e183e` | 成果面 |
| 3327 | `results/_numbering_claims_and_prefix_table_effect_2026_10_13.md` | 39,933 | 2026-10-13 17:42:16 | `34c1031746fa` | 成果面 |
| 3328 | `results/_numbering_face_recheck_2026_10_13.md` | 18,487 | 2026-10-13 21:38:53 | `7953a89ea015` | 成果面 |
| 3329 | `results/_numbering_face_signature_supplement_2026_10_13.md` | 12,578 | 2026-10-13 23:21:43 | `fd88b3669676` | 成果面 |
| 3330 | `results/_numbering_family_count_effect_register_2026_10_14.md` | 22,786 | 2026-10-14 14:09:44 | `80a97ee882d5` | 成果面 |
| 3331 | `results/_numbering_family_count_erratum_2026_10_13.md` | 15,557 | 2026-10-13 23:36:15 | `26b708beb153` | 成果面 |
| 3332 | `results/_numbering_hash_bucket_criterion_design_2026_10_14.md` | 21,733 | 2026-10-14 02:19:39 | `be92eddb4034` | 成果面 |
| 3333 | `results/_numbering_raw_residual_461_root_cause_2026_10_14.md` | 17,806 | 2026-10-14 02:48:36 | `23e0b4f997a4` | 成果面 |
| 3334 | `results/_numbering_system_audit_and_definition_2026_10_13.md` | 44,897 | 2026-10-13 17:14:34 | `47f20fa27a62` | 成果面 |
| 3335 | `results/_o1_498_lock_scope_deliberation_2026_10_16.md` | 52,216 | 2026-10-16 14:43:51 | `c9c808083d46` | 成果面 |
| 3336 | `results/_o1_reading_c_effect_register_2026_10_16.md` | 30,762 | 2026-10-16 15:09:54 | `30e0dee146ce` | 成果面 |
| 3337 | `results/_one_finish_gap_audit_2026_10_17.md` | 45,582 | 2026-10-17 00:23:04 | `1c713252e870` | 成果面 |
| 3338 | `results/_p0_scan_2026_10_12.json` | 20,879 | 2026-10-12 10:44:48 | `224b7fc0dcdf` | 成果面 |
| 3339 | `results/_p4_fallback_target_search_register_2026_10_12.md` | 14,561 | 2026-10-13 00:06:00 | `dba255b2b734` | 成果面 |
| 3340 | `results/_p4_inplace_resolution_register_2026_10_13.md` | 13,194 | 2026-10-13 00:17:28 | `d2aeaeedf39c` | 成果面 |
| 3341 | `results/_p_i_real_labels_2026_09_16/p_i_real_labels_results_2026_09_16.json` | 1,043 | 2026-09-16 22:11:35 | `e934819ee9ed` | 成果面 |
| 3342 | `results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json` | 1,669 | 2026-09-16 17:39:59 | `a9ad1de618f5` | 成果面 |
| 3343 | `results/_p_l_p_c_finite_size_scaling_2026_09_16/p_l_p_c_finite_size_scaling_results_2026_09_16.json` | 9,076 | 2026-09-16 15:50:08 | `664e7cc05aec` | 成果面 |
| 3344 | `results/_p_l_real_data_collapse_2026_09_16/p_l_real_data_collapse_results_v2_2026_09_16.json` | 3,761 | 2026-09-16 22:40:54 | `afe975606d40` | 成果面 |
| 3345 | `results/_p_m_attack_surface_cost_2026_09_16/p_m_attack_surface_cost_results_2026_09_16.json` | 5,266 | 2026-09-16 17:34:14 | `fbcb60cf5102` | 成果面 |
| 3346 | `results/_p_m_real_separation_2026_09_16/p_m_real_separation_results_2026_09_16.json` | 2,042 | 2026-09-16 22:12:02 | `a4b12d1cfedc` | 成果面 |
| 3347 | `results/_p_n_curvature_potential_coupling_2026_09_16/p_n_curvature_potential_coupling_results_2026_09_16.json` | 4,276 | 2026-09-16 17:43:33 | `088f28524a1d` | 成果面 |
| 3348 | `results/_p_o_stranger_verification_2026_09_16/p_o_stranger_verification_results_2026_09_16.json` | 5,916 | 2026-09-16 13:23:52 | `1e4c065da058` | 成果面 |
| 3349 | `results/_pa_harness_anchor_v3_effect_register_2026_10_16.md` | 12,794 | 2026-10-16 20:49:38 | `22c336d5049b` | 成果面 |
| 3350 | `results/_pa_harness_anchor_value_update_v2.json` | 16,043 | 2026-10-16 11:42:27 | `c43a84c70935` | 成果面 |
| 3351 | `results/_pa_harness_anchor_value_update_v3.json` | 23,745 | 2026-10-16 20:20:17 | `0c205e8efa43` | 成果面 |
| 3352 | `results/_pa_harness_anchor_value_update_v3_lock_register_2026_10_16.md` | 19,555 | 2026-10-16 20:22:27 | `ccb5a8e0301e` | 成果面 |
| 3353 | `results/_pack_card_four_rulings_effect_2026_10_17.md` | 46,371 | 2026-10-17 15:23:47 | `7fa815bf567d` | 成果面 |
| 3354 | `results/_pack_fingerprint_baseline_register_2026_10_14.md` | 15,051 | 2026-10-14 15:57:19 | `b8468b52cd64` | 成果面 |
| 3355 | `results/_pack_payload8_k1r4r3_disposition_register_2026_10_14.md` | 17,602 | 2026-10-14 15:55:49 | `092485278299` | 成果面 |
| 3356 | `results/_pb_anchor_reanchor_register_2026_10_14.md` | 11,438 | 2026-10-14 21:21:23 | `91b9326c5a2e` | 成果面 |
| 3357 | `results/_pending_pack_four_rulings_effect_2026_10_17.md` | 27,925 | 2026-10-17 23:12:28 | `9572516d82e7` | 成果面 |
| 3358 | `results/_pi_batch_rulings_and_gate1_definition_register_2026_10_12.md` | 11,798 | 2026-10-12 16:07:48 | `37876a02ad17` | 成果面 |
| 3359 | `results/_pi_four_rulings_adoption_and_effectivity_2026_10_12.md` | 14,146 | 2026-10-12 10:15:30 | `b99a9f039ecc` | 成果面 |
| 3360 | `results/_pi_give_b_class_retrieval_2026_10_14.md` | 31,463 | 2026-10-14 01:57:09 | `74e25d75d59d` | 成果面 |
| 3361 | `results/_pi_give_backlog_review_2026_10_14.md` | 34,309 | 2026-10-14 01:45:10 | `67ef129f9062` | 成果面 |
| 3362 | `results/_plan_v3_pending_verify_2026_09_30.md` | 42,280 | 2026-09-30 19:06:18 | `7374004d6075` | 成果面 |
| 3363 | `results/_poststrip_recalc_2026_10_17.md` | 42,707 | 2026-10-17 22:56:19 | `cfcf430f306c` | 成果面 |
| 3364 | `results/_pre_execution_report_kimi_2026_10_12.md` | 7,612 | 2026-10-12 10:44:48 | `799fbfc334a7` | 成果面 |
| 3365 | `results/_predelete_backup_caliber_draft_2026_10_17.md` | 32,084 | 2026-10-17 11:08:02 | `653505b88a08` | 成果面 |
| 3366 | `results/_prereg_caliber4_epsilon_revision_2026_10_15.md` | 9,659 | 2026-10-15 14:49:09 | `e49c11b43c65` | 成果面 |
| 3367 | `results/_prereg_lock_v1_epsilon_lu_klm41_register_2026_10_15.md` | 18,582 | 2026-10-15 14:49:09 | `a3dd3cc1caf2` | 成果面 |
| 3368 | `results/_prereg_lock_v2_h_epsilon_gamma_taucert_u_register_2026_10_15.md` | 33,312 | 2026-10-15 16:17:57 | `4c782fc8566b` | 成果面 |
| 3369 | `results/_prereg_lock_v2a_t5_completion_register_2026_10_15.md` | 46,621 | 2026-10-15 16:53:46 | `404d4fbeef40` | 成果面 |
| 3370 | `results/_q3_c1c4_l282_transposition_fix_applied_note_2026_10_09.md` | 16,105 | 2026-10-09 23:56:42 | `9572dfc3cd59` | 成果面 |
| 3371 | `results/_q3_transposition_errata_2026_10_09.md` | 11,757 | 2026-10-09 23:26:45 | `659c4101f10b` | 成果面 |
| 3372 | `results/_questionnaire_cards_intake_register_2026_10_09.md` | 442,288 | 2026-10-09 18:10:16 | `d917180db36f` | 成果面 |
| 3373 | `results/_questionnaire_cards_intake_register_supplement_2026_10_09.md` | 72,199 | 2026-10-09 21:28:13 | `193386b9f23c` | 成果面 |
| 3374 | `results/_questionnaire_cards_intake_register_supplement_2_2026_10_10.md` | 262,542 | 2026-10-10 00:23:35 | `dc43e3cb7610` | 成果面 |
| 3375 | `results/_questionnaire_cards_intake_register_supplement_3_2026_10_10.md` | 67,225 | 2026-10-10 01:12:02 | `11681f0ad861` | 成果面 |
| 3376 | `results/_questionnaire_cards_intake_register_supplement_4_2026_10_10.md` | 116,506 | 2026-10-10 10:54:25 | `d6ff041a9df9` | 成果面 |
| 3377 | `results/_questionnaire_cards_intake_register_supplement_5_2026_10_10.md` | 77,189 | 2026-10-10 13:59:18 | `edb57308170d` | 成果面 |
| 3378 | `results/_questionnaire_cards_intake_register_supplement_6_2026_10_10.md` | 106,453 | 2026-10-10 15:09:57 | `95ba771fa760` | 成果面 |
| 3379 | `results/_questionnaire_cards_intake_register_supplement_6_receipt_2026_10_10.md` | 11,752 | 2026-10-10 15:11:57 | `0984955b0370` | 成果面 |
| 3380 | `results/_questionnaire_cards_intake_register_supplement_6_receipt_v2_2026_10_10.md` | 11,756 | 2026-10-12 22:25:44 | `023834aaa293` | 成果面 |
| 3381 | `results/_r2_build_manifest_2026_10_12.json` | 216,510 | 2026-10-12 12:38:31 | `303db70b37f6` | 成果面 |
| 3382 | `results/_r2_execution_receipt_kimi_2026_10_12.md` | 5,342 | 2026-10-12 12:38:31 | `4efccb8df379` | 成果面 |
| 3383 | `results/_r2_reading_verdict_2026_10_17.md` | 43,055 | 2026-10-17 17:04:42 | `99b9bff47682` | 成果面 |
| 3384 | `results/_r2b_adoption_and_bytewise_caliber_effect_2026_10_17.md` | 31,009 | 2026-10-17 17:43:26 | `c8f3a36c152b` | 成果面 |
| 3385 | `results/_r3_m2_disposition_register_2026_10_14.md` | 17,025 | 2026-10-14 11:37:35 | `e11bc0e63ccc` | 成果面 |
| 3386 | `results/_r5_spec_pack_retrieval_register_2026_10_13.md` | 24,845 | 2026-10-14 00:31:31 | `d7ef2c8e56bb` | 成果面 |
| 3387 | `results/_r5_spec_pack_retrieved_2026_10_13/鲍勃_minimax实验委托规格包_2026_10_12.md` | 14,758 | 2026-10-14 00:29:49 | `bb66c577673b` | 成果面 |
| 3388 | `results/_r6_github_face_verification_2026_10_14.md` | 18,215 | 2026-10-14 11:38:01 | `fd70af96eff9` | 成果面 |
| 3389 | `results/_r6_supplement_first_version_disposition_2026_10_14.md` | 19,984 | 2026-10-14 13:13:12 | `b2e0a65f722c` | 成果面 |
| 3390 | `results/_r9_ge01_prereg_effect_register_2026_10_13.md` | 16,466 | 2026-10-13 22:33:25 | `18529950fe6f` | 成果面 |
| 3391 | `results/_r_pair4_design_and_texts_2026_10_09.md` | 35,189 | 2026-10-09 14:22:32 | `f793c5d9128f` | 成果面 |
| 3392 | `results/_r_pair_addendum_2026_10_09.json` | 110,510 | 2026-10-09 16:45:34 | `cebc2f6ef5ec` | 成果面 |
| 3393 | `results/_r_pair_intake_recompute_register_2026_10_09.md` | 36,774 | 2026-10-09 16:48:36 | `2dc64593b889` | 成果面 |
| 3394 | `results/_r_pair_is_corr_coverage_design_2026_10_09.md` | 27,208 | 2026-10-09 12:31:28 | `48f04fa39397` | 成果面 |
| 3395 | `results/_r_pair_question_texts_2026_10_09.md` | 30,352 | 2026-10-09 12:37:13 | `0ad849022328` | 成果面 |
| 3396 | `results/_reading_e_33_baseline_declaration_deliberation_2026_10_15.md` | 29,882 | 2026-10-15 16:54:21 | `74622229f730` | 成果面 |
| 3397 | `results/_reading_e_33_historical_nominal_value_corrigendum_2026_10_15.md` | 26,976 | 2026-10-15 17:15:55 | `20ad5b45ba2c` | 成果面 |
| 3398 | `results/_recycle_purge_resolution_and_434_adoption_2026_10_17.md` | 44,360 | 2026-10-17 11:11:23 | `ba3944565c13` | 成果面 |
| 3399 | `results/_ref_only_no_utility_criteria_effect_2026_10_17.md` | 26,214 | 2026-10-17 14:22:21 | `7fc20904d015` | 成果面 |
| 3400 | `results/_refonly_161_reading_verdict_2026_10_17.md` | 39,243 | 2026-10-17 16:13:11 | `bd94d12323e0` | 成果面 |
| 3401 | `results/_refonly_161_verify_register_2026_10_17.md` | 69,821 | 2026-10-17 15:47:49 | `74d63d55ee97` | 成果面 |
| 3402 | `results/_refonly_161_verify_register_r2_2026_10_17.md` | 94,675 | 2026-10-17 16:42:23 | `b687e16cc7d9` | 成果面 |
| 3403 | `results/_register_correction_batch_and_u14_effect_2026_10_17.md` | 55,316 | 2026-10-17 18:55:21 | `9a94037f80d1` | 成果面 |
| 3404 | `results/_remote_baseline_advance_register_2026_10_12.md` | 6,625 | 2026-10-12 20:33:30 | `ebf55ddb1eb2` | 成果面 |
| 3405 | `results/_remote_pullback_register_2026_10_17.md` | 66,020 | 2026-10-17 15:57:44 | `eaad85e5d605` | 成果面 |
| 3406 | `results/_reply_correctness_audit_2026_10_17.md` | 35,493 | 2026-10-17 16:28:31 | `be357dd6248f` | 成果面 |
| 3407 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 591,833 | 2026-10-12 02:11:15 | `96720fcfd76a` | 成果面 |
| 3408 | `results/_repo_noise_cleanup_register_2026_10_13.md` | 76,649 | 2026-10-13 12:40:13 | `f63672dc0250` | 成果面 |
| 3409 | `results/_repo_post_cleanup_snapshot_2026_10_12.md` | 309,419 | 2026-10-12 03:09:29 | `6039a6e08017` | 成果面 |
| 3410 | `results/_resolution_path_rulings_effect_2026_10_17.md` | 29,195 | 2026-10-17 20:22:36 | `91555b6b7bd6` | 成果面 |
| 3411 | `results/_resume32_adoption_and_flip_register_2026_10_16.md` | 38,971 | 2026-10-17 00:20:14 | `9d220cae64b9` | 成果面 |
| 3412 | `results/_ritt_def_adoption_and_remeasure_effect_2026_10_17.md` | 28,232 | 2026-10-17 19:58:52 | `a7539659c5df` | 成果面 |
| 3413 | `results/_ritt_def_proof_2026_10_17.md` | 23,310 | 2026-10-17 19:47:26 | `5d411ebf07ed` | 成果面 |
| 3414 | `results/_ritt_remeasure_readings_2026_10_17.md` | 23,064 | 2026-10-17 20:10:30 | `16dccc9c0a88` | 成果面 |
| 3415 | `results/_root_session_history_memo_2026_10_14.md` | 66,561 | 2026-10-14 13:01:39 | `2833f89d623b` | 成果面 |
| 3416 | `results/_root_session_history_memo_main_2026_10_14.md` | 132,833 | 2026-10-17 23:33:48 | `21f5284adcdc` | 成果面 |
| 3417 | `results/_rpp_perseed_recalc_2026_10_17.md` | 30,617 | 2026-10-17 22:19:42 | `7e693b27c1f7` | 成果面 |
| 3418 | `results/_s2_attainment_corrigendum_2026_10_16.md` | 25,790 | 2026-10-16 20:30:34 | `9beb6a44c71c` | 成果面 |
| 3419 | `results/_s3_closeout_convergence_2026_10_01.md` | 42,443 | 2026-10-01 12:16:50 | `bb62b5c174da` | 成果面 |
| 3420 | `results/_s3_d1fill_recount_2026_10_01.md` | 22,877 | 2026-10-01 13:44:10 | `a7dff824ed56` | 成果面 |
| 3421 | `results/_s3_f1_loader_fix_recompute_2026_10_08.json` | 20,144 | 2026-10-08 16:58:00 | `3044a070106e` | 成果面 |
| 3422 | `results/_s3_flip_s5_resolution_effect_2026_10_17.md` | 37,073 | 2026-10-17 21:40:02 | `9bd2c6df2834` | 成果面 |
| 3423 | `results/_s3_kv3s_3_full_recompute_2026_10_01.md` | 22,183 | 2026-10-01 08:57:14 | `b0123f161c10` | 成果面 |
| 3424 | `results/_s3_s5_explanation_and_disposition_verdict_2026_10_17.md` | 28,816 | 2026-10-17 17:45:24 | `2c1479af62cb` | 成果面 |
| 3425 | `results/_s3_s5_kd_effect_2026_10_17.md` | 33,609 | 2026-10-17 17:57:09 | `eea5245b31da` | 成果面 |
| 3426 | `results/_s3_s5_kd_effect_2026_10_17_append1.md` | 17,624 | 2026-10-17 18:00:22 | `905be2174c52` | 成果面 |
| 3427 | `results/_s3_th_v21_reconciliation_verdict_2026_10_01.md` | 51,073 | 2026-10-10 11:37:23 | `84fa6996b656` | 成果面 |
| 3428 | `results/_s3prime_alert_disposition_judgment_2026_10_11.md` | 53,188 | 2026-10-11 00:29:00 | `e7fcbc290a7e` | 成果面 |
| 3429 | `results/_s3prime_degeneracy_selfcert_2026_10_11.md` | 39,939 | 2026-10-11 00:15:56 | `e4d96a516289` | 成果面 |
| 3430 | `results/_s4_daily_share_margin_prerequisite_2026_10_09.md` | 18,197 | 2026-10-09 09:59:56 | `a929502e8421` | 成果面 |
| 3431 | `results/_s4_execution_sequence_review_2026_10_10.md` | 19,158 | 2026-10-10 13:04:40 | `0e1eb2fdd25e` | 成果面 |
| 3432 | `results/_s4_face_five_lines_ci_readings_execution_2026_10_09.md` | 29,750 | 2026-10-09 22:50:18 | `73550514152d` | 成果面 |
| 3433 | `results/_s4_face_five_lines_exec_sec8_erratum_2026_10_12.md` | 16,696 | 2026-10-12 16:03:15 | `9e17535df62e` | 成果面 |
| 3434 | `results/_s4_face_sync_2026_10_09.md` | 38,955 | 2026-10-09 15:33:16 | `6f8ba105b892` | 成果面 |
| 3435 | `results/_s4_face_v2_sync_2026_10_09.md` | 46,890 | 2026-10-09 15:45:37 | `9d3cc20fd980` | 成果面 |
| 3436 | `results/_s4_final_ruling_effectivity_register_2026_10_09.md` | 32,975 | 2026-10-09 15:00:52 | `21f2926efc5d` | 成果面 |
| 3437 | `results/_s4_heldout_sampling_caliber_ruling_2026_10_09.md` | 35,453 | 2026-10-09 21:26:53 | `fb1b696de1d6` | 成果面 |
| 3438 | `results/_s4_heldout_sampling_seed42_items_2026_10_09.json` | 20,033 | 2026-10-09 22:08:41 | `6a670e629dca` | 成果面 |
| 3439 | `results/_s4_heldout_sampling_seedprime_items_2026_10_10.json` | 15,409 | 2026-10-13 22:10:07 | `6cbb8ba01bfb` | 成果面 |
| 3440 | `results/_s4_heldout_sampling_seedprime_items_register_2026_10_10.md` | 24,690 | 2026-10-10 23:07:07 | `9da183328f18` | 成果面 |
| 3441 | `results/_s4_heldout_sampling_seedthird_items_2026_10_11.json` | 43,130 | 2026-10-13 22:10:08 | `5777a07c608a` | 成果面 |
| 3442 | `results/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | 22,646 | 2026-10-13 22:10:08 | `784f042bf93d` | 成果面 |
| 3443 | `results/_s4_kex_killline_freeze_2026_10_10.md` | 15,284 | 2026-10-10 13:03:55 | `6269d0c6fd10` | 成果面 |
| 3444 | `results/_s4_open_questions_addendum_2026_10_09.json` | 35,215 | 2026-10-09 14:29:17 | `4378dcc20624` | 成果面 |
| 3445 | `results/_s4_open_questions_design_2026_10_09.md` | 31,803 | 2026-10-09 13:33:22 | `0186a4499bbc` | 成果面 |
| 3446 | `results/_s4_open_questions_intake_recompute_register_2026_10_09.md` | 33,672 | 2026-10-09 14:30:52 | `2e66478e6db6` | 成果面 |
| 3447 | `results/_s4_reading_prep_order_2026_10_08.md` | 20,613 | 2026-10-08 16:46:34 | `7ac726cda752` | 成果面 |
| 3448 | `results/_s4_regen_execution_plan_2026_10_10.md` | 33,444 | 2026-10-10 12:00:40 | `70e22220350d` | 成果面 |
| 3449 | `results/_s4_regen_golive_clearance_2026_10_10.md` | 27,436 | 2026-10-10 13:33:31 | `80d8905b9762` | 成果面 |
| 3450 | `results/_s4_seedprime_inheldout_recompute_2026_10_10.md` | 21,866 | 2026-10-10 23:20:20 | `cf3368e7d5a0` | 成果面 |
| 3451 | `results/_s4_seedprime_seq_t1_only_supplement_2026_10_11.md` | 24,783 | 2026-10-11 00:50:28 | `b2b044289ffe` | 成果面 |
| 3452 | `results/_s4_seedprime_seq_t1_only_supplement_items_2026_10_11.json` | 28,030 | 2026-10-11 00:50:28 | `a834e0e7121a` | 成果面 |
| 3453 | `results/_s4_source_wave_mapping_registration_2026_10_10.md` | 38,231 | 2026-10-10 17:56:29 | `26c8278e3552` | 成果面 |
| 3454 | `results/_s4_substrate_freeze_register_2026_10_09.md` | 29,064 | 2026-10-09 14:17:49 | `f4a52862521b` | 成果面 |
| 3455 | `results/_s4_substrate_grid_availability_2026_10_08.json` | 11,446 | 2026-10-08 16:59:10 | `66be80ab4b81` | 成果面 |
| 3456 | `results/_s4_substrate_grid_availability_2026_10_08.md` | 14,995 | 2026-10-08 17:00:03 | `7deaee06c41a` | 成果面 |
| 3457 | `results/_s4_substrate_refreeze_register_179_2026_10_09.md` | 45,386 | 2026-10-09 21:03:55 | `24ea764daeac` | 成果面 |
| 3458 | `results/_s4_substrate_topup_addendum_2026_10_09.json` | 85,861 | 2026-10-09 13:53:09 | `1780542f0014` | 成果面 |
| 3459 | `results/_s4_substrate_topup_collection_register_2026_10_09.md` | 18,327 | 2026-10-09 10:20:29 | `33c1a818ef4f` | 成果面 |
| 3460 | `results/_s4_topup_intake_recompute_register_2026_10_09.md` | 32,779 | 2026-10-09 13:55:13 | `dfc9b0fbef5a` | 成果面 |
| 3461 | `results/_s4_topup_questionnaire_design_2026_10_09.md` | 38,466 | 2026-10-09 11:00:13 | `b8f8f987f21b` | 成果面 |
| 3462 | `results/_s4_tree_construct_adjusted_readings_2026_10_10.json` | 108,593 | 2026-10-10 09:51:47 | `a7aa4e9c8d47` | 成果面 |
| 3463 | `results/_s4_tree_construct_adjustment_assessment_2026_10_10.md` | 33,453 | 2026-10-10 01:25:59 | `016c7dacaa54` | 成果面 |
| 3464 | `results/_s4_v31_displacement_items_2026_10_10.json` | 36,822 | 2026-10-10 13:56:13 | `6f020c03e52c` | 成果面 |
| 3465 | `results/_s4_v31_drift_register_face1_2026_10_10.md` | 11,485 | 2026-10-10 13:56:41 | `5ab168d82873` | 成果面 |
| 3466 | `results/_s4_v31_keyword_table_final_2026_10_10.md` | 23,270 | 2026-10-10 13:03:25 | `1b7bcbcce589` | 成果面 |
| 3467 | `results/_s4_v31_readings_execution_2026_10_10.md` | 21,467 | 2026-10-10 13:55:46 | `80d765f34163` | 成果面 |
| 3468 | `results/_s4_v31_readings_summary_2026_10_10.json` | 5,569 | 2026-10-10 13:56:13 | `882a1b3deb0b` | 成果面 |
| 3469 | `results/_s4_v31_regen_gold_items_2026_10_10.json` | 36,830 | 2026-10-10 13:54:57 | `4125cb2df92b` | 成果面 |
| 3470 | `results/_s4_v31_regen_gold_register_2026_10_10.md` | 27,133 | 2026-10-10 13:54:32 | `9c9d8e8ecc72` | 成果面 |
| 3471 | `results/_s4_vclause_1_6_revision_2026_10_10.md` | 14,900 | 2026-10-10 13:05:11 | `017b3cf38ae3` | 成果面 |
| 3472 | `results/_s4prime_five_lines_readings_2026_10_11.json` | 15,219 | 2026-10-11 01:22:11 | `65a9b9be6327` | 成果面 |
| 3473 | `results/_s4prime_five_lines_runner_2026_10_11.py` | 29,813 | 2026-10-11 01:19:53 | `f784b2fc92f4` | 成果面 |
| 3474 | `results/_s5doubleprime_five_lines_readings_2026_10_11.json` | 16,099 | 2026-10-13 22:10:09 | `839fb5452578` | 成果面 |
| 3475 | `results/_seed_double_identifier_finalization_2026_10_11.md` | 26,864 | 2026-10-11 15:36:15 | `6904852f8ceb` | 成果面 |
| 3476 | `results/_seven23_map_revision_register_2026_10_12.md` | 7,050 | 2026-10-12 16:37:09 | `e981be2e3286` | 成果面 |
| 3477 | `results/_skill_reference_update_and_user_surface_survey_2026_09_30.md` | 60,621 | 2026-09-30 17:49:57 | `cb7b7ec9ebcd` | 成果面 |
| 3478 | `results/_spec_l22_landing_path_migration_note_2026_10_16.md` | 12,574 | 2026-10-16 20:15:36 | `b297e95ab164` | 成果面 |
| 3479 | `results/_spec_l32_scope_note_2026_10_16.md` | 13,114 | 2026-10-16 20:53:06 | `f171e4d384a9` | 成果面 |
| 3480 | `results/_stage1_gate_remedy_draft_2026_10_12.md` | 35,130 | 2026-10-12 10:18:29 | `764f3376f830` | 成果面 |
| 3481 | `results/_stage1_independent_gate_review_2026_10_12.md` | 29,479 | 2026-10-12 03:17:28 | `4d95ae28c469` | 成果面 |
| 3482 | `results/_stage3_1_bulk_reorg_completion_register_2026_10_12.md` | 15,818 | 2026-10-12 03:16:00 | `7439157b7be4` | 成果面 |
| 3483 | `results/_stage3_1_register_fingerprint_placeholder_erratum_2026_10_12.md` | 4,495 | 2026-10-12 03:17:23 | `a0e437ef317c` | 成果面 |
| 3484 | `results/_stage3_completion_and_stage4_open_register_2026_10_12.md` | 12,634 | 2026-10-12 09:55:13 | `e2f4ad9e1360` | 成果面 |
| 3485 | `results/_stage3_r2_cleanup_register_2026_10_18.md` | 62,885 | 2026-10-18 00:58:56 | `d6b1dc8f8a02` | 成果面 |
| 3486 | `results/_stage3_trigger_readings_items_2026_10_11.json` | 21,049 | 2026-10-13 22:10:08 | `079108c62a82` | 成果面 |
| 3487 | `results/_stage3_trigger_recheck_2026_10_11.md` | 49,109 | 2026-10-11 16:26:38 | `aef26b8cbe50` | 成果面 |
| 3488 | `results/_stage_sequence_ruling_effect_2026_10_17.md` | 18,115 | 2026-10-17 23:33:48 | `b582bde59d6d` | 成果面 |
| 3489 | `results/_stage_sequence_violation_register_2026_10_12.md` | 11,159 | 2026-10-12 02:37:59 | `8dcfc200c7fd` | 成果面 |
| 3490 | `results/_strict3_verdict_2026_10_17.md` | 41,236 | 2026-10-17 18:28:37 | `d392bd36ec34` | 成果面 |
| 3491 | `results/_strip_c3_non_adoption_register_2026_10_16.md` | 25,221 | 2026-10-16 13:57:41 | `726c32d83734` | 成果面 |
| 3492 | `results/_supplement_500_combo_drift_authorized_register_2026_10_16.md` | 13,742 | 2026-10-16 11:59:11 | `71d2ef525d3b` | 成果面 |
| 3493 | `results/_supplement_500_combo_effect_register_2026_10_16.md` | 30,213 | 2026-10-16 13:59:04 | `ddd311fb1311` | 成果面 |
| 3494 | `results/_supplement_500_combo_exec_2026_10_16.md` | 46,503 | 2026-10-16 12:00:22 | `ee7a1563d850` | 成果面 |
| 3495 | `results/_supplement_to_500_design_review_2026_10_16.md` | 46,159 | 2026-10-16 11:03:02 | `7a2d83148969` | 成果面 |
| 3496 | `results/_t1_exp2_activation_supplement_2026_10_09.md` | 24,708 | 2026-10-09 22:17:22 | `8db3f88b5ed0` | 成果面 |
| 3497 | `results/_t1_exp2_answer_face_baseline_2026_10_09.json` | 11,792 | 2026-10-09 22:22:00 | `35773f5f1edb` | 成果面 |
| 3498 | `results/_t1_exp2_executor_2026_10_09.py` | 67,955 | 2026-10-09 22:21:51 | `ce393b41618c` | 成果面 |
| 3499 | `results/_t1_exp2_result_2026_10_09.json` | 35,239 | 2026-10-10 02:33:06 | `d9ccd75c652b` | 成果面 |
| 3500 | `results/_t1_prereg_revision_qwen_temp_sweep_2026_10_09.md` | 16,994 | 2026-10-09 10:03:07 | `bda5d5f3dfa0` | 成果面 |
| 3501 | `results/_t1_prereg_revision_temp_axis_exp2_2026_10_09.md` | 34,217 | 2026-10-09 21:49:30 | `2ff15aeeb5d0` | 成果面 |
| 3502 | `results/_t1_qwen_temp_sweep_exec_register_2026_10_09.md` | 17,341 | 2026-10-09 11:20:07 | `7ad31e741400` | 成果面 |
| 3503 | `results/_t1_qwen_temp_sweep_executor_2026_10_09.py` | 32,399 | 2026-10-09 10:22:20 | `f0c845864603` | 成果面 |
| 3504 | `results/_t1_qwen_temp_sweep_r2_exec_register_2026_10_09.md` | 23,681 | 2026-10-09 18:10:33 | `cf4826a731d6` | 成果面 |
| 3505 | `results/_t1_qwen_temp_sweep_r2_executor_2026_10_09.py` | 53,184 | 2026-10-09 18:06:06 | `38d0cf7fc9ba` | 成果面 |
| 3506 | `results/_t1_qwen_temp_sweep_r2_result_2026_10_09.json` | 58,712 | 2026-10-09 18:06:16 | `8d6242da158c` | 成果面 |
| 3507 | `results/_t1_qwen_temp_sweep_r2_verdict_2026_10_09.md` | 42,817 | 2026-10-09 18:23:43 | `9c18b9893579` | 成果面 |
| 3508 | `results/_t1_qwen_temp_sweep_verdict_2026_10_09.md` | 21,672 | 2026-10-09 11:54:29 | `dfc858d3d930` | 成果面 |
| 3509 | `results/_t1_r2_activation_2026_10_09.md` | 21,111 | 2026-10-09 17:07:33 | `8e59b797aa2d` | 成果面 |
| 3510 | `results/_t1_substrate_gap_census_2026_10_01.md` | 32,371 | 2026-10-01 14:40:17 | `62fb594be3f9` | 成果面 |
| 3511 | `results/_t1_substrate_gap_precondition_2026_10_01.md` | 22,196 | 2026-10-14 14:07:09 | `a019602cfab2` | 成果面 |
| 3512 | `results/_t1_temp_axis_new_experiment_design_2026_10_09.md` | 41,392 | 2026-10-09 21:17:20 | `7aaa90ee6d50` | 成果面 |
| 3513 | `results/_t2_license_final_register_2026_10_16.md` | 18,510 | 2026-10-16 19:59:24 | `0ba73a1793e1` | 成果面 |
| 3514 | `results/_t2_path_b_build_exec_2026_10_16.md` | 35,389 | 2026-10-16 16:27:44 | `359ab9d180f2` | 成果面 |
| 3515 | `results/_t2_path_b_drift_authorized_register_2026_10_16.md` | 10,939 | 2026-10-16 16:27:02 | `d07d33f0eb82` | 成果面 |
| 3516 | `results/_t2_t3_value_request_form_2026_10_14.md` | 15,054 | 2026-10-14 21:36:47 | `21abb5173b87` | 成果面 |
| 3517 | `results/_t2_t3_value_sourcing_2026_10_15.md` | 24,658 | 2026-10-15 10:54:40 | `bcb0d60fdd2d` | 成果面 |
| 3518 | `results/_t3_repro_probe_2026_10_16.md` | 33,722 | 2026-10-16 23:08:35 | `1a104886964f` | 成果面 |
| 3519 | `results/_t3trap_answerable_build_exec_2026_10_15.md` | 31,808 | 2026-10-15 17:31:14 | `b9e9c9b5a06b` | 成果面 |
| 3520 | `results/_t3trap_answerable_drift_authorized_register_2026_10_15.md` | 15,196 | 2026-10-15 17:31:14 | `aa8e9fce651c` | 成果面 |
| 3521 | `results/_t3trap_kd3_bprime_effect_register_2026_10_15.md` | 27,675 | 2026-10-15 17:20:10 | `7a4a0ed3222c` | 成果面 |
| 3522 | `results/_t3trap_kd3_disposition_deliberation_2026_10_15.md` | 29,776 | 2026-10-15 16:53:03 | `b58775c33928` | 成果面 |
| 3523 | `results/_t4_license_final_register_2026_10_16.md` | 16,202 | 2026-10-16 20:17:24 | `d575f88b40ce` | 成果面 |
| 3524 | `results/_t5_anchor_drift_authorized_register_2026_10_15.md` | 11,553 | 2026-10-15 16:25:55 | `1308662a369a` | 成果面 |
| 3525 | `results/_t5_generator_build_exec_2026_10_15.md` | 26,857 | 2026-10-15 16:25:55 | `1fd4a9465809` | 成果面 |
| 3526 | `results/_t_s3_3_disposition_judgment_2026_10_10.md` | 31,855 | 2026-10-10 11:18:26 | `ee7a822a077b` | 成果面 |
| 3527 | `results/_temp_cleanup_register_2026_10_13.md` | 10,598 | 2026-10-13 12:12:20 | `89cbdf1eefab` | 成果面 |
| 3528 | `results/_th_id_attribution_verification_2026_10_09.md` | 8,409 | 2026-10-09 15:02:39 | `94740f8d3c8d` | 成果面 |
| 3529 | `results/_th_t1_n_min_revision_proposal_2026_10_09.md` | 34,884 | 2026-10-09 15:33:46 | `24da21074cc2` | 成果面 |
| 3530 | `results/_theory_u_hit_rate_retirement_register_2026_10_15.md` | 22,012 | 2026-10-15 15:40:00 | `1ba41ba3bbe9` | 成果面 |
| 3531 | `results/_three_exception_pullback_register_2026_10_13.md` | 12,295 | 2026-10-13 00:09:37 | `62fff3dc6cca` | 成果面 |
| 3532 | `results/_three_items_alternative_deliberation_judgment_2026_10_13.md` | 64,069 | 2026-10-13 22:04:41 | `40c154d64169` | 成果面 |
| 3533 | `results/_three_seed_measurement_exec_2026_10_16.md` | 48,178 | 2026-10-16 11:24:03 | `0e0716fde41f` | 成果面 |
| 3534 | `results/_three_seed_readout_validity_deliberation_2026_10_16.md` | 32,097 | 2026-10-16 23:34:41 | `75e5608106ec` | 成果面 |
| 3535 | `results/_three_seed_readout_validity_effect_register_2026_10_16.md` | 27,429 | 2026-10-16 23:51:41 | `1f988e61beb2` | 成果面 |
| 3536 | `results/_tmp_archive_disposition_register_2026_10_12.md` | 12,836 | 2026-10-12 21:11:19 | `3fdf474df1f9` | 成果面 |
| 3537 | `results/_tmp_archive_exec_artifacts_rewrite_map_2026_10_12.md` | 30,244 | 2026-10-12 21:35:19 | `ff0a25dc2720` | 成果面 |
| 3538 | `results/_tmp_census_c2.txt` | 3,602 | 2026-10-14 15:02:43 | `17faee799f6a` | 成果面 |
| 3539 | `results/_tmp_measure_c5b_register.py` | 2,807 | 2026-10-17 15:44:42 | `77248d427f32` | 成果面 |
| 3540 | `results/_tmp_write_copilot_register.py` | 18,397 | 2026-10-17 15:46:06 | `bc87bbf099ef` | 成果面 |
| 3541 | `results/_tra_v0_2026_09_10.py` | 12,125 | 2026-09-10 20:20:20 | `d80a8f75a122` | 成果面 |
| 3542 | `results/_trae_dfamily_reply_intake_register_2026_10_12.md` | 13,735 | 2026-10-12 17:47:05 | `3acfaecda5e0` | 成果面 |
| 3543 | `results/_trae_errata_sha_drift_attribution_2026_10_01.md` | 23,913 | 2026-10-01 12:31:37 | `6d5836cc6d3a` | 成果面 |
| 3544 | `results/_trae_issues_batch2_corrections_register_2026_10_12.md` | 36,422 | 2026-10-12 15:22:51 | `592800923f3f` | 成果面 |
| 3545 | `results/_trae_issues_batch3_six_items_draft_2026_10_12.md` | 29,957 | 2026-10-12 15:23:18 | `2153c41a8cff` | 成果面 |
| 3546 | `results/_trae_issues_dfamily_corrections_register_2026_10_12.md` | 33,471 | 2026-10-12 17:50:41 | `12da29eb102c` | 成果面 |
| 3547 | `results/_trae_issues_disposition_schedule_2026_10_12.md` | 12,849 | 2026-10-12 14:54:30 | `57b9dcca2630` | 成果面 |
| 3548 | `results/_trae_sixitem_disposal_and_collision_register_2026_10_01.md` | 19,268 | 2026-10-01 09:10:55 | `545b17d403be` | 成果面 |
| 3549 | `results/_two_items_alternative_deliberation_judgment_2026_10_13.md` | 44,778 | 2026-10-13 22:04:11 | `f2cdaad477f6` | 成果面 |
| 3550 | `results/_u01_u15_recheck_after_rulings_2026_10_17.md` | 39,219 | 2026-10-17 16:20:57 | `71c6b834dd9d` | 成果面 |
| 3551 | `results/_u04_1_exemption_precondition_verification_2026_10_09.json` | 21,862 | 2026-10-09 17:25:09 | `bddfeac3ee2f` | 成果面 |
| 3552 | `results/_u09_count_caliber_2026_10_17.md` | 24,415 | 2026-10-17 18:52:09 | `cd32d8a84ae6` | 成果面 |
| 3553 | `results/_u5_referent_registry_correction_2026_10_12.md` | 25,048 | 2026-10-12 17:09:36 | `111a76fa9667` | 成果面 |
| 3554 | `results/_u5_semantics_resolution_2026_10_12.md` | 24,046 | 2026-10-12 16:38:57 | `8b5f1a495a99` | 成果面 |
| 3555 | `results/_u_1494_carrier_effect_register_2026_10_16.md` | 42,588 | 2026-10-16 23:15:41 | `6f194df09b33` | 成果面 |
| 3556 | `results/_u_33_34_lock_and_33_declaration_coexistence_register_2026_10_16.md` | 28,868 | 2026-10-16 15:29:26 | `5c6120d7e69b` | 成果面 |
| 3557 | `results/_u_720face_lock_register_2026_10_17.md` | 41,007 | 2026-10-17 20:45:32 | `4ed6194729b5` | 成果面 |
| 3558 | `results/_u_axis_active_ruling_register_2026_10_16.md` | 22,219 | 2026-10-16 21:17:15 | `30fed54c3d09` | 成果面 |
| 3559 | `results/_u_axis_equation_direction_deliberation_2026_10_16.md` | 40,049 | 2026-10-16 21:50:00 | `5b6847e424b0` | 成果面 |
| 3560 | `results/_u_axis_equation_direction_effect_register_2026_10_16.md` | 18,935 | 2026-10-16 22:02:53 | `68c4a68b1ee8` | 成果面 |
| 3561 | `results/_u_axis_input_vs_kdb2_recheck_2026_10_17.md` | 25,669 | 2026-10-17 16:27:08 | `45e62039cee3` | 成果面 |
| 3562 | `results/_u_cluster1_verdict_2026_10_17.md` | 40,213 | 2026-10-17 18:37:07 | `0172e2a52c80` | 成果面 |
| 3563 | `results/_u_cluster2_verdict_2026_10_17.md` | 47,057 | 2026-10-17 18:38:15 | `4dd0d2f38d46` | 成果面 |
| 3564 | `results/_u_domain3_carrier_1494_2026_10_16.md` | 42,227 | 2026-10-16 22:43:24 | `59f52f8bb287` | 成果面 |
| 3565 | `results/_u_hface15_18889_lock_register_2026_10_17.md` | 24,452 | 2026-10-17 19:29:51 | `59f8c6c2826b` | 成果面 |
| 3566 | `results/_u_hface_lock_register_2026_10_16.md` | 15,551 | 2026-10-16 19:47:27 | `892f8f9ae0b5` | 成果面 |
| 3567 | `results/_u_lock_recalc_2026_10_17.md` | 24,411 | 2026-10-17 19:10:46 | `6793b0b56925` | 成果面 |
| 3568 | `results/_u_recalc_post_expansion_2026_10_16.md` | 28,570 | 2026-10-16 19:33:14 | `c5116ff749b1` | 成果面 |
| 3569 | `results/_unclosed_47_direct_clear_b_tier_register_2026_10_13.md` | 31,100 | 2026-10-13 22:32:25 | `0cf3faba8c21` | 成果面 |
| 3570 | `results/_unclosed_47_direct_clear_register_2026_10_13.md` | 35,560 | 2026-10-13 22:26:29 | `3d87efe5680d` | 成果面 |
| 3571 | `results/_unclosed_47_pi_give_draft_2026_10_13.md` | 61,341 | 2026-10-13 21:02:05 | `31d66920001c` | 成果面 |
| 3572 | `results/_unclosed_47_status_review_2026_10_14.md` | 46,386 | 2026-10-14 03:10:30 | `7cbfb9bc984e` | 成果面 |
| 3573 | `results/_upload_execution_receipt_kimi_2026_10_12.md` | 4,790 | 2026-10-12 11:24:32 | `639303213ce3` | 成果面 |
| 3574 | `results/_upload_ledger_2026_10_12.json` | 367,903 | 2026-10-12 11:24:32 | `44019e7dca1e` | 成果面 |
| 3575 | `results/_upload_plan_2026_10_12.json` | 311,429 | 2026-10-12 10:44:48 | `10b282bf7d16` | 成果面 |
| 3576 | `results/_upload_side_desensitized_remote_sha_letter_kimi_2026_10_12.md` | 74,043 | 2026-10-12 12:50:06 | `fcb0a673ee5c` | 成果面 |
| 3577 | `results/_v34_experiment_gap_plan_2026_10_08.md` | 36,066 | 2026-10-08 16:46:11 | `996feb1db9cb` | 成果面 |
| 3578 | `results/_v3_construct_degradation_diag_2026_09_23.json` | 11,609 | 2026-09-23 14:20:36 | `c8d539a58d29` | 成果面 |
| 3579 | `results/_v3_n_cpath_live_data_2026_09_27.json` | 12,711 | 2026-09-27 14:16:19 | `25374af92f88` | 成果面 |
| 3580 | `results/_v3_n_ktb1_distortion_bound_data_2026_09_27.json` | 6,411 | 2026-09-27 14:17:05 | `26c0d0b0ffb6` | 成果面 |
| 3581 | `results/_v3_n_pg_boss_live_data_2026_09_27.json` | 9,220 | 2026-09-27 14:15:46 | `be11c5274807` | 成果面 |
| 3582 | `results/_v3_n_recheck_llm_verdict_2026_09_27.md` | 21,332 | 2026-09-27 14:20:06 | `426cfe18cf65` | 成果面 |
| 3583 | `results/_v3_recheck_01_executor_2026_09_27.py` | 41,004 | 2026-09-27 15:43:40 | `919fa909381e` | 成果面 |
| 3584 | `results/_v3_recheck_01_rescript_2026_09_27.md` | 14,541 | 2026-09-30 16:15:20 | `a3c95102290f` | 成果面 |
| 3585 | `results/_v3_recheck_01_result_2026_09_27.json` | 167,831 | 2026-09-27 16:04:01 | `c19e2ab24e63` | 成果面 |
| 3586 | `results/_v3_recheck_04_executor_2026_09_27.py` | 49,405 | 2026-09-27 15:56:09 | `e098fa21700d` | 成果面 |
| 3587 | `results/_v3_recheck_04_rescript_2026_09_27.md` | 14,780 | 2026-09-30 16:15:20 | `34099595fe75` | 成果面 |
| 3588 | `results/_v3_recheck_04_result_2026_09_27.json` | 840,158 | 2026-09-27 16:04:05 | `db8cfb974ce3` | 成果面 |
| 3589 | `results/_v3_recheck_05_rescript_2026_09_28.md` | 22,178 | 2026-09-28 13:29:42 | `88b7eaf8675d` | 成果面 |
| 3590 | `results/_v3_recheck_05_result_2026_09_28.json` | 450,751 | 2026-10-13 22:10:06 | `81460acbb4f9` | 成果面 |
| 3591 | `results/_v3_recheck_08_executor_2026_09_27.py` | 15,598 | 2026-09-27 14:49:01 | `21c4ba4d479e` | 成果面 |
| 3592 | `results/_v3_recheck_08_rescript_2026_09_27.md` | 10,459 | 2026-09-27 14:50:51 | `2e08b9ae9f09` | 成果面 |
| 3593 | `results/_v3_recheck_08_result_2026_09_27.json` | 10,587 | 2026-09-27 14:51:08 | `0d2af01086db` | 成果面 |
| 3594 | `results/_v3_recheck_08b_executor/executor_2026_09_27.py` | 43,901 | 2026-09-27 15:17:27 | `b292410d9a69` | 成果面 |
| 3595 | `results/_v3_recheck_08b_executor/rescript_2026_09_27.md` | 18,501 | 2026-09-27 15:18:54 | `78f3aba1f24c` | 成果面 |
| 3596 | `results/_v3_recheck_08b_executor/result_2026_09_27.json` | 88,052 | 2026-09-27 15:17:36 | `f9a7fa2d65b1` | 成果面 |
| 3597 | `results/_v3_recheck_08c_preexp_data/_v3_recheck_08c_sha12fix_r1_2026_10_12.py` | 1,395 | 2026-10-12 01:30:19 | `4b7ed4d0a3e5` | 成果面 |
| 3598 | `results/_v3_recheck_08c_preexp_data/executor_2026_09_27.py` | 37,775 | 2026-09-27 17:52:40 | `cb6eb9164df3` | 成果面 |
| 3599 | `results/_v3_recheck_08c_preexp_data/rescript_2026_09_27.md` | 17,069 | 2026-10-12 01:30:19 | `035af77db626` | 成果面 |
| 3600 | `results/_v3_recheck_08c_preexp_data/result_2026_09_27.json` | 146,601 | 2026-09-27 17:52:51 | `689a6e4427a8` | 成果面 |
| 3601 | `results/_v3_recheck_10_rescript_2026_09_27.md` | 14,445 | 2026-09-27 15:23:59 | `fc0ffd27adca` | 成果面 |
| 3602 | `results/_v3_recheck_10_result_2026_09_27.json` | 82,535 | 2026-09-27 15:20:09 | `5d4b6baf1b18` | 成果面 |
| 3603 | `results/_v3_recheck_12_jsv_check_2026_09_27.md` | 15,821 | 2026-09-30 16:15:20 | `c5eab30e9fc6` | 成果面 |
| 3604 | `results/_v3_recheck_12_rescript_2026_09_27.md` | 21,222 | 2026-09-30 16:15:20 | `776c86c735f8` | 成果面 |
| 3605 | `results/_v3_recheck_12_result_2026_09_27.json` | 187,612 | 2026-09-27 16:04:05 | `cdb37ed0b32f` | 成果面 |
| 3606 | `results/_v3_recheck_12_rj5_provenance_2026_09_27.md` | 23,822 | 2026-09-27 17:30:07 | `20f15c49feb5` | 成果面 |
| 3607 | `results/_v3_recheck_19_rescript_2026_09_27.md` | 11,089 | 2026-09-27 14:56:14 | `82a947f2aebd` | 成果面 |
| 3608 | `results/_v3_recheck_19_result_2026_09_27.json` | 59,888 | 2026-09-27 14:56:25 | `df07cf80930f` | 成果面 |
| 3609 | `results/_v3_recheck_21_rescript_2026_09_27.md` | 14,618 | 2026-09-27 16:44:40 | `04f6ecd482b9` | 成果面 |
| 3610 | `results/_v3_recheck_21_result_2026_09_27.json` | 44,928 | 2026-09-27 16:54:07 | `354ae9c14fe2` | 成果面 |
| 3611 | `results/_v3_recheck_26_executor_2026_09_27.py` | 15,056 | 2026-09-27 14:45:28 | `46c326c756c3` | 成果面 |
| 3612 | `results/_v3_recheck_26_preexp_data_2026_09_27.json` | 94,658 | 2026-09-27 15:30:22 | `177c88e1bd82` | 成果面 |
| 3613 | `results/_v3_recheck_26_preexp_executor_2026_09_27.py` | 38,726 | 2026-09-27 15:29:13 | `775217a462f5` | 成果面 |
| 3614 | `results/_v3_recheck_26_preexp_report_2026_09_27.md` | 23,048 | 2026-09-30 16:15:20 | `a46230e344af` | 成果面 |
| 3615 | `results/_v3_recheck_26_rescript_2026_09_27.md` | 13,747 | 2026-09-27 20:10:38 | `6b86576146a3` | 成果面 |
| 3616 | `results/_v3_recheck_26_result_2026_09_27.json` | 11,994 | 2026-09-27 14:51:06 | `eb6a99dd46dd` | 成果面 |
| 3617 | `results/_v3_recheck_26b_executor_2026_09_27.py` | 43,171 | 2026-09-27 15:51:38 | `5c906113a210` | 成果面 |
| 3618 | `results/_v3_recheck_26b_executor_r2_2026_09_28.py` | 52,272 | 2026-09-28 22:47:39 | `0808af6212c5` | 成果面 |
| 3619 | `results/_v3_recheck_26b_executor_r3_2026_09_29.py` | 64,959 | 2026-09-29 10:50:41 | `6c83e7a7ca2e` | 成果面 |
| 3620 | `results/_v3_recheck_26b_r3_result_2026_09_29.json` | 54,294 | 2026-09-29 19:08:57 | `c9d3c9f819f1` | 成果面 |
| 3621 | `results/_v3_recheck_26b_rescript_2026_09_27.md` | 30,552 | 2026-09-30 16:15:20 | `ae81d9b59054` | 成果面 |
| 3622 | `results/_v3_recheck_26b_result_2026_09_27.json` | 44,379 | 2026-09-27 15:52:40 | `49c6e5a07732` | 成果面 |
| 3623 | `results/_v3_recheck_26b_verdict_prep_2026_10_01.md` | 36,133 | 2026-10-01 08:58:09 | `3aab3f7660fc` | 成果面 |
| 3624 | `results/_v3_recheck_27_rescript_2026_09_27.md` | 14,599 | 2026-09-27 15:22:57 | `6f045bdc70e7` | 成果面 |
| 3625 | `results/_v3_recheck_27_result_2026_09_27.json` | 42,571 | 2026-09-27 15:20:39 | `e06cb51fb3af` | 成果面 |
| 3626 | `results/_v3_recheck_28_rescript_2026_09_27.md` | 10,187 | 2026-09-27 14:50:20 | `a0734e0a6860` | 成果面 |
| 3627 | `results/_v3_recheck_28_result_2026_09_27.json` | 26,113 | 2026-09-27 14:53:26 | `c0a8cb9029a7` | 成果面 |
| 3628 | `results/_v3_recheck_35_rescript_2026_09_27.md` | 13,211 | 2026-09-27 16:24:33 | `138faf395f40` | 成果面 |
| 3629 | `results/_v3_recheck_35_result_2026_09_27.json` | 35,091 | 2026-09-29 12:07:14 | `a8a4befb21f5` | 成果面 |
| 3630 | `results/_v3_recheck_prereg_v1_2026_09_27.md` | 37,346 | 2026-09-27 13:33:20 | `88052d7db895` | 成果面 |
| 3631 | `results/_v3_recheck_prereg_v1p1_2026_09_27.md` | 42,970 | 2026-09-27 14:44:22 | `bcc3cee23e82` | 成果面 |
| 3632 | `results/_v3_recheck_prereg_v1p2_2026_09_27.md` | 38,932 | 2026-09-30 16:15:20 | `9da148037744` | 成果面 |
| 3633 | `results/_v3_recheck_prereg_v1p3_2026_09_27.md` | 35,200 | 2026-09-30 16:15:20 | `272ed65bf50e` | 成果面 |
| 3634 | `results/_v3_recheck_prereg_v1p4_2026_09_27.md` | 69,406 | 2026-09-28 15:27:29 | `5294e4a2bd14` | 成果面 |
| 3635 | `results/_v3_recheck_prereg_v1p5_2026_09_29.md` | 18,680 | 2026-09-29 19:22:00 | `7b1374578de4` | 成果面 |
| 3636 | `results/_v3_recheck_verdict_register_2026_09_27.md` | 112,085 | 2026-09-30 16:15:20 | `d9b6b974cfc1` | 成果面 |
| 3637 | `results/_v3_s1_executor/executor_2026_09_27.py` | 54,937 | 2026-09-27 15:44:50 | `10870941c283` | 成果面 |
| 3638 | `results/_v3_s1_executor/rescript_2026_09_27.md` | 17,253 | 2026-09-27 15:45:21 | `9d49a632ee81` | 成果面 |
| 3639 | `results/_v3_s1_executor/result_2026_09_27.json` | 24,975 | 2026-09-27 15:45:21 | `bfc99c3133dd` | 成果面 |
| 3640 | `results/_v3_s2_executor/executor_2026_09_27.py` | 84,993 | 2026-09-27 16:03:46 | `f1e272a0924a` | 成果面 |
| 3641 | `results/_v3_s2_executor/rescript_2026_09_27.md` | 25,151 | 2026-10-12 01:30:19 | `ff0f964be8aa` | 成果面 |
| 3642 | `results/_v3_s2_executor/result_2026_09_27.json` | 51,039 | 2026-09-27 16:05:12 | `d73d51e670de` | 成果面 |
| 3643 | `results/_v3_s3_collection_brief_2026_09_28.md` | 19,045 | 2026-09-28 13:38:11 | `d5ba1161e37f` | 成果面 |
| 3644 | `results/_v3_s3_wordexpand_data/executor_2026_09_28.py` | 46,005 | 2026-09-28 13:35:10 | `80f1445ce45d` | 成果面 |
| 3645 | `results/_v3_s3_wordexpand_data/executor_r1_2026_09_28.py` | 43,524 | 2026-09-28 13:59:47 | `39c29e0f092e` | 成果面 |
| 3646 | `results/_v3_s3_wordexpand_data/rescript_2026_09_28.md` | 18,225 | 2026-09-28 13:36:15 | `98d4f62cd52a` | 成果面 |
| 3647 | `results/_v3_s3_wordexpand_data/rescript_r1_2026_09_28.md` | 17,168 | 2026-09-28 14:04:26 | `c991ddb1deb4` | 成果面 |
| 3648 | `results/_v3_s3_wordexpand_data/result_2026_09_28.json` | 34,953 | 2026-09-28 13:38:18 | `f7f6d875d73a` | 成果面 |
| 3649 | `results/_v3_s3_wordexpand_recheck_r1_2026_09_28.json` | 33,867 | 2026-09-28 14:04:43 | `67ccea282d1c` | 成果面 |
| 3650 | `results/_v3_s_phrasetemplate_preexp_data/executor_2026_09_27.py` | 35,555 | 2026-09-27 17:47:47 | `96f491a8e2bf` | 成果面 |
| 3651 | `results/_v3_s_phrasetemplate_preexp_data/rescript_2026_09_27.md` | 17,574 | 2026-10-12 01:30:19 | `d42ea1fa61f1` | 成果面 |
| 3652 | `results/_v3_s_phrasetemplate_preexp_data/result_2026_09_27.json` | 36,844 | 2026-09-27 17:47:59 | `fae3c4640507` | 成果面 |
| 3653 | `results/_v3_s_phrasetemplate_prereg_v1_2026_09_27.md` | 33,932 | 2026-09-27 17:11:28 | `7e1323b09030` | 成果面 |
| 3654 | `results/_v3_s_prereg_v1_2026_09_27.md` | 46,836 | 2026-09-27 15:28:46 | `ef5a40554960` | 成果面 |
| 3655 | `results/_v3_supplement_verdict_2026_09_23.md` | 15,247 | 2026-09-23 14:27:09 | `b70211bfa83e` | 成果面 |
| 3656 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 194,083 | 2026-09-30 16:18:35 | `965db22e9130` | 成果面 |
| 3657 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 355,819 | 2026-09-29 12:12:36 | `df7e9cd39251` | 成果面 |
| 3658 | `results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md` | 10,288 | 2026-09-24 18:55:03 | `55cd332f66f2` | 成果面 |
| 3659 | `results/_v3_v4_ghostref_reconciliation_2026_09_23.md` | 169,864 | 2026-09-23 15:11:45 | `1d52db0ebf53` | 成果面 |
| 3660 | `results/_v3n_cpath_live_rerun_2026_10_01.json` | 60,012 | 2026-10-01 09:24:20 | `7c26d08ece3b` | 成果面 |
| 3661 | `results/_v3x_18frozen_remeasure_2026_09_16/v3x_18frozen_remeasure_results_2026_09_16.json` | 4,202 | 2026-09-16 23:32:09 | `928794710241` | 成果面 |
| 3662 | `results/_v3x_conservation_anchor_2026_09_17.txt` | 940 | 2026-09-17 10:20:17 | `f331a9c2bd22` | 成果面 |
| 3663 | `results/_v3x_d0_5_aggregation_2026_09_17.md` | 12,010 | 2026-09-17 13:08:30 | `ddf0d1aa96d2` | 成果面 |
| 3664 | `results/_v3x_d0_5_experiment_invitation_2026_09_17.md` | 7,617 | 2026-09-17 09:34:32 | `d8f2b99aa527` | 成果面 |
| 3665 | `results/_v3x_d0_5_proposal_coze_2026_09_17.md` | 13,200 | 2026-09-17 11:06:19 | `759c25b21ed4` | 成果面 |
| 3666 | `results/_v3x_d0_5_proposal_trae_2026_09_17.md` | 13,254 | 2026-09-20 17:11:14 | `b1c227d54a82` | 成果面 |
| 3667 | `results/_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json` | 17,053 | 2026-09-16 12:37:12 | `f39412103366` | 成果面 |
| 3668 | `results/_v3x_p_k_verify_2026_09_16/v3x_p_k_verify_results_2026_09_16.json` | 2,059 | 2026-09-16 23:33:03 | `59c2113b7c71` | 成果面 |
| 3669 | `results/_v3x_p_l_v3_external_spec_2026_09_17.md` | 5,769 | 2026-09-17 11:03:24 | `6a5b6eb635f0` | 成果面 |
| 3670 | `results/_v3x_p_l_v3_mistral_large_2512_20260917_115049.json` | 16,835 | 2026-09-17 11:52:29 | `523b5941c30c` | 成果面 |
| 3671 | `results/_v3x_p_l_v3_summary_mistral_large_2512_20260917_115049.md` | 9,570 | 2026-09-17 11:53:50 | `183205baa9ac` | 成果面 |
| 3672 | `results/_v4_bom_u1_prereg_2026_09_28.md` | 19,185 | 2026-09-28 18:33:05 | `5456acbf2cb5` | 成果面 |
| 3673 | `results/_v4_checkpoint_atomic_and_pycache_2026_09_28.md` | 25,470 | 2026-09-28 15:55:24 | `52b3dec13e06` | 成果面 |
| 3674 | `results/_v4_closeout_account_reconciliation_2026_10_12.md` | 24,453 | 2026-10-12 02:16:41 | `4a3b661a7d13` | 成果面 |
| 3675 | `results/_v4_closeout_bulk_reorganize_register_2026_10_12.md` | 197,283 | 2026-10-12 03:09:00 | `2b244f0760b4` | 成果面 |
| 3676 | `results/_v4_closeout_moves_and_cleanup_register_2026_10_12.md` | 18,568 | 2026-10-12 02:30:44 | `69a834caf812` | 成果面 |
| 3677 | `results/_v4_day_inventory_2026_09_27.md` | 40,487 | 2026-09-27 18:11:43 | `7662d5058a7d` | 成果面 |
| 3678 | `results/_v4_day_inventory_measure_2026_09_27.py` | 8,226 | 2026-09-27 18:02:27 | `3e903f224f87` | 成果面 |
| 3679 | `results/_v4_effective_register_2026_09_28.md` | 30,607 | 2026-09-28 14:22:37 | `2a65c1274202` | 成果面 |
| 3680 | `results/_v4_evidence_audit_reconcile_2026_09_26.md` | 24,168 | 2026-09-30 16:15:20 | `fe907046eda1` | 成果面 |
| 3681 | `results/_v4_exec_surface_switch_2026_09_28.md` | 28,506 | 2026-09-28 17:28:07 | `3bc852e0d48b` | 成果面 |
| 3682 | `results/_v4_item04_textfix_prereg_v1x_2026_09_28.md` | 42,153 | 2026-09-28 17:46:40 | `4ad2695935d3` | 成果面 |
| 3683 | `results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` | 37,629 | 2026-09-26 19:12:42 | `cc498bc28525` | 成果面 |
| 3684 | `results/_v4_maindir_count_monitor_2026_09_27.md` | 15,313 | 2026-09-27 11:50:37 | `71e9cc179bec` | 成果面 |
| 3685 | `results/_v4_pi_cot_v2_coding_review_2026_09_26.md` | 42,914 | 2026-09-26 18:35:47 | `5fbec21e0ad2` | 成果面 |
| 3686 | `results/_v4_pi_cot_v2_dataset.json` | 12,672 | 2026-09-24 15:55:01 | `7b01cd835a41` | 成果面 |
| 3687 | `results/_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | 4,103 | 2026-09-24 18:47:18 | `172093a23e4b` | 成果面 |
| 3688 | `results/_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json` | 6,132 | 2026-09-26 16:54:17 | `439721007aaf` | 成果面 |
| 3689 | `results/_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json` | 7,566 | 2026-09-26 17:04:48 | `41d6c28ca87c` | 成果面 |
| 3690 | `results/_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json` | 6,666 | 2026-09-26 17:22:21 | `99c58906f792` | 成果面 |
| 3691 | `results/_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json` | 7,668 | 2026-09-26 17:27:21 | `c6d092f77932` | 成果面 |
| 3692 | `results/_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json` | 10,257 | 2026-09-26 17:39:37 | `26f110a6e571` | 成果面 |
| 3693 | `results/_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json` | 11,589 | 2026-09-26 18:10:28 | `6e104e2db038` | 成果面 |
| 3694 | `results/_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json` | 14,722 | 2026-09-26 18:18:19 | `d96b747bfc6c` | 成果面 |
| 3695 | `results/_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | 19,615 | 2026-09-26 18:30:47 | `401bd614cdf7` | 成果面 |
| 3696 | `results/_v4_pi_cot_v2_prereg.md` | 4,247 | 2026-09-23 17:56:05 | `cc25c5149ce1` | 成果面 |
| 3697 | `results/_v4_pi_cot_v2_questionnaire_v1.md` | 12,402 | 2026-09-24 10:51:01 | `7b14cdb31d21` | 成果面 |
| 3698 | `results/_v4_pi_cot_v2_result.json` | 9,068 | 2026-09-24 17:41:54 | `1665f367b2c4` | 成果面 |
| 3699 | `results/_v4_pi_cot_v2_result_v2.json` | 18,089 | 2026-09-26 18:50:30 | `f86727c857a8` | 成果面 |
| 3700 | `results/_v4_pi_cot_v2_ruleset.json` | 5,876 | 2026-09-24 17:41:54 | `821465001819` | 成果面 |
| 3701 | `results/_v4_pi_cot_v2_ruleset_executor.py` | 39,281 | 2026-09-24 17:41:44 | `48dca1d4281c` | 成果面 |
| 3702 | `results/_v4_pi_cot_v2_ruleset_v2.json` | 6,179 | 2026-09-26 18:50:30 | `c5b3dd141655` | 成果面 |
| 3703 | `results/_v4_pi_cot_v2_ruleset_v2_executor.py` | 52,465 | 2026-09-26 18:49:42 | `eb22f13d571c` | 成果面 |
| 3704 | `results/_v4_pi_cot_v2_verdict.md` | 22,340 | 2026-09-24 18:07:05 | `eb9ad4193cf2` | 成果面 |
| 3705 | `results/_v4_pi_cot_v2_verdict_v2.md` | 33,723 | 2026-09-26 19:03:30 | `5d79e67a4e9d` | 成果面 |
| 3706 | `results/_v4_pi_cot_v3_alt_reading_definition_2026_09_27.md` | 10,251 | 2026-09-27 17:14:41 | `58ed6be022ed` | 成果面 |
| 3707 | `results/_v4_pi_cot_v3_dataset.json` | 16,025 | 2026-09-27 12:12:25 | `5118f5b44f17` | 成果面 |
| 3708 | `results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json` | 20,194 | 2026-09-27 12:10:45 | `cbf60a630c9f` | 成果面 |
| 3709 | `results/_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json` | 18,714 | 2026-09-27 17:04:40 | `6eed9acdb99a` | 成果面 |
| 3710 | `results/_v4_pi_cot_v3_dataset_addendum_d5_2026_09_27.json` | 16,587 | 2026-09-27 13:17:51 | `990c0c42a6f6` | 成果面 |
| 3711 | `results/_v4_pi_cot_v3_dataset_addendum_d6_2026_09_28.json` | 19,214 | 2026-09-28 13:46:29 | `9669efa804b7` | 成果面 |
| 3712 | `results/_v4_pi_cot_v3_dataset_addendum_d6b_2026_09_28.json` | 27,009 | 2026-09-28 15:00:07 | `5d94a8617b5b` | 成果面 |
| 3713 | `results/_v4_pi_cot_v3_dataset_addendum_d8_bhalf_2026_09_30.json` | 58,581 | 2026-09-30 16:21:49 | `b02ef31f1e4e` | 成果面 |
| 3714 | `results/_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json` | 374,072 | 2026-09-30 16:18:01 | `769ef8b71462` | 成果面 |
| 3715 | `results/_v4_pi_cot_v3_dataset_addendum_s3_d1fill_2026_10_01.json` | 46,909 | 2026-10-01 12:55:21 | `b9026cbf5ca2` | 成果面 |
| 3716 | `results/_v4_pi_cot_v3_dataset_addendum_s3_d7_2026_09_29.json` | 17,252 | 2026-09-29 10:57:48 | `c0ebbd1f4633` | 成果面 |
| 3717 | `results/_v4_pi_cot_v3_dataset_v1p3_2026_09_27.json` | 12,975 | 2026-09-27 17:48:03 | `ed596914259a` | 成果面 |
| 3718 | `results/_v4_pi_cot_v3_k3b_recheck_r1_2026_09_27.json` | 26,891 | 2026-09-27 17:13:08 | `cbc14a76f038` | 成果面 |
| 3719 | `results/_v4_pi_cot_v3_missing_ledger_correction_2026_09_28.md` | 12,851 | 2026-09-28 14:03:02 | `44c4d570375c` | 成果面 |
| 3720 | `results/_v4_pi_cot_v3_prereg.md` | 27,223 | 2026-09-27 12:02:44 | `b7547329af2e` | 成果面 |
| 3721 | `results/_v4_pi_cot_v3_questionnaire_v2_d8_2026_09_28.md` | 53,581 | 2026-09-28 15:19:16 | `238077d25919` | 成果面 |
| 3722 | `results/_v4_pi_cot_v3_result_v3.json` | 27,203 | 2026-09-27 13:04:21 | `585714f9660c` | 成果面 |
| 3723 | `results/_v4_pi_cot_v3_result_v3r1_2026_09_27.json` | 22,292 | 2026-09-27 17:48:03 | `735c03db1ae9` | 成果面 |
| 3724 | `results/_v4_pi_cot_v3_ruleset_v3.json` | 21,392 | 2026-09-27 12:31:02 | `9d77a5e2cbab` | 成果面 |
| 3725 | `results/_v4_pi_cot_v3_ruleset_v3_executor.py` | 58,794 | 2026-09-27 12:29:46 | `8a81d90c69ba` | 成果面 |
| 3726 | `results/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py` | 62,115 | 2026-09-27 16:56:08 | `ee8671a28c2f` | 成果面 |
| 3727 | `results/_v4_pi_cot_v3_v3r1_rescript_2026_09_27.md` | 11,385 | 2026-09-30 16:15:20 | `75aedf9ba95e` | 成果面 |
| 3728 | `results/_v4_pi_cot_v3_verdict_v3.md` | 53,751 | 2026-09-27 13:15:20 | `bb44fdc7ab0f` | 成果面 |
| 3729 | `results/_v4_pi_cot_v3_verdict_v3_signoff_2026_09_27.md` | 42,157 | 2026-09-27 13:24:20 | `41d29f4deb70` | 成果面 |
| 3730 | `results/_v4_supp_l14_n11full_verdict.md` | 19,697 | 2026-09-29 16:25:57 | `8eef73bf9856` | 成果面 |
| 3731 | `results/_v4_supp_l14v3_batch10_r1_executor.py` | 56,894 | 2026-09-26 16:32:01 | `d4dd5c949443` | 成果面 |
| 3732 | `results/_v4_supp_l14v3_batch10_r1_result.json` | 68,329 | 2026-09-26 16:36:02 | `14dddb13d658` | 成果面 |
| 3733 | `results/_v4_supp_l14v3_batch10_r2_executor.py` | 58,073 | 2026-09-26 16:49:05 | `bb601b4f5ecb` | 成果面 |
| 3734 | `results/_v4_supp_l14v3_batch10_r2_result.json` | 69,460 | 2026-09-26 16:53:10 | `400ee4d21fc9` | 成果面 |
| 3735 | `results/_v4_supp_l14v3_batch10_r3_executor.py` | 58,539 | 2026-09-26 16:56:53 | `eef1475e325c` | 成果面 |
| 3736 | `results/_v4_supp_l14v3_batch10_r3_result.json` | 70,658 | 2026-09-26 17:00:02 | `88a06f08928f` | 成果面 |
| 3737 | `results/_v4_supp_l14v3_batch10_r4_executor.py` | 68,856 | 2026-09-26 17:06:19 | `4f68937d7a95` | 成果面 |
| 3738 | `results/_v4_supp_l14v3_batch10_r4_result.json` | 74,733 | 2026-09-26 17:09:13 | `9d91a8dc039a` | 成果面 |
| 3739 | `results/_v4_supp_l14v3_batch10_r5_result.json` | 74,979 | 2026-09-26 17:18:27 | `7f02e08fc0da` | 成果面 |
| 3740 | `results/_v4_supp_l14v3_batch1_executor.py` | 29,354 | 2026-09-24 20:45:39 | `b48019494530` | 成果面 |
| 3741 | `results/_v4_supp_l14v3_batch1_r2_executor.py` | 29,598 | 2026-09-24 21:00:44 | `2bdb5163400f` | 成果面 |
| 3742 | `results/_v4_supp_l14v3_batch1_r2_result.json` | 40,815 | 2026-09-24 21:11:40 | `00c7b545c397` | 成果面 |
| 3743 | `results/_v4_supp_l14v3_batch1_r3_executor.py` | 43,289 | 2026-09-24 21:15:11 | `60c78b6f0281` | 成果面 |
| 3744 | `results/_v4_supp_l14v3_batch1_r3_result.json` | 44,888 | 2026-09-24 21:25:24 | `6e01255b80c9` | 成果面 |
| 3745 | `results/_v4_supp_l14v3_batch1_r4_executor.py` | 46,811 | 2026-09-24 21:28:35 | `4f5269ba8f18` | 成果面 |
| 3746 | `results/_v4_supp_l14v3_batch1_r4_result.json` | 46,927 | 2026-09-24 21:38:53 | `9c800874701a` | 成果面 |
| 3747 | `results/_v4_supp_l14v3_batch1_r5_executor.py` | 49,138 | 2026-09-24 21:43:59 | `91c72f8ad209` | 成果面 |
| 3748 | `results/_v4_supp_l14v3_batch1_r5_result.json` | 67,897 | 2026-09-24 21:54:45 | `664355f29ab9` | 成果面 |
| 3749 | `results/_v4_supp_l14v3_batch1_r6_executor.py` | 47,242 | 2026-09-24 21:59:06 | `5f02c7e0f094` | 成果面 |
| 3750 | `results/_v4_supp_l14v3_batch1_r6_result.json` | 57,925 | 2026-09-25 00:27:42 | `6b92bbff7180` | 成果面 |
| 3751 | `results/_v4_supp_l14v3_batch1_result.json` | 46,518 | 2026-09-24 20:56:34 | `22eb01144062` | 成果面 |
| 3752 | `results/_v4_supp_l14v3_batch2_r1_executor.py` | 50,808 | 2026-09-24 22:34:16 | `e52f930654d3` | 成果面 |
| 3753 | `results/_v4_supp_l14v3_batch2_r1_result.json` | 4,128 | 2026-09-24 22:35:43 | `d245ae4ce385` | 成果面 |
| 3754 | `results/_v4_supp_l14v3_batch2_r2_executor.py` | 55,317 | 2026-09-24 22:44:56 | `e7418f47a130` | 成果面 |
| 3755 | `results/_v4_supp_l14v3_batch2_r2_models_probe.json` | 1,503 | 2026-09-24 22:40:12 | `3c9dc60b5071` | 成果面 |
| 3756 | `results/_v4_supp_l14v3_batch2_r2_result.json` | 62,887 | 2026-09-24 22:51:00 | `8c125e257af8` | 成果面 |
| 3757 | `results/_v4_supp_l14v3_batch2_r3_executor.py` | 56,467 | 2026-09-24 23:12:40 | `72fd2bb3838e` | 成果面 |
| 3758 | `results/_v4_supp_l14v3_batch2_r3_result.json` | 62,886 | 2026-09-24 23:23:19 | `25251aca6d79` | 成果面 |
| 3759 | `results/_v4_supp_l14v3_batch2_r4_executor.py` | 58,176 | 2026-09-24 23:26:12 | `d9fe7aa2d292` | 成果面 |
| 3760 | `results/_v4_supp_l14v3_batch2_r4_result.json` | 63,572 | 2026-09-24 23:30:50 | `15b8ddc5ba9e` | 成果面 |
| 3761 | `results/_v4_supp_l14v3_batch2_r5_executor.py` | 60,046 | 2026-09-27 20:26:47 | `bf1e4fe02402` | 成果面 |
| 3762 | `results/_v4_supp_l14v3_batch2_r5_result.json` | 64,285 | 2026-09-24 23:39:39 | `479f4119cf72` | 成果面 |
| 3763 | `results/_v4_supp_l14v3_batch2_r6_result.json` | 65,083 | 2026-09-24 23:50:52 | `e37d9c74c3e5` | 成果面 |
| 3764 | `results/_v4_supp_l14v3_batch3_r1_executor.py` | 61,899 | 2026-09-27 20:26:47 | `0c284a3dce21` | 成果面 |
| 3765 | `results/_v4_supp_l14v3_batch3_r1_result.json` | 66,520 | 2026-09-24 23:38:45 | `d24b84671c23` | 成果面 |
| 3766 | `results/_v4_supp_l14v3_batch3_r2_executor.py` | 64,634 | 2026-09-27 20:26:47 | `b1699098c53b` | 成果面 |
| 3767 | `results/_v4_supp_l14v3_batch3_r2_result.json` | 67,767 | 2026-09-24 23:51:13 | `58e9c55a770d` | 成果面 |
| 3768 | `results/_v4_supp_l14v3_batch3_r3_executor.py` | 66,396 | 2026-09-27 20:26:47 | `3b7381ce5fe8` | 成果面 |
| 3769 | `results/_v4_supp_l14v3_batch3_r3_result.json` | 68,488 | 2026-09-25 00:01:27 | `6e677ffcc880` | 成果面 |
| 3770 | `results/_v4_supp_l14v3_batch3_r4_executor.py` | 68,874 | 2026-09-25 01:01:33 | `c79b5c274a10` | 成果面 |
| 3771 | `results/_v4_supp_l14v3_batch3_r4_result.json` | 69,635 | 2026-09-25 01:05:56 | `0e47768640d3` | 成果面 |
| 3772 | `results/_v4_supp_l14v3_batch3_r5_result.json` | 70,064 | 2026-09-25 01:23:36 | `38998f994b84` | 成果面 |
| 3773 | `results/_v4_supp_l14v3_batch4_r1_executor.py` | 66,097 | 2026-09-24 23:35:04 | `e84bffd5dc7d` | 成果面 |
| 3774 | `results/_v4_supp_l14v3_batch4_r1_result.json` | 71,775 | 2026-09-24 23:41:34 | `7d9fe9d319a2` | 成果面 |
| 3775 | `results/_v4_supp_l14v3_batch4_r2_executor.py` | 66,774 | 2026-09-24 23:49:42 | `7d8e12267790` | 成果面 |
| 3776 | `results/_v4_supp_l14v3_batch4_r2_result.json` | 71,998 | 2026-09-24 23:55:28 | `6a9a362d9869` | 成果面 |
| 3777 | `results/_v4_supp_l14v3_batch4_r3_executor.py` | 68,560 | 2026-09-25 00:02:06 | `b5e1c3637405` | 成果面 |
| 3778 | `results/_v4_supp_l14v3_batch4_r3_result.json` | 72,884 | 2026-09-25 00:08:49 | `ed5267df7d6f` | 成果面 |
| 3779 | `results/_v4_supp_l14v3_batch4_r4_executor.py` | 73,379 | 2026-09-25 01:08:47 | `184186902a9f` | 成果面 |
| 3780 | `results/_v4_supp_l14v3_batch4_r4_result.json` | 74,448 | 2026-09-25 01:20:35 | `41e0ba55e205` | 成果面 |
| 3781 | `results/_v4_supp_l14v3_batch4_r5_executor.py` | 78,984 | 2026-09-25 01:27:34 | `8a505613b476` | 成果面 |
| 3782 | `results/_v4_supp_l14v3_batch4_r5_result.json` | 76,138 | 2026-09-25 01:34:21 | `bad01f2b89fd` | 成果面 |
| 3783 | `results/_v4_supp_l14v3_batch4_r6_executor.py` | 80,877 | 2026-09-25 01:44:02 | `7f2c5e26e6c5` | 成果面 |
| 3784 | `results/_v4_supp_l14v3_batch4_r6_result.json` | 32,369 | 2026-09-25 01:44:37 | `6b8093ff8962` | 成果面 |
| 3785 | `results/_v4_supp_l14v3_batch5_r1_executor.py` | 63,517 | 2026-09-27 20:26:47 | `dac0648507b9` | 成果面 |
| 3786 | `results/_v4_supp_l14v3_batch5_r1_result.json` | 71,021 | 2026-09-24 23:36:37 | `120d45d1774f` | 成果面 |
| 3787 | `results/_v4_supp_l14v3_batch5_r2_executor.py` | 66,252 | 2026-09-27 20:26:47 | `4c40334929bb` | 成果面 |
| 3788 | `results/_v4_supp_l14v3_batch5_r2_result.json` | 72,550 | 2026-09-24 23:52:24 | `b0f76b5c3522` | 成果面 |
| 3789 | `results/_v4_supp_l14v3_batch5_r3_executor.py` | 66,454 | 2026-09-27 20:26:47 | `ed9557830f8b` | 成果面 |
| 3790 | `results/_v4_supp_l14v3_batch5_r3_result.json` | 73,682 | 2026-09-25 00:03:51 | `8e2acdacfa1e` | 成果面 |
| 3791 | `results/_v4_supp_l14v3_batch5_r4_executor.py` | 67,894 | 2026-09-25 01:01:38 | `28844c34b12b` | 成果面 |
| 3792 | `results/_v4_supp_l14v3_batch5_r4_result.json` | 74,100 | 2026-09-25 01:04:23 | `1c62520c372b` | 成果面 |
| 3793 | `results/_v4_supp_l14v3_batch5_r5_executor.py` | 77,033 | 2026-09-25 01:08:52 | `82c283d8f37a` | 成果面 |
| 3794 | `results/_v4_supp_l14v3_batch5_r5_result.json` | 77,137 | 2026-09-25 01:11:16 | `c874d21a4cbe` | 成果面 |
| 3795 | `results/_v4_supp_l14v3_batch6_r1_executor.py` | 49,296 | 2026-09-25 00:28:11 | `ad35565f1ec9` | 成果面 |
| 3796 | `results/_v4_supp_l14v3_batch6_r1_result.json` | 57,799 | 2026-09-25 00:39:57 | `0d29e1ab4ae2` | 成果面 |
| 3797 | `results/_v4_supp_l14v3_batch6_r2_executor.py` | 53,494 | 2026-09-25 01:01:58 | `93c931fc3b1c` | 成果面 |
| 3798 | `results/_v4_supp_l14v3_batch6_r2_result.json` | 64,672 | 2026-09-25 01:14:34 | `96e1de46ed30` | 成果面 |
| 3799 | `results/_v4_supp_l14v3_batch6_r3_executor.py` | 53,717 | 2026-09-25 01:27:17 | `1385d2ca356f` | 成果面 |
| 3800 | `results/_v4_supp_l14v3_batch6_r3_result.json` | 64,975 | 2026-09-25 01:38:53 | `15a7fecdffe7` | 成果面 |
| 3801 | `results/_v4_supp_l14v3_batch6_r4_executor.py` | 54,588 | 2026-09-25 01:42:04 | `08f329b36e9d` | 成果面 |
| 3802 | `results/_v4_supp_l14v3_batch6_r4_result.json` | 65,254 | 2026-09-25 01:53:14 | `b7377ba019a1` | 成果面 |
| 3803 | `results/_v4_supp_l14v3_batch6_r5_executor.py` | 57,783 | 2026-09-25 01:56:05 | `8a8babb911b8` | 成果面 |
| 3804 | `results/_v4_supp_l14v3_batch6_r5_result.json` | 65,651 | 2026-09-25 02:07:09 | `e40424bf8abe` | 成果面 |
| 3805 | `results/_v4_supp_l14v3_batch7_r1_executor.py` | 51,545 | 2026-09-25 02:13:59 | `c49fc9bca8c4` | 成果面 |
| 3806 | `results/_v4_supp_l14v3_batch7_r1_result.json` | 61,114 | 2026-09-25 02:18:50 | `3558a1d15867` | 成果面 |
| 3807 | `results/_v4_supp_l14v3_batch7_r2_executor.py` | 53,145 | 2026-09-25 02:26:48 | `35cda0c0f7da` | 成果面 |
| 3808 | `results/_v4_supp_l14v3_batch7_r2_result.json` | 61,458 | 2026-09-25 02:31:15 | `924f12c4e7ab` | 成果面 |
| 3809 | `results/_v4_supp_l14v3_batch7_r3_executor.py` | 51,271 | 2026-09-25 02:41:04 | `5c0b426e2ee0` | 成果面 |
| 3810 | `results/_v4_supp_l14v3_batch7_r3_result.json` | 61,389 | 2026-09-25 02:46:39 | `b431a1ba54df` | 成果面 |
| 3811 | `results/_v4_supp_l14v3_batch7_r4_executor.py` | 51,289 | 2026-09-25 03:06:20 | `d789f9bd4fa1` | 成果面 |
| 3812 | `results/_v4_supp_l14v3_batch7_r4_result.json` | 61,824 | 2026-09-25 03:13:45 | `0fe4c1339d88` | 成果面 |
| 3813 | `results/_v4_supp_l14v3_batch7_r5_result.json` | 61,658 | 2026-09-25 03:29:41 | `09a481ebca6b` | 成果面 |
| 3814 | `results/_v4_supp_l14v3_batch8_r1_executor.py` | 56,181 | 2026-09-25 02:21:24 | `1e5f2249c517` | 成果面 |
| 3815 | `results/_v4_supp_l14v3_batch8_r1_result.json` | 62,531 | 2026-09-25 02:21:40 | `e6a94a0a13b7` | 成果面 |
| 3816 | `results/_v4_supp_l14v3_batch8_r2_executor.py` | 57,634 | 2026-09-25 02:35:52 | `6a9bbc43c808` | 成果面 |
| 3817 | `results/_v4_supp_l14v3_batch8_r2_result.json` | 63,440 | 2026-09-25 02:36:27 | `7b23996b5f4c` | 成果面 |
| 3818 | `results/_v4_supp_l14v3_batch8_r3_executor.py` | 58,494 | 2026-09-25 02:50:01 | `0f654d945f12` | 成果面 |
| 3819 | `results/_v4_supp_l14v3_batch8_r3_result.json` | 63,670 | 2026-09-25 03:00:00 | `56faf9324fba` | 成果面 |
| 3820 | `results/_v4_supp_l14v3_batch8_r4_executor.py` | 59,351 | 2026-09-25 03:13:26 | `6b69ec8406d4` | 成果面 |
| 3821 | `results/_v4_supp_l14v3_batch8_r4_result.json` | 64,038 | 2026-09-25 03:18:20 | `c7d5aa2a9b00` | 成果面 |
| 3822 | `results/_v4_supp_l14v3_batch8_r5_executor.py` | 60,475 | 2026-09-25 03:32:20 | `6961281824ae` | 成果面 |
| 3823 | `results/_v4_supp_l14v3_batch8_r5_result.json` | 63,785 | 2026-09-25 03:37:47 | `3620a7daf9c1` | 成果面 |
| 3824 | `results/_v4_supp_l14v3_batch9_r1_executor.py` | 60,645 | 2026-09-26 16:38:53 | `e78ca71bd077` | 成果面 |
| 3825 | `results/_v4_supp_l14v3_batch9_r1_result.json` | 69,251 | 2026-09-26 16:38:42 | `7e8dfe0156cd` | 成果面 |
| 3826 | `results/_v4_supp_l14v3_batch9_r2_executor.py` | 60,580 | 2026-09-26 16:48:39 | `7eec235a9ca2` | 成果面 |
| 3827 | `results/_v4_supp_l14v3_batch9_r2_result.json` | 69,325 | 2026-09-26 16:56:40 | `08b0aaaae726` | 成果面 |
| 3828 | `results/_v4_supp_l14v3_batch9_r3_executor.py` | 62,131 | 2026-09-26 17:01:28 | `cfe41dd4fe62` | 成果面 |
| 3829 | `results/_v4_supp_l14v3_batch9_r3_result.json` | 69,984 | 2026-09-26 17:08:33 | `29e0d865a7bf` | 成果面 |
| 3830 | `results/_v4_supp_l14v3_batch9_r4_executor.py` | 64,538 | 2026-09-26 17:14:29 | `1b3fcfbacd59` | 成果面 |
| 3831 | `results/_v4_supp_l14v3_batch9_r4_result.json` | 71,093 | 2026-09-26 17:23:11 | `eb8b13d9f592` | 成果面 |
| 3832 | `results/_v4_supp_l14v3_batch9_r5_result.json` | 72,047 | 2026-09-26 17:34:59 | `1610f5060ef1` | 成果面 |
| 3833 | `results/_v4_supp_l14v3_model_mapping_2026_09_24.md` | 49,326 | 2026-09-30 16:15:20 | `9ba12a0fbac1` | 成果面 |
| 3834 | `results/_v4_supp_l14v3_n26_verdict.md` | 65,978 | 2026-09-30 16:15:20 | `df6453d57f8a` | 成果面 |
| 3835 | `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md` | 62,847 | 2026-09-30 16:15:20 | `e7c3e2ef4e6b` | 成果面 |
| 3836 | `results/_v4_supp_prereg_v02_add_T15_2026_09_24.md` | 76,991 | 2026-09-24 23:48:31 | `8898b964a9d9` | 成果面 |
| 3837 | `results/_v4_supp_prereg_v02_add_T15r2_2026_09_26.md` | 97,059 | 2026-09-26 16:38:20 | `883dced872b4` | 成果面 |
| 3838 | `results/_v4_supp_prereg_v02_add_T15r2_activation_2026_09_26.md` | 34,195 | 2026-09-26 16:36:21 | `f6ed61c25572` | 成果面 |
| 3839 | `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` | 52,942 | 2026-09-24 20:29:16 | `802dece2286a` | 成果面 |
| 3840 | `results/_v4_supp_t15_executor.py` | 62,285 | 2026-09-24 23:57:30 | `558e635f9ba6` | 成果面 |
| 3841 | `results/_v4_supp_t15_executor_r0_atomic_2026_09_29.py` | 66,317 | 2026-09-29 11:12:41 | `7da23c0e94cf` | 成果面 |
| 3842 | `results/_v4_supp_t15_executor_r1_2026_09_27.py` | 67,517 | 2026-09-27 20:51:43 | `6d22444c65af` | 成果面 |
| 3843 | `results/_v4_supp_t15_executor_r2_atomic_2026_09_28.py` | 70,056 | 2026-09-28 15:46:02 | `9e89e021ea03` | 成果面 |
| 3844 | `results/_v4_supp_t15_executor_r3_2026_09_28.py` | 70,056 | 2026-09-28 17:25:01 | `b86cce242abe` | 成果面 |
| 3845 | `results/_v4_supp_t15_result.json` | 53,265 | 2026-09-25 00:44:39 | `6b47d389b7ae` | 成果面 |
| 3846 | `results/_v4_supp_t15_verdict.md` | 54,377 | 2026-09-30 16:15:20 | `3cb5c2f59961` | 成果面 |
| 3847 | `results/_v4_supp_t15r2_executor.py` | 84,884 | 2026-09-26 16:50:49 | `4b5b720d5cda` | 成果面 |
| 3848 | `results/_v4_supp_t15r2_executor_r0_atomic_2026_09_29.py` | 89,083 | 2026-09-29 11:12:41 | `678032f726a8` | 成果面 |
| 3849 | `results/_v4_supp_t15r2_executor_r1_2026_09_28.py` | 90,390 | 2026-09-28 15:14:04 | `e0936a68fa82` | 成果面 |
| 3850 | `results/_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py` | 92,915 | 2026-09-28 15:44:50 | `215db16a0556` | 成果面 |
| 3851 | `results/_v4_supp_t15r2_executor_r3_2026_09_28.py` | 92,915 | 2026-09-28 17:25:01 | `4f514b3fb4b8` | 成果面 |
| 3852 | `results/_v4_supp_t15r2_result.json` | 73,526 | 2026-09-26 17:15:40 | `c69ab0e3002e` | 成果面 |
| 3853 | `results/_v4_supp_t15r2_verdict.md` | 65,638 | 2026-09-30 16:15:20 | `963725dbd82a` | 成果面 |
| 3854 | `results/_v4_supp_t1_executor.py` | 60,563 | 2026-09-27 20:26:47 | `91b8f70e4e18` | 成果面 |
| 3855 | `results/_v4_supp_t1_result.json` | 82,365 | 2026-09-24 22:32:37 | `d6cb03a4657e` | 成果面 |
| 3856 | `results/_v4_supp_t1_verdict.md` | 29,106 | 2026-09-30 16:15:20 | `0ad42625f333` | 成果面 |
| 3857 | `results/_v4_track2_multimodel_rerun.py` | 38,719 | 2026-09-27 20:26:47 | `5c0983eaaf11` | 成果面 |
| 3858 | `results/_v4_track2_multimodel_rerun_2026_09_23.json` | 35,011 | 2026-09-23 15:26:47 | `e3dae2a4bbc2` | 成果面 |
| 3859 | `results/_v4_track2_multimodel_verdict_2026_09_23.md` | 12,883 | 2026-09-23 15:27:54 | `44d9bad9039b` | 成果面 |
| 3860 | `results/_v5_b15_pp1_impl_fix_2026_09_29.md` | 12,911 | 2026-09-29 17:33:06 | `ded842b6241c` | 成果面 |
| 3861 | `results/_v5_bulk_activation_2026_09_28.md` | 39,378 | 2026-09-30 17:02:47 | `b5a50447b4da` | 成果面 |
| 3862 | `results/_v5_c3_reading_b_prereg_2026_09_28.md` | 32,178 | 2026-09-30 17:02:47 | `8dcf5e1e6dde` | 成果面 |
| 3863 | `results/_v5_checkpoint_tail3_revision_2026_09_29.md` | 27,966 | 2026-09-29 11:24:06 | `c962851ff3ff` | 成果面 |
| 3864 | `results/_v5_clearance_mr14_rerun_note_2026_09_29.md` | 22,894 | 2026-09-29 19:12:01 | `f3dd5efd3e34` | 成果面 |
| 3865 | `results/_v5_closing_register_2026_09_28.md` | 27,224 | 2026-09-30 17:02:47 | `522b08506290` | 成果面 |
| 3866 | `results/_v5_confirm_b11_decisions_register_2026_09_29.md` | 12,276 | 2026-09-29 14:20:13 | `07e9fe512da5` | 成果面 |
| 3867 | `results/_v5_confirm_b14_b15_decisions_register_2026_09_29.md` | 26,154 | 2026-09-29 15:21:25 | `e48276a8dd31` | 成果面 |
| 3868 | `results/_v5_confirm_b5_decisions_register_2026_09_29.md` | 45,525 | 2026-09-29 13:43:30 | `3b5f2819af8f` | 成果面 |
| 3869 | `results/_v5_confirm_b7_decisions_register_2026_09_29.md` | 23,833 | 2026-09-29 14:04:02 | `0a80ae035042` | 成果面 |
| 3870 | `results/_v5_confirm_b9_decisions_register_2026_09_29.md` | 17,008 | 2026-09-29 14:13:01 | `8c510cda6014` | 成果面 |
| 3871 | `results/_v5_exec_f2_r3_register_2026_09_29.md` | 24,177 | 2026-09-29 10:54:17 | `9d64ee1d6996` | 成果面 |
| 3872 | `results/_v5_fake_verdict_session_log_2026_09_28.md` | 18,877 | 2026-09-30 17:02:47 | `132bfa0c02f5` | 成果面 |
| 3873 | `results/_v5_fake_verdict_v1x_prereg_2026_09_28.md` | 28,484 | 2026-09-30 17:02:47 | `088085d6c90d` | 成果面 |
| 3874 | `results/_v5_gt4_reattrib_2026_09_29.json` | 3,074 | 2026-09-29 11:18:07 | `4b75df5f7454` | 成果面 |
| 3875 | `results/_v5_gt5_gt6_gt8_gt5b_gt_prereg_2026_09_28.md` | 63,447 | 2026-09-28 20:14:25 | `2505ff5d203f` | 成果面 |
| 3876 | `results/_v5_gt5_reattrib_2026_09_29.json` | 5,626 | 2026-09-29 11:18:07 | `e15b3b171d60` | 成果面 |
| 3877 | `results/_v5_gt5b_reattrib_2026_09_29.json` | 7,084 | 2026-09-29 11:18:07 | `212e5bb8c7d7` | 成果面 |
| 3878 | `results/_v5_gt6_trajint_2026_09_29.json` | 83,722 | 2026-09-29 11:18:07 | `578fbeaa4635` | 成果面 |
| 3879 | `results/_v5_gt8_expand_2026_09_29.json` | 20,090 | 2026-09-29 11:18:07 | `34ff826f97c2` | 成果面 |
| 3880 | `results/_v5_gt8_lowarm_exec_2026_09_29.md` | 21,542 | 2026-09-29 15:34:42 | `365ea6cb77e8` | 成果面 |
| 3881 | `results/_v5_gt8_lowarm_result_2026_09_29.json` | 26,253 | 2026-09-29 15:21:52 | `c68076c88140` | 成果面 |
| 3882 | `results/_v5_gt8_lowarm_resultb_2026_09_29.json` | 48,948 | 2026-09-29 15:32:44 | `8aa69a5e922d` | 成果面 |
| 3883 | `results/_v5_gt8_lowarm_seta_verify_2026_09_29.json` | 9,001 | 2026-09-29 15:33:32 | `d1370b0a3853` | 成果面 |
| 3884 | `results/_v5_gt_exec_2026_09_29.md` | 27,701 | 2026-09-29 11:21:06 | `9a679f43f796` | 成果面 |
| 3885 | `results/_v5_gt_p10_lowarm_prereg_2026_09_29.md` | 38,464 | 2026-09-29 13:58:52 | `07e28e2fe374` | 成果面 |
| 3886 | `results/_v5_gt_verdict_2026_09_29.md` | 57,227 | 2026-09-29 11:41:25 | `45648b0ec940` | 成果面 |
| 3887 | `results/_v5_handover_guide_project_initiation_2026_10_12.md` | 5,580 | 2026-10-12 21:49:39 | `dddf7b0a7221` | 成果面 |
| 3888 | `results/_v5_item21_anchor_recompute_2026_09_28.json` | 9,527 | 2026-09-28 20:03:28 | `47177cab0303` | 成果面 |
| 3889 | `results/_v5_item21_anchor_recompute_2026_09_28.md` | 9,221 | 2026-09-28 20:04:46 | `e5623d4bd3f3` | 成果面 |
| 3890 | `results/_v5_item21_patched_recompute_2026_09_28.json` | 14,879 | 2026-09-28 20:26:23 | `aa53e5db77c9` | 成果面 |
| 3891 | `results/_v5_item21_strategyqa_realias_recompute_2026_09_29.json` | 34,314 | 2026-09-29 16:17:02 | `49f068c716a8` | 成果面 |
| 3892 | `results/_v5_item26b_attribution_effective_2026_09_28.md` | 35,261 | 2026-09-28 22:29:35 | `c353fbcdc753` | 成果面 |
| 3893 | `results/_v5_item26b_endpoint_definition_prereg_2026_09_28.md` | 38,939 | 2026-09-28 21:32:27 | `5e59a11466db` | 成果面 |
| 3894 | `results/_v5_item26b_literal_gap_prereg_v2_2026_09_28.md` | 38,885 | 2026-09-28 20:24:02 | `bb0a211fa675` | 成果面 |
| 3895 | `results/_v5_item35_prereg_v2_2026_09_28.md` | 35,633 | 2026-09-28 22:22:11 | `1fb2419c6e96` | 成果面 |
| 3896 | `results/_v5_item35_v2_matrix_exec_2026_09_29.md` | 24,624 | 2026-09-29 12:27:44 | `4e88682284d8` | 成果面 |
| 3897 | `results/_v5_item35_v2_matrix_result_2026_09_29.json` | 84,699 | 2026-09-29 12:27:24 | `13ad5b740f80` | 成果面 |
| 3898 | `results/_v5_item35_v2_verdict_2026_09_29.md` | 26,232 | 2026-09-29 12:56:02 | `b59bef293712` | 成果面 |
| 3899 | `results/_v5_item35_v3_collinear_prereg_2026_09_29.md` | 42,504 | 2026-09-29 13:56:34 | `873652fd39dd` | 成果面 |
| 3900 | `results/_v5_item35_v3_collinear_recompute_2026_10_01.json` | 49,682 | 2026-10-01 08:55:37 | `a210e2c41275` | 成果面 |
| 3901 | `results/_v5_item35_v3_collinear_result_2026_09_29.json` | 187,287 | 2026-09-29 14:29:52 | `99f3e504589e` | 成果面 |
| 3902 | `results/_v5_pjpm_pc_closeout_readout_2026_09_29.md` | 32,243 | 2026-09-29 13:46:56 | `1b9ac6b07670` | 成果面 |
| 3903 | `results/_v5_pjpm_pc_deg_prereg_2026_09_29.md` | 59,446 | 2026-09-29 12:17:51 | `989ee2bce660` | 成果面 |
| 3904 | `results/_v5_pjpm_pc_degen_precheck_result_2026_09_29.json` | 103,747 | 2026-09-29 13:46:56 | `3641afe9d49c` | 成果面 |
| 3905 | `results/_v5_r2h2_residual_merged_catalogue_2026_09_29.md` | 50,554 | 2026-09-29 14:29:32 | `b62d19c1c7cc` | 成果面 |
| 3906 | `results/_v5_sub_artifact_ledger_2026_09_28.md` | 71,818 | 2026-09-30 17:02:47 | `dd38c77ea486` | 成果面 |
| 3907 | `results/_v5_theory_input_acquisition_request_2026_09_29.md` | 10,751 | 2026-10-14 14:44:41 | `19099ecb3c46` | 成果面 |
| 3908 | `results/_v5_track2_qwen_retry_2026_09_29.json` | 2,735 | 2026-09-29 11:10:33 | `6acafe021aaf` | 成果面 |
| 3909 | `results/_v5_trae_doubt6_verify_2026_09_28_r3verifier.md` | 30,192 | 2026-09-30 17:02:47 | `58101ef93a6f` | 成果面 |
| 3910 | `results/_v5_v3_deg_c5_b_raw_embeddings_2026_09_29.json` | 744,352 | 2026-10-01 09:21:49 | `1088fdd2b197` | 成果面 |
| 3911 | `results/_v5_v3_deg_c5_proposal_2026_09_29.md` | 33,356 | 2026-09-29 13:25:19 | `2158b11bba9a` | 成果面 |
| 3912 | `results/_v5_v3_deg_fix_c1c4_result_2026_09_29.json` | 266,417 | 2026-09-29 12:11:14 | `1b5bfecc818e` | 成果面 |
| 3913 | `results/_v5_v3_deg_fix_exec_2026_09_29.md` | 30,261 | 2026-09-29 12:10:05 | `7d885528f287` | 成果面 |
| 3914 | `results/_v5_v3_deg_fix_prereg_2026_09_29.md` | 41,622 | 2026-09-29 11:44:32 | `98286cc1aec7` | 成果面 |
| 3915 | `results/_v5_v3_deg_p1_reopen_result_2026_09_29.json` | 571,451 | 2026-09-29 13:41:39 | `b86d6740d487` | 成果面 |
| 3916 | `results/_v5_v3_deg_reopen_line_2026_09_29.md` | 42,778 | 2026-09-29 13:17:28 | `2ea1c2cee65d` | 成果面 |
| 3917 | `results/_v5r_s40_recompute_2026_09_29.json` | 4,992 | 2026-09-29 19:19:15 | `5be465342ae1` | 成果面 |
| 3918 | `results/_value_card_template_7col_2026_10_13.md` | 17,013 | 2026-10-13 17:43:35 | `33f68fd8ea3b` | 成果面 |
| 3919 | `results/_voided_files_reference_update_2026_10_14.md` | 16,514 | 2026-10-14 01:19:06 | `3f29efd33d80` | 成果面 |
| 3920 | `results/_voided_files_relocation_register_2026_10_14.md` | 9,587 | 2026-10-14 00:50:12 | `d72b3a52c20c` | 成果面 |
| 3921 | `results/_whitelist_and_scope_ruling_effect_2026_10_17.md` | 56,228 | 2026-10-17 13:46:44 | `afd2a78e6a4f` | 成果面 |
| 3922 | `results/_whitelist_backup_mapping_2026_10_17.md` | 155,757 | 2026-10-17 12:09:31 | `8115382861f3` | 成果面 |
| 3923 | `results/_whitelist_register_2026_10_17.md` | 120,358 | 2026-10-17 12:09:31 | `7511b98c6483` | 成果面 |
| 3924 | `results/_xiang14_reissue_register_2026_10_13.md` | 13,928 | 2026-10-13 22:21:30 | `519a6be78024` | 成果面 |
| 3925 | `results/_xiang8_xiang12_deliberation_judgment_2026_10_13.md` | 36,926 | 2026-10-13 22:08:23 | `3c6edf11135d` | 成果面 |
| 3926 | `results/_z1_d9_three_and_c1_adoption_register_2026_10_12.md` | 19,446 | 2026-10-12 22:40:47 | `8f1542dca1c5` | 成果面 |
| 3927 | `results/_z1_n2_da25_agency_register_2026_10_12.md` | 22,223 | 2026-10-12 22:43:28 | `718842329683` | 成果面 |
| 3928 | `results/_z1_three_yishi_adoption_register_2026_10_12.md` | 19,922 | 2026-10-12 22:28:05 | `836b5d0611b7` | 成果面 |
| 3929 | `results/_z1_two_items_adoption_register_2026_10_12.md` | 20,261 | 2026-10-12 22:29:24 | `312d74cf5630` | 成果面 |
| 3930 | `results/_zerocall_criterion_redefinition_2026_10_17.md` | 31,602 | 2026-10-17 17:41:45 | `f2bed1e98f62` | 成果面 |
| 3931 | `results/_zerocall_gap_proof_register_2026_10_17.md` | 47,618 | 2026-10-17 17:28:51 | `92d59ee2500f` | 成果面 |
| 3932 | `results/_zone_balance_inventory_2026_10_13.md` | 725,629 | 2026-10-13 12:08:14 | `4a7cfa13c79e` | 成果面 |
| 3933 | `results/boss_pa_1_rbr_rm_result_2026_09_15.json` | 8,753 | 2026-09-15 15:28:10 | `c7c59e0d2f6c` | 成果面 |
| 3934 | `results/boss_pa_2_potential_game_result_2026_09_15.json` | 7,530 | 2026-09-15 15:28:10 | `5c76137d6430` | 成果面 |
| 3935 | `results/boss_pa_3_replicator_dynamics_result_2026_09_15.json` | 9,098 | 2026-09-15 15:28:10 | `d6f233d73c45` | 成果面 |
| 3936 | `results/boss_pc_1_a1_resampling_2026_09_15.json` | 1,017 | 2026-09-15 13:34:48 | `d21912a05d79` | 成果面 |
| 3937 | `results/boss_pc_1_real_2d_ising_2026_09_15.json` | 2,460 | 2026-09-15 15:28:00 | `43d9ce160fc8` | 成果面 |
| 3938 | `results/boss_pc_2_a2_fitting_2026_09_15.json` | 1,024 | 2026-09-15 13:34:48 | `5a880678c386` | 成果面 |
| 3939 | `results/boss_pc_2_real_transverse_ising_2026_09_15.json` | 3,553 | 2026-09-15 15:27:35 | `8933d61b180a` | 成果面 |
| 3940 | `results/boss_pc_3_a3_clipping_2026_09_15.json` | 1,265 | 2026-09-15 13:34:48 | `d74d6b39d1b0` | 成果面 |
| 3941 | `results/boss_pc_3_real_reservoir_2026_09_15.json` | 2,364 | 2026-09-15 15:28:00 | `94b5398be76c` | 成果面 |
| 3942 | `results/boss_pe_1_real_2d_ising_2026_09_15.json` | 2,460 | 2026-09-15 13:34:49 | `43d9ce160fc8` | 成果面 |
| 3943 | `results/boss_pe_2_real_transverse_ising_2026_09_15.json` | 3,553 | 2026-09-15 13:34:49 | `8933d61b180a` | 成果面 |
| 3944 | `results/boss_pe_3_real_reservoir_2026_09_15.json` | 2,364 | 2026-09-15 13:34:49 | `94b5398be76c` | 成果面 |
| 3945 | `results/c5_b_group_fix_readings_2026_10_01.json` | 9,996 | 2026-10-01 09:25:22 | `2a7749da7c4d` | 成果面 |
| 3946 | `results/c5_b_group_fix_readings_2026_10_09.json` | 10,029 | 2026-10-09 13:39:57 | `4e415990b71d` | 成果面 |
| 3947 | `results/c5_b_group_root_candidate_2026_10_01.md` | 28,867 | 2026-10-01 09:24:13 | `2fd8946cfe80` | 成果面 |
| 3948 | `results/c5_guard_0_1_recheck_verdict_2026_10_01.md` | 33,287 | 2026-10-01 10:21:29 | `24418fa60ede` | 成果面 |
| 3949 | `results/c5_guard_minmaxstd_readings_2026_10_01.json` | 19,935 | 2026-10-01 10:14:10 | `7ff301514f66` | 成果面 |
| 3950 | `results/c5_guard_minmaxstd_report_2026_10_01.md` | 19,909 | 2026-10-01 10:15:08 | `f465fbdb7579` | 成果面 |
| 3951 | `results/d7_5anchor_60cells_9model_verdict_2026_09_18.json` | 2,456 | 2026-09-16 11:00:06 | `4505cca79c15` | 成果面 |
| 3952 | `results/deposon_benchmark_v1_3_details.json` | 656,572 | 2026-08-23 00:01:28 | `9fcb6b243e0d` | 成果面 |
| 3953 | `results/deposon_benchmark_v1_3_simple.json` | 2,245 | 2026-08-23 00:01:28 | `9347add72401` | 成果面 |
| 3954 | `results/deposon_benchmark_v1_3_traps.json` | 3,112 | 2026-08-23 00:01:28 | `82eb64151f2b` | 成果面 |
| 3955 | `results/deposon_benchmark_v1_4_gsm8k.json` | 2,741 | 2026-08-23 05:00:55 | `5cd6269d7baf` | 成果面 |
| 3956 | `results/deposon_benchmark_v1_4_gsm8k_details.json` | 208,350 | 2026-08-23 05:00:55 | `39f79fce7cdb` | 成果面 |
| 3957 | `results/deposon_benchmark_v1_4_strategyqa.json` | 1,691 | 2026-08-23 13:04:23 | `b51fd24586b3` | 成果面 |
| 3958 | `results/deposon_benchmark_v1_4_strategyqa_details.json` | 235,779 | 2026-09-16 11:01:12 | `a63ebea7b29a` | 成果面 |
| 3959 | `results/deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json` | 13,562 | 2026-09-15 13:35:18 | `4e4a17d43adf` | 成果面 |
| 3960 | `results/deposon_cpath_simulation_2026_09_10.json` | 6,351 | 2026-09-10 20:44:37 | `9466fdbf9c95` | 成果面 |
| 3961 | `results/deposon_d_fix2_metric_verify_9m60c_2026_09_15.json` | 204,441 | 2026-09-16 11:01:12 | `9f88a212a77c` | 成果面 |
| 3962 | `results/deposon_deepseek_v41_flash_30cells_v3_2026_09_10.json` | 18,592 | 2026-09-10 16:40:43 | `56401317e62b` | 成果面 |
| 3963 | `results/deposon_dpath_cross_modal_2026_09_10.json` | 75,964 | 2026-09-16 11:01:12 | `ab0c2eaff0d1` | 成果面 |
| 3964 | `results/deposon_dpath_cross_modal_runner_2026_09_10.py` | 27,930 | 2026-09-16 11:01:12 | `fb20a6ba5ec6` | 成果面 |
| 3965 | `results/deposon_feshbach_rag_30cells_2026_09_10.py` | 14,343 | 2026-09-16 11:01:12 | `a072e4184e83` | 成果面 |
| 3966 | `results/deposon_g1_mindmap_demo.json` | 3,041 | 2026-08-23 05:00:55 | `55428f6bd848` | 成果面 |
| 3967 | `results/deposon_g2_boltzmann_pathintegral.json` | 2,204 | 2026-08-23 05:00:55 | `9fd0f3399ab3` | 成果面 |
| 3968 | `results/deposon_g2_boltzmann_pathintegral_rewrite.json` | 2,782 | 2026-08-23 09:40:33 | `f36667e5b5b8` | 成果面 |
| 3969 | `results/deposon_game_theory_eval_2026_09_10.json` | 10,096 | 2026-09-10 21:53:17 | `3fa0ff2c8c08` | 成果面 |
| 3970 | `results/deposon_gpt6_teamorouter_2026_09_10.json` | 3,827 | 2026-09-10 16:49:38 | `f44636f5f72f` | 成果面 |
| 3971 | `results/deposon_gpt6_teamorouter_30cells_2026_09_10.json` | 18,290 | 2026-09-10 17:30:03 | `ea38ee252701` | 成果面 |
| 3972 | `results/deposon_gsm8k_stratified.json` | 3,411 | 2026-08-23 09:40:34 | `8b7574b25336` | 成果面 |
| 3973 | `results/deposon_openrouter_5model_rag_30cells_2026_09_10.json` | 111,710 | 2026-09-10 23:34:43 | `2e55c53be25d` | 成果面 |
| 3974 | `results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json` | 18,104 | 2026-09-16 18:39:54 | `b5873afb9d29` | 成果面 |
| 3975 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` | 20,398 | 2026-10-01 09:43:44 | `33ad1c01f745` | 成果面 |
| 3976 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json` | 21,176 | 2026-10-09 13:39:49 | `95f3f0957be8` | 成果面 |
| 3977 | `results/deposon_p_k_cross_subject_fingerprint_blind_test_2026_09_16.json` | 11,341 | 2026-09-16 18:39:55 | `576eaf8d7431` | 成果面 |
| 3978 | `results/deposon_pa_d1_d3_2026_09_15.json` | 15,604 | 2026-09-15 11:29:23 | `e221792715f8` | 成果面 |
| 3979 | `results/deposon_pc_d1_d3_2026_09_15.json` | 20,408 | 2026-09-15 11:01:56 | `b2046af03610` | 成果面 |
| 3980 | `results/deposon_pe_d1_d3_2026_09_15.json` | 17,085 | 2026-09-15 10:49:09 | `594d7a8d3de8` | 成果面 |
| 3981 | `results/deposon_pf_d1_full_9m5c_2026_09_15.json` | 33,829 | 2026-09-16 11:01:12 | `fcb5105df0b6` | 成果面 |
| 3982 | `results/deposon_pf_implementation_2026_09_11.json` | 27,311 | 2026-09-16 11:01:12 | `509dcee3b139` | 成果面 |
| 3983 | `results/deposon_pg_v01_9m60c_2026_09_15.json` | 11,512 | 2026-09-15 13:35:24 | `ab75889ee738` | 成果面 |
| 3984 | `results/deposon_risk1_02940_decision_2026_09_11.json` | 4,336 | 2026-09-15 10:22:25 | `2dc8ca9e36c1` | 成果面 |
| 3985 | `results/deposon_risk2_canonical5_decision_2026_09_11.json` | 4,066 | 2026-09-15 10:22:26 | `cf4a882160e1` | 成果面 |
| 3986 | `results/deposon_risk3_seff_decision_2026_09_11.json` | 6,488 | 2026-09-15 10:22:26 | `67867e752f47` | 成果面 |
| 3987 | `results/deposon_v15_diffusion.json` | 519,387 | 2026-08-23 19:21:32 | `c16d1768d1ca` | 成果面 |
| 3988 | `results/deposon_v15_diffusion_maxpath_negativeresult.json` | 416,460 | 2026-08-23 19:21:32 | `00ee97c82dcc` | 成果面 |
| 3989 | `results/deposon_v15_diffusion_summary.json` | 6,079 | 2026-08-23 19:22:36 | `5b95d06e66b0` | 成果面 |
| 3990 | `results/deposon_v16_llm_prior.json` | 39,974 | 2026-08-23 20:21:38 | `c17b31ae4f3b` | 成果面 |
| 3991 | `results/deposon_v16_paired_stats.json` | 9,176 | 2026-08-23 20:59:51 | `20bc4288e0de` | 成果面 |
| 3992 | `results/deposon_v17_fixed_sampler.json` | 106,317 | 2026-08-23 21:38:59 | `701ad291a714` | 成果面 |
| 3993 | `results/deposon_v17_fusion_fix.json` | 106,164 | 2026-08-23 21:31:41 | `af51da229652` | 成果面 |
| 3994 | `results/deposon_v17_fusion_fix_tieartifact_negativeresult.json` | 106,125 | 2026-08-23 21:31:36 | `556086d9e3bc` | 成果面 |
| 3995 | `results/deposon_v17_multigraph.json` | 16,896 | 2026-08-23 21:34:43 | `2836605ca12f` | 成果面 |
| 3996 | `results/deposon_v18_api_supplements.json` | 80,624 | 2026-08-23 23:20:04 | `62c1a41e1db8` | 成果面 |
| 3997 | `results/deposon_v19_benchmark_fixes.json` | 409,104 | 2026-08-24 01:11:01 | `910c4333eead` | 成果面 |
| 3998 | `results/deposon_v19_fullrank.json` | 42,458 | 2026-08-24 01:04:04 | `fbbfd3ef3890` | 成果面 |
| 3999 | `results/deposon_v19_meanfield.json` | 44,443 | 2026-08-24 01:02:01 | `108da40d5d4e` | 成果面 |
| 4000 | `results/deposon_v19_quickwins.json` | 7,842 | 2026-08-24 01:07:59 | `1ec7aba6afd8` | 成果面 |
| 4001 | `results/deposon_v1_implementation_calculator_2026_09_10.py` | 10,751 | 2026-09-10 22:21:56 | `121f104012f4` | 成果面 |
| 4002 | `results/deposon_v20_baselines.json` | 16,987 | 2026-08-29 01:17:30 | `6edb2aec1660` | 成果面 |
| 4003 | `results/deposon_v20_bigquiz_eval.json` | 35,718 | 2026-08-28 23:54:14 | `283dbc8c5b63` | 成果面 |
| 4004 | `results/deposon_v20_corpus_eval.json` | 631,644 | 2026-08-29 01:21:14 | `ca71aa6858e1` | 成果面 |
| 4005 | `results/deposon_v20_cot_quiz.json` | 7,101 | 2026-08-28 21:13:05 | `94fd018b5cc8` | 成果面 |
| 4006 | `results/deposon_v20_crossval.json` | 8,404 | 2026-08-28 20:27:06 | `76479b7a5ed6` | 成果面 |
| 4007 | `results/deposon_v20_familyl_ingest.json` | 1,303 | 2026-08-28 17:38:45 | `676eb83edc27` | 成果面 |
| 4008 | `results/deposon_v20_fastcheck.json` | 1,768 | 2026-08-28 22:08:40 | `a1ef105b0269` | 成果面 |
| 4009 | `results/deposon_v20_gt.json` | 3,803 | 2026-08-28 17:43:00 | `497b9c2d6746` | 成果面 |
| 4010 | `results/deposon_v20_gt2b.json` | 123,331 | 2026-08-29 19:57:39 | `a2ae7997ee67` | 成果面 |
| 4011 | `results/deposon_v20_gt3.json` | 7,844 | 2026-08-29 15:03:29 | `35b676773243` | 成果面 |
| 4012 | `results/deposon_v20_gt5.json` | 72,647 | 2026-08-29 15:35:11 | `fca14c5735dd` | 成果面 |
| 4013 | `results/deposon_v20_gt5b.json` | 56,425 | 2026-08-29 15:44:55 | `2907006dbe48` | 成果面 |
| 4014 | `results/deposon_v20_gt6.json` | 65,105 | 2026-08-29 15:45:04 | `04b90b638bdc` | 成果面 |
| 4015 | `results/deposon_v20_gt7.json` | 17,925 | 2026-08-29 17:57:57 | `896589b673ec` | 成果面 |
| 4016 | `results/deposon_v20_gt8.json` | 5,396 | 2026-08-29 19:34:34 | `2b88948dca19` | 成果面 |
| 4017 | `results/deposon_v20_gt8b.json` | 2,706 | 2026-08-30 10:28:49 | `6339ea4e500c` | 成果面 |
| 4018 | `results/deposon_v20_gt8b_ingest.json` | 986 | 2026-08-30 10:28:44 | `aa077cc1725e` | 成果面 |
| 4019 | `results/deposon_v20_gt8c.json` | 2,864 | 2026-08-30 16:17:46 | `9b16fa802ef8` | 成果面 |
| 4020 | `results/deposon_v20_gt8c_ingest.json` | 1,018 | 2026-08-30 16:17:42 | `4b11b1bd8ada` | 成果面 |
| 4021 | `results/deposon_v20_photonics.json` | 6,796 | 2026-08-29 01:19:15 | `0b7893196d0b` | 成果面 |
| 4022 | `results/deposon_v20_quiz_eval.json` | 22,623 | 2026-08-28 20:46:44 | `9194ee703218` | 成果面 |
| 4023 | `results/deposon_v20_vector_audit.json` | 915 | 2026-08-28 21:15:08 | `b9b65c568842` | 成果面 |
| 4024 | `results/deposon_v21_gtformal.json` | 69,204 | 2026-08-30 15:44:09 | `9d9ae5001c57` | 成果面 |
| 4025 | `results/deposon_v22_e95ci.json` | 1,496 | 2026-08-30 21:45:29 | `928bcfbdb7c3` | 成果面 |
| 4026 | `results/deposon_v22_p1c.json` | 763 | 2026-08-30 21:59:28 | `2bed4de3a57c` | 成果面 |
| 4027 | `results/deposon_v2_phase1_60cells_2026_09_11.json` | 85,508 | 2026-09-16 11:01:12 | `a18bbc703b42` | 成果面 |
| 4028 | `results/deposon_v2_phase3_strip_embeddings_2026_09_11.json` | 2,398,383 | 2026-09-11 11:33:43 | `1ded6731cc27` | 成果面 |
| 4029 | `results/deposon_v2_phase4_f4_2026_09_11.json` | 5,212 | 2026-09-11 11:17:21 | `cf7682348617` | 成果面 |
| 4030 | `results/deposon_v3_physical_opt_2026_09_11.json` | 17,591 | 2026-09-11 12:05:53 | `27f9bd5cc260` | 成果面 |
| 4031 | `results/deposon_v3_physical_opt_60cells_2026_09_11.json` | 17,732 | 2026-09-15 10:19:42 | `c659695aa23c` | 成果面 |
| 4032 | `results/deposon_v3_v7_summary_2026_09_11.json` | 25,049 | 2026-09-16 11:01:12 | `063ac8d00542` | 成果面 |
| 4033 | `results/deposon_v42_v2_miss_rate_curve_2026_09_16.json` | 24,435 | 2026-09-16 18:27:36 | `0a8ed127d6de` | 成果面 |
| 4034 | `results/deposon_volcengine_22caption_embedding_2026_09_10.json` | 4,559 | 2026-09-10 17:36:46 | `c4b774c8e34c` | 成果面 |
| 4035 | `results/deposon_volcengine_9model_30cells_2026_09_10.json` | 4,894 | 2026-09-16 11:01:12 | `58ab335ca341` | 成果面 |
| 4036 | `results/deposon_volcengine_glm_latest_30cells_v2_2026_09_10.json` | 32,995 | 2026-09-16 11:01:12 | `4ec04d3d7d8c` | 成果面 |
| 4037 | `results/deposon_volcengine_glm_latest_5cells_2026_09_10.json` | 4,895 | 2026-09-16 11:01:12 | `83c35597af81` | 成果面 |
| 4038 | `results/deposon_volcengine_glm_latest_5cells_2026_09_10.py` | 8,112 | 2026-09-16 11:01:12 | `a3ca05aec6fb` | 成果面 |
| 4039 | `results/deposon_volcengine_glm_latest_5cells_v2_2026_09_10.json` | 6,466 | 2026-09-16 11:01:12 | `0c3ede881fb1` | 成果面 |
| 4040 | `results/deposon_volcengine_minimax_m3_30cells_2026_09_10.json` | 23,472 | 2026-09-16 18:20:55 | `fbb7677b9cd5` | 成果面 |
| 4041 | `results/deposon_volcengine_minimax_m3_30cells_2026_09_10.py` | 11,703 | 2026-09-16 18:20:55 | `218ef1a99f97` | 成果面 |
| 4042 | `results/deposon_volcengine_seed_code_30cells_2026_09_10.json` | 23,034 | 2026-09-16 11:01:12 | `5149f5cafcf9` | 成果面 |
| 4043 | `results/deposon_volcengine_worker_a_2026_09_10.json` | 25,464 | 2026-09-16 11:01:12 | `506810017d34` | 成果面 |
| 4044 | `results/deposon_volcengine_worker_b_2026_09_10.json` | 49,338 | 2026-09-16 11:01:12 | `b1eb668377ce` | 成果面 |
| 4045 | `results/deposon_volcengine_worker_b_2026_09_10.py` | 13,232 | 2026-09-16 11:01:12 | `401dfd3c27f3` | 成果面 |
| 4046 | `results/deposon_volcengine_worker_c_2026_09_10.json` | 51,716 | 2026-09-16 11:01:12 | `f6f172820c97` | 成果面 |
| 4047 | `results/deposon_volcengine_worker_c_2026_09_10.py` | 11,692 | 2026-09-16 11:01:12 | `b5eeef1e9bd7` | 成果面 |
| 4048 | `results/deposon_volcengine_worker_d_2026_09_10.json` | 20,280 | 2026-09-16 11:01:12 | `fae79888344b` | 成果面 |
| 4049 | `results/ge01_prereg_5anchor_landing_v1.json` | 50,650 | 2026-10-16 19:56:30 | `5518346a5e61` | 成果面 |
| 4050 | `reviews/data/t1_potential.csv` | 4,833 | 2026-08-28 21:30:52 | `e110a020954f` | 成果面 |
| 4051 | `reviews/data/t1b_classics.csv` | 5,450 | 2026-08-28 21:32:04 | `82016e695f48` | 成果面 |
| 4052 | `reviews/data/t1c_loglinear.csv` | 5,566 | 2026-08-28 21:33:20 | `c50ff98a95cc` | 成果面 |
| 4053 | `reviews/data/t1d_pagerank.csv` | 4,167 | 2026-08-28 21:36:57 | `8b1a9e5113bb` | 成果面 |
| 4054 | `reviews/data/t2_linkpred.csv` | 6,750 | 2026-08-28 21:30:43 | `19555b7d9d43` | 成果面 |
| 4055 | `reviews/data/t2b_linkpred.csv` | 5,520 | 2026-08-28 21:31:15 | `6de8f0e651c4` | 成果面 |
| 4056 | `reviews/data/t2c_advlink.csv` | 6,886 | 2026-08-28 21:32:32 | `67d1d8342060` | 成果面 |
| 4057 | `reviews/data/t2d_hiding.csv` | 5,377 | 2026-08-28 21:33:27 | `5749ce2c5bf7` | 成果面 |
| 4058 | `reviews/data/t2e_nettack.csv` | 1,875 | 2026-08-28 21:35:25 | `2628f74421f2` | 成果面 |
| 4059 | `reviews/data/t2f_waniek.csv` | 1,271 | 2026-08-28 21:35:28 | `f0d2c9d2a39b` | 成果面 |
| 4060 | `reviews/data/t3_mechdesign.csv` | 6,680 | 2026-08-28 21:31:20 | `6e8b6e4730a8` | 成果面 |
| 4061 | `reviews/data/t3b_verifiable.csv` | 6,731 | 2026-08-28 21:32:32 | `f48c9f09a3b4` | 成果面 |
| 4062 | `reviews/data/t3d_llmmd.csv` | 3,405 | 2026-08-28 21:35:31 | `49028967ad57` | 成果面 |
| 4063 | `reviews/data/t3e_commit.csv` | 3,691 | 2026-08-28 21:36:14 | `bf0a2b544a74` | 成果面 |
| 4064 | `reviews/data/t4_poa.csv` | 6,567 | 2026-08-28 21:31:59 | `8ba9fada9ead` | 成果面 |
| 4065 | `reviews/design_probe_v19.md` | 13,967 | 2026-08-24 00:49:48 | `c41f1717310e` | 成果面 |
| 4066 | `reviews/experiment_design_v19.md` | 8,840 | 2026-08-24 00:35:44 | `56ecef878539` | 成果面 |
| 4067 | `reviews/independent_review_20260823.md` | 1,724 | 2026-08-23 21:40:22 | `7474fc258375` | 成果面 |
| 4068 | `reviews/literature_scan_v19.md` | 28,449 | 2026-08-24 00:40:36 | `70ea38d5b9c0` | 成果面 |
| 4069 | `reviews/post_draft_verification_v2X.md` | 9,979 | 2026-08-29 21:06:20 | `0c49f2d36088` | 成果面 |
| 4070 | `reviews/post_edit_verification_v19.md` | 19,327 | 2026-08-24 07:49:36 | `e262e9d684fe` | 成果面 |
| 4071 | `reviews/review_coach_v2X_draft_r2.md` | 15,721 | 2026-08-29 23:42:38 | `67162ab18f9a` | 成果面 |
| 4072 | `reviews/review_coach_v2X_outline.md` | 11,295 | 2026-08-29 15:34:49 | `5bebb5e1d329` | 成果面 |
| 4073 | `reviews/review_realign_v2X.md` | 7,338 | 2026-08-30 01:03:56 | `3ecb285db3d8` | 成果面 |
| 4074 | `run_benchmark_v1_3.py` | 10,690 | 2026-08-23 00:30:44 | `54ea2644df14` | 成果面 |
| 4075 | `run_benchmark_v1_4_gsm8k.py` | 11,253 | 2026-08-24 01:05:38 | `fac50b283da5` | 成果面 |
| 4076 | `run_benchmark_v1_4_strategyqa.py` | 14,537 | 2026-08-30 10:26:51 | `f523875a15db` | 成果面 |
| 4077 | `run_g2_ensemble.py` | 8,907 | 2026-08-23 09:40:07 | `e3914712a984` | 成果面 |
| 4078 | `run_v15_experiment.py` | 22,761 | 2026-08-30 04:56:14 | `58a5623f3aa1` | 成果面 |
| 4079 | `run_v16_llm_prior.py` | 13,423 | 2026-08-30 04:56:13 | `6350bbaecb81` | 成果面 |
| 4080 | `run_v17_fixed_sampler.py` | 10,435 | 2026-08-23 21:38:54 | `3e54797eedeb` | 成果面 |
| 4081 | `run_v17_fusion_fix.py` | 10,236 | 2026-08-23 21:31:25 | `b592470c47ae` | 成果面 |
| 4082 | `run_v17_multigraph.py` | 5,682 | 2026-08-23 21:33:45 | `ca7e6031272c` | 成果面 |
| 4083 | `run_v18_api_supplements.py` | 42,681 | 2026-08-23 23:19:13 | `aef28d92d763` | 成果面 |
| 4084 | `run_v19_benchmark_fixes.py` | 22,802 | 2026-08-24 01:10:53 | `674c2e5349cf` | 成果面 |
| 4085 | `run_v19_fullrank.py` | 8,976 | 2026-08-30 04:56:31 | `8d1067e4e27b` | 成果面 |
| 4086 | `run_v19_meanfield.py` | 11,690 | 2026-08-30 04:56:31 | `67ef3779478a` | 成果面 |
| 4087 | `run_v19_quickwins.py` | 10,509 | 2026-08-24 01:07:34 | `93958a96b19a` | 成果面 |
| 4088 | `run_v20_baselines.py` | 12,435 | 2026-08-29 01:14:15 | `1b9815fad7ca` | 成果面 |
| 4089 | `run_v20_bigquiz_eval.py` | 9,091 | 2026-08-28 23:54:08 | `1c1a82f4b48a` | 成果面 |
| 4090 | `run_v20_bigquiz_fetch.py` | 7,808 | 2026-08-30 10:16:33 | `f810f3a34eb2` | 成果面 |
| 4091 | `run_v20_corpus_eval.py` | 20,470 | 2026-08-28 17:41:03 | `2fad3b28d34c` | 成果面 |
| 4092 | `run_v20_cot_fetch.py` | 3,323 | 2026-08-30 10:14:35 | `b4a214c4e50f` | 成果面 |
| 4093 | `run_v20_crossval_eval.py` | 14,379 | 2026-08-28 20:26:46 | `1cdc6c37b236` | 成果面 |
| 4094 | `run_v20_crossval_fetch.py` | 4,958 | 2026-08-30 10:15:16 | `3465b43e2f8a` | 成果面 |
| 4095 | `run_v20_familyL_fetch.py` | 2,088 | 2026-08-30 10:14:03 | `ff38dbb3de7f` | 成果面 |
| 4096 | `run_v20_familyL_ingest.py` | 6,108 | 2026-08-29 01:14:15 | `c5d96c1f0522` | 成果面 |
| 4097 | `run_v20_fastcheck.py` | 7,243 | 2026-08-28 22:07:04 | `b6585a30d808` | 成果面 |
| 4098 | `run_v20_gt.py` | 9,824 | 2026-08-28 17:14:47 | `9f6df7e94cdc` | 成果面 |
| 4099 | `run_v20_gt2b.py` | 9,076 | 2026-08-29 19:57:30 | `361aff516219` | 成果面 |
| 4100 | `run_v20_gt3_eval.py` | 6,983 | 2026-08-29 15:02:33 | `6a234eee29b3` | 成果面 |
| 4101 | `run_v20_gt3_fetch.py` | 3,858 | 2026-08-30 10:11:34 | `1853f7e82a3a` | 成果面 |
| 4102 | `run_v20_gt3b_fetch.py` | 3,135 | 2026-08-30 10:12:06 | `efaa93762269` | 成果面 |
| 4103 | `run_v20_gt3c_fetch.py` | 3,193 | 2026-08-30 10:13:37 | `48b659b95984` | 成果面 |
| 4104 | `run_v20_gt5.py` | 14,957 | 2026-08-30 10:18:23 | `32c03f5739d7` | 成果面 |
| 4105 | `run_v20_gt5b.py` | 10,419 | 2026-08-30 10:19:10 | `3b344435f4ea` | 成果面 |
| 4106 | `run_v20_gt6.py` | 11,010 | 2026-08-29 15:43:45 | `c5dcdb0f12e2` | 成果面 |
| 4107 | `run_v20_gt7.py` | 17,509 | 2026-08-30 10:20:37 | `38071308e9ef` | 成果面 |
| 4108 | `run_v20_gt8.py` | 13,876 | 2026-08-29 19:33:18 | `d07233229279` | 成果面 |
| 4109 | `run_v20_gt8b_eval.py` | 9,196 | 2026-08-29 22:27:23 | `07b74332ebc2` | 成果面 |
| 4110 | `run_v20_gt8b_fetch.py` | 6,558 | 2026-08-30 10:34:04 | `fce719ad054d` | 成果面 |
| 4111 | `run_v20_gt8b_ingest.py` | 5,676 | 2026-08-29 22:24:05 | `5e3db6f4869d` | 成果面 |
| 4112 | `run_v20_gt8c_eval.py` | 9,594 | 2026-08-30 15:52:41 | `6d6db8bdbb06` | 成果面 |
| 4113 | `run_v20_gt8c_fetch.py` | 8,068 | 2026-08-30 15:51:03 | `8079a5dbe251` | 成果面 |
| 4114 | `run_v20_gt8c_ingest.py` | 5,866 | 2026-08-30 15:51:41 | `81690a38f421` | 成果面 |
| 4115 | `run_v20_photonics.py` | 7,615 | 2026-08-29 01:19:14 | `ec00cb18f95a` | 成果面 |
| 4116 | `run_v20_quizbank.py` | 8,744 | 2026-08-28 20:46:28 | `3b2a7dd2044c` | 成果面 |
| 4117 | `run_v20_vector_audit.py` | 4,717 | 2026-08-28 21:14:03 | `16a270a6bdab` | 成果面 |
| 4118 | `run_v21_gtformal.py` | 16,600 | 2026-08-30 15:35:54 | `9bbe43f41fa8` | 成果面 |
| 4119 | `run_v22_e95ci.py` | 3,058 | 2026-08-30 21:26:23 | `8470e3ce8cae` | 成果面 |
| 4120 | `run_v22_p1c.py` | 7,236 | 2026-08-30 18:28:58 | `6e9673205dc0` | 成果面 |
| 4121 | `scripts/run_deepseek_v41_30cells_v2.py` | 14,017 | 2026-09-10 16:15:10 | `c7411ae13ec0` | 成果面 |
| 4122 | `scripts/run_deepseek_v41_30cells_v3.py` | 13,955 | 2026-09-10 16:38:40 | `03bc34ea88a8` | 成果面 |
| 4123 | `scripts/run_deepseek_v41_60cells_v2_startup.py` | 16,071 | 2026-09-10 17:31:43 | `769e1d04503b` | 成果面 |
| 4124 | `scripts/run_embedding_dual_smoke.py` | 13,599 | 2026-09-10 17:03:53 | `9253225de974` | 成果面 |
| 4125 | `scripts/run_v3x_6way_stage3_recovery.py` | 15,872 | 2026-09-10 18:03:01 | `e4f96f2e9e4f` | 成果面 |
| 4126 | `scripts/run_v3x_6way_verification.py` | 25,060 | 2026-09-10 17:55:59 | `27a046d569d1` | 成果面 |
| 4127 | `scripts/run_v3x_finalize.py` | 5,932 | 2026-09-10 18:15:09 | `46787531bf8e` | 成果面 |
| 4128 | `scripts/run_v3x_stage3_minimal.py` | 12,477 | 2026-09-10 18:07:56 | `8b5d42772d5e` | 成果面 |
| 4129 | `scripts/run_v41_flash_5cells_fix.py` | 17,914 | 2026-09-10 16:54:23 | `e4546d734a53` | 成果面 |
| 4130 | `scripts/run_volcengine_seed_code_30cells.py` | 13,924 | 2026-09-16 11:01:12 | `75002485aa94` | 成果面 |
| 4131 | `svg_mindmap_ingest.py` | 8,811 | 2026-08-23 05:00:55 | `fa661fd759ed` | 成果面 |
| 4132 | `tests/test_agents_merge.py` | 26,615 | 2026-08-30 10:34:38 | `c7cc85ffb3f0` | 成果面 |
| 4133 | `tests/test_diffusion.py` | 12,463 | 2026-08-23 19:21:32 | `2452be26af7e` | 成果面 |
| 4134 | `tests/test_fast.py` | 3,653 | 2026-08-28 22:11:59 | `5829f89c2352` | 成果面 |
| 4135 | `tests/test_fingerprint_v0.py` | 13,788 | 2026-09-01 16:35:59 | `506ba4a55704` | 成果面 |
| 4136 | `tests/test_gt_common.py` | 3,697 | 2026-08-30 10:29:22 | `6a2f32d1316a` | 成果面 |
| 4137 | `tests/test_llm_fetch.py` | 11,095 | 2026-08-30 10:28:46 | `90772f5cf41b` | 成果面 |
| 4138 | `tests/test_llm_prior.py` | 7,701 | 2026-08-23 20:02:35 | `11c2ffa37610` | 成果面 |
| 4139 | `tests/test_new_modes.py` | 21,275 | 2026-08-23 09:40:33 | `0b2276028391` | 成果面 |
| 4140 | `tests/test_protocol.py` | 6,979 | 2026-08-30 04:58:18 | `f103c9d87c61` | 成果面 |
| 4141 | `tests/test_v18.py` | 17,093 | 2026-08-23 23:15:42 | `c523ae4b0989` | 成果面 |
| 4142 | `tests/test_v19.py` | 6,056 | 2026-08-24 01:10:27 | `b44e2945fa31` | 成果面 |
| 4143 | `tests/test_v19_benchmark.py` | 7,371 | 2026-08-24 01:12:52 | `f343754f380c` | 成果面 |
| 4144 | `tests/test_v20.py` | 13,249 | 2026-08-28 17:19:09 | `e4712875f65d` | 成果面 |
| 4145 | `tests/test_v20_gt2b.py` | 4,318 | 2026-08-29 19:58:34 | `4cd18ae1d3dc` | 成果面 |
| 4146 | `tests/test_v20_gt5.py` | 5,746 | 2026-08-29 15:36:51 | `1f104b13a170` | 成果面 |
| 4147 | `tests/test_v20_gt5b.py` | 2,423 | 2026-08-29 15:44:42 | `81feb1f137b4` | 成果面 |
| 4148 | `tests/test_v20_gt6.py` | 2,584 | 2026-08-29 15:44:43 | `5c7dd774a3f3` | 成果面 |
| 4149 | `tests/test_v20_gt7.py` | 6,489 | 2026-08-29 17:56:48 | `e8727f8f42da` | 成果面 |
| 4150 | `tests/test_v20_gt8.py` | 5,122 | 2026-08-29 19:34:11 | `b9479374de4d` | 成果面 |
| 4151 | `tests/test_v20_gt8b.py` | 10,109 | 2026-08-29 22:27:24 | `3c4395df9311` | 成果面 |
| 4152 | `tests/test_v20_gt8c.py` | 13,458 | 2026-08-30 15:55:13 | `562dd8b920bc` | 成果面 |
| 4153 | `tests/test_v21_gtformal.py` | 7,376 | 2026-08-30 15:20:33 | `74650b1d603b` | 成果面 |
| 4154 | `tests/test_v22_p1c.py` | 3,854 | 2026-08-30 18:30:56 | `b19bdb965cc0` | 成果面 |
| 4155 | `tools/__pycache__/distortion_calculator.cpython-314.pyc` | 62,806 | 2026-10-17 23:55:51 | `79d8dc801d51` | 成果面 |
| 4156 | `tools/__pycache__/exp_harness.cpython-314.pyc` | 44,064 | 2026-10-17 23:30:50 | `0a53046bc52d` | 成果面 |
| 4157 | `tools/__pycache__/llm_client.cpython-314.pyc` | 11,727 | 2026-10-15 09:09:36 | `24392cb19f75` | 成果面 |
| 4158 | `tools/_archive_purge_2026_10_17/__pycache__/recycle_channel.cpython-314.pyc` | 5,826 | 2026-10-17 12:21:32 | `adb62c08ca79` | 成果面 |
| 4159 | `tools/_archive_purge_2026_10_17/inventory_compare.json` | 98,697 | 2026-10-17 12:20:15 | `1b9eee6810b4` | 成果面 |
| 4160 | `tools/_archive_purge_2026_10_17/inventory_compare.py` | 4,365 | 2026-10-17 12:20:06 | `7c09c04d53cf` | 成果面 |
| 4161 | `tools/_archive_purge_2026_10_17/recycle_channel.py` | 3,540 | 2026-10-17 12:21:13 | `06619281cd09` | 成果面 |
| 4162 | `tools/_archive_purge_2026_10_17/step2_recheck.py` | 2,656 | 2026-10-17 12:22:09 | `a2e324411df7` | 成果面 |
| 4163 | `tools/_archive_purge_2026_10_17/step2_sample.py` | 4,613 | 2026-10-17 12:21:47 | `54daf47662a2` | 成果面 |
| 4164 | `tools/_archive_purge_2026_10_17/step2_sample_verify.json` | 2,028 | 2026-10-17 12:22:17 | `46e72777f74e` | 成果面 |
| 4165 | `tools/_archive_purge_2026_10_17/step2_sample_verify_rejudge.json` | 397 | 2026-10-17 12:22:17 | `d32809934409` | 成果面 |
| 4166 | `tools/_archive_purge_2026_10_17/step3_bulk_purge.py` | 7,780 | 2026-10-17 12:22:31 | `90523fef8e09` | 成果面 |
| 4167 | `tools/_archive_purge_2026_10_17/step3_bulk_result.json` | 374,277 | 2026-10-17 12:23:20 | `3601cc490af7` | 成果面 |
| 4168 | `tools/_archive_purge_2026_10_17/step4_bin_audit.json` | 8,102 | 2026-10-17 12:23:54 | `89da5036d061` | 成果面 |
| 4169 | `tools/_archive_purge_2026_10_17/step4_bin_audit.py` | 2,442 | 2026-10-17 12:23:48 | `e8e5333144ec` | 成果面 |
| 4170 | `tools/_archive_purge_2026_10_17/step5_register.py` | 17,778 | 2026-10-17 12:26:36 | `cbb6539394a8` | 成果面 |
| 4171 | `tools/_archive_purge_2026_10_17/step5_register_result.json` | 210 | 2026-10-17 12:30:12 | `c6788de2a588` | 成果面 |
| 4172 | `tools/distortion_calculator.py` | 50,896 | 2026-10-17 23:55:07 | `ae7ff6e0bac5` | 成果面 |
| 4173 | `tools/exp_harness.py` | 45,548 | 2026-10-17 23:29:15 | `27cb200220e0` | 成果面 |
| 4174 | `tools/llm_client.py` | 8,118 | 2026-09-09 16:16:02 | `1722500da4aa` | 成果面 |
| 4175 | `tools/make_figures_v2.py` | 21,073 | 2026-08-30 20:52:09 | `0dc3ea09f42d` | 成果面 |
| 4176 | `tools/make_figures_v2_en.py` | 21,188 | 2026-08-30 20:46:55 | `b4e880a6af33` | 成果面 |
| 4177 | `tools/read_key.py` | 1,047 | 2026-09-10 14:45:46 | `a9b56c4e775f` | 成果面 |
| 4178 | `verifier/_build_partial.py` | 7,160 | 2026-09-16 11:01:12 | `04fcd95c70f1` | 成果面 |
| 4179 | `verifier/_read_summary.py` | 1,231 | 2026-09-10 20:50:17 | `b4d89f052875` | 成果面 |
| 4180 | `verifier/_run.log` | 7,190 | 2026-09-10 21:03:13 | `e148d7bf11e1` | 成果面 |
| 4181 | `verifier/_test_one.py` | 2,564 | 2026-09-16 11:01:12 | `893641fd9e25` | 成果面 |
| 4182 | `verifier/_worker_a_run.log` | 4,532 | 2026-09-10 21:29:39 | `9df22377dc55` | 成果面 |
| 4183 | `verifier/audit/__pycache__/conservation.cpython-314.pyc` | 27,641 | 2026-10-13 22:10:04 | `e969ad69a634` | 成果面 |
| 4184 | `verifier/audit/conservation.py` | 22,105 | 2026-09-10 09:29:22 | `4bdec2683f06` | 成果面 |
| 4185 | `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | 6,680 | 2026-09-09 13:19:32 | `03c6c01f3697` | 成果面 |
| 4186 | `verifier/handoff/KT_ABC1_anchors_sha256_12.root_session_11318B.bak_2026_09_23.json` | 11,318 | 2026-09-22 11:02:01 | `6e9cd8cd8e07` | 成果面 |
| 4187 | `verifier/handoff/P_F_PREDECISION_2026_09_11_V0.1.json` | 12,498 | 2026-09-11 13:08:54 | `312d635e6259` | 成果面 |
| 4188 | `verifier/kill_lines/kt_b1_kill_decision.py` | 2,781 | 2026-09-09 13:17:24 | `9f351078e5bf` | 成果面 |
| 4189 | `verifier/run_volcengine_9model_30cells.py` | 12,050 | 2026-09-16 11:01:12 | `54f8033cfb29` | 成果面 |
| 4190 | `verifier/runs/2026-09-04_pd_v0.jsonl` | 100 | 2026-09-04 13:33:46 | `5042869bdf85` | 成果面 |
| 4191 | `verifier/runs/20260823.log` | 1,197 | 2026-08-23 20:24:15 | `f8d8db6a4d8b` | 成果面 |
| 4192 | `verifier/runs/v10_run1.md` | 701 | 2026-08-24 07:51:43 | `54be4344e99a` | 成果面 |
| 4193 | `verifier/runs/v11_run1.md` | 514 | 2026-08-28 17:57:42 | `bd36f361ea12` | 成果面 |
| 4194 | `verifier/runs/v12_run1.md` | 788 | 2026-08-28 20:01:49 | `927eafcb3b0b` | 成果面 |
| 4195 | `verifier/runs/v13_run1.md` | 145 | 2026-08-28 20:30:14 | `aa1456d217fc` | 成果面 |
| 4196 | `verifier/runs/v14_run1.md` | 145 | 2026-08-28 20:48:36 | `3fdca6c35dcb` | 成果面 |
| 4197 | `verifier/runs/v15_run1.md` | 475 | 2026-08-28 21:17:49 | `634ef5fa4ef8` | 成果面 |
| 4198 | `verifier/runs/v16_run1.md` | 359 | 2026-08-28 21:54:50 | `e6bf3b753ff6` | 成果面 |
| 4199 | `verifier/runs/v17_run1.md` | 283 | 2026-08-28 22:51:36 | `9d0332c44044` | 成果面 |
| 4200 | `verifier/runs/v18_run1.md` | 276 | 2026-08-28 23:57:39 | `4a3ce944cce3` | 成果面 |
| 4201 | `verifier/runs/v19_run1.md` | 297 | 2026-08-29 00:25:02 | `7b95dbd3f168` | 成果面 |
| 4202 | `verifier/runs/v20_run1.md` | 295 | 2026-08-29 00:35:08 | `41d3d7f4a148` | 成果面 |
| 4203 | `verifier/runs/v21_run1.md` | 247 | 2026-08-29 01:26:03 | `36b69e195f06` | 成果面 |
| 4204 | `verifier/runs/v21_run2.md` | 448 | 2026-08-29 11:35:00 | `3246c7d46480` | 成果面 |
| 4205 | `verifier/runs/v22_run1.md` | 436 | 2026-08-29 11:22:52 | `582531ccd67d` | 成果面 |
| 4206 | `verifier/runs/v23_run1.md` | 586 | 2026-08-29 15:09:59 | `9578066064cc` | 成果面 |
| 4207 | `verifier/runs/v24_run1.md` | 498 | 2026-08-29 15:50:05 | `67fd4fec19f2` | 成果面 |
| 4208 | `verifier/runs/v25_run1.md` | 526 | 2026-08-29 18:00:55 | `b81e2fb0ea28` | 成果面 |
| 4209 | `verifier/runs/v26_run1.md` | 546 | 2026-08-29 19:39:05 | `09b69c05bb47` | 成果面 |
| 4210 | `verifier/runs/v27_run1.md` | 559 | 2026-08-29 20:02:00 | `0759457758be` | 成果面 |
| 4211 | `verifier/runs/v27_run2.md` | 554 | 2026-08-29 20:03:11 | `82a92d9ce191` | 成果面 |
| 4212 | `verifier/runs/v28_run1.md` | 771 | 2026-08-29 21:09:29 | `6d85472d724c` | 成果面 |
| 4213 | `verifier/runs/v29_run1.md` | 440 | 2026-08-29 23:03:33 | `26a667edec7a` | 成果面 |
| 4214 | `verifier/runs/v29_run2.md` | 627 | 2026-08-29 23:05:27 | `badd1ed95a6d` | 成果面 |
| 4215 | `verifier/runs/v30_run1.md` | 735 | 2026-08-29 23:47:50 | `cef68a7a30a5` | 成果面 |
| 4216 | `verifier/runs/v30_run2.md` | 787 | 2026-08-29 23:49:54 | `d22151b9ad6d` | 成果面 |
| 4217 | `verifier/runs/v30_run3.md` | 771 | 2026-08-29 23:51:37 | `0dc553ed64c2` | 成果面 |
| 4218 | `verifier/runs/v31_run1.md` | 673 | 2026-08-30 01:08:22 | `dcb11fefabf2` | 成果面 |
| 4219 | `verifier/runs/v31_run2.md` | 747 | 2026-08-30 01:10:29 | `8727c88269f3` | 成果面 |
| 4220 | `verifier/runs/v32_run1.md` | 859 | 2026-08-30 03:57:46 | `1798c48acea7` | 成果面 |
| 4221 | `verifier/runs/v32_run2.md` | 894 | 2026-08-30 03:59:13 | `83c987fb96d9` | 成果面 |
| 4222 | `verifier/runs/v32_run3.md` | 886 | 2026-08-30 04:06:01 | `4a99a1134c8c` | 成果面 |
| 4223 | `verifier/runs/v33_run1.md` | 2,160 | 2026-08-30 05:05:50 | `9e917334781c` | 成果面 |
| 4224 | `verifier/runs/v33_run2.md` | 1,783 | 2026-08-30 05:12:50 | `158948a53671` | 成果面 |
| 4225 | `verifier/runs/v34_run1.md` | 83 | 2026-08-30 09:57:16 | `03f773f08fa7` | 成果面 |
| 4226 | `verifier/runs/v34_run2.md` | 118 | 2026-08-30 14:13:30 | `d9bfaae6d08b` | 成果面 |
| 4227 | `verifier/runs/v35_run1.md` | 39 | 2026-08-30 15:47:20 | `a693c838ae57` | 成果面 |
| 4228 | `verifier/runs/v35_run2.md` | 118 | 2026-08-30 17:08:56 | `11ce6990b84a` | 成果面 |
| 4229 | `verifier/runs/v36_runs.log` | 106 | 2026-09-17 23:20:46 | `18668f3d7d58` | 成果面 |
| 4230 | `verifier/runs/v37_runs.log` | 124 | 2026-09-17 23:20:46 | `f0de3de22eae` | 成果面 |
| 4231 | `verifier/runs/v38_runs.log` | 271 | 2026-09-17 23:20:47 | `0fc3395dac12` | 成果面 |
| 4232 | `verifier/runs/v39_runs.log` | 173 | 2026-09-17 23:20:48 | `73b035b4fc3c` | 成果面 |
| 4233 | `verifier/runs/v40_runs.log` | 133 | 2026-09-17 23:20:48 | `0e511b4e6caa` | 成果面 |
| 4234 | `verifier/runs/v41_2026-08-30_run1.txt` | 158 | 2026-09-17 23:20:49 | `e156e87caba8` | 成果面 |
| 4235 | `verifier/runs/v42_2026-08-30_run1.txt` | 279 | 2026-09-17 23:20:49 | `8fde2819ef29` | 成果面 |
| 4236 | `verifier/runs/v42_2026-08-30_run2.txt` | 156 | 2026-09-17 23:20:50 | `1aa0257caac9` | 成果面 |
| 4237 | `verifier/runs/v43_2026-09-01_run1.txt` | 199 | 2026-09-17 23:20:51 | `aa82005b05de` | 成果面 |
| 4238 | `verifier/v1/check.py` | 2,976 | 2026-08-23 10:27:37 | `03bc1adfc82f` | 成果面 |
| 4239 | `verifier/v10/check.py` | 5,261 | 2026-08-24 07:15:04 | `4fd5fdd754c0` | 成果面 |
| 4240 | `verifier/v11/check.py` | 2,767 | 2026-08-28 17:56:50 | `3b8682a7e562` | 成果面 |
| 4241 | `verifier/v12/check.py` | 4,142 | 2026-08-29 01:14:15 | `87c9c883e3bf` | 成果面 |
| 4242 | `verifier/v13/check.py` | 3,495 | 2026-08-28 20:29:43 | `1159facab6db` | 成果面 |
| 4243 | `verifier/v14/check.py` | 3,278 | 2026-08-28 20:48:03 | `4ba223d2185d` | 成果面 |
| 4244 | `verifier/v15/check.py` | 3,231 | 2026-08-28 21:17:37 | `be0f2bbab0a2` | 成果面 |
| 4245 | `verifier/v16/check.py` | 2,691 | 2026-08-28 21:54:41 | `223082632a1d` | 成果面 |
| 4246 | `verifier/v17/check.py` | 2,897 | 2026-08-28 22:51:15 | `679792be51ed` | 成果面 |
| 4247 | `verifier/v17/erratum.md` | 438 | 2026-08-29 01:26:03 | `50f15f7ea3dc` | 成果面 |
| 4248 | `verifier/v18/check.py` | 3,180 | 2026-08-29 01:14:16 | `6abdda4f7400` | 成果面 |
| 4249 | `verifier/v19/check.py` | 1,995 | 2026-08-29 00:24:42 | `c53cf72d085b` | 成果面 |
| 4250 | `verifier/v2/check.py` | 2,510 | 2026-08-23 19:21:32 | `af3a78983537` | 成果面 |
| 4251 | `verifier/v20/check.py` | 2,790 | 2026-08-29 00:33:07 | `9d0f1e950dee` | 成果面 |
| 4252 | `verifier/v20/erratum.md` | 316 | 2026-08-29 01:26:03 | `35081d39f35b` | 成果面 |
| 4253 | `verifier/v21/check.py` | 3,702 | 2026-08-29 01:23:52 | `5e7d7435c4a3` | 成果面 |
| 4254 | `verifier/v22/check.py` | 2,857 | 2026-08-29 11:20:44 | `f16beaae5675` | 成果面 |
| 4255 | `verifier/v23/check.py` | 2,659 | 2026-08-29 15:08:00 | `9ecb25362c9a` | 成果面 |
| 4256 | `verifier/v24/check.py` | 3,124 | 2026-08-29 15:49:47 | `e6c7513d54f3` | 成果面 |
| 4257 | `verifier/v25/check.py` | 2,576 | 2026-08-29 18:00:10 | `cc6ff5453e06` | 成果面 |
| 4258 | `verifier/v26/check.py` | 2,595 | 2026-09-16 11:01:12 | `c58a9652a42a` | 成果面 |
| 4259 | `verifier/v27/check.py` | 2,132 | 2026-09-16 11:01:12 | `118524c7e808` | 成果面 |
| 4260 | `verifier/v28/check.py` | 2,201 | 2026-09-16 11:01:12 | `b73a6b268f64` | 成果面 |
| 4261 | `verifier/v29/check.py` | 2,124 | 2026-09-16 11:01:12 | `5923e2c379f6` | 成果面 |
| 4262 | `verifier/v3/check.py` | 2,544 | 2026-08-23 19:21:32 | `02a5a86d38bf` | 成果面 |
| 4263 | `verifier/v30/check.py` | 2,565 | 2026-09-16 11:01:12 | `2cf46f79a669` | 成果面 |
| 4264 | `verifier/v31/check.py` | 2,185 | 2026-09-16 11:01:12 | `e5bb0020e500` | 成果面 |
| 4265 | `verifier/v32/check.py` | 2,551 | 2026-09-16 11:01:12 | `399bfc743f24` | 成果面 |
| 4266 | `verifier/v33/check.py` | 6,019 | 2026-08-30 05:11:44 | `32fefc485326` | 成果面 |
| 4267 | `verifier/v34/check.py` | 3,715 | 2026-08-30 09:57:03 | `0bbd226cd2ae` | 成果面 |
| 4268 | `verifier/v35/check.py` | 2,385 | 2026-08-30 15:47:20 | `2130a5f5e1bf` | 成果面 |
| 4269 | `verifier/v36/check.sh` | 968 | 2026-09-18 13:43:52 | `2212dcd98cd1` | 成果面 |
| 4270 | `verifier/v37/check.sh` | 1,141 | 2026-09-18 13:43:52 | `ced43b5f8800` | 成果面 |
| 4271 | `verifier/v38/check.sh` | 1,705 | 2026-09-17 23:20:52 | `43b501c5c20d` | 成果面 |
| 4272 | `verifier/v39/check.sh` | 1,935 | 2026-09-17 23:20:53 | `d48ac555761f` | 成果面 |
| 4273 | `verifier/v4/check.py` | 3,205 | 2026-08-23 19:33:47 | `f058e85c5383` | 成果面 |
| 4274 | `verifier/v40/check.sh` | 1,604 | 2026-09-17 23:20:54 | `7b15cd2f4c7e` | 成果面 |
| 4275 | `verifier/v41/check.sh` | 1,687 | 2026-09-17 23:20:54 | `2c9fe869daaa` | 成果面 |
| 4276 | `verifier/v42/check.sh` | 1,509 | 2026-09-17 23:20:55 | `3ea87e2cfc61` | 成果面 |
| 4277 | `verifier/v43/check.sh` | 1,224 | 2026-09-17 23:20:55 | `71b83217032d` | 成果面 |
| 4278 | `verifier/v5/check.py` | 2,255 | 2026-08-23 20:04:44 | `3d776381f665` | 成果面 |
| 4279 | `verifier/v6/check.py` | 2,757 | 2026-08-23 20:23:46 | `8366078a10e4` | 成果面 |
| 4280 | `verifier/v7/check.py` | 4,300 | 2026-08-23 21:03:13 | `a70a68037d92` | 成果面 |
| 4281 | `verifier/v8/check.py` | 3,210 | 2026-08-23 21:40:59 | `01b63b1a9c5f` | 成果面 |
| 4282 | `verifier/v9/check.py` | 5,352 | 2026-08-23 23:46:50 | `5faad917d839` | 成果面 |

### §4.2 区 `D:\私人资料\deposon-sub`（1,276 件 ／ 60,166,418 bytes）

📌 **图例 `†`**：该件系 ③段-R2 **由 repo 净转移**而来（**141** 件）——**本表所列路径为准**，其原 repo 路径见 **§3.3** 对应行。

**逐目录分布**

| 目录 | 件数 | bytes | 类别 |
|:--|--:|--:|:--|
| `.trae/audit/` | 4 | 22,819 | 成果面 |
| `.trae/audit/compile_evidence/` | 3 | 4,856 | 成果面 |
| `.trae/audit/compile_evidence/v1_62refs_20260908/` | 2 | 1,724 | 成果面 |
| `.trae/audit/compile_evidence/v2_overfull_fix_20260909/` | 2 | 3,909 | 成果面 |
| `.trae/audit/compile_evidence/v2pre_h1h3_20260909/` | 2 | 3,163 | 成果面 |
| `.trae/deliverables/` | 3 | 3,297,981 | 成果面 |
| `.trae/scripts/` | 2 | 56,382 | 成果面 |
| `_archive_deposon_2026_09_17/verifier/audit/` | 1 | 22,105 | 成果面 |
| `deposon_team/_designs/` | 11 | 114,291 | 成果面 |
| `deposon_team/plugins/` | 41 | 357,250 | 成果面 |
| `deposon_team/products/` | 2 | 35,285 | 成果面 |
| `deposon_team/verifier/` | 3 | 20,012 | 成果面 |
| `docs/` | 20 | 181,276 | 成果面 |
| `docs/FTFB_EXTERNAL_REVIEW_R2_2026_09_17/` | 3 | 63,039 | 成果面 |
| `docs/reviews/` | 3 | 22,570 | 成果面 |
| `docs/V3X/` | 70 | 940,730 | 成果面 |
| `results/` | 919 | 50,192,960 | 成果面 |
| `results/_archive_2026_09_18/` | 8 | 58,748 | 成果面 |
| `results/_archive_2026_09_20/` | 62 | 2,244,324 | 成果面 |
| `results/_archive_2026_09_21/` | 7 | 789,949 | 成果面 |
| `results/_archive_2026_09_24/` | 8 | 167,029 | 成果面 |
| `results/_p_j_convergence_basin_2026_09_16/` | 1 | 1,669 | 成果面 |
| `results/_r5_spec_pack_retrieved_2026_10_13/` | 1 | 1,037 | 成果面 |
| `reviews/` | 8 | 184,835 | 成果面 |
| `tmp_movedout_2026_09_28/` | 8 | 41,738 | 成果面 |
| `tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/` | 8 | 277,915 | 成果面 |
| `tmp_movedout_2026_10_01/` | 1 | 66,339 | 成果面 |
| `tmp_movedout_2026_10_01/legacy_caliber/` | 1 | 3,756 | 成果面 |
| `tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/` | 10 | 30,711 | 成果面 |
| `tmp_movedout_2026_10_01/process_scripts/v4_wt_2026_09_27/` | 1 | 4,950 | 成果面 |
| `tmp_movedout_2026_10_01/process_scripts/v5_wa_2026_09_30/` | 4 | 15,844 | 成果面 |
| `tmp_movedout_2026_10_09/uncertain_release_2026_09/` | 14 | 226,545 | 成果面 |
| `verifier/` | 1 | 14,360 | 成果面 |
| `verifier/handoff/` | 3 | 16,525 | 成果面 |
| `verifier/kill_lines/` | 2 | 35,391 | 成果面 |
| `verifier/runs/` | 9 | 7,409 | 成果面 |
| `（根散件）/` | 28 | 636,992 | 成果面 |

**逐件（1,276 件）**

| # | 相对路径 | bytes | mtime | SHA-12 | 类别 |
| --: | :-- | --: | :-- | :-- | :-: |
| 1 | `.trae/audit/compare_versions.py` | 7,958 | 2026-09-09 14:14:27 | `03e22a91bc0c` | 成果面 |
| 2 | `.trae/audit/compile_evidence/compile_runner.ps1` | 2,022 | 2026-09-08 22:46:03 | `1fc5f3ab3f93` | 成果面 |
| 3 | `.trae/audit/compile_evidence/COMPILE_SUMMARY.txt` | 1,693 | 2026-09-09 01:40:36 | `1bad41b3929f` | 成果面 |
| 4 | `.trae/audit/compile_evidence/extract_tars.py` | 1,141 | 2026-09-08 22:50:11 | `befdd577adce` | 成果面 |
| 5 | `.trae/audit/compile_evidence/v1_62refs_20260908/compile_runner.ps1` | 1,469 | 2026-09-08 21:23:13 | `51d29cb72b68` | 成果面 |
| 6 | `.trae/audit/compile_evidence/v1_62refs_20260908/COMPILE_SUMMARY.txt` | 255 | 2026-09-08 21:32:11 | `967ae49b3d5f` | 成果面 |
| 7 | `.trae/audit/compile_evidence/v2_overfull_fix_20260909/compile_runner.ps1` | 2,022 | 2026-09-08 22:46:03 | `1fc5f3ab3f93` | 成果面 |
| 8 | `.trae/audit/compile_evidence/v2_overfull_fix_20260909/COMPILE_SUMMARY.txt` | 1,887 | 2026-09-20 17:11:14 | `fe6f9872a2fe` | 成果面 |
| 9 | `.trae/audit/compile_evidence/v2pre_h1h3_20260909/compile_runner.ps1` | 2,022 | 2026-09-08 22:46:03 | `1fc5f3ab3f93` | 成果面 |
| 10 | `.trae/audit/compile_evidence/v2pre_h1h3_20260909/extract_tars.py` | 1,141 | 2026-09-08 22:50:11 | `befdd577adce` | 成果面 |
| 11 | `.trae/audit/identify_dedicated.py` | 3,806 | 2026-09-09 14:14:27 | `3feb84107c02` | 成果面 |
| 12 | `.trae/audit/inspect_current_tars.py` | 2,501 | 2026-09-09 14:14:27 | `291877043221` | 成果面 |
| 13 | `.trae/audit/rebuild_trae_home.py` | 8,554 | 2026-09-09 14:14:27 | `7bd38b8e70d4` | 成果面 |
| 14 | `.trae/deliverables/deposon_arxiv_cn.tar.gz` | 1,659,286 | 2026-09-09 14:14:27 | `9d7351e73652` | 成果面 |
| 15 | `.trae/deliverables/deposon_arxiv_en.tar.gz` | 1,637,413 | 2026-09-09 14:14:26 | `d95be2a05990` | 成果面 |
| 16 | `.trae/deliverables/MANIFEST.sha256.txt` | 1,282 | 2026-09-20 17:11:14 | `3ab185e6c047` | 成果面 |
| 17 | `.trae/scripts/_md_to_tex.py` | 48,627 | 2026-09-09 14:14:27 | `f55da6fe7aea` | 成果面 |
| 18 | `.trae/scripts/_split_packages.py` | 7,755 | 2026-09-09 14:14:27 | `872530d93a7f` | 成果面 |
| 19 | `_archive_deposon_2026_09_17/verifier/audit/conservation.py` | 22,105 | 2026-10-13 00:16:42 | `4bdec2683f06` | 成果面 |
| 20 | `_check_conv_archive.ps1` | 2,326 | 2026-09-26 17:24:02 | `c89d46c47026` | 成果面 |
| 21 | `_list_teamo_models.py` | 1,273 | 2026-09-17 15:43:28 | `c51f3d2005fe` | 成果面 |
| 22 | `_merge_or_stub_overlap_table_v3_2026_09_17.py` | 5,050 | 2026-09-18 13:48:18 | `300daa32f7be` | 成果面 |
| 23 | `_movedout_manifest_2026_09_21.json` | 291,551 | 2026-09-21 19:38:44 | `d1ee21f3f6ae` | 成果面 |
| 24 | `_movedout_manifest_2026_09_28.json` | 2,003 | 2026-09-28 18:27:21 | `6b557f005a40` | 成果面 |
| 25 | `_p_l_v3_phase1_finalize_2026_09_17.py` | 19,226 | 2026-09-17 13:35:21 | `cf8fd1178ab1` | 成果面 |
| 26 | `_p_l_v3_phase1_runner_2026_09_17.py` | 35,425 | 2026-09-18 13:48:18 | `d5e74a98c44b` | 成果面 |
| 27 | `_p_l_v3_phase2_closedsource_finalize_2026_09_17.py` | 14,700 | 2026-09-17 17:55:22 | `20f038a7a8dd` | 成果面 |
| 28 | `_p_l_v3_phase2_closedsource_runner_2026_09_17.py` | 28,344 | 2026-09-18 13:48:18 | `e6005733ca7c` | 成果面 |
| 29 | `_p_l_v3_phase2_closedsource_runner_v2_2026_09_17.py` | 26,716 | 2026-09-18 13:48:18 | `090d34377c9d` | 成果面 |
| 30 | `_p_l_v3_phase2_finalize_2026_09_17.py` | 19,901 | 2026-09-17 14:27:39 | `eaa04c5713d6` | 成果面 |
| 31 | `_p_l_v3_phase2_glm53_only_2026_09_17.py` | 12,604 | 2026-09-18 13:48:18 | `c88608c7a26b` | 成果面 |
| 32 | `_p_l_v3_phase2_or_embedding_2026_09_17.py` | 26,300 | 2026-09-18 13:43:27 | `e7353ffbb94f` | 成果面 |
| 33 | `_p_l_v3_phase2_or_embedding_v3_2026_09_17.py` | 27,863 | 2026-09-18 13:43:27 | `5edc460b35d3` | 成果面 |
| 34 | `_p_l_v3_phase2_runner_2026_09_17.py` | 21,868 | 2026-09-18 13:48:18 | `ac780b206cae` | 成果面 |
| 35 | `_p_l_v3_phase2_vector_emb_2026_09_17.py` | 3,810 | 2026-09-17 14:32:45 | `f5e51b83541a` | 成果面 |
| 36 | `_p_l_v3_phase2_vector_emb_doubao_2026_09_17.py` | 37,263 | 2026-09-17 15:56:35 | `b0a59c92a3e6` | 成果面 |
| 37 | `_print_sha_2026_09_17.py` | 1,227 | 2026-09-17 14:35:20 | `51d33faa22b9` | 成果面 |
| 38 | `_show_teamo_ownedby.py` | 1,342 | 2026-09-17 15:43:49 | `3c8175c35d82` | 成果面 |
| 39 | `_test_3bb_vary.py` | 3,541 | 2026-09-17 15:59:00 | `a7046b2dd65e` | 成果面 |
| 40 | `_test_gpt56sol_real.py` | 2,060 | 2026-09-17 15:57:09 | `19a48c278183` | 成果面 |
| 41 | `_tmp_degen.py` | 719 | 2026-09-26 18:33:39 | `88004f338e9c` | 成果面 |
| 42 | `_tmp_v1_recompute.py` | 9,819 | 2026-09-26 18:30:48 | `86a6407a7bd6` | 成果面 |
| 43 | `_tmp_v2_redesign.py` | 13,762 | 2026-09-26 18:31:50 | `4cd07b3a7dea` | 成果面 |
| 44 | `_tmp_verify.py` | 384 | 2026-09-26 18:37:04 | `e93a9cb16b08` | 成果面 |
| 45 | `_v4_l6_s38v2_verify_2026_09_24.py` | 3,729 | 2026-09-24 11:36:45 | `c665860f459a` | 成果面 |
| 46 | `deposon_team/_designs/D7_PRE_DISPATCH_EXECUTION_REPORT_2026_09_16.md` | 12,667 | 2026-09-16 13:03:05 | `3fbc7f4dfd22` | 成果面 |
| 47 | `deposon_team/_designs/DELEGATION_CONFIGS_FOR_USER_B_2026_09_16.md` | 12,844 | 2026-09-16 22:27:49 | `23bb7d39bf58` | 成果面 |
| 48 | `deposon_team/_designs/EXTERNAL_AGENT_PROMPTS_2026_09_16.md` | 12,326 | 2026-09-16 17:50:08 | `6a7b0c20a133` | 成果面 |
| 49 | `deposon_team/_designs/V3X_CLOSURE_REPORT_REQUIREMENTS_FOR_EXTERNAL_AGENT.md` | 8,714 | 2026-09-16 11:34:05 | `2185433b1f32` | 成果面 |
| 50 | `deposon_team/_designs/v3x_dispatch_log_2026_09_16.md` | 8,429 | 2026-09-16 12:56:39 | `85c3a5cfd84d` | 成果面 |
| 51 | `deposon_team/_designs/V3X_FULL_CLOSEOUT_REPORT_2026_09_16.md` | 12,878 | 2026-09-16 22:48:32 | `95925a562597` | 成果面 |
| 52 | `deposon_team/_designs/V3X_GAME_THEORY_NON_EUCLIDEAN_MASTER_NARRATIVE_2026_09_16.py` | 9,244 | 2026-09-16 11:32:56 | `7f6563d22ce7` | 成果面 |
| 53 | `deposon_team/_designs/V3X_KIMI_7_DIRECTIONS_FULL_ACCEPT_2026_09_16.md` | 10,936 | 2026-09-16 13:18:48 | `eecbe2b1341d` | 成果面 |
| 54 | `deposon_team/_designs/V3X_PATCH_5ANCHOR_RECONCILE_2026_09_16.md` | 8,222 | 2026-09-16 23:30:08 | `27db4950f710` | 成果面 |
| 55 | `deposon_team/_designs/V3X_PATCH_5ANCHOR_RECONCILE_V2_2026_09_17.md` | 6,799 | 2026-09-17 14:29:33 | `c41c1d6aa794` | 成果面 |
| 56 | `deposon_team/_designs/V3X_TEAM_IMPROVEMENT_PLAN_2026_09_16.md` | 11,232 | 2026-09-16 12:46:23 | `11cd57800bd6` | 成果面 |
| 57 | `deposon_team/plugins/_audit_minimax_extract_2026_09_16.py` | 4,364 | 2026-09-16 18:19:05 | `da1c38940b6c` | 成果面 |
| 58 | `deposon_team/plugins/_audit_v3_runners_2026_09_16.py` | 3,145 | 2026-09-16 18:50:08 | `b490f695841c` | 成果面 |
| 59 | `deposon_team/plugins/_build_minimax_artifact_2026_09_16.py` | 7,361 | 2026-09-16 18:11:02 | `d0d188c60a62` | 成果面 |
| 60 | `deposon_team/plugins/_d7_5anchor_60cells_2026_09_18.py` | 10,049 | 2026-09-16 18:54:48 | `568d30cf6d92` | 成果面 |
| 61 | `deposon_team/plugins/_d7_post_anchor_rotation_remediation_2026_09_16.py` | 6,241 | 2026-09-16 18:54:48 | `821fd0b19eb3` | 成果面 |
| 62 | `deposon_team/plugins/_d7_post_anchor_rotation_remediation_2026_09_18.py` | 9,152 | 2026-09-16 18:54:48 | `b0a450752a97` | 成果面 |
| 63 | `deposon_team/plugins/_fix_adendum_c_erratum_2026_09_17.py` | 1,820 | 2026-09-17 19:14:52 | `eb44de412de5` | 成果面 |
| 64 | `deposon_team/plugins/_fix_minimax_extract_2026_09_16.py` | 5,103 | 2026-09-16 18:20:37 | `8a722b0a4aea` | 成果面 |
| 65 | `deposon_team/plugins/_fix_v3_selfcheck_2026_09_16.py` | 7,401 | 2026-09-16 18:57:57 | `b9a414293ebe` | 成果面 |
| 66 | `deposon_team/plugins/_goal_completion_audit_2026_09_17.py` | 3,752 | 2026-09-17 19:17:07 | `5c18b72e7bb3` | 成果面 |
| 67 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_09_16.py` | 18,596 | 2026-09-16 18:54:48 | `d2cd7acb29a1` | 成果面 |
| 68 | `deposon_team/plugins/_p_i_real_labels_runner_2026_09_16.py` | 7,055 | 2026-09-16 22:10:49 | `8678e5083b41` | 成果面 |
| 69 | `deposon_team/plugins/_p_j_convergence_basin_runner_2026_09_16.py` | 9,143 | 2026-09-16 18:56:48 | `877b9415a217` | 成果面 |
| 70 | `deposon_team/plugins/_p_k_blind_test_runner_2026_09_16.py` | 19,031 | 2026-09-16 18:54:48 | `70e34edc0926` | 成果面 |
| 71 | `deposon_team/plugins/_p_l_p_c_finite_size_scaling_runner_2026_09_16.py` | 9,177 | 2026-09-16 20:57:27 | `bca06b3cc2f7` | 成果面 |
| 72 | `deposon_team/plugins/_p_l_real_data_collapse_runner_2026_09_16.py` | 5,663 | 2026-09-16 22:14:44 | `daff134b8e0b` | 成果面 |
| 73 | `deposon_team/plugins/_p_l_real_data_collapse_runner_2026_09_16_v2.py` | 5,778 | 2026-09-16 22:40:44 | `ed9d066f3ea3` | 成果面 |
| 74 | `deposon_team/plugins/_p_m_attack_surface_cost_runner_2026_09_16.py` | 10,622 | 2026-09-16 18:56:48 | `9e054e93982b` | 成果面 |
| 75 | `deposon_team/plugins/_p_m_real_separation_runner_2026_09_16.py` | 7,316 | 2026-09-16 22:11:02 | `d5133ecca740` | 成果面 |
| 76 | `deposon_team/plugins/_p_n_curvature_potential_coupling_runner_2026_09_16.py` | 9,473 | 2026-09-16 18:56:48 | `7355795bbc67` | 成果面 |
| 77 | `deposon_team/plugins/_p_o_stranger_verification_runner_2026_09_16.py` | 13,230 | 2026-09-16 18:56:48 | `d1bc564264ef` | 成果面 |
| 78 | `deposon_team/plugins/_transfer_2026_09_15.ps1` | 2,485 | 2026-09-15 15:47:26 | `4b724f65286a` | 成果面 |
| 79 | `deposon_team/plugins/_transfer_2026_09_15.py` | 2,253 | 2026-09-15 15:48:06 | `0f98b38169dd` | 成果面 |
| 80 | `deposon_team/plugins/_v3x_18frozen_remeasure_2026_09_16.py` | 5,216 | 2026-09-16 23:31:54 | `94686cf517f4` | 成果面 |
| 81 | `deposon_team/plugins/_v3x_experiments_runner_2026_09_16.py` | 18,555 | 2026-09-16 18:54:48 | `0fac09bec7c4` | 成果面 |
| 82 | `deposon_team/plugins/_v3x_p_k_verify_2026_09_16.py` | 5,373 | 2026-09-16 23:32:50 | `e516675e3db5` | 成果面 |
| 83 | `deposon_team/plugins/_v42_v2_runner_2026_09_16.py` | 22,460 | 2026-09-16 18:54:48 | `cf8a1f5fd383` | 成果面 |
| 84 | `deposon_team/plugins/attack_pc_a1_resampling.py` | 4,834 | 2026-09-15 15:08:22 | `b3ff941c9b9e` | 成果面 |
| 85 | `deposon_team/plugins/attack_pc_a2_fitting.py` | 4,502 | 2026-09-15 15:08:22 | `1861aecfbfe2` | 成果面 |
| 86 | `deposon_team/plugins/attack_pc_a3_clipping.py` | 4,469 | 2026-09-15 15:08:22 | `3a62ad10abf7` | 成果面 |
| 87 | `deposon_team/plugins/fix_boss_naming_2026_09_16.py` | 17,479 | 2026-09-15 15:07:35 | `21ad055e7e06` | 成果面 |
| 88 | `deposon_team/plugins/fix_proactive_audit_2026_09_16.py` | 15,444 | 2026-09-15 15:17:54 | `f5704c9b4497` | 成果面 |
| 89 | `deposon_team/plugins/fix_risk1_02940_boundary.py` | 7,125 | 2026-09-15 10:21:12 | `1017671173cb` | 成果面 |
| 90 | `deposon_team/plugins/fix_risk2_canonical5.py` | 8,871 | 2026-09-15 10:21:09 | `cbdbfa029f70` | 成果面 |
| 91 | `deposon_team/plugins/fix_risk3_s_eff_normalization.py` | 13,429 | 2026-09-15 10:22:00 | `ba347f5d9982` | 成果面 |
| 92 | `deposon_team/plugins/fix_selfcheck_bug_n1_2026_09_15.py` | 4,680 | 2026-09-15 15:37:39 | `fb571653df6c` | 成果面 |
| 93 | `deposon_team/plugins/fix_selfcheck_bug_n2_2026_09_15.py` | 3,412 | 2026-09-15 15:37:39 | `eba2d444f4da` | 成果面 |
| 94 | `deposon_team/plugins/fix_selfcheck_bug_n3_2026_09_15.py` | 5,134 | 2026-09-15 15:37:39 | `47fc588b3cae` | 成果面 |
| 95 | `deposon_team/plugins/fix_verify_freeze_policy_2026_09_16.py` | 7,122 | 2026-09-15 15:08:52 | `fa521fe37da0` | 成果面 |
| 96 | `deposon_team/plugins/git_commit_msg_2026_09_18.txt` | 3,223 | 2026-09-15 15:16:26 | `b2841d12a444` | 成果面 |
| 97 | `deposon_team/plugins/runner_pa_d1_d3.py` | 27,712 | 2026-09-15 15:15:39 | `1b9578eadc14` | 成果面 |
| 98 | `deposon_team/products/kimi_artifact_v_2026_09_16.json` | 9,938 | 2026-09-16 18:39:55 | `1f8612344592` | 成果面 |
| 99 | `deposon_team/products/minimax_artifact_v_2026_09_16.json` | 25,347 | 2026-09-16 18:20:56 | `9e1ccbdceacc` | 成果面 |
| 100 | `deposon_team/verifier/v42_v2_2026_09_16.py` | 17,363 | 2026-09-16 18:23:39 | `c5598b13c139` | 成果面 |
| 101 | `deposon_team/verifier/v42_v2_baseline_2026_09_16.json` | 1,879 | 2026-09-16 18:25:53 | `483602856618` | 成果面 |
| 102 | `deposon_team/verifier/v42_v2_runs_2026_09_16.jsonl` | 770 | 2026-09-16 18:25:53 | `b471190e579c` | 成果面 |
| 103 | `Deposon_凝子_统一场论报告_一致性核对_20260907.md` | 3,441 | 2026-09-20 17:11:14 | `125998731621` | 成果面 |
| 104 | `docs/ADVISOR_BRIEFING_2026-08-30.md` | 5,890 | 2026-08-29 10:16:17 | `40278bc425e6` | 成果面 †141 |
| 105 | `docs/ARCH_AUDIT_v2.md` | 14,698 | 2026-08-30 04:39:28 | `5bee4c6cf47c` | 成果面 †141 |
| 106 | `docs/DATASET_HEALTH_v2.md` | 4,892 | 2026-08-30 04:40:23 | `c87a0c1f5af6` | 成果面 †141 |
| 107 | `docs/Deposon_Requirements_v1.md` | 13,914 | 2026-08-22 21:07:01 | `ee33f3f22e1b` | 成果面 †141 |
| 108 | `docs/Deposon_v1_3_验证报告.md` | 8,003 | 2026-08-22 21:07:01 | `dc5be727f920` | 成果面 †141 |
| 109 | `docs/Deposon_v1_4_验证报告.md` | 4,254 | 2026-08-22 21:11:43 | `3bcccf03f7ca` | 成果面 †141 |
| 110 | `docs/FIGURES_v2.md` | 5,851 | 2026-08-30 11:15:47 | `1cd4a4cb0a76` | 成果面 †141 |
| 111 | `docs/FTFB_EXTERNAL_REVIEW_R2_2026_09_17/META_REVIEW_REPORT_2026_09_17.md` | 12,218 | 2026-09-17 12:27:09 | `0fda737a2203` | 成果面 |
| 112 | `docs/FTFB_EXTERNAL_REVIEW_R2_2026_09_17/REVIEW_RB1.md` | 22,982 | 2026-09-17 12:26:13 | `3594378e7d1d` | 成果面 |
| 113 | `docs/FTFB_EXTERNAL_REVIEW_R2_2026_09_17/REVIEW_RB2.md` | 27,839 | 2026-09-17 12:26:13 | `d8eafdd67119` | 成果面 |
| 114 | `docs/LESSONS_INDEX.md` | 4,682 | 2026-08-29 10:11:09 | `7e3674a80cb7` | 成果面 †141 |
| 115 | `docs/LESSONS_v19.md` | 5,290 | 2026-08-28 17:56:50 | `dbbcf8e5e89d` | 成果面 †141 |
| 116 | `docs/LESSONS_v20_deepprobe.md` | 8,409 | 2026-08-29 10:06:48 | `5c898d4407ee` | 成果面 †141 |
| 117 | `docs/MODEL_ARGUMENTATION_v2.md` | 30,142 | 2026-08-30 10:42:40 | `2c83c42804e4` | 成果面 †141 |
| 118 | `docs/PROGRESS_REPORT_LAYMAN.md` | 8,472 | 2026-08-29 15:08:52 | `25546ffdc56b` | 成果面 †141 |
| 119 | `docs/reviews/review_gtformal_integration_v2X.md` | 8,582 | 2026-08-30 16:58:11 | `325c9d87787b` | 成果面 †141 |
| 120 | `docs/reviews/review_salvage_integration_v2X.md` | 6,212 | 2026-08-30 05:06:19 | `96ae50306f36` | 成果面 †141 |
| 121 | `docs/reviews/review_sprint_v2X.md` | 7,776 | 2026-08-30 11:11:11 | `4356cd02562e` | 成果面 †141 |
| 122 | `docs/Roadmap_v2X.md` | 6,467 | 2026-08-24 11:13:19 | `a6aaf3200611` | 成果面 †141 |
| 123 | `docs/SALVAGE_v2.md` | 7,312 | 2026-08-30 04:41:52 | `f28a81d6302d` | 成果面 †141 |
| 124 | `docs/SECURITY_AUDIT_v2.md` | 4,707 | 2026-08-30 04:39:49 | `317fb508940a` | 成果面 †141 |
| 125 | `docs/SPEC_GT2C.md` | 3,172 | 2026-08-30 18:32:55 | `29af533486b2` | 成果面 †141 |
| 126 | `docs/SPEC_GT5C.md` | 3,046 | 2026-08-30 18:33:30 | `1e41b4334735` | 成果面 †141 |
| 127 | `docs/SPEC_v1.5.md` | 6,204 | 2026-08-23 19:22:13 | `c165a86cf551` | 成果面 †141 |
| 128 | `docs/THINKING_V3_GT_CONTRIB_2026.md` | 19,508 | 2026-08-30 20:45:01 | `8c1d733f9182` | 成果面 †141 |
| 129 | `docs/V3X/AGENT_TEAM_OPT_V2_2026_09_11.md` | 11,835 | 2026-09-11 16:30:03 | `bbd074b76526` | 成果面 †141 |
| 130 | `docs/V3X/BOSS_B123_BUGFIX_2026_09_09.md` | 5,615 | 2026-09-09 14:50:57 | `9352a1675b10` | 成果面 †141 |
| 131 | `docs/V3X/BOSS_F_GHOST_PATH_NOTE_2026_09_11.md` | 4,840 | 2026-09-11 13:16:07 | `354a1360234f` | 成果面 †141 |
| 132 | `docs/V3X/BOSS_PE_3_RESERVOIR_VERIFY_REPORT_2026_09_15.md` | 11,079 | 2026-09-15 13:36:08 | `c28f7f0b530f` | 成果面 †141 |
| 133 | `docs/V3X/BOSS_SELFTEST_PHASE_B_2026_09_09.md` | 15,478 | 2026-09-09 14:18:07 | `4485443757e7` | 成果面 †141 |
| 134 | `docs/V3X/BOSS_URL_2026_09_11.md` | 7,135 | 2026-09-11 13:01:49 | `1ba7419178a1` | 成果面 †141 |
| 135 | `docs/V3X/BOSS_URL_DUE_DILIGENCE_2026_09_11.md` | 10,970 | 2026-09-11 12:11:02 | `0fb588bb0c2e` | 成果面 †141 |
| 136 | `docs/V3X/BPA_PILOT_2026_09_09_mavis.md` | 6,864 | 2026-09-09 13:39:22 | `d74e1534493e` | 成果面 †141 |
| 137 | `docs/V3X/CANONICAL_5_UNVERIFIED_NOTE_2026_09_11.md` | 6,804 | 2026-09-11 13:30:46 | `b049140e130c` | 成果面 †141 |
| 138 | `docs/V3X/CPATH_SIMULATION_REPORT_2026_09_10.md` | 6,825 | 2026-09-10 20:47:18 | `de772cd9e7ba` | 成果面 †141 |
| 139 | `docs/V3X/D0_FREEZE_PREP_2026_09_09.md` | 9,844 | 2026-09-09 10:55:24 | `0d1e88c258aa` | 成果面 †141 |
| 140 | `docs/V3X/D3_〔IM〕_MIDTERM_TEMPLATE.md` | 4,361 | 2026-09-09 11:23:41 | `574d5a79e363` | 成果面 †141 |
| 141 | `docs/V3X/D5_DECISIONS_LAND_REPORT_2026_09_15.md` | 21,756 | 2026-09-15 15:15:39 | `8ff1a7c5413f` | 成果面 †141 |
| 142 | `docs/V3X/D7_GITHUB_PUSH_RECEIVE_2026_09_15_v2.md` | 5,930 | 2026-09-15 17:28:16 | `2c4bb6078ee7` | 成果面 †141 |
| 143 | `docs/V3X/D7_ONE_PAGE_SUMMARY_2026_09_11_v5.md` | 6,459 | 2026-09-11 13:30:46 | `67063f9cb238` | 成果面 †141 |
| 144 | `docs/V3X/D7_ONE_PAGE_SUMMARY_TEMPLATE.md` | 5,830 | 2026-09-09 11:00:34 | `87563a63b854` | 成果面 †141 |
| 145 | `docs/V3X/D7_POST_CLEANUP_PLAN_2026_09_18.json` | 20,271 | 2026-09-15 17:27:45 | `0b8a1a357aae` | 成果面 †141 |
| 146 | `docs/V3X/D7_POST_CLEANUP_REPORT_2026_09_16.json` | 1,248 | 2026-09-16 11:01:13 | `40955bf2abc5` | 成果面 †141 |
| 147 | `docs/V3X/D7_PRE_V3_POLISH_AND_TEAM_IMPROVEMENT_2026_09_16.md` | 10,692 | 2026-09-16 11:09:18 | `51869e3184f4` | 成果面 †141 |
| 148 | `docs/V3X/D7_WANG_TEACHER_〔IM〕_PUSH_REQUIREMENTS_2026_09_18.md` | 8,037 | 2026-09-16 11:08:22 | `935cb6ee3566` | 成果面 †141 |
| 149 | `docs/V3X/D_FIX2_METRIC_VERIFY_REPORT_2026_09_15.md` | 7,352 | 2026-09-15 14:07:47 | `0a63824f0805` | 成果面 †141 |
| 150 | `docs/V3X/DEPOSON_EMBEDDING_6WAY_THEORY_V0_2026_09_10.md` | 22,442 | 2026-09-10 20:22:54 | `ac8997b07731` | 成果面 †141 |
| 151 | `docs/V3X/DEPOSON_EMBEDDING_6WAY_VERIFICATION_2026_09_10.md` | 17,803 | 2026-09-10 18:16:43 | `240a7ae4bdfb` | 成果面 †141 |
| 152 | `docs/V3X/DPATH_CROSS_MODAL_2026_09_10.md` | 26,460 | 2026-09-16 11:01:12 | `e4ee3999f7ce` | 成果面 †141 |
| 153 | `docs/V3X/KT_A1_SPEC_V0.1.md` | 29,570 | 2026-09-09 13:42:23 | `78b71d404366` | 成果面 †141 |
| 154 | `docs/V3X/KT_B1_SPEC_V0.1.md` | 39,206 | 2026-09-30 20:36:32 | `0397b757362f` | 成果面 †141 |
| 155 | `docs/V3X/KT_C1_REPORT_PHASE_B_2026_09_09.md` | 8,753 | 2026-09-09 14:17:30 | `825337b10a2d` | 成果面 †141 |
| 156 | `docs/V3X/KT_C1_SPEC_V0.1.md` | 31,241 | 2026-09-09 13:42:23 | `59d8f56347d5` | 成果面 †141 |
| 157 | `docs/V3X/KT_D0_EVIDENCE_CARD.md` | 6,354 | 2026-09-09 10:59:38 | `75b2f3b38c2a` | 成果面 †141 |
| 158 | `docs/V3X/KT_D0_SPEC_V0.1.md` | 20,927 | 2026-09-09 13:42:24 | `cce8e9a1b00e` | 成果面 †141 |
| 159 | `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` | 10,351 | 2026-09-09 10:05:24 | `bd1caab42b4c` | 成果面 †141 |
| 160 | `docs/V3X/P_C_P_E_V0_1_VERIFICATION_2026_09_12.md` | 3,899 | 2026-09-11 13:01:11 | `ee043a13f801` | 成果面 †141 |
| 161 | `docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md` | 6,301 | 2026-09-08 16:03:54 | `d427b2f57c33` | 成果面 †141 |
| 162 | `docs/V3X/P_C_V0_1_VERIFICATION_2026_09_12.md` | 4,885 | 2026-09-11 13:00:18 | `00c7b7ceccdc` | 成果面 †141 |
| 163 | `docs/V3X/P_D_B3_MERKLE_22_CAPTION_VERIFICATION_2026_09_16.md` | 10,979 | 2026-09-16 18:26:46 | `7f1492fbe657` | 成果面 †141 |
| 164 | `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC_CHANGELOG.md` | 15,021 | 2026-09-17 15:16:40 | `fc73cab85d8f` | 成果面 †141 |
| 165 | `docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md` | 34,367 | 2026-10-01 09:51:11 | `c13449101ab3` | 成果面 †141 |
| 166 | `docs/V3X/P_D_FINGERPRINT_V0_SPEC.md` | 9,192 | 2026-09-04 13:11:41 | `3b67461b05fe` | 成果面 †141 |
| 167 | `docs/V3X/P_E_D1_D3_REPORT_2026_09_15.md` | 13,109 | 2026-09-15 11:27:04 | `900da300d11e` | 成果面 †141 |
| 168 | `docs/V3X/P_F_D1_FULL_REPORT_2026_09_15.md` | 15,985 | 2026-09-15 12:15:12 | `817efdc2f0ad` | 成果面 †141 |
| 169 | `docs/V3X/P_F_D1_REPORT_2026_09_15.md` | 12,608 | 2026-09-16 11:01:12 | `e47d0348922e` | 成果面 †141 |
| 170 | `docs/V3X/P_F_IMPLEMENTATION_2026_09_11.md` | 22,973 | 2026-09-16 11:01:12 | `edd048eaa721` | 成果面 †141 |
| 171 | `docs/V3X/P_F_RESEARCH_2026_09_09.md` | 17,603 | 2026-09-09 13:49:14 | `98085df7811a` | 成果面 †141 |
| 172 | `docs/V3X/P_F_SPEC_V0.md` | 19,804 | 2026-09-09 13:50:05 | `de90faf362c5` | 成果面 †141 |
| 173 | `docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md` | 6,375 | 2026-09-11 12:15:55 | `b10fae0da66d` | 成果面 †141 |
| 174 | `docs/V3X/P_F_V0_1_VERIFICATION_2026_09_12.md` | 4,188 | 2026-09-11 13:09:27 | `4d970e9c0aec` | 成果面 †141 |
| 175 | `docs/V3X/P_G_V01_REPORT_2026_09_15.md` | 15,479 | 2026-09-15 12:06:17 | `9a6b08d03e0c` | 成果面 †141 |
| 176 | `docs/V3X/PHASE_B_DELIVERY_2026_09_09.md` | 9,701 | 2026-09-09 14:19:28 | `ba53d73e3937` | 成果面 †141 |
| 177 | `docs/V3X/QUICK_KILL_6_DIRECTIONS.md` | 15,085 | 2026-09-09 09:53:43 | `a476f241edb2` | 成果面 †141 |
| 178 | `docs/V3X/REVIEWER_A_STATIC_AUDIT_2026_09_15.md` | 34,647 | 2026-09-15 14:22:04 | `575572872e9a` | 成果面 †141 |
| 179 | `docs/V3X/REVIEWER_A_TRAE_FIX_AUDIT_2026_09_15.md` | 20,698 | 2026-09-15 15:29:00 | `195373c094d6` | 成果面 †141 |
| 180 | `docs/V3X/REVIEWER_A_TRAE_N123_AUDIT_2026_09_15.md` | 17,151 | 2026-09-15 15:59:57 | `33ee7266cf5b` | 成果面 †141 |
| 181 | `docs/V3X/REVIEWER_B_AUDIT_PHASE_B_2026_09_09.md` | 14,835 | 2026-09-09 14:17:07 | `5e99e79f2e11` | 成果面 †141 |
| 182 | `docs/V3X/REVIEWER_B_TRAE_FIX_RERUN_2026_09_15.md` | 16,278 | 2026-09-15 15:28:54 | `f5ac9820310a` | 成果面 †141 |
| 183 | `docs/V3X/REVIEWER_B_TRAE_N123_RERUN_2026_09_15.md` | 16,926 | 2026-09-15 15:57:55 | `31c27c0117a6` | 成果面 †141 |
| 184 | `docs/V3X/RISK3_V0_FIXES_2026_09_11.md` | 13,271 | 2026-09-11 17:17:36 | `c00d1c22e7ed` | 成果面 †141 |
| 185 | `docs/V3X/SPEC_V0_1_BOSS_SELFTEST_2026_09_09.md` | 10,708 | 2026-09-09 14:18:34 | `00e543564e3f` | 成果面 †141 |
| 186 | `docs/V3X/TRAE_3RISK_FIX_REPORT_2026_09_16.md` | 9,267 | 2026-09-15 15:10:00 | `7478959cfc7d` | 成果面 †141 |
| 187 | `docs/V3X/TRAE_PL_V2_EXPERIMENT_PROPOSAL_2026_09_17.md` | 8,849 | 2026-09-17 11:12:54 | `4020b1809780` | 成果面 †141 |
| 188 | `docs/V3X/TRAE_PROACTIVE_AUDIT_REPORT_2026_09_16.md` | 6,493 | 2026-09-15 15:18:50 | `813b34dcac70` | 成果面 †141 |
| 189 | `docs/V3X/TRAE_SELFCHECK_FIX_REPORT_2026_09_15.md` | 4,840 | 2026-09-15 15:39:00 | `226f740aa120` | 成果面 †141 |
| 190 | `docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md` | 8,526 | 2026-09-16 11:03:10 | `4ffb21bb6bfa` | 成果面 †141 |
| 191 | `docs/V3X/V3X_D6_PAPER_V2_2026_09_09_mavis.md` | 24,778 | 2026-09-09 13:41:07 | `4d06d34cb6fa` | 成果面 †141 |
| 192 | `docs/V3X/V3X_D6_PAPER_zh.md` | 19,716 | 2026-09-09 11:34:06 | `feae8af2fefe` | 成果面 †141 |
| 193 | `docs/V3X/V3X_DAILY_KILL_V2_PLAN.md` | 15,327 | 2026-09-09 11:39:34 | `37e97e1e7b7f` | 成果面 †141 |
| 194 | `docs/V3X/V3X_FULL_EXPERIMENT_DESIGN_2026_09_16.md` | 22,427 | 2026-09-16 12:28:47 | `3d847f9f3151` | 成果面 †141 |
| 195 | `docs/V3X/V3X_PROJECT_EVOLUTION_FOR_KIMI.md` | 12,908 | 2026-09-15 14:55:11 | `4de2cbf57a49` | 成果面 †141 |
| 196 | `docs/V3X/V42_V2_REMEDIATION_CLAUSE_2026_09_16.md` | 4,775 | 2026-09-16 18:33:04 | `e451a5a3d079` | 成果面 †141 |
| 197 | `docs/V3X/V42_V2_VERIFIER_PERFORMANCE_REPORT_2026_09_16.md` | 11,080 | 2026-09-16 18:33:19 | `914053fc3e17` | 成果面 †141 |
| 198 | `docs/V3X/V7_§3_P_C_P_E_GRAY_NOTE_2026_09_11.md` | 7,344 | 2026-09-11 13:15:52 | `f80cc4e1fb7f` | 成果面 †141 |
| 199 | `docs/V3X_COLLAB_DIRECTIONS.md` | 16,363 | 2026-08-31 09:32:54 | `5a27c2350036` | 成果面 †141 |
| 200 | `results/_149_face_effect_disposal_2026_10_10.md` | 24,295 | 2026-10-10 01:15:42 | `e7c1232df138` | 成果面 |
| 201 | `results/_9model_merge_disposition_register_2026_10_09.md` | 11,651 | 2026-10-09 12:09:24 | `455277298212` | 成果面 |
| 202 | `results/_a02_excluded_items_idx_collection_2026_10_10.md` | 39,565 | 2026-10-10 18:40:34 | `03407e0b6662` | 成果面 |
| 203 | `results/_adendum_A_degradation_precheck_20260917_132049.json` | 4,248 | 2026-09-17 13:20:50 | `38fabeb19691` | 成果面 |
| 204 | `results/_adendum_B_pi_real_labels_v2_20260917_133726.json` | 2,374 | 2026-09-17 13:37:29 | `3d344711cf8c` | 成果面 |
| 205 | `results/_adendum_B_pi_real_labels_v2_20260917_133852.json` | 2,374 | 2026-09-17 13:38:55 | `c725e08e0a1c` | 成果面 |
| 206 | `results/_adendum_C_pm_attack_surface_v2_20260917_133726.json` | 4,123 | 2026-09-17 19:15:01 | `193ba7d66412` | 成果面 |
| 207 | `results/_adendum_C_pm_attack_surface_v2_20260917_133852.json` | 4,122 | 2026-09-17 19:15:01 | `6eba63788ca8` | 成果面 |
| 208 | `results/_adendum_D_pc_r2_per_model_v2_20260917_133726.json` | 4,605 | 2026-09-17 13:37:29 | `6fe706750823` | 成果面 |
| 209 | `results/_adendum_D_pc_r2_per_model_v2_20260917_133852.json` | 4,605 | 2026-09-17 13:38:55 | `d66792eea40e` | 成果面 |
| 210 | `results/_adendum_E_pd_supplement_v2_20260917_133726.json` | 1,353 | 2026-09-17 13:37:29 | `2c4790ffb6e3` | 成果面 |
| 211 | `results/_adendum_E_pd_supplement_v2_20260917_133852.json` | 1,353 | 2026-09-17 13:38:55 | `46d8dacb4721` | 成果面 |
| 212 | `results/_adendum_F_pe_3modal_closure_llm_dispatch_20260917_132143.json` | 3,646 | 2026-09-17 13:21:43 | `879494ed8fb9` | 成果面 |
| 213 | `results/_adendum_F_pe_3modal_v2_20260917_143033.json` | 38,622 | 2026-09-17 14:30:34 | `afab79249be7` | 成果面 |
| 214 | `results/_adendum_FGK_complete_20260917_143033.md` | 14,005 | 2026-09-17 14:31:34 | `958188c83cf0` | 成果面 |
| 215 | `results/_adendum_G_pf_dfix2_timing_converge_llm_dispatch_20260917_132143.json` | 2,757 | 2026-09-17 13:21:43 | `d10462080832` | 成果面 |
| 216 | `results/_adendum_G_pf_dfix2_v2_20260917_143033.json` | 95,292 | 2026-09-17 14:30:34 | `bf8db2ad255b` | 成果面 |
| 217 | `results/_adendum_H_pg_dhde_shrink_20260917_132049.json` | 4,613 | 2026-09-17 13:20:50 | `b9a0253ba6a0` | 成果面 |
| 218 | `results/_adendum_I_po_captions_closure_20260917_132049.json` | 4,429 | 2026-09-17 13:20:50 | `18165008bef6` | 成果面 |
| 219 | `results/_adendum_J_warehouse_spearman_health_20260917_132049.json` | 11,337 | 2026-09-17 13:20:50 | `df661d62426a` | 成果面 |
| 220 | `results/_adendum_K_087_cluster_cross_backbone_llm_dispatch_20260917_132143.json` | 2,911 | 2026-09-17 13:21:43 | `acdf933f68e0` | 成果面 |
| 221 | `results/_adendum_K_qwen3_087_cluster_v2_20260917_143033.json` | 32,481 | 2026-09-17 14:30:34 | `43477c8ea2d6` | 成果面 |
| 222 | `results/_adendum_L_verifier_dual_impl_diff_20260917_132049.json` | 2,783 | 2026-09-17 13:20:50 | `1532607ded80` | 成果面 |
| 223 | `results/_adendum_M_pj_convergence_basin_v2_20260917_133726.json` | 3,694 | 2026-09-17 13:37:29 | `ea7ffda97e20` | 成果面 |
| 224 | `results/_adendum_M_pj_convergence_basin_v2_20260917_133852.json` | 3,686 | 2026-09-17 13:38:55 | `8ab01a1e42ae` | 成果面 |
| 225 | `results/_adendum_N_pn_coupling_v2_20260917_133726.json` | 2,012 | 2026-09-17 13:37:29 | `1b91cc25ca57` | 成果面 |
| 226 | `results/_adendum_N_pn_coupling_v2_20260917_133852.json` | 2,011 | 2026-09-17 13:38:55 | `a32f3c8ba520` | 成果面 |
| 227 | `results/_adendum_O_pk_v2_three_way_v2_20260917_133726.json` | 1,971 | 2026-09-17 13:37:29 | `725fd7b961f8` | 成果面 |
| 228 | `results/_adendum_O_pk_v2_three_way_v2_20260917_133852.json` | 1,970 | 2026-09-17 13:38:55 | `a30ff093305d` | 成果面 |
| 229 | `results/_adendum_P_pc_two_phase_fail_h0_20260917_132049.json` | 2,456 | 2026-09-17 13:20:50 | `6b26daddc92c` | 成果面 |
| 230 | `results/_adendum_Q_deepseek_v4_pro_anchor_20260917_132049.json` | 4,003 | 2026-09-17 13:20:50 | `ab5d9ae6e42a` | 成果面 |
| 231 | `results/_af_entity_definition_draft_2026_10_10.md` | 25,257 | 2026-10-10 13:24:57 | `97654060d86e` | 成果面 |
| 232 | `results/_agent_trio_redesign_draft_2026_09_23.md` | 10,026 | 2026-09-23 16:11:18 | `e4320f20cad4` | 成果面 |
| 233 | `results/_alt_delib_pkg3_two_judgments_2026_10_10.md` | 38,032 | 2026-10-10 01:06:09 | `3f52709a48e8` | 成果面 |
| 234 | `results/_archive_2026_09_18/_trae_5audit_aggregated_2026_09_17.md` | 11,465 | 2026-09-17 21:28:25 | `43265e4bf2be` | 成果面 |
| 235 | `results/_archive_2026_09_18/_trae_anchor_18_audit_20260917_193000.md` | 3,449 | 2026-09-17 19:13:39 | `4af67e6cbe71` | 成果面 |
| 236 | `results/_archive_2026_09_18/_trae_code_improvement_v2_2026_09_18.md` | 20,938 | 2026-09-18 12:09:43 | `e151e48ab4b4` | 成果面 |
| 237 | `results/_archive_2026_09_18/_trae_corpus_5_audit_20260917_193000.md` | 3,467 | 2026-09-17 19:13:14 | `f2a655cd5e54` | 成果面 |
| 238 | `results/_archive_2026_09_18/_trae_d7_v1_audit_20260917_190000.json` | 4,253 | 2026-09-17 19:14:38 | `3184b30b7b0d` | 成果面 |
| 239 | `results/_archive_2026_09_18/_trae_d7_v1_audit_20260917_190000.md` | 7,855 | 2026-09-17 19:12:14 | `e240ca712be6` | 成果面 |
| 240 | `results/_archive_2026_09_18/_trae_kimi_push_v3_audit_20260917_193000.md` | 3,281 | 2026-09-17 19:12:38 | `8ece24be6b8a` | 成果面 |
| 241 | `results/_archive_2026_09_18/_trae_paper_8ch_双审_20260917_200000.md` | 4,040 | 2026-09-17 19:14:10 | `bec666969ffc` | 成果面 |
| 242 | `results/_archive_2026_09_20/_archive_manifest_2026_09_18.json` | 4,712 | 2026-09-18 22:04:18 | `a729875c0c67` | 成果面 |
| 243 | `results/_archive_2026_09_20/_archive_manifest_2026_09_20.json` | 35,682 | 2026-09-20 11:07:34 | `4dd89950bf11` | 成果面 |
| 244 | `results/_archive_2026_09_20/_audit_secret_2026_09_20_anchor_guard.py` | 6,433 | 2026-09-20 09:53:50 | `19b4174f6339` | 成果面 |
| 245 | `results/_archive_2026_09_20/_coze_paper_v1_双审报告_2026_09_17.md` | 85,573 | 2026-09-18 13:45:13 | `c3de25e6df57` | 成果面 |
| 246 | `results/_archive_2026_09_20/_coze_〔IM〕_v3_d7format_2026_09_18.pdf` | 454,307 | 2026-09-18 21:31:20 | `adc99e04ac53` | 成果面 |
| 247 | `results/_archive_2026_09_20/_d05_main_runner_2026_09_18.py` | 41,446 | 2026-09-18 10:07:57 | `f3d4ec483599` | 成果面 |
| 248 | `results/_archive_2026_09_20/_d05_md_report_only_2026_09_18.py` | 13,694 | 2026-09-18 10:16:44 | `7a5be4aef9ac` | 成果面 |
| 249 | `results/_archive_2026_09_20/_d05_sanity_3backbone_20260918.log` | 2,088 | 2026-10-12 12:49:03 | `41bea33b9492` | 成果面 |
| 250 | `results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json` | 2,292 | 2026-09-24 19:21:31 | `0a1e91d6f772` | 成果面 |
| 251 | `results/_archive_2026_09_20/_d05_sanity_3backbone_2026_09_18.py` | 5,458 | 2026-09-18 10:00:35 | `a29291a60956` | 成果面 |
| 252 | `results/_archive_2026_09_20/_d05_verify_sha_2026_09_18.py` | 2,938 | 2026-09-18 12:41:58 | `0b7e50a8a036` | 成果面 |
| 253 | `results/_archive_2026_09_20/_deposon_v2scripts_reverify_worker_2026_09_18.py` | 34,134 | 2026-09-18 13:42:18 | `18984b04c45e` | 成果面 |
| 254 | `results/_archive_2026_09_20/_final_sha_2026_09_18.py` | 2,678 | 2026-09-18 13:48:37 | `0769f60a0504` | 成果面 |
| 255 | `results/_archive_2026_09_20/_fix_batch2_2026_09_18.py` | 4,100 | 2026-09-18 13:43:14 | `81bb1751be4c` | 成果面 |
| 256 | `results/_archive_2026_09_20/_fix_batch3_2026_09_18.py` | 3,207 | 2026-09-18 13:44:20 | `01e63e488ce2` | 成果面 |
| 257 | `results/_archive_2026_09_20/_fix_batch4_2026_09_18.py` | 8,225 | 2026-09-18 13:44:58 | `2efcd5ff42f1` | 成果面 |
| 258 | `results/_archive_2026_09_20/_fix_batch6_2026_09_18.py` | 2,214 | 2026-09-18 13:46:45 | `1c59e7b803fe` | 成果面 |
| 259 | `results/_archive_2026_09_20/_fix_batch7_2026_09_18.py` | 4,261 | 2026-09-18 13:47:59 | `389283c51275` | 成果面 |
| 260 | `results/_archive_2026_09_20/_fix_batch8_2026_09_18.py` | 2,249 | 2026-09-18 13:49:57 | `5057ccf97d6b` | 成果面 |
| 261 | `results/_archive_2026_09_20/_fix_d05_rescue_2026_09_18.py` | 3,524 | 2026-09-18 12:41:14 | `2c2cc3ff542a` | 成果面 |
| 262 | `results/_archive_2026_09_20/_ftfb_pass2_results_limitations_audit_2026_09_17.md` | 11,390 | 2026-09-17 22:41:56 | `cfab992cf939` | 成果面 |
| 263 | `results/_archive_2026_09_20/_letter_to_coze_paper_v1_委托_2026_09_17.md` | 12,786 | 2026-09-17 21:29:35 | `6d72e74b3482` | 成果面 |
| 264 | `results/_archive_2026_09_20/_letter_to_coze_〔IM〕_v2_2026_09_18.md` | 18,596 | 2026-09-18 20:50:35 | `ecdbf3a7a9c2` | 成果面 |
| 265 | `results/_archive_2026_09_20/_letter_to_glm_ftfb_deep_revision_2026_09_18.md` | 26,990 | 2026-09-18 13:45:13 | `3de722dc9e39` | 成果面 |
| 266 | `results/_archive_2026_09_20/_letter_to_kimi_push_v3_final_2026_09_17.md` | 10,304 | 2026-09-17 22:55:06 | `e6f8ded3c4ff` | 成果面 |
| 267 | `results/_archive_2026_09_20/_letter_to_kimi_push_v3_final_v2_2026_09_17.md` | 13,964 | 2026-09-17 23:14:56 | `40dda52e5d92` | 成果面 |
| 268 | `results/_archive_2026_09_20/_letter_to_kimi_push_v3_委托_2026_09_17.md` | 13,586 | 2026-09-17 21:30:25 | `042fa374a63f` | 成果面 |
| 269 | `results/_archive_2026_09_20/_letter_to_kimi_upload_requirements_2026_09_18.md` | 22,591 | 2026-09-18 21:30:34 | `6e23b54727e6` | 成果面 |
| 270 | `results/_archive_2026_09_20/_letter_to_mavis_full_mirror_request_2026_09_17.md` | 9,717 | 2026-09-17 23:06:49 | `f2934e5279e6` | 成果面 |
| 271 | `results/_archive_2026_09_20/_letter_to_trae_code_2026_09_17_final.md` | 10,690 | 2026-09-17 18:18:25 | `c1791a7811f3` | 成果面 |
| 272 | `results/_archive_2026_09_20/_p_i_curvature_audit_probe_runner_2026_09_16.py` | 12,919 | 2026-09-16 20:57:28 | `e05555deb611` | 成果面 |
| 273 | `results/_archive_2026_09_20/_probe_doubao_4versions_diff_2026_09_17.json` | 1,393 | 2026-09-17 15:51:14 | `49dde3059959` | 成果面 |
| 274 | `results/_archive_2026_09_20/_probe_doubao_4versions_diff_2026_09_17.py` | 2,720 | 2026-09-17 15:50:56 | `93527eb7b2f7` | 成果面 |
| 275 | `results/_archive_2026_09_20/_probe_doubao_emb_direct_2026_09_17.py` | 2,371 | 2026-09-17 15:48:30 | `9bcfe80c0dd0` | 成果面 |
| 276 | `results/_archive_2026_09_20/_probe_doubao_emb_via_proxy_2026_09_17.py` | 2,589 | 2026-09-17 15:48:59 | `f2818fc2ddff` | 成果面 |
| 277 | `results/_archive_2026_09_20/_probe_teamo_via_proxy.py` | 2,841 | 2026-09-17 15:42:29 | `dce965058076` | 成果面 |
| 278 | `results/_archive_2026_09_20/_reviewer_a_audit_tmp.py` | 4,397 | 2026-09-15 15:57:20 | `268225ccbb76` | 成果面 |
| 279 | `results/_archive_2026_09_20/_sanity_openai_more.py` | 2,187 | 2026-09-17 15:47:48 | `e11319f32dc5` | 成果面 |
| 280 | `results/_archive_2026_09_20/_sanity_teamo_one.py` | 2,119 | 2026-09-17 15:46:36 | `63eb0a0aa102` | 成果面 |
| 281 | `results/_archive_2026_09_20/_sanity_teamo_three.py` | 3,540 | 2026-09-17 15:44:19 | `888d02cd1443` | 成果面 |
| 282 | `results/_archive_2026_09_20/_teamorouter_smoke_tmp.json` | 277 | 2026-09-10 16:46:45 | `4181a24c9ca1` | 成果面 |
| 283 | `results/_archive_2026_09_20/_temp_volc_test.py` | 6,687 | 2026-09-16 11:01:12 | `264f2bf5a3f2` | 成果面 |
| 284 | `results/_archive_2026_09_20/_tmp_inspect_22cap.py` | 675 | 2026-09-11 11:12:09 | `0c9addf4a70f` | 成果面 |
| 285 | `results/_archive_2026_09_20/_tmp_inspect_5model.py` | 1,029 | 2026-09-11 11:11:01 | `048ebc99177c` | 成果面 |
| 286 | `results/_archive_2026_09_20/_v41_flash_rag_caption_embs.bak.json` | 612,511 | 2026-09-10 17:05:53 | `25f745609658` | 成果面 |
| 287 | `results/_archive_2026_09_20/_v41_flash_rag_partial.bak.json` | 88,584 | 2026-09-10 17:07:49 | `b0e2673f4a56` | 成果面 |
| 288 | `results/_archive_2026_09_20/compile_verification.txt` | 9,663 | 2026-09-18 13:45:13 | `463fc7575663` | 成果面 |
| 289 | `results/_archive_2026_09_20/fiction_that_feeds_back.pdf` | 356,123 | 2026-09-17 22:05:22 | `2d9edc8c7303` | 成果面 |
| 290 | `results/_archive_2026_09_20/fiction_that_feeds_back_source.md` | 84,388 | 2026-09-17 22:05:22 | `543479649b3e` | 成果面 |
| 291 | `results/_archive_2026_09_20/ftfb_pass1_background_methodology_audit_2026_09_17.md` | 8,257 | 2026-09-17 22:42:17 | `70bd41d9722d` | 成果面 |
| 292 | `results/_archive_2026_09_20/LETTER_TO_KIMI_GITHUB_UPLOAD_2026_09_18.md` | 13,286 | 2026-09-15 14:55:36 | `8875bf0bc50d` | 成果面 |
| 293 | `results/_archive_2026_09_20/LETTER_TO_TRAE_2026_09_11.md` | 22,776 | 2026-09-16 11:01:12 | `7a95307a3293` | 成果面 |
| 294 | `results/_archive_2026_09_20/LETTER_TO_TRAE_REVIEW_2026_09_16.md` | 12,668 | 2026-09-15 13:47:02 | `1c0885d2b1fa` | 成果面 |
| 295 | `results/_archive_2026_09_20/LETTER_TO_WANG_TEACHER_2026_09_18_FINAL.md` | 10,562 | 2026-09-18 12:19:45 | `7d4b5dd967e2` | 成果面 |
| 296 | `results/_archive_2026_09_20/p_i_curvature_audit_probe_results_2026_09_16.json` | 2,637 | 2026-09-16 17:37:31 | `ae07f5551e87` | 成果面 |
| 297 | `results/_archive_2026_09_20/review_content_A1_glm51.md` | 7,617 | 2026-09-18 00:35:54 | `fd38a2a1ea05` | 成果面 |
| 298 | `results/_archive_2026_09_20/review_content_A2_kimik3.md` | 24,843 | 2026-09-18 09:28:57 | `a964defb923d` | 成果面 |
| 299 | `results/_archive_2026_09_20/review_tech_B1_dsv4pro.md` | 30,494 | 2026-09-18 00:35:54 | `0d36d7cd0589` | 成果面 |
| 300 | `results/_archive_2026_09_20/review_tech_B2_grok46.md` | 13,726 | 2026-09-18 00:35:54 | `fe80bad08eef` | 成果面 |
| 301 | `results/_archive_2026_09_20/REVIEWER_B_TMP_RERUN_2026_09_15.md` | 21,645 | 2026-09-15 14:24:07 | `8cd736ba9f91` | 成果面 |
| 302 | `results/_archive_2026_09_20/SHA256_MANIFEST.txt` | 552 | 2026-09-17 22:06:32 | `416dda94cb63` | 成果面 |
| 303 | `results/_archive_2026_09_20/戴夫_FTFB双审包简报v3_2026-09-17.md` | 8,419 | 2026-09-17 22:06:25 | `6952b3b02b96` | 成果面 |
| 304 | `results/_archive_2026_09_21/2026-09-20.md` | 6,186 | 2026-09-20 18:26:50 | `be7aa1c479b2` | 成果面 |
| 305 | `results/_archive_2026_09_21/2026-09-21.md` | 2,676 | 2026-09-21 09:43:13 | `ef648f34a3a3` | 成果面 |
| 306 | `results/_archive_2026_09_21/_archive_manifest_2026_09_21.json` | 17,353 | 2026-09-21 19:55:39 | `33fe31633da8` | 成果面 |
| 307 | `results/_archive_2026_09_21/deposon_v20_corpus_eval.json` | 631,644 | 2026-08-29 01:21:14 | `ca71aa6858e1` | 成果面 |
| 308 | `results/_archive_2026_09_21/deposon_v20_gt2b.json` | 123,331 | 2026-08-29 19:57:39 | `a2ae7997ee67` | 成果面 |
| 309 | `results/_archive_2026_09_21/deposon_v20_gt3.json` | 7,844 | 2026-08-29 15:03:29 | `35b676773243` | 成果面 |
| 310 | `results/_archive_2026_09_21/deposon_v20_vector_audit.json` | 915 | 2026-08-28 21:15:08 | `b9b65c568842` | 成果面 |
| 311 | `results/_archive_2026_09_24/_final_verify.py` | 2,307 | 2026-09-23 15:34:04 | `31a5d44497f1` | 成果面 |
| 312 | `results/_archive_2026_09_24/_inspect_captions.py` | 591 | 2026-09-10 17:31:00 | `dfb02ade1474` | 成果面 |
| 313 | `results/_archive_2026_09_24/_l13_latency_test.py` | 2,954 | 2026-09-24 14:03:31 | `dae238354342` | 成果面 |
| 314 | `results/_archive_2026_09_24/_v4_pi_decision_questionnaire_2026_09_21_v1.1.md.bak_2026_09_22_gB_post.md` | 113,508 | 2026-09-22 16:00:10 | `07ca9ee8e1bb` | 成果面 |
| 315 | `results/_archive_2026_09_24/_verify_worker_c.py` | 1,155 | 2026-09-10 21:27:55 | `cc578c46b332` | 成果面 |
| 316 | `results/_archive_2026_09_24/_worker_openrouter_rag_run.py` | 24,113 | 2026-09-16 11:01:12 | `4458ccf3d64a` | 成果面 |
| 317 | `results/_archive_2026_09_24/l14_small_batch.py` | 21,784 | 2026-09-24 14:51:45 | `0659c947bec1` | 成果面 |
| 318 | `results/_archive_2026_09_24/latency_test.py` | 617 | 2026-09-24 14:44:18 | `fd9fd98785e1` | 成果面 |
| 319 | `results/_archive_and_b6_inquiry_register_2026_10_08.md` | 21,163 | 2026-10-08 17:12:12 | `1d08a780a715` | 成果面 |
| 320 | `results/_archive_cleanup_extension_2026_09_28.md` | 28,774 | 2026-09-28 20:03:52 | `889d15247607` | 成果面 |
| 321 | `results/_archive_cleanup_non_upload_2026_09_28.md` | 56,714 | 2026-09-28 19:09:12 | `34f2c63306b8` | 成果面 |
| 322 | `results/_archive_ledger_rectification_register_2026_10_09.md` | 20,933 | 2026-10-09 09:31:31 | `99359733eef1` | 成果面 |
| 323 | `results/_archive_manifest_non_upload_v2_2026_09_28.json` | 236,651 | 2026-09-28 19:02:06 | `84eef669234b` | 成果面 |
| 324 | `results/_archive_manifest_non_upload_v3_2026_09_28.json` | 204,256 | 2026-09-28 20:00:44 | `a2e4c5a9b713` | 成果面 |
| 325 | `results/_archive_moveout_register_2026_09_29.md` | 13,363 | 2026-09-29 21:20:14 | `56639e57ac06` | 成果面 |
| 326 | `results/_asset_identity_reconciliation_2026_10_01.md` | 28,291 | 2026-10-01 11:27:03 | `0d22797f084f` | 成果面 |
| 327 | `results/_axis1_three_recomputations_2026_10_11.md` | 29,938 | 2026-10-11 17:26:24 | `8de23f7d7384` | 成果面 |
| 328 | `results/_b01_new_key_classification_2026_10_10.md` | 38,669 | 2026-10-10 21:31:57 | `2ddfecf6201c` | 成果面 |
| 329 | `results/_b01_new_key_residue_judgment_2026_10_10.md` | 41,984 | 2026-10-10 23:13:30 | `345517455dcf` | 成果面 |
| 330 | `results/_b01_p_counting_recompute_2026_10_10.md` | 22,104 | 2026-10-10 20:00:44 | `3511cf21a869` | 成果面 |
| 331 | `results/_b01_recompute_authorization_supplement_2026_10_11.md` | 18,454 | 2026-10-11 00:14:37 | `03a66d4c663a` | 成果面 |
| 332 | `results/_b01_recompute_sec4_2_erratum_2026_10_10.md` | 16,441 | 2026-10-10 21:33:26 | `fac3308fb295` | 成果面 |
| 333 | `results/_b14_audit_f2f3_closure_register_2026_10_11.md` | 29,620 | 2026-10-11 14:36:37 | `9d4a3d6ddf88` | 成果面 |
| 334 | `results/_b14_vk_evidence_audit_2026_10_10.md` | 33,586 | 2026-10-11 00:07:21 | `89f17297f1f5` | 成果面 |
| 335 | `results/_b_coincidence_closeout_register_2026_10_10.md` | 31,451 | 2026-10-10 13:32:32 | `51ce7b49c423` | 成果面 |
| 336 | `results/_b_coincidence_disposition_judgment_2026_10_10.md` | 42,838 | 2026-10-10 13:17:14 | `7ff80485955c` | 成果面 |
| 337 | `results/_backfill_rule_execution_register_2026_10_08.md` | 27,267 | 2026-10-08 16:52:40 | `3a7f8e203b28` | 成果面 |
| 338 | `results/_backfill_rule_final_2026_10_09.md` | 34,602 | 2026-10-09 09:26:50 | `3e97d5286760` | 成果面 |
| 339 | `results/_backfill_rule_vk_closeout_2026_10_08.md` | 26,890 | 2026-10-08 17:02:40 | `20f5835d47d2` | 成果面 |
| 340 | `results/_batch12_deliberation_judgment_2026_10_14.md` | 39,448 | 2026-10-14 16:38:19 | `8218a8777192` | 成果面 †141 |
| 341 | `results/_batch3_receipt_kimi_2026_10_01.md` | 2,238 | 2026-10-01 00:07:36 | `8c2cb4c6a937` | 成果面 |
| 342 | `results/_beta_formal_run_exec_register_2026_10_09.md` | 16,811 | 2026-10-09 23:32:35 | `2e5f080eab6c` | 成果面 |
| 343 | `results/_beta_formal_run_result_2026_10_09.json` | 103,691 | 2026-10-09 23:30:08 | `a5a918fd9861` | 成果面 |
| 344 | `results/_blade_caliber_b8_judgment_2026_10_10.md` | 28,738 | 2026-10-10 09:51:16 | `e189d6eb63d9` | 成果面 |
| 345 | `results/_c1c4_ab_pilot_comparison_2026_10_09.md` | 15,390 | 2026-10-09 23:02:14 | `bdd2a1d7e6c5` | 成果面 |
| 346 | `results/_c2_criterion_third_tier_draft_2026_10_11.md` | 26,713 | 2026-10-11 17:36:57 | `844179898102` | 成果面 |
| 347 | `results/_c4_math_corrections_downstream_erratum_2026_10_10.md` | 28,886 | 2026-10-10 18:18:42 | `643cb9e249f7` | 成果面 |
| 348 | `results/_c4_math_corrections_E1_E2_execution_erratum_2026_10_10.md` | 31,607 | 2026-10-10 21:20:30 | `4c369cb86db4` | 成果面 |
| 349 | `results/_c4_reply_intake_acceptance_register_2026_10_01.md` | 33,728 | 2026-10-10 21:19:00 | `e1e8cb7b9db4` | 成果面 |
| 350 | `results/_c4_theory_source_caliber_correction_2026_09_30.md` | 25,022 | 2026-10-01 09:18:38 | `61b139efd0ef` | 成果面 |
| 351 | `results/_c4_unblock_reply_independent_review_2026_10_10.md` | 27,364 | 2026-10-10 18:13:09 | `2ecd866e2468` | 成果面 |
| 352 | `results/_c8_c2_disposition_register_2026_10_11.md` | 30,956 | 2026-10-11 16:53:47 | `fb816c572779` | 成果面 |
| 353 | `results/_c_component4_d2d3_gap_judgment_2026_10_11.md` | 27,490 | 2026-10-11 00:15:45 | `08d3bfd82235` | 成果面 |
| 354 | `results/_c_component4_three_items_judgment_2026_10_11.md` | 41,580 | 2026-10-11 00:26:46 | `fd0094e2f865` | 成果面 |
| 355 | `results/_c_reading_recompute_2026_10_09.md` | 21,006 | 2026-10-09 09:55:37 | `95d7d23d24fd` | 成果面 |
| 356 | `results/_carrier_qid_disposition_2026_10_11.md` | 3,406 | 2026-10-11 23:22:17 | `7d74d5a4d81e` | 成果面 |
| 357 | `results/_charlie_delivery_register_2026_10_08.md` | 10,733 | 2026-10-08 15:52:36 | `6f4bf31276f5` | 成果面 |
| 358 | `results/_ci_bc_lines_ci_collection_2026_10_09.md` | 24,769 | 2026-10-09 16:47:04 | `6db4d0fb2452` | 成果面 |
| 359 | `results/_ci_bc_scope_estimand_judgments_2026_10_09.md` | 37,682 | 2026-10-09 17:34:04 | `d76ba2297d0d` | 成果面 |
| 360 | `results/_ci_degradation_binding_form_a_register_2026_10_09.md` | 26,104 | 2026-10-09 17:32:42 | `424730b5123d` | 成果面 |
| 361 | `results/_ci_detail_decoupling_degradation_baseline_2026_10_09.md` | 20,973 | 2026-10-09 15:53:38 | `56b62ed5ab74` | 成果面 |
| 362 | `results/_ci_four_items_effectiveness_register_2026_10_09.md` | 29,365 | 2026-10-09 17:14:39 | `4ab2464a266e` | 成果面 |
| 363 | `results/_ci_gap_fill_alt_bc_aper_prime_2026_10_09.md` | 29,709 | 2026-10-09 17:48:22 | `bee0f1f0bdb2` | 成果面 |
| 364 | `results/_ci_line_establishment_2026_10_09.md` | 28,262 | 2026-10-09 15:19:58 | `329c1c5e91d1` | 成果面 |
| 365 | `results/_ci_three_delegated_judgments_2026_10_09.md` | 26,090 | 2026-10-09 17:16:22 | `dac19ee9e66b` | 成果面 |
| 366 | `results/_ci_three_items_effectivity_register_2026_10_09.md` | 31,488 | 2026-10-09 21:12:50 | `2b7166a7d726` | 成果面 |
| 367 | `results/_ci_width_halfwidth_pin_2026_10_09.md` | 17,426 | 2026-10-09 15:52:02 | `51765f40f5f9` | 成果面 |
| 368 | `results/_cleanup_round2_register_2026_09_29.md` | 36,245 | 2026-09-29 22:20:14 | `ee47a2ec49f4` | 成果面 |
| 369 | `results/_cleanup_round_2026_10_01.md` | 27,477 | 2026-10-01 16:42:21 | `0db6e5d6146c` | 成果面 |
| 370 | `results/_cleanup_round_2026_10_08.md` | 33,179 | 2026-10-08 18:25:13 | `d048a6de1dea` | 成果面 |
| 371 | `results/_clearance_materials_register_2026_10_08.md` | 45,254 | 2026-10-08 16:24:26 | `356eb1c53986` | 成果面 |
| 372 | `results/_clearance_mini_rulings_closeout_register_2026_10_01.md` | 31,942 | 2026-10-01 09:10:24 | `9238c2287af5` | 成果面 |
| 373 | `results/_clearance_round_1_register_2026_10_08.md` | 13,826 | 2026-10-08 16:43:54 | `58fa92543338` | 成果面 |
| 374 | `results/_closing_round_4_decisions_register_2026_10_08.md` | 5,322 | 2026-10-08 17:54:26 | `771e37b4a25d` | 成果面 |
| 375 | `results/_closing_round_5_decisions_register_2026_10_08.md` | 3,282 | 2026-10-08 18:02:35 | `5b08d34a05ba` | 成果面 |
| 376 | `results/_closing_round_6_decisions_register_2026_10_08.md` | 3,869 | 2026-10-08 18:05:56 | `272cb570c78b` | 成果面 |
| 377 | `results/_closing_round_7_decisions_register_2026_10_09.md` | 3,206 | 2026-10-09 09:29:38 | `d5976bfe23c6` | 成果面 |
| 378 | `results/_closing_round_9_decisions_register_2026_10_09.md` | 2,314 | 2026-10-09 10:59:27 | `27118156a99a` | 成果面 |
| 379 | `results/_codex_c4_unblock_reply_adoption_register_2026_10_10.md` | 22,895 | 2026-10-10 18:13:35 | `b979e78562a9` | 成果面 |
| 380 | `results/_codex_c4_values_followup_reply_intake_register_2026_10_10.md` | 24,240 | 2026-10-10 17:05:56 | `c46d073589cf` | 成果面 |
| 381 | `results/_codex_c4_values_reply_intake_register_2026_10_10.md` | 12,926 | 2026-10-10 14:09:06 | `8f1d27a02833` | 成果面 |
| 382 | `results/_codex_c4_values_unblock_reply_intake_register_2026_10_10.md` | 27,100 | 2026-10-10 18:06:56 | `a2d7f86d72e5` | 成果面 |
| 383 | `results/_commission_closeout_erratum_and_supplement_2026_10_11.md` | 12,447 | 2026-10-11 23:46:12 | `7c102a6b4667` | 成果面 |
| 384 | `results/_confirm_b9_tension_annex_2026_10_01.md` | 19,454 | 2026-10-01 10:29:54 | `f28724a99a0c` | 成果面 |
| 385 | `results/_confirm_round_2026_10_01_register.md` | 14,500 | 2026-10-01 00:35:17 | `23a97e340fdf` | 成果面 |
| 386 | `results/_confirm_round_2_2026_10_01_register.md` | 22,327 | 2026-10-01 09:44:14 | `817302144788` | 成果面 |
| 387 | `results/_coze_paper_v1_draft_2026_09_17.md` | 29,484 | 2026-09-18 00:21:36 | `c08e7abf5ee3` | 成果面 |
| 388 | `results/_coze_paper_v1_summary_2026_09_17.md` | 3,624 | 2026-09-18 00:20:40 | `2efdc3d7741d` | 成果面 |
| 389 | `results/_coze_〔IM〕_v3_2026_09_18.md` | 7,466 | 2026-09-18 21:03:20 | `229d76e1b86f` | 成果面 |
| 390 | `results/_coze_〔IM〕_v3_d7format_2026_09_18.md` | 8,715 | 2026-09-18 21:08:42 | `905544775aee` | 成果面 |
| 391 | `results/_coze_〔IM〕_v3_final_2026_09_18.md` | 11,657 | 2026-09-18 21:04:55 | `deee45f45c5d` | 成果面 |
| 392 | `results/_coze_〔IM〕_v4_d7format_2026_09_26.pdf` | 465,366 | 2026-09-26 22:50:54 | `a82881653520` | 成果面 |
| 393 | `results/_cpath_sim_runner.py` | 18,783 | 2026-09-10 20:44:28 | `6074d83944dc` | 成果面 |
| 394 | `results/_d05_backbone_robustness_beta_20260918_100853.json` | 1,490 | 2026-09-18 10:14:58 | `9b6f085d96dc` | 成果面 |
| 395 | `results/_d05_combined_report_20260918_100853.md` | 10,555 | 2026-09-18 10:30:53 | `c87eb8974268` | 成果面 |
| 396 | `results/_D05_DATA_RESCUE_NOTE_2026_09_18.md` | 1,181 | 2026-09-18 12:41:46 | `120295a19655` | 成果面 |
| 397 | `results/_d05_i1i5_invariants_check_20260918_100853.json` | 1,920 | 2026-09-18 10:14:59 | `f12af5435928` | 成果面 |
| 398 | `results/_d05_main_run_results_20260918_100853.json` | 15,243 | 2026-09-18 12:41:46 | `0a933d7c8d7a` | 成果面 |
| 399 | `results/_d05_main_run_results_nemotron_3.5_20260918_100853.json` | 15,111 | 2026-09-18 10:14:56 | `1b1b6ad67c39` | 成果面 |
| 400 | `results/_d05_main_run_results_qwen3_failed_20260918_100853.json` | 18,358 | 2026-09-18 12:41:46 | `427b18da8114` | 成果面 |
| 401 | `results/_d05_opt_5_directions_results_20260918_100853.json` | 5,614 | 2026-09-18 10:14:59 | `e5979133195a` | 成果面 |
| 402 | `results/_d05_three_checks_readings_recheck_confirm_2026_10_10.md` | 20,044 | 2026-10-10 12:43:54 | `dcf9f5cfa2db` | 成果面 |
| 403 | `results/_d1_backfill_b3_b7_suggestion_table_2026_10_01.md` | 26,731 | 2026-10-01 12:15:24 | `8e1494301bb8` | 成果面 |
| 404 | `results/_d1_backfill_collection_rounds_2026_10_01.md` | 22,908 | 2026-10-01 12:29:25 | `2d1a0d43e588` | 成果面 |
| 405 | `results/_d1_backfill_conflict_trace_2026_10_01.md` | 31,506 | 2026-10-01 11:06:56 | `0cecda616f15` | 成果面 |
| 406 | `results/_d1_backfill_event_id_prefix_proposal_2026_10_01.md` | 14,074 | 2026-10-01 12:28:08 | `2636394df918` | 成果面 |
| 407 | `results/_d1_backfill_readiness_pack_2026_10_01.md` | 26,462 | 2026-10-01 11:49:06 | `ed644fb07f88` | 成果面 |
| 408 | `results/_d1_ruling_and_s3_transition_2026_10_01.md` | 28,370 | 2026-10-10 11:37:23 | `dc9cb0e02922` | 成果面 |
| 409 | `results/_d7_wang_teacher_〔IM〕_publish_v1_20260918.md` | 9,891 | 2026-09-17 14:39:46 | `f4d5b755736a` | 成果面 |
| 410 | `results/_d8_closeout_protocol_recompute_2026_09_30.md` | 31,007 | 2026-09-30 22:57:20 | `57aba2cd26a6` | 成果面 |
| 411 | `results/_d8_dup_overlap_disposal_2026_09_30.md` | 32,350 | 2026-09-30 14:14:24 | `de8691727842` | 成果面 |
| 412 | `results/_day_close_register_2026_10_01.md` | 33,115 | 2026-10-01 16:55:26 | `6dbac1d1bcd6` | 成果面 |
| 413 | `results/_deemphasis_verification_register_2026_10_08.md` | 27,322 | 2026-10-08 16:02:33 | `3f806e44a13f` | 成果面 |
| 414 | `results/_deposon_v2scripts_kimi7_audit_20260918_105219.json` | 2,096 | 2026-09-18 10:52:19 | `3da62b979053` | 成果面 |
| 415 | `results/_deposon_v2scripts_reverify_20260918_105219.json` | 12,888 | 2026-09-18 10:52:19 | `8ac002ccb082` | 成果面 |
| 416 | `results/_deposon_v2scripts_reverify_20260918_105219.md` | 5,347 | 2026-09-18 10:52:19 | `ee005ea1f031` | 成果面 |
| 417 | `results/_deposon_v2scripts_summary_挂点回扣_20260918_105219.json` | 404 | 2026-09-18 10:52:19 | `2ca5870e4659` | 成果面 |
| 418 | `results/_dup_name_diff_content_scan_2026_10_08.json` | 1,302,889 | 2026-10-08 17:23:27 | `a27d11f45c21` | 成果面 |
| 419 | `results/_e2_glm2_distill_side_receipt_register_2026_10_09.md` | 11,336 | 2026-10-09 10:03:28 | `974124fc53f9` | 成果面 |
| 420 | `results/_e4_lineage_conflict_correction_2026_10_11.md` | 30,510 | 2026-10-11 16:22:45 | `e20b96e32f54` | 成果面 |
| 421 | `results/_e5_nonbinary_count_judgment_2026_10_10.md` | 37,762 | 2026-10-10 11:36:54 | `2ef8797c03f4` | 成果面 |
| 422 | `results/_e6_alt_permp_comparability_closure_2026_10_10.md` | 16,636 | 2026-10-10 15:03:20 | `1c663430b4aa` | 成果面 |
| 423 | `results/_e6_case_a_judgment_face_promotion_2026_10_10.md` | 42,116 | 2026-10-10 12:53:23 | `4e65c53f68e8` | 成果面 |
| 424 | `results/_e6_j5_backfill_resolution_2026_10_10.md` | 23,171 | 2026-10-10 11:45:26 | `c888158b3263` | 成果面 |
| 425 | `results/_e6_j5_semantics_conflict_judgment_2026_10_10.md` | 27,682 | 2026-10-10 13:13:46 | `3c7628a4964d` | 成果面 |
| 426 | `results/_e6_j5_semantics_erratum_note_2026_10_10.md` | 21,166 | 2026-10-10 13:34:44 | `b2db427147e2` | 成果面 |
| 427 | `results/_e6_n_distinct_judge_types_recompute_2026_10_10.md` | 26,304 | 2026-10-10 15:02:56 | `82c5c143134e` | 成果面 |
| 428 | `results/_e6_th_v3_19_alignment_register_2026_10_10.md` | 32,582 | 2026-10-10 15:13:34 | `622cebef2c9f` | 成果面 |
| 429 | `results/_e6_th_v3_19_residual_exits_judgment_2026_10_10.md` | 46,261 | 2026-10-10 17:59:21 | `442d5ff4acdb` | 成果面 |
| 430 | `results/_e6_verdict_v3_rationale_review_2026_10_10.md` | 39,008 | 2026-10-10 13:36:11 | `664e82968fc2` | 成果面 |
| 431 | `results/_ea_audit_batch_vk_2026_10_09.md` | 19,611 | 2026-10-09 12:17:38 | `ce27db55e0c5` | 成果面 |
| 432 | `results/_eps_ls_semantics_judgment_2026_10_11.md` | 31,391 | 2026-10-11 14:59:15 | `51434449ff3b` | 成果面 |
| 433 | `results/_evening_audit_b2_sampling_and_rejudges_2026_10_09.md` | 29,069 | 2026-10-09 23:42:59 | `b067fd28f950` | 成果面 |
| 434 | `results/_executor_prereg_docstring_correction_2026_10_11.md` | 27,721 | 2026-10-12 00:34:33 | `f7f8328c49ba` | 成果面 |
| 435 | `results/_executor_prereg_vs_impl_equivalence_2026_10_11.md` | 20,028 | 2026-10-12 00:08:14 | `e84cec618659` | 成果面 |
| 436 | `results/_exp03_blade_caliber_review_2026_10_10.md` | 19,797 | 2026-10-10 03:00:34 | `8c030758b331` | 成果面 |
| 437 | `results/_exp05_missing_true_disposition_judgment_2026_10_10.md` | 25,552 | 2026-10-10 10:46:49 | `e8e1e63a11db` | 成果面 |
| 438 | `results/_exp05_negative_probe_rescan_2026_10_10.md` | 11,566 | 2026-10-10 03:06:08 | `ca7ff556fd7a` | 成果面 |
| 439 | `results/_exp06_kcf4_check_bit_landing_2026_10_10.md` | 20,709 | 2026-10-10 03:06:42 | `088ba3d58c0f` | 成果面 |
| 440 | `results/_exp08_s4_prompt_face_register_2026_10_10.md` | 11,929 | 2026-10-10 03:07:20 | `83109ecf440e` | 成果面 |
| 441 | `results/_exp08_volume_reconciliation_2026_10_10.md` | 24,140 | 2026-10-10 10:33:56 | `895eb3f2943c` | 成果面 |
| 442 | `results/_external_letters_two_generation_values_note_2026_10_01.md` | 10,979 | 2026-10-01 09:18:01 | `9f4439bf89a9` | 成果面 |
| 443 | `results/_external_pat_ark_prep_2026_09_30.md` | 14,055 | 2026-09-30 19:41:47 | `ca540e5cab23` | 成果面 |
| 444 | `results/_external_sibling_path_reference_rule_2026_10_01.md` | 23,871 | 2026-10-01 13:59:04 | `e79eabb6cfa7` | 成果面 |
| 445 | `results/_f3_definition_deep_judgment_2026_10_11.md` | 42,351 | 2026-10-11 13:46:07 | `11945e587b1d` | 成果面 |
| 446 | `results/_f3_new_definition_draft_2026_10_11.md` | 48,068 | 2026-10-11 12:51:45 | `7482699e8b07` | 成果面 |
| 447 | `results/_f3f4_exit_drafts_2026_10_11.md` | 50,427 | 2026-10-11 01:44:40 | `523dc6cbdf9a` | 成果面 |
| 448 | `results/_f4_direction1_prereq_check_2026_10_11.md` | 38,664 | 2026-10-11 12:42:20 | `bb49153c311f` | 成果面 |
| 449 | `results/_f4_direction1_seed_and_domain_draft_2026_10_11.md` | 33,887 | 2026-10-11 13:29:50 | `f77c080d9fc6` | 成果面 |
| 450 | `results/_f5_77_16items_reconciliation_2026_10_01.md` | 23,930 | 2026-10-01 11:15:01 | `38be1dc9a33f` | 成果面 |
| 451 | `results/_f5_d1_event_count_correction_2026_10_01.md` | 24,994 | 2026-10-01 10:05:17 | `771641e234d6` | 成果面 |
| 452 | `results/_f5_d1_event_count_correction_execution_2026_10_01.md` | 24,279 | 2026-10-01 10:22:03 | `44d8cc9cb4a5` | 成果面 |
| 453 | `results/_fake_verdict_session_log_reverify_2026_09_30.md` | 25,953 | 2026-09-30 12:54:50 | `c14094bdf815` | 成果面 |
| 454 | `results/_family_e_q_type_conflict_resolution_2026_10_14.md` | 19,640 | 2026-10-14 13:15:34 | `dd5547b8e8c7` | 成果面 †141 |
| 455 | `results/_five_items_effectivity_register_2026_10_11.md` | 43,332 | 2026-10-11 16:31:27 | `8affdca64b4b` | 成果面 |
| 456 | `results/_five_pending_items_drafts_2026_10_11.md` | 55,102 | 2026-10-11 16:06:04 | `86c46998de63` | 成果面 |
| 457 | `results/_five_stage_chain_design_reconstruction_2026_10_12.md` | 12,625 | 2026-10-12 01:02:53 | `bff2fb754564` | 成果面 |
| 458 | `results/_forgotten_items_quick_sweep_register_2026_10_01.md` | 43,735 | 2026-10-01 10:05:19 | `91103473289a` | 成果面 |
| 459 | `results/_forgotten_recovery_register_2026_09_29.md` | 47,494 | 2026-09-29 21:39:46 | `d78be896bcb6` | 成果面 |
| 460 | `results/_four_items_execution_batch_2026_10_11.md` | 31,515 | 2026-10-11 15:16:44 | `8006d1962e5f` | 成果面 |
| 461 | `results/_fp3_anchor_and_krj_restrament_register_2026_10_11.md` | 32,886 | 2026-10-11 16:22:16 | `b7c060ab2d49` | 成果面 |
| 462 | `results/_freeze_receipt_2026_10_01_q1.md` | 698 | 2026-10-01 21:02:42 | `9b7101bc09bd` | 成果面 |
| 463 | `results/_ftfb_order_judgment_2026_10_11.md` | 45,911 | 2026-10-11 15:40:48 | `b6eec487e9d7` | 成果面 |
| 464 | `results/_ftfb_v3_pass1_audit_2026_09_18_corrected.md` | 20,117 | 2026-09-18 13:45:13 | `ecb406570615` | 成果面 |
| 465 | `results/_ftfb_v3_pass2_audit_2026_09_18_corrected.md` | 28,579 | 2026-09-18 13:45:13 | `413ddb0bd00e` | 成果面 |
| 466 | `results/_full_tidy_inventory_register_2026_09_30.md` | 27,687 | 2026-09-30 17:48:12 | `33f68dbfbd6f` | 成果面 |
| 467 | `results/_g10_threshold_closed_domain_judgment_2026_10_11.md` | 55,727 | 2026-10-11 01:18:04 | `586abda5ddf7` | 成果面 |
| 468 | `results/_g11_krj4_effectivity_register_2026_10_11.md` | 39,870 | 2026-10-11 12:31:21 | `17168119eccc` | 成果面 |
| 469 | `results/_g4_controlled_reproduction_design_2026_10_09.md` | 23,675 | 2026-10-09 09:47:11 | `b1c7c24926bb` | 成果面 |
| 470 | `results/_g4_e3_definition_independent_judgment_2026_10_09.md` | 29,094 | 2026-10-09 12:33:36 | `aebaff5b503c` | 成果面 |
| 471 | `results/_g4_e3_definition_ruling_material_2026_10_09.md` | 30,662 | 2026-10-09 11:07:09 | `8ae4016bb41d` | 成果面 |
| 472 | `results/_g4_reproduction_execution_register_2026_10_09.md` | 20,414 | 2026-10-09 10:21:25 | `4daaf68cbf0e` | 成果面 |
| 473 | `results/_g4_residual_probe_2026_10_08.md` | 23,025 | 2026-10-08 16:19:49 | `3554aa156e08` | 成果面 |
| 474 | `results/_g4_runtime_state_trace_2026_10_01.md` | 25,631 | 2026-10-01 16:31:10 | `e0ae0ad66acb` | 成果面 |
| 475 | `results/_g4_skill_read_scope_trace_2026_10_01.md` | 26,906 | 2026-10-01 14:31:34 | `9196a608bb0d` | 成果面 |
| 476 | `results/_g5_ccp_p0_verification_2026_10_10.md` | 24,819 | 2026-10-10 19:05:07 | `8c7693379496` | 成果面 |
| 477 | `results/_g5_displacement_threshold_c_approval_effect_and_trigger_eval_2026_10_10.md` | 33,880 | 2026-10-10 14:44:04 | `3015f2481df1` | 成果面 |
| 478 | `results/_g5_displacement_threshold_draft_2026_10_10.md` | 25,619 | 2026-10-10 14:02:11 | `7c8107d9a8fb` | 成果面 |
| 479 | `results/_g5_krj9_denominator_reconciliation_judgment_2026_10_10.md` | 45,207 | 2026-10-10 18:34:36 | `22d90f12d605` | 成果面 |
| 480 | `results/_g5_rejudgment_c_applicability_recheck_2026_10_10.md` | 49,051 | 2026-10-10 17:09:46 | `15301b3025fa` | 成果面 |
| 481 | `results/_g5_rejudgment_construction_question_judgment_2026_10_10.md` | 59,309 | 2026-10-10 17:47:40 | `ee660515d9e3` | 成果面 |
| 482 | `results/_g5_rejudgment_face_prereg_2026_10_10.md` | 35,097 | 2026-10-10 16:04:10 | `04495ef4b343` | 成果面 |
| 483 | `results/_g5_rejudgment_trigger_caliber_judgment_2026_10_10.md` | 48,727 | 2026-10-10 17:12:00 | `16c31894d445` | 成果面 |
| 484 | `results/_g5_seg3_tie_veto_judgment_2026_10_10.md` | 35,983 | 2026-10-10 15:17:28 | `3306d1fd020d` | 成果面 |
| 485 | `results/_g5_x4_dual_axis_interpretation_judgment_2026_10_10.md` | 33,976 | 2026-10-10 18:29:03 | `c3117773ab36` | 成果面 |
| 486 | `results/_g9_read_b_effectivity_register_2026_10_11.md` | 29,649 | 2026-10-11 16:53:23 | `f5d601a0602a` | 成果面 |
| 487 | `results/_gap_closeout_status_2026_10_09.md` | 28,793 | 2026-10-09 11:07:19 | `ea41e346c4c4` | 成果面 |
| 488 | `results/_gate_one_declared_adoption_register_2026_10_11.md` | 12,923 | 2026-10-12 00:18:23 | `3a965362d4f4` | 成果面 |
| 489 | `results/_gate_one_pi_endorsement_register_2026_10_12.md` | 9,579 | 2026-10-12 00:53:49 | `b09209e9c20d` | 成果面 |
| 490 | `results/_ge01_H_enumeration_and_lock_2026_10_13.md` | 28,522 | 2026-10-14 00:09:51 | `4c5860342d7f` | 成果面 †141 |
| 491 | `results/_ge01_H_enumeration_round2_2026_10_13.md` | 37,191 | 2026-10-14 00:52:38 | `ff2afb7a634b` | 成果面 †141 |
| 492 | `results/_ge01_prereg_5anchor_v3_lock_register_2026_10_15.md` | 17,885 | 2026-10-15 13:01:46 | `deea2ccb2643` | 成果面 †141 |
| 493 | `results/_give_up_n10_erratum_2026_10_10.md` | 22,021 | 2026-10-10 15:25:42 | `e0db6b819138` | 成果面 |
| 494 | `results/_give_up_semantics_draft_2026_10_10.md` | 23,497 | 2026-10-10 13:26:05 | `b6a4ae82e038` | 成果面 |
| 495 | `results/_glm_five_items_suggestion_table_2026_10_01.md` | 29,622 | 2026-10-01 11:21:40 | `f2b1359be37d` | 成果面 |
| 496 | `results/_glm_response_v2_template_2026_09_18.md` | 44,191 | 2026-09-18 13:59:16 | `972401e056f6` | 成果面 |
| 497 | `results/_glm_v3_双审报告_2026_09_18.md` | 20,632 | 2026-09-18 09:39:59 | `26537967db82` | 成果面 |
| 498 | `results/_gt_recon_gamma_erratum_note_2026_10_01.md` | 9,103 | 2026-10-01 09:17:17 | `ca063e6b9d60` | 成果面 |
| 499 | `results/_id_face_revision_sync_note_2026_10_10.md` | 20,690 | 2026-10-10 00:43:53 | `5d6c473731c4` | 成果面 |
| 500 | `results/_inspect_captions.py` | 591 | 2026-09-10 17:31:00 | `dfb02ade1474` | 成果面 |
| 501 | `results/_itemH_fingerprint_provenance_2026_10_12.md` | 22,752 | 2026-10-12 15:52:58 | `bacbee9a158f` | 成果面 †141 |
| 502 | `results/_itemH_nonclade_and_hangings_register_2026_10_12.md` | 13,223 | 2026-10-12 16:15:31 | `37ea7f65a8d6` | 成果面 †141 |
| 503 | `results/_j2_identifier_coupling_judgment_2026_10_11.md` | 34,261 | 2026-10-11 16:03:04 | `2fd4505fdca2` | 成果面 |
| 504 | `results/_j2_kj4_disposition_register_2026_10_11.md` | 34,112 | 2026-10-11 16:37:29 | `c1a4ff1b96e5` | 成果面 |
| 505 | `results/_k_cf_4_effectivity_register_2026_10_09.md` | 35,872 | 2026-10-09 17:06:53 | `edc6a548e3ca` | 成果面 |
| 506 | `results/_k_cf_4_low_cardinality_recure_2026_10_09.md` | 33,788 | 2026-10-09 15:39:37 | `5f91d553e392` | 成果面 |
| 507 | `results/_k_cf_4_low_cardinality_reurecheck_and_precedent_fill_2026_10_09.md` | 31,801 | 2026-10-09 15:44:50 | `618280cb8cfd` | 成果面 |
| 508 | `results/_k_v3df_0_1_readings_verdict_2026_10_09.md` | 37,003 | 2026-10-09 12:06:13 | `e98bee353448` | 成果面 |
| 509 | `results/_k_v3df_9_1_c1_c4_legs_verdict_2026_10_09.md` | 27,735 | 2026-10-09 11:50:56 | `a14aafa220c4` | 成果面 |
| 510 | `results/_k_v3df_scope_two_judgments_2026_10_09.md` | 21,350 | 2026-10-09 17:33:46 | `4b22ba3c463e` | 成果面 |
| 511 | `results/_k_v3s_3_4_lock_freeze_2026_10_08.md` | 16,973 | 2026-10-08 16:45:08 | `c64865c32761` | 成果面 |
| 512 | `results/_k_v3s_4_2_domain_extension_judgment_2026_10_09.md` | 23,018 | 2026-10-09 21:06:53 | `a802af7ac3bc` | 成果面 |
| 513 | `results/_kd04_c_denominator_closeout_register_2026_10_10.md` | 23,029 | 2026-10-10 13:21:16 | `78481cc60494` | 成果面 |
| 514 | `results/_kd04_c_denominator_expansion_exec_2026_10_10.md` | 27,915 | 2026-10-10 11:41:56 | `2caa3966b866` | 成果面 |
| 515 | `results/_kd04_c_denominator_verdict_keeper_alternative_judgment_2026_10_10.md` | 25,123 | 2026-10-10 13:03:50 | `19ad36f7ec84` | 成果面 |
| 516 | `results/_kd_19_ambiguous_tags_rejudge_rewrite_register_2026_10_10.md` | 29,664 | 2026-10-14 11:35:04 | `63d1566d273e` | 成果面 |
| 517 | `results/_kd_doc1_correction_adoption_register_2026_10_11.md` | 10,255 | 2026-10-12 00:39:06 | `c55770be5e33` | 成果面 |
| 518 | `results/_kd_heteronym_classification_disposition_2026_10_09.md` | 29,761 | 2026-10-14 14:07:09 | `2d291f1d8de5` | 成果面 |
| 519 | `results/_kd_legacy_rewrite_plan_2026_10_10.md` | 17,643 | 2026-10-10 02:57:52 | `a9698fed8b9b` | 成果面 |
| 520 | `results/_kd_legacy_rewrite_register_2026_10_10.md` | 14,537 | 2026-10-10 10:41:53 | `9a7936882a5d` | 成果面 |
| 521 | `results/_kd_legacy_rewrite_ruling_2026_10_10.md` | 13,731 | 2026-10-10 10:40:29 | `2cadab5ed4f7` | 成果面 |
| 522 | `results/_kd_login_register_section65_correction_2026_10_10.md` | 20,422 | 2026-10-10 13:56:56 | `316d14c137bb` | 成果面 |
| 523 | `results/_kd_resolvability_and_optional_experiments_2026_10_09.md` | 70,328 | 2026-10-14 11:35:54 | `53d4fa3a681f` | 成果面 |
| 524 | `results/_kd_rewrite_fingerprint_sync_2026_10_10.md` | 20,862 | 2026-10-10 11:53:38 | `aeefc94a94b5` | 成果面 |
| 525 | `results/_kd_uncognizable_meaning_rewrite_register_2026_10_10.md` | 19,525 | 2026-10-10 11:38:50 | `b07887551f7c` | 成果面 |
| 526 | `results/_kickoff_decisions_register_2026_10_08.md` | 16,388 | 2026-10-08 16:02:29 | `6ee5d2b8323c` | 成果面 |
| 527 | `results/_kimi_ftfb_s7_independent_recompute_2026_09_18.json` | 3,605 | 2026-09-18 10:39:43 | `879db0217f04` | 成果面 |
| 528 | `results/_kimi_fullupload_r1_r4_rulings_register_2026_09_30.md` | 4,794 | 2026-09-30 21:47:40 | `1c7445fca0de` | 成果面 |
| 529 | `results/_kimi_push_v3_manifest_batch10_1b753116.json` | 5,007 | 2026-09-17 23:34:06 | `326adca520f1` | 成果面 |
| 530 | `results/_kimi_push_v3_manifest_batch11_7d6a7c8f.json` | 2,573 | 2026-09-18 22:27:36 | `383446f24707` | 成果面 |
| 531 | `results/_kimi_push_v3_manifest_batch12_a2853574.json` | 1,246 | 2026-09-18 22:27:36 | `6be21f9586ec` | 成果面 |
| 532 | `results/_kimi_push_v3_manifest_batch13_83f895f9.json` | 739 | 2026-09-18 22:27:36 | `0694838f66a8` | 成果面 |
| 533 | `results/_kimi_push_v3_manifest_batch14_e5952130.json` | 1,055 | 2026-09-18 22:27:36 | `64aa9d8a5c7d` | 成果面 |
| 534 | `results/_kimi_push_v3_manifest_batch15_0e65fe2f.json` | 385 | 2026-09-20 09:39:32 | `cfc345d10c7d` | 成果面 |
| 535 | `results/_kimi_push_v3_manifest_batch1_77e2f952.json` | 2,534 | 2026-09-17 23:22:31 | `b5f517a321a3` | 成果面 |
| 536 | `results/_kimi_push_v3_manifest_batch2_e18c17bb.json` | 9,260 | 2026-09-17 23:23:29 | `f14341b8a1a1` | 成果面 |
| 537 | `results/_kimi_push_v3_manifest_batch3_01ecf050.json` | 9,656 | 2026-09-17 23:24:23 | `fd64909ea1d8` | 成果面 |
| 538 | `results/_kimi_push_v3_manifest_batch4_2f872d54.json` | 9,720 | 2026-09-17 23:25:26 | `d35453f21049` | 成果面 |
| 539 | `results/_kimi_push_v3_manifest_batch5_34439e1e.json` | 9,511 | 2026-09-17 23:28:31 | `2769b83f5b1d` | 成果面 |
| 540 | `results/_kimi_push_v3_manifest_batch6_28055e59.json` | 10,107 | 2026-09-17 23:29:50 | `f3eb7a38ae7d` | 成果面 |
| 541 | `results/_kimi_push_v3_manifest_batch7_0903df7e.json` | 9,748 | 2026-09-17 23:30:56 | `7bda1fecd7c4` | 成果面 |
| 542 | `results/_kimi_push_v3_manifest_batch8_7468a23b.json` | 9,880 | 2026-09-17 23:32:05 | `5a38fc02978c` | 成果面 |
| 543 | `results/_kimi_push_v3_manifest_batch9_f7d9cf1d.json` | 9,745 | 2026-09-17 23:33:10 | `968d7c6c43ca` | 成果面 |
| 544 | `results/_kimi_push_v3_manifest_verifier21_cc3c92d0.json` | 4,159 | 2026-09-18 13:45:13 | `5a6601f47632` | 成果面 |
| 545 | `results/_kimi_safe_batch_push_v1_2026_09_17.json` | 7,280 | 2026-09-17 14:01:43 | `4a204fb0d682` | 成果面 |
| 546 | `results/_kimi_safe_batch_push_v2_full_2026_09_17.json` | 47,954 | 2026-09-17 14:51:41 | `adf3a8017e26` | 成果面 |
| 547 | `results/_kimi_safe_batch_push_v3_full_2026_09_17.json` | 7,954 | 2026-09-18 13:50:24 | `058099c10cfb` | 成果面 |
| 548 | `results/_kj1_abc_choice_judgment_2026_10_11.md` | 42,083 | 2026-10-11 15:02:27 | `d02ec6b0987e` | 成果面 |
| 549 | `results/_kj1_eps_ls_effectivity_register_2026_10_11.md` | 62,344 | 2026-10-11 15:42:36 | `809edb4bb1cc` | 成果面 |
| 550 | `results/_kj1_judgment_premise_correction_2026_10_11.md` | 35,050 | 2026-10-11 15:16:12 | `003b134cce24` | 成果面 |
| 551 | `results/_kj1_sc1_premise_correction_2026_10_11.md` | 31,044 | 2026-10-11 14:59:46 | `8b344b9b4715` | 成果面 |
| 552 | `results/_kj4_e4_unification_judgment_2026_10_11.md` | 36,839 | 2026-10-11 16:08:15 | `a14d49f7d3a2` | 成果面 |
| 553 | `results/_krj10_reverdict_after_r4_convergence_2026_10_11.md` | 31,672 | 2026-10-12 00:05:01 | `a21915ec55a7` | 成果面 |
| 554 | `results/_krj10_terminal_verdict_closure_2026_10_11.md` | 14,101 | 2026-10-11 20:52:41 | `f2e8e32089b2` | 成果面 |
| 555 | `results/_krj4_trj1_adjudication_judgment_2026_10_11.md` | 30,293 | 2026-10-11 20:43:41 | `50e91bf30e45` | 成果面 |
| 556 | `results/_krj4_trj1_pick_and_pass_verdict_2026_10_11.md` | 16,567 | 2026-10-11 21:06:58 | `fb7bb5da85ec` | 成果面 |
| 557 | `results/_krj5_final_disposition_verdict_2026_10_11.md` | 60,700 | 2026-10-11 01:17:39 | `2b6bf509a135` | 成果面 |
| 558 | `results/_krj5_subject_scope_judgment_2026_10_11.md` | 45,372 | 2026-10-11 00:47:58 | `ae9df5119861` | 成果面 |
| 559 | `results/_krj5d_third_tier_effectivity_2026_10_11.md` | 10,729 | 2026-10-11 21:52:41 | `062093d95c9f` | 成果面 |
| 560 | `results/_krj9_scope_clarification_draft_2026_10_10.md` | 28,654 | 2026-10-10 19:55:36 | `b17b3c38ec21` | 成果面 |
| 561 | `results/_krj_all_five_verdicts_rewrite_2026_10_11.md` | 72,247 | 2026-10-11 21:12:00 | `78fb8c47c944` | 成果面 |
| 562 | `results/_krj_all_terminal_verdicts_2026_10_11.md` | 95,659 | 2026-10-11 17:51:02 | `f52231807e36` | 成果面 |
| 563 | `results/_krj_cond4_bytes_erratum_2026_10_11.md` | 3,886 | 2026-10-11 20:41:59 | `78a95e5561fc` | 成果面 |
| 564 | `results/_krj_cond4_effectivity_declaration_2026_10_11.md` | 15,546 | 2026-10-11 20:32:37 | `f5c317f4cc96` | 成果面 |
| 565 | `results/_krj_five_verdicts_adjudication_2026_10_11.md` | 16,064 | 2026-10-11 21:20:35 | `5c0efd663847` | 成果面 |
| 566 | `results/_krj_pi_picks_adoption_krj6_revise_2026_10_11.md` | 15,214 | 2026-10-11 21:34:15 | `31e32ccc59bf` | 成果面 |
| 567 | `results/_kv3s_3_2_terminal_verdict_2026_10_01.md` | 32,296 | 2026-10-14 14:07:09 | `693eefdd7a82` | 成果面 |
| 568 | `results/_kv3s_4_1_2_rejudge_2026_10_09.md` | 51,594 | 2026-10-09 22:34:56 | `9cde399502ba` | 成果面 |
| 569 | `results/_kv3s_4_4_carryover_bytes_correction_2026_10_10.md` | 5,807 | 2026-10-10 00:39:05 | `0a7d2ccf74ad` | 成果面 |
| 570 | `results/_kv3s_4_4_review_carryover_2026_10_10.md` | 17,606 | 2026-10-10 00:38:39 | `660d40ddd78c` | 成果面 |
| 571 | `results/_kv3s_4_terminal_verdict_2026_10_09.md` | 50,858 | 2026-10-09 17:23:30 | `e51317fcc5cf` | 成果面 |
| 572 | `results/_kv3s_4_terminal_verdict_supplement_2026_10_09.md` | 20,211 | 2026-10-09 18:06:24 | `0f82948defb3` | 成果面 |
| 573 | `results/_l3_deferred_items_immediate_disposition_register_2026_10_13.md` | 33,958 | 2026-10-13 22:41:09 | `92e410f45256` | 成果面 †141 |
| 574 | `results/_letters_archive_register_2026_10_01.md` | 26,299 | 2026-10-02 00:29:52 | `9f0740da7e4d` | 成果面 |
| 575 | `results/_lim_aperiod_adoption_and_label_correction_2026_10_11.md` | 14,770 | 2026-10-11 21:43:15 | `f4b129e3312f` | 成果面 |
| 576 | `results/_lim_aperiod_restatement_third_domain_2026_10_11.md` | 27,946 | 2026-10-11 21:38:15 | `8672a5541ca8` | 成果面 |
| 577 | `results/_limb_reading_verdict_kv3s33_2026_10_01.md` | 56,329 | 2026-10-10 11:37:24 | `c5866ce87d9c` | 成果面 |
| 578 | `results/_linestand_pi_signoff_2026_10_01.md` | 35,538 | 2026-10-01 12:20:10 | `cb5d933f8fae` | 成果面 |
| 579 | `results/_linestand_trace_gap_note_2026_10_01.md` | 23,252 | 2026-10-01 10:04:22 | `91bb552bf76b` | 成果面 |
| 580 | `results/_log_observation_review_2026_10_08.md` | 2,918 | 2026-10-08 18:14:19 | `ae20780c8d4e` | 成果面 |
| 581 | `results/_log_surface_scan_2026_10_08.md` | 3,156 | 2026-10-08 18:40:53 | `6b0b202c5a6c` | 成果面 |
| 582 | `results/_m3_glm29_adoption_register_2026_10_13.md` | 23,309 | 2026-10-13 22:33:25 | `6aff3c459ca0` | 成果面 †141 |
| 583 | `results/_m5_eps_drift_disposition_2026_10_11.md` | 2,736 | 2026-10-11 23:19:36 | `0722f25f5838` | 成果面 |
| 584 | `results/_m5_rejudgment_and_dual_value_register_2026_10_14.md` | 16,093 | 2026-10-14 10:42:37 | `4b72fbe08ce2` | 成果面 †141 |
| 585 | `results/_m_r16_alias_table_draft_2026_10_01.md` | 28,128 | 2026-10-01 09:52:02 | `0ba685b0d875` | 成果面 |
| 586 | `results/_m_r16_alias_table_effective_2026_10_01.md` | 36,578 | 2026-10-01 10:28:11 | `4ffdb809ef22` | 成果面 |
| 587 | `results/_mavis_skill_inventory_2026_09_18.md` | 99,702 | 2026-09-18 13:50:10 | `90ba7f7a7fbe` | 成果面 |
| 588 | `results/_mini_round_3_decisions_register_2026_10_01.md` | 44,308 | 2026-10-01 10:24:36 | `bff06d3b3f97` | 成果面 |
| 589 | `results/_mini_round_4_decisions_register_2026_10_01.md` | 37,804 | 2026-10-01 11:06:23 | `0f2d1afcc793` | 成果面 |
| 590 | `results/_mini_round_5_decisions_register_2026_10_01.md` | 53,125 | 2026-10-14 14:07:09 | `eb40a1b9f4e1` | 成果面 |
| 591 | `results/_mini_round_6_7_settlement_register_2026_10_01.md` | 68,053 | 2026-10-14 11:35:54 | `3cb2dfe3c293` | 成果面 |
| 592 | `results/_misformed_commission_drafts_deletion_register_2026_10_11.md` | 7,261 | 2026-10-11 22:45:36 | `bbdc9c2c8028` | 成果面 |
| 593 | `results/_morning_wrapup_pending_rulings_2026_10_01.md` | 7,341 | 2026-10-01 09:36:01 | `2b6e8b527f93` | 成果面 |
| 594 | `results/_mq_rollout_v7_effect_register_2026_10_14.md` | 15,538 | 2026-10-14 22:33:08 | `a709ff7b48de` | 成果面 †141 |
| 595 | `results/_mq_rollout_v8_effect_register_2026_10_14.md` | 14,621 | 2026-10-14 22:55:15 | `5f32931507bb` | 成果面 †141 |
| 596 | `results/_n01_n08_revision_2026_10_10.md` | 26,628 | 2026-10-10 15:22:33 | `fa8400d8ae70` | 成果面 |
| 597 | `results/_n1_d4_clause_placement_determination_2026_10_01.md` | 53,732 | 2026-10-01 13:55:45 | `7cda6adea62b` | 成果面 |
| 598 | `results/_n7_mutual_exclusion_determination_2026_10_01.md` | 40,169 | 2026-10-10 11:37:24 | `b6bdf807cb27` | 成果面 |
| 599 | `results/_naming_erratum_linestand_note_2026_10_01.md` | 12,137 | 2026-10-01 12:27:50 | `38c8218d066b` | 成果面 |
| 600 | `results/_numbering_face_signature_effect_2026_10_13.md` | 11,273 | 2026-10-13 23:34:31 | `6a7f0a1890a4` | 成果面 †141 |
| 601 | `results/_numbering_family_count_corrigendum_2026_10_14.md` | 19,812 | 2026-10-14 02:27:50 | `9baf2ea2e9cb` | 成果面 †141 |
| 602 | `results/_numbering_raw_residual_461_variants_corrigendum_2026_10_14.md` | 5,239 | 2026-10-14 03:00:22 | `33feb734ca80` | 成果面 †141 |
| 603 | `results/_o_r2_r5_external_verification_2026_10_01.md` | 59,327 | 2026-10-01 09:16:48 | `d03832d3e2ff` | 成果面 |
| 604 | `results/_overnight_delivery_index_2026_10_10.md` | 35,344 | 2026-10-10 03:23:28 | `266d0327025d` | 成果面 |
| 605 | `results/_p3_candidate3_supplement_register_2026_10_13.md` | 22,448 | 2026-10-13 22:31:45 | `b7f725de2d95` | 成果面 †141 |
| 606 | `results/_p4_attribution_determination_2026_10_01.md` | 22,053 | 2026-10-01 10:49:15 | `c6793cff46d7` | 成果面 |
| 607 | `results/_p4_clause2_ratification_note_2026_10_01.md` | 26,871 | 2026-10-01 12:19:59 | `cdf009712b96` | 成果面 |
| 608 | `results/_p_d_v03_22caption_verification_20260917_163757.json` | 13,775 | 2026-09-17 16:37:57 | `dfbcc5d6fc34` | 成果面 |
| 609 | `results/_p_d_v03_verification_report_20260917_163757.md` | 9,799 | 2026-09-17 16:39:34 | `67aafb57a8ed` | 成果面 |
| 610 | `results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json` | 1,669 | 2026-09-16 17:39:59 | `a9ad1de618f5` | 成果面 |
| 611 | `results/_p_k_v3_glm_fpr_audit_report_2026-09-17T08-23-41Z.md` | 8,558 | 2026-09-17 16:23:41 | `71d5c23d9f76` | 成果面 |
| 612 | `results/_p_k_v3_glm_json_audit_2026-09-17T08-23-41Z.json` | 6,678 | 2026-09-17 16:23:41 | `f236e88f22ca` | 成果面 |
| 613 | `results/_p_k_v3_three_way_rerun_2026-09-17T08-23-41Z.json` | 12,992 | 2026-09-17 16:23:41 | `05ff758ae921` | 成果面 |
| 614 | `results/_p_l_v3_phase1_report_20260917_132341.md` | 11,035 | 2026-09-17 13:35:32 | `b41a17eda169` | 成果面 |
| 615 | `results/_p_l_v3_phase2_beta_summary_20260917_142748.json` | 2,417 | 2026-09-17 14:27:54 | `86d4cb146241` | 成果面 |
| 616 | `results/_p_l_v3_phase2_closedsource_report_20260917_175544.md` | 5,909 | 2026-09-17 17:55:55 | `02443dd300ce` | 成果面 |
| 617 | `results/_p_l_v3_phase2_closedsource_summary_20260917_175544.json` | 3,286 | 2026-09-17 17:55:55 | `a3eafaf9ba03` | 成果面 |
| 618 | `results/_p_l_v3_phase2_doubao_v2_summary_20260917_170828.json` | 4,357 | 2026-09-17 17:12:34 | `c366f4e30b6b` | 成果面 |
| 619 | `results/_p_l_v3_phase2_doubao_v2_summary_20260917_172206.json` | 14,469 | 2026-09-17 17:55:09 | `e3dccddaed87` | 成果面 |
| 620 | `results/_p_l_v3_phase2_or_embedding_v3_report_20260917_162614.md` | 8,102 | 2026-09-17 16:33:30 | `fa5da7a307bd` | 成果面 |
| 621 | `results/_p_l_v3_phase2_or_embedding_v3_summary_20260917_162614.json` | 8,308 | 2026-09-17 16:29:34 | `21c9f23699a8` | 成果面 |
| 622 | `results/_p_l_v3_phase2_report_20260917_142748.md` | 9,056 | 2026-09-17 14:33:45 | `58e15c07af33` | 成果面 |
| 623 | `results/_p_l_v3_phase3_adendum_summary_20260917_132143.md` | 16,612 | 2026-09-17 13:22:27 | `8c07ab5aa968` | 成果面 |
| 624 | `results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133358.md` | 6,637 | 2026-09-17 13:34:00 | `54859cf2217a` | 成果面 |
| 625 | `results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133512.md` | 6,337 | 2026-09-17 13:35:15 | `c350e420eca6` | 成果面 |
| 626 | `results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133705.md` | 6,434 | 2026-09-17 13:37:07 | `772112cf5bd4` | 成果面 |
| 627 | `results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133726.md` | 6,435 | 2026-09-17 13:37:29 | `d7f03fde4067` | 成果面 |
| 628 | `results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133852.md` | 6,616 | 2026-09-17 13:38:55 | `d66388b6532d` | 成果面 |
| 629 | `results/_p_l_v3_real_collapse_mistral_L100_20260917_132341.json` | 43,903 | 2026-09-17 13:33:51 | `4657b210782a` | 成果面 |
| 630 | `results/_p_l_v3_real_collapse_mistral_L30_20260917_132341.json` | 16,545 | 2026-09-17 13:23:49 | `f6ab84f27d9a` | 成果面 |
| 631 | `results/_p_l_v3_real_collapse_mistral_L45_20260917_132341.json` | 20,108 | 2026-09-17 13:26:47 | `dc37ee54781c` | 成果面 |
| 632 | `results/_p_l_v3_real_collapse_mistral_L60_20260917_132341.json` | 1,174 | 2026-09-17 13:26:47 | `e3fb4f775e22` | 成果面 |
| 633 | `results/_p_l_v3_robustness_claude_sonnet5_L30_20260917_174011.json` | 30,772 | 2026-09-17 17:49:05 | `9d329721f67d` | 成果面 |
| 634 | `results/_p_l_v3_robustness_claude_sonnet5_L60_20260917_174011.json` | 1,292 | 2026-09-17 17:49:05 | `28e462c11692` | 成果面 |
| 635 | `results/_p_l_v3_robustness_gemini_37flash_L30_20260917_175003.json` | 30,514 | 2026-09-17 17:53:55 | `0f5c80a8a4ae` | 成果面 |
| 636 | `results/_p_l_v3_robustness_gemini_37flash_L60_20260917_175003.json` | 1,288 | 2026-09-17 17:53:55 | `e2590651f9c0` | 成果面 |
| 637 | `results/_p_l_v3_robustness_glm53_L30_20260917_142011.json` | 18,281 | 2026-09-17 14:25:11 | `2deadd7be100` | 成果面 |
| 638 | `results/_p_l_v3_robustness_glm53_L60_20260917_142011.json` | 1,037 | 2026-09-17 14:25:11 | `31556b58caa1` | 成果面 |
| 639 | `results/_p_l_v3_robustness_gpt56sol_L30_20260917_173159.json` | 30,347 | 2026-09-17 17:39:13 | `3865d7a61ca1` | 成果面 |
| 640 | `results/_p_l_v3_robustness_gpt56sol_L60_20260917_173159.json` | 1,266 | 2026-09-17 17:39:13 | `8c79e9a289fb` | 成果面 |
| 641 | `results/_p_l_v3_robustness_mistral_L60_20260917_142748.json` | 1,071 | 2026-09-17 14:27:54 | `ba41a0d4b927` | 成果面 |
| 642 | `results/_p_l_v3_robustness_qwen3_L30_20260917_140017.json` | 18,595 | 2026-09-17 14:06:45 | `e9bac1743a2a` | 成果面 |
| 643 | `results/_p_l_v3_robustness_qwen3_L60_20260917_140017.json` | 1,057 | 2026-09-17 14:06:45 | `f79f1b00e5d3` | 成果面 |
| 644 | `results/_p_l_v3_vector_embedding_doubao-text-240715_L30_20260917_172206.json` | 18,509 | 2026-09-17 17:29:03 | `2d4827f9cda2` | 成果面 |
| 645 | `results/_p_l_v3_vector_embedding_doubao-vision-241215_L30_20260917_171614.json` | 1,669,762 | 2026-09-17 17:16:46 | `2b91eb1dbbcf` | 成果面 |
| 646 | `results/_p_l_v3_vector_embedding_doubao-vision-241215_L30_20260917_172206.json` | 1,670,172 | 2026-09-17 17:53:27 | `e836a04a04d8` | 成果面 |
| 647 | `results/_p_l_v3_vector_embedding_doubao-vision-250328_L30_20260917_171614.json` | 1,670,501 | 2026-09-17 17:17:26 | `46c99397f01b` | 成果面 |
| 648 | `results/_p_l_v3_vector_embedding_doubao-vision-250328_L30_20260917_172206.json` | 1,669,285 | 2026-09-17 17:53:27 | `0432f25cf6c3` | 成果面 |
| 649 | `results/_p_l_v3_vector_embedding_doubao-vision-250615_L30_20260917_171614.json` | 1,670,027 | 2026-09-17 17:18:00 | `6b8af7d8bca9` | 成果面 |
| 650 | `results/_p_l_v3_vector_embedding_doubao-vision-250615_L30_20260917_172206.json` | 1,671,116 | 2026-09-17 17:53:28 | `710b7f291355` | 成果面 |
| 651 | `results/_p_l_v3_vector_embedding_doubao-vision-251215_L30_20260917_172206.json` | 1,670,482 | 2026-09-17 17:53:28 | `a00976c6f87b` | 成果面 |
| 652 | `results/_p_l_v3_vector_embedding_doubao_L30_20260917_142748.json` | 11,834 | 2026-09-17 14:32:56 | `b9488e2b01ae` | 成果面 |
| 653 | `results/_p_l_v3_vector_embedding_doubao_L30_20260917_170828.json` | 18,468 | 2026-09-17 17:11:53 | `198f8fe39f94` | 成果面 |
| 654 | `results/_p_l_v3_vector_embedding_glm53_L30_20260917_142748.json` | 11,833 | 2026-09-17 14:32:56 | `d91b0c5f642f` | 成果面 |
| 655 | `results/_p_l_v3_vector_embedding_mistral_L30_20260917_142748.json` | 11,835 | 2026-09-17 14:32:56 | `33d0259073dc` | 成果面 |
| 656 | `results/_p_l_v3_vector_embedding_or_bge-large_L30_20260917_162614.json` | 1,017,974 | 2026-09-17 16:27:59 | `aff028e8506c` | 成果面 |
| 657 | `results/_p_l_v3_vector_embedding_or_e5-multi_L30_20260917_162614.json` | 1,017,684 | 2026-09-17 16:28:49 | `8676b519a031` | 成果面 |
| 658 | `results/_p_l_v3_vector_embedding_or_gte-large_L30_20260917_162614.json` | 1,017,381 | 2026-09-17 16:29:34 | `07561d4d23d1` | 成果面 |
| 659 | `results/_p_l_v3_vector_embedding_or_qwen3-emb-8b_L30_20260917_162614.json` | 3,929,893 | 2026-09-17 16:27:27 | `a4bd70c02aaa` | 成果面 |
| 660 | `results/_p_l_v3_vector_embedding_qwen3-emb-4b_L30_20260917_170828.json` | 2,452,705 | 2026-09-17 17:12:34 | `1928ada51527` | 成果面 |
| 661 | `results/_p_l_v3_vector_embedding_qwen3-emb-4b_L30_20260917_172206.json` | 2,452,273 | 2026-09-17 17:53:29 | `bebee5346543` | 成果面 |
| 662 | `results/_p_l_v3_vector_embedding_qwen3_L30_20260917_142748.json` | 11,833 | 2026-09-17 14:32:56 | `26f7493f1c95` | 成果面 |
| 663 | `results/_p_l_v3_vector_embedding_v2_doubao_report_20260917_170828.md` | 17,833 | 2026-09-17 17:12:34 | `fa9cd7ffa3f2` | 成果面 |
| 664 | `results/_p_l_v3_vector_embedding_v2_doubao_report_20260917_172206.md` | 19,548 | 2026-09-17 17:55:23 | `2e3ec17259e2` | 成果面 |
| 665 | `results/_p_refresh_registration_preliminary_2026_10_10.md` | 32,780 | 2026-10-10 21:56:34 | `a3e14b508a4a` | 成果面 |
| 666 | `results/_p_refresh_s0_judgment_2026_10_10.md` | 41,449 | 2026-10-10 21:28:04 | `369173063a7c` | 成果面 |
| 667 | `results/_p_refresh_scope_judgment_2026_10_10.md` | 34,004 | 2026-10-10 23:12:55 | `44e98dc31e2b` | 成果面 |
| 668 | `results/_p_s4_1_revision_register_2026_10_09.md` | 29,961 | 2026-10-09 12:09:39 | `ad5c76111570` | 成果面 |
| 669 | `results/_pack_d_closeout_confirm_receipt_note_2026_10_01.md` | 35,223 | 2026-10-01 15:57:56 | `15c18a28080f` | 成果面 |
| 670 | `results/_pack_d_closeout_effectuation_note_2026_10_01.md` | 27,609 | 2026-10-01 15:46:18 | `97a3573e2a2d` | 成果面 |
| 671 | `results/_pack_d_closeout_register_2026_10_01.md` | 62,012 | 2026-10-01 14:54:17 | `0f1f94df75ba` | 成果面 |
| 672 | `results/_pc_d1_d3_2026_09_15.py` | 43,019 | 2026-09-15 10:58:21 | `09c7c4ddbb39` | 成果面 |
| 673 | `results/_pending_pi_items_drafts_2026_10_11.md` | 40,678 | 2026-10-11 14:44:15 | `55f469269d3d` | 成果面 |
| 674 | `results/_pending_pi_items_master_register_2026_10_09.md` | 35,258 | 2026-10-09 12:45:09 | `87ab4929477f` | 成果面 |
| 675 | `results/_pending_rulings_drafts_2026_10_11.md` | 42,775 | 2026-10-11 12:17:37 | `c8428b883029` | 成果面 |
| 676 | `results/_pending_supply_search_receipt_2026_10_08.md` | 12,595 | 2026-10-08 16:17:05 | `11bbee2bea42` | 成果面 |
| 677 | `results/_phase1_completion_judgment_2026_10_10.md` | 28,836 | 2026-10-10 19:44:53 | `6049c68f027b` | 成果面 |
| 678 | `results/_pi_card_123_adoption_and_gate_one_request_2026_10_11.md` | 13,883 | 2026-10-12 00:11:11 | `0a4b752cbc56` | 成果面 |
| 679 | `results/_pi_effectivity_declaration_register_2026_10_11.md` | 54,511 | 2026-10-11 14:22:34 | `41a82bde5190` | 成果面 |
| 680 | `results/_pi_facing_items_screen_2026_10_09.md` | 59,604 | 2026-10-09 21:53:15 | `a6d33cf318fe` | 成果面 |
| 681 | `results/_pi_give_a_class_pilot_design_2026_10_14.md` | 103,140 | 2026-10-14 01:55:34 | `5ec0638e9498` | 成果面 †141 |
| 682 | `results/_pi_pending_items_draft_package_2026_10_09.md` | 51,793 | 2026-10-09 23:42:17 | `8fa2a7a2c49d` | 成果面 |
| 683 | `results/_pre_exec_report_kimi_2026_09_30.md` | 5,677 | 2026-09-30 20:04:18 | `3e3ef9007a90` | 成果面 |
| 684 | `results/_pre_execution_report_kimi_2026_10_01.md` | 6,277 | 2026-10-01 20:59:50 | `941e1a68b2df` | 成果面 |
| 685 | `results/_probe_url_update_log_2026_09_23.md` | 5,398 | 2026-09-23 16:06:40 | `8fcdd872dc07` | 成果面 |
| 686 | `results/_protocol_version_landing_status_2026_10_09.md` | 11,562 | 2026-10-09 11:20:01 | `1d1895489d17` | 成果面 |
| 687 | `results/_proxy_signoff_execution_register_2026_10_01.md` | 20,766 | 2026-10-01 16:04:59 | `b6e5e15b70e5` | 成果面 |
| 688 | `results/_pulled_back_P_B_DISTORTION_BOUND_V0_SPEC_2026_10_13.md` | 7,126 | 2026-10-13 00:07:58 | `bb7ca9838150` | 成果面 †141 |
| 689 | `results/_q2_scope_vs_revision_judgment_2026_10_11.md` | 43,195 | 2026-10-11 01:01:21 | `b4f00e5a69c4` | 成果面 |
| 690 | `results/_q3_c1c4_l282_transposition_fix_executor_2026_10_09.py` | 64,849 | 2026-10-09 23:54:41 | `e30d4032f195` | 成果面 |
| 691 | `results/_q3_reported_value_errata_supplement_2026_10_10.md` | 12,499 | 2026-10-10 00:47:10 | `e026f20839b1` | 成果面 |
| 692 | `results/_q4_legacy_disposal_register_2026_10_01.md` | 13,336 | 2026-10-01 09:18:49 | `a8763c406d4f` | 成果面 |
| 693 | `results/_questionnaire_cards_intake_register_supplement_10_2026_10_10.md` | 84,127 | 2026-10-10 19:09:19 | `6c18d336e018` | 成果面 |
| 694 | `results/_questionnaire_cards_intake_register_supplement_11_2026_10_10.md` | 55,341 | 2026-10-10 20:19:27 | `52c97d1c11e9` | 成果面 |
| 695 | `results/_questionnaire_cards_intake_register_supplement_12_2026_10_10.md` | 121,137 | 2026-10-10 23:55:57 | `1ff6919967a7` | 成果面 |
| 696 | `results/_questionnaire_cards_intake_register_supplement_13_2026_10_11.md` | 114,253 | 2026-10-11 12:52:21 | `43e0b642f8b2` | 成果面 |
| 697 | `results/_questionnaire_cards_intake_register_supplement_14_2026_10_11.md` | 54,883 | 2026-10-11 13:35:24 | `79bc4bfe38a5` | 成果面 |
| 698 | `results/_questionnaire_cards_intake_register_supplement_15_2026_10_11.md` | 44,698 | 2026-10-11 13:47:15 | `3654c41eda64` | 成果面 |
| 699 | `results/_questionnaire_cards_intake_register_supplement_7_2026_10_10.md` | 52,602 | 2026-10-10 16:42:53 | `1fb8eac82781` | 成果面 |
| 700 | `results/_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md` | 17,517 | 2026-10-10 17:12:50 | `a651f76a6547` | 成果面 |
| 701 | `results/_questionnaire_cards_intake_register_supplement_8_2026_10_10.md` | 50,790 | 2026-10-10 17:51:27 | `29b30d845841` | 成果面 |
| 702 | `results/_questionnaire_cards_intake_register_supplement_9_2026_10_10.md` | 84,422 | 2026-10-10 18:55:53 | `b6c0b4f29152` | 成果面 |
| 703 | `results/_r1_amendment_undetermined_face_2026_10_01.md` | 45,128 | 2026-10-01 14:41:49 | `dab48b4d77c2` | 成果面 |
| 704 | `results/_r2_reference_pointer_disposition_2026_10_11.md` | 3,121 | 2026-10-11 23:19:28 | `403adec92ce1` | 成果面 |
| 705 | `results/_r2_verdict_179domain_arith_verification_2026_10_09.md` | 30,532 | 2026-10-09 21:45:26 | `511c81b96745` | 成果面 |
| 706 | `results/_r3_r4_interpretation_case_2026_10_01.md` | 64,849 | 2026-10-10 11:37:24 | `46469217883b` | 成果面 |
| 707 | `results/_r3_wording_disposition_2026_10_11.md` | 3,917 | 2026-10-11 23:19:03 | `9d381c9d95e6` | 成果面 |
| 708 | `results/_r4_convergence_2026_10_11.md` | 3,133 | 2026-10-11 23:22:31 | `678394c47724` | 成果面 |
| 709 | `results/_r5_spec_pack_retrieved_2026_10_13/鲍勃_minimax实验委托规格包_2026_10_12.md.asset.json` | 1,037 | 2026-10-14 00:29:49 | `5ca1aa500fd8` | 成果面 †141 |
| 710 | `results/_r6_disposition_2026_10_11.md` | 3,704 | 2026-10-11 23:19:12 | `cc51203fe8f5` | 成果面 |
| 711 | `results/_r_pair_interval_statement_errata_2026_10_09.md` | 9,259 | 2026-10-09 22:43:07 | `61944eb91b72` | 成果面 |
| 712 | `results/_r_pair_nonportrait_full_document_review_2026_10_09.md` | 28,176 | 2026-10-09 22:32:22 | `d8d5e4d2154f` | 成果面 |
| 713 | `results/_r_pair_rp3b_rp2_rpq6_judgments_2026_10_09.md` | 23,975 | 2026-10-09 22:42:46 | `5faa16446171` | 成果面 |
| 714 | `results/_r_pair_texts_independent_review_2026_10_09.md` | 35,443 | 2026-10-09 17:43:25 | `8c5f83c3c4cf` | 成果面 |
| 715 | `results/_reading_face_basis_rejudge_2026_10_10.md` | 24,208 | 2026-10-10 03:13:46 | `3fe193a2a01f` | 成果面 |
| 716 | `results/_readme_proper_batch_recheck_register_2026_09_30.md` | 20,781 | 2026-09-30 17:13:36 | `2e530923457e` | 成果面 |
| 717 | `results/_receipt_disposition_register_2026_10_08.md` | 23,050 | 2026-10-08 17:25:43 | `a79c3b82ee01` | 成果面 |
| 718 | `results/_refcheck_hash_change_reference_recheck_2026_09_30.md` | 33,625 | 2026-09-30 22:57:31 | `f011c29944b9` | 成果面 |
| 719 | `results/_register3_bytes_erratum_2026_10_11.md` | 13,294 | 2026-10-11 12:32:09 | `f9f6805a7b76` | 成果面 |
| 720 | `results/_registry_lag_correction_batch_2026_10_01.md` | 36,367 | 2026-10-01 10:08:43 | `5b86fbf0cbbd` | 成果面 |
| 721 | `results/_remote_residual_disposal_execution_order_2026_10_08.md` | 36,486 | 2026-10-08 17:06:56 | `602c4d09623d` | 成果面 |
| 722 | `results/_round19_followup_round21_22_approvals_effect_register_2026_10_10.md` | 54,850 | 2026-10-10 00:31:15 | `0c8dba07dd1e` | 成果面 |
| 723 | `results/_round20_approvals_effect_register_2026_10_10.md` | 27,711 | 2026-10-10 00:24:02 | `29d737c59e8b` | 成果面 |
| 724 | `results/_round23_26_threshold_review_effect_register_2026_10_10.md` | 47,297 | 2026-10-10 01:15:09 | `9b0c62765576` | 成果面 |
| 725 | `results/_round27_34_approvals_effect_register_2026_10_10.md` | 73,226 | 2026-10-10 11:02:09 | `d0bc0b1a9ae0` | 成果面 |
| 726 | `results/_round45_dispositions_effect_register_2026_10_10.md` | 19,803 | 2026-10-10 14:11:43 | `d66a1076952a` | 成果面 |
| 727 | `results/_round51_effectivity_register_2026_10_10.md` | 27,070 | 2026-10-10 16:04:24 | `b8b0c52296b2` | 成果面 |
| 728 | `results/_round52_e6b_caliber_naming_effectivity_register_2026_10_10.md` | 21,788 | 2026-10-10 16:34:00 | `e861c7bc19ad` | 成果面 |
| 729 | `results/_round52_s4_e4b_ad5_type_effectivity_register_2026_10_10.md` | 45,351 | 2026-10-10 16:31:38 | `debd88fc150c` | 成果面 |
| 730 | `results/_round53_rejudge_prereg_freeze_effectivity_register_2026_10_10.md` | 25,637 | 2026-10-10 17:10:04 | `b27814792394` | 成果面 |
| 731 | `results/_round53_th_v3_19_landfall_schema_effectivity_register_2026_10_10.md` | 20,023 | 2026-10-10 17:11:26 | `4c3a6dc0070d` | 成果面 |
| 732 | `results/_round54_g5_dispositions_register_2026_10_10.md` | 39,977 | 2026-10-10 17:42:45 | `afc67818bb85` | 成果面 |
| 733 | `results/_round55_dispositions_register_2026_10_10.md` | 34,913 | 2026-10-10 18:12:53 | `002fa0a9a5e4` | 成果面 |
| 734 | `results/_round56_ad8fix_effectivity_register_2026_10_10.md` | 16,553 | 2026-10-10 18:12:36 | `2e7f86314428` | 成果面 |
| 735 | `results/_round56_b01_followup_disposition_plan_2026_10_10.md` | 31,004 | 2026-10-10 20:29:17 | `857fb940a43c` | 成果面 |
| 736 | `results/_round56_direct_adoptions_register_2026_10_10.md` | 43,240 | 2026-10-10 19:06:22 | `e3c56c5d0a97` | 成果面 |
| 737 | `results/_round56_direct_adoptions_register_2_2026_10_10.md` | 26,690 | 2026-10-10 20:15:55 | `f8e0fa28c067` | 成果面 |
| 738 | `results/_round56_g2_enable_and_v1_rule_register_2026_10_10.md` | 34,181 | 2026-10-10 19:13:12 | `936f551f0fd3` | 成果面 |
| 739 | `results/_round56_gu_backdoor_exclusion_revision_2026_10_10.md` | 25,045 | 2026-10-10 19:11:29 | `52d3b10a16a0` | 成果面 |
| 740 | `results/_round56_idx_sc1_resolution_2026_10_10.md` | 47,107 | 2026-10-10 19:27:46 | `9b41f2a38b2f` | 成果面 |
| 741 | `results/_round56_idx_sc1_temp_deletion_deviation_note_2026_10_10.md` | 8,181 | 2026-10-10 19:55:10 | `c72086990450` | 成果面 |
| 742 | `results/_round56_n10_erratum_register_2026_10_10.md` | 20,321 | 2026-10-10 18:49:02 | `599d0450434e` | 成果面 |
| 743 | `results/_round56_pending_questions_compilation_2026_10_10.md` | 33,504 | 2026-10-10 18:17:26 | `ef09b3d28a0f` | 成果面 |
| 744 | `results/_round56_pending_questions_compilation_supplement_note_2026_10_10.md` | 29,019 | 2026-10-10 18:40:21 | `421c936f6ae8` | 成果面 |
| 745 | `results/_round56_registration_supplement_2026_10_10.md` | 21,865 | 2026-10-10 21:37:33 | `71a59735302c` | 成果面 |
| 746 | `results/_round56_review_effectivity_register_2026_10_10.md` | 49,013 | 2026-10-10 21:36:54 | `da6b55162e50` | 成果面 |
| 747 | `results/_round56_review_effectivity_register_3_2026_10_10.md` | 77,181 | 2026-10-10 23:50:47 | `84ed13256250` | 成果面 |
| 748 | `results/_round56_review_effectivity_register_4_2026_10_11.md` | 46,908 | 2026-10-11 00:23:15 | `ee31bb8a94fe` | 成果面 |
| 749 | `results/_round56_review_effectivity_register_5_2026_10_11.md` | 67,613 | 2026-10-11 01:04:02 | `5deba7d27bb1` | 成果面 |
| 750 | `results/_round56_review_effectivity_register_6_2026_10_11.md` | 58,478 | 2026-10-11 01:37:31 | `2f3255ea344f` | 成果面 |
| 751 | `results/_round56_sc4_nstar_inconsistency_erratum_2026_10_10.md` | 16,640 | 2026-10-10 18:11:58 | `af4c3335538a` | 成果面 |
| 752 | `results/_round56_shortname_backfill_note_2026_10_10.md` | 22,195 | 2026-10-10 19:07:14 | `bb2444cccd65` | 成果面 |
| 753 | `results/_round56_terminal_boundary_effectivity_register_2026_10_10.md` | 35,878 | 2026-10-10 18:48:25 | `d5bf826278cb` | 成果面 |
| 754 | `results/_round56_th3_coverage_line_effectivity_register_2026_10_10.md` | 28,378 | 2026-10-10 18:49:59 | `6794fb09ce7e` | 成果面 |
| 755 | `results/_round56_th4_two_field_reporting_resolution_2026_10_10.md` | 28,233 | 2026-10-10 18:50:57 | `71894a686e92` | 成果面 |
| 756 | `results/_round56_typeb_backfill_register_2026_10_10.md` | 40,253 | 2026-10-10 21:24:40 | `607ded06d840` | 成果面 |
| 757 | `results/_round56_typeb_form_draft_2026_10_10.md` | 50,170 | 2026-10-10 20:18:30 | `582c5fb9970c` | 成果面 |
| 758 | `results/_round56_typeb_implementation_register_2026_10_10.md` | 26,367 | 2026-10-10 19:08:08 | `c296a7833a70` | 成果面 |
| 759 | `results/_round56_v4_kd_row_correction_revision_2026_10_10.md` | 23,453 | 2026-10-10 19:12:12 | `6d8537cb127f` | 成果面 |
| 760 | `results/_round56a_dispositions_register_2026_10_10.md` | 50,365 | 2026-10-10 18:33:00 | `d8980cfae7f7` | 成果面 |
| 761 | `results/_round56c_card_id_erratum_2026_10_10.md` | 18,747 | 2026-10-10 19:05:04 | `f6c2d40f18ff` | 成果面 |
| 762 | `results/_round56c_d23_ad5_judgment_2026_10_10.md` | 50,747 | 2026-10-10 18:36:42 | `061813859345` | 成果面 |
| 763 | `results/_round56r8_dispositions_register_2026_10_10.md` | 46,135 | 2026-10-10 18:57:58 | `cfb08d0e15f4` | 成果面 |
| 764 | `results/_round56r9r10_dispositions_register_2026_10_10.md` | 49,754 | 2026-10-10 19:57:04 | `0eb408ae60f5` | 成果面 |
| 765 | `results/_rpq_wordlist_and_t1p2_judgments_2026_10_09.md` | 44,796 | 2026-10-09 23:30:07 | `246ce35c4ddc` | 成果面 |
| 766 | `results/_s1prime_trigger_caliber_reevaluation_2026_10_10.md` | 29,991 | 2026-10-10 23:51:48 | `d2326973aaf8` | 成果面 |
| 767 | `results/_s2prime_krj3_applicability_recheck_2026_10_10.md` | 41,322 | 2026-10-11 00:02:57 | `10518510b628` | 成果面 |
| 768 | `results/_s3_c4_recount_2026_10_01.md` | 32,025 | 2026-10-01 11:15:06 | `86af4c109519` | 成果面 |
| 769 | `results/_s3_closeout_rules_case_2026_10_01.md` | 52,659 | 2026-10-01 11:55:45 | `7e622691aec1` | 成果面 |
| 770 | `results/_s3_d1_rulings_supplement_register_2026_10_01.md` | 28,762 | 2026-10-14 14:07:09 | `303bf7c6f34d` | 成果面 |
| 771 | `results/_s3_f1_loader_fix_recompute_2026_10_08.md` | 22,065 | 2026-10-08 17:00:38 | `b2c9840d237b` | 成果面 |
| 772 | `results/_s3_kv3s_3_verdict_2026_10_01.md` | 35,037 | 2026-10-10 11:37:23 | `e394bb6b5ddf` | 成果面 |
| 773 | `results/_s3_missing_field_backfill_rule_draft_2026_10_01.md` | 35,827 | 2026-10-10 11:37:24 | `8496a53d183a` | 成果面 |
| 774 | `results/_s3_missing_field_backfill_rule_effective_2026_10_01.md` | 52,469 | 2026-10-10 11:37:24 | `1450057b0819` | 成果面 |
| 775 | `results/_s3prime_recompute_after_supplement_2026_10_11.md` | 41,708 | 2026-10-11 00:59:13 | `fa025e4dc166` | 成果面 |
| 776 | `results/_s4_abcreadings_reproducibility_check_2026_10_10.md` | 25,234 | 2026-10-10 12:27:42 | `892e5dfe3ed1` | 成果面 |
| 777 | `results/_s4_bc_construction_ruling_2026_10_09.md` | 30,257 | 2026-10-09 23:22:00 | `e2fdb380cd3c` | 成果面 |
| 778 | `results/_s4_chain_clearance_register_2026_10_09.md` | 2,684 | 2026-10-09 14:52:20 | `eda3d304d381` | 成果面 |
| 779 | `results/_s4_corpus_scope_hard_constraint_judgment_2026_10_10.md` | 44,199 | 2026-10-10 17:50:47 | `c7609657dfe4` | 成果面 |
| 780 | `results/_s4_dkb_backfill_register_2026_10_10.md` | 25,591 | 2026-10-10 10:26:50 | `3a992c3fe235` | 成果面 |
| 781 | `results/_s4_e4_axis_disposition_axis2_run_2026_10_10.md` | 29,700 | 2026-10-10 15:05:02 | `2bda07af86fc` | 成果面 |
| 782 | `results/_s4_e4b_ad5_type_separate_judgment_2026_10_10.md` | 51,898 | 2026-10-10 15:44:56 | `f48601fee958` | 成果面 |
| 783 | `results/_s4_empty_sequence_backfill_assessment_2026_10_10.md` | 28,771 | 2026-10-10 00:40:54 | `41b75ffea7be` | 成果面 |
| 784 | `results/_s4_face_closeout_2026_10_09.md` | 29,158 | 2026-10-09 23:49:50 | `f7d76eda2911` | 成果面 |
| 785 | `results/_s4_face_dual_files_verification_2026_10_09.md` | 40,228 | 2026-10-09 16:57:36 | `cc3fc6eebc6b` | 成果面 |
| 786 | `results/_s4_face_five_lines_ci_readings_2026_10_09.md` | 39,462 | 2026-10-09 21:15:30 | `bea9bc43a8f3` | 成果面 |
| 787 | `results/_s4_feature_surface_v3_1_definition_2026_10_10.md` | 30,310 | 2026-10-10 11:10:18 | `d044ce1c069d` | 成果面 |
| 788 | `results/_s4_final_ruling_card_register_2026_10_09.md` | 2,135 | 2026-10-09 15:09:52 | `f62401b619cc` | 成果面 |
| 789 | `results/_s4_heldout_sampling_seed42_items_register_2026_10_09.md` | 34,689 | 2026-10-09 22:11:08 | `73a02ac5937d` | 成果面 |
| 790 | `results/_s4_heldout_sampling_seed42_register_2026_10_09.md` | 37,615 | 2026-10-09 21:11:25 | `2a2ad5c2e29f` | 成果面 |
| 791 | `results/_s4_heldout_sampling_seed42_sets_2026_10_09.json` | 59,100 | 2026-10-09 21:07:05 | `8dfc9e0d8bf9` | 成果面 |
| 792 | `results/_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` | 19,003 | 2026-10-12 23:53:11 | `cd4f1e7b4879` | 成果面 |
| 793 | `results/_s4_heldout_sampling_seedthird_extractor_2026_10_11.py` | 52,785 | 2026-10-12 23:53:15 | `8ae074194a3d` | 成果面 |
| 794 | `results/_s4_heldout_seedprime_verification_2026_10_10.md` | 21,966 | 2026-10-10 23:21:06 | `8c64314d0ec0` | 成果面 |
| 795 | `results/_s4_keyword_expansion_and_regen_design_2026_10_10.md` | 31,149 | 2026-10-10 01:11:17 | `6efddab54ca5` | 成果面 |
| 796 | `results/_s4_reading_surface_and_authority_register_2026_10_09.md` | 34,405 | 2026-10-09 09:28:19 | `0148b5271154` | 成果面 |
| 797 | `results/_s4_regen_traceability_judgment_2026_10_10.md` | 36,071 | 2026-10-10 09:44:42 | `a330273b981c` | 成果面 |
| 798 | `results/_s4_revision_effectiveness_register_2026_10_09.md` | 32,820 | 2026-10-09 14:47:44 | `356fe8509669` | 成果面 |
| 799 | `results/_s4_terminal_face_recompute_2026_10_09.md` | 46,701 | 2026-10-09 17:08:17 | `b412342eabec` | 成果面 |
| 800 | `results/_s4_topup_intake_verdict_2026_10_09.md` | 33,799 | 2026-10-09 14:04:40 | `658d7f3ab231` | 成果面 |
| 801 | `results/_s4_tree_construct_adjustment_exec_2026_10_10.md` | 28,515 | 2026-10-10 09:55:59 | `b6b47008f8fd` | 成果面 |
| 802 | `results/_s4_tree_prereg_revision_2026_10_10.md` | 30,382 | 2026-10-10 10:48:57 | `037140972829` | 成果面 |
| 803 | `results/_s4_v11_axis2_displacement_items_2026_10_10.json` | 9,941 | 2026-10-10 15:04:30 | `0eed9053619c` | 成果面 |
| 804 | `results/_s4_v31_displacement_register_face2_2026_10_10.md` | 17,736 | 2026-10-10 13:57:19 | `b6ce4a79116e` | 成果面 |
| 805 | `results/_s4_v31_exec_section8_errata_2026_10_10.md` | 23,250 | 2026-10-10 14:42:11 | `ec11aec2380d` | 成果面 |
| 806 | `results/_s4_w1_3636_consistency_check_2026_10_10.md` | 29,196 | 2026-10-10 14:15:28 | `0e9ae4b6ee8c` | 成果面 |
| 807 | `results/_s4_w2_disposition_registration_2026_10_10.md` | 23,545 | 2026-10-10 14:59:02 | `566c2f0ad7e8` | 成果面 |
| 808 | `results/_s4_w2_e4_separate_judgment_2026_10_10.md` | 37,607 | 2026-10-10 14:36:06 | `a51bd6530075` | 成果面 |
| 809 | `results/_s4_w2bc_effect_registration_2026_10_10.md` | 26,418 | 2026-10-10 15:36:26 | `b24a8411a260` | 成果面 |
| 810 | `results/_s4prime_five_lines_readings_2026_10_11.md` | 23,877 | 2026-10-11 01:21:28 | `e91e7f52c726` | 成果面 |
| 811 | `results/_s4prime_readings_runner_2026_10_11.py` | 23,870 | 2026-10-12 16:33:48 | `52bb6e3bba15` | 成果面 |
| 812 | `results/_s4q04_level_attribution_judgment_2026_10_10.md` | 26,407 | 2026-10-10 13:20:41 | `49a07216a1bb` | 成果面 |
| 813 | `results/_s5doubleprime_five_lines_runner_2026_10_11.py` | 31,232 | 2026-10-13 00:17:00 | `2d8cf387b478` | 成果面 |
| 814 | `results/_s5dp_mixed_object_erratum_2026_10_11.md` | 8,380 | 2026-10-11 20:36:49 | `07cde000e66f` | 成果面 |
| 815 | `results/_s5prime_double_lim_a_and_item_registers_2026_10_11.md` | 58,378 | 2026-10-11 20:43:15 | `9a62fb2a6956` | 成果面 |
| 816 | `results/_s5prime_lim_a_and_item_registers_2026_10_11.md` | 47,225 | 2026-10-11 01:38:02 | `fa74831fa0ad` | 成果面 |
| 817 | `results/_s6doubleprime_terminal_verdicts_2026_10_11.md` | 76,910 | 2026-10-11 17:10:58 | `bba3b889d849` | 成果面 |
| 818 | `results/_s6doubleprime_verdict_supplement_2026_10_11.md` | 31,515 | 2026-10-11 17:38:34 | `8e19c10ce219` | 成果面 |
| 819 | `results/_s6prime_terminal_verdicts_2026_10_11.md` | 54,937 | 2026-10-11 12:36:08 | `1c8ce58d6484` | 成果面 |
| 820 | `results/_s7doubleprime_verification_2026_10_11.md` | 41,680 | 2026-10-11 17:27:15 | `06ac684b4923` | 成果面 |
| 821 | `results/_s7doubleprime_verification_erratum_2026_10_11.md` | 32,822 | 2026-10-11 17:39:50 | `9ff40693e4ac` | 成果面 |
| 822 | `results/_s7prime_findings_erratum_2026_10_11.md` | 31,008 | 2026-10-11 13:38:58 | `a7dfa8e789b7` | 成果面 |
| 823 | `results/_s7prime_prereq_and_verification_2026_10_11.md` | 36,787 | 2026-10-11 12:59:14 | `e44da4b83810` | 成果面 |
| 824 | `results/_seed_double_criterion_draft_2026_10_11.md` | 40,499 | 2026-10-11 14:21:47 | `025212e91546` | 成果面 |
| 825 | `results/_seed_double_identifier_final_judgment_2026_10_11.md` | 50,222 | 2026-10-11 15:02:43 | `728d18391748` | 成果面 |
| 826 | `results/_seed_double_rule_judgment_2026_10_11.md` | 57,185 | 2026-10-11 14:02:53 | `f70a689fd8c1` | 成果面 |
| 827 | `results/_seven_gap_closures_adoption_register_2026_10_11.md` | 11,960 | 2026-10-12 00:02:59 | `ac3c41663f84` | 成果面 |
| 828 | `results/_skill_cache_inventory_and_reference_update_advice_2026_09_30.md` | 31,692 | 2026-09-30 15:32:36 | `c14489750416` | 成果面 |
| 829 | `results/_skill_call_surface_probe_2026_09_30.md` | 32,261 | 2026-09-30 16:52:00 | `112346df64fb` | 成果面 |
| 830 | `results/_skill_call_surface_probe_supplement_a_2026_09_30.md` | 50,658 | 2026-09-30 17:25:29 | `a06316c3c7f2` | 成果面 |
| 831 | `results/_skill_call_surface_probe_supplement_b_2026_09_30.md` | 82,744 | 2026-09-30 17:36:35 | `69d311e6a4c7` | 成果面 |
| 832 | `results/_skill_directory_update_and_addressing_rule_2026_10_01.md` | 20,335 | 2026-10-01 10:26:01 | `4a3a2d0c5b95` | 成果面 |
| 833 | `results/_skill_erratum_and_parent_success_note_2026_09_30.md` | 24,143 | 2026-09-30 16:16:31 | `7a64949402d9` | 成果面 |
| 834 | `results/_skill_load_failure_window_readonly_facts_2026_09_30.md` | 23,065 | 2026-09-30 16:16:36 | `9f5b73620b8a` | 成果面 |
| 835 | `results/_skill_reference_erratum_and_runtime_anchor_experiment_2026_09_30.md` | 30,771 | 2026-09-30 17:25:45 | `16861e71305f` | 成果面 |
| 836 | `results/_stage1_tail_caliber_unification_register_2026_10_11.md` | 41,140 | 2026-10-11 14:41:24 | `d486ec491e8e` | 成果面 |
| 837 | `results/_stage2_trae_reply_acceptance_register_2026_10_12.md` | 14,874 | 2026-10-12 01:39:16 | `ce0b5a64cfce` | 成果面 |
| 838 | `results/_stage3_extraction_verification_2026_10_11.md` | 22,399 | 2026-10-11 16:56:21 | `f973e6d737c3` | 成果面 |
| 839 | `results/_stage3_open_and_mandate_register_2026_10_12.md` | 13,865 | 2026-10-12 01:54:54 | `1b0a109a7914` | 成果面 |
| 840 | `results/_stage3_readings_verification_2026_10_11.md` | 29,956 | 2026-10-11 17:13:11 | `023a0cdd3350` | 成果面 |
| 841 | `results/_stage3_trigger_readings_2026_10_11.md` | 35,711 | 2026-10-11 16:56:23 | `2900948bca6d` | 成果面 |
| 842 | `results/_sub_artifact_ledger_history_r5_2026_10_01.md` | 35,845 | 2026-10-01 10:15:04 | `372a53b9e832` | 成果面 |
| 843 | `results/_sub_transfer_candidates_2026_10_01.md` | 21,796 | 2026-10-01 19:35:10 | `2f61c0aa2a2b` | 成果面 |
| 844 | `results/_sub_transfer_execution_register_2026_10_01.md` | 13,377 | 2026-10-01 19:45:58 | `c41013a975e0` | 成果面 |
| 845 | `results/_sub_transfer_wave2_register_2026_10_01.md` | 14,286 | 2026-10-01 19:57:08 | `265b03ea493a` | 成果面 |
| 846 | `results/_sub_transfer_wave3_register_2026_10_01.md` | 14,419 | 2026-10-01 20:33:47 | `cd80b993f497` | 成果面 |
| 847 | `results/_suspect17_release_move_register_2026_10_09.md` | 22,351 | 2026-10-09 09:47:38 | `9a4d40bfcdc3` | 成果面 |
| 848 | `results/_t1_7_2_correction_2026_10_08.md` | 16,469 | 2026-10-10 11:37:23 | `d90bf82338f6` | 成果面 |
| 849 | `results/_t1_d7_reading_line_judgment_2026_10_10.md` | 28,559 | 2026-10-10 00:18:41 | `60bd9ae98640` | 成果面 |
| 850 | `results/_t1_exp2_exec_register_2026_10_09.md` | 18,597 | 2026-10-10 02:34:26 | `3a08dcfa8c7f` | 成果面 |
| 851 | `results/_t1_exp2_verdict_2026_10_10.md` | 48,298 | 2026-10-10 02:47:15 | `15c1c4b317a0` | 成果面 |
| 852 | `results/_t1_exp2_verdict_bytes_correction_2026_10_10.md` | 13,480 | 2026-10-10 10:29:40 | `e863ca5fb157` | 成果面 |
| 853 | `results/_t1_gate_closure_and_recompute_verdict_2026_10_01.md` | 72,934 | 2026-10-14 14:07:09 | `16ef897639c4` | 成果面 |
| 854 | `results/_t1_gate_revision_draft_2026_10_09.md` | 27,452 | 2026-10-09 21:17:22 | `50e8b2440346` | 成果面 |
| 855 | `results/_t1_gate_revision_formal_2026_10_09.md` | 35,658 | 2026-10-09 22:21:20 | `0e0cb002c5de` | 成果面 |
| 856 | `results/_t1_o1_design_axis_exemption_judgment_2026_10_09.md` | 17,073 | 2026-10-09 17:09:36 | `a27c7f411de5` | 成果面 |
| 857 | `results/_t1_p2_aggregation_caliber_judgment_2026_10_09.md` | 14,397 | 2026-10-09 17:08:31 | `02f44f5bf2dd` | 成果面 |
| 858 | `results/_t1_pairing_caliber_ruling_2026_10_09.md` | 21,346 | 2026-10-09 21:56:51 | `2ded8091114a` | 成果面 |
| 859 | `results/_t1_r2_d1_field_caliber_correction_2026_10_09.md` | 25,396 | 2026-10-09 21:28:08 | `99cafda125f1` | 成果面 |
| 860 | `results/_t1_temp_axis_retirement_consolidation_2026_10_10.md` | 20,308 | 2026-10-10 10:51:31 | `40cb2e81425a` | 成果面 |
| 861 | `results/_t1_temp_axis_retirement_judgment_2026_10_10.md` | 27,384 | 2026-10-10 09:43:25 | `19afc7e191a7` | 成果面 |
| 862 | `results/_t1p2_enable_judgment_2026_10_10.md` | 20,132 | 2026-10-10 00:30:13 | `1e97d06b6ec9` | 成果面 |
| 863 | `results/_t1p2_escalation_judgment_2026_10_10.md` | 22,930 | 2026-10-10 00:30:53 | `5f43775a3224` | 成果面 |
| 864 | `results/_t1p2_judgment_bytes_correction_2026_10_10.md` | 6,377 | 2026-10-10 00:31:40 | `d9d29bec3a0b` | 成果面 |
| 865 | `results/_test_conv_out.txt` | 7,568 | 2026-09-26 17:16:43 | `6effe5ef7ae6` | 成果面 |
| 866 | `results/_th_id_miscitation_correction_2026_10_09.md` | 10,468 | 2026-10-09 16:43:24 | `b61321ba3b6e` | 成果面 |
| 867 | `results/_theory_boundary_clone_sync_register_2026_10_09.md` | 17,528 | 2026-10-09 09:47:13 | `1f9fd007649c` | 成果面 |
| 868 | `results/_theory_input_request_supplement_2026_09_29.md` | 48,190 | 2026-09-30 20:27:38 | `c966e7b605af` | 成果面 |
| 869 | `results/_three_pending_items_drafts_2026_10_11.md` | 51,748 | 2026-10-11 21:55:16 | `8995859e5a76` | 成果面 |
| 870 | `results/_three_pending_items_effectivity_2026_10_11.md` | 16,744 | 2026-10-11 22:05:39 | `df1f5f75c7a0` | 成果面 |
| 871 | `results/_three_state_standard_repeal_register_2026_10_10.md` | 18,364 | 2026-10-10 14:44:36 | `8503708c73bf` | 成果面 |
| 872 | `results/_thv3_15_parallel_seed_double_note_2026_10_11.md` | 15,569 | 2026-10-11 15:17:29 | `3cd92287059e` | 成果面 |
| 873 | `results/_tidy_round2_archive_transfer_register_2026_09_30.md` | 27,641 | 2026-09-30 19:20:01 | `1c1365f23c92` | 成果面 |
| 874 | `results/_tmp_disposal_register_2026_10_10.md` | 20,812 | 2026-10-10 12:00:12 | `e0f6b744e826` | 成果面 |
| 875 | `results/_tra_v0_2026_09_10.json` | 3,695 | 2026-09-10 20:20:34 | `0b096048e01d` | 成果面 |
| 876 | `results/_track2_endpoints_probe_2026_09_23.json` | 5,803 | 2026-09-23 15:15:30 | `c846f7fc79ee` | 成果面 |
| 877 | `results/_track2_qwen_check_2026_09_23.json` | 2,513 | 2026-09-23 14:22:00 | `727d1ffc7f3f` | 成果面 |
| 878 | `results/_track2_qwen_check_2026_09_23.py` | 12,078 | 2026-09-23 14:21:43 | `3ddba570c221` | 成果面 |
| 879 | `results/_trigger_denominator_caliber_judgment_2026_10_11.md` | 43,448 | 2026-10-11 00:12:10 | `16bf9332deef` | 成果面 |
| 880 | `results/_trj_w1_downstream_erratum_2026_10_10.md` | 24,888 | 2026-10-10 18:41:15 | `e52d0016fbc6` | 成果面 |
| 881 | `results/_trj_w1_verification_2026_10_10.md` | 23,014 | 2026-10-10 18:33:08 | `cc6de8e981f6` | 成果面 |
| 882 | `results/_typeb_m_caliber_2026_10_10.md` | 32,830 | 2026-10-10 23:30:45 | `4d067a884c6c` | 成果面 |
| 883 | `results/_typeb_m_definition_judgment_2026_10_10.md` | 41,432 | 2026-10-10 23:15:39 | `97ac7fcc4803` | 成果面 |
| 884 | `results/_typeb_m_registration_2026_10_10.md` | 27,778 | 2026-10-10 23:32:32 | `3b68d3890473` | 成果面 |
| 885 | `results/_u04_1_exemption_precondition_verification_2026_10_09.md` | 21,377 | 2026-10-09 17:26:27 | `c072ffe6110e` | 成果面 |
| 886 | `results/_u11_execution_register_2026_10_09.md` | 24,549 | 2026-10-10 11:37:24 | `8bc087a16f5a` | 成果面 |
| 887 | `results/_u2u3_effectivity_register_2026_10_10.md` | 27,192 | 2026-10-10 13:49:44 | `b00b87cec825` | 成果面 |
| 888 | `results/_u3_carrier_qid_verification_2026_10_11.md` | 21,572 | 2026-10-11 21:31:55 | `6509ae68f778` | 成果面 |
| 889 | `results/_u5_fingerprint_relocation_erratum_2026_10_10.md` | 24,999 | 2026-10-10 15:25:33 | `200c7e4c57cb` | 成果面 |
| 890 | `results/_u5b_citation_surface_revision_2026_10_10.md` | 50,079 | 2026-10-10 16:06:18 | `5cc29c53a422` | 成果面 |
| 891 | `results/_u5b_p_counting_resolution_2026_10_10.md` | 20,086 | 2026-10-10 18:44:20 | `e12e9d9a32c4` | 成果面 |
| 892 | `results/_u6_negative_delta_compatibility_2026_10_11.md` | 20,969 | 2026-10-11 21:35:16 | `1846e917119f` | 成果面 |
| 893 | `results/_u_cf_category_caliber_2026_10_10.md` | 18,976 | 2026-10-10 23:29:45 | `73f181d76169` | 成果面 |
| 894 | `results/_u_cf_reclassification_2026_10_10.md` | 25,698 | 2026-10-10 23:30:49 | `02f910e8795b` | 成果面 |
| 895 | `results/_u_closure_execution_register_2026_10_09.md` | 12,781 | 2026-10-09 09:38:19 | `cbf0c9503284` | 成果面 |
| 896 | `results/_u_r_numbering_attribution_2026_10_11.md` | 5,331 | 2026-10-11 23:21:55 | `53672c23d7f9` | 成果面 |
| 897 | `results/_u_v04_01_criterion_scope_determination_2026_10_01.md` | 27,079 | 2026-10-01 11:05:37 | `e82609024b59` | 成果面 |
| 898 | `results/_unclosed_items_inventory_2026_10_08.md` | 30,219 | 2026-10-08 16:28:20 | `b0e7c74e951e` | 成果面 |
| 899 | `results/_upload_execution_receipt_kimi_2026_09_26.md` | 4,191 | 2026-09-26 22:08:26 | `b4ac31f917f3` | 成果面 |
| 900 | `results/_upload_execution_receipt_kimi_2026_09_30.md` | 4,159 | 2026-09-30 20:21:45 | `20e1f592ca61` | 成果面 |
| 901 | `results/_upload_execution_receipt_kimi_2026_10_01.md` | 4,581 | 2026-10-01 21:06:04 | `a9a9a1d19661` | 成果面 |
| 902 | `results/_upload_guard_mirror_pair_2026_10_08.md` | 23,534 | 2026-10-08 17:11:17 | `d923371cdbce` | 成果面 |
| 903 | `results/_upload_ledger_kimi_2026_09_30.json` | 218,279 | 2026-09-30 20:21:46 | `b17cb8aae62d` | 成果面 |
| 904 | `results/_upload_ledger_kimi_2026_10_01.json` | 43,275 | 2026-10-01 21:06:04 | `79a0fb18683b` | 成果面 |
| 905 | `results/_uv04_field_completeness_fill_2026_10_01.md` | 28,735 | 2026-10-01 14:19:04 | `eb9b8d185f44` | 成果面 |
| 906 | `results/_v2_setup.py` | 3,483 | 2026-09-16 11:01:12 | `73f2b8712a90` | 成果面 |
| 907 | `results/_v2_show_summary.py` | 1,200 | 2026-09-11 11:21:58 | `0012b38ce438` | 成果面 |
| 908 | `results/_v2_smoketest.py` | 2,040 | 2026-09-16 11:01:12 | `0b6c22c8f379` | 成果面 |
| 909 | `results/_v2_stage1_60cells.py` | 31,556 | 2026-09-16 11:01:12 | `8c7bd12c3a8c` | 成果面 |
| 910 | `results/_v2_stage2_f2_drift.py` | 10,798 | 2026-09-16 11:01:12 | `7e9b2fc57d80` | 成果面 |
| 911 | `results/_v2_stage3_f3_strip.py` | 11,803 | 2026-09-16 11:01:12 | `ce4362e325ca` | 成果面 |
| 912 | `results/_v2_stage4_f4_pdv2.py` | 10,355 | 2026-09-11 11:17:17 | `b84f5aab6faf` | 成果面 |
| 913 | `results/_v2_stage5_f5_dpath.py` | 6,480 | 2026-09-11 11:16:38 | `e8871b829d89` | 成果面 |
| 914 | `results/_v2_verify_outputs.py` | 2,656 | 2026-09-11 11:21:39 | `eb0107dd79b5` | 成果面 |
| 915 | `results/_v3_02_ethard_closure_verdict_2026_10_09.md` | 27,819 | 2026-10-09 14:03:16 | `aa0f96bb618f` | 成果面 |
| 916 | `results/_v3_02_ethard_execution_register_2026_10_09.md` | 22,007 | 2026-10-09 13:43:03 | `23457f5ce432` | 成果面 |
| 917 | `results/_v3_02_override_register_2026_10_09.md` | 36,245 | 2026-10-09 13:33:36 | `c5441e186c3f` | 成果面 |
| 918 | `results/_v3_05_h_caliber_judgment_2026_10_09.md` | 22,050 | 2026-10-09 22:58:01 | `1c2b5f40e15d` | 成果面 |
| 919 | `results/_v3_recheck_05_executor_2026_09_28.py` | 38,733 | 2026-10-12 23:53:11 | `65f8a7514f34` | 成果面 |
| 920 | `results/_v3_recheck_10_executor_2026_09_27.py` | 33,647 | 2026-09-27 15:12:15 | `80947906e592` | 成果面 |
| 921 | `results/_v3_recheck_12_executor_2026_09_27.py` | 49,430 | 2026-09-27 16:00:42 | `4850b1cbb010` | 成果面 |
| 922 | `results/_v3_recheck_12_jsv_phase_data_2026_09_27.json` | 17,718 | 2026-09-27 16:20:32 | `642582d4fbd1` | 成果面 |
| 923 | `results/_v3_recheck_19_executor_2026_09_27.py` | 19,215 | 2026-09-27 14:55:27 | `b133a631b1a8` | 成果面 |
| 924 | `results/_v3_recheck_26b_verdict_2026_10_01.md` | 26,309 | 2026-10-01 09:03:39 | `8bbecb15b28b` | 成果面 |
| 925 | `results/_v3_recheck_27_executor_2026_09_27.py` | 34,084 | 2026-09-27 15:17:40 | `190cbe01d061` | 成果面 |
| 926 | `results/_v3_recheck_28_executor_2026_09_27.py` | 17,735 | 2026-09-27 14:47:05 | `4e8c0dd8f54f` | 成果面 |
| 927 | `results/_v3_recheck_prereg_v1p2_2026_09_29.md` | 25,854 | 2026-09-29 18:34:16 | `a667a5f69b7a` | 成果面 |
| 928 | `results/_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md` | 23,152 | 2026-09-24 20:04:58 | `c64146c4ccac` | 成果面 |
| 929 | `results/_v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md` | 37,212 | 2026-09-26 19:18:37 | `24c64cc23907` | 成果面 |
| 930 | `results/_v3_v4_achievements_inventory_3dir_addendum_v2p1_2026_09_26.md` | 17,130 | 2026-09-26 19:45:55 | `4c731a625868` | 成果面 |
| 931 | `results/_v3n_cpath_live_rerun_verdict_2026_10_01.md` | 16,409 | 2026-10-01 09:26:42 | `a91efbfec3d0` | 成果面 |
| 932 | `results/_v3r1_threshold_final_path_judgment_2026_10_10.md` | 39,653 | 2026-10-10 09:58:13 | `93f187f1ab75` | 成果面 |
| 933 | `results/_v3r1_threshold_path4_draft_2026_10_10.md` | 39,077 | 2026-10-10 10:14:38 | `a51f5de630ed` | 成果面 |
| 934 | `results/_v3r1_threshold_restatement_design_2026_10_10.md` | 33,847 | 2026-10-10 01:00:44 | `fb85a8013f9d` | 成果面 |
| 935 | `results/_v4_85_77_attribution_verifier_r1_2026_09_29.md` | 17,727 | 2026-09-29 16:04:04 | `cd8ebaa86e44` | 成果面 |
| 936 | `results/_v4_closeout_bucket_register_2026_10_01.md` | 41,943 | 2026-10-01 10:49:39 | `99355c24a03b` | 成果面 |
| 937 | `results/_v4_concl_t_verify_2026_09_28.md` | 13,237 | 2026-09-28 19:32:52 | `927adba66e9b` | 成果面 |
| 938 | `results/_v4_daily_cleanup_2026_09_28.md` | 25,491 | 2026-09-28 18:29:44 | `f56e6fbf04ef` | 成果面 |
| 939 | `results/_v4_design_integration_2026_09_21_v1.0.md` | 119,732 | 2026-09-21 14:58:33 | `4b10cde29c27` | 成果面 |
| 940 | `results/_v4_design_integration_2026_09_21_v1.1.md` | 140,007 | 2026-09-21 16:33:04 | `fb5656993071` | 成果面 |
| 941 | `results/_v4_final_verify.py` | 4,794 | 2026-09-23 10:49:06 | `1dc482062d9b` | 成果面 |
| 942 | `results/_v4_gA1_experiment_outline_2026_09_22.md` | 7,837 | 2026-09-22 13:13:10 | `f4a6bdd43962` | 成果面 |
| 943 | `results/_v4_gA1_terminology_draft_2026_09_22.md` | 9,818 | 2026-09-22 13:09:56 | `0a2caf0a2bd2` | 成果面 |
| 944 | `results/_v4_gA3_seeds_judgment_draft_2026_09_22.md` | 19,772 | 2026-09-22 15:26:03 | `9119bb791dc1` | 成果面 |
| 945 | `results/_v4_gamma_r1_exec_2026_09_28.md` | 21,496 | 2026-09-28 17:38:42 | `0d946e65ba3c` | 成果面 |
| 946 | `results/_v4_gamma_r1_prereg_2026_09_28.md` | 33,489 | 2026-09-30 16:15:20 | `c9da8678cf2b` | 成果面 |
| 947 | `results/_v4_gamma_r1_prereg_v2_stop_2026_09_28.md` | 17,999 | 2026-09-28 19:36:48 | `9349e2fdb537` | 成果面 |
| 948 | `results/_v4_gamma_r1_sources_20260928_S1.md` | 2,944 | 2026-09-28 17:36:55 | `3d6e997aa692` | 成果面 |
| 949 | `results/_v4_gamma_r1_sources_20260928_S2.md` | 2,647 | 2026-09-28 17:37:02 | `dcec110ca2e0` | 成果面 |
| 950 | `results/_v4_gamma_r1_sources_20260928_S3.md` | 2,554 | 2026-09-28 17:37:12 | `6b9761d710ca` | 成果面 |
| 951 | `results/_v4_gamma_r1_sources_20260928_S4.md` | 3,050 | 2026-09-28 17:37:22 | `16af6baf8463` | 成果面 |
| 952 | `results/_v4_gamma_r1_sources_20260928_S5_faceD.md` | 2,264 | 2026-09-28 17:37:38 | `4f77d49756db` | 成果面 |
| 953 | `results/_v4_group_b_17letters_judgment_draft_2026_09_22.md` | 24,822 | 2026-09-22 16:24:26 | `99b835595dfb` | 成果面 |
| 954 | `results/_v4_group_b_explore_subs_integration_2026_09_22.md` | 20,532 | 2026-09-22 16:31:25 | `588b45430e88` | 成果面 |
| 955 | `results/_v4_item04_closeout_prereg_2026_09_28.md` | 26,719 | 2026-09-28 18:33:05 | `176e2b1c95ae` | 成果面 |
| 956 | `results/_v4_maindir_cleanup_manifest_2026_09_24.md` | 19,104 | 2026-09-24 17:59:34 | `32cc61d394f2` | 成果面 |
| 957 | `results/_v4_maindir_cleanup_manifest_v2_2026_09_26.md` | 27,909 | 2026-09-26 18:43:10 | `f586a5a21584` | 成果面 |
| 958 | `results/_v4_maindir_cleanup_moves_ledger_2026_09_24.md` | 18,829 | 2026-09-24 18:15:50 | `4025e871726b` | 成果面 |
| 959 | `results/_v4_maindir_cleanup_moves_ledger_v2_2026_09_24.md` | 47,909 | 2026-09-24 18:29:40 | `64c4ef850025` | 成果面 |
| 960 | `results/_v4_maindir_cleanup_moves_ledger_v3_2026_09_24.md` | 31,689 | 2026-09-24 19:16:52 | `8f5136e176b8` | 成果面 |
| 961 | `results/_v4_maindir_cleanup_moves_ledger_v4_2026_09_24.md` | 37,047 | 2026-09-24 19:39:04 | `9bd8932fa214` | 成果面 |
| 962 | `results/_v4_maindir_cleanup_moves_ledger_v5_2026_09_24.md` | 46,058 | 2026-09-24 19:58:55 | `272e8c752406` | 成果面 |
| 963 | `results/_v4_noise_cleanup_manifest_v2_2026_09_24.md` | 9,683 | 2026-09-24 21:42:05 | `90253e8342da` | 成果面 |
| 964 | `results/_v4_noise_cleanup_manifest_v3_2026_09_25.md` | 24,491 | 2026-09-25 01:12:20 | `6f3f6fa3ab1d` | 成果面 |
| 965 | `results/_v4_noise_cleanup_manifest_v4_2026_09_27.md` | 38,001 | 2026-09-27 21:19:39 | `82e90ff496ae` | 成果面 |
| 966 | `results/_v4_pending_decisions_2026_09_28.md` | 24,676 | 2026-09-30 16:15:20 | `fe4671517827` | 成果面 |
| 967 | `results/_v4_pi_cot_v2_collection_log.md` | 1,181 | 2026-09-23 17:49:35 | `167ad91f198e` | 成果面 |
| 968 | `results/_v4_pi_cot_v2_prereg_activation_2026_09_23.md` | 1,016 | 2026-09-23 18:03:11 | `00584e5a5c78` | 成果面 |
| 969 | `results/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` | 26,637 | 2026-09-26 19:14:42 | `ba4d07bd7000` | 成果面 |
| 970 | `results/_v4_pi_cot_v3_lock_and_rejudge_register_2026_09_28.md` | 12,152 | 2026-09-28 14:04:07 | `ae154971d1d2` | 成果面 |
| 971 | `results/_v4_r4_cleanup_execution_2026_09_29.md` | 15,357 | 2026-09-29 14:12:44 | `3932b46b16ce` | 成果面 |
| 972 | `results/_v4_r4_key_purge_manifest_2026_09_24.md` | 13,884 | 2026-09-24 18:55:22 | `5bf4d9ad2877` | 成果面 |
| 973 | `results/_v4_r4_purge_actions_2026_09_24.md` | 33,117 | 2026-09-24 19:24:11 | `8bbfe831e7c3` | 成果面 |
| 974 | `results/_v4_rj5_rederive_2026_09_28.md` | 22,145 | 2026-09-28 18:13:12 | `34ec49511ee3` | 成果面 |
| 975 | `results/_v4_rj5_rederive_appendix_2026_09_28.md` | 9,226 | 2026-09-28 18:13:40 | `985673661209` | 成果面 |
| 976 | `results/_v4_slow_cleanup_manifest_2026_09_28.md` | 15,693 | 2026-09-30 16:15:20 | `012501569aea` | 成果面 |
| 977 | `results/_v4_supp_l14v3_batch10_r5_executor.py` | 70,471 | 2026-09-27 20:26:47 | `04383377b6a2` | 成果面 |
| 978 | `results/_v4_supp_l14v3_batch2_r2_models_probe.log` | 1,260 | 2026-09-24 22:40:12 | `5664c63102a0` | 成果面 |
| 979 | `results/_v4_supp_l14v3_batch2_r2_models_probe.py` | 5,334 | 2026-09-27 20:26:47 | `a31d54a4b765` | 成果面 |
| 980 | `results/_v4_supp_l14v3_batch2_r2_result_probe_fail_v1.json` | 2,635 | 2026-09-24 22:43:10 | `21a89eb36a14` | 成果面 |
| 981 | `results/_v4_supp_l14v3_batch2_r6_executor.py` | 63,788 | 2026-09-27 20:26:47 | `e38d068f309c` | 成果面 |
| 982 | `results/_v4_supp_l14v3_batch3_r5_executor.py` | 72,156 | 2026-09-27 20:26:47 | `b7478168f87f` | 成果面 |
| 983 | `results/_v4_supp_l14v3_batch4_r5_verify.py` | 3,050 | 2026-09-25 01:35:07 | `60d19aeee6f5` | 成果面 |
| 984 | `results/_v4_supp_l14v3_batch4_r6_verify.py` | 4,712 | 2026-09-25 01:45:49 | `222972125231` | 成果面 |
| 985 | `results/_v4_supp_l14v3_batch6_r2_report.md` | 6,460 | 2026-09-25 01:15:52 | `080f9caf313c` | 成果面 |
| 986 | `results/_v4_supp_l14v3_batch6_r3_report.md` | 6,354 | 2026-09-25 01:39:41 | `6ef770d61308` | 成果面 |
| 987 | `results/_v4_supp_l14v3_batch6_r4_report.md` | 7,019 | 2026-09-25 01:53:59 | `0d0edc68cd35` | 成果面 |
| 988 | `results/_v4_supp_l14v3_batch6_r5_report.md` | 8,596 | 2026-09-25 02:08:01 | `d339d7286ad8` | 成果面 |
| 989 | `results/_v4_supp_l14v3_batch7_r5_executor.py` | 53,155 | 2026-09-27 20:26:47 | `38710a448e9c` | 成果面 |
| 990 | `results/_v4_supp_l14v3_batch9_r5_executor.py` | 65,672 | 2026-09-27 20:26:47 | `9b1a82a28dfb` | 成果面 |
| 991 | `results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md` | 21,309 | 2026-09-24 20:34:15 | `843e42ef4d2a` | 成果面 †141 |
| 992 | `results/_v4_supp_prereg_v02_add_T15_activation_2026_09_24.md` | 20,751 | 2026-09-24 23:48:54 | `443efb39804a` | 成果面 †141 |
| 993 | `results/_v4_supp_prereg_v02_add_T1_activation_2026_09_24.md` | 14,234 | 2026-09-24 20:27:29 | `79936b630015` | 成果面 †141 |
| 994 | `results/_v4_supp_t15r2_methodology_template.md` | 17,411 | 2026-09-27 11:40:23 | `6f9b865280a3` | 成果面 |
| 995 | `results/_v4_track2_endpoints_probe.py` | 20,738 | 2026-09-27 20:26:47 | `e7a6eb42c0af` | 成果面 |
| 996 | `results/_v4_track2_models_probe.py` | 3,191 | 2026-09-27 20:27:07 | `da62abaa1e03` | 成果面 |
| 997 | `results/_v4_track2_reprobe.py` | 2,860 | 2026-09-27 20:27:07 | `f92cc93f1304` | 成果面 |
| 998 | `results/_v4_trae_remaining_audit_2026_09_28.md` | 39,681 | 2026-09-28 15:28:25 | `1a8648083228` | 成果面 |
| 999 | `results/_v4s3_shadowing_priority_assessment_2026_10_01.md` | 20,111 | 2026-10-01 14:30:41 | `2aaac67603ce` | 成果面 |
| 1000 | `results/_v5_a_system_default_register_2026_09_28.md` | 19,892 | 2026-09-28 23:00:28 | `8c22796a42f5` | 成果面 |
| 1001 | `results/_v5_agent_trio_post_reorg_note_2026_09_29.md` | 9,795 | 2026-09-29 14:17:11 | `9c7182d93049` | 成果面 |
| 1002 | `results/_v5_alias_table_d01_d04_c01_c03_2026_09_29.md` | 15,315 | 2026-09-29 14:10:27 | `b3e39064d7c5` | 成果面 |
| 1003 | `results/_v5_anchor_drift_backfill_2026_09_28.md` | 14,438 | 2026-09-28 22:59:46 | `6f1edd1ccebb` | 成果面 |
| 1004 | `results/_v5_b12_verify_pack_q1_q3_q4_2026_09_29.md` | 33,803 | 2026-09-29 16:32:42 | `698262e6fe8b` | 成果面 |
| 1005 | `results/_v5_b14_08c_material_plan_2026_09_29.md` | 22,104 | 2026-09-29 17:26:18 | `b69d65cbb329` | 成果面 |
| 1006 | `results/_v5_b14_3_v1_4_prereg_2026_09_29.md` | 20,045 | 2026-09-29 16:55:29 | `0f1665e7056f` | 成果面 |
| 1007 | `results/_v5_b14_4_v1_3_prereg_2026_09_29.md` | 20,043 | 2026-09-29 16:55:31 | `ae474bf48c62` | 成果面 |
| 1008 | `results/_v5_b14_p41c_independent_judgment_2026_09_29.md` | 22,437 | 2026-09-29 19:13:24 | `b752582bc692` | 成果面 |
| 1009 | `results/_v5_b15_offsite_readonly_authorization_2026_09_29.md` | 18,483 | 2026-09-29 17:33:36 | `96a069701b3d` | 成果面 |
| 1010 | `results/_v5_b15_offsite_readonly_authorization_activation_2026_09_29.md` | 35,006 | 2026-09-29 19:40:50 | `99978eb15c10` | 成果面 |
| 1011 | `results/_v5_b17_fault_register_2026_09_29.md` | 18,129 | 2026-09-29 17:01:39 | `48cb0ab5f317` | 成果面 |
| 1012 | `results/_v5_b17_recheck12_register_2026_09_29.md` | 19,981 | 2026-09-29 17:02:29 | `73242a890be9` | 成果面 |
| 1013 | `results/_v5_b18_o8_semantic_verify_2026_09_29.md` | 26,544 | 2026-09-29 20:34:46 | `49d4adf8f197` | 成果面 |
| 1014 | `results/_v5_b18_o8_semantic_verify_r2_2026_09_29.md` | 24,145 | 2026-09-29 20:46:30 | `dc1233d0ab4f` | 成果面 |
| 1015 | `results/_v5_b20_gamma_a_attribution_2026_09_29.md` | 30,789 | 2026-09-29 17:31:42 | `7bad6e52a0f3` | 成果面 |
| 1016 | `results/_v5_b20_gamma_a_rereview_2026_09_29.md` | 30,680 | 2026-09-29 19:01:52 | `b22dda133038` | 成果面 |
| 1017 | `results/_v5_b22_r05_path_backfill_2026_09_29.md` | 12,233 | 2026-09-29 18:18:33 | `09b3105acb6f` | 成果面 |
| 1018 | `results/_v5_b22_r07_four_cond_prereg_2026_09_29.md` | 23,151 | 2026-09-29 18:27:58 | `ceea8f4534fb` | 成果面 |
| 1019 | `results/_v5_b35_result_attribution_2026_09_29.md` | 35,313 | 2026-09-29 17:48:32 | `ec358f6f76a3` | 成果面 |
| 1020 | `results/_v5_bom_u1_exec_2026_09_29.md` | 22,730 | 2026-09-29 10:48:46 | `5b0282960d52` | 成果面 |
| 1021 | `results/_v5_bom_u1_exec_2026_09_29.py` | 31,134 | 2026-09-29 10:46:21 | `c140a28e15ae` | 成果面 |
| 1022 | `results/_v5_clearance_mr10_pb_reembed_prereg_2026_09_29.md` | 18,271 | 2026-09-29 19:24:07 | `c514b321fe10` | 成果面 |
| 1023 | `results/_v5_clearance_mr11_doc_calibration_2026_09_29.md` | 14,974 | 2026-09-29 19:30:58 | `c4bce5a5e8be` | 成果面 |
| 1024 | `results/_v5_clearance_mr19_sha1_note_2026_09_29.md` | 22,859 | 2026-09-29 19:21:08 | `c74ffc6278a8` | 成果面 |
| 1025 | `results/_v5_clearance_mr3_s40_fix_note_2026_09_29.md` | 15,522 | 2026-09-29 19:20:43 | `b1244981065b` | 成果面 |
| 1026 | `results/_v5_clearance_o15_ready_pack_2026_09_29.md` | 48,968 | 2026-09-29 18:19:44 | `618e5990b3e5` | 成果面 |
| 1027 | `results/_v5_clearance_pending_backlog_register_2026_09_29.md` | 32,369 | 2026-09-29 20:52:20 | `1132072288de` | 成果面 |
| 1028 | `results/_v5_clearance_readme_c5_register_2026_09_29.md` | 8,730 | 2026-09-29 21:09:27 | `ababdaa392ca` | 成果面 |
| 1029 | `results/_v5_clearance_round11_register_2026_09_29.md` | 59,923 | 2026-09-29 19:12:41 | `2e5e6f8b328e` | 成果面 |
| 1030 | `results/_v5_clearance_round12_14_register_2026_09_29.md` | 75,131 | 2026-09-29 19:32:25 | `13d741979ebb` | 成果面 |
| 1031 | `results/_v5_clearance_round15_18_register_2026_09_29.md` | 99,989 | 2026-09-29 20:32:07 | `3a3c9c734bf9` | 成果面 |
| 1032 | `results/_v5_clearance_round1_b19_register_2026_09_29.md` | 28,556 | 2026-09-29 18:08:51 | `b69ec2ddc9be` | 成果面 |
| 1033 | `results/_v5_clearance_round2_3_register_2026_09_29.md` | 37,340 | 2026-09-29 18:25:58 | `32ca90e63a56` | 成果面 |
| 1034 | `results/_v5_clearance_round4_5_register_2026_09_29.md` | 52,782 | 2026-09-29 18:35:54 | `9d381fab5f46` | 成果面 |
| 1035 | `results/_v5_clearance_round6_register_2026_09_29.md` | 38,248 | 2026-09-29 18:43:49 | `68fe5b397df3` | 成果面 |
| 1036 | `results/_v5_clearance_round7_8_register_2026_09_29.md` | 63,311 | 2026-09-29 18:53:57 | `60cdeef91d4a` | 成果面 |
| 1037 | `results/_v5_clearance_round9_10_register_2026_09_29.md` | 68,512 | 2026-09-29 19:03:45 | `428e0857ebb7` | 成果面 |
| 1038 | `results/_v5_closing_register_r2_2026_09_28.md` | 25,446 | 2026-09-30 17:02:47 | `1094edb6e8c0` | 成果面 |
| 1039 | `results/_v5_confirm_b10_decisions_register_2026_09_29.md` | 13,282 | 2026-09-29 14:18:35 | `67ea81a2e6d9` | 成果面 |
| 1040 | `results/_v5_confirm_b12_decisions_register_2026_09_29.md` | 15,898 | 2026-09-29 14:24:50 | `db0d6e56a497` | 成果面 |
| 1041 | `results/_v5_confirm_b13_b22_anchor_verify_2026_09_29.md` | 16,393 | 2026-09-29 15:26:00 | `a0c2d1d5fe6b` | 成果面 |
| 1042 | `results/_v5_confirm_b13_b22_exec_queue_2026_09_29.md` | 39,531 | 2026-09-29 16:59:11 | `56549b04a925` | 成果面 |
| 1043 | `results/_v5_confirm_b13_decisions_register_2026_09_29.md` | 33,086 | 2026-09-29 15:14:58 | `c7ca4fbecc8b` | 成果面 |
| 1044 | `results/_v5_confirm_b16_b17_decisions_register_2026_09_29.md` | 29,624 | 2026-09-29 15:22:32 | `8e36a3e4c6ff` | 成果面 |
| 1045 | `results/_v5_confirm_b18_b19_decisions_register_2026_09_29.md` | 21,072 | 2026-09-29 15:23:32 | `ae160194878e` | 成果面 |
| 1046 | `results/_v5_confirm_b1_decisions_register_2026_09_29.md` | 28,469 | 2026-09-29 13:09:11 | `62ca213bb56c` | 成果面 |
| 1047 | `results/_v5_confirm_b20_b22_decisions_register_2026_09_29.md` | 24,883 | 2026-09-29 15:24:33 | `fccaac464565` | 成果面 |
| 1048 | `results/_v5_confirm_b2_decisions_register_2026_09_29.md` | 28,383 | 2026-09-29 13:13:58 | `63ded68919df` | 成果面 |
| 1049 | `results/_v5_confirm_b3_decisions_register_2026_09_29.md` | 34,015 | 2026-09-29 13:24:45 | `4dbb11c219fc` | 成果面 |
| 1050 | `results/_v5_confirm_b4_decisions_register_2026_09_29.md` | 43,498 | 2026-09-29 13:33:06 | `4d02f9df594e` | 成果面 |
| 1051 | `results/_v5_confirm_b8_decisions_register_2026_09_29.md` | 15,106 | 2026-09-29 14:11:28 | `6862659ff900` | 成果面 |
| 1052 | `results/_v5_ea_review_chain_rules_2026_09_29.md` | 11,511 | 2026-09-29 14:13:43 | `8e235f520fb9` | 成果面 |
| 1053 | `results/_v5_fake_verdict_forensics_2026_09_28.md` | 35,870 | 2026-09-28 23:22:52 | `1b135d8b1e08` | 成果面 |
| 1054 | `results/_v5_familyline_r01_r02_independent_judgment_2026_09_29.md` | 25,392 | 2026-09-29 19:40:23 | `e16e50329c88` | 成果面 |
| 1055 | `results/_v5_gamma_end1_rb_clause_addendum_2026_09_29.md` | 10,397 | 2026-09-29 14:08:53 | `bf38e5f0161e` | 成果面 |
| 1056 | `results/_v5_gamma_r1_v2_withdraw_2026_09_29.md` | 24,611 | 2026-09-29 10:59:20 | `f4ef22a5f97c` | 成果面 |
| 1057 | `results/_v5_gt33_attrib_fill_prereg_2026_09_29.md` | 36,984 | 2026-09-29 12:14:15 | `48742d6cbd03` | 成果面 |
| 1058 | `results/_v5_gt33_d5_crossref_note_2026_09_29.md` | 10,989 | 2026-09-29 13:55:24 | `dd50ff801ef7` | 成果面 |
| 1059 | `results/_v5_gt8_lowarm_result_2026_09_29_cb132cd5.json` | 26,253 | 2026-09-29 15:21:52 | `c68076c88140` | 成果面 |
| 1060 | `results/_v5_gt8_lowarm_resultA_cb132cd5_2026_09_29.json` | 28,638 | 2026-09-29 15:29:24 | `24b0d5eda48a` | 成果面 †141 |
| 1061 | `results/_v5_gt8_lowarm_verdict_2026_09_29.md` | 32,653 | 2026-09-29 15:50:16 | `9140b6e5970b` | 成果面 |
| 1062 | `results/_v5_gt8_lowarm_verdict_r2_2026_09_29.md` | 40,282 | 2026-09-29 19:32:56 | `aff727434aa4` | 成果面 |
| 1063 | `results/_v5_gt8f_m1_g1_fail_clause_addendum_2026_09_29.md` | 14,481 | 2026-09-29 14:05:11 | `31e5bd7b4003` | 成果面 |
| 1064 | `results/_v5_gt_exec_2026_09_29.json` | 142,217 | 2026-09-29 11:18:07 | `01e95e49b035` | 成果面 |
| 1065 | `results/_v5_h231_r07_independent_judgment_2026_09_29.md` | 37,949 | 2026-09-29 19:07:37 | `70025895600a` | 成果面 |
| 1066 | `results/_v5_item05_prereg_2026_09_28.md` | 19,115 | 2026-09-28 19:34:42 | `567f0f177699` | 成果面 |
| 1067 | `results/_v5_item21_asset_recovery_2026_09_28.md` | 8,793 | 2026-09-28 19:51:41 | `6c80ff43bdd7` | 成果面 |
| 1068 | `results/_v5_item21_patched_recompute_2026_09_28.md` | 15,895 | 2026-09-28 20:27:30 | `2c1d85913ccc` | 成果面 |
| 1069 | `results/_v5_item21_rerun_conditions_prereg_2026_09_28.md` | 31,429 | 2026-09-28 23:00:28 | `4185bdad6df5` | 成果面 |
| 1070 | `results/_v5_item21_strategyqa_realias_recompute_2026_09_29.md` | 14,639 | 2026-09-29 16:17:29 | `4e941d0a9c48` | 成果面 |
| 1071 | `results/_v5_item21_strategyqa_realias_verdict_2026_09_29.md` | 32,354 | 2026-09-29 16:45:55 | `26eaa156108f` | 成果面 |
| 1072 | `results/_v5_item21_verdict_2026_09_28.md` | 28,155 | 2026-09-28 21:30:15 | `de274bd38955` | 成果面 |
| 1073 | `results/_v5_item35_v3_collinear_exec_2026_09_29.md` | 46,000 | 2026-09-29 15:13:22 | `912afffed6b9` | 成果面 |
| 1074 | `results/_v5_item35_v3_collinear_verdict_2026_10_01.md` | 38,266 | 2026-10-01 09:05:02 | `363cce3dae59` | 成果面 |
| 1075 | `results/_v5_item35_v3_collinear_verdict_prep_2026_10_01.md` | 33,755 | 2026-10-01 08:57:30 | `a31026f2384d` | 成果面 |
| 1076 | `results/_v5_item36_prereg_2026_09_28.md` | 18,141 | 2026-09-28 19:35:54 | `7f42d5ee131c` | 成果面 |
| 1077 | `results/_v5_loadcorpus_fix_2026_09_29.md` | 17,355 | 2026-09-29 11:58:05 | `e47614ccf5ff` | 成果面 |
| 1078 | `results/_v5_loadcorpus_switch_2026_09_29.md` | 16,414 | 2026-09-29 12:13:38 | `d37e97644bf8` | 成果面 |
| 1079 | `results/_v5_paper_remedy_line_orchestration_2026_09_29.md` | 48,292 | 2026-09-29 14:02:32 | `d911674e68cf` | 成果面 |
| 1080 | `results/_v5_paper_remedy_r1_pledge_2026_09_29.md` | 47,778 | 2026-09-29 16:36:25 | `816cb91d4611` | 成果面 |
| 1081 | `results/_v5_paper_remedy_r2_r4_sourcetrace_2026_09_29.md` | 34,647 | 2026-09-29 15:49:34 | `29da2ca8932f` | 成果面 |
| 1082 | `results/_v5_paper_remedy_r6b_x27_sourcetrace_2026_09_29.md` | 16,125 | 2026-09-29 17:10:36 | `b75cc49b360f` | 成果面 |
| 1083 | `results/_v5_pd_v04_root_naming_candidates_2026_09_29.md` | 14,312 | 2026-09-29 14:06:13 | `46599dde51a8` | 成果面 |
| 1084 | `results/_v5_pi_decision_trace_gap_audit_2026_09_29.md` | 33,101 | 2026-09-29 13:53:25 | `38b043c4be6a` | 成果面 |
| 1085 | `results/_v5_pjpm_pc_degen_precheck_executor_2026_09_29.py` | 76,822 | 2026-09-29 13:46:42 | `f58b0d1c1a93` | 成果面 |
| 1086 | `results/_v5_pjpm_pc_reverify_bang2_2026_09_29.md` | 39,517 | 2026-09-29 14:14:27 | `6833cae407e8` | 成果面 |
| 1087 | `results/_v5_pjpm_pc_verdict_bang3_2026_09_29.md` | 41,566 | 2026-09-29 14:27:08 | `1814f9590f0f` | 成果面 |
| 1088 | `results/_v5_pl2_fourband_prereg_2026_09_29.md` | 29,253 | 2026-09-29 17:42:35 | `d5fdb89582fd` | 成果面 |
| 1089 | `results/_v5_prereg_chain_activation_register_2026_09_28.md` | 27,047 | 2026-09-28 22:10:58 | `3cc05f8cbd1a` | 成果面 |
| 1090 | `results/_v5_prereg_chain_status_annotation_2026_09_28.md` | 23,857 | 2026-09-28 22:28:54 | `cb4104938cc8` | 成果面 |
| 1091 | `results/_v5_proxy_temp_T0.3.json` | 143,345 | 2026-09-23 11:59:01 | `04d915714b96` | 成果面 |
| 1092 | `results/_v5_proxy_temp_T1.5.json` | 143,261 | 2026-09-23 11:59:01 | `2b36d8632a80` | 成果面 |
| 1093 | `results/_v5_proxy_vocab_V50.json` | 78,182 | 2026-09-23 11:59:01 | `2deedc43fc40` | 成果面 |
| 1094 | `results/_v5_proxy_vocab_V500.json` | 78,191 | 2026-09-23 11:59:01 | `4ddd6afbf16b` | 成果面 |
| 1095 | `results/_v5_r4_residual_merged_catalogue_2026_09_29.md` | 102,410 | 2026-09-29 16:43:51 | `0c4bbd26ea55` | 成果面 |
| 1096 | `results/_v5_recyclebin_sha12_completion_2026_09_29.md` | 59,551 | 2026-09-29 16:19:12 | `5f3223a4b349` | 成果面 |
| 1097 | `results/_v5_rj5_verdict_2026_09_29.md` | 40,057 | 2026-09-29 02:05:11 | `9c1ccbd5cf5a` | 成果面 |
| 1098 | `results/_v5_sha12_collision_statement_2026_09_29.md` | 28,155 | 2026-09-29 17:20:57 | `f0f44cf6dc65` | 成果面 |
| 1099 | `results/_v5_sub_artifact_ledger_history_r1_2026_09_29.md` | 48,539 | 2026-09-29 10:56:50 | `535b3c2ad102` | 成果面 |
| 1100 | `results/_v5_sub_artifact_ledger_history_r2_2026_09_29.md` | 150,957 | 2026-09-29 11:42:24 | `5ff7784db145` | 成果面 |
| 1101 | `results/_v5_sub_artifact_ledger_history_r3_2026_09_29.md` | 128,760 | 2026-09-29 12:44:15 | `e04a46b02d13` | 成果面 |
| 1102 | `results/_v5_sub_artifact_ledger_history_r4_2026_09_29.md` | 603,599 | 2026-09-29 16:26:42 | `b6b8be476a73` | 成果面 |
| 1103 | `results/_v5_t1_decisions_register_2026_09_29.md` | 31,330 | 2026-09-29 11:34:08 | `7dd7dd3fb721` | 成果面 |
| 1104 | `results/_v5_theory_input_acquisition_request_2026_09_29.md` | 10,691 | 2026-09-30 20:26:40 | `83afc4802fe7` | 成果面 |
| 1105 | `results/_v5_track2_qwen_retry_2026_09_29.md` | 11,957 | 2026-09-29 11:13:37 | `c890771728f3` | 成果面 |
| 1106 | `results/_v5_track2_qwen_retry_executor_20260929.py` | 11,586 | 2026-09-29 11:10:20 | `d34b46e24a7c` | 成果面 |
| 1107 | `results/_v5_v3_deg_c5_b_halt_report_2026_09_29.md` | 14,862 | 2026-09-29 13:44:25 | `f2b68ee099b5` | 成果面 |
| 1108 | `results/_v5_v3_deg_p1_reopen_exec_2026_09_29.md` | 33,622 | 2026-09-29 13:45:42 | `38231ef6f053` | 成果面 |
| 1109 | `results/_v5_v3_deg_p1_reopen_verdict_2026_09_29.md` | 42,645 | 2026-09-29 15:16:34 | `63d898ab1b71` | 成果面 |
| 1110 | `results/_v5_v3_deg_p1_reopen_verdict_r2_2026_09_29.md` | 44,054 | 2026-09-29 15:24:27 | `8adaf4e5d868` | 成果面 |
| 1111 | `results/_v5_v3_deg_p1_reopen_verify_2026_09_29.md` | 27,898 | 2026-09-29 14:20:21 | `4afeb8cd41de` | 成果面 |
| 1112 | `results/_v5_v3_t1_effect_judgment_2026_09_29.md` | 40,697 | 2026-09-29 20:13:28 | `1995bd4460ae` | 成果面 |
| 1113 | `results/_v5_v3deg_prereg_activation_register_2026_09_29.md` | 24,370 | 2026-09-29 12:19:34 | `e587da3b4cf8` | 成果面 |
| 1114 | `results/_v5_v3r2_errata_note_2026_09_29.md` | 29,089 | 2026-09-29 20:12:47 | `d687ad25a68c` | 成果面 |
| 1115 | `results/_v5_v4_export_filter_spec_2026_09_29.md` | 22,884 | 2026-09-29 17:04:12 | `14dd6ccdbed6` | 成果面 |
| 1116 | `results/_v5_v4_proposal_23item_merged_catalogue_2026_09_29.md` | 14,620 | 2026-09-29 14:16:40 | `79bcff089f21` | 成果面 |
| 1117 | `results/_v5_v4_proposal_23item_merged_catalogue_sourceverify_2026_09_29.md` | 22,185 | 2026-09-29 15:18:09 | `ac0d6f19f06c` | 成果面 |
| 1118 | `results/_verdict_pack_d_prep_2026_10_01.md` | 49,471 | 2026-10-14 14:07:09 | `8c2ce0dc1c2d` | 成果面 |
| 1119 | `results/_vk_current_counting_face_2026_10_10.md` | 24,795 | 2026-10-10 21:35:11 | `4d4e41c3eff5` | 成果面 |
| 1120 | `results/_vk_face_category_erratum_2026_10_11.md` | 17,373 | 2026-10-11 00:15:40 | `67bf70301889` | 成果面 |
| 1121 | `results/_vk_two_items_judgments_2026_10_09.md` | 33,399 | 2026-10-09 23:16:17 | `82556d54726c` | 成果面 |
| 1122 | `results/_volc_22cap_emb.py` | 11,105 | 2026-09-10 17:36:26 | `15904ecae629` | 成果面 |
| 1123 | `results/_w1_stage2_premise_stale_register_2026_10_14.md` | 8,326 | 2026-10-14 23:45:51 | `a7e14145e1c8` | 成果面 †141 |
| 1124 | `results/_wordlist_house_effectivity_note_2026_10_10.md` | 14,606 | 2026-10-10 12:01:03 | `4e89a5bb4b68` | 成果面 |
| 1125 | `results/_wordlist_house_establishment_draft_2026_10_10.md` | 38,468 | 2026-10-10 02:43:26 | `afa5eb53d216` | 成果面 |
| 1126 | `results/_worker_openrouter_rag_run.py` | 24,113 | 2026-09-16 11:01:12 | `4458ccf3d64a` | 成果面 |
| 1127 | `results/_wrapup_cleanup_inventory_register_2026_09_29.md` | 22,556 | 2026-09-29 21:31:56 | `6beeb397a4c1` | 成果面 |
| 1128 | `results/_xiang14_third_reissue_registration_2026_10_13.md` | 7,188 | 2026-10-13 23:24:08 | `25141de92c50` | 成果面 †141 |
| 1129 | `results/_zero_consumption_cells_field_correction_2026_10_10.md` | 12,244 | 2026-10-10 20:17:54 | `36f9ac4ebbf6` | 成果面 |
| 1130 | `results/_zero_reading_judgment_2026_10_10.md` | 27,824 | 2026-10-10 21:28:00 | `a9947f5677df` | 成果面 |
| 1131 | `results/attack_pc_a1_resampling_2026_09_15.json` | 1,017 | 2026-09-15 15:27:35 | `d21912a05d79` | 成果面 |
| 1132 | `results/attack_pc_a2_fitting_2026_09_15.json` | 1,024 | 2026-09-15 15:27:36 | `5a880678c386` | 成果面 |
| 1133 | `results/attack_pc_a3_clipping_2026_09_15.json` | 1,265 | 2026-09-15 15:27:36 | `d74d6b39d1b0` | 成果面 |
| 1134 | `results/boss_pa_1_rbr_rm_result_2026_09_15.json` | 8,753 | 2026-09-15 15:28:10 | `c7c59e0d2f6c` | 成果面 |
| 1135 | `results/boss_pa_2_potential_game_result_2026_09_15.json` | 7,530 | 2026-09-15 15:28:10 | `5c76137d6430` | 成果面 |
| 1136 | `results/boss_pa_3_replicator_dynamics_result_2026_09_15.json` | 9,098 | 2026-09-15 15:28:10 | `d6f233d73c45` | 成果面 |
| 1137 | `results/boss_pc_1_a1_resampling_2026_09_15.json` | 1,017 | 2026-09-15 13:34:48 | `d21912a05d79` | 成果面 |
| 1138 | `results/boss_pc_1_real_2d_ising_2026_09_15.json` | 2,460 | 2026-09-15 15:28:00 | `43d9ce160fc8` | 成果面 |
| 1139 | `results/boss_pc_2_real_transverse_ising_2026_09_15.json` | 3,553 | 2026-09-15 15:27:35 | `8933d61b180a` | 成果面 |
| 1140 | `results/boss_pc_3_real_reservoir_2026_09_15.json` | 2,364 | 2026-09-15 15:28:00 | `94b5398be76c` | 成果面 |
| 1141 | `results/c5_b_group_verdict_2026_10_01.md` | 30,118 | 2026-10-01 09:53:17 | `3fbf6b38a383` | 成果面 |
| 1142 | `results/c5_protocol_version_annex_2026_10_01.md` | 18,558 | 2026-10-01 10:25:17 | `2593ea7b93cf` | 成果面 |
| 1143 | `results/d7_5anchor_60cells_9model_verdict_2026_09_18.json` | 2,456 | 2026-09-16 11:00:06 | `4505cca79c15` | 成果面 |
| 1144 | `results/deposon_3risk_v0_fixes_2026_09_11.json` | 8,338 | 2026-09-11 17:16:56 | `d87c0327a6fb` | 成果面 |
| 1145 | `results/deposon_ark_models_2026_09_10.json` | 23,296 | 2026-09-10 15:14:46 | `ccc3ea09a7f5` | 成果面 |
| 1146 | `results/deposon_benchmark_v1_3_labelfree.json` | 3,011 | 2026-08-23 00:30:18 | `57f06a426bec` | 成果面 |
| 1147 | `results/deposon_benchmark_v1_3_labelshuffle.json` | 182,322 | 2026-08-23 00:01:28 | `5a7555358be3` | 成果面 |
| 1148 | `results/deposon_benchmark_v1_3_resonant.json` | 3,134 | 2026-08-23 00:30:18 | `769ae8c908c9` | 成果面 |
| 1149 | `results/deposon_benchmark_v1_4_sc5.json` | 12,479 | 2026-08-23 15:14:50 | `c9796d3b3263` | 成果面 |
| 1150 | `results/deposon_deepseek_v41_flash_2026_09_10.json` | 13,373 | 2026-09-10 15:47:09 | `4d7bea150f3a` | 成果面 |
| 1151 | `results/deposon_deepseek_v41_flash_30cells_2026_09_10.json` | 46,432 | 2026-09-10 16:02:21 | `84df447c38df` | 成果面 |
| 1152 | `results/deposon_deepseek_v41_flash_30cells_v2_2026_09_10.json` | 17,549 | 2026-09-10 16:17:05 | `05cde1ca74ef` | 成果面 |
| 1153 | `results/deposon_deepseek_v41_flash_5cells_fix_2026_09_10.json` | 6,748 | 2026-09-10 16:55:12 | `28bad561c328` | 成果面 |
| 1154 | `results/deposon_embedding_dual_2026_09_10.json` | 6,834 | 2026-09-16 11:01:12 | `33f8ac5d4bff` | 成果面 |
| 1155 | `results/deposon_embedding_openrouter_5models_2026_09_10.json` | 12,785 | 2026-09-10 16:55:37 | `0c0d9afd39ac` | 成果面 |
| 1156 | `results/deposon_feshbach_lindblad_sim_2026_09_10.json` | 7,414 | 2026-09-10 22:09:37 | `aa545c67604d` | 成果面 |
| 1157 | `results/deposon_feshbach_rag_30cells_2026_09_10.json` | 64,978 | 2026-09-16 11:01:12 | `508f664ffa44` | 成果面 |
| 1158 | `results/deposon_g3_arrhenius.json` | 2,284 | 2026-08-23 05:00:55 | `a3de045b5dd7` | 成果面 |
| 1159 | `results/deposon_gpt6_astra_smoke_2026_09_10.json` | 3,500 | 2026-09-10 14:37:29 | `4bf92bfdefda` | 成果面 |
| 1160 | `results/deposon_gpt6_proxy_smoke_2026_09_10.json` | 5,485 | 2026-09-10 15:13:52 | `524b34e319b5` | 成果面 |
| 1161 | `results/deposon_gpt6_proxy_step1_2026_09_10.json` | 1,245 | 2026-09-10 15:13:16 | `2e23115d9d4b` | 成果面 |
| 1162 | `results/deposon_gpt6_proxy_v2_2026_09_10.json` | 5,810 | 2026-09-10 15:47:09 | `a6812512f8f3` | 成果面 |
| 1163 | `results/deposon_gpt6_teamorouter_cn_2026_09_10.json` | 4,855 | 2026-09-10 17:00:24 | `2241567c6efd` | 成果面 |
| 1164 | `results/deposon_gpt6_vpn_smoke_2026_09_10.json` | 3,489 | 2026-09-10 14:53:46 | `3267746e47e9` | 成果面 |
| 1165 | `results/deposon_llm_codingplan_30cells_2026_09_10.json` | 18,634 | 2026-09-10 15:15:24 | `24e4dcbaa4ea` | 成果面 |
| 1166 | `results/deposon_openrouter_5model_30cells_2026_09_10.json` | 31,690 | 2026-09-10 22:47:29 | `b374f80f3b2d` | 成果面 |
| 1167 | `results/deposon_openrouter_embedding_5model_2026_09_10.json` | 9,472 | 2026-09-10 22:24:35 | `45f314f3415c` | 成果面 |
| 1168 | `results/deposon_overseas_open_smoke_2026_09_10.json` | 6,787 | 2026-09-10 14:56:03 | `2481adadcbb9` | 成果面 |
| 1169 | `results/deposon_pf_d1_2026_09_15.json` | 21,933 | 2026-09-15 11:30:53 | `12791772814e` | 成果面 |
| 1170 | `results/deposon_v16_llm_prior_summary.json` | 5,517 | 2026-08-23 20:28:34 | `a7952d9d78db` | 成果面 |
| 1171 | `results/deposon_v2_phase2_dual_mainline_2026_09_11.json` | 3,189 | 2026-09-16 11:01:12 | `e337b824c4b9` | 成果面 |
| 1172 | `results/deposon_v2_phase2_f2_2026_09_11.json` | 4,582 | 2026-09-11 11:19:24 | `8b16b611c4db` | 成果面 |
| 1173 | `results/deposon_v2_phase3_f3_2026_09_11.json` | 2,474 | 2026-09-11 11:19:55 | `0b5dca765d16` | 成果面 |
| 1174 | `results/deposon_v2_phase3_strip_reembed_2026_09_11.json` | 4,160 | 2026-09-11 11:33:43 | `8900526d8e3a` | 成果面 |
| 1175 | `results/deposon_v2_phase5_f5_2026_09_11.json` | 2,356 | 2026-09-11 11:16:45 | `889fc57b3b72` | 成果面 |
| 1176 | `results/deposon_v3x_6way_stage2_2026_09_10.json` | 2,741 | 2026-09-10 17:56:17 | `d301bbfed982` | 成果面 |
| 1177 | `results/deposon_v3x_6way_stage3_2026_09_10.json` | 15,943 | 2026-09-10 18:15:22 | `d892a9d3d6ba` | 成果面 |
| 1178 | `results/deposon_v3x_6way_summary_2026_09_10.json` | 1,506 | 2026-09-10 18:17:10 | `63e0798e5843` | 成果面 |
| 1179 | `results/deposon_v41_flash_60cells_v2_2026_09_10.json` | 38,428 | 2026-09-10 17:34:41 | `b1d802a68723` | 成果面 |
| 1180 | `results/deposon_v41_flash_rag_baseline_2026_09_10.json` | 101,484 | 2026-09-10 17:07:49 | `6754d2655e0a` | 成果面 |
| 1181 | `results/deposon_volcengine_7model_smoke_2026_09_10.json` | 5,944 | 2026-09-16 11:01:12 | `eae44cc3b7b2` | 成果面 |
| 1182 | `results/deposon_volcengine_9model_smoke_2026_09_10.json` | 5,328 | 2026-09-16 11:01:12 | `0e5ae7d7d641` | 成果面 |
| 1183 | `results/deposon_volcengine_coding_plan_5cells_2026_09_10.json` | 6,058 | 2026-09-16 11:01:12 | `52aa8901556e` | 成果面 |
| 1184 | `results/deposon_volcengine_coding_plan_catalog_2026_09_10.json` | 2,841 | 2026-09-16 11:01:12 | `c0efb547b9d1` | 成果面 |
| 1185 | `results/deposon_volcengine_doubao_embedding_2026_09_10.json` | 3,303 | 2026-09-16 11:01:12 | `e99783d18139` | 成果面 |
| 1186 | `results/deposon_volcengine_embedding_30cells_2026_09_10.json` | 24,794 | 2026-09-16 11:01:12 | `12be52bc02a7` | 成果面 |
| 1187 | `results/deposon_volcengine_minimax_m3_30cells_2026_09_10.py` | 11,703 | 2026-09-16 18:20:55 | `218ef1a99f97` | 成果面 |
| 1188 | `results/llm_prior_cache.json` | 938 | 2026-08-23 20:21:35 | `5f16be89efc5` | 成果面 |
| 1189 | `results/llm_prior_cache_v18_contamination.json` | 639 | 2026-08-23 22:56:14 | `d3f72f67977d` | 成果面 |
| 1190 | `results/llm_prior_cache_v18_contentless.json` | 512 | 2026-08-23 23:17:58 | `7c0d169ef164` | 成果面 |
| 1191 | `results/llm_prior_cache_v18_direction.json` | 2,168 | 2026-08-23 23:04:12 | `023f936f80fb` | 成果面 |
| 1192 | `results/llm_prior_cache_v18_labelshuffle.json` | 1,925 | 2026-08-23 22:56:03 | `8dce6d7618a2` | 成果面 |
| 1193 | `results/manifest_large_files.md` | 3,440 | 2026-08-29 01:26:28 | `e0dc7a8e4c75` | 成果面 |
| 1194 | `results/quizbank_v20.json` | 37,250 | 2026-08-28 20:46:44 | `f6035466ff3d` | 成果面 |
| 1195 | `results/quizbank_v20_big.json` | 104,872 | 2026-08-28 23:54:09 | `da6fecdcbbf6` | 成果面 |
| 1196 | `results/skill_a_p_a_60cells_result_2026_09_11.json` | 2,220 | 2026-09-11 17:06:25 | `f4a210d69220` | 成果面 |
| 1197 | `results/skill_b_p_c_alpha_beta_result_2026_09_11.json` | 12,609 | 2026-09-11 17:06:29 | `b921002e4dfb` | 成果面 |
| 1198 | `results/skill_c_p_e_3modality_result_2026_09_11.json` | 5,271 | 2026-09-11 17:06:33 | `470425a8c77d` | 成果面 |
| 1199 | `results/skill_d_p_f_observer_result_2026_09_11.json` | 11,010 | 2026-09-15 13:31:05 | `0207c01b9562` | 成果面 |
| 1200 | `results/v19_edges_audit_input.csv` | 2,186 | 2026-08-28 15:53:28 | `8b6682181392` | 成果面 |
| 1201 | `results/v20_graph_features.csv` | 2,151 | 2026-08-28 20:43:58 | `f95f382ace44` | 成果面 |
| 1202 | `results/v20_regression_field.json` | 5,396 | 2026-08-28 20:44:45 | `534c121765b1` | 成果面 |
| 1203 | `results/v20_regression_field_v2.json` | 4,236 | 2026-08-28 20:45:20 | `3596490e1fc0` | 成果面 |
| 1204 | `results/v20_statcheck_fm_vs_deg.json` | 988 | 2026-08-28 20:44:25 | `dfe014c627ca` | 成果面 |
| 1205 | `results/v20_statcheck_fm_vs_rand.json` | 868 | 2026-08-28 20:44:24 | `1dadfaeb2c43` | 成果面 |
| 1206 | `reviews/deep_probe_R1.md` | 14,895 | 2026-08-29 01:04:00 | `190dd5df9af2` | 成果面 †141 |
| 1207 | `reviews/deep_probe_R2.md` | 23,391 | 2026-08-29 01:10:13 | `a4f8a55b70ba` | 成果面 †141 |
| 1208 | `reviews/literature_scan_v2X_A.md` | 18,876 | 2026-08-28 21:42:49 | `d0bba9379b4b` | 成果面 †141 |
| 1209 | `reviews/literature_scan_v2X_B.md` | 30,468 | 2026-08-28 21:50:11 | `313b30815a39` | 成果面 †141 |
| 1210 | `reviews/peer_review_v19_A.md` | 24,409 | 2026-08-24 00:36:05 | `28878116d87b` | 成果面 †141 |
| 1211 | `reviews/peer_review_v19_B.md` | 42,672 | 2026-08-24 01:07:19 | `da98f9e310d4` | 成果面 †141 |
| 1212 | `reviews/review_coach_v2X_draft.md` | 23,468 | 2026-08-29 22:22:13 | `0bafe659c00d` | 成果面 †141 |
| 1213 | `reviews/review_format_v2X.md` | 6,656 | 2026-08-30 04:02:12 | `2dc4b45424ab` | 成果面 †141 |
| 1214 | `tmp_movedout_2026_09_28/_cleanup_classify_2026_09_28.py` | 3,232 | 2026-09-28 18:17:11 | `efb57dc056f0` | 成果面 |
| 1215 | `tmp_movedout_2026_09_28/_cleanup_classify_out_2026_09_28.txt` | 11,347 | 2026-09-28 18:17:58 | `e1f9db7e1cab` | 成果面 |
| 1216 | `tmp_movedout_2026_09_28/_cleanup_probe_2026_09_28.py` | 2,556 | 2026-09-28 18:14:13 | `20bd0972fa00` | 成果面 |
| 1217 | `tmp_movedout_2026_09_28/_cleanup_probe_out_2026_09_28.txt` | 12,365 | 2026-09-28 18:14:33 | `75f9058f8a51` | 成果面 |
| 1218 | `tmp_movedout_2026_09_28/_cleanup_resolve_2026_09_28.py` | 2,735 | 2026-09-28 18:19:07 | `57085a643c33` | 成果面 |
| 1219 | `tmp_movedout_2026_09_28/_cleanup_resolve_out_2026_09_28.txt` | 1,257 | 2026-09-28 18:19:25 | `1d163e68ed25` | 成果面 |
| 1220 | `tmp_movedout_2026_09_28/_cleanup_transfer_scan_2026_09_28.py` | 3,229 | 2026-09-28 18:25:29 | `97291768f38d` | 成果面 |
| 1221 | `tmp_movedout_2026_09_28/_cleanup_transfer_scan_out_2026_09_28.txt` | 5,017 | 2026-09-28 18:25:45 | `04d99d651df9` | 成果面 |
| 1222 | `tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/_old_corpus_view.py` | 23,893 | 2026-08-29 01:14:15 | `7d8d6a30dd8c` | 成果面 |
| 1223 | `tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/annotate_baseline.py` | 2,050 | 2026-09-29 12:08:25 | `be710bb0c40f` | 成果面 |
| 1224 | `tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/applied_diff.txt` | 5,134 | 2026-09-29 12:11:55 | `05c4704ee5cc` | 成果面 |
| 1225 | `tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/apply_fix.py` | 3,460 | 2026-09-29 13:39:20 | `c3808483722e` | 成果面 |
| 1226 | `tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/baseline_post.json` | 115,634 | 2026-09-29 12:11:10 | `5cdf357a45e8` | 成果面 |
| 1227 | `tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/baseline_pre.json` | 115,139 | 2026-09-29 12:05:24 | `c5e0497b9020` | 成果面 |
| 1228 | `tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/snapshot.py` | 1,438 | 2026-09-29 12:05:09 | `dcede756619f` | 成果面 |
| 1229 | `tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/verify_2026_09_29.py` | 11,167 | 2026-09-29 13:39:08 | `a1c70189ebbb` | 成果面 |
| 1230 | `tmp_movedout_2026_10_01/_docwriter_wt2_enum_final_2026_09_30.tsv` | 66,339 | 2026-09-30 18:01:38 | `53c4c15c4e06` | 成果面 |
| 1231 | `tmp_movedout_2026_10_01/legacy_caliber/README_V1_LEGACY.md` | 3,756 | 2026-08-23 07:47:23 | `18e095c85427` | 成果面 |
| 1232 | `tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s1b_inv2_2026_09_27.py` | 1,546 | 2026-09-27 20:18:50 | `af475f496a5e` | 成果面 |
| 1233 | `tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s2_scan_2026_09_27.py` | 4,000 | 2026-09-27 20:19:13 | `c2cc22b27047` | 成果面 |
| 1234 | `tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s3_keyscan_2026_09_27.py` | 2,647 | 2026-09-27 20:19:48 | `a32af07111df` | 成果面 |
| 1235 | `tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s3b_uuidctx_2026_09_27.py` | 1,707 | 2026-09-27 20:20:08 | `8fdec59aa96b` | 成果面 |
| 1236 | `tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s3c_keydetail_2026_09_27.py` | 2,490 | 2026-09-27 20:20:25 | `16ae5764add1` | 成果面 |
| 1237 | `tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s4_verify_2026_09_27.py` | 2,812 | 2026-09-27 20:25:11 | `dbe00430d769` | 成果面 |
| 1238 | `tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s6_unrefscan_2026_09_27.py` | 2,495 | 2026-09-27 20:26:11 | `1b31a3111a86` | 成果面 |
| 1239 | `tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s7_fix_2026_09_27.py` | 6,101 | 2026-09-27 20:26:39 | `fc200e5f343d` | 成果面 |
| 1240 | `tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s8_fix3_2026_09_27.py` | 3,514 | 2026-09-27 20:26:58 | `051dbdb121c9` | 成果面 |
| 1241 | `tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s9_final_2026_09_27.py` | 3,399 | 2026-09-27 20:27:53 | `aef86f53cc0e` | 成果面 |
| 1242 | `tmp_movedout_2026_10_01/process_scripts/v4_wt_2026_09_27/_v4_wt_s5_verify_2026_09_27.py` | 4,950 | 2026-09-27 20:08:06 | `736e56cd5553` | 成果面 |
| 1243 | `tmp_movedout_2026_10_01/process_scripts/v5_wa_2026_09_30/_v5_wa_s1_2026_09_30.py` | 4,351 | 2026-09-30 19:02:06 | `f77f72f7b86e` | 成果面 |
| 1244 | `tmp_movedout_2026_10_01/process_scripts/v5_wa_2026_09_30/_v5_wa_s2b_2026_09_30.py` | 3,583 | 2026-09-30 19:03:43 | `9403dfac5824` | 成果面 |
| 1245 | `tmp_movedout_2026_10_01/process_scripts/v5_wa_2026_09_30/_v5_wa_s2c_2026_09_30.py` | 3,168 | 2026-09-30 19:04:28 | `2f55832a82cb` | 成果面 |
| 1246 | `tmp_movedout_2026_10_01/process_scripts/v5_wa_2026_09_30/_v5_wa_s3_fix_2026_09_30.py` | 4,742 | 2026-09-30 19:06:08 | `ff16d68fdb81` | 成果面 |
| 1247 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_asset_recount_2026_09_30.md` | 9,441 | 2026-09-30 19:26:23 | `e56286e6cba0` | 成果面 |
| 1248 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_letter_review_bob_w3_commission_2026_09_30.md` | 10,286 | 2026-09-30 19:28:23 | `efe451595a16` | 成果面 |
| 1249 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v4_01_knifeedge_independent_review_2026_09_29.md` | 19,731 | 2026-09-29 15:49:57 | `a66b4159793f` | 成果面 |
| 1250 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v4_tmp_cleanup_2026_09_28.md` | 5,131 | 2026-09-28 18:05:44 | `b8338bdd33f2` | 成果面 |
| 1251 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b14_1_k04_caliber_fixation_2026_09_29.md` | 13,127 | 2026-09-29 16:51:32 | `697145c8352d` | 成果面 |
| 1252 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b14_r3_anchor_retrieval_2026_09_29.md` | 23,023 | 2026-09-29 18:56:44 | `6e0a1461a688` | 成果面 |
| 1253 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b16_1dcritical_lit_search_2026_09_29.md` | 26,931 | 2026-09-29 17:20:00 | `09ad0c6ce46a` | 成果面 |
| 1254 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b16_dual_caliber_rule_2026_09_29.md` | 16,262 | 2026-09-29 17:11:44 | `3b7dfdce494e` | 成果面 |
| 1255 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b16_idx23_blindrate_verify_2026_09_29.md` | 19,755 | 2026-09-29 17:28:04 | `430588419975` | 成果面 |
| 1256 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b16_mq11_case_2026_09_29.md` | 16,723 | 2026-09-29 17:17:10 | `85f92c8d18d1` | 成果面 |
| 1257 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b17_three_caliber_fixation_2026_09_29.md` | 19,709 | 2026-09-29 17:12:46 | `d47b5e067c1c` | 成果面 |
| 1258 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b18_coding_caliber_2026_09_29.md` | 14,304 | 2026-09-29 17:00:32 | `04f6890dc4a8` | 成果面 |
| 1259 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b18_single_count_fixation_2026_09_29.md` | 13,608 | 2026-09-29 17:01:41 | `006e316bfe4c` | 成果面 |
| 1260 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_glm_charlie_reread_ac74a04efeb2_2026_09_29.md` | 18,514 | 2026-09-29 16:01:34 | `bf0874456a58` | 成果面 |
| 1261 | `verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json` | 5,049 | 2026-09-15 13:31:24 | `da517c115f3c` | 成果面 †141 |
| 1262 | `verifier/handoff/P_A_V0_anchors_sha256_12.json` | 7,796 | 2026-10-15 09:53:17 | `c4f029f780d8` | 成果面 †141 |
| 1263 | `verifier/handoff/P_F_PREDECISION_2026_09_09.json` | 3,680 | 2026-09-09 13:50:15 | `b41c98bf90cc` | 成果面 †141 |
| 1264 | `verifier/kill_lines/GT_kill_line_carrier_v0.md` | 16,486 | 2026-10-15 09:49:14 | `0f65a42e7a34` | 成果面 †141 |
| 1265 | `verifier/kill_lines/GT_kill_line_carrier_v1.md` | 18,905 | 2026-10-15 11:08:00 | `9e09214cf088` | 成果面 †141 |
| 1266 | `verifier/README.md` | 14,360 | 2026-08-30 17:08:56 | `d76f2dc473be` | 成果面 †141 |
| 1267 | `verifier/runs/20260823T022721Z.log` | 7 | 2026-08-23 10:27:21 | `cf205dbb8cea` | 成果面 †141 |
| 1268 | `verifier/runs/20260823T130229Z.log` | 839 | 2026-08-23 21:02:31 | `1af06784d975` | 成果面 †141 |
| 1269 | `verifier/runs/20260823T130254Z.log` | 839 | 2026-08-23 21:02:55 | `8316e03518f2` | 成果面 †141 |
| 1270 | `verifier/runs/20260823T130326Z.log` | 819 | 2026-08-23 21:03:27 | `e8698e422d69` | 成果面 †141 |
| 1271 | `verifier/runs/20260823T130405Z.log` | 576 | 2026-08-23 21:04:08 | `d6071ff9493e` | 成果面 †141 |
| 1272 | `verifier/runs/20260823T131053Z.log` | 911 | 2026-08-23 21:10:55 | `94e578649599` | 成果面 †141 |
| 1273 | `verifier/runs/20260823T134128Z.log` | 910 | 2026-08-23 21:41:34 | `6cf95aade825` | 成果面 †141 |
| 1274 | `verifier/runs/20260823T134305Z.log` | 972 | 2026-08-23 21:43:08 | `c9ae2079fc1f` | 成果面 †141 |
| 1275 | `verifier/runs/20260823T154658Z.log` | 1,536 | 2026-08-23 23:47:08 | `1fca45290883` | 成果面 †141 |
| 1276 | `volcengine_glm_latest_30cells_v2_runner_2026_09_10.py` | 20,745 | 2026-09-18 13:48:17 | `26ff34bfcc79` | 成果面 |

## §5 · 计数并列（⛔ 0 校正 ／ 0 择一 ／ 0 静默合并）

### §5.1 四读并列表（时点口径不同之事实并陈）

| 读 | 时点／来源 | REPO 件 | REPO bytes | SUB 件 | SUB bytes | 合计件 | 合计 bytes |
|:-:|:--|--:|--:|--:|--:|--:|--:|
| 读-A | v2.0 实测（`dd3e9806a369` · 2026-10-12 03:20:44） | 1,704 | 54,847,017 | 1,187 | 58,731,756 | 2,891 | 113,578,773 |
| 读-B | 整理登记件 §2（动作完成时点 · 2026-10-18 00:55 前后） | 4,280 | 189,574,034 | 1,276 | 60,166,418 | 5,556 | 249,740,452 |
| 读-C | **本棒实测（2026-10-18 01:05:00）** | **4,282** | **189,657,496** | **1,276** | **60,166,418** | **5,558** | **249,823,914** |

⚠ **0 校正**：读-A（2026-10-12）→ 读-B（2026-10-18）之 +2,665 件差额**逐件归因 ⛔ 0 断言**（其间既有整理后新增成果、亦有他棒并发产出、亦有转移进出）；**差额归因权属 PI／parent 判**。

### §5.2 目录内计数差并列表（`.tmp/` 面 · 三读）

| 面 | REPO `.tmp/` 件 | bytes |
|:--|--:|--:|
| v2.0 实测（2026-10-12） | 441 | 11,375,518 |
| 整理登记件（2026-10-18 · 清走 19 件 `.tmp` 中间件后） | 未单列 | 未单列 |
| **本棒实测** | **2,268** | **122,160,784** |

⚠ **登记件之账外增量 ⛔ 0 断言根因**：本棒 `.tmp/` 件数显著高于 v2.0，**成因**（中间件产出速率 · 白名单备份面 `whitelist_backup_2026_10_17/` 之 **698** 件 · 他棒并发）**本棒 ⛔ 0 分解断言**，仅登记读数。

## §6 · 与整理登记件（`d6b1dc8f8a02`）逐面对齐

| 登记件面 | 登记值 | 本棒实测 | 对齐 |
|:--|:--|:--|:-:|
| §2 两区终态（SUB） | 1,276 件 / 60,166,418 B | 1,276 件 / 60,166,418 B | ✅ **逐字节吻合** |
| §2 两区终态（REPO 件数） | 4,280（+2 自报） | 4,282 | ✅ 件数吻合 |
| §3-1 判据清走 | 89 件（repo 35／sub 54） | 89 行解析；**89/89 已离原位** | ✅ |
| §3-2 本棒自清 | 7 件 | **7/7 已离原位** | ✅ |
| §4-1 净转移 | 141 件（MATCH 141/FAIL 0） | **141/141 新在位且指纹一致；旧残留 0** | ✅ |
| §4-2 回退 | 25 件（RESTORED_MATCH 25/25） | **25/25 已在 REPO；SUB 残留 0** | ✅ |
| §3-3 验道 96/96 | 96/96 | **本棒未核**（⛔ 0 触回收站）| ⚠ 沿用（§9-N-2）|
| §6 拉平目标 ≤1.50:1 | 🔴 未达（3.354:1） | **3.356:1，仍 🔴 未达** | ✅ 一致（⛔ 0 另作可达性判断）|
| §2 字节账（REPO） | 189,574,034 B | 差 **2 B** | ⚠ **D-1** |

## §7 · 今晚增量专章（mtime ≥ **2026-10-17 18:00:00** · **689 件**）

### §7.1 窗口口径与三读

**窗口口径**：mtime ≥ **2026-10-17 18:00:00**（**本棒自定之显式工作切面**，派工单仅给「2026-10-17 晚至 18 凌晨」之定性描述 ⇒ **KD-INV-04**）；本表为 §4 之**子集视图**，**0 重复计数**。

| 读 | 口径 | 件数 | bytes |
|:-:|:--|--:|--:|
| 读-1（**本件采用**） | mtime ≥ 2026-10-17 18:00:00 | **689** | **22,478,908** |
| 读-2 | 2026-10-17 **全日**（00:00 起） | 1,380 | 54,078,477 |
| 读-3 | 2026-10-18（至实测时点） | 42 | 10,754,597 |
| 读-4 | **SUB 区同窗** | **0** | **0** |

📌 **SUB 区 0 增量**之实测事实：SUB 末次 mtime ＝ **2026-10-15 13:01:46** ⇒ 整理转入之 141 件**保留原 mtime**（移动不改时间戳），故**非新写**。

**分时（读-1）**

| 小时 | 件数 | bytes |
|:--|--:|--:|
| 2026-10-17 18 | 67 | 1,233,452 |
| 2026-10-17 19 | 128 | 1,915,534 |
| 2026-10-17 20 | 123 | 2,290,042 |
| 2026-10-17 21 | 77 | 2,630,943 |
| 2026-10-17 22 | 122 | 1,502,378 |
| 2026-10-17 23 | 130 | 2,151,962 |
| 2026-10-18 00 | 42 | 10,754,597 |

**分区面（读-1）**

| 区面 | 件数 | bytes | 备注 |
|:--|--:|--:|:--|
| `.tmp/` | 574 | 18,039,573 | 噪声面 |
| `results/` | 69 | 2,728,544 | 成果面 |
| `pi_rulings/` | 30 | 1,225,599 | 成果面 |
| `.tmp/__pycache__/` | 8 | 235,106 | 噪声面 |
| `（根散件）/` | 4 | 46,772 | 成果面 |
| `tools/__pycache__/` | 2 | 106,870 | 成果面 |
| `tools/` | 2 | 96,444 | 成果面 |

### §7.2 逐件（689 件 · 逐件附 SHA-12）

**面-① `pi_rulings/`（30 件 · 口径令点名之 v85–v89 ＋ B-11 回收件）**

| # | 相对路径 | bytes | mtime | SHA-12 | 备注 |
| --: | :-- | --: | :-- | :-- | :-: |
| 1 | `pi_rulings/_pi_card_answers_register_2026_10_14_b11_recovery.md` | 13,812 | 2026-10-18 00:02:40 | `d224a7380071` | ⭐ 派工单点名 **B-11 回收件**（指代消歧未决 → KD-INV-03） |
| 2 | `pi_rulings/_pi_card_answers_register_2026_10_17_v63_append1.md` | 23,862 | 2026-10-17 18:00:22 | `e566cff9ce9d` |  |
| 3 | `pi_rulings/_pi_card_answers_register_2026_10_17_v64.md` | 48,215 | 2026-10-17 18:25:57 | `02db93851600` |  |
| 4 | `pi_rulings/_pi_card_answers_register_2026_10_17_v65.md` | 34,862 | 2026-10-17 18:52:29 | `361a513b41b2` |  |
| 5 | `pi_rulings/_pi_card_answers_register_2026_10_17_v66.md` | 48,278 | 2026-10-17 18:54:37 | `97b754e4bef8` |  |
| 6 | `pi_rulings/_pi_card_answers_register_2026_10_17_v66_append1.md` | 12,310 | 2026-10-17 19:00:43 | `9cff8adbde16` |  |
| 7 | `pi_rulings/_pi_card_answers_register_2026_10_17_v66_append2.md` | 5,927 | 2026-10-17 19:01:58 | `9d4151dc3053` |  |
| 8 | `pi_rulings/_pi_card_answers_register_2026_10_17_v67.md` | 46,839 | 2026-10-17 19:05:01 | `75b5841a3dfb` |  |
| 9 | `pi_rulings/_pi_card_answers_register_2026_10_17_v68.md` | 49,343 | 2026-10-17 19:13:53 | `da9d5195687a` |  |
| 10 | `pi_rulings/_pi_card_answers_register_2026_10_17_v69.md` | 45,882 | 2026-10-17 19:22:09 | `ff190f0b1f44` |  |
| 11 | `pi_rulings/_pi_card_answers_register_2026_10_17_v70.md` | 41,056 | 2026-10-17 19:25:20 | `8674655fc387` |  |
| 12 | `pi_rulings/_pi_card_answers_register_2026_10_17_v71.md` | 31,504 | 2026-10-17 19:42:40 | `ea23ee2068dd` |  |
| 13 | `pi_rulings/_pi_card_answers_register_2026_10_17_v72.md` | 33,695 | 2026-10-17 19:47:57 | `eaa2535de267` |  |
| 14 | `pi_rulings/_pi_card_answers_register_2026_10_17_v73.md` | 40,176 | 2026-10-17 19:58:04 | `82d6c06b3a0f` |  |
| 15 | `pi_rulings/_pi_card_answers_register_2026_10_17_v74.md` | 47,243 | 2026-10-17 20:02:09 | `f86dbb713d53` |  |
| 16 | `pi_rulings/_pi_card_answers_register_2026_10_17_v75.md` | 45,643 | 2026-10-17 20:15:17 | `1119913b66e4` |  |
| 17 | `pi_rulings/_pi_card_answers_register_2026_10_17_v76.md` | 49,490 | 2026-10-17 20:22:36 | `724b41bf7b46` |  |
| 18 | `pi_rulings/_pi_card_answers_register_2026_10_17_v77.md` | 47,239 | 2026-10-17 20:41:55 | `904c4fc1ce40` |  |
| 19 | `pi_rulings/_pi_card_answers_register_2026_10_17_v78.md` | 57,896 | 2026-10-17 20:46:30 | `11b378afa490` |  |
| 20 | `pi_rulings/_pi_card_answers_register_2026_10_17_v79.md` | 38,119 | 2026-10-17 21:07:57 | `283a697a7704` |  |
| 21 | `pi_rulings/_pi_card_answers_register_2026_10_17_v80.md` | 33,777 | 2026-10-17 21:40:30 | `a40f5698a1da` |  |
| 22 | `pi_rulings/_pi_card_answers_register_2026_10_17_v81.md` | 51,667 | 2026-10-17 22:01:16 | `816a5414a86a` |  |
| 23 | `pi_rulings/_pi_card_answers_register_2026_10_17_v82.md` | 47,749 | 2026-10-17 22:16:05 | `79dd0fdf23c9` |  |
| 24 | `pi_rulings/_pi_card_answers_register_2026_10_17_v83.md` | 49,996 | 2026-10-17 22:32:23 | `e2a67aa39bdd` |  |
| 25 | `pi_rulings/_pi_card_answers_register_2026_10_17_v84.md` | 42,968 | 2026-10-17 22:46:10 | `c565669aadeb` |  |
| 26 | `pi_rulings/_pi_card_answers_register_2026_10_17_v85.md` | 51,362 | 2026-10-17 23:12:28 | `c54c4580baa2` | ⭐ 派工单点名 **v85–v89** |
| 27 | `pi_rulings/_pi_card_answers_register_2026_10_17_v86.md` | 39,039 | 2026-10-17 23:10:53 | `19821507b5b2` | ⭐ 派工单点名 **v85–v89** |
| 28 | `pi_rulings/_pi_card_answers_register_2026_10_17_v87.md` | 56,899 | 2026-10-17 23:35:48 | `346456d03425` | ⭐ 派工单点名 **v85–v89** |
| 29 | `pi_rulings/_pi_card_answers_register_2026_10_17_v88.md` | 39,767 | 2026-10-17 23:35:48 | `061380c8a9fb` | ⭐ 派工单点名 **v85–v89** |
| 30 | `pi_rulings/_pi_card_answers_register_2026_10_17_v89.md` | 50,984 | 2026-10-17 23:53:38 | `b0f09b01f774` | ⭐ 派工单点名 **v85–v89** |

**面-② `results/`（69 件）**

| # | 相对路径 | bytes | mtime | SHA-12 |
| --: | :-- | --: | :-- | :-- |
| 1 | `results/_s3_s5_kd_effect_2026_10_17_append1.md` | 17,624 | 2026-10-17 18:00:22 | `905be2174c52` |
| 2 | `results/_fivezero_final_audit_2026_10_17.md` | 46,339 | 2026-10-17 18:09:49 | `95118aa704db` |
| 3 | `results/_kl_m41_3_verdict_2026_10_17.md` | 33,138 | 2026-10-17 18:25:11 | `5dc4e089f458` |
| 4 | `results/_fail_h0_verdict_2026_10_17.md` | 41,481 | 2026-10-17 18:26:55 | `c8794d87b4b6` |
| 5 | `results/_strict3_verdict_2026_10_17.md` | 41,236 | 2026-10-17 18:28:37 | `d392bd36ec34` |
| 6 | `results/_u_cluster1_verdict_2026_10_17.md` | 40,213 | 2026-10-17 18:37:07 | `0172e2a52c80` |
| 7 | `results/_u_cluster2_verdict_2026_10_17.md` | 47,057 | 2026-10-17 18:38:15 | `4dd0d2f38d46` |
| 8 | `results/_ext5_verdict_2026_10_17.md` | 63,647 | 2026-10-17 18:39:47 | `80a81bd525d4` |
| 9 | `results/_u09_count_caliber_2026_10_17.md` | 24,415 | 2026-10-17 18:52:09 | `cd32d8a84ae6` |
| 10 | `results/_register_correction_batch_and_u14_effect_2026_10_17.md` | 55,316 | 2026-10-17 18:55:21 | `9a94037f80d1` |
| 11 | `results/_kdb2r3_u13_rulings_effect_2026_10_17.md` | 35,207 | 2026-10-17 18:58:09 | `688424929409` |
| 12 | `results/_esc3_esc6_resolution_2026_10_17.md` | 28,717 | 2026-10-17 19:03:44 | `509e52734292` |
| 13 | `results/_gap10_four_rulings_effect_2026_10_17.md` | 35,339 | 2026-10-17 19:05:22 | `b5596dd2abbb` |
| 14 | `results/_u_lock_recalc_2026_10_17.md` | 24,411 | 2026-10-17 19:10:46 | `6793b0b56925` |
| 15 | `results/_kd_u1_u4_rulings_effect_2026_10_17.md` | 30,072 | 2026-10-17 19:13:53 | `4500a4715f3b` |
| 16 | `results/_kd_u5_u6_s3b4_rulings_effect_2026_10_17.md` | 38,534 | 2026-10-17 19:22:09 | `85702808df0c` |
| 17 | `results/_kd_s3b1_verdict_2026_10_17.md` | 45,846 | 2026-10-17 19:22:50 | `ed36d0171672` |
| 18 | `results/_kd1_preexp_contrast_2026_10_17.md` | 27,149 | 2026-10-17 19:23:16 | `351d18d74934` |
| 19 | `results/_kd_s3b5_kd1_esc36_batch_lock_effect_2026_10_17.md` | 48,246 | 2026-10-17 19:25:20 | `3ecf179b83a1` |
| 20 | `results/_u_hface15_18889_lock_register_2026_10_17.md` | 24,452 | 2026-10-17 19:29:51 | `59f8c6c2826b` |
| 21 | `results/_esc5_verdict_2026_10_17.md` | 27,258 | 2026-10-17 19:36:24 | `d970bb175672` |
| 22 | `results/_kd_s3b1_kd1_n7_rulings_effect_2026_10_17.md` | 49,252 | 2026-10-17 19:42:40 | `e09780d24a7a` |
| 23 | `results/_ritt_def_proof_2026_10_17.md` | 23,310 | 2026-10-17 19:47:26 | `5d411ebf07ed` |
| 24 | `results/_esc5_adoption_and_ritt_remeasure_effect_2026_10_17.md` | 34,206 | 2026-10-17 19:50:36 | `e550e344a258` |
| 25 | `results/_ritt_def_adoption_and_remeasure_effect_2026_10_17.md` | 28,232 | 2026-10-17 19:58:52 | `a7539659c5df` |
| 26 | `results/_kd_gap_survey_2026_10_17.md` | 45,716 | 2026-10-17 20:01:00 | `592a50470e76` |
| 27 | `results/_ritt_remeasure_readings_2026_10_17.md` | 23,064 | 2026-10-17 20:10:30 | `16dccc9c0a88` |
| 28 | `results/_kd_gap_resolution_rulings_effect_2026_10_17.md` | 38,813 | 2026-10-17 20:15:17 | `10e40a51c9c1` |
| 29 | `results/_material_root45_remeasure_2026_10_17.md` | 19,477 | 2026-10-17 20:15:44 | `f2a5c4330112` |
| 30 | `results/_kdk45_remeasure_2026_10_17.md` | 31,662 | 2026-10-17 20:17:26 | `25ff6e4f31bc` |
| 31 | `results/_resolution_path_rulings_effect_2026_10_17.md` | 29,195 | 2026-10-17 20:22:36 | `91555b6b7bd6` |
| 32 | `results/_fiveverdict_census_2026_10_17.md` | 31,237 | 2026-10-17 20:23:57 | `0b9512c6b68b` |
| 33 | `results/_gamma_taucert_scope_delimitation_2026_10_17.md` | 37,104 | 2026-10-17 20:30:50 | `7374c29a8d4e` |
| 34 | `results/_face_r_coexist_verdict_2026_10_17.md` | 37,604 | 2026-10-17 20:30:56 | `0fd3788e2d3b` |
| 35 | `results/_freeze_preexp_design_2026_10_17.md` | 40,906 | 2026-10-17 20:30:58 | `d52a5d94a002` |
| 36 | `results/_approval_card_four_rulings_effect_2026_10_17.md` | 50,703 | 2026-10-17 20:43:49 | `8e1b7d6ae996` |
| 37 | `results/_u_720face_lock_register_2026_10_17.md` | 41,007 | 2026-10-17 20:45:32 | `4ed6194729b5` |
| 38 | `results/_census_exit_four_rulings_effect_2026_10_17.md` | 44,267 | 2026-10-17 20:51:12 | `ac0928f38b85` |
| 39 | `results/_af_entity_rules_2026_10_17.md` | 39,994 | 2026-10-17 20:54:54 | `525ae85c1bbc` |
| 40 | `results/_af_rules_approval_effect_2026_10_17.md` | 43,731 | 2026-10-17 21:09:02 | `ce0a2847ad4e` |
| 41 | `results/_kl_m41_3_remeasure_2026_10_17.md` | 36,936 | 2026-10-17 21:31:30 | `20a1ce111547` |
| 42 | `results/_kd_flip_census_2026_10_17.md` | 38,344 | 2026-10-17 21:38:25 | `cbb42aae0865` |
| 43 | `results/_s3_flip_s5_resolution_effect_2026_10_17.md` | 37,073 | 2026-10-17 21:40:02 | `9bd2c6df2834` |
| 44 | `results/_kl_m41_3_reverdict_2026_10_17.md` | 61,667 | 2026-10-17 21:44:34 | `63625672139a` |
| 45 | `results/_n_distinct_proof_2026_10_17.md` | 24,241 | 2026-10-17 21:53:53 | `2b538eba112a` |
| 46 | `results/_kl_m41_3_reverdict_adoption_effect_2026_10_17.md` | 38,651 | 2026-10-17 21:59:26 | `27545e411171` |
| 47 | `results/_af1_attribution_verdict_2026_10_17.md` | 43,259 | 2026-10-17 22:02:25 | `d6d8c488fc33` |
| 48 | `results/_n7_af_relocation_register_2026_10_17.md` | 35,057 | 2026-10-17 22:13:21 | `7a2133c810b1` |
| 49 | `results/_af_flip要件消解_rulings_effect_2026_10_17.md` | 45,096 | 2026-10-17 22:16:05 | `dc5ee48e1f53` |
| 50 | `results/_n_distinct_grain_verdict_2026_10_17.md` | 41,028 | 2026-10-17 22:16:42 | `0abaee4aeefb` |
| 51 | `results/_rpp_perseed_recalc_2026_10_17.md` | 30,617 | 2026-10-17 22:19:42 | `7e693b27c1f7` |
| 52 | `results/_af2_proof_and_grain_scope_effect_2026_10_17.md` | 41,779 | 2026-10-17 22:32:23 | `faee80c8b051` |
| 53 | `results/_af2_5_proof_2026_10_17.md` | 48,208 | 2026-10-17 22:33:28 | `b3c45b4e2ec0` |
| 54 | `results/_af_landing_n7_and_two_cells_effect_2026_10_17.md` | 40,560 | 2026-10-17 22:46:10 | `955222063aa0` |
| 55 | `results/_freeze_preexp_exec_2026_10_17.md` | 34,681 | 2026-10-17 22:51:01 | `547da6852c98` |
| 56 | `results/_poststrip_recalc_2026_10_17.md` | 42,707 | 2026-10-17 22:56:19 | `cfcf430f306c` |
| 57 | `results/_kdb2r2_kd14_merge_governance_2026_10_17.md` | 26,107 | 2026-10-17 23:05:58 | `4fdadf27b70c` |
| 58 | `results/_af_complete_landing_effect_2026_10_17.md` | 54,092 | 2026-10-17 23:11:41 | `14e4181c5b69` |
| 59 | `results/_pending_pack_four_rulings_effect_2026_10_17.md` | 27,925 | 2026-10-17 23:12:28 | `9572516d82e7` |
| 60 | `results/_freeze_criterion_rewire_design_2026_10_17.md` | 42,399 | 2026-10-17 23:28:26 | `02c385de48ac` |
| 61 | `results/_root_session_history_memo_main_2026_10_14.md` | 132,833 | 2026-10-17 23:33:48 | `21f5284adcdc` |
| 62 | `results/_stage_sequence_ruling_effect_2026_10_17.md` | 18,115 | 2026-10-17 23:33:48 | `b582bde59d6d` |
| 63 | `results/_freeze_face_four_rulings_effect_2026_10_17.md` | 41,068 | 2026-10-17 23:35:48 | `1e512ea146d3` |
| 64 | `results/_harness_mask_correct_value_validation_2026_10_17.md` | 21,741 | 2026-10-17 23:36:19 | `b7d638ebef6e` |
| 65 | `results/_merge_govern_approval_and_eps1_release_effect_2026_10_17.md` | 55,555 | 2026-10-17 23:36:49 | `58727d1eec71` |
| 66 | `results/_freeze_rewire_approval_effect_2026_10_17.md` | 62,895 | 2026-10-17 23:53:38 | `8fc84dd44b6b` |
| 67 | `results/_freeze_preexp_exec_r2_2026_10_17.md` | 52,887 | 2026-10-17 23:56:27 | `fd3656a22b1c` |
| 68 | `results/_kd_u6_readside_rewire_validation_2026_10_17.md` | 24,961 | 2026-10-17 23:59:20 | `751205f0368f` |
| 69 | `results/_stage3_r2_cleanup_register_2026_10_18.md` | 62,885 | 2026-10-18 00:58:56 | `d6b1dc8f8a02` |

📌 **四型归属 ⛔ 0 按语义分类**（派工单第 ③ 项所称「生效落账／设计／验真／登记件」之边界未给判据词表 ⇒ **A-3 未决**）；上表**一律按件名逐字**呈出，四型归属**留 PI 判**。

**面-③ `tools/` ＋ 根散件（8 件 · 含派工单点名之两码件改造）**

| # | 相对路径 | bytes | mtime | SHA-12 | 备注 |
| --: | :-- | --: | :-- | :-- | :-: |
| 1 | `_kd_flip_anchor_scan.py` | 2,575 | 2026-10-17 21:31:33 | `9560a4fb4121` |  |
| 2 | `_kd_flip_kdcensus.py` | 3,541 | 2026-10-17 21:34:10 | `ff11e0c650d8` |  |
| 3 | `_kd_flip_write.py` | 38,829 | 2026-10-17 21:38:16 | `e3063681d015` |  |
| 4 | `_kd_flip_verify.py` | 1,827 | 2026-10-17 21:38:33 | `5bbdc66e0855` |  |
| 5 | `tools/exp_harness.py` | 45,548 | 2026-10-17 23:29:15 | `27cb200220e0` | ⭐ 派工单点名 **`27cb200220e0`** —— **本棒实测指纹吻合** ✅ |
| 6 | `tools/__pycache__/exp_harness.cpython-314.pyc` | 44,064 | 2026-10-17 23:30:50 | `0a53046bc52d` | 编译期产物（字节码） |
| 7 | `tools/distortion_calculator.py` | 50,896 | 2026-10-17 23:55:07 | `ae7ff6e0bac5` | ⭐ 派工单点名 **`ae7ff6e0bac5`** —— **本棒实测指纹吻合** ✅ |
| 8 | `tools/__pycache__/distortion_calculator.cpython-314.pyc` | 62,806 | 2026-10-17 23:55:51 | `79d8dc801d51` | 编译期产物（字节码） |

**面-④ `.tmp/` 证据载体面（582 件）**

| 项 | 实测 |
|:--|:--|
| 件数／bytes | **582 / 18,274,679** |
| 其中 `_r2_tool_*`（③段-R2 之棒） | **38** |
| 其余（其他棒之检索/证据/编译中间件） | **544** |

| 扩展名 | 件数 | bytes |
|:--|--:|--:|
| `py` | 316 | 3,457,283 |
| `txt` | 184 | 607,321 |
| `md` | 37 | 1,218,554 |
| `json` | 32 | 12,030,247 |
| `pyc` | 8 | 235,106 |
| `jsonl` | 4 | 724,406 |
| `ps1` | 1 | 1,762 |

| # | 相对路径 | bytes | mtime | SHA-12 |
| --: | :-- | --: | :-- | :-- |
| 1 | `.tmp/dw63_write_append1.py` | 42,008 | 2026-10-17 18:00:16 | `352000396c3c` |
| 2 | `.tmp/dw63_verify_append1.py` | 5,979 | 2026-10-17 18:00:34 | `ce52bcfbfc2b` |
| 3 | `.tmp/dw63_verify_append1.out.txt` | 5,335 | 2026-10-17 18:00:47 | `8cba56d5cb6b` |
| 4 | `.tmp/ea_fivezero_write1.py` | 46,983 | 2026-10-17 18:09:41 | `6253fe226a50` |
| 5 | `.tmp/d64_probe1.py` | 2,221 | 2026-10-17 18:22:01 | `e7e74bfe920e` |
| 6 | `.tmp/d64_scan.py` | 1,873 | 2026-10-17 18:22:36 | `5484e7b0b941` |
| 7 | `.tmp/d64_time.py` | 1,220 | 2026-10-17 18:23:00 | `e2539091823a` |
| 8 | `.tmp/klm41_3_verdict_write_2026_10_17.py` | 34,041 | 2026-10-17 18:25:02 | `d4c4d8b41569` |
| 9 | `.tmp/d64_write.py` | 48,462 | 2026-10-17 18:25:44 | `4f8fa8459b5d` |
| 10 | `.tmp/d64_verify.py` | 2,962 | 2026-10-17 18:26:08 | `96d1a19b71f2` |
| 11 | `.tmp/d64_verify.out.txt` | 1,298 | 2026-10-17 18:26:14 | `2c6f3525290b` |
| 12 | `.tmp/vk_fail_h0_verdict_write_2026_10_17.py` | 42,450 | 2026-10-17 18:26:48 | `5fec803e4c81` |
| 13 | `.tmp/vk_fail_h0_readback_2026_10_17.txt` | 1,218 | 2026-10-17 18:27:09 | `c8df4d40dd29` |
| 14 | `.tmp/_strict3_writer_2026_10_17.py` | 41,981 | 2026-10-17 18:28:07 | `2efbf49ae4fe` |
| 15 | `.tmp/u_cluster1_write_2026_10_17.py` | 40,926 | 2026-10-17 18:36:58 | `4980f4d7e7af` |
| 16 | `.tmp/vk_ext5_write_2026_10_17.py` | 61,083 | 2026-10-17 18:38:09 | `419557cf5ce0` |
| 17 | `.tmp/d65_probe1.py` | 3,589 | 2026-10-17 18:47:25 | `a6ad2cea883f` |
| 18 | `.tmp/d65_probe2.py` | 1,813 | 2026-10-17 18:47:49 | `426977af0830` |
| 19 | `.tmp/d65_probe2.out.txt` | 3,308 | 2026-10-17 18:47:57 | `520db5bf59ef` |
| 20 | `.tmp/d65_probe3.py` | 4,089 | 2026-10-17 18:49:36 | `1597a575153d` |
| 21 | `.tmp/d65_probe3.out.txt` | 3,006 | 2026-10-17 18:49:45 | `39545068509b` |
| 22 | `.tmp/d65_probe4.py` | 2,273 | 2026-10-17 18:50:15 | `54eba478ef4e` |
| 23 | `.tmp/d65_probe4.out.txt` | 2,464 | 2026-10-17 18:50:26 | `c7de1a8044c0` |
| 24 | `.tmp/dw66_probe_a.py` | 1,239 | 2026-10-17 18:50:49 | `eb26c4d5deea` |
| 25 | `.tmp/dw66_probe_b.py` | 848 | 2026-10-17 18:51:08 | `90f88b6412fb` |
| 26 | `.tmp/dw66_probe_scan.py` | 1,537 | 2026-10-17 18:51:34 | `32d8fd5bf9d0` |
| 27 | `.tmp/dw66_probe_scan2.py` | 1,803 | 2026-10-17 18:51:52 | `be57aaa77ed7` |
| 28 | `.tmp/dw66_probe_scan_out.txt` | 1,217 | 2026-10-17 18:51:54 | `bbd0335e41c8` |
| 29 | `.tmp/d65_write1.py` | 36,939 | 2026-10-17 18:52:21 | `d7c451d2638d` |
| 30 | `.tmp/dw66_write_v66.py` | 49,816 | 2026-10-17 18:54:32 | `ac42765cc15b` |
| 31 | `.tmp/d65_write2.py` | 57,693 | 2026-10-17 18:55:13 | `65a872dd4fa6` |
| 32 | `.tmp/d65_verify.py` | 8,800 | 2026-10-17 18:55:38 | `7d5472188ed7` |
| 33 | `.tmp/d65_verify.out.txt` | 5,922 | 2026-10-17 18:55:44 | `6a2c444b3b66` |
| 34 | `.tmp/dw67_probe_a.py` | 3,381 | 2026-10-17 18:56:54 | `ccffe9dd9be2` |
| 35 | `.tmp/dw66_diag.py` | 551 | 2026-10-17 18:56:56 | `1a48f593f24c` |
| 36 | `.tmp/dw66_diag.txt` | 652 | 2026-10-17 18:56:56 | `fec7ddfa329d` |
| 37 | `.tmp/dw67_probe_a_out.txt` | 2,464 | 2026-10-17 18:57:02 | `4480224ea3a3` |
| 38 | `.tmp/dw67_probe_b.py` | 3,557 | 2026-10-17 18:57:17 | `2ead05c573de` |
| 39 | `.tmp/dw67_probe_b_out.txt` | 1,684 | 2026-10-17 18:57:31 | `e7bbf74cece4` |
| 40 | `.tmp/dw66_diag2.py` | 378 | 2026-10-17 18:57:39 | `a8262c6dc57c` |
| 41 | `.tmp/dw66_diag2.txt` | 957 | 2026-10-17 18:57:39 | `a70bb55e5f58` |
| 42 | `.tmp/dw67_probe_c.py` | 1,251 | 2026-10-17 18:57:39 | `9333c129be22` |
| 43 | `.tmp/dw66_fix.py` | 692 | 2026-10-17 18:58:03 | `68cba4a108a3` |
| 44 | `.tmp/dw67_probe_c_out.txt` | 2,987 | 2026-10-17 18:58:04 | `80b412b6f4e5` |
| 45 | `.tmp/dw66_write_effect.py` | 36,495 | 2026-10-17 18:58:09 | `c80cde71954c` |
| 46 | `.tmp/dw66_verify.py` | 3,152 | 2026-10-17 18:58:26 | `41e9d50962f1` |
| 47 | `.tmp/dw66_verify.out.txt` | 1,781 | 2026-10-17 18:58:33 | `6853deb4c67d` |
| 48 | `.tmp/dw66_verify2.out.txt` | 1,518 | 2026-10-17 18:58:53 | `ee4d38c06996` |
| 49 | `.tmp/dw66_verify2.py` | 1,529 | 2026-10-17 18:58:53 | `d6e8db9a0fd8` |
| 50 | `.tmp/dw66_recheck.py` | 1,106 | 2026-10-17 18:59:16 | `8c860537dde9` |
| 51 | `.tmp/dw66_recheck.out.txt` | 911 | 2026-10-17 18:59:23 | `4c44d3915202` |
| 52 | `.tmp/dw66_fix2.py` | 1,120 | 2026-10-17 18:59:38 | `ac06906ed651` |
| 53 | `.tmp/dw66_write_append1.py` | 13,075 | 2026-10-17 19:00:42 | `aeb5c024e321` |
| 54 | `.tmp/dw66_verify3.out.txt` | 894 | 2026-10-17 19:00:59 | `255cdd522e5d` |
| 55 | `.tmp/dw66_verify3.py` | 1,452 | 2026-10-17 19:00:59 | `f15f0d441ceb` |
| 56 | `.tmp/dw66_dir.py` | 627 | 2026-10-17 19:01:25 | `befd9129f0c6` |
| 57 | `.tmp/dw66_dir.txt` | 5,734 | 2026-10-17 19:01:26 | `1fb97ad851b5` |
| 58 | `.tmp/dw66_write_append2.py` | 6,584 | 2026-10-17 19:01:57 | `627d4a59b169` |
| 59 | `.tmp/dw66_final.py` | 1,214 | 2026-10-17 19:02:07 | `43a2db55bdb8` |
| 60 | `.tmp/dw66_final.txt` | 860 | 2026-10-17 19:02:07 | `4fb3ca55eea4` |
| 61 | `.tmp/esc36_write.py` | 29,232 | 2026-10-17 19:03:35 | `4dfb6a7ade55` |
| 62 | `.tmp/dw68_probe_a.py` | 2,117 | 2026-10-17 19:04:04 | `cc7711e63ff0` |
| 63 | `.tmp/u_lock_recalc_probe_hashscan.py` | 1,284 | 2026-10-17 19:04:05 | `f44d4f11cbd8` |
| 64 | `.tmp/dw68_probe_b.py` | 1,106 | 2026-10-17 19:04:22 | `9b6977c86b12` |
| 65 | `.tmp/dw67_write_v67.py` | 48,826 | 2026-10-17 19:04:51 | `6f384c2ff037` |
| 66 | `.tmp/dw68_probe_c.py` | 1,134 | 2026-10-17 19:05:02 | `f05448b67087` |
| 67 | `.tmp/dw67_write_effect.py` | 36,932 | 2026-10-17 19:05:13 | `3486db943f29` |
| 68 | `.tmp/dw67_verify.py` | 2,815 | 2026-10-17 19:05:17 | `94728ace730a` |
| 69 | `.tmp/dw67_verify.out.txt` | 2,116 | 2026-10-17 19:05:23 | `435a27e85d97` |
| 70 | `.tmp/dw68_probe_d.py` | 1,854 | 2026-10-17 19:05:23 | `63f37c940db4` |
| 71 | `.tmp/dw68_probe_d_out.txt` | 1,668 | 2026-10-17 19:05:26 | `bd76566236ef` |
| 72 | `.tmp/u_lock_recalc_probe_closedform.py` | 3,220 | 2026-10-17 19:06:20 | `d86d6a2a571d` |
| 73 | `.tmp/dw68_write.py` | 5,299 | 2026-10-17 19:06:32 | `5307abebb39a` |
| 74 | `.tmp/u_lock_recalc_write.py` | 24,715 | 2026-10-17 19:10:39 | `8af7de4beb95` |
| 75 | `.tmp/d69_probe1.py` | 2,159 | 2026-10-17 19:10:58 | `140397edd7f3` |
| 76 | `.tmp/u_lock_recalc_verify.py` | 2,009 | 2026-10-17 19:11:44 | `6d9a0828458c` |
| 77 | `.tmp/d69_probe2.py` | 1,520 | 2026-10-17 19:11:56 | `b8fe0c9392c5` |
| 78 | `.tmp/dw68_write.out.txt` | 4,027 | 2026-10-17 19:12:08 | `cb26534eb724` |
| 79 | `.tmp/d69_probe3.py` | 1,459 | 2026-10-17 19:12:20 | `1437ced4cc3d` |
| 80 | `.tmp/d69_probe4.py` | 2,596 | 2026-10-17 19:12:39 | `0f5e1543dadc` |
| 81 | `.tmp/dw68_verify.py` | 3,523 | 2026-10-17 19:13:07 | `e4437867415a` |
| 82 | `.tmp/dw68_payload_effect.md` | 30,133 | 2026-10-17 19:13:42 | `cb1723499a25` |
| 83 | `.tmp/dw68_payload_v68.md` | 49,383 | 2026-10-17 19:13:42 | `d60379221f29` |
| 84 | `.tmp/dw68_verify.out.txt` | 1,945 | 2026-10-17 19:13:53 | `e11fc3b79e4b` |
| 85 | `.tmp/dw68_final.out.txt` | 1,098 | 2026-10-17 19:14:23 | `4639d4ecd6f3` |
| 86 | `.tmp/dw68_final.py` | 2,672 | 2026-10-17 19:14:23 | `796442edbec1` |
| 87 | `.tmp/d69_effect_rev1.md` | 35,878 | 2026-10-17 19:16:38 | `aa8ba7c13629` |
| 88 | `.tmp/d69_v69_rev1.md` | 40,644 | 2026-10-17 19:16:38 | `c3621b68a0e7` |
| 89 | `.tmp/d69_verify.py` | 3,364 | 2026-10-17 19:16:47 | `efbbf7cdb7d6` |
| 90 | `.tmp/d69_verify.out.txt` | 2,646 | 2026-10-17 19:16:53 | `e42d7b6b61a2` |
| 91 | `.tmp/d69_verify2.py` | 2,098 | 2026-10-17 19:17:07 | `1e1a4c73e0ab` |
| 92 | `.tmp/d69_verify2.out.txt` | 876 | 2026-10-17 19:17:35 | `c6288995ff7d` |
| 93 | `.tmp/d70_write.py` | 70,471 | 2026-10-17 19:17:47 | `33bed6a60c0e` |
| 94 | `.tmp/d70_write.out.txt` | 3,464 | 2026-10-17 19:18:02 | `db2387d43824` |
| 95 | `.tmp/d69_effect_rev2.md` | 37,867 | 2026-10-17 19:20:04 | `aadbf65b1a1d` |
| 96 | `.tmp/d69_v69_rev2.md` | 44,203 | 2026-10-17 19:20:04 | `f85ec92d75bc` |
| 97 | `.tmp/d69_final.py` | 3,941 | 2026-10-17 19:20:18 | `8f0a1e82406c` |
| 98 | `.tmp/d70_patch1.py` | 15,503 | 2026-10-17 19:20:35 | `fe0291239e63` |
| 99 | `.tmp/d70_patch1.out.txt` | 0 | 2026-10-17 19:20:44 | `e3b0c44298fc` |
| 100 | `.tmp/d70_apply.py` | 1,747 | 2026-10-17 19:21:01 | `9b4cfc6dd058` |
| 101 | `.tmp/kd1_preexp_contrast_probe.py` | 7,910 | 2026-10-17 19:21:13 | `27f4aea260c6` |
| 102 | `.tmp/d70_fix_v70.json` | 9,245 | 2026-10-17 19:21:19 | `c385466bca09` |
| 103 | `.tmp/d69_write.py` | 85,582 | 2026-10-17 19:21:31 | `c3b6cf60889b` |
| 104 | `.tmp/d70_fix_eff.json` | 10,500 | 2026-10-17 19:21:38 | `47de9f384117` |
| 105 | `.tmp/d70_apply2.py` | 2,514 | 2026-10-17 19:22:03 | `6be489416e71` |
| 106 | `.tmp/d69_final.out.txt` | 2,073 | 2026-10-17 19:22:10 | `359924630a53` |
| 107 | `.tmp/d70_err_v70.md` | 5,962 | 2026-10-17 19:22:17 | `5750451d0993` |
| 108 | `.tmp/d70_err_eff.md` | 5,873 | 2026-10-17 19:22:36 | `d463a8b475db` |
| 109 | `.tmp/vk_kds3b1_write_2026_10_17.py` | 49,892 | 2026-10-17 19:22:36 | `c83a8b490d42` |
| 110 | `.tmp/d70_apply.out.txt` | 1,480 | 2026-10-17 19:22:46 | `f5e64973a36e` |
| 111 | `.tmp/d70_fix_eff2.json` | 3,201 | 2026-10-17 19:23:01 | `356307b76db2` |
| 112 | `.tmp/kd1_body.md` | 27,149 | 2026-10-17 19:23:06 | `eb652774ffd9` |
| 113 | `.tmp/d70_apply3.out.txt` | 310 | 2026-10-17 19:23:13 | `9c24b079e119` |
| 114 | `.tmp/d70_apply3.py` | 1,010 | 2026-10-17 19:23:13 | `fcc49b4487d7` |
| 115 | `.tmp/_write_kd1.py` | 796 | 2026-10-17 19:23:16 | `7dff16b36a84` |
| 116 | `.tmp/d70_final.py` | 890 | 2026-10-17 19:23:25 | `426ac9b71216` |
| 117 | `.tmp/d70_apply4.py` | 1,766 | 2026-10-17 19:23:44 | `8ca21abb7758` |
| 118 | `.tmp/d70_apply4.out.txt` | 212 | 2026-10-17 19:23:45 | `bec02e8ecf5d` |
| 119 | `.tmp/d70_final.out.txt` | 2,782 | 2026-10-17 19:23:58 | `125b1901bc58` |
| 120 | `.tmp/d70_final2.py` | 2,166 | 2026-10-17 19:23:58 | `72167147ccca` |
| 121 | `.tmp/d70_drift.py` | 778 | 2026-10-17 19:24:19 | `2e43ebd92169` |
| 122 | `.tmp/d70_driftfix.out.txt` | 1,076 | 2026-10-17 19:24:52 | `88b996edce90` |
| 123 | `.tmp/d70_driftfix.py` | 8,090 | 2026-10-17 19:24:52 | `e6b4593f36d9` |
| 124 | `.tmp/d70_drift_v70.md` | 2,292 | 2026-10-17 19:25:01 | `79fc1550c7f5` |
| 125 | `.tmp/d70_drift_eff.md` | 2,202 | 2026-10-17 19:25:08 | `664759da9f10` |
| 126 | `.tmp/d70_append.py` | 1,034 | 2026-10-17 19:25:20 | `084cae736d8b` |
| 127 | `.tmp/d70_final_verify.out.txt` | 602 | 2026-10-17 19:25:20 | `33182aedc627` |
| 128 | `.tmp/d70_z.out.txt` | 554 | 2026-10-17 19:25:32 | `e8563956bb97` |
| 129 | `.tmp/d70_z.py` | 1,607 | 2026-10-17 19:25:32 | `d600a30fd1ef` |
| 130 | `.tmp/u1889_verify.py` | 477 | 2026-10-17 19:26:06 | `485b2498388b` |
| 131 | `.tmp/u1889_write.py` | 23,022 | 2026-10-17 19:27:55 | `41a3a95e0dc0` |
| 132 | `.tmp/u1889_selfcheck.py` | 2,977 | 2026-10-17 19:28:34 | `f1880cef7fbb` |
| 133 | `.tmp/u1889_selfcheck_out.txt` | 1,619 | 2026-10-17 19:28:38 | `b141543b767c` |
| 134 | `.tmp/u1889_finalize.py` | 3,306 | 2026-10-17 19:28:55 | `81a3e8c0e8f3` |
| 135 | `.tmp/u1889_final.py` | 3,327 | 2026-10-17 19:29:11 | `a3415c482849` |
| 136 | `.tmp/u1889_final2.py` | 3,744 | 2026-10-17 19:29:30 | `1a158989c112` |
| 137 | `.tmp/u1889_final_out.txt` | 1,683 | 2026-10-17 19:29:55 | `fc1f2b476a1a` |
| 138 | `.tmp/esc5_verdict_write_2026_10_17.py` | 27,843 | 2026-10-17 19:36:18 | `10573a36e3e9` |
| 139 | `.tmp/d71_probe.py` | 5,686 | 2026-10-17 19:37:08 | `0e58b81d7801` |
| 140 | `.tmp/d71_probe.out.txt` | 6,174 | 2026-10-17 19:37:17 | `74a4aeea6a9c` |
| 141 | `.tmp/d71_write.py` | 84,687 | 2026-10-17 19:42:33 | `eef47343f274` |
| 142 | `.tmp/d71_write.out.txt` | 983 | 2026-10-17 19:42:40 | `0290b419b61b` |
| 143 | `.tmp/dw72_probe1.py` | 1,084 | 2026-10-17 19:43:10 | `127754f2b66a` |
| 144 | `.tmp/d71_check.py` | 2,058 | 2026-10-17 19:43:49 | `5434c5d33be3` |
| 145 | `.tmp/dw72_probe2.py` | 2,804 | 2026-10-17 19:44:07 | `b5d50e29f867` |
| 146 | `.tmp/dw72_probe3.py` | 2,073 | 2026-10-17 19:44:25 | `7cd02ec22927` |
| 147 | `.tmp/dw72_probe4.py` | 1,965 | 2026-10-17 19:44:56 | `a45fecd0442b` |
| 148 | `.tmp/dw72_write1.py` | 34,422 | 2026-10-17 19:47:50 | `351b5b79205a` |
| 149 | `.tmp/dw72_write2.py` | 34,917 | 2026-10-17 19:50:26 | `1197bb550042` |
| 150 | `.tmp/dw72_verify.py` | 5,583 | 2026-10-17 19:51:07 | `dfcfbd97f541` |
| 151 | `.tmp/ritt_remeasure_freeze_2026_10_17.json` | 6,636 | 2026-10-17 19:53:40 | `a41f38631fab` |
| 152 | `.tmp/ritt_remeasure_collect_2026_10_17.py` | 33,524 | 2026-10-17 19:54:24 | `38b2cecb2d16` |
| 153 | `.tmp/__pycache__/ritt_remeasure_collect_2026_10_17.cpython-314.pyc` | 43,831 | 2026-10-17 19:54:38 | `8823a3df0a45` |
| 154 | `.tmp/dw74_probe1.py` | 2,861 | 2026-10-17 19:57:02 | `bd4bc12aa50a` |
| 155 | `.tmp/dw74_probe1.out.txt` | 3,090 | 2026-10-17 19:57:12 | `a25f946975a5` |
| 156 | `.tmp/dw74_probe2.py` | 3,312 | 2026-10-17 19:57:38 | `8434e940f7b6` |
| 157 | `.tmp/dw74_probe2.out.txt` | 2,558 | 2026-10-17 19:57:53 | `3159fc4722ce` |
| 158 | `.tmp/dw74_write.py` | 46,112 | 2026-10-17 20:00:56 | `105f5cd277c5` |
| 159 | `.tmp/dw74_verify.py` | 1,449 | 2026-10-17 20:01:10 | `f3deae6de211` |
| 160 | `.tmp/dw74_verify2.py` | 2,096 | 2026-10-17 20:01:40 | `a2ba7366fccb` |
| 161 | `.tmp/dw74_verify.out.txt` | 2,896 | 2026-10-17 20:01:45 | `acc64edbbf18` |
| 162 | `.tmp/dw74_勘误追加.py` | 2,829 | 2026-10-17 20:02:03 | `848e1ff5e9ca` |
| 163 | `.tmp/dw75_run1.py` | 3,340 | 2026-10-17 20:07:50 | `6be91fbd5bae` |
| 164 | `.tmp/dw75_probe1.out.txt` | 8,690 | 2026-10-17 20:08:11 | `af26bc4323b7` |
| 165 | `.tmp/dw75_probe1.py` | 17 | 2026-10-17 20:08:11 | `4a309a6ca130` |
| 166 | `.tmp/dw75_run2.py` | 4,174 | 2026-10-17 20:08:31 | `4eb1d28abe74` |
| 167 | `.tmp/dw75_probe2.out.txt` | 2,767 | 2026-10-17 20:08:37 | `8fb37805b2a1` |
| 168 | `.tmp/dw75_probe2.py` | 17 | 2026-10-17 20:08:37 | `1dcb180e74da` |
| 169 | `.tmp/ritt_remeasure_collect_log_2026_10_17.txt` | 10,627 | 2026-10-17 20:08:38 | `eac10421dcad` |
| 170 | `.tmp/ritt_remeasure_llm_calls_2026_10_17.jsonl` | 106,119 | 2026-10-17 20:08:38 | `3e68a203fa06` |
| 171 | `.tmp/ritt_remeasure_measurement_2026_10_17.json` | 325,531 | 2026-10-17 20:08:38 | `29bb4c4a8bca` |
| 172 | `.tmp/dw75_run3.py` | 2,498 | 2026-10-17 20:08:52 | `46f946bb5762` |
| 173 | `.tmp/dw75_probe3.out.txt` | 2,386 | 2026-10-17 20:09:04 | `c3e06067273b` |
| 174 | `.tmp/dw75_probe3.py` | 17 | 2026-10-17 20:09:04 | `091a7849c520` |
| 175 | `.tmp/root45_s11s12_freeze_write_2026_10_17.py` | 4,627 | 2026-10-17 20:12:38 | `ed818a87408f` |
| 176 | `.tmp/kdk45_r1_recompute_2026_10_17.py` | 17,711 | 2026-10-17 20:12:42 | `77a392bb0d57` |
| 177 | `.tmp/root45_s11s12_freeze_2026_10_17.json` | 2,941 | 2026-10-17 20:12:47 | `a830d4e73af2` |
| 178 | `.tmp/kdk45_r1_recompute_2026_10_17.json` | 9,111 | 2026-10-17 20:12:50 | `64c911198107` |
| 179 | `.tmp/root45_s11s12_collect_2026_10_17.py` | 11,994 | 2026-10-17 20:13:02 | `09f11b997cf2` |
| 180 | `.tmp/kdk45_r3_m2t5_measure_2026_10_17.py` | 12,351 | 2026-10-17 20:13:16 | `a34c6884a2ed` |
| 181 | `.tmp/root45_s11s12_llm_calls_2026_10_17.jsonl` | 2,484 | 2026-10-17 20:13:22 | `d34cc2373f0f` |
| 182 | `.tmp/root45_s11s12_measurement_2026_10_17.json` | 8,661 | 2026-10-17 20:13:22 | `2ec5ad7ce1e9` |
| 183 | `.tmp/dw75_write1.py` | 81,327 | 2026-10-17 20:13:31 | `abdbd55abe15` |
| 184 | `.tmp/kdk45_r3_m2t5_calls_2026_10_17.jsonl` | 2,232 | 2026-10-17 20:13:42 | `91db46a87830` |
| 185 | `.tmp/dw75_verify.py` | 2,313 | 2026-10-17 20:13:45 | `9625fabf75f7` |
| 186 | `.tmp/kdk45_r3_verify_2026_10_17.py` | 4,039 | 2026-10-17 20:13:58 | `c07a79494a2d` |
| 187 | `.tmp/kdk45_r3_m2t5_measurement_2026_10_17.json` | 7,470 | 2026-10-17 20:14:07 | `61f904cba24b` |
| 188 | `.tmp/dw75_probe4.out.txt` | 1,166 | 2026-10-17 20:14:20 | `3a334272ea39` |
| 189 | `.tmp/dw75_probe4.py` | 17 | 2026-10-17 20:14:20 | `00d9a33c228b` |
| 190 | `.tmp/dw75_run4.py` | 1,757 | 2026-10-17 20:14:20 | `684d336e52ef` |
| 191 | `.tmp/dw75_patch1.py` | 3,095 | 2026-10-17 20:14:33 | `a653f5054eec` |
| 192 | `.tmp/dw75_patch2.py` | 3,840 | 2026-10-17 20:15:03 | `cda17db939e3` |
| 193 | `.tmp/dw75_verify.out.txt` | 1,511 | 2026-10-17 20:15:18 | `1ae1abd67e57` |
| 194 | `.tmp/dw76_probe0.py` | 1,420 | 2026-10-17 20:15:19 | `23db85bb14eb` |
| 195 | `.tmp/root45_write_2026_10_17.py` | 21,205 | 2026-10-17 20:15:36 | `3eb66353d385` |
| 196 | `.tmp/dw76_probe1.py` | 2,306 | 2026-10-17 20:15:49 | `c67167b4362e` |
| 197 | `.tmp/dw76_probe1.out.txt` | 3,948 | 2026-10-17 20:15:55 | `6a978acda0e7` |
| 198 | `.tmp/dw76_probe2.py` | 647 | 2026-10-17 20:16:14 | `f5f386e64665` |
| 199 | `.tmp/dw76_probe2.out.txt` | 198 | 2026-10-17 20:16:18 | `997dbed7dfaf` |
| 200 | `.tmp/kdk45_write_doc_2026_10_17.py` | 31,791 | 2026-10-17 20:16:35 | `ed9ef1a61a56` |
| 201 | `.tmp/dw76_probe3.out.txt` | 3,992 | 2026-10-17 20:17:08 | `e0ee21457eb4` |
| 202 | `.tmp/dw76_probe3.py` | 627 | 2026-10-17 20:17:08 | `d4c30827efef` |
| 203 | `.tmp/kdk45_final_check_2026_10_17.py` | 882 | 2026-10-17 20:17:51 | `cdfe7086f0df` |
| 204 | `.tmp/dw76_verify.py` | 1,700 | 2026-10-17 20:21:34 | `0d472ee51177` |
| 205 | `.tmp/dw76_fffd.out.txt` | 363 | 2026-10-17 20:21:54 | `bfa97f2b6be8` |
| 206 | `.tmp/dw76_fffd.py` | 625 | 2026-10-17 20:21:54 | `c8d790d23b19` |
| 207 | `.tmp/dw76_write1.py` | 50,812 | 2026-10-17 20:22:19 | `92518b3309a0` |
| 208 | `.tmp/dw76_write2.py` | 30,718 | 2026-10-17 20:22:26 | `d6153aeb2125` |
| 209 | `.tmp/dw76_verify.out.txt` | 636 | 2026-10-17 20:22:36 | `8ab77576ed65` |
| 210 | `.tmp/dw76_cross.out.txt` | 182 | 2026-10-17 20:22:58 | `71c6005724cf` |
| 211 | `.tmp/dw76_cross.py` | 1,133 | 2026-10-17 20:22:58 | `8da3435cc701` |
| 212 | `.tmp/gts_fix.py` | 392 | 2026-10-17 20:30:34 | `fb44e889bce8` |
| 213 | `.tmp/_frc_content.md` | 37,604 | 2026-10-17 20:30:39 | `0fd3788e2d3b` |
| 214 | `.tmp/gts_write.py` | 38,639 | 2026-10-17 20:30:42 | `878a4597dda2` |
| 215 | `.tmp/freeze_preexp_design_write_2026_10_17.py` | 42,362 | 2026-10-17 20:30:47 | `5a6fde945f71` |
| 216 | `.tmp/_frc_write.py` | 1,495 | 2026-10-17 20:30:49 | `1136d247a7c6` |
| 217 | `.tmp/gts_verify.py` | 986 | 2026-10-17 20:30:55 | `a7242e906204` |
| 218 | `.tmp/dw77_probe0.py` | 3,578 | 2026-10-17 20:38:36 | `639aad9f614a` |
| 219 | `.tmp/dw77_probe0.out.txt` | 1,255 | 2026-10-17 20:38:58 | `16eaf3d90cc8` |
| 220 | `.tmp/dw77_probe1.py` | 4,652 | 2026-10-17 20:39:17 | `3a871fd4c0c1` |
| 221 | `.tmp/dw77_probe1.out.txt` | 2,767 | 2026-10-17 20:39:33 | `e03a2ad13211` |
| 222 | `.tmp/u720_probe1.py` | 2,411 | 2026-10-17 20:40:41 | `663fab4c48d6` |
| 223 | `.tmp/u720_probe1.out.txt` | 2,397 | 2026-10-17 20:40:42 | `3aa862e204af` |
| 224 | `.tmp/kdm413_rm_preflight_2026_10_17.py` | 9,459 | 2026-10-17 20:41:03 | `4a2e00cb511b` |
| 225 | `.tmp/kdm413_rm_preflight_2026_10_17.json` | 5,212 | 2026-10-17 20:41:13 | `998c92f003b1` |
| 226 | `.tmp/dw78_probe0.py` | 2,945 | 2026-10-17 20:41:23 | `38ca1cadc48a` |
| 227 | `.tmp/dw78_probe0.out.txt` | 2,065 | 2026-10-17 20:41:32 | `fada6ea8def6` |
| 228 | `.tmp/u720_probe2.py` | 501 | 2026-10-17 20:41:37 | `ab9948ef7584` |
| 229 | `.tmp/dw77_write1.py` | 47,878 | 2026-10-17 20:41:47 | `f6b520547f46` |
| 230 | `.tmp/kdm413_rm_freeze_2026_10_17.py` | 14,868 | 2026-10-17 20:41:59 | `af97eed6a9f1` |
| 231 | `.tmp/kdm413_rm_caliber_decl_2026_10_17.json` | 4,334 | 2026-10-17 20:42:08 | `055eb047a2d0` |
| 232 | `.tmp/kdm413_rm_freeze_2026_10_17.json` | 5,944 | 2026-10-17 20:42:08 | `a884b2cc02bd` |
| 233 | `.tmp/dw78_probe1.py` | 3,654 | 2026-10-17 20:42:28 | `627b3c9f1df4` |
| 234 | `.tmp/kdm413_rm_collect_2026_10_17.py` | 17,518 | 2026-10-17 20:42:40 | `5de96682284a` |
| 235 | `.tmp/dw78_probe1.out.txt` | 2,360 | 2026-10-17 20:42:42 | `0318d077763b` |
| 236 | `.tmp/dw77_write2.py` | 51,765 | 2026-10-17 20:43:36 | `0efd4cf284e5` |
| 237 | `.tmp/dw77_verify.py` | 4,621 | 2026-10-17 20:44:00 | `eef1343080f1` |
| 238 | `.tmp/dw77_verify.out.txt` | 4,783 | 2026-10-17 20:44:11 | `2952a41c9c5f` |
| 239 | `.tmp/u720_verify.py` | 2,038 | 2026-10-17 20:44:15 | `e05fd04ab2da` |
| 240 | `.tmp/u720_write.py` | 40,915 | 2026-10-17 20:45:03 | `9d2fd29d275d` |
| 241 | `.tmp/u720_errata.py` | 4,360 | 2026-10-17 20:45:26 | `5ee4b22c9bdf` |
| 242 | `.tmp/dw78_write1.py` | 58,317 | 2026-10-17 20:46:19 | `119c329d8f1a` |
| 243 | `.tmp/kdm413_rm_verify_2026_10_17.py` | 3,361 | 2026-10-17 20:46:31 | `1e2822415675` |
| 244 | `.tmp/__pycache__/kdm413_rm_analyze_2026_10_17.cpython-314.pyc` | 38,485 | 2026-10-17 20:46:46 | `4ddbd6ab89e7` |
| 245 | `.tmp/__pycache__/kdm413_rm_collect_2026_10_17.cpython-314.pyc` | 26,778 | 2026-10-17 20:46:46 | `aa2e0beac0ef` |
| 246 | `.tmp/__pycache__/kdm413_rm_freeze_2026_10_17.cpython-314.pyc` | 15,653 | 2026-10-17 20:46:46 | `e4b1ec3de237` |
| 247 | `.tmp/__pycache__/kdm413_rm_preflight_2026_10_17.cpython-314.pyc` | 13,515 | 2026-10-17 20:46:46 | `04a796b10c0a` |
| 248 | `.tmp/__pycache__/kdm413_rm_verify_2026_10_17.cpython-314.pyc` | 7,353 | 2026-10-17 20:46:46 | `72289e06bf62` |
| 249 | `.tmp/__pycache__/kdm413_rm_write_doc_2026_10_17.cpython-314.pyc` | 49,347 | 2026-10-17 20:46:46 | `a4d2003024b7` |
| 250 | `.tmp/kdm413_rm_collect_2026_10_17.out.txt` | 1,272 | 2026-10-17 20:47:03 | `cfdf83cc890e` |
| 251 | `.tmp/dw78_fix1.py` | 1,014 | 2026-10-17 20:49:15 | `e15656cde162` |
| 252 | `.tmp/dw78_fix1.out.txt` | 448 | 2026-10-17 20:49:22 | `4c81fb2d558d` |
| 253 | `.tmp/dw78_write2.py` | 42,033 | 2026-10-17 20:49:22 | `fdf660fefbe7` |
| 254 | `.tmp/dw78_verify.py` | 4,466 | 2026-10-17 20:49:43 | `fe803a37154a` |
| 255 | `.tmp/dw78_verify.out.txt` | 2,810 | 2026-10-17 20:49:53 | `e64fbb74c8f8` |
| 256 | `.tmp/kdm413_rm_chain_2026_10_17.ps1` | 1,762 | 2026-10-17 20:50:06 | `13366e678e63` |
| 257 | `.tmp/dw78_append9.py` | 3,891 | 2026-10-17 20:51:02 | `e1e56d7077c4` |
| 258 | `.tmp/dw78_verify2.out.txt` | 205 | 2026-10-17 20:51:12 | `e0565d8a8908` |
| 259 | `.tmp/pk_afrules_body.md` | 39,994 | 2026-10-17 20:54:28 | `525ae85c1bbc` |
| 260 | `.tmp/pk_afrules_write.py` | 2,196 | 2026-10-17 20:54:44 | `01d8dcba5d49` |
| 261 | `.tmp/pk_afrules_verify.py` | 1,727 | 2026-10-17 20:55:07 | `614990249944` |
| 262 | `.tmp/d79_probe1.py` | 4,677 | 2026-10-17 21:04:26 | `43d3d288243e` |
| 263 | `.tmp/d79_probe1.out.txt` | 1,634 | 2026-10-17 21:04:37 | `1729e0288f7c` |
| 264 | `.tmp/d79_body1.md` | 38,119 | 2026-10-17 21:06:12 | `283a697a7704` |
| 265 | `.tmp/_s3_probe_out.txt` | 1,358 | 2026-10-17 21:07:28 | `9071c5ea6c2f` |
| 266 | `.tmp/d79_body2.md` | 38,313 | 2026-10-17 21:07:43 | `e09cea31cd27` |
| 267 | `.tmp/d79_write.py` | 3,087 | 2026-10-17 21:07:51 | `d9aa14af1712` |
| 268 | `.tmp/d79_write.out.txt` | 981 | 2026-10-17 21:07:57 | `dd0945bb002e` |
| 269 | `.tmp/d79_verify.py` | 2,518 | 2026-10-17 21:08:09 | `89fd4a78115e` |
| 270 | `.tmp/_s3_faces.txt` | 72 | 2026-10-17 21:08:16 | `a99b4dea153d` |
| 271 | `.tmp/_s3_probe2.txt` | 956 | 2026-10-17 21:08:16 | `623d848bab37` |
| 272 | `.tmp/d79_errata.py` | 7,268 | 2026-10-17 21:08:51 | `2902df4038a6` |
| 273 | `.tmp/d79_errata.out.txt` | 448 | 2026-10-17 21:09:02 | `3150f9d42792` |
| 274 | `.tmp/d79_verify.out.txt` | 1,465 | 2026-10-17 21:09:18 | `27b7cd9da1d2` |
| 275 | `.tmp/_s3_paths.txt` | 1,809 | 2026-10-17 21:09:46 | `1e60e98469fd` |
| 276 | `.tmp/_s3_probe3.txt` | 88 | 2026-10-17 21:09:46 | `865f7971b4c2` |
| 277 | `.tmp/d80_probe1.py` | 4,352 | 2026-10-17 21:24:36 | `c9a5a66c38bc` |
| 278 | `.tmp/d80_probe1.out.txt` | 4,403 | 2026-10-17 21:24:49 | `4486304a2bfa` |
| 279 | `.tmp/d80_probe2.py` | 1,694 | 2026-10-17 21:25:37 | `dc813551824f` |
| 280 | `.tmp/d80_probe2.out.txt` | 253 | 2026-10-17 21:25:44 | `e78bd94a67d7` |
| 281 | `.tmp/d80_probe3.py` | 2,027 | 2026-10-17 21:26:03 | `32bc82072e7a` |
| 282 | `.tmp/d80_probe3.out.txt` | 15,919 | 2026-10-17 21:26:12 | `bcd6b283cad8` |
| 283 | `.tmp/kdm413_rm_collect_run2.out.txt` | 1,982 | 2026-10-17 21:26:13 | `96c5cea2b7eb` |
| 284 | `.tmp/kdm413_rm_llm_calls_2026_10_17.jsonl` | 613,571 | 2026-10-17 21:26:13 | `7f4cf2cd5f42` |
| 285 | `.tmp/kdm413_rm_readings_2026_10_17.json` | 958,870 | 2026-10-17 21:26:13 | `e97160e999ed` |
| 286 | `.tmp/kdm413_rm_post_2026_10_17.out.txt` | 142 | 2026-10-17 21:26:16 | `757c78a09738` |
| 287 | `.tmp/d80_probe4.py` | 4,341 | 2026-10-17 21:26:59 | `0a92abc8a157` |
| 288 | `.tmp/d80_probe4.out.txt` | 24,376 | 2026-10-17 21:27:11 | `ada6adbff256` |
| 289 | `.tmp/kdm413_rm_analyze_2026_10_17.py` | 30,209 | 2026-10-17 21:28:10 | `67861aa767e9` |
| 290 | `.tmp/kdm413_rm_analysis_2026_10_17.json` | 100,764 | 2026-10-17 21:28:17 | `cf971276fb6b` |
| 291 | `.tmp/d80_probe5.py` | 2,043 | 2026-10-17 21:28:28 | `f0e418379708` |
| 292 | `.tmp/d80_probe5.out.txt` | 7,094 | 2026-10-17 21:28:40 | `d5fd34016b88` |
| 293 | `.tmp/d80_probe6.py` | 3,429 | 2026-10-17 21:29:27 | `e6eec454bfa6` |
| 294 | `.tmp/d80_probe6.out.txt` | 3,279 | 2026-10-17 21:29:40 | `7e666918ad07` |
| 295 | `.tmp/d80_probe7.py` | 2,347 | 2026-10-17 21:30:16 | `26728c05a689` |
| 296 | `.tmp/d80_probe7.out.txt` | 2,073 | 2026-10-17 21:30:27 | `51daafcaf88a` |
| 297 | `.tmp/kdm413_rm_write_doc_2026_10_17.py` | 37,961 | 2026-10-17 21:31:07 | `7043404017ae` |
| 298 | `.tmp/kdm413_rm_verify_2026_10_17.out.txt` | 1,853 | 2026-10-17 21:31:30 | `ebf0d9a78cbc` |
| 299 | `.tmp/d80_body1.md` | 33,430 | 2026-10-17 21:33:33 | `7919da0473d9` |
| 300 | `.tmp/kd_flip_verify.out.txt` | 1,667 | 2026-10-17 21:38:59 | `6ce95e7fbc25` |
| 301 | `.tmp/d80_body2.md` | 37,073 | 2026-10-17 21:39:30 | `9bd2c6df2834` |
| 302 | `.tmp/d80_write.py` | 5,163 | 2026-10-17 21:39:54 | `6c2bc5984da5` |
| 303 | `.tmp/d80_verify.py` | 3,047 | 2026-10-17 21:40:46 | `d8fde3291246` |
| 304 | `.tmp/d80_verify.out.txt` | 1,621 | 2026-10-17 21:40:56 | `6efa85285a43` |
| 305 | `.tmp/klm413_reverdict_payload.md` | 61,667 | 2026-10-17 21:44:26 | `63625672139a` |
| 306 | `.tmp/d81_probe0.py` | 1,032 | 2026-10-17 21:50:08 | `d1dddafb9696` |
| 307 | `.tmp/d81_probe1.py` | 2,458 | 2026-10-17 21:50:51 | `f611e4d4b137` |
| 308 | `.tmp/d81_probe1.out.txt` | 3,530 | 2026-10-17 21:50:53 | `43449fe03dec` |
| 309 | `.tmp/d81_probe2.py` | 3,433 | 2026-10-17 21:51:51 | `afbca81fb239` |
| 310 | `.tmp/d81_probe2.out.txt` | 5,538 | 2026-10-17 21:51:56 | `1e97cc3cadb2` |
| 311 | `.tmp/o81_ndistinct_probe.py` | 6,984 | 2026-10-17 21:51:57 | `d5e9dcf545ae` |
| 312 | `.tmp/o81_ndistinct_probe.out.txt` | 3,794 | 2026-10-17 21:52:05 | `60b911e30775` |
| 313 | `.tmp/d81_probe3.py` | 2,556 | 2026-10-17 21:52:18 | `e497040f0890` |
| 314 | `.tmp/d81_probe3.out.txt` | 1,124 | 2026-10-17 21:52:30 | `2b156bda3661` |
| 315 | `.tmp/d81_probe4.py` | 483 | 2026-10-17 21:53:05 | `dc7de42be926` |
| 316 | `.tmp/o81_ndproof_write.py` | 26,006 | 2026-10-17 21:53:45 | `be3dba7376c5` |
| 317 | `.tmp/d81_body1.md` | 44,858 | 2026-10-17 21:56:04 | `1d65a4b9411a` |
| 318 | `.tmp/d81_body2.md` | 37,061 | 2026-10-17 21:57:53 | `c17a5af0d0bd` |
| 319 | `.tmp/d81_write.py` | 3,489 | 2026-10-17 21:58:05 | `0750ff5e4618` |
| 320 | `.tmp/d81_verify2.py` | 4,032 | 2026-10-17 21:58:28 | `e90d0bc3fc88` |
| 321 | `.tmp/d81_verify_console.txt` | 354 | 2026-10-17 21:58:35 | `c09c6aa95525` |
| 322 | `.tmp/d81_verify_readback_utf8.txt` | 3,426 | 2026-10-17 21:58:35 | `ebe50d99fa78` |
| 323 | `.tmp/d81_errata.py` | 6,851 | 2026-10-17 21:59:19 | `f28aa23fc2a5` |
| 324 | `.tmp/d81_errata_console.txt` | 642 | 2026-10-17 21:59:26 | `10de0cf0c48d` |
| 325 | `.tmp/d81_verify.out.txt` | 4,538 | 2026-10-17 21:59:26 | `afd531777546` |
| 326 | `.tmp/d81_errata2.py` | 4,486 | 2026-10-17 22:00:35 | `954f3e7e6d2c` |
| 327 | `.tmp/d81_errata2_console.txt` | 1,514 | 2026-10-17 22:00:42 | `eb813eec0a3a` |
| 328 | `.tmp/d81_errata3.py` | 6,257 | 2026-10-17 22:01:09 | `3efa38c8d5f0` |
| 329 | `.tmp/d81_verify_final.out.txt` | 1,046 | 2026-10-17 22:01:16 | `20b6b0fe4238` |
| 330 | `.tmp/af1_write.py` | 43,912 | 2026-10-17 22:01:21 | `f73224fcc6f3` |
| 331 | `.tmp/d82_probe1.py` | 3,900 | 2026-10-17 22:08:15 | `8537496a6d35` |
| 332 | `.tmp/d82_probe1.out.txt` | 3,637 | 2026-10-17 22:08:26 | `309ed874b91a` |
| 333 | `.tmp/d82_probe2.py` | 3,776 | 2026-10-17 22:08:38 | `86c7c54ad6c9` |
| 334 | `.tmp/d82_probe2.out.txt` | 1,824 | 2026-10-17 22:08:50 | `d881f2bdecbb` |
| 335 | `.tmp/d82_probe3.py` | 1,855 | 2026-10-17 22:09:34 | `482213c42994` |
| 336 | `.tmp/d82_probe3.out.txt` | 969 | 2026-10-17 22:09:41 | `228f413de0a4` |
| 337 | `.tmp/d82_body1.md` | 44,006 | 2026-10-17 22:11:09 | `90ce55bf3926` |
| 338 | `.tmp/rpp_perseed_recalc_probe_2026_10_17.py` | 8,857 | 2026-10-17 22:12:11 | `3ad523e85535` |
| 339 | `.tmp/rpp_perseed_recalc_probe_out_2026_10_17.txt` | 5,706 | 2026-10-17 22:12:26 | `e0aa42ed95ab` |
| 340 | `.tmp/d82_body2.md` | 40,356 | 2026-10-17 22:12:27 | `e8c74076fde5` |
| 341 | `.tmp/d82_write.py` | 3,764 | 2026-10-17 22:12:39 | `1c5ffcb8bf3f` |
| 342 | `.tmp/d82_verify.out.txt` | 2,002 | 2026-10-17 22:12:47 | `579fc550f43a` |
| 343 | `.tmp/d82_probe4.py` | 1,172 | 2026-10-17 22:12:56 | `f8e57adb5dd8` |
| 344 | `.tmp/d82_probe4.out.txt` | 2,673 | 2026-10-17 22:13:06 | `f7784480363d` |
| 345 | `.tmp/d83_n7r_stage.md` | 35,057 | 2026-10-17 22:13:10 | `7a2133c810b1` |
| 346 | `.tmp/d83_n7r_write.py` | 729 | 2026-10-17 22:13:14 | `dd9f2f339180` |
| 347 | `.tmp/d82_probe5.py` | 1,468 | 2026-10-17 22:13:23 | `03e39c624034` |
| 348 | `.tmp/d83_n7r_verify.py` | 1,998 | 2026-10-17 22:13:27 | `850343c11b1e` |
| 349 | `.tmp/d82_probe5.out.txt` | 840 | 2026-10-17 22:13:33 | `59215ac282e3` |
| 350 | `.tmp/d83_n7r_verify.out.txt` | 1,257 | 2026-10-17 22:13:36 | `b968a2beb941` |
| 351 | `.tmp/d82_probe6.py` | 1,222 | 2026-10-17 22:14:14 | `b1b36288ce49` |
| 352 | `.tmp/d82_probe6.out.txt` | 570 | 2026-10-17 22:14:22 | `a2cf58b8c90d` |
| 353 | `.tmp/d82_append.py` | 7,927 | 2026-10-17 22:14:50 | `9763517baf55` |
| 354 | `.tmp/d82_verify2.out.txt` | 2,093 | 2026-10-17 22:14:59 | `b16c168b7cae` |
| 355 | `.tmp/d82_probe7.out.txt` | 432 | 2026-10-17 22:15:10 | `4071dff45d63` |
| 356 | `.tmp/rpp_perseed_recalc_probe2_2026_10_17.py` | 7,794 | 2026-10-17 22:15:14 | `f89e484df372` |
| 357 | `.tmp/d82_probe8.out.txt` | 571 | 2026-10-17 22:15:19 | `b14995d285a8` |
| 358 | `.tmp/rpp_perseed_recalc_probe2_out_2026_10_17.txt` | 3,224 | 2026-10-17 22:15:22 | `c8cdcedc427b` |
| 359 | `.tmp/d82_probe9.py` | 1,475 | 2026-10-17 22:15:31 | `d3767bc9927c` |
| 360 | `.tmp/d82_probe9.out.txt` | 484 | 2026-10-17 22:15:40 | `c9240ede5a26` |
| 361 | `.tmp/d82_append2.py` | 6,901 | 2026-10-17 22:15:57 | `7a1b66cb76a6` |
| 362 | `.tmp/d82_verify3.out.txt` | 1,312 | 2026-10-17 22:16:05 | `357991a4cf3f` |
| 363 | `.tmp/ndv_stage.md` | 41,028 | 2026-10-17 22:16:30 | `0abaee4aeefb` |
| 364 | `.tmp/ndv_write.py` | 1,303 | 2026-10-17 22:16:35 | `bb41a46309ba` |
| 365 | `.tmp/ndv_verify.out.txt` | 204 | 2026-10-17 22:16:42 | `8639d96ebab1` |
| 366 | `.tmp/_rpp_deliverable_staged_2026_10_17.md` | 30,617 | 2026-10-17 22:19:34 | `7e693b27c1f7` |
| 367 | `.tmp/d83_probe1.py` | 3,623 | 2026-10-17 22:25:54 | `ac46a52ad100` |
| 368 | `.tmp/d83_probe1.out.txt` | 5,736 | 2026-10-17 22:26:01 | `b3c0cce199c3` |
| 369 | `.tmp/d83_probe2.py` | 4,946 | 2026-10-17 22:26:25 | `99fb523577b1` |
| 370 | `.tmp/d83_probe2.out.txt` | 7,806 | 2026-10-17 22:26:37 | `b8fdf1aff2bd` |
| 371 | `.tmp/af25_probe_a_faceC.py` | 1,651 | 2026-10-17 22:27:29 | `c940c09aa738` |
| 372 | `.tmp/af25_probe_a_out.txt` | 26,671 | 2026-10-17 22:27:35 | `e215b6329312` |
| 373 | `.tmp/d83_probe3.py` | 2,371 | 2026-10-17 22:27:43 | `7647d1b8cd64` |
| 374 | `.tmp/d83_probe3.out.txt` | 3,708 | 2026-10-17 22:27:51 | `2bca0aed0868` |
| 375 | `.tmp/af25_probe_a2_faceC.py` | 3,256 | 2026-10-17 22:28:04 | `dff12350bc1e` |
| 376 | `.tmp/af25_probe_a2_out.txt` | 8,336 | 2026-10-17 22:28:08 | `29da375fa3f5` |
| 377 | `.tmp/af25_probe_b_facebeta.py` | 3,665 | 2026-10-17 22:28:42 | `09a2765c4a80` |
| 378 | `.tmp/af25_probe_b_out.txt` | 1,653 | 2026-10-17 22:28:47 | `871304ed72e8` |
| 379 | `.tmp/af25_probe_b2_facebeta.py` | 4,012 | 2026-10-17 22:28:59 | `fa728068bd6b` |
| 380 | `.tmp/af25_probe_b2_out.txt` | 25,781 | 2026-10-17 22:29:03 | `0baba808d1b9` |
| 381 | `.tmp/af25_probe_c_full.py` | 6,472 | 2026-10-17 22:29:46 | `241a7353cfa0` |
| 382 | `.tmp/af25_probe_c_out.txt` | 8,161 | 2026-10-17 22:29:52 | `ded64ecdf8a8` |
| 383 | `.tmp/d83_body1.md` | 49,996 | 2026-10-17 22:30:12 | `e2a67aa39bdd` |
| 384 | `.tmp/d83_probe4.py` | 2,410 | 2026-10-17 22:30:31 | `c15116a74765` |
| 385 | `.tmp/d83_probe4.out.txt` | 4,686 | 2026-10-17 22:30:37 | `b2cc6d88e3fc` |
| 386 | `.tmp/d83_body2.md` | 41,779 | 2026-10-17 22:32:02 | `faee80c8b051` |
| 387 | `.tmp/d83_write.py` | 5,535 | 2026-10-17 22:32:18 | `180d6eafd4ba` |
| 388 | `.tmp/d83_verify.out.txt` | 7,386 | 2026-10-17 22:32:23 | `d53b4e97cc8a` |
| 389 | `.tmp/d83_probe5.py` | 1,578 | 2026-10-17 22:32:32 | `4bbdeefec2f5` |
| 390 | `.tmp/d83_probe5.out.txt` | 2,124 | 2026-10-17 22:32:37 | `cac81507a2f8` |
| 391 | `.tmp/af25_stage.md` | 48,208 | 2026-10-17 22:33:15 | `b3c45b4e2ec0` |
| 392 | `.tmp/af25_write.py` | 564 | 2026-10-17 22:33:19 | `16367c426966` |
| 393 | `.tmp/af25_verify.py` | 1,039 | 2026-10-17 22:33:23 | `717ba31e9dde` |
| 394 | `.tmp/af25_verify.out.txt` | 348 | 2026-10-17 22:33:29 | `1ec19034e29b` |
| 395 | `.tmp/d84_probe1.py` | 1,093 | 2026-10-17 22:39:24 | `1ca7c17c1dfd` |
| 396 | `.tmp/d84_probe2.py` | 1,736 | 2026-10-17 22:39:53 | `d9e9b456a61e` |
| 397 | `.tmp/d84_probe2.out.txt` | 5,550 | 2026-10-17 22:39:54 | `788a3be52720` |
| 398 | `.tmp/d84_probe3.py` | 3,545 | 2026-10-17 22:41:01 | `0a84340e62e1` |
| 399 | `.tmp/d84_probe3.out.txt` | 2,352 | 2026-10-17 22:41:07 | `34ab920c00ca` |
| 400 | `.tmp/psr_probe0.py` | 494 | 2026-10-17 22:42:27 | `24d04a775520` |
| 401 | `.tmp/d84_body1.md` | 42,968 | 2026-10-17 22:43:54 | `c565669aadeb` |
| 402 | `.tmp/d84_body2.md` | 40,560 | 2026-10-17 22:45:39 | `955222063aa0` |
| 403 | `.tmp/d84_write.py` | 3,878 | 2026-10-17 22:46:00 | `29725492eea8` |
| 404 | `.tmp/psr_probe_faceC.py` | 8,460 | 2026-10-17 22:46:01 | `62861c3c215d` |
| 405 | `.tmp/psr_probe_faceC_out.txt` | 10,012 | 2026-10-17 22:46:11 | `0396142b93cf` |
| 406 | `.tmp/freeze_preexp_exec_probe_2026_10_17.py` | 13,829 | 2026-10-17 22:46:23 | `388c731a0f61` |
| 407 | `.tmp/freeze_preexp_exec_probe_out_2026_10_17.md` | 8,593 | 2026-10-17 22:46:32 | `d146fc62162f` |
| 408 | `.tmp/d84_probe4.out.txt` | 202 | 2026-10-17 22:46:35 | `0485e04f9d00` |
| 409 | `.tmp/d84_probe4.py` | 593 | 2026-10-17 22:46:35 | `4171f2db822a` |
| 410 | `.tmp/d84_probe5.out.txt` | 738 | 2026-10-17 22:46:50 | `9bcdbe126c0f` |
| 411 | `.tmp/d84_probe5.py` | 650 | 2026-10-17 22:46:50 | `c789138c9dd7` |
| 412 | `.tmp/psr_probe_beta0.py` | 880 | 2026-10-17 22:46:52 | `8a12501b53aa` |
| 413 | `.tmp/psr_probe_beta0_out.txt` | 1,948 | 2026-10-17 22:46:59 | `d27ac29d6f9a` |
| 414 | `.tmp/d84_probe6.py` | 2,868 | 2026-10-17 22:47:07 | `d0aef4e644af` |
| 415 | `.tmp/freeze_preexp_exec_probe2_2026_10_17.py` | 8,979 | 2026-10-17 22:47:07 | `ccbab1572ae1` |
| 416 | `.tmp/d84_probe7.py` | 998 | 2026-10-17 22:47:21 | `5fc6bde34580` |
| 417 | `.tmp/d84_verify.out.txt` | 5,562 | 2026-10-17 22:47:21 | `eb58d1c1e572` |
| 418 | `.tmp/freeze_preexp_exec_probe2_out_2026_10_17.md` | 5,158 | 2026-10-17 22:47:43 | `58fe8e2fb473` |
| 419 | `.tmp/freeze_preexp_exec_write_2026_10_17.py` | 36,066 | 2026-10-17 22:49:53 | `8409f2f74798` |
| 420 | `.tmp/psr_probe_facebeta.py` | 11,087 | 2026-10-17 22:50:13 | `37ce6750bbbe` |
| 421 | `.tmp/psr_probe_facebeta_out.txt` | 7,179 | 2026-10-17 22:50:25 | `ef2106a43a79` |
| 422 | `.tmp/freeze_preexp_exec_fix_2026_10_17.py` | 1,930 | 2026-10-17 22:50:52 | `ba4a85d3e8d4` |
| 423 | `.tmp/psr_probe_faceC_seqB.py` | 2,306 | 2026-10-17 22:51:28 | `6565297a3dfe` |
| 424 | `.tmp/psr_probe_faceC_seqB_out.txt` | 2,104 | 2026-10-17 22:51:36 | `0de6ceade34b` |
| 425 | `.tmp/_b11_probe.txt` | 889 | 2026-10-17 22:55:00 | `c771f4ced820` |
| 426 | `.tmp/_b11_extract.txt` | 6,654 | 2026-10-17 22:55:42 | `71d70be96c9c` |
| 427 | `.tmp/psr_stage.md` | 42,707 | 2026-10-17 22:56:01 | `cfcf430f306c` |
| 428 | `.tmp/psr_write.py` | 738 | 2026-10-17 22:56:07 | `ffb5045608ce` |
| 429 | `.tmp/psr_verify.py` | 2,290 | 2026-10-17 22:56:34 | `1b34212bbda4` |
| 430 | `.tmp/psr_verify.out.txt` | 1,984 | 2026-10-17 22:56:42 | `44187fa25685` |
| 431 | `.tmp/_b11_hit_messages.jsonl.txt` | 1,903 | 2026-10-17 22:57:55 | `83d0741f85ca` |
| 432 | `.tmp/_b11_hit_g000000000086--ctx_12888aab-113d-47d8-9c0b-1d2b0733ab2e.jsonl.txt` | 1,903 | 2026-10-17 22:58:03 | `83d0741f85ca` |
| 433 | `.tmp/_b11_hit_g000000000087--ctx_182027ab-822e-4907-977e-40e6dac53569.jsonl.txt` | 1,901 | 2026-10-17 22:58:03 | `505eca298c39` |
| 434 | `.tmp/d85_probe1.py` | 3,020 | 2026-10-17 23:03:42 | `7ebe64d0eff9` |
| 435 | `.tmp/d85_p1_def.txt` | 0 | 2026-10-17 23:04:03 | `e3b0c44298fc` |
| 436 | `.tmp/d85_p1_resp.txt` | 0 | 2026-10-17 23:04:03 | `e3b0c44298fc` |
| 437 | `.tmp/d85_p1_scan.txt` | 57 | 2026-10-17 23:04:03 | `3fa1793856fb` |
| 438 | `.tmp/d85_p1_task.txt` | 0 | 2026-10-17 23:04:03 | `e3b0c44298fc` |
| 439 | `.tmp/d86_probe1.py` | 887 | 2026-10-17 23:04:06 | `687a88b98c32` |
| 440 | `.tmp/d85_probe2.py` | 1,355 | 2026-10-17 23:04:08 | `ee5ff4bf1217` |
| 441 | `.tmp/d86_probe1.out.txt` | 940 | 2026-10-17 23:04:09 | `1d91053b90d0` |
| 442 | `.tmp/d85_p1_raw.txt` | 15,655 | 2026-10-17 23:04:28 | `b3ad8f314965` |
| 443 | `.tmp/d86_probe2.py` | 439 | 2026-10-17 23:04:37 | `42858c42bad2` |
| 444 | `.tmp/d85_probe3.py` | 2,484 | 2026-10-17 23:04:51 | `9ff7b9930550` |
| 445 | `.tmp/d85_def.txt` | 0 | 2026-10-17 23:05:00 | `e3b0c44298fc` |
| 446 | `.tmp/d85_resp.txt` | 27,816 | 2026-10-17 23:05:00 | `cb42f72162bf` |
| 447 | `.tmp/d85_task.txt` | 2,677 | 2026-10-17 23:05:00 | `d23292c61928` |
| 448 | `.tmp/d86_probe3.py` | 620 | 2026-10-17 23:05:01 | `107975c87711` |
| 449 | `.tmp/d85_probe4.py` | 2,254 | 2026-10-17 23:05:16 | `a68a9e4d0878` |
| 450 | `.tmp/d85_carddef.txt` | 4,602 | 2026-10-17 23:05:23 | `d83bd231882a` |
| 451 | `.tmp/d86_probe4.py` | 2,234 | 2026-10-17 23:05:35 | `3595aecb1033` |
| 452 | `.tmp/d85_probe5.py` | 3,587 | 2026-10-17 23:05:43 | `c3b40ac9f977` |
| 453 | `.tmp/d86_probe5.py` | 1,358 | 2026-10-17 23:05:44 | `215c0504d46b` |
| 454 | `.tmp/merge_gov_write.py` | 26,827 | 2026-10-17 23:05:51 | `7ad32ca275a1` |
| 455 | `.tmp/d85_p5.out.txt` | 2,562 | 2026-10-17 23:05:54 | `fc3584a325be` |
| 456 | `.tmp/d85_probe6.py` | 2,055 | 2026-10-17 23:06:05 | `60968546ce49` |
| 457 | `.tmp/d85_receipt.txt` | 0 | 2026-10-17 23:06:13 | `e3b0c44298fc` |
| 458 | `.tmp/d85_loc.txt` | 1,545 | 2026-10-17 23:06:16 | `458ded1a9b0d` |
| 459 | `.tmp/d85_probe7.py` | 1,661 | 2026-10-17 23:06:26 | `9e452147d408` |
| 460 | `.tmp/d85_fp2.txt` | 617 | 2026-10-17 23:06:32 | `feb0a03f50ff` |
| 461 | `.tmp/d85_receipt_raw.txt` | 6,622 | 2026-10-17 23:06:32 | `9f4e5977991b` |
| 462 | `.tmp/d85_probe8.py` | 5,860 | 2026-10-17 23:07:08 | `2f90bdfe9e91` |
| 463 | `.tmp/d86_write1.py` | 36,576 | 2026-10-17 23:07:15 | `93c4fbc17cd3` |
| 464 | `.tmp/d85_p8.out.txt` | 1,800 | 2026-10-17 23:07:32 | `2db3a3f7d5ec` |
| 465 | `.tmp/d85_probe9.py` | 1,716 | 2026-10-17 23:07:53 | `c2151ef13c42` |
| 466 | `.tmp/d85_p9.out.txt` | 1,437 | 2026-10-17 23:08:05 | `888446bbf546` |
| 467 | `.tmp/d85_fp3.txt` | 461 | 2026-10-17 23:08:43 | `6f91932e7b96` |
| 468 | `.tmp/d86_write2.py` | 46,018 | 2026-10-17 23:09:03 | `d4992eac401d` |
| 469 | `.tmp/d86_verify.py` | 4,033 | 2026-10-17 23:09:23 | `17d12b4e58cf` |
| 470 | `.tmp/d85_body1.md` | 49,626 | 2026-10-17 23:10:23 | `80229d6489d1` |
| 471 | `.tmp/d86_errata.py` | 11,348 | 2026-10-17 23:10:43 | `73273d1a682d` |
| 472 | `.tmp/d86_verify.out.txt` | 2,341 | 2026-10-17 23:11:08 | `0fb8fb628de0` |
| 473 | `.tmp/d86_verify_print.txt` | 2,341 | 2026-10-17 23:11:08 | `0fb8fb628de0` |
| 474 | `.tmp/d85_body2.md` | 26,187 | 2026-10-17 23:11:26 | `d08e5b7198b0` |
| 475 | `.tmp/d85_write.py` | 1,329 | 2026-10-17 23:11:31 | `72777f36ee87` |
| 476 | `.tmp/d85_write.out.txt` | 405 | 2026-10-17 23:11:39 | `abf861df8b1f` |
| 477 | `.tmp/d86_errata3.py` | 5,832 | 2026-10-17 23:11:40 | `4d66a25c1ab8` |
| 478 | `.tmp/d85_verify.py` | 2,525 | 2026-10-17 23:11:46 | `541e097fd55c` |
| 479 | `.tmp/d86_final.py` | 1,766 | 2026-10-17 23:11:51 | `e2fddad09200` |
| 480 | `.tmp/d85_append.py` | 4,607 | 2026-10-17 23:12:19 | `a23b1d3d5394` |
| 481 | `.tmp/d85_append.out.txt` | 382 | 2026-10-17 23:12:28 | `234a0bce60e9` |
| 482 | `.tmp/d85_verify.out.txt` | 1,710 | 2026-10-17 23:12:42 | `50b4c76a9d71` |
| 483 | `.tmp/d87_probe1.py` | 4,968 | 2026-10-17 23:23:40 | `b18f260dd083` |
| 484 | `.tmp/d87_probe1.out.txt` | 2,897 | 2026-10-17 23:24:00 | `3e71ed35f65b` |
| 485 | `.tmp/d87_probe2.py` | 3,753 | 2026-10-17 23:24:33 | `dd13833989e7` |
| 486 | `.tmp/d87_probe2.out.txt` | 6,002 | 2026-10-17 23:24:40 | `e2709188e23e` |
| 487 | `.tmp/exp_harness_pre_2026_10_17.py` | 41,428 | 2026-10-17 23:26:06 | `026575ff3829` |
| 488 | `.tmp/d87_probe3.py` | 1,998 | 2026-10-17 23:26:13 | `73aa66b90d34` |
| 489 | `.tmp/d87_probe3.out.txt` | 384 | 2026-10-17 23:26:28 | `31d53b401e3a` |
| 490 | `.tmp/freeze_criterion_rewire_design_write_2026_10_17.py` | 42,900 | 2026-10-17 23:27:46 | `2d5ff7602580` |
| 491 | `.tmp/harness_mask_freeze_write_2026_10_17.py` | 7,873 | 2026-10-17 23:28:09 | `079a280da225` |
| 492 | `.tmp/harness_mask_kill_freeze_2026_10_17.json` | 6,673 | 2026-10-17 23:28:19 | `5ecfe565fa1d` |
| 493 | `.tmp/d87_write1.py` | 52,720 | 2026-10-17 23:28:20 | `df8d9c96c381` |
| 494 | `.tmp/d88_probe1.py` | 5,713 | 2026-10-17 23:29:13 | `ea8246bee209` |
| 495 | `.tmp/d88_probe1.out.txt` | 3,694 | 2026-10-17 23:29:49 | `6298a859b828` |
| 496 | `.tmp/d87_append.py` | 5,167 | 2026-10-17 23:30:47 | `f89fa212b30e` |
| 497 | `.tmp/__pycache__/exp_harness_pre_2026_10_17.cpython-314.pyc` | 40,144 | 2026-10-17 23:30:50 | `27b60f271b37` |
| 498 | `.tmp/d88_write2.py` | 41,852 | 2026-10-17 23:32:13 | `a6c6d98da4fe` |
| 499 | `.tmp/harness_mask_validation_2026_10_17.py` | 15,806 | 2026-10-17 23:32:45 | `03f7a0b5e150` |
| 500 | `.tmp/harness_mask_validation_out_2026_10_17.txt` | 7,241 | 2026-10-17 23:32:56 | `ba3413b0d5a3` |
| 501 | `.tmp/d88_write3.py` | 40,507 | 2026-10-17 23:33:31 | `6d9adcf449c9` |
| 502 | `.tmp/harness_mask_diffstat_2026_10_17.py` | 5,616 | 2026-10-17 23:34:07 | `6fe0a6d30555` |
| 503 | `.tmp/harness_mask_diffstat_out_2026_10_17.txt` | 2,337 | 2026-10-17 23:34:19 | `7db31c10646f` |
| 504 | `.tmp/d88_write4.py` | 51,411 | 2026-10-17 23:35:20 | `a1fc06af935c` |
| 505 | `.tmp/d88_verify.py` | 4,575 | 2026-10-17 23:35:32 | `635a18d72c3b` |
| 506 | `.tmp/d88_errata.py` | 5,958 | 2026-10-17 23:36:40 | `ec473bd85ff6` |
| 507 | `.tmp/d88_verify.out.txt` | 2,324 | 2026-10-17 23:36:49 | `dd29936a25a3` |
| 508 | `.tmp/d89_probe1.py` | 5,193 | 2026-10-17 23:45:51 | `4425c3b71380` |
| 509 | `.tmp/d89_probe1.out.txt` | 2,841 | 2026-10-17 23:46:04 | `3a85f181e53a` |
| 510 | `.tmp/d89_probe2.py` | 1,571 | 2026-10-17 23:46:31 | `ef9d91d8e58d` |
| 511 | `.tmp/d89_probe2.out.txt` | 1,030 | 2026-10-17 23:46:38 | `b6c333723b49` |
| 512 | `.tmp/freeze_criterion_rewire_r2_killfreeze_2026_10_17.py` | 8,049 | 2026-10-17 23:48:18 | `209587869f7a` |
| 513 | `.tmp/freeze_criterion_rewire_r2_kill_freeze_2026_10_17.json` | 11,550 | 2026-10-17 23:48:24 | `2b4dafecf4d1` |
| 514 | `.tmp/kd14_p2_write1.py` | 15,489 | 2026-10-17 23:48:44 | `a493231d9229` |
| 515 | `.tmp/kd14_p2_kill_lines_freeze_2026_10_17.md` | 12,032 | 2026-10-17 23:48:55 | `aca85ea4727c` |
| 516 | `.tmp/d89_probe3.py` | 985 | 2026-10-17 23:49:08 | `abacf473e4d5` |
| 517 | `.tmp/d89_probe3.out.txt` | 408 | 2026-10-17 23:49:16 | `577c18f43443` |
| 518 | `.tmp/d89_write1.py` | 47,836 | 2026-10-17 23:49:27 | `1149389b5c99` |
| 519 | `.tmp/freeze_criterion_rewire_r2_probe_out_2026_10_17.txt` | 15,494 | 2026-10-17 23:50:04 | `db80bdffe67a` |
| 520 | `.tmp/freeze_criterion_rewire_r2_llmcheck_2026_10_17.py` | 3,872 | 2026-10-17 23:51:34 | `ddd02b9013d0` |
| 521 | `.tmp/freeze_criterion_rewire_r2_llmcheck_out_2026_10_17.txt` | 1,623 | 2026-10-17 23:51:47 | `1cfa81eca602` |
| 522 | `.tmp/_b11_g86_L93_raw.txt` | 874 | 2026-10-17 23:51:51 | `b210d5c92bb1` |
| 523 | `.tmp/_b11_g86_L94_raw.txt` | 5,843 | 2026-10-17 23:51:51 | `196227473fab` |
| 524 | `.tmp/_b11_g86_L95_raw.txt` | 524 | 2026-10-17 23:51:51 | `522c3ee187b9` |
| 525 | `.tmp/_b11_g86_L98_raw.txt` | 11,039 | 2026-10-17 23:51:51 | `403f30fffb4c` |
| 526 | `.tmp/d89_write2.py` | 59,936 | 2026-10-17 23:51:57 | `07362bc6517b` |
| 527 | `.tmp/freeze_criterion_rewire_r2_probe_2026_10_17.py` | 22,764 | 2026-10-17 23:52:14 | `cb91e876ae7f` |
| 528 | `.tmp/freeze_criterion_rewire_r2_probe_out2_2026_10_17.txt` | 17,037 | 2026-10-17 23:52:22 | `9953747adec5` |
| 529 | `.tmp/_b11_q9_response_verbatim.txt` | 10,599 | 2026-10-17 23:52:38 | `126a2f454747` |
| 530 | `.tmp/d89_verify.py` | 5,657 | 2026-10-17 23:52:50 | `7edae96a586c` |
| 531 | `.tmp/d89_verify.out.txt` | 1,040 | 2026-10-17 23:53:02 | `7b1984940f1a` |
| 532 | `.tmp/d89_append1.py` | 7,403 | 2026-10-17 23:53:23 | `8989ad41e59a` |
| 533 | `.tmp/d89_verify2.py` | 2,421 | 2026-10-17 23:53:44 | `e0dd6709f262` |
| 534 | `.tmp/d89_verify2.out.txt` | 874 | 2026-10-17 23:53:52 | `ab13400e0adf` |
| 535 | `.tmp/freeze_criterion_rewire_r2_deliverable_write_2026_10_17.py` | 49,730 | 2026-10-17 23:55:18 | `37b72b64800c` |
| 536 | `.tmp/freeze_criterion_rewire_r2_append_2026_10_17.py` | 2,305 | 2026-10-17 23:55:37 | `91d5a0a69ba4` |
| 537 | `.tmp/kd14_p2_probe.py` | 15,574 | 2026-10-17 23:55:41 | `6f7ac21bdc3d` |
| 538 | `.tmp/distortion_calculator_pre_410a12482eef.py` | 40,611 | 2026-10-17 23:55:51 | `410a12482eef` |
| 539 | `.tmp/kd14_p2_probe_out_2026_10_17.txt` | 6,858 | 2026-10-17 23:55:51 | `b74675107848` |
| 540 | `.tmp/freeze_criterion_rewire_r2_corr_2026_10_17.py` | 3,182 | 2026-10-17 23:56:20 | `d7e1c199ee85` |
| 541 | `.tmp/_b11_q9_card_definition.txt` | 5,364 | 2026-10-17 23:58:21 | `1b0b8b61feb5` |
| 542 | `.tmp/kd14_p2_write2.py` | 28,296 | 2026-10-17 23:59:10 | `ff9ab107b5f5` |
| 543 | `.tmp/_b11_register_writer.py` | 9,423 | 2026-10-18 00:01:47 | `45d150c5f8ed` |
| 544 | `.tmp/_r2_tool_01_inventory.py` | 2,498 | 2026-10-18 00:17:08 | `99ee7cb1ebae` |
| 545 | `.tmp/_r2_tool_02_breakdown.py` | 2,074 | 2026-10-18 00:17:34 | `ed316d1d905e` |
| 546 | `.tmp/_r2_tool_03_refindex.py` | 4,440 | 2026-10-18 00:19:24 | `32bd762657ba` |
| 547 | `.tmp/_r2_tool_03_refindex.json` | 9,700,261 | 2026-10-18 00:20:08 | `aa05d398bb1d` |
| 548 | `.tmp/_r2_tool_04_classes.py` | 4,920 | 2026-10-18 00:20:37 | `055797145699` |
| 549 | `.tmp/_r2_tool_04b_channels.py` | 4,355 | 2026-10-18 00:21:25 | `8dc5c887150d` |
| 550 | `.tmp/_r2_tool_05_dirs.py` | 2,836 | 2026-10-18 00:23:00 | `f1d5f54866f6` |
| 551 | `.tmp/_r2_tool_06_pools.py` | 4,538 | 2026-10-18 00:23:59 | `38cfc44ab456` |
| 552 | `.tmp/_r2_tool_06_pools.json` | 44,972 | 2026-10-18 00:24:14 | `a7917e01e553` |
| 553 | `.tmp/_r2_tool_07_xferpool.py` | 3,070 | 2026-10-18 00:24:48 | `968db8e49af5` |
| 554 | `.tmp/_r2_tool_08_dups.py` | 3,454 | 2026-10-18 00:25:59 | `9e2bf8865936` |
| 555 | `.tmp/_r2_tool_09_plan.py` | 6,517 | 2026-10-18 00:27:01 | `3e7f88cb9eb8` |
| 556 | `.tmp/_r2_tool_09_plan.json` | 55,738 | 2026-10-18 00:27:10 | `333492128e31` |
| 557 | `.tmp/_r2_tool_10_plan2.py` | 8,115 | 2026-10-18 00:28:19 | `1e4c0eaf09ff` |
| 558 | `.tmp/_r2_tool_11_channels.py` | 4,801 | 2026-10-18 00:30:46 | `3c8a51b1473f` |
| 559 | `.tmp/_r2_tool_12_plan3.py` | 5,757 | 2026-10-18 00:32:48 | `8ab6bb0dd570` |
| 560 | `.tmp/_r2_tool_13_check.py` | 2,424 | 2026-10-18 00:33:17 | `cd966d2cd422` |
| 561 | `.tmp/_r2_tool_14_plan4.py` | 5,689 | 2026-10-18 00:34:47 | `97c00a613313` |
| 562 | `.tmp/_r2_tool_14_plan4.json` | 51,836 | 2026-10-18 00:34:56 | `b7942c0a75f1` |
| 563 | `.tmp/_r2_tool_15_gates.py` | 4,692 | 2026-10-18 00:35:32 | `71f1b4e2b0bb` |
| 564 | `.tmp/_stage3_r2_criteria_freeze_2026_10_18.md` | 9,971 | 2026-10-18 00:36:42 | `885ec7fb04dd` |
| 565 | `.tmp/_r2_tool_16_sample.json` | 56 | 2026-10-18 00:38:50 | `66f49919660b` |
| 566 | `.tmp/_r2_tool_16_trashverify.py` | 3,466 | 2026-10-18 00:38:58 | `a47e89c1ed5c` |
| 567 | `.tmp/_r2_tool_16_sample_verify.json` | 3,167 | 2026-10-18 00:39:04 | `0132123c23c8` |
| 568 | `.tmp/_r2_tool_17_rest.json` | 8,649 | 2026-10-18 00:39:18 | `bb1d12223740` |
| 569 | `.tmp/_r2_tool_18_twins.json` | 27,063 | 2026-10-18 00:39:37 | `7467783c6d4f` |
| 570 | `.tmp/_r2_tool_19_trashverify.json` | 66,439 | 2026-10-18 00:47:59 | `5ff0887b086c` |
| 571 | `.tmp/_r2_tool_20_xfer.py` | 2,548 | 2026-10-18 00:48:12 | `2082a9a876e2` |
| 572 | `.tmp/_r2_tool_20_xfer.json` | 66,273 | 2026-10-18 00:48:19 | `2c06c1d70839` |
| 573 | `.tmp/_r2_tool_21_post.py` | 1,862 | 2026-10-18 00:48:34 | `660a666da351` |
| 574 | `.tmp/_r2_tool_22_selfclean.json` | 464 | 2026-10-18 00:50:08 | `4e4212c74d61` |
| 575 | `.tmp/_r2_tool_22_selfclean_verify.json` | 35,483 | 2026-10-18 00:50:08 | `3fc18c9d09e9` |
| 576 | `.tmp/_r2_tool_23_nolink.py` | 2,040 | 2026-10-18 00:52:28 | `12632e36d05f` |
| 577 | `.tmp/_r2_tool_23_nolink.json` | 90,951 | 2026-10-18 00:52:35 | `5accec1e55d7` |
| 578 | `.tmp/_r2_tool_24_funcref.json` | 8,346 | 2026-10-18 00:53:27 | `74101ab98d63` |
| 579 | `.tmp/_r2_tool_25_restore.py` | 4,227 | 2026-10-18 00:54:42 | `fa2ee5026d9c` |
| 580 | `.tmp/_r2_tool_25_restore.json` | 392,957 | 2026-10-18 00:55:08 | `e8cabb5339c2` |
| 581 | `.tmp/_r2_tool_26_genregister.py` | 20,579 | 2026-10-18 00:57:06 | `e013fac3d234` |
| 582 | `.tmp/_r2_tool_21_post.json` | 949 | 2026-10-18 00:58:32 | `794217ca0f3a` |

⚠ **`.tmp` 夜窗面之内容 ⛔ 0 逐件核**（本棒纯勘察，⛔ 0 内容审计）⇒ 「证据载体」系**按面归并之称谓**，⛔ 0 断言其**均为**证据载体（**KD-INV-07**）。

### §7.3 段面归并（**仅按件名之显式段标归并；无段标者 0 推断**）

| 段 | 件数 | 代表件（SHA-12） | 归并依据 |
|:--|--:|:--|:--|
| ③段（整理／清噪／拉平） | 13 | `.tmp/_s3_faces.txt`<br>`a99b4dea153d` | 件名含段别关键字（**关键词归并，非权威归段**）|
| ①②段（V3/V4 实验全量收束、Trae 走读与委托） | **0 具名段标者** | —— | **无段标者 0 推断** |

⚠ **归段限度**：上表系**关键词归并**之**工作视图**，⛔ **0 断言**任一件之**权威段别归属**（段别权属 PI 宣告范畴）。本棒⛔ 0 按**语义**（如「生效落账」「设计」「验真」）归类（A-3）。

## §8 · 漂移面（**只登记实测时点读数；⛔ 0 断言根因／已止／最终值**）

| # | 件／面 | 登记读数（出处） | 本棒实测（2026-10-18 01:05:00） | 处置 |
|:-:|:--|:--|:--|:--|
| **D-1** | **REPO 字节账** | 整理登记件 §2：整理后 **189,574,034 B**；§2 末另生成本登记件（**62,885 B**）＋生成脚本 `.tmp/_r2_tool_26_genregister.py`（**20,579 B**，`e013fac3d234`）| **189,657,496 B** = 登记 + 62,885 + 20,579 − **2 B** | 件数账 **逐件对平**（4,282 ＝ 4,280 ＋ 2）✅；**字节账差 −2 B 未平** ⇒ ⛔ **0 断言根因**、⛔ **0 校正** → **KD-INV-01** |
| **D-2** | **SUB 字节账** | 登记件 §2：60,166,418 B | **60,166,418 B** | ✅ **逐字节吻合，0 差** |
| **D-3** | **并发写入面** | 登记件 §8-2 第 1 条：清点基线非静态，他棒并发写入**可能** | mtime **晚于**登记件落盘（2026-10-18 00:58:56）之件 **0 件** | ✅ **实测 0 并发** ⇒ 本件计数面**无他棒干扰** |
| **D-4** | **`.tmp/` 件数面** | v2.0（10-12）**441** 件；本棒（10-18）**2,268** 件 | — | 两读并列（§5.2）；⛔ 0 断言增量构成 |
| **D-5** | **pi_rulings 版本序／落盘时序** | v85 mtime **23:12:28**；v86 mtime **23:10:53** | 同左（实测） | ⚠ **v86 落盘早于 v85 而版本号更大** ⇒ 版本序与时序**倒置**；⛔ 0 断言成因 → **KD-INV-02** |

## §9 · 「未核得」清单（凡未实测者一律写「未核得」＋原因）

| # | 项 | 状态 | 原因 |
|:-:|:--|:--|:--|
| **N-1** | ARCHIVE 面（`_non_upload_local_archive`）之件数／bytes／逐件指纹 | 🔴 **未核得（禁触区）** | 本棒授权明令 ⛔ 0 触 ⇒ **其件 ⛔ 0 入清单之逐件面**，全文仅载「**归档区在 · 0 触**」一句；⛔ **0 以 MAIN/SUB 之和代填**、⛔ 0 填估值 |
| **N-2** | 清走 96 件之**回收站实存性** | 🔴 **未核得** | 本棒 ⛔ **0 触回收站** ⇒ 仅核得「已离原位（两区 0 命中）」；「可恢复」沿用登记件 §3-3 之 96/96 验道**登记值**（A-4）|
| **N-3** | 残余功能断链是否确为 0 | 🔴 **未核得** | 登记件载 0；本棒为**纯勘察棒**，⛔ 0 复算活代码引用面 |
| **N-4** | `.tmp/` 夜窗面 **582** 件之**内容**属性 | 🔴 **未核得** | 纯勘察棒 ⛔ 0 内容审计（KD-INV-07）|
| **N-5** | 「生效落账／设计／验真／登记」四型之**边界判据** | 🔴 **未决** | 派工单未给词表（A-3）⇒ ⛔ 0 按语义分类 |
| **N-6** | 「B-11 回收件」之**权威指代** | 🔴 **未决** | 派工单未给文件名；两区按 `b11` 关键字**唯一命中** 1 件（`d224a7380071`）⇒ 采认并登记为消歧未决（KD-INV-03）|
| **N-7** | 读-A（2,891）→ 读-B（5,556）之 **+2,665 件**逐件归因 | 🔴 **未核得** | 其间**既有**整理动作、**亦有**他棒产出；⛔ 0 断言归因（§5.1）|

📌 **诚实交代**：①本件所有 SHA-12／bytes／mtime **均由本棒 `sha256` 逐件实测**（`os.walk` **遍历错误 0**），**0 填估值／0 推断值**；②「未核得／未决」共 **7 项**；③**禁触区 `_non_upload_local_archive` 之目录名**由派工单给定并于本件载之，**其内容 0 读 0 写 0 列目录**——如实登记；④**本件之 SHA-12／bytes 自指不可内含** ⇒ 由落盘后**独立亲测回读**报回父会话（沿 `_stage3_r2_cleanup_register_2026_10_18.md` §9 之同法）。

## §10 · ⛔ 本件 0 作之事项（边界自述）

| # | 事项 | 本件之 0 |
|:-:|:--|:-:|
| 1 | **0 宣告任何闭／开／段之毕**（含 ③段之毕 · ①毕之复核）| ✅ |
| 2 | **0 落五终判**（`pass`／`af`／`kd`／`fail`／`give-up`）——§11-KD 系**缺陷登记**非**实验终判** | ✅ |
| 3 | **0 代 PI 裁**（A-1…A-4 四项歧义均列明候裁，⛔ 0 自裁）| ✅ |
| 4 | **0 回改任何既有件一字**（v2.0 件、③段-R2 登记件、其余全盘 **全未触动**）| ✅ |
| 5 | **0 移动／删除／重命名任何文件**（本棒纯勘察 ＋ 一件新落盘）| ✅ |
| 6 | **0 触归档区** `_non_upload_local_archive`（0 读 0 写 0 列目录）| ✅ |
| 7 | **0 触 GLM 面** | ✅ |
| 8 | **0 联网** | ✅ |
| 9 | **0 读 key**（⛔ 0 读 `.env`／0 取 key）| ✅ |
| 10 | **0 触回收站** | ✅ |
| 11 | **0 以 PowerShell `-Recurse`＋`SilentlyContinue` 作遍历**（全量实测**一律** `os.walk` ＋ `onerror` 计数）| ✅ |
| 12 | **0 断言漂移根因／已止／最终值**（D-1…D-5 均只登记实测读数）| ✅ |
| 13 | **0 校正任何计数差异**（§5 多读并列即止）| ✅ |
| 14 | **0 填估值／推断值**（未核得即写未核得）| ✅ |
| 15 | **0 新建第二个仓内文件**（本件系本棒唯一仓内落盘件；全部临时脚本／中间 JSON 仅落 `%TEMP%`）| ✅ |
| 16 | **0 冒充** PI／parent／worker／verdict-keeper／verifier／protocol-keeper／evidence-auditor | ✅ |

## §11 · 新增面登记（🆕 相对 v2.0 之新增／偏离 · 逐条注明）

### §11-A 新增／偏离面（⛔ 0 改写 v2.0；新增一律置于此 append 节）

| # | 新增／偏离面 | 性质 | 权源／理由 | 落位 |
|:-:|:--|:--|:--|:--|
| **A-1** | 类别判据扩充三面：`pi_rulings/`、`_remote_pullback_2026_10_17/`、`.vscode/` | 🆕 扩充（沿 v2.0 兜底原则）| 整理后新增顶层面，不在 v2.0 枚举内 | §2.4 · §4 |
| **A-2** | `.tmp/` 面由「仅汇总」改为「逐件展开」（**2,268 件**）| ⚠ **偏离惯例** | **派工单明令「全件枚举…逐件」** | §2.2 · §4.1 |
| **A-3** | **分型分布面（md／py／json／其他）** | 🆕 **新增** | 派工单第 ② 项明列 | **本节 §11-A-3** |
| **A-4** | **整理映射面**（清走 96 · 转移 141 · 回退 25 ＋ 盘上复核）| 🆕 **新增**（取代 v2.0 §3「合订主轴」之位）| 本件主题即「整理后时点」| §3 |
| **A-5** | **今晚增量面**（换 v2.0 §7 之窗为 10-17 18:00 → 实测时点）| 🆕 换窗 | 派工单第 ③ 项 | §7 |
| **A-6** | **新出 KD 登记面**（域 `KD-INV`；落前实测两区 **0 占用**）| 🆕 **新增** | 派工单第 ⑦ 项 | **本节 §11-KD** |

### §11-A-3 分型分布（🆕 新增面 · md／py／json／其他）

| 区 | 型 | 件数 | bytes | 占区件数 |
|:--|:-:|--:|--:|--:|
| REPO | `md` | 1,131 | 36,010,588 | 26.41% |
| REPO | `py` | 1,890 | 22,849,462 | 44.14% |
| REPO | `json` | 732 | 122,697,563 | 17.09% |
| REPO | `其他` | 529 | 8,099,883 | 12.35% |
| **REPO 小计** | —— | **4,282** | **189,657,496** | 100.00% |
| SUB | `md` | 849 | 22,801,155 | 66.54% |
| SUB | `py` | 173 | 2,232,638 | 13.56% |
| SUB | `json` | 215 | 30,404,338 | 16.85% |
| SUB | `其他` | 39 | 4,728,287 | 3.06% |
| **SUB 小计** | —— | **1,276** | **60,166,418** | 100.00% |
| **两区合计** | `md` | **1,980** | **58,811,743** | —— |
| **两区合计** | `py` | **2,063** | **25,082,100** | —— |
| **两区合计** | `json` | **947** | **153,101,901** | —— |
| **两区合计** | 其他 | **568** | **12,828,170** | —— |
| **两区合计** | **全部** | **5,558** | **249,823,914** | 100.00% |

📌 **判据**：扩展名按**小写**判别，`.md`／`.py`／`.json` 三型优先，余归「其他」；**0 内容判别**（⛔ 0 判文件性质）。

### §11-KD 新出 KD 逐条登记（编号域 `KD-INV` · 落前实测两区 **0 占用**）

| # | KD | 面 | 描述 | 证据 | 本件处置 |
|:-:|:--|:--|:--|:--|:--|
| **KD-INV-01** | 字节账未平 **−2 B** | REPO | 整理登记件 §2 载整理后 **189,574,034 B**；加登记件 **62,885 B** ＋其生成脚本 **20,579 B** 应为 **189,657,498 B**，本棒实测 **189,657,496 B** | §8 **D-1**（件数账 4,282 ＝ 4,280 ＋ 2 **逐件对平** ✅）| ⛔ **0 断言根因**、⛔ **0 校正**、⛔ **0 回改登记件**；差异登记在案 |
| **KD-INV-02** | pi_rulings **版本序／落盘时序倒置** | REPO | v85 mtime **2026-10-17 23:12:28**（`c54c4580baa2`）**晚于** v86 mtime **23:10:53**（`19821507b5b2`），而 v86 版本号更大 | §8 **D-5**（两件指纹均为本棒实测）| ⛔ 0 断言成因（可能为批量写盘序、可能为他因）；⛔ 0 重命名／⛔ 0 改 mtime |
| **KD-INV-03** | 「B-11 回收件」**指代未决** | 两区 | 派工单点名该件而**未给文件名**；本棒按 `b11` 关键字两区全量检索**唯一命中** `pi_rulings/_pi_card_answers_register_2026_10_14_b11_recovery.md`（13,812 B · 2026-10-18 00:02:40 · `d224a7380071`）| §7.2 面-① · §9-N-6 | **采认并显式标注为消歧未决**，候 PI 复核；⛔ 0 径行认定 |
| **KD-INV-04** | 「今晚」窗口**切点系本棒自定** | REPO | 派工单仅给「2026-10-17 晚至 18 凌晨」之**定性**描述，**未给切点**；本件取 mtime ≥ **2026-10-17 18:00:00** | §7.1 三读并出（读-1 689 件／读-2 10-17 全日 1,380 件）| ⛔ **0 断言**其即 PI 之意；两读并列，候 PI 择 |
| **KD-INV-05** | 清走 96 件之「**可恢复**」实存性**未核** | 两区 | 本棒 ⛔ **0 触回收站** ⇒ 仅核得「已离原位（判据 89/89 ＋ 自清 7/7）」；「可恢复」沿用登记件 §3-3 之 `$I`/`$R` 验道 **96/96** **登记值** | §3.2 · §9-N-2 | 沿用登记值并**标明来源为登记而非实测**；⛔ 0 声称本棒已验 |
| **KD-INV-06** | 非 ASCII 件名之**跨工具编码面** | 两区 | 两区全量共 **24** 件名含非 ASCII 字符；其中今晚面 1 件 `results/_af_flip要件消解_rulings_effect_2026_10_17.md`（45,096 B · `dc5ee48e1f53`）。经实测：UTF-8 读写**正常**、字面**不命中**登记件 C 型畸形判据（无禁用字符 `< > : " \ | ? *`、无控制字符、非首尾点／空格、长度 < 200）⇒ **非 C 型**；然本棒实测 PowerShell 控制台回显**为乱码** | §7.2 面-② · §3.2 C 型判据（登记件 §3）| **非 C 型**（登记在案）；编码面风险登记，⛔ 0 重命名、⛔ 0 判其为缺陷件 |
| **KD-INV-07** | `.tmp/` 夜窗面 **582** 件之**内容属性未核** | REPO | 本棒为**纯勘察棒**，⛔ 0 内容审计 ⇒ 「证据载体面」系**按面归并之称谓** | §7.2 面-④ · §9-N-4 | ⛔ **0 断言**其均为证据载体；⛔ 0 判其可清（处置权属 PI）|

📌 **KD 域声明**：本节 7 条系**本棒新出之已知缺陷登记**（编号域 `KD-INV`），⛔ **0** 与既有 `KDS-*`／`KD04-*` 等域混用（落前已实测两区 `KD-INV` **0 命中**）；⛔ **0** 具五终判效力（**非实验终判**）。

---

## 输入链表（本棒实读 · 逐件 SHA-12）

| # | 件／源 | 角色 | SHA-12 | bytes |
|---:|:--|:--|:--|--:|
| 1 | `results/_achievements_inventory_full_2026_10_09.md` | **体例底本（v2.0）** · 惯例回查 | `dd3e9806a369` | 372,318 |
| 2 | `results/_stage3_r2_cleanup_register_2026_10_18.md` | **整理映射底本** · §3/§4/§6 之源 | `d6b1dc8f8a02` | 62,885 |
| 3 | `results/_stage_sequence_ruling_effect_2026_10_17.md` | 登记件 §1 权重源（本棒实测其指纹） | `b582bde59d6d` | 18,115 |
| 4 | `.tmp/_stage3_r2_criteria_freeze_2026_10_18.md` | 判据冻结件（登记件 §1） | `885ec7fb04dd` | 9,971 |
| 5 | `tools/exp_harness.py` | 派工单点名码件（指纹核验） | `27cb200220e0` | 45,548 |
| 6 | `tools/distortion_calculator.py` | 派工单点名码件（指纹核验） | `ae7ff6e0bac5` | 50,896 |
| — | 本会话 PI 段序令（2026-10-17 23:03:18.216）＋ parent 派工单 | 授权源（消息态，**无指纹**）| — | — |

---

**落款**：**doc-writer**（agent-0032834a3e04）｜五段链 ③段-②R2 · **整理后**全量成果清单 v3.0 出件方

**⛔ 本件 0 代裁 · 0 宣告闭开 · 0 落五终判 · 0 回改既有件 · 0 移动/删除/重命名 · 0 触归档区 · 0 触 GLM · 0 触回收站 · 0 联网 · 0 读 key · 0 填充值**

**终行**：本件之计数／指纹系 **2026-10-18 01:05:00** 实测时点事实；后续落盘（含本件自身，REPO 将 **+1** 件）**0 追溯改写**本表。 *
