# 爱丽丝·V5 前置参考归档评审件（合为唯一·2026-10-18）

- **归档人**：爱丽丝-算法架构师
- **日期**：2026-10-18
- **性质**：归档评审件（转写＋登记；0 重做核验、0 新增评审判断、0 改写任何源件、0 改仓 0 推送）
- **授权链**：PI 2026-10-18 09:35 群令「三项全授权，合为唯一评审件，实验未完成，阶段性更新，含现有待推，KIMI 也即将推送，等线索册与补件」→ 群管理员 2026-10-18 09:55 派单（本件任务书：7 项修正转写前置条件＋文献面并入＋边界登记）
- **对象件**：组外 GLM 件《deposon v5 心哲节点概念映射_2026-10-12.md》（8,374 B，sha `694131a3693b`，只读）

---

## 〇、归档定位（先读）

1. **本件＝V5 面评审成果的唯一归档形态**（「合为唯一」）：以爱丽丝 10-17 架构面评审的 7 项修正为主体，逐项转写为「SPEC 起草前置条件」（P-1～P-7）；并入阿兰 10-17 文献面结论（L-1～L-5）；登记边界三条（B-1～B-3）。
2. **归档 ≠ 立项**：V5 SPEC 立项时机由 PI 定；**线索册与补件到位前，0 立项动作**——不起草 SPEC、不生成种子映射表、不新增任何 V5 机制设计、不扫未扫方向文献、0 改仓。
3. **上游证据件两份保留不改**（本件全部主张的回溯源，指纹本机实测）：

| 件 | 指纹 | 字节 | 用途 |
|---|---|---|---|
| `shared/爱丽丝_V5心哲映射评审_2026_10_17.md` | `b8467a0a1183` | 22,201 | 架构面评审（7 项修正源） |
| `shared/阿兰_心哲文献核验与交叉补扫_2026_10_17.md` | `cbc38d90648f` | 11,906 | 文献面核验源（0 重做核验） |
| `shared/鲍勃_认证态仓态刷新_2026_10_18.md` | `60dbb71d1117` | 11,449 | 时点声明佐证（远端 `74c7d76` 零前移、V5 主线 0 落仓） |

4. **时点声明**：本件基于 2026-10-18 上午现势——远端 main＝`74c7d76`（10-12 我方第七波推送后零前移，认证态与匿名可见性内容面零差异）；V5 主线/心哲文件 0 落仓，仓内唯一 V5 前驱＝10-12 入库的预告字面（见 B-2）。

---

## 一、七项修正 → SPEC 起草前置条件（P-1～P-7）

**总则**：P-1～P-7 为 V5 SPEC 起草的硬前置条件——任一条不满足，SPEC 相应章节不得起草或定稿。逐条源修正原文见上游件 §七「需修正（进 SPEC 前必须处理）」。

### P-1 事实基线：v1.6 先验臂状态
- **【前置条件】** SPEC 凡引 v1.6 LLM 先验臂处，必须写 **completed**（live-API 评估 2026-08-28 完成，`results/deposon_v16_llm_prior.json` 实读 `llm_arms: "completed"`，先验缓存为 2026-08-23 真 API 工件 `a9b5bb6`）。`pending_no_key` 仅可作历史注记（`run_v16_llm_prior.py` 无 key 时的代码路径常量＋`verifier/v5` 提交 `134cc6a`「pending key」系基建期历史快照），**不得写成当前状态**。
- **【源锚】** `results/deposon_v16_llm_prior.json`（39,974 B）；提交 `6d7088f`/`5954771`。
- **【源修正】** 10-17 件「需修正 1」（§7-6 前提错误——上游评审唯一事实性硬伤）。

### P-2 机制读法：意向性 R 通道
- **【前置条件】** SPEC 意向性接口的机制主张**限 T 通道单侧**（E⁽ⁱ⁾=E⁽ⁱ⁻¹⁾·T_i 沿路径递归，「沿指向透射」成立）；R 通道**不得写「折回重估/再入射」**——仓内 R 的注册语义＝blocking 态「erroneous paths decay by local reflection」（局部反射衰减）＋终态记账（per-node shares 求和），反射能量不回流遍历，系统无折回再入射回路（耗散侧 `dissipate()` 原子单调累计、无 `recover()`，反射侧同构无再注入）。若 V5 需要 R 侧重估功能，必须作为**新增机制**单独立项、预登记判死＋守恒账扩展设计。
- **【源锚】** `paper/deposon_paper_final_en.md`（`2ec20b96e941`/68,164 B）T/R/A 定义与 blocking 态语义；上游件 §三意向性行。
- **【源修正】** 10-17 件「需修正 2」。

