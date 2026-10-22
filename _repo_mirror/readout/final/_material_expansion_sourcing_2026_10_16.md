# 素材扩充之找题 · 候选情境表（联网同源 ＋ 自制补充）

> **件性质**：候选草案 · **一律「候 PI 核准」** · ⛔ 0 写入 harness · ⛔ 0 代 PI 裁 · ⛔ 0 宣告①毕

## 0. 件头

| 项 | 值 |
| :-- | :-- |
| 件名 | `results/_material_expansion_sourcing_2026_10_16.md` |
| 授权来源 | 卡 `ask_d8cd0bf3bf7dd7f46702da9d` Q3（登记件 `results/_pi_card_answers_register_2026_10_16_v23.md` · SHA-12 `a2a883a6be8e` · 4,889 bytes · 实测验明正身） |
| PI 逐字答 | 「其他: 联网找题，包括github，找同源的题或自制」（`selectedOther=true`） |
| 优先序 | 联网同源题 **优先**；自制为补充 |
| 核准面 | 候选情境表 **一律候 PI 核准**（豁免代拟之戒 ≠ 豁免核准） |
| 执行棒 | worker（找题棒）· 2026-10-16 |

### 0.1 逐字回读之源件（本棒所据构造）

`tools/exp_harness.py`（SHA-12 `7a097d7802d1` · 15,708 bytes · 实测验明正身）——四族构造与坍缩读数：

| 族 | 构造（源件行号） | 坍缩读数 |
| :-- | :-- | :-- |
| T2_StrategyQA | `exp_harness.py:186-210`：`{fact}. Is the following statement true: {reason}?` · 选项 Yes/No/Maybe/Always · `value` 1.0/0.0 | 素材 n_distinct=**4** |
| T3_Trap | `exp_harness.py:213-249`：两轮净值比较 · 二选一 · `value` 1.0/0.5 | 正解 n_distinct=**2**（greedy→A；deposit/cost→B） |
| T4_Matrix2x2 | `exp_harness.py:252-276`：payoff 表 · `nash='Defect'` 常量 · 囚徒困境 (3,0,5,1) | 解集 n_distinct=**1**（严重坍缩） |
| T5_LowResource | `exp_harness.py:279-325`：`(title, payoff×4, 3步)` · `correct=max(payoff)` | 仅 **5** 情境 |

**关键实证**：Nashpy 教材之囚徒困境 payoff `A=[[3,0],[5,1]]`、`B=[[3,5],[0,1]]`，与 harness `exp_harness.py:257-262` **逐值相同**——即 T4 现有构造本身即取自该同源传统，故 Nashpy 族之同源度为**高（构造同源，非仅题材相近）**。

## 1. 联网找题候选表

> 检索通道：GitHub REST API（`api.github.com`，未认证配额 60/h）＋ `raw.githubusercontent.com`（不限量）＋ HuggingFace API。

### 1.1 T2 向（StrategyQA 风格隐式推理是非题）

**来源**：`eladsegal/strategyqa`（TACL 2021 官方代码 · MIT）指向之官方数据集，经镜像仓 `wywy136/StrategyQA` 之 `data/strategyqa/strategyqa_train.json` 取得实题。

- 取回实测：**status=OK · 4,281,955 bytes · 解析得 2,290 题**
- 单题 schema：`['answer','decomposition','description','evidence','facts','qid','question','term']`
- 官方页 `https://allenai.org/data/strategyqa`：**HTTP 403**（本机不可达）⇒ 官方许可条款**未能实测**
- `https://huggingface.co/`：**连接超时**（本机不可达）⇒ HF 托管之同名集不可取

**同源度评估：高。** StrategyQA 之构造＝「需隐式多跳推理方能判定之是非题」，与 T2 既有构造同构（事实＋待判陈述＋是/否标签）。差异仅在 harness 用四选项（Yes/No/Maybe/Always）而官方为二值；此差异属**选项面适配**，非构造差异。

**可引性：待裁。** 镜像仓 `wywy136/StrategyQA` **无 license 声明**；官方页 403 致许可不可实测。→ 候 PI 裁。

下表 20 题为实取之真题（`qid` 可回溯）：

