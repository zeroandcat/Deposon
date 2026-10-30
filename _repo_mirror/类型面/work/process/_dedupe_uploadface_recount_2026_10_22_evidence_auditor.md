# 去重复族·上传面·按「件数尺」重判（2026-10-22）

- 自路径：`〔幽灵引用·未上传:_dedupe_uploadface_recount_2026_10_22_evidence_auditor.md〕`
- ⚠ **落盘路径之差（停手闸失败之故）**：派工单指定之 `..._recount_2026_10_22.md` 已于 19:26:27 被**主代理直算件**占用（`6a44ad8f7f5a`）⇒ 停手闸（要求 `Test-Path`＝False）**失败** ⇒ 本棒**⛔ 0 覆写他写者件**，改落**同目录 sibling 路径**（详见 §2-5）
- 棒别：evidence-auditor（证据链审计面）· 观测时点 **2026-10-22 18:22:56**（普查）／18:12（面勘）／18:17:09（归档区·GLM 仅计数）
- 令源：派工单《去重复族按「件数尺」重判（上传面）· 证据链》
- 判据基座：PI 2026-10-22 逐字三条（转录于 §1-2·**原文照录**）
- 铁律：⛔ 0 移动／⛔ 0 改名／⛔ 0 删除／⛔ 0 建目录／⛔ 0 回改既有件一字 · ⛔ 0 触归档区内容（**仅计数**）与 `GLM` 面（**仅计数**）· **⛔ 0 以体积为任何理由** · ⛔ 0 联网 · ⛔ 0 读凭据 · ⛔ 0 落五终判／闭 KD／宣告段毕／代裁
- 状态：**0 移动 0 删除 0 改名 0 建目录**——本件系**新建**（本件 sibling 路径落前停手闸：`Test-Path`＝False ＋ 长名式 `.Name -like` 0 命中 ＋ 全仓同名 0 命中）
- 仪器：Python 3.14.7 `os.walk` 穷举 ＋ `hashlib.sha256` 全字节 ＋ 自建引用面扫描器（闸门式精确匹配）——仪器自审见 §2-3

---

## §0 摘要（一屏自足）

| 项 | 数 | 口径 |
|---|---:|---|
| **上传面内重复族（本棒实测）** | **110 组／229 件／冗余 119 件** | 全字节 SHA-256 相同 |
| ├ 可减（按新尺·**已扣禁令锁定层**） | **30 组／35 件** | 其中跨区 24 件・单区内 11 件 |
| ├ ⛔ 0 减·**禁令锁定** | 69 组／71 件 | 落委派域 `E3`–`E8`／对比件域 `MC-E1`–`MC-E5`／内部真册禁令面（详见 §1-4） |
| ├ ⛔ 0 减·代码源/唯一生成器 | 8 组／10 件 | 读数件之生成器，删之即失可复算性 |
| ├ ⛔ 0 减·权威件 | 3 组／3 件 | PI 裁答／判定／登记面 |
| └ ⛔ 0 减·语义不同 | 0 组／0 件 | 0 字节空件＝洁净运行之证据面（**本批该族 2 件全落 pullback 面 ⇒ 已并入「禁令锁定」**） |
| 上传面总件数（时点截面） | 3924 件（repo 2648 ＋ sub 1276） | 排除 `.tmp`／`results\.tmp` |
| 可减件占上传面之比 | **0.89%** | 件数尺·**不计体积** |
| 减后须登记「旧路径→新路径」 | **508 条**（其中路径式引用处 473 ＋ 件自身 35） | 逐处登记，不改原引一字 |

**与旧账之差（一句话）**：旧账判「删除面 ＝ 0」（`cbd85f8c5522`·§2-1）；新尺下**件面可减 35 件**——差之所在不在体积，而在**旧尺把「生幽灵」当否决项**；新尺下幽灵可登记（留映射表即可），故重复件**可减**，而**禁令锁定／代码源／权威件／语义不同四类仍不减**。

**荐案**：**分三批**，由本棒出候选、PI 逐单放行——①**单区内**组先做（登记面小，11 件）；②**跨区**组须 PI 先定「留 repo 侧抑或留被引多者」之取向（PI 10-12「两区件数拉平」与「权威链锚于 repo」两条取向相反，**本棒不代裁**，共 24 件）；③**⛔ 0 减之 80 组／84 件**（禁令锁定 71 件 ＋ 代码源 10 件 ＋ 权威件 3 件 ＋ 语义不同 0 件）**一律不动**；④**代码源之窄读**（其中 8 组之代码件自身即有逐字节副本，删其一并不失可复算性）**另请 PI 裁**——本件按宽读计（不减）。

⚠ **本单 0 移动、0 删除、0 改名**——只出核实与候选；**执行须 PI 逐单令**。

---

## §1 立准（旧账逐字 ＋ 三条硬约束）

### §1-1 旧账逐字回读（**原样引用·⛔ 0 转引·⛔ 0 改写其字**）

**旧读一**——`_reorg_survey_and_disposition_2026_10_22.md`（自测指纹 `cbd85f8c5522`·107,615 B）§2-1 处置总表「噪声·重复副本」行，**逐字**：

> | **噪声·重复副本** | **保留** | 204（99 组） | 冗余 10,161,132 | 字节全同之族（SHA-12 相同） | **99 组逐组实测皆有活引用**（0 组零引用）⇒ 删任一侧即生幽灵；且「同字节异名」本身即复现性之据 ⇒ **删除面 ＝ 0** |

同件 §4-0 汇总，**逐字**：

> | 拟去处 | 件数 | 字节 | 活引用合计 | 快照提及合计 |
> |---|---:|---:|---:|---:|
> | 归档区（`〔归档区〕`） | 227 | 9,604,966 | — | — |
> | `deposon-sub`（项目衍生件） | 56 | 3,146,827 | — | — |
> | 不移动 | 32 | 111,444,076 | 0（路径式） | — |
> | **合计** | **315** | **124,195,869** | 活引用 **11,492**｜路径式 **8,884** | 快照提及 **3,473** |

同件 §6-2「本方案若执行将新增多少幽灵」之「重复副本」行，**逐字**：

> | 0 字节件（30）＋ 重复副本（204） | 234 | **0 处**（**故不删**） | 皆在引用链上（活引用 3–40 处；99 组重复族 0 组零引用） |

**旧读二**——`_bloat_inventory_2026_10_22.md`（自测指纹 `3c55ea8be914`·12,907 B）§2-1「逐字节重复」，**逐字**：

> 全树 **118 组／270 件／可回收 10.6 MB**（`.tmp` 域 24 组）。⚠ **「可留其一」不成立**：每组两侧**皆在引用链上** ⇒ 删除面 ＝ 0（「同字节异名」本身即复现性之据）。其中 28 件为 0 字节件（`e3b0c44298fc`），且**25 件皆被 md 引用**（删之即生幽灵）。

### §1-2 三读并出之事实（**⛔ 0 择一充事实·⛔ 0 断言谁错**）

| 读 | 载体（族标＝其 SHA-12） | 时点 | 组／件 | 判重口径 | 扫描面 | 冗余字节 |
|---|---|---|---:|---|---|---:|
| 旧读一 | 勘查件 `cbd85f8c5522` | 2026-10-22 16:35:59 | 99／204 | SHA-12 相同 | repo 全域 ＋ sub 文本面件 | 10,161,132 |
| 旧读二 | 臃肿账 `3c55ea8be914` | 2026-10-22 00:39–00:52 | 118／270 | 逐字节相同 | 「全树」（`.tmp` 域 24 组） | ~10.6 MB |
| **本读** | 本件（SHA-12 见页脚自证） | **2026-10-22 2026-10-22 18:22:56** | **110／229** | **全字节 SHA-256** | **上传面＝repo 去 `.tmp` ＋ sub 全域** | 1,226,106（冗余 35 件） |

⇒ **同一「重复族」在两份在册件里有两套数，在本件为第三套**；三套**并存登记**，本棒**不判孰是孰非**（判权属 verdict-keeper）。三套数之**口径差**见 §5-3 归因表。

### §1-3 PI 逐字之三条硬约束（本单判据）

> 「**因为有Agent与RAG，体积不是大问题，文件数才是**」
>
> 「**归档区不上传，日志面就留着吧，而且几乎不会有什么干扰而仅供复核**」

| 标 | 约束 | 本件之落实 |
|---|---|---|
| **甲** | 唯一判据＝**件数**；体积**不论** | §3 表虽列字节（供对照旧账），但**无一条处置以体积为据**；§5 净减只以件计 |
| **乙** | 「删任一侧即生幽灵」**不再是阻断理由**（幽灵**可登记**：留「旧路径→新路径」映射表即可） | §4 逐组以「登记义务」而非「生幽灵」判可减；登记条数入 §5 |
| **丙** | **只看上传面**＝repo 去 `.tmp` ＋ `deposon-sub`；**归档区不上传，不在射程** | 普查根＝`〔本地路径已脱敏〕`（排 `.tmp`）＋ `〔本地路径已脱敏〕`；归档区（40,121 件）**仅计数·⛔ 0 列名内容**，且**不入普查、不入判减** |

### §1-4 **先查惯例**（PI 2026-10-22 18:4x 逐字之硬要求：**⛔ 0 以转述充依据**）

**检索式（全仓）**：`永不上传|不得上传|严禁上传|禁上传|⛔ 0 上传|0 上传` ⇒ 命中 **264 件／662 处**（含 `.tmp` 之工作稿）；**核心禁令源件逐件开卷核读**如下（指纹皆**本棒自测**）：

| 源件（仓相对路径） | SHA-12 | bytes | 载何禁令（逐字要点） |
|---|---|---:|---|
| `letters/_internal_true_clue_book_2026_10_12.md` | `355ea3c09461` | 408,329 | §0 行 3-5：**「⛔ 本件永不上传。⛔ 本件不入上传面。⛔ 本件不随包、不外发、不交任何外部方（含 KIMI／Trae／coze／GLM 之对外通道）。」**｜行 5：**「⛔ 严禁将本件之任一节、任一条目、任一术语…转抄入任何上传面件或对外件。」**｜行 203-205 之 3 条铁律 |
| `letters/_commission_kimi_upload_2026_10_18_v0.4_draft.md` | `51ca14265086` | 61,027 | **委托域 E1–E8**（行 207-214）：E1 `.tmp/`｜E2 归档区｜**E3 `letters/` 全区 0 上传**｜**E4 隐私面 ＋ `results/_archive_2026_09_20/` ＋ 密钥门 1 永不上传**｜**E5 本地旧名件 10 件**｜E6 本地独有 5 件｜E7 当日审计/登记 5 件（⛔ 候 PI）｜E8 本机绝对路径泄漏件 3 件｜§7.3 行 350 carve 自证：**「`_remote_pullback_2026_10_17/` **0 自行纳入上传面**」**｜§9 面① 1-1 点名密钥门路径 |
| `letters/_commission_kimi_upload_2026_10_01_v0.2.md` | `a77f7d509285` | 35,421 | 上游委托件（v0.4 之沿承源·E3 之出处「v0.2 §2.2（沿 A3）」） |
| `letters/_commission_kimi_upload_with_d7_2026_10_09_v0.3.md` | `ae00f6fee19e` | 36,763 | 委托域 E3/E4/E5 同表（行 209-213），**「E4 隐私面 10 ＋ `results/_archive_2026_09_20/` 2 ＋ 密钥门 1」** 之件数口径所在 |
| `letters/_commission_kimi_supplemental_sync_2026_10_18_draft.md` | `6bd84d3f4e94` | 58,843 | **对比件域 `MC-E1`–`MC-E5`**（行 121-125）：MC-E1 `.tmp/`｜MC-E2 `letters/` carve｜MC-E3 `S3` 隐私面形态 23 件｜MC-E4 噪声／S5 临时件族 127 件｜MC-E5 H4 严禁件｜**逐件清单之唯一源** 指向 `.tmp/gh_survey_r2/survey_r2_consolidated.json`（`0a37bbd63bd5`）之 `S3_dataset_literal.paths` 25 条 ＋ `S5_temp_heuristics.ABC_union_list` 58 条 |
| `.tmp/gh_survey_r2/survey_r2_consolidated.json` | `0a37bbd63bd5` | 215,148 | **逐件源**（S3 25 条 ＋ S5 58 条 之唯一出处——⛔ 0 自造清单 ⇒ 回读对比件） |

🔴 **编号冲突登记（⛔ 0 交叉引用·⛔ 0 互相代入）**：委派域之 `E1`–`E8` 与对比件域之 `E1`–`E5` **为两套独立编号、实体义相冲**（对比件域行 64-67 自陈；登记 `KD-SSC-03`）。故本件**只**使用「**委托域 `E3`/`E4`/`E5`/`E6`/`E8`**」与「**对比件域 `MC-E3`/`MC-E4`**」并**各标源件与行号**；本件**不将二者混引**。

**锁定层如何落到本单（实测）**：上传面 **229 个重复成员**逐件试上列禁令面，得命中数如下——

| 禁令码 | 面 | 命中成员数 |
|---|---|---:|
| `E3` | face | 0 |
| `E4-arch` | face | 0 |
| `E4-key` | file | 2 |
| `E6` | file | 0 |
| `E8` | file | 2 |
| `PULLBACK` | face | 71 |
| `MC-S3` | file | 0 |
| `MC-S5` | file | 7 |
| `CLUE` | file | 0 |

⇒ 落在禁令面之重复成员合计 **82 件**，涉 **69 组** ⇒ **⛔ 0 减·禁令锁定**（组级：组内任一成员落禁令面 ⇒ 整组不减）。

⚠ **一件关键命中**：本棒普查**头号组**（`0a1e91d6f772`·n=3·**2,292 B**）即 v0.4 §9 面① 1-1 所点之**「H4 密钥门件」**（`results/_d05_sanity_3backbone_20260918_100110.json`，**字节逐位吻合**）⇒ 若无「先查惯例」一层，此组将误入可减候选——**此即 PI 令「先查惯例」之实价值**。

---

## §2 证器（射程·时点·仪器自审）

### §2-1 射程与时点

| 项 | 实测 | 处置 |
|---|---:|---|
| 根 A `〔本地路径已脱敏〕`（**排除** 任意层级之 `.tmp` 目录，含 `results\.tmp`） | 2648 件 | 入普查 |
| 根 B `〔本地路径已脱敏〕` | 1276 件 | 入普查 |
| **上传面合计** | **3924 件**（212,337,883 B） | 入普查 |
| 对照面：repo **含** `.tmp`（+ sub） | 8231 件 | **仅供归因**（不计可减） |
| 排除面 `〔归档区〕`（归档区） | 40,121 件／1,397,000,905 B／19,495 子目录 | **仅计数·⛔ 0 列名内容**（18:17:09 实测，与旧账 §1-1 逐位相符） |
| 排除面 `〔本地路径已脱敏〕` | 21 件／2,578,337 B／3 子目录 | **仅计数·⛔ 0 触内容**（18:17:09 实测，与旧账 §1-1 逐位相符） |
| 第三区 `Deposon_v1_2_0_交付包` | 36 件／3,395,072 B | **不在 PI 所定上传面**（PI 令源只列 repo ＋ sub）⇒ 不入本单射程；仅计数备查 |

**时点**：普查生成于 **2026-10-22 2026-10-22 18:22:56**（耗时 173.1 s）；面勘 18:12；归档区/GLM 计数 18:17:09。**仓为活面**（并行棒仍在写入）⇒ 一切计数为**时点截面**，执行前须重测。

### §2-2 判重口径

- **唯一判据**：**全字节 SHA-256 相同**（`hashlib.sha256` 逐件全量复算；⛔ 0 用内建 `hash()`；⛔ 0 以 SHA-12 前缀判同；⛔ 0 以「大小相等」判同）。
- **前缀口径之对照实测**（本棒加做）：在本仓**每一个作用域**内，按 SHA-12 前缀分组与按全字节 SHA-256 分组所得**组数与件数完全相等**（上传面 110/229；含 `.tmp` 214/475；repo 全树 120/279）⇒ **本仓面内 SHA-12 前缀碰撞 ＝ 0**，故旧账之「SHA-12 相同」与本棒之「全字节相同」**在判重结果上等价**——新旧之差**不可**归因于判重口径。
- **组之定义**：同一 SHA-256 之全部成员；`冗余件数 ＝ n − 1`。

