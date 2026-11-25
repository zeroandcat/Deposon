# `B-O` 三列（①量纲 ②单位 ③与 `B_t`＝3 之换算）· 20 格 · 盘上取数

日期：2026-10-25｜棒：`evidence-auditor`（证据链审计官）｜面：`B-O`（动作→占用量之数值面）之 20 格三列
**范围**：**只取数**。⛔ 0 判五终判 · ⛔ 0 闭 `KD` · ⛔ 0 宣告段毕或门槛成就 · ⛔ 0 代 PI 裁 · ⛔ 0 答占用量数值／收益代价数值／正确解／最优动作／排名／统计量。
**本件＝唯一新件**；⛔ 0 回改任何既有件一字 · ⛔ 0 移动／重命名／删除 · ⛔ 0 新建目录 · ⛔ 0 跑实验 · ⛔ 0 读 `〔本地路径已脱敏〕` · ⛔ 0 调 LLM／API · 归档区仅按名与指纹认人（⛔ 0 读其正文）。

---

## §R-1 结论（先读此节）

1. **两条路径之载体皆在盘**（皆在仓内根 `〔本地路径已脱敏〕`）：
   - **P-1「逐格预算约束元数据」** ＝ `results\work\process\_t5_desensitized_pack_2026_10_24.md` 之 `§OI-1b-1`（20 格逐行，件内 L119–L138）。
   - **P-2「逐格约束条款原文」** ＝ `tools\exp_harness.py` L665–L732 之 `scenarios` 约束三句原文（逐格经 L735 `scenarios[i % len(scenarios)]` 映射）。
2. **三列之整体可得度（主口径，见本节第 4 条）**：三列齐 **5/20**；部分（①②得·③缺）**15/20**；三列全缺 **0/20**。
3. **得 ③ 之 5 格** ＝ `t_05`／`t_08`／`t_11`／`t_13`／`t_15`（单位为 `days`／`hours`）；换算系数取 NIST SP 811 Appendix B.9 之 Time 节（本棒实测抓取，2026-10-25）。
4. ⚠ **口径之别（本棒取数口径，非裁定）**：③ 之「换算」按 K3.1 之 `conversion_reference` 口径（＝**至公共参考单位之可核系数**，`T5_BO_meta_paths_K31B_2026_10_25.md` L44 之 `B_reference = 3 × k`）计；若采委托件 §2 之例式（「1 日 ＝ 1 个 `B` 单位」，`_commission_bo_three_columns_narrow_v1_2026_10_24.md` L37）之宽读（③＝本格单位与 `B_t` 之**所在**单位之关系，恒 1:1），则三列齐为 **20/20**。两读之别归 PI／verdict-keeper，本棒 ⛔ 0 代裁。
5. **0 触达**：本棒对既有件之写操作 ＝ **0**（§R-7 自证）。

---

## §R-2 两路径之载体（含实测指纹）

### §R-2-1 P-1 之载体（逐格预算约束元数据）

| 项 | 值 |
|:--|:--|
| 件 | `results\work\process\_t5_desensitized_pack_2026_10_24.md` |
| 字节／on-disk SHA-12 | **31,937**／**`90a5e34e1ae6`**（本棒 `Get-FileHash` 实测） |
| 段 | `§OI-1b-1`（标题于 L112；逐格表头 L117；20 行于 **L119–L138**） |
| 切片（§OI-1b，L112–L160） | **4,706** B／**`63eb88aaf9fd`** —— 本棒**自测复现**，与 `_commission_t5_inputs_external_EN_round2_draft_2026_10_24.md`（64,125 B／`e2cd66b1b543`）L124 之 manifest 登记值**逐位相符** |
| 同一性第二载体 | `results\work\process\_t5_desensitized_pack_v2_noD_2026_10_24.md`（**30,961** B／**`4af3a674a6be`**）；其 `§OI-1b` 切片（L120–L168）＝ **4,706** B／**`63eb88aaf9fd`** —— 与前者**逐位同值**（双载体互证） |
| 元数据之构成 | `cell_id`｜情境 id｜**预算类型**｜**预算值**｜**预算单位**｜**约束短语**｜附加子句｜步数上限｜语义注记码；来源与版本见该件 L115（短语之由来）、L67（素材载体与锚证） |
| 分布互证 | 该件 L148 之「预算单位之分布：units 12／days 4／rounds 3／hours 1」与本棒 20 行逐行转写之计数**逐位相符**（此为**转写完整性自检**，非新出之统计量） |

