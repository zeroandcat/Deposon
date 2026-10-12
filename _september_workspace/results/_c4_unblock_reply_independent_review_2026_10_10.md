# 独立复核件 · codex「C4 解封回函」（机械复核 ＋ 影响面扫描）

> **件名**：`results/_c4_unblock_reply_independent_review_2026_10_10.md`
> **被验对象**：`letters/_codex_c4_values_unblock_reply_2026_10_10.md`（SHA-12 `a975c7990cd8` · 21,486 B · 143 行）
> **委托件**：`letters/_commission_c4_values_unblock_EN_2026_10_10.md`（SHA-12 `fde64a863b09` · 10,244 B · 83 行）
> **复核棒**：Verifier（独立棒）· **日期**：2026-10-10（Asia/Shanghai）
> **一句话结论**：数学机械层面 **10 项断言 10 MATCH / 0 MISMATCH**；引证准确性与自述一致性 **6/6 相符**；所附脚本六项检查静态通读相符、实跑 **6/6 OK**；三处更正之影响面共登记 **25 处**（**21 处判为直接错误或需勘正**、**4 处建议维持**）。⛔ 本件 0 采认、0 判理论正确性、0 勘正、0 回改任何既有件。

---

## §0 边界声明（本件自限，与委托一致）

| # | 边界 | 本件遵守情况 |
|---|---|---|
| B1 | ⛔ 0 采认 / 0 判档 | 本件为独立复核意见，**不构成采认**；采纳与否归 PI / 学术判断 |
| B2 | ⛔ 0 判理论正确性 | 只做**机械层**（有限合成枚举、有理数恒等式、引证逐字核对）；`u*=1` 之类取值是否适合五族，属学术判断，**本件不裁** |
| B3 | ⛔ 0 改阈值 / 0 回改既有件 | 全程只读；**唯一写动作＝新建本件**（落前 `Test-Path=False`，`results/*independent_review*` 与 `results/*c4_unblock*` glob 均 0 命中） |
| B4 | ⛔ 0 跑项目 executor | 仅运行外部路径所附合成脚本 `verify_c4_originated_math.py`，及本棒自建合成脚本（系统临时目录） |
| B5 | R4 · 0 网络 / 0 skill / 0 LLM 调用 | 无任何网络请求、无 skill 调用、无模型调用；全部为本地文件读取与本地 Python 运算 |
| B6 | 临时件可恢复删除 | 本棒自建两脚本落 `$env:TEMP\verify_c4_indep_2026_10_10\`（仓外）；仓内 **0** 落任何临时件 |
| B7 | ⛔ 0 触及 `D:\私人资料\_non_upload_local_archive` | 全程未访问该路径 |
| B8 | 命名合规 | 无 `_v5_` / 阶段号前缀；`_主题_日期` 式，遵 2026-09-29 命名裁 |

---

## §1 盘上实况与时序异常（如实登记）

1. **仓内副本状态**：委托描述仓内副本「可能已由并行棒落仓」。**首次探测（本次复核开始时）`Test-Path=False`**，其后在复核过程中该文件出现 ⇒ **并行棒于本次复核期间落仓**。
2. **落仓一致性已验**：仓内副本与外部原件 **SHA-12 同为 `a975c7990cd8`、同为 21,486 B** ⇒ 逐字节一致，**被验对象无歧义**。所附脚本同样一致（仓内 `letters/verify_c4_originated_math.py` 与外部件同为 `3042cf59448e` / 4,115 B）。
3. **并行编辑仍在进行**：`results/_codex_c4_values_unblock_reply_intake_register_2026_10_10.md` 于本次复核期间两次探测指纹不同（`a5c493094ef2` / 27,099 B → `a2d7f86d72e5` / 27,100 B）⇒ **该登记册仍在被并行棒改动**；本件所引其指纹为**快照值**，不保证其后不变。

---

## §2 指纹核验（被验件所引七份材料，实测全部相符）

| # | 材料 | 路径 | 回函所标 SHA-12 | 实测 SHA-12 | Bytes | 结论 |
|---|---|---|---|---|---|---|
| 1 | 解封委托信 | `letters/_commission_c4_values_unblock_EN_2026_10_10.md` | `fde64a863b09` | `fde64a863b09` | 10,244 | ✅ 相符（且确为 **83 行**，与回函「full 83-line」自述相符） |
| 2 | P-B V0 spec | `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | `423c84de20d5` | `423c84de20d5` | 15,457 | ✅ |
| 3 | 首值委派信 | `letters/_commission_c4_values_EN_2026_10_10.md` | `a397621085d6` | `a397621085d6` | 56,217 | ✅ |
| 4 | 首次回函（更正对象） | `letters/_codex_theory_derivation_reply_2026_09_30.md` | `7558eb1a5e34` | `7558eb1a5e34` | 71,002 | ✅ |
| 5 | C4 勘误登记册 | `results/_c4_theory_source_caliber_correction_2026_09_30.md` | `61b139efd0ef` | `61b139efd0ef` | 25,022 | ✅ |
| 6 | 预登记验收清单 | `results/_v5_item21_rerun_conditions_prereg_2026_09_28.md` | `4185bdad6df5` | `4185bdad6df5` | 31,429 | ✅ |
| 7 | Bayesian 基线设计稿 | `results/_bayesian_baseline_design_2026_10_10.md` | `7e181a167702` | `7e181a167702` | 29,783 | ✅ |

