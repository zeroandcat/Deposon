# 旧版信件归档登记册 · 2026-10-01（4 族 10 件）

- **棒别**：旧版信件归档执行 ｜ **出证方**：**worker**（本棒实际执行者）。⛔ 不冒充 PI / doc-writer / verdict-keeper / evidence-auditor / protocol-keeper / verifier / Trae code / KIMI / GLM / coze 等任一他棒或受托方。
- **件名**：`results/_letters_archive_register_2026_10_01.md`（**新名合规**——`_主题_日期`，无阶段/版本前缀，沿 PI 09-29「阶段名只能由 PI 定义」纪律）
- **版式**：UTF-8 无 BOM · LF
- **纪律**：0 编造｜0 代裁｜0 回改既有件｜0 删除（⛔ 0 永久删除）｜0 覆写｜0 触非候选件｜归档区仅**新增本批目录**（0 触既有面）｜R4（0 读 key／0 读 `.env`）｜0 网络｜0 对外
- **落盘前撞名实测**：`results\_letters_archive_register_2026_10_01.md` **exists=False**；`results` 近名 glob `*letters_archive*` **0 命中** ⇒ **0 覆写任何既有件**
- **产出**：**1 件**（本登记件）＋ **移动动作 10 件**；0 派生 JSON／0 脚本留存
- **本棒时点**：2026-10-01 21:31 起（归档动作）；本件落盘于其后

---

## §0 授权、判据与范围边界

### §0.1 授权源（逐字照录，不代裁）

> PI 2026-10-01 晚：「一些旧版信件可以归档了」

### §0.2 判据（本次采用，以盘上实读为准）

**「旧版信件」＝ 同一信件族（同名 stem）内已有更新版本留于原地之被取代版本。**

三项要件缺一即**不归档**：
1. **同族**：被取代件与继任件属同一信件族（文件名 stem 同源）；
2. **新版在位**：继任版本**此刻仍在原地**（`letters/`），经实读确认存在且非空；
3. **被取代关系可核**：继任件头部**自述**沿自被取代件的指纹，与本棒实测逐位相符（见 §1.2 印证栏）。

**边界（越界即停）**：**跨 stem 之被取代线**（版本号落在文件名中段、改名立新件、线程更替等导致 stem 不同源者）⇒ **列 §7 待裁清单，不擅移**；存疑 ⇒ **0 动**。

### §0.3 上传面备忘（重要·不因归档而变）

- `letters/` 面**本就 0 上传**（carve，🚫 禁传）；本次归档**不改变上传面**，**KIMI 侧无需任何动作**（不需改委托、不需重发、不需追加说明）。
- 归档区 `〔本地归档区〕` ＝ **🚫 禁传面**；本批 10 件**仅落该面**，未进任何可传目录。
- 现行留位件**全部保持 🚫 0 发送／0 推送／0 转递／0 外联**状态不变（⛔ 0 触动其状态行）。

---

## §1 族别与在位核实（4 族 · 逐族实读）

### §1.1 族别清单

| 族 | 归档件（被取代） | 现行留位件（新版·留位） | 留位件落盘时点 |
|---|---|---|---|
| **A. GLM 双主线论文终稿委托链** | v0.1、v0.2、v0.3、v0.4（4 件） | `letters/_commission_glm_dualtrack_paper_v0.5_2026_10_01.md`（**定稿·待 PI 审发**） | 2026-10-01 11:48:26 |
| **B. 双主线实验成果线索册链** | v0.1（无版本号件）、v0.2、v0.3、v0.4（4 件） | `letters/_dualtrack_paper_clue_book_v0.5_2026_10_01.md`（**定稿·待 PI 审阅**） | 2026-10-01 11:50:06 |
| **C. KIMI 今日增量上传委托链** | v0.1（无版本号件，1 件） | `letters/_commission_kimi_upload_2026_10_01_v0.2.md`（**定稿·待 PI 审发**；圈选 Q1–Q4 已裁定） | 2026-10-01 20:38:35 |
| **D. GLM 双主线委托信·补件链** | 首版（落盘时文件名无版本号，其位次为 v0.1，1 件） | `letters/_commission_glm_dualtrack_paper_addendum_v0.2_2026_10_01.md`（**可达性对齐版·草案·待 PI 审发**） | 2026-10-01 21:19:36 |

