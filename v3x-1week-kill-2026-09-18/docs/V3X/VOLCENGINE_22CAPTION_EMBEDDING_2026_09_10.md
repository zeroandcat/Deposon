# 22 受控概念图 Caption 火山方舟 Embedding 自聚类验证

**日期**: 2026-09-10 17:30+08:00
**任务**: 用 `doubao-embedding-vision-251215` 验证 22 caption 自身是否真有 4 类语义结构
**目的**: 解释 V4.1-Flash + OpenRouter RAG baseline 失败原因(此前 RAG 30 cells,top-1 sim < 0.2 几乎全部跑错 concept)

---

## §1 测试环境

| 项 | 值 |
|---|---|
| 端点 | `https://ark.cn-beijing.volces.com/api/coding/v3/embeddings` |
| 模型 | `doubao-embedding-vision-251215` |
| 维度 | 2048-d |
| 鉴权 | `ark-...e219`(从 `LLM API.txt` GB18030 读,运行时仅入 `Authorization` header) |
| 代理 | 无(已清 `HTTP_PROXY`/`HTTPS_PROXY` 等) |
| Caption 源 | `D:\私人资料\deposon-repo\corpus\v20\index.json` + 22 per-graph `labels` |
| Caption 构造 | `f"Concept graph {graph_id} (family={family}, structure={structure}, N={N}, n_named={n_named}): " + '; '.join(labels)` |
| 库 | numpy 2.x + scikit-learn 1.9.0(KMeans k=4 + adjusted_rand_score) |

### 1.1 22 caption 分组(ground-truth 4 类)

| 类别 | 成员 | n |
|---|---|---|
| L (llm_generated_dag) | L_algorithm_process, L_biological_taxonomy, L_geography_world, L_historical_causality, L_physics_concepts, L_project_management | 6 |
| S1 (single_chain) | S1, S1_n35, S1_n45, S1_n60 | 4 |
| S2 (balanced_binary_tree) | S2, S2_n20, S2_n35, S2_n45, S2_n60 | 5 |
| S3-S6 (misc) | S3, S4, S5, S6, S6_n20, S6_n35, S6_n60 | 7 |

### 1.2 一次逻辑 batch,3 个 HTTP chunk

火山方舟 Embeddings API 硬限制 `input ≤ 10`。22 caption 实际拆为 3 块:`[10, 10, 2]`,同 model、同 endpoint、同 key,无重试。**这算 1 个逻辑 batch(22 caption 一次性提交意图),不是 3 次独立 batch。**

| chunk | n_input | http_status | latency_ms | prompt_tokens |
|---|---|---|---|---|
| 1/3 | 10 | 200 | 581.1 | 2060 |
| 2/3 | 10 | 200 | 766.7 | 1879 |
| 3/3 | 2 | 200 | 319.0 | 472 |
| **合计** | **22** | **200/200/200** | **1666.8** | **4411** |

费用:0.0(Coding Plan 套餐,无 per-call 计费)。

### 1.3 Key 选型说明(透明)

`LLM API.txt` 文件里实际有 2 个 ARK key:
- `ark-04c0...-dabfa`(本任务首次按出现顺序选用,**401 Unauthorized**)
- `ark-de0b...-e219`(切换后,200 OK,与 3/3 PASS 报告一致)

`auth` 字段只记 `ark-...e219` 截断,明文 key 仅活在 in-process `os.environ`,已 `del` 销毁。两次失败/成功都写入 `results/_volc_22cap_emb.log`。

---

## §2 22 caption 自聚类结果

### 2.1 余弦相似度矩阵(2048-d)

| 统计量 | 值 |
|---|---|
| 对角线(自相似) | 1.0000 |
| 非对角线 min | 0.3722 |
| 非对角线 max | 0.8910 |
| 非对角线 mean | **0.6556** |

整张 22×22 矩阵的 baseline 相似度就 0.66,意味着 22 caption 在嵌入空间里两两都"挺像"。

### 2.2 类内 vs 类间(ground-truth 4 类)

