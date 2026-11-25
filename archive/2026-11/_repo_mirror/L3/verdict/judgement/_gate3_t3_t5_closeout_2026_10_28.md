# 门③ 之 `T3`（上探面 252 件逐件核）＋ `T5`（分类面 2 处名差）之补面件（`evidence-auditor`）· 2026-10-28

> 📌 **本件性质**：**证据链补面与登记勘误件**（`T3` 之未核面之补核 ＋ `T5` 之 2 处名差之定性 ＋ 2 处登记级名实不符之勘正登记）。⛔ **0** 落五终判（`pass`／`af`／`kd`／`fail`／`give-up`）· ⛔ **0** 判门③ 成就 · ⛔ **0** 宣告任何零（段毕／门毕／要件毕）· ⛔ **0** 代 PI 裁 · ⛔ **0** 代销记 · ⛔ **0** 回改门③ 核件一字 · ⛔ **0** 回改 EA 审计件一字 · ⛔ **0** 回改任何既有件一字 · ⛔ **0** 移动／重命名／删除任何既有件 · ⛔ **0** 跑实验 · ⛔ **0** 联网 · ⛔ **0** 调 LLM／API · ⛔ **0** 读 key／`.env` · ⛔ **0** 读 `〔本地路径已脱敏〕` · 归档区 `〔归档区〕` **0 写入 · 0 读正文**（**仅按名枚举 1 次**·见 §6）。
> 📌 **本棒**：`evidence-auditor`（证据链审计官 · agent-11335500b168）· 分支会话 `mvs_0cbd4f6c009c4fea89d73c672504bdea` · **观测时点 2026-10-28 13:28–13:45 GMT+8**（各项读数皆附实测时点）。
> 📌 **授权源**：PI 卡 `ask_df2d06ac12ac1127d68b007a`（2026-10-28 13:2x）之裁「**两者同派一支**」——`T3`（上探面 252 件之逐件核）＋ `T5`（分类面 2 处名差之修）**同棒同件**办结。
> 📌 **本件之射程**：**仅**及于 ①`T3` 之丙面 252 件之**落款面**逐件核（补「未核」之面）②`T5` 之 2 处分类名差之**定性 ＋ 处置 ＋ 读数**（补名差之面）。⛔ **0** 评任何判定件之实体面（判死线之真伪·读数之对错·结论之取舍）· ⛔ **0** 判门③ 之成就与否（裁决权属 `verdict-keeper`／PI）· ⛔ **0** 宣告任何零。
> 📌 **本件之结构限（承母件之限·非掩）**：母件 `results/readout/run/_v34_experiment_gap_plan_2026_10_08.md`（36,066／`996feb1db9cb`）**L160** 之判据对象为「**全部**判定件」，而母件 **0 处**给出「判定件」之全集定义 ⇒ 真全集**机械不可得**（EA 审计 §3-6 L250–L252）⇒ 本件**只**把 `T3` 之**已核集合**（252 件）之落款面核毕，⛔ **0** 据此断言母件「全部判定件」已闭（详见 §6-1）。

---

## §0 · 一句话（结论先行）

> 📌 **`T3` 之面已补**——丙面 **252 件**（名单见 §1-1）**逐件核毕**：**252／252 在盘**、**SHA-12 与在册逐位相符（252／252）**、**落款面已逐件核**（真 VK 落款 **16**／机械假阳 **6**／无命中 **230**；**不可判 0**）⇒ **`T3` 之「未核件数」由 252 → 0**。**然本棒⛔0 代裁 `T3` 之阈值成立**（阈值 `T3` 系门③ 核件所立·待 PI 采认）。
> 📌 **`T3` 之附带实得（上修面·如实报）**——252 件中有 **6 件**（no 238／310／405／428／429／455）兼具**真 VK 落款**与**判定面件别／承载判定面** ⇒ 若 PI／VK 采其计入「判定件」，则底数 **111 → 117**；若采不计入，则 111 不变。**此为口径裁·本棒⛔0 代裁**（§3-2）。
> 📌 **`T5` 之 2 处名差已定性**——**主性质 ＝ ①「同件异名（口径不一）」**：两读之差之实体 ＝ **同一判别式之下，「键存在而值为空」之处置不同**（机械表 ⇒「无件性质栏（不可判）」；EA 三步复算 ⇒「非判定件」）；**两读同向·皆不充判定件**·**非实质分歧**（与 EA L271／L289 一致）。**附一型 ＝ EA 审计 L190 之 no 433 行「件名名实不符」**（其所记 `_s3_kv3s_3_verdict_2026_10_01.md` 实为在册 **no 438** 之件）⇒ 以**登记·不改他件一字**之形勘正（§4）。
> 📌 **故门③ 仍不因此转 `PASS`**——`T3`／`T5` 两面虽已补，**其余未闭面（`R2` 2 件挂账／`R3` 真全集不可得／`R4` EA 勘正件未另立）** 仍在，且 **`T3` 之阈值尚待 PI 采认**。⛔ **0** 代 PI 宣告。

---
## §1 · `T3` 之口径（**AC-1**：252 件之名单来源 ＋「落款面」之可机械判定义）

### §1-1 · 「252」之名单来源（**逐环回源·每一环皆自测**）

| 环 | 源（相对 `deposon-repo`） | bytes（自测） | SHA-12（自测） | 该环所供之事实（逐字） | 观测时点 |
|:-:|:--|--:|:--|:--|:--|
| ① | `results/verdict/judgement/_gate3_111_filing_confirm_2026_10_28.md` | 75,768 | `6a870245a820` | §5-2 之 **T3** 行：「**上探面未核件数 ＝ 0**｜计「丙面 252 件之落款面」之未核件数（**或** PI 明裁以 111 为闭集并自承上探风险）｜**252 未核**（R1）｜❌」；§4-3 之 **R1** 行：「丙面 **252 件**之落款面**从未核** ⇒ 底数非闭」 | 13:29 |
| ② | `results/evidence/register/_gate3_108_ea_audit_2026_10_24.md` | 44,650 | `8ebb365be944` | §3-7（L254／L256）：照录源件 B §3-3 第 4 点「丙面 **252 件**之落款面**从未核**（前人只施口径乙于件别）⇒ 108 **非闭数**（**上探面**）」；并明书「本棒**沿其射程**（⛔ **0** 读丙面其余 252 件之内容）⇒ **未核面如实登记**」 | 13:31 |
| ③ | `results/verdict/judgement/_gate3_three_numbers_synthesis_2026_10_23.md` | 31,484 | `bf4515ff2e0b` | §1-3（L40）：「**丙**｜`非判定件`｜**258**｜❌ 落款面从未核｜本棒**定点核出 6 件**（口径乙之技术假阴）；余 **252 件落款未核** ⇒ 上探面」 | 13:32 |
| ④ | **原分母表** `.tmp/_gate3_478_mech.json`（478 行逐件） | — | — | ⚠ **该件今不在盘**：本棒于 `deposon-repo`／`deposon-sub`／`〔归档区〕` 三根**按名枚举**（匹配 `gate3_478`／`mech`）⇒ **0 命中**；在册指纹为 `6d80ae1b7b35`／178,680（源件 B §1-2 #4、41 件 v2 §1-1 #4、EA 审计 §1-2 照录） | 13:30 |
| ⑤ | **替代分母表** `results/evidence/register/_gate3_judgement_set_closure_2026_10_23.md` | 125,068 | `d48666ad32b6` | §7-1（L246–L729）之**口径甲（落档树）全表 N ＝ 478**（逐行含 `#`／SHA-12／bytes／mtime／仓／相对路径）⇒ 本棒之 **478 分母**自此件重建 | 13:33 |

> 📌 **252 之名单＝可机械重演之式**（**本棒所立·可复算**）：
> **闭件 §7-1 之 478 行** → 施**口径乙三步**（闭件 §2-2 L93 逐字 ＋ 478 机械审计件 §1-1 之取值修正）于**件首 16,000 B** ⇒ 得三面：**判定件 95／非判定件 258／无件性质栏（不可判）125** ⇒ 取「非判定件」之 **258** 行 ⇒ **减 6 件技术假阴**（源件 B §1-4 L50–L55 逐字列定之 **no 329／330／371／372／373／374**，其别名 `verdict-keeper判定收口件`／`verdict-keeper判定收口` 之「判定」二字起于**第 14 字位**⇒ 落于「首 14 字」窗之外；该 6 件**已定点开卷**、其落款面已核）⇒ **252**。
> 📌 **6 件假阴之复核（本棒自测）**：其复算态**逐件 ＝「非判定件」**，且别名逐字为 `：verdict-keeper判定收口件`（no 329／330）与 `：verdict-keeper判定收口`（no 371／372／373／374）⇒ 与源件 B §1-4 L50–L55 之登记别名**逐位相符**；其归属语在册逐字为 L3「**本件性质**：verdict-keeper **判定收口件 · r2 档**」等 ⇒ **确为技术假阴**、**确已核**、**不入 252**。
> 📌 ⚠ **登记级事实（如实登记·不改他件一字）**：在册之**分母表本体**（`.tmp/_gate3_478_mech.json`）**今不在盘**；本棒以闭件 §7-1 之 478 行**重建分母**并**复现**其三面计数（见 §1-2 之正控）。此一缺**须 PI／主代理知**（`R3`「真全集机械不可得」之同族面·**归属级缺口·非实体缺陷**）。

### §1-2 · 本棒之仪器及其校准（**正控·负控·仪器之失自陈**）

**口径乙三步（逐字取自在册·本棒不新造）**（闭件 §2-2 L93）：

> ① 件首 **16,000 字节**内存在一行含「**件性质**」或「**件别**」；② 取该键之后、首个「（」「｜」「|」「·」「—」「；」之前的片段（去 markdown 记号与空白）＝ **自载别名**；③ **别名首 14 字内**含「判定」「判断」「裁决」之一，**且**别名**不含**否定词（不是判定件／非判定／非判档／0 判定件／非判定裁）。

**取值修正**（478 机械审计件 §1-1 逐字）：「若该行含 `|`，则**取键所在单元格之下一格为值**，再对其施第 ② 步之分隔截断」。

**本棒之复算读数**（自建仪器·2026-10-28 13:2x–13:3x）：

| 面 | 本棒复算 | 在册（机械表 `counts`，经源件 B §1-3 L34／41 件 v2 §2-1／EA 审计 §1-2 三处照录） | 判 |
|:--|--:|:--|:--|
| 判定件 | **95** | 95 | ✅ 逐位相符 |
| 非判定件（**丙面**） | **258** | 258 | ✅ 逐位相符 |
| 无件性质栏（不可判） | **125** | 125 | ✅ 逐位相符 |

> 📌 **正控①（强正控·集合级）**：本棒复算所得「不可判」之 **125 行**，与在册 `_gate3_125_undetermined_2026_10_23.md`（185,271／`83d1b85ac0a3`）之**逐件 125 名单完全等同**：交集 **125**／本棒多出 **0**／在册多出 **0** ⇒ **差 0**（本棒脚本实测输出 `|125∩reg125|=125 |125-reg125|=0 reg125-|125|=0`）。
> 📌 **正控②**：6 件假阴之复算态与别名逐位相符（见 §1-1 末段）。
> 📌 **正控③（指纹面·全量）**：478 行之**现值 SHA-12 与闭件 §7-1 在册值逐位相符 475／475**（余 3 行系表格尾附「【已审】」格·解析规则已补·见 §1-2 之仪器之失）；**252 之 252 行**之 SHA-12 与在册**逐位相符 252／252**、bytes 逐位相符 252／252 ⇒ **0 不在盘 · 0 指纹漂移**。
> 📌 **负控**：no 24（`f1ca2c59bed9`）全文 4 处 `verdict-keeper` **皆为提及／禁触语**（在册 41 件 v2 §2-4 逐行列明）⇒ 本棒检测器**0 命中**；no 439（他棒落款 `protocol-keeper`）⇒ **0 VK 命中**（其 3 条字段行为他棒角色）⇒ **本检测器非「凡件皆有 VK 落款」之空转**，亦非「凡件皆无」之空转。
> 📌 ⚠ **本棒仪器之失（自陈·先审仪器）**：首轮复算因「表格行取值未取**下一格**」而得 **28／89／358**（与在册 95／258／125 严重不符）⇒ **修仪器（取值规则），不修在册文本**；修正后复算与在册**逐位全等**。另闭件 §7-1 之 3 行带尾附格「【已审】」⇒ 解析规则补之（**在册表体例之容许，不改在册件一字**）。**此二处为本棒仪器之缺口，非在册件之缺陷。**

### §1-3 · 「落款面」之可机械判定义（**本棒所立·可复算**）

> 📌 **定义（白话）**：「落款面」＝ **该件自身之归属字段行**（其值域之首个角色令牌为 `verdict-keeper` 之**真落款行**）。**⛔0** 将「提及／免责语／转引面／派工登记面／他棒落款」充为落款。

**判别式（在册之口径丙 ＋ 三读并测）**：

| 项 | 本棒所采（在册逐字来源） |
|:--|:--|
| **判别式本体** | 闭件 §2-3 L101 逐字：「件首 16,000 字节内，存在一行**同时**含落款字段名…**且**含角色名，**且**该行**值域（末分隔符之后）之首个角色令牌为 `verdict-keeper`**」 |
| **射程** | **读乙口径 ＝ 首 16,000 B ∪ 末 4,000 B**（与门③ 核件 §2-1 面③ 之射程一致）＋ **全件辅扫**（记射程外命中·不计入判定） |
| **落款字段表（29 键）** | 闭件 §2-3 之 11 键（出件方／落盘方／落款／署名／出件／编制／本棒身份／出证方／执笔／作者／经手／出品）＋ 41 件 v2 §2-2 之 12 键（出件方／落款方／落盘方／棒别／署名／出件／落账方／起草棒／本棒身份／出件面／棒／编制者）＋ 合成件 §2-4-② 增 4 键（拟稿／本件身份／任务角色／性质）＋ 125 件件 §3-1 补 2 键（棒／件之性质）＋ faceA §4-2 补 2 键（件性质／件别） |
| **标签式规则** | faceA §4-2 ① 逐字：「字段须为「标签式」（落款字段名之后 ≤6 字内须见分隔符 `：`／`:`／`｜`／`|`）方为字段标签，**文首标题行**为结构性字段（独立成域）」 |
| **值域三读** | 125 件件 §1 之三读逐字：**读甲 R1a** ＝ 行内**末**分隔符之后（分隔符集含 `|`／`｜`）｜**读乙 R1b** ＝ 行内**末**分隔符之后（分隔符集**不含** `|`／`｜`）｜**读丙 R2** ＝ 落款字段名之后**首个**分隔符之后、**首个**括号之前（闭件 §6-5 之自陈修正） |
| **角色令牌** | 值域中首个出现之角色名 ＝ `verdict-keeper`／`protocol-keeper`／`evidence-auditor`／`doc-writer`／`verifier`／`worker`／`mavis`／`parent`（8 名为在册常见集） |
| **命中后之判定** | 机械命中**必**经**开卷定性**：**真落款**／**免责语**／**转引面**／**派工登记面**／**他棒落款**（五分）⇒ 仅「真落款」计为「落款面在否 ＝ 是」 |

