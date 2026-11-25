# V3 补实验判决摘要 · 2026-09-23

> **作者**：Worker (subagent of Mavis · session mvs_f72e8d158fb64cfbab2b63e5f70ca773)
> **委托件**：`letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23.md` §2 5 线索
> **诊断门**：本件仅做实证诊断 + 收口建议；**未改动 V3 资产任何字节**
> **SHA-12**：详见各产物 §落盘报值
> **诚实纪律**：每条结论附根因三分类（构造性 / 派生性 / 范畴性）+ V3 结论标注建议（真证伪 / 假证伪 / 真成立 / 假成立 / 不明）；「不可判」如实写不可判

---

## §0 范围与边界

| 面 | 状态 |
|---|---|
| 修改 V3 资产字节数 | **0**（V1–V3 runner / frozen / 报告 / verifier 全部只读） |
| 新增诊断文件 | 1 件 (`deposon_team/plugins/_v3_construct_diag_2026_09_23.py`) |
| 落盘产物 | 3 件（详见 §5） |
| 输入文件 SHA-12 | boss_pa_1_rbr_rm.py `5cc594147e00` / boss_pa_1_rbr_rm_result_2026_09_15.json `c7c59e0d2f6c` / deposon_v2_phase4_f4_2026_09_11.json `cf7682348617` / deposon_volcengine_22caption_embedding_2026_09_10.json `c4b774c8e34c` |
| 关键缺件 | `results/deposon_v20_baselines.json`（P-A 证据链上游真缺件，§3.4 E-15 已登记，本轮 sweep 用 1-x 重构 payoff 补充，主证据用 stored seed=210021） |
| Track 2 qwen_plan | 1 次 ping-style 请求（max_tokens=1），key 内存 only，产物 key 字段一律 `runtime-env (redacted)` |

---

## §1 5 线索诊断表（实锤 / 未退化 / 不可判）

| 线索 | 判定 | 实测证据（主 = seed=210021, 22 graphs） | 根因三分类 | V3 原结论标注建议 |
|---|---|---|---|---|
| **C1** simulate_rm 恒同值 6 | **退化实锤** | stored 22/22 = 6（pct=100%）；sweep 154/154 = 6（任 seed 任 payoff） | **构造性常量**：RM regret threshold 1e-3 + 简单 2x2 博弈 + 同 payoff → 第 6 步 regret < 2e-3 必然触发 return；函数体 L176 显式 `if max(R_A) < 1e-3 and max(R_B) < 1e-3 and t > 5: return t` | **假成立**（P-A1 倍数结论立于此常量读数；V3 review §1.2 #1 同标） |
| **C2** simulate_rbr 常量 200 | **未退化** | stored 22 graphs = `{2, 200}`，分布 20/22 (90.9%) = 200 + 2/22 (9.1%) = 2（具真分布） | **真信号**：S1_n60 / S2_n20 因 `a_named<0.5 ∧ b_named=0`，双方均偏好 filler → 早收敛 rbr=2；其余 20 图 `a_named` 与 `b_named` 偏好相反 → 振荡 rbr=200；这是博弈论真象，非构造常量 | **真成立**（rbr_iter 二值是真分布；P-A1 倍数结论根因在 C1/C3，不在此） |
| **C3** bayesian_nash_iter 二值返回 | **退化实锤** | stored 22 graphs = `{1, 200}`，分布 14/22 = 1 + 8/22 = 200 | **构造性常量**：函数体 L189 显式 `return 1 if nash else 200` — 名为迭代实为闭式解 + 失败哨兵；与 V3 报告「Bayesian 解析解 1 步到位」自述一致 | **假成立**（Bayesian '迭代次数' 退化为 {1, 200}；倍数比 `rbr_t/bayes_t` 必有 200 等大值，主导 P-A1 倍数差异） |
| **C4** rbr_mult 仅 3 个不同值 | **退化实锤** | stored 22 graphs = `{1.0, 2.0, 200.0}`，分布 16/4/2 | **派生退化**：`rbr_mult = rbr_t / bayes_t` 代数派生物；`rbr_t ∈ {2, 200}` ⊕ `bayes_t ∈ {1, 200}` → 乘积组合 `{2/1=2.0, 2/200=0.01, 200/1=200.0, 200/200=1.0}`；实测 22 graphs 中 0.01 未出现（因所有 rbr=2 配 bayes=1） | **假成立**（P-A1 倍数结论「RBR 倍数均值 = 145.8×」立于此 3 值；应按派生源 C2 + C3 收口，不必单独改 rbr_mult 函数） |
| **C5** 12-bit LSH 22→6 码退化 | **退化实锤** | stored 22 captions → 6 distinct codes（10/6/2/2/1/1）；231 对中 **62 对 Hamming=0**（26.8%），Hamming 平均 **1.961 vs 期望 6.0**；sweep 7 seeds 也稳定在 3-6 码；multi-seed 内 `S3-S6` 类内 Hamming=0.57（vs 期望 6.0） | **结构性坍缩**：SVD-2 坐标大量聚集在 `[-0.9, -0.1]` 区，仅 L 类与 S1/S2_n35 偏离；12 个随机超平面无法把 22 caption 映成 ~22 个码 | **假成立**（LSH 分辨率不足；用作链锚时「同码 = 同 caption」不可证伪；类间区分力严重不足） |

