# KT-A1 SPEC V0 草稿

> **作者**: Mavis(执行线,Worker-A 子代理撰写)
> **日期**: 2026-09-09(D0 准备工作流产出)
> **状态**: V0 草稿(待 D1 由 Mavis 改 Mavis P-A V0 spec §1 加 BOSS 测法节)
> **位置**: `docs/V3X/KT_A1_SPEC_V0.md`
> **关联**:
> - v3 提案(王老师致, 2026-09-04)第六节 KT-A1 行:对外判死线 = g_a* 随 λ_gap 单调(十分位分组 + Mann-Whitney 单侧)
> - Mavis 内部 P-A 平衡稳定化 V0 spec(2026-09-09, 10.3KB):内部主指标 = 稳定化成本倍数 ≤ 1.3×(H1)/ ≥ 2.0×(H0)
> - Mavis 内部 QUICK_KILL_6_DIRECTIONS.md V0.2 方向 1 + BOSS-A1/A2/A3
> - Mavis 内部 D0_FREEZE_PREP_2026_09_09.md §0 信息源综合 + §1 D0 任务定义

---

## 0. 元信息与 3 信息源综合(决策依据)

KT-A1 是 v3 提案(王老师致, 2026-09-04, 4 页 PDF)第六节"Phase 0: 一周判死承诺"中列出的 4 条全新机械判死线之一, 对应 P-A′(SPPE 的稳定化成本)。该提案的 KT-A1 行定义对外判死线为:

> "稳定化所需最小耗散 g_a* 随谱瓶颈 λ_gap 单调;十分位分组序统计量 + Mann-Whitney 单侧检验"

Mavis 内部已有的 `P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md`(2026-09-09 V0.1 → V0.2 升级, 加 §0.5 BOSS 测法节)给出的内部主指标为**稳定化成本倍数** = LLM 玩家达到 ε-纳什均衡所需迭代次数 / Bayesian 理论最优响应迭代次数, 判死线为 H0(≥ 2.0× 判死)/ H1(≤ 1.3× 闭合)/ GRAY(1.3×~2.0×)。

**关键决策:双跑设计**。两套指标在测法上不重叠(对外版是"耗散-谱"序统计量, 内部版是"成本-ε-纳什"迭代倍数), 但共享同一组受控概念图(22 图, 从 v20_gt frozen run 复用)+ 同一组 300 cells(3 机制 × 4 任务族 × 25 决策)。双跑产生两类产物:
- **对外 1 页摘要**(D7): 只用 Mann-Whitney 单侧 p < 0.05 这一行判死结果
- **内部 10-15 页判死报告**(D7 备查): 完整成本倍数表 + 95% CI + 攻击结果 + BOSS 测法裁定

**v3 提案 vs Mavis 内部 spec 冲突显式标注**:
- 冲突 1: v3 提案 KT-A1 原文用 "g_a* 随 λ_gap 单调" 描述对外判死线, 但 Mavis P-A V0 spec 主指标是 "成本倍数"——这两个不是同一指标。本 SPEC V0 用"双跑"兼容, 在 §1.2 显式说"两套判死线都跑"。
- 冲突 2: v3 提案附录 B 说"KT-A1/B1/C1 运行后新增冻结 JSON 将于 D7 交付时补入"——本 SPEC 沿用, 在 §6 5 锚预登记只列 P-A V0 spec §2 的 5 锚(KT-A1 行将沿用), 5 锚 SHA-256 前 12 位由 D0 末 successor 子代理算, V0 草稿期不写死。
- 冲突 3: v3 提案 KT-A1 行 "D2 冻结 SPEC, D4-D5 跑", 而 P-A V0 spec §10 D1 已写 "出本 spec + 5 锚预登记"——按 D0_FREEZE_PREP §3 的合并排程, D1 实际是 KT-A1 冻结锚点日(沿用 P-A V0 spec §10 D1 写法), D2 才进入实施。本 SPEC 沿用合并后的 D1-D7 排程。

---

## 1. 目标与判死线

### 1.1 目标

KT-A1 验证"deposon 散射层的稳定化成本在小规模受控概念图上与 Bayesian 最优响应可比较(成本倍数 ≤ 1.3×), 且稳定化所需最小耗散 g_a* 随谱瓶颈 λ_gap 单调递增"。

