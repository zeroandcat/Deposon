# 鲍勃 · v1.1 论文新增数字独立补测复核（2026-09-27）

- **任务来源**：群管理员 2026-09-27 00:47:25 派发（阿兰《第三作合并输入资产清单》§三.5 待处置项：v1.0→v1.1 新增数字未覆盖于 09-26 两轮复核）
- **对象**：`shared/_v4_paper_final_2026_09_26_v1.1.md`（54,367 B／SHA-12 38BC2CF38D10）＋同名 .tex（58,828 B／58BD3F5BEF3A，交付件）；v1.0→v1.1 全量 diff（md 53 行/tex 36 行变更）先行枚举，新增数字无一遗漏
- **方法**：沿 09-26 23:06 方法——逐值定位仓内源件→字面提取→算术复算→与文内值比对；源件复制至 /tmp 工作副本实测（冻结工件零触动，全程只读）
- **中途口径输入**：用户 00:53「V3口径翻转忘传递（最重大＝PA pass 翻转）」+00:56「先自行在 GitHub 搜证，正式件明后天 minimax 出具」——搜证结果见 §4；**v1.1 全文 grep P-A 零命中**（实测），本轮复核对象不受该翻转影响

---

## 0. 结论速览

| 判定 | 数量 | 说明 |
|---|---|---|
| **吻合** | 9 项 | 49.3%→0／C-T15-1 与 500／t15_ext 裁决／180 公式／15 pairs／TH 双分母与 48/80 边缘态／GLM_2 中文原文／571 分解与 13 件中 2 件归档件／委托信 31,531+31,167+364 |
| **不吻合（结论层零影响）** | **2 项** | ①K-N26-2 五读变体范围上限 0.5844 → 实测 **0.5916**（drop_glm2 漏计）；②T1.5r2「60 calls」→ 实测新增 **62**（60 扩样＋2 补跑；判定件自报算式 4×10+11+11 的总和即 62，其「＝60」为算术笔误） |
| PA 假pass 证据初勘 | 7 条线索 | 构造层疑点已固化（§4），正式翻转待 minimax 件 |

两项不吻合**均源自判定件自身的汇总表述**（论文系忠实转写），且**均不推翻任何 verdict / kill-line 结论**（详见 §3 处置建议）。

---

## 1. 复核环境与源件指纹（/tmp/bob_v11_check/，均为仓内件只读副本）

| 源件 | 字节 | SHA-12 | 用途 |
|---|---|---|---|
| `results/_v4_supp_l14v3_n26_verdict.md` | 64,485 | f4435801d09f | N-26 判定件（五读敏感性） |
| `.tmp/_l14v3_sensitivity_v2.json` | 2,292 | dcaa4b6b3b0b | 五读敏感性原始数据（判定件 §0 登记件） |
| `results/_v4_supp_t1_verdict.md` | 27,538 | f1b5e49f3058 | T1 空响应 49.3% |
| `results/_v4_supp_t15_verdict.md` | 52,884 | 52c985429c91 | T1.5 工具侧修复＋§3.4 Plan A |
| `results/_v4_supp_t15r2_verdict.md` | 64,145 | 8355724a26e3 | T1.5r2 执行账 |
| `results/_v4_supp_prereg_v02_add_T15r2_2026_09_26.md` | 97,059 | 883dced872b4 | t15_ext 裁决登记（§0） |
| `results/_v4_supp_prereg_v02_add_T15r2_activation_2026_09_26.md` | 34,195 | f6ed61c25572 | 同上（activation 面） |
| `results/_v4_supp_t15r2_result.json` | 46,486 | c69ab0e3002e | T1.5r2 执行实测（records_summary） |
| `results/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` | 26,637 | ba4d07bd7000 | signoff（TH 表） |
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 239,387 | 849d76be3a06 | 勘误链 v19（E-35.1/E-34.4） |
| 上传件 `…__v4_commission_paper_final_glm_2026_09_24_v4.md` | 31,531 | d5337702cec9 | 委托信 v4（§2.8 裁决原文／§2.9 圈定面／自报字节） |

仓侧路径前缀 `_september_workspace/`（论文中 results/ 写法为 PI 本地面口径，映射已见于 09-26 22:25 报告）。仓库 HEAD a57d7fe，本轮 pull 无漂移。

---

## 2. 逐项复核表（v1.1 新增数字全量）