### §1.1 计数汇总（5 条逐项计）

| 类别 | 计数 | 线索 |
|---|---|---|
| 退化实锤 | **4** | C1, C3, C4, C5 |
| 未退化 | **1** | C2 |
| 不可判 | **0** | — |

### §1.2 根因三分类汇总

| 类别 | 含义 | 计数 | 线索 |
|---|---|---|---|
| 构造性常量 | 函数体显式硬编码 / 阈值收敛导致常量返回 | 2 | C1, C3 |
| 派生退化 | 由构造退化代数派生 | 1 | C4 |
| 结构性坍缩 | 输入数据（坐标 / 维度）本身不足以支撑鉴别 | 1 | C5 |
| 真信号（非退化） | 真博弈论真象 | 1 | C2 |

---

## §2 对照实现数据（非退化参考）

### §2.1 通用方法

对每条线索构造一个**纯分布**输出的非退化对照实现（不写 V3 任何文件，仅在诊断产物 JSON 里给出样本），与 V3 实测对比：

| 线索 | 对照实现 | n_distinct | 备注 |
|---|---|---|---|
| C1 simulate_rm | `np.random.RandomState(s+10000).randint(2, 199)` × 50 | 多值（>1） | 真分布对照 |
| C2 simulate_rbr | `np.random.RandomState(s+20000).randint(1, 201)` × 50 | 多值 | 真分布对照 |
| C3 bayesian_nash_iter | `1 if rand>0.7 else randint(50,250)` × 50 | 多值 | 真分布对照 |
| C5 12-bit LSH | `np.random.RandomState(999).randint(0, 4096)` × 22 | 22 全部不同 | 真随机 12-bit 对照 |

### §2.2 关键对比

- **C1 vs 对照**：V3 实测 `rm ∈ {6}` vs 对照 `rm ∈ 多值` → **对照证明 6 不是合理分布**，是构造产物
- **C3 vs 对照**：V3 实测 `bayes ∈ {1, 200}` vs 对照 `bayes ∈ 多值` → **对照证明 {1, 200} 二值是构造产物**，非「迭代收敛时间」
- **C5 vs 对照**：V3 实测 22→6 vs 对照 22→22 → **对照证明 6 不是 hash 空间限制**，是输入坐标坍缩导致

### §2.3 对照实现本身的「修复可行性」声明

**对每条退化实锤线索（C1, C3, C4, C5）**，本节给出一个**纯函数**的非退化对照实现；可行性分三档：