### §R-2-2 P-2 之载体（逐格约束条款原文）

| 项 | 值 |
|:--|:--|
| 件 | `tools\exp_harness.py` |
| 字节／on-disk SHA-12 | **45,590**／**`ce64b9b97489`**（本棒实测；与派工单所载**逐位相符**，兼作同一性正控） |
| 原文位置 | `scenarios` 17 条于 **L665–L732**，每条三元组之第 3 项为约束三句：第 1 句＝**总额型约束**（本面所需）、第 2 句恒 `only 3 steps may be spent`、第 3 句＝payoff 语义注记（**非**本面所需，本件不引其内容） |
| 格→情境映射 | **L735** `title, payoff, steps = scenarios[i % len(scenarios)]`；`n=20` 于 **L662**（20 格 ⇒ 3 对格共用同一情境） |
| 约束类别互证 | `results\work\process\_t5_inputs_construction_plan_2026_10_23.md`（85,336 B／`3982b82f095b`）**L126** 独立复核：第 1 项恒为总额型、第 2 项恒步限、第 3 项为语义注记，**无任一「各动作占用」字段** |
| 与 P-1 之关系 | §OI-1b-1 之「约束短语」列 ＝ 本件第 1 句之**转录**；本棒逐条比对 **20/20 相符**（`t_01`/`t_18` 原文作 `cap = 3 units, no extra data`，包内拆为短语＋附加子句；余 19 格逐字相符） |

### §R-2-3 `B_t`＝3 之角色与出处（`B_t_role`）

| 项 | 值 |
|:--|:--|
| 陈述 | 「以 `prompt` 所给**总额** `B_t = 3`（`cap = 3 units` 一类）导出 `Feas(obs_t) = { a : o(a) ≤ B_t }`」 |
| 出处 A | `results\work\process\_t5_inputs_three_track_2026_10_23_redacted_v1_2026_10_24.md`（53,734 B／`ee07d58a1ee2`）**L280** |
| 出处 B（未脱敏本） | `results\work\process\_t5_inputs_three_track_2026_10_23.md`（52,945 B／`7709625c6779`）**L279** |
| 判读 | `B_t` ＝ **该格 `prompt` 之总额型约束所给之预算总量**，非占用量、非收益、非其他量；20/20 格皆为总额型（§OI-1b-2 L150） |

### §R-2-4 单位语义（①量纲之依据）与换算标准（③之依据）

| 单位 | 盘上定义（逐字回读） | 出处（件·行·指纹） |
|:--|:--|:--|
| `unit` | 「one indivisible quantum of the resource named by that cell. Its physical identity and conversion to any external measurement are not supplied. It is not commensurable with a quantum from another scenario.」 | `T5_input_B_occupancy_K31B_2026_10_24.md`（7,703 B／`42e03b658e8a`）**L17** |
| `hour` | 「exactly 3600 seconds when used as a duration」＋NIST SP811 B.9 之引用 | 同上 **L18** |
| `day` | 「exactly 86400 seconds when used as a duration; this is not a claim about a calendar date or a sidereal day」 | 同上 **L19** |
| `round` | 「one complete decision cycle in the scenario. The cycle's start/end and any duration conversion require the scenario definition; neither is supplied, so no seconds conversion is made.」 | 同上 **L20** |
| `step` | 「one atomic action selection in the model. This is a model-count unit, not a physical-time unit. The separate step limit is not merged with resource occupancy.」 | 同上 **L21** |

**换算标准（本棒唯一之联网用途）**：NIST, *Guide to the SI*, Appendix B.9, **Time** 节 —— `day (d)` → second (s) ＝ **8.64 E+04**；`hour (h)` → second (s) ＝ **3.6 E+03**（同节另列 `day (sidereal)` 8.616 409 E+04、`hour (sidereal)` 3.590 170 E+03 —— 本棒**取非恒星者**，与 `L19` 之释义一致）。来源：https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b9 （本棒抓取日 2026-10-25；页面自载「Created February 1, 2016, Updated August 18, 2025」）。
⛔ 本棒**未**用联网补「格→预算量」这条对应链；对应链 100% 来自 §R-2-1／§R-2-2 之盘上件。

