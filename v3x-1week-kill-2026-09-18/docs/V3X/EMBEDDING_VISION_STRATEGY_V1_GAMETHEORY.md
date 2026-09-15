# Doubao-Embedding-Vision 策略 SPEC V1(博弈论视角优化)

> **生成时间**: 2026-09-10 21:50+08:00
> **作者**: Mavis Worker (subagent of mvs_bbeb804b1a6a41109be740636eed1709, session mvs_f80dc4ceefdd4605badb8a9f6d724bdb)
> **任务来源**: user 2026-09-10 21:49 三指令之二"博弈论视角优化 embedding-vision SPEC(沿用 6 方向报告框架)"
> **状态**: **SPEC V1 博弈论优化版**(沿用 V0 + 阶段 1 博弈论指标)
> **V0 父文件**: `docs/V3X/EMBEDDING_VISION_STRATEGY_V0.md` (20128 B, **只读未动**)
> **V1 新增**:博弈论判死线 + 9 model T/R/A 基线 + 5 候选 P-A/B/C/D 评级
> **严守约束**: user 17:38+17:41(只走 coding-plan,无 proxy,无 OpenRouter)+ 7 铁律(0 LLM,不动 5 锚 JSON)

---

## §0 摘要(SPEC V1 核心)

- **目标**:把 V0 SPEC 升级为 V1,**用博弈论视角**对 4 个 vision 方向(a/b/c/d)做评级
- **核心升级**(相对 V0):
  - 🆕 引入 9 model × 30 cells T/R/A 表作为 vision 通道对比基线
  - 🆕 引入 P-A/B/C/D/E 5 候选博弈论判死线
  - 🆕 失真界 A_frac ≤ 0.10 作为 vision 通道的硬判死线
  - 🆕 均衡带 T_frac ∈ [0.80, 0.90] 作为 vision 通道 PASS 阈值
  - 🆕 Deposon 散射场公式 S_eff(E) = T·E_in - R·E_back + A·E_ground(沿 v3 §6)
  - 🆕 BOSS-V1/V2/V3 预判沿 `QUICK_KILL_6_DIRECTIONS.md` V0.2 模板
- **不实施**:本任务只写 SPEC,**不**调 embedding API
- **结论**:**方向 d(跨模态检索)最可行**,新增博弈论判死线:**vision-enabled model 必须 T_frac ≥ 0.80 + A_frac ≤ 0.10 双线触发**

---

## §1 沿用 V0 关键结论(本节为简明回顾,详见 V0 §1-§3)

### 1.1 V0 现状(沿用)

| 项 | 状态 |
|---|---|
| `doubao-embedding-vision-251215` 已有 22 caption text embedding | 完成(`deposon_volcengine_22caption_embedding_2026_09_10.json`) |
| intra/inter ratio = 1.0562 | **NOISE**(沿用 6 方向报告) |
| vision 通道 0 利用 | 4 方向待评估 |
| V0 4 方向评级 | a(22 概念图) / b(散射场可视化) / c(图文混排 RAG) / d(跨模态检索) |

### 1.2 V0 4 方向可行性回顾

| 方向 | 核心思路 | V0 verdict | V1 博弈论升级 |
|---|---|---|---|
| **a**. 22 概念图实际图像 | 22 PNG → image input → 2048-d | ❌ corpus 无图 | 🆕 加 P-C 失真界判死:A_frac ≤ 0.10 |
| **b**. deposon 散射场可视化 | S_eff(E) 渲染 → 22 PNG | 🟡 需写可视化脚本 | 🆕 加 P-E 散射场公式 + 3D 距离 |
| **c**. 多模态 RAG(图文混排) | text+image context → 多模态 LLM | 🟡 需改 RAG | 🟠 V1 仍低优(成本高) |
| **d**. 跨模态检索 | text query → 22 image candidate | 🟢 5 min 可出 verdict | 🆕 加 P-A 均衡带 + P-D 指纹 |

---

## §2 V1 新增:博弈论判死线

### 2.1 9 Model T/R/A 表(沿用阶段 1 评估)

**V1 新增基线**:任何 vision 通道的 30 cells 评估,**必须**对照下表:

