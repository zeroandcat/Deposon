# 域级统一回填之设计件 ｜ 2026-10-18

- **棒**：protocol-keeper（实验设计／度量 · 口径与预登记）
- **上位令**：PI 裁（卡 `ask_e5fcc8d2e9acd2e78e8e147b` Q3 opt1 · 2026-10-18 14:53:52.058）逐字：「**域级统一回填（推荐：115 件之旧指纹引用面之批量更正另立棒（先设计后行））**」
- **本件性质**：**设计件**（先设计后行之「设计」面）｜📋 **候 PI 复核生效 · 生效即锁**
- **面**：⛔ **0 执行任何更正**｜⛔ **0 代 PI 裁／释／择**｜⛔ **0 闭任何既有 KD**｜⛔ **0 落五终判**｜⛔ **0 宣告任何段毕**｜⛔ **0 回改任何既有件**
- **面**：本棒 **0 实验**、⛔ **0 LLM**、⛔ **0 联网**｜R4：**0 密钥明文**入本件／0 入 prompt／0 入日志

## 标的件（三面 · 逐字回读后实测指纹）

| 标的 | 路径 | SHA-12 | bytes | 核验 |
|---|---|---|--:|---|
| 核证件（16 碰撞） | `results/_thirdparty_16_overwrite_necessity_2026_10_18.md` | `6435ecc3a540` | 14,122 | 本棒实测 ✔ |
| 镜像对比件（514 碰撞面） | `results/_mirror_morphology_comparison_2026_10_18.md` | `39dcf23f9f67` | 134,278 | 本棒实测 ✔ |
| **锚件真值面**（被引件本体） | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_d1_ruling_and_s3_transition_2026_10_01.md` | **`dc9cb0e02922`** | **28,370** | 本棒实测 ✔ |
| **旧值实体**（10-12 远端冻结件） | `〔归档件引用·未上传:_d1_ruling_and_s3_transition_2026_10_01.md.remote_2026_10_12〕` | **`66f900b7598b`** | **28,352** | 本棒实测 ✔ |

**指纹口径**：`hashlib.sha256(全文字节).hexdigest()[:12]`（⛔ 0 用内建 `hash()`）——本棒实测确认三面与上位派工单所载**全等**（`dc9cb0e02922`／28,370 B）。

**锚件版式实测**：`sha12=dc9cb0e02922`｜`bytes=28,370`｜**BOM=无**｜**CR=0**｜**LF=272**｜**本体含旧值字面 0 处**、含现值字面 0 处 ⇒ **本设计之更正对象为「引用侧」，被引件本体 byte 0 触动**（沿族 E／族 D 之既有实测结论，本棒独立复测全等）。

---

## §0 结论摘要

### §0-1 三问初判

| 问 | 判 | 依据 |
|---|:-:|---|
| **Q1 素材可得？** | **是** | 在册域 **98 件／678 处**逐件逐处可枚举（两次独立测量**全等**）；旧值实体唯一且可实测（28,352 B·CR=0·无 BOM） |
| **Q2 实验可设计？** | **是** | 构造（引用形态六型＋区级面）已实测归类；执行序、判据、验证面皆可机械构造（承 10-14 族 E 执行件之七步法） |
| **Q3 命题可证伪？** | **是** | kill-line 可机械化（目标面 0 残留 ＋ 逐件 diff 严格等于计划行集合 ＋ 留证面计数冻结）——⚠ **惟原拟「全仓 0 命中旧值」不可满足**，见 §5 |

### §0-2 claim（可证伪命题）

> 旧指纹 `66f900b7598b` 在**在册域**内之**「现行身份指针」用途**（M 台账字节三元组／N 行级指针）可被**逐处**机械更正为 `dc9cb0e02922`（bytes 成对：`28,352`/`28352` → `28,370`/`28370`），且更正**不改动任何命题、判定、计数、时戳、路径、行号、逐字引文**；**Q／P／A／C／D／F／E 各型留证面 0 触动**。

**反方可证伪面**：若任一处更正后致「历史条文直引」失真、或计数核验键之比对对象消失、或被引件本体字节变动、或留证面计数漂移 ⇒ claim 被证伪，判死线 K-028-* 触发。

### §0-3 候裁面三项（详见 §6）

| # | 候裁项 | 状态 |
|:-:|---|---|
| ① | **0 回改铁律之例外授权**（受限例外之射程与形态） | 🔴 候 PI 明裁 |
| ② | **更正目标值之确认**（`dc9cb0e02922`／28,370 B；及「另立新锚」替代案） | 🔴 候 PI 明裁 |
| ③ | **执行之窗口与范围**（repo／sub／letters／pi_rulings／archive／glm 各面之可写性与窗口） | 🔴 候 PI 明裁 |

---

## §1 仪器与控制面

| 项 | 实测 |
|---|---|
| 遍历 | `os.walk` ＋ `onerror` 断言 · **遍历错误 = 0** |
| 读取 | 二进制安全（读 bytes 计数）· **读错误 = 0** · **0 大小跳过** |
| 遍历件数 | 45,898 件（四区：repo／sub／archive／glm） |
| **阳性对照** | `dc9cb0e02922` ＝ **1,222 处／114 件** ⇒ 扫描面有效 |
| **阴性对照** | `66f900b7598c`（末位扰动）＝ **0 处** ⇒ 无假阳性 |
| **稳定性** | 两次独立测量（间隔 20 s）**逐区逐件全等**：`STABLE = True` |
| 排除面 | `.git`／`__pycache__`／`node_modules`；**本棒自身输出**（自指剔除） |

---

## §2 域面之全量枚举

### §2-1 在册域（排除 `.tmp` 工作面）＝ **98 件／678 处**

| 区 | 件 | 处 |
|---|--:|--:|
| REPO（`deposon-repo`） | 29 | 189 |
| SUB（`deposon-sub`） | 40 | 327 |
| ARCHIVE（`〔归档区〕`） | 26 | 157 |
| GLM（交付面·稳定面） | 3 | 5 |
| **合计** | **98** | **678** |

### §2-2 `.tmp` 工作面（**另计 · 非在册**）

`.tmp` 于本棒测量时点为 **65 件／2,577 处**，且**面在持续变动**（本棒 15:13–15:19 之 6 分钟内，即因并行棒之写入与本棒自身探针输出而新增数十件）。

⇒ **`.tmp` 不得计入在册基线**：其计数随时点漂移，纳入将使「设计冻结之基线」与「执行时之现况」不可比。**本设计之基线一律以 §2-1 之 98 件／678 处为准**；`.tmp` 之处置见 §6-③。

### §2-3 「115 件」之重构（如实交代 · 未软化）

上位派工单与核证件 `KD-25` 所载之 **115 件**，经本棒以 **mtime 时间切片法**重构：

> **115 ＝ 98（在册域）＋ 17（`.tmp` 工作面，于 2026-10-18 09:56:29 ≤ T < 12:05:51 之任一时刻）**

- 第 17 个 `.tmp` 命中件＝`hfr_scan_d_ledger.json`（mtime **2026-10-18 09:56:29**）；第 18 个＝`_16_compare.json`（mtime **2026-10-18 12:05:51**，为 16 碰撞核证件自身之比对产物）。
- 核证件之探针 `_16_fingerprint_hunt.py` 落盘于 **12:08:06** ⇒ 其计数必在 **12:05:51 之前**取得 ⇒ **落于上述窗口内**。
- **结论**：`KD-25` 之 115 **非数错**，系**含 `.tmp` 之宽口径＋较早时点**之读数。

**⚠ 口径警示（须入 PI 之裁面）**：在册域另有三组历史读数并存，**互异源于口径与时点，非任一方为数错**：

| 读数 | 值 | 时点／口径 | 出处 |
|---|--:|---|---|
| U-5 引用面 | 31 件／156 处 | 10-10 · SUB 只读区 | `_u5_fingerprint_relocation_erratum_2026_10_10.md`（`200c7e4c57cb`） |
| B 类陈旧登记 | 17 件／89 处 | 10-10 · 族 E 具名 B 类 | `_u5b_citation_surface_revision_2026_10_10.md`（`5cc29c53a422`） |
| 族 D REPO 面 | 20→21 件 | 10-14 | 族 D 对照面／REPO 执行件 |
| 阳性对照 | 51 件 | ~14:5x · repo 单区 | `pi_rulings/_pi_card_answers_register_2026_10_18_v100.md` |
| 控制组 | 53 件 | 14:58 · repo 单区 · 含 `.tmp` · 跳过 >4 MiB | `.tmp/dw108_probe.out.txt` |
| `KD-25` | **115 件** | ~12:07 · 四区 · 含 `.tmp` | `_thirdparty_16_overwrite_necessity_2026_10_18.md`（`6435ecc3a540`） |
| **本设计基线** | **98 件／678 处** | **15:19 · 四区 · 排除 `.tmp` · 两次全等** | **本件 §2-1** |

---

## §3 引用形态面之分类（承族 E 四型 ＋ 区级面）

### §3-1 分类口径之沿用（⛔ 0 自创新类）

本设计**沿用**已在册且**生效即锁**之分类口径：`5cc29c53a422` §2 之**处级形态四型**（M／N／P／Q）与 `345517455dcf` 之 **R-B01-K 双键标注制**，并补入**区级排除面**（F／C／D／E）——⛔ **0 主张此分类为唯一正确分类**（沿 `5cc29c53a422` §9-4 同旨，登记于 §7 KD-30）。

| 型 | 形态 | 在册域处数 | 含该型件数 | 处置口径（沿用） |
|:-:|---|--:|--:|---|
| **M** | 台账**字节三元组**（指纹＋bytes＋时戳／版式 成对行） | 63 | 21 | **成对刷**（指纹＋bytes 同刷，⛔ 0 仅换指纹而留旧 bytes） |
| **N** | **行级指针**（指纹＋行号＋逐字，三重绑定） | 174 | 15 | **指纹＋行号双刷**；行号实测仍成立 ⇒ **行号 0 动** |
| **P** | **计数核验键**（指纹作 grep 计数之比对键） | 41 | 11 | ⛔ **0 擅改计数**（改之即失其核验义）——**须 PI／下游明裁** |
| **Q** | **条文直引**（引「0 追溯」「既有计数」等历史条文） | 26 | 9 | **0 动** —— 其引用系历史事实之登记，非现行身份指针 |
| **A** | 述引／历史标注面（「历史键」「旧指纹」「已漂移」「悬空」等） | 117 | 33 | **0 动** —— 记述旧值之登记件，改之即毁其述引对象 |
| **C** | 对外稿面（`letters/` ＋ 归档对外稿） | 18 | 10 | **0 改** —— 已发／可发之对外函件 |
| **D** | 机器台账／JSON 记录面（如 `_upload_ledger_kimi_2026_10_01.json`，载**全串 sha256** 与实际上传 bytes） | 1 | 1 | **0 改** —— 其所记为**上传事实**，改之即伪证 |
| **F** | 10-12 远端冻结件（`.remote_2026_10_12`） | 155 | 24 | **0 改** —— 历史存照，其旧值即**该时点之真相** |
| **E** | `.tmp` 临时工作面 | —（另计） | — | **0 改**（非在册，见 §2-2） |
| **AMBIG** | **0 信号命中**（启发式分类器无判据可依） | 83 | 27 | **须逐字回读后方可定型** —— 本设计**⛔ 0 代其定型** |
| **合计** | | **678** | 98 件 | ✅ 求和自洽 |

> ⚠ **处数之和 ≠ 件数之和**（一文件可含多型）：98 件之逐件分布见附录 A。

### §3-2 R-B01-K 双键标注制（**在册·生效即锁·本设计⛔0违反**）

`345517455dcf` 逐字：「新键 `dc9cb0e02922` 之引用**一律标「现行」**、⛔ **0 裸键引用**（旧键 `66f900b7598b` 一律标「历史」）」。

⇒ **推论（关键）**：R-B01-K **要求旧键保留在盘并被标注为「历史键」**。故「全仓 0 命中旧值」之判据**与在册生效口径直接冲突**（详见 §5）。

### §3-3 刷候选面（**候裁后方可动**）

| 项 | 值 |
|---|--:|
| 刷候选件（M／N 型 · **区级排除者不计**） | **26 件** |
| 刷候选处（M＋N） | **237 处** |
| 纯 M／N 件（无 P／Q／A 混入） | **7 件** |

**逐件面见附录 A2**；**⚠ 其中含 P／Q／A 混入者，须逐处再判**（沿 10-14 REPO 执行件 §2-0 之「三要件」写前复核）。

---

## §4 批量更正之设计

### §4-1 更正之目标值映射面（四值成对 · 承 10-14 执行件 §1-4）

| 项 | **旧值（被刷新者）** | **新值（写入者）** |
|---|---|---|
| 指纹 SHA-12 | `66f900b7598b` | **`dc9cb0e02922`** |
| bytes（分隔写法） | `28,352` | **`28,370`** |
| bytes（无分隔写法） | `28352` | **`28370`** |
| BOM／CRLF | 无／0 | 无／0（**0 变**） |

**⛔ 0 擅改（G-8 沿用）**：计数列｜行数列｜时戳列｜路径列｜行号列｜逐字引文｜任何判定／终态之值 —— **0 重算、0 改写**。

### §4-2 执行之序（七步 · 承族 E／族 D 执行件 · FTFB）

1. **落前检**：执行登记件 `Test-Path=False` ＋ glob 0 命中 ⇒ ⛔ 0 覆盖；
2. **逐字回读源件**（⛔ 0 凭转述）＋ 被引件本体版式实测（本设计 §标的件表之值须逐项复现）；
3. **现况双通道实测**：通道 A ＝ Python `os.walk` ＋ `io.open(errors='strict')`；通道 B ＝ `ripgrep --count-matches`（⛔ **0 以 `-c` 行计数充处计数**）—— **两通道逐处全等**方可续；
4. 🔴 **写前逐处复核（三要件）**：判「真陈旧」＝ ① 在册面 ② **以旧指纹充现行身份指针**（M／N）③ ⛔ 非 P／Q／A／C／D／F／E／AMBIG；并**独立实测行位原位性**（L108／L115／L119–124／L128／L139／L141／L222 共 12 行，⛔ 0 外推至未测行号）；
5. **原子刷新**：逐处「**读 → 改该行 → 写 → 回读核「仅该处变」**」，逐件断言**差异行集合严格等于计划行集合**、**未触动行逐字节相等**；
6. **后验复算**：双通道残留复算 ＋ **留证面计数逐型冻结比对**（Q／P／A／C／D／F／E 之计数须**恰等于**执行前实测值）＋ 区级排除面 byte 级 0 触动比对；
7. **落盘字节级自测**（bytes／SHA-12／BOM／CR/LF 逐项自报）。

### §4-3 FTFB（判死线先于执行）

> **本设计件经 PI 复核生效之时 ＝ kill-line 之冻结之时；执行棒动手之时 ⇐ 须晚于该冻结。**
> 判死线（§4-4）**于本件内以字面冻结**，⛔ **0 事后调整**；若执行前现况与本件基线（§2-1 之 98 件／678 处）不符 ⇒ ⛔ **0 径行执行**，须**另出差异登记件**并候 PI 复核。

### §4-4 kill-line（机械判死线 · **逐条 id 化 · 生效即锁**）

| id | 判死线 | 机械化判据 |
|---|---|---|
| **K-028-1** | 目标面 0 残留 | 执行后 M／N 型在册件之旧值命中 **＝ 0**（双通道全等） |
| **K-028-2** | 留证面 0 触动 | Q／P／A／C／D／F／AMBIG 各型之旧值计数 **恰等于**执行前冻结值（逐型比对，0 漂移） |
| **K-028-3** | 逐件 diff 面 | 每件之**差异行集合严格等于**计划行集合；未触动行**逐字节相等** |
| **K-028-4** | 被引件本体 0 触动 | 锚件 SHA-12 **恒为** `dc9cb0e02922`／28,370 B／BOM 无／CR=0 |
| **K-028-5** | 双通道一致 | Python 与 ripgrep 之残留读数**逐处全等** |
| **K-028-6** | 语义 0 改动 | diff **仅**该指纹字面与配对 bytes 字面；计数／行号／时戳／判定 **0 变** |
| **K-028-7** | 区级面 0 写入 | F／C／D／E 各面件之 SHA-12 执行前后**全等** |
| **K-028-8** | R4 合规 | 0 密钥明文入件／入日志／入 prompt |

**触发处置**：任一条不成立 ⇒ **判该次执行失败**，须回滚至执行前 SHA-12 集合并如实登记；⛔ **0 径行补刷**。

---

## §5 ⚠ 第一候裁面：**0 回改铁律**与批量更正之张力（及验收判据之不可满足）

### §5-1 张力之实质

**0 回改铁律**（既有件之字节 0 触动）与「批量更正」**在字面上直接互斥**——更正即改写既有件。故本设计**不主张**径行突破，而是提出**受限例外之请裁**：

| 限缩项 | 请裁之射程 |
|---|---|
| 载体 | **仅** M／N 型且**仅**在册面（**⛔ 0 含** F／C／D／E／AMBIG） |
| 粒度 | **仅**该行、**仅**指纹＋配对 bytes 字面 |
| 留证 | 逐处新旧对照**必**入执行登记件（**先留证后改**） |
| 语义 | **⛔ 0 改**命题／判定／计数／时戳／路径／行号／逐字引文 |
| 授权 | **属 PI** —— ⛔ **0 代裁**、⛔ **0 径行采认** |

### §5-2 🔴 验收判据之修正（**原拟判据不可满足**）

上位派工单所拟验收判据「**更正后之全仓 0 命中旧值**」——**本棒实测判定其不可满足**，理由为**三重冲突**：

1. **R-B01-K 冲突**：该制**要求**旧键保留并标「历史键」（§3-2）；
2. **留证型冲突**：Q（历史条文直引 26 处）、P（计数核验键 41 处）、A（述引 117 处）、C（对外稿 18 处）、D（上传台账 1 处）、F（10-12 冻结件 155 处）合计 **358 处**——其旧值字面**皆为「该处之真相」**，刷之即毁其语义（在册既有处置口径明定「Q ＝ 0 动」「P ＝ ⛔ 0 擅改」「C／D ＝ 0 触动」「F ＝ 历史存照」）；
3. **既有执行先例冲突**：10-14 族 D／族 E 执行件之 PI 授权逐字**均仅及「真陈旧」**（REPO 18 处／SUB 34 处），且 `c7d20b3c18ba` **S-1** 逐字登记：族 E 内部对 Q 型「§4 标刷 vs §2／G-9 定 0 动」之冲突**未消解**，**候 PI 明裁**——该候裁项**至今未闭**。

⇒ **本设计将判据修正为**：「**目标面（M／N）0 残留 ＋ 留证面逐型计数冻结且 0 漂移**」（即 K-028-1 ＋ K-028-2 之组合）。
⚠ **此一判据之修正本身须 PI 核准**（⛔ 0 代裁）；若 PI 坚持原拟「全仓 0 命中」，则本设计之正解转为「**另立新锚**」（候裁②之替代案）——两案**不可兼得**。

---

## §6 候裁面三项（🔴 候 PI 明裁）

### 候裁① 0 回改铁律之例外授权

- **请裁**：是否授权**受限例外**（§5-1 之限缩射程）？抑或维持铁律、另立新锚？
- **本棒立场**：⛔ **0 代裁**。仅呈陈：受限例外**已有在册先例**（10-14 PI 明裁「甲 授权执行（REPO 面 18 处）」「甲 授权 sub 侧写入执行（真陈旧 34 处）」），故其**并非无先例之破例**，然**授权权属 PI**。
- **关联未闭项**：`c7d20b3c18ba` **S-1**（族 E 内部 Q 型口径冲突）——**本棒 ⛔ 0 径行闭之**，俟 PI 于本次一并明裁。

### 候裁② 更正目标值之确认

- **案甲（统一回填）**：目标值＝**`dc9cb0e02922`／28,370 B**（本棒实测真值：三区皆符，核证件已录远端 10-12 快照／R2 终态／live HEAD 三面全等）。
- **案乙（另立新锚）**：⛔ 0 回改既有引用，另立新锚件——则旧值**永久留存于 358 处留证面**，且**与案甲互斥**。
- **本棒立场**：⛔ **0 代裁**；仅呈陈案甲之**可证伪性更强**（目标面 237 处可逐处机械验证），案乙则**0 消除**任何旧值残留。

### 候裁③ 执行之窗口与范围

| 面 | 本棒实测之旧值面 | 性质 | 请裁 |
|---|--:|---|---|
| `repo/results` 等在册面 | 29 件／189 处 | 可写（**默认 0 触动**） | 是否授权 |
| `sub` 只读副本面 | 40 件／327 处 | 10-14 经 PI 明裁方可写（`c7d20b3c18ba` 逐字「SUB 只读副本面」） | 是否授权 |
| `letters` 对外稿面 | 10 件（C 类） | **⛔ 0 改**（已发函件） | 建议恒排除 |
| `pi_rulings` | 1 件／2 处 | PI 裁录之登记面 | 是否授权 |
| `〔归档区〕` 冻结面 | 26 件／157 处 | **⛔ 0 改**（历史存照） | 建议恒排除 |
| `GLM` 交付面 | 3 件／5 处 | 已交付受托方之面 | 是否授权（**0 默改**） |
| `.tmp` 工作面 | 65 件／2,577 处 | **非在册**·持续变动 | 建议恒排除 |

**⚠ 载体标识纪律（沿 `55155ec5f430` KD-S1）**：`⛔ 0 以文件名标识载体`——同名件跨面 **SHA-12 不同**（先例：`_t1_gate_closure…` REPO `caf20d1fa538`／72,926 B vs SUB `4bdd82c796b8`／72,934 B）⇒ 执行棒须以**字节级身份**定位载体。

**⚠ 执行窗口**：本棒实测 `.tmp` 面于 6 分钟内变动数十件 ⇒ **执行窗口须避开并行棒密集写入期**，且**执行前须以 T0 重测基线**（FTFB·§4-3）。

---

## §7 新出 KD 登记（编号域实测 **0 占用**）

> **编号域实测**：`results/`＋`sub`＋`archive` 三区全件（排除 `.tmp`）之 `KD-<token>` 扫描 —— **纯数字编号已占用＝{1…27, 83, 215, 720, 1494}**；**28 起 0 占用**。本件新出取 **KD-28 … KD-31**。⛔ **0 闭任何既有 KD**；⛔ **0 落五终判**（下表皆**缺陷登记**，非五终判之「kd」档）。

| KD | 面 | 登记 |
|---|---|---|
| **KD-28** | **判据冲突（「全仓 0 命中旧值」不可满足）** | 该判据与 R-B01-K（要求旧键标「历史」）、Q／P／A／C／D／F 留证型（**358 处**）、及 10-14 执行先例之「真陈旧」限缩授权**三重冲突**；`c7d20b3c18ba` S-1 之族 E 内部 Q 型口径冲突**至今未闭**。⇒ 判据修正为「目标面 0 残留 ＋ 留证面逐型计数冻结」**须 PI 核准**（§5-2） |
| **KD-29** | **计数口径之时点依赖** | `KD-25` 之 **115 ＝ 98 在册 ＋ 17 `.tmp`**，于 **2026-10-18 09:56:29 ≤ T < 12:05:51** 窗口内任一时刻成立（mtime 切片重构）；`.tmp` 面 6 分钟内变动数十件 ⇒ **在册基线须排除 `.tmp`** 且**执行前 T0 重测**，否则设计与执行不可比 |
| **KD-30** | **分类器置信** | §3 之分型系**启发式**（信号词典＋优先级）；**AMBIG 83 处／27 件** 0 信号命中须逐字回读后方可定型；⛔ **0 主张此分类为唯一正确分类**（沿 `5cc29c53a422` §9-4 同旨） |
| **KD-31** | **SUB 面可写性** | 本设计之 40 件／327 处多在 `sub`；该面**默认只读**，10-14 系经 PI 明裁（逐字「甲 授权 sub 侧写入执行」）方写 ⇒ **本设计 ⛔ 0 主张其可写**，授权与否属候裁③ |

---

## §8 0 触动自证与如实交代（未软化）

### §8-1 0 触动

本棒**未修改任何既有件**（⛔ 0 回改、0 覆写、0 追加、0 移动、0 改名、0 删除）。新增仅：

- **交付件 1**：`results/_domain_backfill_design_2026_10_18.md`（本件）
- **临时件**（`.tmp/`，皆为探针／读数）：`pk_domain_enum.py`／`pk_domain_analyze.py`／`pk_domain_polarity.py`／`pk_domain_classify.py`／`pk_kd_domain.py`／`pk_stable_baseline.py`／`pk_table_md.py`／`pk_write_design.py` ＋ 对应读数（`pk_domain_enum_out.{json,txt}`／`pk_domain_polarity.txt`／`pk_domain_classify.{json,txt}`／`pk_kd_domain.json`／`pk_stable_baseline.json`／`pk_table.md`）

⛔ 未触碰 V1–V3 资产｜⛔ 未回改冻结件｜⛔ 未写仓外目录（`〔归档区〕`／`deposon-sub` **只读**）｜⛔ 0 远端写｜⛔ 0 联网。

### §8-2 前棒残留面之核实

- **交付面**：`results/_domain_backfill_design_2026_10_18.md` **Test-Path ＝ False**（本棒落盘前实测）＋ 全仓递归 glob `_domain_backfill_design_2026_10_18*` ＝ **0 命中** ⇒ 前棒**0 残留**（与上位登记件逐字相符：「设计件（protocol-keeper 棒 `bg_17d6f0cb`）中断于达限·**0 落盘**」）。
- **`.tmp` 面**：按 `*domain_backfill*` 递归检索全仓（`Force` 含隐藏项）＝ **0 命中**；`.tmp` 内 14:36–15:09 之写入件经逐件核为**他棒**（`dw106_*`／`dw107_*`／`dw108_*`／`_main_register_v108_v109.py` 系列），**无一件属本任务面**。
- ⇒ **结论**：前棒**无探针可复用**，本棒**另立**；⛔ **0 覆盖**任何既有文件。

### §8-3 如实交代（未软化）

1. **本件为设计面** —— ⛔ **0 执行任何更正**；一切执行待 PI 核准后另派 worker 棒。
2. **`KD-25` 之 115 与本件之 98 互异** —— 本棒已以 mtime 切片**重构**其成因（§2-3：98 ＋ 17 `.tmp`），**非数错**，然**口径之别须 PI 认领**（KD-29）。
3. **分类为启发式** —— **AMBIG 83 处／27 件 0 信号命中**，本棒**⛔ 0 代其定型**；执行棒须逐字回读后方可判「真陈旧」（KD-30）。
4. **判据已修正** —— 「全仓 0 命中旧值」经实测**不可满足**，本设计代之以「目标面 0 残留 ＋ 留证面计数冻结」；⚠ **此修正须 PI 核准**，本棒⛔ 0 代裁（KD-28）。
5. **未做之事（如实登记）**：
   - ⛔ **0 做内容级全哈希扫描**以复验「旧值实体全域唯一」——本棒仅**实测已知实体**（28,352 B／CR=0／无 BOM✔），**全域唯一性沿用核证件之登记**，未独立复跑；
   - ⛔ **0 逐字回读**全部 98 件（**以信号词典＋上下文窗口 220 B 之启发式替代**）——故 §3 分型为**待逐字复核**之读数；
   - ⛔ **0 核**任何判定内容之正确性（属 evidence-auditor 面，沿 `5cc29c53a422` §9-5）。
6. **行位原位性** —— 本件**沿用** 10-14 之 12 行实测（L108／L115／L119–124／L128／L139／L141／L222）；**执行棒须于 T0 独立复测**，⛔ 0 径信本件。
7. **本棒 0 实验**、⛔ 0 主张任何判定／终态之内容当否｜R4：**0 密钥明文**。
8. **状态**：📋 **候 PI 复核生效 · 生效即锁**（生效后 §4-4 之 kill-line ⛔ 0 事后调整）。

---

## 附录 A · 在册域逐件面（98 件 · 678 处 · 本棒 15:19 实测）

> 表由 `.tmp/pk_table.md` **机械 spliced**（⛔ 0 手抄、⛔ 0 凭转述）｜**A1** 全量 98 件｜**A2** 刷候选（M／N）｜**A3** 区级排除（F／C／D）｜**A4** 零信号命中（AMBIG）

### A1 在册域逐件面（98 件 · 678 处）

| # | 区 | 载体（rel） | bytes | 旧值处 | 现值处 | 处级形态分布 |
|--:|---|---|--:|--:|--:|---|
| 1 | ARCHIVE | `letters_archive_2026_10_01/_commission_glm_dualtrack_paper_addendum_2026_10_01.md` | 35,892 | 1 | 0 | C×1 |
| 2 | ARCHIVE | `letters_archive_2026_10_01/_commission_kimi_upload_2026_10_01.md` | 29,880 | 1 | 0 | C×1 |
| 3 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_b01_new_key_classification_2026_10_10.md.remote_2026_10_12` | 38,669 | 14 | 100 | F×14 |
| 4 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_b01_new_key_residue_judgment_2026_10_10.md.remote_2026_10_12` | 41,984 | 7 | 8 | F×7 |
| 5 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_b01_p_counting_recompute_2026_10_10.md.remote_2026_10_12` | 22,104 | 18 | 14 | F×18 |
| 6 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_b14_audit_f2f3_closure_register_2026_10_11.md.remote_2026_10_12` | 29,620 | 1 | 0 | F×1 |
| 7 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_b14_vk_evidence_audit_2026_10_10.md.remote_2026_10_12` | 33,586 | 4 | 3 | F×4 |
| 8 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_d1_backfill_intake_verdict_2026_10_01.md.remote_2026_10_12` | 42,106 | 9 | 0 | F×9 |
| 9 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_mini_round_5_decisions_register_2026_10_01.md.remote_2026_10_12` | 53,131 | 13 | 0 | F×13 |
| 10 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_p_refresh_registration_preliminary_2026_10_10.md.remote_2026_10_12` | 32,780 | 14 | 10 | F×14 |
| 11 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_p_refresh_s0_judgment_2026_10_10.md.remote_2026_10_12` | 41,449 | 5 | 6 | F×5 |
| 12 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_p_refresh_scope_judgment_2026_10_10.md.remote_2026_10_12` | 34,004 | 2 | 3 | F×2 |
| 13 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_questionnaire_cards_intake_register_supplement_10_2026_10_10.md.remote_2026_10_12` | 84,127 | 2 | 0 | F×2 |
| 14 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_questionnaire_cards_intake_register_supplement_12_2026_10_10.md.remote_2026_10_12` | 121,137 | 2 | 4 | F×2 |
| 15 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_questionnaire_cards_intake_register_supplement_7_2026_10_10.md.remote_2026_10_12` | 52,602 | 2 | 2 | F×2 |
| 16 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_round56_b01_followup_disposition_plan_2026_10_10.md.remote_2026_10_12` | 31,004 | 5 | 5 | F×5 |
| 17 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_round56_pending_questions_compilation_2026_10_10.md.remote_2026_10_12` | 33,504 | 1 | 0 | F×1 |
| 18 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_round56_review_effectivity_register_2026_10_10.md.remote_2026_10_12` | 49,013 | 5 | 5 | F×5 |
| 19 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_round56_review_effectivity_register_3_2026_10_10.md.remote_2026_10_12` | 77,181 | 6 | 5 | F×6 |
| 20 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_round56_review_effectivity_register_4_2026_10_11.md.remote_2026_10_12` | 46,908 | 1 | 0 | F×1 |
| 21 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_round56r8_dispositions_register_2026_10_10.md.remote_2026_10_12` | 46,135 | 5 | 4 | F×5 |
| 22 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_t1_gate_closure_and_recompute_verdict_2026_10_01.md.remote_2026_10_12` | 72,951 | 12 | 0 | F×12 |
| 23 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_u5b_p_counting_resolution_2026_10_10.md.remote_2026_10_12` | 20,086 | 15 | 2 | F×15 |
| 24 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_u_cf_category_caliber_2026_10_10.md.remote_2026_10_12` | 18,976 | 6 | 8 | F×6 |
| 25 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_u_cf_reclassification_2026_10_10.md.remote_2026_10_12` | 25,698 | 3 | 5 | F×3 |
| 26 | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_vk_current_counting_face_2026_10_10.md.remote_2026_10_12` | 24,795 | 3 | 3 | F×3 |
| 27 | GLM | `_deposon_dualtrack_paper_evidence_pack_selfextract_2026_10_13.py` | 843,497 | 1 | 1 | M×1 |
| 28 | GLM | `_glm_dualtrack_paper_reply_2026_10_13.md` | 72,584 | 2 | 2 | M×2 |
| 29 | GLM | `letters/_glm_dualtrack_paper_reply_2026_10_13.md` | 72,584 | 2 | 2 | C×2 |
| 30 | REPO | `letters/_commission_glm_dualtrack_paper_addendum_v0.2_2026_10_01.md` | 53,344 | 2 | 0 | C×2 |
| 31 | REPO | `letters/_commission_glm_dualtrack_paper_v0.6_2026_10_12.md` | 56,360 | 1 | 0 | C×1 |
| 32 | REPO | `letters/_commission_kimi_supplemental_sync_2026_10_18_draft.md` | 58,843 | 1 | 0 | C×1 |
| 33 | REPO | `letters/_commission_kimi_upload_2026_10_01_v0.2.md` | 35,421 | 1 | 0 | C×1 |
| 34 | REPO | `letters/_supplement_collision_10_overwrite_2026_10_18.md` | 35,436 | 4 | 3 | C×4 |
| 35 | REPO | `letters/_supplement_consolidated_desensitized_upload_2026_10_18.md` | 57,539 | 4 | 5 | C×4 |
| 36 | REPO | `letters/查理_deposon双主线论文终稿_2026-10-01_v0.3.md` | 239,700 | 1 | 0 | C×1 |
| 37 | REPO | `pi_rulings/_pi_card_answers_register_2026_10_18_v100.md` | 40,128 | 2 | 0 | A×1 ＋ AMBIG×1 |
| 38 | REPO | `results/_b0_sixty_items_location_list_2026_10_13.md` | 33,046 | 2 | 0 | A×2 |
| 39 | REPO | `results/_b_tier_five_subitems_draft_2026_10_14.md` | 37,605 | 5 | 3 | A×1 ＋ AMBIG×3 ＋ M×1 |
| 40 | REPO | `results/_d1_backfill_intake_verdict_2026_10_01.md` | 42,115 | 2 | 7 | AMBIG×2 |
| 41 | REPO | `results/_family_de_stale_refresh_matrix_2026_10_14.md` | 78,861 | 108 | 52 | A×1 ＋ AMBIG×23 ＋ M×11 ＋ N×65 ＋ P×5 ＋ Q×3 |
| 42 | REPO | `results/_family_de_stale_refresh_repo_exec_2026_10_14.md` | 31,151 | 5 | 9 | M×4 ＋ N×1 |
| 43 | REPO | `results/_family_de_stale_refresh_sub_exec_2026_10_14.md` | 31,813 | 9 | 5 | M×2 ＋ N×6 ＋ P×1 |
| 44 | REPO | `results/_five_terminal_judgments_ruling_2026_10_10.md` | 27,315 | 7 | 0 | A×6 ＋ AMBIG×1 |
| 45 | REPO | `results/_gate1_glm_reply_integration_register_2026_10_13.md` | 41,753 | 1 | 1 | AMBIG×1 |
| 46 | REPO | `results/_glm_delivery_face_disposition_register_2026_10_13.md` | 16,662 | 1 | 1 | AMBIG×1 |
| 47 | REPO | `results/_glm_evidence_pack_unpack_register_2026_10_13.md` | 28,909 | 1 | 3 | M×1 |
| 48 | REPO | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_t1_gate_closure_and_recompute_verdict_2026_10_01.md` | 72,926 | 2 | 10 | N×1 ＋ Q×1 |
| 49 | REPO | `results/_supplement_execution_receipt_kimi_2026_10_18.md` | 41,236 | 1 | 1 | A×1 |
| 50 | REPO | `results/_t1_substrate_gap_precondition_2026_10_01.md` | 22,196 | 3 | 3 | AMBIG×3 |
| 51 | REPO | `results/_third_batch_card2_and_rename_approval_effect_2026_10_18.md` | 2,274 | 1 | 0 | A×1 |
| 52 | REPO | `results/_thirdparty_16_overwrite_necessity_2026_10_18.md` | 14,122 | 5 | 8 | AMBIG×1 ＋ M×4 |
| 53 | REPO | `results/_thirdparty_16_overwrite_ruling_effect_2026_10_18.md` | 43,428 | 7 | 5 | A×5 ＋ M×1 ＋ N×1 |
| 54 | REPO | `results/_u5_referent_registry_correction_2026_10_12.md` | 25,048 | 3 | 1 | A×3 |
| 55 | REPO | `results/_u5_semantics_resolution_2026_10_12.md` | 24,046 | 5 | 3 | A×5 |
| 56 | REPO | `results/_unclosed_47_direct_clear_b_tier_register_2026_10_13.md` | 31,100 | 3 | 2 | A×2 ＋ AMBIG×1 |
| 57 | REPO | `results/_unclosed_47_direct_clear_register_2026_10_13.md` | 35,560 | 1 | 1 | AMBIG×1 |
| 58 | REPO | `results/_unique_supplement_letter_approval_effect_2026_10_18.md` | 51,238 | 1 | 0 | A×1 |
| 59 | SUB | `results/_b01_new_key_classification_2026_10_10.md` | 38,669 | 14 | 100 | A×4 ＋ M×3 ＋ N×1 ＋ P×6 |
| 60 | SUB | `results/_b01_new_key_residue_judgment_2026_10_10.md` | 41,984 | 7 | 8 | A×7 |
| 61 | SUB | `results/_b01_p_counting_recompute_2026_10_10.md` | 22,104 | 18 | 14 | A×13 ＋ AMBIG×2 ＋ M×1 ＋ P×2 |
| 62 | SUB | `results/_b14_audit_f2f3_closure_register_2026_10_11.md` | 29,620 | 1 | 0 | AMBIG×1 |
| 63 | SUB | `results/_b14_vk_evidence_audit_2026_10_10.md` | 33,586 | 4 | 3 | AMBIG×3 ＋ M×1 |
| 64 | SUB | `results/_backfill_rule_execution_register_2026_10_08.md` | 27,267 | 1 | 0 | AMBIG×1 |
| 65 | SUB | `results/_backfill_rule_final_2026_10_09.md` | 34,602 | 2 | 0 | AMBIG×2 |
| 66 | SUB | `results/_backfill_rule_vk_closeout_2026_10_08.md` | 26,890 | 1 | 0 | AMBIG×1 |
| 67 | SUB | `results/_give_up_n10_erratum_2026_10_10.md` | 22,021 | 1 | 0 | A×1 |
| 68 | SUB | `results/_kd_heteronym_classification_disposition_2026_10_09.md` | 29,761 | 1 | 6 | AMBIG×1 |
| 69 | SUB | `results/_kd_legacy_rewrite_plan_2026_10_10.md` | 17,643 | 12 | 0 | AMBIG×1 ＋ M×1 ＋ N×10 |
| 70 | SUB | `results/_kd_legacy_rewrite_register_2026_10_10.md` | 14,537 | 18 | 0 | M×1 ＋ N×17 |
| 71 | SUB | `results/_kd_legacy_rewrite_ruling_2026_10_10.md` | 13,731 | 10 | 0 | AMBIG×1 ＋ N×9 |
| 72 | SUB | `results/_kd_login_register_section65_correction_2026_10_10.md` | 20,422 | 1 | 1 | M×1 |
| 73 | SUB | `results/_mini_round_5_decisions_register_2026_10_01.md` | 53,125 | 7 | 6 | AMBIG×7 |
| 74 | SUB | `results/_n01_n08_revision_2026_10_10.md` | 26,628 | 1 | 0 | A×1 |
| 75 | SUB | `results/_p_refresh_registration_preliminary_2026_10_10.md` | 32,780 | 14 | 10 | A×12 ＋ M×1 ＋ Q×1 |
| 76 | SUB | `results/_p_refresh_s0_judgment_2026_10_10.md` | 41,449 | 5 | 6 | A×2 ＋ N×2 ＋ Q×1 |
| 77 | SUB | `results/_p_refresh_scope_judgment_2026_10_10.md` | 34,004 | 2 | 3 | AMBIG×1 ＋ P×1 |
| 78 | SUB | `results/_questionnaire_cards_intake_register_supplement_10_2026_10_10.md` | 84,127 | 2 | 0 | P×2 |
| 79 | SUB | `results/_questionnaire_cards_intake_register_supplement_12_2026_10_10.md` | 121,137 | 2 | 4 | A×2 |
| 80 | SUB | `results/_questionnaire_cards_intake_register_supplement_7_2026_10_10.md` | 52,602 | 2 | 2 | A×2 |
| 81 | SUB | `results/_round52_e6b_caliber_naming_effectivity_register_2026_10_10.md` | 21,788 | 1 | 0 | A×1 |
| 82 | SUB | `results/_round56_b01_followup_disposition_plan_2026_10_10.md` | 31,004 | 5 | 5 | A×2 ＋ AMBIG×2 ＋ M×1 |
| 83 | SUB | `results/_round56_pending_questions_compilation_2026_10_10.md` | 33,504 | 1 | 0 | P×1 |
| 84 | SUB | `results/_round56_review_effectivity_register_2026_10_10.md` | 49,013 | 5 | 5 | A×5 |
| 85 | SUB | `results/_round56_review_effectivity_register_3_2026_10_10.md` | 77,181 | 6 | 5 | A×6 |
| 86 | SUB | `results/_round56_review_effectivity_register_4_2026_10_11.md` | 46,908 | 1 | 0 | A×1 |
| 87 | SUB | `results/_round56r8_dispositions_register_2026_10_10.md` | 46,135 | 5 | 4 | A×3 ＋ P×2 |
| 88 | SUB | `results/_t1_7_2_correction_2026_10_08.md` | 16,469 | 2 | 0 | Q×2 |
| 89 | SUB | `results/_t1_gate_closure_and_recompute_verdict_2026_10_01.md` | 72,934 | 2 | 10 | N×1 ＋ Q×1 |
| 90 | SUB | `results/_three_state_standard_repeal_register_2026_10_10.md` | 18,364 | 7 | 1 | A×2 ＋ AMBIG×3 ＋ N×2 |
| 91 | SUB | `results/_u11_execution_register_2026_10_09.md` | 24,549 | 1 | 0 | Q×1 |
| 92 | SUB | `results/_u5_fingerprint_relocation_erratum_2026_10_10.md` | 24,999 | 37 | 11 | A×9 ＋ AMBIG×3 ＋ M×4 ＋ N×9 ＋ P×5 ＋ Q×7 |
| 93 | SUB | `results/_u5b_citation_surface_revision_2026_10_10.md` | 50,079 | 100 | 38 | A×4 ＋ AMBIG×15 ＋ M×17 ＋ N×46 ＋ P×9 ＋ Q×9 |
| 94 | SUB | `results/_u5b_p_counting_resolution_2026_10_10.md` | 20,086 | 15 | 2 | A×2 ＋ AMBIG×1 ＋ M×2 ＋ N×3 ＋ P×7 |
| 95 | SUB | `results/_u_cf_category_caliber_2026_10_10.md` | 18,976 | 6 | 8 | A×6 |
| 96 | SUB | `results/_u_cf_reclassification_2026_10_10.md` | 25,698 | 3 | 5 | A×3 |
| 97 | SUB | `results/_upload_ledger_kimi_2026_10_01.json` | 43,275 | 1 | 0 | D×1 |
| 98 | SUB | `results/_vk_current_counting_face_2026_10_10.md` | 24,795 | 3 | 3 | M×3 |

