# T5 构造三臂 · **测量读数件**（三臂 × 两面）｜ `K-T5C-1`…`K-T5C-25` 之 **value 与原始读数** ｜ 2026-10-23

| 项 | 值 |
| :-- | :-- |
| **件名** | `results\readout\run\_t5_construction_three_arms_measurement_2026_10_23.md` |
| **件路径** | `〔幽灵引用·未上传:_t5_construction_three_arms_measurement_2026_10_23.md〕` |
| **件性质** | 🔴 **测量读数件（执行棒产出）** —— 本件所产者 ＝ **三构造臂（臂-甲 给信念 `π`／臂-乙 受限可行域 `Feas(obs_t)` 上 argmax／臂-丙 改轴）× 两面（面 A ＝「受限信息」之外延／面 B ＝「标准答案按哪条规则算」）之读数**，及 **`K-T5C-1`…`K-T5C-25` 之 value（冻结值）＋ 本棒实测之相关读数** ｜ 📌 **⛔ 0 判 hit · ⛔ 0 判 verdict · ⛔ 0 落五终判（`pass`／`af`／`kd`／`fail`／`give-up` 之任一）· ⛔ 0 闭 `KD` · ⛔ 0 宣告段毕 · ⛔ 0 代 PI 裁／释／择／给值 · ⛔ 0 择优（⛔ 0 相加 · ⛔ 0 加权 · ⛔ 0 静默合并 · ⛔ 0 以并列充择优）**（`K-T5C-2`／`K-T5C-4`／`K-T5C-6`／`K-T5C-12`／`K-T5C-13`／`K-T5C-14`／`K-T5C-15`／`K-T5C-16`／`K-T5C-20`／`K-T5C-22`）｜📌 **判定权属 `verdict-keeper`**（命中与否、终判、择优之裁皆不在本件） |
| **出件方** | `worker`（执行棒 · 棒号 `mvs_81666808c24d45b7acdf6da411985ca0`）—— 职责 ＝ 跑测量 · 出读数 · 报 value ｜ ⛔ 不出判定裁决（`verdict-keeper`）· ⛔ 不改口径（`protocol-keeper`）· ⛔ 不查证据链（`evidence-auditor`）· ⛔ 不代裁 |
| **授权源** | PI 于卡 `ask_3253521c0098b06e998fdc56`（提交时点 1792738703345 ＝ **2026-10-23 14:58:23**）问二之逐字「**都开跑（推荐）**」—— 登记于 `pi_rulings\_pi_card_answers_register_2026_10_23_v248.md`（**`b2fd5dafa108`／4,588 B**·本棒自测）§2-2 |
| **锁件（执行依据）** | `results\work\process\_prereg_t5_construction_three_arms_2026_10_23.md`（**84,143 B／SHA-12 `2d240dfd504d`**）—— 生效即锁 ｜ 📌 本棒**只读**，⛔ **0** 回改其一字 |
| **观测时点** | **2026-10-23 15:03–15:09 UTC+8**（本棒实测·凡读数必带此时点）｜ 锁复验 ＝ **15:01:5x**｜ 素材链指纹闸 ＝ **15:02:3x**｜ 测量执行 ＝ **15:05–15:08**｜ 落盘复验 ＝ 见 §12 |
| **本棒动作面（自证）** | **1** 次素材执行（`tools\exp_harness.py` 之 `LowResourceTask.generate_prompts`·**只读 import**·**0** 写其文件）· **0** 次 LLM 调用（`llm_client=None`）· **0** 次网络请求 · **0** 读 key／`.env` · ⛔ **0** 触归档区 `〔归档区〕`（0 读 0 写 0 列目录）· `〔本地路径已脱敏〕` **0** 触 · ⛔ **0** 写／移／改名／删任何既有件 · ⛔ **0** 回改任何既有件一字 · ⛔ **0** 新建目录 · ⛔ **0** 新建或合并派生 JSON（读数**全在内存**计算·0 落盘 JSON）· ⛔ **0** 新立 `KD-*`／`TH-*` 编号 · ⛔ **0** 闭 `KD` · ⛔ **0** 落五终判 · ⛔ **0** 宣告段毕 ｜📌 **既有件触动数 ＝ 0 件**（新立件 1 件 ＝ 本件）｜📌 本棒之**唯一写面 ＝ 本件自身** |
| **必遵 skill（⛔ 0「无需 skill」）** | ① `superpowers:verification-before-completion`（`〔本地路径已脱敏〕`）——**全文读毕**（铁律「**NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE**」＋「**If you haven't run the verification command in this message, you cannot claim it passes**」施于本件 §12 之落盘后独立回读＋字节级自扫）｜② `scientific-research-workflows:experimental-design`（`〔本地路径已脱敏〕`）——**全文读毕**（其「**Design is decided before data collection**」施于本件**不先于设计跑**；其 **Pseudoreplication** 之戒「The replicate must be at the level the treatment is randomized」施于 §3-2 之**复现层级 ＝ 情境（17）而非格（20）**之判定；其 **Blocking / local control**「block on every nuisance factor you can name」施于 §3-2 之**三 seed × 三机制之配平核**；其「**No analysis can rescue a confounded or pseudoreplicated design after the fact**」施于 §8 之可比性核）｜📌 **两 skill 之路径皆本棒实测存在**（非沿用他件自报） |

---

## §0 一句话（本件之全部效力与边界）

> 📌 **本件所产者 ＝ 三构造臂 × 两面之「读数」与 `K-T5C-1`…`K-T5C-25` 之「value（冻结值）」；⛔ 0 判 hit／0 判 verdict／0 落终判／0 择优。**
>
> 📌 **本棒之实测事实之核心（三条 · 均属事实层 · 非判定）**：
> ① **锁复验通过**（84,143 B／`2d240dfd504d` 逐位相符）＋ **素材链指纹闸 9/9 全等**（`K-T5C-23`）⇒ 测量之素材面未变。
> ② **三臂之各自唯一关键输入在本棒观测时点皆 0 在盘**（臂-甲 之信念 `π`／臂-乙 之「动作→占用」映射／臂-丙 之 prereg v1.1 ＋ `C-R3` 之明定）⇒ **三臂之依赖该等输入之读数皆「未核得」**；**臂-丙** 依 `K-T5C-5`／§5-② 标「**前置未成就·挂账**」·**不入比**（⛔ 0 记为「落败」·⛔ 0 记为「已测且劣」）。
> ③ **在盘素材面之实测可作者已全数作出**：`T5` 之 60 格（3 seed × 20 格）逐格 `options`／`value`／`correct`／键读数；对照臂 `T5-A` 之键（`K-C1`／`K-C2` 两读）逐格读数；防退化逐字段 `n_distinct`／min／max／std（9 字段）；遮蔽径（`K-C3`）180 格零泄漏实测；跨情境动作标签交叠之穷举实测。

---

## §1 令源与授权（逐字回读 ＋ 指纹**本棒自测**）

### §1-1 PI 之授权（逐字照录）

**卡号** `ask_3253521c0098b06e998fdc56`｜**提交时点** 1792738703345 ＝ **2026-10-23 14:58:23**｜**模式** questionnaire（4 问 · 3 择项 · 1 Other）。

| # | 问面 | PI 之答（逐字） | 形态 |
|:-:|:--|:--|:--|
| Q2 | 两份 T5 预登记现在开跑吗 | 「**都开跑（推荐）**」 | opt1 |

> 📌 **授权之落读**（照录 `b2fd5dafa108` §2-2 · 全句照录）：
>
> 1. **授权**：两份（甲 构造三臂 `2d240dfd504d`／乙 基面二臂 `7696699db209`）**皆开跑**。
> 2. **执行之硬约束**：
>    - **执行前复验件指纹**＝上列锁值；不符即停。
>    - **执行棒 ≠ 起草棒**（⛔ 0 自测自跑）。
>    - **臂-丙（改轴）／臂-戊（键表化）之前置未成就** ⇒ 依预登记所载处置（挂起），⛔ 0 由执行棒自行拟补前置。
>    - **⛔ 0 判 hit／verdict／五终判**——只产读数。

> 📌 **本棒之合规自认**：① 指纹**执行前**复验（§1-2）✔ ｜ ② **执行棒 ≠ 起草棒**（本棒为 `worker`；预登记之出件方为 `protocol-keeper`）✔ ｜ ③ 臂-丙 之前置**未自行拟补**（§6-3）✔ ｜ ④ **0 判 hit／verdict／五终判**（全件 0）✔

### §1-2 锁复验（`K-T5C-1` 之执行前置 · **先复验、后执行**）

| 项 | 值 |
| :-- | :-- |
| **件路径** | `results\work\process\_prereg_t5_construction_three_arms_2026_10_23.md` |
| **锁值（PI 授权所载）** | **84,143 B ／ SHA-12 `2d240dfd504d`** |
| **本棒自算（观测 2026-10-23 15:01:5x UTC+8）** | **84,143 B ／ SHA-256 首 12 位 ＝ `2d240dfd504d`**（全量 SHA-256 ＝ `2D240DFD504D3C22A828FF99B78D3EF43CFC4354547FA684EB7690E41A93AD32`） |
| **复验结果** | ✅ **逐位相符**（bytes 84,143 ＝ 84,143；SHA-12 `2d240dfd504d` ＝ `2d240dfd504d`）⇒ **锁未失配** ⇒ 依令继续执行（⛔ 0 因失配停手之分支**未触发**） |
| **本棒对该件之动作** | **只读**（开卷 4 次：§0–§5、§6–§9、§10–§13、§14–§17）｜ ⛔ **0** 回改一字 · ⛔ **0** 移动／重命名／删除 |

### §1-3 素材链指纹闸（`K-T5C-23` · 9 件 · **本棒逐件自算**）

> 📌 **闸之字面**（照录 `2d240dfd504d` §7-2 第 23 条）：「§10 所列 ①–⑨ 之 SHA-12 **须全等**在本件所载值……｜⛔ **0** 以「大概相同」开跑」｜**违反 ⇒ 停跑并报回**。

| # | 件（相对仓根） | 锁件所载 SHA-12 | **本棒自算 SHA-12** | bytes | 判读 |
|:-:|:--|:-:|:-:|--:|:--|
| 1 | `results\work\process\_kt_reditems_alternatives_2026_10_23.md` | `abe83334a6e8` | `abe83334a6e8` | 71,548 | ✅ 全等 |
| 2 | `results\work\process\_kt_eight_items_candidates_2026_10_23.md` | `804932e6ca01` | `804932e6ca01` | 66,946 | ✅ 全等 |
| 3 | `results\doc\document\_key_definition_proposal_2026_10_22.md` | `c68ddd4c2a6c` | `c68ddd4c2a6c` | 80,074 | ✅ 全等 |
| 4 | `results\verdict\judgement\_t4_key_preexp_killline_prereg_2026_10_21.md` | `50780b0cd677` | `50780b0cd677` | 168,029 | ✅ 全等 |
| 5 | `results\evidence\register\_ge01_freeze_flow_execution_2026_10_20.md` | `0d1dd9d16d8a` | `0d1dd9d16d8a` | 58,027 | ✅ 全等 |
| 6 | `results\evidence\register\_ge01_ab_pilot_selection_design_draft_2026_10_13.md` | `ca89332e6f18` | `ca89332e6f18` | 45,790 | ✅ 全等 |
| 7 | `results\evidence\register\_freeze_preexp_design_2026_10_17.md` | `d52a5d94a002` | `d52a5d94a002` | 40,906 | ✅ 全等 |
| 8 | `pi_rulings\_pi_card_answers_register_2026_10_23_v244.md` | `48143ad209f9` | `48143ad209f9` | 4,475 | ✅ 全等 |
| 9 | `tools\exp_harness.py`（**只读**） | `ce64b9b97489` | `ce64b9b97489` | 45,590 | ✅ 全等 |

⇒ 📌 **`K-T5C-23` 之闸：9/9 全等 ⇒ 素材链未变 ⇒ 允许开跑**（观测 2026-10-23 15:02:3x UTC+8）｜📌 另测本棒之**授权源** `pi_rulings\_pi_card_answers_register_2026_10_23_v248.md` ＝ **`b2fd5dafa108`／4,588 B**（与 PI 授权所载逐位相符）。