全部为 **no-BOM · LF（CRLF=0）**。

---

## §3 数学机械复核结论表（逐项 MATCH／MISMATCH）

| # | 断言（回函出处） | 结论 | 复核依据（我方独立路径） |
|---|---|---|---|
| M1 | L30–36：非空 `K_t` 时 `u_t(a;K_t)=1[a∈K_t]`，故 `u*=max_a u=1`（全域） | **MATCH** | 独立枚举 15 个非空掩码 1–15：`max_a u == 1` 全 15/15；各动作支付 ∈ {0,1} 全 15/15 |
| M2 | L33 / L42–48 表：`max_u(T)=1`（T1–T5 五族） | **MATCH** | 论证**仅依赖 `K_t` 非空**、与族名无关 ⇒ 五族同得 1；不需由任务名或模型性能选值。条件（G1：四动作齐备；G2：`K_t` 非空；G3：M1 不改键/不移除动作）由回函 L36/L40 自陈且本件实测与之一致 |
| M3 | L93–97：T-2 条件下界式 `L = Σ_t[1 − Σ_z max_a Σ_{x: a∈K_t(x)} P_t(x,z)]` | **MATCH** | 独立实现 vs「逐观测全动作枚举取最大值」：在 codex 的 **4,996 例**空间 **0 例不等**；另加**我方自建随机扫描 4,000 例**（2–5 状态、1–3 观测、任意非空键集、有理概率）**0 例不等** |
| M4 | L99：「与 all deterministic policies 等价／最大化选择可取到 ⇒ 是最小值而非仅非负下界」 | **MATCH** | 4,996 例中逐例枚举**全部**观测→动作映射取最小值，与公式逐例相等；**随机化不可改进**另经我方 C3（300 例、每观测 2 点有理混合全枚举，含全部顶点）实测 **0 违例** |
| M5 | L113：M3 均匀策略期望式 `D = E[Σ_t (1 − \|K_t\|/4)]` | **MATCH** | 轨迹级穷举（4^H 条轨迹）混合键 `[1,15,3,7]`、H=4 ⇒ 枚举期望 **3/2**，与 `Σ_t (1 − \|K_t\|/4)` **精确相等** |
| M6 | L113：固定 H 且每决策恰一接受键 ⇒ `3H/4` | **MATCH** | H=4 轨迹级穷举 ⇒ **3** ＝ 3H/4（M5 的特例，非独立假设） |
| M7 | **更正①** L121：聚合域为 `[0,H]`（非 `[0,1]`）；两次拒绝 ⇒ `D=2`；且仅付上界无下界 ⇏ 单项 ≤1 | **MATCH** | H=2 **全轨迹穷举**：`0 ≤ D ≤ H` 违例 **0**，可达最大 **D=2**；反例 `D=2` 复现。「无下界 ⇏ 单项 ≤1」在 `u∈[0,max_u]` 之外机械成立（取 `u<0` 即单项 >1） |
| M8 | **更正②** L123–129：`(G_L/c)/max(G_B/c,ε) = G_L/max(G_B, c·ε)`；消去**仅**在 `G_B ≥ c·ε`；`G_B=0` 时归一化子留存；例 `G_L=2,G_B=0,ε=0.1` ⇒ c=1 得 **20**、c=2 得 **10** | **MATCH** | **750 组**有理元组（`G_L∈0..5`、`G_B∈0..4`、`c∈{1/2,1,2,3,10}`、`ε∈{1/10,1/2,1,2,5}`）恒等式 **0 失败**；无护栏支 `G_B≥cε`：**比值对 c 不变** 0 违例；护栏支 `G_B<cε`：**比值随 c 严格递减** 0 违例；数值例复算 **20 / 10** 与回函一致 |
| M9 | **更正③** L131：同键双态（`K={1}`）常数选择动作 1 ⇒ **零后悔** | **MATCH** | 两隐态同键 `K={1}`、单观测 ⇒ 公式与枚举同为 **L=0**；对照：两态异键 `K={1}`/`K={2}`、同一观测 ⇒ **L=1/2**（符合预期） |
| M10 | **更正③** L131：同时驳倒原回函**无条件两位阈值**（`log₂4`） | **MATCH** | 上述同键双态例中**观测熵＝0 bit ＜ log₂4＝2 bit**，而 **L=0** ⇒ 「容量低于阈值 ⇒ `L>0`」被反例推翻。另实测「`L=0` ⇔ 每个正概率观测的支撑上存在共同接受键」在 **2,000 例**随机有限域上 **0 违例**，与回函 L101 之判据表述相符 |