| # | 文内值（v1.1） | 实测值 | 源件字面 | 结论 |
|---|---|---|---|---|
| 1 | K-N26-2 robust across all five read variants **(range 0.4459 to 0.5844, all below 0.75)**（§7 正文＋附录 B 同值） | 五读 AUC＝{主读 0.5662720…，drop_coze 0.5843871…，**drop_glm2 0.5915773…**，drop_kimi 0.5346553…，drop_all3 0.4458677…}；范围＝0.4459–**0.5916**；全 5 值 < 0.75 ✓ | sensitivity JSON 五键逐一；判定件 §1.6 替代读法 2 自记「AUC = 0.5916」 | **不吻合**（范围上限漏计 drop_glm2；robustness 判定不受影响） |
| 2 | T1.5r2 "**measured execution: 60 calls** across the six cells, 10 to 11 per cell" | records_summary：n_t15r2_records＝**62**（n_t15r2_new_reask2_completed＝60＋n_t15r2_new_reruns_completed＝2）；分 cell 新增＝10/10/10/10/11/11；合并后每 cell 30 records、每教师每 cell 6 records→15 pairs | 判定件 §2.1 自报「实跑＝4 cells × 10 ＋ cell 2 × 11 ＋ cell 3 × 11 **＝ 60 calls**」（该算式总和实为 62） | **部分不吻合**（「10 to 11 per cell」✓；总数应为 62；裁决预算 +60 已足额执行 ✓） |
| 3 | T1 空响应 "**from 49.3 percent to 0**" | T1 判定件：n_empty_responses＝112（49.3% of total calls）；T1.5 判定件：n_empty_responses＝0（qwen3.7-max 非推理＋max_tokens＝500 修正后消除） | 两判定件 §1.4 字面 | **吻合** ✓ |
| 4 | "replaced the reasoning-model configuration with a non-reasoning one and raised the token budget to the recorded value of **500** (construction check **C-T15-1**)" | T1.5 判定件：非退化自证 C-T15-1＝qwen3.7-max 非推理模型＋max_tokens＝500 双修正；experiment_parameters 沿 500 | T1.5 §1.4＋t15r2 result JSON `max_tokens: 500` | **吻合** ✓ |
| 5 | "which the PI ruled on (**ruling t15_ext: 6 cells × +10 = +60 calls**)" | T1.5r2 prereg §0：派工单 2026-09-26 16:26 **t15_ext 拍板 `ask_57981c1bc81e03b9990a06e5`「+60 calls 规化重跑（N_min≥10 字面满足）」；总增量＝6 cells × +10＝+60 calls**（沿 T1.5 verdict §3.4 字面） | prereg/activation 双面字面 | **吻合** ✓ |
| 6 | "**recorded formula: 5 teachers × 2 prompts × 3 re-asks per cell × 6 cells = 180 calls, giving 15 pairs per teacher**" | T1.5 verdict §3.4 Plan A 与 t15r2 prereg §2.2 同式（5×2×3×6＝180，30 calls/cell）；实测每教师每 cell 6 records→n_pairs＝15（same 6＋cross 9） | 判定件/prereg 字面＋result JSON 实算 | **吻合** ✓ |
| 7 | TH-v2-3 "exceeded under **both measured denominators (68 and 72)** and is exactly met, at the 60.0 percent line, under the theoretical 80-event denominator (**48/80**)" | 勘误 E-35.1：D1＝48/72＝66.7%、48/80＝60.0% 理论边缘态（沿 ask_822b1e27 supersede）；E-34.4：48/68＝70.6%、D2 20/68＝29.4%；算术 66.7>60 ✓ 70.6>60 ✓ 48/80＝60.0% 恰达 ✓ | 勘误链 v19 两条目字面＋signoff TH 表 | **吻合** ✓ |
| 8 | §8.2 中文原文「**GLM_2 蒸馏实验失败 / 假证伪根因 / 不得外推**」 | 委托信 v4 §2.8（负向结论与判死不软化纪律）行 99 字面全等：「GLM_2 入论文 §4 负面章（PI 拍板）——GLM_2 蒸馏实验失败 / 假证伪根因 / 不得外推」 | 上传件实测（31,531/d5337702cec9） | **吻合** ✓（译文「phase reading」歧义声明系论文自加限定，合规） |
| 9 | §10.3 "a circled scoping face of **571** items (342 upload-listed, 200 released suspected, 16 coverage candidates, 13 strictly excluded); 342 plus 16, i.e. **358** items" | 委托信 §2.9.1/§3.4：圈定面 571 件＝342＋200＋16＋13，其中 358 件（342＋16）拟上传/覆盖；算术 342+200+16+13＝571 ✓ 342+16＝358 ✓ | 字面 | **吻合** ✓ |
| 10 | §10.3 "the **two archive-resident items** recorded as strictly excluded (among the 13; the second-work PDF is one of them)" | 委托信 §2.9.4：仓内 `_archive_2026_09_20/` 2 件严禁（FTFB PDF 在其中；本盘存在但不属上传面） | 字面 | **吻合** ✓ |
| 11 | 附录 A 新增 [L] 行：委托信 v4 **31,531／D5337702CEC9**；self-reported **31,167 B**；measured difference **+364 B** pending PI ruling | 上传件实测 31,531 B／d5337702cec9；信面 §Z 自报 31,167 B（§7 老实交代段避免自指 SHA 循环）；差 31,531−31,167＝364 ✓ | 实测＋信面 | **吻合** ✓ |

