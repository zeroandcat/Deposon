# V3-N #32 CPATH 理论模拟 **实测**（30-cell with-RAG 补跑完成）

**日期**：2026-10-01
**出件方**：Mavis 团队 worker（agent: worker）—— 本件由 worker 出件，署名如实
**补跑依据**：T1 ark key 恢复（runtime env `ARK_API_KEY` 存在性已核）＋ T2 配额重置点 `2026-09-30 23:59:59 +0800` 已过 ＋ T3 PI 放行（排期 v4 T1-5「#32 补跑」＋本晨开工批）
**本件只作补跑实测登记**：`results/_v3_n_recheck_llm_verdict_2026_09_27.md`（`426cfe18cf65`）**0 触动**；`docs/V3X/CPATH_SIMULATION_REPORT_2026_09_10.md`（`de772cd9e7ba`）**0 触动**

---

## §1 输入链核验（先核后动，本棒盘上实测）

| 件 | 路径 | SHA-12 | 字节 | 与派工/源件自记 |
|---|---|---|---|---|
| 上游 runner | `deposon_team/plugins/_v3n_cpath_live_2026_09_27.py` | `5248ba7ac21c` | 19,823 | ✅ 一致 |
| #32 判定件 | `results/_v3_n_recheck_llm_verdict_2026_09_27.md` | `426cfe18cf65` | 21,332 | ✅ 一致 |
| prep 件 | `results/_external_pat_ark_prep_2026_09_30.md` | `ca540e5cab23` | 14,055 | 本棒实测 |
| #32 既有数据件（只读） | `results/_v3_n_cpath_live_data_2026_09_27.json` | `25374af92f88` | 12,711 | ✅ 一致 |
| baseline（no-RAG） | `results/deposon_volcengine_glm_latest_30cells_v2_2026_09_10.json` | `4ec04d3d7d8c` | 32,995 | ✅ 一致 |
| 设计字面源 | `docs/V3X/CPATH_SIMULATION_REPORT_2026_09_10.md` | `de772cd9e7ba` | 6,825 | ✅ 一致 |
| 22caption 元件（runner 需） | `results/deposon_volcengine_22caption_embedding_2026_09_10.json` | `c4b774c8e34c` | 4,559 | runner 引用件 |
| caption 原文（runner 需） | `corpus/v20/strip_captions_22.json` | `6a2656878745` | 12,798 | runner 引用件 |
| corpus 索引（runner 需） | `corpus/v20/index.json` | `8423ffe266af` | 7,335 | runner 引用件 |

**前置结构自检（0 LLM）**：baseline 30 cells 的 `prompt` 恰为 2 行（`Question: …` ／ `Answer in one number:…`）⇒ runner 的 `lines[0] + Context + lines[-1]` 拼接面成立；`svd2_coords` 覆盖 strip 22/22 ids，无缺项。

**本次产物（新名，既有件 0 覆写）**：

| 件 | 路径 | SHA-12 | 字节 | 编码 |
|---|---|---|---|---|
| 补跑 runner 副本 | `deposon_team/plugins/_v3n_cpath_live_rerun_2026_10_01.py` | `3e932a5409b5` | 20,831 | UTF-8 无 BOM |
| 补跑数据件 | `results/_v3n_cpath_live_rerun_2026_10_01.json` | `7c26d08ece3b` | 60,012 | UTF-8 无 BOM |
| 本判定件 | `results/_v3n_cpath_live_rerun_verdict_2026_10_01.md` | 不自指（见回执行实测登记） | — | UTF-8 无 BOM·LF |

- 补跑 runner 副本对上游 runner 的改动面 **仅 4 处**（`unified_diff` 20 行，已逐行核）：① 模块名 ② `OUT_JSON` 改新名（上游指向既有件 `25374af92f88`，直接跑会覆写）③ `date` 改 2026-10-01 ④ 增 4 行补跑溯源字段（`rerun_of`/`rerun_trigger`/`rerun_extractor_open_face`/`rerun_prior_state`/`rerun_no_overwrite`）。**调用/判分/检索逻辑 0 改动**。
- 判定带 0 新设：仅沿 `de772cd9e7ba` §5 字面 **0% ~ +26.7%**（该件 §5 原文行已核：「C 路径 RAG 理论边际 **0% ~ +26.7%**（完美 oracle 边界）」）。
- 端点/模型 0 新设：chat `ark.cn-beijing.volces.com/api/coding/v3` ＋ `glm-latest`；emb `…/v3/embeddings` ＋ `doubao-embedding-vision-251215`（逐字沿 baseline/上游 runner）。
- 行尾惯例说明：数据件为 **CRLF**。本棒实测 `results/` 下 3/3 JSON 数据件（含 baseline、`25374af92f88`、本件）皆纯 CRLF（Python Windows `open` 默认），故 0 人为归一；本判定件按 md 惯例（320/325 为 LF）写 LF。

