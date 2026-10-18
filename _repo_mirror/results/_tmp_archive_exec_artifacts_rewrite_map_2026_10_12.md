# `.tmp` 实质执行件（A 档 14 件）迁移映射件（批 3 · 项 1 · PI 两裁「甲」）

> 📌 **状态栏**：🟢 **迁移已执行 · 引用面 ⛔ 0 回写** —— 本件＝PI 裁 `tmp_rewrite`＝**甲**「出映射件、不直接回写引用面」之唯一产物｜⛔ 0 回改任何既有件一字（含 §3 所列 13 件被引件）｜⛔ 0 删除任何件｜⛔ 0 触 `_non_upload_local_archive`（0 读 0 写 0 列目录）｜⛔ 0 网络／0 skill／0 LLM／0 读 `.env`／0 经手 PAT｜⛔ 0 触碰他棒产物

---

## §0 执行摘要（一句话）

**A 档 14 件已由 `.tmp\` 物理迁移至 `results\_archive_2026-10-12\exec_artifacts\`（PI 裁 `tmp_target`＝甲），逐件移动前后 SHA-12／bytes 之实测一致性 ＝ 14/14 一致（移动非改写之证）；引用面（迁移后实测 **70 处 ／ 13 件**）⛔ 0 直接回写 —— 本件仅出映射，待下游按需改引。**

| 摘要项 | 数量 | 依据 |
| :-: | :-: | :-: |
| 实移件数 | **14 / 14** | §2 逐件表 |
| 移动前后 SHA-12／bytes 一致 | **14 / 14** | §2 · §4 实测 |
| 新位实存件数 | **14**（恰等于所移之数，⛔ 0 多移） | §4 实测 |
| 旧位残留 | **0**（`.tmp\` 内 14 件均已不在原位） | §4 实测 |
| `.tmp` 计数 | **447 → 433（−14）** | §4 同脚本内前后实测 |
| 底本处置件指纹 | `3fdf474df1f9` ／ 12,836 B 前后**不变** | §4 实测 |
| 路径化引用处数（迁移后复扫） | **70**（A 组 57 ＋ B 组 10 ＋ C 组 3） | §3 |
| 引用面回写 | **⛔ 0 处**（PI 裁「不直接回写」） | §3-5 声明 |

---

## §1 PI 两裁（逐字 · 派工单转录）

| 项 | 内容 |
| :-: | :-: |
| 卡 | `ask_107219cdf0559ef87444541f` |
| **`tmp_target` ＝ 甲** | 目标子路径 **`results/_archive_2026-10-12/exec_artifacts/`** |
| **`tmp_rewrite` ＝ 甲** | **出映射件、不直接回写**引用面 |
| 效力 | 本棒依此二裁执行：迁移已执行（§2）；引用面**仅出映射、⛔ 0 编辑**（§3） |

📌 **逐字出处声明**：上表二裁之逐字**取自派工单对 PI 卡之转录**；本棒 ⛔ 0 读取原卡全文（PI 面／他棒面）⇒ 若与原卡有任何出入，**以原卡为准**。本棒 ⛔ 0 增补 PI 未明示之字面、⛔ 0 扩及二裁射程之外。

---

## §2 14 件逐件迁移映射表

**旧路径**＝`.tmp\<件名>`（原位，均平铺于 `.tmp\` 根）｜**新路径**＝`results\_archive_2026-10-12\exec_artifacts\<件名>`｜迁移方式＝`Move-Item`（⛔ 0 删除、⛔ 0 复制留副本）｜SHA-12 口径＝`sha256` 前 12 位小写（与底本 `3fdf474df1f9` 同口径，已实测对齐）。

| # | 件名 | 旧路径 | 新路径 | bytes | SHA-12 | 移动前 SHA-12／bytes | 移动后 SHA-12／bytes | 一致性 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| 1 | `c5_guard_minmaxstd_2026_10_01.py` | `.tmp\c5_guard_minmaxstd_2026_10_01.py` | `results\_archive_2026-10-12\exec_artifacts\c5_guard_minmaxstd_2026_10_01.py` | 15009 | `d74ff478993c` | `d74ff478993c` ／ 15009 | `d74ff478993c` ／ 15009 | ✅ 一致 |
| 2 | `exp06_supplement_probe_2026_10_10.py` | `.tmp\exp06_supplement_probe_2026_10_10.py` | `results\_archive_2026-10-12\exec_artifacts\exp06_supplement_probe_2026_10_10.py` | 7438 | `97076c37afa7` | `97076c37afa7` ／ 7438 | `97076c37afa7` ／ 7438 | ✅ 一致 |
| 3 | `exp06_independent_json_gen_2026_10_10.py` | `.tmp\exp06_independent_json_gen_2026_10_10.py` | `results\_archive_2026-10-12\exec_artifacts\exp06_independent_json_gen_2026_10_10.py` | 21560 | `5ce8f89c9396` | `5ce8f89c9396` ／ 21560 | `5ce8f89c9396` ／ 21560 | ✅ 一致 |
| 4 | `_exp06_fixcopy_verify_probe_2026_10_10.py` | `.tmp\_exp06_fixcopy_verify_probe_2026_10_10.py` | `results\_archive_2026-10-12\exec_artifacts\_exp06_fixcopy_verify_probe_2026_10_10.py` | 3598 | `680b6893f9f7` | `680b6893f9f7` ／ 3598 | `680b6893f9f7` ／ 3598 | ✅ 一致 |
| 5 | `scan_five_terminal_2026_10_10.py` | `.tmp\scan_five_terminal_2026_10_10.py` | `results\_archive_2026-10-12\exec_artifacts\scan_five_terminal_2026_10_10.py` | 4319 | `7200487fdab1` | `7200487fdab1` ／ 4319 | `7200487fdab1` ／ 4319 | ✅ 一致 |
| 6 | `_exp06_1009fix_build_2026_10_10.py` | `.tmp\_exp06_1009fix_build_2026_10_10.py` | `results\_archive_2026-10-12\exec_artifacts\_exp06_1009fix_build_2026_10_10.py` | 29412 | `e5acb3c0bca2` | `e5acb3c0bca2` ／ 29412 | `e5acb3c0bca2` ／ 29412 | ✅ 一致 |
| 7 | `_exp06_1009fix_lnref_2026_10_10.py` | `.tmp\_exp06_1009fix_lnref_2026_10_10.py` | `results\_archive_2026-10-12\exec_artifacts\_exp06_1009fix_lnref_2026_10_10.py` | 1508 | `9c7096147878` | `9c7096147878` ／ 1508 | `9c7096147878` ／ 1508 | ✅ 一致 |
| 8 | `e4_axis2_crosscheck_2026_10_10.py` | `.tmp\e4_axis2_crosscheck_2026_10_10.py` | `results\_archive_2026-10-12\exec_artifacts\e4_axis2_crosscheck_2026_10_10.py` | 3607 | `fbf93a534b99` | `fbf93a534b99` ／ 3607 | `fbf93a534b99` ／ 3607 | ✅ 一致 |
| 9 | `e4_axis2_denominator_recheck_2026_10_10.py` | `.tmp\e4_axis2_denominator_recheck_2026_10_10.py` | `results\_archive_2026-10-12\exec_artifacts\e4_axis2_denominator_recheck_2026_10_10.py` | 3833 | `5944efd3b68e` | `5944efd3b68e` ／ 3833 | `5944efd3b68e` ／ 3833 | ✅ 一致 |
| 10 | `e4_axis2_final_validation_2026_10_10.py` | `.tmp\e4_axis2_final_validation_2026_10_10.py` | `results\_archive_2026-10-12\exec_artifacts\e4_axis2_final_validation_2026_10_10.py` | 6489 | `8d2211f8ac91` | `8d2211f8ac91` ／ 6489 | `8d2211f8ac91` ／ 6489 | ✅ 一致 |
| 11 | `e4_axis2_hit_unchanged_probe_2026_10_10.py` | `.tmp\e4_axis2_hit_unchanged_probe_2026_10_10.py` | `results\_archive_2026-10-12\exec_artifacts\e4_axis2_hit_unchanged_probe_2026_10_10.py` | 2629 | `fc5d6bde78ad` | `fc5d6bde78ad` ／ 2629 | `fc5d6bde78ad` ／ 2629 | ✅ 一致 |
| 12 | `e4_axis2_v11_displacement_run_2026_10_10.py` | `.tmp\e4_axis2_v11_displacement_run_2026_10_10.py` | `results\_archive_2026-10-12\exec_artifacts\e4_axis2_v11_displacement_run_2026_10_10.py` | 10617 | `a950ae064fde` | `a950ae064fde` ／ 10617 | `a950ae064fde` ／ 10617 | ✅ 一致 |
| 13 | `_exp06_1009fix_lnref2_2026_10_10.py` | `.tmp\_exp06_1009fix_lnref2_2026_10_10.py` | `results\_archive_2026-10-12\exec_artifacts\_exp06_1009fix_lnref2_2026_10_10.py` | 1505 | `3ff21d556306` | `3ff21d556306` ／ 1505 | `3ff21d556306` ／ 1505 | ✅ 一致 |
| 14 | `_exp06_1009fix_verify_2026_10_10.py` | `.tmp\_exp06_1009fix_verify_2026_10_10.py` | `results\_archive_2026-10-12\exec_artifacts\_exp06_1009fix_verify_2026_10_10.py` | 7817 | `47fdf9673acc` | `47fdf9673acc` ／ 7817 | `47fdf9673acc` ／ 7817 | ✅ 一致 |

**小计**：bytes 合计 **119341**｜SHA-12 逐件唯一（⛔ 0 同名同哈希之疑）｜一致性 **14/14**。

---

## §3 路径化引用逐条清单（迁移后实测 70 处 ／ 13 件）

**扫描口径**：`deposon-repo` 递归、文本类扩展名、UTF-8 严格解码（⛔ 0 容错解码）、命中式＝字面 `.tmp` ＋ 分隔符（`\` 或 `/`）＋ 14 件名之一；实扫文本件 **1337** 件（⛔ 0 列目录 `_non_upload_local_archive`、⛔ 0 扫 `.tmp\` 本体）。行号为 **1-based 实测行号**。

### §3-1 三组计数与底本之关系

| 组 | 处数 | 文件数 | 说明 |
| :-: | :-: | :-: | :-: |
| **A 组**（底本计入之项） | **57** | **10** | 与处置底本 §5「路径化引用 57 处 ／ `results` 10 件」**逐件逐数一致** |
| **B 组**（底本落盘后新增） | **10** | **1** | 全在 `results/_corpus_index_citation_surface_annotation_2026_10_12.md` —— **他棒产物面**（底本落盘后由另一棒产出，故未计入底本之 57） |
| **C 组**（迁移件自身内容内） | **3** | **2** | 位于新位 14 件之**内容字符串**中（底本扫描面不含新位目录，故未计入其 57） |
| **合计** | **70** | **13** | ⛔ 0 遗漏、⛔ 0 臆增 |

📌 **底本 57 之复核实况**：A 组 **57** 处 ／ **10** 件，与底本 §5 分布表（`_repo_post_cleanup_snapshot_*` 14／`_achievements_inventory_full_*` 13／`_repo_full_inventory_catalogue_*` 13／`_exp06_selfverified_renaming_note_*` 6／`_exp06_supplement_four_gaps_*` 3／`_exp06_independent_check_*` 2／`_exp06_selfverified_runner_fix_note_*` 2／`c5_guard_minmaxstd_report_*` 2／`c5_guard_minmaxstd_readings_*` 1／`_five_terminal_judgments_ruling_*` 1＝57）**逐数吻合**。

### §3-2 改引式样

**原文式**＝该行命中之逐字字面（含其原有分隔符）｜**应改为之新式**＝分隔符沿该处既有风格保留之新路径。**规范式**（下游若愿统一，可全量采用）：`results/_archive_2026-10-12/exec_artifacts/<件名>`。

### §3-3 A 组逐条清单（57 处 ／ 10 件 · `results\` 面既有件）

| # | 引用者件 | 行号 | 原文式（逐字命中） | 应改为之新式 |
| :-: | :-: | :-: | :-: | :-: |
| 1 | `results/_achievements_inventory_full_2026_10_09.md` | 2946 | `.tmp/exp06_supplement_probe_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/exp06_supplement_probe_2026_10_10.py` |
| 2 | `results/_achievements_inventory_full_2026_10_09.md` | 2947 | `.tmp/exp06_independent_json_gen_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/exp06_independent_json_gen_2026_10_10.py` |
| 3 | `results/_achievements_inventory_full_2026_10_09.md` | 2955 | `.tmp/_exp06_fixcopy_verify_probe_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/_exp06_fixcopy_verify_probe_2026_10_10.py` |
| 4 | `results/_achievements_inventory_full_2026_10_09.md` | 2969 | `.tmp/_exp06_1009fix_verify_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/_exp06_1009fix_verify_2026_10_10.py` |
| 5 | `results/_achievements_inventory_full_2026_10_09.md` | 2971 | `.tmp/_exp06_1009fix_lnref_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/_exp06_1009fix_lnref_2026_10_10.py` |
| 6 | `results/_achievements_inventory_full_2026_10_09.md` | 2972 | `.tmp/_exp06_1009fix_lnref2_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/_exp06_1009fix_lnref2_2026_10_10.py` |
| 7 | `results/_achievements_inventory_full_2026_10_09.md` | 2973 | `.tmp/_exp06_1009fix_build_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/_exp06_1009fix_build_2026_10_10.py` |
| 8 | `results/_achievements_inventory_full_2026_10_09.md` | 3024 | `.tmp/scan_five_terminal_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/scan_five_terminal_2026_10_10.py` |
| 9 | `results/_achievements_inventory_full_2026_10_09.md` | 3091 | `.tmp/e4_axis2_v11_displacement_run_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/e4_axis2_v11_displacement_run_2026_10_10.py` |
| 10 | `results/_achievements_inventory_full_2026_10_09.md` | 3093 | `.tmp/e4_axis2_denominator_recheck_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/e4_axis2_denominator_recheck_2026_10_10.py` |
| 11 | `results/_achievements_inventory_full_2026_10_09.md` | 3094 | `.tmp/e4_axis2_crosscheck_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/e4_axis2_crosscheck_2026_10_10.py` |
| 12 | `results/_achievements_inventory_full_2026_10_09.md` | 3095 | `.tmp/e4_axis2_final_validation_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/e4_axis2_final_validation_2026_10_10.py` |
| 13 | `results/_achievements_inventory_full_2026_10_09.md` | 3097 | `.tmp/e4_axis2_hit_unchanged_probe_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/e4_axis2_hit_unchanged_probe_2026_10_10.py` |
| 14 | `results/_exp06_independent_check_2026_10_10.json` | 394 | `.tmp/c5_guard_minmaxstd_2026_10_01.py` | `results/_archive_2026-10-12/exec_artifacts/c5_guard_minmaxstd_2026_10_01.py` |
| 15 | `results/_exp06_independent_check_2026_10_10.json` | 394 | `.tmp/exp06_supplement_probe_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/exp06_supplement_probe_2026_10_10.py` |
| 16 | `results/_exp06_selfverified_renaming_note_2026_10_10.md` | 24 | `.tmp/_exp06_1009fix_build_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/_exp06_1009fix_build_2026_10_10.py` |
| 17 | `results/_exp06_selfverified_renaming_note_2026_10_10.md` | 25 | `.tmp/_exp06_1009fix_verify_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/_exp06_1009fix_verify_2026_10_10.py` |
| 18 | `results/_exp06_selfverified_renaming_note_2026_10_10.md` | 26 | `.tmp/_exp06_1009fix_lnref_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/_exp06_1009fix_lnref_2026_10_10.py` |
| 19 | `results/_exp06_selfverified_renaming_note_2026_10_10.md` | 348 | `.tmp/_exp06_1009fix_build_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/_exp06_1009fix_build_2026_10_10.py` |
| 20 | `results/_exp06_selfverified_renaming_note_2026_10_10.md` | 348 | `.tmp/_exp06_1009fix_verify_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/_exp06_1009fix_verify_2026_10_10.py` |
| 21 | `results/_exp06_selfverified_renaming_note_2026_10_10.md` | 348 | `.tmp/_exp06_fixcopy_verify_probe_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/_exp06_fixcopy_verify_probe_2026_10_10.py` |
| 22 | `results/_exp06_selfverified_runner_fix_note_2026_10_10.md` | 213 | `.tmp/_exp06_fixcopy_verify_probe_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/_exp06_fixcopy_verify_probe_2026_10_10.py` |
| 23 | `results/_exp06_selfverified_runner_fix_note_2026_10_10.md` | 213 | `.tmp/c5_guard_minmaxstd_2026_10_01.py` | `results/_archive_2026-10-12/exec_artifacts/c5_guard_minmaxstd_2026_10_01.py` |
| 24 | `results/_exp06_supplement_four_gaps_2026_10_10.md` | 7 | `.tmp/c5_guard_minmaxstd_2026_10_01.py` | `results/_archive_2026-10-12/exec_artifacts/c5_guard_minmaxstd_2026_10_01.py` |
| 25 | `results/_exp06_supplement_four_gaps_2026_10_10.md` | 7 | `.tmp/exp06_independent_json_gen_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/exp06_independent_json_gen_2026_10_10.py` |
| 26 | `results/_exp06_supplement_four_gaps_2026_10_10.md` | 7 | `.tmp/exp06_supplement_probe_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/exp06_supplement_probe_2026_10_10.py` |
| 27 | `results/_five_terminal_judgments_ruling_2026_10_10.md` | 86 | `.tmp/scan_five_terminal_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/scan_five_terminal_2026_10_10.py` |
| 28 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2482 | `.tmp\e4_axis2_hit_unchanged_probe_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\e4_axis2_hit_unchanged_probe_2026_10_10.py` |
| 29 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2485 | `.tmp\e4_axis2_final_validation_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\e4_axis2_final_validation_2026_10_10.py` |
| 30 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2487 | `.tmp\e4_axis2_crosscheck_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\e4_axis2_crosscheck_2026_10_10.py` |
| 31 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2488 | `.tmp\e4_axis2_denominator_recheck_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\e4_axis2_denominator_recheck_2026_10_10.py` |
| 32 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2491 | `.tmp\e4_axis2_v11_displacement_run_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\e4_axis2_v11_displacement_run_2026_10_10.py` |
| 33 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2571 | `.tmp\scan_five_terminal_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\scan_five_terminal_2026_10_10.py` |
| 34 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2624 | `.tmp\_exp06_1009fix_build_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\_exp06_1009fix_build_2026_10_10.py` |
| 35 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2625 | `.tmp\_exp06_1009fix_lnref2_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\_exp06_1009fix_lnref2_2026_10_10.py` |
| 36 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2626 | `.tmp\_exp06_1009fix_lnref_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\_exp06_1009fix_lnref_2026_10_10.py` |
| 37 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2628 | `.tmp\_exp06_1009fix_verify_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\_exp06_1009fix_verify_2026_10_10.py` |
| 38 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2642 | `.tmp\_exp06_fixcopy_verify_probe_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\_exp06_fixcopy_verify_probe_2026_10_10.py` |
| 39 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2650 | `.tmp\exp06_independent_json_gen_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\exp06_independent_json_gen_2026_10_10.py` |
| 40 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2651 | `.tmp\exp06_supplement_probe_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\exp06_supplement_probe_2026_10_10.py` |
| 41 | `results/_repo_post_cleanup_snapshot_2026_10_12.md` | 169 | `.tmp\_exp06_1009fix_build_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\_exp06_1009fix_build_2026_10_10.py` |
| 42 | `results/_repo_post_cleanup_snapshot_2026_10_12.md` | 170 | `.tmp\_exp06_1009fix_lnref_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\_exp06_1009fix_lnref_2026_10_10.py` |
| 43 | `results/_repo_post_cleanup_snapshot_2026_10_12.md` | 171 | `.tmp\_exp06_1009fix_lnref2_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\_exp06_1009fix_lnref2_2026_10_10.py` |
| 44 | `results/_repo_post_cleanup_snapshot_2026_10_12.md` | 172 | `.tmp\_exp06_1009fix_verify_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\_exp06_1009fix_verify_2026_10_10.py` |
| 45 | `results/_repo_post_cleanup_snapshot_2026_10_12.md` | 173 | `.tmp\_exp06_fixcopy_verify_probe_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\_exp06_fixcopy_verify_probe_2026_10_10.py` |
| 46 | `results/_repo_post_cleanup_snapshot_2026_10_12.md` | 465 | `.tmp\c5_guard_minmaxstd_2026_10_01.py` | `results/_archive_2026-10-12/exec_artifacts\c5_guard_minmaxstd_2026_10_01.py` |
| 47 | `results/_repo_post_cleanup_snapshot_2026_10_12.md` | 473 | `.tmp\e4_axis2_crosscheck_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\e4_axis2_crosscheck_2026_10_10.py` |
| 48 | `results/_repo_post_cleanup_snapshot_2026_10_12.md` | 474 | `.tmp\e4_axis2_denominator_recheck_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\e4_axis2_denominator_recheck_2026_10_10.py` |
| 49 | `results/_repo_post_cleanup_snapshot_2026_10_12.md` | 475 | `.tmp\e4_axis2_final_validation_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\e4_axis2_final_validation_2026_10_10.py` |
| 50 | `results/_repo_post_cleanup_snapshot_2026_10_12.md` | 476 | `.tmp\e4_axis2_hit_unchanged_probe_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\e4_axis2_hit_unchanged_probe_2026_10_10.py` |
| 51 | `results/_repo_post_cleanup_snapshot_2026_10_12.md` | 477 | `.tmp\e4_axis2_v11_displacement_run_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\e4_axis2_v11_displacement_run_2026_10_10.py` |
| 52 | `results/_repo_post_cleanup_snapshot_2026_10_12.md` | 479 | `.tmp\exp06_independent_json_gen_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\exp06_independent_json_gen_2026_10_10.py` |
| 53 | `results/_repo_post_cleanup_snapshot_2026_10_12.md` | 480 | `.tmp\exp06_supplement_probe_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\exp06_supplement_probe_2026_10_10.py` |
| 54 | `results/_repo_post_cleanup_snapshot_2026_10_12.md` | 497 | `.tmp\scan_five_terminal_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts\scan_five_terminal_2026_10_10.py` |
| 55 | `results/c5_guard_minmaxstd_readings_2026_10_01.json` | 5 | `.tmp/c5_guard_minmaxstd_2026_10_01.py` | `results/_archive_2026-10-12/exec_artifacts/c5_guard_minmaxstd_2026_10_01.py` |
| 56 | `results/c5_guard_minmaxstd_report_2026_10_01.md` | 6 | `.tmp/c5_guard_minmaxstd_2026_10_01.py` | `results/_archive_2026-10-12/exec_artifacts/c5_guard_minmaxstd_2026_10_01.py` |
| 57 | `results/c5_guard_minmaxstd_report_2026_10_01.md` | 198 | `.tmp/c5_guard_minmaxstd_2026_10_01.py` | `results/_archive_2026-10-12/exec_artifacts/c5_guard_minmaxstd_2026_10_01.py` |

### §3-4 B 组逐条清单（10 处 ／ 1 件 · 他棒产物面）

| # | 引用者件 | 行号 | 原文式（逐字命中） | 应改为之新式 |
| :-: | :-: | :-: | :-: | :-: |
| 1 | `results/_corpus_index_citation_surface_annotation_2026_10_12.md` | 118 | `.tmp/_exp06_1009fix_build_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/_exp06_1009fix_build_2026_10_10.py` |
| 2 | `results/_corpus_index_citation_surface_annotation_2026_10_12.md` | 119 | `.tmp/_exp06_1009fix_verify_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/_exp06_1009fix_verify_2026_10_10.py` |
| 3 | `results/_corpus_index_citation_surface_annotation_2026_10_12.md` | 120 | `.tmp/_exp06_fixcopy_verify_probe_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/_exp06_fixcopy_verify_probe_2026_10_10.py` |
| 4 | `results/_corpus_index_citation_surface_annotation_2026_10_12.md` | 129 | `.tmp/c5_guard_minmaxstd_2026_10_01.py` | `results/_archive_2026-10-12/exec_artifacts/c5_guard_minmaxstd_2026_10_01.py` |
| 5 | `results/_corpus_index_citation_surface_annotation_2026_10_12.md` | 176 | `.tmp/_exp06_1009fix_build_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/_exp06_1009fix_build_2026_10_10.py` |
| 6 | `results/_corpus_index_citation_surface_annotation_2026_10_12.md` | 177 | `.tmp/_exp06_1009fix_verify_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/_exp06_1009fix_verify_2026_10_10.py` |
| 7 | `results/_corpus_index_citation_surface_annotation_2026_10_12.md` | 186 | `.tmp/exp06_independent_json_gen_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/exp06_independent_json_gen_2026_10_10.py` |
| 8 | `results/_corpus_index_citation_surface_annotation_2026_10_12.md` | 187 | `.tmp/exp06_supplement_probe_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/exp06_supplement_probe_2026_10_10.py` |
| 9 | `results/_corpus_index_citation_surface_annotation_2026_10_12.md` | 255 | `.tmp/_exp06_1009fix_build_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/_exp06_1009fix_build_2026_10_10.py` |
| 10 | `results/_corpus_index_citation_surface_annotation_2026_10_12.md` | 256 | `.tmp/_exp06_1009fix_verify_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/_exp06_1009fix_verify_2026_10_10.py` |

### §3-4-C C 组逐条清单（3 处 ／ 2 件 · 迁移件自身内容内）

| # | 引用者件（新位） | 行号 | 原文式（逐字命中） | 应改为之新式 |
| :-: | :-: | :-: | :-: | :-: |
| 1 | `results/_archive_2026-10-12/exec_artifacts/c5_guard_minmaxstd_2026_10_01.py` | 265 | `.tmp/c5_guard_minmaxstd_2026_10_01.py` | `results/_archive_2026-10-12/exec_artifacts/c5_guard_minmaxstd_2026_10_01.py` |
| 2 | `results/_archive_2026-10-12/exec_artifacts/exp06_independent_json_gen_2026_10_10.py` | 306 | `.tmp/c5_guard_minmaxstd_2026_10_01.py` | `results/_archive_2026-10-12/exec_artifacts/c5_guard_minmaxstd_2026_10_01.py` |
| 3 | `results/_archive_2026-10-12/exec_artifacts/exp06_independent_json_gen_2026_10_10.py` | 306 | `.tmp/exp06_supplement_probe_2026_10_10.py` | `results/_archive_2026-10-12/exec_artifacts/exp06_supplement_probe_2026_10_10.py` |

### §3-5 ⛔ 0 直接回写之声明

**本棒 ⛔ 0 编辑上述 13 件被引件之任何一字** —— 依 PI 裁 `tmp_rewrite`＝**甲**「**出映射件、不直接回写**引用面」：本件**仅出映射**，§3 全部 70 条「应改为之新式」**均为待改之建议、非既成之改写**；实际改引**归属下游棒**（底本 §8-① 之「引用面回写」仍**须 PI 明确**归属 §1-2 之棒抑或另派）。

📌 **B 组之特殊约束**：`results/_corpus_index_citation_surface_annotation_2026_10_12.md` 系**他棒产物面**（本棒 0 触碰、0 编辑）；若下游棒回写，⛔ 0 覆盖该棒之登记语义（其行文系对 `.tmp` 引用面之**登记**，改动须与其归属棒协调）。

📌 **C 组之特殊约束**：3 处系**迁移件自身内容**中之输出字符串（脚本运行时写入 readings JSON 之字面）。本棒⛔ 0 编辑之 —— 既因硬约束 `⛔ 0 回改任何既有件`，亦因其一改即**破坏 §2 之「移动非改写」实证**（14/14 指纹一致将失据）。且该等字面系**运行时产物之来源记录**，改之即改其陈述内容 ⇒ 处置须另议，本棒 ⛔ 0 代裁。

📌 **遗漏式提及（非路径化、路径化改引不适用）**：迁移后复扫另见**省略式**提及（如 `_exp06_selfverified_renaming_note_2026_10_10.md` L26 之 `…_lnref2_…py`）—— 此类 ⛔ 0 属 `.tmp` 路径式，**改引不适用**，但其**语义指向**同样随迁移而变（见 §6-②）。

---

## §4 迁移前后盘面实测

| 测项 | 迁移前 | 迁移后 | 变化 |
| :-: | :-: | :-: | :-: |
| A 档 14 件所位 | 全部存在于 `.tmp\` | 全部存在于 `results\_archive_2026-10-12\exec_artifacts\` | **14 件迁移** |
| 新位目录 | **不存在**（0 同名冲突） | **新建**、恰含 14 件 | +1 目录 |
| `.tmp` 件数（同脚本内前后实测） | **447** | **433** | **−14** |
| 底本处置件 `results\_tmp_archive_disposition_register_2026_10_12.md` | `3fdf474df1f9` ／ 12,836 B | `3fdf474df1f9` ／ 12,836 B | **0 变更**（0 回改之实证） |
| 被引 11 件（引用面） | — | 见 §4-1（0 写入旁证） | **0 变更** |
| 被引 2 件（迁移件自身） | 与 `.tmp\` 时同 SHA-12 | 与移动前同 SHA-12 | **0 改写**（纯移动） |

### §4-1 被引 13 件之指纹与 mtime

| 被引件 | 类别 | SHA-12 | bytes | mtime |
| :-: | :-: | :-: | :-: | :-: |
| `results/_achievements_inventory_full_2026_10_09.md` | 引用面 | `dd3e9806a369` | 372318 | 2026-10-12 03:20:49 |
| `results/_archive_2026-10-12/exec_artifacts/c5_guard_minmaxstd_2026_10_01.py` | 迁移件自身 | `d74ff478993c` | 15009 | 2026-10-01 10:14:05 |
| `results/_archive_2026-10-12/exec_artifacts/exp06_independent_json_gen_2026_10_10.py` | 迁移件自身 | `5ce8f89c9396` | 21560 | 2026-10-10 10:31:30 |
| `results/_corpus_index_citation_surface_annotation_2026_10_12.md` | 引用面 | `402b1f2754e9` | 28951 | 2026-10-12 21:18:57 |
| `results/_exp06_independent_check_2026_10_10.json` | 引用面 | `4c36c376ab9c` | 20480 | 2026-10-10 10:31:42 |
| `results/_exp06_selfverified_renaming_note_2026_10_10.md` | 引用面 | `8b4ec41a37dd` | 34554 | 2026-10-10 11:25:56 |
| `results/_exp06_selfverified_runner_fix_note_2026_10_10.md` | 引用面 | `247398b687e6` | 17052 | 2026-10-10 10:51:43 |
| `results/_exp06_supplement_four_gaps_2026_10_10.md` | 引用面 | `9f86cc5be8e9` | 26519 | 2026-10-10 10:33:13 |
| `results/_five_terminal_judgments_ruling_2026_10_10.md` | 引用面 | `9e96d0a1ba12` | 27315 | 2026-10-10 12:28:00 |
| `results/_repo_full_inventory_catalogue_2026_10_12.md` | 引用面 | `96720fcfd76a` | 591833 | 2026-10-12 02:11:15 |
| `results/_repo_post_cleanup_snapshot_2026_10_12.md` | 引用面 | `6039a6e08017` | 309419 | 2026-10-12 03:09:29 |
| `results/c5_guard_minmaxstd_readings_2026_10_01.json` | 引用面 | `7ff301514f66` | 19935 | 2026-10-01 10:14:10 |
| `results/c5_guard_minmaxstd_report_2026_10_01.md` | 引用面 | `f465fbdb7579` | 19909 | 2026-10-01 10:15:08 |

📌 **引用面 11 件**之 mtime 全部早于本棒起动（21:2x）⇒ 本棒对其**0 次打开写入**，唯一接触为读取扫描；**迁移件自身 2 件**之 mtime 系 `Move-Item` 所保留之**原修改时间**（非本棒落笔时间），且 SHA-12 与移动前实测一致 ⇒ 内容 0 变更。

---

## §5 ⛔ 0 删除声明

**本棒 ⛔ 0 删除任何件** —— `.tmp` 内 0 删除、仓内 0 删除、目标目录 0 删除；移动系 `Move-Item`（**非复制、非删除**），14 件实体存续于新位且指纹不变。**⛔ 0 留副本**：旧位 14 件均已不在原位（`STILL_IN_TMP = 0`）⇒ 不存在「一物两处」之歧义态。

---

## §6 未决项

① 🔴 **引用面回写之归属与时点未定** —— 迁移后实测 **70 处 ／ 13 件**仍指旧路径 `.tmp\...`，即**迁移已成、断链即在**；PI 裁「不直接回写」⇒ 未另派棒前此 70 处**持续失效**。归属（底本 §8-① 之 §1-2 之棒 vs 另派）仍**须 PI 明确**。

② 🟡 **裸名引用（底本 §5 载 77 处）语义指向失效** —— ⛔ 无 `.tmp` 前缀，路径化改引**不覆盖**之；迁移后仍可按名解析但**语义指向已变**（新位置不在 `.tmp`）⇒ 须与 §3 一并处置，抑或明确接受。**本棒 ⛔ 0 代行重扫裁定**（不扩及 PI 未明示之动作面）。

③ 🟡 **C 组 3 处之处置待另议** —— 迁移件内容内之旧路径字面，改之即破坏「移动非改写」之实证（§2），且系运行时产物之来源记录（§3-5）⇒ 须 PI/下游裁定其归属（登记勘误 vs 保留原字面）。

④ 🟡 **B 档计数口径仍陈旧、且差额来源不明** —— 承底本 §8-④：`.tmp` 为**活动面**，本棒起动前 20 分钟内即实测 **445 → 446 → 447** 连续变动；本棒迁移后为 **433**。甲档「429」之口径**已陈旧**；底本时点即存之 **1 件差额来源不明**，本棒 ⛔ 0 代为归类。

⑤ 🟡 **他棒产物面之登记语义耦合** —— B 组 10 处位于 `results/_corpus_index_citation_surface_annotation_2026_10_12.md`；其行文系对 `.tmp` 引用面之**登记**，回写须与其归属棒协调，⛔ 0 单方覆盖。

⑥ 🟢 **0 未决之外项** —— 迁移动作面 PI 已两裁明确，本棒**无待裁项**；本件亦为 §1-2「索引引用迁移」范围外之独立交付（⛔ 0 代行 §1-2）。

---

> 📌 **交棒声明**：本件＝PI `tmp_rewrite`＝甲「出映射件」之产物；**迁移已执行**（14/14 指纹一致，§2）｜**引用面 ⛔ 0 回写**（§3-5，70 条改引建议待下游棒）｜⛔ 0 删除｜⛔ 0 回改任何既有件（底本 `3fdf474df1f9` 与引用面 11 件 0 变更，§4）｜目标路径取自 PI `tmp_target`＝甲，⛔ 0 自拟。
