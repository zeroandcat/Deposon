# TR-3S 第三轮独立判读 · 读数件（独立读者面）· 2026-10-25

> **判读者**：verifier（第三轮重做·独立读者面）　**判定时点**：2026-10-25 19:3x GMT+0800
> **授料**：仅二件（下表）　**禁读件：未读**（§8.3 逐件声明）
> **本件产出**：读数 ＋ 难例清单 ＋ 一项语料缺陷诊断。
> **⛔0 落五终判（pass/af/kd/fail/give-up）｜⛔0 代 PI 裁｜⛔0 宣告门② 成就或段毕｜⛔0 回改任何既有件**

## 0 · 结论摘要（先读此）

**0.1 一句话**——授料二件之指纹皆与授料书所称相符；但**语料 v4 之 `armB` 78 条记录内无任何命中摘录**（实测键集：68 条仅 `bytes/path/root/sha12`，10 条另加 `reason`）⇒ TR-3S **段一（扫描面＝件之全文）与段二（依小句全文施四问）在授料内不可执行**。

**0.2 本轮之读数**——候选级 **0**（语料自身文本上之机械扫描）；件级 **C=0 ｜ B=0 ｜ N=78 ｜ A=0**；**真状态断言率＝未定义（0/0）**；难例 **78 条（全部）**。

**0.3 ⚠ 此读数不得读作「78 件皆无不明状态」**——那是**缺证据之退度假 A**。规则 §8-4.2 之 A 证成条件（①候选集已逐条定性完毕（0 条留空）②无 C／B／N 候选）之实质为「**经逐处定性·无状态断言**」；本轮段一**未能在件之全文上执行**（扫描面为空）⇒ 实质要件①**未满足** ⇒ **⛔0 宣告 A**；依 §8-3 兜底（⛔0 充 C、⛔0 充 A）与 §8-4.4（N 件必逐件列明，并入挂账＋设法辨明）⇒ 78 件皆落 **N（不可判）**。

**0.4 最小补救之拟案（呈建议，不代 PI 裁）**——重剥语料为 v5：逐条**保留命中摘录**（件／行／列／词元／小句全文／行全文），并维持前轮字段全剥（本次实测 11 个前轮词元 → 0 命中，即「污染已剥除」之面**实测成立**，重剥时勿回退）。

**0.5 与授料书之分歧 3 项**（详见 §10）：D1 摘录是否存在（实测**无**）；D2 段一是否含剔除（规则原文：**无剔除**）；D3 四问次序（规则原文 **一→二→三→四**，授料书所称采认 #15「一→四→三→二」**规则件内未载**）。

## 1 · 授料核验（自测·实测）

| 授料 | 授料书所称 | 实测 | 一致 |
|---|---|---|---|
| 规则 §8 切出件 `results/verdict/judgement/_tr3s_rule_s8_extract_2026_10_25.md` | 9,139 B／`0278ed1e7e62` | 9139 B／`0278ed1e7e62` | ✅ |
| 语料 `.tmp/_g2narrow_out_stripped_v4_2026_10_25.json` | 16,813 B／`f07ad9bb262f` | 16813 B／`f07ad9bb262f` | ✅ |

语料件结构实测（`json.loads` 后逐条清点）：

- 顶层键 7：`['_stripped_note', 'armB', 'controls', 'elapsed_s', 'roots', 'roots_note', 'ts']`；`armB` 长度 **78**。
- 键集直方图：10 条＝`['bytes', 'path', 'reason', 'root', 'sha12']`。
- 键集直方图：68 条＝`['bytes', 'path', 'root', 'sha12']`。
- `reason` 唯一值＝`"name+fingerprint only; content not read"`（10 条·皆属 ARCHIVE）⇒ 该 10 件上游亦**未读内容**。
- **无任何 list／dict 型值字段**；字符串值最大长度 **150 B（＝path）** ⇒ **不存在摘录容器**。
- 体积核：`armB` 之 JSON 序列化占 **14031 B**／全件 16813 B ⇒ 非 `armB` 之部仅余 **2782 B**，而 `note`＋`controls`＋`roots`＋`roots_note`＋`ts` 实占 **1202 B** ⇒ 全件已由「身份字段＋控制组＋根清单」占满，**⛔0 容摘录**。

**前轮字段残留核（授料书称 NONE）**——于**全件字节层面**计命中：

