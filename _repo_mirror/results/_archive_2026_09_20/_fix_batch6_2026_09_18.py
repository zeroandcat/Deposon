# -*- coding: utf-8 -*-
"""Trae 2026-09-18 修复 #6: 修正 _fix_batch2 自身引入的 4 处语法错误 (字面 \\n 未转真换行)。"""
import hashlib
from pathlib import Path

ROOT = Path(r'D:\私人资料\deposon-repo')
BAD = "    nums = # [Trae 2026-09-18 修复 P1-2 千分位] 补逗号容错\\n    nums = re.findall(r'-?\\d[\\d,]*(?:\\.\\d+)?', text)"
GOOD = ("    # [Trae 2026-09-18 修复 P1-2 千分位] 补逗号容错\n"
        "    nums = re.findall(r'-?\\d[\\d,]*(?:\\.\\d+)?', text)")

FILES = ['_p_l_v3_phase2_runner_2026_09_17.py',
         '_p_l_v3_phase2_glm53_only_2026_09_17.py',
         '_p_l_v3_phase2_closedsource_runner_2026_09_17.py',
         '_p_l_v3_phase2_closedsource_runner_v2_2026_09_17.py']

def sha12(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]

for name in FILES:
    p = ROOT / name
    s = p.read_text(encoding='utf-8')
    before = sha12(p)
    if BAD in s:
        s = s.replace(BAD, GOOD, 1)
        p.write_text(s, encoding='utf-8')
        # 立即 compile 验证
        try:
            compile(p.read_text(encoding='utf-8'), str(p), 'exec')
            status = 'compile OK'
        except Exception as e:
            status = 'COMPILE FAIL: ' + str(e)[:80]
        print(f'  fixed {name}: {before} -> {sha12(p)} | {status}')
    else:
        # 尝试宽松匹配 (变体)
        import re
        pat = re.compile(r'(\s*)nums = # \[Trae 2026-09-18 修复 P1-2 千分位\] 补逗号容错\\n(\s*)nums = re\.findall\(r\'-?\d\[\\d,\]\*\(\?:\\\.\\d\+\)\?\', text\)')
        s2, n = pat.subn(lambda m: f"{m.group(1)}# [Trae 2026-09-18 修复 P1-2 千分位] 补逗号容错\n{m.group(2)}nums = re.findall(r'-?\\d[\\d,]*(?:\\.\\d+)?', text)", s)
        if n:
            p.write_text(s2, encoding='utf-8')
            try:
                compile(p.read_text(encoding='utf-8'), str(p), 'exec')
                status = 'compile OK'
            except Exception as e:
                status = 'COMPILE FAIL: ' + str(e)[:80]
            print(f'  fixed(regex) {name}: {before} -> {sha12(p)} | {status}')
        else:
            print(f'  PATTERN-NOT-FOUND {name} (当前 sha12={sha12(p)})')

print()
print('_fix_batch6_2026_09_18 DONE')