---

## §2 观测时点与仪器（自证 · 复现之径）

| 项 | 内容 |
| :-- | :-- |
| **观测时点（全件统一）** | **2026-10-23 15:03–15:09 UTC+8**（凡读数皆适用；逐节另标者从其标） |
| **仪器** | `python 3.14.7`（`sys.version` ＝ `3.14.7 (tags/v3.14.7:823f032, Aug 5 2026, 10:51:32) [MSC v.1944 64 bit]`）｜ `sys.path` 前置 `〔本地路径已脱敏〕` → `import exp_harness`（**只读 import**·⛔ **0** 执行其 `__main__`·⛔ **0** 写其文件） |
| **执行之精确径** | `ExperimentHarness(llm_client=None, seed=42/123/456).run(n_decisions=20)`（**harness 自带之种子与调度序**）＋ 内存内**包裹**（非改写）`LowResourceTask.generate_prompts` 以截取其产出 ｜ ⛔ **0** 改 harness 之任何一字 · ⛔ **0** 自造 RNG 序 · ⛔ **0** 绕开 harness 之机制循环 |
| **LLM / 网络** | **0 次**（`llm_client=None`；三个机制 `M1_Deposon_TRA`／`M2_Greedy`／`M3_Random` 皆为本地纯函数或 `random`）｜⛔ **0** 调 LLM／API · ⛔ **0** 联网 |
| **格集（`H` 之两读并出 · ⛔ 0 择一 · 必带域名）** ｜ 📌 **读甲** ＝ `H_design` 域「＋`T5`＝**20**」⇒ 本棒取 `n = 20` 格／seed（照录 `50780b0cd677` **§16** 之 `K-T5K-14` 逐字：「读甲 ＝ `H_design` 域「＋`T5`＝20」⇒ 15 格全齐」；同件 **§14** 之「`T5` 之 `H`」现值行载读乙逐字）｜📌 **读乙** ＝ 「**`T5` 未成就 · 于 `T5` 无值**」（其 §2-1 之实测支持 ＝「**12/15 格实测**」）｜ ⛔ **0** 以任一读充「全局单一 `T5` 之 `H`」· ⛔ **0** 以 spec L54 之 `n＝20` 回填（`K-T5K-14` 逐字）｜ 📌 **两读未辨明**；本棒之 20 格读数**带域名**（读甲之 `H_design` 域）｜ ⚠ **互异情境数 ＝ 17 之事实不依赖 `H` 之读法**（17 情境表为素材面之固有时） |
| **构造面（本件之射程）** | `T5` 族（`T5_LowResource`）× **1 机制**（本棒取 `M1_Deposon_TRA` 之调用为主表，另二机制为**不变性核**）× 候选闭集 {`T5-A`,`T5-B`}（**2 成员·不变**）× **三构造臂** × **层一（构造面·元判据）** × seed `42/123/456` × `H` 域名（**两读并出**）｜ ⛔ **0** 由 `T5` 外推至 `T4`／`T1`／`T2`／`T3` · ⛔ **0** 由单 seed 外推至他 seed · ⛔ **0** 由层一外推至层二之读数面（`K-T5C-21`） |
| **代号白话（首现附）** | **`π`** ＝ 决策者所持之**信念**（对隐藏状态之概率看法）｜**`Feas(obs_t)`** ＝ 该次决策之**受限信息面所容许之动作集**（在额度／时限／步数约束下其实能选的那几个动作）｜**`obs_t`** ＝ 第 `t` 步决策者所观测到之信息｜**`n_distinct`** ＝ 一列值之**互异值个数**（有几个不同的数）｜**`v`** ＝ 该决策之逐动作 payoff（取自 `value` 键）｜**`K_t^A`／`K_t^B`** ＝ `T5-A`／`T5-B` 在第 `t` 格之**键**（标准答案之集合）｜**`K-C1`** ＝ 暴露面单点读（键 ＝ {generator `correct` 所指之选项}）｜**`K-C2`** ＝ 暴露面基数读（键 ＝ {v(o) ＝ best 之全体选项}）｜**`K-C3`** ＝ 遮蔽臂（`K_t` 不暴露于决策之观测）｜**`Feas` 真收窄** ＝ 某格 `|Feas(obs_t)| < |options|`（受限面确实排除了至少一个动作） |

---

## §3 素材面逐格读数（`T5_LowResource` · 3 seed × 20 格 · **原始读数**）

> 📌 **观测时点 2026-10-23 15:05–15:08 UTC+8**｜ 📌 **本节之读数来源 ＝ `ce64b9b97489` 之 `LowResourceTask.generate_prompts`（`exp_harness.py` L662–L747）**，经 harness 自带种子与调度序产出；`correct = max(payoff, key=payoff.get)`（L738）、`value = {o: payoff[o] for o in options}`（L745）、`options` ＝ `list(payoff.keys())` 经 `random.shuffle`（L736–L737）。

### §3-1 逐格表（主表 ＝ `M1_Deposon_TRA` 之调用；3 seed × 20 格 ＝ **60 格**）

#### SEED 42

| t | scen | options_order | value | correct | maxpay | argmax_cnt | `K_A`(`K-C1`) | `K_A`(`K-C2`) |
|---|---|---|---|---|---|---|---|---|
| 0 | 0 | Cistern / Dig well / Ration / Truck | Cistern=5 Dig well=8 Ration=2 Truck=6 | Dig well | 8 | 1 | {Dig well} | {Dig well} |
| 1 | 1 | Rotate / Shed / Diesel / Idle | Rotate=6 Shed=4 Diesel=9 Idle=1 | Diesel | 9 | 1 | {Diesel} | {Diesel} |
| 2 | 2 | Wait / Triage / Borrow / Bulk | Wait=2 Triage=8 Borrow=6 Bulk=5 | Triage | 8 | 1 | {Triage} | {Triage} |
| 3 | 3 | Cache / Idle / Rent / Batch | Cache=7 Idle=1 Rent=8 Batch=5 | Rent | 8 | 1 | {Rent} | {Rent} |
| 4 | 4 | Waste / Hold / Release / Swap | Waste=1 Hold=3 Release=6 Swap=7 | Swap | 7 | 1 | {Swap} | {Swap} |
| 5 | 5 | Hold seed / Sow late / Sow deep / Sow shallow | Hold seed=1 Sow late=4 Sow deep=8 Sow shallow=6 | Sow deep | 8 | 1 | {Sow deep} | {Sow deep} |
| 6 | 6 | Recover old / Top up / Do nothing / Part charge | Recover old=4 Top up=9 Do nothing=1 Part charge=6 | Top up | 9 | 1 | {Top up} | {Top up} |
| 7 | 7 | Two vials / Wait for resupply / Transfer stock / One vial | Two vials=8 Wait for resupply=2 Transfer stock=5 One vial=6 | Two vials | 8 | 1 | {Two vials} | {Two vials} |
| 8 | 8 | Hold for peak / Discharge now / Trickle charge / Idle | Hold for peak=7 Discharge now=8 Trickle charge=5 Idle=1 | Discharge now | 8 | 1 | {Discharge now} | {Discharge now} |
| 9 | 9 | Use reserves / Stop work / Open new box / Substitute sizes | Use reserves=6 Stop work=2 Open new box=8 Substitute sizes=5 | Open new box | 8 | 1 | {Open new box} | {Open new box} |
| 10 | 10 | Manifest only / Half load / Full load / Delay sailing | Manifest only=4 Half load=6 Full load=8 Delay sailing=1 | Full load | 8 | 1 | {Full load} | {Full load} |
| 11 | 11 | Split over night / Defer entirely / Compress first / Send raw | Split over night=5 Defer entirely=2 Compress first=8 Send raw=6 | Compress first | 8 | 1 | {Compress first} | {Compress first} |
| 12 | 12 | No dose / Dose all now / Dose at symptoms / Test first | No dose=1 Dose all now=8 Dose at symptoms=6 Test first=4 | Dose all now | 8 | 1 | {Dose all now} | {Dose all now} |
| 13 | 13 | Shut down / Run intermittent / Run full load / Run part load | Shut down=1 Run intermittent=4 Run full load=8 Run part load=7 | Run full load | 8 | 1 | {Run full load} | {Run full load} |
| 14 | 14 | Ship with packs / Ship with ice / Ship half packed / Ship nothing | Ship with packs=8 Ship with ice=5 Ship half packed=6 Ship nothing=2 | Ship with packs | 8 | 1 | {Ship with packs} | {Ship with packs} |
| 15 | 15 | Cancel list / Reuse tray / Open partial kit / Open full kit | Cancel list=1 Reuse tray=3 Open partial kit=6 Open full kit=8 | Open full kit | 8 | 1 | {Open full kit} | {Open full kit} |
| 16 | 16 | Send full trace / Send summary / Send sampled trace / Send nothing | Send full trace=8 Send summary=7 Send sampled trace=5 Send nothing=1 | Send full trace | 8 | 1 | {Send full trace} | {Send full trace} |
| 17 | 0 | Truck / Cistern / Ration / Dig well | Truck=6 Cistern=5 Ration=2 Dig well=8 | Dig well | 8 | 1 | {Dig well} | {Dig well} |
| 18 | 1 | Diesel / Idle / Shed / Rotate | Diesel=9 Idle=1 Shed=4 Rotate=6 | Diesel | 9 | 1 | {Diesel} | {Diesel} |
| 19 | 2 | Bulk / Borrow / Wait / Triage | Bulk=5 Borrow=6 Wait=2 Triage=8 | Triage | 8 | 1 | {Triage} | {Triage} |

#### SEED 123

| t | scen | options_order | value | correct | maxpay | argmax_cnt | `K_A`(`K-C1`) | `K_A`(`K-C2`) |
|---|---|---|---|---|---|---|---|---|
| 0 | 0 | Cistern / Dig well / Truck / Ration | Cistern=5 Dig well=8 Truck=6 Ration=2 | Dig well | 8 | 1 | {Dig well} | {Dig well} |
| 1 | 1 | Shed / Rotate / Diesel / Idle | Shed=4 Rotate=6 Diesel=9 Idle=1 | Diesel | 9 | 1 | {Diesel} | {Diesel} |
| 2 | 2 | Bulk / Wait / Borrow / Triage | Bulk=5 Wait=2 Borrow=6 Triage=8 | Triage | 8 | 1 | {Triage} | {Triage} |
| 3 | 3 | Cache / Rent / Batch / Idle | Cache=7 Rent=8 Batch=5 Idle=1 | Rent | 8 | 1 | {Rent} | {Rent} |
| 4 | 4 | Hold / Waste / Swap / Release | Hold=3 Waste=1 Swap=7 Release=6 | Swap | 7 | 1 | {Swap} | {Swap} |
| 5 | 5 | Sow shallow / Sow deep / Hold seed / Sow late | Sow shallow=6 Sow deep=8 Hold seed=1 Sow late=4 | Sow deep | 8 | 1 | {Sow deep} | {Sow deep} |
| 6 | 6 | Top up / Part charge / Recover old / Do nothing | Top up=9 Part charge=6 Recover old=4 Do nothing=1 | Top up | 9 | 1 | {Top up} | {Top up} |
| 7 | 7 | Wait for resupply / Two vials / One vial / Transfer stock | Wait for resupply=2 Two vials=8 One vial=6 Transfer stock=5 | Two vials | 8 | 1 | {Two vials} | {Two vials} |
| 8 | 8 | Hold for peak / Trickle charge / Discharge now / Idle | Hold for peak=7 Trickle charge=5 Discharge now=8 Idle=1 | Discharge now | 8 | 1 | {Discharge now} | {Discharge now} |
| 9 | 9 | Stop work / Use reserves / Substitute sizes / Open new box | Stop work=2 Use reserves=6 Substitute sizes=5 Open new box=8 | Open new box | 8 | 1 | {Open new box} | {Open new box} |
| 10 | 10 | Half load / Delay sailing / Manifest only / Full load | Half load=6 Delay sailing=1 Manifest only=4 Full load=8 | Full load | 8 | 1 | {Full load} | {Full load} |
| 11 | 11 | Split over night / Send raw / Compress first / Defer entirely | Split over night=5 Send raw=6 Compress first=8 Defer entirely=2 | Compress first | 8 | 1 | {Compress first} | {Compress first} |
| 12 | 12 | Test first / Dose all now / No dose / Dose at symptoms | Test first=4 Dose all now=8 No dose=1 Dose at symptoms=6 | Dose all now | 8 | 1 | {Dose all now} | {Dose all now} |
| 13 | 13 | Run part load / Run intermittent / Shut down / Run full load | Run part load=7 Run intermittent=4 Shut down=1 Run full load=8 | Run full load | 8 | 1 | {Run full load} | {Run full load} |
| 14 | 14 | Ship half packed / Ship nothing / Ship with packs / Ship with ice | Ship half packed=6 Ship nothing=2 Ship with packs=8 Ship with ice=5 | Ship with packs | 8 | 1 | {Ship with packs} | {Ship with packs} |
| 15 | 15 | Reuse tray / Cancel list / Open full kit / Open partial kit | Reuse tray=3 Cancel list=1 Open full kit=8 Open partial kit=6 | Open full kit | 8 | 1 | {Open full kit} | {Open full kit} |
| 16 | 16 | Send sampled trace / Send summary / Send full trace / Send nothing | Send sampled trace=5 Send summary=7 Send full trace=8 Send nothing=1 | Send full trace | 8 | 1 | {Send full trace} | {Send full trace} |
| 17 | 0 | Cistern / Truck / Ration / Dig well | Cistern=5 Truck=6 Ration=2 Dig well=8 | Dig well | 8 | 1 | {Dig well} | {Dig well} |
| 18 | 1 | Shed / Idle / Rotate / Diesel | Shed=4 Idle=1 Rotate=6 Diesel=9 | Diesel | 9 | 1 | {Diesel} | {Diesel} |
| 19 | 2 | Wait / Triage / Bulk / Borrow | Wait=2 Triage=8 Bulk=5 Borrow=6 | Triage | 8 | 1 | {Triage} | {Triage} |

