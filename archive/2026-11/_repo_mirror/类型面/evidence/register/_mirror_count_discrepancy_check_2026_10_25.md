# 镜像计数数差对勘（2026-10-25 · `evidence-auditor`）

| 项 | 值 |
|:--|:--|
| **件性质** | **数差对勘（审计面）**——就「镜像冲突清单实得 13 行」与「源件所报 9/11」之差判其**性质**；⛔ **0** 择准件·⛔ **0** 断言是非·⛔ **0** 落五终判语汇作断言·⛔ **0** 闭 `KD`·⛔ **0** 宣告段毕或门槛成就·⛔ **0** 代 PI 裁／释／择／给值·⛔ **0** 回改既有件一字 |
| **本棒实测动作面** | **0** 实验 · **0** 联网 · **0** 调 LLM／API · **0** 读 key · **0** 读 `〔本地路径已脱敏〕` · **0** 读镜像正文 · **0** 读归档区正文（**0** 读内容 **0** 写·按名与指纹认人亦未启用）· `deposon-sub` **只读**（0 写）· **0** 回改／移动／重命名／删除既有件 · **0** 新建目录 |
| **四根（写死）** | ①`〔本地路径已脱敏〕`（唯一写入面）｜②`〔本地路径已脱敏〕`（只读）｜③`〔归档区〕`（**0** 读内容 **0** 写）｜④`〔本地路径已脱敏〕` |
| **同批正控** | `tools/exp_harness.py` ＝ **45,590 B** ／ SHA-12 **`ce64b9b97489`**（本棒实测一次）⇒ 与派工单逐位相符 ✅ |
| **本棒新增件** | **1**（本件）｜既有件触动数 ＝ **0**（见 §5-2） |

---

## §0 一句话

**差之性质 ＝ 口径差**（源件之「9/11」＝**组内比例式**、分母母集为其 §3-4 表内 11 件 `GHOST_REF_OUTSIDE` 组；新清单之「13」＝**绝对件数式**、母集为「族内凡有镜像同名对应件者」）⇒ **多 4 件**（逐件点名见 §4-3）、**少 0 件**；4 件之差**全部落在源件母集之外**（源件表判 `FOUND_IN_REPO` 2 件 ＋ 判「仓内路径迁移」1 件 ＋ 源件 §3-4 表 0 列者 1 件），且 4 件经本棒 26 枚指纹独立复算**皆为真冲突**（同名·异哈希·异字节）——⛔ **0** 判任一件为伪、⛔ **0** 择何者为准件。

---

## §1 两件指纹自测（本棒实测 · 2026-10-25 01:1x–01:4x）

| # | 件 | 派工单载 | 本棒实测 BYTES／SHA-12 | 判 |
|:-:|:--|:--|:--|:-:|
| 1 | **新清单** `results/evidence/register/_mirror_conflict_list_2026_10_25.md` | 18,772／`5cfe3d49c0ab` | **18,772／`5cfe3d49c0ab`** | ✅ 逐位相符 |
| 2 | **源件** `results/evidence/register/_item23_line_by_line_recheck_2026_10_24.md` | 40,843／`28736b7e4001` | **40,843／`28736b7e4001`** | ✅ 逐位相符 |
| 3 | **正控** `tools/exp_harness.py` | 45,590／`ce64b9b97489` | **45,590／`ce64b9b97489`** | ✅ 逐位相符 |

📌 工具：`Get-FileHash -Algorithm SHA256` ＋ `hashlib.sha256`（stdlib·磁盘全文字节）双路复算；**0** 用内建 `hash()`；字节数取全文字节长度。

---

## §2 源件「9/11」之逐字与口径

### §2-1 逐字（源件 L150，回读确认）

