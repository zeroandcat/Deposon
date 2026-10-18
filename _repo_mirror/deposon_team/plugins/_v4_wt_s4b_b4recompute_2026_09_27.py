# -*- coding: utf-8 -*-
"""_v4_wt_s4b_b4recompute — B4 逐字段重算 + 候选字段搜索（只读）"""
import hashlib, json, statistics, itertools
from pathlib import Path
REPO = Path(r'D:\私人资料\deposon-repo'); RES = REPO / 'results'

PJ = json.loads((RES / '_p_j_convergence_basin_2026_09_16' / 'p_j_convergence_basin_results_2026_09_16.json').read_text(encoding='utf-8'))
V3 = json.loads((RES / 'deposon_v3_physical_opt_60cells_2026_09_11.json').read_text(encoding='utf-8'))

def st(vals, mode='pop'):
    vals = [float(x) for x in vals]
    n = len(vals); nd = len(set(vals))
    sd = statistics.pstdev(vals) if (n > 1 and mode == 'pop') else (statistics.stdev(vals) if n > 1 else 0.0)
    return n, nd, round(sd, 6)

print('=' * 100)
print('B4 声明值（第一梯队 #26 rescript §3.1）:')
print('  T_frac60 : n=9 nd=9 std=0.1198')
print('  cos_sim  : n=9 nd=6 std=0.0648')
print('  D_fix2_cosine: n=9 nd=8 std=0.0596')
print('  T30      : n=9 nd=8 std=3.24')
print('=' * 100)

print()
print('--- 逐字段实测（pop / sample 双口径）---')
tf = PJ['all_results']['T_frac60']
print(f'  P-J T_frac60  {tf}')
print(f'      pop={st(tf)}  sample={st(tf,"sample")}   声明 (9,9,0.1198)')

for name, path in [('cos_sim', ('decision_lines_36', 'in_bin_36', 'cos_sim')),
                   ('D_fix2_cosine', ('P_C_distortion_bound_60cells', 'per_model', 'D_fix2_cosine')),
                   ('T30', ('P_C_distortion_bound_60cells', 'per_model', 'T30')),
                   ('T_frac60(60cells)', ('P_C_distortion_bound_60cells', 'per_model', 'T_frac60'))]:
    try:
        arr = [d[path[-1]] for d in V3[path[0]][path[1]]]
        print(f'  {name:<20} {arr}')
        print(f'      pop={st(arr)}  sample={st(arr,"sample")}')
    except Exception as e:
        print(f'  {name:<20} ERR {e}')

print()
print('--- 候选搜索：是否存在任一字段组合产出声明值（含其它可能字段）---')
TARGETS = {'T_frac60': (9, 9, 0.1198), 'cos_sim': (9, 6, 0.0648),
           'D_fix2_cosine': (9, 8, 0.0596), 'T30': (9, 8, 3.24)}
def leaves(o, path=''):
    if isinstance(o, dict):
        for k, v in o.items(): yield from leaves(v, path + '/' + k)
    elif isinstance(o, list) and o and not isinstance(o[0], (dict, list)):
        yield path, o
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from leaves(v, f'{path}[{i}]')

found = {}
for path, arr in itertools.chain(leaves(PJ), leaves(V3)):
    try:
        for mode in ('pop', 'sample'):
            n, nd, sd = st(arr, mode)
            for tname, (tn, tnd, tsd) in TARGETS.items():
                if n == tn and nd == tnd and abs(sd - tsd) < 5e-5:
                    found.setdefault(tname, []).append((path, mode, n, nd, sd))
    except Exception:
        pass
if found:
    for k, v in found.items():
        print(f'  {k}: 命中')
        for row in v: print(f'      {row}')
else:
    print('  0 命中 —— 全 JSON 树中无任何叶子数组的 (n, nd, std_pop) 或 (…, std_sample) 等于声明值')

print()
print('--- 逐行「不符」判定 ---')
rows = [
 ('P-J T_frac60', st(tf, 'pop'), (9, 9, 0.1198)),
 ('cos_sim', st([d['cos_sim'] for d in V3['decision_lines_36']['in_bin_36']], 'pop'), (9, 6, 0.0648)),
 ('D_fix2_cosine', st([d['D_fix2_cosine'] for d in V3['P_C_distortion_bound_60cells']['per_model']], 'pop'), (9, 8, 0.0596)),
 ('T30', st([d['T30'] for d in V3['P_C_distortion_bound_60cells']['per_model']], 'pop'), (9, 8, 3.24)),
]
for name, got, want in rows:
    ok = (got[0] == want[0] and got[1] == want[1] and abs(got[2] - want[2]) < 5e-5)
    print(f'  {"一致" if ok else "不符"}  {name:<18} 实测 n{got[0]} nd{got[1]} std{got[2]}  vs 声明 n{want[0]} nd{want[1]} std{want[2]}')

print()
print('--- 门结论检验：4 行在两套数字下是否均 pass（门判据）---')
print('  门判据（预登记 §3.1 上下文）: n_distinct > 3（防退化）+ std > 0')
for name, got, want in rows:
    print(f'  {name:<18} 实测 nd{got[1]}>3={got[1]>3} std>0={got[2]>0} | 声明 nd{want[1]}>3={want[1]>3} std>0={want[2]>0} → 均 pass={got[1]>3 and got[2]>0 and want[1]>3 and want[2]>0}')
print()
print('_wt_s4b DONE')