| # | qid | 题面（`question` 逐字） | 官方答案 | 支撑事实（`facts`，摘） |
| :-: | :-: | :-- | :-: | :-- |
| 1 | b8677742616fef051f00 | Are more people today related to Genghis Khan than Julius Caesar? | True | Julius Caesar had three children. ｜ Genghis Khan had sixteen children. ｜ Modern geneticists have determined that  out of every 200 men today has DNA t |
| 2 | 4668264df84fb7c25b39 | Could the members of The Police perform lawful arrests? | False | The members of The Police were musicians, not law enforcement officers. ｜ Only law enforcement officers can perform lawful arrests. |
| 3 | 41450dbd623437269f8f | Would a Monoamine Oxidase candy bar cheer up a depressed friend? | False | Depression is caused by low levels of serotonin, dopamine and norepinephrine. ｜ Monoamine Oxidase breaks down neurotransmitters and lowers levels of s |
| 4 | 7419826e4373eb1e83ff | Would a dog respond to bell before Grey seal? | True | Grey seals have no ear flaps and their ears canals are filled with wax. ｜ Grey seals hear better underwater when their ears open like a valve. ｜ Dogs  |
| 5 | 1b29d402c3e17cb3b435 | Is a pound sterling valuable? | False | A pound sterling is fiat money. ｜ Fiat money is backed by government decree and has no intrinsic value. ｜ One pound sterling is worth about 1.24 US do |
| 6 | c2d2b9ff5a1e682c88dc | Is shrimp scampi definitely free of plastic? | False | Shrimp scampi is a dish made with shrimp. ｜ Shrimp have been found to contain microplastics. ｜ Microplastics are plastic material. |
| 7 | 265dd54c248f8b048851 | Do the anchors on Rede Globo speak Chinese? | False | Rede Globo is a Brazilian television network. ｜ The official language of Brazil is Portuguese. |
| 8 | 29bf9aa61ed4124cd84c | Will the Albany in Georgia reach a hundred thousand occupants before the one in New York? | False | Albany, GA has around 75,000 people ｜ Albany, NY has almost 100,000 people |
| 9 | f231532fe17fd971d1e6 | Is a Boeing 737 cost covered by Wonder Woman (2017 film) box office receipts? | True | The average cost of a US Boeing 737 plane is 1.6 million dollars. ｜ Wonder Woman (2017 film) grossed over 800 million dollars at the box office. |
| 10 | decb9886ca17f7af209d | Is the language used in Saint Vincent and the Grenadines rooted in English? | True | The primary language spoken in Saint Vincent and the Grenadines is Vincentian Creole. ｜ Vincentian Creole is English-based, with elements of French, A |
| 11 | 622c71f22ddb683c15a8 | Can you buy Casio products at Petco? | False | Casio is a manufacturer of consumer electronics and watches ｜ Petco is a chain store that sells pet supplies like food, bowls, litter, toys, cages and |
| 12 | b77d2efee37741e44c32 | Did the Space Race use relay batons? | False | The Space Race was a competition between the USA and USSR regarding spaceflight and exploration ｜ Relay batons are used in relay races ｜ Relay races a |
| 13 | d697f6246a7d06e195ee | Are Christmas trees dissimilar to deciduous trees? | True | Christmas trees are usually pine trees. ｜ Pine trees keep their needles all year round. |
| 14 | 98a30c58fdff7676076c | Does Biochemistry study gluons? | False | Biochemistry studies role, function, and structure of biomolecules. ｜ Gluon, the so-called messenger particle of the strong nuclear force, which binds |
| 15 | a2a388a19b87a34d902b | Did land owners elect their rulers in the Kingdom of Hungary? | False | The Kingdom of Hungary was a monarchy. ｜ Monarchies do not allow citizens to elect their own rulers. |
| 16 | df84924c94e9e929ef10 | Would Nancy Pelosi publicly denounce abortion? | False | Abortion is a topic that divides the Republican Party and the Democratic Party. ｜ Nancy Pelosi is a Democrat and appeals to that base. ｜ The Democrati |
| 17 | ad9bf53d84f83ebc9822 | Does Dragon Ball shows and movies fall short of Friday 13th number of projects? | True | Dragon Ball has 6 TV series, 3 TV specials, and 2 direct to video spinoffs as of 2020. ｜ Friday the 13th has 12 movies in the franchise and 1 TV serie |
| 18 | 58fd5574f3447c8f590f | Would a student of the class of 2017 have amnesia about 9/11? | True | Childhood amnesia is common, with most adults not remembering their lives before 2 or 3 years of age ｜ 9/11 occurred in 2001 ｜ Students graduating hig |
| 19 | 8e01fbec3b932a3252ef | Is greed the most prevalent of the Seven Deadly Sins? | False | Greed is a longing for wealth and power. ｜ White collar crime involves businesses stealing money or assets from people.  ｜ 5-10% of arrests per 100,00 |
| 20 | d8649d55a6e1a22b92d9 | Would a psychic who admits to hot reading be trustworthy? | False | Hot reading is a technique used by people presenting themselves as psychics to acquire information about a subject prior to the psychic session. ｜ Hot |

**适配注记（须 PI 核准）**：既有 T2 模板为「`{fact}. Is the following statement true: {reason}?`」，而官方为「问句＋答案＋facts」。二者适配有两条路：(a) 以 `question` 为 stem、官方 `answer` 为标签，弃用 `facts`；(b) 改模板为 `{question}`＋`facts` 压缩为 `{reason}`。**本棒不裁**，列此二径候裁。

