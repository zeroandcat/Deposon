# `T3_Trap@seed42` 三不复现键之**定向复跑与核因** · 实验执行件（2026-10-16 · **候选 PI 核准**）

| 项 | 值 |
| :-- | :-- |
| **件名** | `results/_t3_repro_probe_2026_10_16.md` |
| **棒 ID** | **`T3-REPRO-PROBE`**（deposon ①段 · PI 第十四批 Q2 裁之执行 · 实验执行棒） |
| **件性质** | **实验执行件 · 核因面 ＋ 复现性判定面**（⛔ 0 代 PI 裁·释·择·确认·给值｜⛔ 0 回改任何既有件一字｜⛔ 0 移动／重命名／删除） |
| **落盘方** | **worker**（实验执行棒） |
| **状态** | **已落盘 · 候 PI 核准**（⛔ **0 径行采认**） |
| **授权链** | PI 2026-10-16 22:4x 卡 `ask_ecf6aaf3901b4a99544203ec`（Q2 · 选项 id `q2_5a9a2057_opt1`）逐字（经派工单转述）：**「T3 复现性：另派 worker 棒对 3 个不复现键做定向复跑核因（预算 100 calls 内）」** |
| **本件不宣告** | ⛔ **0 宣告①毕** · ⛔ **0 落五终判**（`pass`／`af`／`kd`／`fail`／`give-up` 之外之语汇**0 充终判**）· ⛔ 0 宣告 `T3` prompt 面变更已授权 · ⛔ 0 宣告 `spec L32` 之 V0 撤回 · ⛔ 0 宣告任何开口面之闭 · ⛔ 0 宣告既有读数面作废 |
| **本棒实发 LLM calls** | **45 格全成**（3 键 × `H_face` 15）＋ **1 次端点 probe**；**attempt 实耗 47**（含 1 次传输重试）· **硬闸 100 未触**（余 53） |
| **本棒写入既有件** | **0 件**（仅新建本件 ＋ `.tmp\` 下 4 个实测面） |

> 📌 **本件之一级结论（先于一切读数）**：**3 个不复现键之归因已闭合至「第四层漂移」**——轨迹面所用 harness 为 **`7a097d7802d1`**（＝第四层之 OLD），第四层漂移 `edf98dc7da62` 将其改为 **`d5c8d676bb5b`**，其登记之 hunk `C_T3_clues` 载「`T3` 型数 3 → 15（＋正解实算表 `t3_answer`）」。本棒以**层间直接重放**排除第五层：`T3` 面于口径 B 下 **L4 digest ≡ L5 digest**（三 seed 全等）⇒ **第五层（`d07d33f0eb82`，T2 改裁 (b)）0 改变 `T3` 面**。
>
> 🔴 **同时如实报告一项与在册结论相悖之实测**：ε 网格件 `f8de4abb5e12` §5 之「**45 键中 42 键与轨迹面逐字相符**、3 键不符」，其比较面**仅为逐面首 prompt 之 `correct` 字面（15 prompt 中取 1）**。本棒以**全面 digest** ＋**逐 prompt `correct`** 两面复测，得 **`T3` 面 26/45 失配、全部五族合计 131/240 失配、15 面之全面 digest 仅 3/15 相符（惟 `T1` 三 seed）**。⇒ **「42/45 复现」系弱比较面之产物，不成立为面级复现结论**（详见 §4、§6-2、§7 `KD-T3RP-2`）。

---

## §0 纪律总则（照录 · 全文适用）

1. **FTFB（判读线先于实验）**：判读线冻结件 `.tmp/t3_repro_probe_ftfb_freeze_2026_10_16.json`（**`44761c404b86`**／2,936 B）**于本棒首 call 之前**落盘（§5-1 自证时序）；判读线三线（`L1` 构造面／`L2` 读数面／`L3` 层间隔离面）**全部为机械判据**，⛔ **0 新拟数值阈值**。
2. **⛔ 0 回改**：源件（ε 网格件、两份漂移登记件、三 seed 实测件与其 jsonl、冻结件、口径声明件）、`tools/exp_harness.py`、`tools/distortion_calculator.py` —— **全为只读**；本件所载之一切结论均为**另立登记**。
3. **⛔ 0 宣告①毕 ／ ⛔ 0 落五终判**：本件仅作**观测与核因**登记；终判权属 verdict-keeper，PI 裁定权属 PI。
4. **key 面（R4）**：token 仅自 env 读入 runner 对象内部；⛔ **0 打印／0 落盘／0 入日志／0 入本件／0 入回执**；落盘前经 **5 类** key 形态扫描实测 **0 命中**（§8）。
5. **可比性前置**：复跑须与轨迹面**同 treatment** 方可比（端点 host／model／`max_tokens`／`temperature`／system 模板／`parse_choice` 规则／`TRIES`），七项逐项照录并实测相符（§5-2）。
6. **阴性结论三重自审**：凡「0 命中／0 相符／未复现」之断，均经**独立重算 ＋ 反向抽样核对 ＋ 源件回读**三重核（各断之三重核记录见对应节）。

---

## §1 源件回读（逐字 · 本棒**直算指纹** · ⛔ 0 凭派工单转述或他件自报落笔）

### §1-1 源件实测指纹（`hashlib.sha256(磁盘全文字节)[:12]`，本棒落笔前直算）

| # | 件（仓库相对路径） | **本棒实测 SHA-12** | **bytes** | 本棒取用面 |
| :-: | :-- | :-: | --: | :-- |
| 1 | `tools/exp_harness.py` | **`026575ff3829`** | **41,428** | 现值（第五层 NEW）· 15 面 prompt 生成（**只读导入**） |
| 2 | `.tmp/t2b_harness_pre_change_snapshot_2026_10_16.py` | **`d5c8d676bb5b`** | **36,217** | 第四层 NEW 快照（层间隔离之对照臂 · **只读导入**） |
| 3 | `.tmp/three_seed_measurement_2026_10_16.json` | **`ff5ed4b0e329`** | **226,256** | 轨迹面读数 45 行 ＋ **`detail` 720 条逐 prompt `correct`/`llm_action`** |
| 4 | `.tmp/three_seed_llm_calls_2026_10_16.jsonl` | **`5a8cbcf85aa7`** | **104,288** | **720 行**逐 call 留痕（`raw_head` 在档） |
| 5 | `.tmp/three_seed_freeze_2026_10_16.json` | **`46260e3b8426`** | **10,536** | 🔴 **轨迹面↔harness 版绑定之一手源**（§3-1） |
| 6 | `results/_ge01_epsilon_grid_exec_register_2026_10_16.md` | **`f8de4abb5e12`** | **45,389** | `KD-GE01-EPS-4` 之在册表述（**只读**） |
| 7 | `results/_material_expansion_drift_authorized_register_2026_10_16.md` | **`edf98dc7da62`** | **15,044** | **第四层**漂移登记件（hunk `C_T3_clues` 之出处） |
| 8 | `results/_t2_path_b_drift_authorized_register_2026_10_16.md` | **`d07d33f0eb82`** | **10,939** | **第五层**漂移登记件（T2 改裁 (b)） |
| 9 | `.tmp/t3_repro_probe_ftfb_freeze_2026_10_16.json` | **`44761c404b86`** | **2,936** | **本棒判读线冻结件**（临时面 · 非锚载体） |
| 10 | `.tmp/t3_repro_probe_measure_2026_10_16.json` | **`31779f66c051`** | **9,137** | 本棒复跑读数面 |
| 11 | `.tmp/t3_repro_probe_llm_calls_2026_10_16.jsonl` | **`54ad4d2cd8bf`** | **7,441** | 本棒复跑 **45 行**逐 call 留痕 |

> ✅ **指纹纪律**：上表 11 项**全部为本棒落笔前直算**，⛔ **0 沿用他件自报**。第 1／3／4 项与 ε 网格件 §1-1 之在册值**逐位吻合**（`026575ff3829`／`ff5ed4b0e329`／`5a8cbcf85aa7`）；第 2 项与第四层登记件 §4 所载 NEW 值**逐位吻合**（`d5c8d676bb5b`／36,217 B）。
>
> ⚠ **轨迹面所用 harness 指纹之可得性**：`ff5ed4b0e329` **本身不自载** harness 指纹字段（实测 0 命中 `harness`／`7a097d78`／`026575ff`）；其**冻结件 `46260e3b8426`** 之 `asset_pre_measurement` 逐字载 `tools/exp_harness.py` 之 `sha256_12` ＝ **`7a097d7802d1`**、`mtime` ＝ `2026-10-15T17:17:49`。本件之轨迹面↔版绑定**以此冻结件为源**，非以 ε 网格件之转述为源。

### §1-2 全仓指纹扫描：`7a097d7802d1` 之盘上可得性

本棒对 `results`／`tools`／`docs`／`.tmp`／`corpus`／`scripts`／`verifier`／`tests`／`reviews`／`deposon_team`／`paper`／`attacks`／`letters` 共 **2,700 件**逐件直算 `sha256[:12]`：

| 目标指纹 | 语义 | 盘上命中 |
| :-- | :-- | --: |
| `7a097d7802d1` | **轨迹面所用 harness**（第四层 OLD） | **0 件**（🔴 实体已不可得） |
| `026575ff3829` | 现值 harness（第五层 NEW） | 1 件（`tools/exp_harness.py`） |
| `d5c8d676bb5b` | 第四层 NEW | 2 件（`.tmp/` 两份快照） |
| `ff5ed4b0e329`／`5a8cbcf85aa7`／`46260e3b8426` | 轨迹面 json／jsonl／冻结件 | 各 1 件 |
| `edf98dc7da62`／`d07d33f0eb82` | 第四／五层漂移登记件 | 各 1 件 |

⇒ **轨迹面之 harness 实体不在盘** ⇒ **「漂移前后 prompt 面之逐字对照」中「漂移前」一侧无法以实体取得**（`KD-T3RP-1`）。本棒之归因遂以**层间 digest 重放**替代实体逐字对照（§3-2、§4-1）。

---

## §2 三不复现键之锁定（逐键辨析）

### §2-1 在册表述之逐字回读（ε 网格件 `f8de4abb5e12`）

| 位 | 逐字 |
| :-- | :-- |
| §8 `KD-GE01-EPS-4` | 「**`T3` prompt 面已变**｜本棒重算 `T3_Trap@seed42` 之首 prompt `correct ＝ Option A`，轨迹面为 `Option B`（45 键中 3 键不符，均属该格·seed）」 |
| §5 | 「**prompt 面可复现性实测**｜逐 `seed×族×机制` 首 prompt 之 `correct` 字面：**45 键中 42 键与轨迹面逐字相符**；**3 键不符**（`T3_Trap@seed42` 之 `M1`／`M2`／`M3`：本棒重算得 `Option A`、轨迹面为 `Option B`）」 |

### §2-2 三键之逐键锁定（本棒实测 · `ff5ed4b0e329` 之 `detail` 720 条一手记录）

`detail` 逐条载 `(seed, mechanism, cell_id, correct, llm_action, rule, tries, err, flag_A_not_in_K)`；`cell_id` 形如 `T3_Trap#00`。三键之 `#00` 格逐键真值（M1 臂取 `correct`，因 prompt 面与机制无关）：

