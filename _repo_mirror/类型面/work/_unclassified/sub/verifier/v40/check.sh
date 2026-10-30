#!/bin/bash
fail=0; R=deposon-repo
A=$R/paper/deposon_paper_final_cn.md; B=$R/paper/deposon_paper_final_en.md
for f in deposon_paper_final_cn.pdf deposon_paper_final_cn.docx deposon_paper_final_en.pdf deposon_paper_final_en.docx; do [ -s "$f" ] || { echo FAIL $f; fail=1; }; done
# 元表述清零（终稿红线）
for w in "统一终稿" "阶段稿" "V1.X" "V2.X" "内部工件" "存在性实证"; do grep -q "$w" $A && { echo "FAIL cn-meta:$w"; fail=1; }; done
for w in "stage-draft" "internal artifact" "companion document" "empirical evidence for the existence"; do grep -qi "$w" $B && { echo "FAIL en-meta:$w"; fail=1; }; done
# N1 锚点
grep -q "单调性与近梯度性实证" $A || { echo FAIL cn-N1; fail=1; }
grep -q "monotonicity and near-gradientness of an auditable scalar" $B || { echo FAIL en-N1; fail=1; }
# R1 工件
python3 -c "
import json; d=json.load(open('$R/results/deposon_v22_e95ci.json'))
assert d['method']=='newcomb_unpaired_conservative'
assert abs(d['gsm8k']['ci'][0]+0.11803)<1e-4 and abs(d['strategyqa']['ci'][1]-0.08759)<1e-4
print('e95ci JSON ok')" || fail=1
# R2 锚点
grep -q "20/22" $A && grep -q "L_geography_world" $A || { echo FAIL cn-R2; fail=1; }
# ref [51] 无悬挂引用
grep -q "\[51\]" $A $B && { echo FAIL ref51; fail=1; }
# pytest（新脚本加入后应仍全过）
cd $R && python -m pytest -q 2>&1 | tail -1 | grep -qE "39[0-9] passed|4[0-9][0-9] passed" || { echo FAIL pytest; fail=1; }; cd ..
! grep -rlq "sk-kimi\|ark-[0-9a-f]{8}" $R/paper/deposon_paper_final_*.md $R/run_v22_e95ci.py || { echo FAIL keys; fail=1; }
echo "exit=$fail"; exit $fail
