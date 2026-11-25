# V3-11 登记件：4-worker → 9-model 全量 JSON 合并（执行面落盘）

> **棒身份**：worker（分支棒 · session `mvs_c31100d24e8b4e3cb1849e7b70973c11`）
> **授权锚**：PI 2026-10-09 卷⑨问卷 `ask_cfb9284519a5abf29d0f03eb` Q1「五段全开·批准后当日即办」＋「①②③④⑤按顺序」
> **缺口母件**：`results/_v34_experiment_gap_plan_2026_10_08.md`（`996feb1db9cb`）§1.1 V3-11 行 ＋ §2.2 W5 行（验收字面逐字为准）
> **执行时点**：2026-10-09 GMT+8
> **本件性质**：登记件（新建）＋ 合并件（新建）；**0 回改任何既有件**

---

## §0 母件验收字面 vs 本棒执行口径（**存疑已判读·非停手项**）

母件同一行内并存两条字面：

- **§1.1 V3-11 行「缺口内容」**：`4-worker → 9-model 全量 JSON 合并`；「残余面」＝`其余 3 worker 件`；「判定链」＝`worker（须重派）`
- **§2.2 W5 行「验收」列**：`每件留痕 ＋ **0 合并派生 JSON** ＋ D+0.5 出具真伪结论`
- **§2.2 W5 行「产出」列**：`… ＋ **9-model 合并** ＋ …`

**判读结论（依仓内既有件与交接件文义，非自创）**：

「派生 JSON 不合并」在仓内是一致口径的**铁律**，其文义为「**0 并入既有件、0 覆写既有件，产出落新名独立件**」，**非**「0 产出合并类 JSON」。逐条佐证（同一措辞、同一含义）：

| 既有件 | 字面 |
|---|---|
| `deposon_team/plugins/_v5_item35_v3_collinear_2026_09_29.py:30` | 「派生 JSON 0 合并：**写新名独立件** `results/_v5_item35_v3_collinear_result_2026_09_29.json`」 |
| `deposon_team/plugins/_v5_item35_v2_matrix_2026_09_29.py:21-22` | 「派生 JSON 0 合并：写新名独立件 …，**0 并入** `deposon_v20_gt2b.json` 或任何 `_v3_*` / `_v5_*` 既有件」 |
| `deposon_team/plugins/_v5_item21_strategyqa_realias_2026_09_29.py:8` | 「产出落**新名件**；派生 JSON **0 合并**；既有结果 JSON **0 覆写、0 改写**」 |
| `letters/_v3_calibration_change_note_for_coze_glm_2026_09_27.md:310` | 「**不得擅自重算或合并派生 JSON**（沿 R5 frozen 派生 JSON 不合并铁律）」 |

⇒ 故 V3-11 之「9-model 合并」**当且仅当**落为**新名独立件**、对既有件**0 字节动作**时成立。**本棒即按此执行**（见 §2「0 回改确认」）。此判读**不构成**对既有 5 件结果 JSON 的任何改写，亦**不代裁**母件字面冲突（若 PI 认定 W5 验收列应作他义，本件降级为「候呈·仅装配面」，数据面不受影响）。

---

## §1 并入面逐项态（4 worker → 9-model 覆盖面）

**名册来源（非自创）**：`verifier/run_volcengine_9model_30cells.py` L38-48 之 `MODELS` 字面量 ＋ `results/deposon_volcengine_9model_30cells_2026_09_10.json` 之 `models[]` 顺序 —— **两集合实测一致（脚本内 assert）**，名册顺序沿基线件。

**基线件缺口**：基线 9-model 主跑（`58ab335ca341`）**PARTIAL**，仅 `doubao-seed-2.0-lite` 1 model COMPLETE（26/30），其余 8 model 为 0/30 或 17/30 未跑完。**4 worker × 2 model ＝ 8 model，与基线 8 个未完成槽位逐一对应、无重叠、无遗漏。**

| # | Model | T | (GSM8K+SQA) | cells | pass_rate_30 | 供数源 | 母件残余面 |
|---:|---|---:|---|---:|---:|---|---|
| 1 | `doubao-seed-2.0-lite` | 26 | 14+12 | 30 | 0.8667 | **基线主跑**（9model COMPLETE） | — |
| 2 | `kimi-k2.7-code` | 19 | 10+9 | 30 | 0.6333 | worker_a | 其余 3 worker 件之一 |
| 3 | `minimax-m3` | 21 | 12+9 | 30 | 0.7 | worker_a | 其余 3 worker 件之一 |
| 4 | `doubao-seed-2.1-turbo` | 18 | 9+9 | 30 | 0.6 | worker_b | 其余 3 worker 件之一 |
| 5 | `deepseek-v4-flash` | 23 | 12+11 | 30 | 0.7667 | worker_b | 其余 3 worker 件之一 |
| 6 | **`glm-5.3`** | **26** | 14+12 | 30 | 0.8667 | **worker_c**（V3-11 判定链本体） | — |
| 7 | **`doubao-seed-evolving`** | 22 | 12+10 | 30 | 0.7333 | **worker_c** | — |
| 8 | `glm-5.3-flash` | 21 | 13+8 | 30 | 0.7 | worker_d | 其余 3 worker 件之一 |
| 9 | `deepseek-v4-pro` | 16 | 7+9 | 30 | 0.5333 | worker_d | 其余 3 worker 件之一 |