| 键 | 格 | **轨迹面 `correct`** | 轨迹面 `llm_action`（三臂各自） | 现件再生 `correct` | 在册判定 | 本棒复核 |
| :-- | :-- | :-: | :-- | :-: | :-- | :-- |
| `42\|M1_Deposon_TRA\|T3_Trap` | `#00` | **`Option B`** | `Option B` | **`Option A`** | 不符 | ✅ **不符（在册所述获本棒复现）** |
| `42\|M2_Greedy\|T3_Trap` | `#00` | **`Option B`** | `Option B` | **`Option A`** | 不符 | ✅ **不符** |
| `42\|M3_Random\|T3_Trap` | `#00` | **`Option B`** | `Option B` | **`Option A`** | 不符 | ✅ **不符** |

**`T3@seed42` 逐 prompt `correct` 全序列（轨迹面 vs 现件，本棒实测）**：

| 面 | `#00`–`#14` 之 `correct`（`B`＝`Option B`，`A`＝`Option A`） |
| :-- | :-- |
| **轨迹面** | `B A A B B B A B A A A B A B A` |
| **现件（`026575ff3829`）** | `A B B A A A A A B A B B A B A` |
| 逐格符/不符 | `X X X X X X . X X . X X . X .` ⇒ **9/15 不符** |

