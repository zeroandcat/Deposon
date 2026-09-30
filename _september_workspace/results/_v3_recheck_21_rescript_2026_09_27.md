# V3-R 改判件 #21 · KT-B1 失真上界重评（三面并报）· worker · 2026-09-27

> **性质**：V3-R 预登记 v1.1（`bcc3cee23e82`）**第三梯队 B 棒执行棒产出**；执行棒只按 K-V3R-21 字面 + 提案 A/B/C 冻结算式跑，0 私设条款
> **上游输入（只读，0 触动）**：`_v3_recheck_prereg_v1p1_2026_09_27.md` §1.2（量纲互斥声明）/§2.2 K-V3R-21/§2.3 TH-V3R1P1-21-*/§2.4 提案 A·B·C；`_v3_n_recheck_llm_verdict_2026_09_27.md` §三条；`_v3_n_ktb1_distortion_bound_data_2026_09_27.json`（`26c0d0b0ffb6`）
> **产出件**：`deposon_team/plugins/_v3r1p1_21_ktb1_distortion_2026_09_27.py`（executor）+ `results/_v3_recheck_21_result_2026_09_27.json`（三面 + γ 清单）
> **0 LLM / 0 proxy / 0 key 读取**；派生 JSON 0 合并；既有件 0 字节改动

> ### ⚠ 量纲互斥硬声明（防误导，冻结）
> `D_dec` 是**决策不一致率**量纲；`0.0004 / 0.0028 / 0.4634` 是 **D(M,T) 失真上界**量纲。
> **二者不可并排比大小。** 面 3 只作（a）deposon 侧非恒等可算面、（b）臂间自对照序；
> **不得**据此宣称 deposon 优于/不优于 OT·KD·LLMLingua。

---

## §1 原结论（沿既有件字面，0 改动）

源件 `results/_v3_n_ktb1_distortion_bound_data_2026_09_27.json`：

| 项 | 沿用值 |
|---|---|
| `measured_deposon_distortion_bound.value` | `2.220446049250313e-16` = 2⁻⁵²（IEEE 754 双精度 eps） |
| 占位 0.5 / 0.05 | **已被实测值替换**（占位问题解除） |
| 通用基线报告值（`baef94e393de`） | B1 `0.0004` / B2 `0.0028` / B3 `0.4634` |
| 通用基线可复算性 | `generic_bound_recomputable = false`（脚本本仓缺失） |
| `outcome.item_21_recommendation` | 仍标「不明」，根因 = 测法轴结构性恒等 + 资产缺口 |

**死因（两条，本件分别处置）**：
1. **测法轴恒等**（面 1）：`T+R+A ≡ 1` 是构造恒等 ⇒ 残差 2.22e-16 **不含任何关于信息失真的证据** ⇒ 无鉴别力；
2. **资产缺口**（面 2）：3 个 BOSS 脚本 + `tools/distortion_calculator.py` 本仓缺失 ⇒ 通用基线侧不可复算、deposon 侧 D(M,T) 不可算。

---

## §2 三面并报（0 合并）

### 面 1 · 恒等口径（对照留档）

| 项 | 值 |
|---|---|
| 复算 max_deviation（`conservation.check_conservation_graded(v19, v19)`） | **`2.220446049250313e-16`** |
| 在盘 `physics_audit.t_plus_r_plus_a_max_deviation` | `2.220446049250313e-16`（**逐位相同**，`stored_vs_recomputed_match = true`） |
| 守恒容差（`TH-V3R1P1-21-c`） | `1e-6` ⇒ PASS |
| 受检记录数 | 1,592 |
| 鉴别力 | **无**（＝2⁻⁵² 双精度舍入极限；`T+R+A≡1` 构造恒等）⇒ 承原结论，0 改判 |

### 面 2 · 原 D(M,T) 口径 · **通用基线侧**（以漂移版实现复算，K-V3R1P1-0-G）

回填源 = 仓外 `_non_upload_local_archive/scripts/scripts/kt_b1/` 3 件（**只读取用，0 复制入仓**）：

| BOSS | 锚版 SHA-12（**全仓 0 命中**） | 回填件（漂移版）SHA-12 / 字节 | 报告值 | **复算值** | 相对偏差 | ±5% 窗 | 复现 |
|---|---|---|---|---|---|---|---|
| B1 Sinkhorn OT | `19325960b8be` | `7c2b41c008a5` / 16,404 B | 0.0004 | **0.00044522183946429185** | **+11.31%** | [0.00038, 0.00042] | ❌ **超差** |
| B2 KD | `1781ea2f742d` | `8c6e98034005` / 15,677 B | 0.0028 | **0.002813601952161043** | +0.486% | [0.00266, 0.00294] | ✅ |
| B3 LLMLingua | `c0b55e0385a4` | `2ded5cf0e863` / 15,389 B | 0.4634 | **0.46342184490589095** | +0.0047% | [0.44023, 0.48657] | ✅ |

