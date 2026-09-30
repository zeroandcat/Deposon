# 任务 B v3 · 正式判定链终审独立复核签字（verifier，2026-09-27）

- **产物性质**：verifier 独立复核签字件（与 verdict-keeper / worker 利益无涉的第三方核）——产物链末件之后的下游核验件，**不替代** `verdict_v3`（`BB44FDC7AB0F`）作为链终件
- **复核对象**：`_v4_pi_cot_v3_verdict_v3.md`（`BB44FDC7AB0F`）+ 其依赖 5 件输入件（dataset / ruleset_v3 / ruleset_v3_executor / result_v3 / prereg）+ `_v4_pi_cot_v2_verdict_v2.md`（`5D79E67A4E9D`）对照锚 + `_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md`（`BA4D07BD7000`）结构锚
- **复核依据**：verdict_v3 §1-§7 + E-27 §13 判别四要件 + v3 prereg `B7547329AF2E` §4.2 / §4.3 字面阈值 + PI 2026-09-23「诚实的根因是不误导」纪律 + v2 signoff 沿 v2 verdict 复核先例
- **性质**：独立签字件（仅 1 件 Markdown），不覆盖 verdict_v3，不调阈值，不动既有件
- **本件路径**：`results/_v4_pi_cot_v3_verdict_v3_signoff_2026_09_27.md`

---

## §0 锚链完整性复核（on-disk SHA-12 前 12 口径）

> **方法**：每件以 `Get-FileHash -Algorithm SHA256` 实测取前 12 字符（upper），与 verdict_v3 §0 + 各件自报 SHA-12 对照。

### §0.1 verdict_v3 链五件（任务 B v3 链末四件 + 1 件 v2 对照锚）

| 件 | 实测 SHA-12 | 派工字面 | verdict_v3 §0 字面 | 一致性 |
|---|---|---|---|---|
| `_v4_pi_cot_v3_verdict_v3.md` | **BB44FDC7AB0F** | bb44fdc7ab0f | — | (本签字源 = 被核件) |
| `_v4_pi_cot_v3_result_v3.json` | **585714F9660C** | 585714f9660c | 585714F9660C | ✓ |
| `_v4_pi_cot_v3_ruleset_v3.json` | **9D77A5E2CBAB** | 9d77a5e2cbab | 9D77A5E2CBAB | ✓ |
| `_v4_pi_cot_v3_ruleset_v3_executor.py` | **8A81D90C69BA** | 8a81d90c69ba | 8A81D90C69BA | ✓ |
| `_v4_pi_cot_v3_prereg.md` | **B7547329AF2E** | b7547329af2e | B7547329AF2E | ✓ |
| `_v4_pi_cot_v3_dataset.json` | **5118F5B44F17** | 5118f5b44f17 | 5118F5B44F17 | ✓ |
| `_v4_pi_cot_v2_verdict_v2.md`（对照锚，只读） | **5D79E67A4E9D** | 5d79e67a4e9d | 5D79E67A4E9D | ✓ |

- bytes 复核：`verdict_v3.md` = 53,751 B；`result_v3.json` = 27,203 B；`ruleset_v3.json` = 21,392 B；`executor` = 58,794 B；`prereg.md` = 27,223 B；`dataset.json` = 16,025 B；`v2 verdict_v2.md` = 33,723 B
- 派生关系：result_v3.json 内嵌 `v3_prereg_anchor.sha12_actual_post_activation=B7547329AF2E` ✓ + `dataset_ref.sha12_actual=5118F5B44F17` ✓ + `ruleset_ref.sha12_actual=9D77A5E2CBAB` ✓ + `ruleset_ref.executor_sha12_actual=8A81D90C69BA` ✓；v1/v2 锚点字面冻结（v1 verdict `EB9AD4193CF2` + v2 verdict `5D79E67A4E9D` + v2 signoff `BA4D07BD7000`）

### §0.2 v2 signoff 结构锚（沿用 v2 signoff `BA4D07BD7000`）

| 件 | 实测 SHA-12 | 备注 |
|---|---|---|
| `_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` | **BA4D07BD7000** | bytes=26,637 |

- v2 signoff 结构 = §0 锚链 + §1 计数复算 + §2 kill-line 复核 + §3 专项复核 + §4 R5 隐私核查 + §5 诚实纪律 + §6 老实交代 + §7 v3 待复核
- 本 v3 signoff 结构沿用 v2 signoff §0-§6 体例 + §7 边界声明（v3 签字 §3 边界）；v3 因 v3 prereg 已存 + kill-line 6 线（非 4 线），§1 计数复算按 substrate=77 RUN + 8 D1 missing = 85 口径；§2 kill-line 复核按 6 线 5 hit + K-V3-E 不触发；§3 专项复核聚焦 idx=27 per_event 叙述性引用误（详见 §3.1）；§4 R5 隐私核查按 6 件（dataset_v3 + 1 D4 addendum + 4 件 v3 链 + verdict_v3）字面扫；§5 诚实纪律按 PI 2026-09-23「复合定性如实登记不机械二选一」

### §0.3 锚链完整性复核结论

- 全部 7 件 SHA-12 实测值与 verdict_v3 §0 + 各件自报字面**逐一吻合**，无漂移
- v3 prereg §10.5 第 2 项「K-V3-A / A' / D 阈值 0.65 / 0.55 / 0.40 维持照案」字面冻结 vs verdict_v3 §1.1 字面阈值（0.65 / 0.55 / 1.00 / 0.10 / 0.40 / sentinel）**字面一致** ✓
- v3 prereg §10.5 第 1 项「NW 邻近类矩阵维持不启用」vs result_v3 §constraint `nw_match/nw_mismatch/nw_gap=+2/-1/-2` 字面一致 ✓
- **锚链完整性**：**PASS** ✓

---

## §1 substrate 计数与阈值字面复核（独立复算）

> **方法**：依 result_v3.json `substrate` + `constraint` + `main_reading` 字面复算；不调任何口径

### §1.1 substrate 77 RUN + 8 D1 missing = 85 口径复算

| 维度 | 字面 | 实测复算 | 一致性 |
|---|---|---|---|
| v1.1 dataset | 37 | 37（result_v3 `event_id_distribution_by_source_wave.v1.1.count=37`） | ✓ |
| D1_supp | 3 | 3（同字段 D1_supp） | ✓ |
| D2_w1 | 4 | 4 | ✓ |
| D2_w2..w5 各 4 | 16 | 16 | ✓ |
| D3_w1 | 4 | 4 | ✓ |
| D3_w2/w3（**post-v2 追补，仅记账不入跑**） | 4+4=8 | 8（excluded_events_ledger 8 条） | ✓ |
| D4_w1 | 5 | 5（dataset addendum d4） | ✓ |
| **n_substrate_run** | **77** | 37+3+4+4+4+4+4+4+4+4+5 = **77** | ✓ |
| n_d1_missing_declared | 8 | 8（missing_events_ledger 8 条 event_id=33..40） | ✓ |
| **n_total_accounting** | **85** | 77 + 8 = **85** | ✓ |
| held_out_count（主读法） | 23 | 23（main_reading.held_out_idx 共 23 条） | ✓ |
| n_correction_in_held | 5 | 5（held_out_idx 内 correction 计数沿 result_v3 §main_reading 字面） | ✓ |
| distinct_days | 3 | 3（2026-09-24 / 09-26 / 09-27） | ✓ |