### P-3 强度档位：Bratman 三环第二环
- **【前置条件】** SPEC 凡引「无承诺→发散」证据处：①表述必须降档为「无耗散时 **58/338 合成图谱**发散（观察性谱发现，未达定理级）」——58/338＝17.2% 子集、合成图、注册件自评「观察性规律（谱发现）＋探索性（博弈论翻译）」；②必须**并列任务级零收益句**（论文 L63 原句：不可逆耗散通道从未在任何已测任务上胜过其禁用对照，收益主张目前仅有理论动机）；③58/338 型谱证据只能作机制面素材，**不得充当任务面判死线**。
- **【源锚】** `docs/THINKING_V3_GT_CONTRIB_2026.md`（`b04c39175ede`/19,769 B，L70 谱发现/L83 自评/L104 C2 线）；论文 L63。
- **【源修正】** 10-17 件「需修正 3」。

### P-4 论证方向：种子路线 vs v1.6 的关系表述
- **【前置条件】** SPEC 对种子路线的辩护词必须写「**避开 v1.6 已判死的线性融合路、继承其零泄漏纪律**」——种子＝节点级初值注入，作用路径为轨迹演化，恰是非线性生效路径（与 E9.6 结论「若融合增益存在，必须来自非线性机制」兼容）；**不得写「与 v1.6 同构/同一条先验线上的自然延伸」**（v1.6 先验是边级＋事后线性融合，注入点不同，结构不严格）。凡引 v1.6 线证据，必须如实携带负结果：v16 六臂 hybrid@λ(0.25/0.5/1/2) 全部 0.2941<0.4、`ge_0.4` 全 false、`pass` 全 false、`any_lambda_pass: false`；E9.6 凸组合融合在已测 λ 上只稀释（0.484→0.452），λ=2 表观增益为 anti-field 伪影。
- **【源锚】** `results/deposon_v16_llm_prior.json`；论文 E9.6 节。
- **【源修正】** 10-17 件「需修正 4」。

### P-5 可复核性：种子映射表冻结
- **【前置条件】** SPEC 起草前必须已设计「心哲范畴→初值」**固定种子映射表的预登记与版本化冻结机制**（表本体可在 SPEC 内定义，但冻结机制缺失则 SPEC 不得定稿）——否则「参数从哪来」审计链断在第 0 步，与已被否掉的「参数发生器」同罪（同一标准反身适用）。若 LLM 参与生成该表，须整套继承 `llm_prior.py` 红线：零泄漏 prompt（只给标签不给结构）、总预算≤2 次、响应落盘缓存（`results/llm_prior_cache.json` 体例）、无 key 抛 RuntimeError 严禁 mock；种子表验收件复用 `verifier/v5` 脚本体例。
- **【源锚】** `llm_prior.py`（7,466 B）；`run_v16_llm_prior.py`（13,423 B）；`verifier/v5/check.py`（commit `134cc6a`）。
- **【源修正】** 10-17 件「需修正 5」。

### P-6 范畴张力：三选一（＝边界 B-3，立项时 PI 拍板项）
- **【前置条件】** SPEC 起草「意图撤销/承诺度」相关章节前，必须已有 PI 就下述三选一的**在册裁定**（团队 0 代裁）：
  - **(a)** 意图＝不可逆承诺——偏离 Bratman 可撤销性，哲学锚改引 Schelling 式承诺装置线（诚实，但等于换了理论）；
  - **(b)** 撤销走 R 通道新增「折返再入射」机制——须预登记判死＋守恒账扩展设计（反射能量再入射的记账规则）；
  - **(c)** 撤销＝承诺度参数自身衰减（不占 A 通道，A 只管写入终局）——最贴对象件原意，但「承诺度衰减动力学」是 V5 **新增未审机制**，须明写。
- **张力根因**：仓内注册的承诺＝**博弈论式不可逆承诺装置**（Schelling 血统；论文 L18 原句：能量一旦凝入无限维 aether 不能回流、被淘汰路径的预算不能复活；工程 `dissipate()` 单调累计无 `recover()`）vs Bratman 意图＝**可重新考虑的规划态**（BDI 有 intention reconsideration 机制）。意图撤销在耗散通道（A）上无实现位。
- **【源锚】** 论文 L18 commitment device 原句；对象件第三环设计。
- **【源修正】** 10-17 件「需修正 6」（上游评审最强发现）。

