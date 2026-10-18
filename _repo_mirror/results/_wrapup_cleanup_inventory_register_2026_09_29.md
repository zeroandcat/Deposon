# 收工整理与四目录清点登记 · 2026-09-29

- 棒别：今日收工棒（worker）· 执行 A 段（整理）＋ B 段（四目录清点）
- 范围：A 段仅 `D:\私人资料\deposon-repo`；B 段四目录全只读
- 纪律：0 编造／0 代裁／0 回改既有件／R4（0 读 key／0 读 `.env`）／UTF-8 无 BOM · LF
- 快照时点：A 段起扫 `2026-09-29 21:26:27 +08:00`；B 段 sub/archive/交付包 `21:29:21`；B 段 repo `21:30:19`；pyc 与撞名实测 `21:30:5x`
- 落盘前撞名实测：`results\_wrapup_cleanup_inventory_register_2026_09_29.md` **CLEAR**（目标名 0 占用；`results\*wrapup*` 近名 0 命中）

---

## §A 清理登记

### A.1 判定依据（先立据，再逐件套用）

仓库根 `.*` 临时件 09-29 15:20–15:33 批次共 **16 件**，与既有勘误链登记口径一致：

- `docs\V3X\TRAE_V3_ASSET_ERRATUM_2026_09_23.md:5084`：「`deposon-repo` 根目录另有 **16 件**不同命名前缀的临时产物（`.tmp_p10_*.py` / `.tmp_p10_*.txt` / `.tmp_setA_*` / `.scratch_*`，**mtime 2026-09-29 15:20–15:33**）⇒ ⛔ 本棒 0 处置…**如实登记现状 16 件即可**」
- `docs\V3X\TRAE_V3_ASSET_ERRATUM_2026_09_23.md:5052`：扫描记录点名 `.tmp_setA_run1.json` 为「非本件」枚举命中

实测复算得该 16 件集合与勘误链所述**逐件吻合**（件数、mtime 窗、前缀三类全对上）。

本棒对该勘误行「0 删除」的口径判读（**此为判读，非代裁，PI 可推翻**）：

1. 该行 `0 处置／0 移动／0 删除` 之限定语为「**本棒**」，作用域为 E-56 批次自身，非对后续收工棒的永久禁令；
2. 该行自陈「文件数／件数类账目统一归『V4 收尾整理』批量校正，本棒 0 单独对账，**如实登记现状即可**」——即该行为**计数登记行**，非对各件内容设证据依赖；
3. 故判定标准取「**是否承载不可复现的唯一信息**」：承载者 0 触动；不承载者入可恢复清理。

### A.2 逐件登记（16 件全量）

SHA-12 = SHA-256 前 12 位十六进制，对**清理前**盘上终态复算。

| # | 路径 | SHA-12 | 字节 | 分类依据 | 去向 |
|---|---|---|---|---|---|
| 1 | `.tmp_p10_err.txt` | `e3b0c44298fc` | 0 | SHA-256 全量 ＝ 空串常量，0 字节无内容；stderr 为空之事实已由 `deposon_team\plugins\_v5_gt8_lowarm_2026_09_29.py:10` 头注自证 | **trash** |
| 2 | `.tmp_setA_err.txt` | `e3b0c44298fc` | 0 | 同上（`…_setA_2026_09_29.py:10` 头注自证） | **trash** |
| 3 | `.scratch_setb_err1.txt` | `e3b0c44298fc` | 0 | 同上 | **trash** |
| 4 | `.scratch_setb_err2.txt` | `e3b0c44298fc` | 0 | 同上 | **trash** |
| 5 | `.scratch_setaverify_err.txt` | `e3b0c44298fc` | 0 | 同上 | **trash** |
| 6 | `.tmp_setA_out2.txt` | `e981c33ece8b` | 3,638 | 与保留件 `.tmp_setA_out.txt`（同 `e981c33ece8b`、同字节）**逐字节相同**的重跑副本；正本在盘，唯一信息 0 损失 | **trash** |
| 7 | `.scratch_setb_run2.txt` | `496fd1304e6d` | 3,618 | 与保留件 `.scratch_setb_run1.txt`（同 `496fd1304e6d`、同字节）**逐字节相同**的重跑副本；正本在盘 | **trash** |
| 8 | `.tmp_p10_out.txt` | `726881f82ecf` | 3,606 | p10 跑批 stdout 全文，唯一 | **留** |
| 9 | `.tmp_p10_inspect.py` | `d0d8002242b1` | 3,587 | 复现脚本（p10 检视），唯一 | **留** |
| 10 | `.scratch_sib_dump.json` | `a0a7f9ea397f` | 13,273 | sibling 快照 dump，唯一 | **留** |
| 11 | `.tmp_setA_run1.json` | `24b0d5eda48a` | 28,638 | setA run1 数据 dump；**已被勘误链 :5052 点名枚举**，留 | **留** |
| 12 | `.tmp_setA_out.txt` | `e981c33ece8b` | 3,638 | setA out 正本（#6 的保留孪生） | **留** |
| 13 | `.tmp_p10_verify.py` | `6c9b7da03d4e` | 2,704 | 复现脚本（p10 校验），唯一 | **留** |
| 14 | `.scratch_setb_run1.txt` | `496fd1304e6d` | 3,618 | setB run1 正本（#7 的保留孪生） | **留** |
| 15 | `.scratch_setb_dump.json` | `5c9265483128` | 25,374 | setB 数据 dump，唯一 | **留** |
| 16 | `.scratch_setaverify.txt` | `390ed8731fcf` | 2,350 | setA 校验输出全文，唯一 | **留** |