---

## §R-3 20 格三列表（含逐格出处）

**记号**：`UNOBTAINED` ＝ 该格该列未获可核证据；**非零、非均值、非估算、非默认值、非他案之值**。

| `cell_id` | ①量纲 | ②单位 | ③与 `B_t`＝3 之换算 | 出处（元数据行 · 原文行） |
|:--|:--|:--|:--|:--|
| `t_01` | 计数（情境资源量子／无量纲之配额） | `unit` | `UNOBTAINED` | §OI-1b-1 **L119** · `exp_harness` **L667** |
| `t_02` | 计数（情境资源量子／无量纲之配额） | `unit` | `UNOBTAINED` | §OI-1b-1 **L120** · `exp_harness` **L670** |
| `t_03` | 计数（决策轮次） | `round` | `UNOBTAINED` | §OI-1b-1 **L121** · `exp_harness` **L673** |
| `t_04` | 计数（情境资源量子／无量纲之配额） | `unit` | `UNOBTAINED` | §OI-1b-1 **L122** · `exp_harness` **L676** |
| `t_05` | **时间（持续时间）** | `day` | **得**：`k` ＝ **8.64 E+04 s/day** ⇒ `B_ref` ＝ 3 × 8.64E+04 s ＝ **2.592 E+05 s**（NIST B.9 Time 节） | §OI-1b-1 **L123** · `exp_harness` **L679** |
| `t_06` | 计数（情境资源量子／无量纲之配额） | `unit` | `UNOBTAINED` | §OI-1b-1 **L124** · `exp_harness` **L684** |
| `t_07` | 计数（情境资源量子／无量纲之配额） | `unit` | `UNOBTAINED` | §OI-1b-1 **L125** · `exp_harness` **L687** |
| `t_08` | **时间（持续时间）** | `hour` | **得**：`k` ＝ **3.6 E+03 s/hour** ⇒ `B_ref` ＝ 3 × 3.6E+03 s ＝ **1.08 E+04 s**（NIST B.9 Time 节） | §OI-1b-1 **L126** · `exp_harness` **L691** |
| `t_09` | 计数（情境资源量子／无量纲之配额） | `unit` | `UNOBTAINED` | §OI-1b-1 **L127** · `exp_harness` **L695** |
| `t_10` | 计数（情境资源量子／无量纲之配额） | `unit` | `UNOBTAINED` | §OI-1b-1 **L128** · `exp_harness` **L699** |
| `t_11` | **时间（持续时间）** | `day` | **得**：`k` ＝ **8.64 E+04 s/day** ⇒ `B_ref` ＝ 3 × 8.64E+04 s ＝ **2.592 E+05 s** | §OI-1b-1 **L129** · `exp_harness` **L703** |
| `t_12` | 计数（情境资源量子／无量纲之配额） | `unit` | `UNOBTAINED` | §OI-1b-1 **L130** · `exp_harness` **L707** |
| `t_13` | **时间（持续时间）** | `day` | **得**：`k` ＝ **8.64 E+04 s/day** ⇒ `B_ref` ＝ 3 × 8.64E+04 s ＝ **2.592 E+05 s** | §OI-1b-1 **L131** · `exp_harness` **L711** |
| `t_14` | 计数（情境资源量子／无量纲之配额） | `unit` | `UNOBTAINED` | §OI-1b-1 **L132** · `exp_harness` **L715** |
| `t_15` | **时间（持续时间）** | `day` | **得**：`k` ＝ **8.64 E+04 s/day** ⇒ `B_ref` ＝ 3 × 8.64E+04 s ＝ **2.592 E+05 s** | §OI-1b-1 **L133** · `exp_harness` **L721** |
| `t_16` | 计数（决策轮次） | `round` | `UNOBTAINED` | §OI-1b-1 **L134** · `exp_harness` **L725** |
| `t_17` | 计数（情境资源量子／无量纲之配额） | `unit` | `UNOBTAINED` | §OI-1b-1 **L135** · `exp_harness` **L729** |
| `t_18` | 计数（情境资源量子／无量纲之配额） | `unit` | `UNOBTAINED` | §OI-1b-1 **L136** · `exp_harness` **L667** |
| `t_19` | 计数（情境资源量子／无量纲之配额） | `unit` | `UNOBTAINED` | §OI-1b-1 **L137** · `exp_harness` **L670** |
| `t_20` | 计数（决策轮次） | `round` | `UNOBTAINED` | §OI-1b-1 **L138** · `exp_harness` **L673** |

