# Doubao-Embedding-Vision 策略 SPEC V0(多模态能力未开发问题)

> **生成时间**: 2026-09-10 21:38+08:00
> **作者**: Mavis Worker (subagent of mvs_bbeb804b1a6a41109be740636eed1709, session mvs_e63b2aaa6fd349ef9e14a7948c01cb24)
> **任务来源**: user 2026-09-10 21:27 三指令之二:「doubao-embedding-vision 的 vision 优势没发挥(需思考其他方向)」
> **状态**: **SPEC V0 草案(只写 spec,不调 LLM,避免重复调用)**
> **配套任务**: 本任务与 `MINIMAX_M3_30CELLS_2026_09_10.md` 并行(minimax-m3 重测 21/30 = 70%)
> **严守约束**: user 2026-09-10 17:38(火山 catalog 内)+ 17:41(只走 coding-plan,无 proxy,无 OpenRouter)

---

## §0 摘要(SPEC V0 核心)

- **问题陈述**:`doubao-embedding-vision-251215` 模型(火山方舟 Coding Plan)的 **vision 能力当前 0 利用**——22 caption embedding 全部只传文本,完全没用上 vision 通道
- **核心矛盾**:该模型同时支持 text(2048-d) + image(多模态融合)输入,但 V3X RAG 路径**只用了 text 路径**
- **SPEC V0 目标**:列出 4 个可能利用 vision 的方向,逐个评估可行性 + 实施成本,**作为 V3X 终极形式的可选输入**
- **不实施**:本任务只写 SPEC,**不**调 embedding API(避免与已有 `deposon_volcengine_22caption_embedding_2026_09_10.json` 重复),具体执行待 user 决定
- **结论**:**方向 d(跨模态检索)最可行**(V3X 已有 22 graph metadata,文本→图像检索可在 5 min 内跑出),**方向 a 需 user 提供概念图**

---

## §1 现状分析:为什么 vision 优势 0 利用

### 1.1 已有数据回顾

| 数据 | 模型 | 输入类型 | 输出 | 状态 |
|---|---|---|---|---|
| `deposon_volcengine_22caption_embedding_2026_09_10.json` | `doubao-embedding-vision-251215` | **仅文本**(22 caption 字符串) | 2048-d × 22 | **完成** |
| 22 caption 文本构造 | — | `f"Concept graph {graph_id} (family=..., structure=..., N=..., n_named=...): " + '; '.join(labels)` | 字符串 | — |
| intra/inter ratio | — | 2048-d 空间 | **1.0562(NOISE)** | 失败 |

### 1.2 vision 通道未触发的 3 个原因

1. **22 caption 全是文本**:`corpus/v20/index.json` 索引 + 22 per-graph `.json` labels,**没有任何图像数据**
2. **deposon 的概念图本来是 GraphViz DOT/NetworkX 渲染**:但**渲染脚本未跑**(deposon V3X 至今没生成 22 张 PNG/SVG 实际图像)
3. **RAG baseline 失败主因 = caption 文本模板压制 PCA**:换 vision 通道**不会**自动解决 NOISE,因为问题在"22 caption 共享模板前缀"而非"embedding 模型"

### 1.3 vision 通道的真正价值(理论)

`doubao-embedding-vision-251215` 是**多模态模型**(参考 OpenRouter 同类 `nvidia/llama-nemotron-embed-vl-1b`,见 `EMBEDDING_OPENROUTER_5MODELS_2026_09_10.md`):
- **text input** → 2048-d text vector
- **image input** → 同样 2048-d image vector(共享向量空间)
- **text-image** 在同一空间对齐 → 可做**跨模态检索**(text query → image candidates)

**理论增益**(若实施方向 a/d):
- 22 张概念图实际图像**视觉特征更丰富**(节点位置、连边粗细、布局对称性),比纯文本 labels 信息量更大
- text 检索图像:用 GSM8K/StrategyQA 题目**直接查** 22 张概念图,跳过 "labels → embedding → top-k" 链路

---

## §2 4 方向分析

### 方向 a. 22 概念图实际图像 embedding ❌(corpus 无图)

