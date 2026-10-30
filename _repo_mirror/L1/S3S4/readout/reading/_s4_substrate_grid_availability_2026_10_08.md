# S4 substrate 分格可得样本数预报（T-5 开跑前置 · 计数/可用性盘点）

- **件性质**：**计数与可用性预报告**（counting / availability pre-report）· **0 判定 · 0 档位 · 0 赋布尔**
- **触发**：PI 2026-10-08 令「排期实验缺口并全量补实验」；《V3~V4 实验缺口排期》§3 第一波开跑单之 **OR-2**
- **派工单**：`results/_v34_experiment_gap_plan_2026_10_08.md` ＝ `996FEB1DB9CB`／36,066 B（**本棒实测**）
- **本件**：`results/_s4_substrate_grid_availability_2026_10_08.md` ＋ `results/_s4_substrate_grid_availability_2026_10_08.json`（**另起名·0 覆写**；落前撞名实测见 §8）
- **出件**：**worker**（Mavis 团队 worker · session `mvs_18a8b3d1c78a4609a00288da177cc96d`｜**署名如实**）
- **日期**：2026-10-08
- **runtime**：纯本机读写；**0 网络 / 0 端点调用 / 0 API key**（R4 永不明文 / 0 读 key / 0 读 `.env`）

---

## §0 本件性质与权限边界（**先读此节**）

> **本件 ＝ 「每格可得样本数」之开跑前预报（T-5 之 T-5 前置件）**，即 **计数与可达性上界**。
> **⛔ 0 判 `K-V3S-4-1/2/3` 任一线**；**⛔ 0 宣告 S4 段可开跑**；**⛔ 0 落 held-out 集**。

| 边界 | 内容 |
|---|---|
| **本棒行使** | **计数面**：逐格可得样本数 · 空格面 · 每格 n 分布 · held-out 静态可达上界 · `P-S4-1` 自洽性算术账 |
| **本棒 0 行使** | ⛔ **档位/布尔** ＝ verdict-keeper 面 ｜ ⛔ **代裁 `P-S4-1`** ＝ PI 面 ｜ ⛔ **抽样器与 held-out 集生成** ＝ S4 执行波 ｜ ⛔ **S4 substrate 冻结**（本件 0 冻结任何清单） |
| **4-2 冻结态** | ⚠️ **`K-V3S-4-2` ⛔ 未冻**（源件自标 `status = "unfrozen_pending_PI"`，`ef5a40554960` L176 逐字）⇒ **本件只出计数与可达性，⛔ 0 出 4-2 达标/未达标判定** |

---

## §1 输入件（**当轮实测指纹 · `hashlib.sha256` ＋ .NET `Get-FileHash` 双法同值**）

| # | 件 | SHA-256[:12] | 字节 | 容器 | 事件行数 |
|---:|---|---|---:|---|---:|
| 1 | `results/_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | `172093A23E4B` | 4,103 | `supplements` | 3 |
| 2 | `results/_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json` | `439721007AAF` | 6,132 | `supplements` | 4 |
| 3 | `results/_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json` | `41D6C28CA87C` | 7,566 | `supplements` | 4 |
| 4 | `results/_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json` | `99C58906F792` | 6,666 | `supplements` | 4 |
| 5 | `results/_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json` | `C6D092F77932` | 7,668 | `supplements` | 4 |
| 6 | `results/_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json` | `26F110A6E571` | 10,257 | `supplements` | 4 |
| 7 | `results/_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json` | `6E104E2DB038` | 11,589 | `supplements` | 4 |
| 8 | `results/_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json` | `D96B747BFC6C` | 14,722 | `supplements` | 4 |
| 9 | `results/_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | `401BD614CDF7` | 19,615 | `supplements` | 4 |
| 10 | `results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json` | `CBF60A630C9F` | 20,194 | `supplements` | 5 |
| 11 | `results/_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json` | `6EED9ACDB99A` | 18,714 | `relabel_table` | **0**（映射表非事件） |
| 12 | `results/_v4_pi_cot_v3_dataset_addendum_d5_2026_09_27.json` | `990C0C42A6F6` | 16,587 | `supplements` | 2 |
| 13 | `results/_v4_pi_cot_v3_dataset_addendum_d6_2026_09_28.json` | `9669EFA804B7` | 19,214 | `supplements` | 2 |
| 14 | `results/_v4_pi_cot_v3_dataset_addendum_d6b_2026_09_28.json` | `5D94A8617B5B` | 27,009 | `supplements` | 2 |
| 15 | `results/_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json` | `769EF8B71462` | 374,072 | `supplements` | 93 |
| 16 | `results/_v4_pi_cot_v3_dataset_addendum_d8_bhalf_2026_09_30.json` | `B02EF31F1E4E` | 58,581 | `supplements` | 3 |
| 17 | `results/_v4_pi_cot_v3_dataset_addendum_s3_d7_2026_09_29.json` | `C0EBBD1F4633` | 17,252 | `supplements` | 1 |
| 18 | `results/_v4_pi_cot_v3_dataset_addendum_s3_d1fill_2026_10_01.json` | `B9026CBF5CA2` | 46,909 | `supplements` | 6 |
| 19 | `corpus/v20/S4.json` | `E6045F0920EC` | 4,932 | `nodes`/`labels`/`edges` | **0**（图件，⛔ 0 强入格） |