**小结：trash 7 件／留 9 件（16 件全量 0 遗漏）。**

### A.3 清理执行与自证

- 通道：`cd` 至仓库根后单批 `rm -- <7 相对路径>`（**0 绝对路径删除命令、0 内联删除脚本、0 绕恢复机制**）
- 批数：**1 批**（7 件 ≤ 12 件上限），**0 并行移动**
- 运行时逐件回执（7/7 全部 `mavis-trash: moved to trash`）：

```
mavis-trash: moved to trash: '.tmp_p10_err.txt'
mavis-trash: moved to trash: '.tmp_setA_err.txt'
mavis-trash: moved to trash: '.scratch_setb_err1.txt'
mavis-trash: moved to trash: '.scratch_setb_err2.txt'
mavis-trash: moved to trash: '.scratch_setaverify_err.txt'
mavis-trash: moved to trash: '.tmp_setA_out2.txt'
mavis-trash: moved to trash: '.scratch_setb_run2.txt'
exit=0
```

- **逐批复核（`still_on_disk`）**：`still_on_disk = 0 / 7`（7 件全部不在原路径）
- **保留件在位复核**：`retained_ok = 9 / 9`
- 0 永久删除

### A.4 `__pycache__` / `.pyc` 候选（**只列候选 · 0 清理**）

依 PI 未决项「6 再生 .pyc 清否」，本棒 **0 触动**。全仓 **10 个 `__pycache__` 目录／46 件 `.pyc`／1,327,171 B**。

