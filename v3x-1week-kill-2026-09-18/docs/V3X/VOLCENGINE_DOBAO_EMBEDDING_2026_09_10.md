# 火山方舟 Doubao-Embedding-Vision 接入测试报告
**时间**: 2026-09-10 17:18 (Asia/Shanghai)
**任务 ID**: VOLCENGINE_EMBEDDING_RETEST_2026_09_10
**触发**: user 2026-09-10 17:15 纠正 base_url(用错 `/v3` → 改用 `/api/coding/v3`)
**Verdict**: ✅ **PASS 3/3**

---

## §1 测试环境

| 项 | 值 |
|---|---|
| Gateway | 火山方舟 Coding Plan |
| base_url | `https://ark.cn-beijing.volces.com/api/coding/v3` |
| endpoint | `POST {base_url}/embeddings` |
| model | `doubao-embedding-vision-251215` |
| auth | Bearer `ark-...` (从 `LLM API.txt` GB18030 runtime 读入 `os.environ['ARK_API_KEY']`,**永不入 prompt/JSON/盘**) |
| proxy | **未设置** (火山国内,cn 出口直连) |
| SDK 模式 | OpenAI 兼容(`urllib.request` 手工) |
| Cell 数 | 1 sanity + 3 cells = 4 API calls |

**对比基线**: 同 key + 同 model + 错 endpoint `/v3` → 之前 8 models 全 404 (bg_6853ef53 Task B)。

---

## §2 1-cell Sanity 结果

| 字段 | 值 |
|---|---|
| input | `"What is 2+2?"` |
| HTTP status | **200 OK** |
| embedding dim | **2048** |
| first 5 | `[-0.0133, -0.0161, -0.0157, 0.0093, -0.0021]` |
| usage | `{prompt_tokens: 26, total_tokens: 26}` |
| latency | **468.0 ms** |
| verdict | ✅ PASS |

**确认**: `doubao-embedding-vision-251215` 在 `/api/coding/v3` 下确实可调,2048 维(非 1024/1536)。

---

## §3 3 Cells 结果(GSM8K×2 + StrategyQA×1)

