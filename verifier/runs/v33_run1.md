## v33 run1 2026-08-30（首轮验收）
cmd: python3 verifier/v33/check.py
PASS A1 pytest 全绿且 >=274
  [pytest] 274 passed, 1 warning in 33.90s
PASS A2a def row_normalize 全仓仅 1 处且在 deposon_protocol.py
PASS A2b 退火循环体全仓仅 1 份
PASS A3a deposon_diffusion.py 含统一入口 denoise
PASS A3b 四文件不再含复制循环体（run_v19_meanfield/deposon_fast/run_v20_gt5/run_v20_gt7）
PASS A4 既有 import 不破且对象 is 同一（row_normalize/prior_score_matrix/full_candidate_mask/field_scores_init）
PASS B5a 附录 A 无 deposon_v20_gt5.json 误标
PASS B5b 附录 A 含 per_graph_detail.S6 追溯
FAIL B6a §6.5 硬件同构可行性段含 18/22 与方向性
PASS B6b §5.6 含 1740 与 0 违规
PASS B6c §6.4 含 GT-2B 选项自由度教训
FAIL B6d §6.3 含 λ=2 反场 artifact
PASS B7 Findings_v2.0_photonics 主结论 18/22 且无 14/22（更正注记段除外）
PASS B8 run_v20_gt3b_fetch.py 错误路径过 _sanitize
PASS B8 run_v20_gt3c_fetch.py 错误路径过 _sanitize
PASS B9 口径词计数快照逐一对照（判死9/inconclusive14/no_separation7/consistency4/探索性6/观察性规律3/待核19）
PASS B10 References 编号 [1]-[59] 连续无缺无重
PASS B11 全仓密钥红线 grep = 0
PASS B12 REVISION_LOG_v2X.md 含第 20 条

FAILS=2
exit=1

### 失败判定（非检查器 bug，实证为工件缺口）
- B6a：`grep "^#" deposon_paper_v2X.md` 显示 Discussion 仅有 6.1–6.4，**§6.5 不存在**；
  全文 grep `18/22`、`硬件`、`同构`、`photonics` 在 paper/v2/deposon_paper_v2X.md 均为 0 命中。
  即「§6.5 硬件同构可行性段（18/22、方向性）」未写入正文。
- B6d：§6.3 现为「方法学局限」（单厂商图生成器 + 题库小样本），全文 grep `反场` 0 命中；
  λ 仅出现于 §4.2 融合稀释（λ∈{0.25,0.5,1,2}，hybrid 不增），无「λ=2 反场 artifact」教训段。
- 注：18/22 在 docs/Findings_v2.0_photonics.md 第 27 行在案（B7 PASS），但未同步进论文正文 §6.5。
- 修复责任在实施侧（论文补写 §6.5 与 §6.3 λ=2 段）；verifier 不改工件，修复后重跑 run2 复核。