- **(a) 判据 3/3 ±5% ⇒ 实得 2/3 ⇒ 不满足**（唯一超差项 B1）
- **B1 超差的机械登记（0 擅改容差、0 改判）**：报告值 `0.0004` 仅 **4 位小数**显示，±5% 相对窗半宽仅 `2.0e-05`，**窄于显示粒度半步 `5e-05`**；实测绝对差 `4.52e-05` **小于**显示半步 ⇒ 数值与「报告值 = 四舍五入到 4 位小数」自洽，但**机械按相对容差判即超差**。两读并报，判定取机械读。
- **B1 reg 扫描全档（冻结超参 reg=0.1 为判读点）**：`0.001→1.75e-07`、`0.005→2.17e-06`、`0.01→1.47e-05`、`0.05→1.24e-04`、**`0.1→4.45e-04`**、`0.5→2.38e-03`（对 reg 单调）
- **B1 记录数事实登记**：漂移版实抽 **995** 条（E9.3 两基准 × 5 臂 × 99~100），与脚本 docstring/常量 `N_QUESTIONS=200` 不一致 ⇒ **0 归因、0 编造差异说明**
- **脚本内部裁定（用其自带占位 deposon 值，仅登记 0 主张）**：B1 `GRAY_BOTH_BELOW`、B2 `GRAY_BOTH_BELOW`、B3 `GRAY_BOTH_ABOVE` ⇒ 与 `baef94e393de` §三 表**逐条一致**
- **漂移差异内容不可核**：锚版 3 件全仓 0 命中 ⇒ 复算读数一律标注「以漂移版实现复算」+ SHA/字节双记；**0 归因**
- **deposon 侧 D(M,T)：不可算**（提案 A-3 已判不可行 + γ）：`tools/distortion_calculator.py` 本仓 + 仓外按名全扫 0 命中；核心理论输入 `u*(a_t)` 与理论界 `L/U` 未交付（`bb7ca9838150` §3.5/§8/§9：理论界由王老师给定、不在 P-B 内自创）⇒ 逆向重建须自创理论 = 违 §9 ⇒ **本条在 PI 给理论输入前结构性不可算**

### 面 3 · 非恒等 `D_dec` 决策轴（提案 B 冻结算式，0 使用 T/R/A、0 使用 u*）

**臂集识别**：E9.5 `per_problem`（平铺 100 条）= `rule_baseline` 臂 —— 证据：隐含正确率 `0.87` == `rule_baseline.accuracy 0.87` ≠ `unified 0.85`（gsm8k）。
（strategyqa 侧 `rule_baseline` 与 `unified` 精度**同为 0.8989** ⇒ 归属证据不唯一；该 benchmark 已判不可算，归属不参与任何读数。）

**gsm8k（N = 100，6 臂 ⇒ 15 臂对；四字段逐条命中：`predicted` 600 / `trap_hit` 600 / `n_paths` 100 / `n_filtered` 100）**

D_dec 决策不一致率（点估计 + seed42 的 95% bootstrap CI；10k resamples）：

| 臂对 | D_dec | CI95 | 臂对 | D_dec | CI95 |
|---|---|---|---|---|---|
| no_deposon \| rule_baseline | 0.99 | [0.97, 1.00] | high_couple \| no_deposon | 0.92 | [0.86, 0.97] |
| no_deposon \| v1_blocking | 0.98 | [0.95, 1.00] | high_couple \| v2_tunneling | 0.90 | [0.84, 0.95] |
| no_deposon \| unified | 0.97 | [0.93, 1.00] | high_couple \| rule_baseline | 0.07 | [0.03, 0.12] |
| rule_baseline \| v2_tunneling | 0.97 | [0.93, 1.00] | high_couple \| v1_blocking | 0.06 | [0.02, 0.11] |
| v1_blocking \| v2_tunneling | 0.96 | [0.92, 0.99] | high_couple \| unified | 0.05 | [0.01, 0.10] |
| unified \| v2_tunneling | 0.95 | [0.90, 0.99] | no_deposon \| v2_tunneling | 0.02 | [0.00, 0.05] |
| | | | rule_baseline \| unified | 0.02 | [0.00, 0.05] |
| | | | unified \| v1_blocking | 0.01 | [0.00, 0.03] |
| | | | rule_baseline \| v1_blocking | 0.01 | [0.00, 0.03] |

D_trap 陷阱命中率：`no_deposon 1.00` > `v2_tunneling 0.98` > `high_couple 0.07` > `unified 0.02` > `v1_blocking 0.01` > `rule_baseline 0.00`