> 📌 **如实在册表述之外补充（如实并列 · ⛔ 0 调和）**：在册 `KD-GE01-EPS-4` 之「45 键中 3 键不符」之**键**（3 个 `M×T×seed` 键）**属实且经本棒复现**；惟其**所据之比较面（首 prompt 1/15）**不足以支撑面级复现结论——同一格·seed 之其余 **14 格中另 8 格亦不符**（§4-2）。本棒**0 回改该件一字**，仅作另立登记。

---

## §3 核因面：归因

### §3-1 归因之前提（两段链，逐字照录 · ⛔ 0 转述）

**(甲) 轨迹面所用 harness ＝ `7a097d7802d1`（一手源）**——`.tmp/three_seed_freeze_2026_10_16.json`（`46260e3b8426`）逐字：

```
frozen_at: 2026-10-16T10:58:59.000090+08:00
frozen_by: mavis (worker) · 三 seed 补测棒（v19 Q2 派生动作 A）
asset_pre_measurement:
  tools/exp_harness.py:  { "sha256_12": "7a097d7802d1",
                           "mtime": "2026-10-15T17:17:49.278559+08:00",
                           "note": "含 V0.3 补造 T5 与 V0.4 T3 可答化两面之漂移（0.4 系授权面）" }
```

**(乙) `7a097d7802d1` ＝ 第四层漂移之 OLD**——`edf98dc7da62` §1-2 逐字：

| 项 | OLD | NEW |
| :-- | :-: | :-: |
| **sha-256（`[:12]`）** | **`7a097d7802d1`** | **`d5c8d676bb5b`** |
| **bytes** | 15,708 | 36,217（**+20509**） |
| **`T3` 型数** | **3** | **15**（＋正解实算表 `t3_answer`） |
| hunk `C_T3_clues` | `cf22f72eaebb` / 546 B / 8 行 | `b913b9910f29` / 4,205 B / 55 行（＋3,659） |

⇒ **两段链接合 ⇒ `T3` prompt 面之变动的发生层 ＝ 第四层**（`7a097d7802d1` → `d5c8d676bb5b`）。

### §3-2 层间隔离实测（排除第五层 · 本棒直接重放）

以盘上第四层 NEW 快照 `d5c8d676bb5b` 与现件 `026575ff3829`，在**口径 B**（单一 seed 依 `task_families` 之序逐族顺序生成）下逐族逐 seed 重生其面，取 `digest12 ＝ sha256(json.dumps(prompts, ensure_ascii=False, sort_keys=True).encode("utf-8"))[:12]`（**该式经轨迹面 `T1@42` 之 `45b6f507342b` 反推验证命中**，见 §4-1）：

| 族 | seed | L4 `digest12` | L5 `digest12` | 轨迹面 `digest12` | **L4 ≡ L5？** | 轨迹 ≡ L5？ |
| :-- | --: | :-: | :-: | :-: | :-: | :-: |
| `T1_GSM8K` | 42 | `45b6f507342b` | `45b6f507342b` | `45b6f507342b` | ✅ **是** | ✅ 是 |
| `T1_GSM8K` | 123 | `d4a3c7dcc854` | `d4a3c7dcc854` | `d4a3c7dcc854` | ✅ **是** | ✅ 是 |
| `T1_GSM8K` | 456 | `8fcb322f32e8` | `8fcb322f32e8` | `8fcb322f32e8` | ✅ **是** | ✅ 是 |
| `T2_StrategyQA` | 42 | `b296ae770e62` | `6e7f28636cd6` | `95211b66b16c` | ❌ 否 | ❌ 否 |
| `T2_StrategyQA` | 123 | `ec0893125504` | `b1e943be0eaf` | `a7323715dcd0` | ❌ 否 | ❌ 否 |
| `T2_StrategyQA` | 456 | `f8848a451474` | `3980a6c92562` | `e87861f31936` | ❌ 否 | ❌ 否 |
| **`T3_Trap`** | **42** | **`8d98c9599173`** | **`8d98c9599173`** | **`68dc2160aff4`** | ✅ **是** | ❌ 否 |
| **`T3_Trap`** | **123** | **`d2d6075b46b3`** | **`d2d6075b46b3`** | **`420381d7ea4e`** | ✅ **是** | ❌ 否 |
| **`T3_Trap`** | **456** | **`a7815223e822`** | **`a7815223e822`** | **`4e093712b425`** | ✅ **是** | ❌ 否 |
| `T4_2x2` | 42／123／456 | `46814328820f` | `46814328820f` | `2a642c8c12e1` | ✅ **是** | ❌ 否 |
| `T5_LowResource` | 42 | `968434db52dd` | `968434db52dd` | `dcde34fe38f8` | ✅ **是** | ❌ 否 |
| `T5_LowResource` | 123 | `c7d7dda7991b` | `c7d7dda7991b` | `c43997640732` | ✅ **是** | ❌ 否 |
| `T5_LowResource` | 456 | `e443e6b89dd1` | `e443e6b89dd1` | `a10e1e7f8a2f` | ✅ **是** | ❌ 否 |