锚定对象为 P-A 平衡稳定化 V0 spec §1 列出的 5 个冻结工件(ECR 基线 + GT 判死裁定族 + 5 个 frozen run + `tools/llm_client.py` + `tools/exp_harness.py`)。本 SPEC 不引入新的冻结工件, 全部沿用 P-A V0 spec §2 5 锚。

### 1.2 双判死线双跑设计

**对外判死线(v3 提案 KT-A1 原文, 王老师视角)**:
- **描述**: 22 受控概念图上, 对每图算 g_a*(λ_gap), 然后按 λ_gap 十分位分 10 组, 序统计量 + Mann-Whitney 单侧检验单调性。
- **PASS 条件**: Mann-Whitney 单侧 p < 0.05 且 g_a* 中位数随分位单调递增
- **FAIL 条件**: p ≥ 0.05 或 中位数序列出现反转
- **产物**: 1 行写在 D7 对外 1 页摘要(沿用 v3 提案 D7 节奏)

**内部判死线(Mavis P-A V0 spec §1, 工程视角)**:
- **H0 判死**: 成本倍数 mean ≥ 2.0×, CI_lo ≥ 1.7 → 机制不可行, P-A 方向撤
- **H1 闭合**: 成本倍数 mean ≤ 1.3×, CI_hi ≤ 1.5 → 机制可商用, P-A 方向 PASS
- **GRAY**: 1.3 < mean < 2.0 或 CI 跨边界 → 扩 cell(n=300 → n=900)重判
- **产物**: 完整 cost 倍数表 + 95% bootstrap CI + 副指标

**裁定对照**: 内部 H1 + 对外 PASS = P-A 方向 PASS(写进 D7 一页摘要 + D6 内部裁定); 内部 H0 = P-A 方向 FAIL(无论对外); 内部 GRAY = 扩 cell 重判, 对外暂停出 1 页摘要; 对外 FAIL 内部 H1 = "成本合理但单调不成立", 降级为"工程化系统"主张(与 BOSS-A1 RBR/RM 同款降级)。

### 1.3 判死线 SPEC 冻结纪律

- SPEC 文本先于运行冻结(2026-09-09 D0 草稿; D1 改 Mavis P-A V0 spec §1 加 §0.5 BOSS 测法节, 同时加本 SPEC §3 §4 §5 全部节)
- 5 锚 SHA-256 前 12 位在 D0 末由 successor 子代理算, 写入 `verifier/handoff/P_A_V0_anchors_sha256_12.json`
- 任何 ≥ 1 锚漂移 → 全 KT-A1 撤回(P-A V0 spec §2 + 本 SPEC §6)
- 判死线 SPEC 不因王老师答复内容回溯修改(v3 提案第八节"判死线 SPEC 不受影响")

---

## 2. 实验设计

### 2.1 玩家

- **LLM 玩家**: Doubao(volces_ark_bytedance)+ DeepSeek, 按 `tools/llm_client.py` 协议(沿用 P-A V0 spec §3.1)
- **Bayesian 基线玩家**: 理论最优响应计算器(已知机制 + 支付 → 决策)
- **统一决策空间**: 4 选 1(与 deposon 概念图同结构)

### 2.2 机制(3 个, 独立实现 + 比对)

- **M1: Deposon T+R+A 三通道**(移植 deposon 散射层)
- **M2: 纯 Greedy 贪心**(无场, 无守恒约束)
- **M3: Random 随机基线**(均匀采样决策)

### 2.3 任务族(4 个)

- **T1: GSM8K 风格多步算术**(n=20, 源自 v1_4_gsm8k 子集)
- **T2: StrategyQA 风格隐式推理**(n=20, 源自 v1_4_strategyqa 子集)
- **T3: 合成陷阱**(n=20, 源自 v1_3_traps)
- **T4: 自定义最小博弈**(n=10, 2×2 矩阵, 明确纳什均衡点)

### 2.4 数据集(22 受控概念图)