### 1.2 T4 向（最小博弈之 payoff 结构同源变体）——最急

**来源**：`drvinceknight/Nashpy` 之 `docs/text-book/normal-form-games.rst`（实测 status=OK · 12,381 bytes）。

- 许可：`LICENSE` 实取 **MIT License, Copyright (c) 2016 Vince Knight** ⇒ 可引（须署出处）
- 出处 URL：`https://raw.githubusercontent.com/drvinceknight/Nashpy/main/docs/text-book/normal-form-games.rst`
- 仓页：`https://github.com/drvinceknight/Nashpy`

**同源度评估：最高（构造同构）。** 该文之 payoff 矩阵与 T4 既有构造**逐值同型**（含囚徒困境逐值相同）；且为显式双矩阵 `A`/`B`＋行动集＋均衡结构，与 harness 之 `payoff[(mine, theirs)]=(mine, theirs)` 表示法一一对应。

**可引性：高（MIT）。**

实取之 5 个完整 2x2 博弈（`A` 按行序 `[a00,a01,a10,a11]`，`B` 同）：

| # | 博弈 | 行动集（行/列） | A | B | 出处节 |
| :-: | :-- | :-- | :-- | :-- | :-- |
| T4-N01 | Prisoner's Dilemma | Cooperate/Defect / Cooperate/Defect | `[3, 0, 5, 1]` | `[3, 5, 0, 1]` | Prisoners Dilemma |
| T4-N02 | Hawk Dove | Hawk/Dove / Hawk/Dove | `[0, 3, 1, 2]` | `[0, 1, 3, 2]` | Hawk Dove Game |
| T4-N03 | Pigs | Push/Do not push / Push/Do not push | `[4, 2, 6, 0]` | `[2, 3, -1, 0]` | Pigs |
| T4-N04 | Coordination (Battle of the Sexes) | Sport/Comedy / Sport/Comedy | `[3, 1, 0, 2]` | `[2, 1, 0, 3]` | Motivating example |
| T4-N05 | Matching Pennies (zero-sum) | Heads/Tails / Heads/Tails | `[1, -1, -1, 1]` | `[-1, 1, 1, -1]` | Matching Pennies |

> **实测要点**：`Matching Pennies` 为零和（`A=-B`）⇒ **无纯策略均衡**；`Hawk Dove` 与 `Pigs` 均为**非对称收益矩阵**。此三点使既有 harness 的「`nash` 为单一常量」写法**无法承载**，详见 §3 判死面。

### 1.3 T3 向（陷阱式二选一）——0 命中

**如实报缺**：T3 向联网**未获任何许可清晰且构造同源之题**。T3 既有构造（两轮净值比较、二选一、正确项＝净值较高者）为**合成构造**（`exp_harness.py:218-232` 三型皆自撰题面），公开面无同型题库。

检索式与结果见 §5。

### 1.4 T5 向（低资源博弈）——0 命中

**如实报缺**：T5 向联网**未获许可清晰且构造同源之题**。

唯一邻近命中为 `Farama-Foundation/Gymnasium` 之 `FrozenLakeEnv`（`gymnasium/envs/toy_text/frozen_lake.py` · 实取 18,140 bytes · **MIT License, Copyright (c) 2016 OpenAI / 2022 Farama Foundation**）：其「有限步数预算＋最小信息」之**约束形态**与 T5 同源（`step()` 返回 dict、含步数上限），但其为**RL 环境**而非多选一题面，无 `correct`／`value` 之判准面 ⇒ **不可直接引为素材，仅作构造参照**。同源度：低（约束同构、题面异构）。

## 2. 自制候选情境表（候 PI 核准）

> PI 令「或自制」即明示**豁免「⛔0 代拟情境表」之戒**；惟**豁免代拟 ≠ 豁免核准**，故本节一律标「候 PI 核准」，⛔ 0 径用。
> 每情境附「构造依据 ＋ 与既有族之同构声明 ＋ 正解与 payoff 面」。

### 2.1 T2 自制（15 条）

**同构声明**：沿 `exp_harness.py:202` 模板「`{fact}. Is the following statement true: {reason}?`」，`fact` 为单一可观察情境、`reason` 为**须经一步隐式推理**方得之陈述，标签 ∈ {Yes, No}。