> 📌 **本棒之取值修正（与 478 机械审计件 §1-1 同族·如实登记）**：**⛔0** 以「末分隔符之后」为唯一口径（125 件件 §3-1 之「读甲截空失」已实证其漏检真落款行）⇒ 本棒**三读并测**、以任一读命中为机械命中，再以**开卷定性**收口。
> 📌 **落款面检测器之正控（同一检测器·同一射程）**：**6 件假阴 6／6 命中**（其 L3「**本件性质**：verdict-keeper **判定收口件**」为真落款行）；**在册乙面 28 件（125 件件 §29-1 所列 no 50／54／64／71／84／95／165／170／176／304／368／378／379／386／408／409／433／438／445／447／450／454／456／457／458／460／461／465）之 VK 落款 28／28 命中** ⇒ 非空转。
> 📌 **射程外命中之处理**：本棒**全件辅扫**另得**射程外**命中（10 件次）⇒ 一律**登记**（行号 ＋ 逐字），但**不**改「落款面在否」之判（射程 ＝ 读乙 之内）——**如实在册**。
> 📌 **本棒 ⛔0 之判**：**⛔0** 判任一判定件之**实体面**（判死线之真伪·读数之对错）；**⛔0** 判任一件**是否属母件「判定件」**（该判准之全集在册 0 处给出·属口径裁·归 PI／VK）。

---
### §2-1 · 第 1–73 件（36 件）

| no | 件名（相对路径） | 仓 | bytes（自测） | SHA-12（自测） | 落款面在否 | 其落款之实（摘引） | 判 |
|:-:|:--|:--|--:|:--|:--|:--|:--|
| 1 | `results/verdict/judgement/_a1_a6_readiness_recheck_2026_10_22.md` | repo | 74978 | `fd7b24a75444` | **是** | L10「| **落盘方** | `verdict-keeper`（判定官）· append-only 新立件」｜L144 尾窗「…署名：**`verdict-keeper`**」 | 不充判定件（落款面已核·真 VK 落款；件别面＝现值复测件·自陈 ⛔0 落五终判） |
| 2 | `results/verdict/judgement/_af1_attribution_verdict_2026_10_17.md` | repo | 43259 | `d6d8c488fc33` | **是** | L1 标题「…归 verdict-keeper（判定收口面）之行使…」｜L7「| **落款方** | **`verdict-keeper`**（判定收口官）」 | 不充判定件（落款面已核·真 VK 落款；件别面＝归属认定件·自陈 ⛔0 落五终判词之一） |
| 3 | `results/verdict/judgement/_af2_5_proof_2026_10_17.md` | repo | 48208 | `b3c45b4e2ec0` | 否 | 落款字段行在·首个角色令牌＝`worker`（L1·(文首标题行·独立域)·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 4 | `results/verdict/judgement/_af2_proof_and_grain_scope_effect_2026_10_17.md` | repo | 41779 | `faee80c8b051` | 否 | 射程内（首 16,000 B ∪ 末 4,000 B）**0** 落款字段行 | 不充判定件（落款面已核·无 VK 落款） |
| 5 | `results/verdict/judgement/_af_complete_landing_effect_2026_10_17.md` | repo | 54092 | `14e4181c5b69` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 6 | `results/verdict/judgement/_af_entity_rules_2026_10_17.md` | repo | 39994 | `525ae85c1bbc` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L7·落款方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 7 | `results/verdict/judgement/_af_flip要件消解_rulings_effect_2026_10_17.md` | repo | 45096 | `dc5ee48e1f53` | 否 | 射程内（首 16,000 B ∪ 末 4,000 B）**0** 落款字段行 | 不充判定件（落款面已核·无 VK 落款） |
| 8 | `results/verdict/judgement/_af_rules_approval_effect_2026_10_17.md` | repo | 43731 | `ce0a2847ad4e` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落款方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 9 | `results/verdict/judgement/_approval_card_four_rulings_effect_2026_10_17.md` | repo | 50703 | `8e1b7d6ae996` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 11 | `results/verdict/judgement/_b0_sixty_items_location_list_2026_10_13.md` | repo | 33046 | `7c1f8a704f83` | 否 | 射程内（首 16,000 B ∪ 末 4,000 B）**0** 落款字段行 | 不充判定件（落款面已核·无 VK 落款） |
| 13 | `results/verdict/judgement/_b_tier_five_subitems_draft_2026_10_14.md` | repo | 37605 | `3adfa261bab9` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L7·署名·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 14 | `results/verdict/judgement/_backfill_verification_2026_10_21.md` | repo | 52147 | `c6367741737a` | 否 | 落款字段行在·首个角色令牌＝`verifier`（L4·落款方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 22 | `results/verdict/judgement/_buexp_backfill_deliberation_2026_10_21.md` | repo | 80157 | `4125ea2b2f82` | 否 | 落款字段行在·首个角色令牌＝`verifier`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 23 | `results/verdict/judgement/_c1_u5_ruling_register_2026_10_12.md` | repo | 15499 | `2c3f48e111cc` | 否 | 落款字段行在·首个角色令牌＝`parent`（L94·棒·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 25 | `results/verdict/judgement/_c4_scope_ruling_and_d1_requalification_register_2026_10_12.md` | repo | 29510 | `b28540b999a6` | 否 | 射程内（首 16,000 B ∪ 末 4,000 B）**0** 落款字段行 | 不充判定件（落款面已核·无 VK 落款） |
| 26 | `results/verdict/judgement/_c5_both_pillars_closed_effect_2026_10_17.md` | repo | 24464 | `91fe9a16059d` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L4·出件·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 27 | `results/verdict/judgement/_c5_split_into_c5a_c5b_2026_10_17.md` | repo | 28902 | `c9e304e43274` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L4·出件·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 29 | `results/verdict/judgement/_c7_naming_deliberation_2026_10_21.md` | repo | 50836 | `36d18da70a95` | 否 | 落款字段行在·首个角色令牌＝`verifier`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 30 | `results/verdict/judgement/_canonical_face_scope_corrigendum_2026_10_16.md` | repo | 14502 | `1b45571bddca` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L149·署名·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 32 | `results/verdict/judgement/_chd_construction_domain_declaration_draft_2026_10_10.md` | repo | 34948 | `17cf0d59cd7b` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L8·出件·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 33 | `results/verdict/judgement/_citation_corrigenda_volume_2026_10_17.md` | repo | 68731 | `7c20c38c501d` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L135·落款·尾窗） | 不充判定件（落款面已核·无 VK 落款） |
| 38 | `results/verdict/judgement/_cluster_abc_pack_adoption_effect_2026_10_18.md` | repo | 82049 | `479e28afba53` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 42 | `results/verdict/judgement/_cluster_dfghi_pack_adoption_effect_2026_10_18.md` | repo | 68478 | `d85a8101aa12` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 47 | `results/verdict/judgement/_cluster_i_f4_f5_evidence_2026_10_18.md` | repo | 39529 | `84037fd8d0a6` | 否 | 落款字段行在·首个角色令牌＝`evidence-auditor`（L9·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 56 | `results/verdict/judgement/_commission_v04_approval_rulings_effect_2026_10_18.md` | repo | 67299 | `d13f3ed169e3` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 57 | `results/verdict/judgement/_consolidated_pending_rulings_scroll_2026_10_18.md` | repo | 104340 | `df894c9acc2a` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L7·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 59 | `results/verdict/judgement/_continued_three_rulings_effect_2026_10_17.md` | repo | 38440 | `4397d1a16805` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 60 | `results/verdict/judgement/_copilot_eq_grok_rulings_effect_2026_10_17.md` | repo | 22894 | `d34d769afaca` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 61 | `results/verdict/judgement/_copilot_reply_adoption_effect_2026_10_17.md` | repo | 39705 | `4a89f8d3ddda` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 63 | `results/verdict/judgement/_coze_v1_v3_core_principle_verification_2026_10_18.md` | repo | 30800 | `dfcda086b498` | 否 | 落款字段行在·首个角色令牌＝`evidence-auditor`（L4·棒·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 65 | `results/verdict/judgement/_coze_v5_r2_residual4_adoption_effect_2026_10_18.md` | repo | 40381 | `f688f21015e0` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 67 | `results/verdict/judgement/_d05_b_coincidence_checks_exec_2026_10_10.md` | repo | 21061 | `840fbf08caf4` | 否 | 落款字段行在·首个角色令牌＝`parent`（L4·本棒身份·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 68 | `results/verdict/judgement/_d13_eta_parts_1to4_caliber_2026_10_20.md` | repo | 44643 | `ffea29afd4d8` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 69 | `results/verdict/judgement/_d13_rename_candidates_2026_10_21.md` | repo | 54962 | `9c75e1d4cd76` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L6·落款·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 72 | `results/verdict/judgement/_d8_supplement_open_questions_2026_09_30.md` | repo | 24833 | `579b375e9508` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L231·出件·尾窗） | 不充判定件（落款面已核·无 VK 落款） |
| 73 | `results/verdict/judgement/_dangling_630_remediation_list_2026_10_17.md` | repo | 120723 | `5bc372de9a84` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L10·署名·首窗） | 不充判定件（落款面已核·无 VK 落款） |
### §2-2 · 第 74–135 件（36 件）

| no | 件名（相对路径） | 仓 | bytes（自测） | SHA-12（自测） | 落款面在否 | 其落款之实（摘引） | 判 |
|:-:|:--|:--|--:|:--|:--|:--|:--|
| 74 | `results/verdict/judgement/_deliverable_pack_manifest_2026_10_21.md` | repo | 80302 | `debce2c6d3cb` | 否 | 落款字段行在·首个角色令牌＝`worker`（L201·出件·尾窗） | 不充判定件（落款面已核·无 VK 落款） |
| 75 | `results/verdict/judgement/_deliverable_pack_v2_manifest_2026_10_21.md` | repo | 57693 | `7ae0efbb777d` | 否 | 落款字段行在·首个角色令牌＝`worker`（L116·出件·尾窗） | 不充判定件（落款面已核·无 VK 落款） |
| 76 | `results/verdict/judgement/_den16_alias_table_revision_2026_10_21.md` | repo | 46947 | `4eee36e8d339` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L8·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 77 | `results/verdict/judgement/_den16_rename_prefix_candidates_2026_10_21.md` | repo | 92103 | `7c3166071a5c` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L8·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 78 | `results/verdict/judgement/_deposon_full_history_main_2026_10_19.md` | repo | 14265 | `9c65f1db6202` | 否 | 射程内（首 16,000 B ∪ 末 4,000 B）**0** 落款字段行 | 不充判定件（落款面已核·无 VK 落款） |
| 80 | `results/verdict/judgement/_dnm16_alias_table_revision_v2_2026_10_21.md` | repo | 56375 | `033365d7a549` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L8·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 86 | `results/verdict/judgement/_e07_deliberation_2026_10_22.md` | repo | 35064 | `1fe936ee5f67` | 否 | 落款字段行在·首个角色令牌＝`verifier`（L154·落款·尾窗） | 不充判定件（落款面已核·无 VK 落款） |
| 87 | `results/verdict/judgement/_e_family_five_face_resolvability_2026_10_22.md` | repo | 52692 | `a8842f8047a8` | 否 | 落款字段行在·首个角色令牌＝`evidence-auditor`（L7·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 88 | `results/verdict/judgement/_eight_hard_gaps_crossout_2026_10_22.md` | repo | 45856 | `fc7989bba72e` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L4·出件·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 89 | `results/verdict/judgement/_eight_hard_gaps_enum_diff_2026_10_22.md` | repo | 32353 | `718812ed542e` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L129·出件·尾窗） | 不充判定件（落款面已核·无 VK 落款） |
| 94 | `results/verdict/judgement/_esc5_adoption_and_ritt_remeasure_effect_2026_10_17.md` | repo | 34206 | `e550e344a258` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落盘方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 96 | `results/verdict/judgement/_eta_construct_c1_c16_recommendation_2026_10_20.md` | repo | 83989 | `56760f30332b` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 98 | `results/verdict/judgement/_eta_missing_params_literature_evidence_2026_10_19.md` | repo | 26537 | `31ce1f43d18f` | 否 | 落款字段行在·首个角色令牌＝`evidence-auditor`（L3·出件面·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 99 | `results/verdict/judgement/_eta_preexp_wait_and_leveling_effect_2026_10_18.md` | repo | 32594 | `a79b0ca9ce9e` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 100 | `results/verdict/judgement/_eta_sep_caliber_draft_2026_10_20.md` | repo | 68943 | `2383be56f28f` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 101 | `results/verdict/judgement/_eta_sep_measurement_recalc_2026_10_20.md` | repo | 37061 | `585a30bf9f54` | 否 | 落款字段行在·首个角色令牌＝`worker`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 103 | `results/verdict/judgement/_exp8_bar_b_wf_candidates_2026_10_21.md` | repo | 35161 | `aacb2ae8a9f5` | 否 | 射程内（首 16,000 B ∪ 末 4,000 B）**0** 落款字段行 | 不充判定件（落款面已核·无 VK 落款） |
| 104 | `results/verdict/judgement/_experiment_face_scope_column1_supplement_draft_2026_10_19.md` | repo | 37932 | `1de82ef76e16` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L9·出件·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 105 | `results/verdict/judgement/_experiment_face_scope_list_draft_2026_10_19.md` | repo | 27727 | `3fdd7f38b124` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L9·出件·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 107 | `results/verdict/judgement/_f12_kd_disposition_register_2026_10_15.md` | repo | 12661 | `9c0427685a19` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·署名·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 108 | `results/verdict/judgement/_f3_payment_vector_reconstruction_2026_10_19.md` | repo | 51428 | `56ed8250525b` | 否 | 落款字段行在·首个角色令牌＝`worker`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 109 | `results/verdict/judgement/_f3_payment_vector_third_party_recalc_2026_10_19.md` | repo | 48898 | `d716cd3f1240` | 否 | 落款字段行在·首个角色令牌＝`evidence-auditor`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 110 | `results/verdict/judgement/_f4_direction1_domain_effectivity_2026_10_11.md` | repo | 40301 | `fd4ec7559342` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L4·本棒身份·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 111 | `results/verdict/judgement/_f7d_today_no_open_erratum_2026_10_19.md` | repo | 21682 | `f794107e790a` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 114 | `results/verdict/judgement/_fake_kd_closeout_register_2026_10_21.md` | repo | 40192 | `23bf57ed06dd` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 122 | `results/verdict/judgement/_family_de_stale_refresh_matrix_2026_10_14.md` | repo | 78861 | `7d67b6af125a` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L6·署名·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 123 | `results/verdict/judgement/_family_de_stale_refresh_repo_exec_2026_10_14.md` | repo | 31151 | `55155ec5f430` | 否 | 落款字段行在·首个角色令牌＝`worker`（L5·棒·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 124 | `results/verdict/judgement/_family_de_stale_refresh_sub_exec_2026_10_14.md` | repo | 31813 | `c7d20b3c18ba` | 否 | 落款字段行在·首个角色令牌＝`worker`（L5·棒·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 125 | `results/verdict/judgement/_field_table_c6_c8_o5_recommendation_draft_2026_10_19.md` | repo | 61896 | `bbcbac292f8d` | **否** | L38「⚠ **本棒 ⛔ 0 复核任何他件判定之实体**（复核权属 `verdict-keeper`／`verifier`）」——命中源为正文「**本棒**」之免责语·非落款栏 | 不充判定件（落款面已核·机械命中为免责语） |
| 127 | `results/verdict/judgement/_five_zero_recheck_evidence_2026_10_18.md` | repo | 37035 | `193d11089327` | 否 | 落款字段行在·首个角色令牌＝`evidence-auditor`（L7·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 128 | `results/verdict/judgement/_four_face_deliberation_2026_10_22.md` | repo | 64238 | `bfb9a022e3e6` | 否 | 落款字段行在·首个角色令牌＝`verifier`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 129 | `results/verdict/judgement/_freeze_face_four_rulings_effect_2026_10_17.md` | repo | 41068 | `1e512ea146d3` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 130 | `results/verdict/judgement/_g5_ccp_execution_prereqs_2026_10_10.md` | repo | 32815 | `ab1a07ae2fd1` | 否 | 落款字段行在·首个角色令牌＝`worker`（L9·出件·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 131 | `results/verdict/judgement/_gamma_taucert_scope_delimitation_2026_10_17.md` | repo | 37104 | `7374c29a8d4e` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 133 | `results/verdict/judgement/_gap10_four_rulings_effect_2026_10_17.md` | repo | 35339 | `b5596dd2abbb` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 135 | `results/verdict/judgement/_gap_l1_59_resolution_recheck_2026_10_22.md` | repo | 95154 | `4e190a8eddd3` | 否 | 落款字段行在·首个角色令牌＝`evidence-auditor`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
### §2-3 · 第 136–193 件（36 件）

