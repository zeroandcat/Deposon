# S4 面域 · **`source_wave` canonical 映射入册**（协议面修订／登记件 · 出口 **6-2**／**AD-8-fix** 落实）· protocol-keeper · 2026-10-10

- **件性质**：**协议面之修订／登记件（可复现性缺口闭合 · 文档面入册）** —— 将 executor `8a81d90c69ba` 之 `provenance_wave_map`（**canonical 映射**）**逐字转录入册**，并**首次给出**「21 件 addendum × wave」之完整对照表与**分步复现路径**，使面 II 之 **24 件**之语料面**可复现**。⛔ **0 判档**（0 出 `pass`／`af`／`kd`／`fail`／`give-up` 五终判之一）｜⛔ **0 代裁**｜⛔ **0 回改任何既有件**（R5：frozen 只追加）｜⛔ **0 改任何阈值／门柱／判死线**｜⛔ **0 跑 executor／0 跑 runner／0 真重建**｜⛔ **0 改任何产出物 JSON**（**本修订系文档面入册**，⛔ 0 径补 `_provenance`／`source_wave` 入 `6f020c03e52c`）
- **授权锚**：PI 2026-10-10「轮 55」卡 `ask_843b65b50a873462f8a56e80` —— **AD-8-fix 答 ＝ 甲「核准（派 protocol-keeper 另立修订件）」**（答于 **17:40:50.668 +0800**，据 `_questionnaire_cards_intake_register_supplement_8_2026_10_10.md` 之活库账目实测：建卡 **17:38:36.526 +0800**、`answered_at` ＝ **17:40:50.668 +0800**，与派工单所载时点**逐项相符**）
- **⚠ 照录来源声明（如实 · 非漏报）**：PI「轮 55」卡之**选项全文未落盘于本仓** —— 本棒全仓检索该卡号**命中 2 件**，经核**均非卡面原件**：① `_s4_corpus_scope_hard_constraint_judgment_2026_10_10.md`（**`c7609657dfe4`**）§行 4–5 系**另一棒就出口 `6-1` 所作之转录**，且该件**自陈「全仓 `results/*.md` 检索卡号，命中 0」**；② `_questionnaire_cards_intake_register_supplement_8_2026_10_10.md` §行 478 之枚举行**仅载 `request_id` ＋ 建卡／答毕时点**，该件**明示「⛔ 未转录」（不属其应录面）**，⛔ **0 载题面或答文一字**。⇒ **本件所载 PI 原答据派工单转录登记**；⛔ **0 网络、0 读运行时库、0 代 PI 补写卡面全文**；⛔ **0 断言**转录与 PI 原话逐字等价。**若 PI 认为转录有偏，以运行时库原件为准**，本件相应条目须另出勘误。
- **📌 口径并陈（同卡多问 · 0 互相改写）**：PI「轮 55」卡据盘上转录**含多问** —— 出口 `6-1`（「全语料」是否硬约束）之答据 `c7609657dfe4` §行 3–4 照录为**丙「另议」**（通道 `bing`）；**本件所据者 ＝ 出口 `6-2`／AD-8-fix 一问之甲「核准」**。⛔ 本件 **0 评价二答之关系、0 主张二者相斥或相成**，仅**分出口各自照录**。
- **本件**：`results/_s4_source_wave_mapping_registration_2026_10_10.md`（**新名新建 · 0 覆写**；落前 `Test-Path=False` ＋ glob **0** 命中实测，见 §8.1）
- **命名合规**：`_主题_日期`；首段 `_s4_` ＝ **阶段面 S4 之既有用法**（同批 `_s4_v31_*`／`_s4_e4_*`／`_s4_vclause_*`／`_s4_w2_*` 诸件一致，**非** V-阶段号）；⛔ **0** `_v3_`／`_v4_`／`_v5_` 等 V-阶段前缀（沿 PI 2026-09-29 命名裁 `57024f2cd30a` §1.2② ＋ 10-01 补记「派工建议名亦须合规」）
- **出件**：**protocol-keeper（口径与预登记官）**（`agent-3e0c193da529` · 分支会话 `mvs_cfa6d5b8b6cc4611a8664d05b96e696d`｜**署名如实** · ⛔ **0 冒充** PI／parent／worker／doc-writer／evidence-auditor／verdict-keeper／verifier）
- **版式**：UTF-8 无 BOM · LF（CRLF ＝ 0）｜**R4**：key 永不明文（⛔ **0 读 key／0 读 `.env`／0 落盘凭据**）｜**0 网络 ／ 0 skill ／ 0 LLM ／ 0 跑 executor ／ 0 跑 runner ／ 0 派生 JSON 新建或合并**（纯本机只读检索 ＋ 本机哈希核算 ＋ 一次性临时脚本，已按可恢复删除通道清理）
- **状态**：🟡 **修订件已出 · 候 PI 复核生效（生效即锁）** —— 本件 ⛔ **0 自宣告生效**、⛔ **0 自判闭**、⛔ **0 结案**；**完整复现核验（真重建）本件 ⛔ 0 代做，列为出口 §7-1**
- **构造面 vs 真实面**：本件全部登记**仅在构造面**（＝ S4 冻结面 **179 行** ＋ 21 件 addendum ＋ V3.1 全 **15 词** ＋ held-out **26** 件）内有效；**外推边界 ＝ 构造域**，⛔ 0 外推至 PI 未结构化之原始答卷面

---

## §0 本件之效力位（一句话）

> **入册 9 条 canonical 映射 ＋ 首次给出 21 件 × wave 全表 ＋ 10 步复现路径**，使「按本册重建 24 件」成为**机械可执行**；⛔ **本件 0 跑、0 产出重建结果、0 宣告复现已核**——**复现之核验属出口 §7-1**。

---

## §1 缺口重述（**照录 `debd88fc150c` §1.5 ＋ 本棒实测并陈**）

### 1.1 缺口事实（照录源：`results/_round52_s4_e4b_ad5_type_effectivity_register_2026_10_10.md` §1.5 · **`debd88fc150c`**）

