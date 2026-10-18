# V5 · H2-30 strategyqa「补字段别名后重算」面 3 重算件 · worker · 2026-09-29

> **性质**：PI 确认批 11 §2 ㊱（`_v5_confirm_b11_decisions_register_2026_09_29.md`）授权面的**纯执行棒**产出。
> 本件**不是**预登记件、**不是**判定件、**不是**改判件、**0 代裁档位**（档位裁定属 verdict-keeper）。
> **上游输入（只读，0 触动）**：`_v5_confirm_b11_decisions_register_2026_09_29.md` §2.1–§2.3；
> `_v3_recheck_21_rescript_2026_09_27.md` ＝ `04f6ecd482b9`（14,618 B）面 3 / §3 防退化门 / §5 γ；
> `deposon_team/plugins/_v3r1p1_21_ktb1_distortion_2026_09_27.py` ＝ `f7b61f041c0b`（30,672 B）；
> `results/_v3_recheck_21_result_2026_09_27.json` ＝ `354ae9c14fe2`（44,928 B）；
> `results/deposon_v19_benchmark_fixes.json` ＝ `910c4333eead`（409,104 B）＝ 面 3 唯一数据源（**在仓内**，非仓外）。
> **产出件**：`deposon_team/plugins/_v5_item21_strategyqa_realias_2026_09_29.py`（新名 executor）＋
> `results/_v5_item21_strategyqa_realias_recompute_2026_09_29.json`（新名结果件，**0 合并**）。
> **0 LLM / 0 proxy / 0 网络 / 0 key 读取**；派生 JSON 0 合并；既有件 0 字节改动。

---

## §0 授权面与三条硬约束的执行登记

| # | 硬约束（落册册 §2.3 逐字） | 本棒执行事实 |
|---:|---|---|
| 1 | **授权面仅限补 `pred` → `predicted` 字段别名** ⇒ 0 改算法、0 改判据、0 改读数定义 | 唯一增量为读取面访问器 `get_field()` + 别名表 `{"predicted": "pred"}`（canonical → 实测名）。数值例程 **`stats()` / `boot_ci()` 与冻结参数 `N_RESAMPLES=10000` / `SEEDS=(42,123,456)` 不由本件定义**，从原 executor **按路径只读 importlib 加载**后直接调用 ⇒ 数值代码即原件字节。**自证见 §5（gsm8k 逐键相等）** |
| 2 | **重算范围仅面 3**（按 benchmark 粒度）⇒ 0 扩面 | 只跑面 3 × 单 benchmark（strategyqa）。**面 1 0 复算、面 2 0 复算（B1 Sinkhorn 0 重跑，约 10 min 的路径 0 触发）**、其余 benchmark 0 触碰。**0 跨 benchmark 合并、0 跨 benchmark 比大小** |
| 3 | **产出落新名件；派生 JSON 0 合并；既有结果 JSON 0 覆写、0 改写** | 新名 executor ＋ 新名 JSON；`354ae9c14fe2` 只读打开（仅用于 §5 自证比对）；落盘后**复测 6 件证据 SHA-12 全部不变**（§6） |

**未决项 #3 已销**（落册册 §6 第 3 项：「H2-30 重算『pred → predicted』别名字段清单须回 `04f6ecd482b9` 原文核」）：
回原文逐条核得 —— **canonical 四字段 ＝ `predicted` / `trap_hit` / `n_paths` / `n_filtered`**
（源件 L68 字面「四字段逐条命中：`predicted` 600 / `trap_hit` 600 / `n_paths` 100 / `n_filtered` 100」；
原 executor L250 `REQUIRED_FIELDS` 同四元组）⇒ **需补别名的字段恰 1 个**（`pred` → `predicted`），余 3 字段名两侧一致、0 需别名。

---

## §1 别名事实登记（0 归因）

| 项 | gsm8k | strategyqa |
|---|---|---|
| 预测字段实测名 | `predicted` | **`pred`** |
| 字段名跨臂一致性 | 6/6 臂均 `predicted` | **6/6 臂均 `pred`** |
| 混合命名 / 跨臂冲突 | 无 | **无** |
| `trap_hit` 命中 | 600 | 594 |
| `n_paths` / `n_filtered` 命中 | 100 / 100（仅平铺 E9.5 臂） | **99 / 99（仅平铺 E9.5 臂）** |
| 补别名后 `predicted` 命中 | 600（不变） | **0 → 594** |

⇒ **别名无跨臂冲突、无混合命名**（0 归因、仅事实登记）。strategyqa 与 gsm8k 的字段布局差异**仅在预测字段名一项**。

---

## §2 臂集识别（沿 executor 口径，0 改臂名）