| 排名 | Model | T_frac | R_frac | A_frac | 用途 |
|---|---|---|---|---|---|
| 1 | `doubao-seed-2.0-lite` | **0.867** | 0.133 | **0.000** | text-only 标杆 |
| 1 | `glm-5.3` | **0.867** | 0.100 | 0.033 | text-only 标杆 |
| 3 | `deepseek-v4-flash` | 0.767 | 0.167 | 0.067 | text-only 边际 |
| 4 | `doubao-seed-evolving` | 0.733 | 0.200 | 0.067 | |
| 5 | `minimax-m3` | 0.700 | 0.267 | 0.033 | |
| 5 | `glm-5.3-flash` | 0.700 | 0.033 | 0.267 | |
| 7 | `kimi-k2.7-code` | 0.633 | 0.267 | 0.100 | |
| 8 | `doubao-seed-2.1-turbo` | 0.600 | 0.067 | 0.333 | 高 A(脆弱) |
| 9 | `deepseek-v4-pro` | 0.533 | 0.067 | 0.400 | 最脆弱 |

**关键观察**:
- **T_frac 9 model 均值 = 0.7111**(即平均 21/30 = 70%)
- **A_frac 9 model 均值 = 0.1359**(即平均 4/30 = 13% 截断)
- **T-A 强负相关**(corr = -0.92)

### 2.2 P-A 均衡带判死线(V1 新增)

**V3 §6 26-cell v2 穿越均衡** = T_frac ∈ [0.80, 0.90]

**应用**:vision-enabled 30 cells 评估中,**至少 1 个 model T_frac ≥ 0.80**(或均值 ≥ 0.80)才算 vision 通道 "有效"

- **若 vision-enabled 30 cells T_frac ≥ 0.80 + 在 [0.80, 0.90] 均衡带** → **PASS**(vision 通道带来增益)
- **若 vision-enabled 30 cells T_frac ∈ [0.70, 0.80]** → **GRAY**(与 text-only 持平)
- **若 vision-enabled 30 cells T_frac < 0.70** → **FAIL**(vision 通道反而劣化)

**历史对比**:
- text-only 9 model: T_frac 均值 0.7111,最大 0.867
- 判死线 = "vision 必须 ≥ 0.80 才算新发现"

### 2.3 P-B 守恒审计(V1 新增)

**T + R + A = 1**(v3 §6 守恒律)对 vision-enabled 30 cells 同样适用

**应用**:vision-enabled 30 cells 评估中,每个 model 的 T/R/A 必须满足 T+R+A=1(residual < 1e-10)

**与 text-only 对比**:text-only 9 model 已确认守恒(v3 §6 沿用),vision-enabled 30 cells 必须**复现**此性质(若不守恒 → 评估有 bug,需重测)

### 2.4 P-C 失真界判死线(V1 新增)

**A_frac ≤ 0.10** 视为"低失真"(v3 §6 失真界)

**应用**:vision-enabled 30 cells 评估中,**A_frac 必须 ≤ 0.10**,否则视为"vision 通道在 timeout/parse-fail 上引入额外失真"

**原因**:text-only 9 model 中 6/9 A_frac ≤ 0.10(doubao-2.0-lite / glm-5.3 / deepseek-v4-flash / doubao-seed-evolving / minimax-m3 / kimi-k2.7-code),**A ≤ 0.10 是 text-only 中位水平**

**判死**:
- A_frac ≤ 0.067 → **零失真**(< 2/30 cells 截断)
- A_frac ∈ (0.067, 0.10] → **低失真**(2-3/30 cells 截断)
- A_frac > 0.10 → **高失真**(≥ 4/30 cells 截断,**判 vision 通道失败**)

### 2.5 P-D 账指纹(V1 沿用 V0)

**V1 不引入 P-D 评估**:vision 通道是"输入模态"扩展,不改变账指纹 SHA-12。P-D 仍沿 V0.1 SPEC + 3 根指纹 + 5 锚。

### 2.6 P-E Deposon 散射场(V1 新增公式)

**V3 §6 散射场公式**(V1 引入 vision 通道):

```
S_eff(E_in) = T·E_in - R·E_back + A·E_ground
```