| no | 件名（相对路径） | 仓 | bytes（自测） | SHA-12（自测） | 落款面在否 | 其落款之实（摘引） | 判 |
|:-:|:--|:--|--:|:--|:--|:--|:--|
| 136 | `results/verdict/judgement/_gate1_five_zero_recheck_2026_10_12.md` | repo | 20330 | `9c70140c7b02` | 否 | 射程内（首 16,000 B ∪ 末 4,000 B）**0** 落款字段行 | 不充判定件（落款面已核·无 VK 落款） |
| 137 | `results/verdict/judgement/_gate1_five_zero_recheck_glm_scope_2026_10_13.md` | repo | 34647 | `2f27acf42897` | 否 | 射程内（首 16,000 B ∪ 末 4,000 B）**0** 落款字段行 | 不充判定件（落款面已核·无 VK 落款） |
| 138 | `results/verdict/judgement/_gate1_gap_three_items_disposition_2026_10_12.md` | repo | 36087 | `5cf848421c2b` | 否 | 落款字段行在·首个角色令牌＝`parent`（L73·棒·尾窗） | 不充判定件（落款面已核·无 VK 落款） |
| 140 | `results/verdict/judgement/_github_suspect_rulings_effect_2026_10_17.md` | repo | 51654 | `f49079f46c2b` | 否 | 射程内（首 16,000 B ∪ 末 4,000 B）**0** 落款字段行 | 不充判定件（落款面已核·无 VK 落款） |
| 143 | `results/verdict/judgement/_h_budget_measurement_exec_2026_10_15.md` | repo | 25705 | `c5a58305876a` | 否 | 落款字段行在·首个角色令牌＝`mavis`（L7·落盘方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 144 | `results/verdict/judgement/_h_exact_enum_killline_prereg_2026_10_21.md` | repo | 74275 | `bfce04eb2745` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 145 | `results/verdict/judgement/_h_exact_enum_trace_2026_10_21.md` | repo | 61131 | `d187e54cc291` | 否 | 落款字段行在·首个角色令牌＝`worker`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 146 | `results/verdict/judgement/_h_face_freeze_ruling_effect_2026_10_18.md` | repo | 28087 | `3aa3bcc56258` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 147 | `results/verdict/judgement/_harness_mask_correct_value_validation_2026_10_17.md` | repo | 21741 | `b7d638ebef6e` | 否 | 射程内（首 16,000 B ∪ 末 4,000 B）**0** 落款字段行 | 不充判定件（落款面已核·无 VK 落款） |
| 148 | `results/verdict/judgement/_historical_ forgetting_recheck_2026_10_18.md` | repo | 34941 | `19b73ab478f5` | 否 | 落款字段行在·首个角色令牌＝`evidence-auditor`（L7·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 149 | `results/verdict/judgement/_historical_forgetting_21_status_update_2026_10_18.md` | repo | 43130 | `f2f1a9be203d` | **是** | L6「| **出件方** | `verdict-keeper`（判定收口官 · agent-3a4d09ba3c90） |」 | 不充判定件（落款面已核·真 VK 落款；件别面＝登记面之现态更新件·自陈 ⛔0 判闭） |
| 150 | `results/verdict/judgement/_independent_review_history_gaps_kd_2026_10_19_sub.md` | repo | 52087 | `9adf7d28fe2d` | 否 | 落款字段行在·首个角色令牌＝`evidence-auditor`（L7·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 153 | `results/verdict/judgement/_item6_c2_card_reference_registration_2026_10_18.md` | repo | 23201 | `df61b2798ecb` | 否 | 射程内（首 16,000 B ∪ 末 4,000 B）**0** 落款字段行 | 不充判定件（落款面已核·无 VK 落款） |
| 155 | `results/verdict/judgement/_item6_c2_four_fields_adoption_effect_2026_10_18.md` | repo | 40889 | `42ead18967d9` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L13·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 159 | `results/verdict/judgement/_kd04_c_denominator_killline_prereg_2026_10_10.md` | repo | 24527 | `8f2025e9de6f` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L1·(文首标题行·独立域)·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 162 | `results/verdict/judgement/_kd14_null_u_carrier_effect_register_2026_10_16.md` | repo | 24828 | `141816a6aec9` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 163 | `results/verdict/judgement/_kd1_preexp_contrast_2026_10_17.md` | repo | 27149 | `351d18d74934` | 否 | 落款字段行在·首个角色令牌＝`worker`（L8·落款方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 164 | `results/verdict/judgement/_kd4_adoption_and_caliber_pack_effect_2026_10_17.md` | repo | 32577 | `ce1604dfd251` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 166 | `results/verdict/judgement/_kd_11_12_resolution_register_2026_10_16.md` | repo | 18606 | `807932c7e1c8` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落盘方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 167 | `results/verdict/judgement/_kd_13_9_3_closure_register_2026_10_16.md` | repo | 19461 | `410f885430a4` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落盘方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 168 | `results/verdict/judgement/_kd_2_4_6_caliber_note_2026_10_16.md` | repo | 20497 | `0fd67a2075b7` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L213·署名·尾窗） | 不充判定件（落款面已核·无 VK 落款） |
| 178 | `results/verdict/judgement/_kd_false9_remedy_proposals_2026_10_20.md` | repo | 85265 | `77bc92c9d227` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L1·(文首标题行·独立域)·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 179 | `results/verdict/judgement/_kd_false9_wave0_calibers_2026_10_20.md` | repo | 76664 | `97ac680345ac` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L1·(文首标题行·独立域)·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 180 | `results/verdict/judgement/_kd_flip_candidates_2026_10_22.md` | repo | 456231 | `229741fc1629` | **是** | L1 标题「（2026-10-22 · verdict-keeper）」｜L8「| **出件方** | **verdict-keeper**（判定收口官 · 棒 `KD-FLIP-CANDIDATES`） |」 | 不充判定件（落款面已核·真 VK 落款；件别面＝可翻转性判读件·自陈 ⛔0 落五终判） |
| 181 | `results/verdict/judgement/_kd_gap_resolution_rulings_effect_2026_10_17.md` | repo | 38813 | `10e40a51c9c1` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 182 | `results/verdict/judgement/_kd_gap_survey_2026_10_17.md` | repo | 45716 | `592a50470e76` | 否 | 落款字段行在·首个角色令牌＝`evidence-auditor`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 183 | `results/verdict/judgement/_kd_ge01_eps4_scope_escalation_note_2026_10_16.md` | repo | 26411 | `731144fbda94` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落盘方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 184 | `results/verdict/judgement/_kd_h1_h7_disposition_draft_2026_10_20.md` | repo | 72915 | `42ea79ea3f06` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L10·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 185 | `results/verdict/judgement/_kd_h1_h7_hidden_gaps_register_2026_10_19.md` | repo | 51557 | `7eefedd92808` | **否** | L356／L360 表格「…📌 **本棒**新增实测…｜PI／`verdict-keeper`」——命中源为正文「**本棒**」叙述语与归责栏·非落款栏 | 不充判定件（落款面已核·机械命中为叙述／归责语） |
| 186 | `results/verdict/judgement/_kd_h1_lineage_declaration_2026_10_20.md` | repo | 54662 | `b17b642f1183` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L10·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 187 | `results/verdict/judgement/_kd_h2_anchor_chain_erratum_2026_10_20.md` | repo | 39377 | `a23dfaf20278` | 否 | 落款字段行在·首个角色令牌＝`evidence-auditor`（L174·棒别·尾窗） | 不充判定件（落款面已核·无 VK 落款） |
| 188 | `results/verdict/judgement/_kd_h4_fingerprint_reanchor_register_2026_10_20.md` | repo | 47335 | `15d1279d1638` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L10·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 189 | `results/verdict/judgement/_kd_h5_h6_recheck_2026_10_14.md` | repo | 22205 | `d9459768e058` | 否 | 落款字段行在·首个角色令牌＝`evidence-auditor`（L7·署名·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 190 | `results/verdict/judgement/_kd_h5_session_history_domain_caliber_2026_10_20.md` | repo | 55674 | `8db6f947bf98` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 191 | `results/verdict/judgement/_kd_h5_session_history_pilot_1of10_2026_10_20.md` | repo | 1000949 | `30a6398b1e2e` | 否 | 落款字段行在·首个角色令牌＝`evidence-auditor`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 193 | `results/verdict/judgement/_kd_history_pack_adjudication_2026_10_19.md` | repo | 56575 | `fce088063dbd` | **是** | L83/L289「**落款**：**verdict-keeper**（判定收口官 · agent-3a4d09ba3c90）｜…· 史面与口径面族之裁议件｜**候 PI 裁**」 | 不充判定件（落款面已核·真 VK 落款；件别面＝裁议件·候 PI 裁·自陈 ⛔0 代裁） |
### §2-4 · 第 194–253 件（36 件）