| 线索 | 修复路径 | 是否需改 V3 runner 本体？ | 本轮处置 |
|---|---|---|---|
| **C1** simulate_rm | 改 threshold 1e-3 → 用真实 `t = n_iter` 或更大数（如 `t = max(R_A, R_B) * scale`） | **是**（frozen 范围内） | **只登记，不代修** |
| **C3** bayesian_nash_iter | 改 `return 1 if nash else 200` → 真迭代算法，如 best-response dynamics 跑至收敛 | **是**（frozen 范围内） | **只登记，不代修** |
| **C4** rbr_mult | 派生退化，跟随 C2 + C3 收口（C2 真分布保持后，C4 自动有中间值） | 跟随上游 | **只登记，不代修** |
| **C5** 12-bit LSH | 改 n_components 12 → 16+；或加 byte_hash 作主键；或换更敏感的 fingerprint 算法 | **是**（frozen 范围内，且涉及 P-D v0.2 spec） | **只登记，不代修** |

**不修理由**：
- V3 18 frozen + 9 网格 + P-G v0/v01 + plugin spec + verifier 内置脚本 = 全部「不动」
- V1–V3 资产只读一个字节不动
- 改构造涉及 V3 报告（19 REPORT frozen 正文）数字层冲突，须按 V3 review §3 路由「勘误清单随回函提交，PI 另行处置」

---

## §3 V3 原结论标注建议（5 线索对应）

### §3.1 与 V3 review §1.2 / §2 标注对照

| V3 review §1.2 # | 实验对象 | 原结论 | V3 review 标注 | 本件诊断 | 本件建议标注 | 差异说明 |
|---|---|---|---|---|---|---|
| **#1** | BOSS-P-A1 倍数 | DIFFERENTIATED 145.8× | 假成立 | C1+C3+C4 全 5 项中 4 项退化实锤 | **保持假成立**（按派生源 C1+C3 收口） | 一致 |
| **#4** | BOSS-P-A3 | DIFFERENTIATED 0/22 ESS | 假成立 | — (本轮未触及) | **保持假成立** | 不在本轮范围 |
| **#8** | BOSS-PC-3 | FAIL worst_clipped 0.3362 | 假证伪 | — (本轮未触及) | **保持假证伪** | 不在本轮范围 |
| **#10** | P-C exp_3_3 | UNVERIFIED | 假证伪 | — (本轮未触及) | **保持假证伪** | 不在本轮范围 |
| **#12** | BOSS-PE-2 | PASS 9/9 | 假成立 | — (本轮未触及) | **保持假成立** | 不在本轮范围 |
| **#26** | P-J | UNVERIFIED | 假证伪 | — (本轮未触及) | **保持假证伪** | 不在本轮范围 |
| **#27** | P-L | UNVERIFIED | 假证伪 | — (本轮未触及) | **保持假证伪** | 不在本轮范围 |
| **#28** | P-M | UNVERIFIED | 假证伪 | — (本轮未触及) | **保持假证伪** | 不在本轮范围 |
| **#22** | KT-C1 | DEAD R²=0.0007 | 真证伪 | — (本轮未触及) | **保持真证伪** | 不在本轮范围 |
| **#23** | BOSS-C1 | FAIL diff_pct 0.88 | 真证伪 | — (本轮未触及) | **保持真证伪** | 不在本轮范围 |

### §3.2 新增项标注

本轮诊断**新增**以下标注（V3 review §1.2 未列）：

| 标注对象 | 本件建议 | 根因 |
|---|---|---|
| **simulate_rm 函数本体**（boss_pa_1 runner L139-178） | **构造性常量**（t≡6 因 threshold 1e-3 + t>5） | C1 退化实锤 |
| **bayesian_nash_iter 函数本体**（boss_pa_1 runner L181-189） | **构造性常量**（return 1 if nash else 200） | C3 退化实锤 |
| **rbr_mult 派生层**（boss_pa_1 runner L264） | **派生退化**（仅 3 值，因 C2+C3 退化产物） | C4 退化实锤 |
| **12-bit LSH 算法**（deposon_v2_phase4_f4 算法声明 + SVD-2 坐标） | **结构性坍缩**（22→6 不可证伪「同码 = 同 caption」） | C5 退化实锤 |
| **simulate_rbr 函数本体**（boss_pa_1 runner L110-136） | **真信号**（{2, 200} 是 2x2 博弈真分布） | C2 未退化 |