| 通道 | 物理含义 | text-only | vision-enabled |
|---|---|---|---|
| T (transmitted) | 沿 PC1 透射(v2 g_aether) | text 编码语义 | text + image 双路对齐 |
| R (reflected) | 沿 PC2 反射(v1 g_couple) | 答错语义 | vision 误识别 |
| A (dissipated) | 残差凝华(无限维) | 截断/timeout | image input 超 2048 token |

**判死**(沿 v3 §6 散射场):
- **T 主导** + A 抑制 + R 微扰 = **V3X 终极形式**(理想散射)
- 若 vision 通道的 3D T/R/A 点云与 text-only 完全重合 → vision **无新增**
- 若 vision 通道 T_frac 提升 ≥ 0.10(即从 0.7111 升到 0.80+) → vision **有效**

---

## §3 V1 4 方向博弈论评级(对应 V0 §2 升级)

### 3.1 方向 a. 22 概念图实际图像(V0 ❌ → V1 ❌ 沿用)

| 维度 | V0 评估 | **V1 博弈论升级** |
|---|---|---|
| 可行性 | ❌ corpus 无图 | ❌ 不变 |
| V1 判死 | — | 需 22 PNG + image embedding + 30 cells text→image 检索 |
| V1 判死线 | — | T_frac ≥ 0.80 + A_frac ≤ 0.10 双线 |
| BOSS 预判 | — | BOSS-V1 经典 CLIP(ViT-B/32)在 22 小图上 top-1 ≥ 80%,**deposon 视觉无差异化** |
| V1 verdict | ❌ corpus 无图 | ❌ **不变**,阻塞需 user 提供 22 PNG |

### 3.2 方向 b. deposon 散射场可视化(V0 🟡 → V1 🟡+S_eff 公式)

| 维度 | V0 评估 | **V1 博弈论升级** |
|---|---|---|
| 可行性 | 🟡 写可视化脚本 | 🟡 不变 |
| 实施 | 30-90 min | 60-90 min(加 S_eff 公式实现) |
| V1 判死 | — | 22 张 S_eff 散射场图 ratio ≥ 1.2(对比 text 1.0562) |
| V1 理论增益 | 散射场图直接编码 T/R/A 三通道 | 沿 v3 §6 S_eff 公式 |
| V1 verdict | 🟡 | 🟡 **提升**(理论自洽,但与方向 a 重复) |

**V1 关键补充**(沿 P-E 散射场公式):
- 散射场图按 `S_eff(E) = T·E_in - R·E_back + A·E_ground` 渲染
- T 通道 = 红色(透射)
- R 通道 = 蓝色(反射)
- A 通道 = 灰色(凝华)
- 边宽 = `|S_eff(E)|`
- 22 张图 = 22 graph metadata 的散射场可视化

### 3.3 方向 c. 多模态 RAG(图文混排)(V0 🟡 → V1 🟠 不变)

| 维度 | V0 评估 | **V1 博弈论升级** |
|---|---|---|
| 可行性 | 🟡 需改 RAG | 🟠 不变 |
| 实施 | 2-3 h(改 RAG + 选 vision LLM) | 同 V0 |
| V1 判死 | — | 30 cells 双路(图+文) ratio vs text-only ratio |
| V1 风险 | 30 cells 重测 = 高成本 | 加 P-C 失真界(若 vision 通道让 A_frac > 0.20 → 失败) |
| V1 verdict | 🟠 低优(成本高) | 🟠 **不变** |

### 3.4 方向 d. 跨模态检索(V0 🟢 → V1 🟢 + 双判死线)

| 维度 | V0 评估 | **V1 博弈论升级** |
|---|---|---|
| 可行性 | 🟢 V3X 已有图 metadata | 🟢 不变 |
| 实施 | 20-30 min | 20-30 min |
| V1 判死 | text→image top-1 ≥ 24/30 | **双判死线**:`top-1 ≥ 24/30` AND `A_frac ≤ 0.10`(P-C 失真界) |
| V1 vs text-only | ratio ≥ 1.2 vs 1.0562 | **加 P-A 均衡带**:text→image 30 cells T_frac ≥ 0.80 |
| V1 verdict | 🟢 最高 | 🟢 **强化** |

