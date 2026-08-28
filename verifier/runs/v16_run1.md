# verifier v16 运行记录

## 2026-08-28 13:32:05 run1
- 命令: python3 verifier/v16/check.py
- 退出码: 1（文献体量阈值 15KB 过严，A 扫描 12KB/40 条高密度核验文献被误判）

## 2026-08-28 13:32:50 run2（阈值 15KB→10KB）
- 退出码: 0
- FAILS: 0 / PASS: 27
- 无 FAIL