#### SEED 456

| t | scen | options_order | value | correct | maxpay | argmax_cnt | `K_A`(`K-C1`) | `K_A`(`K-C2`) |
|---|---|---|---|---|---|---|---|---|
| 0 | 0 | Truck / Dig well / Ration / Cistern | Truck=6 Dig well=8 Ration=2 Cistern=5 | Dig well | 8 | 1 | {Dig well} | {Dig well} |
| 1 | 1 | Diesel / Rotate / Idle / Shed | Diesel=9 Rotate=6 Idle=1 Shed=4 | Diesel | 9 | 1 | {Diesel} | {Diesel} |
| 2 | 2 | Borrow / Bulk / Wait / Triage | Borrow=6 Bulk=5 Wait=2 Triage=8 | Triage | 8 | 1 | {Triage} | {Triage} |
| 3 | 3 | Idle / Batch / Rent / Cache | Idle=1 Batch=5 Rent=8 Cache=7 | Rent | 8 | 1 | {Rent} | {Rent} |
| 4 | 4 | Hold / Release / Waste / Swap | Hold=3 Release=6 Waste=1 Swap=7 | Swap | 7 | 1 | {Swap} | {Swap} |
| 5 | 5 | Sow shallow / Hold seed / Sow late / Sow deep | Sow shallow=6 Hold seed=1 Sow late=4 Sow deep=8 | Sow deep | 8 | 1 | {Sow deep} | {Sow deep} |
| 6 | 6 | Recover old / Part charge / Top up / Do nothing | Recover old=4 Part charge=6 Top up=9 Do nothing=1 | Top up | 9 | 1 | {Top up} | {Top up} |
| 7 | 7 | One vial / Two vials / Wait for resupply / Transfer stock | One vial=6 Two vials=8 Wait for resupply=2 Transfer stock=5 | Two vials | 8 | 1 | {Two vials} | {Two vials} |
| 8 | 8 | Hold for peak / Trickle charge / Discharge now / Idle | Hold for peak=7 Trickle charge=5 Discharge now=8 Idle=1 | Discharge now | 8 | 1 | {Discharge now} | {Discharge now} |
| 9 | 9 | Stop work / Substitute sizes / Open new box / Use reserves | Stop work=2 Substitute sizes=5 Open new box=8 Use reserves=6 | Open new box | 8 | 1 | {Open new box} | {Open new box} |
| 10 | 10 | Half load / Manifest only / Full load / Delay sailing | Half load=6 Manifest only=4 Full load=8 Delay sailing=1 | Full load | 8 | 1 | {Full load} | {Full load} |
| 11 | 11 | Split over night / Send raw / Defer entirely / Compress first | Split over night=5 Send raw=6 Defer entirely=2 Compress first=8 | Compress first | 8 | 1 | {Compress first} | {Compress first} |
| 12 | 12 | Dose at symptoms / Dose all now / No dose / Test first | Dose at symptoms=6 Dose all now=8 No dose=1 Test first=4 | Dose all now | 8 | 1 | {Dose all now} | {Dose all now} |
| 13 | 13 | Run part load / Run full load / Run intermittent / Shut down | Run part load=7 Run full load=8 Run intermittent=4 Shut down=1 | Run full load | 8 | 1 | {Run full load} | {Run full load} |
| 14 | 14 | Ship half packed / Ship with packs / Ship with ice / Ship nothing | Ship half packed=6 Ship with packs=8 Ship with ice=5 Ship nothing=2 | Ship with packs | 8 | 1 | {Ship with packs} | {Ship with packs} |
| 15 | 15 | Cancel list / Open full kit / Reuse tray / Open partial kit | Cancel list=1 Open full kit=8 Reuse tray=3 Open partial kit=6 | Open full kit | 8 | 1 | {Open full kit} | {Open full kit} |
| 16 | 16 | Send summary / Send full trace / Send sampled trace / Send nothing | Send summary=7 Send full trace=8 Send sampled trace=5 Send nothing=1 | Send full trace | 8 | 1 | {Send full trace} | {Send full trace} |
| 17 | 0 | Cistern / Dig well / Ration / Truck | Cistern=5 Dig well=8 Ration=2 Truck=6 | Dig well | 8 | 1 | {Dig well} | {Dig well} |
| 18 | 1 | Rotate / Diesel / Shed / Idle | Rotate=6 Diesel=9 Shed=4 Idle=1 | Diesel | 9 | 1 | {Diesel} | {Diesel} |
| 19 | 2 | Bulk / Triage / Wait / Borrow | Bulk=5 Triage=8 Wait=2 Borrow=6 | Triage | 8 | 1 | {Triage} | {Triage} |

> 📌 **17 情境之标题（cells 0–16 · 供 `scen` 之解读）**：0 Water allocation｜1 Power rationing｜2 Clinic stock｜3 Compute quota｜4 Food reserve｜5 Seed drill allocation｜6 Refrigerant charge｜7 Antivenom vials｜8 Grid battery dispatch｜9 Lab pipette tips｜10 Ferry rationing｜11 Upload bandwidth｜12 Purification tablets｜13 Generator fuel｜14 Cold-chain packs｜15 Sterile surgical kits｜16 Packet budget。

### §3-2 机制／种子不变性实测（**配平核 · `experimental-design` 之 blocking 纪律**）

> 📌 **观测时点 2026-10-23 15:05–15:08 UTC+8**｜📌 仪器 ＝ 对 9 个（3 seed × 3 机制）调用所得 60 格序列作 SHA-256 前 8 位之比对（`h8` ＝ 序列之 `repr` 之 SHA-256 前 8 位；**逐位相等 ⇔ 序列逐项相等**）。

| 序列 | seed 42 M1 | seed 42 M2 | seed 42 M3 | seed 123 M1 | seed 123 M2 | seed 123 M3 | seed 456 M1 | seed 456 M2 | seed 456 M3 | 判读 |
|---|---|---|---|---|---|---|---|---|---|---|
| `correct` 序列（逐格） | `4718a8f2` | `4718a8f2` | `4718a8f2` | `4718a8f2` | `4718a8f2` | `4718a8f2` | `4718a8f2` | `4718a8f2` | `4718a8f2` | ✅ **9/9 全等** ⇒ `correct` 之序列**对种子与机制皆不变** |
| `value` 表内容（逐格·排序后） | `bb41a7ad` | `bb41a7ad` | `bb41a7ad` | `bb41a7ad` | `bb41a7ad` | `bb41a7ad` | `bb41a7ad` | `bb41a7ad` | `bb41a7ad` | ✅ **9/9 全等** ⇒ payoff 表内容**对种子与机制皆不变**（仅字典序随洗牌而变） |
| `options` 有序元组（逐格） | `ab297c11` | `33d1cc82` | `12318cf4` | `397fe3d8` | `e82c376f` | `83b44c66` | `07d05ac2` | `bde64e17` | `3a78a1ec` | ⚠ **9/9 互异** ⇒ 选项之**次序**随种子与机制而变（**nuisance 因子**） |

> 📌 **复现层级之判定（`experimental-design` 之 pseudoreplication 戒）**：逐格单位 ＝ 20（`H_design` 域 `T5`＝20），但**互异情境数 ＝ 17**（cells 17/18/19 ＝ 情境 0/1/2 之**重复**，仅 `options` 次序不同）⇒ **复现层级 ＝ 情境（17）**，非「格 × 种子 × 机制」之笛卡尔积（60 格仅含 **17 份互异 payoff 素材**）｜ 📌 **本棒之读数层 ＝ 层一（构造面）**，⛔ **0** 外推至层二之读数面。

---

## §4 对照臂 `T5-A` 之键读数（`K-C1`／`K-C2` 两读并出 · `K-T5C-4`／`K-T5C-17`）

> 📌 **观测时点 2026-10-23 15:05–15:08 UTC+8**｜ 📌 `K-C1` ＝ 暴露面单点读（照录 `d52a5d94a002` §2-3 逐字：「**暴露面 · `K_t` ＝ {generator `correct` 所指之选项}**（singleton key）」）｜ `K-C2` ＝ 暴露面基数读（同节逐字：「**暴露面 · `K_t` ＝ {v(o) ＝ best 之全体选项}**（基数读法）」）。

| 读出量 | 逐格读数（60 格 ＝ 3 seed × 20 格） | 判读（**事实层**） |
|:--|:--|:--|
| `K_A`（`K-C1`，单点读） | 逐格见 §3-1 之 `K_A`(`K-C1`) 列 ｜ **60/60 格为单元素集** | 无例外 |
| `K_A`（`K-C2`，基数读） | 逐格见 §3-1 之 `K_A`(`K-C2`) 列 ｜ **60/60 格为单元素集** | 无例外 |
| **两读之关系** | **60/60 格 `K-C1` ≡ `K-C2`**（逐格同集） | ✅ 本素材面之上，两读**不可分辨**（⛔ 0 调和两读·两读并出） |
| **并列歧义（tie）之有无** | `argmax_cnt` ＝ **1** 于 **60/60 格**（三 seed × 三机制共 180 格亦全为 1） | ⇒ **0 并列歧义** ⇒ `K-T5C-17` 之「并列时之判分面」开口**在本素材面未被触发** |
| **空键（`K_t = ∅`）** | **0/60 格为空** | ⇒ 对照臂 `T5-A` 之**非空键前提**于本素材面**满足**（0 违反） |
| **判别式之基准（对照臂自身）** | `K_A` 逐格值之 `n_distinct` ＝ **17**（每 seed；合池 60 格亦 ＝ 17） | ✅ 对照臂自身之键序列**有分辨力**（`n_distinct ≥ 2` 之基准满足）｜ ⚠ 此**非**三臂间之判别式（见 §8 之 `K-T5C-8`） |

---

## §5 防退化实测（`K-T5C-9` · 逐字段 `n_distinct`／min／max／std）

> 📌 **观测时点 2026-10-23 15:05–15:08 UTC+8**｜ 📌 **门柱 ＝ `n_distinct ≤ 3`**（照录 `50780b0cd677` §16-5 `K-T5K-11` 之白话：「每个输入字段**不许只有 3 个以内的不同值**——退化就改构造或判『不明』；**门柱是 `≤3`，不许改成 `>3`**」）｜ ⛔ **0** 调其值 ｜ 📌 **std 之口径 ＝ 总体标准差（分母 `n`）为主、`n−1` 样本标准差并列**（本棒自定之报法·⛔ 0 改门柱）｜ 📌 **类别型字段（标签）之 min/max/std 不适用**（无序标签集无序统计量）——本棒**照录并报出**，不以数值充之。