| 词元 | `classA` | `classB` | `examplesB` | `nBA` | `nCA` | `plv3_family` | `ablation` | `nB` | `nC` | `bing` | `yi` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 命中数 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

⇒ **实测成立 ✅**（11 词元命中皆 0）：前轮之分类／计数／样例／族映射确已剥除。

## 2 · 段一（机械候选）· 执行与退化

- 规则 §8-2 之**扫描面**＝「件之全文（读乙；含表格行、标题、代码串、JSON 字面——⛔0 任何形态之预剔）」；词元表（封闭·可增）＝`不明`、`未核得`、`不知`、`不可判`、`存疑`、`悬置`、`未取得`、`不可得`、`待核`（主词元 `不明`、`未核得`；扩展族 7）。
- 授料内**不含任何件之正文**（78 条记录皆仅身份字段）⇒ **可扫面 ＝ 0 字**。
- 退而求其次：以语料**自身之文本**（`path` ＋ `reason` ＋ 顶层散文）作上述 9 词元之机械扫描 ⇒ **命中 0**（候选 **0**）；`controls.target_token` 之值（＝`不明`／`未核得`）为**元数据字段**，非对 78 件之陈述 ⇒ **不生成候选**。
- 全件原始文本中 9 词元之出现次数（供口径核）：`不明`=1、`未核得`=1、`不知`=0、`不可判`=0、`存疑`=0、`悬置`=0、`未取得`=0、`不可得`=0、`待核`=0 ⇒ 仅见于 `controls` 之 `target_token`。
- ⇒ **候选表为空**；§8-5 之「段一·位级可复算（重跑脚本⇒候选表逐位同）」本轮**不成立**（无可重跑之扫描面）。

## 3 · 段二（四问）· 未执行之由

- 0 候选 ⇒ 留痕表 0 行（§8-3：每候选一行；无候选即无留痕；「留空者视同 N」之规则**不触发**）。
- 四问之输入为「小句全文／行全文」⇒ 授料内无 ⇒ **不可施问**（非「四问判得 N」，而是**四问未施**）。
- **次序注记（分歧 D3）**——授料书称采认 #15 之次序为「一→四→三→二」且称规则件内应有载；本部**已通读规则件全文（90 行）**，**未见** `#15` 之编号，亦未见该次序之载文；规则件原文之问次为 **一→二→三→四**（§8-3 小节序列）。依授料书自身之命（「若无载，按规则件原文之序并在回报中标明」）⇒ 本轮采**一→二→三→四**；因 0 候选而无从体现（次序歧义**未生**）。

## 4 · 段三（件级）与读数

- **机械读法**（§8-4.1：件级＝其候选集之性质取最高级；全为 M 或候选集为空＝A）⇒ 在语料自身文本上得 **A=78**。
- **本轮裁定：⛔0 宣告 A**——§8-4.2 明定 A 之证成条件为「①候选集已逐条定性完毕（0 条留空）②无 C／B／N 候选」，并释义为「A ＝『经逐处定性·无状态断言』，**而非『剔除后无命中』**」。本轮之 0 候选**非**「经逐处定性」之所得（段一扫描面为空，未能在件之全文上执行）⇒ 实质要件①不满足 ⇒ 按 §8-3 兜底（⛔0 充 C、⛔0 充 A）与 §8-4.4（N 件必逐件列明，并入挂账＋设法辨明）⇒ **N**。
- **件级计数（以语料记录为单位）**：**C=0 ｜ B=0 ｜ N=78 ｜ A=0**。
- **件数口径备陈（不合成单一数）**：78 条记录中**不同内容（sha12）＝ 76**；同内容重复组 2：
  - `sha12=b9026cbf5ca2` ← rec3+53（〔归档区〕\_remote_delete_face_pullback_2026_10_18\verdict\pi_register\_v4_pi_cot_v3_dataset_addendum_s3_d1fill_2026_10_01.json／deposon-repo\results\verdict\pi_register\_v4_pi_cot_v3_dataset_addendum_s3_d1fill_2026_10_01.json）
  - `sha12=53c28ca1ae3d` ← rec7+27（〔归档区〕\results\readout\reading\_k_v3df_0_1_four_readings_2026_10_09.md.remote_2026_10_12／deposon-repo\results\readout\reading\_k_v3df_0_1_four_readings_2026_10_09.md）
  ⇒ 若以「不同内容件」为单位，N ＝ **76**。两口径**并列**，⛔0 合成单一数。