---

## §2 实测执行（API 调用总账，0 掩饰）

| 项 | 结果 |
|---|---|
| 状态 | **COMPLETED**（`outcome.status`），耗时 **111.5 s** |
| embedding 调用 | **6 次**（批次 items = 10,10,2,10,10,10 ⇒ 22 caption ＋ 30 question = 52 条，分 6 批，与 `EMB_BATCH=10` 一致） |
| chat 调用 | **30 次**（30 cells，串行，间隔 ≥ 2.5 s 强制） |
| **调用总账** | **36 次，全部 HTTP 200；失败 0；重试 0**（`attempt>1` 记录为空；无 429、无 `AccountQuotaExceeded`） |
| 端点外联 | **0**：仅既有 ark 两个端点（chat base ＋ embeddings），无第三方/代理/其他外联 |
| 网络面 | 仅上述 36 次 POST；0 预探（即用即探） |
| key 纪律（R4） | key **仅 runtime 从 env `ARK_API_KEY` 读入内存**；**0 打印、0 落盘、0 入 JSON、0 入 log、0 入 prompt**。自证：以运行时 env 值对落盘 JSON 全文字符串比对 ⇒ `KEY_IN_OUTPUT = False`（自检脚本只输出布尔，不输出 key 本身） |
| token 用量 | `total_tokens` 合计 **26,954**（其中 2 条空答各耗 1,141 / 1,166，见 §6-2） |
| 单条延迟 | 1,516.7 ms ~ 8,400.6 ms |
| 既有凭证 | `ARK_PLAN_LATEST_API_KEY`（root 预核仍 401）**0 重试、0 使用** |

---

## §3 读数结果（30-cell 全体，分母齐）

| 侧 | 口径 | 答对 | 率 | gsm8k | strategyqa |
|---|---|---|---|---|---|
| no-RAG（**同抽取器重判**） | 上游 runner 声明抽取器，对 baseline 已存 30 条 `response_text` 重判 | **24/30** | **80.0%** | 15/15 | 9/15 |
| no-RAG（stored 原值） | baseline 件原抽取器产出之 `is_correct`（抽取器本体未落盘） | 22/30 | 73.3% | 13/15 | 9/15 |
| **with-RAG（本次实测）** | 同一抽取器，30 cells 带 top-3 caption context | **25/30** | **83.3%** | **15/15** | **10/15** |

**实测边际**：

- **对同抽取器 no-RAG（24/30 = 80.0%，RAG 效应隔离口径）**：**+1 cell ＝ +3.3 pp** ⇒ 落在原报告带 **0% ~ +26.7%** 内 ⇒ runner 字面判定「**成立**」。
- 对 stored 原值（22/30 = 73.3%）：**+3 cells ＝ +10.0 pp** ⇒ 亦落在带内（此对比受 §6-1 抽取器口径未决影响，**0 新设判据、仅如实附记**）。

**唯一翻转**：第 30 条（strategyqa id=15）`no-RAG(重判)=False → with-RAG=True`（抽取 `Yes`，期望 `Yes`）。其余 29 条与同抽取器 no-RAG 判定一致。`margin_in_band = true`（数据件 `verdict` 字段原样落盘）。

**检索面（top-3，cos）**：top-3 余弦 min/均值/max = **0.0666 / 0.1469 / 0.2994**；30 cells 共取用 **21/22** 条不同 caption（1 条未被 top-3 命中）。`avg_top3_T_frac_mean = -0.8219`（口径见 §6-3）。

---

## §4 逐 cell 对照表（30 行，实测原样）

`stored`＝baseline 原判定；`重判`＝同抽取器重判 no-RAG；`RAG`＝本次 with-RAG 判定；`抽取/期望`＝with-RAG 侧抽取值；`top3`＝注入 context 的三条 caption id。