**计数：MATCH 10 · MISMATCH 0。**

### §3.1 附带边界用例（我方补测，5 组全通）

| 用例 | 内容 | 读数 | 意义 |
|---|---|---|---|
| E1 | 观测含**零概率**取值 | 公式＝枚举＝1/2 | 零质量观测 **不产生幽灵惩罚**（`max` 对空和取 0 ⇒ 贡献 0），公式对退化分布良定义 |
| E2 | 单隐态、单观测 | 0 | 与「非空 ⇒ 可取 1」一致 |
| E3 | 两态键均为全集 `K=A` | 0 | 全接受 ⇒ 零后悔 |
| E4 | 两态键不相交、单观测 | 1/2 | 单步后悔可达上界之半数（4 态单例键时可达 3/4） |
| E5 | 15×15 键对全域 | `L ≥ 0` 全真 | 非负性全域成立 |

---

## §4 引证准确性与自述一致性核验（6/6 相符）

| # | 回函主张 | 实测 | 结论 |
|---|---|---|---|
| C1 | 更正① 引 `7558eb1a5e34` **L668** | 该行逐字载「**M-2** … each summand lies in `[0,1]`, so `D(M,T) ∈ [0,1]` and the bracket `[L,U]` lives on a normalized scale」 | ✅ 引证准确 |
| C2 | 更正② 引 **L681–700** | L681 载标题「**(1) `max_u` cancels out of the primary metric.**」；**L686 自陈显示式分子仍含 `/max_u`** ⇒ 该回函**结论与其自列公式自相矛盾** | ✅ 引证准确，且**更正成立**（我方复算见 M8） |
| C3 | 更正③ 引 **L423–435** | L423「**`L(M,T) = 0` exactly where the mechanism is identifiable at that capacity.**」；L429「if they do not suffice, some distortion is forced and `L(M,T) > 0`」 | ✅ 引证准确 |
| C4 | 更正③ 引 **L392–398** | L392 D-4「a capacity below `log₂4` cannot identify `a*_t` at all」；L395–398「…which by §2.4(2) drives `L > 0`; at or above it, `L = 0`」 | ✅ 引证准确 |
| C5 | 更正② 并称首值委派 **L170** 重复该错误 | `a397621085d6` L170 逐字载「**`max_u` cancels exactly out of the primary multiplier**」 | ✅ 引证准确 |
| C6 | 「The governing algebra is the spec's lines 61–68」 | spec L61＝`D(M,T)=E_π[Σ_t \|u*−u\|/max_u]`；L66＝`max_u` 为支付上界；L68＝`失真倍数 = D_LLM / max(D_Bayesian, ε)` ⇒ 治理代数三式齐备于 L61–68 | ✅ 相符 |

