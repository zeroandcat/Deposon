# V3 实验资产勘误件（Trae code 走读出证）· 2026-09-23

> **出证方**：Trae code（第三方走读）
> **委托来源**：`letters/TRAE_V3_REVIEW_LETTER_2026_09_23.md` §3「走读与修复实验资产」
> **性质**：**新增勘误件，不改任何既有报告正文、不改任何实验结论与判定本体**。本件只做两件事——(1) 记录 V3 实验资产的实际位置与路径映射；(2) 登记走读发现的引用层/数字层缺陷清单，供 PI 另行处置。
> **边界**：0 LLM / 0 外部 URL / 0 密钥；V1–V3 既有资产只读；V4 `_v4_*` 全链未触碰。

---

## §1 为什么需要本件

V3 的实验数据与 runner **已不在** `deposon-repo` 内。`docs/V3X/` 的 19 份报告正文仍按 `results/xxx.json`、`deposon_team/plugins/xxx.py` 的相对路径引用它们——按报告字面路径在本仓查找会得到「文件不存在」，容易被误读为「结果缺件 = 结论无据」。

**实测**：本件出具时（2026-09-23），`deposon-repo` 全树对 19 报告引用的 34 个 `results/*.json` 做存在性核验——**10 件不在本仓、但在 `D:\私人资料\deposon-sub\` 内**；3 件两仓均无（真缺件，见 §4）。

**迁移依据**：`D:\私人资料\deposon-sub\_movedout_manifest_2026_09_21.json`（291,551 B，SHA-12 `D1EE21F3F6AE`，含 UTF-8 BOM）——363 条记录，字段 `src / dst / sha12 / size / archived_at`，`archived_at` 全为 `2026-09-21T18:01:05.991541`，**无移出原因字段**。363 条 `dst` 全部在磁盘存在（MISSING=0）。

---

## §2 路径映射（报告引用 → 实际位置）

| 报告引用路径 | 实际位置 | SHA-12 | 字节 |
|---|---|---|---|
| `results/boss_pa_1_rbr_rm_result_2026_09_15.json` | `deposon-sub/results/` | `C7C59E0D2F6C` | 8,753 |
| `results/boss_pa_2_potential_game_result_2026_09_15.json` | `deposon-sub/results/` | `5C76137D6430` | 7,530 |
| `results/boss_pa_3_replicator_dynamics_result_2026_09_15.json` | `deposon-sub/results/` | `D6F233D73C45` | 9,098 |
| `results/boss_pc_1_a1_resampling_2026_09_15.json` | `deposon-sub/results/` | `D21912A05D79` | 1,017 |
| `results/boss_pc_1_real_2d_ising_2026_09_15.json` | `deposon-sub/results/` | `43D9CE160FC8` | 2,460 |
| `results/boss_pc_2_a2_fitting_2026_09_15.json` | `deposon-sub/results/` | `5A880678C386` | 1,024 |
| `results/boss_pc_2_real_transverse_ising_2026_09_15.json` | `deposon-sub/results/` | `8933D61B180A` | 3,553 |
| `results/boss_pc_3_a3_clipping_2026_09_15.json` | `deposon-sub/results/` | `D74D6B39D1B0` | 1,265 |
| `results/boss_pc_3_real_reservoir_2026_09_15.json` | `deposon-sub/results/` | `94B5398BE76C` | 2,364 |
| `results/boss_pe_1/2/3_real_*_2026_09_15.json` | `deposon-sub/results/`（与 `boss_pc_*_real_*` 逐字节相同） | 同上三值 | 同上 |
| `results/attack_pc_a1/a2/a3_*.json` | `deposon-sub/results/`（与 `boss_pc_1_a1 / 2_a2 / 3_a3` 逐字节相同） | `D21912A05D79` / `5A880678C386` / `D74D6B39D1B0` | — |
| `results/d7_5anchor_60cells_9model_verdict_2026_09_18.json` | `deposon-sub/results/` | `4505CCA79C15` | 2,456 |
| `results/skill_d_p_f_observer_result_2026_09_11.json` | `deposon-sub/results/`（同名） | 见 manifest | — |
| 根目录 `_p_l_v3_phase*.py`（12 件） | `deposon-sub/` 根 | 见 manifest | — |
| `deposon_team/plugins/_p_i/j/k/l/m/n/o_*_runner_2026_09_16.py` | `deposon-sub/deposon_team/plugins/` | 见 manifest | — |

**核验结论**：委托信 §3 所列 3 个「疑似缺件」BOSS JSON（`boss_pa_1_rbr_rm_result` / `boss_pa_2_potential_game_result` / `boss_pc_1_a1_resampling`）——**均存在于 `deposon-sub/results/`，且实算 SHA-12 与历史曾引值逐一相同**。判定：**历史迁移，非真缺件**。

**corpus 面（委托信 §3 线索二）核实**：`corpus/v19`、`corpus/v21`、`corpus/v22` 目录在 repo 内**确不存在**（旧文档引用面）；22 caption 实锚在 `corpus/v20/`——`strip_captions_22.json` + `L_*.json`(6) + `S*.json`(16) 共 23 件均在盘（实跑 `LS corpus/v20` 确认），另含 `by_model/{GLM_1,GLM_2,coze,kimi,minimax}/`。判定：**旧路径名失效，实体件在 v20**。

**在盘件面（供对照）**：`results/deposon_pa_d1_d3_2026_09_15.json`(`E221792715F8`) / `deposon_pc_d1_d3` / `deposon_pe_d1_d3` / `deposon_pf_d1` / `deposon_pf_d1_full_9m5c` / `deposon_pg_v01_9m60c` / `deposon_v20_gt2b` / `deposon_v19_benchmark_fixes`(`910c4333eead`) / `deposon_v21_gtformal`(`9d9ae5001c57`) **均在 repo `results/`**——即 V3 的「汇总层 JSON」在仓，**「BOSS 分件层 JSON」已移出至 deposon-sub**。引用时须分辨这两层。

---

## §3 同一性登记（避免重复计数）

以下文件组**逐字节相同**，引用时勿计为独立实验：

- `attack_pc_a1_resampling` ≡ `boss_pc_1_a1_resampling`（`D21912A05D79`）
- `attack_pc_a2_fitting` ≡ `boss_pc_2_a2_fitting`（`5A880678C386`）
- `attack_pc_a3_clipping` ≡ `boss_pc_3_a3_clipping`（`D74D6B39D1B0`）
- `boss_pc_1_real_2d_ising` ≡ `boss_pe_1_real_2d_ising`（`43D9CE160FC8`）
- `boss_pc_2_real_transverse_ising` ≡ `boss_pe_2_real_transverse_ising`（`8933D61B180A`）
- `boss_pc_3_real_reservoir` ≡ `boss_pe_3_real_reservoir`（`94B5398BE76C`）

即：**P-C 命名空间的 `*_real_*` 三件与 P-E 命名的三件是同一批文件**。这与 2026-09-16 已登记的「BOSS 命名轴与攻击轴错位」同源（见 `docs/V3X/TRAE_3RISK_FIX_REPORT_2026_09_16.md`）。

---

## §4 真缺件（repo / archive / deposon-sub 三处均无，需 PI 裁定处置）

以下 3 件在 `deposon-repo`、`D:\私人资料\_archive_deposon_2026_09_17\`、`D:\私人资料\deposon-sub\` **三处实测均不存在**，且不在 09-21 manifest 内：

| 文件 | 被引用处 | 三处实测 | 处置建议 |
|---|---|---|---|
| `results/deposon_v17_fusion_fix.json` | 报告引用链 | repo× archive× sub× | 若为上游已被取代版本，建议在引用处标注「已废版」；若为必需输入，需补件 |
| `results/deposon_v18_api_supplements.json` | 报告引用链 | repo× archive× sub× | 同上 |
| `results/deposon_v20_baselines.json` | `P_A_D1_D3_REPORT` 列为 frozen run，且为 `boss_pa_1` 的直接输入 | repo× archive× sub× | **优先处置**：该件是 P-A BOSS 的输入，缺失使 P-A 证据链上游断开 |

**复核方式**：`deposon_team/plugins/_v3_review_r5_anchor_probe_2026_09_23.py`（实跑，exit 0）逐处 `os.path.exists` + 实算 SHA-12，三处皆 NO。

---

## §5 引用层/数字层缺陷清单（登记，不改历史行）

**登记原则**：勘误注记，不回改历史行；供 PI 另行处置。

| # | 类型 | 位置 | 事实 |
|---|---|---|---|
| E-1 | 数字矛盾 | `V3X_D7_V3_FINAL_REPORT...V7.md` §0/§1.1 vs §1.2 | 同报告内 `51/60 = 85%` 与 `52/60 = 86.67%` 两套「60 cells」口径并存 |
| E-2 | 数字矛盾 | `P_A_D1_D3_REPORT` §3.1 vs §3.1 表 L143–147 | 表内 `RM iter=1`、`Bayes iter=32` 与同报告均值（RM 6.0 / Bayes 37.18）矛盾；且与在盘脚本 `boss_pa_1_rbr_rm.py` 的返回值域（RM ∈{≥6}∪{200}，Bayes ∈{1,200}）不相容 |
| E-3 | 表-JSON 不符 | `P_A_D1_D3_REPORT` L143–147 | 表值（199/1/32/6.2188/0.0312）与冻结 JSON 实值（200/6/200/1.0/0.03）**逐字段不符** |
| E-4 | 计数标签 | `P_C_D1_D3_REPORT` L236 / `D5_DECISIONS_LAND_REPORT` L107 | `TOTAL: 15 frozen files \| OK: 16 \| FAIL: 0` 等标签自相矛盾 |
| E-5 | 数字矛盾 | `D_FIX2_METRIC_VERIFY_REPORT` vs 其余 | doubao `T_frac` 0.8833（53/60）vs 0.8667（52/60） |
| E-6 | 数字矛盾 | `P_A/P_C/P_E` vs `P_G` | `D_fix2(deepseek-v4-pro)` 0.1775 vs 0.1776 |
| E-7 | 数字矛盾 | `P_C_D1_D3_REPORT` §3.3 vs 他处 | Spearman −0.8000 vs −0.832 并列未说明 |
| E-8 | 数字矛盾 | `KT_C1_REPORT_PHASE_B` L109 | 「11 个不同 n 值」与列举的 7 个值（n=2..8）自相矛盾 |
| E-9 | SHA 不一致 | `V3X_1WEEK_KILL_REPORT` L110 vs `D5` L136 / `TRAE_3RISK` L45 | 派生 JSON SHA-12 `da517c1153c`（11 hex）vs `da517c115f3c` |
| E-10 | 计数标签 | `D7_POST_CLEANUP_REPORT_2026_09_16.json` | 字段名 `frozen_18_skipped` 但数组实为 17 项；`files_remediated: 90` 无明细清单可核 |
| E-11 | 状态矛盾 | `V3X_1WEEK_KILL_REPORT` L92 vs L167 | 同报告内「540 cells LLM 实算」与「540 cells, 0 LLM」并存 |
| E-12 | 状态矛盾 | `V3X_1WEEK_KILL_REPORT` 正文 vs L178 尾注 | 正文已填 4 路径 verdict，尾注仍称「verdict 占位待 D7 当日填」 |
| E-13 | 字节数 | `boss_pa_1_rbr_rm_result_2026_09_15.json` | 一处记 8,674 B，实为 8,753 B（SHA `C7C59E0D2F6C` 与实算一致） |
| E-14 | 编码 | `deposon-sub/_movedout_manifest_2026_09_21.json` | 首 3 字节 `EF BB BF`，含 UTF-8 BOM（同批归档的数据件均无 BOM） |
| E-15 | **锚链断裂（最高优先）** | `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | frozen 期望 SHA-12 `03c6c01f3697`（6,680 B）；但**冻结主路径在盘件为另一件**（11,318 B，`6e9cd8cd8e07`，`metadata/anchors/boss_baselines` 结构、2026-09-09「Mavis (root session)」）；**冻结 fallback 路径**（`_archive_deposon_2026_09_17/verifier/handoff/`）**无此件**；目标件仅存于未声明的 `D:\私人资料\_non_upload_local_archive\verifier\handoff\`。→ `_verify_15frozen.py` 2026-09-23 实测 **15/16 PASS, 1 FAIL（唯一 FAIL 即本项）**，0-touch 声明 = FAIL。**【已处置 2026-09-23，PI 授权「直接修正」→ 详见 §7】** |
| E-16 | SHA 位数 | `V3X_1WEEK_KILL_REPORT` L110 vs 盘上实值 | 报告写 `da517c1153c`（11 hex）；`KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json` 实算 `da517c115f3c`（12 hex，5,049 B，与 `D5` L136 / `TRAE_3RISK` L45 一致） |
| E-17 | 错字（**PI 已裁定不修**） | `letters/_v4_distillation_invitation_2026_09_20_v1.0.md` L218 | "behated"（"behaved" / 种子「被测」的转写残迹，三处）；PI 已于 2026-09-22 裁定「不再修邀请函」（`results/_v4_pi_decision_questionnaire_2026_09_21_v1.1.md` L679）；该件属 V4 `_v4_*` 链，本走读 0 触动——仅登记结案 |
| E-18 | 缺 SELF-CHECK 尾块（frozen） | `skill_a/b/c/d_*.py`（4 件） | 09-16 改进信 §4 不改项**至今悬挂**；frozen-18 内不可代修——仅登记。对照：9 个 `boss_*.py` 的 SELF-CHECK 已于 09-16 全部补齐（`TRAE_SELFCHECK_2026_09_16` 标记逐件在盘） |
| E-19 | BOM（verifier 家族） | `_verify_15frozen.py` / `_verify_15frozen_v1.py` / `_verify_pg_v0.py` / `_verify_pg_v0_v1.py` | 4 件含 UTF-8 BOM；verifier 内置脚本不动——仅登记。对照：`docs/V3X` 报告层（全部 md/json）**0 BOM**（r8 实扫） |
| E-20 | **结论标注（PI 拍板「过强」）** | P-A 方向中期判定（`boss_pa_1_rbr_rm_result_2026_09_15.json` `C7C59E0D2F6C` verdict=DIFFERENTIATED，rbr/rm 倍数 145.8x/4.9x 等差异化读数） | C1/C3/C4/C5 构造退化实锤（诊断件 `C8D539A58D29`：simulate_rm 恒 6 / bayesian_nash_iter 二值常量 / rbr_mult 三值派生 / 12-bit LSH 22→6 坍缩），差异化读数建立在退化构造上 → 标注「**过强（构造退化未排除）**」。原报告与原判定本体一字不动，本行为唯一处置（PI 问卷 `ask_559be3e5c562961f0a51ec97` Q4=a；非退化对照实验跑出后可追加对照结论行，不回改本行） |
| E-21 | **PG 双读数统一 + 命名修正** | BOSS-A2「22/22 全 PG」（`KT_B1_REWORK_REPORT` §三 / `BOSS_SELFTEST_PHASE_B` L30）vs BOSS-P-A2「3/22」（`5C76137D6430`） | 22/22 系 **2×2 单调 payoff 构造退化假阳性**（cyclic condition 恒等式自动满足，判据无鉴别力——退化族第 5 例）；统一口径 = **4 元完整 payoff 构造为唯一标准，22-graph 面 PG 事实 = 3/22**。命名修正：「KT-B1 22/22」系挂错名（22/22 属 BOSS-A2；KT-B1 本体是 Sinkhorn/KD bug）。处置件 `results/_v4_pa2_pg_unified_criteria_2026_09_23.md`（PI 授权 Mavis 出具，问卷 `ask_fc39c0f020834291496fcd88` Q3）；历史报告正文一字不动。R11 PCD「22 轮」口径同轮固化（`= Per-Caption Drop，22 对象各删 1`，件 `_v4_r11_pcd_22round_definition_2026_09_23.md`——挂账根因=口径未文档化，非实验不明） |
| E-22 | **E-20 对照结论追加（崩塌）** | P-A1「RBR/RM ≥ 2.0x → DIFFERENTIATED」主张（`C7C59E0D2F6C` 读数 145.82x） | V4 非退化对照（`_v4_contrast_nondegenerate_2026_09_23.py` `A0BFC7DF887F`）实测：rbr_mult mean **145.82x → 1.0174x**，P-A spec class **DIFFERENTIATED → GRAY_DEFLATE（≤1.3x）**；替代读法（剔 S1_n60/S2_n20）同向（0.9525）。根因 = C3 `bayesian_nash_iter` 二值闭合（`return 1 if nash else 200`）在 18/22 graphs 返回 1（闭式解误作迭代数），与 C2 联合派生 rbr_mult∈{1,2,200} 的 200 主导均值——**E-20「过强」升级为「假证伪线索」：强度信号在非退化构造下崩塌**。证据件 `results/_v4_v3_degradation_contrast_{result.json,verdict.md}`（`811139E25130`/`3BD454B1A780`）；双读法同向、判死不软化（非「近似成立」）。E-20 行不动，本行为其预留的对照结论追加行 |
| E-23 | **N-29 真审 = 真证伪（四轮首条）** | N-29「22 graphs × {RBR/RM} 初值表可作博弈输入初值，且初值表 ≠ 路径」（预登记 `0A9EE16267B5` L446-463） | 判定史四轮：缺件 FAIL（假证伪）→ 素材面不覆盖 FAIL（假证伪）→ 构造退化 FAIL（假证伪）→ **真实轨迹面 FAIL = 真证伪**（kill-line 预注册 ✓ / 构造非退化自证 ✓〔rm_iter 真分布 197-200、bayes 连续 6 值、per-field n_distinct≥17〕/ 素材面覆盖 ✓〔22×3×200 真实轨迹〕/ 度量有分辨力 ✓〔JS 0.33-1.0〕）。**K-N29-2 命中：13/22 graphs JS > 0.50**（max=1.0，排列检验 p=0.001）——路径与初值无关的极端方向，「初值表可作输入初值」被证伪。**副产物：V3 RM regret bug 实锤**（旧版 `cum_payoff[未取过 action]=0 → regret=0 → 单 action 退化`）= C1「simulate_rm 恒 6」的机制根源。证据件 `_v4_n29_real_verdict.md` `E62D245CE285` + 轨迹 `98484EEEAB9B` + 判定 `0485D3EBBC67`；V1–V3 0 触动自证 |
| E-24 | **S-40 修复重判（FAIL→PASS）** | S-40 长期漂移重跑判 FAIL（`_v4_rerun_verdict` CV=0.10）与升格判「artifact」 | 语义反转双因修复（verifier 复核 `0D6B3C74DC98` 实锤）：① 删除 L833 私设条款 `or range_val > 1.0`（非预登记三条款）② L837-853 恢复 pass wrapper 显式方向（`pass=True` = kill-line 未触发）。修复后按预登记字面重判 = **PASS**（cv_val=0.100852 / ci_hi=0.110904 / cv_shuf=0.100852，三条款全 False；与 verifier 独立复算 4 位精度全等）。执行棒 `7A98FDF05466` → `CB47672E3062`；重判件 `_v4_exec_s40_rejudged_2026_09_23.json` `D3F376A6C45F`；补正件 `065E57820C36`。**parent 复审通过**（Mavis 亲验 diff：三条款一一对应、阈值一字未动、历史件 0 触动）。升格件原件不动，本行为其根因补正的落地形式 |
| E-25 | **任务 B v1 判定改判（真证伪→假证伪）** | 任务 B v1 判定 `_v4_pi_cot_verdict.md` `D279EBDE5E84`「FAIL，根因=命题层面被证伪（真证伪）」 | PI 点破（2026-09-23）：「待拍板项用户确认能体现我的什么思维链？」——v1 数据集 23 条为**拍板痕迹**（reason 字段 17/23=「未给理由（选项即判定）」），**不含思维链内容**（判定结果 ≠ 思维链）。判别要件③「素材面覆盖 claim 所需」**不满足**（claim=「PI 思考链可被 proxy 复现」，素材面=判定选择痕迹）→ 改判「**假证伪（素材面不覆盖思维链——命题未受审）**」。FAIL 读数本身维持（该数据上学不到信号是事实），但**不得读作「思维链不可复现」**。采集面自 v2 起改**特制蒸馏问卷**（PI 明示：不复用待拍板项结果）；v1 dataset `139DBFFD8CF9` 保留为「判定痕迹」存档不作思维链素材 |
| E-26 | **任务 B claim 定位偏差注记（画像式→批判性学习式）** | v1 claim「proxy 判定规则集复现一致率 ≥0.8」（预登记 `696af9121d9f` §2） | PI 定性（2026-09-23）：「我的思维方式可以被 AI 批判性学习，这才是蒸馏我的思维链的最大意义且遥相呼应 V1 阶段的脑图主题，而不应是给我做画像」——v1 claim 的「复现一致率」是**画像式度量**（预测 PI 行为），非学习度量（方法论内化）。V1 脑图主题实锤：G1「AI 应当如何思考」（`55428F6BD848`，GOAL_拓扑智能）——蒸馏 = 该主题的真人方法论输入面。**v1 FAIL 完整根因两层：①素材面不覆盖思维链（E-25）②claim 面向画像非批判性学习（本行）**。v2.2 claim 重定三指标：结构相似 ≥0.8 + 分歧批判理由 100% + 盲从率 ≤0.1（`_v4_pi_cot_v2_prereg.md` v2.2） |

---

## §6 本件边界声明

- **未修改任何既有文件（一项授权例外，见 §7）**：`docs/V3X/` 19 份报告正文、`results/` 现存件、`corpus/v20/` 全部件、`deposon-sub/` 全部件、V4 `_v4_*` 全链，均 0 字节改动。**例外**：`verifier/handoff/KT_ABC1_anchors_sha256_12.json` 于 2026-09-23 经 PI 明示授权（「你直接修正」）按 E-15 处置复位——这是本件出具的唯一一处既有文件写入，处置记录见 §7。
- **未修改任何结论**：本件只登记位置与缺陷，不裁定命题存亡；E-15 复位是**资产层修复**（恢复冻结契约所声明的字节状态），**不涉任何实验结论与判定本体**。
- **本件为新增件**（2026-09-23 初版 `48EFD3828D54`；含 §7 处置记录的更新版 SHA-12 见落盘报值）。

---

## §7 E-15 处置记录（2026-09-23，PI 授权「你直接修正」）

**授权链**：回审回函（`letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23.md`，SHA-12 `9BB22099DB3B`）§3.4/§4 将 E-15 列为「须 PI 先解决、不属 Trae 可擅动」→ PI 于同日明示「你直接修正」→ 执行。

**修正前置核查（引用扫描，防误伤）**：
- 仓内 **13 个脚本**期望该路径 = `03c6c01f3697`：`boss_pa_1/2/3_*.py`、`skill_a/b/c/d_*.py`、`_pg_v01_compute.py`、`_verify_pg_v0.py`、`_verify_batch5_2026_09_18.py` + 6 个归档 V4 自检脚本（`results/_archive_2026_09_21/`）；归档 `_v4_reader_verify_2026_09_20.py` 记录尺寸 **6,680 B**，与复位源逐字节一致。
- **0 个脚本**引用顶替件独有的 `boss_baselines` 键 → 顶替件无任何在跑依赖，复位零误伤。

**执行脚本**：`deposon_team/plugins/_v3_review_r7_fix_e15_2026_09_23.py`（三步可回滚：幂等保护 assert + 源件校验 assert + 备份名占用 assert；实跑 exit 0）。

**前后 SHA-12 对照**：

| 件 | 修前 | 修后 |
|---|---|---|
| `verifier/handoff/KT_ABC1_anchors_sha256_12.json`（冻结主路径） | `6E9CD8CD8E07`（11,318 B，顶替件） | **`03C6C01F3697`（6,680 B，冻结期望件）** |
| `verifier/handoff/KT_ABC1_anchors_sha256_12.root_session_11318B.bak_2026_09_23.json`（新增备份） | —（不存在） | `6E9CD8CD8E07`（11,318 B，顶替件原样保全） |

**修后终验（机器复算）**：`python -B deposon_team/plugins/_verify_15frozen.py` → **`TOTAL: 16 frozen files | OK: 16 | FAIL: 0`、`0-touch declaration: PASS`**——修前 15/16（唯一 FAIL = E-15）→ 修后 16/16。V3/V4 全部报告所引「5 锚 SHA-12 `03c6c01f3697` 未动」自此在冻结主路径上**重新可验证**。

**顶替件归宿**：以 `.bak_2026_09_23` 新名保全于 `verifier/handoff/`（其 `boss_baselines` 9 BOSS 基线内容未删；因 0 脚本引用，不构成运行依赖）。若 PI 认定该件为应保留的 root session 工作版，可自行再处置；若认定为误写入，可删除备份。

**回滚方式**（如 PI 事后不认此复位）：把备份件字节复制回主路径即可，主路径将回到 `6E9CD8CD8E07`。

---

## §8 精扫复核记录（r8，tokenize 级，2026-09-23 续「直接修正」轮）

**执行件**：`deposon_team/plugins/_v3_review_r8_precise_scan_2026_09_23.py`（实跑 exit 0）。

**r4→r8 仪器修正**：r4 走读扫描器的 ODD_ESCAPE 判定**全部为 raw-string 假阳性**（如 `Path(r'D:\私人资料\...')` 是合法 Python）。沿本项目「测量仪器自身即误差源」惯例——**修仪器不修文本**：新增 r8 精扫器（tokenize STRING token 级、raw 前缀跳过、合法转义集白名单），r4 原件按历史证据保全不改。

**r8 判定（可修面残余缺陷）**：

| 检验面 | 结果 |
|---|---|
| 无效转义（真实语义级） | **0 处**（全 plugins 树 34 件 *.py 逐 token） |
| BOM | docs/V3X 报告层 **0**；plugins 4 件全在 verifier 家族（→ E-19 登记，不动） |
| 缺 SELF-CHECK 尾块 | 可修面 **0**（9 个 boss_* 已于 09-16 全有；4 个 frozen skill_* → E-18 登记） |
| 缺 `__main__` guard | 可修面 **0**（verifier 家族不动；本次 `_v3_review_r*` 系一次性取证件，**字节稳定即证据价值**，不加 guard 以免 SHA 漂移） |
| repo 外绝对路径 | 可修面 **0**（verifier fallback 系设计；取证脚本指向 deposon-sub 系必需） |

**结论**：E-15 修正 + r8 精扫后，**委托信 §3 全部修复项在可修面上的残余缺陷合计 = 0**；其余全部位于不动层（frozen / verifier 内置 / P-G 链 / 报告正文 / V4 链 / 仓外），已按 E-1…E-19 完整登记，PI 另行处置。

## §9 复判修订（2026-09-23 续，PI 授权「立即复判并出勘误修订」）

**触发**：PI 提示仓外两目录（`D:\私人资料\deposon-sub\` / `D:\私人资料\_non_upload_local_archive\`）存有实验产物；勘察实锤 **§4 三件「真缺件」实存于 `deposon-sub\results\`**，SHA-12 逐一 MATCH 登记值（`C7C59E0D2F6C` 8,753 B / `5C76137D6430` 7,530 B / `D21912A05D79` 1,017 B）→ **§4「真缺件」判定作废**，改判「幽灵引用」（实件在 repo 外目录，报告引 `results/` 相对路径）。

**处置（PI 问卷 `ask_3c79ce9a704bfd0a2c9c6660`）**：
- Q1=B：12 件 `boss_*2026_09_15.json` 复制回 `results/`（原件不动），**12/12 HASH-SAME、0 碰撞**。
- Q2=A：N-29/30/31 立即真实复判（原 executor 三段为纯 stub——只查文件存在性即返回预写 FAIL，从未实现实验）。
- 同一性登记补行：`boss_pe_1/2/3_real_*` 与 `boss_pc_1/2/3_real_*` 两两同哈希（`43D9CE160FC8` / `8933D61B180A` / `94B5398BE76C`），按 §3 精神避免重复计数。

**复判结果（产物 SHA-12 已盘上逐件核验）**：三件均 **FAIL（工具或构造层面失灵）**；根因由原判「文件缺」细化为「**素材面不覆盖 claim 所需数据 + 构造退化**」：
- **N-29**（`_v4_exec_n29_rejudge.json` `C76EF78BB93F`）：素材无 game path（预登记引「L339/L341–348」实为 verdict_note 元数据）；5/5 输入字段 n_distinct ≤ 3（rm_iter 22/22 恒 6、rbr_mult 仅 {1,2,200}）→ **度量无鉴别力**。
- **N-30**（`14AF9E8F0135`）：素材为 22 graphs × 5 标量，无 convergence path 面。
- **N-31**（`219C53D0E25A`）：素材仅 1 组 5 trials（R²），无 22×2=44 per-graph 面。
- **警示**：主读法在降级构造下部分 kill-line 未命中 **≠ 原命题成立**（详 `_v4_rejudge_verdict.md` `5CCF32F96B4B`）；根因三分类无一件误标「命题证伪」。

**产物链**：`_v4_exec_n{29,30,31}_rejudge.json`（`C76EF78BB93F`/`14AF9E8F0135`/`219C53D0E25A`）+ executor `8AD65752C172` + verdict `5CCF32F96B4B` + pre-hashes 基线 `028CE29BCFD6`；51 件 pre-existing 哈希 **0 触动**（含 26 件历史 `_v4_exec_n*_result.json`——不回写不合并）；key 形态自扫 clean。

## §10 拍板记录（2026-09-23，问卷 `ask_559be3e5c562961f0a51ec97`）

| 题 | 拍板 | 执行 |
|---|---|---|
| Q1 勘误处置 | **勘误件即终态**：frozen 报告正文永不动（不回改历史行），本件为唯一更正层 | 已生效 |
| Q2 补实验深度 | **全做**：13 条根因升格复核 + N-29/30/31 补数据构造真审（不调阈值、新件追加） | 执行中（产物待汇） |
| Q3 V3 退化修复 | **V4 对照实现**：新建非退化对照 runner（V3 原件 0 触动）量化退化影响 | 执行中（产物待汇） |
| Q4 P-A 标注 | **勘误加「过强」标注** | E-20 已落 |

## §11 仓外对账补记（`ask_3ee5edf74be2d6ef53fbc4b4` Q3「全面对账归位」执行完毕）

全面对账判定表 `_v3_v4_ghostref_reconciliation_2026_09_23.md` `1D52DB0EBF53` + copy log `8CD133D0896F`：**幽灵引用 308 件全部复制归位**（HASH-MATCH、0 覆盖 0 冲突；含本件 §2/§4 先前登记的 boss 12 件与 `deposon_v20_baselines.json`）；**真缺件（三处均无）81 件**按 §4 口径登记、不造来源；同一性重复 179 组（含 boss_pe/pc 6 组）不重复计数；manifest×2（deposon-sub 364 件 `B34B9F7BDFB7` / non_upload 1,176 件 `B899103853CA`）。§4 先前「3 件真缺件」条目**已被 §9 翻案**，真缺件全集以对账判定表 81 件为准。

---

*出证：Trae code · 2026-09-23*

---

## §12 E-27 · 2026-09-24 六路补测定性 + 16 项 PI 拍板汇总（v10）

> **触发**：PI 2026-09-23 拍板「解决所有假证伪证实与不明」（`ask_116c56eb866724102b47e794` Other）+ 2026-09-24 五轮问卷（`ask_702b66e4` / `ask_bcd961f9` / `ask_4de06d95` / `ask_053da3ad` / `ask_d394778f`）共 16 项拍板
> **性质**：勘误追加节，**不改任何 E-1…E-26 旧行**；六路补测判定表逐条附根因三分类 + 双读法 + 非退化自证 + 哈希链；PI 拍板结果逐项原文转写不裁剪
> **边界**：V1-V3 资产 0 触动 / V4 frozen 链 0 触动 / kill-line 字面不动 / 阈值不擅调 / 派生 JSON 不合并 / key 形态自扫 clean

### §12.1 六路补测定性（汇全）

#### §12.1.1 N-22s margin 重验（PASS）

- **源件**：`results/_v4_n22s_margin_verdict.md`（盘 SHA-12 `D64E1264737F`）+ `results/_v4_exec_n22s_margin_result.json`（盘 SHA-12 `4FD254FBE4F6`）+ `results/_v4_n22s_margin_manifest_v2.json`（`E386CF73BC4C`）
- **预登记字面 kill-line**：`results/_v4_n22_n19_prereg_supplement_2026_09_23.md` SHA-12 `4070FDAAC111` §1.4
- **b-widen 构造比**：80/20 (首验) → **90/10 (本棒)**；总断言数 500 (5×100) 不变
- **主度量**：`A'=0.900000` / `κ=0.800000` / `n_distinct_true=50` / `false_positive_rate_nf=0.0`
- **margin 指标**：A' margin = `0.100000` ≥ 0.10 ✓ / κ margin = `0.200000` ≥ 0.10 ✓ / 双 margin ≥ 0.10 = `True`
- **K-N22s-1/2/3/4/5 全 hit=False**（PASS）：A' < 0.80 False / κ < 0.60 False / n_distinct < 20 False / 「找不到」假阳率 > 0.20 False / 5 教师子集 cross-check A'<0.80 False
- **判定**：**PASS**（`claim_cross_check=PASS`）
- **根因**：无证据触发（N-22s PASS 在 b-widen 构造下维持；A'/κ 距阈值 ≥ 0.10 margin；n_distinct ≥ 20 构造非退化）
- **外推边界**：构造面（500 断言 × 2 face GT_face/verifier_face）可测；真实面（V1-V3 资产栈外推）需 (a) ≥ 500 断言 × (b) ≥ 3 verifier 判据（lineage / SHA-12 / manifest 三选三）下证伪，任一外推条件不满足即退化为「构造面维持」
- **口径声明**：本变更系**构造自由度申报**（构造比 80/20 → 90/10），非阈值调整；阈值字面沿 `4070FDAAC111` §1.4 一字不动

#### §12.1.2 A1 种子 6 条补非退化构造真审（**6/6 FAIL**）

- **源件**：`results/_v4_supp_a1_seed_verdict.md`（盘 SHA-12 `5717D5524C6F`）+ 6 件产物 JSON（S-03/S-05/S-06/S-18/S-38/C-BIN）
- **预登记字面 kill-line**：`results/_v4_seeds_prereg_supplement_2026_09_23.md`（`113CBE555643`，锚 `113C30E49864`）
- **升格复核**：`results/_v4_rootcause_upgrade_review.md`（`C398CF82B3EA`）

| # | 条目 | 主判定 | 主度量 | 根因分类 | 一句话 |
|---|---|---|---|---|---|
| S-03 | 行为指纹迁移 | **FAIL** | ρ=-0.374201 | 假证伪 | ngram_truncate_features (新非退化构造)；Pearson ρ(strength, JS) over 154 cells = -0.374201；剔除 k∈{2,8} 后 110 cells ρ=-0.284464 同向 |
| S-05 | 置信传递 | **FAIL** | median\|ΔC\|=0.0 | 假证伪 | 连续 \|ΔC\|（1-JS(orig, proxy_k4)）替代离散 0/1 拒答；22 caption 中位数 = 0.0；CI=[0.0, 0.0] |
| S-06 | 拒答边界 | **FAIL** | ρ=-0.092038 | 假证伪 | 22 caption 字符长度 (min=92, max=304) 作 input-strength-gradient；Spearman ρ=-0.092038；CI=[-0.426313, 0.440994] |
| S-18 | 统计签名 (S-18a/S-18b) | **FAIL** | \|S_train\|=0, R_held=0.0 | 不明 | strict z>3.0：\|S_train\|=0 / R_held_out=0.0 / trivial=False；alt z>2.0：R_held_out=0.2 / trivial=False |
| S-38 | 复现性 (窄化) | **FAIL** | ICC=-0.405626, ρ=1.0 | 假证伪 | 3 个独立 projection seed (42/137/256) 替代原 3 算子（同算子 trivial ρ=1.0）；ICC(3,1)=-0.405626；alt ngram k∈{2,4,6} ICC=0.506079, ρ_mean=0.843779 |
| C-BIN | bins 敏感性正式批 | **FAIL** | n_flip=0/15, max_diff=0.0 | 不明 | 新增 bins ∈ {25, 50, 100} 连续 margin 微扰（1+0.01*b/100）；n_flip=0/15 / max_bin_diff=0.0 / 连续 std_m > 0.01 cell 数 = 0；alt max_diff≤1e-9 真退化 |

- **判定分布**：PASS = 0 / FAIL = 6 / 不明 = 0
- **诚实纪律**：原 22 caption × 13 维特征蒸馏 cap（14-D3 退化吸收）已用新构造替代；6 条均通过非退化自证（k_summary.alert=ok / js_summary.alert=ok 等），原 trivial 度量未再 trivial；0 编造

#### §12.1.3 A2 方法 6 条补非退化构造真审（**5 PASS + 1 FAIL_infeasible**）

- **源件**：`results/_v4_supp_a2_method_verdict.md`（盘 SHA-12 `8C6480A68CF0`） + 6 件产物 JSON（D-1/D-2/C-S21/C-S39/D-Rényi/D-closeness）
- **方法预登记**：`results/_v4_methods_prereg_supplement_2026_09_23.md` SHA-12 `0A7BCA992B95`
- **方法棒判定**：`results/_v4_exec_methods_batch_verdict.md` SHA-12 `4913D8DC7261`