### §2-3 仪器自审（含一次**算法返工**）

| 项 | 事实 |
|---|---|
| 穷举方式 | `os.walk` 递归（⛔ 0 单用 `-Filter`；⛔ 0 跟随符号链接）；排除面以目录名硬排除 |
| 指纹 | `hashlib.sha256` 全字节（⛔ 0 内建 `hash()`；⛔ 0 仅取前若干字节） |
| **返工一（仪器自身之误差源）** | 首版引用面扫描器用**巨型 alternation 正则**逐文件全文匹配 ⇒ 复杂度 O(内容长 × 模式数)，对 18 MB 级 `.json` 实测过慢，**首跑超时未成**；**改器不迁就**——重写为**闸门式**（先以 C 级 `in` 逐模式筛，命中者再走单模式边界精确计数），第二跑 **173.1 s** 完成。**未改数据·未改口径·未改阈值** |
| 引用面覆盖 | 扫描 3862 件／204,447,474 B（UTF-8 可解且无 NUL 者）；**跳过 62 件／7,890,409 B**（二进制或不可解）⇒ 一切「引用数」皆为**下界**（承旧账同款声明之精神，但面更宽） |
| 引用面之范围 | **仅上传面**（repo 去 `.tmp` ＋ sub）——旧账之引用面含 `.tmp` 全域，故本棒引用数**不等于**旧账引用数，两者**不可相减** |
| 自指处理 | 件在**自身正文**中之自提及**单列**（`self_hits`），**不计入活引用** |
| 键形态自扫 | 落盘后对本件跑 `` 词边界键形扫描（`sk-`／`tp-`／`ark-`／`API_KEY=`／`Authorization: Bearer`／`AKIA`／`gh[pousr]_`）⇒ 须为 CLEAN 方算完（见 §6-3） |
| 仪器产物位置 | 普查/计划/摘要/口径扫描脚本与 JSON 皆落 **仓外 TEMP**（`〔本地路径已脱敏〕`）；**仓内 0 写入**（本件除外） |

### §2-4 引用面口径（分两列·边界规则写明）

- **路径式**＝引文写出**带路之指**（如 `results\xxx\yyy.md`）：按件的**根相对路径**（POSIX 与反斜杠两形）计数，边界规则 `(?<![A-Za-z0-9_.\-])…(?![A-Za-z0-9_.\-])`。
- **裸名式**＝引文**只写件名不带路**（如 `yyy.md`）：按**件名**（含扩展名）计数，同一边界规则。
- **活引用**＝**他件**（≠ 本件）之提及数；**快照提及**（镜像／索引件里的旧提及）**未单列**——本棒不复制旧账之快照面界定（其快照面在 `.tmp` 内，属本单射程外）。
- **同名歧义**：若同一件名在上传面出现于多个不同路径，裸名式引用**归属不可分**⇒ 该件在表内标〔同名歧义〕，其裸名式计数**在同族各件间同记**，不作区分。

---

### §2-5 **与主代理直算件之互校（两套独立仪器·交叉验证）**

落盘前实测：**派工单指定之目标路径已被主代理 19:26:27 之直算件占用**（`results\_dedupe_uploadface_recount_2026_10_22.md`·33,058 B·SHA-12 `6a44ad8f7f5a`）⇒ **落前停手闸失败**（该闸要求 `Test-Path`＝False）⇒ 本棒**⛔ 0 覆写他写者件**，改落**同目录 sibling 路径**（`..._evidence_auditor.md`），并将该路径之差**如实登记**，请 PI／主代理裁「二件并存抑或以何者为准」。

**互校结果（归因闭合）**：

