# 论文简报（PAPER BRIEF）：Deposon 凝子散射层（终稿）

日期：2026-08-30
论文全文（公开）：https://arxiv.org/abs/2609.09001

本简报对应终稿《Deposon: An Auditable, Conservation-Guaranteed, Game-Theoretically Tested Scattering Layer over LLM Reasoning Paths》，是面向 GitHub 读者的自包含公开摘要。全部数字可追溯至仓库 `results/` 下冻结 JSON（见末节溯源表）。

## 1. 一句话定位

Deposon 把大语言模型的推理路径选择表述为带守恒账的三通道散射过程，其价值主张不是更高的准确率，而是**可审计的表征与守恒保证**——每一次路径淘汰都留下一本可逐节点复核的能量账。预登记对照实验已亲手封死准确率层的退路：表观准确率优势被判定结构性不可归因，一个仅读标签字符串的平凡规则过滤器即可追平全管线，可审计性由此成为唯一存续的价值主张。

## 2. 静态线核心主张与证据

**方法。** 概念分解图上的节点绑定凝子态，路径穿越时发生透射 T、反射 R、不可逆耗散 A 三通道散射。通道权重为构造性定义（Feshbach 形式仅提供物理动机，不导出公式），任意参数下严格满足 T+R+A=1：每一单位能量要么到达终点、要么被反射、要么凝华入以太，三者必居其一，第三方仅需双精度算术即可逐步重算。

**正向证据。** 两个各 100 题的受控合成基准（seed=42，真实 LLM 后端，零降级）上，unified 变体准确率 100%/100%，同一概念图上的诱饵捕获基线仅 7%/10%。物理审计确认三通道幺正性最大偏差 2.2×10⁻¹⁶（双精度机器精度），三个极限态的耗散率与理论预言一致。

**诚实的划界（同文并列）。** 其一，E9.4 等权对照显示等权拉平后 unified 优势不消失（0.85 vs 0.04），但归因于 BFS 短路径优先与类型标签的免费可得性，而非散射机制本身。其二，E9.5 对照显示一个仅读标签字符串的 6 关键词规则过滤器即打平全管线（GSM8K 0.87 ≥ 0.85；StrategyQA 0.899 = 0.899），且功效口径如实给出：差异 GSM8K −2pp（95% CI [−11.8, +7.8]pp）、StrategyQA 0pp（95% CI [−8.8, +8.8]pp），均为**非配对 Newcombe 混合区间**（保守口径；配对不一致对仅 0/2 与 0/0，配对区间退化；计算工件 `deposon_v22_e95ci.json`），可检测差异阈值约 ±10pp，更小增量不可排除。主张因此收窄为**「差异价值仅在机器可验证性」**，由 E9.4 归因机制而非该检验的强形式支撑。其三，E9.6 融合稀释排除性结论：场臂与语义先验的凸组合在全部已测 λ 设置上不超过任一单臂（physics 0.484→0.452），λ=2 的表观增益为反场伪影；若存在融合增益，只能来自非线性机制。**耗散通道零收益声明**：在全部已测任务上开启不可逆耗散从未优于不开启，仅有理论动机。

## 3. 博弈论线核心主张与证据（三层级强度）

反向动力学在受控概念图上被建模为势博弈：留一预测边为玩家、场得分为效用、物理能量负值 Φ=−E 为势候选。全部判定为预登记后的机械规则求值，强度分三档，不混档：

**closed (pre-registered)（判定规则先于运行冻结并机械求值至闭合）。**
- GT-5b 势轨迹单调性：22/22 图 mean-field Φ 轨迹单调不减（预登记线 ≥80%）——每步演化可审计为势上升，审计标量实证成立。
- GT-6 非势残差完备性：残余中位数 1.594×10⁻²⁹，低于 0.10 预登记线；3 张循环结构图例外（0.12–0.15）如实披露。
- 守恒账本身：T+R+A=1 由构造成立（机器精度 2.2×10⁻¹⁶），审计链在构造处终止。

