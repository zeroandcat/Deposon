# 查理 · 第三作 v0.4 口径注册轮修订记录（2026-09-28）

- **任务来源**：群管理员 2026-09-28 00:21:22 派单（第三作 v0.4 修订：口径注册层，正文零改动；五项范围＝R4 升级 registered／v20_baselines 废版注记／COZE·GLM 强制口径自查／signoff 双指纹注记／F·O 清单同步）。
- **输入件**：① 鲍勃《V3 口径变化说明专件消化与影响映射》（2026-09-28，§B 翻转清单＋§C 对表＋§D 影响映射：R4 可升级 registered、v20_baselines 注记、signoff 双指纹、8-gram 属后续轮）；② Coze 专件落库副本（`shared/coze-v3-calibration-note-20260927/`，README＋extracted.txt；§3.1/§3.2 强制口径、§5 锚点自报表、§1.8/§1.9/§1.10 假判族与处置全景）；③ 09-23 判定件＋diag JSON（仓内实测，见 §三）。
- **基线**：`shared/_v3v4_merged_paper_2026_09_27_v0.3.md`（180,626 B／990 行／SHA-12 0B8F594192F9）。v0.3 存档零触碰（本轮落库前后 sha256 复测一致，见 §六）。
- **交付物**：`shared/_v3v4_merged_paper_2026_09_27_v0.4.md`（191,119 B／1008 行／SHA-12 E6C76F9BE292，完整单件）＋本修订记录。

---

## 一、五项范围逐项处置对照

| # | 派单项 | 处置 | 落位 |
|---|---|---|---|
| ① | App C R4 升级：待证占位 → registered，内容按鲍勃报告 §B | **已执行** | C.3 R4 条目整条重写（v0.4 行 1000）：P-A 系 5 项翻转（145.8× 假成立·C1+C3 收口／0/22 ESS 假成立·22/22 常量／3/22 PG 已裁决为 KT_B1_REWORK 22/22 全 PG（E-40.1 字面·单源）／源报告参考表 L143-147 废证·逐字段不符且与同报告均值互斥／「中期 PASS（总）」过强·三项支撑＝2 常量退化＋1 冲突）＋同族假象 9 条降级（记录自报计数：假证伪 5＋假成立 3（含上述两项 P-A 成员）＋结构性恒等 1）＋状态层 2 项不可判（四路径总判·计算态与 verdict 占位并存／综合判死 51/60↔52/60 并存）＋P-C/P-E/P-F 维持不翻转（P-C 可强引真证伪、P-E/P-F 带限定维持）＋处置全景登记（登记不改件·零修复留 PI 拍板／PG 裁决闭合／废版不补件／T1 型假象已由 T 系修正消解且本稿 §13.3 已载）＋证据载体五件（见 §三）＋形制沿 R1–R3（登记事实、不转录原件、不入 References、C.4 保密纪律不受影响）；配套：App A 新增「R4 re-adjudication evidence」表（行 926–936）＋C.0.2 注册节（行 962–964）＋C.4 v0.4 注记（行 1008）。正文维持零 P-A（§四实测）。 |
| ② | v20_baselines 废版注记（E-40.2，单源，v22 未上仓），维持 no-version-chosen | **已执行** | App A「Version-pending items」列表后新增 v0.4 注记（行 915）：登记 E-40.2 字面（三件废版·不再补件·依赖结论引用面降「不可判」；v20_baselines 为三件中唯一列入本清单者）、单源注记（PI 侧 v22 未上仓）、本稿不选版本、pending 状态不变。正文三处 version-pending 句（§16.2/§21(3)/§22.3）零改动——「version-suspended until the PI's final ruling/no version chosen」陈述在废版宣告（单源、待 PI 终裁）下仍然为真。 |
| ③ | COZE/GLM 强制口径自查（专件 §3.1/§3.2），对照第三作既有实践逐项核验 | **已执行，零未达标项** | 逐项核验表见 §二：§3.1 六强制项＋三禁项、§3.2 五强制项＋四禁项，全部实质达标；两项形式注记（章节形态差异／§16.2 括注精度）登记于本记录，不构成未达标，无需按口径调整正文；论文内以 C.0.2 一句登记自查结论（「no non-compliant main-text item was found and no adjustment was required」）。 |
| ④ | signoff 双指纹注记（专件自报 26,637/BA4D07BD7000 vs v0.2 登记 26,633/739245682D40），按 E-37 例外通道先例登记双源指纹并注记待 PI 归一 | **已执行** | App A signoff 行 v0.2 注记后追加 v0.4 注记（行 830）：letters 族专件自报 26,637 B/BA4D07BD7000（自报·专件不上仓·不可盘上复算，与该行所引 commission-ledger 对相符）＝第一指纹源；第二副本在册实测 26,633/739245682D40＝第二指纹源；双源并存登记、归一待 PI；行值维持 commission-ledger 对（冻结值零改动）。C.0.2(iii) 同步登记，并明示系注册层溯源注记、非 E-37 通道新成员、非冻结字面例外（R3 通道范围声明不受扰）。 |
| ⑤ | F/O 清单同步：因本次口径变动发生状态变化的 O 项如实登记 | **已执行** | 状态变化三项如实登记：(a) R4 占位 → registered（本轮唯一收束 O 项，触发事件＝正式件出具＋载体锚在仓，C.0.2 明示）；(b) v20_baselines 状态变化＝废版宣告入册（未收束，no-version-chosen 维持）；(c) signoff 增第二指纹源（「待 PI 归一」维持）。其余 O 项零变化（R5 槽位/R6 待核计数/R7/R8·§22.5 8-gram 维持 deferred/C-2 窗口 2026-10-15/五件版本待定/其余 pending 项）；R8 侧登记鲍勃 §D.11 结论：v0.4 有净正文变动 ⇒ 8-gram 须于后续排版轮重测（本轮不测）。 |