| 口径 | 扫描件数 | 组 | 件 | 冗余 | 备注 |
|---|---:|---:|---:|---:|---|
| 主代理直算件（19:26:27·`6a44ad8f7f5a`） | 4,058 | **111** | **233** | **122** | 其 §0 表载「排除 `.tmp\`／`results\.tmp\`」，然其表内含 `results\.tmp\` 之 2 件 ⇒ **实射程含 `results\.tmp`**（**口径实况与自述不符·如实登记**） |
| **本棒以同一口径复算**（root `.tmp` 排、`results\.tmp` **入**） | 4063 | **111** | **233** | **122** | ✅ **与主代理件逐位吻合** ⇒ 两套独立仪器互证 |
| **本棒正式口径**（`.tmp` 与 `results\.tmp` **皆排**·派工单丙） | 3929 | **110** | **229** | **119** | 与上行之差 ＝ `results\.tmp` 面（134 件）之贡献 |

⇒ **差之归因已闭合**：主代理件与本棒件之差 **1 组／4 件／冗余 3**，**全部来自 `results\.tmp` 面**（含 2 件 0 字节在途件：`_s19memo2_compactions_2026_10_22.md`／`_s19memo2_dispatch2_2026_10_22.md`）——该面按派工单丙**不在上传面**，故本棒正式口径**不取**之。**本棒与主代理直算件在共同口径下结论一致（互证通过）**。

---

## §3 逐组表（上传面内重复族·逐组具名）

排序：**冗余件数降序 → 件数 n 降序**。表列 `P`＝路径式活引用数／`N`＝裸名式活引用数（均为**他件**引用）。`全在上传面`一列恒为「是」——**本表只取自上传面**（构造使然）；其信息在 §5-3 与旧账逐组对照。

| `SHA-12` | 件数 n | 单件字节 | 冗余 n−1 | 逐件路径（P／N） | 路径式 | 裸名式 | mtime 最早者 | 全在上传面 | 跨区 repo↔sub | 分类 | 禁令码 |
|---|---:|---:|---:|---|---|---|---|---|---|---|---|
| `0a1e91d6f772` | 3 | 2,292 | 2 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json` P=3／N=84〔同名歧义〕<br>`repo/_remote_pullback_2026_10_17/results/_d05_sanity_3backbone_20260918_100110.json` P=4／N=84〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json` P=42／N=84〔同名歧义〕 | 3／4／42 | 84／84／84 | 2026-09-24 19:21:31<br>`sub/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `E4-key`、`PULLBACK` |
| `1fc5f3ab3f93` | 3 | 2,022 | 2 | `sub/.trae/audit/compile_evidence/compile_runner.ps1` P=11／N=71〔同名歧义〕<br>`sub/.trae/audit/compile_evidence/v2_overfull_fix_20260909/compile_runner.ps1` P=11／N=71〔同名歧义〕<br>`sub/.trae/audit/compile_evidence/v2pre_h1h3_20260909/compile_runner.ps1` P=11／N=71〔同名歧义〕 | 11／11／11 | 71／71／71 | 2026-09-08 22:46:03<br>`sub/.trae/audit/compile_evidence/compile_runner.ps1` | 是 | 否 | ⛔ 0 减·代码源 | — |
| `25f745609658` | 3 | 612,511 | 2 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_v41_flash_rag_caption_embs.bak.json` P=1／N=58〔同名歧义〕<br>`repo/corpus/v20_caption_surface/_v41_flash_rag_caption_embs.bak.json` P=29／N=58〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_v41_flash_rag_caption_embs.bak.json` P=14／N=58〔同名歧义〕 | 1／29／14 | 58／58／58 | 2026-09-10 17:05:53<br>`repo/corpus/v20_caption_surface/_v41_flash_rag_caption_embs.bak.json` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `MC-S5`、`PULLBACK` |
| `43d9ce160fc8` | 3 | 2,460 | 2 | `repo/results/boss_pc_1_real_2d_ising_2026_09_15.json` P=35／N=46〔同名歧义〕<br>`sub/results/boss_pc_1_real_2d_ising_2026_09_15.json` P=0／N=46〔同名歧义〕<br>`repo/results/boss_pe_1_real_2d_ising_2026_09_15.json` P=35／N=46 | 35／0／35 | 46／46／46 | 2026-09-15 13:34:49<br>`repo/results/boss_pe_1_real_2d_ising_2026_09_15.json` | 是 | 是 | **可减** | — |
| `6cbb8ba01bfb` | 3 | 15,409 | 2 | `repo/results/_d9_e2e_backup_2026_10_13/_s4_heldout_sampling_seedprime_items_2026_10_10.json` P=3／N=120〔同名歧义〕<br>`repo/results/_d9_e2e_rerun_backup_2026_10_13/_s4_heldout_sampling_seedprime_items_2026_10_10.json` P=1／N=120〔同名歧义〕<br>`repo/results/_s4_heldout_sampling_seedprime_items_2026_10_10.json` P=54／N=120〔同名歧义〕 | 3／1／54 | 120／120／120 | 2026-10-10 23:07:39<br>`repo/results/_d9_e2e_backup_2026_10_13/_s4_heldout_sampling_seedprime_items_2026_10_10.json` | 是 | 否 | **可减** | — |
| `8933d61b180a` | 3 | 3,553 | 2 | `repo/results/boss_pc_2_real_transverse_ising_2026_09_15.json` P=39／N=50〔同名歧义〕<br>`sub/results/boss_pc_2_real_transverse_ising_2026_09_15.json` P=0／N=50〔同名歧义〕<br>`repo/results/boss_pe_2_real_transverse_ising_2026_09_15.json` P=51／N=68 | 39／0／51 | 50／50／68 | 2026-09-15 13:34:49<br>`repo/results/boss_pe_2_real_transverse_ising_2026_09_15.json` | 是 | 是 | **可减** | — |
| `94b5398be76c` | 3 | 2,364 | 2 | `repo/results/boss_pc_3_real_reservoir_2026_09_15.json` P=33／N=44〔同名歧义〕<br>`sub/results/boss_pc_3_real_reservoir_2026_09_15.json` P=0／N=44〔同名歧义〕<br>`repo/results/boss_pe_3_real_reservoir_2026_09_15.json` P=32／N=43 | 33／0／32 | 44／44／43 | 2026-09-15 13:34:49<br>`repo/results/boss_pe_3_real_reservoir_2026_09_15.json` | 是 | 是 | **可减** | — |
| `d21912a05d79` | 3 | 1,017 | 2 | `sub/results/attack_pc_a1_resampling_2026_09_15.json` P=22／N=30<br>`repo/results/boss_pc_1_a1_resampling_2026_09_15.json` P=30／N=42〔同名歧义〕<br>`sub/results/boss_pc_1_a1_resampling_2026_09_15.json` P=0／N=42〔同名歧义〕 | 22／30／0 | 30／42／42 | 2026-09-15 13:34:48<br>`repo/results/boss_pc_1_a1_resampling_2026_09_15.json` | 是 | 是 | **可减** | — |
| `dfb02ade1474` | 3 | 591 | 2 | `repo/corpus/v20_caption_surface/_inspect_captions.py` P=30／N=86〔同名歧义〕<br>`sub/results/_archive_2026_09_24/_inspect_captions.py` P=31／N=86〔同名歧义〕<br>`sub/results/_inspect_captions.py` P=13／N=86〔同名歧义〕 | 30／31／13 | 86／86／86 | 2026-09-10 17:31:00<br>`repo/corpus/v20_caption_surface/_inspect_captions.py` | 是 | 是 | ⛔ 0 减·代码源 | — |
| `01e63e488ce2` | 2 | 3,207 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch3_2026_09_18.py` P=3／N=24〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_fix_batch3_2026_09_18.py` P=14／N=24〔同名歧义〕 | 3／14 | 24／24 | 2026-09-18 13:44:20<br>`sub/results/_archive_2026_09_20/_fix_batch3_2026_09_18.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `023f936f80fb` | 2 | 2,168 | 1 | `repo/_remote_pullback_2026_10_17/results/llm_prior_cache_v18_direction.json` P=3／N=54〔同名歧义〕<br>`sub/results/llm_prior_cache_v18_direction.json` P=31／N=54〔同名歧义〕 | 3／31 | 54／54 | 2026-08-23 23:04:12<br>`sub/results/llm_prior_cache_v18_direction.json` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `048ebc99177c` | 2 | 1,029 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_tmp_inspect_5model.py` P=3／N=23〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_tmp_inspect_5model.py` P=15／N=23〔同名歧义〕 | 3／15 | 23／23 | 2026-09-11 11:11:01<br>`sub/results/_archive_2026_09_20/_tmp_inspect_5model.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `MC-S5`、`PULLBACK` |
| `0769f60a0504` | 2 | 2,678 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_final_sha_2026_09_18.py` P=3／N=22〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_final_sha_2026_09_18.py` P=14／N=22〔同名歧义〕 | 3／14 | 22／22 | 2026-09-18 13:48:37<br>`sub/results/_archive_2026_09_20/_final_sha_2026_09_18.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `079108c62a82` | 2 | 21,049 | 1 | `repo/results/_d9_e2e_backup_2026_10_13/_stage3_trigger_readings_items_2026_10_11.json` P=4／N=75〔同名歧义〕<br>`repo/results/_stage3_trigger_readings_items_2026_10_11.json` P=36／N=75〔同名歧义〕 | 4／36 | 75／75 | 2026-10-11 16:52:40<br>`repo/results/_d9_e2e_backup_2026_10_13/_stage3_trigger_readings_items_2026_10_11.json` | 是 | 否 | **可减** | — |
| `0b7e50a8a036` | 2 | 2,938 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_verify_sha_2026_09_18.py` P=3／N=27〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_d05_verify_sha_2026_09_18.py` P=14／N=27〔同名歧义〕 | 3／14 | 27／27 | 2026-09-18 12:41:58<br>`sub/results/_archive_2026_09_20/_d05_verify_sha_2026_09_18.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `0c9addf4a70f` | 2 | 675 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_tmp_inspect_22cap.py` P=2／N=22〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_tmp_inspect_22cap.py` P=14／N=22〔同名歧义〕 | 2／14 | 22／22 | 2026-09-11 11:12:09<br>`sub/results/_archive_2026_09_20/_tmp_inspect_22cap.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `MC-S5`、`PULLBACK` |
| `0d36d7cd0589` | 2 | 30,494 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_tech_B1_dsv4pro.md` P=3／N=34〔同名歧义〕<br>`sub/results/_archive_2026_09_20/review_tech_B1_dsv4pro.md` P=21／N=34〔同名歧义〕 | 3／21 | 34／34 | 2026-09-18 00:35:54<br>`sub/results/_archive_2026_09_20/review_tech_B1_dsv4pro.md` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `15904ecae629` | 2 | 11,105 | 1 | `repo/results/_archive_2026_09_24/_volc_22cap_emb.py` P=29／N=58〔同名歧义〕<br>`sub/results/_volc_22cap_emb.py` P=14／N=58〔同名歧义〕 | 29／14 | 58／58 | 2026-09-10 17:36:26<br>`repo/results/_archive_2026_09_24/_volc_22cap_emb.py` | 是 | 是 | ⛔ 0 减·代码源 | — |
| `18984b04c45e` | 2 | 34,134 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_deposon_v2scripts_reverify_worker_2026_09_18.py` P=3／N=30〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_deposon_v2scripts_reverify_worker_2026_09_18.py` P=14／N=30〔同名歧义〕 | 3／14 | 30／30 | 2026-09-18 13:42:18<br>`sub/results/_archive_2026_09_20/_deposon_v2scripts_reverify_worker_2026_09_18.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `1c59e7b803fe` | 2 | 2,214 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch6_2026_09_18.py` P=3／N=24〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_fix_batch6_2026_09_18.py` P=14／N=24〔同名歧义〕 | 3／14 | 24／24 | 2026-09-18 13:46:45<br>`sub/results/_archive_2026_09_20/_fix_batch6_2026_09_18.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `1dadfaeb2c43` | 2 | 868 | 1 | `repo/_remote_pullback_2026_10_17/results/v20_statcheck_fm_vs_rand.json` P=3／N=35〔同名歧义〕<br>`sub/results/v20_statcheck_fm_vs_rand.json` P=30／N=35〔同名歧义〕 | 3／30 | 35／35 | 2026-08-28 20:44:24<br>`sub/results/v20_statcheck_fm_vs_rand.json` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `218ef1a99f97` | 2 | 11,703 | 1 | `repo/results/deposon_volcengine_minimax_m3_30cells_2026_09_10.py` P=26／N=41〔同名歧义〕<br>`sub/results/deposon_volcengine_minimax_m3_30cells_2026_09_10.py` P=0／N=41〔同名歧义〕 | 26／0 | 41／41 | 2026-09-16 18:20:55<br>`repo/results/deposon_volcengine_minimax_m3_30cells_2026_09_10.py` | 是 | 是 | ⛔ 0 减·代码源 | — |
| `25141de92c50` | 2 | 7,188 | 1 | `repo/results/_xiang14_third_reissue_registration_2026_10_13.md` P=69／N=89〔同名歧义〕<br>`sub/results/_xiang14_third_reissue_registration_2026_10_13.md` P=0／N=89〔同名歧义〕 | 69／0 | 89／89 | 2026-10-13 23:24:08<br>`sub/results/_xiang14_third_reissue_registration_2026_10_13.md` | 是 | 是 | **可减** | — |
| `264f2bf5a3f2` | 2 | 6,687 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_temp_volc_test.py` P=2／N=22〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_temp_volc_test.py` P=13／N=22〔同名歧义〕 | 2／13 | 22／22 | 2026-09-16 11:01:12<br>`sub/results/_archive_2026_09_20/_temp_volc_test.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `MC-S5`、`PULLBACK` |
| `268225ccbb76` | 2 | 4,397 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_reviewer_a_audit_tmp.py` P=2／N=26〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_reviewer_a_audit_tmp.py` P=13／N=26〔同名歧义〕 | 2／13 | 26／26 | 2026-09-15 15:57:20<br>`sub/results/_archive_2026_09_20/_reviewer_a_audit_tmp.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `MC-S5`、`PULLBACK` |
| `2c2cc3ff542a` | 2 | 3,524 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_d05_rescue_2026_09_18.py` P=2／N=24〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_fix_d05_rescue_2026_09_18.py` P=12／N=24〔同名歧义〕 | 2／12 | 24／24 | 2026-09-18 12:41:14<br>`sub/results/_archive_2026_09_20/_fix_d05_rescue_2026_09_18.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `2d9edc8c7303` | 2 | 356,123 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/fiction_that_feeds_back.pdf` P=3／N=91〔同名歧义〕<br>`sub/results/_archive_2026_09_20/fiction_that_feeds_back.pdf` P=58／N=91〔同名歧义〕 | 3／58 | 91／91 | 2026-09-17 22:05:22<br>`sub/results/_archive_2026_09_20/fiction_that_feeds_back.pdf` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `2efcd5ff42f1` | 2 | 8,225 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch4_2026_09_18.py` P=2／N=22〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_fix_batch4_2026_09_18.py` P=12／N=22〔同名歧义〕 | 2／12 | 22／22 | 2026-09-18 13:44:58<br>`sub/results/_archive_2026_09_20/_fix_batch4_2026_09_18.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `2efdc3d7741d` | 2 | 3,624 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_coze_paper_v1_summary_2026_09_17.md` P=2／N=32〔同名歧义〕<br>`sub/results/_coze_paper_v1_summary_2026_09_17.md` P=25／N=32〔同名歧义〕 | 2／25 | 32／32 | 2026-09-18 00:20:40<br>`sub/results/_coze_paper_v1_summary_2026_09_17.md` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `303bf7c6f34d` | 2 | 28,762 | 1 | `repo/results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_s3_d1_rulings_supplement_register_2026_10_01.md` P=6／N=59〔同名歧义〕<br>`sub/results/_s3_d1_rulings_supplement_register_2026_10_01.md` P=41／N=59〔同名歧义〕 | 6／41 | 59／59 | 2026-10-14 14:07:09<br>`sub/results/_s3_d1_rulings_supplement_register_2026_10_01.md` | 是 | 是 | **可减** | — |
| `3184b30b7b0d` | 2 | 4,253 | 1 | `repo/_remote_pullback_2026_10_17/results/_trae_d7_v1_audit_20260917_190000.json` P=2／N=35〔同名歧义〕<br>`sub/results/_archive_2026_09_18/_trae_d7_v1_audit_20260917_190000.json` P=8／N=35〔同名歧义〕 | 2／8 | 35／35 | 2026-09-17 19:14:38<br>`sub/results/_archive_2026_09_18/_trae_d7_v1_audit_20260917_190000.json` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `3596490e1fc0` | 2 | 4,236 | 1 | `repo/_remote_pullback_2026_10_17/results/v20_regression_field_v2.json` P=2／N=55〔同名歧义〕<br>`sub/results/v20_regression_field_v2.json` P=29／N=55〔同名歧义〕 | 2／29 | 55／55 | 2026-08-28 20:45:20<br>`sub/results/v20_regression_field_v2.json` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `35b676773243` | 2 | 7,844 | 1 | `sub/results/_archive_2026_09_21/deposon_v20_gt3.json` P=11／N=94〔同名歧义〕<br>`repo/results/deposon_v20_gt3.json` P=41／N=94〔同名歧义〕 | 11／41 | 94／94 | 2026-08-29 15:03:29<br>`sub/results/_archive_2026_09_21/deposon_v20_gt3.json` | 是 | 是 | **可减** | — |
| `389283c51275` | 2 | 4,261 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch7_2026_09_18.py` P=2／N=22〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_fix_batch7_2026_09_18.py` P=12／N=22〔同名歧义〕 | 2／12 | 22／22 | 2026-09-18 13:47:59<br>`sub/results/_archive_2026_09_20/_fix_batch7_2026_09_18.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `3de722dc9e39` | 2 | 26,990 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_glm_ftfb_deep_revision_2026_09_18.md` P=2／N=41〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_letter_to_glm_ftfb_deep_revision_2026_09_18.md` P=13／N=41〔同名歧义〕 | 2／13 | 41／41 | 2026-09-18 13:45:13<br>`sub/results/_archive_2026_09_20/_letter_to_glm_ftfb_deep_revision_2026_09_18.md` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `416dda94cb63` | 2 | 552 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/SHA256_MANIFEST.txt` P=2／N=32〔同名歧义〕<br>`sub/results/_archive_2026_09_20/SHA256_MANIFEST.txt` P=12／N=32〔同名歧义〕 | 2／12 | 32／32 | 2026-09-17 22:06:32<br>`sub/results/_archive_2026_09_20/SHA256_MANIFEST.txt` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `4181a24c9ca1` | 2 | 277 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_teamorouter_smoke_tmp.json` P=1／N=21〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_teamorouter_smoke_tmp.json` P=13／N=21〔同名歧义〕 | 1／13 | 21／21 | 2026-09-10 16:46:45<br>`sub/results/_archive_2026_09_20/_teamorouter_smoke_tmp.json` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `MC-S5`、`PULLBACK` |
| `41bea33b9492` | 2 | 2,088 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918.log` P=1／N=14〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918.log` P=8／N=14〔同名歧义〕 | 1／8 | 14／14 | 2026-10-12 12:49:03<br>`sub/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918.log` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `4458ccf3d64a` | 2 | 24,113 | 1 | `sub/results/_archive_2026_09_24/_worker_openrouter_rag_run.py` P=28／N=49〔同名歧义〕<br>`sub/results/_worker_openrouter_rag_run.py` P=14／N=49〔同名歧义〕 | 28／14 | 49／49 | 2026-09-16 11:01:12<br>`sub/results/_archive_2026_09_24/_worker_openrouter_rag_run.py` | 是 | 否 | ⛔ 0 减·代码源 | — |
| `4505cca79c15` | 2 | 2,456 | 1 | `repo/results/d7_5anchor_60cells_9model_verdict_2026_09_18.json` P=51／N=94〔同名歧义〕<br>`sub/results/d7_5anchor_60cells_9model_verdict_2026_09_18.json` P=0／N=94〔同名歧义〕 | 51／0 | 94／94 | 2026-09-16 11:00:06<br>`repo/results/d7_5anchor_60cells_9model_verdict_2026_09_18.json` | 是 | 是 | ⛔ 0 减·权威件 | — |
| `463fc7575663` | 2 | 9,663 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/compile_verification.txt` P=2／N=69〔同名歧义〕<br>`sub/results/_archive_2026_09_20/compile_verification.txt` P=12／N=69〔同名歧义〕 | 2／12 | 69／69 | 2026-09-18 13:45:13<br>`sub/results/_archive_2026_09_20/compile_verification.txt` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `483602856618` | 2 | 1,879 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/deposon_team/verifier/v42_v2_baseline_2026_09_16.json` P=2／N=23〔同名歧义〕<br>`sub/deposon_team/verifier/v42_v2_baseline_2026_09_16.json` P=16／N=23〔同名歧义〕 | 2／16 | 23／23 | 2026-09-16 18:25:53<br>`sub/deposon_team/verifier/v42_v2_baseline_2026_09_16.json` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `49dde3059959` | 2 | 1,393 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_doubao_4versions_diff_2026_09_17.json` P=2／N=23〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_probe_doubao_4versions_diff_2026_09_17.json` P=12／N=23〔同名歧义〕 | 2／12 | 23／23 | 2026-09-17 15:51:14<br>`sub/results/_archive_2026_09_20/_probe_doubao_4versions_diff_2026_09_17.json` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `4af67e6cbe71` | 2 | 3,449 | 1 | `repo/_remote_pullback_2026_10_17/results/_trae_anchor_18_audit_20260917_193000.md` P=2／N=37〔同名歧义〕<br>`sub/results/_archive_2026_09_18/_trae_anchor_18_audit_20260917_193000.md` P=9／N=37〔同名歧义〕 | 2／9 | 37／37 | 2026-09-17 19:13:39<br>`sub/results/_archive_2026_09_18/_trae_anchor_18_audit_20260917_193000.md` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `4bdec2683f06` | 2 | 22,105 | 1 | `sub/_archive_deposon_2026_09_17/verifier/audit/conservation.py` P=44／N=232〔同名歧义〕<br>`repo/verifier/audit/conservation.py` P=161／N=232〔同名歧义〕 | 44／161 | 232／232 | 2026-09-10 09:29:22<br>`repo/verifier/audit/conservation.py` | 是 | 是 | ⛔ 0 减·代码源 | — |
| `5057ccf97d6b` | 2 | 2,249 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch8_2026_09_18.py` P=2／N=20〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_fix_batch8_2026_09_18.py` P=12／N=20〔同名歧义〕 | 2／12 | 20／20 | 2026-09-18 13:49:57<br>`sub/results/_archive_2026_09_20/_fix_batch8_2026_09_18.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `543479649b3e` | 2 | 84,388 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/fiction_that_feeds_back_source.md` P=2／N=42〔同名歧义〕<br>`sub/results/_archive_2026_09_20/fiction_that_feeds_back_source.md` P=18／N=42〔同名歧义〕 | 2／18 | 42／42 | 2026-09-17 22:05:22<br>`sub/results/_archive_2026_09_20/fiction_that_feeds_back_source.md` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `55428f6bd848` | 2 | 3,041 | 1 | `repo/results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/deposon_g1_mindmap_demo.json` P=2／N=96〔同名歧义〕<br>`repo/results/deposon_g1_mindmap_demo.json` P=78／N=96〔同名歧义〕 | 2／78 | 96／96 | 2026-08-23 05:00:55<br>`repo/results/deposon_g1_mindmap_demo.json` | 是 | 否 | **可减** | — |
| `5777a07c608a` | 2 | 43,130 | 1 | `repo/results/_d9_e2e_backup_2026_10_13/_s4_heldout_sampling_seedthird_items_2026_10_11.json` P=3／N=118〔同名歧义〕<br>`repo/results/_s4_heldout_sampling_seedthird_items_2026_10_11.json` P=61／N=118〔同名歧义〕 | 3／61 | 118／118 | 2026-10-11 16:03:31<br>`repo/results/_d9_e2e_backup_2026_10_13/_s4_heldout_sampling_seedthird_items_2026_10_11.json` | 是 | 否 | **可减** | — |
| `57f06a426bec` | 2 | 3,011 | 1 | `repo/_remote_pullback_2026_10_17/results/deposon_benchmark_v1_3_labelfree.json` P=2／N=32〔同名歧义〕<br>`sub/results/deposon_benchmark_v1_3_labelfree.json` P=30／N=32〔同名歧义〕 | 2／30 | 32／32 | 2026-08-23 00:30:18<br>`sub/results/deposon_benchmark_v1_3_labelfree.json` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `5a880678c386` | 2 | 1,024 | 1 | `sub/results/attack_pc_a2_fitting_2026_09_15.json` P=22／N=29<br>`repo/results/boss_pc_2_a2_fitting_2026_09_15.json` P=31／N=40 | 22／31 | 29／40 | 2026-09-15 13:34:48<br>`repo/results/boss_pc_2_a2_fitting_2026_09_15.json` | 是 | 是 | **可减** | — |
| `5c76137d6430` | 2 | 7,530 | 1 | `repo/results/boss_pa_2_potential_game_result_2026_09_15.json` P=39／N=59〔同名歧义〕<br>`sub/results/boss_pa_2_potential_game_result_2026_09_15.json` P=0／N=59〔同名歧义〕 | 39／0 | 59／59 | 2026-09-15 15:28:10<br>`repo/results/boss_pa_2_potential_game_result_2026_09_15.json` | 是 | 是 | **可减** | — |
| `5f16be89efc5` | 2 | 938 | 1 | `repo/_remote_pullback_2026_10_17/results/llm_prior_cache.json` P=2／N=72〔同名歧义〕<br>`sub/results/llm_prior_cache.json` P=49／N=72〔同名歧义〕 | 2／49 | 72／72 | 2026-08-23 20:21:35<br>`sub/results/llm_prior_cache.json` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `62fb594be3f9` | 2 | 32,371 | 1 | `repo/results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_t1_substrate_gap_census_2026_10_01.md` P=9／N=55〔同名歧义〕<br>`repo/results/_t1_substrate_gap_census_2026_10_01.md` P=35／N=55〔同名歧义〕 | 9／35 | 55／55 | 2026-10-01 14:40:17<br>`repo/results/_t1_substrate_gap_census_2026_10_01.md` | 是 | 否 | **可减** | — |
| `63eb0a0aa102` | 2 | 2,119 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_sanity_teamo_one.py` P=2／N=18〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_sanity_teamo_one.py` P=12／N=18〔同名歧义〕 | 2／12 | 18／18 | 2026-09-17 15:46:36<br>`sub/results/_archive_2026_09_20/_sanity_teamo_one.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `693eefdd7a82` | 2 | 32,296 | 1 | `repo/results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_kv3s_3_2_terminal_verdict_2026_10_01.md` P=7／N=76〔同名歧义〕<br>`sub/results/_kv3s_3_2_terminal_verdict_2026_10_01.md` P=47／N=76〔同名歧义〕 | 7／47 | 76／76 | 2026-10-14 14:07:09<br>`sub/results/_kv3s_3_2_terminal_verdict_2026_10_01.md` | 是 | 是 | **可减** | — |
| `6952b3b02b96` | 2 | 8,419 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/戴夫_FTFB双审包简报v3_2026-09-17.md` P=2／N=28〔同名歧义〕<br>`sub/results/_archive_2026_09_20/戴夫_FTFB双审包简报v3_2026-09-17.md` P=13／N=28〔同名歧义〕 | 2／13 | 28／28 | 2026-09-17 22:06:25<br>`sub/results/_archive_2026_09_20/戴夫_FTFB双审包简报v3_2026-09-17.md` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `6a2656878745` | 2 | 12,798 | 1 | `repo/corpus/v20/strip_captions_22.json` P=91／N=342〔同名歧义〕<br>`repo/corpus/v20_caption_surface/strip_captions_22.json` P=102／N=342〔同名歧义〕 | 91／102 | 342／342 | 2026-09-11 11:33:40<br>`repo/corpus/v20/strip_captions_22.json` | 是 | 否 | **可减** | — |
| `769ae8c908c9` | 2 | 3,134 | 1 | `repo/_remote_pullback_2026_10_17/results/deposon_benchmark_v1_3_resonant.json` P=2／N=31〔同名歧义〕<br>`sub/results/deposon_benchmark_v1_3_resonant.json` P=29／N=31〔同名歧义〕 | 2／29 | 31／31 | 2026-08-23 00:30:18<br>`sub/results/deposon_benchmark_v1_3_resonant.json` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `784f042bf93d` | 2 | 22,646 | 1 | `repo/results/_d9_e2e_backup_2026_10_13/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` P=6／N=94〔同名歧义〕<br>`repo/results/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` P=53／N=94〔同名歧义〕 | 6／53 | 94／94 | 2026-10-11 16:03:31<br>`repo/results/_d9_e2e_backup_2026_10_13/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | 是 | 否 | ⛔ 0 减·权威件 | — |
| `7a5be4aef9ac` | 2 | 13,694 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_md_report_only_2026_09_18.py` P=2／N=18〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_d05_md_report_only_2026_09_18.py` P=12／N=18〔同名歧义〕 | 2／12 | 18／18 | 2026-09-18 10:16:44<br>`sub/results/_archive_2026_09_20/_d05_md_report_only_2026_09_18.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `7c0d169ef164` | 2 | 512 | 1 | `repo/_remote_pullback_2026_10_17/results/llm_prior_cache_v18_contentless.json` P=2／N=50〔同名歧义〕<br>`sub/results/llm_prior_cache_v18_contentless.json` P=28／N=50〔同名歧义〕 | 2／28 | 50／50 | 2026-08-23 23:17:58<br>`sub/results/llm_prior_cache_v18_contentless.json` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `81bb1751be4c` | 2 | 4,100 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch2_2026_09_18.py` P=2／N=22〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_fix_batch2_2026_09_18.py` P=12／N=22〔同名歧义〕 | 2／12 | 22／22 | 2026-09-18 13:43:14<br>`sub/results/_archive_2026_09_20/_fix_batch2_2026_09_18.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `839fb5452578` | 2 | 16,099 | 1 | `repo/results/_d9_e2e_backup_2026_10_13/_s5doubleprime_five_lines_readings_2026_10_11.json` P=3／N=82〔同名歧义〕<br>`repo/results/_s5doubleprime_five_lines_readings_2026_10_11.json` P=45／N=82〔同名歧义〕 | 3／45 | 82／82 | 2026-10-11 18:14:08<br>`repo/results/_d9_e2e_backup_2026_10_13/_s5doubleprime_five_lines_readings_2026_10_11.json` | 是 | 否 | **可减** | — |
| `888d02cd1443` | 2 | 3,540 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_sanity_teamo_three.py` P=2／N=18〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_sanity_teamo_three.py` P=12／N=18〔同名歧义〕 | 2／12 | 18／18 | 2026-09-17 15:44:19<br>`sub/results/_archive_2026_09_20/_sanity_teamo_three.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `8b6682181392` | 2 | 2,186 | 1 | `repo/_remote_pullback_2026_10_17/results/v19_edges_audit_input.csv` P=2／N=53〔同名歧义〕<br>`sub/results/v19_edges_audit_input.csv` P=29／N=53〔同名歧义〕 | 2／29 | 53／53 | 2026-08-28 15:53:28<br>`sub/results/v19_edges_audit_input.csv` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `8dce6d7618a2` | 2 | 1,925 | 1 | `repo/_remote_pullback_2026_10_17/results/llm_prior_cache_v18_labelshuffle.json` P=2／N=49〔同名歧义〕<br>`sub/results/llm_prior_cache_v18_labelshuffle.json` P=27／N=49〔同名歧义〕 | 2／27 | 49／49 | 2026-08-23 22:56:03<br>`sub/results/llm_prior_cache_v18_labelshuffle.json` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `8ece24be6b8a` | 2 | 3,281 | 1 | `repo/_remote_pullback_2026_10_17/results/_trae_kimi_push_v3_audit_20260917_193000.md` P=2／N=37〔同名歧义〕<br>`sub/results/_archive_2026_09_18/_trae_kimi_push_v3_audit_20260917_193000.md` P=9／N=37〔同名歧义〕 | 2／9 | 37／37 | 2026-09-17 19:12:38<br>`sub/results/_archive_2026_09_18/_trae_kimi_push_v3_audit_20260917_193000.md` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `93527eb7b2f7` | 2 | 2,720 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_doubao_4versions_diff_2026_09_17.py` P=2／N=19〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_probe_doubao_4versions_diff_2026_09_17.py` P=12／N=19〔同名歧义〕 | 2／12 | 19／19 | 2026-09-17 15:50:56<br>`sub/results/_archive_2026_09_20/_probe_doubao_4versions_diff_2026_09_17.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `9bcfe80c0dd0` | 2 | 2,371 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_doubao_emb_direct_2026_09_17.py` P=2／N=19〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_probe_doubao_emb_direct_2026_09_17.py` P=12／N=19〔同名歧义〕 | 2／12 | 19／19 | 2026-09-17 15:48:30<br>`sub/results/_archive_2026_09_20/_probe_doubao_emb_direct_2026_09_17.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `9e1ccbdceacc` | 2 | 25,347 | 1 | `repo/corpus/v20/by_model/minimax/artifact_v_2026_09_16.json` P=63／N=77<br>`sub/deposon_team/products/minimax_artifact_v_2026_09_16.json` P=17／N=20 | 63／17 | 77／20 | 2026-09-16 18:20:56<br>`repo/corpus/v20/by_model/minimax/artifact_v_2026_09_16.json` | 是 | 是 | **可减** | — |
| `a2ae7997ee67` | 2 | 123,331 | 1 | `sub/results/_archive_2026_09_21/deposon_v20_gt2b.json` P=13／N=100〔同名歧义〕<br>`repo/results/deposon_v20_gt2b.json` P=53／N=100〔同名歧义〕 | 13／53 | 100／100 | 2026-08-29 19:57:39<br>`sub/results/_archive_2026_09_21/deposon_v20_gt2b.json` | 是 | 是 | **可减** | — |
| `a3de045b5dd7` | 2 | 2,284 | 1 | `repo/_remote_pullback_2026_10_17/results/deposon_g3_arrhenius.json` P=2／N=31〔同名歧义〕<br>`sub/results/deposon_g3_arrhenius.json` P=29／N=31〔同名歧义〕 | 2／29 | 31／31 | 2026-08-23 05:00:55<br>`sub/results/deposon_g3_arrhenius.json` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `a729875c0c67` | 2 | 4,712 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_archive_manifest_2026_09_18.json` P=2／N=33〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_archive_manifest_2026_09_18.json` P=19／N=33〔同名歧义〕 | 2／19 | 33／33 | 2026-09-18 22:04:18<br>`sub/results/_archive_2026_09_20/_archive_manifest_2026_09_18.json` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `E8`、`PULLBACK` |
| `a7952d9d78db` | 2 | 5,517 | 1 | `repo/_remote_pullback_2026_10_17/results/deposon_v16_llm_prior_summary.json` P=2／N=31〔同名歧义〕<br>`sub/results/deposon_v16_llm_prior_summary.json` P=29／N=31〔同名歧义〕 | 2／29 | 31／31 | 2026-08-23 20:28:34<br>`sub/results/deposon_v16_llm_prior_summary.json` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `a7dff824ed56` | 2 | 22,877 | 1 | `repo/results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_s3_d1fill_recount_2026_10_01.md` P=8／N=52〔同名歧义〕<br>`repo/results/_s3_d1fill_recount_2026_10_01.md` P=37／N=52〔同名歧义〕 | 8／37 | 52／52 | 2026-10-01 13:44:10<br>`repo/results/_s3_d1fill_recount_2026_10_01.md` | 是 | 否 | **可减** | — |
| `a82881653520` | 2 | 465,366 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_coze_online_v4_d7format_2026_09_26.pdf` P=4／N=16<br>`sub/results/_coze_〔IM〕_v4_d7format_2026_09_26.pdf` P=27／N=30 | 4／27 | 16／30 | 2026-09-26 22:50:54<br>`sub/results/_coze_〔IM〕_v4_d7format_2026_09_26.pdf` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `a964defb923d` | 2 | 24,843 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_content_A2_kimik3.md` P=2／N=36〔同名歧义〕<br>`sub/results/_archive_2026_09_20/review_content_A2_kimik3.md` P=14／N=36〔同名歧义〕 | 2／14 | 36／36 | 2026-09-18 09:28:57<br>`sub/results/_archive_2026_09_20/review_content_A2_kimik3.md` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `a9ad1de618f5` | 2 | 1,669 | 1 | `repo/results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json` P=73／N=88〔同名歧义〕<br>`sub/results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json` P=0／N=88〔同名歧义〕 | 73／0 | 88／88 | 2026-09-16 17:39:59<br>`repo/results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json` | 是 | 是 | **可减** | — |
| `adc99e04ac53` | 2 | 454,307 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_coze_online_v3_d7format_2026_09_18.pdf` P=3／N=22<br>`sub/results/_archive_2026_09_20/_coze_〔IM〕_v3_d7format_2026_09_18.pdf` P=11／N=18 | 3／11 | 22／18 | 2026-09-18 21:31:20<br>`sub/results/_archive_2026_09_20/_coze_〔IM〕_v3_d7format_2026_09_18.pdf` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `ae07f5551e87` | 2 | 2,637 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/p_i_curvature_audit_probe_results_2026_09_16.json` P=2／N=23〔同名歧义〕<br>`sub/results/_archive_2026_09_20/p_i_curvature_audit_probe_results_2026_09_16.json` P=12／N=23〔同名歧义〕 | 2／12 | 23／23 | 2026-09-16 17:37:31<br>`sub/results/_archive_2026_09_20/p_i_curvature_audit_probe_results_2026_09_16.json` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `b0e2673f4a56` | 2 | 88,584 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_v41_flash_rag_partial.bak.json` P=2／N=20〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_v41_flash_rag_partial.bak.json` P=13／N=20〔同名歧义〕 | 2／13 | 20／20 | 2026-09-10 17:07:49<br>`sub/results/_archive_2026_09_20/_v41_flash_rag_partial.bak.json` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `MC-S5`、`PULLBACK` |
| `b471190e579c` | 2 | 770 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/deposon_team/verifier/v42_v2_runs_2026_09_16.jsonl` P=3／N=25〔同名歧义〕<br>`sub/deposon_team/verifier/v42_v2_runs_2026_09_16.jsonl` P=17／N=25〔同名歧义〕 | 3／17 | 25／25 | 2026-09-16 18:25:53<br>`sub/deposon_team/verifier/v42_v2_runs_2026_09_16.jsonl` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `b9b65c568842` | 2 | 915 | 1 | `sub/results/_archive_2026_09_21/deposon_v20_vector_audit.json` P=11／N=79〔同名歧义〕<br>`repo/results/deposon_v20_vector_audit.json` P=33／N=79〔同名歧义〕 | 11／33 | 79／79 | 2026-08-28 21:15:08<br>`sub/results/_archive_2026_09_21/deposon_v20_vector_audit.json` | 是 | 是 | ⛔ 0 减·权威件 | — |
| `befdd577adce` | 2 | 1,141 | 1 | `sub/.trae/audit/compile_evidence/extract_tars.py` P=10／N=25〔同名歧义〕<br>`sub/.trae/audit/compile_evidence/v2pre_h1h3_20260909/extract_tars.py` P=10／N=25〔同名歧义〕 | 10／10 | 25／25 | 2026-09-08 22:50:11<br>`sub/.trae/audit/compile_evidence/extract_tars.py` | 是 | 否 | ⛔ 0 减·代码源 | — |
| `c5598b13c139` | 2 | 17,363 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/deposon_team/verifier/v42_v2_2026_09_16.py` P=2／N=22〔同名歧义〕<br>`sub/deposon_team/verifier/v42_v2_2026_09_16.py` P=18／N=22〔同名歧义〕 | 2／18 | 22／22 | 2026-09-16 18:23:39<br>`sub/deposon_team/verifier/v42_v2_2026_09_16.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `c68076c88140` | 2 | 26,253 | 1 | `repo/results/_v5_gt8_lowarm_result_2026_09_29.json` P=24／N=28<br>`sub/results/_v5_gt8_lowarm_result_2026_09_29_cb132cd5.json` P=16／N=17 | 24／16 | 28／17 | 2026-09-29 15:21:52<br>`repo/results/_v5_gt8_lowarm_result_2026_09_29.json` | 是 | 是 | **可减** | — |
| `c7c59e0d2f6c` | 2 | 8,753 | 1 | `repo/results/boss_pa_1_rbr_rm_result_2026_09_15.json` P=167／N=244〔同名歧义〕<br>`sub/results/boss_pa_1_rbr_rm_result_2026_09_15.json` P=0／N=244〔同名歧义〕 | 167／0 | 244／244 | 2026-09-15 15:28:10<br>`repo/results/boss_pa_1_rbr_rm_result_2026_09_15.json` | 是 | 是 | **可减** | — |
| `c9796d3b3263` | 2 | 12,479 | 1 | `repo/_remote_pullback_2026_10_17/results/deposon_benchmark_v1_4_sc5.json` P=2／N=33〔同名歧义〕<br>`sub/results/deposon_benchmark_v1_4_sc5.json` P=29／N=33〔同名歧义〕 | 2／29 | 33／33 | 2026-08-23 15:14:50<br>`sub/results/deposon_benchmark_v1_4_sc5.json` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `ca71aa6858e1` | 2 | 631,644 | 1 | `sub/results/_archive_2026_09_21/deposon_v20_corpus_eval.json` P=11／N=90〔同名歧义〕<br>`repo/results/deposon_v20_corpus_eval.json` P=54／N=90〔同名歧义〕 | 11／54 | 90／90 | 2026-08-29 01:21:14<br>`sub/results/_archive_2026_09_21/deposon_v20_corpus_eval.json` | 是 | 是 | **可减** | — |
| `d2cd7acb29a1` | 2 | 18,596 | 1 | `repo/corpus/v20_caption_surface/_p_d_b3_merkle_22caption_runner_2026_09_16.py` P=38／N=73〔同名歧义〕<br>`sub/deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_09_16.py` P=19／N=73〔同名歧义〕 | 38／19 | 73／73 | 2026-09-16 18:54:48<br>`repo/corpus/v20_caption_surface/_p_d_b3_merkle_22caption_runner_2026_09_16.py` | 是 | 是 | ⛔ 0 减·代码源 | — |
| `d3f72f67977d` | 2 | 639 | 1 | `repo/_remote_pullback_2026_10_17/results/llm_prior_cache_v18_contamination.json` P=2／N=57〔同名歧义〕<br>`sub/results/llm_prior_cache_v18_contamination.json` P=27／N=57〔同名歧义〕 | 2／27 | 57／57 | 2026-08-23 22:56:14<br>`sub/results/llm_prior_cache_v18_contamination.json` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `d6f233d73c45` | 2 | 9,098 | 1 | `repo/results/boss_pa_3_replicator_dynamics_result_2026_09_15.json` P=60／N=76〔同名歧义〕<br>`sub/results/boss_pa_3_replicator_dynamics_result_2026_09_15.json` P=0／N=76〔同名歧义〕 | 60／0 | 76／76 | 2026-09-15 15:28:10<br>`repo/results/boss_pa_3_replicator_dynamics_result_2026_09_15.json` | 是 | 是 | **可减** | — |
| `d74d6b39d1b0` | 2 | 1,265 | 1 | `sub/results/attack_pc_a3_clipping_2026_09_15.json` P=22／N=32<br>`repo/results/boss_pc_3_a3_clipping_2026_09_15.json` P=50／N=65 | 22／50 | 32／65 | 2026-09-15 13:34:48<br>`repo/results/boss_pc_3_a3_clipping_2026_09_15.json` | 是 | 是 | **可减** | — |
| `dc9cb0e02922` | 2 | 28,370 | 1 | `sub/results/_d1_ruling_and_s3_transition_2026_10_01.md` P=94／N=127〔同名歧义〕<br>`repo/results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_d1_ruling_and_s3_transition_2026_10_01.md` P=8／N=127〔同名歧义〕 | 94／8 | 127／127 | 2026-10-10 11:37:23<br>`sub/results/_d1_ruling_and_s3_transition_2026_10_01.md` | 是 | 是 | **可减** | — |
| `dce965058076` | 2 | 2,841 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_teamo_via_proxy.py` P=2／N=18〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_probe_teamo_via_proxy.py` P=12／N=18〔同名歧义〕 | 2／12 | 18／18 | 2026-09-17 15:42:29<br>`sub/results/_archive_2026_09_20/_probe_teamo_via_proxy.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `dfbcc5d6fc34` | 2 | 13,775 | 1 | `repo/corpus/v20_caption_surface/_p_d_v03_22caption_verification_20260917_163757.json` P=21／N=49〔同名歧义〕<br>`sub/results/_p_d_v03_22caption_verification_20260917_163757.json` P=23／N=49〔同名歧义〕 | 21／23 | 49／49 | 2026-09-17 16:37:57<br>`repo/corpus/v20_caption_surface/_p_d_v03_22caption_verification_20260917_163757.json` | 是 | 是 | **可减** | — |
| `dfe014c627ca` | 2 | 988 | 1 | `repo/_remote_pullback_2026_10_17/results/v20_statcheck_fm_vs_deg.json` P=2／N=34〔同名歧义〕<br>`sub/results/v20_statcheck_fm_vs_deg.json` P=28／N=34〔同名歧义〕 | 2／28 | 34／34 | 2026-08-28 20:44:25<br>`sub/results/v20_statcheck_fm_vs_deg.json` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `e05555deb611` | 2 | 12,919 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_i_curvature_audit_probe_runner_2026_09_16.py` P=2／N=24〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_p_i_curvature_audit_probe_runner_2026_09_16.py` P=12／N=24〔同名歧义〕 | 2／12 | 24／24 | 2026-09-16 20:57:28<br>`sub/results/_archive_2026_09_20/_p_i_curvature_audit_probe_runner_2026_09_16.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `e11319f32dc5` | 2 | 2,187 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_sanity_openai_more.py` P=2／N=18〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_sanity_openai_more.py` P=12／N=18〔同名歧义〕 | 2／12 | 18／18 | 2026-09-17 15:47:48<br>`sub/results/_archive_2026_09_20/_sanity_openai_more.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `e3b0c44298fc` | 2 | 0 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/gpt6_30cells_run.log.err` P=2／N=19<br>`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/volcengine_glm_latest_30cells_v2_run_2026_09_10.log.err` P=2／N=19 | 2／2 | 19／19 | 2026-10-17 15:55:05<br>`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/gpt6_30cells_run.log.err` | 是 | 否 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `ef5a40554960` | 2 | 46,836 | 1 | `repo/results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_v3_s_prereg_v1_2026_09_27.md` P=8／N=272〔同名歧义〕<br>`repo/results/_v3_s_prereg_v1_2026_09_27.md` P=208／N=272〔同名歧义〕 | 8／208 | 272／272 | 2026-09-27 15:28:46<br>`repo/results/_v3_s_prereg_v1_2026_09_27.md` | 是 | 否 | **可减** | — |
| `efe05ad775de` | 2 | 24,150 | 1 | `repo/corpus/v20/by_model/kimi/index_v2_2026_09_16.json` P=57／N=217〔同名歧义〕<br>`repo/corpus/v20/index_v2_2026_09_16.json` P=84／N=217〔同名歧义〕 | 57／84 | 217／217 | 2026-09-16 18:39:54<br>`repo/corpus/v20/by_model/kimi/index_v2_2026_09_16.json` | 是 | 否 | **可减** | — |
| `f2818fc2ddff` | 2 | 2,589 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_doubao_emb_via_proxy_2026_09_17.py` P=2／N=20〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_probe_doubao_emb_via_proxy_2026_09_17.py` P=12／N=20〔同名歧义〕 | 2／12 | 20／20 | 2026-09-17 15:48:59<br>`sub/results/_archive_2026_09_20/_probe_doubao_emb_via_proxy_2026_09_17.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `f2934e5279e6` | 2 | 9,717 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_mavis_full_mirror_request_2026_09_17.md` P=2／N=28〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_letter_to_mavis_full_mirror_request_2026_09_17.md` P=14／N=28〔同名歧义〕 | 2／14 | 28／28 | 2026-09-17 23:06:49<br>`sub/results/_archive_2026_09_20/_letter_to_mavis_full_mirror_request_2026_09_17.md` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `f2a655cd5e54` | 2 | 3,467 | 1 | `repo/_remote_pullback_2026_10_17/results/_trae_corpus_5_audit_20260917_193000.md` P=2／N=37〔同名歧义〕<br>`sub/results/_archive_2026_09_18/_trae_corpus_5_audit_20260917_193000.md` P=9／N=37〔同名歧义〕 | 2／9 | 37／37 | 2026-09-17 19:13:14<br>`sub/results/_archive_2026_09_18/_trae_corpus_5_audit_20260917_193000.md` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `f3d4ec483599` | 2 | 41,446 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_main_runner_2026_09_18.py` P=2／N=18〔同名歧义〕<br>`sub/results/_archive_2026_09_20/_d05_main_runner_2026_09_18.py` P=12／N=18〔同名歧义〕 | 2／12 | 18／18 | 2026-09-18 10:07:57<br>`sub/results/_archive_2026_09_20/_d05_main_runner_2026_09_18.py` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `f95f382ace44` | 2 | 2,151 | 1 | `repo/_remote_pullback_2026_10_17/results/v20_graph_features.csv` P=2／N=67〔同名歧义〕<br>`sub/results/v20_graph_features.csv` P=39／N=67〔同名歧义〕 | 2／39 | 67／67 | 2026-08-28 20:43:58<br>`sub/results/v20_graph_features.csv` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `fd38a2a1ea05` | 2 | 7,617 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_content_A1_glm51.md` P=2／N=23〔同名歧义〕<br>`sub/results/_archive_2026_09_20/review_content_A1_glm51.md` P=13／N=23〔同名歧义〕 | 2／13 | 23／23 | 2026-09-18 00:35:54<br>`sub/results/_archive_2026_09_20/review_content_A1_glm51.md` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |
| `fe80bad08eef` | 2 | 13,726 | 1 | `repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_tech_B2_grok46.md` P=2／N=27〔同名歧义〕<br>`sub/results/_archive_2026_09_20/review_tech_B2_grok46.md` P=16／N=27〔同名歧义〕 | 2／16 | 27／27 | 2026-09-18 00:35:54<br>`sub/results/_archive_2026_09_20/review_tech_B2_grok46.md` | 是 | 是 | ⛔ 0 减·**禁令锁定** | `PULLBACK` |

