import json, io, sys, math
import numpy as np
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

C8 = 'results/_v3_recheck_08c_preexp_data/result_2026_09_27.json'
CB = 'results/_v3_recheck_08b_executor/result_2026_09_27.json'
d8 = json.load(open(C8, encoding='utf-8'))
db = json.load(open(CB, encoding='utf-8'))
EPS = 1e-12; FN = 1e-24; EPS64 = float(np.finfo(np.float64).eps)

def resid(tiers, pvals):
    x = np.log10(np.asarray(tiers, dtype=float)); y = np.log10(np.asarray(pvals, dtype=float))
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    return y - A @ coef, y

def f4a(tiers, pvals):
    res, y = resid(tiers, pvals)
    sd = float(y.std(ddof=0))
    return float(np.abs(res).max()/sd) if sd > 0 else None

# ---------- the 12 cases : 9 FIX-D runs + 3 CTRL2 seeds ----------
print('########## 12/12 run-level verification under proposed thresholds ##########')
print('F-3 gate  : range(r2 response curve) <= EPS(1e-12)  -> 不明·判据零信息量')
print('F-4a gate : max|r|/sd <= EPS(1e-12)                  -> 不明·残差不可读')
print('F-1 gate  : legs_identical (bit-exact)               -> 不明·no-op 平凡零')
print()
rows=[]
fd=[r for r in d8['runs'] if r['fixture_id']=='FIX-D_powerlaw_exact']
# FIX-D: r2 constant across ALL 9 runs x 2 legs -> response curve range
fdv=[r['r2_full']['r2'] for r in fd]+[r['r2_clipped']['r2'] for r in fd]
rng_fd = max(fdv)-min(fdv)
for r in fd:
    nm_f = f4a(r['n_full'], r['P_full_synthetic'])
    nm_c = f4a(r['n_clipped'], r['P_clipped_synthetic'])
    rows.append(dict(fam='FIX-D', key='%s/s%d'%(r['scheme_id'],r['trial_seed']),
        F2 = (r['r2_full']['ss_res']/r['r2_full']['ss_tot'] < FN) and (r['r2_clipped']['ss_res']/r['r2_clipped']['ss_tot'] < FN),
        F3 = rng_fd <= EPS, F4a = (max(nm_f,nm_c) <= EPS), F1=False))
c1={r['trial_seed']:r for r in db['controls']['CTRL1_POSITIVE_tier_varying_synthetic']['rows']}
c2s=sorted(db['controls']['CTRL2_NOOP_emulation_of_v3_defect']['rows'], key=lambda x:x['trial_seed'])
c2v=[r['r2_full']['r2'] for r in c2s]
rng_c2=max(c2v)-min(c2v)
for r in c2s:
    nm = f4a([30,60,540], c1[r['trial_seed']]['P_tier_mean_over_resampled_models'])
    rows.append(dict(fam='CTRL2', key='seed%d'%r['trial_seed'],
        F2 = (r['r2_full']['ss_res']/r['r2_full']['ss_tot'] < FN),
        F3 = rng_c2 <= EPS, F4a = (nm <= EPS), F1=True))

print('%-8s %-12s %-6s %-6s %-6s %-8s %s' % ('family','case','F-1','F-2','F-3','F-4a','cascade landing'))
n_caught=0
for x in rows:
    hits=[k for k in ('F1','F2','F3','F4a') if x[k]]
    first = hits[0] if hits else 'NONE'
    landed = '不明' if hits else 'PASS/FAIL (BAD)'
    if hits: n_caught+=1
    print('%-8s %-12s %-6s %-6s %-6s %-8s first=%-5s -> %s' % (
        x['fam'],x['key'],x['F1'],x['F2'],x['F3'],x['F4a'],first,landed))
print()
print('caught before PASS/FAIL = %d/%d' % (n_caught,len(rows)))
f1=[x for x in rows if x['fam']=='FIX-D']; f2=[x for x in rows if x['fam']=='CTRL2']
print('  义1 FIX-D  9 runs : all land 不明 = %s   (via %s)' % (all(x['F2'] or x['F3'] or x['F4a'] for x in f1),
      'F-2' if all(x['F2'] for x in f1) else 'F-3/F-4a'))
print('  义2 CTRL2  3 seeds: all land 不明 = %s   (via F-1)' % all(x['F1'] for x in f2))

print()
print('########## F-3 threshold margin table ##########')
print('  FIX-D  range(r2)  = %-24r  n_distinct=%d  bit-exact 1.0 x18 = %s' % (rng_fd,len(set(fdv)),all(v==1.0 for v in fdv)))
print('  CTRL2  range(r2)  = %-24r  n_distinct=%d' % (rng_c2,len(set(c2v))))
print('  threshold EPS     = %-24r  (08b executor L60 frozen)' % EPS)
print('  FIX-D  range/EPS  = %-24r  -> fires' % (rng_fd/EPS))
print('  CTRL2 range/EPS   = %-24r  -> does not fire' % (rng_c2/EPS))
print('  FIX-C  range(r2)  = %-24r  (reference: kink family must NOT fire F-3)' % 0.4449880834106396)
print('  FIX-A  range(r2)  = %-24r  (reference: noisy power law must NOT fire F-3)' % 0.5436202561199045)

print()
print('########## F-4a threshold margin table ##########')
nm_fd=[]
for r in fd:
    nm_fd.append(f4a(r['n_full'], r['P_full_synthetic'])); nm_fd.append(f4a(r['n_clipped'], r['P_clipped_synthetic']))
nm_c2=[f4a([30,60,540], c1[r['trial_seed']]['P_tier_mean_over_resampled_models']) for r in c2s]
print('  FIX-D  max|r|/sd  max=%-24r  = %.4f x eps64 ; /EPS = %.4e -> fires' % (max(nm_fd),max(nm_fd)/EPS64,max(nm_fd)/EPS))
print('  CTRL2  max|r|/sd  min=%-24r  = %.4e x eps64 ; /EPS = %.4e -> does NOT fire' % (min(nm_c2),min(nm_c2)/EPS64,min(nm_c2)/EPS))
print('  separation ratio CTRL2_min / FIX-D_max = %.4e' % (min(nm_c2)/max(nm_fd)))
print('  FIX-A  max|r|/sd  max=%-24r  (noisy power law: must NOT fire F-4a)' % 1.674024654129127)
print('  FIX-C  max|r|/sd  max=%-24r  (kink: must NOT fire F-4a)' % 1.305512601072783)

print()
print('########## F-4b kink statistic : FAIL to derive (overlap) ##########')
for fx,lo,hi in (('FIX-A_powerlaw_noisy',0.3333333333333333,1.0),('FIX-C_two_slope',0.3333333333333333,1.0)):
    print('  %-24s run_density in [%r, %r]' % (fx,lo,hi))
print('  => OVERLAP on entire range => NO separating threshold derivable from 08c material')
print('  => F-4b registered as 待给值 (0 self-set), NOT given a fabricated threshold')

print()
print('########## collinearity honesty: F-4a vs F-2 on current material ##########')
agree=0; tot=0
for x in rows:
    tot+=1; agree += (x['F2']==x['F4a'])
print('  run-level agreement = %d/%d (%.0f%%) => F-4a adds 0 INCREMENTAL discrimination on current 12 cases' % (agree,tot,100*agree/tot))
print('  => F-4a role = readability PRECONDITION for F-4b (not an independent discriminator)')