**元数据表所在件**（两载体同值互证）：`results\work\process\_t5_desensitized_pack_2026_10_24.md`（31,937 B／`90a5e34e1ae6`）；`results\work\process\_t5_desensitized_pack_v2_noD_2026_10_24.md`（30,961 B／`4af3a674a6be`）。**原文所在件**：`tools\exp_harness.py`（45,590 B／`ce64b9b97489`）。

### §R-3-1 ③ 之两面（必读，勿混）

- **③-甲（本格内·`B_t` 之所在单位）**：由 §OI-1b-1 同行之「预算值 3／预算单位」直读可知，`B_t`＝3 **恒以该格自身之单位表述**（约束短语原式），故**本格内**换算恒为 1:1（`B_t`＝3 × 该格单位），20/20 格皆然。**此恒等关系不作 ③ 之实质答案**——否则 ③ 沦为无信息量之恒真式。
- **③-乙（至公共参考单位）**：即 §R-3 之表所列之 `k` 与 `B_ref`，**5/20 格可核，15/20 格 `UNOBTAINED`**。本棒主口径取此。
- **③ 之数之性质**：`2.592 E+05 s`／`1.08 E+04 s` 系**已登记常数 `B_t`＝3 之单位换算代入**（`3` 之出处见 §R-2-3），**非占用量、非收益／代价、非正解、非最优动作、非排名、非统计量**。

### §R-3-2 可得度（两口径并出）

| 口径 | 三列齐 | 部分（①②得·③缺） | 三列全缺 |
|:--|:--:|:--:|:--:|
| **主口径**（③＝至公共参考单位之可核系数，依 K3.1 `conversion_reference` 之 `B_reference = 3 × k`） | **5/20**（`t_05`·`t_08`·`t_11`·`t_13`·`t_15`） | **15/20** | **0/20** |
| 宽读（③＝本格单位与 `B_t` 所在单位之关系，恒 1:1） | 20/20 | 0/20 | 0/20 |

⚠ 口径之归属为 PI／verdict-keeper 之裁；本棒 ⛔ 0 代裁、⛔ 0 判五终判。
⚠ **该计数于两口径下之稳健性**：若对 ① 采「须含所指资源之**物理**量纲」之严读，则 `unit` 之 12 格之 ① 亦降为部分 —— 而**三列齐之 5 格不变**（皆为时间量纲），全缺仍为 0。故「5／15／0」于两读之择皆稳。

---

## §R-4 缺件具名（逐格具其因，⛔ 0 只写「缺」）

| 缺件 | 具名之因 |
|:--|:--|
| `t_01`·`t_02`·`t_04`·`t_06`·`t_07`·`t_09`·`t_10`·`t_12`·`t_14`·`t_17`·`t_18`·`t_19`（`unit`，12 格）之**第 ③ 列缺** | 因**盘上无 `unit` 之物理身份、亦无可核之换算系数**：K31B B-occupancy md **L17** 明载 `unit` 之「conversion to any external measurement are not supplied」，且「not commensurable with a quantum from another scenario」⇒ 无 `conversion_reference` ⇒ ③ 不可算。⛔ 0 以估算／类比／他案之值／默认值充。 |
| 同上 12 格之**第 ① 列「所指资源之物理量纲」缺** | 因盘上**无名**：约束短语只给 `3 units`，未给所指资源之物理量纲。⛔ 0 以情境标题（如 `Water allocation`）反推体积／质量——**本棒未作此反推**；表中 ① 所填「计数（情境资源量子／无量纲之配额）」乃**计量之计数**量纲，非其物理量纲，此区别已明书。 |
| `t_03`·`t_16`·`t_20`（`round`，3 格）之**第 ③ 列缺** | 因**盘上无 `round` 之起讫与时长定义**：K31B B-occupancy md **L20** 明载「neither is supplied, so no seconds conversion is made」⇒ 不可换算为秒，NIST 之 day/hour 条款**不适用于 `round`**（其非时间单位）。 |
| **全 20 格**之**逐动作占用量** | 因素材 `scenarios` 元组**仅含** (标题, payoff 字典, 3 句约束文本) 三元，**无 occupancy 字段**（§OI-1b-2 **L150**；`_t5_inputs_construction_plan_2026_10_23.md` **L126** 互证）⇒ 本面之值不可得。**本棒 ⛔ 0 答任何占用量数值。** |