**判读（`L3` 线 · 机械判据，0 新拟阈值）**：

1. **`T3` 面于第五层 0 变动**（三 seed 之 L4 ≡ L5，**逐位相等**）⇒ **第五层（`d07d33f0eb82`，T2 改裁 (b)）经实测排除**为 `T3` 面变动之原因（与该登记件 §2-2「`docstring`／`T1`／`T3`／`T4`／`T5` **0 字节变更**」之自述**相符**）。
2. **`T2` 面于第五层已变**（三 seed 之 L4 ≠ L5）⇒ 与该登记件 §2-2 之 `A_T2_online_table_and_note`／`B_T2_reason_compression` 两 hunk **相符**。
3. **`T4`／`T5`／`T3` 之轨迹 ≠ L4** ⇒ 三者之面变动均发生于**第四层或更早**；第四层登记件 §1-2 逐字载其 hunk 为 `C_T3_clues`／`D_T4_games`／`E_T5_scenarios` ⇒ **与第四层登记相符**。

### §3-3 变动之机理（逐字 · 现件 `T3_Trap.generate_prompts` 之 RNG 面）

现件（`026575ff3829`）`tools/exp_harness.py:459-463` 逐字：

```python
        for i in range(n):
            trap = random.choice(sorted(t3_answer))
            options = ['Option A', 'Option B']
            correct = t3_answer[trap]
            random.shuffle(options)
```

第四层将 `t3_answer` 之键集由 **3**（`greedy`／`deposit`／`cost`）扩为 **15**（另增 12 型），并新增独立正解表 `t3_answer`（`tools/exp_harness.py:450-458`，15 项）。**机理**：

- `random.choice` 内部为 `_randbelow(len(seq))`；`len` 由 3 → 15 时，所需位宽 `k ＝ n.bit_length()` 由 **2 → 4**，拒绝概率由 **1/4 → 1/16** ⇒ **同一 RNG 状态下取到之索引 r 之分布与映射整体改变**。
- `sorted(t3_answer)` 之键序亦随之改变（3 键序 `['cost','deposit','greedy']` → 15 键序 `['compounding','cost','cost-rev','deposit','deposit-rev','discount','flat-vs-bonus','guarantee','greedy','greedy-fee','greedy-rev','hidden-carry','negative-both','resource-drain','spend-now']`）⇒ **即使 r 相同，所取之 `trap` 亦不同**。
- 拒绝环之消费差异使 **RNG 流位置随迭代漂移** ⇒ **不止首格，其后各格亦随之全变**（实测：首格不符外，另 8/15 格不符，§2-2）。
- `t3_answer` 之正解映射本身亦改（新增 12 型之正解为实算登记）⇒ **`correct` 之取值来源亦变**。

**⇒ 归因结论（`T3@seed42` 三键）**：

| 候选归因 | 判定 | 依据 |
| :-- | :-- | :-: |
| **素材池/构造表变化所致（第四层 `C_T3_clues`）** | ✅ **成立** | §3-1 两段链 ＋ §3-2 之 L4≡L5 ＋ §3-3 之 RNG 机理 ＋ §4-2 逐 prompt 失配 |
| **第五层（`T2` 改裁 (b)）所致** | ❌ **排除** | §3-2：`T3` 面 L4 ≡ L5（三 seed 逐位相等） |
| **`T2` 素材池 4→39 之 RNG 级联所致** | ❌ **排除（构造性）** | `T2_StrategyQA.generate_prompts` 以 `k = i % pool`（**不由池大小取随机**）＋ 逐 prompt **恰好一次** `random.shuffle(options)`（4 元）⇒ 池大小 4→39 **0 改变 RNG 抽取次数**；`T1` 为逐 prompt 恰 2 次 `random.randint` × 15 ⇒ **`T3` 入场 RNG 态跨五层不变**（T4／T5 于 T3 之后生成，**不可回溯影响** `T3`） |
| **随机性（seed 面）所致** | ❌ **排除** | 同 seed 之 `T3` 面在 L4 与 L5 **逐位相等**（`8d98c9599173`）；若为随机性，同 seed 同版本应可复现，而 L4／L5 之等值证明**抽取本身稳定**；且 `T1` 三 seed 全面 digest **3/3 复现**（§4-1）⇒ 种子与 RNG 流机制无恙 |

---

## §4 复现性实测（面级 · 本棒直算）

### §4-1 全面 digest 面（15 面）

- **digest 式之反推验证**：以 7 种候选式于 `T1@42` 上试比，**唯一命中**轨迹面在册值 `45b6f507342b` 者为 `sha256(json.dumps(prompts, ensure_ascii=False, sort_keys=True).encode("utf-8"))[:12]` ⇒ **本棒全表皆用此式**（⛔ 0 沿用他件之未验证式）。

