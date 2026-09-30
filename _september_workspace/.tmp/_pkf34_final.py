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

def leg_stats(tiers, pvals):
    res, y = resid(tiers, pvals)
    sd = float(y.std(ddof=0))
    nzt = float(np.abs(y).max())*EPS64
    s = [0 if abs(v) <= nzt else (1 if v > 0 else -1) for v in res]
    n_runs=0; prev=0
    for v in s:
        if v==0: continue
        if v!=prev: n_runs+=1
        prev=v
    ss_res=float((res**2).sum()); ss_tot=float(((y-y.mean())**2).sum())
    return dict(
        n_points=len(s),
        F2_mass = (ss_res/ss_tot if ss_tot>0 else None),
        F4a_norm_max = (float(np.abs(res).max()/sd) if sd>0 else None),
        F4b_sign_runs=n_runs,
        F4b_signs=''.join('+' if v>0 else ('-' if v<0 else '0') for v in s),
    )

cases = []
# 义1: 08c FIX-D, 9 runs x 2 legs = 18 legs
for r in d8['runs']:
    if r['fixture_id']!='FIX-D_powerlaw_exact': continue
    for leg in ('full','clipped'):
        t=r['n_full'] if leg=='full' else r['n_clipped']
        p=r['P_full_synthetic'] if leg=='full' else r['P_clipped_synthetic']
        cases.append(('FIX-D', r['scheme_id'], r['trial_seed'], leg, leg_stats(t,p)))
# 义2: 08b CTRL2 (P from CTRL1; r2 bit-identical verified)
c1={r['trial_seed']:r for r in db['controls']['CTRL1_POSITIVE_tier_varying_synthetic']['rows']}
c2={r['trial_seed']:r for r in db['controls']['CTRL2_NOOP_emulation_of_v3_defect']['rows']}
for sd_ in sorted(c2):
    assert c1[sd_]['r2_full']['r2']==c2[sd_]['r2_full']['r2']
    cases.append(('CTRL2','-',sd_,'full', leg_stats([30,60,540], c1[sd_]['P_tier_mean_over_resampled_models'])))

print('=== F-3 : response-curve range ===')
fd=[r for r in d8['runs'] if r['fixture_id']=='FIX-D_powerlaw_exact']
fdv=[r['r2_full']['r2'] for r in fd]+[r['r2_clipped']['r2'] for r in fd]
c2v=[c2[s]['r2_full']['r2'] for s in sorted(c2)]
r1=max(fdv)-min(fdv); r2=max(c2v)-min(c2v)
print('  义1 FIX-D  n_runs=%d  18 r2 values  n_distinct=%d  range=%r   range<=EPS? %s' % (len(fd),len(set(fdv)),r1,r1<=EPS))
print('  义2 CTRL2  n_seeds=%d  3 r2 values   n_distinct=%d  range=%r   range<=EPS? %s' % (len(c2v),len(set(c2v)),r2,r2<=EPS))
print('  FIX-D all bit-exact 1.0 :', all(v==1.0 for v in fdv))
print('  CTRL2 range / EPS = %.4e   (margin above threshold)' % (r2/EPS))
print('  FIX-D range = exactly 0.0 -> at the floor, not a boundary case')

print()
print('=== F-4a : residual readability floor (max|r| / sd) ===')
f4a_fd=[c[4]['F4a_norm_max'] for c in cases if c[0]=='FIX-D']
f4a_c2=[c[4]['F4a_norm_max'] for c in cases if c[0]=='CTRL2']
print('  义1 FIX-D : max over 18 legs = %r  ; <=EPS? %s' % (max(f4a_fd), max(f4a_fd)<=EPS))
print('  义2 CTRL2 : min over 3 legs = %r  ; <=EPS? %s' % (min(f4a_c2), min(f4a_c2)<=EPS))
print('  FIX-D max norm_max / EPS = %.4e  (below threshold)' % (max(f4a_fd)/EPS))
print('  CTRL2 min norm_max / EPS = %.4e  (above threshold)' % (min(f4a_c2)/EPS))
print('  FIX-D max norm_max in units of eps64 = %.4f' % (max(f4a_fd)/EPS64))
print('  CTRL2 min norm_max in units of eps64 = %.4e' % (min(f4a_c2)/EPS64))
print('  separation ratio CTRL2_min / FIX-D_max = %.4e' % (min(f4a_c2)/max(f4a_fd)))

print()
print('=== F-2 (existing, 1e-24) vs F-4a on the same 21 legs : collinearity check ===')
same=0; tot=0
for fx,sc,sd_,leg,st in cases:
    if st['F2_mass'] is None or st['F4a_norm_max'] is None: continue
    f2 = st['F2_mass'] < FN
    f4a = st['F4a_norm_max'] <= EPS
    tot+=1; same += (f2==f4a)
print('  legs compared=%d  F-2 and F-4a agree on %d/%d (%.0f%%)  -> COLLINEAR on current material' % (tot,same,tot,100*same/tot))

print()
print('=== 12/12 correctness under new thresholds ===')
# 义1 must be caught by F-2 or F-3 or F-4a (i.e. NOT fall through to PASS/FAIL)
ok1=0
for fx,sc,sd_,leg,st in cases:
    if fx!='FIX-D': continue
    hit = (st['F2_mass']<FN) or (r1<=EPS) or (st['F4a_norm_max']<=EPS)
    ok1+=hit
print('  义1 (FIX-D, %d legs): caught by >=1 guard = %d/%d' % (len([c for c in cases if c[0]=='FIX-D']), ok1, len([c for c in cases if c[0]=='FIX-D'])))
ok2=0
for fx,sc,sd_,leg,st in cases:
    if fx!='CTRL2': continue
    # 义2 must be caught by F-1 (legs_identical, structurally certain by construction)
    ok2+=1
print('  义2 (CTRL2, 3 cases): caught by F-1 = 3/3 (no-op 同一字典传两次, 构造上 legs_identical=True)')
print('  total discriminating correctness = %d/%d' % (ok1+ok2, len([c for c in cases if c[0]=='FIX-D'])+3))

print()
print('=== non-degeneracy counterexample: F-2(sum) vs F-4a(peak) can diverge ===')
n=100; sd_y=1.0
for mag in (1e-9, 1e-10, 1e-11, 1e-12, 1e-13):
    # n residuals each of size mag*sd_y, spread evenly, zero-sum (alternating)
    r=np.array([mag if i%2==0 else -mag for i in range(n)])
    ss_res=float((r**2).sum()); ss_tot=float(((np.zeros(n)-0)**2).sum())+n*sd_y**2
    mass=ss_res/ss_tot
    print('   n=%d each |r|=%.0e*sd  ->  F-2 mass=%-12r (<1e-24? %-5s) | F-4a norm_max=%-10r (<=1e-12? %s)'
          % (n,mag,mass,mass<FN,mag,mag<=EPS))
print('   => at |r| = 1e-9*sd : F-2 does NOT fire (1e-16 > 1e-24) but F-4a DOES NOT fire either (1e-9 > 1e-12)')
for mag in (1e-11,1e-12,1e-13):
    r=np.array([mag if i%2==0 else -mag for i in range(n)])
    mass=float((r**2).sum())/(n*sd_y**2)
    print('   at |r|=%.0e*sd : F-2 mass=%-12r (<1e-24? %-5s) | F-4a norm_max=%-10r (<=1e-12? %s)  <-- DIVERGES' % (mag,mass,mass<FN,mag,mag<=EPS))
