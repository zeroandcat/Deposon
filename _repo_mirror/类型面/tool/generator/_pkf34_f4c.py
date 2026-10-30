import json, io, sys, math
import numpy as np
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

C8 = 'results/_v3_recheck_08c_preexp_data/result_2026_09_27.json'
d8 = json.load(open(C8, encoding='utf-8'))
EPS = 1e-12; EPS64 = float(np.finfo(np.float64).eps)

def resid(tiers, pvals):
    x = np.log10(np.asarray(tiers, dtype=float)); y = np.log10(np.asarray(pvals, dtype=float))
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    return y - A @ coef, y, x

def longest_run(signs):
    best = cur = 0; prev = 0
    for s in signs:
        if s == 0: continue
        if s == prev: cur += 1
        else: prev = s; cur = 1
        best = max(best, cur)
    return best

def lag1(r):
    if len(r) < 3: return None
    r = np.asarray(r) - np.mean(r)
    d = float((r**2).sum())
    if d == 0: return None
    return float((r[:-1]*r[1:]).sum()/d)

byfix = {}
for r in d8['runs']:
    byfix.setdefault(r['fixture_id'], []).append(r)

print('### residual sign / run / decile structure, per fixture (legs pooled, only DEFINED legs) ###')
print('%-26s %-9s %-11s %-11s %-11s %-10s %-10s %-9s' % (
    'fixture','n_legs','norm_max','longest_run','run/n','lag1_autocorr','p90/p50','flipdens'))
for fx in sorted(byfix):
    rec = []
    for r in byfix[fx]:
        for leg in ('full','clipped'):
            tiers = r['n_full'] if leg=='full' else r['n_clipped']
            pvals = r['P_full_synthetic'] if leg=='full' else r['P_clipped_synthetic']
            blk = r['r2_full'] if leg=='full' else r['r2_clipped']
            if blk['r2'] is None: continue
            res, y, x = resid(tiers, pvals)
            sd = float(y.std(ddof=0))
            nzt = float(np.abs(y).max())*EPS64
            signs = [0 if abs(v) <= nzt else (1 if v > 0 else -1) for v in res]
            nz = [s for s in signs if s != 0]
            lr = longest_run(signs)
            ar = np.abs(res)
            p50 = float(np.percentile(ar,50)); p90 = float(np.percentile(ar,90))
            fl = 0; prev=0
            for s in signs:
                if s==0: continue
                if prev!=0 and s!=prev: fl+=1
                prev=s
            rec.append(dict(
                norm_max = float(np.abs(res).max()/sd) if sd>0 else None,
                longest_run = lr,
                run_frac = lr/(len(res)-1) if len(res)>1 else None,
                lag1 = lag1(res),
                p90_p50 = (p90/p50) if p50>0 else None,
                flipdens = fl/(len(res)-1) if len(res)>1 else None,
                signs = ''.join('+' if s>0 else ('-' if s<0 else '0') for s in signs),
            ))
    def rng(k):
        v=[x[k] for x in rec if x[k] is not None]
        return (min(v),max(v)) if v else (None,None)
    for k in ('norm_max','longest_run','run_frac','lag1','p90_p50','flipdens'):
        lo,hi = rng(k)
        print('  %-26s %-9s %-11r %-11r' % (fx if k=='norm_max' else '', k, lo, hi))
    print('    sign patterns:', ' | '.join(x['signs'] for x in rec[:8]))
    print()
