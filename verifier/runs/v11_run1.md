# verifier v11 运行记录

## 2026-08-28 07:56:51 run1
- 命令: python3 verifier/v11/check.py
- 退出码: 1
- FAILS: 2 / PASS: 23
[FAIL] 数据健康 ≥90 — score=None
[FAIL] pytest 全绿

## 2026-08-28 07:57:55 run2（修复 overall_score 键名 + 重装 pytest 后）
- 退出码: 0
- FAILS: 0 / PASS: 25
- 无 FAIL
[PASS] pytest 全绿 — 160 passed
