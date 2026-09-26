## v27 run1 2026-08-29T12:02:00+00:00
cmd: python3 verifier/v27/check.py
PASS GT-2B verdict == inconclusive（如实，不美化）
PASS T∈{1,2,3} 三档齐全
PASS rule_filter 非单调（0.15/0.275/0.20）
PASS T=2 与既有题库 27.5% 逐点复现
Traceback (most recent call last):
  File "/mnt/agents/output/deposon-repo/verifier/v27/check.py", line 27, in <module>
    check("场免疫破坏如实记录（field 随 T 上升）", fm[2] > fm[1] > fm[0])
                                                   ^^
NameError: name 'fm' is not defined
exit=1
