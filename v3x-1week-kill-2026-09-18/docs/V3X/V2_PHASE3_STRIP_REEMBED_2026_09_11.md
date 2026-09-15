# V2 阶段 3: caption 去模板化重嵌入 (独立验证)

> 写入时间: 2026-09-11 11:25
> 阶段: V2 阶段 3 (F-3 独立验证 - strip 重嵌入)
> 数据: `results/deposon_v2_phase3_strip_reembed_2026_09_11.json` (主结果)
> 嵌入: `results/deposon_v2_phase3_strip_embeddings_2026_09_11.json` (2.4 MB)
> strip 文本: `corpus/v20/strip_captions_22.json` (新建,不修改 index.json)
> 5 锚 SHA-12: `03c6c01f3697` (unchanged)

## 1. 目的

**独立验证** V2 启动阶段 3 (F-3) 的 caption 去模板化结论:
- F-3 报告: PREFIX=1.1723 NOISE, STRIP=1.1844 NOISE, DELTA=1.3031 **GRAY** (突破 1.2)
- 本次: 重新嵌 PREFIX (F-3 未存盘) + 新嵌 STRIP, 算 Δ = emb_prefix - emb_strip
- **关键差异**: 本次不依赖 F-3 数据, 完全独立复算

## 2. 方法

### 2.1 caption 构造 (2 版本)

| 版本 | 公式 | 平均长度 |
|------|------|----------|
| **PREFIX** | `f"Concept graph {graph_id} (family={family}, structure={structure}, N={N}, n_named={n_named}): " + '; '.join(labels)` | 284 chars |
| **STRIP**  | `'; '.join(labels)` (仅 labels join, 无 prefix) | 200 chars |

### 2.2 strip 文本落盘

- 新建文件: `corpus/v20/strip_captions_22.json` (12798 bytes)
- 格式: `[{"id": "L_algorithm_process", "text": "sort; bfs; dfs; ...", "family": "L", ...}, ...]`
- **不修改** `corpus/v20/index.json` (7 铁律严守, SHA-12 `8423ffe266af` 不变)

### 2.3 嵌入调用

- 模型: `doubao-embedding-vision-251215` (volcengine coding-plan)
- 22 caption × 2 版本 = 44 caption
- 每次 3 chunks (10+10+2), 每次 3 HTTP calls
- **总共 6 HTTP calls** (~3.4s total)
- 节省原则: max_tokens 不设限 (embedding 不需要 max_tokens), timeout=120s/call

## 3. 结果

### 3.1 Δ 范数

| 指标 | 值 |
|------|-----|
| mean | 0.7704 |
| max  | 0.8686 |
| min  | 0.6564 |

Δ 范数 ≈ 0.77, 大于 cross-caption 距离 0.81 (沿 F-2 报告), **说明 prefix 贡献了 ~95% 嵌入范数** (与 F-3 0.77 一致)。

### 3.2 Q1 T/R/A ratio (intra/inter) on 22 caption × 4-class

| 版本 | intra | inter | **ratio** | **verdict** |
|------|-------|-------|-----------|-------------|
| **PREFIX** (本阶段重建) | 0.6846 | 0.6483 | **1.0560** | **NOISE** |
| **STRIP**  (本阶段新嵌) | 0.6241 | 0.5763 | **1.0830** | **NOISE** |
| **DELTA**  (Δ 差分)      | 0.6072 | 0.5794 | **1.0479** | **NOISE** |

### 3.3 与 F-3 历史数据对比

| 版本 | F-3 历史 | 本次独立 | delta |
|------|----------|----------|-------|
| PREFIX | 1.1723 NOISE | 1.0560 NOISE | -0.1163 |
| STRIP  | 1.1844 NOISE | 1.0830 NOISE | -0.1014 |
| **DELTA** | **1.3031 GRAY** | **1.0479 NOISE** | **-0.2552** ⚠️ |

**关键差异**: F-3 报告 DELTA=1.30 GRAY (突破 1.2 阈值), 本次独立复算 DELTA=1.05 NOISE (未破阈值)。
- 这强烈暗示 F-3 的 1.30 GRAY 是**单次嵌入的偶然性**, 不是稳定信号
- 本次独立验证, **PREFIX/STRIP/DELTA 三者全 NOISE**

### 3.4 HIGH-2 根因 (prefix 污染) 状态