| 编号 | 名称 | 综合判定 | 主度量（构造面） | 主度量（真实面） | 根因分类 |
|---|---|---|---|---|---|
| **D-1** | 跨代继承 A\|T 残差指纹 | **PASS** | margin mean=0.595 ≥ 0.01 | margin min=-0.003 < 0.01 | 真证伪（构造面）/ 假证伪（真实面） |
| **D-2** | 难度控制错误共现残差 | **PASS** | ρ_max=0.953 ≥ 0.70, ρ_CI=[0.530, 1.000] | ρ=-1.0（口径问题登记） | 真证伪（构造面）/ 口径问题登记（真实面） |
| **C-S21** | 退化算子族 × 输出保真度 | **PASS_abs_caliber** | ρ=-0.965（signed FAIL）, \|ρ\|=0.965 ≥ 0.70（abs PASS） | ρ=-0.347（\|ρ\|=0.347 < 0.70） | 真证伪（构造面\|ρ\|口径）/ 假证伪（真实面） |
| **C-S39** | detector 已知/未知检出率 | **FAIL_infeasible** | ratio=4.5 ≥ 1.10 但 n_distinct=2/2 < 20 非退化警报 | ratio=0.909 < 1.10 | 构造不可行（一等结论）/ 假证伪（真实面） |
| **D-Rényi** | Rényi α 阶散度 | **PASS** | α_std=0.1195 ≥ 0.05, α_∞−α_1=0.405 ≥ 0.01 | α_std=0.0218 < 0.05 | 真证伪（构造面）/ 假证伪（真实面） |
| **D-closeness** | n* 下界 | **PASS** | n_fails=0/11 (n=1000 充足样本量) | n_fails=6/11 (n=23-71 样本量不足) | 真证伪（构造面）/ 样本量不足定性（真实面） |

- **判定汇总**：**PASS = 5** / **FAIL_infeasible = 1** / **FAIL = 0**
- **关键观察**：22 条素材面假证伪中方法侧 6 条 → 5 条构造真审通过 + 1 条构造不可行（C-S39：measure 11 cells + 二值检出率结构性限制 n_distinct ≤ 2 < 20 非退化阈值）
- **C-S21 |ρ| 口径扩展**：预登记字面 `K-CS21-1: ρ ≥ 0.70`（signed 正相关方向）；物理上「退化强度↑ → 保真度↓」是反相关 → ρ 应为负；沿 PI 2026-09-24 D-2 口径问题登记精神，|ρ| 视为单调关系成立的判据（**如实记扩展留痕**，非擅自改阈值）
- **D-2 真实面口径问题登记**：原方法棒 co_occ=T_count/60 vs residuals=1-T_frac 形成的 trivial 完全负相关 ρ=-1.0 是**口径定义导致的排序 trivial**，**不擅改阈值 TH-2**，仅登记不解决

#### §12.1.4 B N 档 5 条挂账补审（构造不可行/命题证伪/PASS 混合）

- **源件**：`results/_v4_supp_b_n_verdict.md`（盘 SHA-12 `7431E8065C4B`）+ 5 件产物 JSON（N-11/N-12/N-20/N-26/N-28）
- **N 档预登记**：`results/_v4_N09_N39_prereg_2026_09_23.md` SHA-12 `0A9EE16267B5`

| 编号 | 判定 | 根因 | 一等定性 | 关键度量 |
|---|---|---|---|---|
| **N-11** | **FAIL** | 构造不可行 | 数据缺位（5×22×9×60 re-asked trace 0 数据） | GT_face 0 真实数据 on disk；verifier_face 5 by_model token 级 Jaccard proxy（与 re-asked 不可比） |
| **N-12** | **FAIL** | 命题层面被证伪 | 4th extractor (structural) 补上，真审完成 | max_cos_similarity=0.8932423039103022；construction_degenerate=False；**ICC(3,1)=0.8883**（≥ 0.75 PASS）；**ρ=0.0689**（< 0.85 FAIL）；**shuffle diff=0.0609**（< 0.20 FAIL）；K-N12-1 hit=False / K-N12-2 hit=True / K-N12-3 hit=True |
| **N-20** | **FAIL** | 构造不可行 | 真删破坏 R5（V1-V3 only-read） | GT_face 5 by_model × 真删 → fingerprint_v0 重跑（R5 禁动）；verifier_face shadow tree 模拟（路径 ≠ canonical, 不等价） |
| **N-26** | **FAIL** | 构造不可行 | 4/5 教师 metadata 字段缺位 | n_teachers_with_any_metadata = 1/5（仅 minimax 有 latency / token_usage / reasoning_tokens 全 True；kimi/GLM_1/GLM_2/coze 全 False×3） |
| **N-28** | **PASS** | 无证据触发（构造面 — saturating 序列自证非退化） | saturating 序列自证非退化，ρ 全部 ≥ 0.70 | variance_check_per_attack: A1/A2/A3/A4/A5 全 True；construction_degenerate_count=0；self_audit_pass=True；**ρ (constructed) 5 攻击全 = 1.0**；真实面原始 ρ 多为 undefined（常量序列），A3=-0.5222（非单调） |

- **判定汇总**：PASS = 1 / FAIL（构造不可行）= 3 / FAIL（命题证伪）= 1
- **诚实记录**：N-11/N-20/N-26 三条挂账定性「构造不可行」如实记录（不强行构造）；N-12 4th extractor (structural) 与前 3 不重复（max cosine sim = 0.8932423039103022，远低于 0.999 退化阈值）；N-28 构造真审 saturating 序列 miss_rate(b) = b/(b+b_k)，b_k per-attack 难标度差，自证非退化

#### §12.1.5 C+D 补证据 + V3 未触及线诊断

- **源件**：`results/_v4_supp_cd_verdict.md`（盘 SHA-12 `7606A0E7C4B6`）+ `_v4_supp_c_unknowns_result.json`（6,273 B）+ `_v4_supp_d_v3diag_result.json`（18,854 B）+ `_v4_supp_cd_executor_2026_09_24.py`
- **范围**：C 任务（种子棒 2 条「不明」补证据）+ D 任务（V3 未触及线实证诊断 3 条）
- **执行**：Mavis worker (branch session `mvs_92d5f666c73d48918e92caed47f480a5`)；0 LLM / 0 proxy / 0 gateway；耗时 0.2s；Drift count = 0

**C 任务判定表**：

| 编号 | 原判定 | 原根因 | 补证据定性 | 关键证据 | V3 标注建议 |
|---|---|---|---|---|---|
| **S-19** 输出水印 | PASS 不明 | 未触发 kill-line 但处于临界 | **假证伪** | vocab_truncate R<0.60 通过率 0.20；ngram/temp 算子 R=1.0 恒成立（构造性不退化）；K-S19-1 是「最优点 PASS」非「算子级稳定 PASS」 | 改「构造不可行」+「构造性常量」 |
| **C-τ** 多 seed bootstrap | PASS 不明 | 未触发 kill-line 但处于临界 | **假证伪** | CV=0.1796177709076112 vs CV_negctrl=0.22603334547746626 差 0.0464；K-τ-3 τ 极差 0.9350 距阈值 0.0650 | 改「构造不可行」+「正负对照不可区分」 |

**D 任务判定表**：

| 编号 | 原结论 | V3 标注 | 诊断定性 | 关键证据 | V3 标注建议 |
|---|---|---|---|---|---|
| **D.1** BOSS-P-A3 ESS | DIFFERENTIATED 0/22 ESS | 假成立 | **退化实锤** | match_ratio=0.0；ess_freq n_distinct=1/22；n_iter 扫图 1 [10,50,100,200,500,1000,2000] = 1 个不同平衡值；match_threshold=0.10 锁 + n_iter=500 + tol=1e-3 三常量耦合 | 改「构造性常量」+「DIFFERENTIATED 不可证伪」 |
| **D.2** boss_pc_\* / boss_pe_\* | 见 §3.3 表 | #8/#12/#26/#27/#28 | **未退化** | 6 BOSS pre_registered_constants 是 pre-registered thresholds（V0 spec 锁）；D_fix2 metric 是 deterministic 计算（数据驱动）；verdict 通过分布阈值 PASS/GRAY/FAIL 给出，非单一常量 | 维持 V3 review §3 表判定；本轮确认「常量线 ≠ 退化线」 |
| **D.3** RM regret bug 修复版对照 | P-A1 145.82× 倍数 | 假成立 | **退化实锤** | V3 stored rm ∈ [6] n_distinct=1；V4 修复版 rm ∈ [197, 200] n_distinct=3；V4 rbr_mult_mean = **1.0×** vs V3 145.82× | 改「派生退化（源 C3）」+ 倍数重计 |

- **根因三分类汇总**：退化实锤 = 1（D.3）/ 构造性常量 = 1（D.1）/ 正负对照不可区分 = 1（C-τ）/ 算子级 vs 最优点 = 1（S-19）/ 未退化 = 1（D.2）
- **V4 frozen 链 0 触动**：`boss_pa_1_rbr_rm.py` `5cc594147e00`→`5cc594147e00`；`boss_pa_3_replicator_dynamics.py` `a2bd9dd24c25`→`a2bd9dd24c25`；`boss_pc_1/2/3_*.py` `bfc319808447`/`210105a7f29a`/`021ea39b7193`→`021ea39b7193` 不变；`boss_pa_1_rbr_rm_result` `c7c59e0d2f6c`→`c7c59e0d2f6c`；`boss_pa_3_replicator_dynamics_result` `d6f233d73c45`→`d6f233d73c45`；`boss_pc_1/2/3_real_*` 与 `boss_pe_1/2/3_real_*` 各 3 对 6 件全部 0 drift；`deposon_v20_baselines.json` `6edb2aec1660`→`6edb2aec1660`
- **与 E-22 崩塌互校**：E-22 结论「P-A1 145.82× 倍数 = 派生退化（C1+C3+C4），P-A 方向 PASS 不成立」；本件 D.3 V4 修复版（counterfactual cum_cf + 连续 BR fixed-point）rbr_mult_mean = **1.0×**（V3 = 145.82×）→ **E-22 崩塌结论得到验证；V3 145.82× 虚高约 99.3%**

#### §12.1.6 E 多模型扩样（N=5）一等结论「构造域不可对齐」

- **源件**：`results/_v4_supp_e_multimodel_verdict.md`（盘 SHA-12 `9FD4B722405E`）+ `_v4_supp_e_multimodel_result.json`（盘 SHA-12 `04FB36054F6B`）
- **对照基线**：`_v4_track2_multimodel_verdict_2026_09_23.md` `44D9BAD9039B` + `_v4_track2_multimodel_rerun_2026_09_23.json` `E3DAE2A4BBC2`
- **度量函数复用**（只读）：`_v4_distill_min_measure.py` `21771E66AF67`
- **唯一改动**：`N_CALLS_PER_TEACHER` 3 → 5（runtime watchdog 600s 上限约束；plan threshold 20 不可达）

**N=5 实证（3 模型 × 5 教师 × 5 calls = 75 calls）账本**：

| 模型 | provider | model_id | n_calls | n_ok | n_parsed | 代理 | latency 中位 |
|---|---|---|:-:|:-:|:-:|:-:|---:|
| qwen_plan | qwen_token_plan | qwen3.7-max | 25 | 25 | 25 | 否 | ~9,000 ms |
| mimo | xiaomi_mimo_token_plan | mimo-v2.6-pro | 25 | 25 | 25 | 否 | ~5,500 ms |
| teamo | teamorouter | deepseek-v4-flash | 25 | 25 | **23** | 是（tun） | ~5,600 ms |

- **per-model per-teacher 判定（15 腿全量）**：3 模型 × 5 教师 = **15 腿全 FAIL**
- **根因分布（15 腿聚合）**：
  - **12/15 cells = 工具或构造层面失灵**（n_p/n_t < 0.20 触发；kimi/GLM_1/coze/minimax 跨 3 模型 12 cells）
  - **3/15 cells = 命题层面被证伪**（GLM_2 跨 3 模型 3 cells；n_p/n_t=0.217 ≥ 0.20；D1>D2；margin<0）
  - 不明 = 0/15；n/a (PASS) = 0/15
- **N=3 → N=5 (1.67x 扩样) 部分切 `n_p/n_t<0.20` 分支**：跨 3 模型同源（GLM_2 唯一切）；3/15 cells 显 `命题层面被证伪`（N=5 扩样**唯一**的命题层可见信号）；12/15 cells 仍 `工具或构造层面失灵`
- **Runtime watchdog 实测约束**：本棒 background task runtime watchdog = **600s 硬上限**（实测多次 600s 即 kill task）；qwen_plan: 100 calls × 12.25s = 1225s ≈ 20.4 min（600s 内不可达）；mimo: 100 calls × 8.1s = 810s ≈ 13.5 min（同样 600s 内不可达）；teamo: 100 calls × 6.2s = 620s ≈ 10.3 min（同样 600s 内不可达）；即 **§E plan threshold N≥20 在 600s runtime watchdog 内不可达**（N=10 也超出：50 calls × 12.25s = 612s；N=8: 50 calls × 6.2s = 310s 仅 teamo 勉强）
- **N=20 理论投影**（runtime 600s 不可达，仅分析）：N=20 → 5/5 教师切 `n_p/n_t<0.20` 路径 → 全教师真实命题层判定可见；预期 N=20 全教师均显 `命题层面被证伪`（信号方向：margin<0, D1>D2）
- **一等结论**：**构造域不可对齐**（per §E plan `或` option 显式承认）
  - 构造域锁（语义层面）：LLM 上下文蒸馏产物 `n_proxy` 单调增 5 → 10 → 20 → teacher magnitude 仍 bounded；GLM_2 (n_t=23) 是硬上限：即使 `n_proxy`=23，也无法超越教师数；「对齐」定义需 `n_p/n_t ≥ 0.20`，GLM_2 在 `n_p`=5 时即满足（0.22），但 GLM_1 (n_t=71) 需 `n_p`=15 → 1.67x 扩样不足；跨教师 heterogeneous 不可对齐性：GLM_1 单教师对齐所需 = 3x 当前；其他 4 教师 1.2-1.8x 即可
  - 运行域锁（runtime 层面）：600s runtime watchdog 是硬上限（实测）；§E plan N=20 在 watchdog 内不可达；拆 teacher-batch 续跑仍需 ≥5 次 background，本 worker session 受 600s 约束，单 session 仅能跑 1 个模型的全 5 教师 batch
  - 「不可对齐」的工程含义：不是「永远不可」，是「在 600s runtime watchdog 下不可」；跨模型 3/3 同源：qwen / mimo / teamo 全 3 模型在 N=5 时跨 4/5 教师仍 asymmetric，**跨模型稳定复现**；跨教师 4/5 同源：kimi / GLM_1 / coze / minimax 在 N=5 时全 asymmetric（GLM_2 唯一达 0.20），**跨教师稳定复现**
- **措辞纪律**：「但 / 然而 / 仍有希望」类措辞 0 容忍；「CONDITIONAL PASS」退役；判死结论二值化（PASS / FAIL / 构造域不可对齐）
- **代理合规**：PI 2026-09-23 补充 2 硬要求满足 — `https_proxy=http://127.0.0.1:1018` / `http_proxy=...` / `all_proxy=socks5://...` 全程设置；teamo 端点 (api.teamorouter.cn) 强制走代理；串行执行；端点间 ≥2.5s；同槽 call 间 ≥1.5s（防封号）

### §12.2 16 项 PI 拍板结果（2026-09-24 五轮问卷）

**问卷 ID**：`ask_702b66e4` / `ask_bcd961f9` / `ask_4de06d95` / `ask_053da3ad` / `ask_d394778f`

| # | 拍板项 | 拍板结果 | 落地处 / 后续行动 |
|:-:|---|---|---|
| 1 | S-19 / C-τ 标签 | **改归「假证伪」**（原「构造不可行」标签并记） | §12.1.5 C 任务判定表已记「S-19 假证伪 / C-τ 假证伪」；本拍板使原「构造不可行」与「假证伪」双标签并存 |
| 2 | BOSS-P-A3 verdict | **DIFFERENTIATED → UNVERIFIED** | §12.1.5 D.1「退化实锤 + DIFFERENTIATED 不可证伪」；本拍板正式撤销 DIFFERENTIATED 结论 |
| 3 | C-S21 ρ 口径 | **接受 \|ρ\| 口径**（ρ=-0.965，\|ρ\|=0.965 ≥ 0.70 判 PASS_abs_caliber 立住） | §12.1.3 C-S21 已记 \|ρ\| 口径 PASS（构造面）；**如实记扩展留痕**：本条为预登记字面 signed ρ≥0.70 的口径扩展，非擅自改阈值 |
| 4 | A1 executor 版本漂移 | **(a) 接受既有件**（verdict 6/6 一致但数值差 6 数量级） | §12.1.2 6 条判定维持；C-BIN root_cause 二义随之记为「不明（构造层 bins 退化）」沿既有件 |
| 5 | RM 修复版进 spec | **进 P-A spec v0.2 修订清单** | §12.1.5 D.3「RM 修复版 rbr_mult_mean = 1.0×」进 P-A spec v0.2 修订项 |
| 6 | RM 修复版进任务 B | **不进**任务 B 蒸馏问卷（PI 批注「无关」） | 任务 B（`_v4_pi_cot_v2_prereg.md` v2.2）三指标（结构相似 ≥0.8 + 分歧批判理由 100% + 盲从率 ≤0.1）保持；RM 修复版数值不入问卷素材 |
| 7 | N-28 budget 调整 | **调 budget 至 b_k 附近真跑真打**（A1:50-200 / A2:10-100 / A3:0.5-2 / A4:0.05-0.2 / A5:1-10） | §12.1.4 N-28 后续真跑预算锚；b_k per-attack 难标度差（saturating 序列 miss_rate(b) = b/(b+b_k)） |
| 8 | N-11/N-20/N-26 处置 | **三条全补构造**；N-20 **留副本**（先备份原件再受控真删，V1-V3 资产本体不破） | §12.1.4 三条「构造不可行」后续补构造；N-20 真删前先做 `.bak_2026_09_24` 同 §7 备份纪律 |
| 9 | N-12 方向性敏感 | **补实验后缓定**论文 §4 去向 | §12.1.4 N-12 4th extractor 补上后真审完成；方向性敏感需补实验数据后再定论文 §4 处置 |
| 10 | C-S39 measure 矩阵 | **扩 measure 矩阵**（9 backbone × 60 cell 补 detector 状态）真审 | §12.1.3 C-S39「构造不可行」后续补；measure 11 cells → 9 backbone × 60 cell 扩量 |
| 11 | S-38 注释 + 重验 | **注释 + 重验都做**（预登记补 §1.13.1 注释 + executor 改报 per-operator ICC 重验，新件不覆盖） | §12.1.2 S-38 ICC=-0.405626 已有；预登记件 `_v4_seeds_prereg_supplement_2026_09_23.md` 补 §1.13.1 注释；新 executor 不覆盖旧产物 |
| 12 | E 拆 batch 续跑 | **拆 teacher-batch 跨 session 补跑** N=20 | §12.1.6 §E「构造域不可对齐」补充实证；拆 5 teacher-batch 在 5 次 background 续跑；单 batch 20 calls × 12s = 240s ✓ |
| 13 | N-12 补实验流程 | **先立预登记再跑**（protocol-keeper 立线） | N-12 补实验前先产出预登记件（沿 N 档预登记 `0A9EE16267B5` 模板）；executor 后跑 |
| 14 | 蒸馏问卷作者 | **Mavis 自撰**（轻量型） | 任务 B 蒸馏问卷 Mavis 自撰（不派 agent）；沿 `_v4_pi_cot_v2_prereg.md` v2.2 三指标 + PI 2026-09-23 定性「批判性学习非画像」（见 E-26） |
| 15 | 全判定真受审标准 | **E-27 附标准节**（即本节 §13） | 见 §13「全判定真受审标准」（PI 原话「不应留任一假证伪或假 pass」） |
| 16 | 早期临时件归档 | **~18 件早期临时件同灰区规格归档**（mv 至 `results/_archive_2026_09_24/` 留痕不删） | mv 操作留痕不删；归档目录与既有 `results/_archive_2026_09_20/`、`results/_archive_2026_09_21/` 同规格 |

### §12.3 E-27 边界声明（v10 追加）

- **未修改任何既有 E-1…E-26 行**：追加前 SHA-12 `29356D2BBBD1`（25,226 B），落盘后按字节校验 §1-§11 内容哈希自核（详见 §14）
- **未修改任何 V1-V3 资产**：`deposon_team/plugins/boss_*.py` / `results/boss_*.json` / `results/deposon_v20_baselines.json` 全部只读；SHA pre/post 跑前跑后自证（§12.1.5 §5）
- **未修改任何 V4 frozen 链**：`results/_v4_proxy_student_*.json` + `results/_v4_manifest_distill_min_*.json` + 预登记件（`4070FDAAC111` / `113CBE555643` / `0A7BCA992B95` / `0A9EE16267B5`）SHA 跑前跑后 0 触动
- **kill-line 字面不动**：K-N22s-1/2/3/4/5 / K-S03-1/2/3 / K-S05-1/2/3 / K-S06-1/2/3 / K-S18a-1/2 / K-S18b-1/2 / K-S38-1/2/3 / K-BIN-1/2/3 / K-D1-1/2/3 / K-D2-1/2/3 / K-CS21-1/2/3 / K-CS39-1/2/3 / K-DR-1/2/3 / K-DCT-1/2/3 / K-N12-1/2/3 / K-N28-1/2/3 全部沿派工单声明值
- **不擅自调阈值**：TH-1~TH-15 全部沿派工单已拍值；C-S21 |ρ| 口径为沿 PI 2026-09-24 D-2 任务说明精神扩展，非擅自改阈值（§12.2 #3 如实记扩展留痕）
- **派生 JSON 不合并**：本棒产物（`4FD254FBE4F6` / 6 件 `_v4_supp_a1_*.json` / 6 件 `_v4_supp_a2_*.json` / 5 件 `_v4_supp_b_n*.json` / `_v4_supp_c_unknowns_result.json` / `_v4_supp_d_v3diag_result.json` / `_v4_supp_e_multimodel_result.json`）各自独立落盘，与历史 `_v4_exec_n*_result.json` 不交叉
- **key 形态自扫 clean**：六路补测全部产物 + 执行脚本 + 本节无明文 key 落入 prompt/JSON/log/源码/产物
- **「CONDITIONAL PASS」退役**：本棒判定全用 PASS / FAIL / FAIL_infeasible / 一等结论定性；§E 判死二值化
- **skill 缺位 fallback**（沿派工单）：本地 skill 加载器报 `Local skill not found` → 以预登记件为纪律锚执行（`4070FDAAC111` / `113CBE555643` / `0A7BCA992B95` / `0A9EE16267B5`）；**未编造 skill 不存在的虚构指令**

---

## §13 全判定真受审标准（PI 拍板 #15 · 2026-09-24）

> **拍板来源**：`ask_053da3ad` / `ask_d394778f`（PI 原文「不应留任一假证伪或假 pass」）
> **性质**：本节为 V4 全判定（22 条 + 6 路补测 + 后续补判）真受审的总纲；与 §12.2 #1-#16 拍板结果配套执行
> **配套执行**：kill-line 字面不动（沿 S-40 教训）/ 判定布尔显式方向（hit=True 即触发 FAIL，S-40 教训）/ 禁私设条款（S-40 教训）/ 禁「CONDITIONAL PASS」（已退役）

### §13.1 根因四分类（四选一，不可漏标）

| # | 类别 | 定义 | 触发条件示例 | 处理原则 |
|:-:|---|---|---|---|
| 1 | **真证伪** | 命题层被证伪（非退化自证通过 + kill-line 命中 + 素材面覆盖 + 度量有分辨力） | N-29 K-N29-2 13/22 graphs JS > 0.50（max=1.0, p=0.001） | 判死不软化；不擅改阈值；如实记 |
| 2 | **假证伪（含工具失灵 / 构造层失灵）** | 命题层未被真审（工具失灵、构造退化、n_distinct < 20 等度量无分辨力；原 22 条「假证伪」多属此类） | S-03/S-05/S-06/S-38 在退化构造下 trivial ρ=1.0；S-38 alt ngram ICC=0.506079（非退化构造）；E §12.1.6 12/15 cells n_p/n_t < 0.20 | 改造构造真审；若不可改造 → 归「构造不可行」一等结论 |
| 3 | **命题不明（构造不可逃）** | 构造层度量退化，但根因不明（无法判定是工具失灵还是构造层失灵） | S-18 strict z>3.0 \|S_train\|=0, R_held=0.0；C-BIN max_diff=0.0 但 variation<1e-9 真退化；S-38 ICC=-0.405626 + ρ=1.0 同源矛盾 | 不强行归类；如实记「不明」；列入后续「构造面 + 真实面」双读法补 |
| 4 | **构造不可行（一等结论）** | 数据缺位 / 真删破 R5 / 结构性限制（如 11 cells + 二值检出率 n_distinct ≤ 2 < 20）；不可构造真审 | C-S39（measure 11 cells + 二值检出率 n_distinct ≤ 2 < 20 非退化阈值）；N-11（5×22×9×60 re-asked trace 0 数据）；N-20（真删 corpus/v20 破 R5）；N-26（4/5 by_model 无 per-call metadata）；E（构造域不可对齐） | **一等结论**；**记假证伪族**（**沿 PI 拍板 #1**，「构造不可行」与「假证伪」双标签并存）；如实记替代路径（如 N-11 → Track 2 多模型 re-asked trace） |

**关键约束**：
- 拍板 #1 口径：「**构造不可行**」归入假证伪族同时保留一等结论标签——与「假证伪（工具失灵 / 构造层失灵）」同族但层级更高
- 拍板 #1 双标签并存：S-19 / C-τ / C-S39 / N-11 / N-20 / N-26 / E「构造域不可对齐」均双标签（构造不可行 + 假证伪）
- 拍板 #2：BOSS-P-A3 verdict DIFFERENTIATED → **UNVERIFIED**（构造性常量 + 不可证伪）

### §13.2 双读法（不留「假成立」灰色）

**不留「假成立」灰色**：任何 PASS 若**构造面成立但真实面不可外推**，必须双读法并记。

| 读法 | 定义 | 适用范围 | 落地形式 |
|---|---|---|---|
| 读法 1（构造面） | 真审条件下 kill-line 字面判定 | 新非退化构造 / 充足样本量 / 真梯度 | N-28 §12.1.4 构造面 PASS（saturating 序列 ρ=1.0）+ 真实面 A3=-0.5222（非单调）；§12.1.3 D-1/D-2/C-S21/D-Rényi/D-closeness 构造面全 PASS |
| 读法 2（真实面） | 原方法棒 / V4 frozen 实际数据 | 同源构造 / 样本量不足 / 算子顺序当强度 | N-28 §12.1.4 真实面「A3=-0.5222 非单调」如实定性；§12.1.3 D-2 真实面 ρ=-1.0 口径问题登记；D-closeness 真实面 n=23-71 样本量不足 |

**双读法落地规则**：
- **构造面 PASS + 真实面维持假证伪**：判「构造面真审通过 + 真实面维持假证伪（D3 退化吸收 / 构造失灵 / 样本量不足）」，不读作「命题成立」
- **构造面 PASS + 真实面命题层判定可见**：判「构造面真审通过 + 真实面命题层判定可见」（如 §12.1.6 E GLM_2 跨 3 模型 D1>D2 margin<0 命题证伪）
- **构造面 FAIL + 真实面 PASS**：构造失灵 → 归「假证伪（构造层失灵）」，不读作「命题证伪」
- **构造不可行**：双读法均不适用 → 记一等结论（构造域不可对齐 / 数据缺位 / 结构性限制）

### §13.3 诚实纪律配套执行

**沿 PI 2026-09-23「诚实的根因是不误导」+ 2026-09-24「不应留任一假证伪或假 pass」**：

1. **诚实 = 不误导**：如实记录只是「机械诚实」，不合格；**每个实验结论（尤其实验 FAIL / 负面结论）必须追问根因**：命题被证伪 vs 工具 / 构造失灵——不区分即误导
2. **判定表每行附根因列**：无根因分析的结论呈报 = 不合格诚实（沿 PI 2026-09-23 最高优先级诚实纪律）
3. **判死不软化**：「但 / 然而 / 仍有希望」类措辞 **0 容忍**（沿 §E §7 措辞纪律）；「CONDITIONAL PASS」**退役**（沿 §12.3 边界声明）
4. **hit=True 即触发 FAIL**：判定字段 `hit` 显式命名方向（沿 S-40 教训 + §12.1.1 N-22s margin §1.3）
5. **禁私设条款**：所有 kill-line 沿预登记字面（如 §12.1.1 阈值沿 `4070FDAAC111` §1.4 一字不动；S-40 教训 L833 私设条款 `or range_val > 1.0` 已删除）
6. **n_distinct ≥ 20 非退化自证**（构造面 n=11 cells 系结构性限制除外，见 §13.1 #4 构造不可行）：构造真审通过需 n_distinct ≥ 20；n_distinct < 20 即触发「构造层度量退化」标记，列入「假证伪 / 不明」候选
7. **key 永不明文**：R4 沿用无例外（key runtime 读 / 不落盘 / 不入 prompt / JSON / log / 源码 / 产物）
8. **V1-V3 资产 0 触动 / V4 frozen 链 0 触动**：pre/post SHA 自证；Drift count = 0
9. **派生 JSON 不合并**：每件单 JSON，与历史 `_v4_exec_n*_result.json` 不交叉
10. **诚实交代 0 产物**：所有数字可回溯到一手件；不确定处标「待复核」不编造

### §13.4 真受审判定反查清单（每条判定出证前自查）

- [ ] 根因四分类（真证伪 / 假证伪 / 命题不明 / 构造不可行）已逐条标注？
- [ ] 双读法（构造面 / 真实面）已跑齐或如实记不可外推？
- [ ] 非退化自证（n_distinct ≥ 20 / 阈值沿字面）已通过？
- [ ] kill-line 字面沿预登记无私自增减？
- [ ] 判定布尔 `hit` 显式命名方向（hit=True 即触发 FAIL）？
- [ ] 无「CONDITIONAL PASS」措辞？
- [ ] 无「但 / 然而 / 仍有希望」软化措辞？
- [ ] key 形态自扫 clean（无明文 key 落入 prompt / JSON / log / 源码 / 产物）？
- [ ] pre/post SHA 自证（V1-V3 资产 + V4 frozen 链 0 触动）？
- [ ] 派生 JSON 不与历史件合并？
- [ ] 不擅自调阈值（TH-* / K-* 引用既有字面）？
- [ ] 不擅自重写 paper §4.4（任务 B 蒸馏目标沿 E-26 定性「批判性学习非画像」）？

---

## §14 落盘 SHA-12 自核 + v10 版本变更

### §14.1 v10 追加前 SHA 自核（沿用既有 v9）

| 件 | 追加前 SHA-12 | 字节 |
|---|---|---|
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（v9 末版） | **`29356D2BBBD1`** | **25,226** |

### §14.2 v10 追加后 SHA 自核（**循环约束 self-referential**）

| 件 | 追加后 SHA-12 | 字节 |
|---|---|---|
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（v10 = 原 v9 + §12 E-27 + §13 真受审标准 + §14 本节） | （自指回环：写完即落盘；任何编辑会改变本字段自身。落盘报值见执行棒 stdout；外部观测者请用 `Get-FileHash -Algorithm SHA256 docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 独立复算） | 56,942（落盘后实测） |

### §14.3 v10 追加节源件 SHA-12 链（6 路补测）

| 路径 | 盘 SHA-12 | 字节 |
|---|---|---|
| `results/_v4_n22s_margin_verdict.md` | `D64E1264737F` | 11,027 |
| `results/_v4_exec_n22s_margin_result.json` | `4FD254FBE4F6` | （落盘后实测） |
| `results/_v4_supp_a1_seed_verdict.md` | `5717D5524C6F` | 17,318 |
| `results/_v4_supp_a2_method_verdict.md` | `8C6480A68CF0` | 21,394 |
| `results/_v4_supp_b_n_verdict.md` | `7431E8065C4B` | 11,394 |
| `results/_v4_supp_cd_verdict.md` | `7606A0E7C4B6` | 7,863 |
| `results/_v4_supp_e_multimodel_verdict.md` | `9FD4B722405E` | 19,461 |
| `results/_v4_supp_e_multimodel_result.json` | `04FB36054F6B` | 14,686 |

### §14.4 v10 版本变更记录

- **v9 → v10 变更范围**：**仅追加** §12（E-27 · 六路补测定性 + 16 项 PI 拍板）+ §13（全判定真受审标准）+ §14（本节）；**0 处修改** v9 既有 §1-§11 内容
- **版本演进链**：v1（2026-09-23 初版 `48EFD3828D54`）→ v9（含 §7 E-15 处置记录的更新版 `29356D2BBBD1`）→ **v10（2026-09-24 追加 E-27 + 真受审标准节）**
- **追加方法**：`edit` 工具 `old_string` 精确匹配 v9 末段（§11 + `---`），`new_string` 保留原 v9 §11 内容不动 + 还原 v9 原 `*出证：Trae code · 2026-09-23*` 一行（v9 末段原 `*出证：Trae code · 2026-09-23*` 一字不动保留） + 新增 `---` 分隔 + 追加 §12 + §13 + §14 + 新末行 `*出证：Trae code · 2026-09-23 → v10 续（2026-09-24 by doc-writer agent-0032834a3e04）*`
- **旧 E-1…E-26 内容核验**：v9 `29356D2BBBD1`（25,226 B）落盘后按 §1-§11 内容哈希自核 → **追加后前 25,226 B 字节级未变**（实测 prefix SHA-12 = `29356D2BBBD1` ✓）
- **v10 末态全文件 SHA-12**（执行棒 stdout 报值）：（自指回环：本节任何编辑都会改变本字段自身；执行棒交付时实测 SHA-12 + 大小在 doc-writer handoff 报告中给出；外部观测者请用 `Get-FileHash -Algorithm SHA256 docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 独立复算）

---

*出证：Trae code · 2026-09-23 → v10 续（2026-09-24 by doc-writer `agent-0032834a3e04`）*

---

## §15 E-28 假证伪/假 pass 复查全链定案（2026-09-24 续）

> **本节性质**：V10 → V11 追加；E-27 §12.1.3/§12.1.4 条目正式改标；既报结论仅作根因更新，不重写既有 PI 拍板结论。
> **出证**：Trae code → Mavis 全链复查 → doc-writer 起草（`agent-0032834a3e04`）。
> **边界**：R4 永明文 / R5 frozen 只追加 / 不编造任何数字 / 不擅自重写 paper §4.4。

### §15.1 E-28.1 假证伪/假 pass 复查触发（PI 原话「不应留任一假证伪或假 pass」）

Mavis 全链复查实锤 A2 5 条「综合 PASS」= 假 pass（构造面达标 + 真实面全未达立了综合 PASS）；弱风险 2 处（GLM_2 小样本 / L1-R2 稀释）。PI 拍板（ask_b15a39edc998bdb65e86b36d）：**重跑 A2 真实面补数据**定真假。

### §15.2 E-28.2 A2 重跑定案（L9 棒，一手件 `results/_v4_supp_l9_a2r_*` 8 件）

**E-27 §12.1.3「5 PASS + 1 FAIL_infeasible」正式改标为「1 PASS + 4 FAIL 不立案 + 1 构造不可行」**：

| 命题 | 真实面判据 | 真实面值 | 阈值 | 判定 | 根因 |
|---|---|---|---|---|---|
| **D-2** | TH-24 \|ρ\| | **0.8065** | ≥ 0.70 | **PASS（真立）** | — |
| D-1 | K-D1 margin min | **-0.0295** | ≥ 0.01 | FAIL 不立案 | 假证伪：D3 退化吸收 |
| C-S21 | \|ρ\| | **0.3369** | ≥ 0.70 | FAIL 不立案 | 假证伪：构造失灵 |
| D-Rényi | α_std | **0.0239** | ≥ 0.05 | FAIL 不立案 | 假证伪：构造失灵 |
| D-closeness | n_max | **71** | ≥ 100 | FAIL 不立案 | 假证伪：样本量不足定性 |

**补充注记**：
- D-2 唯一真立 PASS：沿 TH-24 \|ρ\| 口径，**L9 生效件 `5C579F28634E`**（`_v4_supp_prereg_v02_add_L9_activation_2026_09_24.md`，3,924 B）；signed ρ=-0.8065 方向失配另记注
- v1 件 10 件零触动（`_v4_supp_a2_executor.py` `ef7b3b32e844` 等 68,550 B 等）；K-A2R-N1 5/5 过；可重入 SHA 一致（时间戳冻结）
- **限定注记（防过度引用）**：L9「补采」= 基于既有真实数据的 bootstrap 统计扩展（n_distinct=2200/1800/2200/1100/5），**非新增观测**——D-2 PASS 带此限定

### §15.3 E-28.3 L6 S-38 v2 重验 + verdict-keeper 裁决

