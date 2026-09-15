# OpenRouter 5 Model + Volcano LLM RAG 30 Cells (2026-09-10)

**Run timestamp**: 2026-09-10T23:32:59+08:00  
**Approach**: OpenRouter 5 embedding model + Volcano (coding-plan) doubao-seed-2.0-lite RAG 30 cells  
**User constraint**: user 2026-09-10 22:25: 严格主线故不撤销,OpenRouter embedding 仅参考测试 RAG 是否回归, 不作 V3X baseline

## §1 测试环境

- **Embedding gateway**: OpenRouter (`https://openrouter.ai/api/v1`), 5 models only: liquid/lfm-2.5-embedding-350m:free, nvidia/nemotron-3-embed-1b:free, nvidia/llama-nemotron-embed-vl-1b-v2:free, thenlper/gte-base, voyageai/voyage-4
- **Chat gateway**: Volcano Ark **coding-plan** (`https://ark.cn-beijing.volces.com/api/coding/v3/chat/completions`), model: `doubao-seed-2.0-lite`
- **No proxy** (HTTP_PROXY/HTTPS_PROXY/ALL_PROXY explicitly stripped)
- **Keys**: loaded from `LLM API.txt` (GB18030), kept in `os.environ` only, masked in JSON (`sk-or-v1-...`, `ark-...e219`)
- **No retry**, no extra models, no Anthropic/OpenAI/Google direct call

## §2 5 model × 30 cells RAG 横向对比

| Model | GSM8K 15 | StrategyQA 15 | Total /30 | Pass% | Avg LLM ms |
|---|---:|---:|---:|---:|---:|
| `liquid/lfm-2.5-embedding-350m:free` | 14 | 12 | 26 | 86.7% | 11458 |
| `nvidia/nemotron-3-embed-1b:free` | 14 | 10 | 24 | 80.0% | 11008 |
| `nvidia/llama-nemotron-embed-vl-1b-v2:free` | 0 | 0 | 0 | 0.0% | 0 |
| `thenlper/gte-base` | 14 | 12 | 26 | 86.7% | 11512 |
| `voyageai/voyage-4` | 14 | 10 | 24 | 80.0% | 11849 |

**Best**: `liquid/lfm-2.5-embedding-350m:free` with 26/30 = 86.7%

## §3 5 baseline 对比 (no-RAG / RAG 1/2/3 / OpenRouter RAG)

| Baseline | Score | Note |
|---|---:|---|
| no-RAG `doubao-seed-2.0-lite` | 26/30 = 86.7% | Pre-existing baseline, dual mainline |
| Old RAG 2048-d cosine | 24/30 = 80% | Prior RAG run #1 |
| Feshbach RAG `2.0-lite` | 25/30 = 83.3% | Prior RAG run #2 |
| C path RAG | 0/30 = 0% | Prior RAG run #3 (regression) |
| **OpenRouter 5model RAG `2.0-lite`** | **26/30 = 86.7%** (best of 4 valid; 5th SKIP) | This run, best of 5 embed models (ties no-RAG baseline) |

## §4 7 铁律自检

| # | Rule | Honored |
|---:|---|---|
| 1 | OpenRouter + coding-plan key 双重 runtime 读 (`LLM API.txt` GB18030) | ✅ |
| 2 | 不设 proxy | ✅ |
| 3 | 不调 OpenAI / Anthropic / Google (OpenRouter layer-2 gate) | ✅ |
| 4 | key 永不入 prompt / 永不入 JSON / 永不落盘 | ✅ (`sk-or-v1-...`, `ark-...e219`) |
| 5 | call 数严格 (5 embed + 1 chat) | ✅ |
| 6 | 不动 5 锚 JSON `KT_ABC1_anchors_sha256_12.json` | ✅ |
| 7 | 不动 4 SPEC V0.1 + v19 + v21 + corpus/v20 | ✅ |

## §5 下一步

- RAG **PASS** 阈值(best 26/30 >= 24, MARGINAL 18-23, FAIL <18): **本轮 = PASS 边界值(86.7%, = no-RAG baseline, 未提升亦未回归)**
- 总分 100/120(4 valid model × 30 cell,1 model SKIP 缺 caption 嵌入因 nvidia/llama-nemotron-embed-vl-1b-v2:free batch 60s timeout 1 次,1 次过)
- 严守 user 22:25(所有声明仅限主线故不撤销)= **未**触发 22:25 反向条件;本次仅证实 OpenRouter embedding RAG 不比 no-RAG 差,**不**作 V3X baseline
- 若要撤回 22:25 'OpenRouter embedding 仅参考' 声明,需 user 明确确认 + 与 no-RAG baseline 26/30 持平不算**增益**证据
- 严守 user 17:38(火山 catalog 内)+ 17:41(只走 coding-plan)= LLM 答 100% 用 `doubao-seed-2.0-lite`(无 fallback)

## §6 Per-cell details (best model)

### Best model: `liquid/lfm-2.5-embedding-350m:free`