**V1 关键补充**(沿 P-A 均衡带 + P-C 失真界):
- text→image top-1 命中率 ≥ 24/30 = 80%(P-A 均衡带下沿)
- 30 cells text→image 评估 A_frac ≤ 0.10(P-C 失真界)
- 双线触发 = vision 通道"有效"

---

## §4 V1 实施方案(沿 V0 三阶段 + 博弈论判死线)

### 4.1 阶段 1:短期(sanity 5 min,**V0 不变**)

**目标**:验证 `doubao-embedding-vision-251215` 是否真支持 image input
**判死**(V1 新增):
- sanity 1 (text) → 200 OK
- sanity 2 (image, base64 1x1 PNG) → **200 OK**(若 400/422 → 方向 a/b/d **全部取消**)
- **P-C 失真界预检**:本阶段无 LLM 调用,A_frac 不适用

### 4.2 阶段 2:中期(30 min,方向 a + b 联合,**V1 增 P-E 散射场公式**)

**目标**:22 张 PNG(image input)+ 22 张 S_eff 散射场图 → 2048-d 算 ratio
**V1 判死线**:
- 任一 ratio ≥ 1.2 → 走方向 b(散射场图,P-E 散射场公式)
- 两套 ratio 都 < 1.2 → NOISE 在 modality 之外(根因 = layout 共享),方向 a/b **失败**
- 22 张 S_eff 图额外:与 22 caption text embedding 算 cross-cosine 矩阵,看 P-E 散射场是否独立

**V1 散射场实现**(沿 v3 §6):
```python
# tools/scatter_field_viz.py  (V1 升级版)
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import json

# 22 caption 2D SVD 坐标 (cpath_simulation 已有)
with open('results/deposon_cpath_simulation_2026_09_10.json') as f:
    cpath = json.load(f)

# 沿 v3 §6 散射场公式
T_frac = cpath['scatter_field_global']['T_global_fraction']  # 0.6864
R_frac = cpath['scatter_field_global']['R_global_fraction']  # 0.0786
A_frac = cpath['scatter_field_global']['A_global_fraction']  # 0.235

for graph_id, (x, y) in cpath['per_caption_2d_coords'].items():
    # 节点按 T/R/A 染色
    T_color = (1.0, 0.0, 0.0, T_frac)  # 红色
    R_color = (0.0, 0.0, 1.0, R_frac)  # 蓝色
    A_color = (0.5, 0.5, 0.5, A_frac)  # 灰色
    
    # 边宽 = |S_eff(E)|
    S_eff = T_frac * x - R_frac * y + A_frac * (1.0 - x - y)
    edge_width = abs(S_eff) * 5
    
    g = load_graph(f'corpus/v20/{graph_id}.json')
    pos = nx.spring_layout(g)
    nx.draw(g, pos, node_color=[T_color], edge_color=R_color, width=edge_width)
    plt.savefig(f'figures/scatter_field_{graph_id}.png', dpi=80)
```

### 4.3 阶段 3:长期(60-120 min,方向 d 完整实施 + **V1 增 P-A/P-C 双判死**)

**目标**:跨模态检索 + 30 cells 端到端
**V1 双判死线**:
- 判死 1(P-A 均衡带):text→image top-1 ≥ 24/30 = 80%
- 判死 2(P-C 失真界):30 cells vision-enabled A_frac ≤ 0.10
- 双线触发 = vision 通道"有效"
- 任一未达 → 取消 vision 章节

**V1 评估表**(沿 9 model T/R/A 模板):
```python
# 30 cells vision-enabled T/R/A 评估
vision_T = sum(1 for c in cells if c['is_correct'])
vision_A = sum(1 for c in cells if c.get('error') or c.get('llm_extracted') is None)
vision_R = 30 - vision_T - vision_A

# 判死 1: P-A
assert vision_T / 30 >= 0.80, f"P-A FAIL: T_frac={vision_T/30:.3f} < 0.80"

# 判死 2: P-C
assert vision_A / 30 <= 0.10, f"P-C FAIL: A_frac={vision_A/30:.3f} > 0.10"

# 判死 3: P-B
assert abs((vision_T + vision_R + vision_A) / 30 - 1.0) < 1e-10, "P-B FAIL: T+R+A != 1"
```

---