- **门② 之分子**：件级∈{C,B} 之件数 ＝ **0**（系**读数不可得**所致，⛔0 充「已测得 0」之断言）。**分母**：规则 §8-4.5 采「丙 48／乙 3／甲 20」＝71（沿前棒实测，本棒 0 重测）⇒ 与本语料 **78 记录不对应**（本语料含 10 ARCHIVE ＋ 6 件 `.remote_2026_10_12` 伪扩展名）⇒ 本件 **⛔0 出分子／分母之比**（§8-4.5「⛔0 合成单一数」之同族纪律）。
- **⛔0 宣告门② 成就或未成就**（§8-4.7：宣告权属 PI）。

## 5 · 真状态断言率

- 定义（授料书）：**真断言／候选总数**。
- 实测：**真断言数 ＝ 0**（候选 0 ⇒ 无候选可判真伪）；**候选总数 ＝ 0**。
- ⇒ 比率 ＝ **未定义（0／0）**。本件 **⛔0 将其记作 0%**（0/0 ≠ 0）：此为「**无读数**」，非「零断言率」。

## 6 · 难例清单（78 条·逐条一行）

**不可判之由（代码）**

- **D-1「无摘录·证据未取得」**——语料 v4 之该条记录**不含命中摘录** ⇒ 段一／段二之输入缺失；施判须开卷原件，而依铁律 3（⛔0 自行开卷「一开卷，独立即失」；ARCHIVE 正文⛔0 读）**本轮不开卷** ⇒ 记 **N（不可判）**，并入挂账＋设法辨明。
- ⚠ 此 N 属「**证据未取得**」型，⛔0 与「内容上不可判」之 N 混同：前者须**补授料**后重做段一与段二，后者须辨明后重做段二。
- 本表 `#` 列自 1 起，与语料 `armB` 之记录序**一一对应**（便于他读者回查原语料）。

