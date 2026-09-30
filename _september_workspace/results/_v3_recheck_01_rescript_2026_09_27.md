# V3-R 补审改判件 #1 · BOSS-P-A1 RBR/RM 倍数（rescript）

> **性质**：V3 假象类补审改判件（9 条系列之第 1 条）；**V3 原报告 byte 0 触动**，本件与原标注**并列**登记
> **依据**：`results/_v3_recheck_prereg_v1_2026_09_27.md`（实测 SHA-12 `88052d7db895`，37,346 B）§1.2 #1 / §2.2 K-V3R-1 / §2.4 TH-V3R-1 / §2.3 改判规则表 / §4 改判登记规则
> **配套三件套**：executor `results/_v3_recheck_01_executor_2026_09_27.py` ｜ result `results/_v3_recheck_01_result_2026_09_27.json` ｜ 本 rescript
> **勘误链位**：E-41.x 系（沿既有 E-1…E-16 链追加，0 覆盖原条目）
> **PI 复核栏**：待 PI 签字生效即锁

---

## 1. 输入链核验（只读，先核后用）

| # | 件 | 实测 SHA-12（小写） | 字节 | 预登记 v1 记录 | 判定 |
|---|---|---|---|---|---|
| 1 | `results/boss_pa_1_rbr_rm_result_2026_09_15.json` | `c7c59e0d2f6c` | 8,753 | `D9E14ED29FB9` / 8,753 | ⚠ SHA 不符、**字节逐字一致** |
| 2 | `deposon_team/plugins/boss_pa_1_rbr_rm.py` | `5cc594147e00` | 17,743 | `1935F164D5F3` / 17,743 | ⚠ SHA 不符、**字节逐字一致** |
| 3 | `results/deposon_v20_baselines.json` | `6edb2aec1660` | 16,987 | 未列 | ✓ **在盘**（见 §1.2） |
| 4 | `results/deposon_v3_physical_opt_60cells_2026_09_11.json` | `c659695aa23c` | 17,732 | 未列 | ✓ 在盘 |
| 5 | `results/_v3_recheck_prereg_v1_2026_09_27.md` | `88052d7db895` | 37,346 | 派工单字面 | ✓ MATCH |

### 1.1 预登记 SHA 列偏差（如实登记，不代为修订预登记）

v1 §0.2 对本条 2 件记录的 SHA-12（`D9E14ED29FB9` / `1935F164D5F3`）与本 worker 按 `hashlib.sha256(全文字节).hexdigest()[:12]` 实测值不符，**但字节数逐字一致**（8,753 / 17,743）。v1.1 §0.3 已就同类偏差立过更正登记（`1A90FD8F385A` → `b7547329af2e`），**系统性差异指向哈希输入约定/转写错位，非内容变更**。**内容侧已逐字复核**：预登记对 #1 的描述（22 图、`rm_iter ≡ 6`、`bayes_iter ∈ {1,200}`、`rbr_multiplier_mean = 145.8182`）与盘上 JSON **逐字吻合**。**预登记 0 字节改动**。

### 1.2 v20 baselines「真缺件」fallback —— **实测未触发**

预登记 §1.2 #1 与辅助说明记「v20 baselines 真缺件（`0EDB2AEC1660`），沿 C2 路径用 stored 22 graphs seed=210021 reweight」。

**实测：`results/deposon_v20_baselines.json` 在盘，SHA-12 = `6edb2aec1660`，与 #1 源件内记 `v20_baselines_sha12` 值逐字相同。** ⇒ **fallback 未触发**，本件直接用盘上真件，0 编造补数，0 触发 reweight 路径。

### 1.3 legacy 逐字复现（双口径地基）

以 V3 源件公式逐字转写后重跑：**22/22 图的 `rbr_iter` / `rm_iter` / `bayes_iter` / 两个 multiplier 全部逐字一致**；`rbr_multiplier_mean` 重算 = 145.8182（与源件一致）；verdict 重算 = `DIFFERENTIATED`（与源件一致）。⇒ 源件可复现，本件对「原 V3 阈值字面」口径的读数可信。

## 2. 原 V3 标注（沿 Trae v3 回函 §1.2 #1 字面 + 源件字面）

| 项 | 字面 |
|---|---|
| 对象 | BOSS-P-A1（Repeated Best Response / Regret Matching，Hart & Mas-Colell 2000） |
| 原结论 | **DIFFERENTIATED**（`rbr_multiplier_mean = 145.8182` ≥ 2.0×） |
| 死因（预登记 §1.2 #1 字面） | `simulate_rm` 22/22 `rm_iter ≡ 6`（构造 L176 `if max(R_A)<1e-3 and t>5: return t` 触发）+ `bayesian_nash_iter` 22/22 ∈ {1, 200}（构造 L189 `return 1 if nash else 200` 二值） |
| 类型 | **假成立** |
| 盘上实测复核 | `rm_iter` 22/22 ≡ 6（n_distinct = 1，std = 0）；`bayes_iter` ∈ {1, 200}（n_distinct = 2）；`rbr_iter` ∈ {2, 200} |

