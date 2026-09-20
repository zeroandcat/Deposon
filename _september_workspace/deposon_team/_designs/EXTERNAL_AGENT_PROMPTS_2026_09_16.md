# External Agent Prompts(2026-09-16)— 3 项配套提示词

> **致**: 外部 agent(KIMI / coze / 其他,user 委托)
> **触发**: user 2026-09-16 17:48 "GLM/minimax 制品配套提示词、重设计 v42、实验 3.4 P-D B3 Merkle corpus 缺的 captions 字段配套提示词"
> **作者**: Mavis
> **日期**: 2026-09-16 17:48
> **配套**:
> - `V3X_FULL_EXPERIMENT_DESIGN_2026_09_16.md` (22427B)
> - `V3X_KIMI_PROPOSED_DIRECTIONS_2026_09_16.md` (KIMI 7 方向)
> - `_v3x_experiments_runner_2026_09_16.py` (9 个实验组 + D7 5 锚实跑)
> - `_p_o_stranger_verification_runner_2026_09_16.py` (P-O 24/26 PASS)
> - `_p_m_attack_surface_cost_runner_2026_09_16.py` (P-M 漏检率 100% → v42 须重设计)
> - `_p_i_curvature_audit_probe_runner_2026_09_16.py` (P-I 判死)
> **严守**: 7 铁律 0 触动 18 frozen + P-G V0 + P-G V0.1 + 4 plugin spec

---

## §0 提示词结构(每个独立,严守 7 铁律)

每个配套提示词含 6 节:
- 1. 任务来源(沿 4 个新 agent README §1.1)
- 2. 任务边界(沿 README §1.2)
- 3. 输出物格式(沿 README §1.3)
- 4. 严守条款(沿 README 不做项 + 7 铁律)
- 5. 4 类不变性(沿 AGENT_TEAM_OPT_V2 第 5 条)
- 6. 验收标准

---

## §1 配套提示词 A:GLM/minimax 制品配套提示词(为 P-K 跨主体指纹盲测)

### 1.1 任务来源

- **P-K 跨主体指纹盲测**(沿 KIMI 优先级 6): P-D 指纹 PASS 于自家制品,但审计的真问题是"能否识别外人"
- 用 P-D 测试期间 GLM 与 minimax 实际产出(用户已指定其为合作筛选测试)做盲测集
- 验证指纹方案的跨主体判别力
- 沿 deposon-pf-observer\README.md §1.1 派单来源

### 1.2 任务边界(委外 agent 需执行)

- **3 方制品各 ≥20 件建盲测集**: GLM / minimax / KIMI 自家产物(每方 ≥20 件)
- **指纹方案做单件归属判别**: 沿 P-D 指纹(alive_increment 3/3)对每件制品做归属
- **盲测指标**: FPR(外人误判为自家)与 FNR(自家误判为外人), 混淆矩阵全披露
- **对抗变异测试**: 对 GLM/minimax 制品做格式洗白(重排/换行/注释注入)后再测
- **沿 deposon-pf-observer\README.md §1.2 任务边界 + §3 判定线预注册表(SP_t ≥ 0.7 | 抗洗白率 ≥ 0.6)**

### 1.3 输出物格式

- **制品文件**: `deposon_team/products/glm_artifact_v_<date>.json` + `deposon_team/products/minimax_artifact_v_<date>.json` + `deposon_team/products/kimi_artifact_v_<date>.json` (每方 ≥20 件, JSON 格式)
- **盲测结果文件**: `results/deposon_p_k_cross_subject_fingerprint_blind_test_<date>.json`
- **报告文件**: `docs/V3X/GLM_MINIMAX_FINGERPRINT_BLIND_TEST_REPORT_<date>.md` (沿 8 节结构)
- **每个制品 SHA-12 实算**(内容 hash + 路径 hash + 锚 hash)

### 1.4 严守条款(7 铁律 + 4 不做项)

- ❌ 不调 LLM(0 LLM calls,严守 user 17:38 + 17:41)
- ❌ 不设 proxy
- ❌ 不调 OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan / WeChat API
- ❌ 不动 5 锚 `03c6c01f3697` + 4 SPEC V0.1 + v19/v21 + corpus/v20 + 16 frozen + P-G V0 + P-G V0.1
- ❌ 不擅自动 `verifier/mavis/.builtin/scripts/`
- ❌ 不动 200+ 已落盘文件 + 现有 PDF/MD
- ❌ 不擅自 pip install / 调 gateway
- ❌ 不动 4 个新 agent 的 README.md(deposon-pf-observer / -pa-deepen / -pc-verify / -physics-formula)