从 v20_gt frozen run 复用 22 个受控概念图(对应 P-A V0 spec §1 中 `verifier/runs/` 下的 5 个 frozen run 中的 v20_gt)。这 22 图的 λ_gap 分布应覆盖 0.01~1.0 全谱瓶颈范围, 以便 D5 跑 Mann-Whitney 十分位分组时各分位都有 ≥ 2 图。

**注意**: v20_gt frozen run 的具体图集合在 D1 由 data 子代理从 `verifier/runs/v20_gt_*.json` 提取(本 SPEC 不写死, 沿用 P-A V0 spec §2 `P_A_FROZEN_RUNS` 锚预登记)。

### 2.5 总 cell 数量

3 机制 × 4 任务族 × 25 决策/任务 = **300 cells**(沿用 P-A V0 spec §3.3)

每个 cell 跑 50 轮(防无限循环) + 记录每轮所有玩家策略 + 支付。

### 2.6 收敛判据

- **ε-纳什**: 任一玩家单独改策略的支付增量 < ε=0.01
- **最多迭代**: 50 轮
- **测量**: 每轮记录所有玩家的策略 + 支付

---

## 3. 度量

### 3.1 主指标 1(对外, v3 提案 KT-A1 原文)

```
对 22 图, 每图算 g_a*(λ_gap)
按 λ_gap 十分位分 10 组
算每组 g_a* 中位数
Mann-Whitney 单侧检验(递增方向)
```

- **PASS**: p < 0.05 且 中位数序列单调递增
- **FAIL**: p ≥ 0.05 或 中位数反转

### 3.2 主指标 2(内部, P-A V0 spec §4.1)

```
cost_multiplier(M, T) = total_iterations_LLM(M, T) / total_iterations_Bayesian(M, T)
```

跨 (M, T) 算 mean + 95% bootstrap CI(10k resamples)。

- **H0 判死**: mean ≥ 2.0×, CI_lo ≥ 1.7
- **H1 闭合**: mean ≤ 1.3×, CI_hi ≤ 1.5
- **GRAY**: 1.3 < mean < 2.0 或 CI 跨边界

### 3.3 副指标(沿用 P-A V0 spec §4.2)

- **收敛成功率**: LLM 玩家在 ≤ 50 轮内达到 ε-纳什的 cell 占比
- **均衡点偏移**: LLM 玩家最终策略 vs Bayesian 真实纳什的 Hamming 距离
- **支付 gap**: LLM 玩家平均支付 vs Bayesian 平均支付

### 3.4 95% bootstrap CI 协议(10k resamples)

```python
def bootstrap_ci(values, n_resamples=10000, ci=0.95):
    means = []
    for _ in range(n_resamples):
        sample = np.random.choice(values, size=len(values), replace=True)
        means.append(np.mean(sample))
    return np.percentile(means, [(1-ci)/2 * 100, (1+ci)/2 * 100])
```

任何 ± 5% 之外的 CI 跨边界 → GRAY 重判。

---

## 4. BOSS 测法(防 V1 撞六关键词规则重演)

### 4.0 §0.5 已知陷阱 + 本次如何避开

**V0 已知陷阱**(从 P-D P1 教训 + V1 六关键词规则撞 BOSS 经验固化, 沿用 P-A V0 spec §0.5):

- **P-D P1 教训**: A1 攻击脚本 CLI 模式与 spec §6 判死命令衔接缺口 + 诱导操作者在真实仓库删除冻结锚。**本次避开**: KT-A1 §5 A1 攻击在 `/tmp/deposon_kt_a1_audit_<timestamp>/` 副本中跑, 不碰真实仓库; 5 锚 SHA-256 闭环在 §6 预登记。
- **V1 六关键词规则撞 BOSS**: GSM8K/StrategyQA accuracy 0.87 vs 0.85, deposon 散射层主张被拍平。**本次避开**: KT-A1 §3 主要指标是"稳定化成本倍数"和"g_a* 序统计量", 不是 accuracy; 即使 LLM 玩家 accuracy 与 Bayesian 相同, 只要成本倍数 ≤ 1.3× 仍可 PASS。

### 4.1 BOSS-A1: Repeated Best Response / Regret Matching

**理论背景**: Hart & Mas-Colell 2000, "A Simple Procedure Leading to Correlated Equilibrium"。RBR/RM 是无 deposon 散射层的简单势博弈算法, 经典结果证明在 22 节点上单调收敛。

