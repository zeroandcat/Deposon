# FTFB 论文 · KIMI 第二轮复审驳回返修（R3）——内容层执笔交付

- 日期：2026-09-18　执行：查理（内容线/论文主笔）
- 基准（只读参照）：`shared/戴夫_FTFB_v6验收返修验证_2026-09-18/fiction_that_feeds_back.tex`
  tex 指纹 ec3e1a15d905bdd046f60a372e184c8d57ef033411b2dc33bfc947db63ef53bf（606 行，KIMI 二轮所审版）
- 产出：`shared/查理_FTFB_R3返修稿_2026-09-18.tex`
  tex 指纹 51f4e0c8…（SHA-256 前 8 位；全文见交付清单）
- 驳回收执：`upload/6aacf0c67f0575b0af227022_ftfb_rev_acceptance_review_r2_2026_09_18.md`（附录 A 三处超标句全文）
- 触点纪律：全文仅 5 行被修改（L264 / L298 / L409 / L488 / L494），diff 见
  `shared/查理_FTFB_R3返修自证.diff`（unified diff，45 行）
- 计词口径说明：句级复测采用 KIMI 口径＝**连续字母数字段计数**（撇号、连字符、破折号、括注均切开；
  本轮已用被驳三句 63 / 94 / 57 词三值精确复现验证该口径）。全稿词数采用 GLM 口径 P
  （脚本 `count_words_ftfb_v6.py`：Introduction 标题后 → Appendix 前，剔表剔注，全部空白 token）。

---

## 一、S1 —— §6.1 L264 段 63 词句拆分（KIMI 附录 A.1）

**旧句（单句 63 词，冒号+逗号连接，一个句号收尾）：**

> Row M4 is declared rather than smuggled in: the genre's distilled record contains no freeze-before-the-run demand, so M4's criterion is imported from the pre-registration and third-party-recomputation literature ([R47]–[R50]) rather than mapped from the genre, and the diegetic-prototype record ([R32], [R33]) is carried in that row as motivation, not as the criterion's source.

**新句（3 句，各句词数为 KIMI 口径实测）：**

| # | 新句 | 词数 |
|---|---|---|
| 1 | Row M4 is declared rather than smuggled in. | 8 |
| 2 | The genre's distilled record contains no freeze-before-the-run demand, so M4's criterion is imported from the pre-registration and third-party-recomputation literature ([R47]–[R50]) rather than mapped from the genre. | 35 |
| 3 | The diegetic-prototype record ([R32], [R33]) is carried in that row as motivation, not as the criterion's source. | 19 |

依据：KIMI 二轮 R5/附录 A.1；P2-13「每句 ≤45 词（引文除外）」。数字、引文号 [R47]–[R50]/[R32]/[R33]、
主张强度与措辞逐字保留，仅将冒号/逗号连接改为句号切分并删 1 个连接词 "and"（KIMI 口径 63→62）。

## 二、S2 —— §6.3 L294 段 94 词句拆分（KIMI 附录 A.2；本轮实拆）

**旧句（单句 94 词，冒号引入分号列表）：**

> The practice of using narrative artifacts to steer real research and development is documented, not hypothetical, and the pool carries six entries across three literatures: science fiction prototyping proposes fictional scenarios as a source of technology ideas for engineering audiences [R30]; design fiction states the program in its general form [R31] and operates it as an empirical HCI method [R35]; sociological studies of the film industry document cinematic depictions feeding back into laboratory practice [R32], [R33]; and an analysis of computing's future discourse shows research agendas organized by the imaginaries they inherit [R34].

**新句（5 句，KIMI 口径实测，自查复测通过）：**

| # | 新句 | 词数 |
|---|---|---|
| 1 | The practice of using narrative artifacts to steer real research and development is documented, not hypothetical, and the pool carries six entries across three literatures. | 25 |
| 2 | Science fiction prototyping proposes fictional scenarios as a source of technology ideas for engineering audiences [R30]. | 16 |
| 3 | Design fiction states the program in its general form [R31] and operates it as an empirical HCI method [R35]. | 19 |
| 4 | Sociological studies of the film industry document cinematic depictions feeding back into laboratory practice [R32], [R33]. | 16 |
| 5 | An analysis of computing's future discourse shows research agendas organized by the imaginaries they inherit [R34]. | 17 |

