# `R_ITT` 重测之新读数面登记件：**三 seed × 15 格 · 乙候选口径 · 原生分母恒为 H**

**棒** `RITT-REMEASURE`｜**拟稿** mavis（worker）｜**日期** 2026-10-17｜**性质** 重测执行＋新读数面登记（**⛔ 0 落五终判 · ⛔ 0 代 PI 裁 · ⛔ 0 闭任何既有 `KD`**）
**裁面归属** PI（卡 `ask_c1b1d0be670d7b725c12db03` 之三裁）

**FTFB（判死线先于测量/改动冻结）**：本棒之判死线冻结件 `.tmp/ritt_remeasure_freeze_2026_10_17.json`（`a41f38631fab`）落于**任何 LLM 调用与任何新码件落盘之前**；冻结时点之盘上十件关键件指纹已逐位登记，且**测量终态复校 10/10 与冻结值一致**（§9）。

---

## §0 一句话交付

**新读数面 45 格（15 格 × 3 seed）之 `R_ITT` 全部产出：`R_ITT` ＝ `#{t : A_t ∉ K_t} / H`，原生分母逐格实测恒为 `H`（45/45），no-action 计为 `∉K_t`，720 次 LLM 调用 0 传输错误，独立复算路径 45/45 逐格吻合；`correct` 字段之一等采集已落账（240 行，`correct` 100% 属 options 集）。**

**⇒ 与轨迹面之关系：另立读数面，不与之比**（PI 三裁③）——本棒 ⛔ 0 读轨迹面载体之读数、⛔ 0 作差分、⛔ 0 合并计数。

---

## §1 本棒之射程与纪律边界

| 面 | 本棒之立场 |
| :-- | :-- |
| PI 三裁① 乙候选采认 | ✅ **已按采认执行**（口径逐字落于码面，45/45 原生分母实测坐实） |
| PI 三裁② 授权新增采集码面（采集 `correct`） | ✅ **已新增**（新脚本，基线脚本 0 回改） |
| PI 三裁③ 另立读数面·不与轨迹面比 | ✅ **严格遵守**（另建 cache 与载体，⛔ 0 读/比/合并轨迹面读数） |
| `tools/exp_harness.py`／`distortion_calculator.py` | ⛔ **0 回改一字**（终态指纹与冻结值一致，§9） |
| `.tmp/three_seed_collect_2026_10_16.py`（结构母本） | ⛔ **0 回改一字**（终态 `672d12ad9801` 未变） |
| 轨迹读数载体 `ff5ed4b0e329` | ⛔ **0 读其读数 · 0 差分 · 0 合并计数**；⛔ 0 回改 |
| 既有三 seed 读数面之效力 | ⛔ **0 主张**（归姊妹件裁面） |
| 五终判（`pass`／`af`／`kd`／`fail`／`give-up`） | ⛔ **0 落**——§8 所列 `KD-RM-*` 系**候裁清单之条目名**，非终判 |

---

## §2 逐字回读源之登记（**本棒直算指纹 · 非照录**）

| 源件 | 角色 | 本棒直算 SHA-12 | 本棒直算 bytes | 与在册字面 |
| :-- | :-- | :-- | --: | :-- |
| `results/_ritt_def_proof_2026_10_17.md` | 本棒上游·定义式前置取证件 | `5d411ebf07ed` | 23,310 | ✅ 一致（该件 §2 之自报亦为 `5d411ebf07ed`） |
| `.tmp/three_seed_collect_2026_10_16.py` | **采集码面基线**（结构母本） | `672d12ad9801` | 28,520 | ✅ 一致（该件 §2 之在册值） |
| `.tmp/three_seed_caliber_decl_2026_10_16.json` | **🔴 乙候选之盘上正身**（测量前口径声明） | `5df309d557b0` | 4,859 | ✅ 一致 |
| `.tmp/three_seed_freeze_2026_10_16.json` | 轨迹面判死线冻结件 | `46260e3b8426` | 10,536 | ✅ 一致 |
| `.tmp/three_seed_measurement_2026_10_16.json` | 轨迹读数载体（⛔ 0 读其读数） | `ff5ed4b0e329` | 226,256 | ✅ 一致 |
| `.tmp/m41_r15_collect_readout.py` | 解析规则之实体（照录其 L61-77） | `d4e882337b80` | 13,324 | ✅ 一致 |
| `tools/exp_harness.py` | 面构建实体 | `026575ff3829` | 41,428 | ✅ 一致 |
| `tools/distortion_calculator.py` | `R_PP(D)` 实体 | `410a12482eef` | 40,611 | ✅ 一致 |

