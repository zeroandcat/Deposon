# F4 · `alt_reading_corr_excluded` 口径补定义（反推 + 复现 + 证伪台）

**件名**：`results/_v4_pi_cot_v3_alt_reading_definition_2026_09_27.md`
**关联**：`results/_v4_pi_cot_v3_result_v3.json`（`585714f9660c` / 27,203 B）§`alt_reading_corr_excluded`
**登记面**：`docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` §22.31.4 E-42.4 F4 alt_reading 未决（中 · 未决项）
**结论**：**可反推**（非「不可反推」）—— 口径已定位到具体代码行，且已独立复现 result_v3 的 8 个 alt 字段逐字相同。

---

## §1 结论一句话

> `alt_reading_corr_excluded` = **同一 substrate（77 件）+ 同一 seed=42 划分**下，取主读法 `held_out` 23 件中的**非 correction 事件子集（18 件）**作为新 held 集，然后**整条 metrics 管线重跑**（决策树在剩余 **59** 件上**重新训练**，再对 18 件算 NW-sim / NLED-sim / divergent / critical / bootstrap）。
> **它不是**「把主读法 23 条 `per_event` 抽掉 5 条 correction 后重算」。

**7 种自然读法复现失败的根因就在这一句**：主读法训练面 = 77 − 23 = **54** 件，替读法训练面 = 77 − 18 = **59** 件。被剔掉的 5 件 correction 事件**不是被丢弃，而是被放回训练集重训了树** → 18 件的 `pred` 全部可能改变 → `divergent` / `actual` / `nw_sim` / `nled_sim` / `blind_obey_rate` / `bootstrap_ci` 全部随之改变。只做「抽掉 5 条」而不重训的读法，数学上不可能复现这组数字。

---

## §2 确切定义（可据以重写的口径规格）

| 步 | 动作 | 代码（母件行号） |
|---|---|---|
| 1 | substrate 全量载入 77 件 | `executor.load_all_events_v3()` |
| 2 | 分层留出 0.30 → `held_idx`（23 件，含 correction 分层） | `executor.stratified_holdout_split_v3(events, 0.30, RandomState(42))` |
| 3 | 剔 correction：`held_idx_nocorr = [i for i in held_idx if not is_correction_event_v3(events[i])]` → **18 件** | `_run_final.py:142` |
| 4 | **整链重跑** `compute_metrics_v3(events, held_idx_nocorr)` | `_run_final.py:143` |
| 4a | └ 训练面重算：`tr = 全部 77 件 minus 新 held 18 件` = **59 件** → `build_tree` 重训 | `executor:1121-1123` |
| 4b | └ 对 18 件逐件 `predict_tree` → `nw_sim` / `nled_sim` / `divergent = pred not in seq` / `has_critical_reflection` | `executor:1133-1146` |
| 4c | └ `n_divergent` / `n_critical_among_divergent` / `div_critical_coverage` / `n_agree` / `n_blind_obey` / `blind_obey_rate` 重算 | `executor:1151-1159` |
| 4d | └ `bootstrap_ci_v3(per_event_nw, RandomState(SEED+13), 1000)` 重抽 | `executor:1164-1166` |
| 5 | 只落 7 个 metric 字段（**不落 per_event**） | `_run_final.py:257-266` |

**correction 判据（`is_correction_event_v3`，`executor:716-729`）** = 以下任一为真：
1. `ev["is_correction"]` 是字符串且以 `_pair_pending` 结尾 **或** 等于 `"R_pair"`；
2. `ev.get("read_flip") is True`；
3. `ev.get("event_type") == "pi_disposition"`。

**目标签名（result_v3 §alt 字面，本棒独立复现逐字相同）**：

```
held_out_count                = 18
nw_sim_mean                   = 0.5126984126984128
nled_sim_mean                 = 0.2962962962962963
n_divergent                   = 11
n_critical_among_divergent    = 4
div_critical_coverage         = 0.36363636363636365
blind_obey_rate               = 0.2857142857142857
bootstrap_ci                  = [0.3722222222222222, 0.6611111111111111]
```