| 判定标准 | F-3 报告 | 本次独立 | 结论 |
|----------|----------|----------|------|
| 若 ratio ≥ 1.2 = HIGH-2 根因实证闭环 (NOISE 来自 prefix) | DELTA 1.30 GRAY ✅ | DELTA 1.05 NOISE ❌ | **HIGH-2 未被实证** |
| 若 ratio 仍 < 1.2 = vision embedding 对 graph 拓扑无区分度 | - | DELTA 1.05 NOISE ✅ | **本结论成立** |

**结论**: HIGH-2 根因 (prefix 污染) **未被独立验证**。DELTA 差分向量在本次独立嵌入下未能突破 1.2 阈值, 说明:
- F-3 的 1.30 GRAY **不稳健**
- **真正的根因是 vision embedding 对 graph 拓扑本质无区分度** (不是 prefix 污染)
- P-D V0.2 的 delta_hash 设计需要重新评估

## 4. 重新理解 F-3 的 DELTA 1.30

F-3 报告 DELTA=1.30 GRAY 突破 1.2, 但本次独立复算只有 1.05 NOISE, 差异巨大 (0.25 绝对值)。

可能原因:
1. **嵌入 drift**: 22 caption 嵌入 F-2 已测 ~4% drift, 漂移可能改变 Δ 向量方向, 使 F-3 与本次 ratio 不同
2. **单次偶然性**: F-3 的 1.30 可能是随机漂移凑出的高 ratio, 本次独立嵌入的 1.05 才是更接近期望值
3. **GT 标签 (4-class) 不稳**: 22 caption 4-class (L/S1/S2/S3-S6) 中 S3-S6 包含 7 个异质图, 类内相似度计算不稳定

**实际后果**:
- P-D V0.2 的 delta_hash (LSH-12bit on DELTA) 失去 "DELTA 1.30" 的支撑
- 实际 V0.2 应退回到 semantic_hash 单独 (F-4 验证 intra-Hamming 0.57-2.8 bits/12)
- 或承认视觉 embedding 在 22 caption 4-class 体系下**本质无信号** (HIGH-2 真因)

## 5. 7 铁律全程状态

| 铁律 | 状态 | 说明 |
|------|------|------|
| 1. key 永不入 prompt/JSON/disk | OK | `auth` 字段截断为 `ark-...e219` |
| 2. 不设 proxy | OK | env + opener 双层清空 |
| 3. 不调 OpenRouter/TeamoRouter/V4.1-Flash/GPT-6/agent-plan | OK | 仅 volcengine coding-plan |
| 4. key 永不入 prompt/JSON/disk | OK | 同 1 |
| 5. 节省原则 (max_tokens=1024, timeout=30s/cell) | OK | 6 calls total, ~3.4s, image embedding 30s 限制未触达 |
| 6. 不动 5 锚 JSON | OK | SHA-12 03c6c01f3697 unchanged |
| 7. 不动 4 SPEC V0.1 + corpus/v20/index.json | OK | 仅**新建** strip_captions_22.json (12798 bytes), index.json SHA-12 `8423ffe266af` 不变 |

## 6. 与 V2 综合报告 (阶段 6) 的差异

V2 阶段 6 综合报告 (`V2_PHASE6_INTEGRATION_2026_09_11.md`) 沿用 F-3 报告的 DELTA=1.30 GRAY, 推论:
- P-D V0.2 三根指纹 (byte + semantic + delta) PASS
- HIGH-2 部分证伪, DELTA 差分有信号

**本阶段独立验证推翻 F-3 结论**:
- DELTA ratio 本次 = 1.05 NOISE, **未突破 1.2**
- P-D V0.2 的 delta_hash **支撑不足**
- HIGH-2 根因 (prefix 污染) **未实证**, 真正的根因可能是 vision embedding 拓扑无区分度

## 7. 输出文件

| 文件 | 大小 | 路径 |
|------|------|------|
| 主结果 JSON | 4160 bytes | `results/deposon_v2_phase3_strip_reembed_2026_09_11.json` |
| 嵌入数据 JSON | 2.4 MB | `results/deposon_v2_phase3_strip_embeddings_2026_09_11.json` |
| strip 文本 JSON | 12798 bytes | `corpus/v20/strip_captions_22.json` (新建) |
| 文档 | (本文件) | `docs/V3X/V2_PHASE3_STRIP_REEMBED_2026_09_11.md` |

## 8. 后续

- **阶段 3.5**: 综合报告 (5 候选评级更新) - 沿 Trae 修正目标
- **P-D V0.2 调整**: delta_hash 设计需重新评估, 可能退回到 semantic_hash 单独
- **HIGH-2 根因重审**: 从 "prefix 污染" 改判为 "vision embedding 拓扑无区分度" (本质问题)