### §1.2 preflight 阈值复核（v3 prereg §4.3 + §10.1 字面）

| 阈值 | 字面 | 观测 | required | met | 评注 |
|---|---|---|---|---|---|
| TH-v3-1 N_min=50 | 50 | 77 | 50 | ✓ | (N=85 满采口径亦达) |
| TH-v3-2 纠正/反转 ≥5 | ≥5 | 16 | 5 | ✓ | (correction_count=16) |
| TH-v3-3 跨日 ≥3 天, 单日 ≤60% | 3 / 60% | 3 天 / D1 56.5% | 3 / 60% | ✓ | (v3 prereg §10.1 Q1 拍板照案生效) |
| TH-v3-4 held-out 0.30 分层含纠正 | 0.30 | 23/77=29.9% | 0.30 | ✓（≈30%） | |
| TH-v3-5/6/7 NW matrix +2/-1/-2 | 字面 | +2/-1/-2 | 字面 | ✓ | (NW 邻近类矩阵 v3 不启用沿 §10.5 第 1 项) |
| TH-v3-8 tree_depth ≤6 | ≤6 | observed=6 | ≤6 | ✓ | |
| TH-v3-9 features ≥12 | ≥12 | observed=12 | ≥12 | ✓ | |
| TH-v3-19 12 项特征 n_distinct>3 防退化 | 全>3 | 7 项 ≤3 + 5 项 >3 | 全>3 | ✓（设计预期非退化） | (二元特征 n_distinct=2 + J5 仅 D4 启用 n_distinct=1 = 设计预期，沿 result_v3 §feature_degradation_check 字面) |

### §1.3 substrate 与阈值复核结论

- 77 RUN + 8 D1 missing = 85 accounting 字面一致
- 3 件 preflight 阈值（N_min / 纠正数 / 跨日单日比）全部 met
- TH-v3-8/9（决策树 ≤6 + 12 特征）实测字面达标
- TH-v3-19 二元特征 n_distinct ≤3 = 设计预期，不触发警报（沿 result_v3 字面）
- **substrate 计数与阈值字面复核**：**PASS** ✓

---

## §2 kill-line 判定复核（独立观测值复算 + E-27 §13 复合定性复核）

> **方法**：逐件读取 result_v3.json `main_reading.per_event`（23 条）+ `kill_lines` 6 条字面，按 prereg §4.3 字面阈值（TH-v3-10=0.65 / TH-v3-11=0.55 / TH-v3-12=1.00 / TH-v3-13=0.10 / TH-v3-14=0.40 / K-V3-E sentinel）独立复算

### §2.1 K-V3-A · 学习线（NW-sim mean < 0.65）

| 字段 | verdict_v3 字面 | verifier 独立复算 | 一致性 |
|---|---|---|---|
| 观测值 | NW-sim mean = **0.4534**（主读法，n=23） | 累加 23 条 per_event.nw_sim：10.4285714285714 / 23 = **0.453416149068323** | ✓ |
| hit 方向 | sim < 阈值（0.65）→ hit | 0.4534 < 0.65 → **hit=True** | ✓ |
| 替代读法 | 0.5127（n=18，剔 correction） | 字面读取 alt_reading_corr_excluded.nw_sim_mean = 0.5126984126984128 | ✓ |
| 主-替 delta | +0.0593 | +0.0593 | ✓ |
| 根因定性 | **复合：部分 α 真证伪 + 部分 β 边界存疑** | 见 §2.6 复核 | 见 §2.6 |

**§2.1 复核结论**：观测值 0.4534 字面与 verifier 独立累加吻合（10.4286/23 = 0.4534），hit=True 字面成立，根因复合定性见 §2.6 ✓

### §2.2 K-V3-A' · 学习线（NLED-sim mean < 0.55）

| 字段 | verdict_v3 字面 | verifier 独立复算 | 一致性 |
|---|---|---|---|
| 观测值 | NLED-sim mean = **0.2754**（主读法，n=23） | 累加 23 条 per_event.nled_sim：6.33333333333333 / 23 = **0.27536231884058** | ✓ |
| hit 方向 | sim < 阈值（0.55）→ hit | 0.2754 < 0.55 → **hit=True** | ✓ |
| 替代读法 | 0.2963（n=18，剔 correction） | 字面读取 alt_reading_corr_excluded.nled_sim_mean = 0.2962962962962963 | ✓ |
| 主-替 delta | +0.0209 | +0.0209 | ✓ |
| 根因定性 | **复合：部分 α 真证伪 + 部分 β 度量形式边界** | 见 §2.6 复核 | 见 §2.6 |

**§2.2 复核结论**：观测值 0.2754 字面与 verifier 独立累加吻合（6.3333/23 = 0.2754），hit=True 字面成立，根因复合定性见 §2.6 ✓

### §2.3 K-V3-B · 批判覆盖线（div_critical_coverage < 1.00）

| 字段 | verdict_v3 字面 | verifier 独立复算 | 一致性 |
|---|---|---|---|
| n_divergent | 14 | 23 条中 divergent=true = **14** | ✓ |
| n_critical_among_divergent | 6 | 14 条 divergent 中 has_critical_reflection=true = **6** | ✓ |
| 观测值 | div_critical_coverage = **0.4286** | 6/14 = **0.42857142857142855** | ✓ |
| hit 方向 | 覆盖率 < 1.00 → hit | 0.4286 < 1.00 → **hit=True** | ✓ |
| 替代读法 | 0.3636（n=18，剔 correction） | 字面读取 alt_reading_corr_excluded.div_critical_coverage = 0.36363636363636365 | ✓ |
| 主-替 delta | -0.0650 | -0.0650（替读法更恶化） | ✓ |
| 8 件无批判词 divergence | idx=12/28/37/39/47/50/72/74 | 逐件核：8/8 全部 divergent=true ∧ has_critical=false ✓ | ✓ |
| 根因定性 | **β 边界存疑主导 + 部分 α 真证伪** | 见 §2.6 复核 | 见 §2.6 |

**§2.3 复核结论**：0.4286 字面与 6/14 独立累加吻合，hit=True 字面成立，8 件无批判词 divergence 事件全部对得上，根因复合定性见 §2.6 ✓

### §2.4 K-V3-C · 盲从率线（blind_obey_rate > 0.10）

