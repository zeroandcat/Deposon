# V3-R 改判件 #35 · v20 GT2b BANK_SEED 复现面重评 · worker · 2026-09-27

> **性质**：V3-R 预登记 v1.1（`bcc3cee23e82`）**第三梯队 B 棒执行棒产出**；执行棒只按 K-V3R-35 字面跑，0 私设条款
> **判死线字面**：`field_tol = 0.05` **一字不动**；α（跨 T 波动）/ β（跨臂边际）**强制双报不可互替**；3 seed × 3 T = 9 格矩阵**不聚合为单一 verdict**；`cfg["seed"]` 0 消费点**禁作杠杆**
> **上游输入（只读，0 触动）**：`_v3_recheck_prereg_v1p1_2026_09_27.md` §1.2/§2.2 K-V3R-35/§2.3 TH-V3R1P1-35-*；`_v3_n_recheck_llm_verdict_2026_09_27.md` §三条
> **产出件**：`deposon_team/plugins/_v3r1p1_35_gt2b_bankseed_2026_09_27.py`（executor）+ `results/_v3_recheck_35_result_2026_09_27.json`（9 格 × 双口径矩阵）
> **0 LLM / 0 proxy / 0 key 读取**；派生 JSON 0 合并；既有件 0 字节改动

---

## §1 原结论（沿既有件字面，0 改动）

源件 `results/deposon_v20_gt2b.json`（`a2ae7997ee67`，123,331 B）：

| 字段 | as-run 值 |
|---|---|
| `verdict` | **`inconclusive`** |
| `verdict_detail.field_immunity_ok` | **`false`** |
| `accuracy_by_T` | `rule_filter` [0.15000000000000002, 0.275, 0.19999999999999998]／`field_mean` [0.375, 0.525, 1.0]／`random` [0.35000000000000003, 0.325, 0.2] |
| T=1 档 as-run 边际 | **+0.025**（沿 v1.1 §1.2 γ 登记：**仅作对照，0 作阈值**） |
| `config.seed` | `0` |

**死因（v1.1 §1.1/§1.4 登记的未决点，本件沿用）**：
1. 全部读数来自 **BANK_SEED 单值单次**（`20260828`）⇒ 0 seed 复现面，`inconclusive` 究竟源于机制还是种子未定；
2. `field_immune` 聚合口径（α，跨 T 波动）与「跨臂边际」口径（β）**混用风险**未解除；
3. 缓存域资产本仓 0 命中（`results/gt2_attacker_cache/` 不存在）⇒ 复现面不可开跑。

---

## §2 新构造（K-V3R-35 字面，逐条对照）

| 冻结字面 | 本件执行 | 0 擅调自证 |
|---|---|---|
| 唯一变量 = `BANK_SEED` ∈ {20260828, 20260829, 20260830} | 同 | `frozen_params.bank_seed_set` 逐字登记 |
| `field_tol = 0.05` 一字不动 | 同 | executor 启动即 `assert FIELD_TOL == 0.05`（改则崩） |
| `config` 其余字段（n_steps=50 / beta_schedule='linear' / prior='uniform_out' / lr=0.1 / lam_smooth=0.01 / field_guidance=True / energy_mode='aggregate'）不动 | 同（`frozen_params.config` = `config_dict(cfg)` 原样落盘） | 0 手改 |
| `T_levels={1,2,3}` / 4 域 / `n_options_fixed=4` / `chance_level=0.25` | 同（4 域 = 有缓存域；另 2 域 0 缓存，**不得外推全 6 域**） | `assets.domains_excluded_no_cache` |
| 禁作杠杆 `cfg["seed"]` | **0 改**；并给静态 + 实测双重自证 | 见 §5 |
| 不聚合为单一 verdict | `new_verdict` 字段只作**档位标签**，逐格矩阵 + 一致性计数为主 | `kou_jing_fields.aggregation` |
| 既有 verdict 按原字面另报 | 3 seed 各报一次（`legacy_verdict_separate`） | 0 并入矩阵 |

**改判档位**（沿 v1 §4 四档）：本条落 **「不明」分支** —— 防退化门（读法 A）触发 ⇒ **维持原标注 `inconclusive` 不动**，显式登记 γ，归「V4 收尾整理」待拍板桶（沿 PI 2026-09-27 文件数类/账目类统一处置口径）。**原报告 byte 0 触动**。

