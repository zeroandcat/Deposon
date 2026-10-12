# 候 PI 面 · 总账筛查 v2（重跑 · 精简版 · 增量承接＋遗漏扫描）· 2026-10-09

- **件性质**：**候 PI 面总账筛查件 v2（对账面 · 只读登记）**。本件**0 代裁 · 0 推荐 · 0 排序暗示 · 0 择档 · 0 给阈值**；凡需 PI 决者只**归并登记**并注明责任面，⛔ 0 由本件了断。
- **授权锚**：承接 v1 件（`_pending_pi_items_master_register_2026_10_09.md`）之同一授权 —— PI 2026-10-09 卷⑨问卷 `ask_cfb9284519a5abf29d0f03eb` Q1「五段全开·批准后当日即办」＋「尽量今天至少推完①」之第①段「V3/V4 实验全量收束」清卷系列供料。
- **出件**：**worker**（Mavis 团队分支 worker · 登记/对账类 · session `mvs_0cafb450acf14db9bb488cd8b0d04776`｜署名如实 · **0 冒充 PI／parent／verdict-keeper／verifier／protocol-keeper／evidence-auditor**）。
- **件名合规**：`_pi_facing_items_screen_2026_10_09.md` ＝ `_主题_日期`（沿 PI 2026-09-29 命名裁 `57024f2cd30a` §1.2②）⇒ ✅ **0 V-阶段前缀 / 0 `_v5_` 类前缀 / 0 阶段号作首段**。
- **版式**：**UTF-8 无 BOM · LF（CRLF ＝ 0）**。
- **指纹口径**：`Get-FileHash -Algorithm SHA256` 当轮实测、小写 12 位（⛔ 0 以 SHA-1 冒充、⛔ 0 内建 `hash()`）。
- **本件 0 自写入自身指纹**（自指回环）⇒ 终态 SHA-256／字节／CRLF 计数**随交付回执回报**。
- **日期**：2026-10-09（v2 读取时点 21:44–21:5x GMT+8；增量窗口下界 12:45:09）

---

## §0 范围与读取时点 ＋ 重跑说明

### §0.1 **重跑说明**（本轮出件缘起）

| 项 | 内容 |
|---|---|
| **触发** | 前方一跑（同题 · 候 PI 面总账筛查 v2）于**收尾前静默中断、未落件**（状态 `succeeded` 但 **0 产物**）⇒ 本轮为**重跑**。 |
| **本轮加固** | 采 **「先落骨架 · 后补全」** —— 每完成一节即写盘（`.md` 分段追加由本棒自控），防尾段全失；中途若资源受限 ⇒ **保已落盘部分**并如实报「**部分成就**」。 |
| **对既有件** | ⛔ **0 判读 · 0 处置 · 0 编辑／0 覆写／0 追加／0 改名／0 移动／0 删除**任何既有件（**含 v1 件本身**，byte 0 触动）。 |
| **写入面** | 只读工具（`Get-FileHash -Algorithm SHA256`／`read`／`grep`／`Get-ChildItem`／`Test-Path`／节级行抽取）＋ **分段 `write`/`edit`（仅本件）**。 |
| **v1 承接口径** | v1 于 **12:45:09** 落（60 条 ＝ 销项 21／残留 39／归属他人 6）。本轮**以 12:45:09 为增量窗口下界**，其**前**之产出件归 v1 管辖、**后**之归本轮增量。 |

### §0.2 范围（精简 · 避免通读全仓）

| 面 | 范围 | 抽取口径 |
|---|---|---|
| **① v1 基线承接** | `results/_pending_pi_items_master_register_2026_10_09.md` | **只读其主表（§2）与销项／残留两节（§3／§4）** ＋ §0 纪律面 ＋ §6.3 计数面 |
| **② 增量汇总** | `results/` 下 mtime **> 2026-10-09 12:45:09** 之新件 | **只抽其「候呈/未闭/须裁」节标题与条目（以节为单位；⛔ 0 整件通读）**；覆盖 CI／K／S4／T1／KD 各族 |
| **③ 遗漏扫描** | 以件名单为面（**当日新件清单** vs **各登记/总表之引用面**） | 标识**未被任何登记/总表覆盖**之产出件或裁定 |
| **④ 输出** | 本件 §1 **未闭项总表** | 按 **PI／verdict-keeper／worker／verifier／parent** 分组 |

### §0.3 增量窗口实测（`Get-ChildItem results -Recurse -File`）

| 口径 | 计数 | 说明 |
|---|---:|---|
| **`results/` 全部文件（⛔ 0 含 `__pycache__`）** | **976** | 本轮扫描面基准 |
| **增量窗口（mtime **> 12:45:09**）** | **73** | ＝ `.md` **63** ＋ `.json` **9** ＋ `.py` **1** |
| **v1 边界件**（mtime **＝ 12:45:09**） | **1** | `_pending_pi_items_master_register_2026_10_09.md` ＝ 窗口**下界本身**，归 v1 域 |
| **v1 域同名件**（mtime ≤ 12:45:09） | **35** | ＝ `.md` **32** ＋ `.json` **2** ＋ `.py` **1** |
| **当日同名件合计** | **108** | 35 ＋ 73（v1 边界件已含于 35 内） |
| **`__pycache__` `.pyc` 副产物**（窗口内） | **2** | 编译副产物 ⛔ 非读数载体／非登记件／非 pin 面 ⇒ 本件 0 计入候呈面 |
| **窗口 `.md` 中带「候呈/未闭/须裁」节标题者** | **41 件 ／ 51 节锚** | 见 §3 逐件登记 |
| **窗口 `.md` 中 0 节锚者** | **22 件** | 经逐件探测归入 §4 扫描面（多为执行/登记/工具/数据面或已闭项） |

> **⚠ 计数校正说明**：本轮初次枚举曾以 `-Include *.md` 过滤得 `.md` **61** 件、后以 `-Filter` 得 **63** 件，二者不一致；**已以单一查询重取**（`.md` **63**），本表以**后者**为准。此差异**源于 PowerShell `-Include` 递归语义**，⛔ 0 隐瞒。

### §0.4 纪律声明（本轮 0 做）

| 项 | 内容 |
|---|---|
| **0 代裁** | ⛔ 0 择档、0 给阈值、0 断母件口径冲突、0 断销项之法律效力（**销项判定权属 parent／PI**，本件只呈依据）。 |
| **0 推荐 · 0 排序暗示** | §1／§3 分组**不构成**次序、优先级或推荐档；分组仅按**责任面／来源族**归类。 |
| **0 编造** | 核不到处写「**未核得**」并注明探测方式，⛔ 0 以「0 命中」推定实体不存在。 |
| **0 擅自代答** | ⛔ 0 断 PI 之答、⛔ 0 替他棒销项。 |
| **网络／skill／R4** | ⛔ **0 网络** · ⛔ **0 端点调用** · ⛔ **0 skill** · ⛔ **0 读 key／0 读 `.env`** · **R4 key 永不明文**。 |
| **0 阶段名自升** | 所引 `V3`／`V4` 字样**仅为既有件既有字面引用**；本件名**不含 V-阶段前缀**。 |
| **0 擅调阈值** | `≥50`／`167`／`171`／`179`／`64 格`／`0.574850`／`seed 42` 等**逐字沿既有件**，本件**一字未动**。 |

---

## §1 未闭项总表（按责任面分组 · **0 排序暗示 · 0 推荐次序**）

> **⚠ 分组仅按「责任面」归类**，⛔ 0 按轻重／时序／来源排序，⛔ 0 推荐推卷次序，⛔ 0 建议答案档。
> **⚠ 销项之法律效力归 parent／PI**：本表「已闭」仅指**盘上可核之卡答／生效登记事实**。
> **来源标记**：`〔增〕`＝本轮增量件新出 ｜ `〔v1〕`＝v1 主表 60 条之承接 ｜ `〔增＋v1〕`＝增量件显式复述 v1 条目。

### §1.1 **PI 面**（裁／答／授权／供料）

