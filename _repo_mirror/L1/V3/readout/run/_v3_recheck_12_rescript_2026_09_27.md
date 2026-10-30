# V3-R 补审改判件 #12 · BOSS-PE-2 real transverse Ising（rescript）

> **性质**：V3 假象类补审改判件（9 条系列之第 12 条）；**V3 原报告 byte 0 触动**，本件与原标注**并列**登记
> **依据**：`results/_v3_recheck_prereg_v1_2026_09_27.md`（实测 SHA-12 `88052d7db895`，37,346 B）§1.2 #12 / §2.2 K-V3R-12 / §2.4 TH-V3R-12 / §2.3 改判规则表 / §4 改判登记规则
> **配套三件套**：executor `results/_v3_recheck_12_executor_2026_09_27.py` ｜ result `results/_v3_recheck_12_result_2026_09_27.json` ｜ 本 rescript
> **勘误链位**：E-41.x 系（沿既有 E-1…E-16 链追加，0 覆盖原条目）
> **PI 复核栏**：待 PI 签字生效即锁

---

## 1. 输入链核验（只读，先核后用）

| # | 件 | 实测 SHA-12（小写） | 字节 | 预登记 v1 记录 | 判定 |
|---|---|---|---|---|---|
| 1 | `results/boss_pe_2_real_transverse_ising_2026_09_15.json` | `8933d61b180a` | 3,553 | `04CEDB126B98` / 3,553 | ⚠ SHA 不符、**字节逐字一致** |
| 2 | `results/boss_pc_2_real_transverse_ising_2026_09_15.json` | `8933d61b180a` | 3,553 | 未列 | ✓ **与 #1 字节完全相同**（见 §1.2） |
| 3 | `deposon_team/plugins/boss_pc_2_transverse_field_ising.py` | `210105a7f29a` | 7,053 | 未列 | ✓ 在盘（只读，0 import） |
| 4 | `results/deposon_v3_physical_opt_60cells_2026_09_11.json` | `c659695aa23c` | 17,732 | 未列 | ✓ 在盘 |
| 5 | `docs/V3X/P_E_D1_D3_REPORT_2026_09_15.md` | `900da300d11e` | 13,109 | 未列 | ✓ 在盘（§1.2 risk3「D_fix2 ADOPTED」字面来源） |
| 6 | `results/_v3_recheck_prereg_v1_2026_09_27.md` | `88052d7db895` | 37,346 | 派工单字面 | ✓ MATCH |

**预登记 SHA 列偏差**：v1 §0.2 记 `04CEDB126B98`，本 worker `hashlib.sha256(全文字节).hexdigest()[:12]` 实测 `8933d61b180a`，**字节数逐字一致（3,553）**。同 v1.1 §0.3 已立之更正登记，**系统性差异指向哈希输入约定/转写错位，非内容变更**；**内容侧逐字复核吻合**（9 model、`h_c_at_T ≡ 0.5`、`transverse_ising_region ≡ false`、`outside_gt_0.15 = 9`、五个预注册常数）。**预登记 0 字节改动，未代为修订**。

### 1.2 件谱系：PE-2 与 PC-2 **字节完全相同**（γ₄）

`boss_pe_2_real_transverse_ising_2026_09_15.json` 与 `boss_pc_2_real_transverse_ising_2026_09_15.json` **SHA-12 同为 `8933d61b180a`、字节同为 3,553、`byte_identical = true`**。源件 SELF-CHECK 段记有命名勘误 lineage（`boss_pe_2_…` → `boss_pc_2_…`，历史结果保留于 PE-2 文件名）。

**⇒ #12 的原结论与 BOSS-PC-2 是同一次实跑，不是两次独立实验。** 本件不将其计为两次独立证据，如实登记。

### 1.3 legacy 逐字复现