| # | bench | id | stored | 重判 | RAG | 抽取 | 期望 | top-3 caption | max cos |
|---|---|---|---|---|---|---|---|---|---|
| 1 | gsm8k | 1 | ✗ | ✓ | ✓ | 18.0 | 18.0 | L_algorithm_process, L_historical_causality, S2_n35 | 0.1554 |
| 2 | gsm8k | 2 | ✓ | ✓ | ✓ | 5.0 | 5.0 | S6_n60, S1_n45, S4 | 0.1484 |
| 3 | gsm8k | 3 | ✓ | ✓ | ✓ | 40.0 | 40.0 | S6_n60, S6_n35, S3 | 0.2259 |
| 4 | gsm8k | 4 | ✓ | ✓ | ✓ | 1430.0 | 1430.0 | L_project_management, L_algorithm_process, S1 | 0.1165 |
| 5 | gsm8k | 5 | ✓ | ✓ | ✓ | 36.0 | 36.0 | L_project_management, L_algorithm_process, S1_n35 | 0.0875 |
| 6 | gsm8k | 6 | ✗ | ✓ | ✓ | 8000.0 | 8000.0 | L_physics_concepts, S2_n35, S1 | 0.1275 |
| 7 | gsm8k | 7 | ✓ | ✓ | ✓ | 36.0 | 36.0 | L_physics_concepts, L_biological_taxonomy, S1_n35 | 0.1762 |
| 8 | gsm8k | 8 | ✓ | ✓ | ✓ | 6.0 | 6.0 | S6_n60, S1_n60, S1_n35 | 0.2125 |
| 9 | gsm8k | 9 | ✓ | ✓ | ✓ | 40.0 | 40.0 | S3, S2_n20, L_physics_concepts | 0.1781 |
| 10 | gsm8k | 10 | ✓ | ✓ | ✓ | 140.0 | 140.0 | S1_n35, L_algorithm_process, L_physics_concepts | 0.0990 |
| 11 | gsm8k | 11 | ✓ | ✓ | ✓ | 2125.0 | 2125.0 | S3, S1_n35, L_physics_concepts | 0.1226 |
| 12 | gsm8k | 12 | ✓ | ✓ | ✓ | 32.0 | 32.0 | S6_n20, S2_n35, S1_n35 | 0.1566 |
| 13 | gsm8k | 13 | ✓ | ✓ | ✓ | 50.0 | 50.0 | S1_n35, L_geography_world, S5 | 0.1653 |
| 14 | gsm8k | 14 | ✓ | ✓ | ✓ | 122.0 | 122.0 | S1_n35, L_biological_taxonomy, S1_n45 | 0.1747 |
| 15 | gsm8k | 15 | ✓ | ✓ | ✓ | 34.0 | 34.0 | S3, L_algorithm_process, S2_n20 | 0.1359 |
| 16 | strategyqa | 1 | ✓ | ✓ | ✓ | Yes | Yes | L_historical_causality, S5, S2_n35 | 0.1505 |
| 17 | strategyqa | 2 | ✓ | ✓ | ✓ | No | No | L_geography_world, L_biological_taxonomy, L_project_management | 0.1119 |
| 18 | strategyqa | 3 | ✓ | ✓ | ✓ | Yes | Yes | L_historical_causality, S6_n20, L_physics_concepts | 0.1847 |
| 19 | strategyqa | 4 | ✓ | ✓ | ✓ | No | No | L_project_management, S1_n35, L_algorithm_process | 0.1458 |
| 20 | strategyqa | 5 | ✗ | ✗ | ✗ | No | Yes | L_geography_world, S5, S3 | 0.1608 |
| 21 | strategyqa | 6 | ✓ | ✓ | ✓ | No | No | L_geography_world, S2, S2_n60 | 0.1198 |
| 22 | strategyqa | 7 | ✗ | ✗ | ✗ | Yes | No | L_biological_taxonomy, L_physics_concepts, S3 | 0.1645 |
| 23 | strategyqa | 8 | ✓ | ✓ | ✓ | No | No | L_biological_taxonomy, L_historical_causality, L_physics_concepts | 0.1747 |
| 24 | strategyqa | 9 | ✗ | ✗ | ✗ | **None** | Yes | L_geography_world, L_project_management, L_algorithm_process | 0.1186 |
| 25 | strategyqa | 10 | ✗ | ✗ | ✗ | **None** | No | L_physics_concepts, S1_n35, S5 | 0.1646 |
| 26 | strategyqa | 11 | ✓ | ✓ | ✓ | No | No | L_historical_causality, L_geography_world, L_biological_taxonomy | 0.0895 |
| 27 | strategyqa | 12 | ✓ | ✓ | ✓ | No | No | L_biological_taxonomy, S1_n35, S2 | 0.2128 |
| 28 | strategyqa | 13 | ✓ | ✓ | ✓ | Yes | Yes | L_geography_world, L_biological_taxonomy, S1_n35 | 0.1444 |
| 29 | strategyqa | 14 | ✗ | ✗ | ✗ | No | Yes | S6_n60, S1_n35, S6 | 0.2994 |
| 30 | strategyqa | 15 | ✗ | ✗ | **✓** | Yes | Yes | L_geography_world, S1_n35, S6_n60 | 0.2521 |