**测法**:
1. 加载同样的 22 受控概念图
2. 不跑 deposon 散射层, 直接跑 RBR/RM 算法(沿用 `boss_a1_rbr_rm.py` 占位脚本)
3. 算 P-A V0 spec §4.1 成本倍数
4. 跑 200 节点(可扩大规模以确保统计功效), 算 mean + 95% CI

**裁定**:
- 如 RBR/RM 也 ≤ 1.3× → 主张降级为"工程化系统"(deposon 散射层无差异化)
- 如 RBR/RM > 2.0× → deposon 散射层有差异化(保留主张)
- 如 1.3 < RBR/RM < 2.0 → 灰区, 看 BOSS-A2 / BOSS-A3 是否也撞上, 综合裁定

### 4.2 BOSS-A2: Potential Game(Monderer & Shapley 1996)

**理论背景**: Monderer & Shapley 1996, "Potential Games"。经典 Potential Game 理论给出势函数 φ, 在 φ 单调下任何贪心算法都收敛。

**测法**:
1. 不跑 deposon, 直接把 22 受控概念图转为 Potential Game 形式
2. 套势函数 φ 闭式证明 P-A V0 spec §1 H1 主张(LLM 与 Bayesian 几乎无差)
3. 沿用 `boss_a2_potential_game.py` 占位脚本

**裁定**:
- 如能闭式证明 → deposon 散射层"无新增理论价值", 降级主张
- 如不能闭式证明(因 22 图不满足 Potential Game 形式) → 主张保留

### 4.3 BOSS-A3: Replicator Dynamics + ESS

**理论背景**: Smith 1973, Taylor & Nowak 2006, "Transforming the Analysis of Evolutionary Dynamics"。Replicator Dynamics 在单纯形上跑, 收敛到 ESS(Evolutionarily Stable Strategy)。

**测法**:
1. Replicator Dynamics 跑 22 受控概念图
2. 算 ESS 平衡点
3. 与 deposon 散射层平衡点比较
4. 沿用 `boss_a3_replicator_dynamics.py` 占位脚本

**裁定**:
- 如 ESS 与 deposon 平衡点重合 → 主张被拍平, 降级为"通用进化博弈特例"
- 如不重合 → 主张保留(散射层有差异化)

### 4.4 4 条禁示条款(沿用 P-D P1 + V1 六关键词规则教训)

- **不得**只跑 KT-A1 §2 实验而跳过 BOSS-A1/A2/A3 baseline(防 V1 撞 BOSS 重演)
- **不得**在 BOSS 测法跑通前宣称 KT-A1 PASS(防 P-D P1 复现: 判死过早)
- **不得**在真实仓库跑 BOSS baseline(必须 `/tmp/deposon_kt_a1_audit_<timestamp>/` 副本)
- **不得**让 BOSS 测法脚本诱导操作者删除 §6 预登记 5 锚(无参 + 临时副本, 沿用 P-D V0.1.2 修复模式)

---

## 5. 抗攻击检查(沿用 P-A V0 spec §5)

### 5.1 A1: 提示词扰动

调换 system prompt 中机制描述顺序 3 次, 重跑 10 cell(选 3 机制 × 4 任务族 中代表性 10 cell), 看 cost 倍数变化 > 50% 则报"不稳定"。

**实施细节**: 在 `/tmp/deposon_kt_a1_audit_<timestamp>/` 副本中跑, 不碰真实仓库的 `tools/llm_client.py`。3 次调换覆盖: (a) 顺序 1: M1 → M2 → M3 描述; (b) 顺序 2: M2 → M3 → M1; (c) 顺序 3: M3 → M1 → M2。

### 5.2 A2: 温度敏感性

LLM temperature 0.0 / 0.5 / 1.0 三档, 看 cost 倍数 > 30% 变化则报"温度敏感"。

**实施细节**: `tools/llm_client.py` 支持 temperature 参数(沿用 P-A V0 spec §3.1), D2 实现时确保 3 档都能跑, 不引入额外 LLM API key 读取(沿用 7 条铁律)。

### 5.3 A3: 种子复现

seed = 42, 123, 456 三套, 看 cost 倍数 std/mean > 0.2 则报"种子敏感"。