### §2-1 乙候选口径之**逐字锚**（本棒直读，非转述）

`.tmp/three_seed_caliber_decl_2026_10_17.json` 所载 `C1_R_primary_caliber.R_ITT_definition` 逐字：

> `R_ITT = #{t ∈ 1..H : A_t ∉ K_t} / H`（**全分母**；依 KL-M41-1 逐字，0 有效动作（no-action）计为 `A_t∉K_t`）

**⇒ PI 三裁① 之采认对象与该逐字字面一致；本棒之码面实现与之逐位相符**（`flag = 0 if (a is not None and a == c['correct']) else 1`；`R_ITT = Fraction(sum(flags), H)`）。

---

## §3 新增采集码面（PI 三裁② 之授权产物）

### §3-1 码面之最小增量自查（本棒直算）

| 面 | 结果 |
| :-- | :-- |
| 新脚本 | `.tmp/ritt_remeasure_collect_2026_10_17.py`（`38b2cecb2d16`，33,524 B） |
| 结构母本 | `.tmp/three_seed_collect_2026_10_16.py`（`672d12ad9801`，28,520 B）**0 回改** |
| 新增函数（直算差集） | `collect_correct_face`、`r_itt_recompute_from_detail`（**恰 2 个**） |
| 删除函数（直算差集） | **0** |
| 处理条件逐项核 | `MAX_TOKENS = 48`、`TEMPERATURE = 0`、`SEEDS = (42, 123, 456)`、`TRIES = 3`、`WORKERS = 6`、`TIMEOUT = 60` —— **6/6 与母本一致** |
| `flag` 行 | 母本 L311 与新码面**逐字一致** |

### §3-2 增量四处（授权射程内）

| # | 增量 | 实现 | 对应 PI 裁 |
| :-: | :-- | :-- | :-: |
| ① | **`correct` 字段之一等采集与落盘** | `collect_correct_face()`：逐格记 `correct`／`options`／`n_options`／`correct_is_member_of_options`／`prompt_digest12`／`correct_digest12`／`value_digest12`；另立 `correct_face` 账 | 三裁② |
| ② | **分子与原生分母显式并落盘** | `R_ITT_numerator_nK`（＝`#{A_t∉K_t}`）／`R_ITT_denominator_native_H`／`R_ITT_native_fraction`／`R_ITT_reduced`（是否已约分） | 三裁① |
| ③ | **第二条独立复算路径** | `r_itt_recompute_from_detail()`：⛔ 0 复用主路径 `flags`，仅凭 `detail` 之 `correct`＋`llm_action` 重算 ⇒ 阳性对照 | 自检面 |
| ④ | **读数面另立** | 另建 cache（`3e68a203fa06`）与载体（`29bb4c4a8bca`）⇒ ⛔ 0 读/比/合并轨迹面 | 三裁③ |

**⇒ 复跑侧「0 载 `correct`」之缺口（`KD-RITT-5` 之实体面）在本棒已闭**：新载体 `detail` 720 条与 `correct_face` 240 条**逐格载 `correct`**，且 `correct_face_is_member_of_options_all` ＝ `True`（240/240）。

---

## §4 采集面登记（**3 行 · 交付判据面**）

