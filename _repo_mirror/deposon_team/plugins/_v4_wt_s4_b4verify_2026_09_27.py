# -*- coding: utf-8 -*-
"""_v4_wt_s4_b4verify — B4 独立复核：第一梯队 #26 rescript §3.1 表 4 行 vs 源 JSON 重算（只读）"""
import hashlib, json, statistics
from pathlib import Path
REPO = Path(r'D:\私人资料\deposon-repo'); RES = REPO / 'results'

def sha12(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]

# --- 源件 ---
PJ = RES / '_p_j_convergence_basin_2026_09_16' / 'p_j_convergence_basin_results_2026_09_16.json'
V3P = RES / 'deposon_v3_physical_opt_60cells_2026_09_11.json'
print('=== 源件 ===')
for p in (PJ, V3P):
    print(f'  {"OK " if p.exists() else "MISS"} sha12={sha12(p) if p.exists() else "-"} {p.name}')

pj = json.loads(PJ.read_text(encoding='utf-8'))
print()
print('=== P-J JSON 顶层键 ===')
print(' ', list(pj.keys()))
print('=== P-J 全文（1669B，逐字） ===')
print(json.dumps(pj, ensure_ascii=False, indent=1)[:1800])

# 找 T_frac60 / convergence_rates
def walk(o, path=''):
    out = []
    if isinstance(o, dict):
        for k, v in o.items():
            out.append((path + '/' + k, v))
            out += walk(v, path + '/' + k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            out += walk(v, f'{path}[{i}]')
    return out

print()
print('=== P-J 中 T_frac60 / convergence_rate* 叶子 ===')
for pth, v in walk(pj):
    if any(w in pth.lower() for w in ('t_frac60', 'convergence_rate', 't60', 'frac60')):
        s = v if not isinstance(v, list) else f'list[{len(v)}]={v[:12]}'
        print(f'  {pth} = {s}')

print()
print('=== 60cells JSON 顶层键 ===')
v3 = json.loads(V3P.read_text(encoding='utf-8'))
print(' ', list(v3.keys())[:20])

def stat(vals):
    vals = [float(x) for x in vals]
    n = len(vals)
    nd = len(set(vals))
    sd = statistics.pstdev(vals) if n > 1 else 0.0
    return n, nd, round(sd, 6)

print()
print('=== 60cells 中 per-model 字段探测 ===')
cand = {}
for pth, v in walk(v3):
    if isinstance(v, (int, float)) and any(w in pth.lower() for w in ('cos_sim', 'd_fix2', 't30', 't_frac')):
        cand.setdefault(pth.split('[')[0], []).append((pth, v))
for k in list(cand)[:20]:
    print(f'  {k}  ({len(cand[k])} 项)  e.g. {cand[k][:3]}')
print()
print('=== 顶层直接标量/列表字段一览（前 40） ===')
for pth, v in walk(v3):
    if pth.count('/') <= 2 and not isinstance(v, (dict,)):
        s = v if not isinstance(v, list) else f'list[{len(v)}]'
        if isinstance(v, list) and v and not isinstance(v[0], (dict, list)):
            s += f' -> stat={stat(v)}'
        print(f'  {pth} = {s}')
print()
print('_wt_s4_b4verify DONE')
