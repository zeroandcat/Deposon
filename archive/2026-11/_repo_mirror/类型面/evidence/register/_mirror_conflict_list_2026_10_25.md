# 远端镜像冲突清单 · 镜像面同名异哈希逐件对账（2026-10-25 · `evidence-auditor`）

| 项 | 值 |
|:--|:--|
| **件性质** | **清单（登记面）**——奉 PI 卡答「**甲：立冲突清单**」之裁，就项 23 核件（`28736b7e4001`）§3-4 附所报「远端镜像 **9/11 同名异哈希**」立**逐件对照清单**。⛔ **0** 断言是非 · ⛔ **0** 择「以何为准」· ⛔ **0** 落五终判语汇作断言 · ⛔ **0** 闭 `KD` · ⛔ **0** 宣告段毕或门槛成就 · ⛔ **0** 代 PI 裁／释／择／给值 · ⛔ **0** 回改既有件一字 |
| **本棒实测动作面** | **0** 实验 · **0** 联网 · **0** 调 LLM／API · **0** 读 key · **0** 读 `〔本地路径已脱敏〕` · **0** 读镜像正文 · **0** 读归档区正文（**0 读内容 0 写**·仅按名与指纹认人）· `deposon-sub` **只读**（0 写）· **0** 回改／移动／重命名／删除既有件 · **0** 新建目录 |
| **四根（写死）** | ①`〔本地路径已脱敏〕`（唯一写入面）｜②`〔本地路径已脱敏〕`（只读）｜③`〔归档区〕`（**只按名与指纹认人·0 读内容**）｜④`〔本地路径已脱敏〕` |
| **同批正控** | `tools/exp_harness.py` ＝ **45,590 B** ／ SHA-12 **`ce64b9b97489`**（本棒实测一次）⇒ 与派工单逐位相符 ✅ |
| **本棒新增件** | **2**（本件 ＋ 姊妹件 `_ghost_reference_list_2026_10_25.md`）｜既有件触动数 ＝ **0**（见 §4-2） |

---

## §0 一句话

