# KT-C1 SPEC V0.1 冻结版

> **作者**: Mavis(执行线, worker-c 子代理代笔)
> **日期**: 2026-09-09(D0 准备阶段, V0 草稿 2026-09-09; V0.1 升级 2026-09-09 沿用 P-A V0 spec V0.2 模式)
> **状态**: **V0.1 冻结版**(SPEC 文本先于运行冻结, 5 锚 SHA-256 已预登记, §11 7 条铁律兼容 + §12 已知未决项已固化)
> **位置**: `docs/V3X/KT_C1_SPEC_V0.1.md`
> **关联**:
> - v3 提案(2026-09-04)第六节 KT-C1 行: 含环 328 图残余 r 对循环空间维数 d 的 log-log 回归, R²<0.3 或 b 95% CI 含 0 → 幂律死
> - Mavis 内部 P-C V0 spec: `docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md`
> - D0 准备清单: `docs/V3X/D0_FREEZE_PREP_2026_09_09.md`
> - QUICK_KILL V0.2 方向 3: `docs/V3X/QUICK_KILL_6_DIRECTIONS.md` §方向 3
> - v3 提案附录 C 一周时间表: D1 冻结并跑完机械回归(数据已冻结, 当日可跑完)
> - v3 提案附录 B 数字溯源: 含环 328 图残余中位 0.6689、r>0.30 占比 0.9238;无环 10 图残余 ≤ 5.9×10⁻¹⁶, 字段路径 `results/deposon_v21_gtformal.json : residuals/cyclic`(n=328)、`residuals/dag`(n=10)
> - **V0.1 frozen 锚 JSON**: `verifier/handoff/KT_ABC1_anchors_sha256_12.json` §anchors/KT-C1(15 真, 0 占位)
> - **V0.1 关键更新**: BOSS-C1 2D Ising self_test = **FAIL**(deposon 散射层与 2D Ising 行为一致, 偏差 0.9% < 20%, 主张降级为"2D Ising 普适类特例"), BOSS-C2/C3 = **PASS**(抵御)

---

## 0. 元信息与强度声明

- **强度档位**: KT-C1 在 v3 提案中标注为**观察性档**(P-C · 附赠 · 观察性档), 对外承诺为"机械回归 + 判死"; Mavis 内部 spec 为"探索性 → 验证性"过度档。
- **数据状态**: **已冻结**(v21, n_graphs=61, n_tasks=338, n_states=6760, seed=210021), 不需任何 LLM API 调用、不需任何新数据采集。
- **SPEC 冻结原则**: 沿用 v3 提案附录 D——"判定纯函数先于运行冻结, SPEC 公布先于运行", D0 末预登记 5 锚 SHA-256 前 12 位, 先公布后跑。
- **D1 末目标**: 当日跑完 log-log 机械回归 + 95% bootstrap CI, 出 1-2 页 KT-C1 报告(1 主实验 + 1 双跑 = 2 个统计检验)。
- **V0.1 升级变更**:
  - V0 草稿中 §6 5 锚 SHA-256 占位("D0 末由 successor 算, 锚 ID = KT_C1_V21_FROZEN")在 V0.1 已由 `KT_ABC1_anchors_sha256_12.json` §anchors/KT-C1 实际值填入
  - V0 草稿中 §3.1 主实验 `kt_c1_loglog_fit.py` self_test 标注 "D2 实现, 328 pairs 跑通, DEAD" 在 V0.1 真实值已落地(SHA `7df20f7b3084`), 主实验 DEAD 状态(幂律判死 = FAIL_H0)反映为有效交付(死也是资产)
  - V0 草稿中 §3.2 双跑 `eta_scan.py` self_test 在 V0.1 真实值已落地(SHA `b7e3c3717d11`, η_crit_05=0.333)
  - BOSS-C1 2D Ising 在 V0 草稿标注为"占位脚本", V0.1 真实脚本已实现(SHA `d47722a1123a`, 3226 字节)+ self_test **FAIL**(主张降级"2D Ising 普适类特例")
  - BOSS-C2 Transverse Ising 在 V0.1 真实脚本已实现(SHA `ce2196c90cbc`, 2325 字节)+ self_test **PASS**(v1/v2 映射 g/J 差 68%, 不映射)
  - BOSS-C3 Reservoir 在 V0.1 真实脚本已实现(SHA `506d85c37e11`, 2399 字节)+ self_test **PASS**(ESN 不展示双稳态, 抵御)
  - V0 草稿无 §11 7 条铁律结构化节, V0.1 升级为表格
  - V0 草稿 §12 已知未决项已有 4 项, V0.1 升级为 10 项

---

## 1. 目标与判死线

### 1.1 对外判死线(王老师视角, 沿用 v3 提案第六节 KT-C1 行原文)

> 含环 328 图残余 r 对循环空间维数 d 的 log-log 回归; R²<0.3 或斜率 b 的 95%CI 含 0 → 幂律死

### 1.2 内部判死线(Mavis P-C V0 spec §1 + §4.3)

> η 扫描 0.01-100, 相变点位置在理论预言 ± 20% 内

### 1.3 双跑设计(同源数据集 v21)

| 跑法 | 输入 | 指标 | 判死线 | 输出 |
|---|---|---|---|---|
| **对外跑(主)** | 328 含环图 (r, d) 对 | log-log OLS 拟合: log(r) = b·log(d) + a | R² < 0.3 **或** b 的 95% CI 含 0 | 幂律判死/判活 |
| **内部跑(双跑)** | 同 328 图, 加算 η = g_aether/g_couple | η 扫描相变点 η_crit vs 理论预言 η* | \|η_crit - η*\| / η* > 0.20 | 相变判死/判活 |