**合计**：**110 组／229 件／冗余 119 件**（其中可减 30 组／35 件；⛔ 0 减 11 组／13 件）。

---

## §4 逐组可减性判定（本单之核心）

**判定规则（先说清，再逐组套用）**：

| 序 | 问 | 规则 |
|---:|---|---|
| 1 | 真重复否？ | 全字节 SHA-256 相同＝是（**实测**，非推断）。反例检查三项：**0 字节空件**／**刻意对照族名**（`baseline`／`对照`／`control`／`origin`／`keep_`／`sample_`／`_copy`／`副本`）／**被代码以写入语义产出**（`write_refs`）——三者任一成立即标「语义不同」 |
| 2 | 含唯一生成器／代码源否？ | 成员扩展名 ∈ {`.py`,`.ps1`,`.sh`,`.bat`,`.cmd`,`.ipynb`} 者为**代码源**（读数件之生成器）；此类组**⛔ 0 减**（删之即失可复算性） |
| 3 | 含权威件否？ | 成员落于 `pi_rulings\`／`results\` 根层之判定·登记族名（`register`／`verdict`／`ruling`／`ledger`／`manifest`／`index`／`audit`／`closure`／`closeout`／`signoff`／`effect`／`receipt`）／仓根 `_pi_` 族名者⇒**⛔ 0 减** |
| 4 | 若减，留哪一件？ | **留件规则（确定性）**：①组含权威件则留该件；②否则留**活引用最多**者（路径式＋裸名式之**他件数**合计）；③并列则**留 repo 侧**（权威链锚于主仓）；④并列则留**路径最浅**者；⑤并列则留 **mtime 最早**者；⑥仍并列则留**件名字典序最小**者 |
| 5 | 减后须登记什么？ | 每删一件登记 **1 条「旧路径→新路径」** ＋ 其**路径式活引用处数**条逐处登记（裸名式引用按件名仍可寻，**不断链**，故不计） |

---

### §4-1 `0a1e91d6f772`（n=3·单件 2,292 B·冗余 2）

1. **真重复否**：**是**——全字节 SHA-256 相同（`0a1e91d6f772`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json`→`E4-key`、`PULLBACK`；`repo/_remote_pullback_2026_10_17/results/_d05_sanity_3backbone_20260918_100110.json`→`E4-key`、`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-2 `1fc5f3ab3f93`（n=3·单件 2,022 B·冗余 2）

1. **真重复否**：**是**——全字节 SHA-256 相同（`1fc5f3ab3f93`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`sub/.trae/audit/compile_evidence/compile_runner.ps1`、`sub/.trae/audit/compile_evidence/v2_overfull_fix_20260909/compile_runner.ps1`、`sub/.trae/audit/compile_evidence/v2pre_h1h3_20260909/compile_runner.ps1` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `sub/.trae/audit/compile_evidence/compile_runner.ps1`**（依留件规则 ②：他件引用 25 件（路径式 11／裸名式 71））。**删**：`sub/.trae/audit/compile_evidence/v2_overfull_fix_20260909/compile_runner.ps1`（sub·路径式活引用 11·同名歧义）、`sub/.trae/audit/compile_evidence/v2pre_h1h3_20260909/compile_runner.ps1`（sub·路径式活引用 11·同名歧义）。
5. **减后须登记**：**24 条**（2 件自身「旧路径→新路径」＋ 路径式活引用 22 处逐处登记）。

### §4-3 `25f745609658`（n=3·单件 612,511 B·冗余 2）

1. **真重复否**：**是**——全字节 SHA-256 相同（`25f745609658`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_v41_flash_rag_caption_embs.bak.json`→`PULLBACK`、`MC-S5`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-4 `43d9ce160fc8`（n=3·单件 2,460 B·冗余 2）