**辅助锚件（字面来源）**：`results/_v3_s_prereg_v1_2026_09_27.md` ＝ `EF5A40554960`／46,836 B（L175–L178 §2.4 三线字面 ＋ L218 T-5）；`results/_s3_kv3s_3_full_recompute_2026_10_01.md` ＝ `B0123F161C10`／22,183 B（现读数基线·仅照录，⛔ 0 沿用其读数）。

> ✅ **addendum 件数实测 ＝ 18**（与派工单所载「当轮实测计数 18」同值）。

### §1.1 事件容器认定（**0 混计非事件行**）

- **计入**：`supplements`（**唯一事件容器**）合计 **149 行**；
- **⛔ 0 计入**：`relabel_table`（5）、`cross_cutting_signals`（12）、`honesty_boundary`、`pending_actions`、`source_ask_ids`、`linked_pending_decisions` —— 皆**非事件行**（映射表/信号表/元数据清单）。

---

## §2 分格键之派生口径（**沿既有派生 · ⛔ 0 新造键**）

派工单要求「分格键 ＝ `is_corr_pair` × `scene_bucket_8` × `opt_bucket_8`（**沿既有字段**、⛔ 0 新造键）」。

> **实测结论（重要）**：三键**并非 addendum 记录层之原生字段**（addendum 记录层实有 `is_correction`／`scene_tag`／`option_chosen` 等）。三键系 **v3 executor 之既有派生特征**。

**沿用之既有实现（逐字沿 `results/_v4_pi_cot_v3_ruleset_v3_executor.py`，0 改 1 字）**：

| 项 | 既有实现位置 | 口径 |
|---|---|---|
| `bucket_hash` | L544–545 | `zlib.crc32(s.encode("utf-8")) % mod` |
| `scene_bucket_8` | L595 | `bucket_hash(scene_tag, 8)` |
| `opt_bucket_8` | L596 | `bucket_hash(option_chosen, 8)` |
| `is_corr_pair` | L556–559 ＋ L597 | `1` 当 `is_correction` 为 str 且（`endswith("_pair_pending")` 或 `== "R_pair"`）；否则 `0` |
| 特征键注册 | L328–337 | 12 项特征含此三键 |

**空串回落（如实登记 · ⛔ 0 静默修补）**：`scene_tag` 缺/空 **22 行**、`option_chosen` 缺/空 **15 行** ⇒ 沿既有 `or ""` 回落入桶（`crc32("") % 8 = 0`），**如实声明，未补值、未剔除**。

---

## §3 逐格可得样本数（**128 格全表 · 逐格可数**）

**行** ＝ `is_corr_pair` × `scene_bucket_8`（0–7）｜**列** ＝ `opt_bucket_8`（0–7）

```
        opt →     0    1    2    3    4    5    6    7   | 行合计
b=0  s=0           2   13    4   13    1    0    3    3   |   39
b=0  s=1           1    4    0    4    2    0    1    5   |   17
b=0  s=2           3    1    0    5    0    0    2    3   |   14
b=0  s=3           0    3    2    5    1    0    0    3   |   14
b=0  s=4           4    3    1   11    0    0    0    1   |   20
b=0  s=5           2    1    0    6    0    0    1    5   |   15
b=0  s=6           1    2    0    7    0    0    2    3   |   15
b=0  s=7           3    7    0    3    2    0    0    0   |   15
b=1  s=0..7        0    0    0    0    0    0    0    0   |    0   （8 行全空）
...
b=1  s=7           0    0    0    0    0    0    0    0   |    0
                       ────────────────────────────────────────
                       └────────── 合计 149 ──────────┘
```

### §3.1 格数与空格数（**度量项 1–2**）

| 项 | 读数 |
|---|---:|
| 格总数（2 × 8 × 8） | **128** |
| **占格数** | **42** |
| **空格数** | **86** |
| 每格 n 之 `min` / `max` | **1** / **13** |
| 每格 n 之 `sum` | **149** |
| 占格均值 | 3.5476 |
| 占格中位数 | 3.0 |
| 占格 n 之取值种数 | 9 |
| 占格 n 之总体标准差 | 2.0292 |
| `n == 1` 之格数 | **10** |
| `n ≤ 3` 之格数 | **28** |