D_flux 通道筛选翻转幅度：**仅 `rule_baseline` 可算 = 0.27167**（CI95 [0.2633, 0.2817]，`n_distinct=3`、`std=0.0466`）；另 5 臂 `n_paths`/`n_filtered` **0 命中** ⇒ 不可算（臂级缺口）。

- **`predicted` 含 null 的记录**：`no_deposon` 6 条、`v2_tunneling` 6 条（合计 12，与 `baef94e393de` P2 实测「gsm8k 12 条为 None」一致）⇒ 按字面参与 `1[pred_a≠pred_b]`（null 与数值互异），**0 归一化、0 剔除**（剔除即私设）
- **(b) 判据「≥3 个臂对 n_distinct > 3 且 std > 0」⇒ 不满足**（见 §3 防退化门三读）
- **(c) 判据「3 seed × 10k resamples 臂间大小序 3/3 不变」⇒ 不满足**：seed42 / 123 / 456 的 bootstrap 均值序**互不相同**。**不稳定位置逐对登记**（105 组两两比较中 **102 组三 seed 一致**；3 组不一致）：
  - `no_deposon|unified` ↔ `rule_baseline|v2_tunneling`（点估计**并列 0.97**）
  - `no_deposon|v2_tunneling` ↔ `rule_baseline|unified`（点估计**并列 0.02**）
  - `rule_baseline|v1_blocking` ↔ `unified|v1_blocking`（点估计**并列 0.01**）
  - ⇒ **3 组翻转全部落在点估计完全并列的臂对上**（并列组内 bootstrap 抽样噪声决定次序）；非并列臂对的次序在 3 seed 下稳定。**机械判定仍取 (c) 不满足**（字面要求全序 3/3 不变），并列性质仅作登记，不作放宽。

**strategyqa（N = 99）**：**不可算 + γ** —— 四字段中 `predicted` **0 命中**（该 benchmark 预测字段实测名为 `pred`）⇒ 按提案 B 可算性前置**按 benchmark 粒度**判不可算，**0 跨 benchmark 合并**、0 用别名改判（别名事实仅登记）。

---

## §3 防退化门自证（K-V3R1P1-0-A；二值单列，PI 拍板③）

| 序列 | n_distinct / std | 门（>3 且 >0） |
|---|---|---|
| D_dec per-item 指示量（15 臂对） | 结构性 `n_distinct = 2` | **二值单列**，不与门混算 |
| D_trap per-item 指示量（6 臂） | 结构性 `n_distinct = 2` | **二值单列** |
| D_flux per-item 值（`rule_baseline` 唯一可算臂） | `n_distinct = 3` / `std = 0.0466` | ❌ 不过门（3 不 > 3） |
| 臂对级合计（提案 B 字面：只有 D_dec 是臂对指标） | — | **0 / 15 达标** |

**(b) 读法依赖已披露（0 合并、0 私自改门）**：
- **读法 B-1（本件采用）**：门施于**指标自身的 per-item 序列** ⇒ D_dec 二值单列 + D_flux 仅单臂且 `n_distinct=3` ⇒ 达标数 **0** ⇒ (b) 不满足；
- **读法 B-2（补充实测，仅登记，0 计入判定）**：门施于**源值序列**（每臂 100 条 `predicted`）⇒ `n_distinct` 73~80、`std` 5.3e+03 ~ 2.5e+13 ⇒ **6/6 臂达标** ⇒ (b) 将满足。
- **关键：(b) 的读法不改变本条整体判定** —— (a) 独立失败（2/3），⇒ 无论 (b) 取何读法，K-V3R-21 均落「维持不明」。
  （B-2 数据面观察：`predicted` 存在极端离群值，量级达 1e+14，与 `baef94e393de` P2 记录的 `gsm8k pred min=-2.5e14` 同向；0 归因。）

---

## §4 判死线 (a)(b)(c) 机械落定 + 改判档位

| 判据 | 结果 | 明细 |
|---|---|---|
| (a) 面 2 复算 3/3 在 ±5% 内 | ❌ **不满足** | 2/3（B1 超差 +11.31%） |
| (b) 面 3 ≥3 臂对 `n_distinct>3` 且 `std>0` | ❌ **不满足**（读法 B-1）／读法 B-2 满足 | 达标 0/15；D_flux 仅 1 臂且 `n_distinct=3` |
| (c) 3 seed 臂间大小序 3/3 不变 | ❌ **不满足** | 3 个 bootstrap 序互不相同（105 组两两比较 102 组稳定；3 组翻转全在点估计并列对上） |
| **合并** | ⇒ **维持「不明」+ γ 登记** | |

- **`new_verdict` = `REMAINS_UNKNOWN`**（沿 v1 §4 四档：**不明分支** ⇒ 维持原标注不动，显式登记 γ，归「V4 收尾整理」待拍板桶；原报告 byte **0 触动**）
- **结论上限（冻结，防误导）**：即便将来 (a)(b)(c) 全满足，也只能出「**通用基线侧可算 + deposon 侧不可算**」的**分面结论**；**不得**升级为「deposon 优于/不优于 OT·KD·LLMLingua」的跨面结论