---

## §3 双口径矩阵（9 格 × α/β，field_tol = 0.05）

`n_items = 40/格`（4 域 × 10 items）；「最强对手」= `max(rule_filter(T), random(T))`。

| 格 (seed_T) | field_mean | rule_filter | random | 最强对手 | **α = \|fm−fm(1)\|** | α 判定 | **β = Δ** | β 判定 |
|---|---|---|---|---|---|---|---|---|
| 20260828_T1 | 0.375 | 0.150 | 0.350 | 0.350 (random) | 0.000 | ✅ immune（T=1 自指恒等，单列） | **+0.025** | ❌ BELOW_TOL（＝as-run 对照值） |
| 20260828_T2 | 0.525 | 0.275 | 0.325 | 0.325 (random) | 0.150 | ❌ not immune | +0.200 | ✅ PASS |
| 20260828_T3 | 1.000 | 0.200 | 0.200 | 0.200 (random) | 0.625 | ❌ not immune | +0.800 | ✅ PASS |
| 20260829_T1 | 0.375 | 0.325 | 0.225 | 0.325 (rule_filter) | 0.000 | ✅ immune（T=1 自指恒等） | **+0.04999999999999999** | ❌ BELOW_TOL（**刀锋格**，见 §6 γ-G35-6） |
| 20260829_T2 | 0.550 | 0.325 | 0.200 | 0.325 (rule_filter) | 0.175 | ❌ not immune | +0.225 | ✅ PASS |
| 20260829_T3 | 1.000 | 0.250 | 0.275 | 0.275 (random) | 0.625 | ❌ not immune | +0.725 | ✅ PASS |
| 20260830_T1 | 0.350 | 0.250 | 0.250 | 0.250 (tie→rule_filter) | 0.000 | ✅ immune（T=1 自指恒等） | +0.100 | ✅ PASS |
| 20260830_T2 | 0.425 | 0.275 | 0.300 | 0.300 (random) | 0.075 | ❌ not immune | +0.125 | ✅ PASS |
| 20260830_T3 | 1.000 | 0.150 | 0.350 | 0.350 (random) | 0.650 | ❌ not immune | +0.650 | ✅ PASS |

### 3.1 一致性计数（K-V3R-35：计数，0 单一 verdict）

- **β 档位计数（float 字面）**：PASS **7** / BELOW_TOL **2**；`beta_9_of_9_same_band = false` ⇒ 存在异档格（两条均在 T=1 档）
- **β 档位计数（若刀锋格按数学值取整）**：PASS 8 / BELOW_TOL 1 —— **仅作对照登记，0 参与判定**
- **α（T∈{2,3}，排除 T=1 自指格）**：`field_immune` 计数 **0/6** ⇒ `alpha_all_T2T3_immune = false`
- **α/β 是否同向**：**否** —— α 在全部 6 个非平凡格判「非场免疫」，β 在其中 5 格判 PASS ⇒ **两口径结论不可互替**（K-V3R1P1-0-C），逐格并报如上，0 合并、0 取其一
- **既有 verdict 另报**：3 个 seed 全部 `inconclusive`（`rf = [0.15, 0.275, 0.20]`-类序列非严格单调，`strict_inc`/`strict_dec` 双假）⇒ **换 seed 不改既有判定成因**（成因是 `rf` 非单调，不是场免疫）

### 3.2 环境自证（0 环境漂移）

`as_run_environment_self_check.bit_identical = true` —— 以 `BANK_SEED=20260828` 重跑，9 项 arm×T 读数与在盘 `deposon_v20_gt2b.json` **逐位相同**（含 `0.15000000000000002` 等浮点尾数）；legacy verdict 同为 `inconclusive`；T=1 边际重算 +0.025 与 as-run 对照值一致（0 作阈值、0 参与判定）。

---

## §4 结论（分口径，0 跨口径主张）

