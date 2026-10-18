# gemini4 回函 · 核验登记件（证据链审计 · **候 PI 裁 · ⛔ 0 采认**）

> **件性质**：**核验登记件**（evidence-chain audit register）——对 `letters/REPLY_FROM_GEMINI4_GE01_THEORY_INPUTS_2026_10_15.md` 之代码／公式／条款主张**逐条**与本仓实体核对。
> ⛔ **本件 0 采认任何回函值**（采认面属 PI）｜⛔ **0 代 PI 裁**｜⛔ **0 回填任何锚／给值单**｜⛔ **0 回改任何既有件**｜⛔ **0 调和任何冲突**（冲突并列载明）。
> **审计官**：`evidence-auditor`｜**件日**：2026-10-15｜**棒别**：数据修订／资产处置（worker「数据修订/资产处置」之证据链审计面）

---

## §0 对象正身与本件自报

| 面 | 值 |
| :-- | :-- |
| 核验对象 | `letters/REPLY_FROM_GEMINI4_GE01_THEORY_INPUTS_2026_10_15.md` |
| 对象 SHA-12／bytes | **`44311ade19de`**／**44,520 B**（本审计 2026-10-15 实测 ＝ parent 实测值，**MATCH**） |
| 对象 CR／BOM | CR＝0／BOM＝False（本审计实测） |
| 委托稿 | `letters/LETTER_TO_GEMINI4_GE01_THEORY_INPUTS_2026_10_15.md`＝`70fe266e87d6`／8,361 B／75 行（回函自报值 ＝ 本审计实测值，**MATCH**） |
| 本件标注 | **核验登记 · 候 PI 裁 · ⛔ 0 采认** |

---

## §1 核验方法（仪器自审：测量仪器自身即误差源）

**读件清单（皆本审计逐字节实测 SHA-256 前 12 位／bytes）**：