V3 公式逐字转写后重跑：**9/9 model 的 `T_frac` / `R_frac` / `A_frac` / `D_fix2` / `D_fix2_verdict` / `h_c_at_T` / `dist_to_h_c_T` / `transverse_ising_region` 全部逐字一致**；距离分布 `{strict 0, gray 0, outside 9}` 与 verdict = `PASS (>= 7/9 model significantly deviate…)` 均与源件一致。

## 2. 原 V3 标注

| 项 | 字面 |
|---|---|
| 对象 | BOSS-PE-2（real transverse Ising check） |
| 原结论 | **PASS**（≥ 7/9 model 显著偏离横场 Ising；`distance_distribution.outside_gt_0.15 = 9`） |
| 死因（预登记 §1.2 #12 字面） | `h_c_at_T ≡ 0.5`（Pfeuty 1D chain 简化，构造恒同）+ `transverse_ising_region ≡ false`（同）⇒ 判据输入恒同 |
| 类型 | **假成立** |

### 2.1 三重根因（本件逐条机制化 + 数值核验）

| # | 根因 | 实测 |
|---|---|---|
| 1 | **硬编码常量**：源件 `ising_critical_line(t_frac)` 函数体只有 `return 0.5`，docstring 自承「简化: 沿 T_frac 作 h_c(T) 平均值」但未实现 ⇒ `h_c_at_T ≡ 0.5` 与入参无关 | 9/9 |
| 2 | **冻结常数与判据脱钩（γ₂ 前身）**：`PFEUTY_H_C_OVER_J = 1.0` 虽写入 `pre_registered_constants`，但**判定路径从未使用它**（`v3_constant_is_used_in_code = false`） | 实测 |
| 3 | **量纲错配**：V3 算 `dist_to_h_c_T = \|R_frac − 0.5\|`，其中 `R_frac` 是 cell 比例、`0.5` 注释为「归一化到 T_frac 单位」；而 TFIM 的相变量是**横向场比 h/J**（TH-V3R-12 冻结的 `PFEUTY_H_C_OVER_J = 1.0` 即 h_c/J）。把 cell 比例与场比直接相减，**在 TFIM 相图上没有对应点** | 逐式核验 |

**根因（诚实的根因是不误导）**：原 PASS 立在「硬编码常量 0.5 × 量纲错配相减」之上，**判据输入恒同且与 TFIM 相图无对应**。原判据从未受审。

## 3. 补审构造（沿 §1.2 #12 (a)(b)(c) 字面，0 新设阈值）

```
(a) h_c 真抽样：1D TFIM **标准精确临界条件** sinh(2K) sinh(2Γ) = 1
        => 2Γ_c = asinh(1/sinh(2K))，  h_c/J = Γ_c / K
    约定（本件逐字声明）：H = -(J/4) Σ σ^z_i σ^z_{i+1} - (h/4) Σ σ^x_i，
                        K ≡ βJ/4，Γ ≡ βh/4，t_rel ≡ k_BT/J = 1/(4K)
        => h_c/J = 2 t_rel asinh(1/sinh(1/(2 t_rel)))     （关于 t_rel 单调递增）
    逐 model 在 (T,J) 10x10 = 100 格上取样（≥ v1 要求的「至少 100 sample/model」）
    独立核验：沿 Γ 二分求临界条件残差 sinh(2K)sinh(2Γ)-1 的符号翻转（**不使用 asinh 闭式**）
(b) 真 phase boundary 测试：精确临界线 + per-model empirical 散点
    映射（显式声明的 worker 口径，附敏感性）：
        主轴  drive h/J := R_frac / T_frac，  t_rel := T_frac
        敏感性轴 drive h/J := R_frac（V3 字面轴）
(c) 主判据换 D_fix2（P-E 报告 §1.2 risk3 已 ADOPTED；阈值沿既有字面 0.05 / 0.15）
    verdict 规则一字不动：n_in_strict ≥ 7 -> FAIL；n_outside ≥ 7 -> PASS；否则 GRAY
```

