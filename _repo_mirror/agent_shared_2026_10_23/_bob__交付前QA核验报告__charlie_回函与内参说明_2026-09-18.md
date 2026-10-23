# 交付前 QA 核验报告：查理《致 MiniMax 回函》与《V3 终稿内参转呈说明》

- **执行**：鲍勃-实验分析师 · 2026-09-18 · 只读终审（0 LLM、零推断、挂载仓零改动）
- **对象**：
  - `shared/查理_致MiniMax回函_2026-09-18.md`（实测 214 行、22,495 B、SHA-16 `26a183b5945c8050`）
  - `shared/查理_V3终稿内参转呈说明_2026-09-18.md`（实测 35 行、3,119 B、SHA-16 `aee6d886bd58dd14`）
- **方法**：对管理员指定的 8 组权威源逐项确定性对回；全部 SHA/字节/页数/行数本终端实算；敏感信息模式扫描。零 LLM API、零联网、零推断；不改原稿。

---

## 一、终裁

**PASS**（7 项核对项 a–g 全 PASS；0 处数字/事实缺陷；3 条非缺陷口径备注见 §五）。

---

## 二、逐项核验结果（a–g）

| 项 | 内容 | 结果 |
|---|---|---|
| a | 全部数字与分母逐项对回（百分比、计数、R²、φ、d 值、p 值、字节数、页数、行数、引用数） | **PASS**（明细见 §四，全部对回，0 缺项） |
| b | 全部 SHA 前缀逐位核对（12 位与 16 位） | **PASS**（20 件实测全中：挂载仓 13 件＋FTFB 终版 4 件＋V3 链 3 件；被审 v3 快照另实测 4 件中 4 件一致） |
| c | verdict 标签口径（P-K 三方总判 FAIL 与 P-L v3 子项 GRAY 并存） | **PASS**（两处各自与源一致、无互斥：回函 OVERALL=FAIL 对回 P-K 报告 §1 与 rerun JSON `overall_verdict="FAIL"`；内参 GRAY 对回 V3 终稿摘要与 §5.5「未过预登记阈值 <1%，判定 GRAY」——前者为实验判死线总判口径，后者为论文整合子项口径） |
| d | 8 处缺陷清单与戴夫备忘逐条一致 | **PASS**（F-1~F-8 逐条对照 `戴夫_minimax双审复核备忘_2026-09-17.md` §五，判定语与数字逐字一致） |
| e | 发布边界表述与用户指令一致 | **PASS**（两件均载：本周公开仅 FTFB；V3 内参未公开、不得作为文献引用；〔W老师〕转呈；GitHub 工件 artifact 非文献；API key 永不入交付物在位） |
| f | 敏感信息扫描（key、通道凭据、内部工作流名） | **PASS**（令牌模式 `sk-/ark-/ghp_/eyJ/password/secret/api_key` 等 0 命中；内部 Agent 本名与门审子代理模型名 0 出现；文中 GLM/KIMI/coze/MiniMax 系 5 制品协作方公开事实，非内部工作流泄漏） |
| g | 两件文件交叉重复数字无冲突 | **PASS**（共有数字 10 组逐项一致，见 §四.7） |

---

## 三、指纹实测对回表（0 LLM 实算）

### 3.1 挂载仓 13 件（`/home/z/my-project/upload/mount_agent_directory/deposon-repo/`，全程只读）

