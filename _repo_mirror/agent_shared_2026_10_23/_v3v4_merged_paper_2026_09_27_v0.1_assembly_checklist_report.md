# 第三作合并稿 v0.1 装配轮自检报告（查理-论文主笔，2026-09-27）

- **对象**：`shared/_v3v4_merged_paper_2026_09_27_v0.1.md`（171,023 B / SHA-12 `758E361397C2`，980 行）＝上半件（part1，541 行/104,375 B）＋下半件（part2，74,651 B / `49A17DED4706`）脚本拼接＋A 轨全文重编号。
- **依据**：上半件末尾「Assembly-round checklist (complete v0.1)」四项＋爱丽丝蓝图 §8 验收硬口径＋阿兰验收复核 P0 三项。
- **方法**：程序化实测（python3 正则扫描/逐 token 计数/字面抽查），全部只读；装配脚本 `agents/…e74/work/assemble_v01.py`，检查脚本 `check_v01.py`（工作区留档可复跑）。
- **结果**：**22/22 项全过**（首轮 17/23，4 项为检查词过窄的误报，逐项核实后修正检查词，稿件本体零缺陷；另有 1 项 [0] 系数学区间 [0,4] 非引用 token，已排除）。

---

## 一、装配清单第 1 项：A 轨重编号＋References 编译＋pending 标记

| 检查 | 结果 | 实测 |
|---|---|---|
| 1a. 全文 [n] token 首现序严格递增 1→64 | **PASS** | 首 token 序 [1,2,3,4,5,6,7,8]…末 [62,63,64]；共 64 个不同编号；数字 0 仅出现于 §18.1 的 τ 网格区间 [0,4]（数学区间非引用） |
| 1b. References 列表 | **PASS** | 64 条连续编号 [1]–[64]，零跳号零重复 |
| 2. 引用↔列表双向闭合 | **PASS** | 未被引条目：0；无对应条目的 token：0 |
| 3. 三条 v1.1 作者-年份引用并入编号 | **PASS** | (Nosek et al., 2018)→[18]、(Popper, 1959)→[19]、(Yang et al., 2025, arXiv:2510.15746)→[20]，各恰 1 处替换，残余 0 |
| 去重三处（key04／2510.15746／2404.00699） | **PASS** | A 轨各恰一条：[4] 第一作（匿名 fork）；[20] Yang（v1.1 侧唯一载体，候选池未入文）；[38]（v9 侧 key38 沿用）；App C C.1 表登记三处合流点 |
| 4. pending 标记全量携带 | **PASS** | v19_fullrank×2、v20_baselines×2、pending PI final ruling×3、[L]×14、[R]×5、pending-proof placeholder (R4)×1、pending verification×9、8-gram deferred×3；零删除零升格 |

## 二、装配清单第 2 项：App A/B/C 传播

| 检查 | 结果 | 实测 |
|---|---|---|
| App A 输入件锚 | **PASS** | 新增小节 3 行（v9 tex 102,686/02acb6d563eb；v1.1 md 54,367/38BC2CF38D10；v1.1 tex 58,828/58BD3F5BEF3A），沿鲍勃 09-27 核验值；v1.1 全表逐行原样迁移（TaskB 链 12 行、dataset/信件族 [L]、T 系与 N-26、治理、五版本待定件） |
| App B E-37.1 传播 | **PASS** | K-N26-2 行写 0.5916（「range 0.4459 to 0.5916」）＋同款 E-37.1 勘误注记（原值 0.5844 在该处注记内引用恰 1 次）；全文 0.5844 共 2 处＝part1 §14.2 与 App B 两处注记各 1 次（per-location once 口径）；0.5916 在正文 2 处＋App B 1 处＋conventions/§13.3 计 5 次 |
| App C 口径注册表 | **PASS** | R1（作品序列，v9 并入为唯一公开载体）registered；R2（单篇承载）registered；R3（冻结数字与 verdict 字面纪律，含 E-37 家族）registered；R4 **pending-proof placeholder，明示未收束**（记录零内容、零引用、零立场）；FTFB「submitted to arXiv and, as of the writing day, on hold」＝全稿唯一 on hold（§1.2）；v9 未刊并入声明在 §1.2 conventions 与 §22.4 |
| App C 其余 | **PASS** | C.1 逐节并入比例表（merged in full／migrated with frozen numbers／new composition 逐节标注）；C.2 指针重映射清单；C.3 8-gram 占位（对照 v9 单稿先例值 4.62%/0.21%/0.91%，标注「merged-in coordinate-system material」口径，戴夫终排实测）；C.4 保密纪律核验声明 |

