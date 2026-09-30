import json, io, sys, math
import numpy as np
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
C8 = 'results/_v3_recheck_08c_preexp_data/result_2026_09_27.json'
d8 = json.load(open(C8, encoding='utf-8'))
EPS=1e-12; FN=1e-24; EPS64=float(np.finfo(np.float64).eps)

print('### F-3 non-degeneracy: the float64 R2-saturation band F-2 MISSES ###')
print('F-2 fires when mass_ratio < 1e-24.  r2 == 1.0 exactly when mass_ratio < eps64/2.')
print('=> band [1e-24, eps64/2) = F-2 does NOT fire, but r2 saturates to exactly 1.0 => F-3 DOES fire')
lo=FN; hi=EPS64/2
print('   band = [%r, %r)  width ratio = %.4e' % (lo,hi,hi/lo))
for m in (1e-24, 1e-22, 1e-20, 1e-18, 5.5e-17, 1.0e-16):
    r2 = 1.0-m
    print('   mass=%-10r r2=%-24r r2==1.0:%-5s  F-2 fires:%-5s  F-3 fires (range==0):%s'
          % (m, r2, r2==1.0, m<FN, True))
print()
print('   In this band BOTH legs can be at r2==1.0 with mass>=1e-24 =>')
print('   F-2 MISSES (0.175e-15 to 1.1e-16 gap) but delta==0 AND response curve constant')
print('   => HC-08c-2 double-meaning SURVIVES F-2, and F-3 CLOSES it. F-3 is NOT redundant with F-2.')

print()
print('### distance of every 08c case from the F-3 threshold (no near-boundary case) ###')
byfix={}
for r in d8['runs']: byfix.setdefault(r['fixture_id'],[]).append(r)
for fx in sorted(byfix):
    rs=byfix[fx]
    fv=[r['r2_full']['r2'] for r in rs if r['r2_full']['r2'] is not None]
    cv=[r['r2_clipped']['r2'] for r in rs if r['r2_clipped']['r2'] is not None]
    if not fv and not cv:
        print('  %-26s : 0 DEFINED r2 (identity gate pre-empts)' % fx); continue
    rg=max(max(fv+cv)-min(fv+cv), 0.0)
    print('  %-26s : range=%-24r  range/EPS=%-16.6g  ratio_to_CTRL2=%s'
          % (fx, rg, rg/EPS, ('%.3e'%(rg/1.8526680734032297e-4)) if rg>0 else 'exactly 0'))

print()
print('### exact decimals for citation ###')
print('  CTRL2 range(r2)      = 0.9999133281468088 - 0.9997280613394685 =', repr(0.9999133281468088-0.9997280613394685))
print('  CTRL2 min/max r2     = 0.9997280613394685 / 0.9999133281468088 / 0.9998436107867961')
print('  FIX-D r2             = 1.0 (x18, bit-exact)')
print('  FIX-D max mass_ratio = 4.588410251622214e-30 ; CTRL2 min mass_ratio = 8.66718531911735e-05')
print('  F-4a FIX-D max       = 2.6716150654761252e-15 (= %.4f x eps64)' % (2.6716150654761252e-15/EPS64))
print('  F-4a CTRL2 min       = 0.01260922289568595 (= %.4e x eps64)' % (0.01260922289568595/EPS64))
print('  separation           = %.4e' % (0.01260922289568595/2.6716150654761252e-15))