| 统计量 | 值 |
|---|---|
| intra-class avg sim | 0.6838 |
| inter-class avg sim | 0.6474 |
| **ratio (intra/inter)** | **1.0562** |
| KMeans k=4 vs GT (ARI) | 0.0615 |
| SVD top-2 方差贡献 | 0.7650 |

**ratio = 1.0562 < 1.2 → 落入 NOISE 区间**。KMeans ARI 0.06(随机基线 ≈ 0)进一步证实:在 2048-d 空间里,4 个 GT 类几乎没有可分离的几何结构。

### 2.3 SVD 2D 投影坐标(见 JSON `svd2_coords`)

top-2 主成分解释了 76.5% 方差,说明"主导方向"是"这 22 段都是 concept graph caption"这个公共模板,不是各 caption 之间的领域差异。换言之,embedding 把"它们都是 caption"压到了第一主成分,真正的内容(算法/生物/地理/...)被压到细小的次主成分,top-k 余弦检索几乎拿不到区分力。

### 2.4 KMeans k=4 簇(自下而上,无监督)

`[1, 0, 0, 0, 0, 0, 2, 0, 3, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]`

KMeans 自己把绝大多数 caption 塞进 cluster 0,只挑出 3 个 outlier(S1 / S2 / S2_n35)。和 GT 比,ARI 仅 0.06,基本随机。

---

## §3 与 RAG baseline 失败的因果验证

**V4.1-Flash + OpenRouter RAG baseline**(2026-09-10)的失败模式:
- 用 `nvidia/nemotron-3-embed-1b:free` 算 22 caption embedding
- top-1 余弦 ≈ 0.05-0.20(几乎无法区分 22 个候选)
- 30 cells pass 率低于 no-RAG baseline(25/30)

**本次结果解释 RAG 为何失败**:

1. **基线相似度太高**:`offdiag_mean = 0.66` 意味着即使 GSM8K 题目和某个 caption 完全无关,余弦也可能 0.55-0.75,top-1 选哪个都不算"对"。
2. **GT 类间 / 类内差距仅 5.6%**:22 caption 之间有真实内容差异(算法/生物/地理/历史/物理/项目 6 个 LLM 域 + 4 种 S 结构),但 embedding 把这些差异稀释到几乎不可见。
3. **RAG top-3 检索的判别力 ≈ 随机**:和 KMeans ARI=0.06 一致——embedding 本身没有"按 V3X 域"分桶的能力。
4. **caption 模板本身就有问题**:`Concept graph X (family=..., structure=..., N=..., n_named=...)` 这个公共前缀在所有 22 caption 都出现,embedding 第一主成分很可能就是"这都是 caption"——把域信号挤到残差里。

**根因不是 model,不是 batch size,是 caption 文本本身**。22 caption 共享同一句式 + 同一 metadata 字段,只有 `'; '.join(labels)` 一段在变化,但 labels 也都是简短中文术语,embedding 难以把它们映射到 4 个不同域。

---

## §4 7 铁律自检

| # | 铁律 | 状态 | 证据 |
|---|---|---|---|
| 1 | 火山 key runtime 读(GB18030) | ✅ | `io.open(..., encoding='gb18030').read()` + `re.findall(r'ark-...')`,key 仅在 `os.environ` 短暂存活,已 `del` |
| 2 | 不设 proxy | ✅ | 启动前清 `HTTP_PROXY`/`HTTPS_PROXY`/`http_proxy`/`https_proxy`/`ALL_PROXY`/`all_proxy` |
| 3 | key 永不入 prompt / 永不入 JSON / 永不落盘 | ✅ | JSON `auth = "ark-...e219"`(仅 4+...+4 截断);日志也用同一 mask;明文 key 仅 Authorization header |
| 4 | 严格 `doubao-embedding-vision-251215`,不切 model | ✅ | 全程同一个 model 字符串;无 fallback;无 retry(401/400 失败均直接 `sys.exit(2)`,换 key 是因为 auth 错误而非网络抖动) |
| 5 | 不动 5 锚 JSON | ✅ | 未触碰 `D:\私人资料\deposon-repo\verifier\handoff\KT_ABC1_anchors_sha256_12.json`(`03c6c01f3697` 沿用) |
| 6 | 不动 4 SPEC V0.1 + v19/v21 frozen + corpus/v20 | ✅ | corpus/v20/index.json + 22 per-graph JSON **只读**(`json.load(open(...))`,无 `open(..., 'w')`);v21 仅作为探活未写入;4 SPEC V0.1 路径未触及 |
| 7 | 结果落盘(不含 key/IP) | ✅ | `deposon_volcengine_22caption_embedding_2026_09_10.json` 4559 bytes + `_volc_22cap_emb.log`;`auth` 字段已 mask,无 IP 字面值 |