### 3.0 本件自身勘误（如实登记，0 隐瞒）

**初版推导有符号错误，已作废。** 初版按「2x2 迁移矩阵 leading eigenvalue 简并」推导临界条件，得 `h_c/J = 2 t_rel asinh(e^{-2/t_rel})`。本件后加的**临界条件自校验**证明该推导错误：对 `T = [[e^{K+Γ}, e^{-K}], [e^{-K}, e^{K−Γ}]]`，判别式 `((T11−T22)/2)² + T12·T21 = e^{2K} sinh²(Γ) + e^{−2K} > 0`（Γ > 0 恒成立）⇒ **该 2x2 形式不存在本征值简并**。物理上 1D TFIM 在**有限 L 下恒有隙**，量子临界是 **L→∞ 极限的能级交叉**，不是有限 2x2 的简并。

**作废留证（正面证据）**：自校验对作废公式逐点代入临界条件残差，实测 `deprecated_formula_satisfies_condition_anywhere = false`（例：t=0.3 处残差 = −0.9968，远非 0）。**作废公式的数值未参与任何判定。**

**自校验结果**：7/7 探针通过；闭式 vs 二分最大偏差 **4.441e-16**；临界条件残差最大 **2.220e-16**；`all_pass = true`。

### 3.1 (a) 的可实现性实测（γ₁，不编造）

**实测**：1D TFIM 精确临界线在 (T, h/J) 平面上是**单条曲线** `h_c/J = 2 t_rel asinh(1/sinh(1/(2 t_rel)))`（关于 t_rel 单调递增：t→0 ⇒ 0，t→∞ ⇒ ∞）。解析解与二分数值解**最大绝对偏差 4.441e-16**（核验通过）。

V3 冻结的 `PFEUTY_H_C_OVER_J = 1.0` 只是该曲线上的**一点**（实测落点 **t_rel ≈ 0.567296**，κ ≈ 1.762747），**本身不携带可抽样的 T 依赖分布** ⇒ §1.2 #12(a) 字面要求的「连续 h_c(T,J) 分布」**无法从冻结常数直接导出**。本件以 (T,J) 10×10 格在曲线上取样得真分布（逐 model `h_c_over_J` **n_distinct = 10**），**0 引入预登记之外的物理量，0 编造相图读数**。

自算相界（h_c/J vs t_rel）：`0.2→0.065816`、`0.3→0.229405`、`0.4→0.471607`、`0.5→0.771937`、`0.6→1.117324`、`0.7→1.499281`、`0.8→1.911969`、`0.9→2.351161`、`1.0→2.813658`、`1.1→3.296959`。


### 3.2 (b) 的缺件登记（γ₂，不编造）

§1.2 #12(b) 字面要求「沿 **Jordan-Sucher-Votek 1999** 数值解」。**实测：该文献相图本仓 0 命中、本件 0 联网、0 代理 ⇒ 其曲线与数值未复现、0 编造。** 本件改用**自实现精确对角化相界**替代，并如实标注为**替代品**。JSV 1999 专项对照**留 PI 拍板**（是否授权联网调取，或由 PI 直接提供该相图）。

### 3.3 设计口径（沿 `@scientific-research-workflows` / `experimental-design`）

- **区组** = 9 model；**处理** = 温度 10 档 × 耦合 10 档全因子 = 100 格/模型，**无别名**；9 × 100 = 900 格。
- **伪重复声明**：每 model 的 100 个 `h_c` 样本**嵌套于** model，**独立重复的真实层级 = 9 个 model（不是 900）**；判定在 model 层级聚合，样本量不作为独立信息计入。
- **名义 N 显式标注（γ₅）**：**30/60-cell 精确半化实测 9/9**（`T60 = 2×T30` 且 `R60 = 2×R30` 且 `A60 = 2×A30`）⇒ 60-cell 是 30-cell 的**精确 2× 复制，不携带额外独立信息**；**名义独立 N = 30 cell/model（不是 60）**。跨尺寸信息须重采样方可比；本件沿 60-cell 口径（V3 既有字面）但显式标注该限制，**0 自造权、未重采样**。
- **seed** = 20260927。

