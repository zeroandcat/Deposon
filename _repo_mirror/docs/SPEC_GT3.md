# SPEC GT-3 — 跨评估者先验稳健性（预登记，2026-08-30 冻结）

> 与死同行：判据先于数据。本 SPEC 在任何 GT-3 评估数字产生之前冻结。
> 继承：LESSONS #21（候选集可比性）、#26（attempts 落盘）、#19（判定禁手写）。

## 0. 背景与降级声明

原 GT-3（CLOSURE §3.3）设计为**跨模型族**信号实验（第二厂商 API），
检验「先验优势是否同源污染 artifact」（族 L 图由 kimi-for-coding 生成，
先验臂同模型 ⇒ 同源）。当前可用资源仅为 kimi 端点，但探测确认该端点
授权多个**不同代际/不同推理模式**的模型。故本实验降级为：

- **GT-3a（本 SPEC）**：族内跨评估者稳健性——评估者 ≠ 生成者
  （生成者 kimi-for-coding 固定；评估者为不同模型）。
  能回答：「先验优势是否单一评估者 artifact」；
  **不能**完全排除同厂商同源污染（如实声明，GT-3b 待第二厂商资源）。

## 1. 假设与判定

- **H-GT3**：labels-only 先验在族 L 上的 named Hits@3 优势跨评估者稳健。
- **支持判据（需同时满足）**：
  1. 每个新评估者在 ≥4/6 域上 named Hits@3 > field_mean（同图同协议）；
  2. 三评估者（含既有 kimi-for-coding）的逐域 named Hits@3 肯德尔和谐系数
     W ≥ 0.5（排序一致性）。
- **斩杀线 H_GT3_dead**：任一新评估者在 ≥3/6 域上 named Hits@3 ≤ field_mean
  ⇒ 「先验优势为单评估者 artifact」成立，先验主张全面降级。
- **边界如实披露**：kimi-k2-thinking 为推理模型，其输出解析失败域记为
  parse_failure（不计入 Hits 均值，单独披露，不静默剔除——LESSONS #25）。

## 2. 协议

- Prompt：`llm_prior.build_prior_prompt(labels)`（与 v1.6/v2.0 既有先验臂
  **逐字节相同**的构造器；prompt_sha256 必须等于既有 familyL_prior_cache
  对应域的 sha，否则该域标记 prompt_mismatch 并排除）。
- 评估者：E0=kimi-for-coding（既有缓存，0 次新调用）、
  E1=moonshot-v1-8k、E2=kimi-k2-thinking。
- 图：族 L 全 6 域。协议：全候选留一 named Hits@3
  （`run_v20_crossval_eval.eval_prior_arm`，场基线同 JSON 复用）。
- 缓存：`results/gt3_prior_cache/{model}__{domain}.json`，
  含 prompt_sha256 / model / response_text / attempts。
- 预算登记：探测 3 次（已发生，2026-08-30，3 模型×1 次 16-token 探活）
  + 6 域 × 2 评估者 × MAX_ATTEMPTS=2 ≤ 24 次 ⇒ **总计 ≤27 次 HTTP**。
  attempts 逐缓存落盘（LESSONS #26）。

## 3. 输出

`results/deposon_v20_gt3.json`：逐域×评估者 named/filler Hits@3、
field_mean 基线、W 系数、判定（机械求值）、honesty（降级声明、
parse_failure 清单、预算实耗）。

## 修正案 A1（2026-08-30，数据后补登，如实披露）

- 首轮获取 3 域超时失败（algorithm_process×2、project_management×2），
  按总预算额度内重试一轮（run2 8 次尝试）：moonshot-v1-8k/algorithm_process
  恢复；其余 3 个缓存仍超时失败，按 SPEC §1 记 fetch_failed 单独披露、不静默剔除。
- **预算实耗 28 次**（探测 3 + run1 17 + run2 8），**超出预登记 27 次 1 次**。
  超支原因：重试轮的 attempts 落盘机制如实计数（LESSONS #26 执行成本）。
  处理：如实披露，不追溯修改预算；后续 GT-3b 预算应按 1.5× 超时系数估算。

## 修正案 A2（2026-08-30，GT-3b 跨厂商扩展，数据前冻结）

用户提供火山引擎 Ark/Doubao API（第二厂商）。GT-3b 正式启动：
- **评估者 E3 = doubao-seed-evolving**（字节跳动，与 Kimi 不同厂商、不同模型族）——
  本实验升级为**真·跨厂商验证**，直接检验「先验优势是否同厂商同源污染 artifact」。
- 协议与 GT-3a 逐位相同：同一 build_prior_prompt、prompt_sha256 校验、
  同一 eval_prior_arm 协议；缓存 `results/gt3_prior_cache/doubao-seed-evolving__{domain}.json`。
- 判定（机械求值）：
  1. E3 在 ≥4/6 域 named Hits@3 > field_mean ⇒ 跨厂商稳健；
  2. 四评估者 Kendall W ≥ 0.5（仅四者全 ok 的域）；
  3. 斩杀线：E3 在 ≥3/6 域 ≤ field_mean ⇒ 先验优势判为同源 artifact，全面降级。
- 预算：探测 2 次（已发生）+ 6 域 × MAX_ATTEMPTS=2 ≤ 12 ⇒ **≤14 次 HTTP**；
  attempts 落盘。超时风险高（实测需 >60s），TIMEOUT=240s。
- key 纪律：Ark key 与 Kimi key 同规——仅主代理单次命令内联环境变量，
  不落任何文件/日志/prompt；用户任务后删除。

## 修正案 A3（2026-08-30，第三模型族扩展，数据前冻结）

用户在 Ark 端点追加提供 deepseek-v4-pro-260425（DeepSeek 权重——
与 Moonshot、ByteDance 均为不同模型族）。新增评估者 **E4=deepseek-v4-pro-260425**，
GT-3b 升级为**三模型族交叉验证**（生成者 Moonshot kimi-for-coding；
评估者 Moonshot×2 / ByteDance×1 / DeepSeek×1）。
- 协议与判定同 A2（E4 适用同一 ≥4/6 判据与 ≥3/6 斩杀线；W 在五评估者
  全 ok 的域上计算）。
- 预算：探测 1 次（已发生）+ 6 域 × MAX_ATTEMPTS=2 ≤ 12 ⇒ **≤13 次 HTTP**。
- 注：E4 为推理模型，max_tokens=8000（探测显示小额度会被 reasoning 耗尽）。
