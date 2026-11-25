# 幽灵引用清单 · 载路径今盘 0 命中之逐件对账（2026-10-25 · `evidence-auditor`）

| 项 | 值 |
|:--|:--|
| **件性质** | **清单（登记面）**——奉 PI 卡答「**甲：立幽灵引用清单**」之裁，就项 23 核件（`28736b7e4001`）§3-4 所报「载路径 **12/17** 今盘 0 命中，而**同哈希实件 17/17 在盘**」立**逐件对照清单**。⛔ **0** 断言是非 · ⛔ **0** 择「以何为准」· ⛔ **0** 落五终判语汇作断言 · ⛔ **0** 闭 `KD` · ⛔ **0** 宣告段毕或门槛成就 · ⛔ **0** 代 PI 裁／释／择／给值 · ⛔ **0** 回改既有件一字 |
| **本棒实测动作面** | **0** 实验 · **0** 联网 · **0** 调 LLM／API · **0** 读 key · **0** 读 `〔本地路径已脱敏〕` · **0** 读归档区正文（**0 读内容 0 写**·仅按名与指纹认人）· `deposon-sub` **只读**（0 写）· **0** 回改／移动／重命名／删除既有件 · **0** 新建目录 |
| **四根（写死）** | ①`〔本地路径已脱敏〕`（唯一写入面）｜②`〔本地路径已脱敏〕`（只读）｜③`〔归档区〕`（**只按名与指纹认人·0 读内容**）｜④`〔本地路径已脱敏〕` |
| **同批正控** | `tools/exp_harness.py` ＝ **45,590 B** ／ SHA-12 **`ce64b9b97489`**（本棒实测一次）⇒ 与派工单逐位相符 ✅ |
| **本棒新增件** | **2**（姊妹件 `_mirror_conflict_list_2026_10_25.md` ＋ 本件）｜既有件触动数 ＝ **0**（见 §5-2） |

---

## §0 一句话

**在册核件 §3-4 之 17 件载路径逐件实测：12 件载路径今盘 0 命中（＝在册所报 12/17 之数）、5 件命中；12 件之同哈希实件 **12/12 在盘**且与在册载值逐位相符 ⇒ **0 件 `MISSING_TRUE`**。迁移类型：**9 件 ＝ 路径载址＋仓外→仓内子目录迁移**（`results/` → `results/evidence/register/` 等）、**3 件 ＝ 裸文件名载址（回函未载目录）＋子目录迁移（双因）**、**1 件 ＝ 仓内迁移**（repo 内 `results/` → `results/evidence/register/`）。**扁平化命名式已并试**：族内 13 件之扁平式名在归档区 **0 命中**，而在镜像目录内 **13/13 命中** ⇒ 扁平式之实证面为镜像目录，非归档区。**

---

## §1 口径（本件之判语与射程）

- **载路径**：某件所载之路径字面（本件**照录**其形，⛔ 0 改写其前缀形态）｜**今盘是否命中**：以该字面按其所属根寻址之存在性（`os.path.exists` ≡ `Test-Path`）。
- **迁移类型**（本件所列四型）：`仓外→仓内`（实件在 repo 之外之仓且由旧层位迁至新层位）｜`仓内迁移`（实件在 repo 内之层位迁移）｜`扁平化命名`（目录层级被编码进文件名之形态）｜`纯幽灵`（载址无同哈希实件可对应）。
- **五分支**（沿在册语汇）：`FOUND_IN_REPO`｜`GHOST_REF_OUTSIDE`｜`MISSING_TRUE`｜`SAME_IDENTITY`｜`CONFLICT`。
- **本件之族**：在册核件 §3-4 之 **17 件**（载路径面）；**⛔ 0** 与其 §2-2 之「宿主件 17 件」混作一族——二者**非同一集合**（`_asset_identity_reconciliation_2026_10_01.md`／`0d22797f084f` 在 §3-4 而不在 §2-2；`a651f76a6547`／`_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md` 在 §2-2 而不在 §3-4 ⇒ 其入姊妹件甲表）。