1. **真重复否**：**是**——全字节 SHA-256 相同（`43d9ce160fc8`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/boss_pc_1_real_2d_ising_2026_09_15.json`**（依留件规则 ②：他件引用 57 件（路径式 35／裸名式 46）；规则 ③ repo 侧优先）。**删**：`sub/results/boss_pc_1_real_2d_ising_2026_09_15.json`（sub·路径式活引用 0·同名歧义）、`repo/results/boss_pe_1_real_2d_ising_2026_09_15.json`（repo·路径式活引用 35）。
5. **减后须登记**：**37 条**（2 件自身「旧路径→新路径」＋ 路径式活引用 35 处逐处登记）。

### §4-5 `6cbb8ba01bfb`（n=3·单件 15,409 B·冗余 2）

1. **真重复否**：**是**——全字节 SHA-256 相同（`6cbb8ba01bfb`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/_s4_heldout_sampling_seedprime_items_2026_10_10.json`**（依留件规则 ②：他件引用 83 件（路径式 54／裸名式 120））。**删**：`repo/results/_d9_e2e_backup_2026_10_13/_s4_heldout_sampling_seedprime_items_2026_10_10.json`（repo·路径式活引用 3·同名歧义）、`repo/results/_d9_e2e_rerun_backup_2026_10_13/_s4_heldout_sampling_seedprime_items_2026_10_10.json`（repo·路径式活引用 1·同名歧义）。
5. **减后须登记**：**6 条**（2 件自身「旧路径→新路径」＋ 路径式活引用 4 处逐处登记）。

### §4-6 `8933d61b180a`（n=3·单件 3,553 B·冗余 2）

1. **真重复否**：**是**——全字节 SHA-256 相同（`8933d61b180a`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/boss_pe_2_real_transverse_ising_2026_09_15.json`**（依留件规则 ②：他件引用 73 件（路径式 51／裸名式 68）；规则 ③ repo 侧优先）。**删**：`repo/results/boss_pc_2_real_transverse_ising_2026_09_15.json`（repo·路径式活引用 39·同名歧义）、`sub/results/boss_pc_2_real_transverse_ising_2026_09_15.json`（sub·路径式活引用 0·同名歧义）。
5. **减后须登记**：**41 条**（2 件自身「旧路径→新路径」＋ 路径式活引用 39 处逐处登记）。

### §4-7 `94b5398be76c`（n=3·单件 2,364 B·冗余 2）

1. **真重复否**：**是**——全字节 SHA-256 相同（`94b5398be76c`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/boss_pc_3_real_reservoir_2026_09_15.json`**（依留件规则 ②：他件引用 53 件（路径式 33／裸名式 44）；规则 ③ repo 侧优先）。**删**：`sub/results/boss_pc_3_real_reservoir_2026_09_15.json`（sub·路径式活引用 0·同名歧义）、`repo/results/boss_pe_3_real_reservoir_2026_09_15.json`（repo·路径式活引用 32）。
5. **减后须登记**：**34 条**（2 件自身「旧路径→新路径」＋ 路径式活引用 32 处逐处登记）。

### §4-8 `d21912a05d79`（n=3·单件 1,017 B·冗余 2）

1. **真重复否**：**是**——全字节 SHA-256 相同（`d21912a05d79`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/boss_pc_1_a1_resampling_2026_09_15.json`**（依留件规则 ②：他件引用 45 件（路径式 30／裸名式 42）；规则 ③ repo 侧优先）。**删**：`sub/results/attack_pc_a1_resampling_2026_09_15.json`（sub·路径式活引用 22）、`sub/results/boss_pc_1_a1_resampling_2026_09_15.json`（sub·路径式活引用 0·同名歧义）。
5. **减后须登记**：**24 条**（2 件自身「旧路径→新路径」＋ 路径式活引用 22 处逐处登记）。

### §4-9 `dfb02ade1474`（n=3·单件 591 B·冗余 2）

1. **真重复否**：**是**——全字节 SHA-256 相同（`dfb02ade1474`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/corpus/v20_caption_surface/_inspect_captions.py`、`sub/results/_archive_2026_09_24/_inspect_captions.py`、`sub/results/_inspect_captions.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/corpus/v20_caption_surface/_inspect_captions.py`**（依留件规则 ②：他件引用 57 件（路径式 30／裸名式 86）；规则 ③ repo 侧优先）。**删**：`sub/results/_archive_2026_09_24/_inspect_captions.py`（sub·路径式活引用 31·同名歧义）、`sub/results/_inspect_captions.py`（sub·路径式活引用 13·同名歧义）。
5. **减后须登记**：**46 条**（2 件自身「旧路径→新路径」＋ 路径式活引用 44 处逐处登记）。

