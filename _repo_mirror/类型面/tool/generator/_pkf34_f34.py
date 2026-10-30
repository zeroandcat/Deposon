import json, io, sys, math
import numpy as np
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

C8 = 'results/_v3_recheck_08c_preexp_data/result_2026_09_27.json'
CB = 'results/_v3_recheck_08b_executor/result_2026_09_27.json'
d8 = json.load(open(C8, encoding='utf-8'))
db = json.load(open(CB, encoding='utf-8'))
EPS = 1e-12; EPS64 = float(np.finfo(np.float64).eps)

print('########## CHECK 1: float64 R2-saturation band (F-3 coverage argument) ##########')
for m in (1e-30, 1e-24, 1e-20, 1e-17, 1e-16, 2.220446049250313e-16, 5e-16, 1e-15, 1e-12, 1e-8, 1e-4):
    r2 = 1.0 - m
    print('   mass_ratio=%-24r  r2=1-ratio=%-24r  r2==1.0 ? %s' % (m, r2, r2 == 1.0))
print('   -> float64 R2 saturates to exactly 1.0 once mass_ratio < eps64/2 = %r' % (EPS64/2,))
print('   -> band where F-2 does NOT fire (>=1e-24) but r2 == 1.0 exactly: [1e-24, %r)' % (EPS64/2,))

print()
print('########## CHECK 2: sign-run counts (F-4b kink statistic) ##########')
def resid(tiers, pvals):
    x = np.log10(np.asarray(tiers, dtype=float)); y = np.log10(np.asarray(pvals, dtype=float))
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    return y - A @ coef, y

def runs_and_stats(tiers, pvals):
    res, y = resid(tiers, pvals)
    sd = float(y.std(ddof=0))
    nzt = float(np.abs(y).max())*EPS64
    signs = [0 if abs(v) <= nzt else (1 if v > 0 else -1) for v in res]
    n_runs = 0; prev = 0
    for s in signs:
        if s == 0: continue
        if s != prev: n_runs += 1
        prev = s
    nz = [s for s in signs if s != 0]
    # how many of the first-half vs second-half agree in sign (kink => strong split)
    half = len(nz)//2
    split = None
    if half >= 1:
        a = nz[:half]; b = nz[half:]
        if a and b:
            split = abs(sum(a)/len(a) - sum(b)/len(b))   # in [0,2]
    return dict(n=nzt and len(signs), n_runs=n_runs, n_nz=len(nz),
                norm_max=float(np.abs(res).max()/sd) if sd>0 else None,
                sign_split=split,
                signs=''.join('+' if s>0 else ('-' if s<0 else '0') for s in signs))

byfix = {}
for r in d8['runs']:
    byfix.setdefault(r['fixture_id'], []).append(r)

for fx in sorted(byfix):
    rec=[]
    for r in byfix[fx]:
        for leg in ('full','clipped'):
            tiers = r['n_full'] if leg=='full' else r['n_clipped']
            pvals = r['P_full_synthetic'] if leg=='full' else r['P_clipped_synthetic']
            blk = r['r2_full'] if leg=='full' else r['r2_clipped']
            if blk['r2'] is None: continue
            rec.append(runs_and_stats(tiers,pvals))
    if not rec:
        print(' ', fx, ': 0 DEFINED legs'); continue
    nr = [x['n_runs'] for x in rec]
    nm = [x['norm_max'] for x in rec if x['norm_max'] is not None]
    ss = [x['sign_split'] for x in rec if x['sign_split'] is not None]
    print('  %-26s n_legs=%-3d n_runs min=%d max=%d | norm_max max=%-12r | sign_split min=%s max=%s' % (
        fx, len(rec), min(nr), max(nr), max(nm), (min(ss) if ss else None), (max(ss) if ss else None)))

print()
print('  --- 08b CTRL1 (== CTRL2 same-object fit) ---')
for r in db['controls']['CTRL1_POSITIVE_tier_varying_synthetic']['rows']:
    st = runs_and_stats([30,60,540], r['P_tier_mean_over_resampled_models'])
    print('   seed=%-4d n=%d n_runs=%d n_nz=%d norm_max=%-12r sign_split=%r signs=%s' % (
        r['trial_seed'], st['n'], st['n_runs'], st['n_nz'], st['norm_max'], st['sign_split'], st['signs']))

print()
print('########## CHECK 3: F-3 range(r2) values on the 12 cases ##########')
fd = [r for r in d8['runs'] if r['fixture_id']=='FIX-D_powerlaw_exact']
fdv = [r['r2_full']['r2'] for r in fd] + [r['r2_clipped']['r2'] for r in fd]
c2v = [r['r2_full']['r2'] for r in db['controls']['CTRL2_NOOP_emulation_of_v3_defect']['rows']]
print('  义1 FIX-D : 9 runs, 18 r2 values, distinct=%d, range=%r, range/EPS=%r' % (
    len(set(fdv)), max(fdv)-min(fdv), (max(fdv)-min(fdv))/EPS))
print('  义2 CTRL2 : 3 seeds, range=%r, range/EPS=%r' % (max(c2v)-min(c2v), (max(c2v)-min(c2v))/EPS))
print('  separation ratio CTRL2_range / FIX-D_range : %s (FIX-D range is exactly 0.0)' % 'inf (denominator 0)')
print('  nearest non-zero CTRL2 range = %r = %.4e x EPS' % (max(c2v)-min(c2v), (max(c2v)-min(c2v))/EPS))