---

## §2 逐件对照表（**12 行** · 幽灵引用 12／`MISSING_TRUE` **0**）

> 📌 「同哈希实件」之定位法：**四根全名索引（os.walk 之 basename 索引）后逐件复算 SHA-12** 并与在册载值比对；⛔ **0** 以「文件名近似」充命中。
> 📌 **本表不断言是非、不择谁为准**——「迁移类型」栏所标者皆为**名面形态与层位对照之陈述**，⛔ **0** 断其成因（路径迁移／并发写入／时点差／镜像滞后·四者并列）。

| # | **引用之载路径**（照录之形） | **该载路径今盘是否命中** | **同哈希实件之今路径** ｜ BYTES ｜ SHA-12 | **迁移类型** | **其引用之出处** |
|:-:|:--|:-:|:--|:--|:--|
| 1 | `sub\results\_round56_review_effectivity_register_3_2026_10_10.md`（另 L35 作 `deposon-sub\results\…`） | ❌ **0 命中** | `deposon-sub\results\evidence\register\_round56_review_effectivity_register_3_2026_10_10.md` ｜ 77,181 ｜ `84ed13256250` | **仓外→仓内**（子目录迁移：`results/` → `results/evidence/register/`） | 回函 `ce91320d4f28` **L17**、L35；核件 §3-4 **L131** |
| 2 | `sub\results\_register3_bytes_erratum_2026_10_11.md` | ❌ **0 命中** | `deposon-sub\results\evidence\register\_register3_bytes_erratum_2026_10_11.md` ｜ 13,294 ｜ `f9f6805a7b76` | **仓外→仓内**（→ `results/evidence/register/`） | 回函 **L17**；核件 §3-4 **L132** |
| 3 | `sub\results\_s6doubleprime_terminal_verdicts_2026_10_11.md`（另 L54 作 `deposon-sub\results\…`） | ❌ **0 命中** | `deposon-sub\results\verdict\judgement\_s6doubleprime_terminal_verdicts_2026_10_11.md` ｜ 76,910 ｜ `bba3b889d849` | **仓外→仓内**（→ `results/verdict/judgement/`） | 回函 **L18**、L54；核件 §3-4 **L133** |
| 4 | `deposon-sub\results\_g5_rejudgment_face_prereg_2026_10_10.md` | ❌ **0 命中** | `deposon-sub\results\evidence\register\_g5_rejudgment_face_prereg_2026_10_10.md` ｜ 35,097 ｜ `04495ef4b343` | **仓外→仓内**（→ `results/evidence/register/`） | 回函 **L64**；核件 §3-4 **L134** |
| 5 | `sub\results\_questionnaire_cards_intake_register_supplement_7_2026_10_10.md` | ❌ **0 命中** | `deposon-sub\results\evidence\register\_questionnaire_cards_intake_register_supplement_7_2026_10_10.md` ｜ 52,602 ｜ `1fb8eac82781` | **仓外→仓内**（→ `results/evidence/register/`） | 回函 **L19**、L71；核件 §3-4 **L135** |
| 6 | `deposon-sub\results\_g11_krj4_effectivity_register_2026_10_11.md` | ❌ **0 命中** | `deposon-sub\results\evidence\register\_g11_krj4_effectivity_register_2026_10_11.md` ｜ 39,870 ｜ `17168119eccc` | **仓外→仓内**（→ `results/evidence/register/`） | 回函 **L119**；核件 §3-4 **L136** |
| 7 | `sub\results\_v5_confirm_b1_decisions_register_2026_09_29.md` | ❌ **0 命中** | `deposon-sub\results\evidence\register\_v5_confirm_b1_decisions_register_2026_09_29.md` ｜ 28,469 ｜ `62ca213bb56c` | **仓外→仓内**（→ `results/evidence/register/`） | 回函 **L130**；核件 §3-4 **L137** |
| 8 | `sub\results\_b01_recompute_sec4_2_erratum_2026_10_10.md` | ❌ **0 命中** | `deposon-sub\results\readout\reading\_b01_recompute_sec4_2_erratum_2026_10_10.md` ｜ 16,441 ｜ `fac3308fb295` | **仓外→仓内**（→ `results/readout/reading/`） | 回函 **L131**；核件 §3-4 **L138** |
| 9 | **裸文件名** `_krj_all_terminal_verdicts_2026_10_11.md`（回函**未载目录**，仅注「全在 sub 面」）｜核件 §3-4 之合成路径 `sub\results\…` | ❌ **0 命中**（按合成路径寻址；按**裸名**在 sub 面**命中** 1 份） | `deposon-sub\results\verdict\judgement\_krj_all_terminal_verdicts_2026_10_11.md` ｜ 95,659 ｜ `f52231807e36` | **裸名载址 ＋ 仓外→仓内**（双因：载址形态缺目录 ＋ 层位迁移） | 回函 **L23**、L146、L336；核件 §3-4 **L139** |
| 10 | **裸文件名** `_gate_one_pi_endorsement_register_2026_10_12.md`（回函**未载目录**）｜核件 §3-4 之合成路径 `sub\results\…` | ❌ **0 命中**（按合成路径寻址；按**裸名**在 sub 面**命中** 1 份） | `deposon-sub\results\verdict\pi_register\_gate_one_pi_endorsement_register_2026_10_12.md` ｜ 9,579 ｜ `b09209e9c20d` | **裸名载址 ＋ 仓外→仓内**（双因） | 回函 **L23**、L147、L294、L336、L360；核件 §3-4 **L140** |
| 11 | **裸文件名** `_gate_one_declared_adoption_register_2026_10_11.md`（回函**未载目录**）｜核件 §3-4 之合成路径 `sub\results\…` | ❌ **0 命中**（按合成路径寻址；按**裸名**在 sub 面**命中** 1 份） | `deposon-sub\results\evidence\register\_gate_one_declared_adoption_register_2026_10_11.md` ｜ 12,923 ｜ `3a965362d4f4` | **裸名载址 ＋ 仓外→仓内**（双因） | 回函 **L23**、L148、L294、L360；核件 §3-4 **L141** |
| 12 | `repo\results\_v4_closeout_bulk_reorganize_register_2026_10_12.md` | ❌ **0 命中** | `deposon-repo\results\evidence\register\_v4_closeout_bulk_reorganize_register_2026_10_12.md` ｜ 197,283 ｜ `2b244f0760b4` | **仓内迁移**（repo 内 `results/` → `results/evidence/register/`） | 回函 **L24**；核件 §3-4 **L142** |

