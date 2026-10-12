# 大批量文件夹整理与清噪声 · 执行登记（③段收尾桶）

> **状态栏**：✅ **已执行**（PI 2026-10-12 逐字令：「还包括清噪声呢，收尾桶要大批量整理文件夹，以致 repo 与 sub 目录下文件数差不多，记得更新清单」）
> **执行时点**：2026-10-12 02:33–03:00 (+08:00)｜**执行体**：evidence-auditor｜**通道**：清噪声＝顶层 ``rm --`（mavis-trash → 回收站，可恢复）；转移＝同卷 Move-Item ＋ 逐件 SHA-256 复算
> **前置**：⛔ 0 触及 `_non_upload_local_archive`（0 读 0 写 0 列目录）｜⛔ 0 动作于 `Deposon_v1_2_0_交付包`（仅列提案）｜⛔ 0 覆写既有件｜⛔ 0 回改任何既有件正文一字

---

## 1. 两区拉平前后对照（实测）

| 区 | 前·件数 | 前·bytes | 后·件数 | 后·bytes | 件数变化 | bytes 变化 |
|---|---|---|---|---|---|---|
| `deposon-repo` | 2,541 | 90,366,407 | **1,698** | 54,244,446 | −843 | −36,121,961 |
| `deposon-sub` | 517 | 35,047,715 | **1,187** | 58,731,756 | +670 | +23,684,041 |
| **合计** | 3,058 | 125,414,122 | 2,885 | 112,976,202 | −173 | −12,437,920 |

- **件数比**：前 `4.91 : 1` → 后 **`1.43 : 1`**
- **目标值（草案·候 PI 追认）**：两区件数比 **≤ 1.50 : 1**
- **达成度**：实测 1.43 : 1，**达成**（余量 0.07）
- **理想值 1:1 未达成之根因（如实登记，非推断）**：`deposon-repo/results` 内 **600 件**被**在册活代码按绝对路径钉住**，例 ``results/_t1_exp2_executor_2026_10_09.py:57-59`：`ROOT = Path('_september_workspace')` / `RESULTS_DIR = ROOT / 'results'` / `TMP_DIR = ROOT / '.tmp'`。移动即断链，故 ⛔ 不动。

---

## 2. 断链防护：引用链评估方法与结论

**判据（功能性引用，非清单列举行数）** —— 沿既有 token 查表法，全量分词建索引：

- **FUNC_REF（功能性）** ＝ 活代码（`.py`/`.ps1`/`.sh`/`.bat`/`.js`/`.ts`，排除 `tmp_movedout_*` 历史归档脚本）正文按文件名引用 → **阻断**
- **LIST_ONLY（仅列举）** ＝ 台账/清单/manifest/回函按名列举（例 `_repo_full_inventory_catalogue_2026_10_12.md` 命中 146 件、`_v4_maindir_cleanup_moves_ledger_v2_2026_09_24.md` 命中 62 件）→ **不阻断**，但转移件须出映射条目

> ⚠ **既有事故防重演**：首轮扫描曾因 `.tmp/receipt_disp_idx.txt`（6,876,782 B）等**全仓清单件逐行列举**导致「每件都被误判为有引用」。本棒以「功能性 vs 仅列举」二分消解，全量 3,058 件分词建索引后：unreferenced 168／doc_only 1,747／code_ref 1,143。

**转移件引用强度**：723 件转移标的 **CodeRefs ＝ 0（0 件被活代码引用）**；其中 DocRefs>0 者 **723 件**（全部须出映射条目）。

**映射表条目数**：**723**（全量见 `5，逐条「旧路径 → 新路径」）

---

## 3. 清噪声登记（174 件 · 全走可恢复通道）

**通道执行**：一律顶层 ``rm --` ＋ **字面绝对路径**＋ **前斜杠**；⛔ 0 传 PowerShell 变量；⛔ 0 裸 `Remove-Item`。**回收站可恢复性：全部经 `mavis-trash`，逐件输出 `moved to trash`，可恢复。**

### 3.1 分类小计

| 类别 | 件数 | bytes | 判据 |
|---|---|---|---|
| A `._moved_20260924_1830.*` 同哈希冗余副本（sub） | 53 | 483,049 | 同目录存在逐位全等孪生件，孤儿数 0 |
| B 0 字节件 | 2 | 0 | 无内容 |
| C 畸形名件 `` | 1 | 898 | PowerShell 重定向残留的畸形文件名 |
| E `.tmp` 中间件（仅列举引用） | 118 | 11,965,132 | CodeRefs=0 且非代码/非 md/非成果面名 |
| **合计** | **174** | **12,449,079** | |

### 3.2 因引用或铁律而**保留未清**（54 件，如实登记）

| 保留理由 | 件数 | 说明 |
|---|---|---|
| FUNC_REF | 17 | 被 ``results/` 内活执行体按绝对路径读取，清走即断链 |
| CODE_PROTECTED | 15 | `*.py`（含 9 件 `._moved_20260924_1830.py` 冗余副本）＋ `.ps1`，铁律 ⛔ 0 动 |
| RESULT_FACE_GUARD | 14 | 文件名含 verdict/register/audit/erratum/check/裁定/终判/判死/勘误/核查/登记 等成果面字样 |
| MD_PROTECTED | 8 | `.tmp` 内 `.md` 成稿件 |

### 3.3 逐件登记

| # | 源路径 | SHA-12 | bytes | 类别 | 断链评估 | 可恢复性 |
|---|---|---|---|---|---|---|
| 1 | `_september_workspace/$null` | `400d7e27b03f` | 898 | C 畸形名 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 2 | `_september_workspace/.tmp/_abc_final_2026_10_10.json` | `5f4c2f499620` | 1291 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 3 | `_september_workspace/.tmp/_abc_h1h2_out_2026_10_10.json` | `068be36a60d8` | 4922 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 4 | `_september_workspace/.tmp/_c5_b_prestate_baseline.json` | `09f27c6c1869` | 1543 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 5 | `_september_workspace/.tmp/_c5_b3_utf8_out.txt` | `29de7d0acf02` | 933 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 6 | `_september_workspace/.tmp/_cards_35_48_full.txt` | `8d99789c1999` | 120330 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 7 | `_september_workspace/.tmp/_ci_gap_fill_alt_bc_aper_prime_2026_10_09.log` | `f258ae241deb` | 2360 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 8 | `_september_workspace/.tmp/_ci_gap_fill_err.txt` | `e3b0c44298fc` | 0 | B 0字节 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 9 | `_september_workspace/.tmp/_ci_gap_fill_out.txt` | `353dc9df9650` | 11040 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 10 | `_september_workspace/.tmp/_claude_reply_view.txt` | `54bddf32f9df` | 23246 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 11 | `_september_workspace/.tmp/_cpatomic_keyscan_2026_09_28.json` | `b4e45cffa5cd` | 2672 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 12 | `_september_workspace/.tmp/_cpatomic_patch_manifest_2026_09_28.json` | `cdb8ebc2ece3` | 357 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 13 | `_september_workspace/.tmp/_cpatomic_pycache_post_2026_09_28.json` | `1eb3c5c9c62d` | 6476 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 14 | `_september_workspace/.tmp/_cpatomic_pycache_pre_2026_09_28.json` | `0f62453472b7` | 10772 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 15 | `_september_workspace/.tmp/_cpatomic_verify_2026_09_28.json` | `6b820f7da4a4` | 3144 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 16 | `_september_workspace/.tmp/_d05_caliber_out_2026_10_10.json` | `080606669599` | 1725 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 17 | `_september_workspace/.tmp/_d05_detail.txt` | `6cb5d73bd8da` | 3017 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 18 | `_september_workspace/.tmp/_d05_s4only_out_2026_10_10.json` | `fa0907234347` | 427 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 19 | `_september_workspace/.tmp/_d05_summary.json` | `12655f3523c4` | 1144 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 20 | `_september_workspace/.tmp/_d4_relabel_run1.log` | `97b5245deac3` | 1158 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 21 | `_september_workspace/.tmp/_diff21_anchor_drift.txt` | `fb648f327945` | 20994 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 22 | `_september_workspace/.tmp/_disp.json` | `076648de25ff` | 3484 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 23 | `_september_workspace/.tmp/_e3536.txt` | `e28953f7623b` | 2248 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 24 | `_september_workspace/.tmp/_e6_alt_permp_closure_raw_2026_10_10.json` | `c48395e135fd` | 8345 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 25 | `_september_workspace/.tmp/_e6_ndjt_recompute_out_2026_10_10.json` | `6499760993bf` | 7005 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 26 | `_september_workspace/.tmp/_enc_test.txt` | `b1e6f7046a46` | 67 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 27 | `_september_workspace/.tmp/_exp03_blade_recompute_out_2026_10_10.json` | `3d7de35263f8` | 19719 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 28 | `_september_workspace/.tmp/_final_sha.txt` | `548d466d81a9` | 611 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 29 | `_september_workspace/.tmp/_gaps.txt` | `3f03d0608731` | 435 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 30 | `_september_workspace/.tmp/_gaps2.txt` | `4d899338b548` | 2377 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 31 | `_september_workspace/.tmp/_iscp_dual_probe_out_2026_10_09.txt` | `e3baae0b8d08` | 1342 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 32 | `_september_workspace/.tmp/_iscp_probe_out_2026_10_09.txt` | `b4c67cf64825` | 6424 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 33 | `_september_workspace/.tmp/_kv3s43_diag_out.txt` | `24ce4995aa09` | 2378 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 34 | `_september_workspace/.tmp/_kv3s43_frozen_recompute_readings_2026_10_09.txt` | `2f20780cb7a6` | 13244 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 35 | `_september_workspace/.tmp/_kv3s43_frozen_recompute_readings2_2026_10_09.txt` | `fc3ba9fe051b` | 7100 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 36 | `_september_workspace/.tmp/_kv3s43_frozen_recompute_readings3_2026_10_09.txt` | `3ad13513e25c` | 7370 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 37 | `_september_workspace/.tmp/_l14v3_aggregated_10cells.json` | `6f09512818f0` | 634458 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 38 | `_september_workspace/.tmp/_l14v3_aggregated_10cells_v4.json` | `66a9b8b3dabf` | 2233138 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 39 | `_september_workspace/.tmp/_l14v3_n26_metrics.json` | `80c5eccf4630` | 1445 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 40 | `_september_workspace/.tmp/_l14v3_n26_metrics_v2.json` | `eb9ce9683ad3` | 2579 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 41 | `_september_workspace/.tmp/_l14v3_sensitivity_v2.json` | `dcaa4b6b3b0b` | 2292 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 42 | `_september_workspace/.tmp/_payload.json` | `be0a4f54aade` | 42672 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 43 | `_september_workspace/.tmp/_q_cards_2026_10_11.txt` | `181a8b249b88` | 14888 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 44 | `_september_workspace/.tmp/_q3_l282_fix_validate_2026_10_09.txt` | `35b98fd8cde4` | 6026 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 45 | `_september_workspace/.tmp/_r1_scratch_bom.json` | `339de051e817` | 17 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 46 | `_september_workspace/.tmp/_r1_scratch_corrupt_a.json` | `40a850e41f3e` | 15 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 47 | `_september_workspace/.tmp/_r1_scratch_good.json` | `ac623f06604c` | 14 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 48 | `_september_workspace/.tmp/_r10.txt` | `7f96aa9bb271` | 3867 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 49 | `_september_workspace/.tmp/_r11_ctx.txt` | `25e2c97e9a17` | 4106 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 50 | `_september_workspace/.tmp/_r4_cleanup_worker_keyscan_results_2026_09_29.json` | `f3e8ae7a6db9` | 75 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 51 | `_september_workspace/.tmp/_r4_key_scan_r1_files_2026_09_27.json` | `cee49aa2f482` | 2313 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 52 | `_september_workspace/.tmp/_r4_key_scan_results_2026_09_24.json` | `b03b348fd3da` | 1014 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 53 | `_september_workspace/.tmp/_r6_evidence.txt` | `eaed8c0a509e` | 30834 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 54 | `_september_workspace/.tmp/_rj5_mapping_test_2026_09_27.out.txt` | `796e3a8b432f` | 1384 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 55 | `_september_workspace/.tmp/_rpq_nonportrait_full_probe_out_2026_10_09.txt` | `4470b09da8f4` | 23891 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 56 | `_september_workspace/.tmp/_rpq_nonportrait_full_probe_out3_2026_10_09.txt` | `3b5ecd179b2f` | 43422 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 57 | `_september_workspace/.tmp/_rpq_nonportrait_full_probe_out4_2026_10_09.txt` | `b2c96951bc8f` | 9112 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 58 | `_september_workspace/.tmp/_run_output.log` | `f5fe18205e3d` | 1420 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 59 | `_september_workspace/.tmp/_s4_freeze_rpair_readings_2026_10_09.txt` | `c2276232b04a` | 14312 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 60 | `_september_workspace/.tmp/_s4_intake_recompute_readings_2026_10_09.txt` | `bb5eb15e9c1a` | 6641 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 61 | `_september_workspace/.tmp/_s4_refreeze179_final_readings_2026_10_09.txt` | `4b1a8145e7b7` | 1306 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 62 | `_september_workspace/.tmp/_s4_refreeze179_grid_readings_2026_10_09.txt` | `4d175865db79` | 5293 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 63 | `_september_workspace/.tmp/_s4_refreeze179_grid_readings2_2026_10_09.txt` | `e26ba2c34705` | 2351 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 64 | `_september_workspace/.tmp/_s4_refreeze179_readings_2026_10_09.txt` | `18426ff0afb0` | 3833 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 65 | `_september_workspace/.tmp/_s4_topup_addendum_verify_2026_10_09.txt` | `aabdef1da2b7` | 841 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 66 | `_september_workspace/.tmp/_s4f2_manifest_post.txt` | `8824ece12d30` | 130975 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 67 | `_september_workspace/.tmp/_s4f2_manifest_pre.txt` | `8650ea333291` | 130701 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 68 | `_september_workspace/.tmp/_s4f2_probe_out.txt` | `b8f1e47ba331` | 9943 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 69 | `_september_workspace/.tmp/_s4f2_probe2_out.txt` | `44c9d5176d12` | 9414 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 70 | `_september_workspace/.tmp/_s4f2_probe3_out.txt` | `959372c08eff` | 6228 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 71 | `_september_workspace/.tmp/_s4oq_baseline_faces_2026_10_09.json` | `7deb932bb35d` | 38835 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 72 | `_september_workspace/.tmp/_s4oq_stats_2026_10_09.json` | `570489bb6163` | 1669 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 73 | `_september_workspace/.tmp/_s4oq_sups_draft_2026_10_09.json` | `ace64d4f377d` | 23401 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 74 | `_september_workspace/.tmp/_s4td_existing_faces.json` | `1009161547cf` | 36128 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 75 | `_september_workspace/.tmp/_s4td_existing_qindex.tsv` | `ad8c9e3c966b` | 14093 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 76 | `_september_workspace/.tmp/_s5dp_run_stdout_2026_10_11.txt` | `13f90aafab80` | 7256 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 77 | `_september_workspace/.tmp/_t1_exp2_c_driver.log` | `8abac60bb797` | 108388 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 78 | `_september_workspace/.tmp/_t1_exp2_c_driver_stdout.log` | `0bf18edc773d` | 9410 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 79 | `_september_workspace/.tmp/_t1_exp2_c_driver_stdout2.log` | `120391010514` | 9272 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 80 | `_september_workspace/.tmp/_t1_exp2_c_driver_stdout3.log` | `d0aaca46b41a` | 9376 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 81 | `_september_workspace/.tmp/_t1_exp2_c_driver_stdout4.log` | `16f08ff22f9d` | 73756 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 82 | `_september_workspace/.tmp/_t1_exp2_pi_card_ask6455cd9f15bf7dc12ae673d9.json` | `a7322dfe48e5` | 5269 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 83 | `_september_workspace/.tmp/_t1_exp2_run_d.log` | `b5391e5b0ca3` | 4752 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 84 | `_september_workspace/.tmp/_t1_exp2_run_d2.log` | `34123220512b` | 3132 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 85 | `_september_workspace/.tmp/_t1_gap_prewrite_snapshot_2026_10_01.json` | `f58e66a2410d` | 4911 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 86 | `_september_workspace/.tmp/_t1_qwen_temp_sweep_decomposition.txt` | `2d96061318d9` | 1312 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 87 | `_september_workspace/.tmp/_t1_qwen_temp_sweep_readings_table.txt` | `2e1bec1e11a1` | 2042 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 88 | `_september_workspace/.tmp/_t1_qwen_temp_sweep_retry.log` | `1a791e41bd4b` | 1757 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 89 | `_september_workspace/.tmp/_t1_qwen_temp_sweep_run.log` | `ee6a1ee19548` | 8402 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 90 | `_september_workspace/.tmp/_t1_r2_run_driver.log` | `c397ad7af316` | 37504 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 91 | `_september_workspace/.tmp/_t1_r2_verify_2026_10_09.json` | `860294c4fc8f` | 5641 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 92 | `_september_workspace/.tmp/_t1_temp_axis_design_probe_2026_10_09.json` | `02e8133d3000` | 5657 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 93 | `_september_workspace/.tmp/_t15_inspect3_out.txt` | `56f1909cd962` | 1588 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 94 | `_september_workspace/.tmp/_t15_inspect4_out.txt` | `ba65ec451865` | 3057 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 95 | `_september_workspace/.tmp/_t15_inspect5_out.txt` | `e632feb9ad99` | 933 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 96 | `_september_workspace/.tmp/_t15_inspect6_out.txt` | `194f2ac92089` | 6659 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 97 | `_september_workspace/.tmp/_t15_inspect7_out.txt` | `5d51dcad59d1` | 3647 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 98 | `_september_workspace/.tmp/_t15_percell.txt` | `95d32bed4c21` | 491 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 99 | `_september_workspace/.tmp/_t15_percell_out.txt` | `cbec28a08723` | 772 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 100 | `_september_workspace/.tmp/_tail3_atomic_make_2026_09_29.json` | `6c6fb7078a9d` | 19595 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 101 | `_september_workspace/.tmp/_tail3_atomic_refs_2026_09_29.json` | `d6a3361a794a` | 5784 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 102 | `_september_workspace/.tmp/_tail3_atomic_verify_2026_09_29.json` | `e4226aaf3380` | 11116 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 103 | `_september_workspace/.tmp/_v16_full_decoded.txt` | `fdfe315ff54a` | 174424 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 104 | `_september_workspace/.tmp/_v16_tail_dump.txt` | `fdfe315ff54a` | 174424 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 105 | `_september_workspace/.tmp/_v16_tail_only.txt` | `63fccc843cdd` | 3471 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 106 | `_september_workspace/.tmp/_v3r1_diag.json` | `e2e61ad91ece` | 5699 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 107 | `_september_workspace/.tmp/_v3r1_run1.log` | `2e3ca9e57eb6` | 5062 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 108 | `_september_workspace/.tmp/_v3r1_run2.log` | `4d945579a5ee` | 2066 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 109 | `_september_workspace/.tmp/_vk_baxis_probe_2026_10_09.txt` | `d74e9ae8cd3a` | 5156 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 110 | `_september_workspace/.tmp/_vk_dualread_probe_2026_10_09.txt` | `79ad926f75a8` | 888 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 111 | `_september_workspace/.tmp/anchor_snapshot.json` | `54607fc836a1` | 3706 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 112 | `_september_workspace/.tmp/card23_readout_utf8.txt` | `4aa127d1dc62` | 5088 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 113 | `_september_workspace/.tmp/e4_axis2_run_out.json` | `536080b19999` | 3514 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 114 | `_september_workspace/.tmp/e4_axis2_validation_out.json` | `5b3ef39dc114` | 2657 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 115 | `_september_workspace/.tmp/five_terminal_classify_2026_10_10.json` | `9e04c58572bd` | 188834 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 116 | `_september_workspace/.tmp/five_terminal_domain_2026_10_10.json` | `1efe7e458ab1` | 192600 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 117 | `_september_workspace/.tmp/five_terminal_scan_2026_10_10.json` | `5196b75b95b6` | 126177 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 118 | `_september_workspace/.tmp/five_terminal_supplement_2026_10_10.json` | `b664c3baeb75` | 17614 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 119 | `_september_workspace/.tmp/receipt_disp_idx.txt` | `08261e23970b` | 6876782 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 120 | `_september_workspace/.tmp/vk_v3df_0_1_verify_out_2026_10_09.json` | `d6dccc069511` | 30845 | E .tmp中间件 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 121 | `_september_workspace/results/_v4_supp_l14v3_batch2_r2_models_probe.err.log` | `e3b0c44298fc` | 0 | B 0字节 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 122 | `_september_workspace/results/_adendum_a_degradation_precheck_20260917_132049.json._moved_20260924_1830.json` | `38fabeb19691` | 4248 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 123 | `_september_workspace/results/_adendum_b_pi_real_labels_v2_20260917_133726.json._moved_20260924_1830.json` | `3d344711cf8c` | 2374 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 124 | `_september_workspace/results/_adendum_b_pi_real_labels_v2_20260917_133852.json._moved_20260924_1830.json` | `c725e08e0a1c` | 2374 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 125 | `_september_workspace/results/_adendum_c_pm_attack_surface_v2_20260917_133726.json._moved_20260924_1830.json` | `193ba7d66412` | 4123 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 126 | `_september_workspace/results/_adendum_c_pm_attack_surface_v2_20260917_133852.json._moved_20260924_1830.json` | `6eba63788ca8` | 4122 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 127 | `_september_workspace/results/_adendum_d_pc_r2_per_model_v2_20260917_133726.json._moved_20260924_1830.json` | `6fe706750823` | 4605 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 128 | `_september_workspace/results/_adendum_d_pc_r2_per_model_v2_20260917_133852.json._moved_20260924_1830.json` | `d66792eea40e` | 4605 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 129 | `_september_workspace/results/_adendum_e_pd_supplement_v2_20260917_133726.json._moved_20260924_1830.json` | `2c4790ffb6e3` | 1353 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 130 | `_september_workspace/results/_adendum_e_pd_supplement_v2_20260917_133852.json._moved_20260924_1830.json` | `46d8dacb4721` | 1353 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 131 | `_september_workspace/results/_adendum_f_pe_3modal_closure_llm_dispatch_20260917_132143.json._moved_20260924_1830.json` | `879494ed8fb9` | 3646 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 132 | `_september_workspace/results/_adendum_f_pe_3modal_v2_20260917_143033.json._moved_20260924_1830.json` | `afab79249be7` | 38622 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 133 | `_september_workspace/results/_adendum_fgk_complete_20260917_143033.md._moved_20260924_1830.md` | `958188c83cf0` | 14005 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 134 | `_september_workspace/results/_adendum_g_pf_dfix2_timing_converge_llm_dispatch_20260917_132143.json._moved_20260924_1830.json` | `d10462080832` | 2757 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 135 | `_september_workspace/results/_adendum_g_pf_dfix2_v2_20260917_143033.json._moved_20260924_1830.json` | `bf8db2ad255b` | 95292 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 136 | `_september_workspace/results/_adendum_i_po_captions_closure_20260917_132049.json._moved_20260924_1830.json` | `18165008bef6` | 4429 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 137 | `_september_workspace/results/_adendum_j_warehouse_spearman_health_20260917_132049.json._moved_20260924_1830.json` | `df661d62426a` | 11337 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 138 | `_september_workspace/results/_adendum_k_087_cluster_cross_backbone_llm_dispatch_20260917_132143.json._moved_20260924_1830.json` | `acdf933f68e0` | 2911 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 139 | `_september_workspace/results/_adendum_k_qwen3_087_cluster_v2_20260917_143033.json._moved_20260924_1830.json` | `43477c8ea2d6` | 32481 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 140 | `_september_workspace/results/_adendum_l_verifier_dual_impl_diff_20260917_132049.json._moved_20260924_1830.json` | `1532607ded80` | 2783 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 141 | `_september_workspace/results/_adendum_m_pj_convergence_basin_v2_20260917_133726.json._moved_20260924_1830.json` | `ea7ffda97e20` | 3694 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 142 | `_september_workspace/results/_adendum_m_pj_convergence_basin_v2_20260917_133852.json._moved_20260924_1830.json` | `8ab01a1e42ae` | 3686 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 143 | `_september_workspace/results/_adendum_n_pn_coupling_v2_20260917_133726.json._moved_20260924_1830.json` | `1b91cc25ca57` | 2012 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 144 | `_september_workspace/results/_adendum_n_pn_coupling_v2_20260917_133852.json._moved_20260924_1830.json` | `a32f3c8ba520` | 2011 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 145 | `_september_workspace/results/_adendum_o_pk_v2_three_way_v2_20260917_133726.json._moved_20260924_1830.json` | `725fd7b961f8` | 1971 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 146 | `_september_workspace/results/_adendum_o_pk_v2_three_way_v2_20260917_133852.json._moved_20260924_1830.json` | `a30ff093305d` | 1970 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 147 | `_september_workspace/results/_adendum_p_pc_two_phase_fail_h0_20260917_132049.json._moved_20260924_1830.json` | `6b26daddc92c` | 2456 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 148 | `_september_workspace/results/_adendum_q_deepseek_v4_pro_anchor_20260917_132049.json._moved_20260924_1830.json` | `ab5d9ae6e42a` | 4003 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 149 | `_september_workspace/results/_d05_backbone_robustness_beta_20260918_100853.json._moved_20260924_1830.json` | `9b6f085d96dc` | 1490 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 150 | `_september_workspace/results/_d05_combined_report_20260918_100853.md._moved_20260924_1830.md` | `c87eb8974268` | 10555 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 151 | `_september_workspace/results/_d05_data_rescue_note_2026_09_18.md._moved_20260924_1830.md` | `120295a19655` | 1181 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 152 | `_september_workspace/results/_d05_i1i5_invariants_check_20260918_100853.json._moved_20260924_1830.json` | `f12af5435928` | 1920 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 153 | `_september_workspace/results/_d05_main_run_results_20260918_100853.json._moved_20260924_1830.json` | `0a933d7c8d7a` | 15243 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 154 | `_september_workspace/results/_d05_main_run_results_nemotron_3.5_20260918_100853.json._moved_20260924_1830.json` | `1b1b6ad67c39` | 15111 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 155 | `_september_workspace/results/_d05_main_run_results_qwen3_failed_20260918_100853.json._moved_20260924_1830.json` | `427b18da8114` | 18358 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 156 | `_september_workspace/results/_d05_opt_5_directions_results_20260918_100853.json._moved_20260924_1830.json` | `e5979133195a` | 5614 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 157 | `_september_workspace/results/_kimi_push_v3_manifest_batch1_77e2f952.json._moved_20260924_1830.json` | `b5f517a321a3` | 2534 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 158 | `_september_workspace/results/_kimi_push_v3_manifest_batch10_1b753116.json._moved_20260924_1830.json` | `326adca520f1` | 5007 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 159 | `_september_workspace/results/_kimi_push_v3_manifest_batch11_7d6a7c8f.json._moved_20260924_1830.json` | `383446f24707` | 2573 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 160 | `_september_workspace/results/_kimi_push_v3_manifest_batch12_a2853574.json._moved_20260924_1830.json` | `6be21f9586ec` | 1246 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 161 | `_september_workspace/results/_kimi_push_v3_manifest_batch13_83f895f9.json._moved_20260924_1830.json` | `0694838f66a8` | 739 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 162 | `_september_workspace/results/_kimi_push_v3_manifest_batch14_e5952130.json._moved_20260924_1830.json` | `64aa9d8a5c7d` | 1055 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 163 | `_september_workspace/results/_kimi_push_v3_manifest_batch15_0e65fe2f.json._moved_20260924_1830.json` | `cfc345d10c7d` | 385 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 164 | `_september_workspace/results/_kimi_push_v3_manifest_batch2_e18c17bb.json._moved_20260924_1830.json` | `f14341b8a1a1` | 9260 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 165 | `_september_workspace/results/_kimi_push_v3_manifest_batch3_01ecf050.json._moved_20260924_1830.json` | `fd64909ea1d8` | 9656 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 166 | `_september_workspace/results/_kimi_push_v3_manifest_batch4_2f872d54.json._moved_20260924_1830.json` | `d35453f21049` | 9720 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 167 | `_september_workspace/results/_kimi_push_v3_manifest_batch5_34439e1e.json._moved_20260924_1830.json` | `2769b83f5b1d` | 9511 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 168 | `_september_workspace/results/_kimi_push_v3_manifest_batch6_28055e59.json._moved_20260924_1830.json` | `f3eb7a38ae7d` | 10107 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 169 | `_september_workspace/results/_kimi_push_v3_manifest_batch7_0903df7e.json._moved_20260924_1830.json` | `7bda1fecd7c4` | 9748 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 170 | `_september_workspace/results/_kimi_push_v3_manifest_batch8_7468a23b.json._moved_20260924_1830.json` | `5a38fc02978c` | 9880 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 171 | `_september_workspace/results/_kimi_push_v3_manifest_batch9_f7d9cf1d.json._moved_20260924_1830.json` | `968d7c6c43ca` | 9745 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 172 | `_september_workspace/results/_kimi_safe_batch_push_v1_2026_09_17.json._moved_20260924_1830.json` | `4a204fb0d682` | 7280 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 173 | `_september_workspace/results/_kimi_safe_batch_push_v2_full_2026_09_17.json._moved_20260924_1830.json` | `adf3a8017e26` | 47954 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |
| 174 | `_september_workspace/results/_kimi_safe_batch_push_v3_full_2026_09_17.json._moved_20260924_1830.json` | `058099c10cfb` | 7954 | A 冗余副本 | LIST_ONLY（0 功能性引用） | 回收站可恢复 |

---

## 4. 转移执行结果

| 项 | 值 |
|---|---|
| 转移件数 | **723** |
| 入归档目录 / 出归档目录 | 0 / 0（``repo/results/_archive_*` 与 `sub/results/_archive_*` 均 0 动作） |
| 跨区（repo → sub） | **723**（全量） |
| SHA-256 复算 | **MATCH 723 / FAIL 0 / PRE_MISMATCH 0** |
| 同区转移 | 0 |
| 目标已占用而未动 | 12（SAME_IDENTITY，见 `6） |
| CONFLICT（同名异哈希） | **0** |
| 保留源目录结构 | 是（``results/<相对路径>` → `sub/results/<相对路径>`） |