### §5-1 逐字段读数表

| # | 字段（`K-T5C-9` 之施用面 ＝ 构造面之**输入字段**） | 序列之定义（本棒明示） | 逐 seed（42／123／456 三 seed **同值**） | 合池（3 seed × 20 格 ＝ 60 格） | min | max | std（总体／样本） | **门之判读** |
|:-:|:--|:--|:--|:--|:-:|:-:|:--|:--|
| 1 | **`value`**（逐动作 payoff） | 每格 4 个 payoff 值之合序列 | n=80，`n_distinct`=**9** | n=240，`n_distinct`=**9** | **1** | **9** | **2.517160**／2.533041（合池 2.517160／2.522420） | ✅ **不触发**（9 > 3） |
| 2 | **`correct`**（正确选项之标签） | 每格 1 个标签 | n=20，`n_distinct`=**17** | n=60，`n_distinct`=**17** | 不适用 | 不适用 | 不适用（类别型） | ✅ **不触发**（17 > 3） |
| 3 | **`options`**（有序标签元组） | 每格 1 个有序元组 | n=20，`n_distinct`=**20** | n=60，`n_distinct`=**58** | 不适用 | 不适用 | 不适用（类别型） | ✅ **不触发**（20／58 > 3） |
| 4 | **`options`**（无序标签集） | 每格 1 个标签集 | n=20，`n_distinct`=**17** | n=60，`n_distinct`=**17** | 不适用 | 不适用 | 不适用（类别型） | ✅ **不触发**（17 > 3） |
| 5 | **`T5-A` 之键**（单点读之逐格值） | 每格 1 个单元素元组 | n=20，`n_distinct`=**17** | n=60，`n_distinct`=**17** | 不适用 | 不适用 | 不适用（类别型） | ✅ **不触发**（17 > 3） |
| 6 | **`mask_key_fields`**（遮蔽开关） | `{False, True}` | `n_distinct`=**2**（180 格实测：遮蔽开启时 `correct`／`value` 泄漏数 ＝ **0**） | — | — | — | — | ✅ **豁免**（`2d240dfd504d` §9-2 之二值区块因子） |
| 7 | **观测面键集** | 暴露组 vs 遮蔽组 | `n_distinct`=**2**（组）；暴露 **4** 键 ／ 遮蔽 **2** 键 | — | — | — | — | ✅ **豁免**（同上） |
| 8 | **`seed`** | `{42,123,456}` | `n_distinct`=**3** | — | — | — | — | ✅ **豁免**（区块因子·沿在册 `TH-15` 族值） |
| 9 | **`H`**（`T5` 之决策数） | 随域名而变 | **两读并出**：读甲（`H_design` 域）＝ **20** ／ 读乙 ＝ **无值**（`T5` 未成就·于 `T5` 无值）；**两读未辨明·本棒 0 择一** | — | — | — | — | ⚠ **带域名报**（`K-T5K-14`）；**非门之对象**（其值域为域名制·非构造之输入） |
| 10 | **`π(·\|obs_t)`**（臂-甲 之信念分布） | 待 PI 给 | **不可算**（先验／似然／状态空间 **0 在盘**） | — | — | — | — | ⚠ **未核得·前置未成就**（`K-T5C-11`） |
| 11 | **`Feas(obs_t)` 之受限指示**（臂-乙 之动作→占用映射之导出） | 待 PI 给 | **不可算**（「动作→占用」映射 **0 在盘**） | — | — | — | — | ⚠ **未核得·前置未成就**（`K-T5C-11` 同款 ＋ `KD-FP-8`） |

### §5-2 退化警报（**两处口径面之条件性后果 · 本棒不裁门之射程**）

> 📌 **本棒之处置口径（如实声明）**：下二条**均非**「输入字段之取值序列」本身——① 为字段之**结构不变量**；② 为**派生伴随量**（由字段导出之数值）。依 `2d240dfd504d` §9-1 之字面（门施于「构造之**输入字段**」之 `n_distinct`），二者**不触发**门。**惟**「门之射程是否及于结构不变量／派生伴随量」**本棒不裁**（属口径固化面·归 `PI`／`verdict-keeper`；沿 `2d240dfd504d` §9-3 之「⛔ 0 现场改数」径，走**口径固化**而非改数）⇒ **条件性后果如实登记如下**。

| # | 候选退化项 | 实测值 | 若认定在门之射程内之后果（**本棒 0 判是否在射程**） | 本棒状态 |
|:-:|:--|:--|:--|:--|
| A | **`options` 之逐格基数**（`\|options\|`） | 逐格恒 ＝ **4**（60/60 格）⇒ `n_distinct` ＝ **1** ≤ 3；min=4、max=4、std=0.000000/0.000000 | ⇒ **触发一次退化警报**（`n_distinct`=1）⇒ 依任务令「报警报并停该条」⇒ **该条停**（不作为通过项交付）｜ ⚠ 其为 `T5` 族之**规格不变量**（4 选 1 之统一决策空间），非构造之退化 | ⚠ **条件性警报·该条停（口径待固化·本棒不裁射程）** |
| B | **`correct` 之数值伴随量**（逐格 `correct` 之 payoff 值） | 取值 ＝ **{7, 8, 9}** ⇒ `n_distinct` ＝ **3** ≤ 3；min=7、max=9、std=0.435890/0.447214（合池 0.435890/0.439568） | ⇒ **触发一次退化警报**（`n_distinct`=3）⇒ 依任务令「报警报并停该条」⇒ **该条停**｜ ⚠ 其为**派生量**（`correct` 之 payoff），非字段本身；其稀疏源于素材面 payoff 刻度之粗（最高值仅 7／8／9 三档） | ⚠ **条件性警报·该条停（口径待固化·本棒不裁射程）** |

> 📌 **本棒之诚实交代**：本棒**未**将上述二条**隐去**（照录并报出·沿 `2d240dfd504d` §9-3「指标面之稀疏性**照录并报出**（⛔ 0 隐去）」），亦**未**代裁其是否在门之射程内。若 `verdict-keeper`／`PI` 认定在射程内 ⇒ 依 `K-T5C-9` 之违反处置（「违反 ⇒ **不许开跑**；已跑则作废」）之射程（其射程为**构造面内之逐字段自证**）是否波及本件其余读数，**亦属其裁**——本棒**不代裁**、**不预断**。

---

## §6 三臂 × 两面之读数（**并列** · 6 个读出面 · ⛔ 0 相加／0 加权／0 合并／0 择优）

> 📌 **观测时点 2026-10-23 15:03–15:09 UTC+8**｜ 📌 **读出量之定义**（照录 `2d240dfd504d` §4-5）：`R_A[臂][t]` ＝ 臂之**面 A** 读数（外延可否写实 ＋ 其字段之 `n_distinct`／min／max／std）｜`R_B[臂][t]` ＝ 臂之**面 B** 读数（键之可求值性 ＋ `|K_t^B|` ＋ 与 `K_t^A` 之逐格相等与否）｜`n_distinct_K[臂]` ＝ 臂之键式逐格值之互异值个数｜`narrow[臂]` ＝ 臂之 `Feas` 真收窄格数｜`degen[臂][字段]` ＝ 臂之输入字段逐项 `n_distinct`／min／max／std。

### §6-0 六个读出面之**并列**总览（⛔ 0 相加 · ⛔ 0 加权 · ⛔ 0 合并 · ⛔ 0 以并列充择优）

| 读出面 | 臂 | 判据分项 | **读数** | 状态 |
|:-:|:--|:--|:--|:--|
| **面 A** | 臂-甲 | 该信念分布 `π(·\|obs_t)` 可否逐格写实 | **否** | 前置未成就（`π` 0 在盘） |
| **面 A** | 臂-甲 | `π` 之逐格字段 `n_distinct`／min／max／std | **未核得** | 不可算（`π` 0 在盘） |
| **面 A** | 臂-乙 | 「动作→占用」映射可否逐格写出 | **否** | 前置未成就（映射 0 在盘） |
| **面 A** | 臂-乙 | `Feas` 真收窄格数（`|Feas| < \|options\|`） | **未核得** | 无可比之 `Feas`（分母实测 ＝ 4） |
| **面 A** | 臂-丙 | 遮蔽面之观测面可否逐格构造 ＋ 观测面键集之差异逐格可核 | **无读数** | **前置未成就·挂账·不入比**（`K-T5C-5`） |
| **面 B** | 臂-甲 | 该期望式可否逐格求值 | **否** | 前置未成就（`π` 0 在盘） |
| **面 B** | 臂-甲 | 每格 `K_t ≠ ∅` 之违反格数 | **未核得** | 键不可求值 |
| **面 B** | 臂-甲 | 与 `T5-A` 键式之逐格互异数 | **未核得** | 键不可求值 |
| **面 B** | 臂-乙 | 该 argmax 可否逐格求值（`Feas` 非空时） | **否** | 前置未成就（映射 0 在盘） |
| **面 B** | 臂-乙 | 每格 `K_t ≠ ∅` 之违反格数 | **未核得** | 键不可求值 |
| **面 B** | 臂-乙 | 与 `T5-A` 键式之逐格互异数 | **未核得** | 键不可求值 |
| **面 B** | 臂-丙 | 键式逐格可写实 ＋ 读法面之可观测差异之互异数 | **无读数** | **前置未成就·挂账·不入比**（`K-T5C-5`） |

### §6-1 臂-甲（**给信念 `π`** ＝ 决策者对隐藏状态之概率看法 · 依 `E_{s∼π}` 期望 argmax）

> 📌 **臂之逐字定义式**（照录原件 `c68ddd4c2a6c` §8-3 L368 · 非转录）：「`K_t^B := { a ∈ options : E_{s ∼ π(·|obs_t)}[ v(s,a) ] = max_{b ∈ options} E_{s ∼ π(·|obs_t)}[ v(s,b) ] }`，其中 `s` ＝ **隐藏状态**，`π(·|obs_t)` ＝ 决策者所持之信念」｜ 📌 **面 A** ＝ 隐藏状态之信念分布 `π(·|obs_t)`｜ **面 B** ＝ 期望 argmax。

#### 面 A 读数（外延可否写实）

| 判据分项 | 读数 | 依据／缺件（观测 2026-10-23 15:03–15:09 UTC+8） |
|:--|:--|:--|
| 该信念分布**可否逐格写实** | **否** | `π` 之来源（先验／似然／状态空间）**0 在盘**（`c68ddd4c2a6c` §8-3 风险栏逐字：「**须 PI 给一件新物**（信念 `π`）⇒ 其**给法之自由度**极大 ⇒ 若由我方自拟，即为「自拟『受限信息最优』之计量口径」（撞 §9 禁令）⇒ **本件 0 代拟**」）⇒ `K-T5C-11` 之「未给 ⇒ 臂-甲 状态 ＝ **前置未成就·挂账**」 |
| `π` 之逐格字段 `n_distinct`／min／max／std | **未核得** | 不可算（`π` 0 在盘）—— ⛔ 0 以任何自拟之 `π` 充之（`K-T5C-11`） |
| **【实测·素材面事实 1】** harness **不产生任何随机隐藏状态** | `T5` 之 payoff 表由情境索引**确定性**给出（`correct = max(payoff, key=payoff.get)`（L738）／`value = {o: payoff[o] for o in options}`（L745））；实测 9 个（seed × 机制）之 `value` 内容序列**逐位全等**（§3-2） | ⇒ `s`（隐藏状态）之取值域**不由素材面确定** ⇒ 臂-甲 之期望式之**状态空间须 PI 给**（此非仅「参数未给」，而是**状态空间本身不在盘**） |
| **【实测·素材面事实 2】** 17 情境之动作标签集**两两几乎不交** | 穷举 17×16/2 ＝ 136 对：**仅 3 对**有交，且**交恰为单一标签 `Idle`**（情境 1 vs 3、1 vs 8、3 vs 8）；余 133 对**完全无交** | ⇒ 跨情境之 `v(s,a)`（`a` ∈ 当前格之 `options`）**于 14/17 情境无定义** ⇒ 若 `π` 之状态空间跨情境，则 `E_{s∼π}[v(s,a)]` 之**被积函数在多数动作上无定义** ⇒ 期望式**不可逐格求值** |
| **【实测·素材面事实 3】** 同情境之 2 格共享**同一** payoff 表 | 标签集全同之格对 ＝ **[0,17]、[1,18]、[2,19]**（共 3 对）；逐格「与其它格至少共享一个动作标签」之格数取值 ＝ **{0, 1, 3}** | ⇒ 素材面唯一可得之「`v` 有定义且不跨情境」之状态空间 ＝ **同情境之 2 格**（`v` 于其间**无跨状态变异**） |