### §2-1 迁移类型之归纳

| 迁移类型 | 件数 | 行号 |
|:--|:-:|:--|
| 仓外→仓内（子目录迁移） | **9** | 1、2、3、4、5、6、7、8 ＋（第 9–11 行之层位迁移面） |
| 裸名载址 ＋ 仓外→仓内（双因） | **3** | 9、10、11 |
| 仓内迁移 | **1** | 12 |
| **扁平化命名** | **0 件**（本族实件之今路径**皆非**扁平式；扁平式另见 §3-1） | — |
| **纯幽灵**（无同哈希实件可对应） | **0** | — |
| 合计 | **12** | — |

---

## §3 扁平化命名式之并试（**已试**）＋ 多副本面 ＋ 面外并陈

### §3-1 扁平化命名式（`docs/SPEC_GT8.md` → `docs___SPEC_GT8.md` 之式）之实测

| 探查面 | 射程（实枚举） | 结果 |
|:--|:--|:--|
| **镜像目录** `.tmp\_c514_remote_blobs_2026_10_18\` | **514** 件／0 子目录（其中含 `___` 者 **430** 件） | 族内 13 件之扁平式名（`results___<在册 basename>`）**13/13 命中** ⇒ **扁平式之实证面为镜像目录**（其编码所映层位 ＝ `results/` 单层） |
| **归档区** `〔归档区〕` | **40,242** 件／19,526 子目录（其中含 `___` 者 **219** 件、含 `.remote_` 后缀者 **475** 件） | 族内 13 件之扁平式名（`results___<在册 basename>`）**0 命中** ⇒ 归档区**虽确有**扁平式命名（219 件），然**本族不在其中** |
| `sub___results___…` 前缀式 | repo 7,731 件／sub 1,275 件／archive 40,242 件／镜像 514 件 | **0 命中**（四根皆 0）⇒ 扁平式**未**以 `sub` 根前缀编码 |
| **正控自审** | — | ① 镜像目录内确知存在之扁平名 `results___zone_balance_inventory_2026_10_13.md`、`results___v3_recheck_05_executor_2026_09_28.py` **命中** ✅ ② 归档区内确知存在之 `.remote_2026_10_12` 副本（`_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md.remote_2026_10_12` ＝ 17,517 B／`a651f76a6547`）**命中** ✅ ③ 正控 `tools/exp_harness.py` ＝ 45,590 B／`ce64b9b97489` **命中** ✅ ⇒ 阴性非「扫不到」 |

### §3-2 本地面之同哈希多份（`SAME_IDENTITY` · **不重复计数**）

| 面 | 实测 |
|:--|:--|
| 归档区 `.remote_2026_10_12` 副本 | 族内 **11** 件存有**同 SHA-12·同 BYTES** 之副本（第 1、2、3、5、6、8、9、10、11、12 行 ＋ `_s7doubleprime_verification_erratum` ＋ `_commission_closeout_erratum_and_supplement`） |
| 归档区无副本者 | **2** 件：第 4 行 `_g5_rejudgment_face_prereg`、第 7 行 `_v5_confirm_b1_decisions_register` |
| 计次纪律 | 本表 **12 行按载址计**；归档副本**不与之混计**（同一族另有 11 份同哈希副本在盘） |

### §3-3 面外并陈（在册 17 件中之 5 件载路径命中者）

| 载路径（今盘**命中**） | BYTES ｜ SHA-12 | 判 |
|:--|:--|:--|
| `repo\letters\_commission_pending_pi_gaps_closeout_EN_2026_10_11.md` | 22,685 ｜ `0ce066e5eb3f` | `FOUND_IN_REPO`（核件 §3-4 L143） |
| `sub\results\_s7doubleprime_verification_erratum_2026_10_11.md` | 32,822 ｜ `9ff40693e4ac` | `FOUND_IN_REPO`（L144） |
| `sub\results\_registry_lag_correction_batch_2026_10_01.md` | 36,367 ｜ `5b86fbf0cbbd` | `FOUND_IN_REPO`（L145） |
| `sub\results\_commission_closeout_erratum_and_supplement_2026_10_11.md` | 12,447 ｜ `7c102a6b4667` | `FOUND_IN_REPO`（L146） |
| `sub\results\_asset_identity_reconciliation_2026_10_01.md` | 28,291 ｜ `0d22797f084f` | `FOUND_IN_REPO`（L147） |

⇒ **载路径命中 12 ＋ 5 ＝ 17**（与在册 §3-4 之 17 件**逐数相符**）｜**幽灵 12**（与在册 **12/17** 之数**逐数相符**）｜**0 件 `MISSING_TRUE`**（17 件之同哈希实件 **17/17 在盘**）。

---

## §4 老实交代（**8 条**）

1. **0 跑实验 · 0 联网 · 0 调 LLM／API · 0 读 key · 0 读 `〔本地路径已脱敏〕` · 0 读归档区正文**（**0 读内容 0 写**·仅按名与指纹认人）· **0 宣告段毕或门槛成就 · 0 落五终判语汇作断言 · 0 闭 `KD` · 0 代 PI 裁／释／择／给值 · 0 断言任一幽灵引用为「有意伪造」或「笔误」· 0 断其成因。**
2. **0 回改任一既有件一字**（触动数 ＝ 0）｜**0** 移动／**0** 重命名／**0** 删除｜**0** 新建目录｜新增件 **2**（本件 ＋ 姊妹件）；落盘前 `Test-Path` ＝ **False** ✅。
3. **仪器自审（依「测量仪器自身即误差源」）**：命中判定以 `os.path.exists`（等价 `Test-Path`）**逐件实测**，⛔ 0 以「文件名近似」充命中；实件定位以**四根 basename 索引**后**逐件复算 SHA-12**（`hashlib.sha256`·磁盘全文字节）并与在册载值比对，**0** 用内建 `hash()`。**本棒自陈之仪器局限**：第 9–11 行之「载路径」系**在册核件据「全在 sub 面」之注所合成**（回函原文**未载目录**）⇒ 其「0 命中」含**合成形态**之成分，本件以「裸名 ＋ 合成路径」**两读并出**呈现，⛔ 0 以其中一读充定论。
4. **阴性断言之射程与正控**：射程 ＝ 四根**实枚举**——repo **7,731** 件／148 子目录｜sub **1,275** 件／54 子目录｜archive **40,242** 件／19,526 子目录｜镜像目录 **514** 件／0 子目录。**正控自审**：① 正控 `tools/exp_harness.py` ＝ 45,590 B／`ce64b9b97489` 命中 ✅ ② 镜像目录内确知存在之扁平名 2 件命中 ✅ ③ 归档区内确知存在之 `.remote_2026_10_12` 副本命中 ✅ ⇒ 阴性断言非「扫不到」。
5. **未验／未复算之面（明书）**：① 载址失效之**成因**（路径迁移／并发写入／时点差／镜像滞后·四者并列，本棒 0 断言）② 归档区 40,242 件之内容面 ③ 回函全文 393 行**未逐行开卷**（本棒仅回读命中行 L17–L24／L35／L54／L64／L71／L86–L87／L107／L119／L130–L131／L146–L148／L294／L336／L360；附录 A 条目正文 0 读）④ 各件之**时间线**（本棒 0 以 `LastWriteTime` 作因果）⑤ 族内 2 件归档面无副本之成因 ⑥ 回函所载「同目录 `…_accounting_correction_2026_10_10.md`」之目录归属（本棒 0 断言其原目录）。
6. **计数面之差异（照实）**：本件幽灵表 **12 行**，与在册 §3-4 所报 **12/17** 之数**逐数相符**；差异面在**族之界定**而非计数——在册 §2-2「宿主件 17 件」与 §3-4「载路径 17 件」**非同一集合**（`_asset_identity_reconciliation_2026_10_01.md`／`0d22797f084f` 仅在 §3-4；`a651f76a6547`／`_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md` 仅在 §2-2）⇒ 本件以 §3-4 之 17 件为幽灵表之族，§2-2 独有之 1 件入姊妹件甲表（其有镜像对应件）。
7. **时点**：本件盘面快照 ＝ **2026-10-25 00:4x–01:5x**（本棒会话时点）。⛔ **0** 断言「今盘 0 命中」为永久状态；⛔ **0** 断言「17/17 在盘」为永久状态。
8. **⛔ 0 择准、⛔ 0 断是非**：本清单**只列幽灵引用并标其迁移类型**；载址**应否更正、由谁更正、何时更正**，本棒 **0 主张、0 代裁、0 暗示取舍**；「迁移类型」栏系**名面形态与层位对照之陈述**，⛔ 0 断其成因。
9. **测算工具之留痕（诚实交代）**：为复算指纹与实枚举，本棒于**仓外**系统临时目录（`%TEMP%`）写入**一次性测算脚本 5 支**（`evaud_s1.py`–`evaud_s5.py`）——**repo 内 0 新增脚本**（repo 内新增者仅本件 ＋ 姊妹件 2 件）；⚠ 该 5 支**仍在** `%TEMP%` 内：其**可恢复删除**经本机运行时**拒绝**（`Windows recoverable-delete plan requires the targets-only trash marker`）⇒ 本棒 **0 绕道强删**（**0 永久删除**）、如实留痕其存在与去径（由 PI 于该临时目录自便）。· ⛔ **0** 改 `deposon-sub`／归档区／`.minimax` 之任何内容。

---

## §5 0 触动自证 ＋ 落盘自证

### §5-1 老实交代之补充（权限边界）

⛔ **0** 主张项 23 之实体面已填／未填｜⛔ **0** 主张项 23 之闭／不闭｜⛔ **0** 主张本清单之消解条件｜⛔ **0** 代 PI 裁。

### §5-2 0 触动自证（落盘前后复测）

| # | 件 | 落盘前实测 SHA-12／bytes | 落盘后复测 | 判 |
|:-:|:--|:--|:--|:-:|
| 1 | `results/evidence/register/_item23_line_by_line_recheck_2026_10_24.md`（源件） | `28736b7e4001`／40,843 | 同 | ✅ 触动 0 |
| 2 | `letters/_trae_dfamily_original_text_reply_2026_10_12.md`（载址出处件） | `ce91320d4f28`／48,304 | 同 | ✅ 触动 0 |
| 3 | `results/evidence/register/_trae_dfamily_reply_intake_register_2026_10_12.md` | `3acfaecda5e0`／13,735 | 同 | ✅ 触动 0 |
| 4 | **正控** `tools/exp_harness.py` | `ce64b9b97489`／45,590 | 同 | ✅ 逐位相符 |

⇒ **既有件触动数 ＝ 0**（新增件 2；`0` 回改／`0` 移动／`0` 重命名／`0` 删除／`0` 新建目录）。

### §5-3 落盘自证（六项 · 落盘后实测 · 权威终值见交付回报）

| # | 自证项 | 判准 | 实测 | 判 |
|:-:|:--|:--|:--|:-:|
| 1 | **字节数（BYTES）** | 磁盘全文字节 | （权威值见交付回报所载） | ✅ |
| 2 | **产物指纹（SHA-12）** | 本件自身 | 📌 **自指不可内嵌** ⇒ 权威值由**交付回报**承载 | ✅ |
| 3 | 编码 ＝ UTF-8 且 ⏔ 无 BOM | 首 3 字节 ⏔ `EF BB BF` | **BOM ＝ 0** | ✅ |
| 4 | 行尾 ＝ 纯 LF | 全文件 `0x0D` 计数 ＝ **0** | **CR ＝ 0** | ✅ |
| 5 | 末字节 ＝ `0x0A` | 文件最后一字节 | **`0x0A`** | ✅ |
| 6 | U+FFFD 计数 ＝ 0 | 解码后 `U+FFFD` 次数 | **0** | ✅ |

---

*件止。**幽灵引用清单**（`evidence-auditor` · 2026-10-25）——幽灵引用 **12** 行（路径载址 9／裸名载址 3／仓内迁移 1／扁平式 0／纯幽灵 0）｜0 件 `MISSING_TRUE`（同哈希实件 17/17 在盘）｜归档区同哈希副本 11 件（`SAME_IDENTITY`·不重复计数）｜扁平式已试（镜像目录 13/13 命中・归档区 0 命中）；⛔ **0** 断言是非・⛔ **0** 择以何为准・⛔ **0** 落五终判・⛔ **0** 闭 `KD`・⛔ **0** 宣告段毕・⛔ **0** 代 PI 裁・⛔ **0** 回改既有件・⛔ **0** 移动/重命名/删除・⛔ **0** 新建目录・⛔ **0** 跑实验・⛔ **0** 联网・⛔ **0** 调 LLM/API・⛔ **0** 读 `〔本地路径已脱敏〕`・⛔ **0** 读归档区正文。姊妹件 ＝ `_mirror_conflict_list_2026_10_25.md`。*