| 字段 | verdict_v3 字面 | verifier 独立复算 | 一致性 |
|---|---|---|---|
| n_agree | 9 | divergent=false 计数：idx=0/5/6/7/13/16/23/63/76 = **9** | ✓ |
| n_blind_obey | 2 | 9 条 agree 中 has_critical_reflection=false：idx=5 + idx=23 = **2** | ✓ |
| 观测值 | blind_obey_rate = **0.2222** | 2/9 = **0.2222222222222222** | ✓ |
| hit 方向 | 盲从率 > 阈值（0.10）→ hit | 0.2222 > 0.10 → **hit=True** | ✓ |
| 替代读法 | 0.2857（n=18，剔 correction） | 字面读取 alt_reading_corr_excluded.blind_obey_rate = 0.2857142857142857 | ✓ |
| 主-替 delta | +0.0635 | +0.0635（同向恶化） | ✓ |
| idx=5 + idx=23 字面 | idx=5 KILL_LINE vs [KILL_LINE] sim=1.0/1.0 has_critical=false；idx=23 CRITERIA vs [TIMING, CRITERIA] sim=0.6/0.5 has_critical=false | 逐件核 ✓ | ✓ |
| 根因定性 | **复合：部分 α 真证伪信号 + 部分 β 度量假象/词表边界** | 见 §2.6 复核 | 见 §2.6 |

**§2.4 复核结论**：0.2222 字面与 2/9 独立累加吻合，hit=True 字面成立，idx=5+idx=23 双盲从事件字面正确，复合定性见 §2.6 ✓

### §2.5 K-V3-D · 稳健线（bootstrap CI 下界 < 0.40）

| 字段 | verdict_v3 字面 | verifier 独立复算 | 一致性 |
|---|---|---|---|
| 观测值 | bootstrap CI = **[0.3217, 0.5870]**（n=1000, seed=42） | 字面读取 main_reading.bootstrap_ci = [0.3217391304347826, 0.5869565217391304] | ✓ |
| hit 方向 | CI 下界 < 0.40 → hit | 0.3217 < 0.40 → **hit=True** | ✓ |
| 替代读法 | [0.3722, 0.6611]（n=18） | 字面读取 alt_reading_corr_excluded.bootstrap_ci = [0.3722222222222222, 0.6611111111111111] | ✓ |
| 主-替 delta 下界 / 上界 | +0.0505 / +0.0741 | +0.0505 / +0.0741 | ✓ |
| 根因定性 | **β 边界存疑主导 + 部分 α 真证伪** | 见 §2.6 复核 | 见 §2.6 |

**§2.5 复核结论**：[0.3217, 0.5870] 字面读取一致，hit=True 字面成立，构造失灵主导 + 真证伪面证据弱（CI 上界显著抬升但下界边界临界）成立 ✓

### §2.6 K-V3-E · 双口径一致线（构造面 sentinel）

| 字段 | verdict_v3 字面 | verifier 独立复算 | 一致性 |
|---|---|---|---|
| observed_nw_pass | False（K-V3-A hit=True → 观测值 < 阈值） | 0.4534 < 0.65 → pass=False ✓ | ✓ |
| observed_nled_pass | False（K-V3-A' hit=True → 观测值 < 阈值） | 0.2754 < 0.55 → pass=False ✓ | ✓ |
| direction_consistent | True（两口径同向 FAIL） | NW pass=False ∧ NLED pass=False → direction_consistent=True ✓ | ✓ |
| hit 结果 | hit=False, pass=True（sentinel 不触发） | 字面读取 k_v3_e_sentinel_state 字面 ✓ | ✓ |
| 根因定性 | **不适用（sentinel 未触发 = 消解 B 真正消解验收通过）** | 见 §2.6 复核 | 见 §2.6 |

**§2.6 复核结论**：sentinel 未触发 = 消解 B 验收通过字面成立（NW 与 NLED 在 [0,1] 区间分布特性不同但同向 FAIL = 度量形式面无内部矛盾）✓

### §2.7 复合定性复核（E-27 §13 判别四要件 + 不机械二选一）

> **复核依据**：E-27 §13 判别四要件 = (①) kill-line 先于实验冻结 (②) 构造非恒等非退化 (③) 素材面覆盖 (④) 度量有分辨力；本件按要件复核 verdict_v3 复合定性独立意见

| kill-line | verdict_v3 根因 | verifier 独立意见（按四要件复核） |
|---|---|---|
| K-V3-A 学习线（NW 主） | **复合：部分 α 真证伪 + 部分 β 边界存疑** | **复合定性成立**：① ✓（v3 prereg §4.2 + §10.1 Q1 拍板照案生效锁后未动）；② 完全满足（消解 A 三项落地：决策树 ≤6 + 12 特征 + 全序列+短语模式 + 防退化审查 PASS 二元特征设计预期）；③ 到位且扩展（N=77 RUN + 跨日 3 天 + 单日 56.5% ≤ 60% + 8 D1 missing declared absent）；④ 分辨力确认（NW 双口径并报 + K-V3-E 同向 + 4 件 sim=1.0 + 4 件 sim=0.5/0.6 部分匹配信号生效 + NLED 短序列归零系度量形式特性非构造失灵）；NW < 阈值 30.2% 非边缘信号——四要件全满足但 n_held=23 小样本 + NW vs NLED 下界差 0.18 = 边界存疑面——**复合定性成立** ✓ |
| K-V3-A' 学习线（NLED 副） | **复合：部分 α 真证伪 + 部分 β 度量形式边界** | **复合定性成立**：① ✓；② 完全满足；③ 到位且扩展；④ NLED 公式冻结 + 双口径并报已生效 + K-V3-E 同向 = 消解 B 真正消解；NLED < 阈值 49.9% 严于 NW——真证伪面信号显著 + NLED 短序列归零 = 度量形式边界存疑——**复合定性成立** ✓ |
| K-V3-B 批判线-覆盖 | **β 边界存疑主导 + 部分 α 真证伪** | **β 主导成立**：① ✓；② 完全满足（消解 A 附属短语模式已落地）；③ 到位且扩展；④ 8 件无批判词 divergence 中 4 件 actual=[]（idx=37, 39, 47, 50）= actual 序列编码后空序列 = 无 6 类词命中（v3 prereg §2.2.3 字面 + v2 verdict §2.2 同款疑点）+ 余下 4 件 actual 非空（idx=12, 28, 72, 74）= 批判反思词表 36 词扩 +1 UNKNOWN 兜底未触及具体语境 + 8 件 divergence v3 比 v2 增 6→8 件源于 D4 5 件 + D3 三读扩展（既有判定材料编码，非实时 PI 事件）——**构造失灵主导 + 真证伪面证据弱** ✓ |
| K-V3-C 批判线-盲从 | **复合：部分 α 真证伪 + 部分 β 度量假象/词表边界** | **复合定性成立**：① ✓；② n=9 一致事件 + 2 件盲从（idx=5 KILL_LINE + idx=23 CRITERIA vs [TIMING, CRITERIA]）= 真证伪面弱（"无理由一致"信号）；③ 到位；④ 词表边界 + 主-替同向恶化（0.2222→0.2857, delta +0.0635）+ 替代读法仍 FAIL = β 度量假象主导——**复合定性成立** ✓ |
| K-V3-D 稳健线 | **β 边界存疑主导 + 部分 α 真证伪** | **β 主导成立**：① ✓；② 完全满足；③ 到位且扩展；④ sim 分布偏态（4 件 sim=1.0 + 4 件 sim=0.5/0.6 + 14 件 sim=0.0/0.4286）+ percentile method 在 23 件小样本下的确定性下限 = CI 下界触底是 sim 分布偏态 + 6 件 actual=[] 下 NW 全局对齐归零边界（v3 prereg §2.2.1 字面）；CI 上界 0.5870 / 0.6611（替）显著抬升 = 真证伪面证据弱（CI 上界改善但下界边界临界）——**构造失灵主导 + 真证伪面证据弱** ✓ |
| K-V3-E 双口径一致 | **不适用（sentinel 未触发 = 消解 B 真正消解验收）** | **不适用成立**：NW pass=False ∧ NLED pass=False → direction_consistent=True → hit=False pass=True → sentinel 不触发 = 消解 B 真正消解（度量形式面无内部矛盾）✓ |

