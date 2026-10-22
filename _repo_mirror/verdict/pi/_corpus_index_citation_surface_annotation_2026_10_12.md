# corpus 索引**引用面标注件**（批 3 · 项 E）· 双版并存之登记与逐处版本标注

> 📌 **状态栏（贯穿本件）**：🟢 **标注件 · PI 采甲**（双版并存＋另立引用面标注件・不迁移）｜⛔ **0 回改**任何既有件一字｜⛔ **0 迁移／0 移动／0 重命名／0 删除／0 合并**任何件｜⛔ 0 触 `〔归档件引用·未上传:〔归档区〕〕`（**0 读 0 写 0 列目录**）｜⛔ 0 网络／0 skill／0 LLM／0 读 `.env`／0 经手 PAT｜⛔ 0 改终判词／阈值／门柱｜⛔ 0 赋 `k_v3s_4_4_*` 布尔｜⛔ 0 断言两版互代（沿草案 §1-2 之 0 断言纪律）

---

## §0 一句话结论

PI 就批 3 项 E 之卡答 ＝「**甲：双版并存＋另立引用面标注件，不迁移**」⇒ 本件即该卡答所指之**引用面标注件**：登记**两版索引并存**之实体实测（§2）、登记**两版载荷逐键比对**（§3）、登记**引用面逐件清单与计数**（§4–§5，含 `.tmp`／排除 `.tmp` 双口径 ＋ **repo／sub 两区并核**）、给出**下游引用时之标注语**（§6）、登记**与源草案之计数差异**（§7）与**未决项**（§8）。📌 **本件之全部动作 ＝ 登记与标注，⛔ 0 迁移**。

---

## §1 PI 裁（逐字照录）

| 项 | 值 |
| :-: | :-- |
| 源件 | `results/_trae_issues_batch3_six_items_draft_2026_10_12.md`（SHA-12 `2153c41a8cff` · 29,957 B · ⛔ **0 回改**）之 **§1-2「项 E · 引用迁移（48 件仍指旧版 corpus 索引）」** |
| 卡 | `ask_1f307d991421bf48d1163a54` 之 `b3_itemE` |
| **卡答逐字** | **「甲：双版并存＋另立引用面标注件，不迁移」** |
| 本件即 | 上列卡答所指之「引用面标注件」 |
| 本件 0 声明 | ⛔ **0 迁移** · ⛔ 0 移动 · ⛔ 0 重命名 · ⛔ 0 删除 · ⛔ 0 合并 · ⛔ 0 合并两版为单一文件 · ⛔ **0 回改**任何既有件一字 |

---

## §2 两版索引之实体实测（**双版并存**之登记）

| 版 | 绝对路径 | SHA-12 | bytes | mtime |
| :-: | :-- | :-: | --: | :-- |
| **旧版** | `_repo_mirror/readout/final/index_v3_2026_09_29.json` | `3ba2449cf986` | 24,421 | `2026-10-01 09:43:44` |
| **新版** | `_repo_mirror/readout/final/index_v3_2026_10_09.json` | `74b27393574f` | 24,837 | `2026-10-09 13:39:49` |