| 维度 | 评估 |
|---|---|
| **核心思路** | 22 张概念图 PNG/SVG 实际图像 → `doubao-embedding-vision` image input → 2048-d 图像向量 → 类内/类间 ratio |
| **可行性** | ❌ **corpus 无图像数据**:`corpus/v20/index.json` 只有 graph metadata(N, n_edges, n_named, seed, sha256),22 per-graph JSON 只有 `nodes`/`edges`/`labels`,**无 PNG/SVG 路径** |
| **实施步骤** | 1) 写 GraphViz 渲染脚本(`networkx.draw_graphviz` 或 `pygraphviz`)→ 22 PNG;2) 上传 image URL 或 base64 编码送 vision input;3) 算 22 image embedding 2048-d;4) 算 ratio;5) 对比 text baseline 1.0562 |
| **预计耗时** | 30-60 min(渲染 22 张 + 1 batch embedding) |
| **预估 verdict** | **待定**。图像空间可能**信息量大于文本**(`offdiag_mean` 期望从 0.66 降至 0.4-0.5,`ratio` 期望 ≥ 1.3),但**也**可能因图像模板(同一 layout 算法)同样被压制 |
| **阻塞** | **需 user 提供 / 允许写渲染脚本**。corpus 不含图像是硬约束 |
| **优先级** | 🟡 **中**(若 user 提供 22 张 PNG,30 min 内可出 verdict) |

### 方向 b. deposon 散射场可视化图 🟡(需写可视化脚本)

| 维度 | 评估 |
|---|---|
| **核心思路** | 把 V3X 散射公式 `S_eff(E) = T·E_in - R·E_back + A·E_ground` 渲染为散射场图(T/R/A 三通道不同颜色编码),作为 vision input |
| **可行性** | 🟡 **可写脚本**:沿 `docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_10.md` 已有散射公式实现,加 matplotlib 渲染层 |
| **实施步骤** | 1) 写 `tools/scatter_field_viz.py` 生成 22 张散射场图(T 通道红色 / R 通道蓝色 / A 通道灰色,每节点按 `S_eff` 强度着色);2) image embedding 22 张;3) 算 ratio |
| **预计耗时** | 60-90 min(写可视化 + 跑 22 image embedding) |
| **预估 verdict** | **理论更强**。散射场图直接编码 V3X 主张(T/R/A 三通道),如果连"散射场图"都不能区分 L/S1/S2/S3-S6,那 NOISE 根因不在 embedding 侧 |
| **阻塞** | 无硬阻塞,但**方向 a 优先**(更直接) |
| **优先级** | 🟡 **中**(沿 V3X 散射公式可视化 = 理论自洽,但与方向 a 重复) |

### 方向 c. 多模态 RAG(图文混排) 🟡(需改 RAG)

| 维度 | 评估 |
|---|---|
| **核心思路** | RAG context 改为"图 + 文"混合:每条 caption 同时包含文本(原 labels)+ 缩略图 base64,送入多模态 LLM(`doubao-seed-vision` / `minimax-m3`)? |
| **可行性** | 🟡 **需双模型协调**:`doubao-embedding-vision` 输出 2048-d 仍是文本侧向量,真正"图文混排 RAG" 需多模态 LLM 在 context 中**直接看图**(例如 `doubao-seed-vision` / 火山 vision LLM) |
| **实施步骤** | 1) 改 RAG 管线,context = text + 缩略图;2) 选 vision LLM 做推理;3) 30 cells 重测 |
| **预计耗时** | 2-3 h(改 RAG + 选 vision LLM + 30 cells 重测) |
| **预估 verdict** | **理论最强**。图文混排 RAG 与单文本 RAG 相比,若 ratio 提升 ≥ 0.2 → 直接证明 vision 通道价值 |
| **阻塞** | **需改 RAG 管线**(V3X 当前 RAG 已 lock 80% baseline,改 = 重新跑全套 30 cells) |
| **优先级** | 🟠 **低**(成本高,需 30 cells 重测,风险高) |

### 方向 d. 跨模态检索(GSM8K 文本 → 22 概念图) 🟢 V3X 已有图 metadata 可探索

