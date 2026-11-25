# P-J / P-M / P-C 族 · 收口读数件（棒 1 · worker）· 2026-09-29 下午

> **件性质**：**收口读数件**（只读复算 stored 读数 ＋ 4 项断言命中面登记 ＋ 双口径/档 2 并报）· **纯新建** · **既有件 0 删除 / 0 改写 / 0 覆盖 / 0 合并**
> **件名**：`results/_v5_pjpm_pc_closeout_readout_2026_09_29.md`
> **姊妹产物**：横切预检件（JSON）`results/_v5_pjpm_pc_degen_precheck_result_2026_09_29.json`，SHA-12 `3641afe9d49c`
> **上游锚件**：`results/_v5_pjpm_pc_deg_prereg_2026_09_29.md`，SHA-12 `989ee2bce660`（PI 复核生效 · 确认批 3）
> **裁项包**：PI 确认批 5（派工单字面；问卷原件 0 命中于盘上 ⇒ 见 §6 γ_H）
> **哈希口径**：`hashlib.sha256(全文字节).hexdigest()[:12]`，小写
> **出件方**：Mavis 团队 worker（棒 1 · 收口棒；agent 署名如实，不冒充 protocol-keeper / verdict-keeper / evidence-auditor / doc-writer / PI / Trae code）

---

## §0 速览（7 项一句话）

| # | 项 | 短句 |
|:-:|---|---|
| 1 | 上游锚件复核 | `989ee2bce660` **逐字相符**（不符即中止，本棒 0 触发中止） |
| 2 | 原件 0 触动 | 锚表 **17 件** ＋ 读数链 **4 件** 写盘后逐件复算，漂移 **0** 件（§7） |
| 3 | 三族裁项档位 | 确认批 5 **均 ②档**：P-J 伪秩相关技术面材料 ｜ P-M `SECURE` 无效技术面材料 ｜ P-C 对账面材料 |
| 4 | 四项断言门形态 | ① 复用 `K-V3R-0-A` ｜ ② 复用 `n_distinct > 3` **近似代理** ｜ ③ P-I 诚实降级**定性范式、非门** ｜ ④ 升独立门、切点 `0.5` |
| 5 | 失败处置 | 任一**门**失败 ⇒ **甲案落 KD + γ**；断言③ 非门 0 触发处置 |
| 6 | 判定面 | `K-PJPC-1-1…3-5` 全部落**可裁形式**三态；**终态归 verdict-keeper**（本棒 0 代裁） |
| 7 | 件名 / 别名表 | 批 5 ⑥交 protocol-keeper 出候选 ⇒ 本棒**工作名**落盘，`D-01…D-04` **0 回填** |

---

## §1 三族逐条读数（`n_distinct` / `min` / `max` / `std`）

### §1.1 P-J

| 面 | 序列 | n | n_distinct | min | max | std |
|---|---|---:|---:|---:|---:|---:|
| as-run | `T_frac60（对照，9 model）` | 9 | 7 | 0.5333 | 0.8667 | 0.1065948867 |
| as-run | `convergence_rates（9 model 主读数列）` | 9 | 1 | 0.1 | 0.1 | 0.0000000000 |
| as-run | `basin_map_sample.potentialness（2 点样本）` | 2 | 1 | 0.711111111111111 | 0.711111111111111 | 0.0000000000 |
| 新构造 `O1_discrete_cell_redistribution` | `convergence_rate`（9 model） | 9 | 9 | 0.0132 | 0.0173 | 0.0012788884 |
| 新构造 `O3_logit_normal_form` | `convergence_rate`（9 model） | 9 | 8 | 0.33899999999999997 | 0.3557 | 0.0044661691 |
| 新构造 `O5_replicator_ode_softlimit` | `convergence_rate`（9 model） | 9 | 9 | 17.9501 | 72.0337 | 16.9800088427 |

**P-J ②档技术面材料**：`rho = -0.9667` 系对 9 元素**常量 vector**（`convergence_rates` n_distinct = 1、std = 0.0）算的 Spearman；对照 `T_frac60` n_distinct = 7（真分布存在）⇒ **判据从未受审**。**禁引纪律的正式措辞 0 代拟（归 doc-writer）**。

### §1.2 P-M

| 面 | 序列 | n | n_distinct | min | max | std |
|---|---|---:|---:|---:|---:|---:|
| as-run | `attack_results.attack_budget（10 档轴）` | 10 | 10 | 8 | 80 | 22.9782505862 |
| as-run | `attack_results.unit_perturbation_count（逐档）` | 10 | 10 | 64 | 640 | 183.8260046892 |
| as-run | `attack_results.detection_rate（10 档）` | 10 | 1 | 0.0 | 0.0 | 0.0000000000 |
| as-run | `attack_results.detected_count（10 档）` | 10 | 1 | 0 | 0 | 0.0000000000 |
| as-run | `attack_results.missed_count（10 档）` | 10 | 1 | 8 | 8 | 0.0000000000 |
| as-run | `attack_results.missed_indices_first_5（10 档，序列型）` | 1 | 1 | [0, 1, 2, 3, 4] | [0, 1, 2, 3, 4] | —（标识符型） |
| as-run | `cost_miss_rate_curve.detection_rate（10 档）` | 10 | 1 | 0.0 | 0.0 | 0.0000000000 |
| as-run | `cost_miss_rate_curve.miss_rate（10 档）` | 10 | 1 | 1.0 | 1.0 | 0.0000000000 |
| 新构造 | `matrix.attack_budget（27 格）` | 27 | 9 | 1 | 80 | 27.8288419530 |
| 新构造 | `matrix.trials（27 格）` | 27 | 1 | 400 | 400 | 0.0000000000 |
| 新构造 | `matrix.detected_count（27 格）` | 27 | 1 | 400 | 400 | 0.0000000000 |
| 新构造 | `matrix.detection_rate（27 格 = 3 算子 × 9 budget）` | 27 | 1 | 1.0 | 1.0 | 0.0000000000 |
| 新构造 | `matrix.miss_rate（27 格）` | 27 | 1 | 0.0 | 0.0 | 0.0000000000 |
| 新构造 | `matrix.hamming_detector_rate（27 格）` | 27 | 1 | 1.0 | 1.0 | 0.0000000000 |