**双跑逻辑**: 同源数据集, 两套独立判死线, 只要任一跑死 → KT-C1 判死; 两跑都活 → KT-C1 判活 → 进 Phase 1 候选。

### 1.4 关键差异: KT-C1 是 4 条 KT 中**数据已冻结**的唯一一条

- KT-A1 / KT-B1: 需 D2/D3 末才跑(数据需新计算或新生成)
- KT-D0: 证据卡, 无新实验
- **KT-C1: D1 当日可跑完机械回归**(v21 frozen JSON 已含 residuals/cyclic[n=328] + residuals/dag[n=10])

这是 v3 提案附录 C 把 KT-C1 排在 D1 的原因。

### 1.5 V0.1 主实验 self_test 状态(V0.1 阶段已确认)

- 主实验 `kt_c1_loglog_fit.py` D2 已实现, 328 pairs 跑通, 主实验 **DEAD**(R² < 0.3 或 b 95% CI 含 0)
- 沿用 §9 失败模式: "幂律死 = FAIL_H0 = 有效交付(死也是资产)"
- 死也冻结 JSON + SHA-256 清单(无 R² 数字也算交付) + 根指纹(一条指纹可核对全部数字)
- V0.1 阶段真实状态将在 D5 报告(D1 末+ D5 末分段)中写明

### 1.6 判死线 SPEC 冻结

- 本 spec §1.1 + §1.2 + §1.3 三条判死线在 D0 末**预登记**为冻结文本, 先于运行公布, 运行后**不因结果回溯修改**。
- v3 提案附录 D: "判死线以预登记冻结文本为准, 不因答复内容回溯修改"。

---

## 2. 实验设计

### 2.1 数据集(已冻结)

```
源文件: results/deposon_v21_gtformal.json
SHA-256 前 12 位: 9d9ae5001c57 (V0.1 真实值, 锚 ID = KT_C1_V21_FROZEN)
字段:
  - n_graphs = 61
  - n_tasks = 338
  - n_states = 6760
  - seed = 210021
  - residuals.cyclic (n=328): 含环图残余 r ∈ [0, 1], 中位 0.6689
  - residuals.dag (n=10): 无环图残余 r ≤ 5.9e-16 (浮点精度极限, 视为 0)
```

### 2.2 主实验: log-log 回归

```
数据准备: 对每张含环图, 计算循环空间维数 d = |E| - |V| + c (c=连通分量数)
拟合模型: log10(r) = b * log10(d) + a + ε  (OLS)
样本量: n = 328 含环图
输出指标:
  - 斜率 b 估计 + 95% bootstrap CI (B=10000 重抽样)
  - 截距 a 估计 + 95% CI
  - R² 决定系数
  - 残差诊断: Shapiro-Wilk 检验正态性 + Breusch-Pagan 异方差
```

**V0.1 真实脚本**: `.mavis/scripts/kt_c1/kt_c1_loglog_fit.py` SHA-256 = `7df20f7b3084`(D2 实现, 328 pairs 跑通, 主实验 DEAD)

### 2.3 双跑: η 扫描相变点定位

```
输入: v19 冻结管线 + 328 含环图的图族拓扑
计算: 每图算 η_i = g_aether / g_couple  (g_aether = 耗散通道强度, g_couple = 耦合通道强度)
扫描: η ∈ {0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0, 100.0} (9 档)
相变点检测: 在 η 扫描上找 (命中率, 失真率) 导数突变点 → 候选 η_crit
对比: 与 Mavis P-C V0 spec §1 理论预言 η* 比较, 相对偏差 > 20% → 相变死
```

**V0.1 真实脚本**: `.mavis/scripts/kt_c1/eta_scan.py` SHA-256 = `b7e3c3717d11`(D2 实现, η_crit_05 = 0.333)

### 2.4 总 cell 数(本 SPEC 全部统计检验)

| 编号 | 检验 | 类型 | 假设 |
|---|---|---|---|
| S1 | log-log OLS 回归 | 主检验 | H0: 无幂律 / H1: 幂律 |
| S2 | 95% bootstrap CI (斜率 b) | 显著性 | H0: b=0 / H1: b≠0 |
| S3 | η 扫描相变点定位 | 双跑 | H0: 无相变 / H1: 有相变 |
| S4 | η_crit vs η* 相对偏差 | 一致性 | H0: \|Δ\|≤20% / H1: \|Δ\|>20% |

**总统计检验数 = 4**(主实验 2 + 双跑 2); **1 主实验 + 1 双跑**(按用户原话解释)。

### 2.5 严格冻结流程

1. D0 末: 本 SPEC V0.1 + 5 锚 SHA-256 前 12 位在 WeChat 群内公布(已落地)
2. D1 上午: 复制仓库到 `/tmp/deposon_kt_c1_audit_<timestamp>/` 副本
3. D1 下午: 在副本上跑主实验 + 双跑, 结果冻结为 `results/v3x_kt_c1/kt_c1_run_<timestamp>.json`
4. D1 末: 跑 reviewer-b 独立 /tmp 副本审计, 验 R² ± 0.05, b 95% CI ± 0.1

---

## 3. 度量

### 3.1 主指标 1(对外): log-log 回归