### §3.2 边缘分布（**逐格可对位**）

| `scene_bucket_8` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| n | **39** | 17 | 14 | 14 | 20 | 15 | 15 | 15 |

| `opt_bucket_8` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| n | 16 | **34** | 7 | **54** | 6 | **0** | 9 | 23 |

### §3.3 `is_corr_pair` 轴（**如实登记 · 0 修补**）

| 取值 | 行数 |
|---|---:|
| `0` | **149** |
| `1` | **0** |

> ⚠️ **实测事实**：18 件 addendum 之 `is_correction` 分布 ＝ `False` 104 ／ `True` 7 ／ **缺字段 35** ／ 非标量 3；**无任何 `_pair_pending`／`R_pair` 字符串值** ⇒ 沿既有 `is_corr_bin` 口径，**该轴恒为 0**。
> ⇒ **128 格中 64 格（`b=1` 之全行）在 addendum substrate 上结构性全空**。**如实登记，⛔ 0 造值、⛔ 0 改 `is_corr_bin` 实现、⛔ 0 剔除该轴。**

---

## §4 held-out 可达性（**静态算术上界 · 0 抽样 · 0 `round()` 就近替代**）

**比例字面 ＝ 0.30**（沿 `ef5a40554960` L175 ＝ `TH-v2-4`／`TH-v3-4`，**0 擅调**）。

| 项 | 读数 |
|---|---:|
| 逐格 `floor(n_c × 0.30)` 之和 | **22** |
| 逐格 `ceil(n_c × 0.30)` 之和 | 64 |
| `floor(0.30·n) ≥ 1` 之格数 | **14**（＝ `n ≥ 4` 之格数） |
| `floor(0.30·n) = 0` 之格数 | **28** |
| **`held-out ≥ 50` 在逐格严格 floor 下可达？** | **❌ 否**（22 < 50） |

> ⚠️ **T-5 字面处置（`ef5a40554960` L218 逐字）**：「空格 >0 ⇒ K-V3S-4-1 记『**0.30 名义达标／实际分层不可达**』，⛔ **0 静默改成 `round()` 就近抽样**」。
> ⇒ **空格数 86 > 0** ⇒ **本面即登记「0.30 名义达标／实际分层不可达」**；**⛔ 本件 0 建抽样器、0 抽 seed、0 落 held-out 集、0 用 `round()` 就近替代**。

---

## §5 `P-S4-1` 自洽性达成性（**算术账 · 0 代裁**）

三线字面（`ef5a40554960` L176 逐字，**0 改任一条**）：`substrate ≥ 150` **且** `held-out ≥ 50` **且** `K-V3S-4-1` 达标 ⇒ **自洽下限 substrate ≥ 167**（＝ 50 / 0.30 之算术推导）。

| 线 | 阈值 | 本棒实测 | 达成？ | 差量 |
|---|---:|---:|---|---:|
| substrate | **150** | **149** | ❌ | **−1** |
| held-out | **50** | **22**（逐格 floor 和） | ❌ | **−28** |
| substrate 自洽下限 | **167** | **149** | ❌ | **−18**（缺口 18） |

**辅助算术**：149 × 0.30 ＝ **44.7**；167 × 0.30 ＝ **50.1**。

> ⛔ **`P-S4-1` 之裁（择 150／50／167 之一或明示例外）属 PI 面** ⇒ 本件**0 择线、0 宣告、0 宣告 `K-V3S-4-2` 达标/未达标**，仅将三线读数**并列**呈核。
> ⚠️ **口径敏感性（如实标出）**：149 距 150 仅差 **1 件**、距 167 差 **18 件** ⇒ 是否越线**对本 substrate 冻结口径极敏感**（沿 `_s4_reading_prep_order_2026_10_08.md` §1.1 之 R-3/R-4「170／167 分居两侧」同类提示）。

---

## §6 双实现交叉（N-5 硬要件 · **0 分歧**）

| 实现 | 路径 | 行数 | 占格 | 空格 | floor-sum |
|---|---|---:|---:|---:|---:|
| **实现 1** | `json` ＋ `zlib.crc32` | 149 | 42 | 86 | 22 |
| **实现 2** | `json` ＋ **手写逐位 CRC32**（poly `0xEDB88320`，0 调用 zlib） | 149 | 42 | 86 | 22 |

**逐格互证**：42 个占格**逐格比对 · 分歧 0**；CRC 探针（`scene_tag = "热力学"`）两法同得 `% 8 = 6`。

---

## §7 老实交代（**未坐实项明写**）

