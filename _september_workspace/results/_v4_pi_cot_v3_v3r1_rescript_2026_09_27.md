# v3r1 rescript — D4 重标 v1.3 重跑（D4 重标 → 重训重跑 → 三列并报）

**件名**：`results/_v4_pi_cot_v3_v3r1_rescript_2026_09_27.md`
**背景拍板**：PI 问卷 `ask_ad37c9c9282a3edb0b881fe8` Q4「落 v1.3 重跑」
**性质**：D4 重标（`6EED9ACDB99A`）改 4 项 `judge_type` 特征 → 改树 → v3 读数可能变，**重跑验证并列新件**
**skill 锚**：`scientific-research-workflows:experimental-design`（plugin `@scientific-research-workflows`；Local skill 已核存在于 plugin-cache，SHA-12 树目录 `sha256-tree-v1-611965fcb…cb`）— 落到实处只用上一条字面纪律：**一次只变一个因子，其余 nuisance 钉死**，否则树变与标注变的效应不可分离。
**fallback**：未触发（Local skill 已找到，无虚构 skill 指令）。

---

## 0. 输入链核验（hashlib 实测，SHA-12 = `hashlib.sha256(data).hexdigest()[:12]`）

| 件 | SHA-12 实测 | 字节 | 与派工单锚 |
|---|---|---|---|
| `results/_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json` | `6EED9ACDB99A` | 18714 | ✅ 一致 |
| `results/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py` | `EE8671A28C2F` | 62115 | ✅ 一致 |
| `results/_v4_pi_cot_v3_dataset.json`（v1.2） | `5118F5B44F17` | 16025 | ✅ 一致 |
| `results/_v4_pi_cot_v3_result_v3.json` | `585714F9660C` | 27203 | ✅ 一致 |
| `results/_v4_pi_cot_v3_k3b_recheck_r1_2026_09_27.json` | `CBC14A76F038` | 26891 | ✅ 一致 |
| `results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json` | `CBF60A630C9F` | 20194 | 沿 result_v3 字面已登记漂移 |
| `results/_v4_pi_cot_v3_verdict_v3.md` | `BB44FDC7AB0F` | 53751 | 复验未动 |

**母件口径复现自校验**：本 runner 跑出的 r1 未重标读数与盘上 `k3b_recheck_r1` `main_reading_after` **11/11 项逐字相同**（n_held / nw / nled / n_divergent / n_crit_among_div / cov / n_agree / n_blind / blind_rate / bootstrap_ci / perm_p）→ 本 runner 与前棒同口径，读数可比。

---

## 1. 本次只变了一个因子（构造证据）

| 项 | v1.2 面 | v1.3 面 | 变化 |
|---|---|---|---|
| D4_Q1 | J6 | **J5** | changed |
| D4_Q2 | J6 | **J1**（J4 并记） | changed |
| D4_Q3 | J6 | **J5** | changed |
| D4_Q4 | J3 | **J4** | changed |
| D4_Q5 | J3 | J3 | 未变 |

**实测钉死项**（全部逐字不变）：

- `held_out_idx` 与 v3 **完全相同**（23 件：`0,2,5,6,7,12,13,16,23,27,28,36,37,39,47,50,58,59,63,66,72,74,76`）
- 全部 85 件 `reasoning_full` 逐字不变 → **label（由推理全文派生）逐字不变**
- 全部 85 件 `option_chosen` 逐字不变
- 非 D4 80 件 `judge_type` 逐字不变
- 种子/划分/树参/词表/阈值全部不动：`SEED=42`、`HELD_OUT_RATIO=0.30`、`TREE_DEPTH_MAX=6`、`N_PERM=1000`、`N_BOOT=1000`、12 特征集、NW +2/−1/−2、K-V3-\* 阈值 0.65/0.55/1.00/0.10/0.40 + sentinel

**特征面变化**（5 项二值特征，其余 7 项逐字不变）：

| 特征 | v1.2 和 | v1.3 和 | 变化件数 |
|---|---|---|---|
| `judge_type_J6` | 7 | 4 | 3 |
| `judge_type_J5` | 0 | 2 | 2 |
| `judge_type_J1` | 9 | 10 | 1 |
| `judge_type_J3` | 14 | 13 | 1 |
| `judge_type_J4` | 7 | 8 | 1 |

**树变构造面（如实登记，二者不可混谈）**：D4 五件中 **3 件落在 held-out**（idx 72/74/76）、**2 件落在训练集**（idx 73/75）→ 树由 2 件训练标注驱动，读数由 3 件 held-out 特征驱动。

---

## 2. 三列并报读数对比表（主读法，NW-sim + NLED-sim 双口径）