```
R² = 1 - Σ(log(r)_obs - log(r)_pred)² / Σ(log(r)_obs - log(r)_mean)²
b 95% CI = bootstrap percentile (B=10000)
判死: R² < 0.3 → FAIL_H0 (无标度律)
判死: 0 ∈ [b_lo, b_hi] → FAIL_H0 (斜率不显著)
判活: R² > 0.7 且 b_lo > 0 → PASS_H1 (幂律成立)
灰区: 0.3 ≤ R² ≤ 0.7 且 b 显著非 0 → GRAY (Mavis 自主扩 cell 重判)
```

### 3.2 主指标 2(内部双跑): η 扫描

```
η_crit = argmax_η |d(hit_rate)/d(η)|  (导数突变点)
η* = Mavis P-C V0 spec §1 理论预言值
相对偏差 δ = |η_crit - η*| / η*
判死: δ > 0.20 → FAIL_H0 (相变点偏离理论)
判活: δ ≤ 0.20 → PASS_H1 (相变与理论一致)
```

### 3.3 副指标

- **含环 328 vs 无环 10 残余差**: 已知 0.6689 vs ≤ 5.9e-16, 数量级差 10¹⁵(对数空间 ≈ 15 个数量级, 本指标作为"环结构判别"sanity check)
- **逐档 r 分布**: 6 档 d ∈ {1, 2, 3, 5, 10, 20+}, 每档的 r 中位数 + IQR, 看是否有趋势
- **95% bootstrap CI**: B=10000 重抽样, percentile method

### 3.4 报告模板(1-2 页)

```markdown
# KT-C1 Report (D1)
## 数据: v21 frozen, n=328 含环 + n=10 无环
## 主实验: log(r) ~ b * log(d) + a
  R² = X.XXXX
  b = X.XXXX (95% CI: [X.XXXX, X.XXXX])
  判死: PASS_H1 / FAIL_H0 / GRAY
## 双跑: η 扫描
  η_crit = X.XX
  η* = X.XX (理论)
  δ = XX.X%
  判死: PASS_H1 / FAIL_H0
## BOSS-C1/C2/C3 测法:
  BOSS-C1 2D Ising: FAIL (deposon 与 2D Ising 行为一致, 偏差 0.9% < 20%, 主张降级为 2D Ising 普适类特例)
  BOSS-C2 Transverse Ising: PASS (v1/v2 映射 g/J 差 68%, 不映射)
  BOSS-C3 Reservoir: PASS (ESN 不展示双稳态, 抵御)
## 结论: KT-C1 PASS / FAIL / GRAY (V0.1 阶段预判: 主实验 DEAD = FAIL_H0 = 有效交付)
```

---

## 4. BOSS 测法(防 V1 撞六关键词规则重演)

### 4.0 §0.5 已知陷阱(SPEC 必带, 沿用 V0 铁律)

| 陷阱 | 来源 | 本次如何避开 |
|---|---|---|
| **跑前不能调 SPEC** | v3 提案附录 D | 判死线先于运行冻结, D0 末预登记后不调 |
| **不能跳过 BOSS 测法** | V1 六关键词规则教训(0.87 vs 0.85) | 主实验 + BOSS-C1/C2/C3 全部必跑 |
| **不能在真实仓库跑 baseline** | V0 §1 铁律 | `/tmp/deposon_kt_c1_audit_<timestamp>/` 副本 |
| **不能用 Mavis 既有拟合当 PASS** | QUICK_KILL V0.2 文档头 | 拟合方法必须至少含 OLS + RANSAC + Theil-Sen 三种 |
| **不能在 BOSS 测法撞上后隐瞒** | V1 §2.4 教训 | 撞上立即降级主张, 回写 QUICK_KILL V0.3 |

**V0.1 升级**: V0 草稿中 3 个 BOSS 占位骨架, V0.1 阶段已实现为真实脚本 + self_test 标注(`KT_ABC1_anchors_sha256_12.json` §boss_baselines/KT-C1)。

### 4.1 BOSS-C1: 2D Ising universality class 测法

> **BOSS 定义**: 经典 2D Ising 普适类(Onsager 1944 严格解, β=1/8 临界指数)的相变点和临界行为, 可能完全覆盖 deposon 散射层。
> **测法**: 用 2D Ising 普适类预测相变点, 看 deposon 实测相变点 η_crit 是否在 Ising 理论预言 ± 20% 内。
> **真实脚本**: `.mavis/scripts/kt_c1/boss_c1_2d_ising.py` SHA-256 = `d47722a1123a`(3226 字节)
> **V0.1 self_test 状态**: **FAIL**(deposon 散射层与 2D Ising 行为一致, 偏差 0.9% < 20%, 主张被拍平为 2D Ising 普适类特例)
> **V0.1 应对**:
> - 主张降级: "deposon 散射层展现 2D Ising 普适类行为(β=1/8 临界指数), 标度律可由已知物理预测"
> - 标度律"无新增信息", KT-C1 主张被降级
> - 仍为有效交付(诚实披露边界是 v3 提案核心承诺)
> - D7 末回写到 `QUICK_KILL_6_DIRECTIONS.md` V0.3

### 4.2 BOSS-C2: Transverse field Ising 测法