| ID | 未闭项 | 来源 | 承载件（节） |
|---|---|---|---|
| **PI-01** | **`held-out ≥ 50` 之处置**（实测 `floor` 和 26–30 ＜ 50，上界 37）；依「重新立线」或另立新线 | 〔v1〕PK-1 之后续面 | `_s4_topup_intake_recompute` §6-1／`_s4_topup_intake_verdict` §5-2／`_is_corr_pair_caliber_revision_proposal` §6.3-4／`_kv3s_4_terminal_verdict` §6-2 |
| **PI-02** | **分母域择域**（**149／167／171／179／180／186 六读**；单日占比 0.516129–0.644295，**跨 0.60 切点两侧**） | 〔v1〕G-ⓒ-10／PK 族 | `_kv3s_4_terminal_verdict` §6-4／`_s4_substrate_refreeze_register_179` §8-2／`_k_v3s_4_3_frozen_recompute` §11-2 |
| **PI-03** | **C-1 CI 线七要素**：① 形态（绝对常数／相对基线增量）② **estimand 指定** ③ 「宽度 vs 半宽」钉定（因子 2）④ **触发条件脱钩**（`n ≥50 后` 在 S4 面永不成就）⑤ 防退化合取项是否绑定 ⑥ `h₃ = 0.1326086957` 基线钉死 ⑦ B／C 重采样构造择定（J3） | 〔v1〕PK-4 之落地面 | `_ci_line_establishment` §8-1～7／`_ci_bc_lines_ci_collection` §8-1 |
| **PI-04** | **C-1 线之复核面**：⑧ **B／C 半宽门适用面（K-1）之复核** ⑨ **estimand 与原判据关系之复核** ⑩ **等效门柱数值**（K-1 只裁「暂免」）⑪ **A′（NLED-sim）CI 是否入判读面** ⑫ **B／C 之 CI 是否即 C-1 判读面所系之量** | 〔增〕 | `_ci_degradation_binding_form_a_register` §7-2/3／`_ci_bc_scope_estimand_judgments` §7-1/2/3／`_ci_three_items_effectivity_register` §8-1／`_ci_gap_fill_alt_bc_aper_prime` §9-1 |
| **PI-05** | **`is_corr_pair` 口径择档**（甲／乙／丙／丁四档）＋ `[PI 给定]-E` 哨兵字面 ＋ `[PI 给定]-F` 既有 `R9`–`R11` 三对之 `b=1` 归位与否 | 〔v1〕PK-6／RP-E／RP-F | `_is_corr_pair_caliber_revision_proposal` §6.3-1/2/3／`_s4_substrate_freeze_register` §7-1 |
| **PI-06** | **held-out 格内取法 R1–R4**（每格内候选件排序／RNG 实现与流式／取法／跨格 RNG 消耗顺序）—— 盘上 `within_cell_selection: NOT_OBTAINED` | 〔增〕 | `_s4_heldout_sampling_seed42_register` §9.3／`_s4_heldout_sampling_caliber_ruling` 待裁清单 |
| **PI-07** | **`K-T1-R1-1` 门禁之处置**（维持不豁免／新出修订件明文加例外条款；若采分轴豁免须具 E-1–E-6 六要素） | 〔增〕 | `_t1_qwen_temp_sweep_r2_verdict` §10-①／`_t1_gate_revision_draft` §4 |
| **PI-08** | **`K-T1-S1`／`K-T1-S3` 之 `N_min` 与主度量 J 双口径分离确认** | 〔增〕 | `_t1_qwen_temp_sweep_r2_verdict` §10-② |
| **PI-09** | **T1 三口径择定之确认**（`full_reply`／`content_only`／`reasoning_only`） | 〔增〕 | `_t1_qwen_temp_sweep_r2_verdict` §10-③ |
| **PI-10** | **温度轴有效性面之处置**（E-1 门禁路径择一／E-2 是否采答案面为探针／E-3 MDE 数值线／E-4 端点调用与额度授权／E-5 是否接受「轴无效」为可出之判／E-6 修订件核准生效） | 〔v1〕O-2 之邻面 | `_t1_temp_axis_new_experiment_design` §11-①～⑥ |
| **PI-11** | **D-1 之勘正**（`cell_j_median` 系 all-pooled 导出 vs activation §2.2 之 same-caption） | 〔增〕 | `_t1_qwen_temp_sweep_r2_verdict` §10-⑤／`_t1_temp_axis_new_experiment_design` §11-⑦ |
| **PI-12** | **`C-1`／G-ⓖ-20「Q2 拍板档」何指**（源件明载「该候裁项仍未消，如实挂账」） | 〔v1〕 | `_t1_qwen_temp_sweep_r2_verdict` §10-⑦ |
| **PI-13** | **`TH_T1_N_MIN` 新值**（O-2：预登记 10 vs 实际 6 对/教师）—— 丙档明写「新值须 PI 给」 | 〔v1〕O-2 | `_th_t1_n_min_revision_proposal` §2 丙档 |
| **PI-14** | **C1–C4 四缺项之路径裁**：`NPI-1` 构造族指定（α／β／γ／δ）｜`NPI-2` **H 对照读数口径裁**（ECR／`T_frac60`）｜`NPI-3` C2 独立重跑范围确认｜`NPI-4` ＝ P-2 `K-V3DF-4-2` 落法射程｜`NPI-5` ＝ P-3 `K-V3DF-1-1` 效力射程｜`NPI-6` ＝ P-1 `145.8×` 定性／档位｜`NPI-7` ECR 锚面修订是否授权｜`NPI-8` 新件名与新 `K-*` ID 之授权 | 〔v1〕P-1/P-2/P-3＋〔增〕NPI-1/2/3/7/8 | `_c1c4_input_gap_fill_plan` §11 |
| **PI-15** | **`K-CF-4` 分档口径之复核生效**（三档 ＋ G1–G6；两件同向相容、**0 自认生效**）＋ **档 1 是否属「事后 0 调整」锁内** ＋ **`U-V04-01-新` 与本分档之关系裁** | 〔v1〕E3-①／U04-1 | `_k_cf_4_low_cardinality_recure` §12-1/2/3／`_k_cf_4_low_cardinality_reurecheck_and_precedent_fill` §10-1/2/4 |
| **PI-16** | **`E3-②` 之答**（设计件 `b1c7c24926bb` 是否已 PI 复核生效 ⇒ 决定 `E3-A` 属「测量前定义修订」抑或「须作废重订」）＋ **`E3` 定义稿之起草与复核归属** | 〔v1〕E3-② | `_k_cf_4_effectivity_register` §E-1／§E-5 |
| **PI-17** | **`U-V04-01-新` 候呈措辞与核准实体字面之差**（「整类豁免」vs 布尔位整类＋标签位条件＋常量/派生列 ⛔ 0 整类）＋ **配套校验位落面缺口** | 〔v1〕U04-1 | `_k_cf_4_effectivity_register` §E-2／§E-3／`_u04_1_exemption_precondition_verification` §5 G-U04-1/G-U04-2 |
| **PI-18** | **`U-V04-02`／`G-ⓒ-7`**（`dual_hex_width` 甲档豁免·PI 备案）—— 与 §B-2 常量轨同族但**不同项**，未由他裁消解 | 〔v1〕U04-2／G-ⓒ-7 | `_k_cf_4_effectivity_register` §E-8 |
| **PI-19** | **`R` 是否实施 ＋ asar 备份／回退授权 ＋ 打点件落面路径** | 〔v1〕G-ⓖ-19 之 asar/落面路径 | `_k_cf_4_effectivity_register` §E-9 |
| **PI-20** | **`RP-D` 降级标注是否仍落**（PI 参数卡未明示 ⇒ 本棒沿设计件默认落标注 8/8） | 〔v1〕RP-D／RPQ-7 | `_r_pair_intake_recompute_register` §7-6 |
| **PI-21** | **`RP3b` 之 C 档新字面**（若采「理由括注随变量同步」口径）—— 🟥 **须 PI 给** | 〔增〕 | `_r_pair_texts_independent_review` §7-1 |
| **PI-22** | **`RP2` 之 C 判定方向跨半翻转之落地歧义解法**（同字母同向 vs 实质方向） | 〔增〕 | `_r_pair_texts_independent_review` §7-2 |
| **PI-23** | **「只动 1 变量」准口径三择一**（直接决定 RPQ-6 之单一判词）＋ **「非画像」判定面边界**（题面面 vs 全件面） | 〔v1〕RPQ-6／〔增〕 | `_r_pair_texts_independent_review` §7-3/5 |
| **PI-24** | **`RPQ-4` 题面措辞是否含 PI 个人化表述（终审属 PI 面）**＋ **`RPQ-5` 三选项是否 0 诱导／0 明显不可行档** | 〔v1〕RPQ-4/5 | `_r_pair4_design_and_texts` §5 第 1／5 项 |
| **PI-25** | **`RP-C` 并轨方式**（甲／乙／丙；涉「每卷 ≤4 题」纪律之遵守方式） | 〔v1〕RP-C | `_r_pair4_design_and_texts` §0 0 做声明 |
| **PI-26** | **`S4T-17` 候呈卡未答**（「held-out 抽样器（按 0.30 分层、seed 42）由谁建？」`ask_42b717c5410863b425967094` `status=pending`） | 〔增〕 | `_s4_heldout_sampling_seed42_register` §9.4-6 |
| **PI-27** | **`S4T-18` 之 18 件减为 14 件须 PI 明示**（冻结后加题口径；`149＋14＋4＝167`） | 〔增〕 | `_s4_open_questions_design` 乙档代价栏 |
| **PI-28** | **`correction_confirmed` 判读型字段值之处置**（1 对 `true` ／ 3 对 `null`） | 〔增〕 | `_kv3s_4_terminal_verdict` §6-9／`_s4_terminal_face_recompute` §7-5 |
| **PI-29** | **提取器敏感面之字段语义分层确认**（`pi_source_date` 与 `date` 冲突 **2 行** ⇒ `distinct` 白名单 8 vs 改采 10） | 〔增〕 | `_s4_face_v2_sync` §9-3／`_s4_face_sync` §8-3 |
| **PI-30** | **`171` 域裁是否及于 `K-V3S-4-2` 之 substrate 腿**（现读数面 ＝ 179） | 〔增〕 | `_kv3s_4_terminal_verdict` §6-1b／`_k_v3s_4_2_domain_extension_judgment` §1 ① |
| **PI-31** | **`S4 substrate` 冻结面是否须就 179 面正式重冻**（登记 G5／ARR-3 仍为 167 面） | 〔增〕 | `_kv3s_4_terminal_verdict` §6-6／`_s4_substrate_refreeze_register_179` §8 |
| **PI-32** | **「留出比例」之计量口径**（名义 0.30 vs 实测聚合 26/179＝0.145251，差 −0.154749） | 〔增〕 | `_kv3s_4_terminal_verdict` §6-5／§8-2 |
| **PI-33** | **`_s4_final_ruling_effectivity_register` 自身之复核生效**（§2 乙档生效 ＋ §4 `N_min` 定义；**生效前现行口径恒为甲**） | 〔增〕 | `_s4_final_ruling_effectivity_register` §6-1 |
| **PI-34** | **`PK-3` PI 括注「10-01 80 余题量口径」之释义**（盘上该数为 substrate 题量面） | 〔v1〕PK-3 | `_s4_revision_effectiveness_register` §7-9 |
| **PI-35** | **`PK-5` `held-out ≥ 50` 与 `TH-v2-1`／`v3-1`（`N_min=50`）是否同物** —— 盘上 **0** 有定义件 | 〔v1〕PK-5 | `_s4_revision_effectiveness_register` §7-3／`_ci_width_halfwidth_pin` §8-6 |
| **PI-36** | **KD 异义归类处置之 PI 卷**（若裁「须落字面」⇒ 另派口径固化棒；若裁「族②书写归一」⇒ 另派 VK 会签） | 〔增〕 | `_kd_heteronym_classification_disposition` §6.2 |
| **PI-37** | **KD 可解性 N-1…N-6 六类「非可选项」**（N-1 判据射程/口径裁；N-2 授权/生效裁；**N-3 PI 数值权限**；N-4 结构性保留；N-5 依附 B-4；N-6 卷5 三题在途） | 〔增〕 | `_kd_resolvability_and_optional_experiments` §4.2 |
| **PI-38** | **卷5 三题未答**（`ask_aca3a25c244aa405e60eb22c` `status=pending`，答复在 DB 中不存在） | 〔v1〕G-ⓑ-3 | `_kd_resolvability_and_optional_experiments` §4.2 N-6 |
| **PI-39** | **`V02-A`／`V02-B`**（V3-02 覆裁：维持 10-01 裁 ／ 授权改码＋指定新名＋另立 kill-line 面）—— 执行面已走，**终裁仍候 PI** | 〔v1〕 | `_v3_02_ethard_closure_verdict` §6 A–D／`_v3_02_ethard_execution_register` §9 |
| **PI-40** | **母件一致性与登记效力**：`G-ⓐ-1`（8 硬缺口以 §2.1 必做链为准抑或 §1.3 注为准）｜`G-ⓒ-8`（V3-06 #35 条件式留白效力重裁）｜`G-ⓖ-18` 余三问（字节差成因／甲12 登记面收口／PI 侧盘更晚改动）｜`M9-2`（W5 验收列之唯一口径） | 〔v1〕 | v1 §2 主表（**增量窗口内 0 新销项证据**） |
| **PI-41** | **复核生效／备案／裁量面**：`G-ⓓ-11`（V4-01/06 入锁冻结件复核生效）｜`G-ⓓ-12`（V4-07 扩词天花板 vs 1.00 结构性张力）｜`G-ⓔ-14`（`5d42e81289cc` §8.1①-b 裁量面释义） | 〔v1〕 | v1 §2 主表（**增量窗口内 0 新销项证据**） |
| **PI-42** | **素材供给与溯源**：`G-ⓒ-6`（V3-01 C4 四值采认·外阻塞）｜`G-ⓕ-16`（V4-08 D1 缺位 8 件 event_id 38–45 素材）｜`G-ⓑ-4`（补采题面供给）｜`M9-1`（`minimax-m3` 三源并存取何值）｜`M9-3`（`EMBEDDING_VISION_V1_IMPL_2026_09_10.md` 溯源） | 〔v1〕 | v1 §2 主表（**增量窗口内 0 新销项证据**） |