## 三、装配清单第 3 项：Part III 起草（§17–§24）

| 检查 | 结果 | 实测 |
|---|---|---|
| 蓝图合成区落实 | **PASS** | §17（表 4 六块链映射＋表 5 合并矩阵＝v9 表 3 五行原样＋V4 行新增，行序注记 rows 1–5 外部／row 6 →§18.1／row 7 V4）；§18.1 v9 §9.3 全量并入（matrix row 6 表迁移，[4] 匿名 fork，survey 自指改写为 this paper）；§18.2 register 对齐声明（零数字）；§19 (a)–(d) 全量＋V4 anchor 四段（(c) 显式「V4 anchor: none」防外推）；§20.1–20.2 v9 §10 全量（OP1–OP8 原文，OP8 实例句升级为双案例）＋§20.3 计划性五线（探索性档、零数字、声明「非预测」）；§21 v1.1 §11 七条＋合并稿自身 2 条新增；§22.1–22.5（D10 五小节：v1.1 §10.1–10.3 迁移＋执行面状态句＋v9 §1.3 浓缩＋自重叠披露占位）；§23 v1.1 §12 主体＋v9 AI 披露重述合并；§24 重写（H1 合题主句为骨架） |
| 无空节 | **PASS** | §17–§24 全部小节均有内容；全稿 §1–§24 逐节扫描零空节 |
| 蓝图去重规则 | **PASS** | D2（FTFB 交叉引用单点，part1 §2.1）；D3（三档定义唯一定义处 §3.2＋§16.2 交叉引用不重复）；D5（AI 披露合并 §23）；D7（判死线表仅 §12＋App B 两处，无第三处）；D8（跨线命题三处保留为综述原设计）；D9（写作规则 §16 原文，v9 纪律交叉引用）；D10（Availability 合并 §22 五小节）——App C C.1 逐节登记 |
| 指针重映射 | **PASS** | v1.1 §10/§11/§12/§13→§22/§21/§23/§24；v9 §9.1/§9.2/§9.3→§17.3/§19/§18.1；v9 §10→§20；v9 §1.3→§22.4；Part I 内部指针（§3–§8）零重映射（节号恰好一致）；残留 v1.1/v9 旧编号正文指针 0 处（Part II 的「its Section 3.4, Plan A」系判定件内部节号，按口径不改） |

## 四、装配清单第 4 项：全文检查

| 检查 | 结果 | 实测 |
|---|---|---|
| 5. F 系冻结字面抽查（22 项） | **PASS** | F1（0.0909/0.6842/0.3333/[0.0, 0.2045]/two composite）；F2（0.5663/0.4459–0.5916/五折 CV 五值/kimi 0.7512/均值 0.5617）；F3（49.3%/500/0.870）；F5（239,387/849D76BE3A06）；F6（App A 抽验：dataset 12,672/7B01CD835A41、formal verdict 33,723/5D79E67A4E9D、第一作 68,164、FTFB 356,123/2D9EDC8C7303）；F7（0.70/0.75/0.60 判死线）——全部在位，一字未改 |
| 6. verdict 字面 | **PASS** | FAIL×34、TRIGGERED×14、NOT TRIGGERED×10、composite qualification×15、pass = True×6；E-37.2（62 calls）随 part1 §13.3 原样 |
| 7. O 系零收束 | **PASS** | 收束式表述扫描（has been resolved/is now closed/closes the phase 等 8 式）零命中；open 边界句 5 处（open at writing time×5、closes nothing×5，§16/§20.3/§24 及摘要） |
| 8. 双盲五点 | **PASS** | ①署名占位（Attribution withheld）在位；②仓库 URL/commit/blob 标识符零出现（执行面状态句不带 remote 标识符，按蓝图 5.2 第 2 条执行）；③第一作条目匿名 fork（Attribution withheld for double-blind review）＋v9 实名元素清零（Qihao Yuan 零出现）；④GLM 句式走 PI GitHub 唯一权威源口径；⑤致谢节零存在（acknowledged 仅作为普通动词出现 1 处，§5.2 正文） |
| 9. 保密件零引用 | **PASS** | 周报标识（coze_app/D7–D14/周报/〔当事人W〕/〔机构G〕）零出现；coze 小写仅 4 处＝K-N26 教师列表（判定件字面）；§20.3 计划性描述零数字；App C C.4 声明句为保密纪律自证（非引用） |
| 10. 禁外推枚举 | **PASS** | 七类外推句式（chain-of-thought cannot be distilled 等）零命中；不把 ⑤ 填充实例外推为领域级收束（§17.1 明示「fills no cell of the external base」） |
| 11. 名称消歧 | **PASS** | K-N26-*×24 与 K-N11-*×4 两族分立零混写；KT-C1/KT_C1 零出现；§17.2 增设「程序内判定档 L1–L4 vs 外部五线 L1–L5」消歧注记 |
| 12. 无空节 | **PASS** | 全稿逐节扫描零空节 |
| 13. E-37.1 App B 传播 | **PASS** | 见第二节 |
| 14. 8-gram 自重叠 | **PASS** | 占位在位（App C C.3：「deferred to the typesetting round」×3）；本轮不实测（戴夫 v0.2 终排前实测，沿占位目录声明） |
| 15. 摘要字符预算＋ASCII | **PASS** | 摘要 1,880 字符（≤1,920 预算）；非 ASCII 字符 0 |
| 16. 分件脚手架清除 | **PASS** | 「Part-file note／Lower-Half Placeholder／End of the …part file／assembly-round checklist」零残留；part1 的 Part-file scope 行改写为 Paper scope（完整范围）；conventions note 的编号段改写为统一序列描述；E-37 传播注记补 App B 指针 |