| no | 件名（相对路径） | 仓 | bytes（自测） | SHA-12（自测） | 落款面在否 | 其落款之实（摘引） | 判 |
|:-:|:--|:--|--:|:--|:--|:--|:--|
| 194 | `results/verdict/judgement/_kd_identified_defect_attribution_caliber_2026_10_20.md` | repo | 73752 | `609943436a0d` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L1·(文首标题行·独立域)·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 195 | `results/verdict/judgement/_kd_mda8_arm2_kill_line_freeze_draft_2026_10_19.md` | repo | 73620 | `b666077233c5` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 196 | `results/verdict/judgement/_kd_mda8_arm2_remaining11_recommendation_2026_10_19.md` | repo | 92280 | `30e47f1181d3` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 200 | `results/verdict/judgement/_kd_mda8_gate_resolution_and_new_exp_draft_2026_10_19.md` | repo | 95664 | `ebe106d2da47` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 201 | `results/verdict/judgement/_kd_mda8_preexp_dispatch_spec_draft_2026_10_19.md` | repo | 80642 | `8a77b155fd64` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 202 | `results/verdict/judgement/_kd_mda8_spec_rest_recommendation_2026_10_19.md` | repo | 69095 | `242b7ea98eb7` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 205 | `results/verdict/judgement/_kd_s3_2_3_corrigendum_2026_10_16.md` | repo | 26395 | `5c4fd13640f4` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L232·署名·尾窗） | 不充判定件（落款面已核·无 VK 落款） |
| 206 | `results/verdict/judgement/_kd_s3b1_kd1_n7_rulings_effect_2026_10_17.md` | repo | 49252 | `e09780d24a7a` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落盘方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 208 | `results/verdict/judgement/_kd_s3b5_kd1_esc36_batch_lock_effect_2026_10_17.md` | repo | 48246 | `3ecf179b83a1` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落盘方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 211 | `results/verdict/judgement/_kd_two_gates_boundary_adoption_2026_10_21.md` | repo | 43097 | `b69092972467` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L6·落款·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 212 | `results/verdict/judgement/_kd_two_gates_boundary_proposal_2026_10_21.md` | repo | 41462 | `0ef78a26f637` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L6·落款·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 213 | `results/verdict/judgement/_kd_two_gates_comparison_2026_10_20.md` | repo | 45929 | `45f1ea5e5b23` | 否 | 落款字段行在·首个角色令牌＝`evidence-auditor`（L1·(文首标题行·独立域)·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 214 | `results/verdict/judgement/_kd_u1_u4_rulings_effect_2026_10_17.md` | repo | 30072 | `4500a4715f3b` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 215 | `results/verdict/judgement/_kd_u5_u6_s3b4_rulings_effect_2026_10_17.md` | repo | 38534 | `85702808df0c` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 216 | `results/verdict/judgement/_kd_u6_readside_rewire_validation_2026_10_17.md` | repo | 24961 | `751205f0368f` | 否 | 落款字段行在·首个角色令牌＝`worker`（L7·棒·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 219 | `results/verdict/judgement/_kdb2r2_kd14_merge_governance_2026_10_17.md` | repo | 26107 | `4fdadf27b70c` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L7·棒·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 220 | `results/verdict/judgement/_kdb2r3_u13_rulings_effect_2026_10_17.md` | repo | 35207 | `688424929409` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落盘方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 221 | `results/verdict/judgement/_kdcensus_derived_summary_2026_10_22.md` | repo | 34769 | `53c49723b973` | 否 | 落款字段行在·首个角色令牌＝`evidence-auditor`（L8·落款方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 222 | `results/verdict/judgement/_kdk45_remeasure_2026_10_17.md` | repo | 31662 | `25ff6e4f31bc` | 否 | 落款字段行在·首个角色令牌＝`mavis`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 228 | `results/verdict/judgement/_kimi_preexec_final_rulings_effect_2026_10_18.md` | repo | 42226 | `7828c5300fdf` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 229 | `results/verdict/judgement/_kimi_receipt_authority_rulings_effect_2026_10_18.md` | repo | 62860 | `789fed8aacc7` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 230 | `results/verdict/judgement/_kl_m41_3_remeasure_2026_10_17.md` | repo | 36936 | `20a1ce111547` | 否 | 落款字段行在·首个角色令牌＝`worker`（L9·落款·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 232 | `results/verdict/judgement/_kl_m41_3_reverdict_adoption_effect_2026_10_17.md` | repo | 38651 | `27545e411171` | **否** | L137「| **棒 ①** | **`verdict-keeper`** · 棒 `AF1-ATTRIBUTION`…」——此为**派工登记面**（记他棒身份）·非本件之落款行 | 不充判定件（落款面已核·机械命中为派工登记面之转引） |
| 233 | `results/verdict/judgement/_kl_m41_3_three_seed_exec_2026_10_16.md` | repo | 41140 | `3e13344783b0` | 否 | 落款字段行在·首个角色令牌＝`worker`（L9·落款·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 235 | `results/verdict/judgement/_klm41_2_bootstrap_ci_exec_2026_10_16.md` | repo | 45192 | `a467a77d895f` | 否 | 落款字段行在·首个角色令牌＝`worker`（L235·署名·尾窗） | 不充判定件（落款面已核·无 VK 落款） |
| 236 | `results/verdict/judgement/_krj3_kd_registry_correction_2026_10_12.md` | repo | 16648 | `4d514147670a` | 否 | 射程内（首 16,000 B ∪ 末 4,000 B）**0** 落款字段行 | 不充判定件（落款面已核·无 VK 落款） |
| 237 | `results/verdict/judgement/_ksepcal9_release_pro_release_text_2026_10_21.md` | repo | 50304 | `af84d38cbfba` | 否 | 射程内（首 16,000 B ∪ 末 4,000 B）**0** 落款字段行 | 不充判定件（落款面已核·无 VK 落款） |
| 238 | `results/verdict/judgement/_kv3s_4_4_rejudge_2026_10_09.md` | repo | 42687 | `bc397d5099dd` | **是** | L7「- **出件**：**verdict-keeper**（`agent-3a4d09ba3c90` · 分支会话 `mvs_d335e7c69c2f43529d6ad43048d295a3`）」 | ★上修候选（真 VK 落款 ＋ 件别面＝重判件·K-V3S-4-4 逐线重判出 `hit` 布尔与档位）⇒ 须 PI／VK 裁其是否计入判定件 |
| 242 | `results/verdict/judgement/_m08_measured_enumeration_exec_2026_10_16.md` | repo | 45462 | `4513f841234e` | 否 | 落款字段行在·首个角色令牌＝`worker`（L6·落款方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 245 | `results/verdict/judgement/_m2_terminal_verdict_effect_register_2026_10_14.md` | repo | 31647 | `17fd10488da0` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L6·署名·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 247 | `results/verdict/judgement/_m5_reattribution_recommendation_2026_10_14.md` | repo | 22700 | `0c9641e512e4` | 否 | 落款字段行在·首个角色令牌＝`evidence-auditor`（L5·署名·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 248 | `results/verdict/judgement/_material_expansion_build_exec_2026_10_16.md` | repo | 35966 | `6ca1c64c2c44` | 否 | 落款字段行在·首个角色令牌＝`mavis`（L7·落盘方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 250 | `results/verdict/judgement/_material_root45_remeasure_2026_10_17.md` | repo | 19477 | `f2a5c4330112` | 否 | 落款字段行在·首个角色令牌＝`worker`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 251 | `results/verdict/judgement/_md_a_field_composition_draft_2026_10_18.md` | repo | 58572 | `121a3b861261` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L8·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 252 | `results/verdict/judgement/_mda8_readlaw_o1_o4_c4_recommendation_2026_10_20.md` | repo | 73898 | `1046dd5d1be0` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 253 | `results/verdict/judgement/_mda8a24_armpair_options_2026_10_22.md` | repo | 46658 | `74250c36b502` | **是** | L8「| **出件方** | **verdict-keeper**（判定收口官 · 棒 `KD-ARMPAIR-OPTIONS`） |」 | 不充判定件（落款面已核·真 VK 落款；件别面＝代价对照件·自陈 ⛔0 落五终判） |
### §2-5 · 第 254–311 件（36 件）

| no | 件名（相对路径） | 仓 | bytes（自测） | SHA-12（自测） | 落款面在否 | 其落款之实（摘引） | 判 |
|:-:|:--|:--|--:|:--|:--|:--|:--|
| 254 | `results/verdict/judgement/_merge_govern_approval_and_eps1_release_effect_2026_10_17.md` | repo | 55555 | `58727d1eec71` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 255 | `results/verdict/judgement/_morning_brief_pending_rulings_2026_10_18.md` | repo | 37227 | `9ed6dfdbc62e` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 256 | `results/verdict/judgement/_mq19_item6_caption_restatement_2026_10_15.md` | repo | 10795 | `656b2324d598` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·署名·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 257 | `results/verdict/judgement/_n2_clause_transcription_supplement_2026_10_12.md` | repo | 16192 | `ad8f0d542290` | 否 | 射程内（首 16,000 B ∪ 末 4,000 B）**0** 落款字段行 | 不充判定件（落款面已核·无 VK 落款） |
| 260 | `results/verdict/judgement/_n_distinct_proof_2026_10_17.md` | repo | 24241 | `2b538eba112a` | 否 | 落款字段行在·首个角色令牌＝`worker`（L8·落款方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 263 | `results/verdict/judgement/_ncc_c6_condition4_adjudication_2026_10_21.md` | repo | 62358 | `1c7be88017c7` | **是** | L7「| **出件方** | **verdict-keeper**（判定收口官）——职责 ＝ 实验结论之根因裁决与判定文书收口」 | 不充判定件（落款面已核·真 VK 落款；件别面＝条件④成就之判读件·自陈 ⛔0 代裁／⛔0 落五终判） |
| 264 | `results/verdict/judgement/_ncc_c6_sixpair_measurement_2026_10_21.md` | repo | 66029 | `0d127134aa97` | 否 | 落款字段行在·首个角色令牌＝`worker`（L1·(文首标题行·独立域)·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 265 | `results/verdict/judgement/_ncc_c6_thirdparty_recalc_2026_10_21.md` | repo | 87979 | `2e06217bbe61` | 否 | 落款字段行在·首个角色令牌＝`verifier`（L7·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 267 | `results/verdict/judgement/_night_shift_handover_2026_10_14_r2.md` | repo | 63091 | `1dbe20a3ba1c` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·署名·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 268 | `results/verdict/judgement/_no_backup_ruling_and_report_caliber_effect_2026_10_17.md` | repo | 53634 | `bd748afec4f8` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 275 | `results/verdict/judgement/_o1_transcription_face_erratum_2026_10_20.md` | repo | 81406 | `941002361d54` | **否** | L130「…📌 **其正误之裁 ＝ PI／`verdict-keeper`**」——命中源为正文「**本棒**」与归责语·非落款栏 | 不充判定件（落款面已核·机械命中为归责语） |
| 276 | `results/verdict/judgement/_p3_disposition_deliberation_2026_10_21.md` | repo | 60752 | `14f2e90cc430` | 否 | 落款字段行在·首个角色令牌＝`verifier`（L1·(文首标题行·独立域)·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 277 | `results/verdict/judgement/_p3_path1_codebook_killline_prereg_2026_10_21.md` | repo | 114003 | `30925758a3c7` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 278 | `results/verdict/judgement/_pack_card_four_rulings_effect_2026_10_17.md` | repo | 46371 | `7fa815bf567d` | 否 | 射程内（首 16,000 B ∪ 末 4,000 B）**0** 落款字段行 | 不充判定件（落款面已核·无 VK 落款） |
| 280 | `results/verdict/judgement/_pending_pack_four_rulings_effect_2026_10_17.md` | repo | 27925 | `9572516d82e7` | 否 | 射程内（首 16,000 B ∪ 末 4,000 B）**0** 落款字段行 | 不充判定件（落款面已核·无 VK 落款） |
| 281 | `results/verdict/judgement/_pending_residual_minimal_set_2026_10_18.md` | repo | 53502 | `0f6098f36bd0` | 否 | 落款字段行在·首个角色令牌＝`evidence-auditor`（L7·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 282 | `results/verdict/judgement/_pending_rulings_triage_2026_10_18.md` | repo | 63300 | `19c91a3bf7e8` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L7·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 285 | `results/verdict/judgement/_poststrip_recalc_2026_10_17.md` | repo | 42707 | `cfcf430f306c` | 否 | 射程内（首 16,000 B ∪ 末 4,000 B）**0** 落款字段行 | 不充判定件（落款面已核·无 VK 落款） |
| 286 | `results/verdict/judgement/_predelete_backup_caliber_draft_2026_10_17.md` | repo | 32084 | `653505b88a08` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L7·起草棒·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 287 | `results/verdict/judgement/_preexp_degen_gate_recalc_2026_10_20.md` | repo | 49419 | `374be409dc47` | 否 | 落款字段行在·首个角色令牌＝`worker`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 288 | `results/verdict/judgement/_preexp_mda8a24_c5_armpairs_measurement_2026_10_20.md` | repo | 57997 | `829e07a7a63b` | 否 | 落款字段行在·首个角色令牌＝`worker`（L1·(文首标题行·独立域)·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 289 | `results/verdict/judgement/_preexp_mda8a24_c5_armpairs_recalc_2026_10_20.md` | repo | 59947 | `c038121c9ad5` | 否 | 落款字段行在·首个角色令牌＝`worker`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 290 | `results/verdict/judgement/_preexp_mda8a24_recalc_2026_10_20.md` | repo | 63402 | `39ffd5e4c47f` | 否 | 落款字段行在·首个角色令牌＝`worker`（L8·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 292 | `results/verdict/judgement/_r2_sep_endogeneity_erratum_2026_10_18.md` | repo | 41770 | `ed5591c3c38d` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 293 | `results/verdict/judgement/_r2b_adoption_and_bytewise_caliber_effect_2026_10_17.md` | repo | 31009 | `c8f3a36c152b` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 295 | `results/verdict/judgement/_r_pair_question_texts_2026_10_09.md` | repo | 30352 | `0ad849022328` | 否 | 落款字段行在·首个角色令牌＝`worker`（L53·性质·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 296 | `results/verdict/judgement/_recycle_purge_resolution_and_434_adoption_2026_10_17.md` | repo | 44360 | `ba3944565c13` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L94·署名·尾窗） | 不充判定件（落款面已核·无 VK 落款） |
| 297 | `results/verdict/judgement/_ref_only_no_utility_criteria_effect_2026_10_17.md` | repo | 26214 | `7fc20904d015` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 299 | `results/verdict/judgement/_remote_root_face_413_68_erratum_2026_10_18.md` | repo | 27604 | `81c42f70e271` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L12·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 300 | `results/verdict/judgement/_residual_card1_four_rulings_effect_2026_10_18.md` | repo | 52696 | `cff53e597044` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 301 | `results/verdict/judgement/_resolution_path_rulings_effect_2026_10_17.md` | repo | 29195 | `91555b6b7bd6` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 303 | `results/verdict/judgement/_ritt_def_adoption_and_remeasure_effect_2026_10_17.md` | repo | 28232 | `a7539659c5df` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落盘方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 308 | `results/verdict/judgement/_s3_s5_kd_effect_2026_10_17.md` | repo | 33609 | `eea5245b31da` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 309 | `results/verdict/judgement/_s3_s5_kd_effect_2026_10_17_append1.md` | repo | 17624 | `905be2174c52` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 310 | `results/verdict/judgement/_s3_th_v21_reconciliation_verdict_2026_10_01.md` | repo | 51073 | `84fa6996b656` | **是** | L4「> **本棒身份**：**verdict-keeper**（`agent-3a4d09ba3c90`，本件实际出件者）」｜L196「| **出件** | **verdict-keeper**…判定收口面 · S3／TH 链依 F-5 口径 A（74）重裁棒 |」 | ★上修候选（真 VK 落款 ＋ 件别面＝判定面重裁件·L5「PASS 与 KD 均按判据字面直陈」）⇒ 须 PI／VK 裁其是否计入判定件 |
| 311 | `results/verdict/judgement/_s3prime_alert_disposition_judgment_2026_10_11.md` | repo | 53188 | `e7fcbc290a7e` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L3·件性质·首窗） | 不充判定件（落款面已核·无 VK 落款） |
### §2-6 · 第 312–363 件（36 件）