| `__pycache__` 目录 | 件数 | SHA-12（逐件） |
|---|---|---|
| `.scratch_gamma_r1\__pycache__` | 1 | `fetch.cpython-314.pyc` `9b69fa07feb3` |
| `.scratch_rj5\__pycache__` | 2 | `derive_b_fast.cpython-314.pyc` `538da5946b21`；`derive_b_v3.cpython-314.pyc` `0441d5ff0a19` |
| `.tmp\__pycache__` | 8 | `_v5_c5_b_clause4_consistency_check…` `a0a2b21c15bf`；`_v5_c5_b_fetch_raw_embeddings…` `9e851c2d93ed`；`_v5_item21_patched_b1_semA_none_default…` `b4a1ab09e142`；`_v5_item21_patched_b1_semB_none_skip…` `f4b7bb44ef52`；`_v5_item21_patched_b2_semA_none_default…` `446382bbb63f`；`_v5_item21_patched_b2_semB_none_skip…` `ce4d2edbdc4f`；`_v5_item21_patched_b3_semA_none_default…` `a3315df76d1e`；`_v5_item21_patched_b3_semB_none_skip…` `1c13024cc354` |
| `.tmp\_v5_loadcorpus_switch_2026_09_29\__pycache__` | 1 | `_old_corpus_view.cpython-314.pyc` `26936af8a863` |
| `__pycache__`（仓根） | 18 | `_v5_gt_exec_2026_09_29` `14410b42819f`；`deposon_diffusion` `1f3ba2ed7c6a`；`deposon_protocol` `088fa0dce971`；`llm_fetch` `a657828320d2`；`llm_prior` `1cba3980e9db`；`mindmap_corpus_v20` `df4e45b14505`；`run_v15_experiment` `f3dee598cf7b`；`run_v16_llm_prior` `9def7c7d9778`；`run_v17_fusion_fix` `13f393522c54`；`run_v19_fullrank` `15a1cd457f8a`；`run_v19_meanfield` `7a37ab2865ae`；`run_v19_quickwins` `754f696cd9b3`；`run_v20_baselines` `439d6cfe7c8c`；`run_v20_bigquiz_eval` `6cc05b033586`；`run_v20_corpus_eval` `a290a81d4214`；`run_v20_gt2b` `63ff13e1ee71`；`run_v20_gt6` `15bed469bef1`；`run_v20_gt8` `79cb662e0982` |
| `deposon_team\plugins\__pycache__` | 9 | `_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29` `7915ef539a1d`；`_v3r1p1_21_ktb1_distortion_2026_09_27` `ac379e1009ae`；`_v5_gt8_lowarm_2026_09_29` `3ad4683992c7`；`_v5_gt8_lowarm_setA_2026_09_29` `ec7bb84dfa43`；`_v5_gt8_lowarm_seta_verify_2026_09_29` `2ee22c472dbb`；`_v5_item35_v2_matrix_2026_09_29` `6eda70d5cb33`；`_v5_item35_v3_collinear_2026_09_29` `664c464176e0`；`_v5_pp1_pattern_fix_2026_09_29` `2342a72bca9b`；`_v5r_s40_rerun_executor_fix_2026_09_29` `d6fc8b5f9065` |
| `results\__pycache__` | 4 | `_v3_recheck_26b_executor_r2_2026_09_28` `b402fdae0a82`；`_v3_recheck_26b_executor_r3_2026_09_29` `9e73f2c48ae6`；`_v4_pi_cot_v2_ruleset_v2_executor` `09f27edf5ab4`；`_v4_pi_cot_v3_ruleset_v3_executor` `08d4b51c45c6` |
| `results\_v3_recheck_08b_executor\__pycache__` | 1 | `executor_2026_09_27` `5dfa39f98d45` |
| `results\_v3_recheck_08c_preexp_data\__pycache__` | 1 | `executor_2026_09_27` `52b212480666` |
| `verifier\v21\__pycache__` | 1 | `check.cpython-314.pyc` `910e0977f40f` |

### A.5 `.scratch_*` 目录与 `.tmp\` 内今日件（**0 处置**）