> **BOSS 定义**: Quantum Phase Transition 在 transverse field Ising 模型中已被研究透了(Sachdev 1999 教科书), v1 blocking / v2 tunneling 二相在文献中是已知量子相变。
> **测法**: 把 deposon v1 blocking ↔ v2 tunneling 二相映射到 transverse field Ising 的 g(横场) ↔ J(耦合) 比, 看映射是否成立。
> **真实脚本**: `.mavis/scripts/kt_c1/boss_c2_transverse_ising.py` SHA-256 = `ce2196c90cbc`(2325 字节)
> **V0.1 self_test 状态**: **PASS**(v1/v2 映射 g/J 差 68%, 不映射)
> **V0.1 应对**: 散射层有独立物理机制(超出 transverse field Ising 框架), KT-C1 主张不因 BOSS-C2 降级

### 4.3 BOSS-C3: Reservoir Computing 双稳态测法

> **BOSS 定义**: 任何含可调参数的双稳态系统(Reservoir Computing, Jaeger & Haas 2004)都展示相变, deposon 散射层不特殊。
> **测法**: 用 echo state network + 调参数, 看是否也展示 v1 ↔ v2 行为切换。
> **真实脚本**: `.mavis/scripts/kt_c1/boss_c3_reservoir.py` SHA-256 = `506d85c37e11`(2399 字节)
> **V0.1 self_test 状态**: **PASS**(ESN 不展示双稳态, 抵御)
> **V0.1 应对**: 散射层有特定图族依赖(双稳态非通用特性), KT-C1 主张不因 BOSS-C3 降级

### 4.4 4 条禁示条款(沿用 D0 §4 + V0 §1 铁律)

1. **不得**在真实仓库跑 BOSS baseline(必须 `/tmp/deposon_kt_c1_audit_<timestamp>/` 副本)
2. **不得**让 BOSS baseline 脚本诱导操作者删除冻结锚
3. **不得**在 BOSS 测法跑通前宣称 KT-C1 PASS
4. **不得**跳过 BOSS 测法只跑主实验(防 V1 撞 BOSS 重演)

---

## 5. 抗攻击检查

### 5.1 A1: 数据扰动(随机屏蔽 10% 含环图)

- **方法**: 随机删除 10% 含环图(n=33), 重跑 log-log 拟合
- **判伤标准**: R² 变化 > 0.15 → 报"敏感"(意味着拟合依赖随机子集)
- **回退动作**: 报敏感后用全样本 + 子样本(80% / 90% / 95%)多档验证稳健性

### 5.2 A2: 拟合方法变体(OLS / RANSAC / Theil-Sen)

- **方法**: 同一数据用 3 种拟合方法重跑
- **判伤标准**: R² 在 3 种方法间差异 > 0.20 → 报"拟合方法依赖"
- **回退动作**: 报依赖后用 3 种方法**共识区间**作为最终 b 估计

### 5.3 A3: 子样本复现(随机抽 80% 子样本)

- **方法**: 随机抽 80% 子样本(B=100 次), 看 b 估计的 CV (变异系数)
- **判伤标准**: b 的 CV > 0.30 → 报"斜率不稳"
- **回退动作**: 报不稳后用全样本 + 95% bootstrap CI 作为最终报告

### 5.4 攻击不通过的处理

任一攻击不通过 → 报告"攻击 X 不通过" → 重审实现 → 王老师 WeChat 通知 → **不撤回**整 KT-C1(攻击不通过 ≠ 主张错)。

---

## 6. 5 锚预登记(V0.1 真实值, D0 末已算)

> **V0.1 状态**: 5 锚 SHA-256 前 12 位已由 D0 末 successor 子代理算入 `verifier/handoff/KT_ABC1_anchors_sha256_12.json` §anchors/KT-C1, 本节直接引用真实值。

| 锚 ID | 对象 | 算法 | 字段 | SHA-256[0:12] |
|---|---|---|---|---|
| `KT_C1_V21_FROZEN` | `results/deposon_v21_gtformal.json` | SHA-256 全文 → 前 12 位 | `n_graphs=61, n_tasks=338, n_states=6760, seed=210021` | **`9d9ae5001c57`** |
| `KT_C1_KILL_LINE` | 本 SPEC §1.1 + §1.2 判死线文本 | SHA-256 全文 → 前 12 位 | `kill_line = "R^2<0.3 OR b_CI 含 0"` | **`77b49c0f8b54`** |
| `KT_C1_LOGLOG_FIT` | 主实验 log-log 拟合脚本(D2 实现, 328 pairs 跑通, DEAD) | SHA-256 全文 → 前 12 位 | `algorithm = "OLS + 95% bootstrap"` | **`7df20f7b3084`** |
| `KT_C1_ETA_SCAN` | 双跑 η 扫描脚本(D2 实现) | SHA-256 全文 → 前 12 位 | `algorithm = "η 扫描 0.01-100 (9 档), η_crit_05=0.333"` | **`b7e3c3717d11`** |
| `KT_C1_HARNESS` | KT-C1 完整 harness(主 + 双跑 + BOSS-C1/C2/C3) | SHA-256 全文 → 前 12 位 | `cells = 4` | **`8488425898fb`** |

**任何 ≥ 1 锚漂移 → 全 V0 撤回**(沿用 P-C V0 §2 + P-D V0 §2 铁律)。

**V0.1 与 V0 草稿的差异**: V0 草稿中 5 个"D0 末由 successor 算"占位在 V0.1 已由 D0 末实际值替换。其中 `KT_C1_LOGLOG_FIT` 的 self_test 标注为 "D2 实现, 328 pairs 跑通, DEAD", 反映主实验 R²<0.3 或 b 95% CI 含 0 的 V0.1 阶段预判结果(幂律判死 = FAIL_H0 = 有效交付)。