**P-M ②档技术面材料**：同件 `detection_rate` n_distinct = 1、std = 0.0、min = 0.0（**低于盘上既有 `random_guess_rate` = 0.5**），却记 `v42_safety_index = "SECURE"` ⇒ **该字面与其自身数据面矛盾**。诚实降级版 `a4b12d1cfedc` 已自陈 `v42_redesign_required = true`。**正式措辞 0 代拟（归 doc-writer）**。

**天花板序列披露（`K-PJPC-1-3` 强制）**：新构造面 27 格 `detection_rate` 全 = 1.0 ⇒ n_distinct = 1、std = 0。沿 `a0734e0a6860` §3.1 自陈 = **检测器饱和，非判据退化**；判据非退化性由 input_fields 承担（#28 `gate_per_field` 三项全 True）。**⚠️ 天花板序列不得单独充当「非退化」证据。**

### §1.3 P-C

| 面 | 序列 | n | n_distinct | min | max | std |
|---|---|---:|---:|---:|---:|---:|
| as-run | `per_model_per_eta.t_frac（9 model 对照）` | 9 | 7 | 0.5333 | 0.8667 | 0.1065948867 |
| as-run | `eta_scan（η 轴）` | 9 | 9 | 0.01 | 100.0 | 32.4404504391 |
| as-run | `r2_per_eta` 逐 η 档跨 model（档 0） | 9 | 1 | 0.19840149926690828 | 0.19840149926690828 | 0.0000000000 |
| as-run | `r2_per_eta` 逐 η 档跨 model（档 1） | 9 | 1 | 0.19662389698258478 | 0.19662389698258478 | 0.0000000000 |
| as-run | `r2_per_eta` 逐 η 档跨 model（档 2） | 9 | 1 | 0.1889141637058418 | 0.1889141637058418 | 0.0000000000 |
| as-run | `r2_per_eta` 逐 η 档跨 model（档 3） | 9 | 1 | 0.17970071122194156 | 0.17970071122194156 | 0.0000000000 |
| as-run | `r2_per_eta` 逐 η 档跨 model（档 4） | 9 | 1 | 0.1625999275612872 | 0.1625999275612872 | 0.0000000000 |
| as-run | `r2_per_eta` 逐 η 档跨 model（档 5） | 9 | 1 | 0.120456989018929 | 0.120456989018929 | 0.0000000000 |
| as-run | `r2_per_eta` 逐 η 档跨 model（档 6） | 9 | 1 | 0.07306085701664845 | 0.07306085701664845 | 0.0000000000 |
| as-run | `r2_per_eta` 逐 η 档跨 model（档 7） | 9 | 1 | 0.0013381562740183738 | 0.0013381562740183738 | 0.0000000000 |
| as-run | `r2_per_eta` 逐 η 档跨 model（档 8） | 9 | 1 | 9.016426050829492e-06 | 9.016426050829492e-06 | 0.0000000000 |
| 新构造 | `r2_per_eta` 逐 η 档跨 model（eta=0.01） | 9 | 9 | 0.00614225523225409 | 0.6598733691018495 | 0.2031064447 |
| 新构造 | `r2_per_eta` 逐 η 档跨 model（eta=0.1） | 9 | 9 | 0.0011579268668835407 | 0.5101408443095636 | 0.1484090458 |
| 新构造 | `r2_per_eta` 逐 η 档跨 model（eta=0.5） | 9 | 9 | 0.01873555167265839 | 0.6641964976981287 | 0.2259806888 |
| 新构造 | `r2_per_eta` 逐 η 档跨 model（eta=1） | 9 | 9 | 0.041186011693437385 | 0.6815646123791426 | 0.1972572705 |
| 新构造 | `r2_per_eta` 逐 η 档跨 model（eta=2） | 9 | 9 | 0.023811719048000946 | 0.8510642444031592 | 0.2806574642 |
| 新构造 | `r2_per_eta` 逐 η 档跨 model（eta=5） | 9 | 9 | 0.04036079489125055 | 0.8185764478224623 | 0.2574830390 |
| 新构造 | `r2_per_eta` 逐 η 档跨 model（eta=10） | 9 | 9 | 0.004072367489818984 | 0.9286188996387963 | 0.3012340518 |
| 新构造 | `r2_per_eta` 逐 η 档跨 model（eta=50） | 9 | 9 | 0.08696415507405564 | 0.8155037437669215 | 0.2055830670 |
| 新构造 | `r2_per_eta` 逐 η 档跨 model（eta=100） | 9 | 9 | 0.061499434105409256 | 0.7136848940020104 | 0.2167774670 |