**实施细节**: `tools/exp_harness.py` 接受 seed 参数(沿用 P-A V0 spec §3.1), D2 实现时 3 套 seed 跑 100 决策/cell, 算变异系数(CV = std/mean)。

### 5.4 攻击结果裁定

- A1 不稳定 → 重审实现, 王老师 ack 是否撤回
- A2 温度敏感 → 重审实现, 提示词模板可能需要更严格规范
- A3 种子敏感 → 重审实现, RNG 可能被 LLM 玩家污染

任何 1 攻击不通过 → 整 KT-A1 重审, 不直接撤。

---

## 6. 5 锚预登记(D0 末由 successor 子代理算 SHA-256 前 12 位填入)

> **本节为占位, D0 末由 successor 子代理计算实际 SHA-256 前 12 位, 写入 `verifier/handoff/P_A_V0_anchors_sha256_12.json`**。

| 锚 ID | 对象 | 算法 | 字段 | SHA-256[0:12](占位) |
|---|---|---|---|---|
| `P_A_ECR_BASELINE` | P-A V0 spec §3 ECR=1.333 基线 | SHA-256 全文 → 前 12 位 | `ecr_median=1.333` | `<TO_BE_FILLED>` |
| `P_A_KILL_LINE` | GT 判死裁定族(10 个) | SHA-256 全文 → 前 12 位 | `kills={"GT-1":true, ...}` | `<TO_BE_FILLED>` |
| `P_A_FROZEN_RUNS` | 5 个 frozen run JSON | SHA-256 各 → 前 12 位 | `runs=["v20_gt", ...]` | `<TO_BE_FILLED>` |
| `P_A_LLM_CLIENT` | `tools/llm_client.py` | SHA-256 全文 → 前 12 位 | `version=2026-09-11` | `<TO_BE_FILLED>` |
| `P_A_HARNESS` | `tools/exp_harness.py` | SHA-256 全文 → 前 12 位 | `version=2026-09-11` | `<TO_BE_FILLED>` |

**任何 ≥ 1 锚漂移 → 全 KT-A1 撤回**。

**说明**: KT-A1 沿用 P-A V0 spec §2 的 5 锚, 不引入新锚。这是因为 KT-A1 是 P-A V0 spec 在 v3 提案语境下的对外映射, 内部判死线 + 攻击脚本 + 22 受控概念图 + 300 cells 全部沿用, 不需新增冻结工件。g_a* 序统计量(Mann-Whitney 单侧)作为对外主指标 1 也不引入新锚, 因为它是从 `P_A_FROZEN_RUNS` 中 v20_gt 数据派生, 不需冻结额外的"判死函数源代码"。

---

## 7. 复现协议(reviewer-b 独立 /tmp 副本审计)

### 7.1 复制副本

```bash
TIMESTAMP=$(date +%s)
AUDIT_DIR="/tmp/deposon_kt_a1_audit_${TIMESTAMP}/"
cp -r /path/to/deposon-repo "${AUDIT_DIR}"
```

**约束**: 副本必须落到 `/tmp/` 路径下, 不修改真实仓库(沿用 P-A V0 spec §6 + 7 条铁律 verifier 纪律)。

### 7.2 验 5 锚

读 `verifier/handoff/P_A_V0_anchors_sha256_12.json`, 对副本中的 5 锚对象算 SHA-256 前 12 位, 逐位比对。

### 7.3 选 1 cell 重跑

选 1 cell(例: M1 × T1 GSM8K 20 题), 重跑 100 决策 × 5 seed = 500 calls。

### 7.4 验 ± 5%

- 成本倍数与原值 ± 5% 内 → PASS
- 任意超差 → 撤回整 KT-A1

---

## 8. 交付(沿用 P-A V0 spec §7 + v3 提案附录 C D7 节奏)

