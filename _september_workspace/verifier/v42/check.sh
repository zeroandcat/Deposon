#!/bin/bash
# v42: 真实重跑审计归档 + P-D 指纹方向并入 + handoff 机读文档
O=/mnt/agents/output; R=$O/deposon-repo; fail=0
# 1 审计工件
[ -s $O/AUDIT_2026-08-30.json ] && grep -q '"overall": "PASS' $O/AUDIT_2026-08-30.json || { echo "FAIL audit"; fail=1; }
grep -q "prior_state" $O/AUDIT_2026-08-30.json || { echo "FAIL audit-honesty"; fail=1; }
# 2 handoff 机读文档
python3 -c "import json; d=json.load(open('$O/HANDOFF_MACHINE_READABLE.json')); assert d['schema']=='deposon-handoff/v1' and 'P-D' in d['v3x_collab_directions']['priority']" || { echo "FAIL handoff"; fail=1; }
# 3 V3X 的 P-D
grep -q "P-D" $R/docs/V3X_COLLAB_DIRECTIONS.md && grep -q "指纹" $R/docs/V3X_COLLAB_DIRECTIONS.md || { echo "FAIL v3-pd"; fail=1; }
! grep -qE "PoA|已证|相变|统一终稿|阶段稿|V1\.X|V2\.X" $R/docs/V3X_COLLAB_DIRECTIONS.md || { echo "FAIL v3-stale"; fail=1; }
# 4 压缩包含三件新物
unzip -l $O/deposon_core_bundle_final.zip | grep -q "HANDOFF_MACHINE_READABLE.json" || { echo "FAIL zip-handoff"; fail=1; }
unzip -p $O/deposon_core_bundle_final.zip deposon-repo/docs/V3X_COLLAB_DIRECTIONS.md | grep -q "P-D" || { echo "FAIL zip-v3-stale"; fail=1; }
# 5 密钥零落盘（泛化模式，含审计与handoff新文件）
! grep -rlq "sk-kimi-[0-9A-Za-z]\{20,\}\|ark-[0-9a-f-]\{20,\}" $O/AUDIT_2026-08-30.json $O/HANDOFF_MACHINE_READABLE.json $R/docs/ $O/verifier/v42/ 2>/dev/null || { echo "FAIL keys"; fail=1; }
[ $fail -eq 0 ] && echo "PASS v42" || echo "FAIL v42"
exit $fail