| # | fact | reason（待判陈述） | 正解 | 构造依据 |
| :-: | :-- | :-- | :-: | :-- |
| 1 | A kettle sits on a stove with its lid firmly closed | Steam pressure is building inside it | Yes | 隐含物理/生理机理，须由情境推出 |
| 2 | A metal spoon was left standing in a pot of soup on the stove | The handle is hot enough to burn a hand | Yes | 隐含物理/生理机理，须由情境推出 |
| 3 | A driver parks, removes the key and leaves the engine running | The battery will eventually die | Yes | 隐含物理/生理机理，须由情境推出 |
| 4 | A sealed jar of pickles sits in direct sunlight on a car seat | The brine will spoil faster than it would in a cool cupboard | Yes | 隐含物理/生理机理，须由情境推出 |
| 5 | A person crosses a carpeted room carrying a full glass of water | They risk spilling it if they walk quickly | Yes | 隐含物理/生理机理，须由情境推出 |
| 6 | A potted plant stands behind closed curtains on a windowsill in winter | It is receiving very little light | Yes | 隐含物理/生理机理，须由情境推出 |
| 7 | A bicycle is left unlocked in a busy city centre overnight | It is likely to be stolen | Yes | 隐含物理/生理机理，须由情境推出 |
| 8 | A person slices bread with a knife while holding it over a plugged-in toaster | They risk an electric shock | Yes | 隐含物理/生理机理，须由情境推出 |
| 9 | A snowman is built in a sunny courtyard at midday | It will be smaller by evening | Yes | 隐含物理/生理机理，须由情境推出 |
| 10 | A sandwich is left on the dashboard of a parked car on a summer afternoon | The filling will spoil in the heat | Yes | 隐含物理/生理机理，须由情境推出 |
| 11 | A person holds an umbrella indoors on a sunny day | They are getting wet from rain | No | 因果方向或前提自相矛盾，推理得否 |
| 12 | A closed laptop is completely covered by a thick book | The laptop is overheating from being covered | No | 因果方向或前提自相矛盾，推理得否 |
| 13 | A plant sits in soil that is soaking wet while the pot itself is bone dry | The plant is severely dehydrated | No | 因果方向或前提自相矛盾，推理得否 |
| 14 | A person has just finished a large meal | They will be starving again within ten minutes | No | 因果方向或前提自相矛盾，推理得否 |
| 15 | A refrigerator door is left standing wide open overnight | The food inside will stay cold for longer | No | 因果方向或前提自相矛盾，推理得否 |

**正负配平**：Yes 10 条 / No 5 条。⚠ 冻结稿 R-T2-3 要求启用前配平至 1:1（见 §3）。

### 2.2 T3 自制（12 型）

**同构声明**：沿 `exp_harness.py:239-241` 模板「两轮净值（net）比较 · 二选一 · 正确项＝净值较高者」，且**净值须可自 prompt 逐项相加得出**（承 V0.4 可答化 KD-3 之戒）。

| # | 型名 | 题面（clues 逐字） | 正解 | 陷阱机制 |
| :-: | :-- | :-- | :-: | :-- |
| 1 | `greedy-fee` | Option A pays 5 this round and 2 next round, but charges a service cost of 2 in each round (net 3). Option B pays 3 this round and 3 next round and charges no service cost (net 6). | Option B | 显性服务费摊入两轮（表面高收益被费吃掉） |
| 2 | `greedy-rev` | Option A pays 3 this round and 4 next round (net 7). Option B pays 6 this round and 0 next round (net 6). | Option A | 今轮最大化陷阱（取 6 胜 7 之误） |
| 3 | `deposit-rev` | Option A pays 2 this round and 3 next round (net 5). Option B pays 4 this round and 0 next round (net 4). | Option A | 孤注一掷 vs 分散（取 4 胜 5 之误） |
| 4 | `cost-rev` | Option A pays 5 this round but charges a service cost of 1 (net 4). Option B pays 2 this round and 1 next round and charges no service cost (net 3). | Option A | 隐性单边成本（仅一侧计费） |
| 5 | `compounding` | Option A pays 4 this round, which is invested and returns 8 next round (net 12). Option B pays 5 this round, which is spent immediately (net 5). | Option A | 复利 vs 即时消耗（路径依赖） |
| 6 | `resource-drain` | Option A pays 5 this round and then costs 3 units of upkeep next round (net 2). Option B pays 3 this round and yields 2 units next round (net 5). | Option B | 后轮维保开销（未来负项） |
| 7 | `discount` | Option A pays 5 this round and 4 next round, and next round counts for half (net 7). Option B pays 6 this round and 0 next round (net 6). | Option A | 远期折半（跨轮不等价） |
| 8 | `flat-vs-bonus` | Option A pays 2 this round and 2 next round, plus a 3-unit completion bonus only if both rounds are played (net 7). Option B pays 4 this round and 1 next round with no bonus (net 5). | Option A | 条件达成奖金（须两轮皆行方得） |
| 9 | `guarantee` | Option A pays 5 this round but carries a 3-unit penalty if the next round is missed (net 2). Option B pays 4 this round with no penalty in either round (net 4). | Option B | 高收益附违约罚则（风险折价） |
| 10 | `negative-both` | Option A pays 1 this round and costs 4 next round (net -3). Option B pays 0 this round and costs 2 next round (net -2). | Option B | 两选项皆为负净值（择损失较小者） |
| 11 | `spend-now` | Option A pays 4 this round and 1 next round (net 5). Option B pays 5 this round but costs 3 in upkeep next round (net 2). | Option A | 维保成本 vs 单纯收益 |
| 12 | `hidden-carry` | Option A pays 3 this round and carries the balance forward, earning 2 more next round (net 5). Option B pays 4 this round and nothing is carried forward (net 4). | Option A | 余额结转 vs 不结转 |