- 沿原 executor L269–274：E9.3 五臂 `no_deposon / v1_blocking / v2_tunneling / unified / high_couple`
  ＋ E9.5 平铺 ⇒ `rule_baseline` = **6 臂 ⇒ 15 臂对**（与 gsm8k 同）。
- id 交集：6 臂 id 集**完全相同**，`|common| = |union| = 99` ⇒ **N = 99**（与源件「N = 99」一致，0 掉样本）。
- ⚠️ **别名后归属披露（本棒新增，原 caveat 前提已失效）**：
  - 平铺臂 `rule_baseline` 与 `unified` 精度**同为 `0.898989898989899`** ⇒ 归属证据**不唯一**
    （`identification_unique = false`，`unified_also_matches = true`）。
  - 原件/源件 caveat「该 benchmark 已判不可算 ⇒ **归属不参与任何读数**」**在别名重算后不再成立**（现已 computable）。
  - 波及面：5 个 D_dec 臂对 + D_trap 该臂 ＋ **D_flux 唯一可算臂恰是该归属不唯一的平铺臂**。
  - 本件处置：**沿原 executor 硬编码臂名 `rule_baseline`、0 重命名、0 替 PI 裁定归属**；如实披露（0 归因、0 编造归属说明）。

---

## §3 面 3 · strategyqa 重算读数（N = 99，6 臂，15 臂对）

**D_dec 决策不一致率**（点估计 ＋ seed42 的 95% bootstrap CI；10k resamples，每 seed 共享索引矩阵）：

| 臂对 | D_dec | CI95 | 臂对 | D_dec | CI95 |
|---|---|---|---|---|---|
| no_deposon \| v1_blocking | **0.9798** | [0.9495, 1.0000] | no_deposon \| v2_tunneling | 0.1010 | [0.0505, 0.1616] |
| no_deposon \| unified | 0.9798 | [0.9495, 1.0000] | unified \| v1_blocking | 0.0000 | [0.0000, 0.0000] |
| no_deposon \| rule_baseline | 0.9798 | [0.9495, 1.0000] | high_couple \| v1_blocking | 0.0000 | [0.0000, 0.0000] |
| high_couple \| no_deposon | 0.9798 | [0.9495, 1.0000] | high_couple \| unified | 0.0000 | [0.0000, 0.0000] |
| v1_blocking \| v2_tunneling | **0.8788** | [0.8081, 0.9394] | high_couple \| rule_baseline | 0.0000 | [0.0000, 0.0000] |
| unified \| v2_tunneling | 0.8788 | [0.8081, 0.9394] | rule_baseline \| v1_blocking | 0.0000 | [0.0000, 0.0000] |
| high_couple \| v2_tunneling | 0.8788 | [0.8081, 0.9394] | rule_baseline \| unified | 0.0000 | [0.0000, 0.0000] |
| rule_baseline \| v2_tunneling | 0.8788 | [0.8081, 0.9394] | | | |

**D_trap 陷阱命中率**：`no_deposon 1.0000` > `v2_tunneling 0.8990` > `v1_blocking 0.0000` = `unified 0.0000` = `high_couple 0.0000` = `rule_baseline 0.0000`

**D_flux 通道筛选翻转幅度**：**仅 `rule_baseline` 可算 = `0.500000`**（CI95 [0.5000, 0.5000]，
`n_distinct = 1`、`std = 0.0` ⇒ **常数序列**，不过门）；另 5 臂 `n_paths`/`n_filtered` **0 命中** ⇒ 臂级缺口
（`D_flux_arm_level_gap = [high_couple, no_deposon, unified, v1_blocking, v2_tunneling]`，沿 G21-2 同款）。

- **`predicted` 含 null 的记录：6 臂全 0 条**（与 gsm8k 12 条不同）⇒ 本 benchmark 0 触发 null 处理分支。
- **缺键记录：6 臂全 0 条** ⇒ 别名后 0 落 `MISSING` 哨兵。
- **⚠️ 值域披露（防跨 benchmark 误读）**：strategyqa `pred` 取值域 ＝ **`{"Yes", "No"}` 字符串**；
  gsm8k `predicted` 取值域 ＝ **float**。公式逐字相同（`1[pred_a ≠ pred_b]`），但**strategyqa 的 D_dec 是
  Yes/No 布尔不一致率，非数值距离** ⇒ **两者 0 可比、0 并排、0 相减**（沿量纲/值域互斥纪律，源件 §量纲声明）。

---

## §4 防退化门 (b) 与稳定序 (c)（面 3 自证）

### (b) 判据「≥3 个臂对 `n_distinct > 3` 且 `std > 0`」⇒ ❌ **不满足（机械）**

