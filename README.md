# Deposon (凝子) — Physics-Inspired Reasoning Layer for LLMs

> **将 LLM 作为认知振幅场的生成器，将 Deposon 统一场作为 LLM 推理的物理约束层。**

Deposon（凝子，Deposition + -on）是一个仿物理 AGI 推理框架：把 LLM 分解出的概念图节点绑定为“凝子态”（DeposonState），通过三通道散射（透射/反射/耗散）与无限维正交以太（EtherChannel，能量不可逆沉积）对推理路径进行物理约束筛选，从而阻断陷阱路径、保留正确推理链。

## 核心结果（v1.4.0）

### 合成基准（seed=42，100 题/集）
| 数据集 | no_deposon | unified | effect size |
|---|---|---|---|
| 简单 100 题 | 7% | **100%** | **+0.93** |
| 陷阱 100 题（表面关联误导） | 10% | **100%** | **+0.90** |

### 真实基准（如实报告，含负面结果）
| 基准 | CoT | unified | no_deposon | 统计 |
|---|---|---|---|---|
| GSM8K 100 题 | 97.0% | 85.0% | 2.0% | vs CoT p=4.9e-4；vs nodep p=4.4e-24 |
| StrategyQA 99 题 | 92.9% | 89.9% | 12.1% | vs CoT p=0.549（无显著差异）；vs nodep p=1.8e-16 |
| GSM8K SC@5 基线 | 96.0% | 85.0% | — | vs unified p=0.0034（SC@5 更优，如实报告） |

> **诚实声明**：合成基准效应量度量“同一张 LLM 分解图上物理层筛选 vs 贪心选路”的增量；真实基准上约束-保真权衡呈任务依赖性（GSM8K 长链上信息损失代价主导，StrategyQA 上与 CoT 打平）。分层分析（Table 11）证伪了“长链增量更大”预言并如实报告。详见 `paper/` 与 `results/`。

- 物理审计：幺正性 T+R+A 与 1 的偏差 ≤ 2.2e-16（四通道扩展 T+R+A+B=1 亦逐路径成立）。
- 95/95 回归测试（`tests/test_new_modes.py`）：四个条件等效断言（T→∞/K=1/δ=0/T→0 退化）实证通过。

## 快速开始

```bash
pip install numpy requests
export KIMI_API_KEY="your-key"   # 可选；不设置则自动使用规则引擎降级模式
```

```python
from deposon_agents_v1_3 import DeposonAgentSystem
system = DeposonAgentSystem(llm_backend=None, mode='unified')
result = system.reason("小明有5个苹果，给了小红2个，又买了10个，一共几个？", domain_hint='math')
print(result['best_path'], result['best_score'])
```

## 仓库结构

```
deposon_agents_v1_3.py / v1_4.py     # 核心系统（含 resonant/labelfree/arrhenius 扩展模式）
run_benchmark_v1_3.py                # 合成百题五变体消融
run_benchmark_v1_4_gsm8k.py          # GSM8K 100 题评测
run_benchmark_v1_4_strategyqa.py     # StrategyQA 99 题评测
run_g2_ensemble.py                   # G2 集成机制实验（重写可复现版）
svg_mindmap_ingest.py                # SVG 脑图摄入管线
tests/test_new_modes.py              # 95 项回归与条件等效测试
results/                             # 评测结果 JSON（details 大文件未入库，可复现）
docs/                                # 需求、验证报告、Roadmap_v1.5（凝子场扩散生成）
paper/                               # 论文（见下注）
verifier/                            # 终验清单 v1（check.py）
```

> **论文说明**：`paper/deposon_paper_v1.md`（中文版，v1.4.0 终版）在库；**英文终版（deposon_paper_v1_en.md）因 MCP 传输上限未镜像到本仓库**，中英双版的 docx/PDF 终版产物随 v1.4.0 交付渠道发布；如需英文 md 源文件请开 issue 联系维护者。仓库内中文 md 与英文版内容逐节对应（R4 评审 PASS）。

## 物理模型速查

```
t = 1/(1+g_eff+g_aether)   透射    r = g_eff/(1+g_eff+g_aether)   反射
a = g_aether/(1+g_eff+g_aether) 耗散（不可逆沉积到以太）
g_eff = g_couple/(1+detuning²)     共振增强（前置条件 g_couple,g_aether ≥ 0）
守恒: T+R+A=1（含势垒通道时 T+R+A+B=1，逐路径成立）
```

## 路线图

- [x] v1.2 统一场框架 + 向量化散射 + 持久缓存
- [x] v1.3 真实 LLM 后端 + 效应量根因修复 + validate 主环路
- [x] v1.4 真实基准（GSM8K/StrategyQA/SC@5）+ 双版论文 R4-PASS + G1-G3 算法扩展
- [ ] v1.5 凝子场扩散生成（Deposon Diffusion，见 docs/Roadmap_v1.5.md）+ 验证层改“独立复算比对”范式
- [ ] v2.0 硬件映射验证（PCM/MZI/ECM → 光子芯片）

## License

MIT — 见 [LICENSE](LICENSE)

> 注：`results/` 中的 details 大文件因托管载荷限制未入库，可由 run_benchmark 脚本结合本地缓存（`deposon_cache/`）完整复现。
