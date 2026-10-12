# Deposon v1.3 完整参数表（论文附录 C 用）

来源：`deposon_agents_v1_3.py`（high_couple 修复后版本），行号对应该文件。

## C.1 散射动力学（DeposonState.scatter, :60-70）

入射能量 E_in 经单节点散射为三通道，严格守恒 t+r+a=1（审计最大偏差 2.2e-16）：

- 失谐 detuning = |E_in − resonance_energy|
- 共振因子 resonance_factor = 1 / (1 + detuning²)（Feshbach 型 Lorentzian）
- 有效耦合 g_eff = g_couple × resonance_factor
- 分母 denom = 1 + g_eff + g_aether
- **t（透射）= 1/denom；r（反射）= g_eff/denom；a（耗散）= g_aether/denom**

## C.2 类型 → (g_couple, g_aether) 绑定（spawn_from_graph, :1107-1117）

| 节点类型 | g_couple（基础） | g_aether | 备注 |
|---|---|---|---|
| trap | 5.0 | 0.0 | 强反射阻断诱饵路径 |
| answer（Goal） | 0.05 | 0.05 | |
| operation | 0.3 | 0.2 | |
| number / 其他（concept） | 0.05 | 0.05 | DeposonField 默认值 |

**degree 修正（:1118-1119）**：绑定后 `g_couple *= (1 + 0.02 × degree)`，
degree 为与该节点相连的边数（无向计数）；g_aether 不做 degree 修正。

## C.3 节点 resonance_energy（energy）赋值规则

| 节点 | energy | 出处 |
|---|---|---|
| 第 i 个 number（i 从 0） | 0.3 + 0.05·i | :706（LLM 建图）/ :967（规则建图） |
| operation（OP） | 0.4 | :709 / :969 |
| answer（Goal） | 0.0 | :710 / :970 |
| LLM 语义陷阱 / 通用错误运算陷阱 | 0.1 | :766 |
| Trap_Order（顺序陷阱） | 0.12 | :775 |
| Trap_DeadEnd（死胡同） | 0.1 | :784 |
| 规则引擎 Trap_Surface | 0.15 | :1003 |
| 缺省 | 0.5 | spawn_from_graph :1108 |

散射时该节点的 photon_energy 取其自身 energy（process_path :1145）。

## C.4 路径命运与通过阈值（process_path :1164, _process_sequential :1268）

| 判定 | 条件 |
|---|---|
| fate = blocked | max_i r_i > **0.7** |
| fate = tunneling | 否则 max_i a_i > **0.5** |
| fate = transmitted | 其余 |
| passed（候选可参与答案选取） | final_score > **0.1** |
| **final_score** | = 路径级 transmitted = ∏ᵢ tᵢ（path_energy=1.0 归一） |

答案选取：passed 候选按 final_score 降序（稳定排序）取第 1 条；无 passed 时取全体最高分。
正确性容差 |pred − gold| < 0.01。

## C.5 概念图边权（_build_from_llm_spec :714-786）

| 边 | weight | migration_barrier |
|---|---|---|
| N1/N2 → OP1 | 0.6 | 0.3 |
| OPᵢ → OPᵢ₊₁（多步链） | 0.7 | 0.2 |
| Nᵢ₊₁ → OPᵢ（链中间数字汇入） | 0.6 | 0.3 |
| OP_last → Goal | 0.8 | 0.2 |
| N1 → 陷阱（语义/错误运算，≤3 条） | 0.9 | 0.1 |
| N1 → Trap_Order | 0.85 | 0.1 |
| N1 → Trap_DeadEnd | 0.8 | 0.1 |
| 陷阱 → Goal | 0.55 | 0.3 |

路径搜索：BFS，邻居按 weight 降序、每节点取 top-8（v1.3 由 4 改 8），候选上限 = n_candidates×3 = 30。

## C.6 五变体模式差异（spawn_from_graph :1126-1136；_process_sequential :1250-1270）

| 变体 | use_deposon | 参数变换（在类型绑定+degree 修正之后施加） | 效果 |
|---|---|---|---|
| no_deposon | False | —（绕过场） | 所有路径 final_score=1.0 并列，按 BFS 顺序取首条 |
| v1_blocking | True | 所有节点 g_aether ← 0 | 纯阻塞/反射，无耗散 |
| v2_tunneling | True | 所有节点 g_aether ← max(g_aether, 2.0)，g_couple ← min(g_couple, 0.5) | 强耗散隧穿主导 |
| unified | True | 不变（C.2 绑定原样） | 反射+耗散混合 |
| high_couple（修复后） | True | 所有节点 g_couple ×3，g_aether 不变 | 高耦合极限（修复前误映射为 v1_blocking 的别名，已修复） |

## C.7 运算语义（_apply_op :1395-1406）

addition/subtraction/multiplication/division（除零返回 None）；
percentage：a × (b/10 若 b≤10 否则 b/100)（"打八折"=×0.8）。
多步链 fold_chain：首个运算取两个操作数，后续以累加器 op 下一操作数推进；
命中陷阱节点即应用陷阱对应错误运算并终止。
