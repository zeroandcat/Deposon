# 未读后台回执全量回捞 · 登记件（回执面）

- 任务：未读后台回执全量回捞（显/隐性遗忘 · 回执面）
- 出件 agent：evidence-auditor（署名如实，不代裁）
- 依据：PI 2026-10-08 令「盘点与回捞所有可能事实未收口的显性与隐性遗忘项，本周内完整收尾 V3~V4 全部实验，并全量清点实验成果」
- 落盘时点：2026-10-08 16:2x (+08:00)
- 性质：只读审计 + 登记。0 回改既有件、0 网络、0 代裁。

---

## §1 口径与数据源

### §1.1 数据源

| 源 | 路径 | 访问方式 |
|---|---|---|
| 任务库 | `〔本地绝对路径·脱敏略:runtime-state.sqlite〕` | **只读** URI `?mode=ro`，SQL 全参数占位；0 写入、0 checkpoint |
| 回执面 | `〔本地绝对路径·脱敏略:background-tasks〕\<task_id>\` | 逐件读 `summary.txt`；缺则读 `output.log` |

### §1.2 目标集判定口径

- 目标集＝`delivered_at_ms IS NULL`（未投递）AND `owner_session_id='mvs_bbeb804b1a6a41109be740636eed1709'`（本次 parent 会话）
- 全库背景：总任务 21,772 件；全库未投递 1,450 件；本 owner 全量 2,569 件、其中未投递 **55 件**＝本件目标集。
- 未投递按 owner 分布（top 10，仅作背景，非本次范围）：

| owner_session_id | 未投递数 |
|---|---|
| mvs_43c9aeefb0434f31afdef683f2d0371a | 109 |
| mvs_0d3b22d4f5b3411989e3187387bdd6e1 | 84 |
| mvs_e75ec4760b3f4e3f82f665db85d24ffd | 72 |
| mvs_0b8237ae75aa407484eae3e61e998dbb | 67 |
| mvs_65155fa2f1cd4fd9869c9a2bf308d12d | 61 |
| **mvs_bbeb804b1a6a41109be740636eed1709（本件）** | **55** |
| mvs_9065aeb7d33a48e5b57195687683066c | 50 |
| mvs_b74c4255e9f44302ab7ccb838b145d6a | 48 |
| mvs_fead46d72f2240a2aa59026dddefcda0 | 40 |
| mvs_7227d982a9364988bcb419b66910b8dd | 38 |

### §1.3 目标集构成

| 维度 | 分布 |
|---|---|
| status | succeeded 24 ／ canceled 15 ／ failed 9 ／ lost 5 ／ **running 2** |
| kind | subagent 39 ／ bash 16 |
| 时段 | 2026-09-10 ～ 2026-10-08（持续近 1 月，非单点事件） |
| 回执可读性 | `summary.txt` 存在 41/55；5 件 lost + 1 件 running 无目录；1 件 succeeded 输出 0 字节 |

**重要口径**：55 件中含本件自身（`bg_b3bb81b8…`＝本次回捞任务，running）与同期并行的另 2 件（`bg_61bb2040…` 清卡素材编译 running、`bg_aadf2110…` 缺件深挖回执 EA succeeded）。running 2 件在结束前不具备完整回执，**不判为未收口**，仅登记在跑。

---

## §2 逐件全量表

> 列义：`task_id`（短 8 位）｜status｜结束时点 (+08:00)｜回执要点（产物/声明/待办/异常，≤2 行/类）｜产物对账。
> 对账标记：`MATCH`＝声明路径实测在盘并给出 SHA-256[:12]；`OUTSIDE`＝实存于仓外/归档面（幽灵引用，实件在但不在原声明位置）；`MISSING_TRUE`＝三面（repo／deposon-sub／归档区）全遍历后确无，写真缺件；`不可判`＝回执未给可提取路径；`N/A`＝纯删除/清理作业，不产生交付物。

### §2.1 组 A：subagent · succeeded（声明已交付，产物需核盘）——共 12 件

| # | task_id | 结束 | 声明主题 | 回执要点 | 产物对账 |
|---|---|---|---|---|---|
| A1 | `bg_07a2ed29` | 09-10 17:38 | 22 caption 火山方舟 embedding 验证 | 产物：JSON 结果 + MD 报告。声明：ratio=1.0562 → 判 **NOISE**（intra 0.6838 vs inter 0.6474）；KMeans ARI=0.06。异常：22 caption 文本来源需回溯定位（`_v41_…embs.bak.json` 的 `object` 字段非 caption 文本）。 | JSON `results/deposon_volcengine_22caption_embedding_2026_09_10.json` **MATCH** `c4b774c8e34c`／4,559 B；MD `docs/V3X/VOLCENGINE_22CAPTION_EMBEDDING_2026_09_10.md` → **OUTSIDE**（归档区 `〔归档区〕/docs/V3X/`，`8464109947dd`／9,294 B）；`_volc_22cap_emb.py` **OUTSIDE**（`results/_archive_2026_09_24/`，`15904ecae629`／11,105 B）；`_inspect_captions.py` **OUTSIDE**（3 处同哈希 `dfb02ade1474`／591 B）；`_volc_22cap_emb.log` → **MISSING_TRUE** |
| A2 | `bg_92b6eeb4` | 09-10 21:29 | 补测 worker C（glm-5.3 + doubao-seed-evolving） | 产物：JSON + 脚本 + MD 报告。声明：60 LLM calls 实跑完成、2 model sanity PASS、无重试/无切 model。待办：等 parent 合并 4 worker 结果到 9-model 全量 JSON（棒方明示交接）。异常：blockers 无；自陈风险「results/ 临时件如需清理请手动」。 | `results/deposon_volcengine_worker_c_2026_09_10.json` **MATCH** `f6f172820c97`／51,716 B；`…worker_c_2026_09_10.py` **MATCH** `b5eeef1e9bd7`／11,692 B；MD 报告 → **OUTSIDE**（归档区 `docs/V3X/`，`098dceadec82`／9,723 B）；`_verify_worker_c.py` → **OUTSIDE**（`results/_archive_2026_09_24/`，`cc578c46b332`）；2 件 .log → **MISSING_TRUE** |
| A3 | `bg_552544f7` | 09-18 09:38 | D+0.5 主跑 + 5 方向 + 8 缺陷修正 | 声明：进度 0% 启动中，M1–M8 待办清单已立（含 DeepSeek/Qwen3 30 cells、8 处报告缺陷修正、6 制品 SHA-12）。回执止于侦察阶段。 | **不可判**（回执未给可提取产物路径；status=succeeded 与回执内容「启动中」不自洽 → 见 §4 A-3） |
| A4 | `bg_2bf99d32` | 09-18 10:56 | Deposon v2 scripts 复算 | 产物：5 制品（worker py + 3 件 JSON/MD）。声明：8 维 ALL_PASS、0 LLM、0 key 落盘、0 frozen 触动。异常：statsmodels 未安装（以 pure numpy 复算，Newcombe 与 ref 在 1e-16 内一致）；5 制品路径推断自 `corpus/v20/by_model/`。 | 5 件**全部 OUTSIDE**：worker py → `deposon-sub/results/_archive_2026_09_20/`（`18984b04c45e`／34,134 B）；`_deposon_v2scripts_kimi7_audit_…json` → `deposon-sub/results/`（`3da62b979053`）；`_deposon_v2scripts_reverify_…json` → 同面（`8ac002ccb082`）；`_deposon_v2scripts_reverify_…md` → 同面（`ee005ea1f031`）；`_deposon_v2scripts_summary_挂点回扣_…json` → 同面（`2ca5870e4659`／404 B） |
| A5 | `bg_2d153d13` | 09-20 11:25 | explorer 生成 拉回清单 + 远端删除清单 双清单 | 声明：产出「拉回清单 + 远端删除清单」双清单。异常：`output.log` **0 字节**、无 `summary.txt` → 无任何可核回执内容。 | **不可判**（产物无落盘记录；按「0 产物不编造」不推定其已生成） |
| A6 | `bg_5a9cea83` | 09-25 03:31 | GLM_1 distill 侧 round1（batch7 r5 收官棒） | 产物：executor + result + run.log。声明：baseline [r1–r4] = 88 calls/88 ok/0 empty；累计 **318 calls/9 empty/2.83%** 远低于 0.50 阈值；batch7 达成 **5/5 收官**。待办：全部未决项统留 verdict-keeper 终裁（棒方明示交权）。异常：blockers 无。 | `results/_v4_supp_l14v3_batch7_r5_executor.py` **MATCH**（存在；53,155 B）；`…r5_result.json` **MATCH**（存在；61,658 B）；`_v4_supp_l14v3_batch7_r5_run.log` → 三面未见 → **MISSING_TRUE**（run.log 类日志面） |
| A7 | `bg_73c9f9ec` | 09-26 22:57 | E-38 署名口径修正（不冒充 Trae） | 产物：勘误链 v21 追加（锚件 `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`）。声明：锚定 SHA-12 `FCCFCC869E7A`／257,362 B 与派工一致；旧末行「出证：Trae code」一字不动保留。异常：无。 | 锚件 **MATCH**（在盘；实测 SHA-12 `41f5f1689d09`／857,551 B）。⚠ 实测值 ≠ 棒方声明的 v20 值 `FCCFCC869E7A`／257,362 B —— 属**后续版本继续追加**（v20→v21 及其后），非篡改；字节量级差异（257 KB→858 KB）与多轮追加一致。登记为「登记值落后于盘上终态」，非缺件 |
| A8 | `bg_b7755687` | 10-08 16:13 | N-3① T-1 §7.2 更正件（VK） | 产物：更正/脚注件 1 件。声明：根因确证属**登记计数瑕疵面**（§7.2「非证伪=13」vs 明细实列 12 行，差量 ±1；四栏和 18 vs 明细覆盖 17）。异常（2 项已写入件内自证）；未闭/待 PI（4 项）：更正是否生效即锁、「十八行」口径二择一、第 17 行归属、下游两件是否同步更正及权属。 | `results/_t1_7_2_correction_2026_10_08.md` **MATCH** `cb0195c06647`／16,476 B |
| A9 | `bg_aadf2110` | 10-08 16:18 | N-3③ 缺件深挖检索回执（EA） | 产物：检索回执 1 件。声明：四项缺件**全部实存且 MATCH 登记值**（R-93/94 主仓 `results/`、R-114/115 归档区 `results/`）；远端 HEAD tree `72c5839` 下四路径 404、`commits?path=` 全史返回空数组 ⇒ 远端确无，GLM 记载属实；三面 .git 全 0。异常：GitHub code search 需认证（401）→ 改 git trees/commits 接口绕过（未越权）。 | `results/_pending_supply_search_receipt_2026_10_08.md` **MATCH** `11bbee2bea42`／12,595 B |
| A10 | `bg_c6d03c39` | 10-08 16:20 | N-7 G4 剩面只读探 | 产物：探件 1 件。声明：sqlite（474,656,768 B）与 outbox（实测 6,335 B）两载体均已探完且可读；**E1–E4 四项在两载体中均为「无」**。异常：①上棒件 §6 实况仅有 §6.1，**不存在 §6.3**（与派工描述有偏差，如实登记）；②outbox 三处字节互异（3,113／6,335／8,402）；③⛔ 0 假闭环——闭环门「仍需 runtime 打点 E1–E4」**未被解除**；④`results/` 另 4 件 16:00–16:17 mtime 件非本棒产出。 | `results/_g4_residual_probe_2026_10_08.md` **MATCH** `3554aa156e08`／23,025 B |
| A11 | `bg_abc079a2` | 09-16 11:31 | 建目录 `deposon_team/_designs` | 声明：`CREATED: 〔幽灵引用·原件已缺席·未上传:_designs〕`。 | **OUTSIDE**：该目录已不在主仓，现存 `deposon-sub/deposon_team/_designs` 与归档区 `〔归档区〕/deposon_team/_designs`。属后续迁移/归档所致，创建动作本身当时成功 |
| A12 | `bg_a9111db0` | 09-21 20:10 | 空目录树清点（10 棵 maximal empty tree） | 声明：REPO_FILES=620、ALL_DIRS=87、EMPTY_TREES=10、ROOT_VERIFIER_EXISTS（119 件）、`LIST_FILE_WRITTEN=10`、`ALL_CHECKS=PASS`。待办：把 `results/` 下 10 棵空树（含 `_p_j_convergence_basin_2026_09_16`、`_v3x_18frozen_remeasure_2026_09_16` 等）回填或删并 —— **本棒仅列清单，未处置**。 | **不可判**（回执未给清单文件路径）；`ALL_CHECKS=PASS` 为棒方自述，未独立复核 |

### §2.2 组 B：subagent · canceled（中断，产物多未落）——共 12 件

| # | task_id | 结束 | 声明主题 | 回执要点 | 产物对账 |
|---|---|---|---|---|---|
| B1 | `bg_f2a2f777` | 09-10 17:40 | 火山引擎 Chat 接入（agent-plan + Doubao） | 进度 0%，待办 [读 key / 列 model / sanity / 5 cells / JSON / 报告] 全未执行。异常：aborted。 | **不可判**（无产物路径） |
| B2 | `bg_861d2725` | 09-10 18:13 | Deposon ↔ Embedding 6 方向综合验证 | 进度 5%，阶段 1–4 待办全未执行。异常：aborted。 | **不可判** |
| B3 | `bg_12a74b3a` | 09-10 18:13 | 火山 7 model 1-cell sanity chat 试调 | 进度 20%，7 sanity 未跑完。异常：aborted。 | **不可判** |
| B4 | `bg_3020cff5` | 09-11 12:00 | C+D+E: V3 综合 V7 + BOSS URL 补查 + P-F V0.1 升级 | 进度 33%：C 阶段声明完成（V7 综合报告 37 KB + JSON 23 KB）；**D 阶段（BOSS URL 诚实披露）、E 阶段（P-F V0.1 升级）未开始**。异常：aborted。 | **不可判**（回执未给路径）；内容面检索 `V7 综合报告`/`_v3x_6way_*` 无独立件 → C 阶段产物疑似已被后续清理/并入归档，**不可判不推定** |
| B5 | `bg_21191cee` | 09-18 10:06 | 增补实验全套 实际执行 | 进度 0%，待办 7 项全未执行。异常：aborted。**关键联动**：其后 `bg_df7601e7`（A 组外的 bash 件）执行「沿 mavis-trash 删除本棒真产出 6 文件」，即本棒曾落盘后被清理。 | 原路径 `results/_d05_main_run_results_20260918_100853.json` 等 **MISSING_TRUE**（三面全无，与「已被 trash 清理」一致） |
| B6 | `bg_6a3f6e76` | 09-18 11:54 | 复核 Trae letter 起草改进需求 V2 | 进度未记录即中断。异常：`runtime-shutdown`（非用户主动取消）。 | **不可判**；后续存在 `letters/TRAE_V3_CODE_IMPROVEMENT_LETTER_2026_09_17.md` 等同族件，但**不能确证即本棒产出** → 不判 FOUND |
| B7 | `bg_b40818cb` | 09-18 11:54 | 起草 GLM 回函 V2 模板 | 进度 0%（M1/N5：扫描 6 输入资产 + SHA-12 验真）即中断。异常：`runtime-shutdown`。 | **不可判**；后续 `letters/查理_glm_dualtrack_paper_sole_letter_2026_10_01.md` 存在，但无法归因本棒 → 不判 FOUND |
| B8 | `bg_ccebdf21` | 09-20 11:36 | doc-writer 起草给 kimi 的委托信 + 远端删除清单 | 声明：0 产物老实交代；起草前 PowerShell `$f` 变量歧义，改用脚本文件。异常：aborted。 | **不可判**；同族 `deposon-sub/results/_archive_2026_09_20/_letter_to_kimi_push_v3_委托_2026_09_17.md` 在盘，**但日期早于本棒**（09-17 < 09-20）⇒ 非本棒产物 |
| B9 | `bg_6c32b0af` | 09-20 15:46 | explorer 调研 P0 5 件 V1~V3 frozen asset 真实数据 | 进度至 Step 4（Step1–4 有执行痕迹），Step5（observer/Bell/Poincaré 真实存在性）、Step6（7+9 铁律自查）**未完成**。异常：aborted。 | **不可判**（无报告落盘记录） |
| B10 | `bg_9f039995` | 09-23 17:26 | N-22s margin 增宽重验（新开 manifest） | 声明：5 步计划（pre-fingerprint → manifest v2 + executor → 跑 → post-fingerprint 验 0 触动 → verdict md）。异常：aborted。 | **不可判**（本棒路径未落）；但后续件确在盘：归档区 `_v4_n22s_margin_manifest_v2.json`、`_v4_n22s_margin_executor_2026_09_23.py`、`_v4_exec_n22s_margin_result.json`、pre/post hashes txt ⇒ **待办已被后续棒实质覆盖**，登记为「旧态已被后续覆盖」 |
| B11 | `bg_3416a60c` | 09-24 20:35 | T1 温度/端点敏感性实测 | 进度 5%（勘察 prereg + l12 executor 字面）；待办 [executor 起草] [2×3×2=12 格矩阵实跑] [result.json 落盘] [SHA-12 回报] 全未执行。异常：aborted。 | 本棒路径未落；后续件确在盘：归档区 `_remote_version_freeze_2026_09_26/_v4_supp_t1_executor.py`、`_v4_supp_t1_verdict.md` ⇒ **已被后续覆盖** |
| B12 | `bg_71d98eb6` | 09-24 20:37 | T1 预登记修订：砍端点维度改 qwen 温扫 | 进度 5%，仅列「读 T1 原件 `802DECE2286A`／activation `79936B630015`／Q2 拍板档」待办即中断。异常：aborted。 | **不可判**；未检出 `_t1_rev1*` 命名件，也未检出与 `802DECE2286A` 明确对应的修订件 ⇒ 修订动作**疑似未收口** |

### §2.3 组 C：subagent · failed ——共 4 件

| # | task_id | 结束 | 声明主题 | 回执要点 | 产物对账 |
|---|---|---|---|---|---|
| C1 | `bg_214a5faf` | 09-17 16:06 | 向量化 豆包 embedding（P-L v3 Phase 2，4 端点 × L=30） | 进度 10%（§1 proxy 探活 ✅、§2 ark coding-plan 端点 ✅）；§3 sanity 发现关键问题后中断。异常：`net::ERR_CONNECTION_CLOSED`。 | **不可判**（无产物路径落盘）；后续 P-L v3 phase2 runner/console 日志已被 09-21 trash 批量清理（见 §2.4 组 D） |
| C2 | `bg_f2b4f7b8` | 09-28 21:36 | 【重派】P 系落地立线包：端点定义提案＋KD 扩面＋生效补登 | 声明：锚点 10 项指纹实测全 MATCH；「起草两件新件（新名，0 写既有件）」**未完成即中断**。异常：`net::ERR_CONNECTION_RESET`。 | 本棒**未落盘**；但后续件在盘：`results/_v5_item26b_endpoint_definition_prereg_2026_09_28.md`、`_v5_item26b_attribution_effective_2026_09_28.md` ⇒ **立线包已被后续棒实质完成**，登记为「已被覆盖」 |
| C3 | `bg_73ae7913` | 09-29 19:49 | V3 判定勘误注记件（I-1..I-8 + 指纹歧义） | 声明：4 件锚哈希实测吻合；发现 I-8b 自身计数 delta；#11 指纹 `b70211bfa83e` 实测为真；逐条核验 I-2/I-4/I-5/I-7 后**起草中断**。异常：Token Plan 用量上限（2056）。 | **不可判**（勘误件未落盘路径）；后续 V3 判定面已由 `results/_v5_v3_deg_p1_reopen_verdict_r2_2026_09_29.md` 等覆盖 |
| C4 | `bg_5191d241` | 09-29 14:32 | V3 重开跑判定面（verdict-keeper） | 声明：4 件哈希实测吻合（`38231ef6f053`／`4afeb8cd41de`／`2ea1c2cee65d`／`b86d6740d487`）后即中断。异常：Token Plan 上限（2056）。 | **不可判**；后续件在盘：`results/_v5_v3_deg_p1_reopen_exec_2026_09_29.md`、`…_result_….json`、`…_verdict….md`、`…_verdict_r2_….md` ⇒ **已被覆盖** |

### §2.4 组 D：bash · succeeded（多为 mavis-trash 清理/迁移作业，声明即「已删除/已迁移」）——共 14 件

| # | task_id | 结束 | 声明主题 | 回执要点 | 产物对账 |
|---|---|---|---|---|---|
| D1 | `bg_b81501a9` | 09-21 19:14 | trash：`deposon-sub/.trae/audit/compile_evidence/**`（8 件） | 声明：8 件逐一 `moved to trash`（含 v1_62refs 子树）。 | **MISSING_TRUE**（8 路径三面均无）——与「已 trash」自洽，**属预期非异常** |
| D2 | `bg_0eeb9adf` | 09-21 19:16 | trash：`compile_evidence` v1_62refs 尾 + v2_overfull_fix + v2pre_h1h3（13 件） | 同上，13 件逐一 moved。 | **MISSING_TRUE**（预期） |
| D3 | `bg_d4ca1ccb` | 09-21 19:19 | trash：`deposon-sub/results/_archive_2026_09_20/` 26 件 .log | 26 件逐一 moved。 | **MISSING_TRUE**（预期） |
| D4 | `bg_ebdb2078` | 09-21 19:21 | trash：`_archive_2026_09_20/` 26 件（worker_b/c .log、gpt6_30cells_run.log 等） | 26 件逐一 moved。 | **MISSING_TRUE**（预期） |
| D5 | `bg_c314cf9a` | 09-21 19:24 | trash：`_p_l_v3_phase*` 26 件 log | 26 件逐一 moved。 | **MISSING_TRUE**（预期） |
| D6 | `bg_5ac13a91` | 09-21 19:26 | trash：`_p_l_v3_phase2_*` 26 件 log/err | 26 件逐一 moved。 | **MISSING_TRUE**（预期） |
| D7 | `bg_f654e2b0` | 09-21 19:29 | trash：`_sanity_*`/`_v3x_6way_*`/`_volc_22cap_emb.log` 等 26 件 | 26 件逐一 moved。⚠ 其中含 A1 件的 `_volc_22cap_emb.log` ⇒ 该日志的 MISSING_TRUE 由本棒 trash 解释 | **MISSING_TRUE**（预期） |
| D8 | `bg_b19a6526` | 09-21 19:48 | letters 迁移脚本 `_m6c_migrate_letters_2026_09_21.ps1` | 声明：REPO 620 件不变、SOURCES_OK=38、MOVE_DONE=1、ARC 64→33、HASH_VERIFY=PASS_38_38、MANIFEST_ENTRIES=63、MANIFEST_UPDATED=31。异常：脚本在 `:155` 抛 `FAIL reload not array` → **manifest 重写未完成即终止**。 | 脚本路径含 `:155` 行号，非文件 → **不可判**；见 D9 续跑 |
| D9 | `bg_dd568af3` | 09-21 19:55 | 同上脚本续跑（manifest 修复） | 声明：REBUILT_COUNT=63、RELOAD_ENTRIES=63、RELOAD_LETTERS_DST=31、DST_MISSING=0、DST_HASH_BAD=0、LETTERS_COUNT=38、ARC_COUNT=33、MANIFEST_SHA12=`33FE31633DA8`、**`ALL_CHECKS=PASS`**。 | manifest 现文件名不同（`_archive_manifest_*` 系列，最新 v3 = 09-28）⇒ D8 的中断**已被 D9 收口并被后续版本覆盖** |
| D10 | `bg_a013d8bc` | 09-21 20:01 | trash：`__pycache__`×4 + `docs/V3X/PHASE_B_TMP` | 声明 5 件 moved。 | 4/5 **MISSING_TRUE**（预期）；⚠ `deposon-repo/__pycache__` 与 `deposon_team/plugins/__pycache__` **现仍存在**（后续 Python 运行再生成，非 trash 失效） |
| D11 | `bg_2805a36d` | 09-21 20:07 | JSON 读档统计（同名异内容分类） | 异常：**命令本身 ParserError**（`$j` 变量在 `-Command` 内被吞，出现 `.B_same_name_diff_content` 空变量）→ 该棒**0 有效产出**。 | **不可判**（0 产出，不编造） |
| D12 | `bg_4f26cd53` | 09-21 20:09 | trash：主仓 19 个目录（`.trae/audit`、`.trae/deliverables`、`paper/deposon_arxiv_{cn,en}_pkg`、`results/_archive_2026_09_18` 等） | 声明：19 目录逐一 moved。异常：status=failed（内部报错 `/app.asar/node_modules/@mavis/local-runt…`），但 trash 主体动作**已执行**。 | 逐条实测：`figures`、`v3x-1week-kill-2026-09-18`、`.workbuddy`、`_d05_bg_21191cee_trash_2026_09_18`、`paper/deposon_arxiv_*`、`results/_archive_2026_09_18`、`_coze_paper_v1_review_2026_09_17` 等 **MISSING_TRUE（预期）**；`deposon_team/{products,verifier,_designs}`、`.trae/{audit,deliverables}`、`docs/FTFB_EXTERNAL_REVIEW_R2_2026_09_17` 等在 `deposon-sub` 或归档区 **OUTSIDE 存续** |
| D13 | `bg_5aee3983` | 09-18 21:27 | `Get-ChildItem results -File` 清点 | 异常：`Background bash failed: Parent-death guardian target registration timed out` → **0 产出**。 | **不可判** |
| D14 | `bg_df7601e7` | 09-18 10:42 | 沿 mavis-trash 删除 `bg_21191cee` 真产出 6 文件 | 声明：5 件 `✓ 移走`、1 件 `✗ 不存在`（`_d05_sanity_3backbone_20260918_100110.json`）；保留 KIMI 的 `_letter_to_glm_ftfb_deep_revision_2026_09_18.md`（24,857 B）；Trash `_d05_bg_21191cee_trash_2026_09_18`（5 件）；v0+v1 verify 复跑 0 触动。 | 5 件移走对象 **MISSING_TRUE（预期）**；保留件 `docs/V3X/P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md` **MATCH**（在盘，`2f0765a1d39d`／12,501 B——⚠ 棒方未给该件指纹，此为本次独立实测）；trash 目录 `〔幽灵引用·原件已缺席·未上传:_d05_bg_21191cee_trash_2026_09_18〕` 后续已由 D12 清理 ⇒ **MISSING_TRUE（预期）** |

### §2.5 组 E：subagent · lost（回执目录不存在，回执面不可恢复）——共 5 件

> lost 原因统一为 `Local runtime restarted before …`。目录均不在 `background-tasks\` 下 ⇒ **回执内容不可判**，仅可按任务名 + 盘上后续件定性。

| # | task_id | 结束 | 声明主题 | 后续件检索（三面文件名 + 内容面，41,467 件 / 41,193 文本件全扫） | 判定 |
|---|---|---|---|---|---|
| E1 | `bg_c7a12456` | 09-17 10:36 | P-L v2 真重测 | 未检出 `_p_l_v2*` 命名件；内容面命中 `docs/V3X/TRAE_PL_V2_EXPERIMENT_PROPOSAL_2026_09_17.md` 等 4 件（提案/汇总面），**无「真重测」结果面** | **回执不可判**；重测结论**疑似未收口**（0 证据可证） |
| E2 | `bg_bb13016d` | 09-26 16:18 | GLM_2 distill 侧 round1 | 未检出 `batch7_r5` 之外的 GLM_2 侧独立产物名；同族 r5 件在主仓 | **回执不可判**；与 A6（GLM_1 侧）成对，GLM_2 侧收官态**无回执可证** |
| E3 | `bg_7d7bd7e4` | 09-28 20:37 | Trae 六项存疑面逐项推真复核 | 命中 `results/_trae_sixitem_disposal_and_collision_register_2026_10_01.md`、`_deemphasis_verification_register_2026_10_08.md` | **回执不可判**；后续件在盘，疑已覆盖 |
| E4 | `bg_54bfc0c8` | 09-28 20:37 | #21 三腿真判（verdict-keeper 判定收口） | 命中 `letters/查理_deposon双主线论文终稿_2026-10-01_v0.3.md`、`results/_forgotten_recovery_register_2026_09_29.md` | **回执不可判**；后续件在盘，疑已覆盖 |
| E5 | `bg_67f321b2` | 09-28 20:37 | P 系落地立线包：端点归属定义提案＋KD 扩面＋v1-v1.4 生效补登 | 命中 `results/_v5_item26b_endpoint_definition_prereg_2026_09_28.md`、`_v5_item26b_attribution_effective_2026_09_28.md`、`_v5_c3_reading_b_prereg_2026_09_28.md` | **回执不可判**；立线包后续件在盘（与 C2 重派件一致），疑已覆盖 |

### §2.6 组 F：running（在跑，不判未收口）——共 2 件

| # | task_id | 结束 | 声明主题 | 状态说明 |
|---|---|---|---|---|
| F1 | `bg_61bb2040` | — | 清卡素材编译（候裁卷底稿） | running；回执目录尚未生成。**不判未收口**，待其结束后按同口径回捞 |
| F2 | `bg_b3bb81b8` | — | 未读后台回执全量回捞（EA）＝**本件自身** | running；本登记件即其产出 |

### §2.7 分组计数自证

| 组 | 定义 | 件数 |
|---|---|---|
| A | subagent · succeeded | 12 |
| B | subagent · canceled | 12 |
| C | subagent · failed | 4 |
| D | bash · succeeded / failed（清理迁移类） | 14 |
| E | subagent · lost | 5 |
| F | running | 2 |
| — | **合计** | **55** |

交叉校验：subagent 12+12+4+5+2 = **35**；bash = **14**；status 合计 succeeded 24（12+11+1 running 外无）+ canceled 15 / failed 9 / lost 5 / running 2 —— 与 §1.3 实测分布一致（bash 中 `bg_4f26cd53` failed、`bg_5aee3983` failed 计入 D 组；`bg_2805a36d` succeeded）。

---

## §3 汇总

### §3.1 明显未收口清单（建议 parent 核 / 裁）

| 序 | 项 | 关联件 | 性质 | 依据 |
|---|---|---|---|---|
| U1 | **E1 P-L v2 真重测**结论无回执、无可检出结果件 | `bg_c7a12456` | lost＋三面 0 命中 | §2.5 E1 |
| U2 | **B12 T1 预登记修订**（砍端点维度改 qwen 温扫）疑似未落件 | `bg_71d98eb6` | canceled 于 5%；未检出 `_t1_rev1*` 修订件 | §2.2 B12 |
| U3 | **A5 拉回清单 + 远端删除清单双清单**输出 0 字节、无落盘记录 | `bg_2d153d13` | status=succeeded 但 `output.log` 0 B、无 summary | §2.1 A5 |
| U4 | **A3 `bg_552544f7` succeeded 与回执内容不自洽**（回执止于「启动中 0%」，M1–M8 全未执行却判 succeeded） | `bg_552544f7` | 状态与内容矛盾，须 parent 判是否真跑完 | §2.1 A3 |
| U5 | **D11 `bg_2805a36d` 0 有效产出**（PowerShell ParserError，`$j` 变量被吞） | `bg_2805a36d` | 同名异内容统计未产出 | §2.4 D11 |
| U6 | **E2 GLM_2 distill 侧 round1** 收官态无回执可证（与 A6 GLM_1 侧成对） | `bg_bb13016d` | lost | §2.5 E2 |
| U7 | **A12 10 棵空目录树**仅列清单未处置（回填或删并待定） | `bg_a9111db0` | 棒方明示仅 `LIST_FILE_WRITTEN` | §2.1 A12 |
| U8 | **A7 锚件登记值落后盘上终态**（棒方记 `FCCFCC869E7A`／257,362 B；本次实测 `41f5f1689d09`／857,551 B） | `bg_73c9f9ec` | 属「登记≠盘上」族，需确认后续追加节次 | §2.1 A7 |
| U9 | **MISSING_TRUE 日志面 4 件**：`_volc_22cap_emb.log`、`deposon_volcengine_worker_c_2026_09_10.log`、`.run.log`、`_v4_supp_l14v3_batch7_r5_run.log` | A1／A2／A6 | 三面全遍历 0 命中（其中 `_volc_22cap_emb.log` 已由 D7 trash 解释；其余 3 件无 trash 记录） | §2.1 A1/A2/A6 |
| U10 | **A10 G4 闭环门未解除**：「仍需 runtime 打点 E1–E4」未闭；是否造受控复现待 PI 口径 | `bg_c6d03c39` | 棒方自陈 0 假闭环 | §2.1 A10 |
| U11 | **A8 T-1 §7.2 更正件 4 项待 PI**（生效即锁 / 十八行口径二择一 / 第 17 行归属 / 下游两件同步及权属） | `bg_b7755687` | 棒方明示待裁 | §2.1 A8 |

### §3.2 可忽略（纯日志 / 旧态已被后续覆盖 / 中断即终态）

| 类 | 件数 | 说明 |
|---|---|---|
| mavis-trash 清理作业（D1–D7、D10、D12、D14） | 11 | 声明即删除动作；`MISSING_TRUE` 是**动作已执行的自证**，非异常。删除对象多为 .log/.err/run.log 临时件 |
| 已被后续件实质覆盖 | 5 | B10（N-22s margin v2 → 归档区 executor/result/manifest 在盘）、B11（T1 补测 → 归档区 executor/verdict 在盘）、C2（重派 P 系 → `_v5_item26b_*` 在盘）、C4（V3 重开跑 → `_v5_v3_deg_p1_reopen_*` 在盘）、C3（V3 勘误 → reopen verdict r2 在盘） |
| lost 但后续件在盘 | 3 | E3（`_trae_sixitem_disposal_and_collision_register_2026_10_01.md`）、E4（双主线论文终稿 v0.3 + 09-29 回捞登记）、E5（`_v5_item26b_*` + `_v5_c3_reading_b_prereg`） |
| 中断即终态（早期 0–20% 探索棒，无交付承诺） | 4 | B1、B2、B3、B9（09-10～09-20 火山引擎/embedding 探路棒，均在 5–20% 阶段 aborted） |
| superseded manifest 修缮 | 1 | D8（`:155` FAIL）已被 D9 续跑 `ALL_CHECKS=PASS` 收口，且 manifest 后被 09-23/09-28 新版本覆盖 |
| `__pycache__` 再生 | 2 | D10 删除的 `__pycache__` 现又存在，属后续 Python 运行再生成，非 trash 失效 |
| 0 产出且已如实交代 | 2 | B8（PowerShell `$f` 歧义后中止，棒方自陈 0 产物）、D13（guardian 超时，0 产出） |

### §3.3 不确定需 parent 核（0 代裁，仅列问题）

| 序 | 问题 | 关联件 | 为何我不能判 |
|---|---|---|---|
| Q1 | A3 `bg_552544f7` 到底是否跑完？status=succeeded 但回执止于 0% 启动 | `bg_552544f7` | 状态字段与回执内容矛盾，需 parent 查该棒是否有第二段输出或后续棒承接 |
| Q2 | B12 T1 预登记修订（`802DECE2286A`）是否已在其他件内以不同名完成？ | `bg_71d98eb6` | 三面文件名 + 内容面均未检出明确对应修订件；可能并入他件但无法确证 |
| Q3 | A5 双清单是否确已生成但落在别处？ | `bg_2d153d13` | `output.log` 0 字节、无 summary，无任何路径线索；按「0 产物不编造」不推定 |
| Q4 | E1 P-L v2 真重测是否另有落盘面（如仓外目录未纳入本次三面）？ | `bg_c7a12456` | 本次仅覆盖 repo／deposon-sub／〔归档区〕 三面；更外层面未授权扫描 |
| Q5 | A7 锚件 v20→当前之间追加了多少节次、是否需在勘误链补版本记录？ | `bg_73c9f9ec` | 属实验结论/勘误链本体（verdict-keeper + PI 口径），审计 ≠ 翻案，只登记差异 |
| Q6 | 55 件中含本件与另 1 件并行 EA 回捞（F1/F2），是否需合并登记避免重复计数？ | F1／F2 | 登记合并口径属 parent 决策 |

---

## §4 边界与如实交代

### §4.1 0 触动自证

本件为纯新增登记，0 写入任何既有件、0 移动/删除/改名。落盘前后对代表性锚件做实测对照：

| 锚件 | 落盘前 SHA-12 / 字节 | 落盘后（见 §5） | 判定 |
|---|---|---|---|
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | `41f5f1689d09` / 857,551 | 同值 | 0 触动 |
| `docs/V3X/P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md` | `2f0765a1d39d` / 12,501 | 同值 | 0 触动 |
| `results/_v4_supp_l14v3_batch7_r5_result.json` | `09a481ebca6b` / 61,658 | 同值 | 0 触动 |
| `results/_v4_supp_l14v3_batch7_r5_executor.py` | `38710a448e9c` / 53,155 | 同值 | 0 触动 |
| `letters/TRAE_V3_REVIEW_LETTER_2026_09_23.md` | `0e7600ac4478` / 7,510 | 同值 | 0 触动 |

触动数 = **0**。

### §4.2 落盘自证（撞名实测 + 版式）

- 撞名实测：`results/_forgotten_recovery_register_2026_10_08.md` 落盘前 `exists=False`；`results/` 下相似名仅 1 件 `_forgotten_recovery_register_2026_09_29.md`（历史件，**未触碰**）⇒ 新名可用、无覆盖。
- 版式：UTF-8 **无 BOM**、**纯 LF**（CR=0）；命名不含 `_v3_`/`_v4_`/`_v5_` 阶段前缀（合规于 PI 2026-09-29 命名裁）。
- 本件只读源：sqlite 以 `?mode=ro` 打开（⛔ 0 触发 WAL checkpoint）；`background-tasks\` 全程只读。

### §4.3 key 形态自扫（R4）

对 55 件回执全文（`summary.txt` 优先，缺则 `output.log`）执行 `\b` 词边界扫描：

| 形态 | 命中数 | 处置 |
|---|---|---|
| `\bsk-[A-Za-z0-9_-]{8,}` | 0 | — |
| `\btp-[A-Za-z0-9_-]{8,}` | 0 | — |
| `\bark-[A-Za-z0-9_-]{8,}` | **10** | **0 摘录 / 0 落盘 / 0 入件**（仅记存在性） |
| `\bAPI_KEY\s*=` | **2** | **0 摘录 / 0 落盘 / 0 入件**（仅记存在性） |
| `Authorization:\s*Bearer\s+\S+` | 0 | — |

⇒ 本件 **CLEAN**：未摘录、未复制、未改写任何凭据明文；上表仅记计数与形态。本件自身落盘后再扫 `sk-`/`tp-`/`ark-`/`API_KEY=`/`Bearer` 均为 0 命中（唯一 `ark-` 字样出现在 §4.3 表内的**形态名**中，非凭据值）。

### §4.4 测量仪器自审（诚实交代误差源）

1. **路径提取为正则近似**：从回执文本抽 `[A-Za-z]:[\\/]...` 与 `results/…` 相对路径，个别路径带尾随符号（如 `` ` ``、`;`）已清洗，但**可能漏抽**以裸文件名（无目录前缀）形式出现的产物。此偏差方向为**低估 MISSING 率 / 高估不可判率**。
2. **`MISSING_TRUE` 的强度**：均由三面（repo 1,719 件／sub 503 件／归档区 39,244 件，合计 41,467 件）**完整遍历**后的精确文件名 0 命中得出，非抽样。三面之外的目录（如 `Deposon_v1_2_0_交付包`、`〔本地绝对路径·脱敏略:agents〕\`）**未纳入**——故 `MISSING_TRUE` 的准确表述是「本件三面内确无」，跨全盘存在性的更强断言未作。
3. **负结论二次确认**：3 个关键日志（`_volc_22cap_emb.log`、worker_c 两 .log）除首轮索引外，另做一次无早停的独立全遍历复核，两轮一致。
4. **A7 登记值差异未归因**：棒方 `FCCFCC869E7A`／257,362 B 与实测 `41f5f1689d09`／857,551 B 的差异，本件只**登记不解释**（可能为 v20→v21→后续多轮追加）。判定权属：勘误链本体属 verdict-keeper，审计 ≠ 翻案。
5. **`bg_4f26cd53` status=failed 但动作已执行**：其 trash 主体动作在失败前已完成（回执逐行 `moved to trash` 有据）。本件按「动作已发生」定性为可忽略，同时保留 failed 状态原样登记，未替其改判。
6. **running 2 件未纳入未收口判定**：F1／F2 目录尚未生成，无回执可读；提前判定会构成「succeeded ≠ 跑完」同族的误判。
7. **同一性提示**：`_inspect_captions.py` 在三面 3 处存在且哈希全同（`dfb02ade1474`）＝ SAME_IDENTITY，**计 1 件不重复计数**；D1–D7／D10／D12／D14 的 `MISSING_TRUE` 路径互不重叠，无重复计数。

### §4.5 本件不做的事

- 不判任何实验结论对错（属 verdict-keeper）
- 不改 frozen 内任何件、不回改历史实录行
- 不替 parent 处置 §3.1 的 11 项未收口（可解决项由 parent 派棒，决策项由 PI 拍板）
- 不扫三面之外的目录、不发起网络请求

---

## §5 产出物登记

| 项 | 值 |
|---|---|
| 路径 | `_repo_mirror/verdict/pi/_forgotten_recovery_register_2026_10_08.md` |
| SHA-256[:12] | 填入前实测 `fc94788390fe`（**自指约定**：本字段填入即改变文件哈希，故此处只记「填入前」值；填入后的终值以交付回报所载为准） |
| 字节 | 填入前实测 **33,809 B**（同自指约定；填入后终值见交付回报） |
| 落盘后实测（版式） | UTF-8 无 BOM（`BOM=False`）／CR=0／LF=261（**纯 LF**） |
| 落盘后实测（key 自扫） | `sk-`=0／`tp-`=0／`ark-`=0／`API_KEY=`=1（**形态名字面**，`API_KEY\s*=\s*\S+` 赋值式扫描 0 命中，无凭据值）／`Bearer`=0 ⇒ **CLEAN** |
| 编码/行尾 | UTF-8 无 BOM ／ 纯 LF |
| 新增件数 | 1（仅本件；0 回改既有件、0 网络、0 代裁） |
| 出证 | evidence-auditor · 2026-10-08 · 未读后台回执全量回捞（回执面） |