| 文件 | 回函所载 | 本端实测 | 裁定 |
|---|---|---|---|
| results/ftfb_pass1_background_methodology_audit_2026_09_17.md | 8257 B、`70bd41d9722d` | 8257 B、`70bd41d9722d` | 一致 |
| results/_ftfb_pass2_results_limitations_audit_2026_09_17.md | 11390 B、`cfab992cf939` | 11390 B、`cfab992cf939` | 一致 |
| results/_p_k_v3_three_way_rerun_2026-09-17T08-23-41Z.json | `05ff758ae921` | 12992 B、`05ff758ae921` | 一致 |
| results/_adendum_O_pk_v2_three_way_v2_20260917_133852.json | `a30ff093305d` | 1970 B、`a30ff093305d` | 一致 |
| docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md | `4ffb21bb6bfa` | 8526 B、`4ffb21bb6bfa` | 一致 |
| results/d7_5anchor_60cells_9model_verdict_2026_09_18.json | `4505cca79c15` | 2456 B、`4505cca79c15` | 一致 |
| docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md | `977fe1b48f75` | 19751 B、`977fe1b48f75` | 一致 |
| results/deposon_v3_v7_summary_2026_09_11.json | `063ac8d00542` | 25049 B、`063ac8d00542` | 一致 |
| corpus/v20/by_model/kimi/index_v2_2026_09_16.json | `efe05ad775de` | 24150 B、`efe05ad775de` | 一致 |
| corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json | `268ab1239a8a` | 19685 B、`268ab1239a8a` | 一致 |
| corpus/v20/by_model/GLM_2/glm_artifact_v_2026_09_16.json | `39732a92b5c9` | 13150 B、`39732a92b5c9` | 一致 |
| corpus/v20/by_model/coze/coze_artifact_v_2026_09_16.json | `fee04170aa73` | 10978 B、`fee04170aa73` | 一致 |
| corpus/v20/by_model/minimax/artifact_v_2026_09_16.json | `9e1ccbdceacc` | 25347 B、`9e1ccbdceacc` | 一致 |

### 3.2 FTFB arXiv 终版四件（`shared/戴夫_FTFB_arXiv终版_2026-09-18/`）

| 工件 | 回函所载 | 本端实测 | 裁定 |
|---|---|---|---|
| fiction_that_feeds_back.pdf | 24 页 387,751 B、`cc155e19ab574b30` | 24 页（pdfinfo）、387,751 B、`cc155e19ab574b30` | 一致 |
| fiction_that_feeds_back.tex | `9de366a6c4d60443` | 102,549 B、`9de366a6c4d60443` | 一致 |
| ftfb_arxiv_final_2026_09_18.tar.gz | `845dbe8555be47c1` | 36,701 B、`845dbe8555be47c1` | 一致 |
| arxiv_metadata_2026-09-18.txt | `ea23bdf9a03e72bb` | 3,360 B、`ea23bdf9a03e72bb` | 一致 |

元数据表内容实测：摘要 **1849 字符／266 词**（arXiv 1920 上限，余量 71）、subjects **cs.AI（primary）＋physics.hist-ph＋cs.CY**、License **CC BY 4.0**、Comments **24 pages, 2 tables, no figures**、PDF Author=Qihao Yuan（实名）、pdfTeX-1.40.29、A4——与回函 §5.1 逐项一致。终版 tex 实测 56 条 `\item[R…]`（R01–R56）、R55=Helmholtz（Atkinson 译本 2026-09-17 全文抓取核验）、R56 匿名配套条目（camera-ready 恢复）、R13/R14 `[IDENTIFIER-PENDING]` 保留——与回函 §2.3 一致。

### 3.3 V3 终稿链三件

| 工件 | 内参所载 | 本端实测 | 裁定 |
|---|---|---|---|
| 戴夫_deposon_V3终稿全文_v3_2026-09-18.md | 311 行、`b5323d44d54bd2c1` | 311 行、43,403 B、`b5323d44d54bd2c1` | 一致 |
| dave-v3-final-20260918/deposon_v3_final.tex | 48,607 B、`94251c11ba19` | 48,607 B、`94251c11ba19`（16 位 `94251c11ba19c36b`） | 一致 |
| dave-v3-final-20260918/deposon_v3_final.pdf | 12 页、821,560 B、`6fca1de41689df50` | 12 页（pdfinfo）、821,560 B、`6fca1de41689df50` | 一致 |

### 3.4 被审 v3 快照（回函 §2.3 所引，交叉实测）

| 工件 | 回函所载 | 本端实测 | 裁定 |
|---|---|---|---|
| ftfb_v3.pdf | 23 页 356,123 B、`2d9edc8c7303` | 356,123 B、`2d9edc8c7303` | 一致 |
| ftfb_v3.tex | `d060f75dbe9f` | 93,324 B、`d060f75dbe9f` | 一致 |
| 剥离正文（源稿 L9–L391） | `543479649b3e` | `sed -n '9,391p'` 复算 `543479649b3e` | 一致 |
| 源稿全文 | （戴夫备忘口径 `7a0a98289588`） | 416 行、`7a0a98289588` | 一致 |

---

## 四、数字与事实对回明细（按 8 组源）

