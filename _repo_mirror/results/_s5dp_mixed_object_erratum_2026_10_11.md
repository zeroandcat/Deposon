# `mixed_object` 之勘正（第三域五线读数件 `839fb5452578` 之登记面错误）—— 🔴 **勘正另立件 · 原件 0 回改 · ⛔ 不改一字**

> 📌 **状态栏（贯穿全件）**：🔴 **勘正面成立** —— `results/_s5doubleprime_five_lines_readings_2026_10_11.json`（`839fb5452578`）之 `model_side_declaration.mixed_object` ＝ **`false`**，经独立 verifier 自跑自核，**应然值 ＝ `true`** ⇒ 该字段系**登记错误**（字面不符），**⛔ 非「该面无产物」之义**（⛔ 0 与 `af`／artifact-free 混读）｜ ⛔ **0 回改原 JSON 一字** ｜ ⛔ **0 合并派生 JSON** ｜ ⛔ **0 改其余任何字段** ｜ ⛔ **0 改 `model_side_declaration` 之他项** ｜ ⛔ **0 宣告 `K-RJ-10` 闭／开**（闭宣告归 verdict-keeper／PI） ｜ ⛔ **0 复核 `nw_sim`／`nled_sim` 之计算实体**（verifier 已判读数面 PASS · 不重做） ｜ ⛔ 0 网络／0 skill／0 LLM

---

## §0 一句话结论

独立 verifier（棒 `bg_6443169f` · 2026-10-11）以 `importlib` 只读加载第三域五线 runner 并自跑自核，**99 项检查 97 项逐位相符**，独余 `mixed_object` 一项 **MISMATCH** —— 📌 **实测实质 ＝ `true`**，而该 JSON 载 `false` 且其 `mixed_object_note` 与**同块内** `model_tree` ＝ `"V3"` **相抵触** ⇒ 🔴 **本件为该字段之勘正面**（原 JSON 0 回改、0 派生合并）。

---

## §1 被勘正之对象

| **项** | **内容** |
| --- | --- |
| **被勘正件** | `results/_s5doubleprime_five_lines_readings_2026_10_11.json` |
| **SHA-12** | `839fb5452578`（16,099 B · 无 BOM · LF） |
| **被勘正字段** | `model_side_declaration.mixed_object` ＝ **`false`**（原件所载） |
| **连带之字面不符** | `model_side_declaration.mixed_object_note`（「本面 gold 与 model 皆 `V3.1` 同词表口径下之纯 `V3.1` 面」）—— 与**同块内** `model_tree` ＝ `"V3"` 相抵触 |
| **勘正面** | `model_side_declaration.mixed_object` **应然值 ＝ `true`**；其 `note` 之「纯 V3.1 面」表述**不成立** |

---

## §2 核定之依据（逐条照录 verifier 自跑自核之结论）

| **#** | **依据** | **内容** |
| --- | --- | --- |
| **①** | **gold 侧之实体** | gold 侧 ＝ `KEYWORDS_V3 ⊎ 15 词`（**278 词**；`V3` ＝ 263 词；**0 删 0 改层**）—— 系 `V3.1` 之扩面 |
| **②** | **model 侧之实体** | model 侧 ＝ `KEYWORDS_V3` —— 训练标签源、树、`n_keywords_hit` 特征源**三者皆 V3**（executor L578 逐字 `for jt, kws in KEYWORDS_V3.items()`；runner L274／L281） |
| **③** | **两轴不同 ⇒ 实质 mixed** | gold 侧 ≠ model 侧 ⇒ **`mixed_object` ＝ `true`** |
| **④** | **同块自相抵触** | 该 JSON 同块内 `model_tree` ＝ `"V3"`、`training_label_kwtable` ＝ `"KEYWORDS_V3"`、`n_keywords_hit_feature_kwtable` ＝ `"KEYWORDS_V3"` —— **与 `note` 之「皆 V3.1 同词表口径之纯 V3.1 面」直接抵触** |
| **⑤** | **行为旁证（26 件逐件之实迹）** | `nw_v31 ≠ nw_v3` 有 **5** 件 ｜ `nled_v31 ≠ nled_v3` 有 **1** 件 —— 正系 gold 轴扩为 `V3.1` 之实迹，与「纯 V3.1 面」之表述不合 |
| **⑥** | **冻结条文（判死线本体）** | `04495ef4b343` §3-1 之 `K-RJ-10` 行：`mixed_object` ＝ **`true`**（构造 ＝ `V3.1` gold × `V3` model ⇒ 差值含 gold 覆盖扩大之机械效应，**0 可归因于学习能力变化**；该声明**逐件必附且逐字沿用**，⛔ 0 省略／软化，不达标判停）—— ⛔ **本体 0 回改一字** |
| **⑦** | **旧域同型之核定（先例）** | `1c8ce58d6484` §4-3 已核定**应然值 ＝ `true`**，并载：旧域 `65a9b9be6327` 之同类 `false` 亦系**字面不符**，**0 与「该面无产物」之义混读**；其处置列 `O-5` 归 verifier／doc-writer（**另立勘正件**，⛔ 0 回改既有 JSON／md、⛔ 0 合并派生 JSON）—— 📌 **本件即 `O-5` 之同型于第三域之落** |
| **⑧** | **旧域声明件之旁证** | `fa74831fa0ad` §2.1（第二域 X5 三行声明 · `mixed_object` ＝ **`true`**）—— 旧域声明件亦为 `true` |
| **⑨** | **第三域终判件之预断** | `bba3b889d849` §4-1 ②（🟡 **实质成立、声明件缺** ＋ ⛔ **0 存在**第三域之 X5 **声明件**）—— 其 ⛔ 明示「**0 断言第三域之 `mixed_object` 字段值**（归 **verifier**）」⇒ 📌 **本件即其所派之兑现** |

