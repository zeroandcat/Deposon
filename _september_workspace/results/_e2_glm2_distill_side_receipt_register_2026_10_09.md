# E2 · GLM_2 蒸馏侧 round1 收官态 · 回执面复查登记（晨间波次 U6）

**件类**：evidence-auditor 回执面复查登记（新建登记件 · 0 回改既有件）
**时点**：2026-10-09 上午（晨间波次 U6）
**审计对象**：后台任务 `bg_bb13016d`（旧登记记 09-26 16:18 · lost）声明主题「GLM_2 distill 侧 round1」
**上游件**：
- 排期件 `results/_v34_experiment_gap_plan_2026_10_08.md`（`996feb1db9cb`）V4-15 行
- 处置棒件 `results/_receipt_disposition_register_2026_10_08.md`（`a79c3b82ee01`）§2.2 末注（U6 未列入派单 · 该棒 0 动作）
- 旧查登记 `results/_forgotten_recovery_register_2026_10_08.md`（§2.5 E2 行 · U6 挂账行）

---

## §0 结论摘要

**判定：有新证 · GLM_2 蒸馏侧收官态「可证」，且旧登记的锚件族认定有误。**

旧登记（§2.5 E2）载「未检出 `batch7_r5` 之外 GLM_2 侧独立产物名 ⇒ 收官态无回执可证」。本次独立复查发现该结论的**锚件族锚错**：

| 项 | 旧登记认定 | 本次实测认定 | 依据 |
|---|---|---|---|
| GLM_1 侧收官族 | `batch7_r5` | `batch7_r5`（维持） | 该族 executor 字面自述为 GLM_1 distill 侧 |
| GLM_2 侧产物族 | 「未检出独立产物名」 | **`batch8_r1`–`r5`（10 件，全族在盘）** | `batch8_r5_executor.py:6,30,35` 字面自述「GLM_2 蒸馏侧收官棒」 |
| GLM_2 侧收官态 | 无回执可证 | **已达成：22 caption × 5 calls = 110 calls，5/5 收官** | `batch8_r5_result.json` → `glm2_distill_side_finish` |

**关键**：GLM_2 侧并非「无产物」，而是旧查以 `batch7` 族为锚检索时，漏检了同目录下 `batch8` 族（两族同前缀、同日期邻接 09-25 02:13–03:37）。

**⛔ 本件不判实验结论本体**（收官态读数属 worker/verdict-keeper 域），仅就「回执/产物面是否存在且自洽」作证据链判定。

---

## §1 多式检索表（逐项 0 命中 / 命中）

### §1.1 回执面（运行时 background-tasks，只读）

