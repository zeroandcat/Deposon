# -*- coding: utf-8 -*-
"""_v4_wt_s4c_regonly — §B 只登记档证据抽取（B3/B6/B7/B9/B10）（只读）"""
import hashlib, json, re
from pathlib import Path
REPO = Path(r'D:\私人资料\deposon-repo'); RES = REPO / 'results'
def sha12(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]
def T(p): return Path(p).read_text(encoding='utf-8')

print('=' * 104); print('B3 · 短语模式门槛字面 + 实现截断'); print('=' * 104)
rs = json.loads(T(RES / '_v4_pi_cot_v3_ruleset_v3.json'))
def find(o, key, path=''):
    out = []
    if isinstance(o, dict):
        for k, v in o.items():
            if key.lower() in str(k).lower(): out.append((path+'/'+k, v))
            out += find(v, key, path+'/'+k)
    elif isinstance(o, list):
        for i, v in enumerate(o): out += find(v, key, f'{path}[{i}]')
    return out
for pth, v in find(rs, 'phrase'):
    print(f'  {pth} = {json.dumps(v, ensure_ascii=False)[:400]}')
print('  ruleset "seed" 字段:', find(rs, 'seed'))

ex = T(RES / '_v4_pi_cot_v3_ruleset_v3_executor.py')
m = re.search(r'PHRASE_PATTERNS_V3\s*=\s*\[[^\]]*\]', ex, re.S)
print()
print('  v3 executor PHRASE_PATTERNS_V3 字面:')
print('   ', (m.group(0)[:400] if m else 'NOT FOUND'))

print()
print('=' * 104); print('B6 · seed 字面偏移（ruleset seed 42 vs 实现 SEED+13/11/42）'); print('=' * 104)
print('  ruleset_v3 "seed":', find(rs, 'seed'))
for ln in ex.splitlines():
    if 'RandomState' in ln and ('SEED' in ln or '42' in ln):
        print(f'    {ln.strip()[:130]}')

print()
print('=' * 104); print('B7 · D4 relabel 表 + accuracy'); print('=' * 104)
j = json.loads(T(RES / '_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json'))
rt = j.get('relabel_table')
print('  relabel_table:')
if isinstance(rt, list):
    for r in rt: print('   ', json.dumps(r, ensure_ascii=False)[:260])
else:
    print('   ', json.dumps(rt, ensure_ascii=False)[:700])
print('  accuracy:', json.dumps(j.get('accuracy'), ensure_ascii=False)[:400])
print('  judge_type_distribution:', json.dumps(j.get('judge_type_distribution'), ensure_ascii=False)[:300])
d4 = json.loads(T(RES / '_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json'))
print('  原 d4 件 judge_type:', json.dumps(find(d4, 'judge_type'), ensure_ascii=False)[:500])

print()
print('=' * 104); print('B9 · T1.5r2 verdict §0 字节行'); print('=' * 104)
v = T(RES / '_v4_supp_t15r2_verdict.md')
for i, ln in enumerate(v.splitlines(), 1):
    if '53,923' in ln or '53923' in ln or 'T1.5r2 prereg' in ln or '97,059' in ln:
        print(f'  L{i}: {ln[:180]}')
print(f'  prereg 实测: {sha12(RES / "_v4_supp_prereg_v02_add_T15r2_2026_09_26.md")} {(RES / "_v4_supp_prereg_v02_add_T15r2_2026_09_26.md").stat().st_size}B')

print()
print('=' * 104); print('B10 · JSV 撤除落地（v1 原件含 JSV？v1.2 已撤？）'); print('=' * 104)
v1 = T(RES / '_v3_recheck_prereg_v1_2026_09_27.md')
v1p2 = T(RES / '_v3_recheck_prereg_v1p2_2026_09_27.md')
for nm, txt in (('v1', v1), ('v1p2', v1p2)):
    n_jsv = txt.count('Jordan-Sucher-Votek') + txt.count('Votek') + txt.count('JSV')
    print(f'  {nm}: JSV 相关命中 {n_jsv} 次')
for i, ln in enumerate(v1p2.splitlines(), 1):
    if 'JSV' in ln or 'Votek' in ln:
        print(f'  v1p2 L{i}: {ln[:150]}')

print()
print('=' * 104); print('§A · 两个 kill-line 在 executor 中的实现行'); print('=' * 104)
e01 = T(RES / '_v3_recheck_01_executor_2026_09_27.py')
e04 = T(RES / '_v3_recheck_04_executor_2026_09_27.py')
for nm, txt, pats in (('#01', e01, ('nd_primary', 'sd_primary', '>= 4', 'BAYES_MAX_ITER', 'RM_TOL')),
                      ('#04', e04, ('structurally_unreachable', 'nd', 'PASS', '括号'))):
    print(f'  --- {nm} ---')
    for i, ln in enumerate(txt.splitlines(), 1):
        if any(p in ln for p in pats) and not ln.strip().startswith('#'):
            print(f'    L{i}: {ln.strip()[:150]}')
print()
print('_wt_s4c DONE')