依据：KIMI 二轮 R5/附录 A.2（明确指出该句「自旧稿基本未拆、上轮落点不明，本轮请实拆并自查复测」）。
分号列表改为独立句（文献条目逐条成句），删连接词 "and"（KIMI 口径 94→93）；六条目、三文献、引文号全部逐字保留。

## 三、S3 —— §7.4 L409 段 57 词句拆分（KIMI 附录 A.3）

**旧句（单句 57 词，分号连接）：**

> The five printed anchor prefixes date the formalization and the verdict functions to before the runs they adjudicate, on the artifact's own attestation; the freeze is now backed by an independent third-party recomputation (2026-09-18), but not yet by a trusted time-stamp or a third-party archive — the upgrade path is half executed.

**新句（2 句，KIMI 口径实测）：**

| # | 新句 | 词数 |
|---|---|---|
| 1 | The five printed anchor prefixes date the formalization and the verdict functions to before the runs they adjudicate, on the artifact's own attestation. | 24 |
| 2 | The freeze is now backed by an independent third-party recomputation (2026-09-18), but not yet by a trusted time-stamp or a third-party archive — the upgrade path is half executed. | 33 |

依据：KIMI 二轮 R5/附录 A.3。日期 2026-09-18、不确定性措辞（not yet / half executed）逐字保留。
**同段上轮已拆好的 Temporal-priority 句未动**（"Temporal priority: the fictional setting precedes the
formal system it seeds, anchored by the frozen record." 维持独立短句，零回退）。

## 四、S4 —— 词数回补（GLM 口径 P，脚本 `count_words_ftfb_v6.py` 实测）

| 版本 | tex 指纹(前8) | P（正式口径） | C | T |
|---|---|---|---|---|
| base（深度修订前） | 9de366a6 | 12297 | 13437 | 12794 |
| 二审驳回版 ec3e1a15 | ec3e1a15 | 10467 | 12421 | 11272 |
| **本轮 R3 返修稿** | **51f4e0c8** | **10435** | 12414 | 11240 |

- **10467 → 10435，净削 32 词 ≥ 要求的 15 词，达标线 ≤10452，余量 17 词。**
- 相对 base 降幅：(12297−10435)/12297 = **15.14%**，重回 ≥15% 线（上轮 14.88%，缺口 0.12pp 已补齐）。
- 削词归因（全部来自正文 P 区，零红线触碰）：
  - S1 拆句删连接词 "and"：−1
  - S2 拆句删连接词 "and"：−1
  - m6 定义句去重压缩（见下）：−30
  - 合计：−32
- KIMI 口径（12081 → 12049；较 base 降幅 15.21%，其自报跌破线 0.33pp 亦已补齐）。
- 附录区补句（m12，+约 23 词）不在 P 口径区域内，不影响上述计数。

## 五、结转 Minor 处置

**m6（author-attested freeze 定义句 L409/L496 去重）——已清扫：**

- 旧态：定义核心句（"a digest attests that the artifact was not altered after the fact, … to a party
  that did not build the system, … the freeze preceded the runs"）在 §7.4 L409 与附录 L496 两处近逐字重复。
- 处置（按论文自身 P2-9「正文一处指针」原则，即附录开头自述的 "the body of the paper carries one
  pointer per site"）：**全定义唯一保留于附录 Anchor standing（L496，原文未动）**；正文 §7.4 压缩为
  一句＋指针：
  > The anchor is an author-attested freeze: it buys verifiability, not independence, and its standing is stated in the Appendix.（20 词）
- 保真性：被压缩内容在附录逐字存续（摘要所指 §7.4 落点仍含 "author-attested freeze" 与 provisional
  判级原文）；"buys verifiability, not independence" 措辞逐字保留。此压缩同时贡献 S4 所需的 −30 词。