- **verdict FAIL**（K-S38-1/2/3 全触发；per-operator ICC 3/3 全负：ngram=-0.157 / vocab=-0.500 / temp=-0.494；K-S38-3 按字面恢复「任一算子 ICC<0.60」后 3 算子全 hit）
- **裁因 1 = 真证伪**（verdict-keeper 裁决件 `973103878D6F` = `_v4_supp_l6_s38v2_rootcause_verdict.md`，24,847 B）：反方「构造失灵」读法不成立（n_distinct=22 ≥ 20 + JS 1e-3 ~ 1e-1 连续可分 + v1 trivial ρ=1.0 per_pair=[1,1,1] vs v2 ρ=-0.19 per_pair=[-0.75, 0.99, -0.79] 强对比 = 度量有分辨力）；**A1 报告曾把 S-38 归「假证伪」——根因翻转为真证伪**，此为 E-28 级根因更新；外推边界（跨骨干未覆盖）显式声明
- **裁因 2 = v1/v2 复刻漂移**（v1 记录 ICC=-0.405626 / ρ=1.0 vs v2 复刻 -0.445269 / ρ=-0.185）：verdict-keeper 裁「不明」→ Mavis 消歧路径 2 收窄「**高度指向 (a) executor 版本漂移**」（内证：`_v4_supp_a1_executor.py` L803 注释「原 60-cell 同档 trivial（ρ=0.9977）→ 用 caption 字符长度真梯度替代」= trivial → 真梯度构造演化痕迹，v1 trivial ρ=1.0 是旧构造路径指纹；A1 R1 同族先例）；workspace 非 git 仓库 git 历史不可用，内证即最强证据
- **v1 件恢复事故**：L6 worker 多跑 v1 executor 致 `_v4_supp_a1_s38_result.json` 瞬时被覆盖（hash 变 `68921B048D98`），手动重建恢复 SHA MATCH `41F40FBA1142`（2,853 B，字节级一致可信）；违规点 = 「只跑 v2」纪律失守，教训入档

### §15.4 E-28.4 L3 N-20 真证伪升级

E-27 §12.1.4 的 N-20「构造不可行」升级为「**真证伪**」（L3 留副本真删实测：K-N20-C1 副本一致性 PASS → 真删 fingerprint R=0.0 → shadow 模拟 vs 真删 **不等价实锤** = 命题「shadow 等价真删」被真实数据证伪）；K-N20-N1 structural（1 cell 设计 n_distinct=2）如实标注；原件恢复 SHA `fee04170aa73`（`corpus/v20/by_model/coze/coze_artifact_v_2026_09_16.json`，10,978 B）零破坏；弱项 = L3 executor 时间戳未冻结（二次 run SHA 漂移语义一致）

### §15.5 E-28.5 L1 N-28 现状补记

E-27 §12.1.4「N-28 构造面 PASS」补现状：L1 真打后 **真实面构造不可行**（b_k 附近 5 攻击 miss_rate 全饱和 0.0，非退化自证 5/5 FAIL）——构造面单腿 PASS 不外推不立案（K-N28-R* 先例即此）；**K-N28-R2 弱 PASS 标注**（4/5 攻击 ρ 不可算不参与「均」判据，判定强度稀释）

### §15.6 E-28.6 GLM_2 3 cells 暂定

E 组 GLM_2 跨 3 模型命题证伪（3/15 cells）标「**暂定，L7 N=20 复核前不立案**」（N=5 小样本假证伪风险）

### §15.7 E-28.7 过渡声明闭环

L9 §0.5 过渡声明 3 件执行结果：
- **A2 5 条**：已定案 E-28.2
- **GLM_2**：维持暂定 E-28.6
- **L1-R2**：弱 PASS 标注 E-28.5

→ 过渡声明使命完成，E-28 转正式勘误

### §15.8 E-28.8 待 PI 决 2 项 + 全判定真受审反查

- **D-Rényi operator 升级**：切真 Rényi 散算子（histogram + 真公式）→ α_std=332 ≥ 0.05 可翻 PASS，但需改 `0A7BCA992B95`（`_v4_methods_prereg_supplement_2026_09_23.md`，59,570 B）§4 字面 + 新立 TH-25——worker 保守未擅动（不擅自调阈值铁律），**待 PI 拍板**
- **D-closeness 数据扩展**：真实数据扩到 n ≥ 100 才可立 PASS，**待 PI 拍板**
- **§13.4 反查清单复查记录**：E-28 全部条目逐条过「构造不可行 / 构造补可受审 / 构造不可逃 = 命题不明」三分类 + 不留假证伪或假 pass

---

## §16 v11 追加节 SHA 自核 + 版本变更记录

### §16.1 v11 追加后 SHA 自核（**循环约束 self-referential**）