| no | 件名（相对路径） | 仓 | bytes（自测） | SHA-12（自测） | 落款面在否 | 其落款之实（摘引） | 判 |
|:-:|:--|:--|--:|:--|:--|:--|:--|
| 312 | `results/verdict/judgement/_s3prime_degeneracy_selfcert_2026_10_11.md` | repo | 39939 | `e4d96a516289` | 否 | 落款字段行在·首个角色令牌＝`worker`（L1·(文首标题行·独立域)·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 313 | `results/verdict/judgement/_s4_final_ruling_effectivity_register_2026_10_09.md` | repo | 32975 | `21f2926efc5d` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L5·本棒身份·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 314 | `results/verdict/judgement/_s4_heldout_sampling_caliber_ruling_2026_10_09.md` | repo | 35453 | `fb1b696de1d6` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L8·出件·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 315 | `results/verdict/judgement/_s4_kex_killline_freeze_2026_10_10.md` | repo | 15284 | `6269d0c6fd10` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L10·出件·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 316 | `results/verdict/judgement/_scroll_wave1_four_rulings_effect_2026_10_18.md` | repo | 51739 | `2813eea5584a` | **否** | L211「**件止** ｜ *doc-writer（文稿起草／落账／登记专官）* …｜**闭之登记归 `verdict-keeper`**」——本件落款方＝doc-writer；命中源为归责语 | 不充判定件（落款面已核·本件落款方＝doc-writer·机械命中为归责语） |
| 317 | `results/verdict/judgement/_scroll_wave2_four_rulings_effect_2026_10_18.md` | repo | 51949 | `57881886e428` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 318 | `results/verdict/judgement/_scroll_wave4_three_rulings_effect_2026_10_18.md` | repo | 51604 | `0db1e827d943` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 319 | `results/verdict/judgement/_scroll_wave5_four_rulings_effect_2026_10_18.md` | repo | 71453 | `c44183973483` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 320 | `results/verdict/judgement/_seed_double_identifier_finalization_2026_10_11.md` | repo | 26864 | `6904852f8ceb` | 否 | 落款字段行在·首个角色令牌＝`worker`（L10·出件·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 321 | `results/verdict/judgement/_stage1_killline_values_proposal_2026_10_21.md` | repo | 90488 | `5bccb1af707d` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L1·(文首标题行·独立域)·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 322 | `results/verdict/judgement/_stage1_killline_values_proposal_second_reading_2026_10_21.md` | repo | 99794 | `60f02aa54930` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L1·(文首标题行·独立域)·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 323 | `results/verdict/judgement/_stage3_close_and_cmp2_rulings_effect_2026_10_18.md` | repo | 54315 | `22843cb2ce08` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 324 | `results/verdict/judgement/_stage_sequence_ruling_effect_2026_10_17.md` | repo | 18115 | `b582bde59d6d` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·署名·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 326 | `results/verdict/judgement/_supplement_500_combo_exec_2026_10_16.md` | repo | 46503 | `ee7a1563d850` | 否 | 落款字段行在·首个角色令牌＝`mavis`（L7·落盘方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 327 | `results/verdict/judgement/_supplemental_sync_commission_rulings_effect_2026_10_18.md` | repo | 71443 | `7fa22aa1addb` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 328 | `results/verdict/judgement/_t1_exp2_activation_supplement_2026_10_09.md` | repo | 24708 | `8db3f88b5ed0` | 否 | 射程内（首 16,000 B ∪ 末 4,000 B）**0** 落款字段行 | 不充判定件（落款面已核·无 VK 落款） |
| 332 | `results/verdict/judgement/_t3trap_answerable_build_exec_2026_10_15.md` | repo | 31808 | `b9e9c9b5a06b` | 否 | 落款字段行在·首个角色令牌＝`mavis`（L7·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 333 | `results/verdict/judgement/_t3trap_kd3_bprime_effect_register_2026_10_15.md` | repo | 27675 | `7a4a0ed3222c` | **是** | L7「| **出件方** | `verdict-keeper`（判定收口官） |」｜L186「**落款**：`verdict-keeper`（判定收口官）…」 | 不充判定件（落款面已核·真 VK 落款；件别面＝PI 裁之生效落账件·自陈 ⛔0 代 PI 裁） |
| 335 | `results/verdict/judgement/_t4_key_preexp_killline_prereg_2026_10_21.md` | repo | 168029 | `50780b0cd677` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L7·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 337 | `results/verdict/judgement/_t4t5_layer1_application_2026_10_21.md` | repo | 78379 | `7098861f241a` | 否 | 落款字段行在·首个角色令牌＝`worker`（L7·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 338 | `results/verdict/judgement/_t5_generator_build_exec_2026_10_15.md` | repo | 26857 | `1fd4a9465809` | 否 | 落款字段行在·首个角色令牌＝`mavis`（L7·落盘方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 339 | `results/verdict/judgement/_t5_prereq_premise_correction_2026_10_21.md` | repo | 52401 | `3bc96df61b08` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L1·(文首标题行·独立域)·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 340 | `results/verdict/judgement/_th_id_attribution_verification_2026_10_09.md` | repo | 8409 | `94740f8d3c8d` | 否 | 射程内（首 16,000 B ∪ 末 4,000 B）**0** 落款字段行 | 不充判定件（落款面已核·无 VK 落款） |
| 342 | `results/verdict/judgement/_third_batch_four_rulings_effect_2026_10_18.md` | repo | 64832 | `aef5ae501043` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 344 | `results/verdict/judgement/_thirdparty_16_overwrite_ruling_effect_2026_10_18.md` | repo | 43428 | `322582749c53` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 346 | `results/verdict/judgement/_three_seed_measurement_exec_2026_10_16.md` | repo | 48178 | `0e0716fde41f` | 否 | 落款字段行在·首个角色令牌＝`worker`（L186·署名·尾窗） | 不充判定件（落款面已核·无 VK 落款） |
| 349 | `results/verdict/judgement/_u01_u15_recheck_after_rulings_2026_10_17.md` | repo | 39219 | `71c6b834dd9d` | 否 | 落款字段行在·首个角色令牌＝`evidence-auditor`（L207·署名·尾窗） | 不充判定件（落款面已核·无 VK 落款） |
| 352 | `results/verdict/judgement/_u10_s3_denominator_rulings_effect_2026_10_18.md` | repo | 79234 | `97719ffddda6` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 353 | `results/verdict/judgement/_u5_referent_registry_correction_2026_10_12.md` | repo | 25048 | `111a76fa9667` | 否 | 射程内（首 16,000 B ∪ 末 4,000 B）**0** 落款字段行 | 不充判定件（落款面已核·无 VK 落款） |
| 354 | `results/verdict/judgement/_u5_semantics_resolution_2026_10_12.md` | repo | 24046 | `8b5f1a495a99` | 否 | 射程内（首 16,000 B ∪ 末 4,000 B）**0** 落款字段行 | 不充判定件（落款面已核·无 VK 落款） |
| 355 | `results/verdict/judgement/_u_axis_active_ruling_register_2026_10_16.md` | repo | 22219 | `30fed54c3d09` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落盘方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 357 | `results/verdict/judgement/_u_axis_input_vs_kdb2_recheck_2026_10_17.md` | repo | 25669 | `45e62039cee3` | 否 | 落款字段行在·首个角色令牌＝`evidence-auditor`（L160·署名·尾窗） | 不充判定件（落款面已核·无 VK 落款） |
| 360 | `results/verdict/judgement/_u_domain3_carrier_1494_2026_10_16.md` | repo | 42227 | `59f52f8bb287` | 否 | 落款字段行在·首个角色令牌＝`evidence-auditor`（L7·落盘方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 361 | `results/verdict/judgement/_u_lock_recalc_2026_10_17.md` | repo | 24411 | `6793b0b56925` | 否 | 落款字段行在·首个角色令牌＝`worker`（L197·署名·尾窗） | 不充判定件（落款面已核·无 VK 落款） |
| 362 | `results/verdict/judgement/_unclosed_47_status_review_2026_10_14.md` | repo | 46386 | `7cbfb9bc984e` | 否 | 落款字段行在·首个角色令牌＝`evidence-auditor`（L7·署名·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 363 | `results/verdict/judgement/_unified_caliber_document_2026_10_18.md` | repo | 41859 | `6cfadc256a33` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L8·署名·首窗） | 不充判定件（落款面已核·无 VK 落款） |
### §2-7 · 第 381–478 件（36 件）

| no | 件名（相对路径） | 仓 | bytes（自测） | SHA-12（自测） | 落款面在否 | 其落款之实（摘引） | 判 |
|:-:|:--|:--|--:|:--|:--|:--|:--|
| 381 | `results/verdict/judgement/_weighted_law_killline_prereg_2026_10_21.md` | repo | 69409 | `769b345d9bdf` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L7·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 382 | `results/verdict/judgement/_whitelist_and_scope_ruling_effect_2026_10_17.md` | repo | 56228 | `afd2a78e6a4f` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 385 | `results/verdict/judgement/_zerocall_criterion_redefinition_2026_10_17.md` | repo | 31602 | `f2bed1e98f62` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L7·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 387 | `results/verdict/pi_register/_pi_1009_eight_gap_enum_effect_2026_10_22.md` | repo | 92100 | `6f1bde118d01` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L8·落账方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 388 | `results/verdict/pi_register/_pi_card_payload_extraction_2026_10_20.md` | repo | 53460 | `f8545e95374f` | 否 | 落款字段行在·首个角色令牌＝`evidence-auditor`（L9·出件方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 389 | `results/verdict/pi_register/_pi_decision_backlog_consolidated_2026_10_21.md` | repo | 100274 | `87d3bac68420` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L1·(文首标题行·独立域)·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 392 | `results/verdict/pi_register/_pi_input_timeline_since_20261009_2026_10_22.md` | repo | 318489 | `5d0f272509d6` | **否** | L300「…**判断官卡面并置 verdict-keeper／protocol-keeper**，⛔ 0 代择」｜L595「**另议——verdict-keeper 出性质辨之判断件候你裁**」——命中源为卡面转引·非本件落款行 | 不充判定件（落款面已核·机械命中为卡面转引） |
| 393 | `results/verdict/pi_register/_pi_register_dedup_note_2026_10_21.md` | repo | 3911 | `ae893e953781` | 否 | 射程内（首 16,000 B ∪ 末 4,000 B）**0** 落款字段行 | 不充判定件（落款面已核·无 VK 落款） |
| 399 | `results/verdict/pi_register/_v4_pi_cot_v3_missing_ledger_correction_2026_09_28.md` | repo | 12851 | `44c4d570375c` | 否 | 落款字段行在·首个角色令牌＝`worker`（L166·出件·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 401 | `results/verdict/pi_register/_v4_pi_cot_v3_questionnaire_v2_d8_2026_09_28.md` | repo | 53581 | `238077d25919` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L260·出件·尾窗） | 不充判定件（落款面已核·无 VK 落款） |
| 403 | `results/verdict/judgement/_clearance_mini_rulings_closeout_register_2026_10_01.md` | sub | 31942 | `9238c2287af5` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L4·出证方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 404 | `results/verdict/judgement/_e6_n_distinct_judge_types_recompute_2026_10_10.md` | sub | 26304 | `82c5c143134e` | 否 | 落款字段行在·首个角色令牌＝`worker`（L8·出件·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 405 | `results/verdict/judgement/_e6_verdict_v3_rationale_review_2026_10_10.md` | sub | 39008 | `664e82968fc2` | **是** | L9「- **出件**：**verdict-keeper（判定收口官）**（分支会话 `mvs_7b98ed6186244b35961567bd6b14e1e2`…）」 | ★上修候选（真 VK 落款 ＋ 件别面＝裁因复核／重出件「判定文书收口面」·维持 FAIL 立案）⇒ 须 PI／VK 裁其是否计入判定件 |
| 407 | `results/verdict/judgement/_g4_e3_definition_ruling_material_2026_10_09.md` | sub | 30662 | `8ae4016bb41d` | 否 | 落款字段行在·首个角色令牌＝`worker`（L3·棒别·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 410 | `results/verdict/judgement/_kd04_c_denominator_closeout_register_2026_10_10.md` | sub | 23029 | `78481cc60494` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L9·本棒身份·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 411 | `results/verdict/judgement/_kd04_c_denominator_expansion_exec_2026_10_10.md` | sub | 27915 | `2caa3966b866` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L9·本棒身份·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 420 | `results/verdict/judgement/_kd_resolvability_and_optional_experiments_2026_10_09.md` | sub | 70328 | `53d4fa3a681f` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L92·落款·尾窗） | 不充判定件（落款面已核·无 VK 落款） |
| 427 | `results/verdict/judgement/_krj5_final_disposition_verdict_2026_10_11.md` | sub | 60700 | `2b6bf509a135` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L3·件性质·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 428 | `results/verdict/judgement/_krj_all_five_verdicts_rewrite_2026_10_11.md` | sub | 72247 | `78fb8c47c944` | **是** | L6「- **出件**：**verdict-keeper**（`agent-3a4d09ba3c90` · 分支会话 `mvs_bae6424c7bd04b919d5290d43b5fa125`）」 | ★上修候选·确凿（真 VK 落款 ＋ 件别面＝五终判改判件·L10「13／13 条已落五终判之一：pass 7／kd 6」）⇒ 须 PI／VK 裁其是否计入判定件 |
| 429 | `results/verdict/judgement/_krj_all_terminal_verdicts_2026_10_11.md` | sub | 95659 | `f52231807e36` | **是** | L8「- **出件**：**verdict-keeper**（`agent-3a4d09ba3c90` · 分支会话 `mvs_0a6cc783013b4db78d9a809eb1d13e96`）」 | ★上修候选·确凿（真 VK 落款 ＋ 件别面＝判死线逐条终判件·L12「13 条已逐条终判」）⇒ 须 PI／VK 裁其是否计入判定件 |
| 432 | `results/verdict/judgement/_kv3s_4_terminal_verdict_supplement_2026_10_09.md` | sub | 20211 | `0f82948defb3` | **是** | L1 标题「# K-V3S-4 终版判档件 · 两处旧态勘正补件 · verdict-keeper · 2026-10-09」 | 不充判定件（落款面已核·真 VK 落款；件别面＝勘正补件·自陈 ⛔0 改变 VK 之任何档位结论） |
| 435 | `results/verdict/judgement/_pending_rulings_drafts_2026_10_11.md` | sub | 42775 | `c8428b883029` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L4·本棒身份·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 436 | `results/verdict/judgement/_r2_verdict_179domain_arith_verification_2026_10_09.md` | sub | 30532 | `511c81b96745` | 否 | 落款字段行在·首个角色令牌＝`evidence-auditor`（L3·本件性质·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 437 | `results/verdict/judgement/_round56_v4_kd_row_correction_revision_2026_10_10.md` | sub | 23453 | `6d8537cb127f` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L13·出件·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 440 | `results/verdict/judgement/_s4_final_ruling_card_register_2026_10_09.md` | sub | 2135 | `f62401b619cc` | 否 | 落款字段行在·首个角色令牌＝`parent`（L4·出件·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 443 | `results/verdict/judgement/_s6doubleprime_verdict_supplement_2026_10_11.md` | sub | 31515 | `8e19c10ce219` | **是** | L7「- **出件**：**verdict-keeper**（`agent-3a4d09ba3c90` · 分支会话 `mvs_46811a86c64a4ef8aab1a563b3c96faa`）」 | 不充判定件（落款面已核·真 VK 落款；件别面＝另名补正登记件·自陈 ⛔非判定档位件·不新增任何终判档位） |
| 446 | `results/verdict/judgement/_t1_exp2_verdict_bytes_correction_2026_10_10.md` | sub | 13480 | `e863ca5fb157` | 否 | 射程内（首 16,000 B ∪ 末 4,000 B）**0** 落款字段行 | 不充判定件（落款面已核·无 VK 落款） |
| 455 | `results/verdict/judgement/_v5_gt8_lowarm_verdict_r2_2026_09_29.md` | sub | 40282 | `aff727434aa4` | **是** | L3「> **本件身份**：**verdict-keeper**（Mavis 团队 verdict-keeper，`agent-3a4d09ba3c90`）。」｜L211「**出件｜verdict-keeper**…」 | ★上修候选（真 VK 落款 ＋ 件别面＝r2 重裁件·L4 载「终档落定」）⇒ 须 PI／VK 裁其是否计入判定件 |
| 468 | `results/verdict/pi_register/_linestand_pi_signoff_2026_10_01.md` | sub | 35538 | `cb5d933f8fae` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L4·出证方·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 469 | `results/verdict/pi_register/_pending_pi_items_drafts_2026_10_11.md` | sub | 40678 | `55f469269d3d` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L3·件性质·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 470 | `results/verdict/pi_register/_pending_pi_items_master_register_2026_10_09.md` | sub | 35258 | `87ab4929477f` | 否 | 落款字段行在·首个角色令牌＝`worker`（L5·出件·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 472 | `results/verdict/pi_register/_pi_effectivity_declaration_register_2026_10_11.md` | sub | 54511 | `41a82bde5190` | 否 | 落款字段行在·首个角色令牌＝`doc-writer`（L5·本棒身份·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 473 | `results/verdict/pi_register/_pi_facing_items_screen_2026_10_09.md` | sub | 59604 | `a6d33cf318fe` | 否 | 落款字段行在·首个角色令牌＝`worker`（L5·出件·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 474 | `results/verdict/pi_register/_pi_give_a_class_pilot_design_2026_10_14.md` | sub | 103140 | `5ec0638e9498` | 否 | 落款字段行在·首个角色令牌＝`worker`（L6·署名·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 475 | `results/verdict/pi_register/_pi_pending_items_draft_package_2026_10_09.md` | sub | 51793 | `8fa2a7a2c49d` | 否 | 落款字段行在·首个角色令牌＝`protocol-keeper`（L4·本棒身份·首窗） | 不充判定件（落款面已核·无 VK 落款） |
| 478 | `results/verdict/pi_register/_v4_pi_cot_v3_lock_and_rejudge_register_2026_09_28.md` | sub | 12152 | `ae154971d1d2` | 否 | 落款字段行在·首个角色令牌＝`worker`（L153·出件·首窗） | 不充判定件（落款面已核·无 VK 落款） |
## §3 · `T3` 之加总自证（**AC-2**：252 · 容差 0）

