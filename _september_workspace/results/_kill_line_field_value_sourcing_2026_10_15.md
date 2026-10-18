# `P_B_KILL_LINE` 之 `field` 正式值 · 双路取值（文献线 × 预实验线）

> **候选产出 · 候 PI 核准 · ⛔ 0 径行采认** —— 依 PI 2026-10-15 11:31 口头令「Q-7 `field` 正式值给不了，沿用文献与预实验双线」产出**双路候选与排序建议**。本件**非正式值**、**⛔ 非登记锚值**。
>
> **⛔ 0 回填** `results/_ge01_prereg_5anchor_v2.json`（其 `P_B_KILL_LINE.field` 现载「候 PI 给」，本棒**一字未动**）｜**⛔ 0 回改**任何既有件（含承载件 v1 `9e09214cf088`／18,905 B 与草案 v0 `0f65a42e7a34`）｜**⛔ 0 代 PI 裁**｜**⛔ 0 宣告**该项闭、**⛔ 0 宣告** `C3` 通过、**⛔ 0 宣告**①毕｜**⛔ 0 回改** GT 迁移登记件 §7 R-1。
>
> **上位授权面**：卡答登记件 v12 `97111fee4410` 之 Q1／Q2（Q1 逐字「全部按棒之倾向档打包核准（推荐）」）。**排序建议属「须 PI 择」类** ⇒ 按「代立边界纠正」（PI 2026-10-09 23:38）**⛔ 0 以代立代替直问** ⇒ 本件只出候选、依据与排序，**择一之权归 PI**。
>
> **跑禁**：已解（v6 `7e95b053e249`）—— 故本棒**未跑任何实验**，全文 0 次实验调用。

---

## §1 源件实测（**逐字回读 · ⛔ 0 凭转述**）

指纹为本棒直算 `hashlib.sha256(磁盘全文字节).hexdigest()[:12]`，非转述。

| # | 件（仓库相对路径） | 本棒实测 SHA-12 | bytes | 本棒取用面 |
|:-:|:--|:-:|--:|:--|
| 1 | `results/_ge01_prereg_5anchor_v2.json` | `f06313373fc6` | 21629 | L173–L182（`P_B_KILL_LINE` 之 `field`／`field_status`／`field_note`）、L44–45、L240、L293–294、L339 |
| 2 | `results/_gt_kill_line_carrier_effect_register_2026_10_15.md` | `e40f060fa3a3` | 25941 | §3 表 Q-7 行、§5 登记面 `field` 行、§7 R-1 |
| 3 | `results/_ge01_gt_kill_family_byte_stream_effect_register_2026_10_14.md` | `e631795149eb` | 29189 | §2-1 生效要点、§2-3 H-3／H-4 |
| 4 | `results/_ge01_5anchor_json_draft_2026_10_14.md` | `9898a19d9a1d` | 33387 | §2-1 锚表 `P_B_KILL_LINE` 行、§2-4 逐锚现状、§3-5 甲／乙案 |
| 5 | `verifier/kill_lines/GT_kill_line_carrier_v1.md` | `9e09214cf088` | 18905 | §1 规格表、§3 十成员表与分布、§6 G-4 |
| 6 | `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | `03c6c01f3697` | 6680 | §anchors/KT-A1／KT-B1／KT-C1 之 `field` 体例（**只读参照**） |
| 7 | `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | `423c84de20d5` | 15457 | §2 锚表 L27 之 **spec 面字面**（`object`＝「GT 判死裁定族（10 个）」） |

✅ **承载件锚值未漂移**：本棒直算 `verifier/kill_lines/GT_kill_line_carrier_v1.md` ＝ `9e09214cf088`／18905 B、CR＝0（纯 LF）⇒ 与迁移登记件 §5 登记值**逐位相符**；**本棒只读，未开写**。

---

## §2 文献线（**联网 · 0 直接命中 · 如实报**）

### §2-1 通道清单（**实测 · 逐条列明**）

