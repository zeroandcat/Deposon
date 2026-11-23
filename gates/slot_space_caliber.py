#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# slot_space_caliber.py — slot-space caliber gauge (preview.7 interface F,
# judgment-line v1.3 candidate). Zero network, zero credentials, zero
# external data: vectors live in mocks/slot_space_vectors.json.
# ----------------------------------------------------------------------------
# Motivation (published readings): a dispersion statistic (`slot_var`) was
# reused verbatim from a probe line whose task slot space is 0..127 (center
# 63.5, the uniform mean) onto a line whose observed slots collapsed to
# {0..11} (sample mean 5.5). The reported "variance" 3375.9 was 99.6%
# position term (mean - c)^2 = 3364; the true variance was 11.9167; the
# normalized ratio flipped direction 2.473 ("over-dispersion") ->
# 0.0087 ("strong collapse") — D1 G2/V3R3 round, correction registered
# 2026-11-24 (frozen face 0-touch; separate correction file).
#
# The identity E[(x - c)^2] = Var(x) + (mean - c)^2 is the machine-checkable
# decomposition. This gauge closes the caliber gap:
#
#   F. Slot-space caliber gauge:
#      a reported slot-dispersion statistic must be recomputable from the
#      raw slot observations plus the center and slot space it declares.
#      The gauge recomputes, as exact rationals:
#        var_true   = E[(x - mean)^2]        (sample-mean centered)
#        pos_term   = (mean - c)^2           (center-offset artifact)
#        moment     = E[(x - c)^2]           (what the statistic actually was)
#        share      = pos_term / moment      (position-term dominance)
#      Checks:
#        F1 center-caliber (primary band, adjudicates):
#           share <= 1/2 (inclusive) -> the dispersion reading STANDS;
#           share >  1/2             -> INVALID (the reported statistic is
#                                       majority center-offset, not
#                                       dispersion; must be recomputed).
#        F2 slot-space membership (primary band, adjudicates):
#           every observed slot must lie in [0, space_hi];
#           a violation -> INVALID (the declared space does not contain
#           the observations).
#        F3 ratio caliber (reference, never adjudicates):
#           the normalized ratio must use var_true over the uniform-space
#           variance (space_hi+1)^2 - 1)/12; the defective-face ratio
#           (moment in the numerator) is recomputed side-by-side and
#           reported, never adjudicated on.
#      Degenerate cases: n == 0 -> INCONCLUSIVE (no observations);
#      moment == 0 -> share := 0 (perfectly at-center, no offset).
#
#      Vector anchors (published fractions, D1 correction file 2af01f9538f7):
#        D1 R1 enumeration {0..11}, c = 63.5:
#            share = 40368/40511 > 1/2   INVALID (position term 99.6%)
#            var_true = 143/12;  ratio_true = 143/16383 (0.0087 collapse)
#            moment = 40511/12 (= 3375.9 at 1dp);
#            ratio_defective = 40511/16383 (= 2.473 at 3dp)
#        f8j v73frozen call 04 (readings package c5aa9cc8e73d), c = 63.5:
#            share = 27/44764            VALID (caliber appropriate in the
#                                         0..127 space; sample mean 64.25)
#      Boundary exactness: share == 1/2 -> VALID (inclusive), by exact
#      fraction comparison (no float in any band test).
#
# Dual-implementation note: the structural face (moment decomposition
# identity, share band inclusivity) is a Lean candidate for a following
# preview; this module is the executable face, following the
# judgment_strictness.py Python-only precedent.
# ============================================================================
import json
import os
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
VECTORS_PATH = os.path.join(ROOT, "mocks", "slot_space_vectors.json")

# Pre-registered caliber band (frozen for the published vector set).
SHARE_HI = F(1, 2)     # primary band upper edge (inclusive): position share


def _to_fraction(x):
    """Accept int, float (exact repr), numeric string, or Fraction."""
    if isinstance(x, F):
        return x
    if isinstance(x, int):
        return F(x)
    if isinstance(x, float):
        return F(str(x))
    return F(str(x))