| # | root | 路径（省去根前缀） | bytes | sha12 | 段一候选 | 段二留痕 | 件级 | 难例 |
|---:|:--|:--|---:|:--|---:|---:|:--:|:--|
| 1 | ARCHIVE | `〔归档区〕\_movedout_2026_10_22\readout\reading\results____k_v3df_0_1_four_readings_2026_10_09.json` | 65507 | `e87937d55471` | 0 | 0 | N | D-1 |
| 2 | ARCHIVE | `〔归档区〕\_movedout_2026_10_22\readout\reading\results____s4_substrate_grid_availability_2026_10_08.json` | 11446 | `66be80ab4b81` | 0 | 0 | N | D-1 |
| 3 | ARCHIVE | `〔归档区〕\_remote_delete_face_pullback_2026_10_18\verdict\pi_register\_v4_pi_cot_v3_dataset_addendum_s3_d1fill_2026_10_01.json` | 46909 | `b9026cbf5ca2` | 0 | 0 | N | D-1 |
| 4 | ARCHIVE | `〔归档区〕\results\doc\document\P_B_DISTORTION_BOUND_V0_SPEC.md` | 7126 | `bb7ca9838150` | 0 | 0 | N | D-1 |
| 5 | ARCHIVE | `〔归档区〕\results\doc\document\P_B_DISTORTION_BOUND_V0_SPEC.md.remote_2026_10_12` | 11246 | `638150884d18` | 0 | 0 | N | D-1 |
| 6 | ARCHIVE | `〔归档区〕\results\doc\document\_theory_input_request_supplement_2026_09_29.md.remote_2026_10_12` | 47799 | `20c4979626b2` | 0 | 0 | N | D-1 |
| 7 | ARCHIVE | `〔归档区〕\results\readout\reading\_k_v3df_0_1_four_readings_2026_10_09.md.remote_2026_10_12` | 46522 | `53c28ca1ae3d` | 0 | 0 | N | D-1 |
| 8 | ARCHIVE | `〔归档区〕\results\readout\run\_v3x_d0_5_aggregation_2026_09_17.md.remote_2026_10_12` | 12013 | `91cf5292a5a9` | 0 | 0 | N | D-1 |
| 9 | ARCHIVE | `〔归档区〕\results\readout\run\_v5_theory_input_acquisition_request_2026_09_29.md.remote_2026_10_12` | 10251 | `315e1fc71b5e` | 0 | 0 | N | D-1 |
| 10 | ARCHIVE | `〔归档区〕\results\verdict\judgement\_d1_backfill_intake_verdict_2026_10_01.md.remote_2026_10_12` | 42106 | `c6f90d7d3eb6` | 0 | 0 | N | D-1 |
| 11 | REPO | `deposon-repo\.tmp\_c514_remote_blobs_2026_10_18\docs__V3X__P_B_DISTORTION_BOUND_V0_SPEC.md` | 15549 | `aab9d78ada2d` | 0 | 0 | N | D-1 |
| 12 | REPO | `deposon-repo\.tmp\_c514_remote_blobs_2026_10_18\results___d1_backfill_intake_verdict_2026_10_01.md` | 42115 | `a7e8f90d9db7` | 0 | 0 | N | D-1 |
| 13 | REPO | `deposon-repo\.tmp\_c514_remote_blobs_2026_10_18\results___k_v3df_0_1_four_readings_2026_10_09.md` | 46514 | `1b860ba0a088` | 0 | 0 | N | D-1 |
| 14 | REPO | `deposon-repo\.tmp\_c514_remote_blobs_2026_10_18\results___theory_boundary_clone_sync_register_2026_10_09.md` | 17532 | `f6c7302b66da` | 0 | 0 | N | D-1 |
| 15 | REPO | `deposon-repo\.tmp\_c514_remote_blobs_2026_10_18\results___theory_input_request_supplement_2026_09_29.md` | 48280 | `5417d23e0e8d` | 0 | 0 | N | D-1 |
| 16 | REPO | `deposon-repo\.tmp\_c514_remote_blobs_2026_10_18\results___v3x_d0_5_aggregation_2026_09_17.md` | 12016 | `f69f13347825` | 0 | 0 | N | D-1 |
| 17 | REPO | `deposon-repo\.tmp\_item35_v3_collinear_recompute_2026_10_01.py` | 16493 | `c8d859cbb69e` | 0 | 0 | N | D-1 |
| 18 | REPO | `deposon-repo\corpus\v20\index_v3_2026_10_09.json` | 24837 | `74b27393574f` | 0 | 0 | N | D-1 |
| 19 | REPO | `deposon-repo\deposon_team\plugins\_v5_item35_v2_matrix_2026_09_29.py` | 44777 | `ef73f9b90afc` | 0 | 0 | N | D-1 |
| 20 | REPO | `deposon-repo\deposon_team\plugins\_v5_item35_v3_collinear_2026_09_29.py` | 63376 | `7115928822a1` | 0 | 0 | N | D-1 |
| 21 | REPO | `deposon-repo\docs\V3X\P_B_DISTORTION_BOUND_V0_SPEC.md` | 15457 | `423c84de20d5` | 0 | 0 | N | D-1 |
| 22 | REPO | `deposon-repo\results\evidence\register\_9model_full_merge_from_4workers_2026_10_09.json` | 19337 | `32aa0618a9d7` | 0 | 0 | N | D-1 |
| 23 | REPO | `deposon-repo\results\evidence\register\_t1_prereg_revision_qwen_temp_sweep_2026_10_09.md` | 16994 | `bda5d5f3dfa0` | 0 | 0 | N | D-1 |
| 24 | REPO | `deposon-repo\results\evidence\register\_t1_r2_activation_2026_10_09.md` | 21111 | `8e59b797aa2d` | 0 | 0 | N | D-1 |
| 25 | REPO | `deposon-repo\results\evidence\register\_v5_item35_prereg_v2_2026_09_28.md` | 35633 | `1fb2419c6e96` | 0 | 0 | N | D-1 |
| 26 | REPO | `deposon-repo\results\evidence\register\_v5_item35_v3_collinear_prereg_2026_09_29.md` | 42504 | `873652fd39dd` | 0 | 0 | N | D-1 |
| 27 | REPO | `deposon-repo\results\readout\reading\_k_v3df_0_1_four_readings_2026_10_09.md` | 46522 | `53c28ca1ae3d` | 0 | 0 | N | D-1 |
| 28 | REPO | `deposon-repo\results\readout\reading\_s3_d1fill_recount_2026_10_01.md` | 22877 | `a7dff824ed56` | 0 | 0 | N | D-1 |
| 29 | REPO | `deposon-repo\results\readout\reading\_s3_f1_loader_fix_recompute_2026_10_08.json` | 20144 | `3044a070106e` | 0 | 0 | N | D-1 |
| 30 | REPO | `deposon-repo\results\readout\reading\_s4_daily_share_margin_prerequisite_2026_10_09.md` | 18197 | `a929502e8421` | 0 | 0 | N | D-1 |
| 31 | REPO | `deposon-repo\results\readout\reading\_s4_daily_share_margin_recount_2026_10_23.md` | 16274 | `251afbce2a45` | 0 | 0 | N | D-1 |
| 32 | REPO | `deposon-repo\results\readout\reading\_s4_substrate_grid_availability_2026_10_08.md` | 14995 | `7deaee06c41a` | 0 | 0 | N | D-1 |
| 33 | REPO | `deposon-repo\results\readout\reading\_v5_item35_v3_collinear_recompute_2026_10_01.json` | 49682 | `a210e2c41275` | 0 | 0 | N | D-1 |
| 34 | REPO | `deposon-repo\results\readout\reading\c5_b_group_fix_readings_2026_10_09.json` | 10029 | `4e415990b71d` | 0 | 0 | N | D-1 |
| 35 | REPO | `deposon-repo\results\readout\run\_v3x_d0_5_aggregation_2026_09_17.md` | 12010 | `ddf0d1aa96d2` | 0 | 0 | N | D-1 |
| 36 | REPO | `deposon-repo\results\readout\run\_v4_supp_l14v3_batch8_r1_result.json` | 62531 | `e6a94a0a13b7` | 0 | 0 | N | D-1 |
| 37 | REPO | `deposon-repo\results\readout\run\_v4_supp_l14v3_batch8_r2_result.json` | 63440 | `7b23996b5f4c` | 0 | 0 | N | D-1 |
| 38 | REPO | `deposon-repo\results\readout\run\_v4_supp_l14v3_batch8_r3_result.json` | 63670 | `56faf9324fba` | 0 | 0 | N | D-1 |
| 39 | REPO | `deposon-repo\results\readout\run\_v4_supp_l14v3_batch8_r4_result.json` | 64038 | `c7d5aa2a9b00` | 0 | 0 | N | D-1 |
| 40 | REPO | `deposon-repo\results\readout\run\_v4_supp_l14v3_batch8_r5_result.json` | 63785 | `3620a7daf9c1` | 0 | 0 | N | D-1 |
| 41 | REPO | `deposon-repo\results\readout\run\_v5_item35_v2_matrix_exec_2026_09_29.md` | 24624 | `4e88682284d8` | 0 | 0 | N | D-1 |
| 42 | REPO | `deposon-repo\results\readout\run\_v5_item35_v2_matrix_result_2026_09_29.json` | 84699 | `13ad5b740f80` | 0 | 0 | N | D-1 |
| 43 | REPO | `deposon-repo\results\readout\run\_v5_item35_v3_collinear_result_2026_09_29.json` | 187287 | `99f3e504589e` | 0 | 0 | N | D-1 |
| 44 | REPO | `deposon-repo\results\readout\run\_v5_theory_input_acquisition_request_2026_09_29.md` | 10751 | `19099ecb3c46` | 0 | 0 | N | D-1 |
| 45 | REPO | `deposon-repo\results\readout\run\deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json` | 21176 | `95f3f0957be8` | 0 | 0 | N | D-1 |
| 46 | REPO | `deposon-repo\results\tool\generator\_v4_supp_l14v3_batch8_r1_executor.py` | 56181 | `1e5f2249c517` | 0 | 0 | N | D-1 |
| 47 | REPO | `deposon-repo\results\tool\generator\_v4_supp_l14v3_batch8_r2_executor.py` | 57634 | `6a9bbc43c808` | 0 | 0 | N | D-1 |
| 48 | REPO | `deposon-repo\results\tool\generator\_v4_supp_l14v3_batch8_r3_executor.py` | 58494 | `0f654d945f12` | 0 | 0 | N | D-1 |
| 49 | REPO | `deposon-repo\results\tool\generator\_v4_supp_l14v3_batch8_r4_executor.py` | 59351 | `6b69ec8406d4` | 0 | 0 | N | D-1 |
| 50 | REPO | `deposon-repo\results\tool\generator\_v4_supp_l14v3_batch8_r5_executor.py` | 60475 | `6961281824ae` | 0 | 0 | N | D-1 |
| 51 | REPO | `deposon-repo\results\verdict\judgement\_d1_backfill_intake_verdict_2026_10_01.md` | 42115 | `42a3858976f2` | 0 | 0 | N | D-1 |
| 52 | REPO | `deposon-repo\results\verdict\judgement\_v5_item35_v2_verdict_2026_09_29.md` | 26232 | `b59bef293712` | 0 | 0 | N | D-1 |
| 53 | REPO | `deposon-repo\results\verdict\pi_register\_v4_pi_cot_v3_dataset_addendum_s3_d1fill_2026_10_01.json` | 46909 | `b9026cbf5ca2` | 0 | 0 | N | D-1 |
| 54 | SUB | `deposon-sub\results\_backfill_rule_final_2026_10_09.md` | 34602 | `3e97d5286760` | 0 | 0 | N | D-1 |
| 55 | SUB | `deposon-sub\results\_d05_backbone_robustness_beta_20260918_100853.json` | 1490 | `9b6f085d96dc` | 0 | 0 | N | D-1 |
| 56 | SUB | `deposon-sub\results\_d05_i1i5_invariants_check_20260918_100853.json` | 1920 | `f12af5435928` | 0 | 0 | N | D-1 |
| 57 | SUB | `deposon-sub\results\_d05_main_run_results_20260918_100853.json` | 15243 | `0a933d7c8d7a` | 0 | 0 | N | D-1 |
| 58 | SUB | `deposon-sub\results\_d05_main_run_results_nemotron_3.5_20260918_100853.json` | 15111 | `1b1b6ad67c39` | 0 | 0 | N | D-1 |
| 59 | SUB | `deposon-sub\results\_d05_main_run_results_qwen3_failed_20260918_100853.json` | 18358 | `427b18da8114` | 0 | 0 | N | D-1 |
| 60 | SUB | `deposon-sub\results\_d05_opt_5_directions_results_20260918_100853.json` | 5614 | `e5979133195a` | 0 | 0 | N | D-1 |
| 61 | SUB | `deposon-sub\results\_d1_backfill_b3_b7_suggestion_table_2026_10_01.md` | 26731 | `8e1494301bb8` | 0 | 0 | N | D-1 |
| 62 | SUB | `deposon-sub\results\_d1_backfill_collection_rounds_2026_10_01.md` | 22908 | `2d1a0d43e588` | 0 | 0 | N | D-1 |
| 63 | SUB | `deposon-sub\results\_d1_backfill_conflict_trace_2026_10_01.md` | 31506 | `0cecda616f15` | 0 | 0 | N | D-1 |
| 64 | SUB | `deposon-sub\results\_d1_backfill_readiness_pack_2026_10_01.md` | 26462 | `ed644fb07f88` | 0 | 0 | N | D-1 |
| 65 | SUB | `deposon-sub\results\_theory_input_request_supplement_2026_09_29.md` | 48190 | `c966e7b605af` | 0 | 0 | N | D-1 |
| 66 | SUB | `deposon-sub\results\doc\document\_d05_combined_report_20260918_100853.md` | 10555 | `c87eb8974268` | 0 | 0 | N | D-1 |
| 67 | SUB | `deposon-sub\results\doc\document\_d1_backfill_event_id_prefix_proposal_2026_10_01.md` | 14074 | `2636394df918` | 0 | 0 | N | D-1 |
| 68 | SUB | `deposon-sub\results\evidence\register\_9model_merge_disposition_register_2026_10_09.md` | 11651 | `455277298212` | 0 | 0 | N | D-1 |
| 69 | SUB | `deposon-sub\results\evidence\register\_k_v3s_3_4_lock_freeze_2026_10_08.md` | 16973 | `c64865c32761` | 0 | 0 | N | D-1 |
| 70 | SUB | `deposon-sub\results\evidence\register\_s4_reading_surface_and_authority_register_2026_10_09.md` | 34405 | `0148b5271154` | 0 | 0 | N | D-1 |
| 71 | SUB | `deposon-sub\results\evidence\register\_theory_boundary_clone_sync_register_2026_10_09.md` | 17528 | `1f9fd007649c` | 0 | 0 | N | D-1 |
| 72 | SUB | `deposon-sub\results\readout\reading\_c_reading_recompute_2026_10_09.md` | 21006 | `95d7d23d24fd` | 0 | 0 | N | D-1 |
| 73 | SUB | `deposon-sub\results\readout\reading\_s3_f1_loader_fix_recompute_2026_10_08.md` | 22065 | `b2c9840d237b` | 0 | 0 | N | D-1 |
| 74 | SUB | `deposon-sub\results\readout\run\_v5_item35_v3_collinear_exec_2026_09_29.md` | 46000 | `912afffed6b9` | 0 | 0 | N | D-1 |
| 75 | SUB | `deposon-sub\results\readout\run\_v5_theory_input_acquisition_request_2026_09_29.md` | 10691 | `83afc4802fe7` | 0 | 0 | N | D-1 |
| 76 | SUB | `deposon-sub\results\verdict\judgement\_v5_item35_v3_collinear_verdict_2026_10_01.md` | 38266 | `363cce3dae59` | 0 | 0 | N | D-1 |
| 77 | SUB | `deposon-sub\results\verdict\judgement\_v5_item35_v3_collinear_verdict_prep_2026_10_01.md` | 33755 | `a31026f2384d` | 0 | 0 | N | D-1 |
| 78 | SUB | `deposon-sub\results\work\process\_dup_name_diff_content_scan_2026_10_08.json` | 1302889 | `a27d11f45c21` | 0 | 0 | N | D-1 |

