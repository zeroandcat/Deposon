# 659 交叠之逐件语义判读（#5 族 hash 桶交叠·编号面收口）

> **状态：草案·候 PI 核准。** 本件之全部数值、判定、建议**一律未生效**；⛔ 0 宣告①毕、⛔ 0 宣告任何项「已闭」（含 KD-G 之闭，闭须 PI 裁）、⛔ 0 代 PI 释义／择定／给值、⛔ 0 径行采认本件任何结论。
>
> **并立声明**：本件**另立并列**，⛔ **0 回改** `26b708beb153`／`7953a89ea015`／`47f20fa27a62`／`be92eddb4034`／`956d19e4e670` 任何一字；五件原样在盘，本件为**旁挂判读件**。
>
> **⛔ 本件⛔ 0 直接采信**源件之任何转引值：§1 之 659／68／132／101／656·3 之构成，均由本棒以三通道独立复算得出。

**棒别**：659 交叠逐件语义判读棒（PI 2026-10-14 派工；承族计数补正件 KD-G 之「需派独立人工判读棒」）  
**署名**：`evidence-auditor`（⛔ 0 用 KIMI／GLM／coze／Trae／鲍勃 名头）

---

## §1 方法与源件回读

### §1-1 三源件之逐字回读与元数据实测（本棒逐件实测·⛔ 0 沿用派工单转引值）

| 件（`results/`） | 派工单所载 SHA-12／bytes | 本棒实测 SHA-12 | 本棒实测 bytes | 判定 |
|---|---|---|---:|---|
| `_numbering_family_count_erratum_2026_10_13.md` | `26b708beb153`／15,557 | **`26b708beb153`** | 15,557 | **MATCH** |
| `_numbering_family_count_corrigendum_2026_10_14.md` | `9baf2ea2e9cb`／19,812 | **`9baf2ea2e9cb`** | 19,812 | **MATCH** |
| `_numbering_hash_bucket_criterion_design_2026_10_14.md` | `be92eddb4034`／21,733 | **`be92eddb4034`** | 21,733 | **MATCH** |

哈希算法：`hashlib.sha256`（⛔ 0 使用内建 `hash()`）。**三源件与派工单逐字一致，无元数据偏差。**

### §1-2 逐字回读位点与所得

| 源件 | 位点 | 本棒回读所得（以此为准） |
|---|---:|---|
| `_numbering_family_count_corrigendum_2026_10_14.md` | `:98` | 交叠表第 5 族行：B＝**659**／C＝**659**／交叠件 **101**／归桶后净数 **9,527** |
| `_numbering_family_count_corrigendum_2026_10_14.md` | `:146`–`:153` | 659 之构成：命中 659／不同 `D` 字面 68／不同 run 132／触及件 101／12 位＝656、16 位＝3 |
| `_numbering_family_count_corrigendum_2026_10_14.md` | `:151` | 16 位之 3 项全为 `D30EDA5A1063F9AD`，位于 `_v5_fake_verdict_session_log_2026_09_28.md` `:28`／`:37` |
| `_numbering_family_count_corrigendum_2026_10_14.md` | `:153` | **KD-G 诚实交代**：「659 是否 100% 为真指纹」登记为未闭，⛔ 0 逐件人工语义判读（超该棒射程） |
| `_numbering_family_count_corrigendum_2026_10_14.md` | `:252` | KD-G 条目全文：**部分肯定·未闭**，⛔ 0 逐件判读，**不阻断** #5 之 9,466 |
| `_numbering_family_count_corrigendum_2026_10_14.md` | `:126`–`:127` | 交叠 **659**；修正后 #5 计数 **9,466**（−659，−6.51%） |
| `_numbering_hash_bucket_criterion_design_2026_10_14.md` | `:65` | `:338` 原判准逐字：命中向右延展为 `[A-Za-z0-9_\-]+` 之完整 run，若 `len(run) ≥ 12` 且全为十六进制字符 ⇒ 判为指纹串 |
| `_numbering_hash_bucket_criterion_design_2026_10_14.md` | `:210`、`:234` | 交叠 659、其中 **⛔ 0 逐件人工判读 659 项**（KD-E） |
| `_numbering_family_count_erratum_2026_10_13.md` | `:62` | 第 5 族行：`8,786`／`10,186`／`61`／**`10,125`**／`0.60%` |
| `_numbering_family_count_erratum_2026_10_13.md` | `:26`、`:35` | 12 区主测范围、复跑正则、8 扩展名 |

### §1-3 测量仪器（本棒口径·逐字取自上二件，未改一字）

| 项 | 本棒取值 | 实测 |
|---|---|---|
| 遍历 | Python 3.14 `os.walk`，`onerror` **捕获并计数全部遍历错误**，`followlinks=False`；⛔ 0 以 PowerShell `-Recurse`＋`SilentlyContinue` 作数 | 遍历错误 **0**（口径 B）／**0**（口径 C） |
| 主测范围 | 12 区（`results`／`letters`／`docs`／`corpus`／`paper`／`scripts`／`tools`／`tests`／`verifier`／`reviews`／`attacks`／`deposon_team`） | 口径 B **1319** 件／口径 C **1339** 件 |
| as-of 截止 | `mtime ≤` 勘正件 mtime ＝ `2026-10-13 23:36:15` | 同 |
| 剔除 | 勘正件自身 ＋ F5 专项件 `_compound_numbering_census_2026_10_13.md`（防自证循环） | 已剔 2 件 |
| `.tmp` 临时件 | 计数面剪枝（12 区内实测 `.tmp` 目录 **0** 处） | 同 |
| 禁触区 | `dirnames` 剪枝名含 `〔归档区〕` 者，剪枝在进入该枝前生效；仓内命中 **0** 处 ⇒ 0 读 0 写 0 列目录 | 同 |
| `.env` | 文件名以 `.env` 起者跳过，⛔ **0 读** | 同 |
| 解码 | `io.open(p,'rb')` → `decode('utf-8-sig', errors='strict')` | 解码失败 **0** |
| 复跑正则 | `(?<![A-Za-z0-9_])([A-Z]{1,4}-?\d{1,3})(?![0-9])` | ⛔ 0 改一字 |
| 桶判准 | `run = tok + 右延展[A-Za-z0-9_\-]+`；`len(run) ≥ 12` 且全十六进制 ⇒ 入桶 | ⛔ 0 改一字 |
| 检索根 | 12 区 ＋ 运行时附件面（`.tmp`／`.mavis`／`.trae`／`.vscode`） | 附件面遍历错误 **0**；见 §1-6 |

### §1-4 双通道（实为三通道）复算与一致性

| 通道 | 机制（互不共用代码路径） | 口径 B | 口径 C |
|---|---|---:|---:|
| **A** | `RX.finditer` 逐命中 ＋ 右延展（`:338` 之直接形式化） | **659** | **659** |
| **B** | 极大 `[A-Za-z0-9_\-]+` run 枚举 ＋ 哨兵包围下局部重匹配 | **659** | **659** |
| **C** | **字节层**正则（⛔ 不经 `str` 解码 ⇒ 独立于解码口径） | **659** | **659** |
| **合计** | | **659** | **659** |

| 一致性检验 | 结果 |
|---|---|
| 逐件键集不符之件（通道间） | **0** |
| 口径 B 与 C **逐处**同集（`rel,off,tok,run` 四元组） | **是** |

⇒ **三通道独立复算皆得 659，通道间逐件键集 0 不符，两种扩展名口径逐处同集。本棒独立确认源件之 659 为可复现之精确值。**

### §1-5 与源件 §2-3 构成之逐项对照

| 维度 | 源件 `:146`–`:151` 所载 | 本棒实测 | 判定 |
|---|---:|---:|---|
| 命中总数 | 659 | **659** | **MATCH** |
| 不同 `D` 字面 | 68 | **68** | **MATCH** |
| 不同 run | 132 | **132** | **MATCH** |
| 触及件数 | 101 | **101** | **MATCH** |
| run 长度 12 位 | 656 | **656** | **MATCH** |
| run 长度 16 位 | 3 | **3** | **MATCH** |

⇒ **六项逐项吻合。**

### §1-6 检索根含运行时附件面（实测·⛔ 不计入 659）

| 面 | 同形命中 | 说明 |
|---|---:|---|
| `.tmp`（含本棒自产 6 件摘要件） | **3,765** | 其中 **2,627 为本棒自产摘要件之自匹配**（仪器缺陷，见 §1-7 之 E-4） |
| `.mavis`／`.trae`／`.vscode` | **0** | 无同形命中 |
| 既有件（剔除本棒自产） | **140** | 全在 `.tmp`（`r461_layers.json` 132 ＋ 余 8）；**按规则 `.tmp` 已剪枝，故全不计入 659** |

> 📌 如实登记以免下游误读：**659 ⛔ 非「全仓 D-十六进制串之全集」**，乃 **12 区计数面（剔除 `.tmp`）之同形命中数**。

### §1-7 扫描器自审（测量仪器自身即误差源）

本棒对**自身仪器**发生 **5 处**缺陷／假象，均如实登记；处置一律为**修仪器、不修数、不修文本**。

| # | 仪器缺陷／假象 | 现象 | 危害 | 处置 |
|---:|---|---|---|---|
| **E-1** | 口径 C 之逐处表初版**未建**（仅计总数） | 首跑 `BC_identical=false` | 🔴 高：**若据首跑之 `false` 断言「B／C 不同集」，即为一处假阳性** | 改仪器（两口径同建逐处表）后复测 ⇒ **`true`**。**数未动一字** |
| **E-2** | SHA-256 单算法注册表对撞（首版） | 132 run 中 96 判为「无在盘件可对撞」，一度疑其**非指纹** | 中 | 补入 **SHA-1** 注册表（本链已知 SHA-1 口径误用）＋ 逐处读原文；确认为「在盘件已移出」而非「非指纹」 |
| **E-3** | 紧凑摘要件以 `pre + run + post` 拼接，**run 尾部被重复渲染** | 一度疑 `_upload_plan_2026_10_12.json`／`_r2_build_manifest_2026_10_12.json` 之 `sha12` 字段**字长 22 之畸形** | 🔴 中：**若未验即登记，将向 PI 虚报一处不存在的资产缺陷** | 实测该二件 `sha12` 类字段 830 ＋ 948 处**全为 12 字长** ⇒ **该疑点被否证，不登记为资产缺陷** |
| **E-4** | 附件面扫描**含本棒自产摘要件** | 附件面命中虚高至 3,765 | 中 | 已在 §1-6 **分列自产／既有**；既有件仅 140 处 |
| **E-5** | 首版本件落盘后**字节级自检**实测 CTRL＝1 | 源件 `_v3_v4_achievements_inventory_2026_09_24.md:1911` 之裸 BEL(0x07) 随上下文**逐字**进入本件第 391 行 | 中：**逐字保真与 CTRL＝0 之硬约束相冲** | 改渲染层（控制字节→**可见转义** `\x07`，保信息不丢）后重渲染**本棒自身首版产物**（⛔ 非覆盖他棒之件），复测 CTRL＝**0**；源件 ⛔ 0 触碰，另立 KD-O |

> 📌 **纪律推广建议**（承 `_numbering_family_count_erratum_2026_10_13.md` §1-5 之 E-1 同族）：**「对撞失败」⛔ 0 直接读作「非目标类」**——须先穷举候选算法（SHA-256／SHA-1／MD5）与「目标物已移出」之可能，再作定性；**「疑点」⛔ 0 未验即登记为缺陷**。本棒 E-2／E-3 即此族之二例。

---

## §2 逐处判读表（共 659 处·逐处给判定与依据）

**逐处判读之法（非关键词启发式批量归类）**：本棒**逐处**枚举 659 之每一处，取其**自身原文上下文**（前 42 字 ⏎ run ⏎ 后 46 字）逐处读定；并以**该处 run 之注册表对撞**（全仓在盘件之 SHA-256／SHA-1 前缀实测）作独立佐证。

> ⛔ **本表非启发式归类**：本链已有「启发式误纳致族计数虚增」之实证（`_numbering_family_count_corrigendum_2026_10_14.md` §3-1）。故本棒之判读**不采任何关键词规则**代作判词；关键词／路径标记扫描**仅用作完备性反查**（§2-2），不作定性依据。

**判定码**：`F256` 真哈希指纹（SHA-256 前缀，在盘实测对撞命中）｜`F1` 真哈希指纹（SHA-1 前缀，在盘实测对撞命中）｜`F12` 真哈希指纹（SHA-12 语义，所指件已不在盘，在盘不可对撞；由该处上下文之哈希列语义定）。**三者皆 ⛔ 非 D 族。**

**依据码**：`E1` run 经实测复算命中在盘件 SHA-256 前缀｜`E2` run 经实测复算命中在盘件 SHA-1 前缀｜`E3` run 无在盘件可对撞；逐处读原文，其上下文为 SHA-12 哈希列。