## 4. 补审 result（K-V3R-0-C 双口径）

### 4.1 防退化门自证（K-V3R-0-A）

| 输入字段 | n | n_distinct | std | 门 |
|---|---|---|---|---|
| `T_frac`（盘上真实） | 9 | **7** | 0.053287 | pass |
| `R_frac`（盘上真实） | 9 | **7** | 0.040825 | pass |
| `A_frac`（盘上真实） | 9 | **7** | 0.069832 | pass |
| `D_fix2`（盘上真分布） | 9 | **9** | 0.060087 | pass |
| *（对照）legacy `h_c_at_T`* | *9* | *1* | *0.0* | *退化（预期）* |
| *（对照）legacy `transverse_ising_region`* | *9* | *1* | *0.0* | *退化（预期）* |

`degenerate_alarm_hit = false`

### 4.2 逐 model 重构结果（Arm 主轴 `drive = R_frac / T_frac`）

| model | `R_frac` | drive `h/J` | `dist_min` | `region_new` | `D_fix2` | `D_fix2_verdict` | *legacy* `dist_to_h_c_T` | *legacy* region |
|---|---|---|---|---|---|---|---|---|
| doubao-seed-2.0-lite | 0.0667 | 0.1538 | 0.0756 | False | 0.0007 | PASS | 0.4333 | false |
| glm-5.3 | 0.0500 | 0.1154 | 0.0496 | **True** | 0.0000 | PASS | 0.4500 | false |
| deepseek-v4-flash | 0.0833 | 0.2174 | 0.0120 | **True** | 0.0012 | PASS | 0.4167 | false |
| doubao-seed-evolving | 0.1000 | 0.2727 | 0.0433 | **True** | 0.0014 | PASS | 0.4000 | false |
| minimax-m3 | 0.1333 | 0.3810 | 0.0907 | False | 0.0000 | PASS | 0.3667 | false |
| glm-5.3-flash | 0.0167 | 0.0476 | 0.0182 | **True** | 0.0525 | GRAY | 0.4833 | false |
| kimi-k2.7-code | 0.1333 | 0.4211 | 0.0506 | False | 0.0070 | PASS | 0.3667 | false |
| doubao-seed-2.1-turbo | 0.0333 | 0.1111 | 0.0453 | **True** | 0.1078 | GRAY | 0.4667 | false |
| deepseek-v4-pro | 0.0333 | 0.1250 | 0.0592 | False | 0.1776 | FAIL | 0.4667 | false |

**距离分布**：strict ≤ 0.05 = **5**、gray 0.05–0.15 = **4**、outside > 0.15 = **0** ⇒
**重构 verdict = `GRAY (mixed distribution)`**（V3 规则一字未动：未达 ≥7 strict，也未达 ≥7 outside）。

**`dist_min` 分布：n_distinct = 9，std = 0.023353，min = 0.0120，max = 0.0907** ⇒ 真分布。

**敏感性轴（`drive = R_frac`，V3 字面轴）**：strict = **7**、gray = 2、outside = 0 ⇒ **`FAIL (>= 7/9)` 侧**。

**⇒ 两轴一致的关键事实：outside（>0.15）= 0，9/9 模型无一「显著偏离横场区」。** 原 `PASS（9/9 显著偏离）` 在真相界下**得不到支持**（γ₃：映射未预注册，结论对此敏感，故两轴并报）。


### 4.3 §1.2 #12(c) 主判据 D_fix2（真分布）

**`D_fix2` 分布：n_distinct = 9，std = 0.060087；档位 PASS 6 / GRAY 2 / FAIL 1**（与源件 `d_fix2_distribution` 逐字一致）。
逐 model 档位：PASS = doubao-2.0-lite / glm-5.3 / deepseek-v4-flash / doubao-evolving / minimax-m3 / kimi-k2.7-code；GRAY = glm-5.3-flash / doubao-2.1-turbo；FAIL = deepseek-v4-pro。

