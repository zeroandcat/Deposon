# 任务 B v3 · 正式判定裁因收口（verdict-keeper，2026-09-27）

- **产物性质**：`prereg` → `dataset v1.2` → `ruleset_v3` → `result_v3` → **`verdict_v3`（本件，§8 产物链末件）**
- **任务角色**：verdict-keeper（裁因收口，不跑实验、不改数据、不独立复核执行棒判定、不动既有件）
- **性质**：**正式判定**（formal v3；result_v3.json `formal_judgment=true` + `exploratory=false` 字面；棒 C 执行棒 0 派生自 `verdict_v3`，沿棒 A/B/C 落盘链）
- **诚实纪律**（PI 2026-09-23 立）：诚实 = 不误导；执行棒 result_v3 自报 kill_lines 6 段（5 hit + K-V3-E 不触发）+ `any_hit_strict_5lines=true`，本件按 E-27 §13 判别要件复核后**逐行重判**；复合定性如实登记，不机械二选一，不软化
- **v1 → v2 → v3 演进锚**：
  - v1 verdict（EB9AD4193CF2）= 探索性预跑 FAIL 形态 + 假证伪疑点未排除（构造失灵族）
  - v2 verdict（5D79E67A4E9D）= 正式判定 FAIL 立案 + **复合定性 2β + 2 复合 + 0 纯 α**（构造面补正后 4 hit 全恶化 vs v1）
  - 本件 v3 = 正式判定 FAIL 立案 + **消解 A/B 落地后 5/6 hit 全 FAIL**（构造面已显式外移，但 FAIL 依旧——与 v2 复合定性的关键差异）

---

## §0 输入件 SHA-12 前 12 核验（只读，先核后用）

| 件 | 派工字面 | 核验值 | 状态 |
|---|---|---|---|
| `results/_v4_pi_cot_v3_result_v3.json` | 585714F9660C | **585714F9660C** | ✓ |
| `results/_v4_pi_cot_v3_ruleset_v3.json` | 9D77A5E2CBAB | **9D77A5E2CBAB** | ✓ |
| `results/_v4_pi_cot_v3_ruleset_v3_executor.py` | 8A81D90C69BA | **8A81D90C69BA** | ✓ |
| `results/_v4_pi_cot_v3_dataset.json` | 5118F5B44F17 | **5118F5B44F17** | ✓ |
| `results/_v4_pi_cot_v3_prereg.md` | B7547329AF2E | **B7547329AF2E** | ✓ |
| `results/_v4_pi_cot_v2_verdict_v2.md`（对照锚，只读） | 5D79E67A4E9D | **5D79E67A4E9D** | ✓ |

- 派生关系：result_v3.json 内嵌 `v3_prereg_anchor.sha12_actual_post_activation=B7547329AF2E` ✓ + `dataset_ref.sha12_actual=5118F5B44F17` ✓ + `ruleset_ref.sha12_actual=9D77A5E2CBAB` ✓ + `ruleset_ref.executor_sha12_actual=8A81D90C69BA` ✓；`v1_v2_anchors_preserved` 三件（v1_verdict_sha12=EB9AD4193CF2 + v2_verdict_sha12=5D79E67A4E9D + v2_signoff_sha12=BA4D07BD7000）字面冻结
- **1 件实测漂移**（按 result_v3 §anchor_sha_verification 字面 disclosure，不触动）：`_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json` 派工 briefing 字面锚 `B18FF4177289` vs executor 实测锚 `CBF60A630C9F`——本件 verdict-keeper 不擅重派此差异，按 result_v3 §honesty_note (ii) 字面「executor 仍按实测 SHA 锚入 (0 触动既有件)」处置，沿 supersede 案例模式归口（与 v2 ask_822b1e27 th23_span supersede 同款）
- **既有件 0 触动自查**：本件仅做只读核验（§0 SHA-12 表 + 字面读取）+ 落盘新件 `_v4_pi_cot_v3_verdict_v3.md`；v3 三件（dataset/ruleset_v3/result_v3）+ v2 全链 5 件（prereg/coding_review/ruleset_v2/ruleset_v2_executor/verdict_v2）+ 18 frozen + 9 网格 + 9 v2 addenda + 1 v3 d4 addendum 共 33 件既有资产字面冻结，本件无写入权限触达

---

## §1 核心裁因（诚实 = 不误导）

### §1.1 观测总览（主读法，全 23 held-out；substrate=77 = 64 v2 on-disk + 8 post-v2 in load + 5 D4）

| 维度 | v1（探索性预跑，11 held） | v2（正式判定，22 held） | **v3（正式判定，23 held）** | v2 → v3 方向 |
|---|---|---|---|---|
| 度量口径 | 召回率 \|pred∩actual\|/\|actual\| | 召回率（同款） | **NW-sim + NLED-sim 双口径并报** | **消解 B 落地（度量换代）** |
| 规则集上界 | 决策树 ≤4 + 9 特征 + primary 单元素 | 同款 | **决策树 ≤6 + 12 特征 + 全序列+短语模式** | **消解 A 落地（表现力上界扩展）** |
| substrate | N=37+11=48（D1 only） | N=72（含 D1 缺位 8 件） | **N=77（v2 on-disk 64 + post-v2 8 + D4 5）+ 8 D1 missing declared absent = 85 accounting** | **跨日 2 天 → 3 天；N 显著扩** |
| held-out count | 11 | 22 | **23** | 略增 |
| NW-sim mean | — | — | **0.4534** | v3 新线 |
| NLED-sim mean | — | — | **0.2754** | v3 新线 |
| （v2 对照）mean_similarity | 0.1818 | **0.0909**（召回率） | (无可比, 度量已换代) | — |
| div_critical_coverage | 0.6667 | **0.6842** | **0.4286** | **v3 ↓↓恶化** |
| blind_obey_rate | 0.0 | **0.3333** | **0.2222** | v3 ↓↓改善 |
| perm_p（n=1000, α=0.05） | 0.2937 | **0.7912** | **0.0160** | **v3 ↓↓↓显著改善** |
| bootstrap CI（n=1000, seed=42） | [0.0, 0.4545] | **[0.0, 0.2045]** | **[0.3217, 0.5870]** | **v3 ↑↑显著改善** |
| any_hit | True（3 hit） | True（4 hit） | **True（5 hit, 6 段中 5）** | v3 多 1 hit（K-V3-A' 学习线 NLED 副口径新立） |
| K-V3-E（双口径一致线） | — | — | **不触发（NW/NLED 同向 FAIL，direction_consistent=True）** | v3 新增构造面 sentinel |
| 总体 verdict | FAIL (exploratory) | FAIL (formal v2, 复合定性) | **FAIL (formal v3, 复合定性)** | 性质升级 + 复合定性深化 |

### §1.2 消解 A / 消解 B 实测落地（构造面补正已完成项）

> **v3 与 v2 复合定性的关键差异**（一句一次）：**v2 时"消解 A 表现力上限 + 消解 B 度量换代"系 β 面悬疑（未消解）——v3 时此二者已按锁定参数落地 = 构造面 PASS**——FAIL 依旧，但**根因信号已不来自构造失灵族主导**，而是**来自钳制边界外移后仍存的预测能力不足信号**。这是与 v2 复合定性"部分 β 主导"的关键差异。

#### §1.2.1 消解 A（规则集表现力上界）——实测落地 ✓

- **决策树深度 ≤6**：result_v3 §constraint.tree_depth_observed=6，threshold=6，**PASS 字面**（不超阈）；v2 = 4；扩展 1.5 倍已生效
- **特征 ≥12**：12 项特征落地（v2 既有 9 项 + v3 新增 judge_type_J5 + rf_pos_density + n_keywords_hit），**PASS 字面**
- **全序列返回 + 短语模式**：template_mode = `full_sequence_plus_phrase_patterns`；5 类短语模式（不误导/判死线先于/准则为根/大一统/判据序列）已落地，**PASS 字面**
- **防退化构造审查**：feature_degradation_check 字面——12 项中 7 项（judge_type_J1-J6 + is_corr_pair + judge_type_J5）n_distinct ≤3；按 result_v3 §feature_degradation_check 字面「二元特征 n_distinct=2 是设计预期, 非退化」+「judge_type_J5 仅 D4 启用（n_distinct=1）」，**不触发 TH-v3-19 退化警报**；此为本件可核验的消解 A 验收项之一

