# SPEC v1.8 — API 补实验：同模型标签打乱阴性对照 / 训练污染探针 / 方向稳健性（预登记）

动机：v1.6 LLM 语义先验臂与 v1.7.1 同协议归一融合修复（hybrid_norm@2 named=0.471）之后，评审提出三点担忧：
(a) 先验的「语义性」缺少**同模型但标签打乱**的阴性对照——v1.7.1 的 null 是程序生成的 synthetic null（随机边/置信度打乱），不是 LLM 输出，无法排除「任何形式化 prompt 都会让该模型吐出命中边」的 artifact 假说；
(b) 先验命中 named 边可能来自**训练数据污染**（该脑图或来源文档曾被模型见过）而非语义推断；
(c) named=0.471 对 **prompt 措辞/方向定义**的稳健性未知。

本版不改变 v1.6/v1.7.1 的留一协议与已有结果；只做 3 个各一次调用的 API 补实验（E1/E2/E3）与同协议复评分。评分口径与 v1.7.1 完全一致：同图/同种子 70000+ei/同 N_NEG=10/同行负采样池/top-3；hybrid_norm=min-max 归一融合 + 1e-6 确定性 tiebreak，hybrid_raw=W_done+λ·prior；报告臂为 real 先验（v1.6 缓存，只读）、E1 打乱先验、E3 方向先验各自的 prior-only 与 norm/raw 融合（λ∈{0.5, 2.0}，预登记全报），指标 overall/named/filler top-3 命中率，分母 49/17/32 与 v1.7.1 一致。real 先验臂数字应逐位复现 v1.7.1（tests/test_v18.py 含回归断言）。

## E1 标签打乱阴性对照（1 次 API 调用）

- **假说**：若先验携带的是标签语义而非「该模型对任何标签列表都倾向输出命中 named 边的形式化 pattern」，则用同一模型、同一 prompt 模板、但标签顺序确定性打乱后的先验，named 命中应跌回 synthetic null 水平。
- **方法**：rng=np.random.default_rng(188001)；perm=rng.permutation(45)；shuffled_labels[i]=labels[perm[i]]。用 v1.6 同一 build_prior_prompt 作用于打乱标签调用 API；返回边 (i,j) 为打乱索引空间，映射回原节点 (perm[i], perm[j])，confidence 保留。缓存落盘 results/llm_prior_cache_v18_labelshuffle.json（spec_version=v1.8-E1、model、endpoint、prompt_sha256、perm_seed=188001、perm 完整列表——可审计、非秘密、打乱空间原始边与映射后边均落盘）。
- **预期**：E1 先验 named top-3 接近 v1.7.1 synthetic null 水平（hybrid_norm_rand×5 均值 0.176 附近），明显低于 real 先验。
- **判定口径（预登记）**：主判据用 hybrid_norm@0.5 臂 named top-3——若 |E1 − 0.176| ≤ 0.06 且 real(0.294) − E1 ≥ 0.06，则支持「先验携带语义而非形式 artifacts」；prior-only 臂（null 0.118 / real 0.235）作辅助口径。若 E1 也高，则语义性主张被削弱，如实报告，不作修饰。

## E2 训练污染探针（1 次 API 调用）

- **假说**：若该节点集合整体来自模型训练数据中的具体脑图/文档，模型可能自陈识别并回忆起具体关联；据此评估污染警示强度。
- **方法**：零泄漏 prompt（只给 45 个标签列表），询问该节点集合是否可能来自训练数据中的具体脑图/文档，输出严格 JSON 对象 {"recognized": bool, "confidence": 0-1, "basis": "...", "recalled_edges": [{"parent":int,"child":int},...]}。落盘 results/llm_prior_cache_v18_contamination.json（spec_version=v1.8-E2、prompt_sha256、完整响应 JSON）。
- **定量分析**：recalled_edges 与金边（全 49 及 named 17）的重叠数 vs 随机机会期望——从 N(N−1)=1980 个有向对中无放回抽同等 k 条，期望重叠 = k·|G|/1980。
- **判定口径（预登记）**：recognized=true 且金边重叠 ≥ 3× 机会期望 → 污染警示增强；否则作为弱反证。**E2 为自陈式探针，recognized/回忆边均为模型自述，结论只能作定性参考**，不能作为污染存在或不存在的直接证据。

## E3 方向显式先验稳健性（1 次 API 调用）

- **假说**：named=0.471 若对 prompt 措辞稳健，则在显式给出方向定义的 prompt 变体下，融合 named 应维持同方向水平。
- **方法**：在 build_prior_prompt 基础上增加方向定义——「parent 为语义上位/原因/整体，child 为下位/结果/部分」，并要求每条边附 1 句 justification 字段；解析时忽略 justification 只取 (parent, child, confidence)。落盘 results/llm_prior_cache_v18_direction.json（spec_version=v1.8-E3、prompt_sha256、含 justification 的完整边列表）。与 v1.6 先验（9 边）比较：无向 Jaccard、共有边的方向一致率；并用 E3 先验跑同协议融合（λ∈{0.5,2.0}）。
- **判定口径（预登记）**：named 结果对 prompt 措辞稳健 ⇔ E3 hybrid_norm@2 named ≥ 0.471 − 0.12（容差 ±0.12）。共有边方向一致率 < 0.5 则如实报告「方向定义敏感」。

## API 预算