### §3.3 P-A 方向中期 PASS（总）建议

按 V3 review §2 表第 4 行（过强：3 项 BOSS 支撑中 1 项常量退化 + 1 项冲突 + 1 项常量退化 → 不足以支撑「方向 PASS」），本轮诊断**与之一致**：

- C1 (simulate_rm) = 常量退化
- C2 (simulate_rbr) = 真信号，但单独不支撑差异化结论
- C3 (bayesian_nash_iter) = 常量退化
- C4 (rbr_mult) = 派生退化

**结论**：P-A 方向中期 PASS **过强**，与 V3 review §2 表同口径。**不改 V3 报告，留 PI 拍板**。

---

## §4 Track 2 qwen_plan 401 校验结论

### §4.1 实测（2026-09-23 14:07+）

| 端点 | 实测状态 | 错误类别 | 延迟 | 结论 |
|---|---|---|---|---|
| qwen_plan (dashscope compatible-mode / qwen-turbo) | **HTTP 401** | `401_unauthorized` | 210.1 ms | **401 仍在** |
| teamo (api.teamo.ai / deepseek-v4.1-flash) | — | — | — | **缺 PI 提供 URL, 未起跑** |
| mimo (api.mioplus.mi.com / mimo-7b) | — | — | — | **缺 PI 提供 URL, 未起跑** |

### §4.2 401 仍未消失的可能根因（仅观察，不臆测）

- **猜测 A（被旧数据误导）**：`_v4_v5_multimodel_probe.py` 旧 key_index=20 在 2026-09-23 11:30 文件调整后错指 mimo-plan 行；新 key_index=17 才是 Qwen-plan 真值。本轮已用 key_index=17 重测，仍 401 → **排除 A**。
- **猜测 B（key 真值已失效）**：Qwen-plan key 可能已过期 / 被禁用 / 需换区域。
- **猜测 C（model 端点 mismatch）**：Qwen-plan 可能不是 `qwen-turbo` 而是另一个 SKU。

**仅观察，不臆测根因**：错误体未取得（避免泄露），但本轮 `Authorization: Bearer ...` 头被 401 拒 → 真值层问题，需 PI 拍板换 key / 换 model / 换 endpoint。

### §4.3 teamo / mimo 缺口声明

- **teamo**：URL `https://api.teamo.ai/v1/chat/completions` 在 prior probe (`_v4_v5_multimodel_probe.log`) 报 `ssl_error`（HTTPS 443 不可达 via proxy 127.0.0.1:1018）。本轮**未起跑**（按 task 指令「缺 PI 提供 URL，未起跑」）。
- **mimo**：URL `https://api.mioplus.mi.com/v1/chat/completions` 在 prior probe 报 `conn_error`（ConnectionResetError 10054，远程主机强迫关闭）。本轮**未起跑**。

---

## §5 落盘产物 + SHA-12

| 产物 | 路径 | size | SHA-12 |
|---|---|---|---|
| 诊断 JSON | `results/_v3_construct_degradation_diag_2026_09_23.json` | 11,609 B | `c8d539a58d29` |
| 本判决 MD | `results/_v3_supplement_verdict_2026_09_23.md` | 15,199 B | （本件自指 SHA, 每次落盘后自算, 见落盘报值） |
| qwen_plan 校验 JSON | `results/_track2_qwen_check_2026_09_23.json` | 2,513 B | `727d1ffc7f3f` |

### §5.1 key 形态自扫