#### §1.2.2 消解 B（度量换代）——实测落地 ✓

- **NW 评分矩阵冻结**：match=+2 / mismatch=-1 / gap=-2（TH-v3-5/6/7 字面）一字不动；**不启用 NW 邻近类矩阵**（沿 v3 prereg §10.5 第 1 项处置）
- **NLED 公式冻结**：1 - edit_distance/max(len_a, len_b)（沿 v3 prereg §2.2.2 字面）
- **双口径并报不择优**：NW-sim 0.4534 / NLED-sim 0.2754 **两者并报**（result_v3 §main_reading 字面）
- **K-V3-E 构造面 sentinel**：observed_nw_nled_direction_consistent=true → **不触发警告**；消解 B 无内部矛盾

### §1.3 真证伪 vs 构造失灵甄别（v3 复合定性）

> **核心反差**（一句一次）：**消解 A + 消解 B 落地后（构造面 PASS），5/6 kill-line 仍 hit**——这与 v2「构造失灵族主导」的复合定性**形成方向反转**：v2 时 UNK 改善但 4 hit 全恶化（构造失灵掩护真证伪信号不足）；v3 时构造面补正已尽，**剩余 FAIL 信号系规则集对 PI 实际判据序列预测能力确有结构性不足**——但这**不构成纯 α 真证伪宣告**（n_held=23 小样本 + 8 件 divergence 中 6 件无批判词的边界疑点 + NW vs NLED 双口径下界差 0.18 = 度量仍有局部偏差），故仍归复合定性。

**判别四要件复核**（按 E-27 §13 字面）：

| 要件 | v2 状态 | **v3 状态** | 评注 |
|---|---|---|---|
| ① kill-line 先于实验冻结 | ✓ prereg §4 | ✓ prereg §4 + §10.1 锁后生效 | 两版同 |
| ② 构造非恒等非退化 | 部分满足（UNK 22.2%, 词表 263 词）+ **仍有疑点**（召回率度量下 sim=0 86.4%） | **完全满足**：消解 A 三项（≤6 + ≥12 + 全序列+短语）落地 + 防退化审查 PASS（7 项二元特征为设计预期，不触发 TH-v3-19 警报）+ 12 特征中 3 新（judge_type_J5/rf_pos_density/n_keywords_hit）已启用 | **v3 构造面显式外移** |
| ③ 素材面覆盖 claim 所需 | 到位（沿 PI ask_822b1e27 supersede：N=72, 跨日 2 天 supersede 达标） | **到位且扩展**：N=77 RUN（v2 on-disk 64 + post-v2 8 + D4 5）+ 跨日 3 天（D1 09-24 + D2/D3 09-26 + D4 09-27）+ D1 单日 56.5% ≤ 60% + D4 5 件非实时答题（既有 PI 判定材料编码，沿 result_v3 honesty_note (ii) 字面）+ 8 D1 missing 维持不补造（PI Q3 拍板） | **v3 显著改善** |
| ④ 度量有分辨力 | 疑点加剧（v2 召回率在 v2 词表下 86.4% sim=0） | **分辨力确认 + 局部偏差**：NW + NLED 双口径并报 + K-V3-E 同向 + NW 0.4534/NLED 0.2754 差 0.18（NLED 更严符合 prereg 设计预期）+ NW-sim 23 件 held-out 中 4 件 sim=1.0 + 4 件 sim=0.5/0.6（部分匹配）+ 14 件 sim=0.0/0.4286（实际=空或失配）——**NW 在部分匹配事件上的细粒度分辨力已生效**；**NLED 因编辑距离对短序列（<10 元素）严格归零**（沿 v3 prereg §2.2.3 字面已说明）——分辨力缺口 = 度量形式自身特性，非构造失灵 | **v3 度量分辨力确认** |

**判别结论**（一句一次）：要件 ① ✓ + ② 完全满足 + ③ 到位且扩展 + ④ 分辨力确认——**4 要件全部满足**（v2 时 ② ④ 不全满足）；按 E-27 §13 字面**可判 α 真证伪**——但本裁决**仍复合定性（部分 α 真证伪 + 部分 β 边界存疑）**，理由：(i) n_held=23 仍为小样本结构性高方差；(ii) 8 件 divergence 中 6 件无批判词（盲区系批判反思词表边界 + actual=[] 4 件语义层混叠，非规则集能力上限本身）；(iii) NW vs NLED 下界差 0.18 = 度量形式特性差异（短序列归零）非构造失灵但仍为边界存疑；(iv) D4 5 件非实时答题（D2/D3 既有判定材料编码，无新 PI 实时事件）——信号虽达但**不纯**。

### §1.4 复合定性（不机械二选一）

> **本裁决核心定性**（一句一次）：**部分 α 真证伪信号 + 部分 β 边界存疑**——
>
> - **真证伪面**：(i) 消解 A 表现力上界已扩展至决策树 ≤6 + 12 特征 + 全序列+短语模式（构造面已尽），(ii) 消解 B 度量已换代为 NW + NLED 双口径并报（分辨力已确认），(iii) 素材面已扩展至 N=77 RUN + 跨日 3 天 + 单日 ≤60%，(iv) NW-sim mean 0.4534（主读法 23 held-out）/ NLED-sim mean 0.2754 / 4 件 sim=1.0 + 4 件 sim=0.5/0.6 的部分匹配信号已存——**预测能力不足信号在构造面已显式外移后仍存**——这是**部分真证伪**而非纯构造失灵
>
> - **构造/边界存疑面**：(i) n_held=23 小样本结构性高方差（NW-sim std 仍待核 — 沿 result_v3 字面 4 件 sim=1.0 + 4 件 sim=0.5/0.6 + 14 件 sim=0.0/0.4286 分布极端偏态）；(ii) 8 件 divergence 无批判词 = 批判反思词表边界 + actual=[] 4 件语义层混叠（v2 时 6 件，v3 时扩为 8 件——系 D4 5 件 + D3 三读扩展的混合产物，非词表衰退）；(iii) NW vs NLED 双口径下界差 0.18 = 度量形式特性差异（NLED 短序列严格归零），非构造失灵但仍为边界存疑；(iv) D4 5 件非实时答题（既有 PI 判定材料编码）——信号强度受素材性质制约
>
> - **不外推面**：本复合定性**不构成**「PI 思维链不可蒸馏」或「批判性学习维度不可能达标」的命题层宣告——构造/边界存疑面所述 4 项疑点任一不消解，复合定性上限即被钳制在「当前规则集（v3 词表 263 + 决策树 ≤6 + 12 特征 + 全序列+短语模式）+ 当前度量（NW-sim + NLED-sim 双口径）+ 当前素材（substrate=77 + 8 D1 missing declared absent + D4 5 件非实时编码）」边界内（详见 §5）

### §1.5 v1 → v2 → v3 反常信号演进的具体解读

| 反常 | v1 → v2 方向 | **v2 → v3 方向** | 根因（构造面 vs 真证伪信号） |
|---|---|---|---|
| NW-sim（主学习线） | — | **0.4534 vs 阈值 0.65** | **v3 新立 NW-sim（无 v2 对照）**——但 v2 召回率 0.0909 vs v3 NW 0.4534 数量级显著抬升 = 消解 B（度量换代）已生效；NW < 阈值仍 FAIL = 规则集预测能力不足信号**部分真证伪** |
| NLED-sim（副学习线） | — | **0.2754 vs 阈值 0.55** | 同上；NLED < NW = 度量形式特性（NLED 短序列严格归零），非构造失灵 |
| 批判覆盖 | 0.6667 → 0.6842 略升 | **0.6842 → 0.4286 ↓↓恶化** | **复合**——v3 14 件 divergence 中 8 件无批判词（v2 19 件 divergence 中 6 件无批判词）；新增 divergence 多源于 D4 5 件 + D3 三读扩展（既有判定材料编码，非实时 PI 事件）；批判反思词表边界 + actual=[] 4 件语义层混叠 = β 边界存疑主导；v3 规则集表现力扩展未触及该面 |
| 盲从率 | 0.0 → 0.3333 ↑↑恶化 | **0.3333 → 0.2222 ↓改善** | **真证伪面 + β 边界并存**——v3 9 一致事件中 2 件盲从（idx=5 KILL_LINE + idx=23 CRITERIA vs [TIMING, CRITERIA]）；盲从样本 n=9 仍小样本结构性高方差；idx=23 沿 v2 verdict §2.3 字面已在 v2 时被标为盲从事件（v2 reasoning 短句下 35 批判反思词未触，v3 词表沿 v2 不变）；**复合** |
| perm_p | 0.2937 → 0.7912 ↑恶化 | **0.7912 → 0.0160 ↓↓↓显著改善** | **真证伪面**（主导）——v3 规则集在 perm 重排下表现**显著区别于随机**（perm_p < α=0.05），即规则集对 PI 实际判据序列**确有可学习结构**（v2 perm_p=0.7912 接近 1.0 = 规则集特异性下降，v3 显著逆转）——这是构造面补正后暴露的**部分真证伪信号** |
| bootstrap CI | [0.0, 0.4545] → [0.0, 0.2045] ↓ | **[0.0, 0.2045] → [0.3217, 0.5870] ↑↑** | **真证伪面 + β 边界并存**——v3 CI 全段上移 + 下界从 0.0 抬至 0.3217 = 构造面补正后 sim 分布下界托举（NW 部分匹配信号生效）；下界仍 < 0.40 = 23 件小样本偏态分布产物；v3 比 v2 显著改善但**未达 K-V3-D 阈值** |
| K-V3-E 双口径一致 | — | **direction_consistent=True（不触发）** | **消解 B 真正消解**——NW/NLED 主读法判定方向同向 FAIL = 度量形式面无分歧警告（与 v2 单口径构造失灵形成对照） |