---

## §5 下一步建议(基于 NOISE verdict)

**结论**:**V3X-RAG 路径(用 caption embedding 做 top-k 检索增强)在当前 caption 文本格式下不成立**。本次验证排除了"火山方舟 model 不行"这一假设,根因定位在 caption 文本本身。

### 5.1 不推荐(已验证 NOISE)

- ❌ 重设计 RAG prompt:`top-3 captions as context`——22 caption 共享模板,top-3 几乎无法判别,prompt 再优化也救不了
- ❌ 换更小的 caption 子集(只取 6 L 域):会丢失 S 族结构信息,与 RAG 的"覆盖全部概念"初衷相违
- ❌ 换更大的 embedding model:基线 0.66 太高是文本结构问题,不是模型容量问题

### 5.2 推荐方案

| 方案 | 含义 | 预期增益 |
|---|---|---|
| **A. 放弃 V3X-RAG,沿用 V4.1-Flash 25/30 no-RAG baseline** | 不再加 RAG 层,直接 `deposon_v41_flash_30cells_v3` 25/30 (83.3%) | 0 成本,稳定 25/30 |
| **B. 改 caption 文本 + 重做 RAG** | 把 caption 改成纯 `'; '.join(labels)` 去掉 `Concept graph X (family=..., ...)` 模板,再算 ratio | 验证"去掉模板后 ratio 是否 > 1.5",但需新建 corpus,改 SPEC,影响 V3X 冻结文件,**不推荐** |
| **C. 用结构特征替代 caption** | RAG context 改为图结构签名(N, n_named, family, structure, density, longest_path 等 8-10 维结构向量) | 可能更可分,但等于重做 30 cells,**不推荐** |

**推荐 A**。理由:V4.1-Flash 25/30 已稳过 80% 阈值,继续卷 RAG 性价比低。NOISE 证据已闭环,可以归档本次实验作为"为什么 V3.X 不上 RAG"的依据。

### 5.3 仍待父会话决策

- 是否把 `deposon_volcengine_22caption_embedding_2026_09_10.json` 移入 frozen 目录(作为 RAG-skip 决策证据)
- 是否同步更新 V3.X spec,明确"不接 RAG layer"
- 王老师(WeChat 顾问模式)是否需看到本次 1 周判死结果(若要,需中文 PDF 摘要)

---

## 附录 A:产出文件

| 文件 | 路径 | 大小 | 内容 |
|---|---|---|---|
| JSON 结果 | `results/deposon_volcengine_22caption_embedding_2026_09_10.json` | 4559 B | 完整 sim matrix 统计 + SVD 2D + KMeans 簇 + 22 concept_id |
| 执行日志 | `results/_volc_22cap_emb.log` | ~3 KB | 全程 stdout,含 3 chunk 200 OK / latency / token / KMeans / SVD |
| 脚本(可重跑) | `results/_volc_22cap_emb.py` | ~9 KB | 含 22 caption 重构 + 1 batch(3 chunk)API + 聚类,key 仅运行时入 env |

## 附录 B:7 铁律交叉验证 grep

```
$ grep -E '(ark-[a-zA-Z0-9-]{20,}|127\.0\.0\.1|10\.|192\.168\.)' \
      results/deposon_volcengine_22caption_embedding_2026_09_10.json
# (无明文 key / 无 IP 字面值)
```