### §4-10 `01e63e488ce2`（n=2·单件 3,207 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`01e63e488ce2`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch3_2026_09_18.py`、`sub/results/_archive_2026_09_20/_fix_batch3_2026_09_18.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch3_2026_09_18.py`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-11 `023f936f80fb`（n=2·单件 2,168 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`023f936f80fb`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/results/llm_prior_cache_v18_direction.json`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-12 `048ebc99177c`（n=2·单件 1,029 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`048ebc99177c`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_tmp_inspect_5model.py`、`sub/results/_archive_2026_09_20/_tmp_inspect_5model.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_tmp_inspect_5model.py`→`PULLBACK`、`MC-S5`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-13 `0769f60a0504`（n=2·单件 2,678 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`0769f60a0504`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_final_sha_2026_09_18.py`、`sub/results/_archive_2026_09_20/_final_sha_2026_09_18.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_final_sha_2026_09_18.py`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-14 `079108c62a82`（n=2·单件 21,049 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`079108c62a82`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/_stage3_trigger_readings_items_2026_10_11.json`**（依留件规则 ②：他件引用 55 件（路径式 36／裸名式 75））。**删**：`repo/results/_d9_e2e_backup_2026_10_13/_stage3_trigger_readings_items_2026_10_11.json`（repo·路径式活引用 4·同名歧义）。
5. **减后须登记**：**5 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 4 处逐处登记）。

### §4-15 `0b7e50a8a036`（n=2·单件 2,938 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`0b7e50a8a036`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_verify_sha_2026_09_18.py`、`sub/results/_archive_2026_09_20/_d05_verify_sha_2026_09_18.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_verify_sha_2026_09_18.py`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-16 `0c9addf4a70f`（n=2·单件 675 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`0c9addf4a70f`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_tmp_inspect_22cap.py`、`sub/results/_archive_2026_09_20/_tmp_inspect_22cap.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_tmp_inspect_22cap.py`→`PULLBACK`、`MC-S5`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-17 `0d36d7cd0589`（n=2·单件 30,494 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`0d36d7cd0589`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_tech_B1_dsv4pro.md`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-18 `15904ecae629`（n=2·单件 11,105 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`15904ecae629`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/results/_archive_2026_09_24/_volc_22cap_emb.py`、`sub/results/_volc_22cap_emb.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/_archive_2026_09_24/_volc_22cap_emb.py`**（依留件规则 ②：他件引用 60 件（路径式 29／裸名式 58）；规则 ③ repo 侧优先）。**删**：`sub/results/_volc_22cap_emb.py`（sub·路径式活引用 14·同名歧义）。
5. **减后须登记**：**15 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 14 处逐处登记）。

### §4-19 `18984b04c45e`（n=2·单件 34,134 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`18984b04c45e`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_deposon_v2scripts_reverify_worker_2026_09_18.py`、`sub/results/_archive_2026_09_20/_deposon_v2scripts_reverify_worker_2026_09_18.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_deposon_v2scripts_reverify_worker_2026_09_18.py`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-20 `1c59e7b803fe`（n=2·单件 2,214 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`1c59e7b803fe`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch6_2026_09_18.py`、`sub/results/_archive_2026_09_20/_fix_batch6_2026_09_18.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch6_2026_09_18.py`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-21 `1dadfaeb2c43`（n=2·单件 868 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`1dadfaeb2c43`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/results/v20_statcheck_fm_vs_rand.json`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-22 `218ef1a99f97`（n=2·单件 11,703 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`218ef1a99f97`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/results/deposon_volcengine_minimax_m3_30cells_2026_09_10.py`、`sub/results/deposon_volcengine_minimax_m3_30cells_2026_09_10.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/deposon_volcengine_minimax_m3_30cells_2026_09_10.py`**（依留件规则 ②：他件引用 44 件（路径式 26／裸名式 41）；规则 ③ repo 侧优先）。**删**：`sub/results/deposon_volcengine_minimax_m3_30cells_2026_09_10.py`（sub·路径式活引用 0·同名歧义）。
5. **减后须登记**：**1 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 0 处逐处登记）。

### §4-23 `25141de92c50`（n=2·单件 7,188 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`25141de92c50`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/_xiang14_third_reissue_registration_2026_10_13.md`**（依留件规则 ②：他件引用 44 件（路径式 69／裸名式 89）；规则 ③ repo 侧优先）。**删**：`sub/results/_xiang14_third_reissue_registration_2026_10_13.md`（sub·路径式活引用 0·同名歧义）。
5. **减后须登记**：**1 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 0 处逐处登记）。

### §4-24 `264f2bf5a3f2`（n=2·单件 6,687 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`264f2bf5a3f2`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_temp_volc_test.py`、`sub/results/_archive_2026_09_20/_temp_volc_test.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_temp_volc_test.py`→`PULLBACK`、`MC-S5`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-25 `268225ccbb76`（n=2·单件 4,397 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`268225ccbb76`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_reviewer_a_audit_tmp.py`、`sub/results/_archive_2026_09_20/_reviewer_a_audit_tmp.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_reviewer_a_audit_tmp.py`→`PULLBACK`、`MC-S5`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-26 `2c2cc3ff542a`（n=2·单件 3,524 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`2c2cc3ff542a`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_d05_rescue_2026_09_18.py`、`sub/results/_archive_2026_09_20/_fix_d05_rescue_2026_09_18.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_d05_rescue_2026_09_18.py`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-27 `2d9edc8c7303`（n=2·单件 356,123 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`2d9edc8c7303`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/fiction_that_feeds_back.pdf`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-28 `2efcd5ff42f1`（n=2·单件 8,225 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`2efcd5ff42f1`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch4_2026_09_18.py`、`sub/results/_archive_2026_09_20/_fix_batch4_2026_09_18.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch4_2026_09_18.py`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-29 `2efdc3d7741d`（n=2·单件 3,624 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`2efdc3d7741d`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_coze_paper_v1_summary_2026_09_17.md`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-30 `303bf7c6f34d`（n=2·单件 28,762 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`303bf7c6f34d`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `sub/results/_s3_d1_rulings_supplement_register_2026_10_01.md`**（依留件规则 ②：他件引用 69 件（路径式 41／裸名式 59））。**删**：`repo/results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_s3_d1_rulings_supplement_register_2026_10_01.md`（repo·路径式活引用 6·同名歧义）。
5. **减后须登记**：**7 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 6 处逐处登记）。

### §4-31 `3184b30b7b0d`（n=2·单件 4,253 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`3184b30b7b0d`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/results/_trae_d7_v1_audit_20260917_190000.json`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-32 `3596490e1fc0`（n=2·单件 4,236 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`3596490e1fc0`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/results/v20_regression_field_v2.json`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-33 `35b676773243`（n=2·单件 7,844 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`35b676773243`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/deposon_v20_gt3.json`**（依留件规则 ②：他件引用 74 件（路径式 41／裸名式 94）；规则 ③ repo 侧优先）。**删**：`sub/results/_archive_2026_09_21/deposon_v20_gt3.json`（sub·路径式活引用 11·同名歧义）。
5. **减后须登记**：**12 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 11 处逐处登记）。

### §4-34 `389283c51275`（n=2·单件 4,261 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`389283c51275`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch7_2026_09_18.py`、`sub/results/_archive_2026_09_20/_fix_batch7_2026_09_18.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch7_2026_09_18.py`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-35 `3de722dc9e39`（n=2·单件 26,990 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`3de722dc9e39`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_glm_ftfb_deep_revision_2026_09_18.md`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-36 `416dda94cb63`（n=2·单件 552 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`416dda94cb63`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/SHA256_MANIFEST.txt`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-37 `4181a24c9ca1`（n=2·单件 277 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`4181a24c9ca1`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_teamorouter_smoke_tmp.json`→`PULLBACK`、`MC-S5`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-38 `41bea33b9492`（n=2·单件 2,088 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`41bea33b9492`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918.log`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-39 `4458ccf3d64a`（n=2·单件 24,113 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`4458ccf3d64a`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`sub/results/_archive_2026_09_24/_worker_openrouter_rag_run.py`、`sub/results/_worker_openrouter_rag_run.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `sub/results/_archive_2026_09_24/_worker_openrouter_rag_run.py`**（依留件规则 ②：他件引用 51 件（路径式 28／裸名式 49））。**删**：`sub/results/_worker_openrouter_rag_run.py`（sub·路径式活引用 14·同名歧义）。
5. **减后须登记**：**15 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 14 处逐处登记）。

### §4-40 `4505cca79c15`（n=2·单件 2,456 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`4505cca79c15`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：**是**——`repo/results/d7_5anchor_60cells_9model_verdict_2026_09_18.json`（results/ 根层·判定/登记族名） ⇒ **⛔ 0 减**
4. **若减，留哪一件**：**留 `repo/results/d7_5anchor_60cells_9model_verdict_2026_09_18.json`**（依留件规则 ②：他件引用 88 件（路径式 51／裸名式 94）；规则 ③ repo 侧优先）。**删**：`sub/results/d7_5anchor_60cells_9model_verdict_2026_09_18.json`（sub·路径式活引用 0·同名歧义）。
5. **减后须登记**：**1 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 0 处逐处登记）。

### §4-41 `463fc7575663`（n=2·单件 9,663 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`463fc7575663`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/compile_verification.txt`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-42 `483602856618`（n=2·单件 1,879 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`483602856618`）；**反例命中**：`repo/_remote_pullback_2026_10_17/_september_workspace/deposon_team/verifier/v42_v2_baseline_2026_09_16.json`（刻意对照族名）、`sub/deposon_team/verifier/v42_v2_baseline_2026_09_16.json`（刻意对照族名）。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/deposon_team/verifier/v42_v2_baseline_2026_09_16.json`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-43 `49dde3059959`（n=2·单件 1,393 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`49dde3059959`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_doubao_4versions_diff_2026_09_17.json`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-44 `4af67e6cbe71`（n=2·单件 3,449 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`4af67e6cbe71`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/results/_trae_anchor_18_audit_20260917_193000.md`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-45 `4bdec2683f06`（n=2·单件 22,105 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`4bdec2683f06`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`sub/_archive_deposon_2026_09_17/verifier/audit/conservation.py`、`repo/verifier/audit/conservation.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/verifier/audit/conservation.py`**（依留件规则 ②：他件引用 163 件（路径式 161／裸名式 232）；规则 ③ repo 侧优先）。**删**：`sub/_archive_deposon_2026_09_17/verifier/audit/conservation.py`（sub·路径式活引用 44·同名歧义）。
5. **减后须登记**：**45 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 44 处逐处登记）。

### §4-46 `5057ccf97d6b`（n=2·单件 2,249 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`5057ccf97d6b`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch8_2026_09_18.py`、`sub/results/_archive_2026_09_20/_fix_batch8_2026_09_18.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch8_2026_09_18.py`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-47 `543479649b3e`（n=2·单件 84,388 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`543479649b3e`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/fiction_that_feeds_back_source.md`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-48 `55428f6bd848`（n=2·单件 3,041 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`55428f6bd848`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/deposon_g1_mindmap_demo.json`**（依留件规则 ②：他件引用 93 件（路径式 78／裸名式 96））。**删**：`repo/results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/deposon_g1_mindmap_demo.json`（repo·路径式活引用 2·同名歧义）。
5. **减后须登记**：**3 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 2 处逐处登记）。

### §4-49 `5777a07c608a`（n=2·单件 43,130 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`5777a07c608a`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/_s4_heldout_sampling_seedthird_items_2026_10_11.json`**（依留件规则 ②：他件引用 87 件（路径式 61／裸名式 118））。**删**：`repo/results/_d9_e2e_backup_2026_10_13/_s4_heldout_sampling_seedthird_items_2026_10_11.json`（repo·路径式活引用 3·同名歧义）。
5. **减后须登记**：**4 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 3 处逐处登记）。

### §4-50 `57f06a426bec`（n=2·单件 3,011 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`57f06a426bec`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/results/deposon_benchmark_v1_3_labelfree.json`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-51 `5a880678c386`（n=2·单件 1,024 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`5a880678c386`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/boss_pc_2_a2_fitting_2026_09_15.json`**（依留件规则 ②：他件引用 44 件（路径式 31／裸名式 40）；规则 ③ repo 侧优先）。**删**：`sub/results/attack_pc_a2_fitting_2026_09_15.json`（sub·路径式活引用 22）。
5. **减后须登记**：**23 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 22 处逐处登记）。

### §4-52 `5c76137d6430`（n=2·单件 7,530 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`5c76137d6430`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/boss_pa_2_potential_game_result_2026_09_15.json`**（依留件规则 ②：他件引用 66 件（路径式 39／裸名式 59）；规则 ③ repo 侧优先）。**删**：`sub/results/boss_pa_2_potential_game_result_2026_09_15.json`（sub·路径式活引用 0·同名歧义）。
5. **减后须登记**：**1 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 0 处逐处登记）。

### §4-53 `5f16be89efc5`（n=2·单件 938 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`5f16be89efc5`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/results/llm_prior_cache.json`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-54 `62fb594be3f9`（n=2·单件 32,371 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`62fb594be3f9`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/_t1_substrate_gap_census_2026_10_01.md`**（依留件规则 ②：他件引用 51 件（路径式 35／裸名式 55））。**删**：`repo/results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_t1_substrate_gap_census_2026_10_01.md`（repo·路径式活引用 9·同名歧义）。
5. **减后须登记**：**10 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 9 处逐处登记）。

### §4-55 `63eb0a0aa102`（n=2·单件 2,119 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`63eb0a0aa102`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_sanity_teamo_one.py`、`sub/results/_archive_2026_09_20/_sanity_teamo_one.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_sanity_teamo_one.py`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-56 `693eefdd7a82`（n=2·单件 32,296 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`693eefdd7a82`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `sub/results/_kv3s_3_2_terminal_verdict_2026_10_01.md`**（依留件规则 ②：他件引用 82 件（路径式 47／裸名式 76））。**删**：`repo/results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_kv3s_3_2_terminal_verdict_2026_10_01.md`（repo·路径式活引用 7·同名歧义）。
5. **减后须登记**：**8 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 7 处逐处登记）。

### §4-57 `6952b3b02b96`（n=2·单件 8,419 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`6952b3b02b96`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/戴夫_FTFB双审包简报v3_2026-09-17.md`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-58 `6a2656878745`（n=2·单件 12,798 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`6a2656878745`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/corpus/v20_caption_surface/strip_captions_22.json`**（依留件规则 ②：他件引用 303 件（路径式 102／裸名式 342））。**删**：`repo/corpus/v20/strip_captions_22.json`（repo·路径式活引用 91·同名歧义）。
5. **减后须登记**：**92 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 91 处逐处登记）。

### §4-59 `769ae8c908c9`（n=2·单件 3,134 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`769ae8c908c9`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/results/deposon_benchmark_v1_3_resonant.json`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-60 `784f042bf93d`（n=2·单件 22,646 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`784f042bf93d`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：**是**——`repo/results/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md`（results/ 根层·判定/登记族名） ⇒ **⛔ 0 减**
4. **若减，留哪一件**：**留 `repo/results/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md`**（依留件规则 ②：他件引用 100 件（路径式 53／裸名式 94））。**删**：`repo/results/_d9_e2e_backup_2026_10_13/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md`（repo·路径式活引用 6·同名歧义）。
5. **减后须登记**：**7 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 6 处逐处登记）。

### §4-61 `7a5be4aef9ac`（n=2·单件 13,694 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`7a5be4aef9ac`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_md_report_only_2026_09_18.py`、`sub/results/_archive_2026_09_20/_d05_md_report_only_2026_09_18.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_md_report_only_2026_09_18.py`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-62 `7c0d169ef164`（n=2·单件 512 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`7c0d169ef164`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/results/llm_prior_cache_v18_contentless.json`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-63 `81bb1751be4c`（n=2·单件 4,100 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`81bb1751be4c`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch2_2026_09_18.py`、`sub/results/_archive_2026_09_20/_fix_batch2_2026_09_18.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch2_2026_09_18.py`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-64 `839fb5452578`（n=2·单件 16,099 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`839fb5452578`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/_s5doubleprime_five_lines_readings_2026_10_11.json`**（依留件规则 ②：他件引用 67 件（路径式 45／裸名式 82））。**删**：`repo/results/_d9_e2e_backup_2026_10_13/_s5doubleprime_five_lines_readings_2026_10_11.json`（repo·路径式活引用 3·同名歧义）。
5. **减后须登记**：**4 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 3 处逐处登记）。