**反常解读结论**（一句一次）：v2 → v3 反常信号的方向**整体转向**：v2 时 UNK 改善但 4 hit 全恶化（构造失灵族掩护真证伪信号不足）；v3 时消解 A + 消解 B 落地后，**真证伪信号从构造失灵掩护下暴露**（perm_p 0.7912 → 0.0160 显著改善；NW-sim 0.4534 vs v2 召回率 0.0909 数量级抬升；CI 下界 0.0 → 0.3217），**但批判覆盖与盲从率仍部分恶化/受 β 边界钳制**——按 E-27 §13 不软化判死，但要按诚实纪律如实分项归类。

---

## §2 kill-line 判定表（逐行附根因）

**字面依据**：v3 prereg §4.2（K-V3-A/A'/B/C/D/E）+ §4.3（TH-v3-10 = 0.65 / TH-v3-11 = 0.55 / TH-v3-12 = 1.00 / TH-v3-13 = 0.10 / TH-v3-14 = 0.40 / K-V3-E sentinel 字面）。本表不调任何阈值，不私设任何条款。

**根因三分类**（沿用 E-27 §13）：
- **(α) 命题层面被证伪（真证伪）**：判别四要件全满足且**无 β 边界存疑**。
- **(β) 构造/工具层面失灵（假证伪）**：要件 ②/③/④ 任一不满足——观测失败可归构造退化或素材面不足。
- **(γ) 不明**：证据不足以判 (α) 或 (β)。
- **复合定性行**：明示"部分 α 真证伪信号 + 部分 β 边界存疑"。

### §2.1 K-V3-A · 学习线（NW-sim 主口径 mean < 0.65）

| 字段 | 字面 |
|---|---|
| 规则 | NW-sim mean（主读法）< 0.65 → FAIL |
| 阈值 | TH-v3-10 = 0.65（v3 prereg §4.3 字面） |
| 观测值 | NW-sim mean = **0.4534**（主读法，n=23 held-out） |
| hit 方向（显式） | 观测值 < 阈值 → **hit=True** 即触发 |
| hit 结果 | **True**（0.4534 < 0.65 成立） |
| 替代读法观测 | NW-sim mean = **0.5127**（n=18，剔 correction），主-替 delta = **+0.0593**（双读基本一致） |
| **根因** | **复合定性：部分 α 真证伪信号 + 部分 β 边界存疑**——见根因分析 |
| **形式效力** | **正式判定** |

**根因分析**：
1. **判别要件复核**：
   - ① kill-line 先于冻结 ✓（v3 prereg §4.2 + §10.1 拍板生效锁后未动）
   - ② 构造非恒等非退化——**完全满足**（决策树 ≤6 + 12 特征 + 全序列+短语模式 + 防退化审查 PASS，二元特征 n_distinct=2 为设计预期）；v2 时疑点（召回率度量下 sim=0 86.4%）在 v3 度量换代后**已消解**
   - ③ 素材面覆盖——**到位且扩展**（N=77 RUN + 跨日 3 天 + 单日 ≤60% + 8 D1 missing declared absent）；v2 时沿 PI ask_822b1e27 supersede 到位，v3 进一步达标
   - ④ 度量有分辨力——**分辨力确认**（NW 双口径并报 + K-V3-E 同向 + NW 0.4534 中 4 件 sim=1.0 + 4 件 sim=0.5/0.6 部分匹配信号生效；NLED 短序列严格归零系度量形式特性非构造失灵）
2. **真证伪面证据**：(i) 消解 A + 消解 B 落地后 NW-sim 仍 < 阈值 = 规则集对 PI 实际判据序列预测能力确有结构性不足；(ii) NW vs 阈值缺口 = 0.1966（< 阈值 30.2%）——非边缘信号；(iii) NW 在部分匹配事件（sim=0.5/0.6）的细粒度分辨力已生效，但仍 < 阈值 = 部分真证伪
3. **构造/边界存疑面证据**：(i) n_held=23 仍为小样本结构性高方差；(ii) NW vs NLED 差 0.18 = 度量形式特性差异（NLED 短序列归零），非构造失灵但仍为边界存疑；(iii) 4 件 sim=0.0 事件（idx=2, 37, 39, 47, 50, 59）实际=空 + pred=UNK/CRITERIA = **NW 全局对齐在空序列上定义边界**（沿 v3 prereg §2.2.1 字面归零），非构造失灵
4. **裁因结论**：观测 hit 成立 + 真证伪面信号显著（NW < 阈值 30.2% 非边缘）+ 构造面已显式外移 + 边界存疑面 n_held 小样本 + 度量形式特性差异并存 → **复合定性（部分 α 真证伪 + 部分 β 边界存疑）**；**按诚实纪律不软化**：构造面与真证伪面**并存而非择一**

### §2.2 K-V3-A' · 学习线（NLED-sim 副口径 mean < 0.55）

| 字段 | 字面 |
|---|---|
| 规则 | NLED-sim mean（主读法）< 0.55 → FAIL |
| 阈值 | TH-v3-11 = 0.55（v3 prereg §4.3 字面） |
| 观测值 | NLED-sim mean = **0.2754**（主读法，n=23 held-out） |
| hit 方向（显式） | 观测值 < 阈值 → **hit=True** 即触发 |
| hit 结果 | **True**（0.2754 < 0.55 成立） |
| 替代读法观测 | NLED-sim mean = **0.2963**（n=18，剔 correction），主-替 delta = **+0.0209**（双读基本一致） |
| **根因** | **复合定性：部分 α 真证伪信号 + 部分 β 边界存疑**——见根因分析 |
| **形式效力** | **正式判定** |

**根因分析**：
1. **判别要件复核**：①②③④ 全部满足（同 K-V3-A 字面）；NLED 公式冻结 + 双口径并报已生效
2. **真证伪面证据**：(i) NLED 仍 < 阈值 = 规则集在编辑距离视角下对 PI 判据序列仍有结构性不足；(ii) NLED vs 阈值缺口 = 0.2746（< 阈值 49.9%）——**比 K-V3-A 更严**（NW 缺口 30.2%）；(iii) NLED 是编辑视角稳健基线，与 NW 同向 FAIL = **消解 B 真正消解**（K-V3-E 不触发）
3. **构造/边界存疑面证据**：(i) **NLED 短序列严格归零系度量形式特性**（沿 v3 prereg §2.2.3 字面说明：对 ['CRITERIA'] vs ['CRITERIA', 'RISK'] 短序列编辑距离严格归零边界，与 LCS 同类退化）——**非构造失灵但为度量形式边界**；(ii) NW vs NLED 差 0.18 = 度量形式差异，非构造失灵；(iii) n_held=23 小样本结构性高方差
4. **裁因结论**：观测 hit 成立 + NLED 与 NW 同向 FAIL + 真证伪面信号显著（缺口 49.9% 严于 NW）+ 度量形式特性边界（短序列归零）并存 → **复合定性（部分 α 真证伪 + 部分 β 度量形式边界存疑）**

