# 门槛③ ·「判定件全集」口径封口件（2026-10-23）

> 📌 **件性质**：**判定件全集口径封口登记件**（`evidence-auditor` 证据链审计官自执）——**不是判定件**、**不是收口件**、**不是宣告件**。
> 📌 **授权源**：PI 2026-10-23 15:24:47 卡 `ask_3fd8ca0bc50f9997e967992c` Q3 逐字「**派棒重测（推荐）**」；落账于 `pi_rulings\_pi_card_answers_register_2026_10_23_v250.md`（`34da2994c8a4`／4,255 B）§2-3。
> 📌 **本棒之任务格**：重测件自报之**第一条未核得**即「**判定件全集口径**」——本棒把这一格封口：**辨明「判定件」之定义 → 枚举全集 → 与已审 9 件比对 → 出覆盖率**。
> 📌 **依据件**：`results\evidence\register\_gate3_audit_recount_2026_10_23.md`（**38,179 B**／**`c2e607d15904`**）——今日实算 PASS 4／PWF 5／FAIL 0・被审件 **9**。
> 📌 **观测时点**：**2026-10-23 15:42–16:2x（GMT+8）**；本件全部现值系本棒**自测**（SHA-256 前 12 位／bytes／mtime 逐件复算）。
> 📌 **必带 skill（实读）**：① `superpowers:verification-before-completion`（`〔本地路径已脱敏〕`・**3,646 B**／`2befe7fc55bc`）② `scientific-critical-thinking`（`〔本地路径已脱敏〕`・**23,704 B**／`df53105c317a`）——**皆全文读毕**。⚠ 派工单所载带前缀名 `scientific-research-workflows:scientific-critical-thinking` 之**调用失败**（返回「Local skill not found」），以裸名命中并读毕同一件（落盘路径在 D 盘，异于派工单所载 C 盘——沿 10-22 审计书 §2.6 之「两盘符并存」同族事实）；**⛔ 0「无需 skill」**。
> 📌 **边界自述**：⛔ **0** 宣告门槛③ 已成就或未成就·⛔ **0** 宣告段毕·⛔ **0** 落五终判·⛔ **0** 闭 KD·⛔ **0** 代 PI 裁·⛔ **0** 以新值径换在册值·⛔ **0** 跑实验·⛔ **0** 测量·⛔ **0** 联网·⛔ **0** 调 LLM／API·⛔ **0** 读 key／`.env`·⛔ **0** 回改任何既有件一字·⛔ **0** 移动／重命名／删除·⛔ **0** 新建目录·⛔ **0** 读 `〔归档区〕` 与 `〔本地路径已脱敏〕` 之内容（**仅计数**）。

---

## §0 · 一句话（**本件之全部效力**）

> 📌 **「判定件」之定义已辨明**（母件 L160 逐字 ＋ 件别自载之族称，见 §1）；**但「全部判定件」之全集不可由任何机械判别式唯一定出**——母件 **0 处**给出全集，审计书 §3-3 逐字明载其「**须由 PI／主代理核定**」。
> 📌 故本棒**列 3 种口径**，各给**件数／已审交集／覆盖率**，**⛔ 0 择一**：口径甲（落档树·目录）**478** 件 · 覆盖率 **3/478 = 0.63%**；口径乙（自载件别·判定族）**148** 件 · 覆盖率 **2/148 = 1.35%**；口径丙（判官落款·自证）**61** 件 · 覆盖率 **0/61 = 0.00%**（**该口径判别式实测含假阳性，本棒不采其数为全集之数**，见 §2-3）。
> 📌 **最关键之一格**：**已审 9 件之 7 件自载为非判定件**（逐件见 §3）⇒ **已审面之口径宽于「判定件」面**——**「9 件 ＝ 全部」不成立**。
> 📌 **本件只出读数**：门槛③ 之成就之判**归 PI**；本件**⛔ 0** 宣告之。

---

## §1 · 「判定件」之定义（**逐字引出 · 出处 · 本棒自测指纹**）

### §1-0 术语首现附白话（**代号必附其义**）

| 代号 | 白话 |
|:--|:--|
| **判定件** | **由判官（`verdict-keeper`）落档、载有裁断（hit／verdict／落 kd 等）之件**——即「谁裁的、裁了什么」的那一格之产出件。 |
| **判定收口件** | 判定件之**主族称**：判官把一件之裁断**收口成文**之件（件性质栏自载语）。 |
| **覆盖度判定件** | 判定件之**旁族称**：只裁「某批判死线**有几条真算过**」之覆盖度、非终判之件。 |
| **审计判定件** | **第二人复核件**：审计官（`evidence-auditor`）对某件之证据链复核后出的判定书——**不由判官落档**。 |
| **落档树** | 盘上 `results\verdict\`（`judgement\` ＋ `pi_register\`）之目录面。 |
| **判别式** | 本棒用于机械判别「某件是否属某口径」之**可复算规则**（本件逐条载明，供他人复算）。 |
| **SHA-12** | SHA-256 全值之**前 12 位小写十六进制**，作件之指纹。 |
| **口径** | 「判定件全集」之**候选边界**；本棒**不择一**，并列给覆盖率。 |

### §1-1 母件之**约束性表述**（门槛③ 之文义・全句照录）

> **件**：`results\readout\run\_v34_experiment_gap_plan_2026_10_08.md`（V3~V4 实验缺口全量排期 ＋ 第一波开跑单・出件方 `protocol-keeper`）
> **行**：**L160**（节题 `### §2.3 收官门槛（自设·供 PI 复核）` 在 **L158**）
> **本棒自测指纹**：SHA-256 前 12 位 **`996feb1db9cb`**／**36,066 B**／mtime **2026-10-08 16:46:11**

**逐字（L160 · 全句照录）**：

> 「V3~V4 完整收尾」之宣告须**同时**满足：① §2.1 八项硬缺口 0 残留；② 全部波次产出件 0 有「不明/未核得」状态；③ 全部判定件由 **verdict-keeper** 落档 ＋ **evidence-auditor** 证据链审计 PASS；④ 全量成果清单（上传/论文委托用）出件。**⛔ 本件 0 宣告已收官**（宣告权属 PI，阶段名启用权亦在 PI）。

**⇒ 母件之定义**（**作者口径**）：**判定件 ＝ 由 `verdict-keeper` 落档之件**；且**须**有 `evidence-auditor` 之证据链审计 PASS。

**⚠ 母件 **0 处**给出「全部判定件」之名单或可枚举规则**（本棒全件通读所见）——故**全集不可由母件直接读出**。

### §1-2 件别自载之**族称**（逐字引出・各件本棒自测指纹）

| # | 件（repo 相对路径） | 自测 SHA-12 ／ bytes | **件性质栏逐字**（截取至第一个句止） | 该件自载之族称 |
|:-:|:--|:--|:--|:--|
| 1 | `results\verdict\judgement\_judgement_w39_two_reading_2026_10_23.md` L7 | `f35fe7d03551`／54,862 | 「🟣 **判定收口件（`verdict-keeper` 之裁决产出）** —— 本件所裁者 ＝ **扩词清单 39 词之「两读并存」择优预实验**（读甲＝39 词面入判定面／读乙＝39 词面不入判定面）**一次复算所得读数之判定收口**」 | **判定收口件** |
| 2 | `results\verdict\judgement\_kexp8_coverage_adjudication_2026_10_22.md` L5 | `80631fb4ce3d`／62,301 | 「🔴 **判定收口件**（`verdict-keeper`·根因裁决）」 | **判定收口件** |
| 3 | `results\verdict\judgement\_t4k_k5k_coverage_adjudication_2026_10_22.md` L5 | `66d8d45c7a62`／61,203 | 「🔴 **覆盖度判定件**（非终判件 · 非实验件）——所判者 ＝ **`K-T4K-1..18` ＋ `K-T5K-1..20` ＝ 38 条**判死线**逐条核之覆盖度**（有几条真算过）」 | **覆盖度判定件** |
| 4 | `results\review\audit\_nightly_audit_pass_2026_10_22.md` L5 | `dea7dab1f4cb`／36,878 | 「**审计判定件**（证据链面）——**第二人复核**之果」 | **审计判定件**（**非判官落档**） |
| 5 | `results\verdict\judgement\_e07_deliberation_2026_10_22.md` L5 | `1fe936ee5f67`／35,064 | 「**辨明件**（辨明径之三径之辨 ＋ 候选并出 ＋ 荐案（荐案＋理由＋代价不对称）＋ 候 PI 裁之最小问题 ≤2）｜⛔ **0** 判定件·⛔ **0** 代裁·⛔ **0** 落五终判·⛔ **0** 闭/开/改判任何 `KD`」 | **反例：辨明件（自载「⛔ 0 判定件」）** |

**⇒ 判定件族之白话（一句）**：**「凡是件自己把「件性质」写成「判定件／判定收口件／判定文书／覆盖度判定件／终态判定件」之一者，即自认是判定件；反之，自载「⛔ 0 判定件」者即不是。」**

**⇒ 之边界（母件 0 处给出・审计书逐字明载）**：

> **件**：`results\review\audit\_nightly_audit_pass_2026_10_22.md`（**`dea7dab1f4cb`**／36,878 B）／**L193**（§3-3）
> **逐字（全句照录）**：
> 「门槛第③项之文义为「**全部判定件**由 verdict-keeper 落档 ＋ evidence-auditor 证据链审计 PASS」。**是否因本件而达成，取决于二事（皆非本棒可裁）**：① 「全部判定件」是否以今夜九件为全集（母件之判定件全集须由 PI／主代理核定）；② 门槛所言之「PASS」是否容许「PASS-with-FINDINGS」（若不容许，则第 3／4／7／8／9 件须先消 FINDINGS 或由 PI 明定其效力）。」

**⇒ 本棒之合法动作边界**：**只能给口径与覆盖率，不能定全集**（全集核定权在 PI／主代理）。

---

## §2 · 三种口径（**判别式 · 件数 · 覆盖率**）

### §2-0 扫描面（**穷举范围**）

| 面 | 范围 | `.md` 件数 |
|:--|:--|--:|
| **`deposon-repo`** | 全树 `os.walk`；**排除** `.tmp`／`.mavis`／`node_modules`／`__pycache__`／`.git`／`_remote_pullback_2026_10_17` | **1,504** |
| **`deposon-sub`** | 全树 `os.walk`；**排除** `.tmp`／`.mavis`／`node_modules`／`__pycache__`／`.git` | **863** |
| **仓外两面** | `〔归档区〕`（40,242 件）／`〔本地路径已脱敏〕`（21 件） | **仅计数・⛔ 0 读内容・0 读文件名・0 哈希・0 写入** |

### §2-1 口径甲（**落档树·目录口径**）——**上界**