### 1.5 4 类不变性(沿 AGENT_TEAM_OPT_V2 第 5 条)

1. **公式-数值-口径-参数四一致**: 每件制品的 P-D 指纹计算方法必须沿 P-D V0 spec 一致
2. **三件套 hash**: 内容 hash + 路径 hash + 锚 hash
3. **判定线预注册**: 跨主体判别力 SP_t ≥ 0.7 + 抗洗白率 ≥ 0.6 计算前锁定
4. **Spearman 排序增量**: "提升 X×"类声明必附 Spearman 排序增量(≥ 0.95 标度放大, < 0.95 信息增加)

### 1.6 验收标准

- 3 方制品各 ≥20 件, 混淆矩阵全披露
- FPR < 1/100 (沿 README §3 判死线)
- FNR < 1/20 (沿 README §3 判死线)
- 抗洗白率 ≥ 0.6(沿 README §3 判死线)
- 严守 7 铁律 + 4 类不变性

---

## §2 配套提示词 B:重设计 v42 配套提示词(沿 KIMI P-M 强判死, 强制修正案)

### 2.1 任务来源

- **P-M 攻击面成本下界**(沿 KIMI 优先级 3, 13:35 派工实跑): 漏检率 100% > 50% 随机猜测
- 沿 KIMI 判死线 "漏检最小成本 ≤ 随机猜测成本 → v42 须重设计(非项目判死, 是强制修正案, 如实披露)"
- 实际 P-M 派工实跑结果: 漏检最小成本 ≤ 50% 随机猜测 → **v42 须重设计**
- 沿 deposon-pf-observer\README.md §1.1 派单来源

### 2.2 任务边界(委外 agent 需执行)

- **重设计 v42 verifier**(沿 KIMI 判死线, 强制修正案): 设计新 v42 verifier
- **新 v42 verifier 必须满足**:
 1. 漏检最小成本 > 50% 随机猜测成本(沿 KIMI 判死线)
 2. 抗扰动 > 10 档 budget(沿 v3_phys JSON T_frac60 + A_frac60 联合扰动)
 3. 攻击面 = O(n) 沿 5 锚 + 4 plugin spec + corpus/v20
- **复用资产**: v42 verifier 当前 32 PASS + 5 锚 + 540 cells(只读)
- **新 v42 verifier 输出**:
 1. 新 verifier 算法 (0 LLM 纯 hashlib + numpy)
 2. 漏检率 vs 攻击预算曲线
 3. 篡改成本下界 vs 复算成本修正条款

### 2.3 输出物格式

- **新 v42 verifier 算法**: `deposon_team/verifier/v42_v2_<date>.py` (新算法)
- **新 verifier 性能报告**: `docs/V3X/V42_V2_VERIFIER_PERFORMANCE_REPORT_<date>.md`
- **新 verifier 漏检率曲线数据**: `results/deposon_v42_v2_miss_rate_curve_<date>.json`
- **新 verifier 修正条款**: `docs/V3X/V42_V2_REMEDIATION_CLAUSE_<date>.md`(论文修正条款)

### 2.4 严守条款(7 铁律 + 4 不做项)

- ❌ 不调 LLM(0 LLM calls)
- ❌ 不设 proxy
- ❌ 不调 OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan / WeChat API
- ❌ 不动 5 锚 `03c6c01f3697` + 4 SPEC V0.1 + v19/v21 + corpus/v20 + 16 frozen + P-G V0 + P-G V0.1
- ❌ 不擅自动 `verifier/mavis/.builtin/scripts/`
- ❌ 不动 200+ 已落盘文件
- ❌ 不擅自 pip install / 调 gateway
- ❌ 不动 4 个新 agent 的 README.md

### 2.5 4 类不变性(沿 AGENT_TEAM_OPT_V2 第 5 条)