| Cell | Source | Input 字符 | HTTP | dim | latency | usage | 范数 | passed |
|---|---|---|---|---|---|---|---|---|
| GSM8K_id1 | `…v1_4_gsm8k_details.json` id=1 | ~340 | 200 | 2048 | 459.4 ms | 64 tok | 7.412 | ✅ |
| GSM8K_id2 | 同上 id=2 (Tom's ship) | ~120 | 200 | 2048 | 560.2 ms | 27 tok | 7.070 | ✅ |
| StrategyQA_id1 | `…v1_4_strategyqa_details.json` id=1 (Voldemort) | ~70 | 200 | 2048 | 1278.0 ms | 18 tok | 7.108 | ✅ |

**Total**: 3/3 PASS, **verdict = PASS**。
**Mean latency**: 765.9 ms/cell(单次 call;无并发,顺序执行)。
**token 分布**: prompt_tokens 18–64 区间,与 cell 字符数大致成正比。

### 实测题目文本(脱敏 160 char)
- **GSM8K_id1**: "Melanie is a door-to-door saleswoman. She sold a third of her vacuum cleaners at the green house, 2 more to the red house, and half of what was lef…"
- **GSM8K_id2**: "Tom's ship can travel at 10 miles per hour.  He is sailing from 1 to 4 PM.  He then travels back at a rate of 6 mph.  How long does it take him to get back?"
- **StrategyQA_id1**: "Is Lord Voldemort associated with a staff member of Durmstrang?"

---

## §4 与 `/v3` 错 endpoint 对比

| 维度 | 错 endpoint `/v3` (前次) | 正确 endpoint `/api/coding/v3` (本次) |
|---|---|---|
| HTTP status | 404 Not Found | **200 OK** |
| cells passed | 0/3 (或 0/8 全模型) | **3/3** |
| 原因 | coding-plan key 无 `/v3` 直连权限,需走专属 `/api/coding/v3` | 走 coding-plan 专属 path,授权 OK |
| 关键差别 | 路径前缀 `/api` 缺失 | 完整前缀 `/api/coding/v3` |

**结论**: user 17:15 的纠正是根因。换 endpoint 后,coding-plan key 在该 model 上**完全可用**。

---

## §5 7 铁律自检

| # | 铁律 | 实测 |
|---|---|---|
| 1 | key runtime 读(GB18030 → `os.environ['ARK_API_KEY']`) | ✅ `LLM API.txt` 用 `encoding='gb18030'` 读,12 位前缀 `ark-de0b484e` 命中 user 指定 key |
| 2 | 不设 proxy | ✅ 启动时 `os.environ.pop('HTTP_PROXY'/'HTTPS_PROXY'/...)` 全部清掉,JSON 内 0 个 `proxy` 字面值 |
| 3 | key 永不入 prompt/JSON/盘 | ✅ JSON `auth` 字段只 12 位前缀 + 占位;grep full key pattern `ark-de0b484e-0889-…-fe219` → **0 hit** |
| 4 | 严格 doubao-embedding-vision-251215 | ✅ JSON 内 1 处命中,0 处 `doubao-pro/lite/embedding-text` 错切 |
| 5 | 不动 5 锚 JSON `KT_ABC1_anchors_sha256_12.json` | ✅ 本次任务**只读** `gsm8k_details.json` + `strategyqa_details.json`,**未写**锚/SPEC 文件 |
| 6 | 不动 4 SPEC V0.1 + v19/v21 frozen JSON | ✅ 同上,scope 严格限定在 volcengine embedding 重试 |
| 7 | 结果落盘(不含 key/IP) | ✅ `deposon_volcengine_doubao_embedding_2026_09_10.json` 3301 bytes,grep IP regex → 0 hit |

---

## §6 下一步(建议)

**本次 verdict = PASS**,可推进 V3.X 挂点预筛的 embedding 端到端验证:

1. **P0 - 立即**(今天)
   - 22 受控概念图 caption embedding 验证:把 22 张图的英文 caption 灌进 `doubao-embedding-vision-251215`,看返回 22 个 2048-d 向量 + 邻接结构是否与人工标签一致
   - 输出:`deposon_volcengine_doubao_caption22_2026_09_10.json`

2. **P1 - 短期**(本周)
   - embedding → concept clustering:用 22 个向量做 k-medoids,看 k=4 cluster 是否对得上 P-A/B/C/D 4 候选
   - 若 cluster 稳定 + 与王老师人工选点 1-2 个命中 → 启动 V3.X 1 周判死(参考 user_profile `deposon V3.X = 1 周预筛`)

3. **P2 - 若 P0/P1 PASS**
   - 把 `doubao-embedding-vision-251215` 写入 v3.x `embedding_endpoint` 字段,替代 TeamoRouter(已确认 TeamoRouter 不支持 embedding)
   - 在 KT_ABC1 anchors 里加 1 行 `volcengine_doubao_vision_2048d` 锚(写之前 reviewer 再过一遍)

4. **若 P0 FAIL**
   - 退路 1:换 `doubao-embedding` (非 vision) 试 1024-d 是否 work
   - 退路 2:在 Volcengine 控制台开通 coding-plan 的完整模型列表
   - 退路 3:挂 BGE-M3 (本地 sentence-transformers) 作为备选(但失去云端一致性)

---

## §7 附录

### 落盘文件
- 结果 JSON: `D:\私人资料\deposon-repo\results\deposon_volcengine_doubao_embedding_2026_09_10.json` (3301 bytes)
- 测试脚本(临时,已删): `D:\私人资料\deposon-repo\results\_temp_volc_test.py`

### Key 处置审计
- 来源: `C:\Users\Administrator\Desktop\AI\LLM API.txt` (GB18030)
- runtime env: `os.environ['ARK_API_KEY']` 仅在 Python 进程内
- 出盘: **无** (JSON `auth` 字段 12 位前缀 + 占位)
- print: 仅 `ark-de0b484e…`(12 位前缀,无完整 key 出现)
- proxy: 无

### 调用链
```
1) sanity  "What is 2+2?"                              → 200, 2048d, 468ms
2) GSM8K_id1  Melanie vacuum cleaners (340 chars)      → 200, 2048d, 459ms
3) GSM8K_id2  Tom's ship 10mph 1-4PM (120 chars)       → 200, 2048d, 560ms
4) StrategyQA_id1  Voldemort Durmstrang (70 chars)     → 200, 2048d, 1278ms
                                                              ─────────────
                                                              4/4 PASS
```

---

**报告生成时间**: 2026-09-10 17:18 (CST)
**worker**: mvs_6385fe54bd6142459b2371f72b9bb75a
**handoff to parent**: mvs_bbeb804b1a6a41109be740636eed1709
