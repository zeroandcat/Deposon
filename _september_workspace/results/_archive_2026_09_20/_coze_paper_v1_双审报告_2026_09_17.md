# paper V1 双审报告（异源 4 模型交叉）

- 待审稿：`D:\私人资料\deposon-repo\results\_coze_paper_v1_draft_2026_09_17.md`
- 稿 SHA-12：`c08e7abf5ee3`
- 审稿配置：内容审 A × 2（GLM-5.1 / Kimi-K3）+ 技术审 B × 2（DeepSeek-v4-pro / Grok-4.6）
- 异源声明：4 个审稿模型均非起草方，且非 OpenAI/Anthropic/Google 系

---

## content_A1_glm51（or:z-ai/glm-5.1 → served: z-ai/glm-5.1）

- 状态：OK　报告 SHA-12：`5e8f9dd18590`

## 总体判断
**MAJOR_REVISION**
理由：核心科学发现（标度塌缩部分拒绝、三态分离框架）扎实且负面结果披露诚实，但稿件存在严重的行文自相矛盾（P2 判定逻辑与“必改”框未合并）、大量未消化的内部黑话（判死/挂点/轧平）、以及将工程管理指令混入学术限制章节等结构性问题，当前形态不具备学术可读性。

## 亮点
1. 预注册证伪纪律执行严格，P1/P3 FAIL 与 bug 披露不回溯修改，符合开放科学精神。
2. 三态分离框架逻辑精巧，成功分离了“标度不成立”与“跨实现稳健”的悖论，有方法论贡献。
3. 退化预检族在 0 LLM 层拦截 3 项真 bug，证明不变性预检的工程有效性。
4. 限制披露极度诚实（n=3 统计力不足、FPR 4.44%、proxy 不稳），无掩盖美化。
5. §4.1 对代数恒等式伪影的剖析清晰，准确定位了单调变换导致 Spearman≡1 的数学根源。

## 必改项

| 编号 | 严重度 | 位置 | 问题 | 具体修改建议 |
|---|---|---|---|---|
| M1 | 阻断 | §4.4 / §4.5 / 摘要 | **P2 判定自相矛盾**：§4.4“必改”框称 P2 须降格为“3/5 backbone overlap（1 OR×OR 失败）”，但 §4.5 表格与摘要仍写“6 个独立 backbone 两两 β CI 全重叠 PASS”，未将 OR embedding 失败纳入 P2 总体判定。 | 删除§4.4必改框，将内容直接并入正文。P2 总判定修改为：“**P2 条件性 PASS**——LLM backbone 6/6 全重叠，但 OR embedding 组 1/6 GRAY（symbol-split），跨实现稳健性在 LLM 架构内成立，跨模态架构存在边界。”摘要同步修改。 |
| M2 | 阻断 | §3.1 / §4.4 / §5.1 | **“必改/数字修正”框与正文未合并**：稿件中留有3处“数字修正（必改）”或“数字降格”编辑框（87.0%→85.0%，P2降格，16→17项），这是草稿残留，不是正式论文写法。 | 删除所有“必改/修正”编辑框，将修正后的数值与逻辑直接写为正文唯一表述，原错误数值彻底删去。 |
| M3 | 阻断 | 全文 | **黑话/高深隐喻泛滥，严重损害学术可读性**：“判死”（证伪/拒绝）、“挂点”（理论接口/验证点）、“轧平”（残差为零/恒等式成立）、“挂死也是交付”（负面结果也是有效产出）、“账本”（守恒量系统）。 | 全局替换：判死→证伪/拒绝(falsification/rejection)；挂点→验证接口(validation interface)；轧平→恒等式守恒/残差为零；账本→三通道守恒系统。标题改为《deposon V3X 一周证伪实验：……主张的部分拒绝》。 |
| M4 | 阻断 | §5.1 / §5.2 / 附录 | **拼写错误**：“Adendum”贯穿全文，正确拼写为“Addendum”。 | 全局替换 Adendum → Addendum。 |
| M5 | 重要 | §3.1 | **“0.867 均衡带”过度解读**：两个模型在 30 题中答对 26 题，仅是精度重合，称其为“均衡带”暗示了动力系统吸引子，缺乏理论支撑。 | 改为“双模型精确重合点（26/30）”，删除“均衡带”表述，除非能给出动力学势函数的形式证明。 |
| M6 | 重要 | §6.7 | **学术限制章节混入工程推送指令**：“push README 必列 4 件”是代码仓库管理指令，不是学术限制。 | 将§6.7整段移至附录，或在正文中仅作一句声明：“相关工程缺陷已在仓库 README 中显式声明（见附录X）”，§6仅保留科学限制。 |
| M7 | 重要 | §4.1 | 代码段属于实现细节，与内容审稿冲突，且数学解释不够抽象。 | 删去 Python 代码，改用数学语言表述：“对全正向量 $\vec{x}$，作保序变换 $f(x)=x^\nu$ 与 $g(x)=\eta x$，因 $f, g$ 严格单调递增，$\text{Spearman}(f(\vec{x}), g(\vec{x})) \equiv 1$，此为代数恒等式伪影。” |

## 建议改项

| 编号 | 严重度 | 位置 | 问题 | 具体修改建议 |
|---|---|---|---|---|
| S1 | 建议 | §5.5 | 挂点回扣表中大量使用内部代号（如“KT-C1 幂律死的是自己主张”），合作方极难读懂。 | 将内部代号翻译为学术陈述，如：“KT-C1 幂律证伪（R²=0.0007）与本实验 P1 标度证伪（R²=0.7447）结论一致”。 |
| S2 | 建议 | §1 | 7铁律与0 LLM起草约束属于过程合规声明，占据引言大量篇幅，打断科学叙事。 | 将7铁律与0 LLM声明移至§2（方法/设计）或附录，引言仅保留“实验遵循预注册与零干预原则（详见§2）”。 |
| S3 | 建议 | §4.3 | P1 拟合仅用 L=30/45/100 三点，L=60 被标为“n/a (仅 reference)”，未解释为何不纳入拟合。 | 补充说明 L=60 为何不纳入 P1 拟合（如：非同分布数据/跨模型聚合不可比），否则读者会质疑选择性采数据。 |
| S4 | 建议 | 摘要 | 摘要罗列了 17 项 Addendum 的具体分布（11+2+1+2+1），过于琐碎，冲淡了核心发现。 | 摘要仅保留核心三态分离结论与关键限制，Addendum 分布移至正文。 |
| S5 | 建议 | §4.4 | β 被定义为“cell-level 代理斜率”，但未给出具体回归公式，读者无法判断其与 size scaling exponent 的数学关系。 | 在§4.4补充公式：$\beta_i = \text{slope}(\text{score}_j, \text{index}_j)$ for backbone $i$，并说明其作为代理指标的合理性。 |

## 需要补充的文献方向

1. **有限尺寸标度（FSS）理论**：补在 §4.1 / §5.3，支撑 Adendum P 中“data collapse 的前件是存在幂律标度”这一强理论主张。需引用统计物理中 FSS 的经典文献（如 Fisher, 1970; Cardy, 1996），证明无幂律则塌缩无意义的数学前提。
2. **LLM Scaling Laws 及其失效边界**：补在 §1 / §4.3，将 P1 FAIL (R²=0.7447) 置于 Kaplan et al. (2020) 与 Hoffmann et al. (2022) 的 LLM scaling law 语境下，说明本实验观测到的“尺寸标度失效”是挑战还是特定数据集上的特例。
3. **预注册证伪在 AI/ML 中的实践**：补在 §1 / §2，为“一周判死/不回溯修改”的方法论寻找先例，如 Pilgrim et al. 的 null results in ML 或心理学预注册运动，增强方法论的学术正当性。
4. **Spearman 秩相关的伪影与误用**：补在 §4.1，支撑代数恒等式伪影的发现并非孤例，引用指出单调变换导致伪相关的统计学文献。

## 其他意见

1. **“部分拒绝”的措辞精准度**：论文标题与结论用“部分拒绝”描述 data collapse 假设，逻辑上成立（P1/P3 拒绝，P2 接受）。但需警惕语义模糊：读者可能误解为“数据部分塌缩”。建议在 §7 结论处加一句明确定义：“本文的‘部分拒绝’特指：标度律与塌缩假设被拒绝，但跨实现稳健性假设被接受，而非指标在阈值边缘部分通过。”
2. **GLM 盲测 FPR 的处置逻辑**：§6 限制(2)中，机器判定 OVERALL FAIL，paper 处置 GRAY，理由是“样本量与盲测设计限制”。这属于合理的降级，但必须在 §5.3 Adendum O 处补充具体的统计功效分析或设计缺陷说明，否则“双口径”容易被质疑为“找借口”。需给出：样本量 n=45 下，1% 阈值对应的置信区间宽度，证明当前样本不足以精确区分 1% 和 4.44%。
3. **时间戳与版本依赖**：文中大量出现具体日期（如 2026-09-17）和内部文件名（如 `_v3x_d0_5_experiment_invitation...`），对学术论文而言噪音过大。建议将内部文件名全部移至数据可用性声明，正文只提逻辑阶段（如 D0.5 阶段）。

---

## content_A2_kimik3（or:moonshotai/kimi-k3 → served: moonshotai/kimi-k3）

- 状态：OK　报告 SHA-12：`64fccc506274`

Let me carefully review this manuscript as an academic content reviewer. The task is to review a Chinese research paper draft about a "one-week kill experiment" (判死实验) for the deposon V3X framework, testing data collapse claims for LLMs.

Let me go through the manuscript systematically and check for:

1. Argument clarity and logical chain
2. Claim-evidence matching
3. Structural completeness
4. Honesty of limitation disclosure
5. Validity of the "挂点" (hook point) callbacks
6. Academic expression

Let me identify issues:

**Issue 1: P1 尺寸标度测试的致命设计缺陷**

In §4.3, the Phase 1 test uses Mistral Large 2512 at L ∈ {30, 45, 60, 100}. But look at the table:
- L=30: accuracy 0.8000 (24/30)
- L=45: accuracy 0.5111 (23/45)
- L=60: 0.7111 (9 model aggregate, "仅 reference")
- L=100: 0.4600 (46/100)

Wait, there's a serious problem here. The L=45 and L=100 cells include NEW StrategyQA cells (15 GSM8K + 15 baseline SQA + 15 new SQA for L=45; 15 GSM8K + 15 baseline SQA + 70 new SQA for L=100). The manuscript itself admits in §4.3 point (b): "StrategyQA 新增 cells（15 + 70）难度分布偏移导致 accuracy 单调下降".

This is a confound: the "size scaling" test is not testing size scaling at all — it's testing accuracy on different question sets of varying difficulty. The accuracy drop from 0.80 to 0.46 is likely due to harder questions, not size effects. This means P1 FAIL conclusion is confounded. The manuscript does disclose this as uncertainty (b), but the main conclusion "尺寸标度不成立" (size scaling does not hold) is stated as a kill-level (判死级) conclusion in the abstract and §7. This is a claim-evidence mismatch: the evidence doesn't support a kill-level rejection of size scaling because the experimental design confounds size with question difficulty.

Actually, more fundamentally: what is "size scaling" here? In standard FSS (finite-size scaling), you vary the system size L and measure an observable O. Here L is the number of test questions (cells), and O is... accuracy? That's not a physical system size at all. Testing whether accuracy scales as a power law of the number of test questions is conceptually confused — accuracy on a fixed distribution of questions should be roughly independent of the number of questions (it's an average). The only reason accuracy changes with L here is because the question composition changes. So the entire P1 test is testing a null hypothesis that would only hold by coincidence of question sampling. This is a deep conceptual problem.

