#!/bin/bash
fail=0; R=deposon-repo
# 四件产物
for f in deposon_paper_final_cn.pdf deposon_paper_final_cn.docx deposon_paper_final_en.pdf deposon_paper_final_en.docx; do
  [ -s "$f" ] || { echo "FAIL missing $f"; fail=1; }; done
# 终稿锚点
for g in "T-P1c" "三层级" "融合稀释" "附录 A"; do grep -q "$g" $R/paper/deposon_paper_final_cn.md || { echo "FAIL cn:$g"; fail=1; }; done
for g in "T-P1c" "three tiers|three-tier" "kill" "Appendix A"; do grep -qE "$g" $R/paper/deposon_paper_final_en.md || { echo "FAIL en:$g"; fail=1; }; done
# 图语言一致
[ $(grep -c "_cn.png" $R/paper/deposon_paper_final_cn.md) -ge 5 ] || { echo FAIL cnfig; fail=1; }
[ $(grep -c "_en.png" $R/paper/deposon_paper_final_en.md) -ge 5 ] || { echo FAIL enfig; fail=1; }
grep -q "_cn.png" $R/paper/deposon_paper_final_en.md && { echo FAIL en-has-cn-fig; fail=1; }
# EN 无 CJK
python3 -c "
import re,sys
t=open('$R/paper/deposon_paper_final_en.md',encoding='utf-8').read()
assert not re.search(r'[一-鿿]',t), 'CJK in EN'
print('EN CJK-free ok')" || fail=1
# V3 文档
for g in "均衡稳定化成本" "可验证宣言" "判死线" "61 图/338 任务"; do grep -q "$g" $R/docs/V3X_COLLAB_DIRECTIONS.md || { echo "FAIL v3:$g"; fail=1; }; done
! grep -q "338 图\|338 张" $R/docs/V3X_COLLAB_DIRECTIONS.md || { echo FAIL v3-unit; fail=1; }
# pytest
cd $R && python -m pytest -q 2>&1 | tail -1 | grep -q "398 passed" || { echo FAIL pytest; fail=1; }
cd ..
# 密钥 0 泄露（全部新文件）
! grep -rlq "sk-kimi\|ark-[0-9a-f]{8}" $R/paper/deposon_paper_final_*.md $R/docs/V3X_COLLAB_DIRECTIONS.md $R/tools/make_figures_v2_en.py build/translate_en.py || { echo FAIL keys; fail=1; }
echo "exit=$fail"; exit $fail