### §4-65 `888d02cd1443`（n=2·单件 3,540 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`888d02cd1443`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_sanity_teamo_three.py`、`sub/results/_archive_2026_09_20/_sanity_teamo_three.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_sanity_teamo_three.py`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-66 `8b6682181392`（n=2·单件 2,186 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`8b6682181392`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/results/v19_edges_audit_input.csv`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-67 `8dce6d7618a2`（n=2·单件 1,925 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`8dce6d7618a2`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/results/llm_prior_cache_v18_labelshuffle.json`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-68 `8ece24be6b8a`（n=2·单件 3,281 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`8ece24be6b8a`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/results/_trae_kimi_push_v3_audit_20260917_193000.md`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-69 `93527eb7b2f7`（n=2·单件 2,720 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`93527eb7b2f7`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_doubao_4versions_diff_2026_09_17.py`、`sub/results/_archive_2026_09_20/_probe_doubao_4versions_diff_2026_09_17.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_doubao_4versions_diff_2026_09_17.py`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-70 `9bcfe80c0dd0`（n=2·单件 2,371 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`9bcfe80c0dd0`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_doubao_emb_direct_2026_09_17.py`、`sub/results/_archive_2026_09_20/_probe_doubao_emb_direct_2026_09_17.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_doubao_emb_direct_2026_09_17.py`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-71 `9e1ccbdceacc`（n=2·单件 25,347 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`9e1ccbdceacc`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/corpus/v20/by_model/minimax/artifact_v_2026_09_16.json`**（依留件规则 ②：他件引用 120 件（路径式 63／裸名式 77）；规则 ③ repo 侧优先）。**删**：`sub/deposon_team/products/minimax_artifact_v_2026_09_16.json`（sub·路径式活引用 17）。
5. **减后须登记**：**18 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 17 处逐处登记）。

### §4-72 `a2ae7997ee67`（n=2·单件 123,331 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`a2ae7997ee67`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/deposon_v20_gt2b.json`**（依留件规则 ②：他件引用 95 件（路径式 53／裸名式 100）；规则 ③ repo 侧优先）。**删**：`sub/results/_archive_2026_09_21/deposon_v20_gt2b.json`（sub·路径式活引用 13·同名歧义）。
5. **减后须登记**：**14 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 13 处逐处登记）。

### §4-73 `a3de045b5dd7`（n=2·单件 2,284 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`a3de045b5dd7`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/results/deposon_g3_arrhenius.json`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-74 `a729875c0c67`（n=2·单件 4,712 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`a729875c0c67`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_archive_manifest_2026_09_18.json`→`E8`、`PULLBACK`；`sub/results/_archive_2026_09_20/_archive_manifest_2026_09_18.json`→`E8`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-75 `a7952d9d78db`（n=2·单件 5,517 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`a7952d9d78db`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/results/deposon_v16_llm_prior_summary.json`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-76 `a7dff824ed56`（n=2·单件 22,877 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`a7dff824ed56`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/_s3_d1fill_recount_2026_10_01.md`**（依留件规则 ②：他件引用 54 件（路径式 37／裸名式 52））。**删**：`repo/results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_s3_d1fill_recount_2026_10_01.md`（repo·路径式活引用 8·同名歧义）。
5. **减后须登记**：**9 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 8 处逐处登记）。

### §4-77 `a82881653520`（n=2·单件 465,366 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`a82881653520`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_coze_online_v4_d7format_2026_09_26.pdf`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-78 `a964defb923d`（n=2·单件 24,843 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`a964defb923d`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_content_A2_kimik3.md`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-79 `a9ad1de618f5`（n=2·单件 1,669 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`a9ad1de618f5`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json`**（依留件规则 ②：他件引用 106 件（路径式 73／裸名式 88）；规则 ③ repo 侧优先）。**删**：`sub/results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json`（sub·路径式活引用 0·同名歧义）。
5. **减后须登记**：**1 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 0 处逐处登记）。

### §4-80 `adc99e04ac53`（n=2·单件 454,307 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`adc99e04ac53`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_coze_online_v3_d7format_2026_09_18.pdf`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-81 `ae07f5551e87`（n=2·单件 2,637 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`ae07f5551e87`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/p_i_curvature_audit_probe_results_2026_09_16.json`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-82 `b0e2673f4a56`（n=2·单件 88,584 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`b0e2673f4a56`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_v41_flash_rag_partial.bak.json`→`PULLBACK`、`MC-S5`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-83 `b471190e579c`（n=2·单件 770 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`b471190e579c`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/deposon_team/verifier/v42_v2_runs_2026_09_16.jsonl`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-84 `b9b65c568842`（n=2·单件 915 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`b9b65c568842`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：**是**——`repo/results/deposon_v20_vector_audit.json`（results/ 根层·判定/登记族名） ⇒ **⛔ 0 减**
4. **若减，留哪一件**：**留 `repo/results/deposon_v20_vector_audit.json`**（依留件规则 ②：他件引用 55 件（路径式 33／裸名式 79）；规则 ③ repo 侧优先）。**删**：`sub/results/_archive_2026_09_21/deposon_v20_vector_audit.json`（sub·路径式活引用 11·同名歧义）。
5. **减后须登记**：**12 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 11 处逐处登记）。

### §4-85 `befdd577adce`（n=2·单件 1,141 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`befdd577adce`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`sub/.trae/audit/compile_evidence/extract_tars.py`、`sub/.trae/audit/compile_evidence/v2pre_h1h3_20260909/extract_tars.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `sub/.trae/audit/compile_evidence/extract_tars.py`**（依留件规则 ②：他件引用 20 件（路径式 10／裸名式 25））。**删**：`sub/.trae/audit/compile_evidence/v2pre_h1h3_20260909/extract_tars.py`（sub·路径式活引用 10·同名歧义）。
5. **减后须登记**：**11 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 10 处逐处登记）。

### §4-86 `c5598b13c139`（n=2·单件 17,363 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`c5598b13c139`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/deposon_team/verifier/v42_v2_2026_09_16.py`、`sub/deposon_team/verifier/v42_v2_2026_09_16.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/deposon_team/verifier/v42_v2_2026_09_16.py`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-87 `c68076c88140`（n=2·单件 26,253 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`c68076c88140`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/_v5_gt8_lowarm_result_2026_09_29.json`**（依留件规则 ②：他件引用 40 件（路径式 24／裸名式 28）；规则 ③ repo 侧优先）。**删**：`sub/results/_v5_gt8_lowarm_result_2026_09_29_cb132cd5.json`（sub·路径式活引用 16）。
5. **减后须登记**：**17 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 16 处逐处登记）。

### §4-88 `c7c59e0d2f6c`（n=2·单件 8,753 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`c7c59e0d2f6c`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/boss_pa_1_rbr_rm_result_2026_09_15.json`**（依留件规则 ②：他件引用 216 件（路径式 167／裸名式 244）；规则 ③ repo 侧优先）。**删**：`sub/results/boss_pa_1_rbr_rm_result_2026_09_15.json`（sub·路径式活引用 0·同名歧义）。
5. **减后须登记**：**1 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 0 处逐处登记）。

### §4-89 `c9796d3b3263`（n=2·单件 12,479 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`c9796d3b3263`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/results/deposon_benchmark_v1_4_sc5.json`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-90 `ca71aa6858e1`（n=2·单件 631,644 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`ca71aa6858e1`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/deposon_v20_corpus_eval.json`**（依留件规则 ②：他件引用 98 件（路径式 54／裸名式 90）；规则 ③ repo 侧优先）。**删**：`sub/results/_archive_2026_09_21/deposon_v20_corpus_eval.json`（sub·路径式活引用 11·同名歧义）。
5. **减后须登记**：**12 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 11 处逐处登记）。

### §4-91 `d2cd7acb29a1`（n=2·单件 18,596 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`d2cd7acb29a1`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/corpus/v20_caption_surface/_p_d_b3_merkle_22caption_runner_2026_09_16.py`、`sub/deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_09_16.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/corpus/v20_caption_surface/_p_d_b3_merkle_22caption_runner_2026_09_16.py`**（依留件规则 ②：他件引用 77 件（路径式 38／裸名式 73）；规则 ③ repo 侧优先）。**删**：`sub/deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_09_16.py`（sub·路径式活引用 19·同名歧义）。
5. **减后须登记**：**20 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 19 处逐处登记）。

### §4-92 `d3f72f67977d`（n=2·单件 639 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`d3f72f67977d`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/results/llm_prior_cache_v18_contamination.json`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-93 `d6f233d73c45`（n=2·单件 9,098 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`d6f233d73c45`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/boss_pa_3_replicator_dynamics_result_2026_09_15.json`**（依留件规则 ②：他件引用 96 件（路径式 60／裸名式 76）；规则 ③ repo 侧优先）。**删**：`sub/results/boss_pa_3_replicator_dynamics_result_2026_09_15.json`（sub·路径式活引用 0·同名歧义）。
5. **减后须登记**：**1 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 0 处逐处登记）。

### §4-94 `d74d6b39d1b0`（n=2·单件 1,265 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`d74d6b39d1b0`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/boss_pc_3_a3_clipping_2026_09_15.json`**（依留件规则 ②：他件引用 72 件（路径式 50／裸名式 65）；规则 ③ repo 侧优先）。**删**：`sub/results/attack_pc_a3_clipping_2026_09_15.json`（sub·路径式活引用 22）。
5. **减后须登记**：**23 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 22 处逐处登记）。

### §4-95 `dc9cb0e02922`（n=2·单件 28,370 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`dc9cb0e02922`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `sub/results/_d1_ruling_and_s3_transition_2026_10_01.md`**（依留件规则 ②：他件引用 120 件（路径式 94／裸名式 127））。**删**：`repo/results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_d1_ruling_and_s3_transition_2026_10_01.md`（repo·路径式活引用 8·同名歧义）。
5. **减后须登记**：**9 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 8 处逐处登记）。

### §4-96 `dce965058076`（n=2·单件 2,841 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`dce965058076`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_teamo_via_proxy.py`、`sub/results/_archive_2026_09_20/_probe_teamo_via_proxy.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_teamo_via_proxy.py`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-97 `dfbcc5d6fc34`（n=2·单件 13,775 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`dfbcc5d6fc34`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/corpus/v20_caption_surface/_p_d_v03_22caption_verification_20260917_163757.json`**（依留件规则 ②：他件引用 42 件（路径式 21／裸名式 49）；规则 ③ repo 侧优先）。**删**：`sub/results/_p_d_v03_22caption_verification_20260917_163757.json`（sub·路径式活引用 23·同名歧义）。
5. **减后须登记**：**24 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 23 处逐处登记）。

### §4-98 `dfe014c627ca`（n=2·单件 988 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`dfe014c627ca`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/results/v20_statcheck_fm_vs_deg.json`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-99 `e05555deb611`（n=2·单件 12,919 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`e05555deb611`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_i_curvature_audit_probe_runner_2026_09_16.py`、`sub/results/_archive_2026_09_20/_p_i_curvature_audit_probe_runner_2026_09_16.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_i_curvature_audit_probe_runner_2026_09_16.py`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-100 `e11319f32dc5`（n=2·单件 2,187 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`e11319f32dc5`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_sanity_openai_more.py`、`sub/results/_archive_2026_09_20/_sanity_openai_more.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_sanity_openai_more.py`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-101 `e3b0c44298fc`（n=2·单件 0 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`e3b0c44298fc`）；**反例命中**：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/gpt6_30cells_run.log.err`（0 字节空件）、`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/volcengine_glm_latest_30cells_v2_run_2026_09_10.log.err`（0 字节空件）。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/gpt6_30cells_run.log.err`→`PULLBACK`；`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/volcengine_glm_latest_30cells_v2_run_2026_09_10.log.err`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-102 `ef5a40554960`（n=2·单件 46,836 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`ef5a40554960`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/results/_v3_s_prereg_v1_2026_09_27.md`**（依留件规则 ②：他件引用 293 件（路径式 208／裸名式 272））。**删**：`repo/results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_v3_s_prereg_v1_2026_09_27.md`（repo·路径式活引用 8·同名歧义）。
5. **减后须登记**：**9 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 8 处逐处登记）。

### §4-103 `efe05ad775de`（n=2·单件 24,150 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`efe05ad775de`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **若减，留哪一件**：**留 `repo/corpus/v20/index_v2_2026_09_16.json`**（依留件规则 ②：他件引用 165 件（路径式 84／裸名式 217））。**删**：`repo/corpus/v20/by_model/kimi/index_v2_2026_09_16.json`（repo·路径式活引用 57·同名歧义）。
5. **减后须登记**：**58 条**（1 件自身「旧路径→新路径」＋ 路径式活引用 57 处逐处登记）。