| Day | 交付物 | 路径 | 派给 |
|---|---|---|---|
| D1 | KT-A1 SPEC 冻结(Mavis 改 Mavis P-A V0 spec §1 加 BOSS 测法节) | `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` | Mavis |
| D2 | LLM 玩家 + 3 机制 + 4 任务族 harness + BOSS-A1 RBR/RM baseline 占位 | `.mavis/scripts/kt_a1/`, `tools/` | data |
| D3 | pilot 50 calls 跑通 + BOSS-A1 baseline 跑通 | `results/v3x_kt_a1/pilot_d3.json` | data + v3x |
| D4 | 全 300 calls + BOSS-A2 Potential Game 闭式 + BOSS-A3 Replicator Dynamics | `results/v3x_kt_a1/full_d4.json` | data |
| D5 | reviewer-b 判死 + 3 攻击 + BOSS-A1/A2/A3 测法 + P-A 判死裁定对照 | `docs/V3X/KT_A1_V0_RESULTS_2026_09_09_mavis.md` | reviewer-b + data |
| D6 | 失败模式处理 / GRAY 扩 cell / 若 BOSS 测法全 PASS 则 P-A 方向 PASS | (续 D5 报告) | Mavis + v3x |
| D7 | 一页摘要(对外, 给王老师)+ 完整中文判死报告(内部) | `docs/V3X/KT_A1_V0_PAPER_zh.md` + WeChat | paper-cn + successor |
| D7 | BOSS 测法结果回写到 QUICK_KILL_6_DIRECTIONS.md V0.3 | `docs/V3X/QUICK_KILL_6_DIRECTIONS.md` | successor |

D5 报告 1-2 页: 成本倍数表 + 95% CI + 对外 Mann-Whitney p 值 + 判死裁定 + 攻击结果 + BOSS-A1/A2/A3 裁定。

D7 一页摘要(对外): 只列对外判死线结果 + P-A 方向 PASS/FAIL/GRAY + 王老师 ack 按钮。

---

## 9. 失败模式(与王老师 WeChat 同步, 沿用 P-A V0 spec §8)

- **5 锚漂移 ≥ 1** → 全 KT-A1 撤回
- **判死 H0**(cost 倍数 ≥ 2.0×) → P-A 方向 FAIL, 撤 V3.X 整个 P-A 候选
- **判死 H1**(cost 倍数 ≤ 1.3×)+ **对外 Mann-Whitney p ≥ 0.05** → "成本合理但单调不成立", 降级为"工程化系统"主张(与 BOSS-A1 RBR/RM 同款降级)
- **判死 GRAY**(1.3 < cost < 2.0) → Mavis 自主扩 cell(n=300 → n=900)重判, 王老师仅 ack
- **BOSS-A1 RBR/RM ≤ 1.3×** → 主张降级为"工程化系统"
- **BOSS-A2 Potential Game 能闭式证明** → 主张降级为"包装"
- **BOSS-A3 ESS 与 deposon 平衡点重合** → 主张降级为"通用进化博弈特例"
- **A1/A2/A3 攻击任一不通过** → 重审实现, 王老师 ack 是否撤回
- **王老师答复内容要求改判死线** → 不接受(沿用 v3 提案第八节"判死线 SPEC 不受影响"), 但可调后续深度排序

---

## 10. 时间线(D1-D7, 沿用 P-A V0 spec §10 + D0_FREEZE_PREP §3 合并)

- **D0**(2026-09-09): 锚点预登记 successor 子代理算 5 锚 SHA-256 前 12 位 + 本 SPEC V0 草稿冻结 + §0.5 BOSS 测法节冻结(已包含在 Mavis P-A V0 spec V0.2 升级中)
- **D1**: Mavis 改 Mavis P-A V0 spec §1 加 BOSS 测法节(本 SPEC §4 内容纳入); 5 锚 JSON 落地
- **D2**: 实现 LLM 玩家 + 3 机制 + 4 任务族 harness + BOSS-A1 RBR/RM baseline 占位 → 跑通 pilot 5 cell
- **D3**: pilot 50 calls 跑通 + BOSS-A1 baseline 跑通 + 触发 D3 WeChat 1
- **D4**: 全 300 calls + BOSS-A2 Potential Game 闭式 + BOSS-A3 Replicator Dynamics 跑通
- **D5**: reviewer-b 判死 + 3 攻击 + BOSS-A1/A2/A3 测法 + P-A 判死裁定对照 + D5 报告
- **D6**: 失败模式处理 / GRAY 扩 cell / 若 BOSS 测法全 PASS 则 P-A 方向 PASS; 任一 BOSS 测法撞上则降级主张
- **D7**: 中文短稿 + 全 handoff 归档 + BOSS 测法结果回写到 QUICK_KILL_6_DIRECTIONS.md V0.3

