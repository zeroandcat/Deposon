# T1-r2 差异 D-1 勘正件：result JSON 主字段之口径注明 ＋ 下游引用指引修正（勘正注记层 · 2026-10-09）

> **件性质**：**勘正注记件 / 字段口径注释层**（correction sheet）——**只注明口径 ＋ 出引用指引**；⛔ **0 回改既有件任一字**、⛔ **0 改任何数值**、⛔ **0 重跑**、⛔ **0 判定**（不出 PASS/FAIL、**0 赋 `k_*` 布尔**、**0 判档**）、⛔ **0 合并派生 JSON**。
> **授权锚**：PI 2026-10-09 卡 `ask_b77ea3aa0480fc80b5ff3531` 题⑤**逐字**：「**派勘正件（另件承载·0 回改既有件）——注明字段口径并修正下游引用指引**」。
> **被勘正面**：r2 判定件 `9C18B9893579` §6.2 之**差异 D-1**（字段口径性），及其 §10 候呈清单第 **⑤** 项。
> **命名**：`_主题_日期`，⛔ **0 带 V-阶段前缀**（沿 PI 2026-09-29 命名裁 `57024f2cd30a` §1.2）。
> **版式**：UTF-8 无 BOM · LF。**落前实测** `Test-Path=False` ＋ glob 0 命中 ⇒ **0 覆写撞名**。
> **落件时刻**：2026-10-09 21:2x（CST）。⛔ 0 网络、⛔ 0 skill 加载、**R4 key 永不明文**（0 读 0 落盘 0 回显）。
> **本件自身指纹不自写入本件**（由回执自报）。

---

## §0 输入件指纹表（当轮 `Get-FileHash -Algorithm SHA256` 实测 · 落前 L3）

| 角色 | 件 | SHA-12 | bytes | 与派工单声明 |
|---|---|---|---|---|
| **差异登记方（判定件）** | `results/_t1_qwen_temp_sweep_r2_verdict_2026_10_09.md` | `9C18B9893579` | 42,817 | ✅ 一致 |
| **冻结口径件（activation）** | `results/_t1_r2_activation_2026_10_09.md` | `8E59B797AA2D` | 21,111 | ✅ 一致 |
| **r2 执行登记件** | `results/_t1_qwen_temp_sweep_r2_exec_register_2026_10_09.md` | `CF4826A731D6` | 23,681 | ✅ 一致 |
| **r2 result JSON（被注明口径之件）** | `results/_t1_qwen_temp_sweep_r2_result_2026_10_09.json` | `8D6242DA158C` | 58,712 | ✅ 一致 |
| **r2 executor（字段生成源）** | `results/_t1_qwen_temp_sweep_r2_executor_2026_10_09.py` | `38D0CF7FC9BA` | 53,184 | ✅ 一致 |
| **r1 判定件（沿革面 · 0 回改）** | `results/_t1_qwen_temp_sweep_verdict_2026_10_09.md` | `DFC858D3D930` | 21,672 | ✅ 一致 |
| **r1 执行登记件（沿革面 · 0 回改）** | `results/_t1_qwen_temp_sweep_exec_register_2026_10_09.md` | `7AD31E741400` | 17,341 | ✅ 一致 |
| r1 侧读数 JSON（`.tmp/`，沿革面） | `.tmp/_t1_qwen_temp_sweep_readings.json` | `E5E8F024E42E` | 11,013 | 派工单未列，本件补测 |
| r2 records（`.tmp/`，0 读取内容） | `.tmp/_t1_qwen_temp_sweep_r2_records.json` | `BB511E7B0BAF` | 1,795,870 | 派工单未列，本件仅测指纹 |

> 本件**全程只读**上列各件；**0 编译、0 执行** executor；**0 派生新 JSON**。

---

## §1 D-1 事实复述（逐字摘引 · 0 改写）

### §1.1 冻结字面之出处（activation §2.2 逐字）