1. **三格键非 addendum 原生字段** —— 系 v3 executor 既有派生特征。本棒**沿既有实现逐字复用**（`bucket_hash`／`is_corr_bin`），**0 新造键、0 改实现**。
2. **`is_corr_pair` 轴恒 0** —— 因 addendum 侧无 `_pair_pending`／`R_pair` 字符串值 ⇒ 该轴 64 格结构性全空。**如实登记，0 修补**；其可通约性系「补记规则／配对登记」族问题，**0 由本棒处置**。
3. **空串回落** —— `scene_tag` 缺/空 22 行、`option_chosen` 缺/空 15 行，沿既有 `or ""` 回落入桶；**未补值、未剔除**。
4. **`corpus/v20/S4.json` 贡献 0 行** —— 该图件仅载 `nodes`/`labels`/`edges`（N=40 节点），**0 载三格键** ⇒ 列为锚件，**⛔ 0 强入格表**。
5. **`substrate_N = 149` 之性质** —— 系**本预报告之 addendum 侧实测计数**，⛔ **0 声称其等于未来冻结后之 S4 substrate**；亦**未沿用** `b0123f161c10` 之 N 读数 160–180（`K-V3S-3-2` 明令**重算**而非沿用）。
6. **held-out 可达性为静态上界** —— 由占格量算术推导，**未建抽样器、未抽 seed、未落 held-out 集**（属 S4 执行波）。
7. **`relabel_table` 5 行 0 计入** —— 映射表非事件行；同理 `cross_cutting_signals` 12 行。
8. **0 判定面** —— 本件**0 赋 `k_v3s_4_1_ok`／`k_v3s_4_2_ok`／`k_v3s_4_3_ok` 任一布尔**；**0 代裁 `P-S4-1`**；**0 宣告 S4 段可开跑**。
9. **隐私面** —— 本件⛔ **0 贴 dataset 内部字段**（`reasoning_full`／`scene_verbatim`／`pi_answer_verbatim` 等一律未落盘）；引用**仅路径 ＋ SHA-12 ＋ 字节 ＋ 格子下标 ＋ 聚合计数**。
10. **与 C-3 棒之关系** —— `_s4_reading_prep_order_2026_10_08.md`（执行序）§2.1 之 **S2 步「按 T-5 三维格子逐格报可得样本数」**、§3 之 **G6 闸「T-5 逐格样本数开跑前预报」**、§2.1 前置② 与验收 **A1-2** 均**指向本件**；本件**仅供该步/该闸之计数面**，**0 代该序执行、0 宣告 G6 已成就**（G6 之成就与开跑总闸属 PI/执行面）。
11. **本件自身指纹** —— ⛔ **不自写入本件**（自指回环）⇒ 随交付回执回报，外部观测者请以 `Get-FileHash -Algorithm SHA256` 独立复算。

---

## §8 落盘自证 ＋ 状态

- **落前撞名实测**：`Test-Path` 之 `.json` ＝ **False**、`.md` ＝ **False**；`results/*grid_availability*` glob 命中 **0** ⇒ ✅ **新名新建·0 覆写**
- **编码**：**UTF-8 无 BOM** · **LF**
- **输入面**：全程**只读**（21 件 `Get-FileHash -Algorithm SHA256` ＋ `hashlib.sha256` 双法）；**0 回改任何既有件**
- **产出**：**新增 2 件即停**（OR-2 条所载 JSON ＋ MD 两件名）

| 项 | 内容 |
|---|---|
| **本轮实做** | 分格计数（149 行 × 128 格）＋ 空格面 ＋ 每格 n 分布 ＋ held-out 静态可达上界 ＋ 三线并列算术账 ＋ 双实现交叉（0 分歧） |
| **本轮 0 做** | ⛔ 0 判定 ｜ ⛔ 0 档位 ｜ ⛔ 0 赋布尔 ｜ ⛔ 0 改阈值 ｜ ⛔ 0 `round()` 就近抽样 ｜ ⛔ 0 抽样/seed/held-out 集 ｜ ⛔ 0 代裁 `P-S4-1` ｜ ⛔ 0 回改既有件 ｜ ⛔ 0 网络 ｜ ⛔ 0 贴 dataset 内部字段 |
| **下一动作面** | 本件交 PI/verdict 面复核；`P-S4-1` 拍板（PI 面）→ S4 substrate 冻结 → worker 抽样（seed ＝ 42 沿 `TH-v3-15`，0 换）→ verifier 独立复核 → verdict-keeper 落档 |
| **出件** | **worker**（Mavis 团队 worker · session `mvs_18a8b3d1c78a4609a00288da177cc96d`｜**署名如实**）｜2026-10-08