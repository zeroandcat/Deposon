# Gate arithmetic self-test: pure math, no external data required.
# Vectors are the published P2'-switch-segment aggregates (see BENCHMARK.md).
import sys
from fractions import Fraction as F

def kappa(a, b, m, n, nL, nH):
    return F(a, a + b) - F(m * nL, m * nL + n * nH)

def bias(m, n, nL, nH):
    return F(m * nL, m * nL + n * nH) - F(nL, nL + nH)

def a_caliber(a, b, nL, nH):
    return F(a, a + b) - F(nL, nL + nH)

def b_norm(a, b, m, n, nL, nH):
    return F(64 * b, n * nH) - F(64 * a, m * nL)

# switch segment (published)
a, b, m, n, nL, nH = 191, 53, 971, 181, 13, 19
assert a_caliber(a, b, nL, nH) == F(735, 1952)          # 0.376537...
assert bias(m, n, nL, nH) > F(1, 10)                    # A-caliber decoupled bias > gate
assert abs(kappa(a, b, m, n, nL, nH)) <= F(1, 100)      # coupling component within 0.01
assert abs(b_norm(a, b, m, n, nL, nH)) <= F(1, 10)      # normalized caliber within 0.10
# KIMI segment (G6f supplement, published)
a2, b2, m2, n2 = 301, 63, 1240, 200
assert kappa(a2, b2, m2, n2, nL, nH) == F(229, 12948)   # 0.017686...
assert abs(kappa(a2, b2, m2, n2, nL, nH)) <= F(1, 50)   # within 0.02
assert abs(b_norm(a2, b2, m2, n2, nL, nH)) > F(1, 10)   # B-norm red (reported side-by-side)
# A-main degenerate: n=0 => kappa == 0 identically
assert kappa(648, 0, 2592, 0, nL, nH) == 0
# 2x2 independence zero-locus shared by kappa and b_norm
assert a * n * nH - b * m * nL == -12170                 # switch deviation numerator
assert a2 * n2 * nH - b2 * m2 * nL == 128240            # KIMI deviation numerator
print("test_gates: all assertions passed")
