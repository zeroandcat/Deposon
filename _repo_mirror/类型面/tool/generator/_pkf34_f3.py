import json, io, sys, math
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

C8 = 'results/_v3_recheck_08c_preexp_data/result_2026_09_27.json'
CB = 'results/_v3_recheck_08b_executor/result_2026_09_27.json'
d8 = json.load(open(C8, encoding='utf-8'))
db = json.load(open(CB, encoding='utf-8'))

print('########## PART 1: F-3 response curve ##########')
print('--- 08c FIX-D runs (9) : r2_full / r2_clipped ---')
fd = [r for r in d8['runs'] if r['fixture_id'] == 'FIX-D_powerlaw_exact']
print('n runs =', len(fd))
vals_full, vals_clip = [], []
for r in fd:
    print(' ', r['scheme_id'], 'seed', r['trial_seed'],
          '| r2_full', repr(r['r2_full']['r2']), '| r2_clip', repr(r['r2_clipped']['r2']),
          '| delta', repr(r['delta']))
    vals_full.append(r['r2_full']['r2'])
    vals_clip.append(r['r2_clipped']['r2'])
allv = vals_full + vals_clip
print('FIX-D distinct r2 (18 values):', sorted(set(allv)))
print('FIX-D range(r2_full) =', max(vals_full) - min(vals_full))
print('FIX-D range(r2_clip) =', max(vals_clip) - min(vals_clip))
print('FIX-D range(ALL)     =', max(allv) - min(allv))
print('FIX-D all == 1.0 bit-exact:', all(v == 1.0 for v in allv))

print()
print('--- 08c all fixtures: r2 range per fixture (response curve dynamic range) ---')
byfix = {}
for r in d8['runs']:
    byfix.setdefault(r['fixture_id'], {'f': [], 'c': []})
    byfix[r['fixture_id']]['f'].append(r['r2_full']['r2'])
    byfix[r['fixture_id']]['c'].append(r['r2_clipped']['r2'])
for fx, d in byfix.items():
    fv = [x for x in d['f'] if x is not None]
    cv = [x for x in d['c'] if x is not None]
    print(' ', fx, '| n=', len(d['f']),
          '| range_full=', (max(fv)-min(fv)) if fv else None,
          '| range_clip=', (max(cv)-min(cv)) if cv else None,
          '| n_distinct_all=', len(set([x for x in d['f']+d['c'] if x is not None])))

print()
print('--- 08b CTRL2 (3 rows) : r2_full response across seed dim ---')
c2 = db['controls']['CTRL2_NOOP_emulation_of_v3_defect']['rows']
c2v = [r['r2_full']['r2'] for r in c2]
for r in c2:
    print('  seed', r['trial_seed'], '| r2', repr(r['r2_full']['r2']),
          '| n_points', r['r2_full']['n_points'],
          '| ss_res', repr(r['r2_full']['ss_res']),
          '| ss_tot', repr(r['r2_full']['ss_tot']),
          '| ss_res/ss_tot', r['r2_full']['ss_res']/r['r2_full']['ss_tot'])
print('CTRL2 range(r2_full) =', max(c2v) - min(c2v))
print('CTRL2 distinct =', len(set(c2v)), 'min', min(c2v), 'max', max(c2v))

print()
print('--- 08b CTRL1 (tier-varying synthetic) ---')
c1 = db['controls']['CTRL1_POSITIVE_tier_varying_synthetic']['rows']
print('n rows', len(c1))
for r in c1:
    print('  seed', r['trial_seed'], '| r2_full', repr(r['r2_full']['r2']),
          '| P', r.get('P_tier_mean_over_resampled_models'),
          '| n_points', r['r2_full']['n_points'])
c1v = [r['r2_full']['r2'] for r in c1]
print('CTRL1 range(r2_full) =', max(c1v)-min(c1v), 'distinct', len(set(c1v)))
print('CTRL1[0].r2 == CTRL2[seed42].r2 ?', c1[0]['r2_full']['r2'] == c2[0]['r2_full']['r2'])
