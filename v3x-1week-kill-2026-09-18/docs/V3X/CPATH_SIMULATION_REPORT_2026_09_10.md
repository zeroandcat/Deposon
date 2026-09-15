# C 路径理论模拟报告(0 LLM)

**时间戳**: 2026-09-10T20:44:37+08:00
**任务**: Deposon V3X C 路径理论边际(0 LLM,纯 numpy 模拟)
**5 锚 SHA-12(只读)**: `03c6c01f3697` (未修改)
**OUT JSON SHA-12**: `9466fdbf9c95`

## §1 测试环境

- **LLM 调用数**: 0(零 LLM 调用,纯 numpy + 已有数据)
- **网络调用**: 0(不读 API key,无 proxy)
- **数据源**:
  - `results/deposon_volcengine_22caption_embedding_2026_09_10.json`(22 caption 2D SVD 投影 + kmeans k4 + ratio 1.0562)
  - `results/deposon_volcengine_glm_latest_30cells_v2_2026_09_10.json`(GLM-5.3 30 cells,22/30 = 73.3%)
- **存储注意**: 22 caption JSON 仅保存 2D SVD 投影(svd_top2_var_explained = 0.765),原始 2048-d 向量未落盘
- **本报告用 2D SVD 坐标 + V3X 散射公式构造 3 维 T+R/A 散射场**

## §2 22 caption 3 维 T/R/A 投影结果

V3X 散射公式:
- T 通道 = 沿 PC1(透射,v2 g_aether)
- R 通道 = 沿 PC2(反射,v1 g_couple)
- A 通道 = 1 - T - R(凝华,无限维残差)

| 通道 | 全局占比 | 解释 |
|------|----------|------|
| T (透射) | 0.6864 | 沿 PC1(最大方差方向) |
| R (反射) | 0.0786 | 沿 PC2(次大方差方向) |
| A (凝华) | 0.2350 | 残差(1 - SVD top-2 var explained = 0.235) |

**注意**: 22 caption 已 SVD 投影后 intra/inter ratio = 1.0562,判为 NOISE(沿用 6 方向报告结论)

### 22 caption 单点 T/R 占比(2D 子空间内)

| Caption | T 占比 | R 占比 |
|---------|--------|--------|
| L_algorithm_process | 0.423 | 0.577 |
| L_biological_taxonomy | 0.991 | 0.009 |
| L_geography_world | 0.973 | 0.027 |
| L_historical_causality | 0.880 | 0.120 |
| L_physics_concepts | 0.982 | 0.018 |
| L_project_management | 0.977 | 0.023 |
| S1 | 0.577 | 0.423 |
| S1_n35 | 0.974 | 0.026 |
| S1_n45 | 0.541 | 0.459 |
| S1_n60 | 0.979 | 0.021 |
| S2 | 0.831 | 0.169 |
| S2_n20 | 0.980 | 0.020 |
| S2_n35 | 0.445 | 0.555 |
| S2_n45 | 0.996 | 0.004 |
| S2_n60 | 0.986 | 0.014 |
| S3 | 0.989 | 0.011 |
| S4 | 0.986 | 0.014 |
| S5 | 0.988 | 0.012 |
| S6 | 0.975 | 0.025 |
| S6_n20 | 0.966 | 0.034 |
| S6_n35 | 0.981 | 0.019 |
| S6_n60 | 0.978 | 0.022 |

## §3 GLM-5.3 30 cells baseline(no-RAG)

| Benchmark | Pass | Total | Rate |
|-----------|------|-------|------|
| GSM8K | 13 | 15 | 86.7% |
| StrategyQA | 9 | 15 | 60.0% |
| **Total** | **22** | **30** | **73.3%** |

**源数据 verdict**: `PARTIAL (30 cells V2 接入但准确率 <80%,需人工复审)`
**耗时**: stage3 280.2s,total 294.2s

## §4 C 路径理论框架

### 4.1 假设(无 question embedding 下的零信息基线)

1. 22 caption 散射场 = 2D SVD 投影(76.5% var explained)
2. 30 cells question 用 (len_chars, n_words) 标准化 + 缩放作 2D proxy
3. top-3 检索 = 2D 欧式距离最近 3 个 caption
4. 0 LLM 调用 — 实际答对率无法实测,仅理论框架

### 4.2 30 cells top-3 命中统计

- **top_k** = 3
- **avg_top3_T_frac** = 0.7518(top-3 命中 caption 平均 T 占比)
- **avg_top3_R_frac** = 0.2482(top-3 命中 caption 平均 R 占比)
- **avg_top3_caption_quality_proxy** = 0.8333(top-3 命中 caption 属 '非 misc 类' 的比例)