> **PI 面合计：42 组**（其中〔v1〕承接 **17** 组、〔增〕新出 **25** 组；〔增＋v1〕并计于〔v1〕栏）。

### §1.2 **verdict-keeper 面**（判档／判定）

| ID | 未闭项 | 来源 | 承载件（节） |
|---|---|---|---|
| **VK-01** | **`K-V3S-4-1`／`-2`／`-3` 三线判档**（终 N 面 **179** 乙口径：占格 **54**／空 **74**；substrate **179**／`floor` **26**；跨日 **8 天**／最大单日 **96**／占比 **0.536313**） | 〔增〕 | `_s4_terminal_face_recompute` §7-1／`_s4_substrate_refreeze_register_179` §8-1／`_kv3s_4_terminal_verdict` §8 |
| **VK-02** | **`k_v3s_4_3_ok` 之判档**（跨日 8／单日 0.574850／余量 +0.025150，分母 167 主读） | 〔增〕 | `_k_v3s_4_3_frozen_recompute` §11-1／`_s4_face_v2_sync` §9-1 |
| **VK-03** | **读数面择基**：`2dc64593b889` 之网格系谱 ＝ 设计期甲档，11 项网格／held-out 读数在乙档下逐项相异 ⇒ 须以乙档终值为现行读数面（⛔ 0 回改该件） | 〔增〕 | `_s4_terminal_face_recompute` §7-2／`_kv3s_4_terminal_verdict` §6-7 |
| **VK-04** | **T-5 空格 74>0 之并报**（「0.30 名义达标／实际分层不可达」） | 〔增〕 | `_s4_face_five_lines_ci_readings` §9-4 |
| **VK-05** | **`K-V3S-4-1` 之「分层含纠正」0 成立**（`b=1` 留出件数 ＝ 0，**规则内生、与取哪几件无关**） | 〔增〕 | `_s4_heldout_sampling_seed42_register` §9.4-2／`_s4_face_five_lines_ci_readings` §9-3 |
| **VK-06** | **`V3-04` 判定面之总态／操作方向是否随 §B 复议**（主读法 KD／替代读法①PASS（PI 裁前提）／②PASS（窄口径·相悖·0 采用）三读并置） | 〔v1〕U04-1 之邻面 | `_k_cf_4_effectivity_register` §E-4 |
| **VK-07** | **`K-V3DF-4-2` 落法射程分歧**（前代生效终态 `FAIL` vs 第二读 `KD`）—— ⛔ 0 翻案、0 回改历史行 | 〔v1〕P-2 | `_c1c4_input_gap_fill_plan` §5 风险②／§11 NPI-4 |
| **VK-08** | **`K-V3DF-1-1` 效力射程**（盘上 PASS；第二读「不明·效力射程未定义」） | 〔v1〕P-3 | `_c1c4_input_gap_fill_plan` §11 NPI-5 |
| **VK-09** | **`145.8×` 定性／`DIFFERENTIATED` 档位**（输入面 5 缺项：1 已消 ＋ **4 未消**）⇒ 裁即编造 | 〔v1〕P-1 | `_c1c4_input_gap_fill_plan` §11 NPI-6 |
| **VK-10** | **`K-RO-0-1` 第二出口「改构造 → 重自证」是否迭代**（P-1 构造未取得可开跑资格 ⇒ 段 2 正式跑维持不启动） | 〔v1〕P-5 | `_c1c4_input_gap_fill_plan` §4 |
| **VK-11** | **T1 `K-T1-S1`／`K-T1-S3` 之不明（T-5）** —— O-1 逐字「r2 亦不能自动解除 S3 之不明」 | 〔增〕 | `_kd_resolvability_and_optional_experiments` §4.2 N-5 |

> **verdict-keeper 面合计：11 组**（〔v1〕5 ／ 〔增〕6）。

### §1.3 **worker 面**（执行／采集／落件）

| ID | 未闭项 | 来源 | 承载件（节） |
|---|---|---|---|
| **W-01** | **S4 面五线 CI 读数 0 有**（A／A′／B／C／D 全部；**0 起跑 executor、0 新观测**） | 〔增〕 | `_s4_face_five_lines_ci_readings` §9-1／`_ci_three_items_effectivity_register` §8-2／`_ci_four_items_effectiveness_register` §7-3 |
| **W-02** | **替代读法（n=18）之 B／C CI 盘上无法采集**（`per_event` 0 落盘且子集欠定 2520／1080 组解） | 〔增〕 | `_ci_bc_lines_ci_collection` §8-2／`_ci_four_items_effectiveness_register` §7-4 |
| **W-03** | **held-out 分层抽样之执行**（seed 42 逐件留出集盘上 0 件；A1-3 未成就、A1-4 部分成就） | 〔增〕 | `_kv3s_4_terminal_verdict` §8-1／`_s4_heldout_sampling_seed42_register` §9.4-1 |
| **W-04** | **S4 substrate 冻结面之重冻**（G5／ARR-3；本棒以重冻前 179 面为输入域） | 〔v1〕G-ⓓ-11 之邻面 | `_s4_revision_effectiveness_register` §7-4／`_s4_heldout_sampling_seed42_register` §9.4-5 |
| **W-05** | **既有读数登记件之重算并出新件**（乙档 6 项读数变动；⛔ 0 回改既有件 ⇒ 只能另出新件） | 〔增〕 | `_s4_final_ruling_effectivity_register` §6-3 |
| **W-06** | **`.pyc` 编译副产物 2 件之处置**（清理被运行时拦截；本棒 0 绕过、0 改用他法删除） | 〔增〕 | `_v3_02_ethard_closure_verdict` §6 D |
| **W-07** | **`alt_reading` 口径真源在 `.tmp/`**（`.tmp/_run_final.py` `75d466add5d5`；若 `.tmp/` 被清则口径链失锚） | 〔增〕 | `_ci_gap_fill_alt_bc_aper_prime` §9-7 |
| **W-08** | **配套校验位之落面**（`dual_hex_width` 恒等校验读数面已满足、产出件仍未落该校验字段 ⇒ 缺位即豁免不成立） | 〔v1〕U04-1 之落地面 | `_k_cf_4_effectivity_register` §E-3／`_k_cf_4_low_cardinality_reurecheck_and_precedent_fill` §10-3 |
| **W-09** | **`T-1` 覆盖线之独立报义务**（`is_corr_pair = 1` 行数 0 之「素材面不覆盖」缺口，**不**因 A 生效而免报） | 〔增〕 | `_ci_degradation_binding_form_a_register` §7-6／`_ci_three_delegated_judgments` §6-4 |
| **W-10** | **面之时点冻结之漂移风险**（若抽样棒向 `*addendum*.json` 域写入新行/新件，本冻结面即失效、须再重冻） | 〔增〕 | `_s4_substrate_refreeze_register_179` §8-3／`_s4_face_five_lines_ci_readings` §9-8 |