---

## §5 γ 登记

| ID | 触发 | 状态 |
|---|---|---|
| **G21-1** | 面 3 四字段之一 0 命中 ⇒ strategyqa 不可算（`predicted` 0 命中，实测字段名 `pred`） | **triggered**（按 benchmark 粒度，0 跨 benchmark 合并） |
| **G21-2** | `n_paths`/`n_filtered` 在 E9.3/E9.4 的 5 个臂 0 命中 ⇒ D_flux 仅 `rule_baseline` 单臂可算 | registered_as_arm_level_limit |
| **G21-3** | deposon 侧 D(M,T) 逆向重建判不可行（提案 A-3） | **triggered**（结构性，PI 给理论输入前不可算） |
| **G21-4** | 锚版 3 BOSS 脚本全仓 0 命中 ⇒ 漂移差异内容不可核 | unverifiable_no_attribution |
| **G21-5** | D_dec per-item 序列结构性二值 ⇒ 防退化门 `n_distinct>3` 在臂对级不可达 | **triggered**（读法依赖已披露，见 §3） |
| **G21-6** | (a) 面 2 复现 2/3：B1 相对偏差 +11.31% 超 ±5%（报告值 4 位小数显示，窗半宽窄于显示粒度） | **triggered**（机械判定，0 擅改容差） |
| **G21-7** | (c) 3 seed 臂间大小序不一致（3 组翻转全落在点估计并列的臂对上） | **triggered** |

---

## §6 只读与 0 触动声明

- **仓外只读取用**（K-V3R1P1-0-F）：3 件漂移版 BOSS 脚本**只读取用**（`importlib` 按路径加载，**0 复制入仓 / 0 写入 / 0 移出 / 0 删除 / 0 改 ACL**）；SHA-12 + 字节见 §2 表与 result 件 `external_readonly`
- **既有件 0 触动**：`results/deposon_v19_benchmark_fixes.json`（`910c4333eead`）、`verifier/audit/conservation.py`（`4bdec2683f06`）、`docs/V3X/KT_B1_SPEC_V0.1.md`（`0410ca0fbdae`）、`KT_B1_REWORK_REPORT`（`baef94e393de`）、`P_B_DISTORTION_BOUND_V0_SPEC`（`bb7ca9838150`）、`_v3_n_ktb1_distortion_bound_data_2026_09_27.json`（`26c0d0b0ffb6`）、v1 / v1.1 预登记 —— **全部只读，0 字节改动**（哈希基线落 `result.input_chain`）
- **派生 JSON 0 合并**：新名独立件，0 并入 `_v3_n_*` 或 `deposon_v19_benchmark_fixes.json`
- **key**：0 明文密钥、0 key 读取（3 个漂移版脚本经实测 0 `openai` / 0 `api_key` / 0 `os.environ`，纯本地数值）
- **0 LLM**：0 调用、0 proxy

---

## §7 老实交代

- **skill 未加载**：本 Turn 工具集内**无 skill 加载工具**（无 `skill` / `tool_search` 入口）⇒ 派工单指定 `scientific-research-workflows:experimental-design` **未加载到**；按纪律锚 fallback 执行（`_v3_recheck_prereg_v1p1_2026_09_27.md` K-V3R-21 + 提案 A/B/C 字面 + `_v3_n_recheck_llm_verdict_2026_09_27.md` §三条现状），**0 编造 skill 指令**
- **(b) 判据读法未决**：读法归属属 PI 拍板项；本件按「门施于指标自身 per-item 序列」执行并把 B-2 读法实测并披露；**因 (a) 独立失败，整体判定不随读法变化**
- **面 3 覆盖边界**：仅 **gsm8k（N=100，6 臂，15 臂对）**；strategyqa 不可算；0 外推至 v19 其他实验臂
- **D_flux 覆盖边界**：仅 `rule_baseline` 单臂；0 声称「通道筛选翻转幅度」是臂间指标
- **B1 复算耗时**：漂移版 B1 为纯 Python Sinkhorn（995 记录 × 6 reg × 200 迭代），单次复算约十余分钟；executor 0 并行、0 改脚本、0 降 reg 档（reg 扫描沿脚本默认全档）
- **0 主张**：本件**不**主张 deposon 的失真上界数值（deposon 侧 D(M,T) 仍不可算）；**不**把 `D_dec` 与 `D(M,T)` 并排比大小；**不**将面 3 结果外推为跨面结论
- **succeeded ≠ 跑完**：三面全部算完并落盘；完成宣告以落盘核验（字节 + SHA-12 + 重跑逐字不变）为准，值见最终汇报

---

出件｜Mavis 团队 worker｜2026-09-27
