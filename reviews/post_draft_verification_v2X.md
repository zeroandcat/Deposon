# Deposon v2.X 中文初稿 投稿前独立复核报告

- 复核对象：`paper/v2/deposon_paper_v2X.md`（539 行）
- 复核方式：只读复核；全部数字用 Python 对 `results/` 下冻结 JSON 逐字段复算；红线项 grep 级核查
- 复核日期：2026-08-30
- 复核范围：清单 A–F；未改动任何其他文件

---

## A. 数字追溯：**PASS**

逐项复算（脚本读取 JSON 实值，论文值 vs JSON 值）：

| 论文数字 | 行号 | JSON 实值 | 结果 |
|---|---|---|---|
| H-A1 p=0.0118，16+/4−/2 平 | L215–218, L434 | `corpus_eval…H_A1…p_exact=0.011818`，n_pos=16/n_neg=4/n_tie=2 | PASS |
| H_A_dead.triggered=true，反转 4 图 | L218, L433/435 | `kill_lines.H_A_dead.triggered=true`，reversals_vs_random 恰为 L_historical/L_physics/L_project_management/S2_n45（4 项） | PASS |
| H-A2 p=4.0e-5，19+/1−/2 平 | L221–222, L436 | `H_A2…p_exact=4.005e-05`，19/1/2 | PASS |
| S6 族 0.471 / 锚点 0.470588 | L223–224, L437 | `H_S6_anchor_reproduction.S6_named_hits3=0.470588`，matches anchor exactly | PASS |
| OLS β=+2.12 / p=0.00028 / n=20 | L21, L281–285, L438 | `v20_regression_field_v2.json` coefficient=2.1177, p=0.000279, n=20 | PASS |
| 先验 named Hits@3 0.484–1.000（四图逐值） | L22, L236–237, L439 | crossval `prior_arm_eval`：physics 0.4839 / biological 1.0 / algorithm 0.6897 / historical 0.7826；结构与物理臂均 ≤0.22 | PASS |
| CoT 92.5% | L317, L440 | `cot_quiz.overall_cot_accuracy=0.925` | PASS |
| −7.5pp / 三图各 −10pp / 场 −0.0pp | L260–261, L442 | `gt2_verdict.rule_collapse_mean_pp=0.075`；per_graph rule 0.1/0.0/0.1/0.1；field 全 0.0；verdict=no_separation | PASS |
| 题库轨 rule 27.5% / field 52.5% / prior 92.5% / random 25% | L266, L299, L443 | `quiz_eval.overall`={rule 0.275, field 0.525, prior 0.925, random 0.25} | PASS |
| 大题库 89.5/54.2/50.9/19.6 | L301–302, L454 | `bigquiz_eval.overall`：prior 0.8947 / tfidf 0.5417 / field 0.5091 / rule 0.1964 | PASS |
| GT-1 gap 0.30，20/20 | L348, L445 | `gt.json GT1`：gap=0.30，n_runs_below_meanfield=20/20，dirichlet 0.10 vs meanfield 0.40 | PASS |
| GT-5b 22/22 | L349, L446 | `gt5b.per_graph_summary` 22 图 meanfield_monotone_rate 全 =1.0；verdict=supports_narrowed_monotonicity | PASS |
| GT-6 中位 ≈1.6e-29（1.594e-29），3 例外 S4 0.148 / L_algorithm 0.136 / S5 0.121 | L353, L363–364, L447 | `gt6.verdict.median_residual_ratio=1.5938e-29`；per_graph mean：S4=0.1483、L_algorithm_process=0.1362、S5=0.1205；verdict=potential_game_explanation_complete | PASS |
| PoA median 1.5 / 族 S 13 图；族 L 0.5、0.75；3 张 ∞ | L350, L374–379, L449 | `gt.json GT4`：族 S 有限值恰 13 项、中位 1.5；L_historical=0.5、L_physics=0.75；S1/S2/S5=Infinity 单独计数；全 17 图中位 1.333（论文按 M4 用族 S 子集口径并已在修订记录披露） | PASS |
| GT-8 2/2 同向；对 A +0.7917>+0.1333、对 B +0.0526>−0.0833；degree 高 hub 饱和（diff 0.0 与 −0.9474） | L287–293, L450 | `gt8.verdict=supports_H_GT8`，pairs_concordant=2；diff 数值逐位一致；degree_named 两高 hub 图均 1.0，diff_fm_deg=0.0 / −0.9474 | PASS |
| GT-2B rule 0.150/0.275/0.200 inconclusive；场 0.375/0.525/1.000 | L269–276, L451 | `gt2b.verdict="inconclusive"`；per_T 聚合 rule_filter=0.15/0.275/0.20；field_mean=0.375/0.525/1.000（|Δ|max=0.625 吻合） | PASS |
| GT-3b doubao 4/4、deepseek 6/6、0 败绩、W=1.0 | L241–246, L452 | `gt3.json`：E3_doubao 在 6 域中 4 域 ok（另 2 域 fetch_failed，4/4 通过判据口径成立）；E4_deepseek 6/6 ok；`kendall_W=1.0`；verdict.H_GT3_supported=true | PASS |
| Wilcoxon p=0.0031 / |r|=0.83；配对 t p<0.0001 / d=2.05 | L206–207, L453 | statcheck_fm_vs_rand p=0.003052, r=0.8333；statcheck_fm_vs_deg p=2.13e-08, d=2.0478 | PASS |
| 方向一致率 ≥0.96（1.000 / 0.963），hub 反向 0 | L323–324, L455 | `direction_kind_summary`：abstract→specific 1.0、process→result 0.9627、total_hub_reversed=0 | PASS |
| evasion 100%（4/4 图） | L258, L444 | `gt2_attacker_meta.*.evasion_rate` 全 =1.0 | PASS |
| 先验开放 top-1 67.5% / top-3 82.5% / 2 选 1 期望 94.4% | L441 | results/ 下无独立 JSON 字段，出处为 corrections C2 文档——附录 A 已如实标注文档级（见 E） | PASS（已声明降级） |