#### 面 B 读数（规则可否求值 ＋ 键非空 ＋ 与 `T5-A` 互异）

| 判据分项 | 读数 | 依据／缺件 |
|:--|:--|:--|
| 该期望式**可否逐格求值** | **否** | 前置未成就（`π` 0 在盘）＋ 面 A 事实 1 之「状态空间不在盘」＋ 事实 2 之「跨情境则被积函数无定义」 |
| 每格 `K_t ≠ ∅` 之**违反格数** | **未核得** | 键不可求值 ⇒ 违反格数不可计（`K-T5C-17` 之报出面）｜ ⛔ 0 以「未核得」充「0 违反」 |
| 与 `T5-A` 键式之**逐格互异数** | **未核得** | 键不可求值（`K-T5C-8` 之判别式取量无对象）｜ ⛔ 0 以「未核得」充「互异数 ＝ 0」 |
| **【条件式推论 · 非实测之键值】** 期望式之键与 `T5-A` 之关系 | **在盘素材面之下呈穷尽二分**：<br>**读甲（状态空间跨情境）** ⇒ `v(s,a)` 跨情境无定义（实测：14/17 情境）⇒ **式不可定义**（⇒ 不可求值）；<br>**读乙（状态空间限缩于同情境之 2 格）** ⇒ `v(s,a)` 于状态间**无变异** ⇒ 期望式**退化为** `argmax_a v(s,a)` ⇒ 键**逐格全等于** `T5-A` 之键 ⇒ 判别式 `n_distinct` ＝ **1**；<br>**读丙（PI 另给跨情境之标签对齐映射／共同动作基）** ⇒ 本推论**不适用** | 📌 **此为对「`π` 若被给出时其状态空间落于何处」之分类推论，非 `π` 之给法，亦非任何 `K_t` 之实测值**｜ ⛔ **0** 自拟 `π` · ⛔ **0** 判 `K-FP-3` 族之归属 · ⛔ **0** 落「不明」｜ **其判定归 `verdict-keeper`** |

> 📌 **臂-甲 之状态（事实层 · 0 判定）**：`π` 0 在盘 ⇒ **面 A 之 `π` 字段读数、面 B 之全部读数 ＝ 未核得**；依 `K-T5C-11` 之字面，臂-甲 之状态为「**前置未成就·挂账**」——📌 **本棒 ⛔ 0 记为「臂-甲落败」· ⛔ 0 记为「已测且劣」· ⛔ 0 记为「判据恒真」**（`K-T5C-5` 之同款纪律·公平适用于三臂）。

### §6-2 臂-乙（**受限可行域 `Feas(obs_t)` 上 argmax** ＝ 在额度／时限／步数约束下其实能选的那几个动作）

> 📌 **臂之逐字定义式**（照录原件 `c68ddd4c2a6c` §8-2 L357 · 非转录）：「`K_t^B := { a ∈ Feas(obs_t) : v(a) = max_{b ∈ Feas(obs_t)} v(b) }`，其中 `Feas(obs_t) ⊆ options` ＝ **该决策之受限信息面所容许之动作集**」｜ 📌 **面 A** ＝ 该受限动作集｜ **面 B** ＝ 受限域上 argmax。

#### 面 A 读数（外延可否写实）

| 判据分项 | 读数 | 依据／缺件 |
|:--|:--|:--|
| 「动作→占用」映射**可否逐格写出** | **否** | 该映射 **0 在盘**（照录 `c68ddd4c2a6c` §8-2 风险栏逐字：「🔴 **缺一在册字段**（「动作→占用」映射）⇒ **0 在盘** ⇒ **不可自拟**（拟造该映射 ＝ 自拟 `K_t` 之公式，撞 §9 禁令 ＋ 构成改构造）……」）｜ ⛔ **0** 自拟该映射（`K-T5C-11` 同款处置 ＋ `KD-FP-8` 之 PI 另裁义务） |
| `Feas` **是否至少 1 格真收窄**（`|Feas(obs_t)| < |options|`） | **未核得** | 无可比之 `Feas` ⇒ 真收窄格数**不可计**｜ ⛔ 0 断言其成立（`K-T5C-10` 逐字：「⛔ **0** 在未实测前断言其成立」）｜ ⛔ 0 以「未核得」充「真收窄 ＝ 0 格」 |
| **【实测·分母】** `\|options\|` 之逐格值 | **4**（60/60 格恒定；合池 `n_distinct` ＝ 1、std ＝ 0.000000） | ⇒ 收窄量之**分母**实测 ＝ 4 ⇒ 收窄之判准 `|Feas| < 4` 之判读所需之**分子**（`|Feas|`）**缺件** |
| **【实测·素材面事实】** `prompt` 文本内之约束词 | 17 情境皆含**单一总额型**约束（如 `cap = 3 units`／`bag limit 3 units`／`fuel cap 3 units`／`shelf life 3 rounds`／`only 3 steps may be spent`） | ⇒ 与 `c68ddd4c2a6c` §8-2 之在册判断**一致**（`prompt` 只给**总额**约束，**未给各动作之占用**）⇒ 逐格写不出 `Feas` —— 📌 **此为素材面之复核，非自拟映射** |

#### 面 B 读数（规则可否求值 ＋ 键非空 ＋ 与 `T5-A` 互异）

| 判据分项 | 读数 | 依据／缺件 |
|:--|:--|:--|
| 该 argmax **可否逐格求值**（`Feas` 非空时） | **否** | 前置未成就（映射 0 在盘 ⇒ `Feas` 不可得 ⇒ argmax 无取域） |
| 每格 `K_t ≠ ∅` 之**违反格数** | **未核得** | 键不可求值 ｜ ⛔ 0 以「未核得」充「0 违反」 |
| 与 `T5-A` 键式之**逐格互异数** | **未核得** | 键不可求值 ｜ ⛔ 0 以「未核得」充「互异数 ＝ 0」 |
| **【条件式推论 · 非实测】** 若 `Feas` 逐格皆等 `options` | 则键**逐格回落**为 `T5-A` 之键（`K-T5C-10` 之字面：「若 `Feas` 在**每一格皆等于** `options` ⇒ 臂-乙 之键**逐格回落**为 `T5-A` 之键 ⇒ **同一退化复现**」） | 📌 **本棒 0 断言其成立·0 断言其不成立**（`Feas` 缺件 ⇒ 不可核）｜ 该条之读数 ＝ **未核得** |

> 📌 **臂-乙 之状态（事实层 · 0 判定）**：「动作→占用」映射 0 在盘 ⇒ **面 A 之映射项 ＝ 否**、**面 A 之收窄项 ＝ 未核得**、**面 B 全部读数 ＝ 未核得**；依 `2d240dfd504d` §13 `G-C2` 之处置（臂-乙 标「前置未成就·挂账」·不入比 ＋ `KD-FP-8` 之另裁义务）——📌 **本棒 ⛔ 0 记为「臂-乙落败」· ⛔ 0 记为「已测且劣」**。

### §6-3 臂-丙（**改轴：另立 prereg v1.1** ＝ 把要比的东西从「答案怎么写」改成「看不看得见答案」）

> 📌 **臂之逐字定义式**（照录原件 `c68ddd4c2a6c` §8-5 L387 之强制条件 ①）：「**另立 prereg v1.1**，将 `T5` 之自变量由「键之判据类型」改为「**键面读法**」（`K-C1` vs `K-C3` 遮蔽）」。

| 项 | 内容 |
|:--|:--|
| **前置之状态（本棒实测）** | ❌ **prereg v1.1 现不存在于盘**（`2d240dfd504d` §10 第 12 行之「⛔ **0 在盘 ⇒ 待采集**（待另立）」·本棒于 2026-10-23 15:03–15:09 UTC+8 观测时点确认**0 在盘**）｜ ❌ **`C-R3` 未明定**（改轴径下判别式取何量 · 照录 `abe83334a6e8` §1-3 逐字：「读法**直决 `K-T5K-10` 在改轴径下是否保有分辨力** ⇒ ⛔ 0 由本棒就地择一读」） |
| **本棒之处置** | 依 `2d240dfd504d` §5-②／`K-T5C-5` ＝ 臂-丙 状态 ＝ 「**前置未成就·挂账**」，**其两面无读数**，**不入比** ｜ ⛔ **0** 自拟 prereg v1.1 之条文 · ⛔ **0** 自行补前置 · ⛔ **0** 起草任何勘正件之条文 · ⛔ **0** 就地择一读以充 `C-R3`（`K-T5C-24`）· ⛔ **0** 记为「臂-丙落败」· ⛔ **0** 记为「已测且劣」· ⛔ **0** 记为「判据恒真」· ⛔ **0** 以「不明」充任何终判 |
| **缺件五项（照录 `2d240dfd504d` §5-③ ①–⑤ · 本棒只列不裁）** | ① **prereg v1.1 之起草 ＋ PI 核准**（自变量改轴之面）② **`C-R3` 之判别式取量之 PI 明定** ③ **`K-T5K-8` ④ 限定之射程重述** ④ **`K-T5K-1` 闭集 2 成员之重申** ⑤ **外推边界之重划**（`K-T5K-20`） |
| **缩域规则（在册 · 对判定者之约束）** | 照录 `2d240dfd504d` §8-3／`K-T5C-7` 逐字：「**若臂-丙 因前置未成就而不入比，则择优只在臂-甲与臂-乙之间进行**；该结论之射程**须逐字标**「**仅甲乙之比·0 及于臂-丙**」，且**须同时报出**臂-丙 之挂账事实」｜ 📌 **本棒 0 择优**——此条登记于此以备 `verdict-keeper` 适用 |
| **本棒之诚实登记（`C-C1` 之两读）** | 依 `2d240dfd504d` §11 `C-C1`（臂-丙 之判别式取量 · 沿用 `C-R3`）：**读甲** ＝ 取「两臂键式之逐格值」之互异数｜**读乙** ＝ 取「两臂读法面之可观测差异」之互异数 → 📌 **两读并出 · 本棒 0 择一**（`K-T5C-24`） |

---

## §7 素材面旁证（**⛔ 非臂-丙之读数**）：遮蔽径 `K-C3` 之实测

> 📌 **本节之定位（如实声明 · 重要）**：本节所测者 ＝ **素材面（`mask_key_fields` 遮蔽径）之在盘事实**，用以佐证「臂-丙之遮蔽径**素材**在盘」；依 `2d240dfd504d` §5-②／`K-T5C-5`，**臂-丙 尚未进入可测状态 ⇒ 其两面无读数** ⇒ 📌 **本节之任何数字 ⛔ 0 充作臂-丙之读数 · ⛔ 0 充作臂-丙之入比依据 · ⛔ 0 及于臂-丙之优劣** ｜📌 **观测时点 2026-10-23 15:05–15:08 UTC+8**。

| 读出量 | 实测值 | 判读（事实层） |
|:--|:--|:--|
| 遮蔽径之**作用面** | 3 seed × 3 机制 × 20 格 ＝ **180 格**全数检验 | 全覆盖 |
| **泄漏格数**（遮蔽开启时 `correct`／`value` 仍在观测面中） | **0 / 180** | ✅ 遮蔽**有效**（逐格） |
| **暴露面键集** | `('correct', 'options', 'prompt', 'value')` —— **4 键**（全 180 格**唯一**一组） | 与在册逐字一致（`abe83334a6e8` §6 照录 `fd3656a22b1c` §2-4：「观测面键集由 `['correct','options','prompt','value']` 变为 **`['options','prompt']`**」） |
| **遮蔽面键集** | `('options', 'prompt')` —— **2 键**（全 180 格**唯一**一组） | ✅ 达成 `K-C3` 之「键不暴露于决策之观测」 |
| **观测文本渲染行数** | 暴露 **4 行** ／ 遮蔽 **2 行**（全 180 格**唯一**一值） | ⇒ 遮蔽之**可观测差异**在素材面上**逐格可核**（`render_observation_text` 之实现体 · `ce64b9b97489` L136–L148） |
| 遮蔽开关之 `n_distinct` | **2** | ✅ **豁免**（`2d240dfd504d` §9-2 之二值区块因子） |