**合计：4 族 10 件**（族内每一条的「新版在位」要件**逐一实读确认**，无一件依赖推定）。

### §1.2 被取代关系双向印证（继任件头部自述指纹 vs 本棒实测）

| 被取代件（实测 sha[:12]） | 继任件头部自述沿自该指纹 | 印证 |
|---|---|---|
| `725c93a9cc09`（v0.1） | v0.2 头部「沿 v0.1 `725c93a9cc09`」 | ✅ 相符 |
| `a17275086734`（v0.2） | v0.3 头部「沿 v0.2 `a17275086734`」 | ✅ 相符 |
| `07d7e880235f`（v0.3） | v0.4 头部「沿 v0.3 `07d7e880235f`」 | ✅ 相符 |
| `5ae6bf23a1b2`（v0.4） | v0.5 头部「沿 v0.4 `5ae6bf23a1b2`」 | ✅ 相符 |
| `01a0acbb716b`（线索册 v0.1） | v0.2 头部「沿 v0.1 `01a0acbb716b`」 | ✅ 相符 |
| `998221ed5947`（线索册 v0.2） | v0.3 头部「沿 v0.2 `998221ed5947`」 | ✅ 相符 |
| `9de6f392912a`（线索册 v0.3） | v0.4 头部「沿 v0.3 `9de6f392912a`」 | ✅ 相符 |
| `c7c418081026`（线索册 v0.4） | v0.5 头部「沿 v0.4 `c7c418081026`」 | ✅ 相符 |
| `4a40d54af9d2`（KIMI v0.1） | KIMI v0.2 头部「前版 `4A40D54AF9D2`／29,880 B」 | ✅ 相符（含字节） |
| `689f587f219c`（补件首版） | 补件 v0.2 头部「首版补件 `689f587f219c` · 35,892 B · 落盘 20:04:25」 | ✅ 相符（含字节与时点） |

**10/10 相符** ⇒ 判据要件 3 全部满足，非单方自述。

### §1.3 被取代关系中继任件的**明示处置口径**（原文照录要点）

- A 族 v0.2–v0.5 头部一致载明：「⛔ v0.4／v0.3／v0.2／v0.1 **0 覆写、0 回改、留档为备用**」。
- B 族 v0.5 头部载明：「⛔ v0.4／v0.3／v0.2／v0.1（v0.1 即无版本号件 `_dualtrack_paper_clue_book_2026_10_01.md`）**0 覆写、0 回改、留档为备用**」。
- C 族 v0.2 头部载明：前版「**0 覆写、原样在位** —— 依本文书线「新版本不覆盖旧件」体例，另立 v0.2 新名」。
- D 族 v0.2 头部载明：首版「**0 覆写、0 回改、0 改名**，留档为备用」；「⚠️ 首版落盘时文件名未带版本号（本版起其位次为 v0.1），**本版不追改其文件名**」。

**本棒与上述口径的一致性说明（如实登记，不代裁）**：
- **「0 覆写」「0 回改」「0 改名」「留档为备用」—— 本棒全部满足**：本批为**移动**（同卷改址）而非覆写；文件名**一字未改**（含 D 族首版的无版本号文件名）；**0 永久删除**，件仍完整在册、随时可拉回（§8.3）⇒ **「留档为备用」承诺不破**。
- ⚠️ **C 族「原样在位」之字面与本棒终态的差异（如实登记，不回改该件）**：C 族 v0.2 头部称前版「原样在位」，该字面系其**落盘时点**（2026-10-01 20:38）状态。本棒依 PI 2026-10-01 晚归档指令将其移至归档区，故**「留位」状态已由本登记件（§8 索引）接续承担**。依 **0 回改**纪律，⛔ **未修改 C 族 v0.2 之任何字面**；引用其前版时应以本件 §8 映射解析路径。**哈希未变**，既有哈希引用仍可原样核验。

---

## §2 移前基线（逐件实测 · 10/10）