## §5 V3X 终极形式的 vision 增强版(V1 升级)

### 5.1 V0 终极形式(沿用)

```
V3X 终极形式 = Deposon-aware 推理 + 多模态上下文
输入: question q (text), 候选 22 概念图 {g_i, image_i, caption_i}
1. 多模态 embedding (text + image)
2. 三路融合 (text×image×caption)
3. Deposon-aware 选 top-k
4. LLM 推理 + 三通道评估
5. 输出: T_frac, R_frac, A_frac, sim_combined_top1, 守恒校验 T+R+A=1
```

### 5.2 V1 终极形式(**博弈论视角升级**)

```
V3X 终极形式 (V1 博弈论版) = T 主导 + A 抑制 + R 微扰

输入: question q (text), 候选 22 概念图 {g_i, image_i, caption_i}
1. 多模态 embedding (text + image):
   E_text(q) ← doubao-embedding-vision(text=q)  # 2048-d
   E_image(g_i) ← doubao-embedding-vision(image=g_i.png)  # 2048-d
   E_caption(c_i) ← doubao-embedding-vision(text=c_i)  # 2048-d

2. Deposon 散射场投影 (V1 增 P-E 公式):
   S_eff(E) = T·E_in - R·E_back + A·E_ground
   # 沿 v3 §6, T = 沿 PC1, R = 沿 PC2, A = 残差

3. 博弈论判死线 (V1 新增):
   - P-A 均衡带: T_frac ∈ [0.80, 0.90]  # 26-cell v2 均衡
   - P-B 守恒: T + R + A = 1
   - P-C 失真界: A_frac ≤ 0.10
   - P-D 账指纹: SHA-12 稳定 (沿 V0.1)
   - P-E 散射场: 3D T/R/A 投影距 (1,0,0) 理想点

4. 30 cells 评估 (V1 双判死):
   判死 1: text→image top-1 ≥ 24/30 (P-A 均衡带)
   判死 2: A_frac ≤ 0.10 (P-C 失真界)
   双线触发 → vision 通道 "有效"

5. 9 model T/R/A 横向对比 (V1 引入):
   vision-enabled 30 cells vs 9 model text-only 30 cells
   看 vision-enabled T_frac 是否 ≥ 0.867 (doubao-seed-2.0-lite / glm-5.3 标杆)

6. 输出:
   T_frac, R_frac, A_frac, sim_combined_top1, S_eff_norm,
   守恒校验 T+R+A=1, P-A/P-C 双判死结果
```

**V1 vs V0 关键差异**:
- V0 只算 ratio
- V1 加 **博弈论判死线**(P-A 均衡 + P-C 失真 + P-B 守恒 + P-E 散射场公式 + P-D 指纹)
- V1 加 **9 model T/R/A 横向对比**

---

## §6 BOSS 预判(V1 升级版,沿 `QUICK_KILL_6_DIRECTIONS.md` V0.2 模板)

### 6.1 BOSS-V1 经典 CLIP(ViT-B/32)— vision 通道判死

**测法**:
1. 用 OpenCLIP ViT-B/32 在 22 概念图上算 512-d embedding
2. GSM8K 30 cells text query → 512-d
3. 算 30×22 cosine,top-1 命中率
4. **判死**:`top-1 ≥ 24/30 = 80%` → BOSS-V1 PASS,**deposon 视觉通道无差异化**

**预期**:CLIP 0-shot 在 22 小图上 top-1 ≥ 80% 是大概率事件。**若 BOSS-V1 PASS,deposon vision 通道在"图像分类"上无新增**(只是把现成 CLIP 套到 22 图)

### 6.2 BOSS-V2 SigLIP(Zhai 2023)— vision 通道判死

**测法**:同 BOSS-V1 但用 SigLIP 模型
**判死**:`top-1 ≥ 80%` → BOSS-V2 PASS
**预期**:同 BOSS-V1,SigLIP 在 22 小图上应 ≥ 80%

### 6.3 BOSS-V3 多模态 LLM 直接看图(V1 新增)