| 通道 | 实测结果 |
|:--|:--|
| `mcode-tools connector tools --keyword search` | 命中 **2** 项，**皆为图片类**：`connector__matrix__search_images`／`connector__matrix__reverse_image_search` |
| `mcode-tools connector tools`（**不带过滤 · 全量**，依 skill 规程放宽一次） | 全量 **15** 项（`matrix` 图像／音视频 12 ＋ `email_workbench` 2 ＋ 计 15）⇒ **全catalog 0 通用网页检索／抓取工具** |
| 本地 `web_fetch` → DuckDuckGo HTML 端点 | ✅ **可用**（返回可解析结果页，含显式「No results found」段） |
| 本地 `web_fetch` → Bing | ✅ 可达，但结果面为 JS 模板、**正文可提取性差**（本棒未据其取任何候选） |
| 本地 `web_fetch` → `raw.githubusercontent.com` | ✅ 可达（用于复核唯一邻证，见 §2-3） |

⇒ **App／Connector 通道对本问题 0 提供力**（全 catalog 无网页检索／抓取工具）；改由本地 `web_fetch` 直连检索引擎执行。

### §2-2 检索式与命中（**5 式 · 逐式如实报**）

| # | 检索式（逐字） | 通道 | 命中 |
|:-:|:--|:--|:-:|
| Q1 | `"kill line" preregister anchor manifest field description sha256` | DDG HTML | **0**（显式「No results found」） |
| Q2 | `"kill criteria" pre-registration anchor manifest json "field" descriptor sha256 first 12` | Bing | **0 可提取**（页面可达但正文被模板淹没，不据此判有／无） |
| Q3 | `"kill criteria" pre-registration falsification threshold reproducibility manifest` | DDG HTML | **1**（唯一邻证，见 §2-3） |
| Q4 | `reproducibility manifest json "object" "path" "algorithm" "field" anchor schema checksum` | DDG HTML | **0**（显式「No results found」） |
| Q5 | `pre-registered anchor "kill line" hash "frozen text" experiment ledger` | DDG HTML | **0**（显式「No results found」） |

⇒ **文献线净命中 ＝ 1／5，且该唯一命中不含 `field` 体例内容**（§2-3）。

### §2-3 唯一邻证（**0 体例价值 · ⛔ 0 据以立候选**）

- 命中件：`https://github.com/raphaelbgr/falsification-log`
- 检索页摘要逐字：「A year of testing crypto trading hypotheses to destruction — six classes tested, six falsified, three killed for $0. **Pre-registered kill criteria**, 450k-observation verdicts, and an honest real-money post-mortem.」
- **复核尝试**：本棒以 `web_fetch` 取 `raw.githubusercontent.com/raphaelbgr/falsification-log/main/README.md` ⇒ **HTTP 404**，**正文 0 复核成功**。
- ⇒ **判读**：该件仅佐证「**预登记 kill criteria**」为**外部既有实践**（概念层）；**对「锚表 `field` 键该写成什么字符串」0 提供任何体例规定**。⛔ **0 据以立候选**，⛔ 0 引用其未复核之正文。

### §2-4 文献线结论

**文献线对本问题 0 直接权威。** 理由（非推测，三项实测）：

1. `field` 系**本仓自设的私有关键名**（锚表五键 schema 出自 H-3 之先例件 `03c6c01f3697`），**非任何公开标准之术语** ⇒ 公开文献不载其写法，Q1／Q4／Q5 显式 0 命中与此一致。
2. 即使退到最宽之邻域（可复现性清单元数据），Q4 仍 0 命中 ⇒ **无「近邻标准体例」可援引**。
3. 唯一邻证（§2-3）经**正文复核失败**，**0 体例内容**。

⇒ **文献线候选数 ＝ 0**。本棒**不硬凑**：宁 0 命中如实报，亦**⛔ 0 以伪文献充权威**。此 0 之本身即交付面之一。

---

## §3 预实验线（**承载件内容结构 ＋ 先例体例实测 · 本棒自跑之对照实验**）

> 依 PI 惯用法（PI 2026-10-14 明示「以往常采用预实验择优」）：**⛔ 0 等 PI 给值**，改由**对照实验择优**——即以「先例锚表 15 锚之 `field` 实测体例」＋「承载件实际内容结构」互为对照，取其吻合者。

### §3-1 对照实验 A：**先例锚表 `field` 体例全表实测**（先例件 `03c6c01f3697` · 15 锚逐条读出）

