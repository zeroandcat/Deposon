#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# judgment_strictness.py — judge-strictness gauge (preview.5 interface D,
# judgment-line v1.2 candidate). Zero network, zero credentials, zero
# external data: vectors live in mocks/judgment_strictness_vectors.json.
# ----------------------------------------------------------------------------
# Motivation (published readings): a probe judge that marks 150/150 pairs
# identically has zero discrimination — "too loose" first reading (A4 probe,
# 2026-11-22); a chance-level discrimination (VW-3 e16 0.5156) sits at the
# opportunity band. The judgment-line v1.1 interfaces pin WHERE a reading
# sits (measure locator), WHAT was logged (raw-full), and WHICH band
# adjudicates (three-band). They do not pin whether the judge itself can
# discriminate. This gauge closes that gap:
#
#   D. Judge-strictness calibration (strictness gauge):
#      a judge must be calibrated on a published vector set of
#      same-class (S) and different-class (D) pairs before its verdicts
#      adjudicate. The gauge recomputes from declared marks:
#        d  = discrimination   = (TP + TN) / (S + D)     [primary band]
#        lam = loose bias       = FD / D                  [reference band]
#        sig = strict bias      = FS / S                  [reference band]
#      where TP = D-pairs marked different (correct), TN = S-pairs marked
#      same (correct), FD = D-pairs marked same (over-acceptance),
#      FS = S-pairs marked different (over-rejection).
#
#      Primary band (the only adjudicating band): d >= d_lo
#      (boundary inclusive; published vectors pin d_lo = 3/4).
#        d <  d_lo               -> KILL   (judge unusable: floor or chance)
#        missing/empty calibration -> INCONCLUSIVE (zero-contrast evidence,
#                                     needs mechanism-position support)
#      Reference band (reported side-by-side, never adjudicates): lam, sig.
#      Annotation band (thresholded flags, never adjudicates):
#        lam >= lam_hi  -> "too_loose" flag;  sig >= sig_hi -> "too_strict".
#
#      Vector anchors (published fractions):
#        all-same judge   (150/150 same):  d = 0        KILL (floor anchor)
#        chance judge     (76/151 correct): d = 76/151   KILL (< 3/4)
#        healthy judge    (137/151 + partial rejections): d = 137/151  PASS
#        over-strict judge (all-different): d = S/(S+D)  KILL if S/(S+D) < d_lo
#      Boundary exactness: d == d_lo -> PASS (inclusive), by cross-multiplied
#      integer comparison (no float rounding in the band test).
#
# Dual-implementation note: the structural face (band inclusivity, monotone
# complementarity of lam and sig with d at fixed marginals) is a Lean
# candidate for the next preview (v1.2 freeze); this module is the
# executable face, following the g6f_p0_gate.py Python-only precedent.
# ============================================================================
import json
import os
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
VECTORS_PATH = os.path.join(ROOT, "mocks", "judgment_strictness_vectors.json")

# Pre-registered strictness band (frozen for the published vector set).
D_LO = F(3, 4)        # primary band lower edge (inclusive)
LAM_HI = F(1, 10)      # annotation threshold: loose flag
SIG_HI = F(1, 10)      # annotation threshold: strict flag


def calibrate(pairs):
    """Recompute strictness readings from declared calibration marks.

    pairs: list of {"cls": "S"|"D", "mark": "same"|"different"}.
    Returns a dict with exact-Fraction readings, or None on empty input.
    """
    if not pairs:
        return None
    tp = tn = fd = fs = 0
    for p in pairs:
        if p["cls"] not in ("S", "D") or p["mark"] not in ("same", "different"):
            raise ValueError("calibration pair malformed: %r" % (p,))
        if p["cls"] == "D" and p["mark"] == "different":
            tp += 1
        elif p["cls"] == "S" and p["mark"] == "same":
            tn += 1
        elif p["cls"] == "D" and p["mark"] == "same":
            fd += 1
        else:
            fs += 1
    n = len(pairs)
    return {
        "n": n, "tp": tp, "tn": tn, "fd": fd, "fs": fs,
        "d": F(tp + tn, n),
        "lam": F(fd, tp + fd) if (tp + fd) else None,   # D-marginal defined
        "sig": F(fs, tn + fs) if (tn + fs) else None,   # S-marginal defined
    }


def _ge(a, b):
    """Boundary-inclusive >= on exact fractions (cross-multiplied)."""
    return a >= b