**测法**:
1. 选 `doubao-seed-vision` 或 `minimax-m3` 直接看 22 张 PNG
2. 30 cells 题目 + 22 张图作 context
3. 算 pass rate
4. **判死**:`pass_rate ≥ 24/30 = 80%` → BOSS-V3 PASS,**VLM 0-shot 已足够,embedding 步骤多余**

**预期**:VLM 直接看 22 张图,描述后回答 30 cells,大概率 ≥ 24/30。**若 BOSS-V3 PASS,deposon "vision + Deposon" 双引擎方案 = 拍平为 VLM 0-shot**

### 6.4 BOSS 综合判死

| BOSS | 测法 | 若 PASS |
|---|---|---|
| V1 CLIP | 22 图 512-d cosine top-1 | vision 通道无差异化 |
| V2 SigLIP | 22 图 cosine top-1 | vision 通道无差异化 |
| V3 VLM | VLM 直接看 22 图 30 题 | vision 通道 = VLM 0-shot |
| **V1+V2+V3 全 PASS** | — | **deposon vision 方案整体拍平** |

**V1 含义**:
- 即使 deposon vision 通道在 30 cells 上 T_frac ≥ 0.80,若 BOSS-V1/V2/V3 全 PASS,**deposon vision 仍是"现有工具套用"**,**不构成新科学主张**
- 真正"deposon vision"必须有**Deposon-aware 散射场**独有信号(用 S_eff 公式 + 3D 投影距 (1,0,0) 评估)

---

## §7 7 铁律自检(V1 严格遵守)

| # | 铁律 | V1 状态 | 证据 |
|---|---|---|---|
| 1 | 0 LLM 调用 | ✅ | V1 是 SPEC,无 LLM 调用(阶段 1-3 实施时才调) |
| 2 | 不设 proxy | ✅ | 0 网络调用 |
| 3 | 不调 OpenRouter/TeamoRouter/V4.1-Flash/GPT-6/agent-plan | ✅ | V1 是 SPEC,无 LLM 调用 |
| 4 | key 永不入 prompt/JSON/磁盘 | ✅ | 阶段 1-3 实施时 `auth` 字段只截断 `ark-de0b484e-...` |
| 5 | 节省原则(max_tokens=1024, timeout=30s) | ✅ | 阶段 2/3 实施时 max_tokens=1024 |
| 6 | 不动 5 锚 JSON `KT_ABC1_anchors_sha256_12.json` | ✅ | `03c6c01f3697` 沿用(只读,V1 未触碰) |
| 7 | 不动 4 SPEC V0.1 冻结版 + v19/v21 frozen + corpus/v20/index.json | ✅ | V0 SPEC 只读(20128B),V1 是新增,corpus/v20/index.json 未触碰 |

### 7.1 严守 user 17:38+17:41 指令

- **17:38** 严守:`doubao-embedding-vision-251215` 是火山 catalog 内 model,V1 阶段 1-3 只在 catalog 范围内规划
- **17:41** 严守:阶段 1-3 实施只走 `ark.cn-beijing.volces.com/api/coding/v3` Coding Plan,**不**碰 OpenRouter/TeamoRouter
- **BOSS-V1/V2 用 OpenCLIP/SigLIP 离线模型**(阶段 6 BOSS 预判时)**不**走 OpenRouter

---

## §8 V1 决策点(等 user 决定)

| 决策 | 选项 | 建议 |
|---|---|---|
| 1. V1 SPEC 是否通过(博弈论升级 vs V0 沿用)? | A. 通过 V1(走阶段 1);B. 暂缓,沿 V0;C. 回退 V0 | **A**:V1 升级是 conservative 增量(只加判死线 + 公式,不删 V0 内容) |
| 2. 阶段 1 sanity 是否跑(5 min)? | A. 立即跑;B. 等 V3X 1 周判死完成;C. 跳过 | **A**:sanity 5 min,几乎无成本 |
| 3. 阶段 2 方向 a vs b,先跑哪个? | A. a(22 概念图);B. b(散射场可视化 + S_eff 公式);C. 一起 | **A**:a 直接测 layout 信息量,根因诊断更准 |
| 4. 阶段 3 跨模态检索双判死线是否启用? | A. 启用(top-1 ≥ 24/30 + A_frac ≤ 0.10);B. 只用 top-1 单一判死 | **A**:双线更稳,A 通道失真界是 P-C 必要条件 |
| 5. BOSS-V1/V2/V3 实施时跑哪个? | A. 只跑 V3(VLM 0-shot,最省);B. V1+V2+V3 全跑;C. 跳过 BOSS | **C** 起步,V3X 1 周判死后再决定 BOSS |

