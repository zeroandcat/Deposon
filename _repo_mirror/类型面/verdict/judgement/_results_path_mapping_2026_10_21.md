# `_results_path_mapping_2026_10_21.md` — 档2「旧路径→新路径」预案映射表（拟案面 · 候 PI 裁）

| 项 | 值 |
| :-- | :-- |
| 件名 | `_results_path_mapping_2026_10_21.md` |
| 件路径 | `〔幽灵引用·未上传:_results_path_mapping_2026_10_21.md〕` |
| 件类 | 预案映射表（拟案）· 候 PI 裁 |
| 棒别 | `worker`（deposon 执行棒 · 执行面） |
| 观测时点 | **2026-10-21 10:23:58 (+08:00)**（与配套索引件同批实测） |
| 状态 | **拟案已落盘；⛔ 0 执行 —— 档2 之移动俟 PI 逐单令** |
| 本件射程 | **映射表件之落盘**（唯一写入） |
| 配套件 | `_results_index_2026_10_21.md`（索引件 · 族归属以该件为准） |
| 版本 | **v2**（升版：§0-4 自指污染面声明；§2/§4 引用面列与索引件 v2 同批） |

---

## §0 授权面之界分（首节 · 逐字载入）

### §0-1 PI 裁与本件之射程

> PI v173-Q1 裁「采候选戊 · 三档递进」
> —— 方案件 `_results_split_proposal_2026_10_21.md`（族标 `_results_split_proposal*` · SHA-12 `38eff36f1438` · 36,323 B · 白话：
> 「整理文件夹（拆分 results）」之方案件）

方案件 §2 候选戊：**档0** ＝ 立索引件 ＋「旧路径→新路径」映射表（**零移动**、零断链）；
**档2** ＝ 族级移动（**俟 PI 逐单令**）。**本件即档0 之映射表件 —— 拟案面，非执行面。**

### §0-2 统一声明（本表一切条目皆适用）

> **以下每一条「旧路径 → 拟新路径」映射条目均为预案（拟案面），⛔ 0 执行。**
> **任何既有件之移动／重命名／删除，一律俟 PI 逐单令后方可执行**（方案件 §0-2 勘误注记：铁律不动 ＋ 整理之方案面之拟开；
> 移动之执行须 PI 逐单令 —— ⛔ 0 以「整理文件夹」之令径充移动之执行之授权）。

### §0-3 本棒之禁（逐条遵行）

1. ⛔ 0 移动／重命名／删除任何既有件一字。
2. ⛔ 0 于仓内新建任何目录（拟新路径**仅为文字预案**，未落任何目录）。
3. ⛔ 0 回改任何既有件（本面 0 追加）。
4. ⛔ 0 代裁 · ⛔ 0 落五终判 · ⛔ 0 闭任何 KD · ⛔ 0 宣告段毕。
5. ⛔ 0 联网 · ⛔ 0 读 key · ⛔ 0 触归档区／GLM 写面。
6. ⛔ 0 扩张族界：**771** 件无机械族界者一律标「候 PI 归族」，**不代 PI 拟其族**。

### §0-4 停手闸记录与「自指污染面」

落笔前长名式探测（`Get-ChildItem -Recurse -Force` ＋ `.Name -like` 匹配，⛔ 0 单用 `-Filter`）：

| 目标名 | 长名式命中 | `Test-Path` | 判定 |
| :-- | --: | :-- | :-- |
| `_results_index_2026_10_21.md` | **0** | **False** | 放行 |
| `_results_path_mapping_2026_10_21.md` | **0** | **False** | 放行 |

⚠ **自指污染面**：本映射表件与配套索引件**载有全部件名**。故引用面之测量（§2 之「引用面」列）
**已排除本二件**（否则「每一件皆被指名」将由自证而得）。**后续棒若再作引用面扫描，须同此排除。**

### §0-5 路径基准

**旧路径基准** ＝ 仓根 `〔本地路径已脱敏〕` 之**相对路径**（正斜杠，`results/…`）。
**拟新路径**亦以同基准书写。**拟新路径未落盘、未建目录。**

---

## §1 拟新路径之形态（族级移动之子目录方案）