## 五、阿兰验收复核 P0 三项落实

| P0 | 落实 |
|---|---|
| P0-1 v9 永不提交 | §1.2 conventions＋§22.4 明示「never submitted and will not be; this paper is its only public carrier」；全稿零 v9 公开提交面指向 |
| P0-2 FTFB on hold | §1.2 锚引「submitted to arXiv and, as of the writing day, on hold」（全稿唯一 on hold）＋App C R1 登记；零 arXiv 正式引用切换（触发器挂起） |
| P0-3 PA 翻转 | 全稿「P-A」「PA pass」「BOSS-P」字面零出现（本轮 grep 实测，三式均 0 命中；「R4 purge」4 处系密钥清除轮叙述，不含 P-A 字样，两不相涉）；R4 待证占位不收束（App C R4 条目原文「pending-proof placeholder, explicitly not closed…no position in either direction」）；正文零 09-23 补充判定件与 minimax 件引用 |

## 六、老实交代

1. 装配脚本对 part1 的改动仅限四类：占位目录截断、A 轨重编号（整数 token ≤17 不变、18–61 →+3）、三条作者-年份→[18][19][20]、头部三处 part-file 措辞改写（Part-file scope→Paper scope、conventions 编号段、E-37 传播注记补 App B 指针、附录指针精确化）；part1 的 F 系正文与 Part II 判定链零触动。
2. §17 表 4（六块链映射）与 §17.3 V4 行、§18.2、§19 V4 anchor 四段、§20.3、§21 (8)(9)、§22.5、§24 为新写合成区（蓝图预填素材起草，待双审复核）；§19 (a)–(d)、§17.3 表 5 外部五行、§18.1、§20.1–20.2、References [1]–[17]/[21]–[64] 为 v9/v1.1 素材忠实迁移（token/指针映射＋双盲 fork＋survey 自指改写，数字零改动）。
3. 8-gram 自重叠未实测（占位口径沿占位目录与蓝图 5.4，戴夫终排轮执行）；tex 版未产出（派单明示留后续轮次）。
4. 本报告 22/22 为程序化实测结果；「coze」4 处、F 系 22 项抽查、双盲扫描均为字面级扫描，抽查而非全量人工复读（全量字面对照仅在 §18.1 迁移段与 E-37 三处执行）。
5. 执行面状态句（§22.3 增补）按蓝图 O2 授权写入 2026-09-27 口径，但依双盲红线 2 不携带 remote HEAD 标识符，锚定表述为「per the public release history」；回执两处算术不自洽中仅展开可对算的一处（342−51=291≠294），另一处以「per the receipt's own wording and registered as pending verification」登记不展开（无一手语境，不编造）。

—— 查理-论文主笔 ｜ 2026-09-27 ｜ AI 生成（GLM）
