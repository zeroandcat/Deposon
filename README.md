# Deposon (凝子) — Physics-Inspired Reasoning Layer for LLMs

> **将 LLM 作为认知振幅场的生成器，将 Deposon 统一场作为 LLM 推理的物理约束层。**

Deposon（凝子，Deposition + -on）是一个仿物理 AGI 推理框架：把 LLM 分解出的概念图节点绑定为"凝子态"（DeposonState），通过三通道散射（透射/反射/耗散）与无限维正交以太（EtherChannel，能量不可逆沉积）对推理路径进行物理约束筛选，从而阻断陷阱路径、保留正确推理链。

## 核心结果（v1.3.1，合成百题基准，seed=42）

| 数据集 | no_deposon | unified | effect size |
|---|---|---|---|
| 简单 100 题 | 7% | **100%** | **+0.93** |
| 陷阱 100 题（表面关联误导） | 10% | **100%** | **+0.90** |

- 物理审计：幺正性 t+r+a 与 1 的偏差 < 2.3e-16；v1 极限零耗散、v2 极限强耗散、unified 适度耗散，三极限态与理论预测一致。
- LLM 后端：真实 Kimi API（kimi-for-coding），规则引擎自动降级，持久化缓存（百题评测缓存命中率 100%）。
- v1.2 → v1.3 关键修复：效应量恒 0 的两个根因（答案与散射筛选脱钩；陷阱节点为 BFS 不可达死胡同）——详见 `docs/Deposon_v1_3_验证报告.md`。

> **诚实声明**：合成基准的效应量度量的是"同一张 LLM 分解图上，物理层筛选 vs 贪心选路"的增量价值。与 LLM 本体（CoT 基线）的对比实验在真实 GSM8K 子集上进行，结果见 `results/`（持续更新中）。

## 快速开始

```bash
pip install numpy requests
export KIMI_API_KEY="your-key"   # 可选；不设置则自动使用规则引擎降级模式
python3
```

```python
from deposon_agents_v1_3 import DeposonAgentSystem, BenchmarkEvaluator

system = DeposonAgentSystem(llm_backend=None, mode='unified')   # 无key时规则引擎
result = system.reason("小明有5个苹果，给了小红2个，又买了10个，一共几个？", domain_hint='math')
print(result['best_path'], result['best_score'])
print(result['deposon_stats']['ether_dissipated'])   # 以太耗散能量

# 五变体消融
ablation = system.ablation_study("...", domain_hint='math')
print(system.report_ablation(ablation))
```

## 仓库结构

```
deposon_agents_v1_3.py     # 核心系统（DeposonState / EtherChannel / DeposonField /
                           #   DeposonAgentSystem / LLMBackend / BenchmarkEvaluator）
run_benchmark_v1_3.py      # 百题五变体消融 runner
results/                   # 评测结果 JSON（含逐题明细引用）
docs/                      # 需求文档、验证报告
paper/                     # 论文（撰写中）
```

## 物理模型速查

```
t = 1/(1+g_eff+g_aether)   透射    r = g_eff/(1+g_eff+g_aether)   反射
a = g_aether/(1+g_eff+g_aether) 耗散（不可逆沉积到以太）
g_eff = g_couple/(1+detuning²)     共振增强
守恒: E_final + E_reflected + E_dissipated = E_0
```

## 路线图

- [x] v1.2 统一场框架 + 向量化散射 + 持久缓存
- [x] v1.3 真实 LLM 后端 + 效应量根因修复 + validate 主环路
- [ ] v1.4 真实 GSM8K 基准 + CoT 基线对照（进行中）
- [ ] v1.5 节点共轭映射激活（v2 隧穿价值验证）
- [ ] v2.0 硬件映射验证（PCM/MZI/ECM → 光子芯片）

## License

MIT — 见 [LICENSE](LICENSE)
