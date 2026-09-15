#!/bin/bash
# v41: WRAP-2026 收尾验证 — 报告重写 / V3同步 / 压缩包刷新 / 密钥零落盘
O=/mnt/agents/output; R=$O/deposon-repo; fail=0
# 1 报告禁忌词
! grep -qE "统一终稿|阶段稿|V1\.X|V2\.X|存在性实证" $O/deposon_成果汇报_2026.md || { echo "FAIL report-meta"; fail=1; }
# 2 报告锚点
for k in ECR 已闭合 T-P1c 398 deposon_v22_e95ci Newcombe; do grep -q "$k" $O/deposon_成果汇报_2026.md || { echo "FAIL report-anchor:$k"; fail=1; }; done
# 3 V3文档禁忌词与锚点
! grep -qE "PoA|已证|相变" $R/docs/V3X_COLLAB_DIRECTIONS.md || { echo "FAIL v3-stale"; fail=1; }
for k in T-P1c deposon_v22_e95ci 王子贺; do grep -q "$k" $R/docs/V3X_COLLAB_DIRECTIONS.md || { echo "FAIL v3-anchor:$k"; fail=1; }; done
# 4 压缩包含新文件且时间新于旧包
unzip -l $O/deposon_core_bundle_final.zip | grep -q "成果汇报_2026.md" || { echo "FAIL zip-report"; fail=1; }
unzip -p $O/deposon_core_bundle_final.zip deposon-repo/docs/V3X_COLLAB_DIRECTIONS.md | grep -q T-P1c || { echo "FAIL zip-v3-stale"; fail=1; }
unzip -p $O/deposon_core_bundle_final.zip deposon_成果汇报_2026.md | grep -q ECR || { echo "FAIL zip-report-stale"; fail=1; }
# 5 密钥零落盘（泛化模式）
! grep -rlq "sk-kimi-[0-9A-Za-z]\{20,\}\|ark-[0-9a-f-]\{20,\}" $O/deposon_成果汇报_2026.md $R/docs/ $R/paper/ $O/verifier/ 2>/dev/null || { echo "FAIL keys"; fail=1; }
# 6 四件终稿产物存在且非空
for f in deposon_paper_final_cn.pdf deposon_paper_final_cn.docx deposon_paper_final_en.pdf deposon_paper_final_en.docx; do [ -s $O/$f ] || { echo "FAIL artifact:$f"; fail=1; }; done
[ $fail -eq 0 ] && echo "PASS v41" || echo "FAIL v41"
exit $fail