**形态**：于 `results\` 之下建**族目录**，族内件由顶层移入该族目录 —— 此即方案件 §2 候选甲所述之族界形态，
候选戊之档2（族级移动）沿用之。**族目录命名本棒以「族判据前缀」之机械形式拟定（拟案命名 · 候 PI 裁）**
（方案件候选甲之举例为 `_v\`／`_kd\`／`pi\`／`deposon_\` 等，本表按同一形态取前缀机械形，命名之最终裁归 PI）。

| 族 | 拟族目录名（预案） | 族内件数（顶层口径） | 该族之白话（其义） |
| :-- |--: |--: |--: |
| `_v*` | `results/_v/` | 357 | v 系列落账件族: 实验执行/裁决/登记/读数之主流族 |
| `_kd*` | `results/_kd/` | 62 | kd 族: 已知缺陷面之登记/读数/效应件 |
| `deposon_*` | `results/deposon_/` | 97 | 无前导下划线之早期产物件族 (benchmark/volcengine/v15-v22 等) |
| `_pi_*` | `results/_pi_/` | 6 | pi 面: PI 卡片问答之登记件族 |
| `_root_session_history_memo*` | `results/_root_session_history_memo/` | 2 | 双备忘录两件 (主代理版/子棒版) |
| `boss_*` | `results/boss_/` | 12 | boss 面早期基准件族 |
| `c5_*` | `results/c5_/` | 6 | c5 面护栏/最小最大标准差重算件族 |
| `_d13*` | `results/_d13/` | 1 | d13 面单件 |
| `d7_*` | `results/d7_/` | 1 | d7 面单件 |
| `ge01_*` | `results/ge01_/` | 1 | ge01 面单件 |
| **无机械族界** | **（未定）** | **771** | 无机械族界 —— **俟 PI 归族**，本棒不拟其族目录名 |

⚠ **双重保护面（先例继承 · 方案件 §4-3／§4-4）**：

| 保护面 | 件 | 档2 之处置 |
| :-- | :-- | :-- |
| 双备忘录两件 | `_root_session_history_memo_main_2026_10_14.md`、`_root_session_history_memo_2026_10_14.md` | **不移动**（任何族界不得含此二件） |
| 关键链 | `_v4_pi_cot_v2_*` 全系 | **不移动**（2026-09-26 移动账之先例保护名单） |

---

## §2 映射条目 · 顶层件（按族轴编排）

**每条**：旧路径 → 拟新路径 ｜ 族 ｜ 引用面 ｜ 档2 关联判死线（引自方案件 §3-4 · 其义见该件）。

### §2-1 族 `_v*` — 357 条

| # | 旧路径 | 拟新路径 | 族 | 引用面 | 档2 关联判死线 |
| :-- |--: |--: |--: |--: |--: |
| 1 | `_v123_adoption_effect_2026_10_18.md` | `results/_v/_v123_adoption_effect_2026_10_18.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 2 | `_v133_adoption_effect_2026_10_19.md` | `results/_v/_v133_adoption_effect_2026_10_19.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 3 | `_v136_adoption_effect_2026_10_19.md` | `results/_v/_v136_adoption_effect_2026_10_19.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 4 | `_v137_adoption_effect_2026_10_19.md` | `results/_v/_v137_adoption_effect_2026_10_19.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 5 | `_v138_adoption_effect_2026_10_19.md` | `results/_v/_v138_adoption_effect_2026_10_19.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 6 | `_v139_adoption_effect_2026_10_19.md` | `results/_v/_v139_adoption_effect_2026_10_19.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 7 | `_v140_adoption_effect_2026_10_19.md` | `results/_v/_v140_adoption_effect_2026_10_19.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 8 | `_v141_adoption_effect_2026_10_19.md` | `results/_v/_v141_adoption_effect_2026_10_19.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 9 | `_v142_adoption_effect_2026_10_19.md` | `results/_v/_v142_adoption_effect_2026_10_19.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 10 | `_v143_v144_adoption_effect_2026_10_19.md` | `results/_v/_v143_v144_adoption_effect_2026_10_19.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 11 | `_v145_adoption_effect_2026_10_20.md` | `results/_v/_v145_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 12 | `_v146_adoption_effect_2026_10_20.md` | `results/_v/_v146_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 13 | `_v148_adoption_effect_2026_10_20.md` | `results/_v/_v148_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 14 | `_v148_four_points_erratum_draft_2026_10_20.md` | `results/_v/_v148_four_points_erratum_draft_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 15 | `_v149_adoption_effect_2026_10_20.md` | `results/_v/_v149_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 16 | `_v150_adoption_effect_2026_10_20.md` | `results/_v/_v150_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 17 | `_v151_adoption_effect_2026_10_20.md` | `results/_v/_v151_adoption_effect_2026_10_20.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 18 | `_v152_adoption_effect_2026_10_20.md` | `results/_v/_v152_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 19 | `_v153_adoption_effect_2026_10_20.md` | `results/_v/_v153_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 20 | `_v154_adoption_effect_2026_10_20.md` | `results/_v/_v154_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 21 | `_v155_adoption_effect_2026_10_20.md` | `results/_v/_v155_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 22 | `_v156_adoption_effect_2026_10_20.md` | `results/_v/_v156_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 23 | `_v157_adoption_effect_2026_10_20.md` | `results/_v/_v157_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 24 | `_v158_adoption_effect_2026_10_20.md` | `results/_v/_v158_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 25 | `_v159_adoption_effect_2026_10_20.md` | `results/_v/_v159_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 26 | `_v162_adoption_effect_2026_10_20.md` | `results/_v/_v162_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 27 | `_v163_adoption_effect_2026_10_20.md` | `results/_v/_v163_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 28 | `_v164_adoption_effect_2026_10_20.md` | `results/_v/_v164_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 29 | `_v165_adoption_effect_2026_10_20.md` | `results/_v/_v165_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 30 | `_v166_adoption_effect_2026_10_20.md` | `results/_v/_v166_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 31 | `_v167_adoption_effect_2026_10_20.md` | `results/_v/_v167_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 32 | `_v168_adoption_effect_2026_10_20.md` | `results/_v/_v168_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 33 | `_v169_adoption_effect_2026_10_20.md` | `results/_v/_v169_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 34 | `_v170_adoption_effect_2026_10_20.md` | `results/_v/_v170_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 35 | `_v171_adoption_effect_2026_10_20.md` | `results/_v/_v171_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 36 | `_v172_adoption_effect_2026_10_20.md` | `results/_v/_v172_adoption_effect_2026_10_20.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 37 | `_v173_adoption_effect_2026_10_21.md` | `results/_v/_v173_adoption_effect_2026_10_21.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 38 | `_v34_experiment_gap_plan_2026_10_08.md` | `results/_v/_v34_experiment_gap_plan_2026_10_08.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 39 | `_v3_construct_degradation_diag_2026_09_23.json` | `results/_v/_v3_construct_degradation_diag_2026_09_23.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 40 | `_v3_n_cpath_live_data_2026_09_27.json` | `results/_v/_v3_n_cpath_live_data_2026_09_27.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 41 | `_v3_n_ktb1_distortion_bound_data_2026_09_27.json` | `results/_v/_v3_n_ktb1_distortion_bound_data_2026_09_27.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 42 | `_v3_n_pg_boss_live_data_2026_09_27.json` | `results/_v/_v3_n_pg_boss_live_data_2026_09_27.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 43 | `_v3_n_recheck_llm_verdict_2026_09_27.md` | `results/_v/_v3_n_recheck_llm_verdict_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 44 | `_v3_recheck_01_executor_2026_09_27.py` | `results/_v/_v3_recheck_01_executor_2026_09_27.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 45 | `_v3_recheck_01_rescript_2026_09_27.md` | `results/_v/_v3_recheck_01_rescript_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 46 | `_v3_recheck_01_result_2026_09_27.json` | `results/_v/_v3_recheck_01_result_2026_09_27.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 47 | `_v3_recheck_04_executor_2026_09_27.py` | `results/_v/_v3_recheck_04_executor_2026_09_27.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 48 | `_v3_recheck_04_rescript_2026_09_27.md` | `results/_v/_v3_recheck_04_rescript_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 49 | `_v3_recheck_04_result_2026_09_27.json` | `results/_v/_v3_recheck_04_result_2026_09_27.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 50 | `_v3_recheck_05_rescript_2026_09_28.md` | `results/_v/_v3_recheck_05_rescript_2026_09_28.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 51 | `_v3_recheck_05_result_2026_09_28.json` | `results/_v/_v3_recheck_05_result_2026_09_28.json` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 52 | `_v3_recheck_08_executor_2026_09_27.py` | `results/_v/_v3_recheck_08_executor_2026_09_27.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 53 | `_v3_recheck_08_rescript_2026_09_27.md` | `results/_v/_v3_recheck_08_rescript_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 54 | `_v3_recheck_08_result_2026_09_27.json` | `results/_v/_v3_recheck_08_result_2026_09_27.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 55 | `_v3_recheck_10_rescript_2026_09_27.md` | `results/_v/_v3_recheck_10_rescript_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 56 | `_v3_recheck_10_result_2026_09_27.json` | `results/_v/_v3_recheck_10_result_2026_09_27.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 57 | `_v3_recheck_12_jsv_check_2026_09_27.md` | `results/_v/_v3_recheck_12_jsv_check_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 58 | `_v3_recheck_12_rescript_2026_09_27.md` | `results/_v/_v3_recheck_12_rescript_2026_09_27.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 59 | `_v3_recheck_12_result_2026_09_27.json` | `results/_v/_v3_recheck_12_result_2026_09_27.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 60 | `_v3_recheck_12_rj5_provenance_2026_09_27.md` | `results/_v/_v3_recheck_12_rj5_provenance_2026_09_27.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 61 | `_v3_recheck_19_rescript_2026_09_27.md` | `results/_v/_v3_recheck_19_rescript_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 62 | `_v3_recheck_19_result_2026_09_27.json` | `results/_v/_v3_recheck_19_result_2026_09_27.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 63 | `_v3_recheck_21_rescript_2026_09_27.md` | `results/_v/_v3_recheck_21_rescript_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 64 | `_v3_recheck_21_result_2026_09_27.json` | `results/_v/_v3_recheck_21_result_2026_09_27.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 65 | `_v3_recheck_26_executor_2026_09_27.py` | `results/_v/_v3_recheck_26_executor_2026_09_27.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 66 | `_v3_recheck_26_preexp_data_2026_09_27.json` | `results/_v/_v3_recheck_26_preexp_data_2026_09_27.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 67 | `_v3_recheck_26_preexp_executor_2026_09_27.py` | `results/_v/_v3_recheck_26_preexp_executor_2026_09_27.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 68 | `_v3_recheck_26_preexp_report_2026_09_27.md` | `results/_v/_v3_recheck_26_preexp_report_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 69 | `_v3_recheck_26_rescript_2026_09_27.md` | `results/_v/_v3_recheck_26_rescript_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 70 | `_v3_recheck_26_result_2026_09_27.json` | `results/_v/_v3_recheck_26_result_2026_09_27.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 71 | `_v3_recheck_26b_executor_2026_09_27.py` | `results/_v/_v3_recheck_26b_executor_2026_09_27.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 72 | `_v3_recheck_26b_executor_r2_2026_09_28.py` | `results/_v/_v3_recheck_26b_executor_r2_2026_09_28.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 73 | `_v3_recheck_26b_executor_r3_2026_09_29.py` | `results/_v/_v3_recheck_26b_executor_r3_2026_09_29.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 74 | `_v3_recheck_26b_r3_result_2026_09_29.json` | `results/_v/_v3_recheck_26b_r3_result_2026_09_29.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 75 | `_v3_recheck_26b_rescript_2026_09_27.md` | `results/_v/_v3_recheck_26b_rescript_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 76 | `_v3_recheck_26b_result_2026_09_27.json` | `results/_v/_v3_recheck_26b_result_2026_09_27.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 77 | `_v3_recheck_26b_verdict_prep_2026_10_01.md` | `results/_v/_v3_recheck_26b_verdict_prep_2026_10_01.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 78 | `_v3_recheck_27_rescript_2026_09_27.md` | `results/_v/_v3_recheck_27_rescript_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 79 | `_v3_recheck_27_result_2026_09_27.json` | `results/_v/_v3_recheck_27_result_2026_09_27.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 80 | `_v3_recheck_28_rescript_2026_09_27.md` | `results/_v/_v3_recheck_28_rescript_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 81 | `_v3_recheck_28_result_2026_09_27.json` | `results/_v/_v3_recheck_28_result_2026_09_27.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 82 | `_v3_recheck_35_rescript_2026_09_27.md` | `results/_v/_v3_recheck_35_rescript_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 83 | `_v3_recheck_35_result_2026_09_27.json` | `results/_v/_v3_recheck_35_result_2026_09_27.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 84 | `_v3_recheck_prereg_v1_2026_09_27.md` | `results/_v/_v3_recheck_prereg_v1_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 85 | `_v3_recheck_prereg_v1p1_2026_09_27.md` | `results/_v/_v3_recheck_prereg_v1p1_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 86 | `_v3_recheck_prereg_v1p2_2026_09_27.md` | `results/_v/_v3_recheck_prereg_v1p2_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 87 | `_v3_recheck_prereg_v1p3_2026_09_27.md` | `results/_v/_v3_recheck_prereg_v1p3_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 88 | `_v3_recheck_prereg_v1p4_2026_09_27.md` | `results/_v/_v3_recheck_prereg_v1p4_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 89 | `_v3_recheck_prereg_v1p5_2026_09_29.md` | `results/_v/_v3_recheck_prereg_v1p5_2026_09_29.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 90 | `_v3_recheck_verdict_register_2026_09_27.md` | `results/_v/_v3_recheck_verdict_register_2026_09_27.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 91 | `_v3_s3_collection_brief_2026_09_28.md` | `results/_v/_v3_s3_collection_brief_2026_09_28.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 92 | `_v3_s3_wordexpand_recheck_r1_2026_09_28.json` | `results/_v/_v3_s3_wordexpand_recheck_r1_2026_09_28.json` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 93 | `_v3_s_phrasetemplate_prereg_v1_2026_09_27.md` | `results/_v/_v3_s_phrasetemplate_prereg_v1_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 94 | `_v3_s_prereg_v1_2026_09_27.md` | `results/_v/_v3_s_prereg_v1_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 95 | `_v3_supplement_verdict_2026_09_23.md` | `results/_v/_v3_supplement_verdict_2026_09_23.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 96 | `_v3_v4_achievements_inventory_2026_09_24.md` | `results/_v/_v3_v4_achievements_inventory_2026_09_24.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 97 | `_v3_v4_achievements_inventory_3dir_2026_09_24.md` | `results/_v/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 98 | `_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md` | `results/_v/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 99 | `_v3_v4_ghostref_reconciliation_2026_09_23.md` | `results/_v/_v3_v4_ghostref_reconciliation_2026_09_23.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 100 | `_v3n_cpath_live_rerun_2026_10_01.json` | `results/_v/_v3n_cpath_live_rerun_2026_10_01.json` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 101 | `_v3x_conservation_anchor_2026_09_17.txt` | `results/_v/_v3x_conservation_anchor_2026_09_17.txt` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 102 | `_v3x_d0_5_aggregation_2026_09_17.md` | `results/_v/_v3x_d0_5_aggregation_2026_09_17.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 103 | `_v3x_d0_5_experiment_invitation_2026_09_17.md` | `results/_v/_v3x_d0_5_experiment_invitation_2026_09_17.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 104 | `_v3x_d0_5_proposal_coze_2026_09_17.md` | `results/_v/_v3x_d0_5_proposal_coze_2026_09_17.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 105 | `_v3x_d0_5_proposal_trae_2026_09_17.md` | `results/_v/_v3x_d0_5_proposal_trae_2026_09_17.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 106 | `_v3x_p_l_v3_external_spec_2026_09_17.md` | `results/_v/_v3x_p_l_v3_external_spec_2026_09_17.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 107 | `_v3x_p_l_v3_mistral_large_2512_20260917_115049.json` | `results/_v/_v3x_p_l_v3_mistral_large_2512_20260917_115049.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 108 | `_v3x_p_l_v3_summary_mistral_large_2512_20260917_115049.md` | `results/_v/_v3x_p_l_v3_summary_mistral_large_2512_20260917_115049.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 109 | `_v4_bom_u1_prereg_2026_09_28.md` | `results/_v/_v4_bom_u1_prereg_2026_09_28.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 110 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md` | `results/_v/_v4_checkpoint_atomic_and_pycache_2026_09_28.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 111 | `_v4_closeout_account_reconciliation_2026_10_12.md` | `results/_v/_v4_closeout_account_reconciliation_2026_10_12.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 112 | `_v4_closeout_bulk_reorganize_register_2026_10_12.md` | `results/_v/_v4_closeout_bulk_reorganize_register_2026_10_12.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 113 | `_v4_closeout_moves_and_cleanup_register_2026_10_12.md` | `results/_v/_v4_closeout_moves_and_cleanup_register_2026_10_12.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 114 | `_v4_day_inventory_2026_09_27.md` | `results/_v/_v4_day_inventory_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 115 | `_v4_day_inventory_measure_2026_09_27.py` | `results/_v/_v4_day_inventory_measure_2026_09_27.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 116 | `_v4_effective_register_2026_09_28.md` | `results/_v/_v4_effective_register_2026_09_28.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 117 | `_v4_evidence_audit_reconcile_2026_09_26.md` | `results/_v/_v4_evidence_audit_reconcile_2026_09_26.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 118 | `_v4_exec_surface_switch_2026_09_28.md` | `results/_v/_v4_exec_surface_switch_2026_09_28.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 119 | `_v4_item04_textfix_prereg_v1x_2026_09_28.md` | `results/_v/_v4_item04_textfix_prereg_v1x_2026_09_28.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 120 | `_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` | `results/_v/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 121 | `_v4_maindir_count_monitor_2026_09_27.md` | `results/_v/_v4_maindir_count_monitor_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 122 | `_v4_pi_cot_v2_coding_review_2026_09_26.md` | `_v4_pi_cot_v2_coding_review_2026_09_26.md`（**原地不动**） | _v* | 相对路径引用 | **保护面 · 不移动** |
| 123 | `_v4_pi_cot_v2_dataset.json` | `_v4_pi_cot_v2_dataset.json`（**原地不动**） | _v* | 相对路径引用 | **保护面 · 不移动** |
| 124 | `_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | `_v4_pi_cot_v2_dataset_addendum_2026_09_24.json`（**原地不动**） | _v* | 相对路径引用 | **保护面 · 不移动** |
| 125 | `_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json` | `_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json`（**原地不动**） | _v* | 相对路径引用 | **保护面 · 不移动** |
| 126 | `_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json` | `_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json`（**原地不动**） | _v* | 相对路径引用 | **保护面 · 不移动** |
| 127 | `_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json` | `_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json`（**原地不动**） | _v* | 相对路径引用 | **保护面 · 不移动** |
| 128 | `_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json` | `_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json`（**原地不动**） | _v* | 相对路径引用 | **保护面 · 不移动** |
| 129 | `_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json` | `_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json`（**原地不动**） | _v* | 相对路径引用 | **保护面 · 不移动** |
| 130 | `_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json` | `_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json`（**原地不动**） | _v* | 相对路径引用 | **保护面 · 不移动** |
| 131 | `_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json` | `_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json`（**原地不动**） | _v* | 相对路径引用 | **保护面 · 不移动** |
| 132 | `_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | `_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json`（**原地不动**） | _v* | 相对路径引用 | **保护面 · 不移动** |
| 133 | `_v4_pi_cot_v2_prereg.md` | `_v4_pi_cot_v2_prereg.md`（**原地不动**） | _v* | 相对路径引用 | **保护面 · 不移动** |
| 134 | `_v4_pi_cot_v2_questionnaire_v1.md` | `_v4_pi_cot_v2_questionnaire_v1.md`（**原地不动**） | _v* | 相对路径引用 | **保护面 · 不移动** |
| 135 | `_v4_pi_cot_v2_result.json` | `_v4_pi_cot_v2_result.json`（**原地不动**） | _v* | 相对路径引用 | **保护面 · 不移动** |
| 136 | `_v4_pi_cot_v2_result_v2.json` | `_v4_pi_cot_v2_result_v2.json`（**原地不动**） | _v* | 相对路径引用 | **保护面 · 不移动** |
| 137 | `_v4_pi_cot_v2_ruleset.json` | `_v4_pi_cot_v2_ruleset.json`（**原地不动**） | _v* | 相对路径引用 | **保护面 · 不移动** |
| 138 | `_v4_pi_cot_v2_ruleset_executor.py` | `_v4_pi_cot_v2_ruleset_executor.py`（**原地不动**） | _v* | 相对路径引用 | **保护面 · 不移动** |
| 139 | `_v4_pi_cot_v2_ruleset_v2.json` | `_v4_pi_cot_v2_ruleset_v2.json`（**原地不动**） | _v* | 相对路径引用 | **保护面 · 不移动** |
| 140 | `_v4_pi_cot_v2_ruleset_v2_executor.py` | `_v4_pi_cot_v2_ruleset_v2_executor.py`（**原地不动**） | _v* | 仓根锚定路径引用 | **保护面 · 不移动** |
| 141 | `_v4_pi_cot_v2_verdict.md` | `_v4_pi_cot_v2_verdict.md`（**原地不动**） | _v* | 相对路径引用 | **保护面 · 不移动** |
| 142 | `_v4_pi_cot_v2_verdict_v2.md` | `_v4_pi_cot_v2_verdict_v2.md`（**原地不动**） | _v* | 相对路径引用 | **保护面 · 不移动** |
| 143 | `_v4_pi_cot_v3_alt_reading_definition_2026_09_27.md` | `results/_v/_v4_pi_cot_v3_alt_reading_definition_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 144 | `_v4_pi_cot_v3_dataset.json` | `results/_v/_v4_pi_cot_v3_dataset.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 145 | `_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json` | `results/_v/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 146 | `_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json` | `results/_v/_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 147 | `_v4_pi_cot_v3_dataset_addendum_d5_2026_09_27.json` | `results/_v/_v4_pi_cot_v3_dataset_addendum_d5_2026_09_27.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 148 | `_v4_pi_cot_v3_dataset_addendum_d6_2026_09_28.json` | `results/_v/_v4_pi_cot_v3_dataset_addendum_d6_2026_09_28.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 149 | `_v4_pi_cot_v3_dataset_addendum_d6b_2026_09_28.json` | `results/_v/_v4_pi_cot_v3_dataset_addendum_d6b_2026_09_28.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 150 | `_v4_pi_cot_v3_dataset_addendum_d8_bhalf_2026_09_30.json` | `results/_v/_v4_pi_cot_v3_dataset_addendum_d8_bhalf_2026_09_30.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 151 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json` | `results/_v/_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 152 | `_v4_pi_cot_v3_dataset_addendum_s3_d1fill_2026_10_01.json` | `results/_v/_v4_pi_cot_v3_dataset_addendum_s3_d1fill_2026_10_01.json` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 153 | `_v4_pi_cot_v3_dataset_addendum_s3_d7_2026_09_29.json` | `results/_v/_v4_pi_cot_v3_dataset_addendum_s3_d7_2026_09_29.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 154 | `_v4_pi_cot_v3_dataset_v1p3_2026_09_27.json` | `results/_v/_v4_pi_cot_v3_dataset_v1p3_2026_09_27.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 155 | `_v4_pi_cot_v3_k3b_recheck_r1_2026_09_27.json` | `results/_v/_v4_pi_cot_v3_k3b_recheck_r1_2026_09_27.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 156 | `_v4_pi_cot_v3_missing_ledger_correction_2026_09_28.md` | `results/_v/_v4_pi_cot_v3_missing_ledger_correction_2026_09_28.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 157 | `_v4_pi_cot_v3_prereg.md` | `results/_v/_v4_pi_cot_v3_prereg.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 158 | `_v4_pi_cot_v3_questionnaire_v2_d8_2026_09_28.md` | `results/_v/_v4_pi_cot_v3_questionnaire_v2_d8_2026_09_28.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 159 | `_v4_pi_cot_v3_result_v3.json` | `results/_v/_v4_pi_cot_v3_result_v3.json` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 160 | `_v4_pi_cot_v3_result_v3r1_2026_09_27.json` | `results/_v/_v4_pi_cot_v3_result_v3r1_2026_09_27.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 161 | `_v4_pi_cot_v3_ruleset_v3.json` | `results/_v/_v4_pi_cot_v3_ruleset_v3.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 162 | `_v4_pi_cot_v3_ruleset_v3_executor.py` | `results/_v/_v4_pi_cot_v3_ruleset_v3_executor.py` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 163 | `_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py` | `results/_v/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 164 | `_v4_pi_cot_v3_v3r1_rescript_2026_09_27.md` | `results/_v/_v4_pi_cot_v3_v3r1_rescript_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 165 | `_v4_pi_cot_v3_verdict_v3.md` | `results/_v/_v4_pi_cot_v3_verdict_v3.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 166 | `_v4_pi_cot_v3_verdict_v3_signoff_2026_09_27.md` | `results/_v/_v4_pi_cot_v3_verdict_v3_signoff_2026_09_27.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 167 | `_v4_supp_l14_n11full_verdict.md` | `results/_v/_v4_supp_l14_n11full_verdict.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 168 | `_v4_supp_l14v3_batch10_r1_executor.py` | `results/_v/_v4_supp_l14v3_batch10_r1_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 169 | `_v4_supp_l14v3_batch10_r1_result.json` | `results/_v/_v4_supp_l14v3_batch10_r1_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 170 | `_v4_supp_l14v3_batch10_r2_executor.py` | `results/_v/_v4_supp_l14v3_batch10_r2_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 171 | `_v4_supp_l14v3_batch10_r2_result.json` | `results/_v/_v4_supp_l14v3_batch10_r2_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 172 | `_v4_supp_l14v3_batch10_r3_executor.py` | `results/_v/_v4_supp_l14v3_batch10_r3_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 173 | `_v4_supp_l14v3_batch10_r3_result.json` | `results/_v/_v4_supp_l14v3_batch10_r3_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 174 | `_v4_supp_l14v3_batch10_r4_executor.py` | `results/_v/_v4_supp_l14v3_batch10_r4_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 175 | `_v4_supp_l14v3_batch10_r4_result.json` | `results/_v/_v4_supp_l14v3_batch10_r4_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 176 | `_v4_supp_l14v3_batch10_r5_result.json` | `results/_v/_v4_supp_l14v3_batch10_r5_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 177 | `_v4_supp_l14v3_batch1_executor.py` | `results/_v/_v4_supp_l14v3_batch1_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 178 | `_v4_supp_l14v3_batch1_r2_executor.py` | `results/_v/_v4_supp_l14v3_batch1_r2_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 179 | `_v4_supp_l14v3_batch1_r2_result.json` | `results/_v/_v4_supp_l14v3_batch1_r2_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 180 | `_v4_supp_l14v3_batch1_r3_executor.py` | `results/_v/_v4_supp_l14v3_batch1_r3_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 181 | `_v4_supp_l14v3_batch1_r3_result.json` | `results/_v/_v4_supp_l14v3_batch1_r3_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 182 | `_v4_supp_l14v3_batch1_r4_executor.py` | `results/_v/_v4_supp_l14v3_batch1_r4_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 183 | `_v4_supp_l14v3_batch1_r4_result.json` | `results/_v/_v4_supp_l14v3_batch1_r4_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 184 | `_v4_supp_l14v3_batch1_r5_executor.py` | `results/_v/_v4_supp_l14v3_batch1_r5_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 185 | `_v4_supp_l14v3_batch1_r5_result.json` | `results/_v/_v4_supp_l14v3_batch1_r5_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 186 | `_v4_supp_l14v3_batch1_r6_executor.py` | `results/_v/_v4_supp_l14v3_batch1_r6_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 187 | `_v4_supp_l14v3_batch1_r6_result.json` | `results/_v/_v4_supp_l14v3_batch1_r6_result.json` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 188 | `_v4_supp_l14v3_batch1_result.json` | `results/_v/_v4_supp_l14v3_batch1_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 189 | `_v4_supp_l14v3_batch2_r1_executor.py` | `results/_v/_v4_supp_l14v3_batch2_r1_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 190 | `_v4_supp_l14v3_batch2_r1_result.json` | `results/_v/_v4_supp_l14v3_batch2_r1_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 191 | `_v4_supp_l14v3_batch2_r2_executor.py` | `results/_v/_v4_supp_l14v3_batch2_r2_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 192 | `_v4_supp_l14v3_batch2_r2_models_probe.json` | `results/_v/_v4_supp_l14v3_batch2_r2_models_probe.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 193 | `_v4_supp_l14v3_batch2_r2_result.json` | `results/_v/_v4_supp_l14v3_batch2_r2_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 194 | `_v4_supp_l14v3_batch2_r3_executor.py` | `results/_v/_v4_supp_l14v3_batch2_r3_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 195 | `_v4_supp_l14v3_batch2_r3_result.json` | `results/_v/_v4_supp_l14v3_batch2_r3_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 196 | `_v4_supp_l14v3_batch2_r4_executor.py` | `results/_v/_v4_supp_l14v3_batch2_r4_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 197 | `_v4_supp_l14v3_batch2_r4_result.json` | `results/_v/_v4_supp_l14v3_batch2_r4_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 198 | `_v4_supp_l14v3_batch2_r5_executor.py` | `results/_v/_v4_supp_l14v3_batch2_r5_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 199 | `_v4_supp_l14v3_batch2_r5_result.json` | `results/_v/_v4_supp_l14v3_batch2_r5_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 200 | `_v4_supp_l14v3_batch2_r6_result.json` | `results/_v/_v4_supp_l14v3_batch2_r6_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 201 | `_v4_supp_l14v3_batch3_r1_executor.py` | `results/_v/_v4_supp_l14v3_batch3_r1_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 202 | `_v4_supp_l14v3_batch3_r1_result.json` | `results/_v/_v4_supp_l14v3_batch3_r1_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 203 | `_v4_supp_l14v3_batch3_r2_executor.py` | `results/_v/_v4_supp_l14v3_batch3_r2_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 204 | `_v4_supp_l14v3_batch3_r2_result.json` | `results/_v/_v4_supp_l14v3_batch3_r2_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 205 | `_v4_supp_l14v3_batch3_r3_executor.py` | `results/_v/_v4_supp_l14v3_batch3_r3_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 206 | `_v4_supp_l14v3_batch3_r3_result.json` | `results/_v/_v4_supp_l14v3_batch3_r3_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 207 | `_v4_supp_l14v3_batch3_r4_executor.py` | `results/_v/_v4_supp_l14v3_batch3_r4_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 208 | `_v4_supp_l14v3_batch3_r4_result.json` | `results/_v/_v4_supp_l14v3_batch3_r4_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 209 | `_v4_supp_l14v3_batch3_r5_result.json` | `results/_v/_v4_supp_l14v3_batch3_r5_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 210 | `_v4_supp_l14v3_batch4_r1_executor.py` | `results/_v/_v4_supp_l14v3_batch4_r1_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 211 | `_v4_supp_l14v3_batch4_r1_result.json` | `results/_v/_v4_supp_l14v3_batch4_r1_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 212 | `_v4_supp_l14v3_batch4_r2_executor.py` | `results/_v/_v4_supp_l14v3_batch4_r2_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 213 | `_v4_supp_l14v3_batch4_r2_result.json` | `results/_v/_v4_supp_l14v3_batch4_r2_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 214 | `_v4_supp_l14v3_batch4_r3_executor.py` | `results/_v/_v4_supp_l14v3_batch4_r3_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 215 | `_v4_supp_l14v3_batch4_r3_result.json` | `results/_v/_v4_supp_l14v3_batch4_r3_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 216 | `_v4_supp_l14v3_batch4_r4_executor.py` | `results/_v/_v4_supp_l14v3_batch4_r4_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 217 | `_v4_supp_l14v3_batch4_r4_result.json` | `results/_v/_v4_supp_l14v3_batch4_r4_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 218 | `_v4_supp_l14v3_batch4_r5_executor.py` | `results/_v/_v4_supp_l14v3_batch4_r5_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 219 | `_v4_supp_l14v3_batch4_r5_result.json` | `results/_v/_v4_supp_l14v3_batch4_r5_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 220 | `_v4_supp_l14v3_batch4_r6_executor.py` | `results/_v/_v4_supp_l14v3_batch4_r6_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 221 | `_v4_supp_l14v3_batch4_r6_result.json` | `results/_v/_v4_supp_l14v3_batch4_r6_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 222 | `_v4_supp_l14v3_batch5_r1_executor.py` | `results/_v/_v4_supp_l14v3_batch5_r1_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 223 | `_v4_supp_l14v3_batch5_r1_result.json` | `results/_v/_v4_supp_l14v3_batch5_r1_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 224 | `_v4_supp_l14v3_batch5_r2_executor.py` | `results/_v/_v4_supp_l14v3_batch5_r2_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 225 | `_v4_supp_l14v3_batch5_r2_result.json` | `results/_v/_v4_supp_l14v3_batch5_r2_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 226 | `_v4_supp_l14v3_batch5_r3_executor.py` | `results/_v/_v4_supp_l14v3_batch5_r3_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 227 | `_v4_supp_l14v3_batch5_r3_result.json` | `results/_v/_v4_supp_l14v3_batch5_r3_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 228 | `_v4_supp_l14v3_batch5_r4_executor.py` | `results/_v/_v4_supp_l14v3_batch5_r4_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 229 | `_v4_supp_l14v3_batch5_r4_result.json` | `results/_v/_v4_supp_l14v3_batch5_r4_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 230 | `_v4_supp_l14v3_batch5_r5_executor.py` | `results/_v/_v4_supp_l14v3_batch5_r5_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 231 | `_v4_supp_l14v3_batch5_r5_result.json` | `results/_v/_v4_supp_l14v3_batch5_r5_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 232 | `_v4_supp_l14v3_batch6_r1_executor.py` | `results/_v/_v4_supp_l14v3_batch6_r1_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 233 | `_v4_supp_l14v3_batch6_r1_result.json` | `results/_v/_v4_supp_l14v3_batch6_r1_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 234 | `_v4_supp_l14v3_batch6_r2_executor.py` | `results/_v/_v4_supp_l14v3_batch6_r2_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 235 | `_v4_supp_l14v3_batch6_r2_result.json` | `results/_v/_v4_supp_l14v3_batch6_r2_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 236 | `_v4_supp_l14v3_batch6_r3_executor.py` | `results/_v/_v4_supp_l14v3_batch6_r3_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 237 | `_v4_supp_l14v3_batch6_r3_result.json` | `results/_v/_v4_supp_l14v3_batch6_r3_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 238 | `_v4_supp_l14v3_batch6_r4_executor.py` | `results/_v/_v4_supp_l14v3_batch6_r4_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 239 | `_v4_supp_l14v3_batch6_r4_result.json` | `results/_v/_v4_supp_l14v3_batch6_r4_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 240 | `_v4_supp_l14v3_batch6_r5_executor.py` | `results/_v/_v4_supp_l14v3_batch6_r5_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 241 | `_v4_supp_l14v3_batch6_r5_result.json` | `results/_v/_v4_supp_l14v3_batch6_r5_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 242 | `_v4_supp_l14v3_batch7_r1_executor.py` | `results/_v/_v4_supp_l14v3_batch7_r1_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 243 | `_v4_supp_l14v3_batch7_r1_result.json` | `results/_v/_v4_supp_l14v3_batch7_r1_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 244 | `_v4_supp_l14v3_batch7_r2_executor.py` | `results/_v/_v4_supp_l14v3_batch7_r2_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 245 | `_v4_supp_l14v3_batch7_r2_result.json` | `results/_v/_v4_supp_l14v3_batch7_r2_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 246 | `_v4_supp_l14v3_batch7_r3_executor.py` | `results/_v/_v4_supp_l14v3_batch7_r3_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 247 | `_v4_supp_l14v3_batch7_r3_result.json` | `results/_v/_v4_supp_l14v3_batch7_r3_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 248 | `_v4_supp_l14v3_batch7_r4_executor.py` | `results/_v/_v4_supp_l14v3_batch7_r4_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 249 | `_v4_supp_l14v3_batch7_r4_result.json` | `results/_v/_v4_supp_l14v3_batch7_r4_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 250 | `_v4_supp_l14v3_batch7_r5_result.json` | `results/_v/_v4_supp_l14v3_batch7_r5_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 251 | `_v4_supp_l14v3_batch8_r1_executor.py` | `results/_v/_v4_supp_l14v3_batch8_r1_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 252 | `_v4_supp_l14v3_batch8_r1_result.json` | `results/_v/_v4_supp_l14v3_batch8_r1_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 253 | `_v4_supp_l14v3_batch8_r2_executor.py` | `results/_v/_v4_supp_l14v3_batch8_r2_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 254 | `_v4_supp_l14v3_batch8_r2_result.json` | `results/_v/_v4_supp_l14v3_batch8_r2_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 255 | `_v4_supp_l14v3_batch8_r3_executor.py` | `results/_v/_v4_supp_l14v3_batch8_r3_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 256 | `_v4_supp_l14v3_batch8_r3_result.json` | `results/_v/_v4_supp_l14v3_batch8_r3_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 257 | `_v4_supp_l14v3_batch8_r4_executor.py` | `results/_v/_v4_supp_l14v3_batch8_r4_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 258 | `_v4_supp_l14v3_batch8_r4_result.json` | `results/_v/_v4_supp_l14v3_batch8_r4_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 259 | `_v4_supp_l14v3_batch8_r5_executor.py` | `results/_v/_v4_supp_l14v3_batch8_r5_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 260 | `_v4_supp_l14v3_batch8_r5_result.json` | `results/_v/_v4_supp_l14v3_batch8_r5_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 261 | `_v4_supp_l14v3_batch9_r1_executor.py` | `results/_v/_v4_supp_l14v3_batch9_r1_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 262 | `_v4_supp_l14v3_batch9_r1_result.json` | `results/_v/_v4_supp_l14v3_batch9_r1_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 263 | `_v4_supp_l14v3_batch9_r2_executor.py` | `results/_v/_v4_supp_l14v3_batch9_r2_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 264 | `_v4_supp_l14v3_batch9_r2_result.json` | `results/_v/_v4_supp_l14v3_batch9_r2_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 265 | `_v4_supp_l14v3_batch9_r3_executor.py` | `results/_v/_v4_supp_l14v3_batch9_r3_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 266 | `_v4_supp_l14v3_batch9_r3_result.json` | `results/_v/_v4_supp_l14v3_batch9_r3_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 267 | `_v4_supp_l14v3_batch9_r4_executor.py` | `results/_v/_v4_supp_l14v3_batch9_r4_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 268 | `_v4_supp_l14v3_batch9_r4_result.json` | `results/_v/_v4_supp_l14v3_batch9_r4_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 269 | `_v4_supp_l14v3_batch9_r5_result.json` | `results/_v/_v4_supp_l14v3_batch9_r5_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 270 | `_v4_supp_l14v3_model_mapping_2026_09_24.md` | `results/_v/_v4_supp_l14v3_model_mapping_2026_09_24.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 271 | `_v4_supp_l14v3_n26_verdict.md` | `results/_v/_v4_supp_l14v3_n26_verdict.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 272 | `_v4_supp_prereg_v02_add_L14V3_2026_09_24.md` | `results/_v/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 273 | `_v4_supp_prereg_v02_add_T15_2026_09_24.md` | `results/_v/_v4_supp_prereg_v02_add_T15_2026_09_24.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 274 | `_v4_supp_prereg_v02_add_T15r2_2026_09_26.md` | `results/_v/_v4_supp_prereg_v02_add_T15r2_2026_09_26.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 275 | `_v4_supp_prereg_v02_add_T15r2_activation_2026_09_26.md` | `results/_v/_v4_supp_prereg_v02_add_T15r2_activation_2026_09_26.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 276 | `_v4_supp_prereg_v02_add_T1_2026_09_24.md` | `results/_v/_v4_supp_prereg_v02_add_T1_2026_09_24.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 277 | `_v4_supp_t15_executor.py` | `results/_v/_v4_supp_t15_executor.py` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 278 | `_v4_supp_t15_executor_r0_atomic_2026_09_29.py` | `results/_v/_v4_supp_t15_executor_r0_atomic_2026_09_29.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 279 | `_v4_supp_t15_executor_r1_2026_09_27.py` | `results/_v/_v4_supp_t15_executor_r1_2026_09_27.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 280 | `_v4_supp_t15_executor_r2_atomic_2026_09_28.py` | `results/_v/_v4_supp_t15_executor_r2_atomic_2026_09_28.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 281 | `_v4_supp_t15_executor_r3_2026_09_28.py` | `results/_v/_v4_supp_t15_executor_r3_2026_09_28.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 282 | `_v4_supp_t15_result.json` | `results/_v/_v4_supp_t15_result.json` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 283 | `_v4_supp_t15_verdict.md` | `results/_v/_v4_supp_t15_verdict.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 284 | `_v4_supp_t15r2_executor.py` | `results/_v/_v4_supp_t15r2_executor.py` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 285 | `_v4_supp_t15r2_executor_r0_atomic_2026_09_29.py` | `results/_v/_v4_supp_t15r2_executor_r0_atomic_2026_09_29.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 286 | `_v4_supp_t15r2_executor_r1_2026_09_28.py` | `results/_v/_v4_supp_t15r2_executor_r1_2026_09_28.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 287 | `_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py` | `results/_v/_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 288 | `_v4_supp_t15r2_executor_r3_2026_09_28.py` | `results/_v/_v4_supp_t15r2_executor_r3_2026_09_28.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 289 | `_v4_supp_t15r2_result.json` | `results/_v/_v4_supp_t15r2_result.json` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 290 | `_v4_supp_t15r2_verdict.md` | `results/_v/_v4_supp_t15r2_verdict.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 291 | `_v4_supp_t1_executor.py` | `results/_v/_v4_supp_t1_executor.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 292 | `_v4_supp_t1_result.json` | `results/_v/_v4_supp_t1_result.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 293 | `_v4_supp_t1_verdict.md` | `results/_v/_v4_supp_t1_verdict.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 294 | `_v4_track2_multimodel_rerun.py` | `results/_v/_v4_track2_multimodel_rerun.py` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 295 | `_v4_track2_multimodel_rerun_2026_09_23.json` | `results/_v/_v4_track2_multimodel_rerun_2026_09_23.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 296 | `_v4_track2_multimodel_verdict_2026_09_23.md` | `results/_v/_v4_track2_multimodel_verdict_2026_09_23.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 297 | `_v5_b15_pp1_impl_fix_2026_09_29.md` | `results/_v/_v5_b15_pp1_impl_fix_2026_09_29.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 298 | `_v5_bulk_activation_2026_09_28.md` | `results/_v/_v5_bulk_activation_2026_09_28.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 299 | `_v5_c3_reading_b_prereg_2026_09_28.md` | `results/_v/_v5_c3_reading_b_prereg_2026_09_28.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 300 | `_v5_checkpoint_tail3_revision_2026_09_29.md` | `results/_v/_v5_checkpoint_tail3_revision_2026_09_29.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 301 | `_v5_clearance_mr14_rerun_note_2026_09_29.md` | `results/_v/_v5_clearance_mr14_rerun_note_2026_09_29.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 302 | `_v5_closing_register_2026_09_28.md` | `results/_v/_v5_closing_register_2026_09_28.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 303 | `_v5_confirm_b11_decisions_register_2026_09_29.md` | `results/_v/_v5_confirm_b11_decisions_register_2026_09_29.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 304 | `_v5_confirm_b14_b15_decisions_register_2026_09_29.md` | `results/_v/_v5_confirm_b14_b15_decisions_register_2026_09_29.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 305 | `_v5_confirm_b5_decisions_register_2026_09_29.md` | `results/_v/_v5_confirm_b5_decisions_register_2026_09_29.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 306 | `_v5_confirm_b7_decisions_register_2026_09_29.md` | `results/_v/_v5_confirm_b7_decisions_register_2026_09_29.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 307 | `_v5_confirm_b9_decisions_register_2026_09_29.md` | `results/_v/_v5_confirm_b9_decisions_register_2026_09_29.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 308 | `_v5_exec_f2_r3_register_2026_09_29.md` | `results/_v/_v5_exec_f2_r3_register_2026_09_29.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 309 | `_v5_fake_verdict_session_log_2026_09_28.md` | `results/_v/_v5_fake_verdict_session_log_2026_09_28.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 310 | `_v5_fake_verdict_v1x_prereg_2026_09_28.md` | `results/_v/_v5_fake_verdict_v1x_prereg_2026_09_28.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 311 | `_v5_gt4_reattrib_2026_09_29.json` | `results/_v/_v5_gt4_reattrib_2026_09_29.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 312 | `_v5_gt5_gt6_gt8_gt5b_gt_prereg_2026_09_28.md` | `results/_v/_v5_gt5_gt6_gt8_gt5b_gt_prereg_2026_09_28.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 313 | `_v5_gt5_reattrib_2026_09_29.json` | `results/_v/_v5_gt5_reattrib_2026_09_29.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 314 | `_v5_gt5b_reattrib_2026_09_29.json` | `results/_v/_v5_gt5b_reattrib_2026_09_29.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 315 | `_v5_gt6_trajint_2026_09_29.json` | `results/_v/_v5_gt6_trajint_2026_09_29.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 316 | `_v5_gt8_expand_2026_09_29.json` | `results/_v/_v5_gt8_expand_2026_09_29.json` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 317 | `_v5_gt8_lowarm_exec_2026_09_29.md` | `results/_v/_v5_gt8_lowarm_exec_2026_09_29.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 318 | `_v5_gt8_lowarm_result_2026_09_29.json` | `results/_v/_v5_gt8_lowarm_result_2026_09_29.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 319 | `_v5_gt8_lowarm_resultb_2026_09_29.json` | `results/_v/_v5_gt8_lowarm_resultb_2026_09_29.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 320 | `_v5_gt8_lowarm_seta_verify_2026_09_29.json` | `results/_v/_v5_gt8_lowarm_seta_verify_2026_09_29.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 321 | `_v5_gt_exec_2026_09_29.md` | `results/_v/_v5_gt_exec_2026_09_29.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 322 | `_v5_gt_p10_lowarm_prereg_2026_09_29.md` | `results/_v/_v5_gt_p10_lowarm_prereg_2026_09_29.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 323 | `_v5_gt_verdict_2026_09_29.md` | `results/_v/_v5_gt_verdict_2026_09_29.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 324 | `_v5_handover_guide_project_initiation_2026_10_12.md` | `results/_v/_v5_handover_guide_project_initiation_2026_10_12.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 325 | `_v5_item21_anchor_recompute_2026_09_28.json` | `results/_v/_v5_item21_anchor_recompute_2026_09_28.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 326 | `_v5_item21_anchor_recompute_2026_09_28.md` | `results/_v/_v5_item21_anchor_recompute_2026_09_28.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 327 | `_v5_item21_patched_recompute_2026_09_28.json` | `results/_v/_v5_item21_patched_recompute_2026_09_28.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 328 | `_v5_item21_strategyqa_realias_recompute_2026_09_29.json` | `results/_v/_v5_item21_strategyqa_realias_recompute_2026_09_29.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 329 | `_v5_item26b_attribution_effective_2026_09_28.md` | `results/_v/_v5_item26b_attribution_effective_2026_09_28.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 330 | `_v5_item26b_endpoint_definition_prereg_2026_09_28.md` | `results/_v/_v5_item26b_endpoint_definition_prereg_2026_09_28.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 331 | `_v5_item26b_literal_gap_prereg_v2_2026_09_28.md` | `results/_v/_v5_item26b_literal_gap_prereg_v2_2026_09_28.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 332 | `_v5_item35_prereg_v2_2026_09_28.md` | `results/_v/_v5_item35_prereg_v2_2026_09_28.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 333 | `_v5_item35_v2_matrix_exec_2026_09_29.md` | `results/_v/_v5_item35_v2_matrix_exec_2026_09_29.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 334 | `_v5_item35_v2_matrix_result_2026_09_29.json` | `results/_v/_v5_item35_v2_matrix_result_2026_09_29.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 335 | `_v5_item35_v2_verdict_2026_09_29.md` | `results/_v/_v5_item35_v2_verdict_2026_09_29.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 336 | `_v5_item35_v3_collinear_prereg_2026_09_29.md` | `results/_v/_v5_item35_v3_collinear_prereg_2026_09_29.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 337 | `_v5_item35_v3_collinear_recompute_2026_10_01.json` | `results/_v/_v5_item35_v3_collinear_recompute_2026_10_01.json` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 338 | `_v5_item35_v3_collinear_result_2026_09_29.json` | `results/_v/_v5_item35_v3_collinear_result_2026_09_29.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 339 | `_v5_pjpm_pc_closeout_readout_2026_09_29.md` | `results/_v/_v5_pjpm_pc_closeout_readout_2026_09_29.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 340 | `_v5_pjpm_pc_deg_prereg_2026_09_29.md` | `results/_v/_v5_pjpm_pc_deg_prereg_2026_09_29.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 341 | `_v5_pjpm_pc_degen_precheck_result_2026_09_29.json` | `results/_v/_v5_pjpm_pc_degen_precheck_result_2026_09_29.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 342 | `_v5_r2h2_residual_merged_catalogue_2026_09_29.md` | `results/_v/_v5_r2h2_residual_merged_catalogue_2026_09_29.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 343 | `_v5_sub_artifact_ledger_2026_09_28.md` | `results/_v/_v5_sub_artifact_ledger_2026_09_28.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 344 | `_v5_theory_input_acquisition_request_2026_09_29.md` | `results/_v/_v5_theory_input_acquisition_request_2026_09_29.md` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 345 | `_v5_track2_qwen_retry_2026_09_29.json` | `results/_v/_v5_track2_qwen_retry_2026_09_29.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 346 | `_v5_trae_doubt6_verify_2026_09_28_r3verifier.md` | `results/_v/_v5_trae_doubt6_verify_2026_09_28_r3verifier.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 347 | `_v5_v3_deg_c5_b_raw_embeddings_2026_09_29.json` | `results/_v/_v5_v3_deg_c5_b_raw_embeddings_2026_09_29.json` | _v* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 348 | `_v5_v3_deg_c5_proposal_2026_09_29.md` | `results/_v/_v5_v3_deg_c5_proposal_2026_09_29.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 349 | `_v5_v3_deg_fix_c1c4_result_2026_09_29.json` | `results/_v/_v5_v3_deg_fix_c1c4_result_2026_09_29.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 350 | `_v5_v3_deg_fix_exec_2026_09_29.md` | `results/_v/_v5_v3_deg_fix_exec_2026_09_29.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 351 | `_v5_v3_deg_fix_prereg_2026_09_29.md` | `results/_v/_v5_v3_deg_fix_prereg_2026_09_29.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 352 | `_v5_v3_deg_p1_reopen_result_2026_09_29.json` | `results/_v/_v5_v3_deg_p1_reopen_result_2026_09_29.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 353 | `_v5_v3_deg_reopen_line_2026_09_29.md` | `results/_v/_v5_v3_deg_reopen_line_2026_09_29.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 354 | `_v5r_s40_recompute_2026_09_29.json` | `results/_v/_v5r_s40_recompute_2026_09_29.json` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 355 | `_value_card_template_7col_2026_10_13.md` | `results/_v/_value_card_template_7col_2026_10_13.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 356 | `_voided_files_reference_update_2026_10_14.md` | `results/_v/_voided_files_reference_update_2026_10_14.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 357 | `_voided_files_relocation_register_2026_10_14.md` | `results/_v/_voided_files_relocation_register_2026_10_14.md` | _v* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |

### §2-2 族 `_kd*` — 62 条

| # | 旧路径 | 拟新路径 | 族 | 引用面 | 档2 关联判死线 |
| :-- |--: |--: |--: |--: |--: |
| 358 | `_kd04_c_denominator_expansion_readings_2026_10_10.json` | `results/_kd/_kd04_c_denominator_expansion_readings_2026_10_10.json` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 359 | `_kd04_c_denominator_killline_prereg_2026_10_10.md` | `results/_kd/_kd04_c_denominator_killline_prereg_2026_10_10.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 360 | `_kd13_ecr_anchor_binding_deliberation_2026_10_15.md` | `results/_kd/_kd13_ecr_anchor_binding_deliberation_2026_10_15.md` | _kd* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 361 | `_kd14_null_u_carrier_deliberation_2026_10_16.md` | `results/_kd/_kd14_null_u_carrier_deliberation_2026_10_16.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 362 | `_kd14_null_u_carrier_effect_register_2026_10_16.md` | `results/_kd/_kd14_null_u_carrier_effect_register_2026_10_16.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 363 | `_kd1_preexp_contrast_2026_10_17.md` | `results/_kd/_kd1_preexp_contrast_2026_10_17.md` | _kd* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 364 | `_kd4_adoption_and_caliber_pack_effect_2026_10_17.md` | `results/_kd/_kd4_adoption_and_caliber_pack_effect_2026_10_17.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 365 | `_kd4_homology_verdict_2026_10_17.md` | `results/_kd/_kd4_homology_verdict_2026_10_17.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 366 | `_kd_11_12_resolution_register_2026_10_16.md` | `results/_kd/_kd_11_12_resolution_register_2026_10_16.md` | _kd* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 367 | `_kd_13_9_3_closure_register_2026_10_16.md` | `results/_kd/_kd_13_9_3_closure_register_2026_10_16.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 368 | `_kd_2_4_6_caliber_note_2026_10_16.md` | `results/_kd/_kd_2_4_6_caliber_note_2026_10_16.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 369 | `_kd_civ_closure_effect_2026_10_18.md` | `results/_kd/_kd_civ_closure_effect_2026_10_18.md` | _kd* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 370 | `_kd_civ_closure_verdict_2026_10_18.md` | `results/_kd/_kd_civ_closure_verdict_2026_10_18.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 371 | `_kd_cluster_verdict_pack_adjudication_2026_10_19.md` | `results/_kd/_kd_cluster_verdict_pack_adjudication_2026_10_19.md` | _kd* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 372 | `_kd_crw2_beta_and_t4n05_domain_adjudication_2026_10_20.md` | `results/_kd/_kd_crw2_beta_and_t4n05_domain_adjudication_2026_10_20.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 373 | `_kd_epw3_crw3_ffrep1_adjudication_2026_10_19.md` | `results/_kd/_kd_epw3_crw3_ffrep1_adjudication_2026_10_19.md` | _kd* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 374 | `_kd_eta_main_run_verdict_2026_10_20.md` | `results/_kd/_kd_eta_main_run_verdict_2026_10_20.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 375 | `_kd_eta_selection_verdict_2026_10_20.md` | `results/_kd/_kd_eta_selection_verdict_2026_10_20.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 376 | `_kd_eta_sep_measurement_verdict_2026_10_20.md` | `results/_kd/_kd_eta_sep_measurement_verdict_2026_10_20.md` | _kd* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 377 | `_kd_false9_remedy_proposals_2026_10_20.md` | `results/_kd/_kd_false9_remedy_proposals_2026_10_20.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 378 | `_kd_false9_wave0_calibers_2026_10_20.md` | `results/_kd/_kd_false9_wave0_calibers_2026_10_20.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 379 | `_kd_family_census_2026_10_20.md` | `results/_kd/_kd_family_census_2026_10_20.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 380 | `_kd_flip_census_2026_10_17.md` | `results/_kd/_kd_flip_census_2026_10_17.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 381 | `_kd_gap_resolution_rulings_effect_2026_10_17.md` | `results/_kd/_kd_gap_resolution_rulings_effect_2026_10_17.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 382 | `_kd_gap_survey_2026_10_17.md` | `results/_kd/_kd_gap_survey_2026_10_17.md` | _kd* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 383 | `_kd_ge01_eps4_scope_escalation_note_2026_10_16.md` | `results/_kd/_kd_ge01_eps4_scope_escalation_note_2026_10_16.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 384 | `_kd_h1_h7_disposition_draft_2026_10_20.md` | `results/_kd/_kd_h1_h7_disposition_draft_2026_10_20.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 385 | `_kd_h1_h7_hidden_gaps_register_2026_10_19.md` | `results/_kd/_kd_h1_h7_hidden_gaps_register_2026_10_19.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 386 | `_kd_h1_lineage_declaration_2026_10_20.md` | `results/_kd/_kd_h1_lineage_declaration_2026_10_20.md` | _kd* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 387 | `_kd_h2_anchor_chain_erratum_2026_10_20.md` | `results/_kd/_kd_h2_anchor_chain_erratum_2026_10_20.md` | _kd* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 388 | `_kd_h4_fingerprint_reanchor_register_2026_10_20.md` | `results/_kd/_kd_h4_fingerprint_reanchor_register_2026_10_20.md` | _kd* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 389 | `_kd_h5_background_tasks_full_scan_2026_10_20.md` | `results/_kd/_kd_h5_background_tasks_full_scan_2026_10_20.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 390 | `_kd_h5_background_tasks_full_scan_data_2026_10_20.json` | `results/_kd/_kd_h5_background_tasks_full_scan_data_2026_10_20.json` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 391 | `_kd_h5_h6_recheck_2026_10_14.md` | `results/_kd/_kd_h5_h6_recheck_2026_10_14.md` | _kd* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 392 | `_kd_h5_session_history_domain_caliber_2026_10_20.md` | `results/_kd/_kd_h5_session_history_domain_caliber_2026_10_20.md` | _kd* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 393 | `_kd_h5_session_history_pilot_1of10_2026_10_20.md` | `results/_kd/_kd_h5_session_history_pilot_1of10_2026_10_20.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 394 | `_kd_h6_caliber_mapping_adjudication_2026_10_20.md` | `results/_kd/_kd_h6_caliber_mapping_adjudication_2026_10_20.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 395 | `_kd_history_pack_adjudication_2026_10_19.md` | `results/_kd/_kd_history_pack_adjudication_2026_10_19.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 396 | `_kd_identified_defect_attribution_caliber_2026_10_20.md` | `results/_kd/_kd_identified_defect_attribution_caliber_2026_10_20.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 397 | `_kd_mda8_arm2_kill_line_freeze_draft_2026_10_19.md` | `results/_kd/_kd_mda8_arm2_kill_line_freeze_draft_2026_10_19.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 398 | `_kd_mda8_arm2_remaining11_recommendation_2026_10_19.md` | `results/_kd/_kd_mda8_arm2_remaining11_recommendation_2026_10_19.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 399 | `_kd_mda8_domain_readings_adjudication_2026_10_19.md` | `results/_kd/_kd_mda8_domain_readings_adjudication_2026_10_19.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 400 | `_kd_mda8_f1_two_senses_adjudication_2026_10_19.md` | `results/_kd/_kd_mda8_f1_two_senses_adjudication_2026_10_19.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 401 | `_kd_mda8_first_reading_verdict_2026_10_20.md` | `results/_kd/_kd_mda8_first_reading_verdict_2026_10_20.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 402 | `_kd_mda8_gate_resolution_and_new_exp_draft_2026_10_19.md` | `results/_kd/_kd_mda8_gate_resolution_and_new_exp_draft_2026_10_19.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 403 | `_kd_mda8_preexp_dispatch_spec_draft_2026_10_19.md` | `results/_kd/_kd_mda8_preexp_dispatch_spec_draft_2026_10_19.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 404 | `_kd_mda8_spec_rest_recommendation_2026_10_19.md` | `results/_kd/_kd_mda8_spec_rest_recommendation_2026_10_19.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 405 | `_kd_mda8a24_clearance_verdict_2026_10_20.md` | `results/_kd/_kd_mda8a24_clearance_verdict_2026_10_20.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 406 | `_kd_s3_2_3_corrigendum_2026_10_16.md` | `results/_kd/_kd_s3_2_3_corrigendum_2026_10_16.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 407 | `_kd_s3b1_kd1_n7_rulings_effect_2026_10_17.md` | `results/_kd/_kd_s3b1_kd1_n7_rulings_effect_2026_10_17.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 408 | `_kd_s3b1_verdict_2026_10_17.md` | `results/_kd/_kd_s3b1_verdict_2026_10_17.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 409 | `_kd_s3b5_kd1_esc36_batch_lock_effect_2026_10_17.md` | `results/_kd/_kd_s3b5_kd1_esc36_batch_lock_effect_2026_10_17.md` | _kd* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 410 | `_kd_sepcal7_final_verdict_2026_10_20.md` | `results/_kd/_kd_sepcal7_final_verdict_2026_10_20.md` | _kd* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 411 | `_kd_two_gates_comparison_2026_10_20.md` | `results/_kd/_kd_two_gates_comparison_2026_10_20.md` | _kd* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 412 | `_kd_u1_u4_rulings_effect_2026_10_17.md` | `results/_kd/_kd_u1_u4_rulings_effect_2026_10_17.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 413 | `_kd_u5_u6_s3b4_rulings_effect_2026_10_17.md` | `results/_kd/_kd_u5_u6_s3b4_rulings_effect_2026_10_17.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 414 | `_kd_u6_readside_rewire_validation_2026_10_17.md` | `results/_kd/_kd_u6_readside_rewire_validation_2026_10_17.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 415 | `_kd_unambiguous_meaning_ruling_2026_10_10.md` | `results/_kd/_kd_unambiguous_meaning_ruling_2026_10_10.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 416 | `_kd_writing_convention_guidance_2026_10_09.md` | `results/_kd/_kd_writing_convention_guidance_2026_10_09.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 417 | `_kdb2r2_kd14_merge_governance_2026_10_17.md` | `results/_kd/_kdb2r2_kd14_merge_governance_2026_10_17.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 418 | `_kdb2r3_u13_rulings_effect_2026_10_17.md` | `results/_kd/_kdb2r3_u13_rulings_effect_2026_10_17.md` | _kd* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 419 | `_kdk45_remeasure_2026_10_17.md` | `results/_kd/_kdk45_remeasure_2026_10_17.md` | _kd* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |

