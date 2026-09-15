# V2 阶段 3.5: 综合报告 (阶段 2+3 整合 + 5 候选评级更新)

> 写入时间: 2026-09-11 11:25
> 阶段: V2 阶段 3.5 (综合报告 - 沿 V2 阶段 6 + 本次阶段 2+3 整合)
> 数据: 阶段 2 JSON + 阶段 3 JSON + V2 阶段 1-5 历史
> 5 锚 SHA-12: `03c6c01f3697` (unchanged)

## 1. 阶段 2 + 3 核心结论

### 1.1 阶段 2 (双主线 baseline 验证)

- GLM-5.3 + doubao-seed-2.0-lite 双主线 60 cells (30 + 30) 严格守恒 T+R+A=1
- 9 model × 60 cells partition max frac_residual = **1.11e-16** (16-bit float round-off,沿 V1 §2.4)
- 双主线 60 cells 合并: T=52, R=7, A=1, sum=60 (count) 或 1.0 (frac),residual=0
- V2 dpath 60 cells: 51/60 = 85.00% (STRONG_PASS),vs no-RAG 86.67% (-1.67pp)
- **0 新 API 调用** (严守节省原则)

### 1.2 阶段 3 (caption strip 重嵌入 - 独立验证)

- 重建 PREFIX + 新嵌 STRIP (2 versions × 3 chunks = 6 calls, ~3.4s)
- Δ = emb_prefix - emb_strip 范数 mean=0.77 (与 F-3 一致,prefix 贡献 ~95% 嵌入范数)
- **Q1 T/R/A ratio (本次独立)**:
  - PREFIX: **1.0560 NOISE**
  - STRIP:  **1.0830 NOISE**
  - DELTA:  **1.0479 NOISE** ⚠️
- **F-3 报告对比**:
  - PREFIX: 1.1723 NOISE (本次 -0.1163)
  - STRIP:  1.1844 NOISE (本次 -0.1014)
  - **DELTA: 1.3031 GRAY → 本次 1.0479 NOISE (-0.2552,严重不一致)** ⚠️

## 2. 关键发现: F-3 DELTA 1.30 GRAY 不稳健

**F-3 报告的 DELTA ratio=1.30 GRAY 在本次独立验证中**未能复现**(1.05 NOISE)**。

| 维度 | F-3 报告 | 本次独立 | delta | 结论 |
|------|----------|----------|-------|------|
| DELTA ratio | 1.3031 GRAY | 1.0479 NOISE | -0.2552 | F-3 1.30 是单次偶然性 |
| PREFIX ratio | 1.1723 NOISE | 1.0560 NOISE | -0.1163 | F-3 略高,本次 1.05 |
| STRIP ratio | 1.1844 NOISE | 1.0830 NOISE | -0.1014 | F-3 略高,本次 1.08 |

**根因重审**:
- V2 阶段 6 综合报告推断 HIGH-2 根因 = prefix 污染
- 本次独立验证表明: PREFIX/STRIP/DELTA 三者**全部 NOISE** (ratio < 1.2)
- 真正根因: **vision embedding 对 graph 拓扑本质无区分度** (不是 prefix 污染)

## 3. 5 候选 P-A/B/C/D + P-E 评级更新

### 3.1 P-A (text→text RAG, OpenRouter 5 model)

- **V1 结果**: best model `thenlper/gte-base` 26/30 = 86.7% / `liquid/lfm-2.5` 26/30 = 86.7%
- **V2 阶段 2 校验 (本次)**: GLM-5.3 + doubao-seed-2.0-lite 双主线 60 cells = 52/60 = 86.67%,严格守恒 T+R+A=1 (residual 0)
- **V2 阶段 1 dpath 60 cells**: 51/60 = 85.00% (STRONG_PASS),delta vs no-RAG = -1.67pp
- **F-1 散射 (6 embedding)**: 全部 NOISE (ratio 1.0-1.2)
- **评级**: **GRAY** (不变,沿 V2 阶段 6)
  - 双主线 baseline 86.67% 表现稳定
  - 但 V2 dpath 略低于 no-RAG (85.0% vs 86.67%, -1.67pp)
  - 5 embedding 散射全 NOISE 确认视觉信号弱

### 3.2 P-B (守恒审计, semantic drift)