**实测时点**：2026-10-01 21:31–21:35（移动动作之前）。
**版式实测**：10 件**全部** UTF-8 **无 BOM**、**LF 换行**（CRLF 计数 0/10）——移动为同卷改名，**未触发任何 CRLF 转换**（避坑：落盘转换致自报哈希≠盘上值之族）。

| # | 族 | 文件名（`letters/` 下） | sha256[:12] | 字节 | LF 数 | BOM | 落盘时点 |
|---|---|---|---|---|---|---|---|
| 1 | A | `_commission_glm_dualtrack_paper_v0.1_2026_10_01.md` | `725c93a9cc09` | 19,884 | 194 | 无 | 10-01 00:25:22 |
| 2 | A | `_commission_glm_dualtrack_paper_v0.2_2026_10_01.md` | `a17275086734` | 21,014 | 194 | 无 | 10-01 00:39:32 |
| 3 | A | `_commission_glm_dualtrack_paper_v0.3_2026_10_01.md` | `07d7e880235f` | 23,534 | 195 | 无 | 10-01 09:45:22 |
| 4 | A | `_commission_glm_dualtrack_paper_v0.4_2026_10_01.md` | `5ae6bf23a1b2` | 29,784 | 196 | 无 | 10-01 10:08:26 |
| 5 | B | `_dualtrack_paper_clue_book_2026_10_01.md`（＝v0.1） | `01a0acbb716b` | 62,946 | 557 | 无 | 10-01 00:25:43 |
| 6 | B | `_dualtrack_paper_clue_book_v0.2_2026_10_01.md` | `998221ed5947` | 63,656 | 558 | 无 | 10-01 00:34:38 |
| 7 | B | `_dualtrack_paper_clue_book_v0.3_2026_10_01.md` | `9de6f392912a` | 68,780 | 560 | 无 | 10-01 09:46:16 |
| 8 | B | `_dualtrack_paper_clue_book_v0.4_2026_10_01.md` | `c7c418081026` | 99,576 | 681 | 无 | 10-01 10:08:26 |
| 9 | C | `_commission_kimi_upload_2026_10_01.md`（＝v0.1） | `4a40d54af9d2` | 29,880 | 303 | 无 | 10-01 20:09:12 |
| 10 | D | `_commission_glm_dualtrack_paper_addendum_2026_10_01.md`（＝v0.1） | `689f587f219c` | 35,892 | 327 | 无 | 10-01 20:04:25 |

**合计：10 件 ／ 454,946 B**。

**sha256 全串（备核）**

```
725c93a9cc098c5656c888720bc967f0b34b58e8588453a72406ba599a5a19af  19884  _commission_glm_dualtrack_paper_v0.1_2026_10_01.md
a17275086734142c2def11163c901aad9a423eb79317fc7bf534402e768e7ad4  21014  _commission_glm_dualtrack_paper_v0.2_2026_10_01.md
07d7e880235f907edc1626e5a6f2a3e5b4754ea9c8069acb567c00c1a2fdccf6  23534  _commission_glm_dualtrack_paper_v0.3_2026_10_01.md
5ae6bf23a1b2d1162cb92ffadb575e84ed05de3ba2d7e661f527121f836e97a3  29784  _commission_glm_dualtrack_paper_v0.4_2026_10_01.md
01a0acbb716befc3846f013f480fb57283c53ea7ff8d6fe9fbb13f0881742a68  62946  _dualtrack_paper_clue_book_2026_10_01.md
998221ed5947a256815c64ae3e8bac0e549ab63f232f13c8d3b6905c6a87f00e  63656  _dualtrack_paper_clue_book_v0.2_2026_10_01.md
9de6f392912a0349f898518c870ef5055fddfa2415b25d5eff0ae75d03214d28  68780  _dualtrack_paper_clue_book_v0.3_2026_10_01.md
c7c418081026a5987168d23849a211db79d86e4bf7e5224a421fe1f9b7063cec  99576  _dualtrack_paper_clue_book_v0.4_2026_10_01.md
4a40d54af9d2c4276406602bf4452d0718210bfec4232dda63f3cb90a12dd7a1  29880  _commission_kimi_upload_2026_10_01.md
689f587f219c5af28ac537a86f69a6675652d7058dd1968114c920dd65008407  35892  _commission_glm_dualtrack_paper_addendum_2026_10_01.md
```