`results/_t1_r2_activation_2026_10_09.md`（`8E59B797AA2D`）**L80** §2.2「沿 r1 全同项（一字不改，逐项列明）」表内逐字行：

> `| 配对口径 | **same-caption / per-prompt**（沿 r1 判定件 §2.1 口径归位） | ` `DFC858D3D930` §2.1 |`

**配对数之两口径定义**（activation §2.1 表，**L67-68** 逐字）：

> `| 配对数 / 教师 / cell（构造算式） | ` `C(4,2)=6` | ` `C(6,2)=15` | all-pooled 口径 |`
> `| 配对数 / 教师 / cell（same-caption 口径） | ` `2 prompts × C(2,2)=2` | ` `2 prompts × C(3,2)=6` | 冻结主度量口径 |`

⇒ **两口径之定义（件内可核）**：**all-pooled** ＝ 同一教师 6 条 record **全配对** `C(6,2)=15` 对（含 6 对 same-caption ＋ **9 对跨 caption**）；**same-caption** ＝ 每 prompt 内 3 re-asks 两两配对 `2 × C(3,2)=6` 对。

### §1.2 差异本体（r2 判定件 §6.2 逐字）

`9C18B9893579` **§6.2 L278-282**：

> **差异 D-1（口径性 · 需 PI／protocol-keeper 处置）**：activation §2.2 逐字载「配对口径 ｜ **same-caption / per-prompt**（沿 r1 判定件 §2.1 口径归位）」，**然 executor 之 `cell_j_median`／`n_teachers_ge_0_85`／`cell_j_min`／`cell_j_max` 四个对位字段，实际由 `j_median_all`（**all-pooled**）导出**（L839-847：`allm = [x["j_median_all"] ...]` ⇒ `cell_j_median = median(allm)`）。
>
> - **事实层**：r2 result JSON 之**两套读数并存且逐教师齐备**（`j_median_all` 与 `j_median_same_caption` 双列，L829-837 逐字），故**无隐藏、无丢失**；本件 §2.2 之 6 格矩阵即据**双列**独立重算。
> - **风险层**：**逐字登记**——若下游仅读 `cell_j_median` 而不辨其口径，将把 **all-pooled 读数**误当作 **same-caption（冻结主度量）读数**。**此即 r1 判定件 §2.1 所载「执行件主读口径与冻结字面不一致」之同型问题，在 r2 面于「字段命名层」重现**（r1 之问题发生于「执行登记件主读数口径」，r2 之问题发生于「result JSON 主字段口径」）。
> - **⛔ 本件处置**：**如实登记 ＋ 出勘正建议**（见 §8-⑤）——建议**另立勘正棒或经 protocol-keeper 在字段口径注释面处置**，**⛔ 0 由本件改 executor／result 任何一字**（派工单明示「⛔ 0 代裁」）。

**同件 §10 第 ⑤ 项（L357）逐字**：

> | **⑤** | **差异 D-1 之勘正**（`cell_j_median` 系 all-pooled 导出 vs activation §2.2 之 same-caption） | 涉及既有件（executor／result／activation）之一致性处置 | 本件**如实登记 ＋ 出勘正建议**，**⛔ 0 改既有件任一字** |

**同件 §9 限制第 4 项（L341）逐字**：

> 4. **字段口径风险（D-1）已登记未处置**：`cell_j_median` 系 all-pooled 导出，与冻结主度量 same-caption 不同；**本件以双列并存之事实规避，但该风险未消**。

### §1.3 本件之授权与范围（逐字对位）

- PI 卡题⑤所给之处置 ＝ 「**派勘正件（另件承载·0 回改既有件）——注明字段口径并修正下游引用指引**」⇒ 本件**即该勘正件之本体**（另件承载已落实为另立本件）。
- 判定件所请 ＝ 「另立勘正棒或经 protocol-keeper 在**字段口径注释面**处置」⇒ 本件落在**注释面**（§2 口径注明 ＋ §3 引用指引），⛔ **0 落 executor／result 之代码层或 JSON 层**（那属既有件回改，超出题⑤授权）。
- **口径权限边界（如实划明，0 越界）**：PI 已裁者为「`TH_T1_N_MIN` 之『对』如何计数」（`ask_ced8de9fd514ccc30f4e16e2` 题 1，＝ all-pooled，见 r2 判定件 §1.1-1.2）；**该裁 ⛔ 未涉「主度量之 J 配对口径」**——后者沿 r1 判定件 §2.1 归位 ＝ **same-caption**（r2 判定件 L52 逐字明划两面不合并、不互推）。**本件 0 合并两面、0 重裁任一口径**。

---

## §2 字段口径注明（核心 · 逐字段对位 executor 源码行）

> **本节只注明「该字段是哪一口径」与「同口径之值在件内何处」；⛔ 0 改字段名、0 改字段值、0 建议重跑。**

### §2.1 口径 ＝ **all-pooled**（`j_median_all`）之字段清单

**生成处（executor `38D0CF7FC9BA` L839-847 逐字）**：

```python
allm = [x["j_median_all"] for x in per_teacher if x["j_median_all"] is not None]
cells_out.append({
    "cell_idx": ci, "dim": dim, "temperature": temp,
    "n_teachers_with_data": len(allm),
    "cell_j_median": (round(float(statistics.median(allm)), 6) if allm else None),
    "cell_j_min": (round(min(allm), 6) if allm else None),
    "cell_j_max": (round(max(allm), 6) if allm else None),
    "n_teachers_ge_0_85": sum(1 for x in allm if x >= K_N11_3_THRESHOLD),
    "per_teacher": per_teacher,
})
```

| 字段（JSON 路径） | 实为口径 | 生成行 | 量纲与含义（如实注明） |
|---|---|---|---|
| `readings.<口径>.cells[i].cell_j_median` | **all-pooled** | L843-844 | 5 教师之 `j_median_all` 之 **median**（值域 0–1） |
| `readings.<口径>.cells[i].cell_j_min` | **all-pooled** | L845 | 5 教师之 `j_median_all` 之 **min** |
| `readings.<口径>.cells[i].cell_j_max` | **all-pooled** | L846 | 5 教师之 `j_median_all` 之 **max** |
| `readings.<口径>.cells[i].n_teachers_ge_0_85` | **all-pooled** | L847 | 5 教师中 `j_median_all ≥ 0.85` 之**教师计数**（0–5） |
| `readings.<口径>.cells[i].n_teachers_with_data` | **all-pooled（同源派生）** | L842 | `len(allm)`＝**有 `j_median_all` 值之教师数**（非 same-caption 有值之教师数） |
| `readings.<口径>.cells[i].per_teacher[t].n_ge_0_85` | **all-pooled（同源派生）** | L741 | ⛔ **非教师计数**＝该教师 **15 对 all-pooled 配对中 `J ≥ 0.85` 之对数**；字段名易被误读为布尔/教师数，须注口径 |
| `readings.<口径>.cells[i].per_teacher[t].j_median_all` | **all-pooled** | L829-830 | 该教师 15 对之 J 中位（**自带口径后缀**，无歧义） |
| `readings.<口径>.cells[i].per_teacher[t].j_median_nonempty` | **all-pooled 之 nonempty 变体** | L831-832 | 15 对中**双方均非空**之对之 J 中位（r2 面 `n_pairs_empty_empty=0`，故与 `j_median_all` 同值） |

> **口径分数之二（本件须注明之第二重）**：`readings` 之键名（`full_reply` / `content_only` / `reasoning_only`）＝ **度量对象口径**（`text_of`，L703-708），**与配对口径（all-pooled vs same-caption）是两个独立维度**。引用任一 cell 读数时**两个维度都须注明**。
> **字段语义之如实注明（⛔ 0 另立差异编号）**：上表末二行（`n_teachers_with_data`／`per_teacher[].n_ge_0_85`）之同源派生事实系**本件核查所见**，r2 判定件 §6.2 之 D-1 明列者为**四个 cell 级对位字段**；本件按 D-1 同一派生源（`allm` / `jvs_all`）一并注明，**是否另立差异编号由 PI 裁**，本件 **0 自行立项**。

### §2.2 口径 ＝ **same-caption**（冻结主度量）之值在件内何处

| 需求 | 件内位置 | 可核性 |
|---|---|---|
| **逐教师** same-caption J 中位 | `readings.<度量对象口径>.cells[i].per_teacher[t].j_median_same_caption`（executor L833-834 落盘） | ✅ **r2 result JSON 内已有**，逐教师齐备（**当轮实测：`j_median_same_caption` 键 90 处 ＝ 3 度量口径 × 6 cells × 5 教师；`j_median_cross_caption` 亦 90 处**） |
| **cell 级** same-caption J 中位 | ⛔ **JSON 内无该字段** | ⚠️ **JSON 只存逐教师值，0 存 cell 级聚合** ⇒ 下游若需 cell 级同口径值，**须自 5 教师值取 median**，或直接引 r2 判定件 §2.2 之 6 格矩阵（该矩阵即据双列独立重算，`9C18B9893579` L85-90） |
| **cell 级** same-caption `≥0.85` 教师计数 | ⛔ **JSON 内无该字段** | ⚠️ 同上，须自算或引判定件 §2.2 之逐格结论（L94-96） |
| 逐教师 same-caption 对数（分母） | ⛔ JSON `per_teacher` 未落 `n_pairs_same`／`n_pairs_cross`（executor L740 之 `n_pairs_same`／`n_pairs_cross` **未进 JSON**） | ⚠️ 分母只能引 **activation §2.1 表（L68）＝ `2 prompts × C(3,2)=6`**，或 executor L740 之源码 |

> ⇒ **本节之实质结论（供下游一眼定位）**：**r2 result JSON 之「主字段」`cell_j_median` 系 all-pooled；同口径（same-caption）之值在 `per_teacher[].j_median_same_caption`，且 cell 级聚合在件内不存在。**

### §2.3 两口径差例 ①：`full_reply`（r2 派工面主用度量对象）

**当轮当件实测**（自 `8D6242DA158C` 逐教师双列独立重算；**与 r2 判定件 §2.2 L85-90 所载 6 格逐格一致，0 差异**——此为**复核**，⛔ 非改数）：

| cell | 维度/温度 | `cell_j_median`（**all-pooled**，件内主字段） | same-caption cell 中位（据 `j_median_same_caption` 重算） | 差（同口径 − all-pooled） | same-caption 之 `≥0.85` 教师数 |
|---|---|---|---|---|---|
| 0 | L2 / 0.0 | 0.231198 | **0.286391** | +0.055193 | 0 / 5 |
| 1 | L2 / 0.3 | 0.250575 | **0.546404** | +0.295829 | 0 / 5 |
| 2 | L2 / 0.5 | 0.292754 | **0.516551** | +0.223797 | 0 / 5 |
| 3 | L14 / 0.0 | 0.236364 | **0.610371** | +0.374007 | 0 / 5 |
| 4 | L14 / 0.3 | 0.159453 | **0.253848** | +0.094395 | 0 / 5 |
| 5 | L14 / 0.5 | 0.246269 | **0.532056** | +0.285787 | 0 / 5 |

**方向性事实（0 软化）**：**all-pooled 逐格系统性低于 same-caption**（r2 判定件 §3.3 替代读法一 L146 逐字已述「主读法各格高出 0.055–0.394」，与本表逐格差值一致）；根因 ＝ all-pooled 之 15 对中含 **9 对跨 caption 配对**，跨题零重叠拉低中位。**⛔ 两口径之 `≥0.85` 教师数在 `full_reply` 口径下逐格皆 0，故该口径之阈值结论不因口径错读而翻转**（此为如实限定，非为淡化风险）。

### §2.4 两口径差例 ②：`content_only`（**读数方向之反转示例 · 最尖锐之风险实例**）

| cell | 维度/温度 | `cell_j_median`（**all-pooled**，件内主字段） | same-caption cell 中位 | **若误读之后果（如实指出）** |
|---|---|---|---|---|
| 0 | L2 / 0.0 | **0.0** | **1.0** | 同 cell 两口径**分处阈值两侧** |
| 1 | L2 / 0.3 | **0.0** | **1.0** | 同上 |
| 2 | L2 / 0.5 | **0.0** | **1.0** | 同上 |
| 3 | L14 / 0.0 | **0.0** | **1.0** | 同上 |
| 4 | L14 / 0.3 | **0.0** | **1.0** | 同上 |
| 5 | L14 / 0.5 | **0.0** | **0.65** | 同上 |

- **`n_teachers_ge_0_85` 之对位差**：all-pooled 口径下 **6/6 cells 皆 0**；same-caption 口径下逐 cell 教师数 ＝ **5／4／3／3／3／1**（当轮实测，据 `j_median_same_caption ≥ 0.85` 计）。
- ⇒ **风险之具体形态**：若下游仅引件内主字段 `cell_j_median`／`n_teachers_ge_0_85` 而不注口径，则「same-caption 下 5/6 cells 教师 J 中位 ≥ 0.85」这一**存在且可核**之读数，将被读成「6/6 cells 全 0.0、0 教师达阈」——**结论方向完全反转**。
- ⛔ **本件 0 以该差例支撑任何 `content_only` 结论**：沿 r2 判定件 §2.3（L98 起）／§3.3 替代读法二（L148），`content_only` 系 **r1 残段口径**（`content_len` 中位 3 字符、互异 22/180），**已列非主用**；本表仅为**口径错读之风险演示**，⛔ 0 由此主张「教师在完整语义上高度一致」，⛔ 0 由此改变 r2 之任何裁定。

---

## §3 下游引用指引（**7 条 · 可直接照抄之引用句式**）

> **指引之效力面**：本节约束**任何下游件（论文面／上传面／成果清单／汇报面／派生 JSON 之说明段）对 r2 result JSON 字段之引用**。**引字段名而不注口径 ＝ 违反本指引**。

**G-1 · 引 `cell_j_median`（件内主字段）时**——须写：
> 「r2 `full_reply`／**all-pooled 口径**（每教师 6 records 全配对 `C(6,2)=15` 对，含 9 对跨 caption）之 cell 教师 J 中位 ＝ X」

**G-2 · 引 same-caption（冻结主度量）之 cell 值时**——须写：
> 「r2 `full_reply`／**same-caption 口径**（`2 prompts × C(3,2)=6` 对/教师，activation §2.2 冻结主度量）之 cell 教师 J 中位 ＝ X（取 `per_teacher[].j_median_same_caption` 之 median；cell 级聚合为**本件／判定件依双列所算**，result JSON 内**无**该字段）」

**G-3 · 引 `cell_j_min`／`cell_j_max` 时**——须写：
> 「all-pooled 口径下 5 教师 `j_median_all` 之 min／max ＝ …」

**G-4 · 引 `n_teachers_ge_0_85` 时**——须写：
> 「**all-pooled 口径**下 `j_median_all ≥ 0.85` 之教师数 ＝ X／5」；若所指为 same-caption，**须另计并注明「same-caption 口径、逐 cell X／5（自算／引判定件 §2.2）」**。

**G-5 · 引 `per_teacher[].n_ge_0_85` 时**——须写：
> 「该教师 **15 对 all-pooled 配对中 `J ≥ 0.85` 之对数** ＝ X（⛔ 非教师计数、⛔ 非布尔）」。

**G-6 · 引 `n_teachers_with_data` 时**——须写：
> 「有 `j_median_all` 值之教师数 ＝ 5（all-pooled 侧计）」。

**G-7 · 禁式（三条，⛔ 0 书）**：
> ⛔ 禁写「`cell_j_median` 即 same-caption／冻结主度量读数」——它**不是**；
> ⛔ 禁写「r2 温度敏感性 J 读数 ＝ X」而不注**度量对象口径**（`full_reply`／`content_only`／`reasoning_only`）**与**配对口径（all-pooled／same-caption）**两重**；
> ⛔ 禁把 `content_only` 之读数作主用口径引用（r2 判定件 §2.3 已列非主用），亦⛔ 禁据 `content_only` 断言语义一致性。

> **最小合规范式（整句照抄）**：「r2 `readings.full_reply.cells[i].cell_j_median` ＝ X，该字段为 **all-pooled 配对口径**；**冻结主度量之 same-caption 口径**同 cell 值 ＝ Y（口径注明见 `_t1_r2_d1_field_caliber_correction_2026_10_09.md` §2-§3）。」

---

## §4 r1 同类错位之沿革（如实 · **0 回改**）

| 层 | r1（`DFC858D3D930`／`7AD31E741400`） | r2（`9C18B9893579`／`8D6242DA158C`） |
|---|---|---|
| **错位发生层** | **执行登记件主读数口径层** | **result JSON 主字段命名层** |
| **错位字面（逐字）** | r1 判定件 L110：「**两读法分歧**源于**口径选择**（同 caption 配对 vs 全部 6 对配对），**根源是执行件主读口径与冻结字面（per-prompt 配对）不一致**」 | r2 判定件 §6.2 L281：「此即 r1 判定件 §2.1 所载『执行件主读口径与冻结字面不一致』之**同型问题**，在 r2 面于『**字段命名层**』重现」 |
| **登记件是否标口径** | ✅ §3.1 标题**逐字带口径**：「**主读数（all-pooled · per cell × per teacher）**」；同件 §3.2 另设 same/cross 拆解表（same-caption J ＝ 0.75／1.0／1.0／1.0／0.0／0.25） | ✅ 登记件 §5.3 标题**逐字带字段名**：「cell 教师 J 中位（**`j_median_all`**，6 cells × 5 教师）」——**口径有标** |
| **JSON 层是否并存双口径** | ❌ **无**。r1 读数 JSON `E5E8F024E42E` 字段为 `cell_j_median_5teachers`／`j_median`／`j_median_nonempty`／`n_ge_0_85`(bool)，**当轮实测 `same_caption` 键 0 处、`j_median_all` 0 处** ⇒ **同口径值不在 JSON 内**（只在登记件 §3.2 表与判定件重算） | ⚠️ **有**。r2 result JSON **并存** `j_median_all` ＋ `j_median_same_caption` ＋ `j_median_cross_caption`（各 90 处），**无隐藏、无丢失**；⛔ **然 cell 级主字段名仍不携带口径后缀**（`cell_j_median` 而非 `cell_j_median_same_caption`） |
| **r2 是否已修 r1 之同型错位** | — | **⛔ 未修**：r1 之同型错位（主字段名／主读口径不带配对口径标识）在 r2 **仍存**，仅**位置**由「登记件正文层」移至「JSON 字段名层」 |

**沿革之如实结论（1 句）**：**r1 与 r2 同源、同根（all-pooled 混入跨 caption 配对），且 r1→r2 之间「JSON 存双列」这一半有改善（0 处→各 90 处），而「主字段名不注口径」这一半未改善**；r2 判定件 §6.2 已逐字登记此同型性。

**0 回改**：本节所涉 r1 判定件 `DFC858D3D930`（21,672 B）、r1 登记件 `7AD31E741400`（17,341 B）、r1 读数 JSON `E5E8F024E42E`（11,013 B）**全程只读**，§5 落毕复测一字未变；**r1 之「假证伪族」与「不明」之记载保持历史真实，r2 之修正不追认 r1**（沿 r2 判定件 §8 外推禁令）。

---

## §5 0 回改确认（落前／落毕双测 · SHA-12 + bytes）

### §5.1 落前实测（见 §0，本件写作前）

### §5.2 落毕复测（本件落盘后当轮实测）

| 件 | 落前 SHA-12 / bytes | 落毕 SHA-12 / bytes | 结论 |
|---|---|---|---|
| `_t1_qwen_temp_sweep_r2_executor_2026_10_09.py` | `38D0CF7FC9BA` / 53,184 | `38D0CF7FC9BA` / 53,184 | ✅ 一字未变 |
| `_t1_qwen_temp_sweep_r2_result_2026_10_09.json` | `8D6242DA158C` / 58,712 | `8D6242DA158C` / 58,712 | ✅ 一字未变 |
| `_t1_qwen_temp_sweep_r2_exec_register_2026_10_09.md` | `CF4826A731D6` / 23,681 | `CF4826A731D6` / 23,681 | ✅ 一字未变 |
| `_t1_qwen_temp_sweep_r2_verdict_2026_10_09.md` | `9C18B9893579` / 42,817 | `9C18B9893579` / 42,817 | ✅ 一字未变 |
| `_t1_r2_activation_2026_10_09.md` | `8E59B797AA2D` / 21,111 | `8E59B797AA2D` / 21,111 | ✅ 一字未变 |
| `_t1_qwen_temp_sweep_verdict_2026_10_09.md`（r1） | `DFC858D3D930` / 21,672 | `DFC858D3D930` / 21,672 | ✅ 一字未变 |
| `_t1_qwen_temp_sweep_exec_register_2026_10_09.md`（r1） | `7AD31E741400` / 17,341 | `7AD31E741400` / 17,341 | ✅ 一字未变 |
| `.tmp/_t1_qwen_temp_sweep_readings.json`（r1） | `E5E8F024E42E` / 11,013 | `E5E8F024E42E` / 11,013 | ✅ 一字未变 |
| `.tmp/_t1_qwen_temp_sweep_r2_records.json` | `BB511E7B0BAF` / 1,795,870 | `BB511E7B0BAF` / 1,795,870 | ✅ 一字未变 |

**⇒ 9 件落前落毕 SHA-12 与字节数逐件一致，⛔ 0 回改既有件任一字。**

### §5.3 本件 0 做之面（逐项）

⛔ **0 回改** executor／result／register／verdict／activation／r1 各件任一字 ｜ ⛔ **0 改任何数值**（§2.3-2.4 之差例系**当轮独立重算之复核**，与判定件 §2.2 逐格一致，⛔ 非改数）｜ ⛔ **0 重跑**（0 编译、0 执行、0 新增 API call）｜ ⛔ **0 判定／0 判档／0 赋 `k_*` 布尔** ｜ ⛔ **0 合并派生 JSON** ｜ ⛔ **0 改阈值**（`0.85`／`0.05`／`20`／`10`／`500` 一字沿用）｜ ⛔ **0 读 key 值** ｜ ⛔ **0 触 `frozen`** ｜ ⛔ **0 触 V1–V3 资产** ｜ ⛔ **0 网络** ｜ ⛔ **0 skill 加载** ｜ ⛔ **0 阶段名自升** ｜ ⛔ **0 编造**文献号／法条号／SHA。

---

## §6 诚实限制（不老实的，本件 0 做）

1. **⛔ 本件未消除 D-1 之根因**：executor 之 `cell_j_median` 等字段**仍系 all-pooled 导出**，本件**只在注释面**（§2-§3）注明与指引；**风险本体（字段名不带口径）仍在**（沿 r2 判定件 §9 第 4 项「该风险未消」）。**根因处置（改字段名／改生成式／重跑）⛔ 属既有件回改，超出题⑤授权，本件 0 越界**；其裁归 PI／protocol-keeper。
2. **同口径 cell 级值在 result JSON 内不存在**（§2.2）：下游若只持有 JSON，**须自算或引判定件 §2.2**；本件⛔ 0 派生新 JSON 以补该缺口（R5 禁派生）。
3. **`n_teachers_with_data`／`per_teacher[].n_ge_0_85` 之同源派生**系本件核查所见、r2 判定件 D-1 未列举（§2.1 末注）；本件**已注明、不另立差异编号**；**是否另立由 PI 裁**，本件 0 自行立项、0 隐匿该观察。
4. **`content_only` 差例（§2.4）之方向反转系风险演示，非结论支持**：沿 r2 判定件 §2.3／§3.3，该口径**已列非主用**；本件⛔ 0 由此主张任何命题方向，⛔ 0 改变 r2 之 `K-T1-S1`＝`hit=False`、`K-T1-S3`＝「不明」、根因三分类之任何一档。
5. **r1 侧只能核至 JSON 层**：`results/` 内**无 r1 executor 源件**（仅 `.tmp/_t1_qwen_temp_sweep_readings.json`），故 §4 之 r1 行为**据 JSON 字段实测 ＋ 登记件／判定件逐字**；⛔ 本件未对 r1 之字段生成式作源码级复核（无可核件，**如实登记此核验缺口**）。
6. **`n_pairs_same`／`n_pairs_cross` 未落 JSON**（executor L740 有、JSON 无）⇒ same-caption 之分母只能引 activation §2.1；本件⛔ 0 推断其值（仅引 activation `2 × C(3,2)=6` 之字面）。
7. **本件不属判定链**：沿 r2 判定件 §10 尾「入链仍须 verifier 签字 ＋ PI 复核」体例，**本件之生效亦须 PI 复核**；本件⛔ 0 自封终裁、⛔ 0 视本件为对 D-1 之「已处置」之宣告。
8. **本件 0 处置之他面**：**D-2**（activation 指纹过期／留痕时序）、温度轴有效性面、`K-T1-R1-1` 门禁面、`K-T1-S3` 判「不明」面、r1 遗留候呈项（`C-1`／`C-5`）——**均不在题⑤授权面内，本件 0 触及、0 复裁**。

---

## §7 纪律自证

- ⛔ **0 回改既有件**：§5 双测表 9 件 SHA-12 与字节逐件一致。
- ⛔ **0 撞名**：落前 `Test-Path=False` ＋ glob 0 命中；本件为**另立新件**。
- ⛔ **0 编造**：全部 SHA-12／bytes／字段值／行号／键计数均**当轮实测或当轮独立重算**（§0／§2.1／§2.2／§4／§5.2）；引用既有件处**逐字摘引并给出件名与行号**。
- ⛔ **0 网络**；⛔ **0 skill 加载**；⛔ **0 读 key 值**（R4 key 永不明文：0 读取、0 落盘、0 回显、0 入 prompt／log）。
- ⛔ **0 阶段名自升**：本件名 ＝ `_主题_日期`，⛔ 0 V-前缀（PI 2026-09-29 命名裁 `57024f2cd30a` §1.2）。
- ⛔ **0 软化**：§2.4 之方向反转风险、§6 之 8 项限制**均直书**，⛔ 0 以「但／然而」类措辞掩盖。
- **版式**：UTF-8 无 BOM · LF；**SHA-12 口径 ＝ `sha256(全文字节)` 前 12 位大写十六进制**（沿 T1/r2 各件实测体例）；**本件自身指纹不自写入本件**。

---

> **本件止于注释与指引。** D-1 之事实未变（`cell_j_median`／`n_teachers_ge_0_85`／`cell_j_min`／`cell_j_max` 仍系 **all-pooled** 导出，与 activation §2.2 冻结之 **same-caption** 主度量口径不同）；本件新增者**仅**为「该字段是哪一口径」之逐字段注明（§2）与「引用时须写之句式」之 7 条指引（§3），**外加 r1→r2 同型错位之沿革如实登记（§4，0 回改）**。**0 改数、0 重跑、0 判档、0 回改既有件。** 本件生效须 PI 复核。