---

## §3 勘正之内容（**本件 0 执行 0 改写原 JSON**）

### §3-1 应然值

> `results/_s5doubleprime_five_lines_readings_2026_10_11.json` 之 `model_side_declaration.mixed_object` ＝ **`true`**（原件载 `false` ⇦ **字面不符**）。

### §3-2 其 `mixed_object_note` 应改述为（如实拟，⛔ 0 视为已执行）

> 「本面 gold 侧 ＝ `KEYWORDS_V3 ⊎ 15 词`（`V3.1` 扩面），model 侧／训练标签／`n_keywords_hit` 特征源三者**皆 `KEYWORDS_V3`** ⇒ **两轴不同** ⇒ 本面**为 mixed 构造面**；其与**纯 `V3.1` 面**之别已在同块 `model_tree` ＝ `"V3"` 字段载明。」

### §3-3 ⛔ 本件 0 作之事项

① ⛔ **0 回改**原 JSON（`839fb5452578`）任一字｜② ⛔ **0 合并派生 JSON**｜③ ⛔ **0 改** `model_side_declaration` 之**其余任何字段**（`gold_kwtable`／`model_tree`／`training_label_kwtable`／`n_keywords_hit_feature_kwtable`／`K_EX-8` 皆 0 触）｜④ ⛔ **0 复核** `nw_sim`／`nled_sim` 之计算实体｜⑤ ⛔ **0 宣告**该 JSON 之其他字段之对错｜⑥ ⛔ **0 宣告 `K-RJ-10` 闭／开**｜⑦ ⛔ **0 以本件作为任何条之闭／开之依据**（本件系**登记面勘正**，⛔ 非判定面）。

---

## §4 关联登记（⛔ 0 就其状态作裁）

| **条** | **在册状态（照录）** | **与本件之关系** | **⛔ 边界** |
| --- | --- | --- | --- |
| **`K-RJ-10`** | `f52231807e36` §3-11 判**维持挂账**（域内**无 `S5″` 随件声明面** ＋ **无五线面**） | 本件勘正其**声明面之应然值**；其**随件声明面**之四要件之落齐由**另一棒（worker · `bg_076dbd5e`）**出件 | ⛔ **0 宣告闭** ｜ ⛔ **0 就其条件之成就与否作判**（归 verdict-keeper／PI） |
| **`S5″`（编号归属）** | 卡面 R-2 以 `S5″` 指**第三域五线面**；`bba3b889d849` §4-1 以 `S5″` 指**`S5′` 之对应件（随件声明面）** | **同形异指** —— 本件如实登记 | ⛔ **0 就编号归属作裁**（归 PI／protocol） |
| **`R-4`／`O-5`** | `1c8ce58d6484` §4-3 列 `O-5`（旧域 `65a9b9be6327` 之同类字面不符） | 本件系**同型于第三域**之落；旧域之 `O-5` **仍独立存续** | ⛔ **0 就旧域 `O-5` 之闭／开作判**（归 verifier／doc-writer） |

---

## §5 输入链（自报实测；SHA-12／bytes 为本轮实测，非沿用他件转引值）

| **件** | **角色** | **SHA-12** | **bytes** | **备注** |
| --- | --- | --- | --- | --- |
| `results/_s5doubleprime_five_lines_readings_2026_10_11.json` | **被勘正件** | `839fb5452578` | 16,099 | 本轮实测；无 BOM · LF（CRLF ＝ 0） |
| `results/_s5doubleprime_five_lines_runner_2026_10_11.py` | 该读数件之执行体（只读） | `9de3c08e3863` | 31,138 | 本轮实测；无 BOM · LF |
| `.tmp/_s5dp_run_stdout_2026_10_11.txt` | 本轮运行日志 | — | — | 供比对 |
| `results/_v4_pi_cot_v3_ruleset_v3_executor.py` | 唯一实现源（`n_keywords_hit` 特征码本 ＝ `KEYWORDS_V3`） | `8a81d90c69ba` | 58,794 | 本轮实测；⛔ 0 改 |
| 独立 verifier 棒 | `bg_6443169f`（verifier 面 · 自跑自核 · 99 项 97 项逐位相符） | — | — | 本件之核定来源 |

---

*件止。parent（deposon 链主 · 本轮亲办）· 2026-10-11 · `mixed_object`（第三域五线读数件 `839fb5452578`）之**勘正另立件** —— 应然值 ＝ **`true`**（gold 侧 `KEYWORDS_V3 ⊎ 15 词` × model 侧／训练标签／特征码本三者 `KEYWORDS_V3` ⇒ 两轴不同）；原 JSON ⛔ **0 回改**、⛔ **0 合并派生 JSON**、⛔ 0 改其余字段、⛔ 0 复核读数实体、⛔ **0 宣告 `K-RJ-10` 闭／开**、⛔ **0 以本件作为任何闭／开之依据**、⛔ 0 就 `S5″` 编号归属作裁（卡面／终判件**同形异指** · 如实登记）｜核定为独立 verifier 棒 `bg_6443169f` 兑现 `bba3b889d849` §4-1 ② 之「归 verifier」之派）·*