---

## §3 落位决策（归档区纪律）

| 项 | 值 |
|---|---|
| 目标根 | `〔本地归档区〕/letters_archive_2026_10_01/` |
| 命名依据 | 派工建议名；沿归档区既有惯例（`_archive_2026_09_20`／`_remote_version_freeze_2026_09_26` 之「`_主题_日期`」体例）＋ PI 09-29 命名裁定（去阶段/版本前缀） |
| 落位方式 | **同卷改址移动**（工作区与归档区同在 `D:` 卷 ⇒ 原子改名，**0 数据重写**、0 副本暂存、0 覆盖风险） |
| 目录内布局 | **扁平 10 件 · 文件名一字不改**（⇒ 同族件之间的相互引用仍可解析；仅绝对路径前缀 `letters/` → `letters_archive_2026_10_01/`） |
| **撞名实测（落前）** | 目标目录 `letters_archive_2026_10_01` **exists=False**；区根近名 `letters`／`letters_archive`／`letters_2026_10_01`／`archive_letters_2026_10_01` **全 exists=False**；区根近名 glob `*letter*` **0 命中**；`results` 子目录近名 glob `*letter*` **0 命中** ⇒ **0 覆写** |
| **撞名实测（逐件落位）** | 每件移动前先 `Test-Path` 目标同名件，若存在即中止 ⇒ **10/10 均无同名冲突** |
| 归档区既有面 | **0 触动**：区根目录数 28 → 29，**净增恰为 1**（本批目录）；既有 `results`／`_movedout_scratch_*`／`ARCHIVE_INDEX.md` 等**一律未读写**（⛔ 未向 `ARCHIVE_INDEX.md` 追加——本棒纪律为「归档区仅新增本批目录」） |

---

## §4 移后逐件复核（源已无 ＋ dest 指纹/字节一致）

**逐件比对移前实测值与移后落位值**（sha256 全串比对，非仅前 12 位）：

| # | 文件名 | 源已无 | dest 在位 | sha256 一致 | 字节一致 | 判定 |
|---|---|---|---|---|---|---|
| 1 | `_commission_glm_dualtrack_paper_v0.1_2026_10_01.md` | ✅ | ✅ | ✅ | ✅ 19,884 | **OK** |
| 2 | `_commission_glm_dualtrack_paper_v0.2_2026_10_01.md` | ✅ | ✅ | ✅ | ✅ 21,014 | **OK** |
| 3 | `_commission_glm_dualtrack_paper_v0.3_2026_10_01.md` | ✅ | ✅ | ✅ | ✅ 23,534 | **OK** |
| 4 | `_commission_glm_dualtrack_paper_v0.4_2026_10_01.md` | ✅ | ✅ | ✅ | ✅ 29,784 | **OK** |
| 5 | `_dualtrack_paper_clue_book_2026_10_01.md` | ✅ | ✅ | ✅ | ✅ 62,946 | **OK** |
| 6 | `_dualtrack_paper_clue_book_v0.2_2026_10_01.md` | ✅ | ✅ | ✅ | ✅ 63,656 | **OK** |
| 7 | `_dualtrack_paper_clue_book_v0.3_2026_10_01.md` | ✅ | ✅ | ✅ | ✅ 68,780 | **OK** |
| 8 | `_dualtrack_paper_clue_book_v0.4_2026_10_01.md` | ✅ | ✅ | ✅ | ✅ 99,576 | **OK** |
| 9 | `_commission_kimi_upload_2026_10_01.md` | ✅ | ✅ | ✅ | ✅ 29,880 | **OK** |
| 10 | `_commission_glm_dualtrack_paper_addendum_2026_10_01.md` | ✅ | ✅ | ✅ | ✅ 35,892 | **OK** |

**复核结论：10/10 OK，0 FAIL。** 落位目录实测 **10 件 ／ 454,946 B**，与移前基线**逐件双项（哈希＋字节）全等**。

---

## §5 0 回改与 0 触自证

### §5.1 `letters/` 面基线比对（移动前后全量逐件哈希）

