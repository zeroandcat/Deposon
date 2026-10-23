# 《Fiction That Feeds Back》全稿修正版 撰写说明（逐条 delta）

查理-论文主笔｜2026-09-16｜对应派单：群管理员 17:41。输入：鲍勃复核报告（D-1～D-6＋N1–N3，五项主裁决全 PASS）＋阿兰查新备忘（17:22）。交付：`shared/查理_第二作FTFB全稿修正版_2026-09-16.md`（10,006 词；正文 9,358 ≈14.4–17.0 页＋refs ≈3 页 ≈**17.4–20 页**）。基线：收口版（鲍勃复核对象，SHA-256 510e55d3e394…）。

## 1. 逐条处置矩阵（采纳✓／不采纳✗）
| 项 | 处置 | 落点与说明 |
|---|---|---|
| D-1（应修） | ✓ 采纳 | §7.1 E 段括注补挂 `results/deposon_v21_gtformal.json · verdict.T_P1b.min_cosine`（同时覆盖 P1a 实测字段 `P1a_deviation.max_dev_inf`）。**本轮唯一 §7 改动**（差分断言：§7 仅此 1 行变化） |
| D-2 | ✗ 维持 | −1.0 与 handoff 字段文本逐字一致（handoff 即记 −1.0）；0.899 与冻结首作记录一致；取整明细在鲍勃对账表留档；不为加注触碰已验证节（纪律：§6–§7 除 D-1 零改动） |
| D-3 | ✗ 维持 | p=0.5/p=1.0 为 e95ci JSON mcnemar_b/c 的确定性推导，鲍勃已判「正文使用正确」；推导式留档报告对账表 |
| D-4 | ✓ 采纳 | §1.3 数字政策句补第三类："an experimental number cited by field path into the frozen record examined in §7" |
| D-5 | ✗ 传话戴夫 | §9.1 "(strong)" 括注与 §2.3 裸 Pass 的机械对应已由鲍勃核成立；改表标签=重复打分（违 T3）。排版期拆表时保 strong 依据可溯（§2.3 叙述段） |
| D-6 | ✓ 采纳 | §9.3 "unchanged from §1.2" → "in substance unchanged from §1.2" |
| N1 | ✗ 留档 | enumeration_scope 紧凑记法之辨已在鲍勃报告留档；正文读法自洽（v21 n_states=6760 支撑）；冻结件不改 |
| N2 | ✗ 维持 | "two-parameter" 沿已双审 PASS 口径；审稿追问预案＝GT_FORMALIZATION_v1.md 构造 B 行单纯形参数化 |
| N3 | ✗ 传话戴夫 | basename＋锚值已 repo 实测逐位命中；排版期统一路径风格时可顺带补 docs/ 前缀（代码层替换，非本轮） |

## 2. 阿兰补证并入（题录逐字转录）
| 项 | 处置 | 落点与说明 |
|---|---|---|
| R42 Gonçalves TATuP 2026 | ✓ 入池＋双挂引 | §1.3(iv) 定位语（对话对象非占位者：无四通道类型学、无判定机制→互补）；§9.2 对话句（同义收口） |
| R43 Bormashenko, Entropy 27(4):437, 2025 | ✓ 入池＋挂引 | §4.2 rematerialization 句：虚构量携可测代价回灌物理的当代收敛（综述侧） |
| R44 Hsieh, PRL 134:050404, 2025 | ✓ 入池＋挂引 | 同句（动力学化侧） |
| R45 Miščević, Thought Experiments, Springer, 2024 | ✓ 入池＋一句指针 | §3.1 末尾纯 see-pointer，零内容主张 |
| SciFi-Benchmark | ✗ 不并入 | 编号未稳；正文零出现（脚本断言）；§8 复查＝本轮字节级未动、全部事实句带挂引 |
| 主张句 | ✓ 零改动 | 摘要与 §1.2 逐字一致断言 ×2 PASS |

## 3. 联动与状态
- 池计数 41→45 三处联动：§1.3(ii)、References preamble、§9.2（上轮教训：双侧＋第三处同步，本轮一次到位）。
- 组头新增 "Pool R42–R45 (adjunct to §1, §3, §4, §9; added at second-round verification)"；R40/R41 组头不动。
- 旗标状态不变：R12 撤旗、R13/R14 PENDING（断言 PASS）；"Two entries, [R13] and [R14]" 句式未动。

## 4. 验证套件结果（脚本，修正版上全绿）
45/45 引用闭合零超池；refs=45 条；红线 token 全零；主张句 ×2；**§7 差分＝D-1 唯一 1 行**；§2/§5/§6/§8 字节级不变；§1/§3/§4/§9 差分逐行核对＝仅预期 delta（§1 加 2 行、§3 加 1 行、§4 加 1 行、§9 含 D-6＋计数＋对话句）；AI 披露字节级不变。

## 5. 移交
- 鲍勃：可只复核本 diff（修正说明 §1–§2 全列）；N1 冻结件留档事项无需行动。
- 戴夫：D-5（拆表保 strong 依据可溯）与 N3（docs/ 前缀统一）两项排版期待办；R42 如后续拿到 DOI 由阿兰补传后替换。
- 阿兰：R42–R45 已逐字转录；SciFi-Benchmark 待编号稳定后按 R10 流程再议。