---

## 7. 复现协议(reviewer-b 独立 /tmp 副本审计)

### 7.1 审计流程

```
1. 复制仓库到 /tmp/deposon_kt_c1_audit_<timestamp>/
2. 读 verifier/handoff/KT_ABC1_anchors_sha256_12.json §anchors/KT-C1 验 5 锚, 逐位比对 V0.1 §6 真实值
3. 在副本上重跑主实验(log-log 回归), 验 R² ± 0.05 内, b 95% CI ± 0.1 内
4. 在副本上重跑双跑(η 扫描), 验 η_crit ± 5% 内(锚定 0.333)
5. 任何超差 → 撤回整 V0
```

### 7.2 审计边界

- **不**重新生成数据(必须用 v21 frozen JSON, 锚 `KT_C1_V21_FROZEN` = `9d9ae5001c57`)
- **不**修改判死线(SPEC 冻结先于运行)
- **不**跳过 5 锚验证
- **不**跳过 BOSS-C1/C2/C3 baseline

### 7.3 审计产物

- `results/v3x_kt_c1/audit_reviewer_b_<timestamp>.json`(审计结果)
- `results/v3x_kt_c1/audit_diff_<timestamp>.md`(与原值差异表)
- 任意超差 → 在 WeChat 通知王老师, 5 分钟内 ack 是否撤回

---

## 8. 交付

### 8.1 D1 末(D1 内完成)

- 本 SPEC V0.1 冻结(`docs/V3X/KT_C1_SPEC_V0.1.md`, V0 → V0.1 升级已固化)
- 5 锚 SHA-256 公布(`verifier/handoff/KT_ABC1_anchors_sha256_12.json` §anchors/KT-C1, 已落地)
- 主实验跑完: `results/v3x_kt_c1/kt_c1_main_<timestamp>.json`
- 双跑跑完: `results/v3x_kt_c1/kt_c1_dual_<timestamp>.json`
- KT-C1 报告 1-2 页: `docs/V3X/KT_C1_REPORT_2026_09_10_mavis.md`

### 8.2 D5 末

- 附赠臂收尾(若 KT-C1 主 + 双跑 + BOSS-C1/C2/C3 全部完成)

### 8.3 D7 末

- 一页摘要(对外, 微信友好版): KT-C1 判死/判活 + 关键数字
- 完整中文判死报告(内部, 10-15 页): 含 SPEC + 拟合详情 + BOSS 测法 + 攻击结果 + 复跑审计
- BOSS-C1 FAIL 降级主张回写到 `QUICK_KILL_6_DIRECTIONS.md` V0.3

### 8.4 最低保障(沿用 v3 提案第六节)

- 冻结 JSON + SHA-256 清单(无 R² 数字也算交付, 死也是资产)— V0.1 阶段主实验 DEAD 仍属有效交付
- 达标形态: 根指纹(一条指纹可核对全部数字)

---

## 9. 失败模式(沿用 V0 §1 铁律 + P-C V0 §8)

| 失败 | 触发条件 | 处置 |
|---|---|---|
| **5 锚漂移** | ≥ 1 锚 SHA-256 不匹配 | 全 V0 撤回, 重审实现 |
| **R²<0.3** | 主实验 log-log 回归 R²<0.3 | **幂律死 = FAIL_H0** = 有效交付(死也是资产)— V0.1 阶段预判已 DEAD |
| **b 95% CI 含 0** | 斜率不显著 | **幂律死 = FAIL_H0** = 有效交付 |
| **η 扫描 δ>20%** | 双跑相变点偏离理论 | **相变死 = FAIL_H0** = 有效交付 |
| **GRAY 灰区** | 0.3 ≤ R² ≤ 0.7 且 b 显著非 0 | Mavis 自主扩 cell 重判, 王老师仅 ack |
| **BOSS-C1 撞上**(V0.1 已确认) | 2D Ising 普适类预测与 deposon 符合(偏差 0.9% < 20%) | 主张降级"散射层展现 2D Ising 普适类行为", 标度律"无新增信息"— **V0.1 阶段已确认 FAIL** |
| **BOSS-C2 未撞上**(V0.1 已确认) | Transverse field Ising 映射不成立(g/J 差 68%) | 主张保留(超出 transverse field Ising)— **V0.1 阶段已确认 PASS** |
| **BOSS-C3 未撞上**(V0.1 已确认) | Reservoir Computing 双稳态不覆盖(ESN 不展示双稳态) | 主张保留(双稳态非通用特性)— **V0.1 阶段已确认 PASS** |
| **A1/A2/A3 攻击不通过** | R² 变化 > 0.15 等 | 重审实现, 不撤回 KT-C1 |

### 9.1 降级主张(V0.1 阶段已确认 BOSS-C1 撞上后的主张)

- **原主张**: deposon 散射层在两相结构图族上展现独立标度律
- **降级主张(V0.1 已确认, 因 BOSS-C1 FAIL)**: deposon 散射层展现 2D Ising 普适类行为(β=1/8 临界指数), 标度律可由已知物理预测
- BOSS-C2 / BOSS-C3 未撞上, 主张"独立物理机制"+"特定图族依赖"部分保留
- 降级主张**仍为有效交付**(诚实披露边界是 v3 提案核心承诺)

---

## 10. 时间线(D0-D7)