### §2-3 族 `deposon_*` — 97 条

| # | 旧路径 | 拟新路径 | 族 | 引用面 | 档2 关联判死线 |
| :-- |--: |--: |--: |--: |--: |
| 420 | `deposon_benchmark_v1_3_details.json` | `results/deposon_/deposon_benchmark_v1_3_details.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 421 | `deposon_benchmark_v1_3_simple.json` | `results/deposon_/deposon_benchmark_v1_3_simple.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 422 | `deposon_benchmark_v1_3_traps.json` | `results/deposon_/deposon_benchmark_v1_3_traps.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 423 | `deposon_benchmark_v1_4_gsm8k.json` | `results/deposon_/deposon_benchmark_v1_4_gsm8k.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 424 | `deposon_benchmark_v1_4_gsm8k_details.json` | `results/deposon_/deposon_benchmark_v1_4_gsm8k_details.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 425 | `deposon_benchmark_v1_4_strategyqa.json` | `results/deposon_/deposon_benchmark_v1_4_strategyqa.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 426 | `deposon_benchmark_v1_4_strategyqa_details.json` | `results/deposon_/deposon_benchmark_v1_4_strategyqa_details.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 427 | `deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json` | `results/deposon_/deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 428 | `deposon_cpath_simulation_2026_09_10.json` | `results/deposon_/deposon_cpath_simulation_2026_09_10.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 429 | `deposon_d_fix2_metric_verify_9m60c_2026_09_15.json` | `results/deposon_/deposon_d_fix2_metric_verify_9m60c_2026_09_15.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 430 | `deposon_deepseek_v41_flash_30cells_v3_2026_09_10.json` | `results/deposon_/deposon_deepseek_v41_flash_30cells_v3_2026_09_10.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 431 | `deposon_dpath_cross_modal_2026_09_10.json` | `results/deposon_/deposon_dpath_cross_modal_2026_09_10.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 432 | `deposon_dpath_cross_modal_runner_2026_09_10.py` | `results/deposon_/deposon_dpath_cross_modal_runner_2026_09_10.py` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 433 | `deposon_feshbach_rag_30cells_2026_09_10.py` | `results/deposon_/deposon_feshbach_rag_30cells_2026_09_10.py` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 434 | `deposon_g1_mindmap_demo.json` | `results/deposon_/deposon_g1_mindmap_demo.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 435 | `deposon_g2_boltzmann_pathintegral.json` | `results/deposon_/deposon_g2_boltzmann_pathintegral.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 436 | `deposon_g2_boltzmann_pathintegral_rewrite.json` | `results/deposon_/deposon_g2_boltzmann_pathintegral_rewrite.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 437 | `deposon_game_theory_eval_2026_09_10.json` | `results/deposon_/deposon_game_theory_eval_2026_09_10.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 438 | `deposon_gpt6_teamorouter_2026_09_10.json` | `results/deposon_/deposon_gpt6_teamorouter_2026_09_10.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 439 | `deposon_gpt6_teamorouter_30cells_2026_09_10.json` | `results/deposon_/deposon_gpt6_teamorouter_30cells_2026_09_10.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 440 | `deposon_gsm8k_stratified.json` | `results/deposon_/deposon_gsm8k_stratified.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 441 | `deposon_openrouter_5model_rag_30cells_2026_09_10.json` | `results/deposon_/deposon_openrouter_5model_rag_30cells_2026_09_10.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 442 | `deposon_p_d_b3_merkle_22_caption_2026_09_16.json` | `results/deposon_/deposon_p_d_b3_merkle_22_caption_2026_09_16.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 443 | `deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` | `results/deposon_/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 444 | `deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json` | `results/deposon_/deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 445 | `deposon_p_k_cross_subject_fingerprint_blind_test_2026_09_16.json` | `results/deposon_/deposon_p_k_cross_subject_fingerprint_blind_test_2026_09_16.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 446 | `deposon_pa_d1_d3_2026_09_15.json` | `results/deposon_/deposon_pa_d1_d3_2026_09_15.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 447 | `deposon_pc_d1_d3_2026_09_15.json` | `results/deposon_/deposon_pc_d1_d3_2026_09_15.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 448 | `deposon_pe_d1_d3_2026_09_15.json` | `results/deposon_/deposon_pe_d1_d3_2026_09_15.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 449 | `deposon_pf_d1_full_9m5c_2026_09_15.json` | `results/deposon_/deposon_pf_d1_full_9m5c_2026_09_15.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 450 | `deposon_pf_implementation_2026_09_11.json` | `results/deposon_/deposon_pf_implementation_2026_09_11.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 451 | `deposon_pg_v01_9m60c_2026_09_15.json` | `results/deposon_/deposon_pg_v01_9m60c_2026_09_15.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 452 | `deposon_risk1_02940_decision_2026_09_11.json` | `results/deposon_/deposon_risk1_02940_decision_2026_09_11.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 453 | `deposon_risk2_canonical5_decision_2026_09_11.json` | `results/deposon_/deposon_risk2_canonical5_decision_2026_09_11.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 454 | `deposon_risk3_seff_decision_2026_09_11.json` | `results/deposon_/deposon_risk3_seff_decision_2026_09_11.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 455 | `deposon_v15_diffusion.json` | `results/deposon_/deposon_v15_diffusion.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 456 | `deposon_v15_diffusion_maxpath_negativeresult.json` | `results/deposon_/deposon_v15_diffusion_maxpath_negativeresult.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 457 | `deposon_v15_diffusion_summary.json` | `results/deposon_/deposon_v15_diffusion_summary.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 458 | `deposon_v16_llm_prior.json` | `results/deposon_/deposon_v16_llm_prior.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 459 | `deposon_v16_paired_stats.json` | `results/deposon_/deposon_v16_paired_stats.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 460 | `deposon_v17_fixed_sampler.json` | `results/deposon_/deposon_v17_fixed_sampler.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 461 | `deposon_v17_fusion_fix.json` | `results/deposon_/deposon_v17_fusion_fix.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 462 | `deposon_v17_fusion_fix_tieartifact_negativeresult.json` | `results/deposon_/deposon_v17_fusion_fix_tieartifact_negativeresult.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 463 | `deposon_v17_multigraph.json` | `results/deposon_/deposon_v17_multigraph.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 464 | `deposon_v18_api_supplements.json` | `results/deposon_/deposon_v18_api_supplements.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 465 | `deposon_v19_benchmark_fixes.json` | `results/deposon_/deposon_v19_benchmark_fixes.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 466 | `deposon_v19_fullrank.json` | `results/deposon_/deposon_v19_fullrank.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 467 | `deposon_v19_meanfield.json` | `results/deposon_/deposon_v19_meanfield.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 468 | `deposon_v19_quickwins.json` | `results/deposon_/deposon_v19_quickwins.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 469 | `deposon_v1_implementation_calculator_2026_09_10.py` | `results/deposon_/deposon_v1_implementation_calculator_2026_09_10.py` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 470 | `deposon_v20_baselines.json` | `results/deposon_/deposon_v20_baselines.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 471 | `deposon_v20_bigquiz_eval.json` | `results/deposon_/deposon_v20_bigquiz_eval.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 472 | `deposon_v20_corpus_eval.json` | `results/deposon_/deposon_v20_corpus_eval.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 473 | `deposon_v20_cot_quiz.json` | `results/deposon_/deposon_v20_cot_quiz.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 474 | `deposon_v20_crossval.json` | `results/deposon_/deposon_v20_crossval.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 475 | `deposon_v20_familyl_ingest.json` | `results/deposon_/deposon_v20_familyl_ingest.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 476 | `deposon_v20_fastcheck.json` | `results/deposon_/deposon_v20_fastcheck.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 477 | `deposon_v20_gt.json` | `results/deposon_/deposon_v20_gt.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 478 | `deposon_v20_gt2b.json` | `results/deposon_/deposon_v20_gt2b.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 479 | `deposon_v20_gt3.json` | `results/deposon_/deposon_v20_gt3.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 480 | `deposon_v20_gt5.json` | `results/deposon_/deposon_v20_gt5.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 481 | `deposon_v20_gt5b.json` | `results/deposon_/deposon_v20_gt5b.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 482 | `deposon_v20_gt6.json` | `results/deposon_/deposon_v20_gt6.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 483 | `deposon_v20_gt7.json` | `results/deposon_/deposon_v20_gt7.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 484 | `deposon_v20_gt8.json` | `results/deposon_/deposon_v20_gt8.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 485 | `deposon_v20_gt8b.json` | `results/deposon_/deposon_v20_gt8b.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 486 | `deposon_v20_gt8b_ingest.json` | `results/deposon_/deposon_v20_gt8b_ingest.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 487 | `deposon_v20_gt8c.json` | `results/deposon_/deposon_v20_gt8c.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 488 | `deposon_v20_gt8c_ingest.json` | `results/deposon_/deposon_v20_gt8c_ingest.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 489 | `deposon_v20_photonics.json` | `results/deposon_/deposon_v20_photonics.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 490 | `deposon_v20_quiz_eval.json` | `results/deposon_/deposon_v20_quiz_eval.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 491 | `deposon_v20_vector_audit.json` | `results/deposon_/deposon_v20_vector_audit.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 492 | `deposon_v21_gtformal.json` | `results/deposon_/deposon_v21_gtformal.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 493 | `deposon_v22_e95ci.json` | `results/deposon_/deposon_v22_e95ci.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 494 | `deposon_v22_p1c.json` | `results/deposon_/deposon_v22_p1c.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 495 | `deposon_v2_phase1_60cells_2026_09_11.json` | `results/deposon_/deposon_v2_phase1_60cells_2026_09_11.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 496 | `deposon_v2_phase3_strip_embeddings_2026_09_11.json` | `results/deposon_/deposon_v2_phase3_strip_embeddings_2026_09_11.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 497 | `deposon_v2_phase4_f4_2026_09_11.json` | `results/deposon_/deposon_v2_phase4_f4_2026_09_11.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 498 | `deposon_v3_physical_opt_2026_09_11.json` | `results/deposon_/deposon_v3_physical_opt_2026_09_11.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 499 | `deposon_v3_physical_opt_60cells_2026_09_11.json` | `results/deposon_/deposon_v3_physical_opt_60cells_2026_09_11.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 500 | `deposon_v3_v7_summary_2026_09_11.json` | `results/deposon_/deposon_v3_v7_summary_2026_09_11.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 501 | `deposon_v42_v2_miss_rate_curve_2026_09_16.json` | `results/deposon_/deposon_v42_v2_miss_rate_curve_2026_09_16.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 502 | `deposon_volcengine_22caption_embedding_2026_09_10.json` | `results/deposon_/deposon_volcengine_22caption_embedding_2026_09_10.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 503 | `deposon_volcengine_9model_30cells_2026_09_10.json` | `results/deposon_/deposon_volcengine_9model_30cells_2026_09_10.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 504 | `deposon_volcengine_glm_latest_30cells_v2_2026_09_10.json` | `results/deposon_/deposon_volcengine_glm_latest_30cells_v2_2026_09_10.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 505 | `deposon_volcengine_glm_latest_5cells_2026_09_10.json` | `results/deposon_/deposon_volcengine_glm_latest_5cells_2026_09_10.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 506 | `deposon_volcengine_glm_latest_5cells_2026_09_10.py` | `results/deposon_/deposon_volcengine_glm_latest_5cells_2026_09_10.py` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 507 | `deposon_volcengine_glm_latest_5cells_v2_2026_09_10.json` | `results/deposon_/deposon_volcengine_glm_latest_5cells_v2_2026_09_10.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 508 | `deposon_volcengine_minimax_m3_30cells_2026_09_10.json` | `results/deposon_/deposon_volcengine_minimax_m3_30cells_2026_09_10.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 509 | `deposon_volcengine_minimax_m3_30cells_2026_09_10.py` | `results/deposon_/deposon_volcengine_minimax_m3_30cells_2026_09_10.py` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 510 | `deposon_volcengine_seed_code_30cells_2026_09_10.json` | `results/deposon_/deposon_volcengine_seed_code_30cells_2026_09_10.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 511 | `deposon_volcengine_worker_a_2026_09_10.json` | `results/deposon_/deposon_volcengine_worker_a_2026_09_10.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 512 | `deposon_volcengine_worker_b_2026_09_10.json` | `results/deposon_/deposon_volcengine_worker_b_2026_09_10.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 513 | `deposon_volcengine_worker_b_2026_09_10.py` | `results/deposon_/deposon_volcengine_worker_b_2026_09_10.py` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 514 | `deposon_volcengine_worker_c_2026_09_10.json` | `results/deposon_/deposon_volcengine_worker_c_2026_09_10.json` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 515 | `deposon_volcengine_worker_c_2026_09_10.py` | `results/deposon_/deposon_volcengine_worker_c_2026_09_10.py` | deposon_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 516 | `deposon_volcengine_worker_d_2026_09_10.json` | `results/deposon_/deposon_volcengine_worker_d_2026_09_10.json` | deposon_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |

### §2-4 族 `_pi_*` — 6 条

| # | 旧路径 | 拟新路径 | 族 | 引用面 | 档2 关联判死线 |
| :-- |--: |--: |--: |--: |--: |
| 517 | `_pi_batch_rulings_and_gate1_definition_register_2026_10_12.md` | `results/_pi_/_pi_batch_rulings_and_gate1_definition_register_2026_10_12.md` | _pi_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 518 | `_pi_card_payload_extraction_2026_10_20.json` | `results/_pi_/_pi_card_payload_extraction_2026_10_20.json` | _pi_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 519 | `_pi_card_payload_extraction_2026_10_20.md` | `results/_pi_/_pi_card_payload_extraction_2026_10_20.md` | _pi_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 520 | `_pi_four_rulings_adoption_and_effectivity_2026_10_12.md` | `results/_pi_/_pi_four_rulings_adoption_and_effectivity_2026_10_12.md` | _pi_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 521 | `_pi_give_b_class_retrieval_2026_10_14.md` | `results/_pi_/_pi_give_b_class_retrieval_2026_10_14.md` | _pi_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 522 | `_pi_give_backlog_review_2026_10_14.md` | `results/_pi_/_pi_give_backlog_review_2026_10_14.md` | _pi_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |

### §2-5 族 `_root_session_history_memo*` — 2 条

| # | 旧路径 | 拟新路径 | 族 | 引用面 | 档2 关联判死线 |
| :-- |--: |--: |--: |--: |--: |
| 523 | `_root_session_history_memo_2026_10_14.md` | `_root_session_history_memo_2026_10_14.md`（**原地不动**） | _root_session_history_memo* | 仓根锚定路径引用 | **保护面 · 不移动** |
| 524 | `_root_session_history_memo_main_2026_10_14.md` | `_root_session_history_memo_main_2026_10_14.md`（**原地不动**） | _root_session_history_memo* | 仓根锚定路径引用 | **保护面 · 不移动** |

### §2-6 族 `boss_*` — 12 条