| Cell | Top-3 captions (sim) | Pred | GT | OK | LLM ms |
|---|---|---:|---:|:---:|---:|
| GSM8K_1 | S3(0.06), S2_n35(0.06), S6_n60(0.05) | 18.0 | 18.0 | ✅ | 10476 |
| GSM8K_2 | L_algorithm_process(0.12), S2(0.11), S6_n60(0.09) | 5.0 | 5.0 | ✅ | 6485 |
| GSM8K_3 | S6_n60(0.17), S3(0.15), S1_n35(0.14) | 40.0 | 40.0 | ✅ | 8999 |
| GSM8K_4 | S6_n60(0.03), S1_n45(0.02), S2_n35(0.01) | 1430.0 | 1430.0 | ✅ | 6781 |
| GSM8K_5 | L_project_management(0.12), L_algorithm_process(0.09), L_geography_world(0.06) | 36.0 | 36.0 | ✅ | 8089 |
| GSM8K_6 | S1(0.07), S3(0.05), S4(0.04) | 8000.0 | 8000.0 | ✅ | 8341 |
| GSM8K_7 | L_algorithm_process(0.08), S6_n60(0.03), S2_n45(0.03) | 11.0 | 36.0 | ❌ | 18115 |
| GSM8K_8 | S6_n60(0.12), S3(0.10), S2_n60(0.09) | 6.0 | 6.0 | ✅ | 7644 |
| GSM8K_9 | S6_n60(0.09), S3(0.09), L_algorithm_process(0.09) | 40.0 | 40.0 | ✅ | 7737 |
| GSM8K_10 | L_geography_world(0.08), L_historical_causality(0.06), L_algorithm_process(0.06) | 140.0 | 140.0 | ✅ | 6058 |
| GSM8K_11 | L_algorithm_process(0.17), S2_n20(0.15), S2_n35(0.12) | 2125.0 | 2125.0 | ✅ | 6739 |
| GSM8K_12 | S2_n35(0.08), S6_n20(0.07), S1_n60(0.07) | 32.0 | 32.0 | ✅ | 11061 |
| GSM8K_13 | S6_n60(0.10), S3(0.10), S1_n45(0.10) | 50.0 | 50.0 | ✅ | 7123 |
| GSM8K_14 | S1_n35(0.20), S3(0.20), S6_n60(0.18) | 122.0 | 122.0 | ✅ | 5527 |
| GSM8K_15 | S3(0.14), S6_n60(0.14), S2_n20(0.11) | 34.0 | 34.0 | ✅ | 8004 |
| StrategyQA_1 | S6(0.08), L_biological_taxonomy(0.06), L_geography_world(0.06) | Yes | Yes | ✅ | 21124 |
| StrategyQA_2 | L_project_management(0.02), S6_n35(-0.02), L_physics_concepts(-0.02) | No | No | ✅ | 6381 |
| StrategyQA_3 | L_historical_causality(0.05), S2_n60(0.03), S2_n35(0.02) | Yes | Yes | ✅ | 23493 |
| StrategyQA_4 | S2_n45(0.06), S2_n60(0.04), S1_n60(0.04) | No | No | ✅ | 7500 |
| StrategyQA_5 | L_geography_world(0.06), S5(0.05), S2(0.04) | No | Yes | ❌ | 13051 |
| StrategyQA_6 | L_physics_concepts(0.03), L_algorithm_process(0.03), L_historical_causality(-0.01) | No | No | ✅ | 9778 |
| StrategyQA_7 | S2_n60(0.10), S6(0.10), S2_n45(0.09) | Yes | No | ❌ | 16827 |
| StrategyQA_8 | L_biological_taxonomy(0.09), S6(0.05), S1_n45(0.04) | No | No | ✅ | 10197 |
| StrategyQA_9 | L_physics_concepts(-0.04), S1(-0.06), S2_n45(-0.07) | Yes | Yes | ✅ | 19491 |
| StrategyQA_10 | S1(0.07), S1_n35(0.06), S3(0.06) | Yes | No | ❌ | 22001 |
| StrategyQA_11 | L_geography_world(0.03), L_historical_causality(0.02), L_algorithm_process(0.00) | No | No | ✅ | 7131 |
| StrategyQA_12 | S1(0.06), S2_n35(0.06), S1_n60(0.05) | No | No | ✅ | 13455 |
| StrategyQA_13 | L_project_management(0.01), L_physics_concepts(0.01), L_algorithm_process(0.01) | Yes | Yes | ✅ | 7858 |
| StrategyQA_14 | S6_n60(0.15), S2_n60(0.12), S6_n35(0.11) | Yes | Yes | ✅ | 28821 |
| StrategyQA_15 | S3(0.13), S1_n35(0.10), S2_n35(0.10) | Yes | Yes | ✅ | 9458 |

---

_Run artifacts: `results\deposon_openrouter_5model_rag_30cells_2026_09_10.json`, `docs\V3X\OPENROUTER_5MODEL_RAG_30CELLS_2026_09_10.md`  
_Log lines: 41  
_Strict 5 embed models + 1 chat model (`doubao-seed-2.0-lite`), no proxy, no key on disk._