**P-C ②档对账面材料**：as-run 9 条 `r2_per_eta` 数组**逐字全等 = True**（逐 η 档 n_distinct = [1, 1, 1, 1, 1, 1, 1, 1, 1]）；新构造 **9/9 个 η 档 n_distinct = 9 > 3** ⇒ 证据面 PASS。命题面：as-run max r2_per_eta = 0.19840149926690828 < 0.3 ⇒ `FAIL_H0`，同件 `exp_d7_5anchor_60cells.P-C_two_phase` 字面 = `FAIL_H0 (幂律死)`。**两腿分读并报；PASS 0 构成「幂律成立」证据**（沿 `fc0ffd27adca` γ₃ 零噪声对照腿 `ss_tot ~ 1e-31`）。`K-V3R-27` 已在 P-L/P-C FSS 线上处理同族对账 ⇒ 本棒 **0 重复、0 混件**。

---

## §2 §1.4 四项断言命中面逐条登记（批 5 裁项包逐字承接）

| 断言 | 门形态（批 5） | 面 | 读数 | 命中 | 落态 |
|---|---|---|---|:-:|---|
| ① 输入向量方差 > 0 | 复用 K-V3R-0-A 字面（std > 0），0 新增门槛… | P-J / asrun_退化面 | n_distinct = 1、std = 0.0、min = 0.1 | **命中** | FAIL（退化警报命中） |
| ② 秩不恒同（排序层） | 批 5 ②档：复用 n_distinct > 3 作近似代理（非排序… | P-J / asrun_退化面 | n_distinct = 1、std = 0.0、min = 0.1 | **命中** | FAIL（退化警报命中） |
| ① 输入向量方差 > 0 | 复用 K-V3R-0-A 字面（std > 0），0 新增门槛… | P-J / asrun_退化面 | n_distinct = 1、std = 0.0、min = 0.711111111111111 | **命中** | FAIL（退化警报命中） |
| ② 秩不恒同（排序层） | 批 5 ②档：复用 n_distinct > 3 作近似代理（非排序… | P-J / asrun_退化面 | n_distinct = 1、std = 0.0、min = 0.711111111111111 | **命中** | FAIL（退化警报命中） |
| ③ 标签非硬编码 | **非门**（P-I 诚实降级范式） | P-J / asrun_退化面 | —（定性） | 命中 | 仅登记，0 触发处置 |
| ④ 检测率不低于随机基线 | 见批 5 | P-J / asrun_退化面 | — | N/A | **不适用**（0 当通过、0 当失败） |
| ① 输入向量方差 > 0 | 复用 K-V3R-0-A 字面（std > 0），0 新增门槛… | P-J / 新构造面_O1_discrete_cell_redistribution | n_distinct = 9、std = 0.0012788884062167251、min = 0.0132 | 未命中 | PASS（std > 0） |
| ② 秩不恒同（排序层） | 批 5 ②档：复用 n_distinct > 3 作近似代理（非排序… | P-J / 新构造面_O1_discrete_cell_redistribution | n_distinct = 9、std = 0.0012788884062167251、min = 0.0132 | 未命中 | PASS（n_distinct > 3） |
| ③ 标签非硬编码 | **非门**（P-I 诚实降级范式） | P-J / 新构造面_O1_discrete_cell_redistribution | —（定性） | 未命中 | 仅登记，0 触发处置 |
| ④ 检测率不低于随机基线 | 见批 5 | P-J / 新构造面_O1_discrete_cell_redistribution | — | N/A | **不适用**（0 当通过、0 当失败） |
| ① 输入向量方差 > 0 | 复用 K-V3R-0-A 字面（std > 0），0 新增门槛… | P-J / 新构造面_O3_logit_normal_form | n_distinct = 8、std = 0.004466169126518474、min = 0.33899999999999997 | 未命中 | PASS（std > 0） |
| ② 秩不恒同（排序层） | 批 5 ②档：复用 n_distinct > 3 作近似代理（非排序… | P-J / 新构造面_O3_logit_normal_form | n_distinct = 8、std = 0.004466169126518474、min = 0.33899999999999997 | 未命中 | PASS（n_distinct > 3） |
| ③ 标签非硬编码 | **非门**（P-I 诚实降级范式） | P-J / 新构造面_O3_logit_normal_form | —（定性） | 未命中 | 仅登记，0 触发处置 |
| ④ 检测率不低于随机基线 | 见批 5 | P-J / 新构造面_O3_logit_normal_form | — | N/A | **不适用**（0 当通过、0 当失败） |
| ① 输入向量方差 > 0 | 复用 K-V3R-0-A 字面（std > 0），0 新增门槛… | P-J / 新构造面_O5_replicator_ode_softlimit | n_distinct = 9、std = 16.980008842717528、min = 17.9501 | 未命中 | PASS（std > 0） |
| ② 秩不恒同（排序层） | 批 5 ②档：复用 n_distinct > 3 作近似代理（非排序… | P-J / 新构造面_O5_replicator_ode_softlimit | n_distinct = 9、std = 16.980008842717528、min = 17.9501 | 未命中 | PASS（n_distinct > 3） |
| ③ 标签非硬编码 | **非门**（P-I 诚实降级范式） | P-J / 新构造面_O5_replicator_ode_softlimit | —（定性） | 未命中 | 仅登记，0 触发处置 |
| ④ 检测率不低于随机基线 | 见批 5 | P-J / 新构造面_O5_replicator_ode_softlimit | — | N/A | **不适用**（0 当通过、0 当失败） |
| ① 输入向量方差 > 0 | 复用 K-V3R-0-A 字面（std > 0），0 新增门槛… | P-M / asrun_退化面 | n_distinct = 1、std = 0.0、min = 0.0 | **命中** | FAIL（退化警报命中） |
| ② 秩不恒同（排序层） | 批 5 ②档：复用 n_distinct > 3 作近似代理（非排序… | P-M / asrun_退化面 | n_distinct = 1、std = 0.0、min = 0.0 | **命中** | FAIL（退化警报命中） |
| ① 输入向量方差 > 0 | 复用 K-V3R-0-A 字面（std > 0），0 新增门槛… | P-M / asrun_退化面 | n_distinct = 1、std = 0.0、min = 1.0 | **命中** | FAIL（退化警报命中） |
| ② 秩不恒同（排序层） | 批 5 ②档：复用 n_distinct > 3 作近似代理（非排序… | P-M / asrun_退化面 | n_distinct = 1、std = 0.0、min = 1.0 | **命中** | FAIL（退化警报命中） |
| ③ 标签非硬编码 | **非门**（P-I 诚实降级范式） | P-M / asrun_退化面 | —（定性） | 命中 | 仅登记，0 触发处置 |
| ④ 检测率不低于随机基线 | 批 5 ④档：升独立门；切点 = random_guess_rate… | P-M / asrun_退化面 | n_distinct = 1、std = 0.0、min = 0.0 | **命中** | FAIL（存在 detection_rate < 0.5 的档） |
| ① 输入向量方差 > 0 | 复用 K-V3R-0-A 字面（std > 0），0 新增门槛… | P-M / 新构造面_3算子×9budget | n_distinct = 1、std = 0.0、min = 1.0 | **命中** | FAIL（退化警报命中） |
| ② 秩不恒同（排序层） | 批 5 ②档：复用 n_distinct > 3 作近似代理（非排序… | P-M / 新构造面_3算子×9budget | n_distinct = 1、std = 0.0、min = 1.0 | **命中** | FAIL（退化警报命中） |
| ③ 标签非硬编码 | **非门**（P-I 诚实降级范式） | P-M / 新构造面_3算子×9budget | —（定性） | 未命中 | 仅登记，0 触发处置 |
| ④ 检测率不低于随机基线 | 批 5 ④档：升独立门；切点 = random_guess_rate… | P-M / 新构造面_3算子×9budget | n_distinct = 1、std = 0.0、min = 1.0 | 未命中 | PASS（全部档 ≥ 0.5） |
| ① 输入向量方差 > 0 | 复用 K-V3R-0-A 字面（std > 0），0 新增门槛… | P-C / asrun_退化面 | n_distinct = 1、std = 0.0、min = 0.19840149926690828 | **命中** | FAIL（退化警报命中） |
| ② 秩不恒同（排序层） | 批 5 ②档：复用 n_distinct > 3 作近似代理（非排序… | P-C / asrun_退化面 | n_distinct = 1、std = 0.0、min = 0.19840149926690828 | **命中** | FAIL（退化警报命中） |
| ① 输入向量方差 > 0 | 复用 K-V3R-0-A 字面（std > 0），0 新增门槛… | P-C / asrun_退化面 | n_distinct = 7、std = 0.10659488672794401、min = 0.5333 | 未命中 | PASS（std > 0） |
| ② 秩不恒同（排序层） | 批 5 ②档：复用 n_distinct > 3 作近似代理（非排序… | P-C / asrun_退化面 | n_distinct = 7、std = 0.10659488672794401、min = 0.5333 | 未命中 | PASS（n_distinct > 3） |
| ③ 标签非硬编码 | **非门**（P-I 诚实降级范式） | P-C / asrun_退化面 | —（定性） | 命中 | 仅登记，0 触发处置 |
| ④ 检测率不低于随机基线 | 见批 5 | P-C / asrun_退化面 | — | N/A | **不适用**（0 当通过、0 当失败） |
| ① 输入向量方差 > 0 | 复用 K-V3R-0-A 字面（std > 0），0 新增门槛… | P-C / 新构造面_纯log-log两参数 | n_distinct = 9、std = 0.20310644472745254、min = 0.00614225523225409 | 未命中 | PASS（std > 0） |
| ② 秩不恒同（排序层） | 批 5 ②档：复用 n_distinct > 3 作近似代理（非排序… | P-C / 新构造面_纯log-log两参数 | n_distinct = 9、std = 0.20310644472745254、min = 0.00614225523225409 | 未命中 | PASS（n_distinct > 3） |
| ③ 标签非硬编码 | **非门**（P-I 诚实降级范式） | P-C / 新构造面_纯log-log两参数 | —（定性） | 未命中 | 仅登记，0 触发处置 |
| ④ 检测率不低于随机基线 | 见批 5 | P-C / 新构造面_纯log-log两参数 | — | N/A | **不适用**（0 当通过、0 当失败） |

