# 论文简报（PAPER BRIEF）：Deposon 凝子散射层 1.X 与 2.X

日期：2026-08-30

本简报覆盖 Deposon 项目两条论文线：1.X《Deposon：面向可审计大语言模型推理路径选择的物理约束散射层》（v1.9 冻结稿）与 2.X《可审计优势的博弈论实证》（v2.X 稿）。论文全文未公开推送，本简报为自包含的公开版本，全部数字可追溯至仓库 `results/` 下冻结 JSON（见末节溯源表）。

## 1. 项目定位与两线关系

一句话定位：Deposon 把大语言模型的推理路径选择表述为带守恒账的三通道散射过程，其价值主张不是更高的准确率，而是**可审计的表征与守恒保证**——每一次路径淘汰都留下一本可逐节点复核的能量账。

两线构成「出题 → 定命题 → 给实证」的链条。1.X 建立散射层框架与基准纪律，并在整改中亲手封死了准确率层的退路：基准效应量被证明结构性不可归因，一个平凡规则过滤器即可追平全管线。可审计性由此成为唯一存续的价值主张。2.X 承接该命题做动力学层实证：守恒账此前只经静态核验，2.X 把反向演化建模为图上势博弈，回答「整条动力学轨迹是否也有一只可对标的审计标量、它把审计定量化到什么程度、审计的边界在哪里」。

## 2. 1.X 核心主张与证据

**方法。** 概念分解图上的节点绑定凝子态，路径穿越时发生透射 T、反射 R、不可逆耗散 A 三通道散射。通道权重为构造性定义（Feshbach 形式仅提供物理动机，不导出公式），任意参数下严格满足 T+R+A=1。逐路径能量守恒有证明：每一单位能量要么到达终点、要么被反射、要么凝华入以太，三者必居其一。

**正向证据。** 两个各 100 题的受控合成基准（seed=42，真实 LLM 后端，零降级）上，unified 变体准确率 100%/100%，同一概念图上的贪心基线仅 7%/10%。物理审计确认三通道幺正性最大偏差 2.2×10⁻¹⁶（双精度机器精度），三个极限态的耗散率（0% / 86.92% / 8.63%）与理论预言一致。

**诚实的划界（1.X 自行完成）。** 三处降级与主张同文并列：其一，7%/10% 的基线是**诱饵捕获基线**——建图时诱饵边被有意赋权 0.9 高于正确边 0.6，效应量只度量同图路径筛选增量，不是对 LLM 本体的超越。其二，真实基准上约束层与 CoT 无净优势：GSM8K 子集（n=100）CoT 97.0%、unified 85.0%（McNemar p=4.9×10⁻⁴，CoT 显著更优，如实报告；折叠器修复口径 94.0%，p=0.25 无显著差异）；StrategyQA（n=99）89.9% vs 92.9%（p=0.549，无显著差异）。其三，E9.5 对照显示一个仅读标签字符串的 6 关键词规则过滤器即打平全管线（GSM8K 0.87 ≥ 0.85；StrategyQA 0.899 = 0.899），E9.4 等权对照显示等权拉平后 unified 优势不消失（0.85 vs 0.04），但归因于 BFS 短路径优先与类型标签的免费可得性，而非散射机制本身。**耗散通道零收益声明**：在全部已测任务上开启不可逆耗散从未优于不开启，其收益主张仅有理论动机，留待迭代重搜场景验证。价值命题因此定位于可审计表征与守恒保证。

## 3. 2.X 核心主张与证据（机制层三档强度）

2.X 在 22 张受控概念图上把反向动力学建模为势博弈：留一预测边为玩家、场得分为效用、物理能量负值 Φ=−E 为势候选。全部判定为预登记后的机械规则求值，论证强度分三档，不混档：

**已证（构造保证或预登记判定闭合）。**
- GT-5b 势轨迹单调性：22/22 图 mean-field Φ 轨迹单调不减（收窄主张，预登记线 ≥80%，斩杀线 0 触发）——每步演化可审计为势下降，审计标量实证成立。
- GT-6 非势残差完备性：边效用向量向梯度空间投影，残余中位数 1.594×10⁻²⁹，低于 0.10 预登记线；3 张循环结构图例外（0.12–0.15）如实披露，其上势解释为近似。
- 守恒账本身：T+R+A=1 由构造成立（机器精度 2.2×10⁻¹⁶），审计链在构造处终止。