---

## §3 代码路径（文件:行）

| 角色 | 路径 | SHA-12 | 字节 |
|---|---|---|---|
| 出件 runner（口径真源） | `.tmp/_run_final.py` | `75d466add5d5` | 26,654 |
| 口径宿主 executor（母件） | `results/_v4_pi_cot_v3_ruleset_v3_executor.py` | `8a81d90c69ba` | 58,794 |
| 口径宿主 executor（r1 修正版） | `results/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py` | `ee8671a28c2f` | 62,115 |
| 复现 runner（本棒） | `.tmp/_run_recheck_r1.py` | `a76ec3a2340e` | 34,895 |
| 复核出件（数据面） | `results/_v4_pi_cot_v3_k3b_recheck_r1_2026_09_27.json` | `cbc14a76f038` | 26,891 |

逐行锚点：

- `.tmp/_run_final.py:122-123` 主读法划分
- `.tmp/_run_final.py:130` 主读法 `compute_metrics_v3(events, held_idx)`
- `.tmp/_run_final.py:142` `held_idx_nocorr`（剔 correction）
- `.tmp/_run_final.py:143` `alt_metrics = compute_metrics_v3(events, held_idx_nocorr)` ← **口径的决定性两行**
- `.tmp/_run_final.py:257-266` alt 落盘字段（7 项）
- `results/_v4_pi_cot_v3_ruleset_v3_executor.py:1121-1123` 训练面 = 全部事件 minus held（**重训发生处**）
- `results/_v4_pi_cot_v3_ruleset_v3_executor.py:716-729` `is_correction_event_v3` 判据
- `results/_v4_pi_cot_v3_ruleset_v3_executor.py:1108-1197` `compute_metrics_v3` 全链

---

## §4 复现步骤

```powershell
cd 'D:/私人资料/deposon-repo'
$env:PYTHONIOENCODING='utf-8'
python .tmp/_run_recheck_r1.py
```

预期（实测 `True` / `True` / `True`）：

```
母件复现自校验 17 项全部逐字相同 : True     ← main 10 项 + alt 7 项 vs 盘上 result_v3.json
held 集 母件==r1                : True
```

**第 1 条是 F4 的验收线**：它用盘上 `result_v3.json` 当靶子，母件跑出的 17 个数字（主读法 10 + 替读法 7）必须逐字相同。相同 ⇒ 本棒 runner 与棒 C runner 同口径，§2 定义即真义。

**第 2 条**证明 F1 修复只动文本装载，不动划分：r1 与母件 `held_idx` 逐件相同（`is_correction` 判据不读 `reasoning_full`，故不受 F1 影响）。

**幂等性**（重跑逐字不变）：同一 runner 连跑两次，出件 JSON 的 SHA-12 相同 —— 实测 `runC = runD = cbc14a76f038`（seed=42 贯穿划分 / 排列检验 / bootstrap 三处随机源）。

---

## §5 候选台（8 读法证伪表）

「held 集同 P0」列 = 该读法的 held 集与 P0 逐件相同（是 P0 的同义改写，**不算独立复现**）。

| # | 读法 | held 集同 P0 | 复现 result_v3 alt 8 字段 | 差在哪 |
|---|---|---|---|---|
| **P0** | **剔 correction → 整链重跑（含重训）** ← 真义 | ✅ | ✅ **复现** | — |
| P1 | 主读法 23 条 `per_event` 抽掉 5 条后重算（不重训） | ✅ | ❌ | 树未重训，`pred` 保持主读法值 |
| P2 | substrate 层先剔 correction → 0.30 重划 + 重训 | ❌ | ❌ | held 集变成另一组（剔后 61 件重划） |
| P3 | correction 判据收窄为 `is_correction == "R_pair"` | ✅ | ✅ 数字复现（**退化等效**） | held 集与 P0 逐件相同 → P0 的同义改写，**非独立读法** |
| P4 | 换 held 集（18 件）但沿用主读法那棵树（不重训） | ✅ | ❌ | 树未重训 |
| P5 | held = 全部非 correction 事件（61 件，非 18） | ❌ | ❌ | held 集口径不同 |
| P6 | seed+1 重划后再剔 correction | ❌ | ❌ | 划分随机源不同 |
| P7 | 训练面剔 correction、held 仍用主读法 23 件 | ❌ | ❌ | 两个变量同时动，held 集非 18 |