def caliber(slots, center, space_hi):
    """Recompute slot-space caliber readings from raw slot observations.

    slots:    list of ints (the raw per-call slot observations).
    center:   the center the reported statistic used (int/str fraction).
    space_hi: the declared slot-space upper edge (inclusive; e.g. 127).

    Returns a dict with exact-Fraction readings, or None on empty input.
    Raises ValueError on malformed slots (non-integer slot).
    """
    if not slots:
        return None
    clean = []
    for x in slots:
        if isinstance(x, bool) or not isinstance(x, int):
            raise ValueError("slot must be an int: %r" % (x,))
        clean.append(x)
    n = len(clean)
    c = _to_fraction(center)
    hi = int(space_hi)
    mean = F(sum(clean), n)
    var_true = sum((F(x) - mean) ** 2 for x in clean) / n
    pos = (mean - c) ** 2
    moment = var_true + pos
    share = F(0) if moment == 0 else pos / moment
    uni = F((hi + 1) ** 2 - 1, 12)
    return {
        "n": n,
        "mean": mean,
        "center": c,
        "var_true": var_true,
        "pos_term": pos,
        "moment": moment,
        "share": share,
        "ratio_true": var_true / uni,
        "ratio_defective": moment / uni,
        "uniform_var": uni,
        "in_space": all(0 <= x <= hi for x in clean),
    }


def adjudicate(cal):
    """Two-band adjudication over a caliber reading (cal from caliber()).

    Primary band (the only adjudicating band):
      F1 center-caliber: share <= SHARE_HI (inclusive);
      F2 space-membership: all slots inside [0, space_hi].
    Reference band (never adjudicates): ratio_true / ratio_defective.
    """
    if cal is None:
        return {
            "verdict": "INCONCLUSIVE",
            "primary_band": {"measure": "share", "value": None,
                             "line": "%s (inclusive)" % SHARE_HI},
            "reference_band": [],
        }
    share = cal["share"]
    f1 = share <= SHARE_HI              # boundary inclusive (exact fractions)
    f2 = cal["in_space"]
    verdict = "VALID" if (f1 and f2) else "INVALID"
    return {
        "verdict": verdict,
        "primary_band": {
            "F1_center_caliber": {"measure": "share", "value": share,
                                  "line": "%s (inclusive)" % SHARE_HI,
                                  "passed": f1},
            "F2_space_membership": {"passed": f2},
        },
        "reference_band": [
            {"measure": "ratio_true", "value": cal["ratio_true"],
             "adjudicates": False},
            {"measure": "ratio_defective", "value": cal["ratio_defective"],
             "adjudicates": False},
        ],
    }


