import json, io, sys, math
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

C8 = 'results/_v3_recheck_08c_preexp_data/result_2026_09_27.json'
CB = 'results/_v3_recheck_08b_executor/result_2026_09_27.json'
d8 = json.load(open(C8, encoding='utf-8'))
db = json.load(open(CB, encoding='utf-8'))

EPS = 1e-12              # 08b executor L60 冻结
FLOAT_NOISE = 1e-24      # 08b executor L65 冻结

print('########## F-3 : response-curve statistics ##########')
print('--- per-fixture (08c, 9 runs each: 3 schemes x 3 seeds) ---')
byfix = {}
for r in d8['runs']:
    byfix.setdefault(r['fixture_id'], []).append(r)

for fx in sorted(byfix):
    rs = byfix[fx]
    fv = [r['r2_full']['r2'] for r in rs]
    cv = [r['r2_clipped']['r2'] for r in rs]
    fvv = [v for v in fv if v is not None]
    cvv = [v for v in cv if v is not None]
    # plateau: max run of consecutive bit-exact equal values within each run's ladder
    rng = None
    if fvv and cvv:
        rng = max(max(fvv) - min(fvv), max(cvv) - min(cvv))
    # slope: d r2 / d n_clipped per run, and across-seed slope
    print(' ', fx)
    print('     n_defined_full=%d  n_defined_clip=%d  distinct_all=%d' % (
        len(fvv), len(cvv), len(set([round(float(v),12) for v in fvv+cvv]))))
    print('     range(r2)      = %r' % (rng,))
    print('     range/EPS      = %r' % (None if rng is None else rng / EPS,))
    if fvv:
        print('     r2_full  min=%r max=%r' % (min(fvv), max(fvv)))
    if cvv:
        print('     r2_clip  min=%r max=%r' % (min(cvv), max(cvv)))
    # plateau length: within-run, longest run of identical r2 across schemes (n_full ladder)
    d8s = []
    for r in rs:
        a = r['n_full']
        d8s.append(len(a))
    print('     n_full ladder sizes:', sorted(set(d8s)))

print()
print('--- CTRL2 / CTRL1 (08b) response curve, seed dim ---')
c2 = db['controls']['CTRL2_NOOP_emulation_of_v3_defect']['rows']
c1 = db['controls']['CTRL1_POSITIVE_tier_varying_synthetic']['rows']
for name, rows in (('CTRL2', c2), ('CTRL1', c1)):
    v = [r['r2_full']['r2'] for r in rows]
    rr = max(v) - min(v)
    print(' ', name, 'n=%d' % len(v), 'range=%r' % rr, 'range/EPS=%r' % (rr / EPS),
          'n_distinct=%d' % len(set(v)), 'min=%r max=%r' % (min(v), max(v)))
    print('      residual_mass ss_res/ss_tot per row:',
          ['%r' % (r['r2_full']['ss_res'] / r['r2_full']['ss_tot']) for r in rows])
print('  CTRL2 has n_clipped dim?', 'no  (delta_block(full, full) - same object)')
print('  CTRL2 P values present in rows?', ['P_tier_mean_over_resampled_models' in r for r in c2])
print('  CTRL1 P values present in rows?', ['P_tier_mean_over_resampled_models' in r for r in c1])