| # | 旧路径 | 拟新路径 | 族 | 引用面 | 档2 关联判死线 |
| :-- |--: |--: |--: |--: |--: |
| 525 | `boss_pa_1_rbr_rm_result_2026_09_15.json` | `results/boss_/boss_pa_1_rbr_rm_result_2026_09_15.json` | boss_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 526 | `boss_pa_2_potential_game_result_2026_09_15.json` | `results/boss_/boss_pa_2_potential_game_result_2026_09_15.json` | boss_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 527 | `boss_pa_3_replicator_dynamics_result_2026_09_15.json` | `results/boss_/boss_pa_3_replicator_dynamics_result_2026_09_15.json` | boss_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 528 | `boss_pc_1_a1_resampling_2026_09_15.json` | `results/boss_/boss_pc_1_a1_resampling_2026_09_15.json` | boss_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 529 | `boss_pc_1_real_2d_ising_2026_09_15.json` | `results/boss_/boss_pc_1_real_2d_ising_2026_09_15.json` | boss_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 530 | `boss_pc_2_a2_fitting_2026_09_15.json` | `results/boss_/boss_pc_2_a2_fitting_2026_09_15.json` | boss_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 531 | `boss_pc_2_real_transverse_ising_2026_09_15.json` | `results/boss_/boss_pc_2_real_transverse_ising_2026_09_15.json` | boss_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 532 | `boss_pc_3_a3_clipping_2026_09_15.json` | `results/boss_/boss_pc_3_a3_clipping_2026_09_15.json` | boss_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 533 | `boss_pc_3_real_reservoir_2026_09_15.json` | `results/boss_/boss_pc_3_real_reservoir_2026_09_15.json` | boss_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 534 | `boss_pe_1_real_2d_ising_2026_09_15.json` | `results/boss_/boss_pe_1_real_2d_ising_2026_09_15.json` | boss_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 535 | `boss_pe_2_real_transverse_ising_2026_09_15.json` | `results/boss_/boss_pe_2_real_transverse_ising_2026_09_15.json` | boss_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |
| 536 | `boss_pe_3_real_reservoir_2026_09_15.json` | `results/boss_/boss_pe_3_real_reservoir_2026_09_15.json` | boss_* | 相对路径引用 | `K-SPLIT-4` 已由本表条目承接（裸名／路径暴露面之映射） |

### §2-7 族 `c5_*` — 6 条

| # | 旧路径 | 拟新路径 | 族 | 引用面 | 档2 关联判死线 |
| :-- |--: |--: |--: |--: |--: |
| 537 | `c5_b_group_fix_readings_2026_10_01.json` | `results/c5_/c5_b_group_fix_readings_2026_10_01.json` | c5_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 538 | `c5_b_group_fix_readings_2026_10_09.json` | `results/c5_/c5_b_group_fix_readings_2026_10_09.json` | c5_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 539 | `c5_b_group_root_candidate_2026_10_01.md` | `results/c5_/c5_b_group_root_candidate_2026_10_01.md` | c5_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 540 | `c5_guard_0_1_recheck_verdict_2026_10_01.md` | `results/c5_/c5_guard_0_1_recheck_verdict_2026_10_01.md` | c5_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 541 | `c5_guard_minmaxstd_readings_2026_10_01.json` | `results/c5_/c5_guard_minmaxstd_readings_2026_10_01.json` | c5_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |
| 542 | `c5_guard_minmaxstd_report_2026_10_01.md` | `results/c5_/c5_guard_minmaxstd_report_2026_10_01.md` | c5_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |

### §2-8 族 `_d13*` — 1 条

| # | 旧路径 | 拟新路径 | 族 | 引用面 | 档2 关联判死线 |
| :-- |--: |--: |--: |--: |--: |
| 543 | `_d13_eta_parts_1to4_caliber_2026_10_20.md` | `results/_d13/_d13_eta_parts_1to4_caliber_2026_10_20.md` | _d13* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |

### §2-9 族 `d7_*` — 1 条

| # | 旧路径 | 拟新路径 | 族 | 引用面 | 档2 关联判死线 |
| :-- |--: |--: |--: |--: |--: |
| 544 | `d7_5anchor_60cells_9model_verdict_2026_09_18.json` | `results/d7_/d7_5anchor_60cells_9model_verdict_2026_09_18.json` | d7_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |

### §2-10 族 `ge01_*` — 1 条

| # | 旧路径 | 拟新路径 | 族 | 引用面 | 档2 关联判死线 |
| :-- |--: |--: |--: |--: |--: |
| 545 | `ge01_prereg_5anchor_landing_v1.json` | `results/ge01_/ge01_prereg_5anchor_landing_v1.json` | ge01_* | 仓根锚定路径引用 | `K-SPLIT-3` 阻断面（仓根锚定路径引用 · 映射不可补救 · 须先清代码） |

---

## §3 映射条目 · 族「无机械族界」之 771 件（拟新路径 ＝「候 PI 归族」）

**其义**：此 771 件无机械族界 ⇒ **俟 PI 归族**。本棒**不扩张族界**、**不代拟其族目录名**、**不代拟其拟新路径**。

**故本节之「拟新路径」栏一律为 `候 PI 归族`** —— 该字串**非路径**，仅为**待决标记**。

