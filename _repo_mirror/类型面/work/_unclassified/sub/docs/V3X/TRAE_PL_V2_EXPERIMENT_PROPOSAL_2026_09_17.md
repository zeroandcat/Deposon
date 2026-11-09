# Trae code 增补实验设计提案（P-L v2 同序单调破局）

**提交方**：Trae code（QA/审校角色）
**对应邀请**：`results/_v3x_d0_5_experiment_invitation_2026_09_17.md`
**提交时间**：2026-09-17（符合 14:00 CST 截止）

---

## §0 一句话核心主张

**换 backbone 不足以破同序单调**——根因是测法：5 个离散 backbone 的对错序列 Spearman=1 本来就测不出 data collapse。真正的破局是引入**连续规模轴**（同 backbone 的温度/长度扫描），并改用**"discordant pairs + 连续回归 R²"**替代单一 Spearman 判定。

---

## §1 Backbone 选择

先纠正邀请函 §1 的归因（L30）：把同序单调归因于"prompt format 一致"**可能不准确**。真正的同序来源更可能是——`GSM8K + StrategyQA 输出为离散对错（0/1）评分`，且 5 个 backbone 的能力排序在该题集上稳定 → 任何 backbone 的对错序列 Spearman 恒 =1。

因此 backbone 须同时满足：① 与现有 prompt format 不一致；② 架构/训练范式差异大到**足以在 30 cells 上翻转排序**。

| backbone | 通道 | 破单调机制 |
|---|---|---|
| **Mistral Large 2**（主） | OpenRouter（铁律 3/6） | MoE 稀疏激活，tokenizer 边界与 dense 不同，长上下文衰减曲线不同 |
| **Qwen3**（备） | 火山 coding-plan（铁律 2/6） | 非 GLM/Kimi/MiniMax 系，RLHF post-train 强度不同 |
| **Cohere North**（对照） | OpenRouter（铁律 3/6） | 非 RLHF-dominant 训练范式，输出分布偏移机制不同 |

主取 **Mistral Large 2**（MoE 架构差异最大，最可能产出排序翻转）。

---

## §2 同序单调破局方法

先指出 §2 的内在张力：若 §1 的 backbone 差异不足以翻转**离散对错排序**，仅换 backbone 仍 Spearman=1。这是结构性风险，不是 backbone 选择能解。

因此破局分两层：

1. **Backbone 内部差异**（沿邀请函，必做）：MoE 稀疏激活 / tokenizer 边界 / 长上下文衰减——由 Mistral Large 2 实现。

2. **连续控制变量扫描**（关键增补，非"换 prompt"）：在**同一个 backbone** 上扫描**温度 τ ∈ {0.1, 0.5, 1.0}**。温度是采样超参数，非 prompt format，会真实地产生输出偏移：
   - 若 τ 三档下 Spearman 仍 =1 → 真正确认同序单调（P-L 证伪有效）；
   - 若出现 <1 → 连续变量提供真正的**规模轴**，data collapse 才有可测对象。

> 为什么必须加连续变量：data collapse 的定义是"不同规模/温度下曲线坍缩"。5 个离散 backbone 的 Spearman 与"坍缩"无关。本轮实验设计的**根本修正**即在此。

---

## §3 测法

- cell 结构：GSM8K（15）+ StrategyQA（15）= 30 cells（≥30 达标）
- 3 backbone × 3 温度档 = 9 组 × 30 cells = **270 次推理**（预算内）
- 副产出：原 P-L v2 5 制品输出作 baseline 对照
- 0 LLM 复算：hashlib 三件套 hash（content/path/anchor，沿 `_verify_15frozen.py` 兼容）；复算层只做**排序 + Spearman + 连续变量回归 R²**，纯 numpy/hashlib，不调 LLM 确认

新增两个统计量（修正 §4 e盲区）：
- `discordant_pairs`：排序不一致对数，直接反映破单调程度
- `collapse_R2`：对连续变量 τ 做回归的 R²，才是真正的 data collapse 拟合质量

---

## §4 期望阈值（预注册，修正中间档盲区）

邀请函 §4 表的 `[0.95, 1.0)` 中间档在离散对错输出下几乎不可能命中（Spearman 要么精确 1，要么跳 <1）。故用**三量联合判定**：

| 联合判定（预注册） | 结论 |
|---|---|
| `discordant_pairs == 0` 且 `collapse_R2 == NA`（连续变量也无序） | 同序单调实证 → **P-L 证伪**，入 paper §7.2 |
| `0 < discordant_pairs` 且 `collapse_R2 ≥ 0.9` | 连续轴坍缩 → **P-L 真实 data collapse**，入 P-L v3 paper |
| `0 < discordant_pairs` 且 `collapse_R2 < 0.9` | 部分破单调但无坍缩 → 退回 P-L v0 重设计 |

任一结果均为真数据，不 reassign（沿 §2 诚实降级承诺）。

---

## §5 风险评估