### A2 刷候选件（M／N 型 · 26 件）

| # | 区 | 载体（rel） | bytes | M | N | 其余留证型 |
|--:|---|---|--:|--:|--:|---|
| 1 | GLM | `_deposon_dualtrack_paper_evidence_pack_selfextract_2026_10_13.py` | 843,497 | 1 | 0 | — |
| 2 | GLM | `_glm_dualtrack_paper_reply_2026_10_13.md` | 72,584 | 2 | 0 | — |
| 3 | REPO | `results/_b_tier_five_subitems_draft_2026_10_14.md` | 37,605 | 1 | 0 | A×1 ＋ AMBIG×3 |
| 4 | REPO | `results/_family_de_stale_refresh_matrix_2026_10_14.md` | 78,861 | 11 | 65 | A×1 ＋ AMBIG×23 ＋ P×5 ＋ Q×3 |
| 5 | REPO | `results/_family_de_stale_refresh_repo_exec_2026_10_14.md` | 31,151 | 4 | 1 | — |
| 6 | REPO | `results/_family_de_stale_refresh_sub_exec_2026_10_14.md` | 31,813 | 2 | 6 | P×1 |
| 7 | REPO | `results/_glm_evidence_pack_unpack_register_2026_10_13.md` | 28,909 | 1 | 0 | — |
| 8 | REPO | `results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_t1_gate_closure_and_recompute_verdict_2026_10_01.md` | 72,926 | 0 | 1 | Q×1 |
| 9 | REPO | `results/_thirdparty_16_overwrite_necessity_2026_10_18.md` | 14,122 | 4 | 0 | AMBIG×1 |
| 10 | REPO | `results/_thirdparty_16_overwrite_ruling_effect_2026_10_18.md` | 43,428 | 1 | 1 | A×5 |
| 11 | SUB | `results/_b01_new_key_classification_2026_10_10.md` | 38,669 | 3 | 1 | A×4 ＋ P×6 |
| 12 | SUB | `results/_b01_p_counting_recompute_2026_10_10.md` | 22,104 | 1 | 0 | A×13 ＋ AMBIG×2 ＋ P×2 |
| 13 | SUB | `results/_b14_vk_evidence_audit_2026_10_10.md` | 33,586 | 1 | 0 | AMBIG×3 |
| 14 | SUB | `results/_kd_legacy_rewrite_plan_2026_10_10.md` | 17,643 | 1 | 10 | AMBIG×1 |
| 15 | SUB | `results/_kd_legacy_rewrite_register_2026_10_10.md` | 14,537 | 1 | 17 | — |
| 16 | SUB | `results/_kd_legacy_rewrite_ruling_2026_10_10.md` | 13,731 | 0 | 9 | AMBIG×1 |
| 17 | SUB | `results/_kd_login_register_section65_correction_2026_10_10.md` | 20,422 | 1 | 0 | — |
| 18 | SUB | `results/_p_refresh_registration_preliminary_2026_10_10.md` | 32,780 | 1 | 0 | A×12 ＋ Q×1 |
| 19 | SUB | `results/_p_refresh_s0_judgment_2026_10_10.md` | 41,449 | 0 | 2 | A×2 ＋ Q×1 |
| 20 | SUB | `results/_round56_b01_followup_disposition_plan_2026_10_10.md` | 31,004 | 1 | 0 | A×2 ＋ AMBIG×2 |
| 21 | SUB | `results/_t1_gate_closure_and_recompute_verdict_2026_10_01.md` | 72,934 | 0 | 1 | Q×1 |
| 22 | SUB | `results/_three_state_standard_repeal_register_2026_10_10.md` | 18,364 | 0 | 2 | A×2 ＋ AMBIG×3 |
| 23 | SUB | `results/_u5_fingerprint_relocation_erratum_2026_10_10.md` | 24,999 | 4 | 9 | A×9 ＋ AMBIG×3 ＋ P×5 ＋ Q×7 |
| 24 | SUB | `results/_u5b_citation_surface_revision_2026_10_10.md` | 50,079 | 17 | 46 | A×4 ＋ AMBIG×15 ＋ P×9 ＋ Q×9 |
| 25 | SUB | `results/_u5b_p_counting_resolution_2026_10_10.md` | 20,086 | 2 | 3 | A×2 ＋ AMBIG×1 ＋ P×7 |
| 26 | SUB | `results/_vk_current_counting_face_2026_10_10.md` | 24,795 | 3 | 0 | — |