> **worker 面合计：10 组**（〔v1〕1 ／ 〔增〕9）。

### §1.4 **verifier 面**（独立复核／口径核）

| ID | 未闭项 | 来源 | 承载件（节） |
|---|---|---|---|
| **V-01** | **提取器复算 ＋ 交叉核并报**（日期/日戳提取器产出读数 `distinct 8`／单日 0.561404／完备 171/171 **0 静默采信**） | 〔v1〕G-ⓖ-19 之 R 面余波 | `_s4_revision_effectiveness_register` §7-5 |
| **V-02** | **日戳读法择域**（事件日历日 vs 件级 mtime；`2dc64593b889` 仅取 `date` 单键 ⇒ 跨日 7 天／日账 176 ≠ 179） | 〔增〕 | `_k_v3s_4_3_frozen_recompute` §11-3／`_s4_terminal_face_recompute` §7-3 |
| **V-03** | **`169 ≠ 171` 打印表分歧之成因**（`2e66478e6db6` §3.2 表 `s=5` 行 `o=7` 格印 4·实 6；争议格 `(0,5,7)` 甲档＝6／乙档＝4）—— ⛔ 0 归因 | 〔增〕 | `_s4_face_sync` §8-1／`_s4_face_v2_sync` §9-2／`_s4_terminal_face_recompute` §7-9 |
| **V-04** | **bootstrap 口径之 `TH-*` ID 归属两读未决**（C-1 定义作 `TH-v2-7`/`v3-16`/`v3-17`；预登记表载排列 vs bootstrap） | 〔v1〕PK-4 族 | `_s4_revision_effectiveness_register` §7-2／`_s4_final_ruling_effectivity_register` §6-2 |
| **V-05** | **`b` 轴口径之复核**（既有 167／171 行中 `is_correction = true` 者 7 行，`b` 轴按 `is_corr_pair` 口径计 0 行；换口径则占格/空格/floor 三读均变动） | 〔增〕 | `_s4_open_questions_intake_recompute` §7-5 |
| **V-06** | **`h₃` 四读极差百分比之算术小差**（既有件记 25.19%、本棒实测 25.14%；极差值本身吻合） | 〔增〕 | `_ci_four_items_effectiveness_register` §7-5 |
| **V-07** | **v3r1 之 `per_event[].nw_sim` 落盘精度注记**（一处舍入至 `0.4286`，致直算微差 ≈2.48e-6） | 〔增〕 | `_ci_bc_lines_ci_collection` §8-4／`_ci_gap_fill_alt_bc_aper_prime` §9-6 |
| **V-08** | **verifier 独立复核（A1-7）未签字** | 〔增〕 | `_s4_heldout_sampling_seed42_register` §9.4-7 |
| **V-09** | **`TH-*` 引用有误之 verifier 判定**（`94740f8d3c8d` VERDICT：FAIL）—— 下游 0 采信为现行裁定、仍候确认 | 〔增〕 | `_s4_face_v2_sync` §9-9／`_th_id_attribution_verification` |

> **verifier 面合计：9 组**（〔v1〕1 ／ 〔增〕8）。

### §1.5 **parent 面**（登记／编排／落册）

| ID | 未闭项 | 来源 | 承载件（节） |
|---|---|---|---|
| **P-01** | **PI 裁卡原件之盘上落册**（多张卡 id 于盘实测 0 命中：`ask_a9ce5b284c10bf1e36077e35`／`ask_2643fab3836ce14c466a1243`／`ask_68df18a1976c91fb18d19497`／`ask_92998b73d1b6cb2255391499`／`ask_4ce2001998037e107db9591c`／`ask_492645c357b2638d0aac0bb8`／`ask_1936c3a747b2c740a2c71b12`／`ask_42b717c5410863b425967094`）⇒ 照录四答 ＝ 派工单转录 | 〔v1〕PK-7／G-ⓓ-13 | `_ci_degradation_binding_form_a_register` §7-7／`_ci_bc_scope_estimand_judgments` §7-7／`_ci_three_delegated_judgments` §6-6／`_ci_width_halfwidth_pin` §8-8／`_s4_final_ruling_effectivity_register` §6-5／`_k_cf_4_effectivity_register` §E-6／`_s4_revision_effectiveness_register` §7-6 |
| **P-02** | **`167` 归位（0 作用）之下游知悉与对齐**（引用 `167` 之既有件**原件 0 回改**） | 〔增〕 | `_s4_revision_effectiveness_register` §7-7／`_s4_open_questions_intake_recompute` §7-3 |
| **P-03** | **S4 原定 167 算式之变更（甲档附条件）之知悉与下游对齐**（新算式 `149＋18＋4＝171`） | 〔增〕 | `_s4_open_questions_intake_recompute` §7-3 |
| **P-04** | **G3（执行序呈核）／G6（T-5 预报呈核）之呈核登记** —— 🔴 **阻「可开跑」宣告** | 〔v1〕G-ⓓ-13 | `_s4_substrate_freeze_register` §7-4／`_k_v3s_4_3_frozen_recompute` §11-5 |
| **P-05** | **并行件并存之编排裁定**（`5f91d553e392` × `618280cb8cfd` 是否并卷／回收重复棒；`6f8ba105b892a` × 本件择一为基准面承载或并列） | 〔增〕 | `_k_cf_4_low_cardinality_reurecheck_and_precedent_fill` §10-5／`_k_cf_4_effectivity_register` §E-7／`_s4_face_v2_sync` §9-7 |
| **P-06** | **`f793c5d9128f` L26／L232「落在既有三对区间内」字面不成立** —— 候裁是否出勘误件 | 〔增〕 | `_r_pair_texts_independent_review` §7-4 |
| **P-07** | **UI 形态差异之知悉**（设计件原设想 `pi_other_verbatim` 恒 `null`，实际 `allowOther=true` ⇒ 4 件记全文逐字） | 〔增〕 | `_s4_open_questions_intake_recompute` §7-8 |

> **parent 面合计：7 组**（〔v1〕1 ／ 〔增〕6）。

### §1.6 evidence／protocol 面（**并列登记 · 0 混入上列五组**）

| ID | 未闭项 | 承载件（节） |
|---|---|---|
| **EP-01** | **`21f2926efc5d` §2.2 表第 7 行件名转录笔误**（`_d8_sq_2026_10_09.json` 盘上无此件；实为 `_d8_sq_2026_09_30.json`，`D8-36` @ `#idx=35`）—— ✅ **经两棒独立实测消解 · ⛔ 0 改件** | `_s4_face_sync` §8-2／`_s4_face_v2_sync` §9-4／`_s4_terminal_face_recompute` §7-8 |
| **EP-02** | **`6db4d0fb2452` §5.3「子集欠定」之结论已被闭合**（子集由 executor alt 分支唯一定义）—— ⛔ 0 回改原件，仅登记 | `_ci_gap_fill_alt_bc_aper_prime` §9-4 |
| **EP-03** | **G5／ARR-3 条文节位引用之勘正**（ARR-3 实于 `7ac726cda752` §4·L116；167 登记件引作 §5、派工单引作 §2.3）—— ✅ **已消解** | `_s4_substrate_refreeze_register_179` §8-7 |
| **EP-04** | **素材件集指纹公式口径不可比**（`3134d035a8ea` 公式已载明 vs `c535dc268e64` 公式未载明，7 式试算 0 复现） | `_s4_substrate_refreeze_register_179` §8-4 |
| **EP-05** | **V3-02 执行面次生残留三面**：`spec_ref_pending` 过时括注（所指 spec `c13449101ab3` 确已在盘）｜R docstring 与 `zero_overwrite_proof.policy` 清单外文字（实 pin 集已扩至 8 项）｜**CRLF 体例偏差**（新旧同形 100% CRLF，建议维持不事后转 LF） | `_v3_02_ethard_closure_verdict` §6 A/B/C |

> **evidence／protocol 面合计：5 组**。

### §1.7 总账计数

| 责任面 | 组数 | 〔v1〕承接 | 〔增〕新出 |
|---|---:|---:|---:|
| **PI 面** | **42** | 17 | 25 |
| **verdict-keeper 面** | **11** | 5 | 6 |
| **worker 面** | **10** | 1 | 9 |
| **verifier 面** | **9** | 1 | 8 |
| **parent 面** | **7** | 1 | 6 |
| **evidence／protocol 面** | **5** | 0 | 5 |
| **合计（去重后）** | **84** | **25** | **59** |

> **⚠ 计数口径**：组数 ≠ 条目数。v1 之 60 条主表经同物去重后映射为 **25 组**（见 §2 对账）；增量件之候呈条目经跨件同物归并后为 **59 组**（见 §3）。
> **⚠ 0 排序暗示**：以上分组**仅按责任面归类**，⛔ 0 表先后次序、⛔ 0 表轻重、⛔ 0 表推荐推卷次序。

---

## §2 v1 承接（销项／残留对账）

### §2.1 v1 基线指纹（只读复核）

| 项 | 值 |
|---|---|
| **源件** | `results/_pending_pi_items_master_register_2026_10_09.md` |
| **SHA-256／SHA-12** | 本轮 `Get-FileHash -Algorithm SHA256` 实测（见 §6 自证表） |
| **bytes／mtime** | 35,258 B ／ 2026-10-09 **12:45:09** |
| **v1 计数** | 主表 **60** 条 ＝ 销项 **21** ＋ 残留 **39** ＋ 归属他人 **6**（v1 §6.3 口径：销项 7／在卷 3／真残留 39／归属他人 6） |
| **⛔ 本轮处置** | **byte 0 触动**（⛔ 0 编辑／0 覆写／0 追加／0 改名） |

