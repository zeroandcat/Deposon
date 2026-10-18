# 爱丽丝 · 仓态进展与实验前置事实核查（匿名只读 · 2026-10-18 晚）

> **令源**：管理员 21:59:46 派单（PI 令「核查进展、核查实验面前置，进而更新第三作」之事实核查面）。
> **纪律基线**：匿名只读（0 PAT · 0 写 · 0 改仓 · 0 判定 · 0 代裁 · 0 落终判）；既有件一律只读；本件仅登记「在仓／不在仓／指纹／登记件字面」之事实。
> **核验时点**：2026-10-18 22:0x–22:3x（+0800）；远端 HEAD 见 §2。

---

## §0 方法与口径

- **匿名访问**：`git ls-remote`（0 凭据、禁用 credential helper）＋ `git clone --filter=blob:none`（部分克隆，blob 按需实取）对 `https://github.com/zeroandcat/Deposon.git`；全程未使用 PAT（令牌字面未出现在本棒任何命令）。
- **指纹口径**：SHA-256 前 12 位（`hashlib.sha256` 同口径）＋字节数；树文件计数用 `git ls-tree -r --name-only`。
- **引文字面**：凡引登记件自报状态者，标注件名与节次；自报值未经我方复核者不采为实测（「转引」与「实测」分列）。

---

## §1 远端仓总体现势（匿名面）

| 面 | 实测值 |
|:--|:--|
| 远端 HEAD | `75a8fbb04928712d31f5466d7907aae1b064e655`（＝`refs/heads/main`） |
| 分支/标签 | 仅 `main` 一支；0 新分支、0 标签 |
| 全树规模 | 3,458 件（c153c20 与 75a8fbb 两时点同值） |
| 顶层结构 | `_repo_mirror/` 3,027＋20 中文名件；顶层 `results/` 104、`verifier/` 78、`docs/` 57、`reviews/` 33、`corpus/` 24、`tests/` 22、`paper/` 11、`letters/` 7、`tools/` 2、`deposon_team/` 2 等 |

**波界时间线（实测）**：74c7d76（10-12 21:13 第七波）→ daf7033（10-18 10:24 我方晨推 8 件）→ **KIMI 物流 393 提交**（锚点：5d31b4be 前缀改名 16:12 · 739a7daf 509 覆写 16:50 · 713f2f31 批次三回执 16:59，均 +0800）→ 24e3e6c（20:44 我方 337 件修复）→ c153c20（20:49 我方登记件）→ **75a8fbb（21:56 远端现 HEAD）**。

---

## §2 c153c20 之后远端新提交/新件·逐件清单

**新提交恰 1 件；新件（A）0 件。**

| 项 | 实测明细 |
|:--|:--|
| 提交 | `75a8fbb`（作者 zeroandcat · 2026-10-18 21:56:32 +0800）——鲍勃扩大脱敏字面扫波（令源：PI 2026-10-18 夜令） |
| 改动构成 | **1,098 件全 M**（commit message 自报 8099 处替换/1084 文本件＋14 pyc 同长填充＝1084+14；实测 diff-filter：A=0 · D=0 · R=0）；树 3,458 件前后不变 |
| 与回执对账 | 远端 HEAD＝75a8fbb 与鲍勃 22:05《扩大脱敏面修复推送回执（简办）》（shared/）所报一致 |
| **KIMI 后续波** | **0**——c153c20 后无任何 KIMI 提交；KIMI 物流止于 713f2f31（16:59）；亦无第二 remote 面（仅 main 一支） |

> 附记：c153c20 本身新增件＝1（`_repo_mirror/results/_bob_repo_reconciliation_509repair_experiment_register_2026_10_18.md`，实测 SHA-12 `c10cc47dc813`/13,821 B，与派单转引值逐位相符）；713f2f31→c153c20 全程仅此一 A。

---

## §3 重点现势核查（六项逐件）

### 3-1 线索册 v0.7 —— **不在仓**

- upload 通道 20:14 到件：`dualtrack_paper_clue_book_v0-7_local_remote_2026_10_18.md`，69,901 B，SHA-256 `882309257b0f0120373da7ee8a8f0f1355ea37e99eca94e722041399aa9a65e3`（本棒实测）。
- 远端全树 0 命中：`clue_book/dualtrack/v0-7/v0_7/_v07/线索（中文名）`各字面均 0 命中（中文名件全列 20 件亦无）。
- 仓内相关既有件仅登记面：`_clue_book_v06_backfill_and_dual_version_register_2026_10_12.md`、`_clue_side_dual_and_glm_commission_open_register_2026_10_12.md`。
- **通道先例（仓内登记件字面）**：v0.6 双版本登记件结论「`_september_workspace/letters/` 0 命中 ⇒ 委托本体／线索册不可远端直取 ⇒ 必随包」——即 v0.6 本体亦未入远端仓（KIMI 侧本地 letters 通道，指纹 `8b2a6380edf1`/81,707 B 系该件自报转引）。