**另附具名之界**：`step`（步数上限 3）**非** `B_t` 所量之预算量 —— K31B B-occupancy md **L21** 明载其为模型计数单位且「not merged with resource occupancy」⇒ 本棒**未**以步限充预算单位。

---

## §R-5 阴性断言之射程与正控（两项齐备）

### §R-5-1 四根实枚举（错误数皆 0）

| 根 | 实枚举件数 | 备注 |
|:--|:--:|:--|
| `〔本地路径已脱敏〕` | **7,796** | — |
| `〔本地路径已脱敏〕` | **1,275** | — |
| `〔归档区〕` | **40,242** | 仅**按名＋指纹**认人（⛔ 0 读正文） |
| `〔本地路径已脱敏〕` | **106,007** | 件数随本会话自身生成之运行日志而递增（第二轮合计 155,417） |

> 📌 递归扫描一律 `-ErrorAction SilentlyContinue` **并另取 `-ErrorVariable` 计数**，四根之错误数皆 **0** ⇒ 无静默失败之假阴性。

### §R-5-2 正控（双证）

| 正控 | 结果 |
|:--|:--|
| **同一性正控** | `tools\exp_harness.py` ＝ **45,590** B／SHA-12 **`ce64b9b97489`**，与派工单所载**逐位相符**（开工时与落盘前两次实测皆同值）。 |
| **活性正控** | 同一批扫描模式（`cap = 3 units`｜`shelf life 3 rounds`｜`cold chain 3 hours`｜`grid limit 3 units`｜`budget_unit`｜`budget_quantity_definition`｜`B_t_role`）于仓内根**命中 ≥35 件**（含 §OI-1b-1 与 `exp_harness.py` 本身）⇒ 模式为**活**，余根之 0 命中为有效阴性。 |

### §R-5-3 逐根阴性（含假阳性与自污染之判定）