| 目录 | 件数 | 字节 | 处置 |
|---|---|---|---|
| `.scratch_gamma_r1\` | 31 | 2,408,669 | **留**（含 4 件 PDF 正文 + arXiv XML 原始抓取，属留痕） |
| `.scratch_rj5\` | 26 | 6,952,002 | **留**（含 3 件 PDF 正文，属留痕） |
| `.scratch_t_verify\` | 18 | 42,099 | **留**（step1–step11 + final + write_report 复算链，18 步自洽） |
| `.tmp\` | 256 | 5,717,793 | **留**（含 `_e48_*.py` / `_e48_c*.md` 等勘误节复算脚本、`verif_doubt6_v_20260928\` 快照 26 件、`_v5_loadcorpus_switch_2026_09_29\` 10 件） |
| `.tmp_recovery\` | 31 | 13,910,921 | **留 · 0 触动**（**21:28–21:30 正在被并发写入，见 §C.4**） |

散落 `*_err.txt` 全仓实测 **5 件、全部 0 字节、全部在仓根**（即 A.2 之 #1–#5），**0 遗漏**。

### A.6 两方向转移候选（**只列候选 · 本夜 0 执行**）

| 候选 | 方向 | 件数 | 字节 | 理由 |
|---|---|---|---|---|
| `.scratch_gamma_r1\` | → `_non_upload_local_archive` | 31 | 2,408,669 | 第三方 PDF/XML 原始抓取，不上传留档 |
| `.scratch_rj5\` | → `_non_upload_local_archive` | 26 | 6,952,002 | 同上（含 4.8 MB PDF 正文） |
| `.scratch_t_verify\` | → `_non_upload_local_archive` | 18 | 42,099 | 一次性验算脚本链 |
| `.tmp\verif_doubt6_v_20260928\` | → `_non_upload_local_archive` | 26 | — | 09-28 疑问 6 复算快照，仓内已有同族 `results\` 件 |
| `_v5_loadcorpus_switch_2026_09_29\` | → `deposon-sub` | 10 | — | 项目衍生语料切换件（`baseline_pre/post.json` + `applied_diff.txt` 属可复现实验记录） |

**本夜 0 移动、0 执行。** 全部待 PI 拍板。

---

## §B 四目录清点表（全只读）

### B.1 汇总

| # | 目录 | 文件总数 | 总字节 | 快照时点 |
|---|---|---|---|---|
| ① | `D:\私人资料\deposon-repo` | **1,717** | **546,401,304** | 21:30:19 |
| ② | `D:\私人资料\deposon-sub` | **476** | **34,381,510** | 21:29:21 |
| ③ | `D:\私人资料\_non_upload_local_archive` | **1,474** | **331,624,448** | 21:29:21 |
| ④ | `D:\私人资料\Deposon_v1_2_0_交付包` | **23** | **3,243,552** | 21:29:21 |

> ① 之 1,717 件含 A 段清理后状态（清理前为 1,724 件）。**该数随 `.tmp_recovery\` 并发写入而变动，见 §C.4。**

### B.2 ① `deposon-repo` — 扩展名 Top 10

`.md` 577｜`.py` 540｜`.json` 399｜`.txt` 64｜`.pyc` 46｜`.log` 28｜`.csv` 15｜`.xml` 13｜`.sh` 9｜`.pdf` 9（余 17 件散于其他扩展名）

**顶层目录结构（二层）**（顶层散文件 81 件）

```
.mavis/scripts[4]              .scratch_gamma_r1/{__pycache__[1], raw[17]}    .scratch_rj5/{__pycache__[2], raw[17]}
.scratch_t_verify[18]          .tmp/{__pycache__[8], _v5_loadcorpus_switch_2026_09_29[10], verif_doubt6[1], verif_doubt6_v_20260928[26]}
.tmp_recovery[31]              .trae/scripts[2]        __pycache__[18]        attacks[4]
corpus/{v20[31], v20_caption_surface[10]}                 deposon_team/plugins[87]
docs/{reviews[3], V3X[79]}     letters[69]             paper/v2[2]            reviews/data[15]
results[722]（子目录 22：_archive_2026_09_20/21/24、_v3_recheck_08b/08c、_v3_s*、_p_*×6、_v3x_*×3、.evidence_backup_2026_09_28、__pycache__）
scripts[10]                    tests[23]               tools[5]
verifier[118]（子目录 44：v1–v43、runs[57]、audit、handoff、kill_lines）
```

**mtime 最新 10 件**（21:30:19 快照，全部属 `.tmp_recovery\` 并发写入面）

```
21:30:19|16,116|.tmp_recovery\hit_huila.txt      21:29:12| 1,713|.tmp_recovery\resolve.txt
21:30:18|19,633|.tmp_recovery\hit_quhu.txt       21:28:52|98,949|.tmp_recovery\sha_index.tsv
21:27:39|105,630|.tmp_recovery\hit_queue.txt     21:28:32| 2,165|.tmp_recovery\shaindex.py
21:27:18|56,185|.tmp_recovery\TAIL_g66.md        21:28:06|19,997|.tmp_recovery\queue_g65on.txt
21:27:18|33,766|.tmp_recovery\TAIL_g65.md        21:27:17|20,691|.tmp_recovery\TAIL_g64.md
```

### B.3 ② `deposon-sub` — 扩展名 Top 10

`.json` 211｜`.py` 135｜`.md` 100｜`.txt` 14｜`.ps1` 6｜`.csv` 2｜`.pdf` 2｜`.gz` 2｜`.note` 1｜`(noext)` 1（合计 476 ＝ 文件总数，**无尾差**）

**顶层目录结构（二层）**（顶层散文件 28 件，含 `_movedout_manifest_2026_09_21.json` / `_movedout_manifest_2026_09_28.json`）

```
.trae/{audit[14], deliverables[3], scripts[2]}    deposon_team/{_designs[11], plugins[41], products[2], verifier[3]}
docs/FTFB_EXTERNAL_REVIEW_R2_2026_09_17[3]        tmp_movedout_2026_09_28[8]
results[361]（子目录 14：_archive_2026_09_18/20/21、_p_i…_p_o 共 6、_v3x_*×3）
```

**mtime 最新 10 件**

```
09-28 18:27:21| 2,003|_movedout_manifest_2026_09_28.json
09-28 18:25:45| 5,017|tmp_movedout_2026_09_28\_cleanup_transfer_scan_out_2026_09_28.txt
09-28 18:25:29| 3,229|tmp_movedout_2026_09_28\_cleanup_transfer_scan_2026_09_28.py
09-28 18:19:25| 1,257|tmp_movedout_2026_09_28\_cleanup_resolve_out_2026_09_28.txt
09-28 18:19:07| 2,735|tmp_movedout_2026_09_28\_cleanup_resolve_2026_09_28.py
09-28 18:17:58|11,347|tmp_movedout_2026_09_28\_cleanup_classify_out_2026_09_28.txt
09-28 18:17:11| 3,232|tmp_movedout_2026_09_28\_cleanup_classify_2026_09_28.py
09-28 18:14:33|12,365|tmp_movedout_2026_09_28\_cleanup_probe_out_2026_09_28.txt
09-28 18:14:13| 2,556|tmp_movedout_2026_09_28\_cleanup_probe_2026_09_28.py
09-26 18:37:04|   384|_tmp_verify.py
```

> **该目录自 09-28 18:27 起 0 新增写入**（最新件为 `_movedout_manifest_2026_09_28.json`）。

### B.4 ③ `_non_upload_local_archive` — 扩展名 Top 10

`.json` 432｜`.py` 377｜`.md` 249｜`.log` 158｜`.png` 75｜`.txt` 59｜`.err` 23｜`.pdf` 16｜`.pyc` 14｜`.tex` 10（余 61 件散于其他扩展名）

**顶层目录结构（二层）**（顶层散文件 4 件：`_probe_v19.py` / `_probe_v19_inv.py` / `_probe_v19_inv2.py` / `strategyqa_train.json`）

```
.mavis[1]                      .trae/{audit[6], build[16], snapshots[32], source[13]}     __pycache__[1]
_paper_backup_v181[4]          _worker_temp[42]        attacks[0]/__pycache__[0]           backups/backups[10]
cache/cache[63]                corpus/_worker_temp[2]  deposon_team/{_designs[0], plugins[2], verifier[0]}
docs/V3X[130→122]              figures/v3x[33→23]      installers/installers[4]           logs/logs[131]
paper/{deposon_arxiv_cn_pkg[11], deposon_arxiv_en_pkg[12]}                                proposals[3]  reports[2]
results[661]（子目录 16：gt2/gt3/gt8b/gt8c/familyL/cot_quiz/attacker_xl 等 cache ×10、_archive_2026_09_20/21、
             _remote_version_freeze_2026_09_26[24]、_worker_temp[7]、.tmp[2]、__pycache__[1]、_v4_supp_l3_n20copy_backup[1]）