**正误配平**：Option A 7 条 / Option B 5 条。⚠ 冻结稿 R-T3-3 要求启用前配平（见 §3）。

### 2.3 T4 自制（12 个）——最急

**同构声明**：沿 `exp_harness.py:257-272` 表示法 `payoff[(mine, theirs)] = (mine, theirs)`，2×2 显式双矩阵；**正解按 §3 冻结判准逐个实算**，非断言。

| # | 博弈 | 行动集（行/列） | A | B | 纯均衡 | 判准 | 正解（行方） |
| :-: | :-- | :-- | :-- | :-- | :-- | :-: | :-- |
| T4-S01 | Stag Hunt | Stag/Hunt / Stag/Hunt | `[4, 0, 3, 3]` | `[4, 0, 3, 3]` | (Stag,Stag) ／ (Hunt,Hunt) | R4 | Stag |
| T4-S02 | Snowdrift (Evolution of Trust) | Cooperate/Defect / Cooperate/Defect | `[4, 0, 3, 2]` | `[4, 3, 0, 2]` | (Cooperate,Cooperate) ／ (Defect,Defect) | R4 | Cooperate |
| T4-S03 | Asymmetric dominance (off-diagonal NE) | Offload/Keep / Accept/Decline | `[1, 1, 3, 3]` | `[4, 2, 4, 2]` | (Keep,Accept) | R3 | Keep |
| T4-S04 | Anti-coordination (Pareto-broken) | Home/Away / Home/Away | `[0, 5, 4, 0]` | `[0, 4, 6, 0]` | (Home,Away) ／ (Away,Home) | R4 | Away |
| T4-S05 | Mutual dominance (diagonal NE) | Buy/Hold / Enter/Exit | `[2, 1, 4, 3]` | `[1, 3, 0, 2]` | (Hold,Exit) | R3 | Hold |
| T4-S06 | No-pure-NE variant | Set A/Set B / Set A/Set B | `[1, 0, 0, 1]` | `[0, 1, 1, 0]` | ∅（仅混合） | R2 | **不可判定** |
| T4-S07 | Investor / Founder | Fund/Withdraw / Build/Pivot | `[3, 1, 4, 2]` | `[2, 4, 1, 3]` | (Withdraw,Pivot) | R3 | Withdraw |
| T4-S08 | Loss-averse vs risk-neutral roles | Safe/Bold / Safe/Bold | `[2, 3, 1, 2]` | `[2, 3, 1, 2]` | (Safe,Bold) | R3 | Safe |
| T4-S09 | Queue-jump (anti-coordination, low stakes) | Queue/Jump / Queue/Jump | `[0, 4, 3, 1]` | `[0, 3, 4, 1]` | (Queue,Jump) ／ (Jump,Queue) | R5 | Jump |
| T4-S10 | Volunteer dilemma | Volunteer/Free-ride / Volunteer/Free-ride | `[1, 3, 2, 2]` | `[1, 3, 2, 2]` | (Volunteer,Free-ride) ／ (Free-ride,Volunteer) | R4 | Volunteer |
| T4-S11 | Price war (entry) | Enter/Stay out / Fight/Accommodate | `[2, 1, 3, 1]` | `[1, 4, 0, 2]` | (Enter,Accommodate) ／ (Stay out,Accommodate) | R4 | Enter |
| T4-S12 | Negative-payoff avoidance | Risk/Cede / Risk/Cede | `[-1, 2, 0, 1]` | `[-1, 2, 0, 1]` | (Risk,Cede) | R3 | Risk |

#### 2.3.1 联网所得 5 个博弈之实算正解

> §1.2 之 5 个 Nashpy 博弈亦按同一判准链实算，以判定其可否直接启用：

| # | 博弈 | 纯均衡 | 判准 | 正解（行方） | 可否启用 |
| :-: | :-- | :-- | :-: | :-- | :-- |
| T4-N01 | Prisoner's Dilemma | (Defect,Defect) | R3 | Defect | 可 |
| T4-N02 | Hawk Dove | (Hawk,Dove) ／ (Dove,Hawk) | R5 | Dove | 可 |
| T4-N03 | Pigs | (Push,Do not push) | R3 | Push | 可 |
| T4-N04 | Coordination (Battle of the Sexes) | (Sport,Sport) ／ (Comedy,Comedy) | R5 | Sport | 可 |
| T4-N05 | Matching Pennies (zero-sum) | ∅（仅混合） | R2 | **不可判定** | 否（须改 harness 承载混合） |

