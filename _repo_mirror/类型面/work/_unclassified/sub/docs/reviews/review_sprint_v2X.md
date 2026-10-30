# 复审报告：修订记录第 20–22 条冲刺波（GT-8b 翻转 / 文献核实 / 五图接入）

- 复审对象：`paper/v2/deposon_paper_v2X.md`（733 行，2026-08-30 02:52）在
  `paper/v2/REVISION_LOG_v2X.md` 第 20–22 条下的全部改动，重点第 21、22 条。
- 复审方式：独立只读复核；数字逐字段对 `results/` 冻结 JSON；口径词全量 grep 计数；
  交叉核对 docs/REF_VERIFICATION_v2.md、docs/Findings_GT8B.md、docs/SPEC_GT8B.md、
  docs/FIGURES_v2.md、docs/MODEL_ARGUMENTATION_v2.md；图 5 目视核验 PNG。
- **结论：WARNING**——五项审查清单全部通过（数字、翻转纪律、强度档、文献、图披露、
  口径计数零缺陷），但存在 4 条可行动的 Minor（不改判据、不改数字，均为一致性/卫生类）。

## 逐项证据表

| # | 审查项 | 结论 | 证据 |
|---|---|---|---|
| 1 | GT-8b 翻转数字溯源 | ✅ PASS | 论文 §4.4（L369–381）、附录 A（L640–641）、附录 C（L660–662）全部数字与 `results/deposon_v20_gt8b.json` 逐字段一致：chemical llm_prior 0.6429 / field 0.1429 / random 0.0357 / degree 0.0000 / diff +0.5000（`per_domain.L_chemical_elements.named_summary`、`prior_named_minus_field_named=0.5`）；chinese 0.7805/0.0732/0.0244/0.0488/diff +0.7073；`gt8b_verdict.verdict="supports_H_GT8B"`、n_valid_domains=2、thresholds 0.6/0.2/min_domains=2；`cache_missing={}`。prompt_sha256 a1f01ba0…721a1f 与 Findings_GT8B §7 落盘值一致。 |
| 2 | 翻转纪律（不回溯改写） | ✅ PASS | 六处现行判定均为 supports_H_GT8B 且历史如实保留：§4.4「取数史如实归档不回溯改写：…初判 inconclusive…经修正案 B2 诊断…与 B3…补数转正」（L375–379）；§6.2 L491–492；§6.4 L519–521；§7.1 L545；附录 A L640/L641 双行。全文 13 处 inconclusive 逐一核查，涉 GT-8b 者全部带「初判」历史限定（L376/386/491/519/545/640/641），无一处把 inconclusive 当现行判定残留。docs/Findings_GT8B.md §7 翻转注记在案且 §1–§6 历史段未改写；docs/SPEC_GT8B.md B2/B3 修正案登记在案（max_tokens=32000 一次成功）。 |
| 3 | 强度档未拔高 | ✅ PASS | §4.4「样本仅 2 张新图，方向性证据，非效应量估计」（L380–381）、「仍为 2 图方向性证据」（L386）；§6.2「仍仅 2 张新图，方向性证据」；§7.1「方向性证据」；贡献 4 仍为「观察性规律…不作为已确立的判别器贡献」（L45–48）。docs/MODEL_ARGUMENTATION_v2.md #14 缺口行已更新但档位仍【仅有动机 + 方向性观察】（L399）。 |
| 4 | 文献核实落地 | ✅ PASS（1 处 Minor，见 M4） | `待核` 计数 19→0；[21] 已修正为 Nasr et al. "Tight Auditing of Differentially Private Machine Learning", USENIX Security 2023, pp. 1631–1648，正文 §2.6（L137–138）与文献表（L573）成对带核实注记，References 占位行（L551）同步更新——与 REF_VERIFICATION_v2.md CORRECTED 结论及消歧建议（选 Tight Auditing 而非 ICLR 2025 抽取文）一致。[52]–[59] 八条均带「（已核实 2026-08-30…）」，正文 8 处 + 文献表 8 处成对。抽查 3 条全部与 REF_VERIFICATION_v2.md 吻合：[52] McPherson 2001 VERIFIED（Annu. Rev. Sociol. 27:415–444）；[57] SEAL NeurIPS 2018 VERIFIED（pp. 5171–5181）；[21] CORRECTED。编号 [1]–[59] 连续无跳号、共 59 条（L553–611 逐号核）。 |
| 5 | 附录 D 五图 | ✅ PASS（2 处 Minor，见 M1/M2） | 5 条 `![](figures/figN_*.png)`（L675/684/693/700/712）全部指向存在文件（仓库根 `figures/` 下 5 个 PNG 均在，263–574KB）。「图待中文版制作」5→0。图 5 披露（L702–710）与 docs/FIGURES_v2.md（L72–81）逐项一致：冻结 20 图（17 有限值 + 3 ∞）、L_geography_world=3.0 与 L_project_management=0.2 按冻结公式现算、点纹区分且不计入中位数、S2_n45=0.5 红框如实呈现。底层数据复核：`deposon_v20_gt.json → GT4_price_of_anarchy.verdict` 含 17 有限值（median=1.3333 复算一致）、n_poa_inf=3、S2_n45=0.5 确在冻结集。目视核验 fig5 PNG：22 根条形、3 根斜纹 ∞（S7/S2/S5）、2 根点纹、3 个红框（含 S2_n45），与披露一致。 |
| 6 | 全文一致性（摘要/§5/§6.1） | ✅ PASS（1 处提示，见 M3） | 摘要（L13）不涉 GT-8b；§5 全节无 GT-8b 引用；§6.1 成立域表述与翻转无冲突；§4.4 段尾（L385–386）与 §6.2（L491–492）措辞互相咬合（同向/转正/方向性）。无矛盾。 |
| 7 | 语域抽检 | ✅ PASS | 新增段落（§4.4 GT-8b 段、§6.2、附录 D 引言）为陈述句、无 AI 腔、无过程语汇泄漏进主线叙事（「修正案」「归档」仅出现在 §4.4 取数史与 §6.4 工件节，属批准的内容性限定）。 |
| 8 | 口径词计数 | ✅ PASS | 实测：判死 9 / no_separation 7 / consistency 4 / 探索性 6 / 观察性规律 3 / inconclusive 13（14→13，与第 21 条自检一致）/ 待核 0（19→0）/ 图待中文版制作 0。全部与基线吻合。 |