**覆盖面**：名册 9 槽 **9/9 实填**（`all_slots_filled: true`）；4 worker 全部贡献（`workers_contributing: [worker_a, worker_b, worker_c, worker_d]`）；**9 model 全部 30 cells 达成**（`all_models_30_cells: true`）；`sum_total_passed` ＝ **192**。

**母件 V3-11 判定链「worker_c 已并入否」之答**：**已并入** —— `glm-5.3`(26/30) ＋ `doubao-seed-evolving`(22/30) 二 model 均入合并件，`source_worker_id = "C"`，源件 `f6f172820c97` 可对位。

**交叉核验（逐 model，per-cell 实测 ＝ 声明值）**：9/9 全 PASS。核验法按源件各自 schema 分别取值（**未编造统一 schema**）：

| 源 | per-cell 判据字段 | 复算 passed | ＝ 声明 total |
|---|---|---:|---|
| worker_a | `detailed[model].gsm8k/strategyqa[].passed`（顶层 `detailed`，非 `models[].cells`） | 19 / 21 | ✅ |
| worker_b | `models[].cells[].is_correct` | 18 / 23 | ✅ |
| worker_c | `models[].cells[].is_correct` | 26 / 22 | ✅ |
| worker_d | `models[].cells[].passed` | 21 / 16 | ✅ |

**分母口径**：worker_a 源件**无** `gsm8k_attempted` / `cells_done` 字段 ⇒ 合并件内 `attempted_basis = "derived_from_per_cell_rowcount_in_source"`，15/15 由 `detailed` 逐格条数**实测导出**（非假定）；其余 3 worker 沿源件声明（`declared_in_source`）。源件**未声明** `status` 者（worker_a/d），合并件 `status = null` 且 `status_declared_by_source: false` —— **0 代源件补写**。

---

## §2 0 回改确认

**既有件 0 字节动作**，落盘后实测（`Get-FileHash -Algorithm SHA256` ＋ `(Get-Item).Length`）：

| 源件 | SHA-12 | 状态 |
|---|---|---|
| `results/deposon_volcengine_9model_30cells_2026_09_10.json` | `58ab335ca341` | **UNCHANGED**（4,894 B） |
| `results/deposon_volcengine_worker_a_2026_09_10.json` | `506810017d34` | **UNCHANGED**（25,464 B） |
| `results/deposon_volcengine_worker_b_2026_09_10.json` | `b1eb668377ce` | **UNCHANGED**（49,338 B） |
| `results/deposon_volcengine_worker_c_2026_09_10.json` | `f6f172820c97` | **UNCHANGED**（51,716 B，母件锚值一致） |
| `results/deposon_volcengine_worker_d_2026_09_10.json` | `fae79888344b` | **UNCHANGED**（20,280 B） |
| `results/deposon_volcengine_minimax_m3_30cells_2026_09_10.json` | `fbb7677b9cd5` | **UNCHANGED**（23,472 B） |

5 worker/基线件 mtime 均仍为 `2026/9/16 11:01:12`（未被我方触碰）。

**新建件（本棒 2 件）**：

| 件 | 路径 | SHA-12 | bytes |
|---|---|---|---:|
| 合并件 | `results/_9model_full_merge_from_4workers_2026_10_09.json` | `32aa0618a9d7` | 19,337 |
| 登记件（本件） | `results/_9model_merge_disposition_register_2026_10_09.md` | 见文末自报 | — |
| 装配器（可复跑） | `.tmp/_w5_9model_merge_2026_10_09.py` | — | — |

**落前检查**：两目标件 `Test-Path` 均 `False`；`*9model*merge*` glob 0 命中既有件 ⇒ **0 撞名覆写**。

**命名合规**：沿 PI 2026-10-09 命名裁 `57024f2cd30a`（「去版本前缀 `_主题_日期`，不再带 V-阶段字样」）—— 两件名均**无** `_v5_` / `_v4_` / `_v3_` 等阶段前缀。

---

## §3 自查