### P-7 枚举与行级小修（三处）
- **【前置条件】** SPEC/对照件落笔时：
  ① 「仓内 V5 字样」枚举必须含 **235 件 `_v5_` 前缀族**（`git ls-files` 实测；命名裁定件 `57024f2cd30a` 定性为历史档案字面）——「无 V5 心哲主线内容」的主张精神仍立，列举面须全；
  ② qualia 红线行（B 档红线级）种子列必须为「—」，不得留候选（红线行留候选会锚定后续设计者，与档位自相矛盾）；
  ③ BDI/Bratman/Rao & Georgeff「工程锚点」必须标注为**外部生态资产**（仓内字面 0 命中；「意向性」仓内唯一命中系 ITT 统计义，误友已排除），不得写成仓内资产。
- **【源锚】** git 提交史＋`git ls-files` 计数；对象件映射总表 qualia 行。
- **【源修正】** 10-17 件「需修正 7」。

---

## 二、文献面结论并入（0 重做核验）

**引用源**：`shared/阿兰_心哲文献核验与交叉补扫_2026_10_17.md`（阿兰-文献调研员，2026-10-17；web 检索多源交叉比对出版社官网/PubMed/PhilPapers/ACL Anthology/arXiv 官方页/存档 PDF 版权页，0 编造、0 记忆填值；一手检索留档存其私有区 `v5_phil_scan/`）。**本节逐字转引登记，0 重做核验。**

### L-1 Putnam 年份勘误（SPEC 引用前置条件）
- 对象件原表：Putnam, "The Nature of Mental States" (1973)——**1973 无任何来源支持**（两轮检索 12 条来源零支持）。可查证两版本：
  - **1967**（原发）：原题 "Psychological Predicates"，in W. H. Capitan & D. D. Merrill (eds.), *Art, Mind, and Religion*（University of Pittsburgh Press）；
  - **1975**（重印改题）："The Nature of Mental States"，in Putnam, *Mind, Language and Reality: Philosophical Papers, vol. 2*（CUP）。
- **【前置条件】** SPEC/论文引用时在 1967/1975 中**二选一并全文一致，禁用 1973**。
- **体例注**（从核验数据直接可推，非新核验）：题名与年份须配套——沿用 "The Nature of Mental States" 题名则配 1975（重印版）；引 1967 则题名应作 "Psychological Predicates"（原发版）。

### L-2 交叉文献两方向 10 条（全部「可直接复用」档）

**方向①：LLM theory of mind 实证（5 条）**

| # | 文献 | 出处 | 一句话定位（阿兰原文口径） |
|---|---|---|---|
| T-1 | Kosinski, M., *Theory of Mind May Have Spontaneously Emerged in Large Language Models* | 2023, arXiv:2302.02083（另刊 Stanford GSB Research Paper 4086） | 正面证据方起点；此结论随后遭方法学反证，构成本方向争论原点 |
| T-2 | Ullman, T., *Large Language Models Fail on Trivial Alterations to Theory-of-Mind Tasks* | 2023, arXiv:2302.08399 | 反例检验：微小扰动即令 LLM 翻车，质疑涌现 ToM 的稳健性 |
| T-3 | Sap, M., Le Bras, R., Fried, D., & Choi, Y., *Neural Theory-of-Mind? On the Limits of Social Intelligence in Large LMs* | EMNLP 2022（2022.emnlp-main.248；arXiv:2210.13312） | 系统测评：LLM 显著低于人类，强调测验效度与 shortcut 风险 |
| T-4 | Shapira, N. 等， *Clever Hans or Neural Theory of Mind? Stress Testing Social Reasoning in Large Language Models* | EACL 2024（2024.eacl-long.138；arXiv:2305.14763） | 压力测试：部分 ToM 迹象但大量依赖数据偏差，支持「Clever Hans」假说 |
| T-5 | Strachan, J. W. A., Albergo, D., Borghini, G. 等， *Testing theory of mind in large language models and humans* | *Nature Human Behaviour* 8:1285–1295, 2024, doi:10.1038/s41562-024-01882-z | 顶刊实证：多样化 ToM 测试（含讽刺/暗示/失礼识别），GPT-4 与人类被试不可区分 |

**方向②：BDI/意图架构 × LLM agent（5 条）**

