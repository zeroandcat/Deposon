## v29 run1 2026-08-29T15:03:33+00:00
cmd: python3 verifier/v29/check.py
PASS GT-8b verdict == inconclusive（有效域 1<2，不美化）
PASS 有效域 chinese_dynasties 满足阈值且在 satisfied 清单
Traceback (most recent call last):
  File "/mnt/agents/output/deposon-repo/verifier/v29/check.py", line 14, in <module>
    ns = d["named_summary"]["L_chinese_dynasties"]
         ~^^^^^^^^^^^^^^^^^
KeyError: 'named_summary'
exit=1