**处置汇总（甲案）**：

| 面 | 命中的门 | 落态（可裁形式） |
|---|---|---|
| P-J / asrun_退化面 | K-PJPC-3-1, K-PJPC-3-1, K-PJPC-3-2, K-PJPC-3-2 | **KD** |
| P-J / 新构造面_O1_discrete_cell_redistribution | 0 门命中 | **PASS** |
| P-J / 新构造面_O3_logit_normal_form | 0 门命中 | **PASS** |
| P-J / 新构造面_O5_replicator_ode_softlimit | 0 门命中 | **PASS** |
| P-M / asrun_退化面 | K-PJPC-3-1, K-PJPC-3-1, K-PJPC-3-2, K-PJPC-3-2, K-PJPC-3-4 | **KD** |
| P-M / 新构造面_3算子×9budget | K-PJPC-3-1, K-PJPC-3-2 | **KD** |
| P-C / asrun_退化面 | K-PJPC-3-1, K-PJPC-3-2 | **KD** |
| P-C / 新构造面_纯log-log两参数 | 0 门命中 | **PASS** |

---

## §3 `K-V3R-0-C` 双口径并报（重构造 verdict ＋ 沿原 V3 阈值字面 verdict）

| 族 | 重构造 verdict | 沿原 V3 阈值字面 verdict | 一致性 |
|---|---|---|---|
| **P-J** | PASS（逐本体 O1/O3/O5 3/3，n_distinct = 9/8/9、std > 0） | UNVERIFIED（判据退化：convergence_rate ≡ 0.1，n_distinct = 1、std = 0） | **不一致（维持原标注 + 显式登记 + 归「不明」分支）** |
| **P-M** | PASS（27 格 detection_rate 全 1.0；safety_budget_lower_bound 重测 = 80 ≥ 80） | UNVERIFIED（判据退化：10 档 detection_rate ≡ 0.0，n_distinct = 1、std = 0，低于随机猜测 0.5） | **不一致（维持原标注 + 显式登记 + 归「不明」分支）** |
| **P-C** | PASS（9/9 个 η 档跨 model n_distinct = 9 > 3） | FAIL（维持假证伪）：as-run max r2_per_eta = 0.19840149926690828 < 0.3 ⇒ FAIL_H0，与同件 exp_d7_5anchor_60cells.P-C_two_phase 字面同向 | **不一致（维持原标注 + γ 升级）** |

