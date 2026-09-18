# D05 数据救援注记 (Trae code, 2026-09-18 走读改进 #1)

## 事实链
- D05 bg 任务 (bg_21191cee) 运行 main runner 后被删除, 其工作区含以下两份关键产物, 被移入
  `_d05_bg_21191cee_trash_2026_09_18/results/` (trash 目录, 有被清理灭失风险):
  1. `_d05_main_run_results_20260918_100853.json` (sha12=0a933d7c8d7a) — deepseek_v4 主跑原始数据,
     D05 唯一 sanity PASS + 30 cells 完整跑成的 backbone (24/30, accuracy 0.8, Spearman vs baseline 0.7917)
  2. `_d05_main_run_results_qwen3_failed_20260918_100853.json` (sha12=427b18da8114) — qwen3_32b HTTP 400
     FAIL 证据 ("不擅自换 ID" 纪律记录)
- `results/_d05_backbone_robustness_beta_20260918_100853.json` 的 `_meta` 字段引用上述两 sha12,
  trash 清空即 D05 溯源链断裂。

## 处置
- 本注记随同将两文件**复制**(非移动)回 `results/` 根: 副本哈希与 trash 原件及 β _meta 声称值逐字节一致。
- trash 目录原件保持不动 (bg 系统状态不干预)。
- 下游引用 (combined report §1.1 source 列、verify_sha 脚本) 以 results 根副本为准。

— Trae code (审校/走读), 2026-09-18