---

## 5. 逐件映射表（旧路径 → 新路径 · 723 条）

| # | 旧路径（已失效） | 新路径 | SHA-12 | bytes | 状态 |
|---|---|---|---|---|---|
| 1 | `_september_workspace/results/c5_b_group_verdict_2026_10_01.md` | `_september_workspace/results/c5_b_group_verdict_2026_10_01.md` | `3fbf6b38a383` | 30118 | MATCH |
| 2 | `_september_workspace/results/c5_protocol_version_annex_2026_10_01.md` | `_september_workspace/results/c5_protocol_version_annex_2026_10_01.md` | `2593ea7b93cf` | 18558 | MATCH |
| 3 | `_september_workspace/results/deposon_3risk_v0_fixes_2026_09_11.json` | `_september_workspace/results/deposon_3risk_v0_fixes_2026_09_11.json` | `d87c0327a6fb` | 8338 | MATCH |
| 4 | `_september_workspace/results/deposon_ark_models_2026_09_10.json` | `_september_workspace/results/deposon_ark_models_2026_09_10.json` | `ccc3ea09a7f5` | 23296 | MATCH |
| 5 | `_september_workspace/results/deposon_benchmark_v1_3_labelfree.json` | `_september_workspace/results/deposon_benchmark_v1_3_labelfree.json` | `57f06a426bec` | 3011 | MATCH |
| 6 | `_september_workspace/results/deposon_benchmark_v1_3_labelshuffle.json` | `_september_workspace/results/deposon_benchmark_v1_3_labelshuffle.json` | `5a7555358be3` | 182322 | MATCH |
| 7 | `_september_workspace/results/deposon_benchmark_v1_3_resonant.json` | `_september_workspace/results/deposon_benchmark_v1_3_resonant.json` | `769ae8c908c9` | 3134 | MATCH |
| 8 | `_september_workspace/results/deposon_benchmark_v1_4_sc5.json` | `_september_workspace/results/deposon_benchmark_v1_4_sc5.json` | `c9796d3b3263` | 12479 | MATCH |
| 9 | `_september_workspace/results/deposon_deepseek_v41_flash_2026_09_10.json` | `_september_workspace/results/deposon_deepseek_v41_flash_2026_09_10.json` | `4d7bea150f3a` | 13373 | MATCH |
| 10 | `_september_workspace/results/deposon_deepseek_v41_flash_30cells_2026_09_10.json` | `_september_workspace/results/deposon_deepseek_v41_flash_30cells_2026_09_10.json` | `84df447c38df` | 46432 | MATCH |
| 11 | `_september_workspace/results/deposon_deepseek_v41_flash_30cells_v2_2026_09_10.json` | `_september_workspace/results/deposon_deepseek_v41_flash_30cells_v2_2026_09_10.json` | `05cde1ca74ef` | 17549 | MATCH |
| 12 | `_september_workspace/results/deposon_deepseek_v41_flash_5cells_fix_2026_09_10.json` | `_september_workspace/results/deposon_deepseek_v41_flash_5cells_fix_2026_09_10.json` | `28bad561c328` | 6748 | MATCH |
| 13 | `_september_workspace/results/deposon_embedding_dual_2026_09_10.json` | `_september_workspace/results/deposon_embedding_dual_2026_09_10.json` | `33f8ac5d4bff` | 6834 | MATCH |
| 14 | `_september_workspace/results/deposon_embedding_openrouter_5models_2026_09_10.json` | `_september_workspace/results/deposon_embedding_openrouter_5models_2026_09_10.json` | `0c0d9afd39ac` | 12785 | MATCH |
| 15 | `_september_workspace/results/deposon_feshbach_lindblad_sim_2026_09_10.json` | `_september_workspace/results/deposon_feshbach_lindblad_sim_2026_09_10.json` | `aa545c67604d` | 7414 | MATCH |
| 16 | `_september_workspace/results/deposon_feshbach_rag_30cells_2026_09_10.json` | `_september_workspace/results/deposon_feshbach_rag_30cells_2026_09_10.json` | `508f664ffa44` | 64978 | MATCH |
| 17 | `_september_workspace/results/deposon_g3_arrhenius.json` | `_september_workspace/results/deposon_g3_arrhenius.json` | `a3de045b5dd7` | 2284 | MATCH |
| 18 | `_september_workspace/results/deposon_gpt6_astra_smoke_2026_09_10.json` | `_september_workspace/results/deposon_gpt6_astra_smoke_2026_09_10.json` | `4bf92bfdefda` | 3500 | MATCH |
| 19 | `_september_workspace/results/deposon_gpt6_proxy_smoke_2026_09_10.json` | `_september_workspace/results/deposon_gpt6_proxy_smoke_2026_09_10.json` | `524b34e319b5` | 5485 | MATCH |
| 20 | `_september_workspace/results/deposon_gpt6_proxy_step1_2026_09_10.json` | `_september_workspace/results/deposon_gpt6_proxy_step1_2026_09_10.json` | `2e23115d9d4b` | 1245 | MATCH |
| 21 | `_september_workspace/results/deposon_gpt6_proxy_v2_2026_09_10.json` | `_september_workspace/results/deposon_gpt6_proxy_v2_2026_09_10.json` | `a6812512f8f3` | 5810 | MATCH |
| 22 | `_september_workspace/results/deposon_gpt6_teamorouter_cn_2026_09_10.json` | `_september_workspace/results/deposon_gpt6_teamorouter_cn_2026_09_10.json` | `2241567c6efd` | 4855 | MATCH |
| 23 | `_september_workspace/results/deposon_gpt6_vpn_smoke_2026_09_10.json` | `_september_workspace/results/deposon_gpt6_vpn_smoke_2026_09_10.json` | `3267746e47e9` | 3489 | MATCH |
| 24 | `_september_workspace/results/deposon_llm_codingplan_30cells_2026_09_10.json` | `_september_workspace/results/deposon_llm_codingplan_30cells_2026_09_10.json` | `24e4dcbaa4ea` | 18634 | MATCH |
| 25 | `_september_workspace/results/deposon_openrouter_5model_30cells_2026_09_10.json` | `_september_workspace/results/deposon_openrouter_5model_30cells_2026_09_10.json` | `b374f80f3b2d` | 31690 | MATCH |
| 26 | `_september_workspace/results/deposon_openrouter_embedding_5model_2026_09_10.json` | `_september_workspace/results/deposon_openrouter_embedding_5model_2026_09_10.json` | `45f314f3415c` | 9472 | MATCH |
| 27 | `_september_workspace/results/deposon_overseas_open_smoke_2026_09_10.json` | `_september_workspace/results/deposon_overseas_open_smoke_2026_09_10.json` | `2481adadcbb9` | 6787 | MATCH |
| 28 | `_september_workspace/results/deposon_pf_d1_2026_09_15.json` | `_september_workspace/results/deposon_pf_d1_2026_09_15.json` | `12791772814e` | 21933 | MATCH |
| 29 | `_september_workspace/results/deposon_v16_llm_prior_summary.json` | `_september_workspace/results/deposon_v16_llm_prior_summary.json` | `a7952d9d78db` | 5517 | MATCH |
| 30 | `_september_workspace/results/deposon_v2_phase2_dual_mainline_2026_09_11.json` | `_september_workspace/results/deposon_v2_phase2_dual_mainline_2026_09_11.json` | `e337b824c4b9` | 3189 | MATCH |
| 31 | `_september_workspace/results/deposon_v2_phase2_f2_2026_09_11.json` | `_september_workspace/results/deposon_v2_phase2_f2_2026_09_11.json` | `8b16b611c4db` | 4582 | MATCH |
| 32 | `_september_workspace/results/deposon_v2_phase3_f3_2026_09_11.json` | `_september_workspace/results/deposon_v2_phase3_f3_2026_09_11.json` | `0b5dca765d16` | 2474 | MATCH |
| 33 | `_september_workspace/results/deposon_v2_phase3_strip_reembed_2026_09_11.json` | `_september_workspace/results/deposon_v2_phase3_strip_reembed_2026_09_11.json` | `8900526d8e3a` | 4160 | MATCH |
| 34 | `_september_workspace/results/deposon_v2_phase5_f5_2026_09_11.json` | `_september_workspace/results/deposon_v2_phase5_f5_2026_09_11.json` | `889fc57b3b72` | 2356 | MATCH |
| 35 | `_september_workspace/results/deposon_v3x_6way_stage2_2026_09_10.json` | `_september_workspace/results/deposon_v3x_6way_stage2_2026_09_10.json` | `d301bbfed982` | 2741 | MATCH |
| 36 | `_september_workspace/results/deposon_v3x_6way_stage3_2026_09_10.json` | `_september_workspace/results/deposon_v3x_6way_stage3_2026_09_10.json` | `d892a9d3d6ba` | 15943 | MATCH |
| 37 | `_september_workspace/results/deposon_v3x_6way_summary_2026_09_10.json` | `_september_workspace/results/deposon_v3x_6way_summary_2026_09_10.json` | `63e0798e5843` | 1506 | MATCH |
| 38 | `_september_workspace/results/deposon_v41_flash_60cells_v2_2026_09_10.json` | `_september_workspace/results/deposon_v41_flash_60cells_v2_2026_09_10.json` | `b1d802a68723` | 38428 | MATCH |
| 39 | `_september_workspace/results/deposon_v41_flash_rag_baseline_2026_09_10.json` | `_september_workspace/results/deposon_v41_flash_rag_baseline_2026_09_10.json` | `6754d2655e0a` | 101484 | MATCH |
| 40 | `_september_workspace/results/deposon_volcengine_7model_smoke_2026_09_10.json` | `_september_workspace/results/deposon_volcengine_7model_smoke_2026_09_10.json` | `eae44cc3b7b2` | 5944 | MATCH |
| 41 | `_september_workspace/results/deposon_volcengine_9model_smoke_2026_09_10.json` | `_september_workspace/results/deposon_volcengine_9model_smoke_2026_09_10.json` | `0e5ae7d7d641` | 5328 | MATCH |
| 42 | `_september_workspace/results/deposon_volcengine_coding_plan_5cells_2026_09_10.json` | `_september_workspace/results/deposon_volcengine_coding_plan_5cells_2026_09_10.json` | `52aa8901556e` | 6058 | MATCH |
| 43 | `_september_workspace/results/deposon_volcengine_coding_plan_catalog_2026_09_10.json` | `_september_workspace/results/deposon_volcengine_coding_plan_catalog_2026_09_10.json` | `c0efb547b9d1` | 2841 | MATCH |
| 44 | `_september_workspace/results/deposon_volcengine_doubao_embedding_2026_09_10.json` | `_september_workspace/results/deposon_volcengine_doubao_embedding_2026_09_10.json` | `e99783d18139` | 3303 | MATCH |
| 45 | `_september_workspace/results/deposon_volcengine_embedding_30cells_2026_09_10.json` | `_september_workspace/results/deposon_volcengine_embedding_30cells_2026_09_10.json` | `12be52bc02a7` | 24794 | MATCH |
| 46 | `_september_workspace/results/Deposon_评估汇总_v1_3_0.json` | `_september_workspace/results/Deposon_评估汇总_v1_3_0.json` | `2f02f50c164b` | 2811 | MATCH |
| 47 | `_september_workspace/results/manifest_large_files.md` | `_september_workspace/results/manifest_large_files.md` | `e0dc7a8e4c75` | 3440 | MATCH |
| 48 | `_september_workspace/results/_149_face_effect_disposal_2026_10_10.md` | `_september_workspace/results/_149_face_effect_disposal_2026_10_10.md` | `e7c1232df138` | 24295 | MATCH |
| 49 | `_september_workspace/results/_9model_merge_disposition_register_2026_10_09.md` | `_september_workspace/results/_9model_merge_disposition_register_2026_10_09.md` | `455277298212` | 11651 | MATCH |
| 50 | `_september_workspace/results/_a02_excluded_items_idx_collection_2026_10_10.md` | `_september_workspace/results/_a02_excluded_items_idx_collection_2026_10_10.md` | `03407e0b6662` | 39565 | MATCH |
| 51 | `_september_workspace/results/_af_entity_definition_draft_2026_10_10.md` | `_september_workspace/results/_af_entity_definition_draft_2026_10_10.md` | `97654060d86e` | 25257 | MATCH |
| 52 | `_september_workspace/results/_alt_delib_pkg3_two_judgments_2026_10_10.md` | `_september_workspace/results/_alt_delib_pkg3_two_judgments_2026_10_10.md` | `3f52709a48e8` | 38032 | MATCH |
| 53 | `_september_workspace/results/_archive_and_b6_inquiry_register_2026_10_08.md` | `_september_workspace/results/_archive_and_b6_inquiry_register_2026_10_08.md` | `1d08a780a715` | 21163 | MATCH |
| 54 | `_september_workspace/results/_archive_cleanup_extension_2026_09_28.md` | `_september_workspace/results/_archive_cleanup_extension_2026_09_28.md` | `889d15247607` | 28774 | MATCH |
| 55 | `_september_workspace/results/_archive_cleanup_non_upload_2026_09_28.md` | `_september_workspace/results/_archive_cleanup_non_upload_2026_09_28.md` | `34f2c63306b8` | 56714 | MATCH |
| 56 | `_september_workspace/results/_archive_ledger_rectification_register_2026_10_09.md` | `_september_workspace/results/_archive_ledger_rectification_register_2026_10_09.md` | `99359733eef1` | 20933 | MATCH |
| 57 | `_september_workspace/results/_archive_manifest_non_upload_v2_2026_09_28.json` | `_september_workspace/results/_archive_manifest_non_upload_v2_2026_09_28.json` | `84eef669234b` | 236651 | MATCH |
| 58 | `_september_workspace/results/_archive_manifest_non_upload_v3_2026_09_28.json` | `_september_workspace/results/_archive_manifest_non_upload_v3_2026_09_28.json` | `a2e4c5a9b713` | 204256 | MATCH |
| 59 | `_september_workspace/results/_archive_moveout_register_2026_09_29.md` | `_september_workspace/results/_archive_moveout_register_2026_09_29.md` | `56639e57ac06` | 13363 | MATCH |
| 60 | `_september_workspace/results/_asset_identity_reconciliation_2026_10_01.md` | `_september_workspace/results/_asset_identity_reconciliation_2026_10_01.md` | `0d22797f084f` | 28291 | MATCH |
| 61 | `_september_workspace/results/_axis1_three_recomputations_2026_10_11.md` | `_september_workspace/results/_axis1_three_recomputations_2026_10_11.md` | `8de23f7d7384` | 29938 | MATCH |
| 62 | `_september_workspace/results/_b01_new_key_classification_2026_10_10.md` | `_september_workspace/results/_b01_new_key_classification_2026_10_10.md` | `2ddfecf6201c` | 38669 | MATCH |
| 63 | `_september_workspace/results/_b01_new_key_residue_judgment_2026_10_10.md` | `_september_workspace/results/_b01_new_key_residue_judgment_2026_10_10.md` | `345517455dcf` | 41984 | MATCH |
| 64 | `_september_workspace/results/_b01_p_counting_recompute_2026_10_10.md` | `_september_workspace/results/_b01_p_counting_recompute_2026_10_10.md` | `3511cf21a869` | 22104 | MATCH |
| 65 | `_september_workspace/results/_b01_recompute_authorization_supplement_2026_10_11.md` | `_september_workspace/results/_b01_recompute_authorization_supplement_2026_10_11.md` | `03a66d4c663a` | 18454 | MATCH |
| 66 | `_september_workspace/results/_b01_recompute_sec4_2_erratum_2026_10_10.md` | `_september_workspace/results/_b01_recompute_sec4_2_erratum_2026_10_10.md` | `fac3308fb295` | 16441 | MATCH |
| 67 | `_september_workspace/results/_b14_audit_f2f3_closure_register_2026_10_11.md` | `_september_workspace/results/_b14_audit_f2f3_closure_register_2026_10_11.md` | `9d4a3d6ddf88` | 29620 | MATCH |
| 68 | `_september_workspace/results/_b14_vk_evidence_audit_2026_10_10.md` | `_september_workspace/results/_b14_vk_evidence_audit_2026_10_10.md` | `89f17297f1f5` | 33586 | MATCH |
| 69 | `_september_workspace/results/_backfill_rule_execution_register_2026_10_08.md` | `_september_workspace/results/_backfill_rule_execution_register_2026_10_08.md` | `3a7f8e203b28` | 27267 | MATCH |
| 70 | `_september_workspace/results/_backfill_rule_final_2026_10_09.md` | `_september_workspace/results/_backfill_rule_final_2026_10_09.md` | `3e97d5286760` | 34602 | MATCH |
| 71 | `_september_workspace/results/_backfill_rule_vk_closeout_2026_10_08.md` | `_september_workspace/results/_backfill_rule_vk_closeout_2026_10_08.md` | `20f5835d47d2` | 26890 | MATCH |
| 72 | `_september_workspace/results/_batch3_receipt_kimi_2026_10_01.md` | `_september_workspace/results/_batch3_receipt_kimi_2026_10_01.md` | `8c2cb4c6a937` | 2238 | MATCH |
| 73 | `_september_workspace/results/_beta_formal_run_exec_register_2026_10_09.md` | `_september_workspace/results/_beta_formal_run_exec_register_2026_10_09.md` | `2e5f080eab6c` | 16811 | MATCH |
| 74 | `_september_workspace/results/_beta_formal_run_result_2026_10_09.json` | `_september_workspace/results/_beta_formal_run_result_2026_10_09.json` | `a5a918fd9861` | 103691 | MATCH |
| 75 | `_september_workspace/results/_blade_caliber_b8_judgment_2026_10_10.md` | `_september_workspace/results/_blade_caliber_b8_judgment_2026_10_10.md` | `e189d6eb63d9` | 28738 | MATCH |
| 76 | `_september_workspace/results/_b_coincidence_closeout_register_2026_10_10.md` | `_september_workspace/results/_b_coincidence_closeout_register_2026_10_10.md` | `51ce7b49c423` | 31451 | MATCH |
| 77 | `_september_workspace/results/_b_coincidence_disposition_judgment_2026_10_10.md` | `_september_workspace/results/_b_coincidence_disposition_judgment_2026_10_10.md` | `7ff80485955c` | 42838 | MATCH |
| 78 | `_september_workspace/results/_c1c4_ab_pilot_comparison_2026_10_09.md` | `_september_workspace/results/_c1c4_ab_pilot_comparison_2026_10_09.md` | `bdd2a1d7e6c5` | 15390 | MATCH |
| 79 | `_september_workspace/results/_c2_criterion_third_tier_draft_2026_10_11.md` | `_september_workspace/results/_c2_criterion_third_tier_draft_2026_10_11.md` | `844179898102` | 26713 | MATCH |
| 80 | `_september_workspace/results/_c4_math_corrections_downstream_erratum_2026_10_10.md` | `_september_workspace/results/_c4_math_corrections_downstream_erratum_2026_10_10.md` | `643cb9e249f7` | 28886 | MATCH |
| 81 | `_september_workspace/results/_c4_math_corrections_E1_E2_execution_erratum_2026_10_10.md` | `_september_workspace/results/_c4_math_corrections_E1_E2_execution_erratum_2026_10_10.md` | `4c369cb86db4` | 31607 | MATCH |
| 82 | `_september_workspace/results/_c4_reply_intake_acceptance_register_2026_10_01.md` | `_september_workspace/results/_c4_reply_intake_acceptance_register_2026_10_01.md` | `e1e8cb7b9db4` | 33728 | MATCH |
| 83 | `_september_workspace/results/_c4_theory_source_caliber_correction_2026_09_30.md` | `_september_workspace/results/_c4_theory_source_caliber_correction_2026_09_30.md` | `61b139efd0ef` | 25022 | MATCH |
| 84 | `_september_workspace/results/_c4_unblock_reply_independent_review_2026_10_10.md` | `_september_workspace/results/_c4_unblock_reply_independent_review_2026_10_10.md` | `2ecd866e2468` | 27364 | MATCH |
| 85 | `_september_workspace/results/_c8_c2_disposition_register_2026_10_11.md` | `_september_workspace/results/_c8_c2_disposition_register_2026_10_11.md` | `fb816c572779` | 30956 | MATCH |
| 86 | `_september_workspace/results/_carrier_qid_disposition_2026_10_11.md` | `_september_workspace/results/_carrier_qid_disposition_2026_10_11.md` | `7d74d5a4d81e` | 3406 | MATCH |
| 87 | `_september_workspace/results/_charlie_delivery_register_2026_10_08.md` | `_september_workspace/results/_charlie_delivery_register_2026_10_08.md` | `6f4bf31276f5` | 10733 | MATCH |
| 88 | `_september_workspace/results/_ci_bc_lines_ci_collection_2026_10_09.md` | `_september_workspace/results/_ci_bc_lines_ci_collection_2026_10_09.md` | `6db4d0fb2452` | 24769 | MATCH |
| 89 | `_september_workspace/results/_ci_bc_scope_estimand_judgments_2026_10_09.md` | `_september_workspace/results/_ci_bc_scope_estimand_judgments_2026_10_09.md` | `d76ba2297d0d` | 37682 | MATCH |
| 90 | `_september_workspace/results/_ci_degradation_binding_form_a_register_2026_10_09.md` | `_september_workspace/results/_ci_degradation_binding_form_a_register_2026_10_09.md` | `424730b5123d` | 26104 | MATCH |
| 91 | `_september_workspace/results/_ci_detail_decoupling_degradation_baseline_2026_10_09.md` | `_september_workspace/results/_ci_detail_decoupling_degradation_baseline_2026_10_09.md` | `56b62ed5ab74` | 20973 | MATCH |
| 92 | `_september_workspace/results/_ci_four_items_effectiveness_register_2026_10_09.md` | `_september_workspace/results/_ci_four_items_effectiveness_register_2026_10_09.md` | `4ab2464a266e` | 29365 | MATCH |
| 93 | `_september_workspace/results/_ci_gap_fill_alt_bc_aper_prime_2026_10_09.md` | `_september_workspace/results/_ci_gap_fill_alt_bc_aper_prime_2026_10_09.md` | `bee0f1f0bdb2` | 29709 | MATCH |
| 94 | `_september_workspace/results/_ci_line_establishment_2026_10_09.md` | `_september_workspace/results/_ci_line_establishment_2026_10_09.md` | `329c1c5e91d1` | 28262 | MATCH |
| 95 | `_september_workspace/results/_ci_three_delegated_judgments_2026_10_09.md` | `_september_workspace/results/_ci_three_delegated_judgments_2026_10_09.md` | `dac19ee9e66b` | 26090 | MATCH |
| 96 | `_september_workspace/results/_ci_three_items_effectivity_register_2026_10_09.md` | `_september_workspace/results/_ci_three_items_effectivity_register_2026_10_09.md` | `2b7166a7d726` | 31488 | MATCH |
| 97 | `_september_workspace/results/_ci_width_halfwidth_pin_2026_10_09.md` | `_september_workspace/results/_ci_width_halfwidth_pin_2026_10_09.md` | `51765f40f5f9` | 17426 | MATCH |
| 98 | `_september_workspace/results/_cleanup_round2_register_2026_09_29.md` | `_september_workspace/results/_cleanup_round2_register_2026_09_29.md` | `ee47a2ec49f4` | 36245 | MATCH |
| 99 | `_september_workspace/results/_cleanup_round_2026_10_01.md` | `_september_workspace/results/_cleanup_round_2026_10_01.md` | `0db6e5d6146c` | 27477 | MATCH |
| 100 | `_september_workspace/results/_cleanup_round_2026_10_08.md` | `_september_workspace/results/_cleanup_round_2026_10_08.md` | `d048a6de1dea` | 33179 | MATCH |
| 101 | `_september_workspace/results/_clearance_materials_register_2026_10_08.md` | `_september_workspace/results/_clearance_materials_register_2026_10_08.md` | `356eb1c53986` | 45254 | MATCH |
| 102 | `_september_workspace/results/_clearance_mini_rulings_closeout_register_2026_10_01.md` | `_september_workspace/results/_clearance_mini_rulings_closeout_register_2026_10_01.md` | `9238c2287af5` | 31942 | MATCH |
| 103 | `_september_workspace/results/_clearance_round_1_register_2026_10_08.md` | `_september_workspace/results/_clearance_round_1_register_2026_10_08.md` | `58fa92543338` | 13826 | MATCH |
| 104 | `_september_workspace/results/_closing_round_4_decisions_register_2026_10_08.md` | `_september_workspace/results/_closing_round_4_decisions_register_2026_10_08.md` | `771e37b4a25d` | 5322 | MATCH |
| 105 | `_september_workspace/results/_closing_round_5_decisions_register_2026_10_08.md` | `_september_workspace/results/_closing_round_5_decisions_register_2026_10_08.md` | `5b08d34a05ba` | 3282 | MATCH |
| 106 | `_september_workspace/results/_closing_round_6_decisions_register_2026_10_08.md` | `_september_workspace/results/_closing_round_6_decisions_register_2026_10_08.md` | `272cb570c78b` | 3869 | MATCH |
| 107 | `_september_workspace/results/_closing_round_7_decisions_register_2026_10_09.md` | `_september_workspace/results/_closing_round_7_decisions_register_2026_10_09.md` | `d5976bfe23c6` | 3206 | MATCH |
| 108 | `_september_workspace/results/_closing_round_9_decisions_register_2026_10_09.md` | `_september_workspace/results/_closing_round_9_decisions_register_2026_10_09.md` | `27118156a99a` | 2314 | MATCH |
| 109 | `_september_workspace/results/_codex_c4_unblock_reply_adoption_register_2026_10_10.md` | `_september_workspace/results/_codex_c4_unblock_reply_adoption_register_2026_10_10.md` | `b979e78562a9` | 22895 | MATCH |
| 110 | `_september_workspace/results/_codex_c4_values_followup_reply_intake_register_2026_10_10.md` | `_september_workspace/results/_codex_c4_values_followup_reply_intake_register_2026_10_10.md` | `c46d073589cf` | 24240 | MATCH |
| 111 | `_september_workspace/results/_codex_c4_values_reply_intake_register_2026_10_10.md` | `_september_workspace/results/_codex_c4_values_reply_intake_register_2026_10_10.md` | `8f1d27a02833` | 12926 | MATCH |
| 112 | `_september_workspace/results/_codex_c4_values_unblock_reply_intake_register_2026_10_10.md` | `_september_workspace/results/_codex_c4_values_unblock_reply_intake_register_2026_10_10.md` | `a2d7f86d72e5` | 27100 | MATCH |
| 113 | `_september_workspace/results/_commission_closeout_erratum_and_supplement_2026_10_11.md` | `_september_workspace/results/_commission_closeout_erratum_and_supplement_2026_10_11.md` | `7c102a6b4667` | 12447 | MATCH |
| 114 | `_september_workspace/results/_confirm_b9_tension_annex_2026_10_01.md` | `_september_workspace/results/_confirm_b9_tension_annex_2026_10_01.md` | `f28724a99a0c` | 19454 | MATCH |
| 115 | `_september_workspace/results/_confirm_round_2026_10_01_register.md` | `_september_workspace/results/_confirm_round_2026_10_01_register.md` | `23a97e340fdf` | 14500 | MATCH |
| 116 | `_september_workspace/results/_confirm_round_2_2026_10_01_register.md` | `_september_workspace/results/_confirm_round_2_2026_10_01_register.md` | `817302144788` | 22327 | MATCH |
| 117 | `_september_workspace/results/_coze_〔IM〕_v4_d7format_2026_09_26.pdf` | `_september_workspace/results/_coze_〔IM〕_v4_d7format_2026_09_26.pdf` | `a82881653520` | 465366 | MATCH |
| 118 | `_september_workspace/results/_c_component4_d2d3_gap_judgment_2026_10_11.md` | `_september_workspace/results/_c_component4_d2d3_gap_judgment_2026_10_11.md` | `08d3bfd82235` | 27490 | MATCH |
| 119 | `_september_workspace/results/_c_component4_three_items_judgment_2026_10_11.md` | `_september_workspace/results/_c_component4_three_items_judgment_2026_10_11.md` | `fd0094e2f865` | 41580 | MATCH |
| 120 | `_september_workspace/results/_c_reading_recompute_2026_10_09.md` | `_september_workspace/results/_c_reading_recompute_2026_10_09.md` | `95d7d23d24fd` | 21006 | MATCH |
| 121 | `_september_workspace/results/_d05_three_checks_readings_recheck_confirm_2026_10_10.md` | `_september_workspace/results/_d05_three_checks_readings_recheck_confirm_2026_10_10.md` | `dcf9f5cfa2db` | 20044 | MATCH |
| 122 | `_september_workspace/results/_d1_backfill_b3_b7_suggestion_table_2026_10_01.md` | `_september_workspace/results/_d1_backfill_b3_b7_suggestion_table_2026_10_01.md` | `8e1494301bb8` | 26731 | MATCH |
| 123 | `_september_workspace/results/_d1_backfill_collection_rounds_2026_10_01.md` | `_september_workspace/results/_d1_backfill_collection_rounds_2026_10_01.md` | `2d1a0d43e588` | 22908 | MATCH |
| 124 | `_september_workspace/results/_d1_backfill_conflict_trace_2026_10_01.md` | `_september_workspace/results/_d1_backfill_conflict_trace_2026_10_01.md` | `0cecda616f15` | 31506 | MATCH |
| 125 | `_september_workspace/results/_d1_backfill_event_id_prefix_proposal_2026_10_01.md` | `_september_workspace/results/_d1_backfill_event_id_prefix_proposal_2026_10_01.md` | `2636394df918` | 14074 | MATCH |
| 126 | `_september_workspace/results/_d1_backfill_readiness_pack_2026_10_01.md` | `_september_workspace/results/_d1_backfill_readiness_pack_2026_10_01.md` | `ed644fb07f88` | 26462 | MATCH |
| 127 | `_september_workspace/results/_d1_ruling_and_s3_transition_2026_10_01.md` | `_september_workspace/results/_d1_ruling_and_s3_transition_2026_10_01.md` | `dc9cb0e02922` | 28370 | MATCH |
| 128 | `_september_workspace/results/_d8_closeout_protocol_recompute_2026_09_30.md` | `_september_workspace/results/_d8_closeout_protocol_recompute_2026_09_30.md` | `57aba2cd26a6` | 31007 | MATCH |
| 129 | `_september_workspace/results/_d8_dup_overlap_disposal_2026_09_30.md` | `_september_workspace/results/_d8_dup_overlap_disposal_2026_09_30.md` | `de8691727842` | 32350 | MATCH |
| 130 | `_september_workspace/results/_day_close_register_2026_10_01.md` | `_september_workspace/results/_day_close_register_2026_10_01.md` | `6dbac1d1bcd6` | 33115 | MATCH |
| 131 | `_september_workspace/results/_deemphasis_verification_register_2026_10_08.md` | `_september_workspace/results/_deemphasis_verification_register_2026_10_08.md` | `3f806e44a13f` | 27322 | MATCH |
| 132 | `_september_workspace/results/_dup_name_diff_content_scan_2026_10_08.json` | `_september_workspace/results/_dup_name_diff_content_scan_2026_10_08.json` | `a27d11f45c21` | 1302889 | MATCH |
| 133 | `_september_workspace/results/_e2_glm2_distill_side_receipt_register_2026_10_09.md` | `_september_workspace/results/_e2_glm2_distill_side_receipt_register_2026_10_09.md` | `974124fc53f9` | 11336 | MATCH |
| 134 | `_september_workspace/results/_e4_lineage_conflict_correction_2026_10_11.md` | `_september_workspace/results/_e4_lineage_conflict_correction_2026_10_11.md` | `e20b96e32f54` | 30510 | MATCH |
| 135 | `_september_workspace/results/_e5_nonbinary_count_judgment_2026_10_10.md` | `_september_workspace/results/_e5_nonbinary_count_judgment_2026_10_10.md` | `2ef8797c03f4` | 37762 | MATCH |
| 136 | `_september_workspace/results/_e6_alt_permp_comparability_closure_2026_10_10.md` | `_september_workspace/results/_e6_alt_permp_comparability_closure_2026_10_10.md` | `1c663430b4aa` | 16636 | MATCH |
| 137 | `_september_workspace/results/_e6_case_a_judgment_face_promotion_2026_10_10.md` | `_september_workspace/results/_e6_case_a_judgment_face_promotion_2026_10_10.md` | `4e65c53f68e8` | 42116 | MATCH |
| 138 | `_september_workspace/results/_e6_j5_backfill_resolution_2026_10_10.md` | `_september_workspace/results/_e6_j5_backfill_resolution_2026_10_10.md` | `c888158b3263` | 23171 | MATCH |
| 139 | `_september_workspace/results/_e6_j5_semantics_conflict_judgment_2026_10_10.md` | `_september_workspace/results/_e6_j5_semantics_conflict_judgment_2026_10_10.md` | `3c7628a4964d` | 27682 | MATCH |
| 140 | `_september_workspace/results/_e6_j5_semantics_erratum_note_2026_10_10.md` | `_september_workspace/results/_e6_j5_semantics_erratum_note_2026_10_10.md` | `b2db427147e2` | 21166 | MATCH |
| 141 | `_september_workspace/results/_e6_n_distinct_judge_types_recompute_2026_10_10.md` | `_september_workspace/results/_e6_n_distinct_judge_types_recompute_2026_10_10.md` | `82c5c143134e` | 26304 | MATCH |
| 142 | `_september_workspace/results/_e6_th_v3_19_alignment_register_2026_10_10.md` | `_september_workspace/results/_e6_th_v3_19_alignment_register_2026_10_10.md` | `622cebef2c9f` | 32582 | MATCH |
| 143 | `_september_workspace/results/_e6_th_v3_19_residual_exits_judgment_2026_10_10.md` | `_september_workspace/results/_e6_th_v3_19_residual_exits_judgment_2026_10_10.md` | `442d5ff4acdb` | 46261 | MATCH |
| 144 | `_september_workspace/results/_e6_verdict_v3_rationale_review_2026_10_10.md` | `_september_workspace/results/_e6_verdict_v3_rationale_review_2026_10_10.md` | `664e82968fc2` | 39008 | MATCH |
| 145 | `_september_workspace/results/_ea_audit_batch_vk_2026_10_09.md` | `_september_workspace/results/_ea_audit_batch_vk_2026_10_09.md` | `ce27db55e0c5` | 19611 | MATCH |
| 146 | `_september_workspace/results/_eps_ls_semantics_judgment_2026_10_11.md` | `_september_workspace/results/_eps_ls_semantics_judgment_2026_10_11.md` | `51434449ff3b` | 31391 | MATCH |
| 147 | `_september_workspace/results/_evening_audit_b2_sampling_and_rejudges_2026_10_09.md` | `_september_workspace/results/_evening_audit_b2_sampling_and_rejudges_2026_10_09.md` | `b067fd28f950` | 29069 | MATCH |
| 148 | `_september_workspace/results/_executor_prereg_docstring_correction_2026_10_11.md` | `_september_workspace/results/_executor_prereg_docstring_correction_2026_10_11.md` | `f7f8328c49ba` | 27721 | MATCH |
| 149 | `_september_workspace/results/_executor_prereg_vs_impl_equivalence_2026_10_11.md` | `_september_workspace/results/_executor_prereg_vs_impl_equivalence_2026_10_11.md` | `e84cec618659` | 20028 | MATCH |
| 150 | `_september_workspace/results/_exp03_blade_caliber_review_2026_10_10.md` | `_september_workspace/results/_exp03_blade_caliber_review_2026_10_10.md` | `8c030758b331` | 19797 | MATCH |
| 151 | `_september_workspace/results/_exp05_missing_true_disposition_judgment_2026_10_10.md` | `_september_workspace/results/_exp05_missing_true_disposition_judgment_2026_10_10.md` | `e8e1e63a11db` | 25552 | MATCH |
| 152 | `_september_workspace/results/_exp05_negative_probe_rescan_2026_10_10.md` | `_september_workspace/results/_exp05_negative_probe_rescan_2026_10_10.md` | `ca7ff556fd7a` | 11566 | MATCH |
| 153 | `_september_workspace/results/_exp06_kcf4_check_bit_landing_2026_10_10.md` | `_september_workspace/results/_exp06_kcf4_check_bit_landing_2026_10_10.md` | `088ba3d58c0f` | 20709 | MATCH |
| 154 | `_september_workspace/results/_exp08_s4_prompt_face_register_2026_10_10.md` | `_september_workspace/results/_exp08_s4_prompt_face_register_2026_10_10.md` | `83109ecf440e` | 11929 | MATCH |
| 155 | `_september_workspace/results/_exp08_volume_reconciliation_2026_10_10.md` | `_september_workspace/results/_exp08_volume_reconciliation_2026_10_10.md` | `895eb3f2943c` | 24140 | MATCH |
| 156 | `_september_workspace/results/_external_letters_two_generation_values_note_2026_10_01.md` | `_september_workspace/results/_external_letters_two_generation_values_note_2026_10_01.md` | `9f4439bf89a9` | 10979 | MATCH |
| 157 | `_september_workspace/results/_external_pat_ark_prep_2026_09_30.md` | `_september_workspace/results/_external_pat_ark_prep_2026_09_30.md` | `ca540e5cab23` | 14055 | MATCH |
| 158 | `_september_workspace/results/_external_sibling_path_reference_rule_2026_10_01.md` | `_september_workspace/results/_external_sibling_path_reference_rule_2026_10_01.md` | `e79eabb6cfa7` | 23871 | MATCH |
| 159 | `_september_workspace/results/_f3f4_exit_drafts_2026_10_11.md` | `_september_workspace/results/_f3f4_exit_drafts_2026_10_11.md` | `523dc6cbdf9a` | 50427 | MATCH |
| 160 | `_september_workspace/results/_f3_definition_deep_judgment_2026_10_11.md` | `_september_workspace/results/_f3_definition_deep_judgment_2026_10_11.md` | `11945e587b1d` | 42351 | MATCH |
| 161 | `_september_workspace/results/_f3_new_definition_draft_2026_10_11.md` | `_september_workspace/results/_f3_new_definition_draft_2026_10_11.md` | `7482699e8b07` | 48068 | MATCH |
| 162 | `_september_workspace/results/_f4_direction1_prereq_check_2026_10_11.md` | `_september_workspace/results/_f4_direction1_prereq_check_2026_10_11.md` | `bb49153c311f` | 38664 | MATCH |
| 163 | `_september_workspace/results/_f4_direction1_seed_and_domain_draft_2026_10_11.md` | `_september_workspace/results/_f4_direction1_seed_and_domain_draft_2026_10_11.md` | `f77c080d9fc6` | 33887 | MATCH |
| 164 | `_september_workspace/results/_f5_77_16items_reconciliation_2026_10_01.md` | `_september_workspace/results/_f5_77_16items_reconciliation_2026_10_01.md` | `38be1dc9a33f` | 23930 | MATCH |
| 165 | `_september_workspace/results/_f5_d1_event_count_correction_2026_10_01.md` | `_september_workspace/results/_f5_d1_event_count_correction_2026_10_01.md` | `771641e234d6` | 24994 | MATCH |
| 166 | `_september_workspace/results/_f5_d1_event_count_correction_execution_2026_10_01.md` | `_september_workspace/results/_f5_d1_event_count_correction_execution_2026_10_01.md` | `44d8cc9cb4a5` | 24279 | MATCH |
| 167 | `_september_workspace/results/_fake_verdict_session_log_reverify_2026_09_30.md` | `_september_workspace/results/_fake_verdict_session_log_reverify_2026_09_30.md` | `c14094bdf815` | 25953 | MATCH |
| 168 | `_september_workspace/results/_five_items_effectivity_register_2026_10_11.md` | `_september_workspace/results/_five_items_effectivity_register_2026_10_11.md` | `8affdca64b4b` | 43332 | MATCH |
| 169 | `_september_workspace/results/_five_pending_items_drafts_2026_10_11.md` | `_september_workspace/results/_five_pending_items_drafts_2026_10_11.md` | `86c46998de63` | 55102 | MATCH |
| 170 | `_september_workspace/results/_five_stage_chain_design_reconstruction_2026_10_12.md` | `_september_workspace/results/_five_stage_chain_design_reconstruction_2026_10_12.md` | `bff2fb754564` | 12625 | MATCH |
| 171 | `_september_workspace/results/_forgotten_items_quick_sweep_register_2026_10_01.md` | `_september_workspace/results/_forgotten_items_quick_sweep_register_2026_10_01.md` | `91103473289a` | 43735 | MATCH |
| 172 | `_september_workspace/results/_forgotten_recovery_register_2026_09_29.md` | `_september_workspace/results/_forgotten_recovery_register_2026_09_29.md` | `d78be896bcb6` | 47494 | MATCH |
| 173 | `_september_workspace/results/_four_items_execution_batch_2026_10_11.md` | `_september_workspace/results/_four_items_execution_batch_2026_10_11.md` | `8006d1962e5f` | 31515 | MATCH |
| 174 | `_september_workspace/results/_fp3_anchor_and_krj_restrament_register_2026_10_11.md` | `_september_workspace/results/_fp3_anchor_and_krj_restrament_register_2026_10_11.md` | `b7c060ab2d49` | 32886 | MATCH |
| 175 | `_september_workspace/results/_freeze_receipt_2026_10_01_q1.md` | `_september_workspace/results/_freeze_receipt_2026_10_01_q1.md` | `9b7101bc09bd` | 698 | MATCH |
| 176 | `_september_workspace/results/_ftfb_order_judgment_2026_10_11.md` | `_september_workspace/results/_ftfb_order_judgment_2026_10_11.md` | `b6eec487e9d7` | 45911 | MATCH |
| 177 | `_september_workspace/results/_full_tidy_inventory_register_2026_09_30.md` | `_september_workspace/results/_full_tidy_inventory_register_2026_09_30.md` | `33f68dbfbd6f` | 27687 | MATCH |
| 178 | `_september_workspace/results/_g10_threshold_closed_domain_judgment_2026_10_11.md` | `_september_workspace/results/_g10_threshold_closed_domain_judgment_2026_10_11.md` | `586abda5ddf7` | 55727 | MATCH |
| 179 | `_september_workspace/results/_g11_krj4_effectivity_register_2026_10_11.md` | `_september_workspace/results/_g11_krj4_effectivity_register_2026_10_11.md` | `17168119eccc` | 39870 | MATCH |
| 180 | `_september_workspace/results/_g4_controlled_reproduction_design_2026_10_09.md` | `_september_workspace/results/_g4_controlled_reproduction_design_2026_10_09.md` | `b1c7c24926bb` | 23675 | MATCH |
| 181 | `_september_workspace/results/_g4_e3_definition_independent_judgment_2026_10_09.md` | `_september_workspace/results/_g4_e3_definition_independent_judgment_2026_10_09.md` | `aebaff5b503c` | 29094 | MATCH |
| 182 | `_september_workspace/results/_g4_e3_definition_ruling_material_2026_10_09.md` | `_september_workspace/results/_g4_e3_definition_ruling_material_2026_10_09.md` | `8ae4016bb41d` | 30662 | MATCH |
| 183 | `_september_workspace/results/_g4_reproduction_execution_register_2026_10_09.md` | `_september_workspace/results/_g4_reproduction_execution_register_2026_10_09.md` | `4daaf68cbf0e` | 20414 | MATCH |
| 184 | `_september_workspace/results/_g4_residual_probe_2026_10_08.md` | `_september_workspace/results/_g4_residual_probe_2026_10_08.md` | `3554aa156e08` | 23025 | MATCH |
| 185 | `_september_workspace/results/_g4_runtime_state_trace_2026_10_01.md` | `_september_workspace/results/_g4_runtime_state_trace_2026_10_01.md` | `e0ae0ad66acb` | 25631 | MATCH |
| 186 | `_september_workspace/results/_g4_skill_read_scope_trace_2026_10_01.md` | `_september_workspace/results/_g4_skill_read_scope_trace_2026_10_01.md` | `9196a608bb0d` | 26906 | MATCH |
| 187 | `_september_workspace/results/_g5_ccp_p0_verification_2026_10_10.md` | `_september_workspace/results/_g5_ccp_p0_verification_2026_10_10.md` | `8c7693379496` | 24819 | MATCH |
| 188 | `_september_workspace/results/_g5_displacement_threshold_c_approval_effect_and_trigger_eval_2026_10_10.md` | `_september_workspace/results/_g5_displacement_threshold_c_approval_effect_and_trigger_eval_2026_10_10.md` | `3015f2481df1` | 33880 | MATCH |
| 189 | `_september_workspace/results/_g5_displacement_threshold_draft_2026_10_10.md` | `_september_workspace/results/_g5_displacement_threshold_draft_2026_10_10.md` | `7c8107d9a8fb` | 25619 | MATCH |
| 190 | `_september_workspace/results/_g5_krj9_denominator_reconciliation_judgment_2026_10_10.md` | `_september_workspace/results/_g5_krj9_denominator_reconciliation_judgment_2026_10_10.md` | `22d90f12d605` | 45207 | MATCH |
| 191 | `_september_workspace/results/_g5_rejudgment_construction_question_judgment_2026_10_10.md` | `_september_workspace/results/_g5_rejudgment_construction_question_judgment_2026_10_10.md` | `ee660515d9e3` | 59309 | MATCH |
| 192 | `_september_workspace/results/_g5_rejudgment_c_applicability_recheck_2026_10_10.md` | `_september_workspace/results/_g5_rejudgment_c_applicability_recheck_2026_10_10.md` | `15301b3025fa` | 49051 | MATCH |
| 193 | `_september_workspace/results/_g5_rejudgment_face_prereg_2026_10_10.md` | `_september_workspace/results/_g5_rejudgment_face_prereg_2026_10_10.md` | `04495ef4b343` | 35097 | MATCH |
| 194 | `_september_workspace/results/_g5_rejudgment_trigger_caliber_judgment_2026_10_10.md` | `_september_workspace/results/_g5_rejudgment_trigger_caliber_judgment_2026_10_10.md` | `16c31894d445` | 48727 | MATCH |
| 195 | `_september_workspace/results/_g5_seg3_tie_veto_judgment_2026_10_10.md` | `_september_workspace/results/_g5_seg3_tie_veto_judgment_2026_10_10.md` | `3306d1fd020d` | 35983 | MATCH |
| 196 | `_september_workspace/results/_g5_x4_dual_axis_interpretation_judgment_2026_10_10.md` | `_september_workspace/results/_g5_x4_dual_axis_interpretation_judgment_2026_10_10.md` | `c3117773ab36` | 33976 | MATCH |
| 197 | `_september_workspace/results/_g9_read_b_effectivity_register_2026_10_11.md` | `_september_workspace/results/_g9_read_b_effectivity_register_2026_10_11.md` | `f5d601a0602a` | 29649 | MATCH |
| 198 | `_september_workspace/results/_gap_closeout_status_2026_10_09.md` | `_september_workspace/results/_gap_closeout_status_2026_10_09.md` | `ea41e346c4c4` | 28793 | MATCH |
| 199 | `_september_workspace/results/_gate_one_declared_adoption_register_2026_10_11.md` | `_september_workspace/results/_gate_one_declared_adoption_register_2026_10_11.md` | `3a965362d4f4` | 12923 | MATCH |
| 200 | `_september_workspace/results/_gate_one_pi_endorsement_register_2026_10_12.md` | `_september_workspace/results/_gate_one_pi_endorsement_register_2026_10_12.md` | `b09209e9c20d` | 9579 | MATCH |
| 201 | `_september_workspace/results/_give_up_n10_erratum_2026_10_10.md` | `_september_workspace/results/_give_up_n10_erratum_2026_10_10.md` | `e0db6b819138` | 22021 | MATCH |
| 202 | `_september_workspace/results/_give_up_semantics_draft_2026_10_10.md` | `_september_workspace/results/_give_up_semantics_draft_2026_10_10.md` | `b6a4ae82e038` | 23497 | MATCH |
| 203 | `_september_workspace/results/_glm_five_items_suggestion_table_2026_10_01.md` | `_september_workspace/results/_glm_five_items_suggestion_table_2026_10_01.md` | `f2b1359be37d` | 29622 | MATCH |
| 204 | `_september_workspace/results/_gt_recon_gamma_erratum_note_2026_10_01.md` | `_september_workspace/results/_gt_recon_gamma_erratum_note_2026_10_01.md` | `ca063e6b9d60` | 9103 | MATCH |
| 205 | `_september_workspace/results/_id_face_revision_sync_note_2026_10_10.md` | `_september_workspace/results/_id_face_revision_sync_note_2026_10_10.md` | `5d6c473731c4` | 20690 | MATCH |
| 206 | `_september_workspace/results/_j2_identifier_coupling_judgment_2026_10_11.md` | `_september_workspace/results/_j2_identifier_coupling_judgment_2026_10_11.md` | `2fd4505fdca2` | 34261 | MATCH |
| 207 | `_september_workspace/results/_j2_kj4_disposition_register_2026_10_11.md` | `_september_workspace/results/_j2_kj4_disposition_register_2026_10_11.md` | `c1a4ff1b96e5` | 34112 | MATCH |
| 208 | `_september_workspace/results/_kd04_c_denominator_closeout_register_2026_10_10.md` | `_september_workspace/results/_kd04_c_denominator_closeout_register_2026_10_10.md` | `78481cc60494` | 23029 | MATCH |
| 209 | `_september_workspace/results/_kd04_c_denominator_expansion_exec_2026_10_10.md` | `_september_workspace/results/_kd04_c_denominator_expansion_exec_2026_10_10.md` | `2caa3966b866` | 27915 | MATCH |
| 210 | `_september_workspace/results/_kd04_c_denominator_verdict_keeper_alternative_judgment_2026_10_10.md` | `_september_workspace/results/_kd04_c_denominator_verdict_keeper_alternative_judgment_2026_10_10.md` | `19ad36f7ec84` | 25123 | MATCH |
| 211 | `_september_workspace/results/_kd_19_ambiguous_tags_rejudge_rewrite_register_2026_10_10.md` | `_september_workspace/results/_kd_19_ambiguous_tags_rejudge_rewrite_register_2026_10_10.md` | `b508e5335377` | 29664 | MATCH |
| 212 | `_september_workspace/results/_kd_doc1_correction_adoption_register_2026_10_11.md` | `_september_workspace/results/_kd_doc1_correction_adoption_register_2026_10_11.md` | `c55770be5e33` | 10255 | MATCH |
| 213 | `_september_workspace/results/_kd_heteronym_classification_disposition_2026_10_09.md` | `_september_workspace/results/_kd_heteronym_classification_disposition_2026_10_09.md` | `c0cfd21d57a8` | 29761 | MATCH |
| 214 | `_september_workspace/results/_kd_legacy_rewrite_plan_2026_10_10.md` | `_september_workspace/results/_kd_legacy_rewrite_plan_2026_10_10.md` | `a9698fed8b9b` | 17643 | MATCH |
| 215 | `_september_workspace/results/_kd_legacy_rewrite_register_2026_10_10.md` | `_september_workspace/results/_kd_legacy_rewrite_register_2026_10_10.md` | `9a7936882a5d` | 14537 | MATCH |
| 216 | `_september_workspace/results/_kd_legacy_rewrite_ruling_2026_10_10.md` | `_september_workspace/results/_kd_legacy_rewrite_ruling_2026_10_10.md` | `2cadab5ed4f7` | 13731 | MATCH |
| 217 | `_september_workspace/results/_kd_login_register_section65_correction_2026_10_10.md` | `_september_workspace/results/_kd_login_register_section65_correction_2026_10_10.md` | `316d14c137bb` | 20422 | MATCH |
| 218 | `_september_workspace/results/_kd_resolvability_and_optional_experiments_2026_10_09.md` | `_september_workspace/results/_kd_resolvability_and_optional_experiments_2026_10_09.md` | `3138ac9095b0` | 70328 | MATCH |
| 219 | `_september_workspace/results/_kd_rewrite_fingerprint_sync_2026_10_10.md` | `_september_workspace/results/_kd_rewrite_fingerprint_sync_2026_10_10.md` | `aeefc94a94b5` | 20862 | MATCH |
| 220 | `_september_workspace/results/_kd_uncognizable_meaning_rewrite_register_2026_10_10.md` | `_september_workspace/results/_kd_uncognizable_meaning_rewrite_register_2026_10_10.md` | `b07887551f7c` | 19525 | MATCH |
| 221 | `_september_workspace/results/_kickoff_decisions_register_2026_10_08.md` | `_september_workspace/results/_kickoff_decisions_register_2026_10_08.md` | `6ee5d2b8323c` | 16388 | MATCH |
| 222 | `_september_workspace/results/_kimi_fullupload_r1_r4_rulings_register_2026_09_30.md` | `_september_workspace/results/_kimi_fullupload_r1_r4_rulings_register_2026_09_30.md` | `1c7445fca0de` | 4794 | MATCH |
| 223 | `_september_workspace/results/_kj1_abc_choice_judgment_2026_10_11.md` | `_september_workspace/results/_kj1_abc_choice_judgment_2026_10_11.md` | `d02ec6b0987e` | 42083 | MATCH |
| 224 | `_september_workspace/results/_kj1_eps_ls_effectivity_register_2026_10_11.md` | `_september_workspace/results/_kj1_eps_ls_effectivity_register_2026_10_11.md` | `809edb4bb1cc` | 62344 | MATCH |
| 225 | `_september_workspace/results/_kj1_judgment_premise_correction_2026_10_11.md` | `_september_workspace/results/_kj1_judgment_premise_correction_2026_10_11.md` | `003b134cce24` | 35050 | MATCH |
| 226 | `_september_workspace/results/_kj1_sc1_premise_correction_2026_10_11.md` | `_september_workspace/results/_kj1_sc1_premise_correction_2026_10_11.md` | `8b344b9b4715` | 31044 | MATCH |
| 227 | `_september_workspace/results/_kj4_e4_unification_judgment_2026_10_11.md` | `_september_workspace/results/_kj4_e4_unification_judgment_2026_10_11.md` | `a14d49f7d3a2` | 36839 | MATCH |
| 228 | `_september_workspace/results/_krj10_reverdict_after_r4_convergence_2026_10_11.md` | `_september_workspace/results/_krj10_reverdict_after_r4_convergence_2026_10_11.md` | `a21915ec55a7` | 31672 | MATCH |
| 229 | `_september_workspace/results/_krj10_terminal_verdict_closure_2026_10_11.md` | `_september_workspace/results/_krj10_terminal_verdict_closure_2026_10_11.md` | `f2e8e32089b2` | 14101 | MATCH |
| 230 | `_september_workspace/results/_krj4_trj1_adjudication_judgment_2026_10_11.md` | `_september_workspace/results/_krj4_trj1_adjudication_judgment_2026_10_11.md` | `50e91bf30e45` | 30293 | MATCH |
| 231 | `_september_workspace/results/_krj4_trj1_pick_and_pass_verdict_2026_10_11.md` | `_september_workspace/results/_krj4_trj1_pick_and_pass_verdict_2026_10_11.md` | `fb7bb5da85ec` | 16567 | MATCH |
| 232 | `_september_workspace/results/_krj5d_third_tier_effectivity_2026_10_11.md` | `_september_workspace/results/_krj5d_third_tier_effectivity_2026_10_11.md` | `062093d95c9f` | 10729 | MATCH |
| 233 | `_september_workspace/results/_krj5_final_disposition_verdict_2026_10_11.md` | `_september_workspace/results/_krj5_final_disposition_verdict_2026_10_11.md` | `2b6bf509a135` | 60700 | MATCH |
| 234 | `_september_workspace/results/_krj5_subject_scope_judgment_2026_10_11.md` | `_september_workspace/results/_krj5_subject_scope_judgment_2026_10_11.md` | `ae9df5119861` | 45372 | MATCH |
| 235 | `_september_workspace/results/_krj9_scope_clarification_draft_2026_10_10.md` | `_september_workspace/results/_krj9_scope_clarification_draft_2026_10_10.md` | `b17b3c38ec21` | 28654 | MATCH |
| 236 | `_september_workspace/results/_krj_all_five_verdicts_rewrite_2026_10_11.md` | `_september_workspace/results/_krj_all_five_verdicts_rewrite_2026_10_11.md` | `78fb8c47c944` | 72247 | MATCH |
| 237 | `_september_workspace/results/_krj_all_terminal_verdicts_2026_10_11.md` | `_september_workspace/results/_krj_all_terminal_verdicts_2026_10_11.md` | `f52231807e36` | 95659 | MATCH |
| 238 | `_september_workspace/results/_krj_cond4_bytes_erratum_2026_10_11.md` | `_september_workspace/results/_krj_cond4_bytes_erratum_2026_10_11.md` | `78a95e5561fc` | 3886 | MATCH |
| 239 | `_september_workspace/results/_krj_cond4_effectivity_declaration_2026_10_11.md` | `_september_workspace/results/_krj_cond4_effectivity_declaration_2026_10_11.md` | `f5c317f4cc96` | 15546 | MATCH |
| 240 | `_september_workspace/results/_krj_five_verdicts_adjudication_2026_10_11.md` | `_september_workspace/results/_krj_five_verdicts_adjudication_2026_10_11.md` | `5c0efd663847` | 16064 | MATCH |
| 241 | `_september_workspace/results/_krj_pi_picks_adoption_krj6_revise_2026_10_11.md` | `_september_workspace/results/_krj_pi_picks_adoption_krj6_revise_2026_10_11.md` | `31e32ccc59bf` | 15214 | MATCH |
| 242 | `_september_workspace/results/_kv3s_3_2_terminal_verdict_2026_10_01.md` | `_september_workspace/results/_kv3s_3_2_terminal_verdict_2026_10_01.md` | `b081d19be1b4` | 32296 | MATCH |
| 243 | `_september_workspace/results/_kv3s_4_1_2_rejudge_2026_10_09.md` | `_september_workspace/results/_kv3s_4_1_2_rejudge_2026_10_09.md` | `9cde399502ba` | 51594 | MATCH |
| 244 | `_september_workspace/results/_kv3s_4_4_carryover_bytes_correction_2026_10_10.md` | `_september_workspace/results/_kv3s_4_4_carryover_bytes_correction_2026_10_10.md` | `0a7d2ccf74ad` | 5807 | MATCH |
| 245 | `_september_workspace/results/_kv3s_4_4_review_carryover_2026_10_10.md` | `_september_workspace/results/_kv3s_4_4_review_carryover_2026_10_10.md` | `660d40ddd78c` | 17606 | MATCH |
| 246 | `_september_workspace/results/_kv3s_4_terminal_verdict_2026_10_09.md` | `_september_workspace/results/_kv3s_4_terminal_verdict_2026_10_09.md` | `e51317fcc5cf` | 50858 | MATCH |
| 247 | `_september_workspace/results/_kv3s_4_terminal_verdict_supplement_2026_10_09.md` | `_september_workspace/results/_kv3s_4_terminal_verdict_supplement_2026_10_09.md` | `0f82948defb3` | 20211 | MATCH |
| 248 | `_september_workspace/results/_k_cf_4_effectivity_register_2026_10_09.md` | `_september_workspace/results/_k_cf_4_effectivity_register_2026_10_09.md` | `edc6a548e3ca` | 35872 | MATCH |
| 249 | `_september_workspace/results/_k_cf_4_low_cardinality_recure_2026_10_09.md` | `_september_workspace/results/_k_cf_4_low_cardinality_recure_2026_10_09.md` | `5f91d553e392` | 33788 | MATCH |
| 250 | `_september_workspace/results/_k_cf_4_low_cardinality_reurecheck_and_precedent_fill_2026_10_09.md` | `_september_workspace/results/_k_cf_4_low_cardinality_reurecheck_and_precedent_fill_2026_10_09.md` | `618280cb8cfd` | 31801 | MATCH |
| 251 | `_september_workspace/results/_k_v3df_0_1_readings_verdict_2026_10_09.md` | `_september_workspace/results/_k_v3df_0_1_readings_verdict_2026_10_09.md` | `e98bee353448` | 37003 | MATCH |
| 252 | `_september_workspace/results/_k_v3df_9_1_c1_c4_legs_verdict_2026_10_09.md` | `_september_workspace/results/_k_v3df_9_1_c1_c4_legs_verdict_2026_10_09.md` | `a14aafa220c4` | 27735 | MATCH |
| 253 | `_september_workspace/results/_k_v3df_scope_two_judgments_2026_10_09.md` | `_september_workspace/results/_k_v3df_scope_two_judgments_2026_10_09.md` | `4b22ba3c463e` | 21350 | MATCH |
| 254 | `_september_workspace/results/_k_v3s_3_4_lock_freeze_2026_10_08.md` | `_september_workspace/results/_k_v3s_3_4_lock_freeze_2026_10_08.md` | `c64865c32761` | 16973 | MATCH |
| 255 | `_september_workspace/results/_k_v3s_4_2_domain_extension_judgment_2026_10_09.md` | `_september_workspace/results/_k_v3s_4_2_domain_extension_judgment_2026_10_09.md` | `a802af7ac3bc` | 23018 | MATCH |
| 256 | `_september_workspace/results/_letters_archive_register_2026_10_01.md` | `_september_workspace/results/_letters_archive_register_2026_10_01.md` | `9f0740da7e4d` | 26299 | MATCH |
| 257 | `_september_workspace/results/_limb_reading_verdict_kv3s33_2026_10_01.md` | `_september_workspace/results/_limb_reading_verdict_kv3s33_2026_10_01.md` | `c5866ce87d9c` | 56329 | MATCH |
| 258 | `_september_workspace/results/_lim_aperiod_adoption_and_label_correction_2026_10_11.md` | `_september_workspace/results/_lim_aperiod_adoption_and_label_correction_2026_10_11.md` | `f4b129e3312f` | 14770 | MATCH |
| 259 | `_september_workspace/results/_lim_aperiod_restatement_third_domain_2026_10_11.md` | `_september_workspace/results/_lim_aperiod_restatement_third_domain_2026_10_11.md` | `8672a5541ca8` | 27946 | MATCH |
| 260 | `_september_workspace/results/_linestand_pi_signoff_2026_10_01.md` | `_september_workspace/results/_linestand_pi_signoff_2026_10_01.md` | `cb5d933f8fae` | 35538 | MATCH |
| 261 | `_september_workspace/results/_linestand_trace_gap_note_2026_10_01.md` | `_september_workspace/results/_linestand_trace_gap_note_2026_10_01.md` | `91bb552bf76b` | 23252 | MATCH |
| 262 | `_september_workspace/results/_log_observation_review_2026_10_08.md` | `_september_workspace/results/_log_observation_review_2026_10_08.md` | `ae20780c8d4e` | 2918 | MATCH |
| 263 | `_september_workspace/results/_log_surface_scan_2026_10_08.md` | `_september_workspace/results/_log_surface_scan_2026_10_08.md` | `6b0b202c5a6c` | 3156 | MATCH |
| 264 | `_september_workspace/results/_m5_eps_drift_disposition_2026_10_11.md` | `_september_workspace/results/_m5_eps_drift_disposition_2026_10_11.md` | `0722f25f5838` | 2736 | MATCH |
| 265 | `_september_workspace/results/_mini_round_3_decisions_register_2026_10_01.md` | `_september_workspace/results/_mini_round_3_decisions_register_2026_10_01.md` | `bff06d3b3f97` | 44308 | MATCH |
| 266 | `_september_workspace/results/_mini_round_4_decisions_register_2026_10_01.md` | `_september_workspace/results/_mini_round_4_decisions_register_2026_10_01.md` | `0f2d1afcc793` | 37804 | MATCH |
| 267 | `_september_workspace/results/_mini_round_5_decisions_register_2026_10_01.md` | `_september_workspace/results/_mini_round_5_decisions_register_2026_10_01.md` | `d5fffe6a5e79` | 53125 | MATCH |
| 268 | `_september_workspace/results/_mini_round_6_7_settlement_register_2026_10_01.md` | `_september_workspace/results/_mini_round_6_7_settlement_register_2026_10_01.md` | `a87d1121b4ac` | 68053 | MATCH |
| 269 | `_september_workspace/results/_misformed_commission_drafts_deletion_register_2026_10_11.md` | `_september_workspace/results/_misformed_commission_drafts_deletion_register_2026_10_11.md` | `bbdc9c2c8028` | 7261 | MATCH |
| 270 | `_september_workspace/results/_morning_wrapup_pending_rulings_2026_10_01.md` | `_september_workspace/results/_morning_wrapup_pending_rulings_2026_10_01.md` | `2b6e8b527f93` | 7341 | MATCH |
| 271 | `_september_workspace/results/_m_r16_alias_table_draft_2026_10_01.md` | `_september_workspace/results/_m_r16_alias_table_draft_2026_10_01.md` | `0ba685b0d875` | 28128 | MATCH |
| 272 | `_september_workspace/results/_m_r16_alias_table_effective_2026_10_01.md` | `_september_workspace/results/_m_r16_alias_table_effective_2026_10_01.md` | `4ffdb809ef22` | 36578 | MATCH |
| 273 | `_september_workspace/results/_n01_n08_revision_2026_10_10.md` | `_september_workspace/results/_n01_n08_revision_2026_10_10.md` | `fa8400d8ae70` | 26628 | MATCH |
| 274 | `_september_workspace/results/_n1_d4_clause_placement_determination_2026_10_01.md` | `_september_workspace/results/_n1_d4_clause_placement_determination_2026_10_01.md` | `7cda6adea62b` | 53732 | MATCH |
| 275 | `_september_workspace/results/_n7_mutual_exclusion_determination_2026_10_01.md` | `_september_workspace/results/_n7_mutual_exclusion_determination_2026_10_01.md` | `b6bdf807cb27` | 40169 | MATCH |
| 276 | `_september_workspace/results/_naming_erratum_linestand_note_2026_10_01.md` | `_september_workspace/results/_naming_erratum_linestand_note_2026_10_01.md` | `38c8218d066b` | 12137 | MATCH |
| 277 | `_september_workspace/results/_overnight_delivery_index_2026_10_10.md` | `_september_workspace/results/_overnight_delivery_index_2026_10_10.md` | `266d0327025d` | 35344 | MATCH |
| 278 | `_september_workspace/results/_o_r2_r5_external_verification_2026_10_01.md` | `_september_workspace/results/_o_r2_r5_external_verification_2026_10_01.md` | `d03832d3e2ff` | 59327 | MATCH |
| 279 | `_september_workspace/results/_p4_attribution_determination_2026_10_01.md` | `_september_workspace/results/_p4_attribution_determination_2026_10_01.md` | `c6793cff46d7` | 22053 | MATCH |
| 280 | `_september_workspace/results/_p4_clause2_ratification_note_2026_10_01.md` | `_september_workspace/results/_p4_clause2_ratification_note_2026_10_01.md` | `cdf009712b96` | 26871 | MATCH |
| 281 | `_september_workspace/results/_pack_d_closeout_confirm_receipt_note_2026_10_01.md` | `_september_workspace/results/_pack_d_closeout_confirm_receipt_note_2026_10_01.md` | `15c18a28080f` | 35223 | MATCH |
| 282 | `_september_workspace/results/_pack_d_closeout_effectuation_note_2026_10_01.md` | `_september_workspace/results/_pack_d_closeout_effectuation_note_2026_10_01.md` | `97a3573e2a2d` | 27609 | MATCH |
| 283 | `_september_workspace/results/_pack_d_closeout_register_2026_10_01.md` | `_september_workspace/results/_pack_d_closeout_register_2026_10_01.md` | `0f1f94df75ba` | 62012 | MATCH |
| 284 | `_september_workspace/results/_pending_pi_items_drafts_2026_10_11.md` | `_september_workspace/results/_pending_pi_items_drafts_2026_10_11.md` | `55f469269d3d` | 40678 | MATCH |
| 285 | `_september_workspace/results/_pending_pi_items_master_register_2026_10_09.md` | `_september_workspace/results/_pending_pi_items_master_register_2026_10_09.md` | `87ab4929477f` | 35258 | MATCH |
| 286 | `_september_workspace/results/_pending_rulings_drafts_2026_10_11.md` | `_september_workspace/results/_pending_rulings_drafts_2026_10_11.md` | `c8428b883029` | 42775 | MATCH |
| 287 | `_september_workspace/results/_pending_supply_search_receipt_2026_10_08.md` | `_september_workspace/results/_pending_supply_search_receipt_2026_10_08.md` | `11bbee2bea42` | 12595 | MATCH |
| 288 | `_september_workspace/results/_phase1_completion_judgment_2026_10_10.md` | `_september_workspace/results/_phase1_completion_judgment_2026_10_10.md` | `6049c68f027b` | 28836 | MATCH |
| 289 | `_september_workspace/results/_pi_card_123_adoption_and_gate_one_request_2026_10_11.md` | `_september_workspace/results/_pi_card_123_adoption_and_gate_one_request_2026_10_11.md` | `0a4b752cbc56` | 13883 | MATCH |
| 290 | `_september_workspace/results/_pi_effectivity_declaration_register_2026_10_11.md` | `_september_workspace/results/_pi_effectivity_declaration_register_2026_10_11.md` | `41a82bde5190` | 54511 | MATCH |
| 291 | `_september_workspace/results/_pi_facing_items_screen_2026_10_09.md` | `_september_workspace/results/_pi_facing_items_screen_2026_10_09.md` | `a6d33cf318fe` | 59604 | MATCH |
| 292 | `_september_workspace/results/_pi_pending_items_draft_package_2026_10_09.md` | `_september_workspace/results/_pi_pending_items_draft_package_2026_10_09.md` | `8fa2a7a2c49d` | 51793 | MATCH |
| 293 | `_september_workspace/results/_pre_execution_report_kimi_2026_10_01.md` | `_september_workspace/results/_pre_execution_report_kimi_2026_10_01.md` | `941e1a68b2df` | 6277 | MATCH |
| 294 | `_september_workspace/results/_pre_exec_report_kimi_2026_09_30.md` | `_september_workspace/results/_pre_exec_report_kimi_2026_09_30.md` | `3e3ef9007a90` | 5677 | MATCH |
| 295 | `_september_workspace/results/_protocol_version_landing_status_2026_10_09.md` | `_september_workspace/results/_protocol_version_landing_status_2026_10_09.md` | `1d1895489d17` | 11562 | MATCH |
| 296 | `_september_workspace/results/_proxy_signoff_execution_register_2026_10_01.md` | `_september_workspace/results/_proxy_signoff_execution_register_2026_10_01.md` | `b6e5e15b70e5` | 20766 | MATCH |
| 297 | `_september_workspace/results/_p_refresh_registration_preliminary_2026_10_10.md` | `_september_workspace/results/_p_refresh_registration_preliminary_2026_10_10.md` | `a3e14b508a4a` | 32780 | MATCH |
| 298 | `_september_workspace/results/_p_refresh_s0_judgment_2026_10_10.md` | `_september_workspace/results/_p_refresh_s0_judgment_2026_10_10.md` | `369173063a7c` | 41449 | MATCH |
| 299 | `_september_workspace/results/_p_refresh_scope_judgment_2026_10_10.md` | `_september_workspace/results/_p_refresh_scope_judgment_2026_10_10.md` | `44e98dc31e2b` | 34004 | MATCH |
| 300 | `_september_workspace/results/_p_s4_1_revision_register_2026_10_09.md` | `_september_workspace/results/_p_s4_1_revision_register_2026_10_09.md` | `ad5c76111570` | 29961 | MATCH |
| 301 | `_september_workspace/results/_q2_scope_vs_revision_judgment_2026_10_11.md` | `_september_workspace/results/_q2_scope_vs_revision_judgment_2026_10_11.md` | `b4f00e5a69c4` | 43195 | MATCH |
| 302 | `_september_workspace/results/_q3_c1c4_l282_transposition_fix_executor_2026_10_09.py` | `_september_workspace/results/_q3_c1c4_l282_transposition_fix_executor_2026_10_09.py` | `e30d4032f195` | 64849 | MATCH |
| 303 | `_september_workspace/results/_q3_reported_value_errata_supplement_2026_10_10.md` | `_september_workspace/results/_q3_reported_value_errata_supplement_2026_10_10.md` | `e026f20839b1` | 12499 | MATCH |
| 304 | `_september_workspace/results/_q4_legacy_disposal_register_2026_10_01.md` | `_september_workspace/results/_q4_legacy_disposal_register_2026_10_01.md` | `a8763c406d4f` | 13336 | MATCH |
| 305 | `_september_workspace/results/_questionnaire_cards_intake_register_supplement_10_2026_10_10.md` | `_september_workspace/results/_questionnaire_cards_intake_register_supplement_10_2026_10_10.md` | `6c18d336e018` | 84127 | MATCH |
| 306 | `_september_workspace/results/_questionnaire_cards_intake_register_supplement_11_2026_10_10.md` | `_september_workspace/results/_questionnaire_cards_intake_register_supplement_11_2026_10_10.md` | `52c97d1c11e9` | 55341 | MATCH |
| 307 | `_september_workspace/results/_questionnaire_cards_intake_register_supplement_12_2026_10_10.md` | `_september_workspace/results/_questionnaire_cards_intake_register_supplement_12_2026_10_10.md` | `1ff6919967a7` | 121137 | MATCH |
| 308 | `_september_workspace/results/_questionnaire_cards_intake_register_supplement_13_2026_10_11.md` | `_september_workspace/results/_questionnaire_cards_intake_register_supplement_13_2026_10_11.md` | `43e0b642f8b2` | 114253 | MATCH |
| 309 | `_september_workspace/results/_questionnaire_cards_intake_register_supplement_14_2026_10_11.md` | `_september_workspace/results/_questionnaire_cards_intake_register_supplement_14_2026_10_11.md` | `79bc4bfe38a5` | 54883 | MATCH |
| 310 | `_september_workspace/results/_questionnaire_cards_intake_register_supplement_15_2026_10_11.md` | `_september_workspace/results/_questionnaire_cards_intake_register_supplement_15_2026_10_11.md` | `3654c41eda64` | 44698 | MATCH |
| 311 | `_september_workspace/results/_questionnaire_cards_intake_register_supplement_7_2026_10_10.md` | `_september_workspace/results/_questionnaire_cards_intake_register_supplement_7_2026_10_10.md` | `1fb8eac82781` | 52602 | MATCH |
| 312 | `_september_workspace/results/_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md` | `_september_workspace/results/_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md` | `a651f76a6547` | 17517 | MATCH |
| 313 | `_september_workspace/results/_questionnaire_cards_intake_register_supplement_8_2026_10_10.md` | `_september_workspace/results/_questionnaire_cards_intake_register_supplement_8_2026_10_10.md` | `29b30d845841` | 50790 | MATCH |
| 314 | `_september_workspace/results/_questionnaire_cards_intake_register_supplement_9_2026_10_10.md` | `_september_workspace/results/_questionnaire_cards_intake_register_supplement_9_2026_10_10.md` | `b6c0b4f29152` | 84422 | MATCH |
| 315 | `_september_workspace/results/_r1_amendment_undetermined_face_2026_10_01.md` | `_september_workspace/results/_r1_amendment_undetermined_face_2026_10_01.md` | `dab48b4d77c2` | 45128 | MATCH |
| 316 | `_september_workspace/results/_r2_reference_pointer_disposition_2026_10_11.md` | `_september_workspace/results/_r2_reference_pointer_disposition_2026_10_11.md` | `403adec92ce1` | 3121 | MATCH |
| 317 | `_september_workspace/results/_r2_verdict_179domain_arith_verification_2026_10_09.md` | `_september_workspace/results/_r2_verdict_179domain_arith_verification_2026_10_09.md` | `511c81b96745` | 30532 | MATCH |
| 318 | `_september_workspace/results/_r3_r4_interpretation_case_2026_10_01.md` | `_september_workspace/results/_r3_r4_interpretation_case_2026_10_01.md` | `46469217883b` | 64849 | MATCH |
| 319 | `_september_workspace/results/_r3_wording_disposition_2026_10_11.md` | `_september_workspace/results/_r3_wording_disposition_2026_10_11.md` | `9d381c9d95e6` | 3917 | MATCH |
| 320 | `_september_workspace/results/_r4_convergence_2026_10_11.md` | `_september_workspace/results/_r4_convergence_2026_10_11.md` | `678394c47724` | 3133 | MATCH |
| 321 | `_september_workspace/results/_r6_disposition_2026_10_11.md` | `_september_workspace/results/_r6_disposition_2026_10_11.md` | `cc51203fe8f5` | 3704 | MATCH |
| 322 | `_september_workspace/results/_reading_face_basis_rejudge_2026_10_10.md` | `_september_workspace/results/_reading_face_basis_rejudge_2026_10_10.md` | `3fe193a2a01f` | 24208 | MATCH |
| 323 | `_september_workspace/results/_readme_proper_batch_recheck_register_2026_09_30.md` | `_september_workspace/results/_readme_proper_batch_recheck_register_2026_09_30.md` | `2e530923457e` | 20781 | MATCH |
| 324 | `_september_workspace/results/_receipt_disposition_register_2026_10_08.md` | `_september_workspace/results/_receipt_disposition_register_2026_10_08.md` | `a79c3b82ee01` | 23050 | MATCH |
| 325 | `_september_workspace/results/_refcheck_hash_change_reference_recheck_2026_09_30.md` | `_september_workspace/results/_refcheck_hash_change_reference_recheck_2026_09_30.md` | `f011c29944b9` | 33625 | MATCH |
| 326 | `_september_workspace/results/_register3_bytes_erratum_2026_10_11.md` | `_september_workspace/results/_register3_bytes_erratum_2026_10_11.md` | `f9f6805a7b76` | 13294 | MATCH |
| 327 | `_september_workspace/results/_registry_lag_correction_batch_2026_10_01.md` | `_september_workspace/results/_registry_lag_correction_batch_2026_10_01.md` | `5b86fbf0cbbd` | 36367 | MATCH |
| 328 | `_september_workspace/results/_remote_residual_disposal_execution_order_2026_10_08.md` | `_september_workspace/results/_remote_residual_disposal_execution_order_2026_10_08.md` | `602c4d09623d` | 36486 | MATCH |
| 329 | `_september_workspace/results/_round19_followup_round21_22_approvals_effect_register_2026_10_10.md` | `_september_workspace/results/_round19_followup_round21_22_approvals_effect_register_2026_10_10.md` | `0c8dba07dd1e` | 54850 | MATCH |
| 330 | `_september_workspace/results/_round20_approvals_effect_register_2026_10_10.md` | `_september_workspace/results/_round20_approvals_effect_register_2026_10_10.md` | `29d737c59e8b` | 27711 | MATCH |
| 331 | `_september_workspace/results/_round23_26_threshold_review_effect_register_2026_10_10.md` | `_september_workspace/results/_round23_26_threshold_review_effect_register_2026_10_10.md` | `9b0c62765576` | 47297 | MATCH |
| 332 | `_september_workspace/results/_round27_34_approvals_effect_register_2026_10_10.md` | `_september_workspace/results/_round27_34_approvals_effect_register_2026_10_10.md` | `d0bc0b1a9ae0` | 73226 | MATCH |
| 333 | `_september_workspace/results/_round45_dispositions_effect_register_2026_10_10.md` | `_september_workspace/results/_round45_dispositions_effect_register_2026_10_10.md` | `d66a1076952a` | 19803 | MATCH |
| 334 | `_september_workspace/results/_round51_effectivity_register_2026_10_10.md` | `_september_workspace/results/_round51_effectivity_register_2026_10_10.md` | `b8b0c52296b2` | 27070 | MATCH |
| 335 | `_september_workspace/results/_round52_e6b_caliber_naming_effectivity_register_2026_10_10.md` | `_september_workspace/results/_round52_e6b_caliber_naming_effectivity_register_2026_10_10.md` | `e861c7bc19ad` | 21788 | MATCH |
| 336 | `_september_workspace/results/_round52_s4_e4b_ad5_type_effectivity_register_2026_10_10.md` | `_september_workspace/results/_round52_s4_e4b_ad5_type_effectivity_register_2026_10_10.md` | `debd88fc150c` | 45351 | MATCH |
| 337 | `_september_workspace/results/_round53_rejudge_prereg_freeze_effectivity_register_2026_10_10.md` | `_september_workspace/results/_round53_rejudge_prereg_freeze_effectivity_register_2026_10_10.md` | `b27814792394` | 25637 | MATCH |
| 338 | `_september_workspace/results/_round53_th_v3_19_landfall_schema_effectivity_register_2026_10_10.md` | `_september_workspace/results/_round53_th_v3_19_landfall_schema_effectivity_register_2026_10_10.md` | `4c3a6dc0070d` | 20023 | MATCH |
| 339 | `_september_workspace/results/_round54_g5_dispositions_register_2026_10_10.md` | `_september_workspace/results/_round54_g5_dispositions_register_2026_10_10.md` | `afc67818bb85` | 39977 | MATCH |
| 340 | `_september_workspace/results/_round55_dispositions_register_2026_10_10.md` | `_september_workspace/results/_round55_dispositions_register_2026_10_10.md` | `002fa0a9a5e4` | 34913 | MATCH |
| 341 | `_september_workspace/results/_round56a_dispositions_register_2026_10_10.md` | `_september_workspace/results/_round56a_dispositions_register_2026_10_10.md` | `d8980cfae7f7` | 50365 | MATCH |
| 342 | `_september_workspace/results/_round56c_card_id_erratum_2026_10_10.md` | `_september_workspace/results/_round56c_card_id_erratum_2026_10_10.md` | `f6c2d40f18ff` | 18747 | MATCH |
| 343 | `_september_workspace/results/_round56c_d23_ad5_judgment_2026_10_10.md` | `_september_workspace/results/_round56c_d23_ad5_judgment_2026_10_10.md` | `061813859345` | 50747 | MATCH |
| 344 | `_september_workspace/results/_round56r8_dispositions_register_2026_10_10.md` | `_september_workspace/results/_round56r8_dispositions_register_2026_10_10.md` | `cfb08d0e15f4` | 46135 | MATCH |
| 345 | `_september_workspace/results/_round56r9r10_dispositions_register_2026_10_10.md` | `_september_workspace/results/_round56r9r10_dispositions_register_2026_10_10.md` | `0eb408ae60f5` | 49754 | MATCH |
| 346 | `_september_workspace/results/_round56_ad8fix_effectivity_register_2026_10_10.md` | `_september_workspace/results/_round56_ad8fix_effectivity_register_2026_10_10.md` | `2e7f86314428` | 16553 | MATCH |
| 347 | `_september_workspace/results/_round56_b01_followup_disposition_plan_2026_10_10.md` | `_september_workspace/results/_round56_b01_followup_disposition_plan_2026_10_10.md` | `857fb940a43c` | 31004 | MATCH |
| 348 | `_september_workspace/results/_round56_direct_adoptions_register_2026_10_10.md` | `_september_workspace/results/_round56_direct_adoptions_register_2026_10_10.md` | `e3c56c5d0a97` | 43240 | MATCH |
| 349 | `_september_workspace/results/_round56_direct_adoptions_register_2_2026_10_10.md` | `_september_workspace/results/_round56_direct_adoptions_register_2_2026_10_10.md` | `f8e0fa28c067` | 26690 | MATCH |
| 350 | `_september_workspace/results/_round56_g2_enable_and_v1_rule_register_2026_10_10.md` | `_september_workspace/results/_round56_g2_enable_and_v1_rule_register_2026_10_10.md` | `936f551f0fd3` | 34181 | MATCH |
| 351 | `_september_workspace/results/_round56_gu_backdoor_exclusion_revision_2026_10_10.md` | `_september_workspace/results/_round56_gu_backdoor_exclusion_revision_2026_10_10.md` | `52d3b10a16a0` | 25045 | MATCH |
| 352 | `_september_workspace/results/_round56_idx_sc1_resolution_2026_10_10.md` | `_september_workspace/results/_round56_idx_sc1_resolution_2026_10_10.md` | `9b41f2a38b2f` | 47107 | MATCH |
| 353 | `_september_workspace/results/_round56_idx_sc1_temp_deletion_deviation_note_2026_10_10.md` | `_september_workspace/results/_round56_idx_sc1_temp_deletion_deviation_note_2026_10_10.md` | `c72086990450` | 8181 | MATCH |
| 354 | `_september_workspace/results/_round56_n10_erratum_register_2026_10_10.md` | `_september_workspace/results/_round56_n10_erratum_register_2026_10_10.md` | `599d0450434e` | 20321 | MATCH |
| 355 | `_september_workspace/results/_round56_pending_questions_compilation_2026_10_10.md` | `_september_workspace/results/_round56_pending_questions_compilation_2026_10_10.md` | `ef09b3d28a0f` | 33504 | MATCH |
| 356 | `_september_workspace/results/_round56_pending_questions_compilation_supplement_note_2026_10_10.md` | `_september_workspace/results/_round56_pending_questions_compilation_supplement_note_2026_10_10.md` | `421c936f6ae8` | 29019 | MATCH |
| 357 | `_september_workspace/results/_round56_registration_supplement_2026_10_10.md` | `_september_workspace/results/_round56_registration_supplement_2026_10_10.md` | `71a59735302c` | 21865 | MATCH |
| 358 | `_september_workspace/results/_round56_review_effectivity_register_2026_10_10.md` | `_september_workspace/results/_round56_review_effectivity_register_2026_10_10.md` | `da6b55162e50` | 49013 | MATCH |
| 359 | `_september_workspace/results/_round56_review_effectivity_register_3_2026_10_10.md` | `_september_workspace/results/_round56_review_effectivity_register_3_2026_10_10.md` | `84ed13256250` | 77181 | MATCH |
| 360 | `_september_workspace/results/_round56_review_effectivity_register_4_2026_10_11.md` | `_september_workspace/results/_round56_review_effectivity_register_4_2026_10_11.md` | `ee31bb8a94fe` | 46908 | MATCH |
| 361 | `_september_workspace/results/_round56_review_effectivity_register_5_2026_10_11.md` | `_september_workspace/results/_round56_review_effectivity_register_5_2026_10_11.md` | `5deba7d27bb1` | 67613 | MATCH |
| 362 | `_september_workspace/results/_round56_review_effectivity_register_6_2026_10_11.md` | `_september_workspace/results/_round56_review_effectivity_register_6_2026_10_11.md` | `2f3255ea344f` | 58478 | MATCH |
| 363 | `_september_workspace/results/_round56_sc4_nstar_inconsistency_erratum_2026_10_10.md` | `_september_workspace/results/_round56_sc4_nstar_inconsistency_erratum_2026_10_10.md` | `af4c3335538a` | 16640 | MATCH |
| 364 | `_september_workspace/results/_round56_shortname_backfill_note_2026_10_10.md` | `_september_workspace/results/_round56_shortname_backfill_note_2026_10_10.md` | `bb2444cccd65` | 22195 | MATCH |
| 365 | `_september_workspace/results/_round56_terminal_boundary_effectivity_register_2026_10_10.md` | `_september_workspace/results/_round56_terminal_boundary_effectivity_register_2026_10_10.md` | `d5bf826278cb` | 35878 | MATCH |
| 366 | `_september_workspace/results/_round56_th3_coverage_line_effectivity_register_2026_10_10.md` | `_september_workspace/results/_round56_th3_coverage_line_effectivity_register_2026_10_10.md` | `6794fb09ce7e` | 28378 | MATCH |
| 367 | `_september_workspace/results/_round56_th4_two_field_reporting_resolution_2026_10_10.md` | `_september_workspace/results/_round56_th4_two_field_reporting_resolution_2026_10_10.md` | `71894a686e92` | 28233 | MATCH |
| 368 | `_september_workspace/results/_round56_typeb_backfill_register_2026_10_10.md` | `_september_workspace/results/_round56_typeb_backfill_register_2026_10_10.md` | `607ded06d840` | 40253 | MATCH |
| 369 | `_september_workspace/results/_round56_typeb_form_draft_2026_10_10.md` | `_september_workspace/results/_round56_typeb_form_draft_2026_10_10.md` | `582c5fb9970c` | 50170 | MATCH |
| 370 | `_september_workspace/results/_round56_typeb_implementation_register_2026_10_10.md` | `_september_workspace/results/_round56_typeb_implementation_register_2026_10_10.md` | `c296a7833a70` | 26367 | MATCH |
| 371 | `_september_workspace/results/_round56_v4_kd_row_correction_revision_2026_10_10.md` | `_september_workspace/results/_round56_v4_kd_row_correction_revision_2026_10_10.md` | `6d8537cb127f` | 23453 | MATCH |
| 372 | `_september_workspace/results/_rpq_wordlist_and_t1p2_judgments_2026_10_09.md` | `_september_workspace/results/_rpq_wordlist_and_t1p2_judgments_2026_10_09.md` | `246ce35c4ddc` | 44796 | MATCH |
| 373 | `_september_workspace/results/_r_pair_interval_statement_errata_2026_10_09.md` | `_september_workspace/results/_r_pair_interval_statement_errata_2026_10_09.md` | `61944eb91b72` | 9259 | MATCH |
| 374 | `_september_workspace/results/_r_pair_nonportrait_full_document_review_2026_10_09.md` | `_september_workspace/results/_r_pair_nonportrait_full_document_review_2026_10_09.md` | `d8d5e4d2154f` | 28176 | MATCH |
| 375 | `_september_workspace/results/_r_pair_rp3b_rp2_rpq6_judgments_2026_10_09.md` | `_september_workspace/results/_r_pair_rp3b_rp2_rpq6_judgments_2026_10_09.md` | `5faa16446171` | 23975 | MATCH |
| 376 | `_september_workspace/results/_r_pair_texts_independent_review_2026_10_09.md` | `_september_workspace/results/_r_pair_texts_independent_review_2026_10_09.md` | `8c5f83c3c4cf` | 35443 | MATCH |
| 377 | `_september_workspace/results/_s1prime_trigger_caliber_reevaluation_2026_10_10.md` | `_september_workspace/results/_s1prime_trigger_caliber_reevaluation_2026_10_10.md` | `d2326973aaf8` | 29991 | MATCH |
| 378 | `_september_workspace/results/_s2prime_krj3_applicability_recheck_2026_10_10.md` | `_september_workspace/results/_s2prime_krj3_applicability_recheck_2026_10_10.md` | `10518510b628` | 41322 | MATCH |
| 379 | `_september_workspace/results/_s3prime_recompute_after_supplement_2026_10_11.md` | `_september_workspace/results/_s3prime_recompute_after_supplement_2026_10_11.md` | `fa025e4dc166` | 41708 | MATCH |
| 380 | `_september_workspace/results/_s3_c4_recount_2026_10_01.md` | `_september_workspace/results/_s3_c4_recount_2026_10_01.md` | `86af4c109519` | 32025 | MATCH |
| 381 | `_september_workspace/results/_s3_closeout_rules_case_2026_10_01.md` | `_september_workspace/results/_s3_closeout_rules_case_2026_10_01.md` | `7e622691aec1` | 52659 | MATCH |
| 382 | `_september_workspace/results/_s3_d1_rulings_supplement_register_2026_10_01.md` | `_september_workspace/results/_s3_d1_rulings_supplement_register_2026_10_01.md` | `4ce661acc81f` | 28762 | MATCH |
| 383 | `_september_workspace/results/_s3_f1_loader_fix_recompute_2026_10_08.md` | `_september_workspace/results/_s3_f1_loader_fix_recompute_2026_10_08.md` | `b2c9840d237b` | 22065 | MATCH |
| 384 | `_september_workspace/results/_s3_kv3s_3_verdict_2026_10_01.md` | `_september_workspace/results/_s3_kv3s_3_verdict_2026_10_01.md` | `e394bb6b5ddf` | 35037 | MATCH |
| 385 | `_september_workspace/results/_s3_missing_field_backfill_rule_draft_2026_10_01.md` | `_september_workspace/results/_s3_missing_field_backfill_rule_draft_2026_10_01.md` | `8496a53d183a` | 35827 | MATCH |
| 386 | `_september_workspace/results/_s3_missing_field_backfill_rule_effective_2026_10_01.md` | `_september_workspace/results/_s3_missing_field_backfill_rule_effective_2026_10_01.md` | `1450057b0819` | 52469 | MATCH |
| 387 | `_september_workspace/results/_s4prime_five_lines_readings_2026_10_11.md` | `_september_workspace/results/_s4prime_five_lines_readings_2026_10_11.md` | `e91e7f52c726` | 23877 | MATCH |
| 388 | `_september_workspace/results/_s4prime_readings_runner_2026_10_11.py` | `_september_workspace/results/_s4prime_readings_runner_2026_10_11.py` | `0aa414188361` | 23766 | MATCH |
| 389 | `_september_workspace/results/_s4q04_level_attribution_judgment_2026_10_10.md` | `_september_workspace/results/_s4q04_level_attribution_judgment_2026_10_10.md` | `49a07216a1bb` | 26407 | MATCH |
| 390 | `_september_workspace/results/_s4_abcreadings_reproducibility_check_2026_10_10.md` | `_september_workspace/results/_s4_abcreadings_reproducibility_check_2026_10_10.md` | `892e5dfe3ed1` | 25234 | MATCH |
| 391 | `_september_workspace/results/_s4_bc_construction_ruling_2026_10_09.md` | `_september_workspace/results/_s4_bc_construction_ruling_2026_10_09.md` | `e2fdb380cd3c` | 30257 | MATCH |
| 392 | `_september_workspace/results/_s4_chain_clearance_register_2026_10_09.md` | `_september_workspace/results/_s4_chain_clearance_register_2026_10_09.md` | `eda3d304d381` | 2684 | MATCH |
| 393 | `_september_workspace/results/_s4_corpus_scope_hard_constraint_judgment_2026_10_10.md` | `_september_workspace/results/_s4_corpus_scope_hard_constraint_judgment_2026_10_10.md` | `c7609657dfe4` | 44199 | MATCH |
| 394 | `_september_workspace/results/_s4_dkb_backfill_register_2026_10_10.md` | `_september_workspace/results/_s4_dkb_backfill_register_2026_10_10.md` | `3a992c3fe235` | 25591 | MATCH |
| 395 | `_september_workspace/results/_s4_e4b_ad5_type_separate_judgment_2026_10_10.md` | `_september_workspace/results/_s4_e4b_ad5_type_separate_judgment_2026_10_10.md` | `f48601fee958` | 51898 | MATCH |
| 396 | `_september_workspace/results/_s4_e4_axis_disposition_axis2_run_2026_10_10.md` | `_september_workspace/results/_s4_e4_axis_disposition_axis2_run_2026_10_10.md` | `2bda07af86fc` | 29700 | MATCH |
| 397 | `_september_workspace/results/_s4_empty_sequence_backfill_assessment_2026_10_10.md` | `_september_workspace/results/_s4_empty_sequence_backfill_assessment_2026_10_10.md` | `41b75ffea7be` | 28771 | MATCH |
| 398 | `_september_workspace/results/_s4_face_closeout_2026_10_09.md` | `_september_workspace/results/_s4_face_closeout_2026_10_09.md` | `f7d76eda2911` | 29158 | MATCH |
| 399 | `_september_workspace/results/_s4_face_dual_files_verification_2026_10_09.md` | `_september_workspace/results/_s4_face_dual_files_verification_2026_10_09.md` | `cc3fc6eebc6b` | 40228 | MATCH |
| 400 | `_september_workspace/results/_s4_face_five_lines_ci_readings_2026_10_09.md` | `_september_workspace/results/_s4_face_five_lines_ci_readings_2026_10_09.md` | `bea9bc43a8f3` | 39462 | MATCH |
| 401 | `_september_workspace/results/_s4_feature_surface_v3_1_definition_2026_10_10.md` | `_september_workspace/results/_s4_feature_surface_v3_1_definition_2026_10_10.md` | `d044ce1c069d` | 30310 | MATCH |
| 402 | `_september_workspace/results/_s4_final_ruling_card_register_2026_10_09.md` | `_september_workspace/results/_s4_final_ruling_card_register_2026_10_09.md` | `f62401b619cc` | 2135 | MATCH |
| 403 | `_september_workspace/results/_s4_heldout_sampling_seed42_items_register_2026_10_09.md` | `_september_workspace/results/_s4_heldout_sampling_seed42_items_register_2026_10_09.md` | `73a02ac5937d` | 34689 | MATCH |
| 404 | `_september_workspace/results/_s4_heldout_sampling_seed42_register_2026_10_09.md` | `_september_workspace/results/_s4_heldout_sampling_seed42_register_2026_10_09.md` | `2a2ad5c2e29f` | 37615 | MATCH |
| 405 | `_september_workspace/results/_s4_heldout_sampling_seed42_sets_2026_10_09.json` | `_september_workspace/results/_s4_heldout_sampling_seed42_sets_2026_10_09.json` | `8dfc9e0d8bf9` | 59100 | MATCH |
| 406 | `_september_workspace/results/_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` | `_september_workspace/results/_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` | `1bf6f47a590d` | 18923 | MATCH |
| 407 | `_september_workspace/results/_s4_heldout_sampling_seedthird_extractor_2026_10_11.py` | `_september_workspace/results/_s4_heldout_sampling_seedthird_extractor_2026_10_11.py` | `068e1a7a1d04` | 52655 | MATCH |
| 408 | `_september_workspace/results/_s4_heldout_seedprime_verification_2026_10_10.md` | `_september_workspace/results/_s4_heldout_seedprime_verification_2026_10_10.md` | `8c64314d0ec0` | 21966 | MATCH |
| 409 | `_september_workspace/results/_s4_keyword_expansion_and_regen_design_2026_10_10.md` | `_september_workspace/results/_s4_keyword_expansion_and_regen_design_2026_10_10.md` | `6efddab54ca5` | 31149 | MATCH |
| 410 | `_september_workspace/results/_s4_reading_surface_and_authority_register_2026_10_09.md` | `_september_workspace/results/_s4_reading_surface_and_authority_register_2026_10_09.md` | `0148b5271154` | 34405 | MATCH |
| 411 | `_september_workspace/results/_s4_regen_traceability_judgment_2026_10_10.md` | `_september_workspace/results/_s4_regen_traceability_judgment_2026_10_10.md` | `a330273b981c` | 36071 | MATCH |
| 412 | `_september_workspace/results/_s4_revision_effectiveness_register_2026_10_09.md` | `_september_workspace/results/_s4_revision_effectiveness_register_2026_10_09.md` | `356fe8509669` | 32820 | MATCH |
| 413 | `_september_workspace/results/_s4_terminal_face_recompute_2026_10_09.md` | `_september_workspace/results/_s4_terminal_face_recompute_2026_10_09.md` | `b412342eabec` | 46701 | MATCH |
| 414 | `_september_workspace/results/_s4_topup_intake_verdict_2026_10_09.md` | `_september_workspace/results/_s4_topup_intake_verdict_2026_10_09.md` | `658d7f3ab231` | 33799 | MATCH |
| 415 | `_september_workspace/results/_s4_tree_construct_adjustment_exec_2026_10_10.md` | `_september_workspace/results/_s4_tree_construct_adjustment_exec_2026_10_10.md` | `b6b47008f8fd` | 28515 | MATCH |
| 416 | `_september_workspace/results/_s4_tree_prereg_revision_2026_10_10.md` | `_september_workspace/results/_s4_tree_prereg_revision_2026_10_10.md` | `037140972829` | 30382 | MATCH |
| 417 | `_september_workspace/results/_s4_v11_axis2_displacement_items_2026_10_10.json` | `_september_workspace/results/_s4_v11_axis2_displacement_items_2026_10_10.json` | `0eed9053619c` | 9941 | MATCH |
| 418 | `_september_workspace/results/_s4_v31_displacement_register_face2_2026_10_10.md` | `_september_workspace/results/_s4_v31_displacement_register_face2_2026_10_10.md` | `b6ce4a79116e` | 17736 | MATCH |
| 419 | `_september_workspace/results/_s4_v31_exec_section8_errata_2026_10_10.md` | `_september_workspace/results/_s4_v31_exec_section8_errata_2026_10_10.md` | `ec11aec2380d` | 23250 | MATCH |
| 420 | `_september_workspace/results/_s4_w1_3636_consistency_check_2026_10_10.md` | `_september_workspace/results/_s4_w1_3636_consistency_check_2026_10_10.md` | `0e9ae4b6ee8c` | 29196 | MATCH |
| 421 | `_september_workspace/results/_s4_w2bc_effect_registration_2026_10_10.md` | `_september_workspace/results/_s4_w2bc_effect_registration_2026_10_10.md` | `b24a8411a260` | 26418 | MATCH |
| 422 | `_september_workspace/results/_s4_w2_disposition_registration_2026_10_10.md` | `_september_workspace/results/_s4_w2_disposition_registration_2026_10_10.md` | `566c2f0ad7e8` | 23545 | MATCH |
| 423 | `_september_workspace/results/_s4_w2_e4_separate_judgment_2026_10_10.md` | `_september_workspace/results/_s4_w2_e4_separate_judgment_2026_10_10.md` | `a51bd6530075` | 37607 | MATCH |
| 424 | `_september_workspace/results/_s5doubleprime_five_lines_runner_2026_10_11.py` | `_september_workspace/results/_s5doubleprime_five_lines_runner_2026_10_11.py` | `9de3c08e3863` | 31138 | MATCH |
| 425 | `_september_workspace/results/_s5dp_mixed_object_erratum_2026_10_11.md` | `_september_workspace/results/_s5dp_mixed_object_erratum_2026_10_11.md` | `07cde000e66f` | 8380 | MATCH |
| 426 | `_september_workspace/results/_s5prime_double_lim_a_and_item_registers_2026_10_11.md` | `_september_workspace/results/_s5prime_double_lim_a_and_item_registers_2026_10_11.md` | `9a62fb2a6956` | 58378 | MATCH |
| 427 | `_september_workspace/results/_s5prime_lim_a_and_item_registers_2026_10_11.md` | `_september_workspace/results/_s5prime_lim_a_and_item_registers_2026_10_11.md` | `fa74831fa0ad` | 47225 | MATCH |
| 428 | `_september_workspace/results/_s6doubleprime_terminal_verdicts_2026_10_11.md` | `_september_workspace/results/_s6doubleprime_terminal_verdicts_2026_10_11.md` | `bba3b889d849` | 76910 | MATCH |
| 429 | `_september_workspace/results/_s6doubleprime_verdict_supplement_2026_10_11.md` | `_september_workspace/results/_s6doubleprime_verdict_supplement_2026_10_11.md` | `8e19c10ce219` | 31515 | MATCH |
| 430 | `_september_workspace/results/_s6prime_terminal_verdicts_2026_10_11.md` | `_september_workspace/results/_s6prime_terminal_verdicts_2026_10_11.md` | `1c8ce58d6484` | 54937 | MATCH |
| 431 | `_september_workspace/results/_s7doubleprime_verification_2026_10_11.md` | `_september_workspace/results/_s7doubleprime_verification_2026_10_11.md` | `06ac684b4923` | 41680 | MATCH |
| 432 | `_september_workspace/results/_s7doubleprime_verification_erratum_2026_10_11.md` | `_september_workspace/results/_s7doubleprime_verification_erratum_2026_10_11.md` | `9ff40693e4ac` | 32822 | MATCH |
| 433 | `_september_workspace/results/_s7prime_findings_erratum_2026_10_11.md` | `_september_workspace/results/_s7prime_findings_erratum_2026_10_11.md` | `a7dfa8e789b7` | 31008 | MATCH |
| 434 | `_september_workspace/results/_s7prime_prereq_and_verification_2026_10_11.md` | `_september_workspace/results/_s7prime_prereq_and_verification_2026_10_11.md` | `e44da4b83810` | 36787 | MATCH |
| 435 | `_september_workspace/results/_seed_double_criterion_draft_2026_10_11.md` | `_september_workspace/results/_seed_double_criterion_draft_2026_10_11.md` | `025212e91546` | 40499 | MATCH |
| 436 | `_september_workspace/results/_seed_double_identifier_final_judgment_2026_10_11.md` | `_september_workspace/results/_seed_double_identifier_final_judgment_2026_10_11.md` | `728d18391748` | 50222 | MATCH |
| 437 | `_september_workspace/results/_seed_double_rule_judgment_2026_10_11.md` | `_september_workspace/results/_seed_double_rule_judgment_2026_10_11.md` | `f70a689fd8c1` | 57185 | MATCH |
| 438 | `_september_workspace/results/_seven_gap_closures_adoption_register_2026_10_11.md` | `_september_workspace/results/_seven_gap_closures_adoption_register_2026_10_11.md` | `ac3c41663f84` | 11960 | MATCH |
| 439 | `_september_workspace/results/_skill_cache_inventory_and_reference_update_advice_2026_09_30.md` | `_september_workspace/results/_skill_cache_inventory_and_reference_update_advice_2026_09_30.md` | `c14489750416` | 31692 | MATCH |
| 440 | `_september_workspace/results/_skill_call_surface_probe_2026_09_30.md` | `_september_workspace/results/_skill_call_surface_probe_2026_09_30.md` | `112346df64fb` | 32261 | MATCH |
| 441 | `_september_workspace/results/_skill_call_surface_probe_supplement_a_2026_09_30.md` | `_september_workspace/results/_skill_call_surface_probe_supplement_a_2026_09_30.md` | `a06316c3c7f2` | 50658 | MATCH |
| 442 | `_september_workspace/results/_skill_call_surface_probe_supplement_b_2026_09_30.md` | `_september_workspace/results/_skill_call_surface_probe_supplement_b_2026_09_30.md` | `69d311e6a4c7` | 82744 | MATCH |
| 443 | `_september_workspace/results/_skill_directory_update_and_addressing_rule_2026_10_01.md` | `_september_workspace/results/_skill_directory_update_and_addressing_rule_2026_10_01.md` | `4a3a2d0c5b95` | 20335 | MATCH |
| 444 | `_september_workspace/results/_skill_erratum_and_parent_success_note_2026_09_30.md` | `_september_workspace/results/_skill_erratum_and_parent_success_note_2026_09_30.md` | `7a64949402d9` | 24143 | MATCH |
| 445 | `_september_workspace/results/_skill_load_failure_window_readonly_facts_2026_09_30.md` | `_september_workspace/results/_skill_load_failure_window_readonly_facts_2026_09_30.md` | `9f5b73620b8a` | 23065 | MATCH |
| 446 | `_september_workspace/results/_skill_reference_erratum_and_runtime_anchor_experiment_2026_09_30.md` | `_september_workspace/results/_skill_reference_erratum_and_runtime_anchor_experiment_2026_09_30.md` | `16861e71305f` | 30771 | MATCH |
| 447 | `_september_workspace/results/_stage1_tail_caliber_unification_register_2026_10_11.md` | `_september_workspace/results/_stage1_tail_caliber_unification_register_2026_10_11.md` | `d486ec491e8e` | 41140 | MATCH |
| 448 | `_september_workspace/results/_stage2_trae_reply_acceptance_register_2026_10_12.md` | `_september_workspace/results/_stage2_trae_reply_acceptance_register_2026_10_12.md` | `ce0b5a64cfce` | 14874 | MATCH |
| 449 | `_september_workspace/results/_stage3_extraction_verification_2026_10_11.md` | `_september_workspace/results/_stage3_extraction_verification_2026_10_11.md` | `f973e6d737c3` | 22399 | MATCH |
| 450 | `_september_workspace/results/_stage3_open_and_mandate_register_2026_10_12.md` | `_september_workspace/results/_stage3_open_and_mandate_register_2026_10_12.md` | `1b0a109a7914` | 13865 | MATCH |
| 451 | `_september_workspace/results/_stage3_readings_verification_2026_10_11.md` | `_september_workspace/results/_stage3_readings_verification_2026_10_11.md` | `023a0cdd3350` | 29956 | MATCH |
| 452 | `_september_workspace/results/_stage3_trigger_readings_2026_10_11.md` | `_september_workspace/results/_stage3_trigger_readings_2026_10_11.md` | `2900948bca6d` | 35711 | MATCH |
| 453 | `_september_workspace/results/_sub_artifact_ledger_history_r5_2026_10_01.md` | `_september_workspace/results/_sub_artifact_ledger_history_r5_2026_10_01.md` | `372a53b9e832` | 35845 | MATCH |
| 454 | `_september_workspace/results/_sub_transfer_candidates_2026_10_01.md` | `_september_workspace/results/_sub_transfer_candidates_2026_10_01.md` | `2f61c0aa2a2b` | 21796 | MATCH |
| 455 | `_september_workspace/results/_sub_transfer_execution_register_2026_10_01.md` | `_september_workspace/results/_sub_transfer_execution_register_2026_10_01.md` | `c41013a975e0` | 13377 | MATCH |
| 456 | `_september_workspace/results/_sub_transfer_wave2_register_2026_10_01.md` | `_september_workspace/results/_sub_transfer_wave2_register_2026_10_01.md` | `265b03ea493a` | 14286 | MATCH |
| 457 | `_september_workspace/results/_sub_transfer_wave3_register_2026_10_01.md` | `_september_workspace/results/_sub_transfer_wave3_register_2026_10_01.md` | `cd80b993f497` | 14419 | MATCH |
| 458 | `_september_workspace/results/_suspect17_release_move_register_2026_10_09.md` | `_september_workspace/results/_suspect17_release_move_register_2026_10_09.md` | `9a4d40bfcdc3` | 22351 | MATCH |
| 459 | `_september_workspace/results/_t1p2_enable_judgment_2026_10_10.md` | `_september_workspace/results/_t1p2_enable_judgment_2026_10_10.md` | `1e97d06b6ec9` | 20132 | MATCH |
| 460 | `_september_workspace/results/_t1p2_escalation_judgment_2026_10_10.md` | `_september_workspace/results/_t1p2_escalation_judgment_2026_10_10.md` | `5f43775a3224` | 22930 | MATCH |
| 461 | `_september_workspace/results/_t1p2_judgment_bytes_correction_2026_10_10.md` | `_september_workspace/results/_t1p2_judgment_bytes_correction_2026_10_10.md` | `d9d29bec3a0b` | 6377 | MATCH |
| 462 | `_september_workspace/results/_t1_7_2_correction_2026_10_08.md` | `_september_workspace/results/_t1_7_2_correction_2026_10_08.md` | `d90bf82338f6` | 16469 | MATCH |
| 463 | `_september_workspace/results/_t1_d7_reading_line_judgment_2026_10_10.md` | `_september_workspace/results/_t1_d7_reading_line_judgment_2026_10_10.md` | `60bd9ae98640` | 28559 | MATCH |
| 464 | `_september_workspace/results/_t1_exp2_exec_register_2026_10_09.md` | `_september_workspace/results/_t1_exp2_exec_register_2026_10_09.md` | `3a08dcfa8c7f` | 18597 | MATCH |
| 465 | `_september_workspace/results/_t1_exp2_verdict_2026_10_10.md` | `_september_workspace/results/_t1_exp2_verdict_2026_10_10.md` | `15c1c4b317a0` | 48298 | MATCH |
| 466 | `_september_workspace/results/_t1_exp2_verdict_bytes_correction_2026_10_10.md` | `_september_workspace/results/_t1_exp2_verdict_bytes_correction_2026_10_10.md` | `e863ca5fb157` | 13480 | MATCH |
| 467 | `_september_workspace/results/_t1_gate_closure_and_recompute_verdict_2026_10_01.md` | `_september_workspace/results/_t1_gate_closure_and_recompute_verdict_2026_10_01.md` | `4bdd82c796b8` | 72934 | MATCH |
| 468 | `_september_workspace/results/_t1_gate_revision_draft_2026_10_09.md` | `_september_workspace/results/_t1_gate_revision_draft_2026_10_09.md` | `50e8b2440346` | 27452 | MATCH |
| 469 | `_september_workspace/results/_t1_gate_revision_formal_2026_10_09.md` | `_september_workspace/results/_t1_gate_revision_formal_2026_10_09.md` | `0e0cb002c5de` | 35658 | MATCH |
| 470 | `_september_workspace/results/_t1_o1_design_axis_exemption_judgment_2026_10_09.md` | `_september_workspace/results/_t1_o1_design_axis_exemption_judgment_2026_10_09.md` | `a27c7f411de5` | 17073 | MATCH |
| 471 | `_september_workspace/results/_t1_p2_aggregation_caliber_judgment_2026_10_09.md` | `_september_workspace/results/_t1_p2_aggregation_caliber_judgment_2026_10_09.md` | `02f44f5bf2dd` | 14397 | MATCH |
| 472 | `_september_workspace/results/_t1_pairing_caliber_ruling_2026_10_09.md` | `_september_workspace/results/_t1_pairing_caliber_ruling_2026_10_09.md` | `2ded8091114a` | 21346 | MATCH |
| 473 | `_september_workspace/results/_t1_r2_d1_field_caliber_correction_2026_10_09.md` | `_september_workspace/results/_t1_r2_d1_field_caliber_correction_2026_10_09.md` | `99cafda125f1` | 25396 | MATCH |
| 474 | `_september_workspace/results/_t1_temp_axis_retirement_consolidation_2026_10_10.md` | `_september_workspace/results/_t1_temp_axis_retirement_consolidation_2026_10_10.md` | `40cb2e81425a` | 20308 | MATCH |
| 475 | `_september_workspace/results/_t1_temp_axis_retirement_judgment_2026_10_10.md` | `_september_workspace/results/_t1_temp_axis_retirement_judgment_2026_10_10.md` | `19afc7e191a7` | 27384 | MATCH |
| 476 | `_september_workspace/results/_theory_boundary_clone_sync_register_2026_10_09.md` | `_september_workspace/results/_theory_boundary_clone_sync_register_2026_10_09.md` | `1f9fd007649c` | 17528 | MATCH |
| 477 | `_september_workspace/results/_theory_input_request_supplement_2026_09_29.md` | `_september_workspace/results/_theory_input_request_supplement_2026_09_29.md` | `c966e7b605af` | 48190 | MATCH |
| 478 | `_september_workspace/results/_three_pending_items_drafts_2026_10_11.md` | `_september_workspace/results/_three_pending_items_drafts_2026_10_11.md` | `8995859e5a76` | 51748 | MATCH |
| 479 | `_september_workspace/results/_three_pending_items_effectivity_2026_10_11.md` | `_september_workspace/results/_three_pending_items_effectivity_2026_10_11.md` | `df1f5f75c7a0` | 16744 | MATCH |
| 480 | `_september_workspace/results/_three_state_standard_repeal_register_2026_10_10.md` | `_september_workspace/results/_three_state_standard_repeal_register_2026_10_10.md` | `8503708c73bf` | 18364 | MATCH |
| 481 | `_september_workspace/results/_thv3_15_parallel_seed_double_note_2026_10_11.md` | `_september_workspace/results/_thv3_15_parallel_seed_double_note_2026_10_11.md` | `3cd92287059e` | 15569 | MATCH |
| 482 | `_september_workspace/results/_th_id_miscitation_correction_2026_10_09.md` | `_september_workspace/results/_th_id_miscitation_correction_2026_10_09.md` | `b61321ba3b6e` | 10468 | MATCH |
| 483 | `_september_workspace/results/_tidy_round2_archive_transfer_register_2026_09_30.md` | `_september_workspace/results/_tidy_round2_archive_transfer_register_2026_09_30.md` | `1c1365f23c92` | 27641 | MATCH |
| 484 | `_september_workspace/results/_tmp_disposal_register_2026_10_10.md` | `_september_workspace/results/_tmp_disposal_register_2026_10_10.md` | `e0f6b744e826` | 20812 | MATCH |
| 485 | `_september_workspace/results/_trigger_denominator_caliber_judgment_2026_10_11.md` | `_september_workspace/results/_trigger_denominator_caliber_judgment_2026_10_11.md` | `16bf9332deef` | 43448 | MATCH |
| 486 | `_september_workspace/results/_trj_w1_downstream_erratum_2026_10_10.md` | `_september_workspace/results/_trj_w1_downstream_erratum_2026_10_10.md` | `e52d0016fbc6` | 24888 | MATCH |
| 487 | `_september_workspace/results/_trj_w1_verification_2026_10_10.md` | `_september_workspace/results/_trj_w1_verification_2026_10_10.md` | `cc6de8e981f6` | 23014 | MATCH |
| 488 | `_september_workspace/results/_typeb_m_caliber_2026_10_10.md` | `_september_workspace/results/_typeb_m_caliber_2026_10_10.md` | `4d067a884c6c` | 32830 | MATCH |
| 489 | `_september_workspace/results/_typeb_m_definition_judgment_2026_10_10.md` | `_september_workspace/results/_typeb_m_definition_judgment_2026_10_10.md` | `97ac7fcc4803` | 41432 | MATCH |
| 490 | `_september_workspace/results/_typeb_m_registration_2026_10_10.md` | `_september_workspace/results/_typeb_m_registration_2026_10_10.md` | `3b68d3890473` | 27778 | MATCH |
| 491 | `_september_workspace/results/_u04_1_exemption_precondition_verification_2026_10_09.md` | `_september_workspace/results/_u04_1_exemption_precondition_verification_2026_10_09.md` | `c072ffe6110e` | 21377 | MATCH |
| 492 | `_september_workspace/results/_u11_execution_register_2026_10_09.md` | `_september_workspace/results/_u11_execution_register_2026_10_09.md` | `8bc087a16f5a` | 24549 | MATCH |
| 493 | `_september_workspace/results/_u2u3_effectivity_register_2026_10_10.md` | `_september_workspace/results/_u2u3_effectivity_register_2026_10_10.md` | `b00b87cec825` | 27192 | MATCH |
| 494 | `_september_workspace/results/_u3_carrier_qid_verification_2026_10_11.md` | `_september_workspace/results/_u3_carrier_qid_verification_2026_10_11.md` | `6509ae68f778` | 21572 | MATCH |
| 495 | `_september_workspace/results/_u5b_citation_surface_revision_2026_10_10.md` | `_september_workspace/results/_u5b_citation_surface_revision_2026_10_10.md` | `5cc29c53a422` | 50079 | MATCH |
| 496 | `_september_workspace/results/_u5b_p_counting_resolution_2026_10_10.md` | `_september_workspace/results/_u5b_p_counting_resolution_2026_10_10.md` | `e12e9d9a32c4` | 20086 | MATCH |
| 497 | `_september_workspace/results/_u5_fingerprint_relocation_erratum_2026_10_10.md` | `_september_workspace/results/_u5_fingerprint_relocation_erratum_2026_10_10.md` | `200c7e4c57cb` | 24999 | MATCH |
| 498 | `_september_workspace/results/_u6_negative_delta_compatibility_2026_10_11.md` | `_september_workspace/results/_u6_negative_delta_compatibility_2026_10_11.md` | `1846e917119f` | 20969 | MATCH |
| 499 | `_september_workspace/results/_unclosed_items_inventory_2026_10_08.md` | `_september_workspace/results/_unclosed_items_inventory_2026_10_08.md` | `b0e7c74e951e` | 30219 | MATCH |
| 500 | `_september_workspace/results/_upload_execution_receipt_kimi_2026_09_26.md` | `_september_workspace/results/_upload_execution_receipt_kimi_2026_09_26.md` | `b4ac31f917f3` | 4191 | MATCH |
| 501 | `_september_workspace/results/_upload_execution_receipt_kimi_2026_09_30.md` | `_september_workspace/results/_upload_execution_receipt_kimi_2026_09_30.md` | `20e1f592ca61` | 4159 | MATCH |
| 502 | `_september_workspace/results/_upload_execution_receipt_kimi_2026_10_01.md` | `_september_workspace/results/_upload_execution_receipt_kimi_2026_10_01.md` | `a9a9a1d19661` | 4581 | MATCH |
| 503 | `_september_workspace/results/_upload_guard_mirror_pair_2026_10_08.md` | `_september_workspace/results/_upload_guard_mirror_pair_2026_10_08.md` | `d923371cdbce` | 23534 | MATCH |
| 504 | `_september_workspace/results/_upload_ledger_kimi_2026_09_30.json` | `_september_workspace/results/_upload_ledger_kimi_2026_09_30.json` | `b17cb8aae62d` | 218279 | MATCH |
| 505 | `_september_workspace/results/_upload_ledger_kimi_2026_10_01.json` | `_september_workspace/results/_upload_ledger_kimi_2026_10_01.json` | `79a0fb18683b` | 43275 | MATCH |
| 506 | `_september_workspace/results/_uv04_field_completeness_fill_2026_10_01.md` | `_september_workspace/results/_uv04_field_completeness_fill_2026_10_01.md` | `eb9b8d185f44` | 28735 | MATCH |
| 507 | `_september_workspace/results/_u_cf_category_caliber_2026_10_10.md` | `_september_workspace/results/_u_cf_category_caliber_2026_10_10.md` | `73f181d76169` | 18976 | MATCH |
| 508 | `_september_workspace/results/_u_cf_reclassification_2026_10_10.md` | `_september_workspace/results/_u_cf_reclassification_2026_10_10.md` | `02f910e8795b` | 25698 | MATCH |
| 509 | `_september_workspace/results/_u_closure_execution_register_2026_10_09.md` | `_september_workspace/results/_u_closure_execution_register_2026_10_09.md` | `cbf0c9503284` | 12781 | MATCH |
| 510 | `_september_workspace/results/_u_r_numbering_attribution_2026_10_11.md` | `_september_workspace/results/_u_r_numbering_attribution_2026_10_11.md` | `53672c23d7f9` | 5331 | MATCH |
| 511 | `_september_workspace/results/_u_v04_01_criterion_scope_determination_2026_10_01.md` | `_september_workspace/results/_u_v04_01_criterion_scope_determination_2026_10_01.md` | `e82609024b59` | 27079 | MATCH |
| 512 | `_september_workspace/results/_v3n_cpath_live_rerun_verdict_2026_10_01.md` | `_september_workspace/results/_v3n_cpath_live_rerun_verdict_2026_10_01.md` | `a91efbfec3d0` | 16409 | MATCH |
| 513 | `_september_workspace/results/_v3r1_threshold_final_path_judgment_2026_10_10.md` | `_september_workspace/results/_v3r1_threshold_final_path_judgment_2026_10_10.md` | `93f187f1ab75` | 39653 | MATCH |
| 514 | `_september_workspace/results/_v3r1_threshold_path4_draft_2026_10_10.md` | `_september_workspace/results/_v3r1_threshold_path4_draft_2026_10_10.md` | `a51f5de630ed` | 39077 | MATCH |
| 515 | `_september_workspace/results/_v3r1_threshold_restatement_design_2026_10_10.md` | `_september_workspace/results/_v3r1_threshold_restatement_design_2026_10_10.md` | `fb85a8013f9d` | 33847 | MATCH |
| 516 | `_september_workspace/results/_v3_02_ethard_closure_verdict_2026_10_09.md` | `_september_workspace/results/_v3_02_ethard_closure_verdict_2026_10_09.md` | `aa0f96bb618f` | 27819 | MATCH |
| 517 | `_september_workspace/results/_v3_02_ethard_execution_register_2026_10_09.md` | `_september_workspace/results/_v3_02_ethard_execution_register_2026_10_09.md` | `23457f5ce432` | 22007 | MATCH |
| 518 | `_september_workspace/results/_v3_02_override_register_2026_10_09.md` | `_september_workspace/results/_v3_02_override_register_2026_10_09.md` | `c5441e186c3f` | 36245 | MATCH |
| 519 | `_september_workspace/results/_v3_05_h_caliber_judgment_2026_10_09.md` | `_september_workspace/results/_v3_05_h_caliber_judgment_2026_10_09.md` | `1c2b5f40e15d` | 22050 | MATCH |
| 520 | `_september_workspace/results/_v3_recheck_05_executor_2026_09_28.py` | `_september_workspace/results/_v3_recheck_05_executor_2026_09_28.py` | `d6c8bc163e11` | 38639 | MATCH |
| 521 | `_september_workspace/results/_v3_recheck_10_executor_2026_09_27.py` | `_september_workspace/results/_v3_recheck_10_executor_2026_09_27.py` | `80947906e592` | 33647 | MATCH |
| 522 | `_september_workspace/results/_v3_recheck_12_executor_2026_09_27.py` | `_september_workspace/results/_v3_recheck_12_executor_2026_09_27.py` | `4850b1cbb010` | 49430 | MATCH |
| 523 | `_september_workspace/results/_v3_recheck_12_jsv_phase_data_2026_09_27.json` | `_september_workspace/results/_v3_recheck_12_jsv_phase_data_2026_09_27.json` | `642582d4fbd1` | 17718 | MATCH |
| 524 | `_september_workspace/results/_v3_recheck_19_executor_2026_09_27.py` | `_september_workspace/results/_v3_recheck_19_executor_2026_09_27.py` | `b133a631b1a8` | 19215 | MATCH |
| 525 | `_september_workspace/results/_v3_recheck_26b_verdict_2026_10_01.md` | `_september_workspace/results/_v3_recheck_26b_verdict_2026_10_01.md` | `8bbecb15b28b` | 26309 | MATCH |
| 526 | `_september_workspace/results/_v3_recheck_27_executor_2026_09_27.py` | `_september_workspace/results/_v3_recheck_27_executor_2026_09_27.py` | `190cbe01d061` | 34084 | MATCH |
| 527 | `_september_workspace/results/_v3_recheck_28_executor_2026_09_27.py` | `_september_workspace/results/_v3_recheck_28_executor_2026_09_27.py` | `4e8c0dd8f54f` | 17735 | MATCH |
| 528 | `_september_workspace/results/_v3_recheck_prereg_v1p2_2026_09_29.md` | `_september_workspace/results/_v3_recheck_prereg_v1p2_2026_09_29.md` | `a667a5f69b7a` | 25854 | MATCH |
| 529 | `_september_workspace/results/_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md` | `_september_workspace/results/_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md` | `c64146c4ccac` | 23152 | MATCH |
| 530 | `_september_workspace/results/_v3_v4_achievements_inventory_3dir_addendum_v2p1_2026_09_26.md` | `_september_workspace/results/_v3_v4_achievements_inventory_3dir_addendum_v2p1_2026_09_26.md` | `4c731a625868` | 17130 | MATCH |
| 531 | `_september_workspace/results/_v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md` | `_september_workspace/results/_v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md` | `24c64cc23907` | 37212 | MATCH |
| 532 | `_september_workspace/results/_v4s3_shadowing_priority_assessment_2026_10_01.md` | `_september_workspace/results/_v4s3_shadowing_priority_assessment_2026_10_01.md` | `2aaac67603ce` | 20111 | MATCH |
| 533 | `_september_workspace/results/_v4_85_77_attribution_verifier_r1_2026_09_29.md` | `_september_workspace/results/_v4_85_77_attribution_verifier_r1_2026_09_29.md` | `cd8ebaa86e44` | 17727 | MATCH |
| 534 | `_september_workspace/results/_v4_closeout_bucket_register_2026_10_01.md` | `_september_workspace/results/_v4_closeout_bucket_register_2026_10_01.md` | `99355c24a03b` | 41943 | MATCH |
| 535 | `_september_workspace/results/_v4_concl_t_verify_2026_09_28.md` | `_september_workspace/results/_v4_concl_t_verify_2026_09_28.md` | `927adba66e9b` | 13237 | MATCH |
| 536 | `_september_workspace/results/_v4_daily_cleanup_2026_09_28.md` | `_september_workspace/results/_v4_daily_cleanup_2026_09_28.md` | `f56e6fbf04ef` | 25491 | MATCH |
| 537 | `_september_workspace/results/_v4_final_verify.py` | `_september_workspace/results/_v4_final_verify.py` | `1dc482062d9b` | 4794 | MATCH |
| 538 | `_september_workspace/results/_v4_gamma_r1_exec_2026_09_28.md` | `_september_workspace/results/_v4_gamma_r1_exec_2026_09_28.md` | `0d946e65ba3c` | 21496 | MATCH |
| 539 | `_september_workspace/results/_v4_gamma_r1_prereg_2026_09_28.md` | `_september_workspace/results/_v4_gamma_r1_prereg_2026_09_28.md` | `c9da8678cf2b` | 33489 | MATCH |
| 540 | `_september_workspace/results/_v4_gamma_r1_prereg_v2_stop_2026_09_28.md` | `_september_workspace/results/_v4_gamma_r1_prereg_v2_stop_2026_09_28.md` | `9349e2fdb537` | 17999 | MATCH |
| 541 | `_september_workspace/results/_v4_gamma_r1_sources_20260928_S1.md` | `_september_workspace/results/_v4_gamma_r1_sources_20260928_S1.md` | `3d6e997aa692` | 2944 | MATCH |
| 542 | `_september_workspace/results/_v4_gamma_r1_sources_20260928_S2.md` | `_september_workspace/results/_v4_gamma_r1_sources_20260928_S2.md` | `dcec110ca2e0` | 2647 | MATCH |
| 543 | `_september_workspace/results/_v4_gamma_r1_sources_20260928_S3.md` | `_september_workspace/results/_v4_gamma_r1_sources_20260928_S3.md` | `6b9761d710ca` | 2554 | MATCH |
| 544 | `_september_workspace/results/_v4_gamma_r1_sources_20260928_S4.md` | `_september_workspace/results/_v4_gamma_r1_sources_20260928_S4.md` | `16af6baf8463` | 3050 | MATCH |
| 545 | `_september_workspace/results/_v4_gamma_r1_sources_20260928_S5_faceD.md` | `_september_workspace/results/_v4_gamma_r1_sources_20260928_S5_faceD.md` | `4f77d49756db` | 2264 | MATCH |
| 546 | `_september_workspace/results/_v4_item04_closeout_prereg_2026_09_28.md` | `_september_workspace/results/_v4_item04_closeout_prereg_2026_09_28.md` | `176e2b1c95ae` | 26719 | MATCH |
| 547 | `_september_workspace/results/_v4_maindir_cleanup_manifest_2026_09_24.md` | `_september_workspace/results/_v4_maindir_cleanup_manifest_2026_09_24.md` | `32cc61d394f2` | 19104 | MATCH |
| 548 | `_september_workspace/results/_v4_maindir_cleanup_manifest_v2_2026_09_26.md` | `_september_workspace/results/_v4_maindir_cleanup_manifest_v2_2026_09_26.md` | `f586a5a21584` | 27909 | MATCH |
| 549 | `_september_workspace/results/_v4_maindir_cleanup_moves_ledger_2026_09_24.md` | `_september_workspace/results/_v4_maindir_cleanup_moves_ledger_2026_09_24.md` | `4025e871726b` | 18829 | MATCH |
| 550 | `_september_workspace/results/_v4_maindir_cleanup_moves_ledger_v2_2026_09_24.md` | `_september_workspace/results/_v4_maindir_cleanup_moves_ledger_v2_2026_09_24.md` | `64c4ef850025` | 47909 | MATCH |
| 551 | `_september_workspace/results/_v4_maindir_cleanup_moves_ledger_v3_2026_09_24.md` | `_september_workspace/results/_v4_maindir_cleanup_moves_ledger_v3_2026_09_24.md` | `8f5136e176b8` | 31689 | MATCH |
| 552 | `_september_workspace/results/_v4_maindir_cleanup_moves_ledger_v4_2026_09_24.md` | `_september_workspace/results/_v4_maindir_cleanup_moves_ledger_v4_2026_09_24.md` | `9bd8932fa214` | 37047 | MATCH |
| 553 | `_september_workspace/results/_v4_maindir_cleanup_moves_ledger_v5_2026_09_24.md` | `_september_workspace/results/_v4_maindir_cleanup_moves_ledger_v5_2026_09_24.md` | `272e8c752406` | 46058 | MATCH |
| 554 | `_september_workspace/results/_v4_noise_cleanup_manifest_v2_2026_09_24.md` | `_september_workspace/results/_v4_noise_cleanup_manifest_v2_2026_09_24.md` | `90253e8342da` | 9683 | MATCH |
| 555 | `_september_workspace/results/_v4_noise_cleanup_manifest_v3_2026_09_25.md` | `_september_workspace/results/_v4_noise_cleanup_manifest_v3_2026_09_25.md` | `6f3f6fa3ab1d` | 24491 | MATCH |
| 556 | `_september_workspace/results/_v4_noise_cleanup_manifest_v4_2026_09_27.md` | `_september_workspace/results/_v4_noise_cleanup_manifest_v4_2026_09_27.md` | `82e90ff496ae` | 38001 | MATCH |
| 557 | `_september_workspace/results/_v4_pending_decisions_2026_09_28.md` | `_september_workspace/results/_v4_pending_decisions_2026_09_28.md` | `fe4671517827` | 24676 | MATCH |
| 558 | `_september_workspace/results/_v4_pi_cot_v2_collection_log.md` | `_september_workspace/results/_v4_pi_cot_v2_collection_log.md` | `167ad91f198e` | 1181 | MATCH |
| 559 | `_september_workspace/results/_v4_pi_cot_v2_prereg_activation_2026_09_23.md` | `_september_workspace/results/_v4_pi_cot_v2_prereg_activation_2026_09_23.md` | `00584e5a5c78` | 1016 | MATCH |
| 560 | `_september_workspace/results/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` | `_september_workspace/results/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` | `ba4d07bd7000` | 26637 | MATCH |
| 561 | `_september_workspace/results/_v4_pi_cot_v3_lock_and_rejudge_register_2026_09_28.md` | `_september_workspace/results/_v4_pi_cot_v3_lock_and_rejudge_register_2026_09_28.md` | `ae154971d1d2` | 12152 | MATCH |
| 562 | `_september_workspace/results/_v4_r4_cleanup_execution_2026_09_29.md` | `_september_workspace/results/_v4_r4_cleanup_execution_2026_09_29.md` | `3932b46b16ce` | 15357 | MATCH |
| 563 | `_september_workspace/results/_v4_r4_key_purge_manifest_2026_09_24.md` | `_september_workspace/results/_v4_r4_key_purge_manifest_2026_09_24.md` | `5bf4d9ad2877` | 13884 | MATCH |
| 564 | `_september_workspace/results/_v4_r4_purge_actions_2026_09_24.md` | `_september_workspace/results/_v4_r4_purge_actions_2026_09_24.md` | `8bbfe831e7c3` | 33117 | MATCH |
| 565 | `_september_workspace/results/_v4_rj5_rederive_2026_09_28.md` | `_september_workspace/results/_v4_rj5_rederive_2026_09_28.md` | `34ec49511ee3` | 22145 | MATCH |
| 566 | `_september_workspace/results/_v4_rj5_rederive_appendix_2026_09_28.md` | `_september_workspace/results/_v4_rj5_rederive_appendix_2026_09_28.md` | `985673661209` | 9226 | MATCH |
| 567 | `_september_workspace/results/_v4_slow_cleanup_manifest_2026_09_28.md` | `_september_workspace/results/_v4_slow_cleanup_manifest_2026_09_28.md` | `012501569aea` | 15693 | MATCH |
| 568 | `_september_workspace/results/_v4_supp_l14v3_batch10_r5_executor.py` | `_september_workspace/results/_v4_supp_l14v3_batch10_r5_executor.py` | `04383377b6a2` | 70471 | MATCH |
| 569 | `_september_workspace/results/_v4_supp_l14v3_batch2_r2_models_probe.log` | `_september_workspace/results/_v4_supp_l14v3_batch2_r2_models_probe.log` | `5664c63102a0` | 1260 | MATCH |
| 570 | `_september_workspace/results/_v4_supp_l14v3_batch2_r2_models_probe.py` | `_september_workspace/results/_v4_supp_l14v3_batch2_r2_models_probe.py` | `a31d54a4b765` | 5334 | MATCH |
| 571 | `_september_workspace/results/_v4_supp_l14v3_batch2_r2_result_probe_fail_v1.json` | `_september_workspace/results/_v4_supp_l14v3_batch2_r2_result_probe_fail_v1.json` | `21a89eb36a14` | 2635 | MATCH |
| 572 | `_september_workspace/results/_v4_supp_l14v3_batch2_r6_executor.py` | `_september_workspace/results/_v4_supp_l14v3_batch2_r6_executor.py` | `e38d068f309c` | 63788 | MATCH |
| 573 | `_september_workspace/results/_v4_supp_l14v3_batch3_r5_executor.py` | `_september_workspace/results/_v4_supp_l14v3_batch3_r5_executor.py` | `b7478168f87f` | 72156 | MATCH |
| 574 | `_september_workspace/results/_v4_supp_l14v3_batch4_r5_verify.py` | `_september_workspace/results/_v4_supp_l14v3_batch4_r5_verify.py` | `60d19aeee6f5` | 3050 | MATCH |
| 575 | `_september_workspace/results/_v4_supp_l14v3_batch4_r6_verify.py` | `_september_workspace/results/_v4_supp_l14v3_batch4_r6_verify.py` | `222972125231` | 4712 | MATCH |
| 576 | `_september_workspace/results/_v4_supp_l14v3_batch6_r2_report.md` | `_september_workspace/results/_v4_supp_l14v3_batch6_r2_report.md` | `080f9caf313c` | 6460 | MATCH |
| 577 | `_september_workspace/results/_v4_supp_l14v3_batch6_r3_report.md` | `_september_workspace/results/_v4_supp_l14v3_batch6_r3_report.md` | `6ef770d61308` | 6354 | MATCH |
| 578 | `_september_workspace/results/_v4_supp_l14v3_batch6_r4_report.md` | `_september_workspace/results/_v4_supp_l14v3_batch6_r4_report.md` | `0d0edc68cd35` | 7019 | MATCH |
| 579 | `_september_workspace/results/_v4_supp_l14v3_batch6_r5_report.md` | `_september_workspace/results/_v4_supp_l14v3_batch6_r5_report.md` | `d339d7286ad8` | 8596 | MATCH |
| 580 | `_september_workspace/results/_v4_supp_l14v3_batch7_r5_executor.py` | `_september_workspace/results/_v4_supp_l14v3_batch7_r5_executor.py` | `38710a448e9c` | 53155 | MATCH |
| 581 | `_september_workspace/results/_v4_supp_l14v3_batch9_r5_executor.py` | `_september_workspace/results/_v4_supp_l14v3_batch9_r5_executor.py` | `9b1a82a28dfb` | 65672 | MATCH |
| 582 | `_september_workspace/results/_v4_supp_t15r2_methodology_template.md` | `_september_workspace/results/_v4_supp_t15r2_methodology_template.md` | `6f9b865280a3` | 17411 | MATCH |
| 583 | `_september_workspace/results/_v4_track2_endpoints_probe.py` | `_september_workspace/results/_v4_track2_endpoints_probe.py` | `e7a6eb42c0af` | 20738 | MATCH |
| 584 | `_september_workspace/results/_v4_track2_models_probe.py` | `_september_workspace/results/_v4_track2_models_probe.py` | `da62abaa1e03` | 3191 | MATCH |
| 585 | `_september_workspace/results/_v4_track2_reprobe.py` | `_september_workspace/results/_v4_track2_reprobe.py` | `f92cc93f1304` | 2860 | MATCH |
| 586 | `_september_workspace/results/_v4_trae_remaining_audit_2026_09_28.md` | `_september_workspace/results/_v4_trae_remaining_audit_2026_09_28.md` | `1a8648083228` | 39681 | MATCH |
| 587 | `_september_workspace/results/_v5_agent_trio_post_reorg_note_2026_09_29.md` | `_september_workspace/results/_v5_agent_trio_post_reorg_note_2026_09_29.md` | `9c7182d93049` | 9795 | MATCH |
| 588 | `_september_workspace/results/_v5_alias_table_d01_d04_c01_c03_2026_09_29.md` | `_september_workspace/results/_v5_alias_table_d01_d04_c01_c03_2026_09_29.md` | `b3e39064d7c5` | 15315 | MATCH |
| 589 | `_september_workspace/results/_v5_anchor_drift_backfill_2026_09_28.md` | `_september_workspace/results/_v5_anchor_drift_backfill_2026_09_28.md` | `6f1edd1ccebb` | 14438 | MATCH |
| 590 | `_september_workspace/results/_v5_a_system_default_register_2026_09_28.md` | `_september_workspace/results/_v5_a_system_default_register_2026_09_28.md` | `8c22796a42f5` | 19892 | MATCH |
| 591 | `_september_workspace/results/_v5_b12_verify_pack_q1_q3_q4_2026_09_29.md` | `_september_workspace/results/_v5_b12_verify_pack_q1_q3_q4_2026_09_29.md` | `698262e6fe8b` | 33803 | MATCH |
| 592 | `_september_workspace/results/_v5_b14_08c_material_plan_2026_09_29.md` | `_september_workspace/results/_v5_b14_08c_material_plan_2026_09_29.md` | `b69d65cbb329` | 22104 | MATCH |
| 593 | `_september_workspace/results/_v5_b14_3_v1_4_prereg_2026_09_29.md` | `_september_workspace/results/_v5_b14_3_v1_4_prereg_2026_09_29.md` | `0f1665e7056f` | 20045 | MATCH |
| 594 | `_september_workspace/results/_v5_b14_4_v1_3_prereg_2026_09_29.md` | `_september_workspace/results/_v5_b14_4_v1_3_prereg_2026_09_29.md` | `ae474bf48c62` | 20043 | MATCH |
| 595 | `_september_workspace/results/_v5_b14_p41c_independent_judgment_2026_09_29.md` | `_september_workspace/results/_v5_b14_p41c_independent_judgment_2026_09_29.md` | `b752582bc692` | 22437 | MATCH |
| 596 | `_september_workspace/results/_v5_b15_offsite_readonly_authorization_2026_09_29.md` | `_september_workspace/results/_v5_b15_offsite_readonly_authorization_2026_09_29.md` | `96a069701b3d` | 18483 | MATCH |
| 597 | `_september_workspace/results/_v5_b15_offsite_readonly_authorization_activation_2026_09_29.md` | `_september_workspace/results/_v5_b15_offsite_readonly_authorization_activation_2026_09_29.md` | `99978eb15c10` | 35006 | MATCH |
| 598 | `_september_workspace/results/_v5_b17_fault_register_2026_09_29.md` | `_september_workspace/results/_v5_b17_fault_register_2026_09_29.md` | `48cb0ab5f317` | 18129 | MATCH |
| 599 | `_september_workspace/results/_v5_b17_recheck12_register_2026_09_29.md` | `_september_workspace/results/_v5_b17_recheck12_register_2026_09_29.md` | `73242a890be9` | 19981 | MATCH |
| 600 | `_september_workspace/results/_v5_b18_o8_semantic_verify_2026_09_29.md` | `_september_workspace/results/_v5_b18_o8_semantic_verify_2026_09_29.md` | `49d4adf8f197` | 26544 | MATCH |
| 601 | `_september_workspace/results/_v5_b18_o8_semantic_verify_r2_2026_09_29.md` | `_september_workspace/results/_v5_b18_o8_semantic_verify_r2_2026_09_29.md` | `dc1233d0ab4f` | 24145 | MATCH |
| 602 | `_september_workspace/results/_v5_b20_gamma_a_attribution_2026_09_29.md` | `_september_workspace/results/_v5_b20_gamma_a_attribution_2026_09_29.md` | `7bad6e52a0f3` | 30789 | MATCH |
| 603 | `_september_workspace/results/_v5_b20_gamma_a_rereview_2026_09_29.md` | `_september_workspace/results/_v5_b20_gamma_a_rereview_2026_09_29.md` | `b22dda133038` | 30680 | MATCH |
| 604 | `_september_workspace/results/_v5_b22_r05_path_backfill_2026_09_29.md` | `_september_workspace/results/_v5_b22_r05_path_backfill_2026_09_29.md` | `09b3105acb6f` | 12233 | MATCH |
| 605 | `_september_workspace/results/_v5_b22_r07_four_cond_prereg_2026_09_29.md` | `_september_workspace/results/_v5_b22_r07_four_cond_prereg_2026_09_29.md` | `ceea8f4534fb` | 23151 | MATCH |
| 606 | `_september_workspace/results/_v5_b35_result_attribution_2026_09_29.md` | `_september_workspace/results/_v5_b35_result_attribution_2026_09_29.md` | `ec358f6f76a3` | 35313 | MATCH |
| 607 | `_september_workspace/results/_v5_bom_u1_exec_2026_09_29.md` | `_september_workspace/results/_v5_bom_u1_exec_2026_09_29.md` | `5b0282960d52` | 22730 | MATCH |
| 608 | `_september_workspace/results/_v5_bom_u1_exec_2026_09_29.py` | `_september_workspace/results/_v5_bom_u1_exec_2026_09_29.py` | `c140a28e15ae` | 31134 | MATCH |
| 609 | `_september_workspace/results/_v5_clearance_mr10_pb_reembed_prereg_2026_09_29.md` | `_september_workspace/results/_v5_clearance_mr10_pb_reembed_prereg_2026_09_29.md` | `c514b321fe10` | 18271 | MATCH |
| 610 | `_september_workspace/results/_v5_clearance_mr11_doc_calibration_2026_09_29.md` | `_september_workspace/results/_v5_clearance_mr11_doc_calibration_2026_09_29.md` | `c4bce5a5e8be` | 14974 | MATCH |
| 611 | `_september_workspace/results/_v5_clearance_mr19_sha1_note_2026_09_29.md` | `_september_workspace/results/_v5_clearance_mr19_sha1_note_2026_09_29.md` | `c74ffc6278a8` | 22859 | MATCH |
| 612 | `_september_workspace/results/_v5_clearance_mr3_s40_fix_note_2026_09_29.md` | `_september_workspace/results/_v5_clearance_mr3_s40_fix_note_2026_09_29.md` | `b1244981065b` | 15522 | MATCH |
| 613 | `_september_workspace/results/_v5_clearance_o15_ready_pack_2026_09_29.md` | `_september_workspace/results/_v5_clearance_o15_ready_pack_2026_09_29.md` | `618e5990b3e5` | 48968 | MATCH |
| 614 | `_september_workspace/results/_v5_clearance_pending_backlog_register_2026_09_29.md` | `_september_workspace/results/_v5_clearance_pending_backlog_register_2026_09_29.md` | `1132072288de` | 32369 | MATCH |
| 615 | `_september_workspace/results/_v5_clearance_readme_c5_register_2026_09_29.md` | `_september_workspace/results/_v5_clearance_readme_c5_register_2026_09_29.md` | `ababdaa392ca` | 8730 | MATCH |
| 616 | `_september_workspace/results/_v5_clearance_round11_register_2026_09_29.md` | `_september_workspace/results/_v5_clearance_round11_register_2026_09_29.md` | `2e5e6f8b328e` | 59923 | MATCH |
| 617 | `_september_workspace/results/_v5_clearance_round12_14_register_2026_09_29.md` | `_september_workspace/results/_v5_clearance_round12_14_register_2026_09_29.md` | `13d741979ebb` | 75131 | MATCH |
| 618 | `_september_workspace/results/_v5_clearance_round15_18_register_2026_09_29.md` | `_september_workspace/results/_v5_clearance_round15_18_register_2026_09_29.md` | `3a3c9c734bf9` | 99989 | MATCH |
| 619 | `_september_workspace/results/_v5_clearance_round1_b19_register_2026_09_29.md` | `_september_workspace/results/_v5_clearance_round1_b19_register_2026_09_29.md` | `b69ec2ddc9be` | 28556 | MATCH |
| 620 | `_september_workspace/results/_v5_clearance_round2_3_register_2026_09_29.md` | `_september_workspace/results/_v5_clearance_round2_3_register_2026_09_29.md` | `32ca90e63a56` | 37340 | MATCH |
| 621 | `_september_workspace/results/_v5_clearance_round4_5_register_2026_09_29.md` | `_september_workspace/results/_v5_clearance_round4_5_register_2026_09_29.md` | `9d381fab5f46` | 52782 | MATCH |
| 622 | `_september_workspace/results/_v5_clearance_round6_register_2026_09_29.md` | `_september_workspace/results/_v5_clearance_round6_register_2026_09_29.md` | `68fe5b397df3` | 38248 | MATCH |
| 623 | `_september_workspace/results/_v5_clearance_round7_8_register_2026_09_29.md` | `_september_workspace/results/_v5_clearance_round7_8_register_2026_09_29.md` | `60cdeef91d4a` | 63311 | MATCH |
| 624 | `_september_workspace/results/_v5_clearance_round9_10_register_2026_09_29.md` | `_september_workspace/results/_v5_clearance_round9_10_register_2026_09_29.md` | `428e0857ebb7` | 68512 | MATCH |
| 625 | `_september_workspace/results/_v5_closing_register_r2_2026_09_28.md` | `_september_workspace/results/_v5_closing_register_r2_2026_09_28.md` | `1094edb6e8c0` | 25446 | MATCH |
| 626 | `_september_workspace/results/_v5_confirm_b10_decisions_register_2026_09_29.md` | `_september_workspace/results/_v5_confirm_b10_decisions_register_2026_09_29.md` | `67ea81a2e6d9` | 13282 | MATCH |
| 627 | `_september_workspace/results/_v5_confirm_b12_decisions_register_2026_09_29.md` | `_september_workspace/results/_v5_confirm_b12_decisions_register_2026_09_29.md` | `db0d6e56a497` | 15898 | MATCH |
| 628 | `_september_workspace/results/_v5_confirm_b13_b22_anchor_verify_2026_09_29.md` | `_september_workspace/results/_v5_confirm_b13_b22_anchor_verify_2026_09_29.md` | `a0c2d1d5fe6b` | 16393 | MATCH |
| 629 | `_september_workspace/results/_v5_confirm_b13_b22_exec_queue_2026_09_29.md` | `_september_workspace/results/_v5_confirm_b13_b22_exec_queue_2026_09_29.md` | `56549b04a925` | 39531 | MATCH |
| 630 | `_september_workspace/results/_v5_confirm_b13_decisions_register_2026_09_29.md` | `_september_workspace/results/_v5_confirm_b13_decisions_register_2026_09_29.md` | `c7ca4fbecc8b` | 33086 | MATCH |
| 631 | `_september_workspace/results/_v5_confirm_b16_b17_decisions_register_2026_09_29.md` | `_september_workspace/results/_v5_confirm_b16_b17_decisions_register_2026_09_29.md` | `8e36a3e4c6ff` | 29624 | MATCH |
| 632 | `_september_workspace/results/_v5_confirm_b18_b19_decisions_register_2026_09_29.md` | `_september_workspace/results/_v5_confirm_b18_b19_decisions_register_2026_09_29.md` | `ae160194878e` | 21072 | MATCH |
| 633 | `_september_workspace/results/_v5_confirm_b1_decisions_register_2026_09_29.md` | `_september_workspace/results/_v5_confirm_b1_decisions_register_2026_09_29.md` | `62ca213bb56c` | 28469 | MATCH |
| 634 | `_september_workspace/results/_v5_confirm_b20_b22_decisions_register_2026_09_29.md` | `_september_workspace/results/_v5_confirm_b20_b22_decisions_register_2026_09_29.md` | `fccaac464565` | 24883 | MATCH |
| 635 | `_september_workspace/results/_v5_confirm_b2_decisions_register_2026_09_29.md` | `_september_workspace/results/_v5_confirm_b2_decisions_register_2026_09_29.md` | `63ded68919df` | 28383 | MATCH |
| 636 | `_september_workspace/results/_v5_confirm_b3_decisions_register_2026_09_29.md` | `_september_workspace/results/_v5_confirm_b3_decisions_register_2026_09_29.md` | `4dbb11c219fc` | 34015 | MATCH |
| 637 | `_september_workspace/results/_v5_confirm_b4_decisions_register_2026_09_29.md` | `_september_workspace/results/_v5_confirm_b4_decisions_register_2026_09_29.md` | `4d02f9df594e` | 43498 | MATCH |
| 638 | `_september_workspace/results/_v5_confirm_b8_decisions_register_2026_09_29.md` | `_september_workspace/results/_v5_confirm_b8_decisions_register_2026_09_29.md` | `6862659ff900` | 15106 | MATCH |
| 639 | `_september_workspace/results/_v5_ea_review_chain_rules_2026_09_29.md` | `_september_workspace/results/_v5_ea_review_chain_rules_2026_09_29.md` | `8e235f520fb9` | 11511 | MATCH |
| 640 | `_september_workspace/results/_v5_fake_verdict_forensics_2026_09_28.md` | `_september_workspace/results/_v5_fake_verdict_forensics_2026_09_28.md` | `1b135d8b1e08` | 35870 | MATCH |
| 641 | `_september_workspace/results/_v5_familyline_r01_r02_independent_judgment_2026_09_29.md` | `_september_workspace/results/_v5_familyline_r01_r02_independent_judgment_2026_09_29.md` | `e16e50329c88` | 25392 | MATCH |
| 642 | `_september_workspace/results/_v5_gamma_end1_rb_clause_addendum_2026_09_29.md` | `_september_workspace/results/_v5_gamma_end1_rb_clause_addendum_2026_09_29.md` | `bf38e5f0161e` | 10397 | MATCH |
| 643 | `_september_workspace/results/_v5_gamma_r1_v2_withdraw_2026_09_29.md` | `_september_workspace/results/_v5_gamma_r1_v2_withdraw_2026_09_29.md` | `f4ef22a5f97c` | 24611 | MATCH |
| 644 | `_september_workspace/results/_v5_gt33_attrib_fill_prereg_2026_09_29.md` | `_september_workspace/results/_v5_gt33_attrib_fill_prereg_2026_09_29.md` | `48742d6cbd03` | 36984 | MATCH |
| 645 | `_september_workspace/results/_v5_gt33_d5_crossref_note_2026_09_29.md` | `_september_workspace/results/_v5_gt33_d5_crossref_note_2026_09_29.md` | `dd50ff801ef7` | 10989 | MATCH |
| 646 | `_september_workspace/results/_v5_gt8f_m1_g1_fail_clause_addendum_2026_09_29.md` | `_september_workspace/results/_v5_gt8f_m1_g1_fail_clause_addendum_2026_09_29.md` | `31e5bd7b4003` | 14481 | MATCH |
| 647 | `_september_workspace/results/_v5_gt8_lowarm_result_2026_09_29_cb132cd5.json` | `_september_workspace/results/_v5_gt8_lowarm_result_2026_09_29_cb132cd5.json` | `c68076c88140` | 26253 | MATCH |
| 648 | `_september_workspace/results/_v5_gt8_lowarm_verdict_2026_09_29.md` | `_september_workspace/results/_v5_gt8_lowarm_verdict_2026_09_29.md` | `9140b6e5970b` | 32653 | MATCH |
| 649 | `_september_workspace/results/_v5_gt8_lowarm_verdict_r2_2026_09_29.md` | `_september_workspace/results/_v5_gt8_lowarm_verdict_r2_2026_09_29.md` | `aff727434aa4` | 40282 | MATCH |
| 650 | `_september_workspace/results/_v5_gt_exec_2026_09_29.json` | `_september_workspace/results/_v5_gt_exec_2026_09_29.json` | `01e95e49b035` | 142217 | MATCH |
| 651 | `_september_workspace/results/_v5_h231_r07_independent_judgment_2026_09_29.md` | `_september_workspace/results/_v5_h231_r07_independent_judgment_2026_09_29.md` | `70025895600a` | 37949 | MATCH |
| 652 | `_september_workspace/results/_v5_item05_prereg_2026_09_28.md` | `_september_workspace/results/_v5_item05_prereg_2026_09_28.md` | `567f0f177699` | 19115 | MATCH |
| 653 | `_september_workspace/results/_v5_item21_asset_recovery_2026_09_28.md` | `_september_workspace/results/_v5_item21_asset_recovery_2026_09_28.md` | `6c80ff43bdd7` | 8793 | MATCH |
| 654 | `_september_workspace/results/_v5_item21_patched_recompute_2026_09_28.md` | `_september_workspace/results/_v5_item21_patched_recompute_2026_09_28.md` | `2c1d85913ccc` | 15895 | MATCH |
| 655 | `_september_workspace/results/_v5_item21_rerun_conditions_prereg_2026_09_28.md` | `_september_workspace/results/_v5_item21_rerun_conditions_prereg_2026_09_28.md` | `4185bdad6df5` | 31429 | MATCH |
| 656 | `_september_workspace/results/_v5_item21_strategyqa_realias_recompute_2026_09_29.md` | `_september_workspace/results/_v5_item21_strategyqa_realias_recompute_2026_09_29.md` | `4e941d0a9c48` | 14639 | MATCH |
| 657 | `_september_workspace/results/_v5_item21_strategyqa_realias_verdict_2026_09_29.md` | `_september_workspace/results/_v5_item21_strategyqa_realias_verdict_2026_09_29.md` | `26eaa156108f` | 32354 | MATCH |
| 658 | `_september_workspace/results/_v5_item21_verdict_2026_09_28.md` | `_september_workspace/results/_v5_item21_verdict_2026_09_28.md` | `de274bd38955` | 28155 | MATCH |
| 659 | `_september_workspace/results/_v5_item35_v3_collinear_exec_2026_09_29.md` | `_september_workspace/results/_v5_item35_v3_collinear_exec_2026_09_29.md` | `912afffed6b9` | 46000 | MATCH |
| 660 | `_september_workspace/results/_v5_item35_v3_collinear_verdict_2026_10_01.md` | `_september_workspace/results/_v5_item35_v3_collinear_verdict_2026_10_01.md` | `363cce3dae59` | 38266 | MATCH |
| 661 | `_september_workspace/results/_v5_item35_v3_collinear_verdict_prep_2026_10_01.md` | `_september_workspace/results/_v5_item35_v3_collinear_verdict_prep_2026_10_01.md` | `a31026f2384d` | 33755 | MATCH |
| 662 | `_september_workspace/results/_v5_item36_prereg_2026_09_28.md` | `_september_workspace/results/_v5_item36_prereg_2026_09_28.md` | `7f42d5ee131c` | 18141 | MATCH |
| 663 | `_september_workspace/results/_v5_loadcorpus_fix_2026_09_29.md` | `_september_workspace/results/_v5_loadcorpus_fix_2026_09_29.md` | `e47614ccf5ff` | 17355 | MATCH |
| 664 | `_september_workspace/results/_v5_loadcorpus_switch_2026_09_29.md` | `_september_workspace/results/_v5_loadcorpus_switch_2026_09_29.md` | `d37e97644bf8` | 16414 | MATCH |
| 665 | `_september_workspace/results/_v5_paper_remedy_line_orchestration_2026_09_29.md` | `_september_workspace/results/_v5_paper_remedy_line_orchestration_2026_09_29.md` | `d911674e68cf` | 48292 | MATCH |
| 666 | `_september_workspace/results/_v5_paper_remedy_r1_pledge_2026_09_29.md` | `_september_workspace/results/_v5_paper_remedy_r1_pledge_2026_09_29.md` | `816cb91d4611` | 47778 | MATCH |
| 667 | `_september_workspace/results/_v5_paper_remedy_r2_r4_sourcetrace_2026_09_29.md` | `_september_workspace/results/_v5_paper_remedy_r2_r4_sourcetrace_2026_09_29.md` | `29da2ca8932f` | 34647 | MATCH |
| 668 | `_september_workspace/results/_v5_paper_remedy_r6b_x27_sourcetrace_2026_09_29.md` | `_september_workspace/results/_v5_paper_remedy_r6b_x27_sourcetrace_2026_09_29.md` | `b75cc49b360f` | 16125 | MATCH |
| 669 | `_september_workspace/results/_v5_pd_v04_root_naming_candidates_2026_09_29.md` | `_september_workspace/results/_v5_pd_v04_root_naming_candidates_2026_09_29.md` | `46599dde51a8` | 14312 | MATCH |
| 670 | `_september_workspace/results/_v5_pi_decision_trace_gap_audit_2026_09_29.md` | `_september_workspace/results/_v5_pi_decision_trace_gap_audit_2026_09_29.md` | `38b043c4be6a` | 33101 | MATCH |
| 671 | `_september_workspace/results/_v5_pjpm_pc_degen_precheck_executor_2026_09_29.py` | `_september_workspace/results/_v5_pjpm_pc_degen_precheck_executor_2026_09_29.py` | `f58b0d1c1a93` | 76822 | MATCH |
| 672 | `_september_workspace/results/_v5_pjpm_pc_reverify_bang2_2026_09_29.md` | `_september_workspace/results/_v5_pjpm_pc_reverify_bang2_2026_09_29.md` | `6833cae407e8` | 39517 | MATCH |
| 673 | `_september_workspace/results/_v5_pjpm_pc_verdict_bang3_2026_09_29.md` | `_september_workspace/results/_v5_pjpm_pc_verdict_bang3_2026_09_29.md` | `1814f9590f0f` | 41566 | MATCH |
| 674 | `_september_workspace/results/_v5_pl2_fourband_prereg_2026_09_29.md` | `_september_workspace/results/_v5_pl2_fourband_prereg_2026_09_29.md` | `d5fdb89582fd` | 29253 | MATCH |
| 675 | `_september_workspace/results/_v5_prereg_chain_activation_register_2026_09_28.md` | `_september_workspace/results/_v5_prereg_chain_activation_register_2026_09_28.md` | `3cc05f8cbd1a` | 27047 | MATCH |
| 676 | `_september_workspace/results/_v5_prereg_chain_status_annotation_2026_09_28.md` | `_september_workspace/results/_v5_prereg_chain_status_annotation_2026_09_28.md` | `cb4104938cc8` | 23857 | MATCH |
| 677 | `_september_workspace/results/_v5_proxy_temp_T0.3.json` | `_september_workspace/results/_v5_proxy_temp_T0.3.json` | `04d915714b96` | 143345 | MATCH |
| 678 | `_september_workspace/results/_v5_proxy_temp_T1.5.json` | `_september_workspace/results/_v5_proxy_temp_T1.5.json` | `2b36d8632a80` | 143261 | MATCH |
| 679 | `_september_workspace/results/_v5_proxy_vocab_V50.json` | `_september_workspace/results/_v5_proxy_vocab_V50.json` | `2deedc43fc40` | 78182 | MATCH |
| 680 | `_september_workspace/results/_v5_proxy_vocab_V500.json` | `_september_workspace/results/_v5_proxy_vocab_V500.json` | `4ddd6afbf16b` | 78191 | MATCH |
| 681 | `_september_workspace/results/_v5_r4_residual_merged_catalogue_2026_09_29.md` | `_september_workspace/results/_v5_r4_residual_merged_catalogue_2026_09_29.md` | `0c4bbd26ea55` | 102410 | MATCH |
| 682 | `_september_workspace/results/_v5_recyclebin_sha12_completion_2026_09_29.md` | `_september_workspace/results/_v5_recyclebin_sha12_completion_2026_09_29.md` | `5f3223a4b349` | 59551 | MATCH |
| 683 | `_september_workspace/results/_v5_rj5_verdict_2026_09_29.md` | `_september_workspace/results/_v5_rj5_verdict_2026_09_29.md` | `9c1ccbd5cf5a` | 40057 | MATCH |
| 684 | `_september_workspace/results/_v5_sha12_collision_statement_2026_09_29.md` | `_september_workspace/results/_v5_sha12_collision_statement_2026_09_29.md` | `f0f44cf6dc65` | 28155 | MATCH |
| 685 | `_september_workspace/results/_v5_sub_artifact_ledger_history_r1_2026_09_29.md` | `_september_workspace/results/_v5_sub_artifact_ledger_history_r1_2026_09_29.md` | `535b3c2ad102` | 48539 | MATCH |
| 686 | `_september_workspace/results/_v5_sub_artifact_ledger_history_r2_2026_09_29.md` | `_september_workspace/results/_v5_sub_artifact_ledger_history_r2_2026_09_29.md` | `5ff7784db145` | 150957 | MATCH |
| 687 | `_september_workspace/results/_v5_sub_artifact_ledger_history_r3_2026_09_29.md` | `_september_workspace/results/_v5_sub_artifact_ledger_history_r3_2026_09_29.md` | `e04a46b02d13` | 128760 | MATCH |
| 688 | `_september_workspace/results/_v5_sub_artifact_ledger_history_r4_2026_09_29.md` | `_september_workspace/results/_v5_sub_artifact_ledger_history_r4_2026_09_29.md` | `b6b8be476a73` | 603599 | MATCH |
| 689 | `_september_workspace/results/_v5_t1_decisions_register_2026_09_29.md` | `_september_workspace/results/_v5_t1_decisions_register_2026_09_29.md` | `7dd7dd3fb721` | 31330 | MATCH |
| 690 | `_september_workspace/results/_v5_theory_input_acquisition_request_2026_09_29.md` | `_september_workspace/results/_v5_theory_input_acquisition_request_2026_09_29.md` | `83afc4802fe7` | 10691 | MATCH |
| 691 | `_september_workspace/results/_v5_track2_qwen_retry_2026_09_29.md` | `_september_workspace/results/_v5_track2_qwen_retry_2026_09_29.md` | `c890771728f3` | 11957 | MATCH |
| 692 | `_september_workspace/results/_v5_track2_qwen_retry_executor_20260929.py` | `_september_workspace/results/_v5_track2_qwen_retry_executor_20260929.py` | `d34b46e24a7c` | 11586 | MATCH |
| 693 | `_september_workspace/results/_v5_v3deg_prereg_activation_register_2026_09_29.md` | `_september_workspace/results/_v5_v3deg_prereg_activation_register_2026_09_29.md` | `e587da3b4cf8` | 24370 | MATCH |
| 694 | `_september_workspace/results/_v5_v3r2_errata_note_2026_09_29.md` | `_september_workspace/results/_v5_v3r2_errata_note_2026_09_29.md` | `d687ad25a68c` | 29089 | MATCH |
| 695 | `_september_workspace/results/_v5_v3_deg_c5_b_halt_report_2026_09_29.md` | `_september_workspace/results/_v5_v3_deg_c5_b_halt_report_2026_09_29.md` | `f2b68ee099b5` | 14862 | MATCH |
| 696 | `_september_workspace/results/_v5_v3_deg_p1_reopen_exec_2026_09_29.md` | `_september_workspace/results/_v5_v3_deg_p1_reopen_exec_2026_09_29.md` | `38231ef6f053` | 33622 | MATCH |
| 697 | `_september_workspace/results/_v5_v3_deg_p1_reopen_verdict_2026_09_29.md` | `_september_workspace/results/_v5_v3_deg_p1_reopen_verdict_2026_09_29.md` | `63d898ab1b71` | 42645 | MATCH |
| 698 | `_september_workspace/results/_v5_v3_deg_p1_reopen_verdict_r2_2026_09_29.md` | `_september_workspace/results/_v5_v3_deg_p1_reopen_verdict_r2_2026_09_29.md` | `8adaf4e5d868` | 44054 | MATCH |
| 699 | `_september_workspace/results/_v5_v3_deg_p1_reopen_verify_2026_09_29.md` | `_september_workspace/results/_v5_v3_deg_p1_reopen_verify_2026_09_29.md` | `4afeb8cd41de` | 27898 | MATCH |
| 700 | `_september_workspace/results/_v5_v3_t1_effect_judgment_2026_09_29.md` | `_september_workspace/results/_v5_v3_t1_effect_judgment_2026_09_29.md` | `1995bd4460ae` | 40697 | MATCH |
| 701 | `_september_workspace/results/_v5_v4_export_filter_spec_2026_09_29.md` | `_september_workspace/results/_v5_v4_export_filter_spec_2026_09_29.md` | `14dd6ccdbed6` | 22884 | MATCH |
| 702 | `_september_workspace/results/_v5_v4_proposal_23item_merged_catalogue_2026_09_29.md` | `_september_workspace/results/_v5_v4_proposal_23item_merged_catalogue_2026_09_29.md` | `79bcff089f21` | 14620 | MATCH |
| 703 | `_september_workspace/results/_v5_v4_proposal_23item_merged_catalogue_sourceverify_2026_09_29.md` | `_september_workspace/results/_v5_v4_proposal_23item_merged_catalogue_sourceverify_2026_09_29.md` | `ac0d6f19f06c` | 22185 | MATCH |
| 704 | `_september_workspace/results/_verdict_pack_d_prep_2026_10_01.md` | `_september_workspace/results/_verdict_pack_d_prep_2026_10_01.md` | `119f98cd8d2d` | 49471 | MATCH |
| 705 | `_september_workspace/results/_vk_current_counting_face_2026_10_10.md` | `_september_workspace/results/_vk_current_counting_face_2026_10_10.md` | `4d4e41c3eff5` | 24795 | MATCH |
| 706 | `_september_workspace/results/_vk_face_category_erratum_2026_10_11.md` | `_september_workspace/results/_vk_face_category_erratum_2026_10_11.md` | `67bf70301889` | 17373 | MATCH |
| 707 | `_september_workspace/results/_vk_two_items_judgments_2026_10_09.md` | `_september_workspace/results/_vk_two_items_judgments_2026_10_09.md` | `82556d54726c` | 33399 | MATCH |
| 708 | `_september_workspace/results/_wordlist_house_effectivity_note_2026_10_10.md` | `_september_workspace/results/_wordlist_house_effectivity_note_2026_10_10.md` | `4e89a5bb4b68` | 14606 | MATCH |
| 709 | `_september_workspace/results/_wordlist_house_establishment_draft_2026_10_10.md` | `_september_workspace/results/_wordlist_house_establishment_draft_2026_10_10.md` | `afa5eb53d216` | 38468 | MATCH |
| 710 | `_september_workspace/results/_wrapup_cleanup_inventory_register_2026_09_29.md` | `_september_workspace/results/_wrapup_cleanup_inventory_register_2026_09_29.md` | `6beeb397a4c1` | 22556 | MATCH |
| 711 | `_september_workspace/results/_zero_consumption_cells_field_correction_2026_10_10.md` | `_september_workspace/results/_zero_consumption_cells_field_correction_2026_10_10.md` | `36f9ac4ebbf6` | 12244 | MATCH |
| 712 | `_september_workspace/results/_zero_reading_judgment_2026_10_10.md` | `_september_workspace/results/_zero_reading_judgment_2026_10_10.md` | `a9947f5677df` | 27824 | MATCH |
| 713 | `_september_workspace/results/_archive_2026_09_20/_archive_manifest_2026_09_18.json` | `_september_workspace/results/_archive_2026_09_20/_archive_manifest_2026_09_18.json` | `a729875c0c67` | 4712 | MATCH |
| 714 | `_september_workspace/results/_archive_2026_09_20/_archive_manifest_2026_09_20.json` | `_september_workspace/results/_archive_2026_09_20/_archive_manifest_2026_09_20.json` | `4dd89950bf11` | 35682 | MATCH |
| 715 | `_september_workspace/results/_archive_2026_09_21/_archive_manifest_2026_09_21.json` | `_september_workspace/results/_archive_2026_09_21/_archive_manifest_2026_09_21.json` | `33fe31633da8` | 17353 | MATCH |
| 716 | `_september_workspace/results/_archive_2026_09_24/l14_small_batch.py` | `_september_workspace/results/_archive_2026_09_24/l14_small_batch.py` | `0659c947bec1` | 21784 | MATCH |
| 717 | `_september_workspace/results/_archive_2026_09_24/latency_test.py` | `_september_workspace/results/_archive_2026_09_24/latency_test.py` | `fd9fd98785e1` | 617 | MATCH |
| 718 | `_september_workspace/results/_archive_2026_09_24/_final_verify.py` | `_september_workspace/results/_archive_2026_09_24/_final_verify.py` | `31a5d44497f1` | 2307 | MATCH |
| 719 | `_september_workspace/results/_archive_2026_09_24/_inspect_captions.py` | `_september_workspace/results/_archive_2026_09_24/_inspect_captions.py` | `dfb02ade1474` | 591 | MATCH |
| 720 | `_september_workspace/results/_archive_2026_09_24/_l13_latency_test.py` | `_september_workspace/results/_archive_2026_09_24/_l13_latency_test.py` | `dae238354342` | 2954 | MATCH |
| 721 | `_september_workspace/results/_archive_2026_09_24/_v4_pi_decision_questionnaire_2026_09_21_v1.1.md.bak_2026_09_22_gB_post.md` | `_september_workspace/results/_archive_2026_09_24/_v4_pi_decision_questionnaire_2026_09_21_v1.1.md.bak_2026_09_22_gB_post.md` | `07ca9ee8e1bb` | 113508 | MATCH |
| 722 | `_september_workspace/results/_archive_2026_09_24/_verify_worker_c.py` | `_september_workspace/results/_archive_2026_09_24/_verify_worker_c.py` | `cc578c46b332` | 1155 | MATCH |
| 723 | `_september_workspace/results/_archive_2026_09_24/_worker_openrouter_rag_run.py` | `_september_workspace/results/_archive_2026_09_24/_worker_openrouter_rag_run.py` | `4458ccf3d64a` | 24113 | MATCH |

