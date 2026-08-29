## v29 run2 2026-08-29T15:04:51+00:00（run1 字段名修复后重跑）
cmd: python3 verifier/v29/check.py
PASS GT-8b verdict == inconclusive（有效域 1<2，不美化）
PASS 有效域 chinese_dynasties 满足阈值且在 satisfied 清单
PASS 先验 0.7805 ≫ field 0.0732（阈值 ≥0.6 且 margin>0.2）
PASS chemical_elements 记 cache_missing
PASS 修正案 B1 登记（240s/预算 9/写于重试前声明）
PASS Findings 披露 fetch_failed 全细节
PASS Findings 披露自选择偏差局限
PASS Findings 含预算台账 9 次
PASS GT-8b 全部新文件/缓存无密钥串
PASS pytest 255 全绿

FAILS=0
exit=0