**另核（附带）**：回函 L16 对 spec 的描述（4 动作／3 机制／5 族／归一差之和／`L`,`U` 之命名依据）与其所引 L39–76 范围逐字相符；L50 引 L53–54（T4/T5 未定细节）、L115 引 L39–46（零失真 Bayesian 基线＋M3 均匀采样）均相符。

---

## §5 所附脚本复核（`verify_c4_originated_math.py`）

### §5.1 静态通读（先读后跑）

| # | 检查项（对应回函 L137 自述六项） | 静态核对 | 备注 |
|---|---|---|---|
| S1 | 「checked the proposed payoff extrema for all 15 nonempty keys」 | `test_every_nonempty_key_has_exact_optimum_and_bound_one`：`mask ∈ range(1,16)`，`max(rewards)==1` 且各值 ∈ {0,1} | ✅ 对应 |
| S2 | 「the conditional minimum against all observation-based deterministic policies in **4,996** finite examples」 | 例数＝4^4×2^4 ＝ 4,096 ＋ 15²×2² ＝ 900 ＝ **4,996**；`assertEqual(count, 4996)` 硬断言 | ✅ 我方独立重算同值 |
| S3 | 「the M3 expectation」 | `test_uniform_action_identity_for_every_key`：逐掩码验 `mean(1−payoff)=1−\|K\|/4`，附 `3/4` 与全接受键检查 | ✅ 对应（另见下 §5.2 之实现脆弱点） |
| S4 | 「the cumulative range counterexample」 | `test_two_normalized_errors_are_not_bounded_by_one`：`sum(1−payoff(a,1) for a in (1,2)) == 2` | ✅ 对应 |
| S5 | 「the guarded-ratio algebra」 | `test_guarded_ratio_algebra_and_noncancellation`：恒等式网格 ＋ 例 `2/0.1=20`、`2/0.2=10` | ✅ 对应 |
| S6 | 零信息仍可零后悔（M9 之反例） | `test_no_information_can_still_allow_zero_regret`：同键双态 ⇒ 0；异键 ⇒ 1/2 | ✅ 对应 |

**静态通读发现（不构成数学错误，仅登记）**：
- **N1（脆弱性）** S3 末两行 `self.assertEqual(expected, 0)` 依赖 `for` 循环变量 `expected` 的**泄漏作用域**；虽通过，但若循环体被改写即失效。
- **N2（覆盖面）** 4,996 例仅含两类配置：**单例键 × 4 观测**、**任意键对 × 2 观测**；不含 ≥3 状态且非均匀观测的情形 ⇒ 覆盖面窄于我方 §3 之随机扫描。
- **N3（表述）** 回函 L137 称「All six checks passed」——六项与脚本六项**一一对应**，无夸大。

### §5.2 实跑（本地、只读、无项目 executor）

- 环境：Python **3.14.7**（`C:\Python314\python.exe`）；工作目录＝外部路径 `c4_values_reply_2026_10_10`。
- 结果：`Ran 6 tests in 3.819s` → **`OK`**（6/6 通过）。
- 副作用核查：脚本仅 import `fractions` / `itertools` / `unittest`，无本地模块 import ⇒ **未生成 `__pycache__`**；未读写仓内任何文件。

---

## §6 影响面清单（0 回改 · 仅登记 ＋ 拟勘正路径）

> 全仓检索面：`cancels (out|exactly)`、`cancellation`、`[0,1]`、`D(M,T) ∈`、`normalized scale`、`log₂4` / `log2` / `2 bit` / `两位`、`identifiable` / `non-identifiable` / `机制可辨识`、`L(M,T) = 0`、`相消 / 消去 / 抵消`、`max_u`、`sum of normalized` / `each summand` 等中英双语模式 ＋ glob；命中逐条人工判别（多数 `[0,1]`/`bit` 命中属指纹学、融合权重等无关域，已剔除）。
> **代码面结论**：`max_u` 全仓命中均为 markdown 或 spec 公式字面；`tools/distortion_calculator.py` **盘上不存在**（与既有登记一致）⇒ **三处更正 0 代码落点**。