- **判别式**：件之路径以 `results/verdict/` 开头（**仓之归属 ＋ 目录面**），且件为 `.md`。
- **全集 N ＝ 478 件**（repo `results\verdict\judgement\` 386 ＋ `results\verdict\pi_register\` 16 ＝ 402；sub `judgement\` 63 ＋ `pi_register\` 13 ＝ 76）。
- **已审且属本口径者 ＝ 3 件**｜**覆盖率 ＝ 3/478 = 0.63%**。
- **⚠ 本口径非纯净**：树内含**非判官所出**之件——实抽：`results\verdict\judgement\_four_face_deliberation_2026_10_22.md` L8 逐字「| **出件方** | `verifier`（复核·另议辨明径 · 本棒）——职责 ＝ **辨明与可解性之取证**（现态实测·阴性三审·候选并出·荐案）；⛔ **0** 出判定裁决（`verdict-keeper`）」；`results\verdict\pi_register\_pi_1009_eight_gap_enum_effect_2026_10_22.md` L8 逐字「| **落账方** | **doc-writer**（文稿起草／落账／登记专官 · `agent-0032834a3e04`）——职责 ＝ **起草与登记**」；树内落款之机械判别：判官 **36**／verifier **14**／`parent` **28**／worker **21**／`protocol-keeper` **6**／`doc-writer` **4**／审计官 **11**／**未检出 353**（判别式之限，见 §6-3）。
- **⇒ 本口径之真值地位**：**真全集 ⊆ 甲**（凡判官落档之件必落树）；**甲 ⊋ 真全集**（含上列他棒件）。

### §2-2 口径乙（**自载件别·判定族口径**）——**本棒之最优判别式**

- **判别式**（三步，可复算）：① 件首 **16,000 字节**内存在一行含「**件性质**」或「**件别**」；② 取该键之后、首个「（」「｜」「|」「·」「—」「；」之前的片段（去 markdown 记号与空白）＝ **自载别名**；③ **别名首 14 字内**含「判定」「判断」「裁决」之一，**且**别名**不含**否定词（不是判定件／非判定／非判档／0 判定件／非判定裁）。
- **全集 N ＝ 148 件**（repo 98 ＋ sub 50）。
- **已审且属本口径者 ＝ 2 件**｜**覆盖率 ＝ 2/148 = 1.35%**。
- **本口径之自载族称之广度**：实测别名含「判定收口件」「覆盖度判定件」「终态判定件」「审计判定件」「判定文书」「判定件」「闭之判定件」「收口方案判定件」「就绪判定件」「另议判断件」「独立判断件」「判断件」「判定面档位件」「判定面材料件」等 ⇒ **「判定件」一族之边界由各件自载，且**自载语**不统一**。
- **⚠ 本口径之盲区（可数）**：repo **643**／1,504 件、sub **491**／863 件**无「件性质」栏可判** ⇒ **「未自载」≠「非判定件」**；且「另议判断件／独立判断件」多为**子代理独立判断**产出（**非判官落档**）⇒ 本口径**含母件字面之外者**。

### §2-3 口径丙（**判官落款·自证口径**）——**本棒明示不采其数为全集之数**

- **判别式**：件首 16,000 字节内，存在一行**同时**含落款字段名（出件方／落盘方／落款／署名／出件／编制／本棒身份／出证方／执笔／作者／经手／出品）**且**含角色名，**且**该行**值域（末分隔符之后）之首个角色令牌为 `verdict-keeper`。
- **全集 N ＝ 61 件**（repo 37 ＋ sub 24）｜**已审且属本口径者 ＝ 0 件**｜**覆盖率 ＝ 0/61 = 0.00%**。
- **⚠ 假阳性实测（本棒实抽 2 件・2 件皆假阳）**：
  - `pi_rulings\_pi_card_answers_register_2026_10_18_v117.md`（`8c13b1bab8a3`／2,960 B）L3 逐字「> 出件面：主代理亲补（省 Token Plan 额度面）。」⇒ **非判官落稿**；
  - `results\_archive_2026-10-14\voided\_four_class_backtrace_inventory_2026_10_13.md`（`cc45240386e8`／29,156 B）L3 逐字「📌 **件性质**：**证据链审计件（清点 ＋ 勘误登记 · ⛔ 非判定件 · ⛔ 非毕判断件）**」⇒ **自载非判定件**。
- **⇒ 本口径之真值地位**：**本棒不采其数为全集之数**（假阳性与漏检均已实测：判官自载之件之落款字段名多变，且树内落款**未检出 353** 件）。**其数仅作「落款自证面」之登记级事实**：该面 **61** 件中，**已审 0 件**。

### §2-4 三口径之并（**最宽可机械判读面**）

- **｜甲 ∪ 乙 ∪ 丙｜ ＝ 567 件**（唯一 SHA-12 计）。
- **⚠ 该并集仍非「真全集」**：母件 **0 处**给出全集，审计书 §3-3 明载其须 PI／主代理核定 ⇒ **真全集之精确清单，机械不可得**。

### §2-5 口径之对照总表

| 口径 | 判别式（白话） | **全集 N** | **已审 ∩** | **覆盖率** | 真值地位 |
|:--|:--|--:|--:|--:|:--|
| **甲** | 落在 `results\verdict\` 落档树里 | **478** | **3** | **3/478 = 0.63%** | **上界**（真全集 ⊆ 甲；甲 ⊋ 真全集） |
| **乙** | 件性质栏**自载**「判定／判断／裁决」族 | **148** | **2** | **2/148 = 1.35%** | 本棒最优；**含母件字面外者・有未自载盲区** |
| **丙** | 落款自证**判官所出** | **61** | **0** | **0/61 = 0.00%** | **不采为全集之数**（假阳性已实测） |

---

### §2-6 荐案（**呈裁面之推荐项 · 供 PI 复核 · ⛔ 0 代裁**）

> 📌 **荐案**：**以「口径乙（自载件别·判定族）＝ 148 件」为门槛③ 覆盖率之分母**，并以「口径甲（落档树）＝ 478 件」为**上界**、以「已审 9 件中自载为判定件者 ＝ 2 件」为**已覆盖面**一并呈 PI 核定。
> **理由**：① 乙之判别式**可复算**（§2-2 三步规则已载明，任何人可独立复算）；② 乙**贴近母件字面**（母件以「由 `verdict-keeper` 落档」为定义，乙之自载族称与之一致度最高）；③ 乙**不把树内非判定件算入分母**（甲含 verifier 辨明件、doc-writer 落账件等，§2-1 已逐字实证），故其覆盖率**不过度悲观**；④ 乙之盲区（无「件性质」栏者 repo 643／sub 491）**已可数**，PI 增补一次「件性质」栏即收窄之。
> **代价不对称**：采乙 ⇒ 分母 148、覆盖率 2/148 ＝ 1.35%，**分母偏小之风险 ＝ 漏计未自载之真判定件**（盲区大，方向为**高估覆盖率**）；采甲 ⇒ 分母 478、覆盖率 3/478 ＝ 0.63%，**分母偏大之风险 ＝ 把非判定件算作未审之判定件**（方向为**低估覆盖率**）。**本棒不裁**，两读并出、请 PI 择定或径自核定清单。
> **⚠ 无论采哪口径**：**已审 9 件中 7 件自载为非判定件**（§3-2）之事实不变 ⇒ 在册「9 件」**不可**充门槛③ 之分母。

---

## §3 · 已审 9 件 × 全集（**交集 · 多余 · 缺口**）

### §3-1 已审 9 件之名单（**回原件取**・非凭记忆）

**出处**：审计书 `results\review\audit\_nightly_audit_pass_2026_10_22.md` §3-1（八件・L171–L178）＋ §3-2（并入第九件・L186）；与重测件 `_gate3_audit_recount_2026_10_23.md` §2-2 之表**逐位相符**（本棒两处交叉核）。

| # | 件名 | 自测 SHA-12 | bytes | 三态（原件载） |
|:-:|:--|:--|--:|:--|
| 1 | `_t4k_k5k_coverage_adjudication_2026_10_22.md` | `66d8d45c7a62` | 61,203 | PASS |
| 2 | `_kexp8_coverage_adjudication_2026_10_22.md` | `80631fb4ce3d` | 62,301 | PASS |
| 3 | `_h_exact_enum_run_reading_domain23_2026_10_22.md` | `61969bbffafa` | 66,704 | PASS-with-FINDINGS |
| 4 | `_ge03_ge04_claim_proposal_2026_10_22.md` | `7b3a93361744` | 70,674 | PASS-with-FINDINGS |
| 5 | `_e07_deliberation_2026_10_22.md` | `1fe936ee5f67` | 35,064 | PASS |
| 6 | `_v186_v225_adoption_effect_2026_10_22.md` | `710521028de9` | 271,671 | PASS |
| 7 | `_v226_v230_adoption_effect_2026_10_22.md` | `cda1b9a751b7` | 172,094 | PASS-with-FINDINGS |
| 8 | `_bloat_inventory_2026_10_22.md` | `3c55ea8be914` | 12,907 | PASS-with-FINDINGS |
| 9 | `_ghost_reference_audit_2026_10_22.md` | `37659d4a398a` | 443,091 | PASS-with-FINDINGS |

### §3-2 逐件之**件别归属**（回原件读其「件性质」栏・**本棒逐件开卷**）

| # | 件 | 所在面 | **自载件别（逐字要点）** | 属判定件？ |
|:-:|:--|:--|:--|:-:|
| 1 | T4K 覆盖度判定件 | `results\verdict\judgement\` | 「🔴 **覆盖度判定件**（非终判件 · 非实验件）」 | **是** |
| 2 | KEXP8 覆盖度裁决 | `results\verdict\judgement\` | 「🔴 **判定收口件**（`verdict-keeper`·根因裁决）」 | **是** |
| 3 | H 精确枚举读出件 | `results\readout\reading\` | 「🔴 **读出件**（`H_exact` 域②③ 之 30 格事实表 ＋ 逐格对账 ＋ 判死线核总账 ＋ 留痕面之可得性登记）」；出件方 ＝ `worker` | **否** |
| 4 | GE03／GE04 提案件 | `results\evidence\register\` | 「> 出件面：**protocol-keeper**（口径与预登记官）｜棒别：`PROP-GE03-GE04-CLAIM-PROPOSAL`」 | **否** |
| 5 | E07 辨明件 | `results\verdict\judgement\` | 「**辨明件**（…）｜⛔ **0** 判定件·⛔ **0** 代裁·⛔ **0** 落五终判·⛔ **0** 闭/开/改判任何 `KD`」 | **否（自载明文否定）** |
| 6 | v186–v225 生效落账件 | `results\readout\run\` | 「**PI 卡答链 v186–v225 段之「采认生效」落账**（38 件源登记件之 136 答 ＋ 3 令 ＝ 147 生效分面之逐面生效落账）」 | **否** |
| 7 | v226–v230 生效落账件 | `results\readout\run\` | 「**PI 卡答与口头令之生效落账**（v226 卡四问 ＋ v227 口头令 ＋ v228 口头令 ＋ v229 卡三问 ＋ v230 卡四问 ＝ **十三答（令）合一**）」 | **否** |
| 8 | bloat 臃肿清单件 | `results\work\process\` | 无「件性质」栏可判；其自载之面为「**引用面** ＝ 某件被仓内文本件（md／txt／py／log／jsonl／csv／err／out）以文件名或路径提及之面」＝**清单／勘查件** | **否（无判定自载）** |
| 9 | ghost 幽灵引用审计件 | `results\review\audit\` | 无「件性质」栏可判；为 **EA 审计面**之件 | **否（无判定自载）** |

**⇒ 交集与多余（核心一格）**：
- **属判定件者 ＝ 2 件**（#1 T4K・#2 KEXP8）；
- **已审但**不属判定件**者 ＝ 7 件**（#3–#9）——**口径多余**（审了非判定件）。
- **⚠ 与在册口径之差**：在册读数「审计 PASS 4／PWF 5／FAIL 0」之分母 ＝ **9 件**；若以「判定件」为全集口径，则该分母**含 7 件非判定件** ⇒ **该读数不可直接充门槛③ 之覆盖率分子**。
- **缺口（在全集而未审）**：口径甲 **475 件**／口径乙 **146 件**／口径丙 **61 件**（逐件清单见 §4）。

---

## §4 · 未审件之逐件清单（**前 8 件 · 全表见 §7**）

### §4-1 口径甲之未审（前 8 件）

| # | SHA-12 | bytes | 相对路径（repo／sub） |
|:-:|:--|--:|:--|
| 1 | `fd7b24a75444` | 74,978 | repo:results/verdict/judgement/_a1_a6_readiness_recheck_2026_10_22.md |
| 2 | `d6d8c488fc33` | 43,259 | repo:results/verdict/judgement/_af1_attribution_verdict_2026_10_17.md |
| 3 | `b3c45b4e2ec0` | 48,208 | repo:results/verdict/judgement/_af2_5_proof_2026_10_17.md |
| 4 | `faee80c8b051` | 41,779 | repo:results/verdict/judgement/_af2_proof_and_grain_scope_effect_2026_10_17.md |
| 5 | `14e4181c5b69` | 54,092 | repo:results/verdict/judgement/_af_complete_landing_effect_2026_10_17.md |
| 6 | `525ae85c1bbc` | 39,994 | repo:results/verdict/judgement/_af_entity_rules_2026_10_17.md |
| 7 | `dc5ee48e1f53` | 45,096 | repo:results/verdict/judgement/_af_flip要件消解_rulings_effect_2026_10_17.md |
| 8 | `ce0a2847ad4e` | 43,731 | repo:results/verdict/judgement/_af_rules_approval_effect_2026_10_17.md |

### §4-2 口径乙之未审（前 8 件）

| # | SHA-12 | bytes | 相对路径（repo／sub） |
|:-:|:--|--:|:--|
| 1 | `9aa1c651bcea` | 50,516 | repo:results/doc/document/_cmp2_sep_threshold_s_proposal_2026_10_18.md |
| 2 | `96956b8cf878` | 49,068 | repo:results/doc/document/_eight_hard_gaps_closure_plan_2026_10_22.md |
| 3 | `36f70c0a844c` | 28,728 | repo:results/evidence/register/_batch7_deliberation_judgment_2026_10_13.md |
| 4 | `a93cd166a83b` | 36,623 | repo:results/evidence/register/_batch9_deliberation_judgment_2026_10_14.md |
| 5 | `0b5bb95a86d7` | 44,728 | repo:results/evidence/register/_four_items_alternative_deliberation_judgment_2026_10_13.md |
| 6 | `b32ca40ec103` | 26,832 | repo:results/evidence/register/_ge01_ecr_anchor_convergence_deliberation_2026_10_14.md |
| 7 | `5a72c931148a` | 31,736 | repo:results/evidence/register/_ge01_readiness_after_prereg_effect_2026_10_13.md |
| 8 | `726c32d83734` | 25,221 | repo:results/evidence/register/_strip_c3_non_adoption_register_2026_10_16.md |

### §4-3 口径丙之未审（前 8 件）

| # | SHA-12 | bytes | 相对路径（repo／sub） |
|:-:|:--|--:|:--|
| 1 | `8c13b1bab8a3` | 2,960 | repo:pi_rulings/_pi_card_answers_register_2026_10_18_v117.md |
| 2 | `a9b424570540` | 2,553 | repo:pi_rulings/_pi_card_answers_register_2026_10_18_v121.md |
| 3 | `c4a688152f74` | 2,407 | repo:pi_rulings/_pi_card_answers_register_2026_10_18_v126.md |
| 4 | `2eae0446faf1` | 3,640 | repo:pi_rulings/_pi_card_answers_register_2026_10_20_v163.md |
| 5 | `a006a39967e7` | 7,850 | repo:pi_rulings/_pi_card_answers_register_2026_10_21_v201.md |
| 6 | `cc45240386e8` | 29,156 | repo:results/_archive_2026-10-14/voided/_four_class_backtrace_inventory_2026_10_13.md |
| 7 | `dc9cb0e02922` | 28,370 | repo:results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_d1_ruling_and_s3_transition_2026_10_01.md |
| 8 | `4aba41f67db5` | 56,321 | repo:results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_limb_reading_verdict_kv3s33_2026_10_01.md |

---

## §5 · 资产缺陷登记（**登记级 · 本棒不代修**）

| # | 缺陷 | 出处 | 分级 |
|:-:|:--|:--|:--|
| **D-1** | **母件 0 处给出「全部判定件」之全集**（名单或可枚举规则皆无）⇒ 门槛③ 之覆盖率**分母不可由原件读出** | 母件 L160 全句 ＋ 全件通读 | 登记级（**须 PI／主代理核定**） |
| **D-2** | **审计书已逐字登记此缺口但至今 0 消项**：§3-3 之问①「「全部判定件」是否以今夜九件为全集（母件之判定件全集须由 PI／主代理核定）」**未获裁** | 审计书 L193 | 登记级 |
| **D-3** | **落档树非纯净判定面**：树内含 `verifier` 辨明件、`doc-writer` 落账件、`parent` 件、`worker` 件、`protocol-keeper` 预登记件、审计官审计件 ⇒ **以目录为全集口径必含非判定件** | §2-1 实抽逐字 | 登记级 |
| **D-4** | **件别自载语不统一**：实测并存「判定收口件／覆盖度判定件／终态判定件／审计判定件／判定文书／闭之判定件／另议判断件／独立判断件／判断件…」等 ≥14 种 ⇒ 「判定件」**无单一命名** | §2-2 别名统计 | 登记级 |
| **D-5** | **「件性质」栏缺载面大**：repo **643**／1,504 件、sub **491**／863 件**无该栏可判** ⇒ 自载口径有**不可判盲区** | §2-2 | 登记级 |
| **D-6** | **落款字段名多变**：实测「出件方／落盘方／落款／署名／出件／编制／本棒身份／出证方／执笔／作者／经手／出品」等 ≥12 种，且**免责语**（「⛔ 0 冒充 …」）与之同现 ⇒ 机械判别易生假阳 | §2-3 实抽 2 件皆假阳 | 登记级 |

---

## §6 · 扫描器自述（**仪器自身即误差源**）

1. **仪器**：Python 3.14.7 `os.walk` 全量穷举 ＋ `hashlib.sha256`（⛔ **0** 用内建 `hash()`）＋ Windows PowerShell 5.1 探针；UTF-8 stdout 强制。
2. **仪器之失-1（管道 BOM）**：首轮以 PowerShell 管道投喂 Python 源码，源首字节带 **U+FEFF** ⇒ 抛 `SyntaxError: invalid non-printable character U+FEFF` **中断**；修法＝管道编码改无 BOM（`$OutputEncoding` 设为 `UTF8Encoding($false)`）。**此为仪器之误，非被审件之失**。
3. **仪器之失-2（路径失真）**：次轮脚本内以中文字面量书写仓路径 ⇒ 管道编码失真 ⇒ `os.walk` **静默得 0 件**（假零）。修法＝路径改 `\uXXXX` 转义构造（`〔本地路径已脱敏〕` ＋ `〔本地目录已脱敏〕`）＋ 加 `os.path.isdir` 诊断探针。**⚠ 假零若未察，则本棒将报「全集 0 件」之荒谬结论**——故登记。
4. **仪器之失-3（判别式跨行匹配）**：首版判别式以「件内同时含『出件方』与『verdict-keeper』」立判，**未要求同行** ⇒ 命中 **492** 件，抽样见大量**免责语**假阳（「⛔ 0 冒充 PI／parent／worker／verifier／verdict-keeper／…」）。修法＝**同行共现** ＋ 值域**首个角色令牌**规则（见 §2-3）。
5. **仪器之失-4（别名取末分隔符）**：再版以 `rfind` 取值，致别名被截成**声明尾部**（如「⛔ 0 落五终判 · ⛔ 0 闭 KD…」）⇒ 大量假阳；修法＝取**首个**分隔符之后、首个括号之前之片段（见 §2-2）。
6. **仪器之限（如实登记）**：① 判别式为**语汇式**匹配 ⇒ 若另有判定件**未在首 16,000 字节内自载件性质**，本棒检不出；② 树内落款**未检出 353 件**，故口径丙既漏检又假阳；③ 本棒**未逐件开卷**全部候选件之正文（仅逐件开卷 9 已审件 ＋ 口径乙之代表件）。
7. **仪器之失-5（自指假阳）**：本件落盘后复扫时，**本件自身**（`_gate3_judgement_set_closure_2026_10_23.md`）因「件性质」栏含「判定件全集口径封口登记件」而被口径乙之判别式**误召为判定件**——而本件自载「**不是判定件**」。修法＝**枚举时显式剔除本棒产出件**（本件之观测时点早于其落盘，本不属被枚举面）⇒ 口径乙由 149 件修正为 **148 件**（repo 98 ＋ sub 50）、并集由 568 件修正为 **567 件**。**修仪器不修文本**：本棒 0 因扫描器而改任何既有件一字；本件全部数字以剔除后之值为准。
8. **排除面（明示）**：`.tmp`／`results\.tmp`（暂存面）／`.mavis`／`node_modules`／`__pycache__`／`.git`／`_remote_pullback_2026_10_17`（回捞副本）／仓外两面（**仅计数**）／**本棒产出件本身**（自指假阳之剔除，见上条）。
9. **未跑实验／未测量／未联网／未调 LLM・API／未读 key・`.env`**。

---

## §7 · 逐件清单（全表・机器生成・可复算）

> 📌 下表三段由本棒**同一判别式**机械生成并逐件复算 SHA-12／bytes／mtime；**任何人可复算**。路径前缀 `repo:` ＝ `〔本地路径已脱敏〕`；`sub:` ＝ `〔本地路径已脱敏〕`。

### §7-1 口径甲（落档树）之全表（N ＝ 478）

| # | SHA-12 | bytes | mtime | 仓 | 相对路径 |
|:-:|:--|--:|:--|:--|:--|
| 1 | `fd7b24a75444` | 74,978 | 2026-10-22 02:30:43 | repo | `results/verdict/judgement/_a1_a6_readiness_recheck_2026_10_22.md` |
| 2 | `d6d8c488fc33` | 43,259 | 2026-10-17 22:02:25 | repo | `results/verdict/judgement/_af1_attribution_verdict_2026_10_17.md` |
| 3 | `b3c45b4e2ec0` | 48,208 | 2026-10-17 22:33:28 | repo | `results/verdict/judgement/_af2_5_proof_2026_10_17.md` |
| 4 | `faee80c8b051` | 41,779 | 2026-10-17 22:32:23 | repo | `results/verdict/judgement/_af2_proof_and_grain_scope_effect_2026_10_17.md` |
| 5 | `14e4181c5b69` | 54,092 | 2026-10-17 23:11:41 | repo | `results/verdict/judgement/_af_complete_landing_effect_2026_10_17.md` |
| 6 | `525ae85c1bbc` | 39,994 | 2026-10-17 20:54:54 | repo | `results/verdict/judgement/_af_entity_rules_2026_10_17.md` |
| 7 | `dc5ee48e1f53` | 45,096 | 2026-10-17 22:16:05 | repo | `results/verdict/judgement/_af_flip要件消解_rulings_effect_2026_10_17.md` |
| 8 | `ce0a2847ad4e` | 43,731 | 2026-10-17 21:09:02 | repo | `results/verdict/judgement/_af_rules_approval_effect_2026_10_17.md` |
| 9 | `8e1b7d6ae996` | 50,703 | 2026-10-17 20:43:49 | repo | `results/verdict/judgement/_approval_card_four_rulings_effect_2026_10_17.md` |
| 10 | `215f89a0c461` | 13,861 | 2026-10-20 13:22:02 | repo | `results/verdict/judgement/_arxiv_2609_09001_metadata_snapshot_2026_10_20.md` |
| 11 | `7c1f8a704f83` | 33,046 | 2026-10-13 21:57:15 | repo | `results/verdict/judgement/_b0_sixty_items_location_list_2026_10_13.md` |
| 12 | `f050e5aff611` | 14,233 | 2026-10-12 22:13:16 | repo | `results/verdict/judgement/_b4_alternative_deliberation_judgment_2026_10_12.md` |
| 13 | `3adfa261bab9` | 37,605 | 2026-10-14 02:14:14 | repo | `results/verdict/judgement/_b_tier_five_subitems_draft_2026_10_14.md` |
| 14 | `c6367741737a` | 52,147 | 2026-10-21 23:56:56 | repo | `results/verdict/judgement/_backfill_verification_2026_10_21.md` |
| 15 | `f1e9d439b04d` | 32,458 | 2026-10-14 11:19:13 | repo | `results/verdict/judgement/_batch10_deliberation_judgment_2026_10_14.md` |
| 16 | `70b50503a32e` | 25,153 | 2026-10-14 14:51:15 | repo | `results/verdict/judgement/_batch11_deliberation_judgment_2026_10_14.md` |
| 17 | `10a3b36859d7` | 140,713 | 2026-10-18 16:58:40 | repo | `results/verdict/judgement/_batch3_execution_receipt_kimi_2026_10_18.md` |
| 18 | `a1ad238879ad` | 46,325 | 2026-10-13 22:19:26 | repo | `results/verdict/judgement/_batch5_deliberation_judgment_2026_10_13.md` |
| 19 | `a41332378c56` | 29,421 | 2026-10-13 22:50:27 | repo | `results/verdict/judgement/_batch6_deliberation_judgment_2026_10_13.md` |
| 20 | `a68b2971b8e1` | 49,012 | 2026-10-14 00:52:15 | repo | `results/verdict/judgement/_batch8_deliberation_judgment_2026_10_14.md` |
| 21 | `3db40bac2267` | 28,935 | 2026-10-12 17:50:24 | repo | `results/verdict/judgement/_bd_fixes_summary_2026_10_12.md` |
| 22 | `4125ea2b2f82` | 80,157 | 2026-10-21 21:11:31 | repo | `results/verdict/judgement/_buexp_backfill_deliberation_2026_10_21.md` |
| 23 | `2c3f48e111cc` | 15,499 | 2026-10-12 17:01:19 | repo | `results/verdict/judgement/_c1_u5_ruling_register_2026_10_12.md` |
| 24 | `f1ca2c59bed9` | 37,908 | 2026-10-12 17:10:11 | repo | `results/verdict/judgement/_c4_rejection_axis_reconciliation_judgment_2026_10_12.md` |
| 25 | `b28540b999a6` | 29,510 | 2026-10-12 17:32:00 | repo | `results/verdict/judgement/_c4_scope_ruling_and_d1_requalification_register_2026_10_12.md` |
| 26 | `91fe9a16059d` | 24,464 | 2026-10-17 16:18:36 | repo | `results/verdict/judgement/_c5_both_pillars_closed_effect_2026_10_17.md` |
| 27 | `c9e304e43274` | 28,902 | 2026-10-17 15:21:56 | repo | `results/verdict/judgement/_c5_split_into_c5a_c5b_2026_10_17.md` |
| 28 | `660555b9b6be` | 26,218 | 2026-10-17 16:04:06 | repo | `results/verdict/judgement/_c5b_closure_verdict_2026_10_17.md` |
| 29 | `36d18da70a95` | 50,836 | 2026-10-21 18:47:11 | repo | `results/verdict/judgement/_c7_naming_deliberation_2026_10_21.md` |
| 30 | `1b45571bddca` | 14,502 | 2026-10-16 21:42:29 | repo | `results/verdict/judgement/_canonical_face_scope_corrigendum_2026_10_16.md` |
| 31 | `a694e5d55ce1` | 26,682 | 2026-10-17 16:48:10 | repo | `results/verdict/judgement/_card_register_dir_verdict_2026_10_17.md` |
| 32 | `17cf0d59cd7b` | 34,948 | 2026-10-10 23:35:41 | repo | `results/verdict/judgement/_chd_construction_domain_declaration_draft_2026_10_10.md` |
| 33 | `7c20c38c501d` | 68,731 | 2026-10-17 11:34:33 | repo | `results/verdict/judgement/_citation_corrigenda_volume_2026_10_17.md` |
| 34 | `536a3064ad38` | 49,332 | 2026-10-17 13:22:41 | repo | `results/verdict/judgement/_citation_no_utility_caliber_draft_2026_10_17.md` |
| 35 | `688fbbc3aa6b` | 28,851 | 2026-10-12 03:27:25 | repo | `results/verdict/judgement/_closeout_bucket_refresh_2026_10_09.md` |
| 36 | `31a03b8d756b` | 121,848 | 2026-10-18 13:34:34 | repo | `results/verdict/judgement/_closure_sweep_r2_2026_10_18.md` |
| 37 | `9c05d0ab78d5` | 53,759 | 2026-10-18 14:14:54 | repo | `results/verdict/judgement/_cluster_a_sface_adjudication_2026_10_18.md` |
| 38 | `479e28afba53` | 82,049 | 2026-10-18 14:38:14 | repo | `results/verdict/judgement/_cluster_abc_pack_adoption_effect_2026_10_18.md` |
| 39 | `3f34fd241a50` | 72,984 | 2026-10-18 14:14:50 | repo | `results/verdict/judgement/_cluster_b_carrier_adjudication_2026_10_18.md` |
| 40 | `8e9ec9104a1e` | 63,462 | 2026-10-18 14:20:41 | repo | `results/verdict/judgement/_cluster_c_keyface_adjudication_2026_10_18.md` |
| 41 | `edcc23114b18` | 57,929 | 2026-10-18 14:36:02 | repo | `results/verdict/judgement/_cluster_d_counting_adjudication_2026_10_18.md` |
| 42 | `d85a8101aa12` | 68,478 | 2026-10-18 17:59:24 | repo | `results/verdict/judgement/_cluster_dfghi_pack_adoption_effect_2026_10_18.md` |
| 43 | `e289d12fd5d4` | 52,226 | 2026-10-18 14:37:14 | repo | `results/verdict/judgement/_cluster_f_deletion_adjudication_2026_10_18.md` |
| 44 | `918659f9b0f6` | 76,051 | 2026-10-18 14:49:14 | repo | `results/verdict/judgement/_cluster_g_deletion_preconditions_adjudication_2026_10_18.md` |
| 45 | `616e466f4f49` | 61,721 | 2026-10-18 14:49:58 | repo | `results/verdict/judgement/_cluster_h_directory_adjudication_2026_10_18.md` |
| 46 | `98b3ef11e115` | 51,397 | 2026-10-18 19:03:39 | repo | `results/verdict/judgement/_cluster_i_f1_f6_f7_verdict_2026_10_18.md` |
| 47 | `84037fd8d0a6` | 39,529 | 2026-10-18 19:17:45 | repo | `results/verdict/judgement/_cluster_i_f4_f5_evidence_2026_10_18.md` |
| 48 | `53ac8f30556d` | 65,872 | 2026-10-18 14:55:42 | repo | `results/verdict/judgement/_cluster_i_historical_adjudication_2026_10_18.md` |
| 49 | `c62c7fad4afd` | 34,968 | 2026-10-18 22:46:27 | repo | `results/verdict/judgement/_cluster_i_item14_closure_effect_2026_10_18.md` |
| 50 | `d23de0a9e7eb` | 39,751 | 2026-10-18 21:47:42 | repo | `results/verdict/judgement/_cluster_i_item14_closure_verdict_2026_10_18.md` |
| 51 | `e3daf0cd6fb8` | 40,492 | 2026-10-18 19:33:32 | repo | `results/verdict/judgement/_cluster_i_item6_compatibility_adjudication_2026_10_18.md` |
| 52 | `f2802aa63370` | 40,834 | 2026-10-18 20:55:13 | repo | `results/verdict/judgement/_cluster_i_item6_conditions_adjudication_2026_10_18.md` |
| 53 | `b33aae011ca8` | 45,549 | 2026-10-18 21:29:24 | repo | `results/verdict/judgement/_cluster_i_item6_give_values_adjudication_2026_10_18.md` |
| 54 | `b4252f1f736d` | 48,997 | 2026-10-19 14:46:37 | repo | `results/verdict/judgement/_cluster_j_glm_62_adjudication_2026_10_19.md` |
| 55 | `4b1040954064` | 55,977 | 2026-10-19 14:55:07 | repo | `results/verdict/judgement/_cluster_k_eta_blockers_adjudication_2026_10_19.md` |
| 56 | `d13f3ed169e3` | 67,299 | 2026-10-18 09:11:11 | repo | `results/verdict/judgement/_commission_v04_approval_rulings_effect_2026_10_18.md` |
| 57 | `df894c9acc2a` | 104,340 | 2026-10-18 11:02:12 | repo | `results/verdict/judgement/_consolidated_pending_rulings_scroll_2026_10_18.md` |
| 58 | `44021af1d6ff` | 20,247 | 2026-10-18 22:46:27 | repo | `results/verdict/judgement/_construction_change_count_ruling_effect_2026_10_18.md` |
| 59 | `4397d1a16805` | 38,440 | 2026-10-17 16:56:04 | repo | `results/verdict/judgement/_continued_three_rulings_effect_2026_10_17.md` |
| 60 | `d34d769afaca` | 22,894 | 2026-10-17 16:39:11 | repo | `results/verdict/judgement/_copilot_eq_grok_rulings_effect_2026_10_17.md` |
| 61 | `4a89f8d3ddda` | 39,705 | 2026-10-17 16:05:37 | repo | `results/verdict/judgement/_copilot_reply_adoption_effect_2026_10_17.md` |
| 62 | `cb887fda55b5` | 24,101 | 2026-10-18 23:55:09 | repo | `results/verdict/judgement/_count_value_timestamp_mandate_effect_2026_10_18.md` |
| 63 | `dfcda086b498` | 30,800 | 2026-10-18 20:12:12 | repo | `results/verdict/judgement/_coze_v1_v3_core_principle_verification_2026_10_18.md` |
| 64 | `89de292707fb` | 43,038 | 2026-10-18 19:16:56 | repo | `results/verdict/judgement/_coze_v5_r2_residual4_adjudication_2026_10_18.md` |
| 65 | `f688f21015e0` | 40,381 | 2026-10-18 19:49:18 | repo | `results/verdict/judgement/_coze_v5_r2_residual4_adoption_effect_2026_10_18.md` |
| 66 | `e67ebccc82c9` | 19,740 | 2026-10-01 14:06:32 | repo | `results/verdict/judgement/_cpath_e3_sign_normalization_2026_10_01.md` |
| 67 | `840fbf08caf4` | 21,061 | 2026-10-10 12:10:50 | repo | `results/verdict/judgement/_d05_b_coincidence_checks_exec_2026_10_10.md` |
| 68 | `ffea29afd4d8` | 44,643 | 2026-10-20 20:21:34 | repo | `results/verdict/judgement/_d13_eta_parts_1to4_caliber_2026_10_20.md` |
| 69 | `9c75e1d4cd76` | 54,962 | 2026-10-21 10:45:20 | repo | `results/verdict/judgement/_d13_rename_candidates_2026_10_21.md` |
| 70 | `88c2af72ff7b` | 46,542 | 2026-10-15 14:52:50 | repo | `results/verdict/judgement/_d1_ab_deliberation_judgment_2026_10_15.md` |
| 71 | `42a3858976f2` | 42,115 | 2026-10-14 14:07:09 | repo | `results/verdict/judgement/_d1_backfill_intake_verdict_2026_10_01.md` |
| 72 | `579b375e9508` | 24,833 | 2026-09-30 13:14:41 | repo | `results/verdict/judgement/_d8_supplement_open_questions_2026_09_30.md` |
| 73 | `5bc372de9a84` | 120,723 | 2026-10-17 10:18:20 | repo | `results/verdict/judgement/_dangling_630_remediation_list_2026_10_17.md` |
| 74 | `debce2c6d3cb` | 80,302 | 2026-10-21 16:01:08 | repo | `results/verdict/judgement/_deliverable_pack_manifest_2026_10_21.md` |
| 75 | `7ae0efbb777d` | 57,693 | 2026-10-21 16:47:56 | repo | `results/verdict/judgement/_deliverable_pack_v2_manifest_2026_10_21.md` |
| 76 | `4eee36e8d339` | 46,947 | 2026-10-21 11:49:44 | repo | `results/verdict/judgement/_den16_alias_table_revision_2026_10_21.md` |
| 77 | `7c3166071a5c` | 92,103 | 2026-10-21 14:55:25 | repo | `results/verdict/judgement/_den16_rename_prefix_candidates_2026_10_21.md` |
| 78 | `9c65f1db6202` | 14,265 | 2026-10-19 20:48:28 | repo | `results/verdict/judgement/_deposon_full_history_main_2026_10_19.md` |
| 79 | `a572747a2001` | 45,958 | 2026-10-19 19:10:24 | repo | `results/verdict/judgement/_deposon_full_history_sub_2026_10_19.md` |
| 80 | `033365d7a549` | 56,375 | 2026-10-21 15:53:49 | repo | `results/verdict/judgement/_dnm16_alias_table_revision_v2_2026_10_21.md` |
| 81 | `4b75ecbace2e` | 77,827 | 2026-10-18 21:47:04 | repo | `results/verdict/judgement/_domain_backfill_235_401_mapping_2026_10_18.md` |
| 82 | `86a4fedebbbc` | 21,793 | 2026-10-18 22:46:27 | repo | `results/verdict/judgement/_domain_backfill_401_v2_caliber_effect_2026_10_18.md` |
| 83 | `c190c54b2f04` | 23,336 | 2026-10-18 21:30:14 | repo | `results/verdict/judgement/_domain_backfill_caliber_fix_draft_2026_10_18.md` |
| 84 | `43515db69b4c` | 39,456 | 2026-10-18 20:54:48 | repo | `results/verdict/judgement/_domain_backfill_hold235_adjudication_2026_10_18.md` |
| 85 | `fc9683f63afe` | 1,394 | 2026-10-18 15:29:49 | repo | `results/verdict/judgement/_domain_backfill_rulings_effect_2026_10_18.md` |
| 86 | `1fe936ee5f67` | 35,064 | 2026-10-22 00:15:46 | repo | `results/verdict/judgement/_e07_deliberation_2026_10_22.md` | 【已审】
| 87 | `a8842f8047a8` | 52,692 | 2026-10-22 01:50:28 | repo | `results/verdict/judgement/_e_family_five_face_resolvability_2026_10_22.md` |
| 88 | `fc7989bba72e` | 45,856 | 2026-10-22 14:10:07 | repo | `results/verdict/judgement/_eight_hard_gaps_crossout_2026_10_22.md` |
| 89 | `718812ed542e` | 32,353 | 2026-10-22 02:20:28 | repo | `results/verdict/judgement/_eight_hard_gaps_enum_diff_2026_10_22.md` |
| 90 | `6aab999b02ac` | 41,388 | 2026-10-17 16:12:54 | repo | `results/verdict/judgement/_erratum_3_14H_caliber_impact_2026_10_17.md` |
| 91 | `45452ccac4ac` | 19,052 | 2026-10-17 17:05:14 | repo | `results/verdict/judgement/_erratum_arm_label_transcription_2026_10_17.md` |
| 92 | `198126e7ef6e` | 5,639 | 2026-10-17 14:38:04 | repo | `results/verdict/judgement/_erratum_refonly_draft_alias_found_2026_10_17.md` |
| 93 | `509e52734292` | 28,717 | 2026-10-17 19:03:44 | repo | `results/verdict/judgement/_esc3_esc6_resolution_2026_10_17.md` |
| 94 | `e550e344a258` | 34,206 | 2026-10-17 19:50:36 | repo | `results/verdict/judgement/_esc5_adoption_and_ritt_remeasure_effect_2026_10_17.md` |
| 95 | `d970bb175672` | 27,258 | 2026-10-17 19:36:24 | repo | `results/verdict/judgement/_esc5_verdict_2026_10_17.md` |
| 96 | `56760f30332b` | 83,989 | 2026-10-20 09:42:40 | repo | `results/verdict/judgement/_eta_construct_c1_c16_recommendation_2026_10_20.md` |
| 97 | `57efdf5255ee` | 27,703 | 2026-10-19 15:52:50 | repo | `results/verdict/judgement/_eta_missing_params_and_c1_adjudication_2026_10_19.md` |
| 98 | `31ce1f43d18f` | 26,537 | 2026-10-19 17:49:28 | repo | `results/verdict/judgement/_eta_missing_params_literature_evidence_2026_10_19.md` |
| 99 | `a79b0ca9ce9e` | 32,594 | 2026-10-18 08:53:44 | repo | `results/verdict/judgement/_eta_preexp_wait_and_leveling_effect_2026_10_18.md` |
| 100 | `2383be56f28f` | 68,943 | 2026-10-20 15:46:17 | repo | `results/verdict/judgement/_eta_sep_caliber_draft_2026_10_20.md` |
| 101 | `585a30bf9f54` | 37,061 | 2026-10-20 16:23:53 | repo | `results/verdict/judgement/_eta_sep_measurement_recalc_2026_10_20.md` |
| 102 | `9f86cc5be8e9` | 26,519 | 2026-10-10 10:33:13 | repo | `results/verdict/judgement/_exp06_supplement_four_gaps_2026_10_10.md` |
| 103 | `aacb2ae8a9f5` | 35,161 | 2026-10-22 00:07:46 | repo | `results/verdict/judgement/_exp8_bar_b_wf_candidates_2026_10_21.md` |
| 104 | `1de82ef76e16` | 37,932 | 2026-10-19 15:14:19 | repo | `results/verdict/judgement/_experiment_face_scope_column1_supplement_draft_2026_10_19.md` |
| 105 | `3fdd7f38b124` | 27,727 | 2026-10-19 13:47:00 | repo | `results/verdict/judgement/_experiment_face_scope_list_draft_2026_10_19.md` |
| 106 | `80a81bd525d4` | 63,647 | 2026-10-17 18:39:47 | repo | `results/verdict/judgement/_ext5_verdict_2026_10_17.md` |
| 107 | `9c0427685a19` | 12,661 | 2026-10-15 10:20:26 | repo | `results/verdict/judgement/_f12_kd_disposition_register_2026_10_15.md` |
| 108 | `56ed8250525b` | 51,428 | 2026-10-19 22:36:35 | repo | `results/verdict/judgement/_f3_payment_vector_reconstruction_2026_10_19.md` |
| 109 | `d716cd3f1240` | 48,898 | 2026-10-19 22:55:24 | repo | `results/verdict/judgement/_f3_payment_vector_third_party_recalc_2026_10_19.md` |
| 110 | `fd4ec7559342` | 40,301 | 2026-10-11 14:05:56 | repo | `results/verdict/judgement/_f4_direction1_domain_effectivity_2026_10_11.md` |
| 111 | `f794107e790a` | 21,682 | 2026-10-19 13:44:13 | repo | `results/verdict/judgement/_f7d_today_no_open_erratum_2026_10_19.md` |
| 112 | `0fd3788e2d3b` | 37,604 | 2026-10-17 20:30:56 | repo | `results/verdict/judgement/_face_r_coexist_verdict_2026_10_17.md` |
| 113 | `c8794d87b4b6` | 41,481 | 2026-10-17 18:26:55 | repo | `results/verdict/judgement/_fail_h0_verdict_2026_10_17.md` |
| 114 | `23bf57ed06dd` | 40,192 | 2026-10-21 18:30:37 | repo | `results/verdict/judgement/_fake_kd_closeout_register_2026_10_21.md` |
| 115 | `b6221e7a2efe` | 83,606 | 2026-10-21 11:21:17 | repo | `results/verdict/judgement/_fake_kd_itemwise_adjudication_2026_10_21.md` |
| 116 | `9c09cc70b339` | 72,909 | 2026-10-21 15:33:33 | repo | `results/verdict/judgement/_fake_kd_p3_readjudication_2026_10_21.md` |
| 117 | `e78092e45065` | 97,074 | 2026-10-21 15:08:17 | repo | `results/verdict/judgement/_fake_kd_p4_reversal_adjudication_2026_10_21.md` |
| 118 | `6addfa5db8e9` | 64,697 | 2026-10-21 13:29:21 | repo | `results/verdict/judgement/_fake_kd_p5_reversal_adjudication_2026_10_21.md` |
| 119 | `af506d37e00a` | 71,937 | 2026-10-21 14:53:57 | repo | `results/verdict/judgement/_fake_kd_p6_confirmation_adjudication_2026_10_21.md` |
| 120 | `7a0dd145a76d` | 68,956 | 2026-10-21 14:04:41 | repo | `results/verdict/judgement/_fake_kd_p8_confirmation_adjudication_2026_10_21.md` |
| 121 | `41d7b76ea4d6` | 40,957 | 2026-09-30 17:25:45 | repo | `results/verdict/judgement/_fake_verdict_reverify_sixitem_ledger_2026_09_30.md` |
| 122 | `7d67b6af125a` | 78,861 | 2026-10-14 02:26:22 | repo | `results/verdict/judgement/_family_de_stale_refresh_matrix_2026_10_14.md` |
| 123 | `55155ec5f430` | 31,151 | 2026-10-14 12:57:58 | repo | `results/verdict/judgement/_family_de_stale_refresh_repo_exec_2026_10_14.md` |
| 124 | `c7d20b3c18ba` | 31,813 | 2026-10-14 11:47:48 | repo | `results/verdict/judgement/_family_de_stale_refresh_sub_exec_2026_10_14.md` |
| 125 | `bbcbac292f8d` | 61,896 | 2026-10-19 15:55:08 | repo | `results/verdict/judgement/_field_table_c6_c8_o5_recommendation_draft_2026_10_19.md` |
| 126 | `9e96d0a1ba12` | 27,315 | 2026-10-10 12:28:00 | repo | `results/verdict/judgement/_five_terminal_judgments_ruling_2026_10_10.md` |
| 127 | `193d11089327` | 37,035 | 2026-10-18 09:40:48 | repo | `results/verdict/judgement/_five_zero_recheck_evidence_2026_10_18.md` |
| 128 | `bfb9a022e3e6` | 64,238 | 2026-10-22 02:12:49 | repo | `results/verdict/judgement/_four_face_deliberation_2026_10_22.md` |
| 129 | `1e512ea146d3` | 41,068 | 2026-10-17 23:35:48 | repo | `results/verdict/judgement/_freeze_face_four_rulings_effect_2026_10_17.md` |
| 130 | `ab1a07ae2fd1` | 32,815 | 2026-10-10 18:52:37 | repo | `results/verdict/judgement/_g5_ccp_execution_prereqs_2026_10_10.md` |
| 131 | `7374c29a8d4e` | 37,104 | 2026-10-17 20:30:50 | repo | `results/verdict/judgement/_gamma_taucert_scope_delimitation_2026_10_17.md` |
| 132 | `6630447e5ec7` | 34,667 | 2026-10-15 15:47:25 | repo | `results/verdict/judgement/_gamma_taucert_sourcing_2026_10_15.md` |
| 133 | `b5596dd2abbb` | 35,339 | 2026-10-17 19:05:22 | repo | `results/verdict/judgement/_gap10_four_rulings_effect_2026_10_17.md` |
| 134 | `989f2dc022a5` | 9,043 | 2026-10-19 20:22:09 | repo | `results/verdict/judgement/_gap_and_kd_flip_master_inventory_2026_10_19.md` |
| 135 | `4e190a8eddd3` | 95,154 | 2026-10-22 15:38:14 | repo | `results/verdict/judgement/_gap_l1_59_resolution_recheck_2026_10_22.md` |
| 136 | `9c70140c7b02` | 20,330 | 2026-10-12 22:14:32 | repo | `results/verdict/judgement/_gate1_five_zero_recheck_2026_10_12.md` |
| 137 | `2f27acf42897` | 34,647 | 2026-10-13 00:30:21 | repo | `results/verdict/judgement/_gate1_five_zero_recheck_glm_scope_2026_10_13.md` |
| 138 | `5cf848421c2b` | 36,087 | 2026-10-12 15:33:02 | repo | `results/verdict/judgement/_gate1_gap_three_items_disposition_2026_10_12.md` |
| 139 | `336500609b5c` | 64,097 | 2026-10-21 18:18:01 | repo | `results/verdict/judgement/_ge01_readiness_adjudication_2026_10_21.md` |
| 140 | `f49079f46c2b` | 51,654 | 2026-10-17 16:02:50 | repo | `results/verdict/judgement/_github_suspect_rulings_effect_2026_10_17.md` |
| 141 | `1b07409d441b` | 62,432 | 2026-10-19 13:57:51 | repo | `results/verdict/judgement/_glm_unique_reply_117_triage_2026_10_19.md` |
| 142 | `0291002f749e` | 24,905 | 2026-10-14 12:57:51 | repo | `results/verdict/judgement/_glm_wholepack_irreproducible_erratum_2026_10_14.md` |
| 143 | `c5a58305876a` | 25,705 | 2026-10-15 15:49:09 | repo | `results/verdict/judgement/_h_budget_measurement_exec_2026_10_15.md` |
| 144 | `bfce04eb2745` | 74,275 | 2026-10-21 21:27:57 | repo | `results/verdict/judgement/_h_exact_enum_killline_prereg_2026_10_21.md` |
| 145 | `d187e54cc291` | 61,131 | 2026-10-21 23:04:35 | repo | `results/verdict/judgement/_h_exact_enum_trace_2026_10_21.md` |
| 146 | `3aa3bcc56258` | 28,087 | 2026-10-18 12:03:46 | repo | `results/verdict/judgement/_h_face_freeze_ruling_effect_2026_10_18.md` |
| 147 | `b7d638ebef6e` | 21,741 | 2026-10-17 23:36:19 | repo | `results/verdict/judgement/_harness_mask_correct_value_validation_2026_10_17.md` |
| 148 | `19b73ab478f5` | 34,941 | 2026-10-18 10:04:12 | repo | `results/verdict/judgement/_historical_ forgetting_recheck_2026_10_18.md` |
| 149 | `f2f1a9be203d` | 43,130 | 2026-10-18 20:38:42 | repo | `results/verdict/judgement/_historical_forgetting_21_status_update_2026_10_18.md` |
| 150 | `9adf7d28fe2d` | 52,087 | 2026-10-19 18:24:38 | repo | `results/verdict/judgement/_independent_review_history_gaps_kd_2026_10_19_sub.md` |
| 151 | `4d2c65968311` | 34,256 | 2026-10-16 13:57:41 | repo | `results/verdict/judgement/_interval_420_600_upper_bound_deliberation_2026_10_16.md` |
| 152 | `fce2f69802b9` | 46,687 | 2026-10-16 16:53:10 | repo | `results/verdict/judgement/_interval_ceiling_post_lock_deliberation_2026_10_16.md` |
| 153 | `df61b2798ecb` | 23,201 | 2026-10-18 21:58:57 | repo | `results/verdict/judgement/_item6_c2_card_reference_registration_2026_10_18.md` |
| 154 | `a40de66d87c8` | 50,802 | 2026-10-18 22:35:39 | repo | `results/verdict/judgement/_item6_c2_four_fields_adjudication_2026_10_18.md` |
| 155 | `42ead18967d9` | 40,889 | 2026-10-18 23:01:22 | repo | `results/verdict/judgement/_item6_c2_four_fields_adoption_effect_2026_10_18.md` |
| 156 | `f5bad2e2ff00` | 42,968 | 2026-10-17 14:16:06 | repo | `results/verdict/judgement/_judgement_criteria_reference_only_no_utility_draft_2026_10_17.md` |
| 157 | `f35fe7d03551` | 54,862 | 2026-10-23 12:29:07 | repo | `results/verdict/judgement/_judgement_w39_two_reading_2026_10_23.md` |
| 158 | `09aea8d27041` | 50,919 | 2026-10-21 11:28:29 | repo | `results/verdict/judgement/_kabla6_trigger_review_adjudication_2026_10_21.md` |
| 159 | `8f2025e9de6f` | 24,527 | 2026-10-10 11:27:33 | repo | `results/verdict/judgement/_kd04_c_denominator_killline_prereg_2026_10_10.md` |
| 160 | `99b578a1be2c` | 32,067 | 2026-10-15 11:46:36 | repo | `results/verdict/judgement/_kd13_ecr_anchor_binding_deliberation_2026_10_15.md` |
| 161 | `0a6279970446` | 35,608 | 2026-10-16 22:20:08 | repo | `results/verdict/judgement/_kd14_null_u_carrier_deliberation_2026_10_16.md` |
| 162 | `141816a6aec9` | 24,828 | 2026-10-16 22:40:00 | repo | `results/verdict/judgement/_kd14_null_u_carrier_effect_register_2026_10_16.md` |
| 163 | `351d18d74934` | 27,149 | 2026-10-17 19:23:16 | repo | `results/verdict/judgement/_kd1_preexp_contrast_2026_10_17.md` |
| 164 | `ce1604dfd251` | 32,577 | 2026-10-17 17:09:35 | repo | `results/verdict/judgement/_kd4_adoption_and_caliber_pack_effect_2026_10_17.md` |
| 165 | `1992b9d359a8` | 32,823 | 2026-10-17 16:54:31 | repo | `results/verdict/judgement/_kd4_homology_verdict_2026_10_17.md` |
| 166 | `807932c7e1c8` | 18,606 | 2026-10-16 20:52:09 | repo | `results/verdict/judgement/_kd_11_12_resolution_register_2026_10_16.md` |
| 167 | `410f885430a4` | 19,461 | 2026-10-16 22:19:45 | repo | `results/verdict/judgement/_kd_13_9_3_closure_register_2026_10_16.md` |
| 168 | `0fd67a2075b7` | 20,497 | 2026-10-16 21:38:38 | repo | `results/verdict/judgement/_kd_2_4_6_caliber_note_2026_10_16.md` |
| 169 | `040338b4940c` | 27,186 | 2026-10-18 23:55:09 | repo | `results/verdict/judgement/_kd_civ_closure_effect_2026_10_18.md` |
| 170 | `60e9a18fa428` | 43,116 | 2026-10-18 23:16:13 | repo | `results/verdict/judgement/_kd_civ_closure_verdict_2026_10_18.md` |
| 171 | `d87a711b0ecf` | 113,327 | 2026-10-19 22:54:59 | repo | `results/verdict/judgement/_kd_cluster_verdict_pack_adjudication_2026_10_19.md` |
| 172 | `522be8905484` | 77,119 | 2026-10-20 11:09:45 | repo | `results/verdict/judgement/_kd_crw2_beta_and_t4n05_domain_adjudication_2026_10_20.md` |
| 173 | `85e5caeb3478` | 73,955 | 2026-10-19 20:18:28 | repo | `results/verdict/judgement/_kd_epw3_crw3_ffrep1_adjudication_2026_10_19.md` |
| 174 | `b9ba3ff8d010` | 74,163 | 2026-10-21 17:30:08 | repo | `results/verdict/judgement/_kd_esc5v2_closure_adjudication_2026_10_21.md` |
| 175 | `8a5727bc4c11` | 64,606 | 2026-10-20 14:34:17 | repo | `results/verdict/judgement/_kd_eta_main_run_verdict_2026_10_20.md` |
| 176 | `80b8cafcd085` | 37,788 | 2026-10-20 12:22:23 | repo | `results/verdict/judgement/_kd_eta_selection_verdict_2026_10_20.md` |
| 177 | `ceb71b3a2570` | 66,712 | 2026-10-20 16:22:28 | repo | `results/verdict/judgement/_kd_eta_sep_measurement_verdict_2026_10_20.md` |
| 178 | `77bc92c9d227` | 85,265 | 2026-10-20 22:03:50 | repo | `results/verdict/judgement/_kd_false9_remedy_proposals_2026_10_20.md` |
| 179 | `97ac680345ac` | 76,664 | 2026-10-20 23:11:21 | repo | `results/verdict/judgement/_kd_false9_wave0_calibers_2026_10_20.md` |
| 180 | `229741fc1629` | 456,231 | 2026-10-22 01:57:59 | repo | `results/verdict/judgement/_kd_flip_candidates_2026_10_22.md` |
| 181 | `10e40a51c9c1` | 38,813 | 2026-10-17 20:15:17 | repo | `results/verdict/judgement/_kd_gap_resolution_rulings_effect_2026_10_17.md` |
| 182 | `592a50470e76` | 45,716 | 2026-10-17 20:01:00 | repo | `results/verdict/judgement/_kd_gap_survey_2026_10_17.md` |
| 183 | `731144fbda94` | 26,411 | 2026-10-16 23:36:54 | repo | `results/verdict/judgement/_kd_ge01_eps4_scope_escalation_note_2026_10_16.md` |
| 184 | `42ea79ea3f06` | 72,915 | 2026-10-20 12:20:40 | repo | `results/verdict/judgement/_kd_h1_h7_disposition_draft_2026_10_20.md` |
| 185 | `7eefedd92808` | 51,557 | 2026-10-19 23:41:00 | repo | `results/verdict/judgement/_kd_h1_h7_hidden_gaps_register_2026_10_19.md` |
| 186 | `b17b642f1183` | 54,662 | 2026-10-20 14:27:25 | repo | `results/verdict/judgement/_kd_h1_lineage_declaration_2026_10_20.md` |
| 187 | `a23dfaf20278` | 39,377 | 2026-10-20 14:35:00 | repo | `results/verdict/judgement/_kd_h2_anchor_chain_erratum_2026_10_20.md` |
| 188 | `15d1279d1638` | 47,335 | 2026-10-20 14:27:44 | repo | `results/verdict/judgement/_kd_h4_fingerprint_reanchor_register_2026_10_20.md` |
| 189 | `d9459768e058` | 22,205 | 2026-10-14 02:00:49 | repo | `results/verdict/judgement/_kd_h5_h6_recheck_2026_10_14.md` |
| 190 | `8db6f947bf98` | 55,674 | 2026-10-20 14:45:38 | repo | `results/verdict/judgement/_kd_h5_session_history_domain_caliber_2026_10_20.md` |
| 191 | `30a6398b1e2e` | 1,000,949 | 2026-10-20 16:12:12 | repo | `results/verdict/judgement/_kd_h5_session_history_pilot_1of10_2026_10_20.md` |
| 192 | `9e853e0f259b` | 68,036 | 2026-10-20 14:53:25 | repo | `results/verdict/judgement/_kd_h6_caliber_mapping_adjudication_2026_10_20.md` |
| 193 | `fce088063dbd` | 56,575 | 2026-10-19 23:16:25 | repo | `results/verdict/judgement/_kd_history_pack_adjudication_2026_10_19.md` |
| 194 | `609943436a0d` | 73,752 | 2026-10-20 23:28:12 | repo | `results/verdict/judgement/_kd_identified_defect_attribution_caliber_2026_10_20.md` |
| 195 | `b666077233c5` | 73,620 | 2026-10-19 20:18:15 | repo | `results/verdict/judgement/_kd_mda8_arm2_kill_line_freeze_draft_2026_10_19.md` |
| 196 | `30e47f1181d3` | 92,280 | 2026-10-19 21:12:24 | repo | `results/verdict/judgement/_kd_mda8_arm2_remaining11_recommendation_2026_10_19.md` |
| 197 | `42af8a6e0703` | 65,988 | 2026-10-19 21:16:41 | repo | `results/verdict/judgement/_kd_mda8_domain_readings_adjudication_2026_10_19.md` |
| 198 | `9a960a574260` | 57,571 | 2026-10-19 21:36:01 | repo | `results/verdict/judgement/_kd_mda8_f1_two_senses_adjudication_2026_10_19.md` |
| 199 | `9c75b5c16676` | 64,345 | 2026-10-20 11:48:37 | repo | `results/verdict/judgement/_kd_mda8_first_reading_verdict_2026_10_20.md` |
| 200 | `ebe106d2da47` | 95,664 | 2026-10-19 22:43:03 | repo | `results/verdict/judgement/_kd_mda8_gate_resolution_and_new_exp_draft_2026_10_19.md` |
| 201 | `8a77b155fd64` | 80,642 | 2026-10-19 22:11:00 | repo | `results/verdict/judgement/_kd_mda8_preexp_dispatch_spec_draft_2026_10_19.md` |
| 202 | `242b7ea98eb7` | 69,095 | 2026-10-19 23:04:43 | repo | `results/verdict/judgement/_kd_mda8_spec_rest_recommendation_2026_10_19.md` |
| 203 | `170ab543d941` | 77,696 | 2026-10-20 23:18:42 | repo | `results/verdict/judgement/_kd_mda8a24_clearance_verdict_2026_10_20.md` |
| 204 | `b6f3a254abb1` | 75,087 | 2026-10-21 16:14:42 | repo | `results/verdict/judgement/_kd_mda9_closure_adjudication_2026_10_21.md` |
| 205 | `5c4fd13640f4` | 26,395 | 2026-10-16 21:26:56 | repo | `results/verdict/judgement/_kd_s3_2_3_corrigendum_2026_10_16.md` |
| 206 | `e09780d24a7a` | 49,252 | 2026-10-17 19:42:40 | repo | `results/verdict/judgement/_kd_s3b1_kd1_n7_rulings_effect_2026_10_17.md` |
| 207 | `ed36d0171672` | 45,846 | 2026-10-17 19:22:50 | repo | `results/verdict/judgement/_kd_s3b1_verdict_2026_10_17.md` |
| 208 | `3ecf179b83a1` | 48,246 | 2026-10-17 19:25:20 | repo | `results/verdict/judgement/_kd_s3b5_kd1_esc36_batch_lock_effect_2026_10_17.md` |
| 209 | `c013aeb1235f` | 70,518 | 2026-10-20 22:00:56 | repo | `results/verdict/judgement/_kd_sepcal7_final_verdict_2026_10_20.md` |
| 210 | `6415eb480659` | 50,348 | 2026-10-22 01:58:01 | repo | `results/verdict/judgement/_kd_t5k5_stale_premise_adjudication_2026_10_22.md` |
| 211 | `b69092972467` | 43,097 | 2026-10-21 11:39:27 | repo | `results/verdict/judgement/_kd_two_gates_boundary_adoption_2026_10_21.md` |
| 212 | `0ef78a26f637` | 41,462 | 2026-10-21 10:44:36 | repo | `results/verdict/judgement/_kd_two_gates_boundary_proposal_2026_10_21.md` |
| 213 | `45f1ea5e5b23` | 45,929 | 2026-10-20 23:51:08 | repo | `results/verdict/judgement/_kd_two_gates_comparison_2026_10_20.md` |
| 214 | `4500a4715f3b` | 30,072 | 2026-10-17 19:13:53 | repo | `results/verdict/judgement/_kd_u1_u4_rulings_effect_2026_10_17.md` |
| 215 | `85702808df0c` | 38,534 | 2026-10-17 19:22:09 | repo | `results/verdict/judgement/_kd_u5_u6_s3b4_rulings_effect_2026_10_17.md` |
| 216 | `751205f0368f` | 24,961 | 2026-10-17 23:59:20 | repo | `results/verdict/judgement/_kd_u6_readside_rewire_validation_2026_10_17.md` |
| 217 | `f22ede7226d2` | 24,898 | 2026-10-10 11:36:58 | repo | `results/verdict/judgement/_kd_unambiguous_meaning_ruling_2026_10_10.md` |
| 218 | `f47031323865` | 20,179 | 2026-10-14 12:55:36 | repo | `results/verdict/judgement/_kd_writing_convention_guidance_2026_10_09.md` |
| 219 | `4fdadf27b70c` | 26,107 | 2026-10-17 23:05:58 | repo | `results/verdict/judgement/_kdb2r2_kd14_merge_governance_2026_10_17.md` |
| 220 | `688424929409` | 35,207 | 2026-10-17 18:58:09 | repo | `results/verdict/judgement/_kdb2r3_u13_rulings_effect_2026_10_17.md` |
| 221 | `53c49723b973` | 34,769 | 2026-10-22 14:59:21 | repo | `results/verdict/judgement/_kdcensus_derived_summary_2026_10_22.md` |
| 222 | `25ff6e4f31bc` | 31,662 | 2026-10-17 20:17:26 | repo | `results/verdict/judgement/_kdk45_remeasure_2026_10_17.md` |
| 223 | `80631fb4ce3d` | 62,301 | 2026-10-22 01:26:04 | repo | `results/verdict/judgement/_kexp8_coverage_adjudication_2026_10_22.md` | 【已审】
| 224 | `591b73224eee` | 48,993 | 2026-10-19 17:19:05 | repo | `results/verdict/judgement/_kfp6_nature_and_eta_expface_adjudication_2026_10_19.md` |
| 225 | `e40b7335a0ca` | 1,631 | 2026-10-19 13:06:53 | repo | `results/verdict/judgement/_kickoff_experiment_window_directive_effect_2026_10_19.md` |
| 226 | `e5615b993000` | 19,471 | 2026-10-15 11:42:48 | repo | `results/verdict/judgement/_kill_line_field_value_sourcing_2026_10_15.md` |
| 227 | `d51ff0c7776d` | 21,678 | 2026-10-18 12:01:47 | repo | `results/verdict/judgement/_kimi_postexec_receipt_verification_2026_10_18.md` |
| 228 | `7828c5300fdf` | 42,226 | 2026-10-18 10:38:51 | repo | `results/verdict/judgement/_kimi_preexec_final_rulings_effect_2026_10_18.md` |
| 229 | `789fed8aacc7` | 62,860 | 2026-10-18 12:07:34 | repo | `results/verdict/judgement/_kimi_receipt_authority_rulings_effect_2026_10_18.md` |
| 230 | `20a1ce111547` | 36,936 | 2026-10-17 21:31:30 | repo | `results/verdict/judgement/_kl_m41_3_remeasure_2026_10_17.md` |
| 231 | `63625672139a` | 61,667 | 2026-10-17 21:44:34 | repo | `results/verdict/judgement/_kl_m41_3_reverdict_2026_10_17.md` |
| 232 | `27545e411171` | 38,651 | 2026-10-17 21:59:26 | repo | `results/verdict/judgement/_kl_m41_3_reverdict_adoption_effect_2026_10_17.md` |
| 233 | `3e13344783b0` | 41,140 | 2026-10-16 19:43:13 | repo | `results/verdict/judgement/_kl_m41_3_three_seed_exec_2026_10_16.md` |
| 234 | `5dc4e089f458` | 33,138 | 2026-10-17 18:25:11 | repo | `results/verdict/judgement/_kl_m41_3_verdict_2026_10_17.md` |
| 235 | `a467a77d895f` | 45,192 | 2026-10-16 11:55:08 | repo | `results/verdict/judgement/_klm41_2_bootstrap_ci_exec_2026_10_16.md` |
| 236 | `4d514147670a` | 16,648 | 2026-10-12 17:33:16 | repo | `results/verdict/judgement/_krj3_kd_registry_correction_2026_10_12.md` |
| 237 | `af84d38cbfba` | 50,304 | 2026-10-21 17:03:07 | repo | `results/verdict/judgement/_ksepcal9_release_pro_release_text_2026_10_21.md` |
| 238 | `bc397d5099dd` | 42,687 | 2026-10-09 23:10:27 | repo | `results/verdict/judgement/_kv3s_4_4_rejudge_2026_10_09.md` |
| 239 | `ecbf3288d791` | 42,517 | 2026-10-19 15:06:13 | repo | `results/verdict/judgement/_l2_2_duplication_criterion_adjudication_2026_10_19.md` |
| 240 | `84e8d866054a` | 49,080 | 2026-10-19 15:38:11 | repo | `results/verdict/judgement/_l2_2_two_arms_identity_adjudication_2026_10_19.md` |
| 241 | `75a237b09738` | 6,848 | 2026-10-22 01:52:56 | repo | `results/verdict/judgement/_l36_l40_recheck_2026_10_22.md` |
| 242 | `4513f841234e` | 45,462 | 2026-10-16 16:28:16 | repo | `results/verdict/judgement/_m08_measured_enumeration_exec_2026_10_16.md` |
| 243 | `f621f836aa86` | 17,212 | 2026-10-14 10:56:32 | repo | `results/verdict/judgement/_m2_c_tier_corrigendum_2026_10_14.md` |
| 244 | `810e20778e6c` | 21,750 | 2026-10-14 10:24:37 | repo | `results/verdict/judgement/_m2_kd_disposition_2026_10_14.md` |
| 245 | `17fd10488da0` | 31,647 | 2026-10-14 13:00:11 | repo | `results/verdict/judgement/_m2_terminal_verdict_effect_register_2026_10_14.md` |
| 246 | `f54e8a10acde` | 23,630 | 2026-10-15 11:11:34 | repo | `results/verdict/judgement/_m41_verdict_kd_effect_register_2026_10_15.md` |
| 247 | `0c9641e512e4` | 22,700 | 2026-10-14 10:18:35 | repo | `results/verdict/judgement/_m5_reattribution_recommendation_2026_10_14.md` |
| 248 | `6ca1c64c2c44` | 35,966 | 2026-10-16 15:47:16 | repo | `results/verdict/judgement/_material_expansion_build_exec_2026_10_16.md` |
| 249 | `42a0b3aeff96` | 35,655 | 2026-10-16 16:02:24 | repo | `results/verdict/judgement/_material_expansion_verdict_kd_effect_register_2026_10_16.md` |
| 250 | `f2a5c4330112` | 19,477 | 2026-10-17 20:15:44 | repo | `results/verdict/judgement/_material_root45_remeasure_2026_10_17.md` |
| 251 | `121a3b861261` | 58,572 | 2026-10-18 01:35:03 | repo | `results/verdict/judgement/_md_a_field_composition_draft_2026_10_18.md` |
| 252 | `1046dd5d1be0` | 73,898 | 2026-10-20 10:44:13 | repo | `results/verdict/judgement/_mda8_readlaw_o1_o4_c4_recommendation_2026_10_20.md` |
| 253 | `74250c36b502` | 46,658 | 2026-10-22 14:14:17 | repo | `results/verdict/judgement/_mda8a24_armpair_options_2026_10_22.md` |
| 254 | `58727d1eec71` | 55,555 | 2026-10-17 23:36:49 | repo | `results/verdict/judgement/_merge_govern_approval_and_eps1_release_effect_2026_10_17.md` |
| 255 | `9ed6dfdbc62e` | 37,227 | 2026-10-18 01:43:36 | repo | `results/verdict/judgement/_morning_brief_pending_rulings_2026_10_18.md` |
| 256 | `656b2324d598` | 10,795 | 2026-10-15 10:20:26 | repo | `results/verdict/judgement/_mq19_item6_caption_restatement_2026_10_15.md` |
| 257 | `ad8f0d542290` | 16,192 | 2026-10-12 23:09:19 | repo | `results/verdict/judgement/_n2_clause_transcription_supplement_2026_10_12.md` |
| 258 | `88df2c228eae` | 39,037 | 2026-10-16 20:05:26 | repo | `results/verdict/judgement/_n3_o5_terminal_verdict_2026_10_16.md` |
| 259 | `0abaee4aeefb` | 41,028 | 2026-10-17 22:16:42 | repo | `results/verdict/judgement/_n_distinct_grain_verdict_2026_10_17.md` |
| 260 | `2b538eba112a` | 24,241 | 2026-10-17 21:53:53 | repo | `results/verdict/judgement/_n_distinct_proof_2026_10_17.md` |
| 261 | `57024f2cd30a` | 7,843 | 2026-09-29 21:18:08 | repo | `results/verdict/judgement/_naming_ruling_note_2026_09_29.md` |
| 262 | `0a3dedb79479` | 76,725 | 2026-10-21 18:53:59 | repo | `results/verdict/judgement/_ncc_c6_admission_adjudication_2026_10_21.md` |
| 263 | `1c7be88017c7` | 62,358 | 2026-10-21 20:49:45 | repo | `results/verdict/judgement/_ncc_c6_condition4_adjudication_2026_10_21.md` |
| 264 | `0d127134aa97` | 66,029 | 2026-10-21 18:36:12 | repo | `results/verdict/judgement/_ncc_c6_sixpair_measurement_2026_10_21.md` |
| 265 | `2e06217bbe61` | 87,979 | 2026-10-21 19:30:45 | repo | `results/verdict/judgement/_ncc_c6_thirdparty_recalc_2026_10_21.md` |
| 266 | `015b4e200103` | 11,599 | 2026-10-18 09:30:57 | repo | `results/verdict/judgement/_next_stage3_dir_optimization_ruling_2026_10_18.md` |
| 267 | `1dbe20a3ba1c` | 63,091 | 2026-10-14 02:50:08 | repo | `results/verdict/judgement/_night_shift_handover_2026_10_14_r2.md` |
| 268 | `bd748afec4f8` | 53,634 | 2026-10-17 11:23:23 | repo | `results/verdict/judgement/_no_backup_ruling_and_report_caliber_effect_2026_10_17.md` |
| 269 | `3ac146a3f8e5` | 29,489 | 2026-10-17 10:34:39 | repo | `results/verdict/judgement/_noncore_upload_caliber_draft_2026_10_17.md` |
| 270 | `c98d310e183e` | 209,219 | 2026-10-14 02:40:32 | repo | `results/verdict/judgement/_numbering_659_overlap_semantic_review_2026_10_14.md` |
| 271 | `34c1031746fa` | 39,933 | 2026-10-13 17:42:16 | repo | `results/verdict/judgement/_numbering_claims_and_prefix_table_effect_2026_10_13.md` |
| 272 | `7953a89ea015` | 18,487 | 2026-10-13 21:38:53 | repo | `results/verdict/judgement/_numbering_face_recheck_2026_10_13.md` |
| 273 | `fd88b3669676` | 12,578 | 2026-10-13 23:21:43 | repo | `results/verdict/judgement/_numbering_face_signature_supplement_2026_10_13.md` |
| 274 | `c9c808083d46` | 52,216 | 2026-10-16 14:43:51 | repo | `results/verdict/judgement/_o1_498_lock_scope_deliberation_2026_10_16.md` |
| 275 | `941002361d54` | 81,406 | 2026-10-20 19:47:02 | repo | `results/verdict/judgement/_o1_transcription_face_erratum_2026_10_20.md` |
| 276 | `14f2e90cc430` | 60,752 | 2026-10-21 20:06:20 | repo | `results/verdict/judgement/_p3_disposition_deliberation_2026_10_21.md` |
| 277 | `30925758a3c7` | 114,003 | 2026-10-21 23:15:49 | repo | `results/verdict/judgement/_p3_path1_codebook_killline_prereg_2026_10_21.md` |
| 278 | `7fa815bf567d` | 46,371 | 2026-10-17 15:23:47 | repo | `results/verdict/judgement/_pack_card_four_rulings_effect_2026_10_17.md` |
| 279 | `c233e675832e` | 1,582 | 2026-10-19 13:27:11 | repo | `results/verdict/judgement/_pdf_is_coze_reply_ruling_effect_2026_10_19.md` |
| 280 | `9572516d82e7` | 27,925 | 2026-10-17 23:12:28 | repo | `results/verdict/judgement/_pending_pack_four_rulings_effect_2026_10_17.md` |
| 281 | `0f6098f36bd0` | 53,502 | 2026-10-18 13:33:12 | repo | `results/verdict/judgement/_pending_residual_minimal_set_2026_10_18.md` |
| 282 | `19c91a3bf7e8` | 63,300 | 2026-10-18 10:01:37 | repo | `results/verdict/judgement/_pending_rulings_triage_2026_10_18.md` |
| 283 | `37876a02ad17` | 11,798 | 2026-10-12 16:07:48 | repo | `results/verdict/judgement/_pi_batch_rulings_and_gate1_definition_register_2026_10_12.md` |
| 284 | `b99a9f039ecc` | 14,146 | 2026-10-12 10:15:30 | repo | `results/verdict/judgement/_pi_four_rulings_adoption_and_effectivity_2026_10_12.md` |
| 285 | `cfcf430f306c` | 42,707 | 2026-10-17 22:56:19 | repo | `results/verdict/judgement/_poststrip_recalc_2026_10_17.md` |
| 286 | `653505b88a08` | 32,084 | 2026-10-17 11:08:02 | repo | `results/verdict/judgement/_predelete_backup_caliber_draft_2026_10_17.md` |
| 287 | `374be409dc47` | 49,419 | 2026-10-20 19:47:30 | repo | `results/verdict/judgement/_preexp_degen_gate_recalc_2026_10_20.md` |
| 288 | `829e07a7a63b` | 57,997 | 2026-10-20 22:48:17 | repo | `results/verdict/judgement/_preexp_mda8a24_c5_armpairs_measurement_2026_10_20.md` |
| 289 | `c038121c9ad5` | 59,947 | 2026-10-20 22:03:03 | repo | `results/verdict/judgement/_preexp_mda8a24_c5_armpairs_recalc_2026_10_20.md` |
| 290 | `39ffd5e4c47f` | 63,402 | 2026-10-20 20:01:24 | repo | `results/verdict/judgement/_preexp_mda8a24_recalc_2026_10_20.md` |
| 291 | `99b9bff47682` | 43,055 | 2026-10-17 17:04:42 | repo | `results/verdict/judgement/_r2_reading_verdict_2026_10_17.md` |
| 292 | `ed5591c3c38d` | 41,770 | 2026-10-18 09:29:15 | repo | `results/verdict/judgement/_r2_sep_endogeneity_erratum_2026_10_18.md` |
| 293 | `c8f3a36c152b` | 31,009 | 2026-10-17 17:43:26 | repo | `results/verdict/judgement/_r2b_adoption_and_bytewise_caliber_effect_2026_10_17.md` |
| 294 | `b2e0a65f722c` | 19,984 | 2026-10-14 13:13:12 | repo | `results/verdict/judgement/_r6_supplement_first_version_disposition_2026_10_14.md` |
| 295 | `0ad849022328` | 30,352 | 2026-10-09 12:37:13 | repo | `results/verdict/judgement/_r_pair_question_texts_2026_10_09.md` |
| 296 | `ba3944565c13` | 44,360 | 2026-10-17 11:11:23 | repo | `results/verdict/judgement/_recycle_purge_resolution_and_434_adoption_2026_10_17.md` |
| 297 | `7fc20904d015` | 26,214 | 2026-10-17 14:22:21 | repo | `results/verdict/judgement/_ref_only_no_utility_criteria_effect_2026_10_17.md` |
| 298 | `bd94d12323e0` | 39,243 | 2026-10-17 16:13:11 | repo | `results/verdict/judgement/_refonly_161_reading_verdict_2026_10_17.md` |
| 299 | `81c42f70e271` | 27,604 | 2026-10-18 23:17:27 | repo | `results/verdict/judgement/_remote_root_face_413_68_erratum_2026_10_18.md` |
| 300 | `cff53e597044` | 52,696 | 2026-10-18 14:11:46 | repo | `results/verdict/judgement/_residual_card1_four_rulings_effect_2026_10_18.md` |
| 301 | `91555b6b7bd6` | 29,195 | 2026-10-17 20:22:36 | repo | `results/verdict/judgement/_resolution_path_rulings_effect_2026_10_17.md` |
| 302 | `5653b96d93c4` | 274,617 | 2026-10-21 10:23:58 | repo | `results/verdict/judgement/_results_path_mapping_2026_10_21.md` |
| 303 | `a7539659c5df` | 28,232 | 2026-10-17 19:58:52 | repo | `results/verdict/judgement/_ritt_def_adoption_and_remeasure_effect_2026_10_17.md` |
| 304 | `5d411ebf07ed` | 23,310 | 2026-10-17 19:47:26 | repo | `results/verdict/judgement/_ritt_def_proof_2026_10_17.md` |
| 305 | `7e693b27c1f7` | 30,617 | 2026-10-17 22:19:42 | repo | `results/verdict/judgement/_rpp_perseed_recalc_2026_10_17.md` |
| 306 | `03fe4d044c78` | 54,716 | 2026-10-18 10:17:14 | repo | `results/verdict/judgement/_ruled_unclosed_closure_verdict_2026_10_18.md` |
| 307 | `2c1479af62cb` | 28,816 | 2026-10-17 17:45:24 | repo | `results/verdict/judgement/_s3_s5_explanation_and_disposition_verdict_2026_10_17.md` |
| 308 | `eea5245b31da` | 33,609 | 2026-10-17 17:57:09 | repo | `results/verdict/judgement/_s3_s5_kd_effect_2026_10_17.md` |
| 309 | `905be2174c52` | 17,624 | 2026-10-17 18:00:22 | repo | `results/verdict/judgement/_s3_s5_kd_effect_2026_10_17_append1.md` |
| 310 | `84fa6996b656` | 51,073 | 2026-10-10 11:37:23 | repo | `results/verdict/judgement/_s3_th_v21_reconciliation_verdict_2026_10_01.md` |
| 311 | `e7fcbc290a7e` | 53,188 | 2026-10-11 00:29:00 | repo | `results/verdict/judgement/_s3prime_alert_disposition_judgment_2026_10_11.md` |
| 312 | `e4d96a516289` | 39,939 | 2026-10-11 00:15:56 | repo | `results/verdict/judgement/_s3prime_degeneracy_selfcert_2026_10_11.md` |
| 313 | `21f2926efc5d` | 32,975 | 2026-10-09 15:00:52 | repo | `results/verdict/judgement/_s4_final_ruling_effectivity_register_2026_10_09.md` |
| 314 | `fb1b696de1d6` | 35,453 | 2026-10-09 21:26:53 | repo | `results/verdict/judgement/_s4_heldout_sampling_caliber_ruling_2026_10_09.md` |
| 315 | `6269d0c6fd10` | 15,284 | 2026-10-10 13:03:55 | repo | `results/verdict/judgement/_s4_kex_killline_freeze_2026_10_10.md` |
| 316 | `2813eea5584a` | 51,739 | 2026-10-18 11:55:45 | repo | `results/verdict/judgement/_scroll_wave1_four_rulings_effect_2026_10_18.md` |
| 317 | `57881886e428` | 51,949 | 2026-10-18 12:18:01 | repo | `results/verdict/judgement/_scroll_wave2_four_rulings_effect_2026_10_18.md` |
| 318 | `0db1e827d943` | 51,604 | 2026-10-18 12:37:20 | repo | `results/verdict/judgement/_scroll_wave4_three_rulings_effect_2026_10_18.md` |
| 319 | `c44183973483` | 71,453 | 2026-10-18 13:50:56 | repo | `results/verdict/judgement/_scroll_wave5_four_rulings_effect_2026_10_18.md` |
| 320 | `6904852f8ceb` | 26,864 | 2026-10-11 15:36:15 | repo | `results/verdict/judgement/_seed_double_identifier_finalization_2026_10_11.md` |
| 321 | `5bccb1af707d` | 90,488 | 2026-10-21 19:48:53 | repo | `results/verdict/judgement/_stage1_killline_values_proposal_2026_10_21.md` |
| 322 | `60f02aa54930` | 99,794 | 2026-10-21 20:07:53 | repo | `results/verdict/judgement/_stage1_killline_values_proposal_second_reading_2026_10_21.md` |
| 323 | `22843cb2ce08` | 54,315 | 2026-10-18 08:55:10 | repo | `results/verdict/judgement/_stage3_close_and_cmp2_rulings_effect_2026_10_18.md` |
| 324 | `b582bde59d6d` | 18,115 | 2026-10-17 23:33:48 | repo | `results/verdict/judgement/_stage_sequence_ruling_effect_2026_10_17.md` |
| 325 | `d392bd36ec34` | 41,236 | 2026-10-17 18:28:37 | repo | `results/verdict/judgement/_strict3_verdict_2026_10_17.md` |
| 326 | `ee7a1563d850` | 46,503 | 2026-10-16 12:00:22 | repo | `results/verdict/judgement/_supplement_500_combo_exec_2026_10_16.md` |
| 327 | `7fa22aa1addb` | 71,443 | 2026-10-18 14:26:46 | repo | `results/verdict/judgement/_supplemental_sync_commission_rulings_effect_2026_10_18.md` |
| 328 | `8db3f88b5ed0` | 24,708 | 2026-10-09 22:17:22 | repo | `results/verdict/judgement/_t1_exp2_activation_supplement_2026_10_09.md` |
| 329 | `9c18b9893579` | 42,817 | 2026-10-09 18:23:43 | repo | `results/verdict/judgement/_t1_qwen_temp_sweep_r2_verdict_2026_10_09.md` |
| 330 | `dfc858d3d930` | 21,672 | 2026-10-09 11:54:29 | repo | `results/verdict/judgement/_t1_qwen_temp_sweep_verdict_2026_10_09.md` |
| 331 | `a019602cfab2` | 22,196 | 2026-10-14 14:07:09 | repo | `results/verdict/judgement/_t1_substrate_gap_precondition_2026_10_01.md` |
| 332 | `b9e9c9b5a06b` | 31,808 | 2026-10-15 17:31:14 | repo | `results/verdict/judgement/_t3trap_answerable_build_exec_2026_10_15.md` |
| 333 | `7a4a0ed3222c` | 27,675 | 2026-10-15 17:20:10 | repo | `results/verdict/judgement/_t3trap_kd3_bprime_effect_register_2026_10_15.md` |
| 334 | `b58775c33928` | 29,776 | 2026-10-15 16:53:03 | repo | `results/verdict/judgement/_t3trap_kd3_disposition_deliberation_2026_10_15.md` |
| 335 | `50780b0cd677` | 168,029 | 2026-10-21 18:51:29 | repo | `results/verdict/judgement/_t4_key_preexp_killline_prereg_2026_10_21.md` |
| 336 | `66d8d45c7a62` | 61,203 | 2026-10-22 01:10:33 | repo | `results/verdict/judgement/_t4k_k5k_coverage_adjudication_2026_10_22.md` | 【已审】
| 337 | `7098861f241a` | 78,379 | 2026-10-21 19:15:11 | repo | `results/verdict/judgement/_t4t5_layer1_application_2026_10_21.md` |
| 338 | `1fd4a9465809` | 26,857 | 2026-10-15 16:25:55 | repo | `results/verdict/judgement/_t5_generator_build_exec_2026_10_15.md` |
| 339 | `3bc96df61b08` | 52,401 | 2026-10-21 21:44:44 | repo | `results/verdict/judgement/_t5_prereq_premise_correction_2026_10_21.md` |
| 340 | `94740f8d3c8d` | 8,409 | 2026-10-09 15:02:39 | repo | `results/verdict/judgement/_th_id_attribution_verification_2026_10_09.md` |
| 341 | `a171b04b067a` | 2,274 | 2026-10-18 15:09:29 | repo | `results/verdict/judgement/_third_batch_card2_and_rename_approval_effect_2026_10_18.md` |
| 342 | `aef5ae501043` | 64,832 | 2026-10-18 14:56:09 | repo | `results/verdict/judgement/_third_batch_four_rulings_effect_2026_10_18.md` |
| 343 | `6435ecc3a540` | 14,122 | 2026-10-18 12:11:30 | repo | `results/verdict/judgement/_thirdparty_16_overwrite_necessity_2026_10_18.md` |
| 344 | `322582749c53` | 43,428 | 2026-10-18 12:23:35 | repo | `results/verdict/judgement/_thirdparty_16_overwrite_ruling_effect_2026_10_18.md` |
| 345 | `40c154d64169` | 64,069 | 2026-10-13 22:04:41 | repo | `results/verdict/judgement/_three_items_alternative_deliberation_judgment_2026_10_13.md` |
| 346 | `0e0716fde41f` | 48,178 | 2026-10-16 11:24:03 | repo | `results/verdict/judgement/_three_seed_measurement_exec_2026_10_16.md` |
| 347 | `2153c41a8cff` | 29,957 | 2026-10-12 15:23:18 | repo | `results/verdict/judgement/_trae_issues_batch3_six_items_draft_2026_10_12.md` |
| 348 | `57b9dcca2630` | 12,849 | 2026-10-12 14:54:30 | repo | `results/verdict/judgement/_trae_issues_disposition_schedule_2026_10_12.md` |
| 349 | `71c6b834dd9d` | 39,219 | 2026-10-17 16:20:57 | repo | `results/verdict/judgement/_u01_u15_recheck_after_rulings_2026_10_17.md` |
| 350 | `cd32d8a84ae6` | 24,415 | 2026-10-17 18:52:09 | repo | `results/verdict/judgement/_u09_count_caliber_2026_10_17.md` |
| 351 | `0884b8f98b96` | 59,918 | 2026-10-18 08:50:39 | repo | `results/verdict/judgement/_u10_fail_h0_verdict_2026_10_18.md` |
| 352 | `97719ffddda6` | 79,234 | 2026-10-18 09:29:15 | repo | `results/verdict/judgement/_u10_s3_denominator_rulings_effect_2026_10_18.md` |
| 353 | `111a76fa9667` | 25,048 | 2026-10-12 17:09:36 | repo | `results/verdict/judgement/_u5_referent_registry_correction_2026_10_12.md` |
| 354 | `8b5f1a495a99` | 24,046 | 2026-10-12 16:38:57 | repo | `results/verdict/judgement/_u5_semantics_resolution_2026_10_12.md` |
| 355 | `30fed54c3d09` | 22,219 | 2026-10-16 21:17:15 | repo | `results/verdict/judgement/_u_axis_active_ruling_register_2026_10_16.md` |
| 356 | `5b6847e424b0` | 40,049 | 2026-10-16 21:50:00 | repo | `results/verdict/judgement/_u_axis_equation_direction_deliberation_2026_10_16.md` |
| 357 | `45e62039cee3` | 25,669 | 2026-10-17 16:27:08 | repo | `results/verdict/judgement/_u_axis_input_vs_kdb2_recheck_2026_10_17.md` |
| 358 | `0172e2a52c80` | 40,213 | 2026-10-17 18:37:07 | repo | `results/verdict/judgement/_u_cluster1_verdict_2026_10_17.md` |
| 359 | `4dd0d2f38d46` | 47,057 | 2026-10-17 18:38:15 | repo | `results/verdict/judgement/_u_cluster2_verdict_2026_10_17.md` |
| 360 | `59f52f8bb287` | 42,227 | 2026-10-16 22:43:24 | repo | `results/verdict/judgement/_u_domain3_carrier_1494_2026_10_16.md` |
| 361 | `6793b0b56925` | 24,411 | 2026-10-17 19:10:46 | repo | `results/verdict/judgement/_u_lock_recalc_2026_10_17.md` |
| 362 | `7cbfb9bc984e` | 46,386 | 2026-10-14 03:10:30 | repo | `results/verdict/judgement/_unclosed_47_status_review_2026_10_14.md` |
| 363 | `6cfadc256a33` | 41,859 | 2026-10-18 20:35:38 | repo | `results/verdict/judgement/_unified_caliber_document_2026_10_18.md` |
| 364 | `426cfe18cf65` | 21,332 | 2026-09-27 14:20:06 | repo | `results/verdict/judgement/_v3_n_recheck_llm_verdict_2026_09_27.md` |
| 365 | `3aab3f7660fc` | 36,133 | 2026-10-01 08:58:09 | repo | `results/verdict/judgement/_v3_recheck_26b_verdict_prep_2026_10_01.md` |
| 366 | `d9b6b974cfc1` | 112,085 | 2026-09-30 16:15:20 | repo | `results/verdict/judgement/_v3_recheck_verdict_register_2026_09_27.md` |
| 367 | `b70211bfa83e` | 15,247 | 2026-09-23 14:27:09 | repo | `results/verdict/judgement/_v3_supplement_verdict_2026_09_23.md` |
| 368 | `bb44fdc7ab0f` | 53,751 | 2026-09-27 13:15:20 | repo | `results/verdict/judgement/_v4_pi_cot_v3_verdict_v3.md` |
| 369 | `41d29f4deb70` | 42,157 | 2026-09-27 13:24:20 | repo | `results/verdict/judgement/_v4_pi_cot_v3_verdict_v3_signoff_2026_09_27.md` |
| 370 | `8eef73bf9856` | 19,697 | 2026-09-29 16:25:57 | repo | `results/verdict/judgement/_v4_supp_l14_n11full_verdict.md` |
| 371 | `df6453d57f8a` | 65,978 | 2026-09-30 16:15:20 | repo | `results/verdict/judgement/_v4_supp_l14v3_n26_verdict.md` |
| 372 | `3cb5c2f59961` | 54,377 | 2026-09-30 16:15:20 | repo | `results/verdict/judgement/_v4_supp_t15_verdict.md` |
| 373 | `963725dbd82a` | 65,638 | 2026-09-30 16:15:20 | repo | `results/verdict/judgement/_v4_supp_t15r2_verdict.md` |
| 374 | `0ad42625f333` | 29,106 | 2026-09-30 16:15:20 | repo | `results/verdict/judgement/_v4_supp_t1_verdict.md` |
| 375 | `44d9bad9039b` | 12,883 | 2026-09-23 15:27:54 | repo | `results/verdict/judgement/_v4_track2_multimodel_verdict_2026_09_23.md` |
| 376 | `132bfa0c02f5` | 18,877 | 2026-09-30 17:02:47 | repo | `results/verdict/judgement/_v5_fake_verdict_session_log_2026_09_28.md` |
| 377 | `088085d6c90d` | 28,484 | 2026-09-30 17:02:47 | repo | `results/verdict/judgement/_v5_fake_verdict_v1x_prereg_2026_09_28.md` |
| 378 | `45648b0ec940` | 57,227 | 2026-09-29 11:41:25 | repo | `results/verdict/judgement/_v5_gt_verdict_2026_09_29.md` |
| 379 | `b59bef293712` | 26,232 | 2026-09-29 12:56:02 | repo | `results/verdict/judgement/_v5_item35_v2_verdict_2026_09_29.md` |
| 380 | `33f68fd8ea3b` | 17,013 | 2026-10-13 17:43:35 | repo | `results/verdict/judgement/_value_card_template_7col_2026_10_13.md` |
| 381 | `769b345d9bdf` | 69,409 | 2026-10-21 17:22:56 | repo | `results/verdict/judgement/_weighted_law_killline_prereg_2026_10_21.md` |
| 382 | `afd2a78e6a4f` | 56,228 | 2026-10-17 13:46:44 | repo | `results/verdict/judgement/_whitelist_and_scope_ruling_effect_2026_10_17.md` |
| 383 | `567cb4e5bfe0` | 7,129 | 2026-10-18 21:12:19 | repo | `results/verdict/judgement/_xiang14_third_trace_and_pullback_2026_10_18.md` |
| 384 | `3c6edf11135d` | 36,926 | 2026-10-13 22:08:23 | repo | `results/verdict/judgement/_xiang8_xiang12_deliberation_judgment_2026_10_13.md` |
| 385 | `f2bed1e98f62` | 31,602 | 2026-10-17 17:41:45 | repo | `results/verdict/judgement/_zerocall_criterion_redefinition_2026_10_17.md` |
| 386 | `24418fa60ede` | 33,287 | 2026-10-01 10:21:29 | repo | `results/verdict/judgement/c5_guard_0_1_recheck_verdict_2026_10_01.md` |
| 387 | `6f1bde118d01` | 92,100 | 2026-10-22 02:38:10 | repo | `results/verdict/pi_register/_pi_1009_eight_gap_enum_effect_2026_10_22.md` |
| 388 | `f8545e95374f` | 53,460 | 2026-10-20 19:02:30 | repo | `results/verdict/pi_register/_pi_card_payload_extraction_2026_10_20.md` |
| 389 | `87d3bac68420` | 100,274 | 2026-10-21 10:56:22 | repo | `results/verdict/pi_register/_pi_decision_backlog_consolidated_2026_10_21.md` |
| 390 | `74e25d75d59d` | 31,463 | 2026-10-14 01:57:09 | repo | `results/verdict/pi_register/_pi_give_b_class_retrieval_2026_10_14.md` |
| 391 | `67ef129f9062` | 34,309 | 2026-10-14 01:45:10 | repo | `results/verdict/pi_register/_pi_give_backlog_review_2026_10_14.md` |
| 392 | `5d0f272509d6` | 318,489 | 2026-10-22 15:50:01 | repo | `results/verdict/pi_register/_pi_input_timeline_since_20261009_2026_10_22.md` |
| 393 | `ae893e953781` | 3,911 | 2026-10-21 22:36:09 | repo | `results/verdict/pi_register/_pi_register_dedup_note_2026_10_21.md` |
| 394 | `31d66920001c` | 61,341 | 2026-10-13 21:02:05 | repo | `results/verdict/pi_register/_unclosed_47_pi_give_draft_2026_10_13.md` |
| 395 | `5fbec21e0ad2` | 42,914 | 2026-09-26 18:35:47 | repo | `results/verdict/pi_register/_v4_pi_cot_v2_coding_review_2026_09_26.md` |
| 396 | `cc25c5149ce1` | 4,247 | 2026-09-23 17:56:05 | repo | `results/verdict/pi_register/_v4_pi_cot_v2_prereg.md` |
| 397 | `7b14cdb31d21` | 12,402 | 2026-09-24 10:51:01 | repo | `results/verdict/pi_register/_v4_pi_cot_v2_questionnaire_v1.md` |
| 398 | `58ed6be022ed` | 10,251 | 2026-09-27 17:14:41 | repo | `results/verdict/pi_register/_v4_pi_cot_v3_alt_reading_definition_2026_09_27.md` |
| 399 | `44c4d570375c` | 12,851 | 2026-09-28 14:03:02 | repo | `results/verdict/pi_register/_v4_pi_cot_v3_missing_ledger_correction_2026_09_28.md` |
| 400 | `b7547329af2e` | 27,223 | 2026-09-27 12:02:44 | repo | `results/verdict/pi_register/_v4_pi_cot_v3_prereg.md` |
| 401 | `238077d25919` | 53,581 | 2026-09-28 15:19:16 | repo | `results/verdict/pi_register/_v4_pi_cot_v3_questionnaire_v2_d8_2026_09_28.md` |
| 402 | `75aedf9ba95e` | 11,385 | 2026-09-30 16:15:20 | repo | `results/verdict/pi_register/_v4_pi_cot_v3_v3r1_rescript_2026_09_27.md` |
| 403 | `9238c2287af5` | 31,942 | 2026-10-01 09:10:24 | sub | `results/verdict/judgement/_clearance_mini_rulings_closeout_register_2026_10_01.md` |
| 404 | `82c5c143134e` | 26,304 | 2026-10-10 15:02:56 | sub | `results/verdict/judgement/_e6_n_distinct_judge_types_recompute_2026_10_10.md` |
| 405 | `664e82968fc2` | 39,008 | 2026-10-10 13:36:11 | sub | `results/verdict/judgement/_e6_verdict_v3_rationale_review_2026_10_10.md` |
| 406 | `c14094bdf815` | 25,953 | 2026-09-30 12:54:50 | sub | `results/verdict/judgement/_fake_verdict_session_log_reverify_2026_09_30.md` |
| 407 | `8ae4016bb41d` | 30,662 | 2026-10-09 11:07:09 | sub | `results/verdict/judgement/_g4_e3_definition_ruling_material_2026_10_09.md` |
| 408 | `e98bee353448` | 37,003 | 2026-10-09 12:06:13 | sub | `results/verdict/judgement/_k_v3df_0_1_readings_verdict_2026_10_09.md` |
| 409 | `a14aafa220c4` | 27,735 | 2026-10-09 11:50:56 | sub | `results/verdict/judgement/_k_v3df_9_1_c1_c4_legs_verdict_2026_10_09.md` |
| 410 | `78481cc60494` | 23,029 | 2026-10-10 13:21:16 | sub | `results/verdict/judgement/_kd04_c_denominator_closeout_register_2026_10_10.md` |
| 411 | `2caa3966b866` | 27,915 | 2026-10-10 11:41:56 | sub | `results/verdict/judgement/_kd04_c_denominator_expansion_exec_2026_10_10.md` |
| 412 | `19ad36f7ec84` | 25,123 | 2026-10-10 13:03:50 | sub | `results/verdict/judgement/_kd04_c_denominator_verdict_keeper_alternative_judgment_2026_10_10.md` |
| 413 | `63d1566d273e` | 29,664 | 2026-10-14 11:35:04 | sub | `results/verdict/judgement/_kd_19_ambiguous_tags_rejudge_rewrite_register_2026_10_10.md` |
| 414 | `c55770be5e33` | 10,255 | 2026-10-12 00:39:06 | sub | `results/verdict/judgement/_kd_doc1_correction_adoption_register_2026_10_11.md` |
| 415 | `2d291f1d8de5` | 29,761 | 2026-10-14 14:07:09 | sub | `results/verdict/judgement/_kd_heteronym_classification_disposition_2026_10_09.md` |
| 416 | `a9698fed8b9b` | 17,643 | 2026-10-10 02:57:52 | sub | `results/verdict/judgement/_kd_legacy_rewrite_plan_2026_10_10.md` |
| 417 | `9a7936882a5d` | 14,537 | 2026-10-10 10:41:53 | sub | `results/verdict/judgement/_kd_legacy_rewrite_register_2026_10_10.md` |
| 418 | `2cadab5ed4f7` | 13,731 | 2026-10-10 10:40:29 | sub | `results/verdict/judgement/_kd_legacy_rewrite_ruling_2026_10_10.md` |
| 419 | `316d14c137bb` | 20,422 | 2026-10-10 13:56:56 | sub | `results/verdict/judgement/_kd_login_register_section65_correction_2026_10_10.md` |
| 420 | `53d4fa3a681f` | 70,328 | 2026-10-14 11:35:54 | sub | `results/verdict/judgement/_kd_resolvability_and_optional_experiments_2026_10_09.md` |
| 421 | `aeefc94a94b5` | 20,862 | 2026-10-10 11:53:38 | sub | `results/verdict/judgement/_kd_rewrite_fingerprint_sync_2026_10_10.md` |
| 422 | `b07887551f7c` | 19,525 | 2026-10-10 11:38:50 | sub | `results/verdict/judgement/_kd_uncognizable_meaning_rewrite_register_2026_10_10.md` |
| 423 | `1c7445fca0de` | 4,794 | 2026-09-30 21:47:40 | sub | `results/verdict/judgement/_kimi_fullupload_r1_r4_rulings_register_2026_09_30.md` |
| 424 | `f2e8e32089b2` | 14,101 | 2026-10-11 20:52:41 | sub | `results/verdict/judgement/_krj10_terminal_verdict_closure_2026_10_11.md` |
| 425 | `50e91bf30e45` | 30,293 | 2026-10-11 20:43:41 | sub | `results/verdict/judgement/_krj4_trj1_adjudication_judgment_2026_10_11.md` |
| 426 | `fb7bb5da85ec` | 16,567 | 2026-10-11 21:06:58 | sub | `results/verdict/judgement/_krj4_trj1_pick_and_pass_verdict_2026_10_11.md` |
| 427 | `2b6bf509a135` | 60,700 | 2026-10-11 01:17:39 | sub | `results/verdict/judgement/_krj5_final_disposition_verdict_2026_10_11.md` |
| 428 | `78fb8c47c944` | 72,247 | 2026-10-11 21:12:00 | sub | `results/verdict/judgement/_krj_all_five_verdicts_rewrite_2026_10_11.md` |
| 429 | `f52231807e36` | 95,659 | 2026-10-11 17:51:02 | sub | `results/verdict/judgement/_krj_all_terminal_verdicts_2026_10_11.md` |
| 430 | `5c0efd663847` | 16,064 | 2026-10-11 21:20:35 | sub | `results/verdict/judgement/_krj_five_verdicts_adjudication_2026_10_11.md` |
| 431 | `e51317fcc5cf` | 50,858 | 2026-10-09 17:23:30 | sub | `results/verdict/judgement/_kv3s_4_terminal_verdict_2026_10_09.md` |
| 432 | `0f82948defb3` | 20,211 | 2026-10-09 18:06:24 | sub | `results/verdict/judgement/_kv3s_4_terminal_verdict_supplement_2026_10_09.md` |
| 433 | `c5866ce87d9c` | 56,329 | 2026-10-10 11:37:24 | sub | `results/verdict/judgement/_limb_reading_verdict_kv3s33_2026_10_01.md` |
| 434 | `2b6e8b527f93` | 7,341 | 2026-10-01 09:36:01 | sub | `results/verdict/judgement/_morning_wrapup_pending_rulings_2026_10_01.md` |
| 435 | `c8428b883029` | 42,775 | 2026-10-11 12:17:37 | sub | `results/verdict/judgement/_pending_rulings_drafts_2026_10_11.md` |
| 436 | `511c81b96745` | 30,532 | 2026-10-09 21:45:26 | sub | `results/verdict/judgement/_r2_verdict_179domain_arith_verification_2026_10_09.md` |
| 437 | `6d8537cb127f` | 23,453 | 2026-10-10 19:12:12 | sub | `results/verdict/judgement/_round56_v4_kd_row_correction_revision_2026_10_10.md` |
| 438 | `e394bb6b5ddf` | 35,037 | 2026-10-10 11:37:23 | sub | `results/verdict/judgement/_s3_kv3s_3_verdict_2026_10_01.md` |
| 439 | `e2fdb380cd3c` | 30,257 | 2026-10-09 23:22:00 | sub | `results/verdict/judgement/_s4_bc_construction_ruling_2026_10_09.md` |
| 440 | `f62401b619cc` | 2,135 | 2026-10-09 15:09:52 | sub | `results/verdict/judgement/_s4_final_ruling_card_register_2026_10_09.md` |
| 441 | `658d7f3ab231` | 33,799 | 2026-10-09 14:04:40 | sub | `results/verdict/judgement/_s4_topup_intake_verdict_2026_10_09.md` |
| 442 | `bba3b889d849` | 76,910 | 2026-10-11 17:10:58 | sub | `results/verdict/judgement/_s6doubleprime_terminal_verdicts_2026_10_11.md` |
| 443 | `8e19c10ce219` | 31,515 | 2026-10-11 17:38:34 | sub | `results/verdict/judgement/_s6doubleprime_verdict_supplement_2026_10_11.md` |
| 444 | `1c8ce58d6484` | 54,937 | 2026-10-11 12:36:08 | sub | `results/verdict/judgement/_s6prime_terminal_verdicts_2026_10_11.md` |
| 445 | `15c1c4b317a0` | 48,298 | 2026-10-10 02:47:15 | sub | `results/verdict/judgement/_t1_exp2_verdict_2026_10_10.md` |
| 446 | `e863ca5fb157` | 13,480 | 2026-10-10 10:29:40 | sub | `results/verdict/judgement/_t1_exp2_verdict_bytes_correction_2026_10_10.md` |
| 447 | `0b5fb78727c2` | 72,934 | 2026-10-18 15:41:09 | sub | `results/verdict/judgement/_t1_gate_closure_and_recompute_verdict_2026_10_01.md` |
| 448 | `2ded8091114a` | 21,346 | 2026-10-09 21:56:51 | sub | `results/verdict/judgement/_t1_pairing_caliber_ruling_2026_10_09.md` |
| 449 | `aa0f96bb618f` | 27,819 | 2026-10-09 14:03:16 | sub | `results/verdict/judgement/_v3_02_ethard_closure_verdict_2026_10_09.md` |
| 450 | `8bbecb15b28b` | 26,309 | 2026-10-01 09:03:39 | sub | `results/verdict/judgement/_v3_recheck_26b_verdict_2026_10_01.md` |
| 451 | `a91efbfec3d0` | 16,409 | 2026-10-01 09:26:42 | sub | `results/verdict/judgement/_v3n_cpath_live_rerun_verdict_2026_10_01.md` |
| 452 | `ba4d07bd7000` | 26,637 | 2026-09-26 19:14:42 | sub | `results/verdict/judgement/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` |
| 453 | `1b135d8b1e08` | 35,870 | 2026-09-28 23:22:52 | sub | `results/verdict/judgement/_v5_fake_verdict_forensics_2026_09_28.md` |
| 454 | `9140b6e5970b` | 32,653 | 2026-09-29 15:50:16 | sub | `results/verdict/judgement/_v5_gt8_lowarm_verdict_2026_09_29.md` |
| 455 | `aff727434aa4` | 40,282 | 2026-09-29 19:32:56 | sub | `results/verdict/judgement/_v5_gt8_lowarm_verdict_r2_2026_09_29.md` |
| 456 | `26eaa156108f` | 32,354 | 2026-09-29 16:45:55 | sub | `results/verdict/judgement/_v5_item21_strategyqa_realias_verdict_2026_09_29.md` |
| 457 | `de274bd38955` | 28,155 | 2026-09-28 21:30:15 | sub | `results/verdict/judgement/_v5_item21_verdict_2026_09_28.md` |
| 458 | `363cce3dae59` | 38,266 | 2026-10-01 09:05:02 | sub | `results/verdict/judgement/_v5_item35_v3_collinear_verdict_2026_10_01.md` |
| 459 | `a31026f2384d` | 33,755 | 2026-10-01 08:57:30 | sub | `results/verdict/judgement/_v5_item35_v3_collinear_verdict_prep_2026_10_01.md` |
| 460 | `1814f9590f0f` | 41,566 | 2026-09-29 14:27:08 | sub | `results/verdict/judgement/_v5_pjpm_pc_verdict_bang3_2026_09_29.md` |
| 461 | `9c1ccbd5cf5a` | 40,057 | 2026-09-29 02:05:11 | sub | `results/verdict/judgement/_v5_rj5_verdict_2026_09_29.md` |
| 462 | `63d898ab1b71` | 42,645 | 2026-09-29 15:16:34 | sub | `results/verdict/judgement/_v5_v3_deg_p1_reopen_verdict_2026_09_29.md` |
| 463 | `8adaf4e5d868` | 44,054 | 2026-09-29 15:24:27 | sub | `results/verdict/judgement/_v5_v3_deg_p1_reopen_verdict_r2_2026_09_29.md` |
| 464 | `8c2ce0dc1c2d` | 49,471 | 2026-10-14 14:07:09 | sub | `results/verdict/judgement/_verdict_pack_d_prep_2026_10_01.md` |
| 465 | `3fbf6b38a383` | 30,118 | 2026-10-01 09:53:17 | sub | `results/verdict/judgement/c5_b_group_verdict_2026_10_01.md` |
| 466 | `b09209e9c20d` | 9,579 | 2026-10-12 00:53:49 | sub | `results/verdict/pi_register/_gate_one_pi_endorsement_register_2026_10_12.md` |
| 467 | `31e32ccc59bf` | 15,214 | 2026-10-11 21:34:15 | sub | `results/verdict/pi_register/_krj_pi_picks_adoption_krj6_revise_2026_10_11.md` |
| 468 | `cb5d933f8fae` | 35,538 | 2026-10-01 12:20:10 | sub | `results/verdict/pi_register/_linestand_pi_signoff_2026_10_01.md` |
| 469 | `55f469269d3d` | 40,678 | 2026-10-11 14:44:15 | sub | `results/verdict/pi_register/_pending_pi_items_drafts_2026_10_11.md` |
| 470 | `87ab4929477f` | 35,258 | 2026-10-09 12:45:09 | sub | `results/verdict/pi_register/_pending_pi_items_master_register_2026_10_09.md` |
| 471 | `0a4b752cbc56` | 13,883 | 2026-10-12 00:11:11 | sub | `results/verdict/pi_register/_pi_card_123_adoption_and_gate_one_request_2026_10_11.md` |
| 472 | `41a82bde5190` | 54,511 | 2026-10-11 14:22:34 | sub | `results/verdict/pi_register/_pi_effectivity_declaration_register_2026_10_11.md` |
| 473 | `a6d33cf318fe` | 59,604 | 2026-10-09 21:53:15 | sub | `results/verdict/pi_register/_pi_facing_items_screen_2026_10_09.md` |
| 474 | `5ec0638e9498` | 103,140 | 2026-10-14 01:55:34 | sub | `results/verdict/pi_register/_pi_give_a_class_pilot_design_2026_10_14.md` |
| 475 | `8fa2a7a2c49d` | 51,793 | 2026-10-09 23:42:17 | sub | `results/verdict/pi_register/_pi_pending_items_draft_package_2026_10_09.md` |
| 476 | `167ad91f198e` | 1,181 | 2026-09-23 17:49:35 | sub | `results/verdict/pi_register/_v4_pi_cot_v2_collection_log.md` |
| 477 | `00584e5a5c78` | 1,016 | 2026-09-23 18:03:11 | sub | `results/verdict/pi_register/_v4_pi_cot_v2_prereg_activation_2026_09_23.md` |
| 478 | `ae154971d1d2` | 12,152 | 2026-09-28 14:04:07 | sub | `results/verdict/pi_register/_v4_pi_cot_v3_lock_and_rejudge_register_2026_09_28.md` |


### §7-2 口径乙（自载判定族）之全表（N ＝ 148）

| # | SHA-12 | bytes | mtime | 仓 | 相对路径 |
|:-:|:--|--:|:--|:--|:--|
| 1 | `9aa1c651bcea` | 50,516 | 2026-10-18 08:47:07 | repo | `results/doc/document/_cmp2_sep_threshold_s_proposal_2026_10_18.md` |
| 2 | `96956b8cf878` | 49,068 | 2026-10-22 13:42:30 | repo | `results/doc/document/_eight_hard_gaps_closure_plan_2026_10_22.md` |
| 3 | `36f70c0a844c` | 28,728 | 2026-10-14 00:12:17 | repo | `results/evidence/register/_batch7_deliberation_judgment_2026_10_13.md` |
| 4 | `a93cd166a83b` | 36,623 | 2026-10-14 01:15:44 | repo | `results/evidence/register/_batch9_deliberation_judgment_2026_10_14.md` |
| 5 | `0b5bb95a86d7` | 44,728 | 2026-10-13 21:50:06 | repo | `results/evidence/register/_four_items_alternative_deliberation_judgment_2026_10_13.md` |
| 6 | `b32ca40ec103` | 26,832 | 2026-10-15 09:09:28 | repo | `results/evidence/register/_ge01_ecr_anchor_convergence_deliberation_2026_10_14.md` |
| 7 | `5a72c931148a` | 31,736 | 2026-10-13 23:40:59 | repo | `results/evidence/register/_ge01_readiness_after_prereg_effect_2026_10_13.md` |
| 8 | `726c32d83734` | 25,221 | 2026-10-16 13:57:41 | repo | `results/evidence/register/_strip_c3_non_adoption_register_2026_10_16.md` |
| 9 | `74622229f730` | 29,882 | 2026-10-15 16:54:21 | repo | `results/readout/reading/_reading_e_33_baseline_declaration_deliberation_2026_10_15.md` |
| 10 | `ee7a822a077b` | 31,855 | 2026-10-10 11:18:26 | repo | `results/readout/reading/_t_s3_3_disposition_judgment_2026_10_10.md` |
| 11 | `75e5608106ec` | 32,097 | 2026-10-16 23:34:41 | repo | `results/readout/reading/_three_seed_readout_validity_deliberation_2026_10_16.md` |
| 12 | `ba19ab186747` | 37,430 | 2026-10-14 02:26:53 | repo | `results/review/audit/_kt_a1_anchor_drift_root_cause_2026_10_14.md` |
| 13 | `dea7dab1f4cb` | 36,878 | 2026-10-22 02:02:19 | repo | `results/review/audit/_nightly_audit_pass_2026_10_22.md` |
| 14 | `d6d8c488fc33` | 43,259 | 2026-10-17 22:02:25 | repo | `results/verdict/judgement/_af1_attribution_verdict_2026_10_17.md` |
| 15 | `f1e9d439b04d` | 32,458 | 2026-10-14 11:19:13 | repo | `results/verdict/judgement/_batch10_deliberation_judgment_2026_10_14.md` |
| 16 | `70b50503a32e` | 25,153 | 2026-10-14 14:51:15 | repo | `results/verdict/judgement/_batch11_deliberation_judgment_2026_10_14.md` |
| 17 | `a1ad238879ad` | 46,325 | 2026-10-13 22:19:26 | repo | `results/verdict/judgement/_batch5_deliberation_judgment_2026_10_13.md` |
| 18 | `a41332378c56` | 29,421 | 2026-10-13 22:50:27 | repo | `results/verdict/judgement/_batch6_deliberation_judgment_2026_10_13.md` |
| 19 | `a68b2971b8e1` | 49,012 | 2026-10-14 00:52:15 | repo | `results/verdict/judgement/_batch8_deliberation_judgment_2026_10_14.md` |
| 20 | `f1ca2c59bed9` | 37,908 | 2026-10-12 17:10:11 | repo | `results/verdict/judgement/_c4_rejection_axis_reconciliation_judgment_2026_10_12.md` |
| 21 | `660555b9b6be` | 26,218 | 2026-10-17 16:04:06 | repo | `results/verdict/judgement/_c5b_closure_verdict_2026_10_17.md` |
| 22 | `a694e5d55ce1` | 26,682 | 2026-10-17 16:48:10 | repo | `results/verdict/judgement/_card_register_dir_verdict_2026_10_17.md` |
| 23 | `536a3064ad38` | 49,332 | 2026-10-17 13:22:41 | repo | `results/verdict/judgement/_citation_no_utility_caliber_draft_2026_10_17.md` |
| 24 | `31a03b8d756b` | 121,848 | 2026-10-18 13:34:34 | repo | `results/verdict/judgement/_closure_sweep_r2_2026_10_18.md` |
| 25 | `9c05d0ab78d5` | 53,759 | 2026-10-18 14:14:54 | repo | `results/verdict/judgement/_cluster_a_sface_adjudication_2026_10_18.md` |
| 26 | `3f34fd241a50` | 72,984 | 2026-10-18 14:14:50 | repo | `results/verdict/judgement/_cluster_b_carrier_adjudication_2026_10_18.md` |
| 27 | `8e9ec9104a1e` | 63,462 | 2026-10-18 14:20:41 | repo | `results/verdict/judgement/_cluster_c_keyface_adjudication_2026_10_18.md` |
| 28 | `edcc23114b18` | 57,929 | 2026-10-18 14:36:02 | repo | `results/verdict/judgement/_cluster_d_counting_adjudication_2026_10_18.md` |
| 29 | `e289d12fd5d4` | 52,226 | 2026-10-18 14:37:14 | repo | `results/verdict/judgement/_cluster_f_deletion_adjudication_2026_10_18.md` |
| 30 | `918659f9b0f6` | 76,051 | 2026-10-18 14:49:14 | repo | `results/verdict/judgement/_cluster_g_deletion_preconditions_adjudication_2026_10_18.md` |
| 31 | `616e466f4f49` | 61,721 | 2026-10-18 14:49:58 | repo | `results/verdict/judgement/_cluster_h_directory_adjudication_2026_10_18.md` |
| 32 | `98b3ef11e115` | 51,397 | 2026-10-18 19:03:39 | repo | `results/verdict/judgement/_cluster_i_f1_f6_f7_verdict_2026_10_18.md` |
| 33 | `53ac8f30556d` | 65,872 | 2026-10-18 14:55:42 | repo | `results/verdict/judgement/_cluster_i_historical_adjudication_2026_10_18.md` |
| 34 | `e3daf0cd6fb8` | 40,492 | 2026-10-18 19:33:32 | repo | `results/verdict/judgement/_cluster_i_item6_compatibility_adjudication_2026_10_18.md` |
| 35 | `f2802aa63370` | 40,834 | 2026-10-18 20:55:13 | repo | `results/verdict/judgement/_cluster_i_item6_conditions_adjudication_2026_10_18.md` |
| 36 | `b33aae011ca8` | 45,549 | 2026-10-18 21:29:24 | repo | `results/verdict/judgement/_cluster_i_item6_give_values_adjudication_2026_10_18.md` |
| 37 | `4b1040954064` | 55,977 | 2026-10-19 14:55:07 | repo | `results/verdict/judgement/_cluster_k_eta_blockers_adjudication_2026_10_19.md` |
| 38 | `88c2af72ff7b` | 46,542 | 2026-10-15 14:52:50 | repo | `results/verdict/judgement/_d1_ab_deliberation_judgment_2026_10_15.md` |
| 39 | `509e52734292` | 28,717 | 2026-10-17 19:03:44 | repo | `results/verdict/judgement/_esc3_esc6_resolution_2026_10_17.md` |
| 40 | `57efdf5255ee` | 27,703 | 2026-10-19 15:52:50 | repo | `results/verdict/judgement/_eta_missing_params_and_c1_adjudication_2026_10_19.md` |
| 41 | `80a81bd525d4` | 63,647 | 2026-10-17 18:39:47 | repo | `results/verdict/judgement/_ext5_verdict_2026_10_17.md` |
| 42 | `0fd3788e2d3b` | 37,604 | 2026-10-17 20:30:56 | repo | `results/verdict/judgement/_face_r_coexist_verdict_2026_10_17.md` |
| 43 | `c8794d87b4b6` | 41,481 | 2026-10-17 18:26:55 | repo | `results/verdict/judgement/_fail_h0_verdict_2026_10_17.md` |
| 44 | `b6221e7a2efe` | 83,606 | 2026-10-21 11:21:17 | repo | `results/verdict/judgement/_fake_kd_itemwise_adjudication_2026_10_21.md` |
| 45 | `9c09cc70b339` | 72,909 | 2026-10-21 15:33:33 | repo | `results/verdict/judgement/_fake_kd_p3_readjudication_2026_10_21.md` |
| 46 | `e78092e45065` | 97,074 | 2026-10-21 15:08:17 | repo | `results/verdict/judgement/_fake_kd_p4_reversal_adjudication_2026_10_21.md` |
| 47 | `6addfa5db8e9` | 64,697 | 2026-10-21 13:29:21 | repo | `results/verdict/judgement/_fake_kd_p5_reversal_adjudication_2026_10_21.md` |
| 48 | `af506d37e00a` | 71,937 | 2026-10-21 14:53:57 | repo | `results/verdict/judgement/_fake_kd_p6_confirmation_adjudication_2026_10_21.md` |
| 49 | `7a0dd145a76d` | 68,956 | 2026-10-21 14:04:41 | repo | `results/verdict/judgement/_fake_kd_p8_confirmation_adjudication_2026_10_21.md` |
| 50 | `336500609b5c` | 64,097 | 2026-10-21 18:18:01 | repo | `results/verdict/judgement/_ge01_readiness_adjudication_2026_10_21.md` |
| 51 | `4d2c65968311` | 34,256 | 2026-10-16 13:57:41 | repo | `results/verdict/judgement/_interval_420_600_upper_bound_deliberation_2026_10_16.md` |
| 52 | `fce2f69802b9` | 46,687 | 2026-10-16 16:53:10 | repo | `results/verdict/judgement/_interval_ceiling_post_lock_deliberation_2026_10_16.md` |
| 53 | `a40de66d87c8` | 50,802 | 2026-10-18 22:35:39 | repo | `results/verdict/judgement/_item6_c2_four_fields_adjudication_2026_10_18.md` |
| 54 | `f5bad2e2ff00` | 42,968 | 2026-10-17 14:16:06 | repo | `results/verdict/judgement/_judgement_criteria_reference_only_no_utility_draft_2026_10_17.md` |
| 55 | `f35fe7d03551` | 54,862 | 2026-10-23 12:29:07 | repo | `results/verdict/judgement/_judgement_w39_two_reading_2026_10_23.md` |
| 56 | `09aea8d27041` | 50,919 | 2026-10-21 11:28:29 | repo | `results/verdict/judgement/_kabla6_trigger_review_adjudication_2026_10_21.md` |
| 57 | `99b578a1be2c` | 32,067 | 2026-10-15 11:46:36 | repo | `results/verdict/judgement/_kd13_ecr_anchor_binding_deliberation_2026_10_15.md` |
| 58 | `0a6279970446` | 35,608 | 2026-10-16 22:20:08 | repo | `results/verdict/judgement/_kd14_null_u_carrier_deliberation_2026_10_16.md` |
| 59 | `d87a711b0ecf` | 113,327 | 2026-10-19 22:54:59 | repo | `results/verdict/judgement/_kd_cluster_verdict_pack_adjudication_2026_10_19.md` |
| 60 | `522be8905484` | 77,119 | 2026-10-20 11:09:45 | repo | `results/verdict/judgement/_kd_crw2_beta_and_t4n05_domain_adjudication_2026_10_20.md` |
| 61 | `85e5caeb3478` | 73,955 | 2026-10-19 20:18:28 | repo | `results/verdict/judgement/_kd_epw3_crw3_ffrep1_adjudication_2026_10_19.md` |
| 62 | `b9ba3ff8d010` | 74,163 | 2026-10-21 17:30:08 | repo | `results/verdict/judgement/_kd_esc5v2_closure_adjudication_2026_10_21.md` |
| 63 | `8a5727bc4c11` | 64,606 | 2026-10-20 14:34:17 | repo | `results/verdict/judgement/_kd_eta_main_run_verdict_2026_10_20.md` |
| 64 | `ceb71b3a2570` | 66,712 | 2026-10-20 16:22:28 | repo | `results/verdict/judgement/_kd_eta_sep_measurement_verdict_2026_10_20.md` |
| 65 | `9e853e0f259b` | 68,036 | 2026-10-20 14:53:25 | repo | `results/verdict/judgement/_kd_h6_caliber_mapping_adjudication_2026_10_20.md` |
| 66 | `42af8a6e0703` | 65,988 | 2026-10-19 21:16:41 | repo | `results/verdict/judgement/_kd_mda8_domain_readings_adjudication_2026_10_19.md` |
| 67 | `9a960a574260` | 57,571 | 2026-10-19 21:36:01 | repo | `results/verdict/judgement/_kd_mda8_f1_two_senses_adjudication_2026_10_19.md` |
| 68 | `9c75b5c16676` | 64,345 | 2026-10-20 11:48:37 | repo | `results/verdict/judgement/_kd_mda8_first_reading_verdict_2026_10_20.md` |
| 69 | `170ab543d941` | 77,696 | 2026-10-20 23:18:42 | repo | `results/verdict/judgement/_kd_mda8a24_clearance_verdict_2026_10_20.md` |
| 70 | `b6f3a254abb1` | 75,087 | 2026-10-21 16:14:42 | repo | `results/verdict/judgement/_kd_mda9_closure_adjudication_2026_10_21.md` |
| 71 | `ed36d0171672` | 45,846 | 2026-10-17 19:22:50 | repo | `results/verdict/judgement/_kd_s3b1_verdict_2026_10_17.md` |
| 72 | `c013aeb1235f` | 70,518 | 2026-10-20 22:00:56 | repo | `results/verdict/judgement/_kd_sepcal7_final_verdict_2026_10_20.md` |
| 73 | `6415eb480659` | 50,348 | 2026-10-22 01:58:01 | repo | `results/verdict/judgement/_kd_t5k5_stale_premise_adjudication_2026_10_22.md` |
| 74 | `80631fb4ce3d` | 62,301 | 2026-10-22 01:26:04 | repo | `results/verdict/judgement/_kexp8_coverage_adjudication_2026_10_22.md` | 【已审】
| 75 | `591b73224eee` | 48,993 | 2026-10-19 17:19:05 | repo | `results/verdict/judgement/_kfp6_nature_and_eta_expface_adjudication_2026_10_19.md` |
| 76 | `63625672139a` | 61,667 | 2026-10-17 21:44:34 | repo | `results/verdict/judgement/_kl_m41_3_reverdict_2026_10_17.md` |
| 77 | `5dc4e089f458` | 33,138 | 2026-10-17 18:25:11 | repo | `results/verdict/judgement/_kl_m41_3_verdict_2026_10_17.md` |
| 78 | `ecbf3288d791` | 42,517 | 2026-10-19 15:06:13 | repo | `results/verdict/judgement/_l2_2_duplication_criterion_adjudication_2026_10_19.md` |
| 79 | `84e8d866054a` | 49,080 | 2026-10-19 15:38:11 | repo | `results/verdict/judgement/_l2_2_two_arms_identity_adjudication_2026_10_19.md` |
| 80 | `f54e8a10acde` | 23,630 | 2026-10-15 11:11:34 | repo | `results/verdict/judgement/_m41_verdict_kd_effect_register_2026_10_15.md` |
| 81 | `42a0b3aeff96` | 35,655 | 2026-10-16 16:02:24 | repo | `results/verdict/judgement/_material_expansion_verdict_kd_effect_register_2026_10_16.md` |
| 82 | `88df2c228eae` | 39,037 | 2026-10-16 20:05:26 | repo | `results/verdict/judgement/_n3_o5_terminal_verdict_2026_10_16.md` |
| 83 | `0abaee4aeefb` | 41,028 | 2026-10-17 22:16:42 | repo | `results/verdict/judgement/_n_distinct_grain_verdict_2026_10_17.md` |
| 84 | `0a3dedb79479` | 76,725 | 2026-10-21 18:53:59 | repo | `results/verdict/judgement/_ncc_c6_admission_adjudication_2026_10_21.md` |
| 85 | `c9c808083d46` | 52,216 | 2026-10-16 14:43:51 | repo | `results/verdict/judgement/_o1_498_lock_scope_deliberation_2026_10_16.md` |
| 86 | `99b9bff47682` | 43,055 | 2026-10-17 17:04:42 | repo | `results/verdict/judgement/_r2_reading_verdict_2026_10_17.md` |
| 87 | `bd94d12323e0` | 39,243 | 2026-10-17 16:13:11 | repo | `results/verdict/judgement/_refonly_161_reading_verdict_2026_10_17.md` |
| 88 | `03fe4d044c78` | 54,716 | 2026-10-18 10:17:14 | repo | `results/verdict/judgement/_ruled_unclosed_closure_verdict_2026_10_18.md` |
| 89 | `2c1479af62cb` | 28,816 | 2026-10-17 17:45:24 | repo | `results/verdict/judgement/_s3_s5_explanation_and_disposition_verdict_2026_10_17.md` |
| 90 | `d392bd36ec34` | 41,236 | 2026-10-17 18:28:37 | repo | `results/verdict/judgement/_strict3_verdict_2026_10_17.md` |
| 91 | `b58775c33928` | 29,776 | 2026-10-15 16:53:03 | repo | `results/verdict/judgement/_t3trap_kd3_disposition_deliberation_2026_10_15.md` |
| 92 | `66d8d45c7a62` | 61,203 | 2026-10-22 01:10:33 | repo | `results/verdict/judgement/_t4k_k5k_coverage_adjudication_2026_10_22.md` | 【已审】
| 93 | `0884b8f98b96` | 59,918 | 2026-10-18 08:50:39 | repo | `results/verdict/judgement/_u10_fail_h0_verdict_2026_10_18.md` |
| 94 | `5b6847e424b0` | 40,049 | 2026-10-16 21:50:00 | repo | `results/verdict/judgement/_u_axis_equation_direction_deliberation_2026_10_16.md` |
| 95 | `0172e2a52c80` | 40,213 | 2026-10-17 18:37:07 | repo | `results/verdict/judgement/_u_cluster1_verdict_2026_10_17.md` |
| 96 | `4dd0d2f38d46` | 47,057 | 2026-10-17 18:38:15 | repo | `results/verdict/judgement/_u_cluster2_verdict_2026_10_17.md` |
| 97 | `3aab3f7660fc` | 36,133 | 2026-10-01 08:58:09 | repo | `results/verdict/judgement/_v3_recheck_26b_verdict_prep_2026_10_01.md` |
| 98 | `3c6edf11135d` | 36,926 | 2026-10-13 22:08:23 | repo | `results/verdict/judgement/_xiang8_xiang12_deliberation_judgment_2026_10_13.md` |
| 99 | `345517455dcf` | 41,984 | 2026-10-10 23:13:30 | sub | `results/_b01_new_key_residue_judgment_2026_10_10.md` |
| 100 | `08d3bfd82235` | 27,490 | 2026-10-11 00:15:45 | sub | `results/_c_component4_d2d3_gap_judgment_2026_10_11.md` |
| 101 | `fd0094e2f865` | 41,580 | 2026-10-11 00:26:46 | sub | `results/_c_component4_three_items_judgment_2026_10_11.md` |
| 102 | `d76ba2297d0d` | 37,682 | 2026-10-09 17:34:04 | sub | `results/_ci_bc_scope_estimand_judgments_2026_10_09.md` |
| 103 | `dac19ee9e66b` | 26,090 | 2026-10-09 17:16:22 | sub | `results/_ci_three_delegated_judgments_2026_10_09.md` |
| 104 | `2ef8797c03f4` | 37,762 | 2026-10-10 11:36:54 | sub | `results/_e5_nonbinary_count_judgment_2026_10_10.md` |
| 105 | `3c7628a4964d` | 27,682 | 2026-10-10 13:13:46 | sub | `results/_e6_j5_semantics_conflict_judgment_2026_10_10.md` |
| 106 | `11945e587b1d` | 42,351 | 2026-10-11 13:46:07 | sub | `results/_f3_definition_deep_judgment_2026_10_11.md` |
| 107 | `b6eec487e9d7` | 45,911 | 2026-10-11 15:40:48 | sub | `results/_ftfb_order_judgment_2026_10_11.md` |
| 108 | `aebaff5b503c` | 29,094 | 2026-10-09 12:33:36 | sub | `results/_g4_e3_definition_independent_judgment_2026_10_09.md` |
| 109 | `22d90f12d605` | 45,207 | 2026-10-10 18:34:36 | sub | `results/_g5_krj9_denominator_reconciliation_judgment_2026_10_10.md` |
| 110 | `ee660515d9e3` | 59,309 | 2026-10-10 17:47:40 | sub | `results/_g5_rejudgment_construction_question_judgment_2026_10_10.md` |
| 111 | `16c31894d445` | 48,727 | 2026-10-10 17:12:00 | sub | `results/_g5_rejudgment_trigger_caliber_judgment_2026_10_10.md` |
| 112 | `3306d1fd020d` | 35,983 | 2026-10-10 15:17:28 | sub | `results/_g5_seg3_tie_veto_judgment_2026_10_10.md` |
| 113 | `c3117773ab36` | 33,976 | 2026-10-10 18:29:03 | sub | `results/_g5_x4_dual_axis_interpretation_judgment_2026_10_10.md` |
| 114 | `a802af7ac3bc` | 23,018 | 2026-10-09 21:06:53 | sub | `results/_k_v3s_4_2_domain_extension_judgment_2026_10_09.md` |
| 115 | `d02ec6b0987e` | 42,083 | 2026-10-11 15:02:27 | sub | `results/_kj1_abc_choice_judgment_2026_10_11.md` |
| 116 | `a14d49f7d3a2` | 36,839 | 2026-10-11 16:08:15 | sub | `results/_kj4_e4_unification_judgment_2026_10_11.md` |
| 117 | `9cde399502ba` | 51,594 | 2026-10-09 22:34:56 | sub | `results/_kv3s_4_1_2_rejudge_2026_10_09.md` |
| 118 | `369173063a7c` | 41,449 | 2026-10-10 21:28:04 | sub | `results/_p_refresh_s0_judgment_2026_10_10.md` |
| 119 | `6049c68f027b` | 28,836 | 2026-10-10 19:44:53 | sub | `results/_phase1_completion_judgment_2026_10_10.md` |
| 120 | `b4f00e5a69c4` | 43,195 | 2026-10-11 01:01:21 | sub | `results/_q2_scope_vs_revision_judgment_2026_10_11.md` |
| 121 | `5faa16446171` | 23,975 | 2026-10-09 22:42:46 | sub | `results/_r_pair_rp3b_rp2_rpq6_judgments_2026_10_09.md` |
| 122 | `8c5f83c3c4cf` | 35,443 | 2026-10-09 17:43:25 | sub | `results/_r_pair_texts_independent_review_2026_10_09.md` |
| 123 | `582c5fb9970c` | 50,170 | 2026-10-10 20:18:30 | sub | `results/_round56_typeb_form_draft_2026_10_10.md` |
| 124 | `061813859345` | 50,747 | 2026-10-10 18:36:42 | sub | `results/_round56c_d23_ad5_judgment_2026_10_10.md` |
| 125 | `246ce35c4ddc` | 44,796 | 2026-10-09 23:30:07 | sub | `results/_rpq_wordlist_and_t1p2_judgments_2026_10_09.md` |
| 126 | `49a07216a1bb` | 26,407 | 2026-10-10 13:20:41 | sub | `results/_s4q04_level_attribution_judgment_2026_10_10.md` |
| 127 | `02f44f5bf2dd` | 14,397 | 2026-10-09 17:08:31 | sub | `results/_t1_p2_aggregation_caliber_judgment_2026_10_09.md` |
| 128 | `97ac7fcc4803` | 41,432 | 2026-10-10 23:15:39 | sub | `results/_typeb_m_definition_judgment_2026_10_10.md` |
| 129 | `6509ae68f778` | 21,572 | 2026-10-11 21:31:55 | sub | `results/_u3_carrier_qid_verification_2026_10_11.md` |
| 130 | `1846e917119f` | 20,969 | 2026-10-11 21:35:16 | sub | `results/_u6_negative_delta_compatibility_2026_10_11.md` |
| 131 | `82556d54726c` | 33,399 | 2026-10-09 23:16:17 | sub | `results/_vk_two_items_judgments_2026_10_09.md` |
| 132 | `a27c7f411de5` | 17,073 | 2026-10-09 17:09:36 | sub | `results/doc/document/_t1_o1_design_axis_exemption_judgment_2026_10_09.md` |
| 133 | `c7609657dfe4` | 44,199 | 2026-10-10 17:50:47 | sub | `results/readout/reading/_s4_corpus_scope_hard_constraint_judgment_2026_10_10.md` |
| 134 | `f48601fee958` | 51,898 | 2026-10-10 15:44:56 | sub | `results/readout/reading/_s4_e4b_ad5_type_separate_judgment_2026_10_10.md` |
| 135 | `f7d76eda2911` | 29,158 | 2026-10-09 23:49:50 | sub | `results/readout/reading/_s4_face_closeout_2026_10_09.md` |
| 136 | `a330273b981c` | 36,071 | 2026-10-10 09:44:42 | sub | `results/readout/reading/_s4_regen_traceability_judgment_2026_10_10.md` |
| 137 | `a51bd6530075` | 37,607 | 2026-10-10 14:36:06 | sub | `results/readout/reading/_s4_w2_e4_separate_judgment_2026_10_10.md` |
| 138 | `a9947f5677df` | 27,824 | 2026-10-10 21:28:00 | sub | `results/readout/reading/_zero_reading_judgment_2026_10_10.md` |
| 139 | `664e82968fc2` | 39,008 | 2026-10-10 13:36:11 | sub | `results/verdict/judgement/_e6_verdict_v3_rationale_review_2026_10_10.md` |
| 140 | `e51317fcc5cf` | 50,858 | 2026-10-09 17:23:30 | sub | `results/verdict/judgement/_kv3s_4_terminal_verdict_2026_10_09.md` |
| 141 | `e2fdb380cd3c` | 30,257 | 2026-10-09 23:22:00 | sub | `results/verdict/judgement/_s4_bc_construction_ruling_2026_10_09.md` |
| 142 | `658d7f3ab231` | 33,799 | 2026-10-09 14:04:40 | sub | `results/verdict/judgement/_s4_topup_intake_verdict_2026_10_09.md` |
| 143 | `bba3b889d849` | 76,910 | 2026-10-11 17:10:58 | sub | `results/verdict/judgement/_s6doubleprime_terminal_verdicts_2026_10_11.md` |
| 144 | `1c8ce58d6484` | 54,937 | 2026-10-11 12:36:08 | sub | `results/verdict/judgement/_s6prime_terminal_verdicts_2026_10_11.md` |
| 145 | `2ded8091114a` | 21,346 | 2026-10-09 21:56:51 | sub | `results/verdict/judgement/_t1_pairing_caliber_ruling_2026_10_09.md` |
| 146 | `aa0f96bb618f` | 27,819 | 2026-10-09 14:03:16 | sub | `results/verdict/judgement/_v3_02_ethard_closure_verdict_2026_10_09.md` |
| 147 | `63d898ab1b71` | 42,645 | 2026-09-29 15:16:34 | sub | `results/verdict/judgement/_v5_v3_deg_p1_reopen_verdict_2026_09_29.md` |
| 148 | `8adaf4e5d868` | 44,054 | 2026-09-29 15:24:27 | sub | `results/verdict/judgement/_v5_v3_deg_p1_reopen_verdict_r2_2026_09_29.md` |


### §7-3 口径丙（判官落款自证）之全表（N ＝ 61）

| # | SHA-12 | bytes | mtime | 仓 | 相对路径 |
|:-:|:--|--:|:--|:--|:--|
| 1 | `8c13b1bab8a3` | 2,960 | 2026-10-18 19:24:04 | repo | `pi_rulings/_pi_card_answers_register_2026_10_18_v117.md` |
| 2 | `a9b424570540` | 2,553 | 2026-10-18 20:48:26 | repo | `pi_rulings/_pi_card_answers_register_2026_10_18_v121.md` |
| 3 | `c4a688152f74` | 2,407 | 2026-10-18 22:29:44 | repo | `pi_rulings/_pi_card_answers_register_2026_10_18_v126.md` |
| 4 | `2eae0446faf1` | 3,640 | 2026-10-20 20:07:33 | repo | `pi_rulings/_pi_card_answers_register_2026_10_20_v163.md` |
| 5 | `a006a39967e7` | 7,850 | 2026-10-21 18:45:03 | repo | `pi_rulings/_pi_card_answers_register_2026_10_21_v201.md` |
| 6 | `cc45240386e8` | 29,156 | 2026-10-13 21:20:54 | repo | `results/_archive_2026-10-14/voided/_four_class_backtrace_inventory_2026_10_13.md` |
| 7 | `dc9cb0e02922` | 28,370 | 2026-10-13 15:56:54 | repo | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_d1_ruling_and_s3_transition_2026_10_01.md` |
| 8 | `4aba41f67db5` | 56,321 | 2026-10-13 15:56:54 | repo | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_limb_reading_verdict_kv3s33_2026_10_01.md` |
| 9 | `784e5d375a6e` | 72,926 | 2026-10-18 15:41:08 | repo | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_t1_gate_closure_and_recompute_verdict_2026_10_01.md` |
| 10 | `1b28a9467567` | 29,809 | 2026-10-13 21:21:52 | repo | `results/doc/document/_four_class_backtrace_inventory_2026_10_13_r1.md` |
| 11 | `f465fbdb7579` | 19,909 | 2026-10-01 10:15:08 | repo | `results/doc/document/c5_guard_minmaxstd_report_2026_10_01.md` |
| 12 | `c4e3338619c6` | 50,322 | 2026-10-01 16:02:40 | repo | `results/evidence/register/_criterion_application_scope_prereg_2026_10_01.md` |
| 13 | `2ac4a213e32a` | 29,444 | 2026-10-23 15:07:43 | repo | `results/evidence/register/_ghost_surface_recount_2026_10_23.md` |
| 14 | `d8c41976ef1b` | 22,501 | 2026-10-15 09:50:09 | repo | `results/evidence/register/_gt_kill_family_carrier_draft_register_2026_10_15.md` |
| 15 | `e40f060fa3a3` | 25,941 | 2026-10-15 11:12:43 | repo | `results/evidence/register/_gt_kill_line_carrier_effect_register_2026_10_15.md` |
| 16 | `24ea764daeac` | 45,386 | 2026-10-09 21:03:55 | repo | `results/evidence/register/_s4_substrate_refreeze_register_179_2026_10_09.md` |
| 17 | `07e28e2fe374` | 38,464 | 2026-09-29 13:58:52 | repo | `results/evidence/register/_v5_gt_p10_lowarm_prereg_2026_09_29.md` |
| 18 | `873652fd39dd` | 42,504 | 2026-09-29 13:56:34 | repo | `results/evidence/register/_v5_item35_v3_collinear_prereg_2026_09_29.md` |
| 19 | `d9fe4bebfb84` | 36,597 | 2026-10-20 16:07:29 | repo | `results/readout/reading/_eta_sep_measurement_reading_2026_10_20.md` |
| 20 | `6e71388400ee` | 44,294 | 2026-10-18 19:32:39 | repo | `results/readout/reading/_stage5_g6_g8_four_items_ranking_2026_10_18.md` |
| 21 | `adcf7281d379` | 76,641 | 2026-10-23 15:13:00 | repo | `results/readout/run/_t5_construction_three_arms_measurement_2026_10_23.md` |
| 22 | `9c05d0ab78d5` | 53,759 | 2026-10-18 14:14:54 | repo | `results/verdict/judgement/_cluster_a_sface_adjudication_2026_10_18.md` |
| 23 | `98b3ef11e115` | 51,397 | 2026-10-18 19:03:39 | repo | `results/verdict/judgement/_cluster_i_f1_f6_f7_verdict_2026_10_18.md` |
| 24 | `f2802aa63370` | 40,834 | 2026-10-18 20:55:13 | repo | `results/verdict/judgement/_cluster_i_item6_conditions_adjudication_2026_10_18.md` |
| 25 | `b33aae011ca8` | 45,549 | 2026-10-18 21:29:24 | repo | `results/verdict/judgement/_cluster_i_item6_give_values_adjudication_2026_10_18.md` |
| 26 | `89de292707fb` | 43,038 | 2026-10-18 19:16:56 | repo | `results/verdict/judgement/_coze_v5_r2_residual4_adjudication_2026_10_18.md` |
| 27 | `ffea29afd4d8` | 44,643 | 2026-10-20 20:21:34 | repo | `results/verdict/judgement/_d13_eta_parts_1to4_caliber_2026_10_20.md` |
| 28 | `43515db69b4c` | 39,456 | 2026-10-18 20:54:48 | repo | `results/verdict/judgement/_domain_backfill_hold235_adjudication_2026_10_18.md` |
| 29 | `718812ed542e` | 32,353 | 2026-10-22 02:20:28 | repo | `results/verdict/judgement/_eight_hard_gaps_enum_diff_2026_10_22.md` |
| 30 | `c7d20b3c18ba` | 31,813 | 2026-10-14 11:47:48 | repo | `results/verdict/judgement/_family_de_stale_refresh_sub_exec_2026_10_14.md` |
| 31 | `60e9a18fa428` | 43,116 | 2026-10-18 23:16:13 | repo | `results/verdict/judgement/_kd_civ_closure_verdict_2026_10_18.md` |
| 32 | `80b8cafcd085` | 37,788 | 2026-10-20 12:22:23 | repo | `results/verdict/judgement/_kd_eta_selection_verdict_2026_10_20.md` |
| 33 | `f54e8a10acde` | 23,630 | 2026-10-15 11:11:34 | repo | `results/verdict/judgement/_m41_verdict_kd_effect_register_2026_10_15.md` |
| 34 | `84fa6996b656` | 51,073 | 2026-10-10 11:37:23 | repo | `results/verdict/judgement/_s3_th_v21_reconciliation_verdict_2026_10_01.md` |
| 35 | `0884b8f98b96` | 59,918 | 2026-10-18 08:50:39 | repo | `results/verdict/judgement/_u10_fail_h0_verdict_2026_10_18.md` |
| 36 | `45648b0ec940` | 57,227 | 2026-09-29 11:41:25 | repo | `results/verdict/judgement/_v5_gt_verdict_2026_09_29.md` |
| 37 | `cbb42aae0865` | 38,344 | 2026-10-17 21:38:25 | repo | `results/work/process/_kd_flip_census_2026_10_17.md` |
| 38 | `2ef8797c03f4` | 37,762 | 2026-10-10 11:36:54 | sub | `results/_e5_nonbinary_count_judgment_2026_10_10.md` |
| 39 | `4e65c53f68e8` | 42,116 | 2026-10-10 12:53:23 | sub | `results/_e6_case_a_judgment_face_promotion_2026_10_10.md` |
| 40 | `22d90f12d605` | 45,207 | 2026-10-10 18:34:36 | sub | `results/_g5_krj9_denominator_reconciliation_judgment_2026_10_10.md` |
| 41 | `b6bdf807cb27` | 40,169 | 2026-10-10 11:37:24 | sub | `results/_n7_mutual_exclusion_determination_2026_10_01.md` |
| 42 | `1d1895489d17` | 11,562 | 2026-10-09 11:20:01 | sub | `results/_protocol_version_landing_status_2026_10_09.md` |
| 43 | `07cde000e66f` | 8,380 | 2026-10-11 20:36:49 | sub | `results/_s5dp_mixed_object_erratum_2026_10_11.md` |
| 44 | `cc6de8e981f6` | 23,014 | 2026-10-10 18:33:08 | sub | `results/_trj_w1_verification_2026_10_10.md` |
| 45 | `e82609024b59` | 27,079 | 2026-10-01 11:05:37 | sub | `results/_u_v04_01_criterion_scope_determination_2026_10_01.md` |
| 46 | `b2db427147e2` | 21,166 | 2026-10-10 13:34:44 | sub | `results/doc/document/_e6_j5_semantics_erratum_note_2026_10_10.md` |
| 47 | `c72086990450` | 8,181 | 2026-10-10 19:55:10 | sub | `results/doc/document/_round56_idx_sc1_temp_deletion_deviation_note_2026_10_10.md` |
| 48 | `ac3c41663f84` | 11,960 | 2026-10-12 00:02:59 | sub | `results/evidence/register/_seven_gap_closures_adoption_register_2026_10_11.md` |
| 49 | `3fe193a2a01f` | 24,208 | 2026-10-10 03:13:46 | sub | `results/readout/reading/_reading_face_basis_rejudge_2026_10_10.md` |
| 50 | `b22dda133038` | 30,680 | 2026-09-29 19:01:52 | sub | `results/readout/run/_v5_b20_gamma_a_rereview_2026_09_29.md` |
| 51 | `e16e50329c88` | 25,392 | 2026-09-29 19:40:23 | sub | `results/readout/run/_v5_familyline_r01_r02_independent_judgment_2026_09_29.md` |
| 52 | `70025895600a` | 37,949 | 2026-09-29 19:07:37 | sub | `results/readout/run/_v5_h231_r07_independent_judgment_2026_09_29.md` |
| 53 | `1995bd4460ae` | 40,697 | 2026-09-29 20:13:28 | sub | `results/readout/run/_v5_v3_t1_effect_judgment_2026_09_29.md` |
| 54 | `664e82968fc2` | 39,008 | 2026-10-10 13:36:11 | sub | `results/verdict/judgement/_e6_verdict_v3_rationale_review_2026_10_10.md` |
| 55 | `fb7bb5da85ec` | 16,567 | 2026-10-11 21:06:58 | sub | `results/verdict/judgement/_krj4_trj1_pick_and_pass_verdict_2026_10_11.md` |
| 56 | `c5866ce87d9c` | 56,329 | 2026-10-10 11:37:24 | sub | `results/verdict/judgement/_limb_reading_verdict_kv3s33_2026_10_01.md` |
| 57 | `0b5fb78727c2` | 72,934 | 2026-10-18 15:41:09 | sub | `results/verdict/judgement/_t1_gate_closure_and_recompute_verdict_2026_10_01.md` |
| 58 | `26eaa156108f` | 32,354 | 2026-09-29 16:45:55 | sub | `results/verdict/judgement/_v5_item21_strategyqa_realias_verdict_2026_09_29.md` |
| 59 | `9c1ccbd5cf5a` | 40,057 | 2026-09-29 02:05:11 | sub | `results/verdict/judgement/_v5_rj5_verdict_2026_09_29.md` |
| 60 | `63d898ab1b71` | 42,645 | 2026-09-29 15:16:34 | sub | `results/verdict/judgement/_v5_v3_deg_p1_reopen_verdict_2026_09_29.md` |
| 61 | `8adaf4e5d868` | 44,054 | 2026-09-29 15:24:27 | sub | `results/verdict/judgement/_v5_v3_deg_p1_reopen_verdict_r2_2026_09_29.md` |


