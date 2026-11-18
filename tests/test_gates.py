# Gate arithmetic self-test: pure math, no external data required.
# Vectors are the published P2'-switch-segment aggregates (see BENCHMARK.md).
import os
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

# Judgment-line v1.1 interfaces (gauge gate / raw-full obligation / three-band
# adjudication) — same arithmetic, asserted through the gate module itself
# (loads gates/judgment_v11.py by path; vectors in mocks/judgment_v11_vectors.json).
import importlib.util
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_spec = importlib.util.spec_from_file_location(
    "judgment_v11", os.path.join(_ROOT, "gates", "judgment_v11.py"))
_jv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_jv)
_ok, _g = _jv.run_gate(verbose=False)
assert _ok, {k: v for k, v in _g.items() if v is not True}
# hand-checked anchors (mirror the Lean vector theorems in gates/judgment_v11.lean)
assert _jv.F("38/152") < _jv.F("13/50")                  # key-level below the line
assert _jv.F("646/2432") > _jv.F("13/50")                # flattened mis-read above it
assert _jv.F("620/2432") < _jv.F("13/50")                # and the mirrored flip case
print("test_gates: all assertions passed")