| 项 | 实测值 |
| :-- | :-- |
| **采集脚本** | `.tmp/ritt_remeasure_collect_2026_10_17.py`　**SHA-12** `38b2cecb2d16`　**bytes** 33,524　BOM=0　CR=0 |
| **seed** | `(42, 123, 456)` —— 沿 720 面之三 seed，逐字取自 `three_seed_collect_2026_10_16.py` L55 `SEEDS = (42, 123, 456)`（与测量前口径声明件之 `KL_M41_3_verbatim_anchor` 一致） |
| **H** | `T1_GSM8K`=15／`T2_StrategyQA`=15／`T3_Trap`=15／`T4_2x2`=15／`T5_LowResource`=20　⇒ 每 seed·机制 80 格，**全棒 720 格·3 机制**（45 格·seed 组合） |
| **时点** | 冻结 2026-10-17T19:56:00+08:00（先于任何调用）→ 采集起于其后 → 采集终 **elapsed 643.1 s** → 载体 `29bb4c4a8bca` 落盘 |
| **端点／处理条件** | `claude-haiku-5-5`／host `api.teamorouter.cn`／`max_tokens=48`／`temperature=0`／system 模板与解析规则照录三前棒；**key 仅自 runtime env 读入 client 内部，⛔ 0 打印 0 入件 0 入日志 0 入 prompt**（R4） |
| **调用账** | 发出 720／在册 720／有效动作 700／0 有效动作 20／传输类错误 **0**／缺记录 0 |

### §4-1 采集完整性

| 指标 | 实测 |
| :-- | :-: |
| `cells_total` ／ `cells_missing` | 45 ／ **0** |
| `llm_calls_total` ／ `llm_record_present_total` | 720 ／ 720 |
| `llm_valid_action_total` ／ `llm_zero_valid_action_total` | 700 ／ **20** |
| `llm_err_records_total` | **0** |
| `correct_face_rows` | **240**（＝3 seed × 80 格，每格恰 1 条） |
| `correct` 属 options 集 | **240/240** |

---

## §5 逐格 `R_ITT`（**乙候选口径** · 45 格全量）

**列义**：`nK/H` ＝ **原生分数 `#{A_t∉K_t}/H`**（PI 三裁①：原生分母恒为 `H`）；`R_ITT` ＝ `Fraction` 最简字面；`noact` ＝ 0 有效动作格数（**计为 `∉K_t`**）；`mech` ＝ 机制臂正确数（**仅并报·非 `R_ITT` 分子**，见 §6-2）。