| # | 旧路径 | 拟新路径 | 族 | 引用面 | 注记 |
| :-- |--: |--: |--: |--: |--: |
| 546 | `_9model_full_merge_from_4workers_2026_10_09.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 547 | `_ablation_data_2026_10_20.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 548 | `_ablation_design_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 549 | `_ablation_reading_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 550 | `_achievements_inventory_full_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 551 | `_achievements_inventory_full_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 552 | `_af1_attribution_verdict_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 553 | `_af2_5_proof_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 554 | `_af2_proof_and_grain_scope_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 555 | `_af_complete_landing_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 556 | `_af_entity_rules_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 557 | `_af_flip要件消解_rulings_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 558 | `_af_landing_n7_and_two_cells_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 559 | `_af_rules_approval_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 560 | `_anchor_drift_authorized_adoption_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 561 | `_anchor_status_naming_note_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 562 | `_anchor_value_update_and_l261_patch_migration_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 563 | `_anti_degradation_mechanism_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 564 | `_approval_card_four_rulings_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 565 | `_archive_area_readonly_verification_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 566 | `_archive_manifest_deposon_sub_2026_09_23.json` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 567 | `_archive_manifest_non_upload_2026_09_23.json` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 568 | `_archive_whitelist_purge_exec_register_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 569 | `_archive_zone_exception_g2_extension_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 570 | `_archive_zone_exception_grant_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 571 | `_archive_zone_exception_p4_extension_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 572 | `_archive_zone_scan_violation_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 573 | `_archive_zone_write_clause_corrigendum_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 574 | `_arxiv_2609_09001_metadata_snapshot_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 575 | `_b0_sixty_items_location_list_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 576 | `_b4_alternative_deliberation_judgment_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 577 | `_b4_source_fix_and_reissue_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 578 | `_b_tier_five_subitems_draft_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 579 | `_batch10_deliberation_judgment_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 580 | `_batch11_deliberation_judgment_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 581 | `_batch1_d4_d5_b1_errata_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 582 | `_batch3_closure_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 583 | `_batch3_execution_receipt_kimi_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 584 | `_batch3_residuals_disposition_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 585 | `_batch5_deliberation_judgment_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 586 | `_batch6_deliberation_judgment_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 587 | `_batch7_deliberation_judgment_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 588 | `_batch8_deliberation_judgment_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 589 | `_batch9_deliberation_judgment_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 590 | `_batch_approval_merged_rollout_design_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 591 | `_bayesian_baseline_design_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 592 | `_bd_fixes_summary_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 593 | `_bob_commission_acceptance_and_r4_waiver_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 594 | `_bob_minimax_commission_family_intake_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 595 | `_budget_210_actual_evidence_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 596 | `_budget_720_authorized_actual_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 597 | `_c1_u5_ruling_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 598 | `_c1c4_ab_alpha_pilot_result_2026_10_09.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 599 | `_c1c4_ab_beta_pilot_result_2026_10_09.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 600 | `_c1c4_input_gap_fill_plan_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 601 | `_c4_rejection_axis_reconciliation_judgment_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 602 | `_c4_scope_ruling_and_d1_requalification_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 603 | `_c5_both_pillars_closed_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 604 | `_c5_split_into_c5a_c5b_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 605 | `_c5b_closure_verdict_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 606 | `_c7_remote_timeline_correction_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 607 | `_canonical_face_scope_corrigendum_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 608 | `_card_register_dir_verdict_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 609 | `_card_register_relocation_mapping_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 610 | `_card_register_relocation_register_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 611 | `_census_543_to_256_correction_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 612 | `_census_exit_four_rulings_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 613 | `_census_text_exec_inconsistency_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 614 | `_chd_construction_domain_declaration_draft_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 615 | `_ci_gap_fill_alt_bc_aper_prime_2026_10_09.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 616 | `_citation_corrigenda_volume_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 617 | `_citation_no_utility_caliber_draft_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 618 | `_classification_tree_anchor_erratum_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 619 | `_cleanup511_exec_register_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 620 | `_cleanup_exec_register_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 621 | `_cleanup_inventory_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 622 | `_cleanup_r2_plus83_exec_register_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 623 | `_cleanup_r2_repo_sub_exec_register_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 624 | `_clearance_evening_round_register_2026_09_29.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 625 | `_closeout_bucket_refresh_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 626 | `_closing_round_8_decisions_register_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 627 | `_closure_sweep_r2_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 628 | `_clue_book_v06_backfill_and_dual_version_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 629 | `_clue_side_dual_and_glm_commission_open_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 630 | `_cluster_a_sface_adjudication_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 631 | `_cluster_abc_pack_adoption_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 632 | `_cluster_b_carrier_adjudication_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 633 | `_cluster_c_keyface_adjudication_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 634 | `_cluster_d_counting_adjudication_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 635 | `_cluster_dfghi_pack_adoption_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 636 | `_cluster_f_deletion_adjudication_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 637 | `_cluster_g_deletion_preconditions_adjudication_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 638 | `_cluster_h_directory_adjudication_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 639 | `_cluster_i_f1_f6_f7_verdict_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 640 | `_cluster_i_f4_f5_evidence_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 641 | `_cluster_i_historical_adjudication_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 642 | `_cluster_i_item14_closure_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 643 | `_cluster_i_item14_closure_verdict_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 644 | `_cluster_i_item6_compatibility_adjudication_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 645 | `_cluster_i_item6_conditions_adjudication_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 646 | `_cluster_i_item6_give_values_adjudication_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 647 | `_cluster_j_glm_62_adjudication_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 648 | `_cluster_k_eta_blockers_adjudication_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 649 | `_cmp2_sep_threshold_s_proposal_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 650 | `_collision_196_2026_10_12.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 651 | `_collision_509_ruling_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 652 | `_collision_514_coverage_recheck_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 653 | `_collision_baseline_update_and_disposition_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 654 | `_commission_v04_approval_rulings_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 655 | `_commission_v04_ghost_reference_erratum_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 656 | `_compound_numbering_census_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 657 | `_consolidated_pending_rulings_scroll_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 658 | `_construction_change_count_ruling_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 659 | `_continued_three_rulings_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 660 | `_copilot_agent_t2_t3_reply_register_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 661 | `_copilot_eq_grok_clarification_register_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 662 | `_copilot_eq_grok_rulings_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 663 | `_copilot_reply_adoption_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 664 | `_corpus_index_citation_surface_annotation_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 665 | `_count_chain_independent_review_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 666 | `_count_value_timestamp_mandate_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 667 | `_counting_ban_release_channel_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 668 | `_coze_v1_v3_core_principle_verification_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 669 | `_coze_v5_r2_residual4_adjudication_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 670 | `_coze_v5_r2_residual4_adoption_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 671 | `_cpath_e3_sign_normalization_2026_10_01.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 672 | `_criterion_application_scope_prereg_2026_10_01.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 673 | `_d05_b_coincidence_checks_exec_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 674 | `_d05_b_coincidence_checks_exec_readings_2026_10_10.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 675 | `_d15_d16_caliber_and_authority_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 676 | `_d1_ab_deliberation_judgment_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 677 | `_d1_backfill_intake_verdict_2026_10_01.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 678 | `_d1_c_effect_register_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 679 | `_d1d2_and_guide_adoption_supplement_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 680 | `_d2_bytes_column_annotation_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 681 | `_d2_d6_erratum_and_annotation_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 682 | `_d6_l171_timeblock_restatement_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 683 | `_d8_boundary_revision_register_2026_09_30.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 684 | `_d8_collection_ledger_2026_09_30.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 685 | `_d8_supplement_open_questions_2026_09_30.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 686 | `_d9_base_reissue_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 687 | `_d9_e2e_disposition_and_f4_closure_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 688 | `_d9_e2e_rerun_for_p2_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 689 | `_d9_e2e_run_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 690 | `_d9_e2e_run_register_v2_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 691 | `_d9_h2_r1files_repair_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 692 | `_d9_independent_review_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 693 | `_d9_relpath_map_mojibake_defect_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 694 | `_d9_relpath_rewrite_map_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 695 | `_d9_relpath_rewrite_map_v2_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 696 | `_d9_residual_repair_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 697 | `_d9_rewrite_execution_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 698 | `_d9_runner_input_relpath_erratum_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 699 | `_d_dimension_canonical_coexistence_note_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 700 | `_dangling_630_adoption_and_283_corrigendum_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 701 | `_dangling_630_remediation_list_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 702 | `_degradation_reversal_guide_dual_adoption_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 703 | `_degradation_reversal_guide_kimi_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 704 | `_deliverables_verification_and_v5_handover_pending_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 705 | `_deposon_full_history_main_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 706 | `_deposon_full_history_sub_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 707 | `_desensitization_execution_plan_v04_kimi_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 708 | `_discipline_scope_review_and_harm_audit_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 709 | `_discipline_scope_review_corrigendum_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 710 | `_domain_backfill_235_401_mapping_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 711 | `_domain_backfill_401_v2_caliber_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 712 | `_domain_backfill_brush2_execution_register_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 713 | `_domain_backfill_caliber_fix_draft_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 714 | `_domain_backfill_design_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 715 | `_domain_backfill_execution_register_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 716 | `_domain_backfill_hold235_adjudication_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 717 | `_domain_backfill_hold235_retain_register_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 718 | `_domain_backfill_rulings_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 719 | `_duplicate_name_six_items_attribution_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 720 | `_erratum_3_14H_caliber_impact_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 721 | `_erratum_arm_label_transcription_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 722 | `_erratum_refonly_draft_alias_found_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 723 | `_esc3_esc6_resolution_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 724 | `_esc5_adoption_and_ritt_remeasure_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 725 | `_esc5_verdict_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 726 | `_eta_construct_c1_c16_recommendation_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 727 | `_eta_construct_face_freeze_draft_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 728 | `_eta_main_run_reading_2026_10_20.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 729 | `_eta_main_run_register_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 730 | `_eta_missing_params_and_c1_adjudication_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 731 | `_eta_missing_params_literature_evidence_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 732 | `_eta_preexp_run_reading_2026_10_20.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 733 | `_eta_preexp_run_register_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 734 | `_eta_preexp_stop_register_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 735 | `_eta_preexp_wait_and_leveling_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 736 | `_eta_sep_caliber_draft_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 737 | `_eta_sep_measurement_data_2026_10_20.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 738 | `_eta_sep_measurement_reading_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 739 | `_eta_sep_measurement_recalc_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 740 | `_exp04_h_contrast_readings_2026_10_10.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 741 | `_exp04_h_contrast_readings_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 742 | `_exp06_independent_check_2026_10_10.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 743 | `_exp06_selfverified_renaming_note_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 744 | `_exp06_selfverified_runner_fix_note_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 745 | `_exp06_supplement_four_gaps_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 746 | `_experiment_face_scope_column1_supplement_draft_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 747 | `_experiment_face_scope_list_draft_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 748 | `_ext5_verdict_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 749 | `_external_commission_gemini4_ge01_theory_inputs_2026_10_15_dispatch.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 750 | `_external_commission_gemini4_ge01_theory_inputs_2026_10_15_draft.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 751 | `_f12_kd_disposition_register_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 752 | `_f2_branch_fix_register_2026_09_29.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 753 | `_f2_closeout_note_2026_09_29.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 754 | `_f3_payment_vector_reconstruction_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 755 | `_f3_payment_vector_reconstruction_data_2026_10_19.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 756 | `_f3_payment_vector_third_party_recalc_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 757 | `_f4_direction1_domain_effectivity_2026_10_11.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 758 | `_f7d_today_no_open_erratum_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 759 | `_face_r_coexist_verdict_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 760 | `_fail_h0_verdict_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 761 | `_fake_verdict_reverify_sixitem_ledger_2026_09_30.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 762 | `_family_de_stale_refresh_matrix_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 763 | `_family_de_stale_refresh_repo_exec_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 764 | `_family_de_stale_refresh_sub_exec_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 765 | `_field_sources_lift_register_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 766 | `_field_table_c6_c8_o5_recommendation_draft_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 767 | `_five_terminal_judgments_ruling_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 768 | `_five_zero_recheck_evidence_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 769 | `_fiveverdict_census_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 770 | `_fivezero_final_audit_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 771 | `_forgotten_recovery_register_2026_10_08.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 772 | `_four_class_backtrace_inventory_2026_10_13_r1.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 773 | `_four_items_alternative_deliberation_judgment_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 774 | `_freeze_criterion_rewire_design_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 775 | `_freeze_face_four_rulings_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 776 | `_freeze_final_replay_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 777 | `_freeze_preexp_design_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 778 | `_freeze_preexp_exec_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 779 | `_freeze_preexp_exec_r2_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 780 | `_freeze_rewire_approval_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 781 | `_g1_archive_zone_search_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 782 | `_g1_closure_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 783 | `_g2_residual_cause_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 784 | `_g5_ccp_execution_prereqs_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 785 | `_g5_ccp_seed_designation_revision_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 786 | `_g5_rejudgment_construction_change_plan_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 787 | `_gamma_taucert_scope_delimitation_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 788 | `_gamma_taucert_sourcing_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 789 | `_gap10_four_rulings_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 790 | `_gap_and_kd_flip_master_inventory_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 791 | `_gate1_count_defect_erratum_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 792 | `_gate1_five_zero_recheck_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 793 | `_gate1_five_zero_recheck_glm_scope_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 794 | `_gate1_gap_residuals_adoption_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 795 | `_gate1_gap_three_items_disposition_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 796 | `_gate1_glm_reply_integration_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 797 | `_gate1_scope_inclusion_glm_commission_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 798 | `_gate1_unclosed_classification_tree_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 799 | `_gate1_unclosed_writeoff_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 800 | `_gate_one_registers_erratum_distribution_and_path_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 801 | `_gate_one_reopened_and_stage2_rejection_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 802 | `_gd03_caliber_note_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 803 | `_ge01_5anchor_json_approval_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 804 | `_ge01_5anchor_json_draft_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 805 | `_ge01_5anchor_json_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 806 | `_ge01_ab_pilot_selection_design_draft_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 807 | `_ge01_c2_canonical_effect_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 808 | `_ge01_c3_gaps_disposition_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 809 | `_ge01_c5_disposition_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 810 | `_ge01_calculator_rebuild_design_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 811 | `_ge01_calculator_rebuild_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 812 | `_ge01_d1_theory_input_disposition_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 813 | `_ge01_d1_theory_input_sourcing_design_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 814 | `_ge01_ecr_anchor_convergence_deliberation_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 815 | `_ge01_ecr_anchor_effect_register_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 816 | `_ge01_ecr_anchor_sourcing_design_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 817 | `_ge01_ecr_baseline_invalid_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 818 | `_ge01_epsilon_grid_exec_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 819 | `_ge01_epsilon_sensitivity_grid_design_r1_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 820 | `_ge01_freeze_flow_execution_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 821 | `_ge01_frozen_runs_on_disk_erratum_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 822 | `_ge01_full_1494_exec_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 823 | `_ge01_full_1494_exec_r1_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 824 | `_ge01_full_1494_freeze_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 825 | `_ge01_full_1494_resume32_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 826 | `_ge01_gt_kill_family_byte_stream_effect_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 827 | `_ge01_gt_kill_family_carrier_construction_draft_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 828 | `_ge01_gt_kill_family_generation_design_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 829 | `_ge01_gt_kill_family_member_table_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 830 | `_ge01_launch_gate_recheck_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 831 | `_ge01_numeric_literature_search_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 832 | `_ge01_prereg_5anchor.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 833 | `_ge01_prereg_5anchor_v2.json` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 834 | `_ge01_prereg_5anchor_v2_lock_register_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 835 | `_ge01_prereg_5anchor_v3.json` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 836 | `_ge01_prereg_prelexp_selection_design_v2_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 837 | `_ge01_prereg_seven_requirements_draft_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 838 | `_ge01_readiness_after_prereg_effect_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 839 | `_ge01_s3_v_adjudicable_recheck_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 840 | `_ge01_s3b_v_exec_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 841 | `_ge01_spec_anchor_canonical_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 842 | `_ge01_spec_anchor_erratum_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 843 | `_ge01_t2_t3_null_resolution_design_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 844 | `_ge01_unblock_effect_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 845 | `_ge01_unblock_progress_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 846 | `_ge02_adoption_freeze_register_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 847 | `_ge02_anchor_landing_build_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 848 | `_ge02_anchor_landing_effect_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 849 | `_gemini4_reply_verification_register_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 850 | `_ghostref_copy_log_2026_09_23.json` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 851 | `_github_delete_and_suspect_lists_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 852 | `_github_suspect_rulings_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 853 | `_gitignore_rx_fix_adoption_register_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 854 | `_gitignore_rx_fix_drift_register_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 855 | `_glm_commission_gap_resolution_directive_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 856 | `_glm_crossface_item4_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 857 | `_glm_delivery_face_disposition_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 858 | `_glm_delivery_pack_verification_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 859 | `_glm_evidence_pack_unpack_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 860 | `_glm_gaps_into_stage1_directive_effect_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 861 | `_glm_new_gaps_directive_effect_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 862 | `_glm_pack_index_snapshot_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 863 | `_glm_reply_no_upload_and_gap_review_directive_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 864 | `_glm_reply_pack_intake_verification_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 865 | `_glm_supplement_expand_directive_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 866 | `_glm_unique_reply_117_triage_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 867 | `_glm_wholepack_irreproducible_erratum_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 868 | `_gt_kill_family_carrier_draft_register_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 869 | `_gt_kill_line_carrier_effect_register_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 870 | `_h5_session_census_2026_10_19_part1.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 871 | `_h5_session_census_2026_10_19_part2.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 872 | `_h_budget_measurement_exec_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 873 | `_h_face_external_evidence_eval_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 874 | `_h_face_freeze_ruling_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 875 | `_h_three_domain_naming_caliber_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 876 | `_harness_42b_drift_semantics_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 877 | `_harness_anchor_reconcile_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 878 | `_harness_mask_correct_value_validation_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 879 | `_hidden_gaps_audit_full_history_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 880 | `_historical_ forgetting_recheck_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 881 | `_historical_forgetting_21_status_update_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 882 | `_independent_review_history_gaps_kd_2026_10_19_sub.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 883 | `_interval_420_600_upper_bound_deliberation_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 884 | `_interval_ceiling_post_lock_deliberation_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 885 | `_interval_range_post_lock_note_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 886 | `_is_corr_pair_caliber_revision_proposal_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 887 | `_item6_c2_card_reference_registration_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 888 | `_item6_c2_e3_erratum_update_register_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 889 | `_item6_c2_four_fields_adjudication_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 890 | `_item6_c2_four_fields_adoption_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 891 | `_item6_c3_selflimit_sentence_effect_register_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 892 | `_judgement_criteria_reference_only_no_utility_draft_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 893 | `_k_v3df_0_1_four_readings_2026_10_09.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 894 | `_k_v3df_0_1_four_readings_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 895 | `_k_v3s_4_3_frozen_recompute_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 896 | `_kfp6_nature_and_eta_expface_adjudication_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 897 | `_kickoff_experiment_window_directive_effect_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 898 | `_kill_line_field_value_sourcing_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 899 | `_killface_v1_design_draft_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 900 | `_killface_v1_effect_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 901 | `_kimi_postexec_receipt_verification_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 902 | `_kimi_preexec_final_rulings_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 903 | `_kimi_receipt_authority_rulings_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 904 | `_kl_m41_3_remeasure_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 905 | `_kl_m41_3_reverdict_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 906 | `_kl_m41_3_reverdict_adoption_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 907 | `_kl_m41_3_three_seed_exec_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 908 | `_kl_m41_3_verdict_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 909 | `_klm41_2_bootstrap_ci_exec_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 910 | `_knock_off_directive_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 911 | `_krj3_kd_registry_correction_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 912 | `_kt_a1_anchor_drift_root_cause_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 913 | `_kt_a1_v0_lineage_corrigendum_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 914 | `_kv3s_4_4_rejudge_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 915 | `_l266_face_label_note_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 916 | `_l2_2_duplication_criterion_adjudication_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 917 | `_l2_2_two_arms_identity_adjudication_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 918 | `_leftover_minor_adoptions_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 919 | `_log_purge_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 920 | `_log_purge_v2_execution_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 921 | `_log_retention_policy_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 922 | `_log_retention_purge_2026_10_13.py` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 923 | `_m08_boundary_caliber_c1_c8_effect_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 924 | `_m08_measured_enumeration_exec_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 925 | `_m2_c_tier_corrigendum_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 926 | `_m2_kd_disposition_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 927 | `_m2_terminal_verdict_effect_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 928 | `_m3_disposition_v_eps_star_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 929 | `_m41_double_readout_contrast_exec_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 930 | `_m41_double_readout_contrast_exec_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 931 | `_m41_verdict_kd_effect_register_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 932 | `_m44_status_enum_backfill_design_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 933 | `_m5_k5_network_verification_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 934 | `_m5_reattribution_recommendation_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 935 | `_main_count_caliber_lock_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 936 | `_material_expansion_build_exec_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 937 | `_material_expansion_drift_authorized_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 938 | `_material_expansion_sourcing_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 939 | `_material_expansion_verdict_kd_effect_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 940 | `_material_root45_remeasure_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 941 | `_md_a_field_composition_draft_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 942 | `_md_trigger_prereg_effectivity_2026_10_11.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 943 | `_mda8_preexp_run_reading_2026_10_20.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 944 | `_mda8_preexp_run_register_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 945 | `_mda8_readlaw_o1_o4_c4_recommendation_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 946 | `_mda8a24_release_trigger_proposals_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 947 | `_memo_independence_directive_effect_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 948 | `_memory_errata_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 949 | `_merge_govern_approval_and_eps1_release_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 950 | `_mirror_morphology_comparison_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 951 | `_morning_brief_pending_rulings_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 952 | `_mq19_item6_caption_restatement_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 953 | `_mq19_item6_f12_archive_recompute_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 954 | `_mq20_errata_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 955 | `_mq_rollout_v1_effect_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 956 | `_mq_rollout_v2_effect_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 957 | `_mq_rollout_v3_effect_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 958 | `_mq_rollout_v4_effect_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 959 | `_mq_rollout_v5_effect_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 960 | `_mq_rollout_v6_effect_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 961 | `_mq_rollout_v9_effect_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 962 | `_n2_clause_transcription_supplement_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 963 | `_n2_equivalence_verification_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 964 | `_n3_o5_terminal_effect_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 965 | `_n3_o5_terminal_verdict_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 966 | `_n7_af_relocation_register_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 967 | `_n_distinct_grain_verdict_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 968 | `_n_distinct_proof_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 969 | `_naming_ruling_note_2026_09_29.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 970 | `_next_stage3_dir_optimization_ruling_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 971 | `_night_mode_adoption_and_registry_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 972 | `_night_mode_adoption_corrigendum_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 973 | `_night_mode_adoption_relabel_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 974 | `_night_outputs_adoption_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 975 | `_night_shift_handover_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 976 | `_night_shift_handover_2026_10_14_r2.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 977 | `_no_backup_ruling_and_report_caliber_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 978 | `_noncore_upload_caliber_draft_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 979 | `_noncore_upload_caliber_effect_register_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 980 | `_nonportrait_criterion_formalization_design_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 981 | `_null_u_aggregation_caliber_draft_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 982 | `_null_u_aggregation_effect_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 983 | `_numbering_659_overlap_semantic_review_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 984 | `_numbering_claims_and_prefix_table_effect_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 985 | `_numbering_face_recheck_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 986 | `_numbering_face_signature_supplement_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 987 | `_numbering_family_count_effect_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 988 | `_numbering_family_count_erratum_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 989 | `_numbering_hash_bucket_criterion_design_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 990 | `_numbering_raw_residual_461_root_cause_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 991 | `_numbering_system_audit_and_definition_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 992 | `_o1_498_lock_scope_deliberation_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 993 | `_o1_reading_c_effect_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 994 | `_o1_transcription_face_erratum_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 995 | `_one_finish_gap_audit_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 996 | `_p0_scan_2026_10_12.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 997 | `_p4_fallback_target_search_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 998 | `_p4_inplace_resolution_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 999 | `_pa_harness_anchor_v3_effect_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1000 | `_pa_harness_anchor_value_update_v2.json` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1001 | `_pa_harness_anchor_value_update_v3.json` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1002 | `_pa_harness_anchor_value_update_v3_lock_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1003 | `_pack_card_four_rulings_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1004 | `_pack_fingerprint_baseline_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1005 | `_pack_payload8_k1r4r3_disposition_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1006 | `_pb_anchor_reanchor_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1007 | `_pdf_is_coze_reply_ruling_effect_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1008 | `_pending_pack_four_rulings_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1009 | `_pending_residual_minimal_set_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1010 | `_pending_rulings_triage_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1011 | `_plan_v3_pending_verify_2026_09_30.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1012 | `_post_execution_report_kimi_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1013 | `_poststrip_recalc_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1014 | `_pre_execution_report_kimi_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1015 | `_pre_execution_report_kimi_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1016 | `_predelete_backup_caliber_draft_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1017 | `_preexp_degen_gate_data_2026_10_20.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1018 | `_preexp_degen_gate_reading_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1019 | `_preexp_degen_gate_recalc_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1020 | `_preexp_design_kmda8a24_degen_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1021 | `_preexp_design_new_construct_mda8a24_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1022 | `_preexp_mda8a24_c1_data_2026_10_20.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1023 | `_preexp_mda8a24_c1_reading_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1024 | `_preexp_mda8a24_c2c4_data_2026_10_20.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1025 | `_preexp_mda8a24_c2c4_reading_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1026 | `_preexp_mda8a24_c5_armpairs_data_2026_10_20.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1027 | `_preexp_mda8a24_c5_armpairs_measurement_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1028 | `_preexp_mda8a24_c5_armpairs_measurement_data_2026_10_20.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1029 | `_preexp_mda8a24_c5_armpairs_reading_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1030 | `_preexp_mda8a24_c5_armpairs_recalc_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1031 | `_preexp_mda8a24_recalc_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1032 | `_prereg_caliber4_epsilon_revision_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1033 | `_prereg_lock_v1_epsilon_lu_klm41_register_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1034 | `_prereg_lock_v2_h_epsilon_gamma_taucert_u_register_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1035 | `_prereg_lock_v2a_t5_completion_register_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1036 | `_q3_c1c4_l282_transposition_fix_applied_note_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1037 | `_q3_transposition_errata_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1038 | `_questionnaire_cards_intake_register_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1039 | `_questionnaire_cards_intake_register_supplement_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1040 | `_questionnaire_cards_intake_register_supplement_2_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1041 | `_questionnaire_cards_intake_register_supplement_3_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1042 | `_questionnaire_cards_intake_register_supplement_4_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1043 | `_questionnaire_cards_intake_register_supplement_5_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1044 | `_questionnaire_cards_intake_register_supplement_6_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1045 | `_questionnaire_cards_intake_register_supplement_6_receipt_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1046 | `_questionnaire_cards_intake_register_supplement_6_receipt_v2_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1047 | `_r2_build_manifest_2026_10_12.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1048 | `_r2_execution_receipt_kimi_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1049 | `_r2_reading_verdict_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1050 | `_r2_sep_endogeneity_erratum_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1051 | `_r2b_adoption_and_bytewise_caliber_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1052 | `_r3_m2_disposition_register_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1053 | `_r5_spec_pack_retrieval_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1054 | `_r6_github_face_verification_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1055 | `_r6_supplement_first_version_disposition_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1056 | `_r9_ge01_prereg_effect_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1057 | `_r_pair4_design_and_texts_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1058 | `_r_pair_addendum_2026_10_09.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1059 | `_r_pair_intake_recompute_register_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1060 | `_r_pair_is_corr_coverage_design_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1061 | `_r_pair_question_texts_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1062 | `_reading_e_33_baseline_declaration_deliberation_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1063 | `_reading_e_33_historical_nominal_value_corrigendum_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1064 | `_recycle_purge_resolution_and_434_adoption_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1065 | `_ref_only_no_utility_criteria_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1066 | `_refonly_161_reading_verdict_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1067 | `_refonly_161_verify_register_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1068 | `_refonly_161_verify_register_r2_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1069 | `_register_correction_batch_and_u14_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1070 | `_register_face_errata_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1071 | `_remote_509_desensitization_direction_audit_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1072 | `_remote_baseline_advance_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1073 | `_remote_delete_face_pullback_register_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1074 | `_remote_pullback_register_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1075 | `_remote_root_face_413_68_erratum_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1076 | `_replies_arrival_and_stage2_restore_directive_effect_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1077 | `_reply_correctness_audit_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1078 | `_reply_letter_approval_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1079 | `_reply_path_correction_register_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1080 | `_repo_full_inventory_catalogue_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1081 | `_repo_noise_cleanup_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1082 | `_repo_post_cleanup_snapshot_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1083 | `_residual_card1_four_rulings_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1084 | `_resolution_path_rulings_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1085 | `_results_split_proposal_2026_10_21.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1086 | `_resume32_adoption_and_flip_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1087 | `_ritt_def_adoption_and_remeasure_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1088 | `_ritt_def_proof_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1089 | `_ritt_remeasure_readings_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1090 | `_rpp_perseed_recalc_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1091 | `_ruled_unclosed_closure_verdict_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1092 | `_runface_vs_shape_caliber_draft_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1093 | `_runface_vs_shape_multidim_reading_2026_10_20.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1094 | `_runface_vs_shape_multidim_reading_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1095 | `_runface_vs_shape_multidim_supplement_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1096 | `_s2_attainment_corrigendum_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1097 | `_s3_closeout_convergence_2026_10_01.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1098 | `_s3_d1fill_recount_2026_10_01.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1099 | `_s3_f1_loader_fix_recompute_2026_10_08.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1100 | `_s3_flip_s5_resolution_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1101 | `_s3_kv3s_3_full_recompute_2026_10_01.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1102 | `_s3_s5_explanation_and_disposition_verdict_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1103 | `_s3_s5_kd_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1104 | `_s3_s5_kd_effect_2026_10_17_append1.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1105 | `_s3_th_v21_reconciliation_verdict_2026_10_01.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1106 | `_s3prime_alert_disposition_judgment_2026_10_11.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1107 | `_s3prime_degeneracy_selfcert_2026_10_11.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1108 | `_s4_daily_share_margin_prerequisite_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1109 | `_s4_execution_sequence_review_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1110 | `_s4_face_five_lines_ci_readings_execution_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1111 | `_s4_face_five_lines_exec_sec8_erratum_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1112 | `_s4_face_sync_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1113 | `_s4_face_v2_sync_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1114 | `_s4_final_ruling_effectivity_register_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1115 | `_s4_heldout_sampling_caliber_ruling_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1116 | `_s4_heldout_sampling_seed42_items_2026_10_09.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1117 | `_s4_heldout_sampling_seedprime_items_2026_10_10.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1118 | `_s4_heldout_sampling_seedprime_items_register_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1119 | `_s4_heldout_sampling_seedthird_items_2026_10_11.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1120 | `_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1121 | `_s4_kex_killline_freeze_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1122 | `_s4_open_questions_addendum_2026_10_09.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1123 | `_s4_open_questions_design_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1124 | `_s4_open_questions_intake_recompute_register_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1125 | `_s4_reading_prep_order_2026_10_08.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1126 | `_s4_regen_execution_plan_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1127 | `_s4_regen_golive_clearance_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1128 | `_s4_seedprime_inheldout_recompute_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1129 | `_s4_seedprime_seq_t1_only_supplement_2026_10_11.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1130 | `_s4_seedprime_seq_t1_only_supplement_items_2026_10_11.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1131 | `_s4_source_wave_mapping_registration_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1132 | `_s4_substrate_freeze_register_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1133 | `_s4_substrate_grid_availability_2026_10_08.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1134 | `_s4_substrate_grid_availability_2026_10_08.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1135 | `_s4_substrate_refreeze_register_179_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1136 | `_s4_substrate_topup_addendum_2026_10_09.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1137 | `_s4_substrate_topup_collection_register_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1138 | `_s4_topup_intake_recompute_register_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1139 | `_s4_topup_questionnaire_design_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1140 | `_s4_tree_construct_adjusted_readings_2026_10_10.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1141 | `_s4_tree_construct_adjustment_assessment_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1142 | `_s4_v31_displacement_items_2026_10_10.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1143 | `_s4_v31_drift_register_face1_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1144 | `_s4_v31_keyword_table_final_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1145 | `_s4_v31_readings_execution_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1146 | `_s4_v31_readings_summary_2026_10_10.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1147 | `_s4_v31_regen_gold_items_2026_10_10.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1148 | `_s4_v31_regen_gold_register_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1149 | `_s4_vclause_1_6_revision_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1150 | `_s4prime_five_lines_readings_2026_10_11.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1151 | `_s4prime_five_lines_runner_2026_10_11.py` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1152 | `_s5doubleprime_five_lines_readings_2026_10_11.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1153 | `_scroll_wave1_four_rulings_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1154 | `_scroll_wave2_four_rulings_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1155 | `_scroll_wave4_three_rulings_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1156 | `_scroll_wave5_four_rulings_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1157 | `_seed_double_identifier_finalization_2026_10_11.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1158 | `_seven23_map_revision_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1159 | `_skill_reference_update_and_user_surface_survey_2026_09_30.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1160 | `_spec_l22_landing_path_migration_note_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1161 | `_spec_l32_scope_note_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1162 | `_stage1_eta_kill_line_freeze_draft_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1163 | `_stage1_eta_numeric_freeze_draft_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1164 | `_stage1_eta_preexp_execution_register_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1165 | `_stage1_eta_preexp_run_register_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1166 | `_stage1_experiment_gap_inventory_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1167 | `_stage1_field_table_completion_register_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1168 | `_stage1_field_table_freeze_draft_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1169 | `_stage1_gap_exhaustive_audit_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1170 | `_stage1_gate_remedy_draft_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1171 | `_stage1_independent_gate_review_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1172 | `_stage1_prereq_wave1_evidence_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1173 | `_stage1_prereq_wave1_proposals_2026_10_20.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1174 | `_stage1_progress_sync_directive_effect_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1175 | `_stage34_completion_withdrawal_effect_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1176 | `_stage3_1_bulk_reorg_completion_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1177 | `_stage3_1_register_fingerprint_placeholder_erratum_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1178 | `_stage3_close_and_cmp2_rulings_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1179 | `_stage3_completion_and_stage4_open_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1180 | `_stage3_r2_cleanup_register_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1181 | `_stage3_trigger_readings_items_2026_10_11.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1182 | `_stage3_trigger_recheck_2026_10_11.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1183 | `_stage4_close_and_batch3_receipt_register_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1184 | `_stage5_7_3_registration_dissolution_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1185 | `_stage5_7_6_citation_permission_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1186 | `_stage5_g1_g3_g4_verification_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1187 | `_stage5_g2_deferred_disposition_plan_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1188 | `_stage5_g2_item_e_closure_turn_b_register_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1189 | `_stage5_g2_tier_b_registration_execution_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1190 | `_stage5_g5_remote_refresh_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1191 | `_stage5_g6_g8_adoption_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1192 | `_stage5_g6_g8_caliber_alignment_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1193 | `_stage5_g6_g8_four_items_ranking_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1194 | `_stage5_g6_g8_four_items_ranking_adoption_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1195 | `_stage5_glm_onhold_and_resume_directive_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1196 | `_stage5_new_versions_prep_directive_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1197 | `_stage5_preparation_design_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1198 | `_stage_sequence_ruling_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1199 | `_stage_sequence_violation_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1200 | `_strict3_verdict_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1201 | `_strip_c3_non_adoption_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1202 | `_supplement_500_combo_drift_authorized_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1203 | `_supplement_500_combo_effect_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1204 | `_supplement_500_combo_exec_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1205 | `_supplement_execution_receipt_kimi_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1206 | `_supplement_to_500_design_review_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1207 | `_supplemental_sync_commission_rulings_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1208 | `_t1_exp2_activation_supplement_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1209 | `_t1_exp2_answer_face_baseline_2026_10_09.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1210 | `_t1_exp2_executor_2026_10_09.py` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1211 | `_t1_exp2_result_2026_10_09.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1212 | `_t1_prereg_revision_qwen_temp_sweep_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1213 | `_t1_prereg_revision_temp_axis_exp2_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1214 | `_t1_qwen_temp_sweep_exec_register_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1215 | `_t1_qwen_temp_sweep_executor_2026_10_09.py` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1216 | `_t1_qwen_temp_sweep_r2_exec_register_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1217 | `_t1_qwen_temp_sweep_r2_executor_2026_10_09.py` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1218 | `_t1_qwen_temp_sweep_r2_result_2026_10_09.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1219 | `_t1_qwen_temp_sweep_r2_verdict_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1220 | `_t1_qwen_temp_sweep_verdict_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1221 | `_t1_r2_activation_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1222 | `_t1_substrate_gap_census_2026_10_01.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1223 | `_t1_substrate_gap_precondition_2026_10_01.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1224 | `_t1_temp_axis_new_experiment_design_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1225 | `_t2_license_final_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1226 | `_t2_path_b_build_exec_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1227 | `_t2_path_b_drift_authorized_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1228 | `_t2_t3_value_request_form_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1229 | `_t2_t3_value_sourcing_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1230 | `_t3_repro_probe_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1231 | `_t3trap_answerable_build_exec_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1232 | `_t3trap_answerable_drift_authorized_register_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1233 | `_t3trap_kd3_bprime_effect_register_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1234 | `_t3trap_kd3_disposition_deliberation_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1235 | `_t4_license_final_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1236 | `_t5_anchor_drift_authorized_register_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1237 | `_t5_generator_build_exec_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1238 | `_t_s3_3_disposition_judgment_2026_10_10.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1239 | `_temp_cleanup_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1240 | `_th_id_attribution_verification_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1241 | `_th_t1_n_min_revision_proposal_2026_10_09.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1242 | `_theory_u_hit_rate_retirement_register_2026_10_15.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1243 | `_third_batch_card2_and_rename_approval_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1244 | `_third_batch_four_rulings_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1245 | `_thirdparty_16_overwrite_necessity_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1246 | `_thirdparty_16_overwrite_ruling_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1247 | `_thirdparty_collision_16_register_kimi_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1248 | `_three_exception_pullback_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1249 | `_three_items_alternative_deliberation_judgment_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1250 | `_three_seed_measurement_exec_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1251 | `_three_seed_readout_validity_deliberation_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1252 | `_three_seed_readout_validity_effect_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1253 | `_tmp_archive_disposition_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1254 | `_tmp_archive_exec_artifacts_rewrite_map_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1255 | `_tmp_carrier_original_deletion_register_2026_10_19.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1256 | `_tmp_census_c2.txt` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1257 | `_tmp_measure_c5b_register.py` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1258 | `_tmp_write_copilot_register.py` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1259 | `_tra_v0_2026_09_10.py` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1260 | `_trae_dfamily_reply_intake_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1261 | `_trae_errata_sha_drift_attribution_2026_10_01.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1262 | `_trae_issues_batch2_corrections_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1263 | `_trae_issues_batch3_six_items_draft_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1264 | `_trae_issues_dfamily_corrections_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1265 | `_trae_issues_disposition_schedule_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1266 | `_trae_sixitem_disposal_and_collision_register_2026_10_01.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1267 | `_two_items_alternative_deliberation_judgment_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1268 | `_u01_u15_recheck_after_rulings_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1269 | `_u04_1_exemption_precondition_verification_2026_10_09.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1270 | `_u09_count_caliber_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1271 | `_u10_fail_h0_verdict_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1272 | `_u10_s3_denominator_rulings_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1273 | `_u5_referent_registry_correction_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1274 | `_u5_semantics_resolution_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1275 | `_u_1494_carrier_effect_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1276 | `_u_33_34_lock_and_33_declaration_coexistence_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1277 | `_u_720face_lock_register_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1278 | `_u_axis_active_ruling_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1279 | `_u_axis_equation_direction_deliberation_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1280 | `_u_axis_equation_direction_effect_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1281 | `_u_axis_input_vs_kdb2_recheck_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1282 | `_u_cluster1_verdict_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1283 | `_u_cluster2_verdict_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1284 | `_u_domain3_carrier_1494_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1285 | `_u_hface15_18889_lock_register_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1286 | `_u_hface_lock_register_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1287 | `_u_lock_recalc_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1288 | `_u_recalc_post_expansion_2026_10_16.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1289 | `_unclosed_47_direct_clear_b_tier_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1290 | `_unclosed_47_direct_clear_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1291 | `_unclosed_47_pi_give_draft_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1292 | `_unclosed_47_status_review_2026_10_14.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1293 | `_unified_caliber_document_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1294 | `_unique_supplement_letter_approval_effect_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1295 | `_upload_execution_receipt_kimi_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1296 | `_upload_ledger_2026_10_12.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1297 | `_upload_plan_2026_10_12.json` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1298 | `_upload_side_desensitized_remote_sha_letter_kimi_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1299 | `_upload_side_desensitized_remote_sha_letter_kimi_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1300 | `_whitelist_and_scope_ruling_effect_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1301 | `_whitelist_backup_470_cleanup_register_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1302 | `_whitelist_backup_669_cleanup_register_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1303 | `_whitelist_backup_mapping_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1304 | `_whitelist_register_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1305 | `_xiang14_reissue_register_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1306 | `_xiang14_third_pullback_register_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1307 | `_xiang14_third_reissue_registration_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1308 | `_xiang14_third_trace_and_pullback_2026_10_18.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1309 | `_xiang8_xiang12_deliberation_judgment_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1310 | `_z1_d9_three_and_c1_adoption_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1311 | `_z1_n2_da25_agency_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1312 | `_z1_three_yishi_adoption_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1313 | `_z1_two_items_adoption_register_2026_10_12.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |
| 1314 | `_zerocall_criterion_redefinition_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1315 | `_zerocall_gap_proof_register_2026_10_17.md` | **候 PI 归族** | 无机械族界 | 仓根锚定路径引用 | ⛔ 0 自拟族界 |
| 1316 | `_zone_balance_inventory_2026_10_13.md` | **候 PI 归族** | 无机械族界 | 相对路径引用 | ⛔ 0 自拟族界 |