### 4.4 K-V3R-12 判定（**标签碰撞警示**）

**标签碰撞（本件必须显式声明，否则会得出相反结论）**：D_fix2 的档名 **`PASS`（= 近乎重合于基线 = 无新结构）** 与横场判据的 verdict **`PASS`（= 显著偏离 = 有新结构）语义相反**。本件**一律先映射到声明的语义方向轴**「是否存在新结构（散射层差异化）」再比较，**0 用字符串比较 verdict**。

| 侧 | 读数 | 语义方向 |
|---|---|---|
| 横场判据（主轴） | 5 strict / 4 gray / 0 outside ⇒ `GRAY (mixed)` | **mixed** |
| 横场判据（敏感性轴） | 7 strict / 2 gray / 0 outside ⇒ `FAIL` | no_new_structure |
| D_fix2（≥7 严格规则） | PASS 6 < 7 ⇒ `MIXED_ge7_rule_not_met` | 混合 |
| D_fix2（多数档） | PASS 6/9 多数 ⇒ `no_new_structure` | **no_new_structure** |

| K-V3R-12 判据 | 状态 |
|---|---|
| verdict 与 D_fix2 真分布一致 | **否**（主轴 = `mixed` vs D_fix2 多数档 = `no_new_structure`） |
| 判据输入仍恒同（重构侧） | **否**（`h_c_over_J` 逐 model n_distinct = 10；`dist_min` n_distinct = 9） |
| **`kill_line_pass`** | **false**（不一致分支命中） |

**逐 model 一致性**：`region_new == False ↔ D_fix2_verdict == PASS` **5/9 一致** ⇒ 逐 model 关联亦弱，如实登记，0 用聚合掩盖。

**诚实判读**：K-V3R-12 第一分句（一致 ⇒ PASS）**不成立**，第二分句「不一致 / 判据输入仍恒同 ⇒ **FAIL（维持假成立）**」**命中** ⇒ 维持原「假成立」标注。注意重构判据**已解恒同**（真判据），但**方向不与 D_fix2 一致**，故不得改判「真成立」。

### 4.5 双口径判定（K-V3R-0-C）

| 口径 | verdict | 依据 |
|---|---|---|
| **新构造 verdict** | **FAIL**（K-V3R-12 不一致分支） | 方向不一致（`mixed` vs `no_new_structure`） |
| 重构横场 verdict（主轴 / 敏感性轴） | **GRAY (mixed)** / **FAIL** | V3 规则一字未动；两轴 **outside 均为 0** |
| **沿原 V3 阈值字面 verdict** | **PASS**（9/9 `outside_gt_0.15`，`h_c_at_T ≡ 0.5` 恒同） | 与源件逐字一致（9/9 复现） |
| **一致性** | **不一致** | 新构造 FAIL vs 原标注 PASS，不同向 |

**⚠ 关键改判内容（防误导硬约束）**：原标注 `PASS（9/9 显著偏离横场 Ising ⇒ P-E 是新结构）`。重构真相界下 **outside（>0.15）= 0，9/9 模型无一「显著偏离」** ⇒ **该「新结构」主张在真相界下得不到支持**；且原 PASS 立在「硬编码常量 0.5 × 量纲错配」之上（§2.1）。**本条维持「假成立」标注，0 改判「真成立」。**


## 5. 改判动作（沿预登记 §2.3 + §4）