| # | 件（repo 相对路径） | SHA-12 | bytes |
| :-: | :-- | :-- | --: |
| 1 | `letters/REPLY_FROM_GEMINI4_GE01_THEORY_INPUTS_2026_10_15.md` | `44311ade19de` | 44,520 |
| 2 | `letters/LETTER_TO_GEMINI4_GE01_THEORY_INPUTS_2026_10_15.md` | `70fe266e87d6` | 8,361 |
| 3 | `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | `423c84de20d5` | 15,457 |
| 4 | `tools/exp_harness.py` | `275e480ba4d9` | 10,090 |
| 5 | `tools/distortion_calculator.py` | `410a12482eef` | 40,611 |
| 6 | `results/_m41_double_readout_contrast_exec_2026_10_15.md`（M-41 执行件） | `b9feb5df8d44` | 23,855 |
| 7 | `results/_m41_verdict_kd_effect_register_2026_10_15.md` | 在盘（§2 逐条引） | — |
| 8 | `results/_t2_t3_value_sourcing_2026_10_15.md`（T-2／T-3 取值件） | `bcb0d60fdd2d` | 24,658 |
| 9 | `results/_t2_t3_value_request_form_2026_10_14.md`（给值单） | `21abb5173b87` | 15,054 |
| 10 | `results/_ge01_prereg_seven_requirements_draft_2026_10_13.md`（prereg 七要件） | `0a031a9795a9` | 39,337 |
| 11 | `results/_ge01_calculator_rebuild_design_2026_10_14.md` | `8ab699f017c8` | 46,007 |
| 12 | `letters/_codex_c4_values_unblock_reply_2026_10_10.md` | `a975c7990cd8` | — |
| 13 | `results/_kt_a1_anchor_drift_root_cause_2026_10_14.md`（锚漂移根因件） | 见 §10 | — |
| 14 | `docs/V3X/KT_A1_SPEC_V0.1.md`／`docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` | 在盘（§9／§10 引） | — |

**方法**：`read` 逐行读＋`grep` 定位＋`hashlib.sha256` 全文指纹（**⛔ 0 用内建 `hash()`**）＋**Python `Fraction` 精确复算**（非浮点近似）＋`os.path.exists` 三处路径对账。
**0 写既有件**；0 实验、0 判 verdict、0 联网、0 读 `.env`／key、0 上传。

---

## §2 面① · 代码主张核验（逐条·C1–C10）

| # | 回函主张（回函行号） | 本仓实测证据 | 判定 |
| :-: | :-- | :-- | :-: |
| **C1** | `T3_Trap` prompt 形态＝`"Trap scenario {i+1} (type={trap}). Which option?"`＋`options=['Option A','Option B']`（回函 :160/:174–179） | `tools/exp_harness.py:199` prompt f-string **逐字相符**；`:195` `options = ['Option A', 'Option B']` **逐字相符** | ✅ **相符** |
| **C2** | `random.shuffle(options)` 位于 T3 之「L195–196」三行块（回函 :174–179） | 实测：`:195` options、`:196` correct、**`:197` shuffle** ⇒ 回函所引区间**未含 shuffle 行**（差 1）。附：在册取值件 §3-3（L133）亦记 T3 shuffle 为「:196」⇒ **仓内既有件同差 1**（⛔ 0 推测成因） | 🔴 **不符**（行位差 1；**文本引述本体相符**） |
| **C3** | T2 之 `options`＋`shuffle` 位于「L175–176」（回函 :180–184） | 实测：`:174` `options = ['Yes','No','Maybe','Always']`、**`:175` shuffle** ⇒ 差 1 | 🔴 **不符**（行位差 1） |
| **C4** | 回函 0 对 T4 之 shuffle 作断言（**实测补强**：`Matrix2x2Task` 内 **0 shuffle**） | `exp_harness.py:213–231` 内 `random.shuffle` **0 命中** ⇒ 选项序恒 `['Cooperate','Defect']`；全仓 `random.shuffle` 仅 `:148`／`:175`／`:197` 三处。旁证：取值件 §3-3 L133 实测计数 `[0,1800]`、χ²＝1800 ⇒ **构造性退化在册** | ✅ **相符**（回函未相反断言；实测确认 T4 无 shuffle） |
| **C5** | `value` 逐族编码 correct（T1/T2/T3/T4）引「L153／L180／L202／L229」（回函 :159） | 实测 `:153`／`:180`／`:202`／`:229` —— **四行行位全对**；`KD-1`（执行件 :250／登记件 :97）同引四行亦逐位一致。**附注（实测强于回函）**：`:202` T3 之诱饵值＝**`0.5`（非 0）**，故 T3 之 value 非二元 1/0（影响 F3 之 3/14 射程） | ✅ **相符**（行位全对）＋附注 |
| **C6** | `M2_Greedy`（L97–100）取 `argmax_o value[o]` ⇒ `R_base ≡ 0` | 实测 `GreedyMechanism.choose`＝**`:103–108`**（`:108` `return max(options, key=lambda o: values.get(o, 0))`）；`:97` 实为 `return 'M1_Deposon_TRA'`（M1 之 `name`）。**本体相符**：执行件 L250／登记件 L97 实测 `M2_Greedy` **60/60 全对**、`R_base ≡ 0` | 🔴 **不符**（行位错；**本体相符**） |
| **C7** | `DeposonMechanism.choose`(L75) 与 `GreedyMechanism.choose`(L97) 直读 `context.get('value', {})`（回函 :91） | 实测：M1 value 读＝**`:73`**（权重合成 `:78–84`）、M2＝**`:105–108`**；`:75` 实为 `return random.choice(options)`（无先验退化支路）、`:97` 实为 M1 `name`。**对照**：给值单 L74 自引「`:73–:84`／`:105–:108`」＝ 与本审计实测一致 | 🔴 **不符**（行位错；**「直读 value ⇒ 全信息」本体相符**） |
| **C8** | `RandomMechanism.choose`(L108) 忽略 `context`、强制均匀（回函 :95） | 实测＝**`:117–118`**（`:118` `return random.choice(options)`）；`:108` 实为 M2 之 `return max(...)`。**本体相符** | 🔴 **不符**（行位错；本体相符） |
| **C9** | `context` ＝「the full task dictionary `p`」（回函 :91） | 实测 `:257` `decision = mech.choose(p['options'], p)` ⇒ context＝**整个 `p`**。**实测强于回函**：`p` 除 `'value'` 外**另含 `'correct'` 真值键**（`:152`／`:179`／`:201`／`:228`）⇒ oracle 暴露面比回函所述更宽 | ✅ **相符**（回函所述为实测之真子集；如实登记「实测更强」） |
| **C10** | 三机制＋各 prompt **strictly memoryless** across t（回函 :122） | 实测 `run()` `:250–267` 逐 `p` 独立调 `choose`，**0 跨 t 状态传递** ⇒ memoryless ✅；M-41 实测 60 cell／50 有效／10 no-action 全落 `T3_Trap`（执行件 L172–176、L251） | ✅ **相符** |

**面① 小计：相符 5／不符 5**（不符 5 项**全部为「行位引用」面**；其**实体性主张经实测全部成立** ⇒ 判「引用面缺陷·非主张面缺陷」）。

---

## §3 面② · 公式主张核验（F1–F12）

| # | 回函主张（回函行号） | 本仓实测证据（`Fraction` 精确复算／源码） | 判定 |
| :-: | :-- | :-- | :-: |
| **F1** | `mult = D_LLM/max(D_Bayesian, c·ε*)`；因 `D_Bayesian ≡ 0` ⇒ 分母**恒为** `c·ε*`（守护支路）（回函 :31–34） | `distortion_calculator.py:305–321` `guarded_denominator`：`g_b >= cc*e` → `return g_b`，否则 `return cc*e`；`:343–356` `distortion_multiplier` 文档串 L349–350 逐字「spec L12: `D_Bayesian ≡ 0` ⇒ 分母恒为 `c*eps`」；spec `:12` 逐字「已知机制 + 支付 → 失真 = 0」 | ✅ **相符** |
| **F2** | `kill_decision` 三档：`FAIL_H0` ≥2.0 或 U≥0.3／`PASS_H1` ≤1.5 且 ci_hi≤1.8 且 U≤0.1／`GRAY`（回函 :37–39） | `distortion_calculator.py:419–440` **逐字**；spec `:103–110` **逐字** ⇒ 两面互证 | ✅ **相符** |
| **F3** | `L(M1,T) = 3g_aether/[(1−η)+ηg_couple+4g_aether]·H = 3/14·H ≈ 0.2143H`（回函 :112/:255） | **算术相符**：参数默认值实测 `exp_harness.py:56`（`eta=0.5, g_couple=1.0, g_aether=0.1`）、权重式 `:84` `(1−η)t + η·g_couple·r + a`；本审计 `Fraction` 复算 w\*＝1.1、w₀＝0.1、W＝1.4 ⇒ 3w₀/W ＝ **3/14** ✅；量纲与 `distortion_indicator:248–249`（`D ∈ [0,H]` 计数）一致 ✅。**射程不符**：该闭式**仅**对「4 选 1 且 value 二元」族成立；本审计复算 T3（诱饵 0.5）＝**7/29**、T4（2 选 1 二元）＝**1/12**。回函 §2.1(c)（:111）自身限定「for a symmetric 4-choice task」，但 **T2 终判（:145）与 §5 汇总（:255）去限定表述** | 🔴 **不符**（算术相符·**表述射程过宽**） |
| **F4** | 3/14 推导所用参数＝「for default η=0.5, g_couple=1.0, g_aether=0.1」（回函 :111） | 实测确为构造函数默认值（`:56`）。**在册限定语未被携带**：给值单 **`:107`**「为**默认值**（⛔ 默认值 ≠ 冻结值）」／**`:120`** 反方丁「为**构造函数默认值**（`:56`）**非 prereg 冻结值** ⇒ **须 PI 冻结**」；取值件 `C-P2` 同 | 🔴 **不符**（缺在册限定语；3/14 成立于**未冻结**前提） |
| **F5** | `Π_adm`＝4^4＝256 之观测→动作映射；`π*(z)=z` 为最优（回函 :110–112） | 算术：`|A^A| = 4^4 = 256` ✅；最优性：按类别权重采样下 `w*＝1.1 > w₀＝0.1` ⇒ 众数即正确项 ✅。**未并列之在册事实**：取值件 §3-4（L154–164）／`S-5` 登记「`Π_fin` 之『最优』**恒等于多数标签率**」为**决定性诊断**，并据此判「预实验择优所得之值⛔ 0 采为 `L`」 | ✅ **相符**（算术·最优性）｜张力面见 **X2** |
| **F6** | `U(M,T) = H·τ_cert/[1−(1−γ)^H]`，证书 `E[S̄_H] ≤ τ_cert`（回函 :132–139） | **形式相容 ✅**：本审计复算（H=15/γ=1/2、H=25/γ=1/10、H=33/γ=1/4）最坏位错置之 `E[S̄_H] ≤ D·(1−(1−γ)^H)/H`，反解得同式；`1−(1−γ)^H < 1` ⇒ `U ≥ D`，与回函 :239 之 `0 ≤ L ≤ D ≤ U ≤ H` 相容 ✅ | ✅ **相符** |
| **F7** | `ε*(H)=H/10`（率尺度 1/10）；未标度 `ε*=0.1` 于**计数尺度** ⇒ 单次错误即 `mult = 1/0.1 = 10.0 ≥ 2.0` ⇒ `FAIL_H0`（回函 :43–51） | 量纲论成立（`distortion_indicator:248`「D 之量纲 = 计数」）✅；**精确复算**：`D=1, ε=1/10` ⇒ `mult = 10.0` ✅；`D=3/2, ε=1/10` ⇒ `15.0` ✅（回函 :47）；`ε*(15)=3/2` ⇒ `mult = 1.0` ✅（回函 :75）；且与 `:305–321` 守护式（`G_B=0, c=1` ⇒ 分母＝`ε`）**一致** ✅ | ✅ **相符**（算术·量纲·守护式三合） |
| **F8** | `ε*(H)` 之 prereg 地位（回函 :56–61） | **移入 X1 判**（与在册口径④不相容） | — |
| **F9** | §1.4 敏感度表与失效模式（回函 :70–78） | **复算全过**：`mult = R̄/r0`；FAIL ⟺ `r0 ≤ R̄/2` ✅；PASS ⟺ `r0 ≥ (2/3)R̄` ✅；CI 界 ⟺ `r0 ≥ (5/9)CI_hi`（`1/1.8 = 5/9`）✅；M-41 列 `r0=0.10` ⇒ `mult=1.0` ⇒ PASS（若 `CI_hi(R) ≤ 0.18`）✅；随机基线 vacuous pass 阈 `r0 > 3/8`、`r0 ≥ 1/2` 时随机过 PASS（`0.75/0.5 = 1.5`）✅；粒度下限 `ε*(H) ≥ 2/3`（`H/10 ≥ 1.5` for `H ≥ 15`）✅ | ✅ **相符** |
| **F10** | BL-5 功效现实检验：`1/45≈0.0222`、`1/60≈0.0167`、`sqrt(0.1·0.9/135)≈0.0258`、±`0.0506`；单格翻转 > `|ΔR| ≤ 0.0143`（回函 :197） | 本审计复算：`0.02222`／`0.01667`／`0.02582`／`0.05061`；`0.0222 > 0.0143` ✅ | ✅ **相符** |
| **F11** | `U = null-U` ⇒ `theory_U_hit_rate` 为 `None` ⇒ **阻塞** `kill_decision`（回函 :241） | 本审计实测：`None >= 0.3` ⇒ `TypeError: '>=' not supported between instances of 'NoneType' and 'float'` ⇒ **确阻塞** ✅（对照 `:419` 之 `theory_U_hit_rate >= 0.3`） | ✅ **相符** |
| **F12** | 二元接受键计分下 `u*_t = 1`、`max_u = 1` ⇒ `distortion_gapwise` 与 `distortion_indicator` **algebraically identical**（回函 :219–225） | 恒等式本体 ✅：prereg §6 ①（L170）／②（L171）逐字定义；仓内孪生件 `letters/_codex_c4_values_unblock_reply_2026_10_10.md:31–33` 逐字供给同一约定 ✅。**但登记状态缺注**：`distortion_calculator.py:272`「两口径**未择定**（KD-1/D）」；`:280–281`「本式与口径 ① 逐项均为 {0,1}（量纲同构之**推断，候 PI 核准**）；两族并存之**择定权属 PI**」 | 🔴 **不符**（恒等式相符·**在册「候 PI 核准／择定权属 PI」未携**） |

**面② 小计：相符 8／不符 3**（F8 已并入 X1 计）。

---

## §4 面③ · 条款面核验（M1–M3）

| # | 条款 | 回函所述 | 本仓实测 | 判定 |
| :-: | :-- | :-- | :-- | :-: |
| **M1** | 委托稿 §2.3（L18）「State the exact model (name/version)」＋§7.2（L66）「Exact model name/version used, and any tool calls made」 | 回函 §0（L8–15）注明「Addressee on commission header: Gemini 4」「I am an AI assistant using **Copilot SDK in VS Code**」「**Exact serving model/version string: Unavailable** to this assistant runtime」；§5 项 7（L266）再自认「Exact serving model/build identifier … **not exposed**」 | **条款要件未满足**：①「exact model/version」字符串 **0 给出**（自称不可得）；②**主体同一性未自证**——仅复述委托抬头，**未确认自身即 Gemini 4**；③工具调用三则（read-only view/grep、1 次本地 `hashlib.sha256`、1 次 create）**已列** ✅。**exact model 面之复核者**＝ 0 逐条复核 | 🔴 **部分不符**（要件未满足且自认）＋模型面**不可核** |
| **M2** | 委托稿 §7.5（L69）「do not execute, modify, or upload anything」 | 回函 §0（L4/:20）声明「0 project code files modified, 0 experiments executed, 0 uploads performed」 | 盘上 **0** 该运行时之 transcript／审计日志 ⇒ 该过程性声明**0 独立证据**可核 | ⚪ **不可核**（自述·0 独立证据） |
| **M3** | 委托稿 §2.1–2.5（五项 standing constraints） | 回函逐条以层级／量纲／反退化标注作答 | 逐条实测相符：①kill-lines 先冻（回函以「derivable-with-relaxation」分列 0 偷改阈值 ✅）；②可复现（给推导非仅结论 ✅）；③model 披露（见 M1 ⚠）；④量纲纪律（§2.2 U-3、§1.2 计数/率尺度 ✅）；⑤反退化（M1/M2 之 10/15 **结构零登记为 structural zero**（回函 :92–93）＝ 在册 `L-戊 ①`（给值单 L54）✅；`3H/4` 仅作 sanity check ✅ ＝ 在册 `S-2`（取值件 L198）✅） | ✅ **相符**（除 M1 之 model 项） |

**面③ 小计：相符 1／不符 1／不可核 1**。

---

## §5 面④ · 冲突面（与在册事实之冲突 · **并列载明 · ⛔ 0 调和**）

| # | 回函所述 | 在册事实（实测出处） | 并列判定 |
| :-: | :-- | :-- | :-: |
| **X1** | **推荐 `ε*(H) = H/10`**（随 H 线性变；率尺度 1/10）（回函 :56–61/:80） | ① **prereg `0a031a9795a9` §6④（L173）逐字**：「`ε` 于 prereg 固定（**须 PI 另给 · ⛔ 0 代给**）；草拟约束：**单一标量常数、不随格变/不随 t 变**」；② `H` 之精确值本身 **0 锁**：「`H` 之精确值 ＝ **须 PI 另给**（无盘上精确候选）」（prereg L160）、给值单 `B-P2`／`PI-2`（取值件 L209）同；③ `ε` 值 **0 固定** ⇒ 失真倍数**不可算**（`KD-5`，登记件 L101） | 🔴 **冲突并存**：`ε*(H)` 随 `H` 变 ⇔ 「不随格变」之字面不相容；且 `H` 未锁 ⇒ 该式**当前无确定值**。⛔ **0 调和**；**须 PI 先裁「口径④ vs H 依赖式」** |
| **X2** | `L(M1,T) = 3/14·H` 于 T2 终判／§5 汇总中**去限定**表述（回函 :145/:255） | ① 在册 **`S-4`**：T4 之观测律为**构造性退化**（无 shuffle）⇒「其 `L` 之任何 0 值均为**构造伪影**」（取值件 L200／§3-3 L131–133）；② 在册 **`S-5`**：`Π_fin`「最优」恒等于多数标签率 ⇒「预实验择优所得之值⛔ 0 采为 `L`」（取值件 L201／§3-4）；③ 在册 `S-1`：「⛔ **0 采任何 `L`／`U` 数值**」（取值件 L197） | 🔴 **冲突并存**：回函之 3/14 未携 T4 退化与 `Π_fin` 伪影二诊断；于 T3（7/29）／T4（1/12）不成立。⛔ 0 调和 |
| **X3** | 3/14 之参数（η/g_couple/g_aether） | 给值单 **`:107`／`:120`**（默认值 ≠ 冻结值 · **须 PI 冻结**）；取值件 `C-P2`（`:104`）同 | 🔴 **冲突并存**：回函 0 携「未冻结·须 PI 冻结」限定 ⇒ 其值成立**以未冻结参数为条件** |
| **X4** | §5 参考 4 之 **7 段行位区间**（回函 :263） | 实测：`DeposonMechanism.choose`＝`:61–94`（回函 `L62–89`）／`GreedyMechanism.choose`＝`:103–108`（回函 `L97–101`）／`RandomMechanism.choose`＝`:117–118`（回函 `L108–109`）／`GSM8KTask`＝`:136–158`（回函 `L136–157`）／`StrategyQATask`＝`:161–185`（回函 `L163–184`）／`TrapTask`＝`:188–207`（回函 `L190–206`）／`Matrix2x2Task`＝`:210–234`（回函 `L212–233`）⇒ **7/7 段**与盘上实体不符 | 🔴 **不符**（行位引用面；**成因不可核**——回函 0 述其所据副本，⛔ 0 推测） |
| **X5** | §5 参考 6 引用**仓外绝对路径** `c:\Users\Administrator\codex-workspace\c4_values_reply_2026_10_10\_codex_c4_values_unblock_reply_2026_10_10.md`（回函 :265） | 实测：该仓外路径**实存**，且与仓内 `letters/_codex_c4_values_unblock_reply_2026_10_10.md` **SHA-12 同为 `a975c7990cd8`** ⇒ **SAME_IDENTITY**；亦见 §0 工具面所列 `_draft.md` 与 `_dispatch.md` 同哈希 `70fe266e87d6` ⇒ 亦 **SAME_IDENTITY** | 🟡 **引用可解析（非缺件）**＋**资产缺陷登记**：仓外绝对路径依赖 ⇒ 应改采仓内相对路径（防路径迁移致登记断链） |
| **X6** | Route-丙 之判：「跨协议量纲/域不匹配 ⇒ U-3／U-5 下不可解」；证书源述作「22-concept-graph game（`v20_gt`/`v21_gtformal`）」（回函 :141–143） | 在册 **与回函结论一致** ✅：`KD-C2`「`bd1caab42b4c` §3.4 之 ε-纳什／50 轮属 **P-A** 博弈策略迭代状态过程，≠ P-B 之分类采样/扩散 ⇒ **跨协议**」；`KD-C3`「`D`（被拒计数）与 ε-纳什支付增量**量纲不同** ⇒ 反解 `U` 之映射 0 在盘」；实测 `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md:81` 逐字「ε-纳什：任一玩家单独改策略的支付增量 < **ε=0.01**」＋「最多迭代：50 轮」＝**盘上唯一在册之收敛证书实体**。附：`KD-X2` 另明禁「守卫 `ε`」与「P-A 收敛 `ε=0.01`」**混用** | ✅ **相符**（**结论 0 冲突**）／**缺注**：回函未将证书落到盘上实体 `bd1caab42b4c` §3.4 之 `ε=0.01`／50 轮 |
| **X7** | 锚链面（回函 BL-4A 之条件前提：「If `exp_harness.py` is a frozen anchor…」） | ① `docs/V3X/KT_A1_SPEC_V0.1.md:43` 明列 `tools/exp_harness.py` 为 **5 冻结工件之一**；`:261` 锚表 `P_A_HARNESS` ＝ `9f383935c00c` ⇒ **前提在仓内成立** ✅；② 但实测现值 `275e480ba4d9` ⇒ **MISMATCH**，**已在册判 `DRIFT_AUTHORIZED`**（授权返工·二轨并存，`results/_kt_a1_anchor_drift_root_cause_2026_10_14.md`:42–43 **逐位一致** ＝ 本审计复算**0 新漂移**）；撤回条之宣告通道唯一＝PI 明示（在册 :45） | ✅ **相符**（前提成立）／**缺注**：回函 0 引在册锚登记与 `DRIFT_AUTHORIZED` 根因判 |
| **X8** | （回函 0 引）spec `:22` 指定之锚落位 `verifier/handoff/P_B_V0_anchors_sha256_12.json` | 实测 **`exists=False`** ⇒ P-B 5 锚之**指纹面 0 在盘** | ⛔ **MISSING_TRUE**（如实登记·**⛔ 0 编造来源**；**非回函所致**——回函 0 引此件） |

**面④ 小计：不符 4（X1–X4）／相符 2（X6–X7）／登记 2（X5 SAME_IDENTITY·X8 MISSING_TRUE）**

---

## §6 面⑤ · 不可核面／未复核（**0 逐条复核者·如实标「未复核」**）

| # | 项 | 状态 |
| :-: | :-- | :-- |
| **U1** | 回函精确 serving model／build identifier（回函 §5 项 7 自认） | ⚪ **未复核**（宿主不暴露；**0** 旁证） |
| **U2** | M-41 50/60 原始 LLM transcript（回函 §5 项 7 自认） | ⚪ **未复核**（盘上 0 transcript；结构性读数已由执行件覆核，见 §7 之 X 面外） |
| **U3** | 「Copilot SDK in VS Code」之宿主声明＋§0 所列三次工具调用明细 | ⚪ **未复核**（0 transcript／0 运行时日志在盘） |
| **U4** | **外部文献／标准引用面** | ✅ **实测：回函全文 0 处外部引用**——逐条检索 `http(s)://`／DOI／arXiv／Crossref／「References」**均 0 命中** ⇒ **无外部文献待复核**；其援引之「prior C4 replies」为**本地件**（仓内孪生可核，见 F12／X6）。⚪ 其援引之 Fano／Bayes 风险／有限表 Bayes 风险等**通用数学表述 0 给出处** ⇒ **未复核**（通用数学·非文献主张） |
| **U5** | 仓外 codex C4 回函（`a975c7990cd8`）之内容面 | 🟡 **部分可核**：仓内同哈希孪生件已就 `u*_t=1`／`max_u=1`／`3H/4` 自限／守卫比值代数逐条核（见 F12／X6）✅；其余内容 **未逐条复核** |