### 4.1 源① 鲍勃_V3 终稿数字事实核验包
- **85.0%＝51/60**：existing_30 T=25/R=5＋new_30 T=26/R=4→T=51/R=9/A=0、residual=0、`pass_rate_60=0.85`、STRONG_PASS——回函 §3.1.1 与核验包 ①-1 逐字一致；87.0% 旧值漂移口径一致。
- **Adendum 17 项**：状态口径 11 PASS＋2 GRAY（H、O）＋1 UNVERIFIED（A）＋2 PARTIAL（F、G）＋1 FAIL_NO_MODEL（K）＝17；成本口径 10 零＋7 中（B/C/D/E/M/N/O）＝17；A–Q 唯一字母 17 文件——回函 §3.1.2 一致；旧叙述「7＋6＋3＋1＋1」加和 18 系笔误的披露一致。
- **P2 降格**：3/5（分母 5）；glm53/qwen3/mistral 完整；doubao-seed-2.0-lite 10/30 INCOMPLETE（分母 30）；GPT-4o 不可达；闭源 gpt-5.6-sol/claude-sonnet-5/gemini-3.7-flash 加速器补齐；OR×OR 1/6（分母 6＝两两组合数）、1 true＋5 false、GRAY——回函 §3.1.3 一致。
- **D7 四路径**：P-A PASS（540 守恒 T=384＋R=78＋A=78、9/9、51/60=85.0%、8 PASS＋1 GRAY deepseek-v4-pro）；P-C FAIL_H0（R²=0.1986/0.2670）；P-E PARTIAL_PASS（6 PASS＋2 GRAY＋1 FAIL；D_fix2 8/1/0）；P-F PASS（45/45＝9×5、T=41/R=0/A=4）——回函 §3.2 表逐格一致。
- **P-L v3 三态**：尺寸缩放 FAIL（R²=0.7447）；β CI 重叠降格 PASS（开源 3/3、闭源 3/3，各分母 3）；判官误报率 4.4%（2/45，分母 45）GRAY——回函 §3 与内参「三、关键结论速览」均与核验包 ③ 一致。

### 4.2 源② 戴夫_minimax 双审复核备忘
- Pass 1 实测 8257 B/`70bd41d9722d`、Pass 2 实测 11390 B/`cfab992cf939`——回函 §1.1 一致（本端亦实测一致，见 §3.1）。
- 「40+ 项全绿」「凡可程序化重验的论文侧断言 100% 复算吻合」；Pass 1「全 PASS／0 FAIL／0 GRAY」、Pass 2「4 PASS＋1 GRAY／无 FAIL」；「0 FAIL 获支持」——回函 §2.1 一致。
- 不可复核项 4 类（novelty/GRAY 学术判断；「0 LLM 调用/未调 API」行为性自我声明；Pass 2 自报 SHA-12；审计时间戳）——回函 §2.1 末段一致。
- **F-1~F-8 逐条**（自报 `17AF43E49D57` vs 实测 `70bd41d9722d`；15 个 @ 中 4 个 `@{}`＋1 个 `hybrid_norm@0.5`；Pass 2 wikisource URL 无 @；"confidential channel until camera-ready" 0 命中、实际为 §7 引言且非 §7.1 末段；两条引语非字面子串；"outright" 仅一处指 M3；R36 题实在 References；占位符未填 11390 B）——回函 §2.2 表 8 行逐条一致；判定语「集中于自报指纹与逐字引语层……主结论恰好未被推翻」一致。
- 被审 v3 快照口径（54 条 R01–R54、23 页 356,123 B、tex/剥离指纹）——一致。

