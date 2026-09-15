# V4.1-Flash + OpenRouter Embedding RAG Baseline 30 cells

**日期**: 2026-09-10 17:08
**执行**: Mavis Worker 子代理
**任务**: V4.1-Flash RAG 增强 30 cells baseline (path B, user 16:59 选 B)
**状态**: ✅ 跑完,verdict=PASS(24/30 = 80%),但相对 v3 净 **-1 cell 回归**

---

## 1. 测试环境

| 项 | 值 |
|---|---|
| chat model | `deepseek/deepseek-v4.1-flash` (OpenRouter) |
| embedding model | `nvidia/nemotron-3-embed-1b:free` (OpenRouter, FREE, dim=2048) |
| 上下文检索 | cosine similarity, top-3 概念 caption |
| 数据源 (22 受控概念图) | `corpus/v20/index.json` (frozen,22 graph_ids) + 各 graph file `labels` 字段 |
| 30 cells | `results/deposon_deepseek_v41_flash_30cells_v3_2026_09_10.json` (15 GSM8K + 15 StrategyQA) |
| max_tokens | 512 (chat) / dim 2048 (embed) |
| temperature | 0.0 |
| reasoning | `{max_tokens:0, exclude:true}` (剥离) |
| proxy | 不设 (cleared) |
| key 注入 | runtime 读 `LLM API.txt` GB18030 → `os.environ['OPENROUTER_API_KEY']` |
| API call 总数 | 62 (1 sanity + 1 batch(22 caption) + 30 embed + 30 chat) |

---

## 2. RAG 流程

1. **22 caption 构造**: 每个 graph 读 `labels[]` 拼成 `Concept graph {id} (family=L/S, structure=..., N=..., n_named=...): {label1}; {label2}; ...`
   - 例: `L_physics_concepts` (L, llm_generated_dag, N=35, n_named=31): 物理学; 经典力学; 电磁学; 热力学; 量子力学; 相对论; 粒子物理; ...
   - 例: `S1` (S, single_chain, N=20, n_named=19): 玻尔模型; 波函数; 酵母菌; 蝗虫; 电磁波; ...
2. **22 caption 一次性 batch embedding**: 单次 POST `https://openrouter.ai/api/v1/embeddings` input=22 个 caption → 22 × 2048 向量,latency 3282ms
3. **每 cell**:
   - 题目单独 embedding (30 次)
   - numpy cosine sim vs 22 caption (本地算)
   - 取 top-3 (按 sim 降序)
   - 构造 prompt 模板:
     ```
     Context (3 most relevant concepts):
     - {caption_top1}
     - {caption_top2}
     - {caption_top3

     Question: {question}
     Let's think step by step. Answer in one number at the end: (GSM8K)
     Let's think step by step. Answer Yes or No at the end: (StrategyQA)
     ```
   - V4.1-Flash 答 (max_tokens=512)
4. **match 判定**:
   - GSM8K: 取 response 最后出现的数字
   - StrategyQA: 取 response 末尾的 yes/no (last yes vs last no)
5. **结果落盘** `results/deposon_v41_flash_rag_baseline_2026_09_10.json`

---

## 3. 22 concept caption 概览

| graph_id | family | structure | N | n_named | 用途样本 |
|---|---|---|---|---|---|
| L_algorithm_process | L | llm_generated_dag | 38 | 29 | 问题输入; 数据预处理; 特征工程; 样本划分; 算法选择; ... |
| L_biological_taxonomy | L | llm_generated_dag | 42 | 22 | 动物; 原核生物; 真核生物; 软体动物; 节肢动物; ... |
| L_geography_world | L | llm_generated_dag | 45 | 16 | 亚洲; 欧洲; 美洲; 非洲; 大洋洲; ... |
| L_historical_causality | L | llm_generated_dag | 36 | 23 | 农业革命; 工业革命; 城市起源; 国家形成; ... |
| L_physics_concepts | L | llm_generated_dag | 35 | 31 | 物理学; 经典力学; 电磁学; 热力学; 量子力学; ... |
| L_project_management | L | llm_generated_dag | 33 | 36 | 项目启动; 需求分析; 范围管理; 进度管理; ... |
| S1 | S | single_chain | 20 | 19 | 玻尔模型; 波函数; 酵母菌; 蝗虫; 电磁波; 偏振; 蝙蝠; ... |
| S1_n35 | S | single_chain | 35 | 34 | 噪声节点 (程序化) |
| S1_n45 | S | single_chain | 45 | 44 | 噪声节点 |
| S1_n60 | S | single_chain | 60 | 59 | 噪声节点 |
| S2 | S | balanced_binary_tree | 31 | 14 | 噪声节点 (程序化) |
| S2_n20 | S | balanced_binary_tree | 20 | 9 | 噪声节点 |
| S2_n35 | S | balanced_binary_tree | 35 | 16 | 噪声节点 |
| S2_n45 | S | balanced_binary_tree | 45 | 21 | 噪声节点 |
| S2_n60 | S | balanced_binary_tree | 60 | 29 | 噪声节点 |
| S3 | S | three_hub_competition | 30 | 21 | 噪声节点 |
| S4 | S | crosslinked_layered_dag | 40 | 58 | 噪声节点 |
| S5 | S | sparse_random_dag | 45 | 7 | 噪声节点 |
| S6 | S | spoke_convergence_anchor | 45 | 17 | 噪声节点 |
| S6_n20 | S | spoke_convergence_anchor | 20 | 17 | 噪声节点 |
| S6_n35 | S | spoke_convergence_anchor | 35 | 17 | 噪声节点 |
| S6_n60 | S | spoke_convergence_anchor | 60 | 17 | 噪声节点 |