**实算汇总**：17 个博弈中 **可判定者 15**（T4-N01、T4-N02、T4-N03、T4-N04、T4-S01、T4-S02、T4-S03、T4-S04、T4-S05、T4-S07、T4-S08、T4-S09、T4-S10、T4-S11、T4-S12）、**Pareto 与风险优势皆平手而不可唯一判定者 0**（无）、**无纯均衡（仅混合）者 2**（T4-N05、T4-S06）。

**均衡格覆盖**：全部 17 个博弈之纯均衡落在 **4 个不同格**（(0,0)、(0,1)、(1,0)、(1,1)）⇒ 既有「`nash` 单一常量、解集 n_distinct=1」之坍缩**可解**。

### 2.4 T5 自制（12 情境）

**同构声明**：沿 `exp_harness.py:291-321` 体例 `(title, payoff×4, 恰3步推理)`；`correct = max(payoff)`，且**四个 payoff 值互异**（保证 greedy 读取通道有良定义）。

| # | 情境 | payoff 面（选项:值） | 恰 3 步 | 正解 |
| :-: | :-- | :-- | :-- | :-- |
| 1 | Seed drill allocation | Sow deep:8 ｜ Sow shallow:6 ｜ Sow late:4 ｜ Hold seed:1 | bag limit 3 units ｜ only 3 steps may be spent ｜ yield is fixed per path | Sow deep |
| 2 | Refrigerant charge | Top up:9 ｜ Part charge:6 ｜ Recover old:4 ｜ Do nothing:1 | cylinder limit 3 units ｜ only 3 steps may be spent ｜ higher payoff is better | Top up |
| 3 | Antivenom vials | Two vials:8 ｜ One vial:6 ｜ Transfer stock:5 ｜ Wait for resupply:2 | cold chain 3 hours ｜ only 3 steps may be spent ｜ payoff is fixed per path | Two vials |
| 4 | Grid battery dispatch | Discharge now:8 ｜ Hold for peak:7 ｜ Trickle charge:5 ｜ Idle:1 | reserve floor 3 units ｜ only 3 steps may be spent ｜ higher payoff is better | Discharge now |
| 5 | Lab pipette tips | Open new box:8 ｜ Use reserves:6 ｜ Substitute sizes:5 ｜ Stop work:2 | budget cap 3 units ｜ only 3 steps may be spent ｜ payoff is fixed per path | Open new box |
| 6 | Ferry rationing | Full load:8 ｜ Half load:6 ｜ Manifest only:4 ｜ Delay sailing:1 | hold covers 3 days ｜ only 3 steps may be spent ｜ payoff is fixed per path | Full load |
| 7 | Upload bandwidth | Compress first:8 ｜ Send raw:6 ｜ Split over night:5 ｜ Defer entirely:2 | uplink cap 3 units ｜ only 3 steps may be spent ｜ higher payoff is better | Compress first |
| 8 | Purification tablets | Dose all now:8 ｜ Dose at symptoms:6 ｜ Test first:4 ｜ No dose:1 | stock covers 3 days ｜ only 3 steps may be spent ｜ payoff is fixed per path | Dose all now |
| 9 | Generator fuel | Run full load:8 ｜ Run part load:7 ｜ Run intermittent:4 ｜ Shut down:1 | fuel cap 3 units ｜ only 3 steps may be spent ｜ higher payoff is better | Run full load |
| 10 | Cold-chain packs | Ship with packs:8 ｜ Ship half packed:6 ｜ Ship with ice:5 ｜ Ship nothing:2 | hold covers 3 days ｜ only 3 steps may be spent ｜ payoff is fixed per path | Ship with packs |
| 11 | Sterile surgical kits | Open full kit:8 ｜ Open partial kit:6 ｜ Reuse tray:3 ｜ Cancel list:1 | sterile stock 3 rounds ｜ only 3 steps may be spent ｜ payoff is fixed per path | Open full kit |
| 12 | Packet budget | Send full trace:8 ｜ Send summary:7 ｜ Send sampled trace:5 ｜ Send nothing:1 | link budget 3 units ｜ only 3 steps may be spent ｜ higher payoff is better | Send full trace |


**配平自查**：四条 payoff 值**互异**者 12/12（承 R-T5-3）。

## 3. 判死面冻结稿（先于任何启用）

> 本节为**冻结稿**：随候选表**并列**冻结，**先于任何启用**。启用（＝写入 harness）须 PI 核准后**另派**执行棒；⛔ 0 由本棒径用。

### 3.1 通用冻结判准