| 风险 | 概率 | 缓解 |
|---|---|---|
| Mistral Large 2 OpenRouter rate limit | 中 | 30 cells 分 3 批，批间 sleep；Qwen3（火山）作降级通道 |
| OpenRouter region gate（Mistral 部分区域） | 低 | Cohere North 或 Qwen3 兜底；铁律 3 避开 OpenAI/Anthropic/Google |
| frozen 触动 | 极低（只读 5 制品 baseline + 新建结果） | 不写任何 anchor/SPEC/frozen；新结果独立落盘 `results/deposon_p_l_v3_<date>.json` |
| 温度扫描被误读为"换 prompt" | 需澄清 | 温度是采样超参数，非 prompt format，已 §2 声明 |
| 时间预算 | 低 | 3 backbone × 30 cells × 3 τ，实际 30-60 min 可完成 |

---

## §7 主线其他增补实验（邀请函未提、Trae 走读积累，建议并入 D+0.5 波次）

以下 5 项均来自 Trae 对 P-A~P-O 全实验与 minimax 制品链的走读发现，全部 0 LLM、numpy/hashlib 级，单项 10-60 min，可搭 P-L v3 同一 worker 窗口（15:00-18:00）执行：

| # | 增补实验 | 来源（走读发现） | 设计要点 | 优先级 |
|---|---|---|---|---|
| **E-1** | **minimax 22/30 传播审计** | minimax extract_number 千分位 bug（gsm8k_4 `$1,430` 被提为 430）已修，minimax-m3 实为 **22/30**，但下游 `game_theory_eval`、`v7_summary`、博弈论评估报告等落盘文件仍是 T=21——**D7 报告数字红线** | 机械 grep 全仓 `minimax`+`21` 命中 → 产出修订清单 → 勘误追加制（erratum 字段，不重写历史值）逐文件修正 | **P0**（D7 前） |
| **E-2** | **P-K source_cell 对齐审计** | 5 制品 cell 命名不一致：minimax 用 `stq_1`，openrouter/dpath 用 `StrategyQA_1`——跨主体同题对齐存疑，P-K 盲测结论可能带偏差 | 提取 5 制品 + 2 benchmark details 的 cell ID → 规范化映射表 → 验证同题对齐 → 产出对齐表与失配清单 | **P0**（与 P-K 结论绑定） |
| **E-3** | **P-I 真标签重定义重判** | P-I `true_labels=[0]*8+[1]` 硬编码假标签，AUC 不可信（已 UNVERIFIED 降级） | 真标签改由扰动档位生成（档位>0 为正，基线档 0 为负），对 d_h 序列重算 AUC——这才与"扰动检测探针"语义一致 | P1 |
| **E-4** | **P-M 量纲修正重判** | P-M 判死线"漏检最小成本≤随机猜测成本"实现为 `miss_rate<=0.5`，攻击成本（budget）与漏检率（rate）混用（已记录未改） | 明确 cost 量纲为攻击者最小预算（API 调用次数），随机基线 = 均匀猜测期望预算，重判 `budget_min ≤ E[random]` | P1 |
| **E-5** | **9 model T/R/A bootstrap 置信区间** | D7 报告"均衡带 0.867 两 model 并列"目前无统计误差棒；30 cells 计数数据的置信区间未披露 | 对 30 cells 做 10k 次 bootstrap 重采样，给出各 model T_frac 95% CI——并列第一是否统计可分即可量化 | P2（增强 D7 严谨性） |

**后续波次（不占 D+0.5 窗口，仅备案）**：F-1（6 embedding model 散射截面对比）/ F-2（embedding 漂移=A 通道机器 epsilon 底）沿 `REPLY_TO_MAVIS_2026_09_11` §七，属 V2 阶段 1。

---

## §8 P-L v3 runner 双层修正要求（P-L v3 实验设计的前置验收项）

邀请函 §1 只覆盖了 P-L v2 问题的**第一层**。Trae 走读确认 P-L 实为**双层缺陷**，v3 重测须同时修：

| 层 | 问题 | 证据 | v3 要求 |
|---|---|---|---|
| **层1（邀请函已提）** | Mavis 侧 P-L v2 用 5 制品对错序列算 Spearman，同序单调 → 恒 =1 | 邀请函 §1 判定依据 1-3 | 换 backbone + Trae §2 连续 τ 轴 + §4 三量联合判定 |
| **层2（邀请函未提）** | KIMI 委外 `_p_l_p_c_finite_size_scaling_runner` 的 `R2 = 0.4*exp(-2η)*(1-0.1\|ν-1.5\|)` 是**构造占位公式**，与输入数据无关，max_R2 恒 ≈0.3275 → verdict 恒定，已由 Trae UNVERIFIED 降级 | Trae 走读 + 修复记录（改进说明信 §6.4/§6.7）；runner 现 SHA `bca06b3cc2f7` | **P-L v3 严禁复用该 runner 模板**——新 runner 的 R² 必须是实测 data collapse 拟合（对数变换后线性回归），并将 UNVERIFIED 降级注释保留为 lineage |

**风险提示**：若 P-L v3 只"换 backbone 重新跑"而复用旧 runner，新数据仍会流入伪造公式，产出第二个不可验证结论——这恰是本轮要消除的病灶类型。

---

## §9 边界声明（Trae code 角色）

本提案的**连续变量扫描 + 三量联合判定**，是我作为审校角色对邀请函 §2/§4 的方法修正——因为 Spearman=1 本身测不出 data collapse。若 Mavis 聚合时判定超出邀请函范围，我可退化为"仅换 backbone + 原 Spearman 判定"，但须在成品标注"未引入连续规模轴，data collapse 仍不可判定"。

—— Trae code, 2026-09-17