| 项 | 事实（**照录**） |
|:--|:--|
| **缺口** | 面 II 之语料面构造依赖 `load_addendum_event_v3(sup, source_wave, fname)` 之 **`source_wave` 实参**，而该映射**未载于 `b6ce4a79116e` §1 与 `2bda07af86fc` §2.1** |
| **机制源（本棒实测定位）** | `8a81d90c69ba` **L836–L846** 之 `provenance_wave_map`（9 件 canonical 映射）＋ **L851** `wave = provenance_wave_map[af]` ＋ **L855** `load_addendum_event_v3(sup, wave, af.name)` |
| **可复现性后果（判断件实测）** | **朴素重建得 23 件而非 24 件**（唯一差异件 ＝ `Q10_third_read`，因 `D3_w2` 下触发 L779–L781 之 `d1_original_read` 拼接分支）〔引 `f48601fee958` §3 AD-8 ＋ §2.4〕 |
| **🔴 轮 52 之新增实测事实** | executor **内部**虽于 **L813–L820** 之 `ev["_provenance"]` 留痕 `source_wave`，但 **面 II 逐件 JSON（`6f020c03e52c`）之字段集共 15 项**（`q_id`／`file`／`src_idx`／`in_heldout`／`seq_v3`／`seq_v31`／`primary_v3`／`primary_v31`／`displacement_type`／`version_attribution`／`no_overwrite_reason`／`new_hit_words`／`layer_first_pos_v31`／`corpus_verbatim`／`declaration`）**不含** `_provenance`／`source_wave`〔24／24 件皆无〕⇒ **下游无法自产出物反推 `wave`** |

> 📌 **该 15 字段清单本棒已独立复核**（只读 `6f020c03e52c` 之 `items[*]` 键集，**逐字段相符、0 差异**）⇒ 该事实**成立**。

### 1.2 ⚠ **该事实在映射入册后【仍然成立】（本棒明示 · 0 借本件之修订抵销之）**

| 项 | 陈述 |
|:--|:--|
| **本修订之性质** | **纯文档面入册**：本件 ⛔ **0 编辑／0 覆写／0 派生** 任何产出物 JSON（`6f020c03e52c` **0 字节改动**） |
| **故** | **「产出物面 0 载 `source_wave`、0 可自产出物反推 wave」这一事实，在本修订之后【逐字仍然成立】** —— 本件**未**、⛔ **0** 欲改变该事实 |
| **闭合之确切范围** | 本件闭合者 ＝ **「面域构造之规格缺一参」**（即：重建者**据此可复现**）；⛔ 本件**未**闭合「产出物不可反推」之另一缺口（**留作出口 §7-2**） |
| **⛔ 纪律** | ⛔ **0 以「已入册」为由声称产出物面之缺口已闭**；⛔ **0 以本件为据径改 `6f020c03e52c`** |

### 1.3 📌 **本棒对缺口范围之细化（**加强而非反驳** `debd88fc150c` §1.5）**

> **`debd88fc150c` §1.5 之陈述为真**（该映射确未载于 `b6ce4a79116e` §1 与 `2bda07af86fc` §2.1）；**本棒补充如下三点事实**（均本棒实测，见 §2–§3）：

| # | 细化 | 意义 |
|:-:|:--|:--|
| **①** | 该映射**并非「盘上 0 载」**：其**轮廓**已散见于 `73550514152d`（`results/_s4_face_five_lines_ci_readings_execution_2026_10_09.md`）**L105–L107**、`9c9d8e8ecc72`（`_s4_v31_regen_gold_register_2026_10_10.md`）**L79**、`892e5dfe3ed1` **L49**、`016c7dacaa54` **L271** 诸件（**逐件实测命中**） | ⇒ 缺口之实为 **「无单一 canonical 登记件 ＋ 面 II 之两份规格件未载」**，⛔ **非**「全盘 0 载」；本件之价值在于**收敂为单一可引之登记面**（**口径固化**） |
| **②** | **executor 之 canonical map ＝ 9 件，而面 II 之复现需 10 件**：第 10 件（`_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json` → `D4_w1`）**不在** L836–L846 之 map 内，系 **L863 之字面量** `load_addendum_event_v3(sup, "D4_w1", ADDENDUM_D4.name)` | ⇒ **仅入册 9 条【不足】以复现面 II**；见 §2.4 之口径校正 |
| **③** | 21 件面域文件中，**11 件盘上 0 有 canonical wave**，实跑时取**惰性标签 `S4_face_unregistered_wave`**（`73550514152d` L105–L107 明载；`.tmp/s4_regen_runner.py` **L167** 定义该字面量） | ⇒ 复现需**三层**（canonical 9 ＋ D4 字面 1 ＋ 惰性标签 11），**缺一即不可复现**；见 §2.4／§3 |

---

## §2 ★ **`source_wave` canonical 映射入册**（**逐字转录 ＋ 全链 ＋ 作用位**）

### 2.1 ★ **executor 原文逐字转录**（本棒自读 `8a81d90c69ba` **L836–L846**，**逐字照录 · 0 改写**）

```python
    provenance_wave_map = {
        ADDENDUM_D1: "D1_supp",
        ADDENDUM_D2: "D2_w1",
        ADDENDUM_D2B: "D2_w2",
        ADDENDUM_D2C: "D2_w3",
        ADDENDUM_D2D: "D2_w4",
        ADDENDUM_D2E: "D2_w5",
        ADDENDUM_D3A: "D3_w1",
        ADDENDUM_D3B: "D3_w2",
        ADDENDUM_D3C: "D3_w3",
    }
```

> **入册条数 ＝ 9／9（9 键 ＋ 9 值，0 遗漏、0 增补、0 改写）**。上列逐字与盘上 L836–L846 **相符**。

### 2.2 ★ **键 → 常量 → 文件名 之全链**（本棒自读 **L162–L170** ＋ **L173–L176**，逐件照录）