---

## §8 · 老实交代（**0 软化**）

1. **本棒只出读数**：口径、件数、已审交集、覆盖率。**⛔ 0** 宣告门槛③ 成就或未成就·**⛔ 0** 宣告段毕·**⛔ 0** 落五终判·**⛔ 0** 闭 KD·**⛔ 0** 代 PI 裁·**⛔ 0** 择一口径（**三口径并列**）·**⛔ 0** 以新值径换在册值。
2. **本棒 0 复核任何被审件之实体**——今日读数皆仅及**件别归属与集合面**，未复核判死线条文之真伪、读数之对错、结论之取舍。
3. **本棒 0 跑实验·0 测量·0 联网·0 调 LLM／API·0 读 key／`.env`**；仓外两面（`〔归档区〕` 40,242 件／`〔本地路径已脱敏〕` 21 件）**仅计数**——**0 读内容、0 读文件名、0 哈希、0 写入**。
4. **既有件触动数 ＝ 0**：本棒唯一写入 ＝ 本件（新立）；落笔前停手闸：`Test-Path` ＝ **False** ✅；`results\evidence\register\` 内 `*gate3*` 名件扫描 ＝ **1 命中**（`_gate3_audit_recount_2026_10_23.md`・**他棒既有件**・本棒**只读**）；`*judgement_set*` ＝ **0 命中** ✅；目录**已存在**（⛔ 0 新建目录）。**0** 回改任何既有件一字·**0** 移动·**0** 改名·**0** 删除。
5. **口径之真值地位（如实，不软化）**：**「全部判定件」之精确全集，本棒机械不可得**——母件 0 处给出、审计书 §3-3 明载须 PI／主代理核定、自载语不统一、盲区大（§5 之 D-1–D-6）。**本棒所给三口径之覆盖率，是「按该口径读」的覆盖率，非「门槛③ 真覆盖率」。**
6. **已审 9 件 ≠ 全部**：**7 件自载为非判定件**（§3-2）⇒ **「9 ＝ 全部」之问，答：否**（在任一口径下皆否）；**但「全集 ＝ N」之问，答：未核得**（须 PI 核定）。
7. **本件之终态权威指纹**：本件之 SHA-12／bytes **不载于正文**（自指悖论）——**终态权威值 ＝ 交付面（parent）之独立复算**，沿 10-22 审计书 §8-4-1 之**同族体例**。

---

*件止。`evidence-auditor`（证据链审计官）· 2026-10-23 16:2x（GMT+8）· 门槛③「判定件全集」口径封口件｜母件 L160 逐字核得（自测 `996feb1db9cb`）＋ 件别自载族称逐字引出 ＋ 双仓 2,367 件实扫 ＋ 三口径并列（甲 478／乙 148／丙 61）＋ 已审 9 件之件别逐件开卷（**判定件 2／非判定件 7**）｜⛔ 0 宣告门槛③ 成就或未成就·⛔ 0 落五终判·⛔ 0 闭 KD·⛔ 0 代 PI 裁·⛔ 0 择一口径·⛔ 0 以新值径换在册值·⛔ 0 回改任何既有件一字·⛔ 0 移动／改名／删除·⛔ 0 新建目录·⛔ 0 读归档区与 GLM 内容（仅计数）·⛔ 0 联网·⛔ 0 调 LLM／API。*