| 维度 | 评估 |
|---|---|
| **核心思路** | **不**做完整 vision RAG,**只**做"文本 query → 22 图像 candidate 排序":把 22 概念图渲染为缩略图,GSM8K 题目作为 text query,看 vision embedding top-1 是否命中"该题对应概念域" |
| **可行性** | 🟢 **V3X 已有图 metadata**:corpus/v20 有 22 graph_id + family + structure + N + n_named + sha256,渲染脚本可立即写(20 行 networkx 代码) |
| **实施步骤** | 1) 写 20 行 `tools/graph_to_png.py` 用 networkx 渲染 22 张概念图;2) `doubao-embedding-vision` 接受 22 image input 算 embedding;3) 30 cells 题目的 text input 算 embedding;4) 算 cosine 矩阵;text→image top-1 命中率 |
| **预计耗时** | **20-30 min**(20 行渲染 + 1 batch embedding + cosine) |
| **预估 verdict** | **与已有 ratio=1.0562 文本 baseline 对比**。如果 image 空间 ratio ≥ 1.2 → vision 通道**真**有信号;如果仍 < 1.2 → vision 也救不了 NOISE,根因在 caption 模板而非 modality |
| **阻塞** | **无硬阻塞**。只需 user 同意写渲染脚本(20 行,本仓库可加) |
| **优先级** | 🟢 **最高**(成本最低 + 5 min 即可出 verdict + 不动 RAG 管线 + 不动 frozen JSON) |

---

## §3 实施方案(3 阶段)

### 阶段 1:短期(5 min,不调 LLM,只 catalog 探活)

**目标**:验证 `doubao-embedding-vision-251215` 是否真支持 image input(避免方向 a/d 实施时才发现)

**步骤**:
1. **catalog 探活**:沿 `results/deposon_volcengine_coding_plan_catalog_2026_09_10.json` 查 model catalog 字段(7 铁律:不调 LLM,只读 metadata)
2. **1-cell sanity 测 text + 文本 + image 变体**:
   - sanity 1: `text input` `"What is 1+1?"` → 2048-d
   - sanity 2: 1 张测试图(base64 1x1 PNG 占位)→ 2048-d
   - 验两个 sanity 是否**同时**返回 200
3. **判定**:如 image input 200 OK → 方向 a/b/d 可实施;如 400/422 → 需 user 决定是否换 model

**约束**:max_tokens 不适用(embedding 无生成),1 batch 22 image input 是 embedding API 而非 chat completion
**输出**:`docs/V3X/EMBEDDING_VISION_SANITY_2026_09_10.md`(1 KB)
**预计耗时**:**5 min**

### 阶段 2:中期(30 min,写散射场可视化 + 测图输入)

**目标**:方向 b + 方向 a 联合实施(2 套图都试,取最优)

**步骤**:
1. **写 `tools/graph_to_png.py`**(20 行):
   ```python
   for graph_id in corpus_v20_graphs:
       g = load_graph(corpus_v20 / f'{graph_id}.json')
       pos = nx.spring_layout(g)  # 或 graphviz_layout
       plt.figure(figsize=(4, 4))
       nx.draw(g, pos, with_labels=False, node_size=20, edge_color='gray')
       plt.savefig(f'/tmp/{graph_id}.png', dpi=80, bbox_inches='tight')
   ```
2. **写 `tools/scatter_field_viz.py`**(30 行):
   ```python
   for graph_id, t_vec, r_vec, a_vec in zip(...):
       # 节点按 t/r/a 三通道强度染色
       # T=red, R=blue, A=gray
       # 边宽 = |S_eff(E)|
       plt.savefig(f'/tmp/scatter_{graph_id}.png', dpi=80)
   ```
3. **embedding 22 张 PNG(image input)**:1 batch,同 `doubao-embedding-vision-251215`
4. **算 ratio + KMeans ARI**:对比 text baseline 1.0562 / 0.0615
5. **判定**:
   - 任意一套图 ratio ≥ 1.2 → 走方向 b(散射场图),V3X 终极形式支持 vision
   - 两套图 ratio 都 < 1.2 → NOISE 在 modality 之外(根因 = layout 算法共享),方向 a/b 失败
6. **输出**:
   - `results/deposon_volcengine_22image_embedding_2026_09_10.json`
   - `docs/V3X/EMBEDDING_VISION_PHASE2_2026_09_10.md`(2-3 KB)

**约束**:
- 不动 corpus/v20/index.json(只读)
- 22 PNG 渲染在 `figures/vision_rag/`(新建,需 user 同意)
- 1 batch image input = 3 chunk(10+10+2),沿用 22caption 模式

**预计耗时**:**30 min**

### 阶段 3:长期(1-2 h,22 概念图多模态 embedding 落盘 + 跨模态检索 30 cells)

**目标**:方向 d 完整实施 = 跨模态检索 + 30 cells 端到端