| 族 | seed 42 | seed 123 | seed 456 | **面级结论** |
| :-- | :-: | :-: | :-: | :-- |
| `T1_GSM8K` | ✅ 符 | ✅ 符 | ✅ 符 | **3/3 全面复现** |
| `T2_StrategyQA` | ❌ | ❌ | ❌ | **0/3** |
| `T3_Trap` | ❌ | ❌ | ❌ | **0/3** |
| `T4_2x2` | ❌ | ❌ | ❌ | **0/3**（三 seed 同 digest `2a642c8c12e1` ⇒ 轨迹面之 `T4` 与 seed 无关） |
| `T5_LowResource` | ❌ | ❌ | ❌ | **0/3** |
| **合计** | —— | —— | —— | **3/15 全面 digest 相符（仅 `T1`）** |

### §4-2 逐 prompt `correct` 面（240 prompt · 轨迹面 `detail` 一手真值 vs 现件再生）

| 族 | 失配／总数（逐 prompt `correct`） | 失配率 |
| :-- | :-: | --: |
| `T1_GSM8K` | **0 / 45** | **0.0%** |
| `T2_StrategyQA` | **18 / 45** | 40.0% |
| **`T3_Trap`** | **26 / 45** | **57.8%** |
| `T4_2x2` | **42 / 45** | 93.3% |
| `T5_LowResource` | **45 / 60** | 75.0% |
| **合计** | **131 / 240** | **54.6%** |

**`T3` 逐 seed 明细**：seed 42 ⇒ **9/15** 失配；seed 123 ⇒ **9/15** 失配；seed 456 ⇒ **8/15** 失配。

### §4-3 阴性结论之三重自审（`3/15` 全面 digest 之「不符」）

1. **独立重算**：以第四层快照 `d5c8d676bb5b` 另臂重算 15 面 digest，与现件臂逐位比对 —— 二者在 `T1`/`T3`/`T4`/`T5` 逐位相等、于 `T2` 逐位不等 ⇒ **现件臂之结果非单次抽样波动**（同一 RNG 态下两版产出确定）。
2. **反向抽样核对**：取 `T1` 三 seed（**唯一复现族**）逐 prompt `correct` 复核 ⇒ **45/45 全符**，证明比对式、索引口径（`cell_id` 形如 `T1_GSM8K#00`）、族序、`n_decisions`（`T1`–`T4` 15／`T5` 20）**皆无错** ⇒ **其余四族之失配非比对口径所致**。
3. **源件回读**：`ff5ed4b0e329` 之 `detail` 720 条为逐 prompt 一手记录（`cell_id`＋`correct`＋`llm_action` 三字段齐备），非摘要；已逐条抽样回读并与本棒重生值对照 ⇒ **轨迹面真值非他件转述**。

⇒ **`3/15` 全面 digest 之断，三重自审通过；非口径错、非抽样波动、非转述误差。**

---

## §5 定向复跑（3 键 × `H_face` 15 ＝ 45 格）

### §5-1 FTFB 时序自证（判读线冻结**先于**首 call）

| 序 | 事件 | 证据 |
| :-: | :-- | :-- |
| 1 | 判读线冻结件落盘 | `.tmp/t3_repro_probe_ftfb_freeze_2026_10_16.json` ／ **`44761c404b86`** ／ 2,936 B ／ `BOM=False`、`CR=0` |
| 2 | 冻结件写入后**方**构造 runner 并首调端点 | runner 内首行网络行为为 probe；probe 记录于 `.tmp/t3_repro_probe_measure_2026_10_16.json` 之 `probe` 字段 |
| 3 | 冻结件被复跑读数面**回引** | 复跑读数面 `ftfb_sha12` ＝ `44761c404b86`（与冻结件直算值逐位一致）⇒ **冻结先于测量** |

**判读线三线（照录冻结件 · 0 新拟阈值）**：`L1` 构造面（逐 cell `correct` 与现件再生面全等）／`L2` 读数面（逐 cell `R_ITT` 与轨迹面并报）／`L3` 层间隔离面（L4 ≡ L5 digest）。

### §5-2 treatment 七项照录与实测相符（可比性前置）

| 项 | 轨迹面在册值（照录 `.tmp/klm41_3_ts_collect_2026_10_16.py` L56-L60／L110-L139 逐字） | 本棒复跑实测 |
| :-- | :-- | :-: |
| 端点 host | `api.teamorouter.cn` | ✅ `api.teamorouter.cn` |
| model | `claude-haiku-5-5` | ✅ `claude-haiku-5-5` |
| `max_tokens` | 48 | ✅ 48 |
| `temperature` | 0 | ✅ 0 |
| system 模板 | `You must choose exactly one option from: %s. Respond with ONLY the option text, no explanation. Do not introduce yourself.` | ✅ 逐字相同 |
| 解析规则 | `EXACT` → `TAIL_LAST`(尾 60 字末命中) → `FULL_LAST`(全文末命中) → `EMPTY`／`NOMATCH` | ✅ 逐字相同 |
| `TRIES`／`timeout` | 3 ／ 60 s | ✅ 3 ／ 60 s |

**端点 probe（先于批量 · 1 call）**：`ok=True`、`rule=EXACT`、`raw_head`＝`Option A` ⇒ **端点面可用**（实测为准）。

### §5-3 `L1` 构造面（先于 LLM 之纯构造检验）