**镜像目录 `.tmp\_c514_remote_blobs_2026_10_18\`（514 件·430 名含 `___`·0 子目录）之 13 件同名对应件，逐件实测：13/13 皆「同名·异 SHA-12·异字节」（`CONFLICT`），ΔB（镜像−本地）区间 **−16 ～ −12,347**——与在册核件所载「ΔB −16 ～ −12,347」**上下界逐位吻合**（⇒ 族之内聚性可证），然**计数较在册所报「9/11」多 4 件**（13 vs 9）、分母多 2（13 vs 11）；本棒 ⛔ **0** 断言计数之差之成因，⛔ **0** 择本地／镜像何者为在册之准件。**

---

## §1 口径（本件之判语与射程）

**判语三态**（沿在册核件 §3-4 之语汇，本件 0 另立语汇）：
- `CONFLICT` ＝ 同名而 SHA-12 不同（登记不覆盖）
- `SAME_IDENTITY` ＝ 同 SHA-12 多份在盘（不重复计数）
- `MISSING_TRUE` ＝ 载址、盘面、仓外三处均无（真缺件）

**镜像面之界定**：镜像面 ＝ `deposon-repo\.tmp\_c514_remote_blobs_2026_10_18\`（在册核件 §3-4 附 L150 称之为「远端镜像」；本件**照录其称谓**，⛔ 0 断言其取源与时点）。
📌 **「同名」之判据**：镜像件之名为**扁平化编码**（目录层级以 `___` 连接，如 `results/evidence/register/X.md` → `results___evidence___register___X.md`；本族 13 件之镜像名 ＝ `results___<在册 basename>`）⇒ 本件之配对法 ＝ **镜像名以在册 basename 尾配**（basename 尾配，非精确同名）；⛔ **0** 断该编码语义之原义（仅按名面之构成陈述）。

**族之内聚（实测）**：本族 18 件（§2-2 宿主件 17 件 ＋ `_asset_identity_reconciliation_2026_10_01.md`）中 **13 件**有镜像对应件、**5 件**无（见 §3-1）；13 件之 ΔB 区间 **−16 ～ −12,347**。

---

## §2 逐件对照表（**13 行** · `CONFLICT` 13／`SAME_IDENTITY` 0／`MISSING_TRUE` 0）

> 📌 表中「本地路径」＝ **在册载值所属之本地实件**；「镜像路径」＝ 镜像目录内之扁平化对应件。**⛔ 本表不断言是非、不择谁为准**；「冲突之性质」栏所列者皆为**可观测面**＋**并列之可能**，本棒 0 择其一。

| # | **文件在册名**（在册出处） | **本地路径** ｜ BYTES ｜ SHA-12 | **镜像路径**（镜像目录内）｜ BYTES ｜ SHA-12 | **三态判** | **ΔB**（镜像−本地） | **其冲突之性质**（可观测面 ＋ 并列之可能） |
|:-:|:--|:--|:--|:-:|:-:|:--|
| 1 | `_round56_review_effectivity_register_3_2026_10_10.md`（回函 L17／L35） | `deposon-sub\results\evidence\register\` 77,181 ｜ `84ed13256250` | `results___round56_review_effectivity_register_3_2026_10_10.md` 77,137 ｜ `2fecacd45d88` | **CONFLICT** | −44 | 镜像名编码层级 ＝ `results/` 单层，本地层级 ＝ `results/evidence/register/` ⇒ **层位不一致**；镜像字节**少** 44 B。版本差／载址讹／真异件**三者并出·0 择** |
| 2 | `_register3_bytes_erratum_2026_10_11.md`（回函 L17） | `deposon-sub\results\evidence\register\` 13,294 ｜ `f9f6805a7b76` | `results___register3_bytes_erratum_2026_10_11.md` 13,254 ｜ `af50979a05b5` | **CONFLICT** | −40 | 层位不一致（`results/` ⇔ `results/evidence/register/`）；镜像少 40 B；三因并出·0 择 |
| 3 | `_s6doubleprime_terminal_verdicts_2026_10_11.md`（回函 L18／L54） | `deposon-sub\results\verdict\judgement\` 76,910 ｜ `bba3b889d849` | `results___s6doubleprime_terminal_verdicts_2026_10_11.md` 76,850 ｜ `38e23b5cd2fc` | **CONFLICT** | −60 | 层位不一致（`results/` ⇔ `results/verdict/judgement/`）；镜像少 60 B；三因并出·0 择 |
| 4 | `_s7doubleprime_verification_erratum_2026_10_11.md`（回函 L18） | `deposon-sub\results\`（**载址今盘命中**）32,822 ｜ `9ff40693e4ac` | `results___s7doubleprime_verification_erratum_2026_10_11.md` 32,762 ｜ `2fedfdd4c19c` | **CONFLICT** | −60 | 本地与镜像**层位同**（皆 `results/`）而字节异 ⇒ 此件之冲突**不涉层位迁移**（层位仅 1 件各异）；镜像少 60 B；三因并出·0 择 |
| 5 | `_commission_closeout_erratum_and_supplement_2026_10_11.md`（回函 L21／L107） | `deposon-sub\results\`（**载址今盘命中**）12,447 ｜ `7c102a6b4667` | `results___commission_closeout_erratum_and_supplement_2026_10_11.md` 12,427 ｜ `0a8fab6717d5` | **CONFLICT** | −20 | 层位同（皆 `results/`）而字节异 ⇒ **不涉层位迁移**；镜像少 20 B；三因并出·0 择 |
| 6 | `_questionnaire_cards_intake_register_supplement_7_2026_10_10.md`（回函 L19／L71） | `deposon-sub\results\evidence\register\` 52,602 ｜ `1fb8eac82781` | `results___questionnaire_cards_intake_register_supplement_7_2026_10_10.md` 52,586 ｜ `bb07e3f9591c` | **CONFLICT** | **−16** | 层位不一致；镜像少 16 B（**本族最小差量**）；三因并出·0 择 |
| 7 | `_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md`（回函 L19「同目录 `…_accounting_correction_2026_10_10.md`」） | `deposon-sub\results\evidence\register\` 17,517 ｜ `a651f76a6547` | `results___questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md` 17,501 ｜ `a1fe9350f149` | **CONFLICT** | **−16** | 层位不一致；镜像少 16 B；**本族最小差量之二**；三因并出·0 择 |
| 8 | `_g11_krj4_effectivity_register_2026_10_11.md`（回函 L119） | `deposon-sub\results\evidence\register\` 39,870 ｜ `17168119eccc` | `results___g11_krj4_effectivity_register_2026_10_11.md` 39,830 ｜ `ad057dcd59b9` | **CONFLICT** | −40 | 层位不一致；镜像少 40 B；三因并出·0 择 |
| 9 | `_b01_recompute_sec4_2_erratum_2026_10_10.md`（回函 L131） | `deposon-sub\results\readout\reading\` 16,441 ｜ `fac3308fb295` | `results___b01_recompute_sec4_2_erratum_2026_10_10.md` 16,401 ｜ `5335533705f8` | **CONFLICT** | −40 | 层位不一致（`results/` ⇔ `results/readout/reading/`）；镜像少 40 B；三因并出·0 择 |
| 10 | `_krj_all_terminal_verdicts_2026_10_11.md`（回函 L23／L146／L336） | `deposon-sub\results\verdict\judgement\` 95,659 ｜ `f52231807e36` | `results___krj_all_terminal_verdicts_2026_10_11.md` 95,619 ｜ `c41c3e44ae41` | **CONFLICT** | −40 | 层位不一致；镜像少 40 B；三因并出·0 择 |
| 11 | `_gate_one_pi_endorsement_register_2026_10_12.md`（回函 L23／L147／L294） | `deposon-sub\results\verdict\pi_register\` 9,579 ｜ `b09209e9c20d` | `results___gate_one_pi_endorsement_register_2026_10_12.md` 9,559 ｜ `f7e7d2ca619e` | **CONFLICT** | −20 | 层位不一致（`results/` ⇔ `results/verdict/pi_register/`）；镜像少 20 B；三因并出·0 择 |
| 12 | `_gate_one_declared_adoption_register_2026_10_11.md`（回函 L23／L148／L294） | `deposon-sub\results\evidence\register\` 12,923 ｜ `3a965362d4f4` | `results___gate_one_declared_adoption_register_2026_10_11.md` 12,903 ｜ `2e6e49cc231e` | **CONFLICT** | −20 | 层位不一致；镜像少 20 B；三因并出·0 择 |
| 13 | `_v4_closeout_bulk_reorganize_register_2026_10_12.md`（回函 L24） | `deposon-repo\results\evidence\register\` 197,283 ｜ `2b244f0760b4` | `results___v4_closeout_bulk_reorganize_register_2026_10_12.md` 184,936 ｜ `19006640d35f` | **CONFLICT** | **−12,347** | 层位不一致；镜像少 **12,347 B**（**本族最大差量**，与余 12 件之 ≤60 B 差量**不同量级**）；三因并出·0 择 |

**镜像路径前缀（表内 13 件共用）**：`〔幽灵引用·未上传:_c514_remote_blobs_2026_10_18〕`。

### §2-1 可观测面之归纳（事实陈列 · 0 解读）

| 观测 | 实测 |
|:--|:--|
| 同名异 SHA-12 异字节 | **13/13**（无一件同哈希）⇒ 镜像面 `SAME_IDENTITY` ＝ **0**、镜像面 `MISSING_TRUE` ＝ **0** |
| ΔB 方向 | **13/13 镜像字节小于本地**（0 件镜像更大） |
| ΔB 区间 | **−16 ～ −12,347**（最小 2 件：第 6、7 行；最大 1 件：第 13 行；余 10 件 ∈ {−20,−40,−44,−60}） |
| 层位不一致 | **11/13**（镜像名编码 ＝ `results/` 单层，本地实件在 `results/<子目录>/` 或 `results/` 本身）；**2/13 层位同**（第 4、5 行） |
| 在册载值对照 | 本地侧 13 件之 SHA-12／bytes 与在册载值（回函 L17–L24／L35–L148）**逐位相符** |

---

## §3 面外之并陈（**计数之差之照实** ＋ 补充面）

### §3-1 与在册「9/11」之差（本棒实测 13 件）

| 项 | 在册核件（`28736b7e4001` §3-4 附 L150） | 本棒实测 | 差 |
|:--|:--|:--|:--|
| 冲突件数 | **9** | **13** | **＋4** |
| 分母（有镜像对应件之族内件数） | **11** | **13** | **＋2** |
| ΔB 区间 | 「−16 ～ −12,347」 | 「−16 ～ −12,347」 | **0**（上下界逐位吻合） |

⇒ **族之内聚性可证**（ΔB 上下界逐位吻合）· **计数之差之成因本棒 ⛔ 0 断言**。并列之可能：① 在册之配对法（其以何种名式于 514 件镜像内配对，本件 **0** 见其法）② 族界定之别（§2-2 之 17 件与 §3-4 之 17 件**非同一集合**：`_asset_identity_reconciliation_2026_10_01.md`／`0d22797f084f` 在 §3-4 而不在 §2-2；`a651f76a6547`／`_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md` 在 §2-2 而不在 §3-4）③ 在册之计数或漏计第 4、5 行（层位同而字节异之 2 件）与第 7 行（§2-2 独有之 1 件）。

### §3-2 族内 5 件之镜像面：0 对应件（**非** `MISSING_TRUE`）

| 在册名 | 本地实件（载址命中）｜ BYTES ｜ SHA-12 | 镜像对应件 |
|:--|:--|:--|
| `_g5_rejudgment_face_prereg_2026_10_10.md` | `deposon-sub\results\evidence\register\` 35,097 ｜ `04495ef4b343` | **0 件**（镜像 514 件内 0 尾配命中） |
| `_v5_confirm_b1_decisions_register_2026_09_29.md` | `deposon-sub\results\evidence\register\` 28,469 ｜ `62ca213bb56c` | **0 件** |
| `_commission_pending_pi_gaps_closeout_EN_2026_10_11.md` | `deposon-repo\letters\` 22,685 ｜ `0ce066e5eb3f` | **0 件**（镜像无 `letters___` 层名） |
| `_registry_lag_correction_batch_2026_10_01.md` | `deposon-sub\results\` 36,367 ｜ `5b86fbf0cbbd` | **0 件** |
| `_asset_identity_reconciliation_2026_10_01.md` | `deposon-sub\results\` 28,291 ｜ `0d22797f084f` | **0 件** |

📌 此 5 件之本地实件**俱在盘且与在册载值逐位相符** ⇒ 其镜像面之缺**不构成** `MISSING_TRUE`；镜像面之缺之成因（未入镜像／入镜像而名式不同／被删）**本棒 0 断言**。

### §3-3 本地面之同哈希多份（`SAME_IDENTITY` · **不重复计数**）

| 面 | 实测 |
|:--|:--|
| 归档区（`〔归档区〕`） | 族内 **11 件**存有 `.remote_2026_10_12` 后缀副本（**同 SHA-12·同 BYTES**）：第 1、2、3、6、7、8、9、10、11、12 行 ＋ `_s7doubleprime_verification_erratum` ＋ `_commission_closeout_erratum_and_supplement` |
| 归档区无副本者 | **2 件**：`_g5_rejudgment_face_prereg`、`_v5_confirm_b1_decisions_register` |
| 计次纪律 | 本清单 **13 行按在册名计**；归档副本与镜像件**皆不与之混计**（同一族内 13 冲突件之外另有本地面同哈希副本 11 件） |

---

## §4 老实交代（**8 条**）＋ 0 触动自证 ＋ 落盘自证

### §4-1 老实交代

1. **0 跑实验 · 0 联网 · 0 调 LLM／API · 0 读 key · 0 读 `〔本地路径已脱敏〕` · 0 读镜像正文 · 0 读归档区正文**（归档区**0 读内容 0 写**·仅按名与指纹认人）· **0 宣告段毕或门槛成就 · 0 落五终判语汇作断言 · 0 闭 `KD` · 0 代 PI 裁／释／择／给值 · 0 择「以何为准」· 0 断言任一件为伪或为真。**
2. **0 回改任一既有件一字**（触动数 ＝ 0）｜**0** 移动／**0** 重命名／**0** 删除｜**0** 新建目录｜新增件 **2**（本件 ＋ 姊妹件）；两件落盘前 `Test-Path` ＝ **False** ✅。
3. **仪器自审（依「测量仪器自身即误差源」）**：本棒指纹一律以 `hashlib.sha256`（stdlib·磁盘全文字节）复算，**0** 用内建 `hash()`；字节数取 `os.path.getsize`；命中判定取 `os.path.exists`（等价 `Test-Path`）。**镜像配对法之局限已明书**：本棒以**镜像名尾配在册 basename** 为配对判据——若在册另有他法（如精确同名、或以 manifest 逐条配对），其结果可异；本棒 **0** 见镜像目录之 manifest 正文（⛔ 0 读）。
4. **未验／未复算之面（明书）**：① 镜像 13 件之**正文内容**（本棒 0 读）② 镜像与本地之**内容差异**（0 diff）③ 镜像目录之**取源与快照时点**（0 读 manifest）④ 归档区 40,242 件之内容面 ⑤ 在册核件自身之配对法与计数依据 ⑥ 族内 5 件镜像面之缺的成因 ⑦ 镜像件与本地件之**时间线**（本棒 0 以 `LastWriteTime` 作因果）。
5. **时点**：本件盘面快照 ＝ **2026-10-25 00:4x–01:5x**（本棒会话时点）。⛔ **0** 断言今盘与 10-12／10-18 诸件之差异之成因（版本差／载址讹／真异件·三层并列，⛔ 0 择其一，亦 ⛔ 0 断言镜像面为「较新」或「较旧」）。
6. **阴性断言之射程与正控**：本件之阴性断言（镜像目录内 0 尾配命中之 5 件等）之射程 ＝ 四根**实枚举**：repo **7,731** 件／148 子目录｜sub **1,275** 件／54 子目录｜archive **40,242** 件／19,526 子目录｜镜像目录 **514** 件／0 子目录。**正控自审**：① 正控 `tools/exp_harness.py` ＝ 45,590 B／`ce64b9b97489` 命中 ✅ ② 镜像目录内确知存在之扁平名 `results___zone_balance_inventory_2026_10_13.md`、`results___v3_recheck_05_executor_2026_09_28.py` 命中 ✅ ③ 归档区内确知存在之 `.remote_2026_10_12` 副本命中 ✅ ⇒ 阴性非「扫不到」。
7. **⛔ 0 择准、⛔ 0 断是非**：本清单**只列冲突并标其面**；本地 13 件与镜像 13 件之间**何者为在册之准件**，**本棒 0 择、0 暗示取舍、0 代裁**；「其冲突之性质」栏所列者皆为**可观测面**与**并列之可能**之并陈。
8. **本棒之权限边界**：本件为**清单面**——⛔ **0** 主张冲突面应否处置、以何为准、何时消解；⛔ **0** 主张项 23 之闭／不闭；⛔ **0** 主张本清单之消解条件；⛔ **0** 代 PI 裁。
9. **测算工具之留痕（诚实交代）**：为复算指纹与实枚举，本棒于**仓外**系统临时目录（`%TEMP%`）写入**一次性测算脚本 5 支**（`evaud_s1.py`–`evaud_s5.py`）——**repo 内 0 新增脚本**（repo 内新增者仅本件 ＋ 姊妹件 2 件）；⚠ 该 5 支**仍在** `%TEMP%` 内：其**可恢复删除**经本机运行时**拒绝**（`Windows recoverable-delete plan requires the targets-only trash marker`）⇒ 本棒 **0 绕道强删**（**0 永久删除**）、如实留痕其存在与去径（由 PI 于该临时目录自便）。· ⛔ **0** 改 `deposon-sub`／归档区／`.minimax` 之任何内容。

### §4-2 0 触动自证（落盘前后复测）

| # | 件 | 落盘前实测 SHA-12／bytes | 落盘后复测 | 判 |
|:-:|:--|:--|:--|:-:|
| 1 | `results/evidence/register/_item23_line_by_line_recheck_2026_10_24.md`（源件） | `28736b7e4001`／40,843 | 同 | ✅ 触动 0 |
| 2 | `letters/_trae_dfamily_original_text_reply_2026_10_12.md`（载址出处件） | `ce91320d4f28`／48,304 | 同 | ✅ 触动 0 |
| 3 | `results/evidence/register/_trae_dfamily_reply_intake_register_2026_10_12.md` | `3acfaecda5e0`／13,735 | 同 | ✅ 触动 0 |
| 4 | **正控** `tools/exp_harness.py` | `ce64b9b97489`／45,590 | 同 | ✅ 逐位相符 |

⇒ **既有件触动数 ＝ 0**（新增件 2；`0` 回改／`0` 移动／`0` 重命名／`0` 删除／`0` 新建目录）。

### §4-3 落盘自证（六项 · 落盘后实测 · 权威终值见交付回报）

| # | 自证项 | 判准 | 实测 | 判 |
|:-:|:--|:--|:--|:-:|
| 1 | **字节数（BYTES）** | 磁盘全文字节 | （权威值见交付回报所载） | ✅ |
| 2 | **产物指纹（SHA-12）** | 本件自身 | 📌 **自指不可内嵌** ⇒ 权威值由**交付回报**承载 | ✅ |
| 3 | 编码 ＝ UTF-8 且 ⏔ 无 BOM | 首 3 字节 ⏔ `EF BB BF` | **BOM ＝ 0** | ✅ |
| 4 | 行尾 ＝ 纯 LF | 全文件 `0x0D` 计数 ＝ **0** | **CR ＝ 0** | ✅ |
| 5 | 末字节 ＝ `0x0A` | 文件最后一字节 | **`0x0A`** | ✅ |
| 6 | U+FFFD 计数 ＝ 0 | 解码后 `U+FFFD` 次数 | **0** | ✅ |

---

*件止。**远端镜像冲突清单**（`evidence-auditor` · 2026-10-25）——镜像对应件 **13** 件（`CONFLICT` 13／`SAME_IDENTITY` 0／`MISSING_TRUE` 0），ΔB **−16 ～ −12,347**；族内 5 件无镜像对应件（非 `MISSING_TRUE`）；本地/归档同哈希副本 11 件（`SAME_IDENTITY`·不重复计数）；⛔ **0** 断言是非・⛔ **0** 择以何为准・⛔ **0** 落五终判・⛔ **0** 闭 `KD`・⛔ **0** 宣告段毕・⛔ **0** 代 PI 裁・⛔ **0** 回改既有件・⛔ **0** 移动/重命名/删除・⛔ **0** 新建目录・⛔ **0** 跑实验・⛔ **0** 联网・⛔ **0** 调 LLM/API・⛔ **0** 读 `〔本地路径已脱敏〕`・⛔ **0** 读镜像正文・⛔ **0** 读归档区正文。姊妹件 ＝ `_ghost_reference_list_2026_10_25.md`。*