**P-J 逐本体不聚合（`K-PJPC-1-1`）**：

| 本体 | 重构造 | 沿原字面 | 一致性 |
|---|---|---|---|
| `O1_discrete_cell_redistribution` | PASS | UNVERIFIED（判据退化） | 不一致（new PASS vs legacy UNVERIFIED/判据退化） |
| `O3_logit_normal_form` | PASS | UNVERIFIED（判据退化） | 不一致（new PASS vs legacy UNVERIFIED/判据退化） |
| `O5_replicator_ode_softlimit` | PASS | UNVERIFIED（判据退化） | 不一致（new PASS vs legacy UNVERIFIED/判据退化） |

**`K-PJPC-1-2` 字面空档**：2 ≤ n_distinct ≤ 3 为 K-V3R-26 字面空档；本轮 9/8/9 均在空档外 ⇒ 空档分支 0 触发（沿 26b §3 + γ₂₆₄）

**`K-PJPC-2-2` 两腿分读（证据面 / 命题面）**：

- **证据面**：新构造 PASS ⇒ model 维判据从未受审这一缺陷成立
- **命题面**：FAIL_H0 仍全档成立、β̂ ≈ 0 ⇒ 幂律命题面 0 翻案
- **禁止**：PASS 0 构成『幂律成立』证据（沿 fc0ffd27adca γ₃：零噪声对照腿 ss_tot ~ 1e-31、R² 退化为 ULP 伪值）

---

## §4 既有档 2 判定并报（`17262abfd1d5` §1.1 逐字）

| 族 | 原标注（V3 期字面） | 改判档位 | 处置 |
|---|---|---|---|
| **P-J** | UNVERIFIED（9 model convergence_rate ≡ 0.1，var = 0.0 / n_distinct = 1；JSON 记 rho = -0.9667 系对常量 vector 的伪秩相关） | 第 2 行：PASS + 不一致（26b 三本体 O1/O3/O5 3/3 同向 PASS，hit_tier_all_same = true，同落此档） | 维持原 V3 标注（UNVERIFIED / 假证伪，不动）+ 显式登记新构造 verdict；归「不明」分支；γ₁ 构造常量 / γ₂ 伪秩相关 / γ₃ 双口径不一致 ⇒ 0 构成翻案；桶位 = 「V4 收尾整理」待拍板桶 |
| **P-M** | UNVERIFIED（10 档 budget 8–80 detection_rate ≡ 0.0，全低于随机猜测 0.5） | 第 2 行：PASS + 不一致 | 维持原 V3 标注（UNVERIFIED / 假证伪，不动）+ 显式登记新构造 verdict；归「不明」分支；γ₁ = 原 ≡ 0.0 根因为计数语义反转（盘上 v42_v2 复算记录 + 本行独立复现双证据），非检测能力缺失；γ₂ = 原判据覆盖面仅 5 文件、原 UNVERIFIED 在其自身口径下不可直接引用为安全结论；桶位 = 「V4 收尾整理」待拍板桶 |
| **P-C** | 该维度 UNVERIFIED（9 model r2_per_eta 逐字相同，逐 η 档 n_distinct ≡ 1） | 第 2 行：PASS + 不一致 | 维持原 V3 标注（UNVERIFIED / 假证伪，不动）+ 显式登记新构造 verdict；归「不明」分支；γ₁ model 维判据从未受审 / γ₂ η 原为 scaling 旋钮非物理温度 / γ₃ 新构造逐 model R² 完全由重采样涨落产生 ⇒ K-V3R-10 PASS 不构成「幂律成立」证据；桶位 = 「V4 收尾整理」待拍板桶 |

