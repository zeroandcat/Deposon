# 门槛②「＋360 差因逐条定」· 逐条定因登记件（2026-10-23）

> **术语首现附白话**（PI 两度直纠之面——代号首现必附其义之白话）：
> - **门槛②** ＝ 母件 §2.3「收官门槛」之第二项：「全部波次产出件 **0 有「不明/未核得」状态**」（白话：这一波做出来的东西，不许还有「查不清是啥」的残留）。
> - **真幽灵** ＝ 引文所载之 12 位十六进制指纹（SHA-12）在**本机可核面**上 **0 实存**者（白话：文件里写了一个指纹，盘上找不到对应那个文件）。
> - **幽灵引用** ＝ 「件里引了一个指纹或名字，但盘上找不到那件」（承 10-22 复核件之释义，逐字）。
> - **五分支** ＝ `FOUND_IN_REPO`／`GHOST_REF_OUTSIDE`／`MISSING_TRUE`／`SAME_IDENTITY`／`CONFLICT`（语汇出处见 §1.2）。
> - **`MISSING_TRUE`** ＝ 五分支中「三处均无 ＝ 真缺件」之一支（白话：仓里没有、盘上也没有、外头也没有 ⇒ 真的丢了）。
> - **成对总体** ＝ 「12 位指纹 × 引文所载字节数」成对之候选集——本计数之母体。
> - **`CARRY`** ＝ 「承索引」之读法（白话：不重新扫那一片，直接沿用上一棒留下的索引结果）。
> - **漂移改指** ＝ 旧指纹已亡、而「同名＋近字节」之现行件在盘之改指候选（本件沿 10-22 之判分规则）。
> - **移动映射表** ＝ 10-22 整理之「旧路径 → 新路径」逐件凭据（`results/work/process/_reorg_move_mapping_2026_10_22.md`）。
> - **合册** ＝ 把一族旧件「逐字节并置」为一册（白话：不删内容，合并成一个文件），13 册（`_book_01…_book_13_2026_10_22.md`）。
> - **垃圾候选** ＝ 10-22 勘查案所列「可恢复删·候 PI 逐单」之 56 件。
> - **态变型** ＝ 引文所载指纹是某活件的**旧前缀**或**陈旧字节**（活件后来被续写／改写）。
> - **仪器噪声** ＝ 被扫描器误当指纹之字符串（假阳性）——须修仪器，⛔ 0 以之充因。
> - **未核得** ＝ 事实查清到「知其然不知其所以然」之面；须写清「缺什么才能判」。

---

## §0 自路径・观测时点・签棒・授权・边界