### 4.3 源③ GLM 增补实验设计提案
- φ=0.6591（2×2 计数 a=20/b=2/c=2/d=6）、Fisher 精确检验双侧 p=0.0011、约 3.5σ——回函 §3.3(b) 与提案 §2.4/§4.2 一致。
- 空带 n=30 [0.9354,1)、n=60 收窄 [0.9672,1)——一致；三档判死表（<0.95 成立／[0.95,1.0) 补测／=1.0 证伪）与邀请函 §4 原文逐字核对一致。
- v2 同序陷阱：plugins runner L64–L66 代码实证、25 网格 R² 全 1.0、代数恒等式非测量——一致；ρ_S=1 ⟺ 30/30 逐 cell 恒等（提案 L104）一致。
- minimax 基线 run COMPLETE 22/30（分母 30）——一致。
- Backbone 三选（DeepSeek V4 `deepseek-v4-pro-ga-260813` sanity 200×2＋catalog×4＋缓存三重证据；Qwen3 `qwen3-32b-20250429`；NVIDIA `nvidia/nemotron-3.5-lightning` 仅 reference_only）；I1–I5（gsm8k_1–15＋stq_1–15、question_sha12 30/30、I2 模板、I3 抽取、I4 判分 1e-3/capitalize、I5 0.0/1024/30 s）；四层流水线与 repo→archive 双基查找；方向 A 7 槽位名单＋kimi-k2.7-code 17/30 PARTIAL＋实际补跑池 6；方向 B（恰等价 1 个单向翻转、COMPLETE 且 timeout cell ≤1 等四条件、gsm8k 100 题/stq 99 题）；方向 C（S2a K=3 默认建议开启；S2b τ₀=0.7/K=5/双侧对称/须拍板）；方向 D（不开 minimax.chat 新通路）；方向 E（30/45/60/100）——回函 §4.1/§4.2 全部逐项一致。

### 4.4 源④ P-K 盲测 GLM 槽位产出
- OVERALL=FAIL（1/4 判死线未过）——回函 §3.4 与报告 §1 一致；rerun JSON 实测 `overall_verdict="FAIL"`、`FPR=0.0444`、`FNR=0.0`、`SP_t=1.0` 一致。
- FPR=2/45=4.4%（分母 45＝GLM 23＋KIMI 22）；SP_t=1.0000（判死线 ≥0.7）；FNR=0.0000（26/26，判死线 <1/20）；抗洗白 43/45=0.9556（判死线 ≥0.6）——一致。
- 穿透件 GLM-N10 `bob_pd2_repro_results.json` d=1.3137、GLM-N11 `rerun_diff_summary.json` d=1.8832；排序缝隙 0.018（d=1.314 高出自家带最大 d=1.296）；最小非零 FPR=1/45=0.0222>0.01；6 件 JSON 型外来件中 2 件穿透——报告 §2/§3 一致。
- **T=2.0（z_cap=8、std_floor=1e-6）**：基线 JSON `results/deposon_p_k_cross_subject_fingerprint_blind_test_2026_09_16.json` `preregistration.z_cap=8`、`preregistration.std_floor=1e-06` 本端实测命中；T=2.0 与 P-K 报告 §4「判别规则零改动（d<T=2.0 判自家）」一致。
- 原二方 4/4 判死线 PASS 不受影响——报告基线声明一致；§4.3 预登记修订三项与报告 §6 一致。

### 4.5 源⑤ P-D 两件
- V0.1.1 A1 假性 FAIL（2026-09-04，`--missing` 传入不存在的 `docs/SPEC_GT8C.md`→A1 不删除→compute_root 正常返回→verdict=FAIL→「任一 FAIL → V0 死」误杀；V0.1.2 改「无参＋临时副本自建」；出处 P_E_DOUBAN_EMBEDDING_V0_SPEC.md L50、P_D_FINGERPRINT_V0_SPEC.md V0.1.2 注记）——回函 §3.5(a)1 与事实备忘一.1 一致。
- exp_3_4 失败（2026-09-16 12:35，corpus/v20/index.json 缺 captions、"only 0 captions, need 22"、与 B3 线互为镜像；出处 D7_PRE_DISPATCH L59、键 exp_3_4_p_d_supplement）——一致。
- dual_24bit 名 24bit 实 9 hex=36 bit；三套 hash 口径（V0 spec R1 文件字节[0:12]／V0.2 byte_hash=caption_id[0:12]／stranger runner caption 文本 12 hex 6+6 拼接判非标、裁定 spec 优先）；B3 链 22/22（分母 22 caption）、root `75596bbabdb8`、锚链 `c4cae1ed9ee5`；裁定 spec 升级（替换/并行不推荐、零重算 frozen 零触动）——回函 §3.5(b)(c) 与 P-D 机制技术分析备忘 N1/N2/③ 逐条一致。