---

## §9 附录 A:V1 vs V0 关键差异表

| 维度 | V0 | **V1(博弈论版)** |
|---|---|---|
| 4 方向评级 | a❌ / b🟡 / c🟡 / d🟢 | **a❌ / b🟡+(P-E 公式) / c🟠 / d🟢+(P-A/P-C 双判死)** |
| 判死指标 | ratio ≥ 1.2 (单一) | **T_frac ≥ 0.80 + A_frac ≤ 0.10 + T+R+A=1 + 3D 散射场投影** |
| 公式 | 无 | **S_eff(E) = T·E_in - R·E_back + A·E_ground**(沿 v3 §6) |
| 9 model T/R/A 表 | 无 | **9 model 完整表(沿阶段 1)** |
| BOSS 预判 | BOSS-V1/V2/V3 概念 | **BOSS-V1/V2/V3 实施测法 + 判死线** |
| 终极形式 | ratio + cosine 融合 | **T 主导 + A 抑制 + R 微扰(博弈论视角)** |
| 实施阶段 | 3 阶段(无博弈论判死) | **3 阶段 + 5 候选博弈论判死线** |
| 5 锚 / 4 SPEC V0.1 / v19/v21 frozen | 不动 | **不动(沿 V0)** |
| 严守 user 17:38+17:41 | 是 | **是(V1 强化)** |
| 0 LLM | 是 | **是(V1 是 SPEC,无 LLM 调用)** |

---

## §10 附录 B:V1 数据完整性声明

- **本 SPEC V1 不调 LLM**,**0 调用**(沿 V0)
- **本 SPEC V1 不修改** 5 锚 JSON / 4 SPEC V0.1 / V0 SPEC / corpus/v20/index.json
- **本 SPEC V1 是新增文档**:`docs/V3X/EMBEDDING_VISION_STRATEGY_V1_GAMETHEORY.md`
- **V0 SPEC 父文件 SHA-12 沿用**(20128B,沿用未动)
- **阶段 1-3 实施时**才生成新文件(3 个 JSON + 3 个 MD + 22 PNG),目前**未生成**
- **配套并行任务**:`GAME_THEORY_EVAL_2026_09_10.md`(本任务 9 model 博弈论评估,SHA-12 = `3fa0ff2c8c08`)
- **V3X 终极形式 V1 升级** = T 主导 + A 抑制 + R 微扰(博弈论视角)

---

## §11 附录 C:相关已有报告

| 文件 | 用途 |
|---|---|
| `EMBEDDING_VISION_STRATEGY_V0.md` | V0 父文件(20128B,只读未动) |
| `GAME_THEORY_EVAL_2026_09_10.md` | 9 model T/R/A 博弈论评估(阶段 1 产出) |
| `VOLCENGINE_22CAPTION_EMBEDDING_2026_09_10.md` | 22 caption text embedding(NOISE verdict) |
| `VOLCENGINE_DOBAO_EMBEDDING_2026_09_10.md` | doubao-embedding-vision 早期探活 |
| `EMBEDDING_DUAL_SMOKE_2026_09_10.md` | 双 embedding 探活 |
| `DEPOSON_EMBEDDING_6WAY_THEORY_V0_2026_09_10.md` | 6 方向理论 V0(V1 沿用框架) |
| `QUICK_KILL_6_DIRECTIONS.md` | V0.2 6 方向 BOSS 模板(V1 BOSS-V1/V2/V3 沿用) |
| `CPATH_SIMULATION_REPORT_2026_09_10.md` | C 路径 0 LLM 模拟(沿用 S_eff 全局占比) |
| `KT_A1_SPEC_V0.1.md` / `KT_B1_SPEC_V0.1.md` 等 4 SPEC V0.1 | 4 SPEC 冻结(只读未动) |
| `KT_ABC1_anchors_sha256_12.json` | 5 锚 JSON(SHA-12 = `03c6c01f3697` 未动) |
