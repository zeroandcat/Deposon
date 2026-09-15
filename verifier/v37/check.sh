#!/bin/bash
fail=0
cd /mnt/agents/output/deposon-repo
python - <<'PY' || fail=1
import json
v = json.load(open("results/deposon_v22_p1c.json"))["verdict"]
assert v["verdict"] == "killed" and v["min_cos_per_state_best_tau"] <= -1.0 + 1e-9, v
print("P1c JSON verdict locked: killed")
PY
grep -q "P1c 残余主张判死" ../deposon_成果汇报_2026.md || { echo FAIL report; fail=1; }
grep -q "398 passed" ../deposon_成果汇报_2026.md || { echo FAIL report398; fail=1; }
for f in docs/SPEC_GT2C.md docs/SPEC_GT5C.md; do grep -q "判死线" $f || { echo FAIL $f; fail=1; }; done
! grep -rq "sk-kimi\|ark-[0-9a-f]{8}" run_v22_p1c.py tests/test_v22_p1c.py docs/SPEC_GT2C.md docs/SPEC_GT5C.md results/deposon_v22_p1c.json || { echo FAIL keys; fail=1; }
echo "exit=$fail"; exit $fail
