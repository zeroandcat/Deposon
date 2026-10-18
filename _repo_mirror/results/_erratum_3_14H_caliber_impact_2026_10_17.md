# `3/14·H` 口径冲击面勘误件（3/14·H 另立勘误面 · append-only · ⛔0 回改任何在册件）

| 项 | 内容 |
|:--|:--|
| **件类** | **勘误件（append-only 注记面）** —— 依 PI 2026-10-17 ≈15:56 之裁（卡 `ask_863c78d2c786b5c70829c977` · Q3「回函实质影响」· 所择 `q3_reply_opt1`）之**第二项**「在册 3/14·H 之载**另立勘误面**（另议或勘误件·**0 回改**）」 |
| **PI 逐字答** | 「**采认＋3/14·H 另立勘误面（推荐）**」（选项 id `q3_reply_opt1`·`recommended: true`·`A:` 成对行） |
| **所择档 description（逐字）** | 「回执之 underivable 交付采认为 T-2/T-3 之终态（数值面以「不可得＋理由」落档·终判上限 kd 面）；在册 3/14·H 之载另立勘误面（另议或勘误件·0 回改）」 |
| **本件之射程（只此一项）** | **只就「在册 3/14·H 之载」发勘误注记**（§1–§4）＋**如实登记 KD**（§5）。📌 **⛔0 及于回函三重论断之正确性**（§5-KD-1） |
| **本件 ⛔0** | ①回改／废记／销记任何在册件之一字；②闭 `C5-b`；③裁 161 件两读；④宣告①毕；⑤复算回函之任一算术；⑥为 30 格之任一格回填数值；⑦代 PI 择径（勘误件 vs 另议） |
| **落盘纪律** | UTF-8 无 BOM·纯 LF·`io.open` 直写·落前 `Test-Path=False` ＋ `glob 0 命中`（已实测·§0-3）·**append-only** |
| **状态** | **本件 ⛔0 自充生效件**；其效力界分见 §3-3 |

---

## §0 回读实测节（**先实测·⛔0 沿用转述**）

> 📌 本节全部数值系**本棒亲算**（`Get-FileHash -Algorithm SHA256` · 取前 12 位；字节数系 `ReadAllBytes().Length`），**⛔0 转录任何他件之转述**。

### §0-1 三件回读结果（派工单所载 vs 本棒实测）

| # | 件（路径） | 派工单所载 SHA-12／bytes | **本棒实测 SHA-12／bytes** | 判定 |
|:--|:--|:--|:--|:--|
| ① | `letters/REPLY_FROM_COPILOT_AGENT_T2_T3_THEORY_INPUTS_2026_10_17.md` | `597caf8ba5bc`／30,459 B | **`597caf8ba5bc`／30,459 B** | ✅ **相符**（BOM=no·CRLF=318） |
| ② | `results/_copilot_reply_adoption_effect_2026_10_17.md` | `dc4b450b2878`／— | **`4a89f8d3ddda`／39,705 B** | 🔴 **不符** ⇒ 见 §5-KD-2 |
| ③-a | 判死面 v1 生效件＝**`results/_killface_v1_effect_register_2026_10_16.md`** | `98aabe87ae11` | **`98aabe87ae11`／21,872 B** | ✅ **相符**（派工单未给路径·本棒由指纹反查定位·§0-2） |
| ③-b | U 轴 ACTIVE 件＝**`results/_u_axis_active_ruling_register_2026_10_16.md`** | `30fed54c3d09` | **`30fed54c3d09`／22,219 B** | ✅ **相符**（同上） |

### §0-2 指纹反查（派工单仅给指纹·未给路径者）

- `98aabe87ae11` → `results\_killface_v1_effect_register_2026_10_16.md`（21,872 B）
- `30fed54c3d09` → `results\_u_axis_active_ruling_register_2026_10_16.md`（22,219 B）
- 🔴 **`dc4b450b2878` → 全仓递归（所有扩展名·0 排除 `.git`）0 命中／0 件；文件名面 glob 亦 0 命中** ⇒ **该指纹在盘无正身**（§5-KD-2）

### §0-3 落前占用检查（实测）

- `Test-Path` 目标路径 ＝ **`False`**
- `results/` 内 `erratum`×`3_14`／`3_14`×`erratum` 之 `glob` 命中数 ＝ **`0`**
- ⇒ 📌 **⛔0 启用 `_r1` 后缀**（无占用）

---

## §1 冲击面 ｜ 在册「`L(M1,T)=3/14·H`」之全部载点清单

> 📌 **扫描口径（本棒实测·非转述）**：`results/`＋`letters/`＋`docs/`＋`reviews/`＋`verifier/`＋仓根，递归、全部 `*.md`／`*.py`／`*.json`／`*.txt`，**⛔0 排除 `.tmp/`**（`.tmp` 为他棒写盘脚本与临时件·非在册件）；探针逐字串 ＝ `3/14` ∪ `L(M1,T)`。**实测总计：90 命中行／32 件**；经逐行判读后**真载点 68 行**、**假阳性／异义 22 行**（§1-4）。

### §1-1 T1 级 ｜ 锁值主载面（**正面冲击之靶心**）