### §6.1 更正①（聚合域 / `D ∈ [0,1]`）— 4 处

| # | 件 · 行 | 原文摘录 | 受影响类型 | 建议处置 ＋ 理由 |
|---|---|---|---|---|
| ①-1 | `_codex_theory_derivation_reply_2026_09_30.md` `7558eb1a5e34` **L208** | 「**P3** · Range consistency. `max_u` is a true upper bound on `u`, so each summand lies in `[0,1]`.」 | **前提项，单项界在 `0≤u≤max_u` 下成立** | **维持原文**；仅在勘正件登记「单项界 ⇏ 聚合界」。理由：被更正者为其**推论**，非此行本身 |
| ①-2 | 同件 **L668** | 「each summand lies in `[0,1]`, so `D(M,T) ∈ [0,1]` and the bracket `[L,U]` lives on a normalized scale」 | **直接错误**（聚合推论忽略求和） | **另名勘正**：`D` 域为 `[0,H]`；连带「`[L,U]` lives on a normalized scale」字面须改述（尺度同构仍在，区间宽度变） |
| ①-3 | 同件 **L493** | 「a **threshold on the same `[0,1]`-normalized scale that `D` lives on**」 | **受影响推论**（尺度字面） | **另名勘正**：`[0,1]` → `[0,H]`。理由：同尺度**读法本身**不因本更正失效，仅**字面区间**错误 |
| ①-4 | 同件 **L502–504** | 「*Flagged:* that `U` shares `D`'s normalized scale is my reading, required for the comparison…（此处我用了额外假设）」 | 假设声明 | **维持**。理由：已显式标注为额外假设，与本更正无冲突 |

### §6.2 更正②（`max_u` 精确消去）— 13 处

| # | 件 · 行 | 原文摘录 | 受影响类型 | 建议处置 ＋ 理由 |
|---|---|---|---|---|
| ②-1 | `7558eb1a5e34` **L220–223** | 「the multiplier `D_LLM / max(D_Bayesian, ε)` … and **`max_u` cancels exactly out of that ratio** — it appears in numerator and denominator identically」 | **直接错误** | **另名勘正**：分子含 `/c`、分母在护栏支为 `ε` ⇒ `c` 不消 |
| ②-2 | 同件 **L681–700** | 「**(1) `max_u` cancels out of the primary metric.**」＋ **L686** 显示式 `失真倍数 = D_LLM / ε = ( E_π[Σ_t \|u*−u\|/max_u] ) / ε` | **直接错误**，且**与其自列公式自相矛盾** | **另名勘正**（本条为该主张之**首发处**，优先级最高） |
| ②-3 | 同件 **L795–799** | 「But `max_u` **cancels exactly out of the primary metric** … So the multiplier clause of the verdict is **independent of T-4**」 | **直接错误** ＋ **导出实务结论**（T-4 对乘子无影响） | **另名勘正**：须连带撤回「independent of T-4」之实务读法 |
| ②-4 | 同件 **L940** | 表行 T-4：「F-1 (upstream) — but **cancels out of `mean_mult`**」 | **直接错误**（表格式转述） | **另名勘正** |
| ②-5 | 同件 **L954–956** | 发现②：「**`max_u` cancels exactly out of the primary metric** … blocks no part of `mean_mult`」 | **直接错误**（列为「genuinely derived」之三条结果之一） | **另名勘正**：该条须降级为「有条件成立（仅无护栏支）」 |
| ②-6 | `_commission_c4_values_EN_2026_10_10.md` `a397621085d6` **L55** | 「⚠️ **Note the measured finding that `max_u` cancels exactly out of the primary multiplier** (§2.7 result 2) — that does **not** make T-4 optional」 | **我方件重复该错误**（新回函已点名此面） | **另名勘正**（我方件）：补记「该发现已被 10-10 回函更正」 |
| ②-7 | 同件 **L76** | 表：「upstream `u` — but **cancels out of the multiplier**」 | **我方件重复** | **另名勘正** |
| ②-8 | 同件 **L170** | 「**`max_u` cancels exactly out of the primary multiplier** ⇒ T-4's absence blocks no part of the multiplier」 | **我方件重复**（新回函点名之「erroneous cancellation claim」原句） | **另名勘正**（我方件） |
| ②-9 | 同件 **L38**（H9 条款） | 「⛔ 0 report that `max_u` cancels out (§2.7) **without** reporting that `U` does not」 | **引用面**（纪律条款本身有效） | **维持条款结构**；勘正件补注其所指结果已被更正。理由：H9 为「0 半面结论」之纪律，非事实主张 |
| ②-10 | `_c4_reply_intake_acceptance_register_2026_10_01.md` `91e3d7a03155` **L116** | 表行 T-4：「but **cancels out of `mean_mult`** (§4.3(1))」 | **直接错误**（采认登记面转述） | **追加式勘误候 PI 裁**。理由：该件已「采认入库」，改写须保全历史留痕 |
| ②-11 | 同件 **L141** | 照录发现②原文：「**`max_u` cancels exactly out of the primary metric**…」 | **直接错误**（逐字照录面） | **追加式勘误候 PI 裁** |
| ②-12 | 同件 **L143** | 释义：「`max_u` 于**主度量整项抵消**——T-4 之缺席…**0 阻断** `mean_mult` 之任何部分」 | **释义面被实质推翻** | **追加式勘误候 PI 裁**（释义为本棒自撰，非原文，勘正成本较低） |
| ②-13 | `查理_deposon双主线论文终稿_2026-10-01_v0.3.md` `fd39cf811232` **L536** | 「…`max_u` 在量纲归一中**精确相消**……」 | **对外/论文面中文转述** | **⛔ 本件 0 处置；候 PI 裁**。理由：属 PI 面委托/论文件，且原文已自带「回函自述，无法核实」待核标注 |