### 3-2 GLM 委托 v0.7 —— **不在仓**（补充委托 v0.4 同判）

- upload 通道 20:14 到件：`commission_glm_dualtrack_paper_v0-7_2026_10_18.md`，70,048 B，SHA-256 `07e068165dd559ce5825ea713a5913be3e87dd00a4621e64f76596800a4bb753`（本棒实测）。
- 远端全树 0 命中（同 3-1 口径）。仓内相关件仅 v0.4 关联之 KIMI 侧登记面：`_commission_v04_approval_rulings_effect_2026_10_18.md`、`_commission_v04_ghost_reference_erratum_2026_10_18.md`（其「v04」系 KIMI 上传委托 v0.4 线，源件 `letters/_commission_kimi_upload_2026_10_18_v0.4_draft.md`（61,027 B/`51ca14265086`，转引）亦不在远端仓）。
- 附记（第三件，同批 20:14）：`commission_glm_supplement_509_repair_v0-4_2026_10_18.md`，59,400 B，SHA-256 `591d5ee04d92d757eba43d2bf5a0a6e22a195554b8145e3920c8fb1a2a686226`（本棒实测）——远端 0 落仓。

### 3-3 minimax G-E01/E07/E08 三项回流 —— **0 回流（维持 10-18 晨结论）**

- **树内 minimax 名面全列 11 项**（实测）：`corpus/v20/by_model/minimax/artifact_v_2026_09_16.json`、`deposon_team/plugins/_audit|_build|_fix_minimax_extract_2026_09_16.py`（3）、`deposon_team/products/minimax_artifact_v_2026_09_16.json`、`results/deposon_volcengine_minimax_m3_30cells_2026_09_10.json/.py`（2）、`results/_bob_minimax_commission_family_intake_register_2026_10_12.md`、`results/_r5_spec_pack_retrieved_2026_10_13/鲍勃_minimax实验委托规格包_2026_10_12.md`（仓内副本实测 SHA-12 `bb66c577673b`/14,758 B，与 R-5 取回登记所载相符）＋同名 `.asset.json`——**除规格包及登记件外均 9 月既有；0 件 10-18 新结果件**。
- 三项委托结构（规格包 §0 字面）：G-E01（P-B V0 主实验）、G-E07（Task B 新轮·待 PI 定义）、G-E08（N-26 续跑·待 PI 定义）＝minimax 委托面 3 条。
- 现势依据（仓内今晚登记字面）：G-E07/G-E08 候 G-D06/G-D07（PI 定义）0 定义 0 开跑；G-E01 候 prereg 7 要件冻结＋G-E02/G-D03 前置——三项执行就绪度均为待裁/待输入（c153c20 §4）。
- upload 通道 10-17 后到件仅 PI 三件（20:14）——minimax 回件 0 到件。

### 3-4 G-D 裁定件 —— **不在仓（仓面 0 件）**

- 全树 G-D 专名裁定件 0 命中；pi_rulings 卷（v1–v94，2026_10_13–10_18）系 PI 卡片答面登记，v94 实测 0 处 G-D0 提及；综合待裁滚动册（71 项＝A 类 59＋新 12）实测 0 条 G-D 条目。
- 仓内登记字面：v1.1 计划 §G-D 表列 G-D01..D10（D 族＝PI 裁决型；G-D03 行「P-B 索取单 5 项未决 `19099ecb3c46`…本周立即（呈报即启）」）；c153c20 §4 列「G-D01..D10＝非我方面（PI 裁决型）」「G-D04 未裁（G-E05/G-E06 前置）」「G-D06/G-D07 候 PI 定义（G-E07/G-E08 前置）」。
- 10-12《待裁项团队决议案》（`4228142806c5`，v1.1 计划 §漏斗③转引「D01–D10 全裁＋G-D03 经 PI 双裁定闭合」）不在远端仓（全树 0 命中，系群侧件）。

### 3-5 prereg 冻结件 —— **锁值件在仓；GE01 七要件冻结仍草案态；主实验 prereg 未冻结**