| 序列 | 读数 | 门（>3 且 >0） |
|---|---|---|
| D_dec per-item 指示量（15 臂对） | 结构性 `n_distinct ∈ {1, 2}` ⇒ 全部二值 | **二值单列**（PI 拍板③） |
| D_trap per-item 指示量（6 臂） | 结构性 `n_distinct = 2` ⇒ 全部二值 | **二值单列** |
| D_flux per-item 值（`rule_baseline` 唯一可算臂） | `n_distinct = 1` / `std = 0.0` | ❌ 不过门 |
| **达标计数（B-1 读法）** | **0**（臂对级 0/15 ＋ 臂级 D_flux 0/1） | ❌ **不满足** |

**读法 B-2 补充实测（源件 §3 字面「门施于源值序列」，0 计入上表判定）**：

| 臂 | 源值序列 `n_distinct` | `std` | 可测 | 过门 |
|---|---:|---|:--:|:--:|
| no_deposon / v1_blocking / v2_tunneling / unified / high_couple / rule_baseline | **2**（6/6 臂） | **null** | ❌ 0/6 | ❌ **0/6** |

- **B-2 在 strategyqa 侧 0/6 达标，且与 B-1 同向（都不满足）** ⇒ **(b) 的读法归属（H2-31 ㊲）对 strategyqa 的 (b) 读数无影响**。
  ⚠️ 本句**仅限 strategyqa 单 benchmark 的 (b)**；**0 预判 H2-31 整体裁定**（gsm8k 侧 B-1 不满足 / B-2 满足，方向相反，档位属 verdict-keeper）。
- **B-2 根因（0 编造、0 自创编码）**：源值序列取值域为 **`{"Yes","No"}` 字符串**，原件 `stats()` 的 `std`
  需 float 域 ⇒ `float("Yes")` 抛 `ValueError` ⇒ **std 不可算**。本件只做 **0 编码的纯基数去重计数**（`n_distinct = 2`），
  门规则首个合取项 `n_distinct > 3` 已不满足 ⇒ **无需 std 即可机械落读**。
  **0 自创 `Yes/No` → 数值编码**（编码即私设读数定义，超授权面）。

### (c) 判据「3 seed × 10k resamples 臂间大小序 3/3 不变」⇒ ✅ **满足（机械）**

- seed42 / seed123 / seed456 三条 bootstrap 均值序**逐条完全相同**；105 组两两比较 **105/105 一致**，
  三组两两 discordant 列表**全空**。
- ⚠️ **覆盖面披露（0 改判、0 放宽、仅登记）**：**15 个臂对中 14 个落在点估计完全并列组**
  （0.9798 ×4、0.8788 ×4、0.0 ×6），**唯一不并列的臂对仅 1 个**（`no_deposon|v2_tunneling = 0.1010`）。
  源件 `order_by` 的排序键为 **`(bootstrap 均值, 臂对名字符串)`** ⇒ 并列处由**臂对名 tiebreak** 决定次序。
  故 (c) 的「3/3 稳定」**含名 tiebreak 成分**，**不可**据此宣称该读数具备鉴别力。
  事实补充（0 解释）：`v1_blocking` / `unified` / `high_couple` / `rule_baseline` 四臂在**全部 99 题上逐题同答案**
  （其两两 D_dec 恒 0.0000，共 6 对）。

### 判据汇总（**仅面 3 · 仅 strategyqa 单 benchmark**）

| 判据 | 机械落读 | 说明 |
|---|---|---|
| (b) | ❌ **不满足** | B-1 读法达标 0；B-2 读法达标 0/6（同向） |
| (c) | ✅ **满足** | 105/105 一致；并列/tiebreak 成分已披露 |
| (a) | **本棒 0 判定** | (a) 属**面 2**，**授权面仅面 3** ⇒ 0 复算、0 引用、0 代裁 |

---

## §5 「0 改算法 / 0 改判据 / 0 改读数定义」可核自证

同一代码路径令 **gsm8k**（`predicted` 键存在 ⇒ 别名 0 命中）在**关闭别名**下跑一遍，与既有结果 JSON
`354ae9c14fe2` 的 gsm8k 条目**逐键比对**：

| 比对项 | 结果 |
|---|---|
| `D_dec`（15 臂对全量：点估计 + 3 seed CI） | ✅ 逐键相等 |
| `D_trap` / `D_flux` / `D_dec_diag` / `D_trap_diag` / `D_flux_diag` | ✅ 逐键相等 |
| `D_flux_arm_level_gap` / `four_field_hits` / `computable` / `n_ids` / `arms` | ✅ 逐键相等 |
| `judgment_c.orders_by_seed` | ✅ 相等 |
| `judgment_b.qualifying_count` | ✅ 相等 |
| **总判定 `all_equal`** | ✅ **true** |

⇒ **别名之外 0 差异**为可核事实（非声明）。