| # | 键（常量名） | 常量定义行 | 文件名（**逐字**） | **→ wave** | 文件 SHA-12（**本棒实测**） | executor 申报锚（L178–L188） | 锚核 |
|:-:|:--|:-:|:--|:--|:--|:--|:-:|
| 1 | `ADDENDUM_D1` | L162 | `_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | **`D1_supp`** | `172093a23e4b` | `172093A23E4B` | ✅ |
| 2 | `ADDENDUM_D2` | L163 | `_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json` | **`D2_w1`** | `439721007aaf` | `439721007AAF` | ✅ |
| 3 | `ADDENDUM_D2B` | L164 | `_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json` | **`D2_w2`** | `41d6c28ca87c` | `41D6C28CA87C` | ✅ |
| 4 | `ADDENDUM_D2C` | L165 | `_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json` | **`D2_w3`** | `99c58906f792` | `99C58906F792` | ✅ |
| 5 | `ADDENDUM_D2D` | L166 | `_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json` | **`D2_w4`** | `c6d092f77932` | `C6D092F77932` | ✅ |
| 6 | `ADDENDUM_D2E` | L167 | `_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json` | **`D2_w5`** | `26f110a6e571` | `26F110A6E571` | ✅ |
| 7 | `ADDENDUM_D3A` | L168 | `_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json` | **`D3_w1`** | `6e104e2db038` | `6E104E2DB038` | ✅ |
| 8 | `ADDENDUM_D3B` | L169 | `_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json` | **`D3_w2`** | `d96b747bfc6c` | `D96B747BFC6C` | ✅ |
| 9 | `ADDENDUM_D3C` | L170 | `_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | **`D3_w3`** | `401bd614cdf7` | `401BD614CDF7` | ✅ |

⇒ **锚核 9／9 MATCH、MISMATCH ＝ 0**（本棒以 `Get-FileHash -Algorithm SHA256` 前 12 位**实测** ＋ 与 executor L178–L188 之申报锚**逐项比对**）。
⇒ 遍历序 ＝ `V2_ADDENDUM_FILES`（**L173–L176**，**9 件**）：`D1, D2, D2B, D2C, D2D, D2E, D3A, D3B, D3C`。

### 2.3 ★ **其在复现路径中之作用位（调用链 · 本棒逐行自读）**

| 环节 | 行 | 字面／作用 |
|:--|:-:|:--|
| **① 取映射** | **L836–L846** | `provenance_wave_map`（9 件，见 §2.1） |
| **② 遍历源件** | **L849** | `for af in V2_ADDENDUM_FILES:`（9 件） |
| **③ 读源件** | **L850** | `ad = json.loads(af.read_text(encoding="utf-8"))` |
| **④ ★ 赋 wave（唯一的键→值取用点）** | **L851** | `wave = provenance_wave_map[af]` |
| **⑤ 取 supplements** | **L852** | `sups = ad.get("supplements", [])` |
| **⑥ ★ 注入事件** | **L855** | `ev = load_addendum_event_v3(sup, wave, af.name)` |
| **⑦ ★ wave 于 loader 内之三处分支** | **L742／L777／L779**（另 **L749**） | 见 §2.5 之逐处判定 |

> **注（`⛔ 0 断言其等价`）**：L849–L856 之循环为 **executor 之 v3 主管线**（**10 件中的 9 件**）；面 II 之 179 行**并非**由此循环产生（**系 21 件之 S4 面域构造**，见 §4）。二者**共用同一 loader**（`load_addendum_event_v3`），故 **②–⑦ 之语义对两管线一致**，而**④ 之取值源在面 II 侧为 §3 之三赋值层**。

### 2.4 ★★ **口径校正：canonical 9 件 ≠ 面 II 复现所需 10 件 ≠ 21 件**（**本棒新增 · 关键**）

| 层 | 件数 | wave 之来源 | 载体（**逐字**） |
|:-:|--:|:--|:--|
| **层 A · executor canonical map** | **9** | `provenance_wave_map`（L836–L846） | `8a81d90c69ba`（见 §2.1） |
| **层 B · D4 之字面量** | **1** | **L863** 之字面 `"D4_w1"`（**⛔ 不在** L836–L846 之 map 内） | `8a81d90c69ba` L863：`load_addendum_event_v3(sup, "D4_w1", ADDENDUM_D4.name)` |
| **层 C · 惰性标签（面域余 11 件）** | **11** | **盘上 0 有 canonical wave** ⇒ 实跑取惰性标签 **`S4_face_unregistered_wave`** | `73550514152d` **L105–L107**（明载「盘上 0 有登记 wave 标签」＋ 处置）；`.tmp/s4_regen_runner.py` **L167**（字面量定义）、**L179**（`PROVENANCE_WAVE_MAP_REGISTERED.get(fname, UNREGISTERED_WAVE)`） |
| **合计** | **21** | —— | 与 `6a670e629dca` 之 `domain.r1_byte_sorted_files` 件数**逐项相符** |

> **⚠ 复现之硬性结论（如实登记）**：**仅入册层 A 之 9 条【不足以】复现面 II 之 24 件** —— 须**三层齐备**（9 ＋ 1 ＋ 11）。本件 §3 之全表即**三层之合一展开**，可作单一可引之登记面。
> ⚠ **层 C 之 11 件之 `wave` 真值**（是否应各有其真 wave 名）**盘上 0 载** ⇒ ⛔ 本件 **0 代立**，如实留作出口 **§7-3**。

### 2.5 ★ **`source_wave` 于 loader（`load_addendum_event_v3` · L732–L821）内之作用位 · 逐处判定**