| 先例锚 | `field` 逐字 | 型 |
|:--|:--|:--|
| `P_A_ECR_BASELINE` | `ecr_median=1.333` | 构造型·数值声明 |
| **`P_A_KILL_LINE`** | **`kills=10 GT`** | **构造型·族计数** |
| `P_A_FROZEN_RUNS` | `runs=5 frozen` | 构造型·计数＋冻结态 |
| `P_A_LLM_CLIENT` | `Doubao + DeepSeek, runtime Path().read_text()` | 叙述型 |
| `P_A_HARNESS` | `Mechanism M1/M2/M3 + TaskFamily T1-T4` | 枚举型 |
| `KT_B1_V19_BENCHMARK` | `t_plus_r_plus_a_max_deviation=2.2e-16` | 构造型·数值声明 |
| **`KT_B1_KILL_LINE`** | **`4 档 (PASS_KT_B1 / GRAY_DOWN / GRAY_UP / FAIL_KT_B1)`** | **枚举型·档位清单** |
| `KT_B1_ATTACK_BANK` | `3 类攻击 × 200 次 (D2 实现)` | 枚举型·计数 |
| `KT_B1_AUDIT_FUNCTION` | `T+R+A=1 守恒审计 (D2 实现)` | 叙述型 |
| `KT_B1_HARNESS` | `3 类攻击 × 200 次 + 守恒审计 (D2 实现)` | 叙述＋枚举 |
| `KT_C1_V21_FROZEN` | `n_graphs=61, n_tasks=338, n_states=6760` | 构造型·多项计数 |
| **`KT_C1_KILL_LINE`** | **`kill_line = "R^2<0.3 OR b_CI 含 0"`** | **判死式全文（JSON 化 quoting）** |
| `KT_C1_LOGLOG_FIT` | `OLS + 95% bootstrap (D2 实现, 328 pairs 跑通, DEAD)` | 叙述型 |
| `KT_C1_ETA_SCAN` | `η 扫描 0.01-100 (9 档), η_crit_05=0.333 (D2 实现)` | 枚举型 |
| `KT_C1_HARNESS` | `主 + 双跑 + BOSS-C1/C2/C3 (D2 实现)` | 枚举型 |

**三项实测结论**：

- **(a) `*_KILL_LINE` 同族先例 3 枚，呈现 3 种互异写法**（`kills=10 GT`／`4 档 (...)`／`kill_line = "..."`）⇒ **`field` 无单一强制体例**，先例**不能唯一决定**取值。
- **(b) `field` 一律为**人类可读短串，⛔ 0 与被哈希对象耦合：例 `P_A_ECR_BASELINE` 之 `field`＝`ecr_median=1.333` 而其 `value`＝P-A spec **全文** SHA-12 ⇒ 与 H-4（`field` ＝ 表征说明、⛔ 非被哈希对象）**完全一致**。
- **(c) 先例 `field` 与 spec 面字面**存在系统性分歧**：spec 面（L49）载 `kills={"GT-1":true, ...}`，而先例 JSON 实际登记为 `kills=10 GT` ⇒ **spec 面 ≠ 登记体例**。

### §3-2 对照实验 B：**同批 5 锚内，其余可解锚 `field` 之采择**（v2 实测 · 本棒最强判据）

| 锚 | spec 面字面（`docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md`） | 先例 `03c6c01f3697` 之值 | **v2 实际采择** | 采何者 |
|:--|:--|:--|:--|:-:|
| `P_B_ECR_BASELINE` | `ecr_median=1.333` | `ecr_median=1.333` | `GT4_price_of_anarchy.verdict.median_poa` | **皆未采**（另立 JSON 指针式；`field_note` L45 逐字「字面 'ecr_median' 为禁用字面且本棒未使用」） |
| `P_B_FROZEN_RUNS` | `runs=["v20_gt", ...]` | `runs=5 frozen` | `runs=5 frozen` | **采先例值** |
| `P_B_LLM_CLIENT` | `version=2026-09-11` | `Doubao + DeepSeek, runtime Path().read_text()` | `Doubao + DeepSeek, runtime Path().read_text()` | **采先例值**（`field_note` L294 逐字「**逐字沿 KT-A1 先例**」） |
| `P_B_DISTORTION_CALC` | `version=2026-09-11` | *（无同键先例）* | `version=2026-09-11`（`field_status` 沿占位） | **采 spec 面字面**（⚠ U-2 未复核其对文件内容之准确性） |
| **`P_B_KILL_LINE`** | `kills={"GT-1":true, ...}` | `P_A_KILL_LINE` ＝ `kills=10 GT` | **`候 PI 给`**（本棒之对象） | **候 PI 裁** |