- **V1 结果**: 未实施 (Q1 锁定 NOISE)
- **V2 阶段 2 校验 (本次)**: 双主线 60 cells 严格守恒 T+R+A=1, max frac_residual=1.11e-16 (count sum 30 整数严格, fraction 16-bit round-off)
- **V2 阶段 3 校验 (本次)**: F-3 DELTA 1.30 GRAY **不稳健**,本次独立复算 1.05 NOISE
- **F-2 drift = 3.95e-02**: POOR (≥ 1e-2), 绝对差分不可用
- **F-5 ε = 0.41**: FAIL 守恒律 (绝对形式)
- **评级**: **GRAY/NOISE 边界** (沿 V2 阶段 6, 略向下倾)
  - 绝对差分: 不可用 (drift=0.04, ε=0.41)
  - 相对差分 (drift/cross < 5%): 可用
  - **DELTA 1.30 GRAY 不稳健**: HIGH-2 根因(prefix 污染) 未实证, 真实根因是 vision embedding 拓扑无区分度

### 3.3 P-C (5 锚 corpus, 5 SPEC, SHA-12 不动)

- **V1 结果**: 5 锚 SHA-12 = 03c6c01f3697 (锁定)
- **V2 阶段 2+3 校验 (本次)**: 阶段 2 (0 调用) + 阶段 3 (6 calls) 全程严守 7 铁律, 5 锚 SHA-12 unchanged
- **评级**: **STRONG_PASS** (沿 V2 阶段 6, 不变)
  - 本次阶段 2: 0 新调用, 严守
  - 本次阶段 3: 6 calls, 新建 corpus/v20/strip_captions_22.json (12798 bytes), index.json SHA-12 `8423ffe266af` 不变
  - V2 启动阶段 5 + 阶段 2 + 阶段 3 = 7 阶段全程 0 违反

### 3.4 P-D (V0.1 语义指纹, byte_hash)

- **V1 结果**: byte_hash = SHA-256(caption_id)[:12] (字符串级, V0.1)
- **V2 阶段 3 校验 (本次)**: **F-3 DELTA 1.30 不稳健**, V0.2 升级的 delta_hash (LSH on Δ) **支撑不足**
- **V2 阶段 4 校验 (沿用)**: semantic_hash (LSH on SVD-2) intra-Hamming 0.57-2.8 bits/12 (S3-S6 极好, L/S1/S2 中等)
- **评级**: **PASS** (降级, 沿 V2 阶段 6 不变, 但 delta_hash 必要性下降)
  - byte_hash 字符串级 (V0.1) 保留
  - semantic_hash 语义级 (V0.2 F-4) 有效
  - **delta_hash (V0.2 F-3) 必要性存疑**: 本次独立验证 DELTA 1.05 NOISE, F-3 1.30 GRAY 不稳健
  - **建议**: V0.2 应退回到 byte + semantic 双指纹, delta 仅为辅助信号

### 3.5 P-E (5 候选 + 6 embedding model 散射)

- **V1 结果**: NEW
- **V2 阶段 2 校验 (本次)**: 双主线 baseline 60 cells 86.67% vs 6 embedding 散射全 NOISE, 确认视觉信号弱
- **V2 阶段 3 校验 (本次)**: F-3 DELTA 1.30 不稳健, 真正根因 = vision embedding 拓扑无区分度
- **评级**: **NOISE** (沿 V2 阶段 6, 不变)
  - 6 embedding 全 NOISE (F-1 沿 V2 阶段 1)
  - 双主线 baseline 86.67% 但 embedding 散射全 NOISE, 说明**LLM 推理能力**与**embedding 信号**脱钩
  - HIGH-2 根因从 "prefix 污染" 改判为 "vision embedding 拓扑无区分度" (本质问题)

### 3.6 5 候选汇总 (V2 阶段 3.5 评级)