| 行 | 判定式（逐字要义） | 依 wave 而异？ | **面 II 语料面（179 行）内之实测触发** |
|:-:|:--|:-:|:--|
| **L742** | `if event_id is not None and source_wave == "D1_supp":` | ✅ **是**（**唯一 wave 之字面比较 `==`**） | **3 行**（全在 `_…_2026_09_24.json`／`D1_supp`）；**仅影响 `event_id` 之取源，⛔ 0 影响语料／序列** ⇒ **0 影响位移判定** |
| **L749** | `abs(zlib.crc32((q_id + source_wave).encode("utf-8")) % 10**7) + 100000` | ✅ **是**（wave 串**字面进入** `event_id` 之值） | **0 行** —— 179 行**无一行**落入此 `else` 分支 ⇒ **wave 串【未】进入任何 `event_id` 之值** |
| **L777** | `if source_wave == "D1_supp" and sup.get("critical_reflection_supplement"):` → `rf = rf + " " + sup["critical_reflection_supplement"]` | ✅ **是** | **0 行触发** —— `D1_supp` 之 **3 行皆无 `reasoning_full`**（故先落 L783–L788 之 `else`，⛔ 0 入本分支）⇒ 与 `debd88fc150c` §2.3 之 AD-9 归因**一致** |
| **L779–L781** | `if source_wave.startswith("D3") and sup.get("d1_original_read"):` → `rf = rf + " \|\| D1原读: " + (d1.get("reasoning_full", "") or "")` | ✅ **是**（**wave 之前缀**判定） | 🔴 **12 行触发**（`d3a` 4 ＋ `d3b` 4 ＋ `d3c` 4）—— **此【唯一】为面 II 语料面内 wave 能改变语料文本之通道**，亦即**唯一能改变位移判定**之通道 |

> **📌 `event_id` 分支之全量分布（本棒静态实测 · 179 行）**：**L742 ＝ 3 行**｜**L744（`target_event_id`）＝ 12 行**｜**L746（`pair_id`）＝ 164 行**｜**L749 ＝ 0 行**；合计 **179 行，0 遗漏**。
> **⇒ 结论（`0` 夸大）**：面 II 语料面内，`wave` 之影响**可归为二类** ——（**i**）**语料文本类**：仅 **L779 × 12 行**（决定位移判定）；（**ii**）**标识类**：仅 **L742 × 3 行**之 `event_id` 取源（⛔ **0** 影响语料／序列／位移）。

---

## §3 ★ **21 件 addendum × wave 对照表**（**本棒静态实测** · 可核）

> **实测口径**：逐件读 `supplements`（**Python `json.loads` · 0 跑 executor · 0 跑 runner**），按 §2.5 之分支逻辑统计**语料来源分支**与 **wave 触发**；⛔ **本棒 0 重建序列、0 抽取词表、0 复算任何读数**（**真重建 ＝ 出口 §7-1**）。
> **本棒之一处仪器自纠（如实 · 不隐去）**：初稿以 PowerShell 统计得 **180 行**，经 Python 独立复算得 **179 行**；差异之因 ＝ `_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json` 之 `supplements` **为 `null`／缺省**（**实测 0 件**），PowerShell `@($null)` 之包裹致虚增 **1** 行。**本表采 Python 之 179**（**与在册 `b6ce4a79116e` §1 之 179 逐字相符**）⇒ **本棒仪器之误差已更正并披露**，⛔ 0 以错值入册。