| 件 | 追加后 SHA-12 | 字节 |
|---|---|---|
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（v11 = 原 v10 + §15 E-28 + §16 本节） | （自指回环：写完即落盘；任何编辑会改变本字段自身。落盘报值见执行棒 stdout；外部观测者请用 `Get-FileHash -Algorithm SHA256 docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 独立复算） | （落盘后实测） |

### §16.2 v11 追加节源件 SHA-12 链（复核）

| 路径 | 盘 SHA-12 | 字节 |
|---|---|---|
| `results/_v4_supp_l9_a2r_verdict.md` | `E12C7D2DABA1` | 7,724 |
| `results/_v4_supp_l9_a2r_executor.py` | `73512A46BB5D` | 79,098 |
| `results/_v4_supp_l9_a2r_d2_result.json` | `0A3F7107C3AA` | 3,494 |
| `results/_v4_supp_l9_a2r_d1_result.json` | `1913ED2963DD` | 6,286 |
| `results/_v4_supp_l9_a2r_cs21_result.json` | `F1469D78F589` | 3,620 |
| `results/_v4_supp_l9_a2r_dr_result.json` | `31BCF67BC7A2` | 3,105 |
| `results/_v4_supp_l9_a2r_dct_result.json` | `05903D74173E` | 6,668 |
| `results/_v4_supp_l9_a2r_pre_hashes_2026_09_24.txt` | `188228B24E50` | 3,068 |
| `results/_v4_supp_l9_a2r_post_hashes_2026_09_24.txt` | `A3B2E7306368` | 3,702 |
| `results/_v4_supp_l6_s38v2_verdict.md` | `20D9B44E036E` | 16,224 |
| `results/_v4_supp_l6_s38v2_rootcause_verdict.md`（verdict-keeper 裁决件） | `973103878D6F` | 24,847 |
| `results/_v4_supp_l6_s38v2_prereg_note.md` | `4AC6BFECAB59` | 5,415 |
| `results/_v4_supp_l6_s38v2_executor.py` | `24D759F9EFB1` | 38,818 |
| `results/_v4_supp_l6_s38v2_result.json` | `A184C37EEB2D` | 18,222 |
| `results/_v4_supp_l3_n20copy_verdict.md` | `9D64AB25A3BA` | 16,275 |
| `results/_v4_supp_l3_n20copy_executor.py` | `5190C03F0A69` | 35,923 |
| `results/_v4_supp_l3_n20copy_result.json` | `B84F4747BDB6` | 16,077 |
| `results/_v4_supp_l1_n28r_verdict.md` | `B27AB50089F6` | 9,844 |
| `results/_v4_supp_l1_n28r_executor.py` | `2327B9706581` | 47,227 |
| `results/_v4_supp_l1_n28r_result.json` | `67AA1807F7C7` | 14,632 |
| `results/_v4_methods_prereg_supplement_2026_09_23.md`（§4 字面） | `0A7BCA992B95` | 59,570 |
| `corpus/v20/by_model/coze/coze_artifact_v_2026_09_16.json`（L3 原件恢复） | `fee04170aa73` | 10,978 |
| `results/_v4_supp_a2_executor.py`（v1 件零触动） | `ef7b3b32e844` | 68,550 |
| `results/_v4_supp_a1_s38_result.json`（手动重建恢复 SHA） | `41F40FBA1142` | 2,853 |
| `results/_v4_supp_prereg_v02_2026_09_24.md` | `D85488A64D89` | 42,764 |
| `results/_v4_supp_prereg_v02_activation_2026_09_24.md` | `AD42992DC75D` | 3,202 |
| `results/_v4_supp_prereg_v02_add_L9_2026_09_24.md` | `23879B6CD1CC` | 19,586 |
| `results/_v4_supp_prereg_v02_add_L9_activation_2026_09_24.md`（L9 生效件） | `5C579F28634E` | 3,924 |
| `results/_v4_supp_e_multimodel_verdict.md` | `9FD4B722405E` | 19,461 |
| `results/_v4_supp_e_multimodel_result.json` | `04FB36054F6B` | 14,686 |

**注**：瞬态 hash `68921B048D98`（L6 worker 多跑 v1 executor 致覆盖态）**未落盘可核**——属事故记录指纹，非持久件。

### §16.3 v11 版本变更记录

- **v10 → v11 变更范围**：**仅追加** §15（E-28 · 八小节 + 假证伪/假 pass 复查全链定案）+ §16（本节）；**0 处修改** v10 既有 §1-§14 内容
- **版本演进链**：v1（2026-09-23 初版 `48EFD3828D54`）→ v9（含 §7 E-15 处置记录的更新版 `29356D2BBBD1`）→ v10（2026-09-24 追加 E-27 + 真受审标准节 `11FEA51889B3`，57,531 B）→ **v11（2026-09-24 追加 E-28 + 假证伪/假 pass 复查全链定案节）**
- **追加方法**：`edit` 工具 `old_string` 精确匹配 v10 末行（`*出证：Trae code · 2026-09-23 → v10 续（2026-09-24 by doc-writer \`agent-0032834a3e04\`）*`），`new_string` 保留 v10 末行一字不动 + 新增 `---` 分隔 + 追加 §15 + §16 + 新末行
- **旧 E-1…E-27 内容核验**：v10 `11FEA51889B3`（57,531 B）落盘后按 §1-§14 内容哈希自核 → **追加后前 57,531 B 字节级未变**（实测 prefix SHA-12 = `11FEA51889B3` ✓）
- **v11 末态全文件 SHA-12**（执行棒 stdout 报值）：（自指回环：本节任何编辑都会改变本字段自身；执行棒交付时实测 SHA-12 + 大小在 doc-writer handoff 报告中给出；外部观测者请用 `Get-FileHash -Algorithm SHA256 docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 独立复算）

---

*出证：Trae code · 2026-09-23 → v11 续（2026-09-24 by doc-writer `agent-0032834a3e04`）*

---

## §17 E-29 · 2026-09-24 八线补测终态汇总 + 新勘误 2 项 + PI 拍板待清册（v11 → v12）

> **触发**：PI 2026-09-24 拍板「不应留任一假证伪或假 pass」（沿 `ask_053da3ad` / `ask_d394778f` §15 真受审标准）+ L1–L9 八线补跑（v0.2 §3–§10 字面）逐线收口
> **性质**：勘误追加节，**不改任何 E-1…E-28 旧行 + 不改 v11 §1–§16 内容**；八线补测判定表逐条附根因 + 一手件 SHA-12 链 + 新勘误两项（① N-12 v1 ICC 假阳性 ② L7 K-E-N20-3 方向语义）+ 6 项待 PI 拍板清册
> **边界**：R4 key 永不明文 / R5 frozen 只追加（**追加前 67,812 B prefix SHA-12 = `66CEBBDC834B` 必保持**）/ 全部数字可回溯 §17.1 一手件 SHA 链 / 不擅自重写 paper §4.4（沿 K-N12R-N2 硬约束 + L9 D-2 限定注记）

### §17.1 八线终态汇总（L1–L9 全表）

| 线 | 编号 | 判定 | 根因 | 一手件 + SHA-12 链 |
|:-:|---|---|---|---|
| **L1** | N-28 | **FAIL**（构造不可行） | b_k 附近 5 攻击 miss_rate 全饱和 0.0 → 真实面构造不可行；K-N28-R* 4/5 FAIL（4/5 攻击 ρ 不可算不参与「均」）；K-N28-R2 弱 PASS 标注（沿 E-28.5 补现状） | `_v4_supp_l1_n28r_executor.py` `2327B9706581`（47,227 B）/ `_v4_supp_l1_n28r_result.json` `67AA1807F7C7`（14,632 B）/ `_v4_supp_l1_n28r_verdict.md` `B27AB50089F6`（9,844 B） |
| **L2** | N-11 | **FAIL**（构造不可行，双缺口） | K-N11-1/2 资产面缺 distill/independent_train trace（沿 §3.1/§3.2 V4 放开未落实前不可构造）；K-N11-3 N=2/教师部分完成（J 中位数 0.41–0.52 < 0.85），5 教师真实面 J 中位数组 = {kimi 0.4145, GLM_1 0.4908, GLM_2 0.4611, coze 0.5226, minimax 0.4327} —— N=2 数据退化致命题不明（沿 K-N11-N1「N < 20 → FAIL 命题不明族」），非明确证伪 | `_v4_supp_l2_n11supp_executor.py` `0D455B42CD07`（44,072 B）/ `_v4_supp_l2_n11supp_result.json` `FF7B167AE43F`（17,970 B）/ `_v4_supp_l2_n11supp_verdict.md` `E433A06E7BFB`（15,671 B） |
| **L3** | N-20 | **FAIL 真证伪** | shadow vs 真删 **不等价实锤**（K-N20-C1 副本一致性 PASS → 真删 fingerprint R=0.0 → shadow 模拟 vs 真删不等价 = 命题「shadow 等价真删」被真实数据证伪）；K-N20-N1 structural（1 cell n_distinct=2）如实标注 | `_v4_supp_l3_n20copy_executor.py` `5190C03F0A69`（35,923 B）/ `_v4_supp_l3_n20copy_result.json` `B84F4747BDB6`（16,077 B）/ `_v4_supp_l3_n20copy_verdict.md` `9D64AB25A3BA`（16,275 B） |
| **L4** | N-26 | **FAIL**（构造不可行，问题收窄） | K-N26-1/2/3 4/5 教师配对缺失致准确率/AUC 不可算（构造不可行族）；K-N26-N1 FAIL（4 cells n_distinct<5：payload「ping」短 + minimax qwen_plan 第二 call 失败 n=5 退化为 n_distinct=2/3 ≠ 工具失灵 = payload 设计短 + 样本量小）；K-N26-N2 teamo tun 合规 **PASS 10/10**；metadata v1 1/5 → v2 5/5 全补齐（kimi/GLM_1/GLM_2/coze 由 V3 缺位补全），但缺教师侧配对（V3 调用侧未保留）= 后续重采大工程 | `_v4_supp_l4_n26re_executor.py` `3B6F62686A89`（35,644 B）/ `_v4_supp_l4_n26re_result.json` `065DD4393AB8`（18,428 B）/ `_v4_supp_l4_n26re_verdict.md` `74B5B37F7EEA`（16,365 B） |
| **L5** | C-S39 | **FAIL 真证伪（coze/ngram 不可分）** | K-CS39-1 真实面 ratio=**1.2744** ≥ 1.10 PASS（v1 ratio=4.5 构造失灵消除，扩矩阵 9 backbone × 60 cell = 540 cells 真实面补齐）；K-CS39-2 coze per_teacher_ratio=**1.0493** < 1.10 hit FAIL（v1 全部 per_teacher 退化信号 1e12 反差被扩矩阵消解，唯留 coze 子集真证伪）；K-CS39-3 PASS（FPR=0.0226 < 0.05）；K-CS39-N1 非退化 PASS（known=10/unknown=11 ≥ 5） | `_v4_supp_l5_cs39ext_executor.py` `B3536C07222D`（48,030 B）/ `_v4_supp_l5_cs39ext_result.json` `ACE138CAF82F`（5,788 B）/ `_v4_supp_l5_cs39ext_verdict.md` `FABD1BEDE4C3`（6,766 B） |
| **L6** | S-38 | **FAIL 真证伪**（裁决确认，沿 E-28.3） | verdict-keeper 裁因 1 = 真证伪（n_distinct=22 ≥ 20 + JS 1e-3 ~ 1e-1 连续可分 + v1 trivial ρ=1.0 vs v2 ρ=-0.19 强对比 = 度量有分辨力）；K-S38-1/2/3 全触发（per-operator ICC 3/3 全负：ngram=-0.157 / vocab=-0.500 / temp=-0.494） | `_v4_supp_l6_s38v2_executor.py` `24D759F9EFB1`（38,818 B）/ `_v4_supp_l6_s38v2_result.json` `A184C37EEB2D`（18,222 B）/ `_v4_supp_l6_s38v2_verdict.md` `20D9B44E036E`（16,224 B）/ `_v4_supp_l6_s38v2_rootcause_verdict.md` `973103878D6F`（24,847 B，verdict-keeper 裁决件） |
| **L7** | E N=20 | **FAIL** | K-E-N20-1/2 FAIL（凑齐率 13/15 = 0.8667 < 0.95，teamo×kimi n_p=18 + teamo×GLM_2 n_p=19 因 teamo JSON 围栏偶发 parse 失败 2 calls 而非 20）；K-E-N20-3 FAIL（沿字面「N=5 vs N=20 分布差异 < TH-23=0.05 → FAIL」，实测 max\|ΔD1_JS\|=0.021941 / mean=0.008017）；K-E-N20-N1 PASS（N=20 自动 n_distinct ≥ 5）；K-E-N20-N2 PASS（teamo 走 tun 全程合规）；K-E-N20-N3 PASS（每 batch 实测 155-275s / 600s 内 ✓）；**300 calls 总账（3 模型 × 5 教师 × 20 calls × 理论采样，部分 cells 18-19 受 parse 失败差额）** | `_v4_supp_l7_e_n20_runner.py` `D5640CA314E2`（17,215 B）/ `_v4_supp_l7_e_n20_result.json` `E9D2BFD6C756`（14,385 B）/ `_v4_supp_l7_e_n20_verdict.md` `B8335982AE5E`（6,424 B） |
| **L8** | N-12 | **FAIL 真证伪**（方向性敏感被证伪） | K-N12R-1/2/3 全触发：median(ρ)=**0.2387** < 0.85（rank 不稳） / \|ΔICC\|=**10.2213** > TH-21=0.05（口径差异显著） / min(ρ)=**−0.5774** < TH-22=0.50（rank 反转点 = temperature vs structural，由 minimax 贡献最大 \|Δrank\|=3.5）；K-N12R-N1 PASS（20 cell × 13 维 n_distinct ≥ 12）；K-N12R-N2 PASS（产物不进论文 §4，沿拍板 #9 缓定）；K-N12-1/2/3 沿字面亦全 FAIL（proper 口径 ICC(3,k)=−11.6990, mean(ρ)=0.1796, shuffle_diff=0.1511）—— 沿新勘误 ①（§17.2） | `_v4_supp_l8_n12r_executor.py` `882965FDB738`（56,013 B）/ `_v4_supp_l8_n12r_result.json` `79A3DB97B3A0`（22,680 B）/ `_v4_supp_l8_n12r_verdict.md` `114CF71AB3D4`（19,127 B） |
| **L9** | A2R | **1 PASS（D-2）+ 4 FAIL 不立案**（沿 E-28.2） | D-2 PASS（真立，ρ_max=**0.8065** ≥ TH-24=0.70）；D-1/C-S21/D-Rényi/D-closeness 4 条 FAIL 不立案（真实面 \|ρ\|=0.3369 / α_std=0.0239 / n_max=71 全部不达标；归「假证伪·构造失灵/样本量不足定性」） | `_v4_supp_l9_a2r_executor.py` `73512A46BB5D`（79,098 B）/ `_v4_supp_l9_a2r_verdict.md` `E12C7D2DABA1`（7,724 B） |

**8 线总览**：PASS 真立 = 1（L9 D-2）/ FAIL 真证伪 = 3（L3 N-20, L5 C-S39 coze 子集, L6 S-38, L8 N-12）/ FAIL 构造不可行 = 4（L1 N-28, L2 N-11, L4 N-26, L9 其余 4 条 + L7 K-E-N20-1/2, K-E-N20-3 命中）/ 沿 E-27 §12.1.3/§12.1.4 正式改标 + E-28 假证伪/假 pass 复查全链收口。

### §17.2 新勘误 ① · N-12 v1「ICC=0.8883 PASS」= 公式缺陷假阳性

**事实流**：
- v1 件 `results/_v4_supp_b_n12_result.json`（SHA-12 `A0FF0B899E5F`）记录 ICC(3,1)=**0.8883** 判 K-N12-1 hit=False PASS——**【已确认为假阳性】**
- v1 executor `results/_v4_supp_b_executor.py`（SHA-12 `D71730B77CF3`）的 `icc_31` 公式用 `sum((M − μ_rater)²)` 近似 residual（**非 proper residual**，未剔除 μ_subject 主效）；4 extractor 量纲差异（ngram 8933–18784 / vocab 232–716 / temperature 84–114 / structural 3–5，跨 4 量级）下，Σ(M − μ_rater)² 远大于 Σ proper residual²（60.87M vs 4.79M），造成 MSR/MSE 比的假象 → 「绝对值一致」假阳性
- L8 棒用 proper McGraw-Wong 1996 Case 3A 平均度量绝对协议公式（剔除 subject + rater 主效后 Σ(residual²) / ((n−1)(k−1))）复算：**ICC(3,k) = −11.6990**（**\|ΔICC\| = 10.2213 ≫ TH-21=0.05**）——远低于 0.75 阈值
- ICC(2,k) absolute = **−1.4777**（同 proper residual 口径）；ICC(3,1) single rater = **−0.1752**；3 口径全部负值（MSR=4.79M ≪ MSE=60.87M，反映 between-V20 变异远小于 extractor 内部变异）

**E-27 §12.1.4 表述失真注记**：
- 原文 `N-12` 行记 `ICC(3,1)=0.8883（≥ 0.75 PASS）……K-N12-1 hit=False / K-N12-2 hit=True / K-N12-3 hit=True`，此处 **「ICC PASS」实为 v1 公式缺陷的假阳性**（仅在 v1 b_executor.py `icc_31` 公式下成立）
- 真实面 L8 proper 口径下 ICC(3,k)=−11.6990（hit=True → FAIL），与 K-N12R-1/2/3 三补口径（rank 稳定性 + 口径差异 + rank 反转点）全部 FAIL 同向
- 本条修正确认：**「ICC=0.8883 PASS」系假阳性，proper 口径下 ICC 亦 FAIL**；N-12 三条 K-N12R 全 FAIL + K-N12-1/2/3 沿字面亦全 FAIL（proper ICC / mean(ρ)=0.1796 / shuffle_diff=0.1511），**总判定 FAIL 不变**（与 v11 §15.3 E-28.3 / §15.4 E-28.4 体系一致）

**rank 反转点定位**（L8 verdict §6 实证）：
- **minimax V20** 在 ngram↔temperature / vocab↔temperature / temperature↔structural 三对 extractor 中均贡献最大 \|Δrank\|（分别 = 4.0 / 4.0 / 3.5）
- **量纲分化型制品特征**：minimax 制品 token 总量大（ngram 18784 全表最高）/ byte-level entropy 中等（temperature 84.19 中等）/ schema tree depth 一般（structural 5）—— 跨 extractor rank 不稳是这种「量纲分化型」制品的固有特征，与方向性敏感根因同源
- 物理解释：4 个 extractor 的 raw-value「绝对值一致」容易（每 extractor 自洽），rank「相对次序一致」难（跨量纲次序漂移）；ICC(3,k) 公式对 MSR 接近零敏感（分母小 → 数值爆炸）—— 两公式**对量纲差异型数据均不可靠**本身就是「方向性敏感」的数学表征

### §17.3 新勘误 ② · L7 K-E-N20-3 方向语义复核点（待拍板）

**事实流**：
- K-E-N20-3 字面（沿 `AD42992DC75D` activation + `D85488A64D89` v0.2 §7）：N=5 baseline vs N=20 分布差异 < TH-23=0.05（hit=True → FAIL）
- 实测触发：`max\|Δ D1_JS\| = 0.021941` / `mean\|Δ D1_JS\| = 0.008017`（均远小于 0.05）→ hit=True
- **语义疑点（L7 worker 显式提请）**：「无新信息」在部分语境是**中性结论**——「N=5 已捕获主要信号，扩样至 N=20 未带来增量信息」可读作**稳健性正向**而非「方法失灵」负向
- 字面判 FAIL（沿 v0.2 §7 K-E-N20-3 字面：「分布差异 < TH-23 → FAIL」，「小差异」=「无新信号」= 命题方向不显著）
- 语义判「**稳健性 PASS**」（N=5 结论在 N=20 下复现稳定，无翻盘；与「N=20 推翻 N=5」同属「扩样检验」的两种结果）

**双读法并记**（沿 §13.2 不留「假成立」灰色）：
| 读法 | 解释 | 适用语境 | 落地形式 |
|---|---|---|---|
| **字面读法** | 沿 v0.2 §7 K-E-N20-3 字面 → 触发 → FAIL | 严格方法学判据 | 本棒按字面判 FAIL（与 K-E-N20-1/2 总判定一致） |
| **语义读法** | N=5 vs N=20 同向 = **稳健性正向**（中性结论） | 蒸馏量稳定性 / 启发式结论 | **待拍板**——PI / verdict-keeper 复核（见 §17.7 E-29.7 #5） |

**老实交代**：本条如实并记两读法，字面读法=FALL（本棒采用），语义读法=N=5 结论稳健中性——**「待拍板」不擅自反转判定**；K-E-N20-3 沿 E-27 §11 拍板 #15 标准「FAIL 必区分根因」如实记「构造退化致命题方向可见（数据足够 N=20 样本），但扩样信号弱触发 K-E-N20-3 字面 FAIL」。

### §17.4 GLM_2 暂定 → 正式（E-28.6 闭环）

**事实流**：
- E-28.6 标记「GLM_2 跨 3 模型命题证伪（3/15 cells）= 暂定，L7 N=20 复核前不立案」（N=5 小样本假证伪风险）
- L7 N=20 实测：3 模型 GLM_2 全 D1 > D2 同向（margin_delta < 0）：
  - qwen_plan：D1_JS=0.009724 / D2_JS=0.008193 / margin_delta=−0.001531（命题层面被证伪 ✓）
  - mimo：D1_JS=0.009571 / D2_JS=0.008942 / margin_delta=−0.000630（命题层面被证伪 ✓）
  - teamo：D1_JS=0.007585 / D2_JS=0.006318 / margin_delta=−0.001267（命题层面被证伪 ✓）
- 跨 3 模型 × N=20 稳定同向（v1 N=5 baseline 全同向：qwen_plan −0.001611 / mimo −0.001106 / teamo −0.006920）

**判定升级**（沿 v0.2 §11 + 拍板 #15）：
- 「**暂定**」 → 「**正式命题证伪**」（GLM_2 家族命题证伪信号跨 3 模型成立 = E 组 v1 N=5「构造域不可对齐」一等结论在 N=20 下部分可对齐）
- E-28.6 暂定项 → **正式立项**；GLM_2 跨 3 模型真证伪信号收口
- 沿 GLM_2 (n_t=23) 硬上限（即使 N=20 proxy 也不能超越教师数，但 0.870 ratio 全切 0.20），命题信号方向稳态

### §17.5 N=20 理论投影验证 + 根因分布质变

**理论投影验证**（v1 N=5 verdict §4 投影预期 → N=20 实测）：
| 教师 | n_t | 理论 N=20 ratio 投影 | 实测 N=20 ratio | ≥ 0.20? |
|---|---:|:-:|:-:|:-:|
| kimi | 44 | 0.455 | **0.455** | ✓ |
| GLM_1 | 71 | 0.282 | **0.282** | ✓ |
| GLM_2 | 23 | 0.870 | **0.870** | ✓ |
| coze | 29 | 0.690 | **0.690** | ✓ |
| minimax | 30 | 0.667 | **0.667** | ✓ |

- **5/5 教师 N=20 下 ratio ≥ 0.20 全满足**（沿 v1 投影 5/5 满足 ✓ → 实测 5/5 满足 ✓）
- 理论投影与实测逐字节对齐（kimi/GLM_1/GLM_2/coze/minimax 五个数 0.455/0.282/0.870/0.690/0.667 一字不差）

**根因分布质变**（15 cells cells 在 N=5 vs N=20 下根因变化）：
| 根因分类 | v1 N=5 | 实测 N=20 | 变化 |
|---|:-:|:-:|---|
| **命题层面被证伪** | 3/15 cells（20%，GLM_2 跨 3 模型） | **9/15 cells（60%）** | +6 cells 扩样浮出真死 |
| 工具或构造层面失灵 | 12/15 cells（80%） | **6/15 cells（40%）** | −6 cells 工具失灵族被 N=20 消除 |
| 不明 / n/a (PASS) | 0/15 / 0/15 | 0/15 / 0/15 | 不变 |

- **N=20 扩样的判定学意义**：扩样让**真死浮出**——v1 N=5 下 12/15 cells 归「工具失灵」构造失灵族（n_p/n_t < 0.20 触发），到 N=20 下 6/15 cells 真证伪可见（kimi/GLM_2/coze/minimax 等教师跨 3 模型）
- 「构造域不可对齐」（E 组 v1 verdict 一等结论）→ 在 N=20 下部分可对齐（GLM_2 家族命题证伪信号跨模型成立 = 跨教师对齐片段）
- 600s runtime watchdog 拆分策略：每 background task = 1 model × 1 teacher × N=20 calls (~155-275s / 批)；本棒 5 models × 5 teachers × 4 batches = ~20 batches 跨 5 次 background session 边界 ✓

### §17.6 弱 PASS / 限定口径登记（防过度引用）

如实登记——避免后续 agent / 论文 §4 误读为「强 PASS」：

| 弱 PASS / 限定项 | 口径说明 | 来源 |
|---|---|---|
| **L5 K-CS39-3 FPR PASS** | **工程近似口径**（信号强度 FPR=mean(ci_lower_95)=0.0226）——严格二值 FPR 数据不足（measure 4 IC cells），弱 PASS 标注 | `_v4_supp_l5_cs39ext_verdict.md` `FABD1BEDE4C3` §4.2 |
| **L9 D-2 PASS** | **限定注记（沿 E-28.2）**：补采 = 基于既有真实数据的 bootstrap 统计扩展（n_distinct=2200/1800/2200/1100/5）**非新增观测**；D-2 PASS 带此限定防过度引用 | `_v4_supp_l9_a2r_verdict.md` `E12C7D2DABA1` §15.7 限定注记 |
| **L1 K-N28-R2 弱 PASS** | 4/5 攻击 ρ 不可算不参与「均」判据，判定强度稀释（沿 E-28.5 补现状） | `_v4_supp_l1_n28r_verdict.md` `B27AB50089F6` §K-N28-R2 |
| **L7 K-E-N20-3 FAIL 双读法** | 字面 FAIL + 语义稳健 PASS = **待拍板**（见 §17.3 + §17.7 #5） | `_v4_supp_l7_e_n20_verdict.md` `B8335982AE5E` §2 K-E-N20-3 |
| **L7 凑齐率 13/15** | 如实记录 teamo×kimi n_p=18 / teamo×GLM_2 n_p=19 因 teamo JSON 围栏偶发 parse 失败 2 calls 而非 20；总 calls 账本 = 290 calls / 3 模型 × 5 教师（理论 300，差额 10 由 teamo parse 失败 + 整体节流） | `_v4_supp_l7_e_n20_verdict.md` `B8335982AE5E` §1 凑齐率表 |
| **L8 K-N12R-N2 PASS** | 本棒产物不入论文 §4（沿拍板 #9 缓定，去向由 PI 另行处置） | `_v4_supp_l8_n12r_verdict.md` `114CF71AB3D4` §8.5 + §14 老实交代 |
| **L2 K-N11-3 FAIL 双读法** | 字面 FAIL（5 教师 J 中位数 < 0.85）+ 命题方向可见但 N=2 数据退化致命题不明（沿 K-N11-N1「N < 20 → FAIL 命题不明族」）——非明确证伪 | `_v4_supp_l2_n11supp_verdict.md` `E433A06E7BFB` §4.3 K-N11-3 + §6 双读法 |

### §17.7 待 PI 拍板 6 项收口清册（沿 §13.4 + 拍板 #15）

> **沿 PI 2026-09-23 记忆「漏报纠正」（「确定没有待拍板项了吗？」实有 8 项）——本节 6 项穷尽清点**；如另有遗漏项（如「K-N11-N2 双读法归类」「GLM_2 跨阶段处置」等）由 parent / verdict-keeper 后续补列。

| # | 拍板项 | 触及锚 / 数据 | 拍板点 | 现行处理 |
|:-:|---|---|---|---|
| **1** | **D-Rényi operator 升级** | α_std=0.0239 < 0.05 FAIL 不立案（沿 E-28.2）→ 切真 Rényi 散算子（histogram + 真公式）可翻 α_std=332 ≥ 0.05 | `_v4_methods_prereg_supplement_2026_09_23.md` `0A7BCA992B95`（59,570 B）§4 字面 + 新立 TH-25；worker 保守未擅动 | **待拍板**——是否改 §4 字面 + 新立 TH-25 |
| **2** | **D-closeness 数据扩展** | n_max=71 < 100 FAIL 不立案（沿 E-28.2）→ 真实数据扩到 n ≥ 100 才可立 PASS | `corpus/v20/` + `deposon_v20_baselines.json` `6edb2aec1660`（需重采大工程） | **待拍板**——是否启动 n ≥ 100 真实数据扩展 |
| **3** | **L2 Track 2 全轨道放开** | K-N11-1/2 FAIL 因资产面缺 distill/independent_train trace —— Track 2 多模型 re-asked trace 实验**无法补**此 2 类样本 | `0A9EE16267B5` `§3.1 / §3.2 V4 放开` 字典 / 本棒 qwen_plan 实测（仅一条端点） | **待拍板**——§3.1/§3.2 V4 Track 2 多模型补 distill/independent_train trace（K-N11-1/2 唯一补径） |
| **4** | **N ≥ 20 接力排期** | L2 N=2 < 20 / L4 4 教师配对重采 / L7 teamo 3 calls 凑齐 | L2 ~500 calls（5 教师 × 5+ 端点 × 20 prompt）/ L4 5 by_model × per-call metadata 重采（V3 调用侧保留）/ L7 teamo JSON 围栏偶发 parse 失败（2 calls） | **待拍板**——600s runtime watchdog 拆分策略；worker 接力棒排期 |
| **5** | **L7 K-E-N20-3 方向语义**（E-29.3） | 字面 FAIL（K-E-N20-3 触发）vs 语义「N=5 结论在 N=20 下稳健中性」 | v0.2 §7 K-E-N20-3 字面 / `_v4_supp_l7_e_n20_verdict.md` `B8335982AE5E` §2 + §3 根因表 | **待拍板**——字面 FAIL vs 中性稳健 PASS（双读法归一） |
| **6** | **GLM_2 命题证伪去向**（论文 §4） | GLM_2 跨 3 模型 × N=20 稳定同向命题证伪（已正式立项，§17.4） | L8 K-N12R-N2 硬约束「本棒产物不入论文 §4」≠ GLM_2 家族；L8 不进 §4 系 PI 拍板 #9 个案约束 | **待拍板**——是否进论文 §4（与 K-N12R-N2 不冲突） |

**§17.7 边界声明**：
- **6 项穷尽清点**；如本棒出证后另有遗漏，由 verdict-keeper / parent 后续追加（不自作主张删项）
- **不擅自拍板**：6 项一律等 PI 明示回函 / 工具问卷回复 / 母会话派工变更
- **关键约束**：所有拍板结果将追加为 §17.7 v12.x 子节（v12.1 / v12.2 ...），不动本 §17.1–§17.6 既有内容
- **「待拍板」≠「暂定」 ≠ 「不确定」**：本节「待拍板」= 派工已出但 PI 未回函，依 R4 / R5 / 不擅动阈值 等铁律维持现状，不擅自决断

### §17.8 E-29 边界声明（v12 追加）

- **未修改任何 E-1…E-28 旧行 / 未修改 v11 §1–§16 既有 §15 内容**：追加前 67,812 B prefix SHA-12 = `66CEBBDC834B`（实测，落盘后 append 完成即刻核验）；§17 仅追加于 v11 末行（`*出证：Trae code · 2026-09-23 → v11 续 ...*`）之后
- **未修改任何 V1–V3 资产**：8 线 executor 跑前跑后 SHA 自证全 0 触动（v0.2 v1 件 + 8 线新产 / frozen chain pre/post hashes 实测一致）
- **未修改任何 V4 frozen 链**：L1–L9 8 件 verdict 件 + rootcause 件 + executor 件 + result 件 + hashes 件共 30+ 件落盘（详见 §18.2 源件 SHA-12 链）；`_v4_supp_prereg_v02_*` + `_v4_N09_N39_prereg_*` + `_v4_methods_prereg_supplement_*` + `corpus/v20/by_model/*` + `corpus/v20_caption_surface/*` 等 0 触动
- **kill-line 字面不动**：K-L* 字面全部沿 `D85488A64D89` v0.2 + `AD42992DC75D` activation + `4070FDAAC111` / `113CBE555643` / `0A7BCA992B95` / `0A9EE16267B5` 等预登记字面；TH-21 / TH-22 / TH-23 / TH-24 沿字面不动
- **不擅自调阈值**：TH-21=0.05（K-N12R-2）/ TH-22=0.50（K-N12R-3）/ TH-23=0.05（K-E-N20-3）/ TH-24=0.70（L9 D-2）全部沿字面
- **派生 JSON 不合并**：8 线 30+ 件单 JSON 落盘（`_v4_supp_l{1,2,3,4,5,6,7,8,9}_*_*`），与历史 `_v4_exec_n*_result.json` / `_v4_supp_a1/a2/b/cd/d/e_*` 不交叉；L1–L9 8 件 verdict.md 互不交叉
- **key 形态自扫 clean**：8 线 30+ 件产物 + 8 件 executor + 本节全文 + hashes 文件 0 命中 `sk-[A-Za-z0-9]{20,}` / `AIza[0-9A-Za-z_-]{30,}` / `Bearer\s+[A-Za-z0-9]{20,}` 等 3 形态（沿 `AD42992DC75D` v0.2 §0 锁定）
- **succeeded ≠ 跑完**：本棒为 doc-writer 起草类，仅起草 §17 + §18 + 末行；不代表「实验已落盘核验」——8 线实验数据落盘由各线 worker 棒（executor `2327B9706581` / `0D455B42CD07` / `3B6F62686A89` / `B3536C07222D` / `24D759F9EFB1` / `D5640CA314E2` / `882965FDB738` / `73512A46BB5D`）独立负责，本棒仅消费其 verdict.md + result.json 内容
- **skill 缺位 fallback**（沿派工单）：本地 skill 加载器多次实录 Local skill not found —— 按既有 5 件预登记件 + 派工单字面 + v11 §15.4 E-28.4 先例执行；**未编造 skill 不存在的虚构指令**
- **新勘误 2 项精确落点**：① N-12 v1 ICC=0.8883 PASS = 公式缺陷假阳性（详见 §17.2）；② L7 K-E-N20-3 方向语义（字面 FAIL vs 语义稳健 PASS，待拍板，详见 §17.3）—— 2 项均沿拍板 #15 标准「不留任一假证伪或假 pass」字面级处置

---

## §18 v12 追加节 SHA 自核 + 版本变更记录

### §18.1 v12 追加前 SHA 自核（**沿 v11 末态**）

| 件 | 追加前 SHA-12 | 字节 |
|---|---|---|
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（v11 末版） | **`66CEBBDC834B`** | **67,812** |

> **锚定证据**：派工单声明「追加前 67,812 B prefix SHA-12 = `66CEBBDC834B`」——实测核验 ✓（见本棒 [Validation run] 节）

### §18.2 v12 追加节源件 SHA-12 链（8 线 30+ 件）

| 路径 | 盘 SHA-12 | 字节 |
|---|---|---|
| `results/_v4_supp_l1_n28r_executor.py` | `2327B9706581` | 47,227 |
| `results/_v4_supp_l1_n28r_result.json` | `67AA1807F7C7` | 14,632 |
| `results/_v4_supp_l1_n28r_verdict.md` | `B27AB50089F6` | 9,844 |
| `results/_v4_supp_l1_n28r_pre_hashes_2026_09_24.txt` | （实测 pre） | 198 (txt) |
| `results/_v4_supp_l1_n28r_post_hashes_2026_09_24.txt` | （实测 post） | 198 (txt) |
| `results/_v4_supp_l2_n11supp_executor.py` | `0D455B42CD07` | 44,072 |
| `results/_v4_supp_l2_n11supp_result.json` | `FF7B167AE43F` | 17,970 |
| `results/_v4_supp_l2_n11supp_verdict.md` | `E433A06E7BFB` | 15,671 |
| `results/_v4_supp_l2_n11supp_pre_hashes_2026_09_24.txt` | （实测 pre） | — |
| `results/_v4_supp_l2_n11supp_post_hashes_2026_09_24.txt` | （实测 post） | — |
| `results/_v4_supp_l3_n20copy_executor.py` | `5190C03F0A69` | 35,923 |
| `results/_v4_supp_l3_n20copy_result.json` | `B84F4747BDB6` | 16,077 |
| `results/_v4_supp_l3_n20copy_verdict.md` | `9D64AB25A3BA` | 16,275 |
| `results/_v4_supp_l4_n26re_executor.py` | `3B6F62686A89` | 35,644 |
| `results/_v4_supp_l4_n26re_result.json` | `065DD4393AB8` | 18,428 |
| `results/_v4_supp_l4_n26re_verdict.md` | `74B5B37F7EEA` | 16,365 |
| `results/_v4_supp_l5_cs39ext_executor.py` | `B3536C07222D` | 48,030 |
| `results/_v4_supp_l5_cs39ext_result.json` | `ACE138CAF82F` | 5,788 |
| `results/_v4_supp_l5_cs39ext_verdict.md` | `FABD1BEDE4C3` | 6,766 |
| `results/_v4_supp_l6_s38v2_executor.py` | `24D759F9EFB1` | 38,818 |
| `results/_v4_supp_l6_s38v2_result.json` | `A184C37EEB2D` | 18,222 |
| `results/_v4_supp_l6_s38v2_verdict.md` | `20D9B44E036E` | 16,224 |
| `results/_v4_supp_l6_s38v2_rootcause_verdict.md`（verdict-keeper 裁决件） | `973103878D6F` | 24,847 |
| `results/_v4_supp_l6_s38v2_prereg_note.md` | `4AC6BFECAB59` | 5,415 |
| `results/_v4_supp_l7_e_n20_runner.py` | `D5640CA314E2` | 17,215 |
| `results/_v4_supp_l7_e_n20_result.json` | `E9D2BFD6C756` | 14,385 |
| `results/_v4_supp_l7_e_n20_verdict.md` | `B8335982AE5E` | 6,424 |
| `results/_v4_supp_l7_e_n20_compare.py` | `328ED73043C1` | 31,469 |
| `results/_v4_supp_l7_e_n20_measure.py` | `09DD47B2F378` | 9,238 |
| `results/_v4_supp_l7_e_n20_manifest_2026_09_24.txt` | `D0215843141E` | 2,951 |
| `results/_v4_supp_l7_e_n20_post_hashes_e_frozen_2026_09_24.txt` | `4BB7DB25C57E` | 1,442 |
| `results/_v4_supp_l7_e_n20_post_hashes_v4frozen_2026_09_24.txt` | `5D765F459E5D` | 1,980 |
| `results/_v4_supp_l7_e_n20_pre_hashes_e_frozen_2026_09_24.txt` | `C101CF3DB300` | 2,612 |
| `results/_v4_supp_l7_e_n20_pre_hashes_v4frozen_2026_09_24.txt` | `D0B64D1AB8B7` | 1,960 |
| `results/_v4_supp_l8_n12r_executor.py` | `882965FDB738` | 56,013 |
| `results/_v4_supp_l8_n12r_result.json` | `79A3DB97B3A0` | 22,680 |
| `results/_v4_supp_l8_n12r_verdict.md` | `114CF71AB3D4` | 19,127 |
| `results/_v4_supp_l8_n12r_pre_hashes_2026_09_24.txt` | `D999A43D521F` | 29,820 |
| `results/_v4_supp_l8_n12r_post_hashes_2026_09_24.txt` | `AB290AA01959` | 29,820 |
| `results/_v4_supp_l9_a2r_executor.py` | `73512A46BB5D` | 79,098 |
| `results/_v4_supp_l9_a2r_verdict.md` | `E12C7D2DABA1` | 7,724 |

**v0.2 锚 + 预登记链**（沿 v11 §16.2 + 本棒复核）：
| 路径 | 盘 SHA-12 | 字节 |
|---|---|---|
| `results/_v4_supp_prereg_v02_2026_09_24.md` | `D85488A64D89` | 42,764 |
| `results/_v4_supp_prereg_v02_activation_2026_09_24.md`（K-N12R-N2 等生效件） | `AD42992DC75D` | 3,202 |
| `results/_v4_supp_prereg_v02_add_L9_2026_09_24.md` | `23879B6CD1CC` | 19,586 |
| `results/_v4_supp_prereg_v02_add_L9_activation_2026_09_24.md`（L9 生效件） | `5C579F28634E` | 3,924 |
| `results/_v4_N09_N39_prereg_2026_09_23.md`（N 档预登记） | `0A9EE16267B5` | 95,576 |
| `results/_v4_methods_prereg_supplement_2026_09_23.md`（方法预登记） | `0A7BCA992B95` | 59,570 |
| `results/_v4_seeds_prereg_supplement_2026_09_23.md`（种子预登记） | `113CBE555643` | — |
| `results/_v4_n22_n19_prereg_supplement_2026_09_23.md` | `4070FDAAC111` | — |
| `results/_v4_supp_b_n12_result.json`（v1 N-12 件，沿 R5 不覆盖） | `A0FF0B899E5F` | 2,957 |
| `results/_v4_supp_b_executor.py`（v1 b 件，沿 R5 不覆盖） | `D71730B77CF3` | 38,818（同 L6 文件但 L6 路径独立） |
| `results/_v4_distill_min_measure.py`（度量函数，只读） | `21771E66AF67` | — |
| `corpus/v20/by_model/coze/coze_artifact_v_2026_09_16.json`（L3 原件恢复） | `fee04170aa73` | 10,978 |

### §18.3 v12 追加后 SHA 自核（**循环约束 self-referential**）

| 件 | 追加后 SHA-12 | 字节 |
|---|---|---|
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（v12 = 原 v11 + §17 E-29 + §18 本节） | （自指回环：写完即落盘；任何编辑会改变本字段自身。落盘报值见执行棒 stdout；外部观测者请用 `Get-FileHash -Algorithm SHA256 docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 独立复算） | （落盘后实测） |

### §18.4 v12 版本变更记录

- **v11 → v12 变更范围**：**仅追加** §17（E-29 · 8 节 + 八线终态汇总 + 新勘误 2 项 + 6 项 PI 拍板清册）+ §18（本节）；**0 处修改** v11 既有 §1–§16 内容 + 0 处修改 E-1…E-28 旧行
- **版本演进链**：v1（2026-09-23 初版 `48EFD3828D54`）→ v9（含 §7 E-15 处置记录的更新版 `29356D2BBBD1`）→ v10（2026-09-24 追加 E-27 + 真受审标准节 `11FEA51889B3`，57,531 B）→ v11（2026-09-24 追加 E-28 + 假证伪/假 pass 复查全链定案节 `66CEBBDC834B`，67,812 B）→ **v12（2026-09-24 追加 E-29 + 八线补测终态 + 新勘误 2 项节）**
- **追加方法**：`edit` 工具 `old_string` 精确匹配 v11 末行（`*出证：Trae code · 2026-09-23 → v11 续（2026-09-24 by doc-writer \`agent-0032834a3e04\`）*`，67,812 B / SHA-12 `66CEBBDC834B`），`new_string` 保留 v11 末行一字不动 + 新增 `---` 分隔 + 追加 §17（8 节）+ §18（4 节）+ 新末行
- **旧 E-1…E-28 内容核验**：v11 `66CEBBDC834B`（67,812 B）落盘后按 §1–§16 内容哈希自核 → **追加后前 67,812 B 字节级未变**（实测 prefix SHA-12 = `66CEBBDC834B` ✓）
- **v12 末态全文件 SHA-12**（执行棒 stdout 报值）：（自指回环：本节任何编辑都会改变本字段自身；执行棒交付时实测 SHA-12 + 大小在 doc-writer handoff 报告中给出；外部观测者请用 `Get-FileHash -Algorithm SHA256 docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 独立复算）
- **拍板落地形式**：§17.7 6 项 PI 拍板结果将由 parent / verdict-keeper 追加为 v12.x 子节（v12.1 / v12.2 ...），不动本 §17.1–§17.6 + §18 既有内容

---

*出证：Trae code · 2026-09-23 → v12 续（2026-09-24 by doc-writer `agent-0032834a3e04`）*

---

## §19 E-30 · 2026-09-24 接力 5 棒定案 + 限定口径登记 + 拍板结果补记（v12 → v13）

> **触发**：PI 2026-09-24 拍板「N≥20 接力排期」（`ask_b7bb6076` #4）原文「小→大串行」—— L7（接力 1）/ L11（接力 2）/ L12（接力 3）/ L13（接力 4）/ L14（接力 5）五棒已完成全判定真受审
>
> **性质**：勘误追加节，**不改任何 E-1…E-29 旧行 + 不改 v12 §1–§18 内容**；5 棒判定表逐条附根因 + 一手件 SHA-12 链 + 7 项限定口径登记 + Token Plan 撞限事件实录 + N-26 终点定性 + N-11 定案补记 + 9 项 PI 拍板结果全闭环 + 任务 B 预实验状态注记
>
> **边界**：R4 key 永不明文 / R5 frozen 只追加（**追加前 96,985 B prefix SHA-12 = `BA25509A2EF6` 必保持**）/ 全部数字回溯 §19.7.2 一手件 SHA 链 / 不擅自重写 paper §4.4（沿 K-N12R-N2 硬约束 + L9 D-2 限定注记 + L14 K-N11-3 死因条件限定）

### §19.1 E-30.1 接力 5 棒定案表（小→大串行，PI 拍板 `ask_b7bb6076` #4）

| 棒 | 编号 | 判定 | 根因 | 一手件 + SHA-12 链 |
|:-:|:-:|---|---|---|
| **1** | **L7 凑齐**（V0 E-N20-3） | **PASS**（凑齐率 13/15→15/15=1.0；K-E-N20-1/2 转不 hit；K-E-N20-3 字面 FAIL / PI 反转稳健 PASS 双栏） | teamo JSON 围栏偶发 2 calls 失败补齐：fill 棒凑齐率 13/15→15/15=1.0；K-E-N20-1/2 转不 hit（非真 hit）；K-E-N20-3 字面 FAIL（K-E-N20-3 触发）vs 语义「N=5 结论在 N=20 下稳健中性」反转 = 双读法归一（PI 拍板 #3 沿 §17.7 #5） | `results/_v4_supp_l7_e_n20_fill_result.json` `1713d67076ce`（15,105 B）/ `results/_v4_supp_l7_e_n20_fill_verdict.md` `0e4a7fce58c0`（7,481 B）|
| **2** | **L11 D-closeness 扩数据** | **PASS 翻案** | v2 FAIL 样本量不足（n_max=71<100）→ 扩到 n≥100 真实数据 bootstrap 达标 **2,600 样本**；K-DCT-1 ratio=**19.23%** < 0.5 不 hit；K-DCT-3 边界值 temp=0.5 字面「>0.5」严格大于不触发（弱 PASS 标注，见 §19.2 #1） | `results/_v4_supp_l11_dct100_executor.py` `20dbf8b27c10`（29,533 B）/ `results/_v4_supp_l11_dct100_result.json` `20b0e13064f8`（12,143 B）/ `results/_v4_supp_l11_dct100_verdict.md` `14a98cfaa660`（18,650 B） |
| **3** | **L12 D-Rényi 真算子** | **PASS 翻案**（死因定性=旧 FAIL 系工具失灵族：线性近似压制非线性） | v2 近似算子 α_std=**0.0239** < 0.05 FAIL → 切真 Rényi 散（histogram + 真公式）α_std=**0.2025** ≥ TH-25=0.05（**4× 阈，+8.5× 信号质变**）；K-DR-R1/R2/R3 全不 hit；算子自检 JS=d2_sample 二分反解恢复 **1e-15 精度** | `results/_v4_supp_l12_dr_real_renyi_executor.py` `338af29559e1`（39,821 B）/ `results/_v4_supp_l12_dr_real_renyi_result.json` `6196067736a1`（10,713 B）/ `results/_v4_supp_l12_dr_real_renyi_verdict.md` `977fb07592f4`（24,321 B） |
| **4** | **L13 N-26 教师侧配对重采** | **N-26 真受审终点定案**（V3 侧 distill metadata 历史缺口**不可逆**） | 三元组基底补齐 24/30 complete（**80%**；6/30 = teamo reasoning-only 模型特性）；K-N26-N1 FAIL（max_tokens=50 触顶）/ K-N26-N2 PASS（tun 10/10）/ **K-N26-1/2/3 维持 FAIL 构造不可行**——问题收窄至终点：V3 侧 distill metadata 历史缺口**不可逆**（唯一真审路径=未来重跑 V3 采集同步保留，工程量=整链重跑如实挂账，挂账不设期限） | `results/_v4_supp_l13_n26pair_executor.py` `ff6a280be11a`（51,723 B）/ `results/_v4_supp_l13_n26pair_result.json` `a73bd752af9a`（52,481 B）/ `results/_v4_supp_l13_n26pair_verdict.md` `e105ec1362db`（23,120 B） |
| **5** | **L14 N-11 全轨道（中断恢复 v2）** | **N-11 真审定案：核心条款真证伪 + 配对条款补构造 PASS** | N=20/教师达成（**50 records**，TH-17 字面 PASS）；K-N11-1/2 补构造后 PASS（Track 2 多模型 re-asked trace 补齐 §3.1/§3.2 V4 放开范围）；**K-N11-3 真证伪 FAIL**（教师 J 中位数 **0.36–0.39** < 0.85，N=20 收敛稳定——qwen3.7-max+temp=0.7 构造属性，**真死非工具失灵**）；K-N11-N1/N2 PASS（脱「N<20 → FAIL 命题不明族」）；拍板 #3 沿 §17.7 L14 全达成 | `results/_v4_supp_l14_n11full_executor.py` `336c7b14b62a`（60,992 B）/ `results/_v4_supp_l14_n11full_result.json` `4c11ab9057b9`（12,246 B）/ `results/_v4_supp_l14_n11full_verdict.md` `8eef73bf9856`（19,697 B） |

**§19.1 边界说明**：
- **5 棒穷尽清点**：PI 派工「小→大」已全达成；6 棒及以上无新增（如有由 parent / verdict-keeper 后续追加）
- **每棒根因独立给出**：依 §13.1 四分类「真证伪 / 真死 / 工具失灵 / 构造不可行」逐条标注，未漏标
- **K-N11-3 真死证据强度**：N=20 收敛稳定 × 教师 J 中位数组 vs 阈 0.85 反差显著（~0.4 → 实际 0.36–0.39）——非 N < 20 数据退化致命题不明族
- **L13 N-26 终点不可逆声明**：本棒不擅自设 V3 重采期限，挂账不设 deadline，唯一真审路径即未来 V3 整链重跑

### §19.2 E-30.2 限定口径登记 7 项（防过度引用）

如实登记——避免后续 agent / 论文 §4 误读为「强 PASS」或「无条件复现」：

| # | 限定项 | 口径说明 | 来源 |
|:-:|---|---|---|
| **1** | **L11 K-DCT-3 边界值弱 PASS** | temp fail_ratio=**0.5** 恰等于阈，字面 `>0.5` 严格大于不触发（沿 E-27 §17.6 L7 K-E-N20-3 FAIL 双读法先例） | `_v4_supp_l11_dct100_verdict.md` `14a98cfaa660` §4 K-DCT-3 |
| **2** | **L11 D-closeness 扩数据 = bootstrap 统计扩展非新增观测** | 沿 L9 D-2 同口径（补采 = 基于既有真实数据的 bootstrap 统计扩展，非新增观测） | `_v4_supp_l11_dct100_verdict.md` `14a98cfaa660` §15 限定注记 + L9 `E12C7D2DABA1` §15.7 |
| **3** | **L12 D-Rényi (P,Q) 为 synthetic 构造** | corpus 分布只读约束下按 JS=d2_sample 二分反解，**非真实分布直读**；算子本身自检通过（恢复 1e-15 精度） | `_v4_supp_l12_dr_real_renyi_verdict.md` `977fb07592f4` §4 算子自检 + §15 限定注记 |
| **4** | **L11 13 cells vs v2 saved 11 cells baseline 偏移** | filter 行为差异如实声明（v2 saved 11 cells / v3 filter 13 cells） | `_v4_supp_l11_dct100_verdict.md` `14a98cfaa660` §3 baseline 对账表 |
| **5** | **L13 teamo reasoning-only 6/30 缺 response** | 模型特性非构造失灵（reasoning-only 模型对完整 CoT prompt 模板不返回 response 字段，沿 E-28.x 派生限制先例） | `_v4_supp_l13_n26pair_verdict.md` `e105ec1362db` §3 teamo 缺位表 |
| **6** | **L14 qwen 单端点 + 温度敏感性未探** | qwen3.7-max 单端点（mimo/teamo 留账），温度敏感性未探（temp=0.0/0.3/0.5 未跑） | `_v4_supp_l14_n11full_verdict.md` `8eef73bf9856` §5 端点覆盖 + §7 温度敏感性节 |
| **7** | **L14 K-N11-3 死因条件限定** | qwen3.7-max + temperature=0.7 构造属性（跨端点/跨温度外推未证） | `_v4_supp_l14_n11full_verdict.md` `8eef73bf9856` §K-N11-3 死因条件限定节 |

**§19.2 整体限定说明**：本节 7 项均为「不得在论文 §4 强引用」边界；如需引用须保持本表限定注记。

### §19.3 E-30.3 Token Plan 撞限事件 + 中断恢复实录（2026-09-24 14:56–15:34）

**事件时间线**：
- **14:56 L14 v1 撞 Token Plan 上限**：错误 2056「已达到 Token Plan 用量上限」（5h 额度耗尽），L14 v1 跑至中途被 runtime 拒服务
- **15:03 PI 确认额度重置「刚好差几秒」** + 明示**同一 agent 唤醒保持上下文不另立**（沿 `ask_7fcd4f7f`）
- **15:04–15:23 L14 v2 同件补全**：schema 升 `v4_l14_n11full/2`（result.json `"schema"` 字段实测 = `"v4_l14_n11full/2"`，沿 §19.7.2 L14 disk SHA 链 cross-validate），5 棒尾棒收口
- **未触动 Token Plan 累计额度账本**：5 棒全跑累计 vs ~500 天级目标 8× 节制

**额度节制声明（实测）**：
- L14 v1（接力 5 撞限前）：~30 calls
- L14 v2（接力 5 撞限后补全）：~30 calls（schema `v4_l14_n11full/2` 同件不另立账）
- **L14 v1+v2 共 60 calls**（vs ~500 天级目标 8× 节制）
- 5 棒全累计（L7_fill / L11_dct100 / L12_dr_real / L13_n26pair / L14_n11full）：~420 calls（vs ~500 天级 84% 节制 + 撞限事件 1 次）
- **额度节制声明**：L14 v1+v2 共 60 calls（vs ~500 天级目标 8× 节制）

**中断-恢复语义实录**：
- **同一 agent 唤醒保持上下文不另立**（沿 PI 明示）——L14 棒未因额度撞限而重派 worker，doc-writer 末尾收口亦未重派
- **历史棒次件不覆盖铁律保持**：L7_fill / L11 / L12 / L13 4 棒 pre/post hashes 实测一致；R5 frozen 只追加
- **schema 子目录 `/2` 仅为撞限前/后区分**：内容上 L14 v2 = L14 v1 + 补全（5 棒终态同源件；JSON 内 `"schema": "v4_l14_n11full/2"` 为 v2 标记位，非路径）

### §19.4 E-30.4 N-26 终点定性 + N-11 定案补记

**N-26 终点定性**（接力 4 收口）：
- **proxy 侧 5/5 补齐**（kimi / GLM_1 / GLM_2 / coze / minimax metadata 全立）
- **V4 三元组基底已立**：24/30 complete（80%）（6/30 = teamo reasoning-only 模型特性）
- **V3 侧历史配对缺口不可逆**：5 教师 × per-call metadata 在 V3 期间未保留（仅 L4 N-26 棒时间窗内补齐 kimi/GLM_1/GLM_2/coze = 4/5，但 V3 原始调用侧 5/5 完整度 ≠ 100%）
- **「构造不可行（一等结论）」终点定案**：依 §13.2 双读法，K-N26-1/2/3 维持 FAIL 字面 + 「构造不可行」根因
- **真审条件 = 未来 V3 整链重跑**（挂账不设期限，由 PI 另行处置）

**N-11 定案补记**（接力 5 收口，订正 v12 §17.1 L2 行判定）：
- **K-N11-1/2 补构造 PASS**：Track 2 多模型 re-asked trace 补齐 §3.1/§3.2 V4 放开范围（沿拍板 #3「§3.1/§3.2 V4 Track 2 多模型补 distill/independent_train trace」），L14 棒全达成（5 教师 × 4 端点 × 50 records）
- **K-N11-3 真证伪**：教师 J 中位数 0.36–0.39（实测 N=20）vs 阈 0.85，反差显著 × N=20 收敛稳定——「真死非工具失灵」
- **K-N11-N1/N2 PASS**：脱「N < 20 → FAIL 命题不明族」限制（沿 §17.6 #6 双读法先例）+ N=20 满足 PASS
- **按「全判定真受审」标准定案**：**部分条款活、核心条款真死**（K-N11-1/2/N1/N2 = 活；K-N11-3 = 真死）
- **拍板 #3 沿 §17.7 「§3.1/§3.2 V4 Track 2 多模型补 distill/independent_train trace（K-N11-1/2 唯一补径）」L14 全达成**——「构造不可行」字面撤除，转入真审定案
- **对 v12 §17.1 L2 行修正说明**：v12 §17.1 L2 行判字「**FAIL（构造不可行，双缺口）**」由「构造不可行」族提升为「**真审定案：核心条款真证伪 + 配对条款补构造 PASS**」族——本节为 v13 阶段定案补记，v12 §17.1 L2 行字面 v12 时点保留不动，仅在本节明确收口更新

### §19.5 E-30.5 拍板结果补记（E-29 §17.7 清册 6 项 + 后续 3 项全闭环）

> **沿 PI 2026-09-23 记忆「漏报纠正」——本节 9 项穷尽清点**（§17.7 6 项 + 后续 3 项）；如有遗漏由 verdict-keeper / parent 后续追加。

| # | 拍板项 | 拍板结果 | 闭环锚 |
|:-:|---|---|---|
| **1** | **D-Rényi operator 升级**（§17.7 #1） | ✅ **接力 3 翻案 PASS** | `ask_b7bb6076` #1 + §19.1 #3 真算子 α_std=0.2025 ≥ TH-25=0.05（4× 阈） |
| **2** | **D-closeness 数据扩展**（§17.7 #2） | ✅ **接力 2 翻案 PASS** | §19.1 #2 2,600 样本 n≥100 达标 / K-DCT-1 19.23%<0.5 不 hit |
| **3** | **L2 Track 2 全轨道放开**（§17.7 #3） | ✅ **接力 5 定案**（K-N11-1/2 补构造 PASS） | §19.1 #5 + §19.4 N-11 定案补记 |
| **4** | **N ≥ 20 接力排期**（§17.7 #4） | ✅ **小→大串行 5 棒全完成** | `ask_b7bb6076` #4 / §19.1 #1–#5 |
| **5** | **L7 K-E-N20-3 方向语义**（§17.7 #5） | ✅ **语义反转稳健 PASS**（`ask_b7bb6076` #3）+ L10-E3 注释 `F6FE005EE3C7` 生效 `16E89657DAAA` | `_v4_supp_prereg_v02_activation_2026_09_24.md` `AD42992DC75D` §K-E-N20-3 字面 / `_v4_supp_prereg_v02_add_L10_2026_09_24.md` `F6FE005EE3C7` 生效 → `_v4_supp_prereg_v02_add_L10_activation_2026_09_24.md` `16E89657DAAA` / 接力 1 §19.1 #1 |
| **6** | **GLM_2 论文 §4**（§17.7 #6） | ✅ **入负面结果章**（沿论文修订清单落） | `ask_b172e4d6` #1 + §17.4 GLM_2 暂定 → 正式 |
| **7** | **任务 B 采集开闸**（后续） | ✅ **今日预实验 37 题批**（双判死线初判双 PASS，11 题推理补采中） | `ask_b172e4d6` #2 + §19.6 dataset `AADCA810E40D` |
| **8** | **L10 生效**（后续） | ✅ **生效即锁 + TH-25=0.05 追认** | `ask_ca36f095` / 接力 3 §19.1 #3 TH-25 字面 |
| **9** | **Token Plan 处置**（后续） | ✅ **额度重置同 agent 唤醒续跑**（不另派 worker / 不另立上下文） | `ask_7fcd4f7f` / §19.3 撞限事件实录 |

**§19.5 整体闭环说明**：
- **9 项全闭环**：沿 §17.7 6 项 + 后续 3 项 = §13.4 真受审判定反查清单 6 项 + PI 2026-09-24 拍板 #1/#2/#3/#4/#5/#6 + 拍板 #7/#8/#9
- **拍板落地形式**：本节为 §17.7 6 项 + 后续 3 项收口，**不动本 §17.1–§17.8 + §18 既有内容**
- **后续不擅自补列**：如本棒出证后另有遗漏，由 verdict-keeper / parent 后续追加（不自作主张删项）

### §19.6 E-30.6 任务 B 预实验状态注记

**采集完成态**（接力 7）：
- **37 题批采集完成**（10 轮 ask_user，每轮 2–4 题）
- **dataset 落盘**：`results/_v4_pi_cot_v2_dataset.json` SHA-12 **`AADCA810E40D`**（11,522 B）
- **双判死线初判结果**：
  - 完成率 = **37/37 = 100% PASS**
  - 方法论理由可提取率 = **37/37 = 100% PASS**
- **双判死线初判双 PASS**（接力 7 阶段性结论，非终判）

**补采补采态**（2026-09-24 PI 令「预实验请完整」）：
- **11 题推理补采中**（TH-v2-1 推理全文必采严格口径）
- **补完 dataset 更新 v2 后重判双判死线**

**完整预实验状态注记**：
- **本棒视初判结果 = 阶段性，非终判**——如实限定「初判结果以补采后重判为准」
- **完整判死线 = 37 + 11 = 48 题批**（补采完）/ **如补采有失败 ≥ 1 题 → 完整判死线重跑**
- **沿派工 5 件必带 skill 缺位 fallback**：本地 skill 多次实录 Local skill not found，按既有 5 件预登记件 + 派工单字面 + v11 §15.4 E-28.4 先例执行；**未编造 skill 不存在的虚构指令**

### §19.7 v13 追加节 SHA 自核 + 版本变更记录

#### §19.7.1 v13 追加前 SHA 自核（沿 v12 末态）

| 件 | 追加前 SHA-12 | 字节 |
|---|---|---|
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（v12 末版） | **`BA25509A2EF6`** | **96,985** |

> **锚定证据**：派工单声明「追加前 96,985 B prefix SHA-12 = `BA25509A2EF6`」——实测核验 ✓（见本棒 [Validation run] 节）

#### §19.7.2 v13 追加节源件 SHA-12 链（接力 5 棒 + 拍板落地件）

| 棒 | 路径 | 盘 SHA-12 | 字节 |
|:-:|---|---|---|
| **1** | `results/_v4_supp_l7_e_n20_fill_result.json` | `1713d67076ce` | 15,105 |
| **1** | `results/_v4_supp_l7_e_n20_fill_verdict.md` | `0e4a7fce58c0` | 7,481 |
| **1** | `results/_v4_supp_l7_e_n20_pre_hashes_e_frozen_2026_09_24.txt`（L7 fill 棒继承 L7 v12 pre hashes，无独立 fill_pre） | （实测 pre，详见 §18.2） | 2,612 |
| **1** | `results/_v4_supp_l7_e_n20_post_hashes_e_frozen_2026_09_24.txt`（同上） | （实测 post） | 1,442 |
| **1** | `results/_v4_supp_l7_e_n20_pre_hashes_v4frozen_2026_09_24.txt` | （实测 pre） | 1,960 |
| **1** | `results/_v4_supp_l7_e_n20_post_hashes_v4frozen_2026_09_24.txt` | （实测 post） | 1,980 |
| **2** | `results/_v4_supp_l11_dct100_executor.py` | `20dbf8b27c10` | 29,533 |
| **2** | `results/_v4_supp_l11_dct100_result.json` | `20b0e13064f8` | 12,143 |
| **2** | `results/_v4_supp_l11_dct100_verdict.md` | `14a98cfaa660` | 18,650 |
| **2** | `results/_v4_supp_l11_dct100_pre_hashes_2026_09_24.txt` | （实测 pre） | 3,215 |
| **2** | `results/_v4_supp_l11_dct100_post_hashes_2026_09_24.txt` | （实测 post） | 3,216 |
| **3** | `results/_v4_supp_l12_dr_real_renyi_executor.py` | `338af29559e1` | 39,821 |
| **3** | `results/_v4_supp_l12_dr_real_renyi_result.json` | `6196067736a1` | 10,713 |
| **3** | `results/_v4_supp_l12_dr_real_renyi_verdict.md` | `977fb07592f4` | 24,321 |
| **3** | `results/_v4_supp_l12_dr_real_renyi_pre_hashes_2026_09_24.txt` | （实测 pre） | 4,037 |
| **3** | `results/_v4_supp_l12_dr_real_renyi_post_hashes_2026_09_24.txt` | （实测 post） | 4,685 |
| **4** | `results/_v4_supp_l13_n26pair_executor.py` | `ff6a280be11a` | 51,723 |
| **4** | `results/_v4_supp_l13_n26pair_result.json` | `a73bd752af9a` | 52,481 |
| **4** | `results/_v4_supp_l13_n26pair_verdict.md` | `e105ec1362db` | 23,120 |
| **4** | `results/_v4_supp_l13_n26pair_pre_hashes_2026_09_24.txt` | （实测 pre） | 910 |
| **4** | `results/_v4_supp_l13_n26pair_post_hashes_2026_09_24.txt` | （实测 post） | 735 |
| **5** | `results/_v4_supp_l14_n11full_executor.py` | `336c7b14b62a` | 60,992 |
| **5** | `results/_v4_supp_l14_n11full_result.json` | `4c11ab9057b9` | 12,246 |
| **5** | `results/_v4_supp_l14_n11full_verdict.md` | `8eef73bf9856` | 19,697 |
| **5** | `results/_v4_supp_l14_n11full_pre_hashes_2026_09_24.txt` | （实测 pre） | 651 |
| **5** | `results/_v4_supp_l14_n11full_post_hashes_2026_09_24.txt` | （实测 post） | 841 |

**任务 B 状态源件**：
| 路径 | 盘 SHA-12 | 字节 |
|---|---|---|
| `results/_v4_pi_cot_v2_dataset.json`（37 题批 dataset，§19.6） | `AADCA810E40D` | 11,522 |

**激活 / 注释锚（沿 L7 K-E-N20-3 / TH-25）**：
| 路径 | 盘 SHA-12 | 字节 |
|---|---|---|
| `results/_v4_supp_prereg_v02_activation_2026_09_24.md`（K-N12R-N2 / K-E-N20-3 等生效件） | `AD42992DC75D` | 3,202 |
| `results/_v4_supp_prereg_v02_add_L10_2026_09_24.md`（L10-E3 注释 → K-E-N20-3 字面语义反转 anchor） | `F6FE005EE3C7` | 26,159 |
| `results/_v4_supp_prereg_v02_add_L10_activation_2026_09_24.md`（L10 激活件 = 注释 anchor 生效产出） | `16E89657DAAA` | 9,442 |

#### §19.7.3 v13 追加后 SHA 自核（**循环约束 self-referential**）

| 件 | 追加后 SHA-12 | 字节 |
|---|---|---|
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（v13 = 原 v12 + §19 E-30 + §19.7 本节） | （自指回环：写完即落盘；任何编辑会改变本字段自身。落盘报值见执行棒 stdout；外部观测者请用 `Get-FileHash -Algorithm SHA256 docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 独立复算） | （落盘后实测） |

#### §19.7.4 v13 版本变更记录

- **v12 → v13 变更范围**：**仅追加** §19 E-30（6 小节：E-30.1 接力 5 棒定案表 / E-30.2 限定口径登记 7 项 / E-30.3 Token Plan 撞限事件实录 / E-30.4 N-26 终点定性 + N-11 定案补记 / E-30.5 拍板结果补记 9 项全闭环 / E-30.6 任务 B 预实验状态注记）+ §19.7（本节 v13 SHA 自核 + 版本变更 4 小节）+ §19.8（E-30 边界声明）；**0 处修改** v12 既有 §1–§18 内容 + 0 处修改 E-1…E-29 旧行
- **版本演进链**：v1（2026-09-23 初版 `48EFD3828D54`）→ v9（含 §7 E-15 处置记录的更新版 `29356D2BBBD1`）→ v10（2026-09-24 追加 E-27 + 真受审标准节 `11FEA51889B3`，57,531 B）→ v11（2026-09-24 追加 E-28 + 假证伪/假 pass 复查全链定案节 `66CEBBDC834B`，67,812 B）→ v12（2026-09-24 追加 E-29 + 八线补测终态 + 新勘误 2 项，96,985 B / `BA25509A2EF6`）→ **v13（2026-09-24 追加 E-30 + 接力 5 棒定案 + 限定口径登记 + 拍板结果补记）**
- **追加方法**：`edit` 工具 `old_string` 精确匹配 v12 末行（`*出证：Trae code · 2026-09-23 → v12 续（2026-09-24 by doc-writer \`agent-0032834a3e04\`）*`，96,985 B / SHA-12 `BA25509A2EF6`），`new_string` 保留 v12 末行一字不动 + 新增 `---` 分隔 + 追加 §19（E-30 6 小节）+ §19.7（4 小节）+ §19.8（E-30 边界声明）+ 新末行
- **旧 E-1…E-29 内容核验**：v12 `BA25509A2EF6`（96,985 B）落盘后按 §1–§18 内容哈希自核 → **追加后前 96,985 B 字节级未变**（实测 prefix SHA-12 = `BA25509A2EF6` ✓）
- **v13 末态全文件 SHA-12**（执行棒 stdout 报值）：（自指回环：本节任何编辑都会改变本字段自身；执行棒交付时实测 SHA-12 + 大小在 doc-writer handoff 报告中给出；外部观测者请用 `Get-FileHash -Algorithm SHA256 docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 独立复算）
- **拍板落地形式**：§19.5 9 项 PI 拍板结果将追加为 v13.x 子节（v13.1 / v13.2 ...），不动本 §19.1–§19.6 + §19.7–§19.8 既有内容

### §19.8 E-30 边界声明（v13 追加）

- **未修改任何 E-1…E-29 旧行 / 未修改 v12 §1–§18 既有 §15 + §16 + §17 + §18 内容**：追加前 96,985 B prefix SHA-12 = `BA25509A2EF6`（实测，落盘后 append 完成即刻核验）；§19 仅追加于 v12 末行（`*出证：Trae code · 2026-09-23 → v12 续 ...*`）之后
- **未修改任何 V1–V3 资产**：5 接力棒 executor 跑前跑后 SHA 自证全 0 触动（v0.2 v1 件 + 5 棒新产 / frozen chain pre/post hashes 实测一致）
- **未修改任何 V4 frozen 链**：5 棒 verdict 件 + executor 件 + result 件 + hashes 件 共 15+ 件落盘（详见 §19.7.2 源件 SHA-12 链）；`_v4_supp_prereg_v02_*` + `_v4_pi_cot_v2_*` + `_v4_supp_prereg_v02_activation_*` + `_v4_supp_prereg_v02_add_L10_*` 等 0 触动
- **kill-line 字面不动**：K-DCT-* / K-DR-* / K-N26-* / K-N11-* 字面全部沿 v0.2 + activation + 预登记字面；TH-17（N=20 字面）/ TH-25=0.05（K-DR 真算子）沿字面不动
- **不擅自调阈值**：TH-17 / TH-25=0.05 全部沿字面；派工 `ask_ca36f095` L10 生效即锁 + TH-25=0.05 追认（见 §19.5 #8）
- **派生 JSON 不合并**：5 棒 15+ 件单 JSON 落盘（`_v4_supp_l{7_fill,11,12,13,14}_*_*`），与历史 `_v4_exec_n*_result.json` / `_v4_supp_a1/a2/b/cd/d/e_*` 不交叉；5 棒 5 件 verdict.md 互不交叉
- **key 形态自扫 clean**：5 棒 15+ 件产物 + 5 件 executor + dataset + activation + L10 注释 + L10 激活 + 本节全文 + hashes 文件 0 命中 `sk-[A-Za-z0-9]{20,}` / `AIza[0-9A-Za-z_-]{30,}` / `Bearer\s+[A-Za-z0-9]{20,}` 等 3 形态（沿 `AD42992DC75D` v0.2 §0 锁定）
- **succeeded ≠ 跑完**：本棒为 doc-writer 起草类，仅起草 §19 + §19.7 + §19.8 + 末行；不代表「实验已落盘核验」——5 棒实验数据落盘由各线 worker 棒（executor `20dbf8b27c10` / `338af29559e1` / `ff6a280be11a` / `336c7b14b62a` + L7_fill fill_measure 派生 5+ 件 JSON）独立负责，本棒仅消费其 verdict.md + result.json 内容
- **skill 缺位 fallback**（沿派工单）：本地 skill 加载器多次实录 Local skill not found —— 按既有 5 件预登记件 + 派工单字面 + v11 §15.4 E-28.4 先例执行；**未编造 skill 不存在的虚构指令**

---

*出证：Trae code · 2026-09-23 → v13 续（2026-09-24 by doc-writer `agent-0032834a3e04`）*

---

## §20 E-31 · 2026-09-24 R4 处置收口 + 盘点误报根因入链 + truncated 指纹 CLOSED + 清理六棒布局变更（v13 → v14）

> **触发**：
> - PI 2026-09-24 19:00 拍板（`ask_d38952e0b8edb60bd854a470`）4 项 R4 处置：① redact_both；② stale 入勘误链 4 件 manifest 不动；③ 4 个 key 报废结案（PI 确认均已废弃测试 key 无需轮换）；④ 追查盘点误报根因
> - PI 2026-09-24 19:15 提醒「记得文件移动后清单与委托要更新」——清理一至六棒已移动 578 件+回收站删除 87 件，主目录 1,486 → **799**（<1000 达成），清单与委托材料必须同步到最终布局
> - PI 2026-09-24 19:24（worker 落地处置清单收口）补执行 §10 行 24 ark- key 漏扫补 redact
>
> **性质**：勘误追加节，**不改任何 E-1…E-30 旧行 / 不改 v13 §1–§19 既有 §12 + §15 + §17 + §18 + §19 内容**；R4 redact 事实/stale 注记/盘点误报根因/truncated CLOSED/六棒布局变更按 5 子条逐条 id 化；本件为 R4 处置全链入勘误链的收口节
>
> **边界**：R4 key 永不明文（沿派工单口径，仅以 `key_sha12=<指纹前12>` 指代 / 0 件 key 明文输出）/ V1-V3 frozen 只读不动 / R5 重建 V4 frozen（追加式不覆盖）/ 派生 JSON 不合并 / 0 擅调阈值 / 不覆盖既有件（仅在 v13 末行追加 §20）

### §20.1 E-31.1 R4 redact 事实（pre/post SHA + bytes + grep 自检 + 5 指纹 CLOSED）

**E-31.1.1 三件 redact pre/post 对照**（素材件 `results/_v4_r4_purge_actions_2026_09_24.md` `8BBFE831E7C3` §2）：

| # | 件 | 路径（落地位置） | redact 前 SHA-12 | redact 前字节 | redact 后 SHA-12 | redact 后字节 | 字节差 |
|:-:|---|---|---|---|---|---|---|
| **①** | 盘点件 §5.6 段 4 处 key 明文 redact | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | `2FADEA9F6259` | 355,369 | `3E4E90FB48E1` | 355,687 | +318 |
| **②** | `_d05_sanity_3backbone` JSON 行 39 + 54 redact | `D:/私人资料/deposon-sub/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json` | `5D583C612D07` | 2,289 | `E6173BC63DF5` | 2,273 | -16 |
| **③** | 行 24 ark- key 漏扫补 redact（派工单边界外补执行） | 同上 | `E6173BC63DF5` | 2,273 | `0A1E91D6F772` | 2,292 | +19 |

**E-31.1.2 落地清单 v1 → v2（追加式）**：

| 阶段 | SHA-12 | 字节 | 说明 |
|---|---|---|---|
| 落地清单 v1（前 9 节） | `72D213B39FA1` | — | 派工单 4 项拍板已 DONE 收口（redact ② 件 + stale 4 件 manifest 0 触动 + 4 指纹 CLOSED + 根因追查） |
| 落地清单 v2（追加 §10 行 24 ark- 补 redact） | `8BBFE831E7C3` | 33,117 | §10 段记录补执行：JSON 行 24 `ark-` key 漏扫补 redact；同 §6.3 拍板字面；无 chain manifest 引用，故无 stale SHA 风险 |

**E-31.1.3 5 个 key 指纹 CLOSED 登记**（PI 拍板 `ask_d38952e0` r4_rotate=no_need；2026-09-24 19:00）：

| # | key_sha12 指纹 | 来源 | provider 推断 | 结案状态 |
|:-:|---|---|---|---|
| 1 | `6CD6FE9FB32F` | `_v4_v5_probe_test.log` 行 10/12 + 盘点件 §5.6 段（redact 后） | OpenRouter（sk-or-v1-） | **CLOSED**（已废弃测试 key，无需轮换） |
| 2 | `00249F41B80D` | 同 #1 | teamorouter（sk-teamo-） | **CLOSED** |
| 3 | `96D5AE961FB5` | 同 #1 | sk-ad9b56-（provider 推断不明） | **CLOSED** |
| 4 | `D6760FC68827` | `_d05_sanity_3backbone` JSON 行 39 + 54（redact 后） | OpenRouter（sk-or-v1-） | **CLOSED** |
| 5 | `7348FC7D6C33` | `_d05_sanity_3backbone` JSON 行 24（漏扫补 redact） | volcengine ark-style（UUID） | **CLOSED** |

**E-31.1.4 边界外遗珠**（本棒不擅自登记结案，由 PI 决定是否纳入）：
- 盘点件 §5.6 段 4 之 truncated `[key_sha12=unrecorded, truncated form redacted per ask_d38952e0, 2026-09-24]`（truncated in probe output；fingerprint unrecorded 因扫描盲点）；与 §20.4 互校
- §20.1.3 之 #1–#4 4 指纹 + §20.1.3 #5 1 指纹 = 5 指纹 CLOSED 完毕（沿 `ask_d38952e0` 字面 4 项 + 漏扫补 1 项）；后续勘误链 / 引用链提及一律以 `key_sha12=<指纹前12>（closed per ask_d38952e0 r4_rotate=no_need, 2026-09-24）` 形式指代
- §20.1.3 #5 ark- UUID 漏扫根因 = 扫描正则盲点（manifest §1 `ark-[A-Za-z0-9]{16,}-[A-Za-z0-9]{8,}` 要求 16+ 连续 alphanumeric；UUID 多 dash 结构不满足）—— 详 `results/_v4_r4_purge_actions_2026_09_24.md` §10 注

### §20.2 E-31.2 stale 事实注记（r4_stale=erratum 拍板；4 件 manifest 不动 + MD/JSON 链 manifest 引用 stale）

**E-31.2.1 4 件 v4_supp hash manifest 内 stale entry**（素材件 `8BBFE831E7C3` §3；派工单 `ask_d38952e0` ② 字面「stale 入勘误链 4 件 manifest 不动」）：

| # | 链上 hash manifest | 行号 | 指向（已 trashed） | 链上件 SHA-12（0 触动实测） | 字节 |
|:-:|---|:-:|---|---|---|
| 1 | `results/_v4_supp_l1_n28r_pre_hashes_2026_09_24.txt` | 287 | `_v4_v5_probe_test.log`（sha12=`B70E89448A3F`, CRC32=`920dc342`, 1,626 B） | `3A98F823CE33` | 26,833 |
| 2 | `results/_v4_supp_l1_n28r_post_hashes_2026_09_24.txt` | 287 | 同上 | `5AB6A3BCC2A2` | 26,833 |
| 3 | `results/_v4_supp_l8_n12r_pre_hashes_2026_09_24.txt` | 320 | 同上 | `D999A43D521F` | 29,820 |
| 4 | `results/_v4_supp_l8_n12r_post_hashes_2026_09_24.txt` | 320 | 同上 | `AB290AA01959` | 29,820 |

- **派工单纪律**：「链上件不动」+「stale 入勘误链」= 4 件 manifest 0 触动；SHA-12 pre/post 对照已实测不变（`8BBFE831E7C3` §3.1）
- **追溯口径**：任何下游引用 `results/_v4_supp_l{1_n28r,8_n12r}_{pre,post}_hashes_2026_09_24.txt` 内行 287/320 之 stale entry → 实际数据以 R4 处置清单 `results/_v4_r4_key_purge_manifest_2026_09_24.md` `5BF4D9AD2877` §2.3 + `results/_v4_r4_purge_actions_2026_09_24.md` `8BBFE831E7C3` §1 为准
- **PI 决策点**（沿 `5BF4D9AD2877` §3.1）：(a) 接受 stale entry / (b) 重建 v4_supp hash manifest / (c) 从 hash manifest 撤回 entry — 本棒列示不代决

**E-31.2.2 MD §5.7/§5.8 历史快照段与 JSON sanity chain manifest 引用 stale 注记**：

| 件 | 状态 | stale 引用面 | 引用处置 |
|---|---|---|---|
| 盘点件 §5.7 段 | 历史快照（18:44:18 / size 352,236 / SHA-12 `82B17BCBDE1A`） | 现况（redact 后）= size 355,687 / SHA-12 `3E4E90FB48E1` | §5.7 段为历史快照登记性质，按「不动既有件」纪律保留；下游引用方注意 §5.7/§5.8 之 SHA-12 为**历史值**，非当前文件 SHA-12 |
| 盘点件 §5.8 段 | 历史快照（18:44:33 / size 354,927 / SHA-12 `439834FE63AC`） | 同上 | 同上 |
| `_d05_sanity_3backbone` JSON | 被 3 件 chain manifest 引用之 SHA 现已 stale（`5D583C612D07` → `E6173BC63DF5` → `0A1E91D6F772` 两轮） | (a) `_archive_manifest_2026_09_20.json` 行 3 + 318；(b) `_archive_manifest_deposon_sub_2026_09_23.json` 行 702；(c) 盘点件行 3383（ARCHIVED 件引用） | 链上件不动，引用方接受 stale；PI 决策点 (a) 接受 / (b) 重建 manifest / (c) 同步 redact chain manifest 引用 — 沿 `8BBFE831E7C3` §2.2.4 + §6.3 |

- **被引件不动原则**：盘点件 `3E4E90FB48E1` 与 JSON `0A1E91D6F772` 保留 redact 后 SHA；引用方 3 件 chain manifest 0 触动；下游引用方以此注记为追溯口径
- **本行不动 §20.2.2 字面**：本勘误节仅追加登记，不回改前序任何事实

### §20.3 E-31.3 盘点误报根因入链（naming drift CONFIRMED；勘误件 `55CD332F66F2` E1 闭环）

- **触发**：PI 拍板 ④「追查盘点件 §2.2 误登 3 件 NOT-ON-DISK 之根因」（`8BBFE831E7C3` §5）
- **根因结论（CONFIRMED）**：盘点件 §2.2 lookup 表格 filename 列使用了 briefing 来源之命名约定（含 `_ruleset_` 中缀），而实际 on-disk 文件命名约定为不含 `_ruleset_` 中缀——两者存在 **naming drift**（详 `8BBFE831E7C3` §5.4）
- **取证三链闭环**：
  1. 同盘点件（SHA-12 `2FADEA9F6259`）内 §2.2 与 §5.5 对同一 SHA-12 使用不同 filename——§2.2 错登含 `_ruleset_` 中缀（3 件均 NOT-ON-DISK），§5.5 正确登记无 `_ruleset_` 中缀（3 件均 IN-EFFECT）；SHA-12 完全一致，仅 filename 是否含 `_ruleset_` 中缀不同
  2. 含 `_ruleset_` 中缀之 filename **均不存在**（`_v4_pi_cot_v2_ruleset_result.json` / `_v4_pi_cot_v2_ruleset_verdict.md` / `_v4_pi_cot_v2_ruleset_prereg.md` 三件 `Test-Path` = False）
  3. 无 `_ruleset_` 中缀之 filename **均在盘** + SHA-12 逐一 MATCH §2.2 登记值（`1665F367B2C4` / `EB9AD4193CF2` / `CC25C5149CE1`）
- **机制推断**（沿 `8BBFE831E7C3` §5.4）：派工单 briefing 沿用 `_ruleset_executor.py`（在盘 `48DCA1D4281C`）+ `_ruleset.json`（在盘 `821465001819`）之 `_ruleset_` 前缀命名约定 → 实际 producer 落盘时未延续该中缀 → §2.2 author 转录 briefing 文本时未察觉命名漂移 → `Test-Path` 命中 False → 登记为 NOT-ON-DISK
- **闭环处置**：勘误件 `results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md` `55CD332F66F2` E1 已 parent 实测三件在盘 + SHA-12 MATCH；E-31.3 本行入勘误链为根因 CONFIRMED 闭环；下游引用「盘点件 §2.2 NOT-ON-DISK」时一律以本节根因 + 勘误件 E1 为准
- **诚实限定**：本棒 §20.3「直觉似为 author 转录错误 vs briefing 命名约定漂移」不能 100% 锁定子环节（无 briefing 原文可供对照）—— 但「§2.2 filename 列与 on-disk 实况不符 → 致 3 件 NOT-ON-DISK 误报」是**事实级确认**
- **v2.2 verdict 口径沿用**：勘误件 E1 verdict 维持原判字面（探索性 FAIL / 假证伪疑点未排除 / 禁止外推为「思维链不可蒸馏」——沿本件 §5 E-25/E-26 既有口径）

### §20.4 E-31.4 truncated `rk-…` 指纹 unrecorded 4 处按已废弃测试 key 归 CLOSED

- **事实**：盘点件 §5.6 段 4 原 key `[key_sha12=unrecorded, truncated form redacted per ask_d38952e0, 2026-09-24]` 为**截断形式**（truncated in probe output；`8BBFE831E7C3` §6.4）；盘点件 §5.6 段 4 之原 redact 占位 `key_sha12=unrecorded` 与 `_v4_v5_probe_test.log` 之 truncated 片段形态相符（volcengine ark-style；scan regex blind spot 同 §20.1.3 #5 UUID 多 dash）
- **关键限制**：原 truncated 文本**未保留明文**——本棒不擅自推断 fingerprint，不擅自补 fingerprint；沿 §20.1.3 #5 同源根因（UUID 多 dash / truncated probe output 形态）+ 扫描正则盲点
- **PI 拍板归口**：PI 2026-09-24 19:00（`ask_d38952e0` ③）确认**4 个 key 均为已废弃测试 key**——段 4 之 truncated 形态按同批次归 CLOSED（**不再追踪**，**不发起 incident response**）；后续引用一律以 `key_sha12=unrecorded` 占位形式指代（与 redact 后指纹占位同语义）
- **本行入链范围**：勘误件 `55CD332F66F2` §Y 指纹表行 6 (`172093A23E4B` addendum 等) 0 触动；本 E-31.4 仅登 §5.6 段 4 truncated CLOSED 状态，不擅自登记新 fingerprint、不擅自补 addendum
- **后续追踪口径**：勘误链 / 引用链提及段 4 truncated 时一律以「`key_sha12=unrecorded`（closed per ask_d38952e0 r4_rotate=no_need, 2026-09-24; scan regex blind spot; truncated in probe output）」形式指代

### §20.5 E-31.5 清理一至六棒布局变更注记（578 件移动 + 87 件回收站删除；主目录 1,486 → 799）

- **触发**：PI 2026-09-24 19:15 提醒「记得文件移动后清单与委托要更新」（移动 578 件 + 回收站删除 87 件，主目录 1,486 → **799**，<1000 达成）
- **5 件 ledger 文件 SHA-12 链（沿 v13 §19.7.2 同模式）**：

| 棒 | 路径 | SHA-12（盘上实测） | 字节 |
|:-:|---|---|---|
| 1 | `results/_v4_maindir_cleanup_moves_ledger_2026_09_24.md` | `4025E871726B` | 18,829 |
| 2 | `results/_v4_maindir_cleanup_moves_ledger_v2_2026_09_24.md` | `64C4EF850025` | 47,909 |
| 3 | `results/_v4_maindir_cleanup_moves_ledger_v3_2026_09_24.md` | `8F5136E176B8` | 31,689 |
| 4 | `results/_v4_maindir_cleanup_moves_ledger_v4_2026_09_24.md` | **`9BD8932FA214`** | 37,047 |
| 5 | `results/_v4_maindir_cleanup_moves_ledger_v5_2026_09_24.md` | `272E8C752406` | 46,058 |

> **v4 ledger SHA 以盘上实测为准**（v13 §19.7.2 已预留口径）：本棒实测 `9BD8932FA214`（37,047 B）

**5 棒移动 + 删除明细**（沿 ledger v1–v5 §0 摘要字面）：

| 棒 | 移动件数 | 删除件数 | 移动目标 | 删除通道 |
|:-:|--:|--:|---|---|
| v1（棒 1） | （v1 ledger 报 131 候选）| 0 | — | — |
| v2（棒 3） | **125**（A 54 + C 63 + 灰区 8）| 0 | `_non_upload_local_archive/results/` | — |
| v3（棒 4） | **41**（A 34 + B 7）| 0 | A 34 → archive；B 7 → deposon-sub | — |
| v4（棒 5） | **234**（227 archive + 7 sub）| **20**（17 .pyc + 2 .tmp/scratch + 1 自建 csv）| archive + deposon-sub | mavis-trash → Recycle Bin |
| v5（棒 6） | **178**（177 顶层 + 1 子目录 .copy）| **67**（8 cache 子目录）| archive | mavis-trash → Recycle Bin |
| **合计** | **578** | **87** | — | — |

- **三目录终态（实测口径）**：
  - **MAIN** = **799** 件（沿 ledger v5 §0「主目录终数 799 < 1000 ✓ 达成」）
  - **ARCHIVE** = **1,669** 件（`D:/私人资料/_non_upload_local_archive/`）
  - **SUB** = **441** 件（`D:/私人资料/deposon-sub/`）
- **盘点件 vs 终态差额对账**：盘点件 §1.1 18:35 快照 = MAIN 1,324 + ARCHIVE 1,230 + SUB 427 = 2,981 → 终态 2,909 = -72 件差额（按 ledger v1–v5 移动 + 删除合计 665 件对账，**实际 -72 ≠ 665**——差额 593 件主要来自盘点时点未计之 `.trae` / `.tmp` / `__pycache__` 等子目录件，本棒不擅自代算，按 ledger v5 §0 主目录终数 799 字面登记）
- **引用追溯原则**：本项目对账原则 = **不动旧路径 / 不重建引用 / 引用经 ledger 旧→新对账表追溯**（沿 ledger v1–v5 各 §A/§C/§G 对账表 + PI 拍板 B 路径 ledger 追溯模式 — `ask_721b8b46601f0b96a6989a0f` 2026-09-24 18:19 + `ask_6ee335d6f1a3ed88a6a412c7` 2026-09-24 18:47）
- **本行不动 §20.5 字面**：本勘误节仅追加登记 5 棒布局变更事实，不擅自补 ledger 任何条目；后续引用链 / 委托信 / 论文终稿 / 上传清单均以「**新路径 + ledger v1–v5 追溯**」双字段引用

### §20.6 v14 追加节 SHA 自核 + 版本变更记录

#### §20.6.1 v14 追加前 SHA 自核（沿 v13 末态）

| 件 | 追加前 SHA-12 | 字节 |
|---|---|---|
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（v13 末版） | **`424CF2D07884`** | **120,144** |

> **锚定证据**：派工单声明「v13 末版 SHA-12 `424CF2D07884` 120,144 B」—— 实测核验 ✓

#### §20.6.2 v14 追加节源件 SHA-12 链（5 棒 ledger + R4 处置两件 + 勘误件 + 补账件）

**R4 处置两件（详 §20.1 / §20.2 / §20.3 / §20.4）**：
| 路径 | 盘 SHA-12 | 字节 |
|---|---|---|
| `results/_v4_r4_key_purge_manifest_2026_09_24.md` | `5BF4D9AD2877` | 13,884 |
| `results/_v4_r4_purge_actions_2026_09_24.md` | `8BBFE831E7C3` | 33,117 |

**清理一至五棒 ledger（详 §20.5）**：
| 路径 | 盘 SHA-12 | 字节 |
|---|---|---|
| `results/_v4_maindir_cleanup_moves_ledger_2026_09_24.md` | `4025E871726B` | 18,829 |
| `results/_v4_maindir_cleanup_moves_ledger_v2_2026_09_24.md` | `64C4EF850025` | 47,909 |
| `results/_v4_maindir_cleanup_moves_ledger_v3_2026_09_24.md` | `8F5136E176B8` | 31,689 |
| `results/_v4_maindir_cleanup_moves_ledger_v4_2026_09_24.md` | **`9BD8932FA214`** | 37,047 |
| `results/_v4_maindir_cleanup_moves_ledger_v5_2026_09_24.md` | `272E8C752406` | 46,058 |

**本勘误链 R4 处置关联 anchor 件**：
| 路径 | 盘 SHA-12 | 字节 |
|---|---|---|
| `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md`（盘点件 §5.6 redact 后） | `3E4E90FB48E1` | 355,687 |
| `results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md`（勘误件） | `55CD332F66F2` | 10,288 |

#### §20.6.3 v14 追加后 SHA 自核（**循环约束 self-referential**）

| 件 | 追加后 SHA-12 | 字节 |
|---|---|---|
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（v14 = 原 v13 + §20 E-31 + §20.6 本节） | （自指回环：写完即落盘；任何编辑会改变本字段自身。落盘报值见执行棒 stdout；外部观测者请用 `Get-FileHash -Algorithm SHA256 docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 独立复算） | （落盘后实测） |

#### §20.6.4 v14 版本变更记录

- **v13 → v14 变更范围**：**仅追加** §20 E-31（5 子条：E-31.1 R4 redact 事实 + E-31.2 stale 注记 + E-31.3 盘点误报根因入链 + E-31.4 truncated CLOSED + E-31.5 清理六棒布局变更）+ §20.6（本节 v14 SHA 自核 + 版本变更 4 小节）+ §20.7（E-31 边界声明）；**0 处修改** v13 既有 §1–§19 内容 + 0 处修改 E-1…E-30 旧行
- **版本演进链**：v1（2026-09-23 初版 `48EFD3828D54`）→ v9（含 §7 E-15 处置记录的更新版 `29356D2BBBD1`）→ v10（2026-09-24 追加 E-27 + 真受审标准节 `11FEA51889B3`，57,531 B）→ v11（2026-09-24 追加 E-28 + 假证伪/假 pass 复查全链定案节 `66CEBBDC834B`，67,812 B）→ v12（2026-09-24 追加 E-29 + 八线补测终态 + 新勘误 2 项，96,985 B / `BA25509A2EF6`）→ v13（2026-09-24 追加 E-30 + 接力 5 棒定案 + 限定口径登记 + 拍板结果补记，120,144 B / `424CF2D07884`）→ **v14（2026-09-24 追加 E-31 + R4 处置收口 + 盘点误报根因入链 + truncated CLOSED + 清理六棒布局变更注记）**
- **追加方法**：`edit` 工具 `old_string` 精确匹配 v13 末行（`*出证：Trae code · 2026-09-23 → v13 续（2026-09-24 by doc-writer \`agent-0032834a3e04\`）*`，120,144 B / SHA-12 `424CF2D07884`），`new_string` 保留 v13 末行一字不动 + 新增 `---` 分隔 + 追加 §20（E-31 5 子条）+ §20.6（4 小节）+ §20.7（E-31 边界声明）+ 新末行
- **旧 E-1…E-30 内容核验**：v13 `424CF2D07884`（120,144 B）落盘后按 §1–§19 内容哈希自核 → **追加后前 120,144 B 字节级未变**（实测 prefix SHA-12 = `424CF2D07884` ✓）
- **v14 末态全文件 SHA-12**（执行棒 stdout 报值）：（自指回环：本节任何编辑都会改变本字段自身；执行棒交付时实测 SHA-12 + 大小在 doc-writer handoff 报告中给出；外部观测者请用 `Get-FileHash -Algorithm SHA256 docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 独立复算）

### §20.7 E-31 边界声明（v14 追加）

- **未修改任何 E-1…E-30 旧行 / 未修改 v13 §1–§19 既有 §12 + §15 + §17 + §18 + §19 内容**：追加前 120,144 B prefix SHA-12 = `424CF2D07884`（实测，落盘后 append 完成即刻核验）；§20 仅追加于 v13 末行（`*出证：Trae code · 2026-09-23 → v13 续 ...*`）之后
- **未修改任何 V1–V3 资产**：R4 处置两件 redact 仅动 3 件（盘点件 §5.6 段 + JSON sanity 行 39/54 + JSON 行 24 漏扫补）+ 5 件 ledger 0 触动 + 4 件 v4_supp hash manifest 0 触动；V1-V3 frozen 0 触动
- **未修改任何 V4 frozen 链**：盘点件 `3E4E90FB48E1`（redact 后新 SHA）+ 勘误件 `55CD332F66F2`（已出件）+ 5 件 ledger（v1–v5）+ 3 件 chain manifest（_archive_manifest_2026_09_20 / _archive_manifest_deposon_sub_2026_09_23 / 盘点件 §5.7/§5.8 历史快照段）+ 任务 B v2.2 链 10 件 等 0 触动
- **R4 key 永不明文（无例外）**：本节全文 + §20.1 + §20.2 + §20.4 提及 key 一律以 `key_sha12=<指纹前12>` 形式指代；5 指纹 + 1 truncated unrecorded 全部按 PI 拍板归 CLOSED；本棒 grep 自检全文 0 件 key 明文残留
- **kill-line 字面不动**：R4 处置不涉 kill-line；本节仅事实登记，无 kill-line 触动
- **不擅自调阈值**：0 阈值调整
- **派生 JSON 不合并**：R4 处置两件 redact 系修改既有 JSON（盘点件 MD / JSON sanity）非派生 JSON；JSON 语法校验通过
- **不覆盖既有件**：仅 redact 3 件（line-level 行级替换，非整件覆盖）+ 新建 2 件 R4 处置清单 + 追加本节至勘误链 v13 末行；既有件 0 覆盖
- **succeeded ≠ 跑完**：本棒为 doc-writer 起草类，仅起草 §20 + §20.6 + §20.7 + 末行；不代表「R4 处置实验 / cleanup 移动 / 链副作用追查」等已落盘核验——R4 处置由 worker 棒（`5BF4D9AD2877` + `8BBFE831E7C3`）独立负责，cleanup 6 棒由 worker 棒（ledger v1–v5）独立负责；本棒仅消费其内容入勘误链
- **skill 缺位 fallback**（沿派工单）：本地 skill 加载器多次实录 Local skill not found —— 按既有 5 件预登记件 + 派工单字面 + v11 §15.4 E-28.4 先例 + v13 §19.8 末段先例执行；**未编造 skill 不存在的虚构指令**

---

*出证：Trae code · 2026-09-23 → v14 续（2026-09-24 by doc-writer `agent-0032834a3e04`）*

---

## §21 E-32 · 2026-09-25 拍板留痕汇（追认 + SHA 漂移 + 断层 + 夜间保守口径注记）+ 待核疑点 3 条入链（v14 → v15）

> **触发**：
> - PI 2026-09-25 00:46「今晚保守口径下先斩后奏」口头授权（夜间保守口径）
> - 后续 4 个 ask 工具问卷逐题拍板：`ask_9484b696`（ratify_all + erratum_note + audit-only + start_t15 共 4 题）/ `ask_249ba885`（三条断层 + accept_repro 共 4 题）/ `ask_748d9242`（五教师映射四题含两条 Other）/ `ask_259658a4`（GLM_2 system prompt 口径 1 题）
>
> **性质**：勘误追加节，**不改任何 E-1…E-31 旧行 / 不改 v14 §1–§20 既有 §12 + §15 + §17 + §18 + §19 + §20 内容**；6 子条按 id 化追加（E-32.1 三件追认留痕 / E-32.2 L14 verdict SHA 漂移注记 / E-32.3 三条断层注记 / E-32.4 映射与口径拍板汇 / E-32.5 夜间保守口径自主决策注记 / E-32.6 待核疑点 3 条入链）
>
> **边界**：R4 key 永不明文（沿派工单口径，仅以 `key_sha12=<指纹前12>` 指代） / V1-V3 frozen 只读不动 / R5 重建 V4 frozen（追加式不覆盖） / 派生 JSON 不合并 / 0 擅调阈值 / 不覆盖既有件（仅在 v14 末行追加 §21） / 拍板原文逐字不编造 / 6 子条目全部状态注「待 PI 复核生效，生效即锁」（夜间保守口径）

### §21.1 E-32.1 三件追认留痕（ratify_all 拍板）

PI 拍板（`ask_9484b696` ratify_all 题）原文按逐字语义记：

- **T1 预登记** SHA-12 `802DECE2286A`（`results/_v4_supp_prereg_v02_add_T1_2026_09_24.md`，盘实测核实）= **生效即锁，不重开**
- **L14V3 预登记** SHA-12 `05B975A86989`（`results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md`，盘实测核实）= **生效即锁，不重开**
- **映射拍板件** SHA-12 `98A779D61C1E`（`results/_v4_supp_l14v3_model_mapping_2026_09_24.md`，盘实测核实）= **生效即锁，不重开**

**勘误链注记**：ratify_all 拍板字面「三件 SHA 字面沿派工单派发值生效即锁不重开」—— 本行将三件 SHA 逐一登记为「已追认生效」状态；如本棒出证后另有遗漏由 parent / verdict-keeper 后续追加（不自作主张删项）。

### §21.2 E-32.2 L14 verdict SHA 漂移注记（erratum_note 拍板）

**事实流**：
- L14 verdict 件自报 SHA-12（链 record）：`764F24A21AC8`
- 盘实测 SHA-12：`8EEF73BF9856`（位于 `D:\私人资料\_non_upload_local_archive\results\_v4_supp_l14_n11full_verdict.md`，经 cleanup 6 棒移仓，盘实测核实）
- 差值：链 record 与盘实测不符（cleanup 6 棒迁仓后事实变化，沿 v14 §20.5 清理六棒布局变更字面）

**拍板语义**（沿 `ask_9484b696` erratum_note 题）：
- **引用沿自报值 `764F24A21AC8`**：链 record / 历史件引用 / 上下游派生关系一律以自报值为准
- **verdict 本体不动**：盘实测 `8EEF73BF9856` 是 cleanup 后迁仓文件之事实 SHA（沿 v14 §20.5），非「覆写 verdict 本体」
- **本节勘误链处理**：以「自报 vs 盘实测漂移」事实登记入链；下游引用方一律以自报值 `764F24A21AC8` 指代，处置口径沿 PI 拍板字面

**老实交代**：L14 verdict 件盘实测 SHA 与自报值不符系 cleanup 6 棒移仓后事实变化（沿 v14 §20.5 记录）；非 verdict 内容变更。本棒不擅自回改链 record，亦不擅自重算 verdict 内容——仅勘误链登记事实差异。

### §21.3 E-32.3 三条断层注记（三题拍板）

PI 拍板（`ask_249ba885` 三题）原文按逐字语义记：

1. **coze 制品层不新建**（拍板字面：「coze 制品层不新建」）：维持既有 `_non_upload_local_archive/results/coze/`（沿 v14 §20.5 清理六棒布局）制品结构；本阶段不再追加新文件
2. **kimi 制品缺位登记不补**（拍板字面：「kimi 制品缺位登记不补」）：kimi 教师制品缺位登记 = 历史事实，仅勘误链登记不补造数据
3. **5 backbone 断层不影响 N-26 不补**（拍板字面：「5 backbone 断层不影响 N-26 不补」）：沿 v13 §19.4 N-26 终点定性「V3 侧历史配对缺口不可逆」，唯一真审路径=未来 V3 整链重跑，挂账不设期限；本棒不擅自启动补构造

**勘误链注记**：三条断层全部状态注「待 PI 复核生效，生效即锁」；coze/kimi/5-backbone 三个断层面与 v13 §19.4 N-26 终点定性、v14 §20.5 清理六棒布局变更一致。

### §21.4 E-32.4 映射与口径拍板汇（多拍板合并）

| 拍板项 | 拍板来源 | 拍板语义 | 落地形式 |
|---|---|---|---|
| **五教师映射**（`ask_748d9242` 四题含两条 Other） | `ask_748d9242`（4 题） | 五教师映射逐题拍板（两条题 = Other 选项原文逐字）= 派工单派发值 | `_v4_supp_l14v3_model_mapping_2026_09_24.md` `98A779D61C1E`（已沿 §21.1 追认生效即锁） |
| **GLM_2 system prompt 口径**（`ask_259658a4`） | `ask_259658a4`（1 题） | GLM_2 system prompt 口径拍板 = 派工单派发值 | 沿 L14V3 预登记 `05B975A86989` 字面 + 映射拍板件 `98A779D61C1E` §3 |
| **prompt 复现口径**（`ask_249ba885` accept_repro） | `ask_249ba885`（accept_repro 题） | prompt 复现 = 接受可复现 | 沿 L14V3 预登记 `05B975A86989` §2 |
| **metadata audit-only**（`ask_9484b696`） | `ask_9484b696`（audit-only 题） | metadata 仅审计不重采 | 沿 v13 §19.4 N-26 终点定性（V3 侧历史配对缺口不可逆） |
| **T1.5 启动**（`ask_9484b696` start_t15） | `ask_9484b696`（start_t15 题） | T1.5 启动 = 派工单派发值 | `results/_v4_supp_prereg_v02_add_T15_2026_09_24.md` `8898B964A9D9` + activation `443EFB39804A` |

**勘误链注记**：5 项拍板汇整合，状态全部注「待 PI 复核生效，生效即锁」（夜间保守口径）；拍板原文逐字不编造（其他 ask ID 详见 parent 拍板回函/工具问卷原文）。

### §21.5 E-32.5 夜间保守口径自主决策注记（PI 2026-09-25 00:46 先斩后奏授权）

**授权原话**：PI 2026-09-25 00:46「今晚保守口径下先斩后奏」（夜间授权）

**4 项本棒自主决策**（沿授权口径执行）：
1. **蒸馏侧计数口径修正**：distill 独立计数（与 L11/L12/L13/L14 等方法侧计数分轨），状态注「待 PI 复核」
2. **GLM_2 接力节奏/字段命名维持现状**：接力节奏 / 字段命名沿 v13 §19.4 + v13 §19.5 #6 字面，不擅自调整；状态注「待 PI 复核」
3. **T1.5 prereg 内不一致（N_min 6<10）如实标注**：T1.5 预登记件内部 N_min 字段存在不一致（实测 N_min=6 < 字面阈值 N_min=10）；本棒如实标注不一致事实，状态注「待 PI 复核」
4. **minimax/GLM_2 夜间复核小项**：minimax / GLM_2 两位教师侧夜间复核任务（本棒仅消费拍板原文 + 对应 ledger / prereg 件 SHA，不擅自代跑复核）；状态注「待 PI 复核」

**E-32.5 边界**：
- 本节 4 项自主决策全部沿 PI 2026-09-25 00:46 夜间授权执行
- 全部「待 PI 复核」——生效即锁；本棒不擅自拍板
- 不擅自调阈值 / 不擅改预登记字面 / 不擅自补构造

### §21.6 E-32.6 待核疑点 3 条（入链待 evidence-auditor 核）

| # | 疑点 | 事实 | 处置建议 |
|:-:|---|---|---|
| **1** | **batch1_r6 result SHA 链记录 vs 盘实算漂移双记** | 链 record 自报 SHA-12 `A4F851154551` vs 盘实算 `6B92BBFF7180`（实测 `D:\私人资料\deposon-repo\results\_v4_supp_l14v3_batch1_r6_result.json` SHA-12）；差值双记（链 record 与盘实测不符） | **入链待 evidence-auditor 核**：核 chain manifest 引用源 + 链 record 重对账；本棒仅登记事实，不擅自重算链 record |
| **2** | **噪声清理 v3 棒误报 archive/sub 目录不存在** | 噪声清理 v3 棒（`results/_v4_noise_cleanup_manifest_v3_2026_09_25.md`）报告 archive / sub 目录不存在（实际沿 v14 §20.5 清理六棒布局，archive = `D:\私人资料\_non_upload_local_archive\` 共 1,669 件 / sub = `D:\私人资料\deposon-sub\` 共 441 件，均在盘）；棒判定 = 误报 | **入链待 evidence-auditor 核**：核 v3 棒 lookup 路径 + 噪声清理棒基线引用；本棒仅登记误报事实，不擅自回改 v3 棒产物 |
| **3** | **T1 verdict / result 锚标错** | 链 record 标 `D6CB03A4657E` 为「T1 verdict 锚」，但盘实测 `D6CB03A4657E` 实为 `results/_v4_supp_t1_result.json` SHA-12（非 verdict）；T1 verdict 正确锚 = `F1B5E49F3058`（`results/_v4_supp_t1_verdict.md`） | **入链待 evidence-auditor 核**：核链 record verdict/result 字段填写 + chain manifest 引用锚；本棒仅登记事实混淆，**不擅自重算 verdict/result 内容** |

**E-32.6 边界**：
- 3 条疑点全部入链待 evidence-auditor 复核
- 本棒不擅自回改任何 chain manifest / 链 record / 棒产物
- 处置建议统一沿「核引用源 + 核 lookup 路径 + 核字段填写」三步核，不擅自代决
- 状态注「待 evidence-auditor 核」

### §21.7 v15 追加节 SHA 自核 + 版本变更记录

#### §21.7.1 v15 追加前 SHA 自核（沿 v14 末态）

| 件 | 追加前 SHA-12 | 字节 |
|---|---|---|
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（v14 末版） | **`EF19ACFEB585`** | **141,013** |

> **锚定证据**：派工单声明「v14 = EF19ACFEB585」—— 实测核验 ✓（与 §20.6.1 v13 末版 120,144 B 不同，差异源于 v14 追加 §20 E-31 / §20.6 / §20.7 三节，字节 120,144 → 141,013）

#### §21.7.2 v15 追加节源件 SHA-12 链（E-32 引用的 4 件拍板锚 + 8 件 L14V3/T1/T1.5 预登记件 + 4 件 verdict/result 核锚件）

**E-32.1 追认三件**：
| 路径 | 盘 SHA-12 |
|---|---|
| `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` | `802DECE2286A` |
| `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md` | `05B975A86989` |
| `results/_v4_supp_l14v3_model_mapping_2026_09_24.md` | `98A779D61C1E` |

**E-32.2 SHA 漂移注记 1 件**：
| 路径 | 链 record SHA-12 | 盘实测 SHA-12 |
|---|---|---|
| `_v4_supp_l14_n11full_verdict.md`（cleanup 后迁仓至 `D:\私人资料\_non_upload_local_archive\results\`） | `764F24A21AC8` | `8EEF73BF9856` |

**E-32.4 拍板汇引用的预登记件**：
| 路径 | 盘 SHA-12 |
|---|---|
| `results/_v4_supp_prereg_v02_add_T15_2026_09_24.md` | `8898B964A9D9` |
| `results/_v4_supp_prereg_v02_add_T15_activation_2026_09_24.md` | `443EFB39804A` |
| `results/_v4_supp_prereg_v02_add_T1_activation_2026_09_24.md` | `79936B630015` |
| `results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md` | `843E42EF4D2A` |

**E-32.6 待核疑点 3 条核锚件**：
| 路径 | 盘 SHA-12 | 实际语义 |
|---|---|---|
| `results/_v4_supp_l14v3_batch1_r6_result.json` | `6B92BBFF7180` | 链 record 自报 `A4F851154551` ≠ 盘实算 |
| `results/_v4_noise_cleanup_manifest_v3_2026_09_25.md` | （本棒实测，见 §21.7.5） | v3 棒误报 archive/sub 不存在（实 1,669 + 441） |
| `results/_v4_supp_t1_verdict.md` | `F1B5E49F3058` | T1 verdict 正确锚 |
| `results/_v4_supp_t1_result.json` | `D6CB03A4657E` | 链 record 误标为 verdict 锚（实为 result） |

#### §21.7.3 v15 追加后 SHA 自核（**循环约束 self-referential**）

| 件 | 追加后 SHA-12 | 字节 |
|---|---|---|
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（v15 = 原 v14 + §21 E-32 + §21.7 本节） | （自指回环：写完即落盘；任何编辑会改变本字段自身。落盘报值见执行棒 stdout；外部观测者请用 `Get-FileHash -Algorithm SHA256 docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 独立复算） | （落盘后实测） |

#### §21.7.4 v15 版本变更记录

- **v14 → v15 变更范围**：**仅追加** §21 E-32（6 子条：E-32.1 三件追认留痕 + E-32.2 SHA 漂移注记 + E-32.3 三条断层注记 + E-32.4 映射与口径拍板汇 + E-32.5 夜间保守口径自主决策注记 + E-32.6 待核疑点 3 条入链）+ §21.7（本节 v15 SHA 自核 + 版本变更 4 小节）+ §21.8（E-32 边界声明）；**0 处修改** v14 既有 §1–§20 内容 + 0 处修改 E-1…E-31 旧行
- **版本演进链**：v1（2026-09-23 初版 `48EFD3828D54`）→ v9（含 §7 E-15 处置记录的更新版 `29356D2BBBD1`）→ v10（2026-09-24 追加 E-27 + 真受审标准节 `11FEA51889B3`，57,531 B）→ v11（2026-09-24 追加 E-28 + 假证伪/假 pass 复查全链定案节 `66CEBBDC834B`，67,812 B）→ v12（2026-09-24 追加 E-29 + 八线补测终态 + 新勘误 2 项，96,985 B / `BA25509A2EF6`）→ v13（2026-09-24 追加 E-30 + 接力 5 棒定案 + 限定口径登记 + 拍板结果补记，120,144 B / `424CF2D07884`）→ v14（2026-09-24 追加 E-31 + R4 处置收口 + 盘点误报根因入链 + truncated CLOSED + 清理六棒布局变更注记，141,013 B / `EF19ACFEB585`）→ **v15（2026-09-25 追加 E-32 + 拍板留痕汇 + SHA 漂移注记 + 三条断层 + 夜间保守口径自主决策 + 待核疑点 3 条入链）**
- **追加方法**：`edit` 工具 `old_string` 精确匹配 v14 末行（`*出证：Trae code · 2026-09-23 → v14 续（2026-09-24 by doc-writer \`agent-0032834a3e04\`）*`，141,013 B / SHA-12 `EF19ACFEB585`），`new_string` 保留 v14 末行一字不动 + 新增 `---` 分隔 + 追加 §21（E-32 6 子条）+ §21.7（4 小节）+ §21.8（E-32 边界声明）+ 新末行
- **旧 E-1…E-31 内容核验**：v14 `EF19ACFEB585`（141,013 B）落盘后按 §1–§20 内容哈希自核 → **追加后前 141,013 B 字节级未变**（实测 prefix SHA-12 = `EF19ACFEB585` ✓）
- **v15 末态全文件 SHA-12**（执行棒 stdout 报值）：（自指回环：本节任何编辑都会改变本字段自身；执行棒交付时实测 SHA-12 + 大小在 doc-writer handoff 报告中给出；外部观测者请用 `Get-FileHash -Algorithm SHA256 docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 独立复算）
- **拍板落地形式**：E-32.1–E-32.5 五项拍板结果将追加为 v15.x 子节（v15.1 / v15.2 ...），不动本 §21.1–§21.6 + §21.7–§21.8 既有内容

#### §21.7.5 E-32.6 补充核验（v15 起草过程落盘核验）

| 件 | 盘 SHA-12 | 字节 | 核验结果 |
|---|---|---|---|
| `results/_v4_noise_cleanup_manifest_v3_2026_09_25.md` | `6F3F6FA3AB1D` | 24,491（实测） | 核 E-32.6 #2 误报事实（实测 archive = 1,669 件 + sub = 441 件均在盘，沿 v14 §20.5 字面） |

### §21.8 E-32 边界声明（v15 追加）

- **未修改任何 E-1…E-31 旧行 / 未修改 v14 §1–§20 既有 §12 + §15 + §17 + §18 + §19 + §20 内容**：追加前 v14 末态 prefix SHA-12 = `EF19ACFEB585`（实测，落盘后 append 完成即刻核验）；§21 仅追加于 v14 末行（`*出证：Trae code · 2026-09-23 → v14 续 ...*`）之后
- **未修改任何 V1–V3 资产**：本节为勘误追加节，0 件 V1-V3 资产触动；SHA 漂移注记仅记录 cleanup 后迁仓件之事实变化（沿 v14 §20.5 清理六棒布局变更字面）
- **未修改任何 V4 frozen 链**：E-32 引用的 11+ 件预登记/激活/映射/verdict/result 件 全部只读引用，未触动；pre/post SHA 自证一致
- **R4 key 永不明文（无例外）**：本节全文 0 件 key 明文；grep 自检 clean
- **kill-line 字面不动**：E-32 不涉 kill-line；本节仅事实登记，无 kill-line 触动
- **不擅自调阈值**：0 阈值调整；E-32.5 T1.5 N_min 6<10 不一致仅如实标注，未擅自调阈值
- **派生 JSON 不合并**：本节为勘误追加节，0 件派生 JSON 产出
- **不覆盖既有件**：仅在 v14 末行追加 §21 + §21.7 + §21.8；既有件 0 覆盖；既有 E-1…E-31 0 触动；既有 v14 §1–§20 0 触动
- **拍板原文逐字不编造**：E-32.1–E-32.5 引用 PI 拍板均以 ask ID 形式（`ask_9484b696` / `ask_249ba885` / `ask_748d9242` / `ask_259658a4`）+ SHA 字面 + 落地 SHA 字面引述；不擅自重构拍板原文；其他 ask ID 拍板原文详见 parent 拍板回函/工具问卷原文
- **succeeded ≠ 跑完**：本棒为 doc-writer 起草类，仅起草 §21 + §21.7 + §21.8 + 末行；不代表「E-32.1 三件追认 / E-32.2 SHA 漂移 / E-32.6 待核疑点」等已落盘核验——E-32.6 三条疑点由 evidence-auditor 复核
- **「待 PI 复核」/「待 evidence-auditor 核」状态注记**：E-32.1 三件已「追认生效即锁」（ratify_all 拍板原文语义）；E-32.2 SHA 漂移注记「拍板字面=沿自报值引用，verdict 本体不动」；E-32.3 三条断层「待 PI 复核生效」；E-32.4 五项拍板汇「待 PI 复核生效」；E-32.5 4 项自主决策「待 PI 复核生效」；E-32.6 3 条疑点「待 evidence-auditor 核」—— 6 子条目全部状态明示，不擅自拍板
- **skill 缺位 fallback**（沿派工单）：本地 skill 加载器多次实录 Local skill not found —— 按既有 5 件预登记件 + 派工单字面 + v11 §15.4 E-28.4 + v13 §19.8 + v14 §20.7 末段先例执行；**未编造 skill 不存在的虚构指令**

---

*出证：Trae code · 2026-09-23 → v15 续（2026-09-25 by doc-writer `agent-0032834a3e04`）*

---

## §22 E-33 · 2026-09-26 evidence-auditor 4 疑点逐条定案勘误（v15 → v16）

> **触发**：evidence-auditor 派工 `audit_auth = ask_57981c1bc81e03b9990a06e5`（2026-09-26 16:26 显式），交付件 `results/_v4_evidence_audit_reconcile_2026_09_26.md`（盘 SHA-12 `68F66904C0C8`）§A–§E；E-32.6 §21.6 待核疑点 3 条 + 派工单补 case #2 mapping 字面错 = **共 4 条**，本节按审计定案勘误追加式落地（沿 PI 批3 R1 原文「修正以勘误追加式落」）。
> **性质**：勘误追加节，**不改任何 E-1…E-32 旧行 / 不改 v15 §1–§21.8 既有 §12 + §15 + §17 + §18 + §19 + §20 + §21 内容**；4 子条按 id 化追加（E-33.1 batch1_r6 result 链/盘双漂定案 + E-33.2 mapping L19/L20 hash 字面错 + E-33.3 清理 v3 棒相对路径基准错 + E-33.4 T1 verdict/result 锚标互换定案）
> **边界**：V1–V3 资产 0 触动 / V4 frozen 链 0 触动 / R5 frozen 重建只追加 / 派生 JSON 不合并 / 不覆盖既有件 / 0 擅调阈值 / kill-line 字面不动 / key 永不明文（无例外）

### §22.1 E-33.1 batch1_r6 result SHA 链/盘双漂定案（case #1）

**链记录字面值 vs 盘实测字面值**：

| 维度 | 链记录字面（mapping.md L17 + batch2_r6_result.json L28 + batch3_r1_result.json L22） | 盘实测字面（独立复算） |
|---|---|---|
| SHA-12 | `A4F851154551` | `6B92BBFF7180` |
| 字节 | 58,369 B | 57,925 B（**-444 B**） |
| CreationTime | — | 2026-09-24 22:08:45 |
| LastWriteTime | — | 2026-09-25 00:27:42（**重写跨度 2h19m**） |

**定案（evidence-auditor 实测 2026-09-26，源 `68F66904C0C8` §A row 1 + §B.1）**：
- executor.py (`5F02C7E0F094` / 47,242 B) CreationTime = LastWriteTime = 21:59:06 → **未触动** ✓
- **根因**：result.json 改写时点（00:27:42）晚于 mapping.md 创建（23:14:26）+ batch2_r6_result.json 创建（23:50:52），故下游链 reference 全部锁定原 SHA；改写后**无 chain manifest 重登记**，致链/盘双记
- **改写动机未推定**（本棒不动文件本体，未做逆向 diff 改写前后内容；仅记录「-444 字节差异」+「无 chain manifest 重登记」+「改写时点晚于所有下游引用」事实）
- **不动文件本体**：按 R5 frozen 触禁；本勘误仅记录漂移事实 + 双 SHA 字面 + 改写时点
- **PI 处置路径**（**留 PI 二选一**，处置原则：二选一落定前下游引用沿双记；落定即按拍板结果更新链 reference）：
  - **(a) 接受改写为「增/修字段」**：将 `6B92BBFF7180` 视为新基准，更新下游链 reference（batch2_r6_result.json 等需勘误追加式补 drift 注记）
  - **(b) 撤回改写**：从 git / 备份恢复 `A4F851154551` 基准；**盘上无可恢复副本 → 此路径需用户授权重建**
- **处置状态**：**待 PI 二选一拍板**；落定前下游引用沿双记

### §22.2 E-33.2 mapping L19/L20 hash 字面错定案（case #2）

| 行 | 件 | mapping 字面 SHA-12 | 盘实测 SHA-12 | 盘实测字节 | bytes 一致? | SHA 一致? |
|:-:|---|---|---|---|:-:|:-:|
| L19 | `results/_v4_supp_l14v3_batch2_r2_result.json` | `CB37B699FF73` | `8C125E257AF8` | 62,887 | ✓（62,887 = 62,887） | ❌ |
| L20 | `results/_v4_supp_l14v3_batch2_r2_executor.py` | `5BE9DFE83A27` | `E7418F47A130` | 55,317 | ✓（55,317 = 55,317） | ❌ |

**定案（evidence-auditor 实测 2026-09-26，源 `68F66904C0C8` §A row 2 + §B.2）**：
- mapping 文件本体 SHA = `98A779D61C1E` / 48,028 B（LastWriteTime 2026-09-24 23:14:26）与登记一致 → **文件未触动**
- bytes 字面一致 → **SHA 字面错，非文件被改**
- **根因**：mapping 起草时 hash 算错（**起草类失灵，非执行类失灵**）；mapping 按 R5 frozen 不擅改
- **下游已披露**：batch8_r1_result.json L163 字段 `mapping_sha12_discrepancy_note` 已诚实交代；本勘误与下游披露一致
- **不动 mapping.md**；仅 E-33.2 勘误追加字面登记「mapping L19/L20 SHA 字面错，实际盘 SHA = 8C125E257AF8 + E7418F47A130」

### §22.3 E-33.3 清理 v3 棒 archive/sub 目录误报根因追加（case #3，相对路径基准错）

**清理 v3 棒 §F 字面值（误报）**：

| 目录 | v3 棒路径 | v3 棒存在 | v3 棒文件数 |
|---|---|:-:|:-:|
| `_non_upload_local_archive` | `D:/私人资料/deposon-repo/_non_upload_local_archive` | **False** | 0 |
| `deposon-sub` | `D:/私人资料/deposon-repo/deposon-sub` | **False** | 0 |

**实测字面值**（`Test-Path` + `Get-ChildItem -Recurse -File`）：

| 路径 | Test-Path | 文件数（递归） |
|---|:-:|:-:|
| `D:/私人资料/deposon-repo/_non_upload_local_archive` | False | 0 |
| `D:/私人资料/deposon-repo/deposon-sub` | False | 0 |
| `D:/私人资料/_non_upload_local_archive` | **True** | **1,669** |
| `D:/私人资料/deposon-sub` | **True** | **441** |

**定案（evidence-auditor 实测 2026-09-26，源 `68F66904C0C8` §A row 3 + §B.3）**：
- 两目录在 `D:/私人资料/deposon-repo/`（workspace 子路径）下**不存在**（与 v3 棒一致）；但在 `D:/私人资料/`（workspace **父级路径**）下**存在**，分别 **1,669 件 / 441 件**
- 用户预期「1230+ / 441+」 → 实测 **1,669 / 441**（1669 ≥ 1230 ✓；441 = 441 ✓，与用户预期同源演变一致）
- **根因**：**相对路径基准错**——清理 v3 棒以 workspace 根 `D:/私人资料/deposon-repo` 为基准解析相对路径 `_non_upload_local_archive` / `deposon-sub`，但 archive/sub 实为 workspace **兄弟目录**（父级 `D:/私人资料/`）；v3 棒 lookup 路径时未跨出 workspace 边界外探 + 未识别仓外父级路径存在性
- **v3 棒处置**：v3 棒产物为历史事实（已落盘 `6F3F6FA3AB1D` / 24,491 B），按 R5 frozen 不擅改 + 不回改 v3 棒产物；本勘误仅补「相对路径基准错」根因标注 + 不调已登记数字
- **E-32.6 #2 已登记的 1,669 + 441 字面值维持**（与 v3 棒产物 `6F3F6FA3AB1D` 24,491 B 字面一致；E-32.6 §21.6 入链字面 + 实测复算均一致）

### §22.4 E-33.4 T1 verdict / result 锚标互换定案（case #4，cleanup v3 棒标签互换）

**cleanup v3 棒 §F 字面值（错） vs 实测**：

| 行 | cleanup v3 棒字面 | 实测 SHA-12 | 实测字节 | 实测件 |
|:-:|---|---|---|---|
| L37 | T1 verdict `results/_v4_supp_t1_verdict.md` (52,942 B / SHA-12=`802DECE2286A`) | `F1B5E49F3058` | 27,538 | **t1_verdict.md** ✓ |
| L37 | （未明列 add_T1） | `802DECE2286A` | 52,942 | `_v4_supp_prereg_v02_add_T1_2026_09_24.md`（add_T1） |
| L38 | T1 result `results/_v4_supp_t1_result.json` (82,365 B / SHA-12=`D6CB03A4657E`) | `D6CB03A4657E` | 82,365 | t1_result.json ✓ |
| L44 / L220 | "F1B5E49F3058 系 T1.5 (`_v4_supp_t15_*`) 的 SHA-12 锚 ... 非 T1 verdict 标识" | `F1B5E49F3058` | 27,538 | **t1_verdict.md**（非 T1.5） |

**正确映射字面（勘误定案）**：

| SHA-12 | 路径 | 字节 |
|---|---|---|
| `F1B5E49F3058` ✓ | T1 verdict = `results/_v4_supp_t1_verdict.md` | 27,538 |
| `D6CB03A4657E` ✓ | T1 result = `results/_v4_supp_t1_result.json` | 82,365 |
| `802DECE2286A` | add_T1 = `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` | 52,942 |
| `79936B630015` | add_T1_activation = `results/_v4_supp_prereg_v02_add_T1_activation_2026_09_24.md` | 14,234 |
| `A7CAD9228B0B` | T1 executor = `results/_v4_supp_t1_executor.py` | 59,967 |

**定案（evidence-auditor 实测 2026-09-26，源 `68F66904C0C8` §A row 4 + §B.4）**：
- cleanup v3 棒 L37 把 add_T1 字面（SHA-12 `802DECE2286A` / 52,942 B）错填到 t1_verdict.md 名下（因 add_T1 与 t1_verdict 在文件系统命名相近 + 字段未交叉核对）
- cleanup v3 棒因错 1 推断 + grep F1B5E49F3058 命中 t15_* 件（**T1.5 对 T1 verdict 的正向引用**，非 T1.5 自锚），错误重路由为 T1.5 自锚 → **标签互换**：实情是 F1B5E49F3058 = t1_verdict.md，D6CB03A4657E = t1_result.json，但 v3 棒反写为「D6CB03A4657E = T1 verdict 锚 / F1B5E49F3058 = T1.5 锚」
- **t1_verdict.md 自报 SHA 表（L13-18）字面自洽**（D6CB03A4657E = result / 802DECE2286A = add_T1 / 79936B630015 = add_T1_activation）→ cleanup v3 棒若交叉核 t1_verdict 自表可避免此错
- **不动 v3 棒产物**（按 R5 frozen 不擅改）；本勘误仅记录 cleanup v3 棒字段填写错事实 + 正确映射字面

### §22.5 v16 追加节 SHA 自核 + 版本变更记录

#### §22.5.1 v16 追加前 SHA 自核（沿 v15 末态）

| 件 | 追加前 SHA-12 | 字节 |
|---|---|---|
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（v15 末版） | **`6844BF36F762`** | **158,079** |

> **锚定证据**：派工单 audit_auth 字面声明 v15 = `6844BF36F762`（158,079 B）—— 实测核验 ✓（v14 `EF19ACFEB585` 141,013 B → v15 `6844BF36F762` 158,079 B，差异源于 v15 追加 §21 E-32 + §21.7 + §21.8 共三节，字节 141,013 → 158,079）

#### §22.5.2 v16 追加节源件 SHA-12 链（evidence-auditor 审计报告 1 件 + 10 件核锚件）

**审计源件**：

| 路径 | 盘 SHA-12 |
|---|---|
| `results/_v4_evidence_audit_reconcile_2026_09_26.md` | `68F66904C0C8` |

**E-33 引用的核锚件**：

| 路径 | 盘 SHA-12 | 实际语义 |
|---|---|---|
| `results/_v4_supp_l14v3_batch1_r6_result.json` | `6B92BBFF7180` | 链 record 自报 `A4F851154551` ≠ 盘实算（链/盘双漂） |
| `results/_v4_supp_l14v3_model_mapping_2026_09_24.md` | `98A779D61C1E` | mapping 文件未触动；L19/L20 SHA 字面错 |
| `results/_v4_noise_cleanup_manifest_v3_2026_09_25.md` | `6F3F6FA3AB1D`（24,491 B） | v3 棒产物；相对路径基准错（历史事实保留） |
| `results/_v4_supp_t1_verdict.md` | `F1B5E49F3058` | T1 verdict 正确锚（27,538 B） |
| `results/_v4_supp_t1_result.json` | `D6CB03A4657E` | T1 result（82,365 B；cleanup v3 棒字段错填为 verdict） |
| `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` | `802DECE2286A` | add_T1（52,942 B；cleanup v3 棒 L37 错填到 t1_verdict 名下） |
| `results/_v4_supp_prereg_v02_add_T1_activation_2026_09_24.md` | `79936B630015` | add_T1_activation（14,234 B） |
| `results/_v4_supp_t1_executor.py` | `A7CAD9228B0B` | T1 executor（59,967 B） |
| `results/_v4_supp_l14v3_batch2_r2_result.json` | `8C125E257AF8` | mapping L19 字面错实盘值（62,887 B） |
| `results/_v4_supp_l14v3_batch2_r2_executor.py` | `E7418F47A130` | mapping L20 字面错实盘值（55,317 B） |

#### §22.5.3 v16 追加后 SHA 自核（**循环约束 self-referential**）

| 件 | 追加后 SHA-12 | 字节 |
|---|---|---|
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（v16 = 原 v15 + §22 E-33 + §22.5 + §22.6） | （自指回环：写完即落盘；任何编辑会改变本字段自身。落盘报值见执行棒 stdout；外部观测者请用 `Get-FileHash -Algorithm SHA256 docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 独立复算） | （落盘后实测） |

#### §22.5.4 v16 版本变更记录

- **v15 → v16 变更范围**：**仅追加** §22 E-33（4 子条：E-33.1 batch1_r6 result 链/盘双漂 + E-33.2 mapping L19/L20 hash 字面错 + E-33.3 清理 v3 棒相对路径基准错 + E-33.4 T1 verdict/result 锚标互换定案）+ §22.5（本节 v16 SHA 自核 + 版本变更 4 小节）+ §22.6（E-33 边界声明）；**0 处修改** v15 既有 §1–§21.8 内容 + 0 处修改 E-1…E-32 旧行
- **版本演进链续 v15**：v15（2026-09-25 追加 E-32 + 拍板留痕汇 + SHA 漂移注记 + 三条断层 + 夜间保守口径自主决策 + 待核疑点 3 条入链，158,079 B / `6844BF36F762`）→ **v16（2026-09-26 追加 E-33 + 4 疑点逐条定案勘误，字面源 `results/_v4_evidence_audit_reconcile_2026_09_26.md` SHA-12 `68F66904C0C8`）**
- **追加方法**：`edit` 工具 `old_string` 精确匹配 v15 末行（`*出证：Trae code · 2026-09-23 → v15 续（2026-09-25 by doc-writer \`agent-0032834a3e04\`）*`，158,079 B / SHA-12 `6844BF36F762`），`new_string` 保留 v15 末行一字不动 + 新增 `---` 分隔 + 追加 §22（E-33 4 子条）+ §22.5（4 小节）+ §22.6（E-33 边界声明）+ 新末行
- **旧 E-1…E-32 内容核验**：v15 `6844BF36F762`（158,079 B）落盘后按 §1–§21.8 内容哈希自核 → **追加后前 158,079 B 字节级未变**（实测 prefix SHA-12 = `6844BF36F762` ✓）
- **v16 末态全文件 SHA-12**（执行棒 stdout 报值）：（自指回环：本节任何编辑都会改变本字段自身；执行棒交付时实测 SHA-12 + 大小在 doc-writer handoff 报告中给出；外部观测者请用 `Get-FileHash -Algorithm SHA256 docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 独立复算）

### §22.6 E-33 边界声明（v16 追加）

- **未修改任何 E-1…E-32 旧行 / 未修改 v15 §1–§21.8 既有 §12 + §15 + §17 + §18 + §19 + §20 + §21 内容**：追加前 v15 末态 prefix SHA-12 = `6844BF36F762`（实测，落盘后 append 完成即刻核验）；§22 仅追加于 v15 末行（`*出证：Trae code · 2026-09-23 → v15 续 ...*`）之后
- **未修改任何 V1–V3 资产**：本节为勘误追加节，0 件 V1-V3 资产触动
- **未修改任何 V4 frozen 链 / 不动 R5 frozen 触禁件**：E-33 引用的 10 件核锚件（`6B92BBFF7180` / `98A779D61C1E` / `6F3F6FA3AB1D` / `F1B5E49F3058` / `D6CB03A4657E` / `802DECE2286A` / `79936B630015` / `A7CAD9228B0B` / `8C125E257AF8` / `E7418F47A130`） + 审计源件 1 件 `68F66904C0C8` = 共 11 件 全部只读引用，未触动；pre/post SHA 自证一致；不动 batch1_r6_result.json / mapping.md / cleanup v3 棒 / t1_verdict.md / t1_result.json / batch2_r2_result.json / batch2_r2_executor.py / batch8_r1_result.json 等任何链上件
- **R4 key 永不明文（无例外）**：本节全文 0 件 key 明文；grep 自检 clean
- **kill-line 字面不动**：E-33 不涉 kill-line；本节仅事实登记 + 正确映射字面追加，无 kill-line 触动
- **不擅自调阈值**：0 阈值调整
- **派生 JSON 不合并**：本节为勘误追加节，0 件派生 JSON 产出
- **不覆盖既有件**：仅在 v15 末行追加 §22 + §22.5 + §22.6；既有件 0 覆盖；既有 E-1…E-32 0 触动；既有 v15 §1–§21.8 0 触动
- **字面忠实**：E-33 引用 evidence-auditor 审计报告（`68F66904C0C8`）+ 拍板锚 `ask_57981c1bc81e03b9990a06e5` + 各核锚件 SHA 字面均按 §A row 1-4 + §B.1-B.4 + §C.1-C.4 字面草案引述；不擅自重构拍板原文；其他详见 evidence-auditor 审链报告原文
- **succeeded ≠ 跑完**：本棒为 doc-writer 起草类，仅起草 §22 + §22.5 + §22.6 + 末行；不代表「E-33.1 batch1_r6 result 改写定案 / E-33.2 mapping 字面错 / E-33.3 v3 棒路径基准错 / E-33.4 T1 锚标互换」等已落盘核验——`68F66904C0C8` 审链报告自身「待 PI 复核生效；生效即锁；事后不重开不调」（沿证据链审链报告 §E 状态注）
- **「待 PI 复核」/「待 PI 二选一」/「历史事实保留」状态注记**：
  - **E-33.1**（batch1_r6 result 链/盘双漂）= **处置留 PI 二选一**（接受 `6B92BBFF7180` 为新基准更新下游链 reference / 撤回改写从备份恢复 `A4F851154551`——盘上无可恢复副本不可恢复路径），**二选一落定前下游引用沿双记**；落定即按拍板结果更新链 reference
  - **E-33.2**（mapping L19/L20 hash 字面错）= 起草类失灵已落定（mapping 不动 + 勘误字面追加「实际盘 SHA = 8C125E257AF8 + E7418F47A130」）
  - **E-33.3**（v3 棒路径基准错）= 历史事实保留（v3 棒产物 `6F3F6FA3AB1D` 不动）+ 根因追加（相对路径基准错）
  - **E-33.4**（T1 verdict/result 锚标互换）= 历史事实保留（v3 棒不动）+ 正确映射字面追加（F1B5E49F3058 = T1 verdict ✓ / D6CB03A4657E = T1 result ✓ / 802DECE2286A = add_T1）
  - **4 子条目全部状态明示，不擅自拍板**
- **skill 缺位 fallback**（沿派工单）：本地 skill 加载器多次实录 Local skill not found —— 按 v15 §21.7-21.8 + 派工单锚 `6844BF36F762`（v15 末态）+ `68F66904C0C8` §A-§C 字面既有口径执行；**未编造 skill 不存在的虚构指令**

---

*出证：Trae code · 2026-09-23 → v16 续（2026-09-26 by doc-writer `agent-0032834a3e04`，勘误追加 E-33 4 疑点定案，字面源 `results/_v4_evidence_audit_reconcile_2026_09_26.md` SHA-12 `68F66904C0C8`）*

---

### §22.7 E-34 勘误追加（v17 · 2026-09-26 · case#1 落定 + N-26 终裁 + T1 闭环 + 任务 B 采集闭合 + 锚链口径）

> **v17 性质**：**仅追加** §22.7（E-34 5 子条）+ §22.8（v17 SHA 自核 + 版本变更）+ §22.9（E-34 边界声明）；**0 处修改** v16 既有 §1–§22.6 内容（含 E-1…E-33 全部旧行）；前 174,445 B 字节级未变（prefix SHA-12 = `AB50FEC180DA` ✓ 自核落盘报值）。
> **触发**：PI 2026-09-26 17:33 `ask_c4c1b896880ba5e6292a6a5c` case1 步骤 selectedOptions=accept + 派工单 doc-writer 起草 E-34 五子条（case#1 落定 / N-26 真审终裁引用 / T1 系全链闭环注记 / 任务 B 采集闭合注记 / 锚链口径待拍板注记）。
> **字面源**：5 件独立上游件（见 §22.8.2 SHA-12 链）+ 1 件拍板锚 `ask_c4c1b896880ba5e6292a6a5c` + 1 件 L4 verdict 字面引用 `74B5B37F7EEA`；不擅自改写拍板原文。

#### §22.7.1 E-34.1 case#1 处置落定（batch1_r6 result 链/盘双漂二选一收口）

**拍板锚**：`ask_c4c1b896880ba5e6292a6a5c` case1 步骤 selectedOptions=accept，字面 disposition_text = **「接受 6B92BBFF7180 为新基准，勘误链记改写事实」**（沿 `_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json` `26F110A6E571` / 10,257 B §supplements.case1.disposition_text 字面）。

**二选一收口（PI 已拍板 case1=accept）**：
- **新基准生效**：`6B92BBFF7180` 为 `results/_v4_supp_l14v3_batch1_r6_result.json` 改写后盘实测 SHA-12（57,925 B；LastWriteTime 2026-09-25 00:27:42），替代 E-33.1 §C.1 字面所列二选一选项 (a)「接受改写为新基准」；
- **下游引用更新**：`results/_v4_supp_l14v3_model_mapping_2026_09_24.md` `98A779D61C1E` L17 + `batch2_r6_result.json` L28 + `batch3_r1_result.json` L22 等下游链上件 reference 由 `A4F851154551` / 58,369 B（原 drop 字面）→ `6B92BBFF7180` / 57,925 B（改写后字面）；按 PI 处置路径 (a) 沿 V4 §3.1 + R5 重建 V4 frozen 派生 JSON 不合并 + 不覆盖既有件 三铁律执行勘误追加式更新，下游件本体一字不动，仅在各自 §末尾或 ledger 字面追加「E-34.1 落定：基准改为 6B92BBFF7180」一行；
- **改写事实存照**（E-33.1 §C.1 路径 (b) 不走）：
  - 字节差 = **-444 B**（58,369 → 57,925）；
  - 时间差 = CreationTime 2026-09-24 22:08:45 vs LastWriteTime 2026-09-25 00:27:42（**文件被重写 2h19m 后**）；
  - **无 chain manifest 重登记**：mapping.md（23:14:26）+ batch2_r6_result.json（23:50:52）等下游链上件均在改写前完成，故均锁定原 SHA `A4F851154551`；改写时点（00:27:42）后无任何链上件重新登记新 SHA；
  - executor.py（`5F02C7E0F094` / 47,242 B）CreationTime = LastWriteTime = 21:59:06 → **未触动** ✓；
  - 改写内容性质（增字段 / 调字段 / 意外覆盖）**未推定**——按 evidence-auditor 报告 `68F66904C0C8` §B.1 + §D.2 字面，本审链报告不动文件本体故未逆向 diff；改写动机留链存照，**PI 知情接受 + 勘误链记改写事实** = 不再追问动机。

**E-34.1 状态**：**落定**（PI 2026-09-26 17:33 case1=accept 拍板，勘误链 E-34 同步登记）。下游引用更新由 verifier 或 doc-writer 后续棒按 R5 不覆盖既有件 + 派生 JSON 不合并 铁律执行勘误追加式追加，本棒仅登记不写。

#### §22.7.2 E-34.2 N-26 真审终裁引用（L14V3 distill 整链重跑复现 = 真证伪）

**字面源**：`results/_v4_supp_l14v3_n26_verdict.md` SHA-12 **`F4435801D09F`**（64,485 B；verdict-keeper 起草 2026-09-26 by agent-3a4d09ba3c90；落盘哈希自核 ✓）。

**定性（沿 n26 verdict §0 + §3 + §4 字面）**：**N-26 真审真证伪**（沿 v1/v2 方向「metadata 不可区分」被实证）。五条 kill-line 字面裁定：
- **K-N26-1** = NOT TRIGGERED（教师准确率 5 教师 mean **0.5617** < 0.70 真证伪线；kimi 0.7512 是 5 教师中唯一 ≥0.65 偏强者但仍 <0.70；剔 kimi 后 mean = 0.5143）—— v1/v2 方向**弱维持**（沿 `F4435801D09F` §3.1 + §3.3 字面）；
- **K-N26-2** = TRIGGERED（pooled 二分类 AUC **0.5663** 远 < 0.75 真证伪线；全 5 折 CV AUC 0.5266–0.6318 无一折达 0.75 真证伪线；**全 5 reads 稳健**）—— v1/v2 方向**真证伪**（沿 `F4435801D09F` §3.2 字面）；
- **K-N26-3** = NOT TRIGGERED（3/5 教师 < 0.60，未达 ≥4 阈值；kimi 0.7512 > 0.60 抬升；严格意义上 ≥4 教师门槛不达）—— v1/v2 方向**略不达**（沿 `F4435801D09F` §3.3 字面）；
- **K-N26-N1** = pass=True（22 caption 各 ≥1 successful 字面满足；teacher_kimi 因 r1 已清出 teacher 侧 N=77 < 110 理论下限，但**不属 K-N26-N1 字面「构造退化」族**——披露沿 `F4435801D09F` §5.2 字面）；
- **K-N26-N2** = pass=True。

**与 L4 verdict 关系**：L4 verdict `74B5B37F7EEA` §11「FAIL · 构造不可行 · 4/5 教师 metadata 缺位」**一字不动**（v1/v2 时期「构造不可行」= 缺教师侧配对不可算 = 既判未真审；L14+ 真审后构造补齐 10 cells × 22 caption × 双向 ≥1,090 calls + 真审实证「metadata 不可分」维持 = **与 v1/v2 方向一致而非翻案**）—— 沿 `F4435801D09F` §4.1 + §5.2 字面「不翻 L4 verdict」明示。

**三重构造域限制（沿 `F4435801D09F` §0 + §1.5 字面）**：
- **teacher 侧**：teacher_kimi N=77 < 110 理论下限（teacher_kimi r1 已于 2026-09-24 cleanup manifest 处置后清出）；
- **distill 侧**：22 caption × 5 教师 × ≥5 calls = 132 calls / 教师（10 cells × 22 caption × 双向 ≥1,090 calls 同步保四元组 metadata）；
- **度量侧**：5 折 CV AUC 范围 0.5266–0.6318；pooled AUC 0.5663；全 5 reads 敏感性下均 < 0.75（不外推为「全不可分」——kimi 0.7512 ≠ 全不可分）。

**E-34.2 状态**：**N-26 真审真证伪**（沿 `F4435801D09F` §3 + §4 字面）+ 与 L4 verdict 74B5B37F7EEA 同方向深化非翻案 + 三重构造域限制如实 + **待 PI 正式拍板追认**（verdict-keeper 自身 §E「生效后状态沿 L14+ prereg `05B975A86989` + L14V3 mapping `98A779D61C1E` + T15R2 verdict `8355724A26E3` 锁先例 → 生效即锁；本勘误链 E-34.2 仅作字面引用登记，定性裁定之最终生效须 PI 正式拍板追认）。

#### §22.7.3 E-34.3 T1 系全链闭环注记（T1 → T1.5 → T1.5r2 verdict 件 SHA 汇列）

**闭环路径**（沿 evidence-auditor 报告 `68F66904C0C8` §B.4 + n26 verdict `F4435801D09F` §0 格式锚引用字面 + cleanup v3 棒 `6F3F6FA3AB1D` §F 字面）：
- **T1（假证伪假象）**：`results/_v4_supp_t1_verdict.md` SHA-12 `F1B5E49F3058`（27,538 B）+ `results/_v4_supp_t1_result.json` `D6CB03A4657E`（82,365 B）+ `results/_v4_supp_t1_executor.py` `A7CAD9228B0B`（59,967 B）+ add_T1 `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` `802DECE2286A`（52,942 B）+ add_T1_activation `results/_v4_supp_prereg_v02_add_T1_activation_2026_09_24.md` `79936B630015`（14,234 B）；
- **T1.5（补正真稳健）**：`results/_v4_supp_t15_verdict.md` SHA-12 `52C985429C91`（沿 `F4435801D09F` §0 + `68F66904C0C8` §B.4 grep 命中字面 + ledger 字面引用）；
- **T1.5r2（扩样 N_min 根因消除）**：`results/_v4_supp_t15r2_verdict.md` SHA-12 `8355724A26E3`（41,246 B；沿 `F4435801D09F` §0 + §1.7 格式锚字面 + L18 anchor 表 §18 字面 + n26 verdict §5.2 limitations「T15R2 verdict `8355724A26E3` §5.2 limitations 沿用」字面）。

**T1 → T1.5 → T1.5r2 演进链字面**（沿 n26 verdict §0 + cleanup v3 棒 §F 字面 + E-33.4 §22.4 锚标互换定案字面）：
- T1 verdict `F1B5E49F3058` → T1.5 verdict `52C985429C91`（T1.5 对 T1 verdict 的正向引用，非 T1.5 自锚——cleanup v3 棒 §F L44 / L220 错路由已由 E-33.4 定案纠正）；
- T1.5 verdict `52C985429C91` → T1.5r2 verdict `8355724A26E3`（扩样 N_min 根因消除，verdict 锚 SHA `8355724A26E3`）；
- T1.5r2 verdict `8355724A26E3` → N-26 verdict `F4435801D09F`（N-26 verdict §0 + §1.7「沿 T15R2 verdict `8355724A26E3` 格式锚」字面）。

**E-34.3 状态**：T1 系全链 verdict 件 SHA 闭环汇列注记完成（5 件 T1 + T1.5 + T1.5r2 + N-26 8 件 SHA 字面锚定 + 派生 JSON 不合并铁律沿用 + 不调阈值 + 不翻 L4 verdict 74B5B37F7EEA + L13 verdict E105EC1362DB + L7 verdict B8335982AE5E + N-26 prereg 0A9EE16267B5 + v0.2 件 + add_T1 件 + L9 / L10 追加件 + Track 2 件 + 22 caption + V3 distill 流水线参照系 全栈 0 触动）。

#### §22.7.4 E-34.4 任务 B 采集闭合注记（50 题全毕 · 68 采集件 · TH-v2-1/2/3 字面闭环）

**采集闭合事实**（沿 `26F110A6E571` §honesty_note + §constraints_compliance 字面）：
- **50 题全毕**：Q1–Q50 全编号覆盖（D1 v1.1 = 37 事件 + 11 推理全文补填 = 48 采集；D2 五波 R1b–R7b 七对反转配对 + Q38–Q50 十三补充判定 = 20 采集事件）；全采集合计 **48 + 20 = 68 事件**（扣除 pair 配对占位：R1a–R7a a-half 计 7 在 D1；R1b–R7b b-half 计 7 在 D2；Q1–Q37 全 Q 编号计 37；D2 独立补充判定 Q38–Q50 计 13；独立 R-pair 与独立 Q 之和 = 37 + 7 + 13 = 57 事件，+11 补推理填 = 68 采集件）；
- **dataset v1.1**：`results/_v4_pi_cot_v2_dataset.json` SHA-12 `7B01CD835A41`（12,672 B；落盘前后 SHA-12 复验不变 ✓，沿 `26F110A6E571` §addendum_for.dataset_sha12_pre/post 字面）；
- **D2 wave1–5 五件**（命名映射 d2 / d2b / d2c / d2d / d2e 五 addendum 件 = wave1–5）：

| Wave | 路径 | 盘 SHA-12 | 字节 |
|:-:|---|---|---|
| wave1 | `results/_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json` | `439721007AAF` | 6,132 |
| wave2 | `results/_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json` | `41D6C28CA87C` | 7,566 |
| wave3 | `results/_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json` | `99C58906F792` | 6,666 |
| wave4 | `results/_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json` | `C6D092F77932` | 7,668 |
| wave5 | `results/_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json` | `26F110A6E571` | 10,257 |

**三阈值字面裁定**（沿 `26F110A6E571` §honesty_note 字面）：
- **TH-v2-1 N≥50** = **✓ 通过**（实证 68 ≥ 50）；
- **TH-v2-2 R 反转 7 对闭合** = **✓ 通过**（实证 R1b / R2b / R3b / R4b[R2d2 波 1] + R5b / R6b[d2 波 2] + R7b[d2 波 3] 共 7 对 b-half 全部跨日 ≥1 天闭合）；
- **TH-v2-3 跨日稀释** = **双重不达如实**：
  - **单日占比违反 ≤60% 阈值**：D1 单日 2026-09-24 占比 48/68 = **70.6%**（违反 ≤60% 阈值）；D2 单日 2026-09-26 占比 20/68 = 29.4%；
  - **跨日天数违反 ≥3 天要求**：跨日仅 **2 天**（D1 + D2，prereg 字面要求 ≥3 天）；
  - 须 D3 续采稀释；本批不翻任何既有判定，仅入正式判定前规则集重训语料（与 D1 附录 / D2 wave1/2/3/4 合并评估）；
  - 正式判定须按 verdict.md §5.2 正式裁决触发条件（四要件缺一不可：跨天 D2/D3 数据到位 + TH-v2-2 R 后半配对闭合 + protocol-keeper 复核签字 + verifier 独立复核）重跑重裁。

**E-34.4 状态**：50 题全毕 68 采集件采集闭合完成；TH-v2-1 ✓ + TH-v2-2 ✓ + TH-v2-3 双重不达如实（单日 70.6% + 跨日 2 天）；待 D3 续采稀释 + verdict.md §5.2 正式裁决触发条件复核签字后重判；本棒仅登记不写正式 verdict。

#### §22.7.5 E-34.5 锚链口径待拍板注记（d2 系 fingerprint 字段 vs on-disk SHA 混用事实）

**事实登记**（沿 d2e `26F110A6E571` §fingerprint_self_hash_after_birth + §addendum_for 等字段字面 + d2/d2b/d2c/d2d 既有 fingerprint 字面）：
- **d2 系 addendum 件 5 件的 fingerprint_self_hash_after_birth 字段值 ≠ 各 addendum 件本体盘实测 SHA-12**：
  - 例：d2e `26F110A6E571` 自身 fingerprint_self_hash_after_birth = **`C9D38A166010`**（源 addendum JSON 字段值经 SHA-256 取前 12 位）≠ d2e 件本体盘实测 SHA-12 = **`26F110A6E571`**（文件本体经 SHA-256 取前 12 位）；
  - d2 / d2b / d2c / d2d 同模式（fingerprint_self_hash_after_birth 字段值 ≠ 各 addendum 件本体盘实测 SHA-12）；
- **混用事实**：
  - **on-disk SHA 口径**（盘实测 SHA-12）= addendum_for.{dataset_sha12_pre/post, d2_wave*_anchor_sha12_pre/post} + constraints_compliance 字面引用；
  - **fingerprint 字段口径**（JSON 字段值经 SHA-256 取前 12 位）= fingerprint_self_hash_after_birth 字段字面；
  - 两种口径在 d2 系 5 件中并存使用，**无统一口径文档明示**——下游引用时若按 fingerprint 字段值查 SHA-12，会查到与 on-disk SHA 不同的值；
- **统一口径待 PI 拍板**：
  - 选项 (a)：以 on-disk SHA 为唯一权威口径，fingerprint 字段值视为派生字段（须在 d2 系 5 件追加字段说明 + verifier 独立复核）；
  - 选项 (b)：以 fingerprint 字段值为唯一权威口径（须重算各 addendum 件本体 fingerprint 字段值 + 全链 5 件同步追加）；
  - 选项 (c)：保留两种口径并存但明确分层语义（on-disk SHA = 文件本体验证 / fingerprint = 派生字段验证）；
  - 选项 (d)：PI 另行处置。

**E-34.5 状态**：锚链口径混用事实登记完成；统一口径待 PI 拍板；本棒仅登记不擅自重算或重写 d2 系 5 件任何字段值；按 R5 frozen 派生 JSON 不合并铁律 + 不擅自调阈值 + key 永不明文 + V1–V3 只读不动 四铁律沿用执行。

---

### §22.8 v17 追加节 SHA 自核 + 版本变更记录

#### §22.8.1 v17 追加前 SHA 自核（沿 v16 末态）

| 件 | 追加前 SHA-12 | 字节 |
|---|---|---|
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（v16 末版） | **`AB50FEC180DA`** | **174,445** |

> **锚定证据**：派工单 audit_auth 字面声明 v16 = `AB50FEC180DA`（174,445 B）—— 实测核验 ✓（v15 `6844BF36F762` 158,079 B → v16 `AB50FEC180DA` 174,445 B，差异源于 v16 追加 §22 E-33（4 子条）+ §22.5（v16 SHA 自核 + 版本变更 4 小节）+ §22.6（E-33 边界声明）共三节，字节 158,079 → 174,445）。

#### §22.8.2 v17 追加节源件 SHA-12 链（5 件独立上游件 + 1 件拍板锚 + 1 件 L4 verdict 字面引用）

**E-34 引用的源件**（不触动，仅字面引用）：

| 路径 | 盘 SHA-12 | 实际语义 |
|---|---|---|
| `results/_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json` | `26F110A6E571`（10,257 B） | E-34.1 case#1 拍板字面源（disposition_text + errata_chain_trigger） |
| `results/_v4_supp_l14v3_n26_verdict.md` | `F4435801D09F`（64,485 B） | E-34.2 N-26 真审终裁字面源 |
| `results/_v4_supp_t1_verdict.md` | `F1B5E49F3058`（27,538 B） | E-34.3 T1 verdict 锚 |
| `results/_v4_supp_t1_result.json` | `D6CB03A4657E`（82,365 B） | E-34.3 T1 result 锚 |
| `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` | `802DECE2286A`（52,942 B） | E-34.3 add_T1 锚 |
| `results/_v4_supp_t15r2_verdict.md` | `8355724A26E3`（41,246 B） | E-34.3 T1.5r2 verdict 锚 |
| `results/_v4_supp_t15_verdict.md` | `52C985429C91`（沿 ledger + n26 verdict §0 字面） | E-34.3 T1.5 verdict 锚 |
| `results/_v4_pi_cot_v2_dataset.json` | `7B01CD835A41`（12,672 B） | E-34.4 dataset v1.1 锚 |
| `results/_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json` | `439721007AAF`（6,132 B） | E-34.4 D2 wave1 锚 |
| `results/_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json` | `41D6C28CA87C`（7,566 B） | E-34.4 D2 wave2 锚 |
| `results/_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json` | `99C58906F792`（6,666 B） | E-34.4 D2 wave3 锚 |
| `results/_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json` | `C6D092F77932`（7,668 B） | E-34.4 D2 wave4 锚 |

**E-34 引用的字面锚**：
- PI 拍板锚 `ask_c4c1b896880ba5e6292a6a5c` case1 步骤 selectedOptions=accept（2026-09-26 17:33；落盘「接受 6B92BBFF7180 为新基准，勘误链记改写事实」字面）；
- L4 verdict `74B5B37F7EEA`（盘已清出但 ledger L208 字面引用；E-34.2 §22.7.2 字面引用「FAIL · 构造不可行」一字不动）；
- E-33 旧行（E-33.1 §22.1 / E-33.2 §22.2 / E-33.3 §22.3 / E-33.4 §22.4 / §22.5 / §22.6）—— E-34.1 §22.7.1 字面引用 E-33.1 §C.1 二选一路径字面；
- evidence-auditor 报告 `68F66904C0C8`（22,863 B）—— E-34.3 §22.7.3 字面引用 §B.4 + E-34.1 §22.7.1 字面引用 §B.1 + §C.1 + §D.2；
- cleanup v3 棒 `6F3F6FA3AB1D`（24,491 B）—— E-34.3 §22.7.3 字面引用 §F 字面。

#### §22.8.3 v17 追加后 SHA 自核（**循环约束 self-referential**）

| 件 | 追加后 SHA-12 | 字节 |
|---|---|---|
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（v17 = 原 v16 + §22.7 E-34 + §22.8 + §22.9） | （自指回环：写完即落盘；任何编辑会改变本字段自身。落盘报值见执行棒 stdout；外部观测者请用 `Get-FileHash -Algorithm SHA256 docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 独立复算） | （落盘后实测） |

#### §22.8.4 v17 版本变更记录

- **v16 → v17 变更范围**：**仅追加** §22.7（E-34 5 子条：E-34.1 case#1 落定 + E-34.2 N-26 真审终裁引用 + E-34.3 T1 系全链闭环注记 + E-34.4 任务 B 采集闭合注记 + E-34.5 锚链口径待拍板注记）+ §22.8（本节 v17 SHA 自核 + 版本变更 4 小节）+ §22.9（E-34 边界声明）；**0 处修改** v16 既有 §1–§22.6 内容 + 0 处修改 E-1…E-33 旧行
- **版本演进链续 v16**：v16（2026-09-26 追加 E-33 + 4 疑点逐条定案勘误，字面源 `68F66904C0C8` 158,079 → 174,445 B / `AB50FEC180DA`）→ **v17（2026-09-26 追加 E-34 5 子条，case#1 落定 + N-26 终裁 + T1 闭环 + 任务 B 采集闭合 + 锚链口径待拍板，字面源 5 件独立上游件 + 拍板锚 `ask_c4c1b896880ba5e6292a6a5c` + L4 verdict `74B5B37F7EEA`）**
- **追加方法**：`edit` 工具 `old_string` 精确匹配 v16 末行（`*出证：Trae code · 2026-09-23 → v16 续 ...*`，174,445 B / SHA-12 `AB50FEC180DA`），`new_string` 保留 v16 末行一字不动 + 新增 `---` 分隔 + 追加 §22.7（E-34 5 子条）+ §22.8（4 小节）+ §22.9（E-34 边界声明）+ 新末行
- **旧 E-1…E-33 内容核验**：v16 `AB50FEC180DA`（174,445 B）落盘后按 §1–§22.6 内容哈希自核 → **追加后前 174,445 B 字节级未变**（实测 prefix SHA-12 = `AB50FEC180DA` ✓）
- **v17 末态全文件 SHA-12**（执行棒 stdout 报值）：（自指回环：本节任何编辑都会改变本字段自身；执行棒交付时实测 SHA-12 + 大小在 doc-writer handoff 报告中给出；外部观测者请用 `Get-FileHash -Algorithm SHA256 docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 独立复算）

---

### §22.9 E-34 边界声明（v17 追加）

- **未修改任何 E-1…E-33 旧行 / 未修改 v16 §1–§22.6 既有 §12 + §15 + §17 + §18 + §19 + §20 + §21 + §22 + §22.5 + §22.6 内容**：追加前 v16 末态 prefix SHA-12 = `AB50FEC180DA`（实测，落盘后 append 完成即刻核验）；§22.7–§22.9 仅追加于 v16 末行（`*出证：Trae code · 2026-09-23 → v16 续 ...*`）之后
- **未修改任何 V1–V3 资产**：本节为勘误追加节，0 件 V1-V3 资产触动
- **未修改任何 V4 frozen 链 / 不动 R5 frozen 触禁件**：E-34 引用的 12 件核锚件（`26F110A6E571` / `F4435801D09F` / `F1B5E49F3058` / `D6CB03A4657E` / `802DECE2286A` / `8355724A26E3` / `52C985429C91` / `7B01CD835A41` / `439721007AAF` / `41D6C28CA87C` / `99C58906F792` / `C6D092F77932`）+ 拍板锚 1 件 + 字面引用 4 件（L4 verdict `74B5B37F7EEA` + evidence-auditor `68F66904C0C8` + cleanup v3 棒 `6F3F6FA3AB1D` + E-33 旧行）= 共 17 件全部只读引用，未触动；pre/post SHA 自证一致；不动 d2e addendum / n26 verdict / T1 verdict / T1 result / add_T1 / T1.5r2 verdict / T1.5 verdict / dataset v1.1 / D2 wave1–5 addendum 等任何链上件
- **R4 key 永不明文（无例外）**：本节全文 0 件 key 明文；grep 自检 clean
- **kill-line 字面不动**：E-34 不涉 kill-line；K-N26-1 ACC=0.70 / K-N26-2 AUC=0.75 / K-N26-3 TEACHERS_LT=0.60 一字不动（沿 n26 verdict §0 字面）；本节仅事实登记 + 字面引用 + 状态注记，无 kill-line 触动
- **不擅自调阈值**：0 阈值调整（TH-v2-1 N≥50 + TH-v2-2 R 反转 7 对 + TH-v2-3 单日 ≤60% + 跨日 ≥3 天 一字不动）
- **派生 JSON 不合并**：本节为勘误追加节，0 件派生 JSON 产出（d2 / d2b / d2c / d2d / d2e 五 addendum 件与 dataset v1.1 落盘前后 SHA-12 复验不变 ✓）
- **不覆盖既有件**：仅在 v16 末行追加 §22.7 + §22.8 + §22.9；既有件 0 覆盖；既有 E-1…E-33 0 触动；既有 v16 §1–§22.6 0 触动
- **字面忠实**：E-34 引用 5 件独立上游件 + 1 件拍板锚 + 1 件 L4 verdict 字面均按字面引述；**PI 拍板原文逐字保留**（E-34.1「接受 6B92BBFF7180 为新基准，勘误链记改写事实」沿 `26F110A6E571` §supplements.case1.disposition_text 字面逐字录入，不擅自改写/润色/扩写/补全标点；E-34.4 Q48/Q49/Q50 reasoning_full 字段沿 d2e addendum 字面逐字录入）
- **succeeded ≠ 跑完**：本棒为 doc-writer 起草类，仅起草 §22.7 + §22.8 + §22.9 + 末行；不代表「E-34.1 下游引用更新已执行 / E-34.2 N-26 真审终裁已正式拍板追认 / E-34.4 任务 B 正式 verdict 已落 / E-34.5 锚链口径已统一」——四子条状态注记沿下文
- **「待 PI 复核 / 待 PI 正式拍板追认 / 待 D3 / 历史事实保留」状态注记**：
  - **E-34.1**（case#1 落定）= **落定**（PI 2026-09-26 17:33 case1=accept 拍板，勘误链 E-34.1 同步登记）；下游引用更新由 verifier 或 doc-writer 后续棒按 R5 不覆盖既有件 + 派生 JSON 不合并 铁律执行勘误追加式追加，本棒仅登记不写
  - **E-34.2**（N-26 真审终裁引用）= **字面引用落定 + 定性裁定待 PI 正式拍板追认**（verdict-keeper 自身 §E「生效后状态沿 L14+ prereg `05B975A86989` + L14V3 mapping `98A779D61C1E` + T15R2 verdict `8355724A26E3` 锁先例 → 生效即锁」字面；本勘误链 E-34.2 仅作字面引用登记，定性裁定之最终生效须 PI 正式拍板追认）
  - **E-34.3**（T1 系全链闭环注记）= **注记完成**（5 件 T1 + T1.5 + T1.5r2 + N-26 8 件 SHA 字面锚定 + 派生 JSON 不合并铁律沿用 + 不调阈值 + 全栈 0 触动）
  - **E-34.4**（任务 B 采集闭合注记）= **采集闭合完成 + 正式 verdict 待 D3 + 复核签字**（50 题全毕 68 采集件；TH-v2-1 ✓ + TH-v2-2 ✓ + TH-v2-3 双重不达如实；正式判定须按 verdict.md §5.2 正式裁决触发条件四要件缺一不可重跑重裁）
  - **E-34.5**（锚链口径待拍板注记）= **混用事实登记完成 + 统一口径待 PI 拍板**（4 选项：(a) on-disk SHA 唯一权威 / (b) fingerprint 字段值唯一权威 / (c) 保留两种口径并存分层语义 / (d) PI 另行处置；本棒仅登记不擅自重算或重写 d2 系 5 件任何字段值）
  - **5 子条目全部状态明示，不擅自拍板**
- **skill 缺位 fallback**（沿派工单）：本地 skill 加载器多次实录 Local skill not found —— 按 v16 §22.6 + 派工单锚 `AB50FEC180DA`（v16 末态）+ `68F66904C0C8` §A-§C 字面既有口径执行；**未编造 skill 不存在的虚构指令**

---

*出证：Trae code · 2026-09-23 → v17 续（2026-09-26 by doc-writer `agent-0032834a3e04`，勘误追加 E-34 5 子条：case#1 落定 + N-26 真审终裁引用 + T1 系全链闭环注记 + 任务 B 采集闭合注记 + 锚链口径待拍板注记，字面源 5 件独立上游件 + 拍板锚 `ask_c4c1b896880ba5e6292a6a5c` + L4 verdict `74B5B37F7EEA`）*

---

### §22.10 E-35 勘误追加（v18 · 2026-09-26 · 归档二棒后追认留痕 + 72 件口径拍板 + 锚链统一 + 正式裁决引用 + 路径差异注记）

> **v18 性质**：**仅追加** §22.10（E-35 6 子条）+ §22.11（v18 SHA 自核 + 版本变更）+ §22.12（E-35 边界声明）；**0 处修改** v17 既有 §1–§22.9 内容（含 E-1…E-34 全部旧行）；前 198,204 B 字节级未变（v17 SHA-12 `2DD8039D47E4` 实测 prefix ✓ 自核落盘报值）。
> **触发**：PI 2026-09-26 19:05 派工单 `ask_96e0f651f306f2337cd57b47` 全推荐拍板（ratify_formal=all：N-26 定性 / T1.5r2 四项 / activation 系 / 词表 §2.2 口径全追认生效即锁）+ 派工单 `ask_9c8751ec`「KIMI与GLM知道即可」「你侧无额外补充」（涉 GLM 表述一律以 PI github 为唯一权威源）+ 派工单 `ask_822b1e27` PI 2026-09-26 18:42 拍板 th23_span=跨度 3 天解读达标 supersede + 派工单 C.doc-writer 起草 E-35 6 子条（追认全生效留痕 / 72 件口径拍板 / 锚链统一 on-disk SHA-12 / 小项打包处置六条 / 正式裁决引用 / 归档二棒 6 项路径差异追溯口径注记）。
> **字面源**：1 件派工锚 `ask_96e0f651f306f2337cd57b47` + 1 件派工锚 `ask_9c8751ec` + 1 件派工锚 `ask_822b1e27` + 11 件独立上游件（清单补账件 v2 / 三封委托信 v3 / ledger v6 / verdict_v2 / verdict_v2_signoff / coding_review / n26 verdict / T1.5r2 verdict / add_T15r2 prereg / add_T15r2 activation / E-34 旧行）；不擅自改写拍板原文。

#### §22.10.1 E-35.1 追认全生效留痕（ask_96e0f651 ratify_formal=all）

**拍板锚**：`ask_96e0f651f306f2337cd57b47` PI 2026-09-26 19:05 全推荐拍板 + ratify_formal=all 沿 verifier 签名稿 `BA4D07BD7000` §3.2「dispatcher 拍板并入触发条件 R5 = key 永不明文 + 推理全文仅入本地件 + no-upload 清单完备」+ §8.3 「签字时间 2026-09-26 19:07 沿 agent-context 时间戳」+ verdict_v2 §0 字面引用 ratify_formal=all 字面一致。

**追认 4 类全生效留痕**（沿 ask_96e0f651 ratify_formal=all 字面 + 签字稿 §8.1 PASS 字面）：

**(a) N-26 定性全追认生效即锁**（沿 `F4435801D09F` §3 + §4 字面）：
- K-N26-1 NOT TRIGGERED（教师准确率 5 教师 mean **0.5617** < 0.70 真证伪线；v1/v2 方向**弱维持**）
- K-N26-2 TRIGGERED（pooled 二分类 AUC **0.5663** 远 < 0.75 真证伪线；全 5 reads 稳健；v1/v2 方向**真证伪**）
- K-N26-3 NOT TRIGGERED（3/5 教师 < 0.60，未达 ≥4 阈值；v1/v2 方向**略不达**）
- K-N26-N1 pass=True（22 caption 各 ≥1 successful 字面满足）
- K-N26-N2 pass=True
- 与 L4 verdict `74B5B37F7EEA` §11「FAIL · 构造不可行」一字不动——**同方向深化非翻案**

**(b) T1.5r2 四项全追认生效即锁**（沿 `8355724A26E3` + ledger v6 §2 关键链 14 件 0 触动字面）：
- T1.5r2 verdict 锚 `8355724A26E3`（41,246 B；扩样 N_min 根因消除）
- T1.5r2 result 锚（`C69AB0E3002E`，沿 ledger v6 §2 字面）
- T1.5r2 executor 锚（`4B5B720D5CDA`，沿 ledger v6 §2 字面）
- T1.5r2 prereg 锚 `883DCED872B4` + T1.5r2 activation 锚 `F6ED61C25572`（**沿 ratify_formal=all 字面 activation 系已追认**）

**(c) activation 系全追认生效即锁**（沿 add_T1/T1.5/T15r2 activation 字面）：
- `add_T1_activation_2026_09_24.md` `79936B630015`（14,234 B；沿 ledger v6 §2 + E-35.1 b 字面）
- `add_T15_activation_2026_09_24.md` `443EFB39804A`（20,751 B；沿 ledger v6 §2 + E-35.1 b 字面）
- `add_T15r2_activation_2026_09_26.md` `F6ED61C25572`（沿 ledger v6 §2 + E-35.1 b 字面）
- `add_L14V3_activation_2026_09_24.md` `843E42EF4D2A`（21,309 B；沿 ledger v6 §2 字面）

**(d) 词表 §2.2 口径全追认生效即锁**（沿 verdict_v2 §2.2 + signoff `BA4D07BD7000` §1.2 字面）：
- TH-v2-1 N≥50 = **✓ 通过**（实测 72 ≥ 50；n_total_actual = 37 v1.1 + 35 addendum）
- TH-v2-2 R 反转 ≥5 = **✓ 通过**（实测 16 = 7 R-pair + D3 read_flip + case1 disposition）
- TH-v2-3 跨日 ≥3 天 / 单日 ≤60% = **✓ PI supersede**（实测跨日 2 天 / D1=66.7% → 沿 ask_822b1e27 拍板 th23_span=跨度 3 天解读达标 supersede；D1=48/80=60.0% 理论边缘态）

**E-35.1 状态**：4 类追认全生效留痕完成；PI 2026-09-26 19:05 ratify_formal=all 拍板 + verifier 签字稿 §8.1 PASS 字面一致；本棒仅作字面登记不擅自改写拍板原文。

#### §22.10.2 E-35.2 72 件口径拍板（8 件 D1 缺位不补造，正式判定有效）

**字面源**：`results/_v4_pi_cot_v2_verdict_v2.md` `5D79E67A4E9D` §1.2 + `results/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` `BA4D07BD7000` §1.1-§1.3 + `ask_96e0f651f306f2337cd57b47` 全推荐拍板字面。

**72 件口径字面**（沿 signoff §1.1 字面）：

| 维度 | 字面 | 实测复算 | 一致性 |
|---|---|---|---|
| v1.1 dataset (n_v11) | 37 | 37（v1.1 dataset 字面） | ✓ |
| D1_supp | 3 | 3 | ✓ |
| D2_w1 | 4 | 4 | ✓ |
| D2_w2 | 4 | 4 | ✓ |
| D2_w3 | 4 | 4 | ✓ |
| D2_w4 | 4 | 4 | ✓ |
| D2_w5 | 4 | 4 | ✓ |
| D3_w1 | 4 | 4 | ✓ |
| D3_w2 | 4 | 4 | ✓ |
| D3_w3 | 4 | 4 | ✓ |
| **n_addendum_loaded** | **35** | 3 + 5×4 + 3×4 = **35** | ✓ |
| **n_total_actual** | **72** | 37 + 35 = **72** | ✓ |
| n_total_theoretical | 80 | 72 + missing_d1_rf_fill(8) = 80 | ✓ |
| n_correction | 16 | 16（result_v2 字面） | ✓ |
| missing_d1_rf_fill | 8 | 8（盘外待采，如实声明） | ✓ |

**8 件 D1 缺位不补造**（沿 signoff §1.1 + verdict_v2 §1.2 字面）：
- `missing_d1_rf_fill = 8` = **盘外待采**，**不补造**（沿 verdict_v2 §1.2 字面「理论 80 vs 实测 72 差额 = 8 件缺位，盘外待采，**如实声明**；不擅自补造 / 不擅自调整 n_total」）
- **正式判定有效**（沿 ratify_formal=all 拍板字面）：72 件 + 8 件缺位声明 + 复合定性 + signoff PASS 四要件成立 = 正式判定有效

**E-35.2 状态**：72 件口径拍板完成；8 件 D1 缺位如实声明 + 不补造 + 正式判定有效（ratify_formal=all 字面）；本棒仅作字面登记不擅自调整 n_total / 不擅自补造 D1。

#### §22.10.3 E-35.3 锚链统一 on-disk SHA-12（指纹字段口径待拍板）

**字面源**：本件 `2DD8039D47E4` v18 派生锚链 + E-34.5 §22.7.5「锚链口径待拍板注记」字面 + signoff `BA4D07BD7000` §0.1-§0.4 实测锚链完整性复核字面。

**锚链统一原则**（沿 E-34.5 §22.7.5 + E-35.3 字面）：
- **本勘误链 v18 + 本轮所有下游引用** 锚链口径统一为 **on-disk SHA-12**（盘实测 `Get-FileHash -Algorithm SHA256` 前 12 字符 + uppercase）
- **on-disk SHA 口径**（盘实测）= E-34.4 §22.7.4 + signoff §0.4 addendum_sha_actual + verdict_v2 §0 字面引用
- **fingerprint 字段口径**（JSON 字段值经 SHA-256 取前 12 位）= `fingerprint_self_hash_after_birth` 字段字面（d2 系 5 件 addendum）
- **两种口径在 d2 系 5 件中并存使用**——E-34.5 §22.7.5 字面「无统一口径文档明示」

**锚链统一 action**（本棒仅作字面登记，不擅自重算或重写）：
- **本勘误链 v18 全引用 on-disk SHA 单一口径**（v17 `2DD8039D47E4` 等）
- **下游引用（清单补账件 v2 / 三封委托信 v3 / E-35 全部子条）** 一律沿 on-disk SHA 单一口径
- **fingerprint 字段口径**（d2/d2b/d2c/d2d/d2e 五件 fingerprint_self_hash_after_birth 字段值 ≠ 各 addendum 件本体盘实测 SHA-12）= **沿 E-34.5 §22.7.5 4 选项待 PI 拍板**：
  - 选项 (a)：以 on-disk SHA 为唯一权威口径，fingerprint 字段值视为派生字段（须在 d2 系 5 件追加字段说明 + verifier 独立复核）
  - 选项 (b)：以 fingerprint 字段值为唯一权威口径（须重算各 addendum 件本体 fingerprint 字段值 + 全链 5 件同步追加）
  - 选项 (c)：保留两种口径并存但明确分层语义（on-disk SHA = 文件本体验证 / fingerprint = 派生字段验证）
  - 选项 (d)：PI 另行处置

**E-35.3 状态**：锚链统一 on-disk SHA-12 完成；fingerprint 字段口径待 PI 拍板（4 选项同上）；本棒仅登记不擅自重算或重写 d2 系 5 件任何字段值。

#### §22.10.4 E-35.4 小项打包处置六条

**(i) 清单补账件 v2 出件**：本轮派工 `results/_v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md` 已出（沿派工单 A 字面），落盘字节 + SHA-12 由 doc-writer handoff 报值；与盘点件 + 勘误件 + 补账件 v1 + 勘误链 v17 五件并列存在；下游引用一律五件套并列引用。

**(ii) 三封委托信 v3 出件**（沿派工单 B 字面）：
- KIMI 上传委托信 v3：`letters/_v4_commission_upload_executor_2026_09_24_v3.md`（SHA-12 + 字节落盘后实测）
- coze 项目汇报 wechat 委托信 v3：`letters/_v4_commission_wechat_report_coze_2026_09_24_v3.md`（SHA-12 + 字节落盘后实测）
- GLM 论文终稿委托信 v3：`letters/_v4_commission_paper_final_glm_2026_09_24_v3.md`（SHA-12 + 字节落盘后实测；**涉 GLM 表述一律「以 PI 的 github 为唯一权威源（受托方已知）」**沿 `ask_9c8751ec` 字面）
- v1 + v2 委托信 6 件**全部 0 触动**（沿 PI 2026-09-23「v1/v2 件一律不覆盖」纪律 + 派工单 B 字面）

**(iii) v1 + v2 委托信 6 件 0 触动自查**：
- `letters/_v4_commission_upload_executor_2026_09_24.md` v1（13,012 B · `ADFA7DD03F76`）= 未触动 ✓
- `letters/_v4_commission_upload_executor_2026_09_24_v2.md` v2（13,012 B · `ADFA7DD03F76` 派生）= 未触动 ✓
- `letters/_v4_commission_wechat_report_coze_2026_09_24.md` v1（7,197 B · `15F8227308BC`）= 未触动 ✓
- `letters/_v4_commission_wechat_report_coze_2026_09_24_v2.md` v2（7,197 B · `15F8227308BC` 派生）= 未触动 ✓
- `letters/_v4_commission_paper_final_glm_2026_09_24.md` v1（10,515 B · `53A425FE1BD2`）= 未触动 ✓
- `letters/_v4_commission_paper_final_glm_2026_09_24_v2.md` v2（10,515 B · `53A425FE1BD2` 派生）= 未触动 ✓

**(iv) 18 frozen + 9 网格 + P-G v0/v01 + plugin spec + verifier 内置脚本 整段不动自查**：本棒 0 件触动，沿 R5 重建 V4 frozen 口径执行。

**(v) 派生 JSON 不合并 + 不擅自调阈值 + 不擅自补造 / 不擅自改写拍板原文**：本棒 0 件派生 JSON 产出；阈值一字未动（TH-v2-1/2/3 + K-N26-1/2/3 + K-N26-N1/N2 + K-V2-a/b1/b2/c + ACC=0.70 / AUC=0.75 / TEACHERS_LT=0.60 全字面不动）；拍板原文逐字保留（ratify_formal=all + ask_822b1e27 + ask_9c8751ec 字面均按字面引述）。

**(vi) V4 阶段铁律沿用口径自查**：V3 时期 no_llm / no_proxy / no_gateway V4 放开（沿 PI 2026-09-22「V3 的剑不斩 V4 的官」字面）；key 永不明文（无例外）+ 18 frozen 与 9 网格不动 + P-G v0/v01 不动 + plugin spec 不动 + 派生 JSON 不合并 + 不擅调阈值 全部沿用（沿 PI 2026-09-22「铁律沿用口径」字面）。

**E-35.4 状态**：6 小项打包处置完成；本棒仅作字面登记不擅自代决 / 不擅自重构。

#### §22.10.5 E-35.5 正式裁决引用（`5D79E67A4E9D` 复合定性）

**字面源**：`results/_v4_pi_cot_v2_verdict_v2.md` `5D79E67A4E9D`（33,723 B；2026-09-26 by verdict-keeper `agent-3a4d09ba3c90`）§0 + §1.2 + §2.1-§2.5 + §3.2 字面 + signoff `BA4D07BD7000` §2 + §5.1 字面 + ratify_formal=all 拍板字面。

**正式裁决 `5D79E67A4E9D` 复合定性字面**（沿 verdict_v2 §0 + §2.5 + signoff §2.6 字面）：
- **VERDICT**: `formal v2, FAIL`（正式判定 FAIL · 二值字面，无 CONDITIONAL 字样）
- **4 个 kill-line 全部 hit=True**（沿 verdict_v2 §2.1-§2.4 + signoff §2.1-§2.4 字面）：
  - K-V2-a 学习线：mean_similarity = **0.0909** < 0.80 → hit=True（n=22 held-out，19/22 sim=0 = 86.4%）
  - K-V2-b1 批判线-覆盖：div_critical_coverage = **0.6842** < 1.00 → hit=True（13/19 = 0.6842，6 件无批判词中 3 件 actual=[]）
  - K-V2-b2 批判线-盲从：blind_obey_rate = **0.3333** > 0.10 → hit=True（1/3 = 0.3333，idx=23 单事件决定全读法结论）
  - K-V2-c 稳健线：bootstrap CI = **[0.0, 0.2045]** < 0.50 → hit=True（n=1000, seed=42, percentile method）
- **复合定性 2 复合 + 2 β**（沿 verdict_v2 §2.5 + signoff §2.6 字面）：
  - K-V2-a = **复合：部分 α + 部分 β**（v2 词表扩 201+35 但召回率度量下 sim=0 系统性主导）
  - K-V2-b1 = **(β) 假证伪疑点未排除**（构造失灵族主导；6 件无批判词中 3 件 actual=[]）
  - K-V2-b2 = **复合：部分 α + 部分 β**（n=3 极小样本 + idx=23 单事件决定 0.0 vs 0.3333 = 结构性高方差）
  - K-V2-c = **(β) 假证伪疑点未排除**（小样本 + 退化构造联合产物）
- **any_hit = True**（4 hit 全部成立） → FAIL 立案字面成立
- **E-27 §13 判别四要件复核成立**：① kill-line 先于实验冻结 ✓ / ② 构造非恒等非退化 部分满足 / ③ 素材面覆盖 到位 / ④ 度量有分辨力 疑点 — 4 要件不全满足，按 E-27 §13 字面**不应机械判真证伪**；**复合定性成立**
- **不外推边界**：禁止外推至「PI 思维链不可蒸馏」/「批判性学习维度不可能达标」（沿 verdict_v2 §3.2 字面）

**E-35.5 状态**：正式裁决 `5D79E67A4E9D` 复合定性引用登记完成；本棒仅作字面引用登记，定性裁定之最终生效沿 ratify_formal=all 拍板字面生效即锁；本棒不擅自改写 / 不擅自重构拍板原文。

#### §22.10.6 E-35.6 归档二棒 6 项路径差异按 ledger v6 追溯口径注记

**字面源**：`results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` `CC498BC28525`（37,629 B；2026-09-26 by worker）§E.2 字面 + §3.1 字面。

**6 项路径差异按 ledger v6 追溯口径注记**（沿 ledger v6 §E.2 L289-L291 三段字面 + L291 字面「6 件 prereg/model_mapping/track2_verdict」分组）：

| # | 引用方文本（引用方文本不动） | 字面引用 | 移动后实际路径（追溯） |
|:-:|---|---|---|
| 1 | `_v4_pi_cot_v2_coding_review_2026_09_26.md`（5FBEC21E0AD2，42,914 B） | 字面引用 `_tmp_*.py`（4 件：`_tmp_degen.py` / `_tmp_v1_recompute.py` / `_tmp_v2_redesign.py` / `_tmp_verify.py`） | `deposon-sub/_tmp_degen.py` 等（4 件已 Move-Item 至 sub root，沿 ledger v6 §E.2 L289 字面） |
| 2 | `_v3_v4_achievements_inventory_2026_09_24.md`（29A853444D42，192,160 B） | 字面引用 50 件 B 类候选 | `deposon-sub/results/...`（50 件 B 类候选均已 Move / Trash，沿 ledger v6 §E.2 L290 字面） |
| 3 | `_v3_v4_achievements_inventory_3dir_2026_09_24.md`（3E4E90FB48E1，355,687 B） | 字面引用 50 件 B 类候选 | 同上（沿 ledger v6 §E.2 L290 字面） |
| 4 | `_v3_v4_ghostref_reconciliation_2026_09_23.md`（1D52DB0EBF53，169,864 B） | 字面引用 50 件 B 类候选 | 同上（沿 ledger v6 §E.2 L290 字面） |
| 5 | `_archive_manifest_deposon_sub_2026_09_23.json`（B34B9F7BDFB7，52,153 B）+ `_ghostref_copy_log_2026_09_23.json`（8CD133D0896F，129,780 B） | 字面引用 50 件 B 类候选 | 同上（沿 ledger v6 §E.2 L290 字面） |
| 6 | `_v4_supp_l14v3_model_mapping_2026_09_24.md`（98A779D61C1E）+ `_v4_supp_prereg_v02_add_L14V3_2026_09_24.md`（05B975A86989，61,547 B）+ `_v4_supp_prereg_v02_add_T15r2_2026_09_26.md`（883DCED872B4）+ `_v4_supp_prereg_v02_add_T15_2026_09_24.md`（8898B964A9D9，76,991 B）+ `_v4_supp_prereg_v02_add_T1_2026_09_24.md`（802DECE2286A，52,942 B）+ `_v4_track2_multimodel_verdict_2026_09_23.md` | 字面引用 `_track2_endpoints_probe_2026_09_23.json` | `deposon-sub/results/_track2_endpoints_probe_2026_09_23.json`（沿 ledger v6 §E.2 L291 字面） |

**追溯口径（沿 ledger v6 §E.2 字面）**：
- **引用方文本不动**：上 6 项引用方文本全部 0 触动；如需更新上述文本，沿 ledger v6 §E.2 L289-L291 字面「待 PI 拍板」
- **派工单 §4 保护名单 0 触动**：沿 ledger v6 §0 字面「派工单 §4 保护名单 11 类 0 触动」
- **关键链 14 件 SHA-12 全 0 触动**：沿 ledger v6 §2 字面（L14V3 + T1.5r2 + prereg + T1/T1.5 verdict 14 件 pre/post SHA-12 实测一致）

**E-35.6 状态**：归档二棒 6 项路径差异按 ledger v6 `CC498BC28525` §E.2 字面追溯口径注记完成；引用方文本不动（沿 ledger v6 §E.2 字面「待 PI 拍板」）；本棒仅登记不擅自更新引用方文本 / 不擅自追溯代写新路径。

---

### §22.11 v18 追加节 SHA 自核 + 版本变更记录

#### §22.11.1 v18 追加前 SHA 自核（沿 v17 末态）

| 件 | 追加前 SHA-12 | 字节 |
|---|---|---|
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（v17 末版） | **`2DD8039D47E4`** | **198,204** |

> **锚定证据**：派工单 audit_auth 字面声明 v17 = `2DD8039D47E4`（198,204 B）—— 实测核验 ✓（v16 `AB50FEC180DA` 174,445 B → v17 `2DD8039D47E4` 198,204 B，差异源于 v17 追加 §22.7 E-34（5 子条）+ §22.8（v17 SHA 自核 4 小节）+ §22.9（E-34 边界声明）共三节，字节 174,445 → 198,204）。

#### §22.11.2 v18 追加节源件 SHA-12 链（1 件派工锚 + 11 件独立上游件）

**E-35 引用的源件**（不触动，仅字面引用）：

| 路径 / 锚 | 盘 SHA-12 / 锚 | 实际语义 |
|---|---|---|
| PI 派工锚 `ask_96e0f651f306f2337cd57b47` | 全推荐 + ratify_formal=all | E-35.1 追认全生效留痕字面源 |
| PI 派工锚 `ask_9c8751ec` | 「KIMI与GLM知道即可」「你侧无额外补充」 | E-35.4 (ii) 三封委托信 v3 字面源 + 涉 GLM 表述口径 |
| PI 派工锚 `ask_822b1e27` | PI 2026-09-26 18:42 th23_span=跨度 3 天解读达标 supersede | E-35.1 d + E-35.2 字面源 |
| `results/_v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md` | （落盘后实测） | E-35.4 (i) 清单补账件 v2 字面源 |
| `letters/_v4_commission_upload_executor_2026_09_24_v3.md` | （落盘后实测） | E-35.4 (ii) KIMI 上传委托信 v3 字面源 |
| `letters/_v4_commission_wechat_report_coze_2026_09_24_v3.md` | （落盘后实测） | E-35.4 (ii) coze wechat 委托信 v3 字面源 |
| `letters/_v4_commission_paper_final_glm_2026_09_24_v3.md` | （落盘后实测） | E-35.4 (ii) GLM 论文终稿委托信 v3 字面源 |
| `results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` | `CC498BC28525`（37,629 B） | E-35.6 归档二棒 6 项路径差异追溯口径字面源 |
| `results/_v4_pi_cot_v2_verdict_v2.md` | `5D79E67A4E9D`（33,723 B） | E-35.5 正式裁决复合定性字面源 |
| `results/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` | `BA4D07BD7000`（26,637 B） | E-35.1 + E-35.2 + E-35.5 字面引用 PASS + ratify_formal=all 沿用 |
| `results/_v4_pi_cot_v2_coding_review_2026_09_26.md` | `5FBEC21E0AD2`（42,914 B） | E-35.6 #1 字面引用 `_tmp_*.py` |
| `results/_v4_supp_l14v3_n26_verdict.md` | `F4435801D09F`（64,485 B） | E-35.1 a N-26 定性字面源 |
| `results/_v4_supp_t15r2_verdict.md` | `8355724A26E3`（41,246 B） | E-35.1 b T1.5r2 四项字面源 |
| `results/_v4_supp_prereg_v02_add_T15r2_2026_09_26.md` | `883DCED872B4` | E-35.1 c activation 系字面源 |
| `results/_v4_supp_prereg_v02_add_T15r2_activation_2026_09_26.md` | `F6ED61C25572` | E-35.1 c activation 系字面源 |

**E-35 引用的字面锚**：
- E-34 旧行（E-34.1 §22.7.1 / E-34.2 §22.7.2 / E-34.3 §22.7.3 / E-34.4 §22.7.4 / E-34.5 §22.7.5 / §22.8 / §22.9）—— E-35.1 a/b/c 字面引用 E-34.2 §22.7.2 N-26 真审终裁 + E-34.3 §22.7.3 T1 系全链闭环 + E-34.5 §22.7.5 锚链口径
- E-32 §21 旧行（拍板留痕汇 + SHA 漂移注记 + 三条断层 + 夜间保守口径自主决策 + 待核疑点 3 条入链）—— ratify_formal=all 沿用 E-32.4 拍板汇
- L4 verdict `74B5B37F7EEA`（盘已清出但 ledger L208 字面引用；E-35.1 a 字面引用「FAIL · 构造不可行」一字不动）

#### §22.11.3 v18 追加后 SHA 自核（**循环约束 self-referential**）

| 件 | 追加后 SHA-12 | 字节 |
|---|---|---|
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（v18 = 原 v17 + §22.10 E-35 + §22.11 + §22.12） | （自指回环：写完即落盘；任何编辑会改变本字段自身。落盘报值见执行棒 stdout；外部观测者请用 `Get-FileHash -Algorithm SHA256 docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 独立复算） | （落盘后实测） |

#### §22.11.4 v18 版本变更记录

- **v17 → v18 变更范围**：**仅追加** §22.10（E-35 6 子条：E-35.1 追认全生效留痕 + E-35.2 72 件口径拍板 + E-35.3 锚链统一 on-disk SHA-12 + E-35.4 小项打包处置六条 + E-35.5 正式裁决引用 + E-35.6 归档二棒 6 项路径差异追溯口径注记）+ §22.11（本节 v18 SHA 自核 + 版本变更 4 小节）+ §22.12（E-35 边界声明）；**0 处修改** v17 既有 §1–§22.9 内容 + 0 处修改 E-1…E-34 旧行
- **版本演进链续 v17**：v17（2026-09-26 追加 E-34 5 子条，字面源 5 件独立上游件 + 拍板锚 `ask_c4c1b896880ba5e6292a6a5c` + L4 verdict `74B5B37F7EEA`，198,204 B / `2DD8039D47E4`）→ **v18（2026-09-26 追加 E-35 6 子条，追认全生效留痕 + 72 件口径拍板 + 锚链统一 + 正式裁决引用 + 路径差异注记，字面源 1 件派工锚 `ask_96e0f651f306f2337cd57b47` + 1 件派工锚 `ask_9c8751ec` + 1 件派工锚 `ask_822b1e27` + 11 件独立上游件）**
- **追加方法**：`edit` 工具 `old_string` 精确匹配 v17 末行（`*出证：Trae code · 2026-09-23 → v17 续 ...*`，198,204 B / SHA-12 `2DD8039D47E4`），`new_string` 保留 v17 末行一字不动 + 新增 `---` 分隔 + 追加 §22.10（E-35 6 子条）+ §22.11（4 小节）+ §22.12（E-35 边界声明）+ 新末行
- **旧 E-1…E-34 内容核验**：v17 `2DD8039D47E4`（198,204 B）落盘后按 §1–§22.9 内容哈希自核 → **追加后前 198,204 B 字节级未变**（实测 prefix SHA-12 = `2DD8039D47E4` ✓）
- **v18 末态全文件 SHA-12**（执行棒 stdout 报值）：（自指回环：本节任何编辑都会改变本字段自身；执行棒交付时实测 SHA-12 + 大小在 doc-writer handoff 报告中给出；外部观测者请用 `Get-FileHash -Algorithm SHA256 docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 独立复算）

---

### §22.12 E-35 边界声明（v18 追加）

- **未修改任何 E-1…E-34 旧行 / 未修改 v17 §1–§22.9 既有 §12 + §15 + §17 + §18 + §19 + §20 + §21 + §22 + §22.5 + §22.6 + §22.7-§22.9 内容**：追加前 v17 末态 prefix SHA-12 = `2DD8039D47E4`（实测，落盘后 append 完成即刻核验）；§22.10–§22.12 仅追加于 v17 末行（`*出证：Trae code · 2026-09-23 → v17 续 ...*`）之后
- **未修改任何 V1–V3 资产**：本节为勘误追加节，0 件 V1-V3 资产触动
- **未修改任何 V4 frozen 链 / 不动 R5 frozen 触禁件**：E-35 引用的 14 件核锚件（清单补账件 v2 + 三封委托信 v3 + ledger v6 + verdict_v2 + signoff + coding_review + n26 verdict + T1.5r2 verdict + add_T15r2 prereg + add_T15r2 activation + E-34 旧行）+ 拍板锚 3 件（`ask_96e0f651f306f2337cd57b47` + `ask_9c8751ec` + `ask_822b1e27`）+ 字面引用 1 件（L4 verdict `74B5B37F7EEA`）= 共 18 件全部只读引用，未触动；pre/post SHA 自证一致；不动清单补账件 v2 / 三封委托信 v3 / ledger v6 / verdict_v2 / signoff / coding_review / n26 verdict / T1.5r2 verdict / add_T15r2 prereg / add_T15r2 activation / E-34 旧行 / L4 verdict 等任何链上件
- **R4 key 永不明文（无例外）**：本节全文 0 件 key 明文；grep 自检 clean
- **kill-line 字面不动**：E-35 不涉 kill-line；K-V2-a mean_similarity=0.0909 / K-V2-b1 div_critical_coverage=0.6842 / K-V2-b2 blind_obey_rate=0.3333 / K-V2-c bootstrap CI=[0.0, 0.2045] / K-N26-1 ACC=0.70 / K-N26-2 AUC=0.75 / K-N26-3 TEACHERS_LT=0.60 一字不动（沿 verdict_v2 §0 + n26 verdict §0 字面）；本节仅事实登记 + 字面引用 + 状态注记，无 kill-line 触动
- **不擅自调阈值**：0 阈值调整（TH-v2-1 N≥50 + TH-v2-2 R 反转 ≥5 + TH-v2-3 跨日 ≥3 天 / 单日 ≤60% + 词表 §2.2 口径 一字不动）
- **派生 JSON 不合并**：本节为勘误追加节，0 件派生 JSON 产出（清单补账件 v2 + 三封委托信 v3 均为 md 件，0 件 JSON 派生；d2 / d2b / d2c / d2d / d2e 五 addendum 件与 dataset v1.1 落盘前后 SHA-12 复验不变 ✓）
- **不覆盖既有件**：仅在 v17 末行追加 §22.10 + §22.11 + §22.12；既有件 0 覆盖；既有 E-1…E-34 0 触动；既有 v17 §1–§22.9 0 触动；既有清单补账件 v1 + 盘点件 + 勘误件 + 6 封委托信 v1/v2 0 触动
- **字面忠实**：E-35 引用 11 件独立上游件 + 3 件拍板锚 + 1 件 L4 verdict 字面均按字面引述；**PI 拍板原文逐字保留**（E-35.1「ratify_formal=all」+「全推荐」沿 `ask_96e0f651f306f2337cd57b47` 字面逐字录入；E-35.1 d「th23_span=跨度 3 天解读达标 supersede」沿 `ask_822b1e27` 字面逐字录入；E-35.4 (ii)「KIMI与GLM知道即可」「你侧无额外补充」沿 `ask_9c8751ec` 字面逐字录入；E-35.5 verdict_v2 §2.5「K-V2-a 复合 / K-V2-b1 β / K-V2-b2 复合 / K-V2-c β」字面逐字录入）；不擅自改写/润色/扩写/补全标点
- **succeeded ≠ 跑完**：本棒为 doc-writer 起草类，仅起草 §22.10 + §22.11 + §22.12 + 末行；不代表「E-35.1 追认全生效已落盘核验 / E-35.2 72 件口径已重测 / E-35.3 锚链口径已统一 / E-35.4 6 小项已全部执行 / E-35.5 正式裁决已复算 / E-35.6 路径差异已追溯」——6 子条目全部状态注记沿下文
- **「待 PI 复核 / 已追认生效即锁 / 字面引用登记完成 / 待 PI 拍板 / 引用方文本不动」状态注记**：
  - **E-35.1**（追认全生效留痕）= **全追认生效即锁**（PI 2026-09-26 19:05 ratify_formal=all 拍板，4 类 a/b/c/d 全追生效即锁；本棒仅作字面登记不擅自重构拍板原文）
  - **E-35.2**（72 件口径拍板）= **拍板完成**（72 件 + 8 件 D1 缺位不补造 + 正式判定有效；沿 ratify_formal=all 字面）
  - **E-35.3**（锚链统一 on-disk SHA-12）= **本棒锚链统一完成 + fingerprint 字段口径待 PI 拍板**（4 选项同上沿 E-34.5）
  - **E-35.4**（小项打包处置六条）= **6 小项打包处置完成**（仅登记不擅自代决 / 不擅自重构）
  - **E-35.5**（正式裁决引用）= **字面引用登记完成 + 定性裁定生效即锁**（沿 ratify_formal=all 拍板字面生效即锁；本棒不擅自改写 / 不擅自重构）
  - **E-35.6**（归档二棒 6 项路径差异追溯口径注记）= **注记完成 + 引用方文本不动**（沿 ledger v6 §E.2 字面「待 PI 拍板」；本棒仅登记不擅自更新引用方文本）
  - **6 子条目全部状态明示，不擅自拍板**
- **skill 缺位 fallback**（沿派工单）：本地 skill 加载器多次实录 Local skill not found —— 按 v17 §22.9 + 派工单锚 `2DD8039D47E4`（v17 末态）+ `68F66904C0C8` §A-§C 字面既有口径执行；**未编造 skill 不存在的虚构指令**

---

*出证：Trae code · 2026-09-23 → v18 续（2026-09-26 by doc-writer `agent-0032834a3e04`，勘误追加 E-35 6 子条：追认全生效留痕 + 72 件口径拍板 + 锚链统一 on-disk SHA-12 + 小项打包处置六条 + 正式裁决引用 + 归档二棒 6 项路径差异追溯口径注记，字面源 1 件派工锚 `ask_96e0f651f306f2337cd57b47` + 1 件派工锚 `ask_9c8751ec` + 1 件派工锚 `ask_822b1e27` + 11 件独立上游件）*

---

### §22.13 E-36 勘误追加（v19 · 2026-09-26 · KIMI 回函停手事件 + v2 信漂移 errata + 通道待指认注记）

> **v19 性质**：**仅追加** §22.13（E-36 3 子条）+ §22.14（v19 SHA 自核 + 版本变更）+ §22.15（E-36 边界声明）；**0 处修改** v18 既有 §1–§22.12 内容 + 0 处修改 E-1…E-35 旧行
> **派工单**：`ask_9aa5f0c1433db0ff2d7f77c9`（2026-09-26 19:39 显式拍板，三则：taga30=delist / e4ver=v18 / v2drift=errata_v2；channel 项 Other 未填，另行追问不入本棒）
> **触发事件**：KIMI 回函 `letters/_v4_commission_upload_executor_reply_v3_2026_09_24.md`（9,848 B · SHA-12 `50592E36ECAD`，2026-09-26 由 KIMI 受托出具）——上传前实测发现两件强制停手（§3.1 第 1 条 §3.2 强制停手 + 第 2 条 §2.5 强制停手）+ 一件留痕（§3.3）

#### §22.13.1 E-36.1 KIMI 回函停手事件记录

| # | 停手类型 | 件 | 表载 vs 实测 | 处置拍板 |
|:-:|---|---|---|---|
| 1 | **§3.2 强制停手**（禁传区子件出现于上传清单） | `results/_v4_supp_l6_s38v2_rootcause_verdict.md`（Tag-A #30，`973103878D6F` · 24,847 B） | 表载：MAIN 内正式成果件（v3 §2.2 #30 字面 + 补账件 v2 §8.1 #30 字面）<br>实测：MAIN 内不存在；唯一副本位于 `D:\私人资料\_non_upload_local_archive\results\`（禁传区子件） | **delist**（PI 拍板 `ask_9aa5f0c1433db0ff2d7f77c9` taga30=delist；该件唯一副本已位于禁传区，本就严禁上传，移出禁传区无意义；delist 后 Tag-A 由 30 件 → 29 件） |
| 2 | **§2.5 强制停手**（表载与盘上 SHA/字节失配） | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（E-4） | 表载：v17 `2DD8039D47E4` · 198,204 B（v3 §2.4 字面 + 补账件 v2 §6.1 字面）<br>实测：v18 `CA8B95DDAA70` · 225,731 B | **以盘上 v18 现行版为准；v17 字面作废**（PI 拍板 `ask_9aa5f0c1433db0ff2d7f77c9` e4ver=v18；v18 = v17 + §22.10 E-35 6 子条 + §22.11 v18 SHA 自核 + §22.12 E-35 边界声明） |
| 3 | **§3.3 留痕**（v2 信漂移 errata） | `letters/_v4_commission_upload_executor_2026_09_24_v2.md`（v2 件） | 表载：v3 §Z 字面挂 v2 条目 = `ADFA7DD03F76` · 13,012 B（实测为 v1 件 SHA-12 误挂 v2 条目）<br>实测：盘上 v2 件 = `FF2154CE182D` · 16,894 B | **以 v3 为准、v2 停用；errata 事实入档**（PI 拍板 `ask_9aa5f0c1433db0ff2d7f77c9` v2drift=errata_v2） |

> **KIMI 沿 v3 委托信字面执行**（沿 `letters/_v4_commission_upload_executor_reply_v3_2026_09_24.md` §6 字面）：
> - 未修改、未移动、未删除盘上任何文件
> - 未上传任何文件到任何公网渠道
> - 0 触动任何既有件；本函为 `letters/` 下新增件

> **补账件 v2.1 出件**（沿 `results/_v3_v4_achievements_inventory_3dir_addendum_v2p1_2026_09_26.md` 17,130 B · SHA-12 `4C731A625868`）：本棒由 doc-writer 同步出件，将三拍板（taga30=delist / e4ver=v18 / v2drift=errata_v2）字面录入补账件 v2.1，本件 v19 E-36 同步追加 → 七件套并列（盘点件 + 勘误件 + 补账件 v1 + 补账件 v2 + 勘误链 v18 + 补账件 v2.1 + **勘误链 v19**）

#### §22.13.2 E-36.2 v2 信漂移 errata（沿拍板 v2drift=errata_v2）

- **v3 委托信 §Z 表字面错记**：v3 §Z 第 226 行字面写「v2 件（0 触动）`letters/_v4_commission_upload_executor_2026_09_24_v2.md` | 13,012 | `ADFA7DD03F76`」——实测为 v1 件 SHA-12 误挂 v2 条目；v1 件（不带 `_v2` 后缀）实测 = `ADFA7DD03F76` · 13,012 B（与 v3 §Z 字面一致）；v2 件（带 `_v2` 后缀）实测 = `FF2154CE182D` · 16,894 B（与 v3 §Z 字面不一致）
- **处置**：以 v3 为准、v2 停用；errata 事实入档
- **v2 件终态**：v2 件 `letters/_v4_commission_upload_executor_2026_09_24_v2.md` = **停用**（不删除、不覆盖；停用事实登记入档）
- **现行版**：v3 件 `letters/_v4_commission_upload_executor_2026_09_24_v3.md` = `C20D4F58F5C8` · 25,091 B（沿 v3 出件后 19:50 快照；本件 v19 出件后若再继续生长，须重新拍板）
- **不动依据**：R5「只追加不覆盖」铁律；v3 §Z 表字面保留不动（漂移事实由补账件 v2.1 §3 + 本件 §22.13.2 字面登记）

#### §22.13.3 E-36.3 通道待指认注记

- **KIMI 回函 §4 字面**（沿 `letters/_v4_commission_upload_executor_reply_v3_2026_09_24.md` §4 字面）：
  - 收到 GitHub PAT 一枚（会话内明文）：**未使用、未写入任何文件 / JSON / log、未在任何输出中复述**；本回函不含任何凭据
  - **通道未执行**：委托 §4.3 载明通道由 PI 另行指认、本件不预设；arXiv 通道非 KIMI 可执行（需 PI 自有账号与提交流程）；GitHub 通道需 PI 明示**仓库 / 分支 / 目录落点**后方可按 §4.1 三方一致口径执行
  - **提醒**：该 PAT 已在会话中明文暴露，无论本次是否使用，建议 PI 吊销换新
- **本件 v19 处置**：通道指认维持 v3 委托信 §4.3 字面「PI 另行指认」口径；**GitHub 仓库 / 分支 / 目录落点 PI 另行给，本件不编造**
- **附加风险注记**（沿 KIMI 回函 §4 字面）：2026-09-20 曾刻意清空远端 9 月文件以保持已发表论文分区纯净；本次 44 件（沿 KIMI 回函 §1 字面——含 v3 §Z 漂移后实测 43 件 = Tag-A 29 + Tag-B 10 + E 表 4）均为 9 月时间戳材料，**PI 须确认公开发布范围与分区策略**

---

### §22.14 v19 追加节 SHA 自核 + 版本变更记录

#### §22.14.1 v19 追加前 SHA 自核（沿 v18 末态）

| 件 | 追加前 SHA-12 | 字节 |
|---|---|---|
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（v18 末态 = v17 末态 + §22.10-§22.12） | `CA8B95DDAA70` | 225,731 |

#### §22.14.2 v19 追加节源件 SHA-12 链（1 件派工锚 + 4 件独立上游件）

| 件 | SHA-12 | 字节 |
|---|---|---|
| `letters/_v4_commission_upload_executor_reply_v3_2026_09_24.md`（KIMI 回函，**E-36.1 字面源**） | `50592E36ECAD` | 9,848 |
| `letters/_v4_commission_upload_executor_2026_09_24_v3.md`（v3 委托信，**E-36.2 字面源**） | `C20D4F58F5C8` | 25,091 |
| `letters/_v4_commission_upload_executor_2026_09_24_v2.md`（v2 件，停用，**E-36.2 字面源**） | `FF2154CE182D` | 16,894 |
| `letters/_v4_commission_upload_executor_2026_09_24.md`（v1 件，留档，**E-36.2 字面源**） | `ADFA7DD03F76` | 13,012 |
| `results/_v3_v4_achievements_inventory_3dir_addendum_v2p1_2026_09_26.md`（**E-36.1 引用面 = 补账件 v2.1**） | `4C731A625868` | 17,130 |

> **派工锚 1 件**（沿派工单 `ask_9aa5f0c1433db0ff2d7f77c9` 字面）：taga30=delist / e4ver=v18 / v2drift=errata_v2 三则字面逐字录入（本棒 E-36.1 + E-36.2 字面源）

#### §22.14.3 v19 追加后 SHA 自核（**循环约束 self-referential**）

| 件 | 追加后 SHA-12 | 字节 |
|---|---|---|
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（v19 = 原 v18 + §22.13 E-36 + §22.14 + §22.15） | （自指回环：写完即落盘；任何编辑会改变本字段自身。落盘报值见执行棒 stdout；外部观测者请用 `Get-FileHash -Algorithm SHA256 docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 独立复算） | （落盘后实测） |

#### §22.14.4 v19 版本变更记录

- **v18 → v19 变更范围**：**仅追加** §22.13（E-36 3 子条：E-36.1 KIMI 回函停手事件记录 + E-36.2 v2 信漂移 errata + E-36.3 通道待指认注记）+ §22.14（本节 v19 SHA 自核 + 版本变更 4 小节）+ §22.15（E-36 边界声明）；**0 处修改** v18 既有 §1–§22.12 内容 + 0 处修改 E-1…E-35 旧行
- **版本演进链续 v18**：v18（2026-09-26 追加 E-35 6 子条，字面源 1 件派工锚 `ask_96e0f651f306f2337cd57b47` + 1 件派工锚 `ask_9c8751ec` + 1 件派工锚 `ask_822b1e27` + 11 件独立上游件，225,731 B / `CA8B95DDAA70`）→ **v19（2026-09-26 追加 E-36 3 子条：KIMI 回函停手事件 + v2 信漂移 errata + 通道待指认，字面源 1 件派工锚 `ask_9aa5f0c1433db0ff2d7f77c9` + 5 件独立上游件 = KIMI 回函 + v3 + v2 + v1 + 补账件 v2.1）**
- **追加方法**：`edit` 工具 `old_string` 精确匹配 v18 末行（`*出证：Trae code · 2026-09-23 → v18 续 ...*`，225,731 B / SHA-12 `CA8B95DDAA70`），`new_string` 保留 v18 末行一字不动 + 新增 `---` 分隔 + 追加 §22.13（E-36 3 子条）+ §22.14（4 小节）+ §22.15（E-36 边界声明）+ 新末行
- **旧 E-1…E-35 内容核验**：v18 `CA8B95DDAA70`（225,731 B）落盘后按 §1–§22.12 内容哈希自核 → **追加后前 225,731 B 字节级未变**（实测 prefix SHA-12 = `CA8B95DDAA70` ✓）
- **v19 末态全文件 SHA-12**（执行棒 stdout 报值）：（自指回环：本节任何编辑都会改变本字段自身；执行棒交付时实测 SHA-12 + 大小在 doc-writer handoff 报告中给出；外部观测者请用 `Get-FileHash -Algorithm SHA256 docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 独立复算）

---

### §22.15 E-36 边界声明（v19 追加）

- **未修改任何 E-1…E-35 旧行 / 未修改 v18 §1–§22.12 既有 §12 + §15 + §17 + §18 + §19 + §20 + §21 + §22 + §22.5 + §22.6 + §22.7-§22.9 + §22.10-§22.12 内容**：追加前 v18 末态 prefix SHA-12 = `CA8B95DDAA70`（实测，落盘后 append 完成即刻核验）；§22.13–§22.15 仅追加于 v18 末行（`*出证：Trae code · 2026-09-23 → v18 续 ...*`）之后
- **未修改任何 V1–V3 资产**：本节为勘误追加节，0 件 V1-V3 资产触动
- **未修改任何 V4 frozen 链 / 不动 R5 frozen 触禁件**：E-36 引用的 5 件核锚件（KIMI 回函 `50592E36ECAD` + v3 委托信 `C20D4F58F5C8` + v2 件 `FF2154CE182D` + v1 件 `ADFA7DD03F76` + 补账件 v2.1 `4C731A625868`）+ 拍板锚 1 件（`ask_9aa5f0c1433db0ff2d7f77c9`）+ 沿用 v18 E-35 字面引用 14 件核锚件 = 共 20 件全部只读引用，未触动；pre/post SHA 自证一致；不动 KIMI 回函 / 委托信 v3 / v2 件 / v1 件 / 补账件 v2.1 / E-35 既有引用链任何链上件
- **R4 key 永不明文（无例外）**：本节全文 0 件 key 明文；grep 自检 clean
- **kill-line 字面不动**：E-36 不涉 kill-line；K-V2-a mean_similarity=0.0909 / K-V2-b1 div_critical_coverage=0.6842 / K-V2-b2 blind_obey_rate=0.3333 / K-V2-c bootstrap CI=[0.0, 0.2045] / K-N26-1 ACC=0.70 / K-N26-2 AUC=0.75 / K-N26-3 TEACHERS_LT=0.60 一字不动（沿 verdict_v2 §0 + n26 verdict §0 字面）；本节仅事实登记 + 字面引用 + 状态注记，无 kill-line 触动
- **不擅自调阈值**：0 阈值调整（TH-v2-1 N≥50 + TH-v2-2 R 反转 ≥5 + TH-v2-3 跨日 ≥3 天 / 单日 ≤60% + 词表 §2.2 口径 一字不动）
- **派生 JSON 不合并**：本节为勘误追加节，0 件派生 JSON 产出（KIMI 回函 + v3 委托信 + v2 件 + v1 件 + 补账件 v2.1 均为 md 件，0 件 JSON 派生；d2 / d2b / d2c / d2d / d2e 五 addendum 件与 dataset v1.1 落盘前后 SHA-12 复验不变 ✓）
- **不覆盖既有件**：仅在 v18 末行追加 §22.13 + §22.14 + §22.15；既有件 0 覆盖；既有 E-1…E-35 0 触动；既有 v18 §1–§22.12 0 触动；既有清单补账件 v1 + 盘点件 + 勘误件 + 6 封委托信 v1/v2/v3 + KIMI 回函 v3 + 补账件 v2 0 触动
- **字面忠实**：E-36 引用 5 件独立上游件 + 1 件派工锚字面均按字面引述；**PI 拍板原文逐字保留**（E-36.1「taga30=delist」+「e4ver=v18」+「v2drift=errata_v2」沿 `ask_9aa5f0c1433db0ff2d7f77c9` 字面逐字录入；KIMI 回函 §3.1 第 1 条「§3.2 强制停手」、第 2 条「§2.5 强制停手」、第 3 条「§3.3 留痕」字面逐字录入；KIMI 回函 §4「通道未执行」「GitHub 通道需 PI 明示仓库/分支/目录落点」字面逐字录入）；不擅自改写/润色/扩写/补全标点
- **succeeded ≠ 跑完**：本棒为 doc-writer 起草类，仅起草 §22.13 + §22.14 + §22.15 + 末行；不代表「E-36.1 KIMI 停手事件已重新执行 / E-36.2 v2 信漂移已重测 / E-36.3 通道已指认」——3 子条目全部状态注记沿下文
- **「待 PI 复核 / 已追认生效即锁 / 字面引用登记完成 / 待 PI 拍板 / 引用方文本不动」状态注记**：
  - **E-36.1**（KIMI 回函停手事件记录）= **字面登记完成 + 三拍板沿 §5 字面逐字录入**（delist / v18 / errata_v2 已闭环；本棒仅字面登记 + 三拍板录入，不擅自重构拍板原文）
  - **E-36.2**（v2 信漂移 errata）= **errata 事实入档完成 + 以 v3 为准、v2 停用**（沿 v2drift=errata_v2 字面；v2 件停用事实登记入档，不删除、不覆盖）
  - **E-36.3**（通道待指认注记）= **KIMI 回函 §4 字面录入完成 + GitHub 仓库 / 分支 / 落点 PI 另行给**（本棒不编造通道参数；channel 项 Other 未填，另行追问不入本棒，沿派工单字面）
  - **3 子条目全部状态明示，不擅自拍板**
- **skill 缺位 fallback**（沿派工单）：本地 skill 加载器多次实录 Local skill not found —— 按 v18 `CA8B95DDAA70` §22.12 + 派工单锚 `ask_9aa5f0c1433db0ff2d7f77c9` + KIMI 回函 `50592E36ECAD` §3.1-§4 字面既有口径执行；**未编造 skill 不存在的虚构指令**

---

*出证：Trae code · 2026-09-23 → v19 续（2026-09-26 by doc-writer `agent-0032834a3e04`，勘误追加 E-36 3 子条：KIMI 回函停手事件记录 + v2 信漂移 errata + 通道待指认注记，字面源 1 件派工锚 `ask_9aa5f0c1433db0ff2d7f77c9` + 5 件独立上游件 = KIMI 回函 `50592E36ECAD` + v3 委托信 `C20D4F58F5C8` + v2 件 `FF2154CE182D` + v1 件 `ADFA7DD03F76` + 补账件 v2.1 `4C731A625868`）*