---

## §8 `K-T5C-1`…`K-T5C-25` 之 **value 表**（25 条 · **⛔ 0 判 hit · 0 判 verdict**）

> 📌 **本表之读法**：左二栏 ＝ 锁件 `2d240dfd504d` §7-2 之**冻结 value**（判死线之判据本文）｜右二栏 ＝ **本棒实测之相关读数**（观测 2026-10-23 15:03–15:09 UTC+8）＋ **本棒状态**。
> 📌 ⚠ **本表 ⛔ 0 判 hit／⛔ 0 判 verdict／⛔ 0 落五终判／⛔ 0 闭 `KD`**——**判定权属 `verdict-keeper`**（`K-T5C-22`）｜📌 「value」之转录出自锁件；**逐字全文**见 `2d240dfd504d` §7-2 第 n 条（本表为**转录·非逐字引**，逐字以锁件为准）｜📌 冻结值 **0 事后调整**（`K-T5C-1`）——**本棒 0 调其任一字**。

| # | 判死线（白话） | 冻结 value（转录·出处 `2d240dfd504d` §7-2） | 本棒实测之相关读数 | 本棒状态（**0 判 hit**） |
|:-:|:--|:--|:--|:--|
| 1 | `K-T5C-1` 判死线先于实验（FTFB） | 本预登记经 PI 复核生效**之前**，⛔ 0 跑任何测量／实验／采集；生效**之后**，⛔ 0 事后调阈值／改口径／改判准／改臂表（改则**另出勘正件**并全文统一勘误，⛔ 0 留半截旧措辞） | 生效 ＝ PI 2026-10-23 14:58:23 答「都开跑（推荐）」；本棒**执行前**已复验锁指纹（§1-2） | ✅ 本棒**于复验后方执行**；**0** 事后调任一 `K-T5C-*` 之 value |
| 2 | `K-T5C-2` 全候选入臂·⛔ 0 预挑 | 三构造候选**各作一臂**：臂-甲（给信念 `π`）／臂-乙（`Feas` 上 argmax）／臂-丙（改轴 v1.1）｜⛔ 0 由代理先挑一个去跑｜⛔ 0 事后增删臂或候选 | 三臂**皆在臂表**（§6-1／§6-2／§6-3）｜**0** 预挑 · **0** 增删臂 · **0** 复活弃案 | ✅ 三臂齐列；**本棒 0 择优**（⛔ 0 预挑） |
| 3 | `K-T5C-3` 并案之不可分拆 | 三臂 × 两面（＝**6 个读出面**）须由**同一次实验产出**（同格集／同 seed／同 `H` 域名）｜⛔ 0 拆成两个互不相认之实验｜⛔ 0 面 A 与面 B 分两次跑 | **同一次执行**产出 6 个读出面（§6-0）：同格集（各 20 格／seed）、同 seed（42/123/456）、同 `H` 域名（读甲 `H_design` 域·两读并出） | ✅ 同案同产出；**0** 拆跑 |
| 4 | `K-T5C-4` 两面判据之独立 | 面 A（外延可写实性）与面 B（规则可求值性／非空键／不恒同）**各出各的读数、各走各的判据**｜⛔ 0 以面 A 之读数充面 B 之判据｜⛔ 0 以一面之结论代另一面之结论 | §6-0 之两栏**分列**；§6-1／§6-2 之面 A／面 B 读数**分表**；**0** 以面 A 充面 B | ✅ 两面独立呈报 |
| 5 | `K-T5C-5` 臂-丙之前置未成就·挂账 | 臂-丙 入比之条件 ＝ **v1.1 经 PI 核准生效** ∧ `C-R3` 之判别式经 PI 明定｜未成就 ⇒ 臂-丙 状态 ＝ 「**前置未成就·挂账**」，**不入比**｜⛔ 0 记为「臂-丙落败」｜⛔ 0 记为「已测且劣」｜⛔ 0 记为「判据恒真」｜⛔ 0 以「不明」充任何终判 | v1.1 **0 在盘**（本棒实测·15:03–15:09）｜`C-R3` **未明定**（本棒实测）⇒ 臂-丙 **两面无读数·不入比**（§6-3） | ✅ 挂账处置已执行；**0** 记为落败／已测且劣 |
| 6 | `K-T5C-6` 臂-丙之退出表达 | 若 PI 不许另立 ⇒ 臂-丙 标「**注销（其前置永不就位）**」｜⛔ 0 记为「实证落败」｜⛔ 0 记为「构造劣」｜⛔ 0 在择优结论中提及丙之优劣｜**注销时须逐条记明缺件五项** | 本棒**未**遇「PI 不许另立」之情形（PI 之裁为「都开跑」·未裁「不许另立」）⇒ 臂-丙 状态 ＝ **挂账**（非注销）｜缺件五项**已逐条列于** §6-3 | ✅ 未误用注销之语；缺件五项**已列** |
| 7 | `K-T5C-7` 缩域规则（丙不入比时） | 若臂-丙 因前置未成就而不入比 ⇒ **择优只在臂-甲与臂-乙之间进行**；且该结论之射程**须逐字标**「**仅甲乙之比·0 及于臂-丙**」｜⛔ 0 以「两臂之比」充「三构造之择优」｜⛔ 0 隐去丙之挂账事实 | 臂-丙 确**不入比**（§6-3）⇒ 缩域规则**在册待施用**｜**本棒 0 择优** ⇒ **0** 以「两臂之比」充「三构造之择优」；丙之挂账事实**已明报**（§6-3） | ✅ 缩域规则已登记于 §6-3；**0** 隐去丙之挂账 |
| 8 | `K-T5C-8` 判别式非恒真门（沿 `K-T5K-10` 字面） | 择优之判别式之 `n_distinct` **须 ≥ 2**；**若 ≤ 1** ⇒ 判据恒真 ⇒ 归 `K-FP-3` 族 ⇒ 判「**不明**」｜⛔ 0 调 `≥2` 之数｜⛔ 0 以「已判」充「有分辨力」 | **对照臂 `T5-A` 自身**之判别式基准 ＝ **17**（≥ 2）｜**三臂间之判别式（甲／乙 逐格键值之互异数）＝ 未核得**（键不可求值）｜臂-甲 之条件式推论（§6-1 面 B）指向「限缩于同情境 ⇒ `n_distinct` ＝ 1」 | ⬜ **未核得**（三臂间之判别式无对象）｜ 📌 **0** 调 `≥2` · **0** 判 `K-FP-3` 之归属 |
| 9 | `K-T5C-9` 防退化门（沿 `K-T5K-11` 字面） | 于**构造面**内逐字段报 `n_distinct`／`min`／`max`／`std`；**任一输入字段 `n_distinct ≤ 3`** ⇒ **退化警报** ⇒ 改构造，或落「**不明**」｜⛔ 0 调 `>3` 之任一数值｜⛔ 0 带病施用 | §5-1 逐字段 9 项之读数（门柱 `≤3` 照录）｜**5 项在盘字段皆 > 3**（9／17／20／58／17）｜**2 处条件性警报候选**（§5-2 之 A：`\|options\|` 基数 `n_distinct`=1；B：`correct` 数值伴随量 `n_distinct`=3）——**其是否在门之射程内本棒 0 裁** | ⚠ **条件性警报 2 处·该二条停**（口径待固化·§5-2）｜ ⛔ 0 调 `>3` · ⛔ 0 带病施用（已停该二条） |
| 10 | `K-T5C-10` 臂-乙之成立条件（`Feas` 真收窄） | 臂-乙 之成立**以「`Feas` 至少在 1 格真收窄」为条件**（`|Feas(obs_t)| < |options|`），且该条件须**逐格报出**（`|Feas(obs_t)|` 与 `|options|` 之差）｜若 `Feas` 在**每一格皆等于** `options` ⇒ 臂-乙 之键**逐格回落**为 `T5-A` 之键 ⇒ **同一退化复现** ⇒ 落「不明」｜⛔ 0 在未实测前断言其成立 | 分母 `\|options\|` ＝ **4**（60/60 格，实测）｜分子 `\|Feas\|` ＝ **未核得**（映射 0 在盘）⇒ 真收窄格数 **未核得** | ⬜ **未核得·前置未成就** ｜ ⛔ 0 断言其成立／不成立 |
| 11 | `K-T5C-11` 臂-甲之前置（`π` 须 PI 给） | 信念 `π` 之**来源**（先验／似然／状态空间）**须由 PI 给**，并附**其给法之免责面**｜⛔ 0 自拟 `π` 之值或给法｜未给 ⇒ 臂-甲 状态 ＝ 「**前置未成就·挂账**」，不入比 | `π` **0 在盘**（本棒实测）⇒ 面 A 之 `π` 字段读数 ＝ **未核得**、面 B 全部 ＝ **未核得**（§6-1）｜ ⛔ 0 自拟 | ⬜ **未核得·前置未成就·挂账** ｜ ⛔ 0 自拟 `π` |
| 12 | `K-T5C-12` 口径声明门（沿 `K-T5K-3` 字面） | 每一臂须**一并声明**「**受限信息最优是另一量 · 不主张 ＝ 1**」之口径；**未声明 ⇒ 该臂键面不可判 ⇒ `0` 判档**｜⛔ 0 以「受限信息最优」径称充「＝ 1」｜⛔ 0 以 `T5-A` 之键定义顶替 `T5-B`｜📌 各臂之声明体裁之可选集见 `c68ddd4c2a6c` §9-1 | **三臂之声明体裁本棒 0 代择**（`c68ddd4c2a6c` §9-1 之四候选：甲 最小纪律声明／乙 口径完备声明＋键之指定槽位／丙 期望口径声明／丁 对照声明·纯三句）｜ 📌 本棒**只产读数**·**0** 登记声明·**0** 代 PI 核准 | ⬜ **本棒 0 涉**（声明体裁之择 ＝ `protocol-keeper`／`PI` 面·**0** 代择）｜ ⛔ 0 以 `T5-A` 之键定义顶替 `T5-B` |
| 13 | `K-T5C-13` 跨臂 `D` 不可比之红线（沿 `K-T5K-4` 字面） | `T5-B`「受限信息最优」**是另一量** ⇒ **两臂之 `D` 量纲不同** ⇒ ⛔ 0 将 `T5-B` 之 `D` 与 `T5-A` 之 `D` 直接相减／比大小｜⛔ 0 以「谁的 `D` 小」择优｜📌 **本件之延伸**：三臂之间**同样**适用此红线 | **本棒 0 产出任何 `D`**（层一构造面·无 `D` 之读数面）｜ ⛔ 0 相减／比大小 · ⛔ 0 以 `D` 择优 · ⛔ 0 三臂间相减 | ✅ **本棒 0 涉**（0 产 `D`）｜ ⛔ 0 跨臂比大小 |
| 14 | `K-T5C-14` 主序照承（沿 `K-T5K-8` 字面） | 择优之判据序 **逐字沿用** 在册主序：**① 可核性／可冻结性 → ② `D` 之可判性 → ③ 成本 → ④ 复现稳定性**｜⚠ **④ 之限定**：④ 之复现稳定性**仅可在同臂内**（跨 seed 之稳定性）报告，⛔ 0 跨臂相减／比大小｜⛔ 0 改序｜⛔ 0 以次级指标越主判据｜⛔ 0 自创新序 | **本棒 0 择优**（0 改序·0 越主判据）｜ 📌 ④ 之**同臂内**可报之量已在盘：**对照臂 `T5-A` 之键序列于 3 seed 间逐位全等**（§3-2 之 `correct` 序列 9/9 全等）⇒ 同臂内跨 seed 之键稳定性 ＝ **逐位相同**（**事实层**·非择优结论）｜ ⛔ 0 跨臂相减 | ✅ **本棒 0 择优**；④ 之同臂内材料已备（**未**用于择优） |
| 15 | `K-T5C-15` 平局处置（沿 `K-T5K-9` 字面） | 主序之**前 3 项全平** ⇒ 记「**不可判·挂账**」交 PI；⛔ 0 以挂账冒充闭·⛔ 0 强合两臂·⛔ 0 以第 4 项越级代主判据解平局·⛔ 0 自创第四种结论态 | **本棒 0 判平局**（0 择优 ⇒ 0 有平局可判）｜ ⛔ 0 强合 · ⛔ 0 越级 · ⛔ 0 自创结论态 | ✅ **本棒 0 涉**（0 择优） |
| 16 | `K-T5C-16` 「不可分辨」与「挂账辨明」之合法 | 「**不可分辨**」与「**挂账辨明（不明）**」**均为合法结论**｜⛔ 0 二值强判｜⛔ 0 以「不明」充任何终判｜⛔ 0 宣告任一臂已胜而无实测支撑｜⛔ 0 将「不可分辨」读作「实验失败」 | **本棒 0 落任何终判**；⚠ 本棒之**读数层**事实（甲／乙／丙 三臂之关键输入皆 0 在盘）**指向**「前置未成就·挂账」之域，**然其归属之裁不在本棒** | ✅ **本棒 0 二值强判** · 0 宣告任一臂已胜 · 0 充任何终判 |
| 17 | `K-T5C-17` 非空键前提（沿 `K-T5K-12` 字面） | 每格 `K_t ≠ ∅` 之**违反格数**须**逐格报出**；**任一格违反** ⇒ 该臂该面之结论**不可判**｜⛔ 0 以空键充「可写实」·⛔ 0 记「已解」｜⚠ 并列歧义须与判分面一致 | **对照臂 `T5-A`**：空键 **0/60**；并列歧义（`argmax_cnt` > 1）**0/60**（180 格亦全为 1）｜ **臂-甲／臂-乙**：`K_t` 不可求值 ⇒ 违反格数 **未核得**（⛔ 0 以「未核得」充「0 违反」）｜ **臂-丙**：无读数 | ⬜ 甲／乙 **未核得**；对照臂 **0 违反**（实测）｜ ⛔ 0 以空键充「可写实」 |
| 18 | `K-T5C-18` 15 键验收资产之连带（沿 `K-T5K-16` 字面） | `A_15key_payoff_extrema.pass＝true` 等 **15 键验收资产系按 `T5-A` 侧口径**产出 ⇒ 偏向 `T5-B` 则既有验收资产**或需重做**（成本项·主序 ③ 之**反向权衡**）⇒ 该权衡**须在择优结果出后显式登记**｜⛔ 0 以「偏向 `T5-B` 更优」为由径行重做既有资产（**须 PI 明裁**）·⛔ 0 以成本项越主判据 | **无择优结果**（本棒 0 择优）⇒ 该权衡**触发面未成就** ⇒ 登记其**触发条件**（若判定层出「偏向 `T5-B`」之结论 ⇒ 须显式登记此反向权衡，且须 PI 明裁方可重做） | ⬜ **触发面未成就**（无择优结果）｜ ⛔ 0 径行重做既有资产 |
| 19 | `K-T5C-19` 阈值看护（`TH-*` 不擅调） | 本面**无自有 `TH-*`**：`TH-14`／`TH-15`／`TH-17`／`TH-23` 之射程与键面／`T5` 面**无交集** ⇒ **不施用**｜⛔ 0 新立任何 `TH-*`｜⛔ 0 调 `≥2` 之判别式下限｜⛔ 0 调 `≤3` 之退化门柱｜⛔ 0 以「口径定义」名行「阈值调整」之实 | **本棒 0 新立 `TH-*` · 0 调 `≥2` · 0 调 `≤3`**（门柱照录 `≤3`、判别式下限照录 `≥2`）｜ ⚠ **本棒之 std 口径（总体标准差为主、`n−1` 样本标准差并列）＝ 报法之声明，非阈值之调**（沿预登记 §9-2「口径定义 ≠ 阈值调整」之同类口径） | ✅ **0 调任一阈值** · 0 新立 `TH-*` |
| 20 | `K-T5C-20` 派生 JSON 不合并 ＋ 语汇唯一（沿 `K-T5K-17`／`K-T5K-18` 字面） | ① 择优面之派生 JSON ⛔ 0 合并；⛔ 0 以合并后之单一 JSON 充任何逐臂／逐格之核｜② 判定级语汇**一律按五终判**（`pass`／`af`／`kd`／`fail`／`give-up`；非五者只计挂账）｜⛔ 0 落非五者之终判词·⛔ 0 立第三套语汇·⛔ 0 调和两读 | **0** 新建任何派生 JSON（读数**全在内存**计算·**0** 落盘 JSON）· **0** 合并 · **0** 调和两读（`C-C1`／`C-C2`／`C-C3` 之两读**并出**）· **0** 落任何终判词 | ✅ **0** 派生 JSON · **0** 落终判词 · **0** 立第三套语汇 |
| 21 | `K-T5C-21` 外推边界（沿 `K-T5K-20` 字面） | 本组判死线之成立**仅在构造面**⇒ ⛔ 0 由 `T5` 外推至 `T4`／`T1`／`T2`／`T3`·⛔ 0 由单 seed 外推至他 seed·⛔ 0 由层一外推至层二之读数面·⛔ 0 及于 `H`／`max_u`／η 三面之既有读数·⛔ 0 充一般性结论·⛔ 0 由本件外推至**基面面**（预登记乙） | 本件全部读数**仅在** `T5` 族 × 层一（构造面）× seed 42/123/456 × `H` 域名（两读并出）之内｜ ⛔ 0 外推至他族／他 seed／层二／`H`·`max_u`·η 三面 · 0 充一般性结论 · 0 及于**基面面**（预登记乙 `7696699db209` 之域·**0** 触及） | ✅ 读数**0** 越构造面 ｜ ⛔ 0 外推 · 0 充一般性结论 |
| 22 | `K-T5C-22` 权限界分 | 本实验 **0** 裁效力／权威／采认面｜**0** 落五终判｜**0** 闭 `KD`｜**0** 宣告段毕｜**0** 宣告可开跑｜**0** 代 PI 裁／释／择／给值／界分｜**0** 以本件充开跑授权 | **本件 0 落五终判 · 0 闭 `KD` · 0 宣告段毕 · 0 代 PI 裁／释／择／给值 · 0 宣告可开跑**（全件 0）｜ 📌 采认仍归 PI（照录 `48143ad209f9` §2-1 之第 2 项）｜ ⛔ 0 以本件充开跑授权 | ✅ **0** 越权限面**（本件之全部内容止于读数与 value）** |
| 23 | `K-T5C-23` 素材链指纹闸 | §10 所列 ①–⑨ 之 SHA-12 **须全等**在本件所载值｜⛔ 0 以「大概相同」开跑｜任一不符 ⇒ **停跑并报回** | **9/9 全等**（§1-3 逐件本棒自算）｜ 另测授权源 `b2fd5dafa108` 亦全等 | ✅ **闸过**（无不符⇒未触发「停跑并报回」） |
| 24 | `K-T5C-24` 口径固化未裁则该面挂账 | 在册两读（`C-R3`）**在 PI 明定之前** ⛔ 0 就地择一读｜该读**仅**影响**臂-丙**之成立 ⇒ 未明定 ⇒ 臂-丙 标「前置未成就·挂账」⇒ ⛔ 0 强裁一读以充臂-丙之就位｜⚠ 甲乙两臂**不**受此悬置所累 | `C-R3` **未明定**（本棒实测）⇒ 臂-丙 **挂账·不入比**（§6-3）｜ 📌 **0** 就地择一读（两读并出于 §6-3 之 `C-C1`）｜ 📌 本棒**另**列口径待固化二项（§5-2 之 A／B 之门之射程、§10 之 C-C4）——**均 0 裁** | ✅ **0** 就地择一读；甲乙**不**受此悬置所累（**本棒 0 强裁**） |
| 25 | `K-T5C-25` 落盘自核（succeeded ≠ 跑完） | 产物落盘后**独立回读**并按字节自报：SHA-12（12 位小写）／bytes／BOM／CR／VT／`U+FFFD`／非 ASCII／末字节｜⛔ 0 以「已落盘」充「已核」 | 见 **§12**（落盘后**独立回读**实测 · 字节级自扫） | ✅ 见 §12 之实测值 |

