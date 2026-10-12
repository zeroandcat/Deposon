# 独立复核：deposon_paper_v2X.md 结构标准化重构版（REVISION_LOG 第 18 条）

- 复核对象：`paper/v2/deposon_paper_v2X.md`（669 行，2026-08-30 结构标准化版）
- 复核方式：只读；对照 `results/` 冻结 JSON 抽查数字；全文交叉引用机器扫描
- 复核日期：2026-08-30

## 总体结论：PASS（无 Major；3 项 Minor，均为可随手修复的残留/归档瑕疵）

重构与 REVISION_LOG 第 18 条声明的映射逐节吻合，未发现断句、节号错位或数字漂移；语义口径（判死/inconclusive/mixed/consistency/观察性规律/[待核]）全部保留。

## 1. 结构契约符合度 — 通过

- **节级契约**：编号节 1–7 + References + Appendix（A–E）齐备；References 编号化 [1]–[59]。
- **Introduction 漏斗（7 段，逐段核对）**：P1 领域背景（L21，散射层/概念图/前序工作与重要性）✓；P2 子领域趋势（L23，同质性谱系 + 价值命题迁移）✓；P3 问题与缺口（L25，静态核验 vs 动力学标量，研究问题加粗）✓；P4 缺口实证证据（L27，三稿链条，吸收原 1.2）✓；P5 方案高层（L29，势博弈建模 + 三个可检验命题）✓；P6 贡献列表 5 条（L31–50）✓；P7 路线图（L52）✓。与日志声明的 P1–P7 功能一致。
- **Method 3.1–3.4 齐全**：3.1 核心形式化（含能量独行式）、3.2 关键机制（先验→排序映射）、3.3 设计（协议+图特征操作化）、3.4 实现细节（语料+预登记+统计）✓，与日志旧节对照表一致。
- **Conclusion 含 Limitations**：§7 总结段 + §7.1 Limitations（四条，与 §6 一致）+ 未来工作 ✓。

## 2. 可读性 — 通过

- 每节开头均有路标句（§1 L19、§2 L56、§3 L157、§4 L237、§5 L388、§6 L465、§7 L519）。
- 术语首现定义到位：PoA=无政府代价（L29）、homophily/heterophily（L23/L64）、consistency 口径（L37 提及、§5 开头定义）、hub_concentration/real_semantics（§3.3）。
- 段落长度适中，无超长段；数学式统一 $...$/$$...$$。
- **交叉引用一致性**：正文出现的全部「§x.y」（§2.3/§2.6/§3/§3.1/§3.4/§4.1–4.4/§5/§5.1–5.5/§6/§6.4/§7）与「表 1」「附录 A/E」均有对应目标；无指向已合并旧节（§4.5–4.7、原 §7）的残留引用。「E9.2」（L27、L249）指向前序 1.X 论文的实验编号，属外部引用，不算错引。

## 3. 数字与口径零漂移 — 通过（抽查 14 组，全部一致）