`T3@seed42` 现件再生面 `digest12` ＝ **`8d98c9599173`**（＝ §3-2 之 L5 值，与 L4 逐位相等）；逐 cell `correct` 15 项已列 §2-2。

### §5-4 预算账（硬闸 100）

| 项 | 值 |
| :-- | --: |
| 计划格数 | 45（3 键 × 15） |
| 实成格数 | **45 / 45**（0 格缺） |
| **attempt 实耗**（含重试） | **47** |
| 端点 probe | 1（计入上项） |
| 传输重试 | 1（`tries>1` 者 1 条） |
| **硬闸** | **100** |
| **闸余** | **53** |
| **闸触发** | **0**（`budget_stop` 记录 0 条） |
| **err 记录** | **0** |
| 解析规则分布 | `EXACT` 44 ／ `EMPTY` 1 |

### §5-5 `L2` 读数面（逐格并报 · 如实）

**逐格 `llm_action` 之复跑值 vs 轨迹面值（`SAME`／`DIFF`）**：

| 格 | `M1_Deposon_TRA` | `M2_Greedy` | `M3_Random` |
| :-- | :-- | :-- | :-- |
| `T3_Trap#00` | DIFF `B→A` | DIFF `B→A` | DIFF `B→A` |
| `T3_Trap#01` | SAME `A→A` | DIFF `A→B` | DIFF `A→B` |
| `T3_Trap#02` | DIFF `A→B` | DIFF `A→B` | DIFF `A→B`（复跑 `EMPTY`⇒`None`） |
| `T3_Trap#03` | DIFF `B→A` | SAME `B→B` | DIFF `B→A` |
| `T3_Trap#04` | SAME `A→A` | DIFF `B→A` | SAME `A→A` |
| `T3_Trap#05` | DIFF `A→B` | DIFF `B→A` | DIFF `B→A` |
| `T3_Trap#06` | SAME `A→A` | SAME `A→A` | SAME `A→A` |
| `T3_Trap#07` | DIFF `B→A` | SAME `A→A` | DIFF `B→A` |
| `T3_Trap#08` | DIFF `A→B` | SAME `B→B` | DIFF `A→B` |
| `T3_Trap#09` | SAME `A→A` | SAME `A→A` | SAME `A→A` |
| `T3_Trap#10` | DIFF `A→B` | DIFF `A→B` | DIFF `A→B` |
| `T3_Trap#11` | SAME `B→B` | SAME `B→B` | SAME `B→B` |
| `T3_Trap#12` | SAME `A→A` | DIFF `A→B` | SAME `A→A` |
| `T3_Trap#13` | DIFF `A→B` | DIFF `A→B` | SAME `B→B` |
| `T3_Trap#14` | SAME `A→A` | SAME `A→A` | SAME `A→A` |
| **同/异计** | **8 SAME / 7 DIFF** | **7 SAME / 8 DIFF** | **6 SAME / 9 DIFF** |

⇒ **逐格 `llm_action` 一致率 ＝ 21/45（46.7%）**。

**⚠ `R_ITT` 之可比性（如实 · 关键登记）**：轨迹面 `T3@seed42` 三键之 `R_ITT` 逐字为 `M1`＝`1/5`、`M2`＝`1/5`、`M3`＝`1/15`（`ff5ed4b0e329` 之 `rows`，⛔ 0 改一字）。**本棒 ⛔ 0 复算复跑之 `R_ITT`** —— 缘由：`R_ITT` 之定义式为 **`arm_choice_t ∈ K_t`** 之比率，而 `arm_choice` 系机制臂之变换产物（`DeposonMechanism.choose` 以 `random.random()` 加权抽样、`RandomMechanism.choose` 为 `random.choice`；`tools/exp_harness.py:107-164`），**该变换消费与 prompt 生成同一全局 RNG 流**。轨迹面之 RNG 态由**盘上不可得**之 harness `7a097d7802d1` 决定 ⇒ **轨迹面之 `R_ITT` 不可由本棒以现件复算** ⇒ 复跑之 `R_ITT` 与轨迹面之 `R_ITT` **0 可比**（`KD-T3RP-4`）。本棒**以逐格 `llm_action` 为形式可比之最小面**并报（`temperature=0` 下同面重发之服务端非确定性亦可见于 24/45 之 DIFF，但因**面已不同**，**不可将 DIFF 归因于随机性**）。

---

## §6 结论面

### §6-1 复现性之判定（`T3@seed42` 三键）

| 判据 | 结果 | 读法 |
| :-- | :-- | :-- |
| **归因** | **第四层漂移 `edf98dc7da62` 之 hunk `C_T3_clues`（`T3` 型数 3→15 ＋新增正解表 `t3_answer`）** | §3-1 两段链（一手源）＋ §3-2 层间隔离（L4 ≡ L5 三 seed 逐位相等）＋ §3-3 RNG 机理 |
| **第五层** | **实测排除** | `T3` 面 L4 ≡ L5 |
| **`T3` 面级复现性** | **0/3 全面 digest 相符；逐 prompt `correct` 26/45 失配（57.8%）** | §4-1、§4-2 |
| **三键（`#00` 格）** | **3/3 与轨迹面不符**（轨迹 `Option B` ／ 现件 `Option A`） | §2-2（**在册 `KD-GE01-EPS-4` 所述获复现**） |
| **复跑之读数** | **逐格 `llm_action` 一致 21/45**；`R_ITT` **0 可比** | §5-5 |
| **随机性之排除** | 成立 | §3-3 之随机性行 |

### §6-2 对既有读数面之影响评估（如实）

**(甲) 三键（`T3@seed42` × `M1`／`M2`／`M3`）之既有读数**：