⇒ **实测判据**：同批 5 锚中，**凡「文件哈希型」锚（`value` ＝ 某件全文 SHA-12）且有同键先例者，2／2 采先例值、0／2 采 spec 面字面**。`P_B_ECR_BASELINE` 为**标量读数型**（`value` ＝ 数值 `1.3333…`，非文件哈希）故另立 JSON 指针式，**不适用于本锚**（本锚 `value` ＝ 承载件全文 SHA-12 `9e09214cf088`）。

### §3-3 对照实验 C：**承载件实际内容结构**（`9e09214cf088` 逐字读出 · 供 `field` 表征）

| 结构面 | 实测内容 |
|:--|:--|
| 成员数 | **10**（GT-1 … GT-10） |
| 名单面 | **名-①**（PI 已裁闭 · Q-2） |
| 终态词表 | 五终判 `pass`／`af`／`kd`／`fail`／`give-up`（本件 `af` 计数 **0**） |
| 终态分布 | **`pass` 4（GT-1／GT-4／GT-6／GT-8）｜`fail` 1（GT-5）｜`kd` 5（GT-2／GT-3／GT-7／GT-9／GT-10）｜`af` 0｜`give-up` 0** |
| 行式 | 最简一行一式 · §3 之 6 列（PI 已核准沿用 · Q-6） |
| family 标注 | GT 判死裁定族（10 个） |
| 载体性质 | **自足冻结文本** · **单流全文型**（H-2，先例 3/3） |

⚠ **与 spec 面字面之冲突（如实登记）**：spec L27 之 `kills={"GT-1":true, ...}` 用**布尔值** `true` 表成员，而承载件实际承载的是**五终判字面**（`pass`／`fail`／`kd`）⇒ 二者**内容不同构**。且该 `kills` 字面之**数据实体 0 在盘**（5 锚草案 §2-4 逐字「`kills` 字段声明仅存 3 份 spec 锚表，**数据实体 0 在盘**」），H-4 已明定其**无须被序列化**。

---

## §4 双路并列候选表（**4 候选 · ⛔ 0 代择**）

| 候选 | `field` 拟值（逐字） | 来源线 | 出处（逐字） | 体例匹配度 | 与 H-4 相容性 |
|:-:|:--|:-:|:--|:--|:--|
| **C-甲** | `kills=10 GT` | 预实验 | 先例 `03c6c01f3697` 之 `P_A_KILL_LINE.field` **逐字**（其 `object` ＝「P-A V0 spec §1 GT 判死裁定族」，与本锚**同对象同规模**：GT 判死裁定族·10 成员·单流全文型） | **高** —— 同族先例中**唯一与本锚对象逐字同构**者；同批 5 锚内「文件哈希型锚采先例值」实测 **2／2** | ✅ 短串·表征说明·⛔ 0 触锚值 |
| **C-乙** | `10 成员终态 (pass 4 / fail 1 / kd 5 / af 0 / give-up 0)` | 预实验 | 承 `KT_B1_KILL_LINE.field` 之「档位清单」型 ＋ 承载件 §3 末行**实测**分布 | **中高** —— 形制沿先例同族之第二种写法；内容 100% 出自已生效承载件（**可核**） | ✅ 同上 |
| **C-丙** | `kills={"GT-1":"pass", ...}` | 预实验 | 承 spec L27 之**映射形**（承「`kills` ＋ 逐成员」之形），惟值域依承载件实际改为五终判字面 | **中** —— 沿 spec 面形；⚠ 与 spec 原文（`true`）**不同构** ⇒ 若采，**须 PI 明定**其属「按承载件实际改写」抑或「spec 原文照录」 | ✅ 同上 |
| **C-丁** | `kills={"GT-1":true, ...}` | 预实验 | canonical `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` **L27 逐字照录** | **低** —— 三失：① 值域 `true` 与承载件实际终态不合；② `...` 省略号使其**不可解析**；③ 该字面**数据实体 0 在盘**且 H-4 明定无须序列化 ⇒ 作「表征说明」与承载件内容**脱节** | ✅ 同上（但语义脱节） |

