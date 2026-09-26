## v27 run2 2026-08-29T12:02:44+00:00（run1 脚本 NameError 修复后重跑，run1 保留）
cmd: python3 verifier/v27/check.py
PASS GT-2B verdict == inconclusive（如实，不美化）
PASS T∈{1,2,3} 三档齐全
PASS rule_filter 非单调（0.15/0.275/0.20）
PASS T=2 与既有题库 27.5% 逐点复现
PASS 场免疫破坏如实记录（field 随 T 上升）
PASS SPEC 含判死线/单调判据/零 API 声明
PASS Findings 披露选项构成假象（判据设计缺陷）
PASS GT-2B 新文件无密钥串
PASS pytest 246 全绿

FAILS=0
exit=0