---

## §4 映射条目 · 子目录内件（拟新路径 ＝ 旧路径 · 不动）

**其义**：此 133 件**已处 `results\` 之下之既有子目录内**（28 个子目录）—— 档2 之「族级移动」之对象为**顶层件**。
故本节一律拟「不动」。**若 PI 另裁子目录内件亦须族级移动，则属另单之授权面，本表不预断。**

| # | 旧路径 | 拟新路径 | 族 | 引用面 | 注记 |
| :-- |--: |--: |--: |--: |--: |
| 1317 | `.tmp/_audit_bom_cr_2026_10_19.py` | `.tmp/_audit_bom_cr_2026_10_19.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1318 | `.tmp/_audit_final_2026_10_19.py` | `.tmp/_audit_final_2026_10_19.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1319 | `.tmp/_audit_s12_append_2026_10_19.py` | `.tmp/_audit_s12_append_2026_10_19.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1320 | `.tmp/_audit_s12_heads_2026_10_19.py` | `.tmp/_audit_s12_heads_2026_10_19.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1321 | `.tmp/_audit_s12_heads_out_2026_10_19.txt` | `.tmp/_audit_s12_heads_out_2026_10_19.txt`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1322 | `.tmp/_audit_s12_keyclass_2026_10_19.py` | `.tmp/_audit_s12_keyclass_2026_10_19.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1323 | `.tmp/_audit_s12_keyclass_2026_10_19.txt` | `.tmp/_audit_s12_keyclass_2026_10_19.txt`（**不动**） | 无机械族界 | 裸名引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1324 | `.tmp/_audit_s12_keyscan_2026_10_19.py` | `.tmp/_audit_s12_keyscan_2026_10_19.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1325 | `.tmp/_audit_s12_keyscan_out_2026_10_19.txt` | `.tmp/_audit_s12_keyscan_out_2026_10_19.txt`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1326 | `.tmp/_audit_s12_refined_2026_10_19.py` | `.tmp/_audit_s12_refined_2026_10_19.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1327 | `.tmp/_audit_s12_refined_out_2026_10_19.txt` | `.tmp/_audit_s12_refined_out_2026_10_19.txt`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1328 | `.tmp/_audit_s12_scan_2026_10_19.py` | `.tmp/_audit_s12_scan_2026_10_19.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1329 | `.tmp/_audit_s13_7_append_2026_10_20.py` | `.tmp/_audit_s13_7_append_2026_10_20.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1330 | `.tmp/_audit_s13_anchors_2026_10_20.py` | `.tmp/_audit_s13_anchors_2026_10_20.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1331 | `.tmp/_audit_s13_anchors_out_2026_10_20.txt` | `.tmp/_audit_s13_anchors_out_2026_10_20.txt`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1332 | `.tmp/_audit_s13_append_2026_10_20.py` | `.tmp/_audit_s13_append_2026_10_20.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1333 | `.tmp/_audit_s13_conv_out_2026_10_20.txt` | `.tmp/_audit_s13_conv_out_2026_10_20.txt`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1334 | `.tmp/_audit_s13_final_2026_10_20.py` | `.tmp/_audit_s13_final_2026_10_20.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1335 | `.tmp/_audit_s13_final_out_2026_10_20.txt` | `.tmp/_audit_s13_final_out_2026_10_20.txt`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1336 | `.tmp/_audit_s13_main_heads_2026_10_20.py` | `.tmp/_audit_s13_main_heads_2026_10_20.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1337 | `.tmp/_audit_s13_main_heads_2026_10_20.txt` | `.tmp/_audit_s13_main_heads_2026_10_20.txt`（**不动**） | 无机械族界 | 裸名引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1338 | `.tmp/_audit_s13_scan_2026_10_20.py` | `.tmp/_audit_s13_scan_2026_10_20.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1339 | `.tmp/_audit_tail_2026_10_19.py` | `.tmp/_audit_tail_2026_10_19.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1340 | `.tmp/_s12_7_body_2026_10_19.md` | `.tmp/_s12_7_body_2026_10_19.md`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1341 | `.tmp/_s12_body_2026_10_19.md` | `.tmp/_s12_body_2026_10_19.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1342 | `.tmp/_s13_7_body_2026_10_20.md` | `.tmp/_s13_7_body_2026_10_20.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1343 | `.tmp/_s13_body_2026_10_20.md` | `.tmp/_s13_body_2026_10_20.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1344 | `.tmp/_s14_anchor2_2026_10_21.py` | `.tmp/_s14_anchor2_2026_10_21.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1345 | `.tmp/_s14_anchorchain2_2026_10_21.md` | `.tmp/_s14_anchorchain2_2026_10_21.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1346 | `.tmp/_s14_anchorchain_2026_10_21.md` | `.tmp/_s14_anchorchain_2026_10_21.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1347 | `.tmp/_s14_anchorchain_2026_10_21.py` | `.tmp/_s14_anchorchain_2026_10_21.py`（**不动**） | 无机械族界 | 裸名引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1348 | `.tmp/_s14_append_2026_10_21.py` | `.tmp/_s14_append_2026_10_21.py`（**不动**） | 无机械族界 | 裸名引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1349 | `.tmp/_s14_append_report_2026_10_21.md` | `.tmp/_s14_append_report_2026_10_21.md`（**不动**） | 无机械族界 | 裸名引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1350 | `.tmp/_s14_body_2026_10_21.md` | `.tmp/_s14_body_2026_10_21.md`（**不动**） | 无机械族界 | 裸名引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1351 | `.tmp/_s14_cards_full_2026_10_21.md` | `.tmp/_s14_cards_full_2026_10_21.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1352 | `.tmp/_s14_cards_full_2026_10_21.py` | `.tmp/_s14_cards_full_2026_10_21.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1353 | `.tmp/_s14_disk_scan_2026_10_21.py` | `.tmp/_s14_disk_scan_2026_10_21.py`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1354 | `.tmp/_s14_disk_scan_out_t1.md` | `.tmp/_s14_disk_scan_out_t1.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1355 | `.tmp/_s14_disk_scan_out_t2.md` | `.tmp/_s14_disk_scan_out_t2.md`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1356 | `.tmp/_s14_events2_2026_10_21.py` | `.tmp/_s14_events2_2026_10_21.py`（**不动**） | 无机械族界 | 裸名引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1357 | `.tmp/_s14_final_measure_2026_10_21.md` | `.tmp/_s14_final_measure_2026_10_21.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1358 | `.tmp/_s14_final_measure_2026_10_21.py` | `.tmp/_s14_final_measure_2026_10_21.py`（**不动**） | 无机械族界 | 裸名引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1359 | `.tmp/_s14_instrument_2026_10_21.py` | `.tmp/_s14_instrument_2026_10_21.py`（**不动**） | 无机械族界 | 裸名引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1360 | `.tmp/_s14_instrument_out_2026_10_21.md` | `.tmp/_s14_instrument_out_2026_10_21.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1361 | `.tmp/_s14_main_events2_2026_10_21.md` | `.tmp/_s14_main_events2_2026_10_21.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1362 | `.tmp/_s14_main_events_2026_10_21.md` | `.tmp/_s14_main_events_2026_10_21.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1363 | `.tmp/_s14_main_session_slice_2026_10_21.md` | `.tmp/_s14_main_session_slice_2026_10_21.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1364 | `.tmp/_s14_msgdist_2026_10_21.md` | `.tmp/_s14_msgdist_2026_10_21.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1365 | `.tmp/_s14_msgdist_2026_10_21.py` | `.tmp/_s14_msgdist_2026_10_21.py`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1366 | `.tmp/_s14_session_scan2_2026_10_21.py` | `.tmp/_s14_session_scan2_2026_10_21.py`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1367 | `.tmp/_s14_session_scan_2026_10_21.py` | `.tmp/_s14_session_scan_2026_10_21.py`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1368 | `.tmp/_s14_session_scan_out_2026_10_21.md` | `.tmp/_s14_session_scan_out_2026_10_21.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `.tmp\` 内 · 顶层族级移动不涉 |
| 1369 | `_archive_2026-10-12/exec_artifacts/_exp06_1009fix_build_2026_10_10.py` | `_archive_2026-10-12/exec_artifacts/_exp06_1009fix_build_2026_10_10.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_archive_2026-10-12/exec_artifacts\` 内 · 顶层族级移动不涉 |
| 1370 | `_archive_2026-10-12/exec_artifacts/_exp06_1009fix_lnref2_2026_10_10.py` | `_archive_2026-10-12/exec_artifacts/_exp06_1009fix_lnref2_2026_10_10.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_archive_2026-10-12/exec_artifacts\` 内 · 顶层族级移动不涉 |
| 1371 | `_archive_2026-10-12/exec_artifacts/_exp06_1009fix_lnref_2026_10_10.py` | `_archive_2026-10-12/exec_artifacts/_exp06_1009fix_lnref_2026_10_10.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_archive_2026-10-12/exec_artifacts\` 内 · 顶层族级移动不涉 |
| 1372 | `_archive_2026-10-12/exec_artifacts/_exp06_1009fix_verify_2026_10_10.py` | `_archive_2026-10-12/exec_artifacts/_exp06_1009fix_verify_2026_10_10.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_archive_2026-10-12/exec_artifacts\` 内 · 顶层族级移动不涉 |
| 1373 | `_archive_2026-10-12/exec_artifacts/_exp06_fixcopy_verify_probe_2026_10_10.py` | `_archive_2026-10-12/exec_artifacts/_exp06_fixcopy_verify_probe_2026_10_10.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_archive_2026-10-12/exec_artifacts\` 内 · 顶层族级移动不涉 |
| 1374 | `_archive_2026-10-12/exec_artifacts/c5_guard_minmaxstd_2026_10_01.py` | `_archive_2026-10-12/exec_artifacts/c5_guard_minmaxstd_2026_10_01.py`（**不动**） | c5_* | 相对路径引用 | 已在子目录 `_archive_2026-10-12/exec_artifacts\` 内 · 顶层族级移动不涉 |
| 1375 | `_archive_2026-10-12/exec_artifacts/e4_axis2_crosscheck_2026_10_10.py` | `_archive_2026-10-12/exec_artifacts/e4_axis2_crosscheck_2026_10_10.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_archive_2026-10-12/exec_artifacts\` 内 · 顶层族级移动不涉 |
| 1376 | `_archive_2026-10-12/exec_artifacts/e4_axis2_denominator_recheck_2026_10_10.py` | `_archive_2026-10-12/exec_artifacts/e4_axis2_denominator_recheck_2026_10_10.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_archive_2026-10-12/exec_artifacts\` 内 · 顶层族级移动不涉 |
| 1377 | `_archive_2026-10-12/exec_artifacts/e4_axis2_final_validation_2026_10_10.py` | `_archive_2026-10-12/exec_artifacts/e4_axis2_final_validation_2026_10_10.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_archive_2026-10-12/exec_artifacts\` 内 · 顶层族级移动不涉 |
| 1378 | `_archive_2026-10-12/exec_artifacts/e4_axis2_hit_unchanged_probe_2026_10_10.py` | `_archive_2026-10-12/exec_artifacts/e4_axis2_hit_unchanged_probe_2026_10_10.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_archive_2026-10-12/exec_artifacts\` 内 · 顶层族级移动不涉 |
| 1379 | `_archive_2026-10-12/exec_artifacts/e4_axis2_v11_displacement_run_2026_10_10.py` | `_archive_2026-10-12/exec_artifacts/e4_axis2_v11_displacement_run_2026_10_10.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_archive_2026-10-12/exec_artifacts\` 内 · 顶层族级移动不涉 |
| 1380 | `_archive_2026-10-12/exec_artifacts/exp06_independent_json_gen_2026_10_10.py` | `_archive_2026-10-12/exec_artifacts/exp06_independent_json_gen_2026_10_10.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_archive_2026-10-12/exec_artifacts\` 内 · 顶层族级移动不涉 |
| 1381 | `_archive_2026-10-12/exec_artifacts/exp06_supplement_probe_2026_10_10.py` | `_archive_2026-10-12/exec_artifacts/exp06_supplement_probe_2026_10_10.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_archive_2026-10-12/exec_artifacts\` 内 · 顶层族级移动不涉 |
| 1382 | `_archive_2026-10-12/exec_artifacts/scan_five_terminal_2026_10_10.py` | `_archive_2026-10-12/exec_artifacts/scan_five_terminal_2026_10_10.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_archive_2026-10-12/exec_artifacts\` 内 · 顶层族级移动不涉 |
| 1383 | `_archive_2026-10-12/pycache_sink/deposon_team_plugins_pycache/boss_pa_1_rbr_rm_v3df_ab_alpha_2026_10_09.cpython-314.pyc` | `_archive_2026-10-12/pycache_sink/deposon_team_plugins_pycache/boss_pa_1_rbr_rm_v3df_ab_alpha_2026_10_09.cpython-314.pyc`（**不动**） | boss_* | 仓根锚定路径引用 | 已在子目录 `_archive_2026-10-12/pycache_sink/deposon_team_plugins_pycache\` 内 · 顶层族级移动不涉 |
| 1384 | `_archive_2026-10-12/pycache_sink/deposon_team_plugins_pycache/boss_pa_1_rbr_rm_v3df_ab_beta_2026_10_09.cpython-314.pyc` | `_archive_2026-10-12/pycache_sink/deposon_team_plugins_pycache/boss_pa_1_rbr_rm_v3df_ab_beta_2026_10_09.cpython-314.pyc`（**不动**） | boss_* | 仓根锚定路径引用 | 已在子目录 `_archive_2026-10-12/pycache_sink/deposon_team_plugins_pycache\` 内 · 顶层族级移动不涉 |
| 1385 | `_archive_2026-10-12/pycache_sink/deposon_team_plugins_pycache/boss_pa_1_rbr_rm_v3df_p1_reopen_2026_09_29.cpython-314.pyc` | `_archive_2026-10-12/pycache_sink/deposon_team_plugins_pycache/boss_pa_1_rbr_rm_v3df_p1_reopen_2026_09_29.cpython-314.pyc`（**不动**） | boss_* | 仓根锚定路径引用 | 已在子目录 `_archive_2026-10-12/pycache_sink/deposon_team_plugins_pycache\` 内 · 顶层族级移动不涉 |
| 1386 | `_archive_2026-10-12/pycache_sink/results_pycache/_s4prime_five_lines_runner_2026_10_11.cpython-314.pyc` | `_archive_2026-10-12/pycache_sink/results_pycache/_s4prime_five_lines_runner_2026_10_11.cpython-314.pyc`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_archive_2026-10-12/pycache_sink/results_pycache\` 内 · 顶层族级移动不涉 |
| 1387 | `_archive_2026-10-12/pycache_sink/results_pycache/_s5doubleprime_five_lines_runner_2026_10_11.cpython-314.pyc` | `_archive_2026-10-12/pycache_sink/results_pycache/_s5doubleprime_five_lines_runner_2026_10_11.cpython-314.pyc`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_archive_2026-10-12/pycache_sink/results_pycache\` 内 · 顶层族级移动不涉 |
| 1388 | `_archive_2026-10-12/pycache_sink/results_pycache/_t1_exp2_executor_2026_10_09.cpython-314.pyc` | `_archive_2026-10-12/pycache_sink/results_pycache/_t1_exp2_executor_2026_10_09.cpython-314.pyc`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_archive_2026-10-12/pycache_sink/results_pycache\` 内 · 顶层族级移动不涉 |
| 1389 | `_archive_2026-10-12/pycache_sink/results_pycache/_v4_pi_cot_v3_ruleset_v3_executor.cpython-314.pyc` | `_archive_2026-10-12/pycache_sink/results_pycache/_v4_pi_cot_v3_ruleset_v3_executor.cpython-314.pyc`（**不动**） | _v* | 仓根锚定路径引用 | 已在子目录 `_archive_2026-10-12/pycache_sink/results_pycache\` 内 · 顶层族级移动不涉 |
| 1390 | `_archive_2026-10-12/pycache_sink/results_pycache/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.cpython-314.pyc` | `_archive_2026-10-12/pycache_sink/results_pycache/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.cpython-314.pyc`（**不动**） | _v* | 仓根锚定路径引用 | 已在子目录 `_archive_2026-10-12/pycache_sink/results_pycache\` 内 · 顶层族级移动不涉 |
| 1391 | `_archive_2026-10-12/superseded_variants/_card23_readout_utf8.txts` | `_archive_2026-10-12/superseded_variants/_card23_readout_utf8.txts`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_archive_2026-10-12/superseded_variants\` 内 · 顶层族级移动不涉 |
| 1392 | `_archive_2026-10-14/voided/_four_class_backtrace_inventory_2026_10_13.md` | `_archive_2026-10-14/voided/_four_class_backtrace_inventory_2026_10_13.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_archive_2026-10-14/voided\` 内 · 顶层族级移动不涉 |
| 1393 | `_archive_2026-10-14/voided/_ge01_epsilon_sensitivity_grid_design_2026_10_13.md` | `_archive_2026-10-14/voided/_ge01_epsilon_sensitivity_grid_design_2026_10_13.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_archive_2026-10-14/voided\` 内 · 顶层族级移动不涉 |
| 1394 | `_archive_2026_09_24/_final_verify.py._moved_20260924_1830` | `_archive_2026_09_24/_final_verify.py._moved_20260924_1830`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_archive_2026_09_24\` 内 · 顶层族级移动不涉 |
| 1395 | `_archive_2026_09_24/_l11_run1.json` | `_archive_2026_09_24/_l11_run1.json`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_archive_2026_09_24\` 内 · 顶层族级移动不涉 |
| 1396 | `_archive_2026_09_24/_l14_checkpoint.json` | `_archive_2026_09_24/_l14_checkpoint.json`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_archive_2026_09_24\` 内 · 顶层族级移动不涉 |
| 1397 | `_archive_2026_09_24/_l14_records.json` | `_archive_2026_09_24/_l14_records.json`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_archive_2026_09_24\` 内 · 顶层族级移动不涉 |
| 1398 | `_archive_2026_09_24/_volc_22cap_emb.py` | `_archive_2026_09_24/_volc_22cap_emb.py`（**不动**） | _v* | 相对路径引用 | 已在子目录 `_archive_2026_09_24\` 内 · 顶层族级移动不涉 |
| 1399 | `_archive_2026_09_24/l14_runner_v2.py` | `_archive_2026_09_24/l14_runner_v2.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_archive_2026_09_24\` 内 · 顶层族级移动不涉 |
| 1400 | `_archive_2026_09_24/l14_runner_v2_r1_atomic_2026_09_29.py` | `_archive_2026_09_24/l14_runner_v2_r1_atomic_2026_09_29.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_archive_2026_09_24\` 内 · 顶层族级移动不涉 |
| 1401 | `_d9_e2e_backup_2026_10_13/_s4_heldout_sampling_seedprime_items_2026_10_10.json` | `_d9_e2e_backup_2026_10_13/_s4_heldout_sampling_seedprime_items_2026_10_10.json`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_d9_e2e_backup_2026_10_13\` 内 · 顶层族级移动不涉 |
| 1402 | `_d9_e2e_backup_2026_10_13/_s4_heldout_sampling_seedthird_items_2026_10_11.json` | `_d9_e2e_backup_2026_10_13/_s4_heldout_sampling_seedthird_items_2026_10_11.json`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_d9_e2e_backup_2026_10_13\` 内 · 顶层族级移动不涉 |
| 1403 | `_d9_e2e_backup_2026_10_13/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | `_d9_e2e_backup_2026_10_13/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_d9_e2e_backup_2026_10_13\` 内 · 顶层族级移动不涉 |
| 1404 | `_d9_e2e_backup_2026_10_13/_s5doubleprime_five_lines_readings_2026_10_11.json` | `_d9_e2e_backup_2026_10_13/_s5doubleprime_five_lines_readings_2026_10_11.json`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_d9_e2e_backup_2026_10_13\` 内 · 顶层族级移动不涉 |
| 1405 | `_d9_e2e_backup_2026_10_13/_stage3_trigger_readings_items_2026_10_11.json` | `_d9_e2e_backup_2026_10_13/_stage3_trigger_readings_items_2026_10_11.json`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_d9_e2e_backup_2026_10_13\` 内 · 顶层族级移动不涉 |
| 1406 | `_d9_e2e_backup_2026_10_13/_v3_recheck_05_result_2026_09_28.json` | `_d9_e2e_backup_2026_10_13/_v3_recheck_05_result_2026_09_28.json`（**不动**） | _v* | 仓根锚定路径引用 | 已在子目录 `_d9_e2e_backup_2026_10_13\` 内 · 顶层族级移动不涉 |
| 1407 | `_d9_e2e_rerun_backup_2026_10_13/_s4_heldout_sampling_seedprime_items_2026_10_10.json` | `_d9_e2e_rerun_backup_2026_10_13/_s4_heldout_sampling_seedprime_items_2026_10_10.json`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_d9_e2e_rerun_backup_2026_10_13\` 内 · 顶层族级移动不涉 |
| 1408 | `_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_d1_ruling_and_s3_transition_2026_10_01.md` | `_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_d1_ruling_and_s3_transition_2026_10_01.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_glm_evidence_unpacked_2026_10_13/_september_workspace/results\` 内 · 顶层族级移动不涉 |
| 1409 | `_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_kv3s_3_2_terminal_verdict_2026_10_01.md` | `_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_kv3s_3_2_terminal_verdict_2026_10_01.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_glm_evidence_unpacked_2026_10_13/_september_workspace/results\` 内 · 顶层族级移动不涉 |
| 1410 | `_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_limb_reading_verdict_kv3s33_2026_10_01.md` | `_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_limb_reading_verdict_kv3s33_2026_10_01.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_glm_evidence_unpacked_2026_10_13/_september_workspace/results\` 内 · 顶层族级移动不涉 |
| 1411 | `_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_s3_d1_rulings_supplement_register_2026_10_01.md` | `_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_s3_d1_rulings_supplement_register_2026_10_01.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_glm_evidence_unpacked_2026_10_13/_september_workspace/results\` 内 · 顶层族级移动不涉 |
| 1412 | `_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_s3_d1fill_recount_2026_10_01.md` | `_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_s3_d1fill_recount_2026_10_01.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_glm_evidence_unpacked_2026_10_13/_september_workspace/results\` 内 · 顶层族级移动不涉 |
| 1413 | `_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_t1_gate_closure_and_recompute_verdict_2026_10_01.md` | `_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_t1_gate_closure_and_recompute_verdict_2026_10_01.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_glm_evidence_unpacked_2026_10_13/_september_workspace/results\` 内 · 顶层族级移动不涉 |
| 1414 | `_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_t1_substrate_gap_census_2026_10_01.md` | `_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_t1_substrate_gap_census_2026_10_01.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_glm_evidence_unpacked_2026_10_13/_september_workspace/results\` 内 · 顶层族级移动不涉 |
| 1415 | `_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_v3_s_prereg_v1_2026_09_27.md` | `_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_v3_s_prereg_v1_2026_09_27.md`（**不动**） | _v* | 相对路径引用 | 已在子目录 `_glm_evidence_unpacked_2026_10_13/_september_workspace/results\` 内 · 顶层族级移动不涉 |
| 1416 | `_glm_evidence_unpacked_2026_10_13/_september_workspace/results/deposon_g1_mindmap_demo.json` | `_glm_evidence_unpacked_2026_10_13/_september_workspace/results/deposon_g1_mindmap_demo.json`（**不动**） | deposon_* | 相对路径引用 | 已在子目录 `_glm_evidence_unpacked_2026_10_13/_september_workspace/results\` 内 · 顶层族级移动不涉 |
| 1417 | `_p_i_real_labels_2026_09_16/p_i_real_labels_results_2026_09_16.json` | `_p_i_real_labels_2026_09_16/p_i_real_labels_results_2026_09_16.json`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_p_i_real_labels_2026_09_16\` 内 · 顶层族级移动不涉 |
| 1418 | `_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json` | `_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_p_j_convergence_basin_2026_09_16\` 内 · 顶层族级移动不涉 |
| 1419 | `_p_l_p_c_finite_size_scaling_2026_09_16/p_l_p_c_finite_size_scaling_results_2026_09_16.json` | `_p_l_p_c_finite_size_scaling_2026_09_16/p_l_p_c_finite_size_scaling_results_2026_09_16.json`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_p_l_p_c_finite_size_scaling_2026_09_16\` 内 · 顶层族级移动不涉 |
| 1420 | `_p_l_real_data_collapse_2026_09_16/p_l_real_data_collapse_results_v2_2026_09_16.json` | `_p_l_real_data_collapse_2026_09_16/p_l_real_data_collapse_results_v2_2026_09_16.json`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_p_l_real_data_collapse_2026_09_16\` 内 · 顶层族级移动不涉 |
| 1421 | `_p_m_attack_surface_cost_2026_09_16/p_m_attack_surface_cost_results_2026_09_16.json` | `_p_m_attack_surface_cost_2026_09_16/p_m_attack_surface_cost_results_2026_09_16.json`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_p_m_attack_surface_cost_2026_09_16\` 内 · 顶层族级移动不涉 |
| 1422 | `_p_m_real_separation_2026_09_16/p_m_real_separation_results_2026_09_16.json` | `_p_m_real_separation_2026_09_16/p_m_real_separation_results_2026_09_16.json`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_p_m_real_separation_2026_09_16\` 内 · 顶层族级移动不涉 |
| 1423 | `_p_n_curvature_potential_coupling_2026_09_16/p_n_curvature_potential_coupling_results_2026_09_16.json` | `_p_n_curvature_potential_coupling_2026_09_16/p_n_curvature_potential_coupling_results_2026_09_16.json`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_p_n_curvature_potential_coupling_2026_09_16\` 内 · 顶层族级移动不涉 |
| 1424 | `_p_o_stranger_verification_2026_09_16/p_o_stranger_verification_results_2026_09_16.json` | `_p_o_stranger_verification_2026_09_16/p_o_stranger_verification_results_2026_09_16.json`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_p_o_stranger_verification_2026_09_16\` 内 · 顶层族级移动不涉 |
| 1425 | `_r5_spec_pack_retrieved_2026_10_13/鲍勃_minimax实验委托规格包_2026_10_12.md` | `_r5_spec_pack_retrieved_2026_10_13/鲍勃_minimax实验委托规格包_2026_10_12.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_r5_spec_pack_retrieved_2026_10_13\` 内 · 顶层族级移动不涉 |
| 1426 | `_v3_recheck_08b_executor/executor_2026_09_27.py` | `_v3_recheck_08b_executor/executor_2026_09_27.py`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_v3_recheck_08b_executor\` 内 · 顶层族级移动不涉 |
| 1427 | `_v3_recheck_08b_executor/rescript_2026_09_27.md` | `_v3_recheck_08b_executor/rescript_2026_09_27.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_v3_recheck_08b_executor\` 内 · 顶层族级移动不涉 |
| 1428 | `_v3_recheck_08b_executor/result_2026_09_27.json` | `_v3_recheck_08b_executor/result_2026_09_27.json`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_v3_recheck_08b_executor\` 内 · 顶层族级移动不涉 |
| 1429 | `_v3_recheck_08c_preexp_data/_v3_recheck_08c_sha12fix_r1_2026_10_12.py` | `_v3_recheck_08c_preexp_data/_v3_recheck_08c_sha12fix_r1_2026_10_12.py`（**不动**） | _v* | 仓根锚定路径引用 | 已在子目录 `_v3_recheck_08c_preexp_data\` 内 · 顶层族级移动不涉 |
| 1430 | `_v3_recheck_08c_preexp_data/executor_2026_09_27.py` | `_v3_recheck_08c_preexp_data/executor_2026_09_27.py`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_v3_recheck_08c_preexp_data\` 内 · 顶层族级移动不涉 |
| 1431 | `_v3_recheck_08c_preexp_data/rescript_2026_09_27.md` | `_v3_recheck_08c_preexp_data/rescript_2026_09_27.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_v3_recheck_08c_preexp_data\` 内 · 顶层族级移动不涉 |
| 1432 | `_v3_recheck_08c_preexp_data/result_2026_09_27.json` | `_v3_recheck_08c_preexp_data/result_2026_09_27.json`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_v3_recheck_08c_preexp_data\` 内 · 顶层族级移动不涉 |
| 1433 | `_v3_s1_executor/executor_2026_09_27.py` | `_v3_s1_executor/executor_2026_09_27.py`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_v3_s1_executor\` 内 · 顶层族级移动不涉 |
| 1434 | `_v3_s1_executor/rescript_2026_09_27.md` | `_v3_s1_executor/rescript_2026_09_27.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_v3_s1_executor\` 内 · 顶层族级移动不涉 |
| 1435 | `_v3_s1_executor/result_2026_09_27.json` | `_v3_s1_executor/result_2026_09_27.json`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_v3_s1_executor\` 内 · 顶层族级移动不涉 |
| 1436 | `_v3_s2_executor/executor_2026_09_27.py` | `_v3_s2_executor/executor_2026_09_27.py`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_v3_s2_executor\` 内 · 顶层族级移动不涉 |
| 1437 | `_v3_s2_executor/rescript_2026_09_27.md` | `_v3_s2_executor/rescript_2026_09_27.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_v3_s2_executor\` 内 · 顶层族级移动不涉 |
| 1438 | `_v3_s2_executor/result_2026_09_27.json` | `_v3_s2_executor/result_2026_09_27.json`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_v3_s2_executor\` 内 · 顶层族级移动不涉 |
| 1439 | `_v3_s3_wordexpand_data/executor_2026_09_28.py` | `_v3_s3_wordexpand_data/executor_2026_09_28.py`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_v3_s3_wordexpand_data\` 内 · 顶层族级移动不涉 |
| 1440 | `_v3_s3_wordexpand_data/executor_r1_2026_09_28.py` | `_v3_s3_wordexpand_data/executor_r1_2026_09_28.py`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_v3_s3_wordexpand_data\` 内 · 顶层族级移动不涉 |
| 1441 | `_v3_s3_wordexpand_data/rescript_2026_09_28.md` | `_v3_s3_wordexpand_data/rescript_2026_09_28.md`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_v3_s3_wordexpand_data\` 内 · 顶层族级移动不涉 |
| 1442 | `_v3_s3_wordexpand_data/rescript_r1_2026_09_28.md` | `_v3_s3_wordexpand_data/rescript_r1_2026_09_28.md`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_v3_s3_wordexpand_data\` 内 · 顶层族级移动不涉 |
| 1443 | `_v3_s3_wordexpand_data/result_2026_09_28.json` | `_v3_s3_wordexpand_data/result_2026_09_28.json`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_v3_s3_wordexpand_data\` 内 · 顶层族级移动不涉 |
| 1444 | `_v3_s_phrasetemplate_preexp_data/executor_2026_09_27.py` | `_v3_s_phrasetemplate_preexp_data/executor_2026_09_27.py`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_v3_s_phrasetemplate_preexp_data\` 内 · 顶层族级移动不涉 |
| 1445 | `_v3_s_phrasetemplate_preexp_data/rescript_2026_09_27.md` | `_v3_s_phrasetemplate_preexp_data/rescript_2026_09_27.md`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_v3_s_phrasetemplate_preexp_data\` 内 · 顶层族级移动不涉 |
| 1446 | `_v3_s_phrasetemplate_preexp_data/result_2026_09_27.json` | `_v3_s_phrasetemplate_preexp_data/result_2026_09_27.json`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_v3_s_phrasetemplate_preexp_data\` 内 · 顶层族级移动不涉 |
| 1447 | `_v3x_18frozen_remeasure_2026_09_16/v3x_18frozen_remeasure_results_2026_09_16.json` | `_v3x_18frozen_remeasure_2026_09_16/v3x_18frozen_remeasure_results_2026_09_16.json`（**不动**） | 无机械族界 | 仓根锚定路径引用 | 已在子目录 `_v3x_18frozen_remeasure_2026_09_16\` 内 · 顶层族级移动不涉 |
| 1448 | `_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json` | `_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_v3x_experiments_2026_09_16\` 内 · 顶层族级移动不涉 |
| 1449 | `_v3x_p_k_verify_2026_09_16/v3x_p_k_verify_results_2026_09_16.json` | `_v3x_p_k_verify_2026_09_16/v3x_p_k_verify_results_2026_09_16.json`（**不动**） | 无机械族界 | 相对路径引用 | 已在子目录 `_v3x_p_k_verify_2026_09_16\` 内 · 顶层族级移动不涉 |

---

## §5 计数与自报

| 量 | 值 |
| :-- |--: |
| 映射条目总数 | **1449** ＝ 顶层 **1316** ＋ 子目录内 **133**（与索引件之递归件数 **1449** 一一对应） |
| 其中「族级移动候选」条目（顶层件） | **1316** |
| 其中「候 PI 归族」条目 | **771** |
| 其中「保护面 · 不移动」条目 | **23** |
| 其中「仓根锚定路径引用（`K-SPLIT-3` 阻断面）」条目 | **701** |
| 拟新路径**已落盘**者 | **0**（⛔ 0 建目录 · ⛔ 0 执行移动） |

| 项 | 值 |
| :-- | :-- |
| 件路径 | `〔幽灵引用·未上传:_results_path_mapping_2026_10_21.md〕` |
| 编码 | UTF-8 **无 BOM** |
| 行尾 | **纯 LF**（CR ＝ 0） |
| TAB ／ VT ／ U+FFFD | 0 ／ 0 ／ 0 |
| SHA-12 ／ bytes | **落盘后独立回读实测，载于报回面**（自身指纹不可自含于件内） |
| 落盘后长名式复测 | **在盘**（见报回面） |
| 状态 | **拟案已落盘；档2 之移动俟 PI 逐单令** |
| 修订记录 | v1（2026-10-21 本棒首落盘）未载「自指污染面」排除声明；v2 升版补入 §0-4。本件**未**改动任何既有件一字（v1 为本棒自产件，其升版属本棒自身之产出修订）。 |

---

*本件为预案映射表（拟案面），非裁决件、非执行件。档2 之移动授权与执行皆不在本件射程。*