### §2.3 K-V3-B · 批判覆盖线（div_critical_coverage < 1.00）

| 字段 | 字面 |
|---|---|
| 规则 | 分歧批判理由覆盖率 < 100% → FAIL |
| 阈值 | TH-v3-12 = 1.00（v3 prereg §4.3 字面，沿 v2 TH-v2-5b 字面） |
| 观测值 | div_critical_coverage = **0.4286**（主读法，n=23；n_divergent=14, n_critical_among_divergent=6） |
| hit 方向（显式） | 覆盖率 < 1.00 → **hit=True** 即触发 |
| hit 结果 | **True**（0.4286 < 1.00 成立） |
| 替代读法观测 | div_critical_coverage = **0.3636**（n=18，剔 correction；n_divergent=11, n_critical_among_divergent=4），主-替 delta = **-0.0650**（替代读法更恶化） |
| **根因** | **β 边界存疑主导 + 部分 α 真证伪**——见根因分析 |
| **形式效力** | **正式判定** |

**根因分析**：
1. **8 件无批判词分歧事件**（per_event, divergent=true ∧ has_critical_reflection=false）：
   - **idx=12**（sim=0.5/0.0, pred=CRITERIA vs actual=[TIMING]）：v2 时已标，v3 仍 UNK 边界（极短推理 / 三读漂移）；批判反思词表 v3 沿 v2 不变（v2 = 35 词，v3 = 36 词，沿 v3 ruleset `v2_critical_marker_count=36` 字面）
   - **idx=28**（sim=0.5/0.0, pred=CRITERIA vs actual=[RISK]）：v2 时已标，v3 仍 CRITERIA primary 同；reasoning 短句下批判反思词未触
   - **idx=37**（sim=0.0/0.0, pred=UNK vs actual=[]）：v2 时已标，v3 仍 UNK + actual=空
   - **idx=39**（sim=0.0/0.0, pred=UNK vs actual=[]）：v2 时已标
   - **idx=47**（sim=0.0/0.0, pred=UNK vs actual=[]）：v3 新增（D4 5 件？需逐件核 — 实际 idx=47 来源待核，本棒 worker 已老实交代素材面扩的归因）
   - **idx=50**（sim=0.0/0.0, pred=UNK vs actual=[]）：v2 时已标
   - **idx=72**（sim=0.3/0.0, pred=CRITERIA vs actual=[TIMING, KILL_LINE]）：v3 新增（D4？需逐件核）
   - **idx=74**（sim=0.5/0.0, pred=CRITERIA vs actual=[TIMING]）：v3 新增（D4？需逐件核）
2. **构造/边界存疑面证据**（主导）：
   - **批判反思词表 v3 沿 v2 不变**（35→36 词，沿 v3 ruleset 字面）——消解 A 附属（短语模式）未触及该面（短语模式匹配的是判据类型序列，不补充批判反思词表）
   - **8 件无批判词中 4 件 actual=[]**（idx=37, 39, 47, 50）——v3 词表下"pred 命中但 actual 空"事件本身可能不构成"有批判词但实际无批判反思"，而是 **actual 序列编码后空序列 = 无 6 类词命中**；此种情形下"批判反思词表覆盖不足"与"actual 序列空"两个问题混杂——与 v2 verdict §2.2 字面同款疑点
   - **v3 新增 divergence 多源于 D4 5 件 + D3 三读扩展**（既有判定材料编码，非实时 PI 事件；沿 result_v3 §honesty_note (ii) 字面）——非批判反思词表衰退，而是素材面扩后临界事件增加
   - 余下 4 件 actual 非空（idx=12, 28, 72, 74）：v1 → v2 → v3 双读中 idx=12/28 v1 UNK/CRITERIA → v2/v3 未变；idx=72/74 v3 新增——6 类主词表未变，批判反思词表扩 1 词（36 - 35 = 1，沿 v3 ruleset 字面）未触及这 4 件语境
3. **真证伪面证据**（弱）：
   - v3 词表已涵盖主要批判反思语境，8 件漏检主要为边界情形（actual=[] 或极短推理）+ D4/D3 三读扩展的素材扩产物
4. **裁因结论**：观测 hit 成立 + 构造/边界存疑面证据（词表边界 + actual=[] 语义层混叠 + 素材扩产物）**主导** + 真证伪面证据弱 → **β 边界存疑主导 + 部分 α 真证伪**

### §2.4 K-V3-C · 盲从率线（blind_obey_rate > 0.10）

| 字段 | 字面 |
|---|---|
| 规则 | 盲从率 > 0.10 → FAIL |
| 阈值 | TH-v3-13 = 0.10（v3 prereg §4.3 字面，沿 v2 TH-v2-5b 字面） |
| 观测值 | blind_obey_rate = **0.2222**（主读法，n=23；n_agree=9, n_blind_obey=2） |
| hit 方向（显式） | 盲从率 > 阈值 → **hit=True** 即触发 |
| hit 结果 | **True**（0.2222 > 0.10 成立）——**v1 此项为 False（0.0），v2/v3 此项 True** |
| 替代读法观测 | blind_obey_rate = **0.2857**（n=18，剔 correction），主-替 delta = **+0.0635**（替代读法更恶化） |
| **根因** | **复合定性：部分 α 真证伪信号 + 部分 β 度量假象（小样本高方差）**——见根因分析 |
| **形式效力** | **正式判定** |

**根因分析**：
1. **9 个一致事件**（divergent=false）逐件核（按 result_v3 §main_reading.per_event 字面）：
   - **idx=0**（sim=1.0/1.0, pred=RISK vs actual=[RISK], has_critical=true）：v3 NW 全对齐命中 + 批判词命中——一致且批判 ✓
   - **idx=5**（sim=1.0/1.0, pred=KILL_LINE vs actual=[KILL_LINE], has_critical=**FALSE**）：**v3 盲从事件**——NW 全对齐 + 批判反思词未触（reasoning 短句"不知不..."类认识论句；v2 verdict §2.2 idx=5 字面已有标注）
   - **idx=6**（sim=0.6/0.5, pred=RISK vs actual=[CRITERIA, RISK], has_critical=true）：NW 部分匹配 + 批判词命中——一致且批判 ✓
   - **idx=7**（sim=1.0/1.0, pred=CRITERIA vs actual=[CRITERIA], has_critical=true）：v3 NW 全对齐 + 批判词命中 ✓
   - **idx=13**（sim=0.6/0.5, pred=RISK vs actual=[RISK, CRITERIA], has_critical=true）：NW 部分匹配 + 批判词命中 ✓
   - **idx=16**（sim=1.0/1.0, pred=CRITERIA vs actual=[CRITERIA], has_critical=true）：v3 NW 全对齐 + 批判词命中 ✓
   - **idx=23**（sim=0.6/0.5, pred=CRITERIA vs actual=[TIMING, CRITERIA], has_critical=**FALSE**）：**v3 盲从事件**——NW 部分匹配（CRITERIA 共享 + TIMING 缺"分批"/"两步"等关键词）+ 批判反思词表未触（沿 v2 verdict §2.3 字面已标）
   - **idx=27**（sim=0.6/0.5, pred=CRITERIA vs actual=[CRITERIA, RISK], has_critical=true）：NW 部分匹配 + 批判词命中 ✓
   - **idx=63**（sim=0.6/0.5, pred=RISK vs actual=[RISK, KILL_LINE], has_critical=true）：NW 部分匹配 + 批判词命中 ✓
2. **真证伪面证据**（弱但存在）：
   - 2 件盲从事件（idx=5 KILL_LINE + idx=23 CRITERIA vs [TIMING, CRITERIA]）= 规则集预测与 PI 实际判据序列部分一致（CRITERIA/KILL_LINE 共享），但 PI 未给出批判反思词 = **"无理由一致"信号**；
   - v3 词表下此类事件 = 规则集在不知 PI 是否会批判反思下预测 = **盲从型一致**
3. **构造/边界存疑面证据**（主导）：
   - **n_agree=9 极小样本**——2 件事件即决定 0.0 vs 0.2222 vs 0.2857 = **结构性高方差**；
   - 替代读法 blind_obey_rate=0.2857（剔 correction 子集后 n_agree=7, n_blind_obey=2）——**主-替双读同向恶化**（delta +0.0635），与 v2 时 K-V2-b2 主-替完全分歧（0.3333 vs 0.0, delta -0.3333）形成对比；
   - idx=5 + idx=23 reasoning 短句下批判反思词表 35→36 词确实**未覆盖**该具体语境——词表边界疑点（v2 verdict §2.2 idx=5/12/28/37/50/53 字面已明示）