| # | 文献 | 出处 | 一句话定位（阿兰原文口径） |
|---|---|---|---|
| B-1 | Frering, L., Steinbauer-Wagner, G., & Holzinger, A., *Integrating Belief-Desire-Intention agents with large language models for reliable human–robot interaction and explainable Artificial Intelligence* | *Engineering Applications of Artificial Intelligence* 141:109771, 2025, doi:10.1016/j.engappai.2024.109771 | BDI×LLM 融合的应用正主：BDI 主体＋LLM 通讯层 |
| B-2 | Agiollo, A., & Omicini, A., *Integrating Machine Learning into Belief-Desire-Intention Agents: Current Advances and Open Challenges* | 2025, arXiv:2510.20641 | ML（含 LLM）融入 BDI 的系统化综述，related work 地图 |
| B-3 | Lawton, C., Sacharny, D., & Henderson, T. C., *A Self-Aware BDI Agent for LLM-Driven Reasoning: Architecture, Design, and Preliminary Evaluation* | 2026, University of Utah Kahlert School of Computing 技术报告（pub341） | BDI 作为 LLM 推理的结构化、持久、可验证外壳；注：技术报告身份，正式发表版待跟踪 |
| B-4 | Hu, P., & Ying, X., *Unified Mind Model: Reimagining Autonomous Agents in the LLM Era* | 2025, arXiv:2503.03459（18 页） | LLM 时代自主 agent 的理论认知架构（UMM 含意图层），BDI 之外的意图架构参照 |
| B-5 | Zuppiroli, S., Longo, C. F., Lippolis, A. S., 等， *The Belief-Desire-Intention Ontology for modelling mental reality and agency* | 2025, arXiv:2511.17162（2025-11-21 提交） | BDI 形式本体（模块化 Ontology Design Pattern）；「心哲节点＝本体类＋参数种子」的形式化先例 |

### L-3 未扫三方向（留待 V5 SPEC 立项后再扫）
- **machine consciousness（LLM/机器意识）**——未扫（上轮留档零星线索：Butlin 等 arXiv:2308.08708、Chalmers "Could a Large Language Model be Conscious?"、Andrews "Identifying indicators of consciousness in AI systems"，未核验未分档）；
- **功能主义争论**——未扫；
- **GWT×LLM**——未扫（上轮留档线索：Anthropic "A global workspace in language models"，未核验未分档）。
- 另：Sclar 等 "Minding Language Models' (Lack of) Theory of Mind: A Plug-and-Play Multi-Character Belief Tracker"（ACL 2023，2023.acl-long.780，arXiv:2306.00924，SymbolicToM）系阿兰件**附录条目**（未计入 5 条限额），留待立项后定是否纳入。

### L-4 其余 13 条锚点「核实无误」登记
Brentano 1874／Searle 1983／Bratman 1987／Rao & Georgeff ICMAS-95／Dennett 1987／Baars 1988／Dehaene & Naccache 2001／Rosenthal 2005／Chalmers 1996／Jackson 1982／Tononi 2004／Varela, Thompson & Rosch 1991／Clark 1997——题名/作者/年份/出处全部多源一致。
两条元数据注（SPEC 落笔时用）：
- Dehaene & Naccache（2001）：建议补出处 *Cognition* 79(1–2):1–37；官方副题作 "basic evidence and a workspace framework"；
- Rosenthal（2005）：PhilPapers 登记年标 2006 与出版社 2005 并存（元数据差异）——以 Clarendon Press 2005 版权信息为准。

### L-5 分档计数总表（与阿兰件一致）
| 部分 | 分档 | 计数 |
|---|---|---|
| §6 十四条锚点 | 核实无误 | **13** |
| §6 十四条锚点 | 待核实（Putnam 年份出入） | **1** |
| ToM 实证 | 可直接复用 | **5** |
| BDI×LLM | 可直接复用 | **5** |
| 其余方向（machine consciousness／功能主义争论／GWT×LLM） | 未扫 | **3 个方向** |

---

## 三、登记边界（B-1～B-3）

### B-1 组外件只读 0 改写
对象件 `upload/6ad32c18058badced5be298d_deposon_v5_心哲节点概念映射_2026-10-12.md`（8,374 B，sha `694131a3693b`）系组外 GLM Agent 思考材料：**只读、0 改写、0 修正、0 回传**——7 项修正与文献面勘误全部落在评审/归档件侧（本件与上游两件），组外件本体一字不动。后续一切沿用同纪律（同轮判死线哲学材料亦同）。

### B-2 V5 前驱 f44996f 已入仓（事实登记）
- V5 预告字面已于 **2026-10-12 12:36 随提交 `f44996f` 入仓**：`_september_workspace/results/_questionnaire_cards_intake_register_2026_10_09.md`（442,352 B）L323/L332——「V3 V4收官，V5开启前再刷，提前预告，LLM思维引入心智哲学节点下deposon相关参数种子值，沿袭V1~V4而更有野心」（卡答案 2026-10-08 15:28 提交）。
- **事实后果**：「仓库 0 V5 前驱」表述自 2026-10-12 起失效；该件为 V5 立项后官方表述对齐的**第一对照件**（种子值语义官方表述 ↔ 「参数种子值」字面的对齐度）。
- **现势补充**（时点 2026-10-18，鲍勃认证态刷新件）：预告字面仍是唯一在仓 V5 前驱——V5 主线/心哲文件 0 落仓、远端 main `74c7d76` 零前移、minimax 三项 0 回流。