**根因（诚实的根因是不误导）——本件补一条预登记未点明的第三根因**：

1. **`rm_iter ≡ 6` 不是阈值松紧问题，是精确零 regret 的结构后果。** `simulate_rm` 写 `R[1-s] = max(0, avg[1-s] - avg[s])`，而**未玩过策略的累计支付恒为 0** ⇒ `avg[1-s] = 0`；只要所玩策略平均支付 > 0，regret 恒等于**精确 0.0**（不是「小于 1e-3」）。故 1e-3 / 1e-9 / 1e-15 三档阈值在**同一 t=6 点**触发（实测三档 `rm_iter` 全为 6，n_distinct = 1）。
2. **`bayes_iter ∈ {1,200}` 是二值桩。** 真最佳响应在**协调博弈**（本构造 `a_named > a_filler` 者）下 `br(s) = s`，从错配起点出发进入 **2-周期**、**永不收敛** —— 这正是原码把动态换成 `1 if nash else 200` 的原因。
3. **145.8× 立在上限伪影上（本件新增发现）**：`rbr_iter = 200` 是 `simulate_rbr` 的 `n_iter` **触顶值（= 未收敛）**，20/22 图取此值。V3 的收敛判据 `not switched and t>0 and len(history)>=1` 在「起点已是纳什、从未切换」时 `history` 恒空 ⇒ 永不早退 ⇒ 直接吐上限。**`rbr_multiplier = 200 / 1` 就是这么来的。**

## 3. 补审构造（沿 §1.2 #1 (a)(b)(c) 字面，0 新设阈值）

```
(a) simulate_rm 阈值 1e-3 -> 1e-9（主臂）
    + 1e-3 对照 / 1e-15 浮点极限探测 / §1.2 #1(a)「或」分支真迭代 t = n_iter   共 4 臂
(b) bayesian_nash_iter 改真 best-response 迭代：
    收敛判据 = Nash gap = max_i max(0, u_i(BR_i) - u_i(s_i)) <= ε = 1e-9；最大迭代 2000
    全因子 4 起点 {(0,0),(0,1),(1,0),(1,1)} x 2 模式 {simultaneous, alternating} = 8 格/图
    -> 22 图 x 8 = 176 格；迭代数自 1 起计（纳什条件至少核验 1 次，沿 V3「1 步到位」语义）
(c) rbr_multiplier = rbr_iter / bayes_iter_true
```

**设计口径（沿 plugin `@scientific-research-workflows` / skill `experimental-design`）**

- **区组** = 22 受控概念图；**处理** = 4 起点 × 2 BR 模式全因子，**无别名**。
- **伪重复声明**：22 图中 **10 件是 S1/S2/S6 的 `_n*` 嵌套子采样**（`S1_n35/n45/n60`、`S2_n20/n35/n45/n60`、`S6_n20/n35/n60`），**独立重复的真实层级 = 12 张基准图**。kill-line 仍按冻结的 22 图判；另报去嵌套 12 基准图口径（不参与判定）。
- **名义 N 显式标注**：`N_named` 跨 **7–59**、`N_filler` 跨 **7–59**，且 **9/22 图** 两轴分母不相等 ⇒ 跨尺寸信息不可直接逐图比较。本件按名义 N 逐图登记，**未做重采样（0 新设权）**。
- **seed** = 20260927，预登记并落盘可复算。

## 4. 补审 result（K-V3R-0-C 双口径）

### 4.1 防退化门自证（K-V3R-0-A，跑前对盘上输入字段）

| 输入字段 | n | n_distinct | std | 门（>3 且 >0） |
|---|---|---|---|---|
| `v20_field_mean_named`（盘上真实，逐图） | 22 | **18** | 0.143878 | **pass** |
| `v20_field_mean_filler`（盘上真实，逐图） | 22 | **10** | 0.079822 | **pass** |
| `deposon_freq` 派生（盘上真实，逐图） | 22 | **10** | 0.260784 | **pass** |
| *（对照）legacy `rm_iter`* | *22* | *1* | *0.0* | *退化（预期）* |
| *（对照）legacy `bayes_iter`* | *22* | *2* | *76.753227* | *退化（预期）* |

`degenerate_alarm_hit = false` ｜ **`cap_artifact_alarm_hit = true`（20/22 图 `rbr_iter ≡ 200` = 触顶值）**