**档位分布（并报）**：17262abfd1d5 §2.1：档 1 = 0 条；档 2 = 4 条（#10 / #26 / #28 + #4 修订 R1）；档 3 = 3 条；档 4 = 2 条

**本棒处置**：既有档 2 判定原样并报，0 覆盖、0 撤销、0 追认式翻案（K-PJPC-0-4）

---

## §5 `K-PJPC-*` 逐条落态（可裁形式 · **终态归 verdict-keeper**）

| ID | 三态（可裁形式） | 达标面 / 备注 |
|---|---|---|
| `K-PJPC-0-1_防退化门跑前自证` | **PASS（自证齐备；退化警报命中面已逐条登记）** | 自证齐备：3 族 × 6 面逐条报齐 n_distinct/min/max/std，无缺项；退化警报命中面见 §2 处置汇总 |
| `K-PJPC-0-2_原件0触动门` | **PASS（17/17 件写盘后复算相符，漂移 0）** | 17 件锚表逐件复算相符、漂移 0（写盘后复算见本件 §7）；读数链 4 件亦相符 |
| `K-PJPC-0-3_派生JSON不合并门` | **PASS（本棒唯一新建 JSON 为新名独立件）** | 本棒唯一新建 JSON 落新名独立件；0 打开任何既有 JSON 写入模式 |
| `K-PJPC-0-4_0回改既有改判门` | **PASS（0 覆盖 / 0 撤销 / 0 追认式翻案）** | 既有档 2 判定原样并报、0 覆盖 0 撤销；自证面 = 0-2 锚表 17 件写盘后复算 |
| `K-PJPC-1-2_P-J字面空档` | **0 触发（实测 9 / 8 / 9，均在空档外）** | — |
| `K-PJPC-2-2_PASS不等于命题成立` | **PASS（本棒读数件两腿分读，0 合并）** | — |
| `K-PJPC-2-3_三参数形式拒收记录继承` | **PASS（拒收记录沿用既有件字面，原样并报）** | — |
| `K-PJPC-3-5_失败处置词面` | **KD（横切预检件层）** | — |
| `K-PJPC-4-1_全链重验` | **PASS（本棒三项交付齐备；判定面变化须由 verdict-keeper 裁因）** | — |
| `K-PJPC-4-2_三态收口纪律` | **PASS（本棒 0 自创第四态、0 用模糊态充当结论）** | — |
| `K-PJPC-4-3_0不明收口` | **PASS（本棒全部甲案落点均附 γ 根因列）** | — |
| `K-PJPC-4-4_根因强制` | **PASS（根因沿既有件逐字并报，0 改写为工具失灵/命题被证伪）** | — |

**`K-PJPC-1-1` 逐本体三态（0 合并、0 择优）**：

| 本体 | 三态（可裁形式） | n_distinct | std |
|---|:-:|---:|---:|
| `O1_discrete_cell_redistribution` | **PASS** | 9 | 0.0012788884 |
| `O3_logit_normal_form` | **PASS** | 8 | 0.0044661691 |
| `O5_replicator_ode_softlimit` | **PASS** | 9 | 16.9800088427 |

**`K-PJPC-1-3`（P-M）**：PASS（≥1 档 detection_rate > 0 且 safety_budget_lower_bound 重测 80 ≥ 80）；天花板披露：n_distinct = 1、std = 0 ⇒ 属检测器饱和、非判据退化；⚠️ 不得单独充当「非退化」证据；判据非退化性由 input_fields 承担（沿 a0734e0a6860 §3.1）

**`K-PJPC-2-1`（P-C）**：PASS（9/9 个 η 档 n_distinct = 9）；as-run 对照 = [1, 1, 1, 1, 1, 1, 1, 1, 1]

**`K-PJPC-3-1_断言①方差>0`**（批 5 ①档：复用 K-V3R-0-A，0 新增门槛）：复用 K-V3R-0-A，0 新增门槛；命中面逐条见 §2；命中面 4 个 = ['P-C / asrun_退化面', 'P-J / asrun_退化面', 'P-M / asrun_退化面', 'P-M / 新构造面_3算子×9budget']；