| # | 文件名（逐字） | **wave**（三层归属） | SHA-12（本棒实测） | bytes | **sups** | 语料非空 | **语料空** | `d3cat`(L779) | `d1cat`(L777) | `dtfb` |
|:-:|:--|:--|:--|--:|--:|--:|--:|--:|--:|--:|
| 1 | `_r_pair_addendum_2026_10_09.json` | **C ·** `S4_face_unregistered_wave` | `cebc2f6ef5ec` | 110,510 | 8 | 0 | 8 | 0 | 0 | 0 |
| 2 | `_s4_open_questions_addendum_2026_10_09.json` | **C ·** `S4_face_unregistered_wave` | `4378dcc20624` | 35,215 | 4 | 4 | 0 | 0 | 0 | 0 |
| 3 | `_s4_substrate_topup_addendum_2026_10_09.json` | **C ·** `S4_face_unregistered_wave` | `1780542f0014` | 85,861 | 18 | 18 | 0 | 0 | 0 | 0 |
| 4 | `_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | **A ·** `D1_supp` | `172093a23e4b` | 4,103 | 3 | 0 | 3 | 0 | **0** | 0 |
| 5 | `_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json` | **A ·** `D2_w1` | `439721007aaf` | 6,132 | 4 | 4 | 0 | 0 | 0 | 0 |
| 6 | `_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json` | **A ·** `D2_w2` | `41d6c28ca87c` | 7,566 | 4 | 3 | 1 | 0 | 0 | 0 |
| 7 | `_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json` | **A ·** `D2_w3` | `99c58906f792` | 6,666 | 4 | 3 | 1 | 0 | 0 | 0 |
| 8 | `_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json` | **A ·** `D2_w4` | `c6d092f77932` | 7,668 | 4 | 4 | 0 | 0 | 0 | 0 |
| 9 | `_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json` | **A ·** `D2_w5` | `26f110a6e571` | 10,257 | 4 | 3 | 0 | 0 | 0 | **1** |
| 10 | `_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json` | **A ·** `D3_w1` | `6e104e2db038` | 11,589 | 4 | 4 | 0 | **4** | 0 | 0 |
| 11 | `_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json` | **A ·** `D3_w2` | `d96b747bfc6c` | 14,722 | 4 | 4 | 0 | **4** | 0 | 0 |
| 12 | `_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | **A ·** `D3_w3` | `401bd614cdf7` | 19,615 | 4 | 4 | 0 | **4** | 0 | 0 |
| 13 | `_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json` | **B ·** `D4_w1` | `cbf60a630c9f` | 20,194 | 5 | 5 | 0 | 0 | 0 | 0 |
| 14 | `_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json` | **C ·** `S4_face_unregistered_wave` | `6eed9acdb99a` | 18,714 | **0** | 0 | 0 | 0 | 0 | 0 |
| 15 | `_v4_pi_cot_v3_dataset_addendum_d5_2026_09_27.json` | **C ·** `S4_face_unregistered_wave` | `990c0c42a6f6` | 16,587 | 2 | 1 | 1 | 0 | 0 | 0 |
| 16 | `_v4_pi_cot_v3_dataset_addendum_d6_2026_09_28.json` | **C ·** `S4_face_unregistered_wave` | `9669efa804b7` | 19,214 | 2 | 0 | 2 | 0 | 0 | 0 |
| 17 | `_v4_pi_cot_v3_dataset_addendum_d6b_2026_09_28.json` | **C ·** `S4_face_unregistered_wave` | `5d94a8617b5b` | 27,009 | 2 | 0 | 2 | 0 | 0 | 0 |
| 18 | `_v4_pi_cot_v3_dataset_addendum_d8_bhalf_2026_09_30.json` | **C ·** `S4_face_unregistered_wave` | `b02ef31f1e4e` | 58,581 | 3 | 3 | 0 | 0 | 0 | 0 |
| 19 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json` | **C ·** `S4_face_unregistered_wave` | `769ef8b71462` | 374,072 | 93 | 79 | 14 | 0 | 0 | 0 |
| 20 | `_v4_pi_cot_v3_dataset_addendum_s3_d1fill_2026_10_01.json` | **C ·** `S4_face_unregistered_wave` | `b9026cbf5ca2` | 46,909 | 6 | 0 | 6 | 0 | 0 | 0 |
| 21 | `_v4_pi_cot_v3_dataset_addendum_s3_d7_2026_09_29.json` | **C ·** `S4_face_unregistered_wave` | `c0ebbd1f4633` | 17,252 | 1 | 0 | 1 | 0 | 0 | 0 |
| | **合计** | **A 9 ＋ B 1 ＋ C 11 ＝ 21** | —— | —— | **179** | **139** | **39** | **12** | **0** | **1** |

**列义**：`sups` ＝ `supplements` 件数｜`语料非空` ＝ `reasoning_full` 非空之行数｜`语料空` ＝ 经 **L775–L788 完整分支**（含 `disposition_text`／`other_text` 之回退）后**语料为空**之行数｜`d3cat` ＝ 触发 **L779–L781**（`D3` 前缀 ＋ `d1_original_read` 拼接）之行数｜`d1cat` ＝ 触发 **L777–L778**（`D1_supp` ＋ `critical_reflection_supplement` 拼接）之行数｜`dtfb` ＝ 经 `disposition_text` 回退得语料之行数（**第 9 件之 1 行**）。

> ✅ **与在册之交叉核（本棒实测）**：`sups` 合计 **179** ＝ `6f020c03e52c` `face_ii_denominator.n_rows`（**179**）＝ `b6ce4a79116e` §1「**179 行**」｜`语料空` 合计 **39** ＝ `f48601fee958` §2.1 之「空语料行数 **39**」｜`语料非空` **139** 行对应在册唯一文本 **131**（行级→文本级之去重落差，**本棒 0 复算去重**，见 §7-5）｜`type_counts`（T1 7／T2 0／T3 17／T4 0）与 `heldout_in 9`／`heldout_out 15` 本棒**只读照录**，⛔ **0 复算**。

### 3.1 ★ **面 II 之 24 件之 wave 依赖分解**（**本棒只读实测 `6f020c03e52c`**）

| 面 II 24 件所自 `file` | 件数 | **其 wave** | **是否依赖 canonical 映射** |
|:--|--:|:--|:-:|
| `_s4_open_questions_addendum_2026_10_09.json` | 1 | `S4_face_unregistered_wave`（层 C） | ⛔ 否（**惰性标签为常量字面** ⇒ wave-blind 亦可复现） |
| `_s4_substrate_topup_addendum_2026_10_09.json` | 5 | 同上（层 C） | ⛔ 否 |
| `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json` | 17 | 同上（层 C） | ⛔ 否 |
| 🔴 **`_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json`** | **1**（`Q10_third_read` · `src_idx=3`） | **`D3_w2`**（层 A · canonical） | ✅ **是 —— 24 件中【唯一】依赖 canonical 映射者** |
| **合计** | **24** | —— | **依赖者 1／24；不依赖者 23／24** |

### 3.2 ★ **`Q10_third_read` 之 wave 敏感性（本棒实测至字符级）**

| 项 | 值（本棒实测） |
|:--|:--|
| **源件／位次** | `_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json` · `supplements[3]`（`src_idx=3`） |
| **`q_id` 之来源** | 该行**无 `q_id` 键**（`q_id` ＝ `None`）；其 `pair_id` ＝ **`Q10_third_read`** ⇒ 依 executor **L758** `ev["q_id"] = q_id or pair_id` ⇒ **事件 `q_id` ＝ `Q10_third_read`** |
| **`D3_w2` 下之语料** | `reasoning_full`（**24 字**）＋ 分隔符 `" \|\| D1原读: "`（**10 字**）＋ `d1_original_read.reasoning_full`（**96 字**）＝ **130 字** |
| **与在册之逐字核** | `6f020c03e52c` 之 `Q10_third_read.corpus_verbatim` **长度 ＝ 130**（本棒实测）✅ **逐字相符**（`f48601fee958` §2.4 亦载「`D3_w2` 下语料 **130 字**（＝在册 `corpus_verbatim` **逐字相符**）」） |
| **在册之序列与类型** | `seq_v3` ＝ `['COST','RISK','TIMING']` → `seq_v31` ＝ `['COST','KILL_LINE','RISK','TIMING']`；类型 **T1**；`in_heldout` ＝ `false` |
| **wave-blind（默认/惰性 wave）下之后果** | `wave` 不以 `"D3"` 开头 ⇒ **L779 不触发** ⇒ 语料仅 **24 字**、序列仅 `['COST']` ⇒ **不位移** ⇒ 面 II 由 **24 → 23** |
| **📌 与判断件实测之关系** | 本棒**静态核得**「**1／24 依赖 canonical wave**」之结构，与 `f48601fee958` §2.4 实测「朴素重建得 **23**」**方向一致、量一致**；⛔ 本棒 **0 跑模型、0 抽词表**，故 **0 宣告该重建已复核**（**§7-1**） |
| **📌 另注（**方向性 · 0 夸大**）** | 12 行 `d3cat` 中，`d3a`（4 行）／`d3c`（4 行）之各行**均不在** 面 II 之 24 件内（本棒实测）⇒ 其拼接**未**改变其位移事实；故缺失映射之净效果 ＝ **少计 1 件（24→23）**，⛔ **0 断言**「缺失映射绝不致多计」——该方向（多计）本棒**未测**。 |

---

## §4 ★ **复现路径（分步 · 按本册重建 24 件）**

> 🔴 **⛔ 本件 0 跑 executor／0 跑 runner／0 真重建** —— 以下为**可执行之规格**，**非**本件之执行结果。**执行与核验 ＝ 出口 §7-1**（候 PI 令或后续 worker 步骤）。

| 步 | 动作 | 规格来源（**逐字可依**） | ⛔ 纪律 |
|:-:|:--|:--|:--|
| **1** | 取面域源之文件序 | `6a670e629dca` 之 `domain.r1_byte_sorted_files`（**21 件 · R1 字节序**） | ⛔ 0 改序、0 增删 |
| **2** | ★ **逐件赋 wave** | **§3 全表**（三层合一）：**层 A 9 件**取 §2.2 之 canonical 值｜**层 B 1 件**取 `D4_w1`｜**层 C 11 件**取惰性标签 `S4_face_unregistered_wave` | ⛔ **0 用「默认 wave」代替**；⛔ 0 自造标签名 |
| **3** | 逐件读 `supplements` | `ad.get("supplements", [])`（沿 executor **L852**）＋ **逐件内 `idx` 升序** | ⛔ 0 去重、0 排序变更 |
| **4** | 逐行调 loader | `load_addendum_event_v3(sup, wave, fname)`（**L732–L821**；调用式沿 **L855**） | ⛔ 0 改 loader、0 改 executor |
| **5** | *（自动）* wave 之分支生效 | **L742 × 3**｜**L777 × 0**｜**L779 × 12**｜**L749 × 0**（**§2.5 之实测触发数**） | —— |
| **6** | ★ `is_correction` 真值化适配 | 沿 `73550514152d` §2.3(b)：布尔 `true` ∨ 字符串以 `_pair_pending` 结尾 ∨ `== "R_pair"`（**注：此为 S4 面域之适配，非 executor 原件**） | ⛔ **0 省此步**（省则特征面异）｜⛔ 0 径改 executor |
| **7** | 抽取序列 | `extract_judgment_sequence_v3` 之**逐字复制**（**L478–L519**）：逐层取 `reasoning.find(kw)` 最小位置 → 按位置排序 ＋ `dedup` 保序 → `PHRASE_PATTERNS_V3` 5 条短语模式追加 | ⛔ 0 改抽取机制 |
| **8** | 双词表各抽一次 | `KEYWORDS_V3`（executor **L202–L283**）vs `KEYWORDS_V3 ⊎ 15 词`（`1b7bcbcce589` §4.1／§4.2 **逐字**） | ⛔ 0 改词表、0 增删 15 词 |
| **9** | 逐行比对并分类 | 四类封闭词表之机械判据（`017b3cf38ae3` §3.2）：**T1** 真子序列（按序）｜**T2** 层集合相等 ＋ 首现位置序不同｜**T3** `[]`→非空｜**T4** 两皆 `[]` | ⛔ **0 增设第 5 类**；⛔ 0 改判据 |
| **10** | 逐件登记并对账 | 产出 **24** 件 × **15 字段**（`q_id`／`file`／`src_idx`／`in_heldout`／`seq_v3`／`seq_v31`／`primary_v3`／`primary_v31`／`displacement_type`／`version_attribution`／`no_overwrite_reason`／`new_hit_words`／`layer_first_pos_v31`／`corpus_verbatim`／`declaration`） | ⛔ 0 增删字段（**⛔ 0 补入 `_provenance`／`source_wave`** —— 见 §1.2） |

**步 10 之期望值（**在册锚 · 本棒 0 复算**）**：**179 行** → **位移 24 件** → **T3 17 ＋ T1 7（T2 0／T4 0）** → **held-out 内 9 ／外 15**；其中 `Q10_third_read` 之 `corpus_verbatim` 应为 **130 字**（§3.2）。
**❌ 反例判据（**朴素重建之特征**）**：得 **23** 件 ⇒ **必为步 2 之 wave 赋值缺失**（尤以 `d3b` 之 `D3_w2` 为首要嫌疑）⇒ **0 径改任何阈值以迁就之**。

---

## §5 ★ **锚件指纹**（本棒落笔前**自算** · `Get-FileHash -Algorithm SHA256` 前 12 位 · **禁沿用他件转述**）

| # | 件 | SHA-12（本棒实测） | bytes | 角色 |
|:-:|:--|:--|--:|:--|
| 1 | `results/_v4_pi_cot_v3_ruleset_v3_executor.py` | **`8a81d90c69ba`** | 58,794 | ★**机制源**（L162–L176／L732–L821／L836–L846／L849–L863）· 仅只读·**0 字节改动** |
| 2 | `results/_round52_s4_e4b_ad5_type_effectivity_register_2026_10_10.md` | **`debd88fc150c`** | 45,351 | ★**缺口登记源**（§1.5 ＋ §6-2 出口原文） |
| 3 | `results/_s4_e4b_ad5_type_separate_judgment_2026_10_10.md` | **`f48601fee958`** | 51,898 | ★**AD-8 出处**（§3 AD-8／§2.4 之 23 vs 24 实测） |
| 4 | `results/_s4_v31_displacement_register_face2_2026_10_10.md` | **`b6ce4a79116e`** | 17,736 | ★**面 II 登记件**（§1 之 179 行口径 · **未载 wave 映射**）· 0 覆写 |
| 5 | `results/_s4_e4_axis_disposition_axis2_run_2026_10_10.md` | **`2bda07af86fc`** | 29,700 | ★**原登记处**（§2.1 之「`load_addendum_event_v3(sup, wave, fname)`」· **wave 符号未绑定**）· 0 覆写 |
| 6 | `results/_s4_v31_displacement_items_2026_10_10.json` | **`6f020c03e52c`** | 36,822 | ★**面 II 逐件 JSON**（24 件 · 15 字段）· **0 改动** |
| 7 | `results/_s4_heldout_sampling_seed42_items_2026_10_09.json` | **`6a670e629dca`** | 20,033 | ★**面域源**（`domain.r1_byte_sorted_files` ＝ **21** 件） |
| 8 | `results/_s4_vclause_1_6_revision_2026_10_10.md` | **`017b3cf38ae3`** | 14,900 | **四类封闭词表**（§3.2 判据）· 0 径改 |
| 9 | `results/_s4_v31_keyword_table_final_2026_10_10.md` | **`1b7bcbcce589`** | 23,270 | **V3.1 词表**（15 词） |
| 10 | `results/_s4_v11_axis2_displacement_items_2026_10_10.json` | **`0eed9053619c`** | 9,941 | **轴二逐件 JSON**（另案在册面 · 本件仅列锚） |
| 11 | `results/_v4_pi_cot_v2_dataset.json` | **`7b01cd835a41`** | 12,672 | **v1.1 基础面源**（37 件 · ⛔ 不属面 II） |
| 12 | `results/_s4_face_five_lines_ci_readings_execution_2026_10_09.md` | **`73550514152d`** | 29,750 | ★**层 C 之轮廓出处**（L105–L107）· 0 覆写 |
| 13 | `results/_s4_v31_regen_gold_register_2026_10_10.md` | **`9c9d8e8ecc72`** | 27,133 | 层 C 之再述（L79） |
| 14 | `results/_s4_abcreadings_reproducibility_check_2026_10_10.md` | **`892e5dfe3ed1`** | 25,234 | 层 C 之再述（L49） |
| 15 | `results/_s4_tree_construct_adjustment_assessment_2026_10_10.md` | **`016c7dacaa54`** | 33,453 | 层 C 之再述（L271） |
| 16 | `results/_s4_corpus_scope_hard_constraint_judgment_2026_10_10.md` | **`c7609657dfe4`** | 44,199 | **轮 55 卡另一问（出口 6-1）之转录**（§行 3–5）· ⛔ 0 视为卡面原件 |
| 17 | `results/_questionnaire_cards_intake_register_supplement_8_2026_10_10.md` | — | — | **活库账目**（轮 55 卡建卡／答毕时点之**独立**佐证）〔**按锚**〕 |
| 18 | `.tmp/s4_regen_runner.py`（**临时件**） | **`70467364bdb1`** | 13,040 | ⚠ **在盘唯一之实现载体**（`PROVENANCE_WAVE_MAP_REGISTERED` **L155–L166**／`UNREGISTERED_WAVE` **L167**／`.get(fname, UNREG)` **L179**）· **0 改、0 移、0 删**（见 §7-4 限制） |

> **0 分歧**：第 1／3／4／5／6／7／8／9／10／11 项与 `f48601fee958` §1 之登记值**逐项相符**。
> ⚠ **一处如实补记（**不构成 MISMATCH**）**：第 2 项（`debd88fc150c` · 缺口登记源）**成件晚于** `f48601fee958`，故**未收录于**后者 §1 之 11 项锚表；本棒实测其 SHA-12 ＝ **`debd88fc150c`**（45,351 B），与 `c7609657dfe4` §行 3 所引之同一编号**相符** ⇒ **0 分歧、0 MISMATCH**。

---

## §6 **0 回改确认**（**R5 · frozen 只追加**）

| 纪律 | 确认 |
|:--|:--|
| **⛔ 0 编辑／0 覆写** | 既有件**全部 0 改动**；`8a81d90c69ba`（executor）**0 字节改动**；`6f020c03e52c`（面 II JSON）**0 字节改动**；`b6ce4a79116e`／`2bda07af86fc`／`f48601fee958`／`debd88fc150c` **0 改动** |
| **⛔ 0 改名／0 移动／0 删除** | 既有件**0 改名、0 移动、0 删除**；`.tmp/s4_regen_runner.py` **0 触** |
| **唯一写动作** | ✅ **新建本件**（`results/_s4_source_wave_mapping_registration_2026_10_10.md`） |
| **⛔ 0 派生 JSON** | **0 新建／0 合并**任何派生 JSON（本棒所读 21 件 addendum ＋ 2 件 JSON **全部只读**） |
| **⛔ 临时脚本** | 本棒曾用 **3 个一次性临时脚本**（仓根 `_tmp_pk_*_2026_10_10.py`）作只读统计；**已全部经可恢复删除通道（`rm --`）清理**，落笔前实测 **0 残留**（§8.2） |
| **⛔ 0 触及禁区** | `〔归档区〕` **0 读、0 写、0 列目录** |

---

## §7 **未闭出口**（**⛔ 0 代裁 · 0 代立 · 0 自判闭**）

| 出口 | 类别 | 事项 | 本件处置 |
|:-:|:--|:--|:--|
| **7-1** | **须 PI 令／后续 worker** | 🔴 **完整复现核验（真重建）** —— 按 §4 之 10 步**实跑**，验 179 行／24 件／T3 17＋T1 7／held-out 9·15／`Q10_third_read` 130 字，并与 `6f020c03e52c` 逐字段对账 | 📋 **本件 0 跑、0 宣告复现已核**；⛔ 0 以「入册」冒充「已复核」 |
| **7-2** | **须 PI 裁** | ⚠ **产出物面 0 载 `source_wave`** —— 面 II JSON 15 字段不含 `_provenance`／`source_wave`（§1.2：**映射入册后此事实仍成立**）。是否于后续**另立新件**补载（**⛔ 0 径改 `6f020c03e52c`**） | 📋 如实登记；⛔ 0 代裁 |
| **7-3** | **须 PI 裁** | ⚠ **层 C 之 11 件之 wave 真值盘上 0 载** —— 惰性标签 `S4_face_unregistered_wave` **非真 wave 名**，仅为可复现之占位；11 件是否应各有其真 wave 名，**本件 0 代立** | 📋 §2.4／§3 层 C 如实登记；⛔ **0 代立真值** |
| **7-4** | **须 PI 知悉**（风险面） | ⚠ **唯一实现载体为临时件** —— `.tmp/s4_regen_runner.py`（**`70467364bdb1`**）承载 `PROVENANCE_WAVE_MAP_REGISTERED`（**10 条**＝ 层 A 9 ＋ 层 B `D4_w1`）与惰性标签字面量；`.tmp` 属临时区，**该件之存续不由本件保证** | 📋 **仅登记其指纹与行号**；⛔ 0 移动／0 提升／0 改名（本件 ⛔ **0** 处置他棒临时件之归属） |
| **7-5** | **须 PI 裁／后续核** | ⚠ **行级→文本级之去重落差 0 复算** —— 本棒 §3 表「语料非空 **139** 行」与在册唯一文本 **131** 之落差，本棒 **0 复算去重**（⛔ 0 重建文本池） | 📋 如实标注为**未复算项** |
| **7-6** | **须 PI 知悉**（完整性面） | ⚠ **`ADDENDUM_D4` 之申报锚与盘上不符** —— executor **L190** 申报 `B18FF4177289`，盘上实测 **`cbf60a630c9f`**（20,194 B · mtime **2026-09-27 12:10:45.852**，**早于** executor ⇒ **非事后改动**）。经核 executor **L1337–L1343** 对 D4 系**记录 drift 而非 assert**（另 6 项主锚 L1312–L1323 与 9 项 v2 addendum L1328–L1335 同为记录漂移），故 **⛔ 0 阻断执行**。⇒ **对 24 件之影响 ＝ 0**（`d4` 之 5 行**不在**面 II 之 24 件内，§3.1） | 📋 **如实登记 · 0 径改 executor、0 径改任何既有件**；⛔ 0 断言「漂移无害于一切」（本棒**仅**核其对 24 件之影响为 0） |
| **7-7** | **维持未闭** | `debd88fc150c` §6 之他出口（**6-1**「全语料」是否硬约束／**6-3** TYPE-b／**6-4** G5 之 `N*`／**6-5** AD-5 视角／**6-6** AD-10-corr／**6-7** W-2b 等） | ⛔ **0 复议**（本件仅闭 **6-2** 之登记面） |

---

## §8 **落前撞名实测 ＋ 纪律对照**

### 8.1 落前撞名实测（**本 Turn 实测 · 落笔前**）

| 检查 | 结果 |
|:--|:--|
| `Test-Path 'results/_s4_source_wave_mapping_registration_2026_10_10.md'` | **`False`** ✅ |
| `Get-ChildItem -Recurse -Filter '*source_wave*'`（全仓） | **0 命中** ✅ |
| `Get-ChildItem -Recurse -Filter '*wave_mapping*'`（全仓） | **0 命中** ✅ |
| 同日同族件名对照（`results/_s4_*_2026_10_10.md`，**26 件**） | **0 与本件同名**；`source_wave`／`wave_mapping` 二名**盘上 0 已占** ✅ |

### 8.2 临时脚本清理实测（**落笔前**）

| 检查 | 结果 |
|:--|:--|
| `_tmp_pk_sourcewave_static_2026_10_10.py` | **已移除**（`Test-Path` ＝ `False`）✅ |
| `_tmp_pk_qid_probe_2026_10_10.py` | **已移除**（`Test-Path` ＝ `False`）✅ |
| `_tmp_pk_evtbranch_2026_10_10.py` | **已移除**（`Test-Path` ＝ `False`）✅ |
| 清理通道 | 可恢复删除（`rm --`，mavis-trash）｜⛔ **0 永久删除** |

### 8.3 纪律对照（**逐条自证**）

| 纪律 | 自证 |
|:--|:--|
| **⛔ 0 跑 executor／0 跑 runner／0 真重建** | ✅ 本棒对 executor 与 `.tmp/s4_regen_runner.py` **仅只读**（`read`／`grep`／哈希）；**0 import、0 调用、0 执行**；统计经**独立临时脚本**读 JSON 达成 |
| **⛔ 0 改阈值／门柱／判死线** | ✅ **0 触** `TH-*`／`K-*` 任何字面；本件**0 赋任一 `k_*` 布尔** |
| **⛔ 0 判档／0 代裁** | ✅ **0 出五终判之一**；PI 轮 55 之答**照录**，⛔ 0 代立生效、⛔ 0 自判闭 |
| **⛔ 0 回改任何既有件** | ✅ 见 §6；**唯一写动作 ＝ 新建本件** |
| **R4** | ✅ key 永不明文；**0 读 key／0 读 `.env`／0 落盘凭据** |
| **0 网络／0 skill／0 LLM** | ✅ 全程**纯本机**只读检索 ＋ 本机哈希核算 |
| **署名如实** | ✅ **protocol-keeper（口径与预登记官）**；⛔ 0 冒充 PI／parent／worker／doc-writer／evidence-auditor／verdict-keeper／verifier |
| **诚实交代** | ✅ 本棒**一处仪器误差已自纠并披露**（§3 之 180→179）；**一处锚不符已如实登记**（§7-6 之 D4）；**真重建明确外推为出口**（§7-1）；**0 自嵌本件之落盘后指纹**（**随回执回报**） |

### 8.4 构造面 vs 真实面（**外推边界声明**）

> 本件之全部登记**仅在构造面**（＝ S4 冻结面 **179 行** ＋ 21 件 addendum ＋ `KEYWORDS_V3` ⊎ **15 词** ＋ held-out **26** 件）内有效；**外推边界 ＝ 构造域**。⛔ **0 外推**至 PI 未结构化之原始答卷面；⛔ **0 外推**至面 II 以外之语料面（如 v1.1 基础面、executor 主管线之 72 条唯一文本面 —— 后者虽共用 loader，但**面域、分母与判定面均不同**）。

---

> **⛔ 本件 0 主张**：①本修订**已生效**（**候 PI 复核 · 生效即锁**）；②面 II 之 24 件**已被独立复核**（**§7-1 未闭**）；③「产出物面不可反推 wave」之缺口**已闭合**（**§1.2 明示其仍成立**）；④任何既有件**已被回改**（**§6：0**）。
> **📌 本件所主张者 ＝ 唯一**：**面域构造之 `source_wave` canonical 映射【已入册】（9 条逐字 ＋ 21 件 × wave 全表 ＋ 10 步复现路径），使「按本册重建 24 件」在规格上成为可能** —— 其**执行与核验**仍候 **§7-1**。