| 项 | 结论 |
|---|---|
| 命中档位 | **§2.3 第 3 行（FAIL = 原标注维持）** |
| 改判动作 | **0 改判动作**：维持原 V3 标注（不动，byte 0 触动）+ 本 rescript 与原标注**并列**登记 + γ |
| **判读要点** | 重构判据**已解恒同**（真判据），但方向**不与 D_fix2 一致**（`mixed` vs `no_new_structure`）⇒ K-V3R-12 第一分句不成立，**维持「假成立」**。真相界下 **outside = 0 / 9**，原「9/9 显著偏离 ⇒ 新结构」主张**得不到支持** |
| γ₀ | **本件自身勘误**：初版按 2x2 迁移矩阵本征值简并推导临界条件（`h_c/J = 2 t asinh(e^{-2/t})`），被本件自加的临界条件自校验查出**符号错误**（判别式 `e^{2K}sinh²Γ + e^{-2K} > 0` 恒成立 ⇒ 无简并）而作废；改用标准精确条件 `sinh(2K)sinh(2Γ)=1`。**作废公式数值未参与任何判定**；自校验 7/7 通过（闭式 vs 二分 ≤ 4.441e-16，残差 ≤ 2.220e-16） |
| γ₁ | 1D 精确临界线为**单条曲线**（`h_c/J = 2 t asinh(1/sinh(1/(2t)))`，单调递增；解析 vs 二分最大偏差 4.441e-16）；冻结常数 `PFEUTY_H_C_OVER_J = 1.0` 只是其上一点（t_rel ≈ 0.567296，κ ≈ 1.762747），**不携带可抽样的 T 依赖分布** ⇒ (a) 以 (T,J) 10×10 = 100 格/模型 的取样替代，0 编造 |
| γ₂ | **Jordan-Sucher-Votek 1999 数值相图缺件**（本仓 0 命中、0 联网、0 代理）⇒ 其曲线**未复现、0 编造**；本件以自实现精确临界线替代并标注为替代品。**JSV 专项对照留 PI 拍板** |
| γ₃ | `(T_frac, R_frac) → (T, h/J)` 映射在 V3 与预登记中**均未定义**；本件显式声明 `drive = R_frac/T_frac` 并附 `drive = R_frac` 敏感性轴（主轴 GRAY / 敏感性轴 FAIL，**两轴 outside 均为 0**） |
| γ₄ | **BOSS-PE-2 与 BOSS-PC-2 两件 result JSON 字节完全相同**（同 SHA-12 `8933d61b180a`、同 3,553 B）⇒ 同一次实跑，0 计为两次独立证据 |
| γ₅ | **30/60-cell 精确半化 9/9** ⇒ 60-cell 为 30-cell 的精确 2× 复制，**名义独立 N = 30 cell/model**；跨尺寸信息须重采样，本件未重采样 |
| γ₆ | `deepseek-v4-pro` 的 `D_fix2` 在 PE-2 记 **0.1776**、在 60cells 记 **0.1775**（同式同输入下余弦方向不变 ⇒ 纯 float64 舍入差 0.0001）；如实登记，**0 代为统一** |
| γ₇ | 迁移矩阵/临界条件约定（K ≡ βJ/4、Γ ≡ βh/4）决定 `h_c/J` 的**绝对刻度**；换约定会平移刻度但**无量纲临界条件 `sinh(2K)sinh(2Γ)=1` 不变**。本件全程以无量纲 (κ, Γ) 报告并给出常数落点，供换约定时对齐 |
| γ₈ | **标签碰撞**：D_fix2 档名 `PASS`（近基线 = 无新结构）与横场 verdict `PASS`（显著偏离 = 有新结构）语义相反；本件一律先映射语义方向轴再比较，0 字符串比较 |
| γ₉ | 逐 model 方向一致性仅 **5/9**、聚合方向亦不一致 ⇒ 判据与 D_fix2 的关系**弱**，本条结论强度受限，如实登记 |
| V3 原报告 | **byte 0 触动**（源件与 P-E 报告均未写） |
| 是否翻案 | **否** —— 本件只改「结论-证据关系」的登记，不重裁命题存亡（沿预登记 §5.1） |

## 6. 老实交代段