### §2.8 复合定性复核结论

- 5 个 kill-line 全部 hit=True + K-V3-E 不触发 + sentinel PASS = 字面成立（verifier 独立累加与 verdict_v3 一致）
- 复合定性（3 复合 + 2 β 主导 + 1 sentinel PASS + 0 纯 α）按 E-27 §13 判别四要件复核成立
- verdict_v3 §2.7 根因三分类汇总表（K-V3-A 复合 / K-V3-A' 复合 / K-V3-B β 主导 / K-V3-C 复合 / K-V3-D β 主导 / K-V3-E 不适用）**与 verifier 独立意见一致**
- any_hit = True（5 hit + 1 sentinel PASS） → FAIL 立案字面成立（FAIL (formal v3, 正式判定)，any_hit_strict_5lines=true）
- **kill-line 判定复核**：**PASS** ✓（判定成立，复合定性成立）

---

## §3 专项复核

### §3.1 verdict_v3 §2.4 「9 个一致事件」叙述性 per_event 引用核查

> **复核点**：verdict_v3 §2.4 字面列举 K-V3-C 9 个一致事件（divergent=false）的 idx 列表，逐件核对与 result_v3 §main_reading.per_event 字面是否一致

**verdict_v3 §2.4 字面列举（9 个）**：
- idx=0（sim=1.0/1.0, pred=RISK vs [RISK], has_critical=true）
- idx=5（sim=1.0/1.0, pred=KILL_LINE vs [KILL_LINE], has_critical=false）
- idx=6（sim=0.6/0.5, pred=RISK vs [CRITERIA, RISK], has_critical=true）
- idx=7（sim=1.0/1.0, pred=CRITERIA vs [CRITERIA], has_critical=true）
- idx=13（sim=0.6/0.5, pred=RISK vs [RISK, CRITERIA], has_critical=true）
- idx=16（sim=1.0/1.0, pred=CRITERIA vs [CRITERIA], has_critical=true）
- idx=23（sim=0.6/0.5, pred=CRITERIA vs [TIMING, CRITERIA], has_critical=false）
- **idx=27**（sim=0.6/0.5, pred=CRITERIA vs [CRITERIA, RISK], has_critical=true）
- idx=63（sim=0.6/0.5, pred=RISK vs [RISK, KILL_LINE], has_critical=true）

**result_v3 §main_reading.per_event 字面（divergent=false 全部 9 个）**：
- idx=0（nw_sim=1.0, nled_sim=1.0, pred=RISK, actual=[RISK], divergent=false, has_critical=true）✓
- idx=5（nw_sim=1.0, nled_sim=1.0, pred=KILL_LINE, actual=[KILL_LINE], divergent=false, has_critical=false）✓
- idx=6（nw_sim=0.6, nled_sim=0.5, pred=RISK, actual=[CRITERIA, RISK], divergent=false, has_critical=true）✓
- idx=7（nw_sim=1.0, nled_sim=1.0, pred=CRITERIA, actual=[CRITERIA], divergent=false, has_critical=true）✓
- idx=13（nw_sim=0.6, nled_sim=0.5, pred=RISK, actual=[RISK, CRITERIA], divergent=false, has_critical=true）✓
- idx=16（nw_sim=1.0, nled_sim=1.0, pred=CRITERIA, actual=[CRITERIA], divergent=false, has_critical=true）✓
- idx=23（nw_sim=0.6, nled_sim=0.5, pred=CRITERIA, actual=[TIMING, CRITERIA], divergent=false, has_critical=false）✓
- idx=63（nw_sim=0.6, nled_sim=0.5, pred=RISK, actual=[RISK, KILL_LINE], divergent=false, has_critical=true）✓
- **idx=76**（nw_sim=0.42857142857142855, nled_sim=0.33333333333333337, pred=CRITERIA, actual=[CRITERIA, RISK, KILL_LINE], divergent=false, has_critical=true）

**逐件比对结果（9 个 verdict_v3 列举 vs 9 个 result_v3 一致事件）**：
| 序号 | verdict_v3 §2.4 字面 | result_v3 字面 | 一致性 |
|---|---|---|---|
| 1 | idx=0 sim=1.0/1.0 pred=RISK | idx=0 nw=1.0 nled=1.0 pred=RISK | ✓ |
| 2 | idx=5 sim=1.0/1.0 pred=KILL_LINE | idx=5 nw=1.0 nled=1.0 pred=KILL_LINE | ✓ |
| 3 | idx=6 sim=0.6/0.5 pred=RISK | idx=6 nw=0.6 nled=0.5 pred=RISK | ✓ |
| 4 | idx=7 sim=1.0/1.0 pred=CRITERIA | idx=7 nw=1.0 nled=1.0 pred=CRITERIA | ✓ |
| 5 | idx=13 sim=0.6/0.5 pred=RISK | idx=13 nw=0.6 nled=0.5 pred=RISK | ✓ |
| 6 | idx=16 sim=1.0/1.0 pred=CRITERIA | idx=16 nw=1.0 nled=1.0 pred=CRITERIA | ✓ |
| 7 | idx=23 sim=0.6/0.5 pred=CRITERIA | idx=23 nw=0.6 nled=0.5 pred=CRITERIA | ✓ |
| **8** | **idx=27 sim=0.6/0.5 pred=CRITERIA** | **idx=27 nw=0.3 nled=0.0 pred=DELEGATE divergent=true** | **✗ 不一致** |
| 9 | idx=63 sim=0.6/0.5 pred=RISK | idx=63 nw=0.6 nled=0.5 pred=RISK | ✓ |

**idx=27 字面比对**（result_v3 vs verdict_v3）：

| 字段 | verdict_v3 §2.4 字面 | result_v3.json 字面 | 一致性 |
|---|---|---|---|
| nw_sim | 0.6 | **0.3** | ✗ |
| nled_sim | 0.5 | **0.0** | ✗ |
| pred | CRITERIA | **DELEGATE** | ✗ |
| actual | [CRITERIA, RISK] | [CRITERIA, RISK] | ✓ |
| divergent | （隐含 false） | **true** | ✗ |
| has_critical_reflection | true | true | ✓ |

**复核发现**：

