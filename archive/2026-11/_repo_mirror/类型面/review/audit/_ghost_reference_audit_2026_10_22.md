# 幽灵引用三审复核件（2026-10-22）

> **术语首现附白话**：**幽灵引用** ＝ 件里引了一个指纹或名字，但盘上找不到那件。
> 本件所称「指纹」＝ 12 位小写十六进制（SHA-12）；「所载 bytes」＝ 引文里跟着该指纹写的字节数。

## §0 自路径・时点・签棒

| 项 | 值 |
|---|---|
| 自路径 | `〔幽灵引用·未上传:_ghost_reference_audit_2026_10_22.md〕` |
| 前件（⛔ 0 回改） | `〔幽灵引用·未上传:_ghost_reference_register_2026_10_21.md〕`（`e927dfce3464`·21,235 B·2026-10-21 23:53:28） |
| 生成时点 | 2026-10-22 01:1x–01:3x（本棒观测时点窗口） |
| 签棒 | `evidence-auditor`（证据链审计官）· deposon「数据修订／资产处置」之证据链面 |
| 本棒性质 | **复核件**——自建仪器重测・逐条三审・0 代裁・0 落五终判・0 闭 KD・0 宣告段毕 |

**⛔ 本件之射程**：只判「本机四区（在盘可核面）之在盘与否及其形态」。**⛔ 0 判「不存在于任何世界」**；远端面（GitHub 认可面）**⛔ 0 联网・未测**，一律记「未核·须 PI 或另授权」。

## §1 仪器（自建 v2）・口径・可复算

### 1.1 扫描面与索引面

| 面 | 范围 | 件数 | 备注 |
|---|---|---|---|
| 源面（引文所在） | `deposon-repo\results\**\*.md` ＋ `deposon-repo\pi_rulings\**\*.md` | **1294** 件 | 含 `.tmp\` 之工作面；较前件（469 件）扩大 2.8 倍 |
| 索引面 A | `deposon-repo` 全域 | 6,706 | 全部件逐件 SHA-256 ＋ SHA-1 ＋ git-blob-SHA-1 |
| 索引面 B | `deposon-sub` | 1,276 | 同上 |
| 索引面 C | `GLM` | 21 | 同上 |
| *索引面小计* | *三区逐件全索引* | **8,003** | *遍历错误 0·读错 0* |
| 索引面 D（域外） | `〔本地路径已脱敏〕`／`plugin-cache`／`sessions` ＋ D 盘同构 | **5250** 件实扫（2055 唯一 SHA-12） | runtime 面；**不在四区之内**，故须单列「域外引用型」 |
| 归档区 | `〔归档区〕` | **40,121** 件 | **⛔ 0 触其内件**——仅列名与件数；最新 mtime 2026-10-18 16:19:24 |

### 1.2 抽取口径（v2・收紧后）

**指纹正则**：`(?<![0-9a-fA-F-])[0-9a-f]{12}(?![0-9a-fA-F-])`——后顾负向断言排除 UUID 末段 12-hex（如 `bg_be35e9a8-…-d4f00397473a` 之末段），前瞻断言排除更长 hex 串之内含匹配。

**字节面正则**：指纹前后 40 字内，数字面须为**逗号千分位**（`22,733`）**或**带单位标记（`105 B`／`bytes`／`字节`），其间不得含字母数字。

**成对总体**：**6,951** 唯一指纹／**7106** 候选对（sha12×bytes 去重）。另以「须带单位」之严口径重抽，得 **4700** 对／4651 唯一指纹（供与前件及独立清点棒对账）。

### 1.3 仪器自审两轮（测量仪器自身即误差源）

**v1（首跑）**：得 18,008 唯一 hex／46,620 候选对——**远超**独立清点棒之 1,939。逐条查样后定位噪声源有二：

| # | 噪声源 | 样貌 | 处置 |
|---|---|---|---|
| ① | **UUID 末段 12-hex** | `bg_be35e9a8-4b49-4e5e-b8ad-d4f00397473a` 之末段 | v2 加前置连字符负向断言 |
| ② | **邻近任意大数即成对** | 指纹旁 90 字内任一逗号千分位数字被误取为「所载 bytes」 | v2 改「40 字内＋分隔符不含字母数字＋须千分位或带单位」 |

**v2（收紧后）**：唯一 hex 降至 **13,394**（其中成对者 **6,949**）。**且 v2 于本仓四位「举例」上逐一复现**——此为本棒仪器之校准凭据，非本棒结论：

| 本仓派工所举之例 | 本棒 v2 实测落位 | 判定 |
|---|---|---|
| `0a314eed103a` → C 盘 plugin-cache | `〔本地路径已脱敏〕`·13,044 B | ✔ **域外引用型** |
| `4fc0d746af9d`·105 B（SHA-1 git blob 口径） | `deposon-repo\.gitignore`·105 B·git-blob-SHA-1 命中 | ✔ **口径型** |
| `1442a1296936`·423,375 B（子棒版备忘录旧前缀） | `results\_root_session_history_memo_2026_10_14.md`（现 **558,430 B**）之**前 423,375 字节** SHA-256 逐位吻合 | ✔ **态变型** |
| `fd39cf811232`·236,425 B → 今 `8baa9854b3f7`·239,700 B | 旧＝`.minimax\v2\assets\…-查理_deposon双主线论文终稿_2026-10-01_v0.3.md`；今＝`deposon-repo\letters\查理_deposon双主线论文终稿_2026-10-01_v0.3.md` | ✔ **版本漂移型** |

### 1.4 阳性对照（仪器可用性之自证）

同一批同法扫描于成对总体中命中 **4314** 件在盘实体之 SHA-256（其中字节亦吻合者 4117 件、同哈希多份 195 件、字节陈旧 2 件）——如 `bb66c577673b`＝`鲍勃_minimax实验委托规格包_2026_10_12.md`·14,758 B、`44311ade19de`＝`letters\REPLY_FROM_GEMINI4_GE01_THEORY_INPUTS_2026_10_15.md`·44,520 B、`793986174b23`＝`results\_gemini4_reply_verification_register_2026_10_15.md`·33,393 B ⇒ 仪器非「恒 0」。

---

## §2 汇总表（六类计数）

| 终态 | 义（白话） | 件数 | 占成对总体 |
|---|---|---|---|
| **真幽灵** | 实体 0 在本机四区＋域外面（指纹、字节、前缀、口径四径皆不命中） | **1350** | 19.4% |
| **版本漂移型** | 旧指纹已亡，但**同一实体名＋近字节之现行件在盘**（改指候选） | **31** | 0.4% |
| **域外引用型** | 实体在 runtime／plugin-cache 面（不在四区） | **16** | 0.2% |
| **口径型** | 实体在盘，然引文所载指纹为 **SHA-1 git blob** 口径（非 SHA-256） | **1105** | 15.9% |
| **态变型** | 实体在盘且为**活件续写**致指纹／字节陈旧（旧前缀或字节陈旧） | **137** | 2.0% |
| **待辨** | ⛔ 不设此态——每条必得终态之一 | **0** | 0.0% |
| *（小计：六类）* | | **2639** | 38.0% |
| *（非幽灵：sha256 命中且字节吻合）* | 实体确在盘 | 4117 | 59.2% |
| *（非幽灵：同哈希多份 SAME_IDENTITY，不重复计数）* | 同件存多份 | 195 | 2.8% |
| **成对总体** | 唯一 sha12×所载 bytes 成对之指纹 | **6951** | 100.0% |

**⛔ 待辨 ＝ 0**——6951 件成对指纹逐条得终态，无一件挂「不明」。

## §3 四件点名幽灵・专节

> 四件皆经**三路探法**＋**阴性断言三审**（扫描完整性／模式与命名是否结构性互斥／时点新鲜）逐件复核。**⛔ 0 判「不存在于任何世界」——只判「本机四区 0 实存」。**

### §3-4228 `4228142806c5`——《待裁项团队决议》本体（22,733 B）

| 项 | 值 |
|---|---|
| 所指名 | 《待裁项团队决议》本体 |
| 所载 bytes | 22,733 B |
| 被引次数 | **95**（本棒 md 内出现次数） |
| 引者件 | **34** 件（distinct md） |
| 四区在盘 | **0** |
| 终态 | **真幽灵**（本机四区＋域外面 0 实存） |

**探法**：①**文件名 glob**（三区全量名 ＋ 归档区仅名）——`*待裁*`／`*团队决议*`／`*裁定项*` **各 0 命中**；归档区 40,121 件名中「待裁」「团队决议」**各 0 命中**。②**历史登记路径字面**——语料所载名为《待裁项团队决议》（`_batch7_deliberation_judgment_2026_10_13.md` L157 载「在册载《待裁项团队决议》／22,733 B／200 L」），**0 在盘路径字面**。③**内容哈希**——SHA-256／SHA-1／git-blob-SHA-1／旧前缀四径**皆 0 命中**。

**阴性断言三审**：①**扫描完整性**——三区 os.walk 遍历错误 **0**、读错 **0**（8,003 件全索引）；归档区仅名之遍历错误 **0**（40,121 件）。②**模式与命名是否结构性互斥**——**不互斥**：实体名为中文「待裁项团队决议」，探针 `*待裁*` 足以正面命中该名，故「0 命中」具实证意义（阴性**有效**）。③**时点新鲜**——本棒 2026-10-22 01:0x–01:3x 实测窗口，非沿用 10-21 读数。

**三径荐案**：甲＝**PI 取回**（其达 GitHub 之径归 PI；PI 2026-10-18 裁「GLM 只认 GitHub」⇒ 本地面不充当到位）；乙＝**辨明替代**——以语料转引层（`_buexp_backfill_deliberation_2026_10_21.md` §E-1、`_batch11_deliberation_judgment_2026_10_14.md` KD-4）所载之效力面**限缩使用**，⛔ 0 以转引充原件；丙＝**挂账**（登记为限制面，候 PI 一字）。**本棒荐：甲优先・乙并行・丙兜底；不代裁。**

**引者件与行（列全）**：

- `pi_rulings/_pi_card_answers_register_2026_10_21_v198.md`:23
- `pi_rulings/_pi_card_answers_register_2026_10_21_v199.md`:37
- `pi_rulings/_pi_card_answers_register_2026_10_21_v227.md`:18
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:103
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:176
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:176
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:274
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:493
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:578
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:599
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:601
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:603
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:606
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:607
- `results/.tmp/_s16_body_2026_10_21.md`:168
- `results/_batch11_deliberation_judgment_2026_10_14.md`:30
- `results/_batch11_deliberation_judgment_2026_10_14.md`:114
- `results/_batch11_deliberation_judgment_2026_10_14.md`:144
- `results/_batch11_deliberation_judgment_2026_10_14.md`:169
- `results/_batch11_deliberation_judgment_2026_10_14.md`:179
- `results/_batch11_deliberation_judgment_2026_10_14.md`:185
- `results/_batch7_deliberation_judgment_2026_10_13.md`:49
- `results/_batch7_deliberation_judgment_2026_10_13.md`:157
- `results/_batch7_deliberation_judgment_2026_10_13.md`:160
- `results/_batch7_deliberation_judgment_2026_10_13.md`:172
- `results/_bob_commission_acceptance_and_r4_waiver_register_2026_10_12.md`:55
- `results/_bob_commission_acceptance_and_r4_waiver_register_2026_10_12.md`:80
- `results/_bob_commission_acceptance_and_r4_waiver_register_2026_10_12.md`:92
- `results/_bob_minimax_commission_family_intake_register_2026_10_12.md`:76
- `results/_bob_minimax_commission_family_intake_register_2026_10_12.md`:85
- `results/_bob_minimax_commission_family_intake_register_2026_10_12.md`:131
- `results/_bob_minimax_commission_family_intake_register_2026_10_12.md`:148
- `results/_buexp_backfill_deliberation_2026_10_21.md`:276
- `results/_c5_split_into_c5a_c5b_2026_10_17.md`:207
- `results/_c5_split_into_c5a_c5b_2026_10_17.md`:230
- `results/_cleanup_noise_register_2026_10_21.md`:210
- `results/_gd03_caliber_note_2026_10_20.md`:70
- `results/_gd03_divergence_deliberation_2026_10_21.md`:72
- `results/_gd03_divergence_deliberation_2026_10_21.md`:190
- `results/_gd03_divergence_deliberation_2026_10_21.md`:191
- `results/_gd03_divergence_deliberation_2026_10_21.md`:248
- `results/_gd03_divergence_deliberation_2026_10_21.md`:272
- `results/_gd03_divergence_deliberation_v2_2026_10_21.md`:106
- `results/_gd03_divergence_deliberation_v2_2026_10_21.md`:167
- `results/_gd03_divergence_deliberation_v2_2026_10_21.md`:229
- `results/_gd03_divergence_deliberation_v2_2026_10_21.md`:234
- `results/_gd03_divergence_deliberation_v2_2026_10_21.md`:234
- `results/_gd03_divergence_deliberation_v2_2026_10_21.md`:235
- `results/_gd03_divergence_deliberation_v2_2026_10_21.md`:289
- `results/_gd03_divergence_deliberation_v2_2026_10_21.md`:345
- `results/_gd03_divergence_deliberation_v2_2026_10_21.md`:346
- `results/_gd03_divergence_deliberation_v2_2026_10_21.md`:393
- `results/_ge01_c5_disposition_register_2026_10_14.md`:131
- `results/_ge01_c5_disposition_register_2026_10_14.md`:131
- `results/_ge01_c5_disposition_register_2026_10_14.md`:138
- `results/_ge01_freeze_flow_execution_2026_10_20.md`:167
- `results/_ge01_prereg_seven_requirements_draft_2026_10_13.md`:105
- `results/_ge01_prereg_seven_requirements_draft_2026_10_13.md`:194
- `results/_ge01_readiness_adjudication_2026_10_21.md`:131
- `results/_ge01_readiness_adjudication_2026_10_21.md`:135
- `results/_ge01_readiness_adjudication_2026_10_21.md`:186
- `results/_ge01_readiness_adjudication_2026_10_21.md`:223
- `results/_ge01_readiness_adjudication_2026_10_21.md`:236
- `results/_ge01_readiness_adjudication_2026_10_21.md`:287
- `results/_ge01_readiness_adjudication_2026_10_21.md`:287
- `results/_ge01_readiness_after_prereg_effect_2026_10_13.md`:119
- `results/_ge01_readiness_after_prereg_effect_2026_10_13.md`:119
- `results/_ge03_ge04_claim_proposal_2026_10_22.md`:139
- `results/_ge03_ge04_definition_deliberation_2026_10_21.md`:105
- `results/_ge03_ge04_definition_deliberation_2026_10_21.md`:160
- `results/_ghost_reference_register_2026_10_21.md`:28
- `results/_ghost_reference_register_2026_10_21.md`:35
- `results/_glm_reply_pack_intake_verification_2026_10_19.md`:192
- `results/_glm_reply_pack_intake_verification_2026_10_19.md`:192
- `results/_night_mode_adoption_and_registry_2026_10_14.md`:164
- `results/_replies_arrival_and_stage2_restore_directive_effect_2026_10_19.md`:9
- `results/_root_session_history_memo_2026_10_14.md`:3404
- `results/_root_session_history_memo_main_2026_10_14.md`:1421
- `results/_stage1_prereq_wave1_evidence_2026_10_20.md`:88
- `results/_stage1_prereq_wave1_evidence_2026_10_20.md`:88
- `results/_stage1_prereq_wave1_evidence_2026_10_20.md`:237
- `results/_stage1_prereq_wave1_evidence_2026_10_20.md`:307
- `results/_stage1_prereq_wave1_evidence_2026_10_20.md`:368
- `results/_stage1_prereq_wave1_evidence_2026_10_20.md`:371
- `results/_stage1_prereq_wave1_proposals_2026_10_20.md`:490
- `results/_t4_key_preexp_killline_prereg_2026_10_21.md`:534
- `results/_v172_adoption_effect_2026_10_20.md`:245
- `results/_v172_adoption_effect_2026_10_20.md`:457
- `results/_v186_v225_adoption_effect_2026_10_22.md`:613
- `results/_v226_v230_adoption_effect_2026_10_22.md`:167
- `results/_v226_v230_adoption_effect_2026_10_22.md`:232
- `results/_v226_v230_adoption_effect_2026_10_22.md`:379
- `results/_v226_v230_adoption_effect_2026_10_22.md`:379
- `results/_v226_v230_adoption_effect_2026_10_22.md`:415
- `results/_v226_v230_adoption_effect_2026_10_22.md`:717

### §3-fddc `fddc14e6da27`——爱丽丝_仓态进展与前置事实核查_2026_10_18（15,264 B）

| 项 | 值 |
|---|---|
| 所指名 | 爱丽丝_仓态进展与前置事实核查_2026_10_18 |
| 所载 bytes | 15,264 B |
| 被引次数 | **35**（本棒 md 内出现次数） |
| 引者件 | **11** 件（distinct md） |
| 四区在盘 | **0** |
| 终态 | **真幽灵**（本机四区＋域外面 0 实存） |

**探法**：①**文件名 glob**——`*爱丽丝*` 三区仅 **1 命中**：`GLM\爱丽丝_v11增量双审A路报告_2026_10_19.md`（`ca040f35eae8`·18,486 B，**异名异尺非该实体**）；`*仓态*`／`*前置事实*` **各 0 命中**。②**历史登记路径字面**——语料载名 `爱丽丝_仓态进展与前置事实核查_2026_10_18.md`（`_ge03_ge04_definition_deliberation_2026_10_21.md` L143 逐字），**0 在盘路径字面**；归档区名中「爱丽丝」「仓态」**各 0 命中**。③**内容哈希**——四径**皆 0 命中**。

**阴性断言三审**：①**扫描完整性**——同 §3-1 ①，遍历错误 **0**。②**模式与命名是否结构性互斥**——**不互斥**：实体名含「爱丽丝」，探针可正面命中；唯一命中件之字节 18,486 ≠ 15,264 ⇒ 阴性**有效**（已证「同族异件」之存在，不改判）。③**时点新鲜**——同 §3-1 ③。

**三径荐案**：甲＝**PI 取回**；乙＝**辨明替代**——其「登记件 §4」之字面已由语料两读并出指代（读甲＝GLM 10-18 回函主表序 78／读乙＝鲍勃 10-18 执行计划 v1.1 之 §1.4，**两读不可唯一判定**，归 PI 一字）；本棒⛔ 0 强合。丙＝**挂账**（`pi_rulings` v214-Q2 已采「三面 0 实存・真缺件」，本棒复核同值）。**本棒荐：乙＋丙并行，甲俟 PI 之径；不代裁。**

**引者件与行（列全）**：

- `pi_rulings/_pi_card_answers_register_2026_10_21_v214.md`:19
- `pi_rulings/_pi_card_answers_register_2026_10_21_v214.md`:36
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:284
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:297
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:493
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:578
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:599
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:601
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:603
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:607
- `results/.tmp/_s16_body_2026_10_21.md`:155
- `results/_cleanup_noise_register_2026_10_21.md`:210
- `results/_ge03_ge04_claim_proposal_2026_10_22.md`:129
- `results/_ge03_ge04_claim_proposal_2026_10_22.md`:136
- `results/_ge03_ge04_claim_proposal_2026_10_22.md`:311
- `results/_ge03_ge04_definition_deliberation_2026_10_21.md`:105
- `results/_ge03_ge04_definition_deliberation_2026_10_21.md`:143
- `results/_ge03_ge04_definition_deliberation_2026_10_21.md`:158
- `results/_ge03_ge04_definition_deliberation_2026_10_21.md`:235
- `results/_ge03_ge04_definition_deliberation_2026_10_21.md`:341
- `results/_ghost_reference_register_2026_10_21.md`:29
- `results/_ghost_reference_register_2026_10_21.md`:37
- `results/_root_session_history_memo_2026_10_14.md`:3391
- `results/_stage1_prereq_wave1_evidence_2026_10_20.md`:85
- `results/_stage1_prereq_wave1_evidence_2026_10_20.md`:97
- `results/_stage1_prereq_wave1_evidence_2026_10_20.md`:236
- `results/_stage1_prereq_wave1_evidence_2026_10_20.md`:268
- `results/_stage1_prereq_wave1_evidence_2026_10_20.md`:307
- `results/_stage1_prereq_wave1_evidence_2026_10_20.md`:368
- `results/_stage1_prereq_wave1_evidence_2026_10_20.md`:371
- `results/_v172_adoption_effect_2026_10_20.md`:245
- `results/_v172_adoption_effect_2026_10_20.md`:457
- `results/_v186_v225_adoption_effect_2026_10_22.md`:195
- `results/_v186_v225_adoption_effect_2026_10_22.md`:930
- `results/_v186_v225_adoption_effect_2026_10_22.md`:931

### §3-4fa1 `4fa15c554d93`——Gemini4 GE01 理论输入回函之核验登记件（33,403 B）

| 项 | 值 |
|---|---|
| 所指名 | Gemini4 GE01 理论输入回函之核验登记件 |
| 所载 bytes | 33,403 B |
| 被引次数 | **26**（本棒 md 内出现次数） |
| 引者件 | **8** 件（distinct md） |
| 四区在盘 | **0** |
| 终态 | **真幽灵**（本机四区＋域外面 0 实存） |

**探法**：①**文件名 glob**——`*核验登记*` **0 命中**（**中文名对英文名文件结构性盲**）；补以 `*gemini4*`／`*ge01*`／`*核验*`：**`*gemini4*` 4 命中**，其中 `results\_gemini4_reply_verification_register_2026_10_15.md`（`793986174b23`·**33,393 B**）——其 L1 标题逐字为「gemini4 回函 · **核验登记件**」、L13 自报核验对象 `letters/REPLY_FROM_GEMINI4_GE01_THEORY_INPUTS_2026_10_15.md`（`44311ade19de`·44,520 B）——**语义正名，而指纹异、字节差 10**。②**历史登记路径字面**——`_glm_unique_reply_117_triage_2026_10_19.md` L118 逐字载「核验登记件 `4fa15c554d93`·33,403 B **在仓实测同值**；回函本体 `44311ade19de`·44,520 B 系核验件转引」。③**内容哈希**——四径**皆 0 命中**；但**回函本体 `44311ade19de` 在盘吻合**（`letters\REPLY_FROM_GEMINI4_GE01_THEORY_INPUTS_2026_10_15.md`·44,520 B），且该件**在 10-19 即被载为「在仓实测同值」**。

**阴性断言三审**：①**扫描完整性**——遍历错误 **0**；阳性对照命中 8,015 件之在盘实体 ⇒ 仪器非恒 0。②**模式与命名是否结构性互斥**——**此处须分两读并出**：读甲（窄）＝`*核验登记*` 对英文名文件**结构性盲**，「0 命中」**不具**判别力；读乙（宽）＝`*gemini4*` 可正面命中，**命中之件语义正名而指纹异**（33,393 vs 33,403）⇒ 阴性断言在「同名同尺」面上**成立**，在「语义同一实体」面上**不成立**。⛔ 0 强合两读。③**时点新鲜**——本棒实测窗口；且「在仓实测同值」之断言系 **10-19** 之读数（`_cluster_j_glm_62_adjudication_2026_10_19.md` L155），10-20 已记「本棒 0 复核」、本棒 0 复核 ⇒ **该「在仓」之历史断言于今不可复现**。

**三径荐案**：甲＝**PI 取回**（旧指纹本体之实件）；乙＝**辨明替代**——**最强一径**：现行件 `results\_gemini4_reply_verification_register_2026_10_15.md`（`793986174b23`·33,393 B）在**语义、对象、条目体例**上与所引之核验登记件同一族，**仅字节差 10、指纹不同**⇒ 须由 PI 一字认定「引文所称者是否即此件之旧版」，认定后即可**改指**（②）；丙＝**挂账**（若不认定，则该「在仓实测同值」之表述须作**限制面**登记，⛔ 0 断言其因——移动／删除／他处均未判）。**本棒荐：乙优先，甲俟 PI 之径，丙兜底；不代裁。**

**引者件与行（列全）**：

- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:32
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:277
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:302
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:450
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:456
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:493
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:575
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:578
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:599
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:601
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:605
- `results/_cleanup_noise_register_2026_10_21.md`:210
- `results/_cluster_j_glm_62_adjudication_2026_10_19.md`:155
- `results/_ge03_ge04_definition_deliberation_2026_10_21.md`:105
- `results/_ge03_ge04_definition_deliberation_2026_10_21.md`:161
- `results/_ghost_reference_register_2026_10_21.md`:30
- `results/_ghost_reference_register_2026_10_21.md`:36
- `results/_glm_unique_reply_117_triage_2026_10_19.md`:118
- `results/_stage1_prereq_wave1_evidence_2026_10_20.md`:176
- `results/_stage1_prereq_wave1_evidence_2026_10_20.md`:235
- `results/_stage1_prereq_wave1_evidence_2026_10_20.md`:307
- `results/_stage1_prereq_wave1_evidence_2026_10_20.md`:368
- `results/_stage1_prereq_wave1_evidence_2026_10_20.md`:371
- `results/_stage1_prereq_wave1_evidence_2026_10_20.md`:379
- `results/_v172_adoption_effect_2026_10_20.md`:245
- `results/_v172_adoption_effect_2026_10_20.md`:457

### §3-cf04 `cf04fc2f39db`——《全量补实验执行计划 v1》（36 条之原始分派基底）（14,904 B）

| 项 | 值 |
|---|---|
| 所指名 | 《全量补实验执行计划 v1》（36 条之原始分派基底） |
| 所载 bytes | 14,904 B |
| 被引次数 | **25**（本棒 md 内出现次数） |
| 引者件 | **8** 件（distinct md） |
| 四区在盘 | **0** |
| 终态 | **真幽灵**（本机四区＋域外面 0 实存） |

**探法**：①**文件名 glob**——`*全量补实验*`／`*执行计划*`／`*计划*` 三区**各 0 命中**；归档区 40,121 件名中**各 0 命中**（且归档区**0 个 `shared/` 目录**）。②**历史登记路径字面**——**已取得**，且为**远端仓根相对路径**：规格包本体 `results\_r5_spec_pack_retrieved_2026_10_13\鲍勃_minimax实验委托规格包_2026_10_12.md`（`bb66c577673b`·14,758 B·在盘）L5 逐字载「**分派基底**：《全量补实验执行计划》36 条（`shared/鲍勃_全量补实验执行计划_2026_10_12.md`，`cf04fc2f39db`／14,904 B）」，其 L7 载远端基线锚「zeroandcat/Deposon main @ `9de6fd7`」（远端路径相对仓根，`results/`＝`_september_workspace/results/`）。③**内容哈希**——四径**皆 0 命中**；**归档区 0 `shared/` 目录** ⇒ 其镜像面亦不在本地。

**阴性断言三审**：①**扫描完整性**——三区遍历错误 **0**；归档区仅名之遍历错误 **0**。②**模式与命名是否结构性互斥**——**不互斥**：实体名含「全量补实验执行计划」，探针可正面命中，三区与归档区皆 0 ⇒ 阴性**有效**。③**时点新鲜**——本棒实测窗口；且其**落位字面今日可查**（规格包在盘且逐字可引）。

**三径荐案**：甲＝**PI 取回**（**唯一有实证路径者**——其落位字面 `shared/…` 相对**远端仓根** `zeroandcat/Deposon`，取件之径归 PI；⛔ 0 联网·未测）；乙＝**辨明替代**——其 v1.1 姊妹件《全量补实验执行计划 v1.1》（`c43494ddd528`·21,411 B）之登记载「在仓外冻结区」，然本棒归档区**仅名**扫描**0 命中**（「全量补实验」「执行计划」「计划」皆 0）⇒ **该面亦不可核**，⛔ 0 以 v1.1 充 v1；丙＝**挂账**（36 条之原始条目文本不可核——`_ge03_ge04_claim_proposal_2026_10_22.md` §3 同判，本棒复核同值）。**本棒荐：甲优先・丙兜底；乙已实测不可行。**

**引者件与行（列全）**：

- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:267
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:274
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:293
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:341
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:493
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:578
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:599
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:601
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:603
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:606
- `results/.tmp/_s14_session_scan_out_2026_10_21.md`:607
- `results/_cleanup_noise_register_2026_10_21.md`:210
- `results/_ge03_ge04_claim_proposal_2026_10_22.md`:135
- `results/_ge03_ge04_definition_deliberation_2026_10_21.md`:105
- `results/_ge03_ge04_definition_deliberation_2026_10_21.md`:157
- `results/_ge03_ge04_definition_deliberation_2026_10_21.md`:276
- `results/_ge03_ge04_definition_deliberation_2026_10_21.md`:330
- `results/_ghost_reference_register_2026_10_21.md`:31
- `results/_r5_spec_pack_retrieved_2026_10_13/鲍勃_minimax实验委托规格包_2026_10_12.md`:5
- `results/_stage1_prereq_wave1_evidence_2026_10_20.md`:238
- `results/_stage1_prereq_wave1_evidence_2026_10_20.md`:307
- `results/_stage1_prereq_wave1_evidence_2026_10_20.md`:368
- `results/_stage1_prereq_wave1_evidence_2026_10_20.md`:371
- `results/_v172_adoption_effect_2026_10_20.md`:245
- `results/_v172_adoption_effect_2026_10_20.md`:457

## §4 真幽灵（1350 件）——逐条登记

> 表列：指纹｜所指名（自引用语境抽）｜被引次数｜所载 bytes｜引者件与行（首引件:行 ＋ 件数）｜**拟定处置**。
> **处置为拟案，非裁断**（⛔ 0 代裁）。处置口径：**①补正**＝补登现行真实指纹（低引次、实体现可指）；**②改指**＝改指至在盘之近字节同名件（须先辨明同一性）；**③删引**＝引文无实体可指，⛔ 0 代删，仅登记俟 PI 令；**④登记挂账・候 PI 取回**＝高引次或落位在远端面，取件之径归 PI。

| 指纹 | 所指名 | 引次 | bytes | 引者件与行 | 拟定处置 |
|---|---|---|---|---|---|
| `739a7daf533b` | rescript_2026_09_27.md | 512 | 3456 | `_batch3_execution_receipt_kimi_2026_10_18.md`:390（＋1 件） | ④登记挂账·候 PI 取回 |
| `7a097d7802d1` | _material_expansion_drift_authorized_registe | 266 | 45590 | `_pi_card_answers_register_2026_10_16_v19.md`:37（＋64 件） | ④登记挂账·候 PI 取回 |
| `66f900b7598b` | _d1_ruling_and_s3_transition_2026_10_01.md | 252 | 28352 | `_pi_card_answers_register_2026_10_18_v100.md`:59（＋38 件） | ②改指（候选：_d1_ruling_and_s3_transition_2026_10_01.md·近字节 28370） |
| `275e480ba4d9` | _t5_anchor_drift_authorized_register_2026_10 | 189 | 11553 | `_pi_card_answers_register_2026_10_14_v2.md`:21（＋52 件） | ②改指（候选：_t5_anchor_drift_authorized_register_2026_10_15.md·近字节 11553） |
| `7bfae6498eee` | _s3_th_v21_reconciliation_verdict_2026_10_01 | 124 | 51061 | `_collision_514_coverage_recheck_2026_10_18.md`:123（＋15 件） | ②改指（候选：_s3_th_v21_reconciliation_verdict_2026_10_01.md·近字节 51073） |
| `355a32f7f860` | _s3_missing_field_backfill_rule_effective_20 | 118 | 52466 | `_pi_card_answers_register_2026_10_21_v213.md`:23（＋22 件） | ②改指（候选：_s3_missing_field_backfill_rule_effective_2026_10_01.md·近字节 52469） |
| `4228142806c5` | 待裁项团队决议 | 95 | 22733 | `_pi_card_answers_register_2026_10_21_v198.md`:23（＋33 件） | ④登记挂账·候 PI 取回 |
| `658db4ffff47` | _glm_delivery_pack_verification_2026_10_14.m | 93 | 2391775 | `_batch6_deliberation_judgment_2026_10_13.md`:52（＋24 件） | ④登记挂账·候 PI 取回 |
| `b3ea36a24dcf` | _s3_kv3s_3_verdict_2026_10_01.md | 82 | 35022 | `_s14_session_scan_out_2026_10_21.md`:254（＋15 件） | ②改指（候选：_s3_kv3s_3_verdict_2026_10_01.md·近字节 35037） |
| `27cb200220e0` | _harness_mask_correct_value_validation_2026_ | 72 | 45548 | `_pi_card_answers_register_2026_10_17_v89.md`:56（＋11 件） | ④登记挂账·候 PI 取回 |
| `2e77a13e51f1` | _s3_missing_field_backfill_rule_draft_2026_1 | 66 | 35824 | `_pi_card_answers_register_2026_10_21_v213.md`:23（＋13 件） | ②改指（候选：_s3_missing_field_backfill_rule_draft_2026_10_01.md·近字节 35827） |
| `c6f90d7d3eb6` | _d1_backfill_intake_verdict_2026_10_01.md | 57 | 42106 | `_domain_backfill_hold235_adjudication_2026_10_18.md`:248（＋11 件） | ②改指（候选：results___d1_backfill_intake_verdict_2026_10_01.md·近字节 42115） |
| `cf207df06762` | _t1_substrate_gap_precondition_2026_10_01.md | 55 | 22196 | `_achievements_inventory_full_2026_10_09.md`:879（＋6 件） | ②改指（候选：_t1_substrate_gap_precondition_2026_10_01.md·近字节 22196） |
| `94c50da0bdd0` | _kd_mda8_first_reading_verdict_2026_10_20.md | 48 | 49991 | `_pi_card_answers_register_2026_10_20_v152.md`:24（＋9 件） | ④登记挂账·候 PI 取回 |
| `bf467289589b` | _v5_item35_prereg_v2_2026_09_28.md | 48 | 31682 | `_h5_session_census_2026_10_19_part1.md`:1666（＋8 件） | ④登记挂账·候 PI 取回 |
| `4ce661acc81f` | _s3_d1_rulings_supplement_register_2026_10_0 | 45 | 28762 | `_achievements_inventory_full_2026_10_09.md`:2306（＋11 件） | ②改指（候选：_s3_d1_rulings_supplement_register_2026_10_01.md·近字节 28762） |
| `b081d19be1b4` | _kv3s_3_2_terminal_verdict_2026_10_01.md | 43 | 32296 | `_achievements_inventory_full_2026_10_09.md`:2108（＋15 件） | ②改指（候选：_kv3s_3_2_terminal_verdict_2026_10_01.md·近字节 32296） |
| `708dfac55be9` | _kd_writing_convention_guidance_2026_10_09.m | 42 | 20179 | `_achievements_inventory_full_2026_10_09.md`:774（＋10 件） | ②改指（候选：_kd_writing_convention_guidance_2026_10_09.md·近字节 20179） |
| `be996f2ec163` | _n7_mutual_exclusion_determination_2026_10_0 | 38 | 40166 | `_family_de_stale_refresh_matrix_2026_10_14.md`:151（＋7 件） | ②改指（候选：_n7_mutual_exclusion_determination_2026_10_01.md·近字节 40169） |
| `d0fcd15db0a2` | _root_session_history_memo_main_2026_10_14.m | 38 | 103221 | `_pi_card_answers_register_2026_10_17_v48.md`:14（＋7 件） | ④登记挂账·候 PI 取回 |
| `fddc14e6da27` | 爱丽丝_仓态进展与前置事实核查_2026_10_18.md | 35 | 15264 | `_pi_card_answers_register_2026_10_21_v214.md`:19（＋10 件） | ④登记挂账·候 PI 取回 |
| `6bfa7b210a80` | （49,991 B）之**盘上实体 ＝ 0 命中**｜📌 | 33 | 64345 | `_pi_card_answers_register_2026_10_20_v153.md`:25（＋9 件） | ④登记挂账·候 PI 取回 |
| `2833f89d623b` | _root_session_history_memo_2026_10_14.md | 32 | 66561 | `_pi_card_answers_register_2026_10_18_v99.md`:108（＋11 件） | ②改指（候选：results___root_session_history_memo_2026_10_14.md·近字节 66582） |
| `59fb90c22a7d` | _s3_missing_field_backfill_rule_effective_20 | 32 | 45366 | `_family_de_stale_refresh_matrix_2026_10_14.md`:220（＋4 件） | ④登记挂账·候 PI 取回 |
| `5d42e81289cc` | _limb_reading_verdict_kv3s33_2026_10_01.md | 30 | 56323 | `_s14_session_scan_out_2026_10_21.md`:572（＋9 件） | ②改指（候选：results___limb_reading_verdict_kv3s33_2026_10_01.md·近字节 56321） |
| `ffda214d1917` | _v5_trae_doubt6_verify_2026_09_28.md | 30 | 51778 | `_closeout_bucket_refresh_2026_10_09.md`:100（＋5 件） | ④登记挂账·候 PI 取回 |
| `56c52db3f22a` | _v5_theory_input_acquisition_request_2026_09 | 29 | 10212 | `_pi_card_answers_register_2026_10_17_v46.md`:73（＋12 件） | ②改指（候选：_v5_theory_input_acquisition_request_2026_09_29.md·近字节 10691） |
| `003cf7ee936d` | _t1_gate_closure_and_recompute_verdict_2026_ | 26 | 72951 | `_s14_session_scan_out_2026_10_21.md`:572（＋14 件） | ②改指（候选：PRE_SUB_0b5fb78727c2__t1_gate_closure_and_recompute_verdict_2026_10_01.md.md·近字节 72934） |
| `4fa15c554d93` | _glm_dualtrack_paper_reply_2026_10_18.md | 26 | 33403 | `_s14_session_scan_out_2026_10_21.md`:32（＋7 件） | ④登记挂账·候 PI 取回 |
| `ff88d430e330` | _root_session_history_memo_main_2026_10_14.m | 26 | 117326 | `_pi_card_answers_register_2026_10_17_v50.md`:15（＋5 件） | ④登记挂账·候 PI 取回 |
| `cf04fc2f39db` | 全量补实验执行计划 | 25 | 14904 | `_s14_session_scan_out_2026_10_21.md`:267（＋7 件） | ④登记挂账·候 PI 取回 |
| `689f587f219c` | _commission_glm_dualtrack_paper_addendum_202 | 24 | 35892 | `_cluster_j_glm_62_adjudication_2026_10_19.md`:174（＋7 件） | ④登记挂账·候 PI 取回 |
| `d378062d508a` | ·四要素与时点（ | 23 | 3098723 | `_pi_card_answers_register_2026_10_17_v57.md`:83（＋4 件） | ④登记挂账·候 PI 取回 |
| `ea2c4131e47c` | _voided_files_reference_update_2026_10_14.md | 23 | 16515 | `_batch_approval_merged_rollout_design_2026_10_14.md`:140（＋6 件） | ②改指（候选：_voided_files_reference_update_2026_10_14.md·近字节 16514） |
| `b36625682501` | _root_session_history_memo_main_2026_10_14.m | 21 | 120259 | `_pi_card_answers_register_2026_10_17_v54.md`:94（＋7 件） | ④登记挂账·候 PI 取回 |
| `517075064e45` | _fake_kd_p5_reversal_adjudication_2026_10_21 | 20 | 62558 | `_ghost_reference_register_2026_10_21.md`:116（＋1 件） | ②改指（候选：_fake_kd_p5_reversal_adjudication_2026_10_21.md·近字节 64697） |
| `2fbb82e6c7b4` | _root_session_history_memo_main_2026_10_14.m | 18 | 145838 | `_pi_card_answers_register_2026_10_18_v99.md`:108（＋9 件） | ④登记挂账·候 PI 取回 |
| `0487b78ad851` | _pi_card_answers_register_2026_10_17_v69.md | 17 | 48432 | `_pi_card_answers_register_2026_10_17_v69.md`:18（＋4 件） | ④登记挂账·候 PI 取回 |
| `b38ac3dfc867` | agent.md | 17 | 2763 | `_ghost_reference_register_2026_10_21.md`:79（＋2 件） | ④登记挂账·候 PI 取回 |
| `e269c707b0ca` | _root_session_history_memo_main_2026_10_14.m | 17 | 160603 | `_pi_card_answers_register_2026_10_18_v99.md`:108（＋7 件） | ②改指（候选：results___root_session_history_memo_main_2026_10_14.md·近字节 160625） |
| `cff94f9d940e` | _r3_r4_interpretation_case_2026_10_01.md | 16 | 64843 | `_family_de_stale_refresh_matrix_2026_10_14.md`:151（＋4 件） | ②改指（候选：_r3_r4_interpretation_case_2026_10_01.md·近字节 64849） |
| `63621dcf5326` | _kd_resolvability_and_optional_experiments_2 | 14 | 70353 | `_kd_h5_session_history_pilot_1of10_2026_10_20.md`:6346（＋1 件） | ②改指（候选：_kd_resolvability_and_optional_experiments_2026_10_09.md·近字节 70328） |
| `83fdfd910b91` | _pi_decision_backlog_consolidated_2026_10_21 | 14 | 73478 | `_s14_session_scan_out_2026_10_21.md`:1014（＋3 件） | ④登记挂账·候 PI 取回 |
| `8aba2837bc6a` | P_B_DISTORTION_BOUND_V0_SPEC.md | 14 | 11189 | `_batch9_deliberation_judgment_2026_10_14.md`:68（＋7 件） | ④登记挂账·候 PI 取回 |
| `b32ca40ec123` | _pi_card_answers_register_2026_10_18_v104.md | 14 | 15707 | `_pi_card_answers_register_2026_10_18_v104.md`:271（＋2 件） | ④登记挂账·候 PI 取回 |
| `087a18ec37d0` | _t1_gate_closure_and_recompute_verdict_2026_ | 13 | 72926 | `_pi_card_answers_register_2026_10_17_v46.md`:98（＋8 件） | ②改指（候选：results___t1_gate_closure_and_recompute_verdict_2026_10_01.md·近字节 72926） |
| `16ef897639c4` | 〔幽灵引用·未上传:_t1_gate_closure〕 | 13 | 72934 | `_pi_card_answers_register_2026_10_17_v46.md`:99（＋8 件） | ④登记挂账·候 PI 取回 |
| `4bdd82c796b8` | _t1_gate_closure_and_recompute_verdict_2026_ | 13 | 72934 | `_achievements_inventory_full_2026_10_09.md`:2389（＋6 件） | ②改指（候选：PRE_SUB_0b5fb78727c2__t1_gate_closure_and_recompute_verdict_2026_10_01.md.md·近字节 72934） |
| `60dbb71d1117` | _s3_kv3s_3_verdict_2026_10_01.md | 13 | 11449 | `_s14_session_scan_out_2026_10_21.md`:284（＋1 件） | ④登记挂账·候 PI 取回 |
| `c43494ddd528` | 全量补实验执行计划 v1.1 | 13 | 21411 | `_s14_session_scan_out_2026_10_21.md`:291（＋3 件） | ④登记挂账·候 PI 取回 |
| `3138ac9095b0` | _kd_resolvability_and_optional_experiments_2 | 12 | 70328 | `_achievements_inventory_full_2026_10_09.md`:2064（＋6 件） | ②改指（候选：_kd_resolvability_and_optional_experiments_2026_10_09.md·近字节 70328） |
| `570b7bd3e286` | GT_RECONSTRUCTION.md | 12 | 6695 | `_ge01_gt_kill_family_generation_design_2026_10_14.md`:91（＋4 件） | ④登记挂账·候 PI 取回 |
| `57f5a4c5d5cd` | — | 12 | 31227 | `_d9_h2_r1files_repair_register_2026_10_13.md`:110（＋5 件） | ④登记挂账·候 PI 取回 |
| `e0b891f01a6b` | _pi_card_answers_register_2026_10_16_v32.md | 12 | 25159 | `_pi_card_answers_register_2026_10_16_v32.md`:11（＋6 件） | ④登记挂账·候 PI 取回 |
| `119f98cd8d2d` | _verdict_pack_d_prep_2026_10_01.md | 11 | 49471 | `_achievements_inventory_full_2026_10_09.md`:2671（＋5 件） | ②改指（候选：_verdict_pack_d_prep_2026_10_01.md·近字节 49471） |
| `64a86ad94490` | ／9,385 为现行版**； | 11 | 16644 | `_bob_commission_acceptance_and_r4_waiver_register_2026_10_12.md`:9（＋3 件） | ④登记挂账·候 PI 取回 |
| `9708e7ef1f8c` | _v3_recheck_verdict_register_2026_09_27.md | 11 | 65913 | `_v3_recheck_05_rescript_2026_09_28.md`:5（＋4 件） | ④登记挂账·候 PI 取回 |
| `e12ff3b17bd7` | 件首表所载 | 11 | 39513 | `_pi_card_answers_register_2026_10_17_v74.md`:17（＋3 件） | ④登记挂账·候 PI 取回 |
| `e9aa6e5180ca` | _v5_loadcorpus_switch_2026_09_29.md | 11 | 34547 | `_v3_recheck_verdict_register_2026_09_27.md`:54（＋4 件） | ④登记挂账·候 PI 取回 |
| `00e1978c6c53` | — | 10 | 6680 | `_c7_remote_timeline_correction_register_2026_10_14.md`:84（＋3 件） | ④登记挂账·候 PI 取回 |
| `1195c612de2a` | _pi_card_answers_register_2026_10_18_v97.md | 10 | 40106 | `_pi_card_answers_register_2026_10_18_v98.md`:5（＋3 件） | ④登记挂账·候 PI 取回 |
| `55844e39f00e` | — | 10 | 6416 | `_pi_card_answers_register_2026_10_20_supplement_4cards.md`:159（＋3 件） | ④登记挂账·候 PI 取回 |
| `1781ea2f742d` | (15,389 B) = **漂移版**（锚版 | 9 | 14224 | `_kd_h2_anchor_chain_erratum_2026_10_20.md`:138（＋5 件） | ④登记挂账·候 PI 取回 |
| `19325960b8be` | (15,389 B) = **漂移版**（锚版 | 9 | 14956 | `_kd_h2_anchor_chain_erratum_2026_10_20.md`:137（＋5 件） | ④登记挂账·候 PI 取回 |
| `216f736d624e` | *件止。 | 9 | 90822 | `_ghost_reference_register_2026_10_21.md`:95（＋2 件） | ④登记挂账·候 PI 取回 |
| `2cd7250c3721` | _s4_kv3s_4_123_judgment_prereg_2026_10_12.md | 9 | 5637 | `_s14_session_scan_out_2026_10_21.md`:291（＋2 件） | ④登记挂账·候 PI 取回 |
| `ab1e6fc3d883` | _kimi_receipt_authority_rulings_effect_2026_ | 9 | 59446 | `_kimi_receipt_authority_rulings_effect_2026_10_18.md`:220（＋3 件） | ④登记挂账·候 PI 取回 |
| `c0b55e0385a4` | (15,389 B) = **漂移版**（锚版 | 9 | 13966 | `_kd_h2_anchor_chain_erratum_2026_10_20.md`:139（＋5 件） | ④登记挂账·候 PI 取回 |
| `deec8c91a75b` | _d8_collection_ledger_2026_09_30.md | 9 | 1957 | `_d8_boundary_revision_register_2026_09_30.md`:30（＋2 件） | ④登记挂账·候 PI 取回 |
| `e97c87f8d4b2` | _kd_legacy_rewrite_register_2026_10_10.md | 9 | 28349 | `_domain_backfill_execution_register_2026_10_18.md`:151（＋5 件） | ④登记挂账·候 PI 取回 |
| `0ccd739d026e` | — | 8 | 18988 | `_d9_independent_review_2026_10_12.md`:51（＋4 件） | ④登记挂账·候 PI 取回 |
| `169bbdb28759` | _fake_kd_p4_reversal_adjudication_2026_10_21 | 8 | 2895 | `_fake_kd_p4_reversal_adjudication_2026_10_21.md`:15（＋2 件） | ④登记挂账·候 PI 取回 |
| `338f30ad7460` | _s3_kv3s_3_4_judgment_prereg_2026_10_12.md | 8 | 6156 | `_s14_session_scan_out_2026_10_21.md`:291（＋1 件） | ④登记挂账·候 PI 取回 |
| `3e932a5409b5` | — | 8 | 22133 | `_cpath_e3_sign_normalization_2026_10_01.md`:18（＋0 件） | ④登记挂账·候 PI 取回 |
| `3f7f3b76ee19` | _root_session_history_memo_main_2026_10_14.m | 8 | 114115 | `_pi_card_answers_register_2026_10_17_v51.md`:80（＋1 件） | ④登记挂账·候 PI 取回 |
| `638150884d18` | P_B_DISTORTION_BOUND_V0_SPEC.md | 8 | 11246 | `_g1_archive_zone_search_register_2026_10_12.md`:51（＋3 件） | ④登记挂账·候 PI 取回 |
| `648bd68a2dbc` | _root_session_history_memo_2026_10_14.md | 8 | 187404 | `_deposon_full_history_sub_2026_10_19.md`:139（＋4 件） | ④登记挂账·候 PI 取回 |
| `90b5bb66dadb` | — | 8 | 52745 | `_d9_independent_review_2026_10_12.md`:52（＋4 件） | ④登记挂账·候 PI 取回 |
| `a7267d1cad80` | — | 8 | 38709 | `_d9_independent_review_2026_10_12.md`:50（＋4 件） | ④登记挂账·候 PI 取回 |
| `a7c03b4a4006` | _pi_card_answers_register_2026_10_16_v41.md | 8 | 38393 | `_pi_card_answers_register_2026_10_16_v41.md`:11（＋3 件） | ④登记挂账·候 PI 取回 |
| `a80d9ae8008b` | _s3_kv3s_3_4_judgment_prereg_2026_10_12.md | 8 | 5678 | `_s14_session_scan_out_2026_10_21.md`:291（＋1 件） | ④登记挂账·候 PI 取回 |
| `bd33065703be` | _v150_adoption_effect_2026_10_20.md | 8 | 124295 | `_ghost_reference_register_2026_10_21.md`:151（＋3 件） | ④登记挂账·候 PI 取回 |
| `cb0195c06647` | _t1_7_2_correction_2026_10_08.md | 8 | 16476 | `_family_de_stale_refresh_matrix_2026_10_14.md`:187（＋3 件） | ②改指（候选：_t1_7_2_correction_2026_10_08.md·近字节 16469） |
| `de142d168ab9` | _root_session_history_memo_main_2026_10_14.m | 8 | 69072 | `_u_axis_equation_direction_deliberation_2026_10_16.md`:42（＋1 件） | ④登记挂账·候 PI 取回 |
| `1268868a6b0e` | _s3_d1_rulings_supplement_register_2026_10_0 | 7 | 28762 | `_family_de_stale_refresh_repo_exec_2026_10_14.md`:96（＋1 件） | ②改指（候选：_s3_d1_rulings_supplement_register_2026_10_01.md·近字节 28762） |
| `129223e7c433` | _pi_card_answers_register_2026_10_16_v40.md | 7 | 26292 | `_pi_card_answers_register_2026_10_16_v41.md`:15（＋2 件） | ②改指（候选：_pi_card_answers_register_2026_10_16_v40.md·近字节 26768） |
| `2fb718ddea27` | _kv3s_3_2_terminal_verdict_2026_10_01.md | 7 | 32296 | `_family_de_stale_refresh_repo_exec_2026_10_14.md`:86（＋1 件） | ②改指（候选：_kv3s_3_2_terminal_verdict_2026_10_01.md·近字节 32296） |
| `3deb8194a671` | agent.md | 7 | 2737 | `_ghost_reference_register_2026_10_21.md`:91（＋2 件） | ④登记挂账·候 PI 取回 |
| `4531d6eca058` | _t1_gate_closure_and_recompute_verdict_2026_ | 7 | 72934 | `_family_de_stale_refresh_repo_exec_2026_10_14.md`:127（＋1 件） | ②改指（候选：PRE_SUB_0b5fb78727c2__t1_gate_closure_and_recompute_verdict_2026_10_01.md.md·近字节 72934） |
| `62eed1f4dfa0` | — | 7 | 327975 | `_trae_errata_sha_drift_attribution_2026_10_01.md`:82（＋0 件） | ④登记挂账·候 PI 取回 |
| `a87d1121b4ac` | _mini_round_6_7_settlement_register_2026_10_ | 7 | 68053 | `_achievements_inventory_full_2026_10_09.md`:2129（＋4 件） | ②改指（候选：_mini_round_6_7_settlement_register_2026_10_01.md·近字节 68053） |
| `ab07a9146519` | — | 7 | 21477 | `_o1_498_lock_scope_deliberation_2026_10_16.md`:33（＋1 件） | ④登记挂账·候 PI 取回 |
| `b440f527eb54` | （blob id）／45,590／803 ／ 2026-10-18 13:38:25 ／ | 7 | 10090 | `_ghost_reference_register_2026_10_21.md`:191（＋2 件） | ④登记挂账·候 PI 取回 |
| `b913b9910f29` | — | 7 | 4205 | `_esc3_esc6_resolution_2026_10_17.md`:44（＋4 件） | ④登记挂账·候 PI 取回 |
| `bbc6b3e20b92` | — | 7 | 11369 | `_achievements_inventory_full_2026_10_09.md`:3108（＋4 件） | ④登记挂账·候 PI 取回 |
| `f44996fbfd9f` | 〔本地路径已脱敏〕 | 7 | 3063 | `_pre_execution_report_kimi_2026_10_18.md`:14（＋4 件） | ④登记挂账·候 PI 取回 |
| `1307a6c44fbe` | _fake_kd_p4_reversal_errata_2026_10_21.md | 6 | 518 | `_fake_kd_p4_reversal_adjudication_2026_10_21.md`:62（＋2 件） | ④登记挂账·候 PI 取回 |
| `169d160ba600` | — | 6 | 4630 | `_repo_post_cleanup_snapshot_2026_10_12.md`:291（＋1 件） | ④登记挂账·候 PI 取回 |
| `18ee5064d9f2` | _pi_card_answers_register_2026_10_16_v41.md | 6 | 37888 | `_pi_card_answers_register_2026_10_16_v41.md`:11（＋3 件） | ④登记挂账·候 PI 取回 |
| `21f5284adcdc` | _root_session_history_memo_main_2026_10_14.m | 6 | 132833 | `_achievements_inventory_full_2026_10_18.md`:3979（＋4 件） | ④登记挂账·候 PI 取回 |
| `27e6c78a56ee` | agent.md | 6 | 4022 | `_ghost_reference_register_2026_10_21.md`:149（＋1 件） | ④登记挂账·候 PI 取回 |
| `2aa0fe91b2ec` | _t4_key_preexp_killline_prereg_2026_10_21.md | 6 | 98393 | `_c7_naming_deliberation_2026_10_21.md`:32（＋2 件） | ④登记挂账·候 PI 取回 |
| `2ded5cf0e863` | ；**不复制入仓**（如需留痕则新名落盘 + 双记 SHA/字节 + 「漂移版 ≠ 锚版 | 6 | 15389 | `_kd_h2_anchor_chain_erratum_2026_10_20.md`:139（＋3 件） | ④登记挂账·候 PI 取回 |
| `3124456ce940` | _fake_kd_p4_reversal_errata_2026_10_21.md | 6 | 93555 | `_fake_kd_p4_reversal_errata_2026_10_21.md`:74（＋1 件） | ④登记挂账·候 PI 取回 |
| `52941f523383` | — | 6 | 1386 | `_batch3_execution_receipt_kimi_2026_10_18.md`:45（＋1 件） | ④登记挂账·候 PI 取回 |
| `5f6dc0b7baf3` | （509 反脱敏修复回退）。 _glm_dualtrack_paper_reply_20 | 6 | 3462 | `_s14_session_scan_out_2026_10_21.md`:460（＋3 件） | ④登记挂账·候 PI 取回 |
| `7762f9f8fea8` | — | 6 | 16515 | `_kd_h5_h6_recheck_2026_10_14.md`:104（＋1 件） | ④登记挂账·候 PI 取回 |
| `77b49c0f8b54` | KT_C1_SPEC_V0.md | 6 | 17940 | `_ge01_gt_kill_family_byte_stream_effect_register_2026_10_14.md`:67（＋3 件） | ④登记挂账·候 PI 取回 |
| `7c2b41c008a5` | — | 6 | 16404 | `_kd_h2_anchor_chain_erratum_2026_10_20.md`:137（＋3 件） | ④登记挂账·候 PI 取回 |
| `7e1e2209a013` | agent.md | 6 | 3971 | `_ghost_reference_register_2026_10_21.md`:212（＋1 件） | ④登记挂账·候 PI 取回 |
| `8355724a26e3` | _v4_supp_t15r2_verdict.md | 6 | 41246 | `_skill_reference_update_and_user_surface_survey_2026_09_30.md`:95（＋2 件） | ④登记挂账·候 PI 取回 |
| `8afc120c47f0` | — | 6 | 174424 | `_archive_area_readonly_verification_2026_10_18.md`:221（＋3 件） | ④登记挂账·候 PI 取回 |
| `8c6e98034005` | ；**不复制入仓**（如需留痕则新名落盘 + 双记 SHA/字节 + 「漂移版 ≠ 锚版 | 6 | 15677 | `_kd_h2_anchor_chain_erratum_2026_10_20.md`:138（＋3 件） | ④登记挂账·候 PI 取回 |
| `9935be2c6552` | ）｜⚠ **v67 之 §5 自核节自报 | 6 | 46884 | `_pi_card_answers_register_2026_10_17_v67.md`:272（＋2 件） | ④登记挂账·候 PI 取回 |
| `fe5fe2b8b2d0` | — | 6 | 1386 | `_batch3_execution_receipt_kimi_2026_10_18.md`:43（＋1 件） | ④登记挂账·候 PI 取回 |
| `040f6bc886a4` | _pi_card_answers_register_2026_10_17_v70.md | 5 | 30290 | `_pi_card_answers_register_2026_10_17_v69.md`:19（＋2 件） | ④登记挂账·候 PI 取回 |
| `0c9e73ba0a54` | _t1_gate_closure_and_recompute_verdict_2026_ | 5 | 72926 | `_family_de_stale_refresh_repo_exec_2026_10_14.md`:104（＋0 件） | ②改指（候选：results___t1_gate_closure_and_recompute_verdict_2026_10_01.md·近字节 72926） |
| `113cbe555643` | _v4_seeds_prereg_supplement_2026_09_23.md | 5 | 53633 | `_ge01_ecr_anchor_sourcing_design_2026_10_14.md`:47（＋0 件） | ④登记挂账·候 PI 取回 |
| `16e808e7f166` | 之 **rowid 126982**（role | 5 | 3633 | `_fake_kd_p4_reversal_adjudication_2026_10_21.md`:62（＋1 件） | ④登记挂账·候 PI 取回 |
| `1c6f9de452fd` | _v174_adoption_effect_2026_10_21.md | 5 | 117027 | `_ghost_reference_register_2026_10_21.md`:73（＋2 件） | ④登记挂账·候 PI 取回 |
| `266fceadec42` | _stage1_gap_exhaustive_audit_2026_10_20.md | 5 | 72704 | `_ghost_reference_register_2026_10_21.md`:132（＋1 件） | ④登记挂账·候 PI 取回 |
| `398e51a233ef` | _s2_confirmation_parenthesis_correction_note | 5 | 89304 | `_ghost_reference_register_2026_10_21.md`:94（＋2 件） | ④登记挂账·候 PI 取回 |
| `688ac0e0aa56` | _kd_family_census_2026_10_20.md | 5 | 2751 | `_s14_body_2026_10_21.md`:186（＋2 件） | ④登记挂账·候 PI 取回 |
| `6b1d6710b3e8` | _root_session_history_memo_main_2026_10_14.m | 5 | 88107 | `_pi_card_answers_register_2026_10_17_v45.md`:94（＋0 件） | ④登记挂账·候 PI 取回 |
| `6d976fe9bba0` | _fake_kd_p4_reversal_adjudication_2026_10_21 | 5 | 454 | `_fake_kd_p4_reversal_adjudication_2026_10_21.md`:62（＋2 件） | ④登记挂账·候 PI 取回 |
| `75a36f81fb2e` | _preexp_mda8a24_c1_reading_2026_10_20.md | 5 | 93346 | `_s14_main_events2_2026_10_21.md`:120（＋1 件） | ④登记挂账·候 PI 取回 |
| `75c32e507f95` | — | 5 | 1925 | `_fake_kd_p4_reversal_adjudication_2026_10_21.md`:62（＋1 件） | ④登记挂账·候 PI 取回 |
| `7cbb417ab979` | — | 5 | 1741895 | `_batch10_deliberation_judgment_2026_10_14.md`:63（＋1 件） | ④登记挂账·候 PI 取回 |
| `7d1482b239c7` | _root_session_history_memo_main_2026_10_14.m | 5 | 50344 | `_pi_card_answers_register_2026_10_16_v31.md`:166（＋2 件） | ④登记挂账·候 PI 取回 |
| `7df20f7b3084` | — | 5 | 3837 | `_h5_session_census_2026_10_19_part2.md`:3771（＋2 件） | ④登记挂账·候 PI 取回 |
| `8406cb842cac` | （原件）｜ | 5 | 95135 | `_fake_verdict_reverify_sixitem_ledger_2026_09_30.md`:320（＋1 件） | ④登记挂账·候 PI 取回 |
| `99faefb82bf8` | _v3_recheck_verdict_register_2026_09_27.md | 5 | 87138 | `_v3_recheck_verdict_register_2026_09_27.md`:432（＋2 件） | ④登记挂账·候 PI 取回 |
| `b717994dfda6` | ·载荷 5 件·包指纹 | 5 | 37622 | `_glm_reply_pack_intake_verification_2026_10_19.md`:112（＋2 件） | ④登记挂账·候 PI 取回 |
| `b7e3c3717d11` | 之层级）。**反证之锚**： | 5 | 1910 | `_h5_session_census_2026_10_19_part2.md`:3772（＋2 件） | ④登记挂账·候 PI 取回 |
| `cb5df7a51ad4` | _root_session_history_memo_main_2026_10_14.m | 5 | 81941 | `_ge01_launch_gate_recheck_2026_10_17.md`:97（＋1 件） | ④登记挂账·候 PI 取回 |
| `cf22f72eaebb` | — | 5 | 546 | `_esc3_esc6_resolution_2026_10_17.md`:44（＋3 件） | ④登记挂账·候 PI 取回 |
| `d1d86cb6a33e` | ·77,119 B·407 行·mtime **2026-10-20 11:09:45. | 5 | 74935 | `_ghost_reference_register_2026_10_21.md`:179（＋2 件） | ④登记挂账·候 PI 取回 |
| `da09c2142eca` | 爱丽丝_仓态进展与前置事实核查_2026_10_18.md | 5 | 184418 | `_s14_session_scan_out_2026_10_21.md`:284（＋3 件） | ④登记挂账·候 PI 取回 |
| `e004327ffb74` | 仓 | 5 | 4172 | `_deposon_full_history_sub_2026_10_19.md`:321（＋3 件） | ④登记挂账·候 PI 取回 |
| `e1073738b40d` | C-3 之脚本清理面**，本件**0 代裁** ⇒ **须 PI 另给一字面**。⚠ 另 | 5 | 8643 | `_achievements_inventory_full_2026_10_09.md`:2913（＋3 件） | ④登记挂账·候 PI 取回 |
| `01883f894f49` | _cluster_k_eta_blockers_adjudication_2026_10 | 4 | 38110 | `_cluster_k_eta_blockers_adjudication_2026_10_19.md`:32（＋3 件） | ④登记挂账·候 PI 取回 |
| `0a53046bc52d` | _harness_42b_drift_semantics_2026_10_19.md | 4 | 44064 | `_achievements_inventory_full_2026_10_18.md`:4719（＋2 件） | ④登记挂账·候 PI 取回 |
| `0ee3ffd7e17e` | （同 | 4 | 8346 | `_trae_sixitem_disposal_and_collision_register_2026_10_01.md`:90（＋0 件） | ④登记挂账·候 PI 取回 |
| `0f1bf6024884` | — | 4 | 401 | `_repo_post_cleanup_snapshot_2026_10_12.md`:316（＋2 件） | ④登记挂账·候 PI 取回 |
| `1336484486fa` | （B3 root，spec L265 字面）｜ | 4 | 1812 | `_v5_confirm_b5_decisions_register_2026_09_29.md`:237（＋0 件） | ④登记挂账·候 PI 取回 |
| `188ac065671b` | _u01_u15_recheck_after_rulings_2026_10_17.md | 4 | 87647 | `_u01_u15_recheck_after_rulings_2026_10_17.md`:28（＋1 件） | ④登记挂账·候 PI 取回 |
| `23ee92345bf1` | — | 4 | 3008 | `_achievements_inventory_full_2026_10_09.md`:3001（＋2 件） | ④登记挂账·候 PI 取回 |
| `2a50c9e0e3e5` | _root_session_history_memo_main_2026_10_14.m | 4 | 184364 | `_deposon_full_history_sub_2026_10_19.md`:138（＋3 件） | ④登记挂账·候 PI 取回 |
| `2fe506ab8a68` | — | 4 | 708 | `_repo_post_cleanup_snapshot_2026_10_12.md`:317（＋2 件） | ④登记挂账·候 PI 取回 |
| `315e1fc71b5e` | ）与 | 4 | 10251 | `_ge01_c3_gaps_disposition_2026_10_14.md`:60（＋1 件） | ④登记挂账·候 PI 取回 |
| `3433dbef75ce` | — | 4 | 38201 | `_s14_session_scan_out_2026_10_21.md`:312（＋1 件） | ④登记挂账·候 PI 取回 |
| `3509e3f21790` | — | 4 | 1612 | `_achievements_inventory_full_2026_10_09.md`:3003（＋2 件） | ④登记挂账·候 PI 取回 |
| `36268089944e` | _mini_round_5_decisions_register_2026_10_01. | 4 | 53125 | `_family_de_stale_refresh_repo_exec_2026_10_14.md`:201（＋1 件） | ②改指（候选：results___mini_round_5_decisions_register_2026_10_01.md·近字节 53125） |
| `3d988cb71ee4` | _pi_card_answers_register_2026_10_17_v75.md | 4 | 44442 | `_pi_card_answers_register_2026_10_17_v75.md`:240（＋2 件） | ②改指（候选：_pi_card_answers_register_2026_10_17_v75.md·近字节 45643） |
| `4435748f010d` | — | 4 | 4770 | `_achievements_inventory_full_2026_10_09.md`:3017（＋2 件） | ④登记挂账·候 PI 取回 |
| `4866ba720010` | — | 4 | 4079 | `_achievements_inventory_full_2026_10_09.md`:3011（＋2 件） | ④登记挂账·候 PI 取回 |
| `4b9d3a356bc7` | 〔幽灵引用·未上传:write_t3trap.py〕 | 4 | 30408 | `_cleanup_r2_repo_sub_exec_register_2026_10_17.md`:49（＋0 件） | ④登记挂账·候 PI 取回 |
| `4bc4f8c89e44` | — | 4 | 1967 | `_achievements_inventory_full_2026_10_09.md`:3000（＋2 件） | ④登记挂账·候 PI 取回 |
| `52fc1eadfb4b` | — | 4 | 70508 | `_u_axis_equation_direction_deliberation_2026_10_16.md`:51（＋1 件） | ④登记挂账·候 PI 取回 |
| `53784ec36e27` | — | 4 | 3816 | `_achievements_inventory_full_2026_10_09.md`:3007（＋2 件） | ④登记挂账·候 PI 取回 |
| `55838224f312` | 脚本已改显式失效**（ | 4 | 9503 | `_v5_confirm_b5_decisions_register_2026_09_29.md`:236（＋0 件） | ④登记挂账·候 PI 取回 |
| `59d9f421f5a6` | _root_session_history_memo_main_2026_10_14.m | 4 | 67074 | `_pi_card_answers_register_2026_10_16_v36.md`:24（＋2 件） | ④登记挂账·候 PI 取回 |
| `61c287c9b2b7` | ，0 写 | 4 | 796 | `_repo_post_cleanup_snapshot_2026_10_12.md`:319（＋2 件） | ④登记挂账·候 PI 取回 |
| `62f0a9df8e44` | _v146_adoption_effect_2026_10_20.md | 4 | 31324 | `_ghost_reference_register_2026_10_21.md`:144（＋2 件） | ④登记挂账·候 PI 取回 |
| `66a9b8b3dabf` | 〔幽灵引用·未上传:_l14v3_aggregated_〕 | 4 | 2233138 | `_v4_closeout_bulk_reorganize_register_2026_10_12.md`:103（＋2 件） | ④登记挂账·候 PI 取回 |
| `6d4cc73e617f` | hashlib.sha256(磁盘全文字节).hexdigest()[:12] | 4 | 39177 | `_pi_card_answers_register_2026_10_16_v42.md`:12（＋2 件） | ④登记挂账·候 PI 取回 |
| `6d710fb5679d` | _root_session_history_memo_main_2026_10_14.m | 4 | 182719 | `_ghost_reference_register_2026_10_21.md`:111（＋1 件） | ④登记挂账·候 PI 取回 |
| `7476489839da` | — | 4 | 45951 | `_batch3_execution_receipt_kimi_2026_10_18.md`:44（＋1 件） | ④登记挂账·候 PI 取回 |
| `767d26050580` | — | 4 | 74481 | `_batch3_execution_receipt_kimi_2026_10_18.md`:42（＋1 件） | ④登记挂账·候 PI 取回 |
| `778636a0cfae` | — | 4 | 187 | `_batch10_deliberation_judgment_2026_10_14.md`:80（＋1 件） | ④登记挂账·候 PI 取回 |
| `788fdf5f3142` | — | 4 | 4981 | `_achievements_inventory_full_2026_10_09.md`:3014（＋2 件） | ④登记挂账·候 PI 取回 |
| `78c079bef471` | — | 4 | 1429 | `_achievements_inventory_full_2026_10_09.md`:3004（＋2 件） | ④登记挂账·候 PI 取回 |
| `7b8207d9bbba` | — | 4 | 4587 | `_achievements_inventory_full_2026_10_09.md`:3018（＋2 件） | ④登记挂账·候 PI 取回 |
| `7b8fc7e9ed7f` | — | 4 | 7297 | `_v5_confirm_b5_decisions_register_2026_09_29.md`:235（＋0 件） | ④登记挂账·候 PI 取回 |
| `82c90a7c4d69` | _fake_kd_p4_reversal_errata_2026_10_21.md | 4 | 6646 | `_fake_kd_p4_reversal_adjudication_2026_10_21.md`:66（＋2 件） | ④登记挂账·候 PI 取回 |
| `8329b3829eaa` | _proxy_signoff_execution_register_2026_10_01 | 4 | 41856 | `_criterion_application_scope_prereg_2026_10_01.md`:424（＋3 件） | ④登记挂账·候 PI 取回 |
| `8488425898fb` | — | 4 | 2061 | `_h5_session_census_2026_10_19_part2.md`:3773（＋1 件） | ④登记挂账·候 PI 取回 |
| `849d76be3a06` | ；在册者 ＝ | 4 | 239387 | `_deposon_full_history_sub_2026_10_19.md`:272（＋1 件） | ④登记挂账·候 PI 取回 |
| `88c3533d7fcb` | — | 4 | 4925 | `_achievements_inventory_full_2026_10_09.md`:3010（＋2 件） | ④登记挂账·候 PI 取回 |
| `93d7fa7b875b` | — | 4 | 39725 | `_s14_main_session_slice_2026_10_21.md`:67（＋1 件） | ④登记挂账·候 PI 取回 |
| `9a0d8b5ec2a0` | _root_session_history_memo_main_2026_10_14.m | 4 | 91102 | `_pi_card_answers_register_2026_10_17_v46.md`:91（＋1 件） | ④登记挂账·候 PI 取回 |
| `9cf2f62c293d` | _kd_h5_background_tasks_full_scan_2026_10_20 | 4 | 68234 | `_s14_main_events2_2026_10_21.md`:87（＋2 件） | ②改指（候选：_kd_h5_background_tasks_full_scan_2026_10_20.md·近字节 70187） |
| `a1a4f4e1e64e` | _v150_adoption_effect_2026_10_20.md | 4 | 119961 | `_ghost_reference_register_2026_10_21.md`:221（＋1 件） | ④登记挂账·候 PI 取回 |
| `a8c0349f4e42` | _fake_kd_p3_readjudication_2026_10_21.md | 4 | 277 | `_fake_kd_p3_readjudication_2026_10_21.md`:13（＋1 件） | ④登记挂账·候 PI 取回 |
| `a91f28bfd48b` | — | 4 | 4565 | `_achievements_inventory_full_2026_10_09.md`:3016（＋2 件） | ④登记挂账·候 PI 取回 |
| `afb98c2bbc5b` | _kd_heteronym_classification_disposition_202 | 4 | 29761 | `_family_de_stale_refresh_repo_exec_2026_10_14.md`:198（＋1 件） | ②改指（候选：results___kd_heteronym_classification_disposition_2026_10_09.md·近字节 29761） |
| `b292c8b9152e` | — | 4 | 1636 | `_repo_post_cleanup_snapshot_2026_10_12.md`:199（＋2 件） | ④登记挂账·候 PI 取回 |
| `b3fba6ae6152` | — | 4 | 4651 | `_achievements_inventory_full_2026_10_09.md`:3020（＋2 件） | ④登记挂账·候 PI 取回 |
| `b7adb5afb0e9` | _pi_card_answers_register_2026_10_21_v197.md | 4 | 1424 | `_pi_card_answers_register_2026_10_21_v196.md`:38（＋3 件） | ④登记挂账·候 PI 取回 |
| `bd95582f6c79` | — | 4 | 59743 | `_runface_vs_shape_multidim_reading_2026_10_20.md`:11（＋1 件） | ④登记挂账·候 PI 取回 |
| `ccb6b4aef623` | — | 4 | 4983 | `_achievements_inventory_full_2026_10_09.md`:3013（＋2 件） | ④登记挂账·候 PI 取回 |
| `cd8441417cae` | _root_session_history_memo_main_2026_10_14.m | 4 | 62487 | `_pi_card_answers_register_2026_10_16_v35.md`:36（＋2 件） | ④登记挂账·候 PI 取回 |
| `d445274fcfa4` | — | 4 | 4616 | `_achievements_inventory_full_2026_10_09.md`:3005（＋2 件） | ④登记挂账·候 PI 取回 |
| `da7ea40657f7` | — | 4 | 4823 | `_repo_post_cleanup_snapshot_2026_10_12.md`:413（＋2 件） | ④登记挂账·候 PI 取回 |
| `dfb60c74fe3c` | — | 4 | 366 | `_repo_post_cleanup_snapshot_2026_10_12.md`:318（＋2 件） | ④登记挂账·候 PI 取回 |
| `e1e97f9c6964` | — | 4 | 58189 | `_runface_vs_shape_multidim_reading_2026_10_20.md`:11（＋1 件） | ④登记挂账·候 PI 取回 |
| `e519b5d5f51e` | — | 4 | 4844 | `_achievements_inventory_full_2026_10_09.md`:3012（＋2 件） | ④登记挂账·候 PI 取回 |
| `e54bc00e9787` | _v5_spec_prereq_reference_archive_2026_10_18 | 4 | 20423 | `_s14_session_scan_out_2026_10_21.md`:291（＋1 件） | ④登记挂账·候 PI 取回 |
| `edb264ccfc51` | — | 4 | 4105 | `_achievements_inventory_full_2026_10_09.md`:3019（＋2 件） | ④登记挂账·候 PI 取回 |
| `f55b9936088c` | — | 4 | 1333 | `_repo_post_cleanup_snapshot_2026_10_12.md`:320（＋2 件） | ④登记挂账·候 PI 取回 |
| `fffe7b000d00` | — | 4 | 92060 | `_m44_status_enum_backfill_design_2026_10_16.md`:72（＋0 件） | ④登记挂账·候 PI 取回 |
| `04a796b10c0a` | — | 3 | 13515 | `_achievements_inventory_full_2026_10_18.md`:595（＋1 件） | ④登记挂账·候 PI 取回 |
| `05e3d4c61f53` | — | 3 | 1765 | `_ge01_ecr_anchor_sourcing_design_2026_10_14.md`:46（＋0 件） | ④登记挂账·候 PI 取回 |
| `062b3916a395` | — | 3 | 4203 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:93（＋1 件） | ④登记挂账·候 PI 取回 |
| `0a711147ac83` | — | 3 | 9280 | `_repo_post_cleanup_snapshot_2026_10_12.md`:262（＋1 件） | ④登记挂账·候 PI 取回 |
| `0ade7a44d216` | — | 3 | 4463 | `_repo_post_cleanup_snapshot_2026_10_12.md`:193（＋1 件） | ④登记挂账·候 PI 取回 |
| `0c62f640ffcf` | — | 3 | 5195 | `_archive_area_readonly_verification_2026_10_18.md`:53（＋2 件） | ④登记挂账·候 PI 取回 |
| `0f1b308a495d` | — | 3 | 1362 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:101（＋1 件） | ④登记挂账·候 PI 取回 |
| `0f3f44968250` | — | 3 | 2165 | `_repo_post_cleanup_snapshot_2026_10_12.md`:288（＋1 件） | ④登记挂账·候 PI 取回 |
| `0f62453472b7` | 〔幽灵引用·未上传:_cpatomic_pycache_〕 | 3 | 10772 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:32（＋1 件） | ④登记挂账·候 PI 取回 |
| `100a25f7e818` | — | 3 | 11175 | `_repo_post_cleanup_snapshot_2026_10_12.md`:289（＋1 件） | ④登记挂账·候 PI 取回 |
| `10afd4410e25` | — | 3 | 7211 | `_repo_post_cleanup_snapshot_2026_10_12.md`:185（＋1 件） | ④登记挂账·候 PI 取回 |
| `10baaefe26fd` | _gap10_four_rulings_effect_2026_10_17.md | 3 | 34978 | `_pi_card_answers_register_2026_10_17_v68.md`:20（＋1 件） | ②改指（候选：_gap10_four_rulings_effect_2026_10_17.md·近字节 35339） |
| `10eaaeeb382d` | — | 3 | 2410 | `_repo_post_cleanup_snapshot_2026_10_12.md`:367（＋1 件） | ④登记挂账·候 PI 取回 |
| `129e35128198` | — | 3 | 4142 | `_repo_post_cleanup_snapshot_2026_10_12.md`:90（＋1 件） | ④登记挂账·候 PI 取回 |
| `13511b18379a` | — | 3 | 7662 | `_archive_area_readonly_verification_2026_10_18.md`:57（＋2 件） | ④登记挂账·候 PI 取回 |
| `1397dbcbeafe` | _g10_threshold_closed_domain_judgment_2026_1 | 3 | 55667 | `_archive_area_readonly_verification_2026_10_18.md`:62（＋2 件） | ②改指（候选：_g10_threshold_closed_domain_judgment_2026_10_11.md·近字节 55727） |
| `1730fe65e2ee` | — | 3 | 5022 | `_repo_post_cleanup_snapshot_2026_10_12.md`:244（＋1 件） | ④登记挂账·候 PI 取回 |
| `1748330999c7` | — | 3 | 7133 | `_g2_residual_cause_register_2026_10_12.md`:71（＋0 件） | ④登记挂账·候 PI 取回 |
| `18261cbde500` | — | 3 | 2453 | `_repo_post_cleanup_snapshot_2026_10_12.md`:431（＋1 件） | ④登记挂账·候 PI 取回 |
| `1842e1b1dd01` | _stage3_1_register_fingerprint_placeholder_e | 3 | 4475 | `_archive_area_readonly_verification_2026_10_18.md`:66（＋2 件） | ②改指（候选：_stage3_1_register_fingerprint_placeholder_erratum_2026_10_12.md·近字节 4495） |
| `185fd4c7aeee` | — | 3 | 2876 | `_repo_post_cleanup_snapshot_2026_10_12.md`:219（＋1 件） | ④登记挂账·候 PI 取回 |
| `1c0fbda3978e` | — | 3 | 1326 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:98（＋1 件） | ④登记挂账·候 PI 取回 |
| `1eb3c5c9c62d` | 〔幽灵引用·未上传:_cpatomic_pycache_〕 | 3 | 6476 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:33（＋1 件） | ④登记挂账·候 PI 取回 |
| `239cad89b5c5` | — | 3 | 2525 | `_archive_area_readonly_verification_2026_10_18.md`:55（＋2 件） | ④登记挂账·候 PI 取回 |
| `256711c88004` | — | 3 | 1701 | `_repo_post_cleanup_snapshot_2026_10_12.md`:287（＋1 件） | ④登记挂账·候 PI 取回 |
| `25b01b5a6081` | _kd_h5_session_history_domain_caliber_2026_1 | 3 | 54064 | `_ghost_reference_register_2026_10_21.md`:143（＋1 件） | ②改指（候选：_kd_h5_session_history_domain_caliber_2026_10_20.md·近字节 55674） |
| `27b60f271b37` | — | 3 | 40144 | `_achievements_inventory_full_2026_10_18.md`:591（＋1 件） | ④登记挂账·候 PI 取回 |
| `27d04f1e3b3e` | — | 3 | 14417 | `_kd_h2_anchor_chain_erratum_2026_10_20.md`:136（＋1 件） | ④登记挂账·候 PI 取回 |
| `2b2a0da2d8fb` | — | 3 | 8060 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:94（＋1 件） | ④登记挂账·候 PI 取回 |
| `2c5dd849a2d0` | — | 3 | 6401 | `_repo_post_cleanup_snapshot_2026_10_12.md`:348（＋1 件） | ④登记挂账·候 PI 取回 |
| `2c63da9f7a69` | TRAE_V3_ASSET_ERRATUM_2026_09_23.md | 3 | 275754 | `_trae_errata_sha_drift_attribution_2026_10_01.md`:79（＋1 件） | ④登记挂账·候 PI 取回 |
| `2ca81a4a2d62` | — | 3 | 1494 | `_repo_post_cleanup_snapshot_2026_10_12.md`:245（＋1 件） | ④登记挂账·候 PI 取回 |
| `2dd8039d47e4` | — | 3 | 198204 | `_trae_errata_sha_drift_attribution_2026_10_01.md`:75（＋0 件） | ④登记挂账·候 PI 取回 |
| `2fadea9f6259` | _v3_v4_achievements_inventory_3dir_2026_09_2 | 3 | 355369 | `_achievements_inventory_full_2026_10_09.md`:3389（＋2 件） | ②改指（候选：_v3_v4_achievements_inventory_3dir_2026_09_24.md·近字节 355819） |
| `2fc0385e55db` | user.md | 3 | 89720 | `_ghost_reference_register_2026_10_21.md`:123（＋1 件） | ④登记挂账·候 PI 取回 |
| `304347705aa5` | ·366 B｜卡 rowid 718（v178 之卡 | 3 | 3057 | `_fake_kd_p3_readjudication_2026_10_21.md`:106（＋1 件） | ④登记挂账·候 PI 取回 |
| `308419654ed7` | — | 3 | 58665 | `_archive_area_readonly_verification_2026_10_18.md`:70（＋2 件） | ④登记挂账·候 PI 取回 |
| `31cf2891cf21` | _v155_adoption_effect_2026_10_20.md | 3 | 87389 | `_ghost_reference_register_2026_10_21.md`:180（＋1 件） | ②改指（候选：_v155_adoption_effect_2026_10_20.md·近字节 89658） |
| `31dd999df336` | — | 3 | 21608 | `_cleanup511_exec_register_2026_10_17.md`:44（＋1 件） | ④登记挂账·候 PI 取回 |
| `31e3001c76aa` | — | 3 | 3965 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:88（＋1 件） | ④登记挂账·候 PI 取回 |
| `354e51cfe6d4` | _pi_card_answers_register_2026_10_20_supplem | 3 | 45778 | `_pi_card_answers_register_2026_10_20_supplement_4cards.md`:22（＋2 件） | ②改指（候选：_pi_card_answers_register_2026_10_20_supplement_4cards.md·近字节 46545） |
| `35d6e8c4f838` | — | 3 | 3227 | `_repo_post_cleanup_snapshot_2026_10_12.md`:436（＋1 件） | ④登记挂账·候 PI 取回 |
| `3b88842a96ea` | — | 3 | 2249 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:104（＋1 件） | ④登记挂账·候 PI 取回 |
| `3bb9e2856d95` | — | 3 | 3024 | `_repo_post_cleanup_snapshot_2026_10_12.md`:284（＋1 件） | ④登记挂账·候 PI 取回 |
| `3ca8eec4888f` | — | 3 | 4241 | `_repo_post_cleanup_snapshot_2026_10_12.md`:290（＋1 件） | ④登记挂账·候 PI 取回 |
| `3ebbf43ecdaf` | — | 3 | 2795 | `_repo_post_cleanup_snapshot_2026_10_12.md`:437（＋1 件） | ④登记挂账·候 PI 取回 |
| `3f1ce14b0f10` | _root_session_history_memo_main_2026_10_14.m | 3 | 140072 | `_ghost_reference_register_2026_10_21.md`:220（＋2 件） | ④登记挂账·候 PI 取回 |
| `408e40b5d697` | — | 3 | 3067 | `_repo_post_cleanup_snapshot_2026_10_12.md`:314（＋1 件） | ④登记挂账·候 PI 取回 |
| `41f89124f28e` | _d1_backfill_intake_verdict_2026_10_01.md | 3 | 42115 | `_family_de_stale_refresh_repo_exec_2026_10_14.md`:79（＋0 件） | ②改指（候选：results___d1_backfill_intake_verdict_2026_10_01.md·近字节 42115） |
| `43a8ce00dc25` | — | 3 | 14826 | `_archive_area_readonly_verification_2026_10_18.md`:54（＋2 件） | ④登记挂账·候 PI 取回 |
| `43ee275d6ad5` | — | 3 | 159 | `_batch10_deliberation_judgment_2026_10_14.md`:80（＋1 件） | ④登记挂账·候 PI 取回 |
| `4a15fd75f840` | — | 3 | 5723 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:86（＋1 件） | ④登记挂账·候 PI 取回 |
| `4ae5be9872a1` | — | 3 | 3374 | `_repo_post_cleanup_snapshot_2026_10_12.md`:434（＋1 件） | ④登记挂账·候 PI 取回 |
| `4cd75ea5bd03` | 起**之前置行（＝**前棒口径**） ／ **7,131** ／ ** | 3 | 7131 | `_g2_residual_cause_register_2026_10_12.md`:72（＋0 件） | ④登记挂账·候 PI 取回 |
| `4ddbd6ab89e7` | — | 3 | 38485 | `_achievements_inventory_full_2026_10_18.md`:592（＋1 件） | ④登记挂账·候 PI 取回 |
| `4df64e278ff3` | — | 3 | 1992 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:106（＋1 件） | ④登记挂账·候 PI 取回 |
| `4f1f759f66af` | — | 3 | 9824 | `_repo_post_cleanup_snapshot_2026_10_12.md`:295（＋1 件） | ④登记挂账·候 PI 取回 |
| `51cc4179a02c` | — | 3 | 1128 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:109（＋1 件） | ④登记挂账·候 PI 取回 |
| `5472b7d7bfba` | — | 3 | 4843 | `_repo_post_cleanup_snapshot_2026_10_12.md`:293（＋1 件） | ④登记挂账·候 PI 取回 |
| `57d953dba704` | — | 3 | 5177 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:92（＋1 件） | ④登记挂账·候 PI 取回 |
| `59290d15352c` | — | 3 | 6396 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:105（＋1 件） | ④登记挂账·候 PI 取回 |
| `5950bd120b87` | — | 3 | 5003 | `_repo_post_cleanup_snapshot_2026_10_12.md`:249（＋1 件） | ④登记挂账·候 PI 取回 |
| `5c7cbfec8a92` | _v155_adoption_effect_2026_10_20.md | 3 | 97778 | `_ghost_reference_register_2026_10_21.md`:96（＋1 件） | ④登记挂账·候 PI 取回 |
| `5c8edd9c4230` | — | 3 | 37254 | `_v5_confirm_b5_decisions_register_2026_09_29.md`:234（＋0 件） | ④登记挂账·候 PI 取回 |
| `5f222d513f87` | — | 3 | 5192 | `_repo_post_cleanup_snapshot_2026_10_12.md`:298（＋1 件） | ④登记挂账·候 PI 取回 |
| `5f55151bdc76` | — | 3 | 1832 | `_repo_post_cleanup_snapshot_2026_10_12.md`:444（＋1 件） | ④登记挂账·候 PI 取回 |
| `5fe01006406f` | _v155_adoption_effect_2026_10_20.md | 3 | 84676 | `_ghost_reference_register_2026_10_21.md`:218（＋1 件） | ④登记挂账·候 PI 取回 |
| `605f4e963169` | — | 3 | 3160 | `_repo_post_cleanup_snapshot_2026_10_12.md`:435（＋1 件） | ④登记挂账·候 PI 取回 |
| `60a3e0f59b6f` | — | 3 | 1412 | `_repo_post_cleanup_snapshot_2026_10_12.md`:412（＋1 件） | ④登记挂账·候 PI 取回 |
| `614415fe4019` | — | 3 | 2333 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:95（＋1 件） | ④登记挂账·候 PI 取回 |
| `614cbcdb9ff2` | _kd_eta_selection_verdict_2026_10_20.md | 3 | 43522 | `_eta_preexp_run_register_2026_10_20.md`:393（＋2 件） | ④登记挂账·候 PI 取回 |
| `61f84109fc1f` | — | 3 | 2194 | `_repo_post_cleanup_snapshot_2026_10_12.md`:433（＋1 件） | ④登记挂账·候 PI 取回 |
| `6489bacf4b03` | — | 3 | 4132 | `_repo_post_cleanup_snapshot_2026_10_12.md`:312（＋1 件） | ④登记挂账·候 PI 取回 |
| `651e968aa801` | _t2_path_b_build_exec_2026_10_16.md | 3 | 44275 | `_m08_measured_enumeration_exec_2026_10_16.md`:435（＋2 件） | ④登记挂账·候 PI 取回 |
| `692421d309ea` | — | 3 | 9800 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:100（＋1 件） | ④登记挂账·候 PI 取回 |
| `6a409f23309c` | — | 3 | 8617 | `_archive_area_readonly_verification_2026_10_18.md`:56（＋2 件） | ④登记挂账·候 PI 取回 |
| `6b820f7da4a4` | 〔幽灵引用·未上传:_cpatomic_verify_2〕 | 3 | 3144 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:34（＋1 件） | ④登记挂账·候 PI 取回 |
| `6cb324e4c646` | _kd_h1_h7_disposition_draft_2026_10_20.md | 3 | 70534 | `_ghost_reference_register_2026_10_21.md`:214（＋1 件） | ②改指（候选：_kd_h1_h7_disposition_draft_2026_10_20.md·近字节 72915） |
| `6cc3d55ec4f7` | — | 3 | 2419 | `_repo_post_cleanup_snapshot_2026_10_12.md`:286（＋1 件） | ④登记挂账·候 PI 取回 |
| `6f0098ed1c0c` | — | 3 | 5627 | `_repo_post_cleanup_snapshot_2026_10_12.md`:256（＋1 件） | ④登记挂账·候 PI 取回 |
| `6f1fb2b43c30` | 鲍勃_扩大脱敏面修复推送回执_2026_10_18_简办.md | 3 | 3422 | `_s14_session_scan_out_2026_10_21.md`:284（＋2 件） | ④登记挂账·候 PI 取回 |
| `6f4221a52b77` | — | 3 | 3875 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:84（＋1 件） | ④登记挂账·候 PI 取回 |
| `71f7fac128bc` | — | 3 | 1761 | `_ge01_ecr_anchor_sourcing_design_2026_10_14.md`:45（＋0 件） | ④登记挂账·候 PI 取回 |
| `72289e06bf62` | — | 3 | 7353 | `_achievements_inventory_full_2026_10_18.md`:596（＋1 件） | ④登记挂账·候 PI 取回 |
| `73a2253b0d3d` | — | 3 | 1678 | `_repo_post_cleanup_snapshot_2026_10_12.md`:280（＋1 件） | ④登记挂账·候 PI 取回 |
| `796e3a8b432f` | 〔幽灵引用·未上传:_rj5_mapping_test_〕 | 3 | 1384 | `_v3_recheck_12_rj5_provenance_2026_09_27.md`:236（＋2 件） | ④登记挂账·候 PI 取回 |
| `7c05160d5b33` | — | 3 | 7959 | `_repo_post_cleanup_snapshot_2026_10_12.md`:310（＋1 件） | ④登记挂账·候 PI 取回 |
| `7c0751d00f55` | — | 3 | 1492 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:80（＋1 件） | ④登记挂账·候 PI 取回 |
| `7f2126cfb6ff` | — | 3 | 2418 | `_repo_post_cleanup_snapshot_2026_10_12.md`:257（＋1 件） | ④登记挂账·候 PI 取回 |
| `7f2fba38c479` | — | 3 | 7173 | `_archive_area_readonly_verification_2026_10_18.md`:58（＋2 件） | ④登记挂账·候 PI 取回 |
| `7fd493e240d7` | — | 3 | 23278 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:108（＋1 件） | ④登记挂账·候 PI 取回 |
| `80eba48d3d0b` | — | 3 | 4920 | `_repo_post_cleanup_snapshot_2026_10_12.md`:241（＋1 件） | ④登记挂账·候 PI 取回 |
| `817639d7e5c3` | — | 3 | 6596 | `_repo_post_cleanup_snapshot_2026_10_12.md`:162（＋1 件） | ④登记挂账·候 PI 取回 |
| `823aa6deb0c5` | — | 3 | 4682 | `_repo_post_cleanup_snapshot_2026_10_12.md`:313（＋1 件） | ④登记挂账·候 PI 取回 |
| `868f88e11251` | — | 3 | 1969 | `_repo_post_cleanup_snapshot_2026_10_12.md`:370（＋1 件） | ④登记挂账·候 PI 取回 |
| `87497a1cf3b0` | — | 3 | 6344 | `_repo_post_cleanup_snapshot_2026_10_12.md`:180（＋1 件） | ④登记挂账·候 PI 取回 |
| `8823a3df0a45` | — | 3 | 43831 | `_achievements_inventory_full_2026_10_18.md`:600（＋1 件） | ④登记挂账·候 PI 取回 |
| `886af37712bc` | — | 3 | 15077 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:90（＋1 件） | ④登记挂账·候 PI 取回 |
| `8a2c160bc671` | — | 3 | 23508 | `_leftover_minor_adoptions_register_2026_10_12.md`:80（＋2 件） | ④登记挂账·候 PI 取回 |
| `8b6dbcc64a16` | — | 3 | 7304 | `_repo_post_cleanup_snapshot_2026_10_12.md`:247（＋1 件） | ④登记挂账·候 PI 取回 |
| `8f911e5d6cee` | _eta_main_run_register_2026_10_20.md | 3 | 38383 | `_eta_main_run_register_2026_10_20.md`:340（＋2 件） | ②改指（候选：_eta_main_run_register_2026_10_20.md·近字节 39157） |
| `90023e831e24` | — | 3 | 1152 | `_repo_post_cleanup_snapshot_2026_10_12.md`:250（＋1 件） | ④登记挂账·候 PI 取回 |
| `91a62de1fa50` | — | 3 | 20538 | `_kd_h2_anchor_chain_erratum_2026_10_20.md`:134（＋1 件） | ④登记挂账·候 PI 取回 |
| `96e37ca7314f` | — | 3 | 14709 | `_repo_post_cleanup_snapshot_2026_10_12.md`:322（＋1 件） | ④登记挂账·候 PI 取回 |
| `9aabb430172f` | _round56_idx_sc1_temp_deletion_deviation_not | 3 | 8143 | `_archive_area_readonly_verification_2026_10_18.md`:65（＋2 件） | ②改指（候选：_round56_idx_sc1_temp_deletion_deviation_note_2026_10_10.md·近字节 8181） |
| `9b7deadbc2ed` | — | 3 | 6735 | `_repo_post_cleanup_snapshot_2026_10_12.md`:311（＋1 件） | ④登记挂账·候 PI 取回 |
| `9c869f65ed1f` | ／9,385 **为现行版**； | 3 | 11915 | `_bob_commission_acceptance_and_r4_waiver_register_2026_10_12.md`:54（＋2 件） | ④登记挂账·候 PI 取回 |
| `9da3d432a134` | _glm_response_v2_template_2026_09_18.md | 3 | 44133 | `_archive_area_readonly_verification_2026_10_18.md`:64（＋2 件） | ②改指（候选：_glm_response_v2_template_2026_09_18.md·近字节 44191） |
| `a131c696a55e` | — | 3 | 8584 | `_repo_post_cleanup_snapshot_2026_10_12.md`:299（＋1 件） | ④登记挂账·候 PI 取回 |
| `a2c177ec2bfe` | _v4_tmp_cleanup_2026_09_28.md | 3 | 5122 | `_archive_area_readonly_verification_2026_10_18.md`:72（＋2 件） | ②改指（候选：_v4_tmp_cleanup_2026_09_28.md·近字节 5131） |
| `a2c315831efe` | — | 3 | 3240 | `_repo_post_cleanup_snapshot_2026_10_12.md`:445（＋1 件） | ④登记挂账·候 PI 取回 |
| `a2f7950a4399` | — | 3 | 5729 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:85（＋1 件） | ④登记挂账·候 PI 取回 |
| `a40bf112389c` | — | 3 | 12219 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:83（＋1 件） | ④登记挂账·候 PI 取回 |
| `a4467a8a7118` | — | 3 | 1722 | `_repo_post_cleanup_snapshot_2026_10_12.md`:439（＋1 件） | ④登记挂账·候 PI 取回 |
| `a4d2003024b7` | — | 3 | 49347 | `_achievements_inventory_full_2026_10_18.md`:597（＋1 件） | ④登记挂账·候 PI 取回 |
| `a59587eb5e3f` | — | 3 | 2524 | `_repo_post_cleanup_snapshot_2026_10_12.md`:410（＋1 件） | ④登记挂账·候 PI 取回 |
| `a7155d07b98b` | — | 3 | 1812 | `_repo_post_cleanup_snapshot_2026_10_12.md`:261（＋1 件） | ④登记挂账·候 PI 取回 |
| `a7a80c786fa2` | _v4_pi_decision_questionnaire_2026_09_21_v1. | 3 | 113424 | `_archive_area_readonly_verification_2026_10_18.md`:61（＋2 件） | ②改指（候选：_v4_pi_decision_questionnaire_2026_09_21_v1.1.md.bak_2026_09_22_gB_post.md·近字节 113508） |
| `a87adc2ed532` | — | 3 | 32393 | `_archive_area_readonly_verification_2026_10_18.md`:67（＋2 件） | ④登记挂账·候 PI 取回 |
| `a8995d36078e` | — | 3 | 307384 | `_h5_session_census_2026_10_19_part1.md`:1585（＋1 件） | ④登记挂账·候 PI 取回 |
| `aa2e0beac0ef` | — | 3 | 26778 | `_achievements_inventory_full_2026_10_18.md`:593（＋1 件） | ④登记挂账·候 PI 取回 |
| `ab6b1aa8be4b` | — | 3 | 3641 | `_repo_post_cleanup_snapshot_2026_10_12.md`:242（＋1 件） | ④登记挂账·候 PI 取回 |
| `ac6978f92a6d` | — | 3 | 4201 | `_repo_post_cleanup_snapshot_2026_10_12.md`:258（＋1 件） | ④登记挂账·候 PI 取回 |
| `acf84b8657c5` | — | 3 | 6957 | `_repo_post_cleanup_snapshot_2026_10_12.md`:186（＋1 件） | ④登记挂账·候 PI 取回 |
| `ad615fb96fa1` | — | 3 | 3954 | `_repo_post_cleanup_snapshot_2026_10_12.md`:294（＋1 件） | ④登记挂账·候 PI 取回 |
| `ae51dde19dd6` | — | 3 | 2218 | `_repo_post_cleanup_snapshot_2026_10_12.md`:285（＋1 件） | ④登记挂账·候 PI 取回 |
| `afdce88a79bf` | plan.md | 3 | 10072 | `_closeout_bucket_refresh_2026_10_09.md`:19（＋2 件） | ④登记挂账·候 PI 取回 |
| `b0e0eb00279b` | — | 3 | 2313 | `_repo_post_cleanup_snapshot_2026_10_12.md`:260（＋1 件） | ④登记挂账·候 PI 取回 |
| `b552c38f6b2d` | _pi_card_answers_register_2026_10_17_v47.md | 3 | 60655 | `_pi_card_answers_register_2026_10_17_v47.md`:305（＋1 件） | ④登记挂账·候 PI 取回 |
| `b6339d9f2435` | — | 3 | 13475 | `_kd_h2_anchor_chain_erratum_2026_10_20.md`:135（＋1 件） | ④登记挂账·候 PI 取回 |
| `b633a675c9de` | _t1_qwen_temp_sweep_r2_exec_register_2026_10 | 3 | 23683 | `_archive_area_readonly_verification_2026_10_18.md`:68（＋2 件） | ②改指（候选：_t1_qwen_temp_sweep_r2_exec_register_2026_10_09.md·近字节 23681） |
| `b687b9844ba2` | — | 3 | 6412 | `_repo_post_cleanup_snapshot_2026_10_12.md`:300（＋1 件） | ④登记挂账·候 PI 取回 |
| `b7cb3b7baaa1` | — | 3 | 4537 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:91（＋1 件） | ④登记挂账·候 PI 取回 |
| `b8866d89b84c` | — | 3 | 4518 | `_repo_post_cleanup_snapshot_2026_10_12.md`:296（＋1 件） | ④登记挂账·候 PI 取回 |
| `bbc91c17c8db` | _ge03_ge04_claim_proposal_2026_10_22.md | 3 | 63063 | `_ge03_ge04_claim_proposal_2026_10_22.md`:471（＋0 件） | ④登记挂账·候 PI 取回 |
| `bcde7ec623a3` | — | 3 | 2607 | `_repo_post_cleanup_snapshot_2026_10_12.md`:364（＋1 件） | ④登记挂账·候 PI 取回 |
| `be50e9e27ed7` | — | 3 | 20904 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:82（＋1 件） | ④登记挂账·候 PI 取回 |
| `be98a7b238b0` | — | 3 | 120810 | `_archive_area_readonly_verification_2026_10_18.md`:63（＋2 件） | ④登记挂账·候 PI 取回 |
| `bf2642242416` | — | 3 | 7782 | `_repo_post_cleanup_snapshot_2026_10_12.md`:187（＋1 件） | ④登记挂账·候 PI 取回 |
| `c196aa7709ef` | — | 3 | 3883 | `_kd_h2_anchor_chain_erratum_2026_10_20.md`:39（＋0 件） | ④登记挂账·候 PI 取回 |
| `c7652cb07e11` | — | 3 | 4309 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:103（＋1 件） | ④登记挂账·候 PI 取回 |
| `c7805ba58107` | README_V4_2026_09_29.md | 3 | 39149 | `_naming_ruling_note_2026_09_29.md`:6（＋0 件） | ④登记挂账·候 PI 取回 |
| `cf04cf2f39db` | 全量补实验执行计划 | 3 | 14904 | `_batch9_deliberation_judgment_2026_10_14.md`:67（＋0 件） | ④登记挂账·候 PI 取回 |
| `d0c22d58b4d1` | — | 3 | 8897 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:110（＋1 件） | ④登记挂账·候 PI 取回 |
| `d1905830b2bd` | _t1_qwen_temp_sweep_verdict_2026_10_09.md | 3 | 21652 | `_archive_area_readonly_verification_2026_10_18.md`:71（＋2 件） | ②改指（候选：_t1_qwen_temp_sweep_verdict_2026_10_09.md·近字节 21672） |
| `d47722a1123a` | — | 3 | 3226 | `_kd_h2_anchor_chain_erratum_2026_10_20.md`:140（＋1 件） | ④登记挂账·候 PI 取回 |
| `d67d93ac99da` | — | 3 | 52623 | `_whitelist_and_scope_ruling_effect_2026_10_17.md`:364（＋0 件） | ④登记挂账·候 PI 取回 |
| `d6a3361a794a` | 不计；**本棒 3 件新出件不计**（其件内提及源件名 = 来源链登记，非旧引用面）。扫 | 3 | 5784 | `_v4_closeout_bulk_reorganize_register_2026_10_12.md`:166（＋1 件） | ④登记挂账·候 PI 取回 |
| `da0e79e6e834` | — | 3 | 5929 | `_repo_post_cleanup_snapshot_2026_10_12.md`:248（＋1 件） | ④登记挂账·候 PI 取回 |
| `da2f2dd35fb7` | ） ／ ⚠ 该件 §9-3 自报 | 3 | 65953 | `_ghost_reference_register_2026_10_21.md`:127（＋2 件） | ④登记挂账·候 PI 取回 |
| `dbe562353608` | — | 3 | 2863 | `_repo_post_cleanup_snapshot_2026_10_12.md`:161（＋1 件） | ④登记挂账·候 PI 取回 |
| `dcaa4b6b3b0b` | 〔幽灵引用·未上传:_l14v3_sensitivity〕 | 3 | 2292 | `_v4_closeout_bulk_reorganize_register_2026_10_12.md`:106（＋1 件） | ④登记挂账·候 PI 取回 |
| `dcfea9293d62` | — | 3 | 6529 | `_repo_post_cleanup_snapshot_2026_10_12.md`:265（＋1 件） | ④登记挂账·候 PI 取回 |
| `debf0de9ac50` | _kd_h5_session_history_pilot_1of10_2026_10_2 | 3 | 1004131 | `_ghost_reference_register_2026_10_21.md`:211（＋1 件） | ②改指（候选：_kd_h5_session_history_pilot_1of10_2026_10_20.md·近字节 1000949） |
| `e4226aaf3380` | 〔幽灵引用·未上传:_tail3_atomic_veri〕 | 3 | 11116 | `_v4_closeout_bulk_reorganize_register_2026_10_12.md`:167（＋1 件） | ④登记挂账·候 PI 取回 |
| `e42cf6c832bf` | — | 3 | 5671 | `_repo_post_cleanup_snapshot_2026_10_12.md`:430（＋1 件） | ④登记挂账·候 PI 取回 |
| `e4b1ec3de237` | — | 3 | 15653 | `_achievements_inventory_full_2026_10_18.md`:594（＋1 件） | ④登记挂账·候 PI 取回 |
| `e6bdd2712a13` | — | 3 | 2943 | `_repo_post_cleanup_snapshot_2026_10_12.md`:432（＋1 件） | ④登记挂账·候 PI 取回 |
| `e992573fbe2f` | — | 3 | 50554 | `_archive_area_readonly_verification_2026_10_18.md`:52（＋2 件） | ④登记挂账·候 PI 取回 |
| `eb35c7a23cf5` | — | 3 | 5806 | `_repo_post_cleanup_snapshot_2026_10_12.md`:461（＋1 件） | ④登记挂账·候 PI 取回 |
| `eb9ce9683ad3` | 〔幽灵引用·未上传:_l14v3_n26_metrics〕 | 3 | 2579 | `_v4_closeout_bulk_reorganize_register_2026_10_12.md`:105（＋1 件） | ④登记挂账·候 PI 取回 |
| `f40d20d0794f` | — | 3 | 2396 | `_repo_post_cleanup_snapshot_2026_10_12.md`:438（＋1 件） | ④登记挂账·候 PI 取回 |
| `f43a7df2ffc1` | — | 3 | 6548 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:81（＋1 件） | ④登记挂账·候 PI 取回 |
| `f4a736868825` | — | 3 | 7634 | `_repo_post_cleanup_snapshot_2026_10_12.md`:384（＋1 件） | ④登记挂账·候 PI 取回 |
| `f52d6d66c131` | _kd_h5_session_history_domain_caliber_2026_1 | 3 | 54474 | `_ghost_reference_register_2026_10_21.md`:199（＋2 件） | ②改指（候选：_kd_h5_session_history_domain_caliber_2026_10_20.md·近字节 55674） |
| `facb130159b1` | — | 3 | 8342 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:89（＋1 件） | ④登记挂账·候 PI 取回 |
| `fad7c1e36df8` | — | 3 | 160556 | `_s14_session_scan_out_2026_10_21.md`:284（＋2 件） | ④登记挂账·候 PI 取回 |
| `fc4f86b859fe` | — | 3 | 324996 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:102（＋1 件） | ④登记挂账·候 PI 取回 |
| `fc5f722a09f5` | ·366 B｜卡 rowid 718（v178 之卡 | 3 | 454 | `_fake_kd_p3_readjudication_2026_10_21.md`:106（＋1 件） | ④登记挂账·候 PI 取回 |
| `fccfcc869e7a` | — | 3 | 257362 | `_trae_errata_sha_drift_attribution_2026_10_01.md`:78（＋0 件） | ④登记挂账·候 PI 取回 |
| `fdce3b850265` | — | 3 | 3543 | `_cleanup_r2_plus83_exec_register_2026_10_17.md`:97（＋1 件） | ④登记挂账·候 PI 取回 |
| `ff15ac539b98` | — | 3 | 53180 | `_archive_area_readonly_verification_2026_10_18.md`:69（＋2 件） | ④登记挂账·候 PI 取回 |
| `ff1950e09388` | _glm_reply_pack_intake_verification_2026_10_ | 3 | 59342 | `_ghost_reference_register_2026_10_21.md`:198（＋1 件） | ④登记挂账·候 PI 取回 |
| `0423aecb53ec` | _fake_kd_p3_readjudication_2026_10_21.md | 2 | 366 | `_fake_kd_p3_readjudication_2026_10_21.md`:106（＋1 件） | ④登记挂账·候 PI 取回 |
| `04d96fe5cfa6` | _deemphasis_sha_drift_register_B6a_2026_10_0 | 2 | 11696 | `_batch3_execution_receipt_kimi_2026_10_18.md`:174（＋1 件） | ④登记挂账·候 PI 取回 |
| `064013615cc2` | — | 2 | 59155 | `_achievements_inventory_full_2026_10_18.md`:598（＋1 件） | ④登记挂账·候 PI 取回 |
| `083087218a8d` | — | 2 | 292215 | `_trae_errata_sha_drift_attribution_2026_10_01.md`:80（＋0 件） | ④登记挂账·候 PI 取回 |
| `0a92d7bd23f1` | — | 2 | 192689 | `_batch3_execution_receipt_kimi_2026_10_18.md`:63（＋1 件） | ④登记挂账·候 PI 取回 |
| `0b0a6883ab57` | — | 2 | 3144 | `_mirror_morphology_comparison_2026_10_18.md`:1255（＋1 件） | ④登记挂账·候 PI 取回 |
| `11fea51889b3` | — | 2 | 57531 | `_trae_errata_sha_drift_attribution_2026_10_01.md`:68（＋0 件） | ④登记挂账·候 PI 取回 |
| `12864634c039` | — | 2 | 7193 | `_batch3_execution_receipt_kimi_2026_10_18.md`:161（＋1 件） | ④登记挂账·候 PI 取回 |
| `12ab21c73db8` | _root_session_history_memo_main_2026_10_14.m | 2 | 150494 | `_ghost_reference_register_2026_10_21.md`:219（＋1 件） | ④登记挂账·候 PI 取回 |
| `12f5acb11e9c` | _root_session_history_memo_main_2026_10_14.m | 2 | 165599 | `_ghost_reference_register_2026_10_21.md`:139（＋1 件） | ②改指（候选：results___root_session_history_memo_main_2026_10_14.md·近字节 160625） |
| `130d42ffbef2` | _kd_h5_session_history_domain_caliber_2026_1 | 2 | 54499 | `_ghost_reference_register_2026_10_21.md`:182（＋1 件） | ②改指（候选：_kd_h5_session_history_domain_caliber_2026_10_20.md·近字节 55674） |
| `13425104558a` | — | 2 | 5508890 | `_v5_checkpoint_tail3_revision_2026_09_29.md`:135（＋0 件） | ④登记挂账·候 PI 取回 |
| `1381b75d060b` | — | 2 | 60325 | `_batch3_execution_receipt_kimi_2026_10_18.md`:53（＋1 件） | ④登记挂账·候 PI 取回 |
| `143121c7e120` | _pi_card_answers_register_2026_10_17_v46.md | 2 | 62410 | `_pi_card_answers_register_2026_10_17_v46.md`:323（＋1 件） | ②改指（候选：_pi_card_answers_register_2026_10_17_v46.md·近字节 64372） |
| `1550772e0eed` | — | 2 | 6456 | `_batch3_execution_receipt_kimi_2026_10_18.md`:193（＋1 件） | ④登记挂账·候 PI 取回 |
| `1603d2ce19cc` | _deemphasis_sha_drift_register_B6c_2026_10_0 | 2 | 14351 | `_batch3_execution_receipt_kimi_2026_10_18.md`:176（＋1 件） | ④登记挂账·候 PI 取回 |
| `17067c06d71e` | 禁传； | 2 | 11823 | `_questionnaire_cards_intake_register_2026_10_09.md`:2724（＋0 件） | ④登记挂账·候 PI 取回 |
| `193f22f69988` | _fake_kd_p3_readjudication_2026_10_21.md | 2 | 3365 | `_fake_kd_p3_readjudication_2026_10_21.md`:33（＋1 件） | ④登记挂账·候 PI 取回 |
| `1a4da74b9f68` | — | 2 | 3867 | `_mirror_morphology_comparison_2026_10_18.md`:1282（＋1 件） | ④登记挂账·候 PI 取回 |
| `1ca402efebef` | — | 2 | 175 | `_fake_verdict_reverify_sixitem_ledger_2026_09_30.md`:265（＋0 件） | ④登记挂账·候 PI 取回 |
| `1d0ed76deb8b` | — | 2 | 2248 | `_mirror_morphology_comparison_2026_10_18.md`:1259（＋1 件） | ④登记挂账·候 PI 取回 |
| `1d1ab1f1d4f5` | _kd_h5_session_history_pilot_1of10_2026_10_2 | 2 | 14775 | `_ghost_reference_register_2026_10_21.md`:105（＋1 件） | ④登记挂账·候 PI 取回 |
| `2243e90c71df` | — | 2 | 45871 | `_eta_preexp_stop_register_2026_10_20.md`:299（＋0 件） | ④登记挂账·候 PI 取回 |
| `2624d4f8f34f` | — | 2 | 19595 | `_mirror_morphology_comparison_2026_10_18.md`:1306（＋1 件） | ④登记挂账·候 PI 取回 |
| `2bac80dfb235` | ·366 B｜卡 rowid 609（语二之卡 | 2 | 2093 | `_fake_kd_p3_readjudication_2026_10_21.md`:106（＋1 件） | ④登记挂账·候 PI 取回 |
| `2cba7dee5225` | _fake_kd_p3_readjudication_2026_10_21.md | 2 | 454 | `_fake_kd_p3_readjudication_2026_10_21.md`:33（＋1 件） | ④登记挂账·候 PI 取回 |
| `2d9d5a83dc4e` | — | 2 | 38319 | `_achievements_inventory_full_2026_10_18.md`:599（＋1 件） | ④登记挂账·候 PI 取回 |
| `2ea190308493` | _root_session_history_memo_main_2026_10_14.m | 2 | 52974 | `_pi_card_answers_register_2026_10_16_v31.md`:166（＋1 件） | ④登记挂账·候 PI 取回 |
| `2fb51610efcf` | _q2_77_74_62_three_caliber_consolidation_reg | 2 | 4609 | `_batch3_execution_receipt_kimi_2026_10_18.md`:181（＋1 件） | ④登记挂账·候 PI 取回 |
| `32376299b40f` | — | 2 | 27641 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:183（＋0 件） | ④登记挂账·候 PI 取回 |
| `39267bbc3ea0` | — | 2 | 6659 | `_mirror_morphology_comparison_2026_10_18.md`:1301（＋1 件） | ④登记挂账·候 PI 取回 |
| `3a2decf0d8cf` | — | 2 | 1384 | `_mirror_morphology_comparison_2026_10_18.md`:1296（＋1 件） | ④登记挂账·候 PI 取回 |
| `3bacf10ffed6` | _deemphasis_sha_drift_register_B5_2026_10_06 | 2 | 14237 | `_batch3_execution_receipt_kimi_2026_10_18.md`:173（＋1 件） | ④登记挂账·候 PI 取回 |
| `3bcd1b03e4fd` | — | 2 | 7557 | `_kd_h2_anchor_chain_erratum_2026_10_20.md`:123（＋0 件） | ④登记挂账·候 PI 取回 |
| `3bd65a80adc4` | _cluster_j_glm_62_adjudication_2026_10_19.md | 2 | 47967 | `_cluster_j_glm_62_adjudication_2026_10_19.md`:301（＋1 件） | ②改指（候选：_cluster_j_glm_62_adjudication_2026_10_19.md·近字节 48997） |
| `3da8e31baade` | ·366 B｜卡 rowid 609（语二之卡 | 2 | 454 | `_fake_kd_p3_readjudication_2026_10_21.md`:106（＋1 件） | ④登记挂账·候 PI 取回 |
| `3e0399a304ae` | — | 2 | 8121 | `_cleanup_r2_repo_sub_exec_register_2026_10_17.md`:52（＋0 件） | ④登记挂账·候 PI 取回 |
| `3e528f9919ae` | — | 2 | 31470 | `_batch3_execution_receipt_kimi_2026_10_18.md`:189（＋1 件） | ④登记挂账·候 PI 取回 |
| `3e821561537b` | — | 2 | 10760 | `_batch3_execution_receipt_kimi_2026_10_18.md`:190（＋1 件） | ④登记挂账·候 PI 取回 |
| `3faa1bc953fb` | — | 2 | 11116 | `_mirror_morphology_comparison_2026_10_18.md`:1308（＋1 件） | ④登记挂账·候 PI 取回 |
| `40a94d0d129f` | — | 2 | 3471 | `_mirror_morphology_comparison_2026_10_18.md`:1311（＋1 件） | ④登记挂账·候 PI 取回 |
| `424cf2d07884` | — | 2 | 120144 | `_trae_errata_sha_drift_attribution_2026_10_01.md`:71（＋0 件） | ④登记挂账·候 PI 取回 |
| `439e68738f93` | — | 2 | 2313 | `_mirror_morphology_comparison_2026_10_18.md`:1288（＋1 件） | ④登记挂账·候 PI 取回 |
| `4582f2c1b52f` | — | 2 | 1014 | `_fake_verdict_reverify_sixitem_ledger_2026_09_30.md`:265（＋0 件） | ④登记挂账·候 PI 取回 |
| `4670cf5c9b75` | TRAE_FIX_REQUEST_3RISKS_2026_09_11.md | 2 | 16008 | `_batch3_execution_receipt_kimi_2026_10_18.md`:86（＋1 件） | ②改指（候选：TRAE_FIX_REQUEST_3RISKS_2026_09_11.md·近字节 15990） |
| `48a46fa99a97` | — | 2 | 11765 | `_batch3_execution_receipt_kimi_2026_10_18.md`:191（＋1 件） | ④登记挂账·候 PI 取回 |
| `4a0d97c4c77b` | — | 2 | 3098 | `_material_expansion_build_exec_2026_10_16.md`:79（＋1 件） | ④登记挂账·候 PI 取回 |
| `4c07d998cc13` | — | 2 | 1973 | `_t2_path_b_build_exec_2026_10_16.md`:122（＋1 件） | ④登记挂账·候 PI 取回 |
| `506d85c37e11` | — | 2 | 2399 | `_kd_h2_anchor_chain_erratum_2026_10_20.md`:142（＋0 件） | ④登记挂账·候 PI 取回 |
| `523bd2a85761` | — | 2 | 6187 | `_material_expansion_build_exec_2026_10_16.md`:78（＋1 件） | ④登记挂账·候 PI 取回 |
| `52772769c459` | _fake_kd_p3_readjudication_2026_10_21.md | 2 | 366 | `_fake_kd_p3_readjudication_2026_10_21.md`:106（＋1 件） | ④登记挂账·候 PI 取回 |
| `52cc4c06dc4e` | — | 2 | 67735 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:225（＋1 件） | ④登记挂账·候 PI 取回 |
| `5365182c8f1c` | — | 2 | 1420 | `_mirror_morphology_comparison_2026_10_18.md`:1297（＋1 件） | ④登记挂账·候 PI 取回 |
| `55b6f19e3c1f` | _fake_kd_p3_readjudication_2026_10_21.md | 2 | 1959 | `_fake_kd_p3_readjudication_2026_10_21.md`:106（＋1 件） | ④登记挂账·候 PI 取回 |
| `56342823a0ca` | _deemphasis_sha_drift_register_B1_2026_10_06 | 2 | 1206 | `_batch3_execution_receipt_kimi_2026_10_18.md`:169（＋1 件） | ④登记挂账·候 PI 取回 |
| `57855e19a280` | — | 2 | 2377 | `_mirror_morphology_comparison_2026_10_18.md`:1264（＋1 件） | ④登记挂账·候 PI 取回 |
| `58a557cb0426` | — | 2 | 2066 | `_mirror_morphology_comparison_2026_10_18.md`:1314（＋1 件） | ④登记挂账·候 PI 取回 |
| `5959acd1e683` | — | 2 | 2597 | `_p4_fallback_target_search_register_2026_10_12.md`:93（＋0 件） | ④登记挂账·候 PI 取回 |
| `5dfa39f98d45` | — | 2 | 52838 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:219（＋1 件） | ④登记挂账·候 PI 取回 |
| `5e7c6bf0bf8b` | _glm_reply_pack_intake_verification_2026_10_ | 2 | 3425 | `_ghost_reference_register_2026_10_21.md`:134（＋1 件） | ④登记挂账·候 PI 取回 |
| `5f37681d4c45` | — | 2 | 2297 | `_cleanup_r2_repo_sub_exec_register_2026_10_17.md`:53（＋0 件） | ④登记挂账·候 PI 取回 |
| `610cd2c2bbdb` | LETTER_FROM_TRAE_REVIEW_2026_09_16.md | 2 | 7724 | `_batch3_execution_receipt_kimi_2026_10_18.md`:83（＋1 件） | ②改指（候选：LETTER_FROM_TRAE_REVIEW_2026_09_16.md·近字节 7718） |
| `622ae907e666` | — | 2 | 3057 | `_mirror_morphology_comparison_2026_10_18.md`:1299（＋1 件） | ④登记挂账·候 PI 取回 |
| `6291b2a9aa55` | _probe2.md | 2 | 1333 | `_cleanup_r2_repo_sub_exec_register_2026_10_17.md`:56（＋0 件） | ②改指（候选：d85_probe2.py·近字节 1355） |
| `62cfa0d3ad8e` | （**160,603 B** · mtime 11:30:34 ✅ 仍合）／ | 2 | 97141 | `_cluster_h_directory_adjudication_2026_10_18.md`:42（＋0 件） | ④登记挂账·候 PI 取回 |
| `6507336ade0e` | — | 2 | 1278 | `_batch3_execution_receipt_kimi_2026_10_18.md`:48（＋1 件） | ④登记挂账·候 PI 取回 |
| `66a057896f09` | — | 2 | 6476 | `_mirror_morphology_comparison_2026_10_18.md`:1253（＋1 件） | ④登记挂账·候 PI 取回 |
| `66ad4ead0fa3` | _root_session_history_memo_main_2026_10_14.m | 2 | 172724 | `_ghost_reference_register_2026_10_21.md`:130（＋1 件） | ④登记挂账·候 PI 取回 |
| `66cebbdc834b` | — | 2 | 67812 | `_trae_errata_sha_drift_attribution_2026_10_01.md`:69（＋0 件） | ④登记挂账·候 PI 取回 |
| `6844bf36f762` | — | 2 | 158079 | `_trae_errata_sha_drift_attribution_2026_10_01.md`:73（＋0 件） | ④登记挂账·候 PI 取回 |
| `6b0ecbcfad76` | _s4_kv3s_4_123_judgment_prereg_2026_10_12.md | 2 | 5637 | `_batch3_execution_receipt_kimi_2026_10_18.md`:185（＋1 件） | ④登记挂账·候 PI 取回 |
| `6c6fb7078a9d` | 〔幽灵引用·未上传:_tail3_atomic_make〕 | 2 | 19595 | `_v4_closeout_bulk_reorganize_register_2026_10_12.md`:165（＋1 件） | ④登记挂账·候 PI 取回 |
| `6d08fef6755f` | — | 2 | 5062 | `_mirror_morphology_comparison_2026_10_18.md`:1313（＋1 件） | ④登记挂账·候 PI 取回 |
| `6dd00db4ba4f` | — | 2 | 10772 | `_mirror_morphology_comparison_2026_10_18.md`:1254（＋1 件） | ④登记挂账·候 PI 取回 |
| `6f88c954c36d` | _e20_runner_sha_drift_dual_value_register_20 | 2 | 4352 | `_batch3_execution_receipt_kimi_2026_10_18.md`:177（＋1 件） | ④登记挂账·候 PI 取回 |
| `720cfaf53161` | LETTER_FROM_TRAE_2026_09_11.md | 2 | 13629 | `_batch3_execution_receipt_kimi_2026_10_18.md`:81（＋1 件） | ②改指（候选：LETTER_FROM_TRAE_2026_09_11.md·近字节 13617） |
| `736c19ff59b9` | _deemphasis_sha_drift_register_B4_2026_10_06 | 2 | 11715 | `_batch3_execution_receipt_kimi_2026_10_18.md`:172（＋1 件） | ④登记挂账·候 PI 取回 |
| `7421807680d5` | _gt_reconstruction_sha_drift_dual_value_regi | 2 | 4789 | `_batch3_execution_receipt_kimi_2026_10_18.md`:179（＋1 件） | ④登记挂账·候 PI 取回 |
| `74e9b4667bad` | — | 2 | 634458 | `_mirror_morphology_comparison_2026_10_18.md`:1265（＋1 件） | ④登记挂账·候 PI 取回 |
| `76f2f4ffafd1` | — | 2 | 6581 | `_material_expansion_build_exec_2026_10_16.md`:75（＋1 件） | ④登记挂账·候 PI 取回 |
| `789a11aa9a2a` | _root_session_history_memo_main_2026_10_14.m | 2 | 177334 | `_ghost_reference_register_2026_10_21.md`:175（＋1 件） | ④登记挂账·候 PI 取回 |
| `79732c90c8a4` | — | 2 | 4106 | `_mirror_morphology_comparison_2026_10_18.md`:1283（＋1 件） | ④登记挂账·候 PI 取回 |
| `843d944a56ec` | _c5_kv3df_0_1_minmaxstd_suppl_report_2026_10 | 2 | 8476 | `_batch3_execution_receipt_kimi_2026_10_18.md`:163（＋1 件） | ④登记挂账·候 PI 取回 |
| `8979135365bd` | — | 2 | 3647 | `_mirror_morphology_comparison_2026_10_18.md`:1302（＋1 件） | ④登记挂账·候 PI 取回 |
| `898e7cb3f1fc` | — | 2 | 1014 | `_mirror_morphology_comparison_2026_10_18.md`:1289（＋1 件） | ④登记挂账·候 PI 取回 |
| `8adff5e918e3` | D7_EXTERNAL_ADVISOR_ONLINE_PUSH_REQUIREMENTS | 2 | 8066 | `_batch3_execution_receipt_kimi_2026_10_18.md`:80（＋1 件） | ④登记挂账·候 PI 取回 |
| `8e3b4ad1ffc6` | — | 2 | 1445 | `_mirror_morphology_comparison_2026_10_18.md`:1269（＋1 件） | ④登记挂账·候 PI 取回 |
| `8f06c5f70790` | _kd_eta_main_run_verdict_2026_10_20.md | 2 | 775577 | `_ghost_reference_register_2026_10_21.md`:135（＋1 件） | ④登记挂账·候 PI 取回 |
| `8fe8821fe0e1` | _t1_substrate_gap_precondition_2026_10_01.md | 2 | 22196 | `_family_de_stale_refresh_repo_exec_2026_10_14.md`:120（＋0 件） | ②改指（候选：_t1_substrate_gap_precondition_2026_10_01.md·近字节 22196） |
| `905953d35f0a` | — | 2 | 1636 | `_mirror_morphology_comparison_2026_10_18.md`:1278（＋1 件） | ④登记挂账·候 PI 取回 |
| `9143181f395a` | ·366 B｜卡 rowid 615（宿主之卡 | 2 | 1906 | `_fake_kd_p3_readjudication_2026_10_21.md`:106（＋1 件） | ④登记挂账·候 PI 取回 |
| `936582d2d57b` | — | 2 | 39448 | `_batch3_execution_receipt_kimi_2026_10_18.md`:55（＋1 件） | ④登记挂账·候 PI 取回 |
| `9399019d4f8e` | _glm_reply_pack_intake_verification_2026_10_ | 2 | 168605 | `_ghost_reference_register_2026_10_21.md`:166（＋1 件） | ④登记挂账·候 PI 取回 |
| `94074cd9f442` | — | 2 | 1257 | `_material_expansion_build_exec_2026_10_16.md`:74（＋1 件） | ④登记挂账·候 PI 取回 |
| `94948106150b` | — | 2 | 82649 | `_clue_book_v06_backfill_and_dual_version_register_2026_10_12.md`:26（＋0 件） | ④登记挂账·候 PI 取回 |
| `957e7426e0db` | — | 2 | 74268 | `_batch3_execution_receipt_kimi_2026_10_18.md`:47（＋1 件） | ④登记挂账·候 PI 取回 |
| `96aa598222a9` | （原件）｜ | 2 | 103914 | `_v5_confirm_b5_decisions_register_2026_09_29.md`:222（＋0 件） | ④登记挂账·候 PI 取回 |
| `974578688ea3` | — | 2 | 1158 | `_mirror_morphology_comparison_2026_10_18.md`:1256（＋1 件） | ④登记挂账·候 PI 取回 |
| `9a9bcb9d3fe9` | — | 2 | 2099 | `_fake_verdict_reverify_sixitem_ledger_2026_09_30.md`:265（＋0 件） | ④登记挂账·候 PI 取回 |
| `9ce076070280` | — | 2 | 19685 | `_mirror_morphology_comparison_2026_10_18.md`:1315（＋1 件） | ④登记挂账·候 PI 取回 |
| `9dbe95f45ee0` | — | 2 | 5784 | `_mirror_morphology_comparison_2026_10_18.md`:1307（＋1 件） | ④登记挂账·候 PI 取回 |
| `a0ea7fd3795d` | D3_ONLINE_MIDTERM_TEMPLATE.md | 2 | 4397 | `_mirror_morphology_comparison_2026_10_18.md`:1323（＋1 件） | ④登记挂账·候 PI 取回 |
| `a202d62875f8` | — | 2 | 1039 | `_fake_verdict_reverify_sixitem_ledger_2026_09_30.md`:265（＋0 件） | ④登记挂账·候 PI 取回 |
| `a5c77c7dc81d` | — | 2 | 3477 | `_batch3_execution_receipt_kimi_2026_10_18.md`:186（＋1 件） | ④登记挂账·候 PI 取回 |
| `a7471684df24` | — | 2 | 12998 | `_cleanup_r2_repo_sub_exec_register_2026_10_17.md`:54（＋0 件） | ④登记挂账·候 PI 取回 |
| `a75d029036c1` | _d7_external_advisor_online_publish_v1_20260 | 2 | 9915 | `_batch3_execution_receipt_kimi_2026_10_18.md`:168（＋1 件） | ④登记挂账·候 PI 取回 |
| `aa2968356e41` | _pi_card_answers_register_2026_10_17_v46.md | 2 | 59426 | `_pi_card_answers_register_2026_10_17_v46.md`:320（＋1 件） | ④登记挂账·候 PI 取回 |
| `ab50fec180da` | — | 2 | 174445 | `_trae_errata_sha_drift_attribution_2026_10_01.md`:74（＋0 件） | ④登记挂账·候 PI 取回 |
| `ad24d5c8e2c6` | _fake_kd_p3_readjudication_2026_10_21.md | 2 | 2096 | `_fake_kd_p3_readjudication_2026_10_21.md`:106（＋1 件） | ④登记挂账·候 PI 取回 |
| `add00a68d28a` | _deemphasis_sha_drift_register_B6b_2026_10_0 | 2 | 22219 | `_batch3_execution_receipt_kimi_2026_10_18.md`:175（＋1 件） | ④登记挂账·候 PI 取回 |
| `af5d2e3832cc` | — | 2 | 260598 | `_v186_v225_adoption_effect_2026_10_22.md`:1275（＋0 件） | ④登记挂账·候 PI 取回 |
| `af8148a9fdac` | — | 2 | 2544 | `_batch3_execution_receipt_kimi_2026_10_18.md`:194（＋1 件） | ④登记挂账·候 PI 取回 |
| `b2e2d53b3c16` | _pi_decision_backlog_consolidated_2026_10_21 | 2 | 39007 | `_ghost_reference_register_2026_10_21.md`:186（＋1 件） | ④登记挂账·候 PI 取回 |
| `b4e45cffa5cd` | 〔幽灵引用·未上传:_cpatomic_keyscan_〕 | 2 | 2672 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:36（＋1 件） | ④登记挂账·候 PI 取回 |
| `b7fa15fa25c1` | _root_session_history_memo_main_2026_10_14.m | 2 | 170921 | `_ghost_reference_register_2026_10_21.md`:185（＋1 件） | ④登记挂账·候 PI 取回 |
| `ba25509a2ef6` | — | 2 | 96985 | `_trae_errata_sha_drift_attribution_2026_10_01.md`:70（＋0 件） | ④登记挂账·候 PI 取回 |
| `bd231a2482ae` | — | 2 | 67049 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:191（＋1 件） | ④登记挂账·候 PI 取回 |
| `bdabfcec9798` | — | 2 | 26138 | `_three_seed_readout_validity_effect_register_2026_10_16.md`:13（＋0 件） | ④登记挂账·候 PI 取回 |
| `be5610adfb55` | — | 2 | 2042 | `_batch3_execution_receipt_kimi_2026_10_18.md`:188（＋1 件） | ④登记挂账·候 PI 取回 |
| `bf6c810051d1` | — | 2 | 45794 | `_batch3_execution_receipt_kimi_2026_10_18.md`:49（＋1 件） | ④登记挂账·候 PI 取回 |
| `c1d32ba51a59` | _experiment_execution_plan_v1_1_funnel5_adop | 2 | 21411 | `_batch3_execution_receipt_kimi_2026_10_18.md`:178（＋1 件） | ④登记挂账·候 PI 取回 |
| `c254c3e3d5fd` | — | 2 | 2233138 | `_mirror_morphology_comparison_2026_10_18.md`:1268（＋1 件） | ④登记挂账·候 PI 取回 |
| `c753e5679f06` | plan.md | 2 | 10806 | `_fake_verdict_reverify_sixitem_ledger_2026_09_30.md`:212（＋0 件） | ②改指（候选：V3X_TEAM_IMPROVEMENT_PLAN_2026_09_16.md·近字节 11232） |
| `c78e5368c61f` | — | 2 | 5699 | `_mirror_morphology_comparison_2026_10_18.md`:1312（＋1 件） | ④登记挂账·候 PI 取回 |
| `ca0b3b81b7ce` | — | 2 | 1543 | `_mirror_morphology_comparison_2026_10_18.md`:1250（＋1 件） | ④登记挂账·候 PI 取回 |
| `ca8b95ddaa70` | — | 2 | 225731 | `_trae_errata_sha_drift_attribution_2026_10_01.md`:76（＋0 件） | ④登记挂账·候 PI 取回 |
| `cc75f1e3d8af` | _q2_77_74_62_three_caliber_consolidation_reg | 2 | 4609 | `_stage1_prereq_wave1_evidence_2026_10_20.md`:110（＋0 件） | ④登记挂账·候 PI 取回 |
| `cd0a30e1f0da` | plan.md | 2 | 8425 | `_fake_verdict_reverify_sixitem_ledger_2026_09_30.md`:203（＋0 件） | ②改指（候选：_r2_tool_10_plan2.py·近字节 8115） |
| `ce129294776f` | _e50_c2.md | 2 | 17220 | `_mirror_morphology_comparison_2026_10_18.md`:1261（＋1 件） | ④登记挂账·候 PI 取回 |
| `ce2196c90cbc` | — | 2 | 2325 | `_kd_h2_anchor_chain_erratum_2026_10_20.md`:141（＋0 件） | ④登记挂账·候 PI 取回 |
| `d357b3b05776` | _eta_preexp_run_register_2026_10_20.md | 2 | 1382964 | `_eta_preexp_run_register_2026_10_20.md`:376（＋1 件） | ④登记挂账·候 PI 取回 |
| `d3ec5cf4e6f1` | _repo_state_auth_refresh_register_2026_10_18 | 2 | 11449 | `_batch3_execution_receipt_kimi_2026_10_18.md`:182（＋1 件） | ④登记挂账·候 PI 取回 |
| `d55669326b31` | — | 2 | 20994 | `_mirror_morphology_comparison_2026_10_18.md`:1257（＋1 件） | ④登记挂账·候 PI 取回 |
| `d6286be2bc43` | README_V4_2026_09_29.md | 2 | 48679 | `_naming_ruling_note_2026_09_29.md`:58（＋0 件） | ④登记挂账·候 PI 取回 |
| `d68f2ef16e70` | _deemphasis_sha_drift_register_B2_2026_10_06 | 2 | 1418 | `_batch3_execution_receipt_kimi_2026_10_18.md`:170（＋1 件） | ④登记挂账·候 PI 取回 |
| `d799eebec764` | — | 2 | 40547 | `_erratum_3_14H_caliber_impact_2026_10_17.md`:276（＋0 件） | ④登记挂账·候 PI 取回 |
| `d94143c77e96` | — | 2 | 30834 | `_mirror_morphology_comparison_2026_10_18.md`:1290（＋1 件） | ④登记挂账·候 PI 取回 |
| `d98befafc10e` | — | 2 | 1278 | `_batch3_execution_receipt_kimi_2026_10_18.md`:50（＋1 件） | ④登记挂账·候 PI 取回 |
| `daac269ece6a` | — | 2 | 2292 | `_mirror_morphology_comparison_2026_10_18.md`:1271（＋1 件） | ④登记挂账·候 PI 取回 |
| `dc5f1ad66372` | — | 2 | 1568 | `_cleanup_r2_repo_sub_exec_register_2026_10_17.md`:51（＋0 件） | ④登记挂账·候 PI 取回 |
| `dc78f9a89b1c` | — | 2 | 10320 | `_kd_h2_anchor_chain_erratum_2026_10_20.md`:122（＋0 件） | ④登记挂账·候 PI 取回 |
| `ddafeb14dccc` | _v5_spec_prereq_reference_archive_2026_10_18 | 2 | 20423 | `_batch3_execution_receipt_kimi_2026_10_18.md`:206（＋1 件） | ④登记挂账·候 PI 取回 |
| `ddb27880cb79` | — | 2 | 2672 | `_mirror_morphology_comparison_2026_10_18.md`:1251（＋1 件） | ④登记挂账·候 PI 取回 |
| `dfb09fbf6116` | — | 2 | 102379 | `_pi_card_answers_register_2026_10_17_v51.md`:457（＋0 件） | ④登记挂账·候 PI 取回 |
| `dfeda739c97f` | — | 2 | 10307 | `_batch3_execution_receipt_kimi_2026_10_18.md`:192（＋1 件） | ④登记挂账·候 PI 取回 |
| `e4548dc95e27` | — | 2 | 192689 | `_kt_a1_anchor_drift_root_cause_2026_10_14.md`:112（＋0 件） | ④登记挂账·候 PI 取回 |
| `e5df207d1ece` | _c5_kv3df_0_1_minmaxstd_suppl_prereg_2026_10 | 2 | 5697 | `_batch3_execution_receipt_kimi_2026_10_18.md`:162（＋1 件） | ④登记挂账·候 PI 取回 |
| `e639d79f3a82` | — | 2 | 4142 | `_mirror_morphology_comparison_2026_10_18.md`:1249（＋1 件） | ④登记挂账·候 PI 取回 |
| `e86608904586` | ·366 B｜卡 rowid 615（宿主之卡 | 2 | 366 | `_fake_kd_p3_readjudication_2026_10_21.md`:106（＋1 件） | ④登记挂账·候 PI 取回 |
| `eb9759f2915d` | _s3_kv3s_3_4_judgment_prereg_2026_10_12.md | 2 | 5678 | `_batch3_execution_receipt_kimi_2026_10_18.md`:183（＋1 件） | ④登记挂账·候 PI 取回 |
| `ed9a552ae6cd` | 消息）｜**L432** ＝ 行 SHA-12 | 2 | 4876 | `_fake_kd_p4_reversal_errata_2026_10_21.md`:324（＋1 件） | ④登记挂账·候 PI 取回 |
| `ef19acfeb585` | — | 2 | 141013 | `_trae_errata_sha_drift_attribution_2026_10_01.md`:72（＋0 件） | ④登记挂账·候 PI 取回 |
| `efbbbf7b0d0a` | — | 2 | 952252 | `_m44_status_enum_backfill_design_2026_10_16.md`:73（＋0 件） | ④登记挂账·候 PI 取回 |
| `f19b45ca5335` | _kd_h1_h7_disposition_draft_2026_10_20.md | 2 | 70189 | `_ghost_reference_register_2026_10_21.md`:173（＋1 件） | ②改指（候选：_kd_h1_h7_disposition_draft_2026_10_20.md·近字节 72915） |
| `f2d18d779682` | — | 2 | 2876 | `_mirror_morphology_comparison_2026_10_18.md`:1281（＋1 件） | ④登记挂账·候 PI 取回 |
| `f35523665a53` | _deemphasis_sha_drift_register_B3_2026_10_06 | 2 | 2830 | `_batch3_execution_receipt_kimi_2026_10_18.md`:171（＋1 件） | ④登记挂账·候 PI 取回 |
| `f5fbfa3126c7` | — | 2 | 55314 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:189（＋1 件） | ④登记挂账·候 PI 取回 |
| `f616e00cf299` | _root_session_history_memo_main_2026_10_14.m | 2 | 94447 | `_pi_card_answers_register_2026_10_17_v46.md`:324（＋1 件） | ④登记挂账·候 PI 取回 |
| `f81723551363` | — | 2 | 1160 | `_batch3_execution_receipt_kimi_2026_10_18.md`:187（＋1 件） | ④登记挂账·候 PI 取回 |
| `f8808795aad0` | — | 2 | 1588 | `_mirror_morphology_comparison_2026_10_18.md`:1298（＋1 件） | ④登记挂账·候 PI 取回 |
| `f8acfce7217b` | — | 2 | 7154 | `_t2_path_b_build_exec_2026_10_16.md`:122（＋1 件） | ④登记挂账·候 PI 取回 |
| `f8c3fdbeb1b6` | — | 2 | 3143 | `_batch3_execution_receipt_kimi_2026_10_18.md`:88（＋1 件） | ④登记挂账·候 PI 取回 |
| `f94990aef3b4` | _e50_c1.md | 2 | 16236 | `_mirror_morphology_comparison_2026_10_18.md`:1260（＋1 件） | ④登记挂账·候 PI 取回 |
| `f9c4150ec3dd` | _s3_kv3s_3_4_supplementary_verdict_2026_10_1 | 2 | 6156 | `_batch3_execution_receipt_kimi_2026_10_18.md`:184（＋1 件） | ④登记挂账·候 PI 取回 |
| `fa9fb4874ad6` | — | 2 | 1636 | `_mirror_morphology_comparison_2026_10_18.md`:1277（＋1 件） | ④登记挂账·候 PI 取回 |
| `faf21d9c274e` | — | 2 | 95139 | `_mirror_morphology_comparison_2026_10_18.md`:1322（＋1 件） | ④登记挂账·候 PI 取回 |
| `faf22d4872ad` | — | 2 | 2579 | `_mirror_morphology_comparison_2026_10_18.md`:1270（＋1 件） | ④登记挂账·候 PI 取回 |
| `fb90fd5e6988` | _kd_eta_selection_verdict_2026_10_20.md | 2 | 36612 | `_ghost_reference_register_2026_10_21.md`:213（＋1 件） | ②改指（候选：_kd_eta_selection_verdict_2026_10_20.md·近字节 37788） |
| `fe6909a580f4` | _pi_decision_backlog_consolidated_2026_10_21 | 2 | 53612 | `_ghost_reference_register_2026_10_21.md`:183（＋1 件） | ④登记挂账·候 PI 取回 |
| `007bde15eeed` | — | 1 | 8952 | `_batch3_execution_receipt_kimi_2026_10_18.md`:262（＋0 件） | ①补正（补登现行真实指纹） |
| `00bc7551df03` | _unique_supplement_letter_approval_effect_20 | 1 | 51240 | `_batch3_execution_receipt_kimi_2026_10_18.md`:388（＋0 件） | ②改指（候选：_unique_supplement_letter_approval_effect_2026_10_18.md·近字节 51238） |
| `00c1b6c49015` | _v5_r4_residual_merged_catalogue_2026_09_29. | 1 | 102414 | `_batch3_execution_receipt_kimi_2026_10_18.md`:861（＋0 件） | ②改指（候选：_v5_r4_residual_merged_catalogue_2026_09_29.md·近字节 102410） |
| `0100a7f4c3f6` | — | 1 | 7662 | `_supplement_execution_receipt_kimi_2026_10_18.md`:249（＋0 件） | ①补正（补登现行真实指纹） |
| `01a29ec3dad2` | — | 1 | 65449 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:203（＋0 件） | ①补正（补登现行真实指纹） |
| `025fb2f7345d` | — | 1 | 1283 | `_cleanup511_exec_register_2026_10_17.md`:239（＋0 件） | ①补正（补登现行真实指纹） |
| `0284c0035f1a` | _v4_maindir_cleanup_moves_ledger_v6_2026_09_ | 1 | 37653 | `_batch3_execution_receipt_kimi_2026_10_18.md`:846（＋0 件） | ②改指（候选：_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md·近字节 37629） |
| `039b075d4d92` | _v4_gA1_terminology_draft_2026_09_22.md | 1 | 9820 | `_batch3_execution_receipt_kimi_2026_10_18.md`:839（＋0 件） | ②改指（候选：results___v4_gA1_terminology_draft_2026_09_22.md·近字节 9818） |
| `03b5ff1fd4e8` | — | 1 | 7001 | `_cleanup511_exec_register_2026_10_17.md`:413（＋0 件） | ①补正（补登现行真实指纹） |
| `0485d86b7746` | — | 1 | 44307 | `_cleanup511_exec_register_2026_10_17.md`:227（＋0 件） | ①补正（补登现行真实指纹） |
| `049776685d11` | — | 1 | 28350 | `_cleanup511_exec_register_2026_10_17.md`:209（＋0 件） | ①补正（补登现行真实指纹） |
| `0544ac64d703` | — | 1 | 1036 | `_supplement_execution_receipt_kimi_2026_10_18.md`:79（＋0 件） | ①补正（补登现行真实指纹） |
| `054e08dc3b6e` | _skill_call_surface_probe_supplement_a_2026_ | 1 | 34765 | `_skill_reference_update_and_user_surface_survey_2026_09_30.md`:521（＋0 件） | ①补正（补登现行真实指纹） |
| `0571f07c0fdf` | — | 1 | 10013 | `_cleanup511_exec_register_2026_10_17.md`:293（＋0 件） | ①补正（补登现行真实指纹） |
| `060da13ce763` | — | 1 | 9476 | `_supplement_execution_receipt_kimi_2026_10_18.md`:258（＋0 件） | ①补正（补登现行真实指纹） |
| `0629bf16b893` | — | 1 | 101289 | `_cleanup511_exec_register_2026_10_17.md`:370（＋0 件） | ①补正（补登现行真实指纹） |
| `063921f85a2c` | — | 1 | 13442 | `_material_expansion_build_exec_2026_10_16.md`:57（＋0 件） | ①补正（补登现行真实指纹） |
| `0662a9fc6168` | — | 1 | 46909 | `_supplement_execution_receipt_kimi_2026_10_18.md`:345（＋0 件） | ①补正（补登现行真实指纹） |
| `06ae586bde64` | — | 1 | 1348 | `_cleanup511_exec_register_2026_10_17.md`:346（＋0 件） | ①补正（补登现行真实指纹） |
| `06d65401458f` | _v5_sub_artifact_ledger_history_r3_2026_09_2 | 1 | 128828 | `_batch3_execution_receipt_kimi_2026_10_18.md`:864（＋0 件） | ②改指（候选：results___v5_sub_artifact_ledger_history_r3_2026_09_29.md·近字节 128834） |
| `06f8ac063105` | — | 1 | 3479 | `_cleanup511_exec_register_2026_10_17.md`:276（＋0 件） | ①补正（补登现行真实指纹） |
| `077e58890235` | — | 1 | 4220 | `_batch3_execution_receipt_kimi_2026_10_18.md`:286（＋0 件） | ①补正（补登现行真实指纹） |
| `07cb48d7e9e2` | — | 1 | 1646 | `_cleanup511_exec_register_2026_10_17.md`:445（＋0 件） | ①补正（补登现行真实指纹） |
| `0804046920d3` | — | 1 | 1384 | `_supplement_execution_receipt_kimi_2026_10_18.md`:198（＋0 件） | ①补正（补登现行真实指纹） |
| `086dd86b07d7` | — | 1 | 1256 | `_cleanup511_exec_register_2026_10_17.md`:331（＋0 件） | ①补正（补登现行真实指纹） |
| `0876c28e4694` | — | 1 | 14527 | `_cleanup511_exec_register_2026_10_17.md`:94（＋0 件） | ①补正（补登现行真实指纹） |
| `098dceadec82` | — | 1 | 9723 | `_forgotten_recovery_register_2026_10_08.md`:62（＋0 件） | ①补正（补登现行真实指纹） |
| `0a00688ac31c` | — | 1 | 1562 | `_supplement_execution_receipt_kimi_2026_10_18.md`:123（＋0 件） | ①补正（补登现行真实指纹） |
| `0a92d1936b1b` | — | 1 | 1779 | `_cleanup511_exec_register_2026_10_17.md`:456（＋0 件） | ①补正（补登现行真实指纹） |
| `0af710cf1eef` | — | 1 | 19595 | `_supplement_execution_receipt_kimi_2026_10_18.md`:239（＋0 件） | ①补正（补登现行真实指纹） |
| `0afb03163ed4` | — | 1 | 2687 | `_batch3_execution_receipt_kimi_2026_10_18.md`:237（＋0 件） | ①补正（补登现行真实指纹） |
| `0bb38962013f` | — | 1 | 93324 | `_batch3_execution_receipt_kimi_2026_10_18.md`:285（＋0 件） | ①补正（补登现行真实指纹） |
| `0c50a7661fea` | — | 1 | 8646 | `_cleanup511_exec_register_2026_10_17.md`:376（＋0 件） | ①补正（补登现行真实指纹） |
| `0c694079b862` | — | 1 | 3686 | `_supplement_execution_receipt_kimi_2026_10_18.md`:158（＋0 件） | ①补正（补登现行真实指纹） |
| `0d03f4f85333` | — | 1 | 34126 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:194（＋0 件） | ①补正（补登现行真实指纹） |
| `0d5aefaf6750` | — | 1 | 32393 | `_supplement_execution_receipt_kimi_2026_10_18.md`:313（＋0 件） | ①补正（补登现行真实指纹） |
| `0d83b0db1269` | — | 1 | 3115 | `_ge02_anchor_landing_effect_register_2026_10_16.md`:93（＋0 件） | ①补正（补登现行真实指纹） |
| `0db7be0fe547` | — | 1 | 3866 | `_supplement_execution_receipt_kimi_2026_10_18.md`:141（＋0 件） | ①补正（补登现行真实指纹） |
| `0dce3cf4404b` | — | 1 | 7342 | `_batch3_execution_receipt_kimi_2026_10_18.md`:281（＋0 件） | ①补正（补登现行真实指纹） |
| `0dfd3b6f363b` | — | 1 | 5252 | `_cleanup511_exec_register_2026_10_17.md`:53（＋0 件） | ①补正（补登现行真实指纹） |
| `0e0d7e5edca3` | — | 1 | 1098 | `_cleanup511_exec_register_2026_10_17.md`:394（＋0 件） | ①补正（补登现行真实指纹） |
| `0e2b1cc71dfb` | _stage1_prereq_wave1_evidence_2026_10_20.md | 1 | 39872 | `_ghost_reference_register_2026_10_21.md`:76（＋0 件） | ①补正（补登现行真实指纹） |
| `0e56b13c733f` | _v5_sub_artifact_ledger_history_r1_2026_09_2 | 1 | 48543 | `_batch3_execution_receipt_kimi_2026_10_18.md`:862（＋0 件） | ②改指（候选：_v5_sub_artifact_ledger_history_r1_2026_09_29.md·近字节 48539） |
| `0f05265005f5` | — | 1 | 67220 | `_v5_sub_artifact_ledger_2026_09_28.md`:179（＋0 件） | ①补正（补登现行真实指纹） |
| `0f64eff3d553` | — | 1 | 8917 | `_batch3_execution_receipt_kimi_2026_10_18.md`:432（＋0 件） | ①补正（补登现行真实指纹） |
| `106605dcf464` | — | 1 | 55324 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:205（＋0 件） | ①补正（补登现行真实指纹） |
| `108a5fc1f597` | — | 1 | 3334 | `_cleanup511_exec_register_2026_10_17.md`:281（＋0 件） | ①补正（补登现行真实指纹） |
| `10bd3a54f21b` | — | 1 | 35742 | `_cleanup511_exec_register_2026_10_17.md`:240（＋0 件） | ①补正（补登现行真实指纹） |
| `11363670a32a` | — | 1 | 2773 | `_cleanup511_exec_register_2026_10_17.md`:123（＋0 件） | ①补正（补登现行真实指纹） |
| `11380f9df5bd` | — | 1 | 1636 | `_supplement_execution_receipt_kimi_2026_10_18.md`:149（＋0 件） | ①补正（补登现行真实指纹） |
| `114c466124e3` | — | 1 | 2486 | `_supplement_execution_receipt_kimi_2026_10_18.md`:191（＋0 件） | ①补正（补登现行真实指纹） |
| `12110bb61ab1` | — | 1 | 96443 | `_supplement_execution_receipt_kimi_2026_10_18.md`:233（＋0 件） | ①补正（补登现行真实指纹） |
| `12af91501ec7` | — | 1 | 6132 | `_supplement_execution_receipt_kimi_2026_10_18.md`:329（＋0 件） | ①补正（补登现行真实指纹） |
| `12bcd3f69d28` | — | 1 | 152881 | `_cleanup511_exec_register_2026_10_17.md`:323（＋0 件） | ①补正（补登现行真实指纹） |
| `12c3be4c2a40` | _mini_round_6_7_settlement_register_2026_10_ | 1 | 68053 | `_supplement_execution_receipt_kimi_2026_10_18.md`:381（＋0 件） | ②改指（候选：_mini_round_6_7_settlement_register_2026_10_01.md·近字节 68053） |
| `12ee00f5865f` | — | 1 | 3748 | `_cleanup511_exec_register_2026_10_17.md`:425（＋0 件） | ①补正（补登现行真实指纹） |
| `131ce78626a5` | — | 1 | 3074 | `_supplement_execution_receipt_kimi_2026_10_18.md`:85（＋0 件） | ①补正（补登现行真实指纹） |
| `132b55b0d9a0` | — | 1 | 4397 | `_supplement_execution_receipt_kimi_2026_10_18.md`:291（＋0 件） | ①补正（补登现行真实指纹） |
| `13ddacba74e9` | — | 1 | 48135 | `_cleanup511_exec_register_2026_10_17.md`:114（＋0 件） | ①补正（补登现行真实指纹） |
| `14045422bf33` | — | 1 | 24634 | `_batch3_execution_receipt_kimi_2026_10_18.md`:269（＋0 件） | ①补正（补登现行真实指纹） |
| `147162fce9c2` | — | 1 | 18813 | `_cleanup511_exec_register_2026_10_17.md`:214（＋0 件） | ①补正（补登现行真实指纹） |
| `14f708509f62` | _tmp_disposal_register_2026_10_10.md | 1 | 20812 | `_supplement_execution_receipt_kimi_2026_10_18.md`:322（＋0 件） | ②改指（候选：_tmp_disposal_register_2026_10_10.md·近字节 20812） |
| `1554066ec0f8` | — | 1 | 1780 | `_cleanup511_exec_register_2026_10_17.md`:383（＋0 件） | ①补正（补登现行真实指纹） |
| `157c589b06d9` | — | 1 | 83090 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:134（＋0 件） | ①补正（补登现行真实指纹） |
| `162a9419b037` | — | 1 | 5227 | `_cleanup511_exec_register_2026_10_17.md`:288（＋0 件） | ①补正（补登现行真实指纹） |
| `16e2f8ac7364` | — | 1 | 3749 | `_cleanup511_exec_register_2026_10_17.md`:364（＋0 件） | ①补正（补登现行真实指纹） |
| `179854e9e2c9` | — | 1 | 1907 | `_supplement_execution_receipt_kimi_2026_10_18.md`:77（＋0 件） | ①补正（补登现行真实指纹） |
| `17ba92d24cd4` | _s3_d1_rulings_supplement_register_2026_10_0 | 1 | 28762 | `_supplement_execution_receipt_kimi_2026_10_18.md`:382（＋0 件） | ②改指（候选：_s3_d1_rulings_supplement_register_2026_10_01.md·近字节 28762） |
| `17f02e853e30` | _g5_displacement_threshold_draft_2026_10_10. | 1 | 25619 | `_supplement_execution_receipt_kimi_2026_10_18.md`:302（＋0 件） | ②改指（候选：_g5_displacement_threshold_draft_2026_10_10.md·近字节 25619） |
| `184c47ba8d2a` | — | 1 | 1358 | `_supplement_execution_receipt_kimi_2026_10_18.md`:208（＋0 件） | ①补正（补登现行真实指纹） |
| `184d28f330c9` | MEMORY.md | 1 | 2284 | `_independent_review_history_gaps_kd_2026_10_19_sub.md`:116（＋0 件） | ①补正（补登现行真实指纹） |
| `1853c54e1130` | — | 1 | 52982 | `_cleanup511_exec_register_2026_10_17.md`:233（＋0 件） | ①补正（补登现行真实指纹） |
| `19501a3ce320` | — | 1 | 3304 | `_supplement_execution_receipt_kimi_2026_10_18.md`:212（＋0 件） | ①补正（补登现行真实指纹） |
| `19560d996179` | — | 1 | 3052 | `_cleanup511_exec_register_2026_10_17.md`:236（＋0 件） | ①补正（补登现行真实指纹） |
| `1957e9387f72` | — | 1 | 2756 | `_supplement_execution_receipt_kimi_2026_10_18.md`:221（＋0 件） | ①补正（补登现行真实指纹） |
| `19881212aa35` | — | 1 | 24792 | `_cleanup511_exec_register_2026_10_17.md`:104（＋0 件） | ①补正（补登现行真实指纹） |
| `19b5e68bdf47` | — | 1 | 2542 | `_batch3_execution_receipt_kimi_2026_10_18.md`:241（＋0 件） | ①补正（补登现行真实指纹） |
| `1b2c7dc66074` | — | 1 | 2735 | `_cleanup511_exec_register_2026_10_17.md`:399（＋0 件） | ①补正（补登现行真实指纹） |
| `1b50b08530fa` | — | 1 | 6322 | `_supplement_execution_receipt_kimi_2026_10_18.md`:93（＋0 件） | ①补正（补登现行真实指纹） |
| `1b6acae668c1` | — | 1 | 3149 | `_supplement_execution_receipt_kimi_2026_10_18.md`:269（＋0 件） | ①补正（补登现行真实指纹） |
| `1c38afe2f3c4` | — | 1 | 2454 | `_supplement_execution_receipt_kimi_2026_10_18.md`:67（＋0 件） | ①补正（补登现行真实指纹） |
| `1c758a3e916d` | — | 1 | 2642 | `_cleanup511_exec_register_2026_10_17.md`:434（＋0 件） | ①补正（补登现行真实指纹） |
| `1cde2cd14af6` | — | 1 | 3435 | `_cleanup511_exec_register_2026_10_17.md`:248（＋0 件） | ①补正（补登现行真实指纹） |
| `1ce7ab9eb58a` | — | 1 | 141490 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:127（＋0 件） | ①补正（补登现行真实指纹） |
| `1d0053c171ff` | _letter_to_coze_online_v2_2026_09_18.md | 1 | 18611 | `_batch3_execution_receipt_kimi_2026_10_18.md`:229（＋0 件） | ②改指（候选：_letter_to_coze_online_v2_2026_09_18.md·近字节 18611） |
| `1d47720a4199` | — | 1 | 1558 | `_supplement_execution_receipt_kimi_2026_10_18.md`:165（＋0 件） | ①补正（补登现行真实指纹） |
| `1d4962b3755f` | — | 1 | 143345 | `_supplement_execution_receipt_kimi_2026_10_18.md`:350（＋0 件） | ①补正（补登现行真实指纹） |
| `1fabd981724f` | — | 1 | 16036 | `_supplement_execution_receipt_kimi_2026_10_18.md`:263（＋0 件） | ①补正（补登现行真实指纹） |
| `1ff19afefb5b` | — | 1 | 66339 | `_supplement_execution_receipt_kimi_2026_10_18.md`:99（＋0 件） | ①补正（补登现行真实指纹） |
| `201eb40b2352` | — | 1 | 11589 | `_supplement_execution_receipt_kimi_2026_10_18.md`:334（＋0 件） | ①补正（补登现行真实指纹） |
| `20288ce8af1a` | — | 1 | 8017 | `_supplement_execution_receipt_kimi_2026_10_18.md`:82（＋0 件） | ①补正（补登现行真实指纹） |
| `2050a43a475d` | — | 1 | 4242 | `_cleanup511_exec_register_2026_10_17.md`:330（＋0 件） | ①补正（补登现行真实指纹） |
| `2084e09cf750` | — | 1 | 35237 | `_cleanup_noise_register_2026_10_21.md`:112（＋0 件） | ①补正（补登现行真实指纹） |
| `2124536e1f71` | _questionnaire_cards_intake_register_supplem | 1 | 116476 | `_batch3_execution_receipt_kimi_2026_10_18.md`:688（＋0 件） | ②改指（候选：results___questionnaire_cards_intake_register_supplement_4_2026_10_10.md·近字节 116508） |
| `213dc3a9cdfc` | — | 1 | 2086 | `_cleanup511_exec_register_2026_10_17.md`:194（＋0 件） | ①补正（补登现行真实指纹） |
| `2154f6321f18` | — | 1 | 1554 | `_cleanup511_exec_register_2026_10_17.md`:56（＋0 件） | ①补正（补登现行真实指纹） |
| `21a0aab1c3e4` | — | 1 | 2440 | `_batch3_execution_receipt_kimi_2026_10_18.md`:260（＋0 件） | ①补正（补登现行真实指纹） |
| `21ffca2f540f` | — | 1 | 612511 | `_supplement_execution_receipt_kimi_2026_10_18.md`:282（＋0 件） | ①补正（补登现行真实指纹） |
| `2214e735c7d6` | P_F_D1_FULL_REPORT_2026_09_15.md | 1 | 16011 | `_batch3_execution_receipt_kimi_2026_10_18.md`:459（＋0 件） | ②改指（候选：docs__V3X__P_F_D1_FULL_REPORT_2026_09_15.md·近字节 16013） |
| `2242eaa14d30` | — | 1 | 1409 | `_cleanup511_exec_register_2026_10_17.md`:433（＋0 件） | ①补正（补登现行真实指纹） |
| `22f3c6798d2b` | LETTER_TO_TRAE_2026_09_11.md | 1 | 22856 | `_batch3_execution_receipt_kimi_2026_10_18.md`:499（＋0 件） | ②改指（候选：results___archive_2026_09_20__LETTER_TO_TRAE_2026_09_11.md·近字节 22820） |
| `2315c626e486` | — | 1 | 2309 | `_supplement_execution_receipt_kimi_2026_10_18.md`:209（＋0 件） | ①补正（补登现行真实指纹） |
| `23217908421f` | _v3_s_phrasetemplate_prereg_v1_2026_09_27.md | 1 | 33932 | `_supplement_execution_receipt_kimi_2026_10_18.md`:323（＋0 件） | ②改指（候选：_v3_s_phrasetemplate_prereg_v1_2026_09_27.md·近字节 33932） |
| `233b8d8364ce` | — | 1 | 17483 | `_batch3_execution_receipt_kimi_2026_10_18.md`:427（＋0 件） | ①补正（补登现行真实指纹） |
| `234a79c841bd` | — | 1 | 2516 | `_cleanup511_exec_register_2026_10_17.md`:352（＋0 件） | ①补正（补登现行真实指纹） |
| `239ff51f1523` | — | 1 | 95036 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:211（＋0 件） | ①补正（补登现行真实指纹） |
| `23b1ac0af9e5` | _kd_resolvability_and_optional_experiments_2 | 1 | 70328 | `_supplement_execution_receipt_kimi_2026_10_18.md`:378（＋0 件） | ②改指（候选：_kd_resolvability_and_optional_experiments_2026_10_09.md·近字节 70328） |
| `2459e1b1ffef` | _e50_c1.md | 1 | 15391 | `_fake_verdict_reverify_sixitem_ledger_2026_09_30.md`:162（＋0 件） | ①补正（补登现行真实指纹） |
| `249cc004cd0a` | — | 1 | 4166 | `_cleanup511_exec_register_2026_10_17.md`:391（＋0 件） | ①补正（补登现行真实指纹） |
| `24e1969b5e45` | — | 1 | 2066 | `_supplement_execution_receipt_kimi_2026_10_18.md`:256（＋0 件） | ①补正（补登现行真实指纹） |
| `25477700de0f` | — | 1 | 2765 | `_batch3_execution_receipt_kimi_2026_10_18.md`:236（＋0 件） | ①补正（补登现行真实指纹） |
| `255fa4040c80` | — | 1 | 2550 | `_supplement_execution_receipt_kimi_2026_10_18.md`:108（＋0 件） | ①补正（补登现行真实指纹） |
| `25aeb4c13a66` | _e50_c2.md | 1 | 17220 | `_fake_verdict_reverify_sixitem_ledger_2026_09_30.md`:163（＋0 件） | ①补正（补登现行真实指纹） |
| `25af9ef9009c` | — | 1 | 4319 | `_cleanup511_exec_register_2026_10_17.md`:279（＋0 件） | ①补正（补登现行真实指纹） |
| `25e8ac8397a0` | — | 1 | 2242 | `_batch3_execution_receipt_kimi_2026_10_18.md`:264（＋0 件） | ①补正（补登现行真实指纹） |
| `2601583827b6` | — | 1 | 29639 | `_cleanup511_exec_register_2026_10_17.md`:139（＋0 件） | ①补正（补登现行真实指纹） |
| `26880a8b6ea3` | — | 1 | 2094 | `_cleanup511_exec_register_2026_10_17.md`:145（＋0 件） | ①补正（补登现行真实指纹） |
| `26bfd840f88d` | scout3_findings.md | 1 | 10193 | `_cleanup511_exec_register_2026_10_17.md`:400（＋0 件） | ①补正（补登现行真实指纹） |
| `270d620036a1` | — | 1 | 2248 | `_supplement_execution_receipt_kimi_2026_10_18.md`:100（＋0 件） | ①补正（补登现行真实指纹） |
| `27778065e3a6` | — | 1 | 1191 | `_cleanup511_exec_register_2026_10_17.md`:449（＋0 件） | ①补正（补登现行真实指纹） |
| `27af641910d2` | _v4_group_b_explore_subs_integration_2026_09 | 1 | 20534 | `_batch3_execution_receipt_kimi_2026_10_18.md`:842（＋0 件） | ②改指（候选：_v4_group_b_explore_subs_integration_2026_09_22.md·近字节 20532） |
| `284a0f51bfe4` | — | 1 | 9697098 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:137（＋0 件） | ①补正（补登现行真实指纹） |
| `28bbcff53e5d` | — | 1 | 6737 | `_supplement_execution_receipt_kimi_2026_10_18.md`:237（＋0 件） | ①补正（补登现行真实指纹） |
| `28dfe052933b` | — | 1 | 2579 | `_supplement_execution_receipt_kimi_2026_10_18.md`:136（＋0 件） | ①补正（补登现行真实指纹） |
| `28f99be89b44` | — | 1 | 7668 | `_supplement_execution_receipt_kimi_2026_10_18.md`:332（＋0 件） | ①补正（补登现行真实指纹） |
| `299849cc9149` | _ftfb_v3_pass2_audit_2026_09_18_corrected.md | 1 | 28581 | `_batch3_execution_receipt_kimi_2026_10_18.md`:586（＋0 件） | ②改指（候选：_ftfb_v3_pass2_audit_2026_09_18_corrected.md·近字节 28579） |
| `29c5792a72ba` | — | 1 | 6476 | `_supplement_execution_receipt_kimi_2026_10_18.md`:88（＋0 件） | ①补正（补登现行真实指纹） |
| `29c9850b9b0a` | — | 1 | 2105 | `_cleanup511_exec_register_2026_10_17.md`:181（＋0 件） | ①补正（补登现行真实指纹） |
| `2a3fe852c97c` | — | 1 | 1638 | `_supplement_execution_receipt_kimi_2026_10_18.md`:119（＋0 件） | ①补正（补登现行真实指纹） |
| `2a7b18194ed6` | — | 1 | 1367 | `_cleanup511_exec_register_2026_10_17.md`:420（＋0 件） | ①补正（补登现行真实指纹） |
| `2ad32aca80a6` | — | 1 | 1322 | `_cleanup511_exec_register_2026_10_17.md`:366（＋0 件） | ①补正（补登现行真实指纹） |
| `2b36d3874b4d` | _v4_closeout_bulk_reorganize_register_2026_1 | 1 | 197287 | `_batch3_execution_receipt_kimi_2026_10_18.md`:835（＋0 件） | ②改指（候选：_v4_closeout_bulk_reorganize_register_2026_10_12.md·近字节 197283） |
| `2b74debe23ce` | — | 1 | 7071 | `_cleanup511_exec_register_2026_10_17.md`:212（＋0 件） | ①补正（补登现行真实指纹） |
| `2bb3b8bd9fc3` | — | 1 | 48097 | `_cleanup511_exec_register_2026_10_17.md`:419（＋0 件） | ①补正（补登现行真实指纹） |
| `2bb4721c475b` | — | 1 | 1820 | `_cleanup511_exec_register_2026_10_17.md`:347（＋0 件） | ①补正（补登现行真实指纹） |
| `2be519ee8f4b` | — | 1 | 1666 | `_cleanup511_exec_register_2026_10_17.md`:443（＋0 件） | ①补正（补登现行真实指纹） |
| `2c005210d113` | — | 1 | 1270 | `_supplement_execution_receipt_kimi_2026_10_18.md`:296（＋0 件） | ①补正（补登现行真实指纹） |
| `2d8997a9ec6b` | — | 1 | 1484 | `_supplement_execution_receipt_kimi_2026_10_18.md`:120（＋0 件） | ①补正（补登现行真实指纹） |
| `2e179f2d1d4b` | — | 1 | 2714 | `_cleanup511_exec_register_2026_10_17.md`:231（＋0 件） | ①补正（补登现行真实指纹） |
| `2e6088301882` | _skill_call_surface_probe_supplement_b_2026_ | 1 | 17725 | `_skill_reference_update_and_user_surface_survey_2026_09_30.md`:522（＋0 件） | ①补正（补登现行真实指纹） |
| `2e9050c3f167` | _round23_26_threshold_review_effect_register | 1 | 47297 | `_supplement_execution_receipt_kimi_2026_10_18.md`:305（＋0 件） | ②改指（候选：_round23_26_threshold_review_effect_register_2026_10_10.md·近字节 47297） |
| `2e993b461a14` | _pi_card_answers_register_2026_10_17_v67.md | 1 | 45753 | `_pi_card_answers_register_2026_10_17_v66_append2.md`:27（＋0 件） | ②改指（候选：_pi_card_answers_register_2026_10_17_v67.md·近字节 46839） |
| `2eb41ec8d3e2` | — | 1 | 5784 | `_supplement_execution_receipt_kimi_2026_10_18.md`:241（＋0 件） | ①补正（补登现行真实指纹） |
| `2f4ce8ab83ad` | — | 1 | 1247 | `_batch3_execution_receipt_kimi_2026_10_18.md`:276（＋0 件） | ①补正（补登现行真实指纹） |
| `2f79df3622e7` | _kickoff_decisions_register_2026_10_08.md | 1 | 16412 | `_batch3_execution_receipt_kimi_2026_10_18.md`:362（＋0 件） | ②改指（候选：_kickoff_decisions_register_2026_10_08.md·近字节 16388） |
| `2f8b5a27e179` | — | 1 | 1182 | `_cleanup511_exec_register_2026_10_17.md`:167（＋0 件） | ①补正（补登现行真实指纹） |
| `2f9d6c9b7a38` | — | 1 | 3045 | `_supplement_execution_receipt_kimi_2026_10_18.md`:157（＋0 件） | ①补正（补登现行真实指纹） |
| `2fa2efeb632c` | — | 1 | 17772 | `_batch3_execution_receipt_kimi_2026_10_18.md`:272（＋0 件） | ①补正（补登现行真实指纹） |
| `2fc73d644f55` | — | 1 | 11116 | `_supplement_execution_receipt_kimi_2026_10_18.md`:243（＋0 件） | ①补正（补登现行真实指纹） |
| `2ffd86d567cb` | — | 1 | 1716 | `_cleanup511_exec_register_2026_10_17.md`:396（＋0 件） | ①补正（补登现行真实指纹） |
| `3053d2e576e5` | — | 1 | 1391 | `_supplement_execution_receipt_kimi_2026_10_18.md`:166（＋0 件） | ①补正（补登现行真实指纹） |
| `30a251208318` | _t1_prereg_revision_temp_axis_exp2_2026_10_0 | 1 | 34217 | `_supplement_execution_receipt_kimi_2026_10_18.md`:311（＋0 件） | ②改指（候选：_t1_prereg_revision_temp_axis_exp2_2026_10_09.md·近字节 34217） |
| `30c65db0ca1b` | — | 1 | 3416 | `_batch3_execution_receipt_kimi_2026_10_18.md`:252（＋0 件） | ①补正（补登现行真实指纹） |
| `312330ce3cef` | LETTER_TO_EXTERNAL_ADVISOR_2026_09_18_FINAL. | 1 | 10586 | `_batch3_execution_receipt_kimi_2026_10_18.md`:221（＋0 件） | ②改指（候选：LETTER_TO_EXTERNAL_ADVISOR_2026_09_18_FINAL.md·近字节 10586） |
| `31344dc9a77d` | _kd_writing_convention_guidance_2026_10_09.m | 1 | 20179 | `_supplement_execution_receipt_kimi_2026_10_18.md`:379（＋0 件） | ②改指（候选：_kd_writing_convention_guidance_2026_10_09.md·近字节 20179） |
| `317fce89d2ca` | — | 1 | 18023 | `_supplement_execution_receipt_kimi_2026_10_18.md`:289（＋0 件） | ①补正（补登现行真实指纹） |
| `31c64a39301d` | — | 1 | 5147 | `_cleanup511_exec_register_2026_10_17.md`:76（＋0 件） | ①补正（补登现行真实指纹） |
| `31cde3f8fec0` | _v4_trae_remaining_audit_2026_09_28.md | 1 | 39697 | `_batch3_execution_receipt_kimi_2026_10_18.md`:849（＋0 件） | ②改指（候选：_v4_trae_remaining_audit_2026_09_28.md·近字节 39681） |
| `31d60405eed5` | — | 1 | 6666 | `_supplement_execution_receipt_kimi_2026_10_18.md`:331（＋0 件） | ①补正（补登现行真实指纹） |
| `322ea30656b1` | — | 1 | 2578 | `_supplement_execution_receipt_kimi_2026_10_18.md`:110（＋0 件） | ①补正（补登现行真实指纹） |
| `32e1e35b0480` | — | 1 | 194993 | `_cleanup511_exec_register_2026_10_17.md`:159（＋0 件） | ①补正（补登现行真实指纹） |
| `32e7b06a0de3` | — | 1 | 120810 | `_supplement_execution_receipt_kimi_2026_10_18.md`:303（＋0 件） | ①补正（补登现行真实指纹） |
| `33bf3cdbe7df` | — | 1 | 4234 | `_cleanup511_exec_register_2026_10_17.md`:438（＋0 件） | ①补正（补登现行真实指纹） |
| `340ee68b89a3` | LETTER_TO_TRAE_REVIEW_2026_09_16.md | 1 | 12676 | `_batch3_execution_receipt_kimi_2026_10_18.md`:500（＋0 件） | ②改指（候选：results___archive_2026_09_20__LETTER_TO_TRAE_REVIEW_2026_09_16.md·近字节 12671） |
| `347c767a718f` | — | 1 | 1890 | `_supplement_execution_receipt_kimi_2026_10_18.md`:219（＋0 件） | ①补正（补登现行真实指纹） |
| `3488d16f3efe` | — | 1 | 1598 | `_cleanup511_exec_register_2026_10_17.md`:282（＋0 件） | ①补正（补登现行真实指纹） |
| `349f2d203b96` | — | 1 | 3023 | `_cleanup511_exec_register_2026_10_17.md`:405（＋0 件） | ①补正（补登现行真实指纹） |
| `34bc36b5d744` | scout6_findings.md | 1 | 5343 | `_cleanup511_exec_register_2026_10_17.md`:406（＋0 件） | ①补正（补登现行真实指纹） |
| `34e6d27cd542` | — | 1 | 2090 | `_cleanup511_exec_register_2026_10_17.md`:136（＋0 件） | ①补正（补登现行真实指纹） |
| `351d208cc3fd` | — | 1 | 3726 | `_cleanup511_exec_register_2026_10_17.md`:79（＋0 件） | ①补正（补登现行真实指纹） |
| `359ca8e92cbf` | _v5_b12_verify_pack_q1_q3_q4_2026_09_29.md | 1 | 33813 | `_batch3_execution_receipt_kimi_2026_10_18.md`:850（＋0 件） | ②改指（候选：_v5_b12_verify_pack_q1_q3_q4_2026_09_29.md·近字节 33803） |
| `35d662b2d9a6` | — | 1 | 5044 | `_cleanup511_exec_register_2026_10_17.md`:187（＋0 件） | ①补正（补登现行真实指纹） |
| `35e266592819` | — | 1 | 1746 | `_cleanup511_exec_register_2026_10_17.md`:368（＋0 件） | ①补正（补登现行真实指纹） |
| `373e10955bf2` | — | 1 | 2947 | `_cleanup511_exec_register_2026_10_17.md`:149（＋0 件） | ①补正（补登现行真实指纹） |
| `37497030b73b` | _questionnaire_cards_intake_register_2026_10 | 1 | 442333 | `_batch3_execution_receipt_kimi_2026_10_18.md`:678（＋0 件） | ②改指（候选：results___questionnaire_cards_intake_register_2026_10_09.md·近字节 442352） |
| `374db5178ad9` | scout5_findings.md | 1 | 1016 | `_cleanup511_exec_register_2026_10_17.md`:404（＋0 件） | ①补正（补登现行真实指纹） |
| `37d73d3704a3` | — | 1 | 18086 | `_pa_harness_anchor_value_update_v3_lock_register_2026_10_16.md`:129（＋0 件） | ①补正（补登现行真实指纹） |
| `37dcb976fef4` | — | 1 | 1158 | `_supplement_execution_receipt_kimi_2026_10_18.md`:288（＋0 件） | ①补正（补登现行真实指纹） |
| `3915f60c6d9b` | _v3_v4_achievements_inventory_3dir_addendum_ | 1 | 23162 | `_batch3_execution_receipt_kimi_2026_10_18.md`:826（＋0 件） | ②改指（候选：_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md·近字节 23152） |
| `39bc47e46948` | _pre_execution_report_kimi_2026_10_18.md | 1 | 6971 | `_batch3_execution_receipt_kimi_2026_10_18.md`:372（＋0 件） | ②改指（候选：_pre_execution_report_kimi_2026_10_18.md·近字节 6969） |
| `3a7d4aa4ee7c` | — | 1 | 4212 | `_cleanup511_exec_register_2026_10_17.md`:116（＋0 件） | ①补正（补登现行真实指纹） |
| `3aacc03484d9` | — | 1 | 3009 | `_supplement_execution_receipt_kimi_2026_10_18.md`:64（＋0 件） | ①补正（补登现行真实指纹） |
| `3ae01762d0e9` | — | 1 | 24228 | `_cleanup511_exec_register_2026_10_17.md`:458（＋0 件） | ①补正（补登现行真实指纹） |
| `3ae72acad66e` | — | 1 | 12975 | `_supplement_execution_receipt_kimi_2026_10_18.md`:347（＋0 件） | ①补正（补登现行真实指纹） |
| `3b07efe2765d` | — | 1 | 17263 | `_cleanup511_exec_register_2026_10_17.md`:415（＋0 件） | ①补正（补登现行真实指纹） |
| `3b1d572c143e` | — | 1 | 11522 | `_batch3_execution_receipt_kimi_2026_10_18.md`:258（＋0 件） | ①补正（补登现行真实指纹） |
| `3b667b0acf62` | — | 1 | 52165 | `_batch3_execution_receipt_kimi_2026_10_18.md`:518（＋0 件） | ①补正（补登现行真实指纹） |
| `3cafa1153b07` | — | 1 | 5650 | `_cleanup511_exec_register_2026_10_17.md`:283（＋0 件） | ①补正（补登现行真实指纹） |
| `3cf751a68ced` | — | 1 | 1297 | `_cleanup511_exec_register_2026_10_17.md`:349（＋0 件） | ①补正（补登现行真实指纹） |
| `3d694531b9da` | — | 1 | 10266 | `_cleanup511_exec_register_2026_10_17.md`:296（＋0 件） | ①补正（补登现行真实指纹） |
| `3e41a2c28b17` | — | 1 | 7173 | `_supplement_execution_receipt_kimi_2026_10_18.md`:250（＋0 件） | ①补正（补登现行真实指纹） |
| `3e9c0f4cc072` | — | 1 | 34615 | `_cleanup511_exec_register_2026_10_17.md`:115（＋0 件） | ①补正（补登现行真实指纹） |
| `3f1a88c1b7f6` | — | 1 | 2136 | `_cleanup511_exec_register_2026_10_17.md`:440（＋0 件） | ①补正（补登现行真实指纹） |
| `3fa2aac04729` | — | 1 | 1636 | `_supplement_execution_receipt_kimi_2026_10_18.md`:150（＋0 件） | ①补正（补登现行真实指纹） |
| `3fb1611197c8` | — | 1 | 4992 | `_batch3_execution_receipt_kimi_2026_10_18.md`:250（＋0 件） | ①补正（补登现行真实指纹） |
| `4045112e6166` | — | 1 | 1909 | `_supplement_execution_receipt_kimi_2026_10_18.md`:179（＋0 件） | ①补正（补登现行真实指纹） |
| `408508b1adc9` | — | 1 | 9819 | `_supplement_execution_receipt_kimi_2026_10_18.md`:278（＋0 件） | ①补正（补登现行真实指纹） |
| `41a82bab4d83` | — | 1 | 1990 | `_cleanup511_exec_register_2026_10_17.md`:367（＋0 件） | ①补正（补登现行真实指纹） |
| `41be5e82f978` | — | 1 | 2246 | `_cleanup511_exec_register_2026_10_17.md`:118（＋0 件） | ①补正（补登现行真实指纹） |
| `41bf57479a30` | — | 1 | 1358 | `_cleanup511_exec_register_2026_10_17.md`:235（＋0 件） | ①补正（补登现行真实指纹） |
| `429a95eba06d` | — | 1 | 1403 | `_cleanup511_exec_register_2026_10_17.md`:165（＋0 件） | ①补正（补登现行真实指纹） |
| `42c95e41e08a` | — | 1 | 4900 | `_supplement_execution_receipt_kimi_2026_10_18.md`:271（＋0 件） | ①补正（补登现行真实指纹） |
| `43af2e0ec6e4` | — | 1 | 9311 | `_cleanup511_exec_register_2026_10_17.md`:275（＋0 件） | ①补正（补登现行真实指纹） |
| `43f4077e993e` | _v4_tmp_cleanup_2026_09_28.md | 1 | 5131 | `_supplement_execution_receipt_kimi_2026_10_18.md`:349（＋0 件） | ②改指（候选：_v4_tmp_cleanup_2026_09_28.md·近字节 5131） |
| `4422e0a2032d` | _v3_recheck_prereg_v1p1_2026_09_27.md | 1 | 42978 | `_batch3_execution_receipt_kimi_2026_10_18.md`:822（＋0 件） | ②改指（候选：_v3_recheck_prereg_v1p1_2026_09_27.md·近字节 42970） |
| `4459d3940d6c` | — | 1 | 1314 | `_cleanup511_exec_register_2026_10_17.md`:141（＋0 件） | ①补正（补登现行真实指纹） |
| `44afda519df3` | — | 1 | 634458 | `_supplement_execution_receipt_kimi_2026_10_18.md`:131（＋0 件） | ①补正（补登现行真实指纹） |
| `45185158a8f0` | — | 1 | 174424 | `_supplement_execution_receipt_kimi_2026_10_18.md`:252（＋0 件） | ①补正（补登现行真实指纹） |
| `457ddd94904d` | — | 1 | 2657 | `_cleanup511_exec_register_2026_10_17.md`:82（＋0 件） | ①补正（补登现行真实指纹） |
| `468f256ee779` | — | 1 | 1897 | `_cleanup511_exec_register_2026_10_17.md`:422（＋0 件） | ①补正（补登现行真实指纹） |
| `469aaafcf3e6` | — | 1 | 3055 | `_cleanup511_exec_register_2026_10_17.md`:171（＋0 件） | ①补正（补登现行真实指纹） |
| `4700ce30ca92` | — | 1 | 1114 | `_cleanup511_exec_register_2026_10_17.md`:112（＋0 件） | ①补正（补登现行真实指纹） |
| `470437c653de` | — | 1 | 57153 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:207（＋0 件） | ①补正（补登现行真实指纹） |
| `477a5cc75f25` | ftfb_pass1_background_methodology_audit_2026 | 1 | 8259 | `_batch3_execution_receipt_kimi_2026_10_18.md`:512（＋0 件） | ②改指（候选：results___archive_2026_09_20__ftfb_pass1_background_methodology_audit_2026_09_17.md·近字节 8257） |
| `48349dc56490` | — | 1 | 44364 | `_kd_s3b1_verdict_2026_10_17.md`:346（＋0 件） | ①补正（补登现行真实指纹） |
| `4914e95f523e` | — | 1 | 4400 | `_cleanup511_exec_register_2026_10_17.md`:392（＋0 件） | ①补正（补登现行真实指纹） |
| `493284935015` | — | 1 | 1682 | `_cleanup511_exec_register_2026_10_17.md`:105（＋0 件） | ①补正（补登现行真实指纹） |
| `4968f1f018f1` | — | 1 | 39462 | `_cleanup511_exec_register_2026_10_17.md`:213（＋0 件） | ①补正（补登现行真实指纹） |
| `49ae49495cbd` | — | 1 | 88584 | `_supplement_execution_receipt_kimi_2026_10_18.md`:298（＋0 件） | ①补正（补登现行真实指纹） |
| `49fefa14c065` | — | 1 | 60285 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:208（＋0 件） | ①补正（补登现行真实指纹） |
| `4ac0b69ce6e0` | — | 1 | 21580 | `_cleanup511_exec_register_2026_10_17.md`:156（＋0 件） | ①补正（补登现行真实指纹） |
| `4b40124a5101` | — | 1 | 2048 | `_cleanup511_exec_register_2026_10_17.md`:447（＋0 件） | ①补正（补登现行真实指纹） |
| `4b52d3a6d7fc` | — | 1 | 3958 | `_supplement_execution_receipt_kimi_2026_10_18.md`:155（＋0 件） | ①补正（补登现行真实指纹） |
| `4bc833353076` | — | 1 | 11036 | `_supplement_execution_receipt_kimi_2026_10_18.md`:95（＋0 件） | ①补正（补登现行真实指纹） |
| `4bd95f8cfb25` | — | 1 | 94355 | `_cleanup511_exec_register_2026_10_17.md`:371（＋0 件） | ①补正（补登现行真实指纹） |
| `4c0817f40091` | — | 1 | 16485 | `_cleanup511_exec_register_2026_10_17.md`:40（＋0 件） | ①补正（补登现行真实指纹） |
| `4c10652a2f77` | — | 1 | 1062 | `_cleanup511_exec_register_2026_10_17.md`:344（＋0 件） | ①补正（补登现行真实指纹） |
| `4c4f4708991a` | — | 1 | 1368 | `_cleanup511_exec_register_2026_10_17.md`:311（＋0 件） | ①补正（补登现行真实指纹） |
| `4c58096971b5` | — | 1 | 2262 | `_cleanup511_exec_register_2026_10_17.md`:87（＋0 件） | ①补正（补登现行真实指纹） |
| `4c6eb02b13cf` | — | 1 | 14722 | `_supplement_execution_receipt_kimi_2026_10_18.md`:335（＋0 件） | ①补正（补登现行真实指纹） |
| `4c7ff94163a0` | — | 1 | 21338 | `_supplement_execution_receipt_kimi_2026_10_18.md`:244（＋0 件） | ①补正（补登现行真实指纹） |
| `4cc8cb5177a7` | — | 1 | 3099 | `_cleanup511_exec_register_2026_10_17.md`:448（＋0 件） | ①补正（补登现行真实指纹） |
| `4cccd496e23b` | — | 1 | 36831 | `_cleanup511_exec_register_2026_10_17.md`:463（＋0 件） | ①补正（补登现行真实指纹） |
| `4cf585681505` | — | 1 | 11848 | `_cleanup511_exec_register_2026_10_17.md`:452（＋0 件） | ①补正（补登现行真实指纹） |
| `4d56cf50ee47` | — | 1 | 8701 | `_batch3_execution_receipt_kimi_2026_10_18.md`:431（＋0 件） | ①补正（补登现行真实指纹） |
| `4d6c75dc083c` | — | 1 | 6134 | `_batch3_execution_receipt_kimi_2026_10_18.md`:253（＋0 件） | ①补正（补登现行真实指纹） |
| `4d960834acca` | — | 1 | 17158 | `_batch3_execution_receipt_kimi_2026_10_18.md`:259（＋0 件） | ①补正（补登现行真实指纹） |
| `4dc75e4985e5` | TRAE_FIX_RECEIPT_2026_09_18.md | 1 | 4784 | `_batch3_execution_receipt_kimi_2026_10_18.md`:225（＋0 件） | ②改指（候选：TRAE_FIX_RECEIPT_2026_09_18.md·近字节 4784） |
| `4dc94009e2da` | — | 1 | 5699 | `_supplement_execution_receipt_kimi_2026_10_18.md`:254（＋0 件） | ①补正（补登现行真实指纹） |
| `4e31f9167442` | — | 1 | 25055 | `_batch3_execution_receipt_kimi_2026_10_18.md`:882（＋0 件） | ①补正（补登现行真实指纹） |
| `4e4933dce696` | — | 1 | 2084 | `_cleanup511_exec_register_2026_10_17.md`:196（＋0 件） | ①补正（补登现行真实指纹） |
| `4e8ad6650b28` | — | 1 | 16097 | `_supplement_execution_receipt_kimi_2026_10_18.md`:264（＋0 件） | ①补正（补登现行真实指纹） |
| `4eac36c11811` | — | 1 | 1054 | `_cleanup511_exec_register_2026_10_17.md`:251（＋0 件） | ①补正（补登现行真实指纹） |
| `4efb34e71dcc` | — | 1 | 20714 | `_cleanup511_exec_register_2026_10_17.md`:43（＋0 件） | ①补正（补登现行真实指纹） |
| `5059fdc35f57` | — | 1 | 1508 | `_batch3_execution_receipt_kimi_2026_10_18.md`:227（＋0 件） | ①补正（补登现行真实指纹） |
| `50ac53ae50b3` | — | 1 | 37481 | `_cleanup511_exec_register_2026_10_17.md`:255（＋0 件） | ①补正（补登现行真实指纹） |
| `50b2c15085d4` | — | 1 | 4226 | `_cleanup511_exec_register_2026_10_17.md`:75（＋0 件） | ①补正（补登现行真实指纹） |
| `514dd4317f7c` | — | 1 | 22695 | `_u_hface15_18889_lock_register_2026_10_17.md`:179（＋0 件） | ①补正（补登现行真实指纹） |
| `52036f77995e` | — | 1 | 1282 | `_supplement_execution_receipt_kimi_2026_10_18.md`:164（＋0 件） | ①补正（补登现行真实指纹） |
| `523906bcc978` | — | 1 | 454307 | `_batch3_execution_receipt_kimi_2026_10_18.md`:226（＋0 件） | ①补正（补登现行真实指纹） |
| `5261971aacbe` | — | 1 | 10820 | `_cleanup511_exec_register_2026_10_17.md`:135（＋0 件） | ①补正（补登现行真实指纹） |
| `530d054998a4` | — | 1 | 2411 | `_supplement_execution_receipt_kimi_2026_10_18.md`:183（＋0 件） | ①补正（补登现行真实指纹） |
| `53a1afce2093` | — | 1 | 9470 | `_cleanup511_exec_register_2026_10_17.md`:307（＋0 件） | ①补正（补登现行真实指纹） |
| `53a5fafe3063` | — | 1 | 78250 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:201（＋0 件） | ①补正（补登现行真实指纹） |
| `53fe4853a3a3` | — | 1 | 2802 | `_cleanup511_exec_register_2026_10_17.md`:245（＋0 件） | ①补正（补登现行真实指纹） |
| `54272d42f5c9` | _v176_v179_adoption_effect_2026_10_21.md | 1 | 11639 | `_ghost_reference_register_2026_10_21.md`:171（＋0 件） | ①补正（补登现行真实指纹） |
| `5475398bceb3` | — | 1 | 2763 | `_supplement_execution_receipt_kimi_2026_10_18.md`:206（＋0 件） | ①补正（补登现行真实指纹） |
| `554ed49adac1` | — | 1 | 2062 | `_v4_day_inventory_2026_09_27.md`:236（＋0 件） | ①补正（补登现行真实指纹） |
| `55d7f6a1e428` | — | 1 | 1014 | `_supplement_execution_receipt_kimi_2026_10_18.md`:188（＋0 件） | ①补正（补登现行真实指纹） |
| `5657b35ebbef` | _v3r1_threshold_path4_draft_2026_10_10.md | 1 | 39077 | `_supplement_execution_receipt_kimi_2026_10_18.md`:325（＋0 件） | ②改指（候选：_v3r1_threshold_path4_draft_2026_10_10.md·近字节 39077） |
| `573ee1005d85` | — | 1 | 1276 | `_cleanup511_exec_register_2026_10_17.md`:111（＋0 件） | ①补正（补登现行真实指纹） |
| `584e3e4151b6` | — | 1 | 2300 | `_cleanup511_exec_register_2026_10_17.md`:81（＋0 件） | ①补正（补登现行真实指纹） |
| `5870416973b6` | — | 1 | 12381 | `_cleanup511_exec_register_2026_10_17.md`:324（＋0 件） | ①补正（补登现行真实指纹） |
| `58ce60c11ed9` | — | 1 | 6528 | `_supplement_execution_receipt_kimi_2026_10_18.md`:257（＋0 件） | ①补正（补登现行真实指纹） |
| `590d63384772` | — | 1 | 3501 | `_supplement_execution_receipt_kimi_2026_10_18.md`:122（＋0 件） | ①补正（补登现行真实指纹） |
| `59c30f342362` | — | 1 | 2839 | `_cleanup511_exec_register_2026_10_17.md`:357（＋0 件） | ①补正（补登现行真实指纹） |
| `5a54e8f799f6` | — | 1 | 2292 | `_supplement_execution_receipt_kimi_2026_10_18.md`:137（＋0 件） | ①补正（补登现行真实指纹） |
| `5ab230db4550` | — | 1 | 2712 | `_supplement_execution_receipt_kimi_2026_10_18.md`:223（＋0 件） | ①补正（补登现行真实指纹） |
| `5ac7a7dcce75` | — | 1 | 2810 | `_cleanup511_exec_register_2026_10_17.md`:273（＋0 件） | ①补正（补登现行真实指纹） |
| `5b233e1e021d` | TRAE_DAILY_AUDIT_LETTER_2026_09_18.md | 1 | 11575 | `_batch3_execution_receipt_kimi_2026_10_18.md`:224（＋0 件） | ②改指（候选：TRAE_DAILY_AUDIT_LETTER_2026_09_18.md·近字节 11575） |
| `5b4f2f24fcb0` | — | 1 | 19907 | `_batch3_execution_receipt_kimi_2026_10_18.md`:399（＋0 件） | ①补正（补登现行真实指纹） |
| `5b70135c5b23` | — | 1 | 6845 | `_cleanup511_exec_register_2026_10_17.md`:117（＋0 件） | ①补正（补登现行真实指纹） |
| `5b88cdfd0ea8` | DEPOSON_EMBEDDING_6WAY_THEORY_V0_2026_09_10. | 1 | 22448 | `_batch3_execution_receipt_kimi_2026_10_18.md`:444（＋0 件） | ②改指（候选：DEPOSON_EMBEDDING_6WAY_THEORY_V0_2026_09_10.md·近字节 22442） |
| `5bb21c0cdee1` | _letter_to_trae_code_2026_09_17_final.md | 1 | 10722 | `_batch3_execution_receipt_kimi_2026_10_18.md`:511（＋0 件） | ②改指（候选：results___archive_2026_09_20___letter_to_trae_code_2026_09_17_final.md·近字节 10702） |
| `5bde2e624c81` | — | 1 | 48655 | `_batch3_execution_receipt_kimi_2026_10_18.md`:393（＋0 件） | ①补正（补登现行真实指纹） |
| `5c28c166bb78` | — | 1 | 5974 | `_cleanup511_exec_register_2026_10_17.md`:377（＋0 件） | ①补正（补登现行真实指纹） |
| `5c92ccdf8cbe` | — | 1 | 33337 | `_cleanup511_exec_register_2026_10_17.md`:247（＋0 件） | ①补正（补登现行真实指纹） |
| `5d36d3e9c355` | — | 1 | 12470 | `_batch3_execution_receipt_kimi_2026_10_18.md`:279（＋0 件） | ①补正（补登现行真实指纹） |
| `5d3950a54d65` | — | 1 | 10412 | `_batch3_execution_receipt_kimi_2026_10_18.md`:422（＋0 件） | ①补正（补登现行真实指纹） |
| `5d76ac24a658` | — | 1 | 16203 | `_cleanup511_exec_register_2026_10_17.md`:312（＋0 件） | ①补正（补登现行真实指纹） |
| `5d9d5bc3b5f6` | — | 1 | 70314 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:200（＋0 件） | ①补正（补登现行真实指纹） |
| `5e2418926cec` | — | 1 | 45546 | `_kd_s3b1_verdict_2026_10_17.md`:346（＋0 件） | ①补正（补登现行真实指纹） |
| `5e25e0431bfc` | — | 1 | 2313 | `_supplement_execution_receipt_kimi_2026_10_18.md`:186（＋0 件） | ①补正（补登现行真实指纹） |
| `5e93b0ac8df4` | _stage_t2_t3.md | 1 | 24619 | `_cleanup511_exec_register_2026_10_17.md`:161（＋0 件） | ①补正（补登现行真实指纹） |
| `5f649d030753` | — | 1 | 291575 | `_batch3_execution_receipt_kimi_2026_10_18.md`:396（＋0 件） | ①补正（补登现行真实指纹） |
| `5f9a7560cac7` | — | 1 | 12831 | `_cleanup511_exec_register_2026_10_17.md`:41（＋0 件） | ①补正（补登现行真实指纹） |
| `5fa9f4bc4bf6` | — | 1 | 2712 | `_batch3_execution_receipt_kimi_2026_10_18.md`:239（＋0 件） | ①补正（补登现行真实指纹） |
| `5fb6c3f2c6d7` | — | 1 | 27221 | `_cleanup511_exec_register_2026_10_17.md`:124（＋0 件） | ①补正（补登现行真实指纹） |
| `5fcbf0934ef7` | _v4_maindir_cleanup_manifest_v2_2026_09_26.m | 1 | 27913 | `_batch3_execution_receipt_kimi_2026_10_18.md`:844（＋0 件） | ②改指（候选：_v4_maindir_cleanup_manifest_v2_2026_09_26.md·近字节 27909） |
| `60f5932e4b0b` | AGENT_TEAM_OPT_V2_2026_09_11.md | 1 | 11843 | `_batch3_execution_receipt_kimi_2026_10_18.md`:435（＋0 件） | ②改指（候选：AGENT_TEAM_OPT_V2_2026_09_11.md·近字节 11835） |
| `610b29d1b70e` | — | 1 | 6514 | `_batch3_execution_receipt_kimi_2026_10_18.md`:270（＋0 件） | ①补正（补登现行真实指纹） |
| `6114b547ae4e` | — | 1 | 1845 | `_cleanup511_exec_register_2026_10_17.md`:180（＋0 件） | ①补正（补登现行真实指纹） |
| `612061e6ed17` | — | 1 | 44275 | `_m08_measured_enumeration_exec_2026_10_16.md`:435（＋0 件） | ①补正（补登现行真实指纹） |
| `612fafeb24ca` | — | 1 | 74681 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:210（＋0 件） | ①补正（补登现行真实指纹） |
| `6147078b74be` | — | 1 | 18152 | `_supplement_execution_receipt_kimi_2026_10_18.md`:274（＋0 件） | ①补正（补登现行真实指纹） |
| `6148a4d56b6c` | — | 1 | 2672 | `_supplement_execution_receipt_kimi_2026_10_18.md`:84（＋0 件） | ①补正（补登现行真实指纹） |
| `61706e9cbcf5` | — | 1 | 20751 | `_batch3_execution_receipt_kimi_2026_10_18.md`:900（＋0 件） | ①补正（补登现行真实指纹） |
| `61910bdb5dc4` | — | 1 | 1444 | `_batch3_execution_receipt_kimi_2026_10_18.md`:256（＋0 件） | ①补正（补登现行真实指纹） |
| `61ef6bff9528` | — | 1 | 20194 | `_supplement_execution_receipt_kimi_2026_10_18.md`:338（＋0 件） | ①补正（补登现行真实指纹） |
| `621c2ed0fa75` | _g10_threshold_closed_domain_judgment_2026_1 | 1 | 55667 | `_supplement_execution_receipt_kimi_2026_10_18.md`:300（＋0 件） | ②改指（候选：_g10_threshold_closed_domain_judgment_2026_10_11.md·近字节 55727） |
| `629042265f54` | — | 1 | 50606 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:198（＋0 件） | ①补正（补登现行真实指纹） |
| `62d7d7c4bee9` | _t1_substrate_gap_precondition_2026_10_01.md | 1 | 22196 | `_supplement_execution_receipt_kimi_2026_10_18.md`:383（＋0 件） | ②改指（候选：_t1_substrate_gap_precondition_2026_10_01.md·近字节 22196） |
| `643d3aea5cc6` | _v5_t1_decisions_register_2026_09_29.md | 1 | 31334 | `_batch3_execution_receipt_kimi_2026_10_18.md`:866（＋0 件） | ②改指（候选：results___v5_t1_decisions_register_2026_09_29.md·近字节 31336） |
| `64505229f954` | — | 1 | 70053 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:262（＋0 件） | ①补正（补登现行真实指纹） |
| `647c8cd706b0` | — | 1 | 3061 | `_cleanup511_exec_register_2026_10_17.md`:389（＋0 件） | ①补正（补登现行真实指纹） |
| `648fa1b4f439` | — | 1 | 19192 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:240（＋0 件） | ①补正（补登现行真实指纹） |
| `649a2a016b24` | — | 1 | 2342 | `_batch3_execution_receipt_kimi_2026_10_18.md`:238（＋0 件） | ①补正（补登现行真实指纹） |
| `64e7163e0d13` | — | 1 | 1990 | `_cleanup511_exec_register_2026_10_17.md`:286（＋0 件） | ①补正（补登现行真实指纹） |
| `656a8483cd18` | — | 1 | 20815 | `_cleanup511_exec_register_2026_10_17.md`:234（＋0 件） | ①补正（补登现行真实指纹） |
| `657123a04df6` | — | 1 | 4106 | `_supplement_execution_receipt_kimi_2026_10_18.md`:172（＋0 件） | ①补正（补登现行真实指纹） |
| `659b7993d403` | — | 1 | 31870 | `_cleanup511_exec_register_2026_10_17.md`:461（＋0 件） | ①补正（补登现行真实指纹） |
| `65abea802cd9` | — | 1 | 1774 | `_cleanup511_exec_register_2026_10_17.md`:230（＋0 件） | ①补正（补登现行真实指纹） |
| `65ba10553f14` | — | 1 | 9082 | `_batch3_execution_receipt_kimi_2026_10_18.md`:430（＋0 件） | ①补正（补登现行真实指纹） |
| `65ca656c2d4f` | — | 1 | 9901 | `_cleanup511_exec_register_2026_10_17.md`:49（＋0 件） | ①补正（补登现行真实指纹） |
| `65d1c0362ff5` | — | 1 | 42807 | `_cleanup511_exec_register_2026_10_17.md`:80（＋0 件） | ①补正（补登现行真实指纹） |
| `6646c592fb32` | — | 1 | 5131 | `_supplement_execution_receipt_kimi_2026_10_18.md`:65（＋0 件） | ①补正（补登现行真实指纹） |
| `66de2e44ee7c` | LETTER_TO_KIMI_GITHUB_UPLOAD_2026_09_18.md | 1 | 13306 | `_batch3_execution_receipt_kimi_2026_10_18.md`:498（＋0 件） | ②改指（候选：results___archive_2026_09_20__LETTER_TO_KIMI_GITHUB_UPLOAD_2026_09_18.md·近字节 13295） |
| `674efba35991` | — | 1 | 21119 | `_cleanup511_exec_register_2026_10_17.md`:310（＋0 件） | ①补正（补登现行真实指纹） |
| `679eb741de41` | _letter_to_kimi_upload_requirements_2026_09_ | 1 | 22611 | `_batch3_execution_receipt_kimi_2026_10_18.md`:510（＋0 件） | ②改指（候选：results___archive_2026_09_20___letter_to_kimi_upload_requirements_2026_09_18.md·近字节 22591） |
| `67ef0e56fcbf` | — | 1 | 67589 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:199（＋0 件） | ①补正（补登现行真实指纹） |
| `68251f1418b1` | — | 1 | 2256 | `_cleanup511_exec_register_2026_10_17.md`:243（＋0 件） | ①补正（补登现行真实指纹） |
| `6828c18578ae` | _repo_full_inventory_catalogue_2026_10_12.md | 1 | 591851 | `_batch3_execution_receipt_kimi_2026_10_18.md`:703（＋0 件） | ②改指（候选：_repo_full_inventory_catalogue_2026_10_12.md·近字节 591833） |
| `6994a5c724a5` | — | 1 | 75169 | `_v5_sub_artifact_ledger_2026_09_28.md`:179（＋0 件） | ①补正（补登现行真实指纹） |
| `699fef8ab2bc` | — | 1 | 9607 | `_cleanup511_exec_register_2026_10_17.md`:426（＋0 件） | ①补正（补登现行真实指纹） |
| `69a69f6e9da5` | — | 1 | 3456 | `_cleanup511_exec_register_2026_10_17.md`:358（＋0 件） | ①补正（补登现行真实指纹） |
| `69e38722dbfb` | — | 1 | 3730 | `_supplement_execution_receipt_kimi_2026_10_18.md`:236（＋0 件） | ①补正（补登现行真实指纹） |
| `6a2c2cfd77bd` | — | 1 | 30875 | `_supplement_execution_receipt_kimi_2026_10_18.md`:213（＋0 件） | ①补正（补登现行真实指纹） |
| `6bdbf2659fc3` | — | 1 | 2925 | `_batch3_execution_receipt_kimi_2026_10_18.md`:254（＋0 件） | ①补正（补登现行真实指纹） |
| `6bf8b2b3b615` | — | 1 | 13773 | `_t2_path_b_build_exec_2026_10_16.md`:27（＋0 件） | ①补正（补登现行真实指纹） |
| `6c6ceb50bec7` | — | 1 | 2969 | `_supplement_execution_receipt_kimi_2026_10_18.md`:66（＋0 件） | ①补正（补登现行真实指纹） |
| `6d3212ccba08` | — | 1 | 72275 | `_cleanup511_exec_register_2026_10_17.md`:90（＋0 件） | ①补正（补登现行真实指纹） |
| `6d68adfda98a` | _t1_qwen_temp_sweep_r2_exec_register_2026_10 | 1 | 23683 | `_supplement_execution_receipt_kimi_2026_10_18.md`:314（＋0 件） | ②改指（候选：_t1_qwen_temp_sweep_r2_exec_register_2026_10_09.md·近字节 23681） |
| `6d7bbdc81561` | — | 1 | 3280 | `_supplement_execution_receipt_kimi_2026_10_18.md`:177（＋0 件） | ①补正（补登现行真实指纹） |
| `6d826839f41f` | _trae_code_improvement_v2_2026_09_18.md | 1 | 20952 | `_batch3_execution_receipt_kimi_2026_10_18.md`:495（＋0 件） | ②改指（候选：_trae_code_improvement_v2_2026_09_18.md·近字节 20938） |
| `6e559468d5c3` | — | 1 | 1171 | `_supplement_execution_receipt_kimi_2026_10_18.md`:287（＋0 件） | ①补正（补登现行真实指纹） |
| `6e559e1ee253` | — | 1 | 861900 | `_cleanup511_exec_register_2026_10_17.md`:225（＋0 件） | ①补正（补登现行真实指纹） |
| `6e64fe18a183` | — | 1 | 2176 | `_cleanup511_exec_register_2026_10_17.md`:304（＋0 件） | ①补正（补登现行真实指纹） |
| `6e9c7d9c5f46` | — | 1 | 3057 | `_supplement_execution_receipt_kimi_2026_10_18.md`:222（＋0 件） | ①补正（补登现行真实指纹） |
| `6ea425946ea0` | — | 1 | 207479 | `_cleanup511_exec_register_2026_10_17.md`:321（＋0 件） | ①补正（补登现行真实指纹） |
| `6fd5030dd9c8` | — | 1 | 3824 | `_cleanup511_exec_register_2026_10_17.md`:137（＋0 件） | ①补正（补登现行真实指纹） |
| `6fed070a015d` | — | 1 | 39841 | `_cleanup511_exec_register_2026_10_17.md`:42（＋0 件） | ①补正（补登现行真实指纹） |
| `6ff6c9d507bd` | — | 1 | 3912 | `_supplement_execution_receipt_kimi_2026_10_18.md`:91（＋0 件） | ①补正（补登现行真实指纹） |
| `704ff8780898` | — | 1 | 2636 | `_supplement_execution_receipt_kimi_2026_10_18.md`:242（＋0 件） | ①补正（补登现行真实指纹） |
| `70a87cd5022e` | — | 1 | 4433 | `_t3_repro_probe_2026_10_16.md`:340（＋0 件） | ①补正（补登现行真实指纹） |
| `70b09e3bf2f3` | — | 1 | 7796 | `_supplement_execution_receipt_kimi_2026_10_18.md`:86（＋0 件） | ①补正（补登现行真实指纹） |
| `70c66720dcb3` | — | 1 | 8202 | `_batch3_execution_receipt_kimi_2026_10_18.md`:231（＋0 件） | ①补正（补登现行真实指纹） |
| `713f48eecb52` | _forgotten_recovery_register_2026_09_29.md | 1 | 47534 | `_batch3_execution_receipt_kimi_2026_10_18.md`:580（＋0 件） | ②改指（候选：results___forgotten_recovery_register_2026_09_29.md·近字节 47526） |
| `714b2bf2648b` | _v5_paper_remedy_r2_r4_sourcetrace_2026_09_2 | 1 | 34673 | `_batch3_execution_receipt_kimi_2026_10_18.md`:860（＋0 件） | ②改指（候选：results___v5_paper_remedy_r2_r4_sourcetrace_2026_09_29.md·近字节 34651） |
| `714dc17f8f5c` | README_V4_2026_09_29.md | 1 | 58634 | `_batch3_execution_receipt_kimi_2026_10_18.md`:395（＋0 件） | ②改指（候选：README_V4_2026_09_29.md·近字节 58635） |
| `71bdd060801f` | _v5_paper_remedy_r1_pledge_2026_09_29.md | 1 | 47790 | `_batch3_execution_receipt_kimi_2026_10_18.md`:859（＋0 件） | ②改指（候选：_v5_paper_remedy_r1_pledge_2026_09_29.md·近字节 47778） |
| `71c0ddbb5574` | — | 1 | 2593 | `_cleanup511_exec_register_2026_10_17.md`:146（＋0 件） | ①补正（补登现行真实指纹） |
| `723cbec6ab10` | _t1_temp_axis_new_experiment_design_2026_10_ | 1 | 41392 | `_supplement_execution_receipt_kimi_2026_10_18.md`:319（＋0 件） | ②改指（候选：_t1_temp_axis_new_experiment_design_2026_10_09.md·近字节 41392） |
| `724676326603` | ／635,733 B 两存，差 17,022 B，归 | 1 | 1917 | `_s14_session_scan_out_2026_10_21.md`:284（＋0 件） | ①补正（补登现行真实指纹） |
| `72a379ca1f2a` | — | 1 | 70099 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:209（＋0 件） | ①补正（补登现行真实指纹） |
| `72daf6223808` | — | 1 | 1248 | `_supplement_execution_receipt_kimi_2026_10_18.md`:109（＋0 件） | ①补正（补登现行真实指纹） |
| `735586971318` | — | 1 | 2968 | `_cleanup511_exec_register_2026_10_17.md`:232（＋0 件） | ①补正（补登现行真实指纹） |
| `7364e38f6e7f` | — | 1 | 4055 | `_cleanup511_exec_register_2026_10_17.md`:74（＋0 件） | ①补正（补登现行真实指纹） |
| `73ba04b3ae71` | — | 1 | 16768 | `_supplement_execution_receipt_kimi_2026_10_18.md`:261（＋0 件） | ①补正（补登现行真实指纹） |
| `747aa15e2ec4` | — | 1 | 42427 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:239（＋0 件） | ①补正（补登现行真实指纹） |
| `7485075d16ed` | — | 1 | 38536 | `_cleanup511_exec_register_2026_10_17.md`:435（＋0 件） | ①补正（补登现行真实指纹） |
| `74f7494fa214` | — | 1 | 3303 | `_cleanup511_exec_register_2026_10_17.md`:374（＋0 件） | ①补正（补登现行真实指纹） |
| `7518e88cec4a` | — | 1 | 14826 | `_supplement_execution_receipt_kimi_2026_10_18.md`:70（＋0 件） | ①补正（补登现行真实指纹） |
| `75429a79bae4` | — | 1 | 12367 | `_batch3_execution_receipt_kimi_2026_10_18.md`:887（＋0 件） | ①补正（补登现行真实指纹） |
| `75434cb47c34` | TRAE_V3_ASSET_ERRATUM_2026_09_23.md | 1 | 857591 | `_batch3_execution_receipt_kimi_2026_10_18.md`:471（＋0 件） | ②改指（候选：TRAE_V3_ASSET_ERRATUM_2026_09_23.md·近字节 857551） |
| `7547676c4e4f` | — | 1 | 1382 | `_supplement_execution_receipt_kimi_2026_10_18.md`:182（＋0 件） | ①补正（补登现行真实指纹） |
| `754f1f2c0cc1` | — | 1 | 10614428 | `_cleanup511_exec_register_2026_10_17.md`:317（＋0 件） | ①补正（补登现行真实指纹） |
| `7587f5ac27e4` | — | 1 | 5954 | `_supplement_execution_receipt_kimi_2026_10_18.md`:214（＋0 件） | ①补正（补登现行真实指纹） |
| `75c0b7e05828` | — | 1 | 191403 | `_cleanup511_exec_register_2026_10_17.md`:318（＋0 件） | ①补正（补登现行真实指纹） |
| `75c24b61afc8` | — | 1 | 18564 | `_cleanup511_exec_register_2026_10_17.md`:217（＋0 件） | ①补正（补登现行真实指纹） |
| `75cf5737b281` | — | 1 | 2558 | `_cleanup511_exec_register_2026_10_17.md`:84（＋0 件） | ①补正（补登现行真实指纹） |
| `7638772a1e75` | — | 1 | 18561 | `_batch3_execution_receipt_kimi_2026_10_18.md`:420（＋0 件） | ①补正（补登现行真实指纹） |
| `7721e92ce82e` | — | 1 | 6338 | `_cleanup511_exec_register_2026_10_17.md`:134（＋0 件） | ①补正（补登现行真实指纹） |
| `773bb05aa7d0` | — | 1 | 99075 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:212（＋0 件） | ①补正（补登现行真实指纹） |
| `77ae98fc1ac8` | — | 1 | 66963 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:204（＋0 件） | ①补正（补登现行真实指纹） |
| `788e863f7a23` | — | 1 | 1224 | `_batch3_execution_receipt_kimi_2026_10_18.md`:240（＋0 件） | ①补正（补登现行真实指纹） |
| `78916ede0872` | — | 1 | 52830 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:197（＋0 件） | ①补正（补登现行真实指纹） |
| `796299ccadb5` | — | 1 | 7140 | `_supplement_execution_receipt_kimi_2026_10_18.md`:75（＋0 件） | ①补正（补登现行真实指纹） |
| `799853fe155c` | — | 1 | 1994 | `_cleanup511_exec_register_2026_10_17.md`:86（＋0 件） | ①补正（补登现行真实指纹） |
| `79dd4b4a87e1` | — | 1 | 2634 | `_supplement_execution_receipt_kimi_2026_10_18.md`:193（＋0 件） | ①补正（补登现行真实指纹） |
| `79eb335f5141` | _t1_prereg_revision_qwen_temp_sweep_2026_10_ | 1 | 16994 | `_supplement_execution_receipt_kimi_2026_10_18.md`:310（＋0 件） | ②改指（候选：_t1_prereg_revision_qwen_temp_sweep_2026_10_09.md·近字节 16994） |
| `7a3bbe9d2dcc` | — | 1 | 2084 | `_cleanup511_exec_register_2026_10_17.md`:379（＋0 件） | ①补正（补登现行真实指纹） |
| `7a3f3acf79cf` | — | 1 | 10012 | `_cleanup_noise_register_2026_10_21.md`:110（＋0 件） | ①补正（补登现行真实指纹） |
| `7a6b3d474f0b` | — | 1 | 4938 | `_cleanup511_exec_register_2026_10_17.md`:72（＋0 件） | ①补正（补登现行真实指纹） |
| `7a727d348e6e` | — | 1 | 3068 | `_supplement_execution_receipt_kimi_2026_10_18.md`:152（＋0 件） | ①补正（补登现行真实指纹） |
| `7a897940131c` | — | 1 | 31341 | `_cleanup_noise_register_2026_10_21.md`:114（＋0 件） | ①补正（补登现行真实指纹） |
| `7a8e212ec66d` | — | 1 | 3144 | `_cleanup511_exec_register_2026_10_17.md`:163（＋0 件） | ①补正（补登现行真实指纹） |
| `7ad62751da6f` | — | 1 | 4160 | `_cleanup511_exec_register_2026_10_17.md`:427（＋0 件） | ①补正（补登现行真实指纹） |
| `7ade25305d6f` | _v5_confirm_b8_decisions_register_2026_09_29 | 1 | 15116 | `_batch3_execution_receipt_kimi_2026_10_18.md`:855（＋0 件） | ②改指（候选：results___v5_confirm_b8_decisions_register_2026_09_29.md·近字节 15118） |
| `7b4179f7adf4` | — | 1 | 3515 | `_cleanup511_exec_register_2026_10_17.md`:418（＋0 件） | ①补正（补登现行真实指纹） |
| `7baffdc2aa9a` | — | 1 | 2460 | `_supplement_execution_receipt_kimi_2026_10_18.md`:129（＋0 件） | ①补正（补登现行真实指纹） |
| `7c2b68ec50e2` | — | 1 | 1398 | `_cleanup511_exec_register_2026_10_17.md`:453（＋0 件） | ①补正（补登现行真实指纹） |
| `7c4d9e7e4520` | _v176_v179_adoption_effect_2026_10_21.md | 1 | 3646 | `_ghost_reference_register_2026_10_21.md`:136（＋0 件） | ①补正（补登现行真实指纹） |
| `7c5703fad696` | _glm_response_v2_template_2026_09_18.md | 1 | 44133 | `_supplement_execution_receipt_kimi_2026_10_18.md`:304（＋0 件） | ②改指（候选：_glm_response_v2_template_2026_09_18.md·近字节 44191） |
| `7c89735c66ad` | — | 1 | 19385 | `_cleanup_noise_register_2026_10_21.md`:113（＋0 件） | ①补正（补登现行真实指纹） |
| `7cec2a017c35` | — | 1 | 47962 | `_batch3_execution_receipt_kimi_2026_10_18.md`:620（＋0 件） | ①补正（补登现行真实指纹） |
| `7d0acd6440cb` | — | 1 | 10772 | `_supplement_execution_receipt_kimi_2026_10_18.md`:90（＋0 件） | ①补正（补登现行真实指纹） |
| `7d57d43b3e51` | — | 1 | 8015 | `_cleanup511_exec_register_2026_10_17.md`:365（＋0 件） | ①补正（补登现行真实指纹） |
| `7d6fc895cf23` | — | 1 | 4735 | `_cleanup511_exec_register_2026_10_17.md`:122（＋0 件） | ①补正（补登现行真实指纹） |
| `7de9c35d6a33` | — | 1 | 4091 | `_batch3_execution_receipt_kimi_2026_10_18.md`:290（＋0 件） | ①补正（补登现行真实指纹） |
| `7dfe45b233da` | — | 1 | 3465 | `_cleanup511_exec_register_2026_10_17.md`:401（＋0 件） | ①补正（补登现行真实指纹） |
| `7e30fcba407e` | — | 1 | 7566 | `_supplement_execution_receipt_kimi_2026_10_18.md`:330（＋0 件） | ①补正（补登现行真实指纹） |
| `7e58051ba34b` | _dw_abs_hits_dump.md | 1 | 16838 | `_cleanup511_exec_register_2026_10_17.md`:58（＋0 件） | ①补正（补登现行真实指纹） |
| `7e7ed499cb29` | — | 1 | 5285 | `_cleanup511_exec_register_2026_10_17.md`:417（＋0 件） | ①补正（补登现行真实指纹） |
| `7eb4dbb8e2f3` | — | 1 | 44743 | `_m08_measured_enumeration_exec_2026_10_16.md`:435（＋0 件） | ①补正（补登现行真实指纹） |
| `7ec619efdcd4` | _three_items_judgment_src.md | 1 | 64073 | `_cleanup511_exec_register_2026_10_17.md`:192（＋0 件） | ①补正（补登现行真实指纹） |
| `7ecaae9d458b` | — | 1 | 5164 | `_supplement_execution_receipt_kimi_2026_10_18.md`:89（＋0 件） | ①补正（补登现行真实指纹） |
| `7f9c747b709d` | — | 1 | 1406 | `_cleanup511_exec_register_2026_10_17.md`:327（＋0 件） | ①补正（补登现行真实指纹） |
| `7fc561351cb1` | — | 1 | 2568 | `_supplement_execution_receipt_kimi_2026_10_18.md`:195（＋0 件） | ①补正（补登现行真实指纹） |
| `7ff1277ee4f9` | — | 1 | 15362 | `_cleanup511_exec_register_2026_10_17.md`:103（＋0 件） | ①补正（补登现行真实指纹） |
| `80628dc5a749` | — | 1 | 1831 | `_cleanup511_exec_register_2026_10_17.md`:127（＋0 件） | ①补正（补登现行真实指纹） |
| `8072a5f0003d` | — | 1 | 6760 | `_batch3_execution_receipt_kimi_2026_10_18.md`:247（＋0 件） | ①补正（补登现行真实指纹） |
| `807a33de3fc3` | — | 1 | 1110 | `_supplement_execution_receipt_kimi_2026_10_18.md`:184（＋0 件） | ①补正（补登现行真实指纹） |
| `81148156f14a` | — | 1 | 35431 | `_batch3_execution_receipt_kimi_2026_10_18.md`:398（＋0 件） | ①补正（补登现行真实指纹） |
| `817567721c41` | — | 1 | 1459 | `_supplement_execution_receipt_kimi_2026_10_18.md`:80（＋0 件） | ①补正（补登现行真实指纹） |
| `81c20b9c3110` | — | 1 | 14366 | `_cleanup511_exec_register_2026_10_17.md`:301（＋0 件） | ①补正（补登现行真实指纹） |
| `82320baeb8e2` | — | 1 | 1972 | `_cleanup511_exec_register_2026_10_17.md`:446（＋0 件） | ①补正（补登现行真实指纹） |
| `826b764d980a` | — | 1 | 22442 | `_cleanup511_exec_register_2026_10_17.md`:462（＋0 件） | ①补正（补登现行真实指纹） |
| `8277ff019e1f` | — | 1 | 15935 | `_batch3_execution_receipt_kimi_2026_10_18.md`:433（＋0 件） | ①补正（补登现行真实指纹） |
| `828c7ebeb270` | — | 1 | 5324 | `_cleanup511_exec_register_2026_10_17.md`:101（＋0 件） | ①补正（补登现行真实指纹） |
| `828fdcea6bd6` | — | 1 | 31853 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:238（＋0 件） | ①补正（补登现行真实指纹） |
| `8293e59b0a41` | — | 1 | 18264 | `_batch3_execution_receipt_kimi_2026_10_18.md`:394（＋0 件） | ①补正（补登现行真实指纹） |
| `82ff04b16b92` | _letter_to_kimi_push_v3_final_v2_2026_09_17. | 1 | 13972 | `_batch3_execution_receipt_kimi_2026_10_18.md`:508（＋0 件） | ②改指（候选：results___archive_2026_09_20___letter_to_kimi_push_v3_final_v2_2026_09_17.md·近字节 13967） |
| `834293288bbf` | — | 1 | 11718 | `_t2_path_b_build_exec_2026_10_16.md`:26（＋0 件） | ①补正（补登现行真实指纹） |
| `8464109947dd` | → **OUTSIDE**（归档区 | 1 | 9294 | `_forgotten_recovery_register_2026_10_08.md`:61（＋0 件） | ①补正（补登现行真实指纹） |
| `84b90b209ec5` | — | 1 | 92914 | `_cleanup511_exec_register_2026_10_17.md`:158（＋0 件） | ①补正（补登现行真实指纹） |
| `84c436875595` | — | 1 | 132519 | `_cleanup511_exec_register_2026_10_17.md`:316（＋0 件） | ①补正（补登现行真实指纹） |
| `84f001609fea` | — | 1 | 8578 | `_batch3_execution_receipt_kimi_2026_10_18.md`:274（＋0 件） | ①补正（补登现行真实指纹） |
| `8531ebdb2c9c` | — | 1 | 86220 | `_cleanup511_exec_register_2026_10_17.md`:98（＋0 件） | ①补正（补登现行真实指纹） |
| `85355676c64e` | _g5_displacement_threshold_c_approval_effect | 1 | 33880 | `_supplement_execution_receipt_kimi_2026_10_18.md`:301（＋0 件） | ②改指（候选：_g5_displacement_threshold_c_approval_effect_and_trigger_eval_2026_10_10.md·近字节 33880） |
| `85786983a421` | _clearance_materials_register_2026_10_08.md | 1 | 45385 | `_batch3_execution_receipt_kimi_2026_10_18.md`:350（＋0 件） | ②改指（候选：_clearance_materials_register_2026_10_08.md·近字节 45254） |
| `861f09ac01c2` | — | 1 | 6397 | `_cleanup511_exec_register_2026_10_17.md`:363（＋0 件） | ①补正（补登现行真实指纹） |
| `8655f9495f99` | — | 1 | 2275 | `_cleanup511_exec_register_2026_10_17.md`:182（＋0 件） | ①补正（补登现行真实指纹） |
| `86af98a26b9e` | — | 1 | 1879 | `_cleanup511_exec_register_2026_10_17.md`:451（＋0 件） | ①补正（补登现行真实指纹） |
| `86c5f6065bef` | _v4_design_integration_2026_09_21_v1.1.md | 1 | 140009 | `_batch3_execution_receipt_kimi_2026_10_18.md`:837（＋0 件） | ②改指（候选：_v4_design_integration_2026_09_21_v1.1.md·近字节 140007） |
| `87126807e3dc` | — | 1 | 58665 | `_supplement_execution_receipt_kimi_2026_10_18.md`:316（＋0 件） | ①补正（补登现行真实指纹） |
| `877aa9c2a981` | — | 1 | 7752 | `_supplement_execution_receipt_kimi_2026_10_18.md`:81（＋0 件） | ①补正（补登现行真实指纹） |
| `87aa54dfe1fc` | — | 1 | 38737 | `_cleanup511_exec_register_2026_10_17.md`:258（＋0 件） | ①补正（补登现行真实指纹） |
| `87c967818299` | _ftfb_pass2_results_limitations_audit_2026_0 | 1 | 11392 | `_batch3_execution_receipt_kimi_2026_10_18.md`:505（＋0 件） | ②改指（候选：results___archive_2026_09_20___ftfb_pass2_results_limitations_audit_2026_09_17.md·近字节 11390） |
| `8846a6df8b7a` | — | 1 | 46358 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:195（＋0 件） | ①补正（补登现行真实指纹） |
| `8859e5745902` | — | 1 | 1989 | `_cleanup511_exec_register_2026_10_17.md`:164（＋0 件） | ①补正（补登现行真实指纹） |
| `88bcbb5394eb` | _v159_adoption_effect_2026_10_20.md | 1 | 67405 | `_s14_session_scan_out_2026_10_21.md`:1184（＋0 件） | ①补正（补登现行真实指纹） |
| `88dc7d8a51d5` | — | 1 | 23893 | `_supplement_execution_receipt_kimi_2026_10_18.md`:352（＋0 件） | ①补正（补登现行真实指纹） |
| `8927845d9cd7` | — | 1 | 3235 | `_cleanup511_exec_register_2026_10_17.md`:329（＋0 件） | ①补正（补登现行真实指纹） |
| `8927f7e3a1a5` | — | 1 | 1543 | `_supplement_execution_receipt_kimi_2026_10_18.md`:78（＋0 件） | ①补正（补登现行真实指纹） |
| `893d283024c2` | — | 1 | 19685 | `_supplement_execution_receipt_kimi_2026_10_18.md`:260（＋0 件） | ①补正（补登现行真实指纹） |
| `898a5beb2690` | — | 1 | 2699 | `_supplement_execution_receipt_kimi_2026_10_18.md`:238（＋0 件） | ①补正（补登现行真实指纹） |
| `8a6c53a5bf32` | — | 1 | 4526 | `_batch3_execution_receipt_kimi_2026_10_18.md`:255（＋0 件） | ①补正（补登现行真实指纹） |
| `8a9637d3d2a0` | — | 1 | 1942 | `_supplement_execution_receipt_kimi_2026_10_18.md`:218（＋0 件） | ①补正（补登现行真实指纹） |
| `8aa37037ef39` | — | 1 | 27009 | `_supplement_execution_receipt_kimi_2026_10_18.md`:342（＋0 件） | ①补正（补登现行真实指纹） |
| `8ab58d68ec02` | — | 1 | 33837 | `_batch3_execution_receipt_kimi_2026_10_18.md`:878（＋0 件） | ①补正（补登现行真实指纹） |
| `8b80f93d9e0b` | — | 1 | 16025 | `_supplement_execution_receipt_kimi_2026_10_18.md`:337（＋0 件） | ①补正（补登现行真实指纹） |
| `8bb204dc864e` | _letter_to_kimi_push_v3_final_2026_09_17.md | 1 | 10312 | `_batch3_execution_receipt_kimi_2026_10_18.md`:507（＋0 件） | ②改指（候选：results___archive_2026_09_20___letter_to_kimi_push_v3_final_2026_09_17.md·近字节 10307） |
| `8bbf2224a026` | — | 1 | 27704 | `_cleanup511_exec_register_2026_10_17.md`:465（＋0 件） | ①补正（补登现行真实指纹） |
| `8be469b05e5e` | — | 1 | 5494 | `_supplement_execution_receipt_kimi_2026_10_18.md`:178（＋0 件） | ①补正（补登现行真实指纹） |
| `8c2cf5065dfb` | _v5_sub_artifact_ledger_history_r4_2026_09_2 | 1 | 603753 | `_batch3_execution_receipt_kimi_2026_10_18.md`:865（＋0 件） | ②改指（候选：results___v5_sub_artifact_ledger_history_r4_2026_09_29.md·近字节 603712） |
| `8cd17147e240` | — | 1 | 2142 | `_cleanup511_exec_register_2026_10_17.md`:242（＋0 件） | ①补正（补登现行真实指纹） |
| `8d6efeeae783` | REVIEWER_A_TRAE_FIX_AUDIT_2026_09_15.md | 1 | 20706 | `_batch3_execution_receipt_kimi_2026_10_18.md`:468（＋0 件） | ②改指（候选：REVIEWER_A_TRAE_FIX_AUDIT_2026_09_15.md·近字节 20698） |
| `8d87e4447ef3` | — | 1 | 4366 | `_supplement_execution_receipt_kimi_2026_10_18.md`:200（＋0 件） | ①补正（补登现行真实指纹） |
| `8d91cca38b73` | — | 1 | 3462 | `_batch3_execution_receipt_kimi_2026_10_18.md`:251（＋0 件） | ①补正（补登现行真实指纹） |
| `8d956eb6b97e` | — | 1 | 31984 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:193（＋0 件） | ①补正（补登现行真实指纹） |
| `8dbae21d4eae` | _e50_c1.md | 1 | 16236 | `_supplement_execution_receipt_kimi_2026_10_18.md`:115（＋0 件） | ①补正（补登现行真实指纹） |
| `8e6d0f12d997` | — | 1 | 6441 | `_batch3_execution_receipt_kimi_2026_10_18.md`:502（＋0 件） | ①补正（补登现行真实指纹） |
| `8ea5f8afae25` | — | 1 | 1229 | `_supplement_execution_receipt_kimi_2026_10_18.md`:111（＋0 件） | ①补正（补登现行真实指纹） |
| `8ec0ef8fa1e6` | — | 1 | 7646 | `_cleanup511_exec_register_2026_10_17.md`:85（＋0 件） | ①补正（补登现行真实指纹） |
| `8efe88fe1076` | _root_session_history_memo_2026_10_14.md | 1 | 97162 | `_batch3_execution_receipt_kimi_2026_10_18.md`:705（＋0 件） | ①补正（补登现行真实指纹） |
| `8f2ef3b675a8` | — | 1 | 6476 | `_batch3_execution_receipt_kimi_2026_10_18.md`:268（＋0 件） | ①补正（补登现行真实指纹） |
| `8f53a1f58db3` | — | 1 | 1785 | `_cleanup511_exec_register_2026_10_17.md`:169（＋0 件） | ①补正（补登现行真实指纹） |
| `8fd37c8bedb6` | — | 1 | 2568 | `_supplement_execution_receipt_kimi_2026_10_18.md`:194（＋0 件） | ①补正（补登现行真实指纹） |
| `8ff5e0105026` | — | 1 | 2297 | `_supplement_execution_receipt_kimi_2026_10_18.md`:173（＋0 件） | ①补正（补登现行真实指纹） |
| `9030ad73b4ad` | — | 1 | 27337 | `_batch3_execution_receipt_kimi_2026_10_18.md`:879（＋0 件） | ①补正（补登现行真实指纹） |
| `9056dea1d889` | — | 1 | 6403 | `_cleanup511_exec_register_2026_10_17.md`:57（＋0 件） | ①补正（补登现行真实指纹） |
| `90824245f2e2` | — | 1 | 2634 | `_supplement_execution_receipt_kimi_2026_10_18.md`:192（＋0 件） | ①补正（补登现行真实指纹） |
| `90a3a3ab7e5f` | _s4_v31_regen_gold_register_2026_10_10.md | 1 | 27133 | `_supplement_execution_receipt_kimi_2026_10_18.md`:308（＋0 件） | ②改指（候选：_s4_v31_regen_gold_register_2026_10_10.md·近字节 27133） |
| `920994c1a364` | — | 1 | 2911 | `_cleanup511_exec_register_2026_10_17.md`:107（＋0 件） | ①补正（补登现行真实指纹） |
| `9268c01fa94a` | — | 1 | 4401 | `_supplement_execution_receipt_kimi_2026_10_18.md`:156（＋0 件） | ①补正（补登现行真实指纹） |
| `92d3914037e5` | — | 1 | 32788 | `_cleanup511_exec_register_2026_10_17.md`:385（＋0 件） | ①补正（补登现行真实指纹） |
| `931a59aa1fd1` | — | 1 | 4727 | `_v4_day_inventory_2026_09_27.md`:235（＋0 件） | ①补正（补登现行真实指纹） |
| `933c6ce3e1e8` | — | 1 | 11318 | `_supplement_execution_receipt_kimi_2026_10_18.md`:354（＋0 件） | ①补正（补登现行真实指纹） |
| `9344b7be3ebb` | — | 1 | 12390 | `_cleanup511_exec_register_2026_10_17.md`:378（＋0 件） | ①补正（补登现行真实指纹） |
| `935801fcae82` | — | 1 | 16829 | `_supplement_execution_receipt_kimi_2026_10_18.md`:262（＋0 件） | ①补正（补登现行真实指纹） |
| `93b56fcc52f9` | — | 1 | 4279 | `_cleanup511_exec_register_2026_10_17.md`:150（＋0 件） | ①补正（补登现行真实指纹） |
| `93d85c99c661` | — | 1 | 1073 | `_v4_day_inventory_2026_09_27.md`:230（＋0 件） | ①补正（补登现行真实指纹） |
| `942847227e66` | — | 1 | 1626 | `_cleanup511_exec_register_2026_10_17.md`:108（＋0 件） | ①补正（补登现行真实指纹） |
| `945a3e763796` | — | 1 | 1255 | `_cleanup511_exec_register_2026_10_17.md`:249（＋0 件） | ①补正（补登现行真实指纹） |
| `946f76f1fc4e` | — | 1 | 3217 | `_cleanup511_exec_register_2026_10_17.md`:380（＋0 件） | ①补正（补登现行真实指纹） |
| `94ff1c5b89fc` | — | 1 | 1657 | `_cleanup511_exec_register_2026_10_17.md`:52（＋0 件） | ①补正（补登现行真实指纹） |
| `950f93d0a9d4` | — | 1 | 1124 | `_supplement_execution_receipt_kimi_2026_10_18.md`:101（＋0 件） | ①补正（补登现行真实指纹） |
| `957fa6e06c9b` | — | 1 | 2168 | `_batch3_execution_receipt_kimi_2026_10_18.md`:257（＋0 件） | ①补正（补登现行真实指纹） |
| `96b60eee06b5` | LETTER_TO_TRAE_FIX_SELFCHECK_2026_09_15.md | 1 | 7855 | `_batch3_execution_receipt_kimi_2026_10_18.md`:222（＋0 件） | ②改指（候选：LETTER_TO_TRAE_FIX_SELFCHECK_2026_09_15.md·近字节 7855） |
| `977e576bd99d` | — | 1 | 1246 | `_cleanup511_exec_register_2026_10_17.md`:189（＋0 件） | ①补正（补登现行真实指纹） |
| `97f162c94d17` | _v4_maindir_cleanup_manifest_2026_09_24.md | 1 | 19108 | `_batch3_execution_receipt_kimi_2026_10_18.md`:843（＋0 件） | ②改指（候选：_v4_maindir_cleanup_manifest_2026_09_24.md·近字节 19104） |
| `97f604b07e92` | — | 1 | 1029 | `_supplement_execution_receipt_kimi_2026_10_18.md`:295（＋0 件） | ①补正（补登现行真实指纹） |
| `98103909553a` | — | 1 | 6510 | `_supplement_execution_receipt_kimi_2026_10_18.md`:76（＋0 件） | ①补正（补登现行真实指纹） |
| `9812d4adcaa5` | — | 1 | 1808 | `_cleanup511_exec_register_2026_10_17.md`:287（＋0 件） | ①补正（补登现行真实指纹） |
| `9839bc1ac2fd` | v3x_dispatch_log_2026_09_16.md | 1 | 8437 | `_batch3_execution_receipt_kimi_2026_10_18.md`:409（＋0 件） | ②改指（候选：deposon_team___designs__v3x_dispatch_log_2026_09_16.md·近字节 8439） |
| `983fb938611b` | — | 1 | 1525 | `_supplement_execution_receipt_kimi_2026_10_18.md`:170（＋0 件） | ①补正（补登现行真实指纹） |
| `9871f22d32af` | — | 1 | 32336 | `_cleanup511_exec_register_2026_10_17.md`:268（＋0 件） | ①补正（补登现行真实指纹） |
| `98a3540e4dce` | — | 1 | 29361 | `_supplement_execution_receipt_kimi_2026_10_18.md`:92（＋0 件） | ①补正（补登现行真实指纹） |
| `98f0a3fd7c58` | — | 1 | 19960 | `_cleanup511_exec_register_2026_10_17.md`:256（＋0 件） | ①补正（补登现行真实指纹） |
| `99512bcce87d` | — | 1 | 88364 | `_cleanup511_exec_register_2026_10_17.md`:305（＋0 件） | ①补正（补登现行真实指纹） |
| `9975e2d58fe2` | D3_ONLINE_MIDTERM_TEMPLATE.md | 1 | 4397 | `_supplement_execution_receipt_kimi_2026_10_18.md`:284（＋0 件） | ①补正（补登现行真实指纹） |
| `99c3cfd5e178` | _v34_experiment_gap_plan_2026_10_08.md | 1 | 36070 | `_batch3_execution_receipt_kimi_2026_10_18.md`:389（＋0 件） | ②改指（候选：_v34_experiment_gap_plan_2026_10_08.md·近字节 36066） |
| `9a162fe53d4e` | — | 1 | 78463 | `_cleanup511_exec_register_2026_10_17.md`:62（＋0 件） | ①补正（补登现行真实指纹） |
| `9a4dc287feba` | _v4_pi_decision_questionnaire_2026_09_21_v1. | 1 | 113424 | `_supplement_execution_receipt_kimi_2026_10_18.md`:299（＋0 件） | ②改指（候选：_v4_pi_decision_questionnaire_2026_09_21_v1.1.md.bak_2026_09_22_gB_post.md·近字节 113508） |
| `9a91af13661e` | — | 1 | 3561 | `_supplement_execution_receipt_kimi_2026_10_18.md`:180（＋0 件） | ①补正（补登现行真实指纹） |
| `9ae2477984a2` | _stage3_1_register_fingerprint_placeholder_e | 1 | 4475 | `_supplement_execution_receipt_kimi_2026_10_18.md`:309（＋0 件） | ②改指（候选：_stage3_1_register_fingerprint_placeholder_erratum_2026_10_12.md·近字节 4495） |
| `9ae320d3f65f` | — | 1 | 8577 | `_cleanup511_exec_register_2026_10_17.md`:284（＋0 件） | ①补正（补登现行真实指纹） |
| `9b3374bbba0d` | — | 1 | 426 | `_ge01_ecr_baseline_invalid_register_2026_10_14.md`:140（＋0 件） | ①补正（补登现行真实指纹） |
| `9bf848146012` | — | 1 | 2136 | `_cleanup511_exec_register_2026_10_17.md`:403（＋0 件） | ①补正（补登现行真实指纹） |
| `9c1c4eb43443` | _remote_residual_disposal_execution_order_20 | 1 | 36752 | `_batch3_execution_receipt_kimi_2026_10_18.md`:375（＋0 件） | ②改指（候选：_remote_residual_disposal_execution_order_2026_10_08.md·近字节 36486） |
| `9c5d351481c3` | — | 1 | 3867 | `_supplement_execution_receipt_kimi_2026_10_18.md`:171（＋0 件） | ①补正（补登现行真实指纹） |
| `9c61a9c338a2` | — | 1 | 5510 | `_supplement_execution_receipt_kimi_2026_10_18.md`:246（＋0 件） | ①补正（补登现行真实指纹） |
| `9c80afbc37a3` | — | 1 | 2537 | `_supplement_execution_receipt_kimi_2026_10_18.md`:160（＋0 件） | ①补正（补登现行真实指纹） |
| `9c86c582c827` | — | 1 | 40576 | `_supplement_execution_receipt_kimi_2026_10_18.md`:205（＋0 件） | ①补正（补登现行真实指纹） |
| `9c8eb11f3e3e` | — | 1 | 15778 | `_supplement_execution_receipt_kimi_2026_10_18.md`:265（＋0 件） | ①补正（补登现行真实指纹） |
| `9c9f26ae1b9e` | — | 1 | 7398 | `_supplement_execution_receipt_kimi_2026_10_18.md`:355（＋0 件） | ①补正（补登现行真实指纹） |
| `9d052912d635` | — | 1 | 2576 | `_cleanup511_exec_register_2026_10_17.md`:147（＋0 件） | ①补正（补登现行真实指纹） |
| `9d0c56ec1982` | — | 1 | 1628 | `_supplement_execution_receipt_kimi_2026_10_18.md`:138（＋0 件） | ①补正（补登现行真实指纹） |
| `9d0caf1c1596` | — | 1 | 1673 | `_cleanup511_exec_register_2026_10_17.md`:326（＋0 件） | ①补正（补登现行真实指纹） |
| `9d6c36858636` | _dw_probe.md | 1 | 17596 | `_cleanup511_exec_register_2026_10_17.md`:64（＋0 件） | ①补正（补登现行真实指纹） |
| `9db926fbbff2` | — | 1 | 5728 | `_cleanup511_exec_register_2026_10_17.md`:280（＋0 件） | ①补正（补登现行真实指纹） |
| `9e0657fe2908` | _h_face_freeze_ruling_effect_2026_10_18.md | 1 | 28089 | `_batch3_execution_receipt_kimi_2026_10_18.md`:360（＋0 件） | ②改指（候选：_h_face_freeze_ruling_effect_2026_10_18.md·近字节 28087） |
| `9e78a44efb0c` | — | 1 | 12070 | `_batch3_execution_receipt_kimi_2026_10_18.md`:284（＋0 件） | ①补正（补登现行真实指纹） |
| `9e937104e6b6` | — | 1 | 38140 | `_cleanup511_exec_register_2026_10_17.md`:386（＋0 件） | ①补正（补登现行真实指纹） |
| `9f85f6d057ab` | — | 1 | 30834 | `_supplement_execution_receipt_kimi_2026_10_18.md`:190（＋0 件） | ①补正（补登现行真实指纹） |
| `a096694fbe49` | — | 1 | 148692 | `_batch3_execution_receipt_kimi_2026_10_18.md`:519（＋0 件） | ①补正（补登现行真实指纹） |
| `a0ce44a8dfdf` | — | 1 | 23616 | `_cleanup511_exec_register_2026_10_17.md`:303（＋0 件） | ①补正（补登现行真实指纹） |
| `a1121504815d` | — | 1 | 2397 | `_cleanup511_exec_register_2026_10_17.md`:428（＋0 件） | ①补正（补登现行真实指纹） |
| `a1444ef00c60` | _root_session_history_memo_main_2026_10_14.m | 1 | 32533 | `_t2_path_b_build_exec_2026_10_16.md`:312（＋0 件） | ①补正（补登现行真实指纹） |
| `a1afbeefb6b5` | — | 1 | 4142 | `_supplement_execution_receipt_kimi_2026_10_18.md`:74（＋0 件） | ①补正（补登现行真实指纹） |
| `a29cb5320b61` | — | 1 | 9068 | `_batch3_execution_receipt_kimi_2026_10_18.md`:267（＋0 件） | ①补正（补登现行真实指纹） |
| `a2b13900ae28` | — | 1 | 58581 | `_supplement_execution_receipt_kimi_2026_10_18.md`:343（＋0 件） | ①补正（补登现行真实指纹） |
| `a2f343f8ca3a` | — | 1 | 4459 | `_cleanup511_exec_register_2026_10_17.md`:457（＋0 件） | ①补正（补登现行真实指纹） |
| `a33b034d34cf` | — | 1 | 102623 | `_v5_confirm_b5_decisions_register_2026_09_29.md`:220（＋0 件） | ①补正（补登现行真实指纹） |
| `a36522d01b21` | — | 1 | 5006 | `_cleanup511_exec_register_2026_10_17.md`:110（＋0 件） | ①补正（补登现行真实指纹） |
| `a424fdb26ee8` | — | 1 | 54882 | `_cleanup511_exec_register_2026_10_17.md`:47（＋0 件） | ①补正（补登现行真实指纹） |
| `a5062a4d914e` | — | 1 | 34895 | `_supplement_execution_receipt_kimi_2026_10_18.md`:211（＋0 件） | ①补正（补登现行真实指纹） |
| `a61e113bebe9` | _t1_temp_axis_retirement_judgment_2026_10_10 | 1 | 27384 | `_supplement_execution_receipt_kimi_2026_10_18.md`:321（＋0 件） | ②改指（候选：_t1_temp_axis_retirement_judgment_2026_10_10.md·近字节 27384） |
| `a6215972fef2` | — | 1 | 6071 | `_supplement_execution_receipt_kimi_2026_10_18.md`:121（＋0 件） | ①补正（补登现行真实指纹） |
| `a6b4be97225f` | — | 1 | 1491 | `_cleanup511_exec_register_2026_10_17.md`:353（＋0 件） | ①补正（补登现行真实指纹） |
| `a6d33b79eb42` | — | 1 | 71901 | `_cleanup511_exec_register_2026_10_17.md`:390（＋0 件） | ①补正（补登现行真实指纹） |
| `a84c51c3b216` | — | 1 | 143261 | `_supplement_execution_receipt_kimi_2026_10_18.md`:351（＋0 件） | ①补正（补登现行真实指纹） |
| `a8c512443b0b` | DELEGATION_CONFIGS_FOR_USER_B_2026_09_16.md | 1 | 12858 | `_batch3_execution_receipt_kimi_2026_10_18.md`:402（＋0 件） | ②改指（候选：deposon_team___designs__DELEGATION_CONFIGS_FOR_USER_B_2026_09_16.md·近字节 12866） |
| `a8e130c3b759` | — | 1 | 62920 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:202（＋0 件） | ①补正（补登现行真实指纹） |
| `a8f2ae7e2ff7` | — | 1 | 3436 | `_cleanup511_exec_register_2026_10_17.md`:166（＋0 件） | ①补正（补登现行真实指纹） |
| `a97a0db22a62` | — | 1 | 2233138 | `_supplement_execution_receipt_kimi_2026_10_18.md`:134（＋0 件） | ①补正（补登现行真实指纹） |
| `a9c505ff3d2a` | — | 1 | 33928 | `_cleanup511_exec_register_2026_10_17.md`:254（＋0 件） | ①补正（补登现行真实指纹） |
| `aa3b18afd7af` | — | 1 | 1588 | `_supplement_execution_receipt_kimi_2026_10_18.md`:220（＋0 件） | ①补正（补登现行真实指纹） |
| `aa3ebcdd1808` | _e50_c1.md | 1 | 16236 | `_fake_verdict_reverify_sixitem_ledger_2026_09_30.md`:162（＋0 件） | ①补正（补登现行真实指纹） |
| `aa5a34a44f7e` | — | 1 | 8798 | `_supplement_execution_receipt_kimi_2026_10_18.md`:267（＋0 件） | ①补正（补登现行真实指纹） |
| `aa5ce1f96c08` | — | 1 | 19214 | `_supplement_execution_receipt_kimi_2026_10_18.md`:341（＋0 件） | ①补正（补登现行真实指纹） |
| `aa5faa73531c` | — | 1 | 3100 | `_batch3_execution_receipt_kimi_2026_10_18.md`:246（＋0 件） | ①补正（补登现行真实指纹） |
| `aaaf4931580c` | — | 1 | 1491 | `_v4_day_inventory_2026_09_27.md`:231（＋0 件） | ①补正（补登现行真实指纹） |
| `ab3742fe3bac` | — | 1 | 19741 | `_cleanup511_exec_register_2026_10_17.md`:216（＋0 件） | ①补正（补登现行真实指纹） |
| `ab75b709d50d` | — | 1 | 1053 | `_cleanup511_exec_register_2026_10_17.md`:259（＋0 件） | ①补正（补登现行真实指纹） |
| `ab909b47f848` | — | 1 | 107959 | `_supplement_execution_receipt_kimi_2026_10_18.md`:204（＋0 件） | ①补正（补登现行真实指纹） |
| `abcca18feded` | — | 1 | 6247 | `_batch3_execution_receipt_kimi_2026_10_18.md`:410（＋0 件） | ①补正（补登现行真实指纹） |
| `acf07a1f78bc` | — | 1 | 3444 | `_batch3_execution_receipt_kimi_2026_10_18.md`:280（＋0 件） | ①补正（补登现行真实指纹） |
| `adedb634495b` | — | 1 | 26270 | `_cleanup511_exec_register_2026_10_17.md`:155（＋0 件） | ①补正（补登现行真实指纹） |
| `ae05e267db9c` | — | 1 | 2328 | `_cleanup511_exec_register_2026_10_17.md`:73（＋0 件） | ①补正（补登现行真实指纹） |
| `af207b067524` | scout2_findings.md | 1 | 9453 | `_cleanup511_exec_register_2026_10_17.md`:398（＋0 件） | ①补正（补登现行真实指纹） |
| `af2a193d546d` | — | 1 | 2341 | `_cleanup511_exec_register_2026_10_17.md`:285（＋0 件） | ①补正（补登现行真实指纹） |
| `af2ad133f0f4` | — | 1 | 23220 | `_cleanup511_exec_register_2026_10_17.md`:466（＋0 件） | ①补正（补登现行真实指纹） |
| `af532505b7a1` | — | 1 | 4199 | `_cleanup511_exec_register_2026_10_17.md`:153（＋0 件） | ①补正（补登现行真实指纹） |
| `b0059f7b5e99` | — | 1 | 5903 | `_supplement_execution_receipt_kimi_2026_10_18.md`:159（＋0 件） | ①补正（补登现行真实指纹） |
| `b036ee4c13be` | — | 1 | 374072 | `_supplement_execution_receipt_kimi_2026_10_18.md`:344（＋0 件） | ①补正（补登现行真实指纹） |
| `b06f7ae2c313` | — | 1 | 88197 | `_cleanup511_exec_register_2026_10_17.md`:306（＋0 件） | ①补正（补登现行真实指纹） |
| `b12556882a41` | 鲍勃_阶段性推送回执_2026_10_18.md | 1 | 5928 | `_s14_session_scan_out_2026_10_21.md`:284（＋0 件） | ①补正（补登现行真实指纹） |
| `b1fde3fa431d` | — | 1 | 1870 | `_supplement_execution_receipt_kimi_2026_10_18.md`:118（＋0 件） | ①补正（补登现行真实指纹） |
| `b20b035930f9` | _five_stage_chain_design_reconstruction_2026 | 1 | 12635 | `_batch3_execution_receipt_kimi_2026_10_18.md`:579（＋0 件） | ②改指（候选：_five_stage_chain_design_reconstruction_2026_10_12.md·近字节 12625） |
| `b29b31ac9dc8` | _e50_c2.md | 1 | 16375 | `_fake_verdict_reverify_sixitem_ledger_2026_09_30.md`:163（＋0 件） | ①补正（补登现行真实指纹） |
| `b2a78900a96a` | — | 1 | 2042 | `_cleanup511_exec_register_2026_10_17.md`:437（＋0 件） | ①补正（补登现行真实指纹） |
| `b30e20ade70f` | — | 1 | 13762 | `_supplement_execution_receipt_kimi_2026_10_18.md`:279（＋0 件） | ①补正（补登现行真实指纹） |
| `b31273fc7e58` | — | 1 | 1417 | `_cleanup511_exec_register_2026_10_17.md`:342（＋0 件） | ①补正（补登现行真实指纹） |
| `b47f3563d16f` | — | 1 | 5879 | `_cleanup511_exec_register_2026_10_17.md`:106（＋0 件） | ①补正（补登现行真实指纹） |
| `b543d8d0c511` | — | 1 | 3326 | `_batch3_execution_receipt_kimi_2026_10_18.md`:282（＋0 件） | ①补正（补登现行真实指纹） |
| `b5d6139f573b` | — | 1 | 3647 | `_supplement_execution_receipt_kimi_2026_10_18.md`:228（＋0 件） | ①补正（补登现行真实指纹） |
| `b642ebc7e3ed` | — | 1 | 5891 | `_cleanup511_exec_register_2026_10_17.md`:238（＋0 件） | ①补正（补登现行真实指纹） |
| `b6a22e6cf890` | — | 1 | 17252 | `_supplement_execution_receipt_kimi_2026_10_18.md`:346（＋0 件） | ①补正（补登现行真实指纹） |
| `b76e35f97f59` | — | 1 | 2203 | `_cleanup511_exec_register_2026_10_17.md`:315（＋0 件） | ①补正（补登现行真实指纹） |
| `b7d65bb95ea7` | — | 1 | 29322 | `_cleanup511_exec_register_2026_10_17.md`:356（＋0 件） | ①补正（补登现行真实指纹） |
| `b8fe6ab59208` | — | 1 | 1662 | `_cleanup511_exec_register_2026_10_17.md`:272（＋0 件） | ①补正（补登现行真实指纹） |
| `b93a17c64feb` | — | 1 | 6659 | `_supplement_execution_receipt_kimi_2026_10_18.md`:226（＋0 件） | ①补正（补登现行真实指纹） |
| `b9930af0dfa4` | — | 1 | 3632 | `_supplement_execution_receipt_kimi_2026_10_18.md`:247（＋0 件） | ①补正（补登现行真实指纹） |
| `ba4cf7bd34a2` | — | 1 | 23987 | `_cleanup511_exec_register_2026_10_17.md`:257（＋0 件） | ①补正（补登现行真实指纹） |
| `ba6b414cf529` | — | 1 | 1689 | `_supplement_execution_receipt_kimi_2026_10_18.md`:268（＋0 件） | ①补正（补登现行真实指纹） |
| `ba750186821c` | — | 1 | 2104 | `_cleanup511_exec_register_2026_10_17.md`:129（＋0 件） | ①补正（补登现行真实指纹） |
| `baeaedc35531` | — | 1 | 44936 | `_batch3_execution_receipt_kimi_2026_10_18.md`:821（＋0 件） | ①补正（补登现行真实指纹） |
| `bb31895a5454` | — | 1 | 5659 | `_cleanup511_exec_register_2026_10_17.md`:154（＋0 件） | ①补正（补登现行真实指纹） |
| `bb482f9ed22e` | — | 1 | 6687 | `_supplement_execution_receipt_kimi_2026_10_18.md`:293（＋0 件） | ①补正（补登现行真实指纹） |
| `bb6858cae9f6` | — | 1 | 15839 | `_supplement_execution_receipt_kimi_2026_10_18.md`:266（＋0 件） | ①补正（补登现行真实指纹） |
| `bb6fca155a19` | — | 1 | 16587 | `_supplement_execution_receipt_kimi_2026_10_18.md`:340（＋0 件） | ①补正（补登现行真实指纹） |
| `bb75067f0444` | — | 1 | 68415 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:213（＋0 件） | ①补正（补登现行真实指纹） |
| `bc8d660dc37f` | — | 1 | 4079 | `_supplement_execution_receipt_kimi_2026_10_18.md`:187（＋0 件） | ①补正（补登现行真实指纹） |
| `bca7d63d539f` | _t1_qwen_temp_sweep_verdict_2026_10_09.md | 1 | 21652 | `_supplement_execution_receipt_kimi_2026_10_18.md`:318（＋0 件） | ②改指（候选：_t1_qwen_temp_sweep_verdict_2026_10_09.md·近字节 21672） |
| `bcd7e73a57a3` | — | 1 | 50554 | `_supplement_execution_receipt_kimi_2026_10_18.md`:68（＋0 件） | ①补正（补登现行真实指纹） |
| `bd228857a766` | — | 1 | 1064 | `_batch3_execution_receipt_kimi_2026_10_18.md`:277（＋0 件） | ①补正（补登现行真实指纹） |
| `bd38f9f0cf71` | — | 1 | 3994 | `_cleanup511_exec_register_2026_10_17.md`:345（＋0 件） | ①补正（补登现行真实指纹） |
| `bd544cc14400` | — | 1 | 10102 | `_batch3_execution_receipt_kimi_2026_10_18.md`:245（＋0 件） | ①补正（补登现行真实指纹） |
| `bd8eeccc563f` | — | 1 | 1959 | `_cleanup511_exec_register_2026_10_17.md`:423（＋0 件） | ①补正（补登现行真实指纹） |
| `be276ebaa837` | — | 1 | 1514 | `_ge01_ecr_baseline_invalid_register_2026_10_14.md`:139（＋0 件） | ①补正（补登现行真实指纹） |
| `be8c31f4d3f5` | — | 1 | 55983 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:206（＋0 件） | ①补正（补登现行真实指纹） |
| `be9bb0180152` | _t1_qwen_temp_sweep_exec_register_2026_10_09 | 1 | 17341 | `_supplement_execution_receipt_kimi_2026_10_18.md`:312（＋0 件） | ②改指（候选：_t1_qwen_temp_sweep_exec_register_2026_10_09.md·近字节 17341） |
| `bec98ef06a48` | _round56c_card_id_erratum_2026_10_10.md | 1 | 18749 | `_batch3_execution_receipt_kimi_2026_10_18.md`:736（＋0 件） | ②改指（候选：_round56c_card_id_erratum_2026_10_10.md·近字节 18747） |
| `bee751f59d9d` | — | 1 | 3778 | `_cleanup511_exec_register_2026_10_17.md`:432（＋0 件） | ①补正（补登现行真实指纹） |
| `bf5488dd3e03` | — | 1 | 4739 | `_supplement_execution_receipt_kimi_2026_10_18.md`:273（＋0 件） | ①补正（补登现行真实指纹） |
| `bf69166bf41a` | — | 1 | 1092 | `_batch3_execution_receipt_kimi_2026_10_18.md`:278（＋0 件） | ①补正（补登现行真实指纹） |
| `bfad0adbb7a4` | — | 1 | 1274 | `_cleanup511_exec_register_2026_10_17.md`:246（＋0 件） | ①补正（补登现行真实指纹） |
| `c000fbc1daa8` | — | 1 | 4669 | `_cleanup511_exec_register_2026_10_17.md`:328（＋0 件） | ①补正（补登现行真实指纹） |
| `c028df02048f` | — | 1 | 5147 | `_cleanup511_exec_register_2026_10_17.md`:416（＋0 件） | ①补正（补登现行真实指纹） |
| `c0856f2261cd` | — | 1 | 2830 | `_cleanup511_exec_register_2026_10_17.md`:295（＋0 件） | ①补正（补登现行真实指纹） |
| `c0acb218eeed` | _v3r1_threshold_restatement_design_2026_10_1 | 1 | 33847 | `_supplement_execution_receipt_kimi_2026_10_18.md`:326（＋0 件） | ②改指（候选：_v3r1_threshold_restatement_design_2026_10_10.md·近字节 33847） |
| `c0fa4f010a0e` | — | 1 | 1234 | `_supplement_execution_receipt_kimi_2026_10_18.md`:225（＋0 件） | ①补正（补登现行真实指纹） |
| `c11fe104a0e5` | — | 1 | 1692 | `_cleanup511_exec_register_2026_10_17.md`:294（＋0 件） | ①补正（补登现行真实指纹） |
| `c166350e1753` | — | 1 | 2857 | `_cleanup511_exec_register_2026_10_17.md`:263（＋0 件） | ①补正（补登现行真实指纹） |
| `c18b58b3296b` | — | 1 | 1003 | `_v4_day_inventory_2026_09_27.md`:229（＋0 件） | ①补正（补登现行真实指纹） |
| `c1b7bd01280a` | — | 1 | 1684 | `_cleanup511_exec_register_2026_10_17.md`:193（＋0 件） | ①补正（补登现行真实指纹） |
| `c1da8d161c0b` | — | 1 | 53180 | `_supplement_execution_receipt_kimi_2026_10_18.md`:315（＋0 件） | ①补正（补登现行真实指纹） |
| `c1e8170c962d` | — | 1 | 8018 | `_supplement_execution_receipt_kimi_2026_10_18.md`:197（＋0 件） | ①补正（补登现行真实指纹） |
| `c2082c4fed57` | _t1_qwen_temp_sweep_r2_verdict_2026_10_09.md | 1 | 42817 | `_supplement_execution_receipt_kimi_2026_10_18.md`:317（＋0 件） | ②改指（候选：_t1_qwen_temp_sweep_r2_verdict_2026_10_09.md·近字节 42817） |
| `c23b829945c1` | _deemphasis_verification_register_2026_10_08 | 1 | 27611 | `_batch3_execution_receipt_kimi_2026_10_18.md`:355（＋0 件） | ②改指（候选：_deemphasis_verification_register_2026_10_08.md·近字节 27322） |
| `c2de9490d779` | — | 1 | 31468 | `_supplement_execution_receipt_kimi_2026_10_18.md`:203（＋0 件） | ①补正（补登现行真实指纹） |
| `c32276eebb22` | _letters_archive_register_2026_10_01.md | 1 | 26303 | `_batch3_execution_receipt_kimi_2026_10_18.md`:641（＋0 件） | ②改指（候选：_letters_archive_register_2026_10_01.md·近字节 26299） |
| `c33297a48024` | — | 1 | 6106 | `_batch3_execution_receipt_kimi_2026_10_18.md`:266（＋0 件） | ①补正（补登现行真实指纹） |
| `c347fa1b2e34` | _upload_guard_mirror_pair_2026_10_08.md | 1 | 23634 | `_batch3_execution_receipt_kimi_2026_10_18.md`:816（＋0 件） | ②改指（候选：results___upload_guard_mirror_pair_2026_10_08.md·近字节 23604） |
| `c349c30ddbdc` | — | 1 | 1678 | `_batch3_execution_receipt_kimi_2026_10_18.md`:263（＋0 件） | ①补正（补登现行真实指纹） |
| `c42d45b19fde` | — | 1 | 30676 | `_batch3_execution_receipt_kimi_2026_10_18.md`:419（＋0 件） | ①补正（补登现行真实指纹） |
| `c45247cf27b8` | — | 1 | 204258 | `_batch3_execution_receipt_kimi_2026_10_18.md`:521（＋0 件） | ①补正（补登现行真实指纹） |
| `c4a1990c9f8d` | — | 1 | 43930 | `_cleanup511_exec_register_2026_10_17.md`:292（＋0 件） | ①补正（补登现行真实指纹） |
| `c5134c5f7c7b` | — | 1 | 2194 | `_cleanup511_exec_register_2026_10_17.md`:412（＋0 件） | ①补正（补登现行真实指纹） |
| `c51af9d1cfbf` | — | 1 | 12249258 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:137（＋0 件） | ①补正（补登现行真实指纹） |
| `c54be1035a90` | — | 1 | 11873 | `_cleanup511_exec_register_2026_10_17.md`:39（＋0 件） | ①补正（补登现行真实指纹） |
| `c5d2de462a02` | — | 1 | 8807 | `_supplement_execution_receipt_kimi_2026_10_18.md`:140（＋0 件） | ①补正（补登现行真实指纹） |
| `c62de09bbde9` | — | 1 | 38520 | `_cleanup511_exec_register_2026_10_17.md`:109（＋0 件） | ①补正（补登现行真实指纹） |
| `c66fdfc06f59` | — | 1 | 2813 | `_cleanup511_exec_register_2026_10_17.md`:337（＋0 件） | ①补正（补登现行真实指纹） |
| `c68024ab09ee` | _round56_idx_sc1_temp_deletion_deviation_not | 1 | 8143 | `_supplement_execution_receipt_kimi_2026_10_18.md`:306（＋0 件） | ②改指（候选：_round56_idx_sc1_temp_deletion_deviation_note_2026_10_10.md·近字节 8181） |
| `c681898eac9b` | — | 1 | 3039 | `_cleanup511_exec_register_2026_10_17.md`:264（＋0 件） | ①补正（补登现行真实指纹） |
| `c69c6a06dfcf` | — | 1 | 1184 | `_batch3_execution_receipt_kimi_2026_10_18.md`:230（＋0 件） | ①补正（补登现行真实指纹） |
| `c6ce0ac23598` | — | 1 | 44021 | `_cleanup511_exec_register_2026_10_17.md`:228（＋0 件） | ①补正（补登现行真实指纹） |
| `c6e0d6b59168` | — | 1 | 18714 | `_supplement_execution_receipt_kimi_2026_10_18.md`:339（＋0 件） | ①补正（补登现行真实指纹） |
| `c70f833f9014` | — | 1 | 20939 | `_batch3_execution_receipt_kimi_2026_10_18.md`:411（＋0 件） | ①补正（补登现行真实指纹） |
| `c71a2831383f` | — | 1 | 2329 | `_supplement_execution_receipt_kimi_2026_10_18.md`:102（＋0 件） | ①补正（补登现行真实指纹） |
| `c7da3ec2a062` | — | 1 | 4326911 | `_cleanup511_exec_register_2026_10_17.md`:319（＋0 件） | ①补正（补登现行真实指纹） |
| `c7deb6f758fa` | — | 1 | 4890 | `_supplement_execution_receipt_kimi_2026_10_18.md`:71（＋0 件） | ①补正（补登现行真实指纹） |
| `c86acc2b77a3` | — | 1 | 9232 | `_batch3_execution_receipt_kimi_2026_10_18.md`:228（＋0 件） | ①补正（补登现行真实指纹） |
| `c893e9d84f50` | — | 1 | 89853 | `_cleanup511_exec_register_2026_10_17.md`:237（＋0 件） | ①补正（补登现行真实指纹） |
| `c895409e968f` | — | 1 | 9226 | `_supplement_execution_receipt_kimi_2026_10_18.md`:234（＋0 件） | ①补正（补登现行真实指纹） |
| `c8a5e2dc0420` | — | 1 | 6887 | `_batch3_execution_receipt_kimi_2026_10_18.md`:273（＋0 件） | ①补正（补登现行真实指纹） |
| `c9bd76d9dc10` | — | 1 | 5968 | `_supplement_execution_receipt_kimi_2026_10_18.md`:199（＋0 件） | ①补正（补登现行真实指纹） |
| `ca374754b834` | — | 1 | 2305 | `_cleanup511_exec_register_2026_10_17.md`:430（＋0 件） | ①补正（补登现行真实指纹） |
| `ca5f6e8198a1` | — | 1 | 7167 | `_cleanup511_exec_register_2026_10_17.md`:278（＋0 件） | ①补正（补登现行真实指纹） |
| `ca6c73cb7c65` | — | 1 | 34804 | `_cleanup511_exec_register_2026_10_17.md`:55（＋0 件） | ①补正（补登现行真实指纹） |
| `cabebb13a0f1` | — | 1 | 4282 | `_supplement_execution_receipt_kimi_2026_10_18.md`:153（＋0 件） | ①补正（补登现行真实指纹） |
| `cad1f3e03642` | — | 1 | 8983 | `_supplement_execution_receipt_kimi_2026_10_18.md`:196（＋0 件） | ①补正（补登现行真实指纹） |
| `cada2e0fdaab` | — | 1 | 28811 | `_cleanup511_exec_register_2026_10_17.md`:208（＋0 件） | ①补正（补登现行真实指纹） |
| `cbdf8e990781` | _v4_tmp_cleanup_2026_09_28.md | 1 | 5122 | `_supplement_execution_receipt_kimi_2026_10_18.md`:353（＋0 件） | ②改指（候选：_v4_tmp_cleanup_2026_09_28.md·近字节 5131） |
| `cc1d6f2291f9` | _v3r1_threshold_final_path_judgment_2026_10_ | 1 | 39653 | `_supplement_execution_receipt_kimi_2026_10_18.md`:324（＋0 件） | ②改指（候选：_v3r1_threshold_final_path_judgment_2026_10_10.md·近字节 39653） |
| `cc6c30fe4503` | — | 1 | 3471 | `_supplement_execution_receipt_kimi_2026_10_18.md`:253（＋0 件） | ①补正（补登现行真实指纹） |
| `ccf2abf85550` | _repo_post_cleanup_snapshot_2026_10_12.md | 1 | 309447 | `_batch3_execution_receipt_kimi_2026_10_18.md`:704（＋0 件） | ②改指（候选：_repo_post_cleanup_snapshot_2026_10_12.md·近字节 309419） |
| `cd32e4cf02ff` | — | 1 | 3001 | `_cleanup511_exec_register_2026_10_17.md`:397（＋0 件） | ①补正（补登现行真实指纹） |
| `cd55f8e738a7` | — | 1 | 63363 | `_cleanup511_exec_register_2026_10_17.md`:314（＋0 件） | ①补正（补登现行真实指纹） |
| `cdb4afcff9c4` | — | 1 | 1842 | `_cleanup511_exec_register_2026_10_17.md`:252（＋0 件） | ①补正（补登现行真实指纹） |
| `cdc09278eb09` | _v4_maindir_count_monitor_2026_09_27.md | 1 | 15321 | `_batch3_execution_receipt_kimi_2026_10_18.md`:847（＋0 件） | ②改指（候选：_v4_maindir_count_monitor_2026_09_27.md·近字节 15313） |
| `cdc5706f1289` | — | 1 | 45574 | `_cleanup511_exec_register_2026_10_17.md`:429（＋0 件） | ①补正（补登现行真实指纹） |
| `cdde6f432998` | — | 1 | 1199 | `_cleanup511_exec_register_2026_10_17.md`:190（＋0 件） | ①补正（补登现行真实指纹） |
| `cdf86876eece` | — | 1 | 236653 | `_batch3_execution_receipt_kimi_2026_10_18.md`:520（＋0 件） | ①补正（补登现行真实指纹） |
| `ce1709f782f5` | — | 1 | 17456 | `_batch3_execution_receipt_kimi_2026_10_18.md`:265（＋0 件） | ①补正（补登现行真实指纹） |
| `ce5d71f516e9` | — | 1 | 1272 | `_batch3_execution_receipt_kimi_2026_10_18.md`:275（＋0 件） | ①补正（补登现行真实指纹） |
| `ce8e9dc56752` | — | 1 | 24575 | `_cleanup511_exec_register_2026_10_17.md`:211（＋0 件） | ①补正（补登现行真实指纹） |
| `cec2795228fe` | TRAE_CODE_FIX_LIST_2026_09_18.md | 1 | 9343 | `_batch3_execution_receipt_kimi_2026_10_18.md`:223（＋0 件） | ②改指（候选：TRAE_CODE_FIX_LIST_2026_09_18.md·近字节 9343） |
| `cee46a86017f` | — | 1 | 2377 | `_supplement_execution_receipt_kimi_2026_10_18.md`:127（＋0 件） | ①补正（补登现行真实指纹） |
| `cf6ef1c7e631` | — | 1 | 7398 | `_supplement_execution_receipt_kimi_2026_10_18.md`:281（＋0 件） | ①补正（补登现行真实指纹） |
| `cfd863a3c640` | — | 1 | 32632 | `_cleanup_noise_register_2026_10_21.md`:109（＋0 件） | ①补正（补登现行真实指纹） |
| `cfde1a0d83de` | — | 1 | 30657 | `_cleanup511_exec_register_2026_10_17.md`:313（＋0 件） | ①补正（补登现行真实指纹） |
| `d035dd778940` | — | 1 | 3400 | `_cleanup511_exec_register_2026_10_17.md`:262（＋0 件） | ①补正（补登现行真实指纹） |
| `d0c9cdbd8da6` | — | 1 | 4136 | `_cleanup511_exec_register_2026_10_17.md`:241（＋0 件） | ①补正（补登现行真实指纹） |
| `d12f1011d301` | — | 1 | 1282 | `_cleanup511_exec_register_2026_10_17.md`:340（＋0 件） | ①补正（补登现行真实指纹） |
| `d14c965581a6` | — | 1 | 34829 | `_cleanup511_exec_register_2026_10_17.md`:207（＋0 件） | ①补正（补登现行真实指纹） |
| `d1d8cdc4f7d5` | — | 1 | 1327 | `_cleanup511_exec_register_2026_10_17.md`:436（＋0 件） | ①补正（补登现行真实指纹） |
| `d223e89d3b0c` | _dw_fullrows.md | 1 | 10893 | `_cleanup511_exec_register_2026_10_17.md`:60（＋0 件） | ①补正（补登现行真实指纹） |
| `d225c6086e57` | — | 1 | 47731 | `_glm_unique_reply_117_triage_2026_10_19.md`:141（＋0 件） | ①补正（补登现行真实指纹） |
| `d34ed54fc1f3` | — | 1 | 35886 | `_cleanup511_exec_register_2026_10_17.md`:45（＋0 件） | ①补正（补登现行真实指纹） |
| `d39d9023f615` | — | 1 | 27736 | `_batch3_execution_receipt_kimi_2026_10_18.md`:429（＋0 件） | ①补正（补登现行真实指纹） |
| `d48522c7f373` | _dw_pkg_downstream_dump.md | 1 | 12044 | `_cleanup511_exec_register_2026_10_17.md`:63（＋0 件） | ①补正（补登现行真实指纹） |
| `d5051d628807` | — | 1 | 18519 | `_cleanup511_exec_register_2026_10_17.md`:97（＋0 件） | ①补正（补登现行真实指纹） |
| `d5056090efa0` | — | 1 | 1445 | `_supplement_execution_receipt_kimi_2026_10_18.md`:135（＋0 件） | ①补正（补登现行真实指纹） |
| `d51a459fa20a` | — | 1 | 5639 | `_supplement_execution_receipt_kimi_2026_10_18.md`:163（＋0 件） | ①补正（补登现行真实指纹） |
| `d5c8e33ac072` | _e50_c2.md | 1 | 17220 | `_supplement_execution_receipt_kimi_2026_10_18.md`:116（＋0 件） | ①补正（补登现行真实指纹） |
| `d5d8e2048b07` | — | 1 | 3763 | `_cleanup511_exec_register_2026_10_17.md`:223（＋0 件） | ①补正（补登现行真实指纹） |
| `d5dfe1f283bb` | — | 1 | 26654 | `_supplement_execution_receipt_kimi_2026_10_18.md`:207（＋0 件） | ①补正（补登现行真实指纹） |
| `d5fa8fabe79b` | — | 1 | 17632 | `_batch3_execution_receipt_kimi_2026_10_18.md`:249（＋0 件） | ①补正（补登现行真实指纹） |
| `d6a9ac9c08b7` | — | 1 | 13481 | `_cleanup511_exec_register_2026_10_17.md`:119（＋0 件） | ①补正（补登现行真实指纹） |
| `d6dab1351db9` | — | 1 | 32199 | `_cleanup511_exec_register_2026_10_17.md`:359（＋0 件） | ①补正（补登现行真实指纹） |
| `d7108663b6f1` | — | 1 | 8617 | `_supplement_execution_receipt_kimi_2026_10_18.md`:248（＋0 件） | ①补正（补登现行真实指纹） |
| `d769c3a12750` | — | 1 | 2382 | `_cleanup511_exec_register_2026_10_17.md`:411（＋0 件） | ①补正（补登现行真实指纹） |
| `d809e3836e11` | — | 1 | 25981 | `_cleanup511_exec_register_2026_10_17.md`:459（＋0 件） | ①补正（补登现行真实指纹） |
| `d8640f48c712` | — | 1 | 12050 | `_cleanup511_exec_register_2026_10_17.md`:133（＋0 件） | ①补正（补登现行真实指纹） |
| `d87518e980e7` | — | 1 | 7470 | `_d8_collection_ledger_2026_09_30.md`:84（＋0 件） | ①补正（补登现行真实指纹） |
| `d8a366edcbf5` | scout4_findings.md | 1 | 2035 | `_cleanup511_exec_register_2026_10_17.md`:402（＋0 件） | ①补正（补登现行真实指纹） |
| `d8d5e4938fc5` | — | 1 | 1152 | `_cleanup511_exec_register_2026_10_17.md`:336（＋0 件） | ①补正（补登现行真实指纹） |
| `d8e01c25f6f3` | — | 1 | 19615 | `_supplement_execution_receipt_kimi_2026_10_18.md`:336（＋0 件） | ①补正（补登现行真实指纹） |
| `d8f205375a2c` | — | 1 | 18536 | `_cleanup511_exec_register_2026_10_17.md`:215（＋0 件） | ①补正（补登现行真实指纹） |
| `d8f839eca7ce` | — | 1 | 27013 | `_cleanup511_exec_register_2026_10_17.md`:93（＋0 件） | ①补正（补登现行真实指纹） |
| `d94b604e9dd9` | — | 1 | 6620 | `_cleanup511_exec_register_2026_10_17.md`:309（＋0 件） | ①补正（补登现行真实指纹） |
| `d957e3ad8f87` | — | 1 | 8885 | `_batch3_execution_receipt_kimi_2026_10_18.md`:271（＋0 件） | ①补正（补登现行真实指纹） |
| `d98932573850` | — | 1 | 3378 | `_cleanup511_exec_register_2026_10_17.md`:226（＋0 件） | ①补正（补登现行真实指纹） |
| `d9c9013097c0` | — | 1 | 50302 | `_cleanup511_exec_register_2026_10_17.md`:220（＋0 件） | ①补正（补登现行真实指纹） |
| `d9ee609f4101` | — | 1 | 1420 | `_supplement_execution_receipt_kimi_2026_10_18.md`:210（＋0 件） | ①补正（补登现行真实指纹） |
| `da2762af8b25` | _dw_manifest_lines.md | 1 | 4400 | `_cleanup511_exec_register_2026_10_17.md`:61（＋0 件） | ①补正（补登现行真实指纹） |
| `da5bc61b76c5` | — | 1 | 36025 | `_cleanup511_exec_register_2026_10_17.md`:441（＋0 件） | ①补正（补登现行真实指纹） |
| `da6f97237f4c` | — | 1 | 5895 | `_cleanup511_exec_register_2026_10_17.md`:100（＋0 件） | ①补正（补登现行真实指纹） |
| `dab9a1c18a9e` | _v4_maindir_cleanup_moves_ledger_v3_2026_09_ | 1 | 31691 | `_batch3_execution_receipt_kimi_2026_10_18.md`:845（＋0 件） | ②改指（候选：_v4_maindir_cleanup_moves_ledger_v3_2026_09_24.md·近字节 31689） |
| `daf2e2760fca` | — | 1 | 5195 | `_supplement_execution_receipt_kimi_2026_10_18.md`:69（＋0 件） | ①补正（补登现行真实指纹） |
| `dd983b28e9aa` | — | 1 | 2745 | `_cleanup511_exec_register_2026_10_17.md`:442（＋0 件） | ①补正（补登现行真实指纹） |
| `dde73101cf15` | — | 1 | 48004 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:231（＋0 件） | ①补正（补登现行真实指纹） |
| `ddeddb253a24` | — | 1 | 3026 | `_cleanup511_exec_register_2026_10_17.md`:333（＋0 件） | ①补正（补登现行真实指纹） |
| `de8ad26b54c8` | — | 1 | 5062 | `_supplement_execution_receipt_kimi_2026_10_18.md`:255（＋0 件） | ①补正（补登现行真实指纹） |
| `de93624ff635` | _verdict_pack_d_prep_2026_10_01.md | 1 | 49471 | `_supplement_execution_receipt_kimi_2026_10_18.md`:384（＋0 件） | ②改指（候选：_verdict_pack_d_prep_2026_10_01.md·近字节 49471） |
| `df592309cce7` | — | 1 | 2525 | `_supplement_execution_receipt_kimi_2026_10_18.md`:189（＋0 件） | ①补正（补登现行真实指纹） |
| `df6bdbfa8e99` | _achievements_inventory_full_2026_10_18.md | 1 | 805466 | `_batch3_execution_receipt_kimi_2026_10_18.md`:348（＋0 件） | ②改指（候选：_achievements_inventory_full_2026_10_18.md·近字节 805428） |
| `dfd846fe93ff` | _reg_v32_sec6_2026_10_16.md | 1 | 6788 | `_cleanup511_exec_register_2026_10_17.md`:151（＋0 件） | ①补正（补登现行真实指纹） |
| `e0670450a21e` | — | 1 | 8757 | `_cleanup511_exec_register_2026_10_17.md`:102（＋0 件） | ①补正（补登现行真实指纹） |
| `e1376132083a` | — | 1 | 1158 | `_supplement_execution_receipt_kimi_2026_10_18.md`:96（＋0 件） | ①补正（补登现行真实指纹） |
| `e212bce6f24c` | — | 1 | 23204 | `_supplement_execution_receipt_kimi_2026_10_18.md`:202（＋0 件） | ①补正（补登现行真实指纹） |
| `e241db6b7745` | — | 1 | 2876 | `_supplement_execution_receipt_kimi_2026_10_18.md`:169（＋0 件） | ①补正（补登现行真实指纹） |
| `e243f65ad00c` | — | 1 | 2327 | `_cleanup511_exec_register_2026_10_17.md`:148（＋0 件） | ①补正（补登现行真实指纹） |
| `e3199c565bdf` | — | 1 | 2868 | `_cleanup511_exec_register_2026_10_17.md`:78（＋0 件） | ①补正（补登现行真实指纹） |
| `e3f816702596` | — | 1 | 17106 | `_supplement_execution_receipt_kimi_2026_10_18.md`:139（＋0 件） | ①补正（补登现行真实指纹） |
| `e41753d347c6` | — | 1 | 8417 | `_cleanup511_exec_register_2026_10_17.md`:362（＋0 件） | ①补正（补登现行真实指纹） |
| `e435edef34da` | — | 1 | 2046 | `_batch3_execution_receipt_kimi_2026_10_18.md`:248（＋0 件） | ①补正（补登现行真实指纹） |
| `e4ba8c0c305e` | — | 1 | 1633 | `_cleanup511_exec_register_2026_10_17.md`:266（＋0 件） | ①补正（补登现行真实指纹） |
| `e4fe5b54e2a8` | — | 1 | 10063 | `_cleanup511_exec_register_2026_10_17.md`:67（＋0 件） | ①补正（补登现行真实指纹） |
| `e59531f06223` | _kv3s_3_2_terminal_verdict_2026_10_01.md | 1 | 32296 | `_supplement_execution_receipt_kimi_2026_10_18.md`:380（＋0 件） | ②改指（候选：_kv3s_3_2_terminal_verdict_2026_10_01.md·近字节 32296） |
| `e6bcc77790a9` | — | 1 | 3880 | `_supplement_execution_receipt_kimi_2026_10_18.md`:227（＋0 件） | ①补正（补登现行真实指纹） |
| `e6c566d26edd` | — | 1 | 10156 | `_cleanup511_exec_register_2026_10_17.md`:372（＋0 件） | ①补正（补登现行真实指纹） |
| `e6df31e1eb38` | — | 1 | 117196 | `_cleanup511_exec_register_2026_10_17.md`:410（＋0 件） | ①补正（补登现行真实指纹） |
| `e728ba7bd2b4` | — | 1 | 43047 | `_batch3_execution_receipt_kimi_2026_10_18.md`:663（＋0 件） | ①补正（补登现行真实指纹） |
| `e82e31e2ef6a` | — | 1 | 612511 | `_supplement_execution_receipt_kimi_2026_10_18.md`:297（＋0 件） | ①补正（补登现行真实指纹） |
| `e870aa641631` | — | 1 | 22373 | `_cleanup511_exec_register_2026_10_17.md`:409（＋0 件） | ①补正（补登现行真实指纹） |
| `e88eb617d975` | — | 1 | 19232 | `_batch3_execution_receipt_kimi_2026_10_18.md`:397（＋0 件） | ①补正（补登现行真实指纹） |
| `e88f8cd0bc46` | — | 1 | 1444 | `_cleanup511_exec_register_2026_10_17.md`:421（＋0 件） | ①补正（补登现行真实指纹） |
| `e8abd8ad0df5` | — | 1 | 7755 | `_cleanup511_exec_register_2026_10_17.md`:267（＋0 件） | ①补正（补登现行真实指纹） |
| `e8b3b3672f10` | _t1_temp_axis_retirement_consolidation_2026_ | 1 | 20308 | `_supplement_execution_receipt_kimi_2026_10_18.md`:320（＋0 件） | ②改指（候选：_t1_temp_axis_retirement_consolidation_2026_10_10.md·近字节 20308） |
| `ea509bd7c54b` | — | 1 | 30525 | `_cleanup511_exec_register_2026_10_17.md`:460（＋0 件） | ①补正（补登现行真实指纹） |
| `ea95cd870ddd` | — | 1 | 20994 | `_supplement_execution_receipt_kimi_2026_10_18.md`:98（＋0 件） | ①补正（补登现行真实指纹） |
| `eaca6469925c` | — | 1 | 59327 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:190（＋0 件） | ①补正（补登现行真实指纹） |
| `eb4c98ffcb95` | REVIEWER_B_TMP_RERUN_2026_09_15.md | 1 | 21654 | `_supplement_execution_receipt_kimi_2026_10_18.md`:286（＋0 件） | ②改指（候选：REVIEWER_B_TMP_RERUN_2026_09_15.md·近字节 21654） |
| `ebdf7a3a7962` | — | 1 | 3144 | `_supplement_execution_receipt_kimi_2026_10_18.md`:94（＋0 件） | ①补正（补登现行真实指纹） |
| `ec35695b5479` | — | 1 | 2370 | `_batch3_execution_receipt_kimi_2026_10_18.md`:232（＋0 件） | ①补正（补登现行真实指纹） |
| `ec3bf2f14e34` | — | 1 | 5709 | `_supplement_execution_receipt_kimi_2026_10_18.md`:73（＋0 件） | ①补正（补登现行真实指纹） |
| `ecd789f3b87b` | — | 1 | 7377 | `_supplement_execution_receipt_kimi_2026_10_18.md`:275（＋0 件） | ①补正（补登现行真实指纹） |
| `ed9562894231` | — | 1 | 17745 | `_batch3_execution_receipt_kimi_2026_10_18.md`:421（＋0 件） | ①补正（补登现行真实指纹） |
| `ef853f764395` | — | 1 | 1435 | `_supplement_execution_receipt_kimi_2026_10_18.md`:124（＋0 件） | ①补正（补登现行真实指纹） |
| `efb4fcc11ef9` | — | 1 | 10102 | `_cleanup511_exec_register_2026_10_17.md`:414（＋0 件） | ①补正（补登现行真实指纹） |
| `f02992c7aff2` | — | 1 | 1516 | `_batch3_execution_receipt_kimi_2026_10_18.md`:233（＋0 件） | ①补正（补登现行真实指纹） |
| `f0a5c8c61d15` | _root_session_history_memo_main_2026_10_14.m | 1 | 47890 | `_ge02_anchor_landing_build_register_2026_10_16.md`:137（＋0 件） | ①补正（补登现行真实指纹） |
| `f0af8caa4755` | — | 1 | 95900 | `_cleanup511_exec_register_2026_10_17.md`:92（＋0 件） | ①补正（补登现行真实指纹） |
| `f0c82788b36c` | — | 1 | 4086 | `_cleanup511_exec_register_2026_10_17.md`:439（＋0 件） | ①补正（补登现行真实指纹） |
| `f0e928beca38` | — | 1 | 3743 | `_supplement_execution_receipt_kimi_2026_10_18.md`:185（＋0 件） | ①补正（补登现行真实指纹） |
| `f1c2c373e75c` | — | 1 | 12672 | `_supplement_execution_receipt_kimi_2026_10_18.md`:327（＋0 件） | ①补正（补登现行真实指纹） |
| `f1c47aa6b61c` | — | 1 | 95139 | `_supplement_execution_receipt_kimi_2026_10_18.md`:276（＋0 件） | ①补正（补登现行真实指纹） |
| `f35a35c2820b` | — | 1 | 37 | `_v143_v144_adoption_effect_2026_10_19.md`:272（＋0 件） | ①补正（补登现行真实指纹） |
| `f37bd42cd678` | — | 1 | 174424 | `_supplement_execution_receipt_kimi_2026_10_18.md`:251（＋0 件） | ①补正（补登现行真实指纹） |
| `f3a21eaf849c` | — | 1 | 1684 | `_cleanup511_exec_register_2026_10_17.md`:197（＋0 件） | ①补正（补登现行真实指纹） |
| `f40825a364b8` | _plan_v3_pending_verify_2026_09_30.md | 1 | 42294 | `_batch3_execution_receipt_kimi_2026_10_18.md`:670（＋0 件） | ②改指（候选：_plan_v3_pending_verify_2026_09_30.md·近字节 42280） |
| `f4260aa2fdb4` | — | 1 | 2293 | `_cleanup511_exec_register_2026_10_17.md`:195（＋0 件） | ①补正（补登现行真实指纹） |
| `f4c5f4a22084` | — | 1 | 4103 | `_supplement_execution_receipt_kimi_2026_10_18.md`:328（＋0 件） | ①补正（补登现行真实指纹） |
| `f589b7b0ee56` | — | 1 | 53281 | `_cleanup511_exec_register_2026_10_17.md`:335（＋0 件） | ①补正（补登现行真实指纹） |
| `f5cccc1e5b6a` | — | 1 | 1140 | `_batch3_execution_receipt_kimi_2026_10_18.md`:242（＋0 件） | ①补正（补登现行真实指纹） |
| `f649e045876a` | _v3_v4_achievements_inventory_3dir_addendum_ | 1 | 37218 | `_batch3_execution_receipt_kimi_2026_10_18.md`:827（＋0 件） | ②改指（候选：_v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md·近字节 37212） |
| `f655261eb41b` | — | 1 | 1182 | `_cleanup511_exec_register_2026_10_17.md`:350（＋0 件） | ①补正（补登现行真实指纹） |
| `f668d287956f` | — | 1 | 2695 | `_cleanup511_exec_register_2026_10_17.md`:334（＋0 件） | ①补正（补登现行真实指纹） |
| `f67eeeeaaf9f` | — | 1 | 2619 | `_cleanup511_exec_register_2026_10_17.md`:244（＋0 件） | ①补正（补登现行真实指纹） |
| `f6908a189333` | — | 1 | 17272 | `_supplement_execution_receipt_kimi_2026_10_18.md`:240（＋0 件） | ①补正（补登现行真实指纹） |
| `f69ff63db2fd` | — | 1 | 3355 | `_cleanup511_exec_register_2026_10_17.md`:388（＋0 件） | ①补正（补登现行真实指纹） |
| `f6ac11f43855` | _v3_v4_achievements_inventory_2026_09_24.md | 1 | 194131 | `_batch3_execution_receipt_kimi_2026_10_18.md`:824（＋0 件） | ②改指（候选：results___v3_v4_achievements_inventory_2026_09_24.md·近字节 194179） |
| `f6c67969b5ce` | — | 1 | 3192 | `_cleanup511_exec_register_2026_10_17.md`:302（＋0 件） | ①补正（补登现行真实指纹） |
| `f6d1473f1621` | — | 1 | 48525 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:196（＋0 件） | ①补正（补登现行真实指纹） |
| `f6e6bec76fc3` | — | 1 | 15049 | `_cleanup511_exec_register_2026_10_17.md`:274（＋0 件） | ①补正（补登现行真实指纹） |
| `f7ef3328ea71` | — | 1 | 2703 | `_supplement_execution_receipt_kimi_2026_10_18.md`:154（＋0 件） | ①补正（补登现行真实指纹） |
| `f7f39fb8549a` | _v3_v4_achievements_inventory_3dir_2026_09_2 | 1 | 355847 | `_batch3_execution_receipt_kimi_2026_10_18.md`:825（＋0 件） | ②改指（候选：_v3_v4_achievements_inventory_3dir_2026_09_24.md·近字节 355819） |
| `f83b2eb753ca` | — | 1 | 4676 | `_cleanup511_exec_register_2026_10_17.md`:444（＋0 件） | ①补正（补登现行真实指纹） |
| `f91db5974eb8` | — | 1 | 2369 | `_supplement_execution_receipt_kimi_2026_10_18.md`:117（＋0 件） | ①补正（补登现行真实指纹） |
| `f9cf85807a29` | — | 1 | 3113 | `_cleanup511_exec_register_2026_10_17.md`:354（＋0 件） | ①补正（补登现行真实指纹） |
| `f9d8c648881c` | — | 1 | 3875 | `_cleanup511_exec_register_2026_10_17.md`:381（＋0 件） | ①补正（补登现行真实指纹） |
| `fa35d870c9be` | — | 1 | 5568 | `_cleanup511_exec_register_2026_10_17.md`:277（＋0 件） | ①补正（补登现行真实指纹） |
| `fa7f38e7d882` | — | 1 | 6033 | `_cleanup511_exec_register_2026_10_17.md`:431（＋0 件） | ①补正（补登现行真实指纹） |
| `fabd6d7a9361` | — | 1 | 52274 | `_cleanup511_exec_register_2026_10_17.md`:387（＋0 件） | ①补正（补登现行真实指纹） |
| `fafe20311c7c` | — | 1 | 3652 | `_cleanup511_exec_register_2026_10_17.md`:174（＋0 件） | ①补正（补登现行真实指纹） |
| `fb2016c6f150` | REVIEWER_A_STATIC_AUDIT_2026_09_15.md | 1 | 34677 | `_batch3_execution_receipt_kimi_2026_10_18.md`:467（＋0 件） | ②改指（候选：REVIEWER_A_STATIC_AUDIT_2026_09_15.md·近字节 34647） |
| `fbe1a96a83cb` | — | 1 | 10257 | `_supplement_execution_receipt_kimi_2026_10_18.md`:333（＋0 件） | ①补正（补登现行真实指纹） |
| `fc536507a1d9` | — | 1 | 4233 | `_cleanup511_exec_register_2026_10_17.md`:83（＋0 件） | ①补正（补登现行真实指纹） |
| `fc74b59e22d5` | — | 1 | 12902 | `_batch3_execution_receipt_kimi_2026_10_18.md`:423（＋0 件） | ①补正（补登现行真实指纹） |
| `fc79964c1ea4` | 鲍勃_认证态仓态刷新_2026_10_18.md | 1 | 3317 | `_s14_session_scan_out_2026_10_21.md`:284（＋0 件） | ①补正（补登现行真实指纹） |
| `fcadc56979ce` | — | 1 | 36830 | `_supplement_execution_receipt_kimi_2026_10_18.md`:307（＋0 件） | ①补正（补登现行真实指纹） |
| `fd13418f5b9e` | — | 1 | 17550 | `_supplement_execution_receipt_kimi_2026_10_18.md`:201（＋0 件） | ①补正（补登现行真实指纹） |
| `fd895d6aa0ed` | — | 1 | 5453 | `_cleanup511_exec_register_2026_10_17.md`:96（＋0 件） | ①补正（补登现行真实指纹） |
| `fd9ddbe324c9` | — | 1 | 2728 | `_supplement_execution_receipt_kimi_2026_10_18.md`:217（＋0 件） | ①补正（补登现行真实指纹） |
| `fe55a6133d21` | — | 1 | 5401 | `_supplement_execution_receipt_kimi_2026_10_18.md`:259（＋0 件） | ①补正（补登现行真实指纹） |
| `fece5b1e3282` | — | 1 | 45172 | `_v4_checkpoint_atomic_and_pycache_2026_09_28.md`:232（＋0 件） | ①补正（补登现行真实指纹） |
| `ff36e30bd910` | — | 1 | 3437 | `_cleanup511_exec_register_2026_10_17.md`:407（＋0 件） | ①补正（补登现行真实指纹） |
| `ff37a1576b76` | — | 1 | 1678 | `_cleanup511_exec_register_2026_10_17.md`:290（＋0 件） | ①补正（补登现行真实指纹） |
| `ff5f068ce036` | — | 1 | 35868 | `_cleanup511_exec_register_2026_10_17.md`:140（＋0 件） | ①补正（补登现行真实指纹） |
| `ff8d328137da` | — | 1 | 5869 | `_batch3_execution_receipt_kimi_2026_10_18.md`:283（＋0 件） | ①补正（补登现行真实指纹） |
| `ffa8297e0fe5` | — | 1 | 8224 | `_cleanup511_exec_register_2026_10_17.md`:308（＋0 件） | ①补正（补登现行真实指纹） |
| `a75dbfff187e` | （冻结时点后并发棒新出件所引·本棒补扫） | 1 | 257,109 | `_v226_v230_adoption_effect_2026_10_22.md`（＋0 件） | ④登记挂账・候 PI 取回 |
| `af5d2e3832cc` | （冻结时点后并发棒新出件所引·本棒补扫） | 1 | 260,598 | `_v186_v225_adoption_effect_2026_10_22.md`（＋0 件） | ④登记挂账・候 PI 取回 |

**附**：上表末 2 件系**冻结时点（2026-10-22 00:55）之后**并发棒新出之 4 件所引，本棒作**补扫**（同法同仪器）后并入——补扫 75 对中 SHA-256 命中 71、域外 4、**真幽灵 2**（即此二）。

## §5 版本漂移型（31 件）

> 义：引文所指之旧指纹已 0 在盘，然**同名／近名之现行件在盘且字节相近**——实体并未灭失，系**版本漂移**，处置为「②改指（须先辨明同一性）」。
> **互斥口径**：本类仅取「旧侧 0 在盘（含域外面）且同名近字节之现行件在盘」者；其旧侧**本已在域外面**者归 §6「域外引用型」，于 §6 附注。**按唯一旧指纹计**（一旧指纹可对应多个近字节现行件，此处取字节差最小者）。

| 旧指纹 | 旧 bytes | 旧引次 | 现行指纹 | 现行 bytes | 名重合 | 字节差 | 现行件路径 |
|---|---|---|---|---|---|---|---|
| `9f383935c00c` | 29,570 | 131 | `78b71d404366` | 29,570 | 100% | 0.00% | `〔本地路径已脱敏〕` |
| `3af4695f09d7` | 4,892 | 3 | `c87a0c1f5af6` | 4,892 | 100% | 0.00% | `〔本地路径已脱敏〕` |
| `315a0850cdb8` | 21,710 | 1 | `8143d01ca0e1` | 21,710 | 100% | 0.00% | `〔幽灵引用·未上传:_e48_c4.md〕` |
| `37869b65d809` | 5,966 | 1 | `4d3cae4cbcc0` | 5,966 | 100% | 0.00% | `〔幽灵引用·未上传:_e48_c2.md〕` |
| `484c6f925f23` | 5,039 | 1 | `c2a814a90330` | 5,039 | 100% | 0.00% | `〔幽灵引用·未上传:_e48_c1.md〕` |
| `5bc66a934787` | 20,082 | 1 | `5198a7059c06` | 20,082 | 100% | 0.00% | `〔幽灵引用·未上传:review_content_A1_dsv4pro.md〕` |
| `5eb70737191d` | 13,607 | 1 | `1e6e30d4ce4d` | 13,607 | 100% | 0.00% | `〔幽灵引用·未上传:_e49_c1.md〕` |
| `6fc7d3931044` | 1,686 | 1 | `2f7ab971f691` | 1,686 | 100% | 0.00% | `〔幽灵引用·未上传:_e48_c5.md〕` |
| `745af537d3ee` | 4,892 | 1 | `c87a0c1f5af6` | 4,892 | 100% | 0.00% | `〔本地路径已脱敏〕` |
| `a0236cf328cd` | 18,923 | 1 | `09784ff172b3` | 18,923 | 100% | 0.00% | `〔幽灵引用·未上传:review_tech_B1_grok46.md〕` |
| `aa88e4d58193` | 6,563 | 1 | `769c71475404` | 6,563 | 100% | 0.00% | `〔幽灵引用·未上传:_e48_c3.md〕` |
| `abe5825a3324` | 8,098 | 1 | `8d00c6d4a242` | 8,098 | 100% | 0.00% | `〔幽灵引用·未上传:review_tech_B2_qwen3max.md〕` |
| `c187916dc13e` | 17,411 | 1 | `6f9b865280a3` | 17,411 | 100% | 0.00% | `〔幽灵引用·未上传:_v4_supp_t15r2_methodology_template.md〕` |
| `cf06b5f54185` | 17,872 | 1 | `11beaed14ea7` | 17,872 | 100% | 0.00% | `〔幽灵引用·未上传:_e49_c2.md〕` |
| `570aa07611f4` | 85,645 | 1 | `dc761bd8b85d` | 85,627 | 50% | 0.02% | `〔幽灵引用·未上传:_coze_paper_v1_双审报告_2026_09_17.md〕` |
| `4896fc796ed8` | 8,560 | 1 | `71d5c23d9f76` | 8,558 | 100% | 0.02% | `〔幽灵引用·未上传:_p_k_v3_glm_fpr_audit_report_2026-09-17T08-23-41Z.md〕` |
| `1f54a9822ce1` | 7,857 | 1 | `e240ca712be6` | 7,855 | 100% | 0.03% | `〔幽灵引用·未上传:_trae_d7_v1_audit_20260917_190000.md〕` |
| `30d89421bb45` | 13,600 | 1 | `05f92d837412` | 13,592 | 50% | 0.06% | `〔幽灵引用·未上传:_letter_to_kimi_push_v3_委托_2026_09_17.md〕` |
| `b05ff8152eee` | 16,904 | 1 | `6f3c550cec13` | 16,876 | 100% | 0.17% | `〔幽灵引用·未上传:P_E_DOUBAN_EMBEDDING_V0_SPEC.md〕` |
| `9bff09e32332` | 12,838 | 1 | `f4610b0bb47c` | 12,813 | 50% | 0.19% | `〔幽灵引用·未上传:_letter_to_coze_paper_v1_委托_2026_09_17.md〕` |
| `ed599f6c12fc` | 19,762 | 1 | `feae8af2fefe` | 19,716 | 100% | 0.23% | `〔本地路径已脱敏〕` |
| `3d3a40ce9676` | 31,315 | 1 | `59d8f56347d5` | 31,241 | 100% | 0.24% | `〔本地路径已脱敏〕` |
| `529f58459cf9` | 20,981 | 1 | `cce8e9a1b00e` | 20,927 | 100% | 0.26% | `〔本地路径已脱敏〕` |
| `2f906c2424cd` | 29,668 | 1 | `78b71d404366` | 29,570 | 100% | 0.33% | `〔本地路径已脱敏〕` |
| `2057eb16bc03` | 39,383 | 1 | `0397b757362f` | 39,206 | 100% | 0.45% | `〔本地路径已脱敏〕` |
| `5a0196ba7313` | 19,908 | 1 | `de90faf362c5` | 19,804 | 100% | 0.52% | `〔本地路径已脱敏〕` |
| `223297c38fb6` | 5,862 | 3 | `87563a63b854` | 5,830 | 100% | 0.55% | `〔本地路径已脱敏〕` |
| `71a17c0f1d74` | 5,862 | 1 | `87563a63b854` | 5,830 | 100% | 0.55% | `〔本地路径已脱敏〕` |
| `52c985429c91` | 55,352 | 7 | `3cb5c2f59961` | 54,377 | 100% | 1.76% | `〔幽灵引用·未上传:_v4_supp_t15_verdict.md〕` |
| `5c6d558fa400` | 652,755 | 38 | `57d56acb99f5` | 635,733 | 50% | 2.61% | `〔本地路径已脱敏〕` |
| `0410ca0fbdae` | 35,688 | 22 | `0397b757362f` | 39,206 | 100% | 8.97% | `〔本地路径已脱敏〕` |

## §6 域外引用型（16 件）

> 义：实体**在盘**，然落于四区之外（runtime `assets`／`plugin-cache` 面）。前件（10-21）之四区索引不涵此面，故其中 7 件曾被误列 MISS。

| 指纹 | 所载 bytes | 引次 | 实体实际路径（仓外） |
|---|---|---|---|
| `fd39cf811232` | 236,425 | 66 | `〔本地路径已脱敏〕`·236,425 B |
| `fed0262d707a` | 11,639 | 48 | `〔本地路径已脱敏〕`·11,639 B |
| `2befe7fc55bc` | 3,646 | 44 | `〔本地路径已脱敏〕`·3,646 B |
| `f71ae4210f50` | 9,385 | 26 | `〔本地路径已脱敏〕`·9,385 B |
| `0a314eed103a` | 13,044 | 23 | `〔本地路径已脱敏〕`·13,044 B |
| `62d03f6b5dfc` | 17,844 | 13 | `〔本地路径已脱敏〕`·17,844 B |
| `9845154a984c` | 68,553 | 13 | `〔本地路径已脱敏〕`·68,553 B |
| `ac74a04efeb2` | 7,183 | 13 | `〔本地路径已脱敏〕`·7,183 B |
| `809ab0c4164e` | 223,691 | 12 | `〔本地路径已脱敏〕`·223,691 B |
| `5ac65eacd107` | 11,227 | 8 | `〔本地路径已脱敏〕`·11,227 B |
| `907e616b45c9` | 14,935 | 8 | `〔本地路径已脱敏〕`·14,935 B |
| `6de42dd66f24` | 2,401 | 5 | `〔本地路径已脱敏〕`·2,401 B |
| `6f551e7ad761` | 2,621 | 5 | `〔本地路径已脱敏〕`·2,621 B |
| `31f4fb3c0df5` | 13,047 | 2 | `〔本地路径已脱敏〕`·13,047 B |
| `c6a91d35843e` | 5,920 | 2 | `〔本地路径已脱敏〕`·5,920 B |
| `23d90731e1fe` | 7,095 | 1 | `〔本地路径已脱敏〕`·7,095 B |

**附注一**：`fd39cf811232`（`查理_deposon双主线论文终稿_2026-10-01_v0.3.md`·236,425 B·runtime assets 面）之现行件 `8baa9854b3f7`·239,700 B 在 `deposon-repo\letters\`——**同一实体名、两个落位、两个指纹**（字节差 1.3%）。故其终态以**域外**记（旧侧落位已定），**漂移面另注于 §5 之互斥口径**。

**附注二**：本类另有 **0** 件之旧侧**本已在域外面**（故归本类而非 §5），其「同名近字节之现行件在盘」之漂移面逐条如下：

| 旧指纹 | 旧 bytes | 旧引次 | 现行指纹 | 现行 bytes | 名重合 | 字节差 | 现行件路径 |
|---|---|---|---|---|---|---|---|

## §7 口径型（1105 件）

> 义：实体**在盘**，然引文所载「SHA-12」实为 **SHA-1 git blob** 口径（`git hash-object` 之 `blob <size>\0<content>` 之 SHA-1 前 12 位），非 SHA-256。**此类非幽灵**，前件因只索引 SHA-256 而误列为 MISS。
> 阳性样例：`4fc0d746af9d`·105 B ＝ `deposon-repo\.gitignore`·105 B。

| 指纹 | 所载 bytes | 实体路径（三区） | 实体 bytes | 字节吻合 |
|---|---|---|---|---|
| `4fc0d746af9d` | 105 | `〔本地路径已脱敏〕` | 105 | ✅ |
| `b23ed435697e` | 91 | `〔幽灵引用·未上传:gitignore_sync_remote_old.txt〕` | 91 | ✅ |
| `79a41fc22dab` | 2,292 | `〔幽灵引用·未上传:_d05_sanity_3backbone_20260918_100110.json〕` | 2,292 | ✅ |
| `ffe1669dbf40` | 45,590 | `〔本地路径已脱敏〕` | 45,590 | ✅ |
| `ddd32d5b8398` | 2,568 | `〔幽灵引用·未上传:_recheck_r1_runC.log〕` | 2,568 | ✅ |
| `eeb137ee0997` | 2,634 | `〔幽灵引用·未上传:_recheck_r1_runA.log〕` | 2,634 | ✅ |
| `3ef2e8075f1b` | 21,654 | `〔幽灵引用·未上传:REVIEWER_B_TMP_RERUN_2026_09_15.md〕` | 21,654 | ✅ |
| `a2989b1b5b26` | 18,514 | `〔幽灵引用·未上传:_v5_glm_charlie_reread_ac74a04efeb2_2026_09_29.md〕` | 18,514 | ✅ |
| `aa13f2945e85` | 19,709 | `〔幽灵引用·未上传:_v5_b17_three_caliber_fixation_2026_09_29.md〕` | 19,709 | ✅ |
| `aa3a94399724` | 5,131 | `〔幽灵引用·未上传:_v4_tmp_cleanup_2026_09_28.md〕` | 5,131 | ✅ |
| `cf395fdb3282` | 23,023 | `〔幽灵引用·未上传:_v5_b14_r3_anchor_retrieval_2026_09_29.md〕` | 23,023 | ✅ |
| `e454eb83619f` | 1,155 | `〔幽灵引用·未上传:_verify_worker_c.py〕` | 1,155 | ✅ |
| `01059346371f` | 17,647 | `〔幽灵引用·未上传:docs__V3X__P_F_RESEARCH_2026_09_09.md〕` | 17,647 | ✅ |
| `025c158f7feb` | 11,256 | `〔幽灵引用·未上传:deposon_team___designs__V3X_TEAM_IMPROVEMENT_PLAN_2026_09_16.md〕` | 11,256 | ✅ |
| `04b5307e1392` | 15,375 | `〔幽灵引用·未上传:docs__V3X__V3X_DAILY_KILL_V2_PLAN.md〕` | 15,375 | ✅ |
| `0819ac19f2e1` | 34,653 | `〔幽灵引用·未上传:results___gate1_five_zero_recheck_glm_scope_2026_10_13.md〕` | 34,653 | ✅ |
| `085fbf7cd9aa` | 17,532 | `〔幽灵引用·未上传:results___theory_boundary_clone_sync_register_2026_10_09.md〕` | 17,532 | ✅ |
| `0be54db0d1ea` | 169,884 | `〔幽灵引用·未上传:results___v3_v4_ghostref_reconciliation_2026_09_23.md〕` | 169,884 | ✅ |
| `0da3bc43cd7c` | 7,348 | `〔幽灵引用·未上传:docs__V3X__V7_§3_P_C_P_E_GRAY_NOTE_2026_09_11.md〕` | 7,348 | ✅ |
| `0da60b9a1de6` | 24,835 | `〔幽灵引用·未上传:results___d8_supplement_open_questions_2026_09_30.md〕` | 24,835 | ✅ |
| `0debb6baba97` | 8,554 | `〔幽灵引用·未上传:docs__V3X__V3X_1WEEK_KILL_REPORT_2026_09_18.md〕` | 8,554 | ✅ |
| `0e3f19a48a69` | 13,135 | `〔幽灵引用·未上传:docs__V3X__P_E_D1_D3_REPORT_2026_09_15.md〕` | 13,135 | ✅ |
| `0e617b1f4efc` | 56,901 | `〔幽灵引用·未上传:pi_rulings___pi_card_answers_register_2026_10_17_v87.md〕` | 56,901 | ✅ |
| `0f94a003dbb9` | 7,839 | `〔幽灵引用·未上传:results___v4_gA1_experiment_outline_2026_09_22.md〕` | 7,839 | ✅ |
| `12eeed4c5426` | 6,279 | `〔幽灵引用·未上传:results___pre_execution_report_kimi_2026_10_01.md〕` | 6,279 | ✅ |
| `1507a17b2448` | 49,256 | `〔幽灵引用·未上传:results___kd_s3b1_kd1_n7_rulings_effect_2026_10_17.md〕` | 49,256 | ✅ |
| `1517f0249d63` | 48,280 | `〔幽灵引用·未上传:results___theory_input_request_supplement_2026_09_29.md〕` | 48,280 | ✅ |
| `17f590a839a5` | 12,302 | `〔幽灵引用·未上传:results___v5_confirm_b11_decisions_register_2026_09_29.md〕` | 12,302 | ✅ |
| `17fb4ef17572` | 15,622 | `〔幽灵引用·未上传:results__deposon_pa_d1_d3_2026_09_15.json〕` | 15,622 | ✅ |
| `1ab497ffcf5e` | 25,568 | `〔幽灵引用·未上传:results___exp05_missing_true_disposition_judgment_2026_10_10.md〕` | 25,568 | ✅ |
| `1b145eded648` | 48,972 | `〔幽灵引用·未上传:results___v5_clearance_o15_ready_pack_2026_09_29.md〕` | 48,972 | ✅ |
| `1b17763e4fc7` | 11,495 | `〔幽灵引用·未上传:results___archive_2026_09_18___trae_5audit_aggregated_2026_09_17.md〕` | 11,495 | ✅ |
| `1b1f027db264` | 52,655 | `〔幽灵引用·未上传:results___s4_heldout_sampling_seedthird_extractor_2026_10_11.py〕` | 52,655 | ✅ |
| `1b916be2cd26` | 49,998 | `〔幽灵引用·未上传:pi_rulings___pi_card_answers_register_2026_10_17_v83.md〕` | 49,998 | ✅ |
| `20cedf10c2f5` | 31,106 | `〔幽灵引用·未上传:results___unclosed_47_direct_clear_b_tier_register_2026_10_13.md〕` | 31,106 | ✅ |
| `22fde9ae557b` | 10,600 | `〔幽灵引用·未上传:results___temp_cleanup_register_2026_10_13.md〕` | 10,600 | ✅ |
| `2440a613ed72` | 12,616 | `〔幽灵引用·未上传:docs__V3X__P_F_D1_REPORT_2026_09_15.md〕` | 12,616 | ✅ |
| `27523eab8450` | 21,764 | `〔幽灵引用·未上传:docs__V3X__D5_DECISIONS_LAND_REPORT_2026_09_15.md〕` | 21,764 | ✅ |
| `2a1f389a4d99` | 1,063 | `〔幽灵引用·未上传:results___kimi_push_v3_manifest_batch14_e5952130.json〕` | 1,063 | ✅ |
| `2a9a263e2ffc` | 5,055 | `〔幽灵引用·未上传:verifier__handoff__KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json〕` | 5,055 | ✅ |
| `2d360c03f4d1` | 1,039 | `〔幽灵引用·未上传:results___r5_spec_pack_retrieved_2026_10_13__鲍勃_minimax实验委托规格包_2026_10_12.md.asset.json〕` | 1,039 | ✅ |
| `2f115c9a6662` | 22,187 | `〔幽灵引用·未上传:results___v5_v4_proposal_23item_merged_catalogue_sourceverify_2026_09_29.md〕` | 22,187 | ✅ |
| `2f1b9580912e` | 12,338 | `〔幽灵引用·未上传:deposon_team___designs__EXTERNAL_AGENT_PROMPTS_2026_09_16.md〕` | 12,338 | ✅ |
| `3305435b7d67` | 49,028 | `〔幽灵引用·未上传:results___batch8_deliberation_judgment_2026_10_14.md〕` | 49,028 | ✅ |
| `36aaab76914d` | 5,775 | `〔幽灵引用·未上传:results___v3x_p_l_v3_external_spec_2026_09_17.md〕` | 5,775 | ✅ |
| `37a49fbe40b0` | 36,629 | `〔幽灵引用·未上传:results___batch9_deliberation_judgment_2026_10_14.md〕` | 36,629 | ✅ |
| `38246f705a64` | 24,824 | `〔幽灵引用·未上传:results___v4_group_b_17letters_judgment_draft_2026_09_22.md〕` | 24,824 | ✅ |
| `3adf056b6c80` | 2,811 | `〔幽灵引用·未上传:Deposon_评估汇总_v1_3_0.json〕` | 2,811 | ✅ |
| `3baf552bab87` | 7,366 | `〔幽灵引用·未上传:docs__V3X__D_FIX2_METRIC_VERIFY_REPORT_2026_09_15.md〕` | 7,366 | ✅ |
| `3e6459931d3f` | 14,499 | `〔幽灵引用·未上传:results___clue_side_dual_and_glm_commission_open_register_2026_10_12.md〕` | 14,499 | ✅ |
| `3f455a73da77` | 34,025 | `〔幽灵引用·未上传:results___v5_confirm_b3_decisions_register_2026_09_29.md〕` | 34,025 | ✅ |
| `3f4c25025250` | 12,928 | `〔幽灵引用·未上传:docs__V3X__V3X_PROJECT_EVOLUTION_FOR_KIMI.md〕` | 12,928 | ✅ |
| `40ff107b5181` | 12,523 | `〔幽灵引用·未上传:docs__V3X__P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md〕` | 12,523 | ✅ |
| `4133b3599fd3` | 46,163 | `〔幽灵引用·未上传:results___supplement_to_500_design_review_2026_10_16.md〕` | 46,163 | ✅ |
| `43ef77ff0939` | 20,119 | `〔幽灵引用·未上传:results___ftfb_v3_pass1_audit_2026_09_18_corrected.md〕` | 20,119 | ✅ |
| `455a9f62453b` | 7,639 | `〔幽灵引用·未上传:results___v3x_d0_5_experiment_invitation_2026_09_17.md〕` | 7,639 | ✅ |
| `47787a82029d` | 13,204 | `〔幽灵引用·未上传:results___v3x_d0_5_proposal_coze_2026_09_17.md〕` | 13,204 | ✅ |
| `4790cc6fde8a` | 6,339 | `〔幽灵引用·未上传:results___p_l_v3_phase3_plus_adendum_7_report_20260917_133512.md〕` | 6,339 | ✅ |
| `47f13ee7d3ba` | 26,219 | `〔幽灵引用·未上传:results___collision_baseline_update_and_disposition_2026_10_17.md〕` | 26,219 | ✅ |
| `48ea4e6774c3` | 725,689 | `〔幽灵引用·未上传:results___zone_balance_inventory_2026_10_13.md〕` | 725,689 | ✅ |
| `491f4338aeeb` | 10,989 | `〔幽灵引用·未上传:results___external_letters_two_generation_values_note_2026_10_01.md〕` | 10,989 | ✅ |
| `497d2a008357` | 5,529 | `〔幽灵引用·未上传:deposon_team__plugins__boss_pg_3_geodesic_violation.py〕` | 5,529 | ✅ |
| `4a33af111f0f` | 7,398 | `〔幽灵引用·未上传:audits_dataset_health.json〕` | 7,398 | ✅ |
| `4ac42cc84dac` | 12,689 | `〔幽灵引用·未上传:deposon_team___designs__D7_PRE_DISPATCH_EXECUTION_REPORT_2026_09_16.md〕` | 12,689 | ✅ |
| `4b72a49b9221` | 50,425 | `〔幽灵引用·未上传:results___noncore_upload_caliber_effect_register_2026_10_17.md〕` | 50,425 | ✅ |
| `4cc87c0abd0b` | 5,444 | `〔幽灵引用·未上传:results___r2_execution_receipt_kimi_2026_10_12.md〕` | 5,444 | ✅ |
| `4e262d90f4ca` | 37,446 | `〔幽灵引用·未上传:results___kt_a1_anchor_drift_root_cause_2026_10_14.md〕` | 37,446 | ✅ |
| `4f3916a0596d` | 1,694 | `〔幽灵引用·未上传:verifier__v41__check.sh〕` | 1,694 | ✅ |
| `4f92d3020764` | 4,042 | `〔幽灵引用·未上传:results___archive_2026_09_18___trae_paper_8ch_双审_20260917_200000.md〕` | 4,042 | ✅ |
| `515954f5c09f` | 10,974 | `〔幽灵引用·未上传:docs__V3X__BOSS_URL_DUE_DILIGENCE_2026_09_11.md〕` | 10,974 | ✅ |
| `524651e929bf` | 6,618 | `〔幽灵引用·未上传:results___p_l_v3_phase3_plus_adendum_7_report_20260917_133852.md〕` | 6,618 | ✅ |
| `52a3d1e8be7b` | 11,041 | `〔幽灵引用·未上传:results___p_l_v3_phase1_report_20260917_132341.md〕` | 11,041 | ✅ |
| `5302dfea87da` | 15,107 | `〔幽灵引用·未上传:docs__V3X__QUICK_KILL_6_DIRECTIONS.md〕` | 15,107 | ✅ |
| `5644406f7355` | 150,967 | `〔幽灵引用·未上传:results___v5_sub_artifact_ledger_history_r2_2026_09_29.md〕` | 150,967 | ✅ |
| `56568828a7bc` | 29,511 | `〔幽灵引用·未上传:results___coze_paper_v1_draft_2026_09_17.md〕` | 29,511 | ✅ |
| `5a33f2c079c6` | 32,408 | `〔幽灵引用·未上传:results___d8_boundary_revision_register_2026_09_30.md〕` | 32,408 | ✅ |
| `5b89369890ee` | 217,655 | `〔幽灵引用·未上传:results___r2_build_manifest_2026_10_12.json〕` | 217,655 | ✅ |
| `5d4875397a9f` | 17,738 | `〔幽灵引用·未上传:results__deposon_v3_physical_opt_60cells_2026_09_11.json〕` | 17,738 | ✅ |
| `5d822b49bbc8` | 30,235 | `〔幽灵引用·未上传:results___unclosed_items_inventory_2026_10_08.md〕` | 30,235 | ✅ |
| `6188dbda5e77` | 33,779 | `〔幽灵引用·未上传:pi_rulings___pi_card_answers_register_2026_10_17_v80.md〕` | 33,779 | ✅ |
| `62910e2b2dff` | 64,396 | `〔幽灵引用·未上传:pi_rulings___pi_card_answers_register_2026_10_17_v46.md〕` | 64,396 | ✅ |
| `6396645627f1` | 72,381 | `〔幽灵引用·未上传:pi_rulings___pi_card_answers_register_2026_10_17_v54.md〕` | 72,381 | ✅ |
| `65cc3eaa19f6` | 8,352 | `〔幽灵引用·未上传:results__deposon_3risk_v0_fixes_2026_09_11.json〕` | 8,352 | ✅ |
| `69fa556aa47a` | 19,614 | `〔幽灵引用·未上传:docs__THINKING_V3_GT_CONTRIB_2026.md〕` | 19,614 | ✅ |
| `6b412b2a8c5a` | 12,642 | `〔幽灵引用·未上传:results___stage3_completion_and_stage4_open_register_2026_10_12.md〕` | 12,642 | ✅ |
| `6c291f7574b6` | 31,437 | `〔幽灵引用·未上传:results___v5_item21_rerun_conditions_prereg_2026_09_28.md〕` | 31,437 | ✅ |
| `6cab8f3ed1e8` | 14,986 | `〔幽灵引用·未上传:results___v5_clearance_mr11_doc_calibration_2026_09_29.md〕` | 14,986 | ✅ |
| `6ee482285e78` | 28,163 | `〔幽灵引用·未上传:results___v5_item21_verdict_2026_09_28.md〕` | 28,163 | ✅ |
| `6f4b25cca87b` | 17,091 | `〔幽灵引用·未上传:results__deposon_pe_d1_d3_2026_09_15.json〕` | 17,091 | ✅ |
| `70b0915abdbc` | 7,729 | `〔幽灵引用·未上传:results___pre_execution_report_kimi_2026_10_12.md〕` | 7,729 | ✅ |
| `75600d25d0a0` | 7,990 | `〔幽灵引用·未上传:.trae__audit__compare_versions.py〕` | 7,990 | ✅ |
| `75fb0b94f171` | 51,364 | `〔幽灵引用·未上传:pi_rulings___pi_card_answers_register_2026_10_17_v85.md〕` | 51,364 | ✅ |
| `775144c54f1b` | 8,740 | `〔幽灵引用·未上传:deposon_team___designs__V3X_CLOSURE_REPORT_REQUIREMENTS_FOR_EXTERNAL_AGENT.md〕` | 8,740 | ✅ |
| `79bddad30c1d` | 29,961 | `〔幽灵引用·未上传:results___trae_issues_batch3_six_items_draft_2026_10_12.md〕` | 29,961 | ✅ |
| `816d56eeb283` | 19,777 | `〔幽灵引用·未上传:docs__V3X__P_A_D1_D3_REPORT_2026_09_15.md〕` | 19,777 | ✅ |
| `81afead5bd49` | 12,504 | `〔幽灵引用·未上传:verifier__handoff__P_F_PREDECISION_2026_09_11_V0.1.json〕` | 12,504 | ✅ |
| `8427f472ce39` | 38,280 | `〔幽灵引用·未上传:results___ge01_d1_theory_input_sourcing_design_2026_10_14.md〕` | 38,280 | ✅ |
| `847cee4f1ba8` | 9,576 | `〔幽灵引用·未上传:results___v3x_p_l_v3_summary_mistral_large_2512_20260917_115049.md〕` | 9,576 | ✅ |
| `85f4334d29be` | 10,371 | `〔幽灵引用·未上传:docs__V3X__P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md〕` | 10,371 | ✅ |
| `8764166830d0` | 16,396 | `〔幽灵引用·未上传:docs__V3X_COLLAB_DIRECTIONS.md〕` | 16,396 | ✅ |
| `8927d7c3cee1` | 14,622 | `〔幽灵引用·未上传:results___v3_recheck_21_rescript_2026_09_27.md〕` | 14,622 | ✅ |
| `8b7c48eea3da` | 25,138 | `〔幽灵引用·未上传:results___c4_theory_source_caliber_correction_2026_09_30.md〕` | 25,138 | ✅ |
| `8dc82b7c3c0f` | 11,800 | `〔幽灵引用·未上传:results___pi_batch_rulings_and_gate1_definition_register_2026_10_12.md〕` | 11,800 | ✅ |
| `8df74e7345ab` | 13,568 | `〔幽灵引用·未上传:results__deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json〕` | 13,568 | ✅ |
| `8f3a3743c8ac` | 20,994 | `〔幽灵引用·未上传:results___p0_scan_2026_10_12.json〕` | 20,994 | ✅ |
| `8f44312eeae7` | 39,041 | `〔幽灵引用·未上传:pi_rulings___pi_card_answers_register_2026_10_17_v86.md〕` | 39,041 | ✅ |
| `909fabce2d8b` | 17,813 | `〔幽灵引用·未上传:docs__V3X__DEPOSON_EMBEDDING_6WAY_VERIFICATION_2026_09_10.md〕` | 17,813 | ✅ |
| `90e26e14f4fd` | 5,942 | `〔幽灵引用·未上传:docs__V3X__D7_GITHUB_PUSH_RECEIVE_2026_09_15_v2.md〕` | 5,942 | ✅ |
| `9172d0748ed3` | 45,862 | `〔幽灵引用·未上传:results___kd_s3b1_verdict_2026_10_17.md〕` | 45,862 | ✅ |
| `92ee1bf107cd` | 16,252 | `〔幽灵引用·未上传:volcengine_补测_worker_A_2026_09_10.py〕` | 16,252 | ✅ |
| `948ae3ece224` | 450,701 | `〔幽灵引用·未上传:results___v3_recheck_05_result_2026_09_28.json〕` | 450,701 | ✅ |
| `9502b9beaf9f` | 160,625 | `〔幽灵引用·未上传:results___root_session_history_memo_main_2026_10_14.md〕` | 160,625 | ✅ |
| `969470464033` | 14,626 | `〔幽灵引用·未上传:results___v5_v4_proposal_23item_merged_catalogue_2026_09_29.md〕` | 14,626 | ✅ |
| `98b60214583e` | 20,422 | `〔幽灵引用·未上传:results__deposon_pc_d1_d3_2026_09_15.json〕` | 20,422 | ✅ |
| `995354ff82be` | 13,431 | `〔幽灵引用·未上传:docs__V3X__P_C_D1_D3_REPORT_2026_09_15.md〕` | 13,431 | ✅ |
| `9b5bbb811a91` | 38,553 | `〔幽灵引用·未上传:docs__V3X__V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md〕` | 38,553 | ✅ |
| `9b5ea1432a1c` | 9,062 | `〔幽灵引用·未上传:results___p_l_v3_phase2_report_20260917_142748.md〕` | 9,062 | ✅ |
| `9dd3cea98340` | 13,299 | `〔幽灵引用·未上传:docs__V3X__RISK3_V0_FIXES_2026_09_11.md〕` | 13,299 | ✅ |
| `a1b52ba63522` | 15,501 | `〔幽灵引用·未上传:docs__V3X__P_G_V01_REPORT_2026_09_15.md〕` | 15,501 | ✅ |
| `a26392eb0e96` | 10,952 | `〔幽灵引用·未上传:deposon_team___designs__V3X_KIMI_7_DIRECTIONS_FULL_ACCEPT_2026_09_16.md〕` | 10,952 | ✅ |
| `a401d4a2b4d5` | 61,343 | `〔幽灵引用·未上传:results___unclosed_47_pi_give_draft_2026_10_13.md〕` | 61,343 | ✅ |
| `a732da6d363a` | 51,656 | `〔幽灵引用·未上传:results___github_suspect_rulings_effect_2026_10_17.md〕` | 51,656 | ✅ |
| `aa33183b3cae` | 6,436 | `〔幽灵引用·未上传:results___p_l_v3_phase3_plus_adendum_7_report_20260917_133705.md〕` | 6,436 | ✅ |
| `aa3da939a79c` | 19,774 | `〔幽灵引用·未上传:results___v4_gA3_seeds_judgment_draft_2026_09_22.md〕` | 19,774 | ✅ |
| `ab901b9a72ef` | 12,861 | `〔幽灵引用·未上传:results___trae_issues_disposition_schedule_2026_10_12.md〕` | 12,861 | ✅ |
| `ac783f124570` | 6,437 | `〔幽灵引用·未上传:results___p_l_v3_phase3_plus_adendum_7_report_20260917_133726.md〕` | 6,437 | ✅ |
| `acb25540ac22` | 372,346 | `〔幽灵引用·未上传:results___achievements_inventory_full_2026_10_09.md〕` | 372,346 | ✅ |
| `b43ea3881756` | 47,751 | `〔幽灵引用·未上传:pi_rulings___pi_card_answers_register_2026_10_17_v82.md〕` | 47,751 | ✅ |
| `b83ad0fd3517` | 11,018 | `〔幽灵引用·未上传:results__skill_d_p_f_observer_result_2026_09_11.json〕` | 11,018 | ✅ |
| `b85cd41cbd73` | 31,855 | `〔幽灵引用·未上传:results___kt_a1_v0_lineage_corrigendum_2026_10_14.md〕` | 31,855 | ✅ |
| `b891bb4004c6` | 10,734 | `〔幽灵引用·未上传:docs__V3X__D7_PRE_V3_POLISH_AND_TEAM_IMPROVEMENT_2026_09_16.md〕` | 10,734 | ✅ |
| `bc57b2d877a6` | 6,325 | `〔幽灵引用·未上传:docs__V3X__P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md〕` | 6,325 | ✅ |
| `bcdfdbb0940a` | 8,646 | `〔幽灵引用·未上传:results___gate_one_reopened_and_stage2_rejection_register_2026_10_12.md〕` | 8,646 | ✅ |
| `c06b707cb516` | 12,016 | `〔幽灵引用·未上传:results___v3x_d0_5_aggregation_2026_09_17.md〕` | 12,016 | ✅ |
| `c0d7213a09fa` | 26,713 | `〔本地路径已脱敏〕` | 26,713 | ✅ |
| `c3634de6f3fd` | 18,209 | `〔幽灵引用·未上传:results___clearance_evening_round_register_2026_09_29.md〕` | 18,209 | ✅ |
| `c4e7a025ab3b` | 9,281 | `〔幽灵引用·未上传:docs__V3X__TRAE_3RISK_FIX_REPORT_2026_09_16.md〕` | 9,281 | ✅ |
| `c4ed04fd18fa` | 32,352 | `〔幽灵引用·未上传:results___d8_dup_overlap_disposal_2026_09_30.md〕` | 32,352 | ✅ |
| `c68062107ee4` | 51,671 | `〔幽灵引用·未上传:pi_rulings___pi_card_answers_register_2026_10_17_v81.md〕` | 51,671 | ✅ |
| `c703e9611da8` | 62,893 | `〔幽灵引用·未上传:results___stage3_r2_cleanup_register_2026_10_18.md〕` | 62,893 | ✅ |
| `c7f2a4404206` | 9,914 | `〔幽灵引用·未上传:docs__V3X__D0_FREEZE_PREP_2026_09_09.md〕` | 9,914 | ✅ |
| `c8331b3a63c0` | 75,241 | `〔幽灵引用·未上传:results___upload_side_desensitized_remote_sha_letter_kimi_2026_10_12.md〕` | 75,241 | ✅ |
| `c8de825f3391` | 33,633 | `〔幽灵引用·未上传:results___refcheck_hash_change_reference_recheck_2026_09_30.md〕` | 33,633 | ✅ |
| `ca0ffb87f97b` | 11,526 | `〔幽灵引用·未上传:results__deposon_pg_v01_9m60c_2026_09_15.json〕` | 11,526 | ✅ |
| `ca6633580c8c` | 29,501 | `〔幽灵引用·未上传:results___noncore_upload_caliber_draft_2026_10_17.md〕` | 29,501 | ✅ |
| `cb06e4e5292a` | 6,639 | `〔幽灵引用·未上传:results___p_l_v3_phase3_plus_adendum_7_report_20260917_133358.md〕` | 6,639 | ✅ |
| `cf1f3d2f858c` | 15,549 | `〔幽灵引用·未上传:docs__V3X__P_B_DISTORTION_BOUND_V0_SPEC.md〕` | 15,549 | ✅ |
| `d03126028128` | 18,923 | `〔幽灵引用·未上传:results___s4_heldout_sampling_seedprime_extractor_2026_10_10.py〕` | 18,923 | ✅ |
| `d1462f7a0baf` | 11,091 | `〔幽灵引用·未上传:docs__V3X__BOSS_PE_3_RESERVOIR_VERIFY_REPORT_2026_09_15.md〕` | 11,091 | ✅ |
| `d1f45c8fb34f` | 23,027 | `〔幽灵引用·未上传:docs__V3X__P_F_IMPLEMENTATION_2026_09_11.md〕` | 23,027 | ✅ |
| `d5f27db26e9a` | 22,764 | `〔幽灵引用·未上传:results___itemH_fingerprint_provenance_2026_10_12.md〕` | 22,764 | ✅ |
| `da84d81aa976` | 12,908 | `〔幽灵引用·未上传:deposon_team___designs__V3X_FULL_CLOSEOUT_REPORT_2026_09_16.md〕` | 12,908 | ✅ |
| `dac61c7effde` | 22,455 | `〔幽灵引用·未上传:docs__V3X__V3X_FULL_EXPERIMENT_DESIGN_2026_09_16.md〕` | 22,455 | ✅ |
| `db57fcae77b1` | 4,892 | `〔本地路径已脱敏〕` | 4,892 | ✅ |
| `dc9183d82725` | 24,814 | `〔幽灵引用·未上传:docs__V3X__V3X_D6_PAPER_V2_2026_09_09_mavis.md〕` | 24,814 | ✅ |
| `de3da25bc7a8` | 53,583 | `〔幽灵引用·未上传:results___v4_pi_cot_v3_questionnaire_v2_d8_2026_09_28.md〕` | 53,583 | ✅ |
| `de51c39ddedc` | 6,868 | `〔幽灵引用·未上传:docs__V3X__BPA_PILOT_2026_09_09_mavis.md〕` | 6,868 | ✅ |
| `df3149a13a5d` | 36,286 | `〔幽灵引用·未上传:results___ge01_d1_theory_input_disposition_2026_10_14.md〕` | 36,286 | ✅ |
| `e0a794481e41` | 5,297 | `〔幽灵引用·未上传:deposon_team__plugins__boss_pg_2_hyperbolic_classification_collapse.py〕` | 5,297 | ✅ |
| `e15cac5d6ab4` | 27,153 | `〔幽灵引用·未上传:results___kd1_preexp_contrast_2026_10_17.md〕` | 27,153 | ✅ |
| `e16d2a5f8ecd` | 6,479 | `〔幽灵引用·未上传:docs__V3X__D7_ONE_PAGE_SUMMARY_2026_09_11_v5.md〕` | 6,479 | ✅ |
| `e90fe5903e28` | 7,176 | `〔幽灵引用·未上传:results___pulled_back_P_B_DISTORTION_BOUND_V0_SPEC_2026_10_13.md〕` | 7,176 | ✅ |
| `e9d4379d24b3` | 24,851 | `〔幽灵引用·未上传:results___r5_spec_pack_retrieval_register_2026_10_13.md〕` | 24,851 | ✅ |
| `ed36772f3efe` | 25,319 | `〔幽灵引用·未上传:results___ge01_unblock_progress_2026_10_14.md〕` | 25,319 | ✅ |
| `ef0f17c3f2be` | 9,513 | `〔幽灵引用·未上传:results___kimi_push_v3_manifest_batch5_34439e1e.json〕` | 9,513 | ✅ |
| `f0c93a1f65c2` | 18,135 | `〔幽灵引用·未上传:results___ge01_spec_anchor_erratum_2026_10_14.md〕` | 18,135 | ✅ |
| `f32b043fd6e4` | 3,241 | `〔幽灵引用·未上传:deposon_team__plugins__git_commit_msg_2026_09_18.txt〕` | 3,241 | ✅ |
| `f4dbf7158e55` | 6,012 | `〔幽灵引用·未上传:deposon_team__plugins__boss_pg_1_riemannian_degenerate.py〕` | 6,012 | ✅ |
| `f61a9452e2c8` | 6,805 | `〔幽灵引用·未上传:deposon_team___designs__V3X_PATCH_5ANCHOR_RECONCILE_V2_2026_09_17.md〕` | 6,805 | ✅ |
| `f6b73a4b8228` | 44,782 | `〔幽灵引用·未上传:results___two_items_alternative_deliberation_judgment_2026_10_13.md〕` | 44,782 | ✅ |
| `f78b5f420d57` | 6,362 | `〔幽灵引用·未上传:docs__V3X__KT_D0_EVIDENCE_CARD.md〕` | 6,362 | ✅ |
| `f86ca7abd474` | 35,690 | `〔幽灵引用·未上传:results___archive_2026_09_20___archive_manifest_2026_09_20.json〕` | 35,690 | ✅ |
| `f9beac73eef9` | 3,690 | `〔幽灵引用·未上传:verifier__handoff__P_F_PREDECISION_2026_09_09.json〕` | 3,690 | ✅ |
| `fa634919ff9e` | 4,843 | `〔幽灵引用·未上传:results___upload_execution_receipt_kimi_2026_10_12.md〕` | 4,843 | ✅ |
| `fc1fac3d9898` | 5,582 | `〔幽灵引用·未上传:results___v5_handover_guide_project_initiation_2026_10_12.md〕` | 5,582 | ✅ |
| `fcc9e3a4ac13` | 33,680 | `〔幽灵引用·未上传:pi_rulings___pi_card_answers_register_2026_10_17_v72.md〕` | 33,680 | ✅ |
| `0020de27f803` | 3,221 | `〔幽灵引用·未上传:tmp_movedout_2026_09_28___cleanup_transfer_scan_2026_09_28.py〕` | 3,221 | ✅ |
| `004e79c610af` | 7,863 | `〔幽灵引用·未上传:results___archive_2026_09_18___trae_d7_v1_audit_20260917_190000.md〕` | 7,863 | ✅ |
| `00a219feb86a` | 32,822 | `〔本地路径已脱敏〕` | 32,822 | ✅ |
| `00a941c68be1` | 13,828 | `〔幽灵引用·未上传:results___clearance_round_1_register_2026_10_08.md〕` | 13,828 | ✅ |
| `015bc8dd1609` | 20,969 | `〔本地路径已脱敏〕` | 20,969 | ✅ |
| `030801392946` | 8,536 | `〔幽灵引用·未上传:results___p_k_v3_glm_fpr_audit_report_2026-09-17T08-23-41Z.md〕` | 8,536 | ✅ |
| `034f84aec0e5` | 33,964 | `〔幽灵引用·未上传:results___p_refresh_scope_judgment_2026_10_10.md〕` | 33,964 | ✅ |
| `040718619f7b` | 22,646 | `〔幽灵引用·未上传:_s4_heldout_sampling_seedthird_items_register_2026_10_11.md〕` | 22,646 | ✅ |
| `0467038c016f` | 1,247 | `〔幽灵引用·未上传:deposon_v2_phase3_f3_2026_09_11.log〕` | 1,247 | ✅ |
| `06662bff1840` | 17,373 | `〔幽灵引用·未上传:_vk_face_category_erratum_2026_10_11.md〕` | 17,373 | ✅ |
| `066c6f031ba0` | 66,582 | `〔幽灵引用·未上传:results___root_session_history_memo_2026_10_14.md〕` | 66,582 | ✅ |
| `06c54e651f5d` | 5,458 | `〔幽灵引用·未上传:_d05_sanity_3backbone_2026_09_18.py〕` | 5,458 | ✅ |
| `06c7ada9fbb1` | 41,409 | `〔幽灵引用·未上传:results___p_refresh_s0_judgment_2026_10_10.md〕` | 41,409 | ✅ |
| `07747d9019e7` | 59,309 | `〔本地路径已脱敏〕` | 59,309 | ✅ |
| `0778f4b25bf6` | 15,118 | `〔幽灵引用·未上传:results___v5_confirm_b8_decisions_register_2026_09_29.md〕` | 15,118 | ✅ |
| `0952adb63097` | 2,342 | `〔幽灵引用·未上传:_p_l_v3_phase2_closedsource_runner_v2_20260917_175003_gemini_37flash.log〕` | 2,342 | ✅ |
| `096c001f92ca` | 33,741 | `〔幽灵引用·未上传:results__deposon_pf_d1_full_9m5c_2026_09_15.json〕` | 33,741 | ✅ |
| `0a2b396958c4` | 41,412 | `〔幽灵引用·未上传:results___typeb_m_definition_judgment_2026_10_10.md〕` | 41,412 | ✅ |
| `0a3362018856` | 40,499 | `〔本地路径已脱敏〕` | 40,499 | ✅ |
| `0aa61e767615` | 42,311 | `〔幽灵引用·未上传:results___f3_definition_deep_judgment_2026_10_11.md〕` | 42,311 | ✅ |
| `0b07905291dc` | 77,137 | `〔幽灵引用·未上传:results___round56_review_effectivity_register_3_2026_10_10.md〕` | 77,137 | ✅ |
| `0b57f4096b3f` | 49,109 | `〔幽灵引用·未上传:_stage3_trigger_recheck_2026_10_11.md〕` | 49,109 | ✅ |
| `0c646c01d983` | 33,936 | `〔幽灵引用·未上传:results___g5_x4_dual_axis_interpretation_judgment_2026_10_10.md〕` | 33,936 | ✅ |
| `0c943bbf536b` | 45,911 | `〔本地路径已脱敏〕` | 45,911 | ✅ |
| `0dd53df5dccb` | 22,591 | `〔幽灵引用·未上传:results___archive_2026_09_20___letter_to_kimi_upload_requirements_2026_09_18.md〕` | 22,591 | ✅ |
| `0de951feb9f3` | 262,560 | `〔幽灵引用·未上传:results___questionnaire_cards_intake_register_supplement_2_2026_10_10.md〕` | 262,560 | ✅ |
| `0f1d1f80230f` | 22,328 | `〔幽灵引用·未上传:results___suspect17_release_move_register_2026_10_09.md〕` | 22,328 | ✅ |
| `0f34b6d8b8e6` | 204,236 | `〔幽灵引用·未上传:results___archive_manifest_non_upload_v3_2026_09_28.json〕` | 204,236 | ✅ |
| `0f61665cb8ea` | 47,107 | `〔本地路径已脱敏〕` | 47,107 | ✅ |
| `0fc49c17205b` | 20,420 | `〔幽灵引用·未上传:results___g4_reproduction_execution_register_2026_10_09.md〕` | 20,420 | ✅ |
| `10ca088d9ce1` | 34,165 | `〔幽灵引用·未上传:results___round56_g2_enable_and_v1_rule_register_2026_10_10.md〕` | 34,165 | ✅ |
| `10e844e84dad` | 1,508 | `〔幽灵引用·未上传:_cpath_sim_run_2026_09_10.log〕` | 1,508 | ✅ |
| `10eb0a5e9649` | 24,819 | `〔本地路径已脱敏〕` | 24,819 | ✅ |
| `11f8befcefa3` | 67,613 | `〔幽灵引用·未上传:_round56_review_effectivity_register_5_2026_10_11.md〕` | 67,613 | ✅ |
| `1228f05a235e` | 24,795 | `〔幽灵引用·未上传:_vk_current_counting_face_2026_10_10.md〕` | 24,795 | ✅ |
| `1293be908983` | 32,815 | `〔幽灵引用·未上传:_g5_ccp_execution_prereqs_2026_10_10.md〕` | 32,815 | ✅ |
| `131d0e0d0636` | 67,225 | `〔幽灵引用·未上传:_questionnaire_cards_intake_register_supplement_3_2026_10_10.md〕` | 67,225 | ✅ |
| `139831d429c6` | 10,899 | `〔幽灵引用·未上传:_tdf_s2_apply_2026_10_12.py〕` | 10,899 | ✅ |
| `139986b64f9c` | 39,879 | `〔幽灵引用·未上传:results___s3prime_degeneracy_selfcert_2026_10_11.md〕` | 39,879 | ✅ |
| `13c4094f2053` | 62,308 | `〔幽灵引用·未上传:results___kj1_eps_ls_effectivity_register_2026_10_11.md〕` | 62,308 | ✅ |
| `141f9a6f7450` | 26,296 | `〔幽灵引用·未上传:results___e6_n_distinct_judge_types_recompute_2026_10_10.md〕` | 26,296 | ✅ |
| `1449fe1ab5df` | 49,698 | `〔幽灵引用·未上传:results___round56r9r10_dispositions_register_2026_10_10.md〕` | 49,698 | ✅ |
| `14a461780763` | 21,826 | `〔幽灵引用·未上传:results___s4_seedprime_inheldout_recompute_2026_10_10.md〕` | 21,826 | ✅ |
| `15295e3eeb26` | 77,181 | `〔幽灵引用·未上传:_round56_review_effectivity_register_3_2026_10_10.md〕` | 77,181 | ✅ |
| `1631ae2d6777` | 27,470 | `〔幽灵引用·未上传:results___c_component4_d2d3_gap_judgment_2026_10_11.md〕` | 27,470 | ✅ |
| `16a34c3ae004` | 17,632 | `〔幽灵引用·未上传:_p_l_v3_phase2_probe_emb_proxy_v2.log〕` | 17,632 | ✅ |
| `173e51260711` | 42,351 | `〔本地路径已脱敏〕` | 42,351 | ✅ |
| `1762d338a1c9` | 21,572 | `〔本地路径已脱敏〕` | 21,572 | ✅ |
| `18aa51927654` | 5,856 | `〔幽灵引用·未上传:_tdf_s1_2026_10_12.py〕` | 5,856 | ✅ |
| `19b47d140045` | 16,724 | `〔幽灵引用·未上传:results___three_pending_items_effectivity_2026_10_11.md〕` | 16,724 | ✅ |
| `19e035b669d0` | 1,224 | `〔幽灵引用·未上传:_p_l_v3_phase2_finalize_20260917_142748.log〕` | 1,224 | ✅ |
| `19fea1e0e3e8` | 72,217 | `〔幽灵引用·未上传:results___questionnaire_cards_intake_register_supplement_2026_10_09.md〕` | 72,217 | ✅ |
| `1a098d388a6e` | 1,184 | `〔幽灵引用·未上传:_p_l_v3_phase1_finalize.log〕` | 1,184 | ✅ |
| `1a434dd57eb3` | 11,488 | `〔幽灵引用·未上传:results___exp05_negative_probe_rescan_2026_10_10.md〕` | 11,488 | ✅ |
| `1ad43c70cf01` | 106,453 | `〔幽灵引用·未上传:_questionnaire_cards_intake_register_supplement_6_2026_10_10.md〕` | 106,453 | ✅ |
| `1b693dec8fea` | 34,681 | `〔幽灵引用·未上传:results___s4_heldout_sampling_seed42_items_register_2026_10_09.md〕` | 34,681 | ✅ |
| `1b86970816da` | 6,106 | `〔幽灵引用·未上传:_v41_flash_rag_baseline_run.log.bak〕` | 6,106 | ✅ |
| `1b8daf6983d7` | 28,378 | `〔幽灵引用·未上传:_round56_th3_coverage_line_effectivity_register_2026_10_10.md〕` | 28,378 | ✅ |
| `1ba293951b31` | 85,863 | `〔幽灵引用·未上传:results___s4_substrate_topup_addendum_2026_10_09.json〕` | 85,863 | ✅ |
| `1d0857087ccf` | 29,938 | `〔本地路径已脱敏〕` | 29,938 | ✅ |
| `1d66f37a9e8e` | 20,518 | `〔幽灵引用·未上传:results___v4_group_b_explore_subs_integration_2026_09_22.md〕` | 20,518 | ✅ |
| `1dea5a7f30f7` | 38,231 | `〔幽灵引用·未上传:_s4_source_wave_mapping_registration_2026_10_10.md〕` | 38,231 | ✅ |
| `1e8427ebf11c` | 41,580 | `〔本地路径已脱敏〕` | 41,580 | ✅ |
| `1e9cbb33d96d` | 11,139 | `〔幽灵引用·未上传:results___stage_sequence_violation_register_2026_10_12.md〕` | 11,139 | ✅ |
| `1f182b639d5e` | 28,217 | `〔幽灵引用·未上传:results___round56_th4_two_field_reporting_resolution_2026_10_10.md〕` | 28,217 | ✅ |
| `1fd9e231650b` | 24,453 | `〔幽灵引用·未上传:_v4_closeout_account_reconciliation_2026_10_12.md〕` | 24,453 | ✅ |
| `1ff6f03a1c96` | 76,910 | `〔幽灵引用·未上传:_s6doubleprime_terminal_verdicts_2026_10_11.md〕` | 76,910 | ✅ |
| `203d3ee799ba` | 19,678 | `〔幽灵引用·未上传:tmp_movedout_2026_10_09__uncertain_release_2026_09___v5_b17_three_caliber_fixation_2026_09_29.md〕` | 19,678 | ✅ |
| `20f29e21c80c` | 24,710 | `〔幽灵引用·未上传:results___t1_exp2_activation_supplement_2026_10_09.md〕` | 24,710 | ✅ |
| `217b7f46438f` | 34,004 | `〔本地路径已脱敏〕` | 34,004 | ✅ |
| `219b55f758e9` | 33,504 | `〔本地路径已脱敏〕` | 33,504 | ✅ |
| `21e8e42f284f` | 45,304 | `〔幽灵引用·未上传:results___krj5_subject_scope_judgment_2026_10_11.md〕` | 45,304 | ✅ |
| `223e30582ee0` | 43,448 | `〔本地路径已脱敏〕` | 43,448 | ✅ |
| `2257524856ca` | 32,886 | `〔幽灵引用·未上传:_fp3_anchor_and_krj_restrament_register_2026_10_11.md〕` | 32,886 | ✅ |
| `2292a3044e55` | 16,523 | `〔幽灵引用·未上传:.trae__scripts___arxiv_renumber.py〕` | 16,523 | ✅ |
| `22c18e6d3604` | 12,813 | `〔幽灵引用·未上传:results___archive_2026_09_20___letter_to_coze_paper_v1_委托_2026_09_17.md〕` | 12,813 | ✅ |
| `22d2c1d03065` | 27,853 | `〔幽灵引用·未上传:results___v4_maindir_cleanup_manifest_v2_2026_09_26.md〕` | 27,853 | ✅ |
| `23265fc6acf4` | 21,166 | `〔幽灵引用·未上传:_e6_j5_semantics_erratum_note_2026_10_10.md〕` | 21,166 | ✅ |
| `238be5a072c6` | 40,253 | `〔幽灵引用·未上传:_round56_typeb_backfill_register_2026_10_10.md〕` | 40,253 | ✅ |
| `23d65bf5e9fd` | 25,029 | `〔幽灵引用·未上传:results___round56_gu_backdoor_exclusion_revision_2026_10_10.md〕` | 25,029 | ✅ |
| `249c30c031d3` | 84,422 | `〔幽灵引用·未上传:_questionnaire_cards_intake_register_supplement_9_2026_10_10.md〕` | 84,422 | ✅ |
| `251e2eb167c2` | 49,013 | `〔幽灵引用·未上传:_round56_review_effectivity_register_2026_10_10.md〕` | 49,013 | ✅ |
| `2536948d64ee` | 39,385 | `〔幽灵引用·未上传:docs__V3X__KT_B1_SPEC_V0.1.md〕` | 39,385 | ✅ |
| `25829e1b7260` | 27,364 | `〔幽灵引用·未上传:_c4_unblock_reply_independent_review_2026_10_10.md〕` | 27,364 | ✅ |
| `262ac921c4b0` | 11,921 | `〔幽灵引用·未上传:results___exp08_s4_prompt_face_register_2026_10_10.md〕` | 11,921 | ✅ |
| `26aaf47192de` | 95,619 | `〔幽灵引用·未上传:results___krj_all_terminal_verdicts_2026_10_11.md〕` | 95,619 | ✅ |
| `2724e195ef58` | 26,304 | `〔幽灵引用·未上传:_e6_n_distinct_judge_types_recompute_2026_10_10.md〕` | 26,304 | ✅ |
| `27ca82578a29` | 51,688 | `〔幽灵引用·未上传:results___three_pending_items_drafts_2026_10_11.md〕` | 51,688 | ✅ |
| `280a921dea9a` | 21,865 | `〔本地路径已脱敏〕` | 21,865 | ✅ |
| `281a81f02a88` | 12,926 | `〔幽灵引用·未上传:_codex_c4_values_reply_intake_register_2026_10_10.md〕` | 12,926 | ✅ |
| `289e897f3a07` | 25,042 | `〔幽灵引用·未上传:results__deposon_v3_v7_summary_2026_09_11.json〕` | 25,042 | ✅ |
| `28b94277ca51` | 139,983 | `〔幽灵引用·未上传:results___v4_design_integration_2026_09_21_v1.1.md〕` | 139,983 | ✅ |
| `294752c30345` | 67,227 | `〔幽灵引用·未上传:results___questionnaire_cards_intake_register_supplement_3_2026_10_10.md〕` | 67,227 | ✅ |
| `29be716acfa5` | 41,432 | `〔本地路径已脱敏〕` | 41,432 | ✅ |
| `2a19e1aaf1b8` | 36,799 | `〔幽灵引用·未上传:results___kj4_e4_unification_judgment_2026_10_11.md〕` | 36,799 | ✅ |
| `2a498e82f9f4` | 43,332 | `〔幽灵引用·未上传:_five_items_effectivity_register_2026_10_11.md〕` | 43,332 | ✅ |
| `2b5128e0a098` | 1,516 | `〔幽灵引用·未上传:_p_l_v3_phase2_closedsource_runner_v2_20260917_171640.log〕` | 1,516 | ✅ |
| `2bbf169f9be6` | 32,762 | `〔幽灵引用·未上传:results___s7doubleprime_verification_erratum_2026_10_11.md〕` | 32,762 | ✅ |
| `2c56d7b3835a` | 46,119 | `〔幽灵引用·未上传:results___round56r8_dispositions_register_2026_10_10.md〕` | 46,119 | ✅ |
| `2cd63dba3bb8` | 47,185 | `〔幽灵引用·未上传:results___s5prime_lim_a_and_item_registers_2026_10_11.md〕` | 47,185 | ✅ |
| `2d7b322065d2` | 35,217 | `〔幽灵引用·未上传:results___s4_open_questions_addendum_2026_10_09.json〕` | 35,217 | ✅ |
| `2df029e81991` | 5,848 | `〔幽灵引用·未上传:deposon_team__plugins___tdf_s1_2026_10_12.py〕` | 5,848 | ✅ |
| `2e563e9fd165` | 17,705 | `〔幽灵引用·未上传:deposon_team__plugins__boss_pa_1_rbr_rm.py〕` | 17,705 | ✅ |
| `2e5b3c200544` | 3,462 | `〔幽灵引用·未上传:_p_l_v3_phase2_probe_gpt4o.log〕` | 3,462 | ✅ |
| `2f5edcac6a91` | 1,678 | `〔幽灵引用·未上传:_v3x_6way_stage3_minimal.log〕` | 1,678 | ✅ |
| `2f749d7d1457` | 22,999 | `〔幽灵引用·未上传:results___receipt_disposition_register_2026_10_08.md〕` | 22,999 | ✅ |
| `2feaa54a9800` | 33,152 | `〔幽灵引用·未上传:results___cleanup_round_2026_10_08.md〕` | 33,152 | ✅ |
| `302b47c9138b` | 37,615 | `〔幽灵引用·未上传:_s4_heldout_sampling_seed42_register_2026_10_09.md〕` | 37,615 | ✅ |
| `303659550a1b` | 6,134 | `〔幽灵引用·未上传:_p_l_v3_phase2_vector_emb_doubao_2026_09_17.console.log〕` | 6,134 | ✅ |
| `3077f29a3205` | 16,900 | `〔幽灵引用·未上传:docs__V3X__P_E_DOUBAN_EMBEDDING_V0_SPEC.md〕` | 16,900 | ✅ |
| `30cb0056be0a` | 16,441 | `〔幽灵引用·未上传:_b01_recompute_sec4_2_erratum_2026_10_10.md〕` | 16,441 | ✅ |
| `3136a2fcae1c` | 20,414 | `〔幽灵引用·未上传:_g4_reproduction_execution_register_2026_10_09.md〕` | 20,414 | ✅ |
| `3193804b4aaf` | 34,913 | `〔幽灵引用·未上传:_round55_dispositions_register_2026_10_10.md〕` | 34,913 | ✅ |
| `319c77148b2c` | 24,783 | `〔幽灵引用·未上传:_s4_seedprime_seq_t1_only_supplement_2026_10_11.md〕` | 24,783 | ✅ |
| `31d356a8ff63` | 20,926 | `〔幽灵引用·未上传:results___archive_ledger_rectification_register_2026_10_09.md〕` | 20,926 | ✅ |
| `3239456c7c9e` | 54,883 | `〔幽灵引用·未上传:_questionnaire_cards_intake_register_supplement_14_2026_10_11.md〕` | 54,883 | ✅ |
| `325b927ceea6` | 53,188 | `〔幽灵引用·未上传:_s3prime_alert_disposition_judgment_2026_10_11.md〕` | 53,188 | ✅ |
| `32d25d82a584` | 50,222 | `〔本地路径已脱敏〕` | 50,222 | ✅ |
| `330cf31449c0` | 29,620 | `〔幽灵引用·未上传:_b14_audit_f2f3_closure_register_2026_10_11.md〕` | 29,620 | ✅ |
| `33b19246feb9` | 76,850 | `〔幽灵引用·未上传:results___s6doubleprime_terminal_verdicts_2026_10_11.md〕` | 76,850 | ✅ |
| `343ba0d8fc9d` | 38,032 | `〔本地路径已脱敏〕` | 38,032 | ✅ |
| `345608fea302` | 9,232 | `〔幽灵引用·未上传:_d05_main_runner_20260918.log〕` | 9,232 | ✅ |
| `35309e81bd0a` | 591,773 | `〔幽灵引用·未上传:results___repo_full_inventory_catalogue_2026_10_12.md〕` | 591,773 | ✅ |
| `35362d1a6671` | 10,702 | `〔幽灵引用·未上传:results___archive_2026_09_20___letter_to_trae_code_2026_09_17_final.md〕` | 10,702 | ✅ |
| `3565dd4edb1c` | 9,037 | `〔幽灵引用·未上传:deposon_team__plugins__skill_a_p_a_60cells.py〕` | 9,037 | ✅ |
| `3638e15133ac` | 30,662 | `〔幽灵引用·未上传:_g4_e3_definition_ruling_material_2026_10_09.md〕` | 30,662 | ✅ |
| `36c7b38ca540` | 18,568 | `〔幽灵引用·未上传:_v4_closeout_moves_and_cleanup_register_2026_10_12.md〕` | 18,568 | ✅ |
| `37a856ff5782` | 29,991 | `〔本地路径已脱敏〕` | 29,991 | ✅ |
| `37ab9642da7b` | 22,104 | `〔幽灵引用·未上传:_b01_p_counting_recompute_2026_10_10.md〕` | 22,104 | ✅ |
| `37c28c9d515a` | 22,820 | `〔幽灵引用·未上传:results___archive_2026_09_20__LETTER_TO_TRAE_2026_09_11.md〕` | 22,820 | ✅ |
| `3889af913d4c` | 11,338 | `〔幽灵引用·未上传:results___e2_glm2_distill_side_receipt_register_2026_10_09.md〕` | 11,338 | ✅ |
| `388ef92900f2` | 31,004 | `〔幽灵引用·未上传:_round56_b01_followup_disposition_plan_2026_10_10.md〕` | 31,004 | ✅ |
| `3989ef97bfb1` | 20,949 | `〔幽灵引用·未上传:results___u6_negative_delta_compatibility_2026_10_11.md〕` | 20,949 | ✅ |
| `3a31f5d7ad13` | 15,551 | `〔幽灵引用·未上传:results___thv3_15_parallel_seed_double_note_2026_10_11.md〕` | 15,551 | ✅ |
| `3a50cef82902` | 34,181 | `〔幽灵引用·未上传:_round56_g2_enable_and_v1_rule_register_2026_10_10.md〕` | 34,181 | ✅ |
| `3a5af3e5448e` | 35,425 | `〔幽灵引用·未上传:_p_l_v3_phase1_runner_2026_09_17.py〕` | 35,425 | ✅ |
| `3a8b5c22f5e3` | 43,202 | `〔幽灵引用·未上传:results___round56_direct_adoptions_register_2026_10_10.md〕` | 43,202 | ✅ |
| `3b894f46c3d1` | 29,019 | `〔幽灵引用·未上传:_round56_pending_questions_compilation_supplement_note_2026_10_10.md〕` | 29,019 | ✅ |
| `3bb2b5bc9289` | 26,864 | `〔幽灵引用·未上传:_seed_double_identifier_finalization_2026_10_11.md〕` | 26,864 | ✅ |
| `3bf750dc3f8b` | 27,272 | `〔幽灵引用·未上传:results__deposon_pf_implementation_2026_09_11.json〕` | 27,272 | ✅ |
| `3c2dd5f7c0ab` | 8,098 | `〔幽灵引用·未上传:review_tech_B2_qwen3max.md〕` | 8,098 | ✅ |
| `3c8a0039b3c4` | 27,490 | `〔本地路径已脱敏〕` | 27,490 | ✅ |
| `3caf22fa7486` | 13,865 | `〔幽灵引用·未上传:_stage3_open_and_mandate_register_2026_10_12.md〕` | 13,865 | ✅ |
| `3cb86ea403ad` | 12,870 | `〔幽灵引用·未上传:deposon_team__plugins__boss_pa_3_replicator_dynamics.py〕` | 12,870 | ✅ |
| `3cbc03448af2` | 33,867 | `〔幽灵引用·未上传:results___f4_direction1_seed_and_domain_draft_2026_10_11.md〕` | 33,867 | ✅ |
| `3d38e496a803` | 12,447 | `〔幽灵引用·未上传:_commission_closeout_erratum_and_supplement_2026_10_11.md〕` | 12,447 | ✅ |
| `3d3a6b8994db` | 8,578 | `〔幽灵引用·未上传:deposon_v2_phase1_60cells_2026_09_11.log〕` | 8,578 | ✅ |
| `3df594818649` | 8,257 | `〔幽灵引用·未上传:results___archive_2026_09_20__ftfb_pass1_background_methodology_audit_2026_09_17.md〕` | 8,257 | ✅ |
| `3f3a8d002a47` | 35,711 | `〔幽灵引用·未上传:_stage3_trigger_readings_2026_10_11.md〕` | 35,711 | ✅ |
| `3f6a88210fb2` | 21,552 | `〔幽灵引用·未上传:results___u3_carrier_qid_verification_2026_10_11.md〕` | 21,552 | ✅ |
| `3fbba85846d8` | 33,444 | `〔幽灵引用·未上传:results___round56_pending_questions_compilation_2026_10_10.md〕` | 33,444 | ✅ |
| `408fb37dfc15` | 15,803 | `〔幽灵引用·未上传:results___stage3_1_bulk_reorg_completion_register_2026_10_12.md〕` | 15,803 | ✅ |
| `40932e5803d0` | 23,453 | `〔幽灵引用·未上传:_round56_v4_kd_row_correction_revision_2026_10_10.md〕` | 23,453 | ✅ |
| `40b387aed7af` | 16,064 | `〔幽灵引用·未上传:_krj_five_verdicts_adjudication_2026_10_11.md〕` | 16,064 | ✅ |
| `414410f8c677` | 23,014 | `〔本地路径已脱敏〕` | 23,014 | ✅ |
| `414aeeaaf803` | 27,680 | `〔幽灵引用·未上传:deposon_team__plugins__runner_pa_d1_d3.py〕` | 27,680 | ✅ |
| `41c763713c1a` | 51,748 | `〔本地路径已脱敏〕` | 51,748 | ✅ |
| `41eba7b8f98b` | 1,272 | `〔幽灵引用·未上传:deposon_v2_phase2_f2_2026_09_11.log〕` | 1,272 | ✅ |
| `42c9d2e4a9ea` | 9,068 | `〔幽灵引用·未上传:_volc_22cap_emb.log〕` | 9,068 | ✅ |
| `42cc96d0683f` | 57,185 | `〔本地路径已脱敏〕` | 57,185 | ✅ |
| `42dc9efce725` | 15,304 | `〔幽灵引用·未上传:results___v4_maindir_count_monitor_2026_09_27.md〕` | 15,304 | ✅ |
| `42e99a1c5aa4` | 77,193 | `〔幽灵引用·未上传:results___questionnaire_cards_intake_register_supplement_5_2026_10_10.md〕` | 77,193 | ✅ |
| `431f998079cb` | 20,086 | `〔本地路径已脱敏〕` | 20,086 | ✅ |
| `437f828e6dbd` | 34,908 | `〔幽灵引用·未上传:results___chd_construction_domain_declaration_draft_2026_10_10.md〕` | 34,908 | ✅ |
| `43a3c50882d4` | 48,028 | `〔幽灵引用·未上传:results___f3_new_definition_draft_2026_10_11.md〕` | 48,028 | ✅ |
| `43f36a646019` | 50,329 | `〔幽灵引用·未上传:results___round56a_dispositions_register_2026_10_10.md〕` | 50,329 | ✅ |
| `441b199e098c` | 442,352 | `〔幽灵引用·未上传:results___questionnaire_cards_intake_register_2026_10_09.md〕` | 442,352 | ✅ |
| `44660f750727` | 15,526 | `〔幽灵引用·未上传:results___krj_cond4_effectivity_declaration_2026_10_11.md〕` | 15,526 | ✅ |
| `44d0481664e4` | 19,910 | `〔幽灵引用·未上传:docs__V3X__P_F_SPEC_V0.md〕` | 19,910 | ✅ |
| `44ed4e1dbd49` | 28,886 | `〔本地路径已脱敏〕` | 28,886 | ✅ |
| `4544e99386d7` | 42,266 | `〔幽灵引用·未上传:results___plan_v3_pending_verify_2026_09_30.md〕` | 42,266 | ✅ |
| `45fe997ff1e4` | 24,162 | `〔幽灵引用·未上传:results___codex_c4_values_followup_reply_intake_register_2026_10_10.md〕` | 24,162 | ✅ |
| `461124b1c8bb` | 31,549 | `〔幽灵引用·未上传:results___v4_maindir_cleanup_moves_ledger_v3_2026_09_24.md〕` | 31,549 | ✅ |
| `467ace4389f7` | 46,261 | `〔幽灵引用·未上传:_e6_th_v3_19_residual_exits_judgment_2026_10_10.md〕` | 46,261 | ✅ |
| `46ab58f5894e` | 17,574 | `〔幽灵引用·未上传:rescript_2026_09_27.md〕` | 17,574 | ✅ |
| `46ee8668402e` | 55,341 | `〔幽灵引用·未上传:_questionnaire_cards_intake_register_supplement_11_2026_10_10.md〕` | 55,341 | ✅ |
| `471b37678096` | 15,889 | `〔幽灵引用·未上传:deposon_team__plugins__skill_d_p_f_observer.py〕` | 15,889 | ✅ |
| `47a10d98edae` | 39,939 | `〔幽灵引用·未上传:_s3prime_degeneracy_selfcert_2026_10_11.md〕` | 39,939 | ✅ |
| `484df38a6e46` | 20,892 | `〔幽灵引用·未上传:results___archive_2026_09_18___trae_code_improvement_v2_2026_09_18.md〕` | 20,892 | ✅ |
| `487e281745b8` | 45,167 | `〔幽灵引用·未上传:results___g5_krj9_denominator_reconciliation_judgment_2026_10_10.md〕` | 45,167 | ✅ |
| `48bc160b3265` | 55,102 | `〔本地路径已脱敏〕` | 55,102 | ✅ |
| `48e3ca1d1ccf` | 10,380 | `〔幽灵引用·未上传:deposon_team__plugins__boss_pa_2_potential_game.py〕` | 10,380 | ✅ |
| `490aa8148a87` | 50,365 | `〔幽灵引用·未上传:_round56a_dispositions_register_2026_10_10.md〕` | 50,365 | ✅ |
| `4992c2b84c99` | 41,708 | `〔幽灵引用·未上传:_s3prime_recompute_after_supplement_2026_10_11.md〕` | 41,708 | ✅ |
| `4a2cb20f948f` | 33,786 | `〔幽灵引用·未上传:results___v5_b12_verify_pack_q1_q3_q4_2026_09_29.md〕` | 33,786 | ✅ |
| `4a85ae03c395` | 72,199 | `〔幽灵引用·未上传:_questionnaire_cards_intake_register_supplement_2026_10_09.md〕` | 72,199 | ✅ |
| `4a89109b9893` | 39,505 | `〔幽灵引用·未上传:results___a02_excluded_items_idx_collection_2026_10_10.md〕` | 39,505 | ✅ |
| `4a8e99afdf6d` | 11,336 | `〔幽灵引用·未上传:_e2_glm2_distill_side_receipt_register_2026_10_09.md〕` | 11,336 | ✅ |
| `4b1c32665b9c` | 41,636 | `〔幽灵引用·未上传:_md_trigger_prereg_effectivity_2026_10_11.md〕` | 41,636 | ✅ |
| `4b82a9671d6e` | 18,916 | `〔幽灵引用·未上传:results___u_cf_category_caliber_2026_10_10.md〕` | 18,916 | ✅ |
| `4bfc21e8edfc` | 148,670 | `〔幽灵引用·未上传:results___archive_manifest_non_upload_2026_09_23.json〕` | 148,670 | ✅ |
| `4c4a1d6f60f5` | 38,624 | `〔幽灵引用·未上传:results___f4_direction1_prereq_check_2026_10_11.md〕` | 38,624 | ✅ |
| `4c5d5368aa76` | 12,759 | `〔幽灵引用·未上传:results___u_closure_execution_register_2026_10_09.md〕` | 12,759 | ✅ |
| `4cb29bc0fce1` | 4,992 | `〔幽灵引用·未上传:_p_l_v3_phase2_probe_ext.log〕` | 4,992 | ✅ |
| `4d37c7e75106` | 16,105 | `〔幽灵引用·未上传:_q3_c1c4_l282_transposition_fix_applied_note_2026_10_09.md〕` | 16,105 | ✅ |
| `4d449dc4acd8` | 54,937 | `〔幽灵引用·未上传:_s6prime_terminal_verdicts_2026_10_11.md〕` | 54,937 | ✅ |
| `4de1a9c448f7` | 6,514 | `〔幽灵引用·未上传:deposon_deepseek_v41_flash_30cells_2026_09_10.log〕` | 6,514 | ✅ |
| `4e3fef8ea6ec` | 2,707 | `〔幽灵引用·未上传:tmp_movedout_2026_09_28___cleanup_resolve_2026_09_28.py〕` | 2,707 | ✅ |
| `4ebeea7caa2f` | 54,475 | `〔幽灵引用·未上传:results___pi_effectivity_declaration_register_2026_10_11.md〕` | 54,475 | ✅ |
| `4edd37d18fbc` | 1,270 | `〔幽灵引用·未上传:_tmp_probe_archive〕` | 1,270 | ✅ |
| `4fe0eef8bd7d` | 3,229 | `〔幽灵引用·未上传:_cleanup_transfer_scan_2026_09_28.py〕` | 3,229 | ✅ |
| `4ffa7c767bef` | 20,710 | `〔幽灵引用·未上传:volcengine_glm_latest_30cells_v2_runner_2026_09_10.py〕` | 20,710 | ✅ |
| `500d1c84f2e0` | 57,145 | `〔幽灵引用·未上传:results___seed_double_rule_judgment_2026_10_11.md〕` | 57,145 | ✅ |
| `505d7e1dd421` | 24,755 | `〔幽灵引用·未上传:results___vk_current_counting_face_2026_10_10.md〕` | 24,755 | ✅ |
| `5118e6894251` | 67,575 | `〔幽灵引用·未上传:results___round56_review_effectivity_register_5_2026_10_11.md〕` | 67,575 | ✅ |
| `5140616c2035` | 84,127 | `〔幽灵引用·未上传:_questionnaire_cards_intake_register_supplement_10_2026_10_10.md〕` | 84,127 | ✅ |
| `5142c8d4461a` | 56,984 | `〔幽灵引用·未上传:results___g5_rejudgment_construction_change_plan_2026_10_10.md〕` | 56,984 | ✅ |
| `51527925597f` | 25,638 | `〔幽灵引用·未上传:results___u_cf_reclassification_2026_10_10.md〕` | 25,638 | ✅ |
| `516c6ea1c749` | 38,664 | `〔本地路径已脱敏〕` | 38,664 | ✅ |
| `51ee08ae73cf` | 38,211 | `〔幽灵引用·未上传:results___s4_source_wave_mapping_registration_2026_10_10.md〕` | 38,211 | ✅ |
| `5200924444b7` | 23,437 | `〔幽灵引用·未上传:results___round56_v4_kd_row_correction_revision_2026_10_10.md〕` | 23,437 | ✅ |
| `52335388369a` | 20,690 | `〔幽灵引用·未上传:docs__V3X__REVIEWER_A_TRAE_FIX_AUDIT_2026_09_15.md〕` | 20,690 | ✅ |
| `5267d1048a6e` | 2,046 | `〔幽灵引用·未上传:_p_l_v3_phase2_probe_emb.log〕` | 2,046 | ✅ |
| `5274aee17142` | 9,396 | `〔幽灵引用·未上传:tmp_movedout_2026_10_09__uncertain_release_2026_09___asset_recount_2026_09_30.md〕` | 9,396 | ✅ |
| `52d072ec0343` | 12,595 | `〔本地路径已脱敏〕` | 12,595 | ✅ |
| `52f5f0dd8a8c` | 53,125 | `〔幽灵引用·未上传:_mini_round_5_decisions_register_2026_10_01.md〕` | 53,125 | ✅ |
| `531018438e42` | 11,159 | `〔幽灵引用·未上传:_stage_sequence_violation_register_2026_10_12.md〕` | 11,159 | ✅ |
| `5332c33c3466` | 24,107 | `〔幽灵引用·未上传:results___archive_2026_09_24___worker_openrouter_rag_run.py〕` | 24,107 | ✅ |
| `5376f4aae453` | 77,189 | `〔幽灵引用·未上传:_questionnaire_cards_intake_register_supplement_5_2026_10_10.md〕` | 77,189 | ✅ |
| `53fa9d2e5398` | 31,317 | `〔幽灵引用·未上传:docs__V3X__KT_C1_SPEC_V0.1.md〕` | 31,317 | ✅ |
| `54842032466d` | 15,194 | `〔幽灵引用·未上传:results___krj_pi_picks_adoption_krj6_revise_2026_10_11.md〕` | 15,194 | ✅ |
| `54c4f808cd15` | 6,760 | `〔幽灵引用·未上传:_p_l_v3_phase2_probe_agent.log〕` | 6,760 | ✅ |
| `556bdc0a5670` | 11,929 | `〔幽灵引用·未上传:_exp08_s4_prompt_face_register_2026_10_10.md〕` | 11,929 | ✅ |
| `56b4aa16d2e2` | 19,901 | `〔幽灵引用·未上传:_p_l_v3_phase2_finalize_2026_09_17.py〕` | 19,901 | ✅ |
| `57bde656f762` | 30,472 | `〔幽灵引用·未上传:results___e4_lineage_conflict_correction_2026_10_11.md〕` | 30,472 | ✅ |
| `580177f1eb35` | 33,586 | `〔幽灵引用·未上传:_b14_vk_evidence_audit_2026_10_10.md〕` | 33,586 | ✅ |
| `584717acd90e` | 27,674 | `〔幽灵引用·未上传:results___e6_j5_semantics_conflict_judgment_2026_10_10.md〕` | 27,674 | ✅ |
| `5872e85049bf` | 44,199 | `〔幽灵引用·未上传:_s4_corpus_scope_hard_constraint_judgment_2026_10_10.md〕` | 44,199 | ✅ |
| `5876b6b8d617` | 35,344 | `〔幽灵引用·未上传:_overnight_delivery_index_2026_10_10.md〕` | 35,344 | ✅ |
| `59026ae97582` | 17,501 | `〔幽灵引用·未上传:results___questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md〕` | 17,501 | ✅ |
| `5908015bb22a` | 8,056 | `〔幽灵引用·未上传:deposon_team__plugins___tdf_s1b_2026_10_12.py〕` | 8,056 | ✅ |
| `5a15b031e42e` | 45,871 | `〔幽灵引用·未上传:results___ftfb_order_judgment_2026_10_11.md〕` | 45,871 | ✅ |
| `5a6919ccc9b6` | 12,070 | `〔幽灵引用·未上传:deposon_volcengine_worker_c_2026_09_10.run.log〕` | 12,070 | ✅ |
| `5adc81e60162` | 39,870 | `〔幽灵引用·未上传:_g11_krj4_effectivity_register_2026_10_11.md〕` | 39,870 | ✅ |
| `5b975ed206a5` | 36,787 | `〔本地路径已脱敏〕` | 36,787 | ✅ |
| `5c05888226a8` | 18,923 | `〔幽灵引用·未上传:review_tech_B1_grok46.md〕` | 18,923 | ✅ |
| `5c7cb610a8c7` | 34,897 | `〔幽灵引用·未上传:results___round55_dispositions_register_2026_10_10.md〕` | 34,897 | ✅ |
| `5c8994056166` | 12,920 | `〔幽灵引用·未上传:results___codex_c4_values_reply_intake_register_2026_10_10.md〕` | 12,920 | ✅ |
| `5ccceefbaa16` | 11,859 | `〔幽灵引用·未上传:docs__V3X__AGENT_TEAM_OPT_V2_2026_09_11.md〕` | 11,859 | ✅ |
| `5dc3c0faffed` | 12,671 | `〔幽灵引用·未上传:results___archive_2026_09_20__LETTER_TO_TRAE_REVIEW_2026_09_16.md〕` | 12,671 | ✅ |
| `5eaa7a03f151` | 56,321 | `〔幽灵引用·未上传:results___limb_reading_verdict_kv3s33_2026_10_01.md〕` | 56,321 | ✅ |
| `5ee1916ddb81` | 10,102 | `〔幽灵引用·未上传:_p_l_v3_phase2_or_embedding_v3_2026_09_17.console.log〕` | 10,102 | ✅ |
| `5f1e0670f4c4` | 16,097 | `〔幽灵引用·未上传:results___q3_c1c4_l282_transposition_fix_applied_note_2026_10_09.md〕` | 16,097 | ✅ |
| `5fd04575e161` | 43,312 | `〔幽灵引用·未上传:results___five_items_effectivity_register_2026_10_11.md〕` | 43,312 | ✅ |
| `60238391952b` | 52,156 | `〔幽灵引用·未上传:results___archive_manifest_deposon_sub_2026_09_23.json〕` | 52,156 | ✅ |
| `60f85dbfabc3` | 2,687 | `〔幽灵引用·未上传:_p_l_v3_phase2_closedsource_runner_v2_20260917_174011_claude_sonnet5.log〕` | 2,687 | ✅ |
| `61049ff75bb6` | 24,708 | `〔幽灵引用·未上传:_t1_exp2_activation_supplement_2026_10_09.md〕` | 24,708 | ✅ |
| `626c30caf82d` | 121,137 | `〔幽灵引用·未上传:_questionnaire_cards_intake_register_supplement_12_2026_10_10.md〕` | 121,137 | ✅ |
| `62823388e682` | 7,485 | `〔幽灵引用·未上传:_tdf_s1c_2026_10_12.py〕` | 7,485 | ✅ |
| `628fb6fe4fb0` | 32,830 | `〔本地路径已脱敏〕` | 32,830 | ✅ |
| `62966dc92fca` | 12,903 | `〔幽灵引用·未上传:results___gate_one_declared_adoption_register_2026_10_11.md〕` | 12,903 | ✅ |
| `629dd923bdab` | 16,013 | `〔幽灵引用·未上传:docs__V3X__P_F_D1_FULL_REPORT_2026_09_15.md〕` | 16,013 | ✅ |
| `62e68c52414c` | 50,790 | `〔幽灵引用·未上传:_questionnaire_cards_intake_register_supplement_8_2026_10_10.md〕` | 50,790 | ✅ |
| `635b562d3a5b` | 22,399 | `〔幽灵引用·未上传:_stage3_extraction_verification_2026_10_11.md〕` | 22,399 | ✅ |
| `639a46fbc44c` | 2,440 | `〔幽灵引用·未上传:_v2_stage3_f3_strip.console.log〕` | 2,440 | ✅ |
| `63bad8ab3356` | 11,522 | `〔幽灵引用·未上传:_test_3bb_vary.log〕` | 11,522 | ✅ |
| `641eb4c6ac2a` | 48,969 | `〔幽灵引用·未上传:results___round56_review_effectivity_register_2026_10_10.md〕` | 48,969 | ✅ |
| `648f83115184` | 30,964 | `〔幽灵引用·未上传:results___round56_b01_followup_disposition_plan_2026_10_10.md〕` | 30,964 | ✅ |
| `6567a3e316d1` | 19,988 | `〔幽灵引用·未上传:results___executor_prereg_vs_impl_equivalence_2026_10_11.md〕` | 19,988 | ✅ |
| `66975edaa99f` | 53,128 | `〔幽灵引用·未上传:results___s3prime_alert_disposition_judgment_2026_10_11.md〕` | 53,128 | ✅ |
| `672e14623f28` | 7,342 | `〔幽灵引用·未上传:deposon_volcengine_seed_code_30cells_2026_09_10.log〕` | 7,342 | ✅ |
| `6778a10ac0e3` | 10,891 | `〔幽灵引用·未上传:deposon_team__plugins___tdf_s2_apply_2026_10_12.py〕` | 10,891 | ✅ |
| `67da78b3d19e` | 20,023 | `〔幽灵引用·未上传:_round53_th_v3_19_landfall_schema_effectivity_register_2026_10_10.md〕` | 20,023 | ✅ |
| `67df53c3e97f` | 16,553 | `〔幽灵引用·未上传:_round56_ad8fix_effectivity_register_2026_10_10.md〕` | 16,553 | ✅ |
| `68078f446d66` | 13,883 | `〔幽灵引用·未上传:_pi_card_123_adoption_and_gate_one_request_2026_10_11.md〕` | 13,883 | ✅ |
| `68089948c69a` | 31,497 | `〔幽灵引用·未上传:results___four_items_execution_batch_2026_10_11.md〕` | 31,497 | ✅ |
| `6812ceb67f0a` | 12,427 | `〔幽灵引用·未上传:results___commission_closeout_erratum_and_supplement_2026_10_11.md〕` | 12,427 | ✅ |
| `685e17c9407d` | 45,207 | `〔本地路径已脱敏〕` | 45,207 | ✅ |
| `688b98ff44bd` | 24,868 | `〔幽灵引用·未上传:results___trj_w1_downstream_erratum_2026_10_10.md〕` | 24,868 | ✅ |
| `68bb6bd96c10` | 29,621 | `〔幽灵引用·未上传:results___g9_read_b_effectivity_register_2026_10_11.md〕` | 29,621 | ✅ |
| `68da7b05797b` | 93,324 | `〔幽灵引用·未上传:fiction_that_feeds_back.tex〕` | 93,324 | ✅ |
| `691137aa0627` | 13,592 | `〔幽灵引用·未上传:results___archive_2026_09_20___letter_to_kimi_push_v3_委托_2026_09_17.md〕` | 13,592 | ✅ |
| `69953e57b0fc` | 42,083 | `〔本地路径已脱敏〕` | 42,083 | ✅ |
| `69a21d50620b` | 106,412 | `〔幽灵引用·未上传:results___questionnaire_cards_intake_register_supplement_6_2026_10_10.md〕` | 106,412 | ✅ |
| `6b957b805b3f` | 50,367 | `〔幽灵引用·未上传:results___f3f4_exit_drafts_2026_10_11.md〕` | 50,367 | ✅ |
| `6bc5fde90a05` | 34,261 | `〔本地路径已脱敏〕` | 34,261 | ✅ |
| `6bcf5ed11826` | 18,256 | `〔幽灵引用·未上传:.trae__scripts___verify_tex.py〕` | 18,256 | ✅ |
| `6be2d532c63f` | 35,306 | `〔幽灵引用·未上传:results___overnight_delivery_index_2026_10_10.md〕` | 35,306 | ✅ |
| `6c04e8c0e1d2` | 36,727 | `〔幽灵引用·未上传:results___s7prime_prereq_and_verification_2026_10_11.md〕` | 36,727 | ✅ |
| `6c42ba3f285e` | 62,344 | `〔幽灵引用·未上传:_kj1_eps_ls_effectivity_register_2026_10_11.md〕` | 62,344 | ✅ |
| `6ce92f706bdd` | 24,113 | `〔幽灵引用·未上传:_worker_openrouter_rag_run.py〕` | 24,113 | ✅ |
| `6cf929fa6f49` | 31,371 | `〔幽灵引用·未上传:results___eps_ls_semantics_judgment_2026_10_11.md〕` | 31,371 | ✅ |
| `6d9bc4c95e8e` | 20,933 | `〔幽灵引用·未上传:_archive_ledger_rectification_register_2026_10_09.md〕` | 20,933 | ✅ |
| `6dd94f28c8d1` | 236,631 | `〔幽灵引用·未上传:results___archive_manifest_non_upload_v2_2026_09_28.json〕` | 236,631 | ✅ |
| `6ea8b41cad43` | 34,092 | `〔幽灵引用·未上传:results___j2_kj4_disposition_register_2026_10_11.md〕` | 34,092 | ✅ |
| `6f5d16b74ea8` | 26,844 | `〔幽灵引用·未上传:results___seed_double_identifier_finalization_2026_10_11.md〕` | 26,844 | ✅ |
| `6fc3463e11c1` | 37,582 | `〔幽灵引用·未上传:results___v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md〕` | 37,582 | ✅ |
| `709d6bf1bbd2` | 50,182 | `〔幽灵引用·未上传:results___seed_double_identifier_final_judgment_2026_10_11.md〕` | 50,182 | ✅ |
| `712b03ed9568` | 22,994 | `〔幽灵引用·未上传:results___trj_w1_verification_2026_10_10.md〕` | 22,994 | ✅ |
| `712b54772f56` | 43,388 | `〔幽灵引用·未上传:results___trigger_denominator_caliber_judgment_2026_10_11.md〕` | 43,388 | ✅ |
| `713e5f75c289` | 2,242 | `〔幽灵引用·未上传:_v3x_6way_stage3_recovery.log〕` | 2,242 | ✅ |
| `723b79dffa1c` | 50,774 | `〔幽灵引用·未上传:results___questionnaire_cards_intake_register_supplement_8_2026_10_10.md〕` | 50,774 | ✅ |
| `72854074e603` | 5,452 | `〔幽灵引用·未上传:results___archive_2026_09_20___d05_sanity_3backbone_2026_09_18.py〕` | 5,452 | ✅ |
| `729043e158c8` | 16,640 | `〔本地路径已脱敏〕` | 16,640 | ✅ |
| `72b9df5b6a46` | 1,229 | `〔幽灵引用·未上传:_tdf_s3b_2026_10_12.py〕` | 1,229 | ✅ |
| `73382f10061f` | 21,866 | `〔幽灵引用·未上传:_s4_seedprime_inheldout_recompute_2026_10_10.md〕` | 21,866 | ✅ |
| `734fc54ea746` | 35,862 | `〔幽灵引用·未上传:results___round56_terminal_boundary_effectivity_register_2026_10_10.md〕` | 35,862 | ✅ |
| `7375dbcc2a8b` | 20,082 | `〔幽灵引用·未上传:review_content_A1_dsv4pro.md〕` | 20,082 | ✅ |
| `741e2698699f` | 16,567 | `〔幽灵引用·未上传:_krj4_trj1_pick_and_pass_verdict_2026_10_11.md〕` | 16,567 | ✅ |
| `746426b0b285` | 31,515 | `〔幽灵引用·未上传:_s6doubleprime_verdict_supplement_2026_10_11.md〕` | 31,515 | ✅ |
| `747f06b6009c` | 23,857 | `〔幽灵引用·未上传:results___s4prime_five_lines_readings_2026_10_11.md〕` | 23,857 | ✅ |
| `74b52b923a57` | 21,377 | `〔本地路径已脱敏〕` | 21,377 | ✅ |
| `74e09e84ff0c` | 21,946 | `〔幽灵引用·未上传:results___s4_heldout_seedprime_verification_2026_10_10.md〕` | 21,946 | ✅ |
| `774e2e98ab1f` | 30,956 | `〔幽灵引用·未上传:_c8_c2_disposition_register_2026_10_11.md〕` | 30,956 | ✅ |
| `77bc8321aa38` | 11,960 | `〔幽灵引用·未上传:_seven_gap_closures_adoption_register_2026_10_11.md〕` | 11,960 | ✅ |
| `7801775634bd` | 17,333 | `〔幽灵引用·未上传:results___vk_face_category_erratum_2026_10_11.md〕` | 17,333 | ✅ |
| `7853e29f5cfc` | 31,495 | `〔幽灵引用·未上传:results___s6doubleprime_verdict_supplement_2026_10_11.md〕` | 31,495 | ✅ |
| `78577e0de271` | 19,764 | `〔幽灵引用·未上传:docs__V3X__V3X_D6_PAPER_zh.md〕` | 19,764 | ✅ |
| `78da765f2b4b` | 20,321 | `〔幽灵引用·未上传:_round56_n10_erratum_register_2026_10_10.md〕` | 20,321 | ✅ |
| `796dab06c04e` | 36,839 | `〔本地路径已脱敏〕` | 36,839 | ✅ |
| `7a7627198619` | 32,846 | `〔幽灵引用·未上传:results___fp3_anchor_and_krj_restrament_register_2026_10_11.md〕` | 32,846 | ✅ |
| `7a8b356ffd8b` | 54,877 | `〔幽灵引用·未上传:results___s6prime_terminal_verdicts_2026_10_11.md〕` | 54,877 | ✅ |
| `7b021054c471` | 25,621 | `〔幽灵引用·未上传:results___round53_rejudge_prereg_freeze_effectivity_register_2026_10_10.md〕` | 25,621 | ✅ |
| `7b7684a49c58` | 31,672 | `〔幽灵引用·未上传:_krj10_reverdict_after_r4_convergence_2026_10_11.md〕` | 31,672 | ✅ |
| `7bc1a4d3c812` | 13,294 | `〔幽灵引用·未上传:_register3_bytes_erratum_2026_10_11.md〕` | 13,294 | ✅ |
| `7c59058181e2` | 23,025 | `〔幽灵引用·未上传:_g4_residual_probe_2026_10_08.md〕` | 23,025 | ✅ |
| `7c6f1187c880` | 95,659 | `〔幽灵引用·未上传:_krj_all_terminal_verdicts_2026_10_11.md〕` | 95,659 | ✅ |
| `7ca62a5dc884` | 9,559 | `〔幽灵引用·未上传:results___gate_one_pi_endorsement_register_2026_10_12.md〕` | 9,559 | ✅ |
| `7d540c86567e` | 4,526 | `〔幽灵引用·未上传:_probe_teamo_via_proxy.log〕` | 4,526 | ✅ |
| `7d8441077e67` | 64,849 | `〔幽灵引用·未上传:_q3_c1c4_l282_transposition_fix_executor_2026_10_09.py〕` | 64,849 | ✅ |
| `7d8f557cdf1e` | 22,351 | `〔幽灵引用·未上传:_suspect17_release_move_register_2026_10_09.md〕` | 22,351 | ✅ |
| `7da95eb67e06` | 33,546 | `〔幽灵引用·未上传:results___b14_vk_evidence_audit_2026_10_10.md〕` | 33,546 | ✅ |
| `7e9ff72e8505` | 3,416 | `〔幽灵引用·未上传:_p_l_v3_phase2_runner.log〕` | 3,416 | ✅ |
| `817ff913f1f7` | 34,287 | `〔幽灵引用·未上传:_forgotten_recovery_register_2026_10_08.md〕` | 34,287 | ✅ |
| `8211ed74f0de` | 27,681 | `〔幽灵引用·未上传:results___executor_prereg_docstring_correction_2026_10_11.md〕` | 27,681 | ✅ |
| `8227c455082f` | 40,658 | `〔幽灵引用·未上传:results___pending_pi_items_drafts_2026_10_11.md〕` | 40,658 | ✅ |
| `82b0af3f4730` | 18,414 | `〔幽灵引用·未上传:results___b01_recompute_authorization_supplement_2026_10_11.md〕` | 18,414 | ✅ |
| `82c6c5530d55` | 102,393 | `〔幽灵引用·未上传:results___v5_r4_residual_merged_catalogue_2026_09_29.md〕` | 102,393 | ✅ |
| `834d4dc31af5` | 46,135 | `〔幽灵引用·未上传:_round56r8_dispositions_register_2026_10_10.md〕` | 46,135 | ✅ |
| `84394f9e5ee6` | 1,221 | `〔幽灵引用·未上传:deposon_team__plugins___tdf_s3b_2026_10_12.py〕` | 1,221 | ✅ |
| `843afd0baa41` | 1,158 | `〔幽灵引用·未上传:_audit_temp_inspect_workers.py.bak〕` | 1,158 | ✅ |
| `8489ee888ae0` | 29,479 | `〔幽灵引用·未上传:_stage1_independent_gate_review_2026_10_12.md〕` | 29,479 | ✅ |
| `84d19c144ab1` | 33,179 | `〔幽灵引用·未上传:_cleanup_round_2026_10_08.md〕` | 33,179 | ✅ |
| `8529c3f37779` | 28,565 | `〔幽灵引用·未上传:results___ftfb_v3_pass2_audit_2026_09_18_corrected.md〕` | 28,565 | ✅ |
| `852ce8b50ec9` | 46,514 | `〔幽灵引用·未上传:results___k_v3df_0_1_four_readings_2026_10_09.md〕` | 46,514 | ✅ |
| `853dd2881e5e` | 3,326 | `〔幽灵引用·未上传:deposon_volcengine_worker_b_2026_09_10.log〕` | 3,326 | ✅ |
| `8542b765938a` | 116,508 | `〔幽灵引用·未上传:results___questionnaire_cards_intake_register_supplement_4_2026_10_10.md〕` | 116,508 | ✅ |
| `85a23e2ac195` | 38,669 | `〔本地路径已脱敏〕` | 38,669 | ✅ |
| `86018028a7fa` | 24,799 | `〔幽灵引用·未上传:results___g5_ccp_p0_verification_2026_10_10.md〕` | 24,799 | ✅ |
| `866261714244` | 43,240 | `〔幽灵引用·未上传:_round56_direct_adoptions_register_2026_10_10.md〕` | 43,240 | ✅ |
| `8697740e0aca` | 67,949 | `〔幽灵引用·未上传:results___t1_exp2_executor_2026_10_09.py〕` | 67,949 | ✅ |
| `877fe26ca772` | 55,327 | `〔幽灵引用·未上传:results___questionnaire_cards_intake_register_supplement_11_2026_10_10.md〕` | 55,327 | ✅ |
| `87a2ff256873` | 184,936 | `〔幽灵引用·未上传:results___v4_closeout_bulk_reorganize_register_2026_10_12.md〕` | 184,936 | ✅ |
| `884f61b07779` | 44,698 | `〔幽灵引用·未上传:_questionnaire_cards_intake_register_supplement_15_2026_10_11.md〕` | 44,698 | ✅ |
| `887969a1931c` | 49,031 | `〔幽灵引用·未上传:results___g5_rejudgment_c_applicability_recheck_2026_10_10.md〕` | 49,031 | ✅ |
| `8912d907b188` | 2,168 | `〔幽灵引用·未上传:_sanity_teamo_three.log〕` | 2,168 | ✅ |
| `8943272627e9` | 29,956 | `〔幽灵引用·未上传:_stage3_readings_verification_2026_10_11.md〕` | 29,956 | ✅ |
| `89744f279f62` | 262,542 | `〔幽灵引用·未上传:_questionnaire_cards_intake_register_supplement_2_2026_10_10.md〕` | 262,542 | ✅ |
| `8a16a7461a32` | 291,567 | `〔幽灵引用·未上传:_movedout_manifest_2026_09_21.json〕` | 291,567 | ✅ |
| `8a2cb27e6fe0` | 35,215 | `〔幽灵引用·未上传:_s4_open_questions_addendum_2026_10_09.json〕` | 35,215 | ✅ |
| `8a2ccfd50d52` | 26,329 | `〔幽灵引用·未上传:results___round56_typeb_implementation_register_2026_10_10.md〕` | 26,329 | ✅ |
| `8a85318ae33e` | 29,898 | `〔幽灵引用·未上传:results___axis1_three_recomputations_2026_10_11.md〕` | 29,898 | ✅ |
| `8af3fd8a08db` | 9,441 | `〔幽灵引用·未上传:_asset_recount_2026_09_30.md〕` | 9,441 | ✅ |
| `8b06e5d3f43d` | 17,456 | `〔幽灵引用·未上传:_v41_flash_rag_baseline_run.log〕` | 17,456 | ✅ |
| `8b6724812e08` | 35,012 | `〔幽灵引用·未上传:results___kj1_judgment_premise_correction_2026_10_11.md〕` | 35,012 | ✅ |
| `8bb3eeded041` | 40,301 | `〔幽灵引用·未上传:_f4_direction1_domain_effectivity_2026_10_11.md〕` | 40,301 | ✅ |
| `8c694436358f` | 38,034 | `〔幽灵引用·未上传:results___alt_delib_pkg3_two_judgments_2026_10_10.md〕` | 38,034 | ✅ |
| `8cfd8dd5620c` | 1,092 | `〔幽灵引用·未上传:deposon_v2_phase5_f5_2026_09_11.log〕` | 1,092 | ✅ |
| `8d2534d1a44e` | 43,155 | `〔幽灵引用·未上传:results___q2_scope_vs_revision_judgment_2026_10_11.md〕` | 43,155 | ✅ |
| `8d8488bc8716` | 35,683 | `〔幽灵引用·未上传:results___stage3_trigger_readings_2026_10_11.md〕` | 35,683 | ✅ |
| `8da06df0e058` | 857,249 | `〔幽灵引用·未上传:docs__V3X__TRAE_V3_ASSET_ERRATUM_2026_09_23.md〕` | 857,249 | ✅ |
| `8e40c48ca35d` | 603,712 | `〔幽灵引用·未上传:results___v5_sub_artifact_ledger_history_r4_2026_09_29.md〕` | 603,712 | ✅ |
| `8e93f206b546` | 30,253 | `〔幽灵引用·未上传:results___krj4_trj1_adjudication_judgment_2026_10_11.md〕` | 30,253 | ✅ |
| `8ea98f0f8dc2` | 15,546 | `〔幽灵引用·未上传:_krj_cond4_effectivity_declaration_2026_10_11.md〕` | 15,546 | ✅ |
| `8ef45406f66d` | 46,243 | `〔幽灵引用·未上传:results___e6_th_v3_19_residual_exits_judgment_2026_10_10.md〕` | 46,243 | ✅ |
| `8f52777de504` | 29,649 | `〔幽灵引用·未上传:_g9_read_b_effectivity_register_2026_10_11.md〕` | 29,649 | ✅ |
| `8f6f952dea43` | 13,825 | `〔幽灵引用·未上传:results___stage3_open_and_mandate_register_2026_10_12.md〕` | 13,825 | ✅ |
| `8fb9a1bbd91e` | 27,906 | `〔幽灵引用·未上传:results___lim_aperiod_restatement_third_domain_2026_10_11.md〕` | 27,906 | ✅ |
| `90370c77b4a5` | 24,650 | `〔幽灵引用·未上传:results___s4_heldout_sampling_seedprime_items_register_2026_10_10.md〕` | 24,650 | ✅ |
| `90617176e1ae` | 128,834 | `〔幽灵引用·未上传:results___v5_sub_artifact_ledger_history_r3_2026_09_29.md〕` | 128,834 | ✅ |
| `90692d4100f3` | 27,682 | `〔本地路径已脱敏〕` | 27,682 | ✅ |
| `9069eede88f9` | 16,642 | `〔幽灵引用·未上传:results___round56_sc4_nstar_inconsistency_erratum_2026_10_10.md〕` | 16,642 | ✅ |
| `9094c78c5433` | 309,394 | `〔幽灵引用·未上传:results___repo_post_cleanup_snapshot_2026_10_12.md〕` | 309,394 | ✅ |
| `911ddccd5c44` | 5,683 | `〔幽灵引用·未上传:results___pre_exec_report_kimi_2026_09_30.md〕` | 5,683 | ✅ |
| `911e88d52b64` | 47,737 | `〔幽灵引用·未上传:results___v5_paper_remedy_r1_pledge_2026_09_29.md〕` | 47,737 | ✅ |
| `91ac74bd958a` | 6,277 | `〔幽灵引用·未上传:_pre_execution_report_kimi_2026_10_01.md〕` | 6,277 | ✅ |
| `91d92fd7a88b` | 10,683 | `〔幽灵引用·未上传:results___charlie_delivery_register_2026_10_08.md〕` | 10,683 | ✅ |
| `925a68307d20` | 42,043 | `〔幽灵引用·未上传:results___kj1_abc_choice_judgment_2026_10_11.md〕` | 42,043 | ✅ |
| `92876b0b8dbd` | 20,959 | `〔幽灵引用·未上传:results___g5_ccp_seed_designation_revision_2026_10_10.md〕` | 20,959 | ✅ |
| `933ea82b8572` | 7,261 | `〔幽灵引用·未上传:_misformed_commission_drafts_deletion_register_2026_10_11.md〕` | 7,261 | ✅ |
| `935b16bc9d48` | 21,158 | `〔幽灵引用·未上传:results___e6_j5_semantics_erratum_note_2026_10_10.md〕` | 21,158 | ✅ |
| `938102d0e310` | 6,433 | `〔幽灵引用·未上传:results___archive_2026_09_20___audit_secret_2026_09_20_anchor_guard.py〕` | 6,433 | ✅ |
| `941186a880eb` | 16,531 | `〔幽灵引用·未上传:_arxiv_renumber.py〕` | 16,531 | ✅ |
| `941424bc6d71` | 22,064 | `〔幽灵引用·未上传:results___b01_p_counting_recompute_2026_10_10.md〕` | 22,064 | ✅ |
| `943c8aafa85f` | 72,247 | `〔幽灵引用·未上传:_krj_all_five_verdicts_rewrite_2026_10_11.md〕` | 72,247 | ✅ |
| `94e70b3cff4b` | 47,526 | `〔幽灵引用·未上传:results___forgotten_recovery_register_2026_09_29.md〕` | 47,526 | ✅ |
| `94f2a70ee4d5` | 31,391 | `〔本地路径已脱敏〕` | 31,391 | ✅ |
| `9661494aea4f` | 41,680 | `〔本地路径已脱敏〕` | 41,680 | ✅ |
| `9678a036b1b7` | 3,100 | `〔幽灵引用·未上传:_p_l_v3_phase2_probe.log〕` | 3,100 | ✅ |
| `96bb0a05de8b` | 1,171 | `〔幽灵引用·未上传:_audit_temp_inspect_minimax_m3.py.bak〕` | 1,171 | ✅ |
| `96c744af6776` | 9,343 | `〔幽灵引用·未上传:TRAE_CODE_FIX_LIST_2026_09_18.md〕` | 9,343 | ✅ |
| `97315904a13e` | 41,140 | `〔幽灵引用·未上传:_stage1_tail_caliber_unification_register_2026_10_11.md〕` | 41,140 | ✅ |
| `97619a3c7c8e` | 41,648 | `〔幽灵引用·未上传:results___s3prime_recompute_after_supplement_2026_10_11.md〕` | 41,648 | ✅ |
| `97e2aa66522f` | 17,772 | `〔幽灵引用·未上传:deposon_dpath_cross_modal_runner_2026_09_10.stdout.log〕` | 17,772 | ✅ |
| `987fd959ce49` | 11,105 | `〔幽灵引用·未上传:_volc_22cap_emb.py〕` | 11,105 | ✅ |
| `99f9c34aaa90` | 30,948 | `〔幽灵引用·未上传:results___s7prime_findings_erratum_2026_10_11.md〕` | 30,948 | ✅ |
| `9c27502abd00` | 31,515 | `〔本地路径已脱敏〕` | 31,515 | ✅ |
| `9ca61f7833db` | 24,888 | `〔本地路径已脱敏〕` | 24,888 | ✅ |
| `9e006c0584c8` | 14,874 | `〔幽灵引用·未上传:_stage2_trae_reply_acceptance_register_2026_10_12.md〕` | 14,874 | ✅ |
| `9e29f7f3ab4e` | 114,239 | `〔幽灵引用·未上传:results___questionnaire_cards_intake_register_supplement_13_2026_10_11.md〕` | 114,239 | ✅ |
| `9e692ba895ed` | 3,232 | `〔幽灵引用·未上传:_cleanup_classify_2026_09_28.py〕` | 3,232 | ✅ |
| `9e8ac3f39e98` | 22,895 | `〔幽灵引用·未上传:_codex_c4_unblock_reply_adoption_register_2026_10_10.md〕` | 22,895 | ✅ |
| `9f1e923dd24a` | 17,475 | `〔幽灵引用·未上传:deposon_team__plugins__fix_boss_naming_2026_09_16.py〕` | 17,475 | ✅ |
| `9f37ef2ba0db` | 39,668 | `〔幽灵引用·未上传:results___v4_trae_remaining_audit_2026_09_28.md〕` | 39,668 | ✅ |
| `a07774dbcb71` | 27,804 | `〔幽灵引用·未上传:results___zero_reading_judgment_2026_10_10.md〕` | 27,804 | ✅ |
| `a1847e9f51f7` | 20,046 | `〔幽灵引用·未上传:results___u5b_p_counting_resolution_2026_10_10.md〕` | 20,046 | ✅ |
| `a22aa0b2ddea` | 1,147 | `〔幽灵引用·未上传:results___archive_2026_09_24___verify_worker_c.py〕` | 1,147 | ✅ |
| `a2a4b2977fc9` | 11,566 | `〔幽灵引用·未上传:_exp05_negative_probe_rescan_2026_10_10.md〕` | 11,566 | ✅ |
| `a2bf7d0f85d8` | 28,614 | `〔幽灵引用·未上传:results___krj9_scope_clarification_draft_2026_10_10.md〕` | 28,614 | ✅ |
| `a2dd2d65b1ec` | 31,336 | `〔幽灵引用·未上传:results___v5_t1_decisions_register_2026_09_29.md〕` | 31,336 | ✅ |
| `a2deb8df3616` | 26,367 | `〔幽灵引用·未上传:_round56_typeb_implementation_register_2026_10_10.md〕` | 26,367 | ✅ |
| `a300572d5420` | 22,606 | `〔幽灵引用·未上传:results___s4_heldout_sampling_seedthird_items_register_2026_10_11.md〕` | 22,606 | ✅ |
| `a36975e48f45` | 40,215 | `〔幽灵引用·未上传:results___round56_typeb_backfill_register_2026_10_10.md〕` | 40,215 | ✅ |
| `a4489af68f91` | 11,390 | `〔幽灵引用·未上传:results___archive_2026_09_20___ftfb_pass2_results_limitations_audit_2026_09_17.md〕` | 11,390 | ✅ |
| `a4612beda9a8` | 15,214 | `〔幽灵引用·未上传:_krj_pi_picks_adoption_krj6_revise_2026_10_11.md〕` | 15,214 | ✅ |
| `a483ac9fba64` | 39,977 | `〔幽灵引用·未上传:_round54_g5_dispositions_register_2026_10_10.md〕` | 39,977 | ✅ |
| `a57424c19d1d` | 30,916 | `〔幽灵引用·未上传:results___c8_c2_disposition_register_2026_10_11.md〕` | 30,916 | ✅ |
| `a5bf28d3fcca` | 20,007 | `〔幽灵引用·未上传:results___round53_th_v3_19_landfall_schema_effectivity_register_2026_10_10.md〕` | 20,007 | ✅ |
| `a5c5396ad589` | 8,064 | `〔幽灵引用·未上传:_tdf_s1b_2026_10_12.py〕` | 8,064 | ✅ |
| `a5fbdfb9265b` | 41,984 | `〔本地路径已脱敏〕` | 41,984 | ✅ |
| `a611d3e62978` | 84,113 | `〔幽灵引用·未上传:results___questionnaire_cards_intake_register_supplement_10_2026_10_10.md〕` | 84,113 | ✅ |
| `a675bae218b4` | 8,668 | `〔幽灵引用·未上传:deposon_team__plugins__skill_b_p_c_alpha_beta.py〕` | 8,668 | ✅ |
| `a6cbce33a1ff` | 16,547 | `〔幽灵引用·未上传:results___krj4_trj1_pick_and_pass_verdict_2026_10_11.md〕` | 16,547 | ✅ |
| `a73d123433be` | 34,948 | `〔幽灵引用·未上传:_chd_construction_domain_declaration_draft_2026_10_10.md〕` | 34,948 | ✅ |
| `a76a2658a272` | 18,611 | `〔幽灵引用·未上传:_letter_to_coze_online_v2_2026_09_18.md〕` | 18,611 | ✅ |
| `a76a99b95a0c` | 43,195 | `〔本地路径已脱敏〕` | 43,195 | ✅ |
| `a7cba69019ce` | 19,611 | `〔幽灵引用·未上传:_ea_audit_batch_vk_2026_10_09.md〕` | 19,611 | ✅ |
| `a861f72e0d3c` | 44,684 | `〔幽灵引用·未上传:results___questionnaire_cards_intake_register_supplement_15_2026_10_11.md〕` | 44,684 | ✅ |
| `a894aed7b566` | 30,293 | `〔幽灵引用·未上传:_krj4_trj1_adjudication_judgment_2026_10_11.md〕` | 30,293 | ✅ |
| `a9235f93834e` | 27,058 | `〔幽灵引用·未上传:results___codex_c4_values_unblock_reply_intake_register_2026_10_10.md〕` | 27,058 | ✅ |
| `a9664bdcccdd` | 35,050 | `〔本地路径已脱敏〕` | 35,050 | ✅ |
| `a9a9122ec067` | 40,281 | `〔幽灵引用·未上传:results___f4_direction1_domain_effectivity_2026_10_11.md〕` | 40,281 | ✅ |
| `a9ee659d65c8` | 40,678 | `〔幽灵引用·未上传:_pending_pi_items_drafts_2026_10_11.md〕` | 40,678 | ✅ |
| `ab1a25ac9008` | 18,553 | `〔幽灵引用·未上传:deposon_team__plugins___v3x_experiments_runner_2026_09_16.py〕` | 18,553 | ✅ |
| `ab4d6db386cd` | 41,282 | `〔幽灵引用·未上传:results___s2prime_krj3_applicability_recheck_2026_10_10.md〕` | 41,282 | ✅ |
| `ab7a494cd3d7` | 48,068 | `〔本地路径已脱敏〕` | 48,068 | ✅ |
| `ab979408cda3` | 50,170 | `〔本地路径已脱敏〕` | 50,170 | ✅ |
| `abc9a7d2293a` | 17,517 | `〔幽灵引用·未上传:_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md〕` | 17,517 | ✅ |
| `ac1d0b5bd3c2` | 1,444 | `〔幽灵引用·未上传:_sanity_openai_more.log〕` | 1,444 | ✅ |
| `ac73825cb34a` | 17,576 | `〔幽灵引用·未上传:results___v3_s_phrasetemplate_preexp_data__rescript_2026_09_27.md〕` | 17,576 | ✅ |
| `acba222fdf57` | 58,478 | `〔幽灵引用·未上传:_round56_review_effectivity_register_6_2026_10_11.md〕` | 58,478 | ✅ |
| `acdadd7aefef` | 10,729 | `〔本地路径已脱敏〕` | 10,729 | ✅ |
| `ad9135f3a220` | 44,771 | `〔幽灵引用·未上传:results___v3_recheck_21_result_2026_09_27.json〕` | 44,771 | ✅ |
| `ae2c5587a86b` | 114,253 | `〔幽灵引用·未上传:_questionnaire_cards_intake_register_supplement_13_2026_10_11.md〕` | 114,253 | ✅ |
| `ae7633cfa6b7` | 23,604 | `〔幽灵引用·未上传:results___upload_guard_mirror_pair_2026_10_08.md〕` | 23,604 | ✅ |
| `afcd2edaa952` | 30,664 | `〔幽灵引用·未上传:results___g4_e3_definition_ruling_material_2026_10_09.md〕` | 30,664 | ✅ |
| `b16d7fe824a8` | 194,179 | `〔幽灵引用·未上传:results___v3_v4_achievements_inventory_2026_09_24.md〕` | 194,179 | ✅ |
| `b199ecc80ca8` | 16,744 | `〔本地路径已脱敏〕` | 16,744 | ✅ |
| `b24d710ed030` | 23,092 | `〔幽灵引用·未上传:results___v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md〕` | 23,092 | ✅ |
| `b2bca9e0cc97` | 27,100 | `〔幽灵引用·未上传:_codex_c4_values_unblock_reply_intake_register_2026_10_10.md〕` | 27,100 | ✅ |
| `b2fbd94ef807` | 12,923 | `〔幽灵引用·未上传:_gate_one_declared_adoption_register_2026_10_11.md〕` | 12,923 | ✅ |
| `b38a5f82e104` | 34,651 | `〔幽灵引用·未上传:results___v5_paper_remedy_r2_r4_sourcetrace_2026_09_29.md〕` | 34,651 | ✅ |
| `b38b11217838` | 31,046 | `〔幽灵引用·未上传:results___kj1_sc1_premise_correction_2026_10_11.md〕` | 31,046 | ✅ |
| `b39406b8614e` | 4,091 | `〔幽灵引用·未上传:volcengine_glm_latest_30cells_v2_run_2026_09_10.log〕` | 4,091 | ✅ |
| `b3b155e38028` | 60,700 | `〔幽灵引用·未上传:_krj5_final_disposition_verdict_2026_10_11.md〕` | 60,700 | ✅ |
| `b3c0d245c088` | 31,044 | `〔本地路径已脱敏〕` | 31,044 | ✅ |
| `b4493b9fbe38` | 31,008 | `〔本地路径已脱敏〕` | 31,008 | ✅ |
| `b5004c027d08` | 28,826 | `〔幽灵引用·未上传:results___c4_math_corrections_downstream_erratum_2026_10_10.md〕` | 28,826 | ✅ |
| `b577aa149ac3` | 7,233 | `〔幽灵引用·未上传:results___misformed_commission_drafts_deletion_register_2026_10_11.md〕` | 7,233 | ✅ |
| `b5b0f2cf3c37` | 20,979 | `〔幽灵引用·未上传:_g5_ccp_seed_designation_revision_2026_10_10.md〕` | 20,979 | ✅ |
| `b5cb510206f3` | 14,854 | `〔幽灵引用·未上传:results___stage2_trae_reply_acceptance_register_2026_10_12.md〕` | 14,854 | ✅ |
| `b779b83fb02c` | 21,369 | `〔幽灵引用·未上传:results___u04_1_exemption_precondition_verification_2026_10_09.md〕` | 21,369 | ✅ |
| `b873520cdd95` | 45,372 | `〔本地路径已脱敏〕` | 45,372 | ✅ |
| `b899cb2f91fe` | 44,179 | `〔幽灵引用·未上传:results___s4_corpus_scope_hard_constraint_judgment_2026_10_10.md〕` | 44,179 | ✅ |
| `b8c68387046b` | 34,605 | `〔幽灵引用·未上传:docs__V3X__REVIEWER_A_STATIC_AUDIT_2026_09_15.md〕` | 34,605 | ✅ |
| `b99e008fb01c` | 18,976 | `〔本地路径已脱敏〕` | 18,976 | ✅ |
| `b9aba7f5edb9` | 18,703 | `〔幽灵引用·未上传:results___round56c_card_id_erratum_2026_10_10.md〕` | 18,703 | ✅ |
| `ba5c6e7a4a9c` | 52,602 | `〔幽灵引用·未上传:_questionnaire_cards_intake_register_supplement_7_2026_10_10.md〕` | 52,602 | ✅ |
| `baf86b575ab1` | 34,689 | `〔幽灵引用·未上传:_s4_heldout_sampling_seed42_items_register_2026_10_09.md〕` | 34,689 | ✅ |
| `bb5c9001dd31` | 28,959 | `〔幽灵引用·未上传:results___round56_pending_questions_compilation_supplement_note_2026_10_10.md〕` | 28,959 | ✅ |
| `bb5e79511c7e` | 1,140 | `〔幽灵引用·未上传:_p_l_v3_phase2_glm53_only_20260917_142011.log〕` | 1,140 | ✅ |
| `bb722799e89e` | 47,089 | `〔幽灵引用·未上传:results___round56_idx_sc1_resolution_2026_10_10.md〕` | 47,089 | ✅ |
| `bc45365245aa` | 35,878 | `〔幽灵引用·未上传:_round56_terminal_boundary_effectivity_register_2026_10_10.md〕` | 35,878 | ✅ |
| `bcf317b88d6e` | 10,586 | `〔幽灵引用·未上传:LETTER_TO_EXTERNAL_ADVISOR_2026_09_18_FINAL.md〕` | 10,586 | ✅ |
| `bd07469049db` | 37,173 | `〔幽灵引用·未上传:results___v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md〕` | 37,173 | ✅ |
| `bd948baf6f71` | 20,305 | `〔幽灵引用·未上传:results___round56_n10_erratum_register_2026_10_10.md〕` | 20,305 | ✅ |
| `bddcd0848fb2` | 25,045 | `〔本地路径已脱敏〕` | 25,045 | ✅ |
| `bde67d5a1516` | 12,601 | `〔幽灵引用·未上传:results___pending_supply_search_receipt_2026_10_08.md〕` | 12,601 | ✅ |
| `be3d138384e2` | 1,064 | `〔幽灵引用·未上传:deposon_v2_phase4_f4_2026_09_11.log〕` | 1,064 | ✅ |
| `be3de9009298` | 25,698 | `〔本地路径已脱敏〕` | 25,698 | ✅ |
| `c096f23a2f79` | 19,069 | `〔幽灵引用·未上传:results___v4_maindir_cleanup_manifest_2026_09_24.md〕` | 19,069 | ✅ |
| `c0edaf60f28c` | 16,044 | `〔幽灵引用·未上传:results___krj_five_verdicts_adjudication_2026_10_11.md〕` | 16,044 | ✅ |
| `c114ca7ac083` | 39,565 | `〔本地路径已脱敏〕` | 39,565 | ✅ |
| `c12334453b58` | 13,826 | `〔幽灵引用·未上传:_clearance_round_1_register_2026_10_08.md〕` | 13,826 | ✅ |
| `c17c103993f3` | 26,673 | `〔幽灵引用·未上传:results___c2_criterion_third_tier_draft_2026_10_11.md〕` | 26,673 | ✅ |
| `c3b87ceaad9d` | 5,869 | `〔幽灵引用·未上传:deposon_volcengine_worker_c_2026_09_10.log〕` | 5,869 | ✅ |
| `c3f0ec7ba9fb` | 23,893 | `〔幽灵引用·未上传:_old_corpus_view.py〕` | 23,893 | ✅ |
| `c4580a3b3b29` | 36,995 | `〔幽灵引用·未上传:results___k_v3df_0_1_readings_verdict_2026_10_09.md〕` | 36,995 | ✅ |
| `c4aa2b53e20f` | 37,003 | `〔幽灵引用·未上传:_k_v3df_0_1_readings_verdict_2026_10_09.md〕` | 37,003 | ✅ |
| `c4c89193db52` | 12,359 | `〔幽灵引用·未上传:tmp_movedout_2026_09_28___cleanup_probe_out_2026_09_28.txt〕` | 12,359 | ✅ |
| `c4e270d0b423` | 20,028 | `〔幽灵引用·未上传:_executor_prereg_vs_impl_equivalence_2026_10_11.md〕` | 20,028 | ✅ |
| `c533fd52eb13` | 84,408 | `〔幽灵引用·未上传:results___questionnaire_cards_intake_register_supplement_9_2026_10_10.md〕` | 84,408 | ✅ |
| `c5e19f40a90b` | 58,646 | `〔幽灵引用·未上传:README_V4_2026_09_29.md〕` | 58,646 | ✅ |
| `c634e087d745` | 23,066 | `〔幽灵引用·未上传:tmp_movedout_2026_10_09__uncertain_release_2026_09___v5_b14_r3_anchor_retrieval_2026_09_29.md〕` | 23,066 | ✅ |
| `c6814cf0a0b7` | 15,818 | `〔幽灵引用·未上传:_stage3_1_bulk_reorg_completion_register_2026_10_12.md〕` | 15,818 | ✅ |
| `c69261f091af` | 52,586 | `〔幽灵引用·未上传:results___questionnaire_cards_intake_register_supplement_7_2026_10_10.md〕` | 52,586 | ✅ |
| `c6aca7403cf8` | 6,887 | `〔幽灵引用·未上传:deposon_feshbach_rag_30cells_2026_09_10.log〕` | 6,887 | ✅ |
| `c7f9aceeaa08` | 11,091 | `〔幽灵引用·未上传:results___archive_2026_09_24___volc_22cap_emb.py〕` | 11,091 | ✅ |
| `c7ff24b95ca4` | 17,071 | `〔幽灵引用·未上传:results___v3_recheck_08c_preexp_data__rescript_2026_09_27.md〕` | 17,071 | ✅ |
| `c83c63c766f4` | 2,765 | `〔幽灵引用·未上传:_p_l_v3_phase2_closedsource_runner_v2_20260917_173159_gpt56sol.log〕` | 2,765 | ✅ |
| `c866e0dfd4ba` | 49,049 | `〔幽灵引用·未上传:results___stage3_trigger_recheck_2026_10_11.md〕` | 49,049 | ✅ |
| `c901b65dd9e7` | 6,239 | `〔幽灵引用·未上传:deposon_team__plugins___d7_post_anchor_rotation_remediation_2026_09_16.py〕` | 6,239 | ✅ |
| `c903073be182` | 34,112 | `〔幽灵引用·未上传:_j2_kj4_disposition_register_2026_10_11.md〕` | 34,112 | ✅ |
| `c9422fa9e7ed` | 53,125 | `〔幽灵引用·未上传:results___mini_round_5_decisions_register_2026_10_01.md〕` | 53,125 | ✅ |
| `c9983f6177ac` | 10,709 | `〔幽灵引用·未上传:results___krj5d_third_tier_effectivity_2026_10_11.md〕` | 10,709 | ✅ |
| `ca4bad1a0f19` | 9,818 | `〔幽灵引用·未上传:results___v4_gA1_terminology_draft_2026_09_22.md〕` | 9,818 | ✅ |
| `ca670157f6c9` | 47,000 | `〔幽灵引用·未上传:results___kimi_safe_batch_push_v2_full_2026_09_17.json〕` | 47,000 | ✅ |
| `ca9dc8aefe34` | 2,548 | `〔幽灵引用·未上传:tmp_movedout_2026_09_28___cleanup_probe_2026_09_28.py〕` | 2,548 | ✅ |
| `caba9ef44ff8` | 60,640 | `〔幽灵引用·未上传:results___krj5_final_disposition_verdict_2026_10_11.md〕` | 60,640 | ✅ |
| `cad9573c7130` | 27,721 | `〔幽灵引用·未上传:_executor_prereg_docstring_correction_2026_10_11.md〕` | 27,721 | ✅ |
| `cb3c79a9b561` | 19,571 | `〔幽灵引用·未上传:results___ea_audit_batch_vk_2026_10_09.md〕` | 19,571 | ✅ |
| `cb8f0635c4e8` | 8,952 | `〔幽灵引用·未上传:_v3x_6way_run.log〕` | 8,952 | ✅ |
| `cb94bef12c8c` | 48,647 | `〔幽灵引用·未上传:.trae__scripts___md_to_tex.py〕` | 48,647 | ✅ |
| `cbd82437ff52` | 41,924 | `〔幽灵引用·未上传:results___b01_new_key_residue_judgment_2026_10_10.md〕` | 41,924 | ✅ |
| `cc626bcf5107` | 57,004 | `〔幽灵引用·未上传:_g5_rejudgment_construction_change_plan_2026_10_10.md〕` | 57,004 | ✅ |
| `cc864345e5f3` | 29,425 | `〔幽灵引用·未上传:results___stage1_independent_gate_review_2026_10_12.md〕` | 29,425 | ✅ |
| `ccd50440800d` | 55,082 | `〔幽灵引用·未上传:results___five_pending_items_drafts_2026_10_11.md〕` | 55,082 | ✅ |
| `cd304426ffe5` | 72,207 | `〔幽灵引用·未上传:results___krj_all_five_verdicts_rewrite_2026_10_11.md〕` | 72,207 | ✅ |
| `cd78df661d8b` | 4,220 | `〔幽灵引用·未上传:gpt6_30cells_run.log〕` | 4,220 | ✅ |
| `cdf830797db3` | 14,081 | `〔幽灵引用·未上传:results___krj10_terminal_verdict_closure_2026_10_11.md〕` | 14,081 | ✅ |
| `ce300c1883d8` | 48,514 | `〔幽灵引用·未上传:results___v5_sub_artifact_ledger_history_r1_2026_09_29.md〕` | 48,514 | ✅ |
| `ce3db50d3ec3` | 23,035 | `〔幽灵引用·未上传:results___g4_residual_probe_2026_10_08.md〕` | 23,035 | ✅ |
| `ce503683fb4a` | 46,522 | `〔幽灵引用·未上传:_k_v3df_0_1_four_readings_2026_10_09.md〕` | 46,522 | ✅ |
| `cefb47728dbb` | 37,607 | `〔幽灵引用·未上传:results___s4_heldout_sampling_seed42_register_2026_10_09.md〕` | 37,607 | ✅ |
| `cfd8b638f42d` | 612,511 | `〔幽灵引用·未上传:_v41_flash_rag_caption_embs.bak.json〕` | 612,511 | ✅ |
| `d05d668a6c50` | 31,607 | `〔本地路径已脱敏〕` | 31,607 | ✅ |
| `d08f1625732a` | 30,510 | `〔本地路径已脱敏〕` | 30,510 | ✅ |
| `d10449b8019f` | 41,120 | `〔幽灵引用·未上传:results___stage1_tail_caliber_unification_register_2026_10_11.md〕` | 41,120 | ✅ |
| `d10a14ba179a` | 454,307 | `〔幽灵引用·未上传:_coze_online_v3_d7format_2026_09_18.pdf〕` | 454,307 | ✅ |
| `d15e442aa686` | 10,235 | `〔幽灵引用·未上传:results___kd_doc1_correction_adoption_register_2026_10_11.md〕` | 10,235 | ✅ |
| `d1d9dfb4557a` | 11,940 | `〔幽灵引用·未上传:results___seven_gap_closures_adoption_register_2026_10_11.md〕` | 11,940 | ✅ |
| `d1f01b136d9e` | 23,877 | `〔幽灵引用·未上传:_s4prime_five_lines_readings_2026_10_11.md〕` | 23,877 | ✅ |
| `d2163dca73e5` | 10,295 | `〔幽灵引用·未上传:tmp_movedout_2026_10_09__uncertain_release_2026_09___letter_review_bob_w3_commission_2026_09_30.md〕` | 10,295 | ✅ |
| `d268d9eea466` | 54,871 | `〔幽灵引用·未上传:results___questionnaire_cards_intake_register_supplement_14_2026_10_11.md〕` | 54,871 | ✅ |
| `d39d91ecd84c` | 7,855 | `〔幽灵引用·未上传:LETTER_TO_TRAE_FIX_SELFCHECK_2026_09_15.md〕` | 7,855 | ✅ |
| `d3e6528187c2` | 18,536 | `〔幽灵引用·未上传:results___v4_closeout_moves_and_cleanup_register_2026_10_12.md〕` | 18,536 | ✅ |
| `d42b879bc3de` | 2,925 | `〔幽灵引用·未上传:_p_l_v3_phase2_vector_emb_doubao_2026_09_17.console2.log〕` | 2,925 | ✅ |
| `d46e9dd7ab4f` | 8,872 | `〔幽灵引用·未上传:deposon_team__plugins__skill_c_p_e_3modality.py〕` | 8,872 | ✅ |
| `d4ab99975a77` | 47,225 | `〔幽灵引用·未上传:_s5prime_lim_a_and_item_registers_2026_10_11.md〕` | 47,225 | ✅ |
| `d4b16b573cd0` | 32,795 | `〔幽灵引用·未上传:results___g5_ccp_execution_prereqs_2026_10_10.md〕` | 32,795 | ✅ |
| `d50569ddcca4` | 50,727 | `〔幽灵引用·未上传:results___round56c_d23_ad5_judgment_2026_10_10.md〕` | 50,727 | ✅ |
| `d523d9bea24e` | 41,540 | `〔幽灵引用·未上传:results___c_component4_three_items_judgment_2026_10_11.md〕` | 41,540 | ✅ |
| `d5590410823a` | 56,329 | `〔幽灵引用·未上传:_limb_reading_verdict_kv3s33_2026_10_01.md〕` | 56,329 | ✅ |
| `d62328c4f3a9` | 32,740 | `〔幽灵引用·未上传:results___p_refresh_registration_preliminary_2026_10_10.md〕` | 32,740 | ✅ |
| `d68307e2e863` | 41,598 | `〔幽灵引用·未上传:results___md_trigger_prereg_effectivity_2026_10_11.md〕` | 41,598 | ✅ |
| `d79c8f0c8fd4` | 32,780 | `〔本地路径已脱敏〕` | 32,780 | ✅ |
| `d7b400366a1f` | 32,810 | `〔幽灵引用·未上传:results___typeb_m_caliber_2026_10_10.md〕` | 32,810 | ✅ |
| `d7bc5cb50edf` | 33,976 | `〔幽灵引用·未上传:_g5_x4_dual_axis_interpretation_judgment_2026_10_10.md〕` | 33,976 | ✅ |
| `d8ec52809c02` | 34,269 | `〔幽灵引用·未上传:results___forgotten_recovery_register_2026_10_08.md〕` | 34,269 | ✅ |
| `d908c85c4da4` | 18,510 | `〔幽灵引用·未上传:tmp_movedout_2026_10_09__uncertain_release_2026_09___v5_glm_charlie_reread_ac74a04efeb2_2026_09_29.md〕` | 18,510 | ✅ |
| `d90c313b2c99` | 24,743 | `〔幽灵引用·未上传:results___s4_seedprime_seq_t1_only_supplement_2026_10_11.md〕` | 24,743 | ✅ |
| `d9b81cfc1571` | 22,408 | `〔幽灵引用·未上传:docs__V3X__DEPOSON_EMBEDDING_6WAY_THEORY_V0_2026_09_10.md〕` | 22,408 | ✅ |
| `da1a6ea941f2` | 28,233 | `〔幽灵引用·未上传:_round56_th4_two_field_reporting_resolution_2026_10_10.md〕` | 28,233 | ✅ |
| `da9fb0cad410` | 356,039 | `〔幽灵引用·未上传:results___v3_v4_achievements_inventory_3dir_2026_09_24.md〕` | 356,039 | ✅ |
| `db69ddfd15d8` | 29,670 | `〔幽灵引用·未上传:docs__V3X__KT_A1_SPEC_V0.1.md〕` | 29,670 | ✅ |
| `dc21e594ae6a` | 29,580 | `〔幽灵引用·未上传:results___b14_audit_f2f3_closure_register_2026_10_11.md〕` | 29,580 | ✅ |
| `dc3e67f7d4f5` | 31,652 | `〔幽灵引用·未上传:results___krj10_reverdict_after_r4_convergence_2026_10_11.md〕` | 31,652 | ✅ |
| `dc49602cad89` | 24,690 | `〔幽灵引用·未上传:_s4_heldout_sampling_seedprime_items_register_2026_10_10.md〕` | 24,690 | ✅ |
| `dc518753f244` | 27,946 | `〔本地路径已脱敏〕` | 27,946 | ✅ |
| `dc578941a2df` | 2,735 | `〔幽灵引用·未上传:_cleanup_resolve_2026_09_28.py〕` | 2,735 | ✅ |
| `dcad9d2da5bd` | 85,627 | `〔幽灵引用·未上传:results___archive_2026_09_20___coze_paper_v1_双审报告_2026_09_17.md〕` | 85,627 | ✅ |
| `dcb9123bb035` | 20,983 | `〔幽灵引用·未上传:docs__V3X__KT_D0_SPEC_V0.1.md〕` | 20,983 | ✅ |
| `dcd1fc53e83c` | 19,003 | `〔幽灵引用·未上传:_s4_heldout_sampling_seedprime_extractor_2026_10_10.py〕` | 19,003 | ✅ |
| `dd447d4ca5c2` | 11,347 | `〔幽灵引用·未上传:_cleanup_classify_out_2026_09_28.txt〕` | 11,347 | ✅ |
| `dd8a35858a6b` | 2,556 | `〔幽灵引用·未上传:_cleanup_probe_2026_09_28.py〕` | 2,556 | ✅ |
| `ddb383dcc51b` | 72,926 | `〔幽灵引用·未上传:results___t1_gate_closure_and_recompute_verdict_2026_10_01.md〕` | 72,926 | ✅ |
| `def2db2aea26` | 34,241 | `〔幽灵引用·未上传:results___j2_identifier_coupling_judgment_2026_10_11.md〕` | 34,241 | ✅ |
| `df3281e6871a` | 25,637 | `〔幽灵引用·未上传:_round53_rejudge_prereg_freeze_effectivity_register_2026_10_10.md〕` | 25,637 | ✅ |
| `df46bd4e2eec` | 16,555 | `〔幽灵引用·未上传:results___round56_ad8fix_effectivity_register_2026_10_10.md〕` | 16,555 | ✅ |
| `df5a43c97f7b` | 10,733 | `〔幽灵引用·未上传:_charlie_delivery_register_2026_10_08.md〕` | 10,733 | ✅ |
| `df7a80c3e61f` | 50,150 | `〔幽灵引用·未上传:results___round56_typeb_form_draft_2026_10_10.md〕` | 50,150 | ✅ |
| `dffe99f8d9fa` | 12,866 | `〔幽灵引用·未上传:deposon_team___designs__DELEGATION_CONFIGS_FOR_USER_B_2026_09_16.md〕` | 12,866 | ✅ |
| `e1121ea6b28c` | 41,620 | `〔幽灵引用·未上传:results___s7doubleprime_verification_2026_10_11.md〕` | 41,620 | ✅ |
| `e126cd454064` | 58,440 | `〔幽灵引用·未上传:results___round56_review_effectivity_register_6_2026_10_11.md〕` | 58,440 | ✅ |
| `e1373b419641` | 58,378 | `〔幽灵引用·未上传:_s5prime_double_lim_a_and_item_registers_2026_10_11.md〕` | 58,378 | ✅ |
| `e13bb36e5115` | 2,695 | `〔幽灵引用·未上传:_tdf_s4_final_2026_10_12.py〕` | 2,695 | ✅ |
| `e1b8a8b66c9d` | 28,362 | `〔幽灵引用·未上传:results___round56_th3_coverage_line_effectivity_register_2026_10_10.md〕` | 28,362 | ✅ |
| `e221b31c229a` | 24,240 | `〔幽灵引用·未上传:_codex_c4_values_followup_reply_intake_register_2026_10_10.md〕` | 24,240 | ✅ |
| `e2dc09b06007` | 24,398 | `〔幽灵引用·未上传:results___v4_closeout_account_reconciliation_2026_10_12.md〕` | 24,398 | ✅ |
| `e2f46324fb78` | 39,830 | `〔幽灵引用·未上传:results___g11_krj4_effectivity_register_2026_10_11.md〕` | 39,830 | ✅ |
| `e2fee828f1b8` | 29,951 | `〔幽灵引用·未上传:results___s1prime_trigger_caliber_reevaluation_2026_10_10.md〕` | 29,951 | ✅ |
| `e32529b0371b` | 85,861 | `〔幽灵引用·未上传:_s4_substrate_topup_addendum_2026_10_09.json〕` | 85,861 | ✅ |
| `e3ceee1988ad` | 110,510 | `〔幽灵引用·未上传:_r_pair_addendum_2026_10_09.json〕` | 110,510 | ✅ |
| `e495b054ef0b` | 17,069 | `〔幽灵引用·未上传:rescript_2026_09_27.md〕` | 17,069 | ✅ |
| `e506d97fb9fc` | 2,712 | `〔幽灵引用·未上传:_p_l_v3_phase2_finalize.log〕` | 2,712 | ✅ |
| `e552a449fc9b` | 121,123 | `〔幽灵引用·未上传:results___questionnaire_cards_intake_register_supplement_12_2026_10_10.md〕` | 121,123 | ✅ |
| `e5615dfdf907` | 10,307 | `〔幽灵引用·未上传:results___archive_2026_09_20___letter_to_kimi_push_v3_final_2026_09_17.md〕` | 10,307 | ✅ |
| `e56dd631a770` | 6,476 | `〔幽灵引用·未上传:_worker_openrouter_rag_run.log〕` | 6,476 | ✅ |
| `e5889a1a51bb` | 46,870 | `〔幽灵引用·未上传:results___round56_review_effectivity_register_4_2026_10_11.md〕` | 46,870 | ✅ |
| `e63e29fe22a0` | 16,401 | `〔幽灵引用·未上传:results___b01_recompute_sec4_2_erratum_2026_10_10.md〕` | 16,401 | ✅ |
| `e6599255e59d` | 13,295 | `〔幽灵引用·未上传:results___archive_2026_09_20__LETTER_TO_KIMI_GITHUB_UPLOAD_2026_09_18.md〕` | 13,295 | ✅ |
| `e71aecfebe91` | 24,634 | `〔幽灵引用·未上传:deposon_d_fix2_metric_verify_9m60c_2026_09_15.log〕` | 24,634 | ✅ |
| `e731a8ade38f` | 8,202 | `〔幽灵引用·未上传:_p_l_v3_phase1_runner.log〕` | 8,202 | ✅ |
| `e76d9b74029e` | 49,051 | `〔本地路径已脱敏〕` | 49,051 | ✅ |
| `e777c746f6d8` | 22,379 | `〔幽灵引用·未上传:results___stage3_extraction_verification_2026_10_11.md〕` | 22,379 | ✅ |
| `e7a1b16d5559` | 22,899 | `〔幽灵引用·未上传:results___codex_c4_unblock_reply_adoption_register_2026_10_10.md〕` | 22,899 | ✅ |
| `e875378b22ff` | 41,449 | `〔本地路径已脱敏〕` | 41,449 | ✅ |
| `e88528dbc37e` | 7,477 | `〔幽灵引用·未上传:deposon_team__plugins___tdf_s1c_2026_10_12.py〕` | 7,477 | ✅ |
| `e9232f54656e` | 5,677 | `〔幽灵引用·未上传:_pre_exec_report_kimi_2026_09_30.md〕` | 5,677 | ✅ |
| `e96ad684b886` | 18,023 | `〔幽灵引用·未上传:_audit_temp_stage1_tra_breakdown.py.bak〕` | 18,023 | ✅ |
| `e9e63476d717` | 10,267 | `〔幽灵引用·未上传:tmp_movedout_2026_09_28___cleanup_classify_out_2026_09_28.txt〕` | 10,267 | ✅ |
| `ea3f82948673` | 14,770 | `〔本地路径已脱敏〕` | 14,770 | ✅ |
| `ea7839df970c` | 41,322 | `〔本地路径已脱敏〕` | 41,322 | ✅ |
| `ead67cc76e5d` | 2,370 | `〔幽灵引用·未上传:_p_l_v3_phase2_closedsource_runner.log〕` | 2,370 | ✅ |
| `eb23f9346728` | 4,784 | `〔幽灵引用·未上传:TRAE_FIX_RECEIPT_2026_09_18.md〕` | 4,784 | ✅ |
| `eb5bee36daf4` | 22,195 | `〔幽灵引用·未上传:_round56_shortname_backfill_note_2026_10_10.md〕` | 22,195 | ✅ |
| `eb92d0ae25ed` | 26,158 | `〔幽灵引用·未上传:results___letters_archive_register_2026_10_01.md〕` | 26,158 | ✅ |
| `ebdc60a61dbc` | 12,470 | `〔幽灵引用·未上传:deposon_v41_flash_60cells_v2_2026_09_10.log〕` | 12,470 | ✅ |
| `ec5eb05066a9` | 31,567 | `〔幽灵引用·未上传:results___c4_math_corrections_E1_E2_execution_erratum_2026_10_10.md〕` | 31,567 | ✅ |
| `ecd9f5463bcb` | 42,115 | `〔幽灵引用·未上传:results___d1_backfill_intake_verdict_2026_10_01.md〕` | 42,115 | ✅ |
| `ecfa39768f34` | 2,687 | `〔幽灵引用·未上传:deposon_team__plugins___tdf_s4_final_2026_10_12.py〕` | 2,687 | ✅ |
| `ed112e78cbb8` | 22,157 | `〔幽灵引用·未上传:results___round56_shortname_backfill_note_2026_10_10.md〕` | 22,157 | ✅ |
| `eda36fcfe0df` | 450,751 | `〔幽灵引用·未上传:_v3_recheck_05_result_2026_09_28.json〕` | 450,751 | ✅ |
| `edb4685a740b` | 20,931 | `〔幽灵引用·未上传:deposon_team__plugins___pg_v01_compute.py〕` | 20,931 | ✅ |
| `ee0f43b1fe83` | 52,785 | `〔幽灵引用·未上传:_s4_heldout_sampling_seedthird_extractor_2026_10_11.py〕` | 52,785 | ✅ |
| `ee185be5f7da` | 13,863 | `〔幽灵引用·未上传:results___pi_card_123_adoption_and_gate_one_request_2026_10_11.md〕` | 13,863 | ✅ |
| `ee2c0b0ccc5a` | 13,254 | `〔幽灵引用·未上传:results___register3_bytes_erratum_2026_10_11.md〕` | 13,254 | ✅ |
| `ee4eddfad35f` | 8,439 | `〔幽灵引用·未上传:deposon_team___designs__v3x_dispatch_log_2026_09_16.md〕` | 8,439 | ✅ |
| `ee9375365231` | 12,617 | `〔幽灵引用·未上传:results___five_stage_chain_design_reconstruction_2026_10_12.md〕` | 12,617 | ✅ |
| `ef0bb966d450` | 27,360 | `〔幽灵引用·未上传:results___c4_unblock_reply_independent_review_2026_10_10.md〕` | 27,360 | ✅ |
| `f038e15fe156` | 10,286 | `〔幽灵引用·未上传:_letter_review_bob_w3_commission_2026_09_30.md〕` | 10,286 | ✅ |
| `f03cb6416a01` | 3,444 | `〔幽灵引用·未上传:deposon_volcengine_minimax_m3_30cells_2026_09_10.log〕` | 3,444 | ✅ |
| `f06b8ebb594c` | 27,758 | `〔幽灵引用·未上传:results___typeb_m_registration_2026_10_10.md〕` | 27,758 | ✅ |
| `f0ee0664b7e3` | 13,967 | `〔幽灵引用·未上传:results___archive_2026_09_20___letter_to_kimi_push_v3_final_v2_2026_09_17.md〕` | 13,967 | ✅ |
| `f1e451d60df1` | 54,511 | `〔幽灵引用·未上传:_pi_effectivity_declaration_register_2026_10_11.md〕` | 54,511 | ✅ |
| `f2253efbeb13` | 14,101 | `〔幽灵引用·未上传:_krj10_terminal_verdict_closure_2026_10_11.md〕` | 14,101 | ✅ |
| `f22659a123c5` | 21,827 | `〔幽灵引用·未上传:results___round56_registration_supplement_2026_10_10.md〕` | 21,827 | ✅ |
| `f286e357b13f` | 23,050 | `〔幽灵引用·未上传:_receipt_disposition_register_2026_10_08.md〕` | 23,050 | ✅ |
| `f31efedb713a` | 30,627 | `〔幽灵引用·未上传:deposon_team__plugins___v3r1p1_21_ktb1_distortion_2026_09_27.py〕` | 30,627 | ✅ |
| `f33a29327e11` | 8,885 | `〔幽灵引用·未上传:deposon_dpath_cross_modal_2026_09_10.log〕` | 8,885 | ✅ |
| `f3448246455c` | 59,289 | `〔幽灵引用·未上传:results___g5_rejudgment_construction_question_judgment_2026_10_10.md〕` | 59,289 | ✅ |
| `f3d03ea79519` | 46,908 | `〔幽灵引用·未上传:_round56_review_effectivity_register_4_2026_10_11.md〕` | 46,908 | ✅ |
| `f3d8f45561f5` | 40,459 | `〔幽灵引用·未上传:results___seed_double_criterion_draft_2026_10_11.md〕` | 40,459 | ✅ |
| `f401a22768be` | 17,158 | `〔幽灵引用·未上传:_v2_stage1_60cells.console.log〕` | 17,158 | ✅ |
| `f4501d50cb6c` | 43,039 | `〔幽灵引用·未上传:results___pc_d1_d3_2026_09_15.py〕` | 43,039 | ✅ |
| `f462ad619013` | 110,512 | `〔幽灵引用·未上传:results___r_pair_addendum_2026_10_09.json〕` | 110,512 | ✅ |
| `f479531ce574` | 38,621 | `〔幽灵引用·未上传:results___b01_new_key_classification_2026_10_10.md〕` | 38,621 | ✅ |
| `f48cd3b0d562` | 42,735 | `〔幽灵引用·未上传:results___pending_rulings_drafts_2026_10_11.md〕` | 42,735 | ✅ |
| `f49d7e4235f7` | 27,824 | `〔幽灵引用·未上传:_zero_reading_judgment_2026_10_10.md〕` | 27,824 | ✅ |
| `f526cceb4c75` | 50,747 | `〔本地路径已脱敏〕` | 50,747 | ✅ |
| `f533096eecba` | 42,115 | `〔幽灵引用·未上传:_d1_backfill_intake_verdict_2026_10_01.md〕` | 42,115 | ✅ |
| `f56ccb6de842` | 14,750 | `〔幽灵引用·未上传:results___lim_aperiod_adoption_and_label_correction_2026_10_11.md〕` | 14,750 | ✅ |
| `f59136835d7d` | 42,775 | `〔幽灵引用·未上传:_pending_rulings_drafts_2026_10_11.md〕` | 42,775 | ✅ |
| `f661a9c43455` | 27,778 | `〔本地路径已脱敏〕` | 27,778 | ✅ |
| `f686df361df6` | 28,654 | `〔本地路径已脱敏〕` | 28,654 | ✅ |
| `f6c1e86b1542` | 11,575 | `〔幽灵引用·未上传:TRAE_DAILY_AUDIT_LETTER_2026_09_18.md〕` | 11,575 | ✅ |
| `f6e9704ac575` | 49,754 | `〔幽灵引用·未上传:_round56r9r10_dispositions_register_2026_10_10.md〕` | 49,754 | ✅ |
| `f747cbdd3ce0` | 64,833 | `〔幽灵引用·未上传:results___q3_c1c4_l282_transposition_fix_executor_2026_10_09.py〕` | 64,833 | ✅ |
| `f8110f41c607` | 19,224 | `〔幽灵引用·未上传:_p_l_v3_phase1_finalize_2026_09_17.py〕` | 19,224 | ✅ |
| `f8394583129f` | 42,907 | `〔幽灵引用·未上传:results___v3_recheck_prereg_v1p1_2026_09_27.md〕` | 42,907 | ✅ |
| `f85eddf2fc03` | 2,542 | `〔幽灵引用·未上传:_p_l_v3_phase2_glm53.log〕` | 2,542 | ✅ |
| `f890ddd6e453` | 12,781 | `〔幽灵引用·未上传:_u_closure_execution_register_2026_10_09.md〕` | 12,781 | ✅ |
| `f8c1722d4d67` | 10,255 | `〔幽灵引用·未上传:_kd_doc1_correction_adoption_register_2026_10_11.md〕` | 10,255 | ✅ |
| `f93621af5205` | 9,579 | `〔幽灵引用·未上传:_gate_one_pi_endorsement_register_2026_10_12.md〕` | 9,579 | ✅ |
| `f9b7ad758bcb` | 33,887 | `〔本地路径已脱敏〕` | 33,887 | ✅ |
| `f9f61cac47b0` | 50,427 | `〔本地路径已脱敏〕` | 50,427 | ✅ |
| `faf2d978ef74` | 29,936 | `〔幽灵引用·未上传:results___stage3_readings_verification_2026_10_11.md〕` | 29,936 | ✅ |
| `fb5c677e72a4` | 58,338 | `〔幽灵引用·未上传:results___s5prime_double_lim_a_and_item_registers_2026_10_11.md〕` | 58,338 | ✅ |
| `fc27f4f3a1bf` | 3,224 | `〔幽灵引用·未上传:tmp_movedout_2026_09_28___cleanup_classify_2026_09_28.py〕` | 3,224 | ✅ |
| `fdd3ccd3a8a1` | 39,961 | `〔幽灵引用·未上传:results___round54_g5_dispositions_register_2026_10_10.md〕` | 39,961 | ✅ |
| `fde59293f674` | 15,569 | `〔幽灵引用·未上传:_thv3_15_parallel_seed_double_note_2026_10_11.md〕` | 15,569 | ✅ |
| `fdf02a9a0447` | 21,966 | `〔幽灵引用·未上传:_s4_heldout_seedprime_verification_2026_10_10.md〕` | 21,966 | ✅ |
| `fe1fc73afb48` | 18,454 | `〔幽灵引用·未上传:_b01_recompute_authorization_supplement_2026_10_11.md〕` | 18,454 | ✅ |
| `fe80596a9a6f` | 67,955 | `〔幽灵引用·未上传:_t1_exp2_executor_2026_10_09.py〕` | 67,955 | ✅ |
| `0382feb27519` | 8,727 | `〔幽灵引用·未上传:_coze_online_v3_d7format_2026_09_18.md〕` | 8,727 | ✅ |
| `05353829c864` | 16,829 | `〔幽灵引用·未上传:_v5_item21_patched_b1_semB_none_skip.py〕` | 16,829 | ✅ |
| `05ac84a856ad` | 2,812 | `〔幽灵引用·未上传:_v4_wide_s4_verify_2026_09_27.py〕` | 2,812 | ✅ |
| `07f910b7397a` | 17,252 | `〔幽灵引用·未上传:_v4_pi_cot_v3_dataset_addendum_s3_d7_2026_09_29.json〕` | 17,252 | ✅ |
| `0deb7931c842` | 6,101 | `〔幽灵引用·未上传:_v4_wide_s7_fix_2026_09_27.py〕` | 6,101 | ✅ |
| `0e2301038e1c` | 46,909 | `〔幽灵引用·未上传:_v4_pi_cot_v3_dataset_addendum_s3_d1fill_2026_10_01.json〕` | 46,909 | ✅ |
| `11548fa9c347` | 6,132 | `〔幽灵引用·未上传:_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json〕` | 6,132 | ✅ |
| `158b0518e100` | 7,376 | `〔幽灵引用·未上传:TRAE_V3_CODE_IMPROVEMENT_LETTER_2026_09_16.md〕` | 7,376 | ✅ |
| `1ace80bfb19c` | 72,934 | `〔幽灵引用·未上传:PRE_SUB_0b5fb78727c2__t1_gate_closure_and_recompute_verdict_2026_10_01.md.md〕` | 72,934 | ✅ |
| `1f1904c9d786` | 16,587 | `〔幽灵引用·未上传:_v4_pi_cot_v3_dataset_addendum_d5_2026_09_27.json〕` | 16,587 | ✅ |
| `22e371480238` | 3,399 | `〔幽灵引用·未上传:_v4_wide_s9_final_2026_09_27.py〕` | 3,399 | ✅ |
| `2c84943121fb` | 7,668 | `〔幽灵引用·未上传:_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json〕` | 7,668 | ✅ |
| `2d02d5547f4f` | 16,768 | `〔幽灵引用·未上传:_v5_item21_patched_b1_semA_none_default.py〕` | 16,768 | ✅ |
| `30a2b0875241` | 1,707 | `〔幽灵引用·未上传:_v4_wide_s3b_uuidctx_2026_09_27.py〕` | 1,707 | ✅ |
| `320eb0da8f13` | 4,000 | `〔幽灵引用·未上传:_v4_wide_s2_scan_2026_09_27.py〕` | 4,000 | ✅ |
| `368bdd601d40` | 10,751 | `〔幽灵引用·未上传:_v5_theory_input_acquisition_request_2026_09_29.md〕` | 10,691 | — |
| `4004f2c5eec3` | 12,975 | `〔幽灵引用·未上传:_v4_pi_cot_v3_dataset_v1p3_2026_09_27.json〕` | 12,975 | ✅ |
| `47a98042d24a` | 13,127 | `〔幽灵引用·未上传:_v5_b14_1_k04_caliber_fixation_2026_09_29.md〕` | 13,127 | ✅ |
| `4815f547278f` | 3,583 | `〔幽灵引用·未上传:_v5_wa_s2b_2026_09_30.py〕` | 3,583 | ✅ |
| `49aaf6223a34` | 2,490 | `〔幽灵引用·未上传:_v4_wide_s3c_keydetail_2026_09_27.py〕` | 2,490 | ✅ |
| `4b785e9b99bd` | 4,742 | `〔幽灵引用·未上传:_v5_wa_s3_fix_2026_09_30.py〕` | 4,742 | ✅ |
| `4de634e0ad8e` | 7,566 | `〔幽灵引用·未上传:_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json〕` | 7,566 | ✅ |
| `52f222502a31` | 465,366 | `〔幽灵引用·未上传:_coze_online_v4_d7format_2026_09_26.pdf〕` | 465,366 | ✅ |
| `53b844a9e184` | 16,036 | `〔幽灵引用·未上传:_v5_item21_patched_b2_semA_none_default.py〕` | 16,036 | ✅ |
| `5400179aa0e1` | 11,660 | `〔幽灵引用·未上传:_coze_online_v3_final_2026_09_18.md〕` | 11,660 | ✅ |
| `570275c1731a` | 18,714 | `〔幽灵引用·未上传:_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json〕` | 18,714 | ✅ |
| `57f620eaca69` | 66,339 | `〔幽灵引用·未上传:_docwriter_wt2_enum_final_2026_09_30.tsv〕` | 66,339 | ✅ |
| `581e5d0565e2` | 3,168 | `〔幽灵引用·未上传:_v5_wa_s2c_2026_09_30.py〕` | 3,168 | ✅ |
| `5bf93f2343ff` | 3,514 | `〔幽灵引用·未上传:_v4_wide_s8_fix3_2026_09_27.py〕` | 3,514 | ✅ |
| `5cb3a1cbb369` | 19,615 | `〔幽灵引用·未上传:_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json〕` | 19,615 | ✅ |
| `65ad8aacb53d` | 10,257 | `〔幽灵引用·未上传:_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json〕` | 10,257 | ✅ |
| `66362bf125e7` | 374,072 | `〔幽灵引用·未上传:_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json〕` | 374,072 | ✅ |
| `68c3e712d66f` | 7,476 | `〔幽灵引用·未上传:_coze_online_v3_2026_09_18.md〕` | 7,476 | ✅ |
| `712964f3eb17` | 16,723 | `〔幽灵引用·未上传:_v5_b16_mq11_case_2026_09_29.md〕` | 16,723 | ✅ |
| `713ec0c3bf0c` | 4,351 | `〔幽灵引用·未上传:_v5_wa_s1_2026_09_30.py〕` | 4,351 | ✅ |
| `718926199008` | 19,731 | `〔幽灵引用·未上传:_v4_01_knifeedge_independent_review_2026_09_29.md〕` | 19,731 | ✅ |
| `73a7d1558159` | 16,097 | `〔幽灵引用·未上传:_v5_item21_patched_b2_semB_none_skip.py〕` | 16,097 | ✅ |
| `77ccf7e3f367` | 8,983 | `〔幽灵引用·未上传:_rj5_convention_check_2026_09_27.out.json〕` | 8,983 | ✅ |
| `85cfbc2a5a06` | 20,212 | `〔本地路径已脱敏〕` | 20,212 | ✅ |
| `8c0300e90060` | 16,025 | `〔幽灵引用·未上传:_v4_pi_cot_v3_dataset.json〕` | 16,025 | ✅ |
| `8c45f5bec3dc` | 19,755 | `〔幽灵引用·未上传:_v5_b16_idx23_blindrate_verify_2026_09_29.md〕` | 19,755 | ✅ |
| `8ec92ab97e47` | 22,196 | `〔幽灵引用·未上传:_t1_substrate_gap_precondition_2026_10_01.md〕` | 22,196 | ✅ |
| `945e2a9c7605` | 58,581 | `〔幽灵引用·未上传:_v4_pi_cot_v3_dataset_addendum_d8_bhalf_2026_09_30.json〕` | 58,581 | ✅ |
| `95fff0a09d87` | 14,722 | `〔幽灵引用·未上传:_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json〕` | 14,722 | ✅ |
| `9a23a8f01f35` | 4,950 | `〔幽灵引用·未上传:_v4_wt_s5_verify_2026_09_27.py〕` | 4,950 | ✅ |
| `a047342a5444` | 19,296 | `〔本地路径已脱敏〕` | 19,296 | ✅ |
| `ac3e45e5b0a6` | 1,836 | `〔本地路径已脱敏〕` | 1,836 | ✅ |
| `b3de03b9c386` | 1,546 | `〔幽灵引用·未上传:_v4_wide_s1b_inv2_2026_09_27.py〕` | 1,546 | ✅ |
| `b60f81e8f595` | 19,214 | `〔幽灵引用·未上传:_v4_pi_cot_v3_dataset_addendum_d6_2026_09_28.json〕` | 19,214 | ✅ |
| `b937094b1e44` | 5,154 | `〔幽灵引用·未上传:TRAE_CODE_IMPROVEMENT_LETTER_2026_09_17.md〕` | 5,154 | ✅ |
| `bbabf547f6df` | 6,666 | `〔幽灵引用·未上传:_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json〕` | 6,666 | ✅ |
| `c2bcd2e61452` | 26,931 | `〔幽灵引用·未上传:_v5_b16_1dcritical_lit_search_2026_09_29.md〕` | 26,931 | ✅ |
| `d0b2e5bfd237` | 27,009 | `〔幽灵引用·未上传:_v4_pi_cot_v3_dataset_addendum_d6b_2026_09_28.json〕` | 27,009 | ✅ |
| `d591872191e1` | 2,647 | `〔幽灵引用·未上传:_v4_wide_s3_keyscan_2026_09_27.py〕` | 2,647 | ✅ |
| `d6a600658c5c` | 1,693 | `〔幽灵引用·未上传:COMPILE_SUMMARY.txt〕` | 1,693 | ✅ |
| `daf43fb20421` | 2,495 | `〔幽灵引用·未上传:_v4_wide_s6_unrefscan_2026_09_27.py〕` | 2,495 | ✅ |
| `df5e8e3c7f2d` | 4,429 | `〔本地路径已脱敏〕` | 4,429 | ✅ |
| `df968dda4772` | 14,304 | `〔幽灵引用·未上传:_v5_b18_coding_caliber_2026_09_29.md〕` | 14,304 | ✅ |
| `df9efa13fa0a` | 15,778 | `〔幽灵引用·未上传:_v5_item21_patched_b3_semA_none_default.py〕` | 15,778 | ✅ |
| `e8c841c4559e` | 16,262 | `〔幽灵引用·未上传:_v5_b16_dual_caliber_rule_2026_09_29.md〕` | 16,262 | ✅ |
| `ea7df8d6c21b` | 15,839 | `〔幽灵引用·未上传:_v5_item21_patched_b3_semB_none_skip.py〕` | 15,839 | ✅ |
| `f1c7d5d987c7` | 20,179 | `〔幽灵引用·未上传:_kd_writing_convention_guidance_2026_10_09.md〕` | 20,179 | ✅ |
| `f369e5c35f8a` | 3,571 | `〔幽灵引用·未上传:LETTER_FROM_TRAE_SELFCHECK_FIX_2026_09_15.md〕` | 3,571 | ✅ |
| `f59b97601d73` | 11,589 | `〔幽灵引用·未上传:_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json〕` | 11,589 | ✅ |
| `f60d3f3eca8b` | 5,145 | `〔幽灵引用·未上传:LETTER_FROM_TRAE_3RISK_2026_09_11.md〕` | 5,145 | ✅ |
| `f91692efd347` | 4,103 | `〔幽灵引用·未上传:_v4_pi_cot_v2_dataset_addendum_2026_09_24.json〕` | 4,103 | ✅ |
| `fc04fe9be042` | 20,194 | `〔幽灵引用·未上传:_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json〕` | 20,194 | ✅ |
| `fc0a48202902` | 12,672 | `〔幽灵引用·未上传:_v4_pi_cot_v2_dataset.json〕` | 12,672 | ✅ |
| `fd8c3dbd4794` | 13,608 | `〔幽灵引用·未上传:_v5_b18_single_count_fixation_2026_09_29.md〕` | 13,608 | ✅ |
| `01693e7d0247` | 9,226 | `〔幽灵引用·未上传:_t15_update_result.py〕` | 9,226 | ✅ |
| `0191bd6e8c2d` | 6,071 | `〔幽灵引用·未上传:_en_verify_2026_09_28.py〕` | 6,071 | ✅ |
| `020b1e1f8278` | 4,282 | `〔幽灵引用·未上传:_pkf34_f34.py〕` | 4,282 | ✅ |
| `07046a502a45` | 5,903 | `〔幽灵引用·未上传:_pkf34_final.py〕` | 5,903 | ✅ |
| `0b431bc0f9de` | 62,860 | `〔幽灵引用·未上传:_kimi_receipt_authority_rulings_effect_2026_10_18.md〕` | 62,860 | ✅ |
| `0bd4d69d5ed5` | 3,912 | `〔幽灵引用·未上传:_cpatomic_pycache_pre_2026_09_28.py〕` | 3,912 | ✅ |
| `0df51a7e4e63` | 6,737 | `〔幽灵引用·未上传:_t15r2_verify.py〕` | 6,737 | ✅ |
| `0e189cc246cf` | 1,382 | `〔幽灵引用·未上传:_r4_cleanup_worker_nearmiss_2026_09_29.py〕` | 1,382 | ✅ |
| `11f90ecb2e98` | 8,018 | `〔幽灵引用·未上传:_rj5_convention_check_2026_09_27.py〕` | 8,018 | ✅ |
| `13004c626ba2` | 9,476 | `〔幽灵引用·未上传:_v5_c5_b_fetch_raw_embeddings.py〕` | 9,476 | ✅ |
| `13b028f782d7` | 29,361 | `〔幽灵引用·未上传:_cpatomic_register_2026_09_28.json〕` | 29,361 | ✅ |
| `15ea982a00c6` | 33,410 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_18_v97.md〕` | 33,410 | ✅ |
| `16d2e4b20bc1` | 5,164 | `〔幽灵引用·未上传:_cpatomic_pycache_post_2026_09_28.py〕` | 5,164 | ✅ |
| `17da548d7319` | 7,752 | `〔幽灵引用·未上传:_compute_metrics.py〕` | 7,752 | ✅ |
| `18a9f0bc6409` | 29,664 | `〔幽灵引用·未上传:_kd_19_ambiguous_tags_rejudge_rewrite_register_2026_10_10.md〕` | 29,664 | ✅ |
| `1922769aa303` | 21,678 | `〔幽灵引用·未上传:_kimi_postexec_receipt_verification_2026_10_18.md〕` | 21,678 | ✅ |
| `1b151e8de4f8` | 34,895 | `〔幽灵引用·未上传:_run_recheck_r1.py〕` | 34,895 | ✅ |
| `1b5fd9ed2a51` | 1,638 | `〔幽灵引用·未上传:_en_verify3_2026_09_28.py〕` | 1,638 | ✅ |
| `1bb17e5de63d` | 1,029 | `〔幽灵引用·未上传:_tmp_inspect_5model.py〕` | 1,029 | ✅ |
| `1d22d0187f46` | 54,315 | `〔幽灵引用·未上传:_stage3_close_and_cmp2_rulings_effect_2026_10_18.md〕` | 54,315 | ✅ |
| `1d2d82bd994e` | 39,653 | `〔幽灵引用·未上传:_v3r1_threshold_final_path_judgment_2026_10_10.md〕` | 39,653 | ✅ |
| `1f31c749b9ff` | 82,690 | `〔幽灵引用·未上传:_remote_delete_face_pullback_register_2026_10_18.md〕` | 82,690 | ✅ |
| `20d929b85e09` | 2,550 | `〔幽灵引用·未上传:_e48_docwriter_chain.py〕` | 2,550 | ✅ |
| `2113bef8bb10` | 26,654 | `〔幽灵引用·未上传:_run_final.py〕` | 26,654 | ✅ |
| `222239e99b8a` | 1,689 | `〔幽灵引用·未上传:_v5_qwen_retry_candidates_20260929.py〕` | 1,689 | ✅ |
| `22a7def760e3` | 2,411 | `〔幽灵引用·未上传:_r4_cleanup_worker_scan_2026_09_29.py〕` | 2,411 | ✅ |
| `2382e51cbb4f` | 51,739 | `〔幽灵引用·未上传:_scroll_wave1_four_rulings_effect_2026_10_18.md〕` | 51,739 | ✅ |
| `2402a61a60f2` | 2,756 | `〔幽灵引用·未上传:_t15_inspect4.py〕` | 2,756 | ✅ |
| `24177ad1b147` | 5,968 | `〔幽灵引用·未上传:_rj5_mapping_test_2026_09_27.py〕` | 5,968 | ✅ |
| `26b5b81a2534` | 3,743 | `〔幽灵引用·未上传:_r4_key_scan_2026_09_24.py〕` | 3,743 | ✅ |
| `276b959b5413` | 5,639 | `〔幽灵引用·未上传:_pkf34_v12.py〕` | 5,639 | ✅ |
| `29aaabc97a4b` | 143,261 | `〔幽灵引用·未上传:_v5_proxy_temp_T1.5.json〕` | 143,261 | ✅ |
| `29f020a5b3ba` | 57,912 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_18_v102.md〕` | 57,912 | ✅ |
| `2a7c5eaefee4` | 63,300 | `〔幽灵引用·未上传:_pending_rulings_triage_2026_10_18.md〕` | 63,300 | ✅ |
| `2ac93d8110c3` | 3,561 | `〔幽灵引用·未上传:_r4_cleanup_worker_keyscan_2026_09_29.py〕` | 3,561 | ✅ |
| `2c441b0d9326` | 49,471 | `〔幽灵引用·未上传:_verdict_pack_d_prep_2026_10_01.md〕` | 49,471 | ✅ |
| `2eb998b23b93` | 33,880 | `〔幽灵引用·未上传:_g5_displacement_threshold_c_approval_effect_and_trigger_eval_2026_10_10.md〕` | 33,880 | ✅ |
| `2ec601aa97d3` | 7,251 | `〔幽灵引用·未上传:_post_execution_report_kimi_2026_10_18.md〕` | 7,251 | ✅ |
| `2f06040fc008` | 46,595 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_18_v92.md〕` | 46,595 | ✅ |
| `309a3f0e7a09` | 1,036 | `〔幽灵引用·未上传:_c5_feasibility_probe.py〕` | 1,036 | ✅ |
| `30e47d32a770` | 3,880 | `〔幽灵引用·未上传:_t15_inspect7.py〕` | 3,880 | ✅ |
| `3140b222ec01` | 17,272 | `〔幽灵引用·未上传:_tail3_atomic_make_2026_09_29.py〕` | 17,272 | ✅ |
| `328c8ae04f63` | 4,397 | `〔幽灵引用·未上传:_reviewer_a_audit_tmp.py〕` | 4,397 | ✅ |
| `338b864817b6` | 2,763 | `〔幽灵引用·未上传:_run_day_inventory_table_2026_09_27.py〕` | 2,763 | ✅ |
| `359b86c6902e` | 40,576 | `〔幽灵引用·未上传:_run_d8_bhalf_addendum_2026_09_30.py〕` | 40,576 | ✅ |
| `3a539beb90ec` | 27,133 | `〔幽灵引用·未上传:_s4_v31_regen_gold_register_2026_10_10.md〕` | 27,133 | ✅ |
| `3b088784aca1` | 3,632 | `〔幽灵引用·未上传:_trae_audit_part2.py〕` | 3,632 | ✅ |
| `3b5fc95ac9c6` | 121,848 | `〔幽灵引用·未上传:_closure_sweep_r2_2026_10_18.md〕` | 121,848 | ✅ |
| `3f107092cef8` | 9,819 | `〔本地路径已脱敏〕` | 9,819 | ✅ |
| `3fade1e7f765` | 2,460 | `〔幽灵引用·未上传:_inspect_10cells.py〕` | 2,460 | ✅ |
| `40679de7627a` | 3,730 | `〔幽灵引用·未上传:_t15r2_inspect.py〕` | 3,730 | ✅ |
| `40784ebff5bd` | 33,932 | `〔幽灵引用·未上传:_v3_s_phrasetemplate_prereg_v1_2026_09_27.md〕` | 33,932 | ✅ |
| `42328dc97335` | 2,712 | `〔幽灵引用·未上传:_t15_inspect5.py〕` | 2,712 | ✅ |
| `446456760fe3` | 1,628 | `〔幽灵引用·未上传:_n1_n2_check.py〕` | 1,628 | ✅ |
| `457b83c42f3d` | 13,607 | `〔幽灵引用·未上传:_e49_c1.md〕` | 13,607 | ✅ |
| `4658e9ff764d` | 6,528 | `〔幽灵引用·未上传:_v5_c5_b_clause4_consistency_check.py〕` | 6,528 | ✅ |
| `471962695262` | 1,234 | `〔幽灵引用·未上传:_t15_inspect6.py〕` | 1,234 | ✅ |
| `47a9c9fad721` | 8,807 | `〔幽灵引用·未上传:_patch21_make.py〕` | 8,807 | ✅ |
| `487781f03f7f` | 39,077 | `〔幽灵引用·未上传:_v3r1_threshold_path4_draft_2026_10_10.md〕` | 39,077 | ✅ |
| `48de61d702ac` | 1,558 | `〔幽灵引用·未上传:_postcheck_v16_alt_stdout.txt〕` | 1,558 | ✅ |
| `4a124466a1da` | 17,872 | `〔幽灵引用·未上传:_e49_c2.md〕` | 17,872 | ✅ |
| `4b2d2c2b8125` | 20,812 | `〔幽灵引用·未上传:_tmp_disposal_register_2026_10_10.md〕` | 20,812 | ✅ |
| `4b6afbfa9964` | 3,280 | `〔幽灵引用·未上传:_r3_header_fix_2026_09_28.py〕` | 3,280 | ✅ |
| `4c101994598d` | 51,967 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_18_v93.md〕` | 51,967 | ✅ |
| `4d3ddbee1789` | 4,366 | `〔幽灵引用·未上传:_run2.py〕` | 4,366 | ✅ |
| `4f5528d06f7c` | 67,299 | `〔幽灵引用·未上传:_commission_v04_approval_rulings_effect_2026_10_18.md〕` | 67,299 | ✅ |
| `509f3fdba386` | 2,454 | `〔幽灵引用·未上传:_aggregate_10cells_v4.py〕` | 2,454 | ✅ |
| `518b209d97b4` | 68,053 | `〔幽灵引用·未上传:_mini_round_6_7_settlement_register_2026_10_01.md〕` | 68,053 | ✅ |
| `5437c6a9d6c1` | 11,036 | `〔幽灵引用·未上传:_cpatomic_verify_2026_09_28.py〕` | 11,036 | ✅ |
| `55dea38ae84b` | 6,687 | `〔幽灵引用·未上传:_temp_volc_test.py〕` | 6,687 | ✅ |
| `5832a5c071d0` | 27,384 | `〔幽灵引用·未上传:_t1_temp_axis_retirement_judgment_2026_10_10.md〕` | 27,384 | ✅ |
| `584015ddcd11` | 3,501 | `〔幽灵引用·未上传:_execswitch_verify_2026_09_28.py〕` | 3,501 | ✅ |
| `58b444fc324b` | 79,234 | `〔幽灵引用·未上传:_u10_s3_denominator_rulings_effect_2026_10_18.md〕` | 79,234 | ✅ |
| `5ab36dc862a5` | 1,870 | `〔幽灵引用·未上传:_en_verify2_2026_09_28.py〕` | 1,870 | ✅ |
| `5acda04b5429` | 5,709 | `〔幽灵引用·未上传:_b12_q4_adjacent_2026_09_29.py〕` | 5,709 | ✅ |
| `5b1af280bf83` | 2,699 | `〔幽灵引用·未上传:_tail3_atomic_landing_check_2026_09_29.py〕` | 2,699 | ✅ |
| `5cc9aba339be` | 71,453 | `〔幽灵引用·未上传:_scroll_wave5_four_rulings_effect_2026_10_18.md〕` | 71,453 | ✅ |
| `5f8667592152` | 5,039 | `〔幽灵引用·未上传:_e48_c1.md〕` | 5,039 | ✅ |
| `617e253d881a` | 1,942 | `〔幽灵引用·未上传:_t15_inspect2.py〕` | 1,942 | ✅ |
| `635767454632` | 14,122 | `〔幽灵引用·未上传:_thirdparty_16_overwrite_necessity_2026_10_18.md〕` | 14,122 | ✅ |
| `65b5f8e82a58` | 2,636 | `〔幽灵引用·未上传:_tail3_atomic_refs_2026_09_29.py〕` | 2,636 | ✅ |
| `69494189752d` | 1,907 | `〔幽灵引用·未上传:_b12_tables_2026_09_29.py〕` | 1,907 | ✅ |
| `69e69cbc51f0` | 4,079 | `〔幽灵引用·未上传:_r4_key_scan_r1_files_2026_09_27.py〕` | 4,079 | ✅ |
| `6b33b016873f` | 37,227 | `〔幽灵引用·未上传:_morning_brief_pending_rulings_2026_10_18.md〕` | 37,227 | ✅ |
| `6bfa06d24bfa` | 35,197 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_18_v91.md〕` | 35,197 | ✅ |
| `6c28a787fc97` | 1,248 | `〔幽灵引用·未上传:_e48_docwriter_enum.py〕` | 1,248 | ✅ |
| `6cf8666d955b` | 16,994 | `〔幽灵引用·未上传:_t1_prereg_revision_qwen_temp_sweep_2026_10_09.md〕` | 16,994 | ✅ |
| `7031bd2a1995` | 37,035 | `〔幽灵引用·未上传:_five_zero_recheck_evidence_2026_10_18.md〕` | 37,035 | ✅ |
| `72cb4f23a08d` | 46,191 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_18_v101.md〕` | 46,191 | ✅ |
| `730f2037e8b8` | 51,949 | `〔幽灵引用·未上传:dw99_stage2.md〕` | 51,949 | ✅ |
| `73ed0d6e543e` | 43,856 | `〔幽灵引用·未上传:_stage5_preparation_design_2026_10_18.md〕` | 43,856 | ✅ |
| `74dbe52d8af4` | 35,256 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_18_v90.md〕` | 35,256 | ✅ |
| `76698ca84d3a` | 2,309 | `〔幽灵引用·未上传:_run_frozen_0touch_verify_2026_09_27.py〕` | 2,309 | ✅ |
| `794b2b55de0f` | 143,345 | `〔幽灵引用·未上传:_v5_proxy_temp_T0.3.json〕` | 143,345 | ✅ |
| `79b6566290c2` | 2,369 | `〔幽灵引用·未上传:_en_final_2026_09_28.py〕` | 2,369 | ✅ |
| `7aaa1b5d521f` | 30,875 | `〔幽灵引用·未上传:_run_v3r1_relabel.py〕` | 30,875 | ✅ |
| `7aad941f9485` | 3,866 | `〔幽灵引用·未上传:_patch21_run.py〕` | 3,866 | ✅ |
| `7af140c886b7` | 5,966 | `〔幽灵引用·未上传:_e48_c2.md〕` | 5,966 | ✅ |
| `7b7382214f1a` | 17,550 | `〔幽灵引用·未上传:_run_d4_relabel_addendum.py〕` | 17,550 | ✅ |
| `7cefb4ba8dc3` | 4,890 | `〔幽灵引用·未上传:_b12_q1_refs_2026_09_29.py〕` | 4,890 | ✅ |
| `7d79c2edb86c` | 1,909 | `〔幽灵引用·未上传:_r4_cleanup_worker_keycount_2026_09_29.py〕` | 1,909 | ✅ |
| `7e05748bc4b0` | 17,106 | `〔幽灵引用·未上传:_patch21_emit.py〕` | 17,106 | ✅ |
| `7fc5c5a60075` | 7,140 | `〔幽灵引用·未上传:_b12_q4_exact_2026_09_29.py〕` | 7,140 | ✅ |
| `826ea32705ed` | 32,296 | `〔幽灵引用·未上传:_kv3s_3_2_terminal_verdict_2026_10_01.md〕` | 32,296 | ✅ |
| `83706e76a67c` | 6,563 | `〔幽灵引用·未上传:_e48_c3.md〕` | 6,563 | ✅ |
| `841b83636d65` | 2,329 | `〔幽灵引用·未上传:_e48_apply.py〕` | 2,329 | ✅ |
| `846f4d14836f` | 41,392 | `〔幽灵引用·未上传:_t1_temp_axis_new_experiment_design_2026_10_09.md〕` | 41,392 | ✅ |
| `859ce3ca4928` | 1,435 | `〔幽灵引用·未上传:_final_sha.py〕` | 1,435 | ✅ |
| `86c14d68154c` | 1,686 | `〔幽灵引用·未上传:_e48_c5.md〕` | 1,686 | ✅ |
| `87a802ea14b2` | 4,739 | `〔幽灵引用·未上传:_verify_two_pieces_2026_09_30.py〕` | 4,739 | ✅ |
| `889558f0e014` | 88,584 | `〔幽灵引用·未上传:_v41_flash_rag_partial.bak.json〕` | 88,584 | ✅ |
| `89b3dce63800` | 18,152 | `〔幽灵引用·未上传:f2_branch_fix_transform_2026_09_29.py〕` | 18,152 | ✅ |
| `8aa72c80bbf8` | 21,710 | `〔幽灵引用·未上传:_e48_c4.md〕` | 21,710 | ✅ |
| `8b1af9b69ec5` | 40,128 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_18_v100.md〕` | 40,128 | ✅ |
| `8d094945fb22` | 1,229 | `〔幽灵引用·未上传:_e48_docwriter_hash2.py〕` | 1,229 | ✅ |
| `8d6241e65c3d` | 1,890 | `〔幽灵引用·未上传:_t15_inspect3.py〕` | 1,890 | ✅ |
| `8f373879f400` | 96,443 | `〔幽灵引用·未上传:_t15_records.json〕` | 96,443 | ✅ |
| `90db18676749` | 2,537 | `〔幽灵引用·未上传:_pkf34_nd.py〕` | 2,537 | ✅ |
| `910ca28c22fb` | 3,068 | `〔幽灵引用·未上传:_pkf34_f3.py〕` | 3,068 | ✅ |
| `910f0bf4bb5f` | 25,619 | `〔幽灵引用·未上传:_g5_displacement_threshold_draft_2026_10_10.md〕` | 25,619 | ✅ |
| `91cbe31fc56a` | 59,918 | `〔幽灵引用·未上传:_u10_fail_h0_verdict_2026_10_18.md〕` | 59,918 | ✅ |
| `9314fdf5ebd7` | 7,796 | `〔幽灵引用·未上传:_cpatomic_make_fix_2026_09_28.py〕` | 7,796 | ✅ |
| `9427c4c42c97` | 17,411 | `〔幽灵引用·未上传:_v4_supp_t15r2_methodology_template.md〕` | 17,411 | ✅ |
| `966d6db93b67` | 58,572 | `〔幽灵引用·未上传:md_a_field_composition_draft_2026_10_18.staged.md〕` | 58,572 | ✅ |
| `96a1c1645b1b` | 2,703 | `〔幽灵引用·未上传:_pkf34_f3b.py〕` | 2,703 | ✅ |
| `99cd30477496` | 32,030 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_18_v94.md〕` | 32,030 | ✅ |
| `9ab3cf67a432` | 1,124 | `〔幽灵引用·未上传:_e47_docwriter_count.py〕` | 1,124 | ✅ |
| `9bff630d3493` | 5,494 | `〔幽灵引用·未上传:_r3_verify_2026_09_28.py〕` | 5,494 | ✅ |
| `9d01cad624a6` | 50,107 | `〔幽灵引用·未上传:dw99_stage1.md〕` | 50,107 | ✅ |
| `9dd120c96a34` | 2,486 | `〔幽灵引用·未上传:_recheck_r1_run1.log〕` | 2,486 | ✅ |
| `9f970f8226df` | 4,900 | `〔幽灵引用·未上传:_verify_d8_addendum_2026_09_30.py〕` | 4,900 | ✅ |
| `a165000be31f` | 6,510 | `〔幽灵引用·未上传:_b12_q4_formcand_2026_09_29.py〕` | 6,510 | ✅ |
| `a2b148ab39e8` | 11,318 | `〔幽灵引用·未上传:KT_ABC1_anchors_sha256_12.root_session_11318B.bak_2026_09_23.json〕` | 11,318 | ✅ |
| `a423da2f3226` | 3,686 | `〔幽灵引用·未上传:_pkf34_f4d.py〕` | 3,686 | ✅ |
| `a4e0cf8c4298` | 1,282 | `〔幽灵引用·未上传:_postcheck_v16_alt.py〕` | 1,282 | ✅ |
| `a542d7bc793e` | 54,716 | `〔幽灵引用·未上传:_clv_staging_2026_10_18.md〕` | 54,716 | ✅ |
| `a56d16f7b008` | 1,391 | `〔幽灵引用·未上传:_postcheck_v16_sha.py〕` | 1,391 | ✅ |
| `a65632b4c30b` | 1,110 | `〔幽灵引用·未上传:_r4_cleanup_worker_shape_2026_09_29.py〕` | 1,110 | ✅ |
| `a69fcae9ce3d` | 70,328 | `〔幽灵引用·未上传:_kd_resolvability_and_optional_experiments_2026_10_09.md〕` | 70,328 | ✅ |
| `a8210b5b9676` | 2,728 | `〔幽灵引用·未上传:_t15_inspect.py〕` | 2,728 | ✅ |
| `abf4a09b897d` | 1,484 | `〔幽灵引用·未上传:_en_verify4_2026_09_28.py〕` | 1,484 | ✅ |
| `ac32249b79c9` | 29,761 | `〔幽灵引用·未上传:_kd_heteronym_classification_disposition_2026_10_09.md〕` | 29,761 | ✅ |
| `b07c62634e54` | 20,308 | `〔幽灵引用·未上传:_t1_temp_axis_retirement_consolidation_2026_10_10.md〕` | 20,308 | ✅ |
| `b34a12eb5d90` | 43,428 | `〔幽灵引用·未上传:_thirdparty_16_overwrite_ruling_effect_2026_10_18.md〕` | 43,428 | ✅ |
| `b599603f8215` | 29,761 | `〔幽灵引用·未上传:results___kd_heteronym_classification_disposition_2026_10_09.md〕` | 29,761 | ✅ |
| `b6e931642af4` | 8,017 | `〔幽灵引用·未上传:_compute_metrics_v2.py〕` | 8,017 | ✅ |
| `b741fa6b165a` | 42,817 | `〔幽灵引用·未上传:_t1_qwen_temp_sweep_r2_verdict_2026_10_09.md〕` | 42,817 | ✅ |
| `b747e865f962` | 2,969 | `〔幽灵引用·未上传:_aggregate_10cells_v3.py〕` | 2,969 | ✅ |
| `b7b15766e9b1` | 6,322 | `〔幽灵引用·未上传:_cpatomic_register_2026_09_28.py〕` | 6,322 | ✅ |
| `bb4a13c7a700` | 3,074 | `〔幽灵引用·未上传:_cpatomic_keyscan_2026_09_28.py〕` | 3,074 | ✅ |
| `be5a801851df` | 31,254 | `〔幽灵引用·未上传:_freeze_final_replay_2026_10_18.md〕` | 31,254 | ✅ |
| `c111c4ea2aab` | 8,798 | `〔幽灵引用·未上传:_v5_loadcorpus_verify_2026_09_29.py〕` | 8,798 | ✅ |
| `c25987bd31ff` | 1,358 | `〔幽灵引用·未上传:_run_final_selfscan_2026_09_27.py〕` | 1,358 | ✅ |
| `c4a10b4cfe31` | 36,830 | `〔幽灵引用·未上传:_s4_v31_regen_gold_items_2026_10_10.json〕` | 36,830 | ✅ |
| `c768bc661623` | 5,510 | `〔幽灵引用·未上传:_trae_audit_part1.py〕` | 5,510 | ✅ |
| `c8eccce0733a` | 3,958 | `〔幽灵引用·未上传:_pkf34_f4.py〕` | 3,958 | ✅ |
| `ca1dc65c4db0` | 49,227 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_18_v96.md〕` | 49,227 | ✅ |
| `ca85aea58147` | 1,562 | `〔幽灵引用·未上传:_final_check.py〕` | 1,562 | ✅ |
| `cfc0fdf8d212` | 17,341 | `〔幽灵引用·未上传:_t1_qwen_temp_sweep_exec_register_2026_10_09.md〕` | 17,341 | ✅ |
| `d15d568263ea` | 29,664 | `〔幽灵引用·未上传:results___kd_19_ambiguous_tags_rejudge_rewrite_register_2026_10_10.md〕` | 29,664 | ✅ |
| `d228cf0906d6` | 47,297 | `〔幽灵引用·未上传:_round23_26_threshold_review_effect_register_2026_10_10.md〕` | 47,297 | ✅ |
| `d60dadddb99c` | 28,762 | `〔幽灵引用·未上传:_s3_d1_rulings_supplement_register_2026_10_01.md〕` | 28,762 | ✅ |
| `dada54d9aab6` | 32,594 | `〔幽灵引用·未上传:_eta_preexp_wait_and_leveling_effect_2026_10_18.md〕` | 32,594 | ✅ |
| `dde3583101e5` | 5,131 | `〔幽灵引用·未上传:_aggregate_10cells_v2.py〕` | 5,131 | ✅ |
| `df27b83f1dd2` | 21,338 | `〔幽灵引用·未上传:_tail3_atomic_verify_2026_09_29.py〕` | 21,338 | ✅ |
| `df5d21a96752` | 46,786 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_18_v98.md〕` | 46,786 | ✅ |
| `dfd7e44221fa` | 37,518 | `〔幽灵引用·未上传:_ea_erratum_staging_2026_10_18.md〕` | 37,518 | ✅ |
| `e0601c6df74f` | 2,578 | `〔幽灵引用·未上传:_e48_docwriter_hash.py〕` | 2,578 | ✅ |
| `e0c7b6a7f831` | 104,340 | `〔幽灵引用·未上传:_consolidated_pending_rulings_scroll_2026_10_18.md〕` | 104,340 | ✅ |
| `e158e353d448` | 107,959 | `〔幽灵引用·未上传:_run_d8_addendum_2026_09_30.py〕` | 107,959 | ✅ |
| `e1a1631d04c5` | 3,009 | `〔幽灵引用·未上传:_aggregate_10cells.py〕` | 3,009 | ✅ |
| `e304d53d4747` | 42,226 | `〔幽灵引用·未上传:_kimi_preexec_final_rulings_effect_2026_10_18.md〕` | 42,226 | ✅ |
| `e5daeda4fdb7` | 3,045 | `〔幽灵引用·未上传:_pkf34_f4c.py〕` | 3,045 | ✅ |
| `e8192a81d3d5` | 1,525 | `〔幽灵引用·未上传:_r10.py〕` | 1,525 | ✅ |
| `e94639d36c20` | 13,762 | `〔本地路径已脱敏〕` | 13,762 | ✅ |
| `e9cb29bee98d` | 35,016 | `〔幽灵引用·未上传:_h_face_external_evidence_eval_2026_10_18.md〕` | 35,016 | ✅ |
| `ea229f6c7bd6` | 34,941 | `〔幽灵引用·未上传:_historical_〕 forgetting_recheck_2026_10_18.md` | 34,941 | ✅ |
| `eabc35e9087a` | 1,459 | `〔幽灵引用·未上传:_check_kimi_sides.py〕` | 1,459 | ✅ |
| `ec11b2b73f30` | 3,149 | `〔幽灵引用·未上传:_v5_qwen_retry_introspect_20260929.py〕` | 3,149 | ✅ |
| `ee58dbb80767` | 68,524 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_18_v103.md〕` | 68,524 | ✅ |
| `eefabee5fde5` | 51,604 | `〔幽灵引用·未上传:_scroll_wave4_three_rulings_effect_2026_10_18.md〕` | 51,604 | ✅ |
| `f09d9a231756` | 41,770 | `〔幽灵引用·未上传:_r2_sep_endogeneity_erratum_2026_10_18.md〕` | 41,770 | ✅ |
| `f106f9ba9f59` | 5,954 | `〔幽灵引用·未上传:_sensitivity.py〕` | 5,954 | ✅ |
| `f17e527cfa4f` | 5,401 | `〔幽灵引用·未上传:_v5_item21_anchor_driver.py〕` | 5,401 | ✅ |
| `f1f635588fbc` | 38,991 | `〔幽灵引用·未上传:dw95_stage2.md〕` | 38,991 | ✅ |
| `f2d7b875aa42` | 33,847 | `〔幽灵引用·未上传:_v3r1_threshold_restatement_design_2026_10_10.md〕` | 33,847 | ✅ |
| `f4636107380a` | 4,401 | `〔幽灵引用·未上传:_pkf34_f4b.py〕` | 4,401 | ✅ |
| `f5f5e2fff2c9` | 28,959 | `〔幽灵引用·未上传:dw95_stage1.md〕` | 28,959 | ✅ |
| `f68393b6b384` | 11,599 | `〔幽灵引用·未上传:_next_stage3_dir_optimization_ruling_2026_10_18.md〕` | 11,599 | ✅ |
| `f6b98a7c4462` | 31,468 | `〔幽灵引用·未上传:_run_d6b_addendum_2026_09_28.py〕` | 31,468 | ✅ |
| `f716c0c35939` | 3,304 | `〔幽灵引用·未上传:_run_result_v3.py〕` | 3,304 | ✅ |
| `f84d0c6de951` | 2,297 | `〔幽灵引用·未上传:_r1_alarm_test.py〕` | 2,297 | ✅ |
| `fb299dc324fa` | 23,204 | `〔幽灵引用·未上传:_run_d6_addendum_2026_09_28.py〕` | 23,204 | ✅ |
| `fbaf34a68c17` | 34,217 | `〔幽灵引用·未上传:_t1_prereg_revision_temp_axis_exp2_2026_10_09.md〕` | 34,217 | ✅ |
| `fc239a38f5bd` | 7,377 | `〔幽灵引用·未上传:f2_branch_selftest_2026_09_29.py〕` | 7,377 | ✅ |
| `fd746ac78c08` | 53,502 | `〔幽灵引用·未上传:_pending_residual_minimal_set_2026_10_18.md〕` | 53,502 | ✅ |

## §8 态变型（137 件）

> 义：实体**在盘且为活件**，然引文所载指纹／字节为**旧态**。**非幽灵**——实体在，只引文陈旧。
> 本棒以**旧前缀检验**（对每件算其前 N 字节之 SHA-256）检出：引文指纹 ＝ 现行件**前 N 字节**之 SHA-256 ⇒ 纯追加续写可证。

### 8.1 旧前缀型（135 件）

| 指纹 | 所载 bytes | 引次 | 现行件路径 | 现行 bytes | 前缀吻合字节 |
|---|---|---|---|---|---|
| `2f34ce11b3b4` | 23,513 | 71 | `〔幽灵引用·未上传:_v5_fake_verdict_forensics_2026_09_28.md〕` | 35,870 | 23,513 |
| `6512c6843d11` | 110,211 | 69 | `〔幽灵引用·未上传:_v148_adoption_effect_2026_10_20.md〕` | 121,547 | 110,211 |
| `ba5d1f3fc594` | 78,621 | 53 | `〔幽灵引用·未上传:_ablation_design_2026_10_20.md〕` | 98,542 | 78,621 |
| `7e2b0bb39cfe` | 32,178 | 51 | `〔幽灵引用·未上传:_v5_c3_reading_b_prereg_2026_09_28.md〕` | 32,178 | 31,333 |
| `811793e86d7d` | 44,001 | 47 | `〔幽灵引用·未上传:_runface_vs_shape_caliber_draft_2026_10_20.md〕` | 65,692 | 44,001 |
| `c300e74a082c` | 30,552 | 46 | `〔幽灵引用·未上传:_v3_recheck_26b_rescript_2026_09_27.md〕` | 30,552 | 29,349 |
| `92ac9a956bd3` | 39,378 | 41 | `〔幽灵引用·未上传:_v5_bulk_activation_2026_09_28.md〕` | 39,378 | 38,533 |
| `52cc36328a4b` | 39,872 | 40 | `〔幽灵引用·未上传:_stage1_prereq_wave1_evidence_2026_10_20.md〕` | 55,404 | 39,872 |
| `da9b793fc73f` | 134,043 | 39 | `〔幽灵引用·未上传:_v154_adoption_effect_2026_10_20.md〕` | 148,255 | 134,043 |
| `bc68854a6eba` | 38,932 | 35 | `〔幽灵引用·未上传:_v3_recheck_prereg_v1p2_2026_09_27.md〕` | 38,932 | 37,636 |
| `43a30e29b2be` | 2,672 | 32 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_20_v145.md〕` | 3,742 | 2,672 |
| `4aa9640bbfe7` | 29,347 | 32 | `〔幽灵引用·未上传:_v5_trae_doubt6_verify_2026_09_28_r3verifier.md〕` | 30,192 | 29,347 |
| `17262abfd1d5` | 110,787 | 31 | `〔幽灵引用·未上传:_v3_recheck_verdict_register_2026_09_27.md〕` | 112,085 | 110,787 |
| `a8da321b64d2` | 33,904 | 29 | `〔幽灵引用·未上传:_v3_recheck_prereg_v1p3_2026_09_27.md〕` | 35,200 | 33,904 |
| `1b883d046720` | 27,639 | 27 | `〔幽灵引用·未上传:_v5_fake_verdict_v1x_prereg_2026_09_28.md〕` | 28,484 | 27,639 |
| `3670568a585a` | 7,557 | 25 | `〔幽灵引用·未上传:_gap_and_kd_flip_master_inventory_2026_10_19.md〕` | 9,043 | 7,557 |
| `052707d939d0` | 2,152 | 23 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_19_v139.md〕` | 2,846 | 2,152 |
| `7a739bdc2520` | 18,032 | 22 | `〔幽灵引用·未上传:_v5_fake_verdict_session_log_2026_09_28.md〕` | 18,877 | 18,032 |
| `5d7993240f75` | 4,101 | 21 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_20_v162.md〕` | 5,460 | 4,101 |
| `fc74d20f0ca8` | 34,539 | 21 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_17_v86.md〕` | 39,039 | 34,539 |
| `0a2b5c837c83` | 23,048 | 20 | `〔幽灵引用·未上传:_v3_recheck_26_preexp_report_2026_09_27.md〕` | 23,048 | 21,855 |
| `fbf88f8ac7a6` | 10,103 | 19 | `〔幽灵引用·未上传:_v4_pi_cot_v3_v3r1_rescript_2026_09_27.md〕` | 11,385 | 10,103 |
| `1e46ab68a335` | 2,553 | 18 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_20_v146.md〕` | 4,153 | 2,553 |
| `d80cf1804e80` | 3,883 | 18 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_20_v159.md〕` | 6,597 | 3,883 |
| `434b3213bdce` | 13,233 | 17 | `〔幽灵引用·未上传:_v3_recheck_01_rescript_2026_09_27.md〕` | 14,541 | 13,233 |
| `1442a1296936` | 423,375 | 16 | `〔幽灵引用·未上传:_root_session_history_memo_2026_10_14.md〕` | 558,430 | 423,375 |
| `b0b3f8d8a4aa` | 24,601 | 14 | `〔幽灵引用·未上传:_v5_closing_register_r2_2026_09_28.md〕` | 25,446 | 24,601 |
| `24d06bf17b67` | 200,934 | 13 | `〔幽灵引用·未上传:_root_session_history_memo_main_2026_10_14.md〕` | 273,072 | 200,934 |
| `2e0f6b8bf141` | 13,472 | 13 | `〔幽灵引用·未上传:_v3_recheck_04_rescript_2026_09_27.md〕` | 14,780 | 13,472 |
| `431ecdbd747e` | 244,512 | 13 | `〔幽灵引用·未上传:_root_session_history_memo_main_2026_10_14.md〕` | 273,072 | 244,512 |
| `aa02cbfc84e3` | 15,211 | 13 | `〔幽灵引用·未上传:rescript_2026_09_27.md〕` | 17,069 | 15,211 |
| `f1b5e49f3058` | 27,538 | 13 | `〔幽灵引用·未上传:_v4_supp_t1_verdict.md〕` | 29,106 | 27,538 |
| `92d7a9b8b877` | 316,601 | 12 | `〔幽灵引用·未上传:_root_session_history_memo_2026_10_14.md〕` | 558,430 | 316,601 |
| `a49a2fbcb10a` | 26,379 | 12 | `〔幽灵引用·未上传:_v5_closing_register_2026_09_28.md〕` | 27,224 | 26,379 |
| `aed375c485fb` | 407,284 | 12 | `〔本地路径已脱敏〕` | 857,551 | 407,284 |
| `4217ad8c1381` | 219,360 | 11 | `〔幽灵引用·未上传:_root_session_history_memo_main_2026_10_14.md〕` | 273,072 | 219,360 |
| `a9cbafe581bb` | 148,804 | 11 | `〔幽灵引用·未上传:_v173_adoption_effect_2026_10_21.md〕` | 154,726 | 148,804 |
| `21596e1ada4f` | 53,997 | 10 | `〔幽灵引用·未上传:_stage1_prereq_wave1_evidence_2026_10_20.md〕` | 55,404 | 53,997 |
| `6df402298557` | 14,510 | 10 | `〔幽灵引用·未上传:rescript_2026_09_27.md〕` | 17,574 | 14,510 |
| `98a779d61c1e` | 32,521 | 10 | `〔幽灵引用·未上传:_v4_supp_l14v3_model_mapping_2026_09_24.md〕` | 49,326 | 48,028 |
| `2b9e886e729d` | 14,525 | 9 | `〔幽灵引用·未上传:_v3_recheck_12_jsv_check_2026_09_27.md〕` | 15,821 | 14,525 |
| `57025a20f6e2` | 66,836 | 9 | `〔幽灵引用·未上传:pi_rulings___pi_card_answers_register_2026_10_17_v54.md〕` | 72,381 | 66,836 |
| `94b96e2e6049` | 50,495 | 9 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_17_v55.md〕` | 54,188 | 50,495 |
| `b0e49a6b09f9` | 59,958 | 9 | `〔本地路径已脱敏〕` | 105,136 | 59,958 |
| `d6e5f8a4c440` | 52,276 | 9 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_17_v87.md〕` | 56,899 | 52,276 |
| `02c072833cca` | 32,186 | 8 | `〔幽灵引用·未上传:_v4_gamma_r1_prereg_2026_09_28.md〕` | 33,489 | 32,186 |
| `1e2bb799db18` | 218,236 | 8 | `〔幽灵引用·未上传:_root_session_history_memo_main_2026_10_14.md〕` | 273,072 | 218,236 |
| `48af7bc27f3b` | 266,198 | 8 | `〔幽灵引用·未上传:_root_session_history_memo_main_2026_10_14.md〕` | 273,072 | 266,198 |
| `5a6bb7f70418` | 14,600 | 8 | `〔幽灵引用·未上传:_v4_slow_cleanup_manifest_2026_09_28.md〕` | 15,693 | 14,600 |
| `680a7ce4cf08` | 148,103 | 8 | `〔幽灵引用·未上传:_v153_adoption_effect_2026_10_20.md〕` | 181,493 | 148,103 |
| `6f644de761a3` | 216,105 | 8 | `〔幽灵引用·未上传:_root_session_history_memo_main_2026_10_14.md〕` | 273,072 | 216,105 |
| `bead4fccb740` | 200,159 | 8 | `〔幽灵引用·未上传:_root_session_history_memo_main_2026_10_14.md〕` | 273,072 | 199,159 |
| `f4435801d09f` | 64,485 | 8 | `〔幽灵引用·未上传:_v4_supp_l14v3_n26_verdict.md〕` | 65,978 | 64,485 |
| `331022480a57` | 23,039 | 7 | `〔幽灵引用·未上传:rescript_2026_09_27.md〕` | 25,151 | 23,039 |
| `644e0666fbc4` | 25,901 | 7 | `〔幽灵引用·未上传:_skill_reference_erratum_and_runtime_anchor_experiment_2026_09_30.md〕` | 30,771 | 25,901 |
| `759a268582d4` | 472,023 | 7 | `〔本地路径已脱敏〕` | 857,551 | 472,023 |
| `a3554f59afaf` | 31,161 | 7 | `〔幽灵引用·未上传:_v5_fake_verdict_forensics_2026_09_28.md〕` | 35,870 | 31,161 |
| `d4da2693d309` | 230,027 | 7 | `〔幽灵引用·未上传:_v180_v182_adoption_effect_2026_10_21.md〕` | 244,228 | 230,027 |
| `e01b6a3bfb3c` | 3,320 | 7 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_20_v170.md〕` | 4,772 | 3,320 |
| `0f0a4329c34f` | 2,385 | 6 | `〔幽灵引用·未上传:biological_taxonomy.json〕` | 2,386 | 2,385 |
| `132a5c1e25ed` | 46,985 | 6 | `〔幽灵引用·未上传:_stage1_experiment_gap_inventory_2026_10_19.md〕` | 56,161 | 46,985 |
| `2fb5987f544d` | 192,292 | 6 | `〔幽灵引用·未上传:_v3_v4_achievements_inventory_2026_09_24.md〕` | 194,083 | 192,292 |
| `33478e048831` | 165,732 | 6 | `〔幽灵引用·未上传:_v152_adoption_effect_2026_10_20.md〕` | 171,316 | 165,732 |
| `3d9ad5f1540d` | 8,937 | 6 | `〔幽灵引用·未上传:_v3_recheck_26_rescript_2026_09_27.md〕` | 13,747 | 8,937 |
| `6db65c9d8792` | 23,373 | 6 | `〔幽灵引用·未上传:_v4_pending_decisions_2026_09_28.md〕` | 24,676 | 23,373 |
| `86af2ef6b66c` | 2,341 | 6 | `〔幽灵引用·未上传:historical_causality.json〕` | 2,342 | 2,341 |
| `9c74bb8206c0` | 2,386 | 6 | `〔幽灵引用·未上传:physics_concepts.json〕` | 2,387 | 2,386 |
| `c3ce2bb53af1` | 28,097 | 6 | `〔幽灵引用·未上传:_c5_split_into_c5a_c5b_2026_10_17.md〕` | 28,902 | 28,097 |
| `d2cadc7e7c23` | 5,253 | 6 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_20_v159.md〕` | 6,597 | 5,253 |
| `ddda494f014a` | 2,782 | 6 | `〔幽灵引用·未上传:algorithm_process.json〕` | 2,783 | 2,782 |
| `f3838e36b897` | 149,295 | 6 | `〔幽灵引用·未上传:_v145_adoption_effect_2026_10_20.md〕` | 174,834 | 149,295 |
| `1903cc498578` | 230,412 | 5 | `〔幽灵引用·未上传:ge01_full_1494_llm_calls_2026_10_16.jsonl〕` | 235,298 | 230,412 |
| `192bd0e58826` | 110,673 | 5 | `〔幽灵引用·未上传:_v149_adoption_effect_2026_10_20.md〕` | 116,942 | 110,673 |
| `1cd36ac1b2c0` | 19,914 | 5 | `〔幽灵引用·未上传:_v3_recheck_12_rescript_2026_09_27.md〕` | 21,222 | 19,914 |
| `2696af62e3ee` | 12,742 | 5 | `〔幽灵引用·未上传:_deposon_full_history_main_2026_10_19.md〕` | 14,265 | 12,742 |
| `301e682f04ce` | 143,469 | 5 | `〔幽灵引用·未上传:_v143_v144_adoption_effect_2026_10_19.md〕` | 184,744 | 143,469 |
| `3092bd586f82` | 128,498 | 5 | `〔幽灵引用·未上传:_v152_adoption_effect_2026_10_20.md〕` | 171,316 | 128,498 |
| `45d343b998f0` | 22,498 | 5 | `〔本地路径已脱敏〕` | 25,293 | 22,498 |
| `4ff033ec583d` | 168,666 | 5 | `〔幽灵引用·未上传:_v145_adoption_effect_2026_10_20.md〕` | 174,834 | 168,666 |
| `69508d1965e9` | 107,084 | 5 | `〔幽灵引用·未上传:_v166_adoption_effect_2026_10_20.md〕` | 129,389 | 107,084 |
| `cfd251e771a9` | 508,443 | 5 | `〔本地路径已脱敏〕` | 857,551 | 508,443 |
| `e8f72f8c63fb` | 37,187 | 5 | `〔幽灵引用·未上传:_v3_recheck_prereg_v1p4_2026_09_27.md〕` | 69,406 | 37,187 |
| `f0ddfdf0aec8` | 236,615 | 5 | `〔幽灵引用·未上传:_root_session_history_memo_main_2026_10_14.md〕` | 273,072 | 236,615 |
| `05b975a86989` | 61,547 | 4 | `〔幽灵引用·未上传:_v4_supp_prereg_v02_add_L14V3_2026_09_24.md〕` | 62,847 | 61,547 |
| `0f933318d5a1` | 137,346 | 4 | `〔幽灵引用·未上传:_v169_adoption_effect_2026_10_20.md〕` | 156,752 | 137,346 |
| `189ba84fc12e` | 193,632 | 4 | `〔幽灵引用·未上传:_v3_v4_achievements_inventory_2026_09_24.md〕` | 194,083 | 193,632 |
| `310b8aaeb7de` | 365,341 | 4 | `〔幽灵引用·未上传:_root_session_history_memo_2026_10_14.md〕` | 558,430 | 365,341 |
| `46c8c95a7a4f` | 222,463 | 4 | `〔幽灵引用·未上传:_root_session_history_memo_main_2026_10_14.md〕` | 273,072 | 222,463 |
| `509e17caa955` | 228,636 | 4 | `〔幽灵引用·未上传:_v180_v182_adoption_effect_2026_10_21.md〕` | 244,228 | 228,636 |
| `88acbcfd828a` | 173,497 | 4 | `〔幽灵引用·未上传:_v153_adoption_effect_2026_10_20.md〕` | 181,493 | 173,497 |
| `99c17fdbe0d9` | 558,966 | 4 | `〔本地路径已脱敏〕` | 857,551 | 558,966 |
| `a9f6b6f748a9` | 818,979 | 4 | `〔本地路径已脱敏〕` | 857,551 | 818,979 |
| `abd08ec2150d` | 260,084 | 4 | `〔幽灵引用·未上传:_root_session_history_memo_2026_10_14.md〕` | 558,430 | 260,084 |
| `ae7226f9671a` | 43,692 | 4 | `〔幽灵引用·未上传:_ge02_entity_verification_2026_10_21.md〕` | 44,410 | 43,692 |
| `d42071620490` | 26,609 | 4 | `〔幽灵引用·未上传:_morning_brief_pending_rulings_2026_10_18.md〕` | 37,227 | 26,609 |
| `e61f4050fc02` | 6,195 | 4 | `〔幽灵引用·未上传:_d8_collection_ledger_2026_09_30.md〕` | 20,290 | 6,195 |
| `fa5145d90fe4` | 215,131 | 4 | `〔幽灵引用·未上传:_root_session_history_memo_2026_10_14.md〕` | 558,430 | 215,131 |
| `0789214e950e` | 125,071 | 3 | `〔幽灵引用·未上传:_v150_adoption_effect_2026_10_20.md〕` | 132,608 | 125,071 |
| `128b4167afd5` | 215,227 | 3 | `〔幽灵引用·未上传:_v180_v182_adoption_effect_2026_10_21.md〕` | 244,228 | 215,227 |
| `2764e9e0cf8b` | 84,694 | 3 | `〔幽灵引用·未上传:_v156_adoption_effect_2026_10_20.md〕` | 101,278 | 84,694 |
| `3ebd023879a5` | 84,135 | 3 | `〔幽灵引用·未上传:_v157_adoption_effect_2026_10_20.md〕` | 109,343 | 84,135 |
| `4b792e20f34f` | 115,416 | 3 | `〔幽灵引用·未上传:_v154_adoption_effect_2026_10_20.md〕` | 148,255 | 115,416 |
| `552aa383c51f` | 223,841 | 3 | `〔幽灵引用·未上传:_v180_v182_adoption_effect_2026_10_21.md〕` | 244,228 | 223,841 |
| `8c8610ced9fa` | 360,692 | 3 | `〔本地路径已脱敏〕` | 857,551 | 360,692 |
| `a75dbfff187e` | 257,109 | 3 | `〔幽灵引用·未上传:_v183_v185_adoption_effect_2026_10_21.md〕` | 262,130 | 257,109 |
| `aab40da2421c` | 27,706 | 3 | `〔幽灵引用·未上传:_v4_item04_textfix_prereg_v1x_2026_09_28.md〕` | 42,153 | 27,706 |
| `ca71c02589e7` | 60,649 | 3 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_17_v47.md〕` | 65,046 | 60,649 |
| `d0e6dcb17fb3` | 24,369 | 3 | `〔幽灵引用·未上传:_collision_baseline_update_and_disposition_2026_10_17.md〕` | 26,197 | 24,369 |
| `e17942840ef9` | 78,018 | 3 | `〔幽灵引用·未上传:_v155_adoption_effect_2026_10_20.md〕` | 89,658 | 78,018 |
| `eb5e7433c255` | 48,115 | 3 | `〔幽灵引用·未上传:_scroll_wave1_four_rulings_effect_2026_10_18.md〕` | 51,739 | 48,115 |
| `10e7256e89f1` | 43,192 | 2 | `〔幽灵引用·未上传:_exp8_bar_c_reading_2026_10_21.md〕` | 45,589 | 43,192 |
| `16ea95ae4412` | 46,362 | 2 | `〔幽灵引用·未上传:_independent_review_history_gaps_kd_2026_10_19_sub.md〕` | 52,087 | 46,362 |
| `1e15e7611597` | 115,240 | 2 | `〔幽灵引用·未上传:_v159_adoption_effect_2026_10_20.md〕` | 119,076 | 115,240 |
| `464ae884a347` | 600,749 | 2 | `〔本地路径已脱敏〕` | 857,551 | 600,749 |
| `4864a9b8fa78` | 687,653 | 2 | `〔本地路径已脱敏〕` | 857,551 | 687,653 |
| `5f064147a527` | 34,207 | 2 | `〔幽灵引用·未上传:d83_n7r_stage.md〕` | 35,057 | 34,207 |
| `6b2190b7a60a` | 664,058 | 2 | `〔本地路径已脱敏〕` | 857,551 | 664,058 |
| `72b318ef434b` | 70,973 | 2 | `〔幽灵引用·未上传:_v5_sub_artifact_ledger_2026_09_28.md〕` | 71,818 | 70,973 |
| `7e789561afc9` | 749,579 | 2 | `〔本地路径已脱敏〕` | 857,551 | 749,579 |
| `82e90e0c9cb8` | 795,064 | 2 | `〔本地路径已脱敏〕` | 857,551 | 795,064 |
| `8b1e04c038ee` | 26,998 | 2 | `〔幽灵引用·未上传:_ge02_adoption_freeze_register_2026_10_20.md〕` | 29,719 | 26,998 |
| `91e3d7a03155` | 23,591 | 2 | `〔幽灵引用·未上传:_c4_reply_intake_acceptance_register_2026_10_01.md〕` | 33,728 | 23,591 |
| `aa62c23b02a7` | 632,281 | 2 | `〔本地路径已脱敏〕` | 857,551 | 632,281 |
| `cfe64350b62f` | 225,754 | 2 | `〔幽灵引用·未上传:_root_session_history_memo_main_2026_10_14.md〕` | 273,072 | 225,754 |
| `e361a13ed658` | 107,152 | 2 | `〔幽灵引用·未上传:_v164_adoption_effect_2026_10_20.md〕` | 120,622 | 107,152 |
| `ea78431b6a89` | 349,714 | 2 | `〔幽灵引用·未上传:_ablation_data_2026_10_20.json〕` | 349,715 | 349,714 |
| `0b8041435f8e` | 58,660 | 1 | `〔幽灵引用·未上传:_skill_reference_update_and_user_surface_survey_2026_09_30.md〕` | 60,621 | 58,660 |
| `3b7a4888efd8` | 34,737 | 1 | `〔本地路径已脱敏〕` | 42,948 | 34,737 |
| `91462587a688` | 18,073 | 1 | `〔幽灵引用·未上传:_gd03_caliber_note_2026_10_20.md〕` | 19,611 | 18,073 |
| `9a7262685d9f` | 18,833 | 1 | `〔幽灵引用·未上传:_d8_collection_ledger_2026_09_30.md〕` | 20,290 | 18,833 |
| `a8ba20d693ed` | 27,018 | 1 | `〔幽灵引用·未上传:_four_class_backtrace_inventory_2026_10_13.md〕` | 29,156 | 27,018 |
| `be0f2c61473b` | 38,299 | 1 | `〔幽灵引用·未上传:_fake_verdict_reverify_sixitem_ledger_2026_09_30.md〕` | 40,957 | 38,299 |
| `d03c8ce569ca` | 27,595 | 1 | `〔幽灵引用·未上传:_four_class_backtrace_inventory_2026_10_13_r1.md〕` | 29,809 | 27,595 |
| `e23e1b1e520b` | 24,309 | 1 | `〔幽灵引用·未上传:_pi_card_answers_register_2026_10_16_v32.md〕` | 31,156 | 24,309 |
| `e96d99ff9e75` | 55,340 | 1 | `〔幽灵引用·未上传:_skill_reference_update_and_user_surface_survey_2026_09_30.md〕` | 60,621 | 55,340 |

### 8.2 字节陈旧型（2 件）

| 指纹 | 所载 bytes | 现行件路径 | 现行 bytes |
|---|---|---|---|
| `80a97ee882d5` | 9,466 | `〔幽灵引用·未上传:_numbering_family_count_effect_register_2026_10_14.md〕` | 22,786 |
| `e013fac3d234` | 189,657,496 | `〔幽灵引用·未上传:_r2_tool_26_genregister.py〕` | 20,579 |

## §9 与 10-21 前件（182 件 MISS）之对账

前件 `_ghost_reference_register_2026_10_21.md` 载 MISS **182** 件（＝ A 类 PI 点名 4 件 ＋ B 类 17 ＋ C 类 161；**本棒重判覆盖 B∪C 之 178 件表行**，A 类 4 件另见 §3 专节）。其扫描面仅 **469** 件 md（`pi_rulings` 全 ＋ `results` 根层 10-19 起），成对抽取式为「指纹…数字 B」（**须带 B 单位**）。本棒逐条重判之：

| 前件 MISS 之终态 | 件数 | 义 |
|---|---|---|
| TRUE_GHOST | 116 | 复核后**仍为真幽灵** |
| STATE_PREFIX | 55 | 复核后**实体在盘**——引文载的是活件之旧前缀（前件误列 MISS） |
| EXTERNAL | 7 | 复核后**实体在盘于仓外 runtime/plugin-cache 面**（前件四区索引不涵之） |

**要点**：前件 B∪C 表 **178** 行中，**62 件（35%）经本棒多路探针判为「实体在盘」**（态变 55 ＋ 域外 7）——**幽灵面被前件高估**；余 **116 件复核后仍为真幽灵**。加上 A 类 PI 点名 4 件（§3，本棒复核**四件皆仍为真幽灵**），前件 182 件 MISS 之重判结果为：**真幽灵 120 件／实体在盘 62 件**。

**前件表内之重复**：B∪C 表 **178** 行中唯一指纹仅 **176**（`5c6d558fa400` 于两行分别载 635,733 B 与 652,755 B、`b32ca40ec123` 两行同载 15,707 B）⇒ 前件之 182 与其表体之间存在 **4 行差额**（A 类 4 件不在 B∪C 表内）＋ **2 行重复指纹**。本棒按**唯一指纹**计，不重复计数。

**另**：前件 §5 之 SIZE-MISMATCH 2 件之重判——`1442a1296936`（423,375 B）经**旧前缀检验**判为**态变型（旧前缀）**（现行件 558,430 B，其前 423,375 字节 SHA-256 逐位吻合；`_s16_append_2026_10_21.md` L50 已有「PURE-APPEND ＝ MATCH」之并读），非「指纹在盘而字节不符」；`b32ca40ec103` 重判为 **SAME_IDENTITY**。

**扫描面之差**：本棒 1294 件 md（前件 469）——补入 `results\` 10-19 之前之件、`.tmp\` 工作面、`pi_rulings` 全量。独立清点棒（`bg_fe3a4ded`）所报「1,939 候选对／340 零命中」与本棒之 **7106 对**（宽口径）／**4700 对**（严口径）之差，本棒之成因有二：①扫描面更宽（1294 vs 1,291，量级相近）；②**字节面抽取口径不同**——本棒宽口径并收「逗号千分位无单位」之字节面（如 `7da95eb67e06` ／ 33,546 ／ 327 之表式），严口径则须带单位标记。**两口径之终态完备性相同（待辨 ＝ 0）。**

## §10 老实交代 5 条

1. **⛔ 只判「本机四区 0 实存」**——远端面（GitHub 认可面）**⛔ 0 联网・未测**，一律记「未核·须 PI 或另授权」。四件点名幽灵之中 `cf04fc2f39db` 之落位字面已指明在**远端仓根** `zeroandcat/Deposon` 之 `shared/`，故其「不在本地」非「不存在」。
2. **归档区 ⛔ 0 触内件**——40,121 件**仅列名与件数**；**0 读内容、0 哈希**。故「某件在归档区」**仅能以名判**；`c43494ddd528`（《全量补实验执行计划 v1.1》·21,411 B）虽被前件载为「在仓外冻结区」，本棒**仅名**扫描**0 命中**（「全量补实验」「执行计划」「计划」各 0）⇒ **该面不可核**，⛔ 0 断言其在或不在归档区。归档区根下 `_mirror_pullback_172_2026_10_18\_mirror_manifest.json`（192,689 B）存在（仅记名与字节），其内容本棒⛔ 0 读。
3. **扫描面之冻结时点为 2026-10-22 00:55**（本棒仪器 v2 起跑之清单冻结点）；此后并发棒新出之 4 件（`_v226_v230_adoption_effect_2026_10_22.md` 00:56:54／`_v186_v225_adoption_effect_2026_10_22.md` 01:00:11／`_bloat_inventory_2026_10_22.md` 01:01:01／`_t4k_k5k_coverage_adjudication_2026_10_22.md` 01:10:33）**未入本轮成对抽取**——本棒已作**同法补扫**（75 对：SHA-256 命中 71／域外 4／**真幽灵 2**）并入 §4（末 2 件）。**引次为「md 内出现次数」，非「引用件数」**——与前件之 51／17／14／16 口径不同（前者为全类型文件之引用件数）。
4. **四件点名幽灵之「同一性」判定均属推断，非哈希证明**——`4fa15c554d93` 与在盘 `_gemini4_reply_verification_register_2026_10_15.md` 之关系为**语义＋对象＋条目体例＋字节差 10** 之并证，**⛔ 0 断言二者同一**；同理 §5 全部漂移项之「同一实体」为**名重合＋近字节**之并证，**⛔ 0 断其同一**，故其处置皆为「②改指（须先辨明）」而非「已改指」。
5. **⛔ 0 沿用他件之 182**——本棒自建仪器（v1→v2 两轮自审）逐条重算；与前件之数之差已逐条归因于**扫描面**与**口径**两项（§9）。**⛔ 0 落五终判・⛔ 0 闭 KD・⛔ 0 宣告段毕・⛔ 0 代裁**；§4 之「拟定处置」为拟案，裁归 PI。

## §11 触动 0 之实证

| 面 | 证据 |
|---|---|
| 既有件 | **0 回改**——本棒全部写入落于 **19 个 `.tmp\_s18_ghost_audit_*` 新件**（仪器与生成脚本 12 件 `.py` ＋ 中间数据 7 件 `.json`）＋ 本复核件 1 件；`results\` 内 mtime 晚于 2026-10-21 23:00 之 **40** 件中，**19 件为本棒新件**，余 **21 件为并发他棒所写**（`_v226_v230_adoption_effect_2026_10_22.md`／`_v186_v225_adoption_effect_2026_10_22.md`／`_bloat_inventory_2026_10_22.md`／`_t4k_k5k_coverage_adjudication_2026_10_22.md`／`_e07_deliberation_2026_10_22.md`／`.tmp\_s17_*` 等），**本棒 0 触**。 |
| 归档区 | **0 写入**——文件数 40,121（前后一致）；**最新 mtime ＝ 2026-10-18 16:19:24**；mtime 晚于 2026-10-21 23:00 者 **0**。本棒仅 `os.walk` 列名与 `Get-ChildItem` 列名，**0 读内容、0 哈希、0 写入**。 |
| 移动/重命名/删除 | **0**——全程 0 次移动、0 次重命名、0 次删除（无 `rm`、无 `Move-Item`）。 |
| 新建目录 | **0**——仅用既有 `results\.tmp\` 与 `results\` 两处已存在目录。 |
| 联网 | **0 次**——全程无 `web_search`／`web_fetch`／任何网络调用。 |
| `.env` | **0 读**。 |
| 归档区内容 | **0 读**（仅名）。 |

## §12 字节级自报（本件落盘后独立回读）

| 项 | 值 |
|---|---|
| 路径 | `〔幽灵引用·未上传:_ghost_reference_audit_2026_10_22.md〕` |
| BOM | **0**（无 UTF-8 BOM） |
| CR | **0**（纯 LF） |
| VT | **0**（无 0x0B） |
| U+FFFD | **0**（无替换字符） |
| 非 ASCII | **> 0**（中文正文） |
| bytes／SHA-12 | **出带自报**（本件不能自含其自身哈希——自含即自指悖论；其值随本节落定后由本棒**独立回读**实测并载于回执） |

> **本棒回执**（同一时点、同一次独立回读）：路径 ＋ SHA-12 ＋ bytes ＋ 上表六项属性。**回执之数与本件落盘后实测同源。**
---

*件止。`evidence-auditor` · 2026-10-22 —— 幽灵引用**逐一三审**复核件（自建仪器 v2·六类终态完备·待辨 0）｜四件点名幽灵各三路探法＋阴性断言三审＋三径荐案（⛔ 0 判「不存在于任何世界」）｜⛔ 0 回改既有件 · 0 移 · 0 删 · 0 新建目录 · 0 触归档区内容 · 0 联网 · 0 落五终判 · 0 闭 KD · 0 宣告段毕 · 0 代裁。*