| 项 | 移动前 | 移动后 | 判定 |
|---|---|---|---|
| 件数 | **94** | **84** | −10（恰为本批 10 件） |
| 字节 | **2,627,071** | **2,172,125** | −454,946（恰为本批 10 件之和） |
| 字节守恒 | 2,172,125 ＋ 454,946 ＝ **2,627,071** | | ✅ **守恒相符** |
| 移除件清单 | — | **恰为 §2 表 10 件**，0 多、0 少 | ✅ |
| 留位件**指纹变异** | 84 件逐件 sha256[:12]＋字节复算 | **0 件变异** | ✅ **0 回改** |
| 新增/异源文件 | — | **0 件** | ✅ **0 触非候选件** |

### §5.2 归档区面

| 项 | 值 | 判定 |
|---|---|---|
| 区根目录数 | 28 → **29**（净增 1 ＝ 本批目录） | ✅ 0 触既有面 |
| 既有 `ARCHIVE_INDEX.md` | **未读写、未追加** | ✅ 0 触 |
| 既有 `results`／`_movedout_scratch_2026_09_2*`／`_movedout_scratch_2026_10_01` 等 | **一律 0 读写** | ✅ 0 触 |
| 永久删除 | **0 件** | ✅ |

### §5.3 现行留位件 0 触动

4 件现行件（委托信 v0.5／线索册 v0.5／KIMI v0.2／补件 v0.2）**未移动、未改名、未编辑一字**，仍为 `letters/` 下 🚫 0 发送／0 推送／0 转递／0 外联状态。

---

## §6 跨引用影响与解析依据（⚠️ 本批唯一需后续留意的面）

移动会使**留位件与实录件中指向被归档件的字面路径**失去在位落点。依 **0 回改**纪律，本棒⛔ **未修改任何留位件或实录件**，改以本节＋§8 索引作为引用解析依据。**哈希一律未变**，故既有**哈希**引用仍可原样核验，仅**路径前缀**变更。

### §6.1 留位现行件中的路径引用（4 件 · 共 17 处）

| 留位件 | 引用到已归档件 | 处数 |
|---|---|---|
| `letters/_commission_kimi_upload_2026_10_01_v0.2.md`（C 族现行） | 委托信 v0.1／v0.2／v0.3／v0.4；线索册 v0.1／v0.2／v0.3／v0.4；**KIMI v0.1（其前版）**；补件首版 | **11** |
| `letters/_commission_glm_dualtrack_paper_addendum_v0.2_2026_10_01.md`（D 族现行） | **补件首版（其前版）** ×3（头部 1＋正文 2） | **3** |
| `letters/_dualtrack_paper_clue_book_v0.5_2026_10_01.md`（B 族现行） | 线索册 v0.1（无版本号件）· v0.4 | **2** |
| `letters/_commission_glm_dualtrack_paper_v0.5_2026_10_01.md`（A 族现行） | 线索册 v0.4 | **1** |
| **合计** | | **17** |

### §6.2 `results/` 实录件中的路径引用（7 件 · 共 41 处）

`_sub_artifact_ledger_history_r5_2026_10_01.md`（10）｜`_forgotten_items_quick_sweep_register_2026_10_01.md`（9）｜`_registry_lag_correction_batch_2026_10_01.md`（8）｜`_c4_reply_intake_acceptance_register_2026_10_01.md`（5）｜`_glm_five_items_suggestion_table_2026_10_01.md`（5）｜`_external_letters_two_generation_values_note_2026_10_01.md`（2）｜`_mini_round_4_decisions_register_2026_10_01.md`（2）。

**处置**：实录件系**落册/登记/实录**性质，依「证据/实录件 0 回改・历史留痕」纪律 **一律未改**；其中「旧版在盘于 `letters/`」之表述系**其登记时点**状态，依「登记值可能落后于盘上终态」纪律，**以本件为终态登记**。

### §6.3 同族件互引（无需处理，附记）

本批 10 件之间的相互引用**全部保持可解析**——10 件同落一扁平目录、文件名一字未改（如补件首版正文引用留位件 `_commission_glm_dualtrack_paper_v0.5_…`／`_dualtrack_paper_clue_book_v0.5_…`，该二件**留位**于 `letters/`，路径未变）。

---

## §7 待裁清单（跨 stem／更早线程 · **0 移 0 触**）