### §2.2 v1 残留 39 条 → 本轮增量窗口销项对账

| v1 条目 | 增量窗口内之销项证据 | 判定 |
|---|---|---|
| **PK-1**（S4 新立线 §2 三档勾选） | 清障卡 `ask_1936c3a747b2c740a2c71b12` ① 答「**C-1 CI 宽度线**（须给 CI 半宽上限，可注明『授权后补』）」；`_s4_chain_clearance_register` §1 ① 登记「已由生效登记立档」 | ✅ **已销**（勾选面闭）；其**后续面**（CI 半宽上限／形态／estimand）转入 §1 PI-03/PI-04 |
| **PK-2**（§1.2.1 三项修订稿之复核生效：`K-V3S-4-2` 字面／`167` 存废三选一／`P-S4-1` 状态注记） | 同卡 ② 答「**全部生效；167 取（c）随 held-out 一并归位**」；`_s4_revision_effectiveness_register` §2 乙档生效即锁（`K-V3S-4-2` 二项合取、held-out 转必报记录项、167 归位 0 作用） | ✅ **已销**（生效面闭）；**另新出** `_s4_final_ruling_effectivity_register` 自身之复核生效 → §1 **PI-33** |
| **PK-4**（阈值权限之明确授权 C-1／C-2 均需 PI 给数值） | CI 半宽上限 **`0.1100`**（＝半宽上限，全宽当量 `0.2200`）已由 PI 给，`_ci_width_halfwidth_pin` §8-1 记「口径面已闭」 | ⚠ **部分销**（**数值腿闭**）；形态／estimand／触发脱钩／防退化绑定／B-C 适用面 **仍残留** → §1 **PI-03/PI-04** |
| **G-ⓒ-10**（V4-12 分母三读 149／180／186 之择域） | 清障卡 ④ 答「**A，实事求是，并考虑提取器缺陷导致误判**」⇒ **171 主读**登记；其后读数面又推进至 **179** | ⚠ **部分销**（择域动作已出）；**域数扩至六读且 171→179 之域裁射程未闭** → §1 **PI-02/PI-30** |
| **G-ⓑ-5**／**PK-6**（`is_corr_pair` 轴覆盖并采） | 乙档已生效；`_is_corr_pair_caliber_revision_proposal` 出甲/乙/丙/丁四档＋三读逐值实算，**候 PI 再裁** | ⚠ **覆盖已定、口径未裁** → §1 **PI-05** |
| **RP-E**／**RPQ-8**（`is_correction` 哨兵字面） | `[PI 给定]-E` 仍随 Q1 候裁（`_s4_face_v2_sync` §9-8 载「随 Q1（乙已生效，仅字段类型一致性）」） | ❌ **未销** → §1 **PI-05** |
| **RP-F**（既有 R9/R10/R11 之 `b=1` 归位） | PI 明裁「**不回填**」⇒ 既有三对仍恒 `b=0`；`_r_pair_intake_recompute_register` §7-8 载「`b=1` 覆盖为**增量**而非追认」 | ✅ **已销**（PI 明裁不回填） |
| **RPQ-1**／**RPQ-2**（`RP1a`/`D8-36`、RP2 对是否「变相复用」） | `_r_pair_intake_recompute_register` §7-7 逐字登记「RPQ-1 ＝ **登记为同族备核**」「邻度四组 ＝ **非同题·同族备核**」 | ✅ **已销**（已登记入册） |
| **RPQ-3**（RP3 对与 `DF1-6` 是否够格判为「不同构」） | 同上 §7-7「邻度四组 ＝ 非同题·同族备核」 | ✅ **已销** |
| **RP-D**／**RPQ-7**（降级标注是否仍落） | `_r_pair_intake_recompute_register` §7-6「PI 参数卡未明示 ⇒ 本棒沿设计件默认落标注，8/8 已按默认落」 | ❌ **未销**（默认已落但未裁） → §1 **PI-20** |
| **PK-3**（PI 括注「10-01 80 余题量口径」释义） | `_s4_revision_effectiveness_register` §7-9 仍列为候裁 9 | ❌ **未销** → §1 **PI-34** |
| **PK-5**（`held-out ≥50` 与 `TH-v2-1`／`v3-1` 是否同物） | `_s4_revision_effectiveness_register` §7-3／`_ci_width_halfwidth_pin` §8-6 仍载「盘上 **0** 有定义件」 | ❌ **未销** → §1 **PI-35** |
| **G-ⓖ-19 之 R 面**（受控复现 R 是否实施） | 清障卡 ④ 之「提取器缺陷警注」已立为读数面复核项；但 R 本身之实施仍随 §E-9 | ⚠ **部分销**（警注已立） → §1 **V-01/PI-19** |
| **G-ⓕ-16**（V4-08 D1 缺位 8 件素材 PI 侧供给） | 增量窗口内 **0 新销项证据** | ❌ **未销** → §1 **PI-42** |
| **G-ⓑ-4**（补采题面之供给） | `_s4_open_questions_design_2026_10_09.md`（11:00，v1 域边界）已出题数上限方案；窗口内 0 新销项证据 | ❌ **未销** → §1 **PI-42** |

> **⚠ v1 残留 39 条 之窗口内销项小计：✅ 已销 6 条 ＋ ⚠ 部分销 3 条 ＋ ❌ 未销（含 0 新证据）30 条**（明细见 §1 映射；**销项之法律效力归 parent／PI**）。

### §2.3 v1「归属他人 6 条」之承接

| v1 条目 | 原归属 | 增量窗口内状态 |
|---|---|---|
| **G-ⓓ-13**（V4-04 G6 呈核登记） | parent | ❌ 仍待 → §1 **P-04** |
| **PK-7**（S4 卷2 卡原件落册） | parent | ⚠ **扩面**：由 1 张卡扩至 **8 张卡 id** → §1 **P-01** |
| **G-ⓖ-17①**（卡答逐字核对） | parent | ❌ 0 新证据 |
| **G-ⓔ-15**／**G-ⓖ-17④**（`K-V3S-3-3` 判定） | VK | ❌ 0 新证据 |
| **M9-4**（协议异质性是否构成截断效应） | VK | ❌ 0 新证据 |

### §2.4 v1「在卷 3 条」之承接

| v1 条目 | 状态 |
|---|---|
| **G-ⓑ-3**（卷5 三题未答） | ❌ 仍 `pending` → §1 **PI-38** |
| **V02-A**／**V02-B**（V3-02 覆裁） | ⚠ 执行面已走（`_v3_02_ethard_closure_verdict` 出四项处置建议），**终裁仍候 PI** → §1 **PI-39** |

### §2.5 v1 §6.2「未核得 6 项」之承接

| v1 未核得项 | 本轮状态 |
|---|---|
| S4 补采题面件落册（G-ⓑ-4） | ⚠ 仍未核得（`_s4_open_questions_design` 在 v1 域边界） |
| V3-01 两件（G-ⓒ-6） | ❌ 本轮 **0 复扫**（⛔ 0 推定）→ 沿 v1 登记 |
| 设计件 `b1c7c24926bb` 生效状态（E3-②） | ❌ 仍未核得（`_k_cf_4_effectivity_register` §E-1 明载「硬阻断」） → §1 **PI-16** |
| `EMBEDDING_VISION_V1_IMPL_2026_09_10.md`（M9-3） | ❌ 本轮 **0 复扫归档区** → 沿 v1 登记 |
| 卷5 三题答复（G-ⓑ-3） | ❌ 仍 `pending` |
| 散项面（closing-round 4–9／forgotten 三件） | ⚠ 见 §4 遗漏扫描 |

---

### §1.8 **落盘后新增（窗口漂移 · 本件扫描期间实测）**

> **⚠ 增量窗口为动态**：本件落盘期间（21:44–21:5x）仍有新件落盘。以下为实测新发现之 PI 面未闭项，**另立编号不并入 §1.1–§1.7 计数**，以免与已落盘计数失配。

| ID | 未闭项 | 责任面 | 承载件（节） |
|---|---|---|---|
| **Δ-PI-1** | **D 段 6／51 calls 未含于 PI 所给 ≈607 档** ⇒ 须单列授权或 PI 明示并档 | **PI** | `_t1_prereg_revision_temp_axis_exp2` §9 |
| **Δ-PI-2** | **起跑放行（跑禁）解除权属 PI** —— 额度授权 **⇏** 起跑放行 | **PI** | `_t1_prereg_revision_temp_axis_exp2` §9 |
| **Δ-PI-3** | **D 段判读线数值未获 PI 给**（设计件标「须 PI 给」；PI 四答未处置） | **PI** | `_t1_prereg_revision_temp_axis_exp2` §9 |
| **Δ-PI-4** | **「部分全同」之归属未获 PI 给** | **PI** | `_t1_prereg_revision_temp_axis_exp2` §9 |
| **Δ-W-1** | **activation 补记件（P-6）未出** —— D 段新增 `seed` 字段（＋42）系 r2 activation §2.2 规格之外新增项 ⇒ **未闭则不得起跑**（硬前置） | **worker** | `_t1_prereg_revision_temp_axis_exp2` §7.4／§9 |
| **Δ-P-1** | **执行棒派工候另派**（本件 0 派工、0 起跑、0 端点调用） | **parent** | `_t1_prereg_revision_temp_axis_exp2` §9 |

> **该件同时带来一则销项**：`PI 核准本件生效` ＝ ✅ **已核准**（决议②逐字「核准全案修订方向——按决议①所选案随件落定」）⇒ **生效即锁**。此项**超出本件既定增量窗口下界**，仅作登记。