### A3 区级排除件（F／C／D · 35 件）

| 区级 | 区 | 载体（rel） | bytes | 旧值处 | 面之定性 |
|---|---|---|--:|--:|---|
| C | ARCHIVE | `letters_archive_2026_10_01/_commission_glm_dualtrack_paper_addendum_2026_10_01.md` | 35,892 | 1 | 归档对外稿 |
| C | ARCHIVE | `letters_archive_2026_10_01/_commission_kimi_upload_2026_10_01.md` | 29,880 | 1 | 归档对外稿 |
| C | GLM | `letters/_glm_dualtrack_paper_reply_2026_10_13.md` | 72,584 | 2 | 对外稿面 (letters) |
| C | REPO | `letters/_commission_glm_dualtrack_paper_addendum_v0.2_2026_10_01.md` | 53,344 | 2 | 对外稿面 (letters) |
| C | REPO | `letters/_commission_glm_dualtrack_paper_v0.6_2026_10_12.md` | 56,360 | 1 | 对外稿面 (letters) |
| C | REPO | `letters/_commission_kimi_supplemental_sync_2026_10_18_draft.md` | 58,843 | 1 | 对外稿面 (letters) |
| C | REPO | `letters/_commission_kimi_upload_2026_10_01_v0.2.md` | 35,421 | 1 | 对外稿面 (letters) |
| C | REPO | `letters/_supplement_collision_10_overwrite_2026_10_18.md` | 35,436 | 4 | 对外稿面 (letters) |
| C | REPO | `letters/_supplement_consolidated_desensitized_upload_2026_10_18.md` | 57,539 | 4 | 对外稿面 (letters) |
| C | REPO | `letters/查理_deposon双主线论文终稿_2026-10-01_v0.3.md` | 239,700 | 1 | 对外稿面 (letters) |
| D | SUB | `results/_upload_ledger_kimi_2026_10_01.json` | 43,275 | 1 | 机器台账/JSON 记录面 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_b01_new_key_classification_2026_10_10.md.remote_2026_10_12` | 38,669 | 14 | 10-12 远端冻结件·历史存照 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_b01_new_key_residue_judgment_2026_10_10.md.remote_2026_10_12` | 41,984 | 7 | 10-12 远端冻结件·历史存照 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_b01_p_counting_recompute_2026_10_10.md.remote_2026_10_12` | 22,104 | 18 | 10-12 远端冻结件·历史存照 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_b14_audit_f2f3_closure_register_2026_10_11.md.remote_2026_10_12` | 29,620 | 1 | 10-12 远端冻结件·历史存照 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_b14_vk_evidence_audit_2026_10_10.md.remote_2026_10_12` | 33,586 | 4 | 10-12 远端冻结件·历史存照 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_d1_backfill_intake_verdict_2026_10_01.md.remote_2026_10_12` | 42,106 | 9 | 10-12 远端冻结件·历史存照 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_mini_round_5_decisions_register_2026_10_01.md.remote_2026_10_12` | 53,131 | 13 | 10-12 远端冻结件·历史存照 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_p_refresh_registration_preliminary_2026_10_10.md.remote_2026_10_12` | 32,780 | 14 | 10-12 远端冻结件·历史存照 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_p_refresh_s0_judgment_2026_10_10.md.remote_2026_10_12` | 41,449 | 5 | 10-12 远端冻结件·历史存照 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_p_refresh_scope_judgment_2026_10_10.md.remote_2026_10_12` | 34,004 | 2 | 10-12 远端冻结件·历史存照 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_questionnaire_cards_intake_register_supplement_10_2026_10_10.md.remote_2026_10_12` | 84,127 | 2 | 10-12 远端冻结件·历史存照 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_questionnaire_cards_intake_register_supplement_12_2026_10_10.md.remote_2026_10_12` | 121,137 | 2 | 10-12 远端冻结件·历史存照 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_questionnaire_cards_intake_register_supplement_7_2026_10_10.md.remote_2026_10_12` | 52,602 | 2 | 10-12 远端冻结件·历史存照 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_round56_b01_followup_disposition_plan_2026_10_10.md.remote_2026_10_12` | 31,004 | 5 | 10-12 远端冻结件·历史存照 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_round56_pending_questions_compilation_2026_10_10.md.remote_2026_10_12` | 33,504 | 1 | 10-12 远端冻结件·历史存照 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_round56_review_effectivity_register_2026_10_10.md.remote_2026_10_12` | 49,013 | 5 | 10-12 远端冻结件·历史存照 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_round56_review_effectivity_register_3_2026_10_10.md.remote_2026_10_12` | 77,181 | 6 | 10-12 远端冻结件·历史存照 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_round56_review_effectivity_register_4_2026_10_11.md.remote_2026_10_12` | 46,908 | 1 | 10-12 远端冻结件·历史存照 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_round56r8_dispositions_register_2026_10_10.md.remote_2026_10_12` | 46,135 | 5 | 10-12 远端冻结件·历史存照 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_t1_gate_closure_and_recompute_verdict_2026_10_01.md.remote_2026_10_12` | 72,951 | 12 | 10-12 远端冻结件·历史存照 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_u5b_p_counting_resolution_2026_10_10.md.remote_2026_10_12` | 20,086 | 15 | 10-12 远端冻结件·历史存照 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_u_cf_category_caliber_2026_10_10.md.remote_2026_10_12` | 18,976 | 6 | 10-12 远端冻结件·历史存照 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_u_cf_reclassification_2026_10_10.md.remote_2026_10_12` | 25,698 | 3 | 10-12 远端冻结件·历史存照 |
| F | ARCHIVE | `results/_remote_version_freeze_2026_10_12/_vk_current_counting_face_2026_10_10.md.remote_2026_10_12` | 24,795 | 3 | 10-12 远端冻结件·历史存照 |

### A4 零信号命中件（AMBIG · 27 件）

| # | 区 | 载体（rel） | 旧值处 | AMBIG 处 |
|--:|---|---|--:|--:|
| 1 | REPO | `pi_rulings/_pi_card_answers_register_2026_10_18_v100.md` | 2 | 1 |
| 2 | REPO | `results/_b_tier_five_subitems_draft_2026_10_14.md` | 5 | 3 |
| 3 | REPO | `results/_d1_backfill_intake_verdict_2026_10_01.md` | 2 | 2 |
| 4 | REPO | `results/_family_de_stale_refresh_matrix_2026_10_14.md` | 108 | 23 |
| 5 | REPO | `results/_five_terminal_judgments_ruling_2026_10_10.md` | 7 | 1 |
| 6 | REPO | `results/_gate1_glm_reply_integration_register_2026_10_13.md` | 1 | 1 |
| 7 | REPO | `results/_glm_delivery_face_disposition_register_2026_10_13.md` | 1 | 1 |
| 8 | REPO | `results/_t1_substrate_gap_precondition_2026_10_01.md` | 3 | 3 |
| 9 | REPO | `results/_thirdparty_16_overwrite_necessity_2026_10_18.md` | 5 | 1 |
| 10 | REPO | `results/_unclosed_47_direct_clear_b_tier_register_2026_10_13.md` | 3 | 1 |
| 11 | REPO | `results/_unclosed_47_direct_clear_register_2026_10_13.md` | 1 | 1 |
| 12 | SUB | `results/_b01_p_counting_recompute_2026_10_10.md` | 18 | 2 |
| 13 | SUB | `results/_b14_audit_f2f3_closure_register_2026_10_11.md` | 1 | 1 |
| 14 | SUB | `results/_b14_vk_evidence_audit_2026_10_10.md` | 4 | 3 |
| 15 | SUB | `results/_backfill_rule_execution_register_2026_10_08.md` | 1 | 1 |
| 16 | SUB | `results/_backfill_rule_final_2026_10_09.md` | 2 | 2 |
| 17 | SUB | `results/_backfill_rule_vk_closeout_2026_10_08.md` | 1 | 1 |
| 18 | SUB | `results/_kd_heteronym_classification_disposition_2026_10_09.md` | 1 | 1 |
| 19 | SUB | `results/_kd_legacy_rewrite_plan_2026_10_10.md` | 12 | 1 |
| 20 | SUB | `results/_kd_legacy_rewrite_ruling_2026_10_10.md` | 10 | 1 |
| 21 | SUB | `results/_mini_round_5_decisions_register_2026_10_01.md` | 7 | 7 |
| 22 | SUB | `results/_p_refresh_scope_judgment_2026_10_10.md` | 2 | 1 |
| 23 | SUB | `results/_round56_b01_followup_disposition_plan_2026_10_10.md` | 5 | 2 |
| 24 | SUB | `results/_three_state_standard_repeal_register_2026_10_10.md` | 7 | 3 |
| 25 | SUB | `results/_u5_fingerprint_relocation_erratum_2026_10_10.md` | 37 | 3 |
| 26 | SUB | `results/_u5b_citation_surface_revision_2026_10_10.md` | 100 | 15 |
| 27 | SUB | `results/_u5b_p_counting_resolution_2026_10_10.md` | 15 | 1 |


---

*设计面完毕 ｜ 字节级自报见落盘后独立亲测 ｜ **裁归 PI**（📋 候 PI 复核生效 · 生效即锁 · ⛔ 0 执行）*