📌 **双版并存（PI 采甲之实体面）**：两版**同存于** `〔目录引用·未上传:v20〕\` 之同一目录，实测互不覆盖、互不引继；该目录另存 `index.json`（7,335 B）与 `index_v2_2026_09_16.json`（24,150 B）⇒ 📌 **索引面共 4 件并存**（沿 Trae §1.F① 所载「多版本共存体例」）。

📌 **两版指纹与源草案 §1-2 表逐位吻合 ✓**（`3ba2449cf986` · 24,421 ／ `74b27393574f` · 24,837）——本棒独立复算确认。

📌 **sub 区（`_repo_mirror`）：两版索引皆不在盘** —— 实测 `deposon-sub\corpus\v20\index_v3_2026_09_29.json` ＝ **ABSENT**，且 `deposon-sub\corpus\` 目录本身 **不存在** ⇒ 📌 sub 区**整个 corpus 面不在盘**，故 sub 区引用面为**跨区指向**（见 §5-3／§5-4 与 §8 之 U-2）。

📌 **自引单列（⛔ 不计入引用面计数）**：两版索引**各自内含自身文件名**（旧版见 §5-5），此为 `integrity.path_hashed` 字段之自指，**非引用他件**，故本件全部引用面计数**统一采「排除索引件自引」口径**（口径定义见 §4）。

---

## §3 两版载荷逐键比对（**13 键全比** · 本棒实测）

> 📌 源草案 §1-2 仅比四键（`corpus`／`graphs`／`captions`／`n_captions`）并自承「其余 5 键未逐值比对」；**本棒已补比至全部 13 键**（旧 11 键 ∪ 新 13 键 ＝ 13）。

| 顶层键 | 旧版（09-29） | 新版（10-09） | 逐值 EQ | 备注 |
| :-: | :-- | :-- | :-: | :-- |
| `captions` | list(22) | list(22) | **EQ** | list 长度 22 ＝ 22 |
| `corpus` | len3 | len3 | **EQ** | `v20` ＝ `v20` |
| `fingerprint_anchors` | list(3) | list(3) | **EQ** | list 长度 3 ＝ 3 |
| `generator_version` | len6 | len6 | **EQ** | 字符串长度 6 ＝ 6 |
| `graphs` | list(22) | list(22) | **EQ** | list 长度 22 ＝ 22 |
| `index_v3_meta` | obj(21) | obj(21) | ⛔ 异 | obj 键数 21 ＝ 21　⛔ **异** —— 仅 `date`（`2026-09-29`→`2026-10-09`）与 `generator`（runner 由 `_v0_4_2026_09_29.py`→`_v0_4_2026_10_09.py`）二字段异 |
| `integrity` | obj(6) | obj(6) | ⛔ 异 | obj 键数 6 ＝ 6　⛔ **异** —— 仅 `path_hashed`／`path_sha256`／`content_sha256` 三**自指**字段异（两版各载自身名与自身哈希） |
| `n_captions` | 22 | 22 | **EQ** | 标量 `22` ＝ `22` |
| `n_graphs` | 22 | 22 | **EQ** | 标量 `22` ＝ `22` |
| `named_filler_rule` | len60 | len60 | **EQ** | 字符串长度 60 ＝ 60 |
| `protocol_version` | —（无） | len4 | — | 📌 **新版独有键**（旧版无此键） |
| `protocol_version_axis` | —（无） | len224 | — | 📌 **新版独有键**（旧版无此键） |
| `spec` | len20 | len20 | **EQ** | 字符串长度 20 ＝ 20 |

**📌 逐键实测结论**：

- ✅ **9 键逐值 EQ**：`corpus`／`graphs`(list 22)／`captions`(list 22)／`n_captions`(22)／`fingerprint_anchors`(3)／`generator_version`(6)／`n_graphs`／`named_filler_rule`(60)／`spec`(20)。
- ⛔ **2 键异，且差异仅在「身份／自指／日期／生成器」字段**：`index_v3_meta`（`date` ＋ `generator`）／`integrity`（`path_hashed` ＋ `path_sha256` ＋ `content_sha256`）⇒ 📌 **两版之 corpus 载荷（graphs／captions／n_captions／anchors／spec／filler 规则）无任何实质差异**。
- 📌 **2 键为新版独有**：`protocol_version`（len 4）／`protocol_version_axis`（len 224）。

📌 **与草案 §1-2 之关系**：草案之四键 EQ 结论**本棒复算成立 ✓**；草案所称「其余 5 键未逐值比对」**已被本棒补闭**（实际余键为 **7** 键，草案列举 5 键、`named_filler_rule`／`n_graphs` 未列 —— 登记于 §7）。📌 ⛔ **0 断言**两版互代或新版替代旧版；本件只登记「并存」与「逐键差异面」。

---

## §4 引用面总览（**双口径并报** · **两区并核**）

**口径定义**（⛔ 不混用）：

- **口径①（含 `.tmp`）** ＝ 该区全部文本件中按名提及该索引文件者，含 `.tmp\` 目录内件。
- **口径②（排除 `.tmp`）** ＝ 同上但剔除 `.tmp\` 目录内件。
- 两口径**均排除索引件自引**（§2 自引单列条）。

| 区 | 版 | 口径① 含 `.tmp` | 其中 `.tmp` | 口径② 排除 `.tmp` | 引用处次数（口径①） |
| :-: | :-: | --: | --: | --: | --: |
| **repo** | 旧版 | **52** | 20 | **32** | 126 |
| **repo** | 新版 | **29** | 12 | **17** | 48 |
| **sub** | 旧版 | **14** | 0 | **14** | 21 |
| **sub** | 新版 | **4** | 0 | **4** | 10 |
| **两区并核合计** | 旧版 | **66** | 20 | **46** | 147 |
| **两区并核合计** | 新版 | **33** | 12 | **21** | 58 |

**📌 区面分布（口径①，件级）**

| 版 | repo 区 | sub 区 |
| :-: | :-- | :-- |
| 旧版 | .tmp **20** ／ results **17** ／ letters **8** ／ deposon_team **6** ／ docs **1** | results **14** |
| 新版 | .tmp **12** ／ results **9** ／ deposon_team **4** ／ letters **4** | results **4** |

**📌 版本归属三判（件级）**

| 判 | repo 区 | sub 区 | 两区合计 |
| :-- | --: | --: | --: |
| **同件双引**（一文件内同时提及两版 —— 漂移核心） | **22** | **4** | **26** |
| **仅引旧版** | 30 | 10 | **40** |
| **仅引新版** | 7 | 0 | **7** |
| **引用面并集**（去重总件） | **59** | **14** | **73** |

---

## §5 引用面**逐件清单**（逐件：引用者路径 · 分类 · 引用处数 · 行号 · 所引版本）

> 📌 「分类」栏：`.tmp` ＝ 位于 `.tmp/` 目录内；`实体件` ＝ 排除 `.tmp/` 之件。行号 ＝ 该件内**提及该索引文件名**之行（1 起）。📌 所引版本**由本节标题锁定**。

### §5-1 repo 区 · 所引版本 ＝ **旧版** `index_v3_2026_09_29.json`（`3ba2449cf986`）


| # | 引用者（相对 repo 根） | 分类 | 引用处数 | 行号 |
| --: | :-- | :-: | --: | :-- |
| 1 | `.tmp/_c5_b3_rewalk_postcheck_2026_10_01.py` | `.tmp` | 3 | L5,L10,L30 |
| 2 | `.tmp/_c5_b3_rewalk_utf8check_2026_10_01.py` | `.tmp` | 1 | L4 |
| 3 | `.tmp/_exp06_1009fix_build_2026_10_10.py` | `.tmp` | 1 | L348 |
| 4 | `.tmp/_exp06_1009fix_verify_2026_10_10.py` | `.tmp` | 1 | L128 |
| 5 | `.tmp/_exp06_fixcopy_verify_probe_2026_10_10.py` | `.tmp` | 1 | L86 |
| 6 | `.tmp/_gh_tree.txt` | `.tmp` | 1 | L338 |
| 7 | `.tmp/_ofc_s1_inventory.json` | `.tmp` | 1 | L2803 |
| 8 | `.tmp/_ofc_s1b_inventory.json` | `.tmp` | 2 | L3937,L3948 |
| 9 | `.tmp/_s4fill_probe4.py` | `.tmp` | 1 | L4 |
| 10 | `.tmp/_vk_pv02_recheck_a.py` | `.tmp` | 1 | L12 |
| 11 | `.tmp/_vk_pv02_recheck_b.py` | `.tmp` | 1 | L21 |
| 12 | `.tmp/_vk_pv02_recheck_c.py` | `.tmp` | 2 | L11,L34 |
| 13 | `.tmp/_vk_pv02_recheck_g.py` | `.tmp` | 1 | L9 |
| 14 | `.tmp/c5_guard_minmaxstd_2026_10_01.py` | `.tmp` | 3 | L6,L23,L274 |
| 15 | `.tmp/k_v3df_0_1_four_readings_2026_10_09.py` | `.tmp` | 1 | L18 |
| 16 | `.tmp/u04_1_chain_verify.py` | `.tmp` | 1 | L8 |
| 17 | `.tmp/u04_1_dual_verify.py` | `.tmp` | 1 | L7 |
| 18 | `.tmp/u04_1_make_data.py` | `.tmp` | 1 | L10 |
| 19 | `.tmp/vk_v3df_0_1_materiality.py` | `.tmp` | 1 | L6 |
| 20 | `.tmp/vk_v3df_0_1_verify_2026_10_09.py` | `.tmp` | 1 | L10 |
| 21 | `deposon_team/plugins/_ofc_s2_2026_10_12.py` | 实体件 | 1 | L43 |
| 22 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_fix_2026_10_10.py` | 实体件 | 1 | L142 |
| 23 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_rename_2026_10_10.py` | 实体件 | 1 | L126 |
| 24 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_selfverify_fix_2026_10_10.py` | 实体件 | 1 | L122 |
| 25 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py` | 实体件 | 3 | L7,L62,L64 |
| 26 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py` | 实体件 | 2 | L7,L84 |
| 27 | `docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md` | 实体件 | 3 | L118,L331,L411 |
| 28 | `letters/_commission_glm_dualtrack_paper_v0.5_2026_10_01.md` | 实体件 | 1 | L135 |
| 29 | `letters/_commission_kimi_upload_2026_10_01_v0.2.md` | 实体件 | 1 | L96 |
| 30 | `letters/_commission_trae_direct_fix_oct_full_coverage_2026_10_12.md` | 实体件 | 3 | L110,L243,L245 |
| 31 | `letters/_dualtrack_paper_clue_book_v0.5_2026_10_01.md` | 实体件 | 1 | L313 |
| 32 | `letters/_dualtrack_paper_clue_book_v0.6_local_remote_2026_10_12.md` | 实体件 | 2 | L165,L375 |
| 33 | `letters/_internal_true_clue_book_2026_10_12.md` | 实体件 | 1 | L556 |
| 34 | `letters/_oct_full_coverage_reply_trae_code_2026_10_12.md` | 实体件 | 1 | L80 |
| 35 | `letters/查理_deposon双主线论文终稿_2026-10-01_v0.3.md` | 实体件 | 1 | L1222 |
| 36 | `results/_achievements_inventory_full_2026_10_09.md` | 实体件 | 1 | L342 |
| 37 | `results/_exp06_selfverified_renaming_note_2026_10_10.md` | 实体件 | 2 | L40,L315 |
| 38 | `results/_exp06_selfverified_runner_fix_note_2026_10_10.md` | 实体件 | 2 | L28,L184 |
| 39 | `results/_exp06_supplement_four_gaps_2026_10_10.md` | 实体件 | 3 | L39,L123,L210 |
| 40 | `results/_k_v3df_0_1_four_readings_2026_10_09.json` | 实体件 | 27 | L27,L167,L188,L227,L245,L266,L295,L313,L341,L369,L402,L423,L444,L473,L503,L534,L565,L582,L610,L647,L665,L693,L717,L733,L751,L772,L1530 |
| 41 | `results/_k_v3df_0_1_four_readings_2026_10_09.md` | 实体件 | 28 | L20,L59,L60,L61,L62,L63,L64,L65,L66,L67,L83,L84,L85,L86,L87,L88,L89,L90,L91,L92,L93,L94,L108,L109,L110,L111,L182,L348 |
| 42 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 实体件 | 2 | L1863,L3597 |
| 43 | `results/_repo_post_cleanup_snapshot_2026_10_12.md` | 实体件 | 1 | L530 |
| 44 | `results/_s4_daily_share_margin_prerequisite_2026_10_09.md` | 实体件 | 1 | L32 |
| 45 | `results/_s4_substrate_topup_collection_register_2026_10_09.md` | 实体件 | 1 | L84 |
| 46 | `results/_trae_issues_batch3_six_items_draft_2026_10_12.md` | 实体件 | 2 | L53,L233 |
| 47 | `results/_u04_1_exemption_precondition_verification_2026_10_09.json` | 实体件 | 1 | L9 |
| 48 | `results/c5_b_group_root_candidate_2026_10_01.md` | 实体件 | 1 | L58 |
| 49 | `results/c5_guard_0_1_recheck_verdict_2026_10_01.md` | 实体件 | 1 | L20 |
| 50 | `results/c5_guard_minmaxstd_readings_2026_10_01.json` | 实体件 | 1 | L10 |
| 51 | `results/c5_guard_minmaxstd_report_2026_10_01.md` | 实体件 | 1 | L14 |
| 52 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json` | 实体件 | 2 | L48,L58 |

📌 小计：**52 件**（＝ 口径① 52 ／ 口径② 32）；引用处合计 126 处。

### §5-2 repo 区 · 所引版本 ＝ **新版** `index_v3_2026_10_09.json`（`74b27393574f`）


| # | 引用者（相对 repo 根） | 分类 | 引用处数 | 行号 |
| --: | :-- | :-: | --: | :-- |
| 1 | `.tmp/_exp06_1009fix_build_2026_10_10.py` | `.tmp` | 2 | L425,L439 |
| 2 | `.tmp/_exp06_1009fix_verify_2026_10_10.py` | `.tmp` | 1 | L127 |
| 3 | `.tmp/_gh_tree.txt` | `.tmp` | 1 | L339 |
| 4 | `.tmp/_ofc_s1_inventory.json` | `.tmp` | 1 | L2813 |
| 5 | `.tmp/_ofc_s1b_inventory.json` | `.tmp` | 2 | L3951,L3962 |
| 6 | `.tmp/_vk_pv02_recheck_a.py` | `.tmp` | 1 | L9 |
| 7 | `.tmp/_vk_pv02_recheck_b.py` | `.tmp` | 1 | L20 |
| 8 | `.tmp/_vk_pv02_recheck_c.py` | `.tmp` | 2 | L9,L34 |
| 9 | `.tmp/_vk_pv02_recheck_d.py` | `.tmp` | 1 | L14 |
| 10 | `.tmp/_vk_pv02_recheck_e.py` | `.tmp` | 2 | L15,L25 |
| 11 | `.tmp/exp06_independent_json_gen_2026_10_10.py` | `.tmp` | 1 | L25 |
| 12 | `.tmp/exp06_supplement_probe_2026_10_10.py` | `.tmp` | 2 | L125,L145 |
| 13 | `deposon_team/plugins/_ofc_s2_2026_10_12.py` | 实体件 | 1 | L44 |
| 14 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_fix_2026_10_10.py` | 实体件 | 1 | L148 |
| 15 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_rename_2026_10_10.py` | 实体件 | 1 | L132 |
| 16 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py` | 实体件 | 2 | L72,L74 |
| 17 | `letters/_commission_trae_direct_fix_oct_full_coverage_2026_10_12.md` | 实体件 | 3 | L110,L243,L245 |
| 18 | `letters/_dualtrack_paper_clue_book_v0.6_local_remote_2026_10_12.md` | 实体件 | 1 | L375 |
| 19 | `letters/_internal_true_clue_book_2026_10_12.md` | 实体件 | 1 | L557 |
| 20 | `letters/_oct_full_coverage_reply_trae_code_2026_10_12.md` | 实体件 | 1 | L81 |
| 21 | `results/_achievements_inventory_full_2026_10_09.md` | 实体件 | 1 | L343 |
| 22 | `results/_exp06_independent_check_2026_10_10.json` | 实体件 | 2 | L29,L346 |
| 23 | `results/_exp06_selfverified_renaming_note_2026_10_10.md` | 实体件 | 3 | L38,L218,L313 |
| 24 | `results/_exp06_supplement_four_gaps_2026_10_10.md` | 实体件 | 4 | L38,L117,L124,L195 |
| 25 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 实体件 | 3 | L1864,L2981,L3598 |
| 26 | `results/_repo_post_cleanup_snapshot_2026_10_12.md` | 实体件 | 1 | L531 |
| 27 | `results/_trae_issues_batch3_six_items_draft_2026_10_12.md` | 实体件 | 2 | L54,L233 |
| 28 | `results/_upload_ledger_2026_10_12.json` | 实体件 | 2 | L74,L76 |
| 29 | `results/_upload_plan_2026_10_12.json` | 实体件 | 2 | L59,L60 |