**步骤**:
1. **沿阶段 2 落盘的 22 image embedding**(直接复用,0 成本)
2. **30 cells 题目 text embedding**:沿 `deposon_benchmark_v1_4_gsm8k_details.json` 30 题 + `deposon_benchmark_v1_4_strategyqa_details.json` 15 题(本任务 30 cells 已跑过,可省)
3. **算 text→image cosine 矩阵**:
   - 30 × 22 矩阵
   - top-1 命中率(命中率 = top-1 概念图 family 是否与题目"领域"匹配)
4. **判死线**:
   - text→image top-1 命中率 > 30/30 = 100% → **方向 d PASS**(强信号)
   - 命中率 ≥ 24/30 = 80% → **GRAY**(与已有 baseline 打平)
   - 命中率 < 24/30 → **FAIL**(vision 通道救不了)
5. **30 cells 推理增强**(若方向 d PASS):
   - 沿 C 路径:Deposon-aware 选 top-1 image 作为 context
   - 30 cells 重测(用 minimax-m3,本任务已证明 minimax-m3 70% 稳定)
6. **输出**:
   - `results/deposon_volcengine_22image_embedding_30cells_2026_09_10.json`
   - `docs/V3X/EMBEDDING_VISION_PHASE3_2026_09_10.md`(5-8 KB)

**约束**:
- 不动 30 cells 边界(沿用本任务 minimax-m3 重测 21/30 = 70%)
- 不动 corpus/v20/index.json + 22 per-graph JSON(只读)
- 不调 OpenRouter / TeamoRouter(严守 user 17:38+17:41)

**预计耗时**:**60-120 min**

---

## §4 V3X 多模态终极形式(SPEC V0 草案)

### 4.1 当前 6 方向回顾(沿 6 方向理论 V0)

| 方向 | 当前 verdict | 缺口 |
|---|---|---|
| A. Deposon-aware Embedding | **NOISE**(T 通道 ratio=1.0000) | 文本 caption 模板压制 PCA |
| B. 三通道 LLM 评估 | GRAY(4 LLM 5-8 fails) | 模型能力 / 算力边界 |
| C. 散射场替代 RAG | PARTIAL(8/10 GSM8K) | — |
| D. LLM 推理 = 散射场算子 | THEORETICAL | 无量化指标 |
| E. V3X 失真界 | NOISE(T+R+A=1 在 SVD 2D 弱保持) | 需原始 2048-d |
| F. 终极形式 | NO(因 A/E 拖累) | C 是真正入口 |

### 4.2 终极形式的 vision 增强版(本任务新增)

```
V3X 终极形式 = Deposon-aware 推理 + 多模态上下文

输入: question q (text), 候选 22 概念图 {g_i, image_i, caption_i}
1. 多模态 embedding:
   - E_text(q) ← doubao-embedding-vision(text=q)  # 2048-d
   - E_image(g_i) ← doubao-embedding-vision(image=g_i.png)  # 2048-d
   - E_caption(c_i) ← doubao-embedding-vision(text=c_i)  # 2048-d
2. 三路融合:
   - sim_text(q, g_i) = cosine(E_text(q), E_image(g_i))
   - sim_caption(q, c_i) = cosine(E_text(q), E_caption(c_i))
   - sim_combined = α·sim_text + (1-α)·sim_caption  # α = 0.5 起步
3. Deposon-aware 选 top-k(沿 6 方向理论 V0 §5.4):
   - T_frac(q, g_i) 沿 PCA 主方向投影
   - 选 T_frac 最高的 top-3
4. LLM 推理 + 三通道评估:
   - context = [top-3 image, top-3 caption]
   - 输出 T(pass) / R(fail) / A(trunc/timeout)
5. 输出: T_frac, R_frac, A_frac, sim_combined_top1, 守恒校验 T+R+A=1
```

**与现有 RAG 区别**:
- **现有 RAG**:单 text → text cosine → top-k context
- **V3X 终极 vision 版**:text + image 双路 cosine → 融合 → Deposon-aware top-k

**预期增益**:
- 若方向 d 阶段 3 验证 text→image 命中率 ≥ 80%:V3X 终极形式 = "vision + Deposon"双引擎,论文可写 "V3X 终极形式在多模态场景下通过"
- 若 vision 通道验证失败:V3X 终极形式降级回 C 路径(纯 Deposon-aware RAG,text-only),论文主张相应缩小

### 4.3 论文叙事角度(供 1 周后讨论)