Actually wait — let me re-read. The observable O: "log(O) = 1.0731 − 0.4140·log(L)". What is O? It's not clearly defined. From the table, accuracy is given. If O = accuracy, then O(30) = 0.8, O(45) = 0.5111, O(100) = 0.46. Let's check: log-log fit of these three points. log(0.8) = -0.0969, log(0.5111) = -0.2914, log(0.46) = -0.3372 (natural log: ln(0.8) = -0.223, ln(0.5111) = -0.671, ln(0.46) = -0.777). ln(30) = 3.401, ln(45) = 3.807, ln(100) = 4.605.

Slope from 30 to 100: (-0.777 - (-0.223))/(4.605 - 3.401) = -0.554/1.204 = -0.460. Hmm, they report slope = -0.4140. With three points, the regression slope would be somewhere in between. Let me compute more carefully:

x = [ln30, ln45, ln100] = [3.4012, 3.8067, 4.6052]
y = [ln0.8, ln0.5111, ln0.46] = [-0.2231, -0.6711, -0.7765]

mean x = 3.9377, mean y = -0.5569

Sxy = Σ(x-x̄)(y-ȳ) = (3.4012-3.9377)(-0.2231+0.5569) + (3.8067-3.9377)(-0.6711+0.5569) + (4.6052-3.9377)(-0.7765+0.5569)
= (-0.5365)(0.3338) + (-0.1310)(-0.1142) + (0.6675)(-0.2196)
= -0.17908 + 0.01496 - 0.14658
= -0.3107

Sxx = (0.5365)² + (0.1310)² + (0.6675)² = 0.28783 + 0.01716 + 0.44556 = 0.75055

slope = -0.3107/0.75055 = -0.4140. ✓ Great, so O = accuracy confirmed, slope matches.

Intercept: ȳ - slope·x̄ = -0.5569 + 0.4140×3.9377 = -0.5569 + 1.6302 = 1.0733. ✓ matches 1.0731 (rounding).

So O is accuracy. Now R²: 

predicted: ŷ = 1.0731 - 0.4140x
ŷ(3.4012) = 1.0731 - 1.4081 = -0.3350
ŷ(3.8067) = 1.0731 - 1.5760 = -0.5029
ŷ(4.6052) = 1.0731 - 1.9066 = -0.8335

residuals: 
y1 - ŷ1 = -0.2231 + 0.3350 = 0.1119
y2 - ŷ2 = -0.6711 + 0.5029 = -0.1682
y3 - ŷ3 = -0.7765 + 0.8335 = 0.0570

SSres = 0.01252 + 0.02829 + 0.00325 = 0.04406
SStot = Σ(y-ȳ)² = 0.3338² + 0.1142² + 0.2196² = 0.11142 + 0.01304 + 0.04822 = 0.17268

R² = 1 - 0.04406/0.17268 = 1 - 0.2552 = 0.7448. ✓ matches 0.7447.

OK so the numbers are internally consistent. Good. But the conceptual problem stands: regressing accuracy against number of test items is not "size scaling" in any meaningful sense. Accuracy is an intensive quantity (a mean), not an extensive one. There's no theoretical reason accuracy should follow a power law in the number of test questions. The "data collapse" framework from physics applies when you have curves at different system sizes that collapse onto a universal curve after rescaling. Here, the whole P1/P3 construction seems conceptually confused — and ironically the manuscript itself criticizes the original P-L v1 for "语义错位" (semantic misalignment) of treating 9 backbones at single L=60 as "9 sizes of the same system". But the v3 fix (single backbone × multiple L where L = number of questions) is arguably equally semantically confused: number of evaluation questions is not a system size.

Hmm, but wait — maybe in their framework, L is meant to be dataset size or something. Let me re-read. "P1 尺寸标度（size scaling）FAIL（Mistral Large 2512 单 backbone 于 L ∈ {30, 45, 100} 的 log-log 拟合 R² = 0.7447 < 0.9，n = 3，p = 0.337）". And the table shows L=30 → 30 cells, L=45 → 45 cells, L=100 → 100 cells. So L = number of cells = number of test questions. And O = accuracy.

So the "size scaling" claim being tested is: accuracy follows a power law in the number of test questions. This is indeed a strange claim, but it appears to be the claim that the original P-L proposal made (or the framework inherited). The kill verdict FAIL is then almost guaranteed by construction, because accuracy depends on question composition. The manuscript does disclose (b) that the accuracy monotonic decrease is due to difficulty distribution shift of new StrategyQA cells. But then the honest conclusion should be: "P1 test is uninformative/confounded — the design cannot distinguish size scaling from question-difficulty effects", i.e., UNVERIFIED or INCONCLUSIVE, not a clean "FAIL → 尺寸标度不成立". The abstract states "P1 尺寸标度（size scaling）FAIL" and §7 states "尺寸标度不成立" as a kill-level conclusion. This is overclaiming given the disclosed confound. This is a MAJOR issue.

Actually, let me think about what the right verdict framing is. In their three-state framework, P1 FAIL means "the data does not show power-law scaling in L". Given the confound, the data indeed doesn't show power-law scaling, but the reason is question difficulty, not absence of size scaling. A kill verdict on the claim "accuracy scales as power law in number of questions" is technically supported by the data (R² = 0.7447 < 0.9), but the claim itself is a strawman — no one in scaling-laws literature claims accuracy scales with the number of eval questions. The paper should clarify what the original P-L claim actually was. If the original claim was about model size (parameters) or training data size, then this test doesn't address it at all. The manuscript never defines what "尺寸" (size) refers to in the P-L claim. This is a serious gap: the object of the kill is not defined precisely.

**Issue 2: n=3 with p=0.337 — statistical power**

The manuscript discloses (c) "三点拟合统计力不足（n = 3）". With n=3, df=1, the p-value of 0.337 for the slope. R² = 0.7447 with n=3. The threshold R² ≥ 0.9 with n=3 is extremely stringent/arbitrary — with 3 points, R² is very noisy. Also note: with n=3, the correlation r = ±√0.7447 = ±0.863, t = r√(n-2)/√(1-r²) = 0.863×1/0.504 = 1.71, p (two-tailed, df=1) = 0.337. ✓ consistent. So the numbers are internally consistent. But using a fixed R² ≥ 0.9 threshold with n=3 is statistically questionable — the kill line was pre-registered though, so per their discipline, FAIL stands. But the paper should note that with n=3, even a perfect power law with noise could easily fail R² ≥ 0.9. Actually, the deeper issue: pre-registered threshold + underpowered design = the kill was nearly guaranteed. The paper should discuss this. They do mention statistical power insufficiency. OK.

**Issue 3: P2 的 β 定义与 P2 PASS 的逻辑**

P2 tests "实现稳健性" (implementation robustness) via β bootstrap CI overlap across backbones. β is disclosed as "cell-level 代理斜率（per-cell score 对 cell_index 的线性回归斜率）" — the slope of per-cell score vs cell_index. Wait, what does this measure? Per-cell score (0/1?) regressed on cell index (1..60)? That measures whether accuracy trends across the question ordering. β ≈ -0.01 to -0.02 for all backbones, CIs overlap. Overlap of CIs → PASS "robustness". 

Hmm, several problems:
1. β being a "proxy slope" of score vs cell_index — this measures order effects / difficulty ordering, not any kind of scaling exponent. The manuscript discloses this ("不是 data collapse 主命题的 size scaling exponent"). Good disclosure. But then what does P2 PASS actually establish? It establishes that different backbones have similar per-cell score trends across cell index. That's a weak notion of "implementation robustness". The claim "跨实现稳健性成立" (cross-implementation robustness holds) is thus supported only in this narrow proxy sense. The abstract's phrasing "P2 实现稳健性 PASS（6 个独立 backbone 两两 β bootstrap CI 全部重叠，开源 3/3 + 闭源 3/3）" is accurate as far as it goes, but the interpretation "跨实现稳健性成立" in the conclusion overstates what the proxy measures. At minimum, the conclusion should carry the proxy caveat.

2. CI overlap as a test: overlapping CIs do not imply non-significant difference (the classic fallacy — two CIs can overlap while the difference is significant). Conversely, non-overlap implies significance but overlap doesn't imply non-significance. Using "CI overlap" as a PASS criterion for equivalence is statistically backwards for establishing robustness/similarity. To establish similarity, one should use equivalence testing (TOST) or show the CI of the difference lies within a pre-specified equivalence margin. With bootstrap n=1000/2000 and noisy cell-level data, CIs are wide (e.g., glm53: [-0.026, 0.008], width ~0.034), so overlap is almost guaranteed — the test has no power to detect heterogeneity. So P2 PASS is nearly vacuous. This is a significant methodological weakness that the paper doesn't acknowledge. Actually wait — is this within my remit as "内容审 A" (content reviewer, not code)? Yes, this is about argumentation and claim-evidence matching, not code. The claim "P2 PASS → 跨实现稳健性成立" relies on a statistically invalid inference (CI overlap = equivalence). This should be flagged as a major issue.

3. Also, the OR embedding group got 1/6 overlap (GRAY), and 豆包 group showed "structural finding — endpoint-internal 收敛、跨 endpoint 离散". So across all tested groups, the robustness actually failed in the embedding groups. The headline "P2 实现稳健性 PASS（6 个独立 backbone...）" cherry-picks the 6 LLM backbones while the embedding groups failed. The abstract does mention "开源 3/3 + 闭源 3/3" but doesn't mention the OR 1/6 GRAY in the abstract. §4.4 does disclose it, and §6(3) discloses it. But the "数字降格（必改）" note in §4.4 says earlier drafts' "P2 强稳健" must be downgraded to "P2 3/5 backbone overlap（1 OR×OR 失败）" — wait, this is confusing. The note says the downgrade is required, but then the table in §4.5 still says "P2 实现稳健性 | β CI overlap | 两两重叠 | 6/6 backbone | PASS". And the abstract says "P2 实现稳健性 PASS（6 个独立 backbone 两两 β bootstrap CI 全部重叠，开源 3/3 + 闭源 3/3）". So did they apply the downgrade or not? The "必改" note says the expression must be downgraded to "3/5 backbone overlap (1 OR×OR 失败)", but the actual text still presents P2 as PASS with 6/6. This is internally inconsistent: the correction note and the main text disagree. Actually, hmm, let me re-read.

"> **数字降格（必改）**：早前文稿的 `P2 强稳健` 表述须降格为 **`P2 3/5 backbone overlap（1 OR×OR 失败）`**。实测 β CI overlap 在 OR embedding 组为 1/6；且需明确披露 β 为 **cell-level 代理斜率**..."

So this note says: earlier drafts said "P2 强稳健" which must be downgraded. But the current draft's §4.5 table and abstract still say "P2 PASS (6/6)". The note seems to be a leftover instruction that wasn't actually executed in the text — or the framing is "P2 PASS for the 6 LLM backbones, GRAY for embeddings". The "3/5 backbone overlap" phrasing is confusing (3/5 of what? 5 groups? 5 backbone groups?). Actually maybe "3/5" refers to... hmm. There were groups: 开源 3 backbone (3/3 pairs overlap), 闭源 3 backbone (3/3 pairs), OR embedding 4 项 (1/6 pairs), 豆包 5 embedding (structural finding). So "3/5" might mean 3 of 5 worker groups? The 5 worker cross-backbone mentioned in §2. So 3/5 groups pass? But then the verdict should be PARTIAL or GRAY overall, not PASS. The abstract's "P2 实现稳健性 PASS" with the parenthetical only citing the 6 LLM backbones is arguably cherry-picking. At minimum, there's an unresolved internal contradiction between the "必改" note (which mandates downgrading to "3/5") and the actual verdict presented (PASS 6/6). This is exactly the kind of "数字漂移" the manuscript itself claims to have fixed. This is a significant internal consistency issue — a leftover editorial note that contradicts the presented verdict. Blocker-level for internal consistency? I'd say 重要 (important) — the verdict framing must be unified.