4. **裁因结论**：观测 hit 成立 + 真证伪面证据弱（仅 2 件事件）+ 构造/边界失灵面证据强（n=9 小样本 + 主-替同向 + 词表边界） → **复合定性（部分 α 真证伪 + 部分 β 度量假象/词表边界）**

### §2.5 K-V3-D · 稳健线（bootstrap CI 下界 < 0.40）

| 字段 | 字面 |
|---|---|
| 规则 | bootstrap CI（1000, seed=42）下界 < 0.40 → FAIL |
| 阈值 | TH-v3-14 = 0.40（v3 prereg §4.3 字面，v2 = 0.50） |
| 观测值 | bootstrap CI = **[0.3217, 0.5870]**（主读法，n=1000, seed=42） |
| hit 方向（显式） | CI 下界 < 0.40 → **hit=True** 即触发 |
| hit 结果 | **True**（0.3217 < 0.40 成立） |
| 替代读法观测 | bootstrap CI = **[0.3722, 0.6611]**（n=18，剔 correction），主-替 delta 下界 = **+0.0505** / 上界 = **+0.0741** |
| **根因** | **β 边界存疑主导 + 部分 α 真证伪**——见根因分析 |
| **形式效力** | **正式判定** |

**根因分析**：
1. **CI 下界 = 0.3217**：percentile method 在 n=23 held-out 下，bootstrap 1000 次重采子集极端悲观产物（NW-sim 分布偏态：4 件 sim=1.0 + 4 件 sim=0.5/0.6 + 14 件 sim=0.0/0.4286 + 1 件 sim=0.4286 = 极端偏态）
2. **替代读法 CI=[0.3722, 0.6611]**：n=18 held-out + sim 分布更分散（剔 correction 后 sim>0 事件占比上升）→ 下界从 0.3217 升至 0.3722（仍 < 0.40）；**主-替双读同向但替代读法上界已达标 0.6611**
3. **构造/边界存疑面证据**（主导）：
   - 23 件 held-out 中 NW-sim 分布极端偏态（4 件 sim=1.0 + 4 件 sim=0.5/0.6 + 14 件 sim=0.0/0.4286）→ CI 下界触底是 sim 分布偏态 + percentile method 在小样本下的**确定性下限**；
   - sim=0.0 主导的根因 = 6 件 actual=[]（idx=2, 37, 39, 47, 50, 59）下 NW 全局对齐定义边界（沿 v3 prereg §2.2.1 字面归零），非度量形式失灵
4. **真证伪面证据**（弱）：
   - **上界 0.5870（主读法）/ 0.6611（替代读法）均高于 v2 的 0.2045/0.3382**——消解 A + 消解 B 落地后 CI 上界显著抬升 = 部分匹配信号托举；
   - 但下界 0.3217（主）/ 0.3722（替）仍 < 0.40 = 95% CI 下段在阈值下——**信号方向一致但边界临界**
5. **裁因结论**：观测 hit 成立 + 构造/边界存疑面证据（sim 分布偏态 + actual=[] 边界 + 小样本）**主导** + 真证伪面证据（CI 上界显著抬升但下界边界临界）**弱但存在** → **β 边界存疑主导 + 部分 α 真证伪**

### §2.6 K-V3-E · 双口径一致线（构造面 sentinel）

| 字段 | 字面 |
|---|---|
| 规则 | NW-sim 与 NLED-sim 主读法判定方向不一致（一过一否）→ 消解 B 未真正消解警告；verdict-keeper 必须复核构造面而非机械判 FAIL/PASS |
| 观测值 | observed_nw_pass = **False**（K-V3-A hit）<br>observed_nled_pass = **False**（K-V3-A' hit）<br>observed_nw_nled_direction_consistent = **True** |
| hit 方向（显式） | 方向不一致即触发 → **hit=False**（consistent=True 即不触发） |
| hit 结果 | **False**（consistent=True）→ **不触发 sentinel 警告** |
| 替代读法观测 | K-V3-A 替 = 0.5127（< 0.65 FAIL）/ K-V3-A' 替 = 0.2963（< 0.55 FAIL）→ 替代读法双口径同向 FAIL |
| **根因** | **不适用**（sentinel 未触发；消解 B 真正消解的构造面验收证据） |
| **形式效力** | **正式判定**（消解 B 验收通过） |

**根因分析**：
1. **sentinel 设计意图**（沿 v3 prereg §4.2 字面）：v2 教训 = 单口径构造失灵被掩盖；v3 引入 K-V3-E 作为**构造面 sentinel**——双口径不一致即警告构造面存疑，verdict-keeper 不得机械判 FAIL/PASS
2. **本次实测**：NW-sim mean 0.4534 < 0.65 FAIL + NLED-sim mean 0.2754 < 0.55 FAIL → **两口径同向 FAIL**（direction_consistent=True）
3. **构造面验收结论**：**消解 B 真正消解**——度量形式面无内部矛盾；K-V3-E 不触发 = NW 与 NLED 在 [0,1] 区间分布特性不同（NW 因 gap penalty 惩罚 + 全局对齐 mean 偏高；NLED 因编辑距离 / max 归一 mean 偏低）的设计预期**已实测验证**
4. **裁因结论**：sentinel 未触发 = **消解 B 验收通过**；本件 §2.1 / §2.2 根因分析中**不计入度量形式面分歧**

### §2.7 kill-line 根因三分类汇总

| kill-line | v1 hit | v2 hit | **v3 hit** | v3 根因三分类 | v2 → v3 演化 |
|---|---|---|---|---|---|
| K-V3-A 学习线（NW 主） | — | — | **True** | **复合：部分 α 真证伪 + 部分 β 边界存疑** | (v2 无对照) NW 0.4534 vs 阈值 0.65 |
| K-V3-A' 学习线（NLED 副） | — | — | **True** | **复合：部分 α 真证伪 + 部分 β 度量形式边界** | (v2 无对照) NLED 0.2754 vs 阈值 0.55 |
| K-V3-B 批判覆盖 | True | True | **True** | **β 边界存疑主导 + 部分 α 真证伪** | 0.6842 → 0.4286 ↓↓恶化 |
| K-V3-C 盲从率 | False | True | **True** | **复合：部分 α 真证伪 + 部分 β 度量假象/词表边界** | 0.3333 → 0.2222 ↓↓改善 |
| K-V3-D 稳健线 | True | True | **True** | **β 边界存疑主导 + 部分 α 真证伪** | [0.0,0.2045] → [0.3217,0.5870] ↑↑改善 |
| K-V3-E 双口径一致 | — | — | **False** | **不适用**（sentinel 未触发 = 消解 B 验收通过） | (v3 新增构造面 sentinel) |
| **any_hit (5 段)** | True (3) | True (4) | **True (5)** | **3 复合 + 2 β 主导 + 1 sentinel PASS + 0 纯 α** | v3 多 1 hit（K-V3-A' 新立） |

**总体裁因**（一句一次）：**FAIL 立案**（K-V3-A/A'/B/C/D 五段全部 hit, K-V3-E 不触发）+ **复合定性**：3 个 kill-line 根因为复合（K-V3-A + K-V3-A' + K-V3-C）；2 个 kill-line 为 β 边界存疑主导（K-V3-B + K-V3-D）；K-V3-E 不适用 = 消解 B 验收通过；**0 个 kill-line 为纯 α 真证伪**——本裁决**不机械判全 α 也不判全 β**；与 v2 复合定性差异 = **v2 时 β 构造失灵族部分主导**（召回率度量 + 决策树 ≤4 能力上限 + 批判反思词表边界），**v3 时 β 边界存疑族主导但消解 A/B 已显式外移**（构造面补正已尽，剩余 β 系度量形式边界 + actual=[] 语义层混叠 + 小样本结构性高方差）。

---

## §3 FAIL 立案与外推边界（与死同行）

### §3.1 正式判定 FAIL 立案