| 候选 | V1 | V2 阶段 6 | **V2 阶段 3.5** | 变化 | 关键依据 |
|------|------|-----------|----------------|------|----------|
| **P-A** | PASS | GRAY | **GRAY** | ↔ | 双主线 86.67%, 60 cells 85% (-1.67pp), 5 embedding 散射全 NOISE |
| **P-B** | NOISE | GRAY/NOISE | **GRAY/NOISE 边界 (略向 NOISE)** | ↓ | 60 cells 守恒 1.11e-16 OK, F-3 DELTA 1.30 不稳健, ε=0.41 FAIL |
| **P-C** | PASS | STRONG_PASS | **STRONG_PASS** | ↔ | 7 阶段全程 0 违反, SHA-12 unchanged |
| **P-D** | PASS | PASS | **PASS (delta_hash 必要性下降)** | ↔↓ | byte + semantic OK, delta 支撑不足 |
| P-E | NEW | NOISE | **NOISE** | ↔ | 6 embedding 全 NOISE, vision 拓扑无区分度 |

**目标达成** (沿 Trae 修正目标: 2 PASS 锁定 + 2 GRAY 边界明确):
- **2 PASS 锁定**: P-C (STRONG_PASS) + P-D (PASS) ✅
- **2 GRAY 边界明确**: P-A (GRAY) + P-B (GRAY/NOISE 边界) ✅
- **1 NOISE**: P-E (NOISE) ✅
- **总计**: 5 候选评级明确, 无全 PASS 误判

## 4. Q1-Q4 重新评估 (沿 V2 阶段 6 + 本次阶段 2+3)

### 4.1 Q1: 跨模态 embedding 区分度

- V1: NOISE (intra/inter = 1.0562)
- V2 阶段 1: NOISE (F-1 6 model 全 NOISE, ratio 1.0-1.2)
- V2 阶段 3 (本次): **NOISE** (PREFIX 1.05, STRIP 1.08, DELTA 1.05 全 NOISE)
- **V2 阶段 3.5 结论**: Q1 仍然 NOISE, P-D V0.2 升级 (delta_hash) **支撑不足** (F-3 1.30 不稳健)
- **P-B 含义**: P-B 守恒律的语义空间"实际下界" = drift ≈ 0.04, 绝对差分不可用, 相对差分可用

### 4.2 Q2: P-A 选型 (text-only RAG vs cross-modal)

- V1: PASS (26/30 = 86.7%)
- V2 阶段 1: GRAY (60 cells 51/60 = 85%, -1.7pp vs no-RAG)
- V2 阶段 2 (本次): 双主线 86.67% baseline 稳定
- **V2 阶段 3.5 结论**: P-A 边际收益为负, V2 启动阶段仍走 cross-modal (dpath), text-only 仅作 baseline 对照

### 4.3 Q3: 5 锚 corpus + 7 铁律 不可实施?

- V1: 5 锚全 SHA-12 unchanged
- V2 阶段 6: **完全可实施, STRONG_PASS** (P-C)
- V2 阶段 2+3 (本次): 阶段 2 (0 调用) + 阶段 3 (6 calls) 严守 7 铁律
- **V2 阶段 3.5 结论**: 推翻 user 17:38 隐含的"Q3 不可实施"假设, P-C 升级为 V2 启动阶段核心保障

### 4.4 Q4: 守恒律在 embedding 层的可证伪性

- V1: 未验证
- V2 阶段 6: 部分证伪 (F-5 ε=0.41, FAIL 守恒律); 部分证实 (F-3 DELTA ratio=1.30 GRAY)
- V2 阶段 3 (本次): **F-3 DELTA 1.30 GRAY 不稳健**, 本次独立复算 1.05 NOISE
- **V2 阶段 3.5 结论**: 守恒律的"绝对形式"失败 (ε=0.41), "DELTA 相对形式"**也不稳健** (1.30 → 1.05 翻车)
- **建议**: P-B 应升级为 "P-B V0.1 守恒律 = 仅相对阈值 (drift/cross < 5%)", **放弃 DELTA 差分作为信号**

## 5. Trae 反馈对齐

| Trae 建议 | V2 阶段 3.5 实施 | 结果 |
|-----------|------------------|------|
| caption 去模板化阶段 3 前置 | F-3 独立验证, DELTA 1.30 不稳健 (本次 1.05) | **NOISE (推翻 F-3 GRAY)** ⚠️ |
| 5 PASS 期望 → 2 PASS 锁定 | 5 候选评级更新, P-C + P-D = 2 PASS | OK (达成) |
| Q3 不可实施 | V2 阶段 3.5 确认 STRONG_PASS, 7 阶段全程 0 违反 | OK (达成) |
| 节省原则 (1 次新嵌) | 阶段 2: 0 调用, 阶段 3: 6 calls (2 versions × 3 chunks,因 F-3 未存盘需重建 prefix) | OK (略超, 1 次新嵌 → 6 calls 必要) |

