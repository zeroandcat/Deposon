import json, io, sys, math
import numpy as np
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

C8 = 'results/_v3_recheck_08c_preexp_data/result_2026_09_27.json'
CB = 'results/_v3_recheck_08b_executor/result_2026_09_27.json'
d8 = json.load(open(C8, encoding='utf-8'))
db = json.load(open(CB, encoding='utf-8'))
EPS64 = float(np.finfo(np.float64).eps); EPS = 1e-12

def resid(tiers, pvals):
    x = np.log10(np.asarray(tiers, dtype=float)); y = np.log10(np.asarray(pvals, dtype=float))
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    return y - A @ coef, y

def struct(tiers, pvals):
    res, y = resid(tiers, pvals)
    sd = float(y.std(ddof=0))
    nzt = float(np.abs(y).max())*EPS64
    s = [0 if abs(v) <= nzt else (1 if v > 0 else -1) for v in res]
    nz = [v for v in s if v != 0]
    n_runs = 0; prev = 0
    for v in s:
        if v == 0: continue
        if v != prev: n_runs += 1
        prev = v
    m = len(nz)
    return dict(
        n=len(s), n_nz=m, n_runs=n_runs,
        run_density = (n_runs/m if m else None),
        alt_density = ((n_runs-1)/(m-1) if m > 1 else None),
        norm_max = (float(np.abs(res).max()/sd) if sd > 0 else None),
        signs=''.join('+' if v>0 else ('-' if v<0 else '0') for v in s),
    )

byfix = {}
for r in d8['runs']:
    byfix.setdefault(r['fixture_id'], []).append(r)

rec = {}
for fx in ('FIX-A_powerlaw_noisy','FIX-C_two_slope','FIX-D_powerlaw_exact'):
    out=[]
    for r in byfix[fx]:
        for leg in ('full','clipped'):
            t = r['n_full'] if leg=='full' else r['n_clipped']
            p = r['P_full_synthetic'] if leg=='full' else r['P_clipped_synthetic']
            blk = r['r2_full'] if leg=='full' else r['r2_clipped']
            if blk['r2'] is None: continue
            out.append(struct(t,p))
    rec[fx]=out

print('### candidate structural statistics: FIX-A (noise) vs FIX-C (kink) ###')
for k in ('n_runs','run_density','alt_density'):
    for fx in ('FIX-A_powerlaw_noisy','FIX-C_two_slope'):
        v=[x[k] for x in rec[fx] if x[k] is not None]
        print('  %-6s %-22s min=%-8r max=%-8r  values=%s' % (k, fx, min(v), max(v), sorted(v)))
    a=[x[k] for x in rec['FIX-A_powerlaw_noisy'] if x[k] is not None]
    c=[x[k] for x in rec['FIX-C_two_slope'] if x[k] is not None]
    print('       OVERLAP? A=[%r..%r]  C=[%r..%r]  -> %s' % (min(a),max(a),min(c),max(c),
          'YES (no separating threshold)' if (max(c)>=min(a) and max(a)>=min(c)) else 'NO'))
    print()

print('### FIX-C per-ladder detail (kink signature = few runs on the wide ladder) ###')
for fx in ('FIX-C_two_slope','FIX-A_powerlaw_noisy'):
    print(' --', fx)
    for r in byfix[fx]:
        for leg in ('full','clipped'):
            t = r['n_full'] if leg=='full' else r['n_clipped']
            p = r['P_full_synthetic'] if leg=='full' else r['P_clipped_synthetic']
            blk = r['r2_full'] if leg=='full' else r['r2_clipped']
            if blk['r2'] is None: continue
            st = struct(t,p)
            print('    %-6s seed=%-4s %-8s n=%d n_runs=%d run_dens=%-6s signs=%s' % (
                r['scheme_id'], r['trial_seed'], leg, st['n'], st['n_runs'],
                ('%.3f'%st['run_density']) if st['run_density'] is not None else '-', st['signs']))
    print()

print('### CTRL1/CTRL2 (n=3) ###')
for r in db['controls']['CTRL1_POSITIVE_tier_varying_synthetic']['rows']:
    st = struct([30,60,540], r['P_tier_mean_over_resampled_models'])
    print('    seed=%-4d n=%d n_runs=%d run_dens=%s signs=%s norm_max=%r' % (
        r['trial_seed'], st['n'], st['n_runs'], st['run_density'], st['signs'], st['norm_max']))