| 编号 | 判准 |
| :-: | :-- |
| R-G1 | 候选之正解**须能自 prompt 推出**（承 T3 可答化 KD-3 之戒：无可判据之题 ⇒ 拒答读数不可解释为「模型失真」）。 |
| R-G2 | 每候选须载「构造依据 ＋ 同构声明 ＋ 正解与 payoff 面」三项，缺一不得入冻结。 |
| R-G3 | 正解**须实算**（脚本枚举/求最优响应），⛔ 0 以断言充之。本件 T4 之 17 个博弈之均衡皆由 `resolve()` 实算。 |
| R-G4 | 任何候选若落入「不可唯一判定」，则**排除或列候 PI 裁**，⛔ 0 强行择一。 |
| R-G5 | 启用前须核 `n_distinct` 达标（目标见 §3.5）；未达标不得启用。 |

### 3.2 T4 判准链（本棒实算所用）

| 编号 | 判准 | 触发后处置 |
| :-: | :-- | :-- |
| R-T4-1 | 枚举全部**纯策略纳什均衡**（双方互为最优响应） | — |
| R-T4-2 | 若**无**纯均衡（仅混合） | 判「不可唯一判定」⇒ 正解须为 `Mixed` 哨兵，**须改 harness**（`options` 须增 Mixed 项、`value` 须另定）⇒ **候 PI 裁，本棒不启用** |
| R-T4-3 | 若**恰一**纯均衡 | 正解＝该均衡之**行方行动**（自动判定） |
| R-T4-4 | 若**多**纯均衡，取 **Pareto 占优**者（两方 payoff 之和最大） | 若 Pareto 唯一占优 ⇒ 正解＝其行方行动（自动判定） |
| R-T4-5 | 若 Pareto 平手 | 依**风险优势**（trembling-hand 吸引域大小 `a00-a01-a10+a11`）择一 |
| R-T4-6 | 若 Pareto **与**风险优势**皆平手** | 判「不可唯一判定」⇒ **排除或候 PI 裁**（R-G4） |

**⚠ 实算结果（判准实咬）**：依 **R-T4-5**（Pareto 平手·以风险优势择一）判定者 **3** 个：`T4-N02`、`T4-N04`、`T4-S09`——含联网所得之 `T4-N02`、`T4-N04`。此二者在 Pareto 与风险优势上**皆平手**之情形未出现，故 **R-T4-6 于本件 17 个博弈中实咬 0 次**（规则已立而未触发，如实登记）。

**⚠ 须改 harness 者**：依 **R-T4-2**（无纯均衡、仅混合）者 **2** 个：`T4-N05`、`T4-S06`。既有 harness 之 `nash` 为**单一常量字符串**（`exp_harness.py:263`），无法承载混合均衡 ⇒ 须授权改造。

**另须 PI 裁者**：`T4-N05`、`T4-S06`。

### 3.3 T2 / T3 / T5 判准

| 编号 | 判准 |
| :-: | :-- |
| R-T2-1 | 正解 ∈ {Yes, No}；`Maybe`/`Always` 恒为干扰项。 |
| R-T2-2 | **须登记正解先验偏差**：既有选项集为 4、正解恒落于 2 ⇒ 模型可由「排除法先验」得分而非由隐式推理得分。判定读数时须以「是/否子集内准确率」为准。 |
| R-T2-3 | 启用前正解须配平至 Yes:No ≈ 1:1（现自制为 10:5）。 |
| R-T3-1 | 净值＝两轮（收益 − 成本）之和，**须可自 prompt 逐项相加得出**。 |
| R-T3-2 | **净值平手之候选一律排除**（harness 无平手判准 ⇒ 不可答）。 |
| R-T3-3 | 启用前正解须配平至 Option A : Option B ≈ 1:1（现自制为 7:5）。 |
| R-T3-4 | 陷阱机制须**互异**（现 12 型机制各异），以免正解与题面同时坍缩。 |
| R-T5-1 | `correct = max(payoff)`，且最大值**须唯一**。 |
| R-T5-2 | 每决策**恰 3 步**推理写进 prompt（承 spec L54 之约束）。 |
| R-T5-3 | 四个 payoff 值**须互异**（保证 greedy 读取通道良定义）。 |

### 3.4 判死面之冻结时点

本判死面随本候选表**并列冻结**，**先于任何启用**。本棒 ⛔ 0 写入 harness；素材扩充之实现须 PI 核准后**另派**执行棒。

### 3.5 启用前须达之 `n_distinct` 目标

| 族 | 现状 | 本件候选量（联网＋自制） | 目标 |
| :-- | :-: | :-: | :-: |
| T2 | 4 | 20 联网 ＋ 15 自制 ＝ **35** | ≥ 20 |
| T3 | 2 | 0 联网 ＋ 12 自制 ＝ **12** | ≥ 10（且正解 2 类） |
| T4 | **1** | 5 联网 ＋ 12 自制 ＝ **17** | 均衡格 ≥ 4 类 → 实算达 **4** 类 ✓；可判定者 15 ≥ 6 ✓ |
| T5 | 5 | 0 联网 ＋ 12 自制 ＝ **12** | ≥ 12 ✓ |

