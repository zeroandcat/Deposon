# -*- coding: utf-8 -*-
"""R2b: simulate 函数值域 + boss_pa_1 JSON 结构 + P_A 表值来源追查。"""
import hashlib, json
from pathlib import Path

REPO = Path(r'D:\私人资料\deposon-repo')
SUB = Path(r'D:\私人资料\deposon-sub')
sha12 = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12].upper()

print('=== A. boss_pa_1_rbr_rm.py simulate 函数体 (repo) ===')
src = (REPO / 'deposon_team' / 'plugins' / 'boss_pa_1_rbr_rm.py').read_text(encoding='utf-8', errors='ignore').splitlines()
for start, end in [(110, 138), (139, 180), (181, 200)]:
    print(f'  --- L{start}-{end} ---')
    for n in range(start, min(end + 1, len(src))):
        print('  L%d: %s' % (n, src[n-1][:130]))

print()
print('=== B. boss_pa_1 JSON 中 per-graph 结构 ===')
d = json.loads((SUB / 'results' / 'boss_pa_1_rbr_rm_result_2026_09_15.json').read_text(encoding='utf-8'))
print('  top keys:', list(d.keys()))
# 找 22 图数组
def find_list(obj, path=''):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, list) and len(v) >= 5 and isinstance(v[0], dict):
                print(f'  list at {path}/{k}: n={len(v)}, item keys={list(v[0].keys())[:10]}')
            find_list(v, path + '/' + k)
find_list(d)

print()
print('=== C. 前 3 图完整记录 (找 RM iter 字段名) ===')
def find_graphs(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, list) and len(v) >= 20 and isinstance(v[0], dict) and any('graph' in str(kk).lower() for kk in v[0].keys()):
                return k, v
            r = find_graphs(v)
            if r:
                return r
    return None
r = find_graphs(d)
if r:
    key, arr = r
    print(f'  key={key} n={len(arr)}')
    for item in arr[:3]:
        print('   ', json.dumps(item, ensure_ascii=False)[:300])

print()
print('=== D. deposon_pa_d1_d3_2026_09_15.json 的 per-graph 表 ===')
pd = REPO / 'results' / 'deposon_pa_d1_d3_2026_09_15.json'
if pd.exists():
    j = json.loads(pd.read_text(encoding='utf-8'))
    print('  sha12=', sha12(pd), 'top keys:', list(j.keys())[:12])
    s = json.dumps(j, ensure_ascii=False)
    # 找 22 图节选表相关字段
    for kw in ['L_algorithm_process', 'rbr_multiplier', 'rm_multiplier', '6.2188', 'bayes_iter']:
        i = s.find(kw)
        if i >= 0:
            print(f'  "{kw}" found: ...{s[max(0,i-60):i+120]}...')
        else:
            print(f'  "{kw}" NOT FOUND')

print()
print('=== E. deposon_pa_d1_d3 JSON 中 22 图逐值 (若有) ===')
if pd.exists():
    def find_graphs2(obj, path=''):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, list) and len(v) >= 20 and isinstance(v[0], dict) and any('rbr' in str(kk).lower() or 'rm' in str(kk).lower() for kk in v[0].keys()):
                    print(f'  graphs at {path}/{k}: n={len(v)}')
                    for item in v[:3]:
                        print('   ', json.dumps(item, ensure_ascii=False)[:280])
                    return True
                if find_graphs2(v, path + '/' + k):
                    return True
        return False
    find_graphs2(j)
print('  _r2b DONE')