---

## §6 产物与只读核验

| 项 | 值 |
|---|---|
| 新名 executor | `deposon_team/plugins/_v5_item21_strategyqa_realias_2026_09_29.py` |
| 新名结果 JSON | `results/_v5_item21_strategyqa_realias_recompute_2026_09_29.json`（**0 合并任何既有 JSON**） |
| 确定性 | **重跑逐字节一致**（34,316 B，0 墙钟时间戳） |
| 数据源 | `results/deposon_v19_benchmark_fixes.json` ＝ `910c4333eead`（**在仓内**；**0 仓外访问**、0 写外部归档） |
| 既有件触动 | **0**（落盘后复测 6/6 SHA-12 不变：源件 `04f6ecd482b9`、原 executor `f7b61f041c0b`、结果 JSON `354ae9c14fe2`、预登记 `bcc3cee23e82`、落册册 `07e9fe512da5`、v19 `910c4333eead`） |
| 0 新设阈值 / 0 改容差 | **0**（`0.95` / `±5%` / `1e-6` / `10k` / `3 seed` 全部沿原件冻结值；面 1/面 2 参数**未参与**） |
| 0 LLM / 0 proxy / 0 网络 / 0 key | **0 / 0 / 0 / 0** |
| 临时脚手架 | `%TEMP%\h230_probe.py`、`h230_probe2.py`、`h230_report.py`、`h230_det.py`（4 件，只读探查脚本，**0 落工作区**、0 敏感内容）⇒ ⚠️ **删除被本机安全策略拦截（永久删除命令被禁）⇒ 4 件仍在 `%TEMP%` 内未删**（工作区 0 影响，如实交代） |

---

## §7 γ 状态更新（**登记，0 改源件**）

| ID | 源件状态 | 本棒实测 | 处置 |
|---|---|---|---|
| **G21-1** | `triggered`（strategyqa `predicted` 0 命中 ⇒ 不可算） | **触发面已消除**：补别名后命中 594 ⇒ `computable = true` | **本棒登记为「触发面已消解（经 PI 授权的别名）」**；源件字面 0 改 |
| **G21-2** | `registered_as_arm_level_limit` | **仍成立**：strategyqa 5/6 臂 `n_paths`/`n_filtered` 0 命中 ⇒ D_flux 仅平铺臂可算 | 维持 |
| **G21-5** | `triggered`（D_dec per-item 结构性二值） | **仍成立且新增实证**：15/15 臂对 `n_distinct ∈ {1,2}` | 维持 |
| 新增（**本棒观察，0 改源件编号**） | — | ① 平铺臂归属证据不唯一（§2）② (c) 满足含名 tiebreak 成分（§4）③ B-2 在字符串值域 std 不可算（§4） | **登记，待 verdict-keeper / PI 处置** |

---

## §8 诚实边界与 0 主张

- **0 判档位、0 代裁**：本件**不**出 item_21 的 `new_verdict`。(a) 属面 2（授权面外）⇒ 整体 (a)(b)(c) 合取与
  改判档位**未由本棒计算、0 代裁**（源件 `REMAINS_UNKNOWN` 字面 0 改，档位属 verdict-keeper）。
- **0 跨 benchmark 结论**：strategyqa 与 gsm8k 的面 3 读数**0 合并、0 并排比大小、0 相减**
  （D_dec 值域不同：Yes/No 字符串 vs float；D_flux 单臂不同：0.5000 vs 0.27167）。
- **0 声称「别名修复 = benchmark 变可判」**：本棒只报**该 benchmark 判据 (b)(c) 的机械落读**，
  **不**主张其对 item 21 整体档位的贡献权重。
- **(b) 读法归属 0 择一**：B-1 / B-2 同报（strategyqa 侧同向，gsm8k 侧方向相反）；
  H2-31 ㊲ 的最终裁定**0 代裁**。
- **0 归因**：字段名差异（`pred` vs `predicted`）**0 归因**，仅事实登记。
- **0 私设编码**：0 自创 `Yes/No` → 数值映射（B-2 的 std 因此不可算，如实登记根因）。
- **未完成 / 未做**：面 1 0 复算、面 2 0 复算（B1 Sinkhorn 0 重跑）、其余 benchmark 0 触碰、
  γ 源件字面 0 改写、item_21 档位 0 裁定、臂归属 0 裁定。
- **succeeded ≠ 跑完**：本件以**落盘核验**（新名 2 件 SHA-12 落盘后实测 ＋ 重跑逐字节一致 ＋ 既有件 6/6 SHA-12 不变）为准。

---

**落款**：**Mavis 团队 worker**（执行棒，0 判定代裁）· 2026-09-29｜SHA-12 落盘后实测随回执回报（不自写入本件）