### 4.2 §1.2 #1(a) RM 腿有效性（实测：**不能**解退化）

| 臂 | tol | `rm_iter` | n_distinct | std | cap 触顶 |
|---|---|---|---|---|---|
| 主臂（(a) 字面） | 1e-9 | 22/22 = 6 | 1 | 0.0 | 否 |
| V3 对照 | 1e-3 | 22/22 = 6 | 1 | 0.0 | 否 |
| 浮点极限探测 | 1e-15 | 22/22 = 6 | 1 | 0.0 | 否 |
| (a)「或」分支真迭代 | t = n_iter | 22/22 = 200 | 1 | 0.0 | **是（22/22）** |

**结论：(a) 的两个分支都无法让 `rm_iter` 获得真分布。** 如实登记为**未解除的死面**（不影响 K-V3R-1，因其判据字段是 `rbr_multiplier`；但 `rm_multiplier` 在 4 臂下仍为常量）。**未擅自增补 §1.2 未授权的构造。**

### 4.3 §1.2 #1(b) 真 best-response（176 格）

`bayes_iter_true`：**n_distinct = 3，std = 961.5760，取值 {1, 2, 2000}**。
`hit_iter_cap = 176 格中 64 格`（simultaneous 48 / alternating 16）⇒ 协调博弈 2-周期**真·不收敛**，`bayes_iter_cap_alarm_hit = true`。

### 4.4 §1.2 #1(c) `rbr_multiplier` 派生 —— **刀锋判定**

| 读数 | 定义 | n_distinct | std | 取值 | K-V3R-1（≥4 且 >0） |
|---|---|---|---|---|---|
| **主臂（literal）** | 176 格全用（触顶格按返回的 2000 计入） | **4** | 99.397538 | {0.1, 1.0, 2.0, 200.0} | **PASS** |
| **artifact-free** | 剔除 64 个真·不收敛格（余 112 格） | **3** | 69.4608 | {1.0, 2.0, 200.0} | **FAIL** |
| cap-free RBR 臂 | RBR 改真纳什收敛判据 | 6 | 0.724453 | {0.001, 0.1, 0.5, 1.0, 1.5, **2.0**} | PASS（**但倍数上界仅 2.0×**） |
| 去嵌套 12 基准图 | 按 base_graph 聚合 | 4 | 62.9000 | — | PASS（不参与判定） |

**两读数分歧（刀锋）**：`n_distinct` 恰卡在 4 / 3 的门槛上，且唯一把主臂推过 4 的取值 **0.1 = 200/2000** 正是**上限伪影格**的产物（真值应为「不收敛、倍数无定义」）。**本件 0 擅选口径**：两读数并报，合取报 `FAIL`，literal 报 `PASS`，由 PI 指定。

### 4.5 双口径判定（K-V3R-0-C）

| 口径 | verdict | 依据 |
|---|---|---|
| **新构造 verdict（主臂）** | **PASS** | K-V3R-1：`rbr_multiplier` n_distinct = 4 ≥ 4 **且** std = 99.397538 > 0 |
| **新构造 verdict（artifact-free）** | **FAIL** | 同门槛：n_distinct = 3 ≤ 3 |
| **沿原 V3 阈值字面 verdict** | **DIFFERENTIATED**（rbr_multiplier_mean = 145.8182；pa_h1 ≤ 1.3× / pa_h0 ≥ 2.0×） | 与源件逐字一致（22/22 复现） |
| **一致性** | **不一致** | 读数分歧 + artifact-free 侧 = FAIL，与原标注不同向 |

## 5. 改判动作（沿预登记 §2.3 改判规则表 + §4）