### §6.3 更正③（非辨识 ⇒ `L>0` ／ 两位阈值）— 7 处

| # | 件 · 行 | 原文摘录 | 受影响类型 | 建议处置 ＋ 理由 |
|---|---|---|---|---|
| ③-1 | `7558eb1a5e34` **L392**（D-4） | 「L40 fixes `\|A\| = 4`; a capacity below `log₂4` cannot identify `a*_t` at all」 | **过强断言**（容量单值 ⇏ 可辨识性） | **另名勘正**：容量须与键结构**联合**方可推可辨识性 |
| ③-2 | 同件 **L395–398** | 「…makes `a*_t` unidentifiable, which by §2.4(2) drives `L > 0`; at or above it, `L = 0`」 | **直接错误**（反例：C=0 < 2 bit 而 L=0） | **另名勘正** |
| ③-3 | 同件 **L423–435** | 「**(2) `L(M,T) = 0` exactly where the mechanism is identifiable at that capacity.**」＋ L429「…`L(M,T) > 0`」 | **直接错误**（本更正首发处） | **另名勘正**（优先级最高） |
| ③-4 | 同件 **L959** | 发现③：「`L(M,T) = 0` exactly where the mechanism is identifiable (§2.4(2)) is the one **cell-level acceptance test** the eventual `L` formula must pass」 | **直接错误 ＋ 危险推论**：若被当作**否决工具**，将误否决**合规**之 `L` 公式 | **另名勘正** ＋ **显式标注该「验收测试」已作废** |
| ③-5 | `a397621085d6` **L171** | 「`L(M,T) = 0` exactly where the mechanism is identifiable is the one cell-level acceptance test an eventual `L` formula must pass」 | **我方件重复** | **另名勘正**（我方件） |
| ③-6 | `91e3d7a03155` **L147** | 照录发现③原文（同 ③-4） | **直接错误**（照录面） | **追加式勘误候 PI 裁** |
| ③-7 | 同件 **L149** | 释义：「`L(M,T)=0` 当且仅当该格机制可辨识…为将来公式须通过之一格级验收测试」 | **释义面被实质推翻** | **追加式勘误候 PI 裁** |

### §6.4 已由并行登记面覆盖（0 待勘正）— 1 处