| seed | 机制 | 族 | H | nK/H（原生） | `R_ITT`（最简） | noact | `R_no_action` | mech |
| --: | :-- | :-- | --: | :-- | :-- | --: | :-- | :-- |
| 42 | M1_Deposon_TRA | T1_GSM8K | 15 | 2/15 | `2/15` | 1 | 1/15 | 13/15 |
| 42 | M1_Deposon_TRA | T2_StrategyQA | 15 | 6/15 | `2/5` | 0 | 0 | 13/15 |
| 42 | M1_Deposon_TRA | T3_Trap | 15 | 0/15 | `0` | 0 | 0 | 8/15 |
| 42 | M1_Deposon_TRA | T4_2x2 | 15 | 6/15 | `2/5` | 0 | 0 | 12/15 |
| 42 | M1_Deposon_TRA | T5_LowResource | 20 | 15/20 | `3/4` | 2 | 1/10 | 10/20 |
| 42 | M2_Greedy | T1_GSM8K | 15 | 3/15 | `1/5` | 1 | 1/15 | 15/15 |
| 42 | M2_Greedy | T2_StrategyQA | 15 | 6/15 | `2/5` | 0 | 0 | 15/15 |
| 42 | M2_Greedy | T3_Trap | 15 | 1/15 | `1/15` | 0 | 0 | 15/15 |
| 42 | M2_Greedy | T4_2x2 | 15 | 5/15 | `1/3` | 0 | 0 | 15/15 |
| 42 | M2_Greedy | T5_LowResource | 20 | 16/20 | `4/5` | 2 | 1/10 | 20/20 |
| 42 | M3_Random | T1_GSM8K | 15 | 4/15 | `4/15` | 1 | 1/15 | 4/15 |
| 42 | M3_Random | T2_StrategyQA | 15 | 4/15 | `4/15` | 0 | 0 | 3/15 |
| 42 | M3_Random | T3_Trap | 15 | 2/15 | `2/15` | 0 | 0 | 8/15 |
| 42 | M3_Random | T4_2x2 | 15 | 8/15 | `8/15` | 0 | 0 | 12/15 |
| 42 | M3_Random | T5_LowResource | 20 | 12/20 | `3/5` | 1 | 1/20 | 5/20 |
| 123 | M1_Deposon_TRA | T1_GSM8K | 15 | 6/15 | `2/5` | 1 | 1/15 | 13/15 |
| 123 | M1_Deposon_TRA | T2_StrategyQA | 15 | 6/15 | `2/5` | 0 | 0 | 8/15 |
| 123 | M1_Deposon_TRA | T3_Trap | 15 | 3/15 | `1/5` | 0 | 0 | 9/15 |
| 123 | M1_Deposon_TRA | T4_2x2 | 15 | 6/15 | `2/5` | 0 | 0 | 12/15 |
| 123 | M1_Deposon_TRA | T5_LowResource | 20 | 17/20 | `17/20` | 2 | 1/10 | 11/20 |
| 123 | M2_Greedy | T1_GSM8K | 15 | 5/15 | `1/3` | 2 | 2/15 | 15/15 |
| 123 | M2_Greedy | T2_StrategyQA | 15 | 6/15 | `2/5` | 1 | 1/15 | 15/15 |
| 123 | M2_Greedy | T3_Trap | 15 | 3/15 | `1/5` | 0 | 0 | 15/15 |
| 123 | M2_Greedy | T4_2x2 | 15 | 5/15 | `1/3` | 0 | 0 | 15/15 |
| 123 | M2_Greedy | T5_LowResource | 20 | 19/20 | `19/20` | 0 | 0 | 20/20 |
| 123 | M3_Random | T1_GSM8K | 15 | 5/15 | `1/3` | 0 | 0 | 8/15 |
| 123 | M3_Random | T2_StrategyQA | 15 | 5/15 | `1/3` | 0 | 0 | 4/15 |
| 123 | M3_Random | T3_Trap | 15 | 6/15 | `2/5` | 0 | 0 | 8/15 |
| 123 | M3_Random | T4_2x2 | 15 | 10/15 | `2/3` | 0 | 0 | 6/15 |
| 123 | M3_Random | T5_LowResource | 20 | 17/20 | `17/20` | 1 | 1/20 | 5/20 |
| 456 | M1_Deposon_TRA | T1_GSM8K | 15 | 8/15 | `8/15` | 2 | 2/15 | 13/15 |
| 456 | M1_Deposon_TRA | T2_StrategyQA | 15 | 8/15 | `8/15` | 0 | 0 | 10/15 |
| 456 | M1_Deposon_TRA | T3_Trap | 15 | 1/15 | `1/15` | 0 | 0 | 11/15 |
| 456 | M1_Deposon_TRA | T4_2x2 | 15 | 7/15 | `7/15` | 0 | 0 | 10/15 |
| 456 | M1_Deposon_TRA | T5_LowResource | 20 | 15/20 | `3/4` | 1 | 1/20 | 9/20 |
| 456 | M2_Greedy | T1_GSM8K | 15 | 10/15 | `2/3` | 0 | 0 | 15/15 |
| 456 | M2_Greedy | T2_StrategyQA | 15 | 5/15 | `1/3` | 0 | 0 | 15/15 |
| 456 | M2_Greedy | T3_Trap | 15 | 2/15 | `2/15` | 0 | 0 | 15/15 |
| 456 | M2_Greedy | T4_2x2 | 15 | 7/15 | `7/15` | 0 | 0 | 15/15 |
| 456 | M2_Greedy | T5_LowResource | 20 | 20/20 | `1` | 0 | 0 | 20/20 |
| 456 | M3_Random | T1_GSM8K | 15 | 10/15 | `2/3` | 0 | 0 | 2/15 |
| 456 | M3_Random | T2_StrategyQA | 15 | 6/15 | `2/5` | 0 | 0 | 5/15 |
| 456 | M3_Random | T3_Trap | 15 | 2/15 | `2/15` | 0 | 0 | 6/15 |
| 456 | M3_Random | T4_2x2 | 15 | 8/15 | `8/15` | 0 | 0 | 7/15 |
| 456 | M3_Random | T5_LowResource | 20 | 15/20 | `3/4` | 2 | 1/10 | 5/20 |

