# Verifier Index (append-only)

## v1 — 2026-08-23 (UTC ~02:30)
- 测量内容：v1.4.0 终验清单——安全闸（无 key 泄漏）、关键文件存在性、GSM8K 终版数字（0.97/0.85/p=4.883e-4/物理审计）、论文终版标记（无占位符、Table 11、G2 重写版数字、小写记号清除）、条件等效声明存在性（软警告）、bib 37 条。
- 运行方式：仓库根目录 `python3 verifier/v1/check.py`，exit 0=PASS。
- 与此前版本差异：首个版本。
- 运行记录：见 verifier/runs/。
- v2/ (2026-08-23): v1.5 扩散原型验收——交付文件存在性、pytest 全绿、结果 JSON 完整性(spec_version/energy_mode/honesty/49 逐边明细)、死锁修复证据(B field_active≥48 且 maxpath 对照=0)、A r=0.2 正增益断言、key 泄漏扫描。与 v1 差异：从论文验收转为代码+实验验收。注：v2 存在一个键名 bug(假 FAIL)，保留不改。
- v3/ (2026-08-23): v2 的键名修正版(gold_path_top3_hit.mean)，其余判据与 v2 完全相同；首个全绿验收。
- v4/ (2026-08-23): v3 的远端兼容版——结果文件判据改为“全量 JSON(本地) 或 摘要 JSON(GitHub 克隆) 二选一”，大文件缺失降级为 WARN 而非 FAIL，指标断言兼容摘要扁平结构；其余判据不变。变更原因：>500KB 结果文件因 MCP 传输上限不镜像远端。
