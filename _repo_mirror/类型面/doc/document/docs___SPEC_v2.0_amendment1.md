# SPEC v2.0 修正案 1（2026-08-29，深探整改登记）

> 依据：独立深探 R1（reviews/deep_probe_R1.md）与 R2（reviews/deep_probe_R2.md）
> 的实锤发现。本修正案只追加登记，不回溯改写 SPEC v2.0 原文与既往结果文件。
> 详细更正叙事见 docs/Findings_v2.0_corrections.md。

## A1. 斩杀线 H_A_dead 触发的正式确认（最高优先）

- 事实：results/deposon_v20_corpus_eval.json（20 图版与 22 图版）的冻结字段
  `kill_lines.H_A_dead.triggered = true`（20 图：3 反转；22 图：4 反转——
  L_historical、L_physics、L_project_management、S2_n45）。
- Findings_v2.0.md 手写「未触发（反转仅 1 张 <3）」系 S 族 16 图口径的旧态，
  族 L 并入后已失实；R2 另发现「16/20」与 15+/3−/2= 的文数不符。
- 处置：按预登记规则「H-A1 不显著 **或** ≥3 图反转 → H-A 判死」，
  **H-A（field_mean vs random 的头条主张）正式判死**，转「适用边界」叙事：
  存活主张收缩为 ① field_mean > degree 跨独立性口径稳健（R1 代表 10 张
  p=0.0078）；② 场在高 hub 结构图（S6 族）的局部优势；③ 分工叙事
  （反转图恰全部位于语义/低枢纽图——斩杀线触发本身即边界证据）。
- 22 图补充：H-A1 符号检验 p=0.0118（Holm 仍过）与斩杀线触发并存——
  预登记规则为析取式，两者不矛盾，以斩杀线为准。

## A2.「先验 92.5% = CoT 92.5%」声称撤回

- R1 实锤：题库 4 选项中 2 个攻击者陷阱非图节点，先验/场对其机械 −inf，
  先验有效任务在 39/40 题退化为 2 选 1（机会 50%）；开放候选放回实测
  先验 top-1 = 67.5%（与 CoT 92.5% 差 25 点）；由开放秩推算 2 选 1 期望
  94.4% ≈ 观测 92.5%，完全解释。「更难通道达到直接问答水平」的前提为假。
- 处置：该声称**撤回**。保留的可比口径：CoT 92.5%（4 选 1 带选项文本）
  vs 先验 top-1 67.5% / top-3 82.5%（开放候选）；field_mean 题库 52.5%
  标注为 2 选 1 机会水平，不作信息性解读。

## A3. BOSS 事件统计门槛（v2.0.1 起生效）

- R1 实锤：tfidf 在族 S 合成图上余弦近全零（S4 金边 >0 仅 0/58），排序由
  1e-9 tiebreak 抽签主导（伪装随机臂）；200 次置换证实 S5 的「胜场」
  在 37.5% 抽签中出现（margin 恰 1 条边）。生成器无 bug（标签与结构不同流）。
- 处置：boss 事件须过门槛 **margin ≥ 3 条金边**（gate_pass 字段落盘，
  被拦事件在 boss_events_below_gate 如实保留）。门槛后 BOSS 6 事件：
  L_hist-CN、L_phys-tfidf、L_PM-(PA/n2v/tfidf)、S4-tfidf；被拦 4 事件
  （L_bio、L_hist-tfidf、L_PM-ppr、S5）降级为抽签候选。中文短标签场景
  3-gram 词法臂降格为参考臂。

## A4. 光子 P2 更正（单位 bug + 截断）

- R1 实锤：nep_floor 单位错（1 pW=1e-9 mW，代码误 ×1e-3，下限严 10⁶ 倍）；
  max_hops=10 截断 + 索引贪心掩盖真实链长（S1 实 19 跳被截 9 跳）；
  文档「8 图 >40 dB」失实（落盘 23–26 dB）。
- 处置：真最长路径 DP + 单位修正后，**可探测 18/22，阈值 ≈27 跳**；
  不可探测 = L_algorithm_process(29)、S1_n35(34)、S1_n45(44)、S1_n60(59)。
  「跨层互证」表述降级为「方向一致」（L_historical 20 跳改判可制造）。

## A5. API 预算追认与账本规则

- R2 审计：34 个缓存零 attempt 字段；v18 结果 JSON 幂等重跑自我擦除计数；
  未登记消耗 ~29 次（CoT 小题库 9 + BigQuiz ~20 含 PM 16k 重试），
  SPEC v2.0 无对应条款。
- 追认登记：CoT 9 次（8 prompt）、BigQuiz 两阶段 ~20 次（16 prompt，
  含 PM 先验 max_tokens 8000→16000 的 2 次重试——单 prompt 实际尝试 6 次，
  突破 MAX_ATTEMPTS=2 框架，登记为预算例外，理由：reasoning 溢出陷阱）。
- 新规：此后所有 API 驱动必须把 http_attempts 写入结果 JSON（含重试次数），
  幂等重跑时保留累计计数（禁止自我擦除）；预算例外须当场登记。

## A6. 工程防复发（R2/E1–E4）

- run_v17_fusion_fix.py 等被 import 但未推送的文件全部补推（冷启动断点）。
- ingest_domain 摄入即 build_index；load_corpus 加孤儿哨兵（未入册图 JSON
  显式报错）。
- verifier 地雷排除：v12 族 L 计数、v18 图数改为下界断言；v17/v20 受实验
  更正影响的锚点以 erratum 处理（不覆写冻结版本，v21 承接新锚点）。
- 语料快照承诺修正：MANIFEST 再生命令对语料版本（20→22 图）不具确定性
  复现力，后续以 index.json 的 sha256 快照为准钉版本。