| # | 检索式 | 范围 | 命中 | 判定 |
|---|---|---|---|---|
| R1 | 目录名前缀 `bg_bb13016d*` | `C:\Users\Administrator\.minimax\background-tasks\`（全量 **22,211** 个 `bg_*` 目录） | **0** | 回执目录不存在（与旧登记「lost · 目录不在 background-tasks」**一致**，非新证） |
| R2 | 目录名前缀族 `bg_bb*` | 同上 | 96 | 族内无 `bg_bb13016d`（短 ID 为 8 位 hex 全前缀，形态须为 `bg_bb13016d-<uuid>`） |
| R3 | 时间窗枚举（09-26 16:00–16:40） | 同上 | **112** 个目录 | 窗口内 112 件各有 `output.log` + `summary.txt`（字节数 5 B–70,397 B 不等），**无一件对应 GLM_2 蒸馏侧**；亦无短 ID 命中 |

> **回执面结论**：`bg_bb13016d` 回执目录**确认不存在** ⇒ 回执**内容**不可判（沿 R5 只登记不翻案）。但产物面**可判**（见 §1.2）——回执缺失 ≠ 产物缺失，二者分离登记。

### §1.2 名面 · GLM_2 侧产物（主仓 / deposon-sub / 归档区 三面）

| # | 检索式 | 主仓 `deposon-repo` | `deposon-sub` | 归档区 `_non_upload_local_archive` |
|---|---|---|---|---|
| N1 | `*glm*2*` | 16 | 12 | 20 |
| N2 | `*glm2*` | **0** | **0** | **0** |
| N3 | `*glm_2*` | 5 | 0 | 6 |
| N4 | `*l14v3*` | **126** | **0** | 16 |

**N1/N3 命中逐件判读（均为「非 GLM_2 蒸馏侧 round1 产物」）**：
- `corpus/v20/by_model/GLM_2/glm_artifact_v_2026_09_16.json`（`39732a92b5c9`）→ corpus 静态件，09-16，**非** 09-25 蒸馏侧
- 归档区 `_v4_supp_l7_e_n20_*_GLM_2_b{0,10,20}` 共 6 件（09-24）→ 属 **L7·E·N=20** 线（非 L14+ 蒸馏侧），时间早 1 日
- `letters/*` 共 11 件 → 委托函面，与产物面无关
- `results/deposon_volcengine_glm_*` 共 4 件（09-16）→ V3 火山引擎面，非本线

**N4 命中关键增量**：`l14v3` 族在主仓 126 件，含 `batch8_r1`–`r5` 全 10 件（09-25 02:21–03:37）。

### §1.3 名面 · `batch8` 族（GLM_2 蒸馏侧，本条为决定性命中）

| 文件 | mtime | 字节 | SHA-12（本次实测 `Get-FileHash -Algorithm SHA256`） |
|---|---|---|---|
| `_v4_supp_l14v3_batch8_r1_executor.py` | 09-25 02:21 | 56,181 | `1e5f2249c517` |
| `_v4_supp_l14v3_batch8_r1_result.json` | 09-25 02:21 | 62,531 | `e6a94a0a13b7` |
| `_v4_supp_l14v3_batch8_r2_executor.py` | 09-25 02:35 | 57,634 | `6a9bbc43c808` |
| `_v4_supp_l14v3_batch8_r2_result.json` | 09-25 02:36 | 63,440 | `7b23996b5f4c` |
| `_v4_supp_l14v3_batch8_r3_executor.py` | 09-25 02:50 | 58,494 | `0f654d945f12` |
| `_v4_supp_l14v3_batch8_r3_result.json` | 09-25 03:00 | 63,670 | `56faf9324fba` |
| `_v4_supp_l14v3_batch8_r4_executor.py` | 09-25 03:13 | 59,351 | `6b69ec8406d4` |
| `_v4_supp_l14v3_batch8_r4_result.json` | 09-25 03:18 | 64,038 | `c7d5aa2a9b00` |
| **`_v4_supp_l14v3_batch8_r5_executor.py`** | 09-25 03:32 | 60,475 | `6961281824ae` |
| **`_v4_supp_l14v3_batch8_r5_result.json`** | 09-25 03:37 | 63,785 | `3620a7daf9c1` |

> 前缀链自洽性核验（引自后棒 executor 字面）：`batch10_r1_executor.py:47` 明载「**batch8 r5 GLM_2 distill 收官（最新 cross-batch cumulative baseline）**」，并以其 SHA-12 `3620a7daf9c1`／`6961281824ae` 为锚 —— **与本次实测值逐字一致（MATCH）**。

### §1.4 时间窗面（主仓 `results/` 09-26 15:30–17:30）

窗口内 25 件，含 `batch9`（coze 蒸馏侧，16:32–17:34）、`batch10`（minimax 蒸馏侧，16:32–17:46）、`t15r2` 三族。
- `batch9_r1_executor.py:6` 字面：「**coze** 蒸馏侧开工棒」
- `batch10_r1_executor.py:6` 字面：「**minimax** 蒸馏侧第一棒」
- ⇒ 09-26 16:18 时间窗对应的是 **coze / minimax** 两侧派工，**非 GLM_2**。

**⛔ 时间戳口径声明**：旧登记将 `bg_bb13016d` 结束时间记为 **09-26 16:18**；但 GLM_2 侧产物落盘时间为 **09-25 02:21–03:37**（早约 13 小时）。二者**不一致**。本件如实登记该矛盾，**不改写旧登记行**（R5 只追加），矛盾成因（任务 ID 归属误记 vs 时刻记错）**留待 parent/PI 判**。

### §1.5 内容面 · GLM_2 侧自述字面（决定性证据链）

`_v4_supp_l14v3_batch8_r5_executor.py`（1,188 行）关键行：

| 行号 | 字面（摘） |
|---|---|
| L6 | `V4 L14+ batch 8 · round 5（reask=4）—— GLM_2 蒸馏侧 **收官棒**（沿 r4 口径全套）` |
| L18 | 沿 `_v4_supp_l14v3_batch8_r1_result.json`（SHA-12 `e6a94a0a13b7`）口径续跑（**GLM_2 蒸馏侧 round 1** 22/22 caption ≥1 successful 开工达成） |
| L25–26 | GLM_2 = teamo `glm-5.3` 复用；PI 拍板字面「GLM_1/GLM_2 same lineage」「同 model 不同语料」 |
| L35–37 | 目标 = GLM_2 蒸馏侧 round 5 ≥5 successful call/caption（**收官**）；由 4/5 补至 5/5 |
| L40–41 | `teacher_label` = `GLM_2`；`model_id_shared_with` = `GLM_1` |
| L45 | 收官判定块 `glm2_distill_side_finish` |

`_v4_supp_l14v3_batch8_r5_result.json` → `glm2_distill_side_finish` 实测读数：

```json
{"all_22_captions_met_target": true,
 "finish_disposition": "GLM_2 蒸馏侧全 22 caption 5/5 successful 达标 → batch8 蒸馏侧收官 ✓",
 "glm2_distill_side_target_met_at_round": "r5",
 "met_count_post_r5": 22, "rounds_to_reach_target": 5,
 "rounds_to_reach_target_actual": "5 棒 (r1+r2+r3+r4+r5) = 22 caption × 5 calls = 110 GLM_2 蒸馏侧 calls",
 "still_pending": [], "total_captions": 22}
```

同件 `per_caption_glm2_distill_only_successful_calls` 逐 caption 抽样（5/22，均 `met_target: true` / `succ_count: 5` / `need_more_to_final: 0`）：
`L_algorithm_process`｜`L_biological_taxonomy`｜`L_geography_world`｜`L_historical_causality`｜`L_physics_concepts`｜`L_project_management` …

---

## §2 幽灵引用对账（三分支判定）

| 分支 | 适用项 | 判定 |
|---|---|---|
| **FOUND_IN_REPO** | `batch8_r1`–`r5` 全 10 件（GLM_2 蒸馏侧产物） | ✅ 在盘，指纹齐备；`batch8_r5` 双件被后棒 `batch10_r1` 字面锚定且哈希 MATCH |
| **MISSING_TRUE** | `bg_bb13016d` 回执目录（`background-tasks\bg_bb13016d*`） | ⚠ 回执面三处（任务目录 / 22,211 目录枚举 / 09-26 16:00–16:40 窗口）均无 ⇒ **真缺件**，不造来源 |
| **MISSING_TRUE** | GLM_2 侧 `run.log` 类日志 | ⚠ 沿 U9 族登记（`_v4_supp_l14v3_batch7_r5_run.log` 三面全 0）；本棒**未见** GLM_2 侧 run.log 名，**不推定其应有**（0 证据不编造） |
| SAME_IDENTITY | 归档区 `_remote_version_freeze_2026_09_26/` 内 `_v4_supp_l14v3_batch8_r5_*` | ⚠ 该面无 batch8_r5（仅 batch10_r5 / batch2–5 / batch9_r5 / mapping / verdict / prereg 共 16 件）⇒ **无同一性重复**，不计 |
| CONFLICT | — | **0 件**（未检出同名异哈希） |

---

## §3 资产缺陷登记（只登记 · 不代修）

| # | 缺陷 | 位置 | 处置 |
|---|---|---|---|
| D-1 | 引用路径规范 | `batch10_r1_executor.py:47` 引「batch8 r5 GLM_2 distill 收官」为**裸文件名**（无 `results/` 前缀） | 登记，不代修（属 frozen 内 executor 缺陷面） |
| D-2 | 时间戳矛盾 | 旧登记 E2 行记 `bg_bb13016d` 结束 09-26 16:18；GLM_2 侧产物落盘 09-25 02:21–03:37 | 登记矛盾，留 parent/PI 判；**0 回改旧登记行** |
| D-3 | 锚件族误锚（根因） | 旧登记以 `batch7_r5` 为 GLM_2 侧锚；实测 `batch7` 族 executor 字面自述为 **GLM_1 蒸馏侧**，GLM_2 侧为 `batch8` 族 | 登记为**旧查检索口径缺陷**（同前缀邻接族漏检），非产物缺陷 |

---

## §4 候 PI 项

| # | 事项 | 建议处置 | 备注 |
|---|---|---|---|
| **P-1** | **须重跑才可收官？—— 否。** | **无需重跑。** GLM_2 蒸馏侧 round1–round5 全链产物在盘、收官读数自洽（22/22 caption 5/5、110 calls、`still_pending: []`） | 本项仅回执/证据链判定；收官**读数本身**的实验有效性属 worker/verdict-keeper 域，本件不越界判 |
| **P-2** | 旧登记 E2 行「无回执可证」结论的勘误 | 候 parent 决定是否在 `_forgotten_recovery_register_2026_10_08.md` 追加勘误节（**本件 0 回改**），并销 U6 挂账 | 建议措辞：「回执内容不可判（目录不存在）；产物面可证，GLM_2 侧收官族为 `batch8_r5`（`3620a7daf9c1`／63,785 B），旧查锚件族误锚为 `batch7_r5`」 |
| **P-3** | D-2 时间戳矛盾归因 | 候 parent 判：任务 ID 归属误记 / 旧查时刻记错 / 二者皆有 | 本件不自行取舍 |
| **P-4** | 回执目录真缺件（lost 根因） | 沿 §2.5 组 E 族统一归因（`Local runtime restarted before …`），**0 单独派工** | 与 E1/E3/E4/E5 同族 |

---

## §5 自证

- **0 触动**：本次仅**新建本件**，⛔ 0 回改任何既有件；⛔ 0 触 frozen（18 frozen / 9 网格 / V4 frozen 产物链）；⛔ 0 网络；⛔ 0 skill 调用；⛔ 0 读 key/`.env`（R4）。
- **哈希口径**：`Get-FileHash -Algorithm SHA256`（stdlib Get-FileHash，**禁内建 `hash()`**），SHA-12 取 hex 前 12 位小写。
- **0 产物不编造**：R1/R2/R3 的 0 命中如实登记；GLM_2 侧 `run.log` 未见即写「不推定其应有」。
- **边界**：不跑实验、不出实验判定、不改实验结论本体（审计 ≠ 翻案）。

---

## §6 本件指纹（落盘后实测）

见回执回报（本件 SHA-12 与字节随回执给出）。