def run_gate(verbose=True):
    with open(VECTORS_PATH, "r", encoding="utf-8") as f:
        vectors = json.load(f)
    G = {}

    # F1 published D1 anchor: the {0..11} enumeration against a hardcoded
    #    cross-line center 63.5 — position term 99.6% -> INVALID, and the
    #    recomputed true values match the registered correction exactly.
    v = vectors["d1_r1_enumeration"]
    cal = caliber(v["slots"], v["center"], v["space_hi"])
    r1 = adjudicate(cal)
    G["F1 D1 anchor {0..11} c=63.5 -> INVALID (position term dominates)"] = (
        r1["verdict"] == "INVALID"
        and r1["primary_band"]["F1_center_caliber"]["value"] == F(40368, 40511)
        and cal["var_true"] == F(143, 12)
        and cal["moment"] == F(40511, 12)
        and cal["ratio_true"] == F(143, 16383)
        and cal["ratio_defective"] == F(40511, 16383))

    # F1b published rounding faces: moment 3375.9 at 1dp, defective ratio
    #     2.473 at 3dp, true ratio 0.008729 at 6dp (correction file values).
    G["F1b D1 anchor rounding faces match the registered correction"] = (
        round(float(cal["moment"]), 1) == 3375.9
        and round(float(cal["ratio_defective"]), 3) == 2.473
        and round(float(cal["ratio_true"]), 6) == 0.008729)

    # F2 published f8j anchor: same center 63.5 over a genuinely 0..127
    #    spread (sample mean 64.25) -> VALID; caliber appropriate in the
    #    original line context (the correction's own cross-check).
    v = vectors["f8j_v73frozen_call04"]
    cal2 = caliber(v["slots"], v["center"], v["space_hi"])
    r2 = adjudicate(cal2)
    G["F2 f8j anchor 0..127 spread c=63.5 -> VALID (share 27/44764)"] = (
        r2["verdict"] == "VALID"
        and r2["primary_band"]["F1_center_caliber"]["value"] == F(27, 44764)
        and cal2["var_true"] == F(44737, 48)
        and cal2["mean"] == F(257, 4))

    # F3 boundary exactness: share == 1/2 exactly -> VALID (inclusive edge);
    #     a same-magnitude offset above -> INVALID. Exact fractions only.
    v = vectors["boundary_share_half"]
    r3a = adjudicate(caliber(v["slots"], v["center"], v["space_hi"]))
    v = vectors["just_over_half"]
    r3b = adjudicate(caliber(v["slots"], v["center"], v["space_hi"]))
    G["F3 boundary inclusive exact / just-over kill"] = (
        r3a["verdict"] == "VALID"
        and r3a["primary_band"]["F1_center_caliber"]["value"] == F(1, 2)
        and r3b["verdict"] == "INVALID"
        and r3b["primary_band"]["F1_center_caliber"]["value"] == F(9, 13))

    # F4 space-membership kill: a slot outside the declared space -> INVALID
    #     even when the center caliber itself is fine.
    v = vectors["out_of_space_member"]
    r4 = adjudicate(caliber(v["slots"], v["center"], v["space_hi"]))
    G["F4 out-of-space member killed by membership band"] = (
        r4["verdict"] == "INVALID"
        and r4["primary_band"]["F2_space_membership"]["passed"] is False
        and r4["primary_band"]["F1_center_caliber"]["passed"] is True)

    # F5 empty observations -> INCONCLUSIVE (never a silent pass).
    r5 = adjudicate(caliber([], "63.5", 127))
    G["F5 empty observations INCONCLUSIVE"] = r5["verdict"] == "INCONCLUSIVE"

    # F6 at-center degenerate: single observation at the center ->
    #     moment 0, share := 0 -> VALID (no offset, no dispersion info).
    r6 = adjudicate(caliber([63], 63, 127))
    G["F6 at-center degenerate share:=0 VALID"] = (
        r6["verdict"] == "VALID"
        and r6["primary_band"]["F1_center_caliber"]["value"] == 0)

    # F7 malformed slot -> fail loud (ValueError), not silently skipped.
    try:
        caliber(["x"], "63.5", 127)
        G["F7 malformed slot fails loud"] = False
    except ValueError:
        G["F7 malformed slot fails loud"] = True

    # F8 reference band never adjudicates: the defective ratio is reported
    #     side-by-side on the INVALID anchor (direction-flip evidence).
    G["F8 reference band reports defective ratio without adjudicating"] = (
        all(ref["adjudicates"] is False for ref in r1["reference_band"])
        and any(ref["measure"] == "ratio_defective"
                for ref in r1["reference_band"]))

    ok_all = all(v is True for v in G.values())
    if verbose:
        for k, v in G.items():
            print(("PASS" if v is True else "FAIL"), k)
        print("slot_space_caliber gate: %s (%d/%d)" % (
            "ALL PASS" if ok_all else "FAILED",
            sum(1 for v in G.values() if v is True), len(G)))
    return ok_all, G


if __name__ == "__main__":
    sys.exit(0 if run_gate()[0] else 1)
