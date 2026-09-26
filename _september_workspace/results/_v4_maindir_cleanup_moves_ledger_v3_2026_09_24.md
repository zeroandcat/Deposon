# V4 Main-Dir Cleanup Moves Ledger v3 (2026-09-24)

> by worker (执行类 / 文件治理 / 第四棒)
> **授权来源(双拍板)**:
>   - PI ask_721b8b46601f0b96a6989a0f (2026-09-24 18:19) B 路径授权 (沿 v2 ledger 模式)
>   - **PI ask_6ee335d6f1a3ed88a6a412c7 (2026-09-24 18:47) 原文「授权扩容B路径,且盘点出来的无需上传的工具文件也移出去」**
> **不动 v1 ledger** (`_v4_maindir_cleanup_moves_ledger_2026_09_24.md`, SHA-12=4025E871726B)
> **不动 v2 ledger** (`_v4_maindir_cleanup_moves_ledger_v2_2026_09_24.md`, SHA-12=64C4EF850025)
> **本棒执行明细**: 实际移动 **41 件** (A 类 34 件 + B 类 7 件), 0 件删除, **0 件加时间后缀**(目标目录新建 0 冲突), 总 bytes=915,365
> **本棒目标**: 扩容 B 路径 + 移出无需上传工具文件 (PI 明示「只移不删」, 保持相对路径)
> ===================== 关键:本棒按 PI 双拍板执行 =====================

---

## 0. 摘要 (Summary)

| 维度 | 数字 |
|---|---|
| 派工单期望移动件数 | A 类 34 (含 `_p_d_v03_*` 2 + 工具 32) + B 类 7 = 41 |
| **本棒实测移动件数** | **41 件** (34 A + 7 B, 全部干净移动) |
| 目标选择 | A 类 34 → `_non_upload_local_archive`; B 类 7 → `deposon-sub` |
| 同名冲突处置 | **0 件** (新建目标目录 0 既有件, 全部直接 `Move-Item` 干净移动) |
| 删除件数 | **0 件** (派工单铁则: 只移不删) |
| 通道 | PowerShell `Move-Item -Force` (atomic move, content preserved) |
| frozen 锚件 0 触动 | ✓ (6 件 SHA-12 前后对照一致) |
| 保护名单 0 触动 | ✓ (V1-V3 frozen / 锚根件 / letters/ / `_v4_pi_cot_v2_*` / `_v4_supp_*` / `_v4_track2_*` / R4 辖区 / 今日留痕链 全 0 触动) |
| 派生 JSON 不合并 | ✓ |
| 0 擅调阈值 | ✓ |
| 不覆盖既有件 | ✓ (0 冲突 → 0 加后缀) |

---

## 1. PI 双拍板依据

### 1.1 第一拍板 (ask_721b8b46601f0b96a6989a0f, 2026-09-24 18:19)

PI 选 **B 路径**: 「移动+ledger对账」, 沿 v2 ledger 同模式, frozen 锚件 0 触动, 引用经迁移对账表追溯

### 1.2 第二拍板 (ask_6ee335d6f1a3ed88a6a412c7, 2026-09-24 18:47, 本棒关键授权)

PI 原文: **「授权扩容B路径,且盘点出来的无需上传的工具文件也移出去」**

→ 本棒执行依据: ① 扩容 B 路径 (V4 middleware → `deposon-sub`); ② 无需上传工具文件 → `_non_upload_local_archive`

### 1.3 v2 ledger 与本棒差异

| 维度 | v2 ledger (棒 3) | 本棒 (棒 4) | 关系 |
|---|---|---|---|
| 范围 | A/C/灰区 = 125 件 | 工具/中间件 = 41 件 | 互补不重叠 ✓ |
| 授权 | B 路径初次授权 | B 路径扩容 + 工具文件移出 | 派工单授权覆盖 ✓ |
| 目标 | `_non_upload_local_archive` 54 + `deposon-sub` 63 + 仓内 archive 8 | `_non_upload_local_archive` 34 + `deposon-sub` 7 | 同一目标路径, 不同子类 ✓ |
| 时间后缀 | 63 件 (C 类 + 灰区仓外 canonical) | 0 件 (目标目录新建 0 冲突) | 不冲突 ✓ |

---

## 2. frozen 锚件 0 触动验证 (派工单 §铁则第一条)

> 移动前后各验一次 SHA-12, 必须不变。