A 项无一数字对不上。

## B. 禁用口径红线：**FAIL（1 处 Major）**

| 红线 | 结果 | 证据 |
|---|---|---|
| 不得出现「92.5% vs 92.5」对比（修订记录元行除外） | **FAIL** | L317–318：「直接 CoT 问答 92.5%（40 题子集），**与先验题库 92.5% 数值相等**」——正文仍出现两 92.5% 的并列等值陈述。虽同句即以 C2 撤回，但 outline 修订记录 M1 明确该对比已被禁用（「撤回『92.5% vs 92.5%』改 C2 可比口径」），正文残留等值表述。摘要（L23–24）与 L320–321 的可比口径写法合规 |
| 「实例级复现」Pigou 措辞 | PASS | 仅出现于否定式：L137「不主张『实例级复现』」、L379、L523「无实例级复现措辞」 |
| 势博弈不得写成已证明 | PASS | L29–31、L331–334、L527–528 均 consistency 口径；L333 明确「不声称证明了任何定理」 |
| H-A1 必须标判死 | PASS | L17、L61、L211 标题、L218、L392 全部标注判死 |
| PoA<1 两图必须并列披露 | PASS | L137–138、L350、L379–380 三处并列披露（0.5、0.75） |
| OLS 必须带「探索性」限定 | PASS | L22、L281 标题、L285、L403 |
| GT-3b 口径 =「跨厂商削弱、中文优化族残余局限」 | PASS | L397 逐字命中；L93–96、L241–246、L529 一致 |

## C. m6 裁定一致性（52.5% 口径）：**PASS**

全文 52.5% 仅出现于 §4.6/修订记录 M-1，统一按 C2「2 选 1 机会水平、不携带信息」解读（L299、L305–313、L512–517）。L304 与 L309 引用被否决的 skills 口径（「2×机会、部分迁移」）是作为裁定历史的被否决项呈现并随即驳回，不构成以另一口径作解读的残留；GT-2B 独立佐证（L310–311）方向一致。无残留的另一口径正文表述。

## D. 图语言纪律：**PASS**