3 个不同 prompt（E1/E2/E3 各一），每个 MAX_ATTEMPTS=2（与 llm_prior 一致，首次失败仅重试 1 次），合计 HTTP 尝试 ≤ 6 次；模型 kimi-for-coding，endpoint 同 llm_prior.ENDPOINT（https://api.kimi.com/coding/v1/chat/completions）。缓存已存在且 prompt_sha256 匹配时默认复用缓存、0 次调用（幂等重跑）；--force 强制重调。结果 JSON 记录实际 HTTP 尝试总数。

## 零泄漏红线

所有 prompt 只含节点标签列表，禁止任何边/图结构信息（无索引对 (u,v)、无 u→v/u->v 形式、无边列表）；E1 的打乱只对标签顺序操作，不引入任何结构信息。tests/test_v18.py 对三个 prompt 做零泄漏断言（含逐金边共现检查）。

## 安全红线

key 仅从环境变量 KIMI_API_KEY 读取（脚本中唯一一处）；任何文件/日志/异常不得含 key——异常与 HTTP 回显一律经 llm_prior._sanitize 兜底剔除；严禁 mock 冒充真实调用（无 key 时实验如实记 error/pending，非 LLM 的复评分照跑）。--dry-run 不读 key、不发请求，可在无 key 环境运行。

## 诚实规则

E2 结论一律标注「自陈式探针，仅供定性参考」；所有结果（含 E1 反例、E3 敏感、E2 警示或弱反证）如实报告，不回溯改写 v1.6/v1.7.1 的任何表述；判定容差（0.06/0.06/0.12/3×）为预登记机械规则，不替代人工解读。


---

# 修正案 v1.8.1（2026-08-23，实跑后预登记增补）

本修正案在 E1–E3 实跑完成、E4 实跑之前写就并入库，E4 的判定口径属于预登记；E1 的重解读属于对已完成实验的设计缺陷披露，不改写任何已得数字。

## A1. E1 设计缺陷披露与重解读

E1 实跑结果：映射后边集与 real 先验**完全一致**（9/9 边），全部融合指标与 real 臂逐位相同。根因分析：E1 的「标签打乱」只置换了标签的**索引顺序**，标签内容不变；LLM 读取的是标签语义而非索引位置，其在打乱空间输出的边经逆映射 (perm[i], perm[j]) 必然还原同一组语义边。因此原预登记判定口径的假设「打乱索引可摧毁语义」**不成立**——置换对语义推理透明，E1 按原口径「未达 null」**不构成对语义性主张的反证**，该口径作废。

E1 的实际信息量重定位为**置换不变性检验**：映射后边集与 real 完全一致 ⇔ 先验是标签语义内容的函数，而非索引位置/呈现顺序的函数。该检验**通过**（边集 9/9 一致；共有边置信度 Pearson 相关落盘于结果 JSON）。这排除了「先验命中来自索引排序 artifact」的假说，但不能排除「任何形式化 prompt 都会让模型吐出命中边」的假说——后者需要真正摧毁语义内容的对照，即 E4。

## A2. E4 语义摧毁阴性对照（增补，1 次 API 调用，预登记）

- **假说**：若先验信号来自标签语义内容，则把 45 个标签全部替换为无语义占位符（item_00…item_44，与原节点索引一一对应、无置换）后，同模型同 prompt 模板应无法产出携带 named 信号的先验；若无语义标签下先验仍能命中 named 边，则信号只能来自索引偏置等形式 artifact，语义性主张被削弱。
- **方法**：build_prior_prompt 作用于 contentless_tokens(45)；解析规则同 v1.6，但**空数组为合法弃权**（模型无可输出本身就是结果）。缓存 results/llm_prior_cache_v18_contentless.json（spec_version=v1.8-E4、prompt_sha256、status=ok/abstained）。
- **判定口径（预登记）**：(i) 弃权（0 边）→ 最强形式的支持：无语义内容时模型无法产出任何先验；(ii) 非空 → 主判据 hybrid_norm@0.5 臂 named top-3：|E4 − 0.176| ≤ 0.06 且 real(0.294) − E4 ≥ 0.06 → 支持语义性主张；否则主张被削弱，如实报告，不作修饰。

## A3. E3 首轮实跑的脚本 bug 与恢复披露

E3 首轮实跑消耗 2 次 HTTP 尝试，API 响应本身正常，但脚本存在解包 bug（parse_direction_response 返回的 (prior, full) 二元组被 _post_prompt 二次包装），导致后处理崩溃、原始响应文本被当作 prior 落盘。修复后（含回归测试 test_e3_run_unpacks_parser_tuple_correctly），正式缓存由**首轮真实响应离线解析恢复**（13 边，含 justification），未产生额外 API 调用；畸形原始记录归档于 results/llm_prior_cache_v18_direction_run1_malformed_archive.json 供审计。E3 实际 HTTP 总尝试 2 次，未超原预算。

## A4. 预算更新

prompt 总数 4 个（E1/E2/E3/E4 各一），每个 MAX_ATTEMPTS=2，合计 HTTP 尝试 ≤ 8 次；实际发生：E1=1、E2=1、E3=2（见 A3）、E4 ≤ 2（一次调用内返回弃权结果，尝试数未单独持久化），总计 ≤ 6，未超预算。E4 结果：模型对无语义占位标签弃权（0 边）→ 按 A2 口径 (i) 为最强形式的支持。缓存幂等规则不变。