### 6.1 · 件级归类前之身份核验（字节级·不引入正文入上下文）

- **67／68** 条非 ARCHIVE 记录之 bytes＋sha12 与语料所载**逐位相符**（实测）⇒ 语料之**身份层完好**。
- **盘上已不存在（活件漂移／清理）**：rec17 `deposon-repo\.tmp\_item35_v3_collinear_recompute_2026_10_01.py` ⇒ 其 bytes／sha12 为**转引·未测**。
- **10 条 ARCHIVE 未核**（铁律 3 之硬禁：⛔0 读归档区正文）⇒ 其 bytes／sha12 为**转引·未测**。
- ⇒ **诊断**：语料之**身份层完好**、缺陷**仅在「摘录层」缺失** ⇒ 补授料之最小面为「摘录」，身份层**不必重测**（rec17 除外）。

## 7 · 阴性断言（射程写死 ＋ 同批正控）

**阴性断言（射程）**

- 本件**不**断言 armB 78 件中任何一件之「不明／未核得」状态为「无」；
- 本件**不**断言任何件含或不含真状态断言（除「语料自身文本上机械扫描得 0 候选」这一**关于语料之陈述**外）；
- 本件**不**断言 78 件之候选数、命中内容、件级之实质归属；
- 本件**不**以「0 候选」充「无不明状态」（§8-4.2 之禁）。