| 铁律 | 自证 |
|---|---|
| **0 编造** | 全部数字均自 5 件源件 `json.load` 实测复算，并与 per-cell 逐格交叉核验（9/9 PASS）；0 外部知识填充 |
| **0 代裁** | 0 代 verdict-keeper / protocol-keeper / evidence-auditor / doc-writer 任何判定；存疑项（见 §4）如实呈报不自行了断 |
| **0 新 LLM / 0 端点调用** | 装配器为纯 `json.load` 读取面；全脚本无 `requests` / `openai` / `http` / 端点 URL 调用 ⇒ 本棒**0 需新凭据**（通道/额度问题不触发） |
| **R4 key 永不明文** | 合并件 `auth` 字段 0 传播源件 key 尾部片段（实测 `'e219'` 计数 **0**）；仅留 `ark-[REDACTED]...` 与「key loaded from env at runtime」字面 |
| **UTF-8 无 BOM · LF** | 实测 `BOM: False`、`CRLF: 0`、`LF: 613` |
| **派生 JSON 不合并** | 合并件落**新名独立件**；对既有 5 源件 **0 覆写 / 0 并入**（§2 实测） |
| **覆盖面明示，0 声称全链** | 覆盖面＝「9 名册 × 30 cells 全填」；**0 声称**本合并等于单一受控协议全链（见 §4 协议异质性） |

---

## §4 遗留 / 候呈项（**如实登记·0 自行处置**）

**（1）协议异质性 — 合并件为「覆盖面并集」，非单一受控协议跑**

5 源件运行参数互不相同，合并件为**跨协议并集**：

| 源 | max_tokens | timeout_s | temperature |
|---|---:|---:|---:|
| 基线主跑 | 2048 | 60 | 0.0 |
| worker_a | 1024 | 30 | *（源件无该字段）* |
| worker_b | 1024 | 30 | 0.0 |
| worker_c | 1024 | 30 | 0.0 |
| **worker_d** | **512** | **15** | 0.0 |

**仅登记的共存事实（0 归因、0 改判）**：worker_d 以最紧预算（512 tokens / 15 s）实跑，其 `deepseek-v4-pro` 为 9 model 中 `total_passed` 最低者（16/30）。此共存关系**是否构成截断效应，属判定面，不在本棒权限**；母件 V3-11 判定链仅问「worker_c 已并入否」，故本棒**只登记不归因**。

**（2）`minimax-m3` 三源并存，标注不自洽 — 候呈 PI / verdict-keeper**

| 读数 | 值 | 源件 |
|---|---|---|
| 本合并件采用 | **21/30（0.700）** | `worker_a`（V3-11 合并面＝4 worker 件） |
| 并行读数（未并入） | **22/30（0.7333）** | `deposon_volcengine_minimax_m3_30cells_2026_09_10.json`（**非** 4 worker 之一） |

**且存在既有件标注不自洽（如实登记，0 回改）**：`docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` §2.1 与 `docs/V3X/P_F_IMPLEMENTATION_2026_09_11.md` §2.1 均以 `source = "minimax-m3_standalone"` 标注 `minimax-m3` 且记 `T=21 / T_frac=0.700`；然该 standalone 件**自身载 `total_passed=22 / 0.7333`** ⇒ 标注源与所载数值**不自洽**（21 与 worker_a 符，与 standalone 件 22 不符）。

⇒ 本合并件按母件「残余面＝其余 3 worker 件」取 worker_a 值（21），standalone 值并列登记不并入。**取何值为 PI / verdict-keeper 权限，本棒 0 代裁**；既有 V7 / P-F 报告 0 触动。

**（3）母件 W5「验收」列字面冲突 — 候呈**（判读见 §0；本棒按「新名独立件」义执行，若 PI 采他义则本件降级为候呈）

**（4）`EMBEDDING_VISION_V1_IMPL_2026_09_10.md` §2.2 不可得**：既有 V7 / P-F 两报告均以该件 §2.2 为 9-model 数据**上游出处**，然该件**在主仓 0 命中**（glob 0 匹配）。本棒 0 推定其内容，合并件**改以 4 worker 件 ＋ 基线件为直接供数源**（每 model 均带 `source_path` ＋ `source_sha12` 可对位）。该件是否落归档区，**属「0 命中 ≠ 不存在」面，本棒 0 断言其不存在**。

---

## §5 复算自报（落盘后实测）

```
合并件 results/_9model_full_merge_from_4workers_2026_10_09.json
  SHA-256 : 32aa0618a9d712569c665b7f24f4d24c883ccfbdc10f9c7529a861e51f4730eb
  SHA-12  : 32aa0618a9d7
  bytes   : 19337
  BOM     : False   CRLF: 0   LF: 613   （UTF-8 无 BOM · LF）
  R4 scan : 'e219'=0  'Bearer'=0  'sk-'=0  'api_key'=0  'ark-'=1（[REDACTED] 字面）
```

登记件（本件）SHA-12 与 bytes 由本棒在 handoff 回执中给出（自指文件，落盘即定值；外部观测者请以 `Get-FileHash -Algorithm SHA256` 独立复算）。

---

**登记件完 · 出证：worker（分支棒）· 0 编造 / 0 代裁 / 0 回改既有件 / 0 网络 / 0 新 LLM 调用**