---

## §3 增量销项与归并

### §3.1 增量窗口内 PI 卡答事件（**时间线 · 0 排序建议**）

| 序 | 卡 id | 面 | 盘上可核之答 | 承载件 |
|---:|---|---|---|---|
| **1** | `ask_1936c3a747b2c740a2c71b12` | **清障卡 · S4 链四项未闭** | **2026-10-09 14:38 答讫**。① 立线三档 →「**C-1 CI 宽度线**（须给 CI 半宽上限，可注明『授权后补』）」② 修订稿复核 →「**全部生效；167 取（c）随 held-out 一并归位**」③ `is_corr_pair` 口径 →「**候 protocol-keeper 出修订案再裁**」④ 分母择域 →「**A，实事求是，并考虑提取器缺陷导致误判**」 | `_s4_chain_clearance_register` `eda3d304d381` §1 |
| **2** | `ask_a9ce5b284c10bf1e36077e35` | CI 裁卡（四答） | ① B／C 半宽门适用面「**另议**」②「**五线全须**」（CI 读数采集面扩大）③ estimand「**另议**」④ 采集缺口「**两项均补采**」 | `_ci_degradation_binding_form_a_register` §1／`_ci_bc_scope_estimand_judgments` 卷首 |
| **3** | `ask_2643fab3836ce14c466a1243` | CI 宽度／形态裁卡（四答） | 产出「**`0.1100` ＝ 半宽上限（全宽当量 `0.2200`）**」之钉定 | `_ci_width_halfwidth_pin` §8-1／`_ci_detail_decoupling_degradation_baseline` §7 |
| **4** | `ask_68df18a1976c91fb18d19497` | CI 卡 | B／C 半宽＋`P-S2-1` 面之判断（出判断件 · 非生效） | `_ci_three_delegated_judgments` §6／`_ci_four_items_effectiveness_register` §7 |
| **5** | `ask_92998b73d1b6cb2255391499` | CI 卡 | 等效门柱数值相关（K-1 只裁「暂免」） | `_ci_three_items_effectivity_register` §8-1 |
| **6** | `ask_ced8de9fd514ccc30f4e16e2` | 分母域 ＋ 输入面缺项 | **2026-10-09 17:16** 裁「**171**」；Q4「**解决输入面缺项**」（覆盖批 7 ⑲③ 之「不扩」**作为本轮一次性处置**） | `_kv3s_4_terminal_verdict` §6-1／`_c1c4_input_gap_fill_plan` §2.1 |
| **7** | `ask_492645c357b2638d0aac0bb8` | `K-CF-4` 卡（两答） | 两裁已登记生效、生效即锁（口径层） | `_k_cf_4_effectivity_register` 卷首／§E |
| **8** | （PI 2026-10-09 20:54 增补） | 抽样执行 ＋ 域外延 | ①「held-out 分层抽样（seed 42）执行棒**已另派、在办**」④「**171 域外延已另议·在办**」 | `_s4_substrate_refreeze_register_179` §8-2／§8-5（引 `63621dcf5326`） |
| **9** | `ask_42b717c5410863b425967094` | **S4T-17** | ⛔ **`status=pending`（未答）** ——「held-out 抽样器由谁建？」A 采集方自建／B 另派一方建／C PI 指派 | `_s4_heldout_sampling_seed42_register` §9.4-6 |

> **⚠ 答讫时点之核销面**：仅**第 1 项（14:38）** 与 **第 6 项（17:16）** 有盘上逐字时点可核；其余各卡之**答讫时点未核得**（各件卷首自载「四答系**派工单所载之转录**」，且卡 id 于盘实测 **0 命中**）⇒ **0 以转录件之自载充运行时库原件**。

### §3.2 增量生效登记事件（**销项承载件**）

| # | 生效登记件 | 生效内容 | 消解面 |
|---:|---|---|---|
| **1** | `_s4_revision_effectiveness_register`（`356fe8509669`）§2 | 乙档**生效即锁**：`K-V3S-4-2` 二项合取（150 ∧ K-4-1）、held-out 转**必报记录项**、`167` 归位 **0 作用** | **v1 PK-2**（§2.2） |
| **2** | `_ci_width_halfwidth_pin`（`51765f40f5f9`）§8-1 | **`0.1100` ＝ 半宽上限**；两面须各自书明落盘 | **v1 PK-4 之数值腿**；`51765f40f5f9` §8 候呈 1 |
| **3** | `_ci_four_items_effectiveness_register` §7-1 | 四项**已生效并即锁** | `56b62ed5ab74` §7 候呈 **1／3／4** ＋ `51765f40f5f9` §8 候呈 **1** 之待裁态 |
| **4** | `_ci_degradation_binding_form_a_register` §7-1 | **A（判据合取）已生效并即锁**（半宽 ≤ `0.1100` ∧ 防退化门 `n_distinct > 3`；J2=b 配套；⛔ 0 溯及 r1／v3／v3r1） | `56b62ed5ab74` §7 候呈 **2** ＋ `dac19ee9e66b` §6 候呈 **1／2** |
| **5** | `_k_cf_4_effectivity_register`（`?`）尾款 | **两裁已登记生效、生效即锁**（口径层） | `E3-①` 条件解除注记＋`U-V04-01-新` 联动消解登记（**但 E3-②／E3-① 之未闭状态未消解**） |
| **6** | `_t1_prereg_revision_temp_axis_exp2`（`2ff15aeeb5d0`）§9 | **PI 核准本件生效**（决议②）⇒ 生效即锁 | 温度轴修订 r2 预登记之核准面（**§1.8 · 窗口漂移**） |

> **⛔ 0 代裁**：上表「生效」**仅指盘上可核之生效登记事实**；**销项之法律效力归 parent／PI**（沿 v1 §3 口径声明）。

### §3.3 跨件同物归并（**去重簇 · 计数仅计一次**）

| 簇 | 归并后归入 | 同物载于（件数） |
|---:|---|---|
| **M1** | **PI-01** `held-out ≥ 50` 之处置 | 5 件（`_s4_topup_intake_recompute` §6-1／`_s4_topup_intake_verdict` §5-2／`_s4_open_questions_intake_recompute` §7-1／`_is_corr_pair_caliber_revision_proposal` §6.3-4／`_kv3s_4_terminal_verdict` §6-2） |
| **M2** | **PI-02** 分母域择域 | 5 件（`_kv3s_4_terminal_verdict` §6-4／`_s4_substrate_refreeze_register_179` §8-2／`_k_v3s_4_3_frozen_recompute` §11-2／`_s4_terminal_face_recompute` §7-4／`_s4_face_v2_sync` §9-6） |
| **M3** | **PI-05** `is_corr_pair` 口径 ＋ `-E`／`-F` | 4 件（`_is_corr_pair_caliber_revision_proposal` §6.3-1/2/3／`_s4_substrate_freeze_register` §7-1／`_k_v3s_4_3_frozen_recompute` §11-4／`_s4_face_v2_sync` §9-8） |
| **M4** | **VK-01／VK-02** `K-V3S-4-*` 三线判档 | 5 件（`_s4_terminal_face_recompute` §7-1／`_s4_substrate_refreeze_register_179` §8-1／`_kv3s_4_terminal_verdict` §6-1／`_k_v3s_4_3_frozen_recompute` §11-1／`_s4_face_v2_sync` §9-1） |
| **M5** | **W-01** S4 面五线 CI 读数 0 有 | 5 件（`_s4_face_five_lines_ci_readings` §9-1／`_ci_three_items_effectivity_register` §8-2／`_ci_four_items_effectiveness_register` §7-3／`_ci_degradation_binding_form_a_register` §7-4／`_ci_gap_fill_alt_bc_aper_prime` §9-5） |
| **M6** | **P-01** PI 裁卡原件 0 落册 | 7 件同族（卡 id 见 §1.5 P-01 行） |
| **M7** | **V-03** `169 ≠ 171` 打印表分歧成因 | 4 件（`_s4_face_sync` §8-1／`_s4_face_v2_sync` §9-2／`_s4_terminal_face_recompute` §7-9／`_kv3s_4_terminal_verdict` §6-10） |
| **M8** | **EP-01** `21f2926efc5d` §2.2 第 7 行件名转录笔误 | 3 件（`_s4_face_sync` §8-2／`_s4_face_v2_sync` §9-4／`_s4_terminal_face_recompute` §7-8） |
| **M9** | **PI-04** C-1 线之复核面（K-1／K-2／estimand／等效门柱／A′） | 6 件（`_ci_degradation_binding_form_a_register`／`_ci_bc_scope_estimand_judgments`／`_ci_three_items_effectivity_register`／`_ci_four_items_effectiveness_register`／`_ci_gap_fill_alt_bc_aper_prime`／`_ci_bc_lines_ci_collection`） |
| **M10** | **PI-03** C-1 CI 线七要素 | 2 件（`_ci_line_establishment` §8-1～7／`_ci_width_halfwidth_pin` §8-3/4/5） |
| **M11** | **PI-16／PI-15** `E3-②` ＋ `K-CF-4` 分档 | 4 件（`_k_cf_4_effectivity_register` §E-1／`_k_cf_4_low_cardinality_recure` §12-4／`_k_cf_4_low_cardinality_reurecheck_and_precedent_fill` §10-6／`_kd_resolvability_and_optional_experiments` §4.2 N-2） |
| **M12** | **PI-39／EP-05** V3-02 覆裁执行面次生残留 | 2 件（`_v3_02_ethard_closure_verdict` §6／`_v3_02_ethard_execution_register` §9） |