**同批正控（语料内 `controls`·转引·未测·未开卷）**

| 正控 | 目标词元 | 命中数 | bytes | sha12 |
|:--|:--|---:|---:|:--|
| `alive_buming` → `results/verdict/judgement/_five_zero_recount_under_settled_calibers_2026_10_25.md` | `不明` | 12 | 63083 | `f775cd51a5ff` |
| `alive_wuhe` → `results/verdict/judgement/_gate2_denominator_dispute_2026_10_25.md` | `未核得` | 7 | 34737 | `5b6c39c5b948` |
| `identity_positive_control` → `〔本地路径已脱敏〕` | —（身份正控） | — | 45590 | `ce64b9b97489` |

- 正控之射程：**仅**证同批扫描器对 `不明`／`未核得` 两词**为活**（token_hits>0）；**不**证其命中上下文之性质（**未开卷**：二者之路径落于 `results/verdict/judgement/` 目录 或 文件名含 `dispute` ⇒ 依禁读面不开卷）。
- **附注（未核）**——正控之 `target_token` 仅示 `不明`／`未核得` 两词；语料**未载**扫描器之完整词元集 ⇒ 78 件是否为 TR-3S **九词元**全覆盖之结果，**无从核验**。若上游仅以二主词元扫描，则扩展族 7 词之命中文件**未入此 78 件**——此属**口径差异之待裁面**，本部⛔0 判定，仅呈记。