1. **0 编造**：全部读数由盘上真实 (T,R,A) 整数与自实现精确迁移矩阵经 seeded 计算得出；0 外部文献号新增（Pfeuty 1D Ising / JSV 1999 沿预登记字面引用，**JSV 相图数值未复现、未编造**）。
2. **0 擅调阈值**：`PFEUTY_H_C_OVER_J=1.0` / `TOL_STRICT=0.05` / `TOL_LOOSE=0.15` / `D_FIX2_PASS_LT=0.05` / `D_FIX2_FAIL_GE=0.15` 全部沿 boss_pe_2 `pre_registered_constants` 字面；verdict 规则（≥7 判 PASS/FAIL）一字未动。
3. **worker 落地选择（口径/实现量，非阈值）**：临界条件约定、`(T,J)` 10×10 采样网格及其上下界、`drive` 映射、语义方向映射 —— 均**显式声明 + 附敏感性**（两映射轴并报），0 隐藏，**留 PI 复核**。相界单调性实测通过（`h_c/J` 关于 t_rel 单调递增），故网格加密不改变判定。
4. **自身勘误已如实登记（γ₀）**：初版推导的符号错误被本件自校验查出并作废，**未隐瞒、未让作废数值参与判定**。如实交代的价值高于表面无误。
5. **不掩盖对自己不利的读数**：K-V3R-12 判 **FAIL**（维持假成立）；逐 model 方向一致性仅 **5/9**、聚合方向亦不一致，0 用聚合掩盖。
6. **两处跨文件不一致如实登记未统一**：PE-2 ≡ PC-2 字节相同（γ₄）、`D_fix2` 0.1776 vs 0.1775 舍入差（γ₆）。
7. **skill**：`@scientific-research-workflows` / `experimental-design`（`SKILL.md` SHA-12 `0a314eed103a`）；本仓与 plugin-cache 均可定位，**未 fallback**，0 编造 skill 指令。
8. **succeeded ≠ 跑完**：本件以 result JSON 落盘 + hashlib SHA-12 复算 + **重跑逐字不变自证通过**为准。
9. **0 明文密钥**：`results/_v3_recheck_12_*` 三件 key 形态自扫 0 命中。

---

**PI 复核栏**：☐ 通过（按 §2.3 第 3 行登记生效 · 维持「假成立」）　☐ 打回（退回重跑 / 需补构造 / 需授权 JSV 1999 相图）　签字：__________　日期：__________

出证｜Mavis 团队 worker 出件｜2026-09-27


<!-- appended-note:2026-09-30 skill 引用面复核（PI 派工第④项 · 0 删改历史字面） -->

> **附注（2026-09-30 追加 · 非原件内容）**
> 本件原引用字面**逐字保留、0 删改**；本附注**只增不改**。
>
> - **原引用面**：L204（出现 1 处）· `experimental-design`（SKILL.md SHA-12 `0a314eed103a`）；本仓与 plugin-cache 均可定位
> - **2026-09-30 只读复核**：原引用字面**2026-09-30 仍成立**（写死路径逐字在位、树哈希同目录名、`SKILL.md` SHA-12 对得上）⇒ **无过期值可改**，故仅追加注记、**不就地更新**
> - **当前三段式锚**（plugin:skill + 树哈希前 12 + SKILL.md SHA-12 + 定位方式）：scientific-research-workflows:experimental-design` · 树 ``611965fcb620`` · ``SKILL.md`` SHA-12 ``0a314eed103a`` / 13,044 B（实体直读；运行时加载行为见执行件 §6，**本棒 0 复现**）
> - **「历史实测 vs 今日实测」口径**：本件所记为**当时实测证据**，**保留有效、0 回改**；今日复核值以本附注与执行件为准，读者可据此区分二者（起因件建议 A2）。
> - **执行件**：`results/_skill_reference_update_and_user_surface_survey_2026_09_30.md` · 出件 **worker**（本棒）· **0 删改本件任何既有字节**