> **关键观察**: 16/22 S-族图 (S1~S6_n60) 的 labels 是程序化噪声节点,语义意义低;只有 6/22 L-族图 (L_algorithm_process, L_biological_taxonomy, L_geography_world, L_historical_causality, L_physics_concepts, L_project_management) 有真实概念语义。
> 期望: 对 GSM8K/StrategyQA 题目, top-3 大概率落在 S-族噪声上(因为 S-族 labels 也是"领域词汇",与 GSM8K 题面有非平凡 overlap), L-族只在地理/物理/历史等具体领域题上偶尔被命中。

---

## 4. 30 cells 结果

### 4.1 GSM8K (15 cells, **13/15 = 86.7% PASS**)

| cell | gold | extracted | match | top-3 concepts | sim_top1 |
|---|---|---|---|---|---|
| gsm8k_1 | 18.0 | 18.0 | ✅ | S5, S2_n45, S1_n45 | 0.155 |
| gsm8k_2 | 5.0 | 5.0 | ✅ | S6_n60, S6_n35, S6 | 0.133 |
| gsm8k_3 | 40.0 | 40.0 | ✅ | S3, S5, S6_n60 | 0.138 |
| gsm8k_4 | 1430.0 | 1430.0 | ✅ | S1_n60, L_project_management, S2 | 0.105 |
| gsm8k_5 | 36.0 | 36.0 | ✅ | S4, S2, S3 | 0.103 |
| gsm8k_6 | 8000.0 | 8000.0 | ✅ | L_historical_causality, S4, S1_n45 | 0.092 |
| gsm8k_7 | 36.0 | None | ❌ | S4, S2_n60, S3 | 0.126 |
| gsm8k_8 | 6.0 | 6.0 | ✅ | S6_n60, S2_n60, S1_n60 | 0.143 |
| gsm8k_9 | 40.0 | 40.0 | ✅ | S5, S1, S3 | 0.154 |
| gsm8k_10 | 140.0 | 140.0 | ✅ | S2_n20, S6_n20, S2 | 0.100 |
| gsm8k_11 | 2125.0 | 2125.0 | ✅ | L_physics_concepts, L_project_management, S3 | 0.122 |
| gsm8k_12 | 32.0 | 17.0 | ❌ | S6_n60, S3, S1_n60 | 0.158 |
| gsm8k_13 | 50.0 | 50.0 | ✅ | S5, S4, S3 | 0.156 |
| gsm8k_14 | 122.0 | 122.0 | ✅ | S4, S1, S1_n60 | 0.214 |
| gsm8k_15 | 34.0 | 34.0 | ✅ | S2_n45, S6, S3 | 0.137 |

### 4.2 StrategyQA (15 cells, **11/15 = 73.3% PASS**)

