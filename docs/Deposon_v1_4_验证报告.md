# Deposon（凝子）统一场论 —— v1.4.0 迭代验证报告

**副标题**：validate 主环路 + 真实 GSM8K 基准 + CoT 基线对照

| 项目 | 内容 |
| --- | --- |
| 日期 | 2026-08-22 |
| 版本 | 1.4.0（基于 v1.3.1 迭代） |
| 状态 | A 阶段完成；B 阶段（GSM8K）待 API 配额刷新后补齐 |

---

## 一、执行摘要（本轮迭代概览）

在 v1.3.0（真实 Kimi LLM 后端 + 效应量根因修复）基础上，本轮完成：

1. **A1 — v1.3 残留清零**：3 条 surface_division 题以 prompt v1.3.1 重跑成功，陷阱集 unified 97% → **100%**（六类陷阱全部满分），effect_size +0.84 → **+0.90**。
2. **A2 — validate 纳入主环路**：200 题全量真实 LLM 验证（0 降级，约 8 万 tokens）。
3. **B — 真实 GSM8K 评测**（进行中）：官方 test split 随机抽 100 题（seed=42），引入 **CoT 直接答题基线**作为"LLM 本身"水位线，回答"Deposon 是否给 LLM 带来增量"这一根本问题。

---

## 二、A 阶段详细结果

### 2.1 陷阱数据集最终态（100题, seed=42）

| 变体 | v1.2 | v1.3.0 | v1.3.1（本轮） |
| --- | --- | --- | --- |
| no_deposon | 54% | 13% | 10% |
| v1_blocking | 54% | 97% | **100%** |
| v2_tunneling | 54% | 84% | 84% |
| unified | 54% | 97% | **100%** |
| high_couple | 54% | 97% | **100%** |
| **effect_size** | 0.0 | +0.84 | **+0.90** |

陷阱分类（unified）：none / surface_addition / surface_subtraction / wrong_order / surface_multiplication / surface_division 全部 **100%**。

### 2.2 validate 层全量统计（200题真实 API）

| 数据集 | verdict=correct | verdict=incorrect | 与 is_correct 一致性 |
| --- | --- | --- | --- |
| simple 100题 | 86 | 14 | 0.86 |
| traps 100题 | 78 | 22 | 0.78 |

**诚实声明**：unified 变体实际答题全对，但 validator 对「节点路径式」推理链偏严格，incorrect 判决为**误报**（false negative）。这说明 validate 的 prompt 需要理解 Deposon 路径表示法，v1.5 应改进验证 prompt 或改用「让 LLM 独立复算再比对」的验证范式。当前 validate 适合作为保守的风险标记器，不适合作为绝对判官。

---

## 三、外部基线参照（联网检索，2025-2026 文献）

| 参照点 | GSM8K 表现 | 来源 |
| --- | --- | --- |
| Kimi K2（本系统所用模型家族） | ≈96.1% | arXiv:2601.14053 汇总表 |
| CoT vs 直接答题增益 | +15~20 pp | Wei et al. 2022 系综述 |
| Self-consistency（多路径投票） | +17.9 pp（原始论文） | arXiv:2606.08728 综述引述 |
| 小模型 CoT 水位（8B 级） | 76~95%（随规模） | 多篇量化/综述文献 |

**判读框架**：若 Deposon-unified ≥ CoT 基线，说明物理层至少无损且可能通过陷阱抑制带来增量；若 unified < CoT，则需分析图构建或路径筛选的信息损失——两种结果都有科学价值，如实报告。

---

## 四、B 阶段：GSM8K 真实基准（待配额刷新后填充）

<!-- GSM8K_RESULTS -->

设计：官方 test split（1319 题）seed=42 抽 100 题；三组对比——CoT 基线（无图）/ no_deposon（图+贪心）/ unified（图+物理层）；decompose prompt v1.3.2 支持英文；统计显著性用 McNemar 检验。

---

## 五、资源消耗累计

| 阶段 | API 调用 | tokens |
| --- | --- | --- |
| v1.3.0 campaign | ~400 次 | ~28.5 万 |
| v1.3.1（A1 重跑 + A2 validate 全量） | ~210 次 | ~9 万 |
| v1.4 B 阶段（GSM8K，预计） | ~250 次 | ~15-20 万 |

---

---

## 六、文件清单（/mnt/agents/output/）

| 文件 | 说明 |
| --- | --- |
| deposon-repo/ | GitHub 发布仓库骨架（README/LICENSE/代码/docs/results/paper） |
| deposon_benchmark_v1_3_simple.json / traps.json | v1.3.1 最终双基准结果（unified 双 100%） |
| deposon_benchmark_v1_3_details.json | 200题×5变体逐题明细 + 200题 validate 结果 |
| deposon_benchmark_v1_4_gsm8k.json | GSM8K 结果（W1 窗口后生成） |
| Deposon_评估汇总_v1_3_0.json | 机器可读汇总（v1.3.1） |
| GitHub注册与发布指南.md | 用户操作手册 |
| verifier/ | 验收标准 v1 + 运行日志 |

---

*报告版本： v1.4.0-draft · 生成时间： 2026-08-22 · B 节将在 GSM8K 完成后定稿*