**面⑤ 小计：未复核 5（其中 U4 之「外部文献」面实测为 0 条）**

---

## §7 汇总计数

| 面 | 相符 | 不符 | 不可核／未复核 | 登记（不入判定） |
| :-- | --: | --: | --: | :-- |
| ① 代码主张（C1–C10） | **5** | **5** | 0 | — |
| ② 公式主张（F1–F12） | **8** | **3** | 0 | — |
| ③ 条款面（M1–M3） | **1** | **1** | **1** | — |
| ④ 冲突面（X1–X8） | **2** | **4** | 0 | 2（X5·X8） |
| ⑤ 不可核面（U1–U5） | 0 | 0 | **5** | — |
| **合计（36 判定项）** | **16** | **13** | **6** | **2** |

> **不相符 13 项之性质归类**：**行位引用面 9 项**（C2·C3·C6·C7·C8＋X4＝**6 项**归一为「引用面缺陷」）＋**射程/登记状态 3 项**（F3·F4·F12）＋**冲突面 3 项**（X1·X2·X3）＋**条款 1 项**（M1）。
> ⛔ **0 项为「回函之实体性主张被实测推翻」** —— 全部实体主张（`T4` 无 shuffle、`value` oracle、memoryless、`M3` 忽略 context、`mult` 守护式、`kill_decision` 阈值、3/14 与 `U` 式算术、`ε*` 量纲论、`mult=10.0`、T3 之 M-41 读数复算）**经实测全部成立**。