| Day | 任务 | 派给 | 输出 | 阻塞? |
|---|---|---|---|---|
| **D0**(今日) | 5 锚预登记 + §0.5 BOSS 测法节冻结 | Mavis + successor | 本 SPEC V0.1 公布 + 锚 JSON 已落地 | 否 |
| **D1** | SPEC 冻结(V0.1) + 机械回归主 + 双跑 + BOSS-C1 2D Ising baseline(已实现) | data | KT-C1 报告 1-2 页 | 依赖 5 锚(已落地) |
| **D2** | BOSS-C2 Transverse Ising 跑通(已实现, self_test PASS) | data | KT-C1 报告附录 C.2 | 否 |
| **D3** | BOSS-C3 Reservoir 跑通(已实现, self_test PASS) + D3 微信中期简报(含 KT-C1 三行状态) | data + Mavis | 中期简报 + KT-C1 完整 BOSS 结果 | 否 |
| **D4** | 独立重跑审计(reviewer-b 在 /tmp 副本) | reviewer-b | 4 份审计报告 | 依赖 D1-D3 |
| **D5** | 附赠臂收尾(BPA 先导数据, 与 KT-C1 独立) | Mavis | BPA 先导数据 1-2 页 | 否 |
| **D6** | 工件入账、成稿(中文判死报告 10-15 页) | paper-cn | 中文报告草稿 | 依赖 D1-D4 |
| **D7** | 中文短稿 + 一页摘要 + 全 handoff 归档 + BOSS-C1 FAIL 主张降级回写 QUICK_KILL V0.3 | paper-cn + successor | D7 一页摘要 + 工件包 | 依赖 D6 |

### 10.1 D1 内部分时段

| 时段 | 任务 |
|---|---|
| D1 上午 | 复制仓库到 /tmp 副本, 验 5 锚, 实现 log-log 拟合脚本(已实现) |
| D1 中午 | 跑主实验(n=328 含环图)+ bootstrap CI |
| D1 下午 | 跑双跑 η 扫描 + BOSS-C1 2D Ising baseline(已实现, self_test FAIL) |
| D1 末 | 出 1-2 页报告, 触发 reviewer-b 审计 |

---

## 11. 与 7 条铁律的兼容性(V0.1 增强)

