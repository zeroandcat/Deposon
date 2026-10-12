# Findings GT-3 — 跨评估者/跨厂商先验稳健性（2026-08-30）

> SPEC：docs/SPEC_GT3.md（含修正案 A1/A2/A3，判据先于数据冻结）。
> 数据：results/deposon_v20_gt3.json；缓存 results/gt3_prior_cache/（18 个，attempts 全落盘）。

## 判定（机械求值，非手写）

**H_GT3 支持；斩杀线 H_GT3_dead 未触发。**

- 四个新评估者全部通过 ≥4/6 判据，**合计 0 域** 先验 ≤ 场：
  E1 moonshot-v1-8k 5/5；E2 kimi-k2-thinking 4/4；
  **E3 doubao-seed-evolving（ByteDance）4/4**；
  **E4 deepseek-v4-pro（DeepSeek）6/6**。
- 五评估者全 ok 的 3 域上 Kendall **W=1.0**（逐域排序完全一致）。
- 跨厂商关键证据：DeepSeek 与 ByteDance 模型在 Kimi 生成的图上
  复现同等量级优势（如 biology 全评估者 1.000 vs 场 0.136；
  physics 0.45–0.68 vs 0.097）——**「先验优势是同厂商同源污染 artifact」
  假说被实质性削弱**（未完全排除：三族均为中文优化大模型，见局限）。

## 逐域矩阵（named Hits@3；FAIL=超时/解析失败，如实披露）

| 域 | E0 kimi-coding | E1 moonshot-v1 | E2 k2-thinking | E3 doubao | E4 deepseek | field_mean |
|---|---|---|---|---|---|---|
| physics | 0.48 | 0.45 | 0.48 | **0.68** | 0.52 | 0.10 |
| biology | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.14 |
| algorithm | 0.69 | 0.76 | FAIL | FAIL | 0.52 | 0.10 |
| historical | 0.78 | 0.74 | 0.70 | FAIL | 0.70 | 0.04 |
| geography | 0.75 | 0.75 | 0.75 | 0.81 | 0.81 | 0.19 |
| project_mgmt | 0.39 | FAIL | FAIL | 0.19 | 0.44 | 0.06 |

## 预算与事故（如实）

- Kimi 侧（A1）：探测 3 + run1 17 + run2 8 = 28 次，超预登记 1 次（已披露）。
- Ark 侧：doubao 探测 2 + 12（两轮，含 480s 超时重试）= 14 次，恰达预算上限；
  deepseek 探测 1 + 8 = 9 次 ≤13。
- doubao-seed-evolving 对长结构化 prompt 响应极慢（2 域 480s 仍超时失败）；
  deepseek max_tokens=8000 曾被 reasoning 耗尽（空内容），16000 恢复——
  A3-errata 已记录在脚本注释。
- 评估器曾现 W 计算 bug（排名方向颠倒致 W=0.0 假阴性），已修复并复核。

## 局限

1. 三模型族均为中文优化的头部大模型，训练语料可能共享公开中文知识——
   「完全独立」不可声称；最彻底检验需非中文模型族或人工标注图。
2. 5 个缓存失败（超时/解析）未纳入均值，披露于 failures；
   project_management 域 E1/E2 缺失使该域跨评估者证据较弱（E3=0.19 偏低）。
3. W=1.0 基于 3 个全 ok 域，样本小；以逐域 0 败绩为主证据。