### §5-1 原生分母之实测坐实（PI 三裁① 之落地面）

| 判据 | 实测 |
| :-- | :-: |
| `R_ITT_denominator_native_H` 逐格 ＝ `H_face` | **45/45 ⇒ `R_ITT_native_denominator_all_H` = `True`** |
| 最简形与原生形不同（已约分）之格数 | **28/45**（余 17 格原生即最简） |
| 第二条独立复算路径（仅凭 `detail` 之 `correct`＋`llm_action`） | **45/45 逐格吻合；失配 0 格** |

**⇒ 约分面之实测确证**：`2/5`、`3/4`、`17/20` 等字面**均系 `nK/H` 约分而来**（如 `6/15 → 2/5`），**原生分母恒为 `H`**；凡见最简分数字面者，⛔ 0 解读为「该分数即原生分母」（沿 `KD-RITT-3` 之射程，本棒以 45/45 逐格落地面实测佐证之）。

### §5-2 跨 seed 敏感性（**KL-M41-3 · 阈值 0.20 逐字未动 · 并报 ddof=0／1**）

| 机制·族 | 三 seed 之 `R_ITT`（最简） | ddof0 比率 | ddof0 命中 | ddof1 命中 |
| :-- | :-- | --: | :-: | :-: |
| M1_Deposon_TRA·T1_GSM8K | 2/15, 2/5, 8/15 | 0.4677 | **是** | **是** |
| M1_Deposon_TRA·T2_StrategyQA | 2/5, 2/5, 8/15 | 0.1414 | 否 | 否 |
| M1_Deposon_TRA·T3_Trap | 0, 1/5, 1/15 | 0.9354 | **是** | **是** |
| M1_Deposon_TRA·T4_2x2 | 2/5, 2/5, 7/15 | 0.0744 | 否 | 否 |
| M1_Deposon_TRA·T5_LowResource | 3/4, 17/20, 3/4 | 0.0602 | 否 | 否 |
| M2_Greedy·T1_GSM8K | 1/5, 1/3, 2/3 | 0.4907 | **是** | **是** |
| M2_Greedy·T2_StrategyQA | 2/5, 2/5, 1/3 | 0.0832 | 否 | 否 |
| M2_Greedy·T3_Trap | 1/15, 1/5, 2/15 | 0.4082 | **是** | **是** |
| M2_Greedy·T4_2x2 | 1/3, 1/3, 7/15 | 0.1664 | 否 | **是** |
| M2_Greedy·T5_LowResource | 4/5, 19/20, 1 | 0.0927 | 否 | 否 |
| M3_Random·T1_GSM8K | 4/15, 1/3, 2/3 | 0.4144 | **是** | **是** |
| M3_Random·T2_StrategyQA | 4/15, 1/3, 2/5 | 0.1633 | 否 | 否 |
| M3_Random·T3_Trap | 2/15, 2/5, 2/15 | 0.5657 | **是** | **是** |
| M3_Random·T4_2x2 | 8/15, 2/3, 8/15 | 0.1088 | 否 | 否 |
| M3_Random·T5_LowResource | 3/5, 17/20, 3/4 | 0.1401 | 否 | 否 |

**汇总**：`SEED_SENSITIVE`（ddof=0）＝ **6/15 格**；ddof=1 ＝ **7/15 格**（差异仅 `M2_Greedy·T4_2x2` 一格）。命中格集中于 **`T1_GSM8K` 与 `T3_Trap` 两族 × 三机制全数**（6 格）。
**本棒 ⛔ 0 据此下任何判死裁决**——判死裁决权属 verdict-keeper（`KL_M41_3_summary` 之登记）。

---

## §6 与轨迹面之关系（**PI 三裁③ 之遵守登记**）

### §6-1 另立读数面（本棒 0 比 0 差分）