**独立复现的构造数 = 1**（P0）。P3 命中，**推出**（本棒推断，非盘上直接字面）：主读法 23 件 held 内的 5 件 correction **全部**是 `R_pair` / `*_pair_pending` 型 —— 即 held 集内不存在「仅靠 `read_flip` / `pi_disposition` 判为 correction」的事件，故「收窄判据」在这个具体 split 上与全判据等价。

---

## §6 口径本身的观察（登记，不裁）

替读法**同时**动了两个东西：① 剔掉 correction 事件（note 字面声称的意图）；② 因 held 变小而把 5 件 correction 放回训练集重训（note 未声称的副作用）。因此 `main−alt` 的 delta（如 K-V3-B −0.0650）**不可单独归因于「剔 correction」**，它混入了「树重训」的分量。

本件**只补记定义，不裁口径设计是否恰当**。若 PI 认为替读法应「固定主读法那棵树、只剔 evaluation 侧的 correction」（= P4 口径），则须**另立新名件 + 重跑 + 留痕**，不可改写本定义或 result_v3 既有数字（0 擅改既有件）。此为待拍板项，本棒不代拍。

---

## §7 老实交代（边界）

1. **verifier 双复核呈文本棒未见** —— 呈文本身不落盘（沿 E-42 登记面字面）。故本件的 8 候选台是**本棒自建**，与呈文的「7 种读法」**不保证逐条对应**；本件只声明「本棒自建 8 读法中唯一独立复现者为 P0」，**不代 verifier 陈述其 7 种读法的具体内容**。
2. **口径真源在 `.tmp/`** —— 出件 runner `_run_final.py` 位于临时目录而非 `results/`。这是可审计性弱点：若 `.tmp/` 被清，本定义将失去唯一代码锚点。本件已登记其 SHA-12（`75d466add5d5`）以钉住字节态；**是否把该 runner 迁入 `results/` 属待拍板项，本棒 0 迁移**（迁移 = 触动既有件，需新名 + 授权）。
3. **r1 修正后的 alt 读法另计** —— F1 修复后 r1 的 `alt_reading_after` 见 `_v4_pi_cot_v3_k3b_recheck_r1_2026_09_27.json`，那是**修复后**口径，与本件 §2 的**母件**目标签名**不可混算**。
4. 本件**未改** `result_v3.json`、executor 母件、勘误链、questionnaire_v1 任何既有件（SHA-12 实测复验不变）。
5. **succeeded ≠ 跑完**：本件宣告以盘上 SHA-12 落盘核验为准。

---

**铁律复述**：key 永不明文（本件 0 LLM，0 key 相关）· 既有件 0 触动 · 派生 JSON 不合并 · 0 擅调阈值 · 0 LLM · 不编造 · SHA-12 = `hashlib.sha256(...).hexdigest()[:12]` 小写（本件引用时统一大写显示，盘上锚值同为小写）· S-40 布尔显式命名（`hit=True` 即触发 FAIL 方向）· 产物署名如实（不冒充 Trae / KIMI / GLM / coze）。

**skill**：`scientific-research-workflows:experimental-design`（plugin `@scientific-research-workflows`）—— 该 skill 属「实验前设计」域，本件实际取用其可复现性条款（SKILL.md:196-197「Document the design, seed, and schedule … so the analysis is confirmatory and the layout is auditable」）来约束「口径必须可被第三方按行号复算」；其余条款（设计类型/DOE/随机化）与本件无关，未虚构套用。

---

Mavis 团队 worker 出件 | 2026-09-27