---

## 6. SAME_IDENTITY：目标已存在且逐位全等（12 件 · 未转移、未清走）

| 源路径 | 已存在于 sub 的目标 | SHA-12 |
|---|---|---|
| `_september_workspace/results/deposon_dpath_cross_modal_runner_2026_09_10.py` | `_september_workspace/results/deposon_dpath_cross_modal_runner_2026_09_10.py` | `fb20a6ba5ec6` |
| `_september_workspace/results/deposon_feshbach_rag_30cells_2026_09_10.py` | `_september_workspace/results/deposon_feshbach_rag_30cells_2026_09_10.py` | `a072e4184e83` |
| `_september_workspace/results/deposon_v1_implementation_calculator_2026_09_10.py` | `_september_workspace/results/deposon_v1_implementation_calculator_2026_09_10.py` | `121f104012f4` |
| `_september_workspace/results/deposon_volcengine_glm_latest_5cells_2026_09_10.py` | `_september_workspace/results/deposon_volcengine_glm_latest_5cells_2026_09_10.py` | `a3ca05aec6fb` |
| `_september_workspace/results/deposon_volcengine_worker_b_2026_09_10.py` | `_september_workspace/results/deposon_volcengine_worker_b_2026_09_10.py` | `401dfd3c27f3` |
| `_september_workspace/results/deposon_volcengine_worker_c_2026_09_10.py` | `_september_workspace/results/deposon_volcengine_worker_c_2026_09_10.py` | `b5eeef1e9bd7` |
| `_september_workspace/results/_tra_v0_2026_09_10.py` | `_september_workspace/results/_tra_v0_2026_09_10.py` | `d80a8f75a122` |
| `_september_workspace/results/_v3x_d0_5_experiment_invitation_2026_09_17.md` | `_september_workspace/results/_v3x_d0_5_experiment_invitation_2026_09_17.md` | `d8f2b99aa527` |
| `_september_workspace/results/_v3x_d0_5_proposal_coze_2026_09_17.md` | `_september_workspace/results/_v3x_d0_5_proposal_coze_2026_09_17.md` | `759c25b21ed4` |
| `_september_workspace/results/_v3x_d0_5_proposal_trae_2026_09_17.md` | `_september_workspace/results/_v3x_d0_5_proposal_trae_2026_09_17.md` | `b1c227d54a82` |
| `_september_workspace/results/_v3x_p_l_v3_external_spec_2026_09_17.md` | `_september_workspace/results/_v3x_p_l_v3_external_spec_2026_09_17.md` | `6a5b6eb635f0` |
| `_september_workspace/results/_v3x_p_l_v3_summary_mistral_large_2512_20260917_115049.md` | `_september_workspace/results/_v3x_p_l_v3_summary_mistral_large_2512_20260917_115049.md` | `183205baa9ac` |