以下各线**均存「跨 stem」或「线未闭合／无新版在位」情形**，依 §0.2 边界**一律不擅移**，登记待裁。**本棒 0 动作**（未移动、未改名、未编辑、未删除）。

### §7.1 PI 明确点名的三类

| 线 | 待裁件（sha[:12]／字节） | 族内最新件（留位） | 待裁理由 |
|---|---|---|---|
| **09-24 期旧论文委托线（GLM）** | `53a425fe1bd2`／10,515；`f3b3e13a0f1b`／13,749；`614df9879696`／20,989 | `_v4_commission_paper_final_glm_2026_09_24_v4.md`（`d5337702cec9`／31,531） | **PI 点名「09-24 期旧论文委托线」** ⇒ 待裁 |
| **09-24 期旧〔IM〕汇报线（coze）** | `15f8227308bc`／7,197；`389c51e70d19`／10,599；`e5b63d181b15`／13,898 | `_v4_commission_〔IM〕_report_coze_2026_09_24_v4.md`（`802c705e1469`／21,433） | 与上条同期同线，**PI 同批点名的期线** ⇒ 待裁 |
| **理论推导旧线（codex EN）** | `_commission_codex_theory_derivation_EN_2026_09_30.md`（`af50969bebe2`／66,754） | `_commission_codex_theory_derivation_EN_v0.2_2026_09_30.md`（`8b15f0957e0f`／82,016） | **跨 stem**：新版版本号落在文件名**中段**（`_EN_v0.2_`），stem 不同源 ⇒ 待裁 |
| **更早线程（09-20 V4 蒸馏/主题/邀请线）** | 主题线 trae_work：`_v4_theme_reply_trae_work_2026_09_20.md`（`eba83c88b629`／11,458）、`…_v1.1.md`（`be850d129f35`／13,404）｜主题线 mavis：`_v4_theme_reply_mavis_2026_09_20.md`（`5d932d7085cd`／37,980）、`…_v1.1.md`（`5c61f61f1f7e`／38,085）｜邀请线：`_v4_experiment_invitation_2026_09_20.md`（`20f8242de6ca`／32,164） | 主题线 trae_work v1.2（`6bee6ec434bd`／28,395）｜主题线 mavis v1.2（`f1d73c82511d`／38,087）｜邀请线 v0.2（`72fc2e7fb098`／43,024） | **PI 点名「更早线程」**；且多件 mtime 同为 09-30 16:14:47（批量搬移痕），时序存疑 ⇒ 待裁 |

### §7.2 存疑型（线未闭合 · 待裁）

| 线 | 待裁件 | 族内最新件（留位） | 待裁理由 |
|---|---|---|---|
| 09-24 期上传执行线 | `_v4_commission_upload_executor_2026_09_24.md`（`adfa7dd03f76`／13,012）、`…_v2.md`（`ff2154ce182d`／16,894） | `_v4_commission_upload_executor_2026_09_24_v3.md`（`c20d4f58f5c8`／25,091） | **族内最新件系 v3 且该线带 2 件回函**（`_…_reply_v3_2026_09_24.md`、`_…_reply_v3_exec_2026_09_26.md`）⇒ **线未闭合**；且 v1/v2 之上尚有同线通道授权件交互 ⇒ **存疑 ⇒ 0 移** |

### §7.3 0 适用项（登记备查 · 非候选 · 0 动作）

| 件 | sha[:12]／字节 | 0 适用理由 |
|---|---|---|
| `_commission_glm_theory_derivation_2026_09_30.md` | `344f5b9e0b08`／32,472 | 族内**唯一**件，**无新版在位**（旁有回函 `_c4_theory_scan_reply_claude_code_2026_09_30.md`，非版本） |
| `_v4_acceptance_trae_work_v1.0_2026_09_20.md` | `3caf4e653a68`／7,176 | 族内**唯一**件（版本号在名中，无 v2/v1.1 在位） |
| `_v5_rj5_external_rederive_request_2026_09_28.md` | `cfd58ae66463`／31,381 | 与下一件为**中／英双语变体**，非版本先后；⛔ `_v5_` 系**存量历史前缀**（PI 09-29 命名裁：0 改名 0 追改） |
| `_v5_rj5_external_rederive_request_EN_2026_09_28.md` | `498215a9ec7d`／51,013 | 同上 |