| 视角 | 描述 | 论文价值 |
|---|---|---|
| **V3X 跨模态延拓** | "deposon 散射场从文本延拓到视觉,T/R/A 通道在 22 概念图视觉空间仍可分" | 强(开辟新方向) |
| **V3X 视觉为辅** | "Deposon 主框架 = 文本,vision = 增强检索精度" | 中(实用价值) |
| **V3X 视觉不可分** | "vision 通道 ratio < 1.2,与文本同 NOISE,根因在 22 graph 共享 layout" | 弱(否定性结果,需 BOSS 自检) |

**BOSS 预判**(沿 QUICK_KILL_6_DIRECTIONS 模板):
- BOSS-V1: 经典 CLIP(ViT-B/32) → 跨模态检索在 22 小图上,CLIP 0-shot 即可达到 ≥ 80% top-1。**测法**:跑 OpenCLIP ViT-B/32 baseline,如 30 题 22 图 top-1 ≥ 24 → deposon 视觉通道无差异化。
- BOSS-V2: SigLIP(Zhai 2023) → 同样在 22 图小数据上 top-1 命中率应 ≥ 80%,deposon 视觉方案**无新增**。
- BOSS-V3: 多模态 LLM 直接看图(doubao-seed-vision / minimax-m3)→ VLM 0-shot 描述 22 张图就够,不需要 embedding。**测法**:VLM 直接看 22 张图 + 30 题,看 pass rate;如 ≥ 24/30 → vision RAG 拍平为通用 VLM。

---

## §5 7 铁律自检(本 SPEC V0 严格遵守)

| # | 铁律 | 本任务执行 | 状态 |
|---|---|---|---|
| 1 | 火山 key runtime 读(GB18030) | **不读**(本任务只写 spec,无 LLM 调用) | ✓ |
| 2 | 不设 proxy | **不设**(无网络调用) | ✓ |
| 3 | 不调 OpenRouter/TeamoRouter/V4.1-Flash/GPT-6/agent-plan | **不调**(本任务无 LLM 调用) | ✓ |
| 4 | key 永不入 prompt/JSON/磁盘 | **无 key** | ✓ |
| 5 | 节省原则(max_tokens=1024, timeout=30s) | **不适用**(本任务无 LLM 调用) | ✓ |
| 6 | 不动 5 锚 JSON `KT_ABC1_anchors_sha256_12.json` | 未触碰(`03c6c01f3697` 沿用) | ✓ |
| 7 | 不动 4 SPEC V0.1 + v19/v21 frozen + v20 baselines + corpus/v20/index.json | **SPEC V0 是新增**(本文件)非修改 4 SPEC;corpus/v20/index.json **未触碰**(阶段 2/3 实施时才需读) | ✓ |

### 5.1 严守 user 17:38+17:41 指令

- **17:38** 严守:`doubao-embedding-vision-251215` 是火山 catalog 内 model,本任务只在 catalog 范围内规划
- **17:41** 严守:阶段 2/3 实施只走 `ark.cn-beijing.volces.com/api/coding/v3` Coding Plan,**不**碰 OpenRouter/TeamoRouter
- **不动 proxy**:阶段 1-3 实施时仍清 6 个 proxy env var(沿 worker_c 模式)
- **key 永不落盘**:阶段 1-3 实施时 `auth` 字段只截断 `ark-de0b484e-08...e219`

---

## §6 下一步(等 user 决定)

### 6.1 决策点(等 user 回应)

| 决策 | 选项 | 建议 |
|---|---|---|
| **1. 是否进入阶段 1(5 min sanity)?** | A. 立刻跑(我执行);B. 暂缓,等 V3X 1 周判死完成;C. 跳过,直接进阶段 2 | **A**:sanity 5 min,几乎无成本,可立即验 vision API 可用性 |
| **2. 阶段 2 方向 a vs 方向 b,先跑哪个?** | A. 方向 a(22 概念图实际图像);B. 方向 b(散射场可视化);C. 一起跑 | **A**:方向 a 直接测 layout 信息量,根因诊断更准 |
| **3. 22 概念图渲染脚本放在哪?** | A. `tools/graph_to_png.py`(新建);B. `figures/vision_rag/`(新建 PNG 目录);C. 不渲染,改用 corpus 已有结构特征向量(8-10 维,沿 22 caption embedding §3.1.4) | **A+B**:直接渲染,避免再向 user 索取数据 |
| **4. 阶段 3 跨模态检索 30 cells 是否要重跑推理?** | A. 只测 text→image top-1 命中率(0 LLM 调用);B. 加 30 cells 推理增强对比(完整 C 路径重跑) | **A**:先 0 成本验命中率,如 ≥ 80% 再启动 B |