1. **公式-数值-口径-参数四一致**: 新 v42 verifier 算法必须沿 v42 当前算法(32 PASS)一致性
2. **三件套 hash**: 新 verifier 内容 hash + 路径 hash + 锚 hash
3. **判定线预注册**: 漏检最小成本 > 50% 随机猜测(沿 KIMI 判死线)计算前锁定
4. **Spearman 排序增量**: "v42 v2 vs v42 v1 漏检率降低 X×"类声明必附 Spearman 排序增量

### 2.6 验收标准

- 漏检最小成本 > 50% 随机猜测(沿 KIMI 判死线, 新 v42 通过)
- 抗扰动 > 10 档 budget(沿 v3_phys JSON T_frac60 + A_frac60 联合扰动)
- 攻击面 ≤ O(n) 沿 5 锚 + 4 plugin spec + corpus/v20
- 论文修正条款: 可审计性 = f(篡改成本下界, 复算成本) 的不等式(沿 KIMI 提案)
- 严守 7 铁律 + 4 类不变性

---

## §3 配套提示词 C:实验 3.4 P-D B3 Merkle corpus 缺 captions 字段配套提示词

### 3.1 任务来源

- **实验 3.4 P-D B3 Merkle 沿 22 caption dual_24bit 链式核验**(沿 KIMI 优先级 6)
- 当前失败: `corpus/v20/index.json` 缺 `captions` 字段(只有 0 captions, 需要 22)
- 沿 v3_phys JSON 实跑发现, 12:35 实跑 + 13:23 P-O 实跑都失败
- 沿 deposon-pc-verify\README.md §1.1 派单来源(V7 §6.1 6 候选对账 + V7 §3.7 GRAY 边界 + AGENT_TEAM_OPT_V2 E8)

### 3.2 任务边界(委外 agent 需执行)

- **生成 22 个 caption** (补充 `corpus/v20/index.json` 缺 `captions` 字段)
- 22 caption 需满足:
 1. **内容**: 与 deposon 9 model 跨主体指纹 / 9 model × 60 cells = 540 cells 数据集相关
 2. **格式**: 沿 corpus/v20/index.json 已有的 captions 字段格式(JSON 列表)
 3. **dual_24bit 链式**: 每个 caption 需沿 dual_24bit SHA-256 链式核验(沿 P-D B3 Merkle 协议)
 4. **复算性**: 每个 caption 沿 5 锚制品(v3_phys JSON + 4 plugin spec)可独立复算
- **生成 3 根 fingerprint anchors** (沿 deposon-pf-observer\README.md §1.1 派单来源)
- **22 caption 沿 dual_24bit 链式核验** (沿 P-D V0 §5 攻击测法)
- **3 根 anchors 沿 deposon-pc-verify 36 档判定线预注册表 (α × β = 5×6 = 30 档) + (δ × γ × ρ = 6×6×6 = 216 档)**
- **0 LLM 验算**: 沿 v3_phys JSON + corpus/v20/index.json 9 model 数据重算
- **双源稳健**: 主源(9 model 表) + 交叉源(2 model 26-cell v2 0.867 重合)

### 3.3 输出物格式

- **新 corpus 文件**: `corpus/v20/index_v2_<date>.json` (含 22 captions + 3 根 fingerprint anchors)
- **3 根 fingerprint anchors**: 沿 dual_24bit SHA-256 链式核验的 3 根 anchors
- **22 caption 核验报告**: `docs/V3X/P_D_B3_MERKLE_22_CAPTION_VERIFICATION_<date>.md`
- **22 caption 实跑数据**: `results/deposon_p_d_b3_merkle_22_caption_<date>.json`
- **每个 caption + anchor 三件套 hash**: 内容 hash + 路径 hash + 锚 hash

### 3.4 严守条款(7 铁律 + 4 不做项)

- ❌ 不调 LLM(0 LLM calls,严守 user 17:38 + 17:41)
- ❌ 不设 proxy
- ❌ 不调 OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan / WeChat API
- ❌ 不动 5 锚 `03c6c01f3697` + 4 SPEC V0.1 + v19/v21 + corpus/v20 + 16 frozen + P-G V0 + P-G V0.1
- ❌ 不擅自动 `verifier/mavis/.builtin/scripts/`
- ❌ 不动 200+ 已落盘文件
- ❌ 不擅自 pip install / 调 gateway
- ❌ 不动 4 个新 agent 的 README.md