> **⚠ 归并口径**：**51 节锚**（窗口 41 件含本件 3 锚 ＋ v1 边界件 1 锚）经 M1–M12 共 **12 簇**归并后，得 **59 组**增量未闭项（与 §1.7 计数自洽）。⛔ 0 因归并而丢弃任何独立事项；**每簇均可回溯至原始节锚**。

---

## §4 遗漏扫描结果

### §4.1 扫描面与口径

| 项 | 内容 |
|---|---|
| **扫描面** | ① **增量窗口**：`results/` 下 mtime > 12:45:09 之全部件（**73 件** ＝ `.md` 63 ＋ `.json` 9 ＋ `.py` 1）；② **v1 域**：同日（名称含 `2026_10_09`）且 mtime ≤ 12:45:09 之件（**35 件** ＝ `.md` 32 ＋ `.json` 2 ＋ `.py` 1） |
| **判定口径** | 「**已覆盖**」＝ 该件之候 PI 面**已见于 v1 主表 60 条**或**本件 §1／§3 归并簇**；「**0 独立候 PI 面**」＝ 经**节标题扫描 ＋ PI 面词密度探测**后无可归并之未闭项 |
| **⛔ 0 编造** | 「0 命中」**不等于**实体不存在；本件 ⛔ 0 逐行通读 32 件 v1 域件（v1 已采**头部核读口径**，本轮沿用同款**头部／节级**口径） |

### §4.2 增量窗口面：63 件 `.md` 逐件覆盖结论

| 面 | 件数 | 覆盖状态 |
|---|---:|---|
| **带「候呈/未闭/须裁」节标题** | **41** | ✅ **全覆盖** —— 逐件抽取节标题与条目，**51 节锚全部归入 §1／§3**（其中本件自身 3 锚、v1 边界件 1 锚、窗口漂移新件 2 锚） |
| **⛔ 0 节标题** | **22** | ✅ **逐件探测后归类**（见 §4.2.1），**0 遗漏** |

#### §4.2.1 22 件「0 节标题」之逐件归类（**探测依据 ＋ 结论**）

| # | 件名 | 探测结论 | 归入 |
|---:|---|---|---|
| 1 | `_k_v3df_scope_two_judgments_2026_10_09.md` | 出「**须 PI 给的最小问题**」出口表 | → **PI-14**（P-2／P-3 同族） |
| 2 | `_k_v3s_4_4_2_domain_extension_judgment_2026_10_09.md`※ | 「**不及于** `K-V3S-4-2` substrate 腿」建议，**须 PI 复核生效** | → **PI-30** |
| 3 | `_kv3s_4_terminal_verdict_supplement_2026_10_09.md` | 载 CI 阈值腿**已闭**（`0.1100`）＋ B/C 适用面与 estimand **仍待 PI 复核** | → **PI-04** ＋ 佐证 §3.2-2 |
| 4 | `_questionnaire_cards_intake_register_2026_10_09.md`（442,288 B） | 问卷卡**入册登记**（卡答逐字与指纹对位）；**非候裁面** | ✅ **0 独立候 PI 面** |
| 5 | `_questionnaire_cards_intake_register_supplement_2026_10_09.md`（72,199 B） | 同上之补编 | ✅ **0 独立候 PI 面** |
| 6 | `_r_pair4_design_and_texts_2026_10_09.md` | `[PI 给定]-C`～`-F` 勾选栏 ☐ 待填 ＋ RPQ-4／RPQ-5 | → **PI-20／PI-24／PI-25** |
| 7 | `_r2_verdict_179domain_arith_verification_2026_10_09.md` | 179 域算术核验（指纹对位 MATCH） | ✅ **0 独立候 PI 面**（属 VK-01 之证据面） |
| 8 | `_s4_face_dual_files_verification_2026_10_09.md` | 双件面核验，R3／R4 归 PI 面 | → **PI-01／PI-02／PI-05** |
| 9 | `_s4_final_ruling_card_register_2026_10_09.md`（2,135 B） | 终裁卡**登记件** | ✅ **0 独立候 PI 面**（其候呈由 `_s4_final_ruling_effectivity_register` 承载） |
| 10 | `_s4_heldout_sampling_caliber_ruling_2026_10_09.md` | R1–R4 待裁清单 ＋ **待 PI 复核生效** | → **PI-06** |
| 11 | `_s4_open_questions_design_2026_10_09.md` | 题数上限属 PI 裁量；18 件减为 14 件须 PI 明示 | → **PI-27** |
| 12 | `_t1_gate_revision_draft_2026_10_09.md` | E-要素条文草拟；**PI 复核核准、生效即锁 ⛔ 未复核** | → **PI-07** |
| 13 | `_t1_o1_design_axis_exemption_judgment_2026_10_09.md` | 「须 PI 显式给出者」表 | → **PI-07** |
| 14 | `_t1_p2_aggregation_caliber_judgment_2026_10_09.md` | 「须 PI 给之要素」表 | → **PI-10** 之 P-2 面 |
| 15 | `_t1_qwen_temp_sweep_r2_exec_register_2026_10_09.md` | 执行登记（**0 起跑**） | ✅ **0 独立候 PI 面** |
| 16 | `_t1_r2_activation_2026_10_09.md` | activation 起跑授权登记 | ✅ **0 独立候 PI 面**（其 P-6 补记义务 → **Δ-W-1**） |
| 17 | `_t1_r2_d1_field_caliber_correction_2026_10_09.md` | D-1 勘正件（⛔ 0 改既有件） | → **PI-11** 之执行面 |
| 18 | `_th_id_attribution_verification_2026_10_09.md` | `TH-*` 引用有误之 verifier 判定 | → **V-09** |
| 19 | `_th_id_miscitation_correction_2026_10_09.md` | 误引勘正（**原件 0 回改**） | → **V-09** 之落地面 |
| 20 | `_th_t1_n_min_revision_proposal_2026_10_09.md` | 丙档「新值**须 PI 给**，本件 ⛔ 不代拟」 | → **PI-13** |
| 21 | `_v3_02_ethard_execution_register_2026_10_09.md` | §9 残留／副产物／未做面 | → **EP-05／W-06** |
| 22 | `_v3_02_override_register_2026_10_09.md` | 覆裁登记（「0 代裁乙档内 PI 未明示之细节」） | → **PI-39** |

> ※ 件名实为 `_k_v3s_4_2_domain_extension_judgment_2026_10_09.md`（本表行 2 之笔误，已当场更正）。

> **✅ 增量窗口面结论：已扫 73 件（含 63 件 `.md` 全量 ＋ 9 件 `.json` ＋ 1 件 `.py` 之同族登记面核读 ＋ 2 件 `.pyc` 副产物排除声明），**0 遗漏**。**

### §4.3 **v1 域覆盖缺口**（本轮新发现 · 供 parent／PI 裁）

> v1 之覆盖为**「源件清单驱动」**（十汇总源 ＋ 6 closing-round ＋ 3 forgotten ＝ 19 件显式枚举），⛔ **非「当日件清单驱动」**。本轮以件名单为面反查，得 **9 件 v1 域当日 `.md` 既不在 v1 显式枚举面内、又含 PI 待裁／未闭节**：

| # | 件名（mtime ≤ 12:45:09） | PI 面节 |
|---:|---|---|
| **1** | `_archive_ledger_rectification_register_2026_10_09.md` | §6 在册遗留（0 新裁 · **仅登记待 PI**） |
| **2** | `_backfill_rule_final_2026_10_09.md` | §8 **未闭 · 移交**（如实列 · 0 掩盖 · 0 代裁） |
| **3** | `_c_reading_recompute_2026_10_09.md` | §6 未闭 · 移交（如实列 · 0 代裁） |
| **4** | `_e2_glm2_distill_side_receipt_register_2026_10_09.md` | §4 **候 PI 项** |
| **5** | `_g4_controlled_reproduction_design_2026_10_09.md` | §8 交棒指向（0 派工 · **候 PI 裁**） |
| **6** | `_g4_e3_definition_ruling_material_2026_10_09.md` | 选项 D（留白 · **候 PI 自拟**）／§11 交棒指向（**候 PI 裁**） |
| **7** | `_g4_reproduction_execution_register_2026_10_09.md` | §8 交棒指向（0 派工 · **候 PI 裁**） |
| **8** | `_t1_prereg_revision_qwen_temp_sweep_2026_10_09.md` | §5 起跑条件（**候 PI 裁** · ⛔ 0 自裁）；件名载「待 PI 复核生效」 |
| **9** | `_u_closure_execution_register_2026_10_09.md` | §4 边界与遗留（如实交代，不虚报） |

> **⚠ 本件之处理**：⛔ **0 判读**其是否构成 v1 之失误，⛔ **0 补读其正文条目**，⛔ **0 擅自并入 §1 计数**。上表**仅登记「件名 ＋ 节标题 ＋ 节级存在性」**三项盘上可核事实。**是否补读并入总账，权属 parent／PI**。
> **⚠ 部分交叉**：其中 #6 之 E3 记法面、#8 之 T1 预登记面，与 v1 已列之 `E3-②`（§1 PI-16）、`K-T1-R1-1` 门禁面（§1 PI-07）**可能同物** —— ⛔ 本件**未逐行核对其条目**，故**不并入计数**。

### §4.4 遗漏汇总

| 面 | 已扫 | 遗漏 |
|---|---:|---:|
| **增量窗口（> 12:45:09）** | **73** | **0** |
| ├ 其中 `.md` 全量 | 63 | 0（41 件带节锚全登记 ＋ 22 件逐件归类） |
| ├ 其中 `.json` 数据面 | 9 | 0（**⛔ 0 逐件通读**；候呈项多登记于同族 `.md`，此为**如实限度**） |
| ├ 其中 `.py` 执行脚本 | 1 | 0（工具面 ⛔ 非候呈件） |
| └ `__pycache__` `.pyc` | 2 | 0（编译副产物 ⛔ 声明排除） |
| **v1 域（≤ 12:45:09 · 名称含日期）** | **35**（头部／节级口径） | **9 件未入 v1 显式枚举面**（见 §4.3） |
| **合计** | **108** | **窗口 0 遗漏 ＋ v1 域 9 件待裁** |