## 二、§3.1/§3.2 强制口径逐项自查表

**§3.1（COZE 汇报面，6 强制＋3 禁止）**

| 项 | 第三作既有实践载体 | 判定 |
|---|---|---|
| 三档分档（判死级/观察性/探索性） | 约定段三层证据分级（closed (pre-registered)／consistency／motivation only＋scope markers）；§16.2 按层清点；§17.2 各块层标；§20.3 计划层明示探索层；无未分级结论 | 达标（档名异、功能同：无混层、无未分级引用） |
| FAIL 附根因注记（α/β/γ/复合） | App B「Root-cause classes: composite, β, composite, β」字面；§12.4 复合定性两面；§13.1 α/β/composite 分类学；§15.2 PI 裁决根因；§16.2(4)「every verdict number co-presents its root-cause class」 | 达标（Part II 诸 verdict 源记录均带根因类，无 γ 类成员；R4 新登记状态层 2 项即以 not adjudicable 名位登记于注册层） |
| T1 类假象 PASS 不得引为稳健证据 | §13.2 载 T1 判定字面（any_hit=false）并立即以「决定性产物＝重分类（five of five K-family → β）」收束；§13.3 载修正构造后方向一致（T1.5）；§16.2 将「T-series 方向稳定注记」置于 consistency 层（观察性层） | 达标（附形式注记：§16.2 括注前半句为 T1 记录字面，句内未复附 β 限定，限定载体在 §13.2，且该稳定注记经 T1.5 修正构造重立；全稿无以 T1 PASS 作稳健性（closed 层）证据处） |
| 负结果与正结果一并交付 | Part II 全负记录为一等内容；§1.2「kills are first-class content」；§24「the kills are filed so they cannot be un-killed by narrative」 | 达标 |
| 数字一律盘上实测＋SHA-12 | 约定段「every verdict number … anchored to a path, a byte count, and a SHA-12 digest in Appendix A」；App A 实测表＋[L]/[R] 披露约定；本轮 letters 族指纹均带「自报/记录锚/不可盘上复算」注记 | 达标 |
| 引用他方以「引述/受托方/历史快照」形式 | §14.1 教师代号「internal codenames … internal labels」quoted as recorded；§15.1「internal model labels are quoted as recorded」；§15.2 裁决引文为翻译非替代；R4 登记中第三方回函仅以「third-party」名位出现 | 达标 |
| 禁：软化判死 | §16.2(a)(b) 明令禁软化（banned moves 列举）；verdict 五族字面频次 v0.3/v0.4 全等（§四） | 无违例 |
| 禁：β 升格为 α | 复合定性两面并存（§12.4）；App B 根因类字面托运零改动 | 无违例 |
| 禁：判死级降档探索性 | §16.2 分层零改动；无任何 closed 层结论改置观察/探索层 | 无违例 |

**§3.2（GLM 终稿面，5 强制＋4 禁止）**