> **FAIL 立案内容**（一句一次）：**在当前规则集（v3 词表 263 词 + 36 批判反思词 + 决策树 ≤6 + 12 特征 + 全序列+短语模式 + 防退化审查 PASS）+ 当前素材（substrate=77 RUN = 64 v2 on-disk + 8 post-v2 D3_w2/w3 in load + 5 D4；+ 8 D1 missing declared absent = 85 accounting；跨日 3 天；D1 单日 56.5% ≤ 60%）+ 当前度量（NW-sim + NLED-sim 双口径并报 + bootstrap percentile 1000 + perm 1000）条件下，观测落入 K-V3-A/A'/B/C/D 五段 hit 区域，K-V3-E 双口径一致线不触发——本裁决正式判定 FAIL**。

### §3.2 不外推边界（与 v1/v2 verdict 同款）

**不可外推**（防误用）：
- 不可外推至「**PI 思维链不可蒸馏**」或「**批判性学习维度不可能达标**」——本裁决复合定性中 K-V3-A/A'/C 真证伪面**信号显著但部分 α + 部分 β 边界存疑**（NW < 阈值 30.2% / NLED < 阈值 49.9% / 盲从 n=9 小样本），K-V3-B/D 真证伪面证据**未达命题层宣告**（v3 比 v2 显著改善 / 边界临界）；按 E-27 §13 + 本件 §2 复合定性，外推边界须显式声明
- 不可外推至「v3 消解 A/B 落地无效」——**消解 A 三项 + 消解 B 双口径 + K-V3-E 同向 = 构造面已显式外移**；FAIL 依旧系规则集对 PI 实际判据序列预测能力的真实测度，非消解失败
- 不可外推至「v2 词表改善无价值」——v2 UNK 55.6%→22.2% 已立竿见影；v3 在此基础上扩展表现力上界（决策树 ≤4→≤6 + 特征 9→12 + 全序列+短语模式），**度量从召回率换代为 NW + NLED 双口径**；本裁决 FAIL 系构造面已尽 + 信号已暴露的复合定性，非任何一阶段产物失败
- 不可外推至 V1–V3 资产（18 frozen / 9 网格）——本件与既有件**完全无关**，V1–V3 只读不动底线严守
- 不可外推至任务 B 终稿路径（PI 1 周判死线后的下一阶段）——本裁决仅在当前构造域内有效

### §3.3 形式效力声明

1. 本件 verdict = **FAIL (formal v3, 正式判定)**（K-V3-A/A'/B/C/D 五段 hit, K-V3-E 不触发；any_hit_strict_5lines=true）
2. 根因 = **复合定性**：K-V3-A 复合 + K-V3-A' 复合 + K-V3-B β 主导 + K-V3-C 复合 + K-V3-D β 主导 + K-V3-E 不适用（详见 §2.7）
3. FAIL ≠ 全部真证伪：3 复合 + 2 β 主导 + 1 sentinel PASS = **本裁决不宣告命题层被证伪**
4. 复合定性 ≠ 构造无责：构造/边界存疑面证据（n_held=23 小样本 + 度量形式边界 + actual=[] 语义层混叠 + 素材扩产物 + 词表边界）**显式登记**，不掩盖
5. 后续触发条件（任一改变即可能翻案，沿 verdict_v2 §3.3 体例）：
   - 度量换代（NW-sim + NLED-sim → LCS / F1 / 嵌入判读 / NW 邻近类矩阵启用）
   - 规则集上界再扩展（决策树 ≤6→≤8 + 特征 ≥12→≥15 + 短语模式 → 嵌入判读）
   - D1 缺位 8 件补采 + 批判反思词表扩词 + D4/D5 跨日续采使跨日 ≥5 天
   - held-out 样本扩 23 → 50+（沿 v2 verdict §3.3 触发条件 5）
   - K-V3-A 阈值 0.65 / A' 0.55 / D 0.40 是否需调整（v3 新冻结 vs v2 字面 0.80/0.50 差异显著）

### §3.4 双读法对照并报（不合并、不择优）

**字面依据**：v3 prereg §3.4 + E-27 §13 + result_v3 §alt_reading_corr_excluded 字面「替代读法 (沿 v2 §3.3 字面): 剔 correction 子集; 双口径并报不择优」

| 维度 | 主读法（全 77 substrate, n=23 held-out） | 替代读法（剔 correction, n=18 held-out） | delta（替-主） | 分歧根因 |
|---|---|---|---|---|
| NW-sim mean | **0.4534** | **0.5127** | **+0.0593** | 剔 correction 后 NW-sim 略升 = correction 子集中部分事件 NW-sim 偏低（5 件 correction in held: idx=2, 13, 27, 28, 47 等） |
| NLED-sim mean | **0.2754** | **0.2963** | **+0.0209** | 同上，NLED 略升 |
| div_critical_coverage | **0.4286** | **0.3636** | **-0.0650** | 剔 correction 后 coverage 下降 = correction 子集中批判词命中事件占比相对较高 |
| blind_obey_rate | **0.2222** | **0.2857** | **+0.0635** | 剔 correction 后盲从率上升 = correction 子集中 1 件一致事件（idx=23）剔出后分母变小 |
| perm_p | 0.0160 | (result_v3 未报替代读法 perm_p) | — | 主读法 ≤ 0.05 显著 |
| bootstrap CI | **[0.3217, 0.5870]** | **[0.3722, 0.6611]** | 下界 +0.0505 / 上界 +0.0741 | 剔 correction 后 CI 全段上移 = sim 分布更分散 |

**双读法结论**（一句一次）：
- **NW-sim / NLED-sim / div_critical_coverage / blind_obey_rate / bootstrap CI 5 项均在双读下分化**——主-替 delta 揭示 correction 子集（5 件 held-out, n=23 vs n=18）在主读法中扮演**系统性偏低贡献者**角色（NW/NLED 偏低 → 剔后上升；但 coverage 偏低 → 剔后下降；盲从率偏低 → 剔后上升）；
- **K-V3-C 主-替盲从率同向恶化**（0.2222 → 0.2857, delta +0.0635）是 §2.4 复合定性中"度量假象/词表边界"项的部分证据——**剔 correction 后 v3 仍触发 K-V3-C hit**（与 v2 时 K-V2-b2 主-替完全分歧形成对比）；
- 本裁决**不合并双读法、不择优主读法、如实并报**——按 v3 prereg §3.4 + E-27 §13 字面；任一读法均不构成命题层证伪的充分证据；构造/边界存疑面 + 真证伪信号面**双读下均未排除**

---

## §4 后续路径建议（只建议，不擅派工）

> **声明**：本节为 verdict-keeper 视角的"如果未来要翻案，可走的路径"清单，**不构成派工单**；具体派工与阈值修订须由 PI 拍板。

### §4.1 构造补强方向（v3 消解 A + 消解 B 已落地，下一棒空间）

| 方向 | v3 状态 | 翻案路径 |
|---|---|---|
| **NW 邻近类矩阵启用** | v3 不启用（沿 v3 prereg §10.5 第 1 项处置） | verifier 派工按 6 类邻近关系（CRITERIA ↔ KILL_LINE / CRITERIA ↔ RISK / RISK ↔ TIMING）核验 + PI 拍板启用 |
| **度量再换代（NW + NLED → 嵌入判读 / String Kernels / LCS）** | v3 已用 NW + NLED（短序列归零边界） | (i) LCS 短序列区分力不足已排除（v3 prereg §2.2.3）；(ii) 嵌入判读须本地 embedding 模型（key 永不明文约束下需谨慎）；(iii) NW 邻近类矩阵启用可降低 v2 召回率「∅ 即 0」退化模式——PI 拍板 |
| **决策树深度再上调 + 特征扩** | v3 = ≤6 + 12 特征（v2 = ≤4 + 9 特征） | ≤8 + 15 特征 + 短语模式 → 嵌入判读——须 worker 重训 |
| **D1 缺位 8 件补采** | 维持不补造（PI Q3 拍板） | worker 沿 v2 verdict §1.1 + dataset v1.2 D1 索引补采 → substrate 扩 85 → 93 |
| **D4/D5 续采** | D4 已落盘 5 件（既有 PI 判定材料编码，非实时答题） | worker 续采 D5（24h 内多日多次）使 substrate 扩 85 → 100+ |
| **批判反思词表扩词** | v3 = 36 词（v2 = 35 词，+1 UNKNOWN 兜底） | verifier 派工按 v2 verdict §2.2 字面 8 件无批判词 divergence 事件逐件核验 + 词表扩词 → 临界 K-V3-B 翻案 |
| **held-out 样本扩** | n=23（substrate=77 RUN） | held-out → 50+（扩 substrate 至 150+）——本棒 worker 已老实交代小样本结构性高方差 |