`✗/✓`＝是否答对。gsm8k 15 条本次全对（与同抽取器重判一致）；strategyqa 10/15（唯一新增正确为 id=15）。

---

## §5 判定带核对（0 新设阈值）

| 项 | 值 | 出处 |
|---|---|---|
| 理论边际带 | **0% ~ +26.7%** | `de772cd9e7ba` §5 原文（已核行） |
| 实测边际（对同抽取器 no-RAG） | **+3.3 pp** | 本次实测 |
| 是否在带内 | **是** | 数据件 `verdict.margin_in_band = true` |
| runner 字面判定 | **成立（实测边际落在原报告 0% ~ +26.7% 带内）** | 数据件 `verdict.verdict_literal` 原样落盘 |
| 本棒新增阈值 | **0** | 判据面未触碰 |

**与「未决」面关系（0 改既有件）**：`426cfe18cf65` §2.3 记 #32「未决（端点配额阻断）」。本件为**补跑实测登记**，不回头改写该件 §2/§8；#32 状态由「未决」转「实测已出读数」的事实记于本件，更新既有判定件属另棒/PI 裁范围。

---

## §6 口径面如实登记（0 新设 / 0 代裁；存疑处标「待 PI」）

**6-1｜抽取器口径未决（承 `426cfe18cf65` §8-2，仍未裁）** —「**待 PI**」
- 既有差异原样复现：stored **22/30** vs 同抽取器重判 **24/30**，差额 **−2** 仍全落 gsm8k（13/15 → 15/15），strategyqa 两侧同为 9/15。根因仍是 baseline 只落盘抽取结果、**抽取器本体未落盘**。
- 本次处置：**以 runner 现字面执行并如实登记**（用声明抽取器同时判 no-RAG 与 with-RAG，以隔离 RAG 效应）。**0 新设抽取器、0 代 PI 裁定采用哪一口径**。
- 读数因此给两个口径：+3.3 pp（对 24/30）与 +10.0 pp（对 22/30），**两者均在 0%~+26.7% 带内**；但「以哪一口径为 #32 正式答对率」**待 PI**（§8-2 未闭）。

**6-2｜2/30 条空 response（模型侧推理预算耗尽）—「待 PI」**
- strategyqa id=9、id=10 的 `response_text` 为**空串**（长度 0），抽取得 `None`，按现字面计**错**。
- 二者 `usage` 均为 `completion_tokens=512`（＝`max_tokens` 上限）且 `reasoning_tokens=512`、`prompt_tokens` 629/654 ⇒ **全部预算被 reasoning 占用、未产出可见答案**，属端点/模型侧生成行为，**非已观测到的答错内容**。
- 处置：**如实登记事实，0 外推、0 改判、0 重跑**（重跑＝新增调用与新增口径，超本棒范围）。是否将「空 response」另立处理口径（例如计为不可用而非答错、或放宽 `max_tokens` 重测）**待 PI**；在此之前 25/30 为现字面读数。
- 影响面提示（如实）：若这 2 条实为答错，则边际不变（两侧同错）；若实为答对，则 RAG 侧上界可能更高 —— **本棒不据此改判**。

