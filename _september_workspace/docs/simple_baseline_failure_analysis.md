# M4 根因分析：simple 集 no_deposon 基线仅 7% 准确率的机制解释

- 数据集：HundredQuestionBenchmark（100 题，seed=42，单步算术，无陷阱语义设计）
- 变体：no_deposon（`use_deposon=False`，绕过 Deposon 场，纯贪心游走）
- 数据来源：`deposon_benchmark_v1_3_details.json`（high_couple 修复后重跑版，no_deposon 变体不受该修复影响，与修复前逐题一致）
- 分析全程零 API 消耗（仅读缓存分解结果 + 本地重放）

## 1. 总体数据

| 指标 | 数值 |
|---|---|
| no_deposon 准确率 | 7/100 = 7% |
| 失败案例数 | 93 |
| 失败案例中 best_score 全为 1.0（并列） | 93/93 |
| 失败案例中候选路径数 = 4 | 93/93 |
| 失败案例中正确 OP 路径在候选中排名第 4（最后） | 93/93 |
| 失败案例命中陷阱节点 | 93/93（`Trap_surface_addition` 61、`Trap_surface_subtraction` 29、`Trap_surface_multiplication` 3） |
| 失败案例 best_path 形态 | 全部为 `N1 -> Trap_* -> Goal`（长度 3） |
| 失败案例 decompose 来源 | 全部 kimi_api 缓存（图结构正常，数字提取无误） |

**走向分类结论**：93 个失败案例 100% 属于"被诱饵边权重误导 + 分数并列时按 BFS 顺序取首条"这一类；
不存在"走到错误类型数字节点"或"图中缺少正确路径"的情况（正确 OP 路径始终存在于候选集中，只是排最后）。

## 2. 机制链条（以代码实际逻辑为准）

1. **no_deposon 下所有路径同分**：`DeposonAgentSystem._process_sequential`（deposon_agents_v1_3.py:1263-1267）
   在 `use_deposon=False` 分支直接给每条候选路径 `final_score = 1.0`，没有任何物理区分度。
2. **稳定排序保持 BFS 发现顺序**：`reason()` 中 `processed.sort(key=final_score, reverse=True)`（:1229）
   是稳定排序，全部 1.0 并列时维持原列表顺序，即 BFS 完成顺序。
3. **BFS 按边权重降序扩展邻居**：`_generate_paths`（:1323）`neighbors.sort(key=weight, reverse=True)`。
4. **陷阱边权重被人为设为高于正确边**：`_build_from_llm_spec`（:741-742 注释明写
   "权重 0.9 > 正确边0.6, 使 no_deposon 的贪心游走被陷阱捕获"）——
   `N1->Trap_*` 权重 0.9、`N1->Trap_DeadEnd` 权重 0.8、`N1->OP1` 权重仅 0.6。
5. 因此 BFS 最先完成的路径恒为 `N1 -> Trap_* -> Goal`（acc_weight=0.9+0.55-0.1-0.3=1.05），
   正确链 `N1 -> OP1 -> Goal`（acc_weight=0.6+0.8-0.3-0.2=0.90）恒排第 4。
   `evaluate_math` 取 `passed_candidates[0]`（全部 pass），即陷阱路径。
6. 陷阱路径在 `_compute_answer_from_path` 中应用错误运算（如把"剪去"算成加法），答错。

**7 个"答对"案例也并非基线真正会做题**：全部是除法题中陷阱的"错误运算"恰好等于正确运算
（5 例命中 `Trap_wrong_order`，单步运算链反转后不变；2 例命中 `Trap_surface_division`，
而正确运算本来就是除法）。即 no_deposon 的真实解题能力为 **0/93（非巧合题）**。

## 3. 代表性失败案例（完整路径链）

### 案例 1：`一条绳子长8米，剪去7米，还剩多少米？`（gold=1，pred=15）

N1 出边（BFS 按 weight 降序扩展）：

| 邻居 | weight |
|---|---|
| Trap_surface_addition | 0.9 |
| Trap_WrongOp_addition | 0.9 |
| Trap_WrongOp_multiplication | 0.9 |
| Trap_DeadEnd | 0.8 |
| OP1（正确：subtraction） | 0.6 |

候选路径（评测排序后顺序 = BFS 完成顺序，全部 final_score=1.0）：

| rank | 路径 | final_score | acc_weight | 备注 |
|---|---|---|---|---|
| 0 | N1→Trap_surface_addition→Goal | 1.0 | 1.05 | **被选中**，应用加法 8+7=15 |
| 1 | N1→Trap_WrongOp_addition→Goal | 1.0 | 1.05 | |
| 2 | N1→Trap_WrongOp_multiplication→Goal | 1.0 | 1.05 | |
| 3 | N1→OP1→Goal | 1.0 | 0.90 | 正确路径（8-7=1），排最后 |

### 案例 2：`一支笔79元，买27支要多少钱？`（gold=2133，pred=106）

| rank | 路径 | final_score | acc_weight | 备注 |
|---|---|---|---|---|
| 0 | N1→Trap_surface_addition→Goal | 1.0 | 1.05 | **被选中**，79+27=106 |
| 1 | N1→Trap_WrongOp_addition→Goal | 1.0 | 1.05 | |
| 2 | N1→Trap_WrongOp_subtraction→Goal | 1.0 | 1.05 | |
| 3 | N1→OP1→Goal | 1.0 | 0.90 | 正确路径（79×27=2133），排最后 |

### 案例 3：`小明有47个苹果，给了小红6个，还剩几个？`（gold=41，pred=53）

| rank | 路径 | final_score | acc_weight | 备注 |
|---|---|---|---|---|
| 0 | N1→Trap_surface_addition→Goal | 1.0 | 1.05 | **被选中**，47+6=53 |
| 1 | N1→Trap_WrongOp_addition→Goal | 1.0 | 1.05 | |
| 2 | N1→Trap_WrongOp_multiplication→Goal | 1.0 | 1.05 | |
| 3 | N1→OP1→Goal | 1.0 | 0.90 | 正确路径（47-6=41），排最后 |

## 4. 结论（对审稿人质疑的如实回应）

no_deposon 仅 7% **不是**因为简单题本身难，也不是 BFS 找不到正确路径（正确路径 100% 在候选集中），
机制是三个设计叠加的必然结果：

1. **评分退化**：no_deposon 分支令所有路径 final_score=1.0，选择完全退化为 BFS 顺序；
2. **BFS 贪心按边权重排序**；
3. **诱饵边权重（0.9）被人为设定高于正确链边（0.6）**——源码注释明确写明目的是
   "使 no_deposon 的贪心游走被陷阱捕获"。

因此必须诚实承认：**7% 这个对照数字确实带有"反向设计"成分**——图构造阶段故意让贪心基线
必然踩坑，以凸显 Deposon 场的阻断效果。它衡量的是"无物理层时贪心遍历在该图构造下的表现"，
不应作为"通用贪心基线在简单算术上的能力"来引用。审稿人质疑成立，建议在论文中将该基线
表述为 "greedy BFS on the constructed concept graph (with adversarially weighted decoy edges)"，
并补充任务 B 的 uniform-params 消融（10%，与 no_deposon 持平）作为更中性的对照：
即使保留 Deposon 动力学、仅去掉类型化参数绑定，基线同样失效，说明效应来自
"标签 × 动力学"的组合而非单纯的图遍历顺序。