其余新增面（0.5617/0.5663/五折 CV 五值/0.3955/0.6364/0.5344/0.4909/0.7512/0.021–0.075 等五教师值与 kill-line 值）均属 v1.0 已覆盖项，09-26 23:06 轮已全过，本轮 diff 确认 v1.1 未改动其数值；[L] dataset 行简化、G1/FTFB 行简化均为措辞压缩，值未变。

---

## 3. 两项不吻合详析与处置建议

### M1：K-N26-2 五读变体范围上限（文内 0.5844 vs 实测 0.5916）

- **误差链定位**：N-26 判定件自身两处汇总表述（§1 kill-line 表「全 5 reads…范围 0.4459-0.5844」＋§1.6 末「范围 0.4459-0.5844」）漏计替代读法 2（drop_glm2，判定件自身在替代读法 2 明细行正确记有 0.5916）；论文 v1.1 §7 与附录 B 系对该汇总的忠实转写。原始数据（sensitivity JSON，dcaa4b6b3b0b）无错。
- **结论层影响**：**零**。五读全部 < 0.75 真证伪线（0.5916<0.75），K-N26-2 五读全 hit=True 的稳健性判定成立不变；K-N26-1/K-N26-3 亦不受涉。
- **处置建议**：① 论文下一版（v1.2）两处改「range 0.4459 to **0.5916**」；② 判定件系冻结工件只读不修——按 append-only 纪律入勘误链新条目（E-37 起）登记「范围汇总漏计 drop_glm2」；③ 依 house rule（V3 报告层引用须并列勘误链），第三作/后续版本引用该范围值时并列新勘误条目；④ 本项属「字节/汇总级」误差（同族于周报诚实边界第 7 条「引用面字节登记误差…只登记不修」），不构成 verdict 修订项。

### M2：T1.5r2 执行总数（文内 60 calls vs 实测 62 新增）

- **误差链定位**：T1.5r2 判定件 §2.1 自报「4 cells × 10 ＋ cell 2 × 11 ＋ cell 3 × 11 ＝ 60 calls」——该算式总和为 **62**，其「＝60」系算术笔误；论文「measured execution: 60 calls across the six cells, 10 to 11 per cell」为忠实转写。原始数据（result JSON c69ab0e3002e）无错：60 reask-2 扩样＋2 rerun 补跑＝62 新增（合并后每 cell 30 records、每教师 15 pairs）。
- **结论层影响**：**零**。裁决预算＋60 已足额执行（reask-2 恰 60）；2 补跑系 T1.5 verdict §4.4 建议的落地（计入同次执行）；15 pairs/教师 ≥ N_min＝10、K-N11-N1_T1relax PASS 根因消除确认均不变。
- **处置建议**：① v1.2 改述为「measured execution: 62 new calls (60 ruled expansion calls plus two make-up reruns), 10 to 11 per cell」或在「60」后加「(plus two make-up reruns recorded within the same execution)」；② 判定件不修，勘误链新条目登记「§2.1 总和笔误」；③ 同 M1-④。

两项均为**汇总/算术级**误差，模式与 09-26 23:06 轮「无修订项」的结论兼容（该轮复核的 v1.0 值不涉及这两处新增表述）。

---

## 4. P-A「假 pass」证据初勘（用户 00:53/00:56 指示的 GitHub 自行搜证）

**背景**：用户告知 V3 口径翻转未传递，最重大者为 PA pass 翻转；系 trae code 走读发现，疑似构造层问题致假 pass；正式件由 minimax 于明后天出具。**仓内现行面（HEAD a57d7fe，pull 无新提交）仍记录 P-A 均衡稳定化 PASS**（V3 终稿：「P-A 均衡稳定化 PASS（60 cells 复现率 51/60＝85.0%，540 账目守恒）」，KT_A1 SPEC＝78b71d404366 已实测在位）。v1.1 全文 grep「P-A」零命中，论文不受影响；**第三作合并前 P-A PASS 面应冻结外显**。

**本轮走读固化的 7 条构造层线索（供 minimax 正式件对表，不作结论）**：

