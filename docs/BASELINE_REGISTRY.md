# Baseline Registry — 横向对比算法注册表（防「后期大 BOSS」）

> 2026-08-28 建立。动机（用户指令）：v1.X 末期才冒出两个大 BOSS——直接 CoT
> （GSM8K 97% vs unified 85%）与 6 关键词规则过滤器（0.87 ≥ 0.85）——说明基线
> 枚举不能靠想起一个补一个。本注册表按算法族**穷举**，每个条目三态：
> ✅ 已实现（脚本+结果）/ 🔶 代理实现（零 API 近似，如实标注）/ ⬜ 未实现（注明理由与排期）。
> 新增对比实验必须先查本表，漏族须说明为何不补。

## A. 结构启发式（零 API）

| 算法 | 状态 | 位置/结果 | 备注 |
|---|---|---|---|
| random | ✅ | run_v20_corpus_eval | 锚点 |
| degree（入度） | ✅ | 同上 | |
| Adamic-Adar | ✅ | 同上 | |
| Jaccard | ✅ | 同上 | |
| Common Neighbors | ✅ 本轮 | run_v20_baselines.py | |
| Preferential Attachment | ✅ 本轮 | 同上 | |
| Personalized PageRank | ✅ 本轮 | 同上 | PPR(u,·)，α=0.85 |
| Katz（β=0.005） | ✅ 本轮 | 同上 | 截断 K=3 |
| Node2Vec 嵌入 | 🔶 本轮 | 同上 | 纯 numpy 近似（随机游走+skip-gram 简版，d=16），如实标注非完整实现 |
| KGE（TransE/ComplEx/RotatE） | ⬜ v2.1 | — | 需多图训练；20 图规模可训，排期 v2.1 |

## B. 语义非 LLM（零 API）

| 算法 | 状态 | 位置/结果 | 备注 |
|---|---|---|---|
| 规则关键词过滤 | ✅ | E9.5 / run_v20_corpus_eval | v1.X 大 BOSS #2，已收编 |
| 字符 n-gram TF-IDF 余弦 | ✅ 本轮 | run_v20_baselines.py | embedding 余弦的零 API 代理，如实标注 |
| 标签 embedding 余弦 | ⬜ 待 embedding 端点 | — | kimi-for-coding 无公开 embedding 端点；有端点即补 |
| BM25/词面重叠 | ✅ 本轮 | run_v20_baselines.py（与 n-gram 同族并列） | |

## C. LLM 直接类（API，大 BOSS 高发区）

| 算法 | 状态 | 位置/结果 | 备注 |
|---|---|---|---|
| labels-only 先验（llm_prior） | ✅ | familyL_prior_cache | 零泄漏口径 |
| **直接 CoT 作答** | ✅ 本轮 | run_v20_cot_fetch/eval | **v1.X 大 BOSS #1，正面收编**：题库逐题直接问答 |
| LLM 全候选重排 | 🔶 视同 | — | 与 labels-only 先验同信息通道，不再单列（注明） |
| Self-Consistency 多票 | ⬜ v2.1 | — | 预算 ×5，v2.1 排期 |
| LLM-as-judge 成对比较 | ⬜ 暂不 | — | 与排序任务度量不同构，引用时说明 |

## D. 生成/扩散类（本方法族）

| 算法 | 状态 | 备注 |
|---|---|---|
| field_guided（dirichlet） | ✅ | v1.5 起 |
| field_mean（mean-field） | ✅ | v1.9 E9.1 起 |
| hybrid_norm（λ∈[0,1]） | ✅ | 融合已证稀释 |
| 图扩散生成（EDGE 式） | ⬜ 参考 | R2 文献，非同任务，仅作 related work |

## E. 人类平凡基线

| 算法 | 状态 | 备注 |
|---|---|---|
| 机会水平（1/候选数） | ✅ | 题库 25%、LOO 分层报 |
| 首选项/位置偏置 | ✅ 本轮 | 题库臂 |

## 收编纪律

1. 任何新版本启动时先过本表：每个族至少一个代表臂在场，缺失写理由。
2. 「大 BOSS 测试」：若某基线在任一图/题库上击败主臂，必须在 Findings 头条披露，
   不得埋没（CoT 与规则过滤器的教训）。
3. 代理实现（🔶）必须在结果 JSON honesty 标注与完整实现的差距。