| # | 正文数字 | 冻结 JSON 核验 | 结果 |
|---|---|---|---|
| 1 | H-A1 判死、16+/4−/2 平、p=0.0118、反转 4 图名单 | corpus_eval `H_A_dead.triggered=true`、`p_exact=0.01182`、反转名单逐字一致 | ✓ |
| 2 | H-A2 19+/1−/2 平、p=4.0e-5 | 同上 `H_A2` `p_exact=4.005e-05` | ✓ |
| 3 | S6 0.471 / 锚点 0.470588 / 0.8 阈值记不支持 | 同上 `H_S6_anchor_reproduction`（supported=false，matches anchor exactly） | ✓ |
| 4 | OLS β=2.12 p=0.00028、R²=0.628、调整 0.559、real_semantics −0.16 p=0.012、density p=0.13、n=20 | regression_field_v2 逐字段（2.1177/0.000279/0.628226/0.558519/−0.1618/0.0122/0.1318/20） | ✓ |
| 5 | 先验四图 1.000/0.783/0.690/0.484 | crossval `prior_arm_eval`（1.0/0.7826/0.6897/0.4839） | ✓ |
| 6 | 方向一致率 1.000/0.963、hub 反向 0 | crossval `direction_kind_summary` | ✓ |
| 7 | GT-2 no_separation、rule −7.5pp | crossval `gt2_verdict`（0.075） | ✓ |
| 8 | 题库轨 92.5/52.5/27.5/25%；大题库 89.5/54.2/50.9/19.6% | quiz_eval / bigquiz_eval `overall` 全对 | ✓ |
| 9 | GT-5b 22/22 单调率 100% | gt5b `per_graph_summary` 22 图全 1.0 | ✓ |
| 10 | GT-6 残余中位 1.6e-29、例外 0.148/0.136/0.121 | gt6 `median_residual_ratio=1.594e-29`、`per_graph_summary.*.residual_ratio_mean` 三值全对 | ✓ |
| 11 | PoA median 1.333（全 17 有限值）、1.5（族 S 13）、∞×3、族 L 0.5/0.75 | gt.json `GT4`（median_poa=1.3333、n_poa_inf=3、族 S 中位 1.5、L_historical 0.5、L_physics 0.75） | ✓ |
| 12 | GT-1 gap 0.30、20/20、0.10 vs 0.40 | gt.json `GT1` 逐字段 | ✓ |
| 13 | Wilcoxon p=0.0031、\|r\|=0.83；配对 t p<0.0001、d=2.05 | statcheck 两 JSON（0.003052/r=0.8333；2.13e-08/d=2.0478） | ✓ |
| 14 | GT-8b inconclusive、0.7805 vs 0.0732/0.0244/0.0488、+0.7073 | gt8b `gt8b_verdict`/`per_domain` 全对 | ✓ |

- 判死（H-A1、H-B1 动态斩杀线）、inconclusive（GT-2B、GT-8b）、mixed（GT-7）、no_separation（GT-2）、consistency 口径（§5 开头不放松声明）、观察性规律 v0（§4.4）、[待核] 标注（[21] 年份、[52]–[59] 条目）语义全部未变。
- References 59 条编号与正文 [n] 抽查 10 处（[1][3][11][27][30][34][35][42][49][51]）均有对应条目 ✓。

## Minor 清单（3 项，不阻断）

1. **残留旧式引用「crossval §三」**（§4.3，L295）：GT-2 段括注「主留一协议，crossval §三」是重构前的旧小节编号残留，不符合本稿「§x.y」交叉引用规范且无对应目标。建议改为「见附录 A no_separation 行」或删除括注（正文同段已给出完整出处 JSON 名）。这是本次重构唯一引入/遗留的引用瑕疵。
2. **孤儿参考文献 [12]、[13]**：[12] Christodoulou et al. 2014 与 [13] Benita 2020（分布级 PoA 先例）仅出现在 References 列表，正文从未引用；其余 [1]–[59] 均在正文出现。§5.4 讨论 Pigou 4/3 与分布级 PoA 口径处恰是补引 [13]（以及 [12]）的自然位置，建议在该处补 [12][13] 或从列表移除。
3. **GT-5 终点反转 S6 gap=−0.31 追溯断档**（§5.3 L422）：该数字在附录 A 无条目，且 `results/` 下无 `deposon_v20_gt5.json`（仅 gt5b）。GT-5 属「不回溯改写」保留在案的历史结果，建议附录 A 增一行说明其出处（SPEC_GT5/Findings 文档）或显式标注「文档级」。注意 GT-7 corr −0.87 已在附录 A 如实标注为文档汇总值，处理方式可对齐。

## 备注（非问题）

- GT-6 例外三图（S4/L_algorithm_process/S5）正文数值取自 `residual_ratio_mean`（如 S5 mean=0.1205 而 median=0.0），附录 A 未注明取的是 mean 口径；因附录字段路径写「per_graph_summary」不含子键名，建议正式版补 `.residual_ratio_mean` 子键，避免复算者取 median 时产生 0.0 的误读。列为提示而非 Minor。
- 附录 A–E 与日志声明「一字不动」一致（A 表 25 行追溯、E 可复算 scipy 代码块与 §4.1 数字自洽：hypergeom.sf(3,22,15,4)=0.1866、sf(2,22,6,4)=0.0458，与正文 p=0.187/0.046 对应）。