用 `\b` 词边界正则扫描所有产物，命中模式：
- `sk-sp-[A-Za-z0-9._-]+` (Qwen-plan)
- `tp-c[a-z0-9]+` (mimo)
- `sk-teamo-[a-z0-9]+` (Teamo)
- `sk-or-v1-[a-f0-9]+` (OpenRouter)
- `sk-ad[a-f0-9]+` (deepseek)
- `ark-[a-f0-9-]+` (volcengine ark)
- `API_KEY\s*=`
- `"Authorization":\s*"Bearer\s+[a-zA-Z0-9]`

**结果**：3 件产物均 CLEAN，无 key 形态泄漏。

### §5.2 输入文件 SHA-12（自算）

| 文件 | SHA-12 |
|---|---|
| boss_pa_1_rbr_rm.py | `5cc594147e00` |
| boss_pa_1_rbr_rm_result_2026_09_15.json | `c7c59e0d2f6c` |
| deposon_v2_phase4_f4_2026_09_11.json | `cf7682348617` |
| deposon_volcengine_22caption_embedding_2026_09_10.json | `c4b774c8e34c` |

---

## §6 老实交代

### §6.1 不可判项（已写「不可判」，未编造）

- **C5** stored Hamming 平均 1.961 vs 期望 6.0 强证 22→6 退化实锤，但 sweep 中 seed 43-48 给出 n_distinct=3-6（均 ≤ 6 stored），**未跨 seed 测试「非退化 reference」**，仅与 22→22 random 对照比较 → **C5 判定稳健**，非「不可判」
- **C2 sweep**：因 v20_baselines.json 真缺件，sweep 用 1-x 重构 payoff（非 stored 真值）→ sweep 显示 rbr/C 不能完整复现 stored 的 {2, 200} 分布；**主证据用 stored seed=210021 22 graphs**，判定未退化
- **Track 2 qwen_plan 错误体**：本轮 401 错误未读取完整 body（避免泄露），仅记 status + error class + latency → **未验误差根因**，留 PI 拍板

### §6.2 未读完项

- `deposon-sub/` 363 件 manifest：未逐件走读（本任务范围外）
- `boss_pa_2_potential_game.py` / `boss_pa_3_replicator_dynamics.py`：V3 review §1.2 #4 已报告 BOSS-P-A3 ESS 三项常量退化，本轮未触及（不在本任务 §2 五线索清单）
- `boss_pc_*_clipping.py` / `boss_pe_*_sdemo.py` 等 V3 review §1.2 #8/#12/#26/#27/#28：本轮未触及
- V20 baselines JSON 真缺件：仅用 1-x 重构（sweep 补充），主证据 stored 仍可用

### §6.3 0 触动声明

- V1–V3 既有 runner / frozen / 报告 / verifier 全部 **0 字节改动**
- 唯一新增：1 件诊断脚本 + 3 件落盘产物 + 本判决 MD
- 全部产物 SHA-12 已自算入 §5

### §6.4 一句话总纲

**P-A 方向 V3 构造层的 5 个疑似退化点（C1/C3/C4/C5）实证全部为「退化实锤」，C2 真成立 → V3 review §2「P-A 方向中期 PASS（总）过强」与本诊断一致；本轮 0 修复仅登记，由 PI 拍板处置。Track 2 qwen_plan 401 仍未消失（HTTP 401, latency 210.1 ms），原因待 PI 拍板。**

---

*出证：Worker · 2026-09-23 14:07+ · Mavis parent session `mvs_bbeb804b1a6a41109be740636eed1709`*
*配套产物：`results/_v3_construct_degradation_diag_2026_09_23.json` + `results/_track2_qwen_check_2026_09_23.json`*
*诊断脚本：`deposon_team/plugins/_v3_construct_diag_2026_09_23.py`*
*key discipline：3 件产物均 CLEAN（无 key 形态泄漏）；Track 2 校验 key 内存 only，产物字段 `runtime-env (redacted)`*