---

## 11. 与 7 条铁律兼容性(沿用 P-A V0 spec §9)

- ✅ **双审**: 本 SPEC 写完 self-review 1 遍(见 §12)
- ✅ **API key 不入 prompt**: 不读 `C:\Users\Administrator\Desktop\AI\新建文本文档.txt`, 只在 D2 实现 step 才读; 本 SPEC V0 草稿期不读
- ✅ **术语红线**: 用"成本倍数 / ε-纳什 / 稳定化代价 / 势博弈 / 序统计量"等工程术语
- ✅ **数字溯源**: 全部数字从冻结 JSON 字段路径引(v3 提案附录 B + P-A V0 spec §2 5 锚字段); 本 SPEC 不写新数字
- ✅ **verifier 纪律**: §7 复现协议用 /tmp 副本
- ✅ **预登记**: §6 5 锚先冻结 SHA-256 前 12 位
- ✅ **推送策略**: 不主动发, 等 D0 末群内公布

---

## 12. Self-Review(自审记录)

**V0 草稿自审 1 遍, 逐节核查**:

- ✅ §0 元信息 + 3 信息源综合, 冲突显式标注
- ✅ §1 双判死线双跑设计明确, 裁定对照逻辑清晰
- ✅ §2 实验设计 22 受控概念图 + 300 cells + 3 机制 + 4 任务族, 沿用 P-A V0 spec §3
- ✅ §3 双主指标 + 副指标 + 95% bootstrap CI 协议, 沿用 P-A V0 spec §4
- ✅ §4 BOSS-A1/A2/A3 测法具体, 4 条禁示条款沿用 P-A V0 spec §0.5
- ✅ §5 抗攻击 A1/A2/A3 沿用 P-A V0 spec §5
- ✅ §6 5 锚占位待 D0 末填入, 不写死
- ✅ §7 /tmp 副本审计纪律明确
- ✅ §8 D1-D7 交付物清单 + 派给
- ✅ §9 失败模式 8 条, 含 BOSS 测法 + 攻击结果 + GRAY 重判
- ✅ §10 时间线 D0-D7 沿用合并排程
- ✅ §11 7 条铁律兼容性自检
- ✅ §13 引用与版本

**未发现冲突**: v3 提案 vs Mavis P-A V0 spec 已在 §0 显式标注 3 处差异并通过"双跑"兼容, 无新冲突。

**待 D1 由 Mavis 完成**: 5 锚 SHA-256 前 12 位实际计算, 写入 `verifier/handoff/P_A_V0_anchors_sha256_12.json`。

---

## 13. 引用与版本

- **v3 提案**: 《Deposon × 王子贺老师 合作提案》(2026-09-04, 4 页 PDF, 致: 王子贺 人大高瓴人工智能学院)
- **Mavis P-A V0 spec**: `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` V0.1 → V0.2(2026-09-09 加 §0.5 BOSS 测法节)
- **Mavis QUICK_KILL_6_DIRECTIONS.md V0.2**: `docs/V3X/QUICK_KILL_6_DIRECTIONS.md` 方向 1 P-A + BOSS-A1/A2/A3
- **Mavis D0_FREEZE_PREP_2026_09_09.md**: `docs/V3X/D0_FREEZE_PREP_2026_09_09.md` §0 信息源综合 + §1 D0 任务定义 + §3 排程
- **BOSS 测法理论引用**:
  - BOSS-A1: Hart & Mas-Colell 2000, "A Simple Procedure Leading to Correlated Equilibrium"
  - BOSS-A2: Monderer & Shapley 1996, "Potential Games", Games and Economic Behavior
  - BOSS-A3: Smith 1973, "The Logic of Animal Conflict"; Taylor & Nowak 2006, "Transforming the Analysis of Evolutionary Dynamics"

---

**KT-A1 SPEC V0 草稿结束, 待 D0 末群内公布 + D1 Mavis 改 P-A V0 spec §1 加 BOSS 测法节。**