Actually, let me reconsider. The note says "早前文稿的 P2 强稳健 表述须降格为 P2 3/5 backbone overlap（1 OR×OR 失败）". The current text says "P2 实现稳健性总判定：PASS（6 个独立 backbone 两两 β CI 全重叠）". These are different statements. If the mandated downgrade was to "3/5", then the current "PASS" verdict contradicts the mandated correction. Either the correction was superseded (then the note should be removed) or it wasn't applied (then the verdict is wrong). As a reviewer, I flag: the draft contains an unexecuted mandatory correction note that contradicts its own headline verdict; this must be resolved. Also the abstract says "P2 实现稳健性 PASS（6 个独立 backbone 两两 β bootstrap CI 全部重叠，开源 3/3 + 闭源 3/3）" — this omits the embedding failures from the headline. Given the paper's own ethos of "不轻信正面结果", this is a notable lapse.

**Issue 4: 85.0% 复现率**

§3.1: "实值 60 cells 中 51 项复现 = 85.0%". 51/60 = 0.85 exactly. ✓. The correction note says earlier drafts had 87.0% with no on-disk basis. OK, good correction practice. But "复现率" definition: "沿 P-C distortion bound 60cells 的复现率" — what does "复现" mean here? 51 of 60 cells reproduced... what? This is vague. What is being reproduced? The distortion bound? A reader can't tell what the 85% measures. Needs definition.

**Issue 5: 0.867 均衡带**

§3.1: "双主线在 26/30 = 0.8667 处精确重合：doubao-seed-2.0-lite（26/30）与 glm-5.3（26/30）两个模型落入同一均衡带。这是 9 model 账本中唯一出现的双模型精确重合点，构成跨实现稳定性的一处正面证据。"