| 面 | 本棒之处置 |
| :-- | :-- |
| 定位 | **新口径面之新读数**——依 PI 三裁③，**不与轨迹面比**，**另立读数面** |
| 读数载体 | 另建 `.tmp/ritt_remeasure_measurement_2026_10_17.json`（`29bb4c4a8bca`，325,531 B） |
| 调用缓存 | 另建 `.tmp/ritt_remeasure_llm_calls_2026_10_17.jsonl`（`3e68a203fa06`，106,119 B，720 行） |
| 与轨迹面之差分 | **⛔ 0 作**——本棒⤳⤳ 0 计算任何「新读数 − 轨迹读数」之量，0 合并计数，0 跨面汇聚 |
| 轨迹面读数之效力 | **⛔ 0 主张**（归姊妹件裁面；本面之结论⛔ 0 反向作用于轨迹面） |

### §6-2 机制臂读数**非** `R_ITT` 分子（**并报·不混**）

**本棒数据面自证**：`M2_Greedy`（机制臂全对 15/15–20/20）之 `R_ITT` 仍为 `1/5`…`1`（**远非 0**）⇒ `R_ITT` 读数来自 **LLM 动作侧**而非机制臂 ⇒ §5 之 `mech` 列**仅作对照并报**，⛔ 0 与 `R_ITT` 混算、⛔ 0 解读为机制效应（沿口径声明 C4：三机制读数差异仅来自端点非确定）。

---

## §7 与上游前置清单（`P1`–`P6`）之关系（**照录归属 · 本棒 ⛔ 0 代裁**）

| 前置项 | 内容（照录 `5d411ebf07ed` §5-2） | 本棒之关系 |
| :-- | :-- | :-- |
| `P1` | 定义面之择（采乙候选） | **PI 已裁（卡 `ask_c1b1d0be670d7b725c12db03` 三裁①）**；本棒按采认执行并实测坐实 45/45 |
| `P2` | `KD-T3RP-4` 之处置 | **本棒 ⛔ 0 处置**（非本棒裁面） |
| `P3` | 采集码面之新增授权 | **PI 已裁（三裁②）**；本棒已新增且 0 越授权射程（§3-2 恰四处） |
| `P4` | 正解集之跨态同一性处置 | 🔴 **本棒实测出新事实**（见 `KD-RM-1`）：面 digest 与轨迹面 **3/15 一致**；**PI 三裁③「不与轨迹面比」已使该问题不阻本棒之重测**（本棒⤳⤳ 不作跨面比较，故无可比性要求）；惟若他棒欲作跨面比较，须先裁正解集同一性 |
| `P5` | 并报面（`llm_action`）之重估 | 本棒之 `detail` 720 条逐格载 `llm_action`＋`correct` ⇒ **`KD-RM-2` 之可充性已具备**（值侧）；**⛔ 0 主张该面已无须** |
| `P6` | 判读线 `L2` 之处置 | **本棒 ⛔ 0 处置**（非本棒裁面） |

---

## §8 本件新立 `KD` 清单（**候 PI 裁 · 本棒 0 裁 0 闭 · ⛔ 0 落五终判**）