- 轨迹面该 3 格之 `llm_action` 均为 `Option B`，而该面之 `correct` 亦为 `Option B` ⇒ **该 3 格之 `flag_A_not_in_K` ＝ 0**（答对）。
- 现件面之 `correct` 为 `Option A`；复跑以现件面所得 3 格之 `llm_action` 均为 `Option A` ⇒ **复跑之该 3 格答对**（相对现件面）。
- ⇒ **「该 3 格答对」这一事实于两面皆成立，但因 `correct` 之定义已变，其在面间 0 可传递**；**既有读数不可与复跑读数直接相减或相除**。

**(乙) 污染面之广度（如实 · 比在册更广）**：

| 面 | 既有读数是否因 prompt 面漂移而**不可比** |
| :-- | :-- |
| `T1_GSM8K`（全 45 prompt） | ✅ **可比**（0 失配，全面 digest 3/3 复现） |
| `T2_StrategyQA` | 🔴 **不可比**（18/45 `correct` 失配；且第五层另加 `reason` 面变动） |
| **`T3_Trap`** | 🔴 **不可比**（**26/45** `correct` 失配） |
| `T4_2x2` | 🔴 **不可比**（42/45 失配；`Mixed` 哨兵致 `options` 长度 2→3） |
| `T5_LowResource` | 🔴 **不可比**（45/60 失配） |

⇒ **既有三 seed 读数面之不可比范围为 5 族中 4 族（`T2`／`T3`／`T4`／`T5`），非仅 `T3`**。本棒**仅作登记，⛔ 0 宣告作废**（作废/重测之宣告权属 PI／verdict-keeper）。

**(丙) 与在册之相悖（如实并列 · ⛔ 0 调和 · ⛔ 0 回改）**：ε 网格件 `f8de4abb5e12` §5 之「42/45 复现、3 键不符」在**其自陈之比较面（首 prompt 之 `correct`）**上**成立且经本棒复现**；惟本棒以**全面 digest** 与**逐 prompt `correct`** 两面复测，得 `T3` **26/45** 失配、**131/240** 合计失配。⇒ **该件之「`T3` prompt 面已变」之断成立**；其**复现率数字所据之比较面过窄**，不足以支撑面级复现率之表述。本棒**0 改该件一字**，列 `KD-T3RP-2` 候裁。

**(丁) 对 §2-1 之在册结论之影响评估**：`KD-GE01-EPS-4` 之「与 `KD-GE01-EPS-1` 同源」之归属**成立**（同一 harness 漂移链）。惟其**范围**应自「`T3` prompt 面已变」**升格为**「`T2`／`T3`／`T4`／`T5` 四族之 prompt 面均已变，`T1` 未变」（本棒为**建议**，⛔ 0 代裁）。

---

## §7 `KD` 清单（如实列 · 候 PI 裁 · 本棒 **0 裁 0 闭**）

| # | `KD` | 内容 | 状态 | 归属 |
| :-: | :-- | :-- | :-: | :-- |
| **`KD-T3RP-1`** | **轨迹面之 harness 实体不在盘** | `7a097d7802d1`／15,708 B 之全仓指纹扫描 **0 命中**（2,700 件）⇒ 「漂移前 prompt 面」之**逐字实体对照不可得**；本棒归因遂以**层间 digest 重放**替代 | **新开** | PI／protocol-keeper |
| **`KD-T3RP-2`** | **在册「42/45 复现」之比较面过窄** | ε 网格件 `f8de4abb5e12` §5 之复现率仅据**首 prompt（15 中取 1）** 之 `correct` 字面；本棒两面复测得 **全面 digest 3/15 相符**、**逐 prompt `correct` 131/240 失配（`T3` 26/45）** ⇒ 该件之「`T3` prompt 面已变」之断成立，**其复现率表述不足以支撑面级结论**（⛔ 0 回改该件一字） | **新开**（**候选升格 `KD-GE01-EPS-4` 之射程**） | PI |
| **`KD-T3RP-3`** | **第四层登记件之 hunk 级指纹不可复现** | `edf98dc7da62` §1-2 所载 `C_T3_clues` NEW（`b913b9910f29`／4,205 B／55 行）**无法**以字节窗穷举（0 命中）或行片（最接近 4,433 B／`70a87cd5022e`）复现 ⇒ **file 级指纹全部可复现，hunk 级指纹之计算口径与本棒所用口径不符**（口径未载于该件） | **新开** | protocol-keeper |
| **`KD-T3RP-4`** | **`R_ITT` 之轨迹值不可复算** | `R_ITT` 系机制臂变换量（消费与 prompt 生成同一 RNG 流）；轨迹面 RNG 态由盘上不可得之 `7a097d7802d1` 决定 ⇒ **本棒 0 复算轨迹 `R_ITT`**、复跑 `R_ITT` 与之 **0 可比**（仅并报逐格 `llm_action`） | **新开** | PI／verdict-keeper |
| **`KD-T3RP-5`** | **`T3` 面变动之层内归属之细分不可得** | 归因已闭合至「**第四层**」（两段链闭合）；惟第四层 6 hunk 中 `C_T3_clues` 为 `T3` 唯一相关 hunk 之**归属来自该登记件之自述**，本棒**仅实测「L4 ≡ L5」与「轨迹 ≠ L4」**，⛔ 0 逐 hunk 归因（`C_T3_clues` 之实体字面不在盘） | **新开**（口径限定，非免责） | protocol-keeper |
| **`KD-T3RP-6`** | **`T2` 族面于第五层另有一变** | `T2` 全面 digest 之 L4 ≠ L5（三 seed）⇒ `T2` 面**两次**变动（第四层池 4→39、第五层 `reason` 压缩）⇒ `T2` 之可比性缺口**双源**，非单源 | **新开** | PI |
| **`KD-GE01-EPS-4`**（在册承继） | `T3` prompt 面已变 | 本棒**独立复现**其所述三键之不符 | **承继**（**本棒未回改一字**） | 与 `KD-GE01-EPS-1` 同源 |
| **`KD-GE01-EPS-1`**（在册承继） | harness 锚漂移 | 本棒复测其指纹对比成立（`7a097d7802d1` **0 在盘** ／ 现值 `026575ff3829`）；**0 宣告 V0 撤回** | **承继** | PI／protocol-keeper |
| **`KD-MQ04-5`**（在册承继） | `options` 长度于 `T3`（2）与 `T4`（2/3）不符 spec §3.1 | 本棒实测复核（`T3` 恒 2、`T4` 三 seed 同 digest）；**0 新裁** | **承继** | verdict-keeper |
| **`KD-3`**（在册承继） | `T3_Trap` 欠定格 | 本件 **0 触** | **承继** | PI（另议件） |

