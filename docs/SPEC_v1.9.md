# SPEC v1.9 — Deposon 基准修正与对照实验

## Part A — 扩散侧实验 (E9.1 / E9.2 / E9.6) 预登记协议

执行者: Coder-1。零 API：不发起任何 LLM API 调用；LLM 先验一律读 v1.6 缓存
（prompt_sha256 在案）。dirichlet 路径必须与 v1.7.1 逐位一致（回归测试锁定）。

### E9.1 均值场反向退火（mean-field init）

**问题**（R1 探针）：v1.7.1 反向去噪从 Dirichlet(1) 随机起点出发，50 步 ×0.9 收缩后
场梯度无法重排候选（信噪比 ≈0.1），「named 输 random」可能是采样器假象。

**协议**：新增 `init_mode ∈ {dirichlet, prior_mean}`。`prior_mean` 将反向起点从
Dirichlet 采样换为 Dirichlet 分布均值（等价 DDIM η=0 确定性反向），其余逐行不动、
同种子同负池（种子族 70000+ei / 990000+ei·100+s 双协议）。臂：field_mean（新）、
field_guided（dirichlet 复现）、random、degree、llm_prior、hybrid_norm@0.5、
hybrid_norm@2.0。

**判定规则**：
- H1（随机起点是根因）：field_mean named ≥ 0.8 且对 field_guided 的边级精确
  McNemar p < 0.05（LOO 依赖性如实声明）。
- H2（骨架检测器边界）：若 field_mean filler < 0.15，如实标注「场=骨架检测器，
  overall 单信号稳健性不可得」，不回溯改写旧版结论。
- tie artifact（等分时列号稳定排序）逐边标注，占位 named 3 边（0→10/11/12）单列。

### E9.2 全候选排序协议（full-candidate ranking）

**问题**（R1/R2）：同行负采样（N_NEG=10/top-3）是 1-hop 行内预测，随机基线期望
随行变化，负池成分为 Monte Carlo 噪声（sd≈0.066），阈值化丢弃秩信息。

**协议**：取消负采样——每个留一行对全部非邻居候选（N≈44）排序，报告
MRR / Hits@1 / Hits@3，按 named/filler 分层；与 N_NEG=10 协议同臂并列，记录
臂间优劣符号翻转（sign_flips）；难负样本分析（金边秩分布）。

**判定规则**：采样器敏感性按构造归零（无采样）；如实报告协议结论变化，
不以旧协议口径美化新协议结果。raw 口径的场臂 mask 含同行观测出边，
作为预登记代价披露，filtered 档留待多图后补。

### E9.6 速赢固化（quick wins）

**E9.6a 图级符号检验**：基于 v1.7.1 既有 20 张 filler 重挂图 overall，
random−hybrid_norm@2 与 hybrid−field 逐图差双侧符号检验。
**E9.6b 种子敏感性扫描**：field_mean 对每边跑 5 个种子族，报 named/filler/overall
均值±sd，与 v1.7.1 负池噪声 0.066 对照。
**E9.6c λ=2.0 阴性消融**：real vs confshuffle vs random-edge null×5 在 λ=2.0 档
的 named 命中率；机械判据 real > null 均值+0.06 之外，如实披露 confshuffle≈real
对语义性主张的削弱。

### Part A 通用纪律

- 输出 `results/deposon_v19_{meanfield,fullrank,quickwins}.json`，含 spec_version=v1.9、
  config、逐边明细、honesty 段。
- 探针数字（R1 实跑）不得直接入正文；一切以本 SPEC 预登记重跑数字为准。
- 新增测试入 `tests/test_v19.py`；既有 134 测试必须全绿。

## Part B — 基准侧实验 (E9.3 / E9.4 / E9.5) 预登记协议

执行者: Coder-2。输入一律来自既有 LLM 缓存 (results/ 与 /mnt/agents/output/deposon_cache)，
不发起任何 LLM API 调用；每个输入缓存文件记录 sha256 (cache_provenance)。
所有输出写入 `results/deposon_v19_benchmark_fixes.json`。