| 根 | 射程 | 结果 |
|:--|:--|:--|
| `deposon-repo` | 内容面 + 名面 | **命中**（P-1／P-2 载体在焉，见 §R-2）。 |
| `deposon-sub` | 内容面全 1,275 件 ＋ 名面 | 内容面命中 **1** 处＝**假阳性**：`deposon_team\plugins\_v42_v2_runner_2026_09_16.py` **L323／L332** 之函数形参名 `budget_unit`（属他案，与 `T5` 逐格预算面无关）⇒ **0 件 T5 逐格预算载体**。该命中同时**证模式为活**。名面 0 件 `t5_desensitized|desensitized_pack|t5_inputs|constraint_initialization|feasibility_rule|grounding_basis`。 |
| `〔归档区〕` | **仅名面＋指纹** | 名面 **0** 件 T5 预算摘要类载体名。名含 `t5`／`budget`／`occupancy`／`constraint` 者 23 件已列；与本面相关者唯 `results\doc\document\budget.json`（406 B／`19149bc59be9`）、`results___deposon_v20_gt5.json`（72,647 B／`fca14c5735dd`）、`…gt5b.json`（56,425 B／`2907006dbe48`）——**三者正文皆未读**。⇒ 本棒对该根**不作**「无载体」之断言，仅作「名面无 T5 预算摘要类载体名」之断言。 |
| `〔本地路径已脱敏〕` | 名面全枚举 ＋ 内容面**限域** | 名面 **0** 命中载体名。内容面：①**非转录面**（排除 `v2\sessions\`、`v2\observability\`、`background-tasks\`）实扫 **8,714** 件，命中 **4** 件，**全在** `v2\sqlite\runtime-state.sqlite*`（运行时状态库，内含会话文本）⇒ **非**结构化逐格元数据载体；②**转录面 97,402 件未扫**（⛔ 0 断言其 0 命中）；全根内容面**未竟**（落盘时后台扫描仍在跑，其命中项 **100%** 落于 `background-tasks\`、`v2\observability\logs\sessions\`、`v2\sessions\**\*.jsonl` 与 `.history-mutation-*\snapshots\*.jsonl` 之**会话转录／自污染**面）。⇒ 本棒对该根**只作**「名面无载体 ＋ 已扫及之非转录面无结构化载体」之**限域断言**。 |

---

## §R-6 勘误注记与射程辨析（⛔ 0 回改既有件一字，仅登记）

| 编号 | 事项 | 本棒之实测 | 本棒之处置 |
|:--|:--|:--|:--|
| **E-1** | `results\work\external_blind_grounding_k31_2026_10_24\T5_input_B_occupancy_K31B_2026_10_24_constraint_initialization.csv`（5,728 B／`e89de0cbc569`）之 `budget_unit` 字段 **20/20 行为 `NOT_IN_RANGE`**；同族 md（7,703 B／`42e03b658e8a`）**L47**：「The per-cell physical/resource unit of `B_t` and `r_t_0` is `NOT_IN_RANGE`, because the actual budget-digest body was not supplied.」 | 仓内实有逐格单位之载体（§OI-1b-1，20/20 行皆有「预算单位」列）。 | **射程辨析（非翻案）**：该 `NOT_IN_RANGE` 之射程为「**受托方之可用材料面**」，非「仓内材料面」。本棒 ⛔ 0 回改该二件一字，仅登记；采认归 PI。 |
| **E-2** | K31B 单位轨（`T5_BO_unit_calibration_K31B_2026_10_24.md`，10,607 B／on-disk `3331fb233aa4`）**L129** 结论「三列齐 0/20 · 三列全缺 20/20」，其 §R-2 之 S-1 明书「附件本体不在本次可用材料中」 | 该「附件本体」**在仓内根**：`_t5_desensitized_pack_2026_10_24.md`（31,937 B／`90a5e34e1ae6`），其 `§OI-1b` 切片 4,706 B／`63eb88aaf9fd`（与该轨 L36 所引附件之 manifest 同值）。 | **材料面之实测事实**登记。本棒 **⛔ 0 判该答之对错**（⛔ 0 判五终判）；采认与口径之择归 PI／verdict-keeper。 |
| **E-3** | **锚链面之指纹双命名空间**：K31B 二件之**件内自证 `SELF_SHA12`** 与本棒实测 **on-disk SHA-12** 不同，而**字节数相同**（6,511／10,607）。 | 以两件自述之「定宽零化代入法」复算（仅替换 `SELF_BYTES`／`SELF_SHA12` 两字段之值为零化串，其余字节不变）：`T5_BO_meta_paths_K31B_2026_10_25.md` 零化后 SHA-12 ＝ **`1fb137d79030`** ＝ 其件内自证值（**MATCH**）；`T5_BO_unit_calibration_K31B_2026_10_24.md` 零化后 SHA-12 ＝ **`4a25edaab099`** ＝ 其件内自证值（**MATCH**）。 | **自证链自洽 ⇒ ⛔ 0 判为篡改**；乃两命名空间之别。**引用 K3.1／K31B 之件时必明书所用空间**（见 §R-6-1）。本棒以 **on-disk 实测值**为引用基准。 |
| **E-4** | **仪器误差自陈（本棒自身）**：首读 `tools\exp_harness.py` 之 `read` 渲染将 **L722** 误显为 `higher payoff is better` | 以 `ReadAllLines` ＋ `Select-String` **两法独立**复核：**L722 实为 `payoff is fixed per path`**（＝`N1`），与 §OI-1b-1 之 `t_15`＝`N1`（**L133**）相符；且 §OI-1b-2 **L149** 之分布与源推得之分布相符。 | **无件之缺陷**；系**本棒仪器（`read` 渲染）之误差**。依「测量仪器自身即误差源」之戒：**改仪器（改用行号回读＋双法复核）不改文本**。本件**全部引用皆以行号回读为准**。 |

### §R-6-1 引用件指纹表（on-disk 实测 · 本棒自算）

| 件（仓相对路径） | 字节 | on-disk SHA-12 | 件内自证 `SELF_SHA12`（零化代入法） |
|:--|--:|:--|:--|
| `results\work\process\_t5_desensitized_pack_2026_10_24.md` | 31,937 | `90a5e34e1ae6` | —（件内自承「随交付回执报出」） |
| `results\work\process\_t5_desensitized_pack_v2_noD_2026_10_24.md` | 30,961 | `4af3a674a6be` | — |
| `tools\exp_harness.py` | 45,590 | `ce64b9b97489` | — |
| `results\work\process\_t5_inputs_three_track_2026_10_23_redacted_v1_2026_10_24.md` | 53,734 | `ee07d58a1ee2` | — |
| `results\work\process\_t5_inputs_three_track_2026_10_23.md` | 52,945 | `7709625c6779` | — |
| `results\work\process\_t5_inputs_construction_plan_2026_10_23.md` | 85,336 | `3982b82f095b` | — |
| `results\work\process\_t5_desensitized_pack…` 之委托函 `letters\_commission_t5_inputs_external_EN_round2_draft_2026_10_24.md` | 64,125 | `e2cd66b1b543` | — |
| `letters\_commission_bo_three_columns_narrow_v1_2026_10_24.md` | 7,044 | `e4ce25e6b8d8` | — |
| `results\work\external_blind_meta_paths_k31_2026_10_25\T5_BO_meta_paths_K31B_2026_10_25.md` | 6,511 | `1b95d97b8a1d` | `1fb137d79030`（零化代入法，MATCH） |
| `results\work\external_blind_units_k31_2026_10_24\T5_BO_unit_calibration_K31B_2026_10_24.md` | 10,607 | `3331fb233aa4` | `4a25edaab099`（零化代入法，MATCH） |
| `results\work\external_blind_grounding_k31_2026_10_24\T5_input_B_occupancy_K31B_2026_10_24.md` | 7,703 | `42e03b658e8a` | — |
| `results\work\external_blind_grounding_k31_2026_10_24\T5_input_B_occupancy_K31B_2026_10_24_constraint_initialization.csv` | 5,728 | `e89de0cbc569` | — |

---

## §R-7 0 触动自证

| 项 | 结果 |
|:--|:--|
| 对既有件之写操作 | **0**。本棒之写操作仅 **1** 次 ＝ 落本件。 |
| 移动／重命名／删除／新建目录 | **0**（未动既有件一字；未新建目录）。 |
| 跑实验 | **0**（未 import／未执行 `exp_harness.py`；只作**文本**读取与正则抽取）。 |
| 读 `〔本地路径已脱敏〕` | **0**。 |
| 调 LLM／API | **0**。 |
| 联网 | **1** 次，且**仅**取 NIST SP811 B.9 之换算系数（§R-2-4）⇒ 未用于补「格→预算量」对应链。 |
| 归档区 | **0** 次读正文；仅按名与指纹认人（§R-5-3）。 |
| 冻结资产指纹之同一性复验 | `tools\exp_harness.py` 于开工时 ＝ **45,590** B／`ce64b9b97489`，落盘前复测 **同值**（逐位相符）⇒ 本棒对其 **0 触动**。 |

---

## §R-8 老实交代（逐条）

1. 本棒**只取数**：⛔ 0 判五终判、⛔ 0 闭 `KD`、⛔ 0 宣告段毕或门槛成就、⛔ 0 代 PI 裁。「载体在盘」为**登记面之实测事实**，非裁定；采认归 PI。
2. 本棒**未答**任何占用量数值、收益／代价数值、正确解、最优动作、排名或统计量。③ 之 `2.592 E+05 s`／`1.08 E+04 s` 系**已登记常数 `B_t`＝3 之单位换算代入**，已在 §R-3-1 明标其性质。
3. 读 `exp_harness.py` 时**看见了** payoff 字典与 `correct` 之计算代码（L736–L745）：⛔ 0 摘录、⛔ 0 推断正解、⛔ 0 写入本件。本件之全部内容不涉 `value`／`correct`／`payoff` 之数值。
4. `§OI-2-D`（内面，含 `value` 聚合统计）：本棒**未读、未引**（且无此必要）——本面之所需不出于该节。
5. 联网**仅一次**，仅取 NIST SP811 B.9 之 Time 换算系数（day→s 8.64E+04、hour→s 3.6E+03，并注意同节之 sidereal 另列，本棒取非恒星者）。⛔ 0 用联网补「格→预算量」之对应链。
6. **仪器误差自陈**：首读 `read` 对 `exp_harness.py` L722 之渲染误显为 `higher payoff is better`；经 `ReadAllLines` ＋ `Select-String` 两法独立复核，实为 `payoff is fixed per path`（＝`N1`），与 §OI-1b-1 之 `t_15`＝`N1` 相符 ⇒ **无件之缺陷，系本棒仪器之误差**。已改仪器（全部引用改以行号回读为准）**未改任何文本**（§R-6 之 E-4）。
7. `deposon-sub` 之 1 处内容命中为**假阳性**（`_v42_v2_runner_2026_09_16.py` L323／L332 之形参名 `budget_unit`）；该命中**证模式为活**，故其余根之 0 命中有效。
8. `.minimax` 之内容面命中 **100%** 落于会话日志／转录／运行时状态库（**含本会话自身扫描指令之回显＝自污染**）；其**非转录面**实扫 8,714 件、命中 4 件（全在 `v2\sqlite\runtime-state.sqlite*`）、错误数 0；**转录面 97,402 件未扫**，全根内容面**未竟** ⇒ 本棒对该根**只作限域断言**，⛔ 0 断言「0 命中」。
9. 归档区**未读任何正文**；其 `budget.json`／`gt5.json`／`gt5b.json` **仅按名与指纹认人**。本棒**未**断言该根「无载体」。
10. `unit` 之 ① 列本棒填「计数（情境资源量子／无量纲之配额）」，而**所指资源之物理量纲盘上无名**；本棒**未**以情境标题反推体积／质量（⛔ 0 类比）。该区别已在 §R-3 表与 §R-4 双处明书。
11. `round` 之 ③ **未**借 NIST 之 day/hour 条款充（`round` 非时间单位）；`step`（步限 3）**未**充预算单位。
12. 三列可得度 **5／15／0** 系**本棒取数口径**（③＝至公共参考单位之可核系数）之结果；宽读口径则为 20/20/0。两口径之别**归 PI／verdict-keeper**，本棒 ⛔ 0 代裁。
13. 本件为**唯一新件**；未回改既有件一字；未移动／重命名／删除；未新建目录；未跑实验；未调 API。`.tmp\_bcheck.py` 为**既存**件（466 B），本棒**未改**之，仅依令调用。
14. 本棒未查四根之外之盘（`〔本地路径已脱敏〕` 依铁律不读；`Deposon_v1_2_0_交付包` 不在四根之列，**未查**，未扩射程）。
15. 本件之**自指纹不写于本件内**（自指之循环不入件）——其 BYTES／SHA-12／bcheck 六项**随交付回执报出**。

---

## §R-9 自证

- 本件之 `SELF_BYTES` ＝ **随回执报出**
- 本件之 `SELF_SHA12`（on-disk）＝ **随回执报出**
- 编码：**UTF-8 无 BOM** · **纯 LF**（CR ＝ 0）· **末字节 `0x0A`** · **U+FFFD ＝ 0**
- 复算工具：`python -P .tmp\_bcheck.py <本件路径>`（既存件 466 B，本棒未改之），输出六项 ＝ `BYTES`／`SHA12`／`SHA256`／`BOM·CR·VT·FFFD`／`LAST_BYTE·NON_ASCII·LF`。
- 观测时点：**2026-10-25T03:39+08:00 起 · 2026-10-25T04:0x+08:00 止**（本棒会话）。