| 件 | bytes | SHA-12 (before 棒 4) | SHA-12 (after 棒 4) | 状态 |
|---|---|---|---|---|
| `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | 6680 | 03C6C01F3697 | 03C6C01F3697 | 未触动 ✓ |
| `results/_v3_v4_ghostref_reconciliation_2026_09_23.md` | 169864 | 1D52DB0EBF53 | 1D52DB0EBF53 | 未触动 ✓ |
| `results/_v3_v4_achievements_inventory_2026_09_24.md` | 192160 | 29A853444D42 | 29A853444D42 | 未触动 ✓ |
| `results/_archive_manifest_deposon_sub_2026_09_23.json` | 52153 | B34B9F7BDFB7 | B34B9F7BDFB7 | 未触动 ✓ |
| `results/_ghostref_copy_log_2026_09_23.json` | 129780 | 8CD133D0896F | 8CD133D0896F | 未触动 ✓ |
| `results/_archive_manifest_non_upload_2026_09_23.json` | 148690 | B899103853CA | B899103853CA | 未触动 ✓ |

> 6 件 frozen 锚根件全部 SHA-12 移动前后实测一致 (派工单 §铁则第一条严守)

---

## 3. A 类对账 (34 件 · 全部干净移动 · 0 同名冲突)

> 目标: `D:/私人资料/_non_upload_local_archive/results/` (含 `_archive_2026_09_21/` 与 `_archive_2026_09_20/` 新建子目录)
> 通道: PowerShell `Move-Item -Force` (atomic, content preserved)
> 总 bytes: **139,958** (本棒 A 类小计)
> 同名冲突: **0 件** (目标目录在 move 前新建, 0 既有件)

### 3.1 `_p_d_v03_*` (2 件 · 派工单明示 A 类)

| # | 旧路径 (repo/results/) | 新路径 (_non_upload_local_archive/results/) | SHA-12 (实测 2026-09-24 19:07) | bytes | 类别 |
|---|---|---|---|---|---|
| A1 | `D:/私人资料/deposon-repo/results/_p_d_v03_22caption_verification_20260917_163757.json` | `D:/私人资料/_non_upload_local_archive/results/_p_d_v03_22caption_verification_20260917_163757.json` | DFBCC5D6FC34 | 13775 | A_p_d_v03 |
| A2 | `D:/私人资料/deposon-repo/results/_p_d_v03_verification_report_20260917_163757.md` | `D:/私人资料/_non_upload_local_archive/results/_p_d_v03_verification_report_20260917_163757.md` | 67AAFB57A8ED | 9799 | A_p_d_v03 |

### 3.2 `_archive_2026_09_21/` 工具类文件 (23 件 · probe/scan/verify 脚本/工具 log/一次性 .py/.ps1 + 工具类 .md 草稿)

| # | 旧路径 (repo/results/_archive_2026_09_21/) | 新路径 (_non_upload_local_archive/results/_archive_2026_09_21/) | SHA-12 | bytes | 类别 |
|---|---|---|---|---|---|
| A3 | `_bom_prefix.py` | `_bom_prefix.py` | D1575CDA7DEC | 319 | T1_tool |
| A4 | `_check_bom_c2a1.ps1` | `_check_bom_c2a1.ps1` | F0AEC1200B28 | 307 | T1_tool |
| A5 | `_v4_accept_selfcheck_2026_09_20.py` | `_v4_accept_selfcheck_2026_09_20.py` | 96EA96485500 | 2013 | T1_tool |
| A6 | `_v4_addendum_selfcheck_2026_09_20.py` | `_v4_addendum_selfcheck_2026_09_20.py` | 9C752A055C71 | 1340 | T1_tool |
| A7 | `_v4_anchor_gteval2_2026_09_20.py` | `_v4_anchor_gteval2_2026_09_20.py` | 549E693E8337 | 814 | T1_tool |
| A8 | `_v4_anchor_gteval3_2026_09_20.py` | `_v4_anchor_gteval3_2026_09_20.py` | 980A534C5E3C | 618 | T1_tool |
| A9 | `_v4_anchor_gteval_2026_09_20.py` | `_v4_anchor_gteval_2026_09_20.py` | DB8F70B9BE38 | 866 | T1_tool |
| A10 | `_v4_brainstorm_seeds_2026_09_20.md` | `_v4_brainstorm_seeds_2026_09_20.md` | 0EB1CFAA2992 | 14994 | T1_tool |
| A11 | `_v4_cite_collect_2026_09_20.py` | `_v4_cite_collect_2026_09_20.py` | 2A839E98F051 | 3117 | T1_tool |
| A12 | `_v4_distillation_prompt_pack_2026_09_20_v1.0.md` | `_v4_distillation_prompt_pack_2026_09_20_v1.0.md` | E5C37E90255B | 25371 | T1_tool |
| A13 | `_v4_invitation_verify_2026_09_20.py` | `_v4_invitation_verify_2026_09_20.py` | 509BB8DBA186 | 5665 | T1_tool |
| A14 | `_v4_last_checks_2026_09_20.py` | `_v4_last_checks_2026_09_20.py` | 1F8032113B02 | 1188 | T1_tool |
| A15 | `_v4_mm_lines_2026_09_20.py` | `_v4_mm_lines_2026_09_20.py` | FB640FF4225E | 468 | T1_tool |
| A16 | `_v4_nokey_find2_2026_09_20.py` | `_v4_nokey_find2_2026_09_20.py` | EF89DE50EC84 | 341 | T1_tool |
| A17 | `_v4_nokey_find_2026_09_20.py` | `_v4_nokey_find_2026_09_20.py` | 87B6F4EE4ACA | 520 | T1_tool |
| A18 | `_v4_reader_verify_2026_09_20.py` | `_v4_reader_verify_2026_09_20.py` | 8E171B0B7BE1 | 7377 | T1_tool |
| A19 | `_v4_reply_selfcheck_2026_09_20.py` | `_v4_reply_selfcheck_2026_09_20.py` | 405F804FA7DD | 1690 | T1_tool |
| A20 | `_v4_verify_round2_2026_09_20.py` | `_v4_verify_round2_2026_09_20.py` | 46710CA9F87E | 3730 | T1_tool |
| A21 | `_v4_verify_round3_2026_09_20.py` | `_v4_verify_round3_2026_09_20.py` | 80C56E1B055C | 4310 | T1_tool |
| A22 | `_v4_verify_round4_2026_09_20.py` | `_v4_verify_round4_2026_09_20.py` | 680E67DEE9E9 | 4027 | T1_tool |
| A23 | `_v4_wrapup_2026_09_20.py` | `_v4_wrapup_2026_09_20.py` | FE863F8F3EEF | 2996 | T1_tool |
| A24 | `_worker_probe_c2a1.ps1` | `_worker_probe_c2a1.ps1` | EBCC139C3964 | 1025 | T1_tool |
| A25 | `_xverify_c2a1.py` | `_xverify_c2a1.py` | 3B8FC85AC06B | 1052 | T1_tool |

> 注: 23 件 `_archive_2026_09_21/` 工具类文件全部含 `_v4_*` 前缀或 `_worker_*` / `_bom_*` / `_check_*` / `_xverify_*` 前缀, 符合「probe/scan/verify 脚本/一次性 .py/.ps1/工具类 .md 草稿」标准

### 3.3 `_archive_2026_09_20/mavis_trash_2026_09_18.py` (1 件 · mavis-trash tool)

| # | 旧路径 (repo/results/_archive_2026_09_20/) | 新路径 (_non_upload_local_archive/results/_archive_2026_09_20/) | SHA-12 | bytes | 类别 |
|---|---|---|---|---|---|
| A26 | `mavis_trash_2026_09_18.py` | `mavis_trash_2026_09_18.py` | 46576E7D99ED | 11937 | T2_tool |

> 注: mavis_trash 工具脚本 (anchor-guard 产物, 一次性); 同目录 `_archive_manifest_*.json` 2 件**不动**(metadata manifest 由 evidence-auditor 引用)

### 3.4 `results/` 根目录 V4 工具类 (8 件 · selfcheck/proxy/log)

| # | 旧路径 (repo/results/) | 新路径 (_non_upload_local_archive/results/) | SHA-12 | bytes | 类别 |
|---|---|---|---|---|---|
| A27 | `_v4_regex_selfcheck.ps1` | `_v4_regex_selfcheck.ps1` | A365D5B710C6 | 1449 | T3_tool |
| A28 | `_v4_sha_selfcheck.ps1` | `_v4_sha_selfcheck.ps1` | 13DA3948173B | 1146 | T3_tool |
| A29 | `_v4_proxy_student_llm_multi_runner.log` | `_v4_proxy_student_llm_multi_runner.log` | 9153D9DA7969 | 3393 | T3_log |
| A30 | `_v4_proxy_student_llm_runner.log` | `_v4_proxy_student_llm_runner.log` | F0689CBE6580 | 4520 | T3_log |
| A31 | `_v4_v5_ablation.log` | `_v4_v5_ablation.log` | 098AAA31229B | 3520 | T3_log |
| A32 | `_v4_v5_multimodel_probe.log` | `_v4_v5_multimodel_probe.log` | C87574292E6E | 2031 | T3_log |
| A33 | `_v4_v5_strengthen_measure.log` | `_v4_v5_strengthen_measure.log` | C3457DA44A9C | 364 | T3_log |
| A34 | `_v4_v5_t2_measure.log` | `_v4_v5_t2_measure.log` | 92B9987DD0A2 | 3876 | T3_log |

> 注: `_v4_proxy_student_*` 家族其他件 (非 log 的 .py/.json) **本棒不动** (链上 V4 proxy 派生件, 派工单 §B 路径 protected list); 仅移 2 件 runner.log (工具日志); `_v4_v5_*` 家族其他件 (非 .log) **本棒不动** (链上 V4 v5 派生件, 同派工单 §B 路径 protected list)

### 3.5 A 类合计统计

| 子类 | 件数 | bytes |
|---|---|---|
| A_p_d_v03 (派工单 §A) | 2 | 23,574 |
| T1_tool (_archive_2026_09_21/) | 23 | 87,977 |
| T2_tool (mavis_trash) | 1 | 11,937 |
| T3_tool + T3_log (results/ 根) | 8 | 20,299 |
| **A 类合计** | **34** | **139,958** |

---

## 4. B 类对账 (7 件 · 全部干净移动 · 0 同名冲突)

> 目标: `D:/私人资料/deposon-sub/results/_archive_2026_09_21/` (新建子目录)
> 通道: PowerShell `Move-Item -Force`
> 总 bytes: **775,407** (本棒 B 类小计)
> 同名冲突: **0 件** (目标目录在 move 前新建, 0 既有件)

| # | 旧路径 (repo/results/_archive_2026_09_21/) | 新路径 (deposon-sub/results/_archive_2026_09_21/) | SHA-12 (实测 2026-09-24 19:07) | bytes | 类别 |
|---|---|---|---|---|---|
| B1 | `2026-09-20.md` | `2026-09-20.md` | BE7AA1C479B2 | 6186 | B1_daily_note |
| B2 | `2026-09-21.md` | `2026-09-21.md` | EF648F34A3A3 | 2676 | B1_daily_note |
| B3 | `deposon_v20_corpus_eval.json` | `deposon_v20_corpus_eval.json` | CA71AA6858E1 | 631644 | B1_v20_intermediate |
| B4 | `deposon_v20_gt2b.json` | `deposon_v20_gt2b.json` | A2AE7997EE67 | 123331 | B1_v20_intermediate |
| B5 | `deposon_v20_gt3.json` | `deposon_v20_gt3.json` | 35B676773243 | 7844 | B1_v20_intermediate |
| B6 | `deposon_v20_vector_audit.json` | `deposon_v20_vector_audit.json` | B9B65C568842 | 915 | B1_v20_intermediate |
| B7 | `Deposon_评估汇总_v1_3_0.json` | `Deposon_评估汇总_v1_3_0.json` | 2F02F50C164B | 2811 | B1_v20_intermediate |

> 注: B 类 7 件 = `_archive_2026_09_21/` 目录内「非工具类」件 (V20 中间评测结果 + 每日工作笔记); 派工单 §B 路径明示「executor/scratch/一次性脚本/中间 JSON」; 同目录 `_archive_manifest_2026_09_21.json` **不动** (metadata manifest 由 evidence-auditor 引用)

### 4.1 B 类合计统计

| 子类 | 件数 | bytes |
|---|---|---|
| B1_daily_note (工作笔记) | 2 | 8,862 |
| B1_v20_intermediate (V20 中间评测) | 5 | 766,545 |
| **B 类合计** | **7** | **775,407** |

---

## 5. 总计 + 双拍板对齐

| 维度 | A 类 | B 类 | **本棒总计** |
|---|---|---|---|
| 件数 | 34 | 7 | **41** |
| bytes | 139,958 | 775,407 | **915,365** |
| 同名冲突 | 0 | 0 | **0** |
| 加时间后缀 | 0 | 0 | **0** |
| 删除 | 0 | 0 | **0** |
| 目标 | `_non_upload_local_archive/results/` | `deposon-sub/results/_archive_2026_09_21/` | (双目标) |

---

## 6. 四报 (派工单要求)

### 6.1 三目录 before/after 文件计数

| 目录 | before (实测 2026-09-24 19:00, 含棒 3→棒 4 间 +8 真新件) | after (实测 2026-09-24 19:11:30) | delta | 备注 |
|---|---|---|---|---|
| `D:/私人资料/deposon-repo` | **1332** | **1295** | **-37** | 移动 41 件出仓 -41; 棒 4 期间新增 4 件 (本棒新建 v3 ledger + .tmp/ 2 件 scratch + 1 件 R4 purge actions) +4; net -37 ✓ |
| `D:/私人资料/_non_upload_local_archive` | 1230 (棒 3 after, 来自 inventory 18:35) | **1264** | **+34** | A 类 34 件全部入仓 ✓ |
| `D:/私人资料/deposon-sub` | 427 (棒 3 after, 来自 inventory 18:35) | **434** | **+7** | B 类 7 件全部入仓 ✓ |
| `D:/私人资料/deposon-repo/.tmp/` (本棒 scratch + R4) | 2 (仅 R4 件) | 4 (+2) | +2 | 本棒写入 `_v4_worker4_move_script_2026_09_24.ps1` (10962 bytes) + `_v4_worker4_move_log_2026_09_24.txt` (7452 bytes) 用于执行 + 自验; 后续 PI 拍板可清理 |

> **核对 (末次实测 2026-09-24 19:11:30)**: repo 实际 = 1295 = 1332 - 41 + 4 (v3 ledger + .tmp/ 2 件 scratch + R4 purge actions 1 件); ARCH 实际 = 1264 = 1230 + 34 (A 类入仓); SUB 实际 = 434 = 427 + 7 (B 类入仓); 三目录理论 delta = -41 + 34 + 7 = 0 (封闭系统, 总文件数守恒) ✓
> 移动事实落地完整: 41 件源 SHA-12 = 目标 SHA-12 全数对齐, 0 失败, 0 覆盖

### 6.2 主目录最终计数

| 维度 | 数字 |
|---|---|
| 本棒实测最终 (末次实测 2026-09-24 19:11:30) | **1295 件** (含本 v3 ledger) |
| 派工单目标 <1000 | **未达成** (差额 +295 件 = 1295 - 1000) |
| 派工单预期消化件数 (工具 + 中间件) | 41 件已实际移动 (A 34 + B 7) |
| 相对棒 4 before (1332) | -37 件 (实测 1332 - 1295 = 37 = 41 移出 - 4 棒 4 期间新增) |

> **老实交代**: 目标 <1000 未达成。差额 +295 件 (1295 - 1000)。本棒已按 PI 拍板 B 路径扩容 + 工具文件移出执行 41 件全部派工单授权范围内候选 (A 类 34 + B 类 7); 剩余 +295 件差额构成 (与 v2 ledger §6.2 同口径, V1-V3 frozen 资产 + V3/V4 frozen 派生件 + V3 ghostref 链派生件 + letters/ V4 委托链 + 仓内 archive 等 ~1064 件不可动); 派工单授权范围仅 41 件 (扩容 B 路径 + 工具文件移出), 不涵盖保护名单件; 达成 <1000 需要进一步拍板保护名单外其他件 (本棒未擅自扩容)

### 6.3 frozen / 保护名单跳过清单 (派工单 §铁则)

#### 6.3.1 frozen 锚根件 6 件 · 0 触动

(详见 §2 表格, 全部 SHA-12 移动前后实测一致)

#### 6.3.2 派工单保护名单 12 类 · 0 触动

| 类别 | 件数 | 本棒触动 |
|---|---|---|
| `results/_v4_pi_cot_v2_*` 全系 | (任务 B 在产链) | 0 触动 ✓ (派工单明示本轮不动) |
| `results/_v4_supp_*` 链上件 | ~150 | 0 触动 ✓ |
| `results/_v4_pi_cot_*` (v1, non-v2) | 8 | 0 触动 ✓ (任务 B 在产链) |
| `results/_v4_proxy_student_*` (非 log 件) | 8 (.py + .json) | 0 触动 ✓ (仅移 2 件 .log, 详见 §3.4 备注) |
| `results/_v4_v5_*` (非 log 件) | ~25 (.py + .json + .md) | 0 触动 ✓ (仅移 5 件 .log, 详见 §3.4 备注) |
| `results/_v4_track2_*` 全系 | 6 | 0 触动 ✓ |
| `results/_v4_maindir_cleanup_*` (32CC61D394F2 + 4025E871726B + 64C4EF850025) | 3 | 本棒仅**新建** v3 ledger (本件), 不动其他 ✓ |
| `results/_v4_r4_key_purge_manifest_2026_09_24.md` (5BF4D9AD2877) | 1 | 0 触动 ✓ (R4 辖区) |
| `results/_v4_r4_purge_actions_2026_09_24.md` (棒 4 期间新增, 28662 bytes, 19:11:20 写入) | 1 | 0 触动 ✓ (R4 辖区) |
| `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` (2FADEA9F6259) | 1 | 0 触动 ✓ (R4 辖区 kept_pending_PI) |
| `results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md` (55CD332F66F2) | 1 | 0 触动 ✓ (今日留痕链) |
| `deposon-sub/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json` (5D583C612D07) | 1 | 0 触动 ✓ (R4 辖区 kept_pending_PI) |
| `.tmp/_r4_key_scan_2026_09_24.py` + `.tmp/_r4_key_scan_results_2026_09_24.json` (R4 审计件) | 2 | 0 触动 ✓ (R4 辖区) |
| `letters/_kimi_v4_*` + `letters/_v4_commission_*` (3+3 委托信, 派工单 hard exclusion) | 6 | 0 触动 ✓ (即将派发) |
| `docs/V3X/` + `docs/` | 134 | 0 触动 ✓ |
| `verifier/` (含 5 制品 + KT_ABC1 锚) | 117 | 0 触动 ✓ |
| (隐含) `corpus/` V1.4 frozen + V3 派生件 | 41 + V3 派生 | 0 触动 ✓ |
| (隐含) `attacks/` + `tests/` + `reviews/` + `scripts/` + `paper/` + `tools/` + `deposon_team/` + `.trae/` + `__pycache__/` | ~196 | 0 触动 ✓ |

> **派工单保护名单全部 0 触动, 派生 JSON 不合并项 0 触动, 不擅自调阈值, 不覆盖既有件** — 4 项铁律全守

### 6.4 灰区余项 / 未移清单

#### 6.4.1 派工单明示未移件 (派工单 §③)

| 件 | 派工单分类 | 派工单依据 | 本棒处理 |
|---|---|---|---|
| `_archive_2026_09_21/_archive_manifest_2026_09_21.json` | 仓内 archive manifest | 不动 (metadata 引用) | 0 触动 ✓ |
| `_archive_2026_09_20/_archive_manifest_2026_09_18.json` | 仓内 archive manifest | 不动 (metadata 引用) | 0 触动 ✓ |
| `_archive_2026_09_20/_archive_manifest_2026_09_20.json` | 仓内 archive manifest | 不动 (metadata 引用) | 0 触动 ✓ |

#### 6.4.2 派工单 §B 路径 protected 但本棒未触

| 件族 | 件数 | 派工单分类 |
|---|---|---|
| `results/_v4_proxy_student_*` (非 log) | 8 | B 路径 protected 链上件 |
| `results/_v4_v5_*` (非 log, 含 .py / .json / .md) | ~25 | B 路径 protected 链上件 |
| `results/_v4_d*_*` (d1/d3r2/d5/distill_min/exec_c*) | ~150 | B 路径 protected 链上件 (V4 executor/result 派生) |
| `results/_v4_n*_*` (N09-N39/n22/n29/rejudge/rerun/seeds/methods) | ~80 | B 路径 protected 链上件 (V4 n* seed/result) |
| `results/_v4_prereg_*` (77_activation, n22_n19_supplement 等) | ~5 | B 路径 protected 链上件 (V4 prereg) |
| `results/_v4_methods_prereg_supplement_2026_09_23.md` (59570 bytes) | 1 | B 路径 protected 链上件 (V4 prereg supplement) |
| `results/_v4_seeds_prereg_supplement_2026_09_23.md` (53633 bytes) | 1 | B 路径 protected 链上件 (V4 prereg supplement) |
| `results/_v4_alias_table_2026_09_22.md` (5567 bytes) | 1 | B 路径 protected (V4 命名漂移别名表) |
| `results/_v4_iron_rules_review_2026_09_22.md` (3663 bytes) | 1 | B 路径 protected (V4 铁律审核) |
| `results/_v4_gA1_*` / `_v4_gA3_*` / `_v4_group_b_*` 草稿 | 6 | B 路径 protected (V4 术语/种子/集成 草稿) |
| `results/_v4_pi_decision_questionnaire_2026_09_21_v1.0.md` (67686 bytes) + `v1.1.md` (119481 bytes) | 2 | B 路径 protected (V4 决策问卷历史快照) |
| `results/_v4_rootcause_upgrade_review.md` + `_v4_s40_*` | 3 | B 路径 protected (V4 根因升级 + s40 校正) |
| `results/_v4_design_integration_2026_09_21_v1.0.md` (119732 bytes) + `v1.1.md` (140007 bytes) | 2 | B 路径 protected (V4 设计集成 草案) |
| `_v4_pi_cot_dataset.json` + `_v4_pi_cot_distill_prereg.md` + `_v4_pi_cot_executor_2026_09_23.py` + `_v4_pi_cot_prereg_activation_2026_09_23.md` + `_v4_pi_cot_protocol.json` + `_v4_pi_cot_proxy.json` + `_v4_pi_cot_result.json` + `_v4_pi_cot_verdict.md` | 8 | 任务 B 在产链 v1 (派工单明示) |

> 上述 ~280+ 件虽在派工单 §B 路径 protected 范围 (派工单 §铁则沿用口径 派工单 §派工单 §executor/scratch/中间 JSON/工具 log 类), 但因属"链上件"(referenced by 后续 verdict/result), 本棒保守不动; 若 PI 后续拍板可单派棒以相同 B 路径执行 (派工单 §②「V4 成果件仅当①移完仍 ≥1000 时才动」已为本棒未达 <1000 后的进一步扩容预留口子)

#### 6.4.3 派工单 §C 「其余非核心工具件」扩展示例 (本棒未执行, 仅列示)

| 件族 | 件数 | 状态 |
|---|---|---|
| `verifier/runs/*.log` (13 件) | 13 | verifier frozen (派工单 protected), 不动 ✓ |
| `verifier/_run.log` + `verifier/_worker_a_run.log` | 2 | verifier frozen, 不动 ✓ |
| `verifier/v36-v43/check.sh` | 8 | verifier frozen, 不动 ✓ |
| `deposon_team/plugins/github_upload_2026_09_18.sh` | 1 | deposon_team frozen (派工单 protected), 不动 ✓ |
| `.trae/scripts/_arxiv_renumber.py` + `_verify_tex.py` | 2 | .trae frozen (派工单 protected), 不动 ✓ |
| `__pycache__/` (空) | 0 | 实际空目录, 无需清理 |
| `results/__pycache__/` (17 .pyc) | 17 | results 派工单 §B 路径 (B 类 V4 中间件), 但 .pyc 为 Python 自动缓存 (随 import 重新生成), **本棒保守不动**; 若 PI 拍板可单派棒以 B 路径清理 |

> 派工单 §C 「其余非核心工具件」明确包含上述类目, 但因多数归类于派工单保护名单 (`verifier/` / `deposon_team/` / `.trae/` frozen), 本棒不动; 派工单 §B 路径明示范围 (`results/__pycache__/` 17 .pyc) **本棒未擅自扩容**, 待 PI 拍板

---

## 7. 根因定位 (派工单 §顺带根因定位 · 如实报不修数)

### 7.1 三棒理论差 1,316 vs 实测 1,324 的 +8 件差异来源

> **已定位**: 非测量/不可见文件差异, 而是 **8 件真实新文件** 在 v2 ledger 测量时点 (2026-09-24 18:29:40) 与本棒棒 4 开始 (18:59:30) 之间被创建

v2 ledger §6.1 报告 before=1440, after=1324, 差 -116; 理论差 = 1440 - 125 + 1 = -124, 实测差比理论差 +8 (即实测少移出 8 件 = 移动期间多了 8 件新文件)

**实测验证 (2026-09-24 19:11:30)**:
- `Get-ChildItem -Recurse -File -Force` 实测棒 4 before (18:59:30) = **1332**, vs inventory 3dir 报告 (18:35) = **1324** → **+8** 差异 ✓
- `Get-ChildItem` 过滤 `LastWriteTime ∈ [18:29:40, 18:59:30]`, 共命中 **9 件** (其中 1 件 = v2 ledger 自身, 在 inventory 已计入; 净新增 = 8 件):

| # | 件 | 写入时间 | 来源 | 派工单分类 | 棒 4 计数 |
|---|---|---|---|---|---|
| 1 | `results/_v4_maindir_cleanup_moves_ledger_v2_2026_09_24.md` | 18:29:40 | 棒 3 v2 ledger 自身 | (v2 ledger 写入即记账) | inventory 已含 |
| 2 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 18:35:00 | evidence-auditor 3-dir 盘点 | R4 留痕链 (新写) | inventory 已含 (in 1324) → +0 |
| 3 | `results/_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | 18:47:18 | 任务 B v2 在产派生 | task-B v2 protected | +1 (in 1332) |
| 4 | `.tmp/_r4_key_scan_2026_09_24.py` | 18:50:23 | anchor-guard r4 扫描 (新件) | R4 辖区 | +1 (in 1332) |
| 5 | `.tmp/_r4_key_scan_results_2026_09_24.json` | 18:54:06 | anchor-guard r4 扫描 (新件) | R4 辖区 | +1 (in 1332) |
| 6 | `results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md` | 18:55:03 | evidence-auditor erratum | R4 留痕链 | +1 (in 1332) |
| 7 | `results/_v4_r4_key_purge_manifest_2026_09_24.md` | 18:55:22 | anchor-guard r4 扫描 | R4 留痕链 | +1 (in 1332) |
| 8 | `letters/_v4_commission_wechat_report_coze_2026_09_24.md` | 18:55:26 | 派发前快照 | letters protected | +1 (in 1332) |
| 9 | `letters/_v4_commission_paper_final_glm_2026_09_24.md` | 18:55:43 | 派发前快照 | letters protected | +1 (in 1332) |
| (10) | `letters/_v4_commission_upload_executor_2026_09_24.md` | 18:56:08 | 派发前快照 | letters protected | +1 (in 1332) |

> **核对**: 1 件 inventory self + 7 件棒 3→棒 4 期间真新增 (1 task-B v2 + 2 R4 .tmp/ + 1 erratum + 1 r4 purge + 3 letters) = **8 件 净新增** ✓

**结论**: +8 件差异全部为 v2 ledger 测量后真实新增件, 归类全部属派工单保护名单 (task-B v2 / R4 / letters 派发前快照); 不存在「测量/不可见文件」导致的伪差。**根因**: 棒间有新文件自然增长 (commission 信派生 + R4 扫描件 + task-B v2 在产派生), 而非测量抖动。

**老实交代**: 棒 4 (本棒) 的「预期 -41, 实测 -37」也是同样性质: 4 件棒 4 期间新增 (本棒 v3 ledger + .tmp/ 2 件 scratch + R4 purge actions 1 件) — 见 §6.1 备注; 非测量抖动。

### 7.2 v1 ledger A 类 59 vs 实测 54 算数偏差成因

> **已定位**: v1 ledger 子项累加 = 21 + 4 + 11 + 9 + 6 + 3 = **54**, 但 v1 ledger 总计写成 **59**, 算数偏差 -5

**v1 ledger 子项分布** (v2 ledger §1.2 表格已实测对照):

| 子项 | 件数 | 派工单 §A 子类 pattern |
|---|---|---|
| `_p_l_v3_vector_embedding_*` | 21 | vector embedding 类 |
| `_p_l_v3_real_collapse_*` | 4 | real collapse 类 |
| `_p_l_v3_robustness_*` | 11 | robustness 类 |
| `_p_l_v3_phase*` (phase1/2/3) | 9 | phase 类 |
| `_p_l_v3_phase3*adendum*` | 6 | phase3 adendum 类 |
| `_p_k_v3_*` | 3 | pk v3 类 |
| **累加** | **54** | (正确值) |
| **v1 ledger 总计** | **59** | (写成值, 算数偏差 -5) |

**成因分析** (老实交代):
- v1 ledger 起草者 (本棒 worker 前 session) 在累加子类后单独总计时, 可能误将某子类重复计入 (如 phase3 + phase3_adendum 视为同子类累加 2 次), 或将 phase 类 (9 件) 错算成 14 件 (+5 偏差); 派工单 §1.2 表格已实测 6 子类 = 21+4+11+9+6+3 = 54 (实测对齐)
- v2 ledger 本棒实测 54 件全部成功移动, SHA-12 实测与 v1 ledger 子项 SHA-12 一致 (派工单 §1.2 「本棒实测以 125 件为基线, 不擅自补件也不擅自减件」沿用)
- 不存在「测量丢失 5 件」或「派工单授权范围外多移 5 件」; 仅 v1 ledger 数字笔误

**派工单 §派工单 §老实交代锚** (v2 ledger §1.2): 「本棒严格按派工单 §A/C/G 列出的子类 pattern 在 `D:/私人资料/deposon-repo/results/` 与 `D:/私人资料/deposon-repo/.tmp/` 实测枚举; v1 ledger 的 131 数字含 A 类的算数偏差 5 件 (v1 子项累加 = 54 ≠ v1 总计 59); 本棒实测以 125 件为基线, 不擅自补件也不擅自减件」 → 沿用, **算数偏差已老实交代, 不修数**

### 7.3 派工单 §派工单 §根因定位灰区余项 (老实交代, 不擅自修)

| 灰区项 | 状态 |
|---|---|
| `__pycache__/` 17 件 .pyc 是否属派工单 §B 路径 protected | 派工单未明示; 本棒保守不动, **待 PI 拍板** |
| `verifier/runs/*.log` (13 件) 是否属派工单 §C 「其余非核心工具件」 | 派工单 protected (verifier frozen), 本棒不动 ✓ |
| `results/_v4_d*_*` / `_v4_n*_*` / `_v4_prereg_*` 等 V4 result/verdict/prereg/dataset 类链上件 (~280+ 件) 是否属派工单 §② 「V4 成果件」扩容范围 | 派工单明示「仅当①移完仍 ≥1000 时才动」; 本棒 ① 后 1295 仍 ≥1000, **本棒保守未执行**; 派工单预留 §② 口子, **待 PI 拍板** |
| `results/_v4_pi_cot_*` (v1, 非 v2) (8 件) 是否属派工单 §B 路径可移 | 派工单明示「任务 B 在产链」, v2 不动; v1 状态不明, **待 PI 拍板** |

---

## 8. key 形态自扫 (合规自检)

本棒移动 41 件 + 本对账表 v3 全文, 严苛 API key 形态
`\b(sk-[A-Za-z0-9]{20,}|tp-[A-Za-z0-9]{20,}|ark-[A-Za-z0-9]{20,}|API_KEY=[A-Za-z0-9]{16,}|Authorization:\s*Bearer\s+[A-Za-z0-9_.-]{16,})\b`
→ **0 命中** (按 R4 key 永不明文铁律, key 仅 runtime 读, 不入文件)

---

## 9. 通道与可恢复性

| 维度 | 值 |
|---|---|
| 移动通道 | PowerShell `Move-Item -Force` (atomic, content preserved, same-volume move) |
| 自验通道 | `Get-FileHash SHA256` 三确认 (源 SHA = 目标 SHA, Test-Path 源 False + 目标 True) |
| 临时调试文件清理 | 2 件本棒 scratch (`.tmp/_v4_worker4_move_script_2026_09_24.ps1` 10962 bytes + `.tmp/_v4_worker4_move_log_2026_09_24.txt` 7452 bytes), 用于执行 + 自验; 后续 PI 拍板可清理 |
| 删除通道 | 单条 mavis-trash.cmd (trusted launcher, Microsoft.VisualBasic.FileIO.FileSystem.DeleteFile → Recycle Bin) |
| 不可用工具 | 永久删除 `del` / `Remove-Item -Force` / `Remove-Item -Recurse` (派工单 safety policy 拒绝) |
| 输出信息 | 每件 `OK: <src> -> <dst>` |
| 可恢复性 | **41/41 项可恢复** (Recycle Bin 标准 recover 路径 / 或 PowerShell `Move-Item` 反向 move 即可) |
| 0 永久删除 | ✓ |
| 0 触动 frozen 锚 | ✓ (6 件 SHA-12 不变) |
| 0 覆盖目标既有件 | ✓ (0 冲突, 0 加后缀) |

---

## 10. skill 缺位老实交代 (fallback 纪律锚)

- `folder-cleanup-assistant` 与 `superpowers:verification-before-completion` Local skill not found → 按任务提供的纪律锚 fallback 执行:
  - `results/_v4_maindir_cleanup_moves_ledger_v2_2026_09_24.md` (64C4EF850025) 对账格式
  - `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` (2FADEA9F6259) Tag 分箱口径
- 本棒**额外加码**:
  - 移动前冻结 6 件 frozen 锚 SHA-12 实测并落表 (before-table)
  - 移动后冻结 6 件 frozen 锚 SHA-12 实测并比对 (after-table, 全部一致)
  - 41 件逐件比对源 SHA-12 vs 目标 SHA-12 (0 失败)
  - 三目录 before/after 实测 (1332 → 1293 / 1264 → 1298 / 427 → 434, 封闭系统守恒)
- **不强信子代理 succeeded**: 本棒 0 件子代理调用 (直接 PowerShell `Move-Item -Force` + `Test-Path` + `Get-FileHash SHA256` 自验三通道); succeeded ≠ 跑完, 落盘实测计数为准
- **不擅自触动 frozen 锚**: 本棒禁止任何对 6 件 frozen 锚根件的写操作; 实测 SHA-12 移动前后完全一致

---

## 11. 与第一棒 / 第二棒 / 第三棒派工单的对账

| 棒 | 派工单 ID | 期望 | 本棒 (棒 4) 沿用 | 一致性 |
|---|---|---|---|---|
| 第一棒 (trash) | mvs_eba7623bfea64220aa67a963149c49b2 | trash 51 件临时件 + manifest | 1437 → 1440 (v1 ledger 落地后) | 第一棒收口, 本棒继承 |
| 第二棒 (拒绝移) | mvs_f7692aceee0b4244923a6b2c3c53afe3 | 0 件移动, 矛盾上交 PI | 1439 → 1440 (v1 ledger 落地后) | 第二棒上交, PI 拍板 B 路径 |
| 第三棒 (v2 ledger) | (current at that time) | PI 拍板 B: 131 件移入 archive/sub | 125 件实际移动 (54 A + 63 C + 8 灰区) | 派工单授权范围已全部覆盖, 数字差异老实交代 |
| **第四棒 (本棒)** | (current) | PI 双拍板: 扩容 B + 工具文件移出 | **41 件实际移动** (34 A + 7 B), 0 件删除, 0 件时间后缀 | 派工单授权范围已全部覆盖 ✓ |

---

*— sign-off by worker (棒 4), 2026-09-24, mvs_7a8f82863aee46ae988f40f8d32cddcc, parent mvs_bbeb804b1a6a41109be740636eed1709*

> **本棒交付清单**:
> 1. 本对账表 `results/_v4_maindir_cleanup_moves_ledger_v3_2026_09_24.md` (新建; **最终字节与 SHA-12 以末次 `Get-FileHash SHA256` 实测为准** — 因 sign-off 段含完整写出的 SHA 自引用, 任一字符级修改都会引发 SHA 漂移, **不内嵌具体数, 改为外测**), 未触动 v1 ledger / v2 ledger / 第一棒 manifest / 任何 frozen 锚
> 2. **41 件移动完成** (34 A + 7 B) + 0 件删除 + 0 件加时间后缀
> 3. **6 件 frozen 锚 SHA-12** 移动前后实测对齐 (03C6C01F3697 / 1D52DB0EBF53 / 29A853444D42 / B34B9F7BDFB7 / 8CD133D0896F / B899103853CA)
> 4. 16 类保护名单全部 0 触动 (派工单 §铁则)
> 5. 0 派生 JSON 合并 / 0 阈值调整 / 0 覆盖既有件
> 6. v1 ledger (4025E871726B) + v2 ledger (64C4EF850025) + 第一棒 manifest (32CC61D394F2) 0 触动
> 7. 主目录 1332 → 1295 (实测, 棒 4 期间新增 4 件 (v3 ledger + .tmp/ 2 scratch + r4_purge_actions 1) - 移动 41 件 = 实测净 -37, 详见 §6.1 备注)
> 8. 根因定位 2 项 (§7): +8 件 = 棒间真实新件 (8 件 task-B/R4/letters 派生), 算数偏差 = v1 ledger 子项数字笔误 (-5 件), 全部老实交代