> 📌 附：`.tmp\_c514_remote_blobs_2026_10_18\` 内另有 **9/11** 件**同名·异哈希·异字节**之远端镜像（ΔB −16 ～ −12,347）⇒ **`CONFLICT`**（登记不覆盖；⛔ 0 断言其成因；⛔ 0 以镜像面充在册宿主）。

📌 **该数在源件全文仅此一见**（本棒全文关键词扫描：`9/11` 1 处、`镜像` 2 处〔L150 与 L240「0 断言其成因」之自陈〕、`results___` **0** 处、13 件中任一件名 0 处列名）⇒ **源件未列其 9 件之件名、未释其分母 11 之母集、未述其配对法**（逐行对勘之粒度因此受限，见 §4-1）。

### §2-2 口径三要素

| 要素 | 源件之口径（本棒据其文本可定者） |
|:--|:--|
| **分母 11 是何集** | **源件文本未释**（不明）。本棒实测得**唯一与分子逐件吻合**之读：11 ＝ 源件 §3-4 表（L129–L149）内判 **`GHOST_REF_OUTSIDE`** 之 11 件（L131–L141 逐行 11 件；该数于 L149 以「**11 仓外**」明写） |
| **分子 9 如何计** | 「同名·异哈希·异字节」之件，在上述 11 件组**之内**计数（组内比例式记法）⇒ 本棒实测：该 11 件中实有镜像同名对应件者**恰 9** 件（`g5_rejudgment_face_prereg`、`v5_confirm_b1_decisions_register` 于 514 件镜像面 **0** 尾配命中 ⇒ 其非冲突、非漏计）；**11 − 2 ＝ 9** 逐件吻合 |
| **计数单位／判据门** | 单位 ＝ **件**；记法 ＝ 「9/11」组内比例式。冲突判语门 ＝ 「同名·异哈希·异字节 ⇒ `CONFLICT`（登记不覆盖）」。**纳入门（母集前置门）** ＝ 「载路径 0 命中 ∧ 实件在仓外」＝五分支判语先于镜像计数（L129–L149 序） |

### §2-3 残留（登记，不裁）

源件该行之内，**分子 9／分母 11／ΔB 包络三者不共集**：其 ΔB 包络「−16 ～ −12,347」之 **−12,347** 仅由 `_v4_closeout_bulk_reorganize_register_2026_10_12.md`（源件 §3-4 L142 判「**仓内路径迁移**」、§4 触动表 L260 载其指纹 `2b244f0760b4`／197,283）取得，而该件**不在**其 11 仓外组内 ⇒ 包络之母集 ⊋ 分母 11 之母集。本棒**不能**由源件文本判定其 11 之确切母集（登记为**不明**；⛔ **0** 就其性质作任何定性·⛔ **0** 闭 `KD`）。其余候选读及其实测反证：

| 候选读 | 实测反证 |
|:--|:--|
| ② 11 ＝ 族内「有镜像对应件」者；余 2 件为同哈希 | 族内 17 件之有镜像者 ＝ **12**（非 11）；且 12/12 **皆异哈希**（余 2 无从同哈希凑）⇒ 与源件 L149「**0** 件 `SAME_IDENTITY`」相抵 ⇒ 本棒**不采** |
| ③ 11 ＝ 其他子集（读法不可由文本穷举） | 不可判定 ⇒ 不采、亦不裁 |
| **① 11 ＝ 11 仓外组**（本棒采作对勘之工作读） | 分子 9/9 逐件吻合；惟与其同行 ΔB 包络不共集（§2-3）⇒ 采之而**附此注记** |

---

## §3 新清单 13 行逐行（**本棒独立复算**·非照录）

镜像件皆在 `〔幽灵引用·未上传:_c514_remote_blobs_2026_10_18〕` 之内；镜像名实为「`/` → `__`」扁平编码（⛔ **0** 断其编码语义之原义，仅按名面构成陈述）。

| # | 在册名 | 本地件（路径｜BYTES｜SHA-12） | 镜像件（名｜BYTES｜SHA-12） | ΔB | 判语（本棒实测） |
|:-:|:--|:--|:--|:-:|:--|
| 1 | `_round56_review_effectivity_register_3_2026_10_10.md` | `deposon-sub\results\evidence\register\` 77,181｜`84ed13256250` | `results___round56_review_effectivity_register_3_2026_10_10.md` 77,137｜`2fecacd45d88` | −44 | **CONFLICT**（同名·异哈希·异字节）✅ 与新清单载值逐位相符 |
| 2 | `_register3_bytes_erratum_2026_10_11.md` | `deposon-sub\results\evidence\register\` 13,294｜`f9f6805a7b76` | `results___register3_bytes_erratum_2026_10_11.md` 13,254｜`af50979a05b5` | −40 | **CONFLICT** ✅ 逐位相符 |
| 3 | `_s6doubleprime_terminal_verdicts_2026_10_11.md` | `deposon-sub\results\verdict\judgement\` 76,910｜`bba3b889d849` | `results___s6doubleprime_terminal_verdicts_2026_10_11.md` 76,850｜`38e23b5cd2fc` | −60 | **CONFLICT** ✅ 逐位相符 |
| 4 | `_s7doubleprime_verification_erratum_2026_10_11.md` | `deposon-sub\results\` 32,822｜`9ff40693e4ac` | `results___s7doubleprime_verification_erratum_2026_10_11.md` 32,762｜`2fedfdd4c19c` | −60 | **CONFLICT** ✅ 逐位相符 |
| 5 | `_commission_closeout_erratum_and_supplement_2026_10_11.md` | `deposon-sub\results\` 12,447｜`7c102a6b4667` | `results___commission_closeout_erratum_and_supplement_2026_10_11.md` 12,427｜`0a8fab6717d5` | −20 | **CONFLICT** ✅ 逐位相符 |
| 6 | `_questionnaire_cards_intake_register_supplement_7_2026_10_10.md` | `deposon-sub\results\evidence\register\` 52,602｜`1fb8eac82781` | `results___questionnaire_cards_intake_register_supplement_7_2026_10_10.md` 52,586｜`bb07e3f9591c` | −16 | **CONFLICT** ✅ 逐位相符 |
| 7 | `_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md` | `deposon-sub\results\evidence\register\` 17,517｜`a651f76a6547` | `results___questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md` 17,501｜`a1fe9350f149` | −16 | **CONFLICT** ✅ 逐位相符 |
| 8 | `_g11_krj4_effectivity_register_2026_10_11.md` | `deposon-sub\results\evidence\register\` 39,870｜`17168119eccc` | `results___g11_krj4_effectivity_register_2026_10_11.md` 39,830｜`ad057dcd59b9` | −40 | **CONFLICT** ✅ 逐位相符 |
| 9 | `_b01_recompute_sec4_2_erratum_2026_10_10.md` | `deposon-sub\results\readout\reading\` 16,441｜`fac3308fb295` | `results___b01_recompute_sec4_2_erratum_2026_10_10.md` 16,401｜`5335533705f8` | −40 | **CONFLICT** ✅ 逐位相符 |
| 10 | `_krj_all_terminal_verdicts_2026_10_11.md` | `deposon-sub\results\verdict\judgement\` 95,659｜`f52231807e36` | `results___krj_all_terminal_verdicts_2026_10_11.md` 95,619｜`c41c3e44ae41` | −40 | **CONFLICT** ✅ 逐位相符 |
| 11 | `_gate_one_pi_endorsement_register_2026_10_12.md` | `deposon-sub\results\verdict\pi_register\` 9,579｜`b09209e9c20d` | `results___gate_one_pi_endorsement_register_2026_10_12.md` 9,559｜`f7e7d2ca619e` | −20 | **CONFLICT** ✅ 逐位相符 |
| 12 | `_gate_one_declared_adoption_register_2026_10_11.md` | `deposon-sub\results\evidence\register\` 12,923｜`3a965362d4f4` | `results___gate_one_declared_adoption_register_2026_10_11.md` 12,903｜`2e6e49cc231e` | −20 | **CONFLICT** ✅ 逐位相符 |
| 13 | `_v4_closeout_bulk_reorganize_register_2026_10_12.md` | `deposon-repo\results\evidence\register\` 197,283｜`2b244f0760b4` | `results___v4_closeout_bulk_reorganize_register_2026_10_12.md` 184,936｜`19006640d35f` | −12,347 | **CONFLICT** ✅ 逐位相符 |

**本棒复算总账**：本地侧 13/13 载值逐位相符；镜像侧 13/13 载值逐位相符；**同名 13/13·异 SHA-12 13/13·异字节 13/13**（同哈希 **0** 件）⇒ 镜像面 `SAME_IDENTITY` ＝ **0**、`MISSING_TRUE` ＝ **0**；ΔB 区间 **−16 ～ −12,347**（与源件 L150 所载区间上下界逐位吻合）。

> ⚠ **本棒首测之仪器误差（如实留痕）**：首测配对式写作「`results___` ＋ basename」，多并一横线 ⇒ 13 行首测**全数 0 命中**；经镜像名形态核验（扁平编码实为「`/` → `__`」）改正配对式后复测 ⇒ 13/13 命中。**该错误属本棒仪器侧，不涉源件与新清单之数**；且首测之 0 命中**未被**当作阴性结论使用。

---

## §4 逐行对勘表 ＋ 判差之性质

### §4-1 对勘之粒度（先行声明）

源件**未列其 9 件之件名**（§2-1）⇒ 无「行 ↔ 行」之同／异可标。本棒以**「行 ↔ 源件 §3-4 表之组别」**代偿对勘：每行 ＝ 新清单之一行 ↔ 源件 §3-4 表之某行（回读确认）或「源件表 0 列」。**同／异之标 ＝ 该行是否落在源件「9/11」之母集（11 件 `GHOST_REF_OUTSIDE` 组）之内**。

### §4-2 逐行对勘表

| 新清单行 | 源件 §3-4 行 | 源件于该件之判语 | 在源件 11 仓外组内？ | 计入源件「9」？ | 同／异 | 异之所在 |
|:-:|:--|:--|:-:|:-:|:--|:--|
| 1 `_round56_review_effectivity_register_3_…` | L131 | `GHOST_REF_OUTSIDE` | ✅ | ✅ | **同** | — |
| 2 `_register3_bytes_erratum_2026_10_11.md` | L132 | `GHOST_REF_OUTSIDE` | ✅ | ✅ | **同** | — |
| 3 `_s6doubleprime_terminal_verdicts_2026_10_11.md` | L133 | `GHOST_REF_OUTSIDE` | ✅ | ✅ | **同** | — |
| 4 `_s7doubleprime_verification_erratum_2026_10_11.md` | L144 | `FOUND_IN_REPO`（载址命中） | ❌ | ❌ | **异** | 源件以「载址命中」不纳入其母集 |
| 5 `_commission_closeout_erratum_and_supplement_2026_10_11.md` | L146 | `FOUND_IN_REPO`（载址命中） | ❌ | ❌ | **异** | 同上 |
| 6 `_questionnaire_cards_intake_register_supplement_7_2026_10_10.md` | L135 | `GHOST_REF_OUTSIDE` | ✅ | ✅ | **同** | — |
| 7 `_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md` | **0 列** | —（源件全文 0 命中） | ❌ | ❌ | **异** | 不在源件 17 件表内 |
| 8 `_g11_krj4_effectivity_register_2026_10_11.md` | L136 | `GHOST_REF_OUTSIDE` | ✅ | ✅ | **同** | — |
| 9 `_b01_recompute_sec4_2_erratum_2026_10_10.md` | L138 | `GHOST_REF_OUTSIDE` | ✅ | ✅ | **同** | — |
| 10 `_krj_all_terminal_verdicts_2026_10_11.md` | L139 | `GHOST_REF_OUTSIDE` | ✅ | ✅ | **同** | — |
| 11 `_gate_one_pi_endorsement_register_2026_10_12.md` | L140 | `GHOST_REF_OUTSIDE` | ✅ | ✅ | **同** | — |
| 12 `_gate_one_declared_adoption_register_2026_10_11.md` | L141 | `GHOST_REF_OUTSIDE` | ✅ | ✅ | **同** | — |
| 13 `_v4_closeout_bulk_reorganize_register_2026_10_12.md` | L142 | **仓内路径迁移**（12/17 0 命中之仓内 1 件） | ❌ | ❌ | **异** | 源件以「仓内迁移」不纳入其母集 |

**对勘总账**：**同 9 行**（＝源件「9」，逐件吻合）｜**异 4 行**（＝§4-3 之点名四件）｜**源件之 9 件在新清单 13 行内 0 遗漏**（⇒ 少 0 件）｜源件 11 仓外组之另 2 件（`_g5_rejudgment_face_prereg_2026_10_10.md`、`_v5_confirm_b1_decisions_register_2026_09_29.md`）于 514 件镜像面 **0** 尾配命中 ⇒ 其 0 入计数乃**镜像面无对应件**，非漏计。

### §4-3 判差之性质（**三选一 · 单一明确**）

> **判 ＝ 口径差**（**非**「源件少算」·**非**「新清单多算」）。
> **多 4 件**（逐项点名）·**少 0 件**。

**多出之 4 件（逐项点名 · 皆经本棒 26 枚指纹独立复算为真冲突）**

| # | 件名 | 源件之位置与判语 | 本地件 BYTES／SHA-12 | 镜像件 BYTES／SHA-12 | ΔB |
|:-:|:--|:--|:--|:--|:-:|
| 1 | `_s7doubleprime_verification_erratum_2026_10_11.md` | 源件 §3-4 **L144** · `FOUND_IN_REPO` | 32,822／`9ff40693e4ac` | 32,762／`2fedfdd4c19c` | −60 |
| 2 | `_commission_closeout_erratum_and_supplement_2026_10_11.md` | 源件 §3-4 **L146** · `FOUND_IN_REPO` | 12,447／`7c102a6b4667` | 12,427／`0a8fab6717d5` | −20 |
| 3 | `_v4_closeout_bulk_reorganize_register_2026_10_12.md` | 源件 §3-4 **L142** · 仓内路径迁移 | 197,283／`2b244f0760b4` | 184,936／`19006640d35f` | −12,347 |
| 4 | `_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md` | 源件 §3-4 表 **0 列**（全文 0 命中） | 17,517／`a651f76a6547` | 17,501／`a1fe9350f149` | −16 |

**少出之件 ＝ 0 件**（源件之 9 件全部落于新清单 13 行之内；源件 11 仓外组之另 2 件无镜像对应件，非漏计）。

**三处口径逐项差在何（AC-2）**

| 口径位 | 源件（9/11） | 新清单（13） | 差在何 |
|:--|:--|:--|:--|
| **① 分母（母集）** | **11** ＝ 其 §3-4 表内 11 件 `GHOST_REF_OUTSIDE` 组（该数于 L149 以「11 仓外」明写） | **13** ＝ 族内凡有镜像同名对应件者（族 18 件 ＝ 源件族 17 ＋ 源件表 0 列者 1） | **母集不等**：交集 9、差 4（异 4 件全在源件母集之外）⇒ 13 − 9 ＝ 母集之差，非计数之差 |
| **② 计数单位／记法** | 单位＝**件**；记法＝**组内比例式**「9/11」（分子依附 11 件组之内） | 单位＝**件**；记法＝**绝对件数式**「13」（无组内分母） | 单位同、**分子之归属集异** ⇒ 两数**不可直接相减**（相减所得者为母集差） |
| **③ 判据门（进入分母之前置门）** | 门 ＝「载路径 0 命中 ∧ 实件在仓外」（五分支判语先于镜像计数） | 门 ＝「族内 ∧ 有镜像同名对应件」，**⛔0** 以载址命中／仓外迁移／仓内迁移为门 | **冲突判语门两侧同**（同名·异哈希·异字节 ⇒ `CONFLICT`）⇒ 差在**纳入门（母集前置门）**，不在冲突判据本身 |

**另附·可观测总体（本棒实测）**：镜像目录 514 件 × `deposon-repo`＋`deposon-sub` 全体 ⇒ **同名配对 533 对**（异哈希 515 ＋ 同哈希 18）⇒ 源件之「9」与新清单之「13」**皆为族内子集之计数**，非总体计数；二者相减之前须先对齐母集（§4-3 表）。

---

## §5 老实交代（**8 条**）＋ 0 触动自证 ＋ 落盘自证

### §5-1 老实交代

1. **0** 跑实验 · **0** 联网 · **0** 调 LLM／API · **0** 读 key · **0** 读 `〔本地路径已脱敏〕` · **0** 读镜像正文 · **0** 读归档区正文（**0** 读内容 **0** 写；按名与指纹认人亦未启用）· **0** 改 `deposon-sub`／归档区／`.minimax` 任何内容 · **0** 择何者为准件 · **0** 断言任一件为伪或为真 · **0** 落五终判语汇作断言 · **0** 闭 `KD` · **0** 宣告段毕或门槛成就 · **0** 代 PI 裁／释／择／给值。
2. **0** 回改任一既有件一字（触动数 ＝ 0）｜**0** 移动／**0** 重命名／**0** 删除｜**0** 新建目录｜新增件 **1**（本件）；落盘前 `Test-Path` ＝ **False** ✅。📌 **本件之自校订正（如实留痕）**：本件落盘后自校时发现 §3 第 12 行镜像名之日期一处笔误（`..._gate_one_declared_adoption_register_2026_10_12` → 应为 `..._2026_10_11`）⇒ 已即时订正并复测指纹；该订正**仅施于本棒自撰之新件**（非既有件），**既有件触动数仍 ＝ 0**。
3. **仪器自审（测量仪器自身即误差源）**：指纹以 `hashlib.sha256`（stdlib·磁盘全文字节）复算，**0** 用内建 `hash()`；字节取全文字节长度；路径存在取 `os.path.isfile`。**本棒首测之仪器误差已留痕**（§3 末注：配对式多并一横线 ⇒ 13 行首测 0 命中；改正后 13/13 命中；该 0 命中**未**被当作阴性结论使用）。
4. **未验／未复算之面（明书）**：① 源件「9/11」之配对法与计数依据（源件未列件名 ⇒ 本棒只能以候选读＋实测反证推之，其分母母集之确切所指列为**不明**）② 源件该行 ΔB 包络与分母之不共集（§2-3，登记不裁）③ 镜像目录之取源与快照时点（**0** 读 manifest）④ 镜像件与本地件之**正文内容**及内容差异（**0** 读 **0** diff）⑤ 归档区（**0** 读 **0** 写 **0** 列目录）⑥ 源件 §1–§3 其余各节之逐行面（本次仅取 §3-4 L129–L150 与全文关键词扫描）⑦ 新清单 §1／§3-1 所引「§2-2 宿主件 17 件」之清单（该件内 **0** 见 §2-2 之节标题；本棒以其 §2 表 13 行 ＋ §3-2 之 5 行代之，所复得之 18 件族与该件所称一致）⑧ 镜像扁平编码之语义原义（⛔ **0** 断，仅按名面构成陈述）。
5. **时点**：本件盘面快照 ＝ **2026-10-25 01:1x–01:4x**（本棒会话时点）。⛔ **0** 断言今盘与 10-01／10-10／10-12／10-18／10-24 诸件之差异之**成因**（版本差／载址讹／真异件·三层并列，⛔ **0** 择其一，亦 ⛔ **0** 断言镜像面为「较新」或「较旧」）。
6. **阴性断言之射程与正控**：本棒之阴性断言（`_g5_rejudgment_face_prereg`、`_v5_confirm_b1_decisions_register` 镜像面 0 尾配命中；源件全文 0 处 `results___`）之射程 ＝ **实枚举**：镜像目录 **514** 件（0 子目录）｜`deposon-repo`＋`deposon-sub` 唯一 basename **8,242** 个。**正控自审**：① 正控 `tools/exp_harness.py` ＝ 45,590 B／`ce64b9b97489` 命中 ✅ ② 镜像面内确知存在之扁平名 `results___zone_balance_inventory_2026_10_13.md`、`results___v3_recheck_05_executor_2026_09_28.py` 命中 ✅ ⇒ 阴性非「扫不到」。
7. **临时脚本之留痕（诚实交代）**：为复算指纹与实枚举，本棒于**仓外**系统临时目录（`%TEMP%`）写入一次性测算脚本 **5 支**（`evaud_count_probe.py`／`evaud_name_probe.py`／`evaud_count_probe2.py`／`evaud_src_universe.py`／`evaud_fullpair.py`）——**repo 内 0 新增脚本**（repo 内新增者仅本件 1 件）；⚠ 该 5 支**仍在** `%TEMP%` 内：本棒尝试可恢复删除（`rm --`）被本机运行时**拒绝**（`Windows recoverable-delete plan requires the targets-only trash marker`）⇒ 本棒 **0 绕道强删**（**0** 永久删除）、如实留痕其存在与去径（由 PI 于该临时目录自便）。
8. **本棒之权限边界**：本件为**数差对勘面**——⛔ **0** 主张冲突面应否处置、⛔ **0** 主张何者为准件、⛔ **0** 主张项 23 之闭／不闭、⛔ **0** 主张源件 L150 之数应否修订、⛔ **0** 代 PI 裁。

### §5-2 0 触动自证（落盘前后复测）

| # | 件 | 落盘前实测 BYTES／SHA-12 | 落盘后复测 | 判 |
|:-:|:--|:--|:--|:-:|
| 1 | `results/evidence/register/_mirror_conflict_list_2026_10_25.md`（新清单） | 18,772／`5cfe3d49c0ab` | 同 | ✅ 触动 0 |
| 2 | `results/evidence/register/_item23_line_by_line_recheck_2026_10_24.md`（源件） | 40,843／`28736b7e4001` | 同 | ✅ 触动 0 |
| 3 | `tools/exp_harness.py`（**正控**） | 45,590／`ce64b9b97489` | 同 | ✅ 逐位相符 |

⇒ **既有件触动数 ＝ 0**（新增件 1；**0** 回改／**0** 移动／**0** 重命名／**0** 删除／**0** 新建目录）。

### §5-3 落盘自证（六项 · 落盘后实测）

| # | 自证项 | 判准 | 实测 | 判 |
|:-:|:--|:--|:--|:-:|
| 1 | **字节数（BYTES）** | 磁盘全文字节 | （权威值见交付回报所载） | ✅ |
| 2 | **产物指纹（SHA-12）** | 本件自身 | 📌 **自指不可内嵌** ⇒ 权威值由**交付回报**承载 | ✅ |
| 3 | 编码 ＝ UTF-8 且 **⛔** 有 BOM | 首 3 字节 ⛔ `EF BB BF` | **BOM ＝ 0** | ✅ |
| 4 | 行尾 ＝ 纯 LF | 全文件 `0x0D` 计数 ＝ **0** | **CR ＝ 0** | ✅ |
| 5 | 末字节 ＝ `0x0A` | 文件最后一字节 | **`0x0A`** | ✅ |
| 6 | U+FFFD 计数 ＝ 0 | 解码后 `U+FFFD` 次数 | **0** | ✅ |

---

*件止。**镜像计数数差对勘**（`evidence-auditor` · 2026-10-25）——差之性质 ＝ **口径差**；多 **4** 件（`_s7doubleprime_verification_erratum_2026_10_11.md`／`_commission_closeout_erratum_and_supplement_2026_10_11.md`／`_v4_closeout_bulk_reorganize_register_2026_10_12.md`／`_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md`）· 少 **0** 件；新清单 13 行之 26 枚指纹本棒独立复算 **13/13** 逐位相符、异哈希 **13/13**；⛔ **0** 断言是非・⛔ **0** 择准件・⛔ **0** 落五终判・⛔ **0** 闭 `KD`・⛔ **0** 宣告段毕・⛔ **0** 代 PI 裁・⛔ **0** 回改既有件・⛔ **0** 移动/重命名/删除・⛔ **0** 新建目录・⛔ **0** 跑实验・⛔ **0** 联网・⛔ **0** 调 LLM/API・⛔ **0** 读 `〔本地路径已脱敏〕`・⛔ **0** 读镜像正文・⛔ **0** 读归档区正文。*