📌 小计：**29 件**（＝ 口径① 29 ／ 口径② 17）；引用处合计 48 处。

### §5-3 sub 区（`_repo_mirror` · 只读 · ⛔ 0 写）· 所引版本 ＝ **旧版** `index_v3_2026_09_29.json`


| # | 引用者（相对 sub 根） | 分类 | 引用处数 | 行号 |
| --: | :-- | :-: | --: | :-- |
| 1 | `results/_ea_audit_batch_vk_2026_10_09.md` | 实体件 | 1 | L91 |
| 2 | `results/_exp06_kcf4_check_bit_landing_2026_10_10.md` | 实体件 | 1 | L35 |
| 3 | `results/_k_v3df_0_1_readings_verdict_2026_10_09.md` | 实体件 | 2 | L16,L341 |
| 4 | `results/_mini_round_3_decisions_register_2026_10_01.md` | 实体件 | 1 | L62 |
| 5 | `results/_protocol_version_landing_status_2026_10_09.md` | 实体件 | 3 | L22,L40,L105 |
| 6 | `results/_u04_1_exemption_precondition_verification_2026_10_09.md` | 实体件 | 2 | L15,L180 |
| 7 | `results/_upload_ledger_kimi_2026_10_01.json` | 实体件 | 1 | L13 |
| 8 | `results/_uv04_field_completeness_fill_2026_10_01.md` | 实体件 | 1 | L19 |
| 9 | `results/_v3_02_ethard_closure_verdict_2026_10_09.md` | 实体件 | 2 | L106,L189 |
| 10 | `results/_v3_02_ethard_execution_register_2026_10_09.md` | 实体件 | 1 | L97 |
| 11 | `results/_v3_02_override_register_2026_10_09.md` | 实体件 | 2 | L82,L263 |
| 12 | `results/_v5_v3_deg_c5_b_halt_report_2026_09_29.md` | 实体件 | 1 | L156 |
| 13 | `results/c5_b_group_verdict_2026_10_01.md` | 实体件 | 1 | L16 |
| 14 | `results/c5_protocol_version_annex_2026_10_01.md` | 实体件 | 2 | L80,L114 |