**处置**：两区同哈希并存，**不重复计数、不覆盖、不清走**，原地保留双份并登记（防重复计数）。

---

## 7. 测量仪器自查（本棒发现并修复的三处缺陷 · 如实登记）

1. **引用字段未落盘致阻断表为空**：首轮分类结果的 `CodeRefs` 仅存于内存、未写入 CSV，重建阻断表时取到空值，导致 **17 件被活执行体读取的 `.tmp` 件被误列入清走集**。发现后重建并复验：`FUNC_REF_protected_present = 17 / 17`，清走集 0 泄漏。**若未捕获，将清走 6,277,328 B 的 `_t1_exp2_c_records.json` 等实证底本。**
2. **UTF-8 无 BOM 脚本被 GBK 解码致路径畸变**：辅助 `.ps1` 以 UTF-8 无 BOM 落盘，PowerShell 5.1 按系统代码页解码，`〔本地资料区〕` → `〔本机路径〕/绉佷汉璧勬枡/`（长度 29→31），致 `Substring` 偏移错位、目标路径畸变、**占用检测静默失效**（12 个已占用目标将被覆写）。于**执行前**捕获，重建为 UTF-8 **带 BOM** 并加入 `REPO.Length -ne 29 → throw` 硬断言。**捕获时 0 转移已执行，无数据受损。**