1. **α 口径（既有字面）**：`field_immune = false` 在 **3/3 seed 全部复现**（6 个非平凡格无一 immune）⇒ **换 BANK_SEED 不改变 α 判定**。`field_mean` 随 T 抬升 0.375/0.525/1.0（seed 20260828）跨档差 0.15/0.625，远超 `field_tol = 0.05`。
2. **β 口径（派工字面）**：9 格中 7 格 PASS、2 格 BELOW_TOL，**两条 BELOW 均落在 T=1 档**（+0.025 与 +0.05 刀锋）；T=2/T=3 在 3 个 seed 全部 PASS ⇒ **跨臂边际在 T≥2 稳定达标，T=1 档为边际档**。
3. **两口径分歧本身是结论**：α 判「场不免疫」、β 判「跨臂达标」⇒ 既有 `inconclusive` 的**根因不是口径混用**（两口径在同 9 格上各自自洽且方向相反），而是 **`rf` 序列非单调** + **T=1 档边际**两项同时存在。
4. **本条不可判的原因（诚实）**：不是「跑不动」，而是**防退化门读法 A 触发**（见 §5）⇒ 按 K-V3R-35 (b) 机械落定「不明」+ γ。

---

## §5 防退化门自证（K-V3R1P1-0-A，三读并报，0 私自改门）

`n_distinct > 3 + std > 0`；**读法依赖性如实登记**：

| 读法 | 序列定义 | 结果 | 门 |
|---|---|---|---|
| **A（判死线字面所指：item 级）** | 每格每臂的 4 个域 item 级正确率（n=4） | 27 条（9 格 × 3 臂）中 **仅 6 条过门**（`field_mean` 在全部 3 个 T=3 格 `n_distinct=1, std=0.0`，因 4 域全对） | ❌ 触发 ⇒ (b) 分支「不明」 |
| **B（二值单列，PI 拍板③）** | 每格每臂的 40 条 item 级 0/1 正确性（n=40） | 结构性二值 ⇒ `n_distinct ≤ 2` 恒成立 | 单列，不与门混算 |
| **C（格级读数）** | 9 格格级读数序列（每臂 n=9） | `rule_filter` n_d=5 / `field_mean` n_d=6 / `random` n_d=8，std 均 > 0 | ✅ 全过门 |

**判死线字面所指为「item 级正确率」⇒ 以读法 A 为准** ⇒ 触发 K-V3R-35 (b)「不明」+ γ 登记。读法 C 若被采纳则落 (a) 分支「按矩阵如实登记」——**两读差异如实登记，0 合并、0 私自改门**（口径归属属 PI 拍板项，非本执行棒可决）。

**退化杠杆事前登记（`cfg["seed"]`）双重自证**：
- 静态：`run_v20_gt2b.py` 内 `cfg["seed"]` 消费点 **0**；传入 `field_scores_init` 的种子字面为 `g_seed + (u*131+v) % 100000`；`deposon_protocol.py` 内 `field_scores_init` 以 `{"seed": inst_seed}` **覆盖**传入 cfg 的 seed 字段 ⇒ `cfg.seed` 结构性不可消费
- 实测：把 `cfg.seed` 由 `0` 改为 `987654321` 重跑一格 ⇒ 输出 **bit-identical**（`empirical_bit_identical_when_cfg_seed_changed = true`）
- ⇒ 改 `cfg.seed` 必产 `n_distinct = 1` 退化输出，**本件 0 以其为杠杆**（K-V3R1P1-0-A 退化杠杆事前登记项）

---

## §6 γ 登记（沿 K-V3R-35 (b) + 诚实交代）

| ID | 触发 | 状态 | 处置 |
|---|---|---|---|
| **G35-1** | 读法 A 防退化门 27 条序列中 21 条不过门（`n_distinct ≤ 3` 或 `std = 0`；最典型：T=3 格 `field_mean` 4 域全对 ⇒ `n_distinct=1, std=0`） | **triggered** | 判「不明」；主因 |
| **G35-2** | 另 2 域（`geography_world` / `project_management`）无 `gt2_attacker_cache` | registered_as_scope_limit | 仅 4 域，**不得外推全 6 域**（v1.1 §1.3） |
| **G35-4** | T=1 档 as-run 边际 +0.025 | control_only_not_threshold | 留档，0 作阈值、0 参与判定 |
| **G35-5** | 既有 `mindmap_corpus_v20.load_corpus` 孤儿哨兵在本仓现状抛错（`corpus/v20/` 下 `all.json` / `index_v2_2026_09_16.json` / `strip_captions_22.json` 三个**非图** JSON 未入 `index.json`） | deviation_registered | executor 走**等价只读加载**（`index.json` 登记顺序 + `family=="L"` 过滤，返回集合与成功路径逐件相同）；0 改既有模块、0 改 `index.json`、0 改语料 |
| **G35-6** | **β 刀锋格**：`seed20260829_T1` 的 `Δ = 0.375 − 0.325`，两侧读数在 0.1 粒度网格上 ⇒ **数学值恰为 0.05**，IEEE-754 双精度差为 `0.04999999999999999` ⇒ float 字面判 BELOW_TOL | **triggered** | 0 擅调阈值、0 round；**双读并报**（float 字面 BELOW_TOL / 数学值 PASS） |