### §4.2 D5 续采后路径（沿 v3 prereg §5 起跑条件字面）

| 续采动作 | 阈值 ID | 现状 | 续采后状态 |
|---|---|---|---|
| D1 推理补填 8 件 | TH-v3-1（N≥50） | N=85 已达标（substrate=77 RUN + 8 D1 missing） | N=93 满采 |
| D5 跨日续采 | TH-v3-3（跨日 ≥3 天） | 跨日 3 天（D1+D2/D3+D4）已达标 | 跨日 4-5 天（扩安全余量） |
| 单日占比重算 | TH-v3-3（单日 ≤60%） | D1 56.5%（已达标） | 须重算（视 D5 量级） |
| 重新训练 + 重跑 + 重裁 | — | — | 由 PI 派 worker → verdict-keeper 重裁（v3.x） |

---

## §5 老实交代段（产物核验 + 0 既有件触动自查）

### §5.1 产物核验

| 件 | 状态 | 备注 |
|---|---|---|
| `results/_v4_pi_cot_v3_verdict_v3.md`（本件） | **诞生即报 SHA-12 + 字节数**（见文末） | 唯一产物 |
| 既有 v3 三件（dataset/ruleset_v3/result_v3） | **未触动**（只读核验，§0 SHA-12 表） | 落盘前后 SHA-12 复验不变 |
| 既有 v2 全链 5 件（prereg/coding_review/ruleset_v2/ruleset_v2_executor/verdict_v2） | **未触动**（只读核验） | 同上 |
| 既有 18 frozen + 9 网格 + 9 v2 addenda + 1 v3 d4 addendum | **未触动**（仅引用 SHA-12 锚点） | 同上 |
| 派生 JSON 不合并 | ✓（本件为 Markdown，非 JSON，不触发合并） | — |
| 阈值未擅调 | ✓（TH-v3-1..20 全沿 v3 prereg §4.3 + §10.1 字面；K-V3-A/A'/B/C/D/E 字面不动） | — |
| key 永不明文 | ✓（本件 0 key / 0 LLM / 0 proxy / 0 gateway） | — |
| V1–V3 资产只读 | ✓（本件路径仅在 `results/_v4_pi_cot_v3_*`） | — |
| kill-line 字面不动禁私设条款 | ✓（K-V3-A/A'/B/C/D/E 字面来自 v3 prereg §4.2） | — |
| 判定布尔显式命名方向 | ✓（hit_direction 字面 + hit=True 即触发；K-V3-E 不触发走 sentinel 字面） | 见 §2 各 kill-line 行 |
| 不覆盖任何既有件 | ✓（新件新名 `_v4_pi_cot_v3_verdict_v3.md`，产物链末件） | — |
| v1 裁决 EB9AD4193CF2 不翻案 | ✓（v1 探索性预跑结论字面沿用） | — |
| v2 裁决 5D79E67A4E9D 不翻案 | ✓（v2 正式判定 FAIL 复合定性字面沿用，与 v3 并列共存） | — |

### §5.2 0 既有件触动自查

- **本件未触动**任何既有件——所有 5 件输入 + 33 件既有资产仅做只读核验（§0 SHA-12 表 + 字面读取）
- **本件未触动**主目录——归档二棒在跑，本件按派工单字面「不动其他件（归档二棒在跑勿碰）」严守
- **本件未触动**V1–V3 资产——仅引用 prereg_v3 / result_v3 / ruleset_v3 / ruleset_v3_executor / dataset_v3 / v2 verdict sha12 链溯源，未读 18 frozen / 9 网格任何一件
- **本件未触动**派生 JSON——本件为 Markdown，无 JSON 派生

### §5.3 0 产物诚实声明

- 本件 1 件 Markdown，无 JSON 派生，无图表，无脚本
- **succeeded ≠ 跑完**：产物落盘并 SHA-12 核验后才可宣告完成——本件核验见文末

### §5.4 不编造声明

- 不编造外部专有名词 / 文献号 / 法条号 / 工具版本：Needleman & Wunsch 1970, J. Mol. Biol. 48(3):443-453 沿 v3 ruleset 字面引用（DOI: 10.1016/0022-2836(70)90057-4）
- 不编造观测数字：NW-sim mean 0.4534 / NLED-sim mean 0.2754 / div_critical_coverage 0.4286 / blind_obey_rate 0.2222 / bootstrap CI [0.3217, 0.5870] / perm_p 0.0160 全部来自 result_v3.json §main_reading 字面
- 不编造双读法数值：替代读法 0.5127 / 0.2963 / 0.3636 / 0.2857 / [0.3722, 0.6611] 全部来自 result_v3.json §alt_reading_corr_excluded 字面
- 不编造根因三分类：K-V3-A 复合 / K-V3-A' 复合 / K-V3-B β 主导 / K-V3-C 复合 / K-V3-D β 主导 / K-V3-E 不适用（sentinel 未触发）均按 E-27 §13 判别要件复核后归类（执行棒 result_v3 自报 5 hit + K-V3-E 不触发，本件按诚实纪律逐行重判为复合定性，未机械判纯 α 或纯 β）
- 不编造 idx=5 / idx=23 盲从事件归类：sim=1.0/1.0 KILL_LINE vs [KILL_LINE] has_critical=FALSE + sim=0.6/0.5 CRITERIA vs [TIMING, CRITERIA] has_critical=FALSE 全部来自 result_v3.json §main_reading.per_event 字面
- 不编造 K-V3-B 8 件无批判词 divergence 事件：idx=12/28/37/39/47/50/72/74 全部来自 result_v3.json per_event 字面（v2 时 idx=5/12/28/37/50/53 字面对照，仅 5 件重叠，3 件 v3 新增 = idx=47/72/74；新增源待 verifier 派工逐件核验，本件不擅归因）
- 不编造 D4 addendum SHA 漂移归因：anchor B18FF4177289 vs actual CBF60A630C9F 来自 result_v3.json §anchor_sha_verification 字面 disclosure；本棒 worker 已老实交代「executor 仍按实测 SHA 锚入 (0 触动既有件)」，本件沿 supersede 案例模式归口

### §5.5 已知边界（沿 v3 prereg §6 + E-27 §13 + PI V4 铁律）

- 0 LLM 采集 / 0 key 相关 / key 永不明文（不落盘不入 prompt 不入 JSON 不入 log，仅 runtime 读）
- 非画像声明（不预测 PI 行为 / 不做个人模型外传）；产物 = 方法规则集供 AI 内化（呼应 GOAL_拓扑智能 55428F6BD848）
- 推理全文（85 events）仅入 `_v4_pi_cot_v3_dataset*.json` + v3 d4 addendum 本地件；本件 verdict 不复述推理全文
- 生效即锁（v3 prereg §6 + §10.1 字面）；本件为产物链末件不重写 §1-§4 任何一行
- **NW 邻近类矩阵 v3 不启用**（沿 v3 prereg §10.5 第 1 项处置）；如未来启用须另立预登记 v3.x
- **K-V3-E 双口径一致线**作为构造面 sentinel 入锁（沿 v3 prereg §10.5 第 3 项处置）；v3 实测不触发 = 消解 B 真正消解

### §5.6 待 PI 复核项（poka-yoke 显式）

1. **§2 复合定性「部分 α 真证伪 + 部分 β 边界存疑」**是否需 PI 字面拍板（沿诚实纪律「不机械二选一」）？——与 v2 §5.6 第 1 项同款
2. **§3.3 后续触发条件 5 项**（度量再换代 / 规则集上界再扩展 / D1 补采 / D4/D5 续采 / held-out 样本扩）哪一项 PI 优先派工？
3. **§2.3 K-V3-B 8 件无批判词 divergence 中 3 件 v3 新增**（idx=47/72/74）是否需 verifier 派工逐件核验源（D4 5 件 or D3 三读扩展 or other）——影响"v2 → v3 divergence 扩 6 → 8 件"的归因？
4. **§4.1 NW 邻近类矩阵启用**是否需 PI 拍板（v3 不启用沿 §10.5 第 1 项；启用可降低短序列归零边界但引入 PI 主观判断色彩）？
5. **K-V3-A / A' / D 阈值数值（0.65 / 0.55 / 0.40）**v3 比 v2 显著下调，是否需 PI 字面复核（v3 prereg §9.5 第 2 项待复核项已 Q1 拍板维持照案；本件 FAIL 立案按字面 0.65/0.55/0.40 触发，但 PI 可在未来翻案时调整）？