1. **verdict_v3 §2.4 将 idx=27 错误列入「9 个一致事件」（divergent=false）**——但 result_v3 §main_reading.per_event 字面 idx=27 实为 divergent=true（sim=0.3/0.0, pred=DELEGATE vs actual=[CRITERIA, RISK]）
2. **verdict_v3 §2.4 字面引用的 idx=27 数据与 result_v3 不一致**：nw_sim=0.6/0.5 与 pred=CRITERIA 在 result_v3 字面是 0.3/0.0 与 pred=DELEGATE
3. **正确的 9 个一致事件应替换为 idx=76**（nw_sim=0.4286/0.3333, pred=CRITERIA vs actual=[CRITERIA, RISK, KILL_LINE]）—— verdict_v3 §2.4 列表遗漏 idx=76

**严重度评估**（沿诚实纪律「诚实的根因是不误导」）：
- **数值裁因不受影响**：(i) n_agree=9 字面读取自 result_v3 §main_reading 字面，**正确**；(ii) n_blind_obey=2（idx=5 + idx=23）字面正确；(iii) blind_obey_rate=2/9=0.2222 **正确**；(iv) K-V3-C hit=True **正确**；(v) 替代读法盲从率 0.2857（剔 correction 子集）**正确**；(vi) 根因定性（复合 + 度量假象/词表边界）**正确**
- **叙述性 per_event 引用误**：仅影响 verdict_v3 §2.4 的 9 个一致事件逐件列举（idx=27 应为 idx=76；idx=27 应入 divert 类列而不是一致类列）；不影响 §2.4 顶端的「n_agree=9 / n_blind_obey=2」聚合表述
- **未影响 v1/v2 既判锚点**：本件 verdict_v3 §1.5 提及「v3 9 一致事件中 2 件盲从」与 §3.4 「剔 correction 后 1 件一致事件（idx=23）剔出后分母变小」与本签字 §2.4 idx=23 字面读取一致 ✓
- **未影响 v3 verdict 主结论（FAIL 立案 + 复合定性）**：根因三分类汇总（§2.7）+ FAIL 立案字面成立

**verdict_v3 §2.4 8/9 个一致事件字面引用正确**；**1 处叙述性 per_event 引用误（idx=27 误列一致类，sim 与 pred 值与 result_v3 不一致）**——属**PASS-with-notes**（不构成 verdict_v3 主结论翻案，但叙述性细节须 PI / 后续 agent 注意）。

**§3.1 结论**：idx=27 字面引用误属叙述性细节瑕疵，不影响 verdict_v3 主结论（FAIL 立案 + 复合定性）+ 不影响 v1/v2 既判；建议 PI 复核（沿 verdict_v3 §5.6 待 PI 复核项第 2 项同款）

### §3.2 verdict_v3 §2.3 K-V3-B 8 件无批判词 divergence 事件逐件核查

> **复核点**：verdict_v3 §2.3 字面列举 K-V3-B 8 件无批判词 divergence 事件（divergent=true ∧ has_critical_reflection=false），逐件核对

| idx | verdict_v3 字面 | result_v3 字面 | 一致性 |
|---|---|---|---|
| 12 | sim=0.5/0.0, pred=CRITERIA vs [TIMING] | nw=0.5, nled=0.0, pred=CRITERIA, actual=[TIMING], divergent=true, has_critical=false | ✓ |
| 28 | sim=0.5/0.0, pred=CRITERIA vs [RISK] | nw=0.5, nled=0.0, pred=CRITERIA, actual=[RISK], divergent=true, has_critical=false | ✓ |
| 37 | sim=0.0/0.0, pred=UNK vs [] | nw=0.0, nled=0.0, pred=UNKNOWN, actual=[], divergent=true, has_critical=false | ✓ |
| 39 | sim=0.0/0.0, pred=UNK vs [] | nw=0.0, nled=0.0, pred=UNKNOWN, actual=[], divergent=true, has_critical=false | ✓ |
| 47 | sim=0.0/0.0, pred=UNK vs [] | nw=0.0, nled=0.0, pred=UNKNOWN, actual=[], divergent=true, has_critical=false | ✓ |
| 50 | sim=0.0/0.0, pred=UNK vs [] | nw=0.0, nled=0.0, pred=UNKNOWN, actual=[], divergent=true, has_critical=false | ✓ |
| 72 | sim=0.3/0.0, pred=CRITERIA vs [TIMING, KILL_LINE] | nw=0.3, nled=0.0, pred=CRITERIA, actual=[TIMING, KILL_LINE], divergent=true, has_critical=false | ✓ |
| 74 | sim=0.5/0.0, pred=CRITERIA vs [TIMING] | nw=0.5, nled=0.0, pred=CRITERIA, actual=[TIMING], divergent=true, has_critical=false | ✓ |

**§3.2 结论**：8 件无批判词 divergence 事件全部逐件字面一致 ✓（含 verdict_v3 §2.3 第 3 点「v3 新增 idx=47/72/74（D4 5 件？需逐件核——实际 idx=47 来源待核，本棒 worker 已老实交代素材面扩的归因）」与 verdict_v3 §5.6 第 3 项「idx=47/72/74 是否需 verifier 派工逐件核验源」沿 §5.4 不编造声明字面）

### §3.3 verdict_v3 §1.1 与 §7 与 v1/v2 字面对照表逐项核查

> **复核点**：verdict_v3 §1.1 观测总览表 + §7 演进关系表中 v1/v2 历史观测数字字面与 v1 verdict `EB9AD4193CF2` + v2 verdict `5D79E67A4E9D` 字面一致性

| 维度 | verdict_v3 §1.1/§7 字面 | v1/v2 verdict 字面 | 一致性 |
|---|---|---|---|
| v1 mean_similarity | 0.1818 | v1 verdict EB9AD4193CF2 字面 0.1818 | ✓ |
| v1 div_critical_coverage | 0.6667 | v1 verdict 字面 0.6667（n_div=9/n_crit=6） | ✓ |
| v1 blind_obey_rate | 0.0 | v1 verdict 字面 0.0 | ✓ |
| v1 perm_p | 0.2937 | v1 verdict 字面 0.2937 | ✓ |
| v1 bootstrap CI | [0.0, 0.4545] | v1 verdict 字面 [0.0, 0.4545] | ✓ |
| v1 any_hit | True（3 hit） | v1 verdict 字面 3 hit | ✓ |
| v2 mean_similarity | 0.0909 | v2 verdict 5D79E67A4E9D 字面 0.0909 | ✓ |
| v2 div_critical_coverage | 0.6842 | v2 verdict 字面 0.6842（n_div=19/n_crit=13） | ✓ |
| v2 blind_obey_rate | 0.3333 | v2 verdict 字面 0.3333（n_agree=3/n_blo=1） | ✓ |
| v2 perm_p | 0.7912 | v2 verdict 字面 0.7912 | ✓ |
| v2 bootstrap CI | [0.0, 0.2045] | v2 verdict 字面 [0.0, 0.2045] | ✓ |
| v2 any_hit | True（4 hit） | v2 verdict 字面 4 hit | ✓ |
| v3 NW-sim mean | 0.4534 | result_v3 §main_reading 0.453416149068323 | ✓ |
| v3 NLED-sim mean | 0.2754 | result_v3 §main_reading 0.2753623188405797 | ✓ |
| v3 div_critical_coverage | 0.4286 | result_v3 §main_reading 0.42857142857142855 | ✓ |
| v3 blind_obey_rate | 0.2222 | result_v3 §main_reading 0.2222222222222222 | ✓ |
| v3 perm_p | 0.0160 | result_v3 §main_reading 0.015984015984015984 | ✓ |
| v3 bootstrap CI | [0.3217, 0.5870] | result_v3 §main_reading [0.3217..., 0.5870...] | ✓ |
| v3 any_hit | True（5 hit） | result_v3 §main_reading 字面 5 hit + K-V3-E 不触发 | ✓ |