**未触发项（如实登记）**：仓外只读被拒（未发生，4 件复读前后 SHA-12 + 字节一致）／缓存域缺（未发生，4 域齐全）／跑不完（未发生，9/9 跑完）。

---

## §7 只读与 0 触动声明

- **仓外只读取用**（K-V3R1P1-0-F）：`D:/私人资料/_non_upload_local_archive/results/gt2_attacker_cache/` 4 件，跑前/跑后逐件复读 `sha12 + bytes` **完全一致**（`external_readonly.pre_post_identical = true`）；**0 复制入仓 / 0 写入 / 0 移出 / 0 删除 / 0 改 ACL**；本仓 `results/gt2_attacker_cache/` **仍不存在**
  - `algorithm_process.json` `ddda494f014a` / 2,782 B ｜ `biological_taxonomy.json` `0f0a4329c34f` / 2,385 B ｜ `historical_causality.json` `86af2ef6b66c` / 2,341 B ｜ `physics_concepts.json` `9c74bb8206c0` / 2,386 B
- **既有件 0 触动**：`run_v20_gt2b.py`（`361aff516219`）、`run_v19_meanfield.py`（`67ef3779478a`）、`deposon_protocol.py`、`mindmap_corpus_v20.py`、`corpus/v20/index.json`、6 件 L 族图面、`results/deposon_v20_gt2b.json`（`a2ae7997ee67`）、v1 / v1.1 预登记 —— **全部只读，0 字节改动**（哈希基线落 `result.input_chain` / `result.corpus_files`）
- **派生 JSON 0 合并**：新名独立件 `results/_v3_recheck_35_result_2026_09_27.json`，0 并入 `deposon_v20_gt2b.json` 或任何 `_v3_n_*`
- **key**：0 明文密钥、0 key 读取（本条纯本地数值重算）
- **0 LLM**：0 调用、0 proxy

---

## §8 老实交代

- **skill 未加载**：本 Turn 工具集内**无 skill 加载工具**（无 `skill` / `tool_search` 入口）⇒ 派工单指定 `scientific-research-workflows:experimental-design` **未加载到**；按纪律锚 fallback 执行（`_v3_recheck_prereg_v1p1_2026_09_27.md` K-V3R-35 字面 + `_v3_n_recheck_llm_verdict_2026_09_27.md` §三条现状），**0 编造 skill 指令**
- **口径归属未决（如实登记，非本棒可决）**：「防退化门 `n_distinct` 取哪条序列」决定本条落 (a) 还是 (b) 分支；本件按判死线字面「item 级正确率」取读法 A ⇒ 不明，两读差异全部登记待 PI 拍板
- **β 刀锋格未擅自取整**：1 格处于阈值浮点刀锋上，双读并报，0 改阈值
- **构造面边界**：结论仅覆盖 **4 缓存域 × 40 items/T × 3 BANK_SEED × 3 T 档**；0 外推至全 6 域、0 外推至其他 seed 集、0 外推至其他 `config`
- **0 主张**：本件**不**主张「GT2B 命题被证伪」，也**不**主张「field_mean 优于/劣于 rule_filter」—— 既有 `inconclusive` 维持不动，机制性免疫披露（陷阱标签不在图节点集内 ⇒ field_mean 对其打 −inf）沿源件字面沿用，不因重评而升级
- **succeeded ≠ 跑完**：9/9 格跑完并落盘；但完成宣告以落盘核验（字节 + SHA-12 + 重跑逐字不变）为准，值见最终汇报

---

出件｜Mavis 团队 worker｜2026-09-27