| # | 件 · 行 | 内容 | 状态 |
|---|---|---|---|
| D-1 | `results/_codex_c4_values_unblock_reply_intake_register_2026_10_10.md`（快照 `a2d7f86d72e5` / 27,100 B）**L144–145 / L181–188 / L228** | 已照录三处更正（含恒等式与数值例）、已逐条核「原件是否载该主张」、并在 **L228** 载「三处更正之影响面**另由独立复核件在办**」 | **面已闭**：登记面本身**未复述**三处错误主张（仅作更正之转述）⇒ **0 待勘正**；**本件即其指向之复核件** |

**影响面合计：25 处 = 更正① 4 ＋ 更正② 13 ＋ 更正③ 7 ＋ 已闭 1。其中判为「直接错误/需勘正」21 处（①-2、①-3 ＋ ②-1…②-8、②-10…②-12 ＋ ③-1…③-7），建议「维持」4 处（①-1、①-4、②-9、D-1）。**

---

## §7 出口（Exits · 仅建议，⛔ 0 执行）

| # | 出口 | 拟处置路径 | 归属 |
|---|---|---|---|
| E1 | **我方件的重复面**：`a397621085d6` L55/L76/L170/L171 共 4 处 | 建议**另名勘正件**（沿「0 回改 ＋ 追加式」惯例），逐处标「已被 10-10 回函更正」 | 建议 PI 裁后派棒 |
| E2 | **09-30 回函本体**：`7558eb1a5e34` 11 处（L208/L392/L395–398/L423–435/L493/L681–700/L795–799/L940/L954–956/L959） | 建议**另名勘正件**；其中 L208、L502–504 建议**维持不改**（前提与假设声明） | 建议 PI 裁后派棒 |
| E3 | **已采认登记册** `91e3d7a03155` 5 处（L116/L141/L143/L147/L149） | 建议**追加式勘误**（保全「采认 ≠ 背书」与历史留痕） | **候 PI 裁**（该件属采认面） |
| E4 | **论文/委托面** `fd39cf811232` L536 一处中文转述 | ⛔ **本件 0 处置**；对外件改动须先经 PI | **候 PI 裁** |
| E5 | **更正③的次生风险**：`L=0 ⇔ 可辨识` 若已被用作**否决工具** | 建议在勘正件中**显式作废该「验收测试」**，避免误否决合规 `L` 公式 | 建议 PI 裁后派棒 |
| E6 | **本件之性质** | 本件为独立复核，**不构成采认**；三处更正是否成立于学术层面、其原始定义是否可辨识，**归 PI / 学术判断**，本件 ⛔ 0 判 | PI |

---

## §8 诚实限制

- **L1（理论层未裁）**：`u*=1` / `max_u=1` 属**前瞻性设计约定**（二元评分 ＋ 满信息 oracle）。其是否适合 T1–T5、为 T4/T5 选择何种键，均属学术与建模判断，**本件不裁**（B2）。机械层只验证「在其自陈条件下算术自洽」。
- **L2（有限域实测 ≠ 一般证明）**：一般性论证（最大值可取、随机化不可改进、`D = E[Σ(1−|K_t|/4)]` 的期望可加性）由回函承担；本件只在**有限合成域**内实测（M3/M4/M5 + 4,000 例随机扫描 ＋ 2,000 例判据扫描）。
- **L3（容量仅在退化通道实测）**：`C(Q)=0` 仅经**单观测通道**（观测熵＝0 bit）实测；**未**验证一般 `C(Q)=sup_p I_p` 的数值或存在性。
- **L4（实例键未核）**：`K_t` 在真实任务数据上能否**非空实例化**，属数据面；回函亦未提供实例键，本件 **0 提供**。
- **L5（并行并发）**：`7558eb1a5e34` 等既有件于本次复核期间**未被触动**（本棒全程只读）；但**并行棒仍在改动** `results/_codex_c4_values_unblock_reply_intake_register_2026_10_10.md`（两次探测指纹不同）⇒ 本件对该件的引用为**时点快照**。
- **L6（本棒自身两处 harness 缺陷，如实登记）**：我方独立脚本 **rev1** 曾误报 `C3 violations=173` 与 `C4 M3=192`。追查结论：**均为我方脚本缺陷，非被验件缺陷** —— (i) `brute_rand` 以 `zip` 将混合权重与策略索引**错位配对**，构造出非凸组合；(ii) `m3` 对轨迹期望**重复除以 4**（既乘 1/4 又除以 4^H）。修正后复跑：**C3 violations=0**、`C4` 得 **3** 与 **3/2**，与回函一致。**登记此事以免「首跑红灯」被误读为被验件缺陷。**
- **L7（检索非穷尽）**：`grep`/`glob` 按工具默认规则排除部分忽略目录与二进制；`.tmp/` 下历史脚本的**注释面**若另有同类转述未逐一判读（属临时件，非权威面）。已判读的命中面未发现遗漏的权威落点。
- **L8（未做之事）**：⛔ 0 运行项目 executor、⛔ 0 触及 `_non_upload_local_archive`、⛔ 0 网络 / 0 skill / 0 LLM、⛔ 0 改任何既有件、⛔ 0 采认、⛔ 0 改阈值。
- **L9（本件自身指纹）**：本件字节指纹于**落盘后**于交付回执中实测自报（仓内惯例：指纹报于件外）。