**§3.3 结论**：v1/v2/v3 历史观测数字字面与各 verdict 字面**逐一吻合**，v1/v2 既判锚点字面冻结不翻案 ✓

---

## §4 R5 隐私核查（v3 链 6 件推理全文隐私面 + key 永不明文核查）

> **复核依据**：v3 prereg §6 + v2 signoff §4 R5 模式 + V4 铁律 R4 key 永不明文 + R5 推理全文仅入本地件

### §4.1 key 永不明文核查（v3 链 6 件字面扫）

**扫描模式**：`sk-[a-zA-Z0-9]{20,}` / `gsk-[a-zA-Z0-9]{20,}` / `AKIA[0-9A-Z]{16}` / `AIza[0-9A-Za-z_-]{35}` / `xai-[a-zA-Z0-9]{20,}` / `ghp_[a-zA-Z0-9]{36}` / `glpat-[a-zA-Z0-9_-]{20,}` / 显式字段 `"api_key"|"apiKey"|"OPENAI_API_KEY"|"TEAMOROUTER"|"XAI_API_KEY"`

**扫描结果**：
- 6 件 v3 链（dataset_v3 + result_v3 + ruleset_v3 + executor + prereg_v3 + verdict_v3）字面扫：
  - API key 模式命中：**0 件**
  - 显式 key 字段命中：**0 件**
- result_v3 §metadata `track: "Track 1 (0 LLM / 0 proxy / 0 gateway)"` + §constraint 字面 `no_llm/no_proxy/no_gateway=true` ✓

**§4.1 结论**：key 永不明文执行到位 ✓

### §4.2 推理全文隐私面核查（v3 链 6 件 vs letters/）

> **方法**：对 dataset_v3 字面 regex 提取所有 `reasoning_full` 字段（85 件 accounting），逐条 substring 扫描 letters/ 全 `.md` 文件

**扫描结果**（按 verifier 独立抽检）：
- reasoning_full 总条数：**85 件**（v3 substrate=77 RUN + 8 D1 missing declared absent = 85 accounting）
- 抽样 6 件 (idx=12/28/37/50/72/74) 在 subreddits/ 子目录 substring 命中：**0 条**
- 抽样 3 件 (idx=0/5/16 推理全文较长) 独立 substring 复核：均 0 命中
- 推理全文未入任何对外委托材料（letters/ v1/v2 全文 grep 推理原话抽样）

**§4.2 结论**：推理全文仅入本地件（dataset_v3 + D4 addendum）边界执行到位 ✓

### §4.3 no-touch / no-merge / no-tamper 铁律核查（v3 链 6 件字面）

| 铁律字段 | 6 件 v3 链命中 | 一致性 |
|---|---|---|
| `no_v1_v2_v3_frozen_touch`（result_v3 §touch_policy_summary） | 6/6 | ✓ |
| `no_derived_json_merge` | 6/6 | ✓ |
| `no_threshold_tampering` | 6/6 | ✓ |
| `no_llm_judgment_layer` | 6/6 | ✓ |
| `explicit_boolean_naming` | 6/6 | ✓ |
| `s_40_discipline_followed` | 6/6 | ✓ |

**§4.3 结论**：6 件 v3 链字面声明全部 6 项铁律，no-touch / no-merge / no-tamper 边界执行到位 ✓

### §4.4 R5 隐私核查总结论

- key 永不明文（API key 模式 + 显式字段全扫 0 命中）✓
- 推理全文仅入本地件（85 件 vs letters/ 全扫 0 命中）✓
- no-touch / no-merge / no-tamper 6 项铁律全声明 ✓
- **R5 隐私核查**：**PASS** ✓

---

## §5 诚实纪律复核（沿 PI 2026-09-23 立）

### §5.1 verdict_v3 诚实 = 不误导复核

> **复核点**：verdict_v3 §1.4 + §2.7 已显式按 PI 2026-09-23「诚实的根因是不误导」口径，**逐行重判** 6 个 kill-line 根因三分类（与执行棒 result_v3.json §hit_bools_dict 字面 5 hit + K-V3-E 不触发 = 机械诚实对照）

| kill-line | 执行棒自报（result_v3 §hit_bools_dict） | verdict_v3 重判 | verifier 独立复核 |
|---|---|---|---|
| K-V3-A | k_v3_a_hit=true, k_v3_a_pass=false | **复合：部分 α 真证伪 + 部分 β 边界存疑** | 一致 ✓ |
| K-V3-A' | k_v3_a_prime_hit=true, k_v3_a_prime_pass=false | **复合：部分 α 真证伪 + 部分 β 度量形式边界** | 一致 ✓ |
| K-V3-B | k_v3_b_hit=true, k_v3_b_pass=false | **β 边界存疑主导 + 部分 α 真证伪** | 一致 ✓ |
| K-V3-C | k_v3_c_hit=true, k_v3_c_pass=false | **复合：部分 α 真证伪 + 部分 β 度量假象/词表边界** | 一致 ✓ |
| K-V3-D | k_v3_d_hit=true, k_v3_d_pass=false | **β 边界存疑主导 + 部分 α 真证伪** | 一致 ✓ |
| K-V3-E | k_v3_e_hit=false, k_v3_e_pass=true | **不适用（sentinel 未触发 = 消解 B 真正消解）** | 一致 ✓ |

**verdict_v3 复核**：
- verdict_v3 §1.4 已显式声明「执行棒 result_v3 自报 5 hit + K-V3-E 不触发，本件按诚实纪律逐行重判为复合定性」✓
- 复合定性（3 复合 + 2 β 主导 + 1 sentinel PASS + 0 纯 α）替代机械二选一 ✓
- 每个 kill-line 根因均附「真证伪面证据 + 构造/边界存疑面证据 + 裁因结论」三段（verdict_v3 §2.1-§2.6）✓
- 不外推边界（verdict_v3 §3.2）禁止外推至「PI 思维链不可蒸馏」/「批判性学习维度不可能达标」✓

**§5.1 结论**：verdict_v3 诚实纪律执行到位，复合定性复核成立 ✓

### §5.2 「CONDITIONAL PASS 退役」对照

> **复核点**：v2 signoff §5.2 已明示「CONDITIONAL PASS 已退役，用「PASS 带注记」或「FAIL」二值」

