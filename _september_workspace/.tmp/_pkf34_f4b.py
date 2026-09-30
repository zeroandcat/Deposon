import json, io, sys, math
import numpy as np
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

C8 = 'results/_v3_recheck_08c_preexp_data/result_2026_09_27.json'
CB = 'results/_v3_recheck_08b_executor/result_2026_09_27.json'
d8 = json.load(open(C8, encoding='utf-8'))
db = json.load(open(CB, encoding='utf-8'))
EPS = 1e-12; FN = 1e-24
EPS64 = float(np.finfo(np.float64).eps)   # 2.220446049250313e-16

def stats(tiers, pvals):
    x = np.log10(np.asarray(tiers, dtype=float))
    y = np.log10(np.asarray(pvals, dtype=float))
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    r = y - A @ coef
    ss_res = float((r**2).sum()); ss_tot = float(((y-y.mean())**2).sum())
    sd = float(y.std(ddof=0)); mx = float(np.abs(r).max())
    ar = np.abs(r)
    # noise-tolerant sign flips
    nz = float(np.abs(y).max()) * EPS64
    s = [0 if abs(v) <= nz else (1 if v > 0 else -1) for v in r]
    fl = 0; prev = 0
    for v in s:
        if v == 0: continue
        if prev != 0 and v != prev: fl += 1
        prev = v
    n = len(r)
    out = {
        'n_points': n,
        'ss_res': ss_res, 'ss_tot': ss_tot,
        'mass_ratio': (ss_res/ss_tot if ss_tot > 0 else None),
        'sd_y': sd,
        'norm_max_resid': (mx/sd if sd > 0 else None),
        'mean_abs_resid': float(ar.mean()),
        'rms_resid': float(np.sqrt((r**2).mean())),
        'max_over_rms': (mx/float(np.sqrt((r**2).mean())) if (r**2).mean() > 0 else None),
        'max_over_mean_abs': (mx/float(ar.mean()) if ar.mean() > 0 else None),
        'sign_flips': fl,
        'flip_density': (fl/(n-1) if n > 1 else None),
        'n_sign_runs': (fl+1),
        'abs_resid_deciles': [float(np.percentile(ar, q)) for q in (0,25,50,75,90,100)],
    }
    return out

print('################ F-4 scale-free residual structure ################')
byfix = {}
for r in d8['runs']:
    byfix.setdefault(r['fixture_id'], []).append(r)

print()
print('=== 08c all fixtures / all legs : key structure stats ===')
print('%-26s %-6s %-6s %-4s %-11s %-11s %-10s %-9s %-9s %-6s %-6s' % (
    'fixture','scheme','seed','leg','mass_ratio','norm_max','max_over_rms','max/meanabs','flipdens','nflip','nruns'))
agg = {}
for fx in sorted(byfix):
    for r in byfix[fx]:
        for leg in ('full','clipped'):
            tiers = r['n_full'] if leg=='full' else r['n_clipped']
            pvals = r['P_full_synthetic'] if leg=='full' else r['P_clipped_synthetic']
            blk = r['r2_full'] if leg=='full' else r['r2_clipped']
            st = stats(tiers, pvals)
            agg.setdefault(fx, []).append((leg, st))
            print('%-26s %-6s %-6s %-4s %-11s %-11s %-10s %-9s %-9s %-6s %-6s' % (
                fx, r['scheme_id'], r['trial_seed'], leg,
                '%r'%st['mass_ratio'] if st['mass_ratio'] is not None else '-',
                '%r'%st['norm_max_resid'] if st['norm_max_resid'] is not None else '-',
                '%r'%st['max_over_rms'] if st['max_over_rms'] is not None else '-',
                '%r'%st['max_over_mean_abs'] if st['max_over_mean_abs'] is not None else '-',
                '%r'%st['flip_density'] if st['flip_density'] is not None else '-',
                st['sign_flips'], st['n_sign_runs']))

print()
print('=== per-fixture ranges of the structure stats (leg pooled) ===')
for fx in sorted(agg):
    legs = agg[fx]
    for key in ('mass_ratio','norm_max_resid','max_over_rms','max_over_mean_abs','flip_density'):
        vals = [st[key] for _, st in legs if st[key] is not None]
        if vals:
            print('  %-26s %-18s min=%-14r max=%-14r n=%d' % (fx, key, min(vals), max(vals), len(vals)))
    print()

print('=== 08b CTRL1 (= CTRL2 same-object fit; verify r2 bit-identical per seed) ===')
c1 = db['controls']['CTRL1_POSITIVE_tier_varying_synthetic']['rows']
c2 = db['controls']['CTRL2_NOOP_emulation_of_v3_defect']['rows']
m = {r['trial_seed']: r['r2_full']['r2'] for r in c2}
for r in c1:
    st = stats([30,60,540], r['P_tier_mean_over_resampled_models'])
    same = (r['r2_full']['r2'] == m.get(r['trial_seed']))
    print('  CTRL1 seed=%-4d r2_identical_to_CTRL2=%s mass=%-14r norm_max=%-14r max/rms=%-14r max/meanabs=%-12r nflip=%d nruns=%d' % (
        r['trial_seed'], same, st['mass_ratio'], st['norm_max_resid'], st['max_over_rms'],
        st['max_over_mean_abs'], st['sign_flips'], st['n_sign_runs']))