Two models both getting 26/30 correct is... just two models with the same accuracy on a 30-question test. Calling this an "均衡带" (equilibrium band) and "跨实现稳定性的正面证据" is overinterpretation. With 9 models, the probability that at least two share the same score out of 30 is quite high (birthday-paradox-like). This is a numerology-flavored claim. The term "均衡带" suggests game-theoretic equilibrium (tying to 王老师's equilibrium work), but no equilibrium concept is defined or measured here. This is exactly "把观察性数值说成定理" territory — though they do call it "一处正面证据" rather than a theorem. Still, "精确重合" (exact coincidence) language is overhyped for a coincidence that's statistically unremarkable. Flag as 重要 or 建议. Also note §5.3 Adendum K refers to "0.867 均衡聚类跨 backbone" which failed (FAIL_NO_MODEL), so the "均衡带" claim rests on the two-model coincidence only.

**Issue 6: P-C 幂律前件 R² = 0.1986 / 0.2670 双 FAIL_H0**

§3.1: "含环 328 图残余 r 对循环空间维数 d 的 log-log 回归给出 R² = 0.1986 / 0.2670 双 FAIL_H0（幂律死，b 的 95% CI 含 0）". Two R² values — for what two fits? Not explained. "双 FAIL_H0" — two datasets? Two methods? Unclear. Also §5.3 Adendum P says "P-C two_phase = FAIL_H0（幂律死）与 P-L v3 P1 尺寸标度 R² 是数学前件关系。若 P-L v3 P1 log-log R² < 0.9，应判为与 P-C two_phase 一致的幂律死，而非「P-L 实验失败」。两个独立命题指向同一「无幂律」结论，构成 paper 中「两个独立通道指向同一无幂律」的强证据。"

"强证据" (strong evidence) — two underpowered/confounded null results do not constitute strong evidence of "no power law". Absence of evidence ≠ evidence of absence. Also the "数学前件关系" (mathematical antecedent relation) claim: "data collapse 的前件是「存在幂律标度」" — this is asserted but not argued. Data collapse in the FSS sense presupposes a scaling ansatz, yes, but the logical structure here is loose. And calling two null results "强证据" is an overstatement. Flag.

**Issue 7: 摘要中的数字一致性**

Abstract: "P1 尺寸标度（size scaling）FAIL（Mistral Large 2512 单 backbone 于 L ∈ {30, 45, 100} 的 log-log 拟合 R² = 0.7447 < 0.9，n = 3，p = 0.337）" — consistent with §4.3. ✓

"P3 标度塌缩 FAIL（归一化残差 Q = 0.1929 > 0.15）" — §4.3 says Q = 0.1929, 判读: < 0.05 塌缩成立 / [0.05, 0.15) 边缘 / ≥ 0.15 无塌缩. So Q = 0.1929 ≥ 0.15 → 无塌缩 → FAIL. ✓ consistent. But note §4.5 table says "P3 标度塌缩 | 归一化残差 Q | < 0.05 | 0.1929 | FAIL" — the threshold column says < 0.05, but the decision rule has three zones. Q = 0.1929 falls in "无塌缩" zone either way, so FAIL is consistent. Minor presentation inconsistency (threshold listed as < 0.05 vs three-zone rule). Minor.

"P2 实现稳健性 PASS（6 个独立 backbone 两两 β bootstrap CI 全部重叠，开源 3/3 + 闭源 3/3）" — see Issue 3.

"60 cells 复现率 85.0%" ✓; "22 caption dual_24bit 链 22/22 PASS" ✓; "17 项 Adendum 中 11 项 PASS、2 项 GRAY、1 项 UNVERIFIED、2 项 PARTIAL、1 项 FAIL_NO_MODEL" — 11+2+1+2+1 = 17 ✓ consistent with §5.1 table.

§5.1 table: PASS 11: B, C, D, E, I, J, L, M, N, P, Q — that's 11 letters ✓. GRAY 2: H, O ✓. UNVERIFIED 1: A ✓. PARTIAL 2: F, G ✓. FAIL_NO_MODEL 1: K ✓. Total letters: A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q = 17 ✓.

Wait — but §5.2 says Adendum A (退化预检族) has 4 子项, of which "4 子项中 3 项发现真 bug" — the table in §5.2 lists P-J (✅ 是), P-I (部分), P-M (✅ 是), P-C exp_3_3 (✅ 是). So 3 真 bug + 1 部分. The abstract says "如实披露四处退化预检发现的真 bug" — "四处退化预检发现的真 bug" could be read as "4 处真 bug" but actually it's 3 真 bug + 1 部分. Hmm, "四处退化预检发现的真 bug" — ambiguous: "四处" might modify "退化预检" (four degradation prechecks) rather than "真 bug". Reading: "四处退化预检发现的真 bug" = "the real bugs found by the four degradation prechecks". That's 3 real bugs + 1 partial. OK, ambiguous but defensible. §6 补充 says "本轮 4 项退化预检发现的真 bug（P-J / P-M / P-C exp_3_3）" — lists only 3 items but says "4 项退化预检" (4 prechecks). OK consistent-ish. Minor wording.

Also abstract says "17 项 Adendum 中 11 项 PASS..." — but Adendum A is UNVERIFIED, and its sub-items include P-I which is marked PASS in the §5.2 table ("P-I 曲率审计探针 | ... | 部分 | PASS"). Wait, the §5.2 table's 裁定 column: P-J → UNVERIFIED, P-I → PASS, P-M → UNVERIFIED, P-C exp_3_3 → UNVERIFIED. But §5.1 says Adendum A overall is UNVERIFIED. And §5.1 PASS list includes... let me check: PASS = B, C, D, E, I, J, L, M, N, P, Q. Wait, that includes I, J, M as separate Adenda! But §5.2 treats P-J, P-I, P-M, P-C as sub-items of Adendum A (退化预检族). So there's a double counting or mapping confusion: Adendum A is the precheck family that examined P-J/P-I/P-M/P-C artifacts, and separately Adenda I, J, M exist as their own items with their own verdicts (I PASS, J PASS, M PASS?). Hmm wait, §5.1 says M is PASS. But §5.2 says P-M 攻击面 has detection_rate 10/10 all 0.0 with safety_index = SECURE (contradiction), 裁定 UNVERIFIED, and §8 item 5 says "P-M v42 须重设计：detection = 0 与 safety_index = SECURE 的矛盾必须消除". So how can Adendum M be PASS in §5.1 while P-M is UNVERIFIED in §5.2? 

Hmm, maybe the letters in §5.1 (A–Q) are Adendum labels, and the P-x labels are proposal/挂点 labels, and the mapping is: Adendum A = 退化预检族 (which checked P-J, P-I, P-M, P-C exp_3_3 artifacts), Adendum I = P-O 24/26 closure (§5.3 says "Adendum I（PASS）：P-O 24/26 闭合为 26/26"), Adendum J = 全仓排序健康体检, Adendum L = verifier 双实现差分, Adendum P = P-C two_phase vs P-L v3 P1 前件关系, Adendum Q = deepseek-v4-pro 下界锚. So Adenda letters don't map 1:1 to P-x labels. OK so Adendum M (PASS) is something else, not P-M. But this is genuinely confusing for a reader: Adendum I deals with P-O, Adendum P deals with P-C/P-L... The naming collision between Adendum letters and P-x 挂点 labels is a readability hazard. E.g., "Adendum C 勘误" (§5.4) vs "P-C exp_3_3" (§5.2) vs "P-C 幂律前件" (§3.1). A reader will conflate them. Flag as 建议 (presentation): provide a mapping table Adendum letter ↔ 挂点/命题 ↔ 产物文件.

But wait, there might be a real inconsistency: §5.2's P-I 裁定 is "PASS（d_E 单通道超 0.5 随机基线，属探测性非审计资产）" — so within Adendum A (UNVERIFIED overall), one sub-item is PASS. And §5.1 lists Adendum A as UNVERIFIED. Fine. But then the abstract's "11 项 PASS" includes I, J, M as separate Adenda. Without the mapping table, can't verify. I'll flag the mapping issue and the potential M/P-M confusion as needing clarification.

**Issue 8: §5.4 Adendum C 勘误 — "annotation ≠ mutation"**

The erratum adds annotations to frozen JSON files, changing their SHA-12 (d64e8e2e2518 → 6eba63788ca8). If these files are among the 18 frozen anchors or 5 制品, changing them violates 0 触动. Are Adendum C JSONs frozen? They're `_adendum_C_..._133852.json` — probably not in the frozen list (frozen list is KT specs, P-F series, v19/v21, corpus index, anchor JSONs, plugin specs). So probably fine, but the paper should state explicitly that the annotated files are not among the 18 frozen anchors / 5 制品, otherwise the "0 触动" claim is jeopardized. Also "annotation ≠ mutation，原值零改动" — appending an annotation to a JSON changes the file; calling it "not mutation" is a semantic distinction that needs a precise definition (annotation appended in a separate field? separate file?). Flag as 建议/重要: clarify the erratum mechanism and confirm no frozen asset was modified.

**Issue 9: 挂点回扣 §5.5**

The 4 挂点 callbacks: The table's "王老师侧（提案 v3 引用）" column — e.g., 挂点 1: "540/540 账全轧平，双主线 26/30 精确重合 0.867" — wait, this is supposed to be 王老师's side (the collaborator's work), but "540/540 账全轧平" is the authors' own result. The table seems to mix up which side is which. Let me re-read.

| 挂点 | 王老师侧（提案 v3 引用） | 我方 V3X 侧 | 一致性 |
| 挂点 1：9 模型 × 60 题账本 | 540/540 账全轧平，双主线 26/30 精确重合 0.867 | 3 开源 backbone β CI overlap PASS + ... | ✓ 实现稳健 |

Hmm, "王老师侧（提案 v3 引用）" should cite 王老师's work (e.g., AAAI 2026 SPPE, WINE 2025, arXiv:2604.24530). But the cell contains "540/540 账全轧平，双主线 26/30 精确重合 0.867" which is the authors' own V3X result, not 王老师's work. Similarly 挂点 2's 王老师侧: "KT-D0 主锚 03C6C01F3697 = anchor 0" — that's the authors' own anchor. 挂点 3's 王老师侧: "KT-C1 幂律 R² = 0.0007 死的是自己主张；KT-B1 22.5% < 50% 判死线走正面结果" — these are the authors' own prior KT results, not 王老师's. 挂点 4's 王老师侧: "9 模型 cross-backbone" — again authors' own.

So the entire "王老师侧" column does not actually cite 王老师's work! Compare with §1's table which does list 王老师's work (AAAI 2026 SPPE, WINE 2025, arXiv:2604.24530). The §5.5 table is supposed to demonstrate the connection to the collaborator's directions, but the "王老师侧" column contains the authors' own artifacts. This makes the 挂点回扣 effectively 自说自话 (talking to oneself) — exactly what review criterion 5 asks about. This is a MAJOR finding for criterion 5. The 一致性 column asserts "✓ 实现稳健", "✓ 内容寻址 + 根指纹 + 追加链模式一致" etc., but since the comparison is between two columns of the authors' own results, the "consistency" is trivial/self-referential. The genuine mapping to 王老师's directions (equilibrium migration cost, distribution reporting with distortion bounds, private information thresholds, reproducibility infrastructure, scaling behavior) is asserted in §1's table but never actually executed with content from 王老师's papers. E.g., P-A′ claims to connect to "AAAI 2026 SPPE 精确计算 + 均衡迁移成本" but no equation, theorem, or result from SPPE is cited or compared. So the 挂点回扣 is currently decorative. MAJOR.

Also note: the P-L 挂点 maps to "复杂场景下的标度行为" — generic. The kill of P-L is thus a kill of the authors' own formulation, not of anything in 王老师's work. That's fine (they say 判死对象是挂点而非方向), but the paper should be careful not to imply the collaborator's scaling-behavior direction is affected.

**Issue 10: 摘要结论 "部分拒绝" 的逻辑**

"P-L data collapse 假设被部分拒绝——尺寸标度不成立，但跨实现稳健性成立。" The "部分拒绝" framing: P1 FAIL + P3 FAIL + P2 PASS. But as discussed, P2's PASS is (a) based on CI-overlap-as-equivalence (invalid), (b) contradicted by embedding groups, (c) measuring a proxy unrelated to data collapse. So the "部分" that's not rejected (P2) is the weakest part. Meanwhile P1's FAIL is confounded by question difficulty. So the honest summary is closer to: "the test as designed cannot adjudicate size scaling (confounded + underpowered); the robustness proxy shows overlap among 6 LLM backbones but fails in embedding groups." The headline "部分拒绝" is a reasonable framing of the pre-registered verdicts, but the interpretation in §7 ("尺寸标度不成立...跨实现稳健性成立") states both as facts. Given the disclosed confounds, these should be hedged. The paper's own three-tier discipline (判死级/观察性/探索性) requires that kill-level claims be pre-registered and executed — P1/P3 were pre-registered, so FAIL verdicts stand as "判死级" facts about the pre-registered test. But the semantic leap from "the pre-registered test failed" to "尺寸标度不成立" (size scaling doesn't hold) is an interpretation that should be flagged as 观察性 at best, given confound (b). I think the cleanest reviewer demand: keep the pre-registered verdicts, but explicitly scope them: "在本测试设计下" and note the confound limits external validity; and downgrade P2's interpretation.

**Issue 11: 结构完整性**

8 章 outline: 摘要, §1 Introduction, §2 V3X 设计, §3 P-C + P-D 双 PASS, §4 P-L v3 三态分离, §5 17 项 Adendum, §6 限制, §7 结论, §8 派生建议. That's abstract + 8 sections. The header note says the 委托信 §1 表 §7「结论 + 派生建议」was split into §7 and §8. The split is clean. §6 header says "限制（paper §7.2）" — referencing "paper §7.2" is confusing since this is §6; it's a mapping note to the outline's numbering. Minor.

Repetition: The 4 方共识 table appears in §2 and again in 附录 C (verbatim). The 7 铁律 appear in §1 and again in 附录 D (expanded). Some repetition is fine for appendices, but 附录 C is a verbatim duplicate of §2's table — could be trimmed or cross-referenced. Minor.

§4.2 mentions "v3 worker C：改用 Mistral Large 2512 × 30 cells 跨 backbone，Spearman = 0.375（PASS，破同序）" — "跨 backbone" with a single backbone (Mistral)? "Mistral Large 2512 × 30 cells 跨 backbone" is contradictory phrasing. Probably means cross-... hmm. Actually maybe worker C used Mistral × 30 cells and compared against the 9-model L=60 data? Unclear. The Spearman = 0.375 at L=30 (§4.3: "L = 30 时 0.3750（p = 0.0412，N = 30...破 backbone 同序成立）") — Spearman between what and what? "破 backbone 同序" — breaking the rank identity across backbones. So it's the correlation between Mistral's per-cell scores at L=30 and ... the 9-model aggregate at L=60? Not defined. The auxiliary Spearman's role is unclear: "辅助 Spearman（cell-level，非塌缩判死指标）" — correlation between which two vectors? Needs definition. Flag.

Also §4.3 table row L=60: "（9 model aggregate）... 仅 reference" — so the L=60 point is NOT Mistral-only and is excluded from the fit (fit uses 30/45/100). Good that it's excluded (mixing aggregates would be wrong), but then why include it in the table at all? For reference, fine. But note the fit uses only 3 points while 4 sizes were run — because L=60 wasn't run for Mistral alone? That's a design gap: why not run Mistral at L=60 to get a 4th point? Cost? Should be explained. Actually §2 says "Phase 1 P-L v3（Mistral × L{30,45,60,100}）" — so L=60 was planned for Mistral! But §4.3's table shows L=60 as 9-model aggregate "仅 reference". So either the Mistral L=60 run failed/wasn't done, or it was replaced. This discrepancy between §2's plan (Mistral × L{30,45,60,100}) and §4.3's actual (Mistral at 30/45/100 only, L=60 = aggregate) is unexplained. If Mistral L=60 exists, adding it would give n=4 and materially change the fit. This is a real gap. Flag as 重要: explain why Mistral L=60 is absent; if data exists, include it.

Hmm wait, actually maybe the L=60 for Mistral is the "mistral" row in Phase 2 (accuracy 0.8000, 60 cells)? §4.4 开源 table: mistral accuracy 0.8000. And L=30 Mistral accuracy is also

---

## tech_B1_dsv4pro（or:deepseek/deepseek-v4-pro → served: deepseek/deepseek-v4-pro）

- 状态：OK　报告 SHA-12：`22123cb4aba2`

我们需要回答中文。需要严格审稿。需要仔细分析手稿。用户要求角色统计与方法论审稿人，只审统计正确性与方法论严谨性。需要输出格式严格遵守。需要从 ACCEPT/MINOR/MAJOR/REJECT 选。需要具体位置与可执行改法。需要核对数字。

我们需要深入审稿。手稿内容复杂。需要识别统计问题。

先理解手稿。核心：deposon V3X 一周判死实验。P-L data collapse 三态分离：P1 size scaling FAIL (R²=0.7447<0.9, n=3, p=0.337); P3 collapse FAIL (Q=0.1929>0.15); P2 implementation robustness PASS (6 backbones β bootstrap CI all overlap). Also P-C/P-D double PASS, 17 Adendum etc.

需要审统计正确性。重点问题：

1. P1 尺寸标度：三点拟合 n=3，R²=0.7447，p=0.337。统计力不足。FAIL 判定是否合理？阈值 R²≥0.9 是预注册？三点拟合固有局限是否充分披露？手稿 §4.3 披露三点不确定性 (a)(b)(c)，但结论仍 FAIL。需要审：三点 log-log 拟合 R² 本身对 n=3 几乎无统计力；p=0.337 是斜率检验？n=3 时 p 值不可靠。R² 阈值 0.9 对 n=3 可能太严/太松？需要指出：FAIL 应表述为“未达到预注册阈值，不能支持标度”，而非“尺寸标度不成立”的强否定。手稿摘要和结论说“尺寸标度不成立”，但统计上只能“未能拒绝无标度/证据不足”。需要建议改为“未达预注册阈值，不足以支持尺寸标度”或“在预注册阈值下 FAIL，但统计力不足，不能排除尺寸标度”。位置摘要、§4.3、§4.5、§7。

2. P3 Q = 0.1929 阈值依据？Q 定义与计算式是否给出？手稿没有给出 Q 的定义公式，只说归一化残差 Q，主曲线 O(L)=2.9243·L^(−0.4140)，阈值 <0.05 成立 / [0.05,0.15) 边缘 / ≥0.15 无塌缩。需要指出：Q 的定义、归一化方式、残差类型（相对？绝对？）、是否预注册？阈值依据未给出。这严重。需要建议在方法部分给出公式，例如 Q = sqrt(mean((O_i - O_fit(L_i))^2 / O_i^2)) 或类似，并说明阈值来源（预注册？文献？）。如果未预注册，则不能作为判死线。手稿声称判死线 SPEC 先于运行冻结并公布 SHA-12，但 Q 阈值是否在 SPEC 中？需要核实。手稿未提供。审稿应指出阻断/重要。

3. P2 β bootstrap CI overlap：以 CI 重叠判定“实现稳健”统计上是否成立？CI 重叠与无显著差异关系：95% CI 重叠是保守的，不重叠意味着显著差异，但重叠不一定意味着无显著差异；用“全部重叠”作为 PASS 可能太弱，可能把实际有差异的也判为 PASS。更严谨应使用 bootstrap 差异的 CI 是否包含 0，或进行多重比较校正。手稿说“两两 β bootstrap CI 全部重叠”作为 PASS。需要指出：CI overlap 不是等价于无显著差异；如果目的是“实现稳健性”，应定义效应量等价边界（equivalence margin），或至少报告差异 CI。另外 β 是 cell-level 代理斜率，非 size scaling exponent，已降格披露，但摘要和结论仍可能误导。需要检查是否充分披露：§4.4 数字降格说明，§6(5) 诚实披露，但摘要说“P2 实现稳健性 PASS（6 个独立 backbone 两两 β bootstrap CI 全部重叠）”，没有在摘要中说明 β 是代理斜率。结论 §7 说“跨实现稳健性成立（P2 6/6 backbone β CI 全重叠 PASS）”，也未说明代理。可能误导。需要建议摘要/结论加限定“cell-level 代理斜率，非 size scaling exponent”。

4. 三态分离框架逻辑是否自洽？“部分拒绝”表述是否准确？需要分析：P1 和 P3 都 FAIL，P2 PASS。P-L data collapse 假设被部分拒绝。但 P2 是“实现稳健性”，不是 data collapse 本身？如果 P1/P3 是 data collapse 的核心，P2 是跨实现稳健性，那么“部分拒绝”可能不准确：data collapse 假设本身被拒绝（尺寸标度不成立、塌缩不成立），而实现稳健性成立是另一个命题。说“部分拒绝”可能让人误以为 data collapse 部分成立。需要建议改为“P-L data collapse 主张在预注册阈值下被拒绝（P1/P3 FAIL）；跨实现稳健性作为独立命题 PASS，不构成对 data collapse 的支持”。或者“部分拒绝”需明确定义：拒绝的是尺寸标度与塌缩，未拒绝的是实现稳健性。手稿 §4.5 有解释，但摘要/结论可能误读。需要指出。

5. P-K FPR = 4.44% 双口径：机器 OVERALL FAIL / paper 处置 GRAY 是否自相矛盾？需要审：如果预注册阈值 1%，FPR 4.44% > 1%，机器判定 OVERALL FAIL，但 paper 处置 GRAY，理由样本量与盲测设计限制。这可能是“不调阈值”但改变判定标签？需要指出：如果阈值预注册，超过阈值应为 FAIL，不能因样本量小改为 GRAY；否则违反预注册。但手稿说“沿 KIMI 7 方向，不调阈值”，却将 paper 处置标为 GRAY。这确实矛盾。需要建议：要么维持 OVERALL FAIL，将 GRAY 作为敏感性分析/限制；要么明确 GRAY 是“证据强度不足”而非“不 FAIL”，并说明预注册判定仍为 FAIL。手稿 §5.1 将 O 列为 GRAY，§6(2) 双口径。需要指出矛盾，建议统一：主判定 OVERALL FAIL，GRAY 仅作为证据质量标签，不能替代主判定。

6. 4 项必改数字：85.0% / Adendum 17 / P2 降格 / P-K 双口径是否全部正确落位？需要逐项核对。

- 85.0%：摘要说 60 cells 复现率 85.0%；§3.1 说 51/60=85.0%，数字修正。结论 §7 说 85.0%。落位正确。但需要检查 §3.1 表？没有表。摘要正确。可能还有“87.0%”残留？手稿没有。需要确认。
- Adendum 17：摘要说 17 项 Adendum 中 11 PASS、2 GRAY、1 UNVERIFIED、2 PARTIAL、1 FAIL_NO_MODEL。§5 数字修正说 11+2+1+2+1=17。§5.1 表合计 17。结论 §7 说 17 项 Adendum 中 11 PASS。落位正确。但需要检查 §5.1 表项：PASS 11 项 B,C,D,E,I,J,L,M,N,P,Q；GRAY 2 H,O；UNVERIFIED 1 A；PARTIAL 2 F,G；FAIL_NO_MODEL 1 K。合计 17。正确。但注意 §5.2 退化预检族 Adendum A 说“4 子项中 3 项发现真 bug”，但表 §5.1 说 A UNVERIFIED。可能一致。需要检查是否有新不一致：摘要说“17 项 Adendum 中 11 项 PASS、2 项 GRAY、1 项 UNVERIFIED、2 项 PARTIAL、1 项 FAIL_NO_MODEL”正确。
- P2 降格：§4.4 数字降格说明“早前文稿的 P2 强稳健 表述须降格为 P2 3/5 backbone overlap（1 OR×OR 失败）”。但摘要仍说“P2 实现稳健性 PASS（6 个独立 backbone 两两 β bootstrap CI 全部重叠，开源 3/3 + 闭源 3/3）”。这里“6 个独立 backbone”与降格说明“3/5 backbone overlap（1 OR×OR 失败）”可能不一致？需要分析：P2 主判定是 6 个独立 backbone（开源 3 + 闭源 3）两两 CI 全重叠 PASS。OR embedding 组是额外 4 项，1/6 GRAY。降格说明“P2 3/5 backbone overlap（1 OR×OR 失败）”似乎把 OR 组也算入 P2，但主判定仍 6/6。这可能导致数字不一致：摘要说 6 个独立 backbone 全重叠，但 §4.4 降格说 3/5 backbone overlap。需要澄清：P2 主判定基于 6 个 backbone（3 开源 + 3 闭源）全重叠；OR embedding 组是附加稳健性检查，1/6 GRAY，不改变主判定？但降格说明“P2 3/5 backbone overlap”可能意味着 5 组中 3 组 overlap？需要指出不一致。手稿 §4.4 标题“P2 实现稳健性总判定：PASS（6 个独立 backbone 两两 β CI 全重叠）”，然后数字降格说“早前文稿的 P2 强稳健 表述须降格为 P2 3/5 backbone overlap（1 OR×OR 失败）”。这确实矛盾：如果总判定 PASS 基于 6/6，降格为 3/5 则总判定不应是 PASS？需要审稿指出：P2 降格未完全落位，摘要和结论仍使用“6/6 全重叠 PASS”，未提及 OR 1/6 GRAY 或 3/5 降格。需要建议统一表述：主判定 6/6 全重叠 PASS，但附加 OR embedding 组 1/6 GRAY，因此“强稳健”降格为“有限稳健”；或者如果降格为 3/5，则主判定需重新评估。手稿 §5.5 挂点 1 也写“3 开源 backbone β CI overlap PASS + 3 闭源 backbone β CI overlap PASS + OR 1/6 GRAY + 豆包 structural finding”，这里一致。但摘要未提 OR GRAY。需要指出。
- P-K 双口径：摘要说“GLM 制品盲测假阳性率 4.44%”但未说 OVERALL FAIL/GRAY？摘要说“我们同时如实披露四处退化预检发现的真 bug、GLM 制品盲测假阳性率 4.44%、以及 5 制品 schema 互异等限制。”没有说判定。§6(2) 双口径。结论 §7 未提 P-K。可能落位不完全。需要指出摘要应明确“P-K 机器判定 OVERALL FAIL，paper 处置 GRAY（双口径）”，否则读者不知道判定。

7. SHA-12 自验：用 SHA-256 前 12 位（48 bit）做锚是否可靠？碰撞风险是否需声明？需要审：48-bit 哈希碰撞概率：生日攻击约 2^24 ~ 1.6e7 次有 50% 碰撞；对于少量文件（几十个）碰撞概率很低，但作为“锚”用于完整性验证，48 bit 安全性不足，恶意碰撞可能。需要声明碰撞风险，或使用完整 SHA-256 或至少 16 位（64 bit）。手稿说“SHA-256 前 12 位锚”，并自验 100% PASS。需要指出：48-bit 锚只能作为便捷标识，不能作为防篡改证据；应报告完整 SHA-256 或至少 64-bit，并声明碰撞风险。位置附录 A、§1 判死承诺、§2 冻结资产层等。严重度重要。

其他统计问题：

- P1 拟合：log(O) = 1.0731 − 0.4140·log(L)，R²=0.7447，p=0.337203。需要检查 p 值含义：斜率 t 检验？n=3 自由度 1，p=0.337 可能来自 t 分布？但 n=3 时 p 值不可靠。需要指出。另外 R² 对 n=3 可能高估/低估？三点拟合 R² 可以很高但无统计意义。需要建议报告置信区间或贝叶斯后验，或至少说明 n=3 无法区分幂律与其他单调函数。手稿 §4.3 已披露三点不确定性，但结论仍强。需要建议在摘要/结论加“统计力不足，不能排除尺寸标度”。

- P3 Q 阈值：未给出 Q 定义。需要指出。

- P2 bootstrap CI：需要报告 bootstrap 方法细节：n=1000/2000，CI 类型（percentile? BCa?），β 定义（per-cell score 对 cell_index 线性回归斜率），是否控制多重比较？两两比较 3 组有 3 对，6 组有 15 对？手稿说开源 3 对，闭源 3 对，共 6 对。需要指出多重比较。另外“CI 重叠”作为 PASS 标准可能太宽松；应使用差异 CI 或等价检验。

- P-C 幂律前件：R²=0.1986/0.2670 双 FAIL_H0，b 的 95% CI 含 0。这个可以，但需要检查是否预注册阈值？可能没问题。

- 0.867 均衡带：26/30=0.8667 精确重合，两个模型落入同一均衡带。这是观察性，但“精确重合”可能过度解释：两个模型 accuracy 相同不代表均衡带。需要指出：样本量 30，accuracy 相同可能是巧合；应报告置信区间。手稿说“构成跨实现稳定性的一处正面证据”，但统计上弱。需要建议降格为观察性，报告 CI。

- 60 cells 复现率 85.0%：需要报告置信区间？n=60，51/60=85%，95% CI 约 73.4%-92.5%。手稿未报告。需要建议报告 Wilson CI 或 Clopper-Pearson。另外“复现率”定义是否预注册？需要说明。

- 22 caption 22/22 PASS：样本量小，需要报告二项分布置信区间，22/22 的 95% CI 约 84.6%-100%。手稿未报告。需要建议。

- Adendum H：std=2.028，CV>0.4 不稳健；剔除 2 个边界后 std=0.629 仍 GRAY。样本量不足。这个可以，但需要报告剔除标准是否预注册？可能没问题。

- 退化预检族：4 类不变性预检发现 3 项真 bug。需要审：这些预检是否预注册？手稿说“0 LLM hashlib + numpy 的 4 类不变性预检”，但未说明预注册。如果预检是事后发现，则不能作为判死依据？需要指出：应明确预检是否在数据冻结前预注册；否则属于探索性发现，不能作为 UNVERIFIED 判定。手稿 §5.2 说“横切修复建议”，可能不是预注册。需要建议说明。

- 判死线 SPEC 先于运行冻结并公布 SHA-12 前 12 位锚：需要审：SHA-12 锚只能证明文件未变，但不能证明内容预注册？如果只公布哈希，未公开 SPEC 内容，则无法验证预注册。需要指出：应公开完整 SPEC 或至少可验证的承诺。手稿未提供 SPEC 内容。需要建议。

- 数字一致性：摘要说“9 个 LLM backbone × 60 题（540 cells）”，§3.1 说 9 个 LLM backbone × 60 题 = 540 cells，全部账本恒等式 T+R+A=1 轧平，9/9 model 残差为 0。但 §4.3 表 L=60 是 9 model aggregate，accuracy 0.7111。需要检查 60 cells 复现率 85.0% 与 accuracy 0.7111 的关系？可能不同指标。需要指出：60 cells 复现率 85.0% 与 L=60 accuracy 0.7111 定义不同，需明确。手稿 §3.1 说“沿 P-C distortion bound 60cells 的复现率，实值 60 cells 中 51 项复现 = 85.0%”，而 §4.3 表 L=60 accuracy 0.7111 是 9 model aggregate。可能一个是复现率，一个是 accuracy。需要澄清。

- §4.3 表 L=45 accuracy 0.5111，L=100 accuracy 0.4600，L=30 accuracy 0.8000。P1 拟合使用 30/45/100 三点，但表中有 L=60 0.7111 仅 reference。为什么不用 L=60？因为 9 model aggregate 不是单 backbone？需要说明。手稿说 L=60 复用 frozen per_model（仅 reference），所以不纳入拟合。可以，但需要说明为什么 L=60 不用于拟合：因为不是单 backbone 多尺寸。手稿有说明“仅 reference”。可以。

- P1 拟合 log(O) = 1.0731 − 0.4140·log(L)，R²=0.7447。需要检查 accuracy 0.8000, 0.5111, 0.4600 对应 L=30,45,100。log-log 拟合：log(0.8)≈-0.223, log(0.5111)≈-0.671, log(0.46)≈-0.777; log(L)≈3.401,3.807,4.605。斜率约 (-0.777+0.223)/(4.605-3.401)= -0.554/1.204=-0.46，接近 -0.414。R² 0.7447 可能。但 n=3 无意义。需要指出。

- P3 Q=0.1929：需要公式。可能 Q 是归一化残差平方和？未给出。

- P2 β bootstrap：需要报告 β 的估计值、CI、bootstrap 方法。手稿有表。但“β 为 cell-level 代理斜率（per-cell score 对 cell_index 的线性回归斜率）”需要明确 per-cell score 是什么？是 pass/fail? 如果是二值，线性回归斜率可能不合适。需要指出：如果 outcome 是二值（pass/fail），应使用 logistic 回归或概率随 cell_index 的变化，而不是线性回归斜率；β 的解释可能有问题。手稿未说明 score 类型。需要建议说明。

- 三态分离：P1 尺寸标度、P2 实现稳健性、P3 标度塌缩。逻辑上 P1 和 P3 都依赖尺寸标度，P2 是跨 backbone 稳健性。如果 P1 和 P3 FAIL，P2 PASS，那么“data collapse 假设被部分拒绝”可能不准确，因为 data collapse 本身被拒绝，P2 不是 data collapse 的组成部分。需要建议重新定义“部分拒绝”为“P-L 主张的两个核心标度命题被拒绝，一个稳健性命题通过”。

- 摘要说“P-L data collapse 假设被部分拒绝——尺寸标度不成立，但跨实现稳健性成立。”这可能导致误读：跨实现稳健性成立是否意味着 data collapse 部分成立？需要建议改为“P-L data collapse 主张在预注册阈值下被拒绝（P1/P3 FAIL）；跨实现稳健性作为独立命题 PASS”。

- 结论 §7 说“核心结论。P-L data collapse 假设被部分拒绝：尺寸标度不成立（P1 R² = 0.7447 FAIL、P3 Q = 0.1929 FAIL），跨实现稳健性成立（P2 6/6 backbone β CI 全重叠 PASS）。”同样问题。

- §4.5 综合判死表：P1 FAIL, P2 PASS, P3 FAIL。综合：部分拒绝。需要建议在表中加“统计力”列，或脚注说明 P1/P3 的 FAIL 是“未达预注册阈值”，不是“证明不存在”。

- 数字核对：需要检查摘要中“17 项 Adendum 中 11 项 PASS、2 项 GRAY、1 项 UNVERIFIED、2 项 PARTIAL、1 项 FAIL_NO_MODEL”与 §5.1 表一致。正确。

- 附录 A 自验：5 制品 SHA-12 校验 ✓；18 frozen anchors 表 16 个 ID + P-G 5 个 = 21；但表标题“18 frozen anchors（沿 schema v1，实算 16/16 + P-G 5/5）”列出 16 个 ID，然后 P-G 5 个。合计 21。但 §2 冻结资产层说“18 frozen anchors = 16 frozen + 5 P-G 锚”，这数学上 16+5=21，不是 18。手稿说“18 frozen anchors = 16 frozen（...）+ 5 P-G 锚”，这明显不一致：16+5=21，但称为 18 frozen anchors。需要指出数字不一致。可能“18 frozen anchors”是历史名称，但实际 21 个锚。需要建议澄清：要么改称 21 anchors，要么说明 18 是旧称。位置 §2、附录 A。这是重要数字不一致。

- 附录 A 表“18 frozen anchors”列出 16 个 ID，然后 P-G 5 个，合计 21。但表标题说 18 frozen anchors。需要指出。

- §2 冻结资产层：“18 frozen anchors = 16 frozen（4 份 KT SPEC V0.1 + P-F 系列 SPEC + v19/v21 基准 JSON + corpus v20 index + 2 份 anchor JSON + 4 plugin spec）+ 5 P-G 锚”。这里 16+5=21，但称为 18。需要指出。

- 附录 A 自验方式：“8 件自验 100% PASS。”但前面列了 5 制品 + 18 frozen + schema v1 + 4 plugin spec = 5+21+1+4=31 件？为什么说 8 件？可能“8 件”指 8 类？需要指出不一致。手稿附录 A 标题“8 件 SHA-12 自验”，但内容列了 5 制品、18 frozen、schema v1、4 plugin spec，共 28/31 件。需要澄清“8 件”的定义。可能“8 件”是 8 个类别？但未说明。需要指出。

- 附录 B 5 audit 综合产物：聚合 SHA-12 为“—”，可能没问题。

- §5.5 挂点回扣表：挂点 2 说“锚链 `c4cae1ed9ee5`”，但附录 A 未列出该锚。需要检查是否一致？可能锚链是另一项。需要指出：如果引用锚链，应在附录 A 列出并自验。手稿未提供。需要建议。

- §3.2 P-D 链式核验：state_0 = `7d6d3d39fad8`，ext_1 = `f7b11d1e6988`，merkle_root = `7bf52bea023a`，b3 root = `75596bbabdb8`。这些哈希未在附录 A 自验。需要建议：所有引用的哈希应纳入自验清单。

- §4.1 代数恒等式伪影：代码中 `transformed = [t ** nu for t in T_frac60]` 和 `eta_transformed = [t * eta for t in T_frac60]`，对全正向量，两个单调递增变换恒同序 → Spearman ≡ 1。这个分析正确。但需要指出：如果 nu 可以为负或 eta 为负，则不一定单调；但手稿说全正向量，且 nu, eta 可能正。需要确认。可能没问题。

- §4.2 v2 → v3：v2 仍仅用 9 model × 60 cells 单 backbone → Spearman 仍 ≡ 1（FAIL）。v3 worker C 改用 Mistral Large 2512 × 30 cells 跨 backbone，Spearman = 0.375（PASS，破同序）。这里“跨 backbone”可能指 30 cells 来自不同 backbone？需要澄清。手稿说“Mistral Large 2512 × 30 cells 跨 backbone”，但 Mistral 是单 backbone，如何跨 backbone？可能 worker C 是跨 backbone 的 30 cells？需要指出表述矛盾。§4.3 表 L=30 来源“worker C PASS 复用”，backbone 是 mistral-large-2512。所以“跨 backbone”可能指 30 cells 来自多个 backbone？但表说 backbone 是 mistral-large-2512。需要澄清。

- §4.3 表 L=45 来源“新跑（15 GSM8K + 15 baseline SQA + 15 new SQA）”，L=100 来源“新跑（15 GSM8K + 15 baseline SQA + 70 new SQA）”。需要说明这些数据集是否预注册？可能没问题。

- §4.4 开源 3 backbone 表：glm53 β median -0.009206, CI [-0.026170, 0.008007]；mistral β median -0.015788, CI [-0.031481, -0.003311]；qwen3 β median -0.018441, CI [-0.036910, 0.000110]。三对 CI 全部重叠。但注意 mistral CI 不包含 0，qwen3 CI 包含 0，glm53 CI 包含 0。CI 重叠但 mistral 与 qwen3 可能差异？需要指出：CI 重叠不代表无差异；且 mistral 的 CI 不包含 0，说明其 β 显著不为 0（如果 CI 是 95%），但 qwen3 不显著。这本身可能表明实现间存在差异。需要建议使用差异 CI。

- 闭源 3 backbone 表：gpt-5.6-sol CI [-0.027453, 0.006577] 包含 0；claude-sonnet-5 CI [-0.039812, -0.001869] 不包含 0；gemini-3.7-flash CI [-0.030946, -0.002754] 不包含 0。三对 CI 全部重叠。同样问题。

- §4.4 “加速器降级欺诈验证：3 个 backbone 的 response.model == request.model，per-cell downgrade 出现 0 次（FALSE）。”这个与统计无关，但可以。

- §4.4 OR embedding 4 项：P2 β CI overlap 1/6 GRAY（symbol-split by architecture）。需要说明 1/6 是如何计算的：4 个 embedding 两两比较有 6 对，只有 1 对重叠？需要明确。手稿说“1/6 GRAY”，可能指 6 对中 1 对重叠？但 GRAY 通常指不确定。需要建议明确。

- §4.4 豆包 5 embedding：structural finding —— endpoint-internal 收敛、跨 endpoint 离散。这个没有统计细节。需要建议报告具体指标。

- §5.2 退化预检族：P-J convergence_rates 9 model 全 0.1 常量（var=0）→ UNVERIFIED（Spearman -0.9667 对常量向量无定义）。这里 Spearman -0.9667 对常量向量无定义，但手稿说“Spearman −0.9667 对常量向量无定义”，这矛盾：如果无定义，怎么有 -0.9667？需要指出。可能 Spearman 是在其他向量上计算的？需要澄清。

- §5.2 P-M 攻击面：detection_rate 10/10 全 0.0，safety_index = SECURE（矛盾）→ UNVERIFIED。这个可以。

- §5.2 P-C exp_3_3 eta 扫描：r2_per_eta 对 9 model 逐字相同（9/9 列表相等）→ UNVERIFIED。这个可以。

- §5.3 Adendum H：median=5.444, IQR=1.581, mean=4.897, std=2.028（CV>0.4，不稳健）；剔除 2 个 canonical 边界后 7 model std=0.629，仍 GRAY。需要指出：剔除标准是否预注册？如果事后剔除，可能引入偏差。需要建议说明。

- §5.3 Adendum P：P-C two_phase = FAIL_H0（幂律死）与 P-L v3 P1 尺寸标度 R² 是数学前件关系。若 P-L v3 P1 log-log R² < 0.9，应判为与 P-C two_phase 一致的幂律死，而非“P-L 实验失败”。这里“数学前件关系”需要审：P-C 幂律前件是“存在幂律标度”，P-L data collapse 的前件是“存在幂律标度”。如果 P-C 幂律死，那么 P-L 的 data collapse 前件不成立，因此 P-L 不应判为“实验失败”，而应判为“前件不成立”。这个逻辑可以，但需要明确：P1 的 FAIL 是“未达阈值”，不是“幂律死”的证明。手稿说“两个独立通道指向同一无幂律结论”，但 P1 n=3 统计力不足，不能作为强证据。需要建议降格。

- §6 限制：六项限制。需要检查是否充分披露统计力不足：§6(4) 提到 Phase 1 尺寸标度 FAIL，R²=0.7447<0.9，且三点拟合 n=3、p=0.337，统计力不足。已在 §4.3 披露三点不确定性。但摘要和结论未提统计力不足。需要建议在摘要/结论加限定。

- §6.7 push README 必列 4 件：P-F D_fix2 FAIL_EXPOSURE_PARTIAL、P-K OVERALL FAIL、by_model schema 互异、GLM_1 stale ref。这些与统计无关。

- 附录 C 引用规范：GLM §5 复现前提 seed=42，12×2 超平面，proj>0，hex zfill(3)，阈值 Hamming < 6/12。这些是复现前提，但未说明与统计判定关系。

- 附录 D 7 铁律：0 LLM API 调用等。与统计无关。

需要输出格式：总体判断 + 统计正确性问题表格 + 方法论问题表格 + 数字核对结果 + 必改项汇总 + 其他意见。

需要决定总体判断：MAJOR_REVISION 还是 REJECT？手稿有严重统计问题：P1 n=3 统计力不足仍下强结论；P3 Q 定义缺失；P2 CI overlap 方法不当；数字不一致（18 frozen anchors 16+5=21；8 件自验）；P-K 双口径矛盾。这些是重大方法论问题，但可能可通过修改解决。选择 MAJOR_REVISION 比较合适，因为不是完全不可救药，但需要大幅修改统计表述和方法。如果审稿严格，可能 REJECT？但用户要求审稿，我们应给出 MAJOR_REVISION 并说明理由。

需要确保所有问题具体位置与可执行改法。

现在构建回答。

需要严格遵守输出格式。使用中文。

总体判断：MAJOR_REVISION。理由：统计推断与判定阈值存在多处未预注册/未定义/过度解释，且存在数字不一致，需大幅修订后才能支持结论。

统计正确性问题表格：编号 | 严重度 | 位置 | 问题 | 具体修改建议。

需要列出主要问题：

1. P1 n=3 统计力不足，FAIL 结论过强。严重度：阻断。位置：摘要、§4.3、§4.5、§7。问题：三点拟合 n=3，p=0.337，R²=0.7447 不能支撑“尺寸标度不成立”的强否定；p 值在 n=3 时不可靠。建议：将“FAIL”限定为“未达预注册阈值，不足以支持尺寸标度”；在摘要/结论加“统计力不足，不能排除尺寸标度”；报告斜率 95% CI 或贝叶斯后验；明确 p 值含义。

2. P3 Q 定义与阈值依据缺失。严重度：阻断。位置：§4.3、§4.5、摘要。问题：Q 的计算式、归一化方式、阈值来源未给出；无法判断 0.1929 是否合理。建议：在方法部分给出 Q 公式，说明阈值是否预注册；若未预注册，不能作为判死线，应降级为探索性。

3. P2 CI overlap 判定“实现稳健”统计上不成立。严重度：重要。位置：§4.4、§4.5、摘要、结论。问题：CI 重叠不等于无显著差异；可能漏掉实际差异；未进行多重比较；β 为 cell-level 代理斜率，摘要/结论未充分披露。建议：改用两两差异的 bootstrap CI 是否包含 0，或等价检验；报告多重比较校正；在摘要/结论加“β 为 cell-level 代理斜率，非 size scaling exponent”。

4. P-K 双口径矛盾。严重度：重要。位置：摘要、§5.1、§6(2)、§6.7。问题：预注册阈值 1%，FPR 4.44% 机器判定 OVERALL FAIL，但 paper 处置 GRAY，违反预注册；摘要未提判定。建议：主判定维持 OVERALL FAIL，GRAY 仅作为证据质量标签；摘要明确“P-K 机器判定 OVERALL FAIL（paper 处置 GRAY）”。

5. SHA-12 48-bit 碰撞风险未声明。严重度：重要。位置：附录 A、§1、§2。问题：48-bit 哈希碰撞风险较高，不能作为防篡改证据。建议：报告完整 SHA-256 或至少 64-bit；声明 48-bit 仅作便捷标识，碰撞风险约 2^24 次生日攻击。

6. 60 cells 复现率 85.0% 未报告置信区间。严重度：建议。位置：摘要、§3.1、§7。问题：51/60 的 95% CI 约 73.4%-92.5%，未报告。建议：报告 Wilson CI 或 Clopper-Pearson CI。

7. 22/22 PASS 未报告置信区间。严重度：建议。位置：§3.2、摘要。问题：22/22 的 95% CI 约 84.6%-100%，样本量小。建议：报告二项分布 CI。

8. 0.867 均衡带“精确重合”过度解释。严重度：建议。位置：§3.1。问题：两个模型 accuracy 26/30 相同可能是巧合，未报告 CI。建议：报告 accuracy 的 CI，降格为观察性。

9. P-C 幂律前件 R²=0.1986/0.2670 双 FAIL_H0 的阈值依据？可能预注册？需要检查。手稿未说明阈值。建议：说明阈值来源。

10. Adendum H 剔除 2 个边界是否预注册？建议：说明剔除标准预注册，否则作为敏感性分析。

方法论问题表格：

1. 三态分离框架“部分拒绝”表述可能误读。严重度：重要。位置：摘要、§4.5、§7。问题：P1/P3 是 data collapse 核心，P2 是独立稳健性命题；“部分拒绝”可能让人误以为 data collapse 部分成立。建议：改为“P-L data collapse 主张在预注册阈值下被拒绝（P1/P3 FAIL）；跨实现稳健性作为独立命题 PASS，不构成对 data collapse 的支持”。

2. 判死线 SPEC 预注册可验证性不足。严重度：重要。位置：§1、§2。问题：仅公布 SHA-12 前 12 位锚，未公开 SPEC 内容，无法验证预注册。建议：公开完整 SPEC 或承诺文件，或至少提供可验证的哈希与内容。

3. 退化预检族是否预注册未说明。严重度：重要。位置：§5.2。问题：4 类不变性预检若为事后发现，不能作为 UNVERIFIED 判定依据。建议：明确预检是否在数据冻结前预注册；若否，降级为探索性发现。

4. β 为 cell-level 代理斜率，但 outcome 类型未说明。严重度：建议。位置：§4.4。问题：若 outcome 为二值 pass/fail，线性回归斜率不合适。建议：说明 score 定义；若二值，改用 logistic 回归或概率斜率。

5. 18 frozen anchors 数字不一致（16+5=21）。严重度：阻断。位置：§2、附录 A。问题：16+5=21，但称为 18 frozen anchors。建议：统一为 21 anchors，或说明 18 为旧称。

6. 附录 A “8 件自验”与所列内容不一致。严重度：重要。位置：附录 A。问题：列出 5 制品 + 21 锚 + schema v1 + 4 plugin spec = 31 件，但称 8 件。建议：明确“8 件”指 8 类，或改为实际件数。

7. 哈希引用未全部纳入自验。严重度：建议。位置：§3.2、§5.5。问题：state_0、ext_1、merkle_root、b3 root、锚链 c4cae1ed9ee5 未在附录 A 自验。建议：将所有引用哈希纳入自验清单。

8. P2 降格未完全落位。严重度：重要。位置：摘要、§4.4、结论。问题：摘要/结论仍称“6/6 全重叠 PASS”，未提 OR 1/6 GRAY 或 3/5 降格。建议：统一表述，明确主判定与附加检查。

数字核对结果：

- 85.0%：落位正确（摘要、§3.1、§7）。无残留 87.0%。但未报告 CI。
- Adendum 17：落位正确（摘要、§5、§5.1、§7）。合计 11+2+1+2+1=17 正确。
- P2 降格：未完全落位。摘要和结论仍使用“6/6 全重叠 PASS”，未提 OR 1/6 GRAY 或 3/5 降格；§4.4 降格说明与总判定存在矛盾。
- P-K 双口径：部分落位。§6(2) 和 §6.7 有双口径，但摘要未提判定，结论未提 P-K；需统一。
- 新发现不一致：18 frozen anchors 16+5=21；附录 A “8 件自验”与内容不符；§4.2 “Mistral Large 2512 × 30 cells 跨 backbone”表述矛盾（单 backbone 如何跨 backbone）；§5.2 P-J “Spearman −0.9667 对常量向量无定义”自相矛盾。

必改项汇总：列出阻断/重要项。

其他意见：

---

## tech_B2_grok46（or:x-ai/grok-4.6 → served: x-ai/grok-4.6）

- 状态：OK　报告 SHA-12：`16fa8b4ad016`

## 总体判断
MAJOR_REVISION — 预登记判死可以保留，但当前对 P-L 的「部分拒绝」在统计上过证：P1/P3 是同一三点拟合的两次贴标，n=3 且 L 与题目难度混杂，无法支撑「尺寸标度不成立」；P2 用 CI 重叠当稳健性、估元还不是标度指数，且 6/6 PASS 与必改降格互相打架。

## 统计正确性问题
| 编号 | 严重度 | 位置 | 问题 | 具体修改建议 |
|---|---|---|---|---|
| S1 | 阻断 | §4.3、§4.5、摘要、§7 | n=3、df=1 的 log-log：R²=0.7447、p=0.337。p=0.337 表示斜率与 0 不可分；R²<0.9 只能说「未达到预登记过线」，不能说「尺寸标度不成立」。三点必过原点附近的几何约束极强，FAIL 几乎是设计内建。缺斜率 SE/CI。 | 主结论改为 **INCONCLUSIVE / 未过预登记线**，禁止「不成立」。补：斜率 95% CI、df、预登记功效（在 n=3、α 等价于 R²≥0.9 时功效接近 0，除非近共线）。把「R²<0.9 ⇒ 拒绝幂律」从科学推断降为「未满足预先写死的过线规则」。 |
| S2 | 阻断 | §4.3 表 + 不确定性 (b) | L 不是系统尺寸，是 **题量**，且 L=45/100 掺入 new SQA。acc：0.8000→0.5111→0.4600，后两点贴 yes/no 随机基线 0.5。观测到的「负斜率」可完全由难度漂移+地板效应产生，与 FSS/data collapse 无关。L=60 还是 9-model 聚合，与另三行不可比，却同表。 | 表拆成「可比 Mistral 三档」vs「L=60 仅参考」。P1 主文写明：**本实验不能识别 size scaling**。若仍报拟合，必须先做 item-exchangeability 检验（按题源分层 acc、bootstrap 固定题池重估）。未排除混杂前，P1 不得进入「部分拒绝」的分子。 |
| S3 | 阻断 | §4.3 P3、§4.5 | Q=0.1929 **无定义、无公式、无样本计算**。阈值 0.05/0.15 无文献、无校准、无模拟。主曲线 `O(L)=2.9243·L^(−0.4140)` 就是 P1 同一拟合；Q 若是该拟合的归一化残差，则 **P3 与 P1 统计不独立**，三态表把一次失败数两遍。 | 正文给出 Q 的显式公式（对哪些点、何种归一、是否留一法）。若 Q 派生自同一三点拟合：合并为一条「三点幂律拟合未过线」，删 P3 独立 FAIL，或改用 **预留点/独立 backbone** 的塌缩残差。阈值必须有来源：引用、或预登记模拟分位数；否则改为连续报告 Q，不切三档。 |
| S4 | 阻断 | §4.4、§4.5、摘要、§7 vs §4.4「数字降格」 | 「两两 95% CI 全重叠 ⇒ P2 PASS」不成立：(i) CI 重叠 ≠ 无差异（重叠仍可显著）；(ii) 宽 CI 使重叠几乎必然，准则偏向 PASS（II 型错误膨胀）；(iii) 三开源 CI 均含 0 或贴 0，更像 **β 全无信号**，不是同指数稳健；(iv) 开源 n_boot=1000、闭源 2000，精度不对等还做跨组「全重叠」。正确的「相近」应用等价检验（TOST/ROPE），不是 overlap。 | 停用 overlap-PASS。改报：各 β 的点估计+CI、两两差值 CI、相对 ROPE 的等价检验。若 ROPE 未预登记，降为描述性「区间相交」，**禁止 PASS**。统一 bootstrap 次数。摘要/§7 与降格框必须同一套计数，见 D3。 |
| S5 | 重要 | §4.4 降格框、§6(5) vs 摘要/§4.5 | β= per-cell score～cell_index 的斜率，**不是** ν 或 size-scaling exponent。cell_index 若只是题序，β 的科学含义近乎任意。用它当 data collapse 的「实现稳健性」是估元偷换。降格写了，标题判定没改。 | 全程改名 `β_cell-index`，与标度指数脱钩。P2 移出 P-L 三态，改为「跨模型 cell-index 斜率的描述性重叠」。摘要不得把 P2 PASS 写成对 data collapse 的部分支持。 |
| S6 | 重要 | §6(2)、Adendum O、§5.4 挂点3 | 「GLM 自己的 JSON 有 2/45 被判为自家，FPR=4.44%」：字面是 **TPR/灵敏度**，不是 FPR。FPR 需分母=非 GLM 条目、分子=误判为自家。另：相对 1% 线，n=45、观测 2 次，若真 FPR=1%，P(X≥2)≈0.08，超线本身不稳定。4.4% 与 4.44% 混用。 | 用 2×2 表重写：TP/FP/FN/TN，FPR=FP/(FP+TN)，TPR=TP/(TP+FN)，Clopper-Pearson 区间。预登记 1% 线的机器判定可保留 FAIL；同时报告「相对 1% 的二项不确定性」。全文统一 2/45=4.44%（或 4.4% 并声明舍入）。 |
| S7 | 重要 | §3.1 0.867 均衡带；Adendum K | 26/30=0.8667 被写成「精确重合」「跨实现稳定性正面证据」。二项下多模型打到同一整数并不稀有；无检验（是否高于独立二项的重合率）。K 对该聚类是 FAIL_NO_MODEL，与正面证据并列。 | 删「精确/稳定性证据」。改为「两模型同为 26/30，描述性」。若要推断，给出 9 模型 acc 的多重比较或置换检验。K 未闭合前不要在 §3 当正面结果。 |
| S8 | 重要 | §3.1 账本轧平 | 「540 cells、9/9 残差为 0」若 A≡1−T−R（或三通道由归一化定义），则 T+R+A=1 是 **恒等式**，与 P-L v1 的 Spearman≡1 同类伪影，不能当实证结果。 | 声明通道是否线性约束。若是定义：改写为「会计闭合，非检验」。若独立测量：给出测量误差、轧平算法、最大残差的数值分布，而不是「全为 0」。 |
| S9 | 建议 | §4.3 辅助 Spearman | L=30：ρ=0.375、p=0.0412，相对 ρ=0 勉强显著，相对预登记 0.95 则远不够。v3 worker C 把 0.375 标 PASS（只说明伪影打破）。同一数字两套阈值。 | 分两行：①反伪影烟雾测试（ρ≢1）通过；②标度相关（ρ≥0.95）未通过。禁止一个 PASS 覆盖两种假设。 |
| S10 | 建议 | 附录 A SHA-12 | 12 hex=48 bit。21 个锚的偶然碰撞可忽略（~21²/2⁴⁹）。第二原像约 2⁴⁸，对有资源对手不够作完整性保证；截断也不可抗前缀碰撞工程。 | 正文/附录改登 **完整 SHA-256**；SHA-12 仅作引用缩写，并加一句：截断指纹不作抗碰撞安全声明。 |

## 方法论问题
| 编号 | 严重度 | 位置 | 问题 | 具体修改建议 |
|---|---|---|---|---|
| M1 | 阻断 | §4.5、摘要、§7「部分拒绝」 | 三态不自洽：P1/P3 同拟合；P2 换估元。Data collapse 的拒绝域是「标度变量下主曲线残差」，不是「跨模型某代理斜率重叠」。读者会读成「塌缩假说被证伪一半」。框架自述「只测 P2 会误判稳健」恰好说明 P2 本就不是该假说的态。 | 改表述为：**对 data collapse 主命题（尺寸标度+主曲线塌缩）未能证实，且设计无法有力证伪；另测的跨实现代理斜率呈区间重叠，不构成对该假说的部分接受。** 「部分拒绝」改为「主命题未过线 + 旁路描述性结果」，或定义清楚拒绝的是哪条合取支。 |
| M2 | 阻断 | §4.1–4.3 相对 FSS 语义 | v1 把 9 个 backbone 当 9 个尺寸（语义错位，稿内已承认）。v3 把 **评测题数 L** 当有限尺寸。FSS 的 L 是系统线性尺度/参数量/计算量，不是 test-set 基数。i.i.d. 题下 acc 应与 n 无关。这不是诚实降级后的合法 FSS，是第二次错位。 | 在 §4 开篇写死：本轮 **没有** 实现模型宽度/深度/数据量/compute 的尺寸轴。P1 最多是「acc 对题量的回归（含难度混杂）」。撤回对「P-L data collapse 假设」的直接判决，或把判死对象改写为「用题量冒充 L 的那条操作化」，不要写成对标度塌缩科学主张的判决。 |
| M3 | 重要 | §6(2)、§6.7、Adendum 表、摘要 | 双口径：机器 OVERALL FAIL vs paper GRAY。预登记线不调阈值，却在论文层改 verdict 标签，等价于改决策规则。摘要只报 4.44% 不报 FAIL。README 强制 FAIL、正文 GRAY，外部读者看到三套话。 | 固定一层：预登记判定=FAIL，全文一致。GRAY 只能作为 **讨论**：「n=45 时相对 1% 线的证据弱」，不得进入 Adendum 主表覆盖 FAIL。摘要写「预登记 FAIL（2/45，FPR 口径见 §x）」。 |
| M4 | 重要 | §4.4 OR embedding 1/6 vs 总判 PASS | 4 个 embedding、C(4,2)=6 对，仅 1/6 overlap（若字面）是 **不稳健** 证据。闭源 3 + 开源 3 过线就总判 PASS，embedding 放 GRAY/§7.2。这是选择性聚合。降格「3/5」「1 OR×OR 失败」与 6/6、1/6 计数互不相等。 | 预登记「P2 的分析单元是什么」：LLM backbone 还是含 embedding。分条报告，**禁止** 用通过的子集定义总 PASS。计数公式写进表注：backbone 数、对数、overlap 对数。 |
| M5 | 重要 | §5.2 vs 摘要 vs §6 补充 | 退化预检：摘要「四处真 bug」；§5.2「3 项真 bug」+P-I「部分」；§6「4 项…（P-J/P-M/P-C exp_3_3）」名单 3 个。UNVERIFIED 总项还把 4 子检查打成 Adendum A 一条，PASS 通道被「禁止产 PASS」事后规则约束——若该规则非预登记，则是对阈值/裁定的回溯。 | 一张表：4 子项×（预检是否失败）×（是否预登记一票否决）。真 bug 计数锁死为 3 或 4，摘要跟表。若「失败即 UNVERIFIED」是本轮新加，标为 **探索性规则**，不要写成已冻结判死纪律。 |
| M6 | 重要 | §5.3 Adendum P | 「P-C 幂律死 是 P-L P1 的数学前件，故 P1 R²<0.9 应判为与 P-C 一致的幂律死，而非实验失败」——前件关系需要 **同一可观测量、同一生成模型**。P-C 是含环图残余 r～循环维数 d；P-L 是 acc～题量。两条 FAIL 不能合成「两独立通道指向同一无幂律」的强证据。且 P-C 给出 R²=0.1986/0.2670，挂点3 写 KT-C1 R²=0.0007，不是同一统计量。 | 降为「两处都未拟合到幂律，可观测量不同，仅作并列负结果」。统一 R² 来源或删 0.0007。禁止「应判为幂律死而非实验失败」这种为 P1 洗白的推理。 |
| M7 | 重要 | §5.4 Adendum C 勘误 | 「annotation ≠ mutation，原值零改动」，但 SHA-12 已变（d64e8e…→6eba63…）。哈希变则字节变。与 0 触动、冻结账本叙事冲突。 | 三选一并写清：新文件 sidecar（旧 SHA 仍有效）；或承认 mutation 并给 diff；或只追加 erratum 记录、不改原 JSON。不得同时「零改动」与「新 SHA」。 |
| M8 | 建议 | §2「18 frozen」vs 附录 | 18=16+5 算术错（=21）；巡逻 22/22；schema 21/21。锚点计数是本「账本」论文的识别特征，错了会伤可信度。 | 定义一次：N_frozen、N_PG、N_plugin、是否含 schema。全文只使用这一组整数，附录表行数对得上。 |
| M9 | 建议 | §3.2 22/22 vs Adendum I 26/26 | caption 链 22/22、原口径 24/26、I 又 26/26。分母漂移未定义总体。 | 一张口径表：caption 数、dual_24bit 规则、PASS 分母。P-O 与 P-D 分列，不要在摘要只报 22/22 却在 §5 报 26/26 而不解释。 |

## 数字核对结果
- **85.0%（51/60）**：摘要、§3.1、§7 已统一；87.0% 已标为勘误。51/60=0.85 算术正确。未发现回潮。**落位合格。**
- **Adendum 17**：11+2+1+2+1=17，字母 A–Q 齐。摘要与 §5.1 一致。**落位合格。** 但真 bug 3/4/四处、I 的 26/26 vs P-D 22/22 是 **新的不一致**（见 M5、M9）。
- **P2 降格**：**未真正落位。** 降格框要求改为「3/5 overlap（1 OR×OR 失败）」；摘要仍「6 个独立 backbone 两两全部重叠 PASS」；§4.4 总判「6/6 PASS」；§4.5 表「6/6」；§7「6/6 全重叠 PASS」。3/5、6/6、OR 1/6 三套计数并存。**必改未执行，且引入新矛盾。**
- **P-K 双口径**：§6(2)、§6.7 有机器 FAIL / paper GRAY；Adendum O=GRAY；摘要只写 4.44% 不写判定；挂点3 写 4.4%。**部分落位，口径与百分数未收口。** 另疑 FPR/TPR 用词错误（S6）。
- **其他新不一致（统计相关）**：摘要「四处真 bug」vs §5.2「3 项」vs §6「4 项」名单 3 个；挂点3 R²=0.0007 vs §3.1 0.1986/0.2670；18 vs 16+5=21 vs 22/22。

## 必改项汇总
1. **撤回「尺寸标度不成立 / 部分拒绝 data collapse」作为科学结论。** 改为：预登记过线未满足；n=3、p=0.337、L–难度混杂 ⇒ 对幂律/塌缩既不能接受也不能有力拒绝。
2. **给出 Q 公式；若与 P1 同拟合则取消 P3 独立 FAIL。** 阈值无依据则改为连续量。
3. **P2：停止用 CI 重叠判 PASS；β 退出标度主张；执行已写的降格并消灭 6/6 vs 3/5 vs 1/6。**
4. **P-K：2×2 表定义 FPR；预登记 FAIL 不得在主表改 GRAY；4.44% 统一。**
5. **L 轴语义：写明不是 FSS 尺寸；P1 表删除或隔离 L=60 聚合行。**
6. **真 bug 计数、锚点个数、caption 22 vs 26、Adendum C 哈希「零改动」——四条账面对齐。**
7. **SHA 改登满哈希；SHA-12 仅缩写 + 碰撞能力声明。**

## 其他意见
预登记「挂死也是交付」与 0 回溯改阈值，作为程序是清楚的。问题不在「敢报 FAIL」，在把 **低功效、错估元、非独立的重复贴标** 写成对「标度塌缩主张」的实质判决。v1 代数伪影的揭露（§4.1）是稿中最有价值的方法学段落，应成为主线：先证明旧指标恒真，再说明新操作化仍不是 FSS。

统计上可保留的硬事实只有：(a) 预登记 R²≥0.9 在三点上未过；(b) 若干 backbone 的 `β_cell-index` 区间相交（描述性）；(c) 51/60、22/22 等账本计数（需定义）。把 (a)+(b) 绑成「部分拒绝」会在任何统计审稿下被打回。

功效一句可写进 §4.3：df=1 时 R²=0.7447 对应 |t|≈√(R²/(1−R²))≈1.71，双侧 p≈0.34，与文中 0.337 相符——数字内洽，但恰恰证明 **FAIL 不是对 H1 的检测，只是对一条极苛过线的未命中**。

---

## 【TRAE_FIXED_2026_09_18 元审注记】

**Trae code 走读发现（不改本报告原内容，仅追加披露）**:
1. 本报告为四份子审的**纯拼接**（各段加模型路由头 + SHA-12 + 状态），**无综合结论 / 无审稿日期 / 无审稿方署名**；
   作为"报告"结构不完整（对比 GLM v3 双审报告含综合裁定）。
2. 两份子审**不完整却标"状态：OK"**:
   - `review_content_A2_kimik3.md` 第 160 行句中截断（无 verdict）；
   - `review_tech_B1_dsv4pro.md` 为模型思维链原稿（开头"我们需要回答中文…"），结尾停在空的"其他意见："。
   四份中仅 `review_content_A1_glm51.md` 与 `review_tech_B2_grok46.md` 为成形评审。
3. 报告头 5 个 SHA-12 锚中，4 份子审的声称值为 **CRLF→LF 归一化哈希**（盘上文件为 CRLF，
   直接 `sha256sum` 复算将 MISS），报告未声明该归一化规则；同批 push manifest 则用原始字节哈希。
4. 目录/文件名标注 09_17，实际写入时间为 2026-09-18 00:35:54（跨零点）。

**有效结论保留**: 已成形的 A1/B2 两份子审质量高且口径收敛（均 MAJOR_REVISION，独立命中
P2 计数三套并存 / 18 frozen 算术错 / P-K 双口径 / Mistral L=60 计划有实测无 等论文硬伤），
评审发现真实可采信。