全稿无任何英文图文件引用（grep `.png/.pdf/figure/Figure` 仅命中 1.X 引用说明 L6 与附录 D 文字）。附录 D（L470–479）5 张图全部标注「图待中文版制作」，且按 `paper/FIGURE_LANGUAGE_POLICY.md` 声明命名 `_cn` 后缀规则；修订记录第 10 条（L534）一致。

## E. 降级披露完整性：**PASS**

执笔助手自报 4 处降级均在文中如实声明：
1. 先验 top-1/top-3 与 94.4% 文档级出处——附录 A L441 标注 `docs/Findings_v2.0_corrections.md` C2，修订记录第 11 条（L535–536）显式声明「未在 results/ 独立文件中定位到」；
2. GT-7 corr −0.87 非 JSON 直出——附录 A L448 注明以 GT_RECONSTRUCTION §7 为叙事锚，修订记录 L537–539 声明「相关系数为文档汇总值」（抽查 gt7.json per_graph 确有 hits/Φ 走向数据）；
3. 5 图待制作——附录 D 全数标注；
4. PoA 族 S 子集口径——§5.4 L374–377 注明 13 张有限值图构成，修订记录 M-4（L522–526）披露全 17 图口径中位 1.333 及采用前者的纪律依据。

## F. 结构完整性：**FAIL（1 处 Major）**

- outline §3 证据映射表 8 行（§1–§7 + Appendix）在成稿中均有对应内容；Appendix 行要求的「攻击者标签样例」以 L259「以太假说」「原生生物界」内联给出；PASS。
- **kill list 未闭合**：`outline_v2X.md` L97「- [ ] 领域鉴定器 v0 新图复现（≥2 张）」仍为未勾选状态，但 GT-8 已完成且论文 §4.5 已写入 2/2 同向（supports_H_GT8）。对照同文件 L95–96 GT-3 项已勾选闭合的写法，本项应标闭合（或注明由 GT-8 闭合）。属文档同步遗漏，非数据问题。

---

## 发现的问题清单

### Major

1. **§4.7 残留「92.5% vs 92.5%」等值表述**（L317–318）。「与先验题库 92.5% 数值相等」正是 outline 修订记录 M1 禁用的对比。建议修法：删去等值陈述，直接写「CoT 题库 92.5%；按修正案 C2，『先验=CoT』宣称已正式撤回——先验题库口径因陷阱 −inf 退化为 2 选 1（期望 94.4% 完全解释观测 92.5%），可比口径为 CoT 92.5%（4 选 1）vs 先验开放 top-1 67.5% / top-3 82.5%」。
2. **kill list「领域鉴定器 v0 新图复现」未标闭合**（outline_v2X.md L97）。GT-8（2/2 同向，supports_H_GT8）已完成并入稿 §4.5，待办框仍为 `[ ]`。建议修法：勾选闭合并注明「由 GT-8 闭合（2026-08-30，deposon_v20_gt8.json）」。

### Minor

1. **附录 A L449 的 JSON 路径不精确**：`poa_per_graph_finite` 实际位于 `GT4_price_of_anarchy.verdict.poa_per_graph_finite`（顶层键为 `poa_per_graph`，含 "Infinity" 字符串项）。建议路径写全，避免读者按顶层键查找失败。
2. **L271 表述小歧义**：「三图各 −10pp」与 JSON 一致（0.1/0.0/0.1/0.1），但读者可能误读为四图中三图；建议补「（第四图 0pp）」。
3. **L318 的「94.4% 完全解释观测 92.5%」** 依赖文档级 C2 数字，建议在该句就近加「（文档级口径，见附录 A）」指引，与 E-1 降级声明呼应。
4. §5.2 表 ③（L350）PoA 行未注明 13 图为族 S 子集口径，读者须翻到 §5.4/修订记录才见口径构成；建议在表内加「（族 S 子集口径，见 §5.4）」。

## 总体结论

**有条件 PASS**。全部实验数字（A）与 JSON 冻结值逐位吻合，禁用口径除一处残留外全部合规，降级披露与图纪律完整。返工项（2 项 Major）：① 删除 §4.7 L317–318 的「92.5% 数值相等」等值表述；② 闭合 outline kill list「领域鉴定器 v0 新图复现」项。两项均为文字/文档级修改，不涉及数据。Minor 4 项建议一并处理后可投稿。