**待裁合计：14 件**（§7.1 十二件 ＋ §7.2 两件）；另 §7.3 **4 件** 0 适用登记。**全部 0 动作。**

---

## §8 归档索引（source → dest · 可拉回）

### §8.1 索引条目（10 件 · 逐件映射）

| # | source（移动前） | dest（落位后） | sha256[:12] | 字节 |
|---|---|---|---|---|
| 1 | `deposon-repo\letters\_commission_glm_dualtrack_paper_v0.1_2026_10_01.md` | `_non_upload_local_archive\letters_archive_2026_10_01\_commission_glm_dualtrack_paper_v0.1_2026_10_01.md` | `725c93a9cc09` | 19,884 |
| 2 | `deposon-repo\letters\_commission_glm_dualtrack_paper_v0.2_2026_10_01.md` | `…\letters_archive_2026_10_01\_commission_glm_dualtrack_paper_v0.2_2026_10_01.md` | `a17275086734` | 21,014 |
| 3 | `deposon-repo\letters\_commission_glm_dualtrack_paper_v0.3_2026_10_01.md` | `…\letters_archive_2026_10_01\_commission_glm_dualtrack_paper_v0.3_2026_10_01.md` | `07d7e880235f` | 23,534 |
| 4 | `deposon-repo\letters\_commission_glm_dualtrack_paper_v0.4_2026_10_01.md` | `…\letters_archive_2026_10_01\_commission_glm_dualtrack_paper_v0.4_2026_10_01.md` | `5ae6bf23a1b2` | 29,784 |
| 5 | `deposon-repo\letters\_dualtrack_paper_clue_book_2026_10_01.md` | `…\letters_archive_2026_10_01\_dualtrack_paper_clue_book_2026_10_01.md` | `01a0acbb716b` | 62,946 |
| 6 | `deposon-repo\letters\_dualtrack_paper_clue_book_v0.2_2026_10_01.md` | `…\letters_archive_2026_10_01\_dualtrack_paper_clue_book_v0.2_2026_10_01.md` | `998221ed5947` | 63,656 |
| 7 | `deposon-repo\letters\_dualtrack_paper_clue_book_v0.3_2026_10_01.md` | `…\letters_archive_2026_10_01\_dualtrack_paper_clue_book_v0.3_2026_10_01.md` | `9de6f392912a` | 68,780 |
| 8 | `deposon-repo\letters\_dualtrack_paper_clue_book_v0.4_2026_10_01.md` | `…\letters_archive_2026_10_01\_dualtrack_paper_clue_book_v0.4_2026_10_01.md` | `c7c418081026` | 99,576 |
| 9 | `deposon-repo\letters\_commission_kimi_upload_2026_10_01.md` | `…\letters_archive_2026_10_01\_commission_kimi_upload_2026_10_01.md` | `4a40d54af9d2` | 29,880 |
| 10 | `deposon-repo\letters\_commission_glm_dualtrack_paper_addendum_2026_10_01.md` | `…\letters_archive_2026_10_01\_commission_glm_dualtrack_paper_addendum_2026_10_01.md` | `689f587f219c` | 35,892 |

**落位根（全 10 件 dest 前缀）**：`〔本地归档区〕/letters_archive_2026_10_01/`

### §8.2 批量校验凭据（批次指纹）

| 项 | 值 |
|---|---|
| 件数 | **10** |
| 字节 | **454,946** |
| 批次规范化串 | 10 行 `文件名\|sha256(小写)\|字节`，以 **LF** 连接，计 **1,185 B** |
| **批次 digest（sha256）** | `415eab84ec609a8076558325916e0eda475a1f4409c596b041cc9e9cd0e572a6` |
| **批次 digest[:12]** | `415eab84ec60` |

> 用途：日后核验本批完整性，一算即知是否 10 件齐全、0 篡改（复算方式见 §8.3 末条）。

### §8.3 拉回路径（可拉回 · 一键复原式例）

**全批拉回（复原至原位）**