## Minor 发现（不阻断，建议择机闭合）

- **M1（图链接基准路径）**：5 条图片链接为 `figures/figN_*.png`，仅在以仓库根为基准时解析；
  以论文文件位置（`paper/v2/`）为基准的 markdown 渲染器会解析到不存在的
  `paper/v2/figures/`。若后续走 PDF 构建或 GitHub 文件页预览，五图将断链。建议改
  `../../figures/…` 或在 `paper/v2/` 建软链，并记录在 FIGURE_LANGUAGE_POLICY。
- **M2（图命名违反仓库自有纪律）**：`paper/FIGURE_LANGUAGE_POLICY.md` 规则 5 要求新增图
  文件名带 `_cn`/`_en` 后缀；本轮五张中文图（fig1–fig5）均无后缀。政策规则 3 的历史豁免
  仅覆盖 `fig1_architecture.png`，不及新图。建议重命名加 `_cn` 并同步附录 D 引用。
- **M3（§5.4 与图 5 披露的并读缝隙）**：§5.4 正文只报告「族 L 2 张图 PoA<1（0.5、0.75）」，
  而附录 D 图 5 及其说明现在红框披露了第三张冻结图 S2_n45=0.5（族 S）。§5.4 不构成错
  误陈述（未主张排他），但与图 5 并读时读者会数出 3≠2。建议在 §5.4 该句加括注
  「族 S 另有 S2_n45=0.5，见附录 D 图 5」，一行即可闭合。
- **M4（[21] 作者序）**：文献表 [21] 写作「Nasr, M., Jagielski, M., Carlini, N., Tramèr, F.
  等」，而真实作者序为 Nasr, Hayes, Steinke, Balle, Tramèr, Jagielski, Carlini, Terzis
  （REF_VERIFICATION_v2.md 在案）——点名作者未按原序。带「等」可容忍，但 bib 落库时应
  按原序或只留首作者 + et al.。
- **M5（衍生稿漂移，提示性）**：`paper/v2/deposon_paper_v2X.converted.md`（Aug 29 21:15）
  是第 21/22 条之前的陈旧快照：仍以 inconclusive 为 GT-8b 现行判定（L374/489/516/540/
  635）、保留 19 处 [待核]、附录 D 仍是「图待中文版制作」。若该文件被任何构建/分发流程
  消费，将输出已废止口径。建议重新生成或删除。

## 复核边界

未复核项：fig1–fig4 的图内数据点逐项对账（仅核了 FIGURES_v2.md 的 56 项自检声明与文件
存在性；fig5 已目视+JSON 双核）；pytest 未重跑（本轮未动代码，与第 22 条自检一致）；
docs/REF_VERIFICATION_v2.md 的外部检索真实性按其落盘证据采信（3 条抽查内部一致）。

**一句话结论：第 20–22 条全部改动如实落地、数字与口径零缺陷，判 WARNING 仅因五处
Minor（图链接基准、图命名后缀、§5.4 与图 5 并读缝隙、[21] 作者序、converted.md 陈旧
快照），均不触碰判据与数字，可在一轮小修中闭合后转 PASS。**