- **在仓锁值/预登记件（实测）**：`_prereg_lock_v1_epsilon_lu_klm41_register_2026_10_15.md`、`_prereg_lock_v2_h_epsilon_gamma_taucert_u_register_2026_10_15.md`（v2 自报 33,312 B/`4c782fc8566b`）、**`_prereg_lock_v2a_t5_completion_register_2026_10_15.md`**（现指纹 `404d4fbeef40`/46,621 B）、`_prereg_caliber4_epsilon_revision_2026_10_15.md`、`_ge01_prereg_5anchor_v2/v3_lock_register_2026_10_15.md`（2 件）、`_ge01_prereg_5anchor`（draft/register/approval，10_13–10_14）、`_ge01_prereg_seven_requirements_draft_2026_10_13.md`（现指纹 `525999b86410`/39,305 B；10-15 审计件转引值为 39,337 B/`0a031a9795a9`，现值差 32 B，差异事实登记 0 判成因）。
- **锁件自报状态（字面）**：v2a「T5 补全四面落账完成…**含 3 面开口未成就**（§6）· ⛔ 0 宣告①毕 · **0 更新 G-E01 开跑核验面**」；「15 格之 H/ε* 全齐（T1/T2/T3/T5＝20/2、T4＝10/1）」（v17 卡答转引）；锁值权源＝PI 2026-10-15 16:35 交互卡 Q1 逐字「锁 H_T5=20、ε*_T5=2（推荐）」。
- **七要件草案自报（字面）**：「草案·候 PI 核准」「🔴 0 宣告 7 要件可闭」「G-E01 就绪判定＝待预登记（0 可直接释放开跑）」；要件②决策数 H 与⑤5 锚 JSON 之锁定「客观受外部到位制约」。
- **今晚就绪登记字面**：E 族 prereg 未冻结 0 跑纪律维持（c153c20 §1/§7-6：「若 PI 欲今日开跑任一项，须先冻结对应预登记（G-E01 7 要件清单在 10-18 登记件 §5.3）」）。

### 3-6 letters 目录 —— **现 7 件；c153c20 后 0 新增**

- 各时点实测：74c7d76＝6 件 → daf7033＝7 件（＋鲍勃晨推 `_bob_minimax_delegation_reply_third_supplement_2026_10_12.md`）→ 713f2f31＝7（KIMI 波 0 变动）→ **75a8fbb＝7（现势）**。
- 现存 7 件全列：`_bob_minimax_delegation_reply_third_supplement_2026_10_12`、`_claude_pending_pi_gaps_closeout_reply_2026_10_11`、`_codex_c4_values_followup/_codex_c4_values/_codex_c4_values_unblock_reply_2026_10_10`（3）、`_codex_theory_derivation_reply_2026_09_30`、`_v5_rj5_external_rederive_reply_codex_2026_09_29`。
- **结构性事实（仓内登记件转引）**：KIMI 侧本地 letters 通道另载裁定合卷（`_final_rulings_compilation_kimi_2026_10_18.md`，`832E69EB49A4`/37,950 B）、KIMI 预执行核准函（`87a61f5ecc41`/7,958 B）、Gemini4 往返函、线索册/委托 v0.5–v0.6 本体等——**均未随远端仓**（远端 letters/ 0 命中，批次三回执与 v0.6 登记件字面佐证「必随包」通道）。

---

## §4 实验前置与外部交付回流依赖项（重点展开）

### 4-1 E 族 9 条就绪现势（c153c20 §4 逐字转引·今晚 20:49 登记）

| 族 | 项 | 今日可跑 | 登记字面前置 |
|:--|:--|:--:|:--|
| E | G-E01 | 否 | prereg 7 要件未冻结（D 理论输入/实例键/决策数/加权律/5 锚/计算器重建）＋G-E02/G-D03 前置——0 提前开跑纪律 |
| E | G-E02 | 否 | 理论交付物（calculator＋5 锚）外部侧未到位——非我方可跑面 |
| E | G-E03/G-E04 | 否 | 需另立预登记（沿 GT 判定件同款纪律）——prereg 未冻结 0 跑 |
| E | G-E05/G-E06 | 否 | 前置 G-D04（扩词清单入锁＋缺字段补记规则批 G-R06）未裁 |
| E | G-E07/G-E08 | 否 | 候 G-D06/G-D07（PI 定义）——0 定义 0 开跑 |
| E | G-E09 | 否 | 候 PI 定义另立预登记——0 擅改既有判据字面 |

**36 条总判（该件 §1）**：今日可跑实验面＝0 项；「minimax 待回流项（G-E01 前置之理论输入 u\*(a_t)/L/U 界、G-E02 calculator 交付）：如实登记为非我方可跑面——回流时点 0 保证（外部交付线）」。

### 4-2 外部交付回流依赖项清单（逐项现势）