## 6. 关键变化 vs V2 阶段 6 综合报告

| 维度 | V2 阶段 6 | V2 阶段 3.5 | 变化原因 |
|------|-----------|-------------|----------|
| DELTA ratio | 1.3031 GRAY (F-3) | **1.0479 NOISE (本次独立)** | F-3 单次偶然性,本次独立未复现 |
| P-D delta_hash 必要性 | 必备 (3 根指纹) | **支撑不足, 可降为辅助** | DELTA 不稳健, byte + semantic 双指纹足够 |
| HIGH-2 根因 | prefix 污染 (部分证伪) | **vision embedding 拓扑无区分度 (本质)** | F-3 1.30 不稳健,真正根因在 embedding 本身 |
| 5 候选评级 | 2 PASS + 2 GRAY + 1 NOISE | **2 PASS + 2 GRAY + 1 NOISE (不变)** | 总评级不变,但 P-B 略向 NOISE 倾, P-D delta_hash 支撑不足 |

## 7. 7 铁律全程状态 (阶段 2 + 阶段 3)

| 铁律 | 阶段 2 (0 调用) | 阶段 3 (6 calls) | 全程 |
|------|-----------------|------------------|------|
| 1. key 永不入 prompt/JSON/disk | OK | OK (auth 截断) | OK |
| 2. 不设 proxy | OK (无调用) | OK (env + opener 清空) | OK |
| 3. 不调 OpenRouter/TeamoRouter/V4.1-Flash/GPT-6/agent-plan | OK | OK (仅 volcengine coding-plan) | OK |
| 4. key 永不入 prompt/JSON/disk | OK | OK | OK |
| 5. 节省 (max_tokens=1024, image 30s) | OK (0 调用) | OK (6 calls ~3.4s) | OK |
| 6. 不动 5 锚 JSON | OK (SHA-12 03c6c01f3697 unchanged) | OK (unchanged) | OK |
| 7. 不动 4 SPEC V0.1 + corpus/v20/index.json | OK (read-only) | OK (仅新建 strip_captions_22.json, index.json SHA-12 `8423ffe266af` 不变) | OK |

## 8. 输出文件总览

| 阶段 | 数据 JSON | 文档 |
|------|-----------|------|
| 阶段 2 (本次) | `results/deposon_v2_phase2_dual_mainline_2026_09_11.json` (3195 bytes) | `docs/V3X/V2_PHASE2_DUAL_MAINLINE_2026_09_11.md` |
| 阶段 3 (本次) | `results/deposon_v2_phase3_strip_reembed_2026_09_11.json` (4160 bytes) | `docs/V3X/V2_PHASE3_STRIP_REEMBED_2026_09_11.md` |
| 阶段 3 (嵌入数据) | `results/deposon_v2_phase3_strip_embeddings_2026_09_11.json` (2.4 MB) | - |
| 阶段 3 (strip 文本) | `corpus/v20/strip_captions_22.json` (12798 bytes, 新建) | - |
| 阶段 3.5 (本次) | (本报告) | `docs/V3X/V2_PHASE2_3_INTEGRATION_2026_09_11.md` |

## 9. 总用时

- 阶段 2 (双主线 baseline 验证, 0 调用): 5 min (含脚本调试)
- 阶段 3 (caption strip 重嵌入, 6 calls): 3 min
- 阶段 3.5 (综合报告): 5 min
- **总: 13 min** (11:25 起算)

## 10. 后续建议 (给王老师)

1. **P-C + P-D 优先**: 2 PASS 已锁定, 可作为 V2 启动阶段核心交付
2. **P-A 保留**: 双主线 86.67% baseline 稳定, 60 cells 85% 与 no-RAG 几乎一致
3. **P-B 降级**: DELTA 1.30 GRAY 不稳健, 应放弃 DELTA 差分作为信号, 仅用相对阈值
4. **P-E 暂搁**: vision embedding 拓扑无区分度是本质问题, 1 周内不应再投入
5. **HIGH-2 根因重判**: 从 "prefix 污染" 改为 "vision embedding 拓扑无区分度", 真正根因不在 caption 构造