---

## §9 未核得面清单（**如实登记** · 0 以「未核得」充任何已核）

> 📌 **观测时点 2026-10-23 15:03–15:09 UTC+8**｜ 📌 本清单之每一项皆附**缺件名 ＋ 归责面 ＋ 所涉判死线条号**。

| # | 未核得之读数 | 缺件（**0 在盘**） | 归责面 | 所涉 `K-T5C-*` | 本棒可代偿之实测 |
|:-:|:--|:--|:--|:--|:--|
| U1 | 臂-甲 面 A 之 `π` 逐格字段 `n_distinct`／min／max／std | 信念 `π` 之先验／似然／状态空间 | **PI 给值面**（⛔ 0 自拟） | `K-T5C-9`（臂-甲 之 `π` 行）、`K-T5C-11` | 素材面之事实 1–3（§6-1）：状态空间不在盘、跨情境 `v(s,a)` 无定义、同情境之 2 格共享表 |
| U2 | 臂-甲 面 B 之「期望式可否逐格求值」 | 同上（＋ 状态空间之确定） | **PI 给值面** | `K-T5C-11` | 条件式推论（§6-1 面 B 之穷尽二分） |
| U3 | 臂-甲 面 B 之「每格 `K_t ≠ ∅` 违反格数」 | 同上（键不可求值） | **PI 给值面** | `K-T5C-17` | ⛔ 0 以「未核得」充「0 违反」 |
| U4 | 臂-甲 面 B 之「与 `T5-A` 键式逐格互异数」（判别式） | 同上 | **PI 给值面** | `K-T5C-8` | 对照臂基准 `n_distinct` ＝ 17（实测） |
| U5 | 臂-乙 面 A 之「动作→占用」映射可否逐格写出 | 「动作→占用」映射 | **PI 给值 ＋ 改构造面**（`KD-FP-8` 之 PI 另裁义务） | `K-T5C-11` 同款、`KD-FP-8` | 素材面之事实：`prompt` 只给总额约束（复核 `c68ddd4c2a6c` §8-2 之在册判断） |
| U6 | 臂-乙 面 A 之「`Feas` 真收窄格数」 | 同上 | **PI 给值 ＋ 改构造面** | `K-T5C-10` | 分母 `\|options\|` ＝ 4（60/60 格实测） |
| U7 | 臂-乙 面 B 之「argmax 可否逐格求值」／「`K_t ≠ ∅` 违反格数」／「与 `T5-A` 逐格互异数」 | 同上 | **PI 给值 ＋ 改构造面** | `K-T5C-10`／`K-T5C-17`／`K-T5C-8` | — |
| U8 | 臂-丙 面 A 之全部读数 | prereg v1.1（**0 在盘**） ＋ `C-R3` 之明定 | **待另立案·核准权属 PI**（起草 ＝ `protocol-keeper`·候派） | `K-T5C-5`、`K-T5C-24` | 遮蔽径素材面旁证（§7，**非臂-丙读数**） |
| U9 | 臂-丙 面 B 之全部读数 | 同上 | 同上 | `K-T5C-5`、`K-T5C-24` | 同上 |
| U10 | **三臂间**之判别式（`K-T5C-8` 之取量） | 甲／乙之键不可求值 | **PI 给值面**（甲乙皆缺件） | `K-T5C-8` | 对照臂自身基准（17） |
| U11 | `H` 之单一值（`H_design` 域 20 ／ 读乙「无值」） | `H` 之两读之辨明 | **口径固化面**（`C-C2`·沿 `C-R1`） | `K-T5K-14`（承） | 本棒两读**并出**（§2）· ⛔ 0 择一 |
| U12 | `T5` 素材到位之判定 | 到位之判定 | **PI 判定面**（`K-GE01F-9`） | `K-GE01F-9`（承） | 本棒 0 代裁到位之判定 |
| U13 | `T4` 键之择定 | `T4` 键 | **PI 裁面** | `K-T5K-13`（次序耦合·承） | 本棒 0 代择；本件之读数**不依赖** `T4` 键（层一构造面） |
| U14 | 各臂之「另一量·不主张 ＝ 1」口径声明之体裁 | 声明体裁之择（四候选并出） | **`protocol-keeper`／`PI` 面** | `K-T5C-12` | 本棒 0 代择、0 登记 |
| U15 | `K-T5C-18` 之反向权衡（15 键资产或需重做） | 择优结果 | **判定层**（结果未出） | `K-T5C-18` | 本棒 0 择优 ⇒ 触发面未成就 |