---

## §8 采认面候选清单（**供 PI 卡用 · 本件 0 采认 · 逐条注「经核验相符／存疑」**）

| # | 候选 | 经核验状态 | 须 PI 注意之要点 |
| :-: | :-- | :-- | :-- |
| **P1** | **`ε*` 规则**：`ε*(H) = H/10`（计数尺度）／`1/10`（率尺度） | **经核验相符**（算术·量纲·守护式三合，F7/F9）＋**存疑** | 与 prereg §6④「单一标量常数·不随格变/不随 t 变」**不相容**（X1）⇒ 若采之，**须 PI 明示是否改口径④**；且 `H` 未锁 ⇒ 当前无确定值 |
| **P2** | **`L` 式**：`L(M1,T) = 3g_aether/[(1−η)+ηg_couple+4g_aether]·H = 3/14·H` | **经核验相符**（`Fraction` 复算逐位，F3）＋**存疑** | ①射程仅「4 选 1 且 value 二元」族（T3＝7/29、T4＝1/12）；②参数**未冻结·须 PI 冻结**（X3）；③未携在册 `S-4`／`S-5` 诊断（X2） |
| **P3** | **`U` 式**：`U(M,T) = H·τ_cert/[1−(1−γ)^H]` | **经核验相符**（形式与递归相容·复算通过，F6）＋**存疑** | 属 route-乙 之**定义面修订**；`γ`／`τ_cert` **0 候选值**（须 PI 给）；回函 0 给值 ✅（此为其守纪处） |
| **P4** | **D1-A ／ D1-B 之择** | **阻塞性经核验相符**（`None` ⇒ `TypeError`，F11）｜**择定权属 PI** | **本件 0 建议 0 代裁**；`D1-A`（停用 `theory_U_hit_rate`）／`D1-B`（启用 route-乙 状态场）二者**均须 prereg 冻结**后方可入锁 |
| **P5** | **`KL-M41-1`**（no-action > 5% ⇒ ITT 为默认分母） | **存疑**（回函**新拟**，spec／M-41 在册 **0 载**） | 属口径切换（valid-only → ITT）；与在册 `KD-2` 之诊断互补而非冲突 |
| **P6** | **`KL-M41-2`**（`CI_hi(ΔR_ITT) < 0` 且 `|ΔR| ≥ 1/60`） | **存疑**（回函新拟） | ①`1/60` 之离散地板与在册读数（45/35 格）**不同面**；②采用 ITT 分母之切换须 PI 裁 |
| **P7** | **`KL-M41-3`**（3 seed 之 `std/mean > 0.20` ⇒ `SEED_SENSITIVE`） | **经核验相符** | 与 spec `:116` 之 A3 **逐字一致**（「seed=42,123,456 三套，看 std/mean > 0.2 则报『种子敏感』」）✅ ＝ 全表唯一「原已在新册」之项 |

