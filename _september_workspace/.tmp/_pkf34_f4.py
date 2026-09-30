import json, io, sys, math
import numpy as np
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

C8 = 'results/_v3_recheck_08c_preexp_data/result_2026_09_27.json'
CB = 'results/_v3_recheck_08b_executor/result_2026_09_27.json'
d8 = json.load(open(C8, encoding='utf-8'))
db = json.load(open(CB, encoding='utf-8'))
EPS = 1e-12; FN = 1e-24

def ols_resid(tiers, pvals):
    x = np.log10(np.asarray(tiers, dtype=float))
    y = np.log10(np.asarray(pvals, dtype=float))
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    pred = A @ coef
    r = y - pred
    ss_res = float((r**2).sum()); ss_tot = float(((y-y.mean())**2).sum())
    return r, float(coef[0]), float(coef[1]), ss_res, ss_tot

def sign_flips(r, nz_tol):
    s = []
    for v in r:
        if abs(v) <= nz_tol: s.append(0)
        elif v > 0: s.append(1)
        else: s.append(-1)
    fl = 0; prev = 0
    for v in s:
        if v == 0: continue
        if prev != 0 and v != prev: fl += 1
        prev = v
    return fl, s

def pct(a, q):
    return float(np.percentile(np.asarray(a, dtype=float), q))

print('########## F-4 : residual structure ##########')
print('=== 08c : per fixture, leg=full ===')
byfix = {}
for r in d8['runs']:
    byfix.setdefault(r['fixture_id'], []).append(r)

hdr = '%-32s %-5s %-6s %-11s %-13s %-11s %-9s %-9s'
print(hdr % ('fixture','schem','seed','ss_res/ss_tot','max|r|/ss_tot_sd','max|r|','n_flip','ss_res'))
rows_out = []
for fx in sorted(byfix):
    for r in byfix[fx]:
        for leg in ('full','clipped'):
            tiers = r['n_full'] if leg=='full' else r['n_clipped']
            pvals = r['P_full_synthetic'] if leg=='full' else r['P_clipped_synthetic']
            blk = r['r2_full'] if leg=='full' else r['r2_clipped']
            if blk['r2'] is None:
                print('%-32s %-5s %-6s %-11s %-13s %-11s %-9s %-9s  [%s r2=%s status=%s]' % (
                    fx, r['scheme_id'], r['trial_seed'], 'UNDEF','-','-','-','-',
                    leg, blk['r2'], blk['r2_status']))
                continue
            res, beta, A0, ss_res, ss_tot = ols_resid(tiers, pvals)
            y = np.log10(np.asarray(pvals,dtype=float))
            sd = float(y.std(ddof=0))
            mx = float(np.abs(res).max())
            # noise tol: relative to machine epsilon of y magnitude
            nzt = float(np.abs(y).max()) * 2.220446049250313e-16
            fl, s = sign_flips(res, nzt)
            ratio = ss_res/ss_tot if ss_tot>0 else None
            rows_out.append((fx, r['scheme_id'], r['trial_seed'], leg, ratio, mx, fl, ss_res, sd))
            print(hdr % (fx, r['scheme_id'], r['trial_seed'], '%r'%ratio if ratio is not None else '-',
                         '%r'%(mx/sd if sd>0 else None), '%r'%mx, str(fl), '%r'%ss_res))

print()
print('=== 08b : CTRL1 / CTRL2 tiers=%r ===' % db['controls']['CTRL1_POSITIVE_tier_varying_synthetic']['rows'][0].get('tiers', [30,60,540]))
tiers = [30,60,540]
for name in ('CTRL1_POSITIVE_tier_varying_synthetic','CTRL2_NOOP_emulation_of_v3_defect'):
    rows = db['controls'][name]['rows']
    for r in rows:
        pv = r.get('P_tier_mean_over_resampled_models')
        blk = r['r2_full']
        if pv is None:
            print('  %s seed=%d : NO P on row (no-op reuses same r2 object); r2=%r ss_res=%r ss_tot=%r ratio=%r' % (
                name, r['trial_seed'], blk['r2'], blk['ss_res'], blk['ss_tot'], blk['ss_res']/blk['ss_tot']))
            continue
        res, beta, A0, ss_res, ss_tot = ols_resid(tiers, pv)
        y = np.log10(np.asarray(pv,dtype=float)); sd=float(y.std(ddof=0)); mx=float(np.abs(res).max())
        nzt = float(np.abs(y).max())*2.220446049250313e-16
        fl,s = sign_flips(res, nzt)
        print('  %s seed=%d : ratio=%r max|r|=%r max|r|/sd=%r n_flip=%d signs=%s on-disk ss_res=%r' % (
            name, r['trial_seed'], ss_res/ss_tot, mx, mx/sd if sd>0 else None, fl, s, blk['ss_res']))
