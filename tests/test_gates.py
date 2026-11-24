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

# Judge-strictness gauge (preview.5 interface D) — same arithmetic, asserted
# through the gate module (gates/judgment_strictness.py; vectors in
# mocks/judgment_strictness_vectors.json).
_spec = importlib.util.spec_from_file_location(
    "judgment_strictness", os.path.join(_ROOT, "gates", "judgment_strictness.py"))
_js = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_js)
_ok, _g = _js.run_gate(verbose=False)
assert _ok, {k: v for k, v in _g.items() if v is not True}
# hand-checked anchors (published readings): constant-marks probe 150/150
# lands at chance d = 1/2 (zero discrimination kills); healthy 137/151 passes.
assert _js.F(75, 150) == _js.F(1, 2)
assert _js.F("137/151") > _js.F("3/4") > _js.F("76/151")

# Six-family linkage validator (preview.5 interface E)
_spec = importlib.util.spec_from_file_location(
    "family_linkage", os.path.join(_ROOT, "gates", "family_linkage.py"))
_fl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_fl)
_ok, _g = _fl.run_gate(verbose=False)
assert _ok, {k: v for k, v in _g.items() if v is not True}
print("test_gates: preview.5 assertions passed")

# Slot-space caliber gauge (preview.7 interface F) — same arithmetic, asserted
# through the gate module (gates/slot_space_caliber.py; vectors in
# mocks/slot_space_vectors.json). preview.8 N1 pin: the F1 share is
# pos_term / moment (the reported second moment), NOT pos_term / uniform_var.
_spec = importlib.util.spec_from_file_location(
    "slot_space_caliber", os.path.join(_ROOT, "gates", "slot_space_caliber.py"))
_sc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_sc)
_ok, _g = _sc.run_gate(verbose=False)
assert _ok, {k: v for k, v in _g.items() if v is not True}
assert _sc.F(40368, 40511) > _sc.F(1, 2)            # gate-line share on the D1 anchor -> INVALID
assert _sc.F(3364) / (_sc.F(16383, 12)) > 2          # wrong-denominator read (~2.46): reference face only
assert _sc.F(3364) / (_sc.F(16383, 12)) != _sc.F(40368, 40511)  # different denominators, never the gate line
print("test_gates: preview.8 assertions passed (slot-space caliber gate + N1 denominator pin)")

# Slot-space caliber dual-implementation cross-check (preview.9 closes the
# "Lean mirror candidate" item): the core-only Lean mirror (0 sorry; axiom
# audit transcribed in docs/slot-space-caliber.md) is re-verified statement by
# statement against the Python integer mirror, the executable face, and the
# published vectors. CI carries no Lean toolchain -> the cross-check is textual
# + arithmetic, never a re-compile.
_sc = importlib.util.module_from_spec(importlib.util.spec_from_file_location(
    "slot_space_crosscheck", os.path.join(_ROOT, "gates", "slot_space_crosscheck.py")))
_sc.__spec__.loader.exec_module(_sc)
_ok, _g = _sc.run_crosscheck()
assert _ok, {k: v for k, v in _g.items() if v is not True}
print("test_gates: preview.9 interface F cross-check assertions passed (%d checks)" % len(_g))

# f3 calibration face (preview.9): a judge is calibrated before its marks
# adjudicate. The published N9 DR-2 judge reading is INCONCLUSIVE for
# strictness (every probe sees one face -> no D-marginal), while its
# pre-registered main-1 face is reported side by side, never replaced.
_dc = importlib.util.module_from_spec(importlib.util.spec_from_file_location(
    "descrev_calibration", os.path.join(_ROOT, "gates", "descrev_calibration.py")))
_dc.__spec__.loader.exec_module(_dc)
_ok, _g = _dc.run_gate(verbose=False)
assert _ok, {k: v for k, v in _g.items() if v is not True}
import json as _json
_dr2 = _json.load(open(_dc.VECTORS_PATH, encoding="utf-8"))["dr2_published"]
_r = _dc.calibration_face(_dr2["pkgs"], _dr2["attributions"])
assert _r["verdict"] == "INCONCLUSIVE" and _r["reason_code"] == "ZERO_CONTRAST" and _r["d_pairs"] == 0
assert _dr2["main1_attribution_acc"] >= _dr2["main1_threshold"]   # pre-registered face stands
print("test_gates: preview.9 f3 calibration-face assertions passed (%d checks)" % len(_g))

# Readings-package completeness validator (preview.9 interface G): a complete
# package scores 8/8; the granularity trap (a ledger row without a key-level
# field, e.g. a flattened evict_seq) is NOT a key-level ledger -> key-level
# gates UNDECIDABLE, never silently passed.
_rc = importlib.util.module_from_spec(importlib.util.spec_from_file_location(
    "readout_completeness", os.path.join(_ROOT, "gates", "readout_completeness.py")))
_rc.__spec__.loader.exec_module(_rc)
_ok, _g = _rc.run_gate(verbose=False)
assert _ok and _g["all_pass"], _g
import tempfile as _tf
with _tf.TemporaryDirectory() as _td:
    _pkg = _rc.build_fixture(_td, "tg_complete", None, False)
    _r = _rc.score_package(_pkg, run_recompute=True)
    assert _r["score"] == 8 and _r["verdict"] == "COMPLETE" and _r["key_level"] == "DECIDABLE", _r
    _ops = [f for f in os.listdir(_pkg) if "ledger" in f]
    assert len(_ops) == 1
    open(os.path.join(_pkg, _ops[0]), "w", encoding="utf-8").write('{"evict_seq": [[1, 2], [3, 4]], "token_sim": 0.3}\n')
    _r2 = _rc.score_package(_pkg, run_recompute=True)
    assert _r2["items"][6]["status"] == "FAIL" and _r2["key_level"] == "UNDECIDABLE", _r2
print("test_gates: preview.9 interface G completeness-validator assertions passed")