```powershell
$src = '〔本地归档区〕/letters_archive_2026_10_01'
$dst = '_september_workspace/letters'
Get-ChildItem -LiteralPath $src -File | ForEach-Object {
  $t = Join-Path $dst $_.Name
  if (Test-Path -LiteralPath $t) { Write-Output ("SKIP(同名已存在,0覆写): " + $_.Name) }
  else { Move-Item -LiteralPath $_.FullName -Destination $t }
}
```

**单件拉回**（示例：拉回 C 族 v0.1）

```powershell
Move-Item -LiteralPath '〔本地归档区〕/letters_archive_2026_10_01/_commission_kimi_upload_2026_10_01.md' `
          -Destination '_september_workspace/letters/_commission_kimi_upload_2026_10_01.md'
```

**拉回后校验**（逐件复算，应与 §2 基线全等）

```powershell
Get-ChildItem -LiteralPath '_september_workspace/letters' -File |
  Where-Object { $_.Name -match '_commission_glm_dualtrack_paper_v0\.[1-4]|_dualtrack_paper_clue_book(_v0\.[2-4])?|_commission_kimi_upload_2026_10_01\.md|_commission_glm_dualtrack_paper_addendum_2026_10_01\.md' } |
  ForEach-Object { "{0}  {1}  {2}" -f (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash.ToLower(), $_.Length, $_.Name }
```

**批次 digest 复算**（全批完整性一算）

```powershell
$lines = Get-ChildItem -LiteralPath '〔本地归档区〕/letters_archive_2026_10_01' -File | Sort-Object Name |
  ForEach-Object { $_.Name + '|' + (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash.ToLower() + '|' + $_.Length }
$canon = ($lines -join "`n")
$sha = [System.Security.Cryptography.SHA256]::Create()
(($sha.ComputeHash([System.Text.Encoding]::UTF8.GetBytes($canon)) | ForEach-Object { $_.ToString('x2') }) -join '')
# 期望：415eab84ec609a8076558325916e0eda475a1f4409c596b041cc9e9cd0e572a6
```

⚠️ 拉回后**须复查** §6 所列 17 处留位件引用路径是否需同步——**是否同步回改由 PI 裁**，本棒⛔ 0 代裁、0 自行回改。

---

## §9 遗留 · 风险 · 待裁移交

| 项 | 状态 | 归属 |
|---|---|---|
| §7 待裁 14 件（＋4 件 0 适用登记） | **0 动**，待 PI 裁 | 【人机协同】（我备清单，PI 选认） |
| §6.1 留位现行件 17 处路径引用 | **0 回改**；以本件索引为解析依据 | 【人机协同】（是否回改由 PI 裁） |
| §6.2 `results/` 实录件 41 处路径引用 | **0 回改**（历史留痕）；以本件为终态登记 | 【我】（已如实登记，无需动作） |
| C 族 v0.2 头部「前版原样在位」字面 | **0 回改**；差异已如实登记于 §1.3 | 【人机协同】 |
| 上传面 | **无变化**；`letters/` 本就 0 上传（carve） | 【我】已核，KIMI 侧 0 动作 |
| 归档区 `ARCHIVE_INDEX.md` | **未追加**（本棒纪律：归档区仅新增本批目录） | 【人机协同】（如需并入区级总索引，待裁） |

**本棒 0 网络、0 对外、0 外联、0 发送；R4 守规（0 读 key／0 读 `.env`）；0 永久删除；0 覆写；0 回改既有件。**

---

## §10 交付回执

- **产出**：**1 件登记件** ＋ **移动动作 10 件**
- **件名**：`results/_letters_archive_register_2026_10_01.md`
- **版式**：UTF-8 **无 BOM** · **LF**（落盘后实测，见交付回执随附实测值）
- **归档**：**10 件**（4 族 10 件）／**454,946 B**／批次 digest `415eab84ec609a8076558325916e0eda475a1f4409c596b041cc9e9cd0e572a6`
- **待裁**：**14 件**（＋4 件 0 适用登记）
- **0 回改复核**：`letters/` 留位 84 件**指纹变异 0**；实录件 0 改动；归档区既有面 0 触动
- **署名**：**worker**（本棒实际执行者）

**指纹不自写入本件**（沿既有文书体例：落盘后实测随交付回执回报）。
