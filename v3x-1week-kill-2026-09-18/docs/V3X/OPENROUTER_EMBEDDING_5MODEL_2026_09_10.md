# OpenRouter Embedding 5 Model 接入测试报告

- 时间: 2026-09-10 22:25 CST
- 任务: Mavis 派工, 22:21 user 隐含撤销 17:41 "只走 coding-plan", 测 OpenRouter embedding 5 model 必须
- JSON: `results/deposon_openrouter_embedding_5model_2026_09_10.json`
- 锚: 5 锚 sha256 `03c6c01f3697…` 不动

## §1 测试环境

- gateway: OpenRouter (`https://openrouter.ai/api/v1/embeddings`)
- key: runtime 读 `C:\Users\Administrator\Desktop\AI\LLM API.txt` (GB18030) → 提取 `sk-or-v1-[a-f0-9]{64}` → `os.environ['OPENROUTER_API_KEY']`, 永不入 prompt/JSON/落盘
- proxy: 无 (直连 OpenRouter 海外)
- API calls 预算: 14 (5 sanity + 3×3 embedding), 实跑 14
- 候选 5 model:
  1. `liquid/lfm-2.5-embedding-350m:free` (FREE, 1024-d, 512 ctx)
  2. `nvidia/nemotron-3-embed-1b:free` (FREE, 33K ctx)
  3. `nvidia/llama-nemotron-embed-vl-1b-v2:free` (FREE, multimodal, 131K ctx)
  4. `thenlper/gte-base` ($0.005/M, 768-d, 经典)
  5. `voyageai/voyage-4` ($0.06/M, Matryoshka 32K ctx)

## §2 5 model sanity 结果 (1-cell "What is 2+2?")

| # | model | http | dim | latency (ms) | 1-cell cost | sanity |
|---|---|---|---|---|---|---|
| 1 | `liquid/lfm-2.5-embedding-350m:free` | 200 | 1024 | 2511.8 | 0 | PASS |
| 2 | `nvidia/nemotron-3-embed-1b:free` | 200 | 2048 | 1278.6 | 0 | PASS |
| 3 | `nvidia/llama-nemotron-embed-vl-1b-v2:free` | 200 | 2048 | 1709.4 | 0 | PASS |
| 4 | `thenlper/gte-base` | 200 | 768 | 2248.3 | $4e-08 | PASS |
| 5 | `voyageai/voyage-4` | 200 | 1024 | 1182.2 | $4.2e-07 | PASS |

**5/5 PASS** (HTTP 200, embedding 列表非空)

## §3 3 model × 3 cells 22 caption embedding 结果

22 caption 文本(沿用 5 锚 caption_construction 三种结构):
- cell 1: `L_algorithm_process` (family=llm_dag, structure=dag)
- cell 2: `S1` (family=synthetic, structure=chain)
- cell 3: `S2` (family=synthetic, structure=tree)

| model | dim | cell1 | cell2 | cell3 | 1-cell 均价 | 备注 |
|---|---|---|---|---|---|---|
| `nvidia/nemotron-3-embed-1b:free` | 2048 | OK / 1352.9ms | OK / 1647.9ms | OK / 1333.3ms | $0 | FREE |
| `liquid/lfm-2.5-embedding-350m:free` | 1024 | OK / 2599.0ms | OK / 1843.0ms | OK / 2278.7ms | $0 | FREE |
| `thenlper/gte-base` | 768 | OK / 2219.8ms | OK / 2123.5ms | OK / 2098.6ms | ~$2e-07 | 经典 baseline |

**3 model × 3 cells = 9/9 PASS**; cell 之间 first-4 值明显不同, 非退化为单一向量。

## §4 与已有 baseline 对比

| 来源 | model | dim | 1k caption 估算成本 | 备注 |
|---|---|---|---|---|
| 火山 | `doubao-embedding-vision-251215` | 2048 | ~$0.10/1M (海外估算) | 已 baseline 26/30 |
| OpenRouter | `nvidia/nemotron-3-embed-1b:free` | 2048 | **$0** | FREE + 同 2048-d, 最划算 |
| OpenRouter | `nvidia/llama-nemotron-embed-vl-1b-v2:free` | 2048 | **$0** | multimodal, 后续可走 image+text |
| OpenRouter | `liquid/lfm-2.5-embedding-350m:free` | 1024 | **$0** | 小模型, 1024-d 仍够 22 caption |
| OpenRouter | `thenlper/gte-base` | 768 | $0.005/M | 经典 GTE, 768-d |
| OpenRouter | `voyageai/voyage-4` | 1024 | $0.06/M | Matryoshka 弹性, 贵 |

观察: 三个 FREE model 都 PASS, 维度覆盖 1024/2048; 沿 V1 跨模态检索方向 d 选 model 时, **优先 `nvidia/nemotron-3-embed-1b:free`** (FREE + 2048-d 匹配既有 doubao-embedding 维度, RAG 拼接无需重训).

## §5 7 铁律自检

1. ✅ key runtime 读 GB18030 → `os.environ['OPENROUTER_API_KEY']`, 永不入 prompt/JSON/落盘
2. ✅ 无 proxy (海外开源 gateway 直连, 符合 17:38 不变 + 22:21 撤销)
3. ✅ 不动 OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan 业务路径, OpenRouter 是海外开源 gateway 不冲突 17:38
4. ✅ `auth` 字段写 `sk-or-v1-... (key loaded from env at runtime; literal key never written to disk)`
5. ✅ 14 API calls 严格 (5 sanity + 3×3 embedding), 不重试
6. ✅ 5 锚 sha256 `03c6c01f3697…` 文件未触碰
7. ✅ 4 SPEC V0.1 + v19 + v21 + corpus/v20 未触碰

## §6 下一步 (沿 V1 跨模态检索方向 d 选 model)

候选 1 (推荐): `nvidia/nemotron-3-embed-1b:free`
- 维度 2048, 匹配已有 `doubao-embedding-vision-251215` 2048-d baseline
- FREE, 22 caption × 5 anchor 全 30 cells ≈ $0
- latency ~1.3-1.6s/cell, 30 cells ≈ 40-50s 即可完成

候选 2 (备选): `thenlper/gte-base`
- 经典 GTE 768-d, 业界有大量 pretrained 经验
- $0.005/M, 30 cells ≈ $0.0001 (≈ 0)
- 维度不匹配 2048 baseline, 需 PCA/插值才能拼接

候选 3 (多模态): `nvidia/llama-nemotron-embed-vl-1b-v2:free`
- 2048-d, multimodal, 后续若加 image → 同一空间
- FREE, 同样划算

**建议**: 30 cells 全量跑选 `nvidia/nemotron-3-embed-1b:free`; 若验证需要多模态备份, 同步跑 `llama-nemotron-embed-vl-1b-v2:free`. 此两步 + 5 锚 = 5 选 2 = 120 API calls, 全 FREE.