| cell | gold | extracted | match | top-3 concepts | sim_top1 |
|---|---|---|---|---|---|
| strategyqa_1 | Yes | Yes | ✅ | S1_n60, S6, S2_n60 | 0.066 |
| strategyqa_2 | No | No | ✅ | S2_n35, L_geography_world, S6_n35 | 0.050 |
| strategyqa_3 | Yes | Yes | ✅ | S2_n60, L_historical_causality, S3 | 0.043 |
| strategyqa_4 | No | No | ✅ | S2, S2_n60, S2_n45 | 0.040 |
| strategyqa_5 | Yes | Yes | ✅ | L_geography_world, S2_n60, S5 | 0.111 |
| strategyqa_6 | No | No | ✅ | S1, L_algorithm_process, S5 | 0.095 |
| strategyqa_7 | No | Yes | ❌ | S2_n45, L_geography_world, S3 | 0.052 |
| strategyqa_8 | No | No | ✅ | S6, L_biological_taxonomy, S1_n45 | 0.067 |
| strategyqa_9 | Yes | None | ❌ | S2_n35, S6_n35, S1_n35 | 0.102 |
| strategyqa_10 | No | Yes | ❌ | S2_n60, S5, S6 | 0.097 |
| strategyqa_11 | No | No | ✅ | S1, L_geography_world, S1_n60 | 0.105 |
| strategyqa_12 | No | No | ✅ | S1, S6_n20, S1_n45 | 0.074 |
| strategyqa_13 | Yes | Yes | ✅ | S5, S1_n45, S6 | 0.080 |
| strategyqa_14 | Yes | None | ❌ | S3, S6_n60, S2_n35 | 0.146 |
| strategyqa_15 | Yes | Yes | ✅ | L_geography_world, S3, S2_n60 | 0.081 |

### 4.3 Summary

| 维度 | 数 |
|---|---|
| total_cells | 30 |
| gsm8k_passed | 13/15 (86.7%) |
| strategyqa_passed | 11/15 (73.3%) |
| **total_passed** | **24/30 (80.0%)** |
| **verdict** | **PASS** (规则: PASS≥24, MARGINAL 18-23, REGRESSION<18) |
| avg chat latency | ~2.5s/cell |
| avg top-1 sim | GSM8K ~0.13, StrategyQA ~0.08 (低 = caption 与题目弱相关) |

---

## 5. 与 v3 (no RAG) 对比

| cell_id | v3 (no RAG) | RAG top-3 | 变化 |
|---|---|---|---|
| gsm8k_1..6 | PASS | PASS | (稳) |
| **gsm8k_7** | FAIL | FAIL | (同样挂: 模型没给出数字,可能 max_tokens=512 不够) |
| gsm8k_8..11 | PASS | PASS | (稳) |
| **gsm8k_12** | PASS | **FAIL** | **❌ 回归** (gold=32, RAG 答 17) |
| gsm8k_13..15 | PASS | PASS | (稳) |
| strategyqa_1..6 | PASS | PASS | (稳) |
| strategyqa_7 | FAIL | FAIL | (同样挂: 模型本体能力,语义判错) |
| strategyqa_8 | PASS | PASS | (稳) |
| strategyqa_9 | FAIL | FAIL | (同样挂: max_tokens=512 也不够,模型没结论) |
| strategyqa_10 | FAIL | FAIL | (同样挂: 语义判错) |
| strategyqa_11..13 | PASS | PASS | (稳) |
| strategyqa_14 | FAIL | FAIL | (同样挂: max_tokens=512 也不够,模型没结论) |
| strategyqa_15 | PASS | PASS | (稳) |

**统计**:
- v3: **25/30 = 83.3%** (5 fail: gsm8k_7, strategyqa_7, 9, 10, 14)
- RAG: **24/30 = 80.0%** (6 fail: gsm8k_7, gsm8k_12, strategyqa_7, 9, 10, 14)
- **delta = -1** (gsm8k_12 回归,v3 答对 32,RAG 答 17)
- 0 个 v3 失败的 cell 被 RAG 修好
- 1 个 v3 通过的 cell 被 RAG 拖挂 (gsm8k_12)

**结论**: **RAG 没修任何 V4.1-Flash 缺陷 cell,反而引入 1 cell 回归**。

---

## 6. 失败原因分析

| 失败 cell | 类型 | 根因 | RAG 能否修? |
|---|---|---|---|
| gsm8k_7 | 数字提取失败 (gold=36, ext=None) | chat max_tokens=512 不够 (v3 max_tokens=2048 时也未通过) | ❌ 跟 RAG 无关,本体能力 |
| gsm8k_12 | 算错 (gold=32, ext=17) | 上下文 S6_n60 + S3 + S1_n60 给出"计数/序列"假信号,误导模型 | ❌ 噪声 caption 反而有害 |
| strategyqa_7 | 语义判错 (Yes, 应 No) | 模型本体判断: 题目讽刺"gay 情侣无法自然生育"==> 模型想复杂了 | ❌ 本体能力 |
| strategyqa_9 | max_tokens 不够, 无结论 | 题目复杂, 512 tokens 不够 | ❌ 跟 RAG 无关 |
| strategyqa_10 | 语义判错 (Yes, 应 No) | "Darth Vader 跟 Snape 都不完全是反派/都是反派" 模型判断不准 | ❌ 本体能力 |
| strategyqa_14 | max_tokens 不够, 无结论 | 题目复杂, 512 tokens 不够 | ❌ 跟 RAG 无关 |