**`K-PJPC-3-2_断言②秩不恒同`**（批 5 ②档：复用 n_distinct > 3 作近似代理（⚠️ 分布层近似，非排序层等义 —— 沿 prereg §1.4/§4.2 限定如实标注））：近似代理门：分布非退化 ≠ 排序非恒同；命中面逐条见 §2；命中面 4 个 = ['P-C / asrun_退化面', 'P-J / asrun_退化面', 'P-M / asrun_退化面', 'P-M / 新构造面_3算子×9budget']；本门为近似代理：分布非退化 ≠ 排序非恒同；PI 批 5 采此档 ⇒ 本棒沿用并显式标注其近似性质，0 声称等义

**`K-PJPC-3-3_断言③标签非硬编码`**（批 5 ③档：沿 P-I 诚实降级范式作【定性范式，明确非门】）：明确非门：3 族 × 6 面逐条定性登记，0 触发任何落态处置；登记面（非门，不构成门命中） 8 个 = ['P-C / asrun_退化面', 'P-C / 新构造面_纯log-log两参数', 'P-J / asrun_退化面', 'P-J / 新构造面_O1_discrete_cell_redistribution', 'P-J / 新构造面_O3_logit_normal_form', 'P-J / 新构造面_O5_replicator_ode_softlimit', 'P-M / asrun_退化面', 'P-M / 新构造面_3算子×9budget']；

**`K-PJPC-3-4_断言④检测率不低于随机基线`**（批 5 ④档：升独立门；切点 random_guess_rate = 0.5（盘上既有字段，0 新设））：升独立门、切点 0.5（盘上既有字段）；P-J / P-C 无该字段 ⇒ 如实登记 N/A；命中面 1 个 = ['P-M / asrun_退化面']；['P-J / asrun_退化面（该族无 detection_rate 字段）', 'P-J / 新构造面_O1_discrete_cell_redistribution（该族无 detection_rate 字段）', 'P-J / 新构造面_O3_logit_normal_form（该族无 detection_rate 字段）', 'P-J / 新构造面_O5_replicator_ode_softlimit（该族无 detection_rate 字段）', 'P-C / asrun_退化面（该族无 detection_rate 字段）', 'P-C / 新构造面_纯log-log两参数（该族无 detection_rate 字段）']

---

## §6 γ 根因登记（`K-PJPC-4-3` 强制）

- γ_A｜登记 vs 盘上：17262abfd1d5 §1.1 档 2 行『#26 P-J · 证据锚』记 rescript `3d9ad5f1540d`，而盘上 `results/_v3_recheck_26_rescript_2026_09_27.md` 实测 = `6b86576146a3`；同表其余 4 个 result 锚（eb6a99dd46dd / 49c6e5a07732 / c0a8cb9029a7 / 5d4b6baf1b18）逐字与盘上相符。⇒ 只报事实（1 件不符），0 归因、0 回改登记件、0 回改 rescript（K-PJPC-0-4）。
- γ_B｜26b r2/r3 executor 源件在盘、其新名派生 result 盘上 0 命中：`results/_v3_recheck_26b_executor_r2_2026_09_28.py`（0808af6212c5）与 `_v3_recheck_26b_executor_r3_2026_09_29.py`（6c83e7a7ca2e，mtime 2026-09-29 10:50）存在，但其 OUT 名 `_v3_recheck_26b_r2_result_*.json` / `_r3_result_*.json` 盘上 0 命中 ⇒ 该两轮跑批的派生读数【不在盘】。⇒ 本棒 P-J 新构造读数一律沿 prereg §2.1 锚定的 26b 正式档（rescript c300e74a082c / result 49c6e5a07732，mtime 2026-09-27 15:52），0 据 r2/r3 断言任何读数。
- γ_C｜P-M 新构造面（#28）断言 ① / ② 双命中：detection_rate 27 格全 1.0 ⇒ n_distinct = 1、std = 0。根因沿 a0734e0a6860 §3.1 自陈 = 【检测器饱和】而非判据退化；判据非退化性由 input_fields 承担（#28 `gate_per_field` 三项全 True）。⇒ 本棒按甲案落 KD + γ 并【显式保留该限定】，0 以天花板序列充当「非退化」证据（K-PJPC-1-3 硬约束）。
- γ_D｜断言 ② 的等义性限定：PI 确认批 5 采「复用 n_distinct > 3 作近似代理」档。该代理只在【分布层】成立，与断言 ② 字面（【排序层】两两序关系是否全同）非等义（沿 prereg §1.4/§4.2）。⇒ 本棒沿用该近似并逐处显式标注，0 声称等义；排序层等义门 0 自创。
- γ_E｜P-J / P-C 族无 `detection_rate` 字段 ⇒ 断言 ④ 独立门对该两族【不适用】。⇒ 本棒如实登记 N/A，0 当作通过、0 当作失败（0 以缺件充当门通过）。
- γ_F｜三族终态判定的词面裁定（prereg §2.2-3 甲/乙/丙）在本棒范围内【未裁】：PI 确认批 5 裁了三族修复档位（均 ②档）与 4 项断言门形态，0 触及 §2.2 词面裁定。⇒ 本棒横切预检件层按【甲案】落 KD + γ（棒 1 派工字面）；三族终态 0 代裁，归 verdict-keeper。
- γ_G｜P-C 证据面 / 命题面分读（K-PJPC-2-2）：新构造 9/9 η 档 n_distinct = 9 ⇒ 证据面 PASS；同件 `exp_d7_5anchor_60cells.P-C_two_phase` 字面仍 = `FAIL_H0 (幂律死)`、as-run max r2_per_eta = 0.19840149926690828 < 0.3。⇒ 本棒两腿分读并报，PASS 0 构成「幂律成立」证据（沿 fc0ffd27adca γ₃ 零噪声对照腿）。
- γ_H｜PI 确认批 5 问卷原件 0 命中于盘上 ⇒ 本棒裁项档位系【引用派工单字面】，0 独立复算问卷原件。