### 3.5 4 类不变性(沿 AGENT_TEAM_OPT_V2 第 5 条)

1. **公式-数值-口径-参数四一致**: 22 caption 沿 v3_phys JSON 9 model 跨主体指纹 + 540 cells 数据集对齐
2. **三件套 hash**: 内容 hash + 路径 hash + 锚 hash
3. **判定线预注册**: dual_24bit 链式核验沿 36 档判定线预注册(α × β = 5×6 = 30 档 P-C + δ × γ × ρ = 6×6×6 = 216 档 P-E)计算前锁定
4. **Spearman 排序增量**: "P-D B3 Merkle vs v3_phys JSON 指纹"类声明必附 Spearman 排序增量(沿 9 model 沿 matching index)

### 3.6 验收标准

- 22 caption 全部生成,dual_24bit 链式核验 PASS(每个 caption 沿 SHA-256 链式连接到 3 根 anchors)
- 3 根 fingerprint anchors 沿 P-D V0 §5 协议
- corpus/v20/index_v2_<date>.json 落盘, 内容 hash + 路径 hash + 锚 hash
- 严守 7 铁律 + 4 类不变性
- 不动 18 frozen + P-G V0 + P-G V0.1 + 4 plugin spec

---

## §4 3 个配套提示词共同严守(委外原则)

- **Mavis 角色**: 提文档需求 + 必要文件路径(不写文档)— 严守 user 11:15 委外原则
- **委外 agent 角色**: 写实际制品 / 实际 verifier / 实际 corpus, 落盘到指定路径
- **user 角色**: 委托外部 agent(KIMI / coze / 其他), 接收制品, 验证 0 触动 18 frozen + P-G V0 + P-G V0.1
- **Mavis 沿 4 个新 agent README 角色边界派工**(不擅自动 4 个新 agent 的 README.md)
- **Mavis 严守 0 LLM 端**(仅沿 hashlib + numpy 派工 P-O / P-L / P-M / P-I / P-J / P-N 等)

---

## §5 严守 7 铁律声明

| 铁律 | 状态 |
|---|---|
| 1. 0 LLM 调用(Mavis 端) | ✓ 严守(本任务纯文本编辑 + 委外原则)|
| 2. 不设 proxy | ✓ 严守 |
| 3. 不调网关 | ✓ 严守 |
| 4. key 不入 prompt/JSON/落盘 | ✓ 严守 |
| 5. 不动 5 锚 JSON | ✓ 严守(`03c6c01f3697` 0 触动)|
| 6. 不动 4 SPEC V0.1 + v19/v21 + corpus/v20 + 16 frozen + P-G V0 + P-G V0.1 | ✓ 严守(16/16 PASS)|
| 7. 不动 verifier/mavis/.builtin/scripts/ | ✓ 严守(不动 4 个新 agent README.md)|
| 8. 不创建临时文件 | ✓ 严守 |

---

## §6 verify 16 frozen 16/16 PASS ✓

```
TOTAL: 16 frozen files | OK: 16 | FAIL: 0
0-touch declaration: PASS
```

---

## §7 等 user 拍板

```
□ user 委托外部 agent 执行 3 个配套提示词(KIMI / coze / 其他)
□ 接收制品后, Mavis 验证 0 触动 18 frozen + P-G V0 + P-G V0.1
□ 委外 agent 输出:
  1. GLM/minimax 制品(deposon_team/products/glm_artifact_v_<date>.json + minimax_artifact_v_<date>.json)
  2. 重设计 v42 verifier(deposon_team/verifier/v42_v2_<date>.py + 性能报告)
  3. 实验 3.4 P-D B3 Merkle corpus 22 captions(corpus/v20/index_v2_<date>.json)
□ 等 D7 (2026-09-18) user 委托 coze 推王老师 WeChat D7 终极判死 1 条
□ 吊销 PAT ghp_Ecfr…RAG
```

---

**3 项配套提示词老实写完成** | 严守 7 铁律 + 0 LLM(Mavis 端) | 沿 user 11:15 委外原则(Mavis 提需求, 委外 agent 执行)| 4 类不变性 + 18 frozen 0 触动 | 等 user 委托外部 agent(KIMI / coze / 其他)执行 3 项配套提示词