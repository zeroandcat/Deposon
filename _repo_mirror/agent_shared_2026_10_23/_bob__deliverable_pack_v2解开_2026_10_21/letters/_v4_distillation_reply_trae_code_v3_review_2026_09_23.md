# 回函：V3 实验回审（真证伪/假证伪标注）+ 资产走读与修复 · Trae code → deposon PI

> **回函方**：Trae code（第三方走读 / 学术规范与论文写作辅助）
> **委托件**：`letters/TRAE_V3_REVIEW_LETTER_2026_09_23.md`（SHA-12 `0E7600AC4478`，7,510 B）
> **回函结构**：沿委托信 §6——§0 回审范围确认 / §1 标注表 / §2 回审表 / §3 走读与修复（前后 SHA 对照）/ §4 验证记录 / §5 边界声明 / §6 老实交代
> **方法声明**：本函 0 LLM 调用 / 0 外部 URL / 0 明文密钥；V1–V3 既有资产只读；V4 `_v4_*` 全链 0 触动；一切数字皆机器实算，凡未实算者显式标注「未算」。
> **诚实纪律**：本函只判「结论是否被其证据支持」，不重裁命题本身；标注 ≠ 篡改，修复 ≠ 翻案。凡我改不动的（frozen / 报告正文 / 仓外件），只登记不擅动。

---

## §0 回审范围确认

| 面 | 委托清单 | 本次实测 | 结论 |
|---|---|---|---|
| Runner | 30 个 P-A~P-O 相关 runner | repo `deposon_team/plugins/` 内 **13 件非冻结 *.py**（boss_pa_1/2/3、boss_pc_1/2/3、boss_pg_1/2/3、_pg_v01_compute、_verify_batch5、_verify_pg_v0/_v1）；`deposon-sub/deposon_team/plugins/` 内 **_p_i/j/k/l/m/n/o 系列** | 两层分置，非「30 件同处」 |
| Report | `docs/V3X/` 19 份 REPORT | **19/19 全在盘**，SHA-12 已逐一实算（见 §3 表） | 完整 |
| 数据 | `results/` 实验 JSON | **汇总层在 repo**（deposon_pa_d1_d3 / pc / pe / pf / pg_v01 / v19 / v21 / v20_gt2b 等）；**BOSS 分件层已移出至 `deposon-sub/results/`**（09-21 manifest 363 件） | 分置，见 §3 核实 |

**范围裁决**：委托所设「30 runner + 19 report + 数据 JSON 引用链」三面**均可走读**，但**引用路径与实体位置已分层错位**——这是本次回审的第一性事实，直接决定 §1/§2/§3 所有判定。