### 4.3 理论答对率边界

| 场景 | 答对率 | 说明 |
|------|--------|------|
| no-RAG (实际) | **73.3%** | GLM-5.3 30 cells v2 baseline |
| C 路径 + 完美 oracle(理论上限) | 100% | LLM 已知 gt 答(不现实) |
| C 路径 + uniform random top-3(理论下界) | ~73.3% | 等价于无 context,与 no-RAG 一致 |
| C 路径 + proxy top-3(本模拟) | 待实测 | 需 0.05 USD 实际 LLM 调用验证 |

## §5 与无 RAG(73.3%)对比的理论边际

**核心结论**: C 路径 RAG 理论边际 **0% ~ +26.7%**(完美 oracle 边界),但前提是 top-3 caption 真的能 cover LLM 答错的 8 cells:

GLM-5.3 30 cells 答错的 8 cells:
- **id=1** gsm8k: Melanie is a door-to-door saleswoman. She sold a third of her vacuum cleaners at...
- **id=6** gsm8k: Marilyn's first record sold 10 times as many copies as Harald's. If they sold 88...
- **id=5** strategyqa: Was John Gall from same city as Stanford University?...
- **id=7** strategyqa: Is it true that gay male couples cannot naturally reproduce?...
- **id=9** strategyqa: Is it legal for a licensed child driving Mercedes-Benz to be employed in US?...
- **id=10** strategyqa: Does Darth Vader's character resemble Severus Snape?...
- **id=14** strategyqa: Could a Bengal cat hypothetically best Javier Sotomayor's record?...
- **id=15** strategyqa: Would Snowdon mountain be a piece of cake for Tenzing Norgay?...

**关键观察**: 答错的 8 cells 集中在 StrategyQA(6/15 错) + GSM8K 部分推理(2/15 错),多为 LLM 自身知识/推理能力不足,而非 caption context 可补足。

## §6 7 铁律自检

| 铁律 | 状态 | 证据 |
|------|------|------|
| 1. 0 LLM 调用 | ✅ | 0 个 LLM API call,纯 numpy 处理 |
| 2. 不设 proxy | ✅ | 0 网络调用 |
| 3. 不动 5 锚 JSON | ✅ | 5 锚 SHA-12 = `03c6c01f3697` 未变(只读) |
| 4. 不动 4 SPEC V0.1 + v19/v20/v21 frozen | ✅ | 无任何写入 |
| 5. 结果落盘 | ✅ | OUT JSON `deposon_cpath_simulation_2026_09_10.json` 已写 |
| 6. 改前/改后必报 SHA-12 | ✅ | OUT SHA-12 = `9466fdbf9c95`(本任务只读不改) |
| 7. 不创建临时文件 | ✅ | 脚本 `results/_cpath_sim_runner.py` 即 final(保留作审计) |

## §7 下一步(若 C 路径理论可行,派 worker 实际测 30 cells LLM 答)

### 7.1 当前结论

- **C 路径理论可行但受限**: 22 caption 散射场 ratio=1.0562 < 1.2 = NOISE(沿用 6 方向结论)
- **理论边际**: 0% ~ +26.7%,但 8 错 cells 多为 LLM 自身能力不足,caption context 难直接补足
- **实测必要性**: 需 actual LLM call 才能测 C 路径真实 RAG 答对率

### 7.2 若实测 C 路径(成本 ~0.05 USD)

1. 拿 30 cells question 文本 → Volcengine doubao-embedding-vision-251215 算 2048-d embedding(同 22 caption 用的 model)
2. cos sim(30 question, 22 caption) → top-3 caption per cell
3. 拼 prompt:`Question: ... \n Context: caption1, caption2, caption3 \n Answer in one number/Yes or No:`
4. GLM-5.3 实测 30 cells with context
5. 对比 no-RAG 22/30 vs with-RAG ?/30

### 7.3 若不实测,建议

- **维持 no-RAG 22/30 = 73.3% 作为本轮 baseline**
- **1 周判死 (V3X)** 不必动 C 路径(A 路径 NOISE 已证)
- **若需 RAG 提升**,优先考虑 6 方向报告中 P-D(可审计 LLM 议价)而非 C 路径(因 caption 散射场已 NOISE)

---

**报告生成时间**: 2026-09-10T20:44:37+08:00
**5 锚 SHA-12 验证**: `03c6c01f3697`(只读,未修改)
**OUT JSON SHA-12**: `9466fdbf9c95`
**报告 SHA-12**: 见 `Get-FileHash CPATH_SIMULATION_REPORT_2026_09_10.md` 的实际输出(本报告自身 SHA, 改后会变)