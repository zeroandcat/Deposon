# -*- coding: utf-8 -*-
"""_v4_wt_s2_b1diff — B1 修复面 diff：v3 原 executor vs r1 executor（只读）"""
import difflib, hashlib, os

REPO = r'D:\私人资料\deposon-repo'
A = os.path.join(REPO, 'results', '_v4_pi_cot_v3_ruleset_v3_executor.py')
B = os.path.join(REPO, 'results', '_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py')
C = os.path.join(REPO, 'results', '_v4_pi_cot_v2_ruleset_v2_executor.py')

def sha12(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]

la = open(A, encoding='utf-8').read().splitlines()
lb = open(B, encoding='utf-8').read().splitlines()
lc = open(C, encoding='utf-8').read().splitlines()

print(f'A v3原  {sha12(A)}  {len(la)} 行')
print(f'B v3r1  {sha12(B)}  {len(lb)} 行')
print(f'C v2原  {sha12(C)}  {len(lc)} 行')
print()

# 定位 reasoning_full 段
def find_seg(lines, key='reasoning_full', ctx=22):
    for i, l in enumerate(lines):
        if 'if "reasoning_full" in sup' in l:
            return i
    return None

ia = find_seg(la); ib = find_seg(lb); ic = find_seg(lc)
print('=' * 100)
print(f'v3原 L{ia+1} 起 18 行:')
print('=' * 100)
for i in range(ia, ia+16):
    print(f'  {i+1:>4}| {la[i]}')
print()
print('=' * 100)
print(f'v3r1 L{ib+1} 起 18 行:')
print('=' * 100)
for i in range(ib, ib+16):
    print(f'  {i+1:>4}| {lb[i]}')
print()
print('=' * 100)
print(f'v2原 L{ic+1} 起 16 行:')
print('=' * 100)
for i in range(ic, ic+16):
    print(f'  {i+1:>4}| {lc[i]}')

print()
print('=' * 100)
print('统一 diff：v3原 → v3r1（全文，只看 -/+ 行）')
print('=' * 100)
d = list(difflib.unified_diff(la, lb, lineterm='', n=2, fromfile='v3_orig', tofile='v3r1'))
minus = [x for x in d if x.startswith('-') and not x.startswith('---')]
plus = [x for x in d if x.startswith('+') and not x.startswith('+++')]
print(f'  - 行数 = {len(minus)}  /  + 行数 = {len(plus)}')
print()
for x in d[:120]:
    print('  ' + x)
if len(d) > 120:
    print(f'  ... (共 {len(d)} 行 diff)')
print('_b1diff DONE')