**前置勘误件**：`docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（新增件；本函 §3 的路径映射与缺陷清单以该件为准，不重复）。

---

## §1 标注表：V3 全实验结论 × 三分支 × 根因一句话

### 1.1 三分支的适用说明（先声明，后标注）

委托信 §2 的三分支（真证伪/假证伪/不明）定义针对**证伪型结论**（判死 / FAIL / DEAD / FAIL_H0 / kill-line 触发）。V3 结论中含有大量**存活型结论**（PASS / 差异化 / 保留 / STRICT_CONSERVATION）。为使「全部结论」逐条可标，本函对存活型结论启用**同构三分支**，并在表中以括号注明：

- **证伪型** → 真证伪 / 假证伪 / 不明（原定义）
- **存活型** → **真成立 / 假成立 / 不明**。其中「假成立」= 构造退化 / 素材面缺失 / 度量无鉴别力导致命题**未经受审即看似通过**（与「假证伪」同机制、反方向）——这是委托信未点名但 V4 执行实证中最常见的误导来源。

### 1.2 标注表

| # | 实验 / 结论对象 | 原结论（原文口径） | 标注 | 根因一句话 |
|---|---|---|---|---|
| 1 | BOSS-P-A1 (RBR/RM 倍数) | DIFFERENTIATED（145.8× ≥ 2.0×） | **假成立** | `simulate_rm` 返回值域 {≥6}∪{200}，22/22 图 `rm_iter`≡**6** 常量 → 倍数结论立在常量读数上，度量无鉴别力 |
| 2 | BOSS-P-A1 报告参考表 (L143–147) | 支撑 145.8×/4.9145× 的 22 图节选表 | **不明** | 表值（199/1/32/6.2188/0.0312）与冻结 JSON 实值（200/6/200/1.0/0.03）**逐字段不符**，且与同报告 §3.1 均值互斥 → 该表不可作证据 |
| 3 | BOSS-P-A2 (Potential Game) | DIFFERENTIATED（仅 3/22 = 13.6% 为 PG） | **不明** | 与 `KT_B1_REWORK` §三「22/22 全 PG」**反向冲突**；residual_mean 0.269 非退化，故非假证伪，但两构造口径未对齐 |
| 4 | BOSS-P-A3 (Replicator/ESS) | DIFFERENTIATED（0/22 ESS 重合） | **假成立** | `ess_freq`≡0.5、`is_ess`≡True、`ess_match`≡False **三项 22/22 全常量** → ESS 判据恒同，0/22 是构造产物 |
| 5 | 540 cells 守恒审计 | STRICT_CONSERVATION（max dev 2.22e-16） | **结构性恒等（不构成实验证据）** | 2.220446049250313e-16 = **IEEE 754 双精度机器 epsilon（2⁻⁵²）**；T+R+A=1 是构造恒等，残差即舍入极限，**无鉴别力** |
| 6 | BOSS-PC-1 (A1 resampling) | PASS（r2_mean 0.6661, range 0.1449 < 0.15） | **真成立** | 5 次重采样 r2 = .6221/.7355/.6522/.7300/.5906 有真实波动且全在阈值内，构造非退化 |
| 7 | BOSS-PC-2 (A2 fitting) | PASS（ratio 0.6099 < 0.9） | **真成立** | fits 内 r2_power .5558 vs r2_exp .339 有分辨，构造非退化 |
| 8 | BOSS-PC-3 (A3 clipping) | FAIL（worst_clipped_r2 0.3362 < 0.7） | **假证伪** | 三 trial 的 `r2_delta_full_minus_clipped` ≡**0.0**（3/3）→ clipping 为 no-op，判据未真正受审 |
| 9 | P-C 双相结构 | FAIL_H0（幂律死）×2 拟合 | **真证伪** | 沿 KT-C1 同源判死；kill-line 先于实验（V0 SPEC 预注册）；N=328 真实数据 R²=0.0007、bootstrap CI 含 0 |
| 10 | P-C exp_3_3 (r2_per_eta) | 该维度 UNVERIFIED | **假证伪** | `r2_per_eta` 对 9 model **逐字相同**、η=0.01 跨 model 方差 0.0 → 扫描与 model 无关，该维度无鉴别力（`_adendum_A` 自记） |
| 11 | BOSS-PE-1 (real 2d Ising) | GRAY（beta_mle 0.1934, delta 0.0684） | **不明** | GRAY 本体不可判；且该 JSON 与 boss_pe_3 存在命名轴错位（文件名/`boss_id` 不符，见勘误 §3） |
| 12 | BOSS-PE-2 (real transverse Ising) | PASS（9/9 model 显著偏离） | **假成立** | `h_c_at_T`≡0.5（9/9）、`transverse_ising_region`≡false（9/9）**全常量** → 判据输入恒同，「偏离」是常量化产物 |
| 13 | BOSS-PE-3 (real reservoir) | PASS（A 通道独立，\|Spearman−1\|=1.832） | **真成立（数字层需勘误）** | Spearman −0.832 出自 9 model 真实变化，非退化；但同值在 `P_C` L139 记 −0.8000 → 须勘误 |
| 14 | P-E 散射场 strict/loose | strict 6/2/1、loose 7/2/0（PARTIAL_PASS） | **真成立（待 PI 拍板）** | 9/9 model 复算与 stored 值 1e-4 内**全匹配**；strict/loose 阈值拍板权属 user |
| 15 | P-F D1 observer | all_mid_term_stable=True（自标 MID_TERM） | **真成立（中期限定）** | 报告自标 `MID_TERM_D1 (NOT final)`；45/45 守恒 + per_model 9/9 + 5 锚 STABLE_* 齐备 |
| 16 | P-F D1 canonical 5 值 | [UNVERIFIED] ×5 | **不明** | V7 自标 [UNVERIFIED]，并自认「实为 canonical 5 值拼接锚，非 V0.1 JSON 文件指纹」 |
| 17 | P-F D1 vs V0.1 链哈希 | ⚠️ 不匹配（报告自释为 cell count 差异） | **不明** | `chain_hash` + `value` 双不符；报告自释为预期行为，缺独立复算支撑 |
| 18 | P-G V0.1 5 锚真值 | 5/5 PASS | **真成立** | 5 锚 SHA 由占位 `230b5caee415` → 真值 `9c3c50005103`，判定线严守 |
| 19 | P-G boss_pg 三项 | SCAFFOLDING (PRE-REGISTRATION) | **不明** | 540-LLM 数据未落盘 + PI 未拍板 → 未实跑，无可判 |
| 20 | KT-B1 攻击成功率 | 16/75=21.3% PASS；135/600=22.5% PASS | **不明** | 同句内 21.3% 与「各 cell 11/15~13/15」**量级不符**，成功率口径不可判 |
| 21 | KT-B1 BOSS-B1/B2/B3 | GRAY_BOTH_BELOW / GRAY_BOTH_ABOVE（无 FAIL） | **不明** | 报告自认「deposon 失真上界是**占位值**」→ 通用基线未真受审 |
| 22 | KT-C1 幂律 | DEAD（R²=0.0007 < 0.3, slope 0.2838, CI 含 0） | **真证伪** | N=328 真实数据 + kill-line 先于实验（V0.1 SPEC）+ 10000 次 bootstrap；**是资产** |
| 23 | KT-C1 配套 BOSS-C1 | FAIL（撞上，diff_pct 0.88） | **真证伪** | 2D Ising 撞上致主张被拍平为 2D Ising 普适类特例 |
| 24 | KT-C1 配套 BOSS-C2/C3 | PASS（抵御） | **真成立** | mapping_valid/invariant 判据有分辨，非退化 |
| 25 | P-I real labels | PASS | **真成立** | 09-16 已修 `and→or` 判死线 + 加 UNVERIFIED 警告，诚实降级已落地 |
| 26 | P-J convergence basin | UNVERIFIED | **假证伪** | `convergence_rate` 全 **0.1**（var 0.0, n_unique 1）→ 对常量向量算 Spearman 无定义 |
| 27 | P-L P-C finite-size scaling | UNVERIFIED（已移除伪造 R² 公式） | **假证伪** | `max_R2` 恒 ≈0.3275 < 0.9 → `final_dang_verdict` 恒 PARTIAL_FAIL_H0，判据恒同 |
| 28 | P-M attack surface cost | UNVERIFIED | **假证伪** | `detection_rate` 全 **0.0**（8 档 budget）→ 检测率 < 0.5 违安全下界必要条件，判据退化 |
| 29 | P-M real separation | 双判死线（budget 或 miss_rate） | **真成立（09-16 已修）** | 09-16 已把「漏检最小成本 ≤ 随机猜测成本」的量纲混用改为分离量纲双线 + UNVERIFIED |
| 30 | P-K 跨主体盲测 | FPR 0.0 → 4.44%（2/45 误归因） | **真成立（负性发现）** | 盲测暴露 GLM 制品 JSON key-path 词表重叠（序列化格式泄漏），非行为泄漏——实证有效 |
| 31 | 22-caption embedding | NOISE（ratio 1.0562 < 1.2；ARI 0.0615） | **真证伪（负结果）** | SVD+kmeans 后 intra/inter ratio 近 1、ARI 近随机 → 模板前缀主导，无可用散射信号 |
| 32 | CPATH 理论模拟 | PARTIAL（边际 0%~+26.7%） | **不明** | 报告自标「待实测」，0.05 USD LLM 调用未执行 → 无实测面 |
| 33 | V42 V2 verifier | 5 类漏检 0.0（byte_swap 0.01）；更正 P-M 计数语义反转 | **真成立（自我更正活例）** | 2000 次单 bit 翻转复算**推翻**「漏检率 100%」→ 这是「假证伪被修正」的活例 |
| 34 | v19 E9.3 / E9.4 / E9.5 | FAIL ×3 | **真证伪** | 构造有效（McNemar 检验 + 两基准）：E9.4 gap 0.81 / p 1.7e-23，E9.5 delta −0.02 / p 0.5 |
| 35 | v20 GT2b | inconclusive | **不明** | 报告自标 inconclusive；rule_filter 0.15/0.275/0.20 低于 chance 0.25 |
| 36 | v21 GT formal | overall triggered（T_P1b triggered；T_P3 reparam killed） | **真证伪** | kill_reason `cosine<0`（min −1.0）、reparametrization_claim killed |
| 37 | v2 phase5 f5 | FAIL（P-B 守恒不成立） | **真证伪** | best_conservation 落于 "Quantum-like T+R+A=2"（value 1.5886, deviation 0.4114） |
| 38 | V3X 1 周判死（4 路径） | P-A PASS / P-C FAIL_H0 / P-E PARTIAL_PASS / P-F PASS | **不明** | 「540 cells **LLM 实算**」与「540 cells, **0 LLM**」并存、尾注「verdict **占位**待 D7 当日填」与正文已填 verdict 并存 → 状态层不可判 |
| 39 | V7 综合判死 | 3 PASS + 2 GRAY + 1 死 + 1 TRIGGERED | **不明** | 同报告内 **51/60 与 52/60 并存**；总计口径 L336 / L454 / L614 三处不一 |

**标注汇总（39 行逐条计）**：真证伪 **7**（#9,22,23,31,34,36,37）/ 假证伪 **5**（#8,10,26,27,28）/ 真成立 **11**（#6,7,13,14,15,18,24,25,29,30,33）/ 假成立 **3**（#1,4,12）/ 结构性恒等 **1**（#5）/ 不明 **12**（#2,3,11,16,17,19,20,21,32,35,38,39）。

**读法**：真证伪（7）与真成立（11）合为「命题真受审」的 18 条；假证伪（5）+ 假成立（3）+ 结构性恒等（1）合为「命题未受审 / 范畴错误」的 9 条；不明 12 条为证据面不足以判者。

---

## §2 回审表：结论等级（成立 / 过强 / 过弱 / 不可判）× 依据

本表轴与 §1 不同：§1 问「是不是证伪」，§2 问「**结论与证据是否相称**」。

| 结论（对象） | 等级 | 依据 |
|---|---|---|
| BOSS-P-A1 差异化 145.8× | **过强** | 证据是常量读数（`rm_iter`≡6），撑不起「散射层有差异化」这一强主张 |
| BOSS-P-A2 「仅 3/22 为 PG」 | **不可判** | 与 KT-B1「22/22 全 PG」反向；两构造口径未对齐，无第三方裁决面 |
| BOSS-P-A3 「0/22 ESS 重合」 | **过强** | 三字段全常量，等价于判据恒 False；「0/22」不是实验结果而是构造常数 |
| **P-A 方向中期 PASS（总）** | **过强** | 3 项 BOSS 支撑中 1 项常量退化（A1）、1 项冲突（A2）、1 项常量退化（A3）→ 不足以支撑「方向 PASS」 |
| 540 cells 守恒 STRICT_CONSERVATION | **过强** | 残差 = 机器 epsilon，属浮点结构恒等；把它当「守恒审计通过」的实验证据是范畴错误 |
| BOSS-PC-1 / PC-2 PASS | **成立** | 重采样/拟合读数有真实分布，阈值预注册 |
| BOSS-PC-3 FAIL | **过强** | 以 no-op 构造（delta≡0）为据判 FAIL，应降为「不可判」 |
| P-C 双相结构 FAIL_H0 | **成立** | 与 KT-C1 同源、kill-line 前置、N=328 |
| BOSS-PE-2 PASS | **过强** | 判据输入（`h_c_at_T`）为常量，9/9 偏离是构造必然 |
| BOSS-PE-3 PASS | **成立** | −0.832 出自真实分布（仅数字层口径需并列 −0.8000） |
| P-E strict 6/2/1 | **成立** | 9/9 复算 1e-4 内匹配；阈值拍板权已明示属 user |
| P-F D1 中期稳态 | **成立** | 自标中期限定，证据面（45/45、9/9、5 锚）齐备 |
| P-G V0.1 5/5 | **成立** | 真值替换占位，判定线严守 |
| KT-B1 攻击成功率 | **不可判** | 21.3% 与 11/15~13/15 量级冲突，口径未锁 |
| KT-C1 DEAD | **成立** | 设计健全 + 构造有效 + 素材充分 + 度量有分辨（四要件齐） |
| P-J / P-M / P-C-exp_3_3 的 UNVERIFIED | **成立** | 「UNVERIFIED」正是对退化的正确标注（不是过弱，是恰当降级） |
| V42 V2 自我更正 | **成立** | 复算推翻前诊断，且报告如实写明「计数语义反转」 |
| v19 E9.3–E9.5 / v21 / 22-caption / f5 | **成立** | 构造有效、kill-line 触发、负面结果如实归档 |
| V3X 1 周判死（4 路径） | **不可判** | 状态层自相矛盾（LLM 实算 vs 0 LLM；已填 vs 占位） |
| V7 综合判死 | **不可判** | 51/60 与 52/60 并存 + 三处总计口径不一 → 数字层不自洽 |
| BOSS-PE-1 GRAY / v20 GT2b / CPATH PARTIAL / boss_pg SCAFFOLDING | **不可判** | 各自声明为边际 / 未定 / 待实测 / 预注册占位 |

**等级汇总（21 条逐行计）**：成立 **10** / 过强 **6** / 过弱 **0** / 不可判 **5**（另 1 条「540 cells 守恒」归入「结构性恒等」）。

> **过弱 = 0** 值得一提：V3 未发现「结论弱于证据」者，即无「自我贬低」型误标。所有偏差方向一致——**证据弱于结论**（过强/假成立）。这与 V4 执行实证的方向一致。

---

## §3 走读与修复（前后 SHA-12 对照）

### 3.1 走读清单与可修复面裁定

**走读文件数**：repo `deposon_team/plugins/*.py` 31 件（含本次新增 6 件 review 脚本） + `docs/V3X/` 19 REPORT + `results/` 引用链 34 件 + `deposon-sub/` 363 件（manifest 索引） + `corpus/v20/` 23 件。

**可修复面裁定（关键）**：

| 层 | 件数 | 冻结状态 | 可改？ |
|---|---|---|---|
| 18 frozen（4 `skill_*` + 12 anchor） | 16 项在盘（2 项 anchor JSON 自身为 frozen 计数口径，见 `_verify_15frozen.py` L4 注） | **FROZEN** | ✗ §5 明令 |
| verifier 内置（`_verify_15frozen*.py`） | 2 | §5「不动」 | ✗ |
| P-G v0+v01 链（`_verify_pg_v0*.py`、`_pg_v01_compute.py`） | 3 | §5「不动 P-G v0+v01」 | ✗ |
| 19 REPORT 正文（含 V7 / 1WEEK_KILL / D5 / D_FIX2…） | 19 | §5「已冻结报告正文」 | ✗（数字矛盾走勘误清单，委托信 §3 明示） |
| V3 BOSS 分件层 JSON + `_p_*` runner | 363（deposon-sub） | 仓外；manifest 仅 `src/dst/sha12/size/archived_at`，**无移出原因/授权字段** | ✗（不予处置） |
| repo 内 P-A/P-C/P-G BOSS runner（`boss_*.py`） | 9 | 非冻结，但**承载判定本体**；其输入 JSON 已在仓外 | ✗（改路径 = 改运行语义，且会使其 SHA 与报告引用脱钩，制造新矛盾） |
| `_verify_batch5_2026_09_18.py` | 1 | 非冻结；为一次性 batch 验证脚本 | 无需改（无缺陷涉结论） |

**裁定**：本轮 **可修复面 = ∅**。委托信 §3 所列修复项（幽灵引用 / BOM / 缺 SELF-CHECK / 缺 `__main__` guard / repo 外绝对路径 / 哈希链 / 数字矛盾）**全部落在 frozen、verifier 内置、P-G 链、报告正文或仓外件上**——按 §5 边界，一律**只登记不擅动**。故本轮的「修复」落点为**勘误注记 + 新增勘误件**，与委托信 §3 自身的路由（「数字矛盾…以勘误清单随回函提交，PI 另行处置」）一致。

### 3.2 修复前后 SHA-12 对照表

| 类别 | 文件 | 修复前 SHA-12 | 修复后 SHA-12 | 变更 |
|---|---|---|---|---|
| 既有文件 | **全部**（19 REPORT + 16 frozen 在盘项 + repo 内 25 个既有 *.py + `results/` 全部 + `corpus/v20/` 全部） | 见 §3.1 各表 | **同左** | **0 字节改动** |
| 新增件 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | —（不存在） | `48EFD3828D54`（10,026 B） | 新增 |
| 新增件 | `deposon_team/plugins/_v3_review_r1_inventory_2026_09_23.py` | — | `7B97EF02C52E` | 新增（走读脚本） |
| 新增件 | `_v3_review_r1b_2026_09_23.py` | — | `B5E77E114D88` | 新增 |
| 新增件 | `_v3_review_r1c_2026_09_23.py` | — | `FDFEB03E8D6F` | 新增 |
| 新增件 | `_v3_review_r1d_2026_09_23.py` | — | `4ADBD9B5EAB5` | 新增 |
| 新增件 | `_v3_review_r2_verify_2026_09_23.py` | — | `AEE06C009ED1` | 新增 |
| 新增件 | `_v3_review_r2b_2026_09_23.py` | — | `9D6343BD9755` | 新增 |
| 新增件 | `_v3_review_r2c_2026_09_23.py` | — | `1C30CDA5AAD6` | 新增 |
| 新增件 | `_v3_review_r3_sha_2026_09_23.py` | — | `D3B45B64C0DA` | 新增 |
| 新增件 | `_v3_review_r4_fixscan_2026_09_23.py` | — | `917B18EB9A5F` | 新增 |
| 新增件 | `_v3_review_r5_anchor_probe_2026_09_23.py` | — | `7EBE0F65A64A` | 新增（锚件探针，E-15 出证） |
| 新增件 | `_v3_review_r6_final_sha_2026_09_23.py` | — | `8AF3F4460144` | 新增（落盘 SHA 汇总） |
| 新增件 | 本回函 `letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23.md` | — | 见落盘报值 | 新增 |

> **注**：新增 7 个 `_v3_review_r*.py` 为走读用**一次性证据脚本**，不参与任何 V3 结论、不被任何报告引用、不改动 frozen——如 PI 认为不宜留在 `plugins/`，可整体删除而不影响任何结论（删除后 SHA 表相应回落）。

### 3.3 委托信 §3「已知线索」核实结论

| 线索 | 核实结果 | 依据 |
|---|---|---|
| **3 个 BOSS JSON 疑似缺件** | **非真缺件——历史迁移至 `deposon-sub/results/`**：`boss_pa_1_rbr_rm_result`(`C7C59E0D2F6C`, 8,753 B)、`boss_pa_2_potential_game_result`(`5C76137D6430`)、`boss_pc_1_a1_resampling`(`D21912A05D79`) 逐一在盘且 SHA 与历史引值一致 | 实算（R1/R2） |
| **corpus/v19 / v21 / v22 不存在** | **属实**（旧路径名失效）；22 caption 实锚在 `corpus/v20/`：`strip_captions_22.json` + `L_*.json`(6) + `S*.json`(16) 共 23 件在盘 | `LS corpus/v20` |
| **09-16 不改项是否仍悬挂** | ① 4 个 `skill_*` 仍缺 SELF-CHECK 尾块 → **仍悬挂**（frozen，仅报告）；② `_p_k` repo 外绝对路径 → **已不悬挂**（实扫 `repo外绝对路径=no`） | R2c |
| **`boss_pc_*_real_*` 与 `boss_pe_*_real_*`** | **逐字节相同**（`boss_pc_1_real_2d_ising` ≡ `boss_pe_1_real_2d_ising`，余同）→ 命名轴错位，勿重复计为独立实验 | 实算（勘误 §3） |
| **51/60 vs 52/60** | 属实，**同一报告内并存**：51/60 指 dpath 60 cells（V2 阶段 1-3.5），52/60 指 no-RAG 双主线 baseline | V7 L29/L69/L74 vs L70/L85/L236 |
| **8,674 B vs 8,753 B** | 属实：报告记 8,674 B，实为 8,753 B（SHA `C7C59E0D2F6C` 与实算一致） | R2 |

### 3.4 走读**新发现**（超出委托信线索，最高优先）

**E-15 · 5 锚根件锚链断裂（机器可复算）**

- frozen 声明的 5 锚根件 = `verifier/handoff/KT_ABC1_anchors_sha256_12.json`，期望 SHA-12 `03c6c01f3697`（6,680 B）。
- **冻结主路径**在盘件却是**另一件**：11,318 B，SHA-12 `6e9cd8cd8e07`，结构键 `metadata / anchors / boss_baselines`，`metadata.date = 2026-09-09`、`author = "Mavis (root session)"`。
- **冻结 fallback 路径**（`_archive_deposon_2026_09_17/verifier/handoff/`）**无此件**。
- 目标件 `03c6c01f3697` **仅存于未声明的** `〔本地归档区〕\verifier\handoff\KT_ABC1_anchors_sha256_12.json`。
- **后果（实测）**：`python deposon_team/plugins/_verify_15frozen.py` 于 2026-09-23 输出 `TOTAL: 16 frozen files | OK: 15 | FAIL: 1`、`0-touch declaration: FAIL`——**唯一 FAIL 即本项**。
- **意义**：V3/V4 几乎所有报告都写「5 锚 SHA-12 `03c6c01f3697` 未动 / 0 触动」。**在冻结路径上，该文件当前无法被验证**——锚链根件名实不符。这不是本次走读修改所致（本次 0 字节改动），是既有状态。

**E-16 · 派生锚 SHA 位数**：`V3X_1WEEK_KILL_REPORT` L110 写 `da517c1153c`（11 hex）；实算 `da517c115f3c`（12 hex，5,049 B，与 `D5` L136 / `TRAE_3RISK` L45 一致）。

**真缺件 3 件（三处均无）**：`results/deposon_v17_fusion_fix.json`、`deposon_v18_api_supplements.json`、`deposon_v20_baselines.json` —— 在 repo / `_archive_deposon_2026_09_17` / `deposon-sub` **三处实测均不存在**。其中 `deposon_v20_baselines.json` 是 `boss_pa_1` 的直接输入（P-A 证据链上游），**建议优先处置**。

> 以上 E-15/E-16 与真缺件三件的完整登记见 `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` §4/§5（E-1…E-16）。

---

## §4 验证记录

| 项 | 命令 / 方式 | 结果 |
|---|---|---|
| **compile** | `python -B` 实跑全部本次新增脚本（`_v3_review_r1…r6`），解释器逐行编译 | **exit 0 × 7**，无 SyntaxError |
| **import/真执行** | 上述 7 脚本均**真执行**（非静态阅读）：R1 资产盘点、R2 退化复算、R3 SHA 汇总、R4 可修复面扫描、R5 锚件探针、R6 落盘 SHA 汇总 | 全部产出预期输出，`_r1/_r2/_r3/_r4/_r5/_r6 DONE` |
| **退化结论独立复算** | `_v3_review_r2_verify`：`rm_iter` distinct=[6]；`ess_freq` distinct=['0.5']；`is_ess` distinct=['True']；`ess_match` distinct=['False']；`rbr_multiplier` distinct=[1.0,2.0,200.0] | **22/22 全量，非抽样**，与子代理结论一致 |
| **表-JSON 对账** | `P_A_D1_D3_REPORT` L143–147 vs 冻结 JSON | 表（199/1/32）vs JSON（200/6/200）**逐字段不符**，且表值与脚本返回域不相容 |
| **frozen 0 触动自证** | `python -B deposon_team/plugins/_verify_15frozen.py` | `16 frozen files | OK: 15 | FAIL: 1`——**FAIL 项为 E-15（既有断裂，非本次所致）**；其余 15 项（含 4 `skill_*`）SHA-12 与期望逐一相同 |
| **V4 链 0 触动** | 本次全程未读写任何 `_v4_*` 路径；`results/_v4_*` 与 `letters/_v4_*` 未列本次新增/修改 | **0 触动** |
| **密钥** | 本函与全部新增件正文 | **0 明文密钥** |
| **外部依赖** | 本函 | **0 LLM 调用 / 0 外部 URL** |

> **关于 §4 的「frozen 0 触动 = FAIL」**：这不是本次走读造成的失败，而是**本次走读发现的既有事实**（E-15）。我方 0 字节改动可用「新增件之外无任何 SHA 变化」自证（§3.2）。若 PI 需要「16/16 PASS」的绿标，须先解决 E-15（把目标件复位到冻结主路径，或把 frozen fallback 指向 `_non_upload_local_archive`）——此事按 §5 边界不属我可擅动范围。

---

## §5 边界声明

- **不动**：18 frozen（在盘 16 项，含 4 `skill_*`）/ 9 网格 / P-G v0+v01 / plugin spec / verifier 内置脚本（`_verify_15frozen*.py`）/ V4 `_v4_*` 全链 / 已冻结报告正文（19 REPORT）——**均已核查，0 字节改动**。
- **不改**：任何实验结论与判定本体。本函的标注是**对结论-证据关系的再分类**，不重裁命题存亡；「假证伪/假成立」标签**不构成翻案**，仅指出命题**未受审**。
- **不引**：无任何无法核实的外部专有名词 / 文献号 / 法条号。
- **密钥**：本函与全部新增件 0 明文密钥。
- **仓外件**：`deposon-sub/`（363 件）与 `_non_upload_local_archive/` 仅**读取以核 SHA**，未写入、未移出、未删除。
- **新增件**：`docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` + 6 个 `_v3_review_r*.py` + 本回函，均为**新增**，不覆盖任何既有文件。

---

## §6 老实交代

**1. 存疑项（我判不了、需 PI / 第三方裁定的）**

- **BOSS-P-A2 vs KT-B1 的 PG 口径冲突**：同一命题在 P-A 报 3/22、在 KT-B1 报 22/22。两方构造（residual 阈值 / 图集）未对齐，我**无法判定谁对**——只能标「不可判」。这是 V3 内部最大的单点矛盾。
- **E-15 的真实历史**：主路径那件 11,318 B 的 `6e9cd8cd8e07` 是何时、被何操作写入的，我**查不到**（本仓无 `.git`，无法回溯）。我只报告「此刻磁盘状态如此」，不臆测成因。可能与冻结 schema 中记的「2026-09-17 verifier/ 整体挪 + NTFS ACL 阻回写」有关，但**这是推测，未证实**。
- **`03c6c01f3697` 与 `6e9cd8cd8e07` 的语义关系**：两件都叫 `KT_ABC1_anchors_sha256_12.json`，但体量差 4,638 B（6,680 vs 11,318）。前者是否被后者**取代**（而非被覆盖），需 PI 认定——若为取代，则所有「03c6…未动」的表述属**指向已废版**；若为误覆盖，则是一次**冻结资产破损**。**两种解释对 V3/V4 证据链的影响截然不同**，我不代为选择。
- **`_adendum_A` 的检测能力**：该件自记 P-J/P-M/P-C-exp_3_3 三处退化（`unverified`×6、`constant`×5）。它**是否已覆盖 V3 全部退化点**，我**不敢担保**——我只能确认它抓到了这 3 处，不能证明「其余皆不退化」。**「未检出」≠「不存在」**。
- **BOSS-PC-3 的 clip 语义**：`r2_delta_full_minus_clipped`≡0 可能意味着 (a) clip 是 no-op（构造退化），也可能意味着 (b) full 与 clipped 的定义在实现中本就不产生差异（设计意图）。我倾向前者（因 `clip_r2_min=0.7` 明示应有截断），但**未见 P-C 规范对此的预注册定义**，故标假证伪而非「构造无效」。

**2. 未读完项（诚实清单）**

- **`deposon-sub/` 363 件**：我按 09-21 manifest **逐条核了 `dst` 存在性与部分 SHA-12**（MISSING=0），但**未逐件读完内容**。故「仓外件无其他缺陷」**不是我的结论**。
- **`deposon_team/plugins/_p_i/j/k/l/m/n/o` 系列 runner**（在 deposon-sub）：我核了 09-16 修复标记（`and→or`、UNVERIFIED、移除伪造 R²）**是否仍在**，但**未逐行走读全部逻辑**。
- **19 REPORT 中的 REVIEWER_A/B 系（6 份）与 D7 系非 REPORT 文档**：委托清单为「19 份 REPORT」，我按清单执行；`REVIEWER_*`、`D7_*`、`BOSS_B123_BUGFIX`、`SPEC_V0_1_BOSS_SELFTEST` 等**未纳入本次 19 份**——若 PI 认为应扩范围，请另派。
- **`deposon_v2_phase3_strip_embeddings_2026_09_11.json`（≈2.34 MB 单行）**：仅作存在性与关键字段抽读，**未做全量语义解析**。

**3. 0 触动声明**

我声明：本轮走读对**任何既有文件均 0 字节改动**——19 REPORT、16 项在盘 frozen、repo 内 25 个既有 `*.py`、`results/` 全部既有件、`corpus/v20/` 全部件、`deposon-sub/` 全部件、`_v4_*` 全链，**无一被写**。唯三处新增：勘误件 1 件、走读脚本 7 件、本回函 1 件。可由 §3.2 对照表 + `_verify_15frozen.py` 的 15 项 SHA 逐一相符跨证（4 个 `skill_*` 实算 MATCH，见 `_v3_review_r6` 输出）。

**4. 一句话总纲**

V3 的**判死型结论基本可信**（KT-C1 / P-C / v19 / v21 / f5 / 22-caption 构成真证伪资产）；**存活型结论大面积偏强**（P-A 三项 BOSS 中两项常量退化、PE-2 常量化、守恒审计把机器 epsilon 当证据）；**报告层的数字不自洽**（51/52、−0.8000/−0.832、0.8833/0.8667、0.1775/0.1776、TOTAL 15/16）是系统性的，不是孤例；而**最深的一处是 E-15 锚链断裂**——它是 V3/V4「0 触动」叙事的地基，此刻在冻结路径上无法验证。**我已把根因分类清楚，但一个字也没替 PI 改。**

---

*出证：Trae code · 2026-09-23 · 回函 SHA-12 见落盘报值*
*配套勘误件：`docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`*