**一致性证据（与势博弈解读一致，有口径限定）。**
- GT-4 分布级 PoA：全 17 张有限值图中位 PoA=1.333，高于 1.2 预登记线（族 S 子集 13 图中位 1.5 并列）；族 L 2 图 PoA<1（0.5、0.75）并列披露，与「场只在结构域创造协调价值」的分工叙事自洽。该操作化度量与经典 worst-case PoA 不是同一度量。
- GT-3b 跨厂商复核：三个模型族（Kimi 系、豆包、DeepSeek）在先验优势上 0 败绩、Kendall W=1.0；同源污染假说被实质性削弱，残余局限为三族均为中文优化大模型。
- GT-8b 真实语义轴语料外复现：两个新域均过预登记阈值（chinese_dynasties 先验 0.7805 vs 场 0.0732；chemical_elements 0.6429 vs 0.1429），判 supports_H_GT8B；初判 inconclusive 经修正案 B2/B3 补数转正，取数史归档不回溯改写；仅 2 张新图，方向性证据。

**仅有动机（方向性，不作主张）。**
- 耗散通道的不可逆性收益：全部已测任务零准确率收益，仅有理论动机。
- 硬件同构：散射公式与 ring/MZI/PCM 器件的映射在公式层等价（守恒偏差浮点零），18/22 图在约 2.9dB/跳损耗预算下可探测；非流片、非 SPICE 级仿真，参数为文献典型量级。

## 4. 工程质量与可复现性

- **测试**：重构后 `pytest tests/ -q` 351 passed 全绿（2.X 成稿批次为 255 passed，REFACTOR v2 期间由 274 增至 351）。
- **内容寻址缓存**：全部 LLM 调用按 prompt_sha256 落盘、attempts 全记录；1.X 最终评测运行 1678 次缓存命中、0 未命中、0 规则降级、0 API 错误，结果可确定性复现。
- **版本化 verifier**：`verifier/v1` 至 `v34` 逐版递增，冻结文件走 erratum 不覆写；kill_lines 类字段的强制对照已列入 verifier v21。
- **五候选重构（REFACTOR v2）**：退火核心统一（5 份复制循环 → 单入口）、实验协议库、LLM fetch 管道统一、agents 双层级合并、GT 族共享底座，均为行为保持性重构；重构前后 48/48 个冻结哈希逐位一致。
- **安全审计**（docs/SECURITY_AUDIT_v2.md）：密钥泄露 0 发现（所有 key 仅存在于运行时环境变量），9 项 medium 全部为误报/良性，依赖扫描无已知漏洞；唯一实质加固项（两个 fetch 脚本错误路径未走 `_sanitize`）已记录。
- **数据健康审计**（docs/DATASET_HEALTH_v2.md）：results/ 与 corpus/ 主要数据集经 12 维质检，等级 A/A+，0 完全重复行；报告的缺失值均为结构性缺失（族 S 图本无 LLM 先验），非数据损坏。

## 5. 边界与阴性结果

项目对阴性结果按「不美化、不回溯改写」归档，主要项如下：

- **1.X**：GSM8K 上 CoT 显著更优（p=4.9×10⁻⁴）；规则过滤器打平散射管线（E9.5）；等权对照下优势不可归因于散射机制（E9.4）；耗散通道零收益；「长链上物理层增量更大」的预注册预言被证伪（Δ +0.90/+0.92/+0.67 不随链长增长）；阈值与绑定参数无 held-out 验证；评测确定性来自缓存冻结，多次独立重采样稳健性未测。
- **2.X**：H-A1 头条主张（field_mean > random）被预登记斩杀线判死——符号检验 16+/4−/2 平、p=0.0118 虽显著，但反转图达 4 张触发析取斩杀规则；GT-7 温度前沿判 mixed：升温提高全局势探索收益但不兼提命中率（S6 高温档 Φ 升而命中率 0.4→0.08），「双赢前沿」被否，审计承诺只覆盖势这一本账；GT-2B 多陷阱强度实验判 inconclusive（n=40/格统计功效不足，且判据被选项构成污染）；GT-2 判 no_separation（攻击强度未达决定性）；GT-5 终点反转 inconclusive 在案。
- **划界规律限定**：「高枢纽图用结构信号、真实语义图用语义先验」的分工规律以观察性规律（v0）提出——探索性回归 n=20 且存在特征-设计循环性，hub 轴复现仅 2 对配对（鉴别的是结构信号整体而非场独有优势），real_semantics 轴复现仅 2 图方向性证据；不外推至族 L 之外任务或更大规模图。