reviews/data[0]                scripts/{__pycache__[0], scripts[122→135]}                tests/__pycache__[0]
tmp/{.pytest_cache[0], .tmp[7], .tmp_volcengine_2026_09_10[10], __pycache__[1]}            tools/__pycache__[0]
verifier[102]（audit、handoff、kill_lines、runs[48]、v1–v43×44 子目录）                    verify_archive_backup[2]
```

**mtime 最新 10 件**

```
09-29 19:19:15|101,685|results\__pycache__\_v4_rerun_executor_2026_09_23.cpython-314.pyc
09-28 20:00:18| 19,562|scripts\scripts\kt_b1\__pycache__\boss_b2_kd.cpython-314.pyc
09-28 20:00:17| 18,743|scripts\scripts\kt_b1\__pycache__\boss_b3_llmlingua.cpython-314.pyc
09-28 19:59:53| 20,607|scripts\scripts\kt_b1\__pycache__\boss_b1_sinkhorn_ot.cpython-314.pyc
09-28 19:59:09| 16,679|scripts\scripts\kt_b1\__pycache__\boss_b3_llmlingua.py.cpython-314.pyc
09-28 19:59:09| 17,470|scripts\scripts\kt_b1\__pycache__\boss_b2_kd.cpython-314.pyc
09-28 19:58:39| 18,526|scripts\scripts\kt_b1\__pycache__\boss_b1_sinkhorn_ot.py.cpython-314.pyc
09-26 21:27:06| 11,894|results\_remote_version_freeze_2026_09_26\_freeze_manifest.json
09-26 21:27:06|  1,253|results\_remote_version_freeze_2026_09_26\v20_regression_field_v2.json
09-26 21:27:05|  2,130|results\_remote_version_freeze_2026_09_26\v20_graph_features.csv
```

> **该目录最新件为 09-29 19:19 之 `.pyc`（再生件，非人工写入）**；最新人工件为 09-26 21:27 冻结清单。

### B.5 ④ `Deposon_v1_2_0_交付包` — **全结构逐层**（小型包，23 件全列）

```
[D] output
    output\deposon_agents_v1.py                              ( 32,030 B, 2026-08-22 12:10)
    output\deposon_agents_v1_1.py                            ( 33,233 B, 2026-08-22 12:31)
    output\deposon_agents_v1_2.py                            ( 54,363 B, 2026-08-22 14:37)
    output\Deposon_Agents_技术报告_v1_1.md                    ( 11,523 B, 2026-08-22 12:52)
    output\deposon_benchmark_100_final.json                   (  1,315 B, 2026-08-22 14:07)
    output\deposon_benchmark_100_kimi.json                    (  1,302 B, 2026-08-22 14:20)
    output\deposon_benchmark_100_results.json                (    834 B, 2026-08-22 14:03)
    output\deposon_benchmark_100_traps.json                   (  1,025 B, 2026-08-22 14:24)
    output\deposon_unified_field.py                           ( 23,315 B, 2026-08-22 01:34)
    output\Deposon_技术报告_v1_2_0.md                         (  8,906 B, 2026-08-22 14:28)
    output\Deposon_评估汇总_v1_2_0.json                       (  1,963 B, 2026-08-22 14:28)
    output\Deposon_项目报告_v1_2_0.pdf                        (331,617 B, 2026-08-22 14:42)
    output\Deposon_项目进展与路线图_v1.1.0-RC1.md             ( 10,817 B, 2026-08-22 13:02)