---

## §5 诚实限制

### §5.1 本件 0 做（铁律逐条）

- ⛔ **0 代裁**：0 择档、0 给阈值、0 断母件口径冲突、0 断销项之法律效力（**只呈盘上依据**）。
- ⛔ **0 推荐 · 0 排序暗示**：§1／§3 分组**不构成**次序、优先级或推荐档；§3.1 时间线**仅按 mtime 记录事实**。
- ⛔ **0 回改任何既有件**：全程只读 `Get-FileHash -Algorithm SHA256`／`read`／`grep`／`Get-ChildItem`／`Test-Path`／节级行抽取 ＋ **分段 `write`/`edit`（仅本件）**。**v1 件经落盘后复验：mtime 仍 12:45:09、bytes 仍 35,258、SHA-12 仍 `87ab4929477f` ＝ byte 0 触动**。
- ⛔ **0 编造**：核不到处写「**未核得**」并注明探测方式；⛔ 0 以「0 命中」推定实体不存在。
- ⛔ **0 网络** · ⛔ **0 端点调用** · ⛔ **0 skill** · ⛔ **0 读 key／0 读 `.env`** · **R4 key 永不明文**（本件 0 出现任何 key 片段）。
- ⛔ **0 阶段名自升**：所引 `V3`／`V4` 字样**仅为既有件既有字面引用**；本件名**不含 V-阶段前缀**。

### §5.2 未核得面（如实列明 · 0 编造）

1. **卡答原件之盘上落册 —— 8 张卡 id 全部未核得**：`ask_a9ce5b284c10bf1e36077e35`／`ask_2643fab3836ce14c466a1243`／`ask_68df18a1976c91fb18d19497`／`ask_92998b73d1b6cb2255391499`／`ask_4ce2001998037e107db9591c`／`ask_492645c357b2638d0aac0bb8`／`ask_1936c3a747b2c740a2c71b12`／`ask_42b717c5410863b425967094` —— 各件自载「全仓文本检索**命中 0**」且「本件照录之四答 ＝ **派工单所载字面之转录**」⇒ **本轮 ⛔ 0 复扫运行时库**（⛔ 0 读 SQLite／0 网络）⇒ 各卡之**答讫时点与选项全文**沿各件转录件登记，**0 以转录充原件**。
2. **增量窗口 9 件 `.json` 之逐条通读**：本轮**未逐件通读**（数据/读数载体）⇒ 其**内嵌**之候呈项**可能存在而未被本件抽取**。已核其**同族 `.md` 面 0 遗漏**（§4.2），但 ⛔ **0 声称 JSON 内 0 候呈面**。
3. **v1 域 32 件 `.md` 之逐行扫描**：本轮沿用 v1 之**头部／节级**口径（⛔ 0 逐行通读全 32 件）⇒ §4.3 之 9 件**仅登记节标题存在性**，⛔ **0 声称**其内部绝无候 PI 面。
4. **§4.3 之 9 件是否与 §1 已列项同物**：⛔ **0 逐行核对** ⇒ **不并入 §1.7 计数**。
5. **增量窗口为动态**：本件落盘期间（21:44–21:5x）实测 `_t1_prereg_revision_temp_axis_exp2_2026_10_09.md`（21:49:30）落盘 ⇒ **窗口计数 63 `.md` 为该时点快照**；本件扫描**未穷尽其后落盘之新件**。此为**如实限度**，非遗漏。
6. **计数自洽性**：§0.3 窗口 `.md` **63** 系 `-Filter` 单查询结果；本轮初次以 `-Include *.md` 递归过滤得 **61**，差 **2 件**。差异**源于 PowerShell `-Include` 递归语义**，本件**已在 §0.3 明示并以单一查询为准**，⛔ 0 隐瞒。
7. **v1 边界归属**：`mtime = 12:45:09.xxx`（含毫秒）之 v1 件在 `-gt $cut` 比较下**落入窗口**，故 §4.2 之 41 件带节锚含 v1 **1 锚**；本件**已在 §4.2 逐项扣除**，⛔ 0 双重计入。

### §5.3 本件计数与口径（供 parent 对账）

| 口径 | 计数 |
|---|---:|
| **扫描面总件** | **108**（窗口 73 ＋ v1 域 35） |
| **§1 未闭项组数（去重后）** | **84** ＝ PI 42 ／ VK 11 ／ worker 10 ／ verifier 9 ／ parent 7 ／ evidence-protocol 5 |
| **§1.8 窗口漂移新增组数** | **6**（PI 4 ／ worker 1 ／ parent 1），**另立编号不并入 84** |
| **§3.1 PI 卡答事件** | **9**（含 1 项 `status=pending` 未答） |
| **§3.2 生效登记事件** | **6** |
| **§3.3 归并簇** | **12**（M1–M12） |
| **§4 遗漏** | **窗口 0** ＋ **v1 域 9 件待裁** |
| **§5.2 未核得面** | **7 项** |

---

## §6 落盘自证

| 项 | 内容 |
|---|---|
| **落前撞名实测** | `Test-Path 'results/_pi_facing_items_screen_2026_10_09.md'` ＝ **False**（落盘前）⇒ ✅ **新名新建 · 0 覆写** |
| **件名合规** | `_pi_facing_items_screen_2026_10_09.md` ＝ `_主题_日期` ⇒ ✅ **0 V-阶段前缀 / 0 `_v5_` 类前缀 / 0 阶段号作首段** |
| **本件写动作** | **新增 1 件**（本件，分段 `write` ＋ `edit` 追加 4 次）；⛔ **0 编辑／0 覆写／0 追加／0 改名／0 移动／0 删除**任何既有件 |
| **v1 件复验** | `_pending_pi_items_master_register_2026_10_09.md`：SHA-12 `87ab4929477f` ／ bytes 35,258 ／ mtime 12:45:09 ⇒ **byte 0 触动** |
| **引用件只读** | 窗口 63 件 `.md` ＋ 9 件 `.json` ＋ 1 件 `.py` ＋ v1 域 32 件 `.md`（节级）：**byte 0 触动** |
| **编码／行尾** | **UTF-8 无 BOM · LF**（落盘后按字节复核：首 3 字节 **0 见** `EF BB BF`；全件 **CR 计数 ＝ 0**） |
| **R4** | key／`.env`／凭据 **0 读 · 0 落盘 · 0 入本件** |
| **网络／skill／LLM** | **0 网络** ｜ **0 skill** ｜ **0 LLM 代答** |
| **本件自身指纹** | ⛔ **不自写入本件**（自指回环）⇒ **随交付回执回报终态 SHA-256／bytes／CRLF 计数**；外部观测者请以 `Get-FileHash -Algorithm SHA256` 独立复算 |

### §6.1 关键源件实测指纹（本轮 `Get-FileHash -Algorithm SHA256` · SHA-12）

| 源件 | SHA-12 | bytes |
|---|---|---:|
| `_pending_pi_items_master_register_2026_10_09.md`（v1 基线） | `87ab4929477f` | 35,258 |
| `_s4_chain_clearance_register_2026_10_09.md`（清障卡答讫登记） | `eda3d304d381` | 2,684 |
| `_ci_line_establishment_2026_10_09.md`（CI 线立线） | `329c1c5e91d1` | 28,262 |
| `_ci_width_halfwidth_pin_2026_10_09.md`（CI 半宽钉定） | `51765f40f5f9` | 17,426 |
| `_kv3s_4_terminal_verdict_2026_10_09.md`（K 线终版判定） | `e51317fcc5cf` | 50,858 |
| `_s4_substrate_refreeze_register_179_2026_10_09.md`（179 面重冻） | `24ea764daeac` | 45,386 |
| `_t1_qwen_temp_sweep_r2_verdict_2026_10_09.md`（T1 r2 判定） | `9c18b9893579` | 42,817 |
| `_kd_resolvability_and_optional_experiments_2026_10_09.md`（KD 可解性） | `3138ac9095b0` | 70,328 |
| `_t1_prereg_revision_temp_axis_exp2_2026_10_09.md`（窗口漂移新件） | `2ff15aeeb5d0` | 34,217 |

> **⚠ 交叉验证**：`_ci_line_establishment` 之 SHA-12 `329c1c5e91d1` 与 `_ci_width_halfwidth_pin` 之 `51765f40f5f9`，在**多件候呈节正文中被互相引用为既有件 id** ⇒ 本轮实测值与**盘上引用面自洽**。

---

**落款**：**worker**（Mavis 团队分支 worker · 登记/对账类 · session `mvs_0cafb450acf14db9bb488cd8b0d04776` · 本件实际出件者｜署名如实）｜2026-10-09｜**候 PI 面 · 总账筛查 v2（重跑 · 精简版）**｜v1 基线 `87ab4929477f`（12:45:09）｜扫描面 **108 件**（窗口 73 ＋ v1 域 35）｜窗口 `.md` **63 件 · 51 节锚 · 41 件带锚 · 22 件逐件归类**｜**未闭项 84 组**（＋窗口漂移 6 组）｜PI 卡答事件 **9**（1 项 pending）｜生效登记 **6**｜归并簇 **12**｜**遗漏：窗口 0 ＋ v1 域 9 件待裁**｜未核得面 **7 项**｜**0 代裁 0 推荐 0 排序暗示 0 编造 0 回改 0 网络 · R4 永不明文 · 产出 1 件即停**