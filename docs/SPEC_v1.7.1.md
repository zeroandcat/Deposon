# SPEC v1.7.1 — 同协议融合修复与零 API 阴性对照（取代 v1.7 row-wise 草案）

动机：v1.6 paired 统计显示方向为正但不显著；独立审校指出 λ 四档全等同可疑。诊断为量纲饱和：field 候选内差距 ~1e-2–1e-1，稀疏先验 confidence 0.8–1.0，λ=0.25 即饱和，故四档等价。本版**不改变 v1.6 留一协议**（同图/同种子 70000+ei/同 N_NEG=10/top-3），只做评分时刻修复与阴性对照；零 API（复用 llm_prior_cache.json，缺失则 LLM 臂 pending）。

新增臂（在 v1.6 六臂基础上追加，全部报告）：
- hybrid_norm@λ：仅在当次候选 mask 内对 field_scores 与 prior_scores 分别 min-max 归一后融合 (1-λ)·fg_norm+λ·prior_norm；不用真值，λ∈{0.25,0.5,1,2} 全报。
- 阴性对照（零 API）：(N1) prior_conf_shuffle：9 条先验边端点不变、置信度打乱（seed 固定）；(N2) prior_random_edges×5：在同标签节点集上随机生成 9 条有向边并复用同一组置信度（5 个固定种子，逐种子报告）。用于检验增益是否来自语义先验而非稀疏先验/位置偏置。

预登记探索判据（不回溯改写 v1.6）：E5a 说明 λ 不变性的机制并给出 hybrid_norm 逐 λ 结果；E5b 若 hybrid_norm@0.5 named_path ≤ field_guided 或 real_prior 不优于两类阴性对照均值，则记录为“融合修复未产生可判别语义增益”。统计同 v1.6 paired（边级 McNemar/bootstrap；不多重比较校正，因不依赖 p<0.05 主张）。

安全：不读取/写入 key；不调用网络；严禁 mock；所有 null 先验标记为 synthetic_null，不得冒充 LLM 输出。