| # | 件（repo 相对路径） | 行 | 列 | tok | run（长） | 上下文（前 42 ⏎ run ⏎ 后 46） | 判定 | 判定码 | 依据 |
|---:|---|---:|---:|---|---|---|---|---|---|
| 1 | `deposon_team/plugins/_v4_wt_apply_b4_2026_09_27.py` | 65 | 117 | `D9` | `D9E14ED29FB9`（12） | ss_pa_1_rbr_rm_result_2026_09_15.json'：记 ' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9' = SHA-1，实 SHA-256 = 'C7C59E0D2F6C' | **非 D 族（哈希指纹）** | `F1` | E2 |
| 2 | `deposon_team/plugins/_v4_wt_s3_b2probe_2026_09_27.py` | 14 | 89 | `D9` | `D9E14ED29FB9`（12） | 26_09_15.json',                          ' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9', 8753),\\n ('1-r',   'deposon_team/ | **非 D 族（哈希指纹）** | `F1` | E2 |
| 3 | `deposon_team/plugins/_v4_wt_s3_b2probe_2026_09_27.py` | 68 | 62 | `D9` | `D9E14ED29FB9`（12） | oss_pa_1_rbr_rm_result_2026_09_15.json', ' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9'),\\n ('#4',  'results/boss_pa_3_rep | **非 D 族（哈希指纹）** | `F1` | E2 |
| 4 | `deposon_team/plugins/_v4_wt_s3b_b2confirm_2026_09_27.py` | 8 | 89 | `D9` | `D9E14ED29FB9`（12） | 26_09_15.json',                          ' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9'),\\n ('1-r',   'deposon_team/plugin | **非 D 族（哈希指纹）** | `F1` | E2 |
| 5 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 16 | 85 | `D1` | `D1EE21F3F6AE`（12） | nifest_2026_09_21.json'（291,551 B，SHA-12 ' ⏎ `D1EE21F3F6AE` ⏎ EE21F3F6AE'，含 UTF-8 BOM）——363 条记录，字段 'src / ds | **非 D 族（哈希指纹）** | `F12` | E3 |
| 6 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 26 | 94 | `D6` | `D6F233D73C45`（12） | 6_09_15.json' \| 'deposon-sub/results/' \| ' ⏎ `D6F233D73C45` ⏎ F233D73C45' \| 9,098 \|\\n\| 'results/boss_pc_1_a1 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 7 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 31 | 79 | `D74` | `D74D6B39D1B0`（12） | 6_09_15.json' \| 'deposon-sub/results/' \| ' ⏎ `D74D6B39D1B0` ⏎ D6B39D1B0' \| 1,265 \|\\n\| 'results/boss_pc_3_rea | **非 D 族（哈希指纹）** | `F256` | E1 |
| 8 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 34 | 139 | `D74` | `D74D6B39D1B0`（12） | 节相同） \| 'D21912A05D79' / '5A880678C386' / ' ⏎ `D74D6B39D1B0` ⏎ D6B39D1B0' \| — \|\\n\| 'results/d7_5anchor_60cell | **非 D 族（哈希指纹）** | `F256` | E1 |
| 9 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 54 | 54 | `D74` | `D74D6B39D1B0`（12） | c_a3_clipping' ≡ 'boss_pc_3_a3_clipping'（' ⏎ `D74D6B39D1B0` ⏎ D6B39D1B0'）\\n- 'boss_pc_1_real_2d_ising' ≡ 'bo | **非 D 族（哈希指纹）** | `F256` | E1 |
| 10 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 106 | 437 | `D3` | `D3F376A6C45F`（12） |  '_v4_exec_s40_rejudged_2026_09_23.json' ' ⏎ `D3F376A6C45F` ⏎ F376A6C45F'；补正件 '065E57820C36'。**parent 复审通过** | **非 D 族（哈希指纹）** | `F12` | E3 |
| 11 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 107 | 74 | `D279` | `D279EBDE5E84`（12） | ）** \| 任务 B v1 判定 '_v4_pi_cot_verdict.md' ' ⏎ `D279EBDE5E84` ⏎ EBDE5E84'「FAIL，根因=命题层面被证伪（真证伪）」 \| PI 点破（2026-0 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 12 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 209 | 57 | `D64` | `D64E1264737F`（12） | lts/_v4_n22s_margin_verdict.md'（盘 SHA-12 ' ⏎ `D64E1264737F` ⏎ E1264737F'）+ 'results/_v4_exec_n22s_margin_res | **非 D 族（哈希指纹）** | `F12` | E3 |
| 13 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 451 | 43 | `D64` | `D64E1264737F`（12） | \| 'results/_v4_n22s_margin_verdict.md' \| ' ⏎ `D64E1264737F` ⏎ E1264737F' \| 11,027 \|\\n\| 'results/_v4_exec_n22 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 14 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 788 | 69 | `D0` | `D0B64D1AB8B7`（12） | 20_pre_hashes_v4frozen_2026_09_24.txt' \| ' ⏎ `D0B64D1AB8B7` ⏎ B64D1AB8B7' \| 1,960 \|\\n\| 'results/_v4_supp_l8_ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 15 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 792 | 59 | `D999` | `D999A43D521F`（12） | upp_l8_n12r_pre_hashes_2026_09_24.txt' \| ' ⏎ `D999A43D521F` ⏎ A43D521F' \| 29,820 \|\\n\| 'results/_v4_supp_l8_n | **非 D 族（哈希指纹）** | `F12` | E3 |
| 16 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 1088 | 74 | `D999` | `D999A43D521F`（12） | _pre_hashes_2026_09_24.txt' \| 320 \| 同上 \| ' ⏎ `D999A43D521F` ⏎ A43D521F' \| 29,820 \|\\n\| 4 \| 'results/_v4_supp_ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 17 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 1304 | 53 | `D6` | `D6CB03A4657E`（12） | **T1 verdict / result 锚标错** \| 链 record 标 ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' 为「T1 verdict 锚」，但盘实测 'D6CB03A4657E | **非 D 族（哈希指纹）** | `F256` | E1 |
| 18 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 1304 | 89 | `D6` | `D6CB03A4657E`（12） | rd 标 'D6CB03A4657E' 为「T1 verdict 锚」，但盘实测 ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' 实为 'results/_v4_supp_t1_result.jso | **非 D 族（哈希指纹）** | `F256` | E1 |
| 19 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 1350 | 40 | `D6` | `D6CB03A4657E`（12） | \|\\n\| 'results/_v4_supp_t1_result.json' \| ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' \| 链 record 误标为 verdict 锚（实为 result | **非 D 族（哈希指纹）** | `F256` | E1 |
| 20 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 1468 | 73 | `D6` | `D6CB03A4657E`（12） | _supp_t1_result.json' (82,365 B / SHA-12=' ⏎ `D6CB03A4657E` ⏎ CB03A4657E') \| 'D6CB03A4657E' \| 82,365 \| t1_re | **非 D 族（哈希指纹）** | `F256` | E1 |
| 21 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 1468 | 91 | `D6` | `D6CB03A4657E`（12） | on' (82,365 B / SHA-12='D6CB03A4657E') \| ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' \| 82,365 \| t1_result.json ✓ \|\\n\| L | **非 D 族（哈希指纹）** | `F256` | E1 |
| 22 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 1476 | 4 | `D6` | `D6CB03A4657E`（12） | ts/_v4_supp_t1_verdict.md' \| 27,538 \|\\n\| ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' ✓ \| T1 result = 'results/_v4_supp_ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 23 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 1483 | 152 | `D6` | `D6CB03A4657E`（12） | **标签互换**：实情是 F1B5E49F3058 = t1_verdict.md， ⏎ `D6CB03A4657E` ⏎ CB03A4657E = t1_result.json，但 v3 棒反写为「D6CB03A4 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 24 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 1483 | 192 | `D6` | `D6CB03A4657E`（12） | d，D6CB03A4657E = t1_result.json，但 v3 棒反写为「 ⏎ `D6CB03A4657E` ⏎ CB03A4657E = T1 verdict 锚 / F1B5E49F3058 = T1. | **非 D 族（哈希指纹）** | `F256` | E1 |
| 25 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 1484 | 42 | `D6` | `D6CB03A4657E`（12） | n- **t1_verdict.md 自报 SHA 表（L13-18）字面自洽**（ ⏎ `D6CB03A4657E` ⏎ CB03A4657E = result / 802DECE2286A = add_T1 /  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 26 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 1513 | 40 | `D6` | `D6CB03A4657E`（12） | \|\\n\| 'results/_v4_supp_t1_result.json' \| ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' \| T1 result（82,365 B；cleanup v3 棒字 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 27 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 1538 | 130 | `D6` | `D6CB03A4657E`（12） | C1E' / '6F3F6FA3AB1D' / 'F1B5E49F3058' / ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' / '802DECE2286A' / '79936B630015'  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 28 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 1550 | 96 | `D6` | `D6CB03A4657E`（12） | ）+ 正确映射字面追加（F1B5E49F3058 = T1 verdict ✓ /  ⏎ `D6CB03A4657E` ⏎ CB03A4657E = T1 result ✓ / 802DECE2286A = add_ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 29 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 1605 | 118 | `D6` | `D6CB03A4657E`（12） | 38 B）+ 'results/_v4_supp_t1_result.json' ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E'（82,365 B）+ 'results/_v4_supp_t1_ex | **非 D 族（哈希指纹）** | `F256` | E1 |
| 30 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 1681 | 40 | `D6` | `D6CB03A4657E`（12） | \|\\n\| 'results/_v4_supp_t1_result.json' \| ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E'（82,365 B） \| E-34.3 T1 result 锚 \|\\n | **非 D 族（哈希指纹）** | `F256` | E1 |
| 31 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 1718 | 113 | `D6` | `D6CB03A4657E`（12） | 571' / 'F4435801D09F' / 'F1B5E49F3058' / ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' / '802DECE2286A' / '8355724A26E3'  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 32 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 2629 | 67 | `D96` | `D96B747BFC6C`（12） | v2_dataset_addendum_d3b_2026_09_26.json'（' ⏎ `D96B747BFC6C` ⏎ B747BFC6C'，14,722 B，本棒实测 ✓）honesty_note 字面 = w | **非 D 族（哈希指纹）** | `F256` | E1 |
| 33 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 2661 | 80 | `D96` | `D96B747BFC6C`（12） | ndum_d3b_2026_09_26.json' honesty_note \| ' ⏎ `D96B747BFC6C` ⏎ B747BFC6C'（14,722 B，本棒实测 ✓） \| E-41.4 wave2 8/3 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 34 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 2678 | 366 | `D96` | `D96B747BFC6C`（12） | erifier 呈文结论 + '5D79E67A4E9D' §4.1 / d3b ' ⏎ `D96B747BFC6C` ⏎ B747BFC6C' / d3c '401BD614CDF7' 字面，v23→v24 增量  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 35 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 2690 | 116 | `D96` | `D96B747BFC6C`（12） | B0F' / '41D29F4DEB70' / '5D79E67A4E9D' / ' ⏎ `D96B747BFC6C` ⏎ B747BFC6C' / '401BD614CDF7'）**全部只读核验、未触动**；前 3 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 36 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 2706 | 147 | `D96` | `D96B747BFC6C`（12） | B0F' / '41D29F4DEB70' / '5D79E67A4E9D' / ' ⏎ `D96B747BFC6C` ⏎ B747BFC6C' / '401BD614CDF7'）+ verdict_v3 §2.4  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 37 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 3533 | 41 | `D9` | `D9E14ED29FB9`（12） | \\n\| **γ5** \| 预登记 v1 §0.2 三处 SHA-12 与盘上不符（' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9'/'c7c59e0d2f6c'｜'425507bb555b'/'f33 | **非 D 族（哈希指纹）** | `F1` | E2 |
| 38 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 3538 | 24 | `D6` | `D6C8BC163E11`（12） | 40.1 五处并列注记处置 \|\\n\\n- **本棒 0 改动面**：#5 三件套 ' ⏎ `D6C8BC163E11` ⏎ C8BC163E11'（executor 38,639 B）/ 'F63B36B75A51' | **非 D 族（哈希指纹）** | `F12` | E3 |
| 39 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 3629 | 56 | `D6` | `D6C8BC163E11`（12） | 3_recheck_05_executor_2026_09_28.py' \| **' ⏎ `D6C8BC163E11` ⏎ C8BC163E11'** \| 38,639 \| #5 executor（**0 改动**） | **非 D 族（哈希指纹）** | `F12` | E3 |
| 40 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 3653 | 508 | `D6` | `D6C8BC163E11`（12） | ；字面源 = '88B7EAF8675D' + 'F63B36B75A51' + ' ⏎ `D6C8BC163E11` ⏎ C8BC163E11' + '9708E7EF1F8C' + 'AE154971D1D2'  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 41 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 3664 | 97 | `D6` | `D6C8BC163E11`（12） | F8C'（**本体 0 改 = 登记式更新**）＋ **0 改** #5 三件套（' ⏎ `D6C8BC163E11` ⏎ C8BC163E11' / 'F63B36B75A51' / '88B7EAF8675D'， | **非 D 族（哈希指纹）** | `F12` | E3 |
| 42 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 3753 | 142 | `D4` | `D4DD5C949443`（12） | l14v3_batch10_r1_executor.py'（56,894 B / ' ⏎ `D4DD5C949443` ⏎ DD5C949443'）为单件逻辑链（本棒逐行复核 ✓）：\\n\\n  '''\\n  L355 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 43 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 3786 | 50 | `D96` | `D96B747BFC6C`（12） | dendum_d3b_2026_09_26.json' \| 14,722 \| **' ⏎ `D96B747BFC6C` ⏎ B747BFC6C'** \| '539C197E51D8' \| ✓ \|\\n\| '…_adde | **非 D 族（哈希指纹）** | `F256` | E1 |
| 44 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 3896 | 69 | `D96` | `D96B747BFC6C`（12） | ataset_addendum_d3b_2026_09_26.json' \| **' ⏎ `D96B747BFC6C` ⏎ B747BFC6C'** \| 14,722 \| R-10 漂移件 7/9（自报 '539C1 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 45 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 3901 | 56 | `D4` | `D4DD5C949443`（12） | 4_supp_l14v3_batch10_r1_executor.py' \| **' ⏎ `D4DD5C949443` ⏎ DD5C949443'** \| 56,894 \| R-2 单件逻辑链（L355 / L677 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 46 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 3928 | 637 | `D4` | `D4DD5C949443`（12） | AD2' + 'B70211BFA83E' + 'C8D539A58D29' + ' ⏎ `D4DD5C949443` ⏎ DD5C949443' + '802DECE2286A' + '79936B630015'  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 47 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 3959 | 878 | `D4` | `D4DD5C949443`（12） | AD2' + 'B70211BFA83E' / 'C8D539A58D29' + ' ⏎ `D4DD5C949443` ⏎ DD5C949443' + '802DECE2286A' / '79936B630015'  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 48 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 4098 | 54 | `D92` | `D92F74712DAB`（12） | 8_probe_register.py'（**本棒自产只读探测脚本**） \| **' ⏎ `D92F74712DAB` ⏎ F74712DAB'** \| 873 \| 改判总表并发写状态 + #1/#4 采纳面单次快照 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 49 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 4100 | 52 | `D4` | `D4E6F0934E5F`（12） | e48_apply.py'（**本棒自产追加执行器** · 唯一写入面） \| **' ⏎ `D4E6F0934E5F` ⏎ E6F0934E5F'** \| 2,329 \| 五次 'open(path,'ab')' 顺 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 50 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 4142 | 241 | `D92` | `D92F74712DAB`（12） | 42F13D'、'_e48_probe_register.py' 873 B / ' ⏎ `D92F74712DAB` ⏎ F74712DAB'、'_e48_docwriter_chain.py' 2,550 B / | **非 D 族（哈希指纹）** | `F256` | E1 |
| 51 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 4142 | 352 | `D4` | `D4E6F0934E5F`（12） | 5 件只读复算/探测脚本**；'_e48_apply.py' 2,329 B / ' ⏎ `D4E6F0934E5F` ⏎ E6F0934E5F' = **1 件追加执行器（本棒唯一写入面）**；**均非预登记产物件 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 52 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 4357 | 134 | `D9` | `D9E14ED29FB9`（12） | ss_pa_1_rbr_rm_result_2026_09_15.json'：记 ' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9' = SHA-1，实 SHA-256 = 'C7C59E0D2F6C' | **非 D 族（哈希指纹）** | `F1` | E2 |
| 53 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 4366 | 58 | `D9` | `D9E14ED29FB9`（12） | _pa_1_rbr_rm_result_2026_09_15.json' \| **' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9'**（v1 L32 行 '1'） \| **'D9E14ED29FB9' | **非 D 族（哈希指纹）** | `F1` | E2 |
| 54 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 4366 | 93 | `D9` | `D9E14ED29FB9`（12） | ' \| **'D9E14ED29FB9'**（v1 L32 行 '1'） \| **' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9'** \| 'c7c59e0d2f6c' \| 8,753 \| ✅ **S | **非 D 族（哈希指纹）** | `F1` | E2 |
| 55 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 4368 | 66 | `D30` | `D30EDA5A1063`（12） | prereg_v1_2026_09_27.md'（v1 自身） \| 未自登记 \| ' ⏎ `D30EDA5A1063` ⏎ EDA5A1063' \| '88052d7db895' \| 37,346 \| —（供 ② 交 | **非 D 族（哈希指纹）** | `F1` | E2 |
| 56 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 4472 | 140 | `D9` | `D9E14ED29FB9`（12） | -1[:12].upper() vs SHA-256[:12] 逐件对照复算**（' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9' / '1A90FD8F385A' / 'D30EDA5A1063'， | **非 D 族（哈希指纹）** | `F1` | E2 |
| 57 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 4472 | 174 | `D30` | `D30EDA5A1063`（12） | 对照复算**（'D9E14ED29FB9' / '1A90FD8F385A' / ' ⏎ `D30EDA5A1063` ⏎ EDA5A1063'，SHA-1 命中 3/3、SHA-256 命中 0/3）＋ '.mav | **非 D 族（哈希指纹）** | `F1` | E2 |
| 58 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 4479 | 616 | `D9` | `D9E14ED29FB9`（12） | *非内容变更、非转写错位，系算法口径错用**）＋ **本棒 3/3 独立复算**（' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9' / '1A90FD8F385A' / 'D30EDA5A1063'， | **非 D 族（哈希指纹）** | `F1` | E2 |
| 59 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 4479 | 650 | `D30` | `D30EDA5A1063`（12） | 独立复算**（'D9E14ED29FB9' / '1A90FD8F385A' / ' ⏎ `D30EDA5A1063` ⏎ EDA5A1063'，SHA-1 命中 3/3、SHA-256 命中 0/3）＋ **连带纠 | **非 D 族（哈希指纹）** | `F1` | E2 |
| 60 | `letters/TRAE_V4_WALKTHROUGH_BUGFIX_REQUEST_2026_09_27.md` | 210 | 141 | `D30` | `D30EDA5A1063`（12） | 实测 = 'b7547329af2e'（27,223 B）；v1 件文末自报 = ' ⏎ `D30EDA5A1063` ⏎ EDA5A1063'，实测 = '88052d7db895'（37,346 B）。两处**偏 | **非 D 族（哈希指纹）** | `F1` | E2 |
| 61 | `letters/_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md` | 96 | 38 | `D423` | `D423CA72CB3C`（12） | ' \|\\n\| '.tmp/_t15_inspect3.py' \| 1,890 \| ' ⏎ `D423CA72CB3C` ⏎ CA72CB3C' \|\\n\| '.tmp/_t15_inspect3_out.txt' \|  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 62 | `letters/_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md` | 135 | 65 | `D1` | `D1EE21F3F6AE`（12） | ut_manifest_2026_09_21.json' \| 291,551 \| ' ⏎ `D1EE21F3F6AE` ⏎ EE21F3F6AE' \|\\n\| 'deposon-sub/_tmp_degen.py' \| | **非 D 族（哈希指纹）** | `F12` | E3 |
| 63 | `letters/_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md` | 159 | 73 | `D3` | `D3F72F67977D`（12） | or_cache_v18_contamination.json' \| 639 \| ' ⏎ `D3F72F67977D` ⏎ F72F67977D' \|\\n\| 'deposon-sub/results/llm_prio | **非 D 族（哈希指纹）** | `F12` | E3 |
| 64 | `letters/_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md` | 218 | 74 | `D39` | `D39CB17B051B`（12） | ly_claude_code_2026_09_20.md' \| 64,212 \| ' ⏎ `D39CB17B051B` ⏎ CB17B051B' \|\\n\| 'letters/_v4_distillation_repl | **非 D 族（哈希指纹）** | `F256` | E1 |
| 65 | `letters/_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md` | 228 | 81 | `D3` | `D3BDFC99FCDC`（12） | ode_supplement_2026_09_20.md' \| 11,877 \| ' ⏎ `D3BDFC99FCDC` ⏎ BDFC99FCDC' \|\\n\| 'letters/_v4_ide_track_review | **非 D 族（哈希指纹）** | `F12` | E3 |
| 66 | `letters/_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md` | 265 | 63 | `D4` | `D4DD5C949443`（12） | l14v3_batch10_r1_executor.py' \| 56,894 \| ' ⏎ `D4DD5C949443` ⏎ DD5C949443' \|\\n\| 'results/_v4_supp_l14v3_batch | **非 D 族（哈希指纹）** | `F256` | E1 |
| 67 | `letters/_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md` | 288 | 61 | `D245` | `D245AE4CE385`（12） | p_l14v3_batch2_r1_result.json' \| 4,128 \| ' ⏎ `D245AE4CE385` ⏎ AE4CE385' \|\\n\| 'results/_v4_supp_l14v3_batch2_ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 68 | `letters/_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md` | 298 | 62 | `D9` | `D9FE7AA2D292`（12） | _l14v3_batch2_r4_executor.py' \| 58,176 \| ' ⏎ `D9FE7AA2D292` ⏎ FE7AA2D292' \|\\n\| 'results/_v4_supp_l14v3_batch | **非 D 族（哈希指纹）** | `F256` | E1 |
| 69 | `letters/_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md` | 305 | 62 | `D24` | `D24B84671C23`（12） | _l14v3_batch3_r1_result.json' \| 66,520 \| ' ⏎ `D24B84671C23` ⏎ B84671C23' \|\\n\| 'results/_v4_supp_l14v3_batch3 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 70 | `letters/_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md` | 350 | 59 | `D339` | `D339D7286AD8`（12） | upp_l14v3_batch6_r5_report.md' \| 8,596 \| ' ⏎ `D339D7286AD8` ⏎ D7286AD8' \|\\n\| 'results/_v4_supp_l14v3_batch6_ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 71 | `letters/_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md` | 358 | 62 | `D789` | `D789F9BD4FA1`（12） | _l14v3_batch7_r4_executor.py' \| 51,289 \| ' ⏎ `D789F9BD4FA1` ⏎ F9BD4FA1' \|\\n\| 'results/_v4_supp_l14v3_batch7_ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 72 | `letters/_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md` | 399 | 49 | `D6` | `D6CB03A4657E`（12） | ults/_v4_supp_t1_result.json' \| 82,365 \| ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' \|\\n\| 'results/_v4_supp_t1_verdict. | **非 D 族（哈希指纹）** | `F256` | E1 |
| 73 | `letters/_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md` | 471 | 76 | `D8` | `D8FE147AAC30`（12） | json' \| 7,842 / '1EC7ABA6AFD8' \| 7,843 / ' ⏎ `D8FE147AAC30` ⏎ FE147AAC30' \| 纯尾换行（远端多 1 字节 \\n，前 7842 字节逐字节等价） | **非 D 族（哈希指纹）** | `F12` | E3 |
| 74 | `letters/_letter_to_pi_upload_application_supplement_2026_09_26.md` | 39 | 61 | `D3` | `D3F72F67977D`（12） | or_cache_v18_contamination.json' \| 639 / ' ⏎ `D3F72F67977D` ⏎ F72F67977D' \| 696 / '9539DADEAEC7' \| 实质差异（首异字节 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 75 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 124 | 38 | `D423` | `D423CA72CB3C`（12） | \|\\r\\n\| '.tmp/_t15_inspect3.py' \| 1,890 \| ' ⏎ `D423CA72CB3C` ⏎ CA72CB3C' \|\\r\\n\| '.tmp/_t15_inspect3_out.txt'  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 76 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 163 | 65 | `D1` | `D1EE21F3F6AE`（12） | ut_manifest_2026_09_21.json' \| 291,551 \| ' ⏎ `D1EE21F3F6AE` ⏎ EE21F3F6AE' \|\\r\\n\| 'deposon-sub/_tmp_degen.py' | **非 D 族（哈希指纹）** | `F12` | E3 |
| 77 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 187 | 73 | `D3` | `D3F72F67977D`（12） | or_cache_v18_contamination.json' \| 639 \| ' ⏎ `D3F72F67977D` ⏎ F72F67977D' \|\\r\\n\| 'deposon-sub/results/llm_pr | **非 D 族（哈希指纹）** | `F12` | E3 |
| 78 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 246 | 74 | `D39` | `D39CB17B051B`（12） | ly_claude_code_2026_09_20.md' \| 64,212 \| ' ⏎ `D39CB17B051B` ⏎ CB17B051B' \|\\r\\n\| 'letters/_v4_distillation_re | **非 D 族（哈希指纹）** | `F256` | E1 |
| 79 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 256 | 81 | `D3` | `D3BDFC99FCDC`（12） | ode_supplement_2026_09_20.md' \| 11,877 \| ' ⏎ `D3BDFC99FCDC` ⏎ BDFC99FCDC' \|\\r\\n\| 'letters/_v4_ide_track_revi | **非 D 族（哈希指纹）** | `F12` | E3 |
| 80 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 293 | 63 | `D4` | `D4DD5C949443`（12） | l14v3_batch10_r1_executor.py' \| 56,894 \| ' ⏎ `D4DD5C949443` ⏎ DD5C949443' \|\\r\\n\| 'results/_v4_supp_l14v3_bat | **非 D 族（哈希指纹）** | `F256` | E1 |
| 81 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 316 | 61 | `D245` | `D245AE4CE385`（12） | p_l14v3_batch2_r1_result.json' \| 4,128 \| ' ⏎ `D245AE4CE385` ⏎ AE4CE385' \|\\r\\n\| 'results/_v4_supp_l14v3_batch | **非 D 族（哈希指纹）** | `F256` | E1 |
| 82 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 326 | 62 | `D9` | `D9FE7AA2D292`（12） | _l14v3_batch2_r4_executor.py' \| 58,176 \| ' ⏎ `D9FE7AA2D292` ⏎ FE7AA2D292' \|\\r\\n\| 'results/_v4_supp_l14v3_bat | **非 D 族（哈希指纹）** | `F256` | E1 |
| 83 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 333 | 62 | `D24` | `D24B84671C23`（12） | _l14v3_batch3_r1_result.json' \| 66,520 \| ' ⏎ `D24B84671C23` ⏎ B84671C23' \|\\r\\n\| 'results/_v4_supp_l14v3_batc | **非 D 族（哈希指纹）** | `F256` | E1 |
| 84 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 378 | 59 | `D339` | `D339D7286AD8`（12） | upp_l14v3_batch6_r5_report.md' \| 8,596 \| ' ⏎ `D339D7286AD8` ⏎ D7286AD8' \|\\r\\n\| 'results/_v4_supp_l14v3_batch | **非 D 族（哈希指纹）** | `F12` | E3 |
| 85 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 386 | 62 | `D789` | `D789F9BD4FA1`（12） | _l14v3_batch7_r4_executor.py' \| 51,289 \| ' ⏎ `D789F9BD4FA1` ⏎ F9BD4FA1' \|\\r\\n\| 'results/_v4_supp_l14v3_batch | **非 D 族（哈希指纹）** | `F256` | E1 |
| 86 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 427 | 49 | `D6` | `D6CB03A4657E`（12） | ults/_v4_supp_t1_result.json' \| 82,365 \| ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' \|\\r\\n\| 'results/_v4_supp_t1_verdic | **非 D 族（哈希指纹）** | `F256` | E1 |
| 87 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 515 | 70 | `D511` | `D511C545F88E`（12） | m/plugins/_pg_v01_compute.py' \| 20,923 \| ' ⏎ `D511C545F88E` ⏎ C545F88E' \| CLEAN（放行） \|\\r\\n\| 'deposon-repo/dep | **非 D 族（哈希指纹）** | `F256` | E1 |
| 88 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 524 | 82 | `D3` | `D3B45B64C0DA`（12） | 3_review_r3_sha_2026_09_23.py' \| 1,881 \| ' ⏎ `D3B45B64C0DA` ⏎ B45B64C0DA' \| CLEAN（放行） \|\\r\\n\| 'deposon-repo/d | **非 D 族（哈希指纹）** | `F256` | E1 |
| 89 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 560 | 87 | `D0` | `D0D188C60A62`（12） | inimax_artifact_2026_09_16.py' \| 7,361 \| ' ⏎ `D0D188C60A62` ⏎ D188C60A62' \| CLEAN（放行） \|\\r\\n\| 'deposon-sub/de | **非 D 族（哈希指纹）** | `F12` | E3 |
| 90 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 568 | 96 | `D2` | `D2CD7ACB29A1`（12） | caption_runner_2026_09_16.py' \| 18,596 \| ' ⏎ `D2CD7ACB29A1` ⏎ CD7ACB29A1' \| CLEAN（放行） \|\\r\\n\| 'deposon-sub/de | **非 D 族（哈希指纹）** | `F256` | E1 |
| 91 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 578 | 98 | `D1` | `D1BC564264EF`（12） | ication_runner_2026_09_16.py' \| 13,230 \| ' ⏎ `D1BC564264EF` ⏎ BC564264EF' \| CLEAN（放行） \|\\r\\n\| 'deposon-sub/de | **非 D 族（哈希指纹）** | `F12` | E3 |
| 92 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 604 | 49 | `D76` | `D76F2DC473BE`（12） | oson-repo/verifier/README.md' \| 14,360 \| ' ⏎ `D76F2DC473BE` ⏎ F2DC473BE' \| CLEAN（放行） \|\\r\\n\| 'deposon-repo/ve | **非 D 族（哈希指纹）** | `F256` | E1 |
| 93 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 663 | 53 | `D9` | `D9BFAAE6D08B`（12） | -repo/verifier/runs/v34_run2.md' \| 118 \| ' ⏎ `D9BFAAE6D08B` ⏎ BFAAE6D08B' \| CLEAN（放行） \|\\r\\n\| 'deposon-repo/v | **非 D 族（哈希指纹）** | `F256` | E1 |
| 94 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 708 | 51 | `D48` | `D48AC555761F`（12） | on-repo/verifier/v39/check.sh' \| 1,935 \| ' ⏎ `D48AC555761F` ⏎ AC555761F' \| CLEAN（放行） \|\\r\\n\| 'deposon-repo/ve | **非 D 族（哈希指纹）** | `F256` | E1 |
| 95 | `letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | 760 | 76 | `D8` | `D8FE147AAC30`（12） | json' \| 7,842 \| '1EC7ABA6AFD8' \| 7,843 \| ' ⏎ `D8FE147AAC30` ⏎ FE147AAC30' \| 纯尾换行（远端多 1 字节 '\\\\n'）\| **批准以本地为准覆 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 96 | `letters/_v4_commission_paper_final_glm_2026_09_24_v3.md` | 62 | 78 | `D96` | `D96B747BFC6C`（12） | addendum_d3b_2026_09_26.json'（14,722 B · ' ⏎ `D96B747BFC6C` ⏎ B747BFC6C'，D3 wave2）\\n  - 'results/_v4_pi_cot_ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 97 | `letters/_v4_commission_paper_final_glm_2026_09_24_v4.md` | 65 | 78 | `D96` | `D96B747BFC6C`（12） | addendum_d3b_2026_09_26.json'（14,722 B · ' ⏎ `D96B747BFC6C` ⏎ B747BFC6C'，D3 wave2）\\n  - 'results/_v4_pi_cot_ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 98 | `letters/_v4_commission_upload_executor_2026_09_24_v3.md` | 127 | 76 | `D96` | `D96B747BFC6C`（12） | addendum_d3b_2026_09_26.json'（14,722 B · ' ⏎ `D96B747BFC6C` ⏎ B747BFC6C'） \| D3 wave2 \| **仅入本地件** \|\\n\| 'resul | **非 D 族（哈希指纹）** | `F256` | E1 |
| 99 | `letters/_v4_commission_upload_executor_2026_09_24_v3.md` | 256 | 118 | `D96` | `D96B747BFC6C`（12） | addendum_d3b_2026_09_26.json' \| 14,722 \| ' ⏎ `D96B747BFC6C` ⏎ B747BFC6C' \|\\n\| 任务 B v2.2 dataset addendum d3c | **非 D 族（哈希指纹）** | `F256` | E1 |
| 100 | `letters/_v4_distillation_brainstorm_reply_codex_2026_09_21.md` | 23 | 267 | `D511` | `D511C545F88E`（12） | /plugins/_pg_v01_compute.py:145), SHA-12 ' ⏎ `D511C545F88E` ⏎ C545F88E', lines 145-197). The curvature is fi | **非 D 族（哈希指纹）** | `F256` | E1 |
| 101 | `letters/_v4_distillation_invitation_2026_09_20_v1.0.md` | 101 | 68 | `D511` | `D511C545F88E`（12） | pg_v01_compute.py' (20,923 bytes, SHA-12 ' ⏎ `D511C545F88E` ⏎ C545F88E') — P-G v01 compute scaffold; carries | **非 D 族（哈希指纹）** | `F256` | E1 |
| 102 | `letters/_v4_distillation_invitation_2026_09_20_v1.0.md` | 385 | 78 | `D511` | `D511C545F88E`（12） | m\\plugins\\_pg_v01_compute.py' \| 20,923 \| ' ⏎ `D511C545F88E` ⏎ C545F88E' \| §2.7, §3.1 S-02, §3.2 S-08, §3.6 S | **非 D 族（哈希指纹）** | `F256` | E1 |
| 103 | `letters/_v4_distillation_reply_claude_code_2026_09_20.md` | 68 | 495 | `D3` | `D3BDFC99FCDC`（12） | _code_supplement_2026_09_20.md' 11,877 / ' ⏎ `D3BDFC99FCDC` ⏎ BDFC99FCDC'; '_v4_d1_response_workbuddy_2026_0 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 104 | `letters/_v4_distillation_reply_claude_code_2026_09_20.md` | 253 | 144 | `D6` | `D6F233D73C45`（12） | namics_result_2026_09_15.json' (9,098 B, ' ⏎ `D6F233D73C45` ⏎ F233D73C45'), 'boss_pc_1_a1_resampling_2026_09 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 105 | `letters/_v4_distillation_reply_claude_code_2026_09_20.md` | 346 | 363 | `D511` | `D511C545F88E`（12） | 01_compute.py:114-121' (20,923 B, SHA-12 ' ⏎ `D511C545F88E` ⏎ C545F88E'), computing 'T_H(x) = Exp_0(Log_0(x) | **非 D 族（哈希指纹）** | `F256` | E1 |
| 106 | `letters/_v4_distillation_reply_coze_2026_09_20.md` | 89 | 196 | `D511` | `D511C545F88E`（12） | m/plugins/_pg_v01_compute.py'（20,923 B · ' ⏎ `D511C545F88E` ⏎ C545F88E'）的 'status = SCAFFOLDING (PRE-REGISTR | **非 D 族（哈希指纹）** | `F256` | E1 |
| 107 | `letters/_v4_distillation_reply_coze_2026_09_20.md` | 144 | 50 | `D511` | `D511C545F88E`（12） | 。** 我未打开 '_pg_v01_compute.py'（20,923 B · ' ⏎ `D511C545F88E` ⏎ C545F88E'），也不确定九个模型的 (T,A) 与 'd_fix2_cosine' 的 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 108 | `letters/_v4_distillation_reply_coze_2026_09_20.md` | 246 | 347 | `D6` | `D6F233D73C45`（12） | namics_result_2026_09_15.json'（9,098 B · ' ⏎ `D6F233D73C45` ⏎ F233D73C45'）L29 '"ess_match_ratio": 0.0'、L30 ' | **非 D 族（哈希指纹）** | `F256` | E1 |
| 109 | `letters/_v4_distillation_reply_coze_2026_09_20.md` | 451 | 571 | `D511` | `D511C545F88E`（12） | C2EAFF0D1'、'78AC391D16FC'、'02443DD300CE'、' ⏎ `D511C545F88E` ⏎ C545F88E'、'3D54B277620E'、'F02B3EEE8D6E'），（二）一处 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 110 | `letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23.md` | 151 | 50 | `D3` | `D3B45B64C0DA`（12） |  '_v3_review_r3_sha_2026_09_23.py' \| — \| ' ⏎ `D3B45B64C0DA` ⏎ B45B64C0DA' \| 新增 \|\\n\| 新增件 \| '_v3_review_r4_fix | **非 D 族（哈希指纹）** | `F256` | E1 |
| 111 | `letters/_v4_distillation_theme_reply_workbuddy_part2_2026_09_20.md` | 58 | 69 | `D6` | `D6F233D73C45`（12） | cator_dynamics_result_2026_09_15.json' \| ' ⏎ `D6F233D73C45` ⏎ F233D73C45' \| Replicator Dynamics + ESS（Smith  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 112 | `letters/_v4_theme_reply_mavis_2026_09_20.md` | 82 | 331 | `D511` | `D511C545F88E`（12） | plugins\\_pg_v01_compute.py' (sha256[:12] ' ⏎ `D511C545F88E` ⏎ C545F88E', 20,923 bytes per invitation §8 line | **非 D 族（哈希指纹）** | `F256` | E1 |
| 113 | `letters/_v4_theme_reply_mavis_2026_09_20_v1.1.md` | 82 | 331 | `D511` | `D511C545F88E`（12） | plugins\\_pg_v01_compute.py' (sha256[:12] ' ⏎ `D511C545F88E` ⏎ C545F88E', 20,923 bytes per invitation §8 line | **非 D 族（哈希指纹）** | `F256` | E1 |
| 114 | `letters/_v4_theme_reply_mavis_2026_09_20_v1.2.md` | 82 | 331 | `D511` | `D511C545F88E`（12） | plugins\\_pg_v01_compute.py' (sha256[:12] ' ⏎ `D511C545F88E` ⏎ C545F88E', 20,923 bytes per invitation §8 line | **非 D 族（哈希指纹）** | `F256` | E1 |
| 115 | `letters/_v4_theme_reply_trae_work_2026_09_20.md` | 49 | 236 | `D511` | `D511C545F88E`（12） | eposon_team/plugins/_pg_v01_compute.py' (' ⏎ `D511C545F88E` ⏎ C545F88E') is self-described as scaffolding/pr | **非 D 族（哈希指纹）** | `F256` | E1 |
| 116 | `letters/_v4_theme_reply_trae_work_2026_09_20_v1.2.md` | 37 | 374 | `D511` | `D511C545F88E`（12） | eposon_team/plugins/_pg_v01_compute.py' (' ⏎ `D511C545F88E` ⏎ C545F88E') enumerates Log_0/Exp_0, Möbius addi | **非 D 族（哈希指纹）** | `F256` | E1 |
| 117 | `letters/_v4_walkthrough_bugfix_reply_trae_code_2026_09_27.md` | 232 | 60 | `D9` | `D9E14ED29FB9`（12） | ss_pa_1_rbr_rm_result_2026_09_15.json' \| ' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9' \| **'D9E14ED29FB9'** \| 'C7C59E0D2F | **非 D 族（哈希指纹）** | `F1` | E2 |
| 118 | `letters/_v4_walkthrough_bugfix_reply_trae_code_2026_09_27.md` | 232 | 79 | `D9` | `D9E14ED29FB9`（12） | lt_2026_09_15.json' \| 'D9E14ED29FB9' \| **' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9'** \| 'C7C59E0D2F6C' \| **SHA-1 命中**  | **非 D 族（哈希指纹）** | `F1` | E2 |
| 119 | `letters/_v4_walkthrough_bugfix_reply_trae_code_2026_09_27.md` | 235 | 111 | `D6` | `D6F233D73C45`（12） |  \| '18C9C370A6AE' \| **'18C9C370A6AE'** \| ' ⏎ `D6F233D73C45` ⏎ F233D73C45' \| **SHA-1 命中** \|\\n\| 4-r \| 'deposon | **非 D 族（哈希指纹）** | `F256` | E1 |
| 120 | `letters/_v4_walkthrough_bugfix_reply_trae_code_2026_09_27.md` | 239 | 96 | `D74` | `D74D6B39D1B0`（12） |  \| '717C26DF5A00' \| **'717C26DF5A00'** \| ' ⏎ `D74D6B39D1B0` ⏎ D6B39D1B0' \| **SHA-1 命中** \|\\n\| 10 \| 'results/_ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 121 | `letters/查理_deposon双主线论文终稿_2026-10-01_v0.3.md` | 629 | 126 | `D279` | `D279EBDE5E84`（12） | 标）**」；「**v1 锚点**：预登记 '696af9121d9f' / 判定 ' ⏎ `D279EBDE5E84` ⏎ EBDE5E84'（E-25 改判假证伪素材面 + E-26 claim 定位偏差注记）」（ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 122 | `results/_deliverables_verification_and_v5_handover_pending_2026_10_12.md` | 17 | 155 | `D11` | `D11D75BA6236`（12） |  False \| **0** \| ✅ **与 Trae 自报逐位吻合**（其自报 ' ⏎ `D11D75BA6236` ⏎ D75BA6236'） \|\\n\| '_degradation_reversal_guide_ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 123 | `results/_fake_verdict_reverify_sixitem_ledger_2026_09_30.md` | 108 | 205 | `D30` | `D30EDA5A1063`（12） | 1 偏差显式更正**（'1A90FD8F385A'→'b7547329af2e'；' ⏎ `D30EDA5A1063` ⏎ EDA5A1063'→'88052d7db895'）。锚件 SHA-12 见 §0.1（v1 | **非 D 族（哈希指纹）** | `F1` | E2 |
| 124 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 4 | 51 | `D8` | `D8D5E4D2154F`（12） | ：**protocol-keeper 草案件**（口径固化／判据形式化面）——将 ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §3 建议 1 之拟议口径**形式化为可操作之判据**，并给**≥2 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 125 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 5 | 13 | `D8` | `D8D5E4D2154F`（12） | *。**⛔ 非条款正文、⛔ 非判定、⛔ 0 自生效**。\\n> **落实对象**：' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F'（'results/_r_pair_nonportrait_full_ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 126 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 30 | 73 | `D8` | `D8D5E4D2154F`（12） | 非代裁）**：口径源之禁令实为「**行为禁令 2 项 ＋ 废止口径 1 项**」，' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §3 建议 1 将其并列为「**三要件**」；此**合列／分列之别* | **非 D 族（哈希指纹）** | `F12` | E3 |
| 127 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 40 | 30 | `D8` | `D8D5E4D2154F`（12） | --\|---\|---\|\\n\| '0FD7A26FC339' **L341**（经 ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §0.2 逐字引） \| 「**⛔ 禁止画像式**：⛔ **0 预测  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 128 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 43 | 4 | `D8` | `D8D5E4D2154F`（12） | 判别理由**（该口径之所以违禁，因其**以预测 PI 行为为对象**） \|\\n\| ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' **§3 建议 1** \| 建议立口径件一条：「非画像 ＝ ①0 预 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 129 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 72 | 86 | `D8` | `D8D5E4D2154F`（12） | **若** PI 对两半给出**同一** 'option_chosen'」——沿 ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §1.3 ⑥ 之实测例）；②'r' ＝ **禁令句**（「**⛔ 0 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 130 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 83 | 122 | `D8` | `D8D5E4D2154F`（12） | 举）者，属 'r' ＝ **禁令句／元数据** ⇒ ⛔ **0 计入违例**（沿 ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §1.3 ③「**禁令文本本身恰为合规之证据**」）。**判别之实质 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 131 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 86 | 115 | `D8` | `D8D5E4D2154F`（12） | PI 有此偏好）；②**纪律行／署名行**；③**相似度读数用于措辞距离**（沿 ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §2.2 要件②之核读结论：「**仅用于 0 复用之字面距离、0 用 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 132 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 97 | 59 | `D8` | `D8D5E4D2154F`（12） | · 沿实测）** \| 「**⛔ 0 沿用复现一致率口径**」之**禁令句本体**（' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §2.2 要件③ 实测：A L230／B L252 **2/2 全为 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 133 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 102 | 156 | `D8` | `D8D5E4D2154F`（12） | 用」）＋ **正面要求 1 项**（L341 之「对象＝可迁移之判断方法」）；而 ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §3 建议 1 之拟议字面将其列为「**三要件**」（① ② ③）， | **非 D 族（哈希指纹）** | `F12` | E3 |
| 134 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 104 | 22 | `D8` | `D8D5E4D2154F`（12） | ② ③），**未含**正面要求。\\n>\\n> ⚠ **另须指出之一处面不一致**：' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §2.2 之逐要件论证表实列 **⑤ 项**（①0 预测／②0 构造 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 135 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 108 | 21 | `D8` | `D8D5E4D2154F`（12） | \|\\n\|---\|---\|---\|---\|\\n\| **处理甲 · 合列为三要件**（' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §3 建议 1 之字面） \| 判词 ＝ ①∧②∧③ 三闸 \| ①** | **非 D 族（哈希指纹）** | `F12` | E3 |
| 136 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 116 | 74 | `D8` | `D8D5E4D2154F`（12） | 针正则、0 重跑扫描、0 施测**（沿 0 实测纪律）。以下触发面**均照录** ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §1.3 已载之**三类判别扫描**，其定位为「**候选处之筛查器* | **非 D 族（哈希指纹）** | `F12` | E3 |
| 137 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 118 | 11 | `D8` | `D8D5E4D2154F`（12） | **候选处之筛查器**」，**⛔ 0 单独承载判词**。\\n\\n\| 触发面（照录 ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §1.3） \| 服务之要件 \| 沿既有件实测之性质 \| ⛔ 定位 \| | **非 D 族（哈希指纹）** | `F12` | E3 |
| 138 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 133 | 79 | `D8` | `D8D5E4D2154F`（12） | ②外延边界（候呈 3／5）**未裁**而影响判词；③「未核得」面**存在**（沿 ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §5.5 第 4 项：「**「0 核」≠「已合规」**」） \| ⛔  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 139 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 139 | 40 | `D8` | `D8D5E4D2154F`（12） | n\\n### §2.1 判定面 D 之定义（**「全件面」之可操作化** · 沿 ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §0.4 逐字承接）\\n\\n> **判定面 D（全件面）** ＝ * | **非 D 族（哈希指纹）** | `F12` | E3 |
| 140 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 141 | 47 | `D8` | `D8D5E4D2154F`（12） | 判定面 D（全件面）** ＝ **被审件之逐行全文**，含以下**六类面**（沿 ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §0.4 之列举）：\\n\\n\| 类 \| 面 \| 在判据中之处理 \|\\ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 141 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 147 | 37 | `D8` | `D8D5E4D2154F`（12） | 定性 \|\\n\| ③ \| **题面正文（stem／选项／推理行）** \| 逐处定性（' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §1.2 实测：题面面「PI」＝ **0**） \|\\n\| ④ \| * | **非 D 族（哈希指纹）** | `F12` | E3 |
| 142 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 152 | 24 | `D8` | `D8D5E4D2154F`（12） | r' ＝ **元数据**） \|\\n\\n> ⚠ **六类面之处理 0 例外**：沿 ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §0.3 逐字「**判词须由逐处语义定性**……得出，**不可由字面 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 143 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 159 | 50 | `D8` | `D8D5E4D2154F`（12） |  vs 题面面** \| ✅ **已裁**（全件面**取代**题面面为判定面） \| ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §0.1 ①；原判词 '8C5F83C3C4CF' §3 之题面面判 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 144 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 161 | 57 | `D8` | `D8D5E4D2154F`（12） | 「被引用件全文」** \| 🟨 **候呈 3 · 待 PI**（见 §2.3） \| ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §4 候呈 3；本件 **⛔ 0 代裁** \|\\n\| **引用件语料 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 145 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 162 | 48 | `D8` | `D8D5E4D2154F`（12） | 用件语料面之定性** \| 🟨 **候呈 5 · 待 PI**（见 §2.4） \| ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §3 建议 5／§4；本件 **⛔ 0 代裁** \|\\n\| **判定 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 146 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 167 | 13 | `D8` | `D8D5E4D2154F`（12） | 引用件全文」**（**如实列 · ⛔ 0 代裁**）\\n\\n> **逐字承接**（' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §4 候呈 3 原文）：「**判定面外延边界：是否及于「被引用件全文 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 147 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 172 | 17 | `D8` | `D8D5E4D2154F`（12） | 或「个人化自省」面（不合规）**另作定性** \|\\n\| **已核得之事实** \| ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §1.5 实测：A L212 逐字转录 'SQ-07'「在一条工作线 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 148 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 174 | 46 | `D8` | `D8D5E4D2154F`（12） | *⛔ 未核得之面** \| **被引用件全文未逐件通读**，仅核其被转录之片段（沿 ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §5.5 第 4 项：「**「0 核」≠「已合规」**」） \|\\n\| | **非 D 族（哈希指纹）** | `F12` | E3 |
| 149 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 179 | 13 | `D8` | `D8D5E4D2154F`（12） | 语料面之定性**（**如实列 · ⛔ 0 代裁**）\\n\\n> **逐字承接**（' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §3 建议 5 原文）：「建议登记：**「引用件 ≠ 自撰件」**， | **非 D 族（哈希指纹）** | `F12` | E3 |
| 150 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 222 | 82 | `D8` | `D8D5E4D2154F`（12） | 35C4DDC' §2.5.3）⛔ **0 与**「**裸串 vs 词边界**」（' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §1.1）**混称同口径** ⇒ **分别登记** \| 沿 '246 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 151 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 223 | 101 | `D8` | `D8D5E4D2154F`（12） | 口径**并附裸串读数 \| 'AFA5EB53D216' §3.2 第 4 条（沿 ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §1.1 之 3 处 'API' 伪阳） \|\\n\| **I-5 版本 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 152 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 267 | 26 | `D8` | `D8D5E4D2154F`（12） | 三闸各自独立取证、独立留痕 \|\\n\| **依据（正）** \| ①**逐字落实** ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §3 建议 1 之拟议字面，⛔ 0 增删要件、⛔ 0 改其结构；②形 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 153 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 268 | 188 | `D8` | `D8D5E4D2154F`（12） | 仅以**计数＋0 命中**充当证据，则本判据**退回**字面计数式 ⇒ **恰为 ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §2.3 所指之病**（判据—对象错配）；⚠ **R1-3 正面要求 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 154 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 275 | 48 | `D8` | `D8D5E4D2154F`（12） | 据（正）** \| ①**与已裁之径同构**：'r12a' 已裁「语义禁令口径」＋ ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §0.3 逐字「判词须由逐处语义定性……得出」⇒ 本案**将已裁之径 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 155 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 283 | 59 | `D8` | `D8D5E4D2154F`（12） | *兼顾**语义正当（轨甲）与机械可核（轨乙）；②轨乙**沿既有件已存在之读数**（' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §1.1／§1.6）⇒ **0 新增读数面**；③轨乙对「**自我指 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 156 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 309 | 46 | `D8` | `D8D5E4D2154F`（12） | **它把已裁之径落成结构，而非落成纪律**——'r12a' 已裁「语义禁令口径」，' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §0.3 已逐字定「判词须由逐处语义定性……得出」；案②**以段②为 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 157 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 309 | 155 | `D8` | `D8D5E4D2154F`（12） | 数直接出判词」**在结构上不可能**（而非仅在纪律上被禁止）⇒ **直接对治** ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §2.3 所指之根因（**判据—对象错配**）。\\n> ②**它与既 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 158 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 311 | 31 | `D8` | `D8D5E4D2154F`（12） | 分工、0 派棒**。\\n> ③**它给「未核得」与「覆盖域」以正式之位**⇒ 使 ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §5.5 第 4 项之病（「**「0 核」≠「已合规」**」）在** | **非 D 族（哈希指纹）** | `F12` | E3 |
| 159 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 343 | 145 | `D8` | `D8D5E4D2154F`（12） | ，且本判据**若不立**，则下一件重审将**再次**面临「判据—对象错配」之复现（' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §2.3 之根因）⇒ 正式化之价值**在「可复用与可援引」，非在「本 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 160 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 353 | 27 | `D8` | `D8D5E4D2154F`（12） | ---\|:---:\|---\|\\n\| **1** \| **判据要件之数**：三要件（' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §3 建议 1）抑或五要件（同件 §2.2 之 ④⑤） \| 增删要件 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 161 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 359 | 86 | `D8` | `D8D5E4D2154F`（12） |  \| **本件 0 施测、0 跑实验**；且 0 施测于任何非 PI 受试者（沿 ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §5.5 第 2 项） \| 🟡 中 \| §2.4／§4.1 R1-3 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 162 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 377 | 36 | `D8` | `D8D5E4D2154F`（12） | 设**）。\\n- ⛔ **0 代拟他件之任何字面**：本件所载触发面**照录** ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §1.3 之既有探针面；所载要件字面**照录** '0FD7A26F | **非 D 族（哈希指纹）** | `F12` | E3 |
| 163 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 377 | 125 | `D8` | `D8D5E4D2154F`（12） | FC339' L341／L343 与 '41F5F1689D09' E-26（经 ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §0.2 之逐字引）；**⛔ 0 新拟探针正则、0 新拟词条文字** | **非 D 族（哈希指纹）** | `F12` | E3 |
| 164 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 382 | 27 | `D8` | `D8D5E4D2154F`（12） | **既有件一字不动**）\\n\\n- ⛔ **0 编辑／覆写／改名／移动／删除**：' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F'／'AFA5EB53D216'／'246CE35C4DDC'／'8C5 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 165 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 389 | 134 | `D8` | `D8D5E4D2154F`（12） | ICT_SUBJ' 3＋4、'D3_REPRODUCE' 1＋1）**皆引自** ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §1.3 之既有实测，**0 由本件复核、0 冒充为本件之观测**。 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 166 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 394 | 144 | `D8` | `D8D5E4D2154F`（12） | 「均可迁移」之自陈**本件 0 独立施测**。**「0 核」≠「已合规」**（沿 ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §5.5 第 4 项）。\\n7. ⚠ **「可迁移」0 实证**：「 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 167 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 395 | 76 | `D8` | `D8D5E4D2154F`（12） |  PI 受试者**；本件**沿该限制**，⛔ **0 因全件面合规而消解**（沿 ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §5.5 第 2 项）。\\n8. ⚠ **本件之形式化可外推、其读数 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 168 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 397 | 31 | `D8` | `D8D5E4D2154F`（12） | 推**至构造面之外。\\n9. ⚠ **RPQ-5／RPQ-6 非本件议题**：沿 ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' §4 候呈 6——本件 **0 重审、0 预判**该二项；若 PI  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 169 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 409 | 98 | `D8` | `D8D5E4D2154F`（12） | _2026_10_09.md' \| **落实对象**（§3 建议 1 之源） \| ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' \| 28,176 \|\\n\| 2 \| 'results/_wordli | **非 D 族（哈希指纹）** | `F12` | E3 |
| 170 | `results/_nonportrait_criterion_formalization_design_2026_10_10.md` | 414 | 38 | `D8` | `D8D5E4D2154F`（12） | \|\\n\\n> ✅ **交叉印证**：#1–#3 之 SHA-12 与派工单所载锚（' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F'／'AFA5EB53D216'／'246CE35C4DDC'）**逐一 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 171 | `results/_questionnaire_cards_intake_register_supplement_2_2026_10_10.md` | 1472 | 16 | `D8` | `D8D5E4D2154F`（12） | estion'（逐字原文）：\\n\\n'''text\\nRPQ 重审·判据径择定（件  ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F）：全件面 138 处「PI」逐处定性——语义禁令口径下＝合规（0 处行 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 172 | `results/_questionnaire_cards_intake_register_supplement_2_2026_10_10.md` | 1539 | 219 | `D8` | `D8D5E4D2154F`（12） | id":"r12a_rpq","question":"RPQ 重审·判据径择定（件  ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F）：全件面 138 处「PI」逐处定性——语义禁令口径下＝合规（0 处行 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 173 | `results/_questionnaire_cards_intake_register_supplement_4_2026_10_10.md` | 83 | 25 | `D9` | `D9CCD75C652B`（12） | 字原文）：\\n\\n'''text\\nT1 温度轴 Exp2 全链收官（result『 ⏎ `D9CCD75C652B` ⏎ CCD75C652B』＋判读件『15C1C4B317A0』）。主判：C 段温度轴效应判『轴无 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 174 | `results/_questionnaire_cards_intake_register_supplement_4_2026_10_10.md` | 188 | 231 | `D9` | `D9CCD75C652B`（12） | tire","question":"T1 温度轴 Exp2 全链收官（result『 ⏎ `D9CCD75C652B` ⏎ CCD75C652B』＋判读件『15C1C4B317A0』）。主判：C 段温度轴效应判『轴无 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 175 | `results/_r2_build_manifest_2026_10_12.json` | 26 | 19 | `D511` | `D511C545F88E`（12） | \\n   "bytes": 20931,\\r\\n   "orig_sha12": " ⏎ `D511C545F88E` ⏎ C545F88E",\\r\\n   "new_sha12": "0D17B31E12A0",\\ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 176 | `results/_r2_build_manifest_2026_10_12.json` | 204 | 18 | `D1` | `D1AE2E035F57`（12） | a12": "3E369A1F6171",\\r\\n   "new_sha12": " ⏎ `D1AE2E035F57` ⏎ AE2E035F57",\\r\\n   "git_sha1": "471b3767809659 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 177 | `results/_r2_build_manifest_2026_10_12.json` | 267 | 19 | `D74` | `D74E1534493E`（12） | r\\n   "bytes": 6868,\\r\\n   "orig_sha12": " ⏎ `D74E1534493E` ⏎ E1534493E",\\r\\n   "new_sha12": "DB9DD0C2D9E2", | **非 D 族（哈希指纹）** | `F256` | E1 |
| 178 | `results/_r2_build_manifest_2026_10_12.json` | 364 | 18 | `D8` | `D8AC8D85ACFD`（12） | a12": "51869E3184F4",\\r\\n   "new_sha12": " ⏎ `D8AC8D85ACFD` ⏎ AC8D85ACFD",\\r\\n   "git_sha1": "b891bb4004c6eb | **非 D 族（哈希指纹）** | `F12` | E3 |
| 179 | `results/_r2_build_manifest_2026_10_12.json` | 470 | 18 | `D2` | `D2F7CC2CA41E`（12） | a12": "59D8F56347D5",\\r\\n   "new_sha12": " ⏎ `D2F7CC2CA41E` ⏎ F7CC2CA41E",\\r\\n   "git_sha1": "53fa9d2e5398e0 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 180 | `results/_r2_build_manifest_2026_10_12.json` | 590 | 19 | `D427` | `D427B2F57C33`（12） | r\\n   "bytes": 6325,\\r\\n   "orig_sha12": " ⏎ `D427B2F57C33` ⏎ B2F57C33",\\r\\n   "new_sha12": "9162BA7BDA63",\\ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 181 | `results/_r2_build_manifest_2026_10_12.json` | 607 | 18 | `D48` | `D48BD212BFF5`（12） | a12": "900DA300D11E",\\r\\n   "new_sha12": " ⏎ `D48BD212BFF5` ⏎ BD212BFF5",\\r\\n   "git_sha1": "0e3f19a48a69f2f | **非 D 族（哈希指纹）** | `F12` | E3 |
| 182 | `results/_r2_build_manifest_2026_10_12.json` | 876 | 18 | `D4` | `D4D22A19EF78`（12） | a12": "4D06D34CB6FA",\\r\\n   "new_sha12": " ⏎ `D4D22A19EF78` ⏎ D22A19EF78",\\r\\n   "git_sha1": "dc9183d827254e | **非 D 族（哈希指纹）** | `F12` | E3 |
| 183 | `results/_r2_build_manifest_2026_10_12.json` | 926 | 18 | `D5` | `D5DD6AFFE808`（12） | a12": "37E97E1E7B7F",\\r\\n   "new_sha12": " ⏎ `D5DD6AFFE808` ⏎ DD6AFFE808",\\r\\n   "git_sha1": "04b5307e13926a | **非 D 族（哈希指纹）** | `F12` | E3 |
| 184 | `results/_r2_build_manifest_2026_10_12.json` | 1216 | 19 | `D42` | `D42EA1FA61F1`（12） | \\n   "bytes": 17576,\\r\\n   "orig_sha12": " ⏎ `D42EA1FA61F1` ⏎ EA1FA61F1",\\r\\n   "new_sha12": "7FF365D372EF", | **非 D 族（哈希指纹）** | `F256` | E1 |
| 185 | `results/_r2_build_manifest_2026_10_12.json` | 1297 | 19 | `D8` | `D8F2B99AA527`（12） | r\\n   "bytes": 7639,\\r\\n   "orig_sha12": " ⏎ `D8F2B99AA527` ⏎ F2B99AA527",\\r\\n   "new_sha12": "1939BD5DA027" | **非 D 族（哈希指纹）** | `F256` | E1 |
| 186 | `results/_r2_build_manifest_2026_10_12.json` | 1583 | 18 | `D7` | `D7E965B0AFFE`（12） | a12": "DA517C115F3C",\\r\\n   "new_sha12": " ⏎ `D7E965B0AFFE` ⏎ E965B0AFFE",\\r\\n   "git_sha1": "2a9a263e2ffcfa | **非 D 族（哈希指纹）** | `F12` | E3 |
| 187 | `results/_r2_build_manifest_2026_10_12.json` | 1712 | 19 | `D5` | `D5E74A98C44B`（12） | \\n   "bytes": 35425,\\r\\n   "orig_sha12": " ⏎ `D5E74A98C44B` ⏎ E74A98C44B",\\r\\n   "new_sha12": "231CC88653B9" | **非 D 族（哈希指纹）** | `F12` | E3 |
| 188 | `results/_r2_build_manifest_2026_10_12.json` | 2178 | 19 | `D78` | `D78BE896BCB6`（12） | \\n   "bytes": 47526,\\r\\n   "orig_sha12": " ⏎ `D78BE896BCB6` ⏎ BE896BCB6",\\r\\n   "new_sha12": "F62F7F0F2DD0", | **非 D 族（哈希指纹）** | `F12` | E3 |
| 189 | `results/_r2_build_manifest_2026_10_12.json` | 2303 | 19 | `D5` | `D5FFFE6A5E79`（12） | \\n   "bytes": 53125,\\r\\n   "orig_sha12": " ⏎ `D5FFFE6A5E79` ⏎ FFFE6A5E79",\\r\\n   "new_sha12": "D5FFFE6A5E79" | **非 D 族（哈希指纹）** | `F12` | E3 |
| 190 | `results/_r2_build_manifest_2026_10_12.json` | 2304 | 18 | `D5` | `D5FFFE6A5E79`（12） | a12": "D5FFFE6A5E79",\\r\\n   "new_sha12": " ⏎ `D5FFFE6A5E79` ⏎ FFFE6A5E79",\\r\\n   "git_sha1": "c9422fa9e7ed95 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 191 | `results/_r2_build_manifest_2026_10_12.json` | 2422 | 19 | `D7` | `D7F03FDE4067`（12） | r\\n   "bytes": 6437,\\r\\n   "orig_sha12": " ⏎ `D7F03FDE4067` ⏎ F03FDE4067",\\r\\n   "new_sha12": "C1B275B56D47" | **非 D 族（哈希指纹）** | `F12` | E3 |
| 192 | `results/_r2_build_manifest_2026_10_12.json` | 2710 | 18 | `D93` | `D93A959D4E66`（12） | a12": "8F5136E176B8",\\r\\n   "new_sha12": " ⏎ `D93A959D4E66` ⏎ A959D4E66",\\r\\n   "git_sha1": "461124b1c8bb73d | **非 D 族（哈希指纹）** | `F12` | E3 |
| 193 | `results/_r2_build_manifest_2026_10_12.json` | 2835 | 18 | `D6` | `D6B94CABF03E`（12） | a12": "DE274BD38955",\\r\\n   "new_sha12": " ⏎ `D6B94CABF03E` ⏎ B94CABF03E",\\r\\n   "git_sha1": "6ee482285e7862 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 194 | `results/_r2_build_manifest_2026_10_12.json` | 3030 | 19 | `D87` | `D87C0327A6FB`（12） | r\\n   "bytes": 8352,\\r\\n   "orig_sha12": " ⏎ `D87C0327A6FB` ⏎ C0327A6FB",\\r\\n   "new_sha12": "8947DC572E8B", | **非 D 族（哈希指纹）** | `F12` | E3 |
| 195 | `results/_r2_build_manifest_2026_10_12.json` | 3139 | 19 | `D8` | `D8BD9C41194A`（12） | r\\n   "bytes": 7477,\\r\\n   "orig_sha12": " ⏎ `D8BD9C41194A` ⏎ BD9C41194A",\\r\\n   "new_sha12": "3018608ADC5C" | **非 D 族（哈希指纹）** | `F256` | E1 |
| 196 | `results/_r2_build_manifest_2026_10_12.json` | 3409 | 19 | `D6` | `D6FF041A9DF9`（12） | n   "bytes": 116508,\\r\\n   "orig_sha12": " ⏎ `D6FF041A9DF9` ⏎ FF041A9DF9",\\r\\n   "new_sha12": "6AF84D148366" | **非 D 族（哈希指纹）** | `F256` | E1 |
| 197 | `results/_r2_build_manifest_2026_10_12.json` | 4163 | 18 | `D4` | `D4B4B2D77117`（12） | a12": "08D3BFD82235",\\r\\n   "new_sha12": " ⏎ `D4B4B2D77117` ⏎ B4B2D77117",\\r\\n   "git_sha1": "1631ae2d677770 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 198 | `results/_r2_build_manifest_2026_10_12.json` | 4207 | 19 | `D048` | `D048A6DE1DEA`（12） | \\n   "bytes": 33152,\\r\\n   "orig_sha12": " ⏎ `D048A6DE1DEA` ⏎ A6DE1DEA",\\r\\n   "new_sha12": "93D65A5DBBAA",\\ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 199 | `results/_r2_build_manifest_2026_10_12.json` | 4373 | 18 | `D9` | `D9C9221380C4`（12） | a12": "82C5C143134E",\\r\\n   "new_sha12": " ⏎ `D9C9221380C4` ⏎ C9221380C4",\\r\\n   "git_sha1": "141f9a6f7450e7 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 200 | `results/_r2_build_manifest_2026_10_12.json` | 4478 | 18 | `D85` | `D85A5A00258B`（12） | a12": "83109ECF440E",\\r\\n   "new_sha12": " ⏎ `D85A5A00258B` ⏎ A5A00258B",\\r\\n   "git_sha1": "262ac921c4b02f6 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 201 | `results/_r2_build_manifest_2026_10_12.json` | 4897 | 19 | `D02` | `D02EC6B0987E`（12） | \\n   "bytes": 42043,\\r\\n   "orig_sha12": " ⏎ `D02EC6B0987E` ⏎ EC6B0987E",\\r\\n   "new_sha12": "1078678800DA", | **非 D 族（哈希指纹）** | `F12` | E3 |
| 202 | `results/_r2_build_manifest_2026_10_12.json` | 5917 | 19 | `D5` | `D5BF826278CB`（12） | \\n   "bytes": 35862,\\r\\n   "orig_sha12": " ⏎ `D5BF826278CB` ⏎ BF826278CB",\\r\\n   "new_sha12": "D1B0587072D3" | **非 D 族（哈希指纹）** | `F12` | E3 |
| 203 | `results/_r2_build_manifest_2026_10_12.json` | 5918 | 18 | `D1` | `D1B0587072D3`（12） | a12": "D5BF826278CB",\\r\\n   "new_sha12": " ⏎ `D1B0587072D3` ⏎ B0587072D3",\\r\\n   "git_sha1": "734fc54ea746fa | **非 D 族（哈希指纹）** | `F12` | E3 |
| 204 | `results/_r2_build_manifest_2026_10_12.json` | 6397 | 19 | `D486` | `D486EC491E8E`（12） | \\n   "bytes": 41120,\\r\\n   "orig_sha12": " ⏎ `D486EC491E8E` ⏎ EC491E8E",\\r\\n   "new_sha12": "5EF526AE564B",\\ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 205 | `results/_r2_build_manifest_2026_10_12.json` | 6413 | 18 | `D1` | `D1F0A0BC1925`（12） | a12": "CE0B5A64CFCE",\\r\\n   "new_sha12": " ⏎ `D1F0A0BC1925` ⏎ F0A0BC1925",\\r\\n   "git_sha1": "b5cb510206f3f4 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 206 | `results/_r2_build_manifest_2026_10_12.json` | 6833 | 18 | `D10` | `D10D93B86443`（12） | a12": "B84F5AAB6FAF",\\r\\n   "new_sha12": " ⏎ `D10D93B86443` ⏎ D93B86443",\\r\\n   "git_sha1": "dfeda739c97f35c | **非 D 族（哈希指纹）** | `F12` | E3 |
| 207 | `results/_r2_build_manifest_2026_10_12.json` | 7057 | 19 | `D47` | `D47B5E067C1C`（12） | \\n   "bytes": 19678,\\r\\n   "orig_sha12": " ⏎ `D47B5E067C1C` ⏎ B5E067C1C",\\r\\n   "new_sha12": "33D16F5EC7A6", | **非 D 族（哈希指纹）** | `F12` | E3 |
| 208 | `results/_r2_build_manifest_2026_10_12.json` | 7106 | 18 | `D0` | `D0F91D7499A2`（12） | a12": "5A27C2350036",\\r\\n   "new_sha12": " ⏎ `D0F91D7499A2` ⏎ F91D7499A2",\\r\\n   "git_sha1": "8764166830d0cf | **非 D 族（哈希指纹）** | `F12` | E3 |
| 209 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 130 | 62 | `D76` | `D76BA2297D0D`（12） | cope_estimand_judgments_2026_10_09.md' \| ' ⏎ `D76BA2297D0D` ⏎ BA2297D0D' \| 37682 \| 2026-10-09 17:34:04 \| 终判/ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 210 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 141 | 45 | `D048` | `D048A6DE1DEA`（12） | 'results\\_cleanup_round_2026_10_08.md' \| ' ⏎ `D048A6DE1DEA` ⏎ A6DE1DEA' \| 33179 \| 2026-10-08 18:25:13 \| 读数/结 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 211 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 232 | 59 | `D78` | `D78BE896BCB6`（12） | otten_recovery_register_2026_09_29.md' \| ' ⏎ `D78BE896BCB6` ⏎ BE896BCB6' \| 47494 \| 2026-09-29 21:39:46 \| 登记＋ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 212 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 304 | 55 | `D02` | `D02EC6B0987E`（12） | kj1_abc_choice_judgment_2026_10_11.md' \| ' ⏎ `D02EC6B0987E` ⏎ EC6B0987E' \| 42083 \| 2026-10-11 15:02:27 \| 终判/ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 213 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 344 | 63 | `D5` | `D5FFFE6A5E79`（12） | nd_5_decisions_register_2026_10_01.md' \| ' ⏎ `D5FFFE6A5E79` ⏎ FFFE6A5E79' \| 53125 \| 2026-10-10 11:37:23 \| 登记 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 214 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 403 | 80 | `D6` | `D6FF041A9DF9`（12） | e_register_supplement_4_2026_10_10.md' \| ' ⏎ `D6FF041A9DF9` ⏎ FF041A9DF9' \| 116506 \| 2026-10-10 10:54:25 \| 登 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 215 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 415 | 71 | `D8` | `D8D5E4D2154F`（12） | it_full_document_review_2026_10_09.md' \| ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' \| 28176 \| 2026-10-09 22:32:22 \| 评审 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 216 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 437 | 68 | `D0` | `D0BC0B1A9AE0`（12） | provals_effect_register_2026_10_10.md' \| ' ⏎ `D0BC0B1A9AE0` ⏎ BC0B1A9AE0' \| 73226 \| 2026-10-10 11:02:09 \| 登记 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 217 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 438 | 68 | `D66` | `D66A1076952A`（12） | sitions_effect_register_2026_10_10.md' \| ' ⏎ `D66A1076952A` ⏎ A1076952A' \| 19803 \| 2026-10-10 14:11:43 \| 登记＋ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 218 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 465 | 78 | `D5` | `D5BF826278CB`（12） | ry_effectivity_register_2026_10_10.md' \| ' ⏎ `D5BF826278CB` ⏎ BF826278CB' \| 35878 \| 2026-10-10 18:48:25 \| 登记 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 219 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 511 | 66 | `D044` | `D044CE1C069D`（12） | surface_v3_1_definition_2026_10_10.md' \| ' ⏎ `D044CE1C069D` ⏎ CE1C069D' \| 30310 \| 2026-10-10 11:10:18 \| 读数/结 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 220 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 601 | 72 | `D486` | `D486EC491E8E`（12） | er_unification_register_2026_10_11.md' \| ' ⏎ `D486EC491E8E` ⏎ EC491E8E' \| 41140 \| 2026-10-11 14:41:24 \| 登记＋读 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 221 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 615 | 49 | `D90` | `D90BF82338F6`（12） | ults\\_t1_7_2_correction_2026_10_08.md' \| ' ⏎ `D90BF82338F6` ⏎ BF82338F6' \| 16469 \| 2026-10-10 11:37:23 \| 勘误＋ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 222 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 621 | 48 | `D9` | `D9CCD75C652B`（12） | sults\\_t1_exp2_result_2026_10_09.json' \| ' ⏎ `D9CCD75C652B` ⏎ CCD75C652B' \| 35239 \| 2026-10-10 02:33:06 \| 读数 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 223 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 648 | 62 | `D9` | `D9D29BEC3A0B`（12） | dgment_bytes_correction_2026_10_10.md' \| ' ⏎ `D9D29BEC3A0B` ⏎ D29BEC3A0B' \| 6377 \| 2026-10-10 00:31:40 \| 终判/ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 224 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 660 | 38 | `D80` | `D80A8F75A122`（12） | 面 \|\\n\| 'results\\_tra_v0_2026_09_10.py' \| ' ⏎ `D80A8F75A122` ⏎ A8F75A122' \| 12125 \| 2026-09-10 20:20:20 \| 读数/ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 225 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 706 | 54 | `D6` | `D6C8BC163E11`（12） | _v3_recheck_05_executor_2026_09_28.py' \| ' ⏎ `D6C8BC163E11` ⏎ C8BC163E11' \| 38639 \| 2026-09-28 13:27:45 \| 核查 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 226 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 762 | 59 | `D9` | `D9B6B974CFC1`（12） | echeck_verdict_register_2026_09_27.md' \| ' ⏎ `D9B6B974CFC1` ⏎ B6B974CFC1' \| 112085 \| 2026-09-30 16:15:20 \| 登 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 227 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 764 | 72 | `D42` | `D42EA1FA61F1`（12） | te_preexp_data\\rescript_2026_09_27.md' \| ' ⏎ `D42EA1FA61F1` ⏎ EA1FA61F1' \| 17574 \| 2026-10-12 01:30:19 \| 论文/ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 228 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 773 | 55 | `D73` | `D73D51E670DE`（12） | v3_s2_executor\\result_2026_09_27.json' \| ' ⏎ `D73D51E670DE` ⏎ D51E670DE' \| 51039 \| 2026-09-27 16:05:12 \| 读数/ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 229 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 774 | 54 | `D5` | `D5BA1161E37F`（12） | _v3_s3_collection_brief_2026_09_28.md' \| ' ⏎ `D5BA1161E37F` ⏎ BA1161E37F' \| 19045 \| 2026-09-28 13:38:11 \| 读数 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 230 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 798 | 62 | `D8` | `D8F2B99AA527`（12） | 5_experiment_invitation_2026_09_17.md' \| ' ⏎ `D8F2B99AA527` ⏎ F2B99AA527' \| 7617 \| 2026-09-17 09:34:32 \| 委托＋ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 231 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 851 | 67 | `D96` | `D96B747BFC6C`（12） | _dataset_addendum_d3b_2026_09_26.json' \| ' ⏎ `D96B747BFC6C` ⏎ B747BFC6C' \| 14722 \| 2026-09-26 18:18:19 \| 读数/ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 232 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 909 | 54 | `D4` | `D4DD5C949443`（12） | _v4_supp_l14v3_batch10_r1_executor.py' \| ' ⏎ `D4DD5C949443` ⏎ DD5C949443' \| 56894 \| 2026-09-26 16:32:01 \| 读数 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 233 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 920 | 53 | `D245` | `D245AE4CE385`（12） | \\_v4_supp_l14v3_batch2_r1_result.json' \| ' ⏎ `D245AE4CE385` ⏎ AE4CE385' \| 4128 \| 2026-09-24 22:35:43 \| 读数/结果 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 234 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 930 | 53 | `D9` | `D9FE7AA2D292`（12） | \\_v4_supp_l14v3_batch2_r4_executor.py' \| ' ⏎ `D9FE7AA2D292` ⏎ FE7AA2D292' \| 58176 \| 2026-09-24 23:26:12 \| 读数 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 235 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 937 | 53 | `D24` | `D24B84671C23`（12） | \\_v4_supp_l14v3_batch3_r1_result.json' \| ' ⏎ `D24B84671C23` ⏎ B84671C23' \| 66520 \| 2026-09-24 23:38:45 \| 读数/ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 236 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 982 | 51 | `D339` | `D339D7286AD8`（12） | ts\\_v4_supp_l14v3_batch6_r5_report.md' \| ' ⏎ `D339D7286AD8` ⏎ D7286AD8' \| 8596 \| 2026-09-25 02:08:01 \| 读数/结果 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 237 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 990 | 53 | `D789` | `D789F9BD4FA1`（12） | \\_v4_supp_l14v3_batch7_r4_executor.py' \| ' ⏎ `D789F9BD4FA1` ⏎ F9BD4FA1' \| 51289 \| 2026-09-25 03:06:20 \| 读数/结 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 238 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 1025 | 40 | `D6` | `D6CB03A4657E`（12） | \|\\n\| 'results\\_v4_supp_t1_result.json' \| ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' \| 82365 \| 2026-09-24 22:32:37 \| 读数 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 239 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 1169 | 52 | `D37` | `D37E97644BF8`（12） | s\\_v5_loadcorpus_switch_2026_09_29.md' \| ' ⏎ `D37E97644BF8` ⏎ E97644BF8' \| 16414 \| 2026-09-29 12:13:38 \| 读数/ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 240 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 1182 | 54 | `D5` | `D5FDB89582FD`（12） | _v5_pl2_fourband_prereg_2026_09_29.md' \| ' ⏎ `D5FDB89582FD` ⏎ FDB89582FD' \| 29253 \| 2026-09-29 17:42:35 \| 读数 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 241 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 1203 | 59 | `D34` | `D34B46E24A7C`（12） | rack2_qwen_retry_executor_20260929.py' \| ' ⏎ `D34B46E24A7C` ⏎ B46E24A7C' \| 11586 \| 2026-09-29 11:10:20 \| 读数/ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 242 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 1219 | 51 | `D687` | `D687AD25A68C`（12） | ts\\_v5_v3r2_errata_note_2026_09_29.md' \| ' ⏎ `D687AD25A68C` ⏎ AD25A68C' \| 29089 \| 2026-09-29 20:12:47 \| 勘误＋读 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 243 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 1235 | 69 | `D6` | `D6F233D73C45`（12） | cator_dynamics_result_2026_09_15.json' \| ' ⏎ `D6F233D73C45` ⏎ F233D73C45' \| 9098 \| 2026-09-15 15:28:10 \| 读数/ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 244 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 1240 | 54 | `D74` | `D74D6B39D1B0`（12） | boss_pc_3_a3_clipping_2026_09_15.json' \| ' ⏎ `D74D6B39D1B0` ⏎ D6B39D1B0' \| 1265 \| 2026-09-15 13:34:48 \| 读数/结 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 245 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 1254 | 55 | `D87` | `D87C0327A6FB`（12） | eposon_3risk_v0_fixes_2026_09_11.json' \| ' ⏎ `D87C0327A6FB` ⏎ C0327A6FB' \| 8338 \| 2026-09-11 17:16:56 \| 读数/结 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 246 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 1367 | 56 | `D301` | `D301BBFED982`（12） | poson_v3x_6way_stage2_2026_09_10.json' \| ' ⏎ `D301BBFED982` ⏎ BBFED982' \| 2741 \| 2026-09-10 17:56:17 \| 读数/结果 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 247 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 1368 | 56 | `D892` | `D892A9D3D6BA`（12） | poson_v3x_6way_stage3_2026_09_10.json' \| ' ⏎ `D892A9D3D6BA` ⏎ A9D3D6BA' \| 15943 \| 2026-09-10 18:15:22 \| 读数/结 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 248 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 1461 | 65 | `D39` | `D39CB17B051B`（12） | ation_reply_claude_code_2026_09_20.md' \| ' ⏎ `D39CB17B051B` ⏎ CB17B051B' \| 64212 \| 2026-09-21 11:01:14 \| 回函＋ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 249 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 1518 | 38 | `D4` | `D4ED18152DC0`（12） | 面 \|\\n\| 'docs\\Findings_v2.0_bigquiz.md' \| ' ⏎ `D4ED18152DC0` ⏎ ED18152DC0' \| 3291 \| 2026-08-28 23:55:23 \| 文档面 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 250 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 1563 | 47 | `D74` | `D74E1534493E`（12） | ocs\\V3X\\BPA_PILOT_2026_09_09_mavis.md' \| ' ⏎ `D74E1534493E` ⏎ E1534493E' \| 6864 \| 2026-09-09 13:39:22 \| 文档面  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 251 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 1592 | 52 | `D427` | `D427B2F57C33`（12） | 3X\\P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md' \| ' ⏎ `D427B2F57C33` ⏎ B2F57C33' \| 6301 \| 2026-09-08 16:03:54 \| 文档面 \| | **非 D 族（哈希指纹）** | `F256` | E1 |
| 252 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 1655 | 27 | `D76` | `D76F2DC473BE`（12） | 门＋核查＋执行体＋验证面 \|\\n\| 'verifier\\README.md' \| ' ⏎ `D76F2DC473BE` ⏎ F2DC473BE' \| 14360 \| 2026-08-30 17:08:56 \| 核查＋ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 253 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 1702 | 34 | `D9` | `D9BFAAE6D08B`（12） | 查＋验证面 \|\\n\| 'verifier\\runs\\v34_run2.md' \| ' ⏎ `D9BFAAE6D08B` ⏎ BFAAE6D08B' \| 118 \| 2026-08-30 14:13:30 \| 核查＋验 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 254 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 1748 | 30 | `D48` | `D48AC555761F`（12） | 查＋执行体＋验证面 \|\\n\| 'verifier\\v39\\check.sh' \| ' ⏎ `D48AC555761F` ⏎ AC555761F' \| 1935 \| 2026-09-17 23:20:53 \| 核查＋执 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 255 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 1772 | 48 | `D511` | `D511C545F88E`（12） | poson_team\\plugins\\_pg_v01_compute.py' \| ' ⏎ `D511C545F88E` ⏎ C545F88E' \| 20923 \| 2026-09-16 18:54:48 \| 执行体＋ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 256 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 1775 | 52 | `D8` | `D8BD9C41194A`（12） | n_team\\plugins\\_tdf_s1c_2026_10_12.py' \| ' ⏎ `D8BD9C41194A` ⏎ BD9C41194A' \| 7485 \| 2026-10-12 01:26:27 \| 执行体 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 257 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 1788 | 61 | `D3` | `D3B45B64C0DA`（12） | ugins\\_v3_review_r3_sha_2026_09_23.py' \| ' ⏎ `D3B45B64C0DA` ⏎ B45B64C0DA' \| 1881 \| 2026-09-23 13:26:41 \| 评审＋ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 258 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 1890 | 81 | `D2` | `D2CD7ACB29A1`（12） | merkle_22caption_runner_2026_09_16.py' \| ' ⏎ `D2CD7ACB29A1` ⏎ CD7ACB29A1' \| 18596 \| 2026-09-16 18:54:48 \| 执行 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 259 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 1924 | 41 | `D0` | `D0BBA9379B4B`（12） | \\n\| 'reviews\\literature_scan_v2X_A.md' \| ' ⏎ `D0BBA9379B4B` ⏎ BBA9379B4B' \| 18876 \| 2026-08-28 21:42:49 \| 核查 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 260 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2003 | 28 | `D11` | `D11E085D9ECC`（12） | -\|-:\|:--\|:--\|\\n\| 'attacks\\__init__.py' \| ' ⏎ `D11E085D9ECC` ⏎ E085D9ECC' \| 183 \| 2026-09-01 11:19:18 \| 执行体＋攻 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 261 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2226 | 94 | `D42` | `D42EA1FA61F1`（12） | te_preexp_data\\rescript_2026_09_27.md' \| ' ⏎ `D42EA1FA61F1` ⏎ EA1FA61F1' \| 17574 \|\\n\| 2026-10-12 01:30:19 \|  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 262 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2231 | 74 | `D8` | `D8BD9C41194A`（12） | n_team\\plugins\\_tdf_s1c_2026_10_12.py' \| ' ⏎ `D8BD9C41194A` ⏎ BD9C41194A' \| 7485 \|\\n\| 2026-10-12 01:24:29 \|  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 263 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2313 | 77 | `D02` | `D02EC6B0987E`（12） | kj1_abc_choice_judgment_2026_10_11.md' \| ' ⏎ `D02EC6B0987E` ⏎ EC6B0987E' \| 42083 \|\\n\| 2026-10-11 14:59:46 \|  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 264 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2317 | 94 | `D486` | `D486EC491E8E`（12） | er_unification_register_2026_10_11.md' \| ' ⏎ `D486EC491E8E` ⏎ EC491E8E' \| 41140 \|\\n\| 2026-10-11 14:36:37 \| ' | **非 D 族（哈希指纹）** | `F12` | E3 |
| 265 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2420 | 100 | `D5` | `D5BF826278CB`（12） | ry_effectivity_register_2026_10_10.md' \| ' ⏎ `D5BF826278CB` ⏎ BF826278CB' \| 35878 \|\\n\| 2026-10-10 18:44:20 \| | **非 D 族（哈希指纹）** | `F12` | E3 |
| 266 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2501 | 90 | `D66` | `D66A1076952A`（12） | sitions_effect_register_2026_10_10.md' \| ' ⏎ `D66A1076952A` ⏎ A1076952A' \| 19803 \|\\n\| 2026-10-10 14:09:06 \|  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 267 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2612 | 71 | `D90` | `D90BF82338F6`（12） | ults\\_t1_7_2_correction_2026_10_08.md' \| ' ⏎ `D90BF82338F6` ⏎ BF82338F6' \| 16469 \|\\n\| 2026-10-10 11:37:23 \|  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 268 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2615 | 85 | `D5` | `D5FFFE6A5E79`（12） | nd_5_decisions_register_2026_10_01.md' \| ' ⏎ `D5FFFE6A5E79` ⏎ FFFE6A5E79' \| 53125 \|\\n\| 2026-10-10 11:37:23 \| | **非 D 族（哈希指纹）** | `F12` | E3 |
| 269 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2629 | 88 | `D044` | `D044CE1C069D`（12） | surface_v3_1_definition_2026_10_10.md' \| ' ⏎ `D044CE1C069D` ⏎ CE1C069D' \| 30310 \|\\n\| 2026-10-10 11:06:34 \| ' | **非 D 族（哈希指纹）** | `F12` | E3 |
| 270 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2631 | 90 | `D0` | `D0BC0B1A9AE0`（12） | provals_effect_register_2026_10_10.md' \| ' ⏎ `D0BC0B1A9AE0` ⏎ BC0B1A9AE0' \| 73226 \|\\n\| 2026-10-10 10:59:49 \| | **非 D 族（哈希指纹）** | `F12` | E3 |
| 271 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2638 | 102 | `D6` | `D6FF041A9DF9`（12） | e_register_supplement_4_2026_10_10.md' \| ' ⏎ `D6FF041A9DF9` ⏎ FF041A9DF9' \| 116506 \|\\n\| 2026-10-10 10:51:43  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 272 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2682 | 70 | `D9` | `D9CCD75C652B`（12） | sults\\_t1_exp2_result_2026_10_09.json' \| ' ⏎ `D9CCD75C652B` ⏎ CCD75C652B' \| 35239 \|\\n\| 2026-10-10 02:31:56 \| | **非 D 族（哈希指纹）** | `F256` | E1 |
| 273 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2686 | 65 | `D0` | `D0AACA46B41A`（12） | \| '.tmp\\_t1_exp2_c_driver_stdout3.log' \| ' ⏎ `D0AACA46B41A` ⏎ AACA46B41A' \| 9376 \|\\n\| 2026-10-10 01:25:59 \|  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 274 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2704 | 84 | `D9` | `D9D29BEC3A0B`（12） | dgment_bytes_correction_2026_10_10.md' \| ' ⏎ `D9D29BEC3A0B` ⏎ D29BEC3A0B' \| 6377 \|\\n\| 2026-10-10 00:31:15 \|  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 275 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2741 | 93 | `D8` | `D8D5E4D2154F`（12） | it_full_document_review_2026_10_09.md' \| ' ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F' \| 28176 \|\\n\| 2026-10-09 22:30:43 \| | **非 D 族（哈希指纹）** | `F12` | E3 |
| 276 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2752 | 58 | `D929` | `D929EB9AE0B8`（12） | :19:29 \| '.tmp\\_t1_exp2_selfcert.json' \| ' ⏎ `D929EB9AE0B8` ⏎ EB9AE0B8' \| 6780 \|\\n\| 2026-10-09 22:17:22 \| 'r | **非 D 族（哈希指纹）** | `F256` | E1 |
| 277 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2761 | 52 | `D9` | `D9A4F1898C31`（12） | -09 21:53:50 \| '.tmp\\_probe_schema.py' \| ' ⏎ `D9A4F1898C31` ⏎ A4F1898C31' \| 583 \|\\n\| 2026-10-09 21:53:15 \| ' | **非 D 族（哈希指纹）** | `F12` | E3 |
| 278 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2815 | 84 | `D76` | `D76BA2297D0D`（12） | cope_estimand_judgments_2026_10_09.md' \| ' ⏎ `D76BA2297D0D` ⏎ BA2297D0D' \| 37682 \|\\n\| 2026-10-09 17:33:46 \|  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 279 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2941 | 53 | `D65` | `D65F18FFB59A`（12） | 09 14:16:26 \| '.tmp\\_rp4_probe_r7c.py' \| ' ⏎ `D65F18FFB59A` ⏎ F18FFB59A' \| 643 \|\\n\| 2026-10-09 14:16:15 \| '. | **非 D 族（哈希指纹）** | `F12` | E3 |
| 280 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2964 | 57 | `D925` | `D925E60C1D3C`（12） | 4:00:32 \| '.tmp\\_vk_pv02_recheck_e.py' \| ' ⏎ `D925E60C1D3C` ⏎ E60C1D3C' \| 1742 \|\\n\| 2026-10-09 14:00:06 \| '. | **非 D 族（哈希指纹）** | `F256` | E1 |
| 281 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 2966 | 66 | `D74` | `D74E9AE8CD3A`（12） |  '.tmp\\_vk_baxis_probe_2026_10_09.txt' \| ' ⏎ `D74E9AE8CD3A` ⏎ E9AE8CD3A' \| 5156 \|\\n\| 2026-10-09 13:59:55 \| ' | **非 D 族（哈希指纹）** | `F12` | E3 |
| 282 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3014 | 74 | `D6` | `D6DCCC069511`（12） | k_v3df_0_1_verify_out_2026_10_09.json' \| ' ⏎ `D6DCCC069511` ⏎ DCCC069511' \| 30845 \|\\n\| 2026-10-09 12:00:28 \| | **非 D 族（哈希指纹）** | `F12` | E3 |
| 283 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3143 | 30 | `D48` | `D48AC555761F`（12） | D' \| 1705 \|\\n\| 'verifier\\v39\\check.sh' \| ' ⏎ `D48AC555761F` ⏎ AC555761F' \| 1935 \|\\n\| 'verifier\\v40\\check.sh' | **非 D 族（哈希指纹）** | `F256` | E1 |
| 284 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3171 | 27 | `D76` | `D76F2DC473BE`（12） | 06A5' \| 7279 \|\\n\| 'verifier\\README.md' \| ' ⏎ `D76F2DC473BE` ⏎ F2DC473BE' \| 14360 \|\\n\\n**rescript_2026_09_27. | **非 D 族（哈希指纹）** | `F256` | E1 |
| 285 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3179 | 72 | `D42` | `D42EA1FA61F1`（12） | te_preexp_data\\rescript_2026_09_27.md' \| ' ⏎ `D42EA1FA61F1` ⏎ EA1FA61F1' \| 17574 \|\\n\| 'results\\_v3_s1_execut | **非 D 族（哈希指纹）** | `F256` | E1 |
| 286 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3191 | 55 | `D73` | `D73D51E670DE`（12） | v3_s2_executor\\result_2026_09_27.json' \| ' ⏎ `D73D51E670DE` ⏎ D51E670DE' \| 51039 \|\\n\\n**test_write.txt** ——  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 287 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3292 | 30 | `D9` | `D9A4F1898C31`（12） | \| 944 \| 1 \|\\n\| '.tmp\\_probe_schema.py' \| ' ⏎ `D9A4F1898C31` ⏎ A4F1898C31' \| 583 \| 1 \|\\n\| '.tmp\\_probe21.py'  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 288 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3306 | 31 | `D65` | `D65F18FFB59A`（12） |  453 \| 1 \|\\n\| '.tmp\\_rp4_probe_r7c.py' \| ' ⏎ `D65F18FFB59A` ⏎ F18FFB59A' \| 643 \| 1 \|\\n\| '.tmp\\_run_output.lo | **非 D 族（哈希指纹）** | `F12` | E3 |
| 289 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3372 | 35 | `D925` | `D925E60C1D3C`（12） |  \| 1 \|\\n\| '.tmp\\_vk_pv02_recheck_e.py' \| ' ⏎ `D925E60C1D3C` ⏎ E60C1D3C' \| 1742 \| 1 \|\\n\| '.tmp\\_vk_pv02_reche | **非 D 族（哈希指纹）** | `F256` | E1 |
| 290 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3468 | 30 | `D9` | `D9A4F1898C31`（12） | 1558 \| 16 \|\\n\| '.tmp\\_probe_schema.py' \| ' ⏎ `D9A4F1898C31` ⏎ A4F1898C31' \| 583 \| 1 \|\\n\| '.tmp\\_probe21.py'  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 291 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3491 | 31 | `D65` | `D65F18FFB59A`（12） |  453 \| 1 \|\\n\| '.tmp\\_rp4_probe_r7c.py' \| ' ⏎ `D65F18FFB59A` ⏎ F18FFB59A' \| 643 \| 1 \|\\n\| '.tmp\\_run_output.lo | **非 D 族（哈希指纹）** | `F12` | E3 |
| 292 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3533 | 43 | `D0` | `D0AACA46B41A`（12） | \| '.tmp\\_t1_exp2_c_driver_stdout3.log' \| ' ⏎ `D0AACA46B41A` ⏎ AACA46B41A' \| 9376 \| 72 \|\\n\| '.tmp\\_t1_exp2_c_ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 293 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3560 | 44 | `D74` | `D74E9AE8CD3A`（12） |  '.tmp\\_vk_baxis_probe_2026_10_09.txt' \| ' ⏎ `D74E9AE8CD3A` ⏎ E9AE8CD3A' \| 5156 \| 38 \|\\n\| '.tmp\\_vk_dualread | **非 D 族（哈希指纹）** | `F12` | E3 |
| 294 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3567 | 35 | `D925` | `D925E60C1D3C`（12） |  \| 1 \|\\n\| '.tmp\\_vk_pv02_recheck_e.py' \| ' ⏎ `D925E60C1D3C` ⏎ E60C1D3C' \| 1742 \| 1 \|\\n\| '.tmp\\_vk_pv02_reche | **非 D 族（哈希指纹）** | `F256` | E1 |
| 295 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3601 | 81 | `D2` | `D2CD7ACB29A1`（12） | merkle_22caption_runner_2026_09_16.py' \| ' ⏎ `D2CD7ACB29A1` ⏎ CD7ACB29A1' \| 18596 \| 417 \|\\n\| 'corpus\\v20_cap | **非 D 族（哈希指纹）** | `F256` | E1 |
| 296 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3611 | 48 | `D511` | `D511C545F88E`（12） | poson_team\\plugins\\_pg_v01_compute.py' \| ' ⏎ `D511C545F88E` ⏎ C545F88E' \| 20923 \| 510 \|\\n\| 'deposon_team\\plu | **非 D 族（哈希指纹）** | `F256` | E1 |
| 297 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3640 | 65 | `D39` | `D39CB17B051B`（12） | ation_reply_claude_code_2026_09_20.md' \| ' ⏎ `D39CB17B051B` ⏎ CB17B051B' \| 64212 \| 393 \|\\n\| 'results\\__pycac | **非 D 族（哈希指纹）** | `F256` | E1 |
| 298 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3712 | 53 | `D245` | `D245AE4CE385`（12） | \\_v4_supp_l14v3_batch2_r1_result.json' \| ' ⏎ `D245AE4CE385` ⏎ AE4CE385' \| 4128 \| 101 \|\\n\| 'results\\_v4_supp_ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 299 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3721 | 53 | `D24` | `D24B84671C23`（12） | \\_v4_supp_l14v3_batch3_r1_result.json' \| ' ⏎ `D24B84671C23` ⏎ B84671C23' \| 66520 \| 1514 \|\\n\| 'results\\_v4_su | **非 D 族（哈希指纹）** | `F256` | E1 |
| 300 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3742 | 40 | `D6` | `D6CB03A4657E`（12） | \|\\n\| 'results\\_v4_supp_t1_result.json' \| ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' \| 82365 \| 2451 \|\\n\| 'results\\_v4_s | **非 D 族（哈希指纹）** | `F256` | E1 |
| 301 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3757 | 69 | `D6` | `D6F233D73C45`（12） | cator_dynamics_result_2026_09_15.json' \| ' ⏎ `D6F233D73C45` ⏎ F233D73C45' \| 9098 \| 334 \|\\n\| 'results\\boss_pc | **非 D 族（哈希指纹）** | `F256` | E1 |
| 302 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3762 | 54 | `D74` | `D74D6B39D1B0`（12） | boss_pc_3_a3_clipping_2026_09_15.json' \| ' ⏎ `D74D6B39D1B0` ⏎ D6B39D1B0' \| 1265 \| 57 \|\\n\| 'results\\boss_pc_3 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 303 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3770 | 55 | `D87` | `D87C0327A6FB`（12） | eposon_3risk_v0_fixes_2026_09_11.json' \| ' ⏎ `D87C0327A6FB` ⏎ C0327A6FB' \| 8338 \| 240 \|\\n\| 'results\\deposon_ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 304 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3824 | 56 | `D301` | `D301BBFED982`（12） | poson_v3x_6way_stage2_2026_09_10.json' \| ' ⏎ `D301BBFED982` ⏎ BBFED982' \| 2741 \| 117 \|\\n\| 'results\\deposon_v | **非 D 族（哈希指纹）** | `F12` | E3 |
| 305 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | 3825 | 56 | `D892` | `D892A9D3D6BA`（12） | poson_v3x_6way_stage3_2026_09_10.json' \| ' ⏎ `D892A9D3D6BA` ⏎ A9D3D6BA' \| 15943 \| 452 \|\\n\| 'results\\deposon_ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 306 | `results/_s4_source_wave_mapping_registration_2026_10_10.md` | 87 | 118 | `D96` | `D96B747BFC6C`（12） | 6.json' \| **'D3_w2'** \| 'd96b747bfc6c' \| ' ⏎ `D96B747BFC6C` ⏎ B747BFC6C' \| ✅ \|\\n\| 9 \| 'ADDENDUM_D3C' \| L170  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 307 | `results/_s4_substrate_grid_availability_2026_10_08.json` | 100 | 19 | `D96` | `D96B747BFC6C`（12） | _d3b_2026_09_26.json",\\n    "sha256_12": " ⏎ `D96B747BFC6C` ⏎ B747BFC6C",\\n    "bytes": 14722,\\n    "mtime_l | **非 D 族（哈希指纹）** | `F256` | E1 |
| 308 | `results/_s4_substrate_grid_availability_2026_10_08.md` | 37 | 71 | `D96` | `D96B747BFC6C`（12） | _dataset_addendum_d3b_2026_09_26.json' \| ' ⏎ `D96B747BFC6C` ⏎ B747BFC6C' \| 14,722 \| 'supplements' \| 4 \|\\n\| 9 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 309 | `results/_t1_prereg_revision_qwen_temp_sweep_2026_10_09.md` | 59 | 55 | `D6` | `D6CB03A4657E`（12） | * \| ⚠️ **部分** \| 锚件与下游 result／verdict 链在盘（' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' 82,365 B／'91B8F70E4E18' executor 6 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 310 | `results/_upload_plan_2026_10_12.json` | 287 | 14 | `D2` | `D2CD7ACB29A1`（12） | y",\\r\\n   "bytes": 18596,\\r\\n   "sha12": " ⏎ `D2CD7ACB29A1` ⏎ CD7ACB29A1",\\r\\n   "sha256_full": "d2cd7acb29a | **非 D 族（哈希指纹）** | `F256` | E1 |
| 311 | `results/_upload_plan_2026_10_12.json` | 440 | 14 | `D8` | `D8BD9C41194A`（12） | py",\\r\\n   "bytes": 7485,\\r\\n   "sha12": " ⏎ `D8BD9C41194A` ⏎ BD9C41194A",\\r\\n   "sha256_full": "d8bd9c41194 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 312 | `results/_upload_plan_2026_10_12.json` | 638 | 14 | `D4` | `D4ED18152DC0`（12） | md",\\r\\n   "bytes": 3291,\\r\\n   "sha12": " ⏎ `D4ED18152DC0` ⏎ ED18152DC0",\\r\\n   "sha256_full": "d4ed18152dc | **非 D 族（哈希指纹）** | `F256` | E1 |
| 313 | `results/_upload_plan_2026_10_12.json` | 1529 | 14 | `D6` | `D6FF041A9DF9`（12） | ",\\r\\n   "bytes": 116506,\\r\\n   "sha12": " ⏎ `D6FF041A9DF9` ⏎ FF041A9DF9",\\r\\n   "sha256_full": "d6ff041a9df | **非 D 族（哈希指纹）** | `F256` | E1 |
| 314 | `results/_upload_plan_2026_10_12.json` | 2141 | 14 | `D9` | `D9CCD75C652B`（12） | n",\\r\\n   "bytes": 35239,\\r\\n   "sha12": " ⏎ `D9CCD75C652B` ⏎ CCD75C652B",\\r\\n   "sha256_full": "d9ccd75c652 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 315 | `results/_upload_plan_2026_10_12.json` | 2852 | 14 | `D0` | `D0BBA9379B4B`（12） | d",\\r\\n   "bytes": 18876,\\r\\n   "sha12": " ⏎ `D0BBA9379B4B` ⏎ BBA9379B4B",\\r\\n   "sha256_full": "d0bba9379b4 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 316 | `results/_upload_plan_2026_10_12.json` | 3959 | 14 | `D76` | `D76BA2297D0D`（12） | d",\\r\\n   "bytes": 37682,\\r\\n   "sha12": " ⏎ `D76BA2297D0D` ⏎ BA2297D0D",\\r\\n   "sha256_full": "d76ba2297d0d | **非 D 族（哈希指纹）** | `F12` | E3 |
| 317 | `results/_upload_plan_2026_10_12.json` | 4040 | 14 | `D048` | `D048A6DE1DEA`（12） | d",\\r\\n   "bytes": 33179,\\r\\n   "sha12": " ⏎ `D048A6DE1DEA` ⏎ A6DE1DEA",\\r\\n   "sha256_full": "d048a6de1dea1 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 318 | `results/_upload_plan_2026_10_12.json` | 4904 | 14 | `D02` | `D02EC6B0987E`（12） | d",\\r\\n   "bytes": 42083,\\r\\n   "sha12": " ⏎ `D02EC6B0987E` ⏎ EC6B0987E",\\r\\n   "sha256_full": "d02ec6b0987e | **非 D 族（哈希指纹）** | `F12` | E3 |
| 319 | `results/_upload_plan_2026_10_12.json` | 5507 | 14 | `D8` | `D8D5E4D2154F`（12） | d",\\r\\n   "bytes": 28176,\\r\\n   "sha12": " ⏎ `D8D5E4D2154F` ⏎ D5E4D2154F",\\r\\n   "sha256_full": "d8d5e4d2154 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 320 | `results/_upload_plan_2026_10_12.json` | 5588 | 14 | `D0` | `D0BC0B1A9AE0`（12） | d",\\r\\n   "bytes": 73226,\\r\\n   "sha12": " ⏎ `D0BC0B1A9AE0` ⏎ BC0B1A9AE0",\\r\\n   "sha256_full": "d0bc0b1a9ae | **非 D 族（哈希指纹）** | `F12` | E3 |
| 321 | `results/_upload_plan_2026_10_12.json` | 5597 | 14 | `D66` | `D66A1076952A`（12） | d",\\r\\n   "bytes": 19803,\\r\\n   "sha12": " ⏎ `D66A1076952A` ⏎ A1076952A",\\r\\n   "sha256_full": "d66a1076952a | **非 D 族（哈希指纹）** | `F12` | E3 |
| 322 | `results/_upload_plan_2026_10_12.json` | 5840 | 14 | `D5` | `D5BF826278CB`（12） | d",\\r\\n   "bytes": 35878,\\r\\n   "sha12": " ⏎ `D5BF826278CB` ⏎ BF826278CB",\\r\\n   "sha256_full": "d5bf826278c | **非 D 族（哈希指纹）** | `F12` | E3 |
| 323 | `results/_upload_plan_2026_10_12.json` | 6083 | 14 | `D044` | `D044CE1C069D`（12） | d",\\r\\n   "bytes": 30310,\\r\\n   "sha12": " ⏎ `D044CE1C069D` ⏎ CE1C069D",\\r\\n   "sha256_full": "d044ce1c069db | **非 D 族（哈希指纹）** | `F12` | E3 |
| 324 | `results/_upload_plan_2026_10_12.json` | 6452 | 14 | `D486` | `D486EC491E8E`（12） | d",\\r\\n   "bytes": 41140,\\r\\n   "sha12": " ⏎ `D486EC491E8E` ⏎ EC491E8E",\\r\\n   "sha256_full": "d486ec491e8eb | **非 D 族（哈希指纹）** | `F12` | E3 |
| 325 | `results/_upload_plan_2026_10_12.json` | 6515 | 14 | `D90` | `D90BF82338F6`（12） | d",\\r\\n   "bytes": 16469,\\r\\n   "sha12": " ⏎ `D90BF82338F6` ⏎ BF82338F6",\\r\\n   "sha256_full": "d90bf82338f6 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 326 | `results/_upload_plan_2026_10_12.json` | 6650 | 14 | `D9` | `D9D29BEC3A0B`（12） | md",\\r\\n   "bytes": 6377,\\r\\n   "sha12": " ⏎ `D9D29BEC3A0B` ⏎ D29BEC3A0B",\\r\\n   "sha256_full": "d9d29bec3a0 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 327 | `results/_upload_plan_2026_10_12.json` | 7442 | 14 | `D47` | `D47B5E067C1C`（12） | d",\\r\\n   "bytes": 19709,\\r\\n   "sha12": " ⏎ `D47B5E067C1C` ⏎ B5E067C1C",\\r\\n   "sha256_full": "d47b5e067c1c | **非 D 族（哈希指纹）** | `F12` | E3 |
| 328 | `results/_v3_n_recheck_llm_verdict_2026_09_27.md` | 36 | 71 | `D511` | `D511C545F88E`（12） | ugins/_pg_v01_compute.py' \| ✓ \| 20,923 \| ' ⏎ `D511C545F88E` ⏎ C545F88E' \| 会话首测同值，**0 触动** \|\\n\| #19 SPEC \| 'd | **非 D 族（哈希指纹）** | `F256` | E1 |
| 329 | `results/_v3_n_recheck_llm_verdict_2026_09_27.md` | 40 | 101 | `D511` | `D511C545F88E`（12） | D8C' / '9466FDBF9C95' / 'AB75889EE738' / ' ⏎ `D511C545F88E` ⏎ C545F88E'）。\\n**frozen 面**：'_verify_15frozen.py | **非 D 族（哈希指纹）** | `F256` | E1 |
| 330 | `results/_v3_recheck_01_rescript_2026_09_27.md` | 15 | 85 | `D9` | `D9E14ED29FB9`（12） | 6_09_15.json' \| 'c7c59e0d2f6c' \| 8,753 \| ' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9' / 8,753 \| ⚠ SHA 不符、**字节逐字一致** \|\\n\| | **非 D 族（哈希指纹）** | `F1` | E2 |
| 331 | `results/_v3_recheck_01_rescript_2026_09_27.md` | 23 | 28 | `D9` | `D9E14ED29FB9`（12） | 记，不代为修订预登记）\\n\\nv1 §0.2 对本条 2 件记录的 SHA-12（' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9' / '1935F164D5F3'）与本 worker 按 'hash | **非 D 族（哈希指纹）** | `F1` | E2 |
| 332 | `results/_v3_recheck_05_rescript_2026_09_28.md` | 20 | 163 | `D9` | `D9E14ED29FB9`（12） | f6c'** \| 8,753 \| ✓ 与派工单一致（**与 v1 §0.2 所记 ' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9' 不符，见 §0.3 γ5**） \|\\n\| 0-4 \| 'result | **非 D 族（哈希指纹）** | `F1` | E2 |
| 333 | `results/_v3_recheck_05_rescript_2026_09_28.md` | 40 | 60 | `D9` | `D9E14ED29FB9`（12） | 2 三处 SHA-12 与盘上不符**：'boss_pa_1_*.json'（记 ' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9' / 实测 'c7c59e0d2f6c'）、'_v3x_conserv | **非 D 族（哈希指纹）** | `F1` | E2 |
| 334 | `results/_v3_recheck_26_rescript_2026_09_27.md` | 163 | 117 | `D9` | `D9E14ED29FB9`（12） | ss_pa_1_rbr_rm_result_2026_09_15.json'：记 ' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9' = SHA-1，实 SHA-256 = 'C7C59E0D2F6C' | **非 D 族（哈希指纹）** | `F1` | E2 |
| 335 | `results/_v3_recheck_prereg_v1_2026_09_27.md` | 32 | 72 | `D9` | `D9E14ED29FB9`（12） | ss_pa_1_rbr_rm_result_2026_09_15.json' \| ' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9' \| 8,753 \| 'rbr_iters_per_graph[22] | **非 D 族（哈希指纹）** | `F1` | E2 |
| 336 | `results/_v3_recheck_prereg_v1_2026_09_27.md` | 37 | 107 | `D9` | `D9E14ED29FB9`（12） | 15.json' §'v3_540_conservation_check' \| (' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9' 同 #1) \| — \| T540_sum=384 / R540_su | **非 D 族（哈希指纹）** | `F1` | E2 |
| 337 | `results/_v3_recheck_prereg_v1_2026_09_27.md` | 77 | 446 | `D9` | `D9E14ED29FB9`（12） |  bayes_t' 跟随 (a)+(b) 派生 \| boss_pa_1 JSON ' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9' + runner '1935F164D5F3' + 22 graph | **非 D 族（哈希指纹）** | `F1` | E2 |
| 338 | `results/_v3_recheck_prereg_v1_2026_09_27.md` | 79 | 355 | `D9` | `D9E14ED29FB9`（12） | vation anchor '425507BB555B' + boss_pa_1 ' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9' §'v3_540_conservation_check'（T540_ | **非 D 族（哈希指纹）** | `F1` | E2 |
| 339 | `results/_v3_recheck_prereg_v1p1_2026_09_27.md` | 55 | 123 | `D30` | `D30EDA5A1063`（12） | 希计算偏差产物**，实测真值 = 'B7547329AF2E'；v1 件自报哈希 ' ⏎ `D30EDA5A1063` ⏎ EDA5A1063' 同偏差，真值 = '88052d7db895'。本件独立复算，逐条** | **非 D 族（哈希指纹）** | `F1` | E2 |
| 340 | `results/_v3_recheck_prereg_v1p1_2026_09_27.md` | 60 | 59 | `D30` | `D30EDA5A1063`（12） | echeck_prereg_v1_2026_09_27.md'（v1 自报） \| ' ⏎ `D30EDA5A1063` ⏎ EDA5A1063'（v1 文末登记） \| **'88052d7db895'**（37,34 | **非 D 族（哈希指纹）** | `F1` | E2 |
| 341 | `results/_v3_recheck_prereg_v1p1_2026_09_27.md` | 295 | 85 | `D30` | `D30EDA5A1063`（12） | 1A90FD8F385A' vs 实测 'b7547329af2e'；v1 自报 ' ⏎ `D30EDA5A1063` ⏎ EDA5A1063' vs 实测 '88052d7db895'；**偏差机制 0 定因、0  | **非 D 族（哈希指纹）** | `F1` | E2 |
| 342 | `results/_v3_recheck_prereg_v1p5_2026_09_29.md` | 73 | 101 | `D9` | `D9E14ED29FB9`（12） | _15.json' \| **'c7c59e0d2f6c'** \| 8,753 \| ' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9' \| ✓ 在盘 \|\\n\| 1-r \| BOSS-P-A1 runner | **非 D 族（哈希指纹）** | `F1` | E2 |
| 343 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 80 | 25 | `D11` | `D11E085D9ECC`（12） | -\|---\|---\|---\|\\r\\n\| attacks/__init__.py \|  ⏎ `D11E085D9ECC` ⏎ E085D9ECC \| 183 \| C \| IN-EFFECT \| 2026/09/01 1 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 344 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 220 | 31 | `D9` | `D9BFAAE6D08B`（12） | n logs \|\\r\\n\| verifier/runs/v34_run2.md \|  ⏎ `D9BFAAE6D08B` ⏎ BFAAE6D08B \| 118 \| C \| IN-EFFECT \| 2026/08/30  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 345 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 259 | 27 | `D48` | `D48AC555761F`（12） | (43 items) \|\\r\\n\| verifier/v39/check.sh \|  ⏎ `D48AC555761F` ⏎ AC555761F \| 1935 \| C \| IN-EFFECT \| 2026/09/17  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 346 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 305 | 38 | `D0` | `D0BBA9379B4B`（12） | \|\\r\\n\| reviews/literature_scan_v2X_A.md \|  ⏎ `D0BBA9379B4B` ⏎ BBA9379B4B \| 18876 \| C \| IN-EFFECT \| 2026/08/2 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 347 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 316 | 24 | `D76` | `D76F2DC473BE`（12） | eviews series \|\\r\\n\| verifier/README.md \|  ⏎ `D76F2DC473BE` ⏎ F2DC473BE \| 14360 \| C \| IN-EFFECT \| 2026/08/30 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 348 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 337 | 35 | `D4` | `D4ED18152DC0`（12） | \|  \|\\r\\n\| docs/Findings_v2.0_bigquiz.md \|  ⏎ `D4ED18152DC0` ⏎ ED18152DC0 \| 3291 \|  \| IN-EFFECT \| 2026/08/28  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 349 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 388 | 69 | `D3` | `D3BDFC99FCDC`（12） | view_trae_code_supplement_2026_09_20.md \|  ⏎ `D3BDFC99FCDC` ⏎ BDFC99FCDC \| 11877 \| 2026/09/20 15:02:13 \|\\r\\n | **非 D 族（哈希指纹）** | `F12` | E3 |
| 350 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 503 | 69 | `D7` | `D7F03FDE4067`（12） | lus_adendum_7_report_20260917_133726.md \|  ⏎ `D7F03FDE4067` ⏎ F03FDE4067 \| 6435 \| 2026/09/17 13:37:29 \|\\r\\n\| | **非 D 族（哈希指纹）** | `F12` | E3 |
| 351 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 530 | 69 | `D91` | `D91B0C5F642F`（12） | mbedding_glm53_l30_20260917_142748.json \|  ⏎ `D91B0C5F642F` ⏎ B0C5F642F \| 11833 \| 2026/09/17 14:32:56 \|\\r\\n\| | **非 D 族（哈希指纹）** | `F12` | E3 |
| 352 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 545 | 35 | `D80` | `D80A8F75A122`（12） | 34 \|\\r\\n\| results/_tra_v0_2026_09_10.py \|  ⏎ `D80A8F75A122` ⏎ A8F75A122 \| 12125 \| 2026/09/10 20:20:20 \|\\r\\n\| | **非 D 族（哈希指纹）** | `F256` | E1 |
| 353 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 564 | 36 | `D778` | `D778E436C986`（12） | 8 \|\\r\\n\| results/_v4_d1_chain_verify.py \|  ⏎ `D778E436C986` ⏎ E436C986 \| 884 \| 2026/09/22 17:15:10 \|\\r\\n\| re | **非 D 族（哈希指纹）** | `F12` | E3 |
| 354 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 579 | 48 | `D701` | `D701E14B4E44`（12） | ults/_v4_exec_cbin_rerun2026_09_23.json \|  ⏎ `D701E14B4E44` ⏎ E14B4E44 \| 573 \| 2026/09/23 14:30:21 \|\\r\\n\| re | **非 D 族（哈希指纹）** | `F12` | E3 |
| 355 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 651 | 51 | `D39` | `D39C42D0724F`（12） | s/_v4_exec_n30_constructed_verdict.json \|  ⏎ `D39C42D0724F` ⏎ C42D0724F \| 5025 \| 2026/09/23 15:28:58 \|\\r\\n\|  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 356 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 674 | 38 | `D48` | `D48A372FD118`（12） | \|\\r\\n\| results/_v4_exec_s18_result.json \|  ⏎ `D48A372FD118` ⏎ A372FD118 \| 1642 \| 2026/09/23 12:05:52 \|\\r\\n\|  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 357 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 684 | 51 | `D3` | `D3F376A6C45F`（12） | s/_v4_exec_s40_rejudged_2026_09_23.json \|  ⏎ `D3F376A6C45F` ⏎ F376A6C45F \| 6703 \| 2026/09/23 16:38:39 \|\\r\\n\| | **非 D 族（哈希指纹）** | `F12` | E3 |
| 358 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 696 | 53 | `D2` | `D2E093CE13FA`（12） | _v4_n29_real_post_hashes_2026_09_23.txt \|  ⏎ `D2E093CE13FA` ⏎ E093CE13FA \| 625 \| 2026/09/23 16:38:24 \|\\r\\n\|  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 359 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 728 | 40 | `D70` | `D70B748ADE01`（12） | r\\n\| results/_v4_supp_b_n11_result.json \|  ⏎ `D70B748ADE01` ⏎ B748ADE01 \| 3913 \| 2026/09/24 09:55:11 \|\\r\\n\|  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 360 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 735 | 52 | `D9` | `D9CC869605E1`（12） | /_v4_supp_cd_post_hashes_2026_09_24.txt \|  ⏎ `D9CC869605E1` ⏎ CC869605E1 \| 1395 \| 2026/09/24 09:50:19 \|\\r\\n\| | **非 D 族（哈希指纹）** | `F12` | E3 |
| 361 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 742 | 44 | `D74` | `D74FAF11772B`（12） |  results/_v4_supp_e_multimodel_rerun.py \|  ⏎ `D74FAF11772B` ⏎ FAF11772B \| 43281 \| 2026/09/24 10:07:03 \|\\r\\n\| | **非 D 族（哈希指纹）** | `F12` | E3 |
| 362 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 761 | 61 | `D872` | `D872AA208635`（12） | _l14_n11full_post_hashes_2026_09_24.txt \|  ⏎ `D872AA208635` ⏎ AA208635 \| 841 \| 2026/09/24 15:37:51 \|\\r\\n\| re | **非 D 族（哈希指纹）** | `F12` | E3 |
| 363 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 802 | 45 | `D7` | `D7BAB92DD1D5`（12） | results/_v4_supp_l7_e_n20_fill_diag4.py \|  ⏎ `D7BAB92DD1D5` ⏎ BAB92DD1D5 \| 764 \| 2026/09/24 13:12:16 \|\\r\\n\|  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 364 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 824 | 56 | `D1` | `D1DBFD7044AA`（12） | _supp_l7_e_n20_measure_qwen3_7_max.json \|  ⏎ `D1DBFD7044AA` ⏎ DBFD7044AA \| 8988 \| 2026/09/24 12:47:31 \|\\r\\n\| | **非 D 族（哈希指纹）** | `F12` | E3 |
| 365 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 830 | 66 | `D0` | `D0B64D1AB8B7`（12） | _n20_pre_hashes_v4frozen_2026_09_24.txt \|  ⏎ `D0B64D1AB8B7` ⏎ B64D1AB8B7 \| 1960 \| 2026/09/24 12:12:34 \|\\r\\n\| | **非 D 族（哈希指纹）** | `F12` | E3 |
| 366 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 858 | 56 | `D999` | `D999A43D521F`（12） | _supp_l8_n12r_pre_hashes_2026_09_24.txt \|  ⏎ `D999A43D521F` ⏎ A43D521F \| 29820 \| 2026/09/24 12:02:56 \|\\r\\n\|  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 367 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 898 | 51 | `D74` | `D74D6B39D1B0`（12） | s/attack_pc_a3_clipping_2026_09_15.json \|  ⏎ `D74D6B39D1B0` ⏎ D6B39D1B0 \| 1265 \| 2026/09/15 15:27:36 \|\\r\\n\|  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 368 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 907 | 66 | `D6` | `D6F233D73C45`（12） | licator_dynamics_result_2026_09_15.json \|  ⏎ `D6F233D73C45` ⏎ F233D73C45 \| 9098 \| 2026/09/15 15:28:10 \|\\r\\n\| | **非 D 族（哈希指纹）** | `F256` | E1 |
| 369 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 912 | 51 | `D74` | `D74D6B39D1B0`（12） | s/boss_pc_3_a3_clipping_2026_09_15.json \|  ⏎ `D74D6B39D1B0` ⏎ D6B39D1B0 \| 1265 \| 2026/09/15 13:34:48 \|\\r\\n\|  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 370 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 1045 | 55 | `D22` | `D22CD39735A1`（12） | milyl_prior_cache/physics_concepts.json \|  ⏎ `D22CD39735A1` ⏎ CD39735A1 \| 2595 \| 2026/08/28 20:08:22 \|\\r\\n\|  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 371 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 1080 | 53 | `D7` | `D7AC5A401AA7`（12） | gt8b_cache/prior_chinese_dynasties.json \|  ⏎ `D7AC5A401AA7` ⏎ AC5A401AA7 \| 2937 \| 2026/08/29 22:40:50 \|\\r\\n\| | **非 D 族（哈希指纹）** | `F12` | E3 |
| 372 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 1164 | 52 | `D87` | `D87C0327A6FB`（12） | /deposon_3risk_v0_fixes_2026_09_11.json \|  ⏎ `D87C0327A6FB` ⏎ C0327A6FB \| 8338 \| C \| IN-EFFECT \| 2026/09/11  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 373 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 1171 | 45 | `D511` | `D511C545F88E`（12） | deposon_team/plugins/_pg_v01_compute.py \|  ⏎ `D511C545F88E` ⏎ C545F88E \| 20923 \| C \| IN-EFFECT \| 2026/09/16  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 374 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 1180 | 58 | `D3` | `D3B45B64C0DA`（12） | plugins/_v3_review_r3_sha_2026_09_23.py \|  ⏎ `D3B45B64C0DA` ⏎ B45B64C0DA \| 1881 \| C \| IN-EFFECT \| 2026/09/23 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 375 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 1222 | 53 | `D301` | `D301BBFED982`（12） | deposon_v3x_6way_stage2_2026_09_10.json \|  ⏎ `D301BBFED982` ⏎ BBFED982 \| 2741 \| A \| IN-EFFECT \| 2026/09/10 1 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 376 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 1223 | 53 | `D892` | `D892A9D3D6BA`（12） | deposon_v3x_6way_stage3_2026_09_10.json \|  ⏎ `D892A9D3D6BA` ⏎ A9D3D6BA \| 15943 \| A \| IN-EFFECT \| 2026/09/10  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 377 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 1235 | 52 | `D3` | `D3F72F67977D`（12） | /llm_prior_cache_v18_contamination.json \|  ⏎ `D3F72F67977D` ⏎ F72F67977D \| 639 \| C \| IN-EFFECT \| 2026/08/23  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 378 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 1265 | 59 | `D8` | `D8F2B99AA527`（12） | 0_5_experiment_invitation_2026_09_17.md \|  ⏎ `D8F2B99AA527` ⏎ F2B99AA527 \| 7617 \| C \| IN-EFFECT \| 2026/09/17 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 379 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 1276 | 44 | `D74` | `D74E1534493E`（12） |  docs/V3X/BPA_PILOT_2026_09_09_mavis.md \|  ⏎ `D74E1534493E` ⏎ E1534493E \| 6864 \| C \| IN-EFFECT \| 2026/09/09  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 380 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 1296 | 49 | `D427` | `D427B2F57C33`（12） | /V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md \|  ⏎ `D427B2F57C33` ⏎ B2F57C33 \| 6301 \| C \| IN-EFFECT \| 2026/09/08 1 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 381 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 1347 | 40 | `D64` | `D64E1264737F`（12） | r\\n\| results/_v4_n22s_margin_verdict.md \|  ⏎ `D64E1264737F` ⏎ E1264737F \| 11027 \| A \| IN-EFFECT \| 2026/09/24 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 382 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 1349 | 35 | `D279` | `D279EBDE5E84`（12） | ct \|\\r\\n\| results/_v4_pi_cot_verdict.md \|  ⏎ `D279EBDE5E84` ⏎ EBDE5E84 \| 2208 \| A \| IN-EFFECT \| 2026/09/23 1 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 383 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 1437 | 50 | `D2` | `D2BD7521D651`（12） | ts/_v4_proxy_student_teacher_paths.json \|  ⏎ `D2BD7521D651` ⏎ BD7521D651 \| 2575 \| C \| IN-EFFECT \| 2026/09/22 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 384 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 1459 | 62 | `D39` | `D39CB17B051B`（12） | llation_reply_claude_code_2026_09_20.md \|  ⏎ `D39CB17B051B` ⏎ CB17B051B \| 64212 \| B \| IN-EFFECT \| 2026/09/21 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 385 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 1567 | 78 | `D2` | `D2CD7ACB29A1`（12） | 3_merkle_22caption_runner_2026_09_16.py \|  ⏎ `D2CD7ACB29A1` ⏎ CD7ACB29A1 \| 18596 \| C \| IN-EFFECT \| 2026/09/1 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 386 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 1656 | 73 | `D301` | `D301BBFED982`（12） | ge2_2026_09_10.json \| V3X \| EXP_PRODUCT \|  ⏎ `D301BBFED982` ⏎ BBFED982 \| 2026/09/10 17:56:17 \| V3X 6-way sta | **非 D 族（哈希指纹）** | `F12` | E3 |
| 387 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 1657 | 73 | `D892` | `D892A9D3D6BA`（12） | ge3_2026_09_10.json \| V3X \| EXP_PRODUCT \|  ⏎ `D892A9D3D6BA` ⏎ A9D3D6BA \| 2026/09/10 18:15:22 \| V3X 6-way sta | **非 D 族（哈希指纹）** | `F12` | E3 |
| 388 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 1682 | 56 | `D64` | `D64E1264737F`（12） | _n22s_margin_verdict.md \| V4 \| JUDGMENT \|  ⏎ `D64E1264737F` ⏎ E1264737F \| 2026/09/24 09:42:45 \| N22s margin  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 389 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 1690 | 51 | `D279` | `D279EBDE5E84`（12） | s/_v4_pi_cot_verdict.md \| V4 \| JUDGMENT \|  ⏎ `D279EBDE5E84` ⏎ EBDE5E84 \| 2026/09/23 17:17:32 \| Task-B verdic | **非 D 族（哈希指纹）** | `F12` | E3 |
| 390 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 1764 | 77 | `D39` | `D39CB17B051B`（12） | laude_code_2026_09_20.md \| V4 \| LETTERS \|  ⏎ `D39CB17B051B` ⏎ CB17B051B \| 2026/09/21 11:01:14 \| V4 commissio | **非 D 族（哈希指纹）** | `F256` | E1 |
| 391 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 1911 | 256 | `D11` | `D11E085D9ECC`（12） | atum.md 35081D39F35B, \x07ttacks/__init__.py  ⏎ `D11E085D9ECC` ⏎ E085D9ECC, docs/V3X/P_D_FINGERPRINT_V0_3_SPEC. | **非 D 族（哈希指纹）** | `F256` | E1 |
| 392 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 303 | 28 | `D11` | `D11E085D9ECC`（12） | --\|---\|---\|\\r\\n\| 'attacks/__init__.py' \| ' ⏎ `D11E085D9ECC` ⏎ E085D9ECC' \| 183 \| IN-EFFECT \| C \| 2026/09/01  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 393 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 363 | 81 | `D2` | `D2CD7ACB29A1`（12） | merkle_22caption_runner_2026_09_16.py' \| ' ⏎ `D2CD7ACB29A1` ⏎ CD7ACB29A1' \| 18596 \| IN-EFFECT \| C \| 2026/09/ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 394 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 424 | 48 | `D511` | `D511C545F88E`（12） | poson_team/plugins/_pg_v01_compute.py' \| ' ⏎ `D511C545F88E` ⏎ C545F88E' \| 20923 \| IN-EFFECT \| C \| 2026/09/16 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 395 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 433 | 61 | `D3` | `D3B45B64C0DA`（12） | ugins/_v3_review_r3_sha_2026_09_23.py' \| ' ⏎ `D3B45B64C0DA` ⏎ B45B64C0DA' \| 1881 \| IN-EFFECT \| C \| 2026/09/2 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 396 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 482 | 38 | `D4` | `D4ED18152DC0`（12） | \|\\r\\n\| 'docs/Findings_v2.0_bigquiz.md' \| ' ⏎ `D4ED18152DC0` ⏎ ED18152DC0' \| 3291 \| IN-EFFECT \| C \| 2026/08/2 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 397 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 522 | 47 | `D74` | `D74E1534493E`（12） | ocs/V3X/BPA_PILOT_2026_09_09_mavis.md' \| ' ⏎ `D74E1534493E` ⏎ E1534493E' \| 6864 \| IN-EFFECT \| C \| 2026/09/09 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 398 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 553 | 52 | `D427` | `D427B2F57C33`（12） | 3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md' \| ' ⏎ `D427B2F57C33` ⏎ B2F57C33' \| 6301 \| IN-EFFECT \| C \| 2026/09/08  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 399 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 640 | 65 | `D39` | `D39CB17B051B`（12） | ation_reply_claude_code_2026_09_20.md' \| ' ⏎ `D39CB17B051B` ⏎ CB17B051B' \| 64212 \| IN-EFFECT \| C \| 2026/09/2 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 400 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 650 | 72 | `D3` | `D3BDFC99FCDC`（12） | ew_trae_code_supplement_2026_09_20.md' \| ' ⏎ `D3BDFC99FCDC` ⏎ BDFC99FCDC' \| 11877 \| IN-EFFECT \| C \| 2026/09/ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 401 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 780 | 38 | `D80` | `D80A8F75A122`（12） | \|\\r\\n\| 'results/_tra_v0_2026_09_10.py' \| ' ⏎ `D80A8F75A122` ⏎ A8F75A122' \| 12125 \| IN-EFFECT \| C \| 2026/09/1 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 402 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 791 | 62 | `D8` | `D8F2B99AA527`（12） | 5_experiment_invitation_2026_09_17.md' \| ' ⏎ `D8F2B99AA527` ⏎ F2B99AA527' \| 7617 \| IN-EFFECT \| C \| 2026/09/1 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 403 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 803 | 39 | `D778` | `D778E436C986`（12） | \\r\\n\| 'results/_v4_d1_chain_verify.py' \| ' ⏎ `D778E436C986` ⏎ E436C986' \| 884 \| IN-EFFECT \| C \| 2026/09/22 1 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 404 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 834 | 51 | `D701` | `D701E14B4E44`（12） | ts/_v4_exec_cbin_rerun2026_09_23.json' \| ' ⏎ `D701E14B4E44` ⏎ E14B4E44' \| 573 \| IN-EFFECT \| C \| 2026/09/23 1 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 405 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 907 | 54 | `D39` | `D39C42D0724F`（12） | _v4_exec_n30_constructed_verdict.json' \| ' ⏎ `D39C42D0724F` ⏎ C42D0724F' \| 5025 \| IN-EFFECT \| C \| 2026/09/23 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 406 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 931 | 41 | `D48` | `D48A372FD118`（12） | \\n\| 'results/_v4_exec_s18_result.json' \| ' ⏎ `D48A372FD118` ⏎ A372FD118' \| 1642 \| IN-EFFECT \| C \| 2026/09/23 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 407 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 941 | 54 | `D3` | `D3F376A6C45F`（12） | _v4_exec_s40_rejudged_2026_09_23.json' \| ' ⏎ `D3F376A6C45F` ⏎ F376A6C45F' \| 6703 \| IN-EFFECT \| C \| 2026/09/2 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 408 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 970 | 43 | `D64` | `D64E1264737F`（12） | \| 'results/_v4_n22s_margin_verdict.md' \| ' ⏎ `D64E1264737F` ⏎ E1264737F' \| 11027 \| IN-EFFECT \| C \| 2026/09/2 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 409 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 972 | 56 | `D2` | `D2E093CE13FA`（12） | 4_n29_real_post_hashes_2026_09_23.txt' \| ' ⏎ `D2E093CE13FA` ⏎ E093CE13FA' \| 625 \| IN-EFFECT \| C \| 2026/09/23 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 410 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 994 | 38 | `D279` | `D279EBDE5E84`（12） | \|\\r\\n\| 'results/_v4_pi_cot_verdict.md' \| ' ⏎ `D279EBDE5E84` ⏎ EBDE5E84' \| 2208 \| IN-EFFECT \| C \| 2026/09/23  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 411 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 1008 | 53 | `D2` | `D2BD7521D651`（12） | /_v4_proxy_student_teacher_paths.json' \| ' ⏎ `D2BD7521D651` ⏎ BD7521D651' \| 2575 \| IN-EFFECT \| C \| 2026/09/2 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 412 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 1042 | 43 | `D70` | `D70B748ADE01`（12） | \| 'results/_v4_supp_b_n11_result.json' \| ' ⏎ `D70B748ADE01` ⏎ B748ADE01' \| 3913 \| IN-EFFECT \| C \| 2026/09/24 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 413 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 1050 | 55 | `D9` | `D9CC869605E1`（12） | v4_supp_cd_post_hashes_2026_09_24.txt' \| ' ⏎ `D9CC869605E1` ⏎ CC869605E1' \| 1395 \| IN-EFFECT \| C \| 2026/09/2 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 414 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 1058 | 47 | `D74` | `D74FAF11772B`（12） | esults/_v4_supp_e_multimodel_rerun.py' \| ' ⏎ `D74FAF11772B` ⏎ FAF11772B' \| 43281 \| IN-EFFECT \| C \| 2026/09/2 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 415 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 1081 | 64 | `D872` | `D872AA208635`（12） | 14_n11full_post_hashes_2026_09_24.txt' \| ' ⏎ `D872AA208635` ⏎ AA208635' \| 841 \| IN-EFFECT \| C \| 2026/09/24 1 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 416 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 1124 | 48 | `D7` | `D7BAB92DD1D5`（12） | sults/_v4_supp_l7_e_n20_fill_diag4.py' \| ' ⏎ `D7BAB92DD1D5` ⏎ BAB92DD1D5' \| 764 \| IN-EFFECT \| C \| 2026/09/24 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 417 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 1147 | 59 | `D1` | `D1DBFD7044AA`（12） | upp_l7_e_n20_measure_qwen3_7_max.json' \| ' ⏎ `D1DBFD7044AA` ⏎ DBFD7044AA' \| 8988 \| IN-EFFECT \| C \| 2026/09/2 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 418 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 1153 | 69 | `D0` | `D0B64D1AB8B7`（12） | 20_pre_hashes_v4frozen_2026_09_24.txt' \| ' ⏎ `D0B64D1AB8B7` ⏎ B64D1AB8B7' \| 1960 \| LOCKED \| C \| 2026/09/24 1 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 419 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 1182 | 59 | `D999` | `D999A43D521F`（12） | upp_l8_n12r_pre_hashes_2026_09_24.txt' \| ' ⏎ `D999A43D521F` ⏎ A43D521F' \| 29820 \| IN-EFFECT \| C \| 2026/09/24 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 420 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 1238 | 54 | `D74` | `D74D6B39D1B0`（12） | attack_pc_a3_clipping_2026_09_15.json' \| ' ⏎ `D74D6B39D1B0` ⏎ D6B39D1B0' \| 1265 \| IN-EFFECT \| C \| 2026/09/15 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 421 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 1247 | 69 | `D6` | `D6F233D73C45`（12） | cator_dynamics_result_2026_09_15.json' \| ' ⏎ `D6F233D73C45` ⏎ F233D73C45' \| 9098 \| IN-EFFECT \| C \| 2026/09/1 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 422 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 1252 | 54 | `D74` | `D74D6B39D1B0`（12） | boss_pc_3_a3_clipping_2026_09_15.json' \| ' ⏎ `D74D6B39D1B0` ⏎ D6B39D1B0' \| 1265 \| IN-EFFECT \| C \| 2026/09/15 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 423 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 1266 | 55 | `D87` | `D87C0327A6FB`（12） | eposon_3risk_v0_fixes_2026_09_11.json' \| ' ⏎ `D87C0327A6FB` ⏎ C0327A6FB' \| 8338 \| IN-EFFECT \| C \| 2026/09/11 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 424 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 1377 | 56 | `D301` | `D301BBFED982`（12） | poson_v3x_6way_stage2_2026_09_10.json' \| ' ⏎ `D301BBFED982` ⏎ BBFED982' \| 2741 \| IN-EFFECT \| C \| 2026/09/10  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 425 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 1378 | 56 | `D892` | `D892A9D3D6BA`（12） | poson_v3x_6way_stage3_2026_09_10.json' \| ' ⏎ `D892A9D3D6BA` ⏎ A9D3D6BA' \| 15943 \| IN-EFFECT \| C \| 2026/09/10 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 426 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 1414 | 58 | `D22` | `D22CD39735A1`（12） | lyl_prior_cache/physics_concepts.json' \| ' ⏎ `D22CD39735A1` ⏎ CD39735A1' \| 2595 \| IN-EFFECT \| C \| 2026/08/28 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 427 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 1449 | 56 | `D7` | `D7AC5A401AA7`（12） | 8b_cache/prior_chinese_dynasties.json' \| ' ⏎ `D7AC5A401AA7` ⏎ AC5A401AA7' \| 2937 \| IN-EFFECT \| C \| 2026/08/2 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 428 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 1458 | 55 | `D3` | `D3F72F67977D`（12） | lm_prior_cache_v18_contamination.json' \| ' ⏎ `D3F72F67977D` ⏎ F72F67977D' \| 639 \| IN-EFFECT \| C \| 2026/08/23 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 429 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 1501 | 41 | `D0` | `D0BBA9379B4B`（12） | \\n\| 'reviews/literature_scan_v2X_A.md' \| ' ⏎ `D0BBA9379B4B` ⏎ BBA9379B4B' \| 18876 \| IN-EFFECT \| C \| 2026/08/ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 430 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 1858 | 27 | `D76` | `D76F2DC473BE`（12） | ---\|---\|---\|\\r\\n\| 'verifier/README.md' \| ' ⏎ `D76F2DC473BE` ⏎ F2DC473BE' \| 14360 \| IN-EFFECT \| C \| 2026/08/3 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 431 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 1905 | 34 | `D9` | `D9BFAAE6D08B`（12） | :16 \|\\r\\n\| 'verifier/runs/v34_run2.md' \| ' ⏎ `D9BFAAE6D08B` ⏎ BFAAE6D08B' \| 118 \| IN-EFFECT \| C \| 2026/08/30 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 432 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 1946 | 30 | `D48` | `D48AC555761F`（12） | 3:20:52 \|\\r\\n\| 'verifier/v39/check.sh' \| ' ⏎ `D48AC555761F` ⏎ AC555761F' \| 1935 \| IN-EFFECT \| C \| 2026/09/17 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 433 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 2054 | 55 | `D1` | `D1B82B59E8A6`（12） | ckup_v181/deposon_paper_v1_en.md.bak2' \| ' ⏎ `D1B82B59E8A6` ⏎ B82B59E8A6' \| 121925 \| IN-EFFECT \| C \| 2026/08 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 434 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 2095 | 59 | `D20` | `D20CB499B315`（12） | _p_l_v3_probe_doubao_v2_2026_09_17.py' \| ' ⏎ `D20CB499B315` ⏎ CB499B315' \| 1872 \| IN-EFFECT \| C \| 2026/09/17 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 435 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 2112 | 49 | `D80` | `D80B9C7F922B`（12） | rker_temp/_verify_beta2_2026_09_17.py' \| ' ⏎ `D80B9C7F922B` ⏎ B9C7F922B' \| 1224 \| IN-EFFECT \| C \| 2026/09/17 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 436 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 2194 | 61 | `D96` | `D96CDF2B3BDD`（12） | build/fonts/KaTeX_Script-Regular.woff' \| ' ⏎ `D96CDF2B3BDD` ⏎ CDF2B3BDD' \| 10588 \| IN-EFFECT \| C \| 2026/08/2 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 437 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 2201 | 61 | `D04` | `D04C54219F9E`（12） | build/fonts/KaTeX_Size2-Regular.woff2' \| ' ⏎ `D04C54219F9E` ⏎ C54219F9E' \| 5208 \| IN-EFFECT \| C \| 2026/08/23 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 438 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 2267 | 43 | `D379` | `D379A1960EF0`（12） | \| 'cache/cache/v2/REVISION_LOG_v2X.md' \| ' ⏎ `D379A1960EF0` ⏎ A1960EF0' \| 31989 \| IN-EFFECT \| C \| 2026/08/30 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 439 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 2317 | 54 | `D5` | `D5D22FCE2686`（12） | /GPT6_TEAMOROUTER_SMOKE_2026_09_10.md' \| ' ⏎ `D5D22FCE2686` ⏎ D22FCE2686' \| 7124 \| IN-EFFECT \| C \| 2026/09/1 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 440 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 2583 | 42 | `D8` | `D8E1A201E36B`（12） | n\| 'paper/references.bib.bak_prearxiv' \| ' ⏎ `D8E1A201E36B` ⏎ E1A201E36B' \| 15306 \| IN-EFFECT \| C \| 2026/09/ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 441 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 2624 | 72 | `D7` | `D7F03FDE4067`（12） | s_adendum_7_report_20260917_133726.md' \| ' ⏎ `D7F03FDE4067` ⏎ F03FDE4067' \| 6435 \| IN-EFFECT \| C \| 2026/09/1 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 442 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 2651 | 72 | `D91` | `D91B0C5F642F`（12） | edding_glm53_l30_20260917_142748.json' \| ' ⏎ `D91B0C5F642F` ⏎ B0C5F642F' \| 11833 \| IN-EFFECT \| C \| 2026/09/1 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 443 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 2743 | 58 | `D22` | `D22CD39735A1`（12） | lyL_prior_cache/physics_concepts.json' \| ' ⏎ `D22CD39735A1` ⏎ CD39735A1' \| 2595 \| IN-EFFECT \| C \| 2026/08/28 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 444 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 2778 | 56 | `D7` | `D7AC5A401AA7`（12） | 8b_cache/prior_chinese_dynasties.json' \| ' ⏎ `D7AC5A401AA7` ⏎ AC5A401AA7' \| 2937 \| IN-EFFECT \| C \| 2026/08/2 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 445 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 2787 | 55 | `D3` | `D3F72F67977D`（12） | lm_prior_cache_v18_contamination.json' \| ' ⏎ `D3F72F67977D` ⏎ F72F67977D' \| 639 \| IN-EFFECT \| C \| 2026/08/23 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 446 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 2808 | 33 | `D75` | `D75B5979333D`（12） | 3:27 \|\\r\\n\| 'scripts/_verify_masks.py' \| ' ⏎ `D75B5979333D` ⏎ B5979333D' \| 452 \| IN-EFFECT \| C \| 2026/09/10  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 447 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 2846 | 36 | `D791` | `D791E7830E63`（12） | 0 \|\\r\\n\| 'scripts/scripts/_fix_cn5.py' \| ' ⏎ `D791E7830E63` ⏎ E7830E63' \| 1397 \| IN-EFFECT \| C \| 2026/09/08  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 448 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 2855 | 42 | `D9` | `D9CE72A7D539`（12） | n\| 'scripts/scripts/_fix_overflow2.py' \| ' ⏎ `D9CE72A7D539` ⏎ CE72A7D539' \| 4273 \| IN-EFFECT \| C \| 2026/09/0 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 449 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 2866 | 36 | `D62` | `D62CD2603F60`（12） | 8 \|\\r\\n\| 'scripts/scripts/_qa_2026.py' \| ' ⏎ `D62CD2603F60` ⏎ CD2603F60' \| 5823 \| IN-EFFECT \| C \| 2026/09/08 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 450 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 2871 | 35 | `D4` | `D4AB79727B41`（12） | 56 \|\\r\\n\| 'scripts/scripts/_retest.py' \| ' ⏎ `D4AB79727B41` ⏎ AB79727B41' \| 2049 \| IN-EFFECT \| C \| 2026/09/0 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 451 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 2892 | 44 | `D056` | `D056EA8E13C5`（12） |  'scripts/scripts/fix_thanks_final.py' \| ' ⏎ `D056EA8E13C5` ⏎ EA8E13C5' \| 2511 \| IN-EFFECT \| C \| 2026/09/08  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 452 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 2958 | 64 | `D2` | `D2A0559A83F4`（12） | e_2026_09_10/verify_dev_smoke_9m5c.py' \| ' ⏎ `D2A0559A83F4` ⏎ A0559A83F4' \| 8881 \| IN-EFFECT \| C \| 2026/09/1 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 453 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 2959 | 60 | `D797` | `D797A09057F7`（12） | ngine_2026_09_10/volcengine_5cells.py' \| ' ⏎ `D797A09057F7` ⏎ A09057F7' \| 5984 \| IN-EFFECT \| C \| 2026/09/10  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 454 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 2987 | 27 | `D76` | `D76F2DC473BE`（12） | ---\|---\|---\|\\r\\n\| 'verifier/README.md' \| ' ⏎ `D76F2DC473BE` ⏎ F2DC473BE' \| 14360 \| IN-EFFECT \| C \| 2026/08/3 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 455 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 3033 | 34 | `D9` | `D9BFAAE6D08B`（12） | :16 \|\\r\\n\| 'verifier/runs/v34_run2.md' \| ' ⏎ `D9BFAAE6D08B` ⏎ BFAAE6D08B' \| 118 \| IN-EFFECT \| C \| 2026/08/30 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 456 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 3106 | 51 | `D95` | `D95BE2A05990`（12） | /deliverables/deposon_arxiv_en.tar.gz' \| ' ⏎ `D95BE2A05990` ⏎ BE2A05990' \| 1637413 \| IN-EFFECT \| C \| 2026/09 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 457 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 3132 | 43 | `D1` | `D1EE21F3F6AE`（12） | \| '_movedout_manifest_2026_09_21.json' \| ' ⏎ `D1EE21F3F6AE` ⏎ EE21F3F6AE' \| 291551 \| IN-EFFECT \| C \| 2026/09 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 458 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 3144 | 44 | `D5` | `D5E74A98C44B`（12） |  '_p_l_v3_phase1_runner_2026_09_17.py' \| ' ⏎ `D5E74A98C44B` ⏎ E74A98C44B' \| 35425 \| IN-EFFECT \| C \| 2026/09/ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 459 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 3247 | 67 | `D0` | `D0D188C60A62`（12） | _build_minimax_artifact_2026_09_16.py' \| ' ⏎ `D0D188C60A62` ⏎ D188C60A62' \| 7361 \| IN-EFFECT \| C \| 2026/09/1 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 460 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 3255 | 75 | `D2` | `D2CD7ACB29A1`（12） | merkle_22caption_runner_2026_09_16.py' \| ' ⏎ `D2CD7ACB29A1` ⏎ CD7ACB29A1' \| 18596 \| IN-EFFECT \| C \| 2026/09/ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 461 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 3265 | 77 | `D1` | `D1BC564264EF`（12） | ger_verification_runner_2026_09_16.py' \| ' ⏎ `D1BC564264EF` ⏎ BC564264EF' \| 13230 \| IN-EFFECT \| C \| 2026/09/ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 462 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 3298 | 62 | `D8` | `D8EAFDD67119`（12） | AL_REVIEW_R2_2026_09_17/REVIEW_RB2.md' \| ' ⏎ `D8EAFDD67119` ⏎ EAFDD67119' \| 27839 \| IN-EFFECT \| C \| 2026/09/ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 463 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 3425 | 64 | `D060` | `D060F75DBE9F`（12） | 026_09_20/fiction_that_feeds_back.tex' \| ' ⏎ `D060F75DBE9F` ⏎ F75DBE9F' \| 93324 \| ARCHIVED \| C \| 2026/09/17  | **非 D 族（哈希指纹）** | `F12` | E3 |
| 464 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 3529 | 72 | `D7` | `D7F03FDE4067`（12） | s_adendum_7_report_20260917_133726.md' \| ' ⏎ `D7F03FDE4067` ⏎ F03FDE4067' \| 6435 \| IN-EFFECT \| C \| 2026/09/1 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 465 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 3556 | 72 | `D91` | `D91B0C5F642F`（12） | edding_glm53_L30_20260917_142748.json' \| ' ⏎ `D91B0C5F642F` ⏎ B0C5F642F' \| 11833 \| IN-EFFECT \| C \| 2026/09/1 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 466 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 3573 | 38 | `D80` | `D80A8F75A122`（12） | \|\\r\\n\| 'results/_tra_v0_2026_09_10.py' \| ' ⏎ `D80A8F75A122` ⏎ A8F75A122' \| 12125 \| IN-EFFECT \| C \| 2026/09/1 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 467 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 3595 | 62 | `D8` | `D8F2B99AA527`（12） | 5_experiment_invitation_2026_09_17.md' \| ' ⏎ `D8F2B99AA527` ⏎ F2B99AA527' \| 7617 \| IN-EFFECT \| C \| 2026/09/1 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 468 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 3607 | 54 | `D74` | `D74D6B39D1B0`（12） | attack_pc_a3_clipping_2026_09_15.json' \| ' ⏎ `D74D6B39D1B0` ⏎ D6B39D1B0' \| 1265 \| IN-EFFECT \| C \| 2026/09/15 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 469 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 3610 | 69 | `D6` | `D6F233D73C45`（12） | cator_dynamics_result_2026_09_15.json' \| ' ⏎ `D6F233D73C45` ⏎ F233D73C45' \| 9098 \| IN-EFFECT \| C \| 2026/09/1 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 470 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 3615 | 54 | `D74` | `D74D6B39D1B0`（12） | boss_pc_3_a3_clipping_2026_09_15.json' \| ' ⏎ `D74D6B39D1B0` ⏎ D6B39D1B0' \| 1265 \| IN-EFFECT \| C \| 2026/09/15 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 471 | `results/_v4_effective_register_2026_09_28.md` | 158 | 114 | `D9` | `D9E14ED29FB9`（12） | 异**如实挂账**（记值／实测值分列）：'boss_pa_1_*.json' 记 ' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9' / 实测 'c7c59e0d2f6c'；'_v3x_conserva | **非 D 族（哈希指纹）** | `F1` | E2 |
| 472 | `results/_v4_evidence_audit_reconcile_2026_09_26.md` | 17 | 78 | `D6` | `D6CB03A4657E`（12） | 理 v3 棒 L37 / L44 / L220） \| cleanup v3 棒标 ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' = T1 verdict 锚 + 'F1B5E49F3058' =  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 473 | `results/_v4_evidence_audit_reconcile_2026_09_26.md` | 17 | 150 | `D6` | `D6CB03A4657E`（12） |  'F1B5E49F3058' = T1.5 锚（非 T1 verdict） \| ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' = 'results/_v4_supp_t1_result.json | **非 D 族（哈希指纹）** | `F256` | E1 |
| 474 | `results/_v4_evidence_audit_reconcile_2026_09_26.md` | 17 | 336 | `D6` | `D6CB03A4657E`（12） | v3 棒**标签互换**：t1_verdict 实是 F1B5E49F3058，非  ⏎ `D6CB03A4657E` ⏎ CB03A4657E） \| cleanup v3 棒**两处字段填写错**：(a) L37  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 475 | `results/_v4_evidence_audit_reconcile_2026_09_26.md` | 17 | 621 | `D6` | `D6CB03A4657E`（12） | 3 勘误追加式补正确映射：F1B5E49F3058=T1 verdict.md /  ⏎ `D6CB03A4657E` ⏎ CB03A4657E=T1 result.json / 802DECE2286A=add_T | **非 D 族（哈希指纹）** | `F256` | E1 |
| 476 | `results/_v4_evidence_audit_reconcile_2026_09_26.md` | 127 | 73 | `D6` | `D6CB03A4657E`（12） | _supp_t1_result.json' (82,365 B / SHA-12=' ⏎ `D6CB03A4657E` ⏎ CB03A4657E') \| 'D6CB03A4657E' \| 82,365 \| t1_re | **非 D 族（哈希指纹）** | `F256` | E1 |
| 477 | `results/_v4_evidence_audit_reconcile_2026_09_26.md` | 127 | 91 | `D6` | `D6CB03A4657E`（12） | on' (82,365 B / SHA-12='D6CB03A4657E') \| ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' \| 82,365 \| t1_result.json ✓ \|\\n\| L | **非 D 族（哈希指纹）** | `F256` | E1 |
| 478 | `results/_v4_evidence_audit_reconcile_2026_09_26.md` | 134 | 52 | `D6` | `D6CB03A4657E`（12） | lt \| 'results/_v4_supp_t1_result.json' \| ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' \| 'D6CB03A4657E' \| 82,365 \| ✓ \|\\n\| | **非 D 族（哈希指纹）** | `F256` | E1 |
| 479 | `results/_v4_evidence_audit_reconcile_2026_09_26.md` | 134 | 69 | `D6` | `D6CB03A4657E`（12） | _supp_t1_result.json' \| 'D6CB03A4657E' \| ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' \| 82,365 \| ✓ \|\\n\| T1 executor \| 'r | **非 D 族（哈希指纹）** | `F256` | E1 |
| 480 | `results/_v4_evidence_audit_reconcile_2026_09_26.md` | 139 | 47 | `D6` | `D6CB03A4657E`（12） | erdict.md 自报 SHA 表**自洽**（t1_result.json =  ⏎ `D6CB03A4657E` ⏎ CB03A4657E；add_T1 = 802DECE2286A；自件 SHA 未列因自指回 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 481 | `results/_v4_evidence_audit_reconcile_2026_09_26.md` | 154 | 67 | `D6` | `D6CB03A4657E`（12） | *标签互换**——实情是 F1B5E49F3058 = t1_verdict.md， ⏎ `D6CB03A4657E` ⏎ CB03A4657E = t1_result.json，但 v3 棒反写为「D6CB03A4 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 482 | `results/_v4_evidence_audit_reconcile_2026_09_26.md` | 154 | 107 | `D6` | `D6CB03A4657E`（12） | d，D6CB03A4657E = t1_result.json，但 v3 棒反写为「 ⏎ `D6CB03A4657E` ⏎ CB03A4657E = T1 verdict 锚 / F1B5E49F3058 = T1. | **非 D 族（哈希指纹）** | `F256` | E1 |
| 483 | `results/_v4_evidence_audit_reconcile_2026_09_26.md` | 156 | 51 | `D6` | `D6CB03A4657E`（12） | s 实测**：用户预期「F1B5E49F3058 = T1 verdict ✓ /  ⏎ `D6CB03A4657E` ⏎ CB03A4657E = T1 result / 该棒标签互换」**全部命中**。本审链仅记 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 484 | `results/_v4_evidence_audit_reconcile_2026_09_26.md` | 208 | 24 | `D6` | `D6CB03A4657E`（12） | 09_24.md'（add_T1）\\n> - cleanup v3 棒 L37 标  ⏎ `D6CB03A4657E` ⏎ CB03A4657E 为「T1 verdict 锚」 → 实际 D6CB03A4657E = | **非 D 族（哈希指纹）** | `F256` | E1 |
| 485 | `results/_v4_evidence_audit_reconcile_2026_09_26.md` | 208 | 58 | `D6` | `D6CB03A4657E`（12） | 棒 L37 标 D6CB03A4657E 为「T1 verdict 锚」 → 实际  ⏎ `D6CB03A4657E` ⏎ CB03A4657E = 'results/_v4_supp_t1_result.json' | **非 D 族（哈希指纹）** | `F256` | E1 |
| 486 | `results/_v4_evidence_audit_reconcile_2026_09_26.md` | 212 | 8 | `D6` | `D6CB03A4657E`（12） | supp_t1_verdict.md' / 27,538 B) ✓\\n>   - ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' = T1 result ('_v4_supp_t1_result.j | **非 D 族（哈希指纹）** | `F256` | E1 |
| 487 | `results/_v4_evidence_audit_reconcile_2026_09_26.md` | 217 | 44 | `D6` | `D6CB03A4657E`（12） |  - **t1_verdict.md 自报 SHA 表（L13-18）字面自洽**（ ⏎ `D6CB03A4657E` ⏎ CB03A4657E = result / 802DECE2286A = add_T1 /  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 488 | `results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` | 148 | 59 | `D74` | `D74D6B39D1B0`（12） | c_a3_clipping_2026_09_15.json' \| 1,265 \| ' ⏎ `D74D6B39D1B0` ⏎ D6B39D1B0' \| 'deposon-sub\\results\\attack_pc_a3 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 489 | `results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` | 150 | 58 | `D3` | `D3F72F67977D`（12） | or_cache_v18_contamination.json' \| 639 \| ' ⏎ `D3F72F67977D` ⏎ F72F67977D' \| 'deposon-sub\\results\\llm_prior_c | **非 D 族（哈希指纹）** | `F12` | E3 |
| 490 | `results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` | 198 | 80 | `D96` | `D96B747BFC6C`（12） | addendum_d3b_2026_09_26.json' \| 14,722 \| ' ⏎ `D96B747BFC6C` ⏎ B747BFC6C' \| 未触动 ✓ (PI CoT v2 dataset addendum | **非 D 族（哈希指纹）** | `F256` | E1 |
| 491 | `results/_v4_pi_cot_v2_coding_review_2026_09_26.md` | 29 | 58 | `D96` | `D96B747BFC6C`（12） | 2_dataset_addendum_d3b_2026_09_26.json' \|  ⏎ `D96B747BFC6C` ⏎ B747BFC6C \| D96B747BFC6C \| ✓ \|\\n\| '_v4_pi_cot_ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 492 | `results/_v4_pi_cot_v2_coding_review_2026_09_26.md` | 29 | 73 | `D96` | `D96B747BFC6C`（12） | dum_d3b_2026_09_26.json' \| D96B747BFC6C \|  ⏎ `D96B747BFC6C` ⏎ B747BFC6C \| ✓ \|\\n\| '_v4_pi_cot_v2_dataset_adde | **非 D 族（哈希指纹）** | `F256` | E1 |
| 493 | `results/_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | 29 | 35 | `D96` | `D96B747BFC6C`（12） | json",\\n    "d3_wave2_anchor_sha12_pre": " ⏎ `D96B747BFC6C` ⏎ B747BFC6C",\\n    "d3_wave2_anchor_sha12_post": | **非 D 族（哈希指纹）** | `F256` | E1 |
| 494 | `results/_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | 30 | 36 | `D96` | `D96B747BFC6C`（12） | C6C",\\n    "d3_wave2_anchor_sha12_post": " ⏎ `D96B747BFC6C` ⏎ B747BFC6C",\\n    "touch_policy": "0 触动(本件落盘前后  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 495 | `results/_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | 42 | 2916 | `D96` | `D96B747BFC6C`（12） | 锚值校准] 本件 d3_wave2_anchor_sha12_pre/post =  ⏎ `D96B747BFC6C` ⏎ B747BFC6C(文件实际 SHA-12),与 d3b 自报 fingerprint_se | **非 D 族（哈希指纹）** | `F256` | E1 |
| 496 | `results/_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | 171 | 575 | `D96` | `D96B747BFC6C`（12） | E104E2DB038); D3 wave2 件落盘前后 SHA-12 复验不变 ( ⏎ `D96B747BFC6C` ⏎ B747BFC6C -> D96B747BFC6C,文件实际 SHA-12,与 d3b 自报 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 497 | `results/_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | 171 | 591 | `D96` | `D96B747BFC6C`（12） |  wave2 件落盘前后 SHA-12 复验不变 (D96B747BFC6C ->  ⏎ `D96B747BFC6C` ⏎ B747BFC6C,文件实际 SHA-12,与 d3b 自报 fingerprint_sel | **非 D 族（哈希指纹）** | `F256` | E1 |
| 498 | `results/_v4_pi_cot_v2_prereg.md` | 6 | 38 | `D279` | `D279EBDE5E84`（12） | ）**\\n- **v1 锚点**：预登记 '696af9121d9f' / 判定 ' ⏎ `D279EBDE5E84` ⏎ EBDE5E84'（E-25 改判假证伪素材面 + E-26 claim 定位偏差注记）\\n | **非 D 族（哈希指纹）** | `F12` | E3 |
| 499 | `results/_v4_pi_cot_v2_result_v2.json` | 48 | 21 | `D96` | `D96B747BFC6C`（12） | ": "6E104E2DB038",\\r\\n   "ADDENDUM_D3B": " ⏎ `D96B747BFC6C` ⏎ B747BFC6C",\\r\\n   "ADDENDUM_D3C": "401BD614CDF | **非 D 族（哈希指纹）** | `F256` | E1 |
| 500 | `results/_v4_pi_cot_v2_ruleset_v2.json` | 48 | 21 | `D96` | `D96B747BFC6C`（12） | ": "6E104E2DB038",\\r\\n   "ADDENDUM_D3B": " ⏎ `D96B747BFC6C` ⏎ B747BFC6C",\\r\\n   "ADDENDUM_D3C": "401BD614CDF | **非 D 族（哈希指纹）** | `F256` | E1 |
| 501 | `results/_v4_pi_cot_v2_ruleset_v2_executor.py` | 149 | 22 | `D96` | `D96B747BFC6C`（12） | A": "6E104E2DB038",\\n    "ADDENDUM_D3B": " ⏎ `D96B747BFC6C` ⏎ B747BFC6C",\\n    "ADDENDUM_D3C": "401BD614CDF7 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 502 | `results/_v4_pi_cot_v3_dataset.json` | 94 | 21 | `D96` | `D96B747BFC6C`（12） | 3b_2026_09_26.json",\\n      "sha12_pre": " ⏎ `D96B747BFC6C` ⏎ B747BFC6C",\\n      "sha12_post": "D96B747BFC6C | **非 D 族（哈希指纹）** | `F256` | E1 |
| 503 | `results/_v4_pi_cot_v3_dataset.json` | 95 | 22 | `D96` | `D96B747BFC6C`（12） | e": "D96B747BFC6C",\\n      "sha12_post": " ⏎ `D96B747BFC6C` ⏎ B747BFC6C",\\n      "touch_policy": "0 触动",\\n   | **非 D 族（哈希指纹）** | `F256` | E1 |
| 504 | `results/_v4_pi_cot_v3_dataset.json` | 238 | 68 | `D96` | `D96B747BFC6C`（12） | _v2_dataset_addendum_d3b_2026_09_26.json ( ⏎ `D96B747BFC6C` ⏎ B747BFC6C)",\\n      "results/_v4_pi_cot_v2_dat | **非 D 族（哈希指纹）** | `F256` | E1 |
| 505 | `results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json` | 38 | 35 | `D96` | `D96B747BFC6C`（12） | json",\\n    "d3_wave2_anchor_sha12_pre": " ⏎ `D96B747BFC6C` ⏎ B747BFC6C",\\n    "d3_wave2_anchor_sha12_post": | **非 D 族（哈希指纹）** | `F256` | E1 |
| 506 | `results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json` | 39 | 36 | `D96` | `D96B747BFC6C`（12） | C6C",\\n    "d3_wave2_anchor_sha12_post": " ⏎ `D96B747BFC6C` ⏎ B747BFC6C",\\n    "d3_wave3_anchor_path": "resu | **非 D 族（哈希指纹）** | `F256` | E1 |
| 507 | `results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json` | 190 | 530 | `D96` | `D96B747BFC6C`（12） | e1 6E104E2DB038 -> 6E104E2DB038; d3 wave2  ⏎ `D96B747BFC6C` ⏎ B747BFC6C -> D96B747BFC6C; d3 wave3 401BD614CD | **非 D 族（哈希指纹）** | `F256` | E1 |
| 508 | `results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json` | 190 | 546 | `D96` | `D96B747BFC6C`（12） | -> 6E104E2DB038; d3 wave2 D96B747BFC6C ->  ⏎ `D96B747BFC6C` ⏎ B747BFC6C; d3 wave3 401BD614CDF7 -> 401BD614CD | **非 D 族（哈希指纹）** | `F256` | E1 |
| 509 | `results/_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json` | 254 | 21 | `D96` | `D96B747BFC6C`（12） | 3b_2026_09_26.json",\\n          "sha12": " ⏎ `D96B747BFC6C` ⏎ B747BFC6C",\\n          "n_supplements": 4,\\n   | **非 D 族（哈希指纹）** | `F256` | E1 |
| 510 | `results/_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json` | 320 | 40 | `D1` | `D1C681D275E0`（12） | ,\\n  "fingerprint_self_hash_post_birth": " ⏎ `D1C681D275E0` ⏎ C681D275E0",\\n  "metadata": {\\n    "author": " | **非 D 族（哈希指纹）** | `F12` | E3 |
| 511 | `results/_v4_pi_cot_v3_dataset_addendum_d5_2026_09_27.json` | 42 | 35 | `D96` | `D96B747BFC6C`（12） | json",\\n    "d3_wave2_anchor_sha12_pre": " ⏎ `D96B747BFC6C` ⏎ B747BFC6C",\\n    "d3_wave2_anchor_sha12_post": | **非 D 族（哈希指纹）** | `F256` | E1 |
| 512 | `results/_v4_pi_cot_v3_dataset_addendum_d5_2026_09_27.json` | 43 | 36 | `D96` | `D96B747BFC6C`（12） | C6C",\\n    "d3_wave2_anchor_sha12_post": " ⏎ `D96B747BFC6C` ⏎ B747BFC6C",\\n    "d3_wave3_anchor_path": "resu | **非 D 族（哈希指纹）** | `F256` | E1 |
| 513 | `results/_v4_pi_cot_v3_dataset_addendum_d5_2026_09_27.json` | 136 | 650 | `D96` | `D96B747BFC6C`（12） | e1 6E104E2DB038 -> 6E104E2DB038; d3 wave2  ⏎ `D96B747BFC6C` ⏎ B747BFC6C -> D96B747BFC6C; d3 wave3 401BD614CD | **非 D 族（哈希指纹）** | `F256` | E1 |
| 514 | `results/_v4_pi_cot_v3_dataset_addendum_d5_2026_09_27.json` | 136 | 666 | `D96` | `D96B747BFC6C`（12） | -> 6E104E2DB038; d3 wave2 D96B747BFC6C ->  ⏎ `D96B747BFC6C` ⏎ B747BFC6C; d3 wave3 401BD614CDF7 -> 401BD614CD | **非 D 族（哈希指纹）** | `F256` | E1 |
| 515 | `results/_v4_pi_cot_v3_result_v3.json` | 753 | 26 | `D96` | `D96B747BFC6C`（12） | 26_09_26.json",\\n      "expected_sha12": " ⏎ `D96B747BFC6C` ⏎ B747BFC6C",\\n      "actual_sha12": "D96B747BFC | **非 D 族（哈希指纹）** | `F256` | E1 |
| 516 | `results/_v4_pi_cot_v3_result_v3.json` | 754 | 24 | `D96` | `D96B747BFC6C`（12） | : "D96B747BFC6C",\\n      "actual_sha12": " ⏎ `D96B747BFC6C` ⏎ B747BFC6C",\\n      "drift": false\\n    },\\n    | **非 D 族（哈希指纹）** | `F256` | E1 |
| 517 | `results/_v4_pi_cot_v3_result_v3.json` | 815 | 68 | `D96` | `D96B747BFC6C`（12） | _v2_dataset_addendum_d3b_2026_09_26.json ( ⏎ `D96B747BFC6C` ⏎ B747BFC6C)",\\n      "results/_v4_pi_cot_v2_dat | **非 D 族（哈希指纹）** | `F256` | E1 |
| 518 | `results/_v4_pi_cot_v3_ruleset_v3_executor.py` | 186 | 22 | `D96` | `D96B747BFC6C`（12） | A": "6E104E2DB038",\\n    "ADDENDUM_D3B": " ⏎ `D96B747BFC6C` ⏎ B747BFC6C",\\n    "ADDENDUM_D3C": "401BD614CDF7 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 519 | `results/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py` | 215 | 22 | `D96` | `D96B747BFC6C`（12） | A": "6E104E2DB038",\\n    "ADDENDUM_D3B": " ⏎ `D96B747BFC6C` ⏎ B747BFC6C",\\n    "ADDENDUM_D3C": "401BD614CDF7 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 520 | `results/_v4_supp_l14v3_batch10_r2_executor.py` | 10 | 35 | `D4` | `D4DD5C949443`（12） | ) 接力棒」\\n  - 沿 batch10 r1 executor (SHA-12  ⏎ `D4DD5C949443` ⏎ DD5C949443) + r1 result (SHA-12 14DDDB13D658)  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 521 | `results/_v4_supp_l14v3_batch10_r2_executor.py` | 38 | 34 | `D4` | `D4DD5C949443`（12） |  -> _r2\\n  3. predecessor 链改: r1_executor  ⏎ `D4DD5C949443` ⏎ DD5C949443 + r1_result 14DDDB13D658 + mapping  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 522 | `results/_v4_supp_l14v3_batch10_r2_executor.py` | 897 | 57 | `D4` | `D4DD5C949443`（12） | ndpoint_selection_method": "沿 r1 executor  ⏎ `D4DD5C949443` ⏎ DD5C949443 端点实测 = mimo mimo-v2.6-pro (无代理)",\\n | **非 D 族（哈希指纹）** | `F256` | E1 |
| 523 | `results/_v4_supp_l14v3_batch10_r2_executor.py` | 925 | 61 | `D4` | `D4DD5C949443`（12） | 1_status": "retry 修复 + tracking 改进沿 r1 (沿  ⏎ `D4DD5C949443` ⏎ DD5C949443)",\\n                "r2_status": "r | **非 D 族（哈希指纹）** | `F256` | E1 |
| 524 | `results/_v4_supp_l14v3_batch10_r2_executor.py` | 938 | 55 | `D4` | `D4DD5C949443`（12） |     "3. predecessor_sha12 链改: r1_executor  ⏎ `D4DD5C949443` ⏎ DD5C949443 + r1_result 14DDDB13D658 + mapping  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 525 | `results/_v4_supp_l14v3_batch10_r2_result.json` | 195 | 45 | `D4` | `D4DD5C949443`（12） |     "3. predecessor_sha12 链改: r1_executor  ⏎ `D4DD5C949443` ⏎ DD5C949443 + r1_result 14DDDB13D658 + mapping  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 526 | `results/_v4_supp_l14v3_batch10_r2_result.json` | 208 | 49 | `D4` | `D4DD5C949443`（12） | ndpoint_selection_method": "沿 r1 executor  ⏎ `D4DD5C949443` ⏎ DD5C949443 端点实测 = mimo mimo-v2.6-pro (无代理)",\\n | **非 D 族（哈希指纹）** | `F256` | E1 |
| 527 | `results/_v4_supp_l14v3_batch10_r2_result.json` | 321 | 51 | `D4` | `D4DD5C949443`（12） | 1_status": "retry 修复 + tracking 改进沿 r1 (沿  ⏎ `D4DD5C949443` ⏎ DD5C949443)",\\n      "r2_status": "retry 修复沿 r | **非 D 族（哈希指纹）** | `F256` | E1 |
| 528 | `results/_v4_supp_l14v3_batch10_r4_executor.py` | 12 | 35 | `D4` | `D4DD5C949443`（12） | 工单 §1)\\n  - 沿 batch10 r1 executor (SHA-12  ⏎ `D4DD5C949443` ⏎ DD5C949443) + r1 result (SHA-12 14DDDB13D658)  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 529 | `results/_v4_supp_l14v3_batch2_r2_executor.py` | 12 | 55 | `D245` | `D245AE4CE385`（12） | il 版）executor 'E52F930654D3' + r1 result ' ⏎ `D245AE4CE385` ⏎ AE4CE385' 探活记录\\n- 沿 /v1/models 探活 '_v4_supp_l1 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 530 | `results/_v4_supp_l14v3_batch2_r2_executor.py` | 62 | 50 | `D245` | `D245AE4CE385`（12） | 件（r1 executor 'E52F930654D3' + r1 result ' ⏎ `D245AE4CE385` ⏎ AE4CE385' + batch1 r6 双件不动）\\n\\n【产物】\\n--------- | **非 D 族（哈希指纹）** | `F256` | E1 |
| 531 | `results/_v4_supp_l14v3_batch2_r2_executor.py` | 67 | 18 | `D245` | `D245AE4CE385`（12） | 1' + batch=2 + round=2）\\n- 不覆盖 r1 result ' ⏎ `D245AE4CE385` ⏎ AE4CE385' 或 batch1 r6 result 'a4f851154551'\\n- | **非 D 族（哈希指纹）** | `F256` | E1 |
| 532 | `results/_v4_supp_l14v3_batch2_r2_executor.py` | 78 | 66 | `D245` | `D245AE4CE385`（12） | 增：r1_executor 'E52F930654D3' + r1_result ' ⏎ `D245AE4CE385` ⏎ AE4CE385'\\n8. 新增 'models_listing_summary' 块：44 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 533 | `results/_v4_supp_l14v3_batch2_r2_executor.py` | 85 | 53 | `D245` | `D245AE4CE385`（12） | 含 r1 executor 'E52F930654D3' + r1 result ' ⏎ `D245AE4CE385` ⏎ AE4CE385' + batch1 r6 executor '5f02c7e0f094'  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 534 | `results/_v4_supp_l14v3_batch2_r2_executor.py` | 632 | 41 | `D245` | `D245AE4CE385`（12） | \\n                    "r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                    "r1_result_pat | **非 D 族（哈希指纹）** | `F256` | E1 |
| 535 | `results/_v4_supp_l14v3_batch2_r2_executor.py` | 899 | 37 | `D245` | `D245AE4CE385`（12） | py",\\n                "r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                "r1_result_path":  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 536 | `results/_v4_supp_l14v3_batch2_r2_executor.py` | 970 | 81 | `D245` | `D245AE4CE385`（12） | 链新增: r1_executor E52F930654D3 + r1_result  ⏎ `D245AE4CE385` ⏎ AE4CE385 + models_probe 3C9DC60B5071",\\n       | **非 D 族（哈希指纹）** | `F256` | E1 |
| 537 | `results/_v4_supp_l14v3_batch2_r2_result.json` | 12 | 27 | `D245` | `D245AE4CE385`（12） | xecutor.py",\\r\\n      "r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\r\\n      "r1_result_path": "results | **非 D 族（哈希指纹）** | `F256` | E1 |
| 538 | `results/_v4_supp_l14v3_batch2_r2_result.json` | 78 | 71 | `D245` | `D245AE4CE385`（12） | 链新增: r1_executor E52F930654D3 + r1_result  ⏎ `D245AE4CE385` ⏎ AE4CE385 + models_probe 3C9DC60B5071",\\r\\n     | **非 D 族（哈希指纹）** | `F256` | E1 |
| 539 | `results/_v4_supp_l14v3_batch2_r3_executor.py` | 66 | 79 | `D245` | `D245AE4CE385`（12） | ch1 r6 result 'A4F851154551' 或 r1 result ' ⏎ `D245AE4CE385` ⏎ AE4CE385'\\n- predecessor_sha12 链：r2_executor/r | **非 D 族（哈希指纹）** | `F256` | E1 |
| 540 | `results/_v4_supp_l14v3_batch2_r3_executor.py` | 86 | 179 | `D245` | `D245AE4CE385`（12） | + r1 executor 'E52F930654D3' + r1 result ' ⏎ `D245AE4CE385` ⏎ AE4CE385' + models_probe '3C9DC60B5071' + prer | **非 D 族（哈希指纹）** | `F256` | E1 |
| 541 | `results/_v4_supp_l14v3_batch2_r3_executor.py` | 624 | 41 | `D245` | `D245AE4CE385`（12） | \\n                    "r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                    "r1_result_pat | **非 D 族（哈希指纹）** | `F256` | E1 |
| 542 | `results/_v4_supp_l14v3_batch2_r3_executor.py` | 897 | 37 | `D245` | `D245AE4CE385`（12） | py",\\n                "r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                "r1_result_path":  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 543 | `results/_v4_supp_l14v3_batch2_r3_result.json` | 20 | 27 | `D245` | `D245AE4CE385`（12） | xecutor.py",\\r\\n      "r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\r\\n      "r1_result_path": "results | **非 D 族（哈希指纹）** | `F256` | E1 |
| 544 | `results/_v4_supp_l14v3_batch2_r4_executor.py` | 90 | 235 | `D245` | `D245AE4CE385`（12） | + r1 executor 'E52F930654D3' + r1 result ' ⏎ `D245AE4CE385` ⏎ AE4CE385' + models_probe '3C9DC60B5071' + prer | **非 D 族（哈希指纹）** | `F256` | E1 |
| 545 | `results/_v4_supp_l14v3_batch2_r4_executor.py` | 635 | 41 | `D245` | `D245AE4CE385`（12） | \\n                    "r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                    "r1_result_pat | **非 D 族（哈希指纹）** | `F256` | E1 |
| 546 | `results/_v4_supp_l14v3_batch2_r4_executor.py` | 912 | 37 | `D245` | `D245AE4CE385`（12） | py",\\n                "r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                "r1_result_path":  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 547 | `results/_v4_supp_l14v3_batch2_r4_result.json` | 24 | 27 | `D245` | `D245AE4CE385`（12） | xecutor.py",\\r\\n      "r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\r\\n      "r1_result_path": "results | **非 D 族（哈希指纹）** | `F256` | E1 |
| 548 | `results/_v4_supp_l14v3_batch2_r5_executor.py` | 11 | 25 | `D9` | `D9FE7AA2D292`（12） | ----------------\\n- 沿 batch2 r4 executor ' ⏎ `D9FE7AA2D292` ⏎ FE7AA2D292' + r4 result '15B8DDC5BA9E' 口径（基础口径 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 549 | `results/_v4_supp_l14v3_batch2_r5_executor.py` | 64 | 23 | `D9` | `D9FE7AA2D292`（12） |  0 产物；探活计入 calls 账\\n- 不覆盖既有件（r4 executor ' ⏎ `D9FE7AA2D292` ⏎ FE7AA2D292' + r4 result '15B8DDC5BA9E' + r3 +  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 550 | `results/_v4_supp_l14v3_batch2_r5_executor.py` | 80 | 37 | `D9` | `D9FE7AA2D292`（12） | ack）\\n7. predecessor_sha12 链：r4_executor ' ⏎ `D9FE7AA2D292` ⏎ FE7AA2D292' + r4_result '15B8DDC5BA9E'（新增；r3/r | **非 D 族（哈希指纹）** | `F256` | E1 |
| 551 | `results/_v4_supp_l14v3_batch2_r5_executor.py` | 93 | 26 | `D9` | `D9FE7AA2D292`（12） | 边界】\\n----------\\n- 不动任何既有件（含 r4 executor ' ⏎ `D9FE7AA2D292` ⏎ FE7AA2D292' + r4 result '15B8DDC5BA9E' + r3 ex | **非 D 族（哈希指纹）** | `F256` | E1 |
| 552 | `results/_v4_supp_l14v3_batch2_r5_executor.py` | 93 | 291 | `D245` | `D245AE4CE385`（12） | + r1 executor 'E52F930654D3' + r1 result ' ⏎ `D245AE4CE385` ⏎ AE4CE385' + models_probe '3C9DC60B5071' + prer | **非 D 族（哈希指纹）** | `F256` | E1 |
| 553 | `results/_v4_supp_l14v3_batch2_r5_executor.py` | 627 | 43 | `D9` | `D9FE7AA2D292`（12） |                     "r4_executor_sha12": " ⏎ `D9FE7AA2D292` ⏎ FE7AA2D292",\\n                    "r4_executor | **非 D 族（哈希指纹）** | `F256` | E1 |
| 554 | `results/_v4_supp_l14v3_batch2_r5_executor.py` | 645 | 41 | `D245` | `D245AE4CE385`（12） | \\n                    "r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                    "r1_result_pat | **非 D 族（哈希指纹）** | `F256` | E1 |
| 555 | `results/_v4_supp_l14v3_batch2_r5_executor.py` | 908 | 39 | `D9` | `D9FE7AA2D292`（12） |  {\\n                "r4_executor_sha12": " ⏎ `D9FE7AA2D292` ⏎ FE7AA2D292",\\n                "r4_executor_pat | **非 D 族（哈希指纹）** | `F256` | E1 |
| 556 | `results/_v4_supp_l14v3_batch2_r5_executor.py` | 926 | 37 | `D245` | `D245AE4CE385`（12） | py",\\n                "r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                "r1_result_path":  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 557 | `results/_v4_supp_l14v3_batch2_r5_executor.py` | 998 | 54 | `D9` | `D9FE7AA2D292`（12） |      "7. predecessor_sha12 链: r4_executor  ⏎ `D9FE7AA2D292` ⏎ FE7AA2D292 + r4_result 15B8DDC5BA9E (新增；r3/r2/ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 558 | `results/_v4_supp_l14v3_batch2_r5_result.json` | 10 | 29 | `D9` | `D9FE7AA2D292`（12） | _sha12": {\\r\\n      "r4_executor_sha12": " ⏎ `D9FE7AA2D292` ⏎ FE7AA2D292",\\r\\n      "r4_executor_path": "res | **非 D 族（哈希指纹）** | `F256` | E1 |
| 559 | `results/_v4_supp_l14v3_batch2_r5_result.json` | 28 | 27 | `D245` | `D245AE4CE385`（12） | xecutor.py",\\r\\n      "r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\r\\n      "r1_result_path": "results | **非 D 族（哈希指纹）** | `F256` | E1 |
| 560 | `results/_v4_supp_l14v3_batch2_r5_result.json` | 93 | 44 | `D9` | `D9FE7AA2D292`（12） |      "7. predecessor_sha12 链: r4_executor  ⏎ `D9FE7AA2D292` ⏎ FE7AA2D292 + r4_result 15B8DDC5BA9E (新增；r3/r2/ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 561 | `results/_v4_supp_l14v3_batch2_r6_result.json` | 14 | 29 | `D9` | `D9FE7AA2D292`（12） | ult.json",\\r\\n      "r4_executor_sha12": " ⏎ `D9FE7AA2D292` ⏎ FE7AA2D292",\\r\\n      "r4_executor_path": "res | **非 D 族（哈希指纹）** | `F256` | E1 |
| 562 | `results/_v4_supp_l14v3_batch2_r6_result.json` | 32 | 27 | `D245` | `D245AE4CE385`（12） | xecutor.py",\\r\\n      "r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\r\\n      "r1_result_path": "results | **非 D 族（哈希指纹）** | `F256` | E1 |
| 563 | `results/_v4_supp_l14v3_batch3_r1_executor.py` | 74 | 106 | `D245` | `D245AE4CE385`（12） | ' 或 r2 result '8C125E257AF8' 或 r1 result ' ⏎ `D245AE4CE385` ⏎ AE4CE385'\\n- predecessor_sha12 链：r3_executor ' | **非 D 族（哈希指纹）** | `F256` | E1 |
| 564 | `results/_v4_supp_l14v3_batch3_r1_executor.py` | 99 | 235 | `D245` | `D245AE4CE385`（12） | + r1 executor 'E52F930654D3' + r1 result ' ⏎ `D245AE4CE385` ⏎ AE4CE385' + models_probe '3C9DC60B5071' + prer | **非 D 族（哈希指纹）** | `F256` | E1 |
| 565 | `results/_v4_supp_l14v3_batch3_r1_executor.py` | 648 | 41 | `D245` | `D245AE4CE385`（12） | \\n                    "r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                    "r1_result_pat | **非 D 族（哈希指纹）** | `F256` | E1 |
| 566 | `results/_v4_supp_l14v3_batch3_r1_executor.py` | 955 | 37 | `D245` | `D245AE4CE385`（12） | py",\\n                "r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                "r1_result_path":  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 567 | `results/_v4_supp_l14v3_batch3_r1_result.json` | 26 | 27 | `D245` | `D245AE4CE385`（12） | xecutor.py",\\r\\n      "r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\r\\n      "r1_result_path": "results | **非 D 族（哈希指纹）** | `F256` | E1 |
| 568 | `results/_v4_supp_l14v3_batch3_r2_executor.py` | 11 | 52 | `D24` | `D24B84671C23`（12） | 3 r1 executor 'A4731B39343F' + r1 result ' ⏎ `D24B84671C23` ⏎ B84671C23' 口径锚（GLM_2 教师侧 round 1 reask=0）\\n- 沿 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 569 | `results/_v4_supp_l14v3_batch3_r2_executor.py` | 77 | 50 | `D24` | `D24B84671C23`（12） | 件（r1 executor 'A4731B39343F' + r1 result ' ⏎ `D24B84671C23` ⏎ B84671C23' + r3 executor '72FD2BB3838E' + r3 r | **非 D 族（哈希指纹）** | `F256` | E1 |
| 570 | `results/_v4_supp_l14v3_batch3_r2_executor.py` | 82 | 18 | `D24` | `D24B84671C23`（12） | 1' + batch=3 + round=2）\\n- 不覆盖 r1 result ' ⏎ `D24B84671C23` ⏎ B84671C23' 或 r3 result '25251ACA6D79' 或 r2 res | **非 D 族（哈希指纹）** | `F256` | E1 |
| 571 | `results/_v4_supp_l14v3_batch3_r2_executor.py` | 82 | 102 | `D245` | `D245AE4CE385`（12） |  r2 result '8C125E257AF8' 或 r1 探活 result ' ⏎ `D245AE4CE385` ⏎ AE4CE385' 或 batch1 r6 result 'A4F851154551'\\n- | **非 D 族（哈希指纹）** | `F256` | E1 |
| 572 | `results/_v4_supp_l14v3_batch3_r2_executor.py` | 83 | 63 | `D24` | `D24B84671C23`（12） | 链：r1_executor 'A4731B39343F' + r1_result ' ⏎ `D24B84671C23` ⏎ B84671C23' + r3_executor '72FD2BB3838E' + r3_r | **非 D 族（哈希指纹）** | `F256` | E1 |
| 573 | `results/_v4_supp_l14v3_batch3_r2_executor.py` | 95 | 64 | `D24` | `D24B84671C23`（12） | 链：r1_executor 'A4731B39343F' + r1_result ' ⏎ `D24B84671C23` ⏎ B84671C23'（取代 r1 链的 r3_executor/r3_result 仍保留） | **非 D 族（哈希指纹）** | `F256` | E1 |
| 574 | `results/_v4_supp_l14v3_batch3_r2_executor.py` | 107 | 53 | `D24` | `D24B84671C23`（12） | 含 r1 executor 'A4731B39343F' + r1 result ' ⏎ `D24B84671C23` ⏎ B84671C23' + r3 executor '72FD2BB3838E' + r3 r | **非 D 族（哈希指纹）** | `F256` | E1 |
| 575 | `results/_v4_supp_l14v3_batch3_r2_executor.py` | 107 | 291 | `D245` | `D245AE4CE385`（12） | + r1 executor 'E52F930654D3' + r1 result ' ⏎ `D245AE4CE385` ⏎ AE4CE385' + models_probe '3C9DC60B5071' + prer | **非 D 族（哈希指纹）** | `F256` | E1 |
| 576 | `results/_v4_supp_l14v3_batch3_r2_executor.py` | 657 | 41 | `D24` | `D24B84671C23`（12） | \\n                    "r1_result_sha12": " ⏎ `D24B84671C23` ⏎ B84671C23",\\n                    "r1_result_pa | **非 D 族（哈希指纹）** | `F256` | E1 |
| 577 | `results/_v4_supp_l14v3_batch3_r2_executor.py` | 673 | 44 | `D245` | `D245AE4CE385`（12） |                    "r1_result_sha12_b2": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                    "r1_result_pat | **非 D 族（哈希指纹）** | `F256` | E1 |
| 578 | `results/_v4_supp_l14v3_batch3_r2_executor.py` | 972 | 37 | `D24` | `D24B84671C23`（12） | py",\\n                "r1_result_sha12": " ⏎ `D24B84671C23` ⏎ B84671C23",\\n                "r1_result_path": | **非 D 族（哈希指纹）** | `F256` | E1 |
| 579 | `results/_v4_supp_l14v3_batch3_r2_executor.py` | 988 | 40 | `D245` | `D245AE4CE385`（12） | ,\\n                "r1_result_sha12_b2": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                "r1_result_path_b2 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 580 | `results/_v4_supp_l14v3_batch3_r2_executor.py` | 1065 | 79 | `D24` | `D24B84671C23`（12） | 2 链: r1_executor A4731B39343F + r1_result  ⏎ `D24B84671C23` ⏎ B84671C23 (取代 r1 链的 r3_executor/r3_result 仍保留) | **非 D 族（哈希指纹）** | `F256` | E1 |
| 581 | `results/_v4_supp_l14v3_batch3_r2_result.json` | 14 | 27 | `D24` | `D24B84671C23`（12） | xecutor.py",\\r\\n      "r1_result_sha12": " ⏎ `D24B84671C23` ⏎ B84671C23",\\r\\n      "r1_result_path": "result | **非 D 族（哈希指纹）** | `F256` | E1 |
| 582 | `results/_v4_supp_l14v3_batch3_r2_result.json` | 30 | 30 | `D245` | `D245AE4CE385`（12） | utor.py",\\r\\n      "r1_result_sha12_b2": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\r\\n      "r1_result_path_b2": "resu | **非 D 族（哈希指纹）** | `F256` | E1 |
| 583 | `results/_v4_supp_l14v3_batch3_r2_result.json` | 106 | 69 | `D24` | `D24B84671C23`（12） | 2 链: r1_executor A4731B39343F + r1_result  ⏎ `D24B84671C23` ⏎ B84671C23 (取代 r1 链的 r3_executor/r3_result 仍保留) | **非 D 族（哈希指纹）** | `F256` | E1 |
| 584 | `results/_v4_supp_l14v3_batch3_r3_executor.py` | 12 | 52 | `D24` | `D24B84671C23`（12） | 3 r1 executor 'A4731B39343F' + r1 result ' ⏎ `D24B84671C23` ⏎ B84671C23' 口径（GLM_2 round 1 reask=0）\\n- 沿 batc | **非 D 族（哈希指纹）** | `F256` | E1 |
| 585 | `results/_v4_supp_l14v3_batch3_r3_executor.py` | 79 | 106 | `D24` | `D24B84671C23`（12） | + r1 executor 'A4731B39343F' + r1 result ' ⏎ `D24B84671C23` ⏎ B84671C23' + r3 executor '72FD2BB3838E' + r3 r | **非 D 族（哈希指纹）** | `F256` | E1 |
| 586 | `results/_v4_supp_l14v3_batch3_r3_executor.py` | 84 | 45 | `D24` | `D24B84671C23`（12） | 不覆盖 r2 result '58E9C55A770D' 或 r1 result ' ⏎ `D24B84671C23` ⏎ B84671C23' 或 r3 result '25251ACA6D79' 或 r2 res | **非 D 族（哈希指纹）** | `F256` | E1 |
| 587 | `results/_v4_supp_l14v3_batch3_r3_executor.py` | 84 | 129 | `D245` | `D245AE4CE385`（12） |  r2 result '8C125E257AF8' 或 r1 探活 result ' ⏎ `D245AE4CE385` ⏎ AE4CE385' 或 batch1 r6 result 'A4F851154551'\\n- | **非 D 族（哈希指纹）** | `F256` | E1 |
| 588 | `results/_v4_supp_l14v3_batch3_r3_executor.py` | 85 | 119 | `D24` | `D24B84671C23`（12） | + r1_executor 'A4731B39343F' + r1_result ' ⏎ `D24B84671C23` ⏎ B84671C23' + r3_executor '72FD2BB3838E' + r3_r | **非 D 族（哈希指纹）** | `F256` | E1 |
| 589 | `results/_v4_supp_l14v3_batch3_r3_executor.py` | 109 | 109 | `D24` | `D24B84671C23`（12） | + r1 executor 'A4731B39343F' + r1 result ' ⏎ `D24B84671C23` ⏎ B84671C23' + r3 executor '72FD2BB3838E' + r3 r | **非 D 族（哈希指纹）** | `F256` | E1 |
| 590 | `results/_v4_supp_l14v3_batch3_r3_executor.py` | 109 | 347 | `D245` | `D245AE4CE385`（12） | + r1 executor 'E52F930654D3' + r1 result ' ⏎ `D245AE4CE385` ⏎ AE4CE385' + models_probe '3C9DC60B5071' + prer | **非 D 族（哈希指纹）** | `F256` | E1 |
| 591 | `results/_v4_supp_l14v3_batch3_r3_executor.py` | 664 | 41 | `D24` | `D24B84671C23`（12） | \\n                    "r1_result_sha12": " ⏎ `D24B84671C23` ⏎ B84671C23",\\n                    "r1_result_pa | **非 D 族（哈希指纹）** | `F256` | E1 |
| 592 | `results/_v4_supp_l14v3_batch3_r3_executor.py` | 680 | 44 | `D245` | `D245AE4CE385`（12） |                    "r1_result_sha12_b2": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                    "r1_result_pat | **非 D 族（哈希指纹）** | `F256` | E1 |
| 593 | `results/_v4_supp_l14v3_batch3_r3_executor.py` | 984 | 37 | `D24` | `D24B84671C23`（12） | py",\\n                "r1_result_sha12": " ⏎ `D24B84671C23` ⏎ B84671C23",\\n                "r1_result_path": | **非 D 族（哈希指纹）** | `F256` | E1 |
| 594 | `results/_v4_supp_l14v3_batch3_r3_executor.py` | 1000 | 40 | `D245` | `D245AE4CE385`（12） | ,\\n                "r1_result_sha12_b2": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                "r1_result_path_b2 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 595 | `results/_v4_supp_l14v3_batch3_r3_result.json` | 18 | 27 | `D24` | `D24B84671C23`（12） | xecutor.py",\\r\\n      "r1_result_sha12": " ⏎ `D24B84671C23` ⏎ B84671C23",\\r\\n      "r1_result_path": "result | **非 D 族（哈希指纹）** | `F256` | E1 |
| 596 | `results/_v4_supp_l14v3_batch3_r3_result.json` | 34 | 30 | `D245` | `D245AE4CE385`（12） | utor.py",\\r\\n      "r1_result_sha12_b2": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\r\\n      "r1_result_path_b2": "resu | **非 D 族（哈希指纹）** | `F256` | E1 |
| 597 | `results/_v4_supp_l14v3_batch3_r4_executor.py` | 13 | 52 | `D24` | `D24B84671C23`（12） | 3 r1 executor 'A4731B39343F' + r1 result ' ⏎ `D24B84671C23` ⏎ B84671C23' 口径（GLM_2 round 1 reask=0）\\n- 沿 batc | **非 D 族（哈希指纹）** | `F256` | E1 |
| 598 | `results/_v4_supp_l14v3_batch3_r4_executor.py` | 81 | 162 | `D24` | `D24B84671C23`（12） | + r1 executor 'A4731B39343F' + r1 result ' ⏎ `D24B84671C23` ⏎ B84671C23' + r3 executor '72FD2BB3838E' + r3 r | **非 D 族（哈希指纹）** | `F256` | E1 |
| 599 | `results/_v4_supp_l14v3_batch3_r4_executor.py` | 86 | 72 | `D24` | `D24B84671C23`（12） | ' 或 r2 result '58E9C55A770D' 或 r1 result ' ⏎ `D24B84671C23` ⏎ B84671C23' 或 r3 result '25251ACA6D79' 或 r2 res | **非 D 族（哈希指纹）** | `F256` | E1 |
| 600 | `results/_v4_supp_l14v3_batch3_r4_executor.py` | 86 | 156 | `D245` | `D245AE4CE385`（12） |  r2 result '8C125E257AF8' 或 r1 探活 result ' ⏎ `D245AE4CE385` ⏎ AE4CE385' 或 batch1 r6 result 'A4F851154551'\\n- | **非 D 族（哈希指纹）** | `F256` | E1 |
| 601 | `results/_v4_supp_l14v3_batch3_r4_executor.py` | 87 | 175 | `D24` | `D24B84671C23`（12） | + r1_executor 'A4731B39343F' + r1_result ' ⏎ `D24B84671C23` ⏎ B84671C23' + r3_executor '72FD2BB3838E' + r3_r | **非 D 族（哈希指纹）** | `F256` | E1 |
| 602 | `results/_v4_supp_l14v3_batch3_r4_executor.py` | 99 | 176 | `D24` | `D24B84671C23`（12） | + r1_executor 'A4731B39343F' + r1_result ' ⏎ `D24B84671C23` ⏎ B84671C23' + r3_executor '72FD2BB3838E' + r3_r | **非 D 族（哈希指纹）** | `F256` | E1 |
| 603 | `results/_v4_supp_l14v3_batch3_r4_executor.py` | 111 | 165 | `D24` | `D24B84671C23`（12） | + r1 executor 'A4731B39343F' + r1 result ' ⏎ `D24B84671C23` ⏎ B84671C23' + r3 executor '72FD2BB3838E' + r3 r | **非 D 族（哈希指纹）** | `F256` | E1 |
| 604 | `results/_v4_supp_l14v3_batch3_r4_executor.py` | 111 | 403 | `D245` | `D245AE4CE385`（12） | + r1 executor 'E52F930654D3' + r1 result ' ⏎ `D245AE4CE385` ⏎ AE4CE385' + models_probe '3C9DC60B5071' + prer | **非 D 族（哈希指纹）** | `F256` | E1 |
| 605 | `results/_v4_supp_l14v3_batch3_r4_executor.py` | 673 | 41 | `D24` | `D24B84671C23`（12） | \\n                    "r1_result_sha12": " ⏎ `D24B84671C23` ⏎ B84671C23",\\n                    "r1_result_pa | **非 D 族（哈希指纹）** | `F256` | E1 |
| 606 | `results/_v4_supp_l14v3_batch3_r4_executor.py` | 689 | 44 | `D245` | `D245AE4CE385`（12） |                    "r1_result_sha12_b2": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                    "r1_result_pat | **非 D 族（哈希指纹）** | `F256` | E1 |
| 607 | `results/_v4_supp_l14v3_batch3_r4_executor.py` | 998 | 37 | `D24` | `D24B84671C23`（12） | py",\\n                "r1_result_sha12": " ⏎ `D24B84671C23` ⏎ B84671C23",\\n                "r1_result_path": | **非 D 族（哈希指纹）** | `F256` | E1 |
| 608 | `results/_v4_supp_l14v3_batch3_r4_executor.py` | 1014 | 40 | `D245` | `D245AE4CE385`（12） | ,\\n                "r1_result_sha12_b2": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                "r1_result_path_b2 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 609 | `results/_v4_supp_l14v3_batch3_r4_result.json` | 22 | 27 | `D24` | `D24B84671C23`（12） | xecutor.py",\\r\\n      "r1_result_sha12": " ⏎ `D24B84671C23` ⏎ B84671C23",\\r\\n      "r1_result_path": "result | **非 D 族（哈希指纹）** | `F256` | E1 |
| 610 | `results/_v4_supp_l14v3_batch3_r4_result.json` | 38 | 30 | `D245` | `D245AE4CE385`（12） | utor.py",\\r\\n      "r1_result_sha12_b2": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\r\\n      "r1_result_path_b2": "resu | **非 D 族（哈希指纹）** | `F256` | E1 |
| 611 | `results/_v4_supp_l14v3_batch3_r5_result.json` | 26 | 27 | `D24` | `D24B84671C23`（12） | xecutor.py",\\r\\n      "r1_result_sha12": " ⏎ `D24B84671C23` ⏎ B84671C23",\\r\\n      "r1_result_path": "result | **非 D 族（哈希指纹）** | `F256` | E1 |
| 612 | `results/_v4_supp_l14v3_batch3_r5_result.json` | 42 | 30 | `D245` | `D245AE4CE385`（12） | utor.py",\\r\\n      "r1_result_sha12_b2": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\r\\n      "r1_result_path_b2": "resu | **非 D 族（哈希指纹）** | `F256` | E1 |
| 613 | `results/_v4_supp_l14v3_batch5_r1_executor.py` | 66 | 232 | `D245` | `D245AE4CE385`（12） | + r1 executor 'E52F930654D3' + r1 result ' ⏎ `D245AE4CE385` ⏎ AE4CE385' + models_probe '3C9DC60B5071' + mapp | **非 D 族（哈希指纹）** | `F256` | E1 |
| 614 | `results/_v4_supp_l14v3_batch5_r1_executor.py` | 71 | 106 | `D245` | `D245AE4CE385`（12） | ch1 r6 result 'A4F851154551' 或 r1 result ' ⏎ `D245AE4CE385` ⏎ AE4CE385'\\n- predecessor_sha12 链：r3_executor ' | **非 D 族（哈希指纹）** | `F256` | E1 |
| 615 | `results/_v4_supp_l14v3_batch5_r1_executor.py` | 104 | 235 | `D245` | `D245AE4CE385`（12） | + r1 executor 'E52F930654D3' + r1 result ' ⏎ `D245AE4CE385` ⏎ AE4CE385' + models_probe '3C9DC60B5071' + mapp | **非 D 族（哈希指纹）** | `F256` | E1 |
| 616 | `results/_v4_supp_l14v3_batch5_r1_executor.py` | 661 | 41 | `D245` | `D245AE4CE385`（12） | \\n                    "r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                    "r1_result_pat | **非 D 族（哈希指纹）** | `F256` | E1 |
| 617 | `results/_v4_supp_l14v3_batch5_r1_executor.py` | 934 | 37 | `D245` | `D245AE4CE385`（12） | py",\\n                "r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                "r1_result_path":  | **非 D 族（哈希指纹）** | `F256` | E1 |
| 618 | `results/_v4_supp_l14v3_batch5_r1_result.json` | 24 | 27 | `D245` | `D245AE4CE385`（12） | xecutor.py",\\r\\n      "r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\r\\n      "r1_result_path": "results | **非 D 族（哈希指纹）** | `F256` | E1 |
| 619 | `results/_v4_supp_l14v3_batch5_r2_executor.py` | 77 | 325 | `D245` | `D245AE4CE385`（12） | 1_executor 'E52F930654D3' + b2_r1_result ' ⏎ `D245AE4CE385` ⏎ AE4CE385' + models_probe '3C9DC60B5071' + mapp | **非 D 族（哈希指纹）** | `F256` | E1 |
| 620 | `results/_v4_supp_l14v3_batch5_r2_executor.py` | 662 | 44 | `D245` | `D245AE4CE385`（12） |                    "b2_r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                    "b2_r1_result_ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 621 | `results/_v4_supp_l14v3_batch5_r2_executor.py` | 963 | 40 | `D245` | `D245AE4CE385`（12） | ,\\n                "b2_r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                "b2_r1_result_path | **非 D 族（哈希指纹）** | `F256` | E1 |
| 622 | `results/_v4_supp_l14v3_batch5_r2_result.json` | 28 | 30 | `D245` | `D245AE4CE385`（12） | utor.py",\\r\\n      "b2_r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\r\\n      "b2_r1_result_path": "resu | **非 D 族（哈希指纹）** | `F256` | E1 |
| 623 | `results/_v4_supp_l14v3_batch5_r3_executor.py` | 654 | 44 | `D245` | `D245AE4CE385`（12） |                    "b2_r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                    "b2_r1_result_ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 624 | `results/_v4_supp_l14v3_batch5_r3_executor.py` | 960 | 40 | `D245` | `D245AE4CE385`（12） | ,\\n                "b2_r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                "b2_r1_result_path | **非 D 族（哈希指纹）** | `F256` | E1 |
| 625 | `results/_v4_supp_l14v3_batch5_r3_result.json` | 32 | 30 | `D245` | `D245AE4CE385`（12） | utor.py",\\r\\n      "b2_r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\r\\n      "b2_r1_result_path": "resu | **非 D 族（哈希指纹）** | `F256` | E1 |
| 626 | `results/_v4_supp_l14v3_batch5_r4_executor.py` | 664 | 44 | `D245` | `D245AE4CE385`（12） |                    "b2_r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                    "b2_r1_result_ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 627 | `results/_v4_supp_l14v3_batch5_r4_executor.py` | 974 | 40 | `D245` | `D245AE4CE385`（12） | ,\\n                "b2_r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                "b2_r1_result_path | **非 D 族（哈希指纹）** | `F256` | E1 |
| 628 | `results/_v4_supp_l14v3_batch5_r4_result.json` | 36 | 30 | `D245` | `D245AE4CE385`（12） | utor.py",\\r\\n      "b2_r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\r\\n      "b2_r1_result_path": "resu | **非 D 族（哈希指纹）** | `F256` | E1 |
| 629 | `results/_v4_supp_l14v3_batch5_r5_executor.py` | 698 | 44 | `D245` | `D245AE4CE385`（12） |                    "b2_r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                    "b2_r1_result_ | **非 D 族（哈希指纹）** | `F256` | E1 |
| 630 | `results/_v4_supp_l14v3_batch5_r5_executor.py` | 1073 | 40 | `D245` | `D245AE4CE385`（12） | ,\\n                "b2_r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\n                "b2_r1_result_path | **非 D 族（哈希指纹）** | `F256` | E1 |
| 631 | `results/_v4_supp_l14v3_batch5_r5_result.json` | 40 | 30 | `D245` | `D245AE4CE385`（12） | utor.py",\\r\\n      "b2_r1_result_sha12": " ⏎ `D245AE4CE385` ⏎ AE4CE385",\\r\\n      "b2_r1_result_path": "resu | **非 D 族（哈希指纹）** | `F256` | E1 |
| 632 | `results/_v4_supp_t15_verdict.md` | 51 | 94 | `D6` | `D6CB03A4657E`（12） |  模型 + max_tokens=500 修正构造失灵族后空响应消除；vs T1 ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' 49.3% 空响应）\\n- **n_pairs_empty_empt | **非 D 族（哈希指纹）** | `F256` | E1 |
| 633 | `results/_v4_supp_t1_verdict.md` | 15 | 52 | `D6` | `D6CB03A4657E`（12） | lt \| 'results/_v4_supp_t1_result.json' \| ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' \| 'D6CB03A4657E' \| 82,365 \| ✓ \|\\n\| | **非 D 族（哈希指纹）** | `F256` | E1 |
| 634 | `results/_v4_supp_t1_verdict.md` | 15 | 69 | `D6` | `D6CB03A4657E`（12） | _supp_t1_result.json' \| 'D6CB03A4657E' \| ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' \| 82,365 \| ✓ \|\\n\| T1 executor \| 'r | **非 D 族（哈希指纹）** | `F256` | E1 |
| 635 | `results/_v4_supp_t1_verdict.md` | 33 | 21 | `D6` | `D6CB03A4657E`（12） | ct: "PASS (判定稳健)"'\\n\\n### §1.2 执行棒自报关键证据（' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' §honesty_disclosures）\\n\\n- **240 c | **非 D 族（哈希指纹）** | `F256` | E1 |
| 636 | `results/_v4_supp_t1_verdict.md` | 261 | 32 | `D6` | `D6CB03A4657E`（12） | ✓ 未触动（仅读）\\n  - '_v4_supp_t1_result.json' ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' ✓ 未触动（仅读）\\n  - '_v4_supp_prereg_v0 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 637 | `results/_v4_supp_t1_verdict.md` | 318 | 115 | `D6` | `D6CB03A4657E`（12） | 7CAD9228B0B' + '_v4_supp_t1_result.json' ' ⏎ `D6CB03A4657E` ⏎ CB03A4657E' 同级独立）\\n- **锚定 prereg**：'802DECE228 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 638 | `results/_v4_track2_multimodel_rerun.py` | 15 | 68 | `D2` | `D2BD7521D651`（12） | nerators 内 D1 teacher_paths.json (SHA-12 ' ⏎ `D2BD7521D651` ⏎ BD7521D651')\\n- 三槽 (PI 2026-09-23 拍板三 URL + 补充 | **非 D 族（哈希指纹）** | `F12` | E3 |
| 639 | `results/_v4_track2_multimodel_rerun.py` | 67 | 41 | `D2` | `D2BD7521D651`（12） | \\n# 5 教师 (沿 D1 teacher_paths.json, SHA-12  ⏎ `D2BD7521D651` ⏎ BD7521D651)\\nTEACHER_PATHS_REL = [\\n    ("kimi | **非 D 族（哈希指纹）** | `F12` | E3 |
| 640 | `results/_v4_track2_multimodel_rerun.py` | 447 | 35 | `D2` | `D2BD7521D651`（12） | AF67",\\n                "teacher_paths": " ⏎ `D2BD7521D651` ⏎ BD7521D651",\\n                "track2_multimod | **非 D 族（哈希指纹）** | `F12` | E3 |
| 641 | `results/_v4_track2_multimodel_rerun.py` | 802 | 35 | `D2` | `D2BD7521D651`（12） | AF67",\\n                "teacher_paths": " ⏎ `D2BD7521D651` ⏎ BD7521D651",\\n                "track2_product_ | **非 D 族（哈希指纹）** | `F12` | E3 |
| 642 | `results/_v4_track2_multimodel_rerun_2026_09_23.json` | 36 | 25 | `D2` | `D2BD7521D651`（12） |  "21771E66AF67",\\n      "teacher_paths": " ⏎ `D2BD7521D651` ⏎ BD7521D651",\\n      "track2_product_openrouter | **非 D 族（哈希指纹）** | `F12` | E3 |
| 643 | `results/_v5_fake_verdict_session_log_2026_09_28.md` | 28 | 15 | `D30` | `D30EDA5A1063`（12） | k_prereg_v1_2026_09_27.md'\\n> **SHA-12**：' ⏎ `D30EDA5A1063` ⏎ EDA5A1063'（**SHA-256 前 16 = 'D30EDA5A1063F9AD' | **非 D 族（哈希指纹）** | `F1` | E2 |
| 644 | `results/_v5_fake_verdict_session_log_2026_09_28.md` | 28 | 47 | `D30` | `D30EDA5A1063F9AD`（16） | SHA-12**：'D30EDA5A1063'（**SHA-256 前 16 = ' ⏎ `D30EDA5A1063F9AD` ⏎ EDA5A1063F9AD'**）\\n> **字节**：37,346 B｜**行数**：30 | **非 D 族（哈希指纹）** | `F1` | E2 |
| 645 | `results/_v5_fake_verdict_session_log_2026_09_28.md` | 37 | 23 | `D30` | `D30EDA5A1063F9AD`（16） | 895F135' \| — \| — \|\\n\| **SHA-1[:16]** \| **' ⏎ `D30EDA5A1063F9AD` ⏎ EDA5A1063F9AD'** \| 'D30EDA5A1063F9AD'（自标「SHA-2 | **非 D 族（哈希指纹）** | `F1` | E2 |
| 646 | `results/_v5_fake_verdict_session_log_2026_09_28.md` | 37 | 46 | `D30` | `D30EDA5A1063F9AD`（16） | *SHA-1[:16]** \| **'D30EDA5A1063F9AD'** \| ' ⏎ `D30EDA5A1063F9AD` ⏎ EDA5A1063F9AD'（自标「SHA-256」） \| ✅ **逐字命中** \|\\n\|  | **非 D 族（哈希指纹）** | `F1` | E2 |
| 647 | `results/_v5_fake_verdict_session_log_2026_09_28.md` | 38 | 17 | `D30` | `D30EDA5A1063`（12） | SHA-256」） \| ✅ **逐字命中** \|\\n\| SHA-1[:12] \| ' ⏎ `D30EDA5A1063` ⏎ EDA5A1063' \| 'D30EDA5A1063' \| ✅ **逐字命中** \|\\n\|  | **非 D 族（哈希指纹）** | `F1` | E2 |
| 648 | `results/_v5_fake_verdict_session_log_2026_09_28.md` | 38 | 34 | `D30` | `D30EDA5A1063`（12） | 字命中** \|\\n\| SHA-1[:12] \| 'D30EDA5A1063' \| ' ⏎ `D30EDA5A1063` ⏎ EDA5A1063' \| ✅ **逐字命中** \|\\n\| MD5[:12] \| 'AD6BE | **非 D 族（哈希指纹）** | `F1` | E2 |
| 649 | `results/_v5_fake_verdict_session_log_2026_09_28.md` | 61 | 8 | `D9` | `D9E14ED29FB9`（12） | 547329AF2E' \| OK \| **SHA-1 命中** \|\\n\| 1 \| ' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9' \| 'D9E14ED29FB9' \| 'C7C59E0D2F6C'  | **非 D 族（哈希指纹）** | `F1` | E2 |
| 650 | `results/_v5_fake_verdict_session_log_2026_09_28.md` | 61 | 25 | `D9` | `D9E14ED29FB9`（12） | \| **SHA-1 命中** \|\\n\| 1 \| 'D9E14ED29FB9' \| ' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9' \| 'C7C59E0D2F6C' \| OK \| **SHA-1 命中 | **非 D 族（哈希指纹）** | `F1` | E2 |
| 651 | `results/_v5_fake_verdict_session_log_2026_09_28.md` | 64 | 42 | `D6` | `D6F233D73C45`（12） | n\| 4 \| '18C9C370A6AE' \| '18C9C370A6AE' \| ' ⏎ `D6F233D73C45` ⏎ F233D73C45' \| OK \| **SHA-1 命中** \|\\n\| 4-r \| '26 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 652 | `results/_v5_fake_verdict_session_log_2026_09_28.md` | 68 | 42 | `D74` | `D74D6B39D1B0`（12） | n\| 8 \| '717C26DF5A00' \| '717C26DF5A00' \| ' ⏎ `D74D6B39D1B0` ⏎ D6B39D1B0' \| OK \| **SHA-1 命中** \|\\n\| 10 \| '05B4 | **非 D 族（哈希指纹）** | `F256` | E1 |
| 653 | `results/_v5_fake_verdict_session_log_2026_09_28.md` | 98 | 79 | `D9` | `D9E14ED29FB9`（12） | 见下游棒以 SHA-256 复算得 'c7c59e0d2f6c'，与 v1 记录 ' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9' 比对，判「⚠ SHA 不符、字节一致」—— 即**下游已发现不符，但 | **非 D 族（哈希指纹）** | `F1` | E2 |
| 654 | `results/_v5_fake_verdict_session_log_2026_09_28.md` | 145 | 21 | `D9` | `D9E14ED29FB9`（12） | 且 09-27 \| **26 行** \|\\n\| 'data_json LIKE '% ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9%'' \| **13 行**（09-27 首次出现在 **id=4912 | **非 D 族（哈希指纹）** | `F1` | E2 |
| 655 | `results/_v5_r2h2_residual_merged_catalogue_2026_09_29.md` | 301 | 238 | `D9` | `D9E14ED29FB9`（12） | ss_pa_1_rbr_rm_result_2026_09_15.json' 记 ' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9' ＝ SHA-1，实 SHA-256 ＝ 'C7C59E0D2F6C' | **非 D 族（哈希指纹）** | `F1` | E2 |
| 656 | `results/_v5_sub_artifact_ledger_2026_09_28.md` | 113 | 117 | `D9` | `D9E14ED29FB9`（12） | 1 §0.2 三处 SHA-12 与盘上不符**：'boss_pa_1_*'（记 ' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9' / 实测 'c7c59e0d2f6c'）、'_v3x_conserv | **非 D 族（哈希指纹）** | `F1` | E2 |
| 657 | `results/_v5_sub_artifact_ledger_2026_09_28.md` | 177 | 58 | `D9` | `D9E14ED29FB9`（12） | d8b1e08' §1.3-1c \| **1c 反向定位**：SHA-1 系记值（' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9' / '19F0A2CB8CEF' / '1A90FD8F385A'  | **非 D 族（哈希指纹）** | `F1` | E2 |
| 658 | `results/_v5_track2_qwen_retry_2026_09_29.json` | 11 | 19 | `D35` | `D35EE9ECC881`（12） | -23T07:00:05+00:00",\\r\\n    "sha256_12": " ⏎ `D35EE9ECC881` ⏎ EE9ECC881",\\r\\n    "lines_total": 30\\r\\n  },\\r | **非 D 族（哈希指纹）** | `F12` | E3 |
| 659 | `results/_v5_trae_doubt6_verify_2026_09_28_r3verifier.md` | 286 | 55 | `D9` | `D9E14ED29FB9`（12） | HA-1 口径 \| 'sha1(bytes)[:12].upper()' = **' ⏎ `D9E14ED29FB9` ⏎ E14ED29FB9'** = v1 §0.2 行 1 记值 \| ✓ \|\\n\| 「非 sha | **非 D 族（哈希指纹）** | `F1` | E2 |

### §2-1 汇总（按判定码）

| 判定码 | 语义 | run 数 | **处数** |
|---|---|---:|---:|
| `F256` | 真哈希指纹·SHA-256 前缀（在盘实测对撞命中） | 36 | **359** |
| `F1` | 真哈希指纹·SHA-1 前缀（在盘实测对撞命中） | 3 | **45** |
| `F12` | 真哈希指纹·SHA-12 语义（件已不在盘·上下文哈希列定） | 93 | **255** |
| **合计** | | **132** | **659** |

### §2-2 完备性反查（非定性依据·仅证「无遗漏」）

为防「同形而实为 D 族条目」之漏读，本棒另作**反向完备性扫描**：对 659 之每一处，取其**所在整行**，检验该行**是否含哈希标记**（`SHA-1`／`SHA-12`／`SHA-256`／`MD5`／`hash`／`hex`／`指纹`／`[:12]` 等）或**件路径形态**。

| 检验 | 结果 |
|---|---:|
| 逐处总数 | **659** |
| 该行含哈希标记或件路径者 | **552** |
| 该行**二者皆无**者（＝须人工逐条判读之候选） | **107** |
| 107 条候选之逐条判读结果 | **107／107 皆为哈希锚**，⛔ **0 例**为 D 族条目 |

> 📌 107 条候选之集中形态：**①** 以件之 SHA-12 作**锚件代称**（如「沿 `D8D5E4D2154F` §3 逐字承接」，与其并列者 `0FD7A26FC339`／`AFA5EB53D216`／`246CE35C4DDC`／`8C5F83C3C4CF` 同为同族 SHA-12）；**②** 「不覆盖既有件（… r1 result `D245AE4CE385` …）」之**不可覆盖守卫**；**③** JSON 之 `"ADDENDUM_D3B"`／`"teacher_paths"`／`"sha12"` **指纹字段**。

> 📌 **决定性佐证（抽验·实测）**：`D8D5E4D2154F`（52 处·全为 `F12`）所锚之件虽已不在盘，惟 `_upload_plan_2026_10_12.json`／`_r2_build_manifest_2026_10_12.json` 之 `"sha12": "D8D5E4D2154F…"` ＋ `"sha256_full": "d8d5e4d2154f…"` **双字段在盘登记** ⇒ 其为哈希指纹，**非** D 族编号。

### §2-3 16 位之 3 项之专案判读（承源件 §2-3 之点名）

| 处 | 位点 | run | 该处上下文（逐字） | 判定 | 依据 |
|---:|---|---|---|---|---|
| 644 | `_v5_fake_verdict_session_log_2026_09_28.md:28` | `D30EDA5A1063F9AD` | 「**SHA-12**：`D30EDA5A1063`（**SHA-256 前 16 = `D30EDA5A1063F9AD`**）」 | **非 D 族（哈希指纹）** | 本棒**实测复算**：`_v3_recheck_prereg_v1_2026_09_27.md` 之 `sha1[:16].upper()` ＝ **`D30EDA5A1063F9AD`**（逐字命中） |
| 645 | `_v5_fake_verdict_session_log_2026_09_28.md:37` | `D30EDA5A1063F9AD` | 「`SHA-256[:16]` \| `88052D7DB895F135` … ｜ **SHA-1[:16]** \| **`D30EDA5A1063F9AD`**」 | **非 D 族（哈希指纹）** | 同上实测；且**该件同表并列之 SHA-256[:16] 实测值 ＝ `88052D7DB895F135`，与所载逐字吻合** |
| 646 | `_v5_fake_verdict_session_log_2026_09_28.md:37` | `D30EDA5A1063F9AD` | 「… \| **`D30EDA5A1063F9AD`** \| `D30EDA5A1063F9AD`（自标「SHA-256」） \| ✅ **逐字命中**」 | **非 D 族（哈希指纹）** | 同上 |

> ✅ **源件结论获独立证实**：补正件 §2-3 称该串「属**指纹前缀**」——**本棒实测确认为 SHA-1[:16] 前缀**，其语义判定（**非 D 族**）**成立**。
>
> 🔴 **新登记之源件缺陷（⛔ 0 回改·仅登记）**：该串于源件中被**自标为「SHA-256 前 16」**，而实测为 **SHA-1[:16]**；同表 `SHA-256[:16]` 栏所载 `88052D7DB895F135` 经本棒实测**逐字无误** ⇒ **源件之算法标签误标**，其「自标 SHA-256」字面 ⛔ **不成立**。见 §4 KD-L。

---

## §3 汇总与影响

### §3-1 659 之语义终判

| 项 | 处数 |
|---|---:|
| **真 `D` 族编号**（`^D\d{1,3}$` 之真义条目） | **a ＝ 0** |
| **非 `D` 族（同形）· 全为哈希指纹** | **b ＝ 659** |
| 合计（a ＋ b） | **659** |

> ✅ **a ＋ b ＝ 659，逐处判读无例外。**

**判读依据之三重性**（逐处适用）：

1. **该处自身原文上下文**——659 处**逐处**读取（其中 107 处所在行无显式哈希标记者，**另作逐条人工判读**，见 §2-2）；
2. **该处 run 之注册表对撞**——全仓在盘件之 SHA-256／SHA-1 前缀实测复算，**404 处**直接命中（`F256` 359 ＋ `F1` 45）；
3. **结构性不可能**——真 `D` 族条目之 token 必以**非字母数字**字符与十六进制串分隔（正则之 `(?<![A-Za-z0-9_])` 前瞻），故**结构上不可能**被 `[A-Za-z0-9_\-]+` 右延展吞入 ≥12 位十六进制 run；反之 run 内之 `D` 字面**必为**指纹之内蕴片段。

### §3-2 对 `#5` 勘正数 9,466 之影响

| 项 | 值 |
|---|---:|
| 勘正件复测原计数（`_numbering_family_count_erratum_2026_10_13.md:62`） | 10,186 |
| 污染量（`G-D*` 复合碎片） | −61 |
| hash 桶交叠（本棒判读：**659／659 皆真指纹**） | −659 |
| **修正后 #5 计数** | **9,466** |
| **本棒所需之再调量** | **0** |

> ✅ **结论：9,466 无须再调。** 本棒逐处判读证实 **659 全部为哈希指纹、0 处为真 `D` 族编号** ⇒ 该减量**每一处皆正当**，既无「误扣真条目」之过，亦无「漏扣同形」之欠。
>
> 📌 **方向性补强（本棒新增）**：既证 659 无一为真 D 族，则 **10,186 − 61 − 659 之两次减量无任何重叠之实**，补正件 §2-2 所称「减法可交换、9,466 为精确值」**获逐处语义面之独立支撑**（该件原仅以「前一字符为 `-` 者 ＝ 0」之结构征候论证，本棒以**逐处语义判读**补足其语义面）。

### §3-3 对 #2／#6 之影响

| 族 | 交叠 | 本棒判读后 |
|---|---:|---|
| #2 `^V\d{1,3}$` | **0** | 不变 |
| #6 `^N\d{1,3}$` | **0** | 不变 |

⇒ **0 影响**（`V`／`N` 非十六进制字符 ⇒ 结构上恒不满足判准之字符集条件；本棒未发现任何例外）。

### §3-4 对下游之影响

| 件 | 影响 | 处置 |
|---|---|---|
| `_numbering_family_count_corrigendum_2026_10_14.md` | KD-G 之 **659 逐件语义** 之闭合 | 🔴 **候 PI**：本棒立场「已闭·肯定」；⛔ **0 自宣告闭** |
| `_numbering_hash_bucket_criterion_design_2026_10_14.md` | KD-E 之「659 未逐件判读」之状态 | 🔴 **候 PI** |
| `_numbering_family_count_corrigendum_2026_10_14.md`／`_numbering_hash_bucket_criterion_design_2026_10_14.md` | #5 之 9,466 | ✅ **数值无须改动**（0 回改） |

---

## §4 遗留／KD（本件在册未闭）

### §4-1 KD 条目

| KD | 缺陷／限度 | 证据 | 处置 |
|---|---|---|---|
| **KD-K** | **255 处之判读依「上下文哈希列语义」而非复算**——其所指件**已不在盘**（`F12`），在盘⛔不可对撞；虽逐处读原文定其为指纹，惟**非**复算级证据 | §2 之 `F12` 255 处；§1-6 | 🟡 **在册·非阻断**：若 PI 须复算级证据，须于**归档区**（含仓外 `〔归档区〕`）复算——**本棒⛔ 未触该区**（0 读 0 写 0 列目录） |
| **KD-L** | `_v5_fake_verdict_session_log_2026_09_28.md` `:28` 将 `D30EDA5A1063F9AD` **自标为「SHA-256 前 16」**，实测为该件之 **SHA-1[:16]**（其 SHA-256[:16] ＝ `88052D7DB895F135`，与该件同表所载逐字吻合）⇒ **源件算法标签误标** | §2-3 之实测复算 | 🔴 **登记·⛔ 0 回改**；**候 PI** |
| **KD-M** | 判准**只吃大写十六进制**：小写指纹（如 `"sha256_full": "d8d5e4d2154f…"`）⛔ 不入桶。惟其大写 12 位形态**已同件登记于** `sha12` 字段 ⇒ **对 #5 计数 0 影响**；惟就**桶之完备性**（825 串面）而言为已知锐度边界 | §1-3、§2-1 | 🟢 **对 #5 无影响**；登记于册，供其他族判读时参 |
| **KD-N** | 本棒仪器 4 处缺陷／假象（E-1 口径 C 逐处表未建致 `BC_identical` 假阴；E-2 SHA-256 单算法对撞不足；E-3 摘要件重复渲染致**虚报**一处 `sha12` 字长畸形；E-4 附件面自匹配），**均已处置**；其中 **E-3 之疑点经实测否证**（830＋948 字段全为 12 字长）⇒ ⛔ **不登记为资产缺陷** | §1-7 | 🟢 **本棒自证**；**E-3 建议推广**：疑点⛔ 0 未验即登记为缺陷 |
| **KD-O** | 源件 `_v3_v4_achievements_inventory_2026_09_24.md:1911` 含**裸控制字节 BEL(0x07)**（「… 35081D39F35B, ␇ttacks/__init__.py …」，系目录清单生成之残留）；本棒逐处表第 391 处之上下文即含此字节 | §2 第 391 行 | 🟡 **登记·⛔ 0 回改**：本件以**可见转义 `\x07`** 渲染（保信息、不发裸控制字节）；源件 ⛔ 0 触碰。**另**：全仓 12 区语料实测 **327 件**含控制字节（⛔ TAB／LF），属既有语料状况，超本棒射程，仅登记 |

**KD 条数：5**（KD-K…KD-O）。**其中承自源件者：KD-G 已具逐处判读之全部证据，候 PI 闭。**

### §4-2 遗留（须 PI 项）

| # | 遗留项 | 类别 |
|---:|---|---|
| 1 | **KD-G 是否据此宣告闭合**（本棒立场：**可闭·659 全部为真指纹、0 例外**） | 🔴 **须 PI 裁**（⛔ 0 自宣告闭） |
| 2 | **#5 是否按 hash 判准重勘**（10,125 → **9,466**）——本棒证实该修正量**正当且无须再调** | 🔴 **须 PI 择**（数值面已闭，择定面未闭） |
| 3 | KD-L：`_v5_fake_verdict_session_log_2026_09_28.md` 之算法标签误标（⛔ 0 回改既有件） | 登记·候 PI |
| 4 | KD-K：255 处是否须于归档区复算（⛔ 0 触仓外） | 登记·候 PI |
| 5 | KD-O：`results/_v3_v4_achievements_inventory_2026_09_24.md:1911` 之裸 BEL（⛔ 0 回改既有件）；及全仓 327 件语料含控制字节之既有状况 | 登记·候 PI |

### §4-3 边界收束与自证

**边界**：🔴 **0 宣告①毕**、⛔ 0 宣告任何项「已闭」、⛔ 0 代 PI 释义／择定／给值、⛔ 0 径行采认本件任何结论、⛔ 0 回改／移动／重命名／删除 `9baf2ea2e9cb`／`be92eddb4034`／`26b708beb153`／`7953a89ea015`／`47f20fa27a62`／`956d19e4e670` 任何一字、⛔ 0 读 `.env`、⛔ 0 上传／0 远端写、⛔ 0 触仓外归档区（`〔归档区〕`）、⛔ 0 用他棒名头署名。

**全程只读**：本棒对既有件**0 编辑／0 追加／0 移动／0 重命名／0 删除**。唯一写入面为本件 ＋ `.tmp/` 之 6 件自产摘要件（运行时附件面，计数面已剪枝）。

**自指口径声明**：本件正文**不含**自身最终 SHA-256／bytes 之登记值（「件内内含自身最终哈希」在数学上无不动点，登记即失效）。定稿后权威 **SHA-12／bytes／BOM／CRLF／CR／TAB／CTRL／U+FFFD／non-ASCII** 以本棒回执所载为准（落盘后另行实测，⛔ 0 回改本件）。

*659 交叠逐件语义判读棒 · 2026-10-14 · deposon ①段收官链 · 承 KD-G · 署名 `evidence-auditor`*