### B-3 范畴张力三选一＝立项时 PI 拍板项
即 P-6：选项 (a)/(b)/(c) 全文照录于 P-6；**拍板权＝PI（2026-10-18 派单明示「立项时 PI 拍板项」），团队 0 代裁**；未裁定期 SPEC 意图机制节不得起草；裁定落地后须在 SPEC 内显式登记所选支线与代价（换锚/新增机制/新增未审机制）。

---

## 四、沿用面登记（非前置条件，SPEC 起草时可直接取用）

上游 10-17 评审件「可作 V5 SPEC 前置参考（条件修正后沿用）」五项＋配套约束，一并归档：
1. **三筛子框架**（可组合/可判死/立场透明）——须补第四面「**度量分辨力**」（E-27 判别四要件之④；引 E9.5 ±10pp 可检出差异教训预登记样本量），或并入筛子 2 扩为四筛子；
2. **种子＝心哲语义先验初值＋守恒律不动＋否掉「参数发生器」**——守恒恒等式是构造性的（Λ=1+g_eff+g_aether，T=1/Λ、R=g_eff/Λ、A=g_aether/Λ，对任意参数成立；逐路径能量审计最大偏差 2.220446049250313×10⁻¹⁶＝双精度机器 epsilon；两参数状态即二维初值槽，种子槽位天然存在）。「守恒律不动」为 SPEC 第一原则；
3. **qualia 红线处置**（不做/降格「现象报告节点」）——若采降格路线，判死读数须落到报告行为差异（操纵自变量下的报告内容变化）并预登记；
4. **档位三分法**（A/B/C＋根基）与 C 档「故意不进」的世界观边界写法——预声明载体在册：`docs/WORLDVIEW_GEOMETRY_LOOP_2026.md`（`1568b3dfe5ae`/10,327 B，立场声明体裁、自带判死期限）；A 档资格绑定「已给出判死读数草案（指标＋阈值＋基准＋裁决规则＋非退化构造检查＋样本量/可检出差阈）」，否则降 B 档；
5. **Bratman 线作主线、GWT 线作备选**的排序——两线须**对称携带各自负结果**（耗散零收益／场臂输随机：v1.5 物理场在语义边上 named_path 0.176 vs random 0.412）。
配套约束：终态差异类主张必须携带 **approximate 标签**（P1 dynamic≠BR 三档全判死；势博弈降级 approximate，有环图中位残差 0.669），不得写成定理级；判死协议审计链（逐路径 T+R+A=1 第三方可重算）可沿用。

---

## 五、生效与禁止事项

- 本件自归档时点起为 V5 面**唯一前置参考件**；上游两件 10-17 评审/核验件为证据源，保留不改。
- **生效链**：线索册/补件到位 → PI 定 SPEC 立项时点 →（若立项）SPEC 起草须逐条满足 P-1～P-7 与 L-1（Putnam 1967/1975 二选一）；P-6 三选一在立项时由 PI 拍板后，SPEC 意图机制节方可起草。
- **线索册/补件到位前 0 立项动作**（明示禁止清单）：不起草 SPEC；不生成种子映射表；不做心哲节点判死实验设计；不扫 L-3 三方向文献；0 改仓 0 推送（阶段性推送含现有待推 4 件系管理员另行统一安排事项，与本件内容无关）。

---

## 六、诚实边界

- 本件为**转写＋登记**性质：0 重做核验（文献面全部转引阿兰件）、0 新增评审判断、0 改写上游两件/组外件/仓内任何件；0 改仓 0 推送。
- 转写纪律：所有指纹/读数/行号以上游两件为准逐字搬运；仅 Putnam「题名-年份配套」一条为体例注（从阿兰核验数据直接推导，非新核验）。
- 未涵盖面（如实留白）：L-3 三方向文献（未扫）；P-6 三选一（未裁）；SPEC 本体（未起草）；阿兰件一手检索留档不在本件复制（存其私有区 `v5_phil_scan/`，`raw/A01–A17`＋`raw/B–H`＋`raw2/K01–K04`）。
- 时点：2026-10-18（本地克隆与远端均为 `74c7d76`）。

——爱丽丝（算法架构师），2026-10-18