### §4-104 `f2818fc2ddff`（n=2·单件 2,589 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`f2818fc2ddff`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_doubao_emb_via_proxy_2026_09_17.py`、`sub/results/_archive_2026_09_20/_probe_doubao_emb_via_proxy_2026_09_17.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_doubao_emb_via_proxy_2026_09_17.py`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-105 `f2934e5279e6`（n=2·单件 9,717 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`f2934e5279e6`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_mavis_full_mirror_request_2026_09_17.md`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-106 `f2a655cd5e54`（n=2·单件 3,467 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`f2a655cd5e54`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/results/_trae_corpus_5_audit_20260917_193000.md`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-107 `f3d4ec483599`（n=2·单件 41,446 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`f3d4ec483599`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：**是**——`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_main_runner_2026_09_18.py`、`sub/results/_archive_2026_09_20/_d05_main_runner_2026_09_18.py` ⇒ **⛔ 0 减**
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_main_runner_2026_09_18.py`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-108 `f95f382ace44`（n=2·单件 2,151 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`f95f382ace44`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/results/v20_graph_features.csv`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-109 `fd38a2a1ea05`（n=2·单件 7,617 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`fd38a2a1ea05`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_content_A1_glm51.md`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

### §4-110 `fe80bad08eef`（n=2·单件 13,726 B·冗余 1）

1. **真重复否**：**是**——全字节 SHA-256 相同（`fe80bad08eef`）；**反例命中**：——无 0 字节空件、无对照族名、无「被代码写出」之证据。
2. **含唯一生成器／代码源否**：否（成员皆非代码件）
3. **含权威件否**：否（无成员落于 PI 裁答／判定／登记面）
4. **禁令锁定（最高优先）**：**⛔ 0 减**——组内成员落禁令面：`repo/_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_tech_B2_grok46.md`→`PULLBACK`。
5. **减后须登记**：**不适用**（不减⇒无旧→新登记义务）。

> **§4-4 注（窄读之提请·⛔ 0 代裁）**：上表第 2 问之「代码源 ⇒ ⛔ 0 减」系**按派工单字面**（组含代码源即不减）。然实测中 **8/8 个代码源组，其代码件自身即有 2 份逐字节副本**——若留其一，**可复算性并不因删另一份而失**。此为**窄读**与**宽读**之分歧，**本棒不代裁**，提请 PI 定；本件之可减数**一律按宽读（不减）计**。

---

## §5 汇总与净减（件数尺）

### §5-1 可减件数合计

| 桶 | 组 | 件数 | 义（白话） |
|---|---:|---:|---|
| **上传面内·单区** | 10 | 11 | 组内各件同在 repo 或同在 sub（无跨区取舍问题） |
| **上传面内·跨区** | 20 | 24 | 组跨 repo↔sub；**留哪侧须 PI 定取向**（本棒按留件规则暂取「活引用多者」，见 §4） |
| └ 其中**拟删侧在 sub** | — | 18 | 删 sub 侧副本、留 repo 侧 |
| └ 其中**拟删侧在 repo** | — | 6 | 删 repo 侧副本、留 sub 侧（因该副本被引多于其 repo 侧对应件） |
| **须 PI 特别核** | — | **34** | 该拟删件带**路径式活引用 > 0**（26 件）或**同名歧义**（28 件）⇒ 删除前须先补登记或先定归属 |
| **可减合计** | **30** | **35** | 占上传面 3924 件之 **0.89%**（**件数尺**·⛔ 0 以体积论） |

### §5-2 ⛔ 0 减之件数（逐类给数）

| 类 | 组 | 件数 | 依据 |
|---|---:|---:|---|
| **禁令锁定（最高优先）** | 69 | 71 | 落委派域 `E3`–`E8`／对比件域 `MC-E3`·`MC-E4`／内部真册禁令面（§1-4）⇒ **无论是否重复、删后断链与否，一律 ⛔ 0 减** |
| **唯一生成器／代码源** | 8 | 10 | 读数件之生成器（`.py`/`.ps1`/`.sh`/`.bat`/`.cmd`/`.ipynb`）——删之即失可复算性 |
| **权威件** | 3 | 3 | PI 裁答／判定／登记面（`pi_rulings\`、`results\` 根层判定·登记族名、仓根 `_pi_` 族名） |
| **语义不同** | 0 | 0 | 0 字节空件＝「洁净运行」之证据面（承旧账「噪声·日志／空捕获」之判）；**本批该族 2 件全落 pullback 面 ⇒ 已并入禁令锁定** |
| **小计** | **80** | **84** | 71（禁令）＋ 10（代码源）＋ 3（权威）＋ 0（语义）＝ 84 ✅（可减 35 ＋ ⛔ 0 减 84 ＝ 119 相符） |

### §5-3 与旧账「删面 ＝ 0」之对照（差多少·差在哪）

| 读 | 组／件 | 冗余 | 扫描面 | 判重口径 | 时点 |
|---|---:|---:|---|---|---|
| 旧读一 `cbd85f8c5522` | 99／204 | — | repo 全域 ＋ sub 文本面件 | SHA-12 相同 | 16:35:59 |
| 旧读二 `3c55ea8be914` | 118／270 | ~10.6 MB | 「全树」（`.tmp` 域 24 组） | 逐字节相同 | 00:39–00:52 |
| **本读** | **110／229** | 119 件 | **上传面**（repo 去 `.tmp` ＋ sub） | 全字节 SHA-256 | 2026-10-22 18:22:56 |

**差在哪（逐条归因·凡不能复现者如实写「未能复现」）**：

1. **旧读二 ≈「repo 全树」口径**：本棒以同一口径复算（repo 含 `.tmp`，全字节 SHA-256）得 **120 组／279 件**；旧读二载 **118 组／270 件** ⇒ **差 +2 组／+9 件**。其中旧读二「`.tmp` 域 24 组」与本棒「`.tmp` 全域组 24 组」**逐位吻合** ✅；旧读二「0 字节件 28 件」与本棒同口径 **32 件** 差 **+4 件** ⇒ 两者之差可归因于**时点差**（00:39 → 2026-10-22 18:22:56，仓为活面，`.tmp` 工作件持续增减）**＋ 判重口径经实测等价（0 前缀碰撞）**。
2. **旧读一之口径本棒未能复现**：按其 §1-4 自述之扫描面（repo 全域 ＋ sub 之 `.md/.txt/.py/.log/.ps1/.jsonl` 文本面件）复算，得 **174 组／389 件**；再去 `.tmp`-only 组得 **150 组／334 件**；再完全去 `.tmp` 得 **70 组／143 件**——**三者皆非 99／204**。⇒ 旧读一之 **99 组／204 件** 与本棒任一口径**均不相符**，且**旧读一未发布其 99 组之逐组清单**（其 §4-1 为归档清单，非重复族清单）⇒ **无法逐组对照**。本棒**不判孰是孰非**，只登记：差 **11 组／25 件**，成因**未能辨明**（可能为：其普查面另有未载之排除项／时点差／其判重实际口径与所载「SHA-12 相同」不尽相同）——**列为未查明之面，见 §6-3**。
3. **判重口径之差已排除**：SHA-12 前缀分组与全字节 SHA-256 分组在**每一个作用域**内**组数与件数完全相等** ⇒ 旧读之「SHA-12 相同」与本棒之「全字节相同」**在本仓面上不产生差异**。
4. **扫描面之差（主因）**：旧读二之 118 组中含 **24 组纯 `.tmp` 组**（不在上传面）；旧读一自述扫 repo 全域（含 `.tmp`）——本单之射程**排除 `.tmp`**（丙约束）⇒ 本读之 110 组**必然**少于旧读二之 118 组。

### §5-4 与旧账「删面 ＝ 0」之差（一段话）

旧账之结论是「**删除面 ＝ 0**」，其理据为「99 组逐组实测皆有活引用 ⇒ 删任一侧即生幽灵」——**这是引用尺的判法**：把「生幽灵」当作**否决项**。PI 已于 2026-10-22 换尺：**唯一判据为件数**（体积不论），且明令「归档区不上传，日志面就留着」——按新尺，**生幽灵不构成否决**，幽灵**可登记**（留「旧路径→新路径」映射表即可，不改原引一字）。据此，本棒实测上传面内 **110 组／229 件**重复族，**可减 35 件**（占上传面 3924 件之 0.89%），**不减 84 件**（禁令锁定 71／代码源 10／权威件 3／语义不同 0）。故与旧账之差**不在体积**（体积本单不入射程），而在**判据之基座**：旧账以「引用链完整」为留之充分理由，新尺以「件数」为唯一标尺——**同一批件，在旧尺下 0 可减，在新尺下 35 件可减**；代价则是**登记义务 508 条**（路径式引用 473 处逐处登记 ＋ 35 件自身旧→新登记）。**本棒只出候选与登记底单，0 移动 0 删除 0 改名——执行须 PI 逐单令。**

---

## §6 老实交代（限制面·⛔ 0 软化）

### §6-1 我没扫到哪些面

- **`.tmp` 全域**（`〔本地路径已脱敏〕` ＋ `results\.tmp`）：**已排除**（丙约束），仅作归因对照计数（4307 件）。其**正文未被本单引用面扫描**（故本棒引用数**不覆盖 `.tmp` 之提及**）。
- **归档区 `〔归档区〕`**（40,121 件）：**仅计数·⛔ 0 列名内容·⛔ 0 读其正文**——其内之重复族**完全未判**。
- **`GLM` 面**（21 件）：**仅计数·⛔ 0 触内容**——其内之重复族**完全未判**。
- **`Deposon_v1_2_0_交付包`**（36 件）：不在 PI 所定上传面（repo ＋ sub）内，**未入普查**。
- **二进制／不可解文件**：扫描面内 **62 件／7,890,409 B** 被跳过（PNG/`.pyc`/压缩件等）⇒ **引用数系下界**；其**是否成组重复，本棒未单独普查**（其 SHA-256 已算，故其组别已在组表内，只是不产生引用面读数）。
- **仓外其它根**：`〔本地路径已脱敏〕` 下另有个别散件（PDF/JPG/docx 等）——不在 PI 所定上传面，**未入普查**。
- **禁令面之逐件源**：`letters/`（E3 全区）经实测**在本批重复族中命中 0 件**（141 件内无逐字节重复者）⇒ E3 **未咬合**本单；但 `letters/` 全区**按禁令本就不在上传面**，其**自身**之重复情况本棒**未普查**（⛔ 0 触其内容于判减面）。
- **E5「本地旧名件 10 件」／E7「当日审计/登记 5 件」**：在册件**只给件数·未给逐件路径**（v0.4 之 `KD-V04-06` 明载「H4／v0.3 之 `E4` 只给件数 10 · 0 给任何一条路径 ⇒ ⛔ 0 以「文件名含 dataset」反推充之」）⇒ 本棒**不臆造路径**、**未臆造锁定**，二者在 §6-6 如实登记为**未定位**。
- **`.tmp` 面之提及量**：本棒曾起算「`.tmp` 内对本批成员之提及数」（用以量化引用数之下界缺口），**该作业两度被网络中断取消** ⇒ **未测**（如实登记，非「无提及」）。

### §6-2 我判「可减」时最没把握的是哪几组、为何

| 疑点 | 组数／件数 | 我为何没把握 |
|---|---|---|
| **跨区组之「留哪侧」** | 20 组／24 件 | PI 10-12 逐字「两区件数差不多」指向**减 repo 侧**，而权威链条与登记件多锚于 repo（指向**留 repo 侧**）；两条取向相反，**本棒按「活引用多者留」暂取**，属 PI 裁面 |
| **代码源之窄读／宽读** | 8 组／10 件 | 派工单字面「组含代码源 ⇒ ⛔ 0 减」；然其中 8 组之代码件**自身即有逐字节副本**，删其一**不失可复算性**——本件按宽读计（不减），窄读之果待 PI 裁 |
| **同名歧义件** | 28 件 | 裸名式引用**归属不可分**（同件名多路径），故「留哪一件」之判断在此类上**证据不足**；本件已逐件标〔同名歧义〕，建议 PI 逐件定或整组保留 |
| **`.tmp` 提及未计之组** | 0 处提及（上传面外） | 本棒引用面**不覆盖 `.tmp`**；若某件在 `.tmp` 内被大量提及而上传面内为零提及，其「零引用」为**面内零**而非**真零**（本棒**不主张**真零） |
| **旧读一之 99 组** | — | **未能复现其口径**（§5-3 第 2 条）⇒ 本棒与旧账**无法逐组对照**，此差之归因**未完成** |
| **禁令锁定之 69 组／71 件** | 69 组／71 件 | 锁定依据为**在册禁令面之逐条试面**（§1-4）；其中 **60 组**之锁定完全依赖「`_remote_pullback_2026_10_17/` 0 自行纳入上传面」之 **§7.3 carve**——该 carve 之射程（是否含「本地独有之拉回件」）**未逐件论证**，故本棒取**保守读**（整面锁），**PI 若判该 carve 仅及远端残留件**，则此 60 组之可减性**将重开** |
| **E5／E7 禁令面之未定位者** | 10 ＋ 5 件（**件数已知·路径未知**） | 在册件未给逐件路径 ⇒ 本棒**不臆造**；若这些件中含重复件，则其可减性**本单未判** |

### §6-3 三套数之差·我如何归因（逐条）

1. **旧读二（118／270）↔ 本读之含 `.tmp` 复算（120／279）**：差 **+2 组／+9 件** ⇒ 归因于**时点差**（00:39–00:52 → 2026-10-22 18:22:56，仓为活面）与**0 字节族增生**（28→32 件）；其「`.tmp` 域 24 组」与本棒逐位吻合 ✅，故**扫描面一致**。
2. **旧读一（99／204）↔ 本读**：**未能复现**——按其自述扫描面复算为 174／389、去 `.tmp`-only 组为 150／334、去 `.tmp` 全域为 70／143，**无一为 99／204**；且旧账**未发布其逐组清单**⇒ **不可逐组对照**，成因**悬置**，如实登记为未查明。
3. **判重口径**：**已排除**为成因（前缀与全字节在本仓面**逐作用域相等**）。
4. **扫描面**：**已确证**为主因之一（`.tmp` 域 24 组不在本单射程）。

### §6-4「全字节相同」这一口径之反例风险

- **空文件**：全字节相同（皆为空）但**语义不同**——空件常为「空 stderr ＝ 洁净运行」之**证据面**（旧账「噪声·日志／空捕获」行即为此义）。本单已把 0 字节族（0 组／0 件）**整族列入 ⛔ 0 减**。
- **生成时间戳内嵌于内容之件**：若文件**正文内嵌**时间戳/随机种子，则两份内容**不会**全字节相同（故不会成组）——**此风险在本口径下自动规避**；反之，若时间戳仅存于**文件名或 mtime**，则内容相同而**名异**（本表之常态），此时**「同字节异名」本身即是复现性之据**（旧账此语成立），但**不代表两侧可互换**（路径式引用仍须逐处改指）。
- **常量配置文件 / 刻意留作对照之副本**：内容相同而**用意不同**（一份作基线、一份作被测）。本棒以**族名**（`baseline`／`对照`／`control`／`origin`／`keep_`／`sample_`／`_copy`／`副本`）与**代码写出关系**两项代理信号扫描；实测中**可减组内命中 0 组**（故此风险**未实质发生**），然代理信号**非语义证明**——若 PI 知某组确为对照件，请径行指出，本棒据此改判。
- **语义不同而无族名可依者**：**无法由仪器辨明**。此类若存在，只可能经 PI 指出后追认。
- **「同字节但一侧在禁令面」之反例（实测最重之一）**：本批 **69 组／71 件**之重复族含**落禁令面之成员**（pullback carve 之拉回副本、密钥门件、S5 临时件副本、E8 路径泄漏 manifest 之副本）⇒ **全字节相同 ≠ 可互换**：删其一即**触禁令面**或**动受禁之件**。此即 §1-4 锁定层之价值所在——**若无先查惯例，此 71 件将误入可减候选**。

### §6-5 本单之动作面（0 移动 0 删除 0 改名）

| 项 | 实测 |
|---|---|
| 移动既有件 | **0** |
| 改名 | **0** |
| 删除既有件（任何口径·含可恢复通道） | **0** |
| 新建目录 | **0** |
| 新建**文件** | **1**（本件·`results\_dedupe_uploadface_recount_2026_10_22.md`）——落前停手闸 `Test-Path`＝False ＋ 长名式 0 命中 ⇒ 属**新建**非覆盖 |
| 回改既有件之字数 | **0 字** |
| 触归档区内件（40,121 件） | **0**（仅计数） |
| 触 `GLM` 面内容（21 件） | **0**（仅计数） |
| 仓内其他件之写入（普查器与中间件） | **0**（皆落仓外 TEMP） |
| 联网 | **0 次** |
| 读 `LLM API.txt`／任何凭据 | **0**（上传面内经实测**不存在**此类件） |
| LLM 调用 | **0 次** |
| 落五终判／闭 KD／宣告段毕／代 PI 裁 | **0** |

### §6-6 未查明之面（⛔ 0 掩饰）

1. **旧读一 99 组／204 件之确切口径**——本棒三种复算口径皆不能复现，且其逐组清单未发布 ⇒ **成因悬置**。
2. **跨区组「留哪侧」之正解**——PI 两条取向（拉平／权威链）相冲，本件按规则暂取，**正解待裁**。
3. **同名歧义件之引用归属**——仪器**原理上**不可分（非工具缺陷，属信息不足）。
4. **`.tmp` 面内之重复族**（24 组纯 `.tmp` 组等）——**未判**（不在本单射程）。
5. **归档区／`GLM`／交付包面内之重复族**——**未判**（仅计数）。
6. **二进制件之引用面**——62 件／7,890,409 B 被跳过 ⇒ 其引用数**未测**。
7. **「语义不同」之无族名可依者**——仪器不可辨明，待 PI 指出后追认。
8. **本件自身之引用面**——本件为**新建件**，落盘后始有引用；其可减性**本单不判**（自指面）。
9. **E5「本地旧名件 10 件」之逐件路径**——在册件**只给件数**（`KD-V04-06` 明禁反推）⇒ **未定位·未臆造**；若其中含本批重复件，其可减性**未判**。
10. **E7「当日审计/登记 5 件」之归属**——在册件载「**推荐排除**；是否处置 ⛔ 候 PI」⇒ 本棒**不代裁**，其与本批重复族之交集**未判**。
11. **`.tmp` 面之提及量**——本棒欲量化「引用数之下界缺口」之作业**两度被网络中断** ⇒ **未测**（非「无提及」）。
12. **§7.3 carve 之射程**——`_remote_pullback_2026_10_17/`「0 自行纳入上传面」是否及于「本地独有之拉回件」，在册件未逐件论证；本棒取保守读（整面锁）⇒ 若 PI 判其仅及远端残留件，则 **60 组／60 件**之可减性**将重开**。

---

*件止。evidence-auditor（证据链审计面）· 2026-10-22 · 判据＝件数（甲）· 射程＝上传面（丙）· 幽灵可登记（乙）· **禁令先查（§1-4·最高优先）**。⛔ 0 移动 0 删除 0 改名 0 建目录 · ⛔ 0 回改既有件 · ⛔ 0 触归档区内容与 `GLM` 内容 · ⛔ 0 以体积为据 · ⛔ 0 联网 · ⛔ 0 读凭据 · ⛔ 0 落五终判／闭 KD／宣告段毕／代裁。*