---

## §8 字节属性与 key 形态扫描（内容无关 · 恒真）

| 项 | 期望 | 实测 |
| :-- | :-- | :-- |
| BOM | `False` | `False` |
| CRLF 数 | `0` | `0` |
| 孤立 CR 数 | `0` | `0` |
| TAB 数 | `0` | `0` |
| 控制字符（除 `\n`）数 | `0` | `0` |
| 非 ASCII 字符数 | `>0` | `>0` |
| `U+FFFD`（替换字符，以 `chr(0xFFFD)` 构造）数 | `0` | `0` |
| 末字符 | `\n` | `\n` |
| 换行风格 | 纯 `\n`（LF） | 纯 `\n`（LF） |

**key 形态扫描**：本件落盘后经 **5 类** key 形态扫描（⛔ **0 将扫描项字面写入本件正文**）⇒ **0 命中**。本棒 token 仅自 env 读入 runner 对象内部，⛔ 0 打印／0 落盘／0 入本件／0 入复跑 jsonl／0 入回执。

**⚠ 自指悖论**（沿体例先例 `edf98dc7da62` §5 之同一口径）：本件**不自写入**自身 SHA-12／bytes（填入即改本件内容 ⇒ 其指纹随之变）⇒ 该二项之**盘上实测值载于交付回执**。

---

## §9 本件明确不宣告之面（照录）

⛔ **0 宣告①毕** · ⛔ **0 落五终判**（`pass`／`af`／`kd`／`fail`／`give-up` 之外之语汇 0 充终判；本件所列 `KD` 系**候裁清单之条目名**，非本棒所落之终判）· ⛔ 0 宣告 `T3` prompt 面变更已授权 · ⛔ 0 宣告 `spec L32` 之「全 V0 撤回」是否触发 · ⛔ 0 宣告既有读数面作废 · ⛔ 0 宣告任何开口面之闭 · ⛔ 0 代 PI 裁 · ⛔ 0 回改任何既有件一字 · ⛔ 0 就地改任何锚 JSON · ⛔ 0 移动／重命名／删除任何件 · ⛔ 0 上传。

---

## §10 一句话交付

**`T3_Trap@seed42` 三不复现键之归因已闭合至第四层漂移**（`edf98dc7da62` 之 hunk `C_T3_clues`：`T3` 型数 3→15 ＋新增正解表 `t3_answer`；轨迹面所用 harness 之 `7a097d7802d1` 经一手源冻结件 `46260e3b8426` 确认 ＝ 该层 OLD）；**第五层经层间 digest 重放实测排除**（`T3` 面 L4 ≡ L5，三 seed 逐位相等）；`T2` 池 4→39 之 RNG 级联与随机性两候选**均排除**（`T2` 以 `k=i%pool` 取样、池大小 0 改 RNG 抽取次数；同 seed 下 L4 ≡ L5 且 `T1` 三 seed 全面复现）。**定向复跑 45 格全成、attempt 实耗 47（硬闸 100 未触、0 err）**；三键 `#00` 格之 `llm_action` 复现面一致，逐格一致率 21/45，`R_ITT` 因轨迹 RNG 态不可得而 **0 可比**。🔴 **同时如实报告**：`T3` 面之实测失配为 **26/45 逐 prompt**（非在册之 3/45 —— 在册之 3 键之断**本身成立**，惟其比较面仅为 15 中取 1），且 **`T2`／`T4`／`T5` 三族之 prompt 面同样不可复现**（合计 **131/240** 失配），故既有读数面之不可比范围为**五族中四族**。**候 PI 核准 · ⛔ 0 径行采认 · ⛔ 0 回改任何既有件 · ⛔ 0 宣告①毕 · ⛔ 0 落五终判。**

---

*件止。**实验执行件（T3 复现性定向复跑与核因）**（worker · 实验执行棒）· 2026-10-16 deposon ①段。*
*授权面：PI 第十四批 Q2 卡 `ask_ecf6aaf3901b4a99544203ec`（选项 id `q2_5a9a2057_opt1`）· 经派工单转述。*
*配对实测面（临时面 · 非锚载体）：`.tmp/t3_repro_probe_ftfb_freeze_2026_10_16.json`（`44761c404b86`）／`.tmp/t3_repro_probe_measure_2026_10_16.json`（`31779f66c051`）／`.tmp/t3_repro_probe_llm_calls_2026_10_16.jsonl`（`54ad4d2cd8bf`）。*