| 项 | 值 |
|:--|:--|
| 自路径 | `〔幽灵引用·未上传:_gate2_delta_attribution_2026_10_23.md〕` |
| 撞名预检 | 落笔前查 `results\evidence\register\`（**321** 件）→ **无同名件**；目录已存在，**0 新建目录** |
| 观测时点 | **2026-10-23 15:43:22 – 16:0x（GMT+8）**·自扫一遍（源面 1,335 件）＋ as-of 复算（源面截止 15:00:50）＋ 三读并出；**权威集合差取 as-of 读**（对齐重测件之权威跑窗） |
| 签棒 | `evidence-auditor`（证据链审计官）·deposon「数据修订／资产处置」之证据链面 |
| 授权 | PI 2026-10-23 15:33:28 卡 `ask_117c67d4e24522d28dfb03b2` Q2 择项，逐字：**「派棒逐条定因（推荐）」**；落账件 `pi_rulings\_pi_card_answers_register_2026_10_23_v251.md`（`198545d980ef`）§2-2 |
| 依据件 | `results\evidence\register\_ghost_surface_recount_2026_10_23.md`——**本棒自测 29,444 B／SHA-12 `2ac4a213e32a`**，与派工单所载预期**全等**（末字节 `0x0A`／无 BOM／纯 LF）⇒ **MATCH** |
| 本棒性质 | **定因登记件**——自扫以分离 `CARRY`·逐条定因·两读并出·0 代裁·0 落五终判·0 闭 KD·0 宣告段毕·**⛔ 0 宣告门槛② 成就** |
| 边界自述 | ⛔ 0 移动／重命名／删除／新建目录；⛔ 0 改任何既有件一字；⛔ 0 联网；⛔ 0 跑实验；⛔ 0 调 LLM／API；⛔ 0 读 `〔归档区〕` 之内容（仅列名与计数）；⛔ 0 读 `〔本地路径已脱敏〕` 之内容（仅名／字节／mtime 之元数据）；⛔ 0 以定因之果径改 1,710 或 1,350 之登记 |

**本棒之读法授权（三要素，照 PI 裁「何口径／何时点／实算或转引」）**：

| 三要素 | 本件之值 |
|:--|:--|
| 何口径 | §1 所定之**族甲**（指纹级·s18 线）口径；判分＝五分支语汇之 `MISSING_TRUE` 支；**计数式与去重式两读并出**（见 §2.3） |
| 何时点 | 2026-10-23 15:43:22–16:0x（本棒**实算**，非转引）；对照重测件之 15:00:50 窗（**转引**） |
| 实算或转引 | **实算**（自扫一遍 ＋ as-of 复算 ＋ 逐件追查）；仅 10-22 之在册值与重测件之 1,710 系**转引**（逐字标出处） |

---

## §1 口径核（先回原件）：「门槛② 所计者」究系哪一分

### 1.1 `MISSING_TRUE` 之逐字定义（回原件，不按常识假定）

原件：`results/work/process/_kd_h5_background_tasks_full_scan_2026_10_20.md`（**70,187 B**／SHA-12 `165ac1c8f063`）§5-5「五分支分类」**L438** 逐字照录：

> | `MISSING_TRUE`（三处均无 ＝ 真缺件） | 仓内 0 载 **且** 盘上 0 实体 | **2** | **2** |

### 1.2 「三处」之各指（逐字，同件 **L345**）

> 📌 **真·未登记之 4 枚** ＝ 三处（仓内／盘上会话域／仓外目录）皆无其登记足迹者——⚠ **仓外目录为 0 触 ⇒ 此 4 枚之「未登记」之断言仅及仓内＋盘上两处**（§8 之局限第 2 项）。

⇒ **「三处」＝ ①仓内　②盘上会话域　③仓外目录**（白话：仓里、盘上的运行目录里、仓外的留档目录里，三处都没有）。

⚠ **原件自设之射程限制**（同件 **L455** 逐字照录）：

> 📌 **口径之诚实交代**：此二者于**仓内 ＋ 盘上**两处皆无；📌 **仓外目录（归档区／`〔本地路径已脱敏〕`）为 0 触 ⇒ 该支为「未查」而非「确无」** ⇒ 📌 **`MISSING_TRUE` 之断言之射程仅及仓内＋盘上两处**；📌 **⛔0 造来源**（⛔0 以空占位目录或以他 id 顶替）。

⇒ 本棒沿用同戒：**⛔ 0 以「不在本地」充「不存在」**；**⛔ 0 造来源**（三处均无即写「真缺件」，不虚构来由）。

### 1.3 族甲（计数族）之「真幽灵」义 ＝ 门槛② 所计者

`results/review/audit/_ghost_reference_audit_2026_10_22.md`（**443,091 B**／SHA-12 `37659d4a398a`）§2「汇总表（六类计数）」**L68** 逐字照录：

> | **真幽灵** | 实体 0 在本机四区＋域外面（指纹、字节、前缀、口径四径皆不命中） | **1350** | 19.4% |

⇒ **门槛② 所计者 ＝ 族甲之「真幽灵」一支**（＝ 五分支语汇之 `MISSING_TRUE` 支之族甲表述）。**族乙（会话 id 级）之 `MISSING_TRUE` ＝ 2 件，与本数无涉**（⛔ 0 与 1,350 互算：指纹级 ≠ 会话 id 级）。

### 1.4 在册 1,350 之推导式（逐字，10-22 发射脚本 L33–65）

> `DRIFT_TRUE = _uniq_old([x for x in drift if cls_of(x["old"]) == "TRUE_GHOST"])` ／ `TG = [r for r in B["TRUE_GHOST"] if r["sha12"] not in DRIFT_OLD]` ／ `n_true = len(TG) + len(POSTFREEZE)`

**本棒之复算校验（自 10-22 在册中间件重建）**：`TRUE_GHOST` 桶 **1,379** − 漂移扣除 **31** ＝ `TG` **1,348** ＋ 冻结后补扫 **2** ＝ **1,350** ⇒ **MATCH 在册值**（重建可信，见 §8-1）。

---

## §2 成员面之取法（1,710 与 1,350 各自之「成员面」）

### 2.1 10-22 在册面（读甲）：自中间件**精确重建**

| 步 | 值 | 凭据 |
|:--|--:|:--|
| `TRUE_GHOST` 桶 | **1,379** | `results\.tmp\_s18_ghost_audit_stage3_out_2026_10_22.json` |
| 漂移改指扣除 | **−31** | `results\.tmp\_s18_ghost_audit_stage6_out_2026_10_22.json`（`DRIFT_OLD` 36，其中 31 属 `TRUE_GHOST` 侧） |
| ＝ `TG` | **1,348** | 同 §1.4 之式 |
| ＋ 冻结后并发补扫 | **＋2** | `a75dbfff187e`／`af5d2e3832cc`（10-22 发射脚本 L53–60 之 `POSTFREEZE`） |
| **＝ 在册计数** | **1,350** | **MATCH** 在册值 |
| **去重后（distinct）** | **1,349** | ⚠ `af5d2e3832cc` **已在 `TG` 内** ⇒ 计数式 1,350 含 **1 件重复** |

### 2.2 今日面（读丙）：本棒**自扫**（⛔ 0 以「承索引」为免责语）

| 项 | 值 |
|:--|:--|
| 仪器 | 沿 10-22 仪器 v2 **同法同口径**复刻（指纹正则 `(?<![0-9a-fA-F-])[0-9a-f]{12}(?![0-9a-fA-F-])`；字节面＝前后 40 字内「逗号千分位或带 `B`／`bytes`／`字节`」；分桶次序＝sha256→git-blob→sha1→域外→前缀→真幽灵） |
| 源面 | `results\**\*.md` ＋ `pi_rulings\**\*.md`：**全源面 1,335 件**／**as-of 源面 1,323 件**（mtime ≤ **2026-10-23 15:00:50** ＝ 重测件之权威跑窗之末） |
| 索引面 | `deposon-repo` **6,745** ＋ `deposon-sub` **1,275** ＝ **8,020** 件逐件 SHA-256＋SHA-1＋git-blob-SHA-1（⛔ **GLM 不入哈希面**——0 读其内容） |
| 域外面 | `.minimax` 5 根／**5,260** 件实扫／2,060 唯一 SHA-12 |
| 归档区 | **40,242** 件·**仅列名与计数**（⛔ 0 读内容／0 哈希） |
| 前缀探针 | **8,256,225** 次计算／**1,098** 命中（增量式；⛔ 0 以全量直算之 778 s 版本充数） |
| 遍历错误／读错 | **0／0** |

**三读并出（今日）**：

| 读 | 口径 | 值 | 说明 |
|:--|:--|--:|:--|
| 读丙 | as-of 源面 ＋ **承** 10-22 之 GLM 索引（＝`CARRY`） | **1,711** | `TRUE_GHOST` 桶 **1,737** − 漂移扣除 **26**；**与重测件之桶值 1,737 全等** |
| 读丁 | as-of 源面 ＋ **0 承** GLM 索引（＝**盲读**·自扫分离） | **1,729** | ＝ 读丙 ＋ **18**（GLM 面那 18 条被引指纹） |
| 读戊／读己 | 全源面 1,335 ＋ 承／盲读 | **1,712／1,730** | 全源面较 as-of 多 1 件（并发棒新出件之引） |

### 2.3 ⚠ 计数式 与 去重式 之别（**＋360 之第一处口径缺口**）

| 面 | 计数式（照 10-22 之式：`TG` ＋ 补扫 2） | 去重式（distinct 指纹） | 差 |
|:--|--:|--:|--:|
| 10-22 在册（读甲） | **1,350** | **1,349** | 1 |
| 重测件 15:00 读（读乙） | **1,710** | **1,708** | 2 |
| 本棒 as-of 读（读丙） | 1,713（若照抄补扫加 2） | **1,711** | — |

**关键实测**：重测件 §3.2 之推导式第 ④ 步「＋ 冻结后并发补扫 ＋2」，**该 2 件今日已在 `TRUE_GHOST` 桶内**（本棒实测：`a75dbfff187e` 与 `af5d2e3832cc` 皆 `IN_BUCKET`）⇒ **今日之「＋2」系重复计数**；而 10-22 之同 2 件时**不在**桶内（`a75dbfff187e` 不在、`af5d2e3832cc` 在 ⇒ 10-22 亦含 1 件重复）。
⇒ **今日之 1,710 含 2 件重复，10-22 之 1,350 含 1 件重复**；此即「＋360」与「＋359（去重式）」之差 **1** 的来处。

---

## §3 集合差（1,710 面 vs 1,350 面）

### 3.1 差之算式（三层，皆可复算）

| 层 | 本棒读丙 | 重测件读乙 | 10-22 在册读甲 |
|:--|--:|--:|--:|
| ① `TRUE_GHOST` 桶 | **1,737** | 1,737 | 1,379 |
| ② 漂移改指扣除 | **−26** | −29 | −31 |
| ③ ＝ `TG` | **1,711** | 1,708 | 1,348 |
| ④ ＋ 冻结后补扫 | 0（**已在桶内·再加即重复**） | ＋2 | ＋2 |
| ⑤ ＝ 门槛② 所计之真幽灵 | **1,711** | **1,710** | **1,350** |
| *去重（distinct）* | *1,711* | *1,708* | *1,349* |

### 3.2 成员面之集合差（读丙 vs 读甲·去重面）

| 集 | 件数 | 其义 |
|:--|--:|:--|
| **X** ＝ 今日在、10-22 不在 | **371** | **今日新增之真幽灵**（逐条定因见 §4） |
| **Y** ＝ 10-22 在、今日不在 | **9** | 今日掉出（见 §7） |
| 交集 | 1,340 | 两侧皆在（未变之真幽灵） |
| **净差** | **＋362** | ＝ 371 − 9（**去重式**）；照 10-22 之计数式（1,713 − 1,350）＝ **＋363** |

### 3.3 与 PI 所问「＋360」之对账（**不掩盖、不改写**）

| 差异项 | 件数 | 其因 |
|:--|--:|:--|
| PI 所问（重测件读乙 − 在册读甲，计数式） | **＋360** | ＝ 1,710 − 1,350 |
| 其中：今日重复计数多于 10-22 | **＋1** | 今日补扫 2 件已在桶内（10-22 仅 1 件已在）⇒ 计数式之差比去重式之差少 1 |
| **去重式之同口径差（读乙）** | **＋359** | ＝ 1,708 − 1,349 |
| 本棒读丙 与 重测件读乙 之差 | **＋3** | **漂移检出之仪器差**：本棒 `DRIFT_OLD` 27（真幽灵侧 26）vs 重测件 30（真幽灵侧 29）（见 §8-1） |
| **本棒读丙 之去重式差** | **＋362** | ＝ 1,711 − 1,349 ＝ 371 − 9 |

⚠ **本棒之逐条清单以「读丙 vs 读甲（去重面）」为对象**：重测件之逐件成员面**未落盘**（其 §8 自陈「中间表 **0 落盘**——本棒全部中间数据驻内存」），故逐件清单只能取本棒自扫面；此差 ＋3 之仪器差已登记于 §8-1，**⛔ 0 以「大致相符」带过**。

---

## §4 逐条定因（X ＝ 371 件·逐件）

### 4.1 定因之分布（主因互斥；副因旗标可并存）

| 主因 | 件数 | 占 X | 其义（白话） | 凭据（可逐件复算） |
|:--|--:|--:|:--|:--|
| **A 新落件引入新引用** | **16** | 4.3% | 该指纹在 10-22 源面**从未被引过**，今日始被引 | 10-22 源面候选集（`d2_22.cands`）无此指纹；今引者件之 mtime 皆晚于 10-22 |
| **B 某件被整理移动致引用失效** | **342** | 92.2% | 实体在 10-22 在盘；今日因 10-22/10-23 之整理而离可核面 | 见 §4.2 三类凭据 |
| **C 口径变更** | **9** | 2.4% | 实体未变而**判分规则/成对面**变了 | 漂移改指之判两读不同 5；git-blob 口径面变化 3；未成字节对→成对 1 |
| **仪器噪声** | **2** | 0.5% | **假阳性**：`000000000095`／`000000000096` 非哈希（全零前缀＋序号） | 字符串形态自证；**须修仪器**（加「非全零 12-hex」排除规则），⛔ 0 以之充因 |
| **未核得** | **2** | 0.5% | 事实面未闭合（见 §6） | 缺什么已逐件写明 |
| **小计** | **371** | 100% | | |

**副因旗标（可并存）**：A **20**｜B **311**｜C **36**｜E（态变型）**25**。

### 4.2 B 类之三类凭据（互斥分列·逐件可查）

| 凭据 | 件数 | 其凭据件 | 实体今日何在（实测） |
|:--|--:|:--|:--|
| **B1 移动映射表（10-22 整理之 279 件移动）** | **218** | `results/work/process/_reorg_move_mapping_2026_10_22.md`（`3384932a4054`）§1 逐件（279 行＝归档区 223／sub 56）＋§4「执行回执」（2026-10-22 21:0x·**实际移动 279·0 失败·279/279 移前移后 SHA-256 全等**） | 218 件之实体**今日仍在归档区全域**（按文件名命中 **223/223**）；**其指纹不可核**（归档区 0 哈希）⇒ 落真幽灵者乃**仪器面之限**，非实体之失 |
| **B2 合册 13 册之成员（原件删）** | **97** | `results/_book_01…_book_13_2026_10_22.md`（各册载成员清单：原文件名＋SHA-12＋bytes＋mtime） | 97 件之旧路径**今日皆不在盘**；其原文以「逐字节并置」存于所属册（信息不减） |
| **B3 垃圾候选（PI 16:52 裁·17:0x 可恢复删）** | **27** | 勘查案 §4-2 之 56 件垃圾候选表（号 1–26 ＝ 移动映射表 §2 所载「**26 件已经 PI 16:52 裁、已于 17:0x 可恢复删除**」者） | 今日不在盘（垃圾 56 件中今日不在盘者 **29** 件＝号 1–26 ＋ 41／45／46；其中落本棒 X 集者 **27**） |

**B1 之 218 与 217 之别**：218 件之指纹映射到移动映射表 **217 个行号**（#1–#223 之归档区段）——`audits_dataset_health.json` 一件被引于**两种口径**（SHA-256 `4f827071b0b8` ＋ git-blob `4a33af111f0f`）⇒ **1 行 2 指纹**。

**B2 之按册分布**：册 01（adoption_effect）**63**｜册 02（questionnaire_cards_intake）**12**｜册 03–13 各 **2** ⇒ 97。

---

## §5 `CARRY` 之正面处理（自扫以分离·⛔ 0 以「承索引」为免责语）

### 5.1 读差之逐件分离

承 10-22 之 GLM 索引者共 **18** 枚指纹（本棒实测：GLM 面 21 件·路径集与字节数与 10-22 **全等**、mtime 最晚 2026-10-19 00:47:02 ⇒ 承前值成立）。其逐件两侧落位：

| 面 | 10-22 桶 | 今日 `CARRY` 桶 | 今日 **盲读** 桶 |
|:--|:--|:--|:--|
| 18 件 | `FOUND_IN_REPO` **15**／`SAME_IDENTITY` **3** | 同左（**18/18 非真幽灵**） | **`TRUE_GHOST` 18/18** |

### 5.2 结论（可证·非免责语）

| 读 | 今日 | 10-22 侧同读法 | 差 |
|:--|--:|--:|--:|
| 两侧同**承**索引（读丙 vs 读甲） | **1,711** | 1,349 | **＋362** |
| 两侧同**盲读**（读丁 vs 读甲＋18） | **1,729** | 1,367 | **＋362** |

⇒ **`CARRY` 对「＋360 之差」之贡献 ＝ 0**（那 18 件在两侧**同**落非真幽灵，差中不增不减）；**自扫一遍（盲读）已分离并两读并出**，非以承索引免责。**若改以盲读，今日之数将为 1,729（在册之数不变）——采认归 PI。**

---

## §6 未核得（2 件）——缺什么才能判

| 指纹 | 所引实体（10-22 时） | 今日实况 | 缺什么才能判 |
|:--|:--|:--|:--|
| `30e6a3041078` | `tools\__pycache__\exp_harness.cpython-312.pyc`（39,384 B·9 引次） | 该 `.pyc` 今日不在盘；**同目录今日为 `exp_harness.cpython-314.pyc`**（解释器版本 312→314 之更替） | **缺：解释器重建／缓存清理之时刻与触发者之记录**（`.pyc` 非登记资产，无回执可查）。机制面已可推为「编译缓存随解释器版本更替」，然**时刻无凭据 ⇒ 不充 B 之凭据** |
| `e969ad69a634` | `verifier\audit\__pycache__\conservation.cpython-314.pyc`（27,641 B·3 引次） | 该 `.pyc` 与**其 `__pycache__` 目录**今日皆不在；仓内／sub／归档区**三处名册皆无其名** | **缺：`__pycache__` 清理之执行记录**（谁、何时、依何令）——`.pyc` 非登记资产，无回执可查 |

⇒ **本棒 0 编造归因**；此 2 件在两读中**恒为真幽灵**（实体三处皆无），其**因**待执行记录补齐后再判。

---

## §7 掉出计数之 9 件（Y）

| 项 | 件数 | 其因 |
|:--|--:|:--|
| 今日仍被引、但**不再成字节对**（引次 1–3） | **8** | **口径面变化**：所载字节值今日未被抽为「所载字节」⇒ 今日不入成对总体（与 C 类同族，方向相反） |
| 今日 `FOUND_IN_REPO`（实体归位） | **1**（`dde73101cf15`） | 实体今日在盘 ⇒ 掉出真幽灵面 |

---

## §8 仪器自审（三则·「测量仪器自身即误差源」）

| # | 缺陷 | 发现 | 处置 |
|:-:|:--|:--|:--|
| 1 | **漂移检出之仪器差（3 件）** | 本棒复刻 stage6（名称约束漂移：词元重合 ≥0.5·字节 ±10%）得 `DRIFT_OLD` **27**（真幽灵侧 26）；重测件得 **30**（真幽灵侧 29）⇒ `TG` 差 **3** | **登记差异，不回改任何件**；两读并出（§3.3）。其因**未核得**（两棒之候选集与 `ALLF` 皆异）——**须：漂移候选生成之逐件清单之两侧对照**方能闭合 |
| 2 | **全零串假阳性（2 件）** | `000000000095`／`000000000096` 被 12-hex 正则命中，然**非哈希**（全零前缀＋序号） | **修仪器不修文本**：判分前加「非全零 12-hex」之排除规则；**⛔ 0 以此 2 件充 A 之因**（其已剔出主因分布） |
| 3 | **移动映射表「新路径」栏与实况不符** | 映射表 §1 载新路径为**扁平名**（`_movedout_2026_10_22\<扁平名>`）；实况为**保结构**之 6 子目录（`doc`／`evidence`／`readout`／`tool`／`verdict`／`work`）⇒ **按映射表所载路径 0/279 命中**，按**文件名**则 **223/223 命中**（归档区）＋**56/56**（sub） | **登记级勘误（只登记·⛔ 0 回改原表一字）**：该表 §4-2 自陈「本表『旧→新』两栏即**登记载荷**」⇒ 其**路径栏失准**，致「旧→新」登记**不可按路径照抄**；本棒之 B1 定因以**文件名＋实体在盘**为据（不以其路径栏为据） |

---

## §9 两读并出（⛔ 0 以定因之果径改 1,710 或 1,350 之登记）

| 读 | 值 | 口径 | 时点 | 来源 |
|:--|--:|:--|:--|:--|
| **读甲** | **1,350**（distinct 1,349） | 族甲·`MISSING_TRUE`／真幽灵 | 2026-10-22 01:1x | **转引**＋**重建校验**（`TRUE_GHOST` 1,379 −31 ＋2 ＝ 1,350，MATCH） |
| **读乙** | **1,710**（distinct 1,708） | 族甲·同口径·**承** GLM 索引 | 2026-10-23 14:51:51–15:00:50 | **转引**：依据件 §3.2 |
| **读丙** | **1,711** | 族甲·同口径·**承** 10-22 之 GLM 索引（as-of 源面） | 2026-10-23 15:43–16:0x | **实算**（本棒自扫） |
| **读丁** | **1,729** | 族甲·同口径·**GLM 盲读**（0 承索引） | 同上 | **实算**（`CARRY` 分离读） |
| **读戊／己** | **1,712／1,730** | 全源面 1,335 ＋ 承／盲读 | 同上 | **实算** |

**差**：PI 所问 **＋360**（读乙−读甲·计数式）；**去重式** ＋359（读乙）／**＋362**（读丙）；**`CARRY` 对差之贡献 ＝ 0**。
⚠ **数值之采认归 PI**（PI v246 §2-4-3 逐字：「⛔ 0 以重测值径换在册值——两读并出，数值之采认归 PI。」）——本棒**⛔ 0 改在册之 1,350 一字**，⛔ 0 改重测件之 1,710 一字，⛔ 0 落五终判，⛔ 0 闭 KD，⛔ 0 宣告段毕，**⛔ 0 宣告门槛② 成就**。

---

## §10 未核得面（⛔ 0 充 0）

| # | 面 | 状态 | 其于本数之影响 |
|:-:|:--|:--|:--|
| 1 | **远端面（GitHub 认可面）** | ⛔ 0 联网·未测 | 判定止于「本机可核面 0 实存」；**「不在本地」≠「不存在」** |
| 2 | **归档区 40,242 件** | 0 读内容／0 哈希；**未参与判定分支** | **B1 之 218 件**（＋其同族）实体在而指纹不可核 ⇒ 落真幽灵者乃**仪器面之限** |
| 3 | **GLM 21 件** | 0 读内容；承 10-22 索引（路径集与字节数全等·mtime 全早于冻结点） | 盲读与承索引两读之差 **18**（§5） |
| 4 | **漂移候选之两侧清单** | 未在册 | **3 件**之仪器差未闭合（§8-1） |
| 5 | **`.pyc` 编译缓存之清理/重建记录** | 未在册（非登记资产） | **2 件**未核得之因（§6） |
| 6 | **垃圾 56 件中号 41／45／46 之删除回执** | 未在册（PI 16:52 裁之 26 件之外） | 该 3 件今日已不在盘，然其指纹未落今日新增面（不在 X 集）⇒ **于本差无涉** |
| 7 | **`CONFLICT` 支** | 本族（指纹级）无对应分支 | 今日未给数（**非 0**） |
| 8 | **候选对数（sha12×bytes 去重）** | 未单列 | 今日成对总体以「唯一指纹」表之 |

---

## §11 老实交代（failures & limitations · 0 软化）

1. ⚠ **本棒之逐件清单基于「本棒自扫面」，非重测件之成员面**——重测件 §8 自陈「中间表 **0 落盘**」，其 1,710 之逐件成员面**不可取**；故本件之 X＝371 系「读丙（as-of）vs 读甲（去重面）」之差，**与 PI 所问之 ＋360 差 ＋2**（＝ 计数式重复 1 ＋ 漂移仪器差 3 − 重测件自身之 +1 重复差）。**两读并出，采认归 PI。**
2. ⚠ **本棒之读丙较重测件之 TG 多 3**（漂移检出之仪器差，§8-1）——**未核得**，缺「漂移候选生成之逐件清单之两侧对照」。
3. ⚠ **今日之「＋2 冻结后补扫」经实测系重复计数**（该 2 件已在今日 `TRUE_GHOST` 桶内）——此为**重测件推导式之口径缺口**，**本棒只登记、⛔ 0 回改其件一字**。
4. ⚠ **B1 之 218 件**：实体**在归档区**（223/223 按名命中），惟归档区 0 哈希故本仪器不可核 ⇒ 其落真幽灵**为仪器面之限**，非实体之失；若采「实体在即非真幽灵」之读，**今日值将为 1,711 − 218 ＝ 1,493**（第三读，**列此供 PI 裁，本棒 ⛔ 0 代裁**）。
5. ⚠ **B2 之 97 件**：合册之定义是「逐字节并置·信息不减」，故**其内容今日仍在册内**；然**原路径已失效** ⇒ 旧指纹之失效**为路径面之失效**，非内容之亡。同上，第三读之数为 1,711 − 97 ＝ 1,614。
6. ⚠ **B3 之 27 件**：垃圾候选之删除有 PI 16:52 之裁与 17:0x 之执行（承移动映射表 §2 之述），然**本棒未在册中见逐件删除回执**——**据凭据件文字定因，登记为「据载」**。
7. ⚠ **本棒 0 代裁**——⛔ 0 落五终判・⛔ 0 闭 KD・⛔ 0 宣告段毕・⛔ 0 宣告任何门槛成就・⛔ 0 以定因之果径改 1,710 或 1,350 之登记。
8. ⚠ **本棒 0 联网・0 跑实验・0 调 LLM／API・0 读 GLM 内容・0 读归档区内容**（二者皆仅名／元数据）。

---

## §12 触动 0 之实证

| 面 | 证据 |
|:--|:--|
| 既有件 | **0 回改**——本棒唯一新立件为本件；`results\` 与 `pi_rulings\` 内无一件被本棒改写 |
| 移动／重命名／删除 | **0**——全程 0 次移动、0 次重命名、0 次删除 |
| 新建目录 | **0**——`results\evidence\register\` 为既有目录（321 件） |
| 归档区 | **0 写入、0 读内容、0 哈希**——仅 `os.walk` 列名与计数（40,242） |
| GLM 面 | **0 读内容、0 哈希**——仅名／字节／mtime 之元数据（21 件，与 10-22 全等） |
| 联网 | **0 次** |
| 中间表 | 落于 `.tmp\`（**8 件脚本 ＋ 6 件中间表**，皆本棒新立，非登记件）——**声明之，不充件** |
| `.env`／凭据 | **0 读** |

---

## §13 逐条清单（X ＝ 371 件·逐条）

**读法**：表列＝指纹｜**主因**（互斥：A 新引用／B 整理移动致失效／C 口径变更／仪器噪声／未核得）｜**副因旗标**（可并存：A／B／C／E）｜所指名（自引用语境抽）｜所载 bytes｜**凭据**（可逐件复算：移动映射表行号与新旧路径／合册名与成员名／垃圾候选表号／口径判分／仪器形态）。

| 指纹 | 主因 | 副因 | 所指名 | bytes | 凭据 |
|:--|:--|:--|:--|--:|:--|
| `16df5a41482c` | A | A＋C |  | 66724 | 10-22 源面未引此指纹 ⇒ 引用系新引入（引者含今日新落件） |
| `37c4d7bad0c3` | A | A＋C | _v3s44_ci_width_2026_10_23.md | 52858 | 10-22 源面未引此指纹 ⇒ 引用系新引入（引者含今日新落件） |
| `3bb94431d777` | A | A＋C |  | 46326 | 10-22 源面未引此指纹 ⇒ 引用系新引入（引者含今日新落件） |
| `3f18caf36805` | A | A＋C |  | 611217 | 10-22 源面未引此指纹 ⇒ 引用系新引入（引者含今日新落件） |
| `5f5491244709` | A | A＋C |  | 32484 | 10-22 源面未引此指纹 ⇒ 引用系新引入（引者含今日新落件） |
| `60a521cbeed3` | A | A＋C | rs_register_2026_10_16_v26.md | 46074 | 10-22 源面未引此指纹 ⇒ 引用系新引入（引者含今日新落件） |
| `6f59bc92900d` | A | A＋C | eta 五值择优预实验报告 | 13009 | 10-22 源面未引此指纹 ⇒ 引用系新引入（引者含今日新落件） |
| `71ee14203a52` | A | A＋C | _b8_b6_retention_plan_2026_10_22.md | 344296 | 10-22 源面未引此指纹 ⇒ 引用系新引入（引者含今日新落件） |
| `798c9f999b5b` | A | A＋C | 采认五位处置回函 | 28817 | 10-22 源面未引此指纹 ⇒ 引用系新引入（引者含今日新落件） |
| `9c2549047429` | A | A＋C | _h_exact_domain2_run_2026_10_22.md | 44762 | 10-22 源面未引此指纹 ⇒ 引用系新引入（引者含今日新落件） |
| `abc2a77667a8` | A | A＋C | _ps41_heldout54_2026_10_23.md | 19657 | 10-22 源面未引此指纹 ⇒ 引用系新引入（引者含今日新落件） |
| `bfe4b43f901e` | A | A＋C | _v186_v225_adoption_effect_2026_10_22.md | 262477 | 10-22 源面未引此指纹 ⇒ 引用系新引入（引者含今日新落件） |
| `c341cfa3fd19` | A | A＋C | _reorg_dirrule_content_criteria_supplement_hardforbid_2026_10_22.md | 12146 | 10-22 源面未引此指纹 ⇒ 引用系新引入（引者含今日新落件） |
| `d6a29069b00b` | A | A＋C |  | 55738 | 10-22 源面未引此指纹 ⇒ 引用系新引入（引者含今日新落件） |
| `df191c9f5589` | A | A＋C |  | 48782 | 10-22 源面未引此指纹 ⇒ 引用系新引入（引者含今日新落件） |
| `e7f953ce25f6` | A | A＋C | m_diff_2026_10_22.md | 75817 | 10-22 源面未引此指纹 ⇒ 引用系新引入（引者含今日新落件） |
| `00799137a44f` | B | B |  | 1360 | 垃圾候选表 #10 .tmp/m08_llm_calls_2026_10_16.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `00ee97c82dcc` | B | B |  | 416460 | 移动映射表 #24：results/deposon_v15_diffusion_maxpath_negativeresult.json → 〔归档件引用·未上传:_moved〕 |
| `01abdb24de65` | B | B | _v149_adoption_effect_2026_10_20.md | 116942 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v149_adoption_effect_2026_10_20.md》 |
| `01c492a97b98` | B | B |  | 4123 | 移动映射表 #153：corpus/v20/S2_n60.json → 〔归档件引用·未上传:corpus___v20___S2_n〕 |
| `01d9c95ea690` | B | B |  | 3320 | 移动映射表 #176：corpus/v20/S6.json → 〔归档件引用·未上传:corpus___v20___S6.json（〕 |
| `023834aaa293` | B | B | _questionnaire_cards_intake_register_supplement_6_receipt_v2_2026_10_10.md | 11756 | 合册成员：_book_12_questionnaire_cards_intake_register_supplement_6_2026_10_22.md《_questionnaire_cards_intake_regis |
| `03c8baa18d93` | B | B | REFACTOR_v2.md | 23042 | 移动映射表 #57：docs/REFACTOR_v2.md → 〔归档件引用·未上传:docs___REFACTOR_v2.md（去〕 |
| `04b90b638bdc` | B | B | _v3_v4_ghostref_reconciliation_2026_09_23.md | 65105 | 移动映射表 #40：results/deposon_v20_gt6.json → 〔归档件引用·未上传:results___depo〕 |
| `04f2920e259a` | B | B | _m41_double_readout_contrast_exec_2026_10_14.md | 17009 | 合册成员：_book_10_m41_double_readout_contrast_exec_2026_10_22.md《_m41_double_readout_contrast_exec_2026_10_14.md》 |
| `063ac8d00542` | B | B |  | 25049 | 移动映射表 #53：results/deposon_v3_v7_summary_2026_09_11.json → 〔归档件引用·未上传:_movedout_2026_10_〕 |
| `0789214e950e` | B | E | _v150_adoption_effect_2026_10_20.md | 125071 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v150_adoption_effect_2026_10_20.md》 |
| `088f28524a1d` | B | B |  | 4276 | 移动映射表 #150：results/_p_n_curvature_potential_coupling_2026_09_16/p_n_curvature_potential_coupling_results_2026_ |
| `0984955b0370` | B | B | _questionnaire_cards_intake_register_supplement_6_receipt_2026_10_10.md | 11752 | 合册成员：_book_12_questionnaire_cards_intake_register_supplement_6_2026_10_22.md《_questionnaire_cards_intake_regis |
| `0a8ed127d6de` | B | B | **在盘上不存在** ⇒ 计数反转**0 逐行代码审计** ／ 根因结论（计数反转）建立在**盘上 | 24435 | 移动映射表 #54：results/deposon_v42_v2_miss_rate_curve_2026_09_16.json → 〔归档件引用·未上传:_movedout〕 |
| `0b7893196d0b` | B | B | tref_reconciliation_2026_09_23.md | 6796 | 移动映射表 #113：results/deposon_v20_photonics.json → 〔归档件引用·未上传:results〕 |
| `0bda45a5577f` | B | A＋B＋C |  | 128407 | 垃圾候选表 #2 .tmp/_w_h_exact_pathA_trace_2026_10_21.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `0c3ede881fb1` | B | B |  | 6466 | 移动映射表 #119：results/deposon_volcengine_glm_latest_5cells_v2_2026_09_10.json → 〔归档区〕 |
| `0c49f2d36088` | B | B | post_draft_verification_v2X.md | 9979 | 移动映射表 #93：reviews/post_draft_verification_v2X.md → 〔归档件引用·未上传:revi〕 |
| `0c7ad5235ae9` | B | B |  | 3562 | 移动映射表 #168：corpus/v20/L_biological_taxonomy.json → 〔归档件引用·未上传:corp〕 |
| `0cb1decec878` | B | B | _t3trap_answerable_build_exec_2026_10_15.md | 5250 | 垃圾候选表 #21 .tmp/t3_nt_llm_calls_2026_10_15.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `0db0fe46bdae` | B | B | _v166_adoption_effect_2026_10_20.md | 129389 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v166_adoption_effect_2026_10_20.md》 |
| `0e02218d80e5` | B | B | _v140_adoption_effect_2026_10_19.md | 119434 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v140_adoption_effect_2026_10_19.md》 |
| `0e8c9664b06d` | B | B | _m08_measured_enumeration_exec_2026_10_16.md | 8271 | 垃圾候选表 #11 .tmp/m08_r1_llm_calls_2026_10_16.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `0f36aaeeda6f` | B | B | SYNTHESIS_mind_game.md | 9191 | 移动映射表 #96：docs/SYNTHESIS_mind_game.md → 〔归档件引用·未上传:docs___SYNTHESI〕 |
| `0f8532aefdff` | B | B | 之 hunk 行、 | 3463 | 垃圾候选表 #25 .tmp/whitelist_backup_2026_10_17/t3_harness_diff_2026_10_15.diff（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `0f933318d5a1` | B | E | _v169_adoption_effect_2026_10_20.md | 137346 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v169_adoption_effect_2026_10_20.md》 |
| `105413bee0ba` | B | B | _h5_session_census_2026_10_19_part2.md | 451607 | 合册成员：_book_04_h5_session_census_2026_10_22.md《_h5_session_census_2026_10_19_part2.md》 |
| `106e8667be2d` | B | B |  | 72704 | 移动映射表 #1：results/_exp04_h_contrast_readings_2026_10_10.json → 〔归档件引用·未上传:_movedout_2026〕 |
| `108da40d5d4e` | B | B | tref_reconciliation_2026_09_23.md | 44443 | 移动映射表 #42：results/deposon_v19_meanfield.json → 〔归档件引用·未上传:results_〕 |
| `110607514753` | B | B |  | 5056 | 移动映射表 #136：docs/space_release_log.json → 〔归档件引用·未上传:docs___space_r〕 |
| `11681f0ad861` | B | B | _questionnaire_cards_intake_register_supplement_3_2026_10_10.md | 67225 | 合册成员：_book_02_questionnaire_cards_intake_register_2026_10_22.md《_questionnaire_cards_intake_register_supplemen |
| `116d193b1607` | B | B | outline_v2X.md | 10476 | 移动映射表 #90：paper/v2/outline_v2X.md → 〔归档件引用·未上传:paper___v2___outlin〕 |
| `128b4167afd5` | B | E | _v180_v182_adoption_effect_2026_10_21.md | 215227 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v180_v182_adoption_effect_2026_10_21.md》 |
| `12e0de4bb103` | B | B |  | 4329 | 移动映射表 #148：corpus/v20/L_historical_causality.json → 〔归档件引用·未上传:cor〕 |
| `131d0e0d0636` | B | C | _questionnaire_cards_intake_register_supplement_3_2026_10_10.md | 67225 | 合册成员：_book_02_questionnaire_cards_intake_register_2026_10_22.md《_questionnaire_cards_intake_register_supplemen |
| `14d3e53d90a8` | B | B | _v157_adoption_effect_2026_10_20.md | 109343 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v157_adoption_effect_2026_10_20.md》 |
| `153c64328abc` | B | B | _v155_adoption_effect_2026_10_20.md | 89658 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v155_adoption_effect_2026_10_20.md》 |
| `1665f367b2c4` | B | B |  | 9068 | 移动映射表 #15：results/_v4_pi_cot_v2_result.json → 〔归档件引用·未上传:results__〕 |
| `17826a907207` | B | B | _h5_session_census_2026_10_19_part1.md | 206469 | 合册成员：_book_04_h5_session_census_2026_10_22.md《_h5_session_census_2026_10_19_part1.md》 |
| `1903cc498578` | B | E |  | 230412 | 垃圾候选表 #6 .tmp/ge01_full_1494_llm_calls_2026_10_16.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `192bd0e58826` | B | E | ·116,942 B·522 LF·mtime **2026-10-20 11:31:26.201** —— 📌 **其 §9-7 自报之终态前值 ＝ | 110673 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v149_adoption_effect_2026_10_20.md》 |
| `193386b9f23c` | B | B | _questionnaire_cards_intake_register_supplement_2026_10_09.md | 72199 | 合册成员：_book_02_questionnaire_cards_intake_register_2026_10_22.md《_questionnaire_cards_intake_register_supplemen |
| `19555b7d9d43` | B | B |  | 6750 | 移动映射表 #114：reviews/data/t2_linkpred.csv → 〔归档件引用·未上传:reviews___dat〕 |
| `19fa12f4e053` | B | B | _m41_double_readout_contrast_exec_2026_10_15.md | 24253 | 垃圾候选表 #15 .tmp/m41_rerun_llm_calls.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `1ad43c70cf01` | B | C | _questionnaire_cards_intake_register_supplement_6_2026_10_10.md | 106453 | 合册成员：_book_02_questionnaire_cards_intake_register_2026_10_22.md《_questionnaire_cards_intake_register_supplemen |
| `1ded6731cc27` | B | B |  | 2398383 | 移动映射表 #19：results/deposon_v2_phase3_strip_embeddings_2026_09_11.json → 〔归档件引用·未上传:_move〕 |
| `1e15e7611597` | B | E | _v159_adoption_effect_2026_10_20.md | 115240 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v159_adoption_effect_2026_10_20.md》 |
| `1e4c065da058` | B | B |  | 5916 | 移动映射表 #125：results/_p_o_stranger_verification_2026_09_16/p_o_stranger_verification_results_2026_09_16.json → D |
| `1ec7aba6afd8` | B | B | tref_reconciliation_2026_09_23.md | 7842 | 移动映射表 #105：results/deposon_v19_quickwins.json → 〔归档件引用·未上传:results〕 |
| `20526a028b26` | B | B | _v167_adoption_effect_2026_10_20.md | 143845 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v167_adoption_effect_2026_10_20.md》 |
| `20bc4288e0de` | B | B | econciliation_2026_09_23.md | 9176 | 移动映射表 #97：results/deposon_v16_paired_stats.json → 〔归档件引用·未上传:resul〕 |
| `218ef1a99f97` | B | B |  | 11703 | 移动映射表 #10：results/deposon_volcengine_minimax_m3_30cells_2026_09_10.py → 〔归档件引用·未上传:_mov〕 |
| `23e5910d80c8` | B | B | _v143_v144_adoption_effect_2026_10_19.md | 184744 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v143_v144_adoption_effect_2026_10_19.md》 |
| `25f90f106451` | B | B | variant_params_table.md | 4035 | 移动映射表 #156：docs/variant_params_table.md → 〔归档件引用·未上传:docs___varian〕 |
| `2628f74421f2` | B | B |  | 1875 | 移动映射表 #202：reviews/data/t2e_nettack.csv → 〔归档件引用·未上传:reviews___dat〕 |
| `26abab740b0c` | B | B | _v175_adoption_effect_2026_10_21.md | 145012 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v175_adoption_effect_2026_10_21.md》 |
| `27574d8f93ed` | B | B | _v153_adoption_effect_2026_10_20.md | 181493 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v153_adoption_effect_2026_10_20.md》 |
| `2764e9e0cf8b` | B | E | _v156_adoption_effect_2026_10_20.md | 84694 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v156_adoption_effect_2026_10_20.md》 |
| `27f9bd5cc260` | B | B |  | 17591 | 移动映射表 #70：results/deposon_v3_physical_opt_2026_09_11.json → 〔归档件引用·未上传:_movedout_2026_1〕 |
| `2816b9e0bba8` | B | B | _v170_adoption_effect_2026_10_20.md | 158298 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v170_adoption_effect_2026_10_20.md》 |
| `2836605ca12f` | B | B | ef_reconciliation_2026_09_23.md | 16896 | 移动映射表 #74：results/deposon_v17_multigraph.json → 〔归档件引用·未上传:results〕 |
| `283dbc8c5b63` | B | B | econciliation_2026_09_23.md | 35718 | 移动映射表 #46：results/deposon_v20_bigquiz_eval.json → 〔归档件引用·未上传:resul〕 |
| `2907006dbe48` | B | B | v3_v4_ghostref_reconciliation_2026_09_23.md | 56425 | 移动映射表 #41：results/deposon_v20_gt5b.json → 〔归档件引用·未上传:results___dep〕 |
| `29dcdaa29ec4` | B | B | _v158_adoption_effect_2026_10_20.md | 114409 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v158_adoption_effect_2026_10_20.md》 |
| `2a7749da7c4d` | B | B |  | 9996 | 移动映射表 #13：results/c5_b_group_fix_readings_2026_10_01.json → 〔归档件引用·未上传:_movedout_2026_1〕 |
| `2b88948dca19` | B | B | _v3_v4_ghostref_reconciliation_2026_09_23.md | 5396 | 移动映射表 #130：results/deposon_v20_gt8.json → 〔归档件引用·未上传:results___dep〕 |
| `2d7416841382` | B | B | _v154_adoption_effect_2026_10_20.md | 148255 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v154_adoption_effect_2026_10_20.md》 |
| `2dc8ca9e36c1` | B | B |  | 4336 | 移动映射表 #147：results/deposon_risk1_02940_decision_2026_09_11.json → 〔归档件引用·未上传:_movedout_〕 |
| `2e55c53be25d` | B | B |  | 111710 | 移动映射表 #31：results/deposon_openrouter_5model_rag_30cells_2026_09_10.json → 〔归档件引用·未上传:_m〕 |
| `2f0765a1d39d` | B | B | P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md | 12501 | 移动映射表 #84：docs/V3X/P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md → 〔归档件引用·未上传:_movedout_2026_〕 |
| `301e682f04ce` | B | E | _v143_v144_adoption_effect_2026_10_19.md | 143469 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v143_v144_adoption_effect_2026_10_19.md》 |
| `3092bd586f82` | B | E | _v152_adoption_effect_2026_10_20.md | 128498 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v152_adoption_effect_2026_10_20.md》 |
| `32ca32c00da4` | B | B |  | 3898 | 移动映射表 #158：corpus/v20/L_project_management.json → 〔归档件引用·未上传:corpu〕 |
| `32d26cb09568` | B | B | Findings_v2.0_crossval.md | 4566 | 移动映射表 #143：docs/Findings_v2.0_crossval.md → 〔归档件引用·未上传:docs___Find〕 |
| `33478e048831` | B | E | _v153_adoption_effect_2026_10_20.md | 165732 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v152_adoption_effect_2026_10_20.md》 |
| `33ad1c01f745` | B | B | _criterion_application_scope_prereg_2026_10_01.md | 20398 | 移动映射表 #8：results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json → 〔归档件引用·未上传:_mo〕 |
| `3545c01e1291` | B | B | SPEC_GT8B.md | 7486 | 移动映射表 #107：docs/SPEC_GT8B.md → 〔归档件引用·未上传:docs___SPEC_GT8B.md（去处＝归〕 |
| `35b676773243` | B | B | _v3_v4_ghostref_reconciliation_2026_09_23.md | 7844 | 移动映射表 #104：results/deposon_v20_gt3.json → 〔归档件引用·未上传:results___dep〕 |
| `36c714eabe3b` | B | B | Findings_v2.0_boss.md | 3642 | 移动映射表 #166：docs/Findings_v2.0_boss.md → 〔归档件引用·未上传:docs___Findings〕 |
| `39f79fce7cdb` | B | B |  | 208350 | 移动映射表 #27：results/deposon_benchmark_v1_4_gsm8k_details.json → 〔归档件引用·未上传:_movedout_2026〕 |
| `3a0c5c38de03` | B | B | _v164_adoption_effect_2026_10_20.md | 120622 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v164_adoption_effect_2026_10_20.md》 |
| `3b1c881c4594` | B | B |  | 132875 | 移动映射表 #29：audits_outliers.json → 〔归档件引用·未上传:audits_outliers.json（去〕 |
| `3b6879ab2440` | B | B |  | 2297 | 移动映射表 #196：corpus/v20/S3.json → 〔归档件引用·未上传:corpus___v20___S3.json（〕 |
| `3d7a2a35ef4b` | B | A＋B＋C | _gd03_divergence_deliberation_v2_2026_10_21.md | 60961 | 合册成员：_book_06_gd03_divergence_deliberation_2026_10_22.md《_gd03_divergence_deliberation_v2_2026_10_21.md》 |
| `3db2360cd03d` | B | B | _v174_adoption_effect_2026_10_21.md | 133729 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v174_adoption_effect_2026_10_21.md》 |
| `3e3a5014cb0e` | B | B | SPEC_v2.0_amendment1.md | 4743 | 移动映射表 #141：docs/SPEC_v2.0_amendment1.md → 〔归档件引用·未上传:docs___SPEC_v〕 |
| `3e68a203fa06` | B | B |  | 106119 | 垃圾候选表 #18 .tmp/ritt_remeasure_llm_calls_2026_10_17.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `3ebd023879a5` | B | E | _v157_adoption_effect_2026_10_20.md | 84135 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v157_adoption_effect_2026_10_20.md》 |
| `3ecb285db3d8` | B | B | review_realign_v2X.md | 7338 | 移动映射表 #109：reviews/review_realign_v2X.md → 〔归档件引用·未上传:reviews___re〕 |
| `3fa0ff2c8c08` | B | B |  | 10096 | 移动映射表 #92：results/deposon_game_theory_eval_2026_09_10.json → 〔归档件引用·未上传:_movedout_2026_〕 |
| `432ec337d586` | B | B | SPEC_GT3.md | 5369 | 移动映射表 #132：docs/SPEC_GT3.md → 〔归档件引用·未上传:docs___SPEC_GT3.md（去处＝归档区〕 |
| `43731392b581` | B | B | Findings_v2.0_skills.md | 3456 | 移动映射表 #170：docs/Findings_v2.0_skills.md → 〔归档件引用·未上传:docs___Findin〕 |
| `43d9ce160fc8` | B | B |  | 2460 | 移动映射表 #194：results/boss_pc_1_real_2d_ising_2026_09_15.json → 〔归档件引用·未上传:_movedout_2026_〕 |
| `47177cab0303` | B | B |  | 9527 | 移动映射表 #14：results/_v5_item21_anchor_recompute_2026_09_28.json → 〔归档件引用·未上传:_movedout_20〕 |
| `48edf1b5dd53` | B | B | _results_index_2026_10_21.md | 233679 | 合册成员：_book_05_results_index_2026_10_22.md《_results_index_2026_10_21.md》 |
| `49028967ad57` | B | B |  | 3405 | 移动映射表 #172：reviews/data/t3d_llmmd.csv → 〔归档件引用·未上传:reviews___data_〕 |
| `497b9c2d6746` | B | B | _v3_v4_ghostref_reconciliation_2026_09_23.md | 3803 | 移动映射表 #162：results/deposon_v20_gt.json → 〔归档件引用·未上传:results___depo〕 |
| `4a0689892c1b` | B | B |  | 1724 | 移动映射表 #204：corpus/v20/S6_n20.json → 〔归档件引用·未上传:corpus___v20___S6_n〕 |
| `4a08521f8de1` | B | B | V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md | 38545 | 移动映射表 #45：docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md → 〔归档件引用·未上传:_movedout_2026_〕 |
| `4a33af111f0f` | B | C |  | 7398 | 移动映射表 #108：audits_dataset_health.json → 〔归档件引用·未上传:audits_dataset_〕 |
| `4a85ae03c395` | B | C | _questionnaire_cards_intake_register_supplement_2026_10_09.md | 72199 | 合册成员：_book_02_questionnaire_cards_intake_register_2026_10_22.md《_questionnaire_cards_intake_register_supplemen |
| `4a9b6c5e47af` | B | B | **／68,272 B／mtime **2026-10-20 23:13:08** ｜② **数据件** | 61109 | 移动映射表 #3：results/_runface_vs_shape_multidim_reading_2026_10_20.json → 〔归档件引用·未上传:_moved〕 |
| `4b020eb04605` | B | B | ／ ✅ **沿录**（本棒复算 v1／v2／v3 指纹**逐位一致**： | 10701 | 移动映射表 #12：results/_ge01_prereg_5anchor.json → 〔归档件引用·未上传:results__〕 |
| `4b10f9cae09f` | B | B |  | 3319 | 移动映射表 #177：corpus/v20/S5.json → 〔归档件引用·未上传:corpus___v20___S5.json（〕 |
| `4b11b1bd8ada` | B | B | _reconciliation_2026_09_23.md | 1018 | 移动映射表 #218：results/deposon_v20_gt8c_ingest.json → 〔归档件引用·未上传:resul〕 |
| `4b792e20f34f` | B | E | _v154_adoption_effect_2026_10_20.md | 115416 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v154_adoption_effect_2026_10_20.md》 |
| `4e4a17d43adf` | B | B |  | 13562 | 移动映射表 #81：results/deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json → 〔归档区〕 |
| `4ec04d3d7d8c` | B | B |  | 32995 | 移动映射表 #49：results/deposon_volcengine_glm_latest_30cells_v2_2026_09_10.json → 〔归档区〕 |
| `4f3242b2a661` | B | B | Findings_GT3.md | 2632 | 移动映射表 #189：docs/Findings_GT3.md → 〔归档件引用·未上传:docs___Findings_GT3.m〕 |
| `4f827071b0b8` | B | B |  | 7398 | 移动映射表 #108：audits_dataset_health.json → 〔归档件引用·未上传:audits_dataset_〕 |
| `4ff033ec583d` | B | E | _v145_adoption_effect_2026_10_20.md | 168666 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v145_adoption_effect_2026_10_20.md》 |
| `506810017d34` | B | B |  | 25464 | 移动映射表 #52：results/deposon_volcengine_worker_a_2026_09_10.json → 〔归档件引用·未上传:_movedout_20〕 |
| `509dcee3b139` | B | B |  | 27311 | 移动映射表 #51：results/deposon_pf_implementation_2026_09_11.json → 〔归档件引用·未上传:_movedout_2026〕 |
| `509e17caa955` | B | E | _v180_v182_adoption_effect_2026_10_21.md | 228636 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v180_v182_adoption_effect_2026_10_21.md》 |
| `5149f5cafcf9` | B | B |  | 23034 | 移动映射表 #58：results/deposon_volcengine_seed_code_30cells_2026_09_10.json → 〔归档件引用·未上传:_mo〕 |
| `515ad357fac8` | B | B | _achievements_inventory_full_2026_10_18.md | 805428 | 合册成员：_book_03_achievements_inventory_full_2026_10_22.md《_achievements_inventory_full_2026_10_18.md》 |
| `51b271548835` | B | B | BASELINE_REGISTRY.md | 3356 | 移动映射表 #174：docs/BASELINE_REGISTRY.md → 〔归档件引用·未上传:docs___BASELINE_〕 |
| `523b5941c30c` | B | B |  | 16835 | 移动映射表 #76：results/_v3x_p_l_v3_mistral_large_2512_20260917_115049.json → 〔归档件引用·未上传:_mov〕 |
| `52b4d6e52ae9` | B | B |  | 3171 | 移动映射表 #181：corpus/v20/S1_n45.json → 〔归档件引用·未上传:corpus___v20___S1_n〕 |
| `5376f4aae453` | B | C | _questionnaire_cards_intake_register_supplement_5_2026_10_10.md | 77189 | 合册成员：_book_02_questionnaire_cards_intake_register_2026_10_22.md《_questionnaire_cards_intake_register_supplemen |
| `54ad4d2cd8bf` | B | B | _t3_repro_probe_2026_10_16.md | 7441 | 垃圾候选表 #22 .tmp/t3_repro_probe_llm_calls_2026_10_16.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `54fd5220ccd1` | B | B | _v159_adoption_effect_2026_10_20.md | 119076 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v159_adoption_effect_2026_10_20.md》 |
| `552aa383c51f` | B | E | _v180_v182_adoption_effect_2026_10_21.md | 223841 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v180_v182_adoption_effect_2026_10_21.md》 |
| `553c90aa3ba6` | B | B |  | 1610 | 移动映射表 #208：audits_security.json → 〔归档件引用·未上传:audits_security.json（〕 |
| `55428f6bd848` | B | B | _reconciliation_2026_09_23.md | 3041 | 移动映射表 #183：results/deposon_g1_mindmap_demo.json → 〔归档件引用·未上传:resul〕 |
| `556086d9e3bc` | B | B |  | 106125 | 移动映射表 #34：results/deposon_v17_fusion_fix_tieartifact_negativeresult.json → 〔归档件引用·未上传:_〕 |
| `56401317e62b` | B | B |  | 18592 | 移动映射表 #65：results/deposon_deepseek_v41_flash_30cells_v3_2026_09_10.json → 〔归档件引用·未上传:_m〕 |
| `56ecef878539` | B | B | experiment_design_v19.md | 8840 | 移动映射表 #101：reviews/experiment_design_v19.md → 〔归档件引用·未上传:reviews__〕 |
| `5749ce2c5bf7` | B | B |  | 5377 | 移动映射表 #131：reviews/data/t2d_hiding.csv → 〔归档件引用·未上传:reviews___data〕 |
| `576eaf8d7431` | B | B |  | 11341 | 移动映射表 #87：results/deposon_p_k_cross_subject_fingerprint_blind_test_2026_09_16.json → 〔本地路径已脱敏〕 |
| `584de37ebec1` | B | B |  | 4122 | 移动映射表 #154：corpus/v20/S1_n60.json → 〔归档件引用·未上传:corpus___v20___S1_n〕 |
| `5864bbe5adae` | B | B | Findings_v2.0_corrections.md | 5012 | 移动映射表 #137：docs/Findings_v2.0_corrections.md → 〔归档件引用·未上传:docs___F〕 |
| `586cc2f62fb6` | B | B | _v156_adoption_effect_2026_10_20.md | 101278 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v156_adoption_effect_2026_10_20.md》 |
| `58ab335ca341` | B | B |  | 4894 | 移动映射表 #139：results/deposon_volcengine_9model_30cells_2026_09_10.json → 〔归档件引用·未上传:_move〕 |
| `58bb0a7d2e46` | B | B |  | 3175 | 移动映射表 #180：corpus/v20/S2_n45.json → 〔归档件引用·未上传:corpus___v20___S2_n〕 |
| `594d7a8d3de8` | B | B |  | 17085 | 移动映射表 #71：results/deposon_pe_d1_d3_2026_09_15.json → 〔归档件引用·未上传:re〕 |
| `595699b7ec44` | B | B | _kl_m41_3_three_seed_exec_2026_10_16.md | 123255 | 垃圾候选表 #9 .tmp/klm41_3_ts_llm_calls_2026_10_16.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `59c2113b7c71` | B | B |  | 2059 | 移动映射表 #200：results/_v3x_p_k_verify_2026_09_16/v3x_p_k_verify_results_2026_09_16.json → 〔本地路径已脱敏〕 |
| `5a880678c386` | B | B |  | 1024 | 移动映射表 #217：results/boss_pc_2_a2_fitting_2026_09_15.json → 〔归档件引用·未上传:_movedout_2026_10_〕 |
| `5a8cbcf85aa7` | B | B | （**720 行**逐 call 留痕） ／ | 104288 | 垃圾候选表 #24 .tmp/three_seed_llm_calls_2026_10_16.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `5b95d06e66b0` | B | B | ion_2026_09_23.md | 6079 | 移动映射表 #124：results/deposon_v15_diffusion_summary.json → 〔归档件引用·未上传:_movedout_2026_10_22〕 |
| `5bebb5e1d329` | B | B | review_coach_v2X_outline.md | 11295 | 移动映射表 #89：reviews/review_coach_v2X_outline.md → 〔归档件引用·未上传:reviews〕 |
| `5c76137d6430` | B | B |  | 7530 | 移动映射表 #106：results/boss_pa_2_potential_game_result_2026_09_15.json → 〔归档件引用·未上传:_movedo〕 |
| `5cd6269d7baf` | B | B |  | 2741 | 移动映射表 #186：results/deposon_benchmark_v1_4_gsm8k.json → 〔归档件引用·未上传:_movedout_2026_10_22〕 |
| `5d79e67a4e9d` | B | B | _v4_pi_cot_v2_verdict_v2.md | 33723 | 合册成员：_book_08_pi_cot_v2_verdict_2026_10_22.md《_v4_pi_cot_v2_verdict_v2.md》 |
| `5dbfdb48ea99` | B | B | _v141_adoption_effect_2026_10_19.md | 149571 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v141_adoption_effect_2026_10_19.md》 |
| `601c3b82a978` | B | B | _v168_adoption_effect_2026_10_20.md | 148244 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v168_adoption_effect_2026_10_20.md》 |
| `612452d92285` | B | B |  | 15592 | 垃圾候选表 #5 .tmp/eta_main_run_llm_calls_2026_10_20.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `62c1a41e1db8` | B | B | ）、**⛔ 非单一可解析路径** ⇒ 5 子项须以 SHA-12 census 反查定位（④ | 80624 | 移动映射表 #36：results/deposon_v18_api_supplements.json → 〔归档件引用·未上传:re〕 |
| `6339ea4e500c` | B | B | v3_v4_ghostref_reconciliation_2026_09_23.md | 2706 | 移动映射表 #187：results/deposon_v20_gt8b.json → 〔归档件引用·未上传:results___de〕 |
| `640bf1db28f8` | B | B | _v148_adoption_effect_2026_10_20.md | 121547 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v148_adoption_effect_2026_10_20.md》 |
| `64f0a3772c12` | B | B | REF_VERIFICATION_v2.md | 5860 | 移动映射表 #126：docs/REF_VERIFICATION_v2.md → 〔归档件引用·未上传:docs___REF_VER〕 |
| `6512c6843d11` | B | E | _v148_adoption_effect_2026_10_20.md | 110211 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v148_adoption_effect_2026_10_20.md》 |
| `664e7cc05aec` | B | B | ** ／ **原件 0 触动门**：横切件落盘后， | 9076 | 移动映射表 #99：results/_p_l_p_c_finite_size_scaling_2026_09_16/p_l_p_c_finite_size_scaling_results_2026_09_16.json  |
| `66be80ab4b81` | B | B | _08.md | 11446 | 移动映射表 #11：results/_s4_substrate_grid_availability_2026_10_08.json → 〔归档件引用·未上传:_movedou〕 |
| `67162ab18f9a` | B | B | review_coach_v2X_draft_r2.md | 15721 | 移动映射表 #77：reviews/review_coach_v2X_draft_r2.md → 〔归档件引用·未上传:review〕 |
| `67867e752f47` | B | B |  | 6488 | 移动映射表 #118：results/deposon_risk3_seff_decision_2026_09_11.json → 〔归档件引用·未上传:_movedout_2〕 |
| `67d1d8342060` | B | B |  | 6886 | 移动映射表 #112：reviews/data/t2c_advlink.csv → 〔归档件引用·未上传:reviews___dat〕 |
| `680a7ce4cf08` | B | E | _v153_adoption_effect_2026_10_20.md | 148103 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v153_adoption_effect_2026_10_20.md》 |
| `68a5b08ef007` | B | B | SPEC_GT2B.md | 3318 | 移动映射表 #178：docs/SPEC_GT2B.md → 〔归档件引用·未上传:docs___SPEC_GT2B.md（去处＝归〕 |
| `69508d1965e9` | B | E | _v166_adoption_effect_2026_10_20.md | 107084 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v166_adoption_effect_2026_10_20.md》 |
| `6a2656878745` | B | B |  | 12798 | 移动映射表 #83：corpus/v20/strip_captions_22.json → 〔归档件引用·未上传:corpus___〕 |
| `6a703b06f0fe` | B | B |  | 1085 | 移动映射表 #215：LICENSE → 〔归档件引用·未上传:LICENSE（去处＝归档区〕；新路径今日存在＝False） |
| `6ae87e5d08eb` | B | B | _gd03_divergence_deliberation_2026_10_21.md | 44153 | 合册成员：_book_06_gd03_divergence_deliberation_2026_10_22.md《_gd03_divergence_deliberation_2026_10_21.md》 |
| `6b09de9911c0` | B | B | SPEC_GT8C.md | 6326 | 移动映射表 #122：docs/SPEC_GT8C.md → 〔归档件引用·未上传:docs___SPEC_GT8C.md（去处＝归〕 |
| `6c9d18dce714` | B | B | _v138_adoption_effect_2026_10_19.md | 99967 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v138_adoption_effect_2026_10_19.md》 |
| `6de8f0e651c4` | B | B |  | 5520 | 移动映射表 #128：reviews/data/t2b_linkpred.csv → 〔归档件引用·未上传:reviews___da〕 |
| `6e8b6e4730a8` | B | B |  | 6680 | 移动映射表 #116：reviews/data/t3_mechdesign.csv → 〔归档件引用·未上传:reviews___d〕 |
| `6eab35fe7636` | B | B | _v165_adoption_effect_2026_10_20.md | 125713 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v165_adoption_effect_2026_10_20.md》 |
| `6edb2aec1660` | B | B | ／18,905 B／mtime 10-15 11:08:00**（本棒 I1 命中 1·即 sub 区命中）③–⑦ | 16987 | 移动映射表 #73：results/deposon_v20_baselines.json → 〔归档件引用·未上传:results_〕 |
| `6f1e9689201b` | B | B | _t5_anchor_drift_authorized_register_2026_10_15.md | 4043 | 垃圾候选表 #26 .tmp/whitelist_backup_2026_10_17/t5_harness_diff_2026_10_15.diff（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `6f3c550cec13` | B | B | P_E_DOUBAN_EMBEDDING_V0_SPEC.md | 16876 | 移动映射表 #75：docs/V3X/P_E_DOUBAN_EMBEDDING_V0_SPEC.md → 〔归档件引用·未上传:do〕 |
| `6fe6a91f8adf` | B | B | _pre_execution_report_kimi_2026_10_18.md | 6969 | 合册成员：_book_13_pre_execution_report_kimi_2026_10_22.md《_pre_execution_report_kimi_2026_10_18.md》 |
| `701ad291a714` | B | B | onciliation_2026_09_23.md | 106317 | 移动映射表 #32：results/deposon_v17_fixed_sampler.json → 〔归档件引用·未上传:resu〕 |
| `704e2fd0d021` | B | B |  | 4296 | 移动映射表 #149：corpus/v20/S6_n60.json → 〔归档件引用·未上传:corpus___v20___S6_n〕 |
| `70ea38d5b9c0` | B | B | literature_scan_v19.md | 28449 | 移动映射表 #50：reviews/literature_scan_v19.md → 〔归档件引用·未上传:reviews___li〕 |
| `72a2a0c90985` | B | B | _d9_e2e_run_register_v2_2026_10_13.md | 26904 | 合册成员：_book_11_d9_e2e_run_register_2026_10_22.md《_d9_e2e_run_register_v2_2026_10_13.md》 |
| `734af9135441` | B | B | _budget_210_actual_evidence_register_2026_10_16.md | 24320 | 垃圾候选表 #17 .tmp/mq04_nt_llm_calls_2026_10_15.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `7474fc258375` | B | B | independent_review_20260823.md | 1724 | 移动映射表 #205：reviews/independent_review_20260823.md → 〔归档件引用·未上传:rev〕 |
| `76479b7a5ed6` | B | B | ostref_reconciliation_2026_09_23.md | 8404 | 移动映射表 #103：results/deposon_v20_crossval.json → 〔归档件引用·未上传:results_〕 |
| `77b0c1466dc0` | B | B |  | 3699 | 移动映射表 #164：corpus/v20/L_geography_world.json → 〔归档件引用·未上传:corpus__〕 |
| `799fbfc334a7` | B | B | _pre_execution_report_kimi_2026_10_12.md | 7612 | 合册成员：_book_13_pre_execution_report_kimi_2026_10_22.md《_pre_execution_report_kimi_2026_10_12.md》 |
| `79c7321056b8` | B | B | P_C_D1_D3_REPORT_2026_09_15.md | 13419 | 移动映射表 #82：docs/V3X/P_C_D1_D3_REPORT_2026_09_15.md → 〔归档件引用·未上传:doc〕 |
| `7bed1edfdb0e` | B | B | _v169_adoption_effect_2026_10_20.md | 156752 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v169_adoption_effect_2026_10_20.md》 |
| `7d0dbb58d53a` | B | B | _m41_double_readout_contrast_exec_2026_10_15.md | 3467 | 垃圾候选表 #14 .tmp/m41_r15_llm_calls.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `7d7086961937` | B | B | _v171_adoption_effect_2026_10_20.md | 165524 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v171_adoption_effect_2026_10_20.md》 |
| `7e5dc4b045d8` | B | B | Findings_v2.0.md | 4364 | 移动映射表 #146：docs/Findings_v2.0.md → 〔归档件引用·未上传:docs___Findings_v2.0〕 |
| `7ec9674b45da` | B | B | _v145_adoption_effect_2026_10_20.md | 174834 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v145_adoption_effect_2026_10_20.md》 |
| `7f4cf2cd5f42` | B | B |  | 613571 | 垃圾候选表 #8 .tmp/kdm413_rm_llm_calls_2026_10_17.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `7fb001add973` | B | B | related_work_v2X.md | 10114 | 移动映射表 #91：paper/v2/related_work_v2X.md → 〔归档件引用·未上传:paper___v2___r〕 |
| `81ecbbd30f95` | B | B | _v136_adoption_effect_2026_10_19.md | 68094 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v136_adoption_effect_2026_10_19.md》 |
| `82016e695f48` | B | B |  | 5450 | 移动映射表 #129：reviews/data/t1b_classics.csv → 〔归档件引用·未上传:reviews___da〕 |
| `821465001819` | B | B | _v4_pi_cot_v2_prereg.md | 5876 | 移动映射表 #17：results/_v4_pi_cot_v2_ruleset.json → 〔归档件引用·未上传:results_〕 |
| `82eb64151f2b` | B | B | ation_2026_09_23.md | 3112 | 移动映射表 #182：results/deposon_benchmark_v1_3_traps.json → 〔归档件引用·未上传:_movedout_2026_10_22〕 |
| `83c35597af81` | B | B |  | 4895 | 移动映射表 #18：results/deposon_volcengine_glm_latest_5cells_2026_09_10.json → 〔归档件引用·未上传:_mo〕 |
| `8423ffe266af` | B | B | P_F_SPEC_V0.md | 7335 | 移动映射表 #110：corpus/v20/index.json → 〔归档件引用·未上传:corpus___v20___index〕 |
| `84323775a212` | B | B | CLOSURE_v19_and_v2X_gametheory.md | 9065 | 移动映射表 #100：docs/CLOSURE_v19_and_v2X_gametheory.md → 〔归档件引用·未上传:doc〕 |
| `8487e4a34d29` | B | A＋B＋C | _cleanup_noise_register_2026_10_21.md | 7495 | 合册成员：_book_05_results_index_2026_10_22.md《_results_index_v2_2026_10_21.md》 |
| `848e1ff5e9ca` | B | B＋C | .tmp/dw74_勘误追加.py | 2829 | 垃圾候选表 #4 .tmp/dw74_勘误追加.py（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `854282220b93` | B | B | _upload_side_desensitized_remote_sha_letter_kimi_2026_10_18.md | 11237 | 合册成员：_book_07_upload_side_desensitized_remote_sha_letter_kimi_2026_10_22.md《_upload_side_desensitized_remote_s |
| `864bf2a98513` | B | B | _v152_adoption_effect_2026_10_20.md | 171316 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v152_adoption_effect_2026_10_20.md》 |
| `869c0071fbc2` | B | B | Findings_GT8.md | 3890 | 移动映射表 #159：docs/Findings_GT8.md → 〔归档件引用·未上传:docs___Findings_GT8.m〕 |
| `86f05646031b` | B | B | _supplement_500_combo_exec_2026_10_16.md | 59626 | 垃圾候选表 #3 .tmp/combo_llm_calls_2026_10_16.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `88acbcfd828a` | B | E | _v153_adoption_effect_2026_10_20.md | 173497 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v153_adoption_effect_2026_10_20.md》 |
| `8933d61b180a` | B | B | hashlib.sha256(全文字节).hexdigest()[:12] | 3553 | 移动映射表 #169：results/boss_pc_2_real_transverse_ising_2026_09_15.json → 〔归档件引用·未上传:_movedo〕 |
| `89430a7002d3` | B | B | _v146_adoption_effect_2026_10_20.md | 151322 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v146_adoption_effect_2026_10_20.md》 |
| `896589b673ec` | B | B | _v3_v4_ghostref_reconciliation_2026_09_23.md | 17925 | 移动映射表 #68：results/deposon_v20_gt7.json → 〔归档件引用·未上传:results___depo〕 |
| `89744f279f62` | B | C | _questionnaire_cards_intake_register_supplement_2_2026_10_10.md | 262542 | 合册成员：_book_02_questionnaire_cards_intake_register_2026_10_22.md《_questionnaire_cards_intake_register_supplemen |
| `8b1a9e5113bb` | B | B |  | 4167 | 移动映射表 #152：reviews/data/t1d_pagerank.csv → 〔归档件引用·未上传:reviews___da〕 |
| `8b7574b25336` | B | B | econciliation_2026_09_23.md | 3411 | 移动映射表 #171：results/deposon_gsm8k_stratified.json → 〔归档件引用·未上传:resu〕 |
| `8ba9fada9ead` | B | B |  | 6567 | 移动映射表 #117：reviews/data/t4_poa.csv → 〔归档件引用·未上传:reviews___data___t〕 |
| `8d02fbadd277` | B | B |  | 2676 | 移动映射表 #188：corpus/v20/S6_n35.json → 〔归档件引用·未上传:corpus___v20___S6_n〕 |
| `8df31c95b1fc` | B | B |  | 2557 | 移动映射表 #190：corpus/v20/all.json → 〔归档件引用·未上传:corpus___v20___all.jso〕 |
| `8e488d14bff6` | B | B | _t5_generator_build_exec_2026_10_15.md | 7258 | 垃圾候选表 #23 .tmp/t5_nt_llm_calls_2026_10_15.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `910c4333eead` | B | B | ／ 5 个 frozen run JSON(v20_gt + v19 + v21 + v18 + v17) ／ SHA-256 各 → 前 12 位 ／ | 409104 | 移动映射表 #25：results/deposon_v19_benchmark_fixes.json → 〔归档件引用·未上传:re〕 |
| `9158f54ec248` | B | B | Findings_v2.0_photonics.md | 4377 | 移动映射表 #145：docs/Findings_v2.0_photonics.md → 〔归档件引用·未上传:docs___Fin〕 |
| `9194ee703218` | B | B | tref_reconciliation_2026_09_23.md | 22623 | 移动映射表 #59：results/deposon_v20_quiz_eval.json → 〔归档件引用·未上传:results_〕 |
| `91db46a87830` | B | B |  | 2232 | 垃圾候选表 #7 .tmp/kdk45_r3_m2t5_calls_2026_10_17.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `928bcfbdb7c3` | B | B |  | 1496 | 移动映射表 #211：results/deposon_v22_e95ci.json → 〔归档件引用·未上传:results___d〕 |
| `9347add72401` | B | B | ion_2026_09_23.md | 2245 | 移动映射表 #197：results/deposon_benchmark_v1_3_simple.json → 〔归档件引用·未上传:_movedout_2026_10_22〕 |
| `9466fdbf9c95` | B | B |  | 6351 | 移动映射表 #120：results/deposon_cpath_simulation_2026_09_10.json → 〔归档件引用·未上传:_movedout_2026〕 |
| `94b5398be76c` | B | B |  | 2364 | 移动映射表 #195：results/boss_pc_3_real_reservoir_2026_09_15.json → 〔归档件引用·未上传:_movedout_2026〕 |
| `94fd018b5cc8` | B | B | ostref_reconciliation_2026_09_23.md | 7101 | 移动映射表 #111：results/deposon_v20_cot_quiz.json → 〔归档件引用·未上传:results_〕 |
| `956183753a2e` | B | B | Findings_GT8B.md | 9809 | 移动映射表 #95：docs/Findings_GT8B.md → 〔归档件引用·未上传:docs___Findings_GT8B〕. |
| `95ba771fa760` | B | B | _questionnaire_cards_intake_register_supplement_6_2026_10_10.md | 106453 | 合册成员：_book_02_questionnaire_cards_intake_register_2026_10_22.md《_questionnaire_cards_intake_register_supplemen |
| `968776002868` | B | B | simple_baseline_failure_analysis.md | 6080 | 移动映射表 #123：docs/simple_baseline_failure_analysis.md → 〔归档件引用·未上传:d〕 |
| `977fe1b48f75` | B | B | P_A_D1_D3_REPORT_2026_09_15.md | 19751 | 移动映射表 #62：docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md → 〔归档件引用·未上传:doc〕 |
| `9917ca76e30c` | B | B | _v173_adoption_effect_2026_10_21.md | 154726 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v173_adoption_effect_2026_10_21.md》 |
| `9ad0ad5a2645` | B | B | _v123_adoption_effect_2026_10_18.md | 69959 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v123_adoption_effect_2026_10_18.md》 |
| `9b16fa802ef8` | B | B | v3_v4_ghostref_reconciliation_2026_09_23.md | 2864 | 移动映射表 #184：results/deposon_v20_gt8c.json → 〔归档件引用·未上传:results___de〕 |
| `9c853eec100d` | B | B | _v172_adoption_effect_2026_10_20.md | 158273 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v172_adoption_effect_2026_10_20.md》 |
| `9d9ae5001c57` | B | B | P_F_V0_1_UPGRADE_2026_09_11.md | 69204 | 移动映射表 #39：results/deposon_v21_gtformal.json → 〔归档件引用·未上传:results__〕 |
| `9f88a212a77c` | B | B |  | 204441 | 移动映射表 #28：results/deposon_d_fix2_metric_verify_9m60c_2026_09_15.json → 〔归档件引用·未上传:_move〕 |
| `9fcb6b243e0d` | B | B | n_2026_09_23.md | 656572 | 移动映射表 #20：results/deposon_benchmark_v1_3_details.json → 〔归档件引用·未上传:_movedout_2026_10_22〕 |
| `9fd0f3399ab3` | B | B | _09_23.md | 2204 | 移动映射表 #199：results/deposon_g2_boltzmann_pathintegral.json → 〔归档件引用·未上传:_movedout_2026_1〕 |
| `9fd8a187cac0` | B | B | _v151_adoption_effect_2026_10_20.md | 80524 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v151_adoption_effect_2026_10_20.md》 |
| `a1651f3d9303` | B | B | _m41_double_readout_contrast_exec_2026_10_14.md | 642 | 垃圾候选表 #13 .tmp/m41_llm_calls.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `a18b5d0d4485` | B | B | FIGURE_LANGUAGE_POLICY.md | 2495 | 移动映射表 #192：paper/FIGURE_LANGUAGE_POLICY.md → 〔归档件引用·未上传:paper___FI〕 |
| `a18bbc703b42` | B | B |  | 85508 | 移动映射表 #35：results/deposon_v2_phase1_60cells_2026_09_11.json → 〔归档件引用·未上传:_movedout_2026〕 |
| `a1ef105b0269` | B | B | tref_reconciliation_2026_09_23.md | 1768 | 移动映射表 #203：results/deposon_v20_fastcheck.json → 〔归档件引用·未上传:results〕 |
| `a2ae7997ee67` | B | B | 「✅ 支持」**非终判件**且该件**已漂移**（同件 §0.3） ／ | 123331 | 移动映射表 #30：results/deposon_v20_gt2b.json → 〔归档件引用·未上传:results___dep〕 |
| `a3ca05aec6fb` | B | B |  | 8112 | 移动映射表 #16：results/deposon_volcengine_glm_latest_5cells_2026_09_10.py → 〔归档件引用·未上传:_move〕 |
| `a4b12d1cfedc` | B | B | n_distinct = 1 ｜ 诚实降级版 | 2042 | 移动映射表 #201：results/_p_m_real_separation_2026_09_16/p_m_real_separation_results_2026_09_16.json → 〔本地路径已脱敏〕 |
| `a54a3af46ba2` | B | B | _t2_path_b_build_exec_2026_10_16.md | 5317 | 垃圾候选表 #20 .tmp/t2b_llm_calls_2026_10_16.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `a63ebea7b29a` | B | B |  | 235779 | 移动映射表 #26：results/deposon_benchmark_v1_4_strategyqa_details.json → 〔归档件引用·未上传:_movedout〕 |
| `a7f479793f01` | B | B | Findings_v2.0_hardening.md | 3563 | 移动映射表 #167：docs/Findings_v2.0_hardening.md → 〔归档件引用·未上传:docs___Fin〕 |
| `a867d51f6444` | B | A＋B＋C |  | 1353 | 垃圾候选表 #1 .tmp/_w_eta_main_dry_calls.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `a890c56f7705` | B | B |  | 1512 | 移动映射表 #210：corpus/v20/S1.json → 〔归档件引用·未上传:corpus___v20___S1.json（〕 |
| `a9ad1de618f5` | B | B |  | 1669 | 移动映射表 #207：results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json → 〔本地路径已脱敏〕 |
| `a9cbafe581bb` | B | E | _v173_adoption_effect_2026_10_21.md | 148804 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v173_adoption_effect_2026_10_21.md》 |
| `ab0c2eaff0d1` | B | B |  | 75964 | 移动映射表 #37：results/deposon_dpath_cross_modal_2026_09_10.json → 〔归档件引用·未上传:_movedout_2026〕 |
| `ab3045b2c6d9` | B | B |  | 27 | 移动映射表 #223：requirements.txt → 〔归档件引用·未上传:requirements.txt（去处＝归档区〕；新 |
| `ab75889ee738` | B | B |  | 11512 | 移动映射表 #85：results/deposon_pg_v01_9m60c_2026_09_15.json → 〔归档件引用·未上传:_movedout_2026_10_2〕 |
| `ac3a90575192` | B | B | _v163_adoption_effect_2026_10_20.md | 113932 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v163_adoption_effect_2026_10_20.md》 |
| `ad0e445714d9` | B | B | SPEC_v1.8.md | 9850 | 移动映射表 #94：docs/SPEC_v1.8.md → 〔归档件引用·未上传:docs___SPEC_v1.8.md（去处＝归档〕 |
| `aeefb8ef6972` | B | B | GT_FORMALIZATION_v1.md | 19100 | 移动映射表 #64：docs/GT_FORMALIZATION_v1.md → 〔归档件引用·未上传:docs___GT_FORMA〕 |
| `af22751858d1` | B | B | _d9_e2e_run_register_2026_10_13.md | 12581 | 合册成员：_book_11_d9_e2e_run_register_2026_10_22.md《_d9_e2e_run_register_2026_10_13.md》 |
| `af51da229652` | B | B | ）、**⛔ 非单一可解析路径** ⇒ 5 子项须以 SHA-12 census 反查定位（④ | 106164 | 移动映射表 #33：results/deposon_v17_fusion_fix.json → 〔归档件引用·未上传:results〕 |
| `afe975606d40` | B | B | UNVERIFIED(true_labels 占位, AUC 不可信) | 3761 | 移动映射表 #163：results/_p_l_real_data_collapse_2026_09_16/p_l_real_data_collapse_results_v2_2026_09_16.json → 〔本地路径已脱敏〕 |
| `b1eb668377ce` | B | B |  | 49338 | 移动映射表 #5：results/deposon_volcengine_worker_b_2026_09_10.json → 〔归档件引用·未上传:_movedout_202〕 |
| `b1f6c5aa4de6` | B | B |  | 2234 | 移动映射表 #198：corpus/v20/S2.json → 〔归档件引用·未上传:corpus___v20___S2.json（〕 |
| `b2046af03610` | B | B |  | 20408 | 移动映射表 #60：results/deposon_pc_d1_d3_2026_09_15.json → 〔归档件引用·未上传:re〕 |
| `b51fd24586b3` | B | B | _09_23.md | 1691 | 移动映射表 #206：results/deposon_benchmark_v1_4_strategyqa.json → 〔归档件引用·未上传:_movedout_2026_1〕 |
| `b5873afb9d29` | B | B | c5_b_group_root_candidate_2026_10_01.md | 18104 | 移动映射表 #67：results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json → 〔归档件引用·未上传:_movedo〕 |
| `b6c7c3d5e2e5` | B | B | _v180_v182_adoption_effect_2026_10_21.md | 244228 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v180_v182_adoption_effect_2026_10_21.md》 |
| `b723af2ed8aa` | B | B | _v176_v179_adoption_effect_2026_10_21.md | 289618 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v176_v179_adoption_effect_2026_10_21.md》 |
| `b9feb5df8d44` | B | B | _m41_double_readout_contrast_exec_2026_10_15.md | 23855 | 合册成员：_book_10_m41_double_readout_contrast_exec_2026_10_22.md《_m41_double_readout_contrast_exec_2026_10_15.md》 |
| `bac61d51fd20` | B | B | SPEC_v2.0.md | 5333 | 移动映射表 #133：docs/SPEC_v2.0.md → 〔归档件引用·未上传:docs___SPEC_v2.0.md（去处＝归〕 |
| `bf0a2b544a74` | B | B |  | 3691 | 移动映射表 #165：reviews/data/t3e_commit.csv → 〔归档件引用·未上传:reviews___data〕 |
| `bfc9d38c8c0f` | B | B |  | 1537 | 移动映射表 #209：corpus/v20/S2_n20.json → 〔归档件引用·未上传:corpus___v20___S2_n〕 |
| `c05e334b7bf6` | B | B | _v162_adoption_effect_2026_10_20.md | 119837 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v162_adoption_effect_2026_10_20.md》 |
| `c0f886e0d8b0` | B | B | _v183_v185_adoption_effect_2026_10_21.md | 262130 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v183_v185_adoption_effect_2026_10_21.md》 |
| `c165cd33a362` | B | B | PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md | 4587 | 移动映射表 #142：docs/V3X/PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md → 〔归档件引用·未上传:_movedout_2026_10〕 |
| `c16d1768d1ca` | B | B | tref_reconciliation_2026_09_23.md | 519387 | 移动映射表 #23：results/deposon_v15_diffusion.json → 〔归档件引用·未上传:results_〕 |
| `c17b31ae4f3b` | B | B | tref_reconciliation_2026_09_23.md | 39974 | 移动映射表 #44：results/deposon_v16_llm_prior.json → 〔归档件引用·未上传:results_〕 |
| `c3167a531e0e` | B | B | _d9_relpath_rewrite_map_2026_10_12.md | 21352 | 合册成员：_book_09_d9_relpath_rewrite_map_2026_10_22.md《_d9_relpath_rewrite_map_2026_10_12.md》 |
| `c41f1717310e` | B | B | design_probe_v19.md | 13967 | 移动映射表 #79：reviews/design_probe_v19.md → 〔归档件引用·未上传:reviews___desig〕 |
| `c43a84c70935` | B | B | ／8,118 B（本棒直算，与 | 16043 | 移动映射表 #9：results/_pa_harness_anchor_value_update_v2.json → 〔归档件引用·未上传:_movedout_2026_10〕 |
| `c4b774c8e34c` | B | B | 字段非 caption 文本）。 ／ JSON | 4559 | 移动映射表 #144：results/deposon_volcengine_22caption_embedding_2026_09_10.json → 〔归档区〕 |
| `c50ff98a95cc` | B | B |  | 5566 | 移动映射表 #127：reviews/data/t1c_loglinear.csv → 〔归档件引用·未上传:reviews___d〕 |
| `c659695aa23c` | B | B | （540 cells 计数真源） ／ boss_pa_1 | 17732 | 移动映射表 #69：results/deposon_v3_physical_opt_60cells_2026_09_11.json → 〔归档件引用·未上传:_movedou〕 |
| `c7c59e0d2f6c` | B | B | （12） ／ 异**如实挂账**（记值／实测值分列）：'boss_pa_1_*.json' 记 ' ⏎ | 8753 | 移动映射表 #102：results/boss_pa_1_rbr_rm_result_2026_09_15.json → 〔归档件引用·未上传:_movedout_2026_〕 |
| `ca71aa6858e1` | B | B | _reconciliation_2026_09_23.md | 631644 | 移动映射表 #21：results/deposon_v20_corpus_eval.json → 〔归档件引用·未上传:result〕 |
| `cf4a882160e1` | B | B |  | 4066 | 移动映射表 #155：results/deposon_risk2_canonical5_decision_2026_09_11.json → 〔归档件引用·未上传:_move〕 |
| `cf7682348617` | B | B |  | 5212 | 移动映射表 #135：results/deposon_v2_phase4_f4_2026_09_11.json → 〔归档件引用·未上传:_movedout_2026_10_〕 |
| `d02f0d4792a7` | B | B | _v139_adoption_effect_2026_10_19.md | 105619 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v139_adoption_effect_2026_10_19.md》 |
| `d21912a05d79` | B | B |  | 1017 | 移动映射表 #219：results/boss_pc_1_a1_resampling_2026_09_15.json → 〔归档件引用·未上传:_movedout_2026_〕 |
| `d30121ed7ebf` | B | B | _m08_measured_enumeration_exec_2026_10_16.md | 8230 | 垃圾候选表 #12 .tmp/m08_r1_llm_calls_partial_pass1_2026_10_16.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `d34cc2373f0f` | B | B |  | 2484 | 垃圾候选表 #19 .tmp/root45_s11s12_llm_calls_2026_10_17.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `d4da2693d309` | B | E | _v180_v182_adoption_effect_2026_10_21.md | 230027 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v180_v182_adoption_effect_2026_10_21.md》 |
| `d4ed18152dc0` | B | B | Findings_v2.0_bigquiz.md | 3291 | 移动映射表 #179：docs/Findings_v2.0_bigquiz.md → 〔归档件引用·未上传:docs___Findi〕 |
| `d6f233d73c45` | B | B |  | 9098 | 移动映射表 #98：results/boss_pa_3_replicator_dynamics_result_2026_09_15.json → 〔归档件引用·未上传:_mo〕 |
| `d6ff041a9df9` | B | B | _questionnaire_cards_intake_register_supplement_4_2026_10_10.md | 116506 | 合册成员：_book_02_questionnaire_cards_intake_register_2026_10_22.md《_questionnaire_cards_intake_register_supplemen |
| `d6ff7e9b4bd6` | B | B | _d9_relpath_rewrite_map_v2_2026_10_12.md | 28112 | 合册成员：_book_09_d9_relpath_rewrite_map_2026_10_22.md《_d9_relpath_rewrite_map_v2_2026_10_12.md》 |
| `d74d6b39d1b0` | B | B |  | 1265 | 移动映射表 #214：results/boss_pc_3_a3_clipping_2026_09_15.json → 〔归档件引用·未上传:_movedout_2026_10〕 |
| `d8780859d310` | B | B |  | 3397 | 移动映射表 #173：corpus/v20/L_physics_concepts.json → 〔归档件引用·未上传:corpus_〕 |
| `d917180db36f` | B | B | _questionnaire_cards_intake_register_2026_10_09.md | 442288 | 合册成员：_book_02_questionnaire_cards_intake_register_2026_10_22.md《_questionnaire_cards_intake_register_2026_10_0 |
| `d9cd98f30fcc` | B | B | _v150_adoption_effect_2026_10_20.md | 132608 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v150_adoption_effect_2026_10_20.md》 |
| `da9b793fc73f` | B | E | _v154_adoption_effect_2026_10_20.md | 134043 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v154_adoption_effect_2026_10_20.md》 |
| `dc43e3cb7610` | B | B | _questionnaire_cards_intake_register_supplement_2_2026_10_10.md | 262542/44796 | 合册成员：_book_02_questionnaire_cards_intake_register_2026_10_22.md《_questionnaire_cards_intake_register_supplemen |
| `dd3e9806a369` | B | B | _achievements_inventory_full_2026_10_09.md | 372318 | 合册成员：_book_03_achievements_inventory_full_2026_10_22.md《_achievements_inventory_full_2026_10_09.md》 |
| `de450c0beffa` | B | B | PAPER_BRIEF.md | 11296 | 移动映射表 #88：docs/PAPER_BRIEF.md → 〔归档件引用·未上传:docs___PAPER_BRIEF.md（去〕 |
| `dfbcc5d6fc34` | B | B |  | 13775 | 移动映射表 #80：corpus/v20_caption_surface/_p_d_v03_22caption_verification_20260917_163757.json → 〔本地路径已脱敏〕 |
| `e110a020954f` | B | B |  | 4833 | 移动映射表 #140：reviews/data/t1_potential.csv → 〔归档件引用·未上传:reviews___da〕 |
| `e17942840ef9` | B | E | _v155_adoption_effect_2026_10_20.md | 78018 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v155_adoption_effect_2026_10_20.md》 |
| `e20a1bbeaee7` | B | B |  | 2480 | 移动映射表 #193：corpus/v20/S2_n35.json → 〔归档件引用·未上传:corpus___v20___S2_n〕 |
| `e221792715f8` | B | B |  | 15604 | 移动映射表 #78：results/deposon_pa_d1_d3_2026_09_15.json → 〔归档件引用·未上传:re〕 |
| `e262e9d684fe` | B | B | post_edit_verification_v19.md | 19327 | 移动映射表 #63：reviews/post_edit_verification_v19.md → 〔归档件引用·未上传:revie〕 |
| `e361a13ed658` | B | E | _v164_adoption_effect_2026_10_20.md | 107152 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v164_adoption_effect_2026_10_20.md》 |
| `e3dae2a4bbc2` | B | B |  | 35011 | 移动映射表 #6：results/_v4_track2_multimodel_rerun_2026_09_23.json → 〔归档件引用·未上传:_movedout_202〕 |
| `e6045f0920ec` | B | B |  | 4932 | 移动映射表 #138：corpus/v20/S4.json → 〔归档件引用·未上传:corpus___v20___S4.json（〕 |
| `e6cc74f9917d` | B | B | Findings_GT2B.md | 3322 | 移动映射表 #175：docs/Findings_GT2B.md → 〔归档件引用·未上传:docs___Findings_GT2B〕 |
| `e87937d55471` | B | B | _k_v3df_0_1_four_readings_2026_10_09.md | 65507/46522 | 移动映射表 #2：results/_k_v3df_0_1_four_readings_2026_10_09.json → 〔归档件引用·未上传:_movedout_2026_〕 |
| `e922d168ab60` | B | B | _ge01_full_1494_exec_r1_2026_10_16.md | 235298 | 垃圾候选表 #6 .tmp/ge01_full_1494_llm_calls_2026_10_16.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `e934819ee9ed` | B | B |  | 1043 | 移动映射表 #216：results/_p_i_real_labels_2026_09_16/p_i_real_labels_results_2026_09_16.json → 〔本地路径已脱敏〕 |
| `ea38ee252701` | B | B |  | 18290 | 移动映射表 #66：results/deposon_gpt6_teamorouter_30cells_2026_09_10.json → 〔归档件引用·未上传:_movedo〕 |
| `eb8c189c01f4` | B | B | _v142_adoption_effect_2026_10_19.md | 131781 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v142_adoption_effect_2026_10_19.md》 |
| `eb9ad4193cf2` | B | B | _v4_pi_cot_v2_verdict.md | 22340 | 合册成员：_book_08_pi_cot_v2_verdict_2026_10_22.md《_v4_pi_cot_v2_verdict.md》 |
| `edb57308170d` | B | B | _questionnaire_cards_intake_register_supplement_5_2026_10_10.md | 77189 | 合册成员：_book_02_questionnaire_cards_intake_register_2026_10_22.md《_questionnaire_cards_intake_register_supplemen |
| `edf6f4465ead` | B | B | SPEC_GT8.md | 4181 | 移动映射表 #151：docs/SPEC_GT8.md → 〔归档件引用·未上传:docs___SPEC_GT8.md（去处＝归档区〕 |
| `efe05ad775de` | B | B |  | 24150 | 移动映射表 #55：corpus/v20/index_v2_2026_09_16.json → 〔归档件引用·未上传:corpus_〕 |
| `f035043bfddd` | B | B |  | 2521 | 移动映射表 #191：corpus/v20/S1_n35.json → 〔归档件引用·未上传:corpus___v20___S1_n〕 |
| `f06313373fc6` | B | B | ／ ✅ **沿录**（本棒复算 v1／v2／v3 指纹**逐位一致**： | 21629 | 移动映射表 #7：results/_ge01_prereg_5anchor_v2.json → 〔归档件引用·未上传:results〕 |
| `f0d2c9d2a39b` | B | B |  | 1271 | 移动映射表 #213：reviews/data/t2f_waniek.csv → 〔归档件引用·未上传:reviews___data〕 |
| `f119f2f30287` | B | B | P_D_FINGERPRINT_V0_3_SPEC.md | 34393 | 移动映射表 #47：docs/V3X/P_D_FINGERPRINT_V0_3_SPEC.md → 〔归档件引用·未上传:docs_〕 |
| `f36667e5b5b8` | B | B |  | 2782 | 移动映射表 #185：results/deposon_g2_boltzmann_pathintegral_rewrite.json → 〔归档件引用·未上传:_movedou〕 |
| `f3838e36b897` | B | E | _v145_adoption_effect_2026_10_20.md | 149295 | 合册成员：_book_01_adoption_effect_2026_10_22.md《_v145_adoption_effect_2026_10_20.md》 |
| `f39412103366` | B | B |  | 17053 | 移动映射表 #72：results/_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json → 〔本地路径已脱敏〕 |
| `f44636f5f72f` | B | B |  | 3827 | 移动映射表 #161：results/deposon_gpt6_teamorouter_2026_09_10.json → 〔归档件引用·未上传:_movedout_2026〕 |
| `f48c9f09a3b4` | B | B |  | 6731 | 移动映射表 #115：reviews/data/t3b_verifiable.csv → 〔归档件引用·未上传:reviews___〕 |
| `f6f172820c97` | B | B |  | 51716 | 移动映射表 #4：results/deposon_volcengine_worker_c_2026_09_10.json → 〔归档件引用·未上传:_movedout_202〕 |
| `fab607f0e180` | B | B | Findings_GT_FORMAL.md | 6345 | 移动映射表 #121：docs/Findings_GT_FORMAL.md → 〔归档件引用·未上传:docs___Findings〕 |
| `fae79888344b` | B | B |  | 20280 | 移动映射表 #61：results/deposon_volcengine_worker_d_2026_09_10.json → 〔归档件引用·未上传:_movedout_20〕 |
| `fbb7677b9cd5` | B | B |  | 23472 | 移动映射表 #56：results/deposon_volcengine_minimax_m3_30cells_2026_09_10.json → 〔归档件引用·未上传:_m〕 |
| `fbbfd3ef3890` | B | B | ostref_reconciliation_2026_09_23.md | 42458 | 移动映射表 #43：results/deposon_v19_fullrank.json → 〔归档件引用·未上传:results__〕 |
| `fbcb60cf5102` | B | B | 既有字段，**非新设**）｜④ **修 verdict 面**：v42 重设计属**论文修正条款面**（ | 5266 | 移动映射表 #134：results/_p_m_attack_surface_cost_2026_09_16/p_m_attack_surface_cost_results_2026_09_16.json → 〔本地路径已脱敏〕 |
| `fbdedcb0ef48` | B | B | _material_expansion_build_exec_2026_10_16.md | 21339 | 垃圾候选表 #16 .tmp/me_llm_calls_2026_10_16.jsonl（今日不在盘；PI 16:52 裁·17:0x 可恢复删除之 26 件） |
| `fca14c5735dd` | B | B | ）均为 | 72647 | 移动映射表 #38：results/deposon_v20_gt5.json → 〔归档件引用·未上传:results___depo〕 |
| `fcb0a673ee5c` | B | B | _upload_side_desensitized_remote_sha_letter_kimi_2026_10_12.md | 74043 | 合册成员：_book_07_upload_side_desensitized_remote_sha_letter_kimi_2026_10_22.md《_upload_side_desensitized_remote_s |
| `fcb5105df0b6` | B | B |  | 33829 | 移动映射表 #48：results/deposon_pf_d1_full_9m5c_2026_09_15.json → 〔归档件引用·未上传:_movedout_2026_1〕 |
| `ff0ef9131fdd` | B | B |  | 3920 | 移动映射表 #157：corpus/v20/L_algorithm_process.json → 〔归档件引用·未上传:corpus〕 |
| `ff9ff3177c06` | B | B | RELEASE_v1.4.0.md | 3847 | 移动映射表 #160：RELEASE_v1.4.0.md → 〔归档件引用·未上传:RELEASE_v1.4.0.md（去处＝归档区〕 |
| `30d89421bb45` | C | C | results/_archive_2026_09_20/_letter_to_kimi_push_v3_委托_2026_09_17.md | 13600 | 10-22 曾被「漂移改指」扣除，今日不扣除 ⇒ 口径差（同一实体之判两读不同） |
| `570aa07611f4` | C | C | results/_archive_2026_09_20/_coze_paper_v1_双审报告_2026_09_17.md | 85645 | 10-22 曾被「漂移改指」扣除，今日不扣除 ⇒ 口径差（同一实体之判两读不同） |
| `5c6d558fa400` | C | C | arXiv提交四件套/Deposon_II_v9_arXiv预印本.pdf | 652755/635733/17022 | 10-22 曾被「漂移改指」扣除，今日不扣除 ⇒ 口径差（同一实体之判两读不同） |
| `85cfbc2a5a06` | C | C |  | 20212/6 | 10-22 判为口径型（git-blob·实体在盘），今日该口径不命中 ⇒ 口径面变化 |
| `9bff09e32332` | C | C | results/_archive_2026_09_20/_letter_to_coze_paper_v1_委托_2026_09_17.md | 12838 | 10-22 曾被「漂移改指」扣除，今日不扣除 ⇒ 口径差（同一实体之判两读不同） |
| `a047342a5444` | C | C | _pi_dual_ruling_register_ge02_acceptance_ge01_readiness_2026_10_12.md | 19296 | 10-22 判为口径型（git-blob·实体在盘），今日该口径不命中 ⇒ 口径面变化 |
| `ac3e45e5b0a6` | C | C |  | 1836 | 10-22 判为口径型（git-blob·实体在盘），今日该口径不命中 ⇒ 口径面变化 |
| `b05ff8152eee` | C | C | P_E_DOUBAN_EMBEDDING_V0_SPEC.md | 16904 | 10-22 曾被「漂移改指」扣除，今日不扣除 ⇒ 口径差（同一实体之判两读不同） |
| `be0c6e9e27a8` | C | C | _ge03_ge04_claim_proposal_2026_10_22.md | 65943 | 10-22 曾引而未成字节对，今日成对 ⇒ 口径面变化 |
| `000000000095` | 仪器噪声 | A＋C |  | 3424028 | 10-22 源面未引此指纹 ⇒ 引用系新引入（引者含今日新落件）；此串非真哈希（全零前缀＋序号）⇒ 仪器假阳性，须修仪器（加排除规则），⛔ 0 以此充因 |
| `000000000096` | 仪器噪声 | A＋C |  | 3241672 | 10-22 源面未引此指纹 ⇒ 引用系新引入（引者含今日新落件）；此串非真哈希（全零前缀＋序号）⇒ 仪器假阳性，须修仪器（加排除规则），⛔ 0 以此充因 |
| `30e6a3041078` | 未核得 | — | **／41,236 B（**未变**）｜ | 39384 | ｜缺：缺：实体离面之执行回执（逐件路径＋时刻＋通道） |
| `e969ad69a634` | 未核得 | — |  | 27641 | ｜缺：缺：实体离面之执行回执（逐件路径＋时刻＋通道） |

**小计校验**：A **16** ＋ B **342** ＋ C **9** ＋ 仪器噪声 **2** ＋ 未核得 **2** ＝ **371** ✔（互斥不重叠）

---

## §14 字节级自报（落盘后独立回读）

| 项 | 值 |
|:--|:--|
| 路径 | `〔幽灵引用·未上传:_gate2_delta_attribution_2026_10_23.md〕` |
| BOM | **0**（无 UTF-8 BOM） |
| CR | **0**（纯 LF） |
| VT | **0**（无 0x0B） |
| U+FFFD | **0**（无替换字符） |
| 末字节 | **0x0A** |
| bytes／SHA-12 | **出带自报**——本件不能自含其自身哈希（自含即自指悖论；承 10-22 复核件 §12 之同戒）：其值随本节落定后由本棒**独立回读**实测，并载于**回执**（同一时点、同一读源） |
| key 形态自扫 | 词边界扫描（3 类密钥前缀 ＋ 2 类凭据头之赋值形；**模式字面量不载于本件正文**，以免自触发）＝ **CLEAN**（0 命中）——见回执 |

---

*件止。`evidence-auditor` · 2026-10-23 —— 门槛②「＋360 差因逐条定」件（自扫以分离 `CARRY` · 口径先回原件核 · 371 件逐条定因（互斥不重叠）· 未核得 2 件写明缺项 · 两读并出 · ⛔ 0 以定因之果径改 1,710 或 1,350 之登记）｜⛔ 0 回改既有件 · 0 移 · 0 删 · 0 新建目录 · 0 触归档区内容 · 0 读 GLM 内容 · 0 联网 · 0 落五终判 · 0 闭 KD · 0 宣告段毕 · 0 宣告门槛② 成就 · 0 代裁。*
