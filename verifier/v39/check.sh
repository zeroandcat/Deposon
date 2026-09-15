#!/bin/bash
fail=0; R=deposon-repo
for f in deposon_paper_final_cn.pdf deposon_paper_final_cn.docx deposon_paper_final_en.pdf deposon_paper_final_en.docx; do
  [ -s "$f" ] || { echo "FAIL $f"; fail=1; }; done
A=$R/paper/deposon_paper_final_cn.md; B=$R/paper/deposon_paper_final_en.md
# 大修锚点
for g in "已闭合（预登记判定）" "ECR" "Newcombe-Wilson" "未检出" "Φ=Σu_i" "系统采样" "aeefb8ef6972" "Artifact availability"; do grep -q "$g" $A || { echo "FAIL cn:$g"; fail=1; }; done
for g in "closed (pre-registered)" "empirical coordination ratio" "Newcombe-Wilson" "systematically sampled" "aeefb8ef6972" "Artifact availability" "post-hoc provenance"; do grep -q "$g" $B || { echo "FAIL en:$g"; fail=1; }; done
# 残留清零
grep -q "因果增量为零" $A && { echo FAIL cn-overclaim; fail=1; }
grep -q "causal accuracy increment is zero" $B && { echo FAIL en-overclaim; fail=1; }
grep -q "小图穷举" $A && { echo FAIL cn-exhaustive; fail=1; }
grep -q "provenanceance\|closed (pre-registered)ance" $B && { echo FAIL en-artifact; fail=1; }
# 引用 60-64
for n in 60 61 62 63 64; do grep -q "^\[$n\]" $A || { echo "FAIL cn-ref$n"; fail=1; }; done
# V3 文档断链修复
grep -q "THINKING_V3_GT_CONTRIB_2026" $R/docs/V3X_COLLAB_DIRECTIONS.md || { echo FAIL v3link; fail=1; }
[ -s $R/docs/THINKING_V3_GT_CONTRIB_2026.md ] || { echo FAIL v3file; fail=1; }
# 图: CN 图新于 EN 脚本重跑(均 12:51+), 抽检 fig2 无 tofu 由人工目检已确认
[ $(find $R/figures -name "*_cn.png" -newer $R/tools/make_figures_v2_en.py | wc -l) -eq 5 ] || { echo FAIL cnfig-stale; fail=1; }
# pytest
cd $R && python -m pytest -q 2>&1 | tail -1 | grep -q "398 passed" || { echo FAIL pytest; fail=1; }; cd ..
# 密钥
! grep -rlq "sk-kimi\|ark-[0-9a-f]{8}" $R/paper/deposon_paper_final_*.md $R/docs/V3X_COLLAB_DIRECTIONS.md $R/docs/THINKING_V3_GT_CONTRIB_2026.md || { echo FAIL keys; fail=1; }
echo "exit=$fail"; exit $fail