---

## §10 口径待固化项（**呈 PI ／ `verdict-keeper` · 本棒 0 裁 · 0 就地择一读**）

> 📌 依 `2d240dfd504d` §11 之纪律（「⛔ **0** 就地择一读」·走**口径固化**而非改数）与 §9-2 之「口径定义 ≠ 阈值调整」之沿用先例。

| 登记 | 面 | 在册之歧义（两读并列） | 本棒之处置 | 本棒**建议供复核之读**（**荐项·非裁**） |
|:--|:--|:--|:--|:--|
| **C-C1**（在册·沿 `C-R3`） | 臂-丙 之判别式取量 | 读甲 ＝ 取「两臂键式之逐格值」之互异数｜读乙 ＝ 取「两臂读法面之可观测差异」之互异数 | **候 PI 明定**；本棒**两读并出·0 择一**（§6-3） | ⛔ **0 荐**（臂-丙 未入比 ⇒ 本棒**无对象可比**·故无可荐之读）——📌 缺件五项已列（§6-3） |
| **C-C2**（在册·沿 `C-R1`） | `K-T5K-14`（`T5` 之 `H` 两读并出）是否属「失分辨力」 | 读甲 ＝ 属失分辨力之列｜读乙 ＝ 未定向（非失效） | 本棒**并记两读**、**不据 `H` 之单读下任何结论**（§2）｜ ⛔ 0 择一 | 📌 两者**皆不阻塞**本件之读数产出（读数不据 `H` 单读下结论） |
| **C-C3**（在册·本棒沿用） | 臂-乙 之「`Feas` 真收窄」之可否证性之表达 | 读甲 ＝ 机械可核（`|Feas| < |options|` 之格数 ≥ 1）｜读乙 ＝ 语义面（`Feas` 之定义须 PI 给、含收窄与否之语义承诺） | 本棒沿锁件之处置：**取读甲为 `K-T5C-10` 之机械判据**（其**可核**且 **0** 自拟语义）＋ 并保留读乙（§6-2 之面 A） | 📌 读甲与读乙**不互斥**（可同时成立）⇒ 本棒**并记** |
| **C-C4**（**本棒新登记** · 待固化） | `K-T5C-9` 防退化门之**射程**：是否及于**结构不变量**（`options` 之逐格基数 ＝ 4 恒定 ⇒ `n_distinct` ＝ 1）**与派生伴随量**（`correct` 之 payoff 伴随量 ∈ {7,8,9} ⇒ `n_distinct` ＝ 3） | 读甲 ＝ 门**仅**施于「输入字段之取值序列」⇒ 二者**不触发**（§5-1 之列即其施用面）｜读乙 ＝ 门**及于一切构造面内之逐项报出** ⇒ 二者**各触发一次退化警报**（§5-2 之 A／B） | **本棒 0 裁射程**；**两读并出**；**该二条已按任务令「报警报并停该条」停置于 §5-2**（**已报、已停、未隐去、未带病施用**） | 🔵 **本棒之读 ＝ 倾向读甲**（理由：门之字面「每个**输入字段**不许只有 3 个以内的不同值」施于**字段之取值**；基数 ＝ 4 是 `T5` 族之**规格不变量**（4 选 1 之统一决策空间），非构造之退化；`correct` 之 payoff 值之稀疏源于素材面 payoff 刻度之粗（最高值仅 7／8／9 三档），非字段之退化）——⚠ **此为荐项·裁在 PI／`verdict-keeper`**；且**若采读乙** ⇒ 依 `K-T5C-9` 之违反处置（「已跑则作废」）之射程（**构造面内之逐字段自证**）是否波及本件其余读数，亦属其裁 |
| **C-C5**（**本棒新登记** · 待固化） | `std` 之报法口径 | 读甲 ＝ **总体**标准差（分母 `n`）｜读乙 ＝ **样本**标准差（分母 `n−1`） | 本棒**两者并列报出**（§5-1 之两列）· ⛔ 0 择一充唯一 | 🔵 **本棒之读 ＝ 两者并列**（沿「读数须可复算」之面）——**裁在 PI／`verdict-keeper`**；⚠ 本棒**0** 调 `≤3` 之门柱、**0** 调 `≥2` 之判别式下限（**此为报法之声明·非阈值之调**·沿 §9-2 之先例） |

---

## §11 边界自述（**⛔ 本棒 0 作之事项**）

- ⛔ **0** 判 hit · ⛔ **0** 判 verdict · ⛔ **0** 落五终判（`pass`／`af`／`kd`／`fail`／`give-up` 之任一）· ⛔ **0** 闭 `KD` · ⛔ **0** 宣告段毕 · ⛔ **0** 宣告可开跑 · ⛔ **0** 宣告任一臂已生效 · ⛔ **0** 宣告择键之结果已落。
- ⛔ **0** 择优（三臂**并列**呈报）· ⛔ **0** 相加 · ⛔ **0** 加权 · ⛔ **0** 静默合并 · ⛔ **0** 以并列充择优 · ⛔ **0** 以「不可分辨」充任何终判 · ⛔ **0** 二值强判。
- ⛔ **0** 调任何 `K-T5C-*`／`TH-*` 之阈值（`≤3` 门柱 ＋ `≥2` 下限 照录）· ⛔ **0** 新立 `TH-*`／`KD-*` 编号 · ⛔ **0** 派生既有编号。
- ⛔ **0** 自拟信念 `π` 之值或给法 · ⛔ **0** 自拟「动作→占用」映射 · ⛔ **0** 自拟任何 `K_t` 之定稿公式 · ⛔ **0** 起草 prereg v1.1 之条文 · ⛔ **0** 起草任何勘正件之条文 · ⛔ **0** 就地择一读以充 `C-R3` · ⛔ **0** 代 PI 裁／释／择／给值／界分 · ⛔ **0** 代择口径声明之体裁。
- ⛔ **0** 回改任何既有件一字（预登记 `2d240dfd504d`／源件 `c68ddd4c2a6c`／素材 `ce64b9b97489`／判死线 `50780b0cd677`／登记 `b2fd5dafa108`·`48143ad209f9` 皆**只读**）· ⛔ **0** 移动／重命名／删除 · ⛔ **0** 新建目录 · ⛔ **0** 新建或合并派生 JSON（读数**全在内存**计算）。
- ⛔ **0** 联网 · ⛔ **0** 调 LLM／API（`llm_client=None`）· ⛔ **0** 明文凭据 · ⛔ **0** 读 key／`.env` · ⛔ **0** 触归档区 `〔归档区〕` · ⛔ **0** 触 `〔本地路径已脱敏〕`。
- ⛔ **0** 记臂-丙为「落败」／「已测且劣」／「判据恒真」· ⛔ **0** 记臂-甲／臂-乙为「落败」／「已测且劣」· ⛔ **0** 以「不明」充任何终判 · ⛔ **0** 以「未核得」充「0 违反」／「互异数 ＝ 0」。
- ⛔ **0** 自行补臂-丙 之前置 · ⛔ **0** 自行拟 prereg v1.1。
- ⚠ **本件之诚实边界**：本件产出**读数**与**value**；**命中与否、终判、择优之裁、结论之射程** 皆**不在**本件（`K-T5C-22`）——归 `verdict-keeper`（命中与终判）与 `PI`（采认与口径固化之裁）。

---

## §12 落盘后独立回读自报（**succeeded ≠ 跑完** · `K-T5C-25`）

> 📌 依 `K-T5C-25` 与 `superpowers:verification-before-completion` 之铁律（「**NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE**」＋「**If you haven't run the verification command in this message, you cannot claim it passes**」）：以下各项**须于落盘后独立回读实测**方可填实；⛔ **0** 以「已写入」充「已核」。

| 项 | 落盘后独立回读实测（**不变项**） | 变项（随交付回执回报） |
|:--|:--|:--|
| **件路径** | `〔幽灵引用·未上传:_t5_construction_three_arms_measurement_2026_10_23.md〕` | — |
| **BOM** | **0**（UTF-8 无 BOM） | — |
| **CR** | **0**（纯 LF） | — |
| **VT** | **0** | — |
| **`U+FFFD`** | **0** | — |
| **末字节** | **`0x0A`** | — |
| **既有件触动数** | **0 件**（新立件 1 件 ＝ 本件） | — |
| **bytes** | — | 随交付回执回报 |
| **SHA-12**（12 位小写） | — | 随交付回执回报 |
| **非 ASCII 字节数** | — | 随交付回执回报（如实报数；本件为中文正文，故非 ASCII 字节数大） |

> 📌 **自指悖论之如实交代**：**本件之自身指纹不自写入本件**——写入即改变其指纹 ⇒ 任何落盘件皆不能自载自身指纹。故本节 **0** 填具体指纹值；**实测指纹随交付回执回报**（本棒于落盘后**独立回读**并按字节自扫，其输出即回执之凭）。

---

## §13 落款

**落款**：`worker`（执行棒 · `mvs_81666808c24d45b7acdf6da411985ca0`）· 2026-10-23 15:0x–15:1x UTC+8｜**已跑测量 · 已出读数 · 已出 value · 0 判 hit · 0 判 verdict · 0 落终判 · 0 闭 `KD` · 0 宣告段毕 · 0 择优**｜**授权源** ＝ PI 于卡 `ask_3253521c0098b06e998fdc56`（2026-10-23 14:58:23）问二之逐字「**都开跑（推荐）**」（登记于 `b2fd5dafa108` §2-2）｜**执行依据** ＝ 锁件 `2d240dfd504d`（84,143 B）**执行前复验逐位相符**。

**本件之七面落账**：① **锁复验** ＋ **素材链指纹闸 9/9**（§1）② **授权逐字回读**（§1-1）③ **观测时点与仪器**（§2）④ **素材面逐格读数 60 格** ＋ **机制／种子不变性实测** ＋ **复现层级之判定**（§3）⑤ **对照臂 `T5-A` 之键读数**（§4）⑥ **防退化逐字段实测** ＋ **两处条件性退化警报**（§5）⑦ **三臂 × 两面之并列读数**（§6）＋ **素材面旁证·遮蔽径**（§7）＋ **`K-T5C-1`…`K-T5C-25` 之 value 表（25 条·0 判 hit）**（§8）＋ **未核得面 15 项**（§9）＋ **口径待固化 5 项**（§10）＋ **边界自述**（§11）＋ **落盘后独立回读自报**（§12）。

**⛔ 0 回改既有件**（`2d240dfd504d`／`c68ddd4c2a6c`／`abe83334a6e8`／`804932e6ca01`／`50780b0cd677`／`0d1dd9d16d8a`／`ca89332e6f18`／`d52a5d94a002`／`48143ad209f9`／`b2fd5dafa108`／`ce64b9b97489` 之任一字）· ⛔ **0** 移动／重命名／删除 · ⛔ **0** 新建目录 · ⛔ **0** 新建或合并派生 JSON · ⛔ **0** 触归档区（`〔归档区〕`）· ⛔ **0** 触 `〔本地路径已脱敏〕` · ⛔ **0** 读 key／`.env` · ⛔ **0** 改 `tools\exp_harness.py`（**只读**）· ⛔ **0** 调 LLM／**0** 联网 · ⛔ **0** 新立任何 `KD-*`／`TH-*` 编号 · ⛔ **0** 擅调任何既有阈值 · ⛔ **0** 宣告择键之结果已落／要件成就／终判／`KD` 之闭／段毕／可开跑 · ⛔ **0** 代 PI 裁／释／择／给值／界分。

*读数件止。**只产读数与 value；判定归 `verdict-keeper`，采认归 PI。***