| 读数 | **v3 原**（母件 `8A81D90C69BA`） | **r1**（F1 修复后 `EE8671A28C2F`） | **v3r1**（重标后，本件） | v3r1 − v3 | v3r1 − r1 |
|---|---|---|---|---|---|
| NW-sim mean | 0.4534 | 0.4578 | **0.4665** | +0.0130 | +0.0087 |
| NLED-sim mean | 0.2754 | 0.2101 | **0.2319** | −0.0435 | +0.0217 |
| 分歧批判理由覆盖率 | 0.4286（6/14） | 0.6000（9/15） | **0.6000（9/15）** | +0.1714 | ±0 |
| 盲从率 | 0.2222（2/9） | 0.2500（2/8） | **0.2500（2/8）** | +0.0278 | ±0 |
| bootstrap CI (NW) | [0.3217, 0.5870] | [0.3559, 0.5634] | **[0.3522, 0.5851]** | — | — |
| perm_p | 0.0160 | 0.1878 | **0.1279** | +0.1119 | −0.0599 |
| n_held | 23 | 23 | **23** | ±0 | ±0 |
| n_divergent | 14 | 15 | **15** | +1 | ±0 |
| n_agree | 9 | 8 | **8** | −1 | ±0 |
| 树深 / 展平规则数 | 6 / 20 | 6 / 20 | **6 / 19** | −1 条规则 | −1 条规则 |

**alt 读法（剔 correction 子集，n_held=18）**：

| 读数 | v3 原 | r1 | **v3r1** |
|---|---|---|---|
| NW-sim mean | 0.5127 | 0.5016 | **0.5016** |
| NLED-sim mean | 0.2963 | 0.1852 | **0.1852** |
| 分歧批判理由覆盖率 | 0.3636 | 0.6154 | **0.6154** |
| 盲从率 | 0.2857 | 0.4000 | **0.4000** |
| bootstrap CI | [0.3722, 0.6611] | [0.3944, 0.6167] | **[0.3944, 0.6167]** |

→ **alt 读法 v3r1 与 r1 逐字相同**：剔 correction 后的 18 件 held-out 里，D4 落 held 的 3 件中 idx 76 被保留但特征对其预测无影响面 → 重标未传导到 alt 口径（如实观测，非计算遗漏）。

---

## 3. K-V3-\* 判定方向变化检查（阈值一字未动）

| 判死线 | 阈值 | v3 观察值 | r1 观察值 | **v3r1 观察值** | v3 hit | **v3r1 hit** | 方向变化 |
|---|---|---|---|---|---|---|---|
| K-V3-A（学习线 NW 主口径） | 0.65 | 0.4534 | 0.4578 | **0.4665** | True | **True** | 无 |
| K-V3-A'（学习线 NLED 副口径） | 0.55 | 0.2754 | 0.2101 | **0.2319** | True | **True** | 无 |
| K-V3-B（分歧批判覆盖率） | 1.00 | 0.4286 | 0.6000 | **0.6000** | True | **True** | 无 |
| K-V3-C（盲从率上限） | 0.10 | 0.2222 | 0.2500 | **0.2500** | True | **True** | 无 |
| K-V3-D（CI 下限） | 0.40 | 0.3217 | 0.3559 | **0.3522** | True | **True** | 无 |
| K-V3-E（双口径一致 sentinel） | sentinel | 一致 | 一致 | **一致** | False | **False** | 无 |

**判定方向变化总数 = 0**。K-V3-E 仍不触发，根因同 result_v3：NW 与 NLED **同向 FAIL**，不存在「一过一否」的构造面告警。

---

## 4. 改判语义

1. **并列不覆盖**：`result_v3r1`（`735C03DB1AE9`）与 `result_v3`（`585714F9660C`）**并列**；dataset v1.3（`ED596914259A`）与 v1.2（`5118F5B44F17`）**并列**。v1.2 / result_v3 / verdict_v3 **0 字节改动**（落盘后 SHA-12 复验见 §6）。
2. **v3 判定不翻**：v3 的 5/6 hit（K-V3-E 不触发）**原样有效**；本重跑**未推翻、未改写**该判定。
3. **重跑是换数据面，不是换判据**：阈值 0.65/0.55/1.00/0.10/0.40 + sentinel 一字未动；读数变只可能来自 `judge_type` 标注面。
4. **本件不替代 v3 判定**：若 PI 需以重标面为正式判定面，属 verdict-keeper 复核范围，**非本棒擅断**。

---

## 5. 防退化门（沿 PI 拍板③ 二值单列）

- `judge_type_J5` 的 n_distinct 由 **1 → 2**（D4 两件入 J5：1 件预测值 + 1 件负样本），仍属低基数。
- 其余 12 特征 n_distinct 与 v1.2 **完全一致**（`rf_pos_density` 47、`n_keywords_hit` 11、`scene_bucket_8` 8、`opt_bucket_8` 8、`rf_len_bucket` 4、J1/J2/J3/J4/J6 各 2、`is_corr_pair` 2）。
- 沿 PI 拍板③ **二值单列不展开**（未做 5/6 混合编码敏感性分析，如实登记为未做）。
- 沿 result_v3 §feature_degradation_check 字面：低基数是设计预期，**不触发 TH-v3-19 处置**。