| 项 | 第三作既有实践载体 | 判定 |
|---|---|---|
| quote-not-remeasure（判死记录＝可复算资产） | R3 冻结字面托运纪律；E-37 例外通道两成员（E-37.1/E-37.2）为注册例外；冻结 verdict 文件未改（v0.2/v0.3/v0.4 一贯）；本轮 R4 登记为 as-reported＋载体锚定，不重算不合并 | 达标 |
| 复合定性不外推（3 子项） | 任务 B v2 → §12.6(1) 明言不构成「PI 思维链不可蒸馏」命题级宣告；N-26 → §14.4 明言不支持「完全不可分」（kimi 0.7512 反信号在录）；T1 → 见上；§16.2(c) 禁外推清单字面枚举 | 达标 |
| 涉 GLM 模型/版本/能力/署名以 PI github 为唯一权威源 | §14.1/§15.2/§23 三处明言 defer to the PI's GitHub as the sole authoritative source；全文无模型版本/端点/产品名 | 达标 |
| AI 使用声明署名如实 | §23：多 agent AI 管线（scout/architect/analyst/writer/formatting specialist）＋「The drafting model is GLM」如实披露；第三方名头仅以记录字面出现 | 达标 |
| 失败/负面结论章按复合定性分子节组织（α/β/复合/构造存疑四子节，不混写） | 实质达标：每个 FAIL 并置根因类（App B 类字面、§12.4 两面、§13.1 分类学、§14.3 L4 构造不可行），无未分类、无混写；形式差异：第三作按判链时序组织（§12–§15）而非四子节单章——专件该项系对独立终稿受托面的「建议 §4」形态 | 实质达标＋形式注记（本轮正文零改动不予重构；如 PI 要求四子节形态，另开轮次） |
| 禁：4 hit 软化为「部分触发」 | App B「Four kill-lines, all hit」字面托运；§16.2(a) 禁改写 | 无违例 |
| 禁：v3 预登记生效未跑出当已判 | 全文零 v3 重启预登记记载（Task B 链止于 v2.2；grep 无 v3 prereg 载体）；R4 登记为 V3 期补充判定的外部重审记录，不裁任何 v3 期运行 | 无违例 |
| 禁：判死记录合并重写新表 | App B「exactly as carried」两判定表重述；R5 派生 JSON 不合并铁律；本轮 App B 分区字节级全等（§四） | 无违例 |
| 禁：以 PI github 以外源件填 GLM 模型版本/能力/署名 | 无此类表述（唯一权威源三处 defer 在位） | 无违例 |

**结论**：15 强制项全部实质达标（含 2 项形式注记），7 禁止项零违例；无未达标项 ⇒ 无需按口径调整正文。两项形式注记与档名映射差异登记于本记录（working chain 载体），论文内仅登记自查结论一句（C.0.2）。

## 三、证据件仓内实测与指纹核验（本轮实测，2026-09-28）

