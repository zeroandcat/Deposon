# SPEC_GT2B — GT-2 多陷阱强度升级（题库轨）预登记

- 登记时间：先于任何 GT-2B 运行结果写入（先写后跑）。
- 执行脚本：`run_v20_gt2b.py` → `results/deposon_v20_gt2b.json`。
- 零 LLM API：仅复用 `results/gt2_attacker_cache/*.json` 既有缓存；不发起任何网络/API 调用；不合成、不改写陷阱标签。
- 依据：docs/Findings_v2.0_skills.md §三（rule_filter 27.5%≈机会、field_mean 52.5%）与 §四.2（「GT-2 升级（多陷阱注入）以 rule_filter 的题库表现为直接度量」）。

## 1. 假设

- **H_GT2B**：rule_filter（关键词表规则防御）的题库准确率随攻击者陷阱注入强度 T 上升而**单调下降**。
- **场免疫零假设**：field_mean 保持机制性免疫——陷阱标签不在图节点集内，场对其打 -inf，准确率不随 T 变化（±0.05 容差带内）。该免疫是排序对象域的机制结果，非语义识别能力，如实披露。

## 2. 设计

- 题库：沿用 run_v20_quizbank 的 BANK_SEED=20260828 与选题逻辑，4 域 × 10 题，L4 单选，stem/金边不变。
- **固定 4 选项（机会水平恒 25%）**：陷阱数 T ∈ {1, 2, 3}，其余 3−T 个干扰位用图内随机节点补足。选项数不变 ⇒ 隔离「陷阱强度」与「选项数」两个自由度。
- 陷阱分配：每题取缓存陷阱 `traps[(T*k + j) % len(traps)]`（j=0..T−1，k 为题号），与既有题库同族的确定性取法。
- 臂：rule_filter / field_mean / random（种子化）。**llm_prior 本轮不跑**（零 API 纪律，先验臂属于 API 轨）。
- 域覆盖：geography_world / project_management 无 gt2_attacker_cache，**降级为 4 域**（与既有 quizbank_v20 一致），如实披露。
- 确定性：全部随机操作由 `np.random.default_rng` 显式种子驱动；禁用进程随机化的 `hash()`，改用 crc32 稳定哈希；结果 JSON 不含运行时字段，同种子两次运行逐字节一致。

## 3. 缓存可用性核查（登记时实测）

| 域 | 缓存陷阱数（唯一） | 与图节点集交集 |
|---|---|---|
| algorithm_process | 12 | 空 |
| biological_taxonomy | 12 | 空 |
| historical_causality | 12 | 空 |
| physics_concepts | 12 | 空 |

每域 12 ≥ 3 ⇒ **T ∈ {1, 2, 3} 全级别可跑，无需降级**（题目间陷阱复用采用模取，与既有题库一致；题内 T 个陷阱互不相同——12 个陷阱、T≤3 时模取不重叠）。

## 4. 成功标准（判定逻辑，机械执行）

对总体准确率 acc(T)：

- **supports_H_GT2B**：rule_filter 满足 acc(1) > acc(2) > acc(3)（严格单调递减），且场免疫判据通过。
- **inconclusive**：任一级反转或持平（非严格递减且非单调上升）。
- **H_GT2B_dead**：rule_filter 准确率随 T 单调**上升**（acc(1) < acc(2) < acc(3)），如实宣布判死。
- **场免疫判据**：|acc_field(T) − acc_field(1)| ≤ 0.05 对所有 T 成立。若被违反，如实披露「机制性免疫被破坏」，不修改判据。

## 5. 诚实纪律

- 判定机械求值，负面/反转如实；不写回既有 Findings 结论。
- field_mean 免疫是机制性（对象域外标签 -inf），不作为语义防御能力主张。
- 题库仅供横向对比（题型效度），不作为独立基准主张。