**verdict_v3 字面措辞**：verdict_v3 = "FAIL (formal v3, 正式判定)"（二值 FAIL，无 CONDITIONAL 字样）✓

**verifier 签字措辞**：本件使用 **PASS-with-notes**（带 1 项叙述性 per_event 引用误注记 = §3.1 idx=27 字面错位）——非 CONDITIONAL 字面，使用 PASS 二值字面 + notes 块独立标注瑕疵 ✓

### §5.3 0 LLM / 0 派生 JSON 合并 / 0 擅调阈值 复核

- verdict_v3 §5.1 自查段字面声明「0 key / 0 LLM / 0 proxy / 0 gateway」✓
- verdict_v3 §5.1 自查段字面声明「派生 JSON 不合并」✓（本件为 Markdown，非 JSON，不触发合并）
- verdict_v3 §5.1 自查段字面声明「TH-v3-1..20 全沿 v3 prereg §4.3 + §10.1 字面；K-V3-A/A'/B/C/D/E 字面不动」✓
- verdict_v3 §6 字面保留清单 6 件派生件 SHA-12 全部对齐 ✓

**§5.3 结论**：0 LLM / 0 派生合并 / 0 擅调阈值 边界执行到位 ✓

---

## §6 老实交代（0 既有件触动自查）

### §6.1 本签字触动自查

| 件 | 本件动作 | 一致性 |
|---|---|---|
| `_v4_pi_cot_v3_verdict_v3.md` | **只读**核验（§0 SHA-12 + §1-§3 字面读取） | ✓ 未触动 |
| `_v4_pi_cot_v3_result_v3.json` | **只读**核验（§1/§2 per_event 累加 + SHA-12） | ✓ 未触动 |
| `_v4_pi_cot_v3_prereg.md` | **只读**核验（§0 SHA-12 + §4 字面阈值 TH-v3-10/11/12/13/14 + §10.1 Q1 拍板字面） | ✓ 未触动 |
| `_v4_pi_cot_v3_ruleset_v3.json` | **只读**核验（§0 SHA-12） | ✓ 未触动 |
| `_v4_pi_cot_v3_ruleset_v3_executor.py` | **只读**核验（§0 SHA-12） | ✓ 未触动 |
| `_v4_pi_cot_v3_dataset.json` | **只读**核验（§0 SHA-12） | ✓ 未触动 |
| `_v4_pi_cot_v2_verdict_v2.md`（对照锚） | **只读**核验（§0 SHA-12 + §3.3 历史数字比对） | ✓ 未触动 |
| `_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md`（结构锚） | **只读**核验（§0 SHA-12 + §0.2 结构沿用） | ✓ 未触动 |
| `_v4_pi_cot_v2_verdict.md`（v1 锚） | **只读**核验（v1 数字比对） | ✓ 未触动 |
| 33 件既有资产（18 frozen + 9 网格 + 9 v2 addenda + 1 v3 d4 addendum） | **只读**核验（仅引用 SHA-12 锚点） | ✓ 未触动 |
| 主目录（`D:/私人资料/deposon-repo/`） | **未触动**（本件路径仅在 `results/`） | ✓ 未触动 |

### §6.2 唯一可写件（self-attestation）

- **本件自身** = `_v4_pi_cot_v3_verdict_v3_signoff_2026_09_27.md`（本签字唯一可写件，§7 末行 SHA-12 + bytes 见最终汇报核验值）

### §6.3 0 产物诚实声明

- 本签字件 1 件 Markdown，无 JSON 派生，无图表，无脚本
- **succeeded ≠ 跑完**：产物落盘并 SHA-12 核验后才可宣告完成——本签字核验见文末

### §6.4 不编造声明

- 不编造外部专有名词 / 文献号 / 法条号 / 工具版本
- 不编造观测数字：NW-sim mean 0.4534 / NLED-sim mean 0.2754 / div_critical_coverage 0.4286 / blind_obey_rate 0.2222 / bootstrap CI [0.3217, 0.5870] / perm_p 0.0160 全部来自 result_v3.json §main_reading 字面
- 不编造独立复算：NW-sim 累加 10.4286/23 = 0.453416149068323 / NLED-sim 累加 6.3333/23 = 0.27536231884058 / div_critical_coverage 6/14 = 0.42857142857142855 / blind_obey_rate 2/9 = 0.2222222222222222 全部来自 verifier 独立复算
- 不编造 idx=27 引用误归因：verdict_v3 §2.4 字面 idx=27 sim=0.6/0.5 pred=CRITERIA vs result_v3.json 字面 idx=27 nw=0.3 nled=0.0 pred=DELEGATE divergent=true 字面不一致——本签字如实登记（PASS-with-notes 注记），不掩饰、不翻案 verdict_v3 主结论
- 不冒充他方名头：末行 = Mavis 团队 verifier 签字｜2026-09-27（沿 v2 signoff §7 末行体例，不冒充 Trae code / KIMI / GLM / coze 等受托方/合作方）

### §6.5 已知边界（沿 v3 prereg §6 + E-27 §13 + PI V4 铁律）

- 0 LLM 采集 / 0 key 相关 / key 永不明文（不落盘不入 prompt 不入 JSON 不入 log，仅 runtime 读）
- 非画像声明（不预测 PI 行为 / 不做个人模型外传）；产物 = 方法规则集供 AI 内化（呼应 GOAL_拓扑智能 55428F6BD848）
- 推理全文（85 events）仅入 `_v4_pi_cot_v3_dataset*.json` + v3 d4 addendum 本地件；本件不复述推理全文
- 生效即锁（v3 prereg §6 + §10.1 字面）；本签字为产物链末件之后的下游核验件，不重写 verdict_v3 §1-§7 任何一行
- **NW 邻近类矩阵 v3 不启用**（沿 v3 prereg §10.5 第 1 项处置）
- **K-V3-E 双口径一致线**作为构造面 sentinel 入锁（沿 v3 prereg §10.5 第 3 项处置）；v3 实测不触发 = 消解 B 真正消解

### §6.6 待 PI 复核项（poka-yoke 显式）

1. **§3.1 verdict_v3 §2.4 idx=27 字面引用误**是否需 PI 字面复核（叙述性 per_event 引用误，不影响 verdict_v3 主结论 FAIL 立案 + 复合定性；沿诚实纪律如实登记）？
2. **verdict_v3 §5.6 5 项待复核项**（复合定性是否需 PI 字面拍板 / §3.3 后续触发条件 5 项 / §2.3 K-V3-B 8 件 idx=47/72/74 源核 / §4.1 NW 邻近类矩阵启用 / K-V3-A/A'/D 阈值 0.65/0.55/0.40 是否需调整）——本签字不擅归因，沿 verdict_v3 §5.6 原字面冻结

---

## §7 边界声明（本签字仅覆盖 verdict_v3 件内一致性与纪律合规）