| 件 | 实测 | 与派单/鲍勃报告比对 |
|---|---|---|
| `repos/Deposon/_september_workspace/results/_v3_supplement_verdict_2026_09_23.md` | 15,247 B／B70211BFA83E | 与派单值、鲍勃 §B.4、专件 §5 一致 |
| `repos/Deposon/_september_workspace/results/_v3_construct_degradation_diag_2026_09_23.json` | 11,609 B／C8D539A58D29 | 同上一致 |
| `repos/Deposon/_september_workspace/docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（仓面） | 239,387 B／849D76BE3A06 | 与 App A Governance 行一致（止于 v19/E-36）；专件 §5 自报 v22＝292,215/083087218A8D 属 PI 侧扩展，按单源登记 |
| `repos/Deposon/_september_workspace/results/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` | 26,637 B／BA4D07BD7000 | 与行引 commission-ledger 对及专件 §5 自报一致（第一指纹源） |
| `repos/Deposon/_september_workspace/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md`（第二副本） | 26,633 B／739245682D40 | 与 v0.2 登记一致（第二指纹源；diff 实测 4 字节差＝1 个表格行内两处 `\|` 转义对） |
| Trae 回函 `letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23.md` | 不上仓；指纹为仓内文本记录锚：28,207 B／9BB22099DB3B（载于 3dir achievements inventory 与勘误链 v19 两处仓内文本） | 按 [R] 记录锚登记，非本轮实测 |
| Coze 专件原件 `letters/_v3_calibration_change_note_for_coze_glm_2026_09_27.md` | 不上仓；自报 21,869 B／A5C33BD45D78 | 按自报登记（不可盘上复算）；论文内不载文件名（fingerprint-only 外显，遵专件自署「对外只给指纹」），全名载于鲍勃报告/落库 README |

## 四、纪律自检

1. **F 系字面零改动**：分区 sha256 全等——Abstract（v0.3 L14-21 vs v0.4 L14-21：2faedd5e8279）、Part I（无 hunk）、Part II（L288-633：57f2605b0b38）、References（L682-815：9e1aa39e97c6）、App B（v0.3 L926-934 vs v0.4 L940-948：8f1160a16090）；diff（n=0）10 个 hunk 全部位于 L3／L636／L638／注册层（App A×4＋App C×3），零计划外改动。
2. **verdict 字面频次全等**（grep -o 全文口径）：FAIL 34=34、hit 18=18、TRIGGERED 14=14、NOT TRIGGERED 10=10、composite qualification 15=15（v0.3→v0.4）。
3. **引用闭合**：方括号 token 总数 220=220；[41] 6=6、[45] 5=5；References 分区字节级全等（64↔64 不动）；本轮新增文本零方括号引用（R4 载体全部走 App A 锚，不入 References）。
4. **数值 token 多重集**：全文删除仅 {「27.」×1}（App A 前导句句式改分号所致标点附着，数字 2026-09-27 本身保留，非数值内容变化）；正文区（L14-681）删除＝∅、增量仅 v0.4×3＋v0.3×1（两处轮次句）；全文增量 175 token 全部位于注册层（R4 证据指纹、翻转读数、E-40 编号、日期、行号引用等，逐一可溯源至派单与鲍勃报告 §B）。
5. **正文零 P-A**：正文区（L14-681）P-A／four-path／145.8／ESS 均 0 命中；全文各命中 1 次，全部位于 App C R4 注册条目（计划内）。Part I/II/III 判链零涉。
6. **O 系**：唯一收束项＝R4 占位（触发事件已登记）；其余开放项零收束（v20_baselines 状态变化未收束、signoff 待归一维持、R8/§22.5 维持 deferred、C-2 窗口不动）。
7. **双盲与零命中**：a57d7fe/Qihao/2609.09001/〔当事人W〕 均 0=0；coze 4=4（v1.1 教师代号）、Yuan 1=1（文献作者子串）、D14 2=2（SHA 十六进制子串）、minimax 4=4、kimi 5=5（均冻结字面）；专件文件名（for_coze／calibration_change_note）论文内 0 命中；Coze 周报族与本专件正文零引用零转述（C.4 v0.4 注记在位）；新增文本无作者/机构身份信息。
8. **体例与空节**：全英文 arXiv 预印体例（新增节均英文）；空节旗标 18=18 基线不变、表头直跟节 12=12；标题数 114→116（新增 C.0.2 与 R4-evidence 两节，均有实内容，无空节）。
9. **版本联动口径**（沿 v0.3 先例 L3/L636/L638，与 v0.3 轮次机械项同位）：L3 版本行、§21(6)/(9) 两句轮次史真值维护（旧句保留即失实：v0.4 已发生而句内未载／「this round」指代漂移）；除该 3 处外正文零触点，全部改动落于注册层。

## 五、注意事项与边界

1. 本轮为注册层轮：R4 登记内容为「as reported」外部重审记录，正文判链、冻结数字、verdict 字面零涉；PI 侧 v22（E-40.1/E-40.2）为单源引用，正文 frozen-at-v19 托运不动（C.0.2(iv) 明示）。
2. 专件按其自署保密纪律处理：不入论文引用面与公共仓，对外仅指纹（论文内连文件名亦不载，全名在 working chain：鲍勃报告/落库 README/本记录 §三）；D14 周报族零涉及。
3. v0.3 存档零触碰；v0.2/v0.3 注册节（C.0/C.0.1）原样保留，C.0.2 明示「stand unchanged」。
4. 8-gram 自重叠重测（净正文变动已发生）、tex 版/R8 回填/编译属后续排版轮（鲍勃 §D.11 口径），本轮未做未预判；R5/FTFB R4 重投/arXiv ID/解 hold/C-2 窗口（2026-10-15）等事件仍 pending。
5. 专件 §E 其余宣告（任务 B v3 预登记 B7547329AF2E 仓内缺件、KD 判据 0.0028、dataset v1.2=85 events、v17/v18 废版等）不在派单五项范围，未入论文注册面；论文 Task B 链止于 v2.2，不受影响。
6. 「V3 的剑不斩 V4 的官」（专件 §2.7）：V3 期翻转不涉 V4 判链——与鲍勃 §D.8 影响映射（F 系 22 项不涉 P-A）一致，论文 Part II 零改动为该口径的自然后果。
7. 自查两项形式注记（§3.2-5 四子节形态差异、§3.1-3 §16.2 括注精度）仅登记于本记录；如 PI 要求按四子节形态重组失败章，属正文重构级改动，应另开轮次。

## 六、交付实测值

- `shared/_v3v4_merged_paper_2026_09_27_v0.4.md`：191,119 B／1008 行（wc -l）／SHA-12 E6C76F9BE292
- 修订面：10 位点＝10 hunk（diff -U0；v0.3 行号 3／636／638／818／830／914 后插入／923 后插入／947 后插入／982／990），零计划外改动；正文触点仅 2 处（L636/L638 轮次机械项）
- 基线 v0.3 复测（交付前）：180,626 B／990 行／SHA-12 0B8F594192F9（与三路审读轮登记值一致，存档未触碰）
- 新增注册面：App A（前导句扩展＋signoff v0.4 注记＋version-pending v0.4 注记＋R4-evidence 表 5 行）；App C（C.0.2 节＋R4 条目重写＋C.4 v0.4 注记）

—— 查理-论文主笔 ｜ 2026-09-28 落版 ｜ AI 生成