**一致性证据（方向一致，强判据未达成，有口径限定）。**
- GT-4 经验协调率 ECR：全部 17 张有限值图中位 ECR=1.333（≈4/3，但不与任何经典 worst-case 均衡效率界数值并置——分布级操作化度量，非同一度量），高于 1.2 预登记线；覆盖 20/22 图（2 张族 L 图冻结运行未评测，如实披露）；ECR<1 案例并列披露（族 L 0.5/0.75、S2_n45=0.5），与「场只在结构域创造协调价值」的分工边界自洽。
- GT-3b 跨厂商复核：三个模型族在先验优势上 0 败绩、Kendall W=1.0；残余局限为三族均为中文优化大模型。
- GT-8b 真实语义轴语料外复现：两个新域均过预登记阈值；仅 2 张新图，方向性证据。

**动力学等价三层级判死（终稿最清晰的限制结论）。** 「确定性平均场反向 = 无噪声最优反应动力学」的全部三个形式化层级 P1a/P1b/T-P1c 在判死协议下被证伪：协议为 systematically sampled 61 graph families（n≤8 小图，链/星/树/随机 DAG/含环五族）× exhaustive-state 6760 判死态（338 个单节点全候选掩码任务 × 20 步平均场，seed=210021）。P1a 呈 O(1) 偏差 0.8569；P1b min cos=−1.0（过冲机制在案）；T-P1c 双重判死——τ∈[0,4] 的 81 档全局网格处处失败（最优全局 τ 下 min cos=−1.0），逐状态自选 τ* 下 min cos 仍为 −1.0、τ* 中位数为 0（85.98% 态 τ*=0），熵正则项无修复力。P2 势完备性降级为**近似势博弈**：无环支撑图残差 ≤5.9×10⁻¹⁶（数值零），含环支撑图残差中位 0.669，r>0.30 比例 0.924 越过预登记 1/3 降级线。动力学层仅一致性级证据存续。

**仅有动机（方向性，不作主张）。** 耗散通道的不可逆性收益（全部已测任务零准确率收益）；硬件同构（散射公式与 ring/MZI/PCM 器件在公式层等价，非流片、非 SPICE 级仿真）。

## 4. 工程质量与可复现性

- **测试**：`pytest tests/ -q` 398 passed 全绿；2026-08-30 真实重跑审计 PASS（verdict 脚本重跑与冻结 JSON 逐位一致，审计记录见 `AUDIT_2026-08-30.json`）。
- **预登记时间锚（SHA-256 前 12 位）**：判定纯函数与 SPEC 先于任何运行冻结——`docs/GT_FORMALIZATION_v1.md` = aeefb8ef6972；`run_v21_gtformal.py` = 9bbe43f41fa8；`run_v22_p1c.py` = 6e9673205dc0。任何人可对照锚点核验冻结版本并机械重跑全部判定。
- **内容寻址缓存**：全部 LLM 调用按 prompt_sha256 落盘、attempts 全记录；最终评测运行 1678 次缓存命中、0 未命中、0 规则降级、0 API 错误，结果可确定性复现。
- **版本化 verifier**：`verifier/v1` 至 `v34` 逐版递增，冻结文件走 erratum 不覆写。
- **安全审计**（docs/SECURITY_AUDIT_v2.md）：密钥泄露 0 发现（所有 key 仅存在于运行时环境变量）。
- **数据健康审计**（docs/DATASET_HEALTH_v2.md）：results/ 与 corpus/ 主要数据集经 12 维质检，等级 A/A+，0 完全重复行。

## 5. 边界与阴性结果

项目对阴性结果按「不美化、不回溯改写」归档，判死结论与闭合结论等权重：

- **静态线**：GSM8K 上 CoT 显著更优（97.0% vs 85.0%，McNemar p=4.9×10⁻⁴）；规则过滤器打平散射管线且 ±10pp 以下增量不可排除（E9.5 功效口径）；等权对照下优势不可归因于散射机制（E9.4）；凸组合融合只稀释（E9.6）；耗散通道零收益。
- **博弈论线**：动力学等价三层级 P1a/P1b/T-P1c 全部判死；P2 降级为近似势博弈（含环中位残差 0.669）；H-A1 头条主张（field_mean > random）被预登记斩杀线判死（符号检验 16+/4−/2 平，4 张反转图触发析取斩杀规则）；GT-7 温度前沿判 mixed，「双赢前沿」被否，审计承诺只覆盖势这一本账；GT-2B 判 inconclusive（统计功效不足）；GT-2 判 no_separation。
- **划界规律限定**：「高枢纽图用结构信号、真实语义图用语义先验」的分工规律以观察性规律提出——探索性回归 n=20 且存在特征-设计循环性，hub 轴与 real_semantics 轴复现样本量小；不外推至族 L 之外任务或更大规模图。