| # | `KD` | 内容 | 状态 | 归属 |
| :-: | :-- | :-- | :-- | :-- |
| **`KD-RM-1`** | **正解集跨态漂移于本棒实测坐实：面 digest 与轨迹面仅 3/15 一致**（`T1_GSM8K` 三 seed 全同；`T2_StrategyQA`／`T3_Trap`／`T4_2x2`／`T5_LowResource` 十二格全异） | 预飞以 `d12(prompt+options+correct+value)` 逐族逐 seed 与轨迹面 `digest_by_seed_family` 比对，**3/15 一致、12/15 不一致**；本棒 ⛔ 0 打开其差异根因（⛔ 0 开卷 `C_T3_clues` 之实体），**照录** `1a104886964f` §7 `KD-T3RP-3` 之漂移事实。**⇒ 本棒 ⛔ 0 与轨迹面作任何值之比较**（PI 三裁③ 已在射程上排除该需要） | **新开**（可比性面·**候 PI 裁**） | **PI／protocol-keeper** |
| **`KD-RM-2`** | **重测之复跑侧阻因已消解：新载体逐格载 `correct`，`R_ITT` 之分子可算** | `detail` 720 条 ＋ `correct_face` 240 条逐格载 `correct`；`R_ITT` 45/45 产出、原生分母 45/45 恒为 `H`、独立复算 45/45 吻合；`correct` 240/240 属 options 集 ⇒ **`5d411ebf07ed` §5-1 之「复跑侧 0 载 `correct`」缺口在本棒已闭** | **新开**（缺口闭合面·**候 PI 核准**） | **PI／verdict-keeper** |
| **`KD-RM-3`** | **`R_ITT` 在本面之读数**（45 格全量见 §5；原生分母恒为 `H`；no-action 计为 `∉K_t`，本面实测 20 格 0 有效动作） | 新读数面之读数登记；**⛔ 0 与轨迹面之任何值合并或比较**（PI 三裁③） | **新开**（读数面·**候 PI 采认**） | **PI／verdict-keeper** |
| **`KD-RM-4`** | **跨 seed 敏感性：`R_ITT` 之 `SEED_SENSITIVE` ddof0 ＝ 6/15 格、ddof1 ＝ 7/15 格，命中格集中于 `T1_GSM8K` 与 `T3_Trap` 两族全数** | 阈值 0.20 逐字未动；ddof=0／1 并报；判别为精确有理数比较（⛔ 0 浮点容差）；**本棒 ⛔ 0 据此下判死裁决** | **新开**（判读面·**候 PI／verdict-keeper 裁**） | **verdict-keeper／PI** |
| **`KD-RM-5`** | **本面之可比性自限声明** | 因 `KD-RM-1`，本面读数**仅在自身面内自持**（`R_ITT` 分子/分母/独立复算 45/45 自洽）；**⛔ 0 外推为轨迹面之更新、⛔ 0 解读为口径变更之效应、⛔ 0 与他面并置比较** | **新开**（射程面·**候 PI 核准**） | **PI** |

---

## §9 字节级自报（**落盘后直算 · 本棒直算非照录**）

| 项 | 本件 |
| :-- | :-: |
| 路径 | `results/_ritt_remeasure_readings_2026_10_17.md` |
| SHA-12 | **见交付面于落盘后直算自报**（本件⛔ 0 自嵌·自指悖论） |
| bytes | **同上·交付面自报** |
| 编码 | UTF-8 **无 BOM**（BOM=0） |
| 行尾 | **纯 LF**（CR=0） |
| `U+FFFD` | **0** |

### §9-1 既有码件终态复校（**FTFB 之闭合证明**）

冻结时点 vs 测量终态，**10/10 逐位一致 ⇒ 0 回改**：

| 源件 | 冻结件登记 SHA-12 | 测量终态直算 SHA-12 | 一致 |
| :-- | :-- | :-- | :-: |
| `results/_ritt_def_proof_2026_10_17.md` | `5d411ebf07ed` | `5d411ebf07ed` | ✅ |
| `.tmp/three_seed_collect_2026_10_16.py` | `672d12ad9801` | `672d12ad9801` | ✅ |
| `tools/exp_harness.py` | `026575ff3829` | `026575ff3829` | ✅ |
| `tools/distortion_calculator.py` | `410a12482eef` | `410a12482eef` | ✅ |
| `.tmp/three_seed_caliber_decl_2026_10_16.json` | `5df309d557b0` | `5df309d557b0` | ✅ |
| `.tmp/three_seed_freeze_2026_10_16.json` | `46260e3b8426` | `46260e3b8426` | ✅ |
| `.tmp/three_seed_measurement_2026_10_16.json` | `ff5ed4b0e329` | `ff5ed4b0e329` | ✅ |
| `.tmp/three_seed_llm_calls_2026_10_16.jsonl` | `5a8cbcf85aa7` | `5a8cbcf85aa7` | ✅ |
| `.tmp/m41_r15_collect_readout.py` | `d4e882337b80` | `d4e882337b80` | ✅ |
| `results/_esc5_adoption_and_ritt_remeasure_effect_2026_10_17.md` | `e550e344a258` | `e550e344a258` | ✅（他棒所有·本棒⤳⤳ 0 触碰） |

