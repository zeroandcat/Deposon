# 批 14 #08c R-3 五锚追源件 · **0 恢复 0 改 0 移** · worker · 2026-09-29

> **件名**：`results/_v5_b14_r3_anchor_retrieval_2026_09_29.md`
> **承接**：PI 裁「#08c R-3 = **找回：另派棒全面追源**」（源件 `b69d65cbb329` §3-R-3 / §5 待拍板表第 3 行）
> **性质**：**只读追源核明件**。本件 **0 恢复任何件、0 移动任何件、0 改任何既有件、0 代 PI 拍板 R-3 二择一**。
> **⛔ 本件不做**：⛔ 0 恢复回收站件（只读扫描元数据）；⛔ 0 改册 / 源件（全只读）；⛔ 0 自算 manifest 落盘（**自算 ＝ 重定义锚集，属重基线，0 属 worker 职权**）；⛔ 0 编造任何路径或指纹；⛔ 0 把兄弟族（`P_A_*`）登记值当作 P_C 登记值使用。
> **R4 key 永不明文**：**0 读取 key、0 落盘、0 入 prompt / JSON / log**。
> **SHA-12 口径**：`hashlib.sha256(全文字节).hexdigest()[:12]`、**小写 12 位**、**盘上实测**；本件自身指纹不自写入本件（随回执回报）。
> **标注纪律**：全文对每条指纹区分 **【实测】**（本 turn `hashlib` 盘上复算）与 **【线索】**（沿引件链转录的登记值，本 turn 0 读到其登记载体者）。
> **版式**：UTF-8 无 BOM · LF。

---

## §0 输入链核验（**先核后引 · 盘上实测**）