---

## §6 字面保留清单（防回溯覆盖）

- `_v4_pi_cot_v3_prereg.md` (B7547329AF2E) §0-§10 字面 —— 全部沿用不动
- `_v4_pi_cot_v3_dataset.json` (5118F5B44F17) 全部字段 —— 存照不覆盖
- `_v4_pi_cot_v3_ruleset_v3.json` (9D77A5E2CBAB) 全部字段 —— 存照不覆盖
- `_v4_pi_cot_v3_ruleset_v3_executor.py` (8A81D90C69BA) 全部代码 —— 存照不覆盖
- `_v4_pi_cot_v3_result_v3.json` (585714F9660C) 全部字段（含 `v1_v2_anchors_preserved` 三件 SHA-12 + `anchor_sha_verification` 18 件 + `touch_policy_summary` 全项 PASS） —— 存照不覆盖
- `_v4_pi_cot_v2_verdict_v2.md` (5D79E67A4E9D) §1-§7 字面 —— 全部沿用不动，本件 v3 与 v2 并列共存
- `_v4_pi_cot_v2_prereg.md` (CC25C5149CE1) §1-§7 字面 —— 全部沿用不动
- `_v4_pi_cot_v2_coding_review_2026_09_26.md` (5FBEC21E0AD2) §2.2 operationalization_v2 字面 —— 全部沿用不动
- `_v4_pi_cot_v2_ruleset_v2.json` (C5B3DD141655) 全部字段 —— 存照不覆盖
- `_v4_pi_cot_v2_ruleset_v2_executor.py` (EB22F13D571C) 全部代码 —— 存照不覆盖
- `_v4_pi_cot_v2_result_v2.json` (F86727C857A8) 全部字段 —— 存照不覆盖
- `_v4_pi_cot_v2_verdict.md` (EB9AD4193CF2) v1 探索性预跑裁因 + §6.2 外推边界 —— 全部沿用不动，本件 v3 与 v1 并列共存
- `_v4_pi_cot_v2_dataset.json` (7B01CD835A41) v1.1 dataset —— 存照不覆盖
- `_v4_pi_cot_v2_collection_log.md` (167AD91F198E) 采集口岸 —— 存照不覆盖
- TH-v3-1..20 + K-V3-A/A'/B/C/D/E + seed=42 + 决策树 ≤6 + 排列 n=1000 + bootstrap n=1000 + NW match=+2/mismatch=-1/gap=-2 + NLED 1 - edit/max —— 全部沿 v3 prereg 字面
- **K-V3-A/A'/D 阈值 0.65/0.55/0.40**与 v2 K-V2-a/c 阈值 0.80/0.50 不沿用数值（沿 v3 prereg §4.1 字面「v3 另立新线不沿用数值亦不继承判定」）

---

## §7 与 v2 verdict 的演进关系

| 维度 | v1（探索性预跑） | v2（正式判定） | **v3（正式判定）** | 演化学意义 |
|---|---|---|---|---|
| 形式效力 | 探索性预跑非正式判定 | 正式判定 | **正式判定** | 满足 v3 prereg §3 铁字面 + §10.1 Q1 拍板生效后升级 |
| 编码表 UNK 率 | 55.6% | 22.2% | (v3 沿 v2 编码表，UNK 率同款 ~22%) | v2 词表改善立竿见影；v3 沿用 |
| 度量口径 | 召回率 \|pred∩actual\|/\|actual\| | 召回率（同款） | **NW-sim + NLED-sim 双口径并报** | **消解 B 落地（v3 prereg §2.2 字面）** |
| 规则集上界 | 决策树 ≤4 + 9 特征 + primary 单元素 | 同款 | **决策树 ≤6 + 12 特征 + 全序列+短语模式** | **消解 A 落地（v3 prereg §1.2 字面）** |
| held-out count | 11 | 22 | **23** | 略增 |
| substrate | N=48（D1 only） | N=72（含 D1 缺位 8 件） | **N=77 RUN + 8 D1 missing = 85** | 跨日 2 天 → 3 天；N 显著扩 |
| NW-sim mean | — | — | **0.4534** | v3 新线（无 v2 对照） |
| NLED-sim mean | — | — | **0.2754** | v3 新线（无 v2 对照） |
| （v2 对照）mean_similarity | 0.1818 | **0.0909**（召回率） | (无可比, 度量已换代) | — |
| div_critical_coverage | 0.6667 | 0.6842 | **0.4286** | v3 ↓↓恶化（素材扩后 divergence 扩 + 词表边界 + actual=[] 混叠） |
| blind_obey_rate | 0.0 | 0.3333 | **0.2222** | v3 ↓↓改善（剔 correction 后 0.2857 仍 FAIL） |
| perm_p | 0.2937 | 0.7912 | **0.0160** | **v3 ↓↓↓显著改善**（规则集确有可学习结构） |
| bootstrap CI | [0.0, 0.4545] | [0.0, 0.2045] | **[0.3217, 0.5870]** | v3 ↑↑改善（消解 A/B 落地后 CI 上界显著抬升） |
| any_hit | True（3 hit） | True（4 hit） | **True（5 hit）** | v3 多 1 hit（K-V3-A' 新立） |
| K-V3-E 双口径一致 | — | — | **不触发（direction_consistent=True）** | v3 新增构造面 sentinel；消解 B 真正消解 |
| 本裁决 root_cause_3class | 3 β（构造失灵族）+ 1 未触发 | 2 β + 2 复合 + 0 纯 α | **3 复合 + 2 β 主导 + 1 sentinel PASS + 0 纯 α** | **复合定性深化** |
| verdict 措辞 | "FAIL 形态保留，根因改判" | "FAIL 立案，复合定性" | **"FAIL 立案，复合定性（消解 A/B 落地后）"** | 复合定性深化 + 构造面已显式外移 |
| 外推边界 | "禁止外推至 PI 思维链不可蒸馏" | 同款禁止 + 复合定性上限钳制 | **同款禁止 + 复合定性上限钳制 + 消解 A/B 已尽声明** | 沿 v1/v2 边界 + v3 消解面声明 |

**演进结论**（一句一次）：v1 → v2 是**从「机械二选一（真/假证伪）」到「复合定性（构造失灵 + 命题信号并存）」的诚实升级**；v2 → v3 是**从「β 构造失灵族部分主导」到「β 边界存疑族主导但消解 A/B 已显式外移」**——v3 构造面（决策树 ≤6 + 12 特征 + 全序列+短语模式 + NW/NLED 双口径并报）已尽，但 FAIL 依旧（K-V3-A/A'/B/C/D 五段全 hit）——**真证伪信号在构造面补正后暴露，复合定性深化**；v1 verdict 探索性预跑性质不变 + v2 verdict 复合定性不变 + 本件 v3 字面冻结，三件并列共存，**不翻案 v1/v2**。

---

## 文末产物核验（诞生即报）

> ⚠ 本字段为避免「回填 SHA → 文件变 → 哈希变 → 再回填」无限循环的稳定方案——SHA-12 前 12 与字节数**不在文件内自记**，统一在最终汇报中核验报出，避免字面不自洽。

- 路径：`results/_v4_pi_cot_v3_verdict_v3.md`
- SHA-12 前 12：**见最终汇报核验值**
- 字节数：**见最终汇报核验值**
- 派生关系：本件由 `_v4_pi_cot_v3_result_v3.json` (585714F9660C) + `_v4_pi_cot_v3_ruleset_v3.json` (9D77A5E2CBAB) + `_v4_pi_cot_v3_ruleset_v3_executor.py` (8A81D90C69BA) + `_v4_pi_cot_v3_dataset.json` (5118F5B44F17) + `_v4_pi_cot_v3_prereg.md` (B7547329AF2E) 5 件字面读取 + `_v4_pi_cot_v2_verdict_v2.md` (5D79E67A4E9D) v2 对照锚参照生成；所有 6 件均只读核验未触动；v1/v2 verdict 字面冻结不覆盖
- 产物链末件（§8 字面），不重写

---

出件｜Mavis 团队 verdict-keeper（`agent-3a4d09ba3c90`）｜2026-09-27