### §3-1 · 逐件表之加总（**七批 × 36 件 ＝ 252**）

| 项 | 数 | 自证 |
|:--|--:|:--|
| 批次数 | **7** | §2-1 … §2-7，每批 **36** 件（36 × 7 ＝ **252** ✅） |
| 表内行数（`| no \|` 之行） | **252** | 本棒脚本实测：解析本件之表 ＝ **252** 行，`no` 之集合 ＝ 闭件 §7-1 之 478 中「非判定件」258 减 6 假阴 ⇒ **no 无重、无缺** |
| **在盘** | **252** | 逐件 `os.path.exists` ＝ True（252／252） |
| **不在盘** | **0** | — |
| **不可判（`NOT_MEASURED`）** | **0** | 逐件皆 `MEASURED`；**⛔0 按 `N_full` 填零**（本棒**逐件实测**得 0，非填零） |
| SHA-12 与在册逐位相符 | **252／252** | 对照 ＝ 闭件 §7-1 之在册 SHA-12 |
| bytes 与在册逐位相符 | **252／252** | 同上 |
| **落款面在否 ＝ 是（真 VK 落款）** | **16** | no 1／2／149／180／193／238／253／263／310／333／405／428／429／432／443／455 |
| 落款面在否 ＝ 否 · **机械假阳**（非真落款） | **6** | no 125／185／232／275／316／392（见 §2 各行「其落款之实」） |
| 落款面在否 ＝ 否 · **无命中** | **230** | 射程内 0 落款字段行（230 件） |
| **加总自证** | **16 ＋ 6 ＋ 230 ＝ 252 ✅** | **容差 0** |
| **判之分布** | ★上修候选 **6**（no 238／310／405／428／429／455）／不充判定件 **246** | 246 ＋ 6 ＝ **252 ✅** |

### §3-2 · `T3` 之读数（**如实报·不软化**）

> 📌 **「未核件数」由 252 → 0**：丙面 252 件之**落款面**已**逐件核毕**（252／252 实测·0 不可判）⇒ **`T3` 之该阈值（未核件数 ＝ 0）之面已补**。**然 ⛔0 代裁该阈值成立**——`T3` 之阈值系门③ 核件 §5-2 所立、**待 PI 采认后方为已立**（门③ 核件 §5-2 末逐字：「阈值之纪律…须经 PI 采认后方为已立；本件⛔0 代裁·⛔0 宣告门③ 成就」）。
> 📌 **附带实得（上修面·须 PI／VK 裁）**：252 件中 **6 件**兼具「**真 VK 落款**」与「**判定面件别／承载判定面**」：

| no | 件 | 件别面（口径乙取值） | 判定面之实（逐字） | 若采计入之影响 |
|:-:|:--|:--|:--|:--|
| 238 | `results/verdict/judgement/_kv3s_4_4_rejudge_2026_10_09.md` | `：重判件` | L3「**重判件**（`K-V3S-4-4` 档位）…**逐线重判**（`hit` 布尔 ＋ 档位 ＋ 根因三分类 ＋ 依据）」 | 底数 **111 → 117** |
| 310 | `results/verdict/judgement/_s3_th_v21_reconciliation_verdict_2026_10_01.md` | `登记` | L1「**依 F-5 口径 A（74）重裁件**」｜L16「**性质**：**判定面重裁件**（补充重裁 · 并列记）」｜L5「PASS 与 KD 均按判据字面直陈」 | 底数 **111 → 117** |
| 405 | `results/verdict/judgement/_e6_verdict_v3_rationale_review_2026_10_10.md` | `：裁因复核／重出件` | L3「**裁因复核／重出件（判定文书收口面）**…**⛔ 0 翻案六线判定**（5/6 hit → **FAIL 立案维持**）」 | 底数 **111 → 117** |
| 428 | `results/verdict/judgement/_krj_all_five_verdicts_rewrite_2026_10_11.md` | `：五终判改判件` | L10「**13／13 条已落五终判之一**：**`pass` 7**／**`kd` 6**」 | 底数 **111 → 117** |
| 429 | `results/verdict/judgement/_krj_all_terminal_verdicts_2026_10_11.md` | `：判死线逐条终判件` | L12「**13 条已逐条终判** —— 全闭 7 · 附条件闭·条件 4 · 维持挂账 2」 | 底数 **111 → 117** |
| 455 | `results/verdict/judgement/_v5_gt8_lowarm_verdict_r2_2026_09_29.md` | `：r2重裁件` | L4「**r2 重裁件（新名）**＝载 PI 轮 6 裁…在该面的**终档落定**」 | 底数 **111 → 117** |

> 📌 **本棒⛔0 代裁**：「该 6 件**是否属母件之『判定件』」**属口径裁**（母件 0 处给出全集定义 ⇒ 真全集机械不可得·EA 审计 §3-6）⇒ 本棒**只呈事实**（6 件具真 VK 落款且具判定面），**不裁其计入与否**。
> 📌 **若采计入之连带面（如实登记）**：底数 111 → **117**（77 ＋ 28 ＋ 6 ＋ **6**）⇒ 则门③ 核件 §3 之 111 行表须**增补 6 行**（本棒**⛔0 回改门③ 核件一字**）·且 `T4`「底数一致性差 ＝ 0」之射程随之变动。
> 📌 **另 10 件真 VK 落款者（no 1／2／149／180／193／253／263／333／432／443）之定性**：其件别面分别为现值复测件／归属认定件／登记面之现态更新件／可翻转性判读件／裁议件／代价对照件／条件④成就之判读件／PI 裁之生效落账件／勘正补件／另名补正登记件，且**逐件自陈 ⛔0 落五终判**（或 ⛔非判定档位件／⛔0 代裁／候 PI 裁）⇒ **落款方成立而判定件属性不成立** ⇒ **不充**。**此 6＋10 之分野之判准 ＝「真落款」＋「件别面／正文是否承载判定面」·归 PI／VK。**

---

## §4 · `T5` 之 2 处名差（**AC-3 ＋ AC-4**）

### §4-1 · 两侧字面直取（**回源·逐字**）

**（甲）机械表侧（`state` 之在册读）**——机械表本体 `.tmp/_gate3_478_mech.json` 今**不在盘**（§1-1 环 ④），故其 `state` 之在册读由**两处互证**之逐件登记取得：

