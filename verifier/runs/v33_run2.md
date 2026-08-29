## v33 run2 2026-08-30（工件缺口修复后复核）
cmd: python3 verifier/v33/check.py
checker 变更：B6a/B6b/B6c/B6d 由全文 find 切片改为按 `### 6.x` 节标题正则切片（^#+\s*6\.x\s 起、下一 ^#{1,3} 标题止），消除 run1 全文级 grep 误报风险；run1 记录未删改。
PASS A1 pytest 全绿且 >=274
  [pytest] 274 passed, 1 warning in 33.38s
PASS A2a def row_normalize 全仓仅 1 处且在 deposon_protocol.py
PASS A2b 退火循环体全仓仅 1 份
PASS A3a deposon_diffusion.py 含统一入口 denoise
PASS A3b 四文件不再含复制循环体
PASS A4 既有 import 不破且对象 is 同一
PASS B5a 附录 A 无 deposon_v20_gt5.json 误标
PASS B5b 附录 A 含 per_graph_detail.S6 追溯
PASS B6a §6.5 硬件同构可行性段含 18/22 与方向性
PASS B6b §5.6 含 1740 与 0 违规
PASS B6c §6.4 含 GT-2B 选项自由度教训
PASS B6d §6.3 含 λ=2 反场 artifact
PASS B7 Findings_v2.0_photonics 主结论 18/22 且无 14/22（更正注记段除外）
PASS B8 run_v20_gt3b_fetch.py 错误路径过 _sanitize
PASS B8 run_v20_gt3c_fetch.py 错误路径过 _sanitize
PASS B9 口径词计数快照逐一对照（判死9/inconclusive14/no_separation7/consistency4/探索性6/观察性规律3/待核19）
PASS B10 References 编号 [1]-[59] 连续无缺无重
PASS B11 全仓密钥红线 grep = 0
PASS B12 REVISION_LOG_v2X.md 含第 20 条

FAILS=0
exit=0

### 非空转抽查（对抗核实）
- §6.3（L492–502）L498 含「λ=2 阴性消融（E9.6）暴露反场…」；
- §6.5（L525–）标题「硬件同构可行性（方向性证据）」，L528/L532 含 18/22；
- §6.4（L502–525）L523 含「选项自由度」；
- 节级切片边界经 grep 行号与标题位置逐一核对，切片命中目标节而非邻节。