**文献线候选**：**0**（§2-4）⇒ 上表 4 候选**全部出自预实验线**；文献线**未贡献任何候选**，此为**如实结果**，非遗漏。

---

## §5 并列结论与排序建议（**候 PI 裁 · ⛔ 0 径行采认**）

### §5-1 首选（**一句**）

> **首选 `C-甲`：`field` ＝ `kills=10 GT`** —— 依先例 `P_A_KILL_LINE` 之**逐字同构**（同对象·同规模·同「单流全文型」）而定，且与同批 5 锚内「文件哈希型锚 2／2 采先例值」之实测判据一致。

**支撑三条（逐条可核）**：

1. **同构先例唯一**：先例 `P_A_KILL_LINE` 之 `object` 逐字为「P-A V0 spec §1 GT 判死裁定族」，与 canonical L27 之「GT 判死裁定族（10 个）」**同族同规模**；二者 `value` 皆为**单一承载件全文**之 SHA-12（H-2 单流全文型，先例 3/3）。
2. **同批实测判据 2／2**：`P_B_FROZEN_RUNS` 采 `runs=5 frozen`、`P_B_LLM_CLIENT` 采先例值（`field_note` 逐字「逐字沿 KT-A1 先例」）⇒ **凡文件哈希型锚且有同键先例者，v2 一律采先例值**。
3. **⛔ 0 触锚值**：H-4 明定 `field` ＝ 表征说明、**非被哈希对象** ⇒ 改 `field` **不改**承载件字节流 ⇒ 锚值 `9e09214cf088`／18905 B **恒定**，无锚值二次漂移风险。

### §5-2 备选与**采择条件（供 PI 一键裁）**

| 若 PI 认为… | 则取 | 理由 |
|:--|:-:|:--|
| `field` 只需**标识族与规模**（最简，沿先例最短写法） | **C-甲** `kills=10 GT` | 先例逐字；最短；无冗余 |
| `field` 须**反映承载件实际终态分布**（信息量优先） | **C-乙** `10 成员终态 (pass 4 / fail 1 / kd 5 / af 0 / give-up 0)` | 承 `KT_B1_KILL_LINE` 之档位清单型；内容 100% 出自已生效件 |
| `field` 须**沿 spec 面字面**（规格对齐优先） | **C-丁**（并**须**接受 §4 所列三失） | ⚠ 语义与承载件脱节 |
| `field` 须**沿 spec 形但按实际内容** | **C-丙**（并**须**明定值域改写授权） | ⚠ 属对 spec 字面之改写 |

### §5-3 本棒**未**主张者（⛔ 逐项列明）

- ⛔ **0 主张**唯一正解（先例同族 3 枚写法互异 ⇒ `field` 无单一强制体例，见 §3-1(a)）。
- ⛔ **0 主张** C-甲 之 `10 GT` 已由 PI 核准；**0** 将本件任一候选**径行采认**。
- ⛔ **0 以文献线**为任一候选背书（文献线 0 直接命中，§2-4）。

---

## §6 ⛔ 纪律边界（本棒自查 · 逐项）