| 依赖项 | 委托/规格面 | 回流现势（实测＋登记字面） |
|:--|:--|:--|
| minimax G-E01 主实验 | 规格包已入仓（副本指纹相符 §3-3） | **0 回流**；候 prereg 7 要件＋G-D03＋G-E02 理论输入（三前置全开口） |
| minimax G-E07/G-E08 | 规格包已入仓 | **0 回流**；候 G-D06/G-D07 PI 定义（0 定义 0 开跑） |
| Gemini4 · GE01 理论输入（T1–T5 面理论值/口径核） | 委托 dispatch＋draft **在仓**（10-15） | **回函已到 KIMI 本地 letters 通道**（`REPLY_FROM_GEMINI4_GE01_THEORY_INPUTS_2026_10_15.md`，44,520 B/`44311ade19de`，核验件转引）——**回函本体不在远端仓**；仓内核验登记件在（`_gemini4_reply_verification_register_2026_10_15.md`，现指纹 `4fa15c554d93`/33,403 B），自报「候 PI 裁 · ⛔ 0 采认」 |
| codex · G-E02 calculator/5 锚 | v1.1 计划字面「来源已定未到位」 | **镜像波后仓内已有实体**：`_repo_mirror/tools/distortion_calculator.py`（实测 50,896 B/`ae7ff6e0bac5`）、`_ge01_prereg_5anchor.json`（10,701 B/`4b020eb04605`）＋v2；10-13 七要件草案时点该资产曾登记「仓内缺失·KTB1」——现已在仓（差异事实登记）；**采认/冻结面未毕**（§3-5 锁件自报 3 面开口） |
| G-D01..D10 裁定 | PI 裁决型 | **仓内 0 裁定件**（§3-4）；G-D04/G-D06/G-D07 系当前实验链之未下面 |
| prereg 七要件冻结 | GE01 开跑硬门 | 草案态（10-13）＋锁值件三面开口（10-15）——**未冻结**（§3-5） |

### 4-3 KIMI 物流（c153c20 前既成）对实验前置面之资产性变化（实测归纳）

- 镜像波（5d31b4be 及此前 726＋53 件）使 KIMI 本地资产**首次入远端仓**：calculator/exp_harness（`_repo_mirror/tools/`，现指纹 50,896 B/45,590 B）、`pi_rulings/` 卷 v1–v94、10_13–10_17 结果登记面（AF/锚漂移/KD 族裁定效力件/批次审判件/决议效力件等）、R-5 规格包副本、GLM 证据解包件（`_glm_evidence_unpacked_2026_10_13/`，含 S3/D1/T-1 判定与 v3_s prereg 等 10 件）。
- 批次三（713f2f31）新增今日件：`_batch3_execution_receipt_kimi_2026_10_18.md`（现指纹 `bb029b086ab6`/140,693 B）等 56 件丙档。
- 以上均为**文件在仓之事实**；其采认/效力/冻结判定面不在本棒范围（0 判定）。

---

## §5 论文更新（第三作）关联面

- **输入件现势**：线索册 v0.7＋GLM 委托 v0.7＋补充委托 v0.4 三件均**仅 upload 通道**（20:14，指纹见 §3-1/3-2）——远端仓 0 落仓、KIMI 后续波 0 发生（§2）。
- **仓内第三作相关既有件**：`paper/deposon_paper_unique_thread_v10_2026_10_18.md`（查理 v10 唯一脉络稿，实测 168,605 B/`9399019d4f8e`，与 shared 同件同值）；`paper/` 其余 10 件（final_cn/en、v1、v2X 系、references.bib、FIGURE_LANGUAGE_POLICY）。
- **裁定面输入（在仓）**：pi_rulings v1–v94、综合待裁滚动册 71 项（现指纹 `525ae3cbc2a7`/104,318 B）、KIMI 预执行终裁效力件（`_kimi_preexec_final_rulings_effect_2026_10_18.md`）、v04 两件——均可作更新第三作之仓内事实源。
- v1.1 计划 §6 字面（转引）：「G-D01/G-D02 未裁——论文声明面暂时挂账」。

---

## §6 通道事实（辅助）

- **upload/**：最新到件＝PI 三件（10-18 20:14）；此前 10-17 16:08 两件（判死线/心哲映射）；10-13 两件（arxiv 通知、glm commission reply request）——**10-17 后无外部（minimax/Gemini4/KIMI）回件**。
- **shared/**：本日件均我方团队产出（鲍勃回执 3 件、查理 v10、爱丽丝评审 2 件、阿兰核验 1 件等）。

---

## §7 纪律声明

1. 本棒全程匿名只读：0 PAT 使用、0 写、0 推送、0 修改任何仓内/既有件；部分克隆置于本棒私有目录（`agents/…/tmp_repo_check/`）。
2. 本件仅登记事实（在仓/不在仓/指纹/登记件自报字面）；**0 判定、0 代裁、0 落终判**；凡「自报/转引」字面均标明出处，未以我方实测复核者不混计。
3. 指纹口径 SHA-256[:12]；「现指纹」＝本棒于 75a8fbb 实测（部分件经 75a8fbb 脱敏波后与历史登记值存在字节差——差异如实并列，0 判成因）。

（完 · 爱丽丝 · 2026-10-18 晚 · 匿名只读事实核查）