📌 小计：**14 件**；引用处合计 21 处。📌 **sub 区无 `.tmp` 面**（实测 `deposon-sub\.tmp` 不存在）⇒ 口径①＝口径②＝**14**。📌 所指实体在 sub 区**不在盘**（§2）。

### §5-4 sub 区 · 所引版本 ＝ **新版** `index_v3_2026_10_09.json`


| # | 引用者（相对 sub 根） | 分类 | 引用处数 | 行号 |
| --: | :-- | :-: | --: | :-- |
| 1 | `results/_exp06_kcf4_check_bit_landing_2026_10_10.md` | 实体件 | 3 | L34,L119,L158 |
| 2 | `results/_v3_02_ethard_closure_verdict_2026_10_09.md` | 实体件 | 3 | L24,L40,L80 |
| 3 | `results/_v3_02_ethard_execution_register_2026_10_09.md` | 实体件 | 2 | L65,L148 |
| 4 | `results/_v3_02_override_register_2026_10_09.md` | 实体件 | 2 | L82,L219 |

📌 小计：**4 件**；引用处合计 10 处。所指实体在 sub 区**不在盘**（§2）。

### §5-5 索引件**自引**（⛔ 单列，**不计入** §4／§5 之引用面计数）

| 版 | 自引件（相对 repo 根） | 引用处数 | 行号 | 自指字段 |
| :-: | :-- | --: | :-- | :-- |
| 旧版 | `corpus/v20/index_v3_2026_09_29.json` | 1 | — | `integrity.path_hashed` ＝ `index_v3_2026_09_29.json`（载自身文件名） |
| 旧版 | `results/_corpus_index_citation_surface_annotation_2026_10_12.md`（**本标注件自身**） | ⛔ **0 计入** | — | 本件为标注面，非引用面；其提及数随本件文本变动，**故不予登记**（避免自我计数、逐次递增） |
| 新版 | `corpus/v20/index_v3_2026_10_09.json` | 1 | — | `integrity.path_hashed` ＝ `index_v3_2026_10_09.json`（载自身文件名） |
| 新版 | `results/_corpus_index_citation_surface_annotation_2026_10_12.md`（**本标注件自身**） | ⛔ **0 计入** | — | 本件为标注面，非引用面；其提及数随本件文本变动，**故不予登记**（避免自我计数、逐次递增） |