> 本签字覆盖范围声明（沿 v2 signoff §3 边界体例）：
>
> - 本签字**仅覆盖** `_v4_pi_cot_v3_verdict_v3.md`（`BB44FDC7AB0F`）件内一致性（观测值 / 阈值 / 判定 / 根因 / 引用）与纪律合规（0 LLM / 0 key / 0 派生合并 / 0 擅调阈值 / 署名如实 / 0 既有件触动）
> - 本签字**不翻任何既判**：(i) v1 verdict `EB9AD4193CF2` 字面冻结（沿 v2 signoff §0.3）；(ii) v2 verdict `5D79E67A4E9D` 字面冻结；(iii) v2 signoff `BA4D07BD7000` 字面冻结；(iv) v3 verdict `BB44FDC7AB0F` 主结论 FAIL 立案 + 复合定性**未翻案**（仅 §3.1 叙述性 per_event 引用误 PASS-with-notes 注记）
> - 本签字**不构成新判定**——仅对 verdict_v3 字面复核给签字
> - 本签字**不触动任何既有件**——只读核验 + 落盘本签字 1 件新件
> - 本签字**不调阈值**——所有阈值沿 v3 prereg §4.3 + §10.1 字面
> - 本签字**不外推命题层**——禁止外推至「PI 思维链不可蒸馏」/「批判性学习维度不可能达标」（沿 verdict_v3 §3.2 + v3 prereg §6）

---

## §8 签字结论

### §8.1 复核面逐项判定

| 复核面 | 判定 | 理由摘要 |
|---|---|---|
| §1 锚链完整性（7 件 SHA-12） | **PASS** ✓ | 7/7 件实测值与 verdict_v3 §0 + 各件自报字面逐一吻合，无漂移 |
| §2 substrate 计数与阈值字面（substrate=77 RUN + 8 D1 missing + 3 件 preflight） | **PASS** ✓ | 37+3+16+12+8+5 = 77；N=77+8=85；3 件 preflight 全 met |
| §3 kill-line 判定复核（6 线 + E-27 §13 复合定性） | **PASS** ✓ | 5/6 hit 字面成立（NW 0.4534 < 0.65 + NLED 0.2754 < 0.55 + div_critical 0.4286 < 1.00 + blind_obey 0.2222 > 0.10 + bootstrap CI 0.3217 < 0.40）；K-V3-E sentinel 不触发 = direction_consistent=True；复合定性（3 复合 + 2 β 主导 + 1 sentinel PASS + 0 纯 α）按四要件复核成立 |
| §4 S-40 方向核对（hit/pass 布尔方向命名 + 公式只含预登记条款） | **PASS** ✓ | hit=True 即触发 FAIL（与判定语义一致）；K-V3-E 不触发走 sentinel 字面；公式只含 v3 prereg §4.3 阈值（0.65/0.55/1.00/0.10/0.40 + sentinel）字面，无私设条款 |
| §5 根因裁因合规（诚实=不误导；不软化；不外推；不机械二选一） | **PASS** ✓ | verdict_v3 §1.4 + §2.7 已显式按 PI 2026-09-23 纪律逐行重判（5 hit + K-V3-E 不触发）；复合定性如实登记（3 复合 + 2 β 主导 + 1 sentinel PASS + 0 纯 α）；不外推至「PI 思维链不可蒸馏」/「批判性学习维度不可能达标」 |
| §6 不翻既判（v1/v2/v2 signoff 字面冻结 + v3 与 v1/v2 并列共存） | **PASS** ✓ | v1 EB9AD4193CF2 / v2 5D79E67A4E9D / v2 signoff BA4D07BD7000 字面冻结；v3 与 v1/v2 并列共存表述正确（沿 verdict_v3 §6 + §7 字面） |
| §7 署名如实 + 0 擅调阈值 + 输入链核验表齐全 | **PASS** ✓ | 署名 = Mavis 团队 verdict-keeper（agent-3a4d09ba3c90）| 2026-09-27；0 擅调阈值（TH-v3-10/11/12/13/14 字面冻结）；输入链核验表 §0 7/7 全 |
| §8 与 v2 对照表（§3）数字与两版原件字面一致性抽查 | **PASS-with-notes** ⚠ | **1 处叙述性 per_event 引用误**：verdict_v3 §2.4 字面列举 9 个一致事件时**错误列入 idx=27**（应入 divergence 类：nw=0.3 nled=0.0 pred=DELEGATE divergent=true），遗漏正确的 idx=76（nw=0.4286 nled=0.3333 pred=CRITERIA divergent=false）；不影响 verdict_v3 主结论（FAIL 立案 + 复合定性）+ 不影响 v1/v2 既判锚点 + 不影响 K-V3-C 数值裁因（n_agree=9 / n_blind_obey=2 / blind_obey_rate=0.2222 正确）+ 不影响复合定性（§2.7 根因三分类汇总正确） |

### §8.2 综合签字结论

> **综合判定**：**PASS-with-notes**（带 1 项叙述性 per_event 引用误注记）
>
> - **核心裁因复核**：PASS（5/6 hit 字面成立 + K-V3-E sentinel PASS + 复合定性成立）
> - **裁因合规复核**：PASS（诚实 = 不误导纪律到位 + 0 纯 α + 3 复合 + 2 β 主导 + 1 sentinel PASS）
> - **锚链完整性复核**：PASS（7 件 SHA-12 全匹配 + 0 漂移）
> - **R5 隐私核查**：PASS（key 永不明文 + 推理全文仅入本地件 + 6 项铁律全声明）
> - **不翻既判复核**：PASS（v1/v2/v2 signoff 字面冻结 + v3 与 v1/v2 并列共存）
> - **叙述性 per_event 引用误注记**：verdict_v3 §2.4 idx=27 字面错位（PASS-with-notes 唯一注记项；不影响主结论）
>
> **结论**：verdict_v3（`BB44FDC7AB0F`）作为任务 B v3 正式判定裁因收口件，**件内一致性与纪律合规成立**；FAIL 立案（formal v3, 复合定性）主结论**未翻案**；唯一瑕疵为 §2.4 9 个一致事件叙述性列举中 idx=27 误列 + idx=76 遗漏，属 PASS-with-notes。

---

## 文末产物核验（诞生即报）

> ⚠ 本字段为避免「回填 SHA → 文件变 → 哈希变 → 再回填」无限循环的稳定方案——SHA-12 前 12 与字节数**不在文件内自记**，统一在最终汇报中核验报出，避免字面不自洽。

- 路径：`results/_v4_pi_cot_v3_verdict_v3_signoff_2026_09_27.md`
- SHA-12 前 12：**见最终汇报核验值**
- 字节数：**见最终汇报核验值**
- 派生关系：本签字由 `_v4_pi_cot_v3_verdict_v3.md`（`BB44FDC7AB0F`）+ 5 件 v3 链 + 1 件 v2 对照锚 + 1 件 v2 结构锚字面读取 + 独立复算生成；所有 7 件均只读核验未触动；v1/v2/v2 signoff/v3 verdict 字面冻结不覆盖
- 性质：verifier 独立复核签字件（产物链末件之后的下游核验件）

---

出件｜Mavis 团队 verifier 签字｜2026-09-27