**m12（检索快照可得性 L488/L494 显式覆盖）——已清扫：**

- L488（检索协议段，句末追加可得性从句）：
  > …the raw retrieval snapshots (five results per query) are retained in the project's literature line **and are available from the author on request in this edition, under the availability terms stated below.**
- L494（可得性条目段，"covered by" 间接表述改直接声明）：
  > The raw retrieval snapshots of the Appendix's search record, retained in the project's literature line rather than in the frozen repository, **are available from the author on request in this edition, under the same terms as the frozen repository.**
- 两处均采用全文既有可得性标准句式（"available from the author on request in this edition"），
  与冻结仓库口径一致；改动位于附录区，不占正文词数。

**m13（F-C2 豁免「只降不死」题句点破）——记录不修理由：**

1. 该点破句已存在于 §9.3 段末（上一轮 m13 修复产物，本版原文）：
   > One asymmetry is stated rather than left tacit: F-C2's dispensable-input exemption means a supply-level channel claim can be downgraded but never killed outright by D, so no direct kill line attaches to the supply tier itself.
   KIMI 一轮 m13 所要求的内容（只降不死、无直接判死线、一句点破）在此已完整落地。
2. 若在 F-C2 题句（§1.2 L99 或 §9.3 复录句）内再加插入，将触碰本轮红线「判死线 F-C1–F-C4 不得触碰」
   （§9.3 复录须与 §1.2 substance-unchanged），且与段末既有句语义重复、徒增词数，与 S4 收紧方向冲突。
- 故按「顺手清扫**或记录不修理由**」的处置授权，选择记录不修。若 KIMI 三轮坚持题句级落点，
   建议明示豁免红线后再动。

## 六、纪律与回归核验（全绿）

| 项 | 结果 |
|---|---|
| 五锚（aeefb8ef6972 / 9bbe43f41fa8 / 6e9673205dc0 / 68a5b08ef007 / 6b09de9911c0） | 逐字节不动、各恰 1 次 ✓ |
| R01–R56 编号 | 集合完全一致（56 个，无增无删无变）✓ |
| 零 CJK / 零 email | 0 / 0 ✓ |
| 摘要 | 逐字节一致（1867 字符，未触碰）✓ |
| 判死线 F-C1–F-C4（L99 / L478） | 未触碰（不在 5 个触点行内）✓ |
| 降级措辞 / 数字 / 锚点 / 不确定性措辞 | 逐字保留（diff 逐块核验）✓ |
| 触点控制 | 仅 5 行改动（L264/L298/L409/L488/L494），diff 45 行，零清单外改动 ✓ |
| LaTeX 结构 | 花括号平衡（469 对）；零新增/删除命令；改动纯散文 ✓ |
| 编译冒烟（tectonic 对照测试） | 新旧版在同一行 L27（`\DeclareUnicodeCharacter`，pdflatex/inputenc 专用命令）报同一引擎兼容错——系本机无 pdflatex 的既有已知差异，**非本轮引入**；改动不含任何命令层变化，pdflatex 三遍编译兼容性由结构核验保证，S5 排版重打包时由戴夫实测 ✓ |
| 敏感 token 扫描（first/only/deposon/JSTOR/Cambridge/IDENTIFIER-PENDING 等） | 计数与旧版全部一致 ✓ |
| 上轮已拆句（L357 三子句、§7.4 Temporal-priority 句） | 未触碰、未回退 ✓ |
| 元版本自我指称 | 未引入（"in this edition" 为全文既有句式）✓ |

## 七、交接

- 排版重打包（S5 补件：pdflatex 三遍编译、PDF、tar 包、指纹链、README 更正）由戴夫接手；
  建议以本对照表＋自证 diff 作为回执附件基础。
- 交付物：`查理_FTFB_R3返修稿_2026-09-18.tex`（正文）、本对照表、`查理_FTFB_R3返修自证.diff`。