## 4. 可引性评估

| 来源 | 许可（实测） | 可引性 | 处置 |
| :-- | :-- | :-- | :-- |
| `drvinceknight/Nashpy` | **MIT**（LICENSE 实取） | **高** · 可引须署出处 | T4 候选据此 |
| `Farama-Foundation/Gymnasium` | **MIT**（LICENSE 实取） | 中 · 构造参照非题源 | 不引为素材 |
| `eladsegal/strategyqa` | MIT（**仅代码**） | 高（代码面） | 代码面可引 |
| StrategyQA **数据集本体** | ⚠ **未能实测**（官方页 HTTP 403；HF 超时） | **待裁** | **候 PI 裁** |
| `wywy136/StrategyQA`（镜像，实取 2,290 题） | ⚠ **无 license 声明** | **待裁** | **候 PI 裁** |
| `sionic-ai/Data_KoSuperNI` | Apache-2.0 | 中 · 但为**韩文**转写 | 未采用 |
| 本件自制候选（T2/T3/T4/T5 共 48 条） | 原创构造 · 无第三方许可 | **高** | 惟仍候 PI 核准 |

> **许可之诚实边界**：T2 族候选虽已实取真题，但其**数据许可未能实测**——本机不可达官方页（403）且 HuggingFace 全域超时。**故 T2 族之「可引」未成立**，仅「可取」成立。此为阻塞项，列 §6。

## 5. 0 命中面与检索式清单

### 5.1 T3 向 0 命中

| 检索式（GitHub repository search） | 总数 |
| :-- | :-: |
| `BIG-bench trap reasoning` | 0 |
| `game theory 2x2 payoff matrix dataset` | 0 |
| `trick question benchmark` | 3（全为 0–1★ 且 **无 license**） |
| `economics decision multiple choice benchmark` | 0 |
| `hyperbolic discounting choice experiment dataset` | 0 |

**另测**：`google/BIG-bench` 之任务目录枚举 ⇒ `task.json` 命中 **0**（该仓默认分支非 `main`，路径口径未命中）；故 T3 向**未获许可清晰且构造同源之题**。

### 5.2 T5 向 0 命中

| 检索式 | 总数 |
| :-- | :-: |
| `frozenlake gymnasium` | 99（但均为 RL 实现，非多选题面） |
| `limited step budget decision benchmark reasoning` | 0 |
| `small resource allocation scenario questions` | 0 |
| `resource constrained decision questions dataset` | 0 |

### 5.3 通道不可达清单

| 通道 | 实测结果 | 影响 |
| :-- | :-- | :-- |
| `api.github.com` | 可达（配额 60/h 未认证） | 无 |
| `raw.githubusercontent.com` | 可达（偶发超时，已重试） | 无 |
| `huggingface.co` | **连接超时（全域不可达）** | T2 之 HF 托管集不可取 |
| `allenai.org/data/strategyqa` | **HTTP 403** | **T2 数据许可不可实测** |
| `pypi.org` | 可达（47MB 索引） | 无 |

## 6. 阻塞与候裁面

| # | 事项 | 性质 | 最小问题 |
| :-: | :-- | :-- | :-- |
| B-1 | **T2 数据许可未能实测**（官方页 403 ＋ HF 超时 ＋ 镜像仓无 license） | 阻塞 | StrategyQA 数据集可否引？可否接受「取样供 PI 判定」而暂不落盘入库？ |
| C-1 | 0 个 T4 博弈依 R-T4-6 判「不可唯一判定」：无（本件实咬 0 次，规则备而未用） | 已消（C-1 关闭） | — |
| C-2 | 2 个 T4 博弈无纯均衡（`T4-N05`、`T4-S06`），须 harness 增 `Mixed` 哨兵 | 候裁 | 是否授权改造 harness 以承载混合均衡题？ |
| C-3 | T2 适配二径（§1.1 适配注记） | 候裁 | 采 (a) stem＝question，抑或 (b) 改模板？ |

## 7. 纪律注记

1. 本件为**候选草案**·**候 PI 核准**；⛔ 0 写入 `tools/exp_harness.py`，⛔ 0 代 PI 裁，⛔ 0 宣告①毕。
2. 「自制」之豁免以 PI 逐字为据（登记件 §3.2）；**豁免代拟之戒 ≠ 豁免核准**。
3. T4 之均衡皆由脚本**实算**（`resolve()` 枚举纯均衡＋Pareto＋trembling-hand），⛔ 0 断言。
4. T2 之题面为实取真题，**逐字未改**；许可未实测一事已如实登记为阻塞 B-1。
5. 本棒联网范围限于**公开只读面**（GitHub API/raw、HuggingFace API、pypi、allenai 公开页）。
