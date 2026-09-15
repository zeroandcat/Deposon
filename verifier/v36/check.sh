#!/bin/bash
fail=0
F1=deposon_v3定义与博弈论贡献思考_2026.md; F2=deposon_成果汇报_2026.md
for g in "不是测不准原理的同构演化" "均衡稳定化成本" "王子贺" "守恒≠真值" "Q7" "部分承诺"; do grep -q "$g" "$F1" || { echo "FAIL F1: $g"; fail=1; }; done
for g in "定位思考" "判死" "均衡稳定化成本" "0.484→0.452" "deposon_v3定义与博弈论贡献思考" "非冻结 JSON" "## 七、交付物清单"; do grep -q "$g" "$F2" || { echo "FAIL F2: $g"; fail=1; }; done
# no project files modified check skipped (no code touched by design)
echo "exit=$fail"; exit $fail
