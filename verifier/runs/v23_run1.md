# v23 运行记录 — run1（2026-08-30）

- 触发：GT-3b 三模型族跨厂商实验完成（H_GT3 支持，W=1.0，0 败绩）
- 结果：FAILS=0；pytest 200 passed
- 资产：SPEC_GT3 修正案 A2/A3、gt3_prior_cache 24 个、deposon_v20_gt3.json、
  Findings_GT3.md、gt3b/gt3c fetch 脚本
- 如实披露：5 缓存失败；doubao 预算恰达上限 12+探测 2；deepseek 8+探测 1；
  kimi 侧超支 1（A1 已披露）；deepseek max_tokens errata
- 插曲：eval 首编辑未落盘（Lesson #12 再现，重做后核验）；pytest 环境重置（Lesson #27 再现）