### §5-6 **同件双引**清单（漂移核心 · 一文件内同时提及两版）

| # | 区 | 引用者 | 旧版行号 | 新版行号 |
| --: | :-: | :-- | :-- | :-- |
| 1 | repo | `.tmp/_exp06_1009fix_build_2026_10_10.py` | L348 | L425,L439 |
| 2 | repo | `.tmp/_exp06_1009fix_verify_2026_10_10.py` | L128 | L127 |
| 3 | repo | `.tmp/_gh_tree.txt` | L338 | L339 |
| 4 | repo | `.tmp/_ofc_s1_inventory.json` | L2803 | L2813 |
| 5 | repo | `.tmp/_ofc_s1b_inventory.json` | L3937,L3948 | L3951,L3962 |
| 6 | repo | `.tmp/_vk_pv02_recheck_a.py` | L12 | L9 |
| 7 | repo | `.tmp/_vk_pv02_recheck_b.py` | L21 | L20 |
| 8 | repo | `.tmp/_vk_pv02_recheck_c.py` | L11,L34 | L9,L34 |
| 9 | repo | `deposon_team/plugins/_ofc_s2_2026_10_12.py` | L43 | L44 |
| 10 | repo | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_fix_2026_10_10.py` | L142 | L148 |
| 11 | repo | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_rename_2026_10_10.py` | L126 | L132 |
| 12 | repo | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py` | L7,L84 | L72,L74 |
| 13 | repo | `letters/_commission_trae_direct_fix_oct_full_coverage_2026_10_12.md` | L110,L243,L245 | L110,L243,L245 |
| 14 | repo | `letters/_dualtrack_paper_clue_book_v0.6_local_remote_2026_10_12.md` | L165,L375 | L375 |
| 15 | repo | `letters/_internal_true_clue_book_2026_10_12.md` | L556 | L557 |
| 16 | repo | `letters/_oct_full_coverage_reply_trae_code_2026_10_12.md` | L80 | L81 |
| 17 | repo | `results/_achievements_inventory_full_2026_10_09.md` | L342 | L343 |
| 18 | repo | `results/_exp06_selfverified_renaming_note_2026_10_10.md` | L40,L315 | L38,L218,L313 |
| 19 | repo | `results/_exp06_supplement_four_gaps_2026_10_10.md` | L39,L123,L210 | L38,L117,L124,L195 |
| 20 | repo | `results/_repo_full_inventory_catalogue_2026_10_12.md` | L1863,L3597 | L1864,L2981,L3598 |
| 21 | repo | `results/_repo_post_cleanup_snapshot_2026_10_12.md` | L530 | L531 |
| 22 | repo | `results/_trae_issues_batch3_six_items_draft_2026_10_12.md` | L53,L233 | L54,L233 |
| 23 | sub | `results/_exp06_kcf4_check_bit_landing_2026_10_10.md` | L35 | L34,L119,L158 |
| 24 | sub | `results/_v3_02_ethard_closure_verdict_2026_10_09.md` | L106,L189 | L24,L40,L80 |
| 25 | sub | `results/_v3_02_ethard_execution_register_2026_10_09.md` | L97 | L65,L148 |
| 26 | sub | `results/_v3_02_override_register_2026_10_09.md` | L82,L263 | L82,L219 |

📌 小计：**repo 22 件 ＋ sub 4 件 ＝ 26 件**同件双引 ⇒ 📌 **引用漂移已由隐性转为显性可查**（沿草案 §1-2 ② 之拟登记目的）。

---

## §6 **标注语**（供下游引用时指明所指版本）

**① 体例总句**（沿草案 §1-2 ② 之拟字面，PI 采甲）：

> 「两版索引并存为既定体例；引用面以标注件为准，未标注处沿原件不动。」

**② 逐处版本标注语**（下游引用时**书写模板** —— ⛔ **0 回写**既有件；如需回写即构成「改引」，须**另立件**）：

- **所引 ＝ 旧版时**：

  > 「本处所指索引 ＝ **旧版** `corpus/v20/index_v3_2026_09_29.json`（SHA-12 `3ba2449cf986` · 24,421 B · mtime `2026-10-01 09:43:44`）。该版与新版 `index_v3_2026_10_09.json`（`74b27393574f` · 24,837 B）**并存为既定体例**；两版 `graphs`／`captions`／`n_captions`／`corpus` 四键载荷**逐值相同**，13 键中仅 `index_v3_meta`／`integrity` 之**身份自指字段**与新版新增之 `protocol_version`／`protocol_version_axis` 有别。⛔ **0 断言**二者互代或新版替代旧版。」

- **所引 ＝ 新版时**：

  > 「本处所指索引 ＝ **新版** `corpus/v20/index_v3_2026_10_09.json`（SHA-12 `74b27393574f` · 24,837 B · mtime `2026-10-09 13:39:49`），含 `protocol_version`／`protocol_version_axis` 两独有键。该版与旧版 `index_v3_2026_09_29.json`（`3ba2449cf986` · 24,421 B）**并存为既定体例**。⛔ **0 断言**二者互代。」

- **同件双引时**（§5-6 之 26 件）：

  > 「本件**同时**引用两版索引（逐行号见引用面标注件 §5-6）：旧版 …… ／ 新版 ……；两版并存，非版本迁移，非笔误。」

**③ 引用计数之标注**：凡载引用件数者，须**同时标明口径**（「含 `.tmp`」或「排除 `.tmp`」）与**区**（repo／sub），⛔ **0 单报一数**（沿「模式三·同概念多口径并存」之弊 —— 此即 §7 差异登记之由来）。

---

## §7 与源草案 §1-2 之**计数差异登记**

> 📌 依「模式三／四·对账责任面」：本件复算值 vs 草案值，逐条登记，⛔ 0 代草案更正、⛔ 0 代 PI 裁定。

| # | 测项 | 草案 §1-2 载值 | 本棒实测值 | 出入判定 |
| --: | :-- | :-- | :-- | :-- |
| D-1 | 旧版指纹／bytes | `3ba2449cf986` · 24,421 B | `3ba2449cf986` · 24,421 B | ✅ **逐位吻合** |
| D-2 | 新版指纹／bytes | `74b27393574f` · 24,837 B | `74b27393574f` · 24,837 B | ✅ **逐位吻合** |
| D-3 | 四键逐值比对 | 四键 EQ | 四键 EQ ＋ 载荷 sha12 复算 | ✅ **复算成立** |
| D-4 | 引用件数（含 `.tmp`） | 旧 52 ／ 新 29 | 旧 **52** ／ 新 **29** | ✅ **吻合** |
| D-5 | 引用件数（排除 `.tmp`） | 旧 32 ／ 新 17 | 旧 **32** ／ 新 **17** | ✅ **吻合** |
| D-6 | 旧版区面分布 | `.tmp` 20 ／ `results` **16** ／ `letters` 8 ／ `plugins` 6 ／ `corpus/v20` **1** ／ `docs/V3X` 1 | `.tmp` 20 ／ `results` **17** ／ `letters` 8 ／ `plugins` 6 ／ `corpus/v20` **0** ／ `docs/V3X` 1 | ⚠️ **总数同（52）而两格异**（见 D-6a） |
| D-6a | ↳ 差异成因 | 草案将索引件**自引**计入 `corpus/v20` 1；而草案**自身**（`results/_trae_issues_batch3_six_items_draft_2026_10_12.md` L53／L233）提及该二文件名却不可能计入己方统计 ⇒ 致 `results` 少计 1、`corpus/v20` 多计 1 | 本件口径 ＝ **排除自引**（§4 口径定义） | 📌 一增一减、**总数巧合相等**；⛔ 0 断言草案有误（其口径自洽） |
| D-7 | 草案所称「其余 5 键」 | 「其余 5 键（`spec`／`integrity`／`fingerprint_anchors`／`index_v3_meta`／`generator_version`）未逐值比对」 | 旧版 11 键 减 四键 ＝ **7 键**；草案列举 5 键，`named_filler_rule`／`n_graphs` **未列** | ⚠️ **枚举不全**；本棒已补比全 13 键（§3） |
| D-8 | **sub 区**引用面 | **未载** | 旧 **14** 件 ／ 新 **4** 件（全在 `results/`，sub 无 `.tmp` 面） | 📌 **草案未覆盖面**（本件补） |
| D-9 | sub 区两版索引实体 | 未载 | **两版皆 ABSENT**（`deposon-sub\corpus\` 不存在） | 📌 **草案未覆盖面**（本件补） |
| D-10 | Trae §1.E「48 件／25 件」 | 草案 §1-2 注：落于两口径之间，**计数口径未统一** | 本件两口径仍并存（§4）⇒ 该差异**未被消除，仅被标注** | ⛔ 0 统一、⛔ 0 代裁（登记于 §8 U-4） |

---

## §8 未决项

| # | 未决项 | 实测事实 | ⛔ 本件 0 为 |
| --: | :-- | :-- | :-- |
| U-1 | **计数口径未统一**（Trae 48／25 vs 本件 66／33 vs 草案 52／29） | 三组数字口径各异：Trae 未标口径、草案为 repo 区、含 `.tmp` | ⛔ 0 统一口径、⛔ 0 代 PI 裁定；本件**双口径并报**并已定义口径（§4 口径定义 ＋ §6 ③ 标注要求） |
| U-2 | **sub 区 14＋4 处引用指向 sub 区不在盘之实体** | `deposon-sub\corpus\` 目录不存在；两版索引仅存于 repo 区 | ⛔ 0 在 sub 侧另立登记、⛔ 0 迁入、⛔ 0 改引；**sub 为只读区（0 写）**，处置权属 PI |
| U-3 | **「实质读数」vs「仅登记提及」之区分未判** | 草案 §1-2 ② 曾拟登记该维度；本棒⛔ 0 逐处判读（仅登记「引用处＋行号＋版本」） | ⛔ 0 代判该维度；如需该维度须**另派逐处判读棒**（本件不作断言） |
| U-4 | **与 §1-1（`.tmp` 归档）强耦合** | 本件引用面含 `.tmp` 件 旧 20 ／ 新 12；若 `.tmp` 先行归档，本引用面将**二次变动** | ⛔ 0 预判、⛔ 0 先行排期；本件**须随 `.tmp` 处置重出**（届时**另立修订件**，⛔ 0 回改本件） |
| U-5 | **两版互代关系** | §3 实测 13 键中 9 键 EQ、2 键仅身份自指字段异、2 键新版独有 | ⛔ **0 断言**互代／替代；⛔ 0 断言任一版为伪 |
| U-6 | **draft 所载 `.tmp` 面 20＋12 处**与本件一致否 | 一致（本件复算 `.tmp` 旧 20 ／ 新 12） | ✅ 已闭（0 未决） |

---

## §9 件末声明

1. 📌 **本件为「标注面」**：登记两版索引之**并存实体**、**逐键差异**、**逐处引用面**与**标注语**。
2. ⛔ **本件⛔ 不构成任何引用面之改写** —— §5 所列 52＋29＋14＋4 件引用面**全部保持原样**，其行内文本**一字未动**；两版索引件**未被迁移、未被移动、未被重命名、未被删除、未被合并**。
3. ⛔ **下游如需改引**（即把某处引用由旧版改指新版或反之），**须另立件**（勘正件／路径勘误件），并沿 **0 回改铁律**走另立面；⛔ 0 借本件回写既有件。
4. ⛔ 本件 0 触 `〔归档件引用·未上传:〔归档区〕〕`（**0 读 0 写 0 列目录**）；⛔ 0 网络／0 skill／0 LLM／0 读 `.env`／0 经手 PAT；⛔ 0 改终判词／阈值／门柱；⛔ 0 赋 `k_v3s_4_4_*` 布尔。
5. 📌 **本件为新件，⛔ 0 回改任何既有件**（含源草案 `results/_trae_issues_batch3_six_items_draft_2026_10_12.md`，其 SHA-12 `2153c41a8cff` · 29,957 B 保持不变）。
6. ⛔ 本件 0 触他棒产物：`results/_tmp_archive_disposition*`／`results/_duplicate_name_six_items_attribution*`／`results/_batch3_closure*`／`results/_trae_issues_batch3_six_items_draft*`／`letters/`／`_bob_*`／`_remote_baseline*` 之**内容**（`letters\` 仅作**只读引用面统计**）。

---

📌 **件末复述**：**两版索引并存为既定体例；引用面以本标注件为准，未标注处沿原件不动；⛔ 0 迁移，⛔ 0 回改，下游改引须另立件。**