3. **PowerShell 变量大小写不敏感致 `SUB 被覆写 → 快照 sub 面指纹表作废**：快照生成器第 2 节用 $sub 作目录数组变量，与第 1 节的路径常量 $SUB **同名（PowerShell 变量大小写不敏感）**，`2 将其覆写为数组。致第 3 节第二轮 $root 取到数组，$root.Length ＝ 数组元素数（8）而非路径长（19），Substring(9) 产出畸变路径 eposon-repo\\...，且区小计误报 847（真值 1,187）。**已捕获**：修正变量名并加入四重硬断言（$root -isnot [string] → abort / FullName.StartsWith() → abort / $rel -match '^[A-Za-z]:' → abort / 区小计 ≠ 独立复算值 → abort），重新生成后 sub 面 1,187 件逐件路径与盘面一致。
> **纪律**：测量仪器自身即误差源 —— 假阳性/假阴性优先修仪器，不修文本。三处缺陷均在**落盘前或复验时**捕获，故终态两产出无一处失真。

---

## 8. 边界自证

| 边界 | 状态 |
|---|---|
| ⛔ 0 永久删除 | ✅ 全部经 `mavis-trash` 回收站 |
| ⛔ 0 断链 | ✅ 723/723 SHA-256 MATCH；0 件被活代码引用者被移动 |
| ⛔ 0 触禁触区 | ✅ `_non_upload_local_archive` 0 读 0 写 0 列目录；`Deposon_v1_2_0_交付包` 0 动作 |
| ⛔ 0 立成果清单 / 0 出收尾桶 | ✅ 本棒仅出登记与终态快照 |
| ⛔ 0 覆写既有件 | ✅ `96720fcfd76a` / `4a3b661a7d13` 指纹复验未变，原样保留 |
| ⛔ 0 逐项发卡问 PI | ✅ 夜间模式，产出直接追认 |
| ⛔ 0 填估值/推断值 | ✅ 全部实测 |
| ⛔ 0 网络 / 0 skill / 0 LLM / 0 读 `.env` | ✅ |
| ⛔ 0 宣告任何闭/开/段之毕 | ✅ 本件仅登记动作 |

---

## 9. 未执行提案（列而不做 · 待 PI 裁）

1. `Deposon_v1_2_0_交付包`（23 件）：本棒 ⛔ 0 动作，是否纳入整理面待裁。
2. 9 件 `._moved_20260924_1830.py` 冗余副本：铁律保护 `*.py` 未清走；若 PI 放行可清。
3. ``results/_archive_2026-10-12/pycache_sink/` 内 8 件 `.pyc`（529,402 B）：系上一轮归档件，保留归档完整性未动。
4. ``repo/.tmp` 余 441 件：其中 396 件 `.py` 受铁律保护，17 件 FUNC_REF 保留。
5. 600 件绝对路径钉住之 ``repo/results` 件：若欲彻底 1:1，须另立「执行体改相对路径」棒，本棒 ⛔ 不越界。

---

*evidence-auditor · 2026-10-12 · 已执行 · ⛔ 0 永久删除 0 断链 0 触禁触区 0 立清单*