| # | 件 | 本 turn 实测 SHA-12 | 字节 | 与派工单给定值 | 本件用途 |
|---|---|---|---:|---|---|
| 1 | `results/_v5_b14_08c_material_plan_2026_09_29.md` | **`b69d65cbb329`** | 22,104 | ✅ 一致 | §3-R-3 表（锚 ID / 对象 / 08c 实测结论）、§5 待拍板第 3 行 |
| 2 | `results/_v3_recheck_prereg_v1p3_2026_09_27.md` | **`a8da321b64d2`** | 33,904 | ✅ 一致 | §3.2 R-3 定义（L191）、§4.2.1 B.5（L270） |
| 3 | `docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md` | **`d427b2f57c33`** | 6,301 | ✅ 一致（与 `b69d65cbb329` §0 表第 4 行同值） | ⭐ **五锚清单唯一字面来源**（§2 L17–L29，本 turn **逐行直读**，非转录） |
| 4 | `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | **`03c6c01f3697`** | 6,680 | —（派工单未给，本 turn 定位） | ⭐ **兄弟族（P_A/P_B/P_C1 命名混淆，见 §3 注）锚登记载体**，含 5 值 frozen-run roster |
| 5 | `docs/V3X/RISK3_V0_FIXES_2026_09_11.md` | **`c00d1c22e7ed`** | 13,271 | —（本 turn 定位） | §6.2 KT-A1 锚表（L205–L211）＝ roster 的**第二处**登记副本 |
| 6 | `D:/私人资料/deposon_bundle_embedded.md` | 20,577,910 | — | — | 2026-09-01 全库快照（base64 包裹 zip，638 条）—— **本 turn 纯内存解码，0 落盘** |

---

## §1 五锚清单（**逐字直读 `d427b2f57c33` §2 L17–L29**）

| # | 锚 ID | 对象（spec §2 字面） | 算法 | 字段（spec §2 字面） | spec §1 对应句 |
|---|---|---|---|---|---|
| 1 | `P_C_ECR_BASELINE` | 本文 §3 ECR=1.333 基线 | SHA-256 全文 → 前 12 位 | `ecr_median=1.333` | 「本文 §3 的 ECR=1.333 基线」 |
| 2 | `P_C_GT_FORMAL_KILLS` | GT_FORMAL P1a/P1b/P2/P3 判死族 | SHA-256 全文 → 前 12 位 | `kills={"P1a":true, ...}` | 「本文 §3 的 GT_FORMAL P1a/P1b/P2/P3 判死族」 |
| 3 | `P_C_FROZEN_RUNS` | 5 个 frozen run JSON | SHA-256 各 → 前 12 位 | `runs=["v21_gtformal", ...]` | 「`verifier/runs/` 下 5 个 frozen run」 |
| 4 | `P_C_LLM_CLIENT` | `tools/llm_client.py` | SHA-256 全文 → 前 12 位 | `version=2026-09-11` | 「`tools/llm_client.py`」 |
| 5 | `P_C_SCALING_PROBE` | `tools/scaling_probe.py` | SHA-256 全文 → 前 12 位 | `version=2026-09-11` | 「`tools/scaling_probe.py`（**D1 由 data 实现**）」 |

> **登记值本体**：`d427b2f57c33` §2 L19 字面记「D1 由 successor 子代理计算，路径 `verifier/handoff/P_C_V0_anchors_sha256_12.json`」⇒ **五锚的登记值全部只存在于该 manifest 内**。该 manifest 本 turn **不可得**（§2 面 ①–⑥）⇒ **本件 0 能给出任何一锚的 P_C 登记值**。
> **spec §2 L29 字面**：「任何 ≥ 1 锚漂移 → 全 V0 撤回。」

---

## §2 检索面（**六面 · 只读 · 覆盖面登记**）

| 面 | 范围 | 方法 | 本 turn 结果 |
|---|---|---|---|
| ① | 工作区全树 `D:/私人资料/deposon-repo/` | 文件名 glob（`*scal*` / `*probe*` / `*anchor*` / `*baseline*` / `*gtformal*` / `*llm_client*` / `*scaling_probe*` / `*P_C_V0_anchors*` / `*deposon_v1[789]*` / `*deposon_v2[01]*`）＋ **全树 SHA-256 复算 1,617 件** | `scaling_probe` 命名 **0 命中**；锚值命中见 §3 |
| ② | `D:/私人资料/deposon-sub/`（仓外只读） | 同上 · 全树复算 **476 件** | 0 命中（`tmp_movedout_2026_09_28/` 已扫） |
| ③ | `D:/私人资料/_non_upload_local_archive/`（仓外只读 · 逐层） | 同上 · 全树复算 **1,458 件**；含 `.trae/snapshots/`、`backups/`、`.mavis/`、`verify_archive_backup/`、`verifier/handoff/`、`verifier/runs/`、`tools/` 逐层列举 | 0 命中 `scaling_probe`；`backups/`·`.mavis/`·`verify_archive_backup/` 内 **0** 件 `llm_client|scaling|exp_harness|anchors` |
| ③b | `D:/私人资料/Deposon_v1_2_0_交付包/`（仓外只读） | 全树复算 **23 件** | 0 命中（`upload/` + `output/` 全为 V1.2.0 期交付物） |
| ④ | Windows 回收站 `C:\$Recycle.Bin` / `D:\$Recycle.Bin` | **只读扫描**，列目录 + 读 `$I` 元数据 | **0 与五锚相关**（详见下） |
| ⑤ | `.tmp/`（工作区）、`_non_upload_local_archive/tmp/.tmp`、`%TEMP%` | 目录枚举 + 名称 glob | 0 命中（`%TEMP%` 命中 4 件均属他族：`anchor_fp.py` / `pk_anchor.py` / `verif_v3_div/anchors.py` / `vfy_sandbox/results/deposon_v20_baselines.json`） |
| ⑥ | 历史台账 / 勘误链 / 档案 manifest 的**路径字面** | `grep` 内容面 | 7 件含五锚 ID；沿引件链**先核后引**定位到 `03c6c01f3697` 与 `c00d1c22e7ed` 两处登记副本（§3 关键） |
| ⑥b | 2026-09-01 全库快照 `deposon_bundle_embedded.md` | **纯内存** base64 解码 → `zipfile` 目录遍历（638 条）＋ 逐成员内容面扫描 | `tools/` 仅 2 条（`make_figures_v2*.py`）；`verifier/handoff/` **0 条**；`docs/V3X/` **0 条**；全文 **0 条**内容含 `scaling_probe` / `P_C_V0_anchors` |

**④ 回收站实测明细（**0 恢复**，仅读元数据）**：

| 盘 | 件 | 字节 | mtime | 读出结论 |
|---|---|---:|---|---|
| `C:\$Recycle.Bin\S-1-5-21-…-500\` | `$I52NDVM` | 156 | 2026-09-28 16:12:28 | 版本 2 · 原大小 **378,100 B** · 删除时刻 2026-09-28 08:12:28 · 原路径 `C:\Users\Administrator\Downloads\…docx`（**与五锚 0 关联**） |
| 同目录 | `$R52NDVM`（数据体） | — | — | ⛔ **不存在** ⇒ 该条即便恢复亦 0 内容 |
| `C:\…`、`D:\…` | `desktop.ini` ×2 | 129 | 2026-09-21 | 系统件 · 0 关 |

⇒ **回收站 0 五锚相关件**（全盘仅 1 条已删项，且数据体已不在）。

**补充覆盖面（派工单 6 面之外，本 turn 顺带扫及）**：`D:/私人资料/` 顶层 38 项全部列举（含 `deposon_bundle_embedded.md`、`deposon_bundle_selfextract.sh`、`HANDOFF_MACHINE_READABLE.json`、`SESSION_BOOTSTRAP_PROMPT.md`、`AUDIT_2026-08-30.json`）。**四根目录均 0 `.git`** ⇒ **0 版本历史可回溯**（无 git 对象库、无 stash、无 reflog 面）。

---

## §3 逐锚登记（**在盘 / 不可得**）

> ⭐ **本 turn 关键发现（沿引件链先核后引所得）**：P_C 五锚的**登记值载体虽缺**，但**兄弟族锚登记值在盘** —— `verifier/handoff/KT_ABC1_anchors_sha256_12.json`（`03c6c01f3697`）§anchors.KT-A1 内**逐字记有 5 个 frozen run JSON 的完整 roster（5 个 SHA-12）**，`docs/V3X/RISK3_V0_FIXES_2026_09_11.md` §6.2（L209）为同一 roster 的第二处副本（两处字面互校一致）。
> ⚠️ **该族为 `P_A_*` 命名**（`KT-A1` 下），**0 等同 P_C 登记值**；本件**仅用它作「同名对象的已知指纹」去全盘复算命中**，**0 用它替代 P_C 登记值、0 据它宣告 P_C 锚的漂移与否**。

### 锚 1 `P_C_ECR_BASELINE`（对象＝本文 §3 ECR=1.333 基线）

| 项 | 值 | 标注 |
|---|---|---|
| 盘上位置 | `docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md` | 【实测】载体在盘 |
| 字节 / mtime | 6,301 B · 2026-09-08 16:03:54 | 【实测】 |
| 盘上实测 SHA-12 | **`d427b2f57c33`** | 【实测】 |
| P_C 登记值 | **不可得** | manifest 缺 |
| 口径外推值 | `d427b2f57c33` | **【推定】**非实测登记值 |

> **外推依据（可复核）**：`03c6c01f3697` 内 `P_A_ECR_BASELINE` 的 `path` 字段 ＝ `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md`、其 `value` ＝ `bd1caab42b4c`；本 turn 实测 **该 P_A spec 文件 SHA-12 ＝ `bd1caab42b4c`（10,351 B）** ⇒ **该族「对象＝本文 §3」时，登记值 ＝ spec 文件自身全文 SHA-12** 之口径**已被实测坐实**。同一口径施于 P-C spec ⇒ 推定 `d427b2f57c33`。
> **但**：P_C manifest 不可读 ⇒ 上述为**口径外推的推定值**，**不可用于宣告「P_C 锚 0 漂移」**。

### 锚 2 `P_C_GT_FORMAL_KILLS`（对象＝GT_FORMAL P1a/P1b/P2/P3 判死族）

| 项 | 值 | 标注 |
|---|---|---|
| 盘上位置 | 同上（**同载体、同算法**，口径同 `P_A_KILL_LINE`） | 【实测】载体在盘 |
| 字节 / mtime | 6,301 B · 2026-09-08 16:03:54 | 【实测】 |
| 盘上实测 SHA-12 | **`d427b2f57c33`** | 【实测】 |
| P_C 登记值 | **不可得** | manifest 缺 |
| 口径外推值 | `d427b2f57c33` | **【推定】** |

> **外推依据**：`03c6c01f3697` 内 `P_A_KILL_LINE` 的 `object` ＝ 「P-A V0 spec §1 GT 判死裁定族」、`path` 同为该 spec 文件、`value` 同为 `bd1caab42b4c` ⇒ **同族内「ECR 基线」与「GT 判死族」两锚**指同一载体、**取同值**。P-C 的 `GT_FORMAL P1a/P1b/P2/P3 判死族` 按 spec §1 亦明载于「本文 §3」⇒ 同载体推定。
> **但**：`P_C_GT_FORMAL_KILLS` 字段面记 `kills={"P1a":true, ...}`，**盘上 0 处可读到 P1a/P1b/P2/P3 的判死登记实体** ⇒ 该锚的**判死族内容面**仍不可核，仅载体可核。

### 锚 3 `P_C_FROZEN_RUNS`（对象＝5 个 frozen run JSON）

**兄弟族 roster【线索】**（`03c6c01f3697` → `P_A_FROZEN_RUNS`，`path` 字段字面 ＝ 「`results/deposon_v20_baselines.json` + v19 + v21 + v18 + v17」，`c00d1c22e7ed` L209 互校一致）：

| roster 位 | 【线索】登记 SHA-12 | 【实测】盘上命中位置 | 【实测】字节 | 【实测】mtime | 判定 |
|---|---|---|---:|---|---|
| 1（v20） | `6edb2aec1660` | `results/deposon_v20_baselines.json` | 16,987 | 2026-08-29 01:17:30 | ✅ **在盘 · 指纹吻合** |
| 2（v19） | `910c4333eead` | `results/deposon_v19_benchmark_fixes.json` | 409,104 | 2026-08-24 01:11:01 | ✅ **在盘 · 指纹吻合** |
| 3（v21） | `9d9ae5001c57` | `results/deposon_v21_gtformal.json` | 69,204 | 2026-08-30 15:44:09 | ✅ **在盘 · 指纹吻合** |
| 4（v18） | `62c1a41e1db8` | `results/deposon_v18_api_supplements.json` | 80,624 | 2026-08-23 23:20:04 | ✅ **在盘 · 指纹吻合** |
| 5（v17） | `af51da229652` | `results/deposon_v17_fusion_fix.json` | 106,164 | 2026-08-23 21:31:41 | ✅ **在盘 · 指纹吻合** |

- **命中方法**：四根目录 **3,574 件全盘 `hashlib` 复算**（含 `deposon-sub` 476 件、`_non_upload_local_archive` 1,458 件、交付包 23 件、2026-09-01 bundle 638 条），以 roster 值反查命中。
- **旁证【实测】**：roster 位 2/3 与该 manifest 内 `KT_B1_V19_BENCHMARK`（path ＝ `results/deposon_v19_benchmark_fixes.json`）、`KT_C1_V21_FROZEN`（path ＝ `results/deposon_v21_gtformal.json`）**路径字面互证**；位 3 值 `9d9ae5001c57` 与 P-C spec §2 字段字面 `runs=["v21_gtformal", ...]` **首项名对上**。
- **重复面【实测】**：`deposon_v20_baselines.json` / `v18_api_supplements.json` / `v17_fusion_fix.json` 各有 2 份同指纹副本（工作区 ＋ `_non_upload_local_archive/results/`）；`v19_benchmark_fixes.json` / `v21_gtformal.json` 各 1 份；另有 `%TEMP%/vfy_sandbox/results/deposon_v20_baselines.json` = `6edb2aec1660` 同指纹第三份。
- ⛔ **本件 0 宣告的**：**0** 不宣告「`P_C_FROZEN_RUNS` 5 锚 0 漂移」—— P_C 自身登记值不可读，**「相对 P_C 登记值」的比对 0 可执行**；上表吻合的是**兄弟族 `P_A_*` 登记值**。
- ⚠️ **一处命名陷阱（如实登记）**：spec §1 记该 5 frozen run 在「`verifier/runs/` 下」；盘上 `verifier/runs/` 实为 57 条 `v10…v35_*.md` **文本 run ＋ log ＋ 1 条 `.jsonl`**（`2026-09-04_pd_v0.jsonl`，100 B），**0 条 roster JSON**。⇒ **spec §1 的目录字面与 roster 实际落位（`results/`）不一致**；roster 的 5 件实际均在 `results/`。本件**只登记该不一致，0 改 spec**。

### 锚 4 `P_C_LLM_CLIENT`（对象＝`tools/llm_client.py`）

| 项 | 值 | 标注 |
|---|---|---|
| 盘上位置 | `tools/llm_client.py` | 【实测】**对象在盘** |
| 字节 / mtime | 8,118 B · **2026-09-09 16:16:02** | 【实测】 |
| 盘上实测 SHA-12 | **`1722500da4aa`** | 【实测】 |
| P_C 登记值 | **不可得** | manifest 缺 |
| ⚠️ 实测观察 | 该件 mtime **2026-09-09 16:16:02 < spec §2 字段声明的 `version=2026-09-11`** | 【实测】**时序倒挂 2 日** |

- **盘上邻近版本【实测】**：`_non_upload_local_archive/.trae/snapshots/p0p1_fix_20260909/tools__llm_client.py` = 5,832 B / **`ea0addb60236`**（另一版，**≠** `1722500da4aa`）。
- **兄弟族登记值 `055e874ea5c1`【线索】**（`03c6c01f3697` → `P_A_LLM_CLIENT`）：**全盘 3,574 件 + bundle 638 条复算 ⇒ 0 命中** ⇒ 该指纹对应的 `llm_client.py` 版本**在盘上不可得**。
- ⇒ **本件 0 宣告**该锚漂移与否（P_C 登记值不可读）；**仅登记**：对象在盘（`1722500da4aa`）、mtime 早于 spec 声明的 version 日期、兄弟族登记值所指的版本盘上 0 副本。

### 锚 5 `P_C_SCALING_PROBE`（对象＝`tools/scaling_probe.py`）—— ⛔ **不可得**

| 检索面 | 检索式 | 结果 |
|---|---|---|
| ① 工作区全树 | 文件名 `*scaling_probe*`；`*scal*` / `*probe*`（70 件命中全为 `probe`/`scaling` 异名件，**0 件** `scaling_probe`） | **0 命中** |
| ① 工作区全树内容面 | 7 件含 `P_C_SCALING_PROBE` / `P_C_V0_anchors` 字面（`b69d65cbb329` / `a8da321b64d2` / `results/_v5_sub_artifact_ledger_history_r2_2026_09_29.md` / `results/_v3_recheck_08_result_2026_09_27.json` / `results/_v3_recheck_08_rescript_2026_09_27.md` / `results/_v3_recheck_08_executor_2026_09_27.py` / `d427b2f57c33` 本身） | **全部为「登记/声明」字面，0 件为文件本体** |
| ② `deposon-sub/` | 同名 + 全树 476 件复算 | **0 命中** |
| ③ `_non_upload_local_archive/` | 同名 + 全树 1,458 件复算 + `backups/`·`.mavis/`·`verify_archive_backup/`·`tmp/`·`.trae/snapshots/` 逐层 | **0 命中** |
| ③b 交付包 | 全树 23 件复算 | **0 命中** |
| ④ 回收站 | `C:\$Recycle.Bin` + `D:\$Recycle.Bin` 逐目录列举 | **0 命中**（唯一 `$I52NDVM` 与本锚 0 关联，且 `$R` 数据体已不在） |
| ⑤ `.tmp/` + `%TEMP%` | 名称 glob + 目录枚举 | **0 命中** |
| ⑥b 2026-09-01 全库快照 | bundle 638 条：目录遍历（`tools/` 仅 2 条 `make_figures*`）＋ **逐成员内容面** 扫 `scaling_probe` / `P_C_V0_anchors` | **0 命中** |
| git 面 | 四根目录 `.git` | **0 `.git`** ⇒ 0 历史可回溯 |

**⇒ 该锚 = 全部检索面 0 命中，登记「不可得」**（非「在盘待核」）。

**最近邻线索（线索 · 非本锚）**：
- `D:/私人资料/deposon-sub/deposon_team/plugins/_p_l_p_c_finite_size_scaling_runner_2026_09_16.py` = 9,177 B / **`bca06b3cc2f7`**；产物 `results/_p_l_p_c_finite_size_scaling_2026_09_16/p_l_p_c_finite_size_scaling_results_2026_09_16.json` = 9,076 B / **`664e7cc05aec`**（工作区 ＋ `deposon-sub` ＋ `_non_upload_local_archive` **三处同指纹**）。
- ⚠️ **该件 0 是本锚**：`a8da321b64d2` L183 已逐字判否（其 N 轴面为 `p_c_36_dang_R2_distribution`，非 spec §3.1 图族规模 N；`elapsed_seconds = 0.005299`；0 逐档原始观测）⇒ **本件仅作「最近邻」登记，0 建议顶替、0 视为找回**。

---

## §4 对 `b69d65cbb329`（08c §3-R-3 表）既有登记的核对

| 08c 登记 | 本 turn 实测 | 判定 |
|---|---|---|
| `verifier/handoff/P_C_V0_anchors_sha256_12.json` **MISSING** | 6 面 ＋ bundle 638 条全 **0 命中** | ✅ **确认** |
| `tools/scaling_probe.py` **MISSING** | 6 面 ＋ bundle 目录 **＋ bundle 逐成员内容面** 全 **0 命中** | ✅ **确认**（并**加强**：08c 未扫 2026-09-01 全库快照，本 turn 已扫，仍 0） |
| `tools/llm_client.py` 在盘但对不上：`1722500da4aa` vs `055e874ea5c1` | `1722500da4aa` 复现 ✅；但**该比对基准的族属需更正** | ⚠️ **部分更正**：`055e874ea5c1` 系 `03c6c01f3697` 内 **`P_A_*` 锚**登记值（`P_A_LLM_CLIENT`），**0 是 P_C 登记值**；且该指纹全盘 **0 命中**（该版 `llm_client.py` 已不可得） |
| 5 个 frozen run JSON **「4/5 缺」** | roster 5 值全盘复算 ⇒ **5/5 对象在盘且逐件指纹吻合** | ❌ **更正**：08c 所猜文件名（`deposon_v17/v18/v19/v21_baselines.json`）**盘上 0 件存在**，故其「缺」结论系**文件名猜错**所致；按 `03c6c01f3697` 登记的 roster 实际落位为 `results/` 下 `v20_baselines` / `v19_benchmark_fixes` / **`v21_gtformal`** / `v18_api_supplements` / `v17_fusion_fix`，**5 件全在**。⚠️ 该更正**只改「对象在否」，不改「P_C 登记值不可读 ⇒ 漂移不可判」** |

> **⛔ 本棒 0 做的**：0 改 `b69d65cbb329` / `a8da321b64d2` / `03c6c01f3697` / `c00d1c22e7ed` / `d427b2f57c33` 任一字节（**全只读**）；0 落任何新 manifest（**自算 ＝ 重定义锚集**）；0 把 `P_A_*` 登记值登记成 `P_C_*` 登记值；0 从载体反推 P_C 登记值并宣告 0 漂移；0 恢复任何回收站件；0 网络自取。

---

## §5 影响面（**哪些面因此不可验**）

| 面 | 状态 | 依据 |
|---|---|---|
| **R-3「spec §2 五锚可验」整体** | ⛔ **仍不可判** | 「可验」三要件 ＝ ①有 P_C 登记值 ②对象在盘 ③复算吻合。**①缺**（manifest 不可得）⇒ 三要件 0 满足 ⇒ R-3 维持「✗ 未满足」，但**维持理由须由 08c 的「对象消失」更正为「登记值载体不可得 ＋ 1/5 对象不可得」** |
| **spec §8 L119「5 锚漂移 ≥ 1 → 全 V0 撤回」** | ⛔ **判据不可执行** | 无 P_C 登记值 ⇒ 「漂移」量 0 可定义 |
| **spec §6 L104–L109 复现协议** | ⛔ **第 2 步即断** | L107 字面「读 `verifier/handoff/P_C_V0_anchors_sha256_12.json` 验 5 锚」⇒ 首步即 0 文件 |
| **锚 1 / 2（ECR 基线 / GT 判死族）** | ⚠️ **载体在盘、口径可推定、登记值不可判** | §3 锚 1 / 锚 2 |
| **锚 3（5 frozen run）** | ✅ **对象 5/5 在盘**（`03c6c01f3697` roster 逐件吻合）**；P_C 登记值不可判** | §3 锚 3 |
| **锚 4（`llm_client.py`）** | ✅ **对象在盘**（`1722500da4aa`）；⚠️ mtime 早于 spec 声明 `version` 日期 2 日；P_C 登记值不可判 | §3 锚 4 |
| **锚 5（`scaling_probe.py`）** | ⛔ **对象不可得 ＋ 登记值不可得** ⇒ **该锚完全不可验** | §3 锚 5 |
| **P-C V0 执行面（连带）** | ⛔ **盘上 0 执行痕迹** | `results/v3x_pc_v0/`（spec §7 交付路径）**MISSING**；`docs/V3X/P_C_V0_RESULTS_2026_09_09_mavis.md`（spec §7 D5 交付件）**MISSING**；`tools/scaling_probe.py`（spec §10 D2 交付物）**MISSING**；manifest（spec §10 D1 交付物）**MISSING** |

### §5.1 根因线索（**根因推断 · 非实测 · 判定权在 PI**）

> **诚实纪律（不误导）**：本节**不**宣告「文件丢失 / 锚漂移」。盘上证据**更支持另一读法**：
> 1. `d427b2f57c33` §10 时间线字面：**D1 ＝「pilot n=20 锁相变点 + 出本 spec final + **5 锚预登记**」**（派给 v3x + successor）；**D2 ＝「**实现 scaling_probe** + 7 档 N × 10 任务 harness」**（派给 data）。
> 2. §1 字面：`tools/scaling_probe.py`「（**D1 由 data 实现**）」⇒ **spec 自记该件本应是待实现产物**。
> 3. **D1 与 D2 两侧交付物（manifest ＋ scaling_probe）均不在盘**；D3–D5 执行/报告交付面（`results/v3x_pc_v0/`、D5 报告）**亦全不在盘**。
> 4. 对照：同族 P-A 的 5 锚 manifest **已于 2026-09-09 建成**（`03c6c01f3697`），且 `c00d1c22e7ed` L160–L169「0 触动 frozen 文件清单」把 P_C spec 与 P_A/P_B/P_D/P_E/P_F spec **并列**登记，但 **P_C 唯独 0 独立 manifest**。
> ⇒ **「P-C V0 在盘上从未执行」** 这一读法，与全部实测一致；而「5 锚漂移 ≥ 1 → 全 V0 撤回」的**触发前提**（V0 已执行且有可复算登记值）**在盘上 0 证据支持**。
> ⚠️ **本件 0 代裁**：R-3 二择一（**(a)** 找回 ＋ 沿 §6 复验 / **(b)** 判「V0 5 锚永久不可验」⇒ 沿 §8 撤回）**仍属 PI 拍板**（沿 `b69d65cbb329` §5 待拍板表第 3 行）。本件新增的输入是：**(a) 路径已穷尽且 `scaling_probe.py` 全面 0 命中**；**(b) 的根因读法可能是「未执行」而非「漂移」**——若采 (b)，撤回**对象**本身（未执行的 V0）需 PI 重新界定。
> ⛔ **本件 0 做**：0 宣告 R-3 已满足 / 已不可满足；0 代 PI 择一；0 起草 (a)(b) 任一处置面。

---

## §6 诚实边界（本件 0 做清单）

| # | 边界 | 状态 |
|---|---|---|
| 1 | 0 改任何既有件 | ✅ 全程只读（`read` / `grep` / 只读枚举 / 只读 `hashlib`） |
| 2 | 0 恢复 / 0 移动 / 0 删除 | ✅ 回收站**仅读元数据**；**0 写任何既有目录** |
| 3 | 0 编造路径或指纹 | ✅ 全文**【实测】/【线索】/【推定】** 三级标注；无登记值处一律写「不可得」 |
| 4 | 0 自算 manifest | ✅ 本件 0 落任何新 manifest（自算 ＝ 重定义锚集 ＝ 重基线） |
| 5 | 0 跨族顶替 | ✅ `P_A_*` 登记值**仅**用作全盘复算的检索靶，**0 登记为 P_C 登记值**、0 据其宣告漂移 |
| 6 | R4 key 永不明文 | ✅ **0 读取 key、0 落盘、0 入 prompt / JSON / log**（本 turn 0 触任何 key 路径） |
| 7 | 0 恢复 bundle 落盘 | ✅ 2026-09-01 全库快照**纯内存** base64 + `zipfile` 解码，**0 写盘** |
| 8 | 0 网络自取 | ✅ 全程本地只读 |

**遗留未覆盖**：① `C:` / `D:` 全盘**非 deposon 相关**目录未逐件扫（本 turn 仅扫 `D:/私人资料/` 4 根 ＋ 回收站 ＋ `%TEMP%` ＋ 2026-09-01 bundle）；② 无 git 历史、无云端备份、无离线介质面（**PI 持有面**）0 可触及；③ `E:` 及其他盘符**未探**（盘上未见该盘符线索，0 编造其存在）。

---

**出证**：worker（mavis_31052a118b3940718ef9fbfafa01e5e9）· 2026-09-29 · 只读追源 · **0 恢复 0 改 0 移 0 自算 manifest**