| 源（相对 `deposon-repo`） | bytes（自测） | SHA-12（自测） | 所载逐字 |
|:--|--:|:--|:--|
| `results/evidence/register/_gate3_125_undetermined_2026_10_23.md`（在册「无件性质栏（不可判）」125 面之逐件登记） | 185,271 | `83d1b85ac0a3` | **L1340**：「**㊤ no 433** · \`_limb_reading_verdict_kv3s33_2026_10_01.md\` · \`c5866ce87d9c\` · 56,329 B · sub」｜**L1365**：「**㊨ no 447** · \`_t1_gate_closure_and_recompute_verdict_2026_10_01.md\` · \`0b5fb78727c2\` · 72,934 B · sub」⇒ **二者皆在「无件性质栏（不可判）」125 面之内** |

**（乙）EA 审计侧（逐字·自测）**——`results/evidence/register/_gate3_108_ea_audit_2026_10_24.md`（44,650／`8ebb365be944`）：

> 📌 **L190**：「| 433 | \`results/verdict/judgement/_s3_kv3s_3_verdict_2026_10_01.md\` | 乙B | **非判定件**（别名首 14 字不含判定／判断／裁决） | **无件性质栏（不可判）** | **读甲**＝「其件性质栏别名前 14 字不属判定族 ⇒ 非判定件」／**读乙**＝「其件性质栏缺失 ⇒ 不可判」；**两读同向·皆不充判定件**；且该件之判定件归属系**口径丙**（落款面）所补定（合成件 §2-4-② 之 no 433 行）⇒ **甲面／乙面之口径差·非分类之误** |」
> 📌 **L191**：「| 447 | \`results/verdict/judgement/_t1_gate_closure_and_recompute_verdict_2026_10_01.md\` | 乙B | **非判定件** | **无件性质栏（不可判）** | **同上**（合成件 §2-4-② 之 no 447 行之支撑通道＝**三读全命中**） |」
> 📌 **L271**：「- **(c) 分类正确性 —— 绿而有 2 处名差**：口径乙三步复算 **109／111 与机械表逐位相符**；**2 处名差**（no 433／no 447）**两读同向**（皆不充判定件）⇒ **非实质分歧**（§2-2）。」
> 📌 **L289**：「2. **呈 PI（2 处分类名差）**：no 433／no 447 之口径乙面与机械表面之**名差**（两读同向·§2-2）⇒ **登记级**·⛔ 本棒 **0** 改判·**无须** PI 之裁（仅登记）。」

**（丙）本棒开卷实测（第三侧·逐字）**：

| no | 在册之件（自测 SHA-12／bytes） | 头 16,000 B 内「件性质／件别」之行（逐字） | 其真落款行（逐字） |
|:-:|:--|:--|:--|
| 433 | `_limb_reading_verdict_kv3s33_2026_10_01.md`／`c5866ce87d9c`／56,329／**sub** | **L13**「## §0 件性质 · 授权面 · 边界」｜**L15**「### §0.1 件性质」⇒ **两行皆为节标题·非字段式标签·取值皆空** | **L3**「> **本棒身份**：**verdict-keeper**（判定收口官 · \`agent-3a4d09ba3c90\`，本件实际出件者）。本件**只作 \`K-V3S-3-3\` 后半档位之判读与根因裁决**。」 |
| 447 | `_t1_gate_closure_and_recompute_verdict_2026_10_01.md`／`0b5fb78727c2`／72,934／**sub** | **L12**「## §0 件性质 · 授权面 · 登记源」⇒ **节标题·取值空** | **L4**「> **本棒身份**：**verdict-keeper**（判定收口官 · \`agent-3a4d09ba3c90\`，本件实际出件者）。」 |

> 📌 **旁证（第三侧·在册）**：125 件件 **L1341–L1342**（no 433）「**口径丙之判**：**vK 落款**（**三读全命中**）…**合成判**：**判定件**（落款方＝**判官**）」｜**L1366–L1368**（no 447）同 ⇒ **二件之真落款方 ＝ `verdict-keeper`**、且**已在乙面 28 之内**（**已在 111 底数中**）。

### §4-2 · 名差之性质（**三择一·给据**）

| 择 | 判 | 依据（实测·回源） |
|:-:|:--|:--|
| ② **真的两件**（机械表多算／少算） | ❌ **不成立** | 机械表之 `state` 为**逐 no 单值**（478 行之 `rows` 含 `no`／`sha12`／`path`／`state`／`alias`／`sha_match`，`state` 无多值）；本棒实测 no 433 之 SHA-12 **唯一**指向 `_limb_reading_verdict_kv3s33_2026_10_01.md`（`c5866ce87d9c`），no 447 唯一指向 `_t1_gate_closure_and_recompute_verdict_2026_10_01.md`（`0b5fb78727c2`）⇒ **同一 `no` 两侧所指为同一件·无重复·无漏计**。 |
| ③ **笔误** | ⚠ **部分成立（另一层）** | **EA 审计 L190 之 no 433 行所记件名 `_s3_kv3s_3_verdict_2026_10_01.md`（35,037 B／自测 SHA-12 `e394bb6b5ddf`）实为在册 no 438 之件**（在册 no 438 之 SHA-12 ＝ `e394bb6b5ddf`，见 125 件件 §29-1 与 合成件 §2-4-② 之 no 438 行）；**在册 no 433 之件名为 `_limb_reading_verdict_kv3s33_2026_10_01.md`（`c5866ce87d9c`）** ⇒ **EA L190 之件名名实不符（笔误型）**。**no 447 行（L191）之件名与在册逐位相符**（无此型）。 |
| ① **同件异名（口径不一）** | ✅ **主性质成立** | **两读之差之实体 ＝ 同一判别式（口径乙）之下、「键存在而值为空」之处置不同**：机械表（脚本）**取值失败即跳过该行**、无他行可取值 ⇒ 归「无件性质栏（不可判）」；EA 三步复算 **键存在即 step ① 成立**、step ② 取值空 ⇒ step ③ 无族词 ⇒ 归「非判定件」。本棒复算**两读各施一遍**：字面三步读 ⇒ 「非判定件」；跳过读 ⇒ 「无件性质栏（不可判）」⇒ **两读互斥而各自自洽** ⇒ **此非判别式之误，乃口径之别**。**且两读同向（皆不充判定件）·非实质分歧**——与 EA L271／L289 之自陈一致。 |

> 📌 **实体孰为准（供参考·不代裁）**：二件之「件性质」行**皆为节标题**（`## §0 件性质 · 授权面 · 边界`／`### §0.1 件性质`／`## §0 件性质 · 授权面 · 登记源`）⇒ 其**自载别名不存在** ⇒ 就**件别面**而言，「不可判」为**实体上更准**之读；EA 之「非判定件」为其**归类标签**之别。**⛔0 据此代裁**。
> 📌 **名差不改底数（两面皆然）**：二件之真落款方 ＝ `verdict-keeper`（口径丙·三读全命中）⇒ 其判定件归属**已由乙面 28 收录**（125 件件 §29-1 逐字）⇒ **无论采甲读或乙读，二件皆已在 111 之内**——**除非**乙读导致乙面之取件面改口径（见 §4-3 甲／乙之连带面）。

### §4-3 · 处置（**AC-4**：勘正之形 或 两读并出 ＋ 处置后之读数）

> 📌 **本棒所采之处置形 ＝ 两读并出 ＋ 登记级勘误（append-only·⛔0 回改 EA 审计件一字·⛔0 回改门③ 核件一字）**：

**勘误①（名实不符·笔误型·登记面）**——以**本件**为唯一登记面：

> 📌 EA 审计 §2-2 之 **L190** 行，no 433 所记件名 `_s3_kv3s_3_verdict_2026_10_01.md`（35,037 B／自测 SHA-12 `e394bb6b5ddf`）**名实不符**：该指纹在册为 **no 438**（`_s3_kv3s_3_verdict_2026_10_01.md`）；**在册 no 433 之件** ＝ `results/verdict/judgement/_limb_reading_verdict_kv3s33_2026_10_01.md`（**sub**／56,329 B／自测 SHA-12 `c5866ce87d9c`·在册 125 件件 L1340 逐字）。⇒ **以本节为准**（勘误注记·**前文一字未改**）；**⛔0 回改 EA 审计件**；**该行之「口径乙三步复算 ＝ 非判定件」之结论不受影响**（二件之复算态经本棒实测**同为**「无件性质栏（不可判）」之机械表读，见 §4-2 之 ① 之依据）。

**勘误②（口径之别·定性·登记面）**——`T5` 之 2 处名差 **＝ 「同件异名·口径不一」**，其差之实体 ＝ **「键存在而值为空」之处置不同**；**成因之可机械判之据 ＝ 二件之「件性质」行皆为节标题（非字段式标签）** ⇒ 其自载别名不存在。**两读同向·皆不充判定件·非实质分歧**（与 EA L271／L289 同向·并补其成因之据）。

**须 PI／VK 择者之一**（**本棒⛔0 代裁**）：

| 读 | 内容 | 连带面（诚实推演） | **`T5` 之读数** |
|:--|:--|:--|:--|
| **甲** | 采「**不可判**」为该 2 件之分类（＝机械表与 125 件件**两处互证**之在册读） | 三面计数 ＝ 95／258／125 **不变**；乙面 28 **不变**；底数 **111 不变**；该 2 件**已在**乙面 28（口径丙补定）之内 | **0** |
| **乙** | 采「**非判定件**」为该 2 件之分类（＝EA 之字面三步读） | 不可判 125 → **123**、非判定件 258 → **260**；乙面 28 → **26**（若取件面随之改口径）⇒ 底数 111 → **109**；**或**若另立「有 VK 落款即入判定件」之补定面 ⇒ 二件仍入 ⇒ 底数 **111 不变** | **2** |