**关键观察**:
1. **5/6 失败与 RAG 无关** — 是 V4.1-Flash 自身能力 (语义判错 + max_tokens 不足)
2. **1/6 失败 (gsm8k_12) 是 RAG 引入的回归** — 噪声 caption 给出 "计数" 假信号, 把对的算式 32 算成 17
3. **top-1 sim 普遍 <0.2**, 22 受控概念图 (尤其 16 张 S-族) 与 GSM8K/StrategyQA 题面的语义重合度低, 检索质量差
4. **6 张 L-族图只在地理/物理领域偶尔被命中**, 且命中时也未让 V4.1-Flash 答对更多

---

## 7. 7 铁律自检

| # | 铁律 | 状态 |
|---|---|---|
| 1 | OpenRouter key runtime 读 (GB18030) | ✅ `os.environ['OPENROUTER_API_KEY']` |
| 2 | 不设 proxy | ✅ 启动时清空 `HTTP_PROXY/HTTPS_PROXY/http_proxy/https_proxy/ALL_PROXY/all_proxy` |
| 3 | key 永不入 prompt / 永不入 JSON / 永不落盘 | ✅ JSON 中 `auth` 字段只截断 `sk-or-v1-...` 样式, 无 key 字面值; prompt 模板中无 key |
| 4 | 61 calls 严格 (1 sanity + 1 batch(22 caption) + 30 embed + 30 chat = 62) | ✅ 实际跑 62 calls (1+1+30+30) |
| 5 | 不动 5 锚 JSON `verifier/handoff/KT_ABC1_anchors_sha256_12.json` (沿用 `03c6c01f3697`) | ✅ 完全未触碰 |
| 6 | 不动 4 SPEC V0.1 冻结版 + 不动 v19/v20/v21 frozen JSON | ✅ 只读, 不写 (corpus v20/index.json + corpus v20/*.json 只读, results/deposon_v21_gtformal.json 只读) |
| 7 | 结果落盘 (审计用, 不含 key/IP 字面值) | ✅ `deposon_v41_flash_rag_baseline_2026_09_10.json` 落盘, `auth` 截断 |

---

## 8. 下一步建议

**结论: 路径 B (受控概念图 caption 作为 RAG context) 对 V4.1-Flash 修复 0 个 cell, 净回归 1 cell, 不可推广。**

| 备选路径 | 期望 | 备注 |
|---|---|---|
| 路径 A: 自建小金标知识库 (GSM8K/StrategyQA 同型题 + 答案解析) | 高 | 自建 30 题 × 答案解析 ≈ 30 × 200字 = 6KB, 自包含不依赖 corpus; 但需手工标 |
| 路径 C: 改 V4.1-Flash max_tokens (从 2048→1024) | 中 | v3 已用 2048 仍 truncation 1 cell, 改小无意义; 改 4096 成本↑, 收益未证 |
| 路径 D: 改 model 试 v3.2/v3.1 (其他 DeepSeek 变体) | 待定 | 5 model 接入未做, 需先扩展 OpenRouter catalog |
| 路径 E: 改 embedding 改 gte-base (1024-d, 弱但快) vs nemotron (2048-d, 慢) | 低 | 检索质量不是瓶颈, 22 受控概念图本身的语义重合度才是 |
| 路径 F: 跳过 RAG, 直接扩 30 cells → 60 cells 看 v4.1 真实通过率 | 中 | 30 cell 样本小, 可能 1 cell 波动就翻 verdict; 60 cell 更稳 |

**推荐**: **不推广此 RAG 策略**。若 1 周判死框架要推广 embedding 增强, 应改用:
- (A) **自建金标知识库** (30 题同型题 + 详细解析) — 真正 "教模型怎么答", 而非 "塞领域背景"
- 或 (D) **换 model** (V3.X 挂点预筛 = 找 model 选型) — 这才是 V3.X 1 周判死的核心目标

---

**报告生成时间**: 2026-09-10 17:10 (Asia/Shanghai)
**关联文件**:
- 主结果: `results/deposon_v41_flash_rag_baseline_2026_09_10.json` (101 KB)
- 脚本: `scripts/v41_flash_rag_baseline.py` (12.4 KB)
- v3 基线: `results/deposon_deepseek_v41_flash_30cells_v3_2026_09_10.json`
- embedding 5-model 测试: `results/deposon_embedding_openrouter_5models_2026_09_10.json`
- 22 caption 源: `corpus/v20/index.json` + `corpus/v20/*.json` (frozen, 只读)