### E9.3 high_couple 别名修复 (对应 Table 10/12 修正)

**问题**: v1.4 中 `'high_couple': {'mode': 'v1_blocking', 'use_deposon': True}`，
high_couple 臂是 v1_blocking 的纯别名，从未启用高耦合物理路径。

**修复定义**: 新增真实 mode `'high_couple'`：在 `spawn_from_graph` 之后将所有
deposon 的 g_couple 乘以 `HIGH_COUPLE_GAIN = 5.0`（陷阱节点 g_couple=5.0 同步放大，
即物理层耦合路径被真实扰动），g_aether 置 0（保持 blocking 语义，仅放大耦合）。
旧别名行为仅在显式 legacy 开关 `DEPOSON_V14_HIGH_COUPLE_ALIAS=1` 环境变量下复现，
用于历史复现；默认（含 ablation_study 与两个 v1.4 runner）使用真修复。

**协议**: 用既有 GSM8K seed=42 n=100 与 StrategyQA seed=42 n=99（排除 1 个
api_blocked 题）LLM decompose 缓存，离线重跑五臂
(no_deposon / v1_blocking / v2_tunneling / unified / high_couple)。

**判定规则**:
- 通过 (修复有效): high_couple 臂的 per-problem 预测向量与 v1_blocking 臂不完全相同
  （证明不再是别名），且物理守恒审计 t+r+a 偏差 < 1e-6。
- 报告: 修正后五臂准确率，与原 Table 10/12 数字并列；high_couple 相对 v1_blocking
  的 McNemar 精确双侧 p 值。

### E9.4 等权诱饵中性对照

**问题**: v1.4 图构造中正确边权 0.6/0.7/0.8、陷阱边权 0.9/0.85/0.8 且每题强制
Trap_DeadEnd，实验结构偏向 Deposon。

**协议**: 同一缓存 decompose，建图后将所有边（含陷阱边）weight 拉平为常数
`FLAT_WEIGHT = 0.7`（migration_barrier 保持原值，仅中性化权重先验），
重跑 no_deposon 与 unified 两臂（GSM8K n=100，StrategyQA n=99）。

**判定规则**:
- 通过 (中性化成立): unified 与 no_deposon 准确率差 < 10 个百分点，
  且 McNemar 精确双侧 p > 0.05。
- 失败: 仍有显著优势 → 说明 Deposon 增益不完全依赖权重先验，需重新归因。

### E9.5 规则基线 (非 LLM 标签过滤)

**问题**: 缺少平凡（非 LLM）基线，无法证明 LLM 先验的价值增量。

**协议**: 纯确定性规则过滤器 `rule_label_filter`：在 no_deposon 贪心路径生成后，
丢弃任何经过「标签命中关键词表」节点的路径，关键词表 =
{trap, dead, end, impossible, guess, wrong}（大小写不敏感，匹配节点 id/标签），
在剩余路径中取贪心序首条；若全部被过滤则回退未过滤首条（与 no_deposon 相同）。
不使用任何 LLM 输入之外的语义信息，不读节点 type 元数据（仅读标签字符串）。
在相同样本上运行，报告准确率。

**判定规则**:
- 报告规则基线准确率与 unified 臂（LLM 先验）准确率之差 Δ。
- 通过 (LLM 先验有增量): unified - rule_baseline > 0 且 McNemar p < 0.05。
- 若规则基线追平 unified，则 LLM 先验无增量，结论需下调。

### 通用纪律

- 每个实验记录 config（含 seed=42、常数取值）、per-problem 明细、汇总指标。
- cache_provenance: 每个被读取的缓存/输入文件的 sha256 与路径。
- 缓存缺失 → 显式抛错（CacheMissingError），绝不伪造数据、不触发 API。
- no LLM API calls issued; inputs read from cache (sha256 on record)。