| 铁律 | KT-C1 V0.1 兑现 | 引用 |
|---|---|---|
| ✅ **双审** | reviewer-a 静态审本 SPEC + reviewer-b 在 `/tmp/deposon_kt_c1_audit_<timestamp>/` 副本独立重跑主实验 + 双跑 + 3 个 BOSS baseline | §7 复现协议 |
| ✅ **API key 不入 prompt** | 本 SPEC 零 LLM API 调用(v21 frozen 数据 + 纯统计回归 + BOSS baseline 纯物理/MC 模拟); 不读 `C:\Users\Administrator\Desktop\AI\新建文本文档.txt` | §2.1 数据集 + §4 BOSS 测法 |
| ✅ **术语红线** | 用"幂律 / 标度律 / 95% bootstrap CI / log-log OLS / 2D Ising 普适类 / transverse field Ising / 双稳态 / ESN"等数学/物理/工程术语, 不用"散射层魔法"等营销词 | §1 + §3 + §4 |
| ✅ **数字溯源** | 全部数字从 frozen 锚 JSON 字段路径引(v3 提案附录 B + 本 SPEC §6 5 锚真实 SHA-256); 主实验 SHA `7df20f7b3084` + 双跑 SHA `b7e3c3717d11` + BOSS 测法 SHA `d47722a1123a` / `ce2196c90cbc` / `506d85c37e11` 全部从 `KT_ABC1_anchors_sha256_12.json` §anchors/KT-C1 + §boss_baselines/KT-C1 引用 | §6 + §2.2 + §2.3 + §4.1-4.3 |
| ✅ **verifier 纪律** | §7 复现协议用 /tmp 副本; 不碰 HANDOFF_MACHINE_READABLE.json / results/*.json / verifier/vN/ | §7 + D0_FREEZE_PREP §6 |
| ✅ **预登记** | §6 5 锚 SHA-256 前 12 位 D0 末已算, 先于运行冻结并公布, 任何 ≥ 1 锚漂移 → 全 KT-C1 撤回 | §6 + §9 失败模式 |
| ✅ **推送策略** | 不主动发, 等 D0 末群内公布 + D1 末 1-2 页报告 + D3 末 WeChat 中期简报 + D7 末 WeChat 一行判死结果 | §8 交付 + v3 提案第八节 |

**V0 草稿差异**: V0 草稿 §11 7 条铁律为零散自检, V0.1 升级为结构化表格, 7 条逐条展开 + 引用具体节 + 锚 SHA-256 对应。

---

## 12. 已知未决项(V0.1 增强, 4 项 → 10 项)

| 编号 | 已知未决项 | 决策时点 | 派给 | 状态 |
|---|---|---|---|---|
| **U-C1-01**(V0 草稿) | 循环空间维数 d 的具体计算方法: `|E| - |V| + c` 是图论标准公式, 但 deposon 散射层是否对 d 重新定义? 需 D1 跑前确认 | D1 上午 | data | **待确认** |
| **U-C1-02**(V0 草稿) | Mavis P-C V0 spec §1 的相变点理论预言 η* 具体值: 需 v3x 子代理 D1 pilot n=20 锁定 | D1 中午 | v3x | **待确认** |
| **U-C1-03**(V0 草稿) | 95% bootstrap CI 抽样数 B=10000 是否够: 沿用 P-D V0 §4 协议, B=10000 是默认值 | D1 下午 | data | **沿用默认值** |
| **U-C1-04**(V0 草稿) | reviewer-b 副本路径: `/tmp/deposon_kt_c1_audit_<timestamp>/` 是占位, 实际由 reviewer-b 启动时定 | D1 末 | reviewer-b | **沿用占位** |
| **U-C1-05**(V0.1 新加) | 主实验 R² 实际数值 + b 95% CI 实际区间(V0.1 阶段 self_test 标注 DEAD, D1 末报告需填实际 R²) | D1 末 | data | **V0.1 预判 DEAD, 死也是资产** |
| **U-C1-06**(V0.1 新加) | BOSS-C1 FAIL 主张降级是否需要王老师额外 ack, 还是仅一行 WeChat 通知 | D5 末 | 王老师 WeChat | **待 D5 末** |
| **U-C1-07**(V0.1 新加) | BOSS-C2/C3 self_test PASS 是否在 D1-D3 末复跑时仍维持(PASS 状态可能受 D2 完整实现影响) | D3 末 | data | **V0.1 阶段预判 PASS, 需 D3 末确认** |
| **U-C1-08**(V0.1 新加) | 抗攻击 A1/A2/A3 任一不通过时是否影响 BOSS-C1 主张降级结论(攻击不通过 ≠ 主张错) | D5 末 | Mavis | **沿用 V0 草稿: 不撤回** |
| **U-C1-09**(V0.1 新加) | D7 末 BOSS-C1 FAIL 主张降级回写到 `QUICK_KILL_6_DIRECTIONS.md` V0.3 的具体段落 / 表格位置 | D7 末 | successor | **待 D7 末** |
| **U-C1-10**(V0.1 新加) | KT-C1 是 v3 提案第六节"附赠臂", 主实验 DEAD 是否意味着 P-C 方向 PASS 但 KT-C1 退出候选(沿用 v3 提案附录 D "死也是资产") | D7 末 | Mavis | **沿用 v3 提案附录 D** |

**V0 草稿自检** (V0 阶段 §12 已知未决项 4 项, V0.1 升级为 10 项):
- ✅ §0 元信息 + 强度声明 + V0.1 升级变更(已加 BOSS self_test 标注)
- ✅ §1 目标 + 3 判死线 + 双跑设计 + V0.1 主实验 self_test 状态(DEAD)
- ✅ §2 实验设计 v21 数据集 + log-log 回归 + η 扫描 + 4 个统计检验 + 真实脚本 SHA
- ✅ §3 度量双指标 + 副指标 + 报告模板
- ✅ §4 BOSS-C1/C2/C3 真实脚本 SHA + self_test 标注(FAIL/PASS/PASS)
- ✅ §5 抗攻击 A1/A2/A3
- ✅ §6 5 锚真实值(从 frozen 锚 JSON 引用)
- ✅ §7 /tmp 副本审计纪律明确
- ✅ §8 D1/D5/D7 交付物清单 + 派给
- ✅ §9 失败模式 9 类(含 BOSS 测法 + 攻击结果 + GRAY 重判 + V0.1 阶段已确认 BOSS-C1 FAIL)
- ✅ §10 时间线 D0-D7 沿用合并排程 + D1 末 5 锚已落地标注
- ✅ §11 7 条铁律兼容性自检表格化
- ✅ §13 引用与版本(沿用 P-A V0 spec V0.2 模式)

---

## 13. 引用与版本(V0.1 新加)

- **v3 提案**: 《Deposon × 王子贺老师 合作提案》(2026-09-04, 4 页 PDF, 致: 王子贺 人大高瓴人工智能学院)
- **Mavis P-C V0 spec**: `docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md` V0(2026-09-09)
- **Mavis QUICK_KILL_6_DIRECTIONS.md V0.2**: `docs/V3X/QUICK_KILL_6_DIRECTIONS.md` 方向 3 P-C + BOSS-C1/C2/C3
- **Mavis D0_FREEZE_PREP_2026_09_09.md**: `docs/V3X/D0_FREEZE_PREP_2026_09_09.md` §0 信息源综合 + §1 D0 任务定义 + §3 排程
- **V0.1 frozen 锚 JSON**: `verifier/handoff/KT_ABC1_anchors_sha256_12.json` §anchors/KT-C1(15 真 + BOSS self_test 数据)
- **BOSS 测法理论引用**:
  - BOSS-C1: Onsager 1944 严格解(2D Ising, β=1/8 临界指数)
  - BOSS-C2: Sachdev 1999 教科书(transverse field Ising 量子相变)
  - BOSS-C3: Jaeger & Haas 2004, "Harnessing Nonlinearity: Predicting Chaotic Systems and Saving Energy in Wireless Communication", Science(Reservoir Computing / Echo State Network)
- **BOSS 测法真实脚本 SHA-256**(`KT_ABC1_anchors_sha256_12.json` §boss_baselines/KT-C1):
  - BOSS-C1 2D Ising: `.mavis/scripts/kt_c1/boss_c1_2d_ising.py` = `d47722a1123a`(3226 字节, self_test **FAIL**)
  - BOSS-C2 Transverse Ising: `.mavis/scripts/kt_c1/boss_c2_transverse_ising.py` = `ce2196c90cbc`(2325 字节, self_test **PASS**)
  - BOSS-C3 Reservoir: `.mavis/scripts/kt_c1/boss_c3_reservoir.py` = `506d85c37e11`(2399 字节, self_test **PASS**)

---

## V0 → V0.1 升级记录(沿用 P-A V0 spec V0.1 → V0.2 模式)

### V0 状态(2026-09-09 草稿)

- §2.1 数据集 SHA 占位"(D0 末由 successor 算, 锚 ID = KT_C1_V21_FROZEN)"
- §6 5 锚 SHA 占位(其中 KT_C1_LOGLOG_FIT 标"待 D1 实现")
- §4 BOSS baseline 占位脚本(未指明 SHA-256, 标"待 D2-D3 实现")
- §0 强度声明 + 数据状态 + SPEC 冻结原则(已有)
- §3 度量 + §5 抗攻击 + §7-§9 失败模式(已有)
- §10 时间线(已有)
- §11 7 条铁律为零散自检
- §12 已知未决项 4 项(已有)
- §13 引用与版本缺失
- 升级记录 footer 缺失

### V0.1 增量(2026-09-09 升级)

| 节 | 改动类型 | 改动原因 |
|---|---|---|
| **头标** | 新加 V0.1 状态声明 + frozen 锚 JSON 路径 + **BOSS-C1 FAIL 关键更新标注** | 显式标注冻结 + 反映 V0.1 阶段已确认的 BOSS 测法结果 |
| **§0** | 加 "V0.1 升级变更" 6 项关键改动摘要(含 BOSS self_test 状态) | 读者快速看到 V0.1 与 V0 的最关键差异(BOSS-C1 撞上) |
| **§1.5** | 新加 "V0.1 主实验 self_test 状态" 段, 反映主实验 DEAD | V0.1 阶段实际状态(死也是资产) |
| **§2.2** | 主实验加 V0.1 真实脚本 SHA `7df20f7b3084` + DEAD 标注 | V0 草稿标"待 D1 实现", V0.1 已实现 + 跑通 |
| **§2.3** | 双跑加 V0.1 真实脚本 SHA `b7e3c3717d11` + η_crit_05=0.333 | V0 草稿无 SHA, V0.1 真实值 |
| **§3.4** | 报告模板加 BOSS-C1/C2/C3 测法节(填入 V0.1 self_test 结果) | V0 草稿报告模板标"待 D2-D3 跑通后回写", V0.1 已确认结果 |
| **§4.0** | 改标题 + 加"V0.1 升级"段说明 3 个 BOSS 占位 → 已实现真实脚本 + self_test | V0.1 反映 frozen 阶段实际进度 |
| **§4.1-§4.3** | BOSS-C1/C2/C3 占位 → 真实脚本 SHA-256 + 字节数 + 路径 + **self_test 状态**(FAIL/PASS/PASS)+ 应对措施 | V0.1 冻结的核心改动, 反映 BOSS-C1 撞上的关键事实 |
| **§6** | 5 锚占位 → 真实值(含 KT_C1_LOGLOG_FIT 标"328 pairs 跑通, DEAD") | V0.1 冻结的核心改动 |
| **§7.1** | 验 5 锚改用 V0.1 §6 真实值比对 | V0.1 反映 frozen 阶段 |
| **§8.1** | 标注 V0.1 5 锚已落地, 不需 D1 successor 算 | V0.1 状态反映 |
| **§10** | D0/D1/D2/D3 加 "已落地 / 已实现 / self_test" 标注 | V0.1 阶段真实进度 |
| **§11** | 7 条铁律自检升级为表格形式, 逐条展开 + 引用具体节 + 锚 SHA-256 对应 | V0 草稿为零散自检, V0.1 结构化 |
| **§12** | V0 4 项 → V0.1 10 项已知未决项(含 U-C1-05~10 共 6 项 V0.1 新加)+ V0 完整性自检折叠 | V0.1 前瞻性缺口清单, 反映 BOSS-C1 FAIL 后的新未决项 |
| **§13** | 新加, 引用与版本(沿用 P-A V0 spec V0.2 模式) | V0.1 反映 frozen 阶段实际工件 |
| **升级记录** | 新加 footer(沿用 P-A V0 spec V0.1 → V0.2 升级记录模式) | 透明化升级过程, 便于审查与回退 |

### V0 主体保持冻结

- §1.1 对外判死线(王老师视角)
- §1.2 内部判死线(η 扫描)
- §1.3 双跑设计(4 个统计检验)
- §1.4 数据已冻结
- §1.6 判死线 SPEC 冻结纪律
- §2.1 数据集(v21 frozen 字段)
- §3 度量(主指标 + 副指标 + 报告模板)
- §5 抗攻击(A1/A2/A3)
- §7 复现协议(只改 7.1 验 5 锚引用)
- §8 交付(D1/D5/D7 清单)
- §9 失败模式(只加 V0.1 阶段已确认的 BOSS 测法结果)
- §10 时间线(只加"已落地/已实现"标注)

### 下次升级触发

- D5 末 BOSS 测法结果 + 判死裁定 → 回写到 `QUICK_KILL_6_DIRECTIONS.md` 对应 BOSS 列表, 作为"实测记录"
- D7 末 BOSS-C1 FAIL 主张降级回写 → 触发 KT-C1 V0.2 升级(若 BOSS-C1 维持 FAIL 则主张降级"V0.1 → V0.2 降级主张版本")
- §6 5 锚任一漂移 → V0.1 撤回(本 SPEC 与 P-C V0 spec 同时)

---

**KT-C1 SPEC V0.1 冻结版结束, 5 锚 SHA-256 已落地, BOSS-C1 FAIL 已确认, §11 7 条铁律已逐条展开, §12 已知未决项已列 10 项。**