### §9-2 本棒所建 5 件（**落点沿先例 `.tmp/`**：既有采集脚本、冻结件、口径声明件、清单一律落 `.tmp/`；仅交付登记件落 `results/`）

| 件 | SHA-12 | bytes | BOM | CR |
| :-- | :-- | --: | :-: | :-: |
| `.tmp/ritt_remeasure_freeze_2026_10_17.json` | `a41f38631fab` | 6,636 | 0 | 0 |
| `.tmp/ritt_remeasure_collect_2026_10_17.py` | `38b2cecb2d16` | 33,524 | 0 | 0 |
| `.tmp/ritt_remeasure_llm_calls_2026_10_17.jsonl` | `3e68a203fa06` | 106,119 | 0 | 0 |
| `.tmp/ritt_remeasure_measurement_2026_10_17.json` | `29bb4c4a8bca` | 325,531 | 0 | 0 |
| `.tmp/ritt_remeasure_collect_log_2026_10_17.txt` | `eac10421dcad` | 10,627 | 0 | 0 |

---

## §10 老实交代（**failures & limitations** · 如实列 · ⛔ 0 软化）

| # | 项 | 如实内容 |
| :-: | :-- | :-- |
| 1 | **0 落终判** | §8 之 `KD-RM-1`–`5` 系**候裁清单之条目名**，**非本棒所落之终判**；本棒 **0 落五终判**、0 闭任何既有 `KD`、0 宣告①毕 |
| 2 | **执行链之两次启动失败** | 首次以 `python -c` 启，因 **PowerShell 原生参数引号剥离**致 `SyntaxError`（退出 1）；二次以管道启，因 **BOM（U+FEFF）注入**致 `SyntaxError`（退出 1）；两次均发生于**参数解析层**，**0 次 LLM 调用、0 字节写入**（盘上残留实测：cache/log/carrier 三者皆 `False`），最终以**原始字节 stdin**（`Process.StandardInput.BaseStream`）启成功（退出 0） |
| 3 | **`KD-RM-1` 未开卷** | 本棒**⛔ 0 打开**正解集跨态漂移之根因（`C_T3_clues` 实体不在盘/未开卷）⇒ 仅登记 digest 层不一致之事实，**0 归因、0 断言何 hunk 所致** |
| 4 | **`correct_face` 之粒度** | `correct_face` 为 **每 seed·族·格 1 条（240 行）**；其与 `detail`（720 条，含 3 机制维）之关系为：`detail` 经 `cell_id`＋`seed` 关联至 `correct_face` 之对应条目（`correct` 值逐格一致） |
| 5 | **本棒⤳⤳未验证之项** | ⛔ 0 主张 `R_ITT` 与 `D_ITT` 是否同一量（承 `5d411ebf07ed` §7 第 5 项之未决）；⛔ 0 主张 `S̄` 面之判死结论（虽已并报，**0 落判死裁决**） |
| 6 | **单模型单 seed 组之不确定性** | 本面为**单模型**（`claude-haiku-5-5`）× 三 seed × **一次**采集；温度 0 下端点非确定之既有发现（`KD-T3-A1` 之同族）**照录** ⇒ 本面读数**含端点非确定成分**，⛔ 0 主张其为端点之确定值 |
| 7 | **`llm_action`/`raw_head` 之载体** | 本棒 cache 与载体逐格载 `raw_head`（前 160 字符）以供阳性对照；**⛔ 0 含任何 key 明文**（key 仅存于 client 内存，R4） |
| 8 | **本件自身之自指限制** | 本件之 bytes／SHA-12 **⛔ 0 自嵌**（自指悖论）⇒ 由**交付面于落盘后直算自报** |

---

**署名**：**mavis（worker）**｜棒 `RITT-REMEASURE`｜2026-10-17 deposon ①段｜**候 PI 核准 · ⛔ 0 径行采认 · ⛔ 0 代裁 PI 面 · ⛔ 0 闭任何既有 `KD` · ⛔ 0 回改任何既有件一字 · ⛔ 0 宣告①毕 · ⛔ 0 落五终判 · ⛔ 0 与轨迹面作任何比较或合并 · key 永不明文（R4）**