## 6. 全文获取说明

两篇论文的完整版未公开推送至本仓库。获取论文全文请联系项目维护者（见仓库内说明）。本简报所载全部结论与数字与冻结稿一致，可独立引用。

## 7. 数字溯源表

关键数字 → `results/` 字段路径（均为冻结 JSON）：

| 数字 | 出处 |
|---|---|
| T+R+A=1 最大偏差 2.2×10⁻¹⁶ | `deposon_benchmark_v1_3_simple.json` / `..._traps.json` → `physics_audit.t_plus_r_plus_a_max_deviation`（GSM8K 同字段见 `deposon_benchmark_v1_4_gsm8k.json`） |
| 合成基准 100% vs 7%/10% | 同上两文件 → `unified_accuracy` / `baseline_accuracy` |
| 三极限态耗散率 0%/86.92%/8.63% | `deposon_benchmark_v1_3_traps.json` → `variant_results` 各臂耗散统计（全场口径见论文表 11） |
| GSM8K：CoT 97.0%、unified 85.0%、p=4.9×10⁻⁴ | `deposon_benchmark_v1_4_gsm8k.json` → `cot_baseline_accuracy`、`unified_accuracy`、`mcnemar_unified_vs_cot.p_value` |
| 折叠器修复口径 94.0%（p=0.25） | 同上 → `sensitivity_analysis.accuracy_sensitivity.unified`、`mcnemar_sensitivity_unified_vs_cot.p_value` |
| SC@5 96.0%（vs unified p=0.0034） | `deposon_benchmark_v1_4_sc5.json` → `sc5_accuracy`、`mcnemar_sc5_vs_unified.p_value` |
| StrategyQA：CoT 92.9%、unified 89.9%、p=0.549 | `deposon_benchmark_v1_4_strategyqa.json` → `cot_baseline_accuracy`、`unified_accuracy`、`mcnemar_unified_vs_cot.p_value` |
| E9.4 等权对照 0.85 vs 0.04（p=1.7×10⁻²³） | `deposon_v19_benchmark_fixes.json` → `experiments.E9.4_equal_weight_decoy_control.benchmarks.gsm8k.summary`、`mcnemar_unified_vs_no_deposon.p_value` |
| E9.5 规则基线 0.87 / 0.899 | 同上 → `experiments.E9.5_rule_baseline.benchmarks.{gsm8k,strategyqa}.rule_baseline.accuracy` |
| GT-5b 22/22 单调 | `deposon_v20_gt5b.json` → `per_graph_summary.*.meanfield_monotone_rate=1.0` |
| GT-6 残余中位 1.594×10⁻²⁹ | `deposon_v20_gt6.json` → `verdict.median_residual_ratio` |
| PoA 中位 1.333（17 图）/ 1.5（族 S 13 图）/ 族 L 0.5、0.75 | `deposon_v20_gt.json` → `GT4_price_of_anarchy.verdict.median_poa`、`poa_per_graph_finite` |
| GT-7 mixed | `deposon_v20_gt7.json` → `verdict`、`per_graph`（逐图温度档明细） |
| GT-8b supports_H_GT8B（0.7805/0.6429，diff +0.7073/+0.5000） | `deposon_v20_gt8b.json` → `gt8b_verdict.verdict`、`per_domain.*.named_summary`、`prior_named_minus_field_named` |
| H-A1 判死（16+/4−/2 平，p=0.0118） | `deposon_v20_corpus_eval.json` → `verdicts.kill_lines.H_A_dead.triggered=true`、`verdicts.H_A1_field_mean_gt_random.sign_test.p_exact` |
| 全链路审计 1740 任务 0 违规 | `deposon_v20_vector_audit.json` → `n_tasks=1740`、`violation_counts.*=0`、`all_pass=true` |

---

*本简报为公开版本；论文全文与预登记文件、判定脚本、修订编年的完整归档见仓库内说明，获取全文请联系项目维护者。*