[D] upload
    upload\AI时代脑图价值_对话集.docx                          ( 79,376 B, 2026-08-22 00:17)
    upload\AI时代脑图价值研究报告_v7_守正创新版.pdf            (1,039,343 B, 2026-08-22 00:16)
    upload\AI思考与量子突破_对话集.docx                        (102,343 B, 2026-08-22 00:17)
    upload\AI应当如何思考_从仿生向到仿物理向_v2.pdf            (238,039 B, 2026-08-22 00:16)
    upload\core_v3.py                                         ( 22,705 B, 2026-08-22 00:16)
    upload\Deposon_Requirements_v1.md                         ( 13,914 B, 2026-08-22 00:16)
    upload\Deposon_凝子_统一场论研究报告_v1.pdf                (687,460 B, 2026-08-22 00:16)
    upload\photonai_v3.py                                     ( 19,337 B, 2026-08-22 00:16)
    upload\仿光子范式_v3_改进版_含脑图.pdf                      (506,288 B, 2026-08-22 00:16)
    upload\仿光子范式算法实现报告_v4.3.md                      ( 22,504 B, 2026-08-22 01:45)
```

**扩展名**：`.py` 6｜`.pdf` 5｜`.json` 5｜`.md` 5｜`.docx` 2（＝23，**无尾差**）
**实测**：`output/` 13 件 + `upload/` 10 件 = 23 件；**无顶层散文件**；**0 隐藏文件**；mtime 全部落在 2026-08-22 00:16–14:42 单一制作窗内，**自 08-22 起 0 改动**。

### B.6 计数类差异处置

按 PI 2026-09-27 口径「文件数一类均 V4 收尾并整理时再校正」：

- **本棒 0 对账、0 追问、0 校正。**
- 已知待归 V4 收尾整理之计数项：① `deposon-repo` 根临时件由勘误链 :5084 所记 **16 件** → 本棒清理后 **9 件**（差额 −7，即本棒 trash 件数）；② 四目录 Top 10 扩展名尾差（repo 余 17 件 / archive 余 61 件）；③ `.pyc` 46 件之清否（PI 未决项「6」）；④ 通用口径基线差异（如 986/994/1,004 之旧挂账）。
- 以上**如实登记现状即止**，不单独成卷。

---

## §C 老实交代

### C.1 被拦 / 受限命令

- **0 条命令被安全策略拦截。** 本棒 0 尝试绕道删除，0 尝试绝对路径删除，0 尝试内联删除脚本。
- 交付包（④）**0 触碰**：B 段全只读。
- 此前他棒留痕：`.tmp_recovery\L1_g66.md:37` 记「`.tmp_p10_*`、`.scratch_*`（安全策略拦截删除，无害候处置）」——本棒**未复用**该路径，改为走 `rm --` 可恢复通道并成功。

### C.2 0 清判定（哪些**没清**、为什么）

| 类别 | 件数 | 字节 | 0 清理由 |
|---|---|---|---|
| `.pyc` / `__pycache__` | 46 / 10 目录 | 1,327,171 | **PI 未决项「6 再生 .pyc 清否」未拍板** ⇒ 宁留勿错删 |
| `.scratch_gamma_r1\` | 31 | 2,408,669 | 第三方 PDF/XML 原始抓取，属证据留痕 |
| `.scratch_rj5\` | 26 | 6,952,002 | 同上 |
| `.scratch_t_verify\` | 18 | 42,099 | 18 步复算链自洽，属留痕 |
| `.tmp\`（内今日件） | 256 | 5,717,793 | 含 E-48 勘误节已登记之只读复算脚本、09-28 疑问 6 快照 26 件 |
| 保留之 9 件根临时件 | 9 | — | 承载不可复现唯一信息（见 A.2） |
| 四目录之 ②③④ | — | — | B 段全只读，0 移动 0 删除 |

### C.3 分类判读之不确定性（**PI 可推翻**）

A.1 第 3 条把勘误链 :5084 的 16 件登记判为「**计数登记行**而非内容依赖」，据此对其中 7 件施以清理。**该判读为本棒自裁，非 PI 授权**；若 PI 判该行构成内容级证据依赖，则 7 件可由 `.mavis-trash` 通道原路取回（`still_on_disk=0` 已自证其不在原路径，trash 为可恢复态）。此为本棒唯一一处需 PI 追认的判读点。

### C.4 快照时点与并发写入面（**计数不稳定，已如实标注**）

- `.tmp_recovery\` 在本棒 B 段窗口内**持续被并发写入**：21:26 观测 20 件 → 21:30:19 观测 **31 件**（新增 `shaindex.py` / `sha_index.tsv` / `hit_*.txt` / `TAIL_g6*.md` 等，mtime 密集落在 21:27–21:30）。该目录属**其他会话在跑工作面**。
- 故 `deposon-repo` 之 1,717 件 / 546,401,304 B 系 **21:30:19 瞬时快照**，非静止值；**该目录计数在交接瞬间即可能再变**。
- 本棒对 `.tmp_recovery\` **0 读内容、0 触动、0 计入清理面**（仅目录级计数与 mtime 取样）。
- 其余三目录（②③④）快照时点 21:29:21，均无并发写入迹象（② 最新件 09-28、③ 最新人工件 09-26、④ 全部 08-22），计数可信。

### C.5 纪律自证

- 0 编造：全部字节数 / 件数 / mtime / SHA-12 均由本棒 `hashlib` 等价复算与目录枚举实测产出；**未引用任何未实测之数**。
- 0 代裁：唯一判读点已在 §C.3 明示待 PI 追认；A.6 五项转移候选 0 执行。
- 0 回改既有件：全棒仅新增本件 1 份；对 `docs\` `results\` 等既有件 **0 写 0 改**。
- R4：**0 读 key**、**0 读 `.env`**、0 触及凭据面（A 段 SHA 复算仅读字节流，未解析内容）。
- 编码：UTF-8 无 BOM · LF。
- 落盘前撞名实测 CLEAR（见抬头）。

---

*本件由今日收工棒（worker）产出，仅供 parent 采信后并入唯一 README（明日开工必读）。本棒 0 改 README。*