---

## 6. 落盘件（4 件，全部新名并列）

| 件 | 路径 | 字节 | SHA-12 |
|---|---|---|---|
| dataset v1.3 | `results/_v4_pi_cot_v3_dataset_v1p3_2026_09_27.json` | 12975 | `ED596914259A` |
| result v3r1 | `results/_v4_pi_cot_v3_result_v3r1_2026_09_27.json` | 22292 | `735C03DB1AE9` |
| rescript（本件） | `results/_v4_pi_cot_v3_v3r1_rescript_2026_09_27.md` | （本件） | （落盘后实测） |
| runner | `.tmp/_run_v3r1_relabel.py` | 30875 | — |

**既有件 0 字节改动复验**（落盘后实测）：`dataset.json` `5118F5B44F17`／`result_v3.json` `585714F9660C`／`addendum_d4` `CBF60A630C9F`／`d4_relabel` `6EED9ACDB99A`／`executor_r1` `EE8671A28C2F`／`verdict_v3.md` `BB44FDC7AB0F`／`k3b_recheck_r1` `CBC14A76F038` — 全部与开工前一致。

**合规**：0 LLM / 0 key 落盘 / 0 派生 JSON 合并 / 0 擅调阈值 / 0 覆盖既有件 / S-40 命名 / 0 派生件合并入既有件。

---

## 7. 老实交代

1. **D4_Q2 的 J4 并记未跑平行重跑**：relabel addendum 字面以 J1 为主记、J4 并记（二者可辩）。本件按 J1 单值落地特征面，J4 只入 `judge_type_relabeled_alternative` 字段。**J4 主记的平行重跑未做**——属未覆盖面，如实登记，不代 PI 择一。
2. **二值单列未做敏感性分析**：沿 PI 拍板③ 未展开 5/6 混合编码；若 PI 要看「J6 消失后是否应合并类别」的影响，本件**未覆盖**。
3. **读数变化幅度小，根因已追**（不误导 > 机械诚实）：v3r1 相对 r1 的变化 NW +0.0087 / NLED +0.0217，根因是 4 件标注变更只落在 85 件中的 5 件、其中 2 件在训练集 3 件在 held-out，特征面变化仅 J6 −3 / J5 +2 属**小幅扰动**——读数方向可归因于标注，**不构成新证据**。展平规则数 20 → 19 是树变的直接体现。
4. **覆盖率与盲从率零变化非计算错误**：`cov` 0.6、`blind` 0.25 与 r1 完全相同，已逐件核对计数面（n_divergent 15 / n_critical_among_divergent 9 / n_agree 8 / n_blind_obey 2）——属如实观测。
5. **perm_p 与 v3 母件方向相反的根因不在本重标**：0.0160（v3）→ 0.1878（r1）→ 0.1279（v3r1），三者均 >/≤ alpha 0.05 的跨线发生在 **F1 修复**（改了 D1_supp 三件 reasoning_full，标签面同变），非重标所致。本棒只如实报读数，**不擅调 N_PERM / seed**。
6. **D4 addendum 源件未落地重标**：重标在内存生效（runner 层），`addendum_d4` 与 `d4_relabel` 两件均 0 字节改动。若 PI 要求源件级落地，需另派数据修订棒，**非本棒擅写源件**。
7. **succeeded ≠ 跑完**：本件与前两件均已 SHA-12 实测核验后才宣告。

---

**署名**：Mavis 团队 worker 出件｜2026-09-27


<!-- appended-note:2026-09-30 skill 引用面复核（PI 派工第④项 · 0 删改历史字面） -->

> **附注（2026-09-30 追加 · 非原件内容）**
> 本件原引用字面**逐字保留、0 删改**；本附注**只增不改**。
>
> - **原引用面**：L6（出现 2 处）· `experimental-design` 已核存在于 plugin-cache（树目录缩写）
> - **2026-09-30 只读复核**：原引用字面**2026-09-30 仍成立**（写死路径逐字在位、树哈希同目录名、`SKILL.md` SHA-12 对得上）⇒ **无过期值可改**，故仅追加注记、**不就地更新**
> - **当前三段式锚**（plugin:skill + 树哈希前 12 + SKILL.md SHA-12 + 定位方式）：scientific-research-workflows:experimental-design` · 树 ``611965fcb620`` · ``SKILL.md`` SHA-12 ``0a314eed103a`` / 13,044 B（实体直读；运行时加载行为见执行件 §6，**本棒 0 复现**）
> - **「历史实测 vs 今日实测」口径**：本件所记为**当时实测证据**，**保留有效、0 回改**；今日复核值以本附注与执行件为准，读者可据此区分二者（起因件建议 A2）。
> - **执行件**：`results/_skill_reference_update_and_user_surface_survey_2026_09_30.md` · 出件 **worker**（本棒）· **0 删改本件任何既有字节**