---

## §7 `K-PJPC-0-2` 写盘后逐件复算（17 件）

| # | 件 | 基线 SHA-12 | 写盘后实测 | 相符 |
|:-:|---|---|---|:-:|
| 1 | `results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json` | `a9ad1de618f5` | `a9ad1de618f5` | ✅ |
| 2 | `results/_p_m_attack_surface_cost_2026_09_16/p_m_attack_surface_cost_results_2026_09_16.json` | `fbcb60cf5102` | `fbcb60cf5102` | ✅ |
| 3 | `results/_p_m_real_separation_2026_09_16/p_m_real_separation_results_2026_09_16.json` | `a4b12d1cfedc` | `a4b12d1cfedc` | ✅ |
| 4 | `results/_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json` | `f39412103366` | `f39412103366` | ✅ |
| 5 | `results/_p_i_real_labels_2026_09_16/p_i_real_labels_results_2026_09_16.json` | `e934819ee9ed` | `e934819ee9ed` | ✅ |
| 6 | `results/_p_l_real_data_collapse_2026_09_16/p_l_real_data_collapse_results_v2_2026_09_16.json` | `afe975606d40` | `afe975606d40` | ✅ |
| 7 | `results/_p_l_p_c_finite_size_scaling_2026_09_16/p_l_p_c_finite_size_scaling_results_2026_09_16.json` | `664e7cc05aec` | `664e7cc05aec` | ✅ |
| 8 | `results/deposon_v42_v2_miss_rate_curve_2026_09_16.json` | `0a8ed127d6de` | `0a8ed127d6de` | ✅ |
| 9 | `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | `03c6c01f3697` | `03c6c01f3697` | ✅ |
| 10 | `docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md` | `d427b2f57c33` | `d427b2f57c33` | ✅ |
| 11 | `results/deposon_v3_physical_opt_60cells_2026_09_11.json` | `c659695aa23c` | `c659695aa23c` | ✅ |
| 12 | `results/_v3_recheck_prereg_v1_2026_09_27.md` | `88052d7db895` | `88052d7db895` | ✅ |
| 13 | `results/_v3_recheck_verdict_register_2026_09_27.md` | `17262abfd1d5` | `17262abfd1d5` | ✅ |
| 14 | `results/_v3_recheck_26_rescript_2026_09_27.md` | `6b86576146a3` | `6b86576146a3` | ✅ |
| 15 | `results/_v3_recheck_26b_rescript_2026_09_27.md` | `c300e74a082c` | `c300e74a082c` | ✅ |
| 16 | `results/_v3_recheck_28_rescript_2026_09_27.md` | `a0734e0a6860` | `a0734e0a6860` | ✅ |
| 17 | `results/_v3_recheck_10_rescript_2026_09_27.md` | `fc0ffd27adca` | `fc0ffd27adca` | ✅ |

**漂移件数 ＝ 0** ⇒ `K-PJPC-0-2` 达标。

---

## §8 0 越权 / 老实交代

- **0触原件frozen**：全部既有件只读加载；K-PJPC-0-2 锚表 17 件 + 读数链 4 件写盘前后逐件复算（见收口读数件 §7）
- **0出判定裁决**：K-PJPC-1-1/1-2/1-3/2-1/2-2/2-3/3-1…3-5 全部落【可裁形式】三态；终态判定归 verdict-keeper（棒 3）
- **0改阈值**：新设数值判定阈值 = 0（见 threshold_watch）
- **0读key**：R4 无例外沿用；本棒 0 读、0 引用任何 key 值
- **0代拟E条目报告措辞**：②档技术面材料 / 对账面材料只出可机械复算的证据面数字与约束；正式措辞 0 代拟（归 doc-writer）
- **0合并派生JSON**：本棒唯一新建 JSON 为横切预检件新名件（K-PJPC-0-3）
- **署名如实**：本件署 worker；不冒充 PI / protocol-keeper / verdict-keeper / evidence-auditor / doc-writer / Trae code
- **skill**：派工单未指定 skill 名 ⇒ 本棒 0 加载、0 引用、0 虚构任何 skill 条文；纪律锚 = 派工单字面 + 盘上既有件字面
- **自指指纹**：本件 SHA-12 0 自写入（自指不可解）⇒ 落盘后由收口回执以实测值回报

---

**本件 SHA-12**：**0 自写入**（自指不可解）⇒ 落盘后由收口回执以 `hashlib.sha256(全文字节).hexdigest()[:12]`（小写）实测回报。

**出证｜Mavis 团队 worker（棒 1 · 收口棒；agent 署名如实，不冒充 protocol-keeper / verdict-keeper / evidence-auditor / doc-writer / PI / Trae code）｜2026-09-29 下午**