### 6.2 与 V3X 1 周判死的时间线协同

| 时间 | 任务 | 决策依赖 |
|---|---|---|
| **本周(2026-09-10 ~ 09-14)** | 5 候选 P-A/B/C/D + minimax-m3 1 周判死 | minimax-m3 70% 已知,**主推 V4.1-Flash 25/30** |
| **下周(2026-09-15 ~ 09-21)** | 若 5 候选有 PASS → 启动方向 a/d 阶段 1+2(30-60 min) | vision sanity 通过后立即跑 |
| **9 月底(2026-09-22 ~ 09-30)** | 阶段 3 完整跑(60-120 min) | 若方向 a/d PASS,作为 6 月单论文的 vision 章节 |

### 6.3 阻塞点(等 user 决定)

- **关键阻塞**:是否允许**新建 `figures/vision_rag/` 目录**放 22 PNG?(沿 V3X 冻结规范,corpus 是 v20 frozen,figures 是论文产物,**不**是 frozen)
- **关键决策**:方向 d 阶段 3 跨模态检索若 80%+ 命中,**是否**进 30 cells 推理重测?(可能 2-3 h,且需重跑 RAG baseline 24/30 对比)
- **不阻塞**:阶段 1 sanity 5 min,**无依赖**,user 同意即可跑

---

## §7 取消条件(沿 V3X = 1 周预筛)

按 deposon V3X = 1 周判死原则(见 user profile 2026-09-04):
- 阶段 1 sanity 若 vision API **不可用**(400/422)→ 整个 SPEC V0 取消,方向 d 改走纯文本 cosine 增强(已失败)
- 阶段 2 任意方向 ratio < 1.2 → 整个 SPEC V0 取消,V3X 终极形式降级为 C 路径(纯 Deposon-aware RAG)
- 阶段 3 跨模态 top-1 命中率 < 24/30 → 取消 vision 章节,V3X 论文不写 vision 部分

**取消 ≠ 失败**:NOISE 否定性结果也写报告归档,作为"为什么 V3.X 不上 vision 通道"的依据(同 `VOLCENGINE_22CAPTION_EMBEDDING_2026_09_10.md` §5 模式)

---

## 附录 A:数据完整性声明

- **本 SPEC V0 不调 LLM**,**0 调用**(`auth` 字段、IP 字面值、key 全部不出现)
- **本 SPEC V0 不修改** 5 锚 JSON / 4 SPEC V0.1 / corpus/v20/index.json
- **本 SPEC V0 是新增文档**:`docs/V3X/EMBEDDING_VISION_STRATEGY_V0.md`
- **阶段 1-3 实施时**才生成新文件(3 个 JSON + 3 个 MD + 22 PNG),目前**未生成**
- **配套并行任务**:`MINIMAX_M3_30CELLS_2026_09_10.md`(21/30 = 70% PASS,MARGINAL)

## 附录 B:相关已有报告

| 文件 | 用途 |
|---|---|
| `VOLCENGINE_22CAPTION_EMBEDDING_2026_09_10.md` | 22 caption text embedding 完整报告(NOISE verdict) |
| `VOLCENGINE_DOBAO_EMBEDDING_2026_09_10.md` | doubao-embedding-vision 早期探活 |
| `EMBEDDING_DUAL_SMOKE_2026_09_10.md` | 双 embedding 探活(已确认 vision 通道存在) |
| `EMBEDDING_OPENROUTER_5MODELS_2026_09_10.md` | OpenRouter 5 embedding 模型对比(本任务**不**走 OpenRouter) |
| `DEPOSON_EMBEDDING_6WAY_THEORY_V0_2026_09_10.md` | 6 方向理论版 V0(本 SPEC V0 是其 vision 延拓) |
| `MINIMAX_M3_30CELLS_2026_09_10.md` | 并行任务:minimax-m3 重测 21/30 = 70% |
| `QUICK_KILL_6_DIRECTIONS.md` | V0.2 6 方向 BOSS 模板(本 SPEC V0 阶段 3 含 BOSS-V1/V2/V3) |