## 6. 全文获取

论文终稿已公开发布于 arXiv：**https://arxiv.org/abs/2609.09001**。代码、冻结 JSON、判定纯函数与测试套件随仓库发布；冻结版本可对照 §4 的 SHA-256 锚核验，全部判定可机械重跑。

## 7. 数字溯源表

关键数字 → `results/` 字段路径（均为冻结 JSON）：

| 数字 | 出处 |
|---|---|
| T+R+A=1 最大偏差 2.2×10⁻¹⁶ | `deposon_v19_benchmark_fixes.json` → `physics_audit.t_plus_r_plus_a_max_deviation` |
| 合成基准 100%/100% vs 7%/10%（seed=42） | `deposon_benchmark_v1_3_simple.json` / `..._traps.json` → `variant_results` |
| GSM8K：CoT 97.0%、unified 85.0%、p=4.9×10⁻⁴ | `deposon_benchmark_v1_4_gsm8k.json` → `cot_baseline_accuracy`、`unified_accuracy`、`mcnemar_unified_vs_cot.p_value` |
| StrategyQA：CoT 92.9%、unified 89.9%、p=0.549 | `deposon_benchmark_v1_4_strategyqa.json` → `cot_baseline_accuracy`、`unified_accuracy`、`mcnemar_unified_vs_cot.p_value` |
| E9.4 等权对照 0.85 vs 0.04（p=1.7×10⁻²³） | `deposon_v19_benchmark_fixes.json` → `experiments.E9.4_equal_weight_decoy_control` |
| E9.5 规则基线 0.87/0.899（b=0,c=2, p=0.5 / p=1.0） | 同上 → `experiments.E9.5_rule_baseline.benchmarks` |
| E9.5 差异 95% CI：GSM8K [−11.8,+7.8]pp / StrategyQA [−8.8,+8.8]pp（非配对 Newcombe） | `deposon_v22_e95ci.json` → `gsm8k`/`strategyqa` |
| E9.6 融合稀释 physics 0.484→0.452 | `deposon_v20_crossval.json` → `hybrid_lambda_convex=0.5` |
| GT-5b 22/22 单调 | `deposon_v20_gt5b.json` → `per_graph_summary.*.meanfield_monotone_rate=1.0` |
| GT-6 残余中位 1.594×10⁻²⁹ | `deposon_v20_gt6.json` → `verdict.median_residual_ratio` |
| ECR 中位 1.333（17 图）/ 1.5（族 S 13 图）/ 族 L 0.5、0.75；覆盖 20/22 图 | `deposon_v20_gt.json` → `GT4_price_of_anarchy.verdict`（字段名为冻结惯例不改名）、`poa_per_graph_finite` |
| GT-7 mixed | `deposon_v20_gt7.json` → `verdict`、`per_graph` |
| GT-8b supports（0.7805/0.6429） | `deposon_v20_gt8b.json` → `gt8b_verdict`、`per_domain.*.named_summary` |
| H-A1 判死（16+/4−/2 平，p=0.0118） | `deposon_v20_corpus_eval.json` → `verdicts.kill_lines.H_A_dead`、`verdicts.H_A1_field_mean_gt_random.sign_test` |
| GT_FORMAL：P1a 偏差 0.8569；P1b min cos=−1.0；P2 含环中位 0.669、无环 ≤5.9×10⁻¹⁶；61 图/338 任务/6760 态 | `deposon_v21_gtformal.json`（seed=210021）→ `verdict.P1a_deviation`、`verdict.T_P1b`、`verdict.T_P2`、`n_graphs/n_tasks/n_states` |
| T-P1c 判死：τ∈[0,4] 81 档 min cos=−1.0，逐状态 τ* 中位 0（frac_at_tau0=0.8598） | `deposon_v22_p1c.json`（seed=210021）→ `verdict`、`descriptive.tau_star_per_state`、`tau_grid` |

---

*本简报为公开版本；与 arXiv 终稿（2609.09001）所载结论与数字一致，可独立引用。*