### 4.6 源⑥ FTFB 终版刷新说明＋arXiv 终版目录
- 指纹链四件、24 页 387,751 B、56 引（R01–R56）、摘要 1849 字符/266 词、subjects、CC BY 4.0——回函 §2.3/§5.1 与刷新说明指纹链表一致，且本端四件实测全中（§3.2）。
- 被审快照 23 页 356,123 B、54 引——一致（§3.4 实测）。
- R3 清单项（M4 行判据来源显式化、「structural isomorphism」全文降级为「constructed structural parallel」）——R3 逐项修订说明②「M4 行重写」在位、终版 tex 含 2 处「constructed structural parallel」；R55 Gutenberg #77725（Atkinson 译本 2026-09-17 17:39 落盘）——R3 说明⑤在位。回函 §2.3 一致。

### 4.7 源⑦ V3 终稿门审汇总裁决＋成品包／源⑧ 邀请函
- 12 页双盲、9 章＋44 条引用＋双语摘要（228 汉字）——本端实测：pdfinfo 12 页、正文 9 章（§1–§9）、References `[1]`–`[44]` 连续 44 条、中文摘要 CJK 汉字 **228**——内参说明一致。
- R1 修订 19 处——V3 终稿 md L309「除清单 19 处外正文零改动」＋《V3 R1 修订响应》一致。
- 终版门审：A 路 9.7/10、B 路 10/10、阻塞 0／Major 0／Minor 0——汇总裁决 L30 一致；SHA 链三件（md/tex/PDF）实测全中（§3.3）。
- 五线坐标系（§2）与 DAS-2M 零 LLM 检索线（§6）——V3 终稿章节结构一致。
- KT-C1 消歧：外部侧 R²=0.0007（外部源件所载，非本仓实测）vs 本仓 KT_C1 R²=0.1986/0.2670 FAIL_H0——V3 终稿 §4 两处消歧在位，内参说明「四、名称消歧」一致。
- 7 铁律（邀请函 §4 原文逐条）：API key runtime 读取不落盘不入检测规则／国内走火山／海外走 OpenRouter（限非 OpenAI/Anthropic/Google）／节省原则小模型 30 cells／钥匙不写入 markdown/code/memory／OpenRouter 仅备用／不动 verifier 内建脚本目录——回函 §6.1 七条逐条一致；实验纪律（0-LLM hashlib 复算层、18 frozen 零触动、诚实降级禁止修饰）与邀请函「实验纪律」三款一致。
- 18 frozen 18/18 PASS（`results/_v3x_18frozen_remeasure_2026_09_16/` 目录实测在位）；schema 21/21（16 文件锚＋5 P-G 种子锚）；22 题注双指纹 22/22；4 plugin spec 0 触动——回函 §3.6 一致。
- V3X GitHub 工件 artifact 非文献、内参仅供〔W老师〕内部参考勿外传勿引用、以正式发布版为准——内参说明「五、保密请求」与用户指令一致。

### 4.8 交叉重复数字（g 项）
两件文件共有数字 10 组：85.0%＝51/60、540 守恒、R²=0.1986/0.2670、45/45（9×5）、4.4%（2/45）、17 项（11+2+1+2+1／10+7）、3/5 与 1/6、开源 3/3 闭源 3/3、12 页双盲、V3 未公开口径——全部一致，0 冲突。

---

## 五、备注（3 条，均非缺陷，不改原稿）

1. **英文摘要词数口径**：内参说明「英文摘要 235 词」与门审 A 路一致，本端 whitespace 分词实测亦为 235；门审 B 路记录为 230–237 区间、门审本端机械核验记 230，系分词算法定义差异（门审记录内两读数并存），不构成与源的冲突。
2. **被审快照指纹列举数**：回函 §2.3 列被审 v3 快照 3 件指纹（PDF/tex/剥离正文）＋54 条引用池；戴夫备忘口径另有源稿全文 `7a0a98289588` 与 compile_verification `62d86debeeea`。所列项全部正确，属选择性列举，无错漏。
3. **铁律 4 转写**：回函「不一次跑大网格」对邀请函原文「不一次跑 300 cells」为同义概括转写，语义无损。

---

## 六、纪律自查

挂载仓全程只读（本轮零写入/零移动/零重命名）；0 LLM API；零联网；零推断；两份原稿未做任何改动（本报告为独立核验件）。全部实测命令可重放。

**终裁：PASS——两件交付物数字与事实层可放行。**

—— 鲍勃-实验分析师 · 2026-09-18 · 交付前 QA 终审