| # | 路径 | 行号 | 逐字（承载句·原样） | 件指纹／bytes |
|:--|:--|:--|:--|:--|
| **1** | `results/_prereg_lock_v1_epsilon_lu_klm41_register_2026_10_15.md` | **L71** | 「\| **锁入之值** \| **``L(M1,T)=3/14·H≈0.2143H``**（闭式 ＝ `3·g_aether / [(1−η)+η·g_couple+4·g_aether] · H`） \|」 | `a3dd3cc1caf2`／18,582 B |
| **2** | 同件 | **L72** | 「\| **限族（强制标注 · ⛔0 越族）** \| **仅**「**4 选 1 且 `value` 二元**」族成立（回函 §2.1(c) 自身限定 "for a symmetric 4-choice task"）；**族差照录**：**T3 ＝ `7/29`**、**T4 ＝ `1/12`** ⇒ ⛔0 将 `3/14` 移用于族外 \|」 | 同上 |
| **3** | 同件 | **L74** | 「\| **本棒独立复算（`Fraction` · 实测）** \| `3·(1/10) / [(1−1/2)+(1/2)·1+4·(1/10)] = (3/10)/(7/5) = 3/14 = 0.21428571… ⇒ **0.2143** …」 | 同上 |
| **3b** | 同件 | **L73**（连带行·不含 `3/14` 字面） | 「\| **三参数之冻结** \| **`η=0.5`／`g_couple=1.0`／`g_aether=0.1`** —— **原系构造函数默认值**（`tools/exp_harness.py:56`），**经本卡裁转 prereg 冻结值**（给值单 `21abb5173b87` `:107`／`:120` 之「默认值 ≠ 冻结值 · 须 PI 冻结」限定语**由本裁闭合**） \|」 | 同上 |
| **3c** | 同件 | **L75／L76**（连带行） | L75「\| **射程附记（照录不动）** \| `M_2` 仍登记为 `structural zero`（`L(M2,T)=0`）… \|」／L76「\| **⛔0 调和之二在册诊断（并存不调和照录）** \| ① **`S-4`**…② **`S-5`**…——**本件之 `L` 入锁不推翻该二诊断** \|」 | 同上 |
| **4** | `results/_prereg_lock_v2_h_epsilon_gamma_taucert_u_register_2026_10_15.md` | **L205** | 「\| 4 \| **`L` 限定值** \| §2-2 **`L(M1,T)＝3/14·H`** 入锁 ＋ 三参数转冻结（L71–L73） \| **本件不触**（Q1／Q3 裁面均不涉 `L`） \| **v1 逐字继续有效** \|」 | `4c782fc8566b`／33,312 B |

📌 **T1 小计：3 探针命中行（L71／L72／L74）＋ 3 连带行（L73／L75–L76）／2 件**。

### §1-2 T2 级 ｜ 核验·存疑·采认登记面（**回函之拒已在册预置者**）

| # | 路径 | 行号 | 逐字（承载句·原样） | 件指纹／bytes |
|:--|:--|:--|:--|:--|
| 5 | `results/_gemini4_reply_verification_register_2026_10_15.md` | **L72**（`F3`） | 「\| **F3** \| `L(M1,T) = 3g_aether/[(1−η)+ηg_couple+4g_aether]·H = 3/14·H ≈ 0.2143H` …**算术相符**… ✅ \| **射程不符**：该闭式**仅**对「4 选 1 且 value 二元」族成立；本审计复算 T3（诱饵 0.5）＝**7/29**、T4（2 选 1 二元）＝**1/12** … \| 🔴 **不符**（算术相符·**表述射程过宽**） \|」 | `793986174b23`／33,393 B |
| 6 | 同件 | **L73**（`F4`） | 「\| **F4** \| 3/14 推导所用参数＝「for default η=0.5, g_couple=1.0, g_aether=0.1」 … **在册限定语未被携带** … **3/14 成立于**未冻结**前提** \| 🔴 **不符**（缺在册限定语…） \|」 | 同上 |
| 7 | 同件 | **L104**（`X2`） | 「\| **X2** \| `L(M1,T) = 3/14·H` 于 T2 终判／§5 汇总中**去限定**表述 … \| 🔴 **冲突并存** … ⛔0 调和 \|」 | 同上 |
| 8 | 同件 | **L105**（`X3`） | 「\| **X3** \| 3/14 之参数（η/g_couple/g_aether） \| 给值单 **`:107`／`:120`**（默认值 ≠ 冻结值 · **须 PI 冻结**）… \| 🔴 **冲突并存** …**以未冻结参数为条件** \|」 | 同上 |
| 9 | 同件 | **L151**（`P2`） | 「\| **P2** \| **`L` 式**：`L(M1,T) = 3g_aether/[(1−η)+ηg_couple+4g_aether]·H = 3/14·H` \| **经核验相符**（`Fraction` 复算逐位，F3）＋**存疑** \| ①射程仅「4 选 1 且 value 二元」族（T3＝7/29、T4＝1/12）；②参数**未冻结·须 PI 冻结**（X3）；③未携在册 `S-4`／`S-5` 诊断（X2） \|」 | 同上 |
| 10 | 同件 | **L55／L142／L225** | L55「…**附注（实测强于回函）**：`:202` T3 之诱饵值＝**`0.5`（非 0）**，故 T3 之 value 非二元 1/0（影响 F3 之 3/14 射程）…」／L142「…3/14 与 `U` 式算术…**经实测全部成立**。」／L225「…`ε*(H)=H/10` 随 `H` 变…**与在册 prereg §6④ 不相容**，且 `H` 之精确值本身「须 PI 另给·0 代给」⇒ `ε*` 与 `3/14·H` 两式**皆成立于未冻结前提**，须 PI 先裁「口径④ vs H 依赖式」与参数冻结，**方可采认**。」 | 同上 |
| 11 | `results/_pi_card_answers_register_2026_10_15_v14.md` | **L29** | 「- **登记注记**：选项全文义＝**采 `L(M1,T)=3/14·H` 限「4 选 1 且 value 二元」族**＋默认值转冻结（`η=0.5`／`g_couple=1.0`／`g_aether=0.1` **经本裁转为 prereg 冻结值**）＋**U 式之 route-乙 定义面修订核准**…」 | `ac3b580defbb`／5,805 B |
| 12 | 同件 | **L27** | 「- **题面摘要**：`L(M1,T)=3/14·H`——经核验相符但三存疑（射程仅「4 选 1 且 value 二元」族；参数未冻结须 PI 冻结；未携在册 S-4/S-5 诊断 X2）…」 | 同上 |
| 13 | `results/_prereg_caliber4_epsilon_revision_2026_10_15.md` | **L63** | 「\| **6** \| 本棒独立复算（`Fraction` · 实测） \| `η=1/2`／`g_couple=1`／`g_aether=1/10` ⇒ …`3·(1/10)/(7/5) = 3/14`… \|」 | `e49c11b43c65`／9,659 B |
| 14 | `results/_gamma_taucert_sourcing_2026_10_15.md` | **L157** | 「…其对总权重之份额实测为 `3·g_aether/W = 3·0.1/1.4 = 3/14 = 0.214286…`——**此值恰等于 `L(M_1,T)/H = 3/14`**…⇒ **`g_aether` 归属 `L` 面之量纲，非 `U` 面之时间衰减率**…」 | `6630447e5ec7`／34,667 B |
| 15 | `results/_d1_ab_deliberation_judgment_2026_10_15.md` | **L54** | 「- **D1-B（`:244`）**：「…noisy `M1` observation channel `Q_{M1}`, activating the exact bounds `L(M1,T)=3g_aether/[(1-η)+ηg_couple+4g_aether]·H` and `U(M,T)=H·τ_cert/[1-(1-γ)^H]`」。」 | `88c2af72ff7b`／46,542 B |

📌 **T2 小计：13 探针命中行／5 件**（`793986174b23` 8 行＋`ac3b580defbb` 2 行＋`e49c11b43c65`／`6630447e5ec7`／`88c2af72ff7b` 各 1 行）。

### §1-3 T3 级 ｜ 回函本体及其转录·引用·卡面登记面（**载「已载该拒」而非载「锁值」**）

| # | 路径 | 命中行号 | 性质 | 件指纹／bytes |
|:--|:--|:--|:--|:--|
| 16 | `letters/REPLY_FROM_COPILOT_AGENT_T2_T3_THEORY_INPUTS_2026_10_17.md` | **L48／L129／L148／L188／L300**（5 行） | **回函本体·论断①之拒**（逐字见 §2-1） | `597caf8ba5bc`／30,459 B |
| 17 | `letters/_commission_t2_t3_theory_inputs_2026_10_17.md` | **L51**（1 行） | 委托函·`T-2` 交付描述转录 | `393d71e51fbf`／22,746 B |
| 18 | `letters/_commission_t2_t3_theory_inputs_copilot_agent_2026_10_17.md` | **L54**（1 行） | 同上（copilot 副本） | `385003e41ce2`／23,919 B |
| 19 | `letters/_commission_t2_t3_theory_inputs_grok_2026_10_17.md` | **L54**（1 行） | 同上（grok 副本） | `6922929bfda8`／23,906 B |
| 20 | `results/_copilot_agent_t2_t3_reply_register_2026_10_17.md` | **L34／L70**（2 行） | 回函之登记转录 | `1767d8fb075d`／16,863 B |
| 21 | `results/_c5b_closure_verdict_2026_10_17.md` | **L72**（1 行） | 以**本体行号**引「`3/14·H` 之拒」（L48／L148） | `660555b9b6be`／26,218 B |
| 22 | `results/_copilot_reply_adoption_effect_2026_10_17.md` | **L8／17／28／29／31／40／59／61／77／81／82／85／90／91／94／130／141／178／182／186／199**（21 行） | **采认落档件·§5「3/14·H 勘误面（候派登记）」** | `4a89f8d3ddda`／39,705 B |
| 23 | `results/_pi_card_answers_register_2026_10_17_v55.md` | **L53／75／77／98／112／172／175／177／178／179／183／185／189／200／253／254／266／267／272**（19 行） | 卡面登记件·Q3 问／答逐字＋`KD-1/2/7` | `84f6c4bfdb07`／54,188 B |

📌 **T3 小计：51 探针命中行／8 件**。

### §1-4 假阳性／异义排除表（**22 行／13 件 · ⛔0 充载点**）

| 类别 | 路径·行号 | 逐字/实测 | 排除理由 |
|:--|:--|:--|:--|
| **异义 A：实测 `D` 列读数（非 `L(M1,T)`）** | `results/_three_seed_measurement_exec_2026_10_16.md` L118／L144；`results/_ge01_s3b_v_exec_2026_10_16.md` L103 | L103 逐字「\| `M1_Deposon_TRA`／`T1` \| 15 \| 14 \| **4** \| 3 \| `3/14` \|」 | 🔴 **该 `3/14` 系三 seed 实测表之 `D` 比率读数**（分母 `14` ＝ valid 数），**与 `L(M1,T)=3/14·H` 无语义承继** ⇒ ⛔0 充锁值载点 |
| **编号／日志族（`13/14`／`13/14/15`／`K-D-14`／`γ-13/14`／`MQ-05/13/14`）** | `results/_kd_11_12_resolution_register_2026_10_16.md` L133；`results/_citation_corrigenda_volume_2026_10_17.md` L146；`results/_count_chain_independent_review_2026_10_13.md` L130；`results/_plan_v3_pending_verify_2026_09_30.md` L46；`results/_fake_verdict_reverify_sixitem_ledger_2026_09_30.md` L329；`results/_root_session_history_memo_main_2026_10_14.md` L172／L447；`results/_v4_pi_cot_v3_questionnaire_v2_d8_2026_09_28.md` L78；`results/_v4_pi_cot_v3_verdict_v3_signoff_2026_09_27.md` L413／L481；`results/_v5_gt_verdict_2026_09_29.md` L435；`results/_tmp_write_copilot_register.py` L41／L77；`reviews/review_coach_v2X_draft_r2.md` L3；`verifier/runs/v30_run1.md`·`v30_run2.md`·`v30_run3.md` L6；`verifier/v30/check.py` L19 | 例：L133 逐字「…「仍候裁 ＝ `K-D-1/2/3/4/6/7/13/14`」…**漏列者 ＝ `K-D-9`**」；L78 逐字「6 类 = 14/13/14/13/13/13」 | 🔴 **纯序号／修订日志之 `13/14`** ⇒ ⛔0 充载点 |
| **`root_session_history_memo_main_2026_10_14.md` L230** | 逐字载 gemini4 回函结论「T2 判 underivable-as-stated/derivable-with-relaxation（L(M1,T)=3/14·H；T-3 route-乙 U=H·τ_cert/[1−(1−γ)^H]）」 | ⇒ 📌 **判为「转述载」而非锁值载**（历史备忘录·非锁值面）；为免遗漏**计入 T3 之历史面**（不计入 T1/T2 之冲击靶心） |

**§1 合计**：**真载点 68 行／15 件**（＝T1 6 行·2 件 ＋ T2 13 行·5 件 ＋ T3 51 行·8 件）；**假阳性／异义 22 行／13 件**；**扫描总计 90 行／32 件**（68＋22＝90 ✓·15＋13＝28＋4 跨类去重＝32 ✓）。

---

## §2 回函论断①之逐字与射程（**含口径辨析 · ⛔0 调和**）

### §2-1 论断①之逐字（`597caf8ba5bc` 正身·L48／L129／L145／L148／L188／L300）

| 行号 | 逐字 |
|:--|:--|
| **L48**（§2 处置表行） | 「\| `L(M1,T) = 3/14 · H` at `η=0.5`, `g_couple=1`, `g_aether=0.1`, offered for the `M1` cells \| **Rejected** \| Special case of one policy's error rate, not the spec's information-constrained minimum; holds only for 4 options with values `{1,0,0,0}`; the three parameters are constructor defaults, not frozen values. Arithmetic of that special case is confirmed in §3.5 and then not used. \|」 |
| **L129**（§3.5 标题） | 「### 3.5 Correction of the `3/14 · H` special case — not a delivered value」 |
| **L145**（闭式） | 「P(miss) = 3 · g_aether / ((1 - η) + η · g_couple + 4 · g_aether)」 |
| **L148**（**判读之核心**） | 「At the defaults, `w* = 1.1`, `w0 = 0.1`, total `1.4`, `P(miss) = 0.3/1.4 = 3/14`. **That arithmetic is right.** It is the indicator error rate of **this one sampler on that one value pattern**. It is also the error rate of the identity map on a single draw from that sampler. Either reading is a policy evaluation under a stipulated channel. **Neither is `L(M,T)` for a cell**, and **the pattern is not the harness pattern outside `T1` and `T2`**.」 |
| **L188**（`T-2` 终判词） | 「**`T-2` verdict: underivable as stated (obstruction: … the information-constrained minimum is a structural zero and not an IC-capacity solution; the mechanism singletons are policy evaluations, not that minimum; … `3/14·H` is rejected).**」 |
| **L300**（复算清单第 3 项） | 「3. The 4-choice zero-distractor weight ratio reduces to `3·g_aether / ((1-η)+η·g_couple+4·g_aether)`, and the defaults give `3/14`. **Then refuse it as a cell value** for the reasons in §3.5.」 |

### §2-2 口径辨（本节为本件之实体 · **⛔0 调和 · 如实并列**）

> **派工问面**：「在册载之 `3/14·H` 系何种口径（采样器误差率 vs 理论极小）——若口径本即「采样器读数」则回函之拒或不同靶」。

| 辨项 | **在册口径（实测）** | **回函口径（实测）** | 判定 |
|:--|:--|:--|:--|
| **B-1 值之身份** | `prereg_lock_v1` **L71** 置于「**锁入之值**」行、冠以 **`L(M1,T)`** 之名 ⇒ 在册将其登记为 **`M1` 之信息约束失真下界（`L` 之锁值）** | **L48**「Rejected」＋ **L148**「**Neither is `L(M,T)` for a cell**」 ⇒ 回函将其辨为 **「该单一采样器（`this one sampler`）于该单一 value 模式之指示器误差率」，并明言「Either reading is a policy evaluation under a stipulated channel」 | 🔴 **同源不同靶**：同一闭式、同一数值，在册赋「`L` 之锁值」之身份，在回函赋「采样器误差率」之身份并**因此被拒** ⇒ **正面冲击成立于「身份／口径」层**；📌 然 **L148 明言「That arithmetic is right」**、**L48 明言「Arithmetic of that special case is confirmed」** ⇒ **算术层不受冲击**。**⛔0 以「算术无误」充「口径无误」、⛔0 以「口径被拒」充「算术被驳」** |
| **B-2 参数冻结面** | `prereg_lock_v1` **L73** 逐字：「**原系构造函数默认值**（`tools/exp_harness.py:56`），**经本卡裁转 prereg 冻结值**」／`pi_card_answers_register_2026_10_15_v14` **L29** 逐字：「**经本裁转为 prereg 冻结值**」 ⇒ **在册：PI 已裁·三参数为 prereg 冻结值** | **L48** 逐字：「**the three parameters are constructor defaults, not frozen values**」 | 🔴 **正面冲突（如实并列·⛔0 调和）** —— 回函之陈述以「代码之实况（构造函数默认值）」为真；在册之陈述以「PI 2026-10-15 之裁（转冻结）」为真。二者**层次不同**（代码层 vs prereg 治理层），**⛔0 断言其一为误**。📌 **在册既有「未冻结」存疑面**（`793986174b23` L73／L105／`793986174b23` L151·`ac3b580defbb` L27 均载「参数未冻结·须 PI 冻结」）**已于 PI 裁后闭合**（L73 逐字「…限定语**由本裁闭合**」） |
| **B-3 射程限定语** | `prereg_lock_v1` **L72** 逐字：「**仅**「**4 选 1 且 `value` 二元**」族成立…**T3 ＝ `7/29`**、**T4 ＝ `1/12`**」／`793986174b23` **L72／L151** 同族逐字 | **L48** 逐字：「holds only for 4 options with values `{1,0,0,0}`」／**L148**「the pattern is not the harness pattern outside `T1` and `T2`」 | ✅ **口径同形、实体一致** —— 在册与回函**各自已载射程限定**，且族差值（`7/29`／`1/12`）**完全一致** ⇒ 📌 **字面差 ≠ 实体差**：卡问面所称「**限 4 选 1 且 value 二元族**」之**实体确在册**（仅逐字串「限 4 选 1」于全仓 0 命中，在册字面作「4 选 1 且 `value` 二元」）⇒ 🔴 **⛔0 断言「在册 0 有射程限定」**、**⛔0 断言卡问面失准** |
| **B-4 作用域** | 在册 **L72** 以「⛔0 将 `3/14` 移用于族外」**主动收窄** | 回函 **L148**「the pattern is not the harness pattern outside `T1` and `T2`」、**L172–L174** 逐格标注 T3「not the 4-choice formula」／T4「no shuffle; `T4-N05` has `best=0`」 | ✅ **两者同向收窄**；⚠ **回函更严**：其逐格表将 T5 亦排除（「zero-distractor formula does not apply」·L174），在册 L72 未列 T5 之独立族差 |

**§2-2 判定（不软化）**：🔴 **回函之拒系对「作为 `L(M1,T)` 锁值之 `3/14·H`」的正面冲击**，靶心 ＝ 在册 T1 级锁值主载面（`a3dd3cc1caf2` L71／`4c782fc8566b` L205）；📌 **⛔0 调和其算术**（回函自认算术正确）；📌 **⛔0 调和其射程**（在册已有同形限定）；🔴 **唯一未被在册消解者为 B-2 之冻结面冲突**，**⛔0 代裁**（§5-KD-3 候另议）。

### §2-3 论断②／论断③ 之逐字锚（**连带登记 · 本件 ⛔0 为其出勘误面**）

| 论断 | 载体行号（`597caf8ba5bc`） | 逐字（承载句） |
|:--|:--|:--|
| **② Route 乙「充分非 iff」** | **L52** | 「\| Route 乙 formula `U = H·τ_cert / [1-(1-γ)^H]`, claimed necessary and sufficient for all timings \| **Rejected as a cell value; the displayed equality is not an iff** \| It is a sufficient condition for one stipulated average-state certificate, tight only in a restricted mass range. `γ` and `τ_cert` are free. The state is not the harness. Counterexample in §4.4. \|」 |
| | **L241** | 「That is the displayed Route 乙 formula. It is **sufficient. It is not necessary**, and it is not tight for every `D`, because only the first coordinate has the maximum coefficient. For `D > 1` the worst timing must spill onto strictly smaller coefficients when `γ ∈ (0,1)` and `H > 1`.」 |
| | **L243／L248／L251／L258** | L243「### 4.4 Counterexample to the iff claim」／L248「U = 2 · (1/2) / (3/4) = 4/3」／L251「Coefficients in `Σ S` are `3/4` at `k = 0` and `1/2` at `k = 1`. Put mass `1` on `k = 0` and `1/3` on `k = 1` (total `D = 4/3`):」／L258「…solves `3/4 + (1/2)·x = 1` with `x ≤ 1`, hence `x = 1/2` and `D = 3/2`, which is strictly larger than `4/3`.」 |
| | **L262** | 「Direction, stated so it cannot be swapped: the formula is a **sufficient** robust tolerance for the average-state certificate under worst-case timing. It is not the tolerance for the terminal state `S_H` … It is **not necessary**. It is not a property of `M1`, `M2`, or `M3` as coded.」 |
| | **L286**（`T-3` 终判词） | 「**`T-3` verdict: underivable as stated (obstruction: the three coded mechanisms are memoryless… the Route 乙 closed form is a sufficient condition on a state process that is not the harness, **is not an iff**, and is not a cell value).**」 |
| | **L301**（复算清单第 4 项） | 「4. The average-state unroll in §4.3, and the `H=2`, `γ=1/2`, `τ=1/2` counterexample: formula `4/3`, actual worst-case average at that total `11/24 < 1/2`, tight robust total `3/2`.」 |
| **③ structural zero ／ `M2` `D≡0`** | **L47／L49** | L47「\| On-disk `M1`/`M2` information minimum is a structural zero, to be registered rather than sold as a solution \| **Accepted as a registration, not as a solved value** \| Re-derived in §3 from the harness call `mech.choose(p['options'], p)`. The context dict contains `value` and `correct`. \|」／L49「\| `M2` left as structural zero under that relaxation \| **Accepted as a registration** \| Same key exposure. Assigning `0` as a solution would fail anti-degeneracy. \|」 |
| | **L89** | 「…The information-constrained minimum of `Π_ctx` is therefore `0` on all 15 cells. That zero is **key exposure**. It is not an IC-capacity bound, and it is not a solution. It is **registered as a structural zero**.」 |
| | **L101** | 「…so this policy's loss is `0` under both readings, for every seed and every `H`. Realized **`D(M2, T) ≡ 0`** on the coded surface. That is still a structural zero, not an IC solution.」 |
| | **L204** | 「If the inequality to be certified is `D ≤ U`, every `U ≥ 0` satisfies it when `D ≡ 0`. `U` is not identified. Assigning one would be fabrication. This registration is per cell, not a number.」 |
| | **L275／L286** | L275「\| M2×T1 \| Registered, not assigned. \| `D ≡ 0` under §3.1 on the coded policy, so every `U ≥ 0` satisfies `D ≤ U`. \| fail \| fail \| fail \| fail \| reg \|」／L286（见上） |

---

## §3 勘误注记（**以本件为准之面 · append-only · 0 回改原件**）

### §3-1 注记之逐字（本件新增之唯一实体）

> **ERRATUM-314H-01** ｜ 在册载点 `results/_prereg_lock_v1_epsilon_lu_klm41_register_2026_10_15.md` L71–L76（及 `results/_prereg_lock_v2_h_epsilon_gamma_taucert_u_register_2026_10_15.md` L205 之入锁转录）所载 **`L(M1,T)=3/14·H`** 一值，**自 2026-10-17 起须随附本注记引用**：
> **copilot 回函（`597caf8ba5bc`）论断①「Rejected」之正面冲击已及本值之身份／口径层** —— 该回执明文「Neither is `L(M,T)` for a cell」（L148），将同一闭式辨为**单一采样器之指示器误差率**而非 `spec` 之信息约束极小；**然该回执明文自认算术无误**（「That arithmetic is right」·L148）⇒ **本注记 ⛔0 注销该闭式之算术、⛔0 注销其「仅 4 选 1 且 `value` 二元」之射程限定、⛔0 注销在册 L72／`793986174b23` L72／L151 已载之族差（`T3＝7/29`／`T4＝1/12`）**；**本注记 ⛔0 就该值之「可否继续作为 `L(M1,T)` 之锁值」作任何终判** —— 该面**候另议**（§5-KD-1／KD-3）。
>
> **ERRATUM-314H-02**（连带·论断②）｜在册载有 `U(M,T)=H·τ_cert/[1-(1-γ)^H]` 之任一件（§4-2 之 96 件族），**自 2026-10-17 起须随附本注记引用**：**该式为充分条件、非必要、且所载等式非 iff**（回函 L52／L241／L262／L286；反例 `H=2`·`γ=1/2`·`τ=1/2` ⇒ 公式值 `4/3` vs tight robust total `3/2`·L248／L258）。📌 **本注记 ⛔0 废该式之任一在册数值代入结果**（⛔0 回改原件）、**⛔0 裁其可否继续入判**（§4-3 之 `U` 锁值面逐字并列·⛔0 调和）。
>
> **ERRATUM-314H-03**（连带·论断③）｜在册载有 `structural zero` 登记（`M_2` 之 `L(M2,T)=0`／`D(M2,T) ≡ 0`）之任一件（§4-4 之 33 件族），**自 2026-10-17 起须随附本注记引用**：**该零系 key exposure 之结构性零，非 IC-capacity 下界、非已解之值**（回函 L47／L49／L89／L101）。📌 在册 `a3dd3cc1caf2` L75 已载「`M_2` 仍登记为 `structural zero`」⇒ **本注记与该在册字面一致，⛔0 增改其语义**。

### §3-2 附注引用体例（**⛔0 回改原件之实现方式**）

| 规则 | 内容 |
|:--|:--|
| **R-1 append-only** | 在册件 **⛔0 触动一字**；本注记**另立件承载**，下游引用时以「**该件原文 ＋ 本件 §3-1 注记编号**」并引 |
| **R-2 逐字保留** | 原件之逐字（含 `a3dd3cc1caf2` L72 之「⛔0 将 `3/14` 移用于族外」、L76 之「⛔0 调和之二在册诊断」）**⛔0 软化、⛔0 删除、⛔0 改写** |
| **R-3 判死不软化** | 本件对回函论断之**射程**只作界分（§2-2），**⛔0 使用「但／然而／仍有希望」等软化语** |
| **R-4 注记非判决** | 本注记 **⛔0 充 PI 裁**、**⛔0 充终判**、**⛔0 充核验**；其登记之后果见 §5 |
| **R-5 指纹链** | 下游引用本注记时，**须以本件 SHA-12 之字节级自报为唯一指纹来源**（§6 之自指悖论声明） |

### §3-3 本件效力之界分（🔴 不软化）

- ✅ **本件所及**：①在册 `3/14·H` 载点之**清单与注记**（§1／§3-1）；②回函论断①之**逐字与射程界分**（§2）；③论断②③之**连带登记**（§2-3／§3-1 之 02／03）；④**KD 之如实登记**（§5）。
- 🔴 **本件 ⛔0 所及**：①**回函三重论断之正确性**（⛔0 复算 `3/14`／`4/3`／`3/2`／`11/24`／`7/29`／`1/12` 之任一算术·⛔0 验 `T4` 之 17 组 tuple·⛔0 开卷 `tools/exp_harness.py` 之任一行）⇒ **「正确性已核」⛔0 视为闭**（§5-KD-1）；② `3/14·H` 在册载之**回改／废记／销记**；③`C5-b` 之闭否；④161 件之择读；⑤30 格之任一数值之回填；⑥`C5`／`C5-b`／`G-E01` 任何条件之闭；⑦**grok 回执之实质论断**（§5-KD-5）。

---

## §4 连锁面（**如实列 · ⛔0 代裁**）

### §4-1 派工点名之三面 ｜ 是否以 `3/14·H` 为输入（**本棒三重自审**）

| 面 | 载体（指纹／bytes） | 探针 `3/14` | 探针 `L(M1` | 探针 `3·g_aether`／`7/29`／`1/12` | 探针 `prereg_lock_v1` | **判定** |
|:--|:--|:--|:--|:--|:--|:--|
| **判死面 v1 生效件** | `results/_killface_v1_effect_register_2026_10_16.md`／`98aabe87ae11`／21,872 B | **0** | **0** | **0** | **0** | 🔴 **0 载 `3/14·H`·⛔0 以其为输入**（三重自审：①全文计数 5 探针皆 0；②全仓 `grep` 文件名面 0 命中；③本件名 0 含 `3_14`／`3/14`） |
| **U 轴 ACTIVE 件** | `results/_u_axis_active_ruling_register_2026_10_16.md`／`30fed54c3d09`／22,219 B | **0** | **0** | **0** | **0** | 🔴 **0 载 `3/14·H`·⛔0 以其为输入**（同上三重自审） |
| **1494 面（六件全扫）** | `_ge01_full_1494_exec_2026_10_16.md` `e0efc8501305`／`_ge01_full_1494_exec_r1_2026_10_16.md` `515128a23182`／`_ge01_full_1494_freeze_2026_10_16.md` `171d1b6d5725`／`_ge01_full_1494_resume32_register_2026_10_16.md` `ae4b90375fe7`／`_u_1494_carrier_effect_register_2026_10_16.md` `6f194df09b33`／`_u_domain3_carrier_1494_2026_10_16.md` `59f52f8bb287` | **0 全部** | **0 全部** | **0 全部** | — | 🔴 **0 载 `3/14·H`·⛔0 以其为输入**（六件逐件全扫·非抽样） |

📌 **§4-1 三行结论（供上游一读）**：
1. **判死面 `98aabe87ae11`** ｜ `3/14`＝0／`L(M1`＝0／合并探针＝0 ⇒ **0 载论断①所涉之值，非其输入**。
2. **U 轴 `30fed54c3d09`** ｜ 同 ＝ 0/0/0 ⇒ **0 载论断①所涉之值**；然 **载论断②之对象**：`τ_cert` 命中 **2 行**（L59「`γ`＝`τ_cert`＝`1/10` **已入锁**」／L108「**route-乙 三前置齐备**」）⇒ **论断② 之连锁于该面成立（作为前置条件之载，非 iff 之载）**。
3. **1494 面六件** ｜ 全部 **0 载 `3/14·H`**；然 **载论断②之参数**：`γ`／`τ_cert`＝`1/10` 之冻结逐字在 `_ge01_full_1494_freeze_2026_10_16.md` L153 ⇒ **论断② 之连锁于该面成立（参数层）**；📌 **该六件 0 载 Route 乙 反例值 `4/3`**（§4-3 之假阳性辨）。

### §4-2 论断②「充分非 iff」之连锁面（**96 件 · ⛔0 逐件代裁**）

- **实测范围**：`results/`＋`letters/`＋`docs/` 全递归，逐行探针 `U(M,T)` ∪ `U(M1,T)` ∪ `τ_cert` ⇒ **命中 494 行／96 件**。
- 📌 **本件 ⛔0 逐件列**（494 行逐行转录超出本件射程·⛔0 断言之）⇒ **以家族计数交付之**（完整清单可据 §5-KD-4 候采集）。
- **载点密度最高之 12 件**（供上游优先核）：

| 件 | 命中行数 | 指纹／bytes |
|:--|:--|:--|
| `results/_prereg_lock_v2_h_epsilon_gamma_taucert_u_register_2026_10_15.md` | 26 | `4c782fc8566b`／33,312 B |
| `results/_d1_ab_deliberation_judgment_2026_10_15.md` | 23 | `88c2af72ff7b`／46,542 B |
| `results/_ge01_launch_gate_recheck_2026_10_17.md` | 20 | — |
| `results/_three_seed_measurement_exec_2026_10_16.md` | 20 | `0e0716fde41f`／48,178 B |
| `results/_t3trap_kd3_bprime_effect_register_2026_10_15.md` | 20 | — |
| `results/_gamma_taucert_sourcing_2026_10_15.md` | 36 | `6630447e5ec7`／34,667 B |
| `results/_resume32_adoption_and_flip_register_2026_10_16.md` | 14 | — |
| `results/_t3trap_kd3_disposition_deliberation_2026_10_15.md` | 14 | — |
| `results/_prereg_lock_v2a_t5_completion_register_2026_10_15.md` | 11 | — |
| `results/_d1_c_effect_register_2026_10_15.md` | 11 | — |
| `results/_t3trap_answerable_build_exec_2026_10_15.md` | 11 | — |
| `results/_killface_v1_effect_register_2026_10_16.md` | 1（`U-戊`／`D≡0`·L110） | `98aabe87ae11`／21,872 B |

### §4-3 判死面 `98aabe87ae11` 之「`U` 必要非充分」语汇（**⚠ 与论断② 语汇同族·靶不同·⛔0 混同**）

| 判读项 | 实测逐字 |
|:--|:--|
| **在册载语** | L82「…且 **`U` 必要非充分**——`U` 轴之 `ACTIVE` 尚须 route-乙 三前置齐备…」／L88「…② **`U` 必要非充分**；…」／L91「…＋「`U` **必要非充分**」⇒ **v1 生效 ⇏ 判死线已闭 ⇏ 可开跑**。」 |
| **回函论语汇** | L52「the displayed equality is **not an iff**」／L262「It is **sufficient** … It is **not necessary**」 |
| 🔴 **判定（⛔0 调和）** | 二者**语汇同族（充分／必要之逻辑修饰语）而靶不同**：在册 L82/88/91 所论 ＝ **「`U`（作判死轨之门槛）必要非充分」**；回函 L52/262 所论 ＝ **「Route 乙 闭式（作 tolerance 之式）充分而非必要、且非 iff」** ⇒ 🔴 **⛔0 断言二者同义**、**⛔0 以在册「必要非充分」充回函之拒已被在册预置**。📌 **二者可并存而不相消**（如 `a3dd3cc1caf2` L76 体例：「并存不调和照录」） |

### §4-4 论断③「structural zero ／ `M2` `D≡0`」之连锁面（**33 件**）

- **实测范围**：同 §4-2 通道，探针 `structural zero` ∪ `结构性 zero` ∪ `结构零` ∪ `D(M2…≡0` ∪ `D≡0` ⇒ **命中 99 行／33 件**。
- 📌 **关键载点（逐字）**：

| 件 | 行号 | 逐字 | 指纹 |
|:--|:--|:--|:--|
| `results/_prereg_lock_v1_epsilon_lu_klm41_register_2026_10_15.md` | **L75** | 「\| **射程附记（照录不动）** \| `M_2` 仍登记为 `structural zero`（`L(M2,T)=0`）；`M_3` 仍登记为无信息边界（`3H/4` **仅** sanity check · ⛔0 充 `L` 或 `U`） \|」 | `a3dd3cc1caf2` |
| `results/_killface_v1_effect_register_2026_10_16.md` | **L110** | 「\| **`K-D-4`** \| **`U-戊` 登记值可否入判**… \| `U-戊` 之 `U` 为登记而非赋值（**`D≡0` ⇒ 任意 `U` 成立**）… \| 🔴 **未成就·仍候裁**」 | `98aabe87ae11` |
| `results/_u_1494_carrier_effect_register_2026_10_16.md` | **L111** | 「…**`T1_GSM8K` 之 `U` 在两域皆为 `U-戊`（登记值而非可识别值）**…`D≡0` ⇒ 证书于 `T1` 面对任意 `τ_cert` 自动成立 ⇒「**`U-戊` 登记而非赋值**」」 | `6f194df09b33` |
| `results/_u_domain3_carrier_1494_2026_10_16.md` | **L14／L118** | L14「…本件所增者非新数字而为新承载（新登记面与新出处）。**本件 ⛔0 择域、⛔0 宣告该值可入判死轨**…」／L118「\| **承载之对象** \| **`1494` 面**…**之判死轨之 `U` 供值** \|」 | `59f52f8bb287` |

📌 **结论**：论断③ 之实体在册**已为逐格登记语言**（`U-戊`「登记而非赋值」·`D≡0` ⇒ 任意 `U` 成立）⇒ 🔴 **本注记 `ERRATUM-314H-03` 与在册语义一致，⛔0 增改、⛔0 撤销在册任一登记**。

### §4-5 ⚠ 假阳性之同名面（**⛔0 误植防御 · 本棒实测所得**）

> 📌 **本节为防下游误植而设**：`_ge01_full_1494_*` 六件之朴素字符串探针 `4/3` 合计命中 **58 次**，然**边界正则**（`(?<![0-9])4/3`）复核后，其中 **`34/33` 之子串**（`H` 元组 `34/33/33/33/33`）占绝大多数，**且** `_ge01_full_1494_exec_r1`（朴素 21／边界 12）与 `_ge01_full_1494_resume32_register`（朴素 19／边界 12）之边界命中**逐行实测为 `4/33`**（`T3_Trap` 比率列·L125／L130／L135／L140 等）⇒

| 件 | 朴素 `4/3` | 边界 `4/3` | `34/33` | 边界命中之实字 |
|:--|:--|:--|:--|:--|
| `_ge01_full_1494_exec_2026_10_16.md` | 6 | **0** | 6 | —（全为 `34/33`） |
| `_ge01_full_1494_exec_r1_2026_10_16.md` | 21 | 12 | 2 | **`4/33`**（`T3_Trap` 比率） |
| `_ge01_full_1494_freeze_2026_10_16.md` | 1 | **0** | 1 | —（全为 `34/33`） |
| `_ge01_full_1494_resume32_register_2026_10_16.md` | 19 | 12 | 0 | **`4/33`** |
| `_u_1494_carrier_effect_register_2026_10_16.md` | 3 | **0** | 3 | —（全为 `34/33`） |
| `_u_domain3_carrier_1494_2026_10_16.md` | 8 | **0** | 8 | —（全为 `34/33`） |
| `_killface_v1_effect_register_2026_10_16.md` | 1 | **0** | 1 | —（全为 `34/33`） |
| `_u_axis_active_ruling_register_2026_10_16.md` | 0 | **0** | 0 | — |

🔴 **结论**：**1494 面六件 ＋ 判死面 ＋ U 轴 ⇒ Route 乙 反例值 `4/3` 之真字命中 ＝ 0 行**（`iff` 语汇亦 ＝ 0 行·八件全扫）⇒ **⛔0 断言该八件已载回函之反例**；📌 反之，**该八件亦 0 载 `3/14·H`**（§4-1）⇒ **两论断于该八面皆无载点**。

---

## §5 KD（如实交代 · 不软化 · 0 编造）

| # | KD | 实测事实 | ⛔0 之处置 |
|:--|:--|:--|:--|
| **KD-1** | 🔴 **回函三重论断之正确性·独立核验未做（采认射程外）** | PI 所择档 `description` 逐字**限于**「交付采认」与「另立勘误面」两项，**⛔0 载「论断经核验属实」之义**（`4a89f8d3ddda` §2-KD-1 逐字同）⇒ 📌 **本棒 0 复算**（`3/14`／`4/3`／`3/2`／`11/24`／`7/29`／`1/12` 之任一算术）·**0 验** `T4` 之 17 组 tuple·**0 开卷** `tools/exp_harness.py` 之任一行 | 🔴 **⛔0 以本裁或本件充正确性已核**；**候另议**（PI 未择 `opt3`「另议（核验判断件）」⇒ ⛔0 视为该径已被采；**正确性面 ⛔0 视为闭**） |
| **KD-2** | 🔴 **派工单所载采认落档件指纹与实测不符** | 派工单载 `results/_copilot_reply_adoption_effect_2026_10_17.md` 之 SHA-12 ＝ **`dc4b450b2878`**；📌 **本棒实测该件现值 ＝ `4a89f8d3ddda`／39,705 B**，且**全仓递归（所有扩展名·0 排除 `.git`）0 命中／0 件**，文件名面 `glob` 亦 0 命中 ⇒ **该指纹在盘无正身** | 🔴 **⛔0 以实测值覆盖派工单之值**、**⛔0 断言派工单有误**；**两者并列登记**（§0-1 ②）。**成因待查**（**0 断言**系他棒改写、系版本差、系误抄）⇒ **候上游复核** |
| **KD-3** | 🔴 **参数冻结面之冲突未裁（`ERRATUM-314H-01` 未闭合面）** | §2-2 之 B-2：在册 `a3dd3cc1caf2` L73 载「**经本卡裁转 prereg 冻结值**」／`ac3b580defbb` L29 载「**经本裁转为 prereg 冻结值**」；回函 `597caf8ba5bc` L48 载「constructor defaults, **not frozen values**」 | 🔴 **⛔0 调和、⛔0 择一**、**⛔0 代裁**（层次不同：代码层 vs prereg 治理层）⇒ **候另议** |
| **KD-4** | ⚠ **论断②／③ 之 96 件／33 件连锁面未逐件逐行转录** | §4-2（494 行／96 件）与 §4-4（99 行／33 件）仅交付**家族计数＋高密度前 12 件＋关键逐字锚** | 📌 **⛔0 断言已全量逐行登记**；**全量清单候采集**（**本件 ⛔0 虚构清单**） |
| **KD-5** | ⚠ **grok 回执未至** | `letters/_commission_t2_t3_theory_inputs_grok_2026_10_17.md`（`6922929bfda8`·23,906 B）**在盘者为委托函（commission）·非回执**；📌 **本棒 0 见 grok 回执正文** | 🔴 **⛔0 以 copilot 回函论断代 grok 之面**、**⛔0 断言 grok 结论与 copilot 同或不同** |
| **KD-6** | ⚠ **`.tmp/` 通道 0 纳入** | 本棒扫描**⛔0 排除 `.tmp/`**（含他棒写盘脚本 `dw55_w_v55.py` `6d474cc82852`／`dw55_w_adopt.py` `72c172c18cd0` 等）⇒ 📌 该通道另有 `3/14` 命中（其内容多为**本棒族之写盘脚本自载之卡面/条文字面**） | 📌 **⛔0 断言「全仓 3/14 仅 90 行」**；**断言范围 ＝ §1 探针口径**（0 排除 `.tmp`·含 `reviews`／`verifier`／仓根） |
| **KD-7** | ⚠ **回函本体含 CRLF** | `597caf8ba5bc` 实测 **CRLF ＝ 318 处**（30,459 B·BOM=no）⇒ 📌 **其行号锚以 `ReadAllLines` 之逻辑行为准**，⚠ **跨工具读之物理行位可能偏移** | 📌 本件 ⛔0 归咎于该件；**行号锚已随本件登记**（§2-1／§2-3） |
| **KD-8** | ⚠ **本件 ⛔0 自指其指纹** | 本件自身 SHA-12 **⛔0 可能出现在其自身正文内**（自指悖论）⇒ 指纹**唯一登记处 ＝ 落盘后字节级自报**（§6） | 🔴 **⛔0 读作「该件不存在」**、**⛔0 以他件代本件指纹** |
| **KD-9** | ⚠ **判死面／U 轴 之 0 命中系全文件扫描所得** | §4-1 之 0 命中由**全文 `ReadAllText` 正则计数**所得（5 探针 × 8 件）⇒ 📌 **非抽样**；⚠ 然 **⛔0 及于他棒／他会话之盘面** | — |

---

## §6 落盘自核节

| 项 | 内容 |
|:--|:--|
| **落盘通道** | Python 3.14.7 · `io.open(..., 'w', encoding='utf-8', newline='\n')` · **UTF-8 无 BOM · 纯 LF** |
| **落前检查（实测）** | `Test-Path` ＝ `False`；`results/` 内 `erratum`×`3_14` `glob` 命中 ＝ `0` ⇒ **⛔0 启用 `_r1`** |
| **落盘后自检（复算式）** | `sha256(bytes)[:12]` ＝ SHA-12；`len(bytes)` ＝ bytes；`bytes[:3]==EF BB BF` ＝ BOM 判定；`count(b'\r\n')` ＝ CRLF 计数；`count(codecs.decode(bytes,'utf-8','replace') 中之 U+FFFD 码位)` ＝ U+FFFD 计数（📌 **本行 ⛔0 内嵌真实 U+FFFD 字符**·改以码位名记述·否则自检永不为 0） |
| **落盘环之内环修正（如实登记）** | ⚠ **本件经两段落盘**：① 首落 `d799eebec764`／40,547 B 自检得 **U+FFFD ＝ 3**（L68 逐字误植 1 处 ＋ L275 自检式内嵌真实 U+FFFD 字符 1 处·计 3 码位）；② 本棒**即于本件自身**修正后重落（本件为**新建**件·落前 `Test-Path=False`·**⛔0 属「在册件之回改」**）。📌 **该首落指纹 `d799eebec764` 作废、不再有效**；**⛔0 视为历史上曾存在之一在册版本** |

| **本件自身指纹之登记处** | 🔴 **本件正文 ⛔0 载其自身 SHA-12**（自指悖论·KD-8）⇒ **唯一指纹来源 ＝ 落盘后之字节级自报（随派工回报交付）**。⚠ **⛔0 读作「该件不存在」**、**⛔0 以任何他件之值代本件指纹** |
| **append-only 自证** | 本棒**未对任何在册件执行写入**（`ReadAllText`／`ReadAllBytes`／`Get-FileHash` 皆为只读）⇒ **⛔0 触动在册件一字**；本件为**新建**（落前 `Test-Path=False`） |

---

**件末** ｜ `ERRATUM-314H` ｜ 生成者 `doc-writer`（agent-0032834a3e04）｜ 2026-10-17 ｜ **append-only·⛔0 回改·⛔0 代裁·⛔0 编造**