**6-3｜`svd2` PC1 符号口径（runner 现字面 vs 报告 §2）—「待 PI」**
- 上游 runner `top3_T_frac_mean` 直接取 `svd2_coords[id][0]`；本棒实测该 22 条 PC1 坐标**全部为负**（min −0.9212 / max −0.5211 / mean −0.8181），故落盘 `avg_top3_T_frac_mean = -0.8219`。
- 报告 `de772cd9e7ba` §2 的「T（透射）占比」列全为**正**（0.423 ~ 0.996），即该报告取值带了绝对值/反号约定。
- 处置：**以 runner 现字面执行并如实登记**（0 新设符号约定、0 代裁）。该字段**不参与**答对率与边际判定（仅检索面描述量），故对 §3 读数无影响；符号口径统一**待 PI**。

---

## §7 0 触自证

| 纪律 | 自证 |
|---|---|
| R4（key） | key 仅 runtime env 读入内存；落盘 JSON 全文字符串比对 `KEY_IN_OUTPUT = False`；stdout 全程 0 打印 key；0 入 prompt/JSON/log |
| 0 编造 | 全部 SHA-12/字节/读数/token/延迟/余弦均为本棒盘上实测或数据件原样落盘；未实测项已列 §6 与 §8，0 猜测 |
| 0 改既有件 | `25374af92f88`（#32 数据件）、`426cfe18cf65`（#32 判定件）、`de772cd9e7ba`（报告）、`4ec04d3d7d8c`（baseline）、`5248ba7ac21c`（上游 runner）**均 0 写入**；新名输出 2 件（runner 副本 ＋ 数据件）＋本判定件 |
| 0 新设阈值 | 判定带仅用 `de772cd9e7ba` §5 字面 0%~+26.7%；抽取器/符号/空 response 三面均按现字面并标「待 PI」 |
| 网络面 | 仅既有 ark chat ＋ embeddings 两端点，共 36 次 POST；0 预探、0 第三方、0 代理；401 凭证 `ARK_PLAN_LATEST_API_KEY` 0 重试 0 使用 |
| 编码 | 本判定件 UTF-8 无 BOM·LF；数据件 UTF-8 无 BOM·CRLF（与 `results/` 3/3 JSON 惯例一致，见 §1） |
| 署名如实 | 本件与补跑数据件署名 worker（agent: worker）；引用件（上游 runner/#32 判定件/09-10 报告/baseline）仅作引用，未以其名义出证 |
| 如实交代 | 未核对 2 条空 response 的 `finish_reason`（端点未随响应返回该字段，0 推断）；未单独计价（端点响应无计价字段，源件字面「~0.05 USD」未复算） |

---

## §8 老实交代（未核项 / 存疑，0 猜测）

1. **抽取器本体仍未定位**：baseline 只落盘抽取结果；本棒**0 猜测**抽取器实现，0 定位、0 重写（§6-1）。
2. **2 条空 response 的上游成因未定位**：`finish_reason` 端点未返回；仅据 `usage`（`reasoning_tokens` 占满 `max_tokens`）作**事实陈述**，成因 0 断言（§6-2）。
3. **`svd2` 符号口径未统一**：报告 §2 与 runner 现字面差一个符号约定；0 判定哪侧为准（§6-3）。
4. **T3「PI 已放行」的盘上字面**：本棒可核到 `README_V4_2026_09_29.md` §0「**#32 补跑**（如依赖方舟）」＋ `ca540e5cab23` §3.1（T1/T2/T3 三条件）与 `_forgotten_recovery_register_2026_09_29.md` E7「#32 补跑 ＋ D8 问卷 80 题」；**T3 的放行动作本体来自本晨开工批/排期 v4 T1-5（排期件本身未在本次输入清单内，0 猜测其路径与指纹）**。
5. **`#32` 在既有判定件中的状态字段未更新**：`426cfe18cf65` §2.3 仍记「未决」；本件不改该件（0 改既有件），状态更新落点**待 PI 指定**。
6. **成本未复算**：源件字面「~0.05 USD」为 09-10 理论模拟的设计估值；本次实测 0 取计价数据（端点响应无计价字段），0 复述该估值当本次成本。

---

**本件实测 SHA-12 / 字节**：由本次补跑回执行 `Get-FileHash` 实测登记（不自指本行；避免自引用哈希）
**出件**：Mavis 团队 worker（agent: worker）｜2026-10-01
**署名如实**：本件由 worker 出件；所引上游 runner / #32 判定件 / 09-10 报告 / baseline / prep 件均为原始出证方，本件只作引用与实测登记。