## 8 · 未核／未开卷之面（老实交代）

1. **未开卷**——78 件之正文：ARCHIVE 10 件（铁律 3 之硬禁）；REPO 43 ＋ SUB 25（铁律 3 之「⛔0 自行开卷（一开卷，独立即失）」）。**未以任何形式读取其正文文本入上下文**；仅对 67 件作**字节级指纹核对**（SHA-12＋长度，不产生文本）。
2. **未开卷**——`controls` 之三件（目录／文件名落于禁读面或与判读面同族）。
3. **未读禁读件**（逐件声明）：`_unclear_second_judge_2026_10_25.md`（162,211 B）、`_unclear_second_judge_clean_2026_10_25.md`（46,555 B）、`_unclear_reading_rule_dispute_2026_10_25.md`（53,237 B）、`_unclear_rule_ablation_side_and_tr3s_2026_10_25.md`（38,806 B）、`_gate2_narrow_measure_and_ablation_2026_10_25.md`（44,000 B）；另**未读**任何文件名含 `judge`／`ablation`／`dispute` 之件。**本部只读了授料书所许之规则切出件（其 §8 节）与语料 v4 之二件。**
4. **未读**——`.tmp` 内同族语料变体：`_g2narrow_out_2026_10_25.json`、`_g2narrow_out_stripped.json`、`_g2narrow_out_stripped_v2_2026_10_25.json`、`_g2narrow_out_stripped_v3_2026_10_25.json`（**仅列名，未开卷**）⇒ 其中任一件若载摘录，可作补授料之来源（**须 PI 给或另派**；本部⛔0 擅取，亦⛔0 自行剥制 v5）。
5. **未核**——扫描器之完整词元集（见 §7 末注）。
6. **未核**——门② 分母（丙 48／乙 3／甲 20）与本 78 记录之对应关系（未开卷名单件）。
7. **未核**——读甲／读乙两读之并出（须件之全文；§8-4.6 之「非 Markdown 件读甲恒为 A」亦须原文方可施）。
8. **未核**——非 Markdown 件（24 `.json` ＋ 8 `.py` ＋ 6 `.remote_2026_10_12` ＝ 38／78）之载体失效面「何为产出件之陈述」（§8-7② 明载**须 PI 给**）。
9. **未做**——四问次序「一→四→三→二」与「一→二→三→四」之敏感度测试（无候选可测）。