> 📌 **`T5` 之阈值的第二支（门③ 核件 §5-2 逐字）**：「计『口径乙复算与机械表 \`state\` 不符』之件数（**或** PI 明裁其 2 处名差为『非实质差·登记级·可容』）」⇒ **若 PI 采此支**，则即便乙读成立，`T5` 之**未消解**数亦为 **0**（**须 PI 之裁·本棒⛔0 代裁·本棒亦不预裁**）。
> 📌 **本棒之现读数（如实呈面）**：按**甲读**（在册读·两处互证）⇒ `T5` ＝ **0**；按**乙读**⇒ `T5` ＝ **2**。**本棒不宣告 0**；**呈 PI 一言择之**（PI 不择 ⇒ 仍为 2）。
> 📌 **附（R4 面·不擅动）**：EA 审计件之「108」→「111」之**勘正件**仍未另立（门③ 核件 R4 行；`pi_rulings/_pi_card_answers_register_2026_10_24_v269.md` L113 载「待办」）⇒ **本棒⛔0 代立**（⛔0 回改审计件一字）——**可由本棒另立该勘正件，待 PI 一令**；**本棒不预立·不预裁**。

---

## §6 · 本件之限（**failures & limitations·不软化**）

1. **母件之结构限（承之·非掩之）**：母件 L160 之判据对象是「**全部**判定件」，而母件 **0 处**给出「判定件」之全集定义 ⇒ **真全集机械不可得**（EA 审计 §3-6 L250–L252）⇒ 本件**只**把 `T3` 之**已核集合**（丙面 252 件）之落款面核毕，**⛔0** 断言母件「全部判定件」已闭 ⇒ 门③ 之**全称量词仍未证**（`R3` 未消解）。
2. **`T3` 之射程限**：落款面之判 ＝ **读乙射程（首 16,000 B ∪ 末 4,000 B）** 之内 + 三读并测 + **开卷定性**；**射程外**另有 10 件次命中（已登记·未改判）；**口径丙之假阳面**（在册闭件 §2-3 自陈「假阳性实测」·125 件件 §3-1「命中行 ≠ 落款行」）**本棒以开卷定性收口**，**⛔0** 断言其假阳率已闭。
3. **上修面未裁**：§3-2 之 6 件上修候选**是否属「判定件」**属口径裁 ⇒ 底数 111 或为 111、或为 117（或 109，取决于 `T5` 之读）⇒ **本棒三读并存·不预裁**。
4. **`T5` 之读未择**：§4-3 甲／乙两读之差 ＝ 2 件·且牵动底数之数 ⇒ **本棒不宣告 0**；**待 PI 一言**。
5. **分母表本体不在盘**：`.tmp/_gate3_478_mech.json`（在册 `6d80ae1b7b35`／178,680）今**不在三根** ⇒ 本棒以闭件 §7-1 之 478 行**重建**分母并复现其三面计数（§1-2 正控）⇒ **该缺须 PI／主代理知**（登记级·非实体缺陷）。
6. **本棒仪器之失（自陈）**：首轮口径乙复算因「表格行取值未取下一格」而得 28／89／358（与在册 95／258／125 严重不符）⇒ **修仪器**（取值规则）**不修在册文本**；修正后与在册**逐位全等**。另闭件 §7-1 有 3 行带尾附格「【已审】」⇒ 解析规则补之（**在册表体例之容许·不改在册件一字**）。
7. **本棒之落款面检测器**：假阳经**开卷定性**逐件排除 6 件（免责语 3／派工登记面 1／归责语 1／他棒落款 1／卡面转引 1）⇒ **本棒不宣称「零假阳」**，仅宣称「本 252 件之假阳**已逐件识别并登记**」。
8. **⛔ 本棒 0 判之清单**：⛔ 0 落五终判 · ⛔ 0 判门③ 成就 · ⛔ 0 宣告任何零 · ⛔ 0 代 PI 裁 · ⛔ 0 代销记 · ⛔ 0 判任一判定件之实体面 · ⛔ 0 判任一件是否属母件「判定件」 · ⛔ 0 改门③ 核件一字 · ⛔ 0 改 EA 审计件一字 · ⛔ 0 移动／重命名／删除既有件 · ⛔ 0 跑实验 · ⛔ 0 联网 · ⛔ 0 读 key／`.env` · ⛔ 0 读 `〔本地路径已脱敏〕` · **归档区 0 写入 · 0 读正文**（**仅按名枚举 1 次**：为定位机械表 JSON，匹配式 `gate3_478`／`mech`；命中 0 件；**所读件与其指纹：无——未读任何正文**）。

---
## §5 · 自证（**AC-5**）

### §5-1 · 字节五项（本件之实测·**本节写入前一刻之状态**）

| 项 | 值 | 测法 |
|:--|:--|:--|
| bytes | **101,147** | `python -P .tmp/_bcheck.py '<本件>'` |
| SHA-12 | **`808057d441d2`** | 同上（SHA-256 前 12 位·**⛔0 用内建 `hash()`**） |
| BOM | **0** | 同上 |
| CR | **0** | 同上（纯 LF） |
| VT | **0** | 同上 |
| U+FFFD | **0** | 同上 |
| 末字节 | **0x0a** | 同上（末行有换行） |
| LF 行数 | 470 | 同上 |

> 📌 **口径说明（如实）**：上列 ＝ **本节（§5）写入前一刻**之实测；**本节写入后之最终值见本件末行自报**（本棒末行以 `Get-Item` ＋ `_bcheck.py` 复测后写入）⇒ **两次测量皆由本棒亲跑·皆附时点**。
> 📌 **本棒之落盘方式**：本件共 **9 次前缀核追加**（`_append_generic.py`：BOM 0／CR 0／末字节 0x0a／FFFD 0 之正文核 ＋ **前像 bytes＋SHA-12 双条件核对** ＋ 追加后 `PREFIX_IDENTICAL=True` 复查）⇒ **⛔0 用 `Write` 覆盖任何既有内容**（`Write` 仅用于**首次创建**本件与生成本棒之 `.tmp` 正文碎片）。

### §5-2 · 触动既有件数 ＝ **0**

| 面 | 证据 | 判 |
|:--|:--|:--|
| **被核之 252 件** | 逐件现值 SHA-12 与 bytes **与闭件 §7-1 在册值逐位相符 252／252**（§2 各行·§3-1）⇒ **0 件被改** | ✅ |
| **分母之 478 件** | 逐件现值 SHA-12 与 bytes **与在册逐位相符 478／478**·不在盘 0（§1-2 正控③）⇒ **0 件被改** | ✅ |
| **九件关键源件** | 门③ 核件／EA 审计／闭件／源件 B／母件／125 件件／41 件 v2／478 机械审计件／faceA 清单：SHA-12 与在册**逐位相符**（§5-3）⇒ **0 件被改** | ✅ |
| **门③ 核件一字** | 本棒**未对其作任何写入**（只读 ＋ 自测指纹） | ✅ |
| **EA 审计件一字** | 本棒**未对其作任何写入**（只读 ＋ 自测指纹）；`T5` 之勘误**只登记于本件**（§4-3 勘误①②） | ✅ |
| **归档区** `〔归档区〕` | **0 写入**·**0 读正文**·**仅按名枚举 1 次**（为定位机械表 JSON·命中 0） | ✅ |
| **`〔本地路径已脱敏〕`** | **只读**（252 件中 6 件位 sub·逐件读并算 SHA-12·0 写） | ✅ |
| **本棒新增件** | **1**（本件，位于 `results/verdict/judgement/`）＋ `.tmp` 之自建仪器与正文碎片（**仪器区·非登记面**） | 登记 |

### §5-3 · 引证清单（**每一指纹皆本棒自测·附观测时点**）

| # | 件（相对 `deposon-repo`；`sub` 者标之） | bytes（自测） | SHA-12（自测） | mtime（自测） | 观测时点 | 本件引于 |
|:-:|:--|--:|:--|:--|:--:|:--|
| 1 | `results/verdict/judgement/_gate3_111_filing_confirm_2026_10_28.md` | 75,768 | `6a870245a820` | 2026-10-28 11:49:29 | 13:29 | §0／§1-1 环①／§5-2 |
| 2 | `results/evidence/register/_gate3_108_ea_audit_2026_10_24.md` | 44,650 | `8ebb365be944` | 2026-10-24 01:15:54 | 13:31 | §0／§1-1 环②／§4-1／§4-2 |
| 3 | `results/evidence/register/_gate3_judgement_set_closure_2026_10_23.md` | 125,068 | `d48666ad32b6` | 2026-10-23 15:56:37 | 13:33 | §1-1 环⑤／§1-2／§4-1 |
| 4 | `results/verdict/judgement/_gate3_three_numbers_synthesis_2026_10_23.md` | 31,484 | `bf4515ff2e0b` | 2026-10-23 23:53:34 | 13:32 | §1-1 环③／§4-1（合成件 §2-4-②） |
| 5 | `results/readout/run/_v34_experiment_gap_plan_2026_10_08.md`（**母件**） | 36,066 | `996feb1db9cb` | 2026-10-08 16:46:11 | 13:38 | §0／§6-1（**L160 逐字回源**） |
| 6 | `results/evidence/register/_gate3_125_undetermined_2026_10_23.md` | 185,271 | `83d1b85ac0a3` | 2026-10-23 23:24:08 | 13:36 | §1-2 正控①／§4-1 甲侧／§4-2 |
| 7 | `results/verdict/judgement/_41_items_status_verdict_v2_2026_10_23.md` | 24,375 | `0522de54eaa4` | 2026-10-23 23:02:01 | 13:36 | §1-1 环④／§1-3（字段表 12 键） |
| 8 | `results/evidence/register/_gate3_478_mech_audit_2026_10_23.md` | 6,679 | `b04b8db96b26` | 2026-10-23 21:57:15 | 13:34 | §1-1 环④／§1-2（取值修正） |
| 9 | `results/evidence/register/_gate3_faceA_itemlist_register_2026_10_24.md` | 38,840 | `512b31f1a1ed` | 2026-10-24 02:07:25 | 13:38 | §1-3（faceA §4-2 之标签式规则） |
| 10 | `pi_rulings/_pi_card_answers_register_2026_10_24_v269.md` | 9,398 | `0cee727234cf` | 2026-10-24 02:0x | 13:51 | §4-3 附（R4 面·**L113 逐字**：「须另立勘正件（⛔0 回改原审计件）——**待办**」） |
| 11 | `sub:` `results/verdict/judgement/_limb_reading_verdict_kv3s33_2026_10_01.md`（**在册 no 433**） | 56,329 | `c5866ce87d9c` | 2026-10-10 11:37:24 | 13:51 | §4-1 丙／§4-2／§4-3 |
| 12 | `sub:` `results/verdict/judgement/_t1_gate_closure_and_recompute_verdict_2026_10_01.md`（**在册 no 447**） | 72,934 | `0b5fb78727c2` | 2026-10-10 11:37:23 | 13:51 | §4-1 丙／§4-2／§4-3 |
| 13 | `sub:` `results/verdict/judgement/_s3_kv3s_3_verdict_2026_10_01.md`（**在册 no 438**） | 35,037 | `e394bb6b5ddf` | 2026-10-10 11:37:23 | 13:51 | §4-2 ③／§4-3 勘误① |
| 14 | `.tmp/_gate3_478_mech.json`（**原分母表·今不在盘**） | 在册 178,680 | 在册 `6d80ae1b7b35` | — | 13:30（**三根按名枚举 0 命中**） | §1-1 环④／§4-1 甲侧／§6-5 |
| 15 | **252 件之全体**（§2 各行所列） | 逐件 | 逐件 | — | 13:3x | §2／§3-1 |

> 📌 **本件之自建仪器（`.tmp` 之自建件·非登记面）**：`_t3_t5_derive_2026_10_28.py`／`_t3_t5_calib.py`／`_t3_t5_detail.py`／`_t3_scan252.py`／`_t3_dump_hits.py`／`_t3_final.py`／`_t3_gen_table.py`／`_t3_cite.py`／`_t3_cite2.py`／`_t3_hdr.py`／`_t3_hdr2.py`／`_t3_diag.py`／`_t3_252.json`／`_t3_hits_context.txt`／`_body_*.md`（正文碎片）｜**⛔0 回改任何既有件·⛔0 移动／重命名既有件**（本棒曾以运行时可恢复删除通道清理自建碎片，因该通道以「targets-only trash marker」拒收而**未成**——**如实登记**：`.tmp` 内留有自建碎片若干，**位登记面排除区**，**0 件既有件受累**）。

---

## §7 · 状态行

`门③ T3／T5 补面 · T3：丙面 252 件逐件核毕（在盘 252／不可判 0／SHA-12 逐位相符 252）· 落款面：真 VK 落款 16／机械假阳 6／无命中 230（16+6+230=252 ✅）· 上修候选 6（no 238/310/405/428/429/455）待 PI／VK 裁 · T5：2 处名差定性 ＝「同件异名·口径不一」（键存在而值为空之处置不同·两读同向·非实质分歧）＋ 勘误① EA L190 no 433 件名名实不符（其实为 no 438 之件）· T5 读数 ＝ 甲读 0／乙读 2·待 PI 一言择之 · 触既有件 0 · 归档区 0 写 0 读正文 · ⛔0 落五终判 · ⛔0 判门③ 成就 · ⛔0 宣告任何零 · 呈 PI／VK`

**落款**：`evidence-auditor`（证据链审计官 · agent-11335500b168）· 分支会话 `mvs_0cbd4f6c009c4fea89d73c672504bdea` · 2026-10-28 13:2x–13:5x GMT+8 · ⛔ 0 落五终判 · ⛔ 0 代 PI 裁 · ⛔ 0 回改任何既有件一字 · ⛔ 0 跑实验 · ⛔ 0 联网 · ⛔ 0 读 key／`.env` · ⛔ 0 读 `〔本地路径已脱敏〕` · 归档区 0 写 0 读正文

---
## §8 · 节序注记 ＋ 末行自报（**append-only·以本节为准**）

> 📌 **节序勘正（体例·不掩）**：本件之**节号**与**物理次序**不一致——**§6（本件之限）之物理位置在 §5（自证）之前**，因 §6 随 §3／§4 同批落盘（**append-only·⛔0 回改既有内容**）⇒ **以节号为准**；§5（自证）与 §6（之限）**内容互不依赖**（§5 之引证清单含 §6 之限项之实测件，§6 不引 §5 之数）⇒ **不构成循环引用·不须回改**。
> 📌 **表内 252 行之终检（本棒于落盘后对**本件自身**之表复算·非引脚本原值）**：表行 **252**｜`no` 唯一值 **252**｜最小 1／最大 478（**非连续为必然**——252 ≠ 478 之连续区间，因 6 件假阴与 125／95 两面已剔）｜**落款面在否「是」＝ 16**＋**「否」＝ 236**＝ **252 ✅（容差 0）**｜批次节 **7**（§2-1…§2-7·每批 36 件）｜`★上修候选` 于 §2 表内 **6 行**（另 §3-1 汇总行 1 处提及·全件提及共 7 处）。
> 📌 **本棒之落盘次数 ＝ 10**（首次创建 1 ＋ 前缀核追加 **9**：B1 §1／B2–B8 §2 七批／B9 §3＋§4＋§6／B10 §5＋§7／B11 本节）⇒ **⛔0 攒到最后一并写**（每批皆即时落盘并有独立前缀核）。

### §8-1 · 末行自报（**本行写入前一刻之实测**）

> 📌 **我落盘了**：`〔幽灵引用·未上传:_gate3_t3_t5_closeout_2026_10_28.md〕`
>
> | 项 | 实测值 | 测法（可复跑） |
> |:--|:--|:--|
> | `Test-Path` | **True** | `Test-Path -LiteralPath '<路径>'` |
> | bytes | **108,325**（本行写入前一刻） | `Get-Item -LiteralPath '<路径>'` ／ `python -P .tmp/_bcheck.py '<路径>'` |
> | SHA-12 | **`71a3f32012d3`**（本行写入前一刻） | 同上（SHA-256 前 12 位·⛔0 用内建 `hash()`） |
> | mtime | **2026-10-28 13:52:19** | `Get-Item … .LastWriteTime` |
> | 字节五项 | BOM **0**／CR **0**／VT **0**／FFFD **0**／末字节 **0x0a** | `python -P .tmp/_bcheck.py '<路径>'` |
> | **节数** | **§0…§8 共 9 节**（其中 §2 含 **7** 个子批 §2-1…§2-7） | 逐节标题实测 |
> | **252 件之加总自证** | 表行 **252**；在盘 **252**／不在盘 **0**／**不可判（`NOT_MEASURED`）0**；落款面「是」**16**＋「否」**236**＝**252 ✅（容差 0）**；判 ＝ ★上修候选 **6** ＋ 不充判定件 **246** ＝ **252 ✅** | 对**本件自身**之表复算 |
> | 触动既有件数 | **0**（被核 252 件 SHA-12 逐位相符 252／252；分母 478 件 478／478；九件关键源件逐位相符；归档区 **0 写 0 读正文**；sub 只读） | §5-2 |
> | 归位／归件 | **无**（本棒**未**归位任何件·**未**移动／改名／删除任何件） | §5-2 |
> | 本行写入后之最终值 | ＝ 上列 bytes ＋ 本行正文之字节数 | 复跑 `_bcheck.py` 即可实测 |
>
> **末行**：`门③ T3／T5 补面件已落盘 · 落盘路径 〔幽灵引用·未上传:_gate3_t3_t5_closeout_2026_10_28.md〕 · 本行写入前一刻 108,325 B／71a3f32012d3／2026-10-28 13:52:19 · 节数 §0…§8 ＝ 9（§2 含 7 子批）· 252 件加总 252 ✅（在盘 252／不可判 0／是 16＋否 236／上修候选 6＋不充 246）· 触既有件 0 · 归档区 0 写 · ⛔0 落五终判 · ⛔0 判门③ 成就 · ⛔0 宣告任何零 · 呈 PI／VK`

---
## §9 · 勘正与终检（**append-only·以本节为准·前文一字未改**）

> 📌 **勘正①（计数口径）**：§8 之「`★上修候选` 于 §2 表内 **6 行**（另 §3-1 汇总行 1 处提及·**全件提及共 7 处**）」一句，其中「**全件提及共 7 处**」为**该节写入前**之字面计数；§8 自身及其后各节之**汇总复述**亦含该字面 ⇒ 全件之字面提及数随之增加。**以「§2 表内 6 行」为准**（终检实测：`★上修候选` 于 §2 之 252 行中命中 **6 行**·其 `no` ＝ 238／310／405／428／429／455）⇒ **上修候选之实数 ＝ 6**，**汇总复述不增其实数**。

> 📌 **终检（本节写入前一刻·本棒亲跑）**：

| 项 | 实测 | 测法 |
|:--|:--|:--|
| 本件 bytes | **111,766** | `python -P .tmp/_bcheck.py '<本件>'` |
| 本件 SHA-12 | **`0633164328ea`** | 同上 |
| 本件 mtime | **2026-10-28 13:53:05** | `Get-Item` |
| 字节五项 | BOM **0**／CR **0**／VT **0**／FFFD **0**／末字节 **0x0a** | 同上 |
| §2 表行数 | **252**｜`no` 唯一 **252** | 对本件自身之表复算 |
| 落款面「是／否」 | **16 ＋ 236 ＝ 252 ✅** | 同上 |
| 批次节 | **7**（§2-1…§2-7） | 同上 |
| 节数 | §0…§9 ＝ **10 节** | 逐节标题实测 |
| **触既有件** | **0**——十件关键源件指纹**终检 10／10 相符**（门③ 核件 `6a870245a820`／EA 审计 `8ebb365be944`／闭件 `d48666ad32b6`／源件 B `bf4515ff2e0b`／母件 `996feb1db9cb`／125 件件 `83d1b85ac0a3`／41 件 v2 `0522de54eaa4`／478 机械审计件 `b04b8db96b26`／faceA 清单 `512b31f1a1ed`／v269 `0cee727234cf`）＋ 被核 252 件 SHA-12 逐位相符 252／252 ＋ 分母 478 件 478／478 | §5-2 |

> 📌 **落盘次数 ＝ 11**（创建 1 ＋ 前缀核追加 **10**）⇒ 每批皆即时落盘·各有独立前缀核（`PREFIX_IDENTICAL=True` 复查 10／10）。
> 📌 **⛔ 本件之自限（终版复述）**：⛔ 0 落五终判 · ⛔ 0 判门③ 成就 · ⛔ 0 宣告任何零 · ⛔ 0 代 PI 裁 · ⛔ 0 代销记 · ⛔ 0 改门③ 核件一字 · ⛔ 0 改 EA 审计件一字 · ⛔ 0 移动／重命名／删除既有件 · ⛔ 0 跑实验 · ⛔ 0 联网 · ⛔ 0 读 key／`.env` · ⛔ 0 读 `〔本地路径已脱敏〕` · 归档区 **0 写 · 0 读正文**。
> 📌 **呈面（呈·非裁）**：① `T3` 之未核数 252 → **0**（面已补·阈值待 PI 采认）；② 上修候选 **6** 件之归属待 PI／VK 一言（采计入 ⇒ 底数 111 → 117）；③ `T5` 之 2 处名差已定性 ＝ **「同件异名·口径不一」** ＋ **勘误①（EA L190 no 433 件名名实不符）**，读数 ＝ **甲读 0／乙读 2**·待 PI 一言择之；④ 原分母表 `.tmp/_gate3_478_mech.json` **今不在盘**（在册 `6d80ae1b7b35`／178,680）·本棒以闭件 §7-1 重建并复现其三面计数——**此缺须 PI／主代理知**。

---