---

## §9 边界遵守自证

| 自证项 | 证据 |
|---|---|
| 落前撞名检查 | `Test-Path 'results/_c4_unblock_reply_independent_review_2026_10_10.md'` ＝ **False**；`results/*independent_review*`、`results/*c4_unblock*` glob 均 **0 命中** ⇒ ✅ 新名新建 · 0 覆写 |
| 0 回改既有件 | 全程仅 `Read` / `Grep` / `Glob`；**唯一写**为新建本件。既有件中仅本棒自建脚本落**仓外**系统临时目录 |
| 0 跑 executor | 仅运行：① 外部路径所附 `verify_c4_originated_math.py`（合成数学）② 仓外临时目录内本棒自建 `indep_c4_check.py`、`edge_c4_check.py`（合成数学） |
| 命名合规 | `_c4_unblock_reply_independent_review_2026_10_10.md` —— 无 `_v5_`／无阶段号首段，符合 2026-09-29 命名裁 |
| 临时件可恢复删除 | `$env:TEMP\verify_c4_indep_2026_10_10\{indep_c4_check.py, edge_c4_check.py}`，仓外，可按需恢复删除 |

---

## §10 指纹自报（输入侧实测 · 2026-10-10）

| 角色 | 件 | SHA-12 | Bytes |
|---|---|---|---|
| 被验回函（仓内副本） | `letters/_codex_c4_values_unblock_reply_2026_10_10.md` | `a975c7990cd8` | 21,486 |
| 被验回函（外部原件） | `…\codex-workspace\c4_values_reply_2026_10_10\_codex_c4_values_unblock_reply_2026_10_10.md` | `a975c7990cd8` | 21,486 |
| 所附脚本（仓内副本） | `letters/verify_c4_originated_math.py` | `3042cf59448e` | 4,115 |
| 所附脚本（外部原件） | `…\verify_c4_originated_math.py` | `3042cf59448e` | 4,115 |
| 委托件 | `letters/_commission_c4_values_unblock_EN_2026_10_10.md` | `fde64a863b09` | 10,244 |
| 更正对象（09-30 回函） | `letters/_codex_theory_derivation_reply_2026_09_30.md` | `7558eb1a5e34` | 71,002 |
| 首值委派信 | `letters/_commission_c4_values_EN_2026_10_10.md` | `a397621085d6` | 56,217 |
| 采认登记册 | `results/_c4_reply_intake_acceptance_register_2026_10_01.md` | `91e3d7a03155` | 23,591 |
| 并行登记册（快照 · 仍在变动） | `results/_codex_c4_values_unblock_reply_intake_register_2026_10_10.md` | `a2d7f86d72e5` | 27,100 |
| 论文/委托面（中文转述面） | `letters/查理_deposon双主线论文终稿_2026-10-01_v0.3.md` | `fd39cf811232` | 236,425 |
| 本棒自建临时脚本（仓外） | `indep_c4_check.py` / `edge_c4_check.py` | 见交付回执 | — |

**本件自身 SHA-12 / bytes / BOM / CRLF 于落盘后实测自报于交付回执（件外）。**

**复核件终。⛔ 0 采认 · 0 判档 · 0 改阈值 · 0 回改任何既有件。**