def adjudicate(cal):
    """Three-band adjudication over a calibration reading (cal from calibrate).

    Primary band: d >= D_LO (inclusive) is the ONLY adjudicating test.
    """
    if cal is None:
        return {
            "verdict": "INCONCLUSIVE",
            "primary_band": {"measure": "d", "value": None,
                             "line": "%s (inclusive)" % D_LO},
            "reference_band": [],
            "annotation_band": [],
        }
    d = cal["d"]
    verdict = "PASS" if _ge(d, D_LO) else "KILL"
    refs = []
    if cal["lam"] is not None:
        refs.append({"measure": "lam", "value": cal["lam"], "adjudicates": False})
    if cal["sig"] is not None:
        refs.append({"measure": "sig", "value": cal["sig"], "adjudicates": False})
    anns = []
    if cal["lam"] is not None and _ge(cal["lam"], LAM_HI):
        anns.append({"flag": "too_loose", "value": cal["lam"], "adjudicates": False})
    if cal["sig"] is not None and _ge(cal["sig"], SIG_HI):
        anns.append({"flag": "too_strict", "value": cal["sig"], "adjudicates": False})
    return {
        "verdict": verdict,
        "primary_band": {"measure": "d", "value": d,
                         "line": "%s (inclusive)" % D_LO},
        "reference_band": refs,
        "annotation_band": anns,
    }


def run_gate(verbose=True):
    with open(VECTORS_PATH, "r", encoding="utf-8") as f:
        vectors = json.load(f)
    G = {}

    # D1 constant-marks anchor: the 150/150 zero-discrimination probe
    #     (published) — constant "same" marking lands at chance d = 1/2.
    r1 = adjudicate(calibrate(vectors["all_same_150"]))
    G["D1 constant-marks anchor all-same 150/150 -> KILL at chance"] = (
        r1["verdict"] == "KILL" and r1["primary_band"]["value"] == F(1, 2)
        and r1["annotation_band"][0]["flag"] == "too_loose")

    # D2 chance anchor: 76/151 < 3/4 -> KILL (opportunity-band reference).
    r2 = adjudicate(calibrate(vectors["chance_76_of_151"]))
    G["D2 chance anchor 76/151 -> KILL"] = (
        r2["verdict"] == "KILL" and r2["primary_band"]["value"] == F(76, 151))

    # D3 healthy anchor: 137/151 >= 3/4 -> PASS; loose/strict within ann lines.
    r3 = adjudicate(calibrate(vectors["healthy_137_of_151"]))
    G["D3 healthy anchor 137/151 -> PASS"] = (
        r3["verdict"] == "PASS" and r3["primary_band"]["value"] == F(137, 151)
        and r3["annotation_band"] == [])

    # D4 boundary exactness: d == d_lo exactly -> PASS (inclusive edge),
    #     and a one-pair drop below the same margin -> KILL.
    r4a = adjudicate(calibrate(vectors["boundary_exact"]))
    r4b = adjudicate(calibrate(vectors["boundary_minus_one"]))
    G["D4 boundary inclusive exact / one-below kill"] = (
        r4a["verdict"] == "PASS" and r4a["primary_band"]["value"] == D_LO
        and r4b["verdict"] == "KILL")

    # D5 over-strict anchor: all-different marks kill via d alone
    #     (sig is reference band only — never adjudicates).
    r5 = adjudicate(calibrate(vectors["all_different"]))
    G["D5 over-strict anchor killed by primary band only"] = (
        r5["verdict"] == "KILL"
        and any(a["flag"] == "too_strict" for a in r5["annotation_band"])
        and all(ref["adjudicates"] is False for ref in r5["reference_band"]))

    # D6 empty calibration -> INCONCLUSIVE (zero-contrast information).
    r6 = adjudicate(calibrate([]))
    G["D6 empty calibration INCONCLUSIVE"] = r6["verdict"] == "INCONCLUSIVE"

    # D7 malformed pair -> fail loud (ValueError), not silently skipped.
    try:
        calibrate([{"cls": "X", "mark": "same"}])
        G["D7 malformed pair fails loud"] = False
    except ValueError:
        G["D7 malformed pair fails loud"] = True

    ok_all = all(v is True for v in G.values())
    if verbose:
        for k, v in G.items():
            print(("PASS" if v is True else "FAIL"), k)
        print("judgment_strictness gate: %s (%d/%d)" % (
            "ALL PASS" if ok_all else "FAILED",
            sum(1 for v in G.values() if v is True), len(G)))
    return ok_all, G


if __name__ == "__main__":
    sys.exit(0 if run_gate()[0] else 1)