1. **51/60 的混合构造**：`deposon_v2_phase1_60cells_2026_09_11.json`（由 `_v2_stage1_60cells.py` 生成）中 60 cells＝30 历史沿用（源自 2026_09_10 dpath 件，25/30 正确）＋30 新跑（26/30 正确）；「60 cells 复现率」实际重跑面仅 30 cells。
2. **阈值贴线**：51/60＝85.0% 恰落 STRONG_PASS 线（≥0.85），单 cell 边际即降档；D7 摘要以「PASS」出账。
3. **机制无增益自记**：comparison 字段自记 no-RAG 投影基线 52/60＝86.7% > dpath 51/60＝85.0%——「复现率」为裸准确率阈值达标，非机制增益证据。
4. **540 守恒构造性恒真**：每模型 T+R+A 恒等于其 cell 数（T＝384＋R＝78＋A＝78），残差 0 无判别力；V3 终稿/〔IM〕 自标注「构造性恒真/构造性」。
5. **SPEC 判死线与出账证据面的映射缺口**：KT_A1 SPEC V0.1（78b71d404366）预登记双判死线——对外＝Mann-Whitney 单侧 p<0.05＋g_a* 十分位单调；内部＝成本倍数 H0(≥2.0×)/H1(≤1.3×)＋裁定对照表。仓内已检件（deposon_pa_d1_d3_2026_09_15.json、60cells 件、d7_5anchor 件）均未见 Mann-Whitney p 值与成本倍数 CI 的执行结果记录；D7 一页摘要以 51/60＋540＋BOSS 三重可分性（倍数均值 145.8182×、PG 13.6%、ESS 0%）出账——该三面与 SPEC 预登记判死线的对应关系缺对账件（此为「构造层有问题」最可能的落点之一）。
6. **9 模型面 GRAY 存在**：d7_5anchor_60cells_9model_verdict_2026_09_18.json 之 P-A_cross_modal_dpath＝8 PASS＋1 GRAY（deepseek-v4-pro）。
7. **既有 trae 归档审计不含翻转**：_archive_2026_09_18/_trae_d7_v1_audit（09-17）仅修数字（87.0%→85.0%、Adendum 计数、P-L 措辞）与 P-M detection/verdict 矛盾阻断项，未见 P-A PASS 翻转记录——用户所报翻转未落仓，与「忘传递」陈述一致。

**处置**：待 minimax 正式件（明后天）逐条对表后再定翻转范围与波及面（V3 终稿四路径叙述、成就盘点 3dir、coze_〔IM〕 系列均为潜在外显面）；在此之前第三作 V3 主线不得引用 P-A PASS 现行面，v1.1 无涉。

---

## 5. 纪律与红线自查

- **只读**：全部源件经 /tmp 副本实测，冻结工件零触动；仓库零写入零移档（git 状态干净）。
- **verdict 字面**：本报告所有判定值（PASS/FAIL/GRAY/TRIGGERED、kill-line、AUC、p 口径）均为源件字面转写，零软化零外推；M1/M2 之「不吻合」仅限汇总/算术表述，不改判定本体。
- **先核后用**：判定件输入链 SHA-12 本轮逐一复验（§1 表全对）。
- **0 编造**：全部实测值可对回 §1 指纹件；未检项如实标注（Mann-Whitney/成本倍数执行结果「仓内已检件未见」，见 §4.5）。
- **双盲/保密**：本报告为内部核验件；Coze 周报保密口径维持（不入任何论文引用面）。

## 6. 老实交代

- v1.0→v1.1 diff 的数字枚举以 .tex（交付件）为准、.md 交叉，两者一致；「等」字涵盖的外围数字（章号/年份/字节数等非证据性数字）未逐项列示。
- M1/M2 的误差源定性（「判定件汇总笔误＋论文忠实转写」）基于字面对勘与原始数据复算，未采访判定件作者；正式定性以勘误链条目为准。
- §4 搜证为初勘（1.5 小时内）：仅覆盖 results/ 与 docs/V3X/ 主面及 _archive_2026_09_18 trae 归档；Mavis 私域脚本（.mavis/scripts/kt_a1/）仅确认在位未逐行走读；P-A V0 spec 五冻结件未逐一重算。正式翻转以 minimax 出具件为准，本节仅固化线索。
- 用户口径三项（v9 永不提交/FTFB on hold/PA 翻转）对文献合并包的影响已另出勘误补编（见群内通报），不在本报告范围。

—— 鲍勃-实验分析师 ｜ 2026-09-27 00:47 接单，落版于 01:2x ｜ AI 生成
