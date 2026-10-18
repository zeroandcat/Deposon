# V3–V4 全量成果清单 v2.0（五段链 ③段-②）

> **版本**：v2.0（全量清单件）｜**取代关系**：⛔ **0 取代 0 回改**任何既有件——本件系**另立新件**，与 v1.0 族（`_v3_v4_achievements_inventory_*_2026_09_24.md` 三件）**并存**，凡口径冲突以本件为准
> **出件方**：**doc-writer（agent-0032834a3e04）**｜**实测时点**：2026-10-12 03:20:44 (+08:00)｜**件路径**：`results/_achievements_inventory_full_2026_10_09.md`
> **命名**：沿 `artifacts/plan.md` §四③段**既批设计名**（原设计产件路径逐字为 `results/_achievements_inventory_full_2026_10_09.md`），含 `2026_10_09` 日期戳；**命名理由如实登记**见 §2.5
> **状态**：🟡 **本件 0 宣告任何闭/开/段之毕**｜⛔ **0 立收尾桶**（③段-③ 之棒，本棒不启）｜⛔ **0 代 PI 拍板**
> **版式**：UTF-8 无 BOM · 纯 LF · 落盘后字节级自核（SHA-12／bytes／BOM／CR／TAB／CTRL）

---

## §0 · 一句话结论

**两区（`deposon-repo` ＋ `deposon-sub`）实测共 2,891 件、合计 113,578,773 bytes**（REPO **1,704 件 / 54,847,017 bytes**；SUB **1,187 件 / 58,731,756 bytes**）；其中成果面（除 `.tmp/` 噪声面外）逐件展开 **2,450** 件，`.tmp/` 面 **441** 件按既有惯例仅作汇总登记；**10-10→10-12 增量窗内共 471 件**，逐件附 SHA-12。

📌 **计数为时点事实**：实测期间存在**同链并发写入**（见 §8 漂移面 D-4），故本件计数以「实测时点 2026-10-12 03:20:44」为准，**不复述、不回溯校正**。

## §1 · 授权与底本

### §1.1 授权来源（逐条）

| # | 授权源 | 原文要点 | 本件之执行 |
| :-:|:--|:--|:--|
| 1 | `artifacts/plan.md` §四③段（既批设计·10-09 修订版，存于 `_questionnaire_cards_intake_register_2026_10_09.md` 卡载荷内；**该路径实体已不在盘**，见 §9-N1） | 「产出 `results/_achievements_inventory_full_2026_10_09.md`（合订 3dir 主干＋三 addendum＋erratum＋10-01→10-09 全增量；三面计数并列 0 校正）」 | 逐项落为 §3–§7 |
| 2 | 同上·验收条款 | 「逐件 SHA-12/bytes/mtime；未核得写「未核得」；与 closing_round 册逐份对齐」 | 落为 §4／§9／§6 |
| 3 | **PI 2026-10-12 令**（经 parent 转派） | 「**记得更新清单**」「**先完整全量得整理文件夹再立全清单**」 | 本棒＝**立全清单**之棒；整理已由 ③段-① 毕 |
| 4 | parent 派工单（2026-10-12 03:14） | 日期窗**顺延至 10-01→10-12**；逐件表以终态快照为底本；0 立桶、0 代裁 | 落为 §7 增量窗 |

### §1.2 底本（**全部经本棒 `sha256` 逐件复核**；⛔ 0 目视沿用 parent 转录值））

| 角色 | 相对路径 | SHA-12（实测） | bytes（实测） | mtime（实测） | 复核 |
|:--|:--|:--|--:|:--|:--|
| ③段-① 整理执行登记 | `results/_v4_closeout_bulk_reorganize_register_2026_10_12.md` | `2b244f0760b4` | 197,283 | 2026-10-12 03:09:00 | ✅ 与转录值一致 |
| **终态盘面指纹底本** | `results/_repo_post_cleanup_snapshot_2026_10_12.md` | `6039a6e08017` | 309,419 | 2026-10-12 03:09:29 | ✅ 与转录值一致 |
| 清点底本 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | `96720fcfd76a` | 591,833 | 2026-10-12 02:11:15 | ✅ 与转录值一致 |
| 账目校正 | `results/_v4_closeout_account_reconciliation_2026_10_12.md` | `4a3b661a7d13` | 24,453 | 2026-10-12 02:16:41 | ✅ 与转录值一致 |
| 转移与清噪登记 | `results/_v4_closeout_moves_and_cleanup_register_2026_10_12.md` | `69a834caf812` | 18,568 | 2026-10-12 02:30:44 | ✅ 与转录值一致 |

📌 **上表 5 件全部与派工单转录值一致**；**指纹底本**＝`_repo_post_cleanup_snapshot_2026_10_12.md`（`6039a6e08017`），本件逐件表之结构与排序沿之。

## §2 · 惯例回查结果（回查证据在案，⛔ 0 按最窄义自拟）

### §2.1 「3dir」所指 —— 已确证

**3dir ＝ MAIN ＋ ARCHIVE ＋ SUB 三目录**，非「repo／sub／交付包」。

**回查证据**：v1.0 族 3dir 件 `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` 第 5 行逐字：

> Scope: **MAIN** (`〔本机路径〕/private-data/deposon-repo`) + **ARCHIVE** (`〔本机路径〕/private-data/_non_upload_local_archive`) + **SUB** (`〔本机路径〕/private-data/deposon-sub`)

| 标签 | 绝对路径 | 本棒处置 |
|:--|:--|:--|
| MAIN | `_repo_mirror` | ✅ 全量实测逐件 |
| SUB | `_repo_mirror` | ✅ 全量实测逐件 |
| ARCHIVE | `〔本地归档区〕` | ⛔ **本棒授权 0 读 0 写 0 列目录** ⇒ **未核得（禁触区）**，见 §9-N2 |

**`Deposon_v1_2_0_交付包` 不属 3dir**：该目录在 v1.0 族 3dir 件之 Scope／三目录表中**0 出现**，且 §三-2 三项实证亦仅述 repo/sub 两区 ⇒ **本件不纳入**（列为范围外事实登记）。

### §2.2 「三面」所指 —— **已查惯例，⚠ 尚余歧义**

**已查惯例（仓内「三面」既有四义，逐条列证）**：

| 义 | 出处 | 释义 | 与本件设计之合 |
|:-:|:--|:--|:--|
| 义-1 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` §1.1「Directory roll-up」 | MAIN/ARCHIVE/SUB **三目录计数**并列 | **最高**：与同句「3dir 主干」连读，计数之三面即三目录 |
| 义-2 | `_g5_ccp_execution_prereqs_2026_10_10.md` L11 | 「三面登记 ＋ 三路独立重算同值」＝**同一事实之三个独立记录面** | 中：「并列 0 校正」可解为三独立面并陈 |
| 义-3 | `letters/TRAE_V4_WALKTHROUGH_BUGFIX_REQUEST_2026_09_27.md` L363 | 构造/判定/登记/跨系列「三面一致性」 | 低：属走读一致性核验，非计数 |
| 义-4 | `letters/查理_deposon双主线论文终稿_2026-10-01_v0.3.md` L624 | 可提取/可迁移/批判性「三面度量」 | 低：属论文指标面 |

**本件工作读法（明示·未裁）**：§4 之逐件表已给出 **MAIN/SUB 两区全量逐件**（ARCHIVE 因禁触为「未核得」）⇒ §5 依**义-1**呈「三目录计数并列表」，**同时**并列**义-2** 之「三独立计数面」（盘面实测／终态快照登记／派工单转录）——**两读法一并呈出，不择一、不消解**。

**余歧义（须 PI／parent 定，本棒 0 自裁）**：「三面计数并列 0 校正」之「三面」究指**三目录面（义-1）**抑或**三独立计数面（义-2）**？本件以「两表并出」消解歧义，⛔ **0 按最窄义自拟**。

**「并列 0 校正」之含义复核（沿既有纪律）**：已回查既有成文 —— `results/_fake_verdict_reverify_sixitem_ledger_2026_09_30.md` §5.3「同族漂移登记（仓外 · **本棒 0 校正** · 待 PI 裁）」、`results/_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json` `difference_note`「两口径如实并记，**归口 V4 收尾整理时批量校正**」。⇒ **本件口径复核结论：三口径计数并列呈示、⛔ 0 逐项校正、⛔ 0 择一、⛔ 0 静默合并**；差异一律登记不改。

### §2.3 「`.tmp` 是否逐件展开」—— 已回查：依惯例 **仅汇总**

**回查证据**：v1.0 族 3dir 件 §0.3 Coverage rules 逐字——「every file in MAIN/ARCHIVE/SUB is disk-tested; **brief enumerated detail covers substantive achievements; transient/internal-only files appear in the count roll-up only**」；同件 §3 各目录行「Substantive items: 1283 (**transient .pyc/.log: 41**)」之计数/枚举二分。

**实测佐证**：该 3dir 件全文 3,449 行中，`results/` 路径行 **1,366** 行（全量展开），而含 `.tmp` 之表行仅 **17** 行（系被选中之实质件，**非全量**）。

**本件处置（依惯例）**：`.tmp/` 面 **441 件 / 11,375,518 bytes 不逐件展开**，仅于 §4.1 出汇总表；其 **10-10→10-12 增量窗内成员**则于 §7 **逐件附 SHA-12**（增量章之验收要求优先）。

### §2.4 命名惯例 —— 已回查

**已查惯例**：`results/` 成果族**一律带日期戳**（`_…_2026_10_09.md` 式），且**同一对象之续版另立新名＋日期顺延**（例：`_v4_closeout_moves_and_cleanup_register_2026_10_12.md` 之于前轮；`_closeout_bucket_refresh_2026_10_09.md` 之设计名亦自带日期戳）。

**本件命名处置**：沿 §1.1 授权源 ① 之**既批设计名逐字** `results/_achievements_inventory_full_2026_10_09.md`。

**⚠ 命名理由如实登记（两事实并存，不消解）**：
1. 该路径 `Test-Path=False`、glob `*achievements_inventory_full*` **0 命中** ⇒ **未撞名**，沿既批名**无覆盖风险**；
2. `results/_stage_sequence_violation_register_2026_10_12.md` L78 逐字登记本件路径为 ③段-② 之**约定产件**（「`results/_achievements_inventory_full_2026_10_09.md`」）⇒ **既有在册登记件以该名为准**；
3. 故**虽**日期窗已顺延至 10-12，**仍沿既批名**（不另立 `_2026_10_12` 新名）—— 理由：**在册登记一致性 ＋ 零撞名**；窗口顺延**不**作命名顺延之充分理由。
4. **窗口顺延本身之登记**：设计件原文为「10-01→**10-09** 全增量」，本件落为「**10-01→10-12**」，此为 PI 2026-10-12「记得更新清单」令之执行，**在 §7 明示顺延**。

### §2.5 余歧义汇总（0 沉默略过）

| # | 歧义 | 已查惯例 | 余留 | 本件处置 |
|:-:|:--|:--|:--|:--|
| A-1 | 「三面」所指 | 四义见 §2.2 | **义-1 vs 义-2 未决** | 两表并出，0 择一 |
| A-2 | 「三 addendum」所指 | 仓内 addendum 命名件 **39** 件（§3.2.1 全枚举），「三」无唯一收敛 | **未决** | **全枚举 ＋ 候选三组并出**（§3.2.2），⛔ 0 择一 |
| A-3 | 3dir 含 ARCHIVE vs 本棒禁触 ARCHIVE | 3dir 定义确含 ARCHIVE | **授权冲突** | ARCHIVE 面列「**未核得（禁触区）**」（§9-N2） |
| A-4 | `.tmp` 派工单称 560 件 vs 实测 441 件 | 既有惯例 `.tmp` 仅汇总 | **数值差未校正** | 两数并列（§5），0 校正 |

## §3 · 合订主轴（3dir 主干 ＋ addendum ＋ erratum ＋ 增量）

### §3.1 3dir 主干

| 面 | 对象 | SHA-12（实测） | bytes | mtime |
|:--|:--|:--|--:|:--|
| MAIN·v1.0 基件 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | `965db22e9130` | 194,083 | 2026-09-30 16:18:35 |
| MAIN·v1.0 3dir 扩展件 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | `df7e9cd39251` | 355,819 | 2026-09-29 12:12:36 |
| ARCHIVE 面 | `〔本地归档区〕` | **未核得（禁触区 · 本棒 0 读 0 写 0 列目录）** | **未核得** | **未核得** |
| SUB·面 | `deposon-sub` 全量 | 见 §4.2 逐件表 | 见 §4.2 | 见 §4.2 |

⚠ **v1.0 两件之登记值与现测值不一致**（并存登记，0 校正，⛔ 0 断言根因）→ 见 §8 漂移面 **D-1／D-2**。

### §3.2 addendum（**全枚举 ＋ 候选三组并出**）

#### §3.2.1 全枚举（凡件名含 `addendum` 者，逐件 SHA-12）

| # | 区 | 相对路径 | bytes | mtime | SHA-12 |
|---:|:--|:--|--:|:--|:--|
| 1 | REPO | `letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23_fix_addendum.md` | 6,067 | 2026-09-23 13:46:15 | `59b8df6e2e22` |
| 2 | REPO | `results/_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | 4,103 | 2026-09-24 18:47:18 | `172093a23e4b` |
| 3 | SUB | `results/_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md` | 23,152 | 2026-09-24 20:04:58 | `c64146c4ccac` |
| 4 | REPO | `results/_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json` | 6,132 | 2026-09-26 16:54:17 | `439721007aaf` |
| 5 | REPO | `results/_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json` | 7,566 | 2026-09-26 17:04:48 | `41d6c28ca87c` |
| 6 | REPO | `results/_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json` | 6,666 | 2026-09-26 17:22:21 | `99c58906f792` |
| 7 | REPO | `results/_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json` | 7,668 | 2026-09-26 17:27:21 | `c6d092f77932` |
| 8 | REPO | `results/_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json` | 10,257 | 2026-09-26 17:39:37 | `26f110a6e571` |
| 9 | REPO | `results/_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json` | 11,589 | 2026-09-26 18:10:28 | `6e104e2db038` |
| 10 | REPO | `results/_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json` | 14,722 | 2026-09-26 18:18:19 | `d96b747bfc6c` |
| 11 | REPO | `results/_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | 19,615 | 2026-09-26 18:30:47 | `401bd614cdf7` |
| 12 | SUB | `results/_v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md` | 37,212 | 2026-09-26 19:18:37 | `24c64cc23907` |
| 13 | SUB | `results/_v3_v4_achievements_inventory_3dir_addendum_v2p1_2026_09_26.md` | 17,130 | 2026-09-26 19:45:55 | `4c731a625868` |
| 14 | REPO | `results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json` | 20,194 | 2026-09-27 12:10:45 | `cbf60a630c9f` |
| 15 | REPO | `results/_v4_pi_cot_v3_dataset_addendum_d5_2026_09_27.json` | 16,587 | 2026-09-27 13:17:51 | `990c0c42a6f6` |
| 16 | REPO | `.tmp/_run_d4_relabel_addendum.py` | 17,550 | 2026-09-27 17:04:03 | `620eabf853af` |
| 17 | REPO | `results/_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json` | 18,714 | 2026-09-27 17:04:40 | `6eed9acdb99a` |
| 18 | REPO | `.tmp/_run_d6_addendum_2026_09_28.py` | 23,204 | 2026-09-28 13:46:23 | `e472ea36ed08` |
| 19 | REPO | `results/_v4_pi_cot_v3_dataset_addendum_d6_2026_09_28.json` | 19,214 | 2026-09-28 13:46:29 | `9669efa804b7` |
| 20 | REPO | `.tmp/_run_d6b_addendum_2026_09_28.py` | 31,468 | 2026-09-28 14:59:58 | `f0a4e919eeaa` |
| 21 | REPO | `results/_v4_pi_cot_v3_dataset_addendum_d6b_2026_09_28.json` | 27,009 | 2026-09-28 15:00:07 | `5d94a8617b5b` |
| 22 | REPO | `results/_v4_pi_cot_v3_dataset_addendum_s3_d7_2026_09_29.json` | 17,252 | 2026-09-29 10:57:48 | `c0ebbd1f4633` |
| 23 | SUB | `results/_v5_gt8f_m1_g1_fail_clause_addendum_2026_09_29.md` | 14,481 | 2026-09-29 14:05:11 | `31e5bd7b4003` |
| 24 | SUB | `results/_v5_gamma_end1_rb_clause_addendum_2026_09_29.md` | 10,397 | 2026-09-29 14:08:53 | `bf38e5f0161e` |
| 25 | REPO | `.tmp/_run_d8_addendum_2026_09_30.py` | 107,959 | 2026-09-30 16:17:55 | `7ce330b3e5ae` |
| 26 | REPO | `results/_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json` | 374,072 | 2026-09-30 16:18:01 | `769ef8b71462` |
| 27 | REPO | `.tmp/_verify_d8_addendum_2026_09_30.py` | 4,900 | 2026-09-30 16:18:13 | `28de8c99c054` |
| 28 | REPO | `.tmp/_run_d8_bhalf_addendum_2026_09_30.py` | 40,576 | 2026-09-30 16:21:44 | `90fa2c443529` |
| 29 | REPO | `results/_v4_pi_cot_v3_dataset_addendum_d8_bhalf_2026_09_30.json` | 58,581 | 2026-09-30 16:21:49 | `b02ef31f1e4e` |
| 30 | REPO | `results/_v4_pi_cot_v3_dataset_addendum_s3_d1fill_2026_10_01.json` | 46,909 | 2026-10-01 12:55:21 | `b9026cbf5ca2` |
| 31 | REPO | `letters/_commission_glm_dualtrack_paper_addendum_v0.2_2026_10_01.md` | 53,344 | 2026-10-01 21:19:36 | `758e1ef3de27` |
| 32 | REPO | `.tmp/_s4_topup_addendum_builder_2026_10_09.py` | 21,122 | 2026-10-09 13:53:01 | `b9987c7a8d5f` |
| 33 | REPO | `results/_s4_substrate_topup_addendum_2026_10_09.json` | 85,861 | 2026-10-09 13:53:09 | `1780542f0014` |
| 34 | REPO | `.tmp/_s4oq_addendum_struct_2026_10_09.py` | 843 | 2026-10-09 14:25:17 | `67652acdf681` |
| 35 | REPO | `.tmp/_s4oq_write_addendum_2026_10_09.py` | 11,886 | 2026-10-09 14:29:16 | `63e61afa6517` |
| 36 | REPO | `results/_s4_open_questions_addendum_2026_10_09.json` | 35,215 | 2026-10-09 14:29:17 | `4378dcc20624` |
| 37 | REPO | `.tmp/_s4oq_verify_addendum_2026_10_09.py` | 2,252 | 2026-10-09 14:29:27 | `419c15a7a2c5` |
| 38 | REPO | `.tmp/_rp_addendum_build_2026_10_09.py` | 30,375 | 2026-10-09 16:45:20 | `c4e8b75d656b` |
| 39 | REPO | `results/_r_pair_addendum_2026_10_09.json` | 110,510 | 2026-10-09 16:45:34 | `cebc2f6ef5ec` |

**合计 39 件**（MAIN 34 ＋ SUB 5）。

#### §3.2.2 「三 addendum」候选三组（⛔ **0 择一**，供 PI／parent 裁）

| 候选 | 构成 | 依据 | 本件状态 |
|:-:|:--|:--|:--|
| **候选-α** | v1.0 清单族之三件谱系（基件／3dir 件／erratum） | 09-24 谱系恰为三件 | ⚠ 与「＋erratum」**重复计**（erratum 即第三件）⇒ **自洽性存疑** |
| **候选-β** | **10-01→10-09 窗口内 3 件成果 addendum**：`_v4_pi_cot_v3_dataset_addendum_s3_d1fill_2026_10_01.json`／`_s4_substrate_topup_addendum_2026_10_09.json`／`_r_pair_addendum_2026_10_09.json` | 三者皆为该窗口之**成果性** addendum（数据集补样／S4 补样／R_pair） | 📌 **本件工作读法**；三件指纹见 §3.2.1 |
| **候选-γ** | dataset addendum 波之末三波（`d6b_09_28`／`s3_d7_09_29`／`d8_sq_09_30`） | 波次序列末三 | 指纹见 §3.2.1 |

**余歧义 A-2 处置**：⛔ **0 自裁**；本件以「**全枚举 39 件 ＋ 候选三组并出**」使歧义**不阻塞**交付 —— PI／parent 无论采何读法，所需逐件 SHA-12 **均已在 §3.2.1 在案**。

### §3.3 erratum

| 件 | 出件方 | SHA-12（实测） | bytes | mtime |
|:--|:--|:--|--:|:--|
| `results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md` | **doc-writer（agent-0032834a3e04 · 本棒同一出件方）** | `55cd332f66f2` | 10,288 | 2026-09-24 18:55:03 |

📌 本件即**该 erratum 之继任全量清单**，沿其「**勘误登记、不回改既有件正文行**」之成例（该件对 3dir 件为 0 字节改动）——本件亦对 v1.0 族三件 **0 字节改动**。

### §3.4 增量（10-01→**10-12**，顺延登记）

设计件原文为「10-01→**10-09** 全增量」；本件依 PI 2026-10-12「记得更新清单」令**顺延至 10-01→10-12**，其中 **10-10→10-12** 段独立成章（**§7**，**471 件**，逐件附 SHA-12）。10-01→10-09 段之增量件已并入 §4 逐件表（同一实测集，**0 重复计数**：§4 与 §7 为**同集之两种切面**，§7 为 §4 的子集视图）。

## §4 · 逐件表（相对路径 ／ SHA-12 ／ bytes ／ mtime ／ 类别）

**类别判据**：`成果面`（`results/`、`letters/`、`docs/`、`paper/`、`deposon_team/`、`reviews/`、`scripts/`、`tests/`、`tools/`、`verifier/`、`corpus/`、`attacks/`、`.trae/`、`.mavis/`、根散件、`tmp_movedout_*`）／`噪声面`（`.tmp/`，依 §2.3 仅汇总）

**排序**：区 → 目录 → 相对路径（小写稳定序，沿终态快照口径）。**SHA-12** ＝ SHA-256 前 12 位，**全部由本棒实测**。

### §4.0 汇总

| 区 | 路径 | 件数 | bytes | 末次 mtime |
|:--|:--|--:|--:|:--|
| REPO | `_repo_mirror` | **1,704** | **54,847,017** | 2026-10-12 03:18:02 |
| SUB | `_repo_mirror` | **1,187** | **58,731,756** | 2026-10-12 01:54:54 |
| **合计** | —— | **2,891** | **113,578,773** | —— |

### §4.1 区 `_repo_mirror`（1,704 件 ／ 54,847,017 bytes）

**逐目录分布**

| 目录 | 件数 | bytes | 类别 |
|:--|--:|--:|:--|
| `.mavis/scripts/kt_a1/` | 2 | 19 | 成果面 |
| `.mavis/scripts/kt_b1/` | 1 | 966 | 成果面 |
| `.mavis/scripts/kt_c1/` | 1 | 7 | 成果面 |
| `.tmp/` | 441 | 11,375,518 | 噪声面（仅汇总） |
| `.trae/scripts/` | 2 | 34,781 | 成果面 |
| `attacks/` | 4 | 12,922 | 成果面 |
| `corpus/v20/` | 28 | 166,342 | 成果面 |
| `corpus/v20/by_model/GLM_1/` | 1 | 19,685 | 成果面 |
| `corpus/v20/by_model/GLM_2/` | 1 | 13,150 | 成果面 |
| `corpus/v20/by_model/coze/` | 1 | 10,978 | 成果面 |
| `corpus/v20/by_model/kimi/` | 1 | 24,150 | 成果面 |
| `corpus/v20/by_model/minimax/` | 1 | 25,347 | 成果面 |
| `corpus/v20_caption_surface/` | 10 | 691,723 | 成果面 |
| `deposon_team/plugins/` | 83 | 1,229,354 | 成果面 |
| `docs/` | 52 | 395,656 | 成果面 |
| `docs/V3X/` | 80 | 1,965,288 | 成果面 |
| `docs/reviews/` | 3 | 22,570 | 成果面 |
| `letters/` | 98 | 2,683,139 | 成果面 |
| `paper/` | 3 | 124,497 | 成果面 |
| `paper/v2/` | 2 | 20,590 | 成果面 |
| `results/` | 583 | 32,356,113 | 成果面 |
| `results/_archive_2026-10-12/pycache_sink/deposon_team_plugins_pycache/` | 3 | 216,752 | 成果面 |
| `results/_archive_2026-10-12/pycache_sink/results_pycache/` | 5 | 312,650 | 成果面 |
| `results/_archive_2026-10-12/superseded_variants/` | 1 | 5,088 | 成果面 |
| `results/_archive_2026_09_24/` | 7 | 136,395 | 成果面 |
| `results/_p_i_real_labels_2026_09_16/` | 1 | 1,043 | 成果面 |
| `results/_p_j_convergence_basin_2026_09_16/` | 1 | 1,669 | 成果面 |
| `results/_p_l_p_c_finite_size_scaling_2026_09_16/` | 1 | 9,076 | 成果面 |
| `results/_p_l_real_data_collapse_2026_09_16/` | 1 | 3,761 | 成果面 |
| `results/_p_m_attack_surface_cost_2026_09_16/` | 1 | 5,266 | 成果面 |
| `results/_p_m_real_separation_2026_09_16/` | 1 | 2,042 | 成果面 |
| `results/_p_n_curvature_potential_coupling_2026_09_16/` | 1 | 4,276 | 成果面 |
| `results/_p_o_stranger_verification_2026_09_16/` | 1 | 5,916 | 成果面 |
| `results/_v3_recheck_08b_executor/` | 3 | 150,454 | 成果面 |
| `results/_v3_recheck_08c_preexp_data/` | 4 | 202,840 | 成果面 |
| `results/_v3_s1_executor/` | 3 | 97,165 | 成果面 |
| `results/_v3_s2_executor/` | 3 | 161,183 | 成果面 |
| `results/_v3_s3_wordexpand_data/` | 5 | 159,875 | 成果面 |
| `results/_v3_s_phrasetemplate_preexp_data/` | 3 | 89,973 | 成果面 |
| `results/_v3x_18frozen_remeasure_2026_09_16/` | 1 | 4,202 | 成果面 |
| `results/_v3x_experiments_2026_09_16/` | 1 | 17,053 | 成果面 |
| `results/_v3x_p_k_verify_2026_09_16/` | 1 | 2,059 | 成果面 |
| `reviews/` | 17 | 301,475 | 成果面 |
| `reviews/data/` | 15 | 74,769 | 成果面 |
| `scripts/` | 10 | 148,821 | 成果面 |
| `tests/` | 23 | 212,514 | 成果面 |
| `tools/` | 5 | 61,516 | 成果面 |
| `verifier/` | 7 | 49,087 | 成果面 |
| `verifier/audit/` | 1 | 22,105 | 成果面 |
| `verifier/handoff/` | 5 | 39,225 | 成果面 |
| `verifier/kill_lines/` | 1 | 2,781 | 成果面 |
| `verifier/runs/` | 57 | 31,474 | 成果面 |
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
| `(root)/` | 72 | 1,020,964 | 成果面 |
| **小计** | **1,704** | **54,847,017** | —— |

#### §4.1.1 `.tmp/` 噪声面（**依 §2.3 惯例：仅汇总，0 逐件展开**）

| 项 | 件数 | bytes |
|:--|--:|--:|
| `.tmp/` 全量 | **441** | **11,375,518** |
| 其中 10-10→10-12 增量窗内 | 84 | 6,905,446 |

📌 该面之**逐件 SHA-12** 见 §7（增量窗成员）；**10-10 之前之 `.tmp` 件依惯例不逐件展开**，如需全展开须另立件（⛔ 本棒不越权）。

#### §4.1.2 逐件（1,263 件）

| # | 相对路径 | bytes | mtime | SHA-12 |
|---:|:--|--:|:--|:--|
| 1 | `.gitignore` | 91 | 2026-08-22 21:07:01 | `7d8d71ea2af2` |
| 2 | `.mavis/scripts/kt_a1/test_persist.txt` | 15 | 2026-09-24 22:30:25 | `2898abb5082b` |
| 3 | `.mavis/scripts/kt_a1/test_write.txt` | 4 | 2026-09-24 22:27:23 | `9f86d081884c` |
| 4 | `.mavis/scripts/kt_b1/fix_safe_float.py` | 966 | 2026-09-24 22:23:52 | `4420543e60a4` |
| 5 | `.mavis/scripts/kt_c1/test_write.txt` | 7 | 2026-09-24 22:29:06 | `85d443e165bb` |
| 6 | `.trae/scripts/_arxiv_renumber.py` | 16,531 | 2026-09-09 14:14:27 | `f488ad141ef9` |
| 7 | `.trae/scripts/_verify_tex.py` | 18,250 | 2026-09-09 14:14:27 | `3b977bb8a715` |
| 8 | `_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` | 26,633 | 2026-09-26 19:13:56 | `739245682d40` |
| 9 | `_v5_gt_exec_2026_09_29.py` | 75,689 | 2026-09-29 11:17:03 | `eef7b446cc0e` |
| 10 | `attacks/__init__.py` | 183 | 2026-09-01 11:19:18 | `d11e085d9ecc` |
| 11 | `attacks/a1_delete_anchor.py` | 4,693 | 2026-09-04 13:11:07 | `78ac391d16fc` |
| 12 | `attacks/a2_reshuffle_manifest.py` | 3,792 | 2026-09-01 11:19:34 | `3d54b277620e` |
| 13 | `attacks/a3_rewrite_runs.py` | 4,254 | 2026-09-01 16:31:25 | `f02b3eee8d6e` |
| 14 | `audits_dataset_health.json` | 7,398 | 2026-08-28 15:53:27 | `4f827071b0b8` |
| 15 | `audits_outliers.json` | 132,875 | 2026-08-28 15:53:28 | `3b1c881c4594` |
| 16 | `audits_security.json` | 1,610 | 2026-08-28 15:52:30 | `553c90aa3ba6` |
| 17 | `corpus/v20/all.json` | 2,557 | 2026-09-17 10:24:31 | `8df31c95b1fc` |
| 18 | `corpus/v20/by_model/coze/coze_artifact_v_2026_09_16.json` | 10,978 | 2026-09-24 11:28:03 | `fee04170aa73` |
| 19 | `corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json` | 19,685 | 1979-11-30 00:00:00 | `268ab1239a8a` |
| 20 | `corpus/v20/by_model/GLM_2/glm_artifact_v_2026_09_16.json` | 13,150 | 1979-11-30 00:00:00 | `39732a92b5c9` |
| 21 | `corpus/v20/by_model/kimi/index_v2_2026_09_16.json` | 24,150 | 2026-09-16 18:39:54 | `efe05ad775de` |
| 22 | `corpus/v20/by_model/minimax/artifact_v_2026_09_16.json` | 25,347 | 2026-09-16 18:20:56 | `9e1ccbdceacc` |
| 23 | `corpus/v20/index.json` | 7,335 | 2026-08-28 23:53:05 | `8423ffe266af` |
| 24 | `corpus/v20/index_v2_2026_09_16.json` | 24,150 | 2026-09-16 18:39:54 | `efe05ad775de` |
| 25 | `corpus/v20/index_v3_2026_09_29.json` | 24,421 | 2026-10-01 09:43:44 | `3ba2449cf986` |
| 26 | `corpus/v20/index_v3_2026_10_09.json` | 24,837 | 2026-10-09 13:39:49 | `74b27393574f` |
| 27 | `corpus/v20/L_algorithm_process.json` | 3,920 | 2026-08-28 17:38:45 | `ff0ef9131fdd` |
| 28 | `corpus/v20/L_biological_taxonomy.json` | 3,562 | 2026-08-28 17:38:45 | `0c7ad5235ae9` |
| 29 | `corpus/v20/L_geography_world.json` | 3,699 | 2026-08-28 23:11:44 | `77b0c1466dc0` |
| 30 | `corpus/v20/L_historical_causality.json` | 4,329 | 2026-08-28 17:38:45 | `12e0de4bb103` |
| 31 | `corpus/v20/L_physics_concepts.json` | 3,397 | 2026-08-28 17:38:45 | `d8780859d310` |
| 32 | `corpus/v20/L_project_management.json` | 3,898 | 2026-08-28 23:12:37 | `32ca32c00da4` |
| 33 | `corpus/v20/S1.json` | 1,512 | 2026-08-28 17:07:51 | `a890c56f7705` |
| 34 | `corpus/v20/S1_n35.json` | 2,521 | 2026-08-28 17:07:52 | `f035043bfddd` |
| 35 | `corpus/v20/S1_n45.json` | 3,171 | 2026-08-28 17:07:52 | `52b4d6e52ae9` |
| 36 | `corpus/v20/S1_n60.json` | 4,122 | 2026-08-28 17:07:52 | `584de37ebec1` |
| 37 | `corpus/v20/S2.json` | 2,234 | 2026-08-28 17:07:52 | `b1f6c5aa4de6` |
| 38 | `corpus/v20/S2_n20.json` | 1,537 | 2026-08-28 17:07:52 | `bfc9d38c8c0f` |
| 39 | `corpus/v20/S2_n35.json` | 2,480 | 2026-08-28 17:07:52 | `e20a1bbeaee7` |
| 40 | `corpus/v20/S2_n45.json` | 3,175 | 2026-08-28 17:07:52 | `58bb0a7d2e46` |
| 41 | `corpus/v20/S2_n60.json` | 4,123 | 2026-08-28 17:07:52 | `01c492a97b98` |
| 42 | `corpus/v20/S3.json` | 2,297 | 2026-08-28 17:07:52 | `3b6879ab2440` |
| 43 | `corpus/v20/S4.json` | 4,932 | 2026-08-28 17:07:52 | `e6045f0920ec` |
| 44 | `corpus/v20/S5.json` | 3,319 | 2026-08-28 17:07:52 | `4b10f9cae09f` |
| 45 | `corpus/v20/S6.json` | 3,320 | 2026-08-28 17:07:52 | `01d9c95ea690` |
| 46 | `corpus/v20/S6_n20.json` | 1,724 | 2026-08-28 17:07:52 | `4a0689892c1b` |
| 47 | `corpus/v20/S6_n35.json` | 2,676 | 2026-08-28 17:07:52 | `8d02fbadd277` |
| 48 | `corpus/v20/S6_n60.json` | 4,296 | 2026-08-28 17:07:52 | `704e2fd0d021` |
| 49 | `corpus/v20/strip_captions_22.json` | 12,798 | 2026-09-11 11:33:40 | `6a2656878745` |
| 50 | `corpus/v20_caption_surface/_adendum_I_po_captions_closure_20260917_132049.json` | 4,429 | 2026-09-17 13:20:50 | `18165008bef6` |
| 51 | `corpus/v20_caption_surface/_inspect_captions.py` | 591 | 2026-09-10 17:31:00 | `dfb02ade1474` |
| 52 | `corpus/v20_caption_surface/_p_d_b3_merkle_22caption_runner_2026_09_16.py` | 18,596 | 2026-09-16 18:54:48 | `d2cd7acb29a1` |
| 53 | `corpus/v20_caption_surface/_p_d_v03_22caption_verification_20260917_163757.json` | 13,775 | 2026-09-17 16:37:57 | `dfbcc5d6fc34` |
| 54 | `corpus/v20_caption_surface/_v41_flash_rag_caption_embs.bak.json` | 612,511 | 2026-09-10 17:05:53 | `25f745609658` |
| 55 | `corpus/v20_caption_surface/caption_distance_mat_22.json` | 8,552 | 2026-09-23 16:44:30 | `1c4fff004cc4` |
| 56 | `corpus/v20_caption_surface/caption_features_22.json` | 18,362 | 2026-09-23 16:44:30 | `727a253566dd` |
| 57 | `corpus/v20_caption_surface/caption_stats_22.json` | 632 | 2026-09-23 16:44:30 | `da34f54d4f5b` |
| 58 | `corpus/v20_caption_surface/manifest.json` | 1,477 | 2026-09-23 16:44:30 | `4fdda6480bb5` |
| 59 | `corpus/v20_caption_surface/strip_captions_22.json` | 12,798 | 2026-09-11 11:33:40 | `6a2656878745` |
| 60 | `deposon_agents.py` | 104,622 | 2026-09-18 13:41:44 | `5496954b0ad5` |
| 61 | `deposon_agents_v1_3.py` | 1,827 | 2026-08-30 10:23:11 | `715026b48678` |
| 62 | `deposon_agents_v1_4.py` | 1,726 | 2026-08-30 10:23:11 | `59f0ce83e06d` |
| 63 | `deposon_diffusion.py` | 19,171 | 2026-08-30 04:52:41 | `fe4d668eb1da` |
| 64 | `deposon_fast.py` | 4,581 | 2026-08-30 04:53:24 | `7a2dcbadac73` |
| 65 | `deposon_g2_modes.py` | 6,316 | 2026-08-23 09:33:59 | `6a175a264b46` |
| 66 | `deposon_photonics.py` | 10,402 | 2026-08-29 00:34:47 | `c7e78ad9f030` |
| 67 | `deposon_protocol.py` | 2,845 | 2026-08-30 04:55:56 | `ca756668ce2e` |
| 68 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_fix_2026_10_10.py` | 33,994 | 2026-10-10 11:23:01 | `341b6726ac4e` |
| 69 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_rename_2026_10_10.py` | 35,321 | 2026-10-10 11:23:01 | `cd43c41716f0` |
| 70 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_selfverify_fix_2026_10_10.py` | 31,457 | 2026-10-10 10:50:15 | `041525fd05a2` |
| 71 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py` | 20,322 | 2026-09-29 13:43:09 | `de16bc002198` |
| 72 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py` | 21,826 | 2026-10-09 13:38:37 | `7c095c54fb99` |
| 73 | `deposon_team/plugins/_pg_v01_compute.py` | 20,923 | 2026-09-16 18:54:48 | `d511c545f88e` |
| 74 | `deposon_team/plugins/_tdf_s1_2026_10_12.py` | 5,856 | 2026-10-12 01:23:22 | `5f9ab0ad7bab` |
| 75 | `deposon_team/plugins/_tdf_s1b_2026_10_12.py` | 8,064 | 2026-10-12 01:24:29 | `bebba19790c0` |
| 76 | `deposon_team/plugins/_tdf_s1c_2026_10_12.py` | 7,485 | 2026-10-12 01:26:27 | `d8bd9c41194a` |
| 77 | `deposon_team/plugins/_tdf_s2_apply_2026_10_12.py` | 10,899 | 2026-10-12 01:29:57 | `4bd6d16e20d7` |
| 78 | `deposon_team/plugins/_tdf_s3_jumps_2026_10_12.py` | 676 | 2026-10-12 01:30:39 | `16f7e10ac78f` |
| 79 | `deposon_team/plugins/_tdf_s3b_2026_10_12.py` | 1,229 | 2026-10-12 01:31:26 | `ccec66bb426e` |
| 80 | `deposon_team/plugins/_tdf_s4_final_2026_10_12.py` | 2,695 | 2026-10-12 01:34:23 | `1df9a5d22e42` |
| 81 | `deposon_team/plugins/_v3_construct_diag_2026_09_23.py` | 22,490 | 2026-09-23 14:20:25 | `ce10a3dbcb2b` |
| 82 | `deposon_team/plugins/_v3_review_r1_inventory_2026_09_23.py` | 5,526 | 2026-09-23 13:13:02 | `7b97ef02c52e` |
| 83 | `deposon_team/plugins/_v3_review_r1b_2026_09_23.py` | 1,795 | 2026-09-23 13:13:45 | `b5e77e114d88` |
| 84 | `deposon_team/plugins/_v3_review_r1c_2026_09_23.py` | 2,919 | 2026-09-23 13:14:27 | `fdfeb03e8d6f` |
| 85 | `deposon_team/plugins/_v3_review_r1d_2026_09_23.py` | 1,712 | 2026-09-23 13:14:59 | `4adbd9b5eab5` |
| 86 | `deposon_team/plugins/_v3_review_r2_verify_2026_09_23.py` | 4,528 | 2026-09-23 13:24:40 | `aee06c009ed1` |
| 87 | `deposon_team/plugins/_v3_review_r2b_2026_09_23.py` | 3,189 | 2026-09-23 13:25:02 | `9d6343bd9755` |
| 88 | `deposon_team/plugins/_v3_review_r2c_2026_09_23.py` | 4,400 | 2026-09-23 13:25:39 | `1c30cda5aad6` |
| 89 | `deposon_team/plugins/_v3_review_r3_sha_2026_09_23.py` | 1,881 | 2026-09-23 13:26:41 | `d3b45b64c0da` |
| 90 | `deposon_team/plugins/_v3_review_r4_fixscan_2026_09_23.py` | 3,896 | 2026-09-23 13:31:36 | `917b18eb9a5f` |
| 91 | `deposon_team/plugins/_v3_review_r5_anchor_probe_2026_09_23.py` | 2,653 | 2026-09-23 13:33:00 | `7ebe0f65a64a` |
| 92 | `deposon_team/plugins/_v3_review_r6_final_sha_2026_09_23.py` | 2,135 | 2026-09-23 13:34:47 | `8af3f4460144` |
| 93 | `deposon_team/plugins/_v3_review_r7_fix_e15_2026_09_23.py` | 2,951 | 2026-09-23 13:39:17 | `40d66379ef17` |
| 94 | `deposon_team/plugins/_v3_review_r8_precise_scan_2026_09_23.py` | 5,241 | 2026-09-23 13:44:30 | `2ff60f715def` |
| 95 | `deposon_team/plugins/_v3_review_r9_final_state_2026_09_23.py` | 2,117 | 2026-09-23 13:46:51 | `fcf5baf4dd7f` |
| 96 | `deposon_team/plugins/_v3n_cpath_live_2026_09_27.py` | 19,823 | 2026-09-27 14:16:12 | `5248ba7ac21c` |
| 97 | `deposon_team/plugins/_v3n_cpath_live_r1_2026_09_27.py` | 28,187 | 2026-09-27 20:54:38 | `321d39c7df41` |
| 98 | `deposon_team/plugins/_v3n_cpath_live_rerun_2026_10_01.py` | 22,133 | 2026-10-01 14:02:02 | `7d8d26174ce9` |
| 99 | `deposon_team/plugins/_v3n_ktb1_distortion_bound_2026_09_27.py` | 13,055 | 2026-09-27 14:16:59 | `5572ef4055a5` |
| 100 | `deposon_team/plugins/_v3n_pg_boss_live_2026_09_27.py` | 14,223 | 2026-09-27 14:15:38 | `b6040d34f0ac` |
| 101 | `deposon_team/plugins/_v3r1p1_21_ktb1_distortion_2026_09_27.py` | 30,672 | 2026-09-27 16:35:23 | `f7b61f041c0b` |
| 102 | `deposon_team/plugins/_v3r1p1_35_gt2b_bankseed_2026_09_27.py` | 26,734 | 2026-09-27 16:23:05 | `62353279cd0c` |
| 103 | `deposon_team/plugins/_v3x_frozen_schema_v1.json` | 12,919 | 2026-09-17 10:27:19 | `9e99dcc4d920` |
| 104 | `deposon_team/plugins/_v4_contrast_nondegenerate_2026_09_23.py` | 42,876 | 2026-09-23 16:06:11 | `a0bfc7df887f` |
| 105 | `deposon_team/plugins/_v4_wide_s1_inventory_2026_09_27.py` | 1,669 | 2026-09-27 20:18:35 | `145ae518f5f0` |
| 106 | `deposon_team/plugins/_v4_wide_s5_prescan_2026_09_27.py` | 2,839 | 2026-09-27 20:25:46 | `724964301582` |
| 107 | `deposon_team/plugins/_v4_wt_apply_b4_2026_09_27.py` | 6,113 | 2026-09-27 20:10:30 | `fd0a08029841` |
| 108 | `deposon_team/plugins/_v4_wt_s0_verify_2026_09_27.py` | 8,462 | 2026-09-27 20:02:03 | `4dcb81343577` |
| 109 | `deposon_team/plugins/_v4_wt_s2_b1diff_2026_09_27.py` | 2,015 | 2026-09-27 20:02:28 | `b61cb447f306` |
| 110 | `deposon_team/plugins/_v4_wt_s2_b1recheck_2026_09_27.py` | 5,650 | 2026-09-27 20:03:23 | `e643ac7f9718` |
| 111 | `deposon_team/plugins/_v4_wt_s3_b2probe_2026_09_27.py` | 6,089 | 2026-09-27 20:08:43 | `a5db027adac5` |
| 112 | `deposon_team/plugins/_v4_wt_s3b_b2confirm_2026_09_27.py` | 3,604 | 2026-09-27 20:09:01 | `7aaf6f21d459` |
| 113 | `deposon_team/plugins/_v4_wt_s4_b4verify_2026_09_27.py` | 2,595 | 2026-09-27 20:09:38 | `5e1ec533de1f` |
| 114 | `deposon_team/plugins/_v4_wt_s4b_b4recompute_2026_09_27.py` | 4,174 | 2026-09-27 20:09:59 | `edcdfda20f91` |
| 115 | `deposon_team/plugins/_v4_wt_s4c_regonly_2026_09_27.py` | 3,900 | 2026-09-27 20:10:57 | `20f265761280` |
| 116 | `deposon_team/plugins/_v4_wt_s6_final_2026_09_27.py` | 3,435 | 2026-09-27 20:13:00 | `653077d03468` |
| 117 | `deposon_team/plugins/_v5_gt8_lowarm_2026_09_29.py` | 57,033 | 2026-09-29 15:28:35 | `9b21988afff7` |
| 118 | `deposon_team/plugins/_v5_gt8_lowarm_setA_2026_09_29.py` | 43,224 | 2026-09-29 15:27:05 | `f72f062f6b67` |
| 119 | `deposon_team/plugins/_v5_gt8_lowarm_seta_verify_2026_09_29.py` | 15,553 | 2026-09-29 15:33:15 | `bed2d444c196` |
| 120 | `deposon_team/plugins/_v5_item21_strategyqa_realias_2026_09_29.py` | 25,482 | 2026-09-29 16:15:43 | `aaaae1f02815` |
| 121 | `deposon_team/plugins/_v5_item35_v2_matrix_2026_09_29.py` | 44,777 | 2026-09-29 12:23:55 | `ef73f9b90afc` |
| 122 | `deposon_team/plugins/_v5_item35_v3_collinear_2026_09_29.py` | 63,376 | 2026-09-29 14:21:40 | `7115928822a1` |
| 123 | `deposon_team/plugins/_v5_pp1_pattern_fix_2026_09_29.py` | 22,544 | 2026-09-29 17:31:40 | `e3cf9d552f30` |
| 124 | `deposon_team/plugins/_v5_wa_s2_2026_09_30.py` | 5,812 | 2026-09-30 19:03:02 | `88cd82e65627` |
| 125 | `deposon_team/plugins/_v5_wa_s4_2026_09_30.py` | 2,063 | 2026-09-30 19:07:54 | `2e7743dd8139` |
| 126 | `deposon_team/plugins/_v5r_s40_rerun_executor_fix_2026_09_29.py` | 17,665 | 2026-09-29 19:19:06 | `a4ae5d5f19c8` |
| 127 | `deposon_team/plugins/_verify_15frozen.py` | 3,905 | 2026-09-17 10:12:02 | `efae9274962e` |
| 128 | `deposon_team/plugins/_verify_15frozen_v1.py` | 2,094 | 2026-09-17 10:27:53 | `60523e406055` |
| 129 | `deposon_team/plugins/_verify_batch5_2026_09_18.py` | 4,238 | 2026-09-18 13:45:30 | `bc6cbf27a338` |
| 130 | `deposon_team/plugins/_verify_pg_v0.py` | 3,978 | 2026-09-17 10:12:02 | `cdd3415ad993` |
| 131 | `deposon_team/plugins/_verify_pg_v0_v1.py` | 2,521 | 2026-09-17 10:27:53 | `67088ae1a860` |
| 132 | `deposon_team/plugins/boss_pa_1_rbr_rm.py` | 17,743 | 2026-09-15 15:16:26 | `5cc594147e00` |
| 133 | `deposon_team/plugins/boss_pa_1_rbr_rm_v3df_ab_alpha_2026_10_09.py` | 45,777 | 2026-10-09 22:54:53 | `06016f90fd3a` |
| 134 | `deposon_team/plugins/boss_pa_1_rbr_rm_v3df_ab_beta_2026_10_09.py` | 47,580 | 2026-10-09 22:59:41 | `3524e454d8ed` |
| 135 | `deposon_team/plugins/boss_pa_1_rbr_rm_v3df_c1c4_2026_09_29.py` | 61,102 | 2026-09-29 12:05:45 | `7761f2c339e6` |
| 136 | `deposon_team/plugins/boss_pa_1_rbr_rm_v3df_p1_reopen_2026_09_29.py` | 91,135 | 2026-09-29 13:40:58 | `77724bce0c06` |
| 137 | `deposon_team/plugins/boss_pa_2_potential_game.py` | 10,410 | 2026-09-15 15:16:26 | `33dfb4338c53` |
| 138 | `deposon_team/plugins/boss_pa_3_replicator_dynamics.py` | 12,900 | 2026-09-15 15:16:26 | `a2bd9dd24c25` |
| 139 | `deposon_team/plugins/boss_pc_1_2d_ising_universality.py` | 7,547 | 2026-09-15 15:37:54 | `bfc319808447` |
| 140 | `deposon_team/plugins/boss_pc_2_transverse_field_ising.py` | 7,053 | 2026-09-15 15:37:54 | `210105a7f29a` |
| 141 | `deposon_team/plugins/boss_pc_3_reservoir_computing.py` | 7,373 | 2026-09-15 15:37:54 | `021ea39b7193` |
| 142 | `deposon_team/plugins/boss_pg_1_riemannian_degenerate.py` | 5,996 | 2026-09-15 15:37:53 | `97fede6c8a4e` |
| 143 | `deposon_team/plugins/boss_pg_2_hyperbolic_classification_collapse.py` | 5,285 | 2026-09-15 15:37:53 | `f006d4caca94` |
| 144 | `deposon_team/plugins/boss_pg_3_geodesic_violation.py` | 5,517 | 2026-09-15 15:37:54 | `09f37c01a258` |
| 145 | `deposon_team/plugins/github_dir_structure_2026_09_18.md` | 11,675 | 2026-09-15 15:17:42 | `0fd07ad38282` |
| 146 | `deposon_team/plugins/github_upload_2026_09_18.sh` | 6,030 | 2026-09-15 15:18:06 | `52bc19845b2b` |
| 147 | `deposon_team/plugins/skill_a_p_a_60cells.py` | 9,078 | 2026-09-11 17:05:38 | `b1463bb24403` |
| 148 | `deposon_team/plugins/skill_b_p_c_alpha_beta.py` | 8,699 | 2026-09-11 17:05:38 | `e5a299f69a22` |
| 149 | `deposon_team/plugins/skill_c_p_e_3modality.py` | 8,915 | 2026-09-11 17:05:38 | `e19e76c5da7e` |
| 150 | `deposon_team/plugins/skill_d_p_f_observer.py` | 15,927 | 2026-09-15 13:30:57 | `3e369a1f6171` |
| 151 | `docs/ADVISOR_BRIEFING_2026-08-30.md` | 5,890 | 2026-08-29 10:16:17 | `40278bc425e6` |
| 152 | `docs/ARCH_AUDIT_v2.md` | 14,698 | 2026-08-30 04:39:28 | `5bee4c6cf47c` |
| 153 | `docs/BASELINE_REGISTRY.md` | 3,356 | 2026-08-28 20:59:38 | `51b271548835` |
| 154 | `docs/CLOSURE_v19_and_v2X_gametheory.md` | 9,065 | 2026-08-28 15:55:51 | `84323775a212` |
| 155 | `docs/DATASET_HEALTH_v2.md` | 4,892 | 2026-08-30 04:40:23 | `c87a0c1f5af6` |
| 156 | `docs/Deposon_Requirements_v1.md` | 13,914 | 2026-08-22 21:07:01 | `ee33f3f22e1b` |
| 157 | `docs/Deposon_v1_3_验证报告.md` | 8,003 | 2026-08-22 21:07:01 | `dc5be727f920` |
| 158 | `docs/Deposon_v1_4_验证报告.md` | 4,254 | 2026-08-22 21:11:43 | `3bcccf03f7ca` |
| 159 | `docs/FIGURES_v2.md` | 5,851 | 2026-08-30 11:15:47 | `1cd4a4cb0a76` |
| 160 | `docs/Findings_GT2B.md` | 3,322 | 2026-08-29 20:00:21 | `e6cc74f9917d` |
| 161 | `docs/Findings_GT3.md` | 2,632 | 2026-08-29 15:06:30 | `4f3242b2a661` |
| 162 | `docs/Findings_GT8.md` | 3,890 | 2026-08-29 19:36:27 | `869c0071fbc2` |
| 163 | `docs/Findings_GT8B.md` | 9,809 | 2026-08-30 10:38:41 | `956183753a2e` |
| 164 | `docs/Findings_GT_FORMAL.md` | 6,345 | 2026-08-30 15:45:12 | `fab607f0e180` |
| 165 | `docs/Findings_v2.0.md` | 4,364 | 2026-08-28 17:44:22 | `7e5dc4b045d8` |
| 166 | `docs/Findings_v2.0_bigquiz.md` | 3,291 | 2026-08-28 23:55:23 | `d4ed18152dc0` |
| 167 | `docs/Findings_v2.0_boss.md` | 3,642 | 2026-08-28 21:16:05 | `36c714eabe3b` |
| 168 | `docs/Findings_v2.0_corrections.md` | 5,012 | 2026-08-29 01:23:08 | `5864bbe5adae` |
| 169 | `docs/Findings_v2.0_crossval.md` | 4,566 | 2026-08-28 20:28:59 | `32d26cb09568` |
| 170 | `docs/Findings_v2.0_hardening.md` | 3,563 | 2026-08-28 22:49:38 | `a7f479793f01` |
| 171 | `docs/Findings_v2.0_photonics.md` | 4,377 | 2026-08-30 04:46:02 | `9158f54ec248` |
| 172 | `docs/Findings_v2.0_skills.md` | 3,456 | 2026-08-28 20:47:31 | `43731392b581` |
| 173 | `docs/GT_FORMALIZATION_v1.md` | 19,100 | 2026-08-30 15:45:39 | `aeefb8ef6972` |
| 174 | `docs/GT_RECONSTRUCTION.md` | 13,424 | 2026-09-28 22:57:17 | `cff15d000d47` |
| 175 | `docs/LESSONS_INDEX.md` | 4,682 | 2026-08-29 10:11:09 | `7e3674a80cb7` |
| 176 | `docs/LESSONS_v19.md` | 5,290 | 2026-08-28 17:56:50 | `dbbcf8e5e89d` |
| 177 | `docs/LESSONS_v20_deepprobe.md` | 8,409 | 2026-08-29 10:06:48 | `5c898d4407ee` |
| 178 | `docs/MODEL_ARGUMENTATION_v2.md` | 30,142 | 2026-08-30 10:42:40 | `2c83c42804e4` |
| 179 | `docs/PAPER_BRIEF.md` | 11,296 | 2026-08-30 11:09:37 | `de450c0beffa` |
| 180 | `docs/PROGRESS_REPORT_LAYMAN.md` | 8,472 | 2026-08-29 15:08:52 | `25546ffdc56b` |
| 181 | `docs/REF_VERIFICATION_v2.md` | 5,860 | 2026-08-30 11:17:21 | `64f0a3772c12` |
| 182 | `docs/REFACTOR_v2.md` | 23,042 | 2026-08-30 10:39:00 | `03c8baa18d93` |
| 183 | `docs/reviews/review_gtformal_integration_v2X.md` | 8,582 | 2026-08-30 16:58:11 | `325c9d87787b` |
| 184 | `docs/reviews/review_salvage_integration_v2X.md` | 6,212 | 2026-08-30 05:06:19 | `96ae50306f36` |
| 185 | `docs/reviews/review_sprint_v2X.md` | 7,776 | 2026-08-30 11:11:11 | `4356cd02562e` |
| 186 | `docs/Roadmap_v2X.md` | 6,467 | 2026-08-24 11:13:19 | `a6aaf3200611` |
| 187 | `docs/SALVAGE_v2.md` | 7,312 | 2026-08-30 04:41:52 | `f28a81d6302d` |
| 188 | `docs/SECURITY_AUDIT_v2.md` | 4,707 | 2026-08-30 04:39:49 | `317fb508940a` |
| 189 | `docs/simple_baseline_failure_analysis.md` | 6,080 | 2026-08-23 00:01:28 | `968776002868` |
| 190 | `docs/space_release_log.json` | 5,056 | 2026-08-28 23:54:50 | `110607514753` |
| 191 | `docs/SPEC_GT2B.md` | 3,318 | 2026-08-29 19:56:29 | `68a5b08ef007` |
| 192 | `docs/SPEC_GT2C.md` | 3,172 | 2026-08-30 18:32:55 | `29af533486b2` |
| 193 | `docs/SPEC_GT3.md` | 5,369 | 2026-08-29 14:09:52 | `432ec337d586` |
| 194 | `docs/SPEC_GT5C.md` | 3,046 | 2026-08-30 18:33:30 | `1e41b4334735` |
| 195 | `docs/SPEC_GT8.md` | 4,181 | 2026-08-29 19:40:49 | `edf6f4465ead` |
| 196 | `docs/SPEC_GT8B.md` | 7,486 | 2026-08-30 10:37:50 | `3545c01e1291` |
| 197 | `docs/SPEC_GT8C.md` | 6,326 | 2026-08-30 15:50:15 | `6b09de9911c0` |
| 198 | `docs/SPEC_v1.5.md` | 6,204 | 2026-08-23 19:22:13 | `c165a86cf551` |
| 199 | `docs/SPEC_v1.8.md` | 9,850 | 2026-08-23 23:19:47 | `ad0e445714d9` |
| 200 | `docs/SPEC_v2.0.md` | 5,333 | 2026-08-28 16:54:47 | `bac61d51fd20` |
| 201 | `docs/SPEC_v2.0_amendment1.md` | 4,743 | 2026-08-29 01:22:16 | `3e3a5014cb0e` |
| 202 | `docs/SYNTHESIS_mind_game.md` | 9,191 | 2026-08-29 00:22:08 | `0f36aaeeda6f` |
| 203 | `docs/THINKING_V3_GT_CONTRIB_2026.md` | 19,508 | 2026-08-30 20:45:01 | `8c1d733f9182` |
| 204 | `docs/V3X/AGENT_TEAM_OPT_V2_2026_09_11.md` | 11,835 | 2026-09-11 16:30:03 | `bbd074b76526` |
| 205 | `docs/V3X/BOSS_B123_BUGFIX_2026_09_09.md` | 5,615 | 2026-09-09 14:50:57 | `9352a1675b10` |
| 206 | `docs/V3X/BOSS_F_GHOST_PATH_NOTE_2026_09_11.md` | 4,840 | 2026-09-11 13:16:07 | `354a1360234f` |
| 207 | `docs/V3X/BOSS_PE_3_RESERVOIR_VERIFY_REPORT_2026_09_15.md` | 11,079 | 2026-09-15 13:36:08 | `c28f7f0b530f` |
| 208 | `docs/V3X/BOSS_SELFTEST_PHASE_B_2026_09_09.md` | 15,478 | 2026-09-09 14:18:07 | `4485443757e7` |
| 209 | `docs/V3X/BOSS_URL_2026_09_11.md` | 7,135 | 2026-09-11 13:01:49 | `1ba7419178a1` |
| 210 | `docs/V3X/BOSS_URL_DUE_DILIGENCE_2026_09_11.md` | 10,970 | 2026-09-11 12:11:02 | `0fb588bb0c2e` |
| 211 | `docs/V3X/BPA_PILOT_2026_09_09_mavis.md` | 6,864 | 2026-09-09 13:39:22 | `d74e1534493e` |
| 212 | `docs/V3X/CANONICAL_5_UNVERIFIED_NOTE_2026_09_11.md` | 6,804 | 2026-09-11 13:30:46 | `b049140e130c` |
| 213 | `docs/V3X/CPATH_SIMULATION_REPORT_2026_09_10.md` | 6,825 | 2026-09-10 20:47:18 | `de772cd9e7ba` |
| 214 | `docs/V3X/D0_FREEZE_PREP_2026_09_09.md` | 9,844 | 2026-09-09 10:55:24 | `0d1e88c258aa` |
| 215 | `docs/V3X/D3_〔IM〕_MIDTERM_TEMPLATE.md` | 4,361 | 2026-09-09 11:23:41 | `574d5a79e363` |
| 216 | `docs/V3X/D5_DECISIONS_LAND_REPORT_2026_09_15.md` | 21,756 | 2026-09-15 15:15:39 | `8ff1a7c5413f` |
| 217 | `docs/V3X/D7_GITHUB_PUSH_RECEIVE_2026_09_15_v2.md` | 5,930 | 2026-09-15 17:28:16 | `2c4bb6078ee7` |
| 218 | `docs/V3X/D7_ONE_PAGE_SUMMARY_2026_09_11_v5.md` | 6,459 | 2026-09-11 13:30:46 | `67063f9cb238` |
| 219 | `docs/V3X/D7_ONE_PAGE_SUMMARY_TEMPLATE.md` | 5,830 | 2026-09-09 11:00:34 | `87563a63b854` |
| 220 | `docs/V3X/D7_POST_CLEANUP_PLAN_2026_09_18.json` | 20,271 | 2026-09-15 17:27:45 | `0b8a1a357aae` |
| 221 | `docs/V3X/D7_POST_CLEANUP_REPORT_2026_09_16.json` | 1,248 | 2026-09-16 11:01:13 | `40955bf2abc5` |
| 222 | `docs/V3X/D7_PRE_V3_POLISH_AND_TEAM_IMPROVEMENT_2026_09_16.md` | 10,692 | 2026-09-16 11:09:18 | `51869e3184f4` |
| 223 | `docs/V3X/D7_EXTERNAL_ADVISOR_〔IM〕_PUSH_REQUIREMENTS_2026_09_18.md` | 8,037 | 2026-09-16 11:08:22 | `935cb6ee3566` |
| 224 | `docs/V3X/D_FIX2_METRIC_VERIFY_REPORT_2026_09_15.md` | 7,352 | 2026-09-15 14:07:47 | `0a63824f0805` |
| 225 | `docs/V3X/DEPOSON_EMBEDDING_6WAY_THEORY_V0_2026_09_10.md` | 22,442 | 2026-09-10 20:22:54 | `ac8997b07731` |
| 226 | `docs/V3X/DEPOSON_EMBEDDING_6WAY_VERIFICATION_2026_09_10.md` | 17,803 | 2026-09-10 18:16:43 | `240a7ae4bdfb` |
| 227 | `docs/V3X/DPATH_CROSS_MODAL_2026_09_10.md` | 26,460 | 2026-09-16 11:01:12 | `e4ee3999f7ce` |
| 228 | `docs/V3X/KT_A1_SPEC_V0.1.md` | 29,570 | 2026-09-09 13:42:23 | `78b71d404366` |
| 229 | `docs/V3X/KT_B1_REWORK_REPORT_2026_09_10.md` | 11,478 | 2026-09-10 12:05:42 | `baef94e393de` |
| 230 | `docs/V3X/KT_B1_SPEC_V0.1.md` | 39,206 | 2026-09-30 20:36:32 | `0397b757362f` |
| 231 | `docs/V3X/KT_C1_REPORT_PHASE_B_2026_09_09.md` | 8,753 | 2026-09-09 14:17:30 | `825337b10a2d` |
| 232 | `docs/V3X/KT_C1_SPEC_V0.1.md` | 31,241 | 2026-09-09 13:42:23 | `59d8f56347d5` |
| 233 | `docs/V3X/KT_D0_EVIDENCE_CARD.md` | 6,354 | 2026-09-09 10:59:38 | `75b2f3b38c2a` |
| 234 | `docs/V3X/KT_D0_SPEC_V0.1.md` | 20,927 | 2026-09-09 13:42:24 | `cce8e9a1b00e` |
| 235 | `docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md` | 19,751 | 2026-09-15 11:31:34 | `977fe1b48f75` |
| 236 | `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` | 10,351 | 2026-09-09 10:05:24 | `bd1caab42b4c` |
| 237 | `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | 15,457 | 2026-09-30 20:36:51 | `423c84de20d5` |
| 238 | `docs/V3X/P_C_D1_D3_REPORT_2026_09_15.md` | 13,419 | 2026-09-15 15:08:22 | `79c7321056b8` |
| 239 | `docs/V3X/P_C_P_E_V0_1_VERIFICATION_2026_09_12.md` | 3,899 | 2026-09-11 13:01:11 | `ee043a13f801` |
| 240 | `docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md` | 6,301 | 2026-09-08 16:03:54 | `d427b2f57c33` |
| 241 | `docs/V3X/P_C_V0_1_VERIFICATION_2026_09_12.md` | 4,885 | 2026-09-11 13:00:18 | `00c7b7ceccdc` |
| 242 | `docs/V3X/P_D_B3_MERKLE_22_CAPTION_VERIFICATION_2026_09_16.md` | 10,979 | 2026-09-16 18:26:46 | `7f1492fbe657` |
| 243 | `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC.md` | 34,393 | 2026-09-17 15:15:44 | `f119f2f30287` |
| 244 | `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC_CHANGELOG.md` | 15,021 | 2026-09-17 15:16:40 | `fc73cab85d8f` |
| 245 | `docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md` | 34,367 | 2026-10-01 09:51:11 | `c13449101ab3` |
| 246 | `docs/V3X/P_D_FINGERPRINT_V0_SPEC.md` | 9,192 | 2026-09-04 13:11:41 | `3b67461b05fe` |
| 247 | `docs/V3X/P_E_D1_D3_REPORT_2026_09_15.md` | 13,109 | 2026-09-15 11:27:04 | `900da300d11e` |
| 248 | `docs/V3X/P_E_DOUBAN_EMBEDDING_V0_SPEC.md` | 16,876 | 2026-09-08 21:56:01 | `6f3c550cec13` |
| 249 | `docs/V3X/P_F_D1_FULL_REPORT_2026_09_15.md` | 15,985 | 2026-09-15 12:15:12 | `817efdc2f0ad` |
| 250 | `docs/V3X/P_F_D1_REPORT_2026_09_15.md` | 12,608 | 2026-09-16 11:01:12 | `e47d0348922e` |
| 251 | `docs/V3X/P_F_IMPLEMENTATION_2026_09_11.md` | 22,973 | 2026-09-16 11:01:12 | `edd048eaa721` |
| 252 | `docs/V3X/P_F_RESEARCH_2026_09_09.md` | 17,603 | 2026-09-09 13:49:14 | `98085df7811a` |
| 253 | `docs/V3X/P_F_SPEC_V0.md` | 19,804 | 2026-09-09 13:50:05 | `de90faf362c5` |
| 254 | `docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md` | 6,375 | 2026-09-11 12:15:55 | `b10fae0da66d` |
| 255 | `docs/V3X/P_F_V0_1_VERIFICATION_2026_09_12.md` | 4,188 | 2026-09-11 13:09:27 | `4d970e9c0aec` |
| 256 | `docs/V3X/P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md` | 12,501 | 2026-09-15 11:33:11 | `2f0765a1d39d` |
| 257 | `docs/V3X/P_G_V01_REPORT_2026_09_15.md` | 15,479 | 2026-09-15 12:06:17 | `9a6b08d03e0c` |
| 258 | `docs/V3X/PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md` | 4,587 | 2026-09-11 11:17:21 | `c165cd33a362` |
| 259 | `docs/V3X/PHASE_B_DELIVERY_2026_09_09.md` | 9,701 | 2026-09-09 14:19:28 | `ba53d73e3937` |
| 260 | `docs/V3X/QUICK_KILL_6_DIRECTIONS.md` | 15,085 | 2026-09-09 09:53:43 | `a476f241edb2` |
| 261 | `docs/V3X/REVIEWER_A_STATIC_AUDIT_2026_09_15.md` | 34,647 | 2026-09-15 14:22:04 | `575572872e9a` |
| 262 | `docs/V3X/REVIEWER_A_TRAE_FIX_AUDIT_2026_09_15.md` | 20,698 | 2026-09-15 15:29:00 | `195373c094d6` |
| 263 | `docs/V3X/REVIEWER_A_TRAE_N123_AUDIT_2026_09_15.md` | 17,151 | 2026-09-15 15:59:57 | `33ee7266cf5b` |
| 264 | `docs/V3X/REVIEWER_B_AUDIT_PHASE_B_2026_09_09.md` | 14,835 | 2026-09-09 14:17:07 | `5e99e79f2e11` |
| 265 | `docs/V3X/REVIEWER_B_TRAE_FIX_RERUN_2026_09_15.md` | 16,278 | 2026-09-15 15:28:54 | `f5ac9820310a` |
| 266 | `docs/V3X/REVIEWER_B_TRAE_N123_RERUN_2026_09_15.md` | 16,926 | 2026-09-15 15:57:55 | `31c27c0117a6` |
| 267 | `docs/V3X/RISK3_V0_FIXES_2026_09_11.md` | 13,271 | 2026-09-11 17:17:36 | `c00d1c22e7ed` |
| 268 | `docs/V3X/SPEC_V0_1_BOSS_SELFTEST_2026_09_09.md` | 10,708 | 2026-09-09 14:18:34 | `00e543564e3f` |
| 269 | `docs/V3X/TRAE_3RISK_FIX_REPORT_2026_09_16.md` | 9,267 | 2026-09-15 15:10:00 | `7478959cfc7d` |
| 270 | `docs/V3X/TRAE_PL_V2_EXPERIMENT_PROPOSAL_2026_09_17.md` | 8,849 | 2026-09-17 11:12:54 | `4020b1809780` |
| 271 | `docs/V3X/TRAE_PROACTIVE_AUDIT_REPORT_2026_09_16.md` | 6,493 | 2026-09-15 15:18:50 | `813b34dcac70` |
| 272 | `docs/V3X/TRAE_SELFCHECK_FIX_REPORT_2026_09_15.md` | 4,840 | 2026-09-15 15:39:00 | `226f740aa120` |
| 273 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 857,551 | 2026-09-29 19:42:49 | `41f5f1689d09` |
| 274 | `docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md` | 8,526 | 2026-09-16 11:03:10 | `4ffb21bb6bfa` |
| 275 | `docs/V3X/V3X_D6_PAPER_V2_2026_09_09_mavis.md` | 24,778 | 2026-09-09 13:41:07 | `4d06d34cb6fa` |
| 276 | `docs/V3X/V3X_D6_PAPER_zh.md` | 19,716 | 2026-09-09 11:34:06 | `feae8af2fefe` |
| 277 | `docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` | 38,545 | 2026-09-16 11:01:12 | `4a08521f8de1` |
| 278 | `docs/V3X/V3X_DAILY_KILL_V2_PLAN.md` | 15,327 | 2026-09-09 11:39:34 | `37e97e1e7b7f` |
| 279 | `docs/V3X/V3X_FULL_EXPERIMENT_DESIGN_2026_09_16.md` | 22,427 | 2026-09-16 12:28:47 | `3d847f9f3151` |
| 280 | `docs/V3X/V3X_PROJECT_EVOLUTION_FOR_KIMI.md` | 12,908 | 2026-09-15 14:55:11 | `4de2cbf57a49` |
| 281 | `docs/V3X/V42_V2_REMEDIATION_CLAUSE_2026_09_16.md` | 4,775 | 2026-09-16 18:33:04 | `e451a5a3d079` |
| 282 | `docs/V3X/V42_V2_VERIFIER_PERFORMANCE_REPORT_2026_09_16.md` | 11,080 | 2026-09-16 18:33:19 | `914053fc3e17` |
| 283 | `docs/V3X/V7_§3_P_C_P_E_GRAY_NOTE_2026_09_11.md` | 7,344 | 2026-09-11 13:15:52 | `f80cc4e1fb7f` |
| 284 | `docs/V3X_COLLAB_DIRECTIONS.md` | 16,363 | 2026-08-31 09:32:54 | `5a27c2350036` |
| 285 | `docs/variant_params_table.md` | 4,035 | 2026-08-23 00:01:28 | `25f90f106451` |
| 286 | `fingerprint_v0.py` | 10,950 | 2026-09-01 16:36:32 | `c0c38007c4e8` |
| 287 | `gt_common.py` | 3,601 | 2026-08-30 10:17:31 | `425b4b2f1c01` |
| 288 | `letters/_c4_theory_scan_reply_claude_code_2026_09_30.md` | 27,894 | 2026-09-30 21:51:00 | `2166b37e5d2a` |
| 289 | `letters/_claude_pending_pi_gaps_closeout_reply_2026_10_11.md` | 22,064 | 2026-10-11 23:40:53 | `f4defae83553` |
| 290 | `letters/_codex_c4_values_followup_reply_2026_10_10.md` | 4,490 | 2026-10-10 16:02:26 | `97a35f8ae94c` |
| 291 | `letters/_codex_c4_values_reply_2026_10_10.md` | 13,378 | 2026-10-10 13:49:24 | `8e4972352291` |
| 292 | `letters/_codex_c4_values_unblock_reply_2026_10_10.md` | 21,486 | 2026-10-10 17:35:08 | `a975c7990cd8` |
| 293 | `letters/_codex_theory_derivation_reply_2026_09_30.md` | 71,002 | 2026-09-30 23:52:12 | `7558eb1a5e34` |
| 294 | `letters/_commission_c4_values_EN_2026_10_10.md` | 56,217 | 2026-10-10 13:14:46 | `a397621085d6` |
| 295 | `letters/_commission_c4_values_EN_differences_exits_note_2026_10_10.md` | 7,817 | 2026-10-10 13:15:32 | `b20f25a66267` |
| 296 | `letters/_commission_c4_values_followup_EN_2026_10_10.md` | 7,583 | 2026-10-10 14:31:49 | `abe0652ab00f` |
| 297 | `letters/_commission_c4_values_unblock_EN_2026_10_10.md` | 10,244 | 2026-10-10 17:17:35 | `fde64a863b09` |
| 298 | `letters/_commission_c4_values_unblock_EN_differences_exits_note_2026_10_10.md` | 3,139 | 2026-10-10 17:17:46 | `1c769e28f8f5` |
| 299 | `letters/_commission_codex_theory_derivation_EN_2026_09_30.md` | 66,754 | 2026-09-30 19:58:54 | `af50969bebe2` |
| 300 | `letters/_commission_codex_theory_derivation_EN_v0.2_2026_09_30.md` | 82,016 | 2026-09-30 21:55:05 | `8b15f0957e0f` |
| 301 | `letters/_commission_glm_dualtrack_paper_addendum_v0.2_2026_10_01.md` | 53,344 | 2026-10-01 21:19:36 | `758e1ef3de27` |
| 302 | `letters/_commission_glm_dualtrack_paper_v0.5_2026_10_01.md` | 42,807 | 2026-10-01 11:48:26 | `d1650b14d89c` |
| 303 | `letters/_commission_glm_theory_derivation_2026_09_30.md` | 32,472 | 2026-09-30 19:49:06 | `344f5b9e0b08` |
| 304 | `letters/_commission_kimi_upload_2026_10_01_v0.2.md` | 35,421 | 2026-10-01 20:38:35 | `a77f7d509285` |
| 305 | `letters/_commission_pending_pi_gaps_closeout_EN_2026_10_11.md` | 22,685 | 2026-10-11 22:27:45 | `0ce066e5eb3f` |
| 306 | `letters/_commission_trae_direct_fix_2026_10_09_v0.1.md` | 37,262 | 2026-10-12 01:16:25 | `c50822b41539` |
| 307 | `letters/_commission_trae_direct_fix_oct_full_coverage_2026_10_12.md` | 46,077 | 2026-10-12 03:18:02 | `60751abbeb3b` |
| 308 | `letters/_dualtrack_paper_clue_book_v0.5_2026_10_01.md` | 109,614 | 2026-10-01 11:50:06 | `0fd7a26fc339` |
| 309 | `letters/_kimi_v4_t12_review_2026_09_20.md` | 6,644 | 2026-09-20 14:53:18 | `38070fd12f31` |
| 310 | `letters/_kimi_v4_theme_reply_2026_09_20.md` | 7,372 | 2026-09-20 17:52:32 | `3e37352efb4b` |
| 311 | `letters/_kimi_v4_theme_reply_2_brainstorm_2026_09_20.md` | 14,155 | 2026-09-20 21:11:34 | `bc14f47d927d` |
| 312 | `letters/_letter_to_pi_upload_application_approval_2026_09_26.md` | 23,368 | 2026-09-26 21:29:31 | `76d0b60e6bdc` |
| 313 | `letters/_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md` | 36,945 | 2026-09-26 20:45:07 | `512c73d45087` |
| 314 | `letters/_letter_to_pi_upload_application_supplement_2026_09_26.md` | 9,151 | 2026-09-26 21:28:18 | `5346a361801b` |
| 315 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 68,449 | 2026-09-26 21:07:20 | `44d9a1972a13` |
| 316 | `letters/_minimax_feedback_log_bloat_2026_09_29.md` | 13,361 | 2026-09-29 22:56:25 | `79ff4043169a` |
| 317 | `letters/_trae_direct_fix_reply_trae_code_2026_10_12.md` | 21,379 | 2026-10-12 01:34:03 | `f37ebc80d1df` |
| 318 | `letters/_v3_calibration_change_note_for_coze_glm_2026_09_27.md` | 42,948 | 2026-09-27 20:43:21 | `dda07ad77910` |
| 319 | `letters/_v3_recheck_indep_judgment_request_2026_09_27.md` | 22,702 | 2026-09-27 16:18:21 | `2c486c1791d5` |
| 320 | `letters/_v4_acceptance_coze_2026_09_20.md` | 5,467 | 2026-09-20 14:58:15 | `b2bf2a073ac8` |
| 321 | `letters/_v4_acceptance_trae_code_2026_09_20.md` | 7,746 | 2026-09-30 16:14:47 | `3e2f1c84e86d` |
| 322 | `letters/_v4_acceptance_trae_work_v1.0_2026_09_20.md` | 7,176 | 2026-09-20 17:36:19 | `3caf4e653a68` |
| 323 | `letters/_v4_attribution_errata_trae_work_2026_09_20.md` | 2,816 | 2026-09-20 17:36:48 | `e061c5806af6` |
| 324 | `letters/_v4_commission_inventory_anchor_note_2026_09_29.md` | 2,655 | 2026-09-29 13:25:03 | `849f8eba5bf0` |
| 325 | `letters/_v4_commission_kimi_fullupload_w3_2026_09_30.md` | 16,404 | 2026-09-30 19:41:29 | `84c2f4aa9691` |
| 326 | `letters/_v4_commission_paper_final_glm_2026_09_24.md` | 10,515 | 2026-09-24 18:55:43 | `53a425fe1bd2` |
| 327 | `letters/_v4_commission_paper_final_glm_2026_09_24_v2.md` | 13,749 | 2026-09-24 20:05:57 | `f3b3e13a0f1b` |
| 328 | `letters/_v4_commission_paper_final_glm_2026_09_24_v3.md` | 20,989 | 2026-09-26 19:19:09 | `614df9879696` |
| 329 | `letters/_v4_commission_paper_final_glm_2026_09_24_v4.md` | 31,531 | 2026-09-26 21:25:21 | `d5337702cec9` |
| 330 | `letters/_v4_commission_upload_channel_authorization_2026_09_26.md` | 26,937 | 2026-09-26 19:50:59 | `5e5479bfc453` |
| 331 | `letters/_v4_commission_upload_channel_authorization_reply_kimi_2026_09_26.md` | 11,575 | 2026-09-26 20:04:44 | `f8f4ae2e7b9b` |
| 332 | `letters/_v4_commission_upload_executor_2026_09_24.md` | 13,012 | 2026-09-24 18:56:08 | `adfa7dd03f76` |
| 333 | `letters/_v4_commission_upload_executor_2026_09_24_v2.md` | 16,894 | 2026-09-24 20:05:57 | `ff2154ce182d` |
| 334 | `letters/_v4_commission_upload_executor_2026_09_24_v3.md` | 25,091 | 2026-09-26 19:20:04 | `c20d4f58f5c8` |
| 335 | `letters/_v4_commission_upload_executor_reply_v3_2026_09_24.md` | 9,848 | 2026-09-26 19:35:40 | `50592e36ecad` |
| 336 | `letters/_v4_commission_upload_executor_reply_v3_exec_2026_09_26.md` | 4,471 | 2026-09-26 19:53:10 | `631bb517f79d` |
| 337 | `letters/_v4_commission_〔IM〕_report_coze_2026_09_24.md` | 7,197 | 2026-09-24 18:55:26 | `15f8227308bc` |
| 338 | `letters/_v4_commission_〔IM〕_report_coze_2026_09_24_v2.md` | 10,599 | 2026-09-24 20:05:56 | `389c51e70d19` |
| 339 | `letters/_v4_commission_〔IM〕_report_coze_2026_09_24_v3.md` | 13,898 | 2026-09-26 19:19:29 | `e5b63d181b15` |
| 340 | `letters/_v4_commission_〔IM〕_report_coze_2026_09_24_v4.md` | 21,433 | 2026-09-26 21:25:16 | `802c705e1469` |
| 341 | `letters/_v4_commission_〔IM〕_report_coze_reply_v4_2026_09_24.md` | 16,471 | 2026-09-26 22:20:19 | `c60dfd7c0f45` |
| 342 | `letters/_v4_d1_response_workbuddy_2026_09_20.md` | 14,881 | 2026-09-20 14:36:48 | `bc663b671994` |
| 343 | `letters/_v4_d1_review_codex_2026_09_20.md` | 4,506 | 2026-09-21 11:12:20 | `48387412b109` |
| 344 | `letters/_v4_distillation_acceptance_coze_2026_09_20.md` | 14,295 | 2026-09-20 18:03:55 | `3a8cb7b9d041` |
| 345 | `letters/_v4_distillation_acceptance_kimi_2026_09_20.md` | 6,454 | 2026-09-20 17:56:29 | `a4d194dbf9ad` |
| 346 | `letters/_v4_distillation_acceptance_trae_code_2026_09_20.md` | 5,218 | 2026-09-20 17:32:33 | `dc47fbf3c491` |
| 347 | `letters/_v4_distillation_brainstorm_reply_codex_2026_09_21.md` | 9,048 | 2026-09-21 11:12:20 | `0ff6c042b845` |
| 348 | `letters/_v4_distillation_invitation_2026_09_20_v1.0.md` | 54,784 | 2026-09-30 16:14:47 | `e4b00fa97d03` |
| 349 | `letters/_v4_distillation_reply_claude_code_2026_09_20.md` | 64,212 | 2026-09-21 11:01:14 | `d39cb17b051b` |
| 350 | `letters/_v4_distillation_reply_coze_2026_09_20.md` | 71,084 | 2026-09-20 21:53:15 | `00593014cbd3` |
| 351 | `letters/_v4_distillation_reply_trae_code_2026_09_20.md` | 43,570 | 2026-09-20 21:21:36 | `e87ec8f7e2fe` |
| 352 | `letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23.md` | 28,207 | 2026-09-23 13:35:13 | `9bb22099db3b` |
| 353 | `letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23_fix_addendum.md` | 6,067 | 2026-09-23 13:46:15 | `59b8df6e2e22` |
| 354 | `letters/_v4_distillation_theme_reply_workbuddy_2026_09_20.md` | 18,785 | 2026-09-20 18:19:48 | `e3fe63a2f708` |
| 355 | `letters/_v4_distillation_theme_reply_workbuddy_brainstorm_2026_09_21.md` | 13,553 | 2026-09-21 09:42:45 | `cdb27cd3008c` |
| 356 | `letters/_v4_distillation_theme_reply_workbuddy_part2_2026_09_20.md` | 12,963 | 2026-09-20 18:26:36 | `bfb4932f4467` |
| 357 | `letters/_v4_experiment_invitation_2026_09_20.md` | 32,164 | 2026-09-30 16:14:47 | `20f8242de6ca` |
| 358 | `letters/_v4_experiment_invitation_2026_09_20_v0.2.md` | 43,024 | 2026-09-30 16:14:47 | `72fc2e7fb098` |
| 359 | `letters/_v4_ide_track_review_trae_code_supplement_2026_09_20.md` | 13,263 | 2026-09-30 16:14:47 | `f88e429717aa` |
| 360 | `letters/_v4_ide_track_review_trae_work_2026_09_20.md` | 7,488 | 2026-09-20 17:35:40 | `21d384cf3422` |
| 361 | `letters/_v4_review_claude_code_2026_09_20.md` | 7,004 | 2026-09-20 14:32:01 | `b6f9956bcf5c` |
| 362 | `letters/_v4_theme_reply_mavis_2026_09_20.md` | 37,980 | 2026-09-30 16:14:47 | `5d932d7085cd` |
| 363 | `letters/_v4_theme_reply_mavis_2026_09_20_v1.1.md` | 38,085 | 2026-09-30 16:14:47 | `5c61f61f1f7e` |
| 364 | `letters/_v4_theme_reply_mavis_2026_09_20_v1.2.md` | 38,087 | 2026-09-30 16:14:47 | `f1d73c82511d` |
| 365 | `letters/_v4_theme_reply_trae_work_2026_09_20.md` | 11,458 | 2026-09-20 17:35:40 | `eba83c88b629` |
| 366 | `letters/_v4_theme_reply_trae_work_2026_09_20_v1.1.md` | 13,404 | 2026-09-20 17:39:33 | `be850d129f35` |
| 367 | `letters/_v4_theme_reply_trae_work_2026_09_20_v1.2.md` | 28,395 | 2026-09-20 20:58:07 | `6bee6ec434bd` |
| 368 | `letters/_v4_walkthrough_bugfix_reply_trae_code_2026_09_27.md` | 60,139 | 2026-09-27 20:13:23 | `f86b8b6c8ed2` |
| 369 | `letters/_v4_wide_walkthrough_reply_trae_code_2026_09_27.md` | 20,610 | 2026-09-27 20:28:20 | `9a98abf3119a` |
| 370 | `letters/_v5_rj5_external_rederive_request_2026_09_28.md` | 31,381 | 2026-09-28 18:22:06 | `cfd58ae66463` |
| 371 | `letters/_v5_rj5_external_rederive_request_EN_2026_09_28.md` | 51,013 | 2026-09-28 18:47:14 | `498215a9ec7d` |
| 372 | `letters/_walkthrough_bugfix_audit_reply_trae_code_2026_09_30.md` | 15,606 | 2026-09-30 19:07:36 | `5bfc26bbaa41` |
| 373 | `letters/LETTER_FROM_TRAE_2026_09_11.md` | 13,617 | 2026-09-11 16:30:23 | `1d3a9e52abe3` |
| 374 | `letters/LETTER_FROM_TRAE_3RISK_2026_09_11.md` | 5,145 | 2026-09-15 10:25:49 | `a1afbf3e1296` |
| 375 | `letters/LETTER_FROM_TRAE_REVIEW_2026_09_16.md` | 7,718 | 2026-09-15 15:19:16 | `6145162379c9` |
| 376 | `letters/LETTER_FROM_TRAE_SELFCHECK_FIX_2026_09_15.md` | 3,571 | 2026-09-15 15:39:01 | `141e05bf56ea` |
| 377 | `letters/TRAE_CODE_IMPROVEMENT_LETTER_2026_09_17.md` | 5,154 | 2026-09-17 19:16:03 | `53a90b9efbb9` |
| 378 | `letters/TRAE_FIX_REQUEST_3RISKS_2026_09_11.md` | 15,990 | 2026-09-11 17:27:09 | `62c4af080ea3` |
| 379 | `letters/TRAE_V3_CODE_IMPROVEMENT_LETTER_2026_09_16.md` | 7,376 | 2026-09-16 20:58:07 | `9aa717b2e1ac` |
| 380 | `letters/TRAE_V3_REVIEW_LETTER_2026_09_23.md` | 7,510 | 2026-09-23 13:08:23 | `0e7600ac4478` |
| 381 | `letters/TRAE_V4_WALKTHROUGH_BUGFIX_REQUEST_2026_09_27.md` | 105,136 | 2026-09-27 19:20:37 | `6ac3cb09567b` |
| 382 | `letters/TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md` | 101,560 | 2026-09-30 18:05:24 | `e17412088546` |
| 383 | `letters/verify_c4_originated_math.py` | 4,115 | 2026-10-10 17:30:17 | `3042cf59448e` |
| 384 | `letters/查理_deposon双主线论文终稿_2026-10-01_v0.3.md` | 239,700 | 2026-10-10 21:21:41 | `8baa9854b3f7` |
| 385 | `letters/查理_glm_dualtrack_paper_sole_letter_2026_10_01.md` | 13,105 | 2026-10-02 00:19:43 | `3c5059319ffe` |
| 386 | `LICENSE` | 1,085 | 2026-08-22 21:07:57 | `6a703b06f0fe` |
| 387 | `llm_fetch.py` | 8,433 | 2026-08-30 10:09:18 | `fda22714de2d` |
| 388 | `llm_prior.py` | 7,466 | 2026-08-30 10:10:54 | `7fba7d72a679` |
| 389 | `mindmap_corpus_v20.py` | 25,791 | 2026-09-29 12:06:04 | `e77e7f3455e0` |
| 390 | `paper/deposon_paper_final_cn.md` | 53,838 | 2026-09-20 17:11:14 | `c5f6a23f4408` |
| 391 | `paper/deposon_paper_final_en.md` | 68,164 | 2026-09-20 17:11:14 | `2ec20b96e941` |
| 392 | `paper/FIGURE_LANGUAGE_POLICY.md` | 2,495 | 2026-08-30 11:16:21 | `a18b5d0d4485` |
| 393 | `paper/v2/outline_v2X.md` | 10,476 | 2026-08-30 10:43:36 | `116d193b1607` |
| 394 | `paper/v2/related_work_v2X.md` | 10,114 | 2026-08-29 15:43:30 | `7fb001add973` |
| 395 | `README.md` | 7,279 | 2026-09-30 23:53:17 | `a80b3db006a5` |
| 396 | `README_V4_2026_09_29.md` | 58,635 | 2026-09-30 20:36:18 | `a6f88fb6e325` |
| 397 | `RELEASE_v1.4.0.md` | 3,847 | 2026-08-23 16:38:29 | `ff9ff3177c06` |
| 398 | `requirements.txt` | 27 | 2026-08-22 21:07:57 | `ab3045b2c6d9` |
| 399 | `results/_9model_full_merge_from_4workers_2026_10_09.json` | 19,337 | 2026-10-09 12:08:37 | `32aa0618a9d7` |
| 400 | `results/_archive_2026-10-12/pycache_sink/deposon_team_plugins_pycache/boss_pa_1_rbr_rm_v3df_ab_alpha_2026_10_09.cpython-314.pyc` | 55,784 | 2026-10-09 23:25:55 | `f96453ebead6` |
| 401 | `results/_archive_2026-10-12/pycache_sink/deposon_team_plugins_pycache/boss_pa_1_rbr_rm_v3df_ab_beta_2026_10_09.cpython-314.pyc` | 57,022 | 2026-10-09 23:25:21 | `80a752cca163` |
| 402 | `results/_archive_2026-10-12/pycache_sink/deposon_team_plugins_pycache/boss_pa_1_rbr_rm_v3df_p1_reopen_2026_09_29.cpython-314.pyc` | 103,946 | 2026-10-10 10:03:53 | `74467bb37f95` |
| 403 | `results/_archive_2026-10-12/pycache_sink/results_pycache/_s4prime_five_lines_runner_2026_10_11.cpython-314.pyc` | 43,685 | 2026-10-11 16:51:05 | `f4194cc5a522` |
| 404 | `results/_archive_2026-10-12/pycache_sink/results_pycache/_s5doubleprime_five_lines_runner_2026_10_11.cpython-314.pyc` | 44,952 | 2026-10-11 20:32:37 | `9fc3e2152679` |
| 405 | `results/_archive_2026-10-12/pycache_sink/results_pycache/_t1_exp2_executor_2026_10_09.cpython-314.pyc` | 87,302 | 2026-10-09 22:50:42 | `346595df084c` |
| 406 | `results/_archive_2026-10-12/pycache_sink/results_pycache/_v4_pi_cot_v3_ruleset_v3_executor.cpython-314.pyc` | 67,081 | 2026-10-09 17:34:40 | `08d4b51c45c6` |
| 407 | `results/_archive_2026-10-12/pycache_sink/results_pycache/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.cpython-314.pyc` | 69,630 | 2026-10-09 17:43:14 | `e7ab1adbf898` |
| 408 | `results/_archive_2026-10-12/superseded_variants/_card23_readout_utf8.txts` | 5,088 | 2026-10-10 00:37:18 | `4aa127d1dc62` |
| 409 | `results/_archive_2026_09_24/_final_verify.py._moved_20260924_1830` | 2,279 | 2026-09-24 13:37:46 | `db4428293040` |
| 410 | `results/_archive_2026_09_24/_l11_run1.json` | 12,143 | 2026-09-24 13:34:09 | `20b0e13064f8` |
| 411 | `results/_archive_2026_09_24/_l14_checkpoint.json` | 10,963 | 2026-09-24 14:56:40 | `91b582672b49` |
| 412 | `results/_archive_2026_09_24/_l14_records.json` | 50,957 | 2026-09-24 15:34:57 | `8f6fcf027149` |
| 413 | `results/_archive_2026_09_24/_volc_22cap_emb.py` | 11,105 | 2026-09-10 17:36:26 | `15904ecae629` |
| 414 | `results/_archive_2026_09_24/l14_runner_v2.py` | 23,056 | 2026-09-24 15:07:26 | `acf1cd6ccbd4` |
| 415 | `results/_archive_2026_09_24/l14_runner_v2_r1_atomic_2026_09_29.py` | 25,892 | 2026-09-29 11:12:41 | `b1923528ab84` |
| 416 | `results/_archive_manifest_deposon_sub_2026_09_23.json` | 52,153 | 2026-09-23 15:11:29 | `b34b9f7bdfb7` |
| 417 | `results/_archive_manifest_non_upload_2026_09_23.json` | 148,690 | 2026-09-23 15:11:35 | `b899103853ca` |
| 418 | `results/_bayesian_baseline_design_2026_10_10.md` | 29,783 | 2026-10-10 02:45:24 | `7e181a167702` |
| 419 | `results/_c1c4_ab_alpha_pilot_result_2026_10_09.json` | 104,225 | 2026-10-09 22:55:04 | `bc7c35707b78` |
| 420 | `results/_c1c4_ab_beta_pilot_result_2026_10_09.json` | 109,879 | 2026-10-09 22:59:59 | `fd72ebf836e1` |
| 421 | `results/_c1c4_input_gap_fill_plan_2026_10_09.md` | 35,635 | 2026-10-09 17:27:41 | `9f5675633e03` |
| 422 | `results/_chd_construction_domain_declaration_draft_2026_10_10.md` | 34,948 | 2026-10-10 23:35:41 | `17cf0d59cd7b` |
| 423 | `results/_ci_gap_fill_alt_bc_aper_prime_2026_10_09.json` | 23,272 | 2026-10-09 17:43:45 | `f729a6a03a9e` |
| 424 | `results/_clearance_evening_round_register_2026_09_29.md` | 18,201 | 2026-09-29 22:49:26 | `9c5543961e27` |
| 425 | `results/_closing_round_8_decisions_register_2026_10_09.md` | 2,151 | 2026-10-09 10:12:53 | `a28a478e14a8` |
| 426 | `results/_cpath_e3_sign_normalization_2026_10_01.md` | 19,740 | 2026-10-01 14:06:32 | `e67ebccc82c9` |
| 427 | `results/_criterion_application_scope_prereg_2026_10_01.md` | 50,322 | 2026-10-01 16:02:40 | `c4e3338619c6` |
| 428 | `results/_d05_b_coincidence_checks_exec_2026_10_10.md` | 21,061 | 2026-10-10 12:10:50 | `840fbf08caf4` |
| 429 | `results/_d05_b_coincidence_checks_exec_readings_2026_10_10.json` | 13,960 | 2026-10-10 12:08:44 | `586c435d1f15` |
| 430 | `results/_d1_backfill_intake_verdict_2026_10_01.md` | 42,115 | 2026-10-10 11:37:23 | `a7e8f90d9db7` |
| 431 | `results/_d8_boundary_revision_register_2026_09_30.md` | 32,406 | 2026-09-30 14:00:09 | `b46370bb9e3b` |
| 432 | `results/_d8_collection_ledger_2026_09_30.md` | 20,290 | 2026-09-30 16:42:14 | `031dd8429048` |
| 433 | `results/_d8_supplement_open_questions_2026_09_30.md` | 24,833 | 2026-09-30 13:14:41 | `579b375e9508` |
| 434 | `results/_exp04_h_contrast_readings_2026_10_10.json` | 72,704 | 2026-10-10 10:05:05 | `106e8667be2d` |
| 435 | `results/_exp04_h_contrast_readings_2026_10_10.md` | 17,386 | 2026-10-10 10:06:54 | `ac571bfe4d1d` |
| 436 | `results/_exp06_independent_check_2026_10_10.json` | 20,480 | 2026-10-10 10:31:42 | `4c36c376ab9c` |
| 437 | `results/_exp06_selfverified_renaming_note_2026_10_10.md` | 34,554 | 2026-10-10 11:25:56 | `8b4ec41a37dd` |
| 438 | `results/_exp06_selfverified_runner_fix_note_2026_10_10.md` | 17,052 | 2026-10-10 10:51:43 | `247398b687e6` |
| 439 | `results/_exp06_supplement_four_gaps_2026_10_10.md` | 26,519 | 2026-10-10 10:33:13 | `9f86cc5be8e9` |
| 440 | `results/_f2_branch_fix_register_2026_09_29.md` | 22,940 | 2026-09-29 22:57:03 | `a0cab58c032e` |
| 441 | `results/_f2_closeout_note_2026_09_29.md` | 16,317 | 2026-09-29 23:05:32 | `1599cb99abf3` |
| 442 | `results/_f4_direction1_domain_effectivity_2026_10_11.md` | 40,301 | 2026-10-11 14:05:56 | `fd4ec7559342` |
| 443 | `results/_fake_verdict_reverify_sixitem_ledger_2026_09_30.md` | 40,957 | 2026-09-30 17:25:45 | `41d7b76ea4d6` |
| 444 | `results/_five_terminal_judgments_ruling_2026_10_10.md` | 27,315 | 2026-10-10 12:28:00 | `9e96d0a1ba12` |
| 445 | `results/_forgotten_recovery_register_2026_10_08.md` | 34,287 | 2026-10-08 16:33:10 | `c981347cffad` |
| 446 | `results/_g5_ccp_execution_prereqs_2026_10_10.md` | 32,815 | 2026-10-10 18:52:37 | `ab1a07ae2fd1` |
| 447 | `results/_g5_ccp_seed_designation_revision_2026_10_10.md` | 20,979 | 2026-10-10 19:15:26 | `b53f40abb90b` |
| 448 | `results/_g5_rejudgment_construction_change_plan_2026_10_10.md` | 57,004 | 2026-10-10 18:22:43 | `fa0001a6dd0a` |
| 449 | `results/_ghostref_copy_log_2026_09_23.json` | 129,780 | 2026-09-23 15:11:45 | `8cd133d0896f` |
| 450 | `results/_is_corr_pair_caliber_revision_proposal_2026_10_09.md` | 33,497 | 2026-10-09 14:46:03 | `084c7d20067f` |
| 451 | `results/_k_v3df_0_1_four_readings_2026_10_09.json` | 65,507 | 2026-10-09 11:24:10 | `e87937d55471` |
| 452 | `results/_k_v3df_0_1_four_readings_2026_10_09.md` | 46,522 | 2026-10-09 11:24:10 | `53c28ca1ae3d` |
| 453 | `results/_k_v3s_4_3_frozen_recompute_2026_10_09.md` | 26,674 | 2026-10-09 14:27:36 | `1c1494083255` |
| 454 | `results/_kd04_c_denominator_expansion_readings_2026_10_10.json` | 23,314 | 2026-10-10 11:44:09 | `249009e6a0cc` |
| 455 | `results/_kd04_c_denominator_killline_prereg_2026_10_10.md` | 24,527 | 2026-10-10 11:27:33 | `8f2025e9de6f` |
| 456 | `results/_kd_unambiguous_meaning_ruling_2026_10_10.md` | 24,898 | 2026-10-10 11:36:58 | `f22ede7226d2` |
| 457 | `results/_kd_writing_convention_guidance_2026_10_09.md` | 20,179 | 2026-10-09 21:59:00 | `708dfac55be9` |
| 458 | `results/_kv3s_4_4_rejudge_2026_10_09.md` | 42,687 | 2026-10-09 23:10:27 | `bc397d5099dd` |
| 459 | `results/_md_trigger_prereg_effectivity_2026_10_11.md` | 41,636 | 2026-10-11 14:03:16 | `5d8cd0d1676f` |
| 460 | `results/_naming_ruling_note_2026_09_29.md` | 7,843 | 2026-09-29 21:18:08 | `57024f2cd30a` |
| 461 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 55,605 | 2026-10-10 02:54:17 | `f4e145b090b1` |
| 462 | `results/_p_i_real_labels_2026_09_16/p_i_real_labels_results_2026_09_16.json` | 1,043 | 2026-09-16 22:11:35 | `e934819ee9ed` |
| 463 | `results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json` | 1,669 | 2026-09-16 17:39:59 | `a9ad1de618f5` |
| 464 | `results/_p_l_p_c_finite_size_scaling_2026_09_16/p_l_p_c_finite_size_scaling_results_2026_09_16.json` | 9,076 | 2026-09-16 15:50:08 | `664e7cc05aec` |
| 465 | `results/_p_l_real_data_collapse_2026_09_16/p_l_real_data_collapse_results_v2_2026_09_16.json` | 3,761 | 2026-09-16 22:40:54 | `afe975606d40` |
| 466 | `results/_p_m_attack_surface_cost_2026_09_16/p_m_attack_surface_cost_results_2026_09_16.json` | 5,266 | 2026-09-16 17:34:14 | `fbcb60cf5102` |
| 467 | `results/_p_m_real_separation_2026_09_16/p_m_real_separation_results_2026_09_16.json` | 2,042 | 2026-09-16 22:12:02 | `a4b12d1cfedc` |
| 468 | `results/_p_n_curvature_potential_coupling_2026_09_16/p_n_curvature_potential_coupling_results_2026_09_16.json` | 4,276 | 2026-09-16 17:43:33 | `088f28524a1d` |
| 469 | `results/_p_o_stranger_verification_2026_09_16/p_o_stranger_verification_results_2026_09_16.json` | 5,916 | 2026-09-16 13:23:52 | `1e4c065da058` |
| 470 | `results/_plan_v3_pending_verify_2026_09_30.md` | 42,280 | 2026-09-30 19:06:18 | `7374004d6075` |
| 471 | `results/_q3_c1c4_l282_transposition_fix_applied_note_2026_10_09.md` | 16,105 | 2026-10-09 23:56:42 | `9572dfc3cd59` |
| 472 | `results/_q3_transposition_errata_2026_10_09.md` | 11,757 | 2026-10-09 23:26:45 | `659c4101f10b` |
| 473 | `results/_questionnaire_cards_intake_register_2026_10_09.md` | 442,288 | 2026-10-09 18:10:16 | `d917180db36f` |
| 474 | `results/_questionnaire_cards_intake_register_supplement_2026_10_09.md` | 72,199 | 2026-10-09 21:28:13 | `193386b9f23c` |
| 475 | `results/_questionnaire_cards_intake_register_supplement_2_2026_10_10.md` | 262,542 | 2026-10-10 00:23:35 | `dc43e3cb7610` |
| 476 | `results/_questionnaire_cards_intake_register_supplement_3_2026_10_10.md` | 67,225 | 2026-10-10 01:12:02 | `11681f0ad861` |
| 477 | `results/_questionnaire_cards_intake_register_supplement_4_2026_10_10.md` | 116,506 | 2026-10-10 10:54:25 | `d6ff041a9df9` |
| 478 | `results/_questionnaire_cards_intake_register_supplement_5_2026_10_10.md` | 77,189 | 2026-10-10 13:59:18 | `edb57308170d` |
| 479 | `results/_questionnaire_cards_intake_register_supplement_6_2026_10_10.md` | 106,453 | 2026-10-10 15:09:57 | `95ba771fa760` |
| 480 | `results/_questionnaire_cards_intake_register_supplement_6_receipt_2026_10_10.md` | 11,752 | 2026-10-10 15:11:57 | `0984955b0370` |
| 481 | `results/_r_pair4_design_and_texts_2026_10_09.md` | 35,189 | 2026-10-09 14:22:32 | `f793c5d9128f` |
| 482 | `results/_r_pair_addendum_2026_10_09.json` | 110,510 | 2026-10-09 16:45:34 | `cebc2f6ef5ec` |
| 483 | `results/_r_pair_intake_recompute_register_2026_10_09.md` | 36,774 | 2026-10-09 16:48:36 | `2dc64593b889` |
| 484 | `results/_r_pair_is_corr_coverage_design_2026_10_09.md` | 27,208 | 2026-10-09 12:31:28 | `48f04fa39397` |
| 485 | `results/_r_pair_question_texts_2026_10_09.md` | 30,352 | 2026-10-09 12:37:13 | `0ad849022328` |
| 486 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 591,833 | 2026-10-12 02:11:15 | `96720fcfd76a` |
| 487 | `results/_repo_post_cleanup_snapshot_2026_10_12.md` | 309,419 | 2026-10-12 03:09:29 | `6039a6e08017` |
| 488 | `results/_s3_closeout_convergence_2026_10_01.md` | 42,443 | 2026-10-01 12:16:50 | `bb62b5c174da` |
| 489 | `results/_s3_d1fill_recount_2026_10_01.md` | 22,877 | 2026-10-01 13:44:10 | `a7dff824ed56` |
| 490 | `results/_s3_f1_loader_fix_recompute_2026_10_08.json` | 20,144 | 2026-10-08 16:58:00 | `3044a070106e` |
| 491 | `results/_s3_kv3s_3_full_recompute_2026_10_01.md` | 22,183 | 2026-10-01 08:57:14 | `b0123f161c10` |
| 492 | `results/_s3_th_v21_reconciliation_verdict_2026_10_01.md` | 51,073 | 2026-10-10 11:37:23 | `84fa6996b656` |
| 493 | `results/_s3prime_alert_disposition_judgment_2026_10_11.md` | 53,188 | 2026-10-11 00:29:00 | `e7fcbc290a7e` |
| 494 | `results/_s3prime_degeneracy_selfcert_2026_10_11.md` | 39,939 | 2026-10-11 00:15:56 | `e4d96a516289` |
| 495 | `results/_s4_daily_share_margin_prerequisite_2026_10_09.md` | 18,197 | 2026-10-09 09:59:56 | `a929502e8421` |
| 496 | `results/_s4_execution_sequence_review_2026_10_10.md` | 19,158 | 2026-10-10 13:04:40 | `0e1eb2fdd25e` |
| 497 | `results/_s4_face_five_lines_ci_readings_execution_2026_10_09.md` | 29,750 | 2026-10-09 22:50:18 | `73550514152d` |
| 498 | `results/_s4_face_sync_2026_10_09.md` | 38,955 | 2026-10-09 15:33:16 | `6f8ba105b892` |
| 499 | `results/_s4_face_v2_sync_2026_10_09.md` | 46,890 | 2026-10-09 15:45:37 | `9d3cc20fd980` |
| 500 | `results/_s4_final_ruling_effectivity_register_2026_10_09.md` | 32,975 | 2026-10-09 15:00:52 | `21f2926efc5d` |
| 501 | `results/_s4_heldout_sampling_caliber_ruling_2026_10_09.md` | 35,453 | 2026-10-09 21:26:53 | `fb1b696de1d6` |
| 502 | `results/_s4_heldout_sampling_seed42_items_2026_10_09.json` | 20,033 | 2026-10-09 22:08:41 | `6a670e629dca` |
| 503 | `results/_s4_heldout_sampling_seedprime_items_2026_10_10.json` | 15,409 | 2026-10-10 23:07:39 | `6cbb8ba01bfb` |
| 504 | `results/_s4_heldout_sampling_seedprime_items_register_2026_10_10.md` | 24,690 | 2026-10-10 23:07:07 | `9da183328f18` |
| 505 | `results/_s4_heldout_sampling_seedthird_items_2026_10_11.json` | 43,130 | 2026-10-11 16:03:31 | `5777a07c608a` |
| 506 | `results/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | 22,646 | 2026-10-11 16:03:31 | `784f042bf93d` |
| 507 | `results/_s4_kex_killline_freeze_2026_10_10.md` | 15,284 | 2026-10-10 13:03:55 | `6269d0c6fd10` |
| 508 | `results/_s4_open_questions_addendum_2026_10_09.json` | 35,215 | 2026-10-09 14:29:17 | `4378dcc20624` |
| 509 | `results/_s4_open_questions_design_2026_10_09.md` | 31,803 | 2026-10-09 13:33:22 | `0186a4499bbc` |
| 510 | `results/_s4_open_questions_intake_recompute_register_2026_10_09.md` | 33,672 | 2026-10-09 14:30:52 | `2e66478e6db6` |
| 511 | `results/_s4_reading_prep_order_2026_10_08.md` | 20,613 | 2026-10-08 16:46:34 | `7ac726cda752` |
| 512 | `results/_s4_regen_execution_plan_2026_10_10.md` | 33,444 | 2026-10-10 12:00:40 | `70e22220350d` |
| 513 | `results/_s4_regen_golive_clearance_2026_10_10.md` | 27,436 | 2026-10-10 13:33:31 | `80d8905b9762` |
| 514 | `results/_s4_seedprime_inheldout_recompute_2026_10_10.md` | 21,866 | 2026-10-10 23:20:20 | `cf3368e7d5a0` |
| 515 | `results/_s4_seedprime_seq_t1_only_supplement_2026_10_11.md` | 24,783 | 2026-10-11 00:50:28 | `b2b044289ffe` |
| 516 | `results/_s4_seedprime_seq_t1_only_supplement_items_2026_10_11.json` | 28,030 | 2026-10-11 00:50:28 | `a834e0e7121a` |
| 517 | `results/_s4_source_wave_mapping_registration_2026_10_10.md` | 38,231 | 2026-10-10 17:56:29 | `26c8278e3552` |
| 518 | `results/_s4_substrate_freeze_register_2026_10_09.md` | 29,064 | 2026-10-09 14:17:49 | `f4a52862521b` |
| 519 | `results/_s4_substrate_grid_availability_2026_10_08.json` | 11,446 | 2026-10-08 16:59:10 | `66be80ab4b81` |
| 520 | `results/_s4_substrate_grid_availability_2026_10_08.md` | 14,995 | 2026-10-08 17:00:03 | `7deaee06c41a` |
| 521 | `results/_s4_substrate_refreeze_register_179_2026_10_09.md` | 45,386 | 2026-10-09 21:03:55 | `24ea764daeac` |
| 522 | `results/_s4_substrate_topup_addendum_2026_10_09.json` | 85,861 | 2026-10-09 13:53:09 | `1780542f0014` |
| 523 | `results/_s4_substrate_topup_collection_register_2026_10_09.md` | 18,327 | 2026-10-09 10:20:29 | `33c1a818ef4f` |
| 524 | `results/_s4_topup_intake_recompute_register_2026_10_09.md` | 32,779 | 2026-10-09 13:55:13 | `dfc9b0fbef5a` |
| 525 | `results/_s4_topup_questionnaire_design_2026_10_09.md` | 38,466 | 2026-10-09 11:00:13 | `b8f8f987f21b` |
| 526 | `results/_s4_tree_construct_adjusted_readings_2026_10_10.json` | 108,593 | 2026-10-10 09:51:47 | `a7aa4e9c8d47` |
| 527 | `results/_s4_tree_construct_adjustment_assessment_2026_10_10.md` | 33,453 | 2026-10-10 01:25:59 | `016c7dacaa54` |
| 528 | `results/_s4_v31_displacement_items_2026_10_10.json` | 36,822 | 2026-10-10 13:56:13 | `6f020c03e52c` |
| 529 | `results/_s4_v31_drift_register_face1_2026_10_10.md` | 11,485 | 2026-10-10 13:56:41 | `5ab168d82873` |
| 530 | `results/_s4_v31_keyword_table_final_2026_10_10.md` | 23,270 | 2026-10-10 13:03:25 | `1b7bcbcce589` |
| 531 | `results/_s4_v31_readings_execution_2026_10_10.md` | 21,467 | 2026-10-10 13:55:46 | `80d765f34163` |
| 532 | `results/_s4_v31_readings_summary_2026_10_10.json` | 5,569 | 2026-10-10 13:56:13 | `882a1b3deb0b` |
| 533 | `results/_s4_v31_regen_gold_items_2026_10_10.json` | 36,830 | 2026-10-10 13:54:57 | `4125cb2df92b` |
| 534 | `results/_s4_v31_regen_gold_register_2026_10_10.md` | 27,133 | 2026-10-10 13:54:32 | `9c9d8e8ecc72` |
| 535 | `results/_s4_vclause_1_6_revision_2026_10_10.md` | 14,900 | 2026-10-10 13:05:11 | `017b3cf38ae3` |
| 536 | `results/_s4prime_five_lines_readings_2026_10_11.json` | 15,219 | 2026-10-11 01:22:11 | `65a9b9be6327` |
| 537 | `results/_s4prime_five_lines_runner_2026_10_11.py` | 29,813 | 2026-10-11 01:19:53 | `f784b2fc92f4` |
| 538 | `results/_s5doubleprime_five_lines_readings_2026_10_11.json` | 16,099 | 2026-10-11 18:14:08 | `839fb5452578` |
| 539 | `results/_seed_double_identifier_finalization_2026_10_11.md` | 26,864 | 2026-10-11 15:36:15 | `6904852f8ceb` |
| 540 | `results/_skill_reference_update_and_user_surface_survey_2026_09_30.md` | 60,621 | 2026-09-30 17:49:57 | `cb7b7ec9ebcd` |
| 541 | `results/_stage1_independent_gate_review_2026_10_12.md` | 29,479 | 2026-10-12 03:17:28 | `4d95ae28c469` |
| 542 | `results/_stage3_1_bulk_reorg_completion_register_2026_10_12.md` | 15,818 | 2026-10-12 03:16:00 | `7439157b7be4` |
| 543 | `results/_stage3_1_register_fingerprint_placeholder_erratum_2026_10_12.md` | 4,495 | 2026-10-12 03:17:23 | `a0e437ef317c` |
| 544 | `results/_stage3_trigger_readings_items_2026_10_11.json` | 21,049 | 2026-10-11 16:52:40 | `079108c62a82` |
| 545 | `results/_stage3_trigger_recheck_2026_10_11.md` | 49,109 | 2026-10-11 16:26:38 | `aef26b8cbe50` |
| 546 | `results/_stage_sequence_violation_register_2026_10_12.md` | 11,159 | 2026-10-12 02:37:59 | `8dcfc200c7fd` |
| 547 | `results/_t1_exp2_activation_supplement_2026_10_09.md` | 24,708 | 2026-10-09 22:17:22 | `8db3f88b5ed0` |
| 548 | `results/_t1_exp2_answer_face_baseline_2026_10_09.json` | 11,792 | 2026-10-09 22:22:00 | `35773f5f1edb` |
| 549 | `results/_t1_exp2_executor_2026_10_09.py` | 67,955 | 2026-10-09 22:21:51 | `ce393b41618c` |
| 550 | `results/_t1_exp2_result_2026_10_09.json` | 35,239 | 2026-10-10 02:33:06 | `d9ccd75c652b` |
| 551 | `results/_t1_prereg_revision_qwen_temp_sweep_2026_10_09.md` | 16,994 | 2026-10-09 10:03:07 | `bda5d5f3dfa0` |
| 552 | `results/_t1_prereg_revision_temp_axis_exp2_2026_10_09.md` | 34,217 | 2026-10-09 21:49:30 | `2ff15aeeb5d0` |
| 553 | `results/_t1_qwen_temp_sweep_exec_register_2026_10_09.md` | 17,341 | 2026-10-09 11:20:07 | `7ad31e741400` |
| 554 | `results/_t1_qwen_temp_sweep_executor_2026_10_09.py` | 32,399 | 2026-10-09 10:22:20 | `f0c845864603` |
| 555 | `results/_t1_qwen_temp_sweep_r2_exec_register_2026_10_09.md` | 23,681 | 2026-10-09 18:10:33 | `cf4826a731d6` |
| 556 | `results/_t1_qwen_temp_sweep_r2_executor_2026_10_09.py` | 53,184 | 2026-10-09 18:06:06 | `38d0cf7fc9ba` |
| 557 | `results/_t1_qwen_temp_sweep_r2_result_2026_10_09.json` | 58,712 | 2026-10-09 18:06:16 | `8d6242da158c` |
| 558 | `results/_t1_qwen_temp_sweep_r2_verdict_2026_10_09.md` | 42,817 | 2026-10-09 18:23:43 | `9c18b9893579` |
| 559 | `results/_t1_qwen_temp_sweep_verdict_2026_10_09.md` | 21,672 | 2026-10-09 11:54:29 | `dfc858d3d930` |
| 560 | `results/_t1_r2_activation_2026_10_09.md` | 21,111 | 2026-10-09 17:07:33 | `8e59b797aa2d` |
| 561 | `results/_t1_substrate_gap_census_2026_10_01.md` | 32,371 | 2026-10-01 14:40:17 | `62fb594be3f9` |
| 562 | `results/_t1_substrate_gap_precondition_2026_10_01.md` | 22,196 | 2026-10-01 13:40:35 | `cf207df06762` |
| 563 | `results/_t1_temp_axis_new_experiment_design_2026_10_09.md` | 41,392 | 2026-10-09 21:17:20 | `7aaa90ee6d50` |
| 564 | `results/_t_s3_3_disposition_judgment_2026_10_10.md` | 31,855 | 2026-10-10 11:18:26 | `ee7a822a077b` |
| 565 | `results/_th_id_attribution_verification_2026_10_09.md` | 8,409 | 2026-10-09 15:02:39 | `94740f8d3c8d` |
| 566 | `results/_th_t1_n_min_revision_proposal_2026_10_09.md` | 34,884 | 2026-10-09 15:33:46 | `24da21074cc2` |
| 567 | `results/_tra_v0_2026_09_10.py` | 12,125 | 2026-09-10 20:20:20 | `d80a8f75a122` |
| 568 | `results/_trae_errata_sha_drift_attribution_2026_10_01.md` | 23,913 | 2026-10-01 12:31:37 | `6d5836cc6d3a` |
| 569 | `results/_trae_sixitem_disposal_and_collision_register_2026_10_01.md` | 19,268 | 2026-10-01 09:10:55 | `545b17d403be` |
| 570 | `results/_u04_1_exemption_precondition_verification_2026_10_09.json` | 21,862 | 2026-10-09 17:25:09 | `bddfeac3ee2f` |
| 571 | `results/_v34_experiment_gap_plan_2026_10_08.md` | 36,066 | 2026-10-08 16:46:11 | `996feb1db9cb` |
| 572 | `results/_v3_construct_degradation_diag_2026_09_23.json` | 11,609 | 2026-09-23 14:20:36 | `c8d539a58d29` |
| 573 | `results/_v3_n_cpath_live_data_2026_09_27.json` | 12,711 | 2026-09-27 14:16:19 | `25374af92f88` |
| 574 | `results/_v3_n_ktb1_distortion_bound_data_2026_09_27.json` | 6,411 | 2026-09-27 14:17:05 | `26c0d0b0ffb6` |
| 575 | `results/_v3_n_pg_boss_live_data_2026_09_27.json` | 9,220 | 2026-09-27 14:15:46 | `be11c5274807` |
| 576 | `results/_v3_n_recheck_llm_verdict_2026_09_27.md` | 21,332 | 2026-09-27 14:20:06 | `426cfe18cf65` |
| 577 | `results/_v3_recheck_01_executor_2026_09_27.py` | 41,004 | 2026-09-27 15:43:40 | `919fa909381e` |
| 578 | `results/_v3_recheck_01_rescript_2026_09_27.md` | 14,541 | 2026-09-30 16:15:20 | `a3c95102290f` |
| 579 | `results/_v3_recheck_01_result_2026_09_27.json` | 167,831 | 2026-09-27 16:04:01 | `c19e2ab24e63` |
| 580 | `results/_v3_recheck_04_executor_2026_09_27.py` | 49,405 | 2026-09-27 15:56:09 | `e098fa21700d` |
| 581 | `results/_v3_recheck_04_rescript_2026_09_27.md` | 14,780 | 2026-09-30 16:15:20 | `34099595fe75` |
| 582 | `results/_v3_recheck_04_result_2026_09_27.json` | 840,158 | 2026-09-27 16:04:05 | `db8cfb974ce3` |
| 583 | `results/_v3_recheck_05_rescript_2026_09_28.md` | 22,178 | 2026-09-28 13:29:42 | `88b7eaf8675d` |
| 584 | `results/_v3_recheck_05_result_2026_09_28.json` | 450,701 | 2026-09-28 13:28:21 | `f63b36b75a51` |
| 585 | `results/_v3_recheck_08_executor_2026_09_27.py` | 15,598 | 2026-09-27 14:49:01 | `21c4ba4d479e` |
| 586 | `results/_v3_recheck_08_rescript_2026_09_27.md` | 10,459 | 2026-09-27 14:50:51 | `2e08b9ae9f09` |
| 587 | `results/_v3_recheck_08_result_2026_09_27.json` | 10,587 | 2026-09-27 14:51:08 | `0d2af01086db` |
| 588 | `results/_v3_recheck_08b_executor/executor_2026_09_27.py` | 43,901 | 2026-09-27 15:17:27 | `b292410d9a69` |
| 589 | `results/_v3_recheck_08b_executor/rescript_2026_09_27.md` | 18,501 | 2026-09-27 15:18:54 | `78f3aba1f24c` |
| 590 | `results/_v3_recheck_08b_executor/result_2026_09_27.json` | 88,052 | 2026-09-27 15:17:36 | `f9a7fa2d65b1` |
| 591 | `results/_v3_recheck_08c_preexp_data/_v3_recheck_08c_sha12fix_r1_2026_10_12.py` | 1,395 | 2026-10-12 01:30:19 | `4b7ed4d0a3e5` |
| 592 | `results/_v3_recheck_08c_preexp_data/executor_2026_09_27.py` | 37,775 | 2026-09-27 17:52:40 | `cb6eb9164df3` |
| 593 | `results/_v3_recheck_08c_preexp_data/rescript_2026_09_27.md` | 17,069 | 2026-10-12 01:30:19 | `035af77db626` |
| 594 | `results/_v3_recheck_08c_preexp_data/result_2026_09_27.json` | 146,601 | 2026-09-27 17:52:51 | `689a6e4427a8` |
| 595 | `results/_v3_recheck_10_rescript_2026_09_27.md` | 14,445 | 2026-09-27 15:23:59 | `fc0ffd27adca` |
| 596 | `results/_v3_recheck_10_result_2026_09_27.json` | 82,535 | 2026-09-27 15:20:09 | `5d4b6baf1b18` |
| 597 | `results/_v3_recheck_12_jsv_check_2026_09_27.md` | 15,821 | 2026-09-30 16:15:20 | `c5eab30e9fc6` |
| 598 | `results/_v3_recheck_12_rescript_2026_09_27.md` | 21,222 | 2026-09-30 16:15:20 | `776c86c735f8` |
| 599 | `results/_v3_recheck_12_result_2026_09_27.json` | 187,612 | 2026-09-27 16:04:05 | `cdb37ed0b32f` |
| 600 | `results/_v3_recheck_12_rj5_provenance_2026_09_27.md` | 23,822 | 2026-09-27 17:30:07 | `20f15c49feb5` |
| 601 | `results/_v3_recheck_19_rescript_2026_09_27.md` | 11,089 | 2026-09-27 14:56:14 | `82a947f2aebd` |
| 602 | `results/_v3_recheck_19_result_2026_09_27.json` | 59,888 | 2026-09-27 14:56:25 | `df07cf80930f` |
| 603 | `results/_v3_recheck_21_rescript_2026_09_27.md` | 14,618 | 2026-09-27 16:44:40 | `04f6ecd482b9` |
| 604 | `results/_v3_recheck_21_result_2026_09_27.json` | 44,928 | 2026-09-27 16:54:07 | `354ae9c14fe2` |
| 605 | `results/_v3_recheck_26_executor_2026_09_27.py` | 15,056 | 2026-09-27 14:45:28 | `46c326c756c3` |
| 606 | `results/_v3_recheck_26_preexp_data_2026_09_27.json` | 94,658 | 2026-09-27 15:30:22 | `177c88e1bd82` |
| 607 | `results/_v3_recheck_26_preexp_executor_2026_09_27.py` | 38,726 | 2026-09-27 15:29:13 | `775217a462f5` |
| 608 | `results/_v3_recheck_26_preexp_report_2026_09_27.md` | 23,048 | 2026-09-30 16:15:20 | `a46230e344af` |
| 609 | `results/_v3_recheck_26_rescript_2026_09_27.md` | 13,747 | 2026-09-27 20:10:38 | `6b86576146a3` |
| 610 | `results/_v3_recheck_26_result_2026_09_27.json` | 11,994 | 2026-09-27 14:51:06 | `eb6a99dd46dd` |
| 611 | `results/_v3_recheck_26b_executor_2026_09_27.py` | 43,171 | 2026-09-27 15:51:38 | `5c906113a210` |
| 612 | `results/_v3_recheck_26b_executor_r2_2026_09_28.py` | 52,272 | 2026-09-28 22:47:39 | `0808af6212c5` |
| 613 | `results/_v3_recheck_26b_executor_r3_2026_09_29.py` | 64,959 | 2026-09-29 10:50:41 | `6c83e7a7ca2e` |
| 614 | `results/_v3_recheck_26b_r3_result_2026_09_29.json` | 54,294 | 2026-09-29 19:08:57 | `c9d3c9f819f1` |
| 615 | `results/_v3_recheck_26b_rescript_2026_09_27.md` | 30,552 | 2026-09-30 16:15:20 | `ae81d9b59054` |
| 616 | `results/_v3_recheck_26b_result_2026_09_27.json` | 44,379 | 2026-09-27 15:52:40 | `49c6e5a07732` |
| 617 | `results/_v3_recheck_26b_verdict_prep_2026_10_01.md` | 36,133 | 2026-10-01 08:58:09 | `3aab3f7660fc` |
| 618 | `results/_v3_recheck_27_rescript_2026_09_27.md` | 14,599 | 2026-09-27 15:22:57 | `6f045bdc70e7` |
| 619 | `results/_v3_recheck_27_result_2026_09_27.json` | 42,571 | 2026-09-27 15:20:39 | `e06cb51fb3af` |
| 620 | `results/_v3_recheck_28_rescript_2026_09_27.md` | 10,187 | 2026-09-27 14:50:20 | `a0734e0a6860` |
| 621 | `results/_v3_recheck_28_result_2026_09_27.json` | 26,113 | 2026-09-27 14:53:26 | `c0a8cb9029a7` |
| 622 | `results/_v3_recheck_35_rescript_2026_09_27.md` | 13,211 | 2026-09-27 16:24:33 | `138faf395f40` |
| 623 | `results/_v3_recheck_35_result_2026_09_27.json` | 35,091 | 2026-09-29 12:07:14 | `a8a4befb21f5` |
| 624 | `results/_v3_recheck_prereg_v1_2026_09_27.md` | 37,346 | 2026-09-27 13:33:20 | `88052d7db895` |
| 625 | `results/_v3_recheck_prereg_v1p1_2026_09_27.md` | 42,970 | 2026-09-27 14:44:22 | `bcc3cee23e82` |
| 626 | `results/_v3_recheck_prereg_v1p2_2026_09_27.md` | 38,932 | 2026-09-30 16:15:20 | `9da148037744` |
| 627 | `results/_v3_recheck_prereg_v1p3_2026_09_27.md` | 35,200 | 2026-09-30 16:15:20 | `272ed65bf50e` |
| 628 | `results/_v3_recheck_prereg_v1p4_2026_09_27.md` | 69,406 | 2026-09-28 15:27:29 | `5294e4a2bd14` |
| 629 | `results/_v3_recheck_prereg_v1p5_2026_09_29.md` | 18,680 | 2026-09-29 19:22:00 | `7b1374578de4` |
| 630 | `results/_v3_recheck_verdict_register_2026_09_27.md` | 112,085 | 2026-09-30 16:15:20 | `d9b6b974cfc1` |
| 631 | `results/_v3_s1_executor/executor_2026_09_27.py` | 54,937 | 2026-09-27 15:44:50 | `10870941c283` |
| 632 | `results/_v3_s1_executor/rescript_2026_09_27.md` | 17,253 | 2026-09-27 15:45:21 | `9d49a632ee81` |
| 633 | `results/_v3_s1_executor/result_2026_09_27.json` | 24,975 | 2026-09-27 15:45:21 | `bfc99c3133dd` |
| 634 | `results/_v3_s2_executor/executor_2026_09_27.py` | 84,993 | 2026-09-27 16:03:46 | `f1e272a0924a` |
| 635 | `results/_v3_s2_executor/rescript_2026_09_27.md` | 25,151 | 2026-10-12 01:30:19 | `ff0f964be8aa` |
| 636 | `results/_v3_s2_executor/result_2026_09_27.json` | 51,039 | 2026-09-27 16:05:12 | `d73d51e670de` |
| 637 | `results/_v3_s3_collection_brief_2026_09_28.md` | 19,045 | 2026-09-28 13:38:11 | `d5ba1161e37f` |
| 638 | `results/_v3_s3_wordexpand_data/executor_2026_09_28.py` | 46,005 | 2026-09-28 13:35:10 | `80f1445ce45d` |
| 639 | `results/_v3_s3_wordexpand_data/executor_r1_2026_09_28.py` | 43,524 | 2026-09-28 13:59:47 | `39c29e0f092e` |
| 640 | `results/_v3_s3_wordexpand_data/rescript_2026_09_28.md` | 18,225 | 2026-09-28 13:36:15 | `98d4f62cd52a` |
| 641 | `results/_v3_s3_wordexpand_data/rescript_r1_2026_09_28.md` | 17,168 | 2026-09-28 14:04:26 | `c991ddb1deb4` |
| 642 | `results/_v3_s3_wordexpand_data/result_2026_09_28.json` | 34,953 | 2026-09-28 13:38:18 | `f7f6d875d73a` |
| 643 | `results/_v3_s3_wordexpand_recheck_r1_2026_09_28.json` | 33,867 | 2026-09-28 14:04:43 | `67ccea282d1c` |
| 644 | `results/_v3_s_phrasetemplate_preexp_data/executor_2026_09_27.py` | 35,555 | 2026-09-27 17:47:47 | `96f491a8e2bf` |
| 645 | `results/_v3_s_phrasetemplate_preexp_data/rescript_2026_09_27.md` | 17,574 | 2026-10-12 01:30:19 | `d42ea1fa61f1` |
| 646 | `results/_v3_s_phrasetemplate_preexp_data/result_2026_09_27.json` | 36,844 | 2026-09-27 17:47:59 | `fae3c4640507` |
| 647 | `results/_v3_s_phrasetemplate_prereg_v1_2026_09_27.md` | 33,932 | 2026-09-27 17:11:28 | `7e1323b09030` |
| 648 | `results/_v3_s_prereg_v1_2026_09_27.md` | 46,836 | 2026-09-27 15:28:46 | `ef5a40554960` |
| 649 | `results/_v3_supplement_verdict_2026_09_23.md` | 15,247 | 2026-09-23 14:27:09 | `b70211bfa83e` |
| 650 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 194,083 | 2026-09-30 16:18:35 | `965db22e9130` |
| 651 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 355,819 | 2026-09-29 12:12:36 | `df7e9cd39251` |
| 652 | `results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md` | 10,288 | 2026-09-24 18:55:03 | `55cd332f66f2` |
| 653 | `results/_v3_v4_ghostref_reconciliation_2026_09_23.md` | 169,864 | 2026-09-23 15:11:45 | `1d52db0ebf53` |
| 654 | `results/_v3n_cpath_live_rerun_2026_10_01.json` | 60,012 | 2026-10-01 09:24:20 | `7c26d08ece3b` |
| 655 | `results/_v3x_18frozen_remeasure_2026_09_16/v3x_18frozen_remeasure_results_2026_09_16.json` | 4,202 | 2026-09-16 23:32:09 | `928794710241` |
| 656 | `results/_v3x_conservation_anchor_2026_09_17.txt` | 940 | 2026-09-17 10:20:17 | `f331a9c2bd22` |
| 657 | `results/_v3x_d0_5_aggregation_2026_09_17.md` | 12,010 | 2026-09-17 13:08:30 | `ddf0d1aa96d2` |
| 658 | `results/_v3x_d0_5_experiment_invitation_2026_09_17.md` | 7,617 | 2026-09-17 09:34:32 | `d8f2b99aa527` |
| 659 | `results/_v3x_d0_5_proposal_coze_2026_09_17.md` | 13,200 | 2026-09-17 11:06:19 | `759c25b21ed4` |
| 660 | `results/_v3x_d0_5_proposal_trae_2026_09_17.md` | 13,254 | 2026-09-20 17:11:14 | `b1c227d54a82` |
| 661 | `results/_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json` | 17,053 | 2026-09-16 12:37:12 | `f39412103366` |
| 662 | `results/_v3x_p_k_verify_2026_09_16/v3x_p_k_verify_results_2026_09_16.json` | 2,059 | 2026-09-16 23:33:03 | `59c2113b7c71` |
| 663 | `results/_v3x_p_l_v3_external_spec_2026_09_17.md` | 5,769 | 2026-09-17 11:03:24 | `6a5b6eb635f0` |
| 664 | `results/_v3x_p_l_v3_mistral_large_2512_20260917_115049.json` | 16,835 | 2026-09-17 11:52:29 | `523b5941c30c` |
| 665 | `results/_v3x_p_l_v3_summary_mistral_large_2512_20260917_115049.md` | 9,570 | 2026-09-17 11:53:50 | `183205baa9ac` |
| 666 | `results/_v4_bom_u1_prereg_2026_09_28.md` | 19,185 | 2026-09-28 18:33:05 | `5456acbf2cb5` |
| 667 | `results/_v4_checkpoint_atomic_and_pycache_2026_09_28.md` | 25,470 | 2026-09-28 15:55:24 | `52b3dec13e06` |
| 668 | `results/_v4_closeout_account_reconciliation_2026_10_12.md` | 24,453 | 2026-10-12 02:16:41 | `4a3b661a7d13` |
| 669 | `results/_v4_closeout_bulk_reorganize_register_2026_10_12.md` | 197,283 | 2026-10-12 03:09:00 | `2b244f0760b4` |
| 670 | `results/_v4_closeout_moves_and_cleanup_register_2026_10_12.md` | 18,568 | 2026-10-12 02:30:44 | `69a834caf812` |
| 671 | `results/_v4_day_inventory_2026_09_27.md` | 40,487 | 2026-09-27 18:11:43 | `7662d5058a7d` |
| 672 | `results/_v4_day_inventory_measure_2026_09_27.py` | 8,226 | 2026-09-27 18:02:27 | `3e903f224f87` |
| 673 | `results/_v4_effective_register_2026_09_28.md` | 30,607 | 2026-09-28 14:22:37 | `2a65c1274202` |
| 674 | `results/_v4_evidence_audit_reconcile_2026_09_26.md` | 24,168 | 2026-09-30 16:15:20 | `fe907046eda1` |
| 675 | `results/_v4_exec_surface_switch_2026_09_28.md` | 28,506 | 2026-09-28 17:28:07 | `3bc852e0d48b` |
| 676 | `results/_v4_item04_textfix_prereg_v1x_2026_09_28.md` | 42,153 | 2026-09-28 17:46:40 | `4ad2695935d3` |
| 677 | `results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` | 37,629 | 2026-09-26 19:12:42 | `cc498bc28525` |
| 678 | `results/_v4_maindir_count_monitor_2026_09_27.md` | 15,313 | 2026-09-27 11:50:37 | `71e9cc179bec` |
| 679 | `results/_v4_pi_cot_v2_coding_review_2026_09_26.md` | 42,914 | 2026-09-26 18:35:47 | `5fbec21e0ad2` |
| 680 | `results/_v4_pi_cot_v2_dataset.json` | 12,672 | 2026-09-24 15:55:01 | `7b01cd835a41` |
| 681 | `results/_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | 4,103 | 2026-09-24 18:47:18 | `172093a23e4b` |
| 682 | `results/_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json` | 6,132 | 2026-09-26 16:54:17 | `439721007aaf` |
| 683 | `results/_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json` | 7,566 | 2026-09-26 17:04:48 | `41d6c28ca87c` |
| 684 | `results/_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json` | 6,666 | 2026-09-26 17:22:21 | `99c58906f792` |
| 685 | `results/_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json` | 7,668 | 2026-09-26 17:27:21 | `c6d092f77932` |
| 686 | `results/_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json` | 10,257 | 2026-09-26 17:39:37 | `26f110a6e571` |
| 687 | `results/_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json` | 11,589 | 2026-09-26 18:10:28 | `6e104e2db038` |
| 688 | `results/_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json` | 14,722 | 2026-09-26 18:18:19 | `d96b747bfc6c` |
| 689 | `results/_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | 19,615 | 2026-09-26 18:30:47 | `401bd614cdf7` |
| 690 | `results/_v4_pi_cot_v2_prereg.md` | 4,247 | 2026-09-23 17:56:05 | `cc25c5149ce1` |
| 691 | `results/_v4_pi_cot_v2_questionnaire_v1.md` | 12,402 | 2026-09-24 10:51:01 | `7b14cdb31d21` |
| 692 | `results/_v4_pi_cot_v2_result.json` | 9,068 | 2026-09-24 17:41:54 | `1665f367b2c4` |
| 693 | `results/_v4_pi_cot_v2_result_v2.json` | 18,089 | 2026-09-26 18:50:30 | `f86727c857a8` |
| 694 | `results/_v4_pi_cot_v2_ruleset.json` | 5,876 | 2026-09-24 17:41:54 | `821465001819` |
| 695 | `results/_v4_pi_cot_v2_ruleset_executor.py` | 39,281 | 2026-09-24 17:41:44 | `48dca1d4281c` |
| 696 | `results/_v4_pi_cot_v2_ruleset_v2.json` | 6,179 | 2026-09-26 18:50:30 | `c5b3dd141655` |
| 697 | `results/_v4_pi_cot_v2_ruleset_v2_executor.py` | 52,465 | 2026-09-26 18:49:42 | `eb22f13d571c` |
| 698 | `results/_v4_pi_cot_v2_verdict.md` | 22,340 | 2026-09-24 18:07:05 | `eb9ad4193cf2` |
| 699 | `results/_v4_pi_cot_v2_verdict_v2.md` | 33,723 | 2026-09-26 19:03:30 | `5d79e67a4e9d` |
| 700 | `results/_v4_pi_cot_v3_alt_reading_definition_2026_09_27.md` | 10,251 | 2026-09-27 17:14:41 | `58ed6be022ed` |
| 701 | `results/_v4_pi_cot_v3_dataset.json` | 16,025 | 2026-09-27 12:12:25 | `5118f5b44f17` |
| 702 | `results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json` | 20,194 | 2026-09-27 12:10:45 | `cbf60a630c9f` |
| 703 | `results/_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json` | 18,714 | 2026-09-27 17:04:40 | `6eed9acdb99a` |
| 704 | `results/_v4_pi_cot_v3_dataset_addendum_d5_2026_09_27.json` | 16,587 | 2026-09-27 13:17:51 | `990c0c42a6f6` |
| 705 | `results/_v4_pi_cot_v3_dataset_addendum_d6_2026_09_28.json` | 19,214 | 2026-09-28 13:46:29 | `9669efa804b7` |
| 706 | `results/_v4_pi_cot_v3_dataset_addendum_d6b_2026_09_28.json` | 27,009 | 2026-09-28 15:00:07 | `5d94a8617b5b` |
| 707 | `results/_v4_pi_cot_v3_dataset_addendum_d8_bhalf_2026_09_30.json` | 58,581 | 2026-09-30 16:21:49 | `b02ef31f1e4e` |
| 708 | `results/_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json` | 374,072 | 2026-09-30 16:18:01 | `769ef8b71462` |
| 709 | `results/_v4_pi_cot_v3_dataset_addendum_s3_d1fill_2026_10_01.json` | 46,909 | 2026-10-01 12:55:21 | `b9026cbf5ca2` |
| 710 | `results/_v4_pi_cot_v3_dataset_addendum_s3_d7_2026_09_29.json` | 17,252 | 2026-09-29 10:57:48 | `c0ebbd1f4633` |
| 711 | `results/_v4_pi_cot_v3_dataset_v1p3_2026_09_27.json` | 12,975 | 2026-09-27 17:48:03 | `ed596914259a` |
| 712 | `results/_v4_pi_cot_v3_k3b_recheck_r1_2026_09_27.json` | 26,891 | 2026-09-27 17:13:08 | `cbc14a76f038` |
| 713 | `results/_v4_pi_cot_v3_missing_ledger_correction_2026_09_28.md` | 12,851 | 2026-09-28 14:03:02 | `44c4d570375c` |
| 714 | `results/_v4_pi_cot_v3_prereg.md` | 27,223 | 2026-09-27 12:02:44 | `b7547329af2e` |
| 715 | `results/_v4_pi_cot_v3_questionnaire_v2_d8_2026_09_28.md` | 53,581 | 2026-09-28 15:19:16 | `238077d25919` |
| 716 | `results/_v4_pi_cot_v3_result_v3.json` | 27,203 | 2026-09-27 13:04:21 | `585714f9660c` |
| 717 | `results/_v4_pi_cot_v3_result_v3r1_2026_09_27.json` | 22,292 | 2026-09-27 17:48:03 | `735c03db1ae9` |
| 718 | `results/_v4_pi_cot_v3_ruleset_v3.json` | 21,392 | 2026-09-27 12:31:02 | `9d77a5e2cbab` |
| 719 | `results/_v4_pi_cot_v3_ruleset_v3_executor.py` | 58,794 | 2026-09-27 12:29:46 | `8a81d90c69ba` |
| 720 | `results/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py` | 62,115 | 2026-09-27 16:56:08 | `ee8671a28c2f` |
| 721 | `results/_v4_pi_cot_v3_v3r1_rescript_2026_09_27.md` | 11,385 | 2026-09-30 16:15:20 | `75aedf9ba95e` |
| 722 | `results/_v4_pi_cot_v3_verdict_v3.md` | 53,751 | 2026-09-27 13:15:20 | `bb44fdc7ab0f` |
| 723 | `results/_v4_pi_cot_v3_verdict_v3_signoff_2026_09_27.md` | 42,157 | 2026-09-27 13:24:20 | `41d29f4deb70` |
| 724 | `results/_v4_supp_l14_n11full_verdict.md` | 19,697 | 2026-09-29 16:25:57 | `8eef73bf9856` |
| 725 | `results/_v4_supp_l14v3_batch10_r1_executor.py` | 56,894 | 2026-09-26 16:32:01 | `d4dd5c949443` |
| 726 | `results/_v4_supp_l14v3_batch10_r1_result.json` | 68,329 | 2026-09-26 16:36:02 | `14dddb13d658` |
| 727 | `results/_v4_supp_l14v3_batch10_r2_executor.py` | 58,073 | 2026-09-26 16:49:05 | `bb601b4f5ecb` |
| 728 | `results/_v4_supp_l14v3_batch10_r2_result.json` | 69,460 | 2026-09-26 16:53:10 | `400ee4d21fc9` |
| 729 | `results/_v4_supp_l14v3_batch10_r3_executor.py` | 58,539 | 2026-09-26 16:56:53 | `eef1475e325c` |
| 730 | `results/_v4_supp_l14v3_batch10_r3_result.json` | 70,658 | 2026-09-26 17:00:02 | `88a06f08928f` |
| 731 | `results/_v4_supp_l14v3_batch10_r4_executor.py` | 68,856 | 2026-09-26 17:06:19 | `4f68937d7a95` |
| 732 | `results/_v4_supp_l14v3_batch10_r4_result.json` | 74,733 | 2026-09-26 17:09:13 | `9d91a8dc039a` |
| 733 | `results/_v4_supp_l14v3_batch10_r5_result.json` | 74,979 | 2026-09-26 17:18:27 | `7f02e08fc0da` |
| 734 | `results/_v4_supp_l14v3_batch1_executor.py` | 29,354 | 2026-09-24 20:45:39 | `b48019494530` |
| 735 | `results/_v4_supp_l14v3_batch1_r2_executor.py` | 29,598 | 2026-09-24 21:00:44 | `2bdb5163400f` |
| 736 | `results/_v4_supp_l14v3_batch1_r2_result.json` | 40,815 | 2026-09-24 21:11:40 | `00c7b545c397` |
| 737 | `results/_v4_supp_l14v3_batch1_r3_executor.py` | 43,289 | 2026-09-24 21:15:11 | `60c78b6f0281` |
| 738 | `results/_v4_supp_l14v3_batch1_r3_result.json` | 44,888 | 2026-09-24 21:25:24 | `6e01255b80c9` |
| 739 | `results/_v4_supp_l14v3_batch1_r4_executor.py` | 46,811 | 2026-09-24 21:28:35 | `4f5269ba8f18` |
| 740 | `results/_v4_supp_l14v3_batch1_r4_result.json` | 46,927 | 2026-09-24 21:38:53 | `9c800874701a` |
| 741 | `results/_v4_supp_l14v3_batch1_r5_executor.py` | 49,138 | 2026-09-24 21:43:59 | `91c72f8ad209` |
| 742 | `results/_v4_supp_l14v3_batch1_r5_result.json` | 67,897 | 2026-09-24 21:54:45 | `664355f29ab9` |
| 743 | `results/_v4_supp_l14v3_batch1_r6_executor.py` | 47,242 | 2026-09-24 21:59:06 | `5f02c7e0f094` |
| 744 | `results/_v4_supp_l14v3_batch1_r6_result.json` | 57,925 | 2026-09-25 00:27:42 | `6b92bbff7180` |
| 745 | `results/_v4_supp_l14v3_batch1_result.json` | 46,518 | 2026-09-24 20:56:34 | `22eb01144062` |
| 746 | `results/_v4_supp_l14v3_batch2_r1_executor.py` | 50,808 | 2026-09-24 22:34:16 | `e52f930654d3` |
| 747 | `results/_v4_supp_l14v3_batch2_r1_result.json` | 4,128 | 2026-09-24 22:35:43 | `d245ae4ce385` |
| 748 | `results/_v4_supp_l14v3_batch2_r2_executor.py` | 55,317 | 2026-09-24 22:44:56 | `e7418f47a130` |
| 749 | `results/_v4_supp_l14v3_batch2_r2_models_probe.json` | 1,503 | 2026-09-24 22:40:12 | `3c9dc60b5071` |
| 750 | `results/_v4_supp_l14v3_batch2_r2_result.json` | 62,887 | 2026-09-24 22:51:00 | `8c125e257af8` |
| 751 | `results/_v4_supp_l14v3_batch2_r3_executor.py` | 56,467 | 2026-09-24 23:12:40 | `72fd2bb3838e` |
| 752 | `results/_v4_supp_l14v3_batch2_r3_result.json` | 62,886 | 2026-09-24 23:23:19 | `25251aca6d79` |
| 753 | `results/_v4_supp_l14v3_batch2_r4_executor.py` | 58,176 | 2026-09-24 23:26:12 | `d9fe7aa2d292` |
| 754 | `results/_v4_supp_l14v3_batch2_r4_result.json` | 63,572 | 2026-09-24 23:30:50 | `15b8ddc5ba9e` |
| 755 | `results/_v4_supp_l14v3_batch2_r5_executor.py` | 60,046 | 2026-09-27 20:26:47 | `bf1e4fe02402` |
| 756 | `results/_v4_supp_l14v3_batch2_r5_result.json` | 64,285 | 2026-09-24 23:39:39 | `479f4119cf72` |
| 757 | `results/_v4_supp_l14v3_batch2_r6_result.json` | 65,083 | 2026-09-24 23:50:52 | `e37d9c74c3e5` |
| 758 | `results/_v4_supp_l14v3_batch3_r1_executor.py` | 61,899 | 2026-09-27 20:26:47 | `0c284a3dce21` |
| 759 | `results/_v4_supp_l14v3_batch3_r1_result.json` | 66,520 | 2026-09-24 23:38:45 | `d24b84671c23` |
| 760 | `results/_v4_supp_l14v3_batch3_r2_executor.py` | 64,634 | 2026-09-27 20:26:47 | `b1699098c53b` |
| 761 | `results/_v4_supp_l14v3_batch3_r2_result.json` | 67,767 | 2026-09-24 23:51:13 | `58e9c55a770d` |
| 762 | `results/_v4_supp_l14v3_batch3_r3_executor.py` | 66,396 | 2026-09-27 20:26:47 | `3b7381ce5fe8` |
| 763 | `results/_v4_supp_l14v3_batch3_r3_result.json` | 68,488 | 2026-09-25 00:01:27 | `6e677ffcc880` |
| 764 | `results/_v4_supp_l14v3_batch3_r4_executor.py` | 68,874 | 2026-09-25 01:01:33 | `c79b5c274a10` |
| 765 | `results/_v4_supp_l14v3_batch3_r4_result.json` | 69,635 | 2026-09-25 01:05:56 | `0e47768640d3` |
| 766 | `results/_v4_supp_l14v3_batch3_r5_result.json` | 70,064 | 2026-09-25 01:23:36 | `38998f994b84` |
| 767 | `results/_v4_supp_l14v3_batch4_r1_executor.py` | 66,097 | 2026-09-24 23:35:04 | `e84bffd5dc7d` |
| 768 | `results/_v4_supp_l14v3_batch4_r1_result.json` | 71,775 | 2026-09-24 23:41:34 | `7d9fe9d319a2` |
| 769 | `results/_v4_supp_l14v3_batch4_r2_executor.py` | 66,774 | 2026-09-24 23:49:42 | `7d8e12267790` |
| 770 | `results/_v4_supp_l14v3_batch4_r2_result.json` | 71,998 | 2026-09-24 23:55:28 | `6a9a362d9869` |
| 771 | `results/_v4_supp_l14v3_batch4_r3_executor.py` | 68,560 | 2026-09-25 00:02:06 | `b5e1c3637405` |
| 772 | `results/_v4_supp_l14v3_batch4_r3_result.json` | 72,884 | 2026-09-25 00:08:49 | `ed5267df7d6f` |
| 773 | `results/_v4_supp_l14v3_batch4_r4_executor.py` | 73,379 | 2026-09-25 01:08:47 | `184186902a9f` |
| 774 | `results/_v4_supp_l14v3_batch4_r4_result.json` | 74,448 | 2026-09-25 01:20:35 | `41e0ba55e205` |
| 775 | `results/_v4_supp_l14v3_batch4_r5_executor.py` | 78,984 | 2026-09-25 01:27:34 | `8a505613b476` |
| 776 | `results/_v4_supp_l14v3_batch4_r5_result.json` | 76,138 | 2026-09-25 01:34:21 | `bad01f2b89fd` |
| 777 | `results/_v4_supp_l14v3_batch4_r6_executor.py` | 80,877 | 2026-09-25 01:44:02 | `7f2c5e26e6c5` |
| 778 | `results/_v4_supp_l14v3_batch4_r6_result.json` | 32,369 | 2026-09-25 01:44:37 | `6b8093ff8962` |
| 779 | `results/_v4_supp_l14v3_batch5_r1_executor.py` | 63,517 | 2026-09-27 20:26:47 | `dac0648507b9` |
| 780 | `results/_v4_supp_l14v3_batch5_r1_result.json` | 71,021 | 2026-09-24 23:36:37 | `120d45d1774f` |
| 781 | `results/_v4_supp_l14v3_batch5_r2_executor.py` | 66,252 | 2026-09-27 20:26:47 | `4c40334929bb` |
| 782 | `results/_v4_supp_l14v3_batch5_r2_result.json` | 72,550 | 2026-09-24 23:52:24 | `b0f76b5c3522` |
| 783 | `results/_v4_supp_l14v3_batch5_r3_executor.py` | 66,454 | 2026-09-27 20:26:47 | `ed9557830f8b` |
| 784 | `results/_v4_supp_l14v3_batch5_r3_result.json` | 73,682 | 2026-09-25 00:03:51 | `8e2acdacfa1e` |
| 785 | `results/_v4_supp_l14v3_batch5_r4_executor.py` | 67,894 | 2026-09-25 01:01:38 | `28844c34b12b` |
| 786 | `results/_v4_supp_l14v3_batch5_r4_result.json` | 74,100 | 2026-09-25 01:04:23 | `1c62520c372b` |
| 787 | `results/_v4_supp_l14v3_batch5_r5_executor.py` | 77,033 | 2026-09-25 01:08:52 | `82c283d8f37a` |
| 788 | `results/_v4_supp_l14v3_batch5_r5_result.json` | 77,137 | 2026-09-25 01:11:16 | `c874d21a4cbe` |
| 789 | `results/_v4_supp_l14v3_batch6_r1_executor.py` | 49,296 | 2026-09-25 00:28:11 | `ad35565f1ec9` |
| 790 | `results/_v4_supp_l14v3_batch6_r1_result.json` | 57,799 | 2026-09-25 00:39:57 | `0d29e1ab4ae2` |
| 791 | `results/_v4_supp_l14v3_batch6_r2_executor.py` | 53,494 | 2026-09-25 01:01:58 | `93c931fc3b1c` |
| 792 | `results/_v4_supp_l14v3_batch6_r2_result.json` | 64,672 | 2026-09-25 01:14:34 | `96e1de46ed30` |
| 793 | `results/_v4_supp_l14v3_batch6_r3_executor.py` | 53,717 | 2026-09-25 01:27:17 | `1385d2ca356f` |
| 794 | `results/_v4_supp_l14v3_batch6_r3_result.json` | 64,975 | 2026-09-25 01:38:53 | `15a7fecdffe7` |
| 795 | `results/_v4_supp_l14v3_batch6_r4_executor.py` | 54,588 | 2026-09-25 01:42:04 | `08f329b36e9d` |
| 796 | `results/_v4_supp_l14v3_batch6_r4_result.json` | 65,254 | 2026-09-25 01:53:14 | `b7377ba019a1` |
| 797 | `results/_v4_supp_l14v3_batch6_r5_executor.py` | 57,783 | 2026-09-25 01:56:05 | `8a8babb911b8` |
| 798 | `results/_v4_supp_l14v3_batch6_r5_result.json` | 65,651 | 2026-09-25 02:07:09 | `e40424bf8abe` |
| 799 | `results/_v4_supp_l14v3_batch7_r1_executor.py` | 51,545 | 2026-09-25 02:13:59 | `c49fc9bca8c4` |
| 800 | `results/_v4_supp_l14v3_batch7_r1_result.json` | 61,114 | 2026-09-25 02:18:50 | `3558a1d15867` |
| 801 | `results/_v4_supp_l14v3_batch7_r2_executor.py` | 53,145 | 2026-09-25 02:26:48 | `35cda0c0f7da` |
| 802 | `results/_v4_supp_l14v3_batch7_r2_result.json` | 61,458 | 2026-09-25 02:31:15 | `924f12c4e7ab` |
| 803 | `results/_v4_supp_l14v3_batch7_r3_executor.py` | 51,271 | 2026-09-25 02:41:04 | `5c0b426e2ee0` |
| 804 | `results/_v4_supp_l14v3_batch7_r3_result.json` | 61,389 | 2026-09-25 02:46:39 | `b431a1ba54df` |
| 805 | `results/_v4_supp_l14v3_batch7_r4_executor.py` | 51,289 | 2026-09-25 03:06:20 | `d789f9bd4fa1` |
| 806 | `results/_v4_supp_l14v3_batch7_r4_result.json` | 61,824 | 2026-09-25 03:13:45 | `0fe4c1339d88` |
| 807 | `results/_v4_supp_l14v3_batch7_r5_result.json` | 61,658 | 2026-09-25 03:29:41 | `09a481ebca6b` |
| 808 | `results/_v4_supp_l14v3_batch8_r1_executor.py` | 56,181 | 2026-09-25 02:21:24 | `1e5f2249c517` |
| 809 | `results/_v4_supp_l14v3_batch8_r1_result.json` | 62,531 | 2026-09-25 02:21:40 | `e6a94a0a13b7` |
| 810 | `results/_v4_supp_l14v3_batch8_r2_executor.py` | 57,634 | 2026-09-25 02:35:52 | `6a9bbc43c808` |
| 811 | `results/_v4_supp_l14v3_batch8_r2_result.json` | 63,440 | 2026-09-25 02:36:27 | `7b23996b5f4c` |
| 812 | `results/_v4_supp_l14v3_batch8_r3_executor.py` | 58,494 | 2026-09-25 02:50:01 | `0f654d945f12` |
| 813 | `results/_v4_supp_l14v3_batch8_r3_result.json` | 63,670 | 2026-09-25 03:00:00 | `56faf9324fba` |
| 814 | `results/_v4_supp_l14v3_batch8_r4_executor.py` | 59,351 | 2026-09-25 03:13:26 | `6b69ec8406d4` |
| 815 | `results/_v4_supp_l14v3_batch8_r4_result.json` | 64,038 | 2026-09-25 03:18:20 | `c7d5aa2a9b00` |
| 816 | `results/_v4_supp_l14v3_batch8_r5_executor.py` | 60,475 | 2026-09-25 03:32:20 | `6961281824ae` |
| 817 | `results/_v4_supp_l14v3_batch8_r5_result.json` | 63,785 | 2026-09-25 03:37:47 | `3620a7daf9c1` |
| 818 | `results/_v4_supp_l14v3_batch9_r1_executor.py` | 60,645 | 2026-09-26 16:38:53 | `e78ca71bd077` |
| 819 | `results/_v4_supp_l14v3_batch9_r1_result.json` | 69,251 | 2026-09-26 16:38:42 | `7e8dfe0156cd` |
| 820 | `results/_v4_supp_l14v3_batch9_r2_executor.py` | 60,580 | 2026-09-26 16:48:39 | `7eec235a9ca2` |
| 821 | `results/_v4_supp_l14v3_batch9_r2_result.json` | 69,325 | 2026-09-26 16:56:40 | `08b0aaaae726` |
| 822 | `results/_v4_supp_l14v3_batch9_r3_executor.py` | 62,131 | 2026-09-26 17:01:28 | `cfe41dd4fe62` |
| 823 | `results/_v4_supp_l14v3_batch9_r3_result.json` | 69,984 | 2026-09-26 17:08:33 | `29e0d865a7bf` |
| 824 | `results/_v4_supp_l14v3_batch9_r4_executor.py` | 64,538 | 2026-09-26 17:14:29 | `1b3fcfbacd59` |
| 825 | `results/_v4_supp_l14v3_batch9_r4_result.json` | 71,093 | 2026-09-26 17:23:11 | `eb8b13d9f592` |
| 826 | `results/_v4_supp_l14v3_batch9_r5_result.json` | 72,047 | 2026-09-26 17:34:59 | `1610f5060ef1` |
| 827 | `results/_v4_supp_l14v3_model_mapping_2026_09_24.md` | 49,326 | 2026-09-30 16:15:20 | `9ba12a0fbac1` |
| 828 | `results/_v4_supp_l14v3_n26_verdict.md` | 65,978 | 2026-09-30 16:15:20 | `df6453d57f8a` |
| 829 | `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md` | 62,847 | 2026-09-30 16:15:20 | `e7c3e2ef4e6b` |
| 830 | `results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md` | 21,309 | 2026-09-24 20:34:15 | `843e42ef4d2a` |
| 831 | `results/_v4_supp_prereg_v02_add_T15_2026_09_24.md` | 76,991 | 2026-09-24 23:48:31 | `8898b964a9d9` |
| 832 | `results/_v4_supp_prereg_v02_add_T15_activation_2026_09_24.md` | 20,751 | 2026-09-24 23:48:54 | `443efb39804a` |
| 833 | `results/_v4_supp_prereg_v02_add_T15r2_2026_09_26.md` | 97,059 | 2026-09-26 16:38:20 | `883dced872b4` |
| 834 | `results/_v4_supp_prereg_v02_add_T15r2_activation_2026_09_26.md` | 34,195 | 2026-09-26 16:36:21 | `f6ed61c25572` |
| 835 | `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` | 52,942 | 2026-09-24 20:29:16 | `802dece2286a` |
| 836 | `results/_v4_supp_prereg_v02_add_T1_activation_2026_09_24.md` | 14,234 | 2026-09-24 20:27:29 | `79936b630015` |
| 837 | `results/_v4_supp_t15_executor.py` | 62,285 | 2026-09-24 23:57:30 | `558e635f9ba6` |
| 838 | `results/_v4_supp_t15_executor_r0_atomic_2026_09_29.py` | 66,317 | 2026-09-29 11:12:41 | `7da23c0e94cf` |
| 839 | `results/_v4_supp_t15_executor_r1_2026_09_27.py` | 67,517 | 2026-09-27 20:51:43 | `6d22444c65af` |
| 840 | `results/_v4_supp_t15_executor_r2_atomic_2026_09_28.py` | 70,056 | 2026-09-28 15:46:02 | `9e89e021ea03` |
| 841 | `results/_v4_supp_t15_executor_r3_2026_09_28.py` | 70,056 | 2026-09-28 17:25:01 | `b86cce242abe` |
| 842 | `results/_v4_supp_t15_result.json` | 53,265 | 2026-09-25 00:44:39 | `6b47d389b7ae` |
| 843 | `results/_v4_supp_t15_verdict.md` | 54,377 | 2026-09-30 16:15:20 | `3cb5c2f59961` |
| 844 | `results/_v4_supp_t15r2_executor.py` | 84,884 | 2026-09-26 16:50:49 | `4b5b720d5cda` |
| 845 | `results/_v4_supp_t15r2_executor_r0_atomic_2026_09_29.py` | 89,083 | 2026-09-29 11:12:41 | `678032f726a8` |
| 846 | `results/_v4_supp_t15r2_executor_r1_2026_09_28.py` | 90,390 | 2026-09-28 15:14:04 | `e0936a68fa82` |
| 847 | `results/_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py` | 92,915 | 2026-09-28 15:44:50 | `215db16a0556` |
| 848 | `results/_v4_supp_t15r2_executor_r3_2026_09_28.py` | 92,915 | 2026-09-28 17:25:01 | `4f514b3fb4b8` |
| 849 | `results/_v4_supp_t15r2_result.json` | 73,526 | 2026-09-26 17:15:40 | `c69ab0e3002e` |
| 850 | `results/_v4_supp_t15r2_verdict.md` | 65,638 | 2026-09-30 16:15:20 | `963725dbd82a` |
| 851 | `results/_v4_supp_t1_executor.py` | 60,563 | 2026-09-27 20:26:47 | `91b8f70e4e18` |
| 852 | `results/_v4_supp_t1_result.json` | 82,365 | 2026-09-24 22:32:37 | `d6cb03a4657e` |
| 853 | `results/_v4_supp_t1_verdict.md` | 29,106 | 2026-09-30 16:15:20 | `0ad42625f333` |
| 854 | `results/_v4_track2_multimodel_rerun.py` | 38,719 | 2026-09-27 20:26:47 | `5c0983eaaf11` |
| 855 | `results/_v4_track2_multimodel_rerun_2026_09_23.json` | 35,011 | 2026-09-23 15:26:47 | `e3dae2a4bbc2` |
| 856 | `results/_v4_track2_multimodel_verdict_2026_09_23.md` | 12,883 | 2026-09-23 15:27:54 | `44d9bad9039b` |
| 857 | `results/_v5_b15_pp1_impl_fix_2026_09_29.md` | 12,911 | 2026-09-29 17:33:06 | `ded842b6241c` |
| 858 | `results/_v5_bulk_activation_2026_09_28.md` | 39,378 | 2026-09-30 17:02:47 | `b5a50447b4da` |
| 859 | `results/_v5_c3_reading_b_prereg_2026_09_28.md` | 32,178 | 2026-09-30 17:02:47 | `8dcf5e1e6dde` |
| 860 | `results/_v5_checkpoint_tail3_revision_2026_09_29.md` | 27,966 | 2026-09-29 11:24:06 | `c962851ff3ff` |
| 861 | `results/_v5_clearance_mr14_rerun_note_2026_09_29.md` | 22,894 | 2026-09-29 19:12:01 | `f3dd5efd3e34` |
| 862 | `results/_v5_closing_register_2026_09_28.md` | 27,224 | 2026-09-30 17:02:47 | `522b08506290` |
| 863 | `results/_v5_confirm_b11_decisions_register_2026_09_29.md` | 12,276 | 2026-09-29 14:20:13 | `07e9fe512da5` |
| 864 | `results/_v5_confirm_b14_b15_decisions_register_2026_09_29.md` | 26,154 | 2026-09-29 15:21:25 | `e48276a8dd31` |
| 865 | `results/_v5_confirm_b5_decisions_register_2026_09_29.md` | 45,525 | 2026-09-29 13:43:30 | `3b5f2819af8f` |
| 866 | `results/_v5_confirm_b7_decisions_register_2026_09_29.md` | 23,833 | 2026-09-29 14:04:02 | `0a80ae035042` |
| 867 | `results/_v5_confirm_b9_decisions_register_2026_09_29.md` | 17,008 | 2026-09-29 14:13:01 | `8c510cda6014` |
| 868 | `results/_v5_exec_f2_r3_register_2026_09_29.md` | 24,177 | 2026-09-29 10:54:17 | `9d64ee1d6996` |
| 869 | `results/_v5_fake_verdict_session_log_2026_09_28.md` | 18,877 | 2026-09-30 17:02:47 | `132bfa0c02f5` |
| 870 | `results/_v5_fake_verdict_v1x_prereg_2026_09_28.md` | 28,484 | 2026-09-30 17:02:47 | `088085d6c90d` |
| 871 | `results/_v5_gt4_reattrib_2026_09_29.json` | 3,074 | 2026-09-29 11:18:07 | `4b75df5f7454` |
| 872 | `results/_v5_gt5_gt6_gt8_gt5b_gt_prereg_2026_09_28.md` | 63,447 | 2026-09-28 20:14:25 | `2505ff5d203f` |
| 873 | `results/_v5_gt5_reattrib_2026_09_29.json` | 5,626 | 2026-09-29 11:18:07 | `e15b3b171d60` |
| 874 | `results/_v5_gt5b_reattrib_2026_09_29.json` | 7,084 | 2026-09-29 11:18:07 | `212e5bb8c7d7` |
| 875 | `results/_v5_gt6_trajint_2026_09_29.json` | 83,722 | 2026-09-29 11:18:07 | `578fbeaa4635` |
| 876 | `results/_v5_gt8_expand_2026_09_29.json` | 20,090 | 2026-09-29 11:18:07 | `34ff826f97c2` |
| 877 | `results/_v5_gt8_lowarm_exec_2026_09_29.md` | 21,542 | 2026-09-29 15:34:42 | `365ea6cb77e8` |
| 878 | `results/_v5_gt8_lowarm_result_2026_09_29.json` | 26,253 | 2026-09-29 15:21:52 | `c68076c88140` |
| 879 | `results/_v5_gt8_lowarm_resultA_cb132cd5_2026_09_29.json` | 28,638 | 2026-09-29 15:29:24 | `24b0d5eda48a` |
| 880 | `results/_v5_gt8_lowarm_resultb_2026_09_29.json` | 48,948 | 2026-09-29 15:32:44 | `8aa69a5e922d` |
| 881 | `results/_v5_gt8_lowarm_seta_verify_2026_09_29.json` | 9,001 | 2026-09-29 15:33:32 | `d1370b0a3853` |
| 882 | `results/_v5_gt_exec_2026_09_29.md` | 27,701 | 2026-09-29 11:21:06 | `9a679f43f796` |
| 883 | `results/_v5_gt_p10_lowarm_prereg_2026_09_29.md` | 38,464 | 2026-09-29 13:58:52 | `07e28e2fe374` |
| 884 | `results/_v5_gt_verdict_2026_09_29.md` | 57,227 | 2026-09-29 11:41:25 | `45648b0ec940` |
| 885 | `results/_v5_item21_anchor_recompute_2026_09_28.json` | 9,527 | 2026-09-28 20:03:28 | `47177cab0303` |
| 886 | `results/_v5_item21_anchor_recompute_2026_09_28.md` | 9,221 | 2026-09-28 20:04:46 | `e5623d4bd3f3` |
| 887 | `results/_v5_item21_patched_recompute_2026_09_28.json` | 14,879 | 2026-09-28 20:26:23 | `aa53e5db77c9` |
| 888 | `results/_v5_item21_strategyqa_realias_recompute_2026_09_29.json` | 34,314 | 2026-09-29 16:17:02 | `49f068c716a8` |
| 889 | `results/_v5_item26b_attribution_effective_2026_09_28.md` | 35,261 | 2026-09-28 22:29:35 | `c353fbcdc753` |
| 890 | `results/_v5_item26b_endpoint_definition_prereg_2026_09_28.md` | 38,939 | 2026-09-28 21:32:27 | `5e59a11466db` |
| 891 | `results/_v5_item26b_literal_gap_prereg_v2_2026_09_28.md` | 38,885 | 2026-09-28 20:24:02 | `bb0a211fa675` |
| 892 | `results/_v5_item35_prereg_v2_2026_09_28.md` | 35,633 | 2026-09-28 22:22:11 | `1fb2419c6e96` |
| 893 | `results/_v5_item35_v2_matrix_exec_2026_09_29.md` | 24,624 | 2026-09-29 12:27:44 | `4e88682284d8` |
| 894 | `results/_v5_item35_v2_matrix_result_2026_09_29.json` | 84,699 | 2026-09-29 12:27:24 | `13ad5b740f80` |
| 895 | `results/_v5_item35_v2_verdict_2026_09_29.md` | 26,232 | 2026-09-29 12:56:02 | `b59bef293712` |
| 896 | `results/_v5_item35_v3_collinear_prereg_2026_09_29.md` | 42,504 | 2026-09-29 13:56:34 | `873652fd39dd` |
| 897 | `results/_v5_item35_v3_collinear_recompute_2026_10_01.json` | 49,682 | 2026-10-01 08:55:37 | `a210e2c41275` |
| 898 | `results/_v5_item35_v3_collinear_result_2026_09_29.json` | 187,287 | 2026-09-29 14:29:52 | `99f3e504589e` |
| 899 | `results/_v5_pjpm_pc_closeout_readout_2026_09_29.md` | 32,243 | 2026-09-29 13:46:56 | `1b9ac6b07670` |
| 900 | `results/_v5_pjpm_pc_deg_prereg_2026_09_29.md` | 59,446 | 2026-09-29 12:17:51 | `989ee2bce660` |
| 901 | `results/_v5_pjpm_pc_degen_precheck_result_2026_09_29.json` | 103,747 | 2026-09-29 13:46:56 | `3641afe9d49c` |
| 902 | `results/_v5_r2h2_residual_merged_catalogue_2026_09_29.md` | 50,554 | 2026-09-29 14:29:32 | `b62d19c1c7cc` |
| 903 | `results/_v5_sub_artifact_ledger_2026_09_28.md` | 71,818 | 2026-09-30 17:02:47 | `dd38c77ea486` |
| 904 | `results/_v5_track2_qwen_retry_2026_09_29.json` | 2,735 | 2026-09-29 11:10:33 | `6acafe021aaf` |
| 905 | `results/_v5_trae_doubt6_verify_2026_09_28_r3verifier.md` | 30,192 | 2026-09-30 17:02:47 | `58101ef93a6f` |
| 906 | `results/_v5_v3_deg_c5_b_raw_embeddings_2026_09_29.json` | 744,352 | 2026-10-01 09:21:49 | `1088fdd2b197` |
| 907 | `results/_v5_v3_deg_c5_proposal_2026_09_29.md` | 33,356 | 2026-09-29 13:25:19 | `2158b11bba9a` |
| 908 | `results/_v5_v3_deg_fix_c1c4_result_2026_09_29.json` | 266,417 | 2026-09-29 12:11:14 | `1b5bfecc818e` |
| 909 | `results/_v5_v3_deg_fix_exec_2026_09_29.md` | 30,261 | 2026-09-29 12:10:05 | `7d885528f287` |
| 910 | `results/_v5_v3_deg_fix_prereg_2026_09_29.md` | 41,622 | 2026-09-29 11:44:32 | `98286cc1aec7` |
| 911 | `results/_v5_v3_deg_p1_reopen_result_2026_09_29.json` | 571,451 | 2026-09-29 13:41:39 | `b86d6740d487` |
| 912 | `results/_v5_v3_deg_reopen_line_2026_09_29.md` | 42,778 | 2026-09-29 13:17:28 | `2ea1c2cee65d` |
| 913 | `results/_v5r_s40_recompute_2026_09_29.json` | 4,992 | 2026-09-29 19:19:15 | `5be465342ae1` |
| 914 | `results/boss_pa_1_rbr_rm_result_2026_09_15.json` | 8,753 | 2026-09-15 15:28:10 | `c7c59e0d2f6c` |
| 915 | `results/boss_pa_2_potential_game_result_2026_09_15.json` | 7,530 | 2026-09-15 15:28:10 | `5c76137d6430` |
| 916 | `results/boss_pa_3_replicator_dynamics_result_2026_09_15.json` | 9,098 | 2026-09-15 15:28:10 | `d6f233d73c45` |
| 917 | `results/boss_pc_1_a1_resampling_2026_09_15.json` | 1,017 | 2026-09-15 13:34:48 | `d21912a05d79` |
| 918 | `results/boss_pc_1_real_2d_ising_2026_09_15.json` | 2,460 | 2026-09-15 15:28:00 | `43d9ce160fc8` |
| 919 | `results/boss_pc_2_a2_fitting_2026_09_15.json` | 1,024 | 2026-09-15 13:34:48 | `5a880678c386` |
| 920 | `results/boss_pc_2_real_transverse_ising_2026_09_15.json` | 3,553 | 2026-09-15 15:27:35 | `8933d61b180a` |
| 921 | `results/boss_pc_3_a3_clipping_2026_09_15.json` | 1,265 | 2026-09-15 13:34:48 | `d74d6b39d1b0` |
| 922 | `results/boss_pc_3_real_reservoir_2026_09_15.json` | 2,364 | 2026-09-15 15:28:00 | `94b5398be76c` |
| 923 | `results/boss_pe_1_real_2d_ising_2026_09_15.json` | 2,460 | 2026-09-15 13:34:49 | `43d9ce160fc8` |
| 924 | `results/boss_pe_2_real_transverse_ising_2026_09_15.json` | 3,553 | 2026-09-15 13:34:49 | `8933d61b180a` |
| 925 | `results/boss_pe_3_real_reservoir_2026_09_15.json` | 2,364 | 2026-09-15 13:34:49 | `94b5398be76c` |
| 926 | `results/c5_b_group_fix_readings_2026_10_01.json` | 9,996 | 2026-10-01 09:25:22 | `2a7749da7c4d` |
| 927 | `results/c5_b_group_fix_readings_2026_10_09.json` | 10,029 | 2026-10-09 13:39:57 | `4e415990b71d` |
| 928 | `results/c5_b_group_root_candidate_2026_10_01.md` | 28,867 | 2026-10-01 09:24:13 | `2fd8946cfe80` |
| 929 | `results/c5_guard_0_1_recheck_verdict_2026_10_01.md` | 33,287 | 2026-10-01 10:21:29 | `24418fa60ede` |
| 930 | `results/c5_guard_minmaxstd_readings_2026_10_01.json` | 19,935 | 2026-10-01 10:14:10 | `7ff301514f66` |
| 931 | `results/c5_guard_minmaxstd_report_2026_10_01.md` | 19,909 | 2026-10-01 10:15:08 | `f465fbdb7579` |
| 932 | `results/d7_5anchor_60cells_9model_verdict_2026_09_18.json` | 2,456 | 2026-09-16 11:00:06 | `4505cca79c15` |
| 933 | `results/deposon_benchmark_v1_3_details.json` | 656,572 | 2026-08-23 00:01:28 | `9fcb6b243e0d` |
| 934 | `results/deposon_benchmark_v1_3_simple.json` | 2,245 | 2026-08-23 00:01:28 | `9347add72401` |
| 935 | `results/deposon_benchmark_v1_3_traps.json` | 3,112 | 2026-08-23 00:01:28 | `82eb64151f2b` |
| 936 | `results/deposon_benchmark_v1_4_gsm8k.json` | 2,741 | 2026-08-23 05:00:55 | `5cd6269d7baf` |
| 937 | `results/deposon_benchmark_v1_4_gsm8k_details.json` | 208,350 | 2026-08-23 05:00:55 | `39f79fce7cdb` |
| 938 | `results/deposon_benchmark_v1_4_strategyqa.json` | 1,691 | 2026-08-23 13:04:23 | `b51fd24586b3` |
| 939 | `results/deposon_benchmark_v1_4_strategyqa_details.json` | 235,779 | 2026-09-16 11:01:12 | `a63ebea7b29a` |
| 940 | `results/deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json` | 13,562 | 2026-09-15 13:35:18 | `4e4a17d43adf` |
| 941 | `results/deposon_cpath_simulation_2026_09_10.json` | 6,351 | 2026-09-10 20:44:37 | `9466fdbf9c95` |
| 942 | `results/deposon_d_fix2_metric_verify_9m60c_2026_09_15.json` | 204,441 | 2026-09-16 11:01:12 | `9f88a212a77c` |
| 943 | `results/deposon_deepseek_v41_flash_30cells_v3_2026_09_10.json` | 18,592 | 2026-09-10 16:40:43 | `56401317e62b` |
| 944 | `results/deposon_dpath_cross_modal_2026_09_10.json` | 75,964 | 2026-09-16 11:01:12 | `ab0c2eaff0d1` |
| 945 | `results/deposon_dpath_cross_modal_runner_2026_09_10.py` | 27,930 | 2026-09-16 11:01:12 | `fb20a6ba5ec6` |
| 946 | `results/deposon_feshbach_rag_30cells_2026_09_10.py` | 14,343 | 2026-09-16 11:01:12 | `a072e4184e83` |
| 947 | `results/deposon_g1_mindmap_demo.json` | 3,041 | 2026-08-23 05:00:55 | `55428f6bd848` |
| 948 | `results/deposon_g2_boltzmann_pathintegral.json` | 2,204 | 2026-08-23 05:00:55 | `9fd0f3399ab3` |
| 949 | `results/deposon_g2_boltzmann_pathintegral_rewrite.json` | 2,782 | 2026-08-23 09:40:33 | `f36667e5b5b8` |
| 950 | `results/deposon_game_theory_eval_2026_09_10.json` | 10,096 | 2026-09-10 21:53:17 | `3fa0ff2c8c08` |
| 951 | `results/deposon_gpt6_teamorouter_2026_09_10.json` | 3,827 | 2026-09-10 16:49:38 | `f44636f5f72f` |
| 952 | `results/deposon_gpt6_teamorouter_30cells_2026_09_10.json` | 18,290 | 2026-09-10 17:30:03 | `ea38ee252701` |
| 953 | `results/deposon_gsm8k_stratified.json` | 3,411 | 2026-08-23 09:40:34 | `8b7574b25336` |
| 954 | `results/deposon_openrouter_5model_rag_30cells_2026_09_10.json` | 111,710 | 2026-09-10 23:34:43 | `2e55c53be25d` |
| 955 | `results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json` | 18,104 | 2026-09-16 18:39:54 | `b5873afb9d29` |
| 956 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` | 20,398 | 2026-10-01 09:43:44 | `33ad1c01f745` |
| 957 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json` | 21,176 | 2026-10-09 13:39:49 | `95f3f0957be8` |
| 958 | `results/deposon_p_k_cross_subject_fingerprint_blind_test_2026_09_16.json` | 11,341 | 2026-09-16 18:39:55 | `576eaf8d7431` |
| 959 | `results/deposon_pa_d1_d3_2026_09_15.json` | 15,604 | 2026-09-15 11:29:23 | `e221792715f8` |
| 960 | `results/deposon_pc_d1_d3_2026_09_15.json` | 20,408 | 2026-09-15 11:01:56 | `b2046af03610` |
| 961 | `results/deposon_pe_d1_d3_2026_09_15.json` | 17,085 | 2026-09-15 10:49:09 | `594d7a8d3de8` |
| 962 | `results/deposon_pf_d1_full_9m5c_2026_09_15.json` | 33,829 | 2026-09-16 11:01:12 | `fcb5105df0b6` |
| 963 | `results/deposon_pf_implementation_2026_09_11.json` | 27,311 | 2026-09-16 11:01:12 | `509dcee3b139` |
| 964 | `results/deposon_pg_v01_9m60c_2026_09_15.json` | 11,512 | 2026-09-15 13:35:24 | `ab75889ee738` |
| 965 | `results/deposon_risk1_02940_decision_2026_09_11.json` | 4,336 | 2026-09-15 10:22:25 | `2dc8ca9e36c1` |
| 966 | `results/deposon_risk2_canonical5_decision_2026_09_11.json` | 4,066 | 2026-09-15 10:22:26 | `cf4a882160e1` |
| 967 | `results/deposon_risk3_seff_decision_2026_09_11.json` | 6,488 | 2026-09-15 10:22:26 | `67867e752f47` |
| 968 | `results/deposon_v15_diffusion.json` | 519,387 | 2026-08-23 19:21:32 | `c16d1768d1ca` |
| 969 | `results/deposon_v15_diffusion_maxpath_negativeresult.json` | 416,460 | 2026-08-23 19:21:32 | `00ee97c82dcc` |
| 970 | `results/deposon_v15_diffusion_summary.json` | 6,079 | 2026-08-23 19:22:36 | `5b95d06e66b0` |
| 971 | `results/deposon_v16_llm_prior.json` | 39,974 | 2026-08-23 20:21:38 | `c17b31ae4f3b` |
| 972 | `results/deposon_v16_paired_stats.json` | 9,176 | 2026-08-23 20:59:51 | `20bc4288e0de` |
| 973 | `results/deposon_v17_fixed_sampler.json` | 106,317 | 2026-08-23 21:38:59 | `701ad291a714` |
| 974 | `results/deposon_v17_fusion_fix.json` | 106,164 | 2026-08-23 21:31:41 | `af51da229652` |
| 975 | `results/deposon_v17_fusion_fix_tieartifact_negativeresult.json` | 106,125 | 2026-08-23 21:31:36 | `556086d9e3bc` |
| 976 | `results/deposon_v17_multigraph.json` | 16,896 | 2026-08-23 21:34:43 | `2836605ca12f` |
| 977 | `results/deposon_v18_api_supplements.json` | 80,624 | 2026-08-23 23:20:04 | `62c1a41e1db8` |
| 978 | `results/deposon_v19_benchmark_fixes.json` | 409,104 | 2026-08-24 01:11:01 | `910c4333eead` |
| 979 | `results/deposon_v19_fullrank.json` | 42,458 | 2026-08-24 01:04:04 | `fbbfd3ef3890` |
| 980 | `results/deposon_v19_meanfield.json` | 44,443 | 2026-08-24 01:02:01 | `108da40d5d4e` |
| 981 | `results/deposon_v19_quickwins.json` | 7,842 | 2026-08-24 01:07:59 | `1ec7aba6afd8` |
| 982 | `results/deposon_v1_implementation_calculator_2026_09_10.py` | 10,751 | 2026-09-10 22:21:56 | `121f104012f4` |
| 983 | `results/deposon_v20_baselines.json` | 16,987 | 2026-08-29 01:17:30 | `6edb2aec1660` |
| 984 | `results/deposon_v20_bigquiz_eval.json` | 35,718 | 2026-08-28 23:54:14 | `283dbc8c5b63` |
| 985 | `results/deposon_v20_corpus_eval.json` | 631,644 | 2026-08-29 01:21:14 | `ca71aa6858e1` |
| 986 | `results/deposon_v20_cot_quiz.json` | 7,101 | 2026-08-28 21:13:05 | `94fd018b5cc8` |
| 987 | `results/deposon_v20_crossval.json` | 8,404 | 2026-08-28 20:27:06 | `76479b7a5ed6` |
| 988 | `results/deposon_v20_familyl_ingest.json` | 1,303 | 2026-08-28 17:38:45 | `676eb83edc27` |
| 989 | `results/deposon_v20_fastcheck.json` | 1,768 | 2026-08-28 22:08:40 | `a1ef105b0269` |
| 990 | `results/deposon_v20_gt.json` | 3,803 | 2026-08-28 17:43:00 | `497b9c2d6746` |
| 991 | `results/deposon_v20_gt2b.json` | 123,331 | 2026-08-29 19:57:39 | `a2ae7997ee67` |
| 992 | `results/deposon_v20_gt3.json` | 7,844 | 2026-08-29 15:03:29 | `35b676773243` |
| 993 | `results/deposon_v20_gt5.json` | 72,647 | 2026-08-29 15:35:11 | `fca14c5735dd` |
| 994 | `results/deposon_v20_gt5b.json` | 56,425 | 2026-08-29 15:44:55 | `2907006dbe48` |
| 995 | `results/deposon_v20_gt6.json` | 65,105 | 2026-08-29 15:45:04 | `04b90b638bdc` |
| 996 | `results/deposon_v20_gt7.json` | 17,925 | 2026-08-29 17:57:57 | `896589b673ec` |
| 997 | `results/deposon_v20_gt8.json` | 5,396 | 2026-08-29 19:34:34 | `2b88948dca19` |
| 998 | `results/deposon_v20_gt8b.json` | 2,706 | 2026-08-30 10:28:49 | `6339ea4e500c` |
| 999 | `results/deposon_v20_gt8b_ingest.json` | 986 | 2026-08-30 10:28:44 | `aa077cc1725e` |
| 1000 | `results/deposon_v20_gt8c.json` | 2,864 | 2026-08-30 16:17:46 | `9b16fa802ef8` |
| 1001 | `results/deposon_v20_gt8c_ingest.json` | 1,018 | 2026-08-30 16:17:42 | `4b11b1bd8ada` |
| 1002 | `results/deposon_v20_photonics.json` | 6,796 | 2026-08-29 01:19:15 | `0b7893196d0b` |
| 1003 | `results/deposon_v20_quiz_eval.json` | 22,623 | 2026-08-28 20:46:44 | `9194ee703218` |
| 1004 | `results/deposon_v20_vector_audit.json` | 915 | 2026-08-28 21:15:08 | `b9b65c568842` |
| 1005 | `results/deposon_v21_gtformal.json` | 69,204 | 2026-08-30 15:44:09 | `9d9ae5001c57` |
| 1006 | `results/deposon_v22_e95ci.json` | 1,496 | 2026-08-30 21:45:29 | `928bcfbdb7c3` |
| 1007 | `results/deposon_v22_p1c.json` | 763 | 2026-08-30 21:59:28 | `2bed4de3a57c` |
| 1008 | `results/deposon_v2_phase1_60cells_2026_09_11.json` | 85,508 | 2026-09-16 11:01:12 | `a18bbc703b42` |
| 1009 | `results/deposon_v2_phase3_strip_embeddings_2026_09_11.json` | 2,398,383 | 2026-09-11 11:33:43 | `1ded6731cc27` |
| 1010 | `results/deposon_v2_phase4_f4_2026_09_11.json` | 5,212 | 2026-09-11 11:17:21 | `cf7682348617` |
| 1011 | `results/deposon_v3_physical_opt_2026_09_11.json` | 17,591 | 2026-09-11 12:05:53 | `27f9bd5cc260` |
| 1012 | `results/deposon_v3_physical_opt_60cells_2026_09_11.json` | 17,732 | 2026-09-15 10:19:42 | `c659695aa23c` |
| 1013 | `results/deposon_v3_v7_summary_2026_09_11.json` | 25,049 | 2026-09-16 11:01:12 | `063ac8d00542` |
| 1014 | `results/deposon_v42_v2_miss_rate_curve_2026_09_16.json` | 24,435 | 2026-09-16 18:27:36 | `0a8ed127d6de` |
| 1015 | `results/deposon_volcengine_22caption_embedding_2026_09_10.json` | 4,559 | 2026-09-10 17:36:46 | `c4b774c8e34c` |
| 1016 | `results/deposon_volcengine_9model_30cells_2026_09_10.json` | 4,894 | 2026-09-16 11:01:12 | `58ab335ca341` |
| 1017 | `results/deposon_volcengine_glm_latest_30cells_v2_2026_09_10.json` | 32,995 | 2026-09-16 11:01:12 | `4ec04d3d7d8c` |
| 1018 | `results/deposon_volcengine_glm_latest_5cells_2026_09_10.json` | 4,895 | 2026-09-16 11:01:12 | `83c35597af81` |
| 1019 | `results/deposon_volcengine_glm_latest_5cells_2026_09_10.py` | 8,112 | 2026-09-16 11:01:12 | `a3ca05aec6fb` |
| 1020 | `results/deposon_volcengine_glm_latest_5cells_v2_2026_09_10.json` | 6,466 | 2026-09-16 11:01:12 | `0c3ede881fb1` |
| 1021 | `results/deposon_volcengine_minimax_m3_30cells_2026_09_10.json` | 23,472 | 2026-09-16 18:20:55 | `fbb7677b9cd5` |
| 1022 | `results/deposon_volcengine_minimax_m3_30cells_2026_09_10.py` | 11,703 | 2026-09-16 18:20:55 | `218ef1a99f97` |
| 1023 | `results/deposon_volcengine_seed_code_30cells_2026_09_10.json` | 23,034 | 2026-09-16 11:01:12 | `5149f5cafcf9` |
| 1024 | `results/deposon_volcengine_worker_a_2026_09_10.json` | 25,464 | 2026-09-16 11:01:12 | `506810017d34` |
| 1025 | `results/deposon_volcengine_worker_b_2026_09_10.json` | 49,338 | 2026-09-16 11:01:12 | `b1eb668377ce` |
| 1026 | `results/deposon_volcengine_worker_b_2026_09_10.py` | 13,232 | 2026-09-16 11:01:12 | `401dfd3c27f3` |
| 1027 | `results/deposon_volcengine_worker_c_2026_09_10.json` | 51,716 | 2026-09-16 11:01:12 | `f6f172820c97` |
| 1028 | `results/deposon_volcengine_worker_c_2026_09_10.py` | 11,692 | 2026-09-16 11:01:12 | `b5eeef1e9bd7` |
| 1029 | `results/deposon_volcengine_worker_d_2026_09_10.json` | 20,280 | 2026-09-16 11:01:12 | `fae79888344b` |
| 1030 | `reviews/data/t1_potential.csv` | 4,833 | 2026-08-28 21:30:52 | `e110a020954f` |
| 1031 | `reviews/data/t1b_classics.csv` | 5,450 | 2026-08-28 21:32:04 | `82016e695f48` |
| 1032 | `reviews/data/t1c_loglinear.csv` | 5,566 | 2026-08-28 21:33:20 | `c50ff98a95cc` |
| 1033 | `reviews/data/t1d_pagerank.csv` | 4,167 | 2026-08-28 21:36:57 | `8b1a9e5113bb` |
| 1034 | `reviews/data/t2_linkpred.csv` | 6,750 | 2026-08-28 21:30:43 | `19555b7d9d43` |
| 1035 | `reviews/data/t2b_linkpred.csv` | 5,520 | 2026-08-28 21:31:15 | `6de8f0e651c4` |
| 1036 | `reviews/data/t2c_advlink.csv` | 6,886 | 2026-08-28 21:32:32 | `67d1d8342060` |
| 1037 | `reviews/data/t2d_hiding.csv` | 5,377 | 2026-08-28 21:33:27 | `5749ce2c5bf7` |
| 1038 | `reviews/data/t2e_nettack.csv` | 1,875 | 2026-08-28 21:35:25 | `2628f74421f2` |
| 1039 | `reviews/data/t2f_waniek.csv` | 1,271 | 2026-08-28 21:35:28 | `f0d2c9d2a39b` |
| 1040 | `reviews/data/t3_mechdesign.csv` | 6,680 | 2026-08-28 21:31:20 | `6e8b6e4730a8` |
| 1041 | `reviews/data/t3b_verifiable.csv` | 6,731 | 2026-08-28 21:32:32 | `f48c9f09a3b4` |
| 1042 | `reviews/data/t3d_llmmd.csv` | 3,405 | 2026-08-28 21:35:31 | `49028967ad57` |
| 1043 | `reviews/data/t3e_commit.csv` | 3,691 | 2026-08-28 21:36:14 | `bf0a2b544a74` |
| 1044 | `reviews/data/t4_poa.csv` | 6,567 | 2026-08-28 21:31:59 | `8ba9fada9ead` |
| 1045 | `reviews/deep_probe_R1.md` | 14,895 | 2026-08-29 01:04:00 | `190dd5df9af2` |
| 1046 | `reviews/deep_probe_R2.md` | 23,391 | 2026-08-29 01:10:13 | `a4f8a55b70ba` |
| 1047 | `reviews/design_probe_v19.md` | 13,967 | 2026-08-24 00:49:48 | `c41f1717310e` |
| 1048 | `reviews/experiment_design_v19.md` | 8,840 | 2026-08-24 00:35:44 | `56ecef878539` |
| 1049 | `reviews/independent_review_20260823.md` | 1,724 | 2026-08-23 21:40:22 | `7474fc258375` |
| 1050 | `reviews/literature_scan_v19.md` | 28,449 | 2026-08-24 00:40:36 | `70ea38d5b9c0` |
| 1051 | `reviews/literature_scan_v2X_A.md` | 18,876 | 2026-08-28 21:42:49 | `d0bba9379b4b` |
| 1052 | `reviews/literature_scan_v2X_B.md` | 30,468 | 2026-08-28 21:50:11 | `313b30815a39` |
| 1053 | `reviews/peer_review_v19_A.md` | 24,409 | 2026-08-24 00:36:05 | `28878116d87b` |
| 1054 | `reviews/peer_review_v19_B.md` | 42,672 | 2026-08-24 01:07:19 | `da98f9e310d4` |
| 1055 | `reviews/post_draft_verification_v2X.md` | 9,979 | 2026-08-29 21:06:20 | `0c49f2d36088` |
| 1056 | `reviews/post_edit_verification_v19.md` | 19,327 | 2026-08-24 07:49:36 | `e262e9d684fe` |
| 1057 | `reviews/review_coach_v2X_draft.md` | 23,468 | 2026-08-29 22:22:13 | `0bafe659c00d` |
| 1058 | `reviews/review_coach_v2X_draft_r2.md` | 15,721 | 2026-08-29 23:42:38 | `67162ab18f9a` |
| 1059 | `reviews/review_coach_v2X_outline.md` | 11,295 | 2026-08-29 15:34:49 | `5bebb5e1d329` |
| 1060 | `reviews/review_format_v2X.md` | 6,656 | 2026-08-30 04:02:12 | `2dc4b45424ab` |
| 1061 | `reviews/review_realign_v2X.md` | 7,338 | 2026-08-30 01:03:56 | `3ecb285db3d8` |
| 1062 | `run_benchmark_v1_3.py` | 10,690 | 2026-08-23 00:30:44 | `54ea2644df14` |
| 1063 | `run_benchmark_v1_4_gsm8k.py` | 11,253 | 2026-08-24 01:05:38 | `fac50b283da5` |
| 1064 | `run_benchmark_v1_4_strategyqa.py` | 14,537 | 2026-08-30 10:26:51 | `f523875a15db` |
| 1065 | `run_g2_ensemble.py` | 8,907 | 2026-08-23 09:40:07 | `e3914712a984` |
| 1066 | `run_v15_experiment.py` | 22,761 | 2026-08-30 04:56:14 | `58a5623f3aa1` |
| 1067 | `run_v16_llm_prior.py` | 13,423 | 2026-08-30 04:56:13 | `6350bbaecb81` |
| 1068 | `run_v17_fixed_sampler.py` | 10,435 | 2026-08-23 21:38:54 | `3e54797eedeb` |
| 1069 | `run_v17_fusion_fix.py` | 10,236 | 2026-08-23 21:31:25 | `b592470c47ae` |
| 1070 | `run_v17_multigraph.py` | 5,682 | 2026-08-23 21:33:45 | `ca7e6031272c` |
| 1071 | `run_v18_api_supplements.py` | 42,681 | 2026-08-23 23:19:13 | `aef28d92d763` |
| 1072 | `run_v19_benchmark_fixes.py` | 22,802 | 2026-08-24 01:10:53 | `674c2e5349cf` |
| 1073 | `run_v19_fullrank.py` | 8,976 | 2026-08-30 04:56:31 | `8d1067e4e27b` |
| 1074 | `run_v19_meanfield.py` | 11,690 | 2026-08-30 04:56:31 | `67ef3779478a` |
| 1075 | `run_v19_quickwins.py` | 10,509 | 2026-08-24 01:07:34 | `93958a96b19a` |
| 1076 | `run_v20_baselines.py` | 12,435 | 2026-08-29 01:14:15 | `1b9815fad7ca` |
| 1077 | `run_v20_bigquiz_eval.py` | 9,091 | 2026-08-28 23:54:08 | `1c1a82f4b48a` |
| 1078 | `run_v20_bigquiz_fetch.py` | 7,808 | 2026-08-30 10:16:33 | `f810f3a34eb2` |
| 1079 | `run_v20_corpus_eval.py` | 20,470 | 2026-08-28 17:41:03 | `2fad3b28d34c` |
| 1080 | `run_v20_cot_fetch.py` | 3,323 | 2026-08-30 10:14:35 | `b4a214c4e50f` |
| 1081 | `run_v20_crossval_eval.py` | 14,379 | 2026-08-28 20:26:46 | `1cdc6c37b236` |
| 1082 | `run_v20_crossval_fetch.py` | 4,958 | 2026-08-30 10:15:16 | `3465b43e2f8a` |
| 1083 | `run_v20_familyL_fetch.py` | 2,088 | 2026-08-30 10:14:03 | `ff38dbb3de7f` |
| 1084 | `run_v20_familyL_ingest.py` | 6,108 | 2026-08-29 01:14:15 | `c5d96c1f0522` |
| 1085 | `run_v20_fastcheck.py` | 7,243 | 2026-08-28 22:07:04 | `b6585a30d808` |
| 1086 | `run_v20_gt.py` | 9,824 | 2026-08-28 17:14:47 | `9f6df7e94cdc` |
| 1087 | `run_v20_gt2b.py` | 9,076 | 2026-08-29 19:57:30 | `361aff516219` |
| 1088 | `run_v20_gt3_eval.py` | 6,983 | 2026-08-29 15:02:33 | `6a234eee29b3` |
| 1089 | `run_v20_gt3_fetch.py` | 3,858 | 2026-08-30 10:11:34 | `1853f7e82a3a` |
| 1090 | `run_v20_gt3b_fetch.py` | 3,135 | 2026-08-30 10:12:06 | `efaa93762269` |
| 1091 | `run_v20_gt3c_fetch.py` | 3,193 | 2026-08-30 10:13:37 | `48b659b95984` |
| 1092 | `run_v20_gt5.py` | 14,957 | 2026-08-30 10:18:23 | `32c03f5739d7` |
| 1093 | `run_v20_gt5b.py` | 10,419 | 2026-08-30 10:19:10 | `3b344435f4ea` |
| 1094 | `run_v20_gt6.py` | 11,010 | 2026-08-29 15:43:45 | `c5dcdb0f12e2` |
| 1095 | `run_v20_gt7.py` | 17,509 | 2026-08-30 10:20:37 | `38071308e9ef` |
| 1096 | `run_v20_gt8.py` | 13,876 | 2026-08-29 19:33:18 | `d07233229279` |
| 1097 | `run_v20_gt8b_eval.py` | 9,196 | 2026-08-29 22:27:23 | `07b74332ebc2` |
| 1098 | `run_v20_gt8b_fetch.py` | 6,558 | 2026-08-30 10:34:04 | `fce719ad054d` |
| 1099 | `run_v20_gt8b_ingest.py` | 5,676 | 2026-08-29 22:24:05 | `5e3db6f4869d` |
| 1100 | `run_v20_gt8c_eval.py` | 9,594 | 2026-08-30 15:52:41 | `6d6db8bdbb06` |
| 1101 | `run_v20_gt8c_fetch.py` | 8,068 | 2026-08-30 15:51:03 | `8079a5dbe251` |
| 1102 | `run_v20_gt8c_ingest.py` | 5,866 | 2026-08-30 15:51:41 | `81690a38f421` |
| 1103 | `run_v20_photonics.py` | 7,615 | 2026-08-29 01:19:14 | `ec00cb18f95a` |
| 1104 | `run_v20_quizbank.py` | 8,744 | 2026-08-28 20:46:28 | `3b2a7dd2044c` |
| 1105 | `run_v20_vector_audit.py` | 4,717 | 2026-08-28 21:14:03 | `16a270a6bdab` |
| 1106 | `run_v21_gtformal.py` | 16,600 | 2026-08-30 15:35:54 | `9bbe43f41fa8` |
| 1107 | `run_v22_e95ci.py` | 3,058 | 2026-08-30 21:26:23 | `8470e3ce8cae` |
| 1108 | `run_v22_p1c.py` | 7,236 | 2026-08-30 18:28:58 | `6e9673205dc0` |
| 1109 | `scripts/run_deepseek_v41_30cells_v2.py` | 14,017 | 2026-09-10 16:15:10 | `c7411ae13ec0` |
| 1110 | `scripts/run_deepseek_v41_30cells_v3.py` | 13,955 | 2026-09-10 16:38:40 | `03bc34ea88a8` |
| 1111 | `scripts/run_deepseek_v41_60cells_v2_startup.py` | 16,071 | 2026-09-10 17:31:43 | `769e1d04503b` |
| 1112 | `scripts/run_embedding_dual_smoke.py` | 13,599 | 2026-09-10 17:03:53 | `9253225de974` |
| 1113 | `scripts/run_v3x_6way_stage3_recovery.py` | 15,872 | 2026-09-10 18:03:01 | `e4f96f2e9e4f` |
| 1114 | `scripts/run_v3x_6way_verification.py` | 25,060 | 2026-09-10 17:55:59 | `27a046d569d1` |
| 1115 | `scripts/run_v3x_finalize.py` | 5,932 | 2026-09-10 18:15:09 | `46787531bf8e` |
| 1116 | `scripts/run_v3x_stage3_minimal.py` | 12,477 | 2026-09-10 18:07:56 | `8b5d42772d5e` |
| 1117 | `scripts/run_v41_flash_5cells_fix.py` | 17,914 | 2026-09-10 16:54:23 | `e4546d734a53` |
| 1118 | `scripts/run_volcengine_seed_code_30cells.py` | 13,924 | 2026-09-16 11:01:12 | `75002485aa94` |
| 1119 | `svg_mindmap_ingest.py` | 8,811 | 2026-08-23 05:00:55 | `fa661fd759ed` |
| 1120 | `tests/test_agents_merge.py` | 26,615 | 2026-08-30 10:34:38 | `c7cc85ffb3f0` |
| 1121 | `tests/test_diffusion.py` | 12,463 | 2026-08-23 19:21:32 | `2452be26af7e` |
| 1122 | `tests/test_fast.py` | 3,653 | 2026-08-28 22:11:59 | `5829f89c2352` |
| 1123 | `tests/test_fingerprint_v0.py` | 13,788 | 2026-09-01 16:35:59 | `506ba4a55704` |
| 1124 | `tests/test_gt_common.py` | 3,697 | 2026-08-30 10:29:22 | `6a2f32d1316a` |
| 1125 | `tests/test_llm_fetch.py` | 11,095 | 2026-08-30 10:28:46 | `90772f5cf41b` |
| 1126 | `tests/test_llm_prior.py` | 7,701 | 2026-08-23 20:02:35 | `11c2ffa37610` |
| 1127 | `tests/test_new_modes.py` | 21,275 | 2026-08-23 09:40:33 | `0b2276028391` |
| 1128 | `tests/test_protocol.py` | 6,979 | 2026-08-30 04:58:18 | `f103c9d87c61` |
| 1129 | `tests/test_v18.py` | 17,093 | 2026-08-23 23:15:42 | `c523ae4b0989` |
| 1130 | `tests/test_v19.py` | 6,056 | 2026-08-24 01:10:27 | `b44e2945fa31` |
| 1131 | `tests/test_v19_benchmark.py` | 7,371 | 2026-08-24 01:12:52 | `f343754f380c` |
| 1132 | `tests/test_v20.py` | 13,249 | 2026-08-28 17:19:09 | `e4712875f65d` |
| 1133 | `tests/test_v20_gt2b.py` | 4,318 | 2026-08-29 19:58:34 | `4cd18ae1d3dc` |
| 1134 | `tests/test_v20_gt5.py` | 5,746 | 2026-08-29 15:36:51 | `1f104b13a170` |
| 1135 | `tests/test_v20_gt5b.py` | 2,423 | 2026-08-29 15:44:42 | `81feb1f137b4` |
| 1136 | `tests/test_v20_gt6.py` | 2,584 | 2026-08-29 15:44:43 | `5c7dd774a3f3` |
| 1137 | `tests/test_v20_gt7.py` | 6,489 | 2026-08-29 17:56:48 | `e8727f8f42da` |
| 1138 | `tests/test_v20_gt8.py` | 5,122 | 2026-08-29 19:34:11 | `b9479374de4d` |
| 1139 | `tests/test_v20_gt8b.py` | 10,109 | 2026-08-29 22:27:24 | `3c4395df9311` |
| 1140 | `tests/test_v20_gt8c.py` | 13,458 | 2026-08-30 15:55:13 | `562dd8b920bc` |
| 1141 | `tests/test_v21_gtformal.py` | 7,376 | 2026-08-30 15:20:33 | `74650b1d603b` |
| 1142 | `tests/test_v22_p1c.py` | 3,854 | 2026-08-30 18:30:56 | `b19bdb965cc0` |
| 1143 | `tools/exp_harness.py` | 10,090 | 2026-09-09 16:16:50 | `275e480ba4d9` |
| 1144 | `tools/llm_client.py` | 8,118 | 2026-09-09 16:16:02 | `1722500da4aa` |
| 1145 | `tools/make_figures_v2.py` | 21,073 | 2026-08-30 20:52:09 | `0dc3ea09f42d` |
| 1146 | `tools/make_figures_v2_en.py` | 21,188 | 2026-08-30 20:46:55 | `b4e880a6af33` |
| 1147 | `tools/read_key.py` | 1,047 | 2026-09-10 14:45:46 | `a9b56c4e775f` |
| 1148 | `verifier/_build_partial.py` | 7,160 | 2026-09-16 11:01:12 | `04fcd95c70f1` |
| 1149 | `verifier/_read_summary.py` | 1,231 | 2026-09-10 20:50:17 | `b4d89f052875` |
| 1150 | `verifier/_run.log` | 7,190 | 2026-09-10 21:03:13 | `e148d7bf11e1` |
| 1151 | `verifier/_test_one.py` | 2,564 | 2026-09-16 11:01:12 | `893641fd9e25` |
| 1152 | `verifier/_worker_a_run.log` | 4,532 | 2026-09-10 21:29:39 | `9df22377dc55` |
| 1153 | `verifier/audit/conservation.py` | 22,105 | 2026-09-10 09:29:22 | `4bdec2683f06` |
| 1154 | `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | 6,680 | 2026-09-09 13:19:32 | `03c6c01f3697` |
| 1155 | `verifier/handoff/KT_ABC1_anchors_sha256_12.root_session_11318B.bak_2026_09_23.json` | 11,318 | 2026-09-22 11:02:01 | `6e9cd8cd8e07` |
| 1156 | `verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json` | 5,049 | 2026-09-15 13:31:24 | `da517c115f3c` |
| 1157 | `verifier/handoff/P_F_PREDECISION_2026_09_09.json` | 3,680 | 2026-09-09 13:50:15 | `b41c98bf90cc` |
| 1158 | `verifier/handoff/P_F_PREDECISION_2026_09_11_V0.1.json` | 12,498 | 2026-09-11 13:08:54 | `312d635e6259` |
| 1159 | `verifier/kill_lines/kt_b1_kill_decision.py` | 2,781 | 2026-09-09 13:17:24 | `9f351078e5bf` |
| 1160 | `verifier/README.md` | 14,360 | 2026-08-30 17:08:56 | `d76f2dc473be` |
| 1161 | `verifier/run_volcengine_9model_30cells.py` | 12,050 | 2026-09-16 11:01:12 | `54f8033cfb29` |
| 1162 | `verifier/runs/2026-09-04_pd_v0.jsonl` | 100 | 2026-09-04 13:33:46 | `5042869bdf85` |
| 1163 | `verifier/runs/20260823.log` | 1,197 | 2026-08-23 20:24:15 | `f8d8db6a4d8b` |
| 1164 | `verifier/runs/20260823T022721Z.log` | 7 | 2026-08-23 10:27:21 | `cf205dbb8cea` |
| 1165 | `verifier/runs/20260823T130229Z.log` | 839 | 2026-08-23 21:02:31 | `1af06784d975` |
| 1166 | `verifier/runs/20260823T130254Z.log` | 839 | 2026-08-23 21:02:55 | `8316e03518f2` |
| 1167 | `verifier/runs/20260823T130326Z.log` | 819 | 2026-08-23 21:03:27 | `e8698e422d69` |
| 1168 | `verifier/runs/20260823T130405Z.log` | 576 | 2026-08-23 21:04:08 | `d6071ff9493e` |
| 1169 | `verifier/runs/20260823T131053Z.log` | 911 | 2026-08-23 21:10:55 | `94e578649599` |
| 1170 | `verifier/runs/20260823T134128Z.log` | 910 | 2026-08-23 21:41:34 | `6cf95aade825` |
| 1171 | `verifier/runs/20260823T134305Z.log` | 972 | 2026-08-23 21:43:08 | `c9ae2079fc1f` |
| 1172 | `verifier/runs/20260823T154658Z.log` | 1,536 | 2026-08-23 23:47:08 | `1fca45290883` |
| 1173 | `verifier/runs/v10_run1.md` | 701 | 2026-08-24 07:51:43 | `54be4344e99a` |
| 1174 | `verifier/runs/v11_run1.md` | 514 | 2026-08-28 17:57:42 | `bd36f361ea12` |
| 1175 | `verifier/runs/v12_run1.md` | 788 | 2026-08-28 20:01:49 | `927eafcb3b0b` |
| 1176 | `verifier/runs/v13_run1.md` | 145 | 2026-08-28 20:30:14 | `aa1456d217fc` |
| 1177 | `verifier/runs/v14_run1.md` | 145 | 2026-08-28 20:48:36 | `3fdca6c35dcb` |
| 1178 | `verifier/runs/v15_run1.md` | 475 | 2026-08-28 21:17:49 | `634ef5fa4ef8` |
| 1179 | `verifier/runs/v16_run1.md` | 359 | 2026-08-28 21:54:50 | `e6bf3b753ff6` |
| 1180 | `verifier/runs/v17_run1.md` | 283 | 2026-08-28 22:51:36 | `9d0332c44044` |
| 1181 | `verifier/runs/v18_run1.md` | 276 | 2026-08-28 23:57:39 | `4a3ce944cce3` |
| 1182 | `verifier/runs/v19_run1.md` | 297 | 2026-08-29 00:25:02 | `7b95dbd3f168` |
| 1183 | `verifier/runs/v20_run1.md` | 295 | 2026-08-29 00:35:08 | `41d3d7f4a148` |
| 1184 | `verifier/runs/v21_run1.md` | 247 | 2026-08-29 01:26:03 | `36b69e195f06` |
| 1185 | `verifier/runs/v21_run2.md` | 448 | 2026-08-29 11:35:00 | `3246c7d46480` |
| 1186 | `verifier/runs/v22_run1.md` | 436 | 2026-08-29 11:22:52 | `582531ccd67d` |
| 1187 | `verifier/runs/v23_run1.md` | 586 | 2026-08-29 15:09:59 | `9578066064cc` |
| 1188 | `verifier/runs/v24_run1.md` | 498 | 2026-08-29 15:50:05 | `67fd4fec19f2` |
| 1189 | `verifier/runs/v25_run1.md` | 526 | 2026-08-29 18:00:55 | `b81e2fb0ea28` |
| 1190 | `verifier/runs/v26_run1.md` | 546 | 2026-08-29 19:39:05 | `09b69c05bb47` |
| 1191 | `verifier/runs/v27_run1.md` | 559 | 2026-08-29 20:02:00 | `0759457758be` |
| 1192 | `verifier/runs/v27_run2.md` | 554 | 2026-08-29 20:03:11 | `82a92d9ce191` |
| 1193 | `verifier/runs/v28_run1.md` | 771 | 2026-08-29 21:09:29 | `6d85472d724c` |
| 1194 | `verifier/runs/v29_run1.md` | 440 | 2026-08-29 23:03:33 | `26a667edec7a` |
| 1195 | `verifier/runs/v29_run2.md` | 627 | 2026-08-29 23:05:27 | `badd1ed95a6d` |
| 1196 | `verifier/runs/v30_run1.md` | 735 | 2026-08-29 23:47:50 | `cef68a7a30a5` |
| 1197 | `verifier/runs/v30_run2.md` | 787 | 2026-08-29 23:49:54 | `d22151b9ad6d` |
| 1198 | `verifier/runs/v30_run3.md` | 771 | 2026-08-29 23:51:37 | `0dc553ed64c2` |
| 1199 | `verifier/runs/v31_run1.md` | 673 | 2026-08-30 01:08:22 | `dcb11fefabf2` |
| 1200 | `verifier/runs/v31_run2.md` | 747 | 2026-08-30 01:10:29 | `8727c88269f3` |
| 1201 | `verifier/runs/v32_run1.md` | 859 | 2026-08-30 03:57:46 | `1798c48acea7` |
| 1202 | `verifier/runs/v32_run2.md` | 894 | 2026-08-30 03:59:13 | `83c987fb96d9` |
| 1203 | `verifier/runs/v32_run3.md` | 886 | 2026-08-30 04:06:01 | `4a99a1134c8c` |
| 1204 | `verifier/runs/v33_run1.md` | 2,160 | 2026-08-30 05:05:50 | `9e917334781c` |
| 1205 | `verifier/runs/v33_run2.md` | 1,783 | 2026-08-30 05:12:50 | `158948a53671` |
| 1206 | `verifier/runs/v34_run1.md` | 83 | 2026-08-30 09:57:16 | `03f773f08fa7` |
| 1207 | `verifier/runs/v34_run2.md` | 118 | 2026-08-30 14:13:30 | `d9bfaae6d08b` |
| 1208 | `verifier/runs/v35_run1.md` | 39 | 2026-08-30 15:47:20 | `a693c838ae57` |
| 1209 | `verifier/runs/v35_run2.md` | 118 | 2026-08-30 17:08:56 | `11ce6990b84a` |
| 1210 | `verifier/runs/v36_runs.log` | 106 | 2026-09-17 23:20:46 | `18668f3d7d58` |
| 1211 | `verifier/runs/v37_runs.log` | 124 | 2026-09-17 23:20:46 | `f0de3de22eae` |
| 1212 | `verifier/runs/v38_runs.log` | 271 | 2026-09-17 23:20:47 | `0fc3395dac12` |
| 1213 | `verifier/runs/v39_runs.log` | 173 | 2026-09-17 23:20:48 | `73b035b4fc3c` |
| 1214 | `verifier/runs/v40_runs.log` | 133 | 2026-09-17 23:20:48 | `0e511b4e6caa` |
| 1215 | `verifier/runs/v41_2026-08-30_run1.txt` | 158 | 2026-09-17 23:20:49 | `e156e87caba8` |
| 1216 | `verifier/runs/v42_2026-08-30_run1.txt` | 279 | 2026-09-17 23:20:49 | `8fde2819ef29` |
| 1217 | `verifier/runs/v42_2026-08-30_run2.txt` | 156 | 2026-09-17 23:20:50 | `1aa0257caac9` |
| 1218 | `verifier/runs/v43_2026-09-01_run1.txt` | 199 | 2026-09-17 23:20:51 | `aa82005b05de` |
| 1219 | `verifier/v1/check.py` | 2,976 | 2026-08-23 10:27:37 | `03bc1adfc82f` |
| 1220 | `verifier/v10/check.py` | 5,261 | 2026-08-24 07:15:04 | `4fd5fdd754c0` |
| 1221 | `verifier/v11/check.py` | 2,767 | 2026-08-28 17:56:50 | `3b8682a7e562` |
| 1222 | `verifier/v12/check.py` | 4,142 | 2026-08-29 01:14:15 | `87c9c883e3bf` |
| 1223 | `verifier/v13/check.py` | 3,495 | 2026-08-28 20:29:43 | `1159facab6db` |
| 1224 | `verifier/v14/check.py` | 3,278 | 2026-08-28 20:48:03 | `4ba223d2185d` |
| 1225 | `verifier/v15/check.py` | 3,231 | 2026-08-28 21:17:37 | `be0f2bbab0a2` |
| 1226 | `verifier/v16/check.py` | 2,691 | 2026-08-28 21:54:41 | `223082632a1d` |
| 1227 | `verifier/v17/check.py` | 2,897 | 2026-08-28 22:51:15 | `679792be51ed` |
| 1228 | `verifier/v17/erratum.md` | 438 | 2026-08-29 01:26:03 | `50f15f7ea3dc` |
| 1229 | `verifier/v18/check.py` | 3,180 | 2026-08-29 01:14:16 | `6abdda4f7400` |
| 1230 | `verifier/v19/check.py` | 1,995 | 2026-08-29 00:24:42 | `c53cf72d085b` |
| 1231 | `verifier/v2/check.py` | 2,510 | 2026-08-23 19:21:32 | `af3a78983537` |
| 1232 | `verifier/v20/check.py` | 2,790 | 2026-08-29 00:33:07 | `9d0f1e950dee` |
| 1233 | `verifier/v20/erratum.md` | 316 | 2026-08-29 01:26:03 | `35081d39f35b` |
| 1234 | `verifier/v21/check.py` | 3,702 | 2026-08-29 01:23:52 | `5e7d7435c4a3` |
| 1235 | `verifier/v22/check.py` | 2,857 | 2026-08-29 11:20:44 | `f16beaae5675` |
| 1236 | `verifier/v23/check.py` | 2,659 | 2026-08-29 15:08:00 | `9ecb25362c9a` |
| 1237 | `verifier/v24/check.py` | 3,124 | 2026-08-29 15:49:47 | `e6c7513d54f3` |
| 1238 | `verifier/v25/check.py` | 2,576 | 2026-08-29 18:00:10 | `cc6ff5453e06` |
| 1239 | `verifier/v26/check.py` | 2,595 | 2026-09-16 11:01:12 | `c58a9652a42a` |
| 1240 | `verifier/v27/check.py` | 2,132 | 2026-09-16 11:01:12 | `118524c7e808` |
| 1241 | `verifier/v28/check.py` | 2,201 | 2026-09-16 11:01:12 | `b73a6b268f64` |
| 1242 | `verifier/v29/check.py` | 2,124 | 2026-09-16 11:01:12 | `5923e2c379f6` |
| 1243 | `verifier/v3/check.py` | 2,544 | 2026-08-23 19:21:32 | `02a5a86d38bf` |
| 1244 | `verifier/v30/check.py` | 2,565 | 2026-09-16 11:01:12 | `2cf46f79a669` |
| 1245 | `verifier/v31/check.py` | 2,185 | 2026-09-16 11:01:12 | `e5bb0020e500` |
| 1246 | `verifier/v32/check.py` | 2,551 | 2026-09-16 11:01:12 | `399bfc743f24` |
| 1247 | `verifier/v33/check.py` | 6,019 | 2026-08-30 05:11:44 | `32fefc485326` |
| 1248 | `verifier/v34/check.py` | 3,715 | 2026-08-30 09:57:03 | `0bbd226cd2ae` |
| 1249 | `verifier/v35/check.py` | 2,385 | 2026-08-30 15:47:20 | `2130a5f5e1bf` |
| 1250 | `verifier/v36/check.sh` | 968 | 2026-09-18 13:43:52 | `2212dcd98cd1` |
| 1251 | `verifier/v37/check.sh` | 1,141 | 2026-09-18 13:43:52 | `ced43b5f8800` |
| 1252 | `verifier/v38/check.sh` | 1,705 | 2026-09-17 23:20:52 | `43b501c5c20d` |
| 1253 | `verifier/v39/check.sh` | 1,935 | 2026-09-17 23:20:53 | `d48ac555761f` |
| 1254 | `verifier/v4/check.py` | 3,205 | 2026-08-23 19:33:47 | `f058e85c5383` |
| 1255 | `verifier/v40/check.sh` | 1,604 | 2026-09-17 23:20:54 | `7b15cd2f4c7e` |
| 1256 | `verifier/v41/check.sh` | 1,687 | 2026-09-17 23:20:54 | `2c9fe869daaa` |
| 1257 | `verifier/v42/check.sh` | 1,509 | 2026-09-17 23:20:55 | `3ea87e2cfc61` |
| 1258 | `verifier/v43/check.sh` | 1,224 | 2026-09-17 23:20:55 | `71b83217032d` |
| 1259 | `verifier/v5/check.py` | 2,255 | 2026-08-23 20:04:44 | `3d776381f665` |
| 1260 | `verifier/v6/check.py` | 2,757 | 2026-08-23 20:23:46 | `8366078a10e4` |
| 1261 | `verifier/v7/check.py` | 4,300 | 2026-08-23 21:03:13 | `a70a68037d92` |
| 1262 | `verifier/v8/check.py` | 3,210 | 2026-08-23 21:40:59 | `01b63b1a9c5f` |
| 1263 | `verifier/v9/check.py` | 5,352 | 2026-08-23 23:46:50 | `5faad917d839` |

### §4.2 区 `_repo_mirror`（1,187 件 ／ 58,731,756 bytes）

**逐目录分布**

| 目录 | 件数 | bytes | 类别 |
|:--|--:|--:|:--|
| `.trae/audit/` | 4 | 22,819 | 成果面 |
| `.trae/audit/compile_evidence/` | 3 | 4,856 | 成果面 |
| `.trae/audit/compile_evidence/v1_62refs_20260908/` | 2 | 1,724 | 成果面 |
| `.trae/audit/compile_evidence/v2_overfull_fix_20260909/` | 2 | 3,909 | 成果面 |
| `.trae/audit/compile_evidence/v2pre_h1h3_20260909/` | 3 | 4,856 | 成果面 |
| `.trae/deliverables/` | 3 | 3,297,981 | 成果面 |
| `.trae/scripts/` | 2 | 56,382 | 成果面 |
| `deposon_team/_designs/` | 11 | 114,291 | 成果面 |
| `deposon_team/plugins/` | 41 | 357,250 | 成果面 |
| `deposon_team/products/` | 2 | 35,285 | 成果面 |
| `deposon_team/verifier/` | 3 | 20,012 | 成果面 |
| `docs/FTFB_EXTERNAL_REVIEW_R2_2026_09_17/` | 3 | 63,039 | 成果面 |
| `results/` | 925 | 49,912,022 | 成果面 |
| `results/_archive_2026_09_18/` | 8 | 58,748 | 成果面 |
| `results/_archive_2026_09_20/` | 71 | 2,417,495 | 成果面 |
| `results/_archive_2026_09_21/` | 8 | 792,760 | 成果面 |
| `results/_archive_2026_09_24/` | 8 | 167,029 | 成果面 |
| `results/_p_i_real_labels_2026_09_16/` | 1 | 1,043 | 成果面 |
| `results/_p_j_convergence_basin_2026_09_16/` | 1 | 1,669 | 成果面 |
| `results/_p_l_p_c_finite_size_scaling_2026_09_16/` | 1 | 9,076 | 成果面 |
| `results/_p_l_real_data_collapse_2026_09_16/` | 1 | 3,761 | 成果面 |
| `results/_p_m_attack_surface_cost_2026_09_16/` | 1 | 5,266 | 成果面 |
| `results/_p_m_real_separation_2026_09_16/` | 1 | 2,042 | 成果面 |
| `results/_p_n_curvature_potential_coupling_2026_09_16/` | 1 | 4,276 | 成果面 |
| `results/_p_o_stranger_verification_2026_09_16/` | 1 | 5,916 | 成果面 |
| `results/_v3x_18frozen_remeasure_2026_09_16/` | 1 | 4,202 | 成果面 |
| `results/_v3x_experiments_2026_09_16/` | 1 | 17,053 | 成果面 |
| `results/_v3x_p_k_verify_2026_09_16/` | 1 | 2,059 | 成果面 |
| `tmp_movedout_2026_09_28/` | 8 | 41,738 | 成果面 |
| `tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/` | 9 | 301,808 | 成果面 |
| `tmp_movedout_2026_10_01/` | 1 | 66,339 | 成果面 |
| `tmp_movedout_2026_10_01/legacy_caliber/` | 1 | 3,756 | 成果面 |
| `tmp_movedout_2026_10_01/process_scripts/` | 1 | 16,252 | 成果面 |
| `tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/` | 10 | 30,711 | 成果面 |
| `tmp_movedout_2026_10_01/process_scripts/v4_wt_2026_09_27/` | 1 | 4,950 | 成果面 |
| `tmp_movedout_2026_10_01/process_scripts/v5_wa_2026_09_30/` | 4 | 15,844 | 成果面 |
| `tmp_movedout_2026_10_09/uncertain_release_2026_09/` | 14 | 226,545 | 成果面 |
| `(root)/` | 28 | 636,992 | 成果面 |
| **小计** | **1,187** | **58,731,756** | —— |

#### §4.2.2 逐件（1,187 件）

| # | 相对路径 | bytes | mtime | SHA-12 |
|---:|:--|--:|:--|:--|
| 1 | `.trae/audit/compare_versions.py` | 7,958 | 2026-09-09 14:14:27 | `03e22a91bc0c` |
| 2 | `.trae/audit/compile_evidence/compile_runner.ps1` | 2,022 | 2026-09-08 22:46:03 | `1fc5f3ab3f93` |
| 3 | `.trae/audit/compile_evidence/COMPILE_SUMMARY.txt` | 1,693 | 2026-09-09 01:40:36 | `1bad41b3929f` |
| 4 | `.trae/audit/compile_evidence/extract_tars.py` | 1,141 | 2026-09-08 22:50:11 | `befdd577adce` |
| 5 | `.trae/audit/compile_evidence/v1_62refs_20260908/compile_runner.ps1` | 1,469 | 2026-09-08 21:23:13 | `51d29cb72b68` |
| 6 | `.trae/audit/compile_evidence/v1_62refs_20260908/COMPILE_SUMMARY.txt` | 255 | 2026-09-08 21:32:11 | `967ae49b3d5f` |
| 7 | `.trae/audit/compile_evidence/v2_overfull_fix_20260909/compile_runner.ps1` | 2,022 | 2026-09-08 22:46:03 | `1fc5f3ab3f93` |
| 8 | `.trae/audit/compile_evidence/v2_overfull_fix_20260909/COMPILE_SUMMARY.txt` | 1,887 | 2026-09-20 17:11:14 | `fe6f9872a2fe` |
| 9 | `.trae/audit/compile_evidence/v2pre_h1h3_20260909/compile_runner.ps1` | 2,022 | 2026-09-08 22:46:03 | `1fc5f3ab3f93` |
| 10 | `.trae/audit/compile_evidence/v2pre_h1h3_20260909/COMPILE_SUMMARY.txt` | 1,693 | 2026-09-09 01:40:13 | `1bad41b3929f` |
| 11 | `.trae/audit/compile_evidence/v2pre_h1h3_20260909/extract_tars.py` | 1,141 | 2026-09-08 22:50:11 | `befdd577adce` |
| 12 | `.trae/audit/identify_dedicated.py` | 3,806 | 2026-09-09 14:14:27 | `3feb84107c02` |
| 13 | `.trae/audit/inspect_current_tars.py` | 2,501 | 2026-09-09 14:14:27 | `291877043221` |
| 14 | `.trae/audit/rebuild_trae_home.py` | 8,554 | 2026-09-09 14:14:27 | `7bd38b8e70d4` |
| 15 | `.trae/deliverables/deposon_arxiv_cn.tar.gz` | 1,659,286 | 2026-09-09 14:14:27 | `9d7351e73652` |
| 16 | `.trae/deliverables/deposon_arxiv_en.tar.gz` | 1,637,413 | 2026-09-09 14:14:26 | `d95be2a05990` |
| 17 | `.trae/deliverables/MANIFEST.sha256.txt` | 1,282 | 2026-09-20 17:11:14 | `3ab185e6c047` |
| 18 | `.trae/scripts/_md_to_tex.py` | 48,627 | 2026-09-09 14:14:27 | `f55da6fe7aea` |
| 19 | `.trae/scripts/_split_packages.py` | 7,755 | 2026-09-09 14:14:27 | `872530d93a7f` |
| 20 | `_check_conv_archive.ps1` | 2,326 | 2026-09-26 17:24:02 | `c89d46c47026` |
| 21 | `_list_teamo_models.py` | 1,273 | 2026-09-17 15:43:28 | `c51f3d2005fe` |
| 22 | `_merge_or_stub_overlap_table_v3_2026_09_17.py` | 5,050 | 2026-09-18 13:48:18 | `300daa32f7be` |
| 23 | `_movedout_manifest_2026_09_21.json` | 291,551 | 2026-09-21 19:38:44 | `d1ee21f3f6ae` |
| 24 | `_movedout_manifest_2026_09_28.json` | 2,003 | 2026-09-28 18:27:21 | `6b557f005a40` |
| 25 | `_p_l_v3_phase1_finalize_2026_09_17.py` | 19,226 | 2026-09-17 13:35:21 | `cf8fd1178ab1` |
| 26 | `_p_l_v3_phase1_runner_2026_09_17.py` | 35,425 | 2026-09-18 13:48:18 | `d5e74a98c44b` |
| 27 | `_p_l_v3_phase2_closedsource_finalize_2026_09_17.py` | 14,700 | 2026-09-17 17:55:22 | `20f038a7a8dd` |
| 28 | `_p_l_v3_phase2_closedsource_runner_2026_09_17.py` | 28,344 | 2026-09-18 13:48:18 | `e6005733ca7c` |
| 29 | `_p_l_v3_phase2_closedsource_runner_v2_2026_09_17.py` | 26,716 | 2026-09-18 13:48:18 | `090d34377c9d` |
| 30 | `_p_l_v3_phase2_finalize_2026_09_17.py` | 19,901 | 2026-09-17 14:27:39 | `eaa04c5713d6` |
| 31 | `_p_l_v3_phase2_glm53_only_2026_09_17.py` | 12,604 | 2026-09-18 13:48:18 | `c88608c7a26b` |
| 32 | `_p_l_v3_phase2_or_embedding_2026_09_17.py` | 26,300 | 2026-09-18 13:43:27 | `e7353ffbb94f` |
| 33 | `_p_l_v3_phase2_or_embedding_v3_2026_09_17.py` | 27,863 | 2026-09-18 13:43:27 | `5edc460b35d3` |
| 34 | `_p_l_v3_phase2_runner_2026_09_17.py` | 21,868 | 2026-09-18 13:48:18 | `ac780b206cae` |
| 35 | `_p_l_v3_phase2_vector_emb_2026_09_17.py` | 3,810 | 2026-09-17 14:32:45 | `f5e51b83541a` |
| 36 | `_p_l_v3_phase2_vector_emb_doubao_2026_09_17.py` | 37,263 | 2026-09-17 15:56:35 | `b0a59c92a3e6` |
| 37 | `_print_sha_2026_09_17.py` | 1,227 | 2026-09-17 14:35:20 | `51d33faa22b9` |
| 38 | `_show_teamo_ownedby.py` | 1,342 | 2026-09-17 15:43:49 | `3c8175c35d82` |
| 39 | `_test_3bb_vary.py` | 3,541 | 2026-09-17 15:59:00 | `a7046b2dd65e` |
| 40 | `_test_gpt56sol_real.py` | 2,060 | 2026-09-17 15:57:09 | `19a48c278183` |
| 41 | `_tmp_degen.py` | 719 | 2026-09-26 18:33:39 | `88004f338e9c` |
| 42 | `_tmp_v1_recompute.py` | 9,819 | 2026-09-26 18:30:48 | `86a6407a7bd6` |
| 43 | `_tmp_v2_redesign.py` | 13,762 | 2026-09-26 18:31:50 | `4cd07b3a7dea` |
| 44 | `_tmp_verify.py` | 384 | 2026-09-26 18:37:04 | `e93a9cb16b08` |
| 45 | `_v4_l6_s38v2_verify_2026_09_24.py` | 3,729 | 2026-09-24 11:36:45 | `c665860f459a` |
| 46 | `deposon_team/_designs/D7_PRE_DISPATCH_EXECUTION_REPORT_2026_09_16.md` | 12,667 | 2026-09-16 13:03:05 | `3fbc7f4dfd22` |
| 47 | `deposon_team/_designs/DELEGATION_CONFIGS_FOR_USER_B_2026_09_16.md` | 12,844 | 2026-09-16 22:27:49 | `23bb7d39bf58` |
| 48 | `deposon_team/_designs/EXTERNAL_AGENT_PROMPTS_2026_09_16.md` | 12,326 | 2026-09-16 17:50:08 | `6a7b0c20a133` |
| 49 | `deposon_team/_designs/V3X_CLOSURE_REPORT_REQUIREMENTS_FOR_EXTERNAL_AGENT.md` | 8,714 | 2026-09-16 11:34:05 | `2185433b1f32` |
| 50 | `deposon_team/_designs/v3x_dispatch_log_2026_09_16.md` | 8,429 | 2026-09-16 12:56:39 | `85c3a5cfd84d` |
| 51 | `deposon_team/_designs/V3X_FULL_CLOSEOUT_REPORT_2026_09_16.md` | 12,878 | 2026-09-16 22:48:32 | `95925a562597` |
| 52 | `deposon_team/_designs/V3X_GAME_THEORY_NON_EUCLIDEAN_MASTER_NARRATIVE_2026_09_16.py` | 9,244 | 2026-09-16 11:32:56 | `7f6563d22ce7` |
| 53 | `deposon_team/_designs/V3X_KIMI_7_DIRECTIONS_FULL_ACCEPT_2026_09_16.md` | 10,936 | 2026-09-16 13:18:48 | `eecbe2b1341d` |
| 54 | `deposon_team/_designs/V3X_PATCH_5ANCHOR_RECONCILE_2026_09_16.md` | 8,222 | 2026-09-16 23:30:08 | `27db4950f710` |
| 55 | `deposon_team/_designs/V3X_PATCH_5ANCHOR_RECONCILE_V2_2026_09_17.md` | 6,799 | 2026-09-17 14:29:33 | `c41c1d6aa794` |
| 56 | `deposon_team/_designs/V3X_TEAM_IMPROVEMENT_PLAN_2026_09_16.md` | 11,232 | 2026-09-16 12:46:23 | `11cd57800bd6` |
| 57 | `deposon_team/plugins/_audit_minimax_extract_2026_09_16.py` | 4,364 | 2026-09-16 18:19:05 | `da1c38940b6c` |
| 58 | `deposon_team/plugins/_audit_v3_runners_2026_09_16.py` | 3,145 | 2026-09-16 18:50:08 | `b490f695841c` |
| 59 | `deposon_team/plugins/_build_minimax_artifact_2026_09_16.py` | 7,361 | 2026-09-16 18:11:02 | `d0d188c60a62` |
| 60 | `deposon_team/plugins/_d7_5anchor_60cells_2026_09_18.py` | 10,049 | 2026-09-16 18:54:48 | `568d30cf6d92` |
| 61 | `deposon_team/plugins/_d7_post_anchor_rotation_remediation_2026_09_16.py` | 6,241 | 2026-09-16 18:54:48 | `821fd0b19eb3` |
| 62 | `deposon_team/plugins/_d7_post_anchor_rotation_remediation_2026_09_18.py` | 9,152 | 2026-09-16 18:54:48 | `b0a450752a97` |
| 63 | `deposon_team/plugins/_fix_adendum_c_erratum_2026_09_17.py` | 1,820 | 2026-09-17 19:14:52 | `eb44de412de5` |
| 64 | `deposon_team/plugins/_fix_minimax_extract_2026_09_16.py` | 5,103 | 2026-09-16 18:20:37 | `8a722b0a4aea` |
| 65 | `deposon_team/plugins/_fix_v3_selfcheck_2026_09_16.py` | 7,401 | 2026-09-16 18:57:57 | `b9a414293ebe` |
| 66 | `deposon_team/plugins/_goal_completion_audit_2026_09_17.py` | 3,752 | 2026-09-17 19:17:07 | `5c18b72e7bb3` |
| 67 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_09_16.py` | 18,596 | 2026-09-16 18:54:48 | `d2cd7acb29a1` |
| 68 | `deposon_team/plugins/_p_i_real_labels_runner_2026_09_16.py` | 7,055 | 2026-09-16 22:10:49 | `8678e5083b41` |
| 69 | `deposon_team/plugins/_p_j_convergence_basin_runner_2026_09_16.py` | 9,143 | 2026-09-16 18:56:48 | `877b9415a217` |
| 70 | `deposon_team/plugins/_p_k_blind_test_runner_2026_09_16.py` | 19,031 | 2026-09-16 18:54:48 | `70e34edc0926` |
| 71 | `deposon_team/plugins/_p_l_p_c_finite_size_scaling_runner_2026_09_16.py` | 9,177 | 2026-09-16 20:57:27 | `bca06b3cc2f7` |
| 72 | `deposon_team/plugins/_p_l_real_data_collapse_runner_2026_09_16.py` | 5,663 | 2026-09-16 22:14:44 | `daff134b8e0b` |
| 73 | `deposon_team/plugins/_p_l_real_data_collapse_runner_2026_09_16_v2.py` | 5,778 | 2026-09-16 22:40:44 | `ed9d066f3ea3` |
| 74 | `deposon_team/plugins/_p_m_attack_surface_cost_runner_2026_09_16.py` | 10,622 | 2026-09-16 18:56:48 | `9e054e93982b` |
| 75 | `deposon_team/plugins/_p_m_real_separation_runner_2026_09_16.py` | 7,316 | 2026-09-16 22:11:02 | `d5133ecca740` |
| 76 | `deposon_team/plugins/_p_n_curvature_potential_coupling_runner_2026_09_16.py` | 9,473 | 2026-09-16 18:56:48 | `7355795bbc67` |
| 77 | `deposon_team/plugins/_p_o_stranger_verification_runner_2026_09_16.py` | 13,230 | 2026-09-16 18:56:48 | `d1bc564264ef` |
| 78 | `deposon_team/plugins/_transfer_2026_09_15.ps1` | 2,485 | 2026-09-15 15:47:26 | `4b724f65286a` |
| 79 | `deposon_team/plugins/_transfer_2026_09_15.py` | 2,253 | 2026-09-15 15:48:06 | `0f98b38169dd` |
| 80 | `deposon_team/plugins/_v3x_18frozen_remeasure_2026_09_16.py` | 5,216 | 2026-09-16 23:31:54 | `94686cf517f4` |
| 81 | `deposon_team/plugins/_v3x_experiments_runner_2026_09_16.py` | 18,555 | 2026-09-16 18:54:48 | `0fac09bec7c4` |
| 82 | `deposon_team/plugins/_v3x_p_k_verify_2026_09_16.py` | 5,373 | 2026-09-16 23:32:50 | `e516675e3db5` |
| 83 | `deposon_team/plugins/_v42_v2_runner_2026_09_16.py` | 22,460 | 2026-09-16 18:54:48 | `cf8a1f5fd383` |
| 84 | `deposon_team/plugins/attack_pc_a1_resampling.py` | 4,834 | 2026-09-15 15:08:22 | `b3ff941c9b9e` |
| 85 | `deposon_team/plugins/attack_pc_a2_fitting.py` | 4,502 | 2026-09-15 15:08:22 | `1861aecfbfe2` |
| 86 | `deposon_team/plugins/attack_pc_a3_clipping.py` | 4,469 | 2026-09-15 15:08:22 | `3a62ad10abf7` |
| 87 | `deposon_team/plugins/fix_boss_naming_2026_09_16.py` | 17,479 | 2026-09-15 15:07:35 | `21ad055e7e06` |
| 88 | `deposon_team/plugins/fix_proactive_audit_2026_09_16.py` | 15,444 | 2026-09-15 15:17:54 | `f5704c9b4497` |
| 89 | `deposon_team/plugins/fix_risk1_02940_boundary.py` | 7,125 | 2026-09-15 10:21:12 | `1017671173cb` |
| 90 | `deposon_team/plugins/fix_risk2_canonical5.py` | 8,871 | 2026-09-15 10:21:09 | `cbdbfa029f70` |
| 91 | `deposon_team/plugins/fix_risk3_s_eff_normalization.py` | 13,429 | 2026-09-15 10:22:00 | `ba347f5d9982` |
| 92 | `deposon_team/plugins/fix_selfcheck_bug_n1_2026_09_15.py` | 4,680 | 2026-09-15 15:37:39 | `fb571653df6c` |
| 93 | `deposon_team/plugins/fix_selfcheck_bug_n2_2026_09_15.py` | 3,412 | 2026-09-15 15:37:39 | `eba2d444f4da` |
| 94 | `deposon_team/plugins/fix_selfcheck_bug_n3_2026_09_15.py` | 5,134 | 2026-09-15 15:37:39 | `47fc588b3cae` |
| 95 | `deposon_team/plugins/fix_verify_freeze_policy_2026_09_16.py` | 7,122 | 2026-09-15 15:08:52 | `fa521fe37da0` |
| 96 | `deposon_team/plugins/git_commit_msg_2026_09_18.txt` | 3,223 | 2026-09-15 15:16:26 | `b2841d12a444` |
| 97 | `deposon_team/plugins/runner_pa_d1_d3.py` | 27,712 | 2026-09-15 15:15:39 | `1b9578eadc14` |
| 98 | `deposon_team/products/kimi_artifact_v_2026_09_16.json` | 9,938 | 2026-09-16 18:39:55 | `1f8612344592` |
| 99 | `deposon_team/products/minimax_artifact_v_2026_09_16.json` | 25,347 | 2026-09-16 18:20:56 | `9e1ccbdceacc` |
| 100 | `deposon_team/verifier/v42_v2_2026_09_16.py` | 17,363 | 2026-09-16 18:23:39 | `c5598b13c139` |
| 101 | `deposon_team/verifier/v42_v2_baseline_2026_09_16.json` | 1,879 | 2026-09-16 18:25:53 | `483602856618` |
| 102 | `deposon_team/verifier/v42_v2_runs_2026_09_16.jsonl` | 770 | 2026-09-16 18:25:53 | `b471190e579c` |
| 103 | `Deposon_凝子_统一场论报告_一致性核对_20260907.md` | 3,441 | 2026-09-20 17:11:14 | `125998731621` |
| 104 | `docs/FTFB_EXTERNAL_REVIEW_R2_2026_09_17/META_REVIEW_REPORT_2026_09_17.md` | 12,218 | 2026-09-17 12:27:09 | `0fda737a2203` |
| 105 | `docs/FTFB_EXTERNAL_REVIEW_R2_2026_09_17/REVIEW_RB1.md` | 22,982 | 2026-09-17 12:26:13 | `3594378e7d1d` |
| 106 | `docs/FTFB_EXTERNAL_REVIEW_R2_2026_09_17/REVIEW_RB2.md` | 27,839 | 2026-09-17 12:26:13 | `d8eafdd67119` |
| 107 | `results/_149_face_effect_disposal_2026_10_10.md` | 24,295 | 2026-10-10 01:15:42 | `e7c1232df138` |
| 108 | `results/_9model_merge_disposition_register_2026_10_09.md` | 11,651 | 2026-10-09 12:09:24 | `455277298212` |
| 109 | `results/_a02_excluded_items_idx_collection_2026_10_10.md` | 39,565 | 2026-10-10 18:40:34 | `03407e0b6662` |
| 110 | `results/_adendum_A_degradation_precheck_20260917_132049.json` | 4,248 | 2026-09-17 13:20:50 | `38fabeb19691` |
| 111 | `results/_adendum_B_pi_real_labels_v2_20260917_133726.json` | 2,374 | 2026-09-17 13:37:29 | `3d344711cf8c` |
| 112 | `results/_adendum_B_pi_real_labels_v2_20260917_133852.json` | 2,374 | 2026-09-17 13:38:55 | `c725e08e0a1c` |
| 113 | `results/_adendum_C_pm_attack_surface_v2_20260917_133726.json` | 4,123 | 2026-09-17 19:15:01 | `193ba7d66412` |
| 114 | `results/_adendum_C_pm_attack_surface_v2_20260917_133852.json` | 4,122 | 2026-09-17 19:15:01 | `6eba63788ca8` |
| 115 | `results/_adendum_D_pc_r2_per_model_v2_20260917_133726.json` | 4,605 | 2026-09-17 13:37:29 | `6fe706750823` |
| 116 | `results/_adendum_D_pc_r2_per_model_v2_20260917_133852.json` | 4,605 | 2026-09-17 13:38:55 | `d66792eea40e` |
| 117 | `results/_adendum_E_pd_supplement_v2_20260917_133726.json` | 1,353 | 2026-09-17 13:37:29 | `2c4790ffb6e3` |
| 118 | `results/_adendum_E_pd_supplement_v2_20260917_133852.json` | 1,353 | 2026-09-17 13:38:55 | `46d8dacb4721` |
| 119 | `results/_adendum_F_pe_3modal_closure_llm_dispatch_20260917_132143.json` | 3,646 | 2026-09-17 13:21:43 | `879494ed8fb9` |
| 120 | `results/_adendum_F_pe_3modal_v2_20260917_143033.json` | 38,622 | 2026-09-17 14:30:34 | `afab79249be7` |
| 121 | `results/_adendum_FGK_complete_20260917_143033.md` | 14,005 | 2026-09-17 14:31:34 | `958188c83cf0` |
| 122 | `results/_adendum_G_pf_dfix2_timing_converge_llm_dispatch_20260917_132143.json` | 2,757 | 2026-09-17 13:21:43 | `d10462080832` |
| 123 | `results/_adendum_G_pf_dfix2_v2_20260917_143033.json` | 95,292 | 2026-09-17 14:30:34 | `bf8db2ad255b` |
| 124 | `results/_adendum_H_pg_dhde_shrink_20260917_132049.json` | 4,613 | 2026-09-17 13:20:50 | `b9a0253ba6a0` |
| 125 | `results/_adendum_I_po_captions_closure_20260917_132049.json` | 4,429 | 2026-09-17 13:20:50 | `18165008bef6` |
| 126 | `results/_adendum_J_warehouse_spearman_health_20260917_132049.json` | 11,337 | 2026-09-17 13:20:50 | `df661d62426a` |
| 127 | `results/_adendum_K_087_cluster_cross_backbone_llm_dispatch_20260917_132143.json` | 2,911 | 2026-09-17 13:21:43 | `acdf933f68e0` |
| 128 | `results/_adendum_K_qwen3_087_cluster_v2_20260917_143033.json` | 32,481 | 2026-09-17 14:30:34 | `43477c8ea2d6` |
| 129 | `results/_adendum_L_verifier_dual_impl_diff_20260917_132049.json` | 2,783 | 2026-09-17 13:20:50 | `1532607ded80` |
| 130 | `results/_adendum_M_pj_convergence_basin_v2_20260917_133726.json` | 3,694 | 2026-09-17 13:37:29 | `ea7ffda97e20` |
| 131 | `results/_adendum_M_pj_convergence_basin_v2_20260917_133852.json` | 3,686 | 2026-09-17 13:38:55 | `8ab01a1e42ae` |
| 132 | `results/_adendum_N_pn_coupling_v2_20260917_133726.json` | 2,012 | 2026-09-17 13:37:29 | `1b91cc25ca57` |
| 133 | `results/_adendum_N_pn_coupling_v2_20260917_133852.json` | 2,011 | 2026-09-17 13:38:55 | `a32f3c8ba520` |
| 134 | `results/_adendum_O_pk_v2_three_way_v2_20260917_133726.json` | 1,971 | 2026-09-17 13:37:29 | `725fd7b961f8` |
| 135 | `results/_adendum_O_pk_v2_three_way_v2_20260917_133852.json` | 1,970 | 2026-09-17 13:38:55 | `a30ff093305d` |
| 136 | `results/_adendum_P_pc_two_phase_fail_h0_20260917_132049.json` | 2,456 | 2026-09-17 13:20:50 | `6b26daddc92c` |
| 137 | `results/_adendum_Q_deepseek_v4_pro_anchor_20260917_132049.json` | 4,003 | 2026-09-17 13:20:50 | `ab5d9ae6e42a` |
| 138 | `results/_af_entity_definition_draft_2026_10_10.md` | 25,257 | 2026-10-10 13:24:57 | `97654060d86e` |
| 139 | `results/_agent_trio_redesign_draft_2026_09_23.md` | 10,026 | 2026-09-23 16:11:18 | `e4320f20cad4` |
| 140 | `results/_alt_delib_pkg3_two_judgments_2026_10_10.md` | 38,032 | 2026-10-10 01:06:09 | `3f52709a48e8` |
| 141 | `results/_archive_2026_09_18/_trae_5audit_aggregated_2026_09_17.md` | 11,465 | 2026-09-17 21:28:25 | `43265e4bf2be` |
| 142 | `results/_archive_2026_09_18/_trae_anchor_18_audit_20260917_193000.md` | 3,449 | 2026-09-17 19:13:39 | `4af67e6cbe71` |
| 143 | `results/_archive_2026_09_18/_trae_code_improvement_v2_2026_09_18.md` | 20,938 | 2026-09-18 12:09:43 | `e151e48ab4b4` |
| 144 | `results/_archive_2026_09_18/_trae_corpus_5_audit_20260917_193000.md` | 3,467 | 2026-09-17 19:13:14 | `f2a655cd5e54` |
| 145 | `results/_archive_2026_09_18/_trae_d7_v1_audit_20260917_190000.json` | 4,253 | 2026-09-17 19:14:38 | `3184b30b7b0d` |
| 146 | `results/_archive_2026_09_18/_trae_d7_v1_audit_20260917_190000.md` | 7,855 | 2026-09-17 19:12:14 | `e240ca712be6` |
| 147 | `results/_archive_2026_09_18/_trae_kimi_push_v3_audit_20260917_193000.md` | 3,281 | 2026-09-17 19:12:38 | `8ece24be6b8a` |
| 148 | `results/_archive_2026_09_18/_trae_paper_8ch_双审_20260917_200000.md` | 4,040 | 2026-09-17 19:14:10 | `bec666969ffc` |
| 149 | `results/_archive_2026_09_20/_archive_manifest_2026_09_18.json` | 4,712 | 2026-09-18 22:04:18 | `a729875c0c67` |
| 150 | `results/_archive_2026_09_20/_archive_manifest_2026_09_20.json` | 35,682 | 2026-09-20 11:07:34 | `4dd89950bf11` |
| 151 | `results/_archive_2026_09_20/_audit_secret_2026_09_20_anchor_guard.py` | 6,433 | 2026-09-20 09:53:50 | `19b4174f6339` |
| 152 | `results/_archive_2026_09_20/_coze_paper_v1_双审报告_2026_09_17.md` | 85,573 | 2026-09-18 13:45:13 | `c3de25e6df57` |
| 153 | `results/_archive_2026_09_20/_coze_〔IM〕_v3_d7format_2026_09_18.pdf` | 454,307 | 2026-09-18 21:31:20 | `adc99e04ac53` |
| 154 | `results/_archive_2026_09_20/_d05_main_runner_2026_09_18.py` | 41,446 | 2026-09-18 10:07:57 | `f3d4ec483599` |
| 155 | `results/_archive_2026_09_20/_d05_md_report_only_2026_09_18.py` | 13,694 | 2026-09-18 10:16:44 | `7a5be4aef9ac` |
| 156 | `results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json` | 2,292 | 2026-09-24 19:21:31 | `0a1e91d6f772` |
| 157 | `results/_archive_2026_09_20/_d05_sanity_3backbone_2026_09_18.py` | 5,458 | 2026-09-18 10:00:35 | `a29291a60956` |
| 158 | `results/_archive_2026_09_20/_d05_verify_sha_2026_09_18.py` | 2,938 | 2026-09-18 12:41:58 | `0b7e50a8a036` |
| 159 | `results/_archive_2026_09_20/_deposon_v2scripts_reverify_worker_2026_09_18.py` | 34,134 | 2026-09-18 13:42:18 | `18984b04c45e` |
| 160 | `results/_archive_2026_09_20/_final_sha_2026_09_18.py` | 2,678 | 2026-09-18 13:48:37 | `0769f60a0504` |
| 161 | `results/_archive_2026_09_20/_fix_batch2_2026_09_18.py` | 4,100 | 2026-09-18 13:43:14 | `81bb1751be4c` |
| 162 | `results/_archive_2026_09_20/_fix_batch3_2026_09_18.py` | 3,207 | 2026-09-18 13:44:20 | `01e63e488ce2` |
| 163 | `results/_archive_2026_09_20/_fix_batch4_2026_09_18.py` | 8,225 | 2026-09-18 13:44:58 | `2efcd5ff42f1` |
| 164 | `results/_archive_2026_09_20/_fix_batch6_2026_09_18.py` | 2,214 | 2026-09-18 13:46:45 | `1c59e7b803fe` |
| 165 | `results/_archive_2026_09_20/_fix_batch7_2026_09_18.py` | 4,261 | 2026-09-18 13:47:59 | `389283c51275` |
| 166 | `results/_archive_2026_09_20/_fix_batch8_2026_09_18.py` | 2,249 | 2026-09-18 13:49:57 | `5057ccf97d6b` |
| 167 | `results/_archive_2026_09_20/_fix_d05_rescue_2026_09_18.py` | 3,524 | 2026-09-18 12:41:14 | `2c2cc3ff542a` |
| 168 | `results/_archive_2026_09_20/_ftfb_pass2_results_limitations_audit_2026_09_17.md` | 11,390 | 2026-09-17 22:41:56 | `cfab992cf939` |
| 169 | `results/_archive_2026_09_20/_letter_to_coze_paper_v1_委托_2026_09_17.md` | 12,786 | 2026-09-17 21:29:35 | `6d72e74b3482` |
| 170 | `results/_archive_2026_09_20/_letter_to_coze_〔IM〕_v2_2026_09_18.md` | 18,596 | 2026-09-18 20:50:35 | `ecdbf3a7a9c2` |
| 171 | `results/_archive_2026_09_20/_letter_to_glm_ftfb_deep_revision_2026_09_18.md` | 26,990 | 2026-09-18 13:45:13 | `3de722dc9e39` |
| 172 | `results/_archive_2026_09_20/_letter_to_kimi_push_v3_final_2026_09_17.md` | 10,304 | 2026-09-17 22:55:06 | `e6f8ded3c4ff` |
| 173 | `results/_archive_2026_09_20/_letter_to_kimi_push_v3_final_v2_2026_09_17.md` | 13,964 | 2026-09-17 23:14:56 | `40dda52e5d92` |
| 174 | `results/_archive_2026_09_20/_letter_to_kimi_push_v3_委托_2026_09_17.md` | 13,586 | 2026-09-17 21:30:25 | `042fa374a63f` |
| 175 | `results/_archive_2026_09_20/_letter_to_kimi_upload_requirements_2026_09_18.md` | 22,591 | 2026-09-18 21:30:34 | `6e23b54727e6` |
| 176 | `results/_archive_2026_09_20/_letter_to_mavis_full_mirror_request_2026_09_17.md` | 9,717 | 2026-09-17 23:06:49 | `f2934e5279e6` |
| 177 | `results/_archive_2026_09_20/_letter_to_trae_code_2026_09_17_final.md` | 10,690 | 2026-09-17 18:18:25 | `c1791a7811f3` |
| 178 | `results/_archive_2026_09_20/_openrouter_emb_runner.bak.note` | 5 | 2026-09-10 22:25:43 | `f01a374e9c81` |
| 179 | `results/_archive_2026_09_20/_p_i_curvature_audit_probe_runner_2026_09_16.py` | 12,919 | 2026-09-16 20:57:28 | `e05555deb611` |
| 180 | `results/_archive_2026_09_20/_probe_doubao_4versions_diff_2026_09_17.json` | 1,393 | 2026-09-17 15:51:14 | `49dde3059959` |
| 181 | `results/_archive_2026_09_20/_probe_doubao_4versions_diff_2026_09_17.py` | 2,720 | 2026-09-17 15:50:56 | `93527eb7b2f7` |
| 182 | `results/_archive_2026_09_20/_probe_doubao_emb_direct_2026_09_17.py` | 2,371 | 2026-09-17 15:48:30 | `9bcfe80c0dd0` |
| 183 | `results/_archive_2026_09_20/_probe_doubao_emb_via_proxy_2026_09_17.py` | 2,589 | 2026-09-17 15:48:59 | `f2818fc2ddff` |
| 184 | `results/_archive_2026_09_20/_probe_teamo_via_proxy.py` | 2,841 | 2026-09-17 15:42:29 | `dce965058076` |
| 185 | `results/_archive_2026_09_20/_reviewer_a_audit_tmp.py` | 4,397 | 2026-09-15 15:57:20 | `268225ccbb76` |
| 186 | `results/_archive_2026_09_20/_sanity_openai_more.py` | 2,187 | 2026-09-17 15:47:48 | `e11319f32dc5` |
| 187 | `results/_archive_2026_09_20/_sanity_teamo_one.py` | 2,119 | 2026-09-17 15:46:36 | `63eb0a0aa102` |
| 188 | `results/_archive_2026_09_20/_sanity_teamo_three.py` | 3,540 | 2026-09-17 15:44:19 | `888d02cd1443` |
| 189 | `results/_archive_2026_09_20/_teamorouter_smoke_tmp.json` | 277 | 2026-09-10 16:46:45 | `4181a24c9ca1` |
| 190 | `results/_archive_2026_09_20/_temp_volc_test.py` | 6,687 | 2026-09-16 11:01:12 | `264f2bf5a3f2` |
| 191 | `results/_archive_2026_09_20/_tmp_inspect_22cap.py` | 675 | 2026-09-11 11:12:09 | `0c9addf4a70f` |
| 192 | `results/_archive_2026_09_20/_tmp_inspect_5model.py` | 1,029 | 2026-09-11 11:11:01 | `048ebc99177c` |
| 193 | `results/_archive_2026_09_20/_tmp_probe_archive` | 1,270 | 2026-09-10 17:02:22 | `a6689025804c` |
| 194 | `results/_archive_2026_09_20/_v41_flash_rag_caption_embs.bak.json` | 612,511 | 2026-09-10 17:05:53 | `25f745609658` |
| 195 | `results/_archive_2026_09_20/_v41_flash_rag_partial.bak.json` | 88,584 | 2026-09-10 17:07:49 | `b0e2673f4a56` |
| 196 | `results/_archive_2026_09_20/compile_verification.txt` | 9,663 | 2026-09-18 13:45:13 | `463fc7575663` |
| 197 | `results/_archive_2026_09_20/fiction_that_feeds_back.pdf` | 356,123 | 2026-09-17 22:05:22 | `2d9edc8c7303` |
| 198 | `results/_archive_2026_09_20/fiction_that_feeds_back.tex` | 93,324 | 2026-09-17 22:05:22 | `d060f75dbe9f` |
| 199 | `results/_archive_2026_09_20/fiction_that_feeds_back_source.md` | 84,388 | 2026-09-17 22:05:22 | `543479649b3e` |
| 200 | `results/_archive_2026_09_20/ftfb_pass1_background_methodology_audit_2026_09_17.md` | 8,257 | 2026-09-17 22:42:17 | `70bd41d9722d` |
| 201 | `results/_archive_2026_09_20/LETTER_TO_KIMI_GITHUB_UPLOAD_2026_09_18.md` | 13,286 | 2026-09-15 14:55:36 | `8875bf0bc50d` |
| 202 | `results/_archive_2026_09_20/LETTER_TO_TRAE_2026_09_11.md` | 22,776 | 2026-09-16 11:01:12 | `7a95307a3293` |
| 203 | `results/_archive_2026_09_20/LETTER_TO_TRAE_FIX_SELFCHECK_2026_09_15.md` | 7,855 | 2026-09-15 15:31:39 | `c0d629df69d8` |
| 204 | `results/_archive_2026_09_20/LETTER_TO_TRAE_REVIEW_2026_09_16.md` | 12,668 | 2026-09-15 13:47:02 | `1c0885d2b1fa` |
| 205 | `results/_archive_2026_09_20/LETTER_TO_EXTERNAL_ADVISOR_2026_09_18_FINAL.md` | 10,562 | 2026-09-18 12:19:45 | `7d4b5dd967e2` |
| 206 | `results/_archive_2026_09_20/p_i_curvature_audit_probe_results_2026_09_16.json` | 2,637 | 2026-09-16 17:37:31 | `ae07f5551e87` |
| 207 | `results/_archive_2026_09_20/review_content_A1_dsv4pro.md` | 20,082 | 2026-09-18 09:27:36 | `5198a7059c06` |
| 208 | `results/_archive_2026_09_20/review_content_A1_glm51.md` | 7,617 | 2026-09-18 00:35:54 | `fd38a2a1ea05` |
| 209 | `results/_archive_2026_09_20/review_content_A2_kimik3.md` | 24,843 | 2026-09-18 09:28:57 | `a964defb923d` |
| 210 | `results/_archive_2026_09_20/review_tech_B1_dsv4pro.md` | 30,494 | 2026-09-18 00:35:54 | `0d36d7cd0589` |
| 211 | `results/_archive_2026_09_20/review_tech_B1_grok46.md` | 18,923 | 2026-09-18 09:34:12 | `09784ff172b3` |
| 212 | `results/_archive_2026_09_20/review_tech_B2_grok46.md` | 13,726 | 2026-09-18 00:35:54 | `fe80bad08eef` |
| 213 | `results/_archive_2026_09_20/review_tech_B2_qwen3max.md` | 8,098 | 2026-09-18 09:30:15 | `8d00c6d4a242` |
| 214 | `results/_archive_2026_09_20/REVIEWER_B_TMP_RERUN_2026_09_15.md` | 21,645 | 2026-09-15 14:24:07 | `8cd736ba9f91` |
| 215 | `results/_archive_2026_09_20/SHA256_MANIFEST.txt` | 552 | 2026-09-17 22:06:32 | `416dda94cb63` |
| 216 | `results/_archive_2026_09_20/TRAE_CODE_FIX_LIST_2026_09_18.md` | 9,343 | 2026-09-18 13:49:19 | `ace3c6b390cb` |
| 217 | `results/_archive_2026_09_20/TRAE_DAILY_AUDIT_LETTER_2026_09_18.md` | 11,575 | 2026-09-18 13:07:49 | `0011b7924dfb` |
| 218 | `results/_archive_2026_09_20/TRAE_FIX_RECEIPT_2026_09_18.md` | 4,784 | 2026-09-18 13:49:39 | `2e6a31af5e4b` |
| 219 | `results/_archive_2026_09_20/戴夫_FTFB双审包简报v3_2026-09-17.md` | 8,419 | 2026-09-17 22:06:25 | `6952b3b02b96` |
| 220 | `results/_archive_2026_09_21/2026-09-20.md` | 6,186 | 2026-09-20 18:26:50 | `be7aa1c479b2` |
| 221 | `results/_archive_2026_09_21/2026-09-21.md` | 2,676 | 2026-09-21 09:43:13 | `ef648f34a3a3` |
| 222 | `results/_archive_2026_09_21/_archive_manifest_2026_09_21.json` | 17,353 | 2026-09-21 19:55:39 | `33fe31633da8` |
| 223 | `results/_archive_2026_09_21/deposon_v20_corpus_eval.json` | 631,644 | 2026-08-29 01:21:14 | `ca71aa6858e1` |
| 224 | `results/_archive_2026_09_21/deposon_v20_gt2b.json` | 123,331 | 2026-08-29 19:57:39 | `a2ae7997ee67` |
| 225 | `results/_archive_2026_09_21/deposon_v20_gt3.json` | 7,844 | 2026-08-29 15:03:29 | `35b676773243` |
| 226 | `results/_archive_2026_09_21/deposon_v20_vector_audit.json` | 915 | 2026-08-28 21:15:08 | `b9b65c568842` |
| 227 | `results/_archive_2026_09_21/Deposon_评估汇总_v1_3_0.json` | 2,811 | 2026-08-22 21:07:01 | `2f02f50c164b` |
| 228 | `results/_archive_2026_09_24/_final_verify.py` | 2,307 | 2026-09-23 15:34:04 | `31a5d44497f1` |
| 229 | `results/_archive_2026_09_24/_inspect_captions.py` | 591 | 2026-09-10 17:31:00 | `dfb02ade1474` |
| 230 | `results/_archive_2026_09_24/_l13_latency_test.py` | 2,954 | 2026-09-24 14:03:31 | `dae238354342` |
| 231 | `results/_archive_2026_09_24/_v4_pi_decision_questionnaire_2026_09_21_v1.1.md.bak_2026_09_22_gB_post.md` | 113,508 | 2026-09-22 16:00:10 | `07ca9ee8e1bb` |
| 232 | `results/_archive_2026_09_24/_verify_worker_c.py` | 1,155 | 2026-09-10 21:27:55 | `cc578c46b332` |
| 233 | `results/_archive_2026_09_24/_worker_openrouter_rag_run.py` | 24,113 | 2026-09-16 11:01:12 | `4458ccf3d64a` |
| 234 | `results/_archive_2026_09_24/l14_small_batch.py` | 21,784 | 2026-09-24 14:51:45 | `0659c947bec1` |
| 235 | `results/_archive_2026_09_24/latency_test.py` | 617 | 2026-09-24 14:44:18 | `fd9fd98785e1` |
| 236 | `results/_archive_and_b6_inquiry_register_2026_10_08.md` | 21,163 | 2026-10-08 17:12:12 | `1d08a780a715` |
| 237 | `results/_archive_cleanup_extension_2026_09_28.md` | 28,774 | 2026-09-28 20:03:52 | `889d15247607` |
| 238 | `results/_archive_cleanup_non_upload_2026_09_28.md` | 56,714 | 2026-09-28 19:09:12 | `34f2c63306b8` |
| 239 | `results/_archive_ledger_rectification_register_2026_10_09.md` | 20,933 | 2026-10-09 09:31:31 | `99359733eef1` |
| 240 | `results/_archive_manifest_non_upload_v2_2026_09_28.json` | 236,651 | 2026-09-28 19:02:06 | `84eef669234b` |
| 241 | `results/_archive_manifest_non_upload_v3_2026_09_28.json` | 204,256 | 2026-09-28 20:00:44 | `a2e4c5a9b713` |
| 242 | `results/_archive_moveout_register_2026_09_29.md` | 13,363 | 2026-09-29 21:20:14 | `56639e57ac06` |
| 243 | `results/_asset_identity_reconciliation_2026_10_01.md` | 28,291 | 2026-10-01 11:27:03 | `0d22797f084f` |
| 244 | `results/_axis1_three_recomputations_2026_10_11.md` | 29,938 | 2026-10-11 17:26:24 | `8de23f7d7384` |
| 245 | `results/_b01_new_key_classification_2026_10_10.md` | 38,669 | 2026-10-10 21:31:57 | `2ddfecf6201c` |
| 246 | `results/_b01_new_key_residue_judgment_2026_10_10.md` | 41,984 | 2026-10-10 23:13:30 | `345517455dcf` |
| 247 | `results/_b01_p_counting_recompute_2026_10_10.md` | 22,104 | 2026-10-10 20:00:44 | `3511cf21a869` |
| 248 | `results/_b01_recompute_authorization_supplement_2026_10_11.md` | 18,454 | 2026-10-11 00:14:37 | `03a66d4c663a` |
| 249 | `results/_b01_recompute_sec4_2_erratum_2026_10_10.md` | 16,441 | 2026-10-10 21:33:26 | `fac3308fb295` |
| 250 | `results/_b14_audit_f2f3_closure_register_2026_10_11.md` | 29,620 | 2026-10-11 14:36:37 | `9d4a3d6ddf88` |
| 251 | `results/_b14_vk_evidence_audit_2026_10_10.md` | 33,586 | 2026-10-11 00:07:21 | `89f17297f1f5` |
| 252 | `results/_b_coincidence_closeout_register_2026_10_10.md` | 31,451 | 2026-10-10 13:32:32 | `51ce7b49c423` |
| 253 | `results/_b_coincidence_disposition_judgment_2026_10_10.md` | 42,838 | 2026-10-10 13:17:14 | `7ff80485955c` |
| 254 | `results/_backfill_rule_execution_register_2026_10_08.md` | 27,267 | 2026-10-08 16:52:40 | `3a7f8e203b28` |
| 255 | `results/_backfill_rule_final_2026_10_09.md` | 34,602 | 2026-10-09 09:26:50 | `3e97d5286760` |
| 256 | `results/_backfill_rule_vk_closeout_2026_10_08.md` | 26,890 | 2026-10-08 17:02:40 | `20f5835d47d2` |
| 257 | `results/_batch3_receipt_kimi_2026_10_01.md` | 2,238 | 2026-10-01 00:07:36 | `8c2cb4c6a937` |
| 258 | `results/_beta_formal_run_exec_register_2026_10_09.md` | 16,811 | 2026-10-09 23:32:35 | `2e5f080eab6c` |
| 259 | `results/_beta_formal_run_result_2026_10_09.json` | 103,691 | 2026-10-09 23:30:08 | `a5a918fd9861` |
| 260 | `results/_blade_caliber_b8_judgment_2026_10_10.md` | 28,738 | 2026-10-10 09:51:16 | `e189d6eb63d9` |
| 261 | `results/_c1c4_ab_pilot_comparison_2026_10_09.md` | 15,390 | 2026-10-09 23:02:14 | `bdd2a1d7e6c5` |
| 262 | `results/_c2_criterion_third_tier_draft_2026_10_11.md` | 26,713 | 2026-10-11 17:36:57 | `844179898102` |
| 263 | `results/_c4_math_corrections_downstream_erratum_2026_10_10.md` | 28,886 | 2026-10-10 18:18:42 | `643cb9e249f7` |
| 264 | `results/_c4_math_corrections_E1_E2_execution_erratum_2026_10_10.md` | 31,607 | 2026-10-10 21:20:30 | `4c369cb86db4` |
| 265 | `results/_c4_reply_intake_acceptance_register_2026_10_01.md` | 33,728 | 2026-10-10 21:19:00 | `e1e8cb7b9db4` |
| 266 | `results/_c4_theory_source_caliber_correction_2026_09_30.md` | 25,022 | 2026-10-01 09:18:38 | `61b139efd0ef` |
| 267 | `results/_c4_unblock_reply_independent_review_2026_10_10.md` | 27,364 | 2026-10-10 18:13:09 | `2ecd866e2468` |
| 268 | `results/_c8_c2_disposition_register_2026_10_11.md` | 30,956 | 2026-10-11 16:53:47 | `fb816c572779` |
| 269 | `results/_c_component4_d2d3_gap_judgment_2026_10_11.md` | 27,490 | 2026-10-11 00:15:45 | `08d3bfd82235` |
| 270 | `results/_c_component4_three_items_judgment_2026_10_11.md` | 41,580 | 2026-10-11 00:26:46 | `fd0094e2f865` |
| 271 | `results/_c_reading_recompute_2026_10_09.md` | 21,006 | 2026-10-09 09:55:37 | `95d7d23d24fd` |
| 272 | `results/_carrier_qid_disposition_2026_10_11.md` | 3,406 | 2026-10-11 23:22:17 | `7d74d5a4d81e` |
| 273 | `results/_charlie_delivery_register_2026_10_08.md` | 10,733 | 2026-10-08 15:52:36 | `6f4bf31276f5` |
| 274 | `results/_ci_bc_lines_ci_collection_2026_10_09.md` | 24,769 | 2026-10-09 16:47:04 | `6db4d0fb2452` |
| 275 | `results/_ci_bc_scope_estimand_judgments_2026_10_09.md` | 37,682 | 2026-10-09 17:34:04 | `d76ba2297d0d` |
| 276 | `results/_ci_degradation_binding_form_a_register_2026_10_09.md` | 26,104 | 2026-10-09 17:32:42 | `424730b5123d` |
| 277 | `results/_ci_detail_decoupling_degradation_baseline_2026_10_09.md` | 20,973 | 2026-10-09 15:53:38 | `56b62ed5ab74` |
| 278 | `results/_ci_four_items_effectiveness_register_2026_10_09.md` | 29,365 | 2026-10-09 17:14:39 | `4ab2464a266e` |
| 279 | `results/_ci_gap_fill_alt_bc_aper_prime_2026_10_09.md` | 29,709 | 2026-10-09 17:48:22 | `bee0f1f0bdb2` |
| 280 | `results/_ci_line_establishment_2026_10_09.md` | 28,262 | 2026-10-09 15:19:58 | `329c1c5e91d1` |
| 281 | `results/_ci_three_delegated_judgments_2026_10_09.md` | 26,090 | 2026-10-09 17:16:22 | `dac19ee9e66b` |
| 282 | `results/_ci_three_items_effectivity_register_2026_10_09.md` | 31,488 | 2026-10-09 21:12:50 | `2b7166a7d726` |
| 283 | `results/_ci_width_halfwidth_pin_2026_10_09.md` | 17,426 | 2026-10-09 15:52:02 | `51765f40f5f9` |
| 284 | `results/_cleanup_round2_register_2026_09_29.md` | 36,245 | 2026-09-29 22:20:14 | `ee47a2ec49f4` |
| 285 | `results/_cleanup_round_2026_10_01.md` | 27,477 | 2026-10-01 16:42:21 | `0db6e5d6146c` |
| 286 | `results/_cleanup_round_2026_10_08.md` | 33,179 | 2026-10-08 18:25:13 | `d048a6de1dea` |
| 287 | `results/_clearance_materials_register_2026_10_08.md` | 45,254 | 2026-10-08 16:24:26 | `356eb1c53986` |
| 288 | `results/_clearance_mini_rulings_closeout_register_2026_10_01.md` | 31,942 | 2026-10-01 09:10:24 | `9238c2287af5` |
| 289 | `results/_clearance_round_1_register_2026_10_08.md` | 13,826 | 2026-10-08 16:43:54 | `58fa92543338` |
| 290 | `results/_closing_round_4_decisions_register_2026_10_08.md` | 5,322 | 2026-10-08 17:54:26 | `771e37b4a25d` |
| 291 | `results/_closing_round_5_decisions_register_2026_10_08.md` | 3,282 | 2026-10-08 18:02:35 | `5b08d34a05ba` |
| 292 | `results/_closing_round_6_decisions_register_2026_10_08.md` | 3,869 | 2026-10-08 18:05:56 | `272cb570c78b` |
| 293 | `results/_closing_round_7_decisions_register_2026_10_09.md` | 3,206 | 2026-10-09 09:29:38 | `d5976bfe23c6` |
| 294 | `results/_closing_round_9_decisions_register_2026_10_09.md` | 2,314 | 2026-10-09 10:59:27 | `27118156a99a` |
| 295 | `results/_codex_c4_unblock_reply_adoption_register_2026_10_10.md` | 22,895 | 2026-10-10 18:13:35 | `b979e78562a9` |
| 296 | `results/_codex_c4_values_followup_reply_intake_register_2026_10_10.md` | 24,240 | 2026-10-10 17:05:56 | `c46d073589cf` |
| 297 | `results/_codex_c4_values_reply_intake_register_2026_10_10.md` | 12,926 | 2026-10-10 14:09:06 | `8f1d27a02833` |
| 298 | `results/_codex_c4_values_unblock_reply_intake_register_2026_10_10.md` | 27,100 | 2026-10-10 18:06:56 | `a2d7f86d72e5` |
| 299 | `results/_commission_closeout_erratum_and_supplement_2026_10_11.md` | 12,447 | 2026-10-11 23:46:12 | `7c102a6b4667` |
| 300 | `results/_confirm_b9_tension_annex_2026_10_01.md` | 19,454 | 2026-10-01 10:29:54 | `f28724a99a0c` |
| 301 | `results/_confirm_round_2026_10_01_register.md` | 14,500 | 2026-10-01 00:35:17 | `23a97e340fdf` |
| 302 | `results/_confirm_round_2_2026_10_01_register.md` | 22,327 | 2026-10-01 09:44:14 | `817302144788` |
| 303 | `results/_coze_paper_v1_draft_2026_09_17.md` | 29,484 | 2026-09-18 00:21:36 | `c08e7abf5ee3` |
| 304 | `results/_coze_paper_v1_summary_2026_09_17.md` | 3,624 | 2026-09-18 00:20:40 | `2efdc3d7741d` |
| 305 | `results/_coze_〔IM〕_v3_2026_09_18.md` | 7,466 | 2026-09-18 21:03:20 | `229d76e1b86f` |
| 306 | `results/_coze_〔IM〕_v3_d7format_2026_09_18.md` | 8,715 | 2026-09-18 21:08:42 | `905544775aee` |
| 307 | `results/_coze_〔IM〕_v3_final_2026_09_18.md` | 11,657 | 2026-09-18 21:04:55 | `deee45f45c5d` |
| 308 | `results/_coze_〔IM〕_v4_d7format_2026_09_26.pdf` | 465,366 | 2026-09-26 22:50:54 | `a82881653520` |
| 309 | `results/_cpath_sim_runner.py` | 18,783 | 2026-09-10 20:44:28 | `6074d83944dc` |
| 310 | `results/_d05_backbone_robustness_beta_20260918_100853.json` | 1,490 | 2026-09-18 10:14:58 | `9b6f085d96dc` |
| 311 | `results/_d05_combined_report_20260918_100853.md` | 10,555 | 2026-09-18 10:30:53 | `c87eb8974268` |
| 312 | `results/_D05_DATA_RESCUE_NOTE_2026_09_18.md` | 1,181 | 2026-09-18 12:41:46 | `120295a19655` |
| 313 | `results/_d05_i1i5_invariants_check_20260918_100853.json` | 1,920 | 2026-09-18 10:14:59 | `f12af5435928` |
| 314 | `results/_d05_main_run_results_20260918_100853.json` | 15,243 | 2026-09-18 12:41:46 | `0a933d7c8d7a` |
| 315 | `results/_d05_main_run_results_nemotron_3.5_20260918_100853.json` | 15,111 | 2026-09-18 10:14:56 | `1b1b6ad67c39` |
| 316 | `results/_d05_main_run_results_qwen3_failed_20260918_100853.json` | 18,358 | 2026-09-18 12:41:46 | `427b18da8114` |
| 317 | `results/_d05_opt_5_directions_results_20260918_100853.json` | 5,614 | 2026-09-18 10:14:59 | `e5979133195a` |
| 318 | `results/_d05_three_checks_readings_recheck_confirm_2026_10_10.md` | 20,044 | 2026-10-10 12:43:54 | `dcf9f5cfa2db` |
| 319 | `results/_d1_backfill_b3_b7_suggestion_table_2026_10_01.md` | 26,731 | 2026-10-01 12:15:24 | `8e1494301bb8` |
| 320 | `results/_d1_backfill_collection_rounds_2026_10_01.md` | 22,908 | 2026-10-01 12:29:25 | `2d1a0d43e588` |
| 321 | `results/_d1_backfill_conflict_trace_2026_10_01.md` | 31,506 | 2026-10-01 11:06:56 | `0cecda616f15` |
| 322 | `results/_d1_backfill_event_id_prefix_proposal_2026_10_01.md` | 14,074 | 2026-10-01 12:28:08 | `2636394df918` |
| 323 | `results/_d1_backfill_readiness_pack_2026_10_01.md` | 26,462 | 2026-10-01 11:49:06 | `ed644fb07f88` |
| 324 | `results/_d1_ruling_and_s3_transition_2026_10_01.md` | 28,370 | 2026-10-10 11:37:23 | `dc9cb0e02922` |
| 325 | `results/_d7_external_advisor_〔IM〕_publish_v1_20260918.md` | 9,891 | 2026-09-17 14:39:46 | `f4d5b755736a` |
| 326 | `results/_d8_closeout_protocol_recompute_2026_09_30.md` | 31,007 | 2026-09-30 22:57:20 | `57aba2cd26a6` |
| 327 | `results/_d8_dup_overlap_disposal_2026_09_30.md` | 32,350 | 2026-09-30 14:14:24 | `de8691727842` |
| 328 | `results/_day_close_register_2026_10_01.md` | 33,115 | 2026-10-01 16:55:26 | `6dbac1d1bcd6` |
| 329 | `results/_deemphasis_verification_register_2026_10_08.md` | 27,322 | 2026-10-08 16:02:33 | `3f806e44a13f` |
| 330 | `results/_deposon_v2scripts_kimi7_audit_20260918_105219.json` | 2,096 | 2026-09-18 10:52:19 | `3da62b979053` |
| 331 | `results/_deposon_v2scripts_reverify_20260918_105219.json` | 12,888 | 2026-09-18 10:52:19 | `8ac002ccb082` |
| 332 | `results/_deposon_v2scripts_reverify_20260918_105219.md` | 5,347 | 2026-09-18 10:52:19 | `ee005ea1f031` |
| 333 | `results/_deposon_v2scripts_summary_挂点回扣_20260918_105219.json` | 404 | 2026-09-18 10:52:19 | `2ca5870e4659` |
| 334 | `results/_dup_name_diff_content_scan_2026_10_08.json` | 1,302,889 | 2026-10-08 17:23:27 | `a27d11f45c21` |
| 335 | `results/_e2_glm2_distill_side_receipt_register_2026_10_09.md` | 11,336 | 2026-10-09 10:03:28 | `974124fc53f9` |
| 336 | `results/_e4_lineage_conflict_correction_2026_10_11.md` | 30,510 | 2026-10-11 16:22:45 | `e20b96e32f54` |
| 337 | `results/_e5_nonbinary_count_judgment_2026_10_10.md` | 37,762 | 2026-10-10 11:36:54 | `2ef8797c03f4` |
| 338 | `results/_e6_alt_permp_comparability_closure_2026_10_10.md` | 16,636 | 2026-10-10 15:03:20 | `1c663430b4aa` |
| 339 | `results/_e6_case_a_judgment_face_promotion_2026_10_10.md` | 42,116 | 2026-10-10 12:53:23 | `4e65c53f68e8` |
| 340 | `results/_e6_j5_backfill_resolution_2026_10_10.md` | 23,171 | 2026-10-10 11:45:26 | `c888158b3263` |
| 341 | `results/_e6_j5_semantics_conflict_judgment_2026_10_10.md` | 27,682 | 2026-10-10 13:13:46 | `3c7628a4964d` |
| 342 | `results/_e6_j5_semantics_erratum_note_2026_10_10.md` | 21,166 | 2026-10-10 13:34:44 | `b2db427147e2` |
| 343 | `results/_e6_n_distinct_judge_types_recompute_2026_10_10.md` | 26,304 | 2026-10-10 15:02:56 | `82c5c143134e` |
| 344 | `results/_e6_th_v3_19_alignment_register_2026_10_10.md` | 32,582 | 2026-10-10 15:13:34 | `622cebef2c9f` |
| 345 | `results/_e6_th_v3_19_residual_exits_judgment_2026_10_10.md` | 46,261 | 2026-10-10 17:59:21 | `442d5ff4acdb` |
| 346 | `results/_e6_verdict_v3_rationale_review_2026_10_10.md` | 39,008 | 2026-10-10 13:36:11 | `664e82968fc2` |
| 347 | `results/_ea_audit_batch_vk_2026_10_09.md` | 19,611 | 2026-10-09 12:17:38 | `ce27db55e0c5` |
| 348 | `results/_eps_ls_semantics_judgment_2026_10_11.md` | 31,391 | 2026-10-11 14:59:15 | `51434449ff3b` |
| 349 | `results/_evening_audit_b2_sampling_and_rejudges_2026_10_09.md` | 29,069 | 2026-10-09 23:42:59 | `b067fd28f950` |
| 350 | `results/_executor_prereg_docstring_correction_2026_10_11.md` | 27,721 | 2026-10-12 00:34:33 | `f7f8328c49ba` |
| 351 | `results/_executor_prereg_vs_impl_equivalence_2026_10_11.md` | 20,028 | 2026-10-12 00:08:14 | `e84cec618659` |
| 352 | `results/_exp03_blade_caliber_review_2026_10_10.md` | 19,797 | 2026-10-10 03:00:34 | `8c030758b331` |
| 353 | `results/_exp05_missing_true_disposition_judgment_2026_10_10.md` | 25,552 | 2026-10-10 10:46:49 | `e8e1e63a11db` |
| 354 | `results/_exp05_negative_probe_rescan_2026_10_10.md` | 11,566 | 2026-10-10 03:06:08 | `ca7ff556fd7a` |
| 355 | `results/_exp06_kcf4_check_bit_landing_2026_10_10.md` | 20,709 | 2026-10-10 03:06:42 | `088ba3d58c0f` |
| 356 | `results/_exp08_s4_prompt_face_register_2026_10_10.md` | 11,929 | 2026-10-10 03:07:20 | `83109ecf440e` |
| 357 | `results/_exp08_volume_reconciliation_2026_10_10.md` | 24,140 | 2026-10-10 10:33:56 | `895eb3f2943c` |
| 358 | `results/_external_letters_two_generation_values_note_2026_10_01.md` | 10,979 | 2026-10-01 09:18:01 | `9f4439bf89a9` |
| 359 | `results/_external_pat_ark_prep_2026_09_30.md` | 14,055 | 2026-09-30 19:41:47 | `ca540e5cab23` |
| 360 | `results/_external_sibling_path_reference_rule_2026_10_01.md` | 23,871 | 2026-10-01 13:59:04 | `e79eabb6cfa7` |
| 361 | `results/_f3_definition_deep_judgment_2026_10_11.md` | 42,351 | 2026-10-11 13:46:07 | `11945e587b1d` |
| 362 | `results/_f3_new_definition_draft_2026_10_11.md` | 48,068 | 2026-10-11 12:51:45 | `7482699e8b07` |
| 363 | `results/_f3f4_exit_drafts_2026_10_11.md` | 50,427 | 2026-10-11 01:44:40 | `523dc6cbdf9a` |
| 364 | `results/_f4_direction1_prereq_check_2026_10_11.md` | 38,664 | 2026-10-11 12:42:20 | `bb49153c311f` |
| 365 | `results/_f4_direction1_seed_and_domain_draft_2026_10_11.md` | 33,887 | 2026-10-11 13:29:50 | `f77c080d9fc6` |
| 366 | `results/_f5_77_16items_reconciliation_2026_10_01.md` | 23,930 | 2026-10-01 11:15:01 | `38be1dc9a33f` |
| 367 | `results/_f5_d1_event_count_correction_2026_10_01.md` | 24,994 | 2026-10-01 10:05:17 | `771641e234d6` |
| 368 | `results/_f5_d1_event_count_correction_execution_2026_10_01.md` | 24,279 | 2026-10-01 10:22:03 | `44d8cc9cb4a5` |
| 369 | `results/_fake_verdict_session_log_reverify_2026_09_30.md` | 25,953 | 2026-09-30 12:54:50 | `c14094bdf815` |
| 370 | `results/_five_items_effectivity_register_2026_10_11.md` | 43,332 | 2026-10-11 16:31:27 | `8affdca64b4b` |
| 371 | `results/_five_pending_items_drafts_2026_10_11.md` | 55,102 | 2026-10-11 16:06:04 | `86c46998de63` |
| 372 | `results/_five_stage_chain_design_reconstruction_2026_10_12.md` | 12,625 | 2026-10-12 01:02:53 | `bff2fb754564` |
| 373 | `results/_forgotten_items_quick_sweep_register_2026_10_01.md` | 43,735 | 2026-10-01 10:05:19 | `91103473289a` |
| 374 | `results/_forgotten_recovery_register_2026_09_29.md` | 47,494 | 2026-09-29 21:39:46 | `d78be896bcb6` |
| 375 | `results/_four_items_execution_batch_2026_10_11.md` | 31,515 | 2026-10-11 15:16:44 | `8006d1962e5f` |
| 376 | `results/_fp3_anchor_and_krj_restrament_register_2026_10_11.md` | 32,886 | 2026-10-11 16:22:16 | `b7c060ab2d49` |
| 377 | `results/_freeze_receipt_2026_10_01_q1.md` | 698 | 2026-10-01 21:02:42 | `9b7101bc09bd` |
| 378 | `results/_ftfb_order_judgment_2026_10_11.md` | 45,911 | 2026-10-11 15:40:48 | `b6eec487e9d7` |
| 379 | `results/_ftfb_v3_pass1_audit_2026_09_18_corrected.md` | 20,117 | 2026-09-18 13:45:13 | `ecb406570615` |
| 380 | `results/_ftfb_v3_pass2_audit_2026_09_18_corrected.md` | 28,579 | 2026-09-18 13:45:13 | `413ddb0bd00e` |
| 381 | `results/_full_tidy_inventory_register_2026_09_30.md` | 27,687 | 2026-09-30 17:48:12 | `33f68dbfbd6f` |
| 382 | `results/_g10_threshold_closed_domain_judgment_2026_10_11.md` | 55,727 | 2026-10-11 01:18:04 | `586abda5ddf7` |
| 383 | `results/_g11_krj4_effectivity_register_2026_10_11.md` | 39,870 | 2026-10-11 12:31:21 | `17168119eccc` |
| 384 | `results/_g4_controlled_reproduction_design_2026_10_09.md` | 23,675 | 2026-10-09 09:47:11 | `b1c7c24926bb` |
| 385 | `results/_g4_e3_definition_independent_judgment_2026_10_09.md` | 29,094 | 2026-10-09 12:33:36 | `aebaff5b503c` |
| 386 | `results/_g4_e3_definition_ruling_material_2026_10_09.md` | 30,662 | 2026-10-09 11:07:09 | `8ae4016bb41d` |
| 387 | `results/_g4_reproduction_execution_register_2026_10_09.md` | 20,414 | 2026-10-09 10:21:25 | `4daaf68cbf0e` |
| 388 | `results/_g4_residual_probe_2026_10_08.md` | 23,025 | 2026-10-08 16:19:49 | `3554aa156e08` |
| 389 | `results/_g4_runtime_state_trace_2026_10_01.md` | 25,631 | 2026-10-01 16:31:10 | `e0ae0ad66acb` |
| 390 | `results/_g4_skill_read_scope_trace_2026_10_01.md` | 26,906 | 2026-10-01 14:31:34 | `9196a608bb0d` |
| 391 | `results/_g5_ccp_p0_verification_2026_10_10.md` | 24,819 | 2026-10-10 19:05:07 | `8c7693379496` |
| 392 | `results/_g5_displacement_threshold_c_approval_effect_and_trigger_eval_2026_10_10.md` | 33,880 | 2026-10-10 14:44:04 | `3015f2481df1` |
| 393 | `results/_g5_displacement_threshold_draft_2026_10_10.md` | 25,619 | 2026-10-10 14:02:11 | `7c8107d9a8fb` |
| 394 | `results/_g5_krj9_denominator_reconciliation_judgment_2026_10_10.md` | 45,207 | 2026-10-10 18:34:36 | `22d90f12d605` |
| 395 | `results/_g5_rejudgment_c_applicability_recheck_2026_10_10.md` | 49,051 | 2026-10-10 17:09:46 | `15301b3025fa` |
| 396 | `results/_g5_rejudgment_construction_question_judgment_2026_10_10.md` | 59,309 | 2026-10-10 17:47:40 | `ee660515d9e3` |
| 397 | `results/_g5_rejudgment_face_prereg_2026_10_10.md` | 35,097 | 2026-10-10 16:04:10 | `04495ef4b343` |
| 398 | `results/_g5_rejudgment_trigger_caliber_judgment_2026_10_10.md` | 48,727 | 2026-10-10 17:12:00 | `16c31894d445` |
| 399 | `results/_g5_seg3_tie_veto_judgment_2026_10_10.md` | 35,983 | 2026-10-10 15:17:28 | `3306d1fd020d` |
| 400 | `results/_g5_x4_dual_axis_interpretation_judgment_2026_10_10.md` | 33,976 | 2026-10-10 18:29:03 | `c3117773ab36` |
| 401 | `results/_g9_read_b_effectivity_register_2026_10_11.md` | 29,649 | 2026-10-11 16:53:23 | `f5d601a0602a` |
| 402 | `results/_gap_closeout_status_2026_10_09.md` | 28,793 | 2026-10-09 11:07:19 | `ea41e346c4c4` |
| 403 | `results/_gate_one_declared_adoption_register_2026_10_11.md` | 12,923 | 2026-10-12 00:18:23 | `3a965362d4f4` |
| 404 | `results/_gate_one_pi_endorsement_register_2026_10_12.md` | 9,579 | 2026-10-12 00:53:49 | `b09209e9c20d` |
| 405 | `results/_give_up_n10_erratum_2026_10_10.md` | 22,021 | 2026-10-10 15:25:42 | `e0db6b819138` |
| 406 | `results/_give_up_semantics_draft_2026_10_10.md` | 23,497 | 2026-10-10 13:26:05 | `b6a4ae82e038` |
| 407 | `results/_glm_five_items_suggestion_table_2026_10_01.md` | 29,622 | 2026-10-01 11:21:40 | `f2b1359be37d` |
| 408 | `results/_glm_response_v2_template_2026_09_18.md` | 44,191 | 2026-09-18 13:59:16 | `972401e056f6` |
| 409 | `results/_glm_v3_双审报告_2026_09_18.md` | 20,632 | 2026-09-18 09:39:59 | `26537967db82` |
| 410 | `results/_gt_recon_gamma_erratum_note_2026_10_01.md` | 9,103 | 2026-10-01 09:17:17 | `ca063e6b9d60` |
| 411 | `results/_id_face_revision_sync_note_2026_10_10.md` | 20,690 | 2026-10-10 00:43:53 | `5d6c473731c4` |
| 412 | `results/_inspect_captions.py` | 591 | 2026-09-10 17:31:00 | `dfb02ade1474` |
| 413 | `results/_j2_identifier_coupling_judgment_2026_10_11.md` | 34,261 | 2026-10-11 16:03:04 | `2fd4505fdca2` |
| 414 | `results/_j2_kj4_disposition_register_2026_10_11.md` | 34,112 | 2026-10-11 16:37:29 | `c1a4ff1b96e5` |
| 415 | `results/_k_cf_4_effectivity_register_2026_10_09.md` | 35,872 | 2026-10-09 17:06:53 | `edc6a548e3ca` |
| 416 | `results/_k_cf_4_low_cardinality_recure_2026_10_09.md` | 33,788 | 2026-10-09 15:39:37 | `5f91d553e392` |
| 417 | `results/_k_cf_4_low_cardinality_reurecheck_and_precedent_fill_2026_10_09.md` | 31,801 | 2026-10-09 15:44:50 | `618280cb8cfd` |
| 418 | `results/_k_v3df_0_1_readings_verdict_2026_10_09.md` | 37,003 | 2026-10-09 12:06:13 | `e98bee353448` |
| 419 | `results/_k_v3df_9_1_c1_c4_legs_verdict_2026_10_09.md` | 27,735 | 2026-10-09 11:50:56 | `a14aafa220c4` |
| 420 | `results/_k_v3df_scope_two_judgments_2026_10_09.md` | 21,350 | 2026-10-09 17:33:46 | `4b22ba3c463e` |
| 421 | `results/_k_v3s_3_4_lock_freeze_2026_10_08.md` | 16,973 | 2026-10-08 16:45:08 | `c64865c32761` |
| 422 | `results/_k_v3s_4_2_domain_extension_judgment_2026_10_09.md` | 23,018 | 2026-10-09 21:06:53 | `a802af7ac3bc` |
| 423 | `results/_kd04_c_denominator_closeout_register_2026_10_10.md` | 23,029 | 2026-10-10 13:21:16 | `78481cc60494` |
| 424 | `results/_kd04_c_denominator_expansion_exec_2026_10_10.md` | 27,915 | 2026-10-10 11:41:56 | `2caa3966b866` |
| 425 | `results/_kd04_c_denominator_verdict_keeper_alternative_judgment_2026_10_10.md` | 25,123 | 2026-10-10 13:03:50 | `19ad36f7ec84` |
| 426 | `results/_kd_19_ambiguous_tags_rejudge_rewrite_register_2026_10_10.md` | 29,664 | 2026-10-10 11:06:34 | `b508e5335377` |
| 427 | `results/_kd_doc1_correction_adoption_register_2026_10_11.md` | 10,255 | 2026-10-12 00:39:06 | `c55770be5e33` |
| 428 | `results/_kd_heteronym_classification_disposition_2026_10_09.md` | 29,761 | 2026-10-09 17:54:34 | `c0cfd21d57a8` |
| 429 | `results/_kd_legacy_rewrite_plan_2026_10_10.md` | 17,643 | 2026-10-10 02:57:52 | `a9698fed8b9b` |
| 430 | `results/_kd_legacy_rewrite_register_2026_10_10.md` | 14,537 | 2026-10-10 10:41:53 | `9a7936882a5d` |
| 431 | `results/_kd_legacy_rewrite_ruling_2026_10_10.md` | 13,731 | 2026-10-10 10:40:29 | `2cadab5ed4f7` |
| 432 | `results/_kd_login_register_section65_correction_2026_10_10.md` | 20,422 | 2026-10-10 13:56:56 | `316d14c137bb` |
| 433 | `results/_kd_resolvability_and_optional_experiments_2026_10_09.md` | 70,328 | 2026-10-09 21:01:37 | `3138ac9095b0` |
| 434 | `results/_kd_rewrite_fingerprint_sync_2026_10_10.md` | 20,862 | 2026-10-10 11:53:38 | `aeefc94a94b5` |
| 435 | `results/_kd_uncognizable_meaning_rewrite_register_2026_10_10.md` | 19,525 | 2026-10-10 11:38:50 | `b07887551f7c` |
| 436 | `results/_kickoff_decisions_register_2026_10_08.md` | 16,388 | 2026-10-08 16:02:29 | `6ee5d2b8323c` |
| 437 | `results/_kimi_ftfb_s7_independent_recompute_2026_09_18.json` | 3,605 | 2026-09-18 10:39:43 | `879db0217f04` |
| 438 | `results/_kimi_fullupload_r1_r4_rulings_register_2026_09_30.md` | 4,794 | 2026-09-30 21:47:40 | `1c7445fca0de` |
| 439 | `results/_kimi_push_v3_manifest_batch10_1b753116.json` | 5,007 | 2026-09-17 23:34:06 | `326adca520f1` |
| 440 | `results/_kimi_push_v3_manifest_batch11_7d6a7c8f.json` | 2,573 | 2026-09-18 22:27:36 | `383446f24707` |
| 441 | `results/_kimi_push_v3_manifest_batch12_a2853574.json` | 1,246 | 2026-09-18 22:27:36 | `6be21f9586ec` |
| 442 | `results/_kimi_push_v3_manifest_batch13_83f895f9.json` | 739 | 2026-09-18 22:27:36 | `0694838f66a8` |
| 443 | `results/_kimi_push_v3_manifest_batch14_e5952130.json` | 1,055 | 2026-09-18 22:27:36 | `64aa9d8a5c7d` |
| 444 | `results/_kimi_push_v3_manifest_batch15_0e65fe2f.json` | 385 | 2026-09-20 09:39:32 | `cfc345d10c7d` |
| 445 | `results/_kimi_push_v3_manifest_batch1_77e2f952.json` | 2,534 | 2026-09-17 23:22:31 | `b5f517a321a3` |
| 446 | `results/_kimi_push_v3_manifest_batch2_e18c17bb.json` | 9,260 | 2026-09-17 23:23:29 | `f14341b8a1a1` |
| 447 | `results/_kimi_push_v3_manifest_batch3_01ecf050.json` | 9,656 | 2026-09-17 23:24:23 | `fd64909ea1d8` |
| 448 | `results/_kimi_push_v3_manifest_batch4_2f872d54.json` | 9,720 | 2026-09-17 23:25:26 | `d35453f21049` |
| 449 | `results/_kimi_push_v3_manifest_batch5_34439e1e.json` | 9,511 | 2026-09-17 23:28:31 | `2769b83f5b1d` |
| 450 | `results/_kimi_push_v3_manifest_batch6_28055e59.json` | 10,107 | 2026-09-17 23:29:50 | `f3eb7a38ae7d` |
| 451 | `results/_kimi_push_v3_manifest_batch7_0903df7e.json` | 9,748 | 2026-09-17 23:30:56 | `7bda1fecd7c4` |
| 452 | `results/_kimi_push_v3_manifest_batch8_7468a23b.json` | 9,880 | 2026-09-17 23:32:05 | `5a38fc02978c` |
| 453 | `results/_kimi_push_v3_manifest_batch9_f7d9cf1d.json` | 9,745 | 2026-09-17 23:33:10 | `968d7c6c43ca` |
| 454 | `results/_kimi_push_v3_manifest_verifier21_cc3c92d0.json` | 4,159 | 2026-09-18 13:45:13 | `5a6601f47632` |
| 455 | `results/_kimi_safe_batch_push_v1_2026_09_17.json` | 7,280 | 2026-09-17 14:01:43 | `4a204fb0d682` |
| 456 | `results/_kimi_safe_batch_push_v2_full_2026_09_17.json` | 47,954 | 2026-09-17 14:51:41 | `adf3a8017e26` |
| 457 | `results/_kimi_safe_batch_push_v3_full_2026_09_17.json` | 7,954 | 2026-09-18 13:50:24 | `058099c10cfb` |
| 458 | `results/_kj1_abc_choice_judgment_2026_10_11.md` | 42,083 | 2026-10-11 15:02:27 | `d02ec6b0987e` |
| 459 | `results/_kj1_eps_ls_effectivity_register_2026_10_11.md` | 62,344 | 2026-10-11 15:42:36 | `809edb4bb1cc` |
| 460 | `results/_kj1_judgment_premise_correction_2026_10_11.md` | 35,050 | 2026-10-11 15:16:12 | `003b134cce24` |
| 461 | `results/_kj1_sc1_premise_correction_2026_10_11.md` | 31,044 | 2026-10-11 14:59:46 | `8b344b9b4715` |
| 462 | `results/_kj4_e4_unification_judgment_2026_10_11.md` | 36,839 | 2026-10-11 16:08:15 | `a14d49f7d3a2` |
| 463 | `results/_krj10_reverdict_after_r4_convergence_2026_10_11.md` | 31,672 | 2026-10-12 00:05:01 | `a21915ec55a7` |
| 464 | `results/_krj10_terminal_verdict_closure_2026_10_11.md` | 14,101 | 2026-10-11 20:52:41 | `f2e8e32089b2` |
| 465 | `results/_krj4_trj1_adjudication_judgment_2026_10_11.md` | 30,293 | 2026-10-11 20:43:41 | `50e91bf30e45` |
| 466 | `results/_krj4_trj1_pick_and_pass_verdict_2026_10_11.md` | 16,567 | 2026-10-11 21:06:58 | `fb7bb5da85ec` |
| 467 | `results/_krj5_final_disposition_verdict_2026_10_11.md` | 60,700 | 2026-10-11 01:17:39 | `2b6bf509a135` |
| 468 | `results/_krj5_subject_scope_judgment_2026_10_11.md` | 45,372 | 2026-10-11 00:47:58 | `ae9df5119861` |
| 469 | `results/_krj5d_third_tier_effectivity_2026_10_11.md` | 10,729 | 2026-10-11 21:52:41 | `062093d95c9f` |
| 470 | `results/_krj9_scope_clarification_draft_2026_10_10.md` | 28,654 | 2026-10-10 19:55:36 | `b17b3c38ec21` |
| 471 | `results/_krj_all_five_verdicts_rewrite_2026_10_11.md` | 72,247 | 2026-10-11 21:12:00 | `78fb8c47c944` |
| 472 | `results/_krj_all_terminal_verdicts_2026_10_11.md` | 95,659 | 2026-10-11 17:51:02 | `f52231807e36` |
| 473 | `results/_krj_cond4_bytes_erratum_2026_10_11.md` | 3,886 | 2026-10-11 20:41:59 | `78a95e5561fc` |
| 474 | `results/_krj_cond4_effectivity_declaration_2026_10_11.md` | 15,546 | 2026-10-11 20:32:37 | `f5c317f4cc96` |
| 475 | `results/_krj_five_verdicts_adjudication_2026_10_11.md` | 16,064 | 2026-10-11 21:20:35 | `5c0efd663847` |
| 476 | `results/_krj_pi_picks_adoption_krj6_revise_2026_10_11.md` | 15,214 | 2026-10-11 21:34:15 | `31e32ccc59bf` |
| 477 | `results/_kv3s_3_2_terminal_verdict_2026_10_01.md` | 32,296 | 2026-10-01 16:06:09 | `b081d19be1b4` |
| 478 | `results/_kv3s_4_1_2_rejudge_2026_10_09.md` | 51,594 | 2026-10-09 22:34:56 | `9cde399502ba` |
| 479 | `results/_kv3s_4_4_carryover_bytes_correction_2026_10_10.md` | 5,807 | 2026-10-10 00:39:05 | `0a7d2ccf74ad` |
| 480 | `results/_kv3s_4_4_review_carryover_2026_10_10.md` | 17,606 | 2026-10-10 00:38:39 | `660d40ddd78c` |
| 481 | `results/_kv3s_4_terminal_verdict_2026_10_09.md` | 50,858 | 2026-10-09 17:23:30 | `e51317fcc5cf` |
| 482 | `results/_kv3s_4_terminal_verdict_supplement_2026_10_09.md` | 20,211 | 2026-10-09 18:06:24 | `0f82948defb3` |
| 483 | `results/_letters_archive_register_2026_10_01.md` | 26,299 | 2026-10-02 00:29:52 | `9f0740da7e4d` |
| 484 | `results/_lim_aperiod_adoption_and_label_correction_2026_10_11.md` | 14,770 | 2026-10-11 21:43:15 | `f4b129e3312f` |
| 485 | `results/_lim_aperiod_restatement_third_domain_2026_10_11.md` | 27,946 | 2026-10-11 21:38:15 | `8672a5541ca8` |
| 486 | `results/_limb_reading_verdict_kv3s33_2026_10_01.md` | 56,329 | 2026-10-10 11:37:24 | `c5866ce87d9c` |
| 487 | `results/_linestand_pi_signoff_2026_10_01.md` | 35,538 | 2026-10-01 12:20:10 | `cb5d933f8fae` |
| 488 | `results/_linestand_trace_gap_note_2026_10_01.md` | 23,252 | 2026-10-01 10:04:22 | `91bb552bf76b` |
| 489 | `results/_log_observation_review_2026_10_08.md` | 2,918 | 2026-10-08 18:14:19 | `ae20780c8d4e` |
| 490 | `results/_log_surface_scan_2026_10_08.md` | 3,156 | 2026-10-08 18:40:53 | `6b0b202c5a6c` |
| 491 | `results/_m5_eps_drift_disposition_2026_10_11.md` | 2,736 | 2026-10-11 23:19:36 | `0722f25f5838` |
| 492 | `results/_m_r16_alias_table_draft_2026_10_01.md` | 28,128 | 2026-10-01 09:52:02 | `0ba685b0d875` |
| 493 | `results/_m_r16_alias_table_effective_2026_10_01.md` | 36,578 | 2026-10-01 10:28:11 | `4ffdb809ef22` |
| 494 | `results/_mavis_skill_inventory_2026_09_18.md` | 99,702 | 2026-09-18 13:50:10 | `90ba7f7a7fbe` |
| 495 | `results/_mini_round_3_decisions_register_2026_10_01.md` | 44,308 | 2026-10-01 10:24:36 | `bff06d3b3f97` |
| 496 | `results/_mini_round_4_decisions_register_2026_10_01.md` | 37,804 | 2026-10-01 11:06:23 | `0f2d1afcc793` |
| 497 | `results/_mini_round_5_decisions_register_2026_10_01.md` | 53,125 | 2026-10-10 11:37:23 | `d5fffe6a5e79` |
| 498 | `results/_mini_round_6_7_settlement_register_2026_10_01.md` | 68,053 | 2026-10-01 12:38:47 | `a87d1121b4ac` |
| 499 | `results/_misformed_commission_drafts_deletion_register_2026_10_11.md` | 7,261 | 2026-10-11 22:45:36 | `bbdc9c2c8028` |
| 500 | `results/_morning_wrapup_pending_rulings_2026_10_01.md` | 7,341 | 2026-10-01 09:36:01 | `2b6e8b527f93` |
| 501 | `results/_n01_n08_revision_2026_10_10.md` | 26,628 | 2026-10-10 15:22:33 | `fa8400d8ae70` |
| 502 | `results/_n1_d4_clause_placement_determination_2026_10_01.md` | 53,732 | 2026-10-01 13:55:45 | `7cda6adea62b` |
| 503 | `results/_n7_mutual_exclusion_determination_2026_10_01.md` | 40,169 | 2026-10-10 11:37:24 | `b6bdf807cb27` |
| 504 | `results/_naming_erratum_linestand_note_2026_10_01.md` | 12,137 | 2026-10-01 12:27:50 | `38c8218d066b` |
| 505 | `results/_o_r2_r5_external_verification_2026_10_01.md` | 59,327 | 2026-10-01 09:16:48 | `d03832d3e2ff` |
| 506 | `results/_overnight_delivery_index_2026_10_10.md` | 35,344 | 2026-10-10 03:23:28 | `266d0327025d` |
| 507 | `results/_p4_attribution_determination_2026_10_01.md` | 22,053 | 2026-10-01 10:49:15 | `c6793cff46d7` |
| 508 | `results/_p4_clause2_ratification_note_2026_10_01.md` | 26,871 | 2026-10-01 12:19:59 | `cdf009712b96` |
| 509 | `results/_p_d_v03_22caption_verification_20260917_163757.json` | 13,775 | 2026-09-17 16:37:57 | `dfbcc5d6fc34` |
| 510 | `results/_p_d_v03_verification_report_20260917_163757.md` | 9,799 | 2026-09-17 16:39:34 | `67aafb57a8ed` |
| 511 | `results/_p_i_real_labels_2026_09_16/p_i_real_labels_results_2026_09_16.json` | 1,043 | 2026-09-16 22:11:35 | `e934819ee9ed` |
| 512 | `results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json` | 1,669 | 2026-09-16 17:39:59 | `a9ad1de618f5` |
| 513 | `results/_p_k_v3_glm_fpr_audit_report_2026-09-17T08-23-41Z.md` | 8,558 | 2026-09-17 16:23:41 | `71d5c23d9f76` |
| 514 | `results/_p_k_v3_glm_json_audit_2026-09-17T08-23-41Z.json` | 6,678 | 2026-09-17 16:23:41 | `f236e88f22ca` |
| 515 | `results/_p_k_v3_three_way_rerun_2026-09-17T08-23-41Z.json` | 12,992 | 2026-09-17 16:23:41 | `05ff758ae921` |
| 516 | `results/_p_l_p_c_finite_size_scaling_2026_09_16/p_l_p_c_finite_size_scaling_results_2026_09_16.json` | 9,076 | 2026-09-16 15:50:08 | `664e7cc05aec` |
| 517 | `results/_p_l_real_data_collapse_2026_09_16/p_l_real_data_collapse_results_v2_2026_09_16.json` | 3,761 | 2026-09-16 22:40:54 | `afe975606d40` |
| 518 | `results/_p_l_v3_phase1_report_20260917_132341.md` | 11,035 | 2026-09-17 13:35:32 | `b41a17eda169` |
| 519 | `results/_p_l_v3_phase2_beta_summary_20260917_142748.json` | 2,417 | 2026-09-17 14:27:54 | `86d4cb146241` |
| 520 | `results/_p_l_v3_phase2_closedsource_report_20260917_175544.md` | 5,909 | 2026-09-17 17:55:55 | `02443dd300ce` |
| 521 | `results/_p_l_v3_phase2_closedsource_summary_20260917_175544.json` | 3,286 | 2026-09-17 17:55:55 | `a3eafaf9ba03` |
| 522 | `results/_p_l_v3_phase2_doubao_v2_summary_20260917_170828.json` | 4,357 | 2026-09-17 17:12:34 | `c366f4e30b6b` |
| 523 | `results/_p_l_v3_phase2_doubao_v2_summary_20260917_172206.json` | 14,469 | 2026-09-17 17:55:09 | `e3dccddaed87` |
| 524 | `results/_p_l_v3_phase2_or_embedding_v3_report_20260917_162614.md` | 8,102 | 2026-09-17 16:33:30 | `fa5da7a307bd` |
| 525 | `results/_p_l_v3_phase2_or_embedding_v3_summary_20260917_162614.json` | 8,308 | 2026-09-17 16:29:34 | `21c9f23699a8` |
| 526 | `results/_p_l_v3_phase2_report_20260917_142748.md` | 9,056 | 2026-09-17 14:33:45 | `58e15c07af33` |
| 527 | `results/_p_l_v3_phase3_adendum_summary_20260917_132143.md` | 16,612 | 2026-09-17 13:22:27 | `8c07ab5aa968` |
| 528 | `results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133358.md` | 6,637 | 2026-09-17 13:34:00 | `54859cf2217a` |
| 529 | `results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133512.md` | 6,337 | 2026-09-17 13:35:15 | `c350e420eca6` |
| 530 | `results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133705.md` | 6,434 | 2026-09-17 13:37:07 | `772112cf5bd4` |
| 531 | `results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133726.md` | 6,435 | 2026-09-17 13:37:29 | `d7f03fde4067` |
| 532 | `results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133852.md` | 6,616 | 2026-09-17 13:38:55 | `d66388b6532d` |
| 533 | `results/_p_l_v3_real_collapse_mistral_L100_20260917_132341.json` | 43,903 | 2026-09-17 13:33:51 | `4657b210782a` |
| 534 | `results/_p_l_v3_real_collapse_mistral_L30_20260917_132341.json` | 16,545 | 2026-09-17 13:23:49 | `f6ab84f27d9a` |
| 535 | `results/_p_l_v3_real_collapse_mistral_L45_20260917_132341.json` | 20,108 | 2026-09-17 13:26:47 | `dc37ee54781c` |
| 536 | `results/_p_l_v3_real_collapse_mistral_L60_20260917_132341.json` | 1,174 | 2026-09-17 13:26:47 | `e3fb4f775e22` |
| 537 | `results/_p_l_v3_robustness_claude_sonnet5_L30_20260917_174011.json` | 30,772 | 2026-09-17 17:49:05 | `9d329721f67d` |
| 538 | `results/_p_l_v3_robustness_claude_sonnet5_L60_20260917_174011.json` | 1,292 | 2026-09-17 17:49:05 | `28e462c11692` |
| 539 | `results/_p_l_v3_robustness_gemini_37flash_L30_20260917_175003.json` | 30,514 | 2026-09-17 17:53:55 | `0f5c80a8a4ae` |
| 540 | `results/_p_l_v3_robustness_gemini_37flash_L60_20260917_175003.json` | 1,288 | 2026-09-17 17:53:55 | `e2590651f9c0` |
| 541 | `results/_p_l_v3_robustness_glm53_L30_20260917_142011.json` | 18,281 | 2026-09-17 14:25:11 | `2deadd7be100` |
| 542 | `results/_p_l_v3_robustness_glm53_L60_20260917_142011.json` | 1,037 | 2026-09-17 14:25:11 | `31556b58caa1` |
| 543 | `results/_p_l_v3_robustness_gpt56sol_L30_20260917_173159.json` | 30,347 | 2026-09-17 17:39:13 | `3865d7a61ca1` |
| 544 | `results/_p_l_v3_robustness_gpt56sol_L60_20260917_173159.json` | 1,266 | 2026-09-17 17:39:13 | `8c79e9a289fb` |
| 545 | `results/_p_l_v3_robustness_mistral_L60_20260917_142748.json` | 1,071 | 2026-09-17 14:27:54 | `ba41a0d4b927` |
| 546 | `results/_p_l_v3_robustness_qwen3_L30_20260917_140017.json` | 18,595 | 2026-09-17 14:06:45 | `e9bac1743a2a` |
| 547 | `results/_p_l_v3_robustness_qwen3_L60_20260917_140017.json` | 1,057 | 2026-09-17 14:06:45 | `f79f1b00e5d3` |
| 548 | `results/_p_l_v3_vector_embedding_doubao-text-240715_L30_20260917_172206.json` | 18,509 | 2026-09-17 17:29:03 | `2d4827f9cda2` |
| 549 | `results/_p_l_v3_vector_embedding_doubao-vision-241215_L30_20260917_171614.json` | 1,669,762 | 2026-09-17 17:16:46 | `2b91eb1dbbcf` |
| 550 | `results/_p_l_v3_vector_embedding_doubao-vision-241215_L30_20260917_172206.json` | 1,670,172 | 2026-09-17 17:53:27 | `e836a04a04d8` |
| 551 | `results/_p_l_v3_vector_embedding_doubao-vision-250328_L30_20260917_171614.json` | 1,670,501 | 2026-09-17 17:17:26 | `46c99397f01b` |
| 552 | `results/_p_l_v3_vector_embedding_doubao-vision-250328_L30_20260917_172206.json` | 1,669,285 | 2026-09-17 17:53:27 | `0432f25cf6c3` |
| 553 | `results/_p_l_v3_vector_embedding_doubao-vision-250615_L30_20260917_171614.json` | 1,670,027 | 2026-09-17 17:18:00 | `6b8af7d8bca9` |
| 554 | `results/_p_l_v3_vector_embedding_doubao-vision-250615_L30_20260917_172206.json` | 1,671,116 | 2026-09-17 17:53:28 | `710b7f291355` |
| 555 | `results/_p_l_v3_vector_embedding_doubao-vision-251215_L30_20260917_172206.json` | 1,670,482 | 2026-09-17 17:53:28 | `a00976c6f87b` |
| 556 | `results/_p_l_v3_vector_embedding_doubao_L30_20260917_142748.json` | 11,834 | 2026-09-17 14:32:56 | `b9488e2b01ae` |
| 557 | `results/_p_l_v3_vector_embedding_doubao_L30_20260917_170828.json` | 18,468 | 2026-09-17 17:11:53 | `198f8fe39f94` |
| 558 | `results/_p_l_v3_vector_embedding_glm53_L30_20260917_142748.json` | 11,833 | 2026-09-17 14:32:56 | `d91b0c5f642f` |
| 559 | `results/_p_l_v3_vector_embedding_mistral_L30_20260917_142748.json` | 11,835 | 2026-09-17 14:32:56 | `33d0259073dc` |
| 560 | `results/_p_l_v3_vector_embedding_or_bge-large_L30_20260917_162614.json` | 1,017,974 | 2026-09-17 16:27:59 | `aff028e8506c` |
| 561 | `results/_p_l_v3_vector_embedding_or_e5-multi_L30_20260917_162614.json` | 1,017,684 | 2026-09-17 16:28:49 | `8676b519a031` |
| 562 | `results/_p_l_v3_vector_embedding_or_gte-large_L30_20260917_162614.json` | 1,017,381 | 2026-09-17 16:29:34 | `07561d4d23d1` |
| 563 | `results/_p_l_v3_vector_embedding_or_qwen3-emb-8b_L30_20260917_162614.json` | 3,929,893 | 2026-09-17 16:27:27 | `a4bd70c02aaa` |
| 564 | `results/_p_l_v3_vector_embedding_qwen3-emb-4b_L30_20260917_170828.json` | 2,452,705 | 2026-09-17 17:12:34 | `1928ada51527` |
| 565 | `results/_p_l_v3_vector_embedding_qwen3-emb-4b_L30_20260917_172206.json` | 2,452,273 | 2026-09-17 17:53:29 | `bebee5346543` |
| 566 | `results/_p_l_v3_vector_embedding_qwen3_L30_20260917_142748.json` | 11,833 | 2026-09-17 14:32:56 | `26f7493f1c95` |
| 567 | `results/_p_l_v3_vector_embedding_v2_doubao_report_20260917_170828.md` | 17,833 | 2026-09-17 17:12:34 | `fa9cd7ffa3f2` |
| 568 | `results/_p_l_v3_vector_embedding_v2_doubao_report_20260917_172206.md` | 19,548 | 2026-09-17 17:55:23 | `2e3ec17259e2` |
| 569 | `results/_p_m_attack_surface_cost_2026_09_16/p_m_attack_surface_cost_results_2026_09_16.json` | 5,266 | 2026-09-16 17:34:14 | `fbcb60cf5102` |
| 570 | `results/_p_m_real_separation_2026_09_16/p_m_real_separation_results_2026_09_16.json` | 2,042 | 2026-09-16 22:12:02 | `a4b12d1cfedc` |
| 571 | `results/_p_n_curvature_potential_coupling_2026_09_16/p_n_curvature_potential_coupling_results_2026_09_16.json` | 4,276 | 2026-09-16 17:43:33 | `088f28524a1d` |
| 572 | `results/_p_o_stranger_verification_2026_09_16/p_o_stranger_verification_results_2026_09_16.json` | 5,916 | 2026-09-16 13:23:52 | `1e4c065da058` |
| 573 | `results/_p_refresh_registration_preliminary_2026_10_10.md` | 32,780 | 2026-10-10 21:56:34 | `a3e14b508a4a` |
| 574 | `results/_p_refresh_s0_judgment_2026_10_10.md` | 41,449 | 2026-10-10 21:28:04 | `369173063a7c` |
| 575 | `results/_p_refresh_scope_judgment_2026_10_10.md` | 34,004 | 2026-10-10 23:12:55 | `44e98dc31e2b` |
| 576 | `results/_p_s4_1_revision_register_2026_10_09.md` | 29,961 | 2026-10-09 12:09:39 | `ad5c76111570` |
| 577 | `results/_pack_d_closeout_confirm_receipt_note_2026_10_01.md` | 35,223 | 2026-10-01 15:57:56 | `15c18a28080f` |
| 578 | `results/_pack_d_closeout_effectuation_note_2026_10_01.md` | 27,609 | 2026-10-01 15:46:18 | `97a3573e2a2d` |
| 579 | `results/_pack_d_closeout_register_2026_10_01.md` | 62,012 | 2026-10-01 14:54:17 | `0f1f94df75ba` |
| 580 | `results/_pc_d1_d3_2026_09_15.py` | 43,019 | 2026-09-15 10:58:21 | `09c7c4ddbb39` |
| 581 | `results/_pending_pi_items_drafts_2026_10_11.md` | 40,678 | 2026-10-11 14:44:15 | `55f469269d3d` |
| 582 | `results/_pending_pi_items_master_register_2026_10_09.md` | 35,258 | 2026-10-09 12:45:09 | `87ab4929477f` |
| 583 | `results/_pending_rulings_drafts_2026_10_11.md` | 42,775 | 2026-10-11 12:17:37 | `c8428b883029` |
| 584 | `results/_pending_supply_search_receipt_2026_10_08.md` | 12,595 | 2026-10-08 16:17:05 | `11bbee2bea42` |
| 585 | `results/_phase1_completion_judgment_2026_10_10.md` | 28,836 | 2026-10-10 19:44:53 | `6049c68f027b` |
| 586 | `results/_pi_card_123_adoption_and_gate_one_request_2026_10_11.md` | 13,883 | 2026-10-12 00:11:11 | `0a4b752cbc56` |
| 587 | `results/_pi_effectivity_declaration_register_2026_10_11.md` | 54,511 | 2026-10-11 14:22:34 | `41a82bde5190` |
| 588 | `results/_pi_facing_items_screen_2026_10_09.md` | 59,604 | 2026-10-09 21:53:15 | `a6d33cf318fe` |
| 589 | `results/_pi_pending_items_draft_package_2026_10_09.md` | 51,793 | 2026-10-09 23:42:17 | `8fa2a7a2c49d` |
| 590 | `results/_pre_exec_report_kimi_2026_09_30.md` | 5,677 | 2026-09-30 20:04:18 | `3e3ef9007a90` |
| 591 | `results/_pre_execution_report_kimi_2026_10_01.md` | 6,277 | 2026-10-01 20:59:50 | `941e1a68b2df` |
| 592 | `results/_probe_url_update_log_2026_09_23.md` | 5,398 | 2026-09-23 16:06:40 | `8fcdd872dc07` |
| 593 | `results/_protocol_version_landing_status_2026_10_09.md` | 11,562 | 2026-10-09 11:20:01 | `1d1895489d17` |
| 594 | `results/_proxy_signoff_execution_register_2026_10_01.md` | 20,766 | 2026-10-01 16:04:59 | `b6e5e15b70e5` |
| 595 | `results/_q2_scope_vs_revision_judgment_2026_10_11.md` | 43,195 | 2026-10-11 01:01:21 | `b4f00e5a69c4` |
| 596 | `results/_q3_c1c4_l282_transposition_fix_executor_2026_10_09.py` | 64,849 | 2026-10-09 23:54:41 | `e30d4032f195` |
| 597 | `results/_q3_reported_value_errata_supplement_2026_10_10.md` | 12,499 | 2026-10-10 00:47:10 | `e026f20839b1` |
| 598 | `results/_q4_legacy_disposal_register_2026_10_01.md` | 13,336 | 2026-10-01 09:18:49 | `a8763c406d4f` |
| 599 | `results/_questionnaire_cards_intake_register_supplement_10_2026_10_10.md` | 84,127 | 2026-10-10 19:09:19 | `6c18d336e018` |
| 600 | `results/_questionnaire_cards_intake_register_supplement_11_2026_10_10.md` | 55,341 | 2026-10-10 20:19:27 | `52c97d1c11e9` |
| 601 | `results/_questionnaire_cards_intake_register_supplement_12_2026_10_10.md` | 121,137 | 2026-10-10 23:55:57 | `1ff6919967a7` |
| 602 | `results/_questionnaire_cards_intake_register_supplement_13_2026_10_11.md` | 114,253 | 2026-10-11 12:52:21 | `43e0b642f8b2` |
| 603 | `results/_questionnaire_cards_intake_register_supplement_14_2026_10_11.md` | 54,883 | 2026-10-11 13:35:24 | `79bc4bfe38a5` |
| 604 | `results/_questionnaire_cards_intake_register_supplement_15_2026_10_11.md` | 44,698 | 2026-10-11 13:47:15 | `3654c41eda64` |
| 605 | `results/_questionnaire_cards_intake_register_supplement_7_2026_10_10.md` | 52,602 | 2026-10-10 16:42:53 | `1fb8eac82781` |
| 606 | `results/_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md` | 17,517 | 2026-10-10 17:12:50 | `a651f76a6547` |
| 607 | `results/_questionnaire_cards_intake_register_supplement_8_2026_10_10.md` | 50,790 | 2026-10-10 17:51:27 | `29b30d845841` |
| 608 | `results/_questionnaire_cards_intake_register_supplement_9_2026_10_10.md` | 84,422 | 2026-10-10 18:55:53 | `b6c0b4f29152` |
| 609 | `results/_r1_amendment_undetermined_face_2026_10_01.md` | 45,128 | 2026-10-01 14:41:49 | `dab48b4d77c2` |
| 610 | `results/_r2_reference_pointer_disposition_2026_10_11.md` | 3,121 | 2026-10-11 23:19:28 | `403adec92ce1` |
| 611 | `results/_r2_verdict_179domain_arith_verification_2026_10_09.md` | 30,532 | 2026-10-09 21:45:26 | `511c81b96745` |
| 612 | `results/_r3_r4_interpretation_case_2026_10_01.md` | 64,849 | 2026-10-10 11:37:24 | `46469217883b` |
| 613 | `results/_r3_wording_disposition_2026_10_11.md` | 3,917 | 2026-10-11 23:19:03 | `9d381c9d95e6` |
| 614 | `results/_r4_convergence_2026_10_11.md` | 3,133 | 2026-10-11 23:22:31 | `678394c47724` |
| 615 | `results/_r6_disposition_2026_10_11.md` | 3,704 | 2026-10-11 23:19:12 | `cc51203fe8f5` |
| 616 | `results/_r_pair_interval_statement_errata_2026_10_09.md` | 9,259 | 2026-10-09 22:43:07 | `61944eb91b72` |
| 617 | `results/_r_pair_nonportrait_full_document_review_2026_10_09.md` | 28,176 | 2026-10-09 22:32:22 | `d8d5e4d2154f` |
| 618 | `results/_r_pair_rp3b_rp2_rpq6_judgments_2026_10_09.md` | 23,975 | 2026-10-09 22:42:46 | `5faa16446171` |
| 619 | `results/_r_pair_texts_independent_review_2026_10_09.md` | 35,443 | 2026-10-09 17:43:25 | `8c5f83c3c4cf` |
| 620 | `results/_reading_face_basis_rejudge_2026_10_10.md` | 24,208 | 2026-10-10 03:13:46 | `3fe193a2a01f` |
| 621 | `results/_readme_proper_batch_recheck_register_2026_09_30.md` | 20,781 | 2026-09-30 17:13:36 | `2e530923457e` |
| 622 | `results/_receipt_disposition_register_2026_10_08.md` | 23,050 | 2026-10-08 17:25:43 | `a79c3b82ee01` |
| 623 | `results/_refcheck_hash_change_reference_recheck_2026_09_30.md` | 33,625 | 2026-09-30 22:57:31 | `f011c29944b9` |
| 624 | `results/_register3_bytes_erratum_2026_10_11.md` | 13,294 | 2026-10-11 12:32:09 | `f9f6805a7b76` |
| 625 | `results/_registry_lag_correction_batch_2026_10_01.md` | 36,367 | 2026-10-01 10:08:43 | `5b86fbf0cbbd` |
| 626 | `results/_remote_residual_disposal_execution_order_2026_10_08.md` | 36,486 | 2026-10-08 17:06:56 | `602c4d09623d` |
| 627 | `results/_round19_followup_round21_22_approvals_effect_register_2026_10_10.md` | 54,850 | 2026-10-10 00:31:15 | `0c8dba07dd1e` |
| 628 | `results/_round20_approvals_effect_register_2026_10_10.md` | 27,711 | 2026-10-10 00:24:02 | `29d737c59e8b` |
| 629 | `results/_round23_26_threshold_review_effect_register_2026_10_10.md` | 47,297 | 2026-10-10 01:15:09 | `9b0c62765576` |
| 630 | `results/_round27_34_approvals_effect_register_2026_10_10.md` | 73,226 | 2026-10-10 11:02:09 | `d0bc0b1a9ae0` |
| 631 | `results/_round45_dispositions_effect_register_2026_10_10.md` | 19,803 | 2026-10-10 14:11:43 | `d66a1076952a` |
| 632 | `results/_round51_effectivity_register_2026_10_10.md` | 27,070 | 2026-10-10 16:04:24 | `b8b0c52296b2` |
| 633 | `results/_round52_e6b_caliber_naming_effectivity_register_2026_10_10.md` | 21,788 | 2026-10-10 16:34:00 | `e861c7bc19ad` |
| 634 | `results/_round52_s4_e4b_ad5_type_effectivity_register_2026_10_10.md` | 45,351 | 2026-10-10 16:31:38 | `debd88fc150c` |
| 635 | `results/_round53_rejudge_prereg_freeze_effectivity_register_2026_10_10.md` | 25,637 | 2026-10-10 17:10:04 | `b27814792394` |
| 636 | `results/_round53_th_v3_19_landfall_schema_effectivity_register_2026_10_10.md` | 20,023 | 2026-10-10 17:11:26 | `4c3a6dc0070d` |
| 637 | `results/_round54_g5_dispositions_register_2026_10_10.md` | 39,977 | 2026-10-10 17:42:45 | `afc67818bb85` |
| 638 | `results/_round55_dispositions_register_2026_10_10.md` | 34,913 | 2026-10-10 18:12:53 | `002fa0a9a5e4` |
| 639 | `results/_round56_ad8fix_effectivity_register_2026_10_10.md` | 16,553 | 2026-10-10 18:12:36 | `2e7f86314428` |
| 640 | `results/_round56_b01_followup_disposition_plan_2026_10_10.md` | 31,004 | 2026-10-10 20:29:17 | `857fb940a43c` |
| 641 | `results/_round56_direct_adoptions_register_2026_10_10.md` | 43,240 | 2026-10-10 19:06:22 | `e3c56c5d0a97` |
| 642 | `results/_round56_direct_adoptions_register_2_2026_10_10.md` | 26,690 | 2026-10-10 20:15:55 | `f8e0fa28c067` |
| 643 | `results/_round56_g2_enable_and_v1_rule_register_2026_10_10.md` | 34,181 | 2026-10-10 19:13:12 | `936f551f0fd3` |
| 644 | `results/_round56_gu_backdoor_exclusion_revision_2026_10_10.md` | 25,045 | 2026-10-10 19:11:29 | `52d3b10a16a0` |
| 645 | `results/_round56_idx_sc1_resolution_2026_10_10.md` | 47,107 | 2026-10-10 19:27:46 | `9b41f2a38b2f` |
| 646 | `results/_round56_idx_sc1_temp_deletion_deviation_note_2026_10_10.md` | 8,181 | 2026-10-10 19:55:10 | `c72086990450` |
| 647 | `results/_round56_n10_erratum_register_2026_10_10.md` | 20,321 | 2026-10-10 18:49:02 | `599d0450434e` |
| 648 | `results/_round56_pending_questions_compilation_2026_10_10.md` | 33,504 | 2026-10-10 18:17:26 | `ef09b3d28a0f` |
| 649 | `results/_round56_pending_questions_compilation_supplement_note_2026_10_10.md` | 29,019 | 2026-10-10 18:40:21 | `421c936f6ae8` |
| 650 | `results/_round56_registration_supplement_2026_10_10.md` | 21,865 | 2026-10-10 21:37:33 | `71a59735302c` |
| 651 | `results/_round56_review_effectivity_register_2026_10_10.md` | 49,013 | 2026-10-10 21:36:54 | `da6b55162e50` |
| 652 | `results/_round56_review_effectivity_register_3_2026_10_10.md` | 77,181 | 2026-10-10 23:50:47 | `84ed13256250` |
| 653 | `results/_round56_review_effectivity_register_4_2026_10_11.md` | 46,908 | 2026-10-11 00:23:15 | `ee31bb8a94fe` |
| 654 | `results/_round56_review_effectivity_register_5_2026_10_11.md` | 67,613 | 2026-10-11 01:04:02 | `5deba7d27bb1` |
| 655 | `results/_round56_review_effectivity_register_6_2026_10_11.md` | 58,478 | 2026-10-11 01:37:31 | `2f3255ea344f` |
| 656 | `results/_round56_sc4_nstar_inconsistency_erratum_2026_10_10.md` | 16,640 | 2026-10-10 18:11:58 | `af4c3335538a` |
| 657 | `results/_round56_shortname_backfill_note_2026_10_10.md` | 22,195 | 2026-10-10 19:07:14 | `bb2444cccd65` |
| 658 | `results/_round56_terminal_boundary_effectivity_register_2026_10_10.md` | 35,878 | 2026-10-10 18:48:25 | `d5bf826278cb` |
| 659 | `results/_round56_th3_coverage_line_effectivity_register_2026_10_10.md` | 28,378 | 2026-10-10 18:49:59 | `6794fb09ce7e` |
| 660 | `results/_round56_th4_two_field_reporting_resolution_2026_10_10.md` | 28,233 | 2026-10-10 18:50:57 | `71894a686e92` |
| 661 | `results/_round56_typeb_backfill_register_2026_10_10.md` | 40,253 | 2026-10-10 21:24:40 | `607ded06d840` |
| 662 | `results/_round56_typeb_form_draft_2026_10_10.md` | 50,170 | 2026-10-10 20:18:30 | `582c5fb9970c` |
| 663 | `results/_round56_typeb_implementation_register_2026_10_10.md` | 26,367 | 2026-10-10 19:08:08 | `c296a7833a70` |
| 664 | `results/_round56_v4_kd_row_correction_revision_2026_10_10.md` | 23,453 | 2026-10-10 19:12:12 | `6d8537cb127f` |
| 665 | `results/_round56a_dispositions_register_2026_10_10.md` | 50,365 | 2026-10-10 18:33:00 | `d8980cfae7f7` |
| 666 | `results/_round56c_card_id_erratum_2026_10_10.md` | 18,747 | 2026-10-10 19:05:04 | `f6c2d40f18ff` |
| 667 | `results/_round56c_d23_ad5_judgment_2026_10_10.md` | 50,747 | 2026-10-10 18:36:42 | `061813859345` |
| 668 | `results/_round56r8_dispositions_register_2026_10_10.md` | 46,135 | 2026-10-10 18:57:58 | `cfb08d0e15f4` |
| 669 | `results/_round56r9r10_dispositions_register_2026_10_10.md` | 49,754 | 2026-10-10 19:57:04 | `0eb408ae60f5` |
| 670 | `results/_rpq_wordlist_and_t1p2_judgments_2026_10_09.md` | 44,796 | 2026-10-09 23:30:07 | `246ce35c4ddc` |
| 671 | `results/_s1prime_trigger_caliber_reevaluation_2026_10_10.md` | 29,991 | 2026-10-10 23:51:48 | `d2326973aaf8` |
| 672 | `results/_s2prime_krj3_applicability_recheck_2026_10_10.md` | 41,322 | 2026-10-11 00:02:57 | `10518510b628` |
| 673 | `results/_s3_c4_recount_2026_10_01.md` | 32,025 | 2026-10-01 11:15:06 | `86af4c109519` |
| 674 | `results/_s3_closeout_rules_case_2026_10_01.md` | 52,659 | 2026-10-01 11:55:45 | `7e622691aec1` |
| 675 | `results/_s3_d1_rulings_supplement_register_2026_10_01.md` | 28,762 | 2026-10-01 13:35:56 | `4ce661acc81f` |
| 676 | `results/_s3_f1_loader_fix_recompute_2026_10_08.md` | 22,065 | 2026-10-08 17:00:38 | `b2c9840d237b` |
| 677 | `results/_s3_kv3s_3_verdict_2026_10_01.md` | 35,037 | 2026-10-10 11:37:23 | `e394bb6b5ddf` |
| 678 | `results/_s3_missing_field_backfill_rule_draft_2026_10_01.md` | 35,827 | 2026-10-10 11:37:24 | `8496a53d183a` |
| 679 | `results/_s3_missing_field_backfill_rule_effective_2026_10_01.md` | 52,469 | 2026-10-10 11:37:24 | `1450057b0819` |
| 680 | `results/_s3prime_recompute_after_supplement_2026_10_11.md` | 41,708 | 2026-10-11 00:59:13 | `fa025e4dc166` |
| 681 | `results/_s4_abcreadings_reproducibility_check_2026_10_10.md` | 25,234 | 2026-10-10 12:27:42 | `892e5dfe3ed1` |
| 682 | `results/_s4_bc_construction_ruling_2026_10_09.md` | 30,257 | 2026-10-09 23:22:00 | `e2fdb380cd3c` |
| 683 | `results/_s4_chain_clearance_register_2026_10_09.md` | 2,684 | 2026-10-09 14:52:20 | `eda3d304d381` |
| 684 | `results/_s4_corpus_scope_hard_constraint_judgment_2026_10_10.md` | 44,199 | 2026-10-10 17:50:47 | `c7609657dfe4` |
| 685 | `results/_s4_dkb_backfill_register_2026_10_10.md` | 25,591 | 2026-10-10 10:26:50 | `3a992c3fe235` |
| 686 | `results/_s4_e4_axis_disposition_axis2_run_2026_10_10.md` | 29,700 | 2026-10-10 15:05:02 | `2bda07af86fc` |
| 687 | `results/_s4_e4b_ad5_type_separate_judgment_2026_10_10.md` | 51,898 | 2026-10-10 15:44:56 | `f48601fee958` |
| 688 | `results/_s4_empty_sequence_backfill_assessment_2026_10_10.md` | 28,771 | 2026-10-10 00:40:54 | `41b75ffea7be` |
| 689 | `results/_s4_face_closeout_2026_10_09.md` | 29,158 | 2026-10-09 23:49:50 | `f7d76eda2911` |
| 690 | `results/_s4_face_dual_files_verification_2026_10_09.md` | 40,228 | 2026-10-09 16:57:36 | `cc3fc6eebc6b` |
| 691 | `results/_s4_face_five_lines_ci_readings_2026_10_09.md` | 39,462 | 2026-10-09 21:15:30 | `bea9bc43a8f3` |
| 692 | `results/_s4_feature_surface_v3_1_definition_2026_10_10.md` | 30,310 | 2026-10-10 11:10:18 | `d044ce1c069d` |
| 693 | `results/_s4_final_ruling_card_register_2026_10_09.md` | 2,135 | 2026-10-09 15:09:52 | `f62401b619cc` |
| 694 | `results/_s4_heldout_sampling_seed42_items_register_2026_10_09.md` | 34,689 | 2026-10-09 22:11:08 | `73a02ac5937d` |
| 695 | `results/_s4_heldout_sampling_seed42_register_2026_10_09.md` | 37,615 | 2026-10-09 21:11:25 | `2a2ad5c2e29f` |
| 696 | `results/_s4_heldout_sampling_seed42_sets_2026_10_09.json` | 59,100 | 2026-10-09 21:07:05 | `8dfc9e0d8bf9` |
| 697 | `results/_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` | 18,923 | 2026-10-10 21:59:20 | `1bf6f47a590d` |
| 698 | `results/_s4_heldout_sampling_seedthird_extractor_2026_10_11.py` | 52,655 | 2026-10-11 16:03:09 | `068e1a7a1d04` |
| 699 | `results/_s4_heldout_seedprime_verification_2026_10_10.md` | 21,966 | 2026-10-10 23:21:06 | `8c64314d0ec0` |
| 700 | `results/_s4_keyword_expansion_and_regen_design_2026_10_10.md` | 31,149 | 2026-10-10 01:11:17 | `6efddab54ca5` |
| 701 | `results/_s4_reading_surface_and_authority_register_2026_10_09.md` | 34,405 | 2026-10-09 09:28:19 | `0148b5271154` |
| 702 | `results/_s4_regen_traceability_judgment_2026_10_10.md` | 36,071 | 2026-10-10 09:44:42 | `a330273b981c` |
| 703 | `results/_s4_revision_effectiveness_register_2026_10_09.md` | 32,820 | 2026-10-09 14:47:44 | `356fe8509669` |
| 704 | `results/_s4_terminal_face_recompute_2026_10_09.md` | 46,701 | 2026-10-09 17:08:17 | `b412342eabec` |
| 705 | `results/_s4_topup_intake_verdict_2026_10_09.md` | 33,799 | 2026-10-09 14:04:40 | `658d7f3ab231` |
| 706 | `results/_s4_tree_construct_adjustment_exec_2026_10_10.md` | 28,515 | 2026-10-10 09:55:59 | `b6b47008f8fd` |
| 707 | `results/_s4_tree_prereg_revision_2026_10_10.md` | 30,382 | 2026-10-10 10:48:57 | `037140972829` |
| 708 | `results/_s4_v11_axis2_displacement_items_2026_10_10.json` | 9,941 | 2026-10-10 15:04:30 | `0eed9053619c` |
| 709 | `results/_s4_v31_displacement_register_face2_2026_10_10.md` | 17,736 | 2026-10-10 13:57:19 | `b6ce4a79116e` |
| 710 | `results/_s4_v31_exec_section8_errata_2026_10_10.md` | 23,250 | 2026-10-10 14:42:11 | `ec11aec2380d` |
| 711 | `results/_s4_w1_3636_consistency_check_2026_10_10.md` | 29,196 | 2026-10-10 14:15:28 | `0e9ae4b6ee8c` |
| 712 | `results/_s4_w2_disposition_registration_2026_10_10.md` | 23,545 | 2026-10-10 14:59:02 | `566c2f0ad7e8` |
| 713 | `results/_s4_w2_e4_separate_judgment_2026_10_10.md` | 37,607 | 2026-10-10 14:36:06 | `a51bd6530075` |
| 714 | `results/_s4_w2bc_effect_registration_2026_10_10.md` | 26,418 | 2026-10-10 15:36:26 | `b24a8411a260` |
| 715 | `results/_s4prime_five_lines_readings_2026_10_11.md` | 23,877 | 2026-10-11 01:21:28 | `e91e7f52c726` |
| 716 | `results/_s4prime_readings_runner_2026_10_11.py` | 23,766 | 2026-10-11 16:52:24 | `0aa414188361` |
| 717 | `results/_s4q04_level_attribution_judgment_2026_10_10.md` | 26,407 | 2026-10-10 13:20:41 | `49a07216a1bb` |
| 718 | `results/_s5doubleprime_five_lines_runner_2026_10_11.py` | 31,138 | 2026-10-11 18:12:11 | `9de3c08e3863` |
| 719 | `results/_s5dp_mixed_object_erratum_2026_10_11.md` | 8,380 | 2026-10-11 20:36:49 | `07cde000e66f` |
| 720 | `results/_s5prime_double_lim_a_and_item_registers_2026_10_11.md` | 58,378 | 2026-10-11 20:43:15 | `9a62fb2a6956` |
| 721 | `results/_s5prime_lim_a_and_item_registers_2026_10_11.md` | 47,225 | 2026-10-11 01:38:02 | `fa74831fa0ad` |
| 722 | `results/_s6doubleprime_terminal_verdicts_2026_10_11.md` | 76,910 | 2026-10-11 17:10:58 | `bba3b889d849` |
| 723 | `results/_s6doubleprime_verdict_supplement_2026_10_11.md` | 31,515 | 2026-10-11 17:38:34 | `8e19c10ce219` |
| 724 | `results/_s6prime_terminal_verdicts_2026_10_11.md` | 54,937 | 2026-10-11 12:36:08 | `1c8ce58d6484` |
| 725 | `results/_s7doubleprime_verification_2026_10_11.md` | 41,680 | 2026-10-11 17:27:15 | `06ac684b4923` |
| 726 | `results/_s7doubleprime_verification_erratum_2026_10_11.md` | 32,822 | 2026-10-11 17:39:50 | `9ff40693e4ac` |
| 727 | `results/_s7prime_findings_erratum_2026_10_11.md` | 31,008 | 2026-10-11 13:38:58 | `a7dfa8e789b7` |
| 728 | `results/_s7prime_prereq_and_verification_2026_10_11.md` | 36,787 | 2026-10-11 12:59:14 | `e44da4b83810` |
| 729 | `results/_seed_double_criterion_draft_2026_10_11.md` | 40,499 | 2026-10-11 14:21:47 | `025212e91546` |
| 730 | `results/_seed_double_identifier_final_judgment_2026_10_11.md` | 50,222 | 2026-10-11 15:02:43 | `728d18391748` |
| 731 | `results/_seed_double_rule_judgment_2026_10_11.md` | 57,185 | 2026-10-11 14:02:53 | `f70a689fd8c1` |
| 732 | `results/_seven_gap_closures_adoption_register_2026_10_11.md` | 11,960 | 2026-10-12 00:02:59 | `ac3c41663f84` |
| 733 | `results/_skill_cache_inventory_and_reference_update_advice_2026_09_30.md` | 31,692 | 2026-09-30 15:32:36 | `c14489750416` |
| 734 | `results/_skill_call_surface_probe_2026_09_30.md` | 32,261 | 2026-09-30 16:52:00 | `112346df64fb` |
| 735 | `results/_skill_call_surface_probe_supplement_a_2026_09_30.md` | 50,658 | 2026-09-30 17:25:29 | `a06316c3c7f2` |
| 736 | `results/_skill_call_surface_probe_supplement_b_2026_09_30.md` | 82,744 | 2026-09-30 17:36:35 | `69d311e6a4c7` |
| 737 | `results/_skill_directory_update_and_addressing_rule_2026_10_01.md` | 20,335 | 2026-10-01 10:26:01 | `4a3a2d0c5b95` |
| 738 | `results/_skill_erratum_and_parent_success_note_2026_09_30.md` | 24,143 | 2026-09-30 16:16:31 | `7a64949402d9` |
| 739 | `results/_skill_load_failure_window_readonly_facts_2026_09_30.md` | 23,065 | 2026-09-30 16:16:36 | `9f5b73620b8a` |
| 740 | `results/_skill_reference_erratum_and_runtime_anchor_experiment_2026_09_30.md` | 30,771 | 2026-09-30 17:25:45 | `16861e71305f` |
| 741 | `results/_stage1_tail_caliber_unification_register_2026_10_11.md` | 41,140 | 2026-10-11 14:41:24 | `d486ec491e8e` |
| 742 | `results/_stage2_trae_reply_acceptance_register_2026_10_12.md` | 14,874 | 2026-10-12 01:39:16 | `ce0b5a64cfce` |
| 743 | `results/_stage3_extraction_verification_2026_10_11.md` | 22,399 | 2026-10-11 16:56:21 | `f973e6d737c3` |
| 744 | `results/_stage3_open_and_mandate_register_2026_10_12.md` | 13,865 | 2026-10-12 01:54:54 | `1b0a109a7914` |
| 745 | `results/_stage3_readings_verification_2026_10_11.md` | 29,956 | 2026-10-11 17:13:11 | `023a0cdd3350` |
| 746 | `results/_stage3_trigger_readings_2026_10_11.md` | 35,711 | 2026-10-11 16:56:23 | `2900948bca6d` |
| 747 | `results/_sub_artifact_ledger_history_r5_2026_10_01.md` | 35,845 | 2026-10-01 10:15:04 | `372a53b9e832` |
| 748 | `results/_sub_transfer_candidates_2026_10_01.md` | 21,796 | 2026-10-01 19:35:10 | `2f61c0aa2a2b` |
| 749 | `results/_sub_transfer_execution_register_2026_10_01.md` | 13,377 | 2026-10-01 19:45:58 | `c41013a975e0` |
| 750 | `results/_sub_transfer_wave2_register_2026_10_01.md` | 14,286 | 2026-10-01 19:57:08 | `265b03ea493a` |
| 751 | `results/_sub_transfer_wave3_register_2026_10_01.md` | 14,419 | 2026-10-01 20:33:47 | `cd80b993f497` |
| 752 | `results/_suspect17_release_move_register_2026_10_09.md` | 22,351 | 2026-10-09 09:47:38 | `9a4d40bfcdc3` |
| 753 | `results/_t1_7_2_correction_2026_10_08.md` | 16,469 | 2026-10-10 11:37:23 | `d90bf82338f6` |
| 754 | `results/_t1_d7_reading_line_judgment_2026_10_10.md` | 28,559 | 2026-10-10 00:18:41 | `60bd9ae98640` |
| 755 | `results/_t1_exp2_exec_register_2026_10_09.md` | 18,597 | 2026-10-10 02:34:26 | `3a08dcfa8c7f` |
| 756 | `results/_t1_exp2_verdict_2026_10_10.md` | 48,298 | 2026-10-10 02:47:15 | `15c1c4b317a0` |
| 757 | `results/_t1_exp2_verdict_bytes_correction_2026_10_10.md` | 13,480 | 2026-10-10 10:29:40 | `e863ca5fb157` |
| 758 | `results/_t1_gate_closure_and_recompute_verdict_2026_10_01.md` | 72,934 | 2026-10-10 11:37:24 | `4bdd82c796b8` |
| 759 | `results/_t1_gate_revision_draft_2026_10_09.md` | 27,452 | 2026-10-09 21:17:22 | `50e8b2440346` |
| 760 | `results/_t1_gate_revision_formal_2026_10_09.md` | 35,658 | 2026-10-09 22:21:20 | `0e0cb002c5de` |
| 761 | `results/_t1_o1_design_axis_exemption_judgment_2026_10_09.md` | 17,073 | 2026-10-09 17:09:36 | `a27c7f411de5` |
| 762 | `results/_t1_p2_aggregation_caliber_judgment_2026_10_09.md` | 14,397 | 2026-10-09 17:08:31 | `02f44f5bf2dd` |
| 763 | `results/_t1_pairing_caliber_ruling_2026_10_09.md` | 21,346 | 2026-10-09 21:56:51 | `2ded8091114a` |
| 764 | `results/_t1_r2_d1_field_caliber_correction_2026_10_09.md` | 25,396 | 2026-10-09 21:28:08 | `99cafda125f1` |
| 765 | `results/_t1_temp_axis_retirement_consolidation_2026_10_10.md` | 20,308 | 2026-10-10 10:51:31 | `40cb2e81425a` |
| 766 | `results/_t1_temp_axis_retirement_judgment_2026_10_10.md` | 27,384 | 2026-10-10 09:43:25 | `19afc7e191a7` |
| 767 | `results/_t1p2_enable_judgment_2026_10_10.md` | 20,132 | 2026-10-10 00:30:13 | `1e97d06b6ec9` |
| 768 | `results/_t1p2_escalation_judgment_2026_10_10.md` | 22,930 | 2026-10-10 00:30:53 | `5f43775a3224` |
| 769 | `results/_t1p2_judgment_bytes_correction_2026_10_10.md` | 6,377 | 2026-10-10 00:31:40 | `d9d29bec3a0b` |
| 770 | `results/_test_conv_out.txt` | 7,568 | 2026-09-26 17:16:43 | `6effe5ef7ae6` |
| 771 | `results/_th_id_miscitation_correction_2026_10_09.md` | 10,468 | 2026-10-09 16:43:24 | `b61321ba3b6e` |
| 772 | `results/_theory_boundary_clone_sync_register_2026_10_09.md` | 17,528 | 2026-10-09 09:47:13 | `1f9fd007649c` |
| 773 | `results/_theory_input_request_supplement_2026_09_29.md` | 48,190 | 2026-09-30 20:27:38 | `c966e7b605af` |
| 774 | `results/_three_pending_items_drafts_2026_10_11.md` | 51,748 | 2026-10-11 21:55:16 | `8995859e5a76` |
| 775 | `results/_three_pending_items_effectivity_2026_10_11.md` | 16,744 | 2026-10-11 22:05:39 | `df1f5f75c7a0` |
| 776 | `results/_three_state_standard_repeal_register_2026_10_10.md` | 18,364 | 2026-10-10 14:44:36 | `8503708c73bf` |
| 777 | `results/_thv3_15_parallel_seed_double_note_2026_10_11.md` | 15,569 | 2026-10-11 15:17:29 | `3cd92287059e` |
| 778 | `results/_tidy_round2_archive_transfer_register_2026_09_30.md` | 27,641 | 2026-09-30 19:20:01 | `1c1365f23c92` |
| 779 | `results/_tmp_disposal_register_2026_10_10.md` | 20,812 | 2026-10-10 12:00:12 | `e0f6b744e826` |
| 780 | `results/_tra_v0_2026_09_10.json` | 3,695 | 2026-09-10 20:20:34 | `0b096048e01d` |
| 781 | `results/_tra_v0_2026_09_10.py` | 12,125 | 2026-09-10 20:20:20 | `d80a8f75a122` |
| 782 | `results/_track2_endpoints_probe_2026_09_23.json` | 5,803 | 2026-09-23 15:15:30 | `c846f7fc79ee` |
| 783 | `results/_track2_qwen_check_2026_09_23.json` | 2,513 | 2026-09-23 14:22:00 | `727d1ffc7f3f` |
| 784 | `results/_track2_qwen_check_2026_09_23.py` | 12,078 | 2026-09-23 14:21:43 | `3ddba570c221` |
| 785 | `results/_trigger_denominator_caliber_judgment_2026_10_11.md` | 43,448 | 2026-10-11 00:12:10 | `16bf9332deef` |
| 786 | `results/_trj_w1_downstream_erratum_2026_10_10.md` | 24,888 | 2026-10-10 18:41:15 | `e52d0016fbc6` |
| 787 | `results/_trj_w1_verification_2026_10_10.md` | 23,014 | 2026-10-10 18:33:08 | `cc6de8e981f6` |
| 788 | `results/_typeb_m_caliber_2026_10_10.md` | 32,830 | 2026-10-10 23:30:45 | `4d067a884c6c` |
| 789 | `results/_typeb_m_definition_judgment_2026_10_10.md` | 41,432 | 2026-10-10 23:15:39 | `97ac7fcc4803` |
| 790 | `results/_typeb_m_registration_2026_10_10.md` | 27,778 | 2026-10-10 23:32:32 | `3b68d3890473` |
| 791 | `results/_u04_1_exemption_precondition_verification_2026_10_09.md` | 21,377 | 2026-10-09 17:26:27 | `c072ffe6110e` |
| 792 | `results/_u11_execution_register_2026_10_09.md` | 24,549 | 2026-10-10 11:37:24 | `8bc087a16f5a` |
| 793 | `results/_u2u3_effectivity_register_2026_10_10.md` | 27,192 | 2026-10-10 13:49:44 | `b00b87cec825` |
| 794 | `results/_u3_carrier_qid_verification_2026_10_11.md` | 21,572 | 2026-10-11 21:31:55 | `6509ae68f778` |
| 795 | `results/_u5_fingerprint_relocation_erratum_2026_10_10.md` | 24,999 | 2026-10-10 15:25:33 | `200c7e4c57cb` |
| 796 | `results/_u5b_citation_surface_revision_2026_10_10.md` | 50,079 | 2026-10-10 16:06:18 | `5cc29c53a422` |
| 797 | `results/_u5b_p_counting_resolution_2026_10_10.md` | 20,086 | 2026-10-10 18:44:20 | `e12e9d9a32c4` |
| 798 | `results/_u6_negative_delta_compatibility_2026_10_11.md` | 20,969 | 2026-10-11 21:35:16 | `1846e917119f` |
| 799 | `results/_u_cf_category_caliber_2026_10_10.md` | 18,976 | 2026-10-10 23:29:45 | `73f181d76169` |
| 800 | `results/_u_cf_reclassification_2026_10_10.md` | 25,698 | 2026-10-10 23:30:49 | `02f910e8795b` |
| 801 | `results/_u_closure_execution_register_2026_10_09.md` | 12,781 | 2026-10-09 09:38:19 | `cbf0c9503284` |
| 802 | `results/_u_r_numbering_attribution_2026_10_11.md` | 5,331 | 2026-10-11 23:21:55 | `53672c23d7f9` |
| 803 | `results/_u_v04_01_criterion_scope_determination_2026_10_01.md` | 27,079 | 2026-10-01 11:05:37 | `e82609024b59` |
| 804 | `results/_unclosed_items_inventory_2026_10_08.md` | 30,219 | 2026-10-08 16:28:20 | `b0e7c74e951e` |
| 805 | `results/_upload_execution_receipt_kimi_2026_09_26.md` | 4,191 | 2026-09-26 22:08:26 | `b4ac31f917f3` |
| 806 | `results/_upload_execution_receipt_kimi_2026_09_30.md` | 4,159 | 2026-09-30 20:21:45 | `20e1f592ca61` |
| 807 | `results/_upload_execution_receipt_kimi_2026_10_01.md` | 4,581 | 2026-10-01 21:06:04 | `a9a9a1d19661` |
| 808 | `results/_upload_guard_mirror_pair_2026_10_08.md` | 23,534 | 2026-10-08 17:11:17 | `d923371cdbce` |
| 809 | `results/_upload_ledger_kimi_2026_09_30.json` | 218,279 | 2026-09-30 20:21:46 | `b17cb8aae62d` |
| 810 | `results/_upload_ledger_kimi_2026_10_01.json` | 43,275 | 2026-10-01 21:06:04 | `79a0fb18683b` |
| 811 | `results/_uv04_field_completeness_fill_2026_10_01.md` | 28,735 | 2026-10-01 14:19:04 | `eb9b8d185f44` |
| 812 | `results/_v2_setup.py` | 3,483 | 2026-09-16 11:01:12 | `73f2b8712a90` |
| 813 | `results/_v2_setup.py._moved_20260924_1830.py` | 3,483 | 2026-09-16 11:01:12 | `73f2b8712a90` |
| 814 | `results/_v2_show_summary.py` | 1,200 | 2026-09-11 11:21:58 | `0012b38ce438` |
| 815 | `results/_v2_show_summary.py._moved_20260924_1830.py` | 1,200 | 2026-09-11 11:21:58 | `0012b38ce438` |
| 816 | `results/_v2_smoketest.py` | 2,040 | 2026-09-16 11:01:12 | `0b6c22c8f379` |
| 817 | `results/_v2_smoketest.py._moved_20260924_1830.py` | 2,040 | 2026-09-16 11:01:12 | `0b6c22c8f379` |
| 818 | `results/_v2_stage1_60cells.py` | 31,556 | 2026-09-16 11:01:12 | `8c7bd12c3a8c` |
| 819 | `results/_v2_stage1_60cells.py._moved_20260924_1830.py` | 31,556 | 2026-09-16 11:01:12 | `8c7bd12c3a8c` |
| 820 | `results/_v2_stage2_f2_drift.py` | 10,798 | 2026-09-16 11:01:12 | `7e9b2fc57d80` |
| 821 | `results/_v2_stage2_f2_drift.py._moved_20260924_1830.py` | 10,798 | 2026-09-16 11:01:12 | `7e9b2fc57d80` |
| 822 | `results/_v2_stage3_f3_strip.py` | 11,803 | 2026-09-16 11:01:12 | `ce4362e325ca` |
| 823 | `results/_v2_stage3_f3_strip.py._moved_20260924_1830.py` | 11,803 | 2026-09-16 11:01:12 | `ce4362e325ca` |
| 824 | `results/_v2_stage4_f4_pdv2.py` | 10,355 | 2026-09-11 11:17:17 | `b84f5aab6faf` |
| 825 | `results/_v2_stage4_f4_pdv2.py._moved_20260924_1830.py` | 10,355 | 2026-09-11 11:17:17 | `b84f5aab6faf` |
| 826 | `results/_v2_stage5_f5_dpath.py` | 6,480 | 2026-09-11 11:16:38 | `e8871b829d89` |
| 827 | `results/_v2_stage5_f5_dpath.py._moved_20260924_1830.py` | 6,480 | 2026-09-11 11:16:38 | `e8871b829d89` |
| 828 | `results/_v2_verify_outputs.py` | 2,656 | 2026-09-11 11:21:39 | `eb0107dd79b5` |
| 829 | `results/_v2_verify_outputs.py._moved_20260924_1830.py` | 2,656 | 2026-09-11 11:21:39 | `eb0107dd79b5` |
| 830 | `results/_v3_02_ethard_closure_verdict_2026_10_09.md` | 27,819 | 2026-10-09 14:03:16 | `aa0f96bb618f` |
| 831 | `results/_v3_02_ethard_execution_register_2026_10_09.md` | 22,007 | 2026-10-09 13:43:03 | `23457f5ce432` |
| 832 | `results/_v3_02_override_register_2026_10_09.md` | 36,245 | 2026-10-09 13:33:36 | `c5441e186c3f` |
| 833 | `results/_v3_05_h_caliber_judgment_2026_10_09.md` | 22,050 | 2026-10-09 22:58:01 | `1c2b5f40e15d` |
| 834 | `results/_v3_recheck_05_executor_2026_09_28.py` | 38,639 | 2026-09-28 13:27:45 | `d6c8bc163e11` |
| 835 | `results/_v3_recheck_10_executor_2026_09_27.py` | 33,647 | 2026-09-27 15:12:15 | `80947906e592` |
| 836 | `results/_v3_recheck_12_executor_2026_09_27.py` | 49,430 | 2026-09-27 16:00:42 | `4850b1cbb010` |
| 837 | `results/_v3_recheck_12_jsv_phase_data_2026_09_27.json` | 17,718 | 2026-09-27 16:20:32 | `642582d4fbd1` |
| 838 | `results/_v3_recheck_19_executor_2026_09_27.py` | 19,215 | 2026-09-27 14:55:27 | `b133a631b1a8` |
| 839 | `results/_v3_recheck_26b_verdict_2026_10_01.md` | 26,309 | 2026-10-01 09:03:39 | `8bbecb15b28b` |
| 840 | `results/_v3_recheck_27_executor_2026_09_27.py` | 34,084 | 2026-09-27 15:17:40 | `190cbe01d061` |
| 841 | `results/_v3_recheck_28_executor_2026_09_27.py` | 17,735 | 2026-09-27 14:47:05 | `4e8c0dd8f54f` |
| 842 | `results/_v3_recheck_prereg_v1p2_2026_09_29.md` | 25,854 | 2026-09-29 18:34:16 | `a667a5f69b7a` |
| 843 | `results/_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md` | 23,152 | 2026-09-24 20:04:58 | `c64146c4ccac` |
| 844 | `results/_v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md` | 37,212 | 2026-09-26 19:18:37 | `24c64cc23907` |
| 845 | `results/_v3_v4_achievements_inventory_3dir_addendum_v2p1_2026_09_26.md` | 17,130 | 2026-09-26 19:45:55 | `4c731a625868` |
| 846 | `results/_v3n_cpath_live_rerun_verdict_2026_10_01.md` | 16,409 | 2026-10-01 09:26:42 | `a91efbfec3d0` |
| 847 | `results/_v3r1_threshold_final_path_judgment_2026_10_10.md` | 39,653 | 2026-10-10 09:58:13 | `93f187f1ab75` |
| 848 | `results/_v3r1_threshold_path4_draft_2026_10_10.md` | 39,077 | 2026-10-10 10:14:38 | `a51f5de630ed` |
| 849 | `results/_v3r1_threshold_restatement_design_2026_10_10.md` | 33,847 | 2026-10-10 01:00:44 | `fb85a8013f9d` |
| 850 | `results/_v3x_18frozen_remeasure_2026_09_16/v3x_18frozen_remeasure_results_2026_09_16.json` | 4,202 | 2026-09-16 23:32:09 | `928794710241` |
| 851 | `results/_v3x_conservation_anchor_2026_09_17.txt` | 940 | 2026-09-17 10:20:17 | `f331a9c2bd22` |
| 852 | `results/_v3x_d0_5_aggregation_2026_09_17.md` | 12,010 | 2026-09-17 13:08:30 | `ddf0d1aa96d2` |
| 853 | `results/_v3x_d0_5_experiment_invitation_2026_09_17.md` | 7,617 | 2026-09-17 09:34:32 | `d8f2b99aa527` |
| 854 | `results/_v3x_d0_5_proposal_coze_2026_09_17.md` | 13,200 | 2026-09-17 11:06:19 | `759c25b21ed4` |
| 855 | `results/_v3x_d0_5_proposal_trae_2026_09_17.md` | 13,254 | 2026-09-20 17:11:14 | `b1c227d54a82` |
| 856 | `results/_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json` | 17,053 | 2026-09-16 12:37:12 | `f39412103366` |
| 857 | `results/_v3x_p_k_verify_2026_09_16/v3x_p_k_verify_results_2026_09_16.json` | 2,059 | 2026-09-16 23:33:03 | `59c2113b7c71` |
| 858 | `results/_v3x_p_l_v3_external_spec_2026_09_17.md` | 5,769 | 2026-09-17 11:03:24 | `6a5b6eb635f0` |
| 859 | `results/_v3x_p_l_v3_mistral_large_2512_20260917_115049.json` | 16,835 | 2026-09-17 11:52:29 | `523b5941c30c` |
| 860 | `results/_v3x_p_l_v3_summary_mistral_large_2512_20260917_115049.md` | 9,570 | 2026-09-17 11:53:50 | `183205baa9ac` |
| 861 | `results/_v4_85_77_attribution_verifier_r1_2026_09_29.md` | 17,727 | 2026-09-29 16:04:04 | `cd8ebaa86e44` |
| 862 | `results/_v4_closeout_bucket_register_2026_10_01.md` | 41,943 | 2026-10-01 10:49:39 | `99355c24a03b` |
| 863 | `results/_v4_concl_t_verify_2026_09_28.md` | 13,237 | 2026-09-28 19:32:52 | `927adba66e9b` |
| 864 | `results/_v4_daily_cleanup_2026_09_28.md` | 25,491 | 2026-09-28 18:29:44 | `f56e6fbf04ef` |
| 865 | `results/_v4_design_integration_2026_09_21_v1.0.md` | 119,732 | 2026-09-21 14:58:33 | `4b10cde29c27` |
| 866 | `results/_v4_design_integration_2026_09_21_v1.1.md` | 140,007 | 2026-09-21 16:33:04 | `fb5656993071` |
| 867 | `results/_v4_final_verify.py` | 4,794 | 2026-09-23 10:49:06 | `1dc482062d9b` |
| 868 | `results/_v4_gA1_experiment_outline_2026_09_22.md` | 7,837 | 2026-09-22 13:13:10 | `f4a6bdd43962` |
| 869 | `results/_v4_gA1_terminology_draft_2026_09_22.md` | 9,818 | 2026-09-22 13:09:56 | `0a2caf0a2bd2` |
| 870 | `results/_v4_gA3_seeds_judgment_draft_2026_09_22.md` | 19,772 | 2026-09-22 15:26:03 | `9119bb791dc1` |
| 871 | `results/_v4_gamma_r1_exec_2026_09_28.md` | 21,496 | 2026-09-28 17:38:42 | `0d946e65ba3c` |
| 872 | `results/_v4_gamma_r1_prereg_2026_09_28.md` | 33,489 | 2026-09-30 16:15:20 | `c9da8678cf2b` |
| 873 | `results/_v4_gamma_r1_prereg_v2_stop_2026_09_28.md` | 17,999 | 2026-09-28 19:36:48 | `9349e2fdb537` |
| 874 | `results/_v4_gamma_r1_sources_20260928_S1.md` | 2,944 | 2026-09-28 17:36:55 | `3d6e997aa692` |
| 875 | `results/_v4_gamma_r1_sources_20260928_S2.md` | 2,647 | 2026-09-28 17:37:02 | `dcec110ca2e0` |
| 876 | `results/_v4_gamma_r1_sources_20260928_S3.md` | 2,554 | 2026-09-28 17:37:12 | `6b9761d710ca` |
| 877 | `results/_v4_gamma_r1_sources_20260928_S4.md` | 3,050 | 2026-09-28 17:37:22 | `16af6baf8463` |
| 878 | `results/_v4_gamma_r1_sources_20260928_S5_faceD.md` | 2,264 | 2026-09-28 17:37:38 | `4f77d49756db` |
| 879 | `results/_v4_group_b_17letters_judgment_draft_2026_09_22.md` | 24,822 | 2026-09-22 16:24:26 | `99b835595dfb` |
| 880 | `results/_v4_group_b_explore_subs_integration_2026_09_22.md` | 20,532 | 2026-09-22 16:31:25 | `588b45430e88` |
| 881 | `results/_v4_item04_closeout_prereg_2026_09_28.md` | 26,719 | 2026-09-28 18:33:05 | `176e2b1c95ae` |
| 882 | `results/_v4_maindir_cleanup_manifest_2026_09_24.md` | 19,104 | 2026-09-24 17:59:34 | `32cc61d394f2` |
| 883 | `results/_v4_maindir_cleanup_manifest_v2_2026_09_26.md` | 27,909 | 2026-09-26 18:43:10 | `f586a5a21584` |
| 884 | `results/_v4_maindir_cleanup_moves_ledger_2026_09_24.md` | 18,829 | 2026-09-24 18:15:50 | `4025e871726b` |
| 885 | `results/_v4_maindir_cleanup_moves_ledger_v2_2026_09_24.md` | 47,909 | 2026-09-24 18:29:40 | `64c4ef850025` |
| 886 | `results/_v4_maindir_cleanup_moves_ledger_v3_2026_09_24.md` | 31,689 | 2026-09-24 19:16:52 | `8f5136e176b8` |
| 887 | `results/_v4_maindir_cleanup_moves_ledger_v4_2026_09_24.md` | 37,047 | 2026-09-24 19:39:04 | `9bd8932fa214` |
| 888 | `results/_v4_maindir_cleanup_moves_ledger_v5_2026_09_24.md` | 46,058 | 2026-09-24 19:58:55 | `272e8c752406` |
| 889 | `results/_v4_noise_cleanup_manifest_v2_2026_09_24.md` | 9,683 | 2026-09-24 21:42:05 | `90253e8342da` |
| 890 | `results/_v4_noise_cleanup_manifest_v3_2026_09_25.md` | 24,491 | 2026-09-25 01:12:20 | `6f3f6fa3ab1d` |
| 891 | `results/_v4_noise_cleanup_manifest_v4_2026_09_27.md` | 38,001 | 2026-09-27 21:19:39 | `82e90ff496ae` |
| 892 | `results/_v4_pending_decisions_2026_09_28.md` | 24,676 | 2026-09-30 16:15:20 | `fe4671517827` |
| 893 | `results/_v4_pi_cot_v2_collection_log.md` | 1,181 | 2026-09-23 17:49:35 | `167ad91f198e` |
| 894 | `results/_v4_pi_cot_v2_prereg_activation_2026_09_23.md` | 1,016 | 2026-09-23 18:03:11 | `00584e5a5c78` |
| 895 | `results/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` | 26,637 | 2026-09-26 19:14:42 | `ba4d07bd7000` |
| 896 | `results/_v4_pi_cot_v3_lock_and_rejudge_register_2026_09_28.md` | 12,152 | 2026-09-28 14:04:07 | `ae154971d1d2` |
| 897 | `results/_v4_r4_cleanup_execution_2026_09_29.md` | 15,357 | 2026-09-29 14:12:44 | `3932b46b16ce` |
| 898 | `results/_v4_r4_key_purge_manifest_2026_09_24.md` | 13,884 | 2026-09-24 18:55:22 | `5bf4d9ad2877` |
| 899 | `results/_v4_r4_purge_actions_2026_09_24.md` | 33,117 | 2026-09-24 19:24:11 | `8bbfe831e7c3` |
| 900 | `results/_v4_rj5_rederive_2026_09_28.md` | 22,145 | 2026-09-28 18:13:12 | `34ec49511ee3` |
| 901 | `results/_v4_rj5_rederive_appendix_2026_09_28.md` | 9,226 | 2026-09-28 18:13:40 | `985673661209` |
| 902 | `results/_v4_slow_cleanup_manifest_2026_09_28.md` | 15,693 | 2026-09-30 16:15:20 | `012501569aea` |
| 903 | `results/_v4_supp_l14v3_batch10_r5_executor.py` | 70,471 | 2026-09-27 20:26:47 | `04383377b6a2` |
| 904 | `results/_v4_supp_l14v3_batch2_r2_models_probe.log` | 1,260 | 2026-09-24 22:40:12 | `5664c63102a0` |
| 905 | `results/_v4_supp_l14v3_batch2_r2_models_probe.py` | 5,334 | 2026-09-27 20:26:47 | `a31d54a4b765` |
| 906 | `results/_v4_supp_l14v3_batch2_r2_result_probe_fail_v1.json` | 2,635 | 2026-09-24 22:43:10 | `21a89eb36a14` |
| 907 | `results/_v4_supp_l14v3_batch2_r6_executor.py` | 63,788 | 2026-09-27 20:26:47 | `e38d068f309c` |
| 908 | `results/_v4_supp_l14v3_batch3_r5_executor.py` | 72,156 | 2026-09-27 20:26:47 | `b7478168f87f` |
| 909 | `results/_v4_supp_l14v3_batch4_r5_verify.py` | 3,050 | 2026-09-25 01:35:07 | `60d19aeee6f5` |
| 910 | `results/_v4_supp_l14v3_batch4_r6_verify.py` | 4,712 | 2026-09-25 01:45:49 | `222972125231` |
| 911 | `results/_v4_supp_l14v3_batch6_r2_report.md` | 6,460 | 2026-09-25 01:15:52 | `080f9caf313c` |
| 912 | `results/_v4_supp_l14v3_batch6_r3_report.md` | 6,354 | 2026-09-25 01:39:41 | `6ef770d61308` |
| 913 | `results/_v4_supp_l14v3_batch6_r4_report.md` | 7,019 | 2026-09-25 01:53:59 | `0d0edc68cd35` |
| 914 | `results/_v4_supp_l14v3_batch6_r5_report.md` | 8,596 | 2026-09-25 02:08:01 | `d339d7286ad8` |
| 915 | `results/_v4_supp_l14v3_batch7_r5_executor.py` | 53,155 | 2026-09-27 20:26:47 | `38710a448e9c` |
| 916 | `results/_v4_supp_l14v3_batch9_r5_executor.py` | 65,672 | 2026-09-27 20:26:47 | `9b1a82a28dfb` |
| 917 | `results/_v4_supp_t15r2_methodology_template.md` | 17,411 | 2026-09-27 11:40:23 | `6f9b865280a3` |
| 918 | `results/_v4_track2_endpoints_probe.py` | 20,738 | 2026-09-27 20:26:47 | `e7a6eb42c0af` |
| 919 | `results/_v4_track2_models_probe.py` | 3,191 | 2026-09-27 20:27:07 | `da62abaa1e03` |
| 920 | `results/_v4_track2_reprobe.py` | 2,860 | 2026-09-27 20:27:07 | `f92cc93f1304` |
| 921 | `results/_v4_trae_remaining_audit_2026_09_28.md` | 39,681 | 2026-09-28 15:28:25 | `1a8648083228` |
| 922 | `results/_v4s3_shadowing_priority_assessment_2026_10_01.md` | 20,111 | 2026-10-01 14:30:41 | `2aaac67603ce` |
| 923 | `results/_v5_a_system_default_register_2026_09_28.md` | 19,892 | 2026-09-28 23:00:28 | `8c22796a42f5` |
| 924 | `results/_v5_agent_trio_post_reorg_note_2026_09_29.md` | 9,795 | 2026-09-29 14:17:11 | `9c7182d93049` |
| 925 | `results/_v5_alias_table_d01_d04_c01_c03_2026_09_29.md` | 15,315 | 2026-09-29 14:10:27 | `b3e39064d7c5` |
| 926 | `results/_v5_anchor_drift_backfill_2026_09_28.md` | 14,438 | 2026-09-28 22:59:46 | `6f1edd1ccebb` |
| 927 | `results/_v5_b12_verify_pack_q1_q3_q4_2026_09_29.md` | 33,803 | 2026-09-29 16:32:42 | `698262e6fe8b` |
| 928 | `results/_v5_b14_08c_material_plan_2026_09_29.md` | 22,104 | 2026-09-29 17:26:18 | `b69d65cbb329` |
| 929 | `results/_v5_b14_3_v1_4_prereg_2026_09_29.md` | 20,045 | 2026-09-29 16:55:29 | `0f1665e7056f` |
| 930 | `results/_v5_b14_4_v1_3_prereg_2026_09_29.md` | 20,043 | 2026-09-29 16:55:31 | `ae474bf48c62` |
| 931 | `results/_v5_b14_p41c_independent_judgment_2026_09_29.md` | 22,437 | 2026-09-29 19:13:24 | `b752582bc692` |
| 932 | `results/_v5_b15_offsite_readonly_authorization_2026_09_29.md` | 18,483 | 2026-09-29 17:33:36 | `96a069701b3d` |
| 933 | `results/_v5_b15_offsite_readonly_authorization_activation_2026_09_29.md` | 35,006 | 2026-09-29 19:40:50 | `99978eb15c10` |
| 934 | `results/_v5_b17_fault_register_2026_09_29.md` | 18,129 | 2026-09-29 17:01:39 | `48cb0ab5f317` |
| 935 | `results/_v5_b17_recheck12_register_2026_09_29.md` | 19,981 | 2026-09-29 17:02:29 | `73242a890be9` |
| 936 | `results/_v5_b18_o8_semantic_verify_2026_09_29.md` | 26,544 | 2026-09-29 20:34:46 | `49d4adf8f197` |
| 937 | `results/_v5_b18_o8_semantic_verify_r2_2026_09_29.md` | 24,145 | 2026-09-29 20:46:30 | `dc1233d0ab4f` |
| 938 | `results/_v5_b20_gamma_a_attribution_2026_09_29.md` | 30,789 | 2026-09-29 17:31:42 | `7bad6e52a0f3` |
| 939 | `results/_v5_b20_gamma_a_rereview_2026_09_29.md` | 30,680 | 2026-09-29 19:01:52 | `b22dda133038` |
| 940 | `results/_v5_b22_r05_path_backfill_2026_09_29.md` | 12,233 | 2026-09-29 18:18:33 | `09b3105acb6f` |
| 941 | `results/_v5_b22_r07_four_cond_prereg_2026_09_29.md` | 23,151 | 2026-09-29 18:27:58 | `ceea8f4534fb` |
| 942 | `results/_v5_b35_result_attribution_2026_09_29.md` | 35,313 | 2026-09-29 17:48:32 | `ec358f6f76a3` |
| 943 | `results/_v5_bom_u1_exec_2026_09_29.md` | 22,730 | 2026-09-29 10:48:46 | `5b0282960d52` |
| 944 | `results/_v5_bom_u1_exec_2026_09_29.py` | 31,134 | 2026-09-29 10:46:21 | `c140a28e15ae` |
| 945 | `results/_v5_clearance_mr10_pb_reembed_prereg_2026_09_29.md` | 18,271 | 2026-09-29 19:24:07 | `c514b321fe10` |
| 946 | `results/_v5_clearance_mr11_doc_calibration_2026_09_29.md` | 14,974 | 2026-09-29 19:30:58 | `c4bce5a5e8be` |
| 947 | `results/_v5_clearance_mr19_sha1_note_2026_09_29.md` | 22,859 | 2026-09-29 19:21:08 | `c74ffc6278a8` |
| 948 | `results/_v5_clearance_mr3_s40_fix_note_2026_09_29.md` | 15,522 | 2026-09-29 19:20:43 | `b1244981065b` |
| 949 | `results/_v5_clearance_o15_ready_pack_2026_09_29.md` | 48,968 | 2026-09-29 18:19:44 | `618e5990b3e5` |
| 950 | `results/_v5_clearance_pending_backlog_register_2026_09_29.md` | 32,369 | 2026-09-29 20:52:20 | `1132072288de` |
| 951 | `results/_v5_clearance_readme_c5_register_2026_09_29.md` | 8,730 | 2026-09-29 21:09:27 | `ababdaa392ca` |
| 952 | `results/_v5_clearance_round11_register_2026_09_29.md` | 59,923 | 2026-09-29 19:12:41 | `2e5e6f8b328e` |
| 953 | `results/_v5_clearance_round12_14_register_2026_09_29.md` | 75,131 | 2026-09-29 19:32:25 | `13d741979ebb` |
| 954 | `results/_v5_clearance_round15_18_register_2026_09_29.md` | 99,989 | 2026-09-29 20:32:07 | `3a3c9c734bf9` |
| 955 | `results/_v5_clearance_round1_b19_register_2026_09_29.md` | 28,556 | 2026-09-29 18:08:51 | `b69ec2ddc9be` |
| 956 | `results/_v5_clearance_round2_3_register_2026_09_29.md` | 37,340 | 2026-09-29 18:25:58 | `32ca90e63a56` |
| 957 | `results/_v5_clearance_round4_5_register_2026_09_29.md` | 52,782 | 2026-09-29 18:35:54 | `9d381fab5f46` |
| 958 | `results/_v5_clearance_round6_register_2026_09_29.md` | 38,248 | 2026-09-29 18:43:49 | `68fe5b397df3` |
| 959 | `results/_v5_clearance_round7_8_register_2026_09_29.md` | 63,311 | 2026-09-29 18:53:57 | `60cdeef91d4a` |
| 960 | `results/_v5_clearance_round9_10_register_2026_09_29.md` | 68,512 | 2026-09-29 19:03:45 | `428e0857ebb7` |
| 961 | `results/_v5_closing_register_r2_2026_09_28.md` | 25,446 | 2026-09-30 17:02:47 | `1094edb6e8c0` |
| 962 | `results/_v5_confirm_b10_decisions_register_2026_09_29.md` | 13,282 | 2026-09-29 14:18:35 | `67ea81a2e6d9` |
| 963 | `results/_v5_confirm_b12_decisions_register_2026_09_29.md` | 15,898 | 2026-09-29 14:24:50 | `db0d6e56a497` |
| 964 | `results/_v5_confirm_b13_b22_anchor_verify_2026_09_29.md` | 16,393 | 2026-09-29 15:26:00 | `a0c2d1d5fe6b` |
| 965 | `results/_v5_confirm_b13_b22_exec_queue_2026_09_29.md` | 39,531 | 2026-09-29 16:59:11 | `56549b04a925` |
| 966 | `results/_v5_confirm_b13_decisions_register_2026_09_29.md` | 33,086 | 2026-09-29 15:14:58 | `c7ca4fbecc8b` |
| 967 | `results/_v5_confirm_b16_b17_decisions_register_2026_09_29.md` | 29,624 | 2026-09-29 15:22:32 | `8e36a3e4c6ff` |
| 968 | `results/_v5_confirm_b18_b19_decisions_register_2026_09_29.md` | 21,072 | 2026-09-29 15:23:32 | `ae160194878e` |
| 969 | `results/_v5_confirm_b1_decisions_register_2026_09_29.md` | 28,469 | 2026-09-29 13:09:11 | `62ca213bb56c` |
| 970 | `results/_v5_confirm_b20_b22_decisions_register_2026_09_29.md` | 24,883 | 2026-09-29 15:24:33 | `fccaac464565` |
| 971 | `results/_v5_confirm_b2_decisions_register_2026_09_29.md` | 28,383 | 2026-09-29 13:13:58 | `63ded68919df` |
| 972 | `results/_v5_confirm_b3_decisions_register_2026_09_29.md` | 34,015 | 2026-09-29 13:24:45 | `4dbb11c219fc` |
| 973 | `results/_v5_confirm_b4_decisions_register_2026_09_29.md` | 43,498 | 2026-09-29 13:33:06 | `4d02f9df594e` |
| 974 | `results/_v5_confirm_b8_decisions_register_2026_09_29.md` | 15,106 | 2026-09-29 14:11:28 | `6862659ff900` |
| 975 | `results/_v5_ea_review_chain_rules_2026_09_29.md` | 11,511 | 2026-09-29 14:13:43 | `8e235f520fb9` |
| 976 | `results/_v5_fake_verdict_forensics_2026_09_28.md` | 35,870 | 2026-09-28 23:22:52 | `1b135d8b1e08` |
| 977 | `results/_v5_familyline_r01_r02_independent_judgment_2026_09_29.md` | 25,392 | 2026-09-29 19:40:23 | `e16e50329c88` |
| 978 | `results/_v5_gamma_end1_rb_clause_addendum_2026_09_29.md` | 10,397 | 2026-09-29 14:08:53 | `bf38e5f0161e` |
| 979 | `results/_v5_gamma_r1_v2_withdraw_2026_09_29.md` | 24,611 | 2026-09-29 10:59:20 | `f4ef22a5f97c` |
| 980 | `results/_v5_gt33_attrib_fill_prereg_2026_09_29.md` | 36,984 | 2026-09-29 12:14:15 | `48742d6cbd03` |
| 981 | `results/_v5_gt33_d5_crossref_note_2026_09_29.md` | 10,989 | 2026-09-29 13:55:24 | `dd50ff801ef7` |
| 982 | `results/_v5_gt8_lowarm_result_2026_09_29_cb132cd5.json` | 26,253 | 2026-09-29 15:21:52 | `c68076c88140` |
| 983 | `results/_v5_gt8_lowarm_verdict_2026_09_29.md` | 32,653 | 2026-09-29 15:50:16 | `9140b6e5970b` |
| 984 | `results/_v5_gt8_lowarm_verdict_r2_2026_09_29.md` | 40,282 | 2026-09-29 19:32:56 | `aff727434aa4` |
| 985 | `results/_v5_gt8f_m1_g1_fail_clause_addendum_2026_09_29.md` | 14,481 | 2026-09-29 14:05:11 | `31e5bd7b4003` |
| 986 | `results/_v5_gt_exec_2026_09_29.json` | 142,217 | 2026-09-29 11:18:07 | `01e95e49b035` |
| 987 | `results/_v5_h231_r07_independent_judgment_2026_09_29.md` | 37,949 | 2026-09-29 19:07:37 | `70025895600a` |
| 988 | `results/_v5_item05_prereg_2026_09_28.md` | 19,115 | 2026-09-28 19:34:42 | `567f0f177699` |
| 989 | `results/_v5_item21_asset_recovery_2026_09_28.md` | 8,793 | 2026-09-28 19:51:41 | `6c80ff43bdd7` |
| 990 | `results/_v5_item21_patched_recompute_2026_09_28.md` | 15,895 | 2026-09-28 20:27:30 | `2c1d85913ccc` |
| 991 | `results/_v5_item21_rerun_conditions_prereg_2026_09_28.md` | 31,429 | 2026-09-28 23:00:28 | `4185bdad6df5` |
| 992 | `results/_v5_item21_strategyqa_realias_recompute_2026_09_29.md` | 14,639 | 2026-09-29 16:17:29 | `4e941d0a9c48` |
| 993 | `results/_v5_item21_strategyqa_realias_verdict_2026_09_29.md` | 32,354 | 2026-09-29 16:45:55 | `26eaa156108f` |
| 994 | `results/_v5_item21_verdict_2026_09_28.md` | 28,155 | 2026-09-28 21:30:15 | `de274bd38955` |
| 995 | `results/_v5_item35_v3_collinear_exec_2026_09_29.md` | 46,000 | 2026-09-29 15:13:22 | `912afffed6b9` |
| 996 | `results/_v5_item35_v3_collinear_verdict_2026_10_01.md` | 38,266 | 2026-10-01 09:05:02 | `363cce3dae59` |
| 997 | `results/_v5_item35_v3_collinear_verdict_prep_2026_10_01.md` | 33,755 | 2026-10-01 08:57:30 | `a31026f2384d` |
| 998 | `results/_v5_item36_prereg_2026_09_28.md` | 18,141 | 2026-09-28 19:35:54 | `7f42d5ee131c` |
| 999 | `results/_v5_loadcorpus_fix_2026_09_29.md` | 17,355 | 2026-09-29 11:58:05 | `e47614ccf5ff` |
| 1000 | `results/_v5_loadcorpus_switch_2026_09_29.md` | 16,414 | 2026-09-29 12:13:38 | `d37e97644bf8` |
| 1001 | `results/_v5_paper_remedy_line_orchestration_2026_09_29.md` | 48,292 | 2026-09-29 14:02:32 | `d911674e68cf` |
| 1002 | `results/_v5_paper_remedy_r1_pledge_2026_09_29.md` | 47,778 | 2026-09-29 16:36:25 | `816cb91d4611` |
| 1003 | `results/_v5_paper_remedy_r2_r4_sourcetrace_2026_09_29.md` | 34,647 | 2026-09-29 15:49:34 | `29da2ca8932f` |
| 1004 | `results/_v5_paper_remedy_r6b_x27_sourcetrace_2026_09_29.md` | 16,125 | 2026-09-29 17:10:36 | `b75cc49b360f` |
| 1005 | `results/_v5_pd_v04_root_naming_candidates_2026_09_29.md` | 14,312 | 2026-09-29 14:06:13 | `46599dde51a8` |
| 1006 | `results/_v5_pi_decision_trace_gap_audit_2026_09_29.md` | 33,101 | 2026-09-29 13:53:25 | `38b043c4be6a` |
| 1007 | `results/_v5_pjpm_pc_degen_precheck_executor_2026_09_29.py` | 76,822 | 2026-09-29 13:46:42 | `f58b0d1c1a93` |
| 1008 | `results/_v5_pjpm_pc_reverify_bang2_2026_09_29.md` | 39,517 | 2026-09-29 14:14:27 | `6833cae407e8` |
| 1009 | `results/_v5_pjpm_pc_verdict_bang3_2026_09_29.md` | 41,566 | 2026-09-29 14:27:08 | `1814f9590f0f` |
| 1010 | `results/_v5_pl2_fourband_prereg_2026_09_29.md` | 29,253 | 2026-09-29 17:42:35 | `d5fdb89582fd` |
| 1011 | `results/_v5_prereg_chain_activation_register_2026_09_28.md` | 27,047 | 2026-09-28 22:10:58 | `3cc05f8cbd1a` |
| 1012 | `results/_v5_prereg_chain_status_annotation_2026_09_28.md` | 23,857 | 2026-09-28 22:28:54 | `cb4104938cc8` |
| 1013 | `results/_v5_proxy_temp_T0.3.json` | 143,345 | 2026-09-23 11:59:01 | `04d915714b96` |
| 1014 | `results/_v5_proxy_temp_T1.5.json` | 143,261 | 2026-09-23 11:59:01 | `2b36d8632a80` |
| 1015 | `results/_v5_proxy_vocab_V50.json` | 78,182 | 2026-09-23 11:59:01 | `2deedc43fc40` |
| 1016 | `results/_v5_proxy_vocab_V500.json` | 78,191 | 2026-09-23 11:59:01 | `4ddd6afbf16b` |
| 1017 | `results/_v5_r4_residual_merged_catalogue_2026_09_29.md` | 102,410 | 2026-09-29 16:43:51 | `0c4bbd26ea55` |
| 1018 | `results/_v5_recyclebin_sha12_completion_2026_09_29.md` | 59,551 | 2026-09-29 16:19:12 | `5f3223a4b349` |
| 1019 | `results/_v5_rj5_verdict_2026_09_29.md` | 40,057 | 2026-09-29 02:05:11 | `9c1ccbd5cf5a` |
| 1020 | `results/_v5_sha12_collision_statement_2026_09_29.md` | 28,155 | 2026-09-29 17:20:57 | `f0f44cf6dc65` |
| 1021 | `results/_v5_sub_artifact_ledger_history_r1_2026_09_29.md` | 48,539 | 2026-09-29 10:56:50 | `535b3c2ad102` |
| 1022 | `results/_v5_sub_artifact_ledger_history_r2_2026_09_29.md` | 150,957 | 2026-09-29 11:42:24 | `5ff7784db145` |
| 1023 | `results/_v5_sub_artifact_ledger_history_r3_2026_09_29.md` | 128,760 | 2026-09-29 12:44:15 | `e04a46b02d13` |
| 1024 | `results/_v5_sub_artifact_ledger_history_r4_2026_09_29.md` | 603,599 | 2026-09-29 16:26:42 | `b6b8be476a73` |
| 1025 | `results/_v5_t1_decisions_register_2026_09_29.md` | 31,330 | 2026-09-29 11:34:08 | `7dd7dd3fb721` |
| 1026 | `results/_v5_theory_input_acquisition_request_2026_09_29.md` | 10,691 | 2026-09-30 20:26:40 | `83afc4802fe7` |
| 1027 | `results/_v5_track2_qwen_retry_2026_09_29.md` | 11,957 | 2026-09-29 11:13:37 | `c890771728f3` |
| 1028 | `results/_v5_track2_qwen_retry_executor_20260929.py` | 11,586 | 2026-09-29 11:10:20 | `d34b46e24a7c` |
| 1029 | `results/_v5_v3_deg_c5_b_halt_report_2026_09_29.md` | 14,862 | 2026-09-29 13:44:25 | `f2b68ee099b5` |
| 1030 | `results/_v5_v3_deg_p1_reopen_exec_2026_09_29.md` | 33,622 | 2026-09-29 13:45:42 | `38231ef6f053` |
| 1031 | `results/_v5_v3_deg_p1_reopen_verdict_2026_09_29.md` | 42,645 | 2026-09-29 15:16:34 | `63d898ab1b71` |
| 1032 | `results/_v5_v3_deg_p1_reopen_verdict_r2_2026_09_29.md` | 44,054 | 2026-09-29 15:24:27 | `8adaf4e5d868` |
| 1033 | `results/_v5_v3_deg_p1_reopen_verify_2026_09_29.md` | 27,898 | 2026-09-29 14:20:21 | `4afeb8cd41de` |
| 1034 | `results/_v5_v3_t1_effect_judgment_2026_09_29.md` | 40,697 | 2026-09-29 20:13:28 | `1995bd4460ae` |
| 1035 | `results/_v5_v3deg_prereg_activation_register_2026_09_29.md` | 24,370 | 2026-09-29 12:19:34 | `e587da3b4cf8` |
| 1036 | `results/_v5_v3r2_errata_note_2026_09_29.md` | 29,089 | 2026-09-29 20:12:47 | `d687ad25a68c` |
| 1037 | `results/_v5_v4_export_filter_spec_2026_09_29.md` | 22,884 | 2026-09-29 17:04:12 | `14dd6ccdbed6` |
| 1038 | `results/_v5_v4_proposal_23item_merged_catalogue_2026_09_29.md` | 14,620 | 2026-09-29 14:16:40 | `79bcff089f21` |
| 1039 | `results/_v5_v4_proposal_23item_merged_catalogue_sourceverify_2026_09_29.md` | 22,185 | 2026-09-29 15:18:09 | `ac0d6f19f06c` |
| 1040 | `results/_verdict_pack_d_prep_2026_10_01.md` | 49,471 | 2026-10-01 13:22:05 | `119f98cd8d2d` |
| 1041 | `results/_vk_current_counting_face_2026_10_10.md` | 24,795 | 2026-10-10 21:35:11 | `4d4e41c3eff5` |
| 1042 | `results/_vk_face_category_erratum_2026_10_11.md` | 17,373 | 2026-10-11 00:15:40 | `67bf70301889` |
| 1043 | `results/_vk_two_items_judgments_2026_10_09.md` | 33,399 | 2026-10-09 23:16:17 | `82556d54726c` |
| 1044 | `results/_volc_22cap_emb.py` | 11,105 | 2026-09-10 17:36:26 | `15904ecae629` |
| 1045 | `results/_wordlist_house_effectivity_note_2026_10_10.md` | 14,606 | 2026-10-10 12:01:03 | `4e89a5bb4b68` |
| 1046 | `results/_wordlist_house_establishment_draft_2026_10_10.md` | 38,468 | 2026-10-10 02:43:26 | `afa5eb53d216` |
| 1047 | `results/_worker_openrouter_rag_run.py` | 24,113 | 2026-09-16 11:01:12 | `4458ccf3d64a` |
| 1048 | `results/_wrapup_cleanup_inventory_register_2026_09_29.md` | 22,556 | 2026-09-29 21:31:56 | `6beeb397a4c1` |
| 1049 | `results/_zero_consumption_cells_field_correction_2026_10_10.md` | 12,244 | 2026-10-10 20:17:54 | `36f9ac4ebbf6` |
| 1050 | `results/_zero_reading_judgment_2026_10_10.md` | 27,824 | 2026-10-10 21:28:00 | `a9947f5677df` |
| 1051 | `results/attack_pc_a1_resampling_2026_09_15.json` | 1,017 | 2026-09-15 15:27:35 | `d21912a05d79` |
| 1052 | `results/attack_pc_a2_fitting_2026_09_15.json` | 1,024 | 2026-09-15 15:27:36 | `5a880678c386` |
| 1053 | `results/attack_pc_a3_clipping_2026_09_15.json` | 1,265 | 2026-09-15 15:27:36 | `d74d6b39d1b0` |
| 1054 | `results/boss_pa_1_rbr_rm_result_2026_09_15.json` | 8,753 | 2026-09-15 15:28:10 | `c7c59e0d2f6c` |
| 1055 | `results/boss_pa_2_potential_game_result_2026_09_15.json` | 7,530 | 2026-09-15 15:28:10 | `5c76137d6430` |
| 1056 | `results/boss_pa_3_replicator_dynamics_result_2026_09_15.json` | 9,098 | 2026-09-15 15:28:10 | `d6f233d73c45` |
| 1057 | `results/boss_pc_1_a1_resampling_2026_09_15.json` | 1,017 | 2026-09-15 13:34:48 | `d21912a05d79` |
| 1058 | `results/boss_pc_1_real_2d_ising_2026_09_15.json` | 2,460 | 2026-09-15 15:28:00 | `43d9ce160fc8` |
| 1059 | `results/boss_pc_2_a2_fitting_2026_09_15.json` | 1,024 | 2026-09-15 13:34:48 | `5a880678c386` |
| 1060 | `results/boss_pc_2_real_transverse_ising_2026_09_15.json` | 3,553 | 2026-09-15 15:27:35 | `8933d61b180a` |
| 1061 | `results/boss_pc_3_a3_clipping_2026_09_15.json` | 1,265 | 2026-09-15 13:34:48 | `d74d6b39d1b0` |
| 1062 | `results/boss_pc_3_real_reservoir_2026_09_15.json` | 2,364 | 2026-09-15 15:28:00 | `94b5398be76c` |
| 1063 | `results/boss_pe_1_real_2d_ising_2026_09_15.json` | 2,460 | 2026-09-15 13:34:49 | `43d9ce160fc8` |
| 1064 | `results/boss_pe_2_real_transverse_ising_2026_09_15.json` | 3,553 | 2026-09-15 13:34:49 | `8933d61b180a` |
| 1065 | `results/boss_pe_3_real_reservoir_2026_09_15.json` | 2,364 | 2026-09-15 13:34:49 | `94b5398be76c` |
| 1066 | `results/c5_b_group_verdict_2026_10_01.md` | 30,118 | 2026-10-01 09:53:17 | `3fbf6b38a383` |
| 1067 | `results/c5_protocol_version_annex_2026_10_01.md` | 18,558 | 2026-10-01 10:25:17 | `2593ea7b93cf` |
| 1068 | `results/d7_5anchor_60cells_9model_verdict_2026_09_18.json` | 2,456 | 2026-09-16 11:00:06 | `4505cca79c15` |
| 1069 | `results/deposon_3risk_v0_fixes_2026_09_11.json` | 8,338 | 2026-09-11 17:16:56 | `d87c0327a6fb` |
| 1070 | `results/deposon_ark_models_2026_09_10.json` | 23,296 | 2026-09-10 15:14:46 | `ccc3ea09a7f5` |
| 1071 | `results/deposon_benchmark_v1_3_labelfree.json` | 3,011 | 2026-08-23 00:30:18 | `57f06a426bec` |
| 1072 | `results/deposon_benchmark_v1_3_labelshuffle.json` | 182,322 | 2026-08-23 00:01:28 | `5a7555358be3` |
| 1073 | `results/deposon_benchmark_v1_3_resonant.json` | 3,134 | 2026-08-23 00:30:18 | `769ae8c908c9` |
| 1074 | `results/deposon_benchmark_v1_4_sc5.json` | 12,479 | 2026-08-23 15:14:50 | `c9796d3b3263` |
| 1075 | `results/deposon_deepseek_v41_flash_2026_09_10.json` | 13,373 | 2026-09-10 15:47:09 | `4d7bea150f3a` |
| 1076 | `results/deposon_deepseek_v41_flash_30cells_2026_09_10.json` | 46,432 | 2026-09-10 16:02:21 | `84df447c38df` |
| 1077 | `results/deposon_deepseek_v41_flash_30cells_v2_2026_09_10.json` | 17,549 | 2026-09-10 16:17:05 | `05cde1ca74ef` |
| 1078 | `results/deposon_deepseek_v41_flash_5cells_fix_2026_09_10.json` | 6,748 | 2026-09-10 16:55:12 | `28bad561c328` |
| 1079 | `results/deposon_dpath_cross_modal_runner_2026_09_10.py` | 27,930 | 2026-09-16 11:01:12 | `fb20a6ba5ec6` |
| 1080 | `results/deposon_embedding_dual_2026_09_10.json` | 6,834 | 2026-09-16 11:01:12 | `33f8ac5d4bff` |
| 1081 | `results/deposon_embedding_openrouter_5models_2026_09_10.json` | 12,785 | 2026-09-10 16:55:37 | `0c0d9afd39ac` |
| 1082 | `results/deposon_feshbach_lindblad_sim_2026_09_10.json` | 7,414 | 2026-09-10 22:09:37 | `aa545c67604d` |
| 1083 | `results/deposon_feshbach_rag_30cells_2026_09_10.json` | 64,978 | 2026-09-16 11:01:12 | `508f664ffa44` |
| 1084 | `results/deposon_feshbach_rag_30cells_2026_09_10.py` | 14,343 | 2026-09-16 11:01:12 | `a072e4184e83` |
| 1085 | `results/deposon_g3_arrhenius.json` | 2,284 | 2026-08-23 05:00:55 | `a3de045b5dd7` |
| 1086 | `results/deposon_gpt6_astra_smoke_2026_09_10.json` | 3,500 | 2026-09-10 14:37:29 | `4bf92bfdefda` |
| 1087 | `results/deposon_gpt6_proxy_smoke_2026_09_10.json` | 5,485 | 2026-09-10 15:13:52 | `524b34e319b5` |
| 1088 | `results/deposon_gpt6_proxy_step1_2026_09_10.json` | 1,245 | 2026-09-10 15:13:16 | `2e23115d9d4b` |
| 1089 | `results/deposon_gpt6_proxy_v2_2026_09_10.json` | 5,810 | 2026-09-10 15:47:09 | `a6812512f8f3` |
| 1090 | `results/deposon_gpt6_teamorouter_cn_2026_09_10.json` | 4,855 | 2026-09-10 17:00:24 | `2241567c6efd` |
| 1091 | `results/deposon_gpt6_vpn_smoke_2026_09_10.json` | 3,489 | 2026-09-10 14:53:46 | `3267746e47e9` |
| 1092 | `results/deposon_llm_codingplan_30cells_2026_09_10.json` | 18,634 | 2026-09-10 15:15:24 | `24e4dcbaa4ea` |
| 1093 | `results/deposon_openrouter_5model_30cells_2026_09_10.json` | 31,690 | 2026-09-10 22:47:29 | `b374f80f3b2d` |
| 1094 | `results/deposon_openrouter_embedding_5model_2026_09_10.json` | 9,472 | 2026-09-10 22:24:35 | `45f314f3415c` |
| 1095 | `results/deposon_overseas_open_smoke_2026_09_10.json` | 6,787 | 2026-09-10 14:56:03 | `2481adadcbb9` |
| 1096 | `results/deposon_pf_d1_2026_09_15.json` | 21,933 | 2026-09-15 11:30:53 | `12791772814e` |
| 1097 | `results/deposon_v16_llm_prior_summary.json` | 5,517 | 2026-08-23 20:28:34 | `a7952d9d78db` |
| 1098 | `results/deposon_v1_implementation_calculator_2026_09_10.py` | 10,751 | 2026-09-10 22:21:56 | `121f104012f4` |
| 1099 | `results/deposon_v2_phase2_dual_mainline_2026_09_11.json` | 3,189 | 2026-09-16 11:01:12 | `e337b824c4b9` |
| 1100 | `results/deposon_v2_phase2_f2_2026_09_11.json` | 4,582 | 2026-09-11 11:19:24 | `8b16b611c4db` |
| 1101 | `results/deposon_v2_phase3_f3_2026_09_11.json` | 2,474 | 2026-09-11 11:19:55 | `0b5dca765d16` |
| 1102 | `results/deposon_v2_phase3_strip_reembed_2026_09_11.json` | 4,160 | 2026-09-11 11:33:43 | `8900526d8e3a` |
| 1103 | `results/deposon_v2_phase5_f5_2026_09_11.json` | 2,356 | 2026-09-11 11:16:45 | `889fc57b3b72` |
| 1104 | `results/deposon_v3x_6way_stage2_2026_09_10.json` | 2,741 | 2026-09-10 17:56:17 | `d301bbfed982` |
| 1105 | `results/deposon_v3x_6way_stage3_2026_09_10.json` | 15,943 | 2026-09-10 18:15:22 | `d892a9d3d6ba` |
| 1106 | `results/deposon_v3x_6way_summary_2026_09_10.json` | 1,506 | 2026-09-10 18:17:10 | `63e0798e5843` |
| 1107 | `results/deposon_v41_flash_60cells_v2_2026_09_10.json` | 38,428 | 2026-09-10 17:34:41 | `b1d802a68723` |
| 1108 | `results/deposon_v41_flash_rag_baseline_2026_09_10.json` | 101,484 | 2026-09-10 17:07:49 | `6754d2655e0a` |
| 1109 | `results/deposon_volcengine_7model_smoke_2026_09_10.json` | 5,944 | 2026-09-16 11:01:12 | `eae44cc3b7b2` |
| 1110 | `results/deposon_volcengine_9model_smoke_2026_09_10.json` | 5,328 | 2026-09-16 11:01:12 | `0e5ae7d7d641` |
| 1111 | `results/deposon_volcengine_coding_plan_5cells_2026_09_10.json` | 6,058 | 2026-09-16 11:01:12 | `52aa8901556e` |
| 1112 | `results/deposon_volcengine_coding_plan_catalog_2026_09_10.json` | 2,841 | 2026-09-16 11:01:12 | `c0efb547b9d1` |
| 1113 | `results/deposon_volcengine_doubao_embedding_2026_09_10.json` | 3,303 | 2026-09-16 11:01:12 | `e99783d18139` |
| 1114 | `results/deposon_volcengine_embedding_30cells_2026_09_10.json` | 24,794 | 2026-09-16 11:01:12 | `12be52bc02a7` |
| 1115 | `results/deposon_volcengine_glm_latest_5cells_2026_09_10.py` | 8,112 | 2026-09-16 11:01:12 | `a3ca05aec6fb` |
| 1116 | `results/deposon_volcengine_minimax_m3_30cells_2026_09_10.py` | 11,703 | 2026-09-16 18:20:55 | `218ef1a99f97` |
| 1117 | `results/deposon_volcengine_worker_b_2026_09_10.py` | 13,232 | 2026-09-16 11:01:12 | `401dfd3c27f3` |
| 1118 | `results/deposon_volcengine_worker_c_2026_09_10.py` | 11,692 | 2026-09-16 11:01:12 | `b5eeef1e9bd7` |
| 1119 | `results/Deposon_评估汇总_v1_3_0.json` | 2,811 | 2026-08-22 21:07:01 | `2f02f50c164b` |
| 1120 | `results/llm_prior_cache.json` | 938 | 2026-08-23 20:21:35 | `5f16be89efc5` |
| 1121 | `results/llm_prior_cache_v18_contamination.json` | 639 | 2026-08-23 22:56:14 | `d3f72f67977d` |
| 1122 | `results/llm_prior_cache_v18_contentless.json` | 512 | 2026-08-23 23:17:58 | `7c0d169ef164` |
| 1123 | `results/llm_prior_cache_v18_direction.json` | 2,168 | 2026-08-23 23:04:12 | `023f936f80fb` |
| 1124 | `results/llm_prior_cache_v18_labelshuffle.json` | 1,925 | 2026-08-23 22:56:03 | `8dce6d7618a2` |
| 1125 | `results/manifest_large_files.md` | 3,440 | 2026-08-29 01:26:28 | `e0dc7a8e4c75` |
| 1126 | `results/quizbank_v20.json` | 37,250 | 2026-08-28 20:46:44 | `f6035466ff3d` |
| 1127 | `results/quizbank_v20_big.json` | 104,872 | 2026-08-28 23:54:09 | `da6fecdcbbf6` |
| 1128 | `results/skill_a_p_a_60cells_result_2026_09_11.json` | 2,220 | 2026-09-11 17:06:25 | `f4a210d69220` |
| 1129 | `results/skill_b_p_c_alpha_beta_result_2026_09_11.json` | 12,609 | 2026-09-11 17:06:29 | `b921002e4dfb` |
| 1130 | `results/skill_c_p_e_3modality_result_2026_09_11.json` | 5,271 | 2026-09-11 17:06:33 | `470425a8c77d` |
| 1131 | `results/skill_d_p_f_observer_result_2026_09_11.json` | 11,010 | 2026-09-15 13:31:05 | `0207c01b9562` |
| 1132 | `results/v19_edges_audit_input.csv` | 2,186 | 2026-08-28 15:53:28 | `8b6682181392` |
| 1133 | `results/v20_graph_features.csv` | 2,151 | 2026-08-28 20:43:58 | `f95f382ace44` |
| 1134 | `results/v20_regression_field.json` | 5,396 | 2026-08-28 20:44:45 | `534c121765b1` |
| 1135 | `results/v20_regression_field_v2.json` | 4,236 | 2026-08-28 20:45:20 | `3596490e1fc0` |
| 1136 | `results/v20_statcheck_fm_vs_deg.json` | 988 | 2026-08-28 20:44:25 | `dfe014c627ca` |
| 1137 | `results/v20_statcheck_fm_vs_rand.json` | 868 | 2026-08-28 20:44:24 | `1dadfaeb2c43` |
| 1138 | `tmp_movedout_2026_09_28/_cleanup_classify_2026_09_28.py` | 3,232 | 2026-09-28 18:17:11 | `efb57dc056f0` |
| 1139 | `tmp_movedout_2026_09_28/_cleanup_classify_out_2026_09_28.txt` | 11,347 | 2026-09-28 18:17:58 | `e1f9db7e1cab` |
| 1140 | `tmp_movedout_2026_09_28/_cleanup_probe_2026_09_28.py` | 2,556 | 2026-09-28 18:14:13 | `20bd0972fa00` |
| 1141 | `tmp_movedout_2026_09_28/_cleanup_probe_out_2026_09_28.txt` | 12,365 | 2026-09-28 18:14:33 | `75f9058f8a51` |
| 1142 | `tmp_movedout_2026_09_28/_cleanup_resolve_2026_09_28.py` | 2,735 | 2026-09-28 18:19:07 | `57085a643c33` |
| 1143 | `tmp_movedout_2026_09_28/_cleanup_resolve_out_2026_09_28.txt` | 1,257 | 2026-09-28 18:19:25 | `1d163e68ed25` |
| 1144 | `tmp_movedout_2026_09_28/_cleanup_transfer_scan_2026_09_28.py` | 3,229 | 2026-09-28 18:25:29 | `97291768f38d` |
| 1145 | `tmp_movedout_2026_09_28/_cleanup_transfer_scan_out_2026_09_28.txt` | 5,017 | 2026-09-28 18:25:45 | `04d99d651df9` |
| 1146 | `tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/_old_corpus_view.py` | 23,893 | 2026-08-29 01:14:15 | `7d8d6a30dd8c` |
| 1147 | `tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/annotate_baseline.py` | 2,050 | 2026-09-29 12:08:25 | `be710bb0c40f` |
| 1148 | `tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/applied_diff.txt` | 5,134 | 2026-09-29 12:11:55 | `05c4704ee5cc` |
| 1149 | `tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/apply_fix.py` | 3,460 | 2026-09-29 13:39:20 | `c3808483722e` |
| 1150 | `tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/baseline_post.json` | 115,634 | 2026-09-29 12:11:10 | `5cdf357a45e8` |
| 1151 | `tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/baseline_pre.json` | 115,139 | 2026-09-29 12:05:24 | `c5e0497b9020` |
| 1152 | `tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/mindmap_corpus_v20.py.orig_7d8d6a30dd8c.bak` | 23,893 | 2026-08-29 01:14:15 | `7d8d6a30dd8c` |
| 1153 | `tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/snapshot.py` | 1,438 | 2026-09-29 12:05:09 | `dcede756619f` |
| 1154 | `tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/verify_2026_09_29.py` | 11,167 | 2026-09-29 13:39:08 | `a1c70189ebbb` |
| 1155 | `tmp_movedout_2026_10_01/_docwriter_wt2_enum_final_2026_09_30.tsv` | 66,339 | 2026-09-30 18:01:38 | `53c4c15c4e06` |
| 1156 | `tmp_movedout_2026_10_01/legacy_caliber/README_V1_LEGACY.md` | 3,756 | 2026-08-23 07:47:23 | `18e095c85427` |
| 1157 | `tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s1b_inv2_2026_09_27.py` | 1,546 | 2026-09-27 20:18:50 | `af475f496a5e` |
| 1158 | `tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s2_scan_2026_09_27.py` | 4,000 | 2026-09-27 20:19:13 | `c2cc22b27047` |
| 1159 | `tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s3_keyscan_2026_09_27.py` | 2,647 | 2026-09-27 20:19:48 | `a32af07111df` |
| 1160 | `tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s3b_uuidctx_2026_09_27.py` | 1,707 | 2026-09-27 20:20:08 | `8fdec59aa96b` |
| 1161 | `tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s3c_keydetail_2026_09_27.py` | 2,490 | 2026-09-27 20:20:25 | `16ae5764add1` |
| 1162 | `tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s4_verify_2026_09_27.py` | 2,812 | 2026-09-27 20:25:11 | `dbe00430d769` |
| 1163 | `tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s6_unrefscan_2026_09_27.py` | 2,495 | 2026-09-27 20:26:11 | `1b31a3111a86` |
| 1164 | `tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s7_fix_2026_09_27.py` | 6,101 | 2026-09-27 20:26:39 | `fc200e5f343d` |
| 1165 | `tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s8_fix3_2026_09_27.py` | 3,514 | 2026-09-27 20:26:58 | `051dbdb121c9` |
| 1166 | `tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s9_final_2026_09_27.py` | 3,399 | 2026-09-27 20:27:53 | `aef86f53cc0e` |
| 1167 | `tmp_movedout_2026_10_01/process_scripts/v4_wt_2026_09_27/_v4_wt_s5_verify_2026_09_27.py` | 4,950 | 2026-09-27 20:08:06 | `736e56cd5553` |
| 1168 | `tmp_movedout_2026_10_01/process_scripts/v5_wa_2026_09_30/_v5_wa_s1_2026_09_30.py` | 4,351 | 2026-09-30 19:02:06 | `f77f72f7b86e` |
| 1169 | `tmp_movedout_2026_10_01/process_scripts/v5_wa_2026_09_30/_v5_wa_s2b_2026_09_30.py` | 3,583 | 2026-09-30 19:03:43 | `9403dfac5824` |
| 1170 | `tmp_movedout_2026_10_01/process_scripts/v5_wa_2026_09_30/_v5_wa_s2c_2026_09_30.py` | 3,168 | 2026-09-30 19:04:28 | `2f55832a82cb` |
| 1171 | `tmp_movedout_2026_10_01/process_scripts/v5_wa_2026_09_30/_v5_wa_s3_fix_2026_09_30.py` | 4,742 | 2026-09-30 19:06:08 | `ff16d68fdb81` |
| 1172 | `tmp_movedout_2026_10_01/process_scripts/volcengine_补测_worker_A_2026_09_10.py` | 16,252 | 2026-09-16 11:01:12 | `20b8a2f54ad9` |
| 1173 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_asset_recount_2026_09_30.md` | 9,441 | 2026-09-30 19:26:23 | `e56286e6cba0` |
| 1174 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_letter_review_bob_w3_commission_2026_09_30.md` | 10,286 | 2026-09-30 19:28:23 | `efe451595a16` |
| 1175 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v4_01_knifeedge_independent_review_2026_09_29.md` | 19,731 | 2026-09-29 15:49:57 | `a66b4159793f` |
| 1176 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v4_tmp_cleanup_2026_09_28.md` | 5,131 | 2026-09-28 18:05:44 | `b8338bdd33f2` |
| 1177 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b14_1_k04_caliber_fixation_2026_09_29.md` | 13,127 | 2026-09-29 16:51:32 | `697145c8352d` |
| 1178 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b14_r3_anchor_retrieval_2026_09_29.md` | 23,023 | 2026-09-29 18:56:44 | `6e0a1461a688` |
| 1179 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b16_1dcritical_lit_search_2026_09_29.md` | 26,931 | 2026-09-29 17:20:00 | `09ad0c6ce46a` |
| 1180 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b16_dual_caliber_rule_2026_09_29.md` | 16,262 | 2026-09-29 17:11:44 | `3b7dfdce494e` |
| 1181 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b16_idx23_blindrate_verify_2026_09_29.md` | 19,755 | 2026-09-29 17:28:04 | `430588419975` |
| 1182 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b16_mq11_case_2026_09_29.md` | 16,723 | 2026-09-29 17:17:10 | `85f92c8d18d1` |
| 1183 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b17_three_caliber_fixation_2026_09_29.md` | 19,709 | 2026-09-29 17:12:46 | `d47b5e067c1c` |
| 1184 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b18_coding_caliber_2026_09_29.md` | 14,304 | 2026-09-29 17:00:32 | `04f6890dc4a8` |
| 1185 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b18_single_count_fixation_2026_09_29.md` | 13,608 | 2026-09-29 17:01:41 | `006e316bfe4c` |
| 1186 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_glm_charlie_reread_ac74a04efeb2_2026_09_29.md` | 18,514 | 2026-09-29 16:01:34 | `bf0874456a58` |
| 1187 | `volcengine_glm_latest_30cells_v2_runner_2026_09_10.py` | 20,745 | 2026-09-18 13:48:17 | `26ff34bfcc79` |

## §5 · 三面计数并列（⛔ 0 校正 ／ 0 择一 ／ 0 静默合并）

### §5.1 义-1 读法：三目录计数并列表

| 目录面 | 件数 | bytes | 来源 | 状态 |
|:--|--:|--:|:--|:--|
| MAIN（`deposon-repo`） | **1,704** | 54,847,017 | 本棒实测 2026-10-12 03:20:44 | ✅ |
| SUB（`deposon-sub`） | **1,187** | 58,731,756 | 本棒实测 2026-10-12 03:20:44 | ✅ |
| ARCHIVE（`_non_upload_local_archive`） | **未核得** | **未核得** | —— | 🔴 **禁触区 · 本棒 0 读 0 写 0 列目录** |
| **三面合计** | **未核得**（缺 ARCHIVE 面） | **未核得** | —— | 🔴 **不填估值** |

📌 **两区比**：MAIN : SUB ＝ **1704 : 1187 ≈ 1.44 : 1**（③段-① 整理前为 2,541 : 517 ≈ 4.91 : 1 ⇒ **拉平后比值收窄**，此为时点事实登记）。

### §5.2 义-2 读法：三独立计数面并列表

| 计数面 | REPO 件数 | SUB 件数 | 时点/来源 |
|:--|--:|--:|:--|
| 面-A：**本棒实测** | **1,704** | **1,187** | 2026-10-12 03:20:44 |
| 面-B：终态快照登记（`6039a6e08017` §1） | 1,699 | 1,187 | 2026-10-12 03:0x |
| 面-C：派工单转录 | 1,700 | 1,187 | parent 2026-10-12 03:14 转录 |

**三面并列（0 校正）**：面-A vs 面-B 差 **+5 件**（REPO）｜面-A vs 面-C 差 **+4 件**（REPO）｜SUB 三面同值 1,187 ✅。**差异一律登记不改**，归口「V4 收尾整理」时点批量校正（沿 §2.2 之口径复核）。

📌 **面-A 偏高的可核事实**：实测期间（03:16:00）`results/_stage3_1_bulk_reorg_completion_register_2026_10_12.md`（15,818 bytes）落地于 REPO ⇒ 该件即面-B→面-A 增量之一。**⛔ 0 断言此为唯一差额来源**（并发写入面，见 §8 D-4）。

### §5.3 目录内计数差并列表（`.tmp` 面）

| 计数面 | `.tmp/` 件数 | 来源 |
|:--|--:|:--|
| 面-A：本棒实测 | **441** | 2026-10-12 03:20:44 |
| 面-B：终态快照登记 | 441 | `6039a6e08017` §2 |
| 面-C：派工单转录 | 560 | parent 转录 |

**三面并列（0 校正）**：面-A ＝ 面-B ＝ **441** ✅；**面-C 与前二者差 −119 件** ⇒ 并列登记，**⛔ 0 校正、⛔ 0 断言面-C 之成因**。

## §6 · 与 `closing_round` 册逐份对齐

**册件**：`results/_closing_round_8_decisions_register_2026_10_09.md`｜**SHA-12（实测）**＝ `a28a478e14a8`｜**bytes** ＝ 2,151｜**mtime** ＝ 2026-10-09 10:12:53

**对齐口径**：以册 §1 四答 ＋ §2 四棒为**左列**，以其**盘上落地产件**为**右列**；⛔ **0 判定「已毕/未毕」**，⛔ **0 宣告闭开**——仅作**件级在盘对齐**。

| 册条目 | 册原文要点 | 盘上落地产件（区） | SHA-12 | 对齐 |
|:--|:--|:--|:--|:--|
| **§1 Q1 · G4 路径** | 丙·M＋P＋R 全授权（含 runtime 改造） | `results/_g4_controlled_reproduction_design_2026_10_09.md`<br>`SUB/2026-10-09 09:47:11`<br>`results/_g4_reproduction_execution_register_2026_10_09.md`<br>`SUB/2026-10-09 10:21:25`<br>`results/_g4_e3_definition_ruling_material_2026_10_09.md`<br>`SUB/2026-10-09 11:07:09`<br>`results/_g4_e3_definition_independent_judgment_2026_10_09.md`<br>`SUB/2026-10-09 12:33:36` | `b1c7c24926bb`<br>`4daaf68cbf0e`<br>`8ae4016bb41d`<br>`aebaff5b503c` | ✅ 在盘（4 件） |
| **§1 Q2 · S4 补样** | 乙·授权采集棒按 d1fill 同款管道推进 | `results/_s4_substrate_topup_collection_register_2026_10_09.md`<br>`REPO/2026-10-09 10:20:29`<br>`results/_s4_substrate_topup_addendum_2026_10_09.json`<br>`REPO/2026-10-09 13:53:09` | `33c1a818ef4f`<br>`1780542f0014` | ✅ 在盘（2 件） |
| **§1 Q3 · T1 修订案** | 甲·全案采认；生效即锁；授权 qwen 温扫起跑 | `results/_t1_prereg_revision_qwen_temp_sweep_2026_10_09.md`<br>`REPO/2026-10-09 10:03:07`<br>`results/_t1_qwen_temp_sweep_executor_2026_10_09.py`<br>`REPO/2026-10-09 10:22:20` | `bda5d5f3dfa0`<br>`f0c845864603` | ✅ 在盘（2 件） |
| **§1 Q4 · 六项打包** | 按左档打包过（①许可 ②维持口径 ③不补注 ④维持留候 ⑤暂不联络 ⑥并陈） | `results/_questionnaire_cards_intake_register_2026_10_09.md`<br>`REPO/2026-10-09 18:10:16` | `d917180db36f` | ✅ 在盘（1 件） |
| **§2 棒① S4 补样采集棒** | `bg_ad0e30ec-…`（worker） | `results/_s4_substrate_topup_collection_register_2026_10_09.md`<br>`REPO/2026-10-09 10:20:29` | `33c1a818ef4f` | ✅ 在盘（1 件） |
| **§2 棒② G4 复现执行棒** | `bg_1efd47e6-…`（worker；M→P→R） | `results/_g4_reproduction_execution_register_2026_10_09.md`<br>`SUB/2026-10-09 10:21:25` | `4daaf68cbf0e` | ✅ 在盘（1 件） |
| **§2 棒③ T1 qwen 温扫棒** | `bg_384f2598-…`（worker） | `results/_t1_qwen_temp_sweep_executor_2026_10_09.py`<br>`REPO/2026-10-09 10:22:20` | `f0c845864603` | ✅ 在盘（1 件） |
| **§2 棒④ 待启（槽位制）** | W4 波（V3-02/04/05/12）；U6 销项＋勘误；上传防护备行 | `results/_upload_guard_mirror_pair_2026_10_08.md`<br>`SUB/2026-10-08 17:11:17` | `d923371cdbce` | ✅ 在盘（1 件） |

📌 **对齐限度声明**：册 §2 棒④ 为「**待启（槽位制）**」之**多项目合列**（W4 波／U6 销项＋勘误／上传防护备行），本件仅能对齐其中**上传防护备行**一员（`_upload_guard_mirror_pair_2026_10_08.md`，在 **SUB** 区）⇒ **W4 波与 U6 两项：未核得（按名未命中，本棒 0 扩大检索面）**，见 §9-N3。

📌 **册件区面**：`_upload_guard_mirror_pair_2026_10_08.md` 现**在 SUB 区**；`results/_stage_sequence_violation_register_2026_10_12.md` 曾以「🟢 在盘 ＝ `d923371cdbce`·23,534 B」登记之 ⇒ **登记指纹与实测指纹之并陈**见 §8 **D-5**（⛔ 0 断言成因，⛔ 0 校正）。

## §7 · 10-10 → 10-12 增量专章（**471 件**，逐件附 SHA-12）

**窗口口径**：mtime ≥ `2026-10-10 00:00:00`（本棒实测切面）；**0 校正** ＋ **0 择一**；本表为 §4 之**子集视图**，**0 重复计数**。

| 日期 | 件数 | bytes | 归段（仅列具名段标者，⛔ 0 推断） |
|:--|--:|--:|:--|
| 2026-10-10 | 323 | 15,008,613 | 0 具名段标（未归段） |
| 2026-10-11 | 114 | 3,935,474 | 具名段标者 6 件 |
| 2026-10-12 | 34 | 1,584,703 | 具名段标者 8 件 |
| **合计** | **471** | **20,528,790** | —— |

### §7.1 分日逐件

#### 2026-10-10（323 件）

| # | 区 | 相对路径 | bytes | mtime | SHA-12 | 类别 |
|---:|:--|:--|--:|:--|:--|:--|
| 1 | SUB | `results/_t1_d7_reading_line_judgment_2026_10_10.md` | 28,559 | 2026-10-10 00:18:41 | `60bd9ae98640` | 成果面 |
| 2 | REPO | `results/_questionnaire_cards_intake_register_supplement_2_2026_10_10.md` | 262,542 | 2026-10-10 00:23:35 | `dc43e3cb7610` | 成果面 |
| 3 | SUB | `results/_round20_approvals_effect_register_2026_10_10.md` | 27,711 | 2026-10-10 00:24:02 | `29d737c59e8b` | 成果面 |
| 4 | SUB | `results/_t1p2_enable_judgment_2026_10_10.md` | 20,132 | 2026-10-10 00:30:13 | `1e97d06b6ec9` | 成果面 |
| 5 | SUB | `results/_t1p2_escalation_judgment_2026_10_10.md` | 22,930 | 2026-10-10 00:30:53 | `5f43775a3224` | 成果面 |
| 6 | SUB | `results/_round19_followup_round21_22_approvals_effect_register_2026_10_10.md` | 54,850 | 2026-10-10 00:31:15 | `0c8dba07dd1e` | 成果面 |
| 7 | SUB | `results/_t1p2_judgment_bytes_correction_2026_10_10.md` | 6,377 | 2026-10-10 00:31:40 | `d9d29bec3a0b` | 成果面 |
| 8 | REPO | `results/_archive_2026-10-12/superseded_variants/_card23_readout_utf8.txts` | 5,088 | 2026-10-10 00:37:18 | `4aa127d1dc62` | 成果面 |
| 9 | SUB | `results/_kv3s_4_4_review_carryover_2026_10_10.md` | 17,606 | 2026-10-10 00:38:39 | `660d40ddd78c` | 成果面 |
| 10 | SUB | `results/_kv3s_4_4_carryover_bytes_correction_2026_10_10.md` | 5,807 | 2026-10-10 00:39:05 | `0a7d2ccf74ad` | 成果面 |
| 11 | SUB | `results/_s4_empty_sequence_backfill_assessment_2026_10_10.md` | 28,771 | 2026-10-10 00:40:54 | `41b75ffea7be` | 成果面 |
| 12 | SUB | `results/_id_face_revision_sync_note_2026_10_10.md` | 20,690 | 2026-10-10 00:43:53 | `5d6c473731c4` | 成果面 |
| 13 | SUB | `results/_q3_reported_value_errata_supplement_2026_10_10.md` | 12,499 | 2026-10-10 00:47:10 | `e026f20839b1` | 成果面 |
| 14 | SUB | `results/_v3r1_threshold_restatement_design_2026_10_10.md` | 33,847 | 2026-10-10 01:00:44 | `fb85a8013f9d` | 成果面 |
| 15 | SUB | `results/_alt_delib_pkg3_two_judgments_2026_10_10.md` | 38,032 | 2026-10-10 01:06:09 | `3f52709a48e8` | 成果面 |
| 16 | SUB | `results/_s4_keyword_expansion_and_regen_design_2026_10_10.md` | 31,149 | 2026-10-10 01:11:17 | `6efddab54ca5` | 成果面 |
| 17 | REPO | `.tmp/gen_supp3.py` | 15,813 | 2026-10-10 01:11:45 | `eb53c9ce140c` | 噪声面 |
| 18 | REPO | `results/_questionnaire_cards_intake_register_supplement_3_2026_10_10.md` | 67,225 | 2026-10-10 01:12:02 | `11681f0ad861` | 成果面 |
| 19 | SUB | `results/_round23_26_threshold_review_effect_register_2026_10_10.md` | 47,297 | 2026-10-10 01:15:09 | `9b0c62765576` | 成果面 |
| 20 | SUB | `results/_149_face_effect_disposal_2026_10_10.md` | 24,295 | 2026-10-10 01:15:42 | `e7c1232df138` | 成果面 |
| 21 | REPO | `.tmp/_s4_tree_construct_probe_2026_10_10.py` | 8,643 | 2026-10-10 01:23:46 | `e1073738b40d` | 噪声面 |
| 22 | REPO | `results/_s4_tree_construct_adjustment_assessment_2026_10_10.md` | 33,453 | 2026-10-10 01:25:59 | `016c7dacaa54` | 成果面 |
| 23 | REPO | `.tmp/_t1_exp2_c_records.json` | 6,277,328 | 2026-10-10 02:31:55 | `f53681c7569a` | 噪声面 |
| 24 | REPO | `results/_t1_exp2_result_2026_10_09.json` | 35,239 | 2026-10-10 02:33:06 | `d9ccd75c652b` | 成果面 |
| 25 | SUB | `results/_t1_exp2_exec_register_2026_10_09.md` | 18,597 | 2026-10-10 02:34:26 | `3a08dcfa8c7f` | 成果面 |
| 26 | SUB | `results/_wordlist_house_establishment_draft_2026_10_10.md` | 38,468 | 2026-10-10 02:43:26 | `afa5eb53d216` | 成果面 |
| 27 | REPO | `results/_bayesian_baseline_design_2026_10_10.md` | 29,783 | 2026-10-10 02:45:24 | `7e181a167702` | 成果面 |
| 28 | SUB | `results/_t1_exp2_verdict_2026_10_10.md` | 48,298 | 2026-10-10 02:47:15 | `15c1c4b317a0` | 成果面 |
| 29 | REPO | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 55,605 | 2026-10-10 02:54:17 | `f4e145b090b1` | 成果面 |
| 30 | SUB | `results/_kd_legacy_rewrite_plan_2026_10_10.md` | 17,643 | 2026-10-10 02:57:52 | `a9698fed8b9b` | 成果面 |
| 31 | SUB | `results/_exp03_blade_caliber_review_2026_10_10.md` | 19,797 | 2026-10-10 03:00:34 | `8c030758b331` | 成果面 |
| 32 | SUB | `results/_exp05_negative_probe_rescan_2026_10_10.md` | 11,566 | 2026-10-10 03:06:08 | `ca7ff556fd7a` | 成果面 |
| 33 | SUB | `results/_exp06_kcf4_check_bit_landing_2026_10_10.md` | 20,709 | 2026-10-10 03:06:42 | `088ba3d58c0f` | 成果面 |
| 34 | SUB | `results/_exp08_s4_prompt_face_register_2026_10_10.md` | 11,929 | 2026-10-10 03:07:20 | `83109ecf440e` | 成果面 |
| 35 | SUB | `results/_reading_face_basis_rejudge_2026_10_10.md` | 24,208 | 2026-10-10 03:13:46 | `3fe193a2a01f` | 成果面 |
| 36 | SUB | `results/_overnight_delivery_index_2026_10_10.md` | 35,344 | 2026-10-10 03:23:28 | `266d0327025d` | 成果面 |
| 37 | SUB | `results/_t1_temp_axis_retirement_judgment_2026_10_10.md` | 27,384 | 2026-10-10 09:43:25 | `19afc7e191a7` | 成果面 |
| 38 | SUB | `results/_s4_regen_traceability_judgment_2026_10_10.md` | 36,071 | 2026-10-10 09:44:42 | `a330273b981c` | 成果面 |
| 39 | SUB | `results/_blade_caliber_b8_judgment_2026_10_10.md` | 28,738 | 2026-10-10 09:51:16 | `e189d6eb63d9` | 成果面 |
| 40 | REPO | `.tmp/_s4_tree_construct_exec_2026_10_10.py` | 34,265 | 2026-10-10 09:51:36 | `4cbd10b61aae` | 噪声面 |
| 41 | REPO | `results/_s4_tree_construct_adjusted_readings_2026_10_10.json` | 108,593 | 2026-10-10 09:51:47 | `a7aa4e9c8d47` | 成果面 |
| 42 | SUB | `results/_s4_tree_construct_adjustment_exec_2026_10_10.md` | 28,515 | 2026-10-10 09:55:59 | `b6b47008f8fd` | 成果面 |
| 43 | SUB | `results/_v3r1_threshold_final_path_judgment_2026_10_10.md` | 39,653 | 2026-10-10 09:58:13 | `93f187f1ab75` | 成果面 |
| 44 | REPO | `results/_archive_2026-10-12/pycache_sink/deposon_team_plugins_pycache/boss_pa_1_rbr_rm_v3df_p1_reopen_2026_09_29.cpython-314.pyc` | 103,946 | 2026-10-10 10:03:53 | `74467bb37f95` | 成果面 |
| 45 | REPO | `.tmp/exp04_h_contrast_2026_10_10.py` | 14,333 | 2026-10-10 10:04:20 | `572f1b9c3927` | 噪声面 |
| 46 | REPO | `results/_exp04_h_contrast_readings_2026_10_10.json` | 72,704 | 2026-10-10 10:05:05 | `106e8667be2d` | 成果面 |
| 47 | REPO | `results/_exp04_h_contrast_readings_2026_10_10.md` | 17,386 | 2026-10-10 10:06:54 | `ac571bfe4d1d` | 成果面 |
| 48 | REPO | `.tmp/_dump_dkb3_records_2026_10_10.py` | 1,781 | 2026-10-10 10:11:13 | `144b204237bf` | 噪声面 |
| 49 | REPO | `.tmp/_dump_dkb3_records2_2026_10_10.py` | 1,366 | 2026-10-10 10:12:37 | `e71d1e81da64` | 噪声面 |
| 50 | SUB | `results/_v3r1_threshold_path4_draft_2026_10_10.md` | 39,077 | 2026-10-10 10:14:38 | `a51f5de630ed` | 成果面 |
| 51 | SUB | `results/_s4_dkb_backfill_register_2026_10_10.md` | 25,591 | 2026-10-10 10:26:50 | `3a992c3fe235` | 成果面 |
| 52 | SUB | `results/_t1_exp2_verdict_bytes_correction_2026_10_10.md` | 13,480 | 2026-10-10 10:29:40 | `e863ca5fb157` | 成果面 |
| 53 | REPO | `.tmp/_verify_r32_card_2026_10_10.py` | 631 | 2026-10-10 10:30:11 | `61f99fc5fdb9` | 噪声面 |
| 54 | REPO | `.tmp/exp06_supplement_probe_2026_10_10.py` | 7,438 | 2026-10-10 10:30:11 | `97076c37afa7` | 噪声面 |
| 55 | REPO | `.tmp/exp06_independent_json_gen_2026_10_10.py` | 21,560 | 2026-10-10 10:31:30 | `5ce8f89c9396` | 噪声面 |
| 56 | REPO | `results/_exp06_independent_check_2026_10_10.json` | 20,480 | 2026-10-10 10:31:42 | `4c36c376ab9c` | 成果面 |
| 57 | REPO | `results/_exp06_supplement_four_gaps_2026_10_10.md` | 26,519 | 2026-10-10 10:33:13 | `9f86cc5be8e9` | 成果面 |
| 58 | SUB | `results/_exp08_volume_reconciliation_2026_10_10.md` | 24,140 | 2026-10-10 10:33:56 | `895eb3f2943c` | 成果面 |
| 59 | SUB | `results/_kd_legacy_rewrite_ruling_2026_10_10.md` | 13,731 | 2026-10-10 10:40:29 | `2cadab5ed4f7` | 成果面 |
| 60 | SUB | `results/_kd_legacy_rewrite_register_2026_10_10.md` | 14,537 | 2026-10-10 10:41:53 | `9a7936882a5d` | 成果面 |
| 61 | SUB | `results/_exp05_missing_true_disposition_judgment_2026_10_10.md` | 25,552 | 2026-10-10 10:46:49 | `e8e1e63a11db` | 成果面 |
| 62 | SUB | `results/_s4_tree_prereg_revision_2026_10_10.md` | 30,382 | 2026-10-10 10:48:57 | `037140972829` | 成果面 |
| 63 | REPO | `.tmp/_exp06_fixcopy_verify_probe_2026_10_10.py` | 3,598 | 2026-10-10 10:49:23 | `680b6893f9f7` | 噪声面 |
| 64 | REPO | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_selfverify_fix_2026_10_10.py` | 31,457 | 2026-10-10 10:50:15 | `041525fd05a2` | 成果面 |
| 65 | SUB | `results/_t1_temp_axis_retirement_consolidation_2026_10_10.md` | 20,308 | 2026-10-10 10:51:31 | `40cb2e81425a` | 成果面 |
| 66 | REPO | `results/_exp06_selfverified_runner_fix_note_2026_10_10.md` | 17,052 | 2026-10-10 10:51:43 | `247398b687e6` | 成果面 |
| 67 | REPO | `results/_questionnaire_cards_intake_register_supplement_4_2026_10_10.md` | 116,506 | 2026-10-10 10:54:25 | `d6ff041a9df9` | 成果面 |
| 68 | REPO | `.tmp/_vk_q.py` | 519 | 2026-10-10 10:57:23 | `67364902116c` | 噪声面 |
| 69 | REPO | `.tmp/_vk_q2.py` | 540 | 2026-10-10 10:57:35 | `d5759d40dc43` | 噪声面 |
| 70 | REPO | `.tmp/_vk_q3.py` | 612 | 2026-10-10 10:57:46 | `a00cd309205f` | 噪声面 |
| 71 | REPO | `.tmp/_vk_q4.py` | 784 | 2026-10-10 10:58:01 | `defc3c53b7df` | 噪声面 |
| 72 | REPO | `.tmp/_vk_q5.py` | 1,246 | 2026-10-10 10:58:17 | `7b95307225ba` | 噪声面 |
| 73 | REPO | `.tmp/_vk_q6.py` | 811 | 2026-10-10 10:59:49 | `7da34dd24eb0` | 噪声面 |
| 74 | SUB | `results/_round27_34_approvals_effect_register_2026_10_10.md` | 73,226 | 2026-10-10 11:02:09 | `d0bc0b1a9ae0` | 成果面 |
| 75 | SUB | `results/_kd_19_ambiguous_tags_rejudge_rewrite_register_2026_10_10.md` | 29,664 | 2026-10-10 11:06:34 | `b508e5335377` | 成果面 |
| 76 | SUB | `results/_s4_feature_surface_v3_1_definition_2026_10_10.md` | 30,310 | 2026-10-10 11:10:18 | `d044ce1c069d` | 成果面 |
| 77 | REPO | `.tmp/_exp06_1009fix_verify_2026_10_10.py` | 7,817 | 2026-10-10 11:17:16 | `47fdf9673acc` | 噪声面 |
| 78 | REPO | `results/_t_s3_3_disposition_judgment_2026_10_10.md` | 31,855 | 2026-10-10 11:18:26 | `ee7a822a077b` | 成果面 |
| 79 | REPO | `.tmp/_exp06_1009fix_lnref_2026_10_10.py` | 1,508 | 2026-10-10 11:20:15 | `9c7096147878` | 噪声面 |
| 80 | REPO | `.tmp/_exp06_1009fix_lnref2_2026_10_10.py` | 1,505 | 2026-10-10 11:20:46 | `3ff21d556306` | 噪声面 |
| 81 | REPO | `.tmp/_exp06_1009fix_build_2026_10_10.py` | 29,412 | 2026-10-10 11:22:20 | `e5acb3c0bca2` | 噪声面 |
| 82 | REPO | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_fix_2026_10_10.py` | 33,994 | 2026-10-10 11:23:01 | `341b6726ac4e` | 成果面 |
| 83 | REPO | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_rename_2026_10_10.py` | 35,321 | 2026-10-10 11:23:01 | `cd43c41716f0` | 成果面 |
| 84 | REPO | `results/_exp06_selfverified_renaming_note_2026_10_10.md` | 34,554 | 2026-10-10 11:25:56 | `8b4ec41a37dd` | 成果面 |
| 85 | REPO | `results/_kd04_c_denominator_killline_prereg_2026_10_10.md` | 24,527 | 2026-10-10 11:27:33 | `8f2025e9de6f` | 成果面 |
| 86 | SUB | `results/_e5_nonbinary_count_judgment_2026_10_10.md` | 37,762 | 2026-10-10 11:36:54 | `2ef8797c03f4` | 成果面 |
| 87 | REPO | `results/_kd_unambiguous_meaning_ruling_2026_10_10.md` | 24,898 | 2026-10-10 11:36:58 | `f22ede7226d2` | 成果面 |
| 88 | REPO | `results/_d1_backfill_intake_verdict_2026_10_01.md` | 42,115 | 2026-10-10 11:37:23 | `a7e8f90d9db7` | 成果面 |
| 89 | REPO | `results/_s3_th_v21_reconciliation_verdict_2026_10_01.md` | 51,073 | 2026-10-10 11:37:23 | `84fa6996b656` | 成果面 |
| 90 | SUB | `results/_d1_ruling_and_s3_transition_2026_10_01.md` | 28,370 | 2026-10-10 11:37:23 | `dc9cb0e02922` | 成果面 |
| 91 | SUB | `results/_mini_round_5_decisions_register_2026_10_01.md` | 53,125 | 2026-10-10 11:37:23 | `d5fffe6a5e79` | 成果面 |
| 92 | SUB | `results/_s3_kv3s_3_verdict_2026_10_01.md` | 35,037 | 2026-10-10 11:37:23 | `e394bb6b5ddf` | 成果面 |
| 93 | SUB | `results/_t1_7_2_correction_2026_10_08.md` | 16,469 | 2026-10-10 11:37:23 | `d90bf82338f6` | 成果面 |
| 94 | SUB | `results/_limb_reading_verdict_kv3s33_2026_10_01.md` | 56,329 | 2026-10-10 11:37:24 | `c5866ce87d9c` | 成果面 |
| 95 | SUB | `results/_n7_mutual_exclusion_determination_2026_10_01.md` | 40,169 | 2026-10-10 11:37:24 | `b6bdf807cb27` | 成果面 |
| 96 | SUB | `results/_r3_r4_interpretation_case_2026_10_01.md` | 64,849 | 2026-10-10 11:37:24 | `46469217883b` | 成果面 |
| 97 | SUB | `results/_s3_missing_field_backfill_rule_draft_2026_10_01.md` | 35,827 | 2026-10-10 11:37:24 | `8496a53d183a` | 成果面 |
| 98 | SUB | `results/_s3_missing_field_backfill_rule_effective_2026_10_01.md` | 52,469 | 2026-10-10 11:37:24 | `1450057b0819` | 成果面 |
| 99 | SUB | `results/_t1_gate_closure_and_recompute_verdict_2026_10_01.md` | 72,934 | 2026-10-10 11:37:24 | `4bdd82c796b8` | 成果面 |
| 100 | SUB | `results/_u11_execution_register_2026_10_09.md` | 24,549 | 2026-10-10 11:37:24 | `8bc087a16f5a` | 成果面 |
| 101 | SUB | `results/_kd_uncognizable_meaning_rewrite_register_2026_10_10.md` | 19,525 | 2026-10-10 11:38:50 | `b07887551f7c` | 成果面 |
| 102 | SUB | `results/_kd04_c_denominator_expansion_exec_2026_10_10.md` | 27,915 | 2026-10-10 11:41:56 | `2caa3966b866` | 成果面 |
| 103 | REPO | `.tmp/_kd04_c_den_exec_2026_10_10.py` | 21,430 | 2026-10-10 11:42:44 | `419f9f691e63` | 噪声面 |
| 104 | REPO | `results/_kd04_c_denominator_expansion_readings_2026_10_10.json` | 23,314 | 2026-10-10 11:44:09 | `249009e6a0cc` | 成果面 |
| 105 | SUB | `results/_e6_j5_backfill_resolution_2026_10_10.md` | 23,171 | 2026-10-10 11:45:26 | `c888158b3263` | 成果面 |
| 106 | REPO | `.tmp/d05_hash_index.py` | 1,004 | 2026-10-10 11:51:23 | `070b6f865eba` | 噪声面 |
| 107 | SUB | `results/_kd_rewrite_fingerprint_sync_2026_10_10.md` | 20,862 | 2026-10-10 11:53:38 | `aeefc94a94b5` | 成果面 |
| 108 | REPO | `.tmp/_d05_probe_keys.py` | 1,967 | 2026-10-10 11:54:20 | `4bc4f8c89e44` | 噪声面 |
| 109 | REPO | `.tmp/_d05_probe_inter.py` | 3,008 | 2026-10-10 11:55:01 | `23ee92345bf1` | 噪声面 |
| 110 | REPO | `.tmp/_d05_instrument_audit.py` | 5,948 | 2026-10-10 11:58:15 | `edfa99486954` | 噪声面 |
| 111 | REPO | `.tmp/_d05_probe_ho.py` | 1,612 | 2026-10-10 11:59:12 | `3509e3f21790` | 噪声面 |
| 112 | REPO | `.tmp/_d05_probe_align.py` | 1,429 | 2026-10-10 11:59:34 | `78c079bef471` | 噪声面 |
| 113 | REPO | `.tmp/_d05_probe_tree.py` | 4,616 | 2026-10-10 11:59:58 | `d445274fcfa4` | 噪声面 |
| 114 | SUB | `results/_tmp_disposal_register_2026_10_10.md` | 20,812 | 2026-10-10 12:00:12 | `e0f6b744e826` | 成果面 |
| 115 | REPO | `.tmp/_d05_probe_labels.py` | 3,816 | 2026-10-10 12:00:18 | `53784ec36e27` | 噪声面 |
| 116 | REPO | `results/_s4_regen_execution_plan_2026_10_10.md` | 33,444 | 2026-10-10 12:00:40 | `70e22220350d` | 成果面 |
| 117 | SUB | `results/_wordlist_house_effectivity_note_2026_10_10.md` | 14,606 | 2026-10-10 12:01:03 | `4e89a5bb4b68` | 成果面 |
| 118 | REPO | `.tmp/_d05_probe_seq.py` | 4,925 | 2026-10-10 12:02:02 | `88c3533d7fcb` | 噪声面 |
| 119 | REPO | `.tmp/_d05_probe_dist.py` | 4,079 | 2026-10-10 12:02:24 | `4866ba720010` | 噪声面 |
| 120 | REPO | `.tmp/_d05_probe_phrase.py` | 4,844 | 2026-10-10 12:02:44 | `e519b5d5f51e` | 噪声面 |
| 121 | REPO | `.tmp/_d05_probe_arm1.py` | 4,983 | 2026-10-10 12:04:00 | `ccb6b4aef623` | 噪声面 |
| 122 | REPO | `.tmp/_d05_probe_order.py` | 4,981 | 2026-10-10 12:04:21 | `788fdf5f3142` | 噪声面 |
| 123 | REPO | `.tmp/_d05_probe_metrics.py` | 908 | 2026-10-10 12:04:33 | `5a670ae27a5b` | 噪声面 |
| 124 | REPO | `.tmp/_d05_probe_thresh.py` | 4,565 | 2026-10-10 12:04:50 | `a91f28bfd48b` | 噪声面 |
| 125 | REPO | `.tmp/_d05_probe_train.py` | 4,770 | 2026-10-10 12:05:07 | `4435748f010d` | 噪声面 |
| 126 | REPO | `.tmp/_d05_probe_den.py` | 4,587 | 2026-10-10 12:05:24 | `7b8207d9bbba` | 噪声面 |
| 127 | REPO | `.tmp/_d05_probe_leak.py` | 4,105 | 2026-10-10 12:07:07 | `edb264ccfc51` | 噪声面 |
| 128 | REPO | `.tmp/_d05_probe_j1.py` | 4,651 | 2026-10-10 12:07:27 | `b3fba6ae6152` | 噪声面 |
| 129 | REPO | `.tmp/_d05_b_coincidence_checks_2026_10_10.py` | 22,078 | 2026-10-10 12:08:37 | `c1fc428d450c` | 噪声面 |
| 130 | REPO | `results/_d05_b_coincidence_checks_exec_readings_2026_10_10.json` | 13,960 | 2026-10-10 12:08:44 | `586c435d1f15` | 成果面 |
| 131 | REPO | `results/_d05_b_coincidence_checks_exec_2026_10_10.md` | 21,061 | 2026-10-10 12:10:50 | `840fbf08caf4` | 成果面 |
| 132 | REPO | `.tmp/scan_five_terminal_2026_10_10.py` | 4,319 | 2026-10-10 12:21:36 | `7200487fdab1` | 噪声面 |
| 133 | REPO | `.tmp/scan_domain_five_terminal_2026_10_10.py` | 2,243 | 2026-10-10 12:21:53 | `732489dc3dbd` | 噪声面 |
| 134 | REPO | `.tmp/scan_supplement_five_terminal_2026_10_10.py` | 6,010 | 2026-10-10 12:22:25 | `7c0a6d022104` | 噪声面 |
| 135 | REPO | `.tmp/_abc_readings_reprocheck_2026_10_10.py` | 9,491 | 2026-10-10 12:23:04 | `0ec2a2bf3bab` | 噪声面 |
| 136 | REPO | `.tmp/_abc_readings_reprocheck_out_2026_10_10.json` | 78,436 | 2026-10-10 12:23:11 | `2f9aa16b63ca` | 噪声面 |
| 137 | REPO | `.tmp/scan_classify_five_terminal_2026_10_10.py` | 7,603 | 2026-10-10 12:23:20 | `0b9b59083534` | 噪声面 |
| 138 | REPO | `.tmp/_abc_diff_2026_10_10.py` | 6,620 | 2026-10-10 12:23:35 | `6d6733f0e5c2` | 噪声面 |
| 139 | REPO | `.tmp/_abc_h1h2_2026_10_10.py` | 7,889 | 2026-10-10 12:25:31 | `16f19bad301f` | 噪声面 |
| 140 | REPO | `.tmp/_abc_rfd_2026_10_10.py` | 5,938 | 2026-10-10 12:26:11 | `39268ca6adff` | 噪声面 |
| 141 | REPO | `.tmp/_abc_final_2026_10_10.py` | 7,329 | 2026-10-10 12:26:39 | `15b4de4fdff6` | 噪声面 |
| 142 | SUB | `results/_s4_abcreadings_reproducibility_check_2026_10_10.md` | 25,234 | 2026-10-10 12:27:42 | `892e5dfe3ed1` | 成果面 |
| 143 | REPO | `results/_five_terminal_judgments_ruling_2026_10_10.md` | 27,315 | 2026-10-10 12:28:00 | `9e96d0a1ba12` | 成果面 |
| 144 | REPO | `.tmp/_d05_three_checks_recheck_2026_10_10.py` | 11,134 | 2026-10-10 12:41:16 | `fc1201cb71e7` | 噪声面 |
| 145 | REPO | `.tmp/_d05_three_checks_recheck_out_2026_10_10.json` | 3,622 | 2026-10-10 12:41:33 | `4eb425260682` | 噪声面 |
| 146 | REPO | `.tmp/_d05_caliber_2026_10_10.py` | 8,011 | 2026-10-10 12:42:22 | `65cb84529cb2` | 噪声面 |
| 147 | REPO | `.tmp/_d05_s4only_2026_10_10.py` | 3,438 | 2026-10-10 12:42:55 | `802069e2c06e` | 噪声面 |
| 148 | SUB | `results/_d05_three_checks_readings_recheck_confirm_2026_10_10.md` | 20,044 | 2026-10-10 12:43:54 | `dcf9f5cfa2db` | 成果面 |
| 149 | SUB | `results/_e6_case_a_judgment_face_promotion_2026_10_10.md` | 42,116 | 2026-10-10 12:53:23 | `4e65c53f68e8` | 成果面 |
| 150 | REPO | `results/_s4_v31_keyword_table_final_2026_10_10.md` | 23,270 | 2026-10-10 13:03:25 | `1b7bcbcce589` | 成果面 |
| 151 | SUB | `results/_kd04_c_denominator_verdict_keeper_alternative_judgment_2026_10_10.md` | 25,123 | 2026-10-10 13:03:50 | `19ad36f7ec84` | 成果面 |
| 152 | REPO | `results/_s4_kex_killline_freeze_2026_10_10.md` | 15,284 | 2026-10-10 13:03:55 | `6269d0c6fd10` | 成果面 |
| 153 | REPO | `results/_s4_execution_sequence_review_2026_10_10.md` | 19,158 | 2026-10-10 13:04:40 | `0e1eb2fdd25e` | 成果面 |
| 154 | REPO | `results/_s4_vclause_1_6_revision_2026_10_10.md` | 14,900 | 2026-10-10 13:05:11 | `017b3cf38ae3` | 成果面 |
| 155 | SUB | `results/_e6_j5_semantics_conflict_judgment_2026_10_10.md` | 27,682 | 2026-10-10 13:13:46 | `3c7628a4964d` | 成果面 |
| 156 | REPO | `letters/_commission_c4_values_EN_2026_10_10.md` | 56,217 | 2026-10-10 13:14:46 | `a397621085d6` | 成果面 |
| 157 | REPO | `letters/_commission_c4_values_EN_differences_exits_note_2026_10_10.md` | 7,817 | 2026-10-10 13:15:32 | `b20f25a66267` | 成果面 |
| 158 | SUB | `results/_b_coincidence_disposition_judgment_2026_10_10.md` | 42,838 | 2026-10-10 13:17:14 | `7ff80485955c` | 成果面 |
| 159 | SUB | `results/_s4q04_level_attribution_judgment_2026_10_10.md` | 26,407 | 2026-10-10 13:20:41 | `49a07216a1bb` | 成果面 |
| 160 | SUB | `results/_kd04_c_denominator_closeout_register_2026_10_10.md` | 23,029 | 2026-10-10 13:21:16 | `78481cc60494` | 成果面 |
| 161 | SUB | `results/_af_entity_definition_draft_2026_10_10.md` | 25,257 | 2026-10-10 13:24:57 | `97654060d86e` | 成果面 |
| 162 | SUB | `results/_give_up_semantics_draft_2026_10_10.md` | 23,497 | 2026-10-10 13:26:05 | `b6a4ae82e038` | 成果面 |
| 163 | SUB | `results/_b_coincidence_closeout_register_2026_10_10.md` | 31,451 | 2026-10-10 13:32:32 | `51ce7b49c423` | 成果面 |
| 164 | REPO | `results/_s4_regen_golive_clearance_2026_10_10.md` | 27,436 | 2026-10-10 13:33:31 | `80d8905b9762` | 成果面 |
| 165 | SUB | `results/_e6_j5_semantics_erratum_note_2026_10_10.md` | 21,166 | 2026-10-10 13:34:44 | `b2db427147e2` | 成果面 |
| 166 | SUB | `results/_e6_verdict_v3_rationale_review_2026_10_10.md` | 39,008 | 2026-10-10 13:36:11 | `664e82968fc2` | 成果面 |
| 167 | REPO | `.tmp/s4_regen_runner.py` | 13,040 | 2026-10-10 13:43:59 | `70467364bdb1` | 噪声面 |
| 168 | REPO | `.tmp/run_steps.py` | 2,756 | 2026-10-10 13:45:15 | `019f8405d4cf` | 噪声面 |
| 169 | REPO | `.tmp/diffcause.py` | 2,724 | 2026-10-10 13:47:39 | `2b24513cdf74` | 噪声面 |
| 170 | REPO | `.tmp/scope_scan.py` | 3,380 | 2026-10-10 13:48:55 | `07349acfe90f` | 噪声面 |
| 171 | REPO | `.tmp/pool_search.py` | 2,127 | 2026-10-10 13:49:20 | `3245af3f3bbb` | 噪声面 |
| 172 | REPO | `letters/_codex_c4_values_reply_2026_10_10.md` | 13,378 | 2026-10-10 13:49:24 | `8e4972352291` | 成果面 |
| 173 | SUB | `results/_u2u3_effectivity_register_2026_10_10.md` | 27,192 | 2026-10-10 13:49:44 | `b00b87cec825` | 成果面 |
| 174 | REPO | `.tmp/singlevar.py` | 1,515 | 2026-10-10 13:50:16 | `f0bba43af3e5` | 噪声面 |
| 175 | REPO | `.tmp/prep.py` | 4,091 | 2026-10-10 13:51:46 | `e401c8e50f93` | 噪声面 |
| 176 | REPO | `.tmp/tables.py` | 1,818 | 2026-10-10 13:52:29 | `02cc157b6d69` | 噪声面 |
| 177 | REPO | `results/_s4_v31_regen_gold_register_2026_10_10.md` | 27,133 | 2026-10-10 13:54:32 | `9c9d8e8ecc72` | 成果面 |
| 178 | REPO | `.tmp/write_items_json.py` | 4,388 | 2026-10-10 13:54:45 | `9dce7986e20d` | 噪声面 |
| 179 | REPO | `results/_s4_v31_regen_gold_items_2026_10_10.json` | 36,830 | 2026-10-10 13:54:57 | `4125cb2df92b` | 成果面 |
| 180 | REPO | `results/_s4_v31_readings_execution_2026_10_10.md` | 21,467 | 2026-10-10 13:55:46 | `80d765f34163` | 成果面 |
| 181 | REPO | `.tmp/write_summary_json.py` | 9,049 | 2026-10-10 13:56:04 | `6214ad3cdc2d` | 噪声面 |
| 182 | REPO | `results/_s4_v31_displacement_items_2026_10_10.json` | 36,822 | 2026-10-10 13:56:13 | `6f020c03e52c` | 成果面 |
| 183 | REPO | `results/_s4_v31_readings_summary_2026_10_10.json` | 5,569 | 2026-10-10 13:56:13 | `882a1b3deb0b` | 成果面 |
| 184 | REPO | `results/_s4_v31_drift_register_face1_2026_10_10.md` | 11,485 | 2026-10-10 13:56:41 | `5ab168d82873` | 成果面 |
| 185 | SUB | `results/_kd_login_register_section65_correction_2026_10_10.md` | 20,422 | 2026-10-10 13:56:56 | `316d14c137bb` | 成果面 |
| 186 | SUB | `results/_s4_v31_displacement_register_face2_2026_10_10.md` | 17,736 | 2026-10-10 13:57:19 | `b6ce4a79116e` | 成果面 |
| 187 | REPO | `results/_questionnaire_cards_intake_register_supplement_5_2026_10_10.md` | 77,189 | 2026-10-10 13:59:18 | `edb57308170d` | 成果面 |
| 188 | SUB | `results/_g5_displacement_threshold_draft_2026_10_10.md` | 25,619 | 2026-10-10 14:02:11 | `7c8107d9a8fb` | 成果面 |
| 189 | SUB | `results/_codex_c4_values_reply_intake_register_2026_10_10.md` | 12,926 | 2026-10-10 14:09:06 | `8f1d27a02833` | 成果面 |
| 190 | SUB | `results/_round45_dispositions_effect_register_2026_10_10.md` | 19,803 | 2026-10-10 14:11:43 | `d66a1076952a` | 成果面 |
| 191 | SUB | `results/_s4_w1_3636_consistency_check_2026_10_10.md` | 29,196 | 2026-10-10 14:15:28 | `0e9ae4b6ee8c` | 成果面 |
| 192 | REPO | `letters/_commission_c4_values_followup_EN_2026_10_10.md` | 7,583 | 2026-10-10 14:31:49 | `abe0652ab00f` | 成果面 |
| 193 | SUB | `results/_s4_w2_e4_separate_judgment_2026_10_10.md` | 37,607 | 2026-10-10 14:36:06 | `a51bd6530075` | 成果面 |
| 194 | SUB | `results/_s4_v31_exec_section8_errata_2026_10_10.md` | 23,250 | 2026-10-10 14:42:11 | `ec11aec2380d` | 成果面 |
| 195 | SUB | `results/_g5_displacement_threshold_c_approval_effect_and_trigger_eval_2026_10_10.md` | 33,880 | 2026-10-10 14:44:04 | `3015f2481df1` | 成果面 |
| 196 | SUB | `results/_three_state_standard_repeal_register_2026_10_10.md` | 18,364 | 2026-10-10 14:44:36 | `8503708c73bf` | 成果面 |
| 197 | REPO | `.tmp/_e6_ndjt_recompute_2026_10_10.py` | 5,064 | 2026-10-10 14:58:57 | `59c2d618305f` | 噪声面 |
| 198 | SUB | `results/_s4_w2_disposition_registration_2026_10_10.md` | 23,545 | 2026-10-10 14:59:02 | `566c2f0ad7e8` | 成果面 |
| 199 | REPO | `.tmp/e4_axis2_v11_displacement_run_2026_10_10.py` | 10,617 | 2026-10-10 14:59:32 | `a950ae064fde` | 噪声面 |
| 200 | REPO | `.tmp/_e6_alt_permp_closure_runner_2026_10_10.py` | 9,985 | 2026-10-10 14:59:42 | `9bb254aa58a9` | 噪声面 |
| 201 | REPO | `.tmp/e4_axis2_denominator_recheck_2026_10_10.py` | 3,833 | 2026-10-10 15:00:04 | `5944efd3b68e` | 噪声面 |
| 202 | REPO | `.tmp/e4_axis2_crosscheck_2026_10_10.py` | 3,607 | 2026-10-10 15:00:27 | `fbf93a534b99` | 噪声面 |
| 203 | REPO | `.tmp/e4_axis2_final_validation_2026_10_10.py` | 6,489 | 2026-10-10 15:01:06 | `8d2211f8ac91` | 噪声面 |
| 204 | REPO | `.tmp/_e6_alt_permp_closure_analysis_2026_10_10.py` | 2,736 | 2026-10-10 15:02:17 | `affabef74de4` | 噪声面 |
| 205 | REPO | `.tmp/e4_axis2_hit_unchanged_probe_2026_10_10.py` | 2,629 | 2026-10-10 15:02:27 | `fc5d6bde78ad` | 噪声面 |
| 206 | SUB | `results/_e6_n_distinct_judge_types_recompute_2026_10_10.md` | 26,304 | 2026-10-10 15:02:56 | `82c5c143134e` | 成果面 |
| 207 | SUB | `results/_e6_alt_permp_comparability_closure_2026_10_10.md` | 16,636 | 2026-10-10 15:03:20 | `1c663430b4aa` | 成果面 |
| 208 | SUB | `results/_s4_v11_axis2_displacement_items_2026_10_10.json` | 9,941 | 2026-10-10 15:04:30 | `0eed9053619c` | 成果面 |
| 209 | SUB | `results/_s4_e4_axis_disposition_axis2_run_2026_10_10.md` | 29,700 | 2026-10-10 15:05:02 | `2bda07af86fc` | 成果面 |
| 210 | REPO | `.tmp/_intake_cards_35_48_extract.py` | 3,416 | 2026-10-10 15:07:41 | `74cca5bda270` | 噪声面 |
| 211 | REPO | `.tmp/_build_intake_supplement_6.py` | 13,094 | 2026-10-10 15:09:02 | `6336456853ae` | 噪声面 |
| 212 | REPO | `.tmp/_append_intake_supplement_6_tail.py` | 9,335 | 2026-10-10 15:09:46 | `c3339682d68c` | 噪声面 |
| 213 | REPO | `results/_questionnaire_cards_intake_register_supplement_6_2026_10_10.md` | 106,453 | 2026-10-10 15:09:57 | `95ba771fa760` | 成果面 |
| 214 | REPO | `.tmp/_verify_intake_supplement_6.py` | 3,678 | 2026-10-10 15:10:32 | `1fbb1bd1db6c` | 噪声面 |
| 215 | REPO | `.tmp/_crosscheck_messages_35_48.py` | 1,608 | 2026-10-10 15:10:47 | `dcfe48359488` | 噪声面 |
| 216 | REPO | `.tmp/_build_receipt_supplement_6.py` | 11,369 | 2026-10-10 15:11:50 | `bbc6b3e20b92` | 噪声面 |
| 217 | REPO | `results/_questionnaire_cards_intake_register_supplement_6_receipt_2026_10_10.md` | 11,752 | 2026-10-10 15:11:57 | `0984955b0370` | 成果面 |
| 218 | SUB | `results/_e6_th_v3_19_alignment_register_2026_10_10.md` | 32,582 | 2026-10-10 15:13:34 | `622cebef2c9f` | 成果面 |
| 219 | SUB | `results/_g5_seg3_tie_veto_judgment_2026_10_10.md` | 35,983 | 2026-10-10 15:17:28 | `3306d1fd020d` | 成果面 |
| 220 | SUB | `results/_n01_n08_revision_2026_10_10.md` | 26,628 | 2026-10-10 15:22:33 | `fa8400d8ae70` | 成果面 |
| 221 | SUB | `results/_u5_fingerprint_relocation_erratum_2026_10_10.md` | 24,999 | 2026-10-10 15:25:33 | `200c7e4c57cb` | 成果面 |
| 222 | SUB | `results/_give_up_n10_erratum_2026_10_10.md` | 22,021 | 2026-10-10 15:25:42 | `e0db6b819138` | 成果面 |
| 223 | SUB | `results/_s4_w2bc_effect_registration_2026_10_10.md` | 26,418 | 2026-10-10 15:36:26 | `b24a8411a260` | 成果面 |
| 224 | SUB | `results/_s4_e4b_ad5_type_separate_judgment_2026_10_10.md` | 51,898 | 2026-10-10 15:44:56 | `f48601fee958` | 成果面 |
| 225 | REPO | `letters/_codex_c4_values_followup_reply_2026_10_10.md` | 4,490 | 2026-10-10 16:02:26 | `97a35f8ae94c` | 成果面 |
| 226 | SUB | `results/_g5_rejudgment_face_prereg_2026_10_10.md` | 35,097 | 2026-10-10 16:04:10 | `04495ef4b343` | 成果面 |
| 227 | SUB | `results/_round51_effectivity_register_2026_10_10.md` | 27,070 | 2026-10-10 16:04:24 | `b8b0c52296b2` | 成果面 |
| 228 | SUB | `results/_u5b_citation_surface_revision_2026_10_10.md` | 50,079 | 2026-10-10 16:06:18 | `5cc29c53a422` | 成果面 |
| 229 | SUB | `results/_round52_s4_e4b_ad5_type_effectivity_register_2026_10_10.md` | 45,351 | 2026-10-10 16:31:38 | `debd88fc150c` | 成果面 |
| 230 | SUB | `results/_round52_e6b_caliber_naming_effectivity_register_2026_10_10.md` | 21,788 | 2026-10-10 16:34:00 | `e861c7bc19ad` | 成果面 |
| 231 | SUB | `results/_questionnaire_cards_intake_register_supplement_7_2026_10_10.md` | 52,602 | 2026-10-10 16:42:53 | `1fb8eac82781` | 成果面 |
| 232 | SUB | `results/_codex_c4_values_followup_reply_intake_register_2026_10_10.md` | 24,240 | 2026-10-10 17:05:56 | `c46d073589cf` | 成果面 |
| 233 | SUB | `results/_g5_rejudgment_c_applicability_recheck_2026_10_10.md` | 49,051 | 2026-10-10 17:09:46 | `15301b3025fa` | 成果面 |
| 234 | SUB | `results/_round53_rejudge_prereg_freeze_effectivity_register_2026_10_10.md` | 25,637 | 2026-10-10 17:10:04 | `b27814792394` | 成果面 |
| 235 | SUB | `results/_round53_th_v3_19_landfall_schema_effectivity_register_2026_10_10.md` | 20,023 | 2026-10-10 17:11:26 | `4c3a6dc0070d` | 成果面 |
| 236 | SUB | `results/_g5_rejudgment_trigger_caliber_judgment_2026_10_10.md` | 48,727 | 2026-10-10 17:12:00 | `16c31894d445` | 成果面 |
| 237 | SUB | `results/_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md` | 17,517 | 2026-10-10 17:12:50 | `a651f76a6547` | 成果面 |
| 238 | REPO | `letters/_commission_c4_values_unblock_EN_2026_10_10.md` | 10,244 | 2026-10-10 17:17:35 | `fde64a863b09` | 成果面 |
| 239 | REPO | `letters/_commission_c4_values_unblock_EN_differences_exits_note_2026_10_10.md` | 3,139 | 2026-10-10 17:17:46 | `1c769e28f8f5` | 成果面 |
| 240 | REPO | `letters/verify_c4_originated_math.py` | 4,115 | 2026-10-10 17:30:17 | `3042cf59448e` | 成果面 |
| 241 | REPO | `letters/_codex_c4_values_unblock_reply_2026_10_10.md` | 21,486 | 2026-10-10 17:35:08 | `a975c7990cd8` | 成果面 |
| 242 | SUB | `results/_round54_g5_dispositions_register_2026_10_10.md` | 39,977 | 2026-10-10 17:42:45 | `afc67818bb85` | 成果面 |
| 243 | SUB | `results/_g5_rejudgment_construction_question_judgment_2026_10_10.md` | 59,309 | 2026-10-10 17:47:40 | `ee660515d9e3` | 成果面 |
| 244 | SUB | `results/_s4_corpus_scope_hard_constraint_judgment_2026_10_10.md` | 44,199 | 2026-10-10 17:50:47 | `c7609657dfe4` | 成果面 |
| 245 | SUB | `results/_questionnaire_cards_intake_register_supplement_8_2026_10_10.md` | 50,790 | 2026-10-10 17:51:27 | `29b30d845841` | 成果面 |
| 246 | REPO | `results/_s4_source_wave_mapping_registration_2026_10_10.md` | 38,231 | 2026-10-10 17:56:29 | `26c8278e3552` | 成果面 |
| 247 | SUB | `results/_e6_th_v3_19_residual_exits_judgment_2026_10_10.md` | 46,261 | 2026-10-10 17:59:21 | `442d5ff4acdb` | 成果面 |
| 248 | SUB | `results/_codex_c4_values_unblock_reply_intake_register_2026_10_10.md` | 27,100 | 2026-10-10 18:06:56 | `a2d7f86d72e5` | 成果面 |
| 249 | SUB | `results/_round56_sc4_nstar_inconsistency_erratum_2026_10_10.md` | 16,640 | 2026-10-10 18:11:58 | `af4c3335538a` | 成果面 |
| 250 | SUB | `results/_round56_ad8fix_effectivity_register_2026_10_10.md` | 16,553 | 2026-10-10 18:12:36 | `2e7f86314428` | 成果面 |
| 251 | SUB | `results/_round55_dispositions_register_2026_10_10.md` | 34,913 | 2026-10-10 18:12:53 | `002fa0a9a5e4` | 成果面 |
| 252 | SUB | `results/_c4_unblock_reply_independent_review_2026_10_10.md` | 27,364 | 2026-10-10 18:13:09 | `2ecd866e2468` | 成果面 |
| 253 | SUB | `results/_codex_c4_unblock_reply_adoption_register_2026_10_10.md` | 22,895 | 2026-10-10 18:13:35 | `b979e78562a9` | 成果面 |
| 254 | SUB | `results/_round56_pending_questions_compilation_2026_10_10.md` | 33,504 | 2026-10-10 18:17:26 | `ef09b3d28a0f` | 成果面 |
| 255 | SUB | `results/_c4_math_corrections_downstream_erratum_2026_10_10.md` | 28,886 | 2026-10-10 18:18:42 | `643cb9e249f7` | 成果面 |
| 256 | REPO | `results/_g5_rejudgment_construction_change_plan_2026_10_10.md` | 57,004 | 2026-10-10 18:22:43 | `fa0001a6dd0a` | 成果面 |
| 257 | SUB | `results/_g5_x4_dual_axis_interpretation_judgment_2026_10_10.md` | 33,976 | 2026-10-10 18:29:03 | `c3117773ab36` | 成果面 |
| 258 | SUB | `results/_round56a_dispositions_register_2026_10_10.md` | 50,365 | 2026-10-10 18:33:00 | `d8980cfae7f7` | 成果面 |
| 259 | SUB | `results/_trj_w1_verification_2026_10_10.md` | 23,014 | 2026-10-10 18:33:08 | `cc6de8e981f6` | 成果面 |
| 260 | SUB | `results/_g5_krj9_denominator_reconciliation_judgment_2026_10_10.md` | 45,207 | 2026-10-10 18:34:36 | `22d90f12d605` | 成果面 |
| 261 | SUB | `results/_round56c_d23_ad5_judgment_2026_10_10.md` | 50,747 | 2026-10-10 18:36:42 | `061813859345` | 成果面 |
| 262 | SUB | `results/_round56_pending_questions_compilation_supplement_note_2026_10_10.md` | 29,019 | 2026-10-10 18:40:21 | `421c936f6ae8` | 成果面 |
| 263 | SUB | `results/_a02_excluded_items_idx_collection_2026_10_10.md` | 39,565 | 2026-10-10 18:40:34 | `03407e0b6662` | 成果面 |
| 264 | SUB | `results/_trj_w1_downstream_erratum_2026_10_10.md` | 24,888 | 2026-10-10 18:41:15 | `e52d0016fbc6` | 成果面 |
| 265 | SUB | `results/_u5b_p_counting_resolution_2026_10_10.md` | 20,086 | 2026-10-10 18:44:20 | `e12e9d9a32c4` | 成果面 |
| 266 | SUB | `results/_round56_terminal_boundary_effectivity_register_2026_10_10.md` | 35,878 | 2026-10-10 18:48:25 | `d5bf826278cb` | 成果面 |
| 267 | SUB | `results/_round56_n10_erratum_register_2026_10_10.md` | 20,321 | 2026-10-10 18:49:02 | `599d0450434e` | 成果面 |
| 268 | SUB | `results/_round56_th3_coverage_line_effectivity_register_2026_10_10.md` | 28,378 | 2026-10-10 18:49:59 | `6794fb09ce7e` | 成果面 |
| 269 | SUB | `results/_round56_th4_two_field_reporting_resolution_2026_10_10.md` | 28,233 | 2026-10-10 18:50:57 | `71894a686e92` | 成果面 |
| 270 | REPO | `results/_g5_ccp_execution_prereqs_2026_10_10.md` | 32,815 | 2026-10-10 18:52:37 | `ab1a07ae2fd1` | 成果面 |
| 271 | SUB | `results/_questionnaire_cards_intake_register_supplement_9_2026_10_10.md` | 84,422 | 2026-10-10 18:55:53 | `b6c0b4f29152` | 成果面 |
| 272 | SUB | `results/_round56r8_dispositions_register_2026_10_10.md` | 46,135 | 2026-10-10 18:57:58 | `cfb08d0e15f4` | 成果面 |
| 273 | SUB | `results/_round56c_card_id_erratum_2026_10_10.md` | 18,747 | 2026-10-10 19:05:04 | `f6c2d40f18ff` | 成果面 |
| 274 | SUB | `results/_g5_ccp_p0_verification_2026_10_10.md` | 24,819 | 2026-10-10 19:05:07 | `8c7693379496` | 成果面 |
| 275 | SUB | `results/_round56_direct_adoptions_register_2026_10_10.md` | 43,240 | 2026-10-10 19:06:22 | `e3c56c5d0a97` | 成果面 |
| 276 | SUB | `results/_round56_shortname_backfill_note_2026_10_10.md` | 22,195 | 2026-10-10 19:07:14 | `bb2444cccd65` | 成果面 |
| 277 | SUB | `results/_round56_typeb_implementation_register_2026_10_10.md` | 26,367 | 2026-10-10 19:08:08 | `c296a7833a70` | 成果面 |
| 278 | SUB | `results/_questionnaire_cards_intake_register_supplement_10_2026_10_10.md` | 84,127 | 2026-10-10 19:09:19 | `6c18d336e018` | 成果面 |
| 279 | SUB | `results/_round56_gu_backdoor_exclusion_revision_2026_10_10.md` | 25,045 | 2026-10-10 19:11:29 | `52d3b10a16a0` | 成果面 |
| 280 | SUB | `results/_round56_v4_kd_row_correction_revision_2026_10_10.md` | 23,453 | 2026-10-10 19:12:12 | `6d8537cb127f` | 成果面 |
| 281 | SUB | `results/_round56_g2_enable_and_v1_rule_register_2026_10_10.md` | 34,181 | 2026-10-10 19:13:12 | `936f551f0fd3` | 成果面 |
| 282 | REPO | `results/_g5_ccp_seed_designation_revision_2026_10_10.md` | 20,979 | 2026-10-10 19:15:26 | `b53f40abb90b` | 成果面 |
| 283 | SUB | `results/_round56_idx_sc1_resolution_2026_10_10.md` | 47,107 | 2026-10-10 19:27:46 | `9b41f2a38b2f` | 成果面 |
| 284 | REPO | `.tmp/_vk_q7.py` | 1,331 | 2026-10-10 19:37:27 | `a6c525f88f11` | 噪声面 |
| 285 | REPO | `.tmp/_vk_q8.py` | 1,025 | 2026-10-10 19:37:42 | `5a81e5558c72` | 噪声面 |
| 286 | SUB | `results/_phase1_completion_judgment_2026_10_10.md` | 28,836 | 2026-10-10 19:44:53 | `6049c68f027b` | 成果面 |
| 287 | SUB | `results/_round56_idx_sc1_temp_deletion_deviation_note_2026_10_10.md` | 8,181 | 2026-10-10 19:55:10 | `c72086990450` | 成果面 |
| 288 | SUB | `results/_krj9_scope_clarification_draft_2026_10_10.md` | 28,654 | 2026-10-10 19:55:36 | `b17b3c38ec21` | 成果面 |
| 289 | SUB | `results/_round56r9r10_dispositions_register_2026_10_10.md` | 49,754 | 2026-10-10 19:57:04 | `0eb408ae60f5` | 成果面 |
| 290 | SUB | `results/_b01_p_counting_recompute_2026_10_10.md` | 22,104 | 2026-10-10 20:00:44 | `3511cf21a869` | 成果面 |
| 291 | SUB | `results/_round56_direct_adoptions_register_2_2026_10_10.md` | 26,690 | 2026-10-10 20:15:55 | `f8e0fa28c067` | 成果面 |
| 292 | SUB | `results/_zero_consumption_cells_field_correction_2026_10_10.md` | 12,244 | 2026-10-10 20:17:54 | `36f9ac4ebbf6` | 成果面 |
| 293 | SUB | `results/_round56_typeb_form_draft_2026_10_10.md` | 50,170 | 2026-10-10 20:18:30 | `582c5fb9970c` | 成果面 |
| 294 | SUB | `results/_questionnaire_cards_intake_register_supplement_11_2026_10_10.md` | 55,341 | 2026-10-10 20:19:27 | `52c97d1c11e9` | 成果面 |
| 295 | SUB | `results/_round56_b01_followup_disposition_plan_2026_10_10.md` | 31,004 | 2026-10-10 20:29:17 | `857fb940a43c` | 成果面 |
| 296 | SUB | `results/_c4_reply_intake_acceptance_register_2026_10_01.md` | 33,728 | 2026-10-10 21:19:00 | `e1e8cb7b9db4` | 成果面 |
| 297 | SUB | `results/_c4_math_corrections_E1_E2_execution_erratum_2026_10_10.md` | 31,607 | 2026-10-10 21:20:30 | `4c369cb86db4` | 成果面 |
| 298 | REPO | `letters/查理_deposon双主线论文终稿_2026-10-01_v0.3.md` | 239,700 | 2026-10-10 21:21:41 | `8baa9854b3f7` | 成果面 |
| 299 | SUB | `results/_round56_typeb_backfill_register_2026_10_10.md` | 40,253 | 2026-10-10 21:24:40 | `607ded06d840` | 成果面 |
| 300 | SUB | `results/_zero_reading_judgment_2026_10_10.md` | 27,824 | 2026-10-10 21:28:00 | `a9947f5677df` | 成果面 |
| 301 | SUB | `results/_p_refresh_s0_judgment_2026_10_10.md` | 41,449 | 2026-10-10 21:28:04 | `369173063a7c` | 成果面 |
| 302 | SUB | `results/_b01_new_key_classification_2026_10_10.md` | 38,669 | 2026-10-10 21:31:57 | `2ddfecf6201c` | 成果面 |
| 303 | SUB | `results/_b01_recompute_sec4_2_erratum_2026_10_10.md` | 16,441 | 2026-10-10 21:33:26 | `fac3308fb295` | 成果面 |
| 304 | SUB | `results/_vk_current_counting_face_2026_10_10.md` | 24,795 | 2026-10-10 21:35:11 | `4d4e41c3eff5` | 成果面 |
| 305 | SUB | `results/_round56_review_effectivity_register_2026_10_10.md` | 49,013 | 2026-10-10 21:36:54 | `da6b55162e50` | 成果面 |
| 306 | SUB | `results/_round56_registration_supplement_2026_10_10.md` | 21,865 | 2026-10-10 21:37:33 | `71a59735302c` | 成果面 |
| 307 | SUB | `results/_p_refresh_registration_preliminary_2026_10_10.md` | 32,780 | 2026-10-10 21:56:34 | `a3e14b508a4a` | 成果面 |
| 308 | SUB | `results/_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` | 18,923 | 2026-10-10 21:59:20 | `1bf6f47a590d` | 成果面 |
| 309 | REPO | `results/_s4_heldout_sampling_seedprime_items_register_2026_10_10.md` | 24,690 | 2026-10-10 23:07:07 | `9da183328f18` | 成果面 |
| 310 | REPO | `results/_s4_heldout_sampling_seedprime_items_2026_10_10.json` | 15,409 | 2026-10-10 23:07:39 | `6cbb8ba01bfb` | 成果面 |
| 311 | SUB | `results/_p_refresh_scope_judgment_2026_10_10.md` | 34,004 | 2026-10-10 23:12:55 | `44e98dc31e2b` | 成果面 |
| 312 | SUB | `results/_b01_new_key_residue_judgment_2026_10_10.md` | 41,984 | 2026-10-10 23:13:30 | `345517455dcf` | 成果面 |
| 313 | SUB | `results/_typeb_m_definition_judgment_2026_10_10.md` | 41,432 | 2026-10-10 23:15:39 | `97ac7fcc4803` | 成果面 |
| 314 | REPO | `results/_s4_seedprime_inheldout_recompute_2026_10_10.md` | 21,866 | 2026-10-10 23:20:20 | `cf3368e7d5a0` | 成果面 |
| 315 | SUB | `results/_s4_heldout_seedprime_verification_2026_10_10.md` | 21,966 | 2026-10-10 23:21:06 | `8c64314d0ec0` | 成果面 |
| 316 | SUB | `results/_u_cf_category_caliber_2026_10_10.md` | 18,976 | 2026-10-10 23:29:45 | `73f181d76169` | 成果面 |
| 317 | SUB | `results/_typeb_m_caliber_2026_10_10.md` | 32,830 | 2026-10-10 23:30:45 | `4d067a884c6c` | 成果面 |
| 318 | SUB | `results/_u_cf_reclassification_2026_10_10.md` | 25,698 | 2026-10-10 23:30:49 | `02f910e8795b` | 成果面 |
| 319 | SUB | `results/_typeb_m_registration_2026_10_10.md` | 27,778 | 2026-10-10 23:32:32 | `3b68d3890473` | 成果面 |
| 320 | REPO | `results/_chd_construction_domain_declaration_draft_2026_10_10.md` | 34,948 | 2026-10-10 23:35:41 | `17cf0d59cd7b` | 成果面 |
| 321 | SUB | `results/_round56_review_effectivity_register_3_2026_10_10.md` | 77,181 | 2026-10-10 23:50:47 | `84ed13256250` | 成果面 |
| 322 | SUB | `results/_s1prime_trigger_caliber_reevaluation_2026_10_10.md` | 29,991 | 2026-10-10 23:51:48 | `d2326973aaf8` | 成果面 |
| 323 | SUB | `results/_questionnaire_cards_intake_register_supplement_12_2026_10_10.md` | 121,137 | 2026-10-10 23:55:57 | `1ff6919967a7` | 成果面 |

#### 2026-10-11（114 件）

| # | 区 | 相对路径 | bytes | mtime | SHA-12 | 类别 |
|---:|:--|:--|--:|:--|:--|:--|
| 1 | SUB | `results/_s2prime_krj3_applicability_recheck_2026_10_10.md` | 41,322 | 2026-10-11 00:02:57 | `10518510b628` | 成果面 |
| 2 | SUB | `results/_b14_vk_evidence_audit_2026_10_10.md` | 33,586 | 2026-10-11 00:07:21 | `89f17297f1f5` | 成果面 |
| 3 | SUB | `results/_trigger_denominator_caliber_judgment_2026_10_11.md` | 43,448 | 2026-10-11 00:12:10 | `16bf9332deef` | 成果面 |
| 4 | SUB | `results/_b01_recompute_authorization_supplement_2026_10_11.md` | 18,454 | 2026-10-11 00:14:37 | `03a66d4c663a` | 成果面 |
| 5 | SUB | `results/_vk_face_category_erratum_2026_10_11.md` | 17,373 | 2026-10-11 00:15:40 | `67bf70301889` | 成果面 |
| 6 | SUB | `results/_c_component4_d2d3_gap_judgment_2026_10_11.md` | 27,490 | 2026-10-11 00:15:45 | `08d3bfd82235` | 成果面 |
| 7 | REPO | `results/_s3prime_degeneracy_selfcert_2026_10_11.md` | 39,939 | 2026-10-11 00:15:56 | `e4d96a516289` | 成果面 |
| 8 | SUB | `results/_round56_review_effectivity_register_4_2026_10_11.md` | 46,908 | 2026-10-11 00:23:15 | `ee31bb8a94fe` | 成果面 |
| 9 | SUB | `results/_c_component4_three_items_judgment_2026_10_11.md` | 41,580 | 2026-10-11 00:26:46 | `fd0094e2f865` | 成果面 |
| 10 | REPO | `results/_s3prime_alert_disposition_judgment_2026_10_11.md` | 53,188 | 2026-10-11 00:29:00 | `e7fcbc290a7e` | 成果面 |
| 11 | SUB | `results/_krj5_subject_scope_judgment_2026_10_11.md` | 45,372 | 2026-10-11 00:47:58 | `ae9df5119861` | 成果面 |
| 12 | REPO | `.tmp/_s4_seedprime_seq_t1_supplement_2026_10_11.py` | 31,705 | 2026-10-11 00:50:21 | `3a9db2126e4f` | 噪声面 |
| 13 | REPO | `results/_s4_seedprime_seq_t1_only_supplement_2026_10_11.md` | 24,783 | 2026-10-11 00:50:28 | `b2b044289ffe` | 成果面 |
| 14 | REPO | `results/_s4_seedprime_seq_t1_only_supplement_items_2026_10_11.json` | 28,030 | 2026-10-11 00:50:28 | `a834e0e7121a` | 成果面 |
| 15 | SUB | `results/_s3prime_recompute_after_supplement_2026_10_11.md` | 41,708 | 2026-10-11 00:59:13 | `fa025e4dc166` | 成果面 |
| 16 | SUB | `results/_q2_scope_vs_revision_judgment_2026_10_11.md` | 43,195 | 2026-10-11 01:01:21 | `b4f00e5a69c4` | 成果面 |
| 17 | SUB | `results/_round56_review_effectivity_register_5_2026_10_11.md` | 67,613 | 2026-10-11 01:04:02 | `5deba7d27bb1` | 成果面 |
| 18 | SUB | `results/_krj5_final_disposition_verdict_2026_10_11.md` | 60,700 | 2026-10-11 01:17:39 | `2b6bf509a135` | 成果面 |
| 19 | SUB | `results/_g10_threshold_closed_domain_judgment_2026_10_11.md` | 55,727 | 2026-10-11 01:18:04 | `586abda5ddf7` | 成果面 |
| 20 | REPO | `results/_s4prime_five_lines_runner_2026_10_11.py` | 29,813 | 2026-10-11 01:19:53 | `f784b2fc92f4` | 成果面 |
| 21 | SUB | `results/_s4prime_five_lines_readings_2026_10_11.md` | 23,877 | 2026-10-11 01:21:28 | `e91e7f52c726` | 成果面 |
| 22 | REPO | `results/_s4prime_five_lines_readings_2026_10_11.json` | 15,219 | 2026-10-11 01:22:11 | `65a9b9be6327` | 成果面 |
| 23 | SUB | `results/_round56_review_effectivity_register_6_2026_10_11.md` | 58,478 | 2026-10-11 01:37:31 | `2f3255ea344f` | 成果面 |
| 24 | SUB | `results/_s5prime_lim_a_and_item_registers_2026_10_11.md` | 47,225 | 2026-10-11 01:38:02 | `fa74831fa0ad` | 成果面 |
| 25 | SUB | `results/_f3f4_exit_drafts_2026_10_11.md` | 50,427 | 2026-10-11 01:44:40 | `523dc6cbdf9a` | 成果面 |
| 26 | SUB | `results/_pending_rulings_drafts_2026_10_11.md` | 42,775 | 2026-10-11 12:17:37 | `c8428b883029` | 成果面 |
| 27 | SUB | `results/_g11_krj4_effectivity_register_2026_10_11.md` | 39,870 | 2026-10-11 12:31:21 | `17168119eccc` | 成果面 |
| 28 | SUB | `results/_register3_bytes_erratum_2026_10_11.md` | 13,294 | 2026-10-11 12:32:09 | `f9f6805a7b76` | 成果面 |
| 29 | SUB | `results/_s6prime_terminal_verdicts_2026_10_11.md` | 54,937 | 2026-10-11 12:36:08 | `1c8ce58d6484` | 成果面 |
| 30 | SUB | `results/_f4_direction1_prereq_check_2026_10_11.md` | 38,664 | 2026-10-11 12:42:20 | `bb49153c311f` | 成果面 |
| 31 | SUB | `results/_f3_new_definition_draft_2026_10_11.md` | 48,068 | 2026-10-11 12:51:45 | `7482699e8b07` | 成果面 |
| 32 | SUB | `results/_questionnaire_cards_intake_register_supplement_13_2026_10_11.md` | 114,253 | 2026-10-11 12:52:21 | `43e0b642f8b2` | 成果面 |
| 33 | SUB | `results/_s7prime_prereq_and_verification_2026_10_11.md` | 36,787 | 2026-10-11 12:59:14 | `e44da4b83810` | 成果面 |
| 34 | SUB | `results/_f4_direction1_seed_and_domain_draft_2026_10_11.md` | 33,887 | 2026-10-11 13:29:50 | `f77c080d9fc6` | 成果面 |
| 35 | SUB | `results/_questionnaire_cards_intake_register_supplement_14_2026_10_11.md` | 54,883 | 2026-10-11 13:35:24 | `79bc4bfe38a5` | 成果面 |
| 36 | SUB | `results/_s7prime_findings_erratum_2026_10_11.md` | 31,008 | 2026-10-11 13:38:58 | `a7dfa8e789b7` | 成果面 |
| 37 | SUB | `results/_f3_definition_deep_judgment_2026_10_11.md` | 42,351 | 2026-10-11 13:46:07 | `11945e587b1d` | 成果面 |
| 38 | SUB | `results/_questionnaire_cards_intake_register_supplement_15_2026_10_11.md` | 44,698 | 2026-10-11 13:47:15 | `3654c41eda64` | 成果面 |
| 39 | SUB | `results/_seed_double_rule_judgment_2026_10_11.md` | 57,185 | 2026-10-11 14:02:53 | `f70a689fd8c1` | 成果面 |
| 40 | REPO | `results/_md_trigger_prereg_effectivity_2026_10_11.md` | 41,636 | 2026-10-11 14:03:16 | `5d8cd0d1676f` | 成果面 |
| 41 | REPO | `results/_f4_direction1_domain_effectivity_2026_10_11.md` | 40,301 | 2026-10-11 14:05:56 | `fd4ec7559342` | 成果面 |
| 42 | SUB | `results/_seed_double_criterion_draft_2026_10_11.md` | 40,499 | 2026-10-11 14:21:47 | `025212e91546` | 成果面 |
| 43 | SUB | `results/_pi_effectivity_declaration_register_2026_10_11.md` | 54,511 | 2026-10-11 14:22:34 | `41a82bde5190` | 成果面 |
| 44 | SUB | `results/_b14_audit_f2f3_closure_register_2026_10_11.md` | 29,620 | 2026-10-11 14:36:37 | `9d4a3d6ddf88` | 成果面 |
| 45 | SUB | `results/_stage1_tail_caliber_unification_register_2026_10_11.md` | 41,140 | 2026-10-11 14:41:24 | `d486ec491e8e` | 成果面 |
| 46 | SUB | `results/_pending_pi_items_drafts_2026_10_11.md` | 40,678 | 2026-10-11 14:44:15 | `55f469269d3d` | 成果面 |
| 47 | SUB | `results/_eps_ls_semantics_judgment_2026_10_11.md` | 31,391 | 2026-10-11 14:59:15 | `51434449ff3b` | 成果面 |
| 48 | SUB | `results/_kj1_sc1_premise_correction_2026_10_11.md` | 31,044 | 2026-10-11 14:59:46 | `8b344b9b4715` | 成果面 |
| 49 | SUB | `results/_kj1_abc_choice_judgment_2026_10_11.md` | 42,083 | 2026-10-11 15:02:27 | `d02ec6b0987e` | 成果面 |
| 50 | SUB | `results/_seed_double_identifier_final_judgment_2026_10_11.md` | 50,222 | 2026-10-11 15:02:43 | `728d18391748` | 成果面 |
| 51 | SUB | `results/_kj1_judgment_premise_correction_2026_10_11.md` | 35,050 | 2026-10-11 15:16:12 | `003b134cce24` | 成果面 |
| 52 | SUB | `results/_four_items_execution_batch_2026_10_11.md` | 31,515 | 2026-10-11 15:16:44 | `8006d1962e5f` | 成果面 |
| 53 | SUB | `results/_thv3_15_parallel_seed_double_note_2026_10_11.md` | 15,569 | 2026-10-11 15:17:29 | `3cd92287059e` | 成果面 |
| 54 | REPO | `results/_seed_double_identifier_finalization_2026_10_11.md` | 26,864 | 2026-10-11 15:36:15 | `6904852f8ceb` | 成果面 |
| 55 | SUB | `results/_ftfb_order_judgment_2026_10_11.md` | 45,911 | 2026-10-11 15:40:48 | `b6eec487e9d7` | 成果面 |
| 56 | SUB | `results/_kj1_eps_ls_effectivity_register_2026_10_11.md` | 62,344 | 2026-10-11 15:42:36 | `809edb4bb1cc` | 成果面 |
| 57 | SUB | `results/_j2_identifier_coupling_judgment_2026_10_11.md` | 34,261 | 2026-10-11 16:03:04 | `2fd4505fdca2` | 成果面 |
| 58 | SUB | `results/_s4_heldout_sampling_seedthird_extractor_2026_10_11.py` | 52,655 | 2026-10-11 16:03:09 | `068e1a7a1d04` | 成果面 |
| 59 | REPO | `results/_s4_heldout_sampling_seedthird_items_2026_10_11.json` | 43,130 | 2026-10-11 16:03:31 | `5777a07c608a` | 成果面 |
| 60 | REPO | `results/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | 22,646 | 2026-10-11 16:03:31 | `784f042bf93d` | 成果面 |
| 61 | SUB | `results/_five_pending_items_drafts_2026_10_11.md` | 55,102 | 2026-10-11 16:06:04 | `86c46998de63` | 成果面 |
| 62 | SUB | `results/_kj4_e4_unification_judgment_2026_10_11.md` | 36,839 | 2026-10-11 16:08:15 | `a14d49f7d3a2` | 成果面 |
| 63 | SUB | `results/_fp3_anchor_and_krj_restrament_register_2026_10_11.md` | 32,886 | 2026-10-11 16:22:16 | `b7c060ab2d49` | 成果面 |
| 64 | SUB | `results/_e4_lineage_conflict_correction_2026_10_11.md` | 30,510 | 2026-10-11 16:22:45 | `e20b96e32f54` | 成果面 |
| 65 | REPO | `results/_stage3_trigger_recheck_2026_10_11.md` | 49,109 | 2026-10-11 16:26:38 | `aef26b8cbe50` | 成果面 |
| 66 | SUB | `results/_five_items_effectivity_register_2026_10_11.md` | 43,332 | 2026-10-11 16:31:27 | `8affdca64b4b` | 成果面 |
| 67 | SUB | `results/_j2_kj4_disposition_register_2026_10_11.md` | 34,112 | 2026-10-11 16:37:29 | `c1a4ff1b96e5` | 成果面 |
| 68 | REPO | `results/_archive_2026-10-12/pycache_sink/results_pycache/_s4prime_five_lines_runner_2026_10_11.cpython-314.pyc` | 43,685 | 2026-10-11 16:51:05 | `f4194cc5a522` | 成果面 |
| 69 | SUB | `results/_s4prime_readings_runner_2026_10_11.py` | 23,766 | 2026-10-11 16:52:24 | `0aa414188361` | 成果面 |
| 70 | REPO | `results/_stage3_trigger_readings_items_2026_10_11.json` | 21,049 | 2026-10-11 16:52:40 | `079108c62a82` | 成果面 |
| 71 | SUB | `results/_g9_read_b_effectivity_register_2026_10_11.md` | 29,649 | 2026-10-11 16:53:23 | `f5d601a0602a` | 成果面 |
| 72 | SUB | `results/_c8_c2_disposition_register_2026_10_11.md` | 30,956 | 2026-10-11 16:53:47 | `fb816c572779` | 成果面 |
| 73 | SUB | `results/_stage3_extraction_verification_2026_10_11.md` | 22,399 | 2026-10-11 16:56:21 | `f973e6d737c3` | 成果面 |
| 74 | SUB | `results/_stage3_trigger_readings_2026_10_11.md` | 35,711 | 2026-10-11 16:56:23 | `2900948bca6d` | 成果面 |
| 75 | SUB | `results/_s6doubleprime_terminal_verdicts_2026_10_11.md` | 76,910 | 2026-10-11 17:10:58 | `bba3b889d849` | 成果面 |
| 76 | SUB | `results/_stage3_readings_verification_2026_10_11.md` | 29,956 | 2026-10-11 17:13:11 | `023a0cdd3350` | 成果面 |
| 77 | SUB | `results/_axis1_three_recomputations_2026_10_11.md` | 29,938 | 2026-10-11 17:26:24 | `8de23f7d7384` | 成果面 |
| 78 | SUB | `results/_s7doubleprime_verification_2026_10_11.md` | 41,680 | 2026-10-11 17:27:15 | `06ac684b4923` | 成果面 |
| 79 | SUB | `results/_c2_criterion_third_tier_draft_2026_10_11.md` | 26,713 | 2026-10-11 17:36:57 | `844179898102` | 成果面 |
| 80 | SUB | `results/_s6doubleprime_verdict_supplement_2026_10_11.md` | 31,515 | 2026-10-11 17:38:34 | `8e19c10ce219` | 成果面 |
| 81 | SUB | `results/_s7doubleprime_verification_erratum_2026_10_11.md` | 32,822 | 2026-10-11 17:39:50 | `9ff40693e4ac` | 成果面 |
| 82 | SUB | `results/_krj_all_terminal_verdicts_2026_10_11.md` | 95,659 | 2026-10-11 17:51:02 | `f52231807e36` | 成果面 |
| 83 | REPO | `.tmp/_s5dp_five_lines_runner_third_2026_10_11.py` | 31,138 | 2026-10-11 18:12:11 | `9de3c08e3863` | 噪声面 |
| 84 | SUB | `results/_s5doubleprime_five_lines_runner_2026_10_11.py` | 31,138 | 2026-10-11 18:12:11 | `9de3c08e3863` | 成果面 |
| 85 | REPO | `results/_s5doubleprime_five_lines_readings_2026_10_11.json` | 16,099 | 2026-10-11 18:14:08 | `839fb5452578` | 成果面 |
| 86 | REPO | `results/_archive_2026-10-12/pycache_sink/results_pycache/_s5doubleprime_five_lines_runner_2026_10_11.cpython-314.pyc` | 44,952 | 2026-10-11 20:32:37 | `9fc3e2152679` | 成果面 |
| 87 | SUB | `results/_krj_cond4_effectivity_declaration_2026_10_11.md` | 15,546 | 2026-10-11 20:32:37 | `f5c317f4cc96` | 成果面 |
| 88 | SUB | `results/_s5dp_mixed_object_erratum_2026_10_11.md` | 8,380 | 2026-10-11 20:36:49 | `07cde000e66f` | 成果面 |
| 89 | SUB | `results/_krj_cond4_bytes_erratum_2026_10_11.md` | 3,886 | 2026-10-11 20:41:59 | `78a95e5561fc` | 成果面 |
| 90 | SUB | `results/_s5prime_double_lim_a_and_item_registers_2026_10_11.md` | 58,378 | 2026-10-11 20:43:15 | `9a62fb2a6956` | 成果面 |
| 91 | SUB | `results/_krj4_trj1_adjudication_judgment_2026_10_11.md` | 30,293 | 2026-10-11 20:43:41 | `50e91bf30e45` | 成果面 |
| 92 | SUB | `results/_krj10_terminal_verdict_closure_2026_10_11.md` | 14,101 | 2026-10-11 20:52:41 | `f2e8e32089b2` | 成果面 |
| 93 | SUB | `results/_krj4_trj1_pick_and_pass_verdict_2026_10_11.md` | 16,567 | 2026-10-11 21:06:58 | `fb7bb5da85ec` | 成果面 |
| 94 | SUB | `results/_krj_all_five_verdicts_rewrite_2026_10_11.md` | 72,247 | 2026-10-11 21:12:00 | `78fb8c47c944` | 成果面 |
| 95 | SUB | `results/_krj_five_verdicts_adjudication_2026_10_11.md` | 16,064 | 2026-10-11 21:20:35 | `5c0efd663847` | 成果面 |
| 96 | SUB | `results/_u3_carrier_qid_verification_2026_10_11.md` | 21,572 | 2026-10-11 21:31:55 | `6509ae68f778` | 成果面 |
| 97 | SUB | `results/_krj_pi_picks_adoption_krj6_revise_2026_10_11.md` | 15,214 | 2026-10-11 21:34:15 | `31e32ccc59bf` | 成果面 |
| 98 | SUB | `results/_u6_negative_delta_compatibility_2026_10_11.md` | 20,969 | 2026-10-11 21:35:16 | `1846e917119f` | 成果面 |
| 99 | SUB | `results/_lim_aperiod_restatement_third_domain_2026_10_11.md` | 27,946 | 2026-10-11 21:38:15 | `8672a5541ca8` | 成果面 |
| 100 | SUB | `results/_lim_aperiod_adoption_and_label_correction_2026_10_11.md` | 14,770 | 2026-10-11 21:43:15 | `f4b129e3312f` | 成果面 |
| 101 | SUB | `results/_krj5d_third_tier_effectivity_2026_10_11.md` | 10,729 | 2026-10-11 21:52:41 | `062093d95c9f` | 成果面 |
| 102 | SUB | `results/_three_pending_items_drafts_2026_10_11.md` | 51,748 | 2026-10-11 21:55:16 | `8995859e5a76` | 成果面 |
| 103 | SUB | `results/_three_pending_items_effectivity_2026_10_11.md` | 16,744 | 2026-10-11 22:05:39 | `df1f5f75c7a0` | 成果面 |
| 104 | REPO | `letters/_commission_pending_pi_gaps_closeout_EN_2026_10_11.md` | 22,685 | 2026-10-11 22:27:45 | `0ce066e5eb3f` | 成果面 |
| 105 | SUB | `results/_misformed_commission_drafts_deletion_register_2026_10_11.md` | 7,261 | 2026-10-11 22:45:36 | `bbdc9c2c8028` | 成果面 |
| 106 | SUB | `results/_r3_wording_disposition_2026_10_11.md` | 3,917 | 2026-10-11 23:19:03 | `9d381c9d95e6` | 成果面 |
| 107 | SUB | `results/_r6_disposition_2026_10_11.md` | 3,704 | 2026-10-11 23:19:12 | `cc51203fe8f5` | 成果面 |
| 108 | SUB | `results/_r2_reference_pointer_disposition_2026_10_11.md` | 3,121 | 2026-10-11 23:19:28 | `403adec92ce1` | 成果面 |
| 109 | SUB | `results/_m5_eps_drift_disposition_2026_10_11.md` | 2,736 | 2026-10-11 23:19:36 | `0722f25f5838` | 成果面 |
| 110 | SUB | `results/_u_r_numbering_attribution_2026_10_11.md` | 5,331 | 2026-10-11 23:21:55 | `53672c23d7f9` | 成果面 |
| 111 | SUB | `results/_carrier_qid_disposition_2026_10_11.md` | 3,406 | 2026-10-11 23:22:17 | `7d74d5a4d81e` | 成果面 |
| 112 | SUB | `results/_r4_convergence_2026_10_11.md` | 3,133 | 2026-10-11 23:22:31 | `678394c47724` | 成果面 |
| 113 | REPO | `letters/_claude_pending_pi_gaps_closeout_reply_2026_10_11.md` | 22,064 | 2026-10-11 23:40:53 | `f4defae83553` | 成果面 |
| 114 | SUB | `results/_commission_closeout_erratum_and_supplement_2026_10_11.md` | 12,447 | 2026-10-11 23:46:12 | `7c102a6b4667` | 成果面 |

#### 2026-10-12（34 件）

| # | 区 | 相对路径 | bytes | mtime | SHA-12 | 类别 |
|---:|:--|:--|--:|:--|:--|:--|
| 1 | SUB | `results/_seven_gap_closures_adoption_register_2026_10_11.md` | 11,960 | 2026-10-12 00:02:59 | `ac3c41663f84` | 成果面 |
| 2 | SUB | `results/_krj10_reverdict_after_r4_convergence_2026_10_11.md` | 31,672 | 2026-10-12 00:05:01 | `a21915ec55a7` | 成果面 |
| 3 | SUB | `results/_executor_prereg_vs_impl_equivalence_2026_10_11.md` | 20,028 | 2026-10-12 00:08:14 | `e84cec618659` | 成果面 |
| 4 | SUB | `results/_pi_card_123_adoption_and_gate_one_request_2026_10_11.md` | 13,883 | 2026-10-12 00:11:11 | `0a4b752cbc56` | 成果面 |
| 5 | SUB | `results/_gate_one_declared_adoption_register_2026_10_11.md` | 12,923 | 2026-10-12 00:18:23 | `3a965362d4f4` | 成果面 |
| 6 | SUB | `results/_executor_prereg_docstring_correction_2026_10_11.md` | 27,721 | 2026-10-12 00:34:33 | `f7f8328c49ba` | 成果面 |
| 7 | SUB | `results/_kd_doc1_correction_adoption_register_2026_10_11.md` | 10,255 | 2026-10-12 00:39:06 | `c55770be5e33` | 成果面 |
| 8 | SUB | `results/_gate_one_pi_endorsement_register_2026_10_12.md` | 9,579 | 2026-10-12 00:53:49 | `b09209e9c20d` | 成果面 |
| 9 | SUB | `results/_five_stage_chain_design_reconstruction_2026_10_12.md` | 12,625 | 2026-10-12 01:02:53 | `bff2fb754564` | 成果面 |
| 10 | REPO | `letters/_commission_trae_direct_fix_2026_10_09_v0.1.md` | 37,262 | 2026-10-12 01:16:25 | `c50822b41539` | 成果面 |
| 11 | REPO | `deposon_team/plugins/_tdf_s1_2026_10_12.py` | 5,856 | 2026-10-12 01:23:22 | `5f9ab0ad7bab` | 成果面 |
| 12 | REPO | `deposon_team/plugins/_tdf_s1b_2026_10_12.py` | 8,064 | 2026-10-12 01:24:29 | `bebba19790c0` | 成果面 |
| 13 | REPO | `deposon_team/plugins/_tdf_s1c_2026_10_12.py` | 7,485 | 2026-10-12 01:26:27 | `d8bd9c41194a` | 成果面 |
| 14 | REPO | `deposon_team/plugins/_tdf_s2_apply_2026_10_12.py` | 10,899 | 2026-10-12 01:29:57 | `4bd6d16e20d7` | 成果面 |
| 15 | REPO | `results/_v3_recheck_08c_preexp_data/_v3_recheck_08c_sha12fix_r1_2026_10_12.py` | 1,395 | 2026-10-12 01:30:19 | `4b7ed4d0a3e5` | 成果面 |
| 16 | REPO | `results/_v3_recheck_08c_preexp_data/rescript_2026_09_27.md` | 17,069 | 2026-10-12 01:30:19 | `035af77db626` | 成果面 |
| 17 | REPO | `results/_v3_s2_executor/rescript_2026_09_27.md` | 25,151 | 2026-10-12 01:30:19 | `ff0f964be8aa` | 成果面 |
| 18 | REPO | `results/_v3_s_phrasetemplate_preexp_data/rescript_2026_09_27.md` | 17,574 | 2026-10-12 01:30:19 | `d42ea1fa61f1` | 成果面 |
| 19 | REPO | `deposon_team/plugins/_tdf_s3_jumps_2026_10_12.py` | 676 | 2026-10-12 01:30:39 | `16f7e10ac78f` | 成果面 |
| 20 | REPO | `deposon_team/plugins/_tdf_s3b_2026_10_12.py` | 1,229 | 2026-10-12 01:31:26 | `ccec66bb426e` | 成果面 |
| 21 | REPO | `letters/_trae_direct_fix_reply_trae_code_2026_10_12.md` | 21,379 | 2026-10-12 01:34:03 | `f37ebc80d1df` | 成果面 |
| 22 | REPO | `deposon_team/plugins/_tdf_s4_final_2026_10_12.py` | 2,695 | 2026-10-12 01:34:23 | `1df9a5d22e42` | 成果面 |
| 23 | SUB | `results/_stage2_trae_reply_acceptance_register_2026_10_12.md` | 14,874 | 2026-10-12 01:39:16 | `ce0b5a64cfce` | 成果面 |
| 24 | SUB | `results/_stage3_open_and_mandate_register_2026_10_12.md` | 13,865 | 2026-10-12 01:54:54 | `1b0a109a7914` | 成果面 |
| 25 | REPO | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 591,833 | 2026-10-12 02:11:15 | `96720fcfd76a` | 成果面 |
| 26 | REPO | `results/_v4_closeout_account_reconciliation_2026_10_12.md` | 24,453 | 2026-10-12 02:16:41 | `4a3b661a7d13` | 成果面 |
| 27 | REPO | `results/_v4_closeout_moves_and_cleanup_register_2026_10_12.md` | 18,568 | 2026-10-12 02:30:44 | `69a834caf812` | 成果面 |
| 28 | REPO | `results/_stage_sequence_violation_register_2026_10_12.md` | 11,159 | 2026-10-12 02:37:59 | `8dcfc200c7fd` | 成果面 |
| 29 | REPO | `results/_v4_closeout_bulk_reorganize_register_2026_10_12.md` | 197,283 | 2026-10-12 03:09:00 | `2b244f0760b4` | 成果面 |
| 30 | REPO | `results/_repo_post_cleanup_snapshot_2026_10_12.md` | 309,419 | 2026-10-12 03:09:29 | `6039a6e08017` | 成果面 |
| 31 | REPO | `results/_stage3_1_bulk_reorg_completion_register_2026_10_12.md` | 15,818 | 2026-10-12 03:16:00 | `7439157b7be4` | 成果面 |
| 32 | REPO | `results/_stage3_1_register_fingerprint_placeholder_erratum_2026_10_12.md` | 4,495 | 2026-10-12 03:17:23 | `a0e437ef317c` | 成果面 |
| 33 | REPO | `results/_stage1_independent_gate_review_2026_10_12.md` | 29,479 | 2026-10-12 03:17:28 | `4d95ae28c469` | 成果面 |
| 34 | REPO | `letters/_commission_trae_direct_fix_oct_full_coverage_2026_10_12.md` | 46,077 | 2026-10-12 03:18:02 | `60751abbeb3b` | 成果面 |

### §7.2 段面归并（**仅按件名之显式段标归并；无段标者 0 推断**）

| 段 | 件数 | 代表件（SHA-12） | 归并依据 |
|:--|--:|:--|:--|
| ①段（V3/V4 实验全量收束） | 90 | `results/_kv3s_4_4_review_carryover_2026_10_10.md`<br>`660d40ddd78c` | 件名含段别关键字（**关键词归并，非权威归段**） |
| ②段（Trae 走读与直接更正委托） | 4 | `letters/_commission_trae_direct_fix_2026_10_09_v0.1.md`<br>`c50822b41539` | 件名含段别关键字（**关键词归并，非权威归段**） |
| ③段（整理／清噪／拉平） | 18 | `results/_kd04_c_denominator_closeout_register_2026_10_10.md`<br>`78481cc60494` | 件名含段别关键字（**关键词归并，非权威归段**） |

⚠ **归段限度**：上表系**关键词归并**之**工作视图**，⛔ **0 断言**任一件之**权威段别归属**（段别权属 PI 宣告范畴）；重叠者计入多组，故各组之和 **≥ 471**。

## §8 · 漂移面（**只登记实测时点读数；⛔ 0 断言根因／已止／最终值**）

| # | 件 | 登记读数（出处） | 本棒实测（2026-10-12 03:20:44） | 处置 |
|:-:|:--|:--|:--|:--|
| **D-1** | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | `2fadea9f6259` · 355,369 B（其 erratum 件 §头登记） | `df7e9cd39251` · 355,819 B · mtime 2026-09-29 12:12:36 | ⛔ 0 断言成因（**02-后字节数与 mtime 均异**）；**0 回改** |
| **D-2** | `results/_v3_v4_achievements_inventory_2026_09_24.md` | `29a853444d42`（3dir 件 L6「Predecessor」登记） | `965db22e9130` · 194,083 B · mtime 2026-09-30 16:18:35 | ⛔ 0 断言成因；**0 回改** |
| **D-3** | `results/_v4_supp_t15_verdict.md`（**原派工单 #21**） | **四读并存**：29,106 ／ 55,352 ／ 52,884 ／ 54,377 | `3cb5c2f59961` · 54,377 B · mtime 2026-09-30 16:15:20 | ⛔ **0 断言根因／0 断言已止／0 断言最终值**——**仅登记第五读**（54,377 为本棒实测） |
| **D-4** | **REPO 盘面计数并发漂移** | 面-B 1,699（03:0x）／面-C 1,700（03:14）／面-A 1,704（2026-10-12 03:20:44） | 同左 | **0 校正**；并发写入件之一已核名（`_stage3_1_bulk_reorg_completion_register_2026_10_12.md`，03:16:00 落地）⇒ **⛔ 0 断言其为唯一差额来源** |
| **D-5** | `results/_upload_guard_mirror_pair_2026_10_08.md` | `d923371cdbce` · 23,534 B（`_stage_sequence_violation_register_2026_10_12.md` L67 登记） | `d923371cdbce` · 23,534 B · **在 SUB 区** | ⛔ 0 断言成因；登记件未注明区面 ⇒ **并列登记** |

📌 **D-3 说明**：派工单所述四读（29,106／55,352／52,884／54,377）与本棒实测第五读**并列在案**；**本棒对该件 0 触碰、0 复算、0 判定**——其处置权属 ③段-③（下一棒）。

## §9 · 「未核得」清单（凡未实测者一律写「未核得」＋原因）

| # | 项 | 状态 | 原因 |
|:-:|:--|:--|:--|
| **N-1** | `artifacts/plan.md` §四③段设计原文**之盘上实体** | 🔴 **未核得** | 该路径实体**已不在盘**；设计原文仅存于 `results/_questionnaire_cards_intake_register_2026_10_09.md` 卡载荷内（计划件自述 10-09 11:28 复核 ENOENT、全桶搜索 0 命中）。本件 §1.1 之授权引文即取自该载荷 |
| **N-2** | ARCHIVE 面（`_non_upload_local_archive`）之件数／bytes／逐件指纹 | 🔴 **未核得** | **本棒授权明令 0 读 0 写 0 列目录** ⇒ 三目录面之第三面缺失（§5.1）；⛔ **0 以 MAIN/SUB 之和代填**，⛔ **0 填估值** |
| **N-3** | `closing_round` 册 §2 棒④ 之 **W4 波**与 **U6 销项＋勘误** 两员之落地产件 | 🔴 **未核得** | 按件名关键字检索**两区 0 命中**；本棒 ⛔ 0 扩大检索面（⛔ 0 全内容扫描） |
| **N-4** | `.tmp/` 面 10-10 之前各件之逐件 SHA-12 | 🔴 **未核得** | 依 §2.3 既有惯例（transient 仅入 roll-up）**不逐件展开**；非「未测」而是「惯例不展开」——如需全展开须另立件 |
| **N-5** | `Deposon_v1_2_0_交付包` 之内容与指纹 | 🔴 **未核得（范围外）** | 该目录**不属 3dir**（§2.1）且不在本棒授权范围内 ⇒ **0 列目录** |
| **N-6** | 「三 addendum」之唯一所指 | 🔴 **未决** | §3.2.2 三候选并出，⛔ 0 自裁；**所需逐件指纹已全枚举在案**（§3.2.1） |
| **N-7** | 「三面计数」之唯一所指 | 🔴 **未决** | §2.2 义-1／义-2 两读并出，⛔ 0 自裁 |
| **N-8** | 派工单 `.tmp` 面 560 件之说 | 🔴 **未核得（差异并列）** | 本棒实测 441 件、快照登记 441 件 ⇒ 三读并列（§5.3），⛔ 0 校正 |
| **N-9** | 派工单 REPO 1,700 件之说 | 🔴 **未核得（差异并列）** | 三读并列（§5.2）⇒ ⛔ 0 校正 |

📌 **诚实交代**：①本件所有 SHA-12／bytes／mtime **均由本棒实测**（`sha256` 逐件），**0 填估值／0 推断值**；②「未核得」共 **8 项**（N-1…N-8 为未核得／未决，N-9 并入 N-8 族之计数差登记）；③**本棒曾列 `〔本地资料区〕` 顶层目录以定位 `plan.md`** ⇒ **禁触区 `_non_upload_local_archive` 之目录名被枚举一次**，其**内容 0 读 0 列**——如实登记。

## §10 · ⛔ 本件 0 作之事项（边界自述）

| # | 事项 | 本件之 0 |
|:-:|:--|:--|
| 1 | **0 宣告任何闭／开／段之毕**（含③段之毕、①毕之复核） | ✅ |
| 2 | **0 立收尾桶**（`results/_closeout_bucket_refresh_2026_10_09.md` 系③段-③ 之棒，本棒⛔ 0 启、0 预写） | ✅ |
| 3 | **0 代 PI 拍板**（A-1／A-2／A-4 三项歧义均列明候裁，⛔ 0 自裁） | ✅ |
| 4 | **0 回改任何既有件一字**（v1.0 族三件、③段-① 二件、底本五件，**全未触动**） | ✅ |
| 5 | **0 移动／重命名／删除任何文件**（整理已由③段-① 毕；本棒纯只读 ＋ 一件新落盘） | ✅ |
| 6 | **0 赋任一 `k_v3s_4_4_*` 布尔** | ✅ |
| 7 | **0 断言漂移根因／已止／最终值**（D-1…D-5 均只登记实测读数） | ✅ |
| 8 | **0 校正任何计数差异**（§5 三读并列即止） | ✅ |
| 9 | **0 填估值／推断值**（未核得即写未核得） | ✅ |
| 10 | **0 触碰禁触区** `_non_upload_local_archive`（0 读 0 写 0 列目录；顶层枚举一次已如实登记于 §9） | ✅ |
| 11 | **0 网络／0 skill／0 LLM／0 API**；**0 读 `.env`** | ✅ |
| 12 | **0 冒充** PI／parent／worker／verdict-keeper／verifier／protocol-keeper／evidence-auditor／Trae code／Claude Code／KIMI／GLM／coze | ✅ |
| 13 | **0 新建第二个文件**（本件系本棒唯一落盘件；临时脚本仅落 `%TEMP%` 并于交付后清理） | ✅ |

---

## 输入链表（本棒实读 · 逐件 SHA-12）

| # | 件／源 | 角色 | SHA-12 | bytes |
|---:|:--|:--|:--|--:|
| 1 | `results/_stage_sequence_violation_register_2026_10_12.md` | ③段-② 产件名之在册登记 | `8dcfc200c7fd` | 11,159 |
| 2 | `results/_v4_closeout_bulk_reorganize_register_2026_10_12.md` | ③段-① 整理执行登记 | `2b244f0760b4` | 197,283 |
| 3 | `results/_repo_post_cleanup_snapshot_2026_10_12.md` | 终态指纹底本 | `6039a6e08017` | 309,419 |
| 4 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 清点底本 | `96720fcfd76a` | 591,833 |
| 5 | `results/_v4_closeout_account_reconciliation_2026_10_12.md` | 账目校正 | `4a3b661a7d13` | 24,453 |
| 6 | `results/_v4_closeout_moves_and_cleanup_register_2026_10_12.md` | 转移与清噪登记 | `69a834caf812` | 18,568 |
| 7 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | v1.0 基件（惯例回查） | `965db22e9130` | 194,083 |
| 8 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | v1.0 3dir 件（3dir 定义来源） | `df7e9cd39251` | 355,819 |
| 9 | `results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md` | erratum（出件方同一） | `55cd332f66f2` | 10,288 |
| 10 | `results/_closing_round_8_decisions_register_2026_10_09.md` | closing_round 册（§6 对齐左列） | `a28a478e14a8` | 2,151 |
| 11 | `results/_questionnaire_cards_intake_register_2026_10_09.md` | plan.md 设计原文之载荷所在（§1.1 授权引文） | `d917180db36f` | 442,288 |
| 12 | `results/_fake_verdict_reverify_sixitem_ledger_2026_09_30.md` | 「0 校正」口径成文（§2.2） | `41d7b76ea4d6` | 40,957 |
| 13 | `results/_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json` | 「两口径并记·归口批量校正」成文（§2.2） | `769ef8b71462` | 374,072 |
| — | 本会话 PI 令 ＋ parent 派工单（2026-10-12 03:14） | 授权源（消息态，无指纹） | — | — |

---

**落款**：**doc-writer**（agent-0032834a3e04）｜五段链 ③段-② · 全量成果清单 v2.0 出件方

**⛔ 本件 0 代裁 · 0 宣告闭开 · 0 回改既有件 · 0 立收尾桶（下一棒）· 0 触碰禁触区 · 0 填充值**

**终行**：本件之计数／指纹系 **2026-10-12 03:20:44** 实测时点事实；后续落盘（含本件自身，REPO 将 **+1** 件）**0 追溯改写**本表。 *