| 项 | 结论 |
|---|---|
| 命中档位 | **刀锋双读数分歧** ⇒ 不落任一档；按 §2.3 第 2 行动作执行 |
| 改判动作 | **维持原 V3 标注（不动）** + **显式登记**双读数 verdict + γ；**0 擅选口径**，待 PI 复核指定哪一读数为准 |
| γ₁ | `rm_iter ≡ 6` 系**精确零 regret** 的结构后果，§1.2 #1(a) 的 4 个臂**全部未能解除**（非阈值问题） |
| γ₂ | `rbr_multiplier_mean = 145.8182` 立在 **20/22 图 `rbr_iter ≡ 200`**（`simulate_rbr` 的 `n_iter` 触顶值 = 未收敛）之上；改用真纳什收敛判据后**真倍数上界仅 2.0×**，恰在 `pa_h0 = 2.0×` 边界 ⇒ **145.8× 不可维持** |
| γ₃ | 真 best-response 在协调博弈下**真·不收敛**（2-周期），176 格中 64 格触 2000 上限；该 64 格在 literal 读数中被赋值为 0.1×，属**上限伪影** |
| γ₄ | 22 图中 10 件为 S1/S2/S6 的 `_n*` 嵌套子采样，**独立重复真实层级 = 12 基准图**（不是 22）；名义 N 跨 7–59 且 9/22 图两轴分母不等 |
| γ₅ | 预登记 §1.2 的「v20 baselines 真缺件」与盘上实测不符（**在盘且 SHA 与源件内记值一致**）⇒ fallback 未触发；预登记 0 字节改动 |
| 若 PI 采纳 artifact-free 臂 | **§2.3 第 3 行（FAIL = 原标注维持）→ 0 改判动作** |
| 若 PI 采纳 cap-free RBR 臂 | §2.3 第 1/2 行（该臂 n_distinct = 6 但倍数上界 2.0×，实质主张仍不成立） |
| V3 原报告 | **byte 0 触动**（源件与 V3X 报告均未写） |
| 是否翻案 | **否** —— 本件只改「结论-证据关系」的登记，不重裁命题存亡（沿预登记 §5.1） |

## 6. 老实交代段

1. **0 编造**：`rbr_iter` / `rm_iter` / `bayes_iter` / 各 multiplier 全部由盘上 `deposon_v20_baselines.json` 的真实 (named, filler) 召回率经 seeded 计算得出；实现自由度（bayes 起点 4 档、BR 模式 2 档、RM tol 4 档）已逐项登记为敏感性网格；0 外部文献号新增。
2. **worker 落地选择（非阈值）**：bayes 起点集、BR 模式集、迭代数自 1 起计的计数约定、cap-free RBR 臂的存在 —— 均为**实现量**（K-V3R-0-B 管阈值不管实现），已附敏感性并留 PI 复核。**未新增任何判定阈值**。
3. **未把 §1.2 未授权的构造塞进主判据**：RBR 未被 §1.2 #1 列为重构目标，故主判据**不改** RBR（`rbr_iter` 沿 V3 冻结值）；RBR 的真收敛臂**只作敏感性、不参与判定**。同理未擅自把 (a) 扩到新阈值。
4. **刀锋不掩饰**：literal / artifact-free 两读数分别给 PASS / FAIL，本件**合取报 FAIL**、**并明示 literal 读数为 PASS**，0 择一冒充定论。
5. **预登记 SHA 列偏差未代为修订**（§1.1），字节数一致 + 内容逐字复核通过。
6. **skill**：`@scientific-research-workflows` / `experimental-design`（`SKILL.md` SHA-12 `0a314eed103a`）；本仓与 plugin-cache 均可定位，**未 fallback**，0 编造 skill 指令。
7. **succeeded ≠ 跑完**：本件以 result JSON 落盘 + hashlib SHA-12 复算 + **重跑逐字不变自证通过**为准。
8. **0 明文密钥**：`results/_v3_recheck_01_*` 三件 key 形态自扫 0 命中。

---

**PI 复核栏**：☐ 通过（指定口径：☐ literal PASS ☐ artifact-free FAIL ☐ cap-free RBR）　☐ 打回（退回重跑 / 需补构造）　签字：__________　日期：__________

出证｜Mavis 团队 worker 出件｜2026-09-27


<!-- appended-note:2026-09-30 skill 引用面复核（PI 派工第④项 · 0 删改历史字面） -->

> **附注（2026-09-30 追加 · 非原件内容）**
> 本件原引用字面**逐字保留、0 删改**；本附注**只增不改**。
>
> - **原引用面**：L143（出现 1 处）· `experimental-design`（SKILL.md SHA-12 `0a314eed103a`）；本仓与 plugin-cache 均可定位
> - **2026-09-30 只读复核**：原引用字面**2026-09-30 仍成立**（写死路径逐字在位、树哈希同目录名、`SKILL.md` SHA-12 对得上）⇒ **无过期值可改**，故仅追加注记、**不就地更新**
> - **当前三段式锚**（plugin:skill + 树哈希前 12 + SKILL.md SHA-12 + 定位方式）：scientific-research-workflows:experimental-design` · 树 ``611965fcb620`` · ``SKILL.md`` SHA-12 ``0a314eed103a`` / 13,044 B（实体直读；运行时加载行为见执行件 §6，**本棒 0 复现**）
> - **「历史实测 vs 今日实测」口径**：本件所记为**当时实测证据**，**保留有效、0 回改**；今日复核值以本附注与执行件为准，读者可据此区分二者（起因件建议 A2）。
> - **执行件**：`results/_skill_reference_update_and_user_surface_survey_2026_09_30.md` · 出件 **worker**（本棒）· **0 删改本件任何既有字节**