## 9 · 复算方式（本件之可复算性）

- §1–§5 之**结构、计数、核验**：位级可复算（脚本：`.tmp/_tr3s_probe_2026_10_25.py`、`.tmp/_tr3s_fpcheck_2026_10_25.py`；本件之表由 `.tmp/_tr3s_r3_report_gen_2026_10_25.py` 自语料生成）。
- §6 之**分类**：**未复算**（无可执行输入）——此非「已核」，而是「**未测**」。

## 10 · 与授料书之分歧登记（3 项）

| # | 授料书所述 | 实测／规则原文 | 本轮处置 |
|:-:|:--|:--|:--|
| D1 | 每条记录含「剔除前之原始命中摘录」 | **无**：键集仅 4–5 字段，无摘录容器；全件已由身份字段＋控制组占满 | 段一／段二不可执行 ⇒ 78 件全 N；建议重剥 v5 保留摘录 |
| D2 | 段一「含其所定之剔除（否定式、计数零、『不明文』词形之子串等）」 | 规则 §8-2 明载「段一**只生成、不剔除**（⛔0 任何剔除）」；否定式／计数零属 §8-3 **问四**（⇒ M）；「不明文」词形之子串**规则件内未载** | 按**规则原文**执行（段一不剔除）；否定／计数零之判留待段二 |
| D3 | 四问次序「一→四→三→二」（采认 #15），规则件内应有载 | 规则件**未载** #15 与该次序；原文之序为 一→二→三→四 | 依授料书之命采**原文之序**；本轮 0 候选，歧义未生 |

## 11 · 本件之自限（⛔ 清单）

⛔0 落五终判（pass/af/kd/fail/give-up）｜⛔0 代 PI 裁｜⛔0 宣告门② 成就或段毕｜⛔0 回改任何既有件（新建此一件而已）｜⛔0 读归档区正文｜⛔0 读禁读件｜⛔0 以「0 候选」充「无不明状态」｜⛔0 合成单一数（计数双口径并列）｜⛔0 宣告真状态断言率之数（记「未定义」）｜⛔0 自行剥制语料 v5。