---

## §9 幽灵引用三处对账（引用 vs 仓内实存 vs 仓外实存 · 五分支）

| # | 引用（回函所述） | 回函行 | 仓内实存 | 仓外实存 | 分支判定 |
| :-: | :-- | :-: | :-- | :-- | :-: |
| 1 | `letters/LETTER_TO_GEMINI4_GE01_THEORY_INPUTS_2026_10_15.md` | :3/:260 | ✅ `70fe266e87d6`／8,361 B／**75 行**（自报三值全符） | — | **FOUND_IN_REPO** ✅ |
| 2 | `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | :261 | ✅ `423c84de20d5`／**15,457 B**（自报字节相符） | — | **FOUND_IN_REPO** ✅ |
| 3 | `tools/distortion_calculator.py`（7 个符号名） | :262 | ✅ 全部存在：`PAY_DOMAIN`:96／`DEFAULT_C`:99／`distortion_indicator`:240／`distortion_gapwise`:270／`guarded_denominator`:305／`distortion_multiplier`:343／`kill_decision`:419 | — | **FOUND_IN_REPO** ✅（回函未给具体行位 ⇒ 行位面**不可核**，符号名面相符） |
| 4 | `tools/exp_harness.py`（7 段区间） | :263 | ✅ 实存 `275e480ba4d9`／10,090 B | — | **FOUND_IN_REPO**（存在性 ✅／行位 ❌ 见 X4） |
| 5 | `results/_m41_verdict_kd_effect_register_2026_10_15.md`（§§1–5·KD-1..5·BL-1..5） | :264 | ✅ 实存；`KD-1`:97／`KD-5`:101／`BL-2`:127／`BL-3..5`:128–130 逐项实测存在 | — | **FOUND_IN_REPO** ✅ |
| 6 | `results/_external_commission_gemini4_ge01_theory_inputs_2026_10_15_draft.md` | :18 | ✅ 实存，**与 `_dispatch.md` 同哈希 `70fe266e87d6`** | — | **SAME_IDENTITY**（0 冲突） |
| 7 | `c:\Users\Administrator\codex-workspace\c4_values_reply_2026_10_10\_codex_c4_values_unblock_reply_2026_10_10.md` | :265 | ✅ **同哈希孪生件** `letters/_codex_c4_values_unblock_reply_2026_10_10.md` ＝ `a975c7990cd8` | ✅ 实存（仓外） | **SAME_IDENTITY**（引用可解析·**仓外绝对路径依赖** ⇒ 资产缺陷登记） |
| 8 | （回函 0 引）spec `:22` 之 `verifier/handoff/P_B_V0_anchors_sha256_12.json` | — | ❌ **`exists=False`** | ❌ 未查（仓外非本面） | **MISSING_TRUE**（如实登记·⛔ 0 编造） |
| 9 | `c:\Users\Administrator\codex-workspace\`（回函 §0 所述之 prior C4 replies 目录） | :18 | — | ✅ 目录实存 | **FOUND_OUTSIDE**（目录面·内容面见 U5） |
| 10 | `docs/V3X/KT_A1_SPEC_V0.1.md`／`docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md`（本审计为 X6/X7 所引，**非回函所引**） | — | ✅ 两者均实存 | — | **FOUND_IN_REPO** ✅ |

**五分支计数**：FOUND_IN_REPO ＝ 6（#1–#5·#10）／**SAME_IDENTITY ＝ 2**（#6·#7）／FOUND_OUTSIDE ＝ 1（#9）／**MISSING_TRUE ＝ 1**（#8）／**CONFLICT（同名不同哈希·登记不覆盖）＝ 0**。

---

## §10 锚链核验（SHA-12／SHA-256 复算·MATCH／MISMATCH 逐件报）

| 锚 ID／件 | 登记值 | 登记出处 | 实测 SHA-12 | bytes | 判定 |
| :-- | :-- | :-- | :-- | --: | :-: |
| `P_A_HARNESS` | `9f383935c00c` | `KT_A1_SPEC_V0.1.md`:239／:261 | **`275e480ba4d9`** | 10,090 | 🔴 **MISMATCH** —— 但**在册已判 `DRIFT_AUTHORIZED`**（2026-09-10 Option A 授权返工·二轨并存）｜根因件 `_kt_a1_anchor_drift_root_cause_2026_10_14.md`:43 逐位一致 ⇒ **⛔ 0 记为新漂移** |
| `P_A_LLM_CLIENT` | `055e874ea5c1` | `KT_A1_SPEC_V0.1.md`:260 | **`1722500da4aa`** | 8,118 | 🔴 **MISMATCH** —— 同上（在册 :42 一致，`DRIFT_AUTHORIZED`） |
| `P_B_DISTORTION_CALC` | **在册 0 载摘要值**（仅锚 ID＋`version=2026-09-11`） | `P_B spec`:30 | `410a12482eef` | 40,611 | ⚪ **不可核**（在册面无值可比；且落位 JSON 见 X8 **MISSING_TRUE**） |
| `P_B_LLM_CLIENT` | **在册 0 载摘要值**（`version=2026-09-11`） | `P_B spec`:29 | `1722500da4aa` | 8,118 | ⚪ **不可核**（同上） |
| 回函正身 | `44311ade19de`／44,520 B（parent 已实测） | 派工单 | `44311ade19de` | 44,520 | ✅ **MATCH** |
| 委托稿（回函自报 `:19`/`:260`） | `70fe266e87d6`／8,361 B／75 行 | 回函自报 | 同 | 8,361 | ✅ **MATCH**（行数亦符） |
| P-B spec（回函自报 `:261`） | `423c84de20d5`／15,457 B | 回函自报 | 同 | 15,457 | ✅ **MATCH** |
| prereg 七要件 | `0a031a9795a9`／39,337 B | calculator 头 L23 | 同 | 39,337 | ✅ **MATCH** |
| 设计件 | `8ab699f017c8`／46,007 B | calculator 头 L35 | 同 | 46,007 | ✅ **MATCH** |
| M-41 执行件 | `b9feb5df8d44`／23,855 B | 派工单 | 同 | 23,855 | ✅ **MATCH** |
| T-2／T-3 取值件 | `bcb0d60fdd2d`／24,658 B | 派工单 | 同 | 24,658 | ✅ **MATCH** |
| 给值单 | `21abb5173b87`／15,054 B | 派工单 | 同 | 15,054 | ✅ **MATCH** |

> **0 项**为「回函自报指纹与盘上实体不符」⇒ 回函之可核引用面**全部真实**。

---

## §11 0 触动自证

- 本棒**新增件 ＝ 1**：本件 `results/_gemini4_reply_verification_register_2026_10_15.md`（落盘前实测 `Test-Path=False`＋stem 全仓 0 命中）。
- **既有件触动数 ＝ 0**：`letters/`·`docs/`·`tools/`·`results/` 全部**只读**；本审计未对任何既有件执行写入／移动／重命名／删除。
- **frozen 面**：V1–V3 资产、frozen 锚件（`exp_harness.py`／`llm_client.py`／`distortion_calculator.py`／spec／prereg）**0 写入**；仓外目录（`c:/Users/Administrator/codex-workspace/`）**只读 0 写入**。
- **0 网络**、**0 LLM 调用**、**0 读 `.env`／key**、**0 上传／0 远端写**、**0 宣告①毕**、**0 闭 `R-8`**。
- 数值面全部以 `Fraction` 精确复算，**⛔ 0 浮点近似充精确值**。

---

## §12 资产缺陷登记（**登记 ≠ 修复 · frozen 内只登记不代修**）

| # | 缺陷面 | 位 | 性质 | 处置 |
| :-: | :-- | :-- | :-- | :-: |
| A1 | **行位引用面缺陷**（回函 12 处行位中 **6 处**与盘上实体不符；实体主张本体均成立） | 回函 :91/:95/:159/:174–184/:263 | 引用层 | ⛔ 0 代改回函（外来件·PI 面）；**须 PI 注意**：可采其结论、⛔ 0 采其行位 |
| A2 | **仓外绝对路径依赖** | 回函 :265（`c:\Users\Administrator\codex-workspace\...`） | 引用层 | 建议后续引用改采仓内相对路径（仓内已有同哈希孪生件） |
| A3 | **spec 指定之锚落位件缺件** | `verifier/handoff/P_B_V0_anchors_sha256_12.json`（`P_B spec`:22） | 资产面 | **MISSING_TRUE** 如实登记；⛔ 0 编造、⛔ 0 自造以填 |
| A4 | **在册锚登记 vs 盘上实体 2 处 MISMATCH** | `KT_A1_SPEC_V0.1.md`:260–261 | 锚链面 | **在册已判 `DRIFT_AUTHORIZED`**（根因件 :42–43）⇒ 本件**0 重复报为新漂移**、**0 宣告撤回**（撤回通道唯一＝PI 明示） |
| A5 | **仓内既有行位偏差（同族）** | 取值件 `_t2_t3_value_sourcing_2026_10_15.md`:133 记 T3 shuffle 为「:196」（实测 **:197**） | 引用层 | 本审计**登记**，⛔ **0 回改既有件**（历史留痕） |
| A6 | **`ε` 一词双重占用**（守卫 `ε` vs P-A 收敛 `ε=0.01`） | 在册 `KD-X2`（`c2af59477178`） | 术语面 | 回函 0 混用 ✅（本审计已核其全文）；继续沿 `KD-X2` ⛔ 0 混用 |

---

## §13 交回 parent 之要点（一句话冲突 + 计数）

- **须 PI 注意之一句**：回函所荐 `ε*(H)=H/10` 随 `H` 变，**与在册 prereg §6④「`ε` 须 PI 于 prereg 固定·单一标量常数·不随格变/不随 t 变」不相容**，且 `H` 之精确值本身「须 PI 另给·0 代给」⇒ `ε*` 与 `3/14·H` 两式**皆成立于未冻结前提**，须 PI 先裁「口径④ vs H 依赖式」与参数冻结，方可采认。
- **计数**：**相符 16 ／ 不符 13 ／ 不可核 6**（另登记 SAME_IDENTITY 2·MISSING_TRUE 1）。
- **⛔ 0 冲突项须注意**：回函**未**推翻任何实体主张；13 项「不符」中 **6 项**为**行位引用**（含 §5 之 7 段区间全不符），**3 项**为射程/登记状态，**3 项**为与在册口径之冲突（X1–X3），**1 项**为 model 条款部分不符。
- **⛔ 0 阻塞**：本审计 0 遇阻；唯 2 项**不可核**已如实标注（model 字符串·运行时 transcript），**0 编造**。

---

*件止。`evidence-auditor` · 2026-10-15 —— **核验登记 · 候 PI 裁 · ⛔ 0 采认**｜逐条 36 判定项（相符 16／不符 13／不可核 6）＋登记 3（同一性 2·缺件 1）｜锚链 12 件 MATCH/MISMATCH 逐件报（2 处 MISMATCH 皆**在册已判** `DRIFT_AUTHORIZED`，**0 新漂移**）｜⛔ 0 代 PI 裁 · 0 采任何回函值 · 0 回填锚／给值单 · 0 回改既有件 · 0 调和冲突 · 0 编造来源（`MISSING_TRUE` 如实登记）· 0 触 frozen · 0 写仓外。*