| 项 | 状态 |
|:--|:--|
| ⛔ 0 回填 v2 JSON 之 `field` | ✅ 未动（`P_B_KILL_LINE.field` 仍为「候 PI 给」） |
| ⛔ 0 回改承载件 v1／草案 v0 | ✅ 未动（只读；直算值 `9e09214cf088`／18905 与登记件逐位相符） |
| ⛔ 0 回改迁移登记件 §7 R-1 | ✅ 未动 |
| ⛔ 0 代 PI 裁 | ✅ 只出候选＋依据＋排序建议，**择归 PI** |
| ⛔ 0 宣告闭 / `C3` 通过 / ①毕 | ✅ 未宣告 |
| ⛔ 0 跑实验 | ✅ 未跑（跑禁已解但本棒无需实验） |
| ⛔ 0 编造文献 | ✅ 文献线 0 命中**如实报**；唯一邻证正文复核 404 已登记（§2-3） |
| ⛔ 0 编造不确定信息 | ✅ 全部候选均标出处与匹配度；⛔ 0 断言「正解」 |
| ⛔ 0 经手 key（R4：key 永不明文） | ✅ 未读 `.env`、未取任何 key |
| ⛔ 0 上传／0 远端写 | ✅ 仅只读联网检索，无任何写出 |
| ⛔ 0 移动／重命名／删除既有件 | ✅ 未动 |
| ⛔ 0 用他棒名头署名 | ✅ 落款为 `field-value-sourcing` 棒 |

---

## §7 字节级自报（**落盘后盘上实测**）

**⚠ 自指悖论（沿承载件 v1 §8-5 之同一口径）**：本件**不自写入**自身 SHA-12／bytes（填入即改本件内容 ⇒ 其指纹随之变）⇒ 该二项之**盘上实测值载于交付回执**。下表 7 项为**内容无关之字节属性**，可在本件内如实自报且恒真。

| 项 | 本件自报 | 要求 | 判 |
|:--|:--|:-:|:-:|
| 落盘方式 | Python `io.open(..., encoding='utf-8', newline='\n', errors='strict')` **直写** | ⛔ 0 经 PowerShell 管道中转 UTF-8 正文 | ✅ |
| Windows 路径 | **一律 raw 字符串** | —— | ✅ |
| SHA-12 | *（见交付回执 · 自指悖论）* | —— | ⚠ 不可自含 |
| bytes | *（见交付回执 · 自指悖论）* | —— | ⚠ 不可自含 |
| BOM | **False** | False | ✅ |
| CRLF | **0** | 0 | ✅ |
| CR | **0** | 0 | ✅ |
| TAB | **0** | 0 | ✅ |
| 其他控制字符（含 0x7F） | **0** | 0 | ✅ |
| nonAscii | **> 0**（中文未损） | > 0 | ✅ |
| U+FFFD | **0**（以 `chr(0xFFFD)` 构造探针计） | 0 | ✅ |
| 落盘前闸 | `Test-Path=False` ＋ glob **0** 命中 | —— | ✅ 已实测 |

---

## §8 交付回执（**待 PI 裁之面**）

- **待 PI 择**：`P_B_KILL_LINE.field` 之正式值 ⇒ 四候选（C-甲／C-乙／C-丙／C-丁）＋排序建议（首选 **C-甲** `kills=10 GT`）。
- **PI 择毕之后**（**另棒**执行，本棒 ⛔ 0 预行）：回填 v2 之 `field`／`field_status`／`field_note` ＋ 更新 U-1；⛔ 0 由本棒代行。
- **连带**（沿迁移登记件 §7，本棒 ⛔ 0 动）：R-4（v2 回填，**另棒**）｜R-2／R-3（GT-2/3/7 与 GT-9/10 之解封，**PI 另裁**）｜R-5（U-4／U-5／KD-4）。

---

**落款**：`field-value-sourcing` 棒 · 2026-10-15｜**候 PI 核准 · ⛔ 0 径行采认**｜授权源：PI 2026-10-15 11:31 口头令「Q-7 `field` 正式值给不了，沿用文献与预实验双线」（口头令 · 本件为转达；同批卡答登记件 v12 `97111fee4410` 之 Q1／Q2 为上位授权面）｜跑禁已解（v6 `7e95b053e249`）｜**文献线 5 式 · 净命中 1／5 且 0 体例内容 · 正文复核 404**｜**预实验线 4 候选 · 首选 `kills=10 GT`**｜⛔ 0 回填 v2 JSON · 0 回改既有件（含承载件 v1 与草案 v0）· 0 代 PI 裁 · 0 宣告闭／`C3`／①毕 · 0 跑实验 · 0 编造文献 · 0 经手 key · 0 上传／0 远端写 · 0 移动／重命名／删除。
