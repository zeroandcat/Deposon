#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# descrev_calibration.py — f3 calibration face of the describability
# attribution judge (preview.9; honors the promise made in the f3 row of
# docs/family-linkage.md: "calibration face for the solve-judge").
# ----------------------------------------------------------------------------
# The describability reverse-solve chains (N9 DR-1 / DR-2) report a main-1
# reading "LOO nearest-centroid attribution accuracy". This module re-expresses
# that judge as S/D calibration pairs and feeds them to the judge-strictness
# gauge (gates/judgment_strictness.py) — the same gauge every other judge of
# the line must pass. Zero network, zero credentials; published numbers live
# in mocks/descrev_calibration_vectors.json.
#
# Judge semantics (chain code, verbatim rule):
#   * valid classes  = classes with >= 2 discovered packages, "unknown" excluded
#   * probes         = packages with a stats vector whose class is valid
#   * per probe, one face per valid class whose centroid is computable
#     (>= 1 OTHER package of that class with a stats vector)
#   * the probe is attributed to the nearest centroid — a single label
#
# Calibration pair per (probe, face): class S if face == probe's own class
# else D; mark "same" iff the probe was attributed to that face, else
# "different". Single-label attribution => exactly one "same" mark per probe.
#
# Verdict vocabulary (never relaxes the pre-registered main-1 face, which is
# reported side by side):
#   FULL_CONTRAST -> strictness gauge verdict (PASS / KILL) over the pairs
#   ZERO_CONTRAST -> INCONCLUSIVE: some probe has no D face (no class other
#                    than its own has a computable centroid). An accuracy of
#                    1.0 over such probes carries no discrimination
#                    information; it is never reported as PASS.
# Usage: python3 gates/descrev_calibration.py   (exit 0 = ALL PASS)
# ============================================================================
import os
import re
import sys
import json
import importlib.util
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
VECTORS_PATH = os.path.join(ROOT, "mocks", "descrev_calibration_vectors.json")


def _load_strictness():
    spec = importlib.util.spec_from_file_location(
        "judgment_strictness", os.path.join(HERE, "judgment_strictness.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def valid_classes(pkgs):
    """Classes with >= 2 discovered packages; 'unknown' never valid."""
    counts = {}
    for p in pkgs:
        counts[p["cls"]] = counts.get(p["cls"], 0) + 1
    return {c for c, n in counts.items() if n >= 2 and c != "unknown"}


def computable_faces(pkgs):
    """probe id -> ordered list of (face class, centroid member count)."""
    valid = valid_classes(pkgs)
    faces = {}
    for p in pkgs:
        if not p["stats"] or p["cls"] not in valid:
            continue
        row = []
        for c in sorted(valid):
            members = [q for q in pkgs if q["cls"] == c and q["stats"] and q["id"] != p["id"]]
            row.append((c, len(members)))
        faces[p["id"]] = row
    return faces


def pairs_from_faces(faces, attributions):
    pairs = []
    for probe in sorted(faces):
        if probe not in attributions:
            raise ValueError("attribution missing for probe %r" % probe)
        own = None
        row = faces[probe]
        for c, n in row:
            if n == 0:
                continue                      # centroid not computable -> no face
            if attributions[probe] not in [cc for cc, nn in row if nn > 0]:
                raise ValueError("attribution %r is not a computable face of %r" % (attributions[probe], probe))
            # the probe's own class is the S face; every other face is a D face
            pairs.append({"probe": probe, "face": c,
                          "cls": "S" if c == _own_class(faces, probe, row, c) else "D",
                          "mark": "same" if attributions[probe] == c else "different"})
    return pairs


# The probe's own class is not stored in `faces`; carry it explicitly.
def _own_class(faces, probe, row, c):
    return faces["_own"][probe] if "_own" in faces else c


def build_pairs(pkgs, attributions):
    """Explicit S/D pair construction (the single source used by run_gate)."""
    valid = valid_classes(pkgs)
    by_id = {p["id"]: p for p in pkgs}
    faces = computable_faces(pkgs)
    pairs = []
    for probe in sorted(faces):
        if probe not in attributions:
            raise ValueError("attribution missing for probe %r" % probe)
        own = by_id[probe]["cls"]
        live = [c for c, n in faces[probe] if n > 0]
        if attributions[probe] not in live:
            raise ValueError("attribution %r is not a computable face of %r" % (attributions[probe], probe))
        for c in live:
            pairs.append({"probe": probe, "face": c,
                          "cls": "S" if c == own else "D",
                          "mark": "same" if attributions[probe] == c else "different"})
    return pairs, faces


def calibration_face(pkgs, attributions, main1=None):
    pairs, faces = build_pairs(pkgs, attributions)
    per_probe = [len([1 for c, n in row if n > 0]) for row in faces.values()]
    s_pairs = sum(1 for p in pairs if p["cls"] == "S")
    d_pairs = sum(1 for p in pairs if p["cls"] == "D")
    strict = _load_strictness()
    out = {"n_probes": len(faces), "faces_per_probe": per_probe,
           "s_pairs": s_pairs, "d_pairs": d_pairs,
           "pre_registered": main1}
    if d_pairs == 0:
        out.update({"verdict": "INCONCLUSIVE", "reason_code": "ZERO_CONTRAST",
                    "reason": "no D pair: every probe sees a computable centroid only for its own class "
                              "(other valid classes have no stats-bearing members) — attribution accuracy "
                              "carries no discrimination information",
                    "cal": strict.calibrate(pairs) if pairs else None, "adjudication": None})
        return out
    cal = strict.calibrate(pairs)
    adj = strict.adjudicate(cal)
    out.update({"verdict": adj["verdict"], "reason_code": "FULL_CONTRAST", "reason": "",
                "cal": cal, "adjudication": adj})
    return out


def _fr(x):
    return None if x is None else F(x)


def _bruteforce_pairs(pkgs, attributions):
    """Independent construction by nested enumeration (cross-check only)."""
    valid = valid_classes(pkgs)
    res = []
    for p in pkgs:
        if not p["stats"] or p["cls"] not in valid:
            continue
        for c in valid:
            n = 0
            for q in pkgs:
                if q is q_p(pkgs, p["id"]):
                    continue
                if q["cls"] == c and q["stats"]:
                    n += 1
            if n == 0:
                continue
            same = attributions[p["id"]] == c
            res.append((p["id"], c, "S" if c == p["cls"] else "D", "same" if same else "different"))
    return sorted(res)


def q_p(pkgs, pid):
    return next(x for x in pkgs if x["id"] == pid)


def run_gate(verbose=True):
    vectors = json.load(open(VECTORS_PATH, encoding="utf-8"))
    strict = _load_strictness()
    G = {}

    dr2 = vectors["dr2_published"]
    r1 = calibration_face(dr2["pkgs"], dr2["attributions"], main1={
        "main1_attribution_acc": dr2["main1_attribution_acc"], "main1_threshold": dr2["main1_threshold"],
        "main3_format_blind_acc": dr2["main3_format_blind_acc"], "main2_attr_stability": dr2["main2_attr_stability"]})
    e = dr2["expect"]
    G["C1 DR-2 published -> INCONCLUSIVE / ZERO_CONTRAST (faces 1 per probe, S=4, D=0)"] = (
        r1["verdict"] == e["verdict"] and r1["reason_code"] == e["reason_code"]
        and r1["faces_per_probe"] == e["faces_per_probe"] and r1["s_pairs"] == e["s_pairs"]
        and r1["d_pairs"] == e["d_pairs"] and r1["n_probes"] == e["n_probes"])
    G["C2 DR-2 calibration carries no D-marginal (lam undefined) and no adjudication"] = (
        r1["cal"] is not None and r1["cal"]["lam"] is None and r1["adjudication"] is None)
    G["C3 DR-2 pre-registered main-1 face reported side by side, never replaced"] = (
        r1["pre_registered"]["main1_attribution_acc"] >= r1["pre_registered"]["main1_threshold"]
        and r1["verdict"] == "INCONCLUSIVE")

    def face_of(key):
        v = vectors[key]
        return calibration_face(v["pkgs"], v["attributions"]), v

    r2, v2 = face_of("two_class_all_correct")
    G["C4 two-class full contrast, all correct -> PASS d=1 lam=0 sig=0"] = (
        r2["verdict"] == "PASS" and r2["cal"]["d"] == 1 and r2["cal"]["lam"] == 0 and r2["cal"]["sig"] == 0
        and r2["s_pairs"] == 5 and r2["d_pairs"] == 5)
    r3, v3 = face_of("two_class_two_misattributed")
    G["C5 two-class, two misattributed -> KILL d=3/5 lam=2/5 sig=2/5"] = (
        r3["verdict"] == "KILL" and r3["cal"]["d"] == F(3, 5) and r3["cal"]["lam"] == F(2, 5) and r3["cal"]["sig"] == F(2, 5))
    r3b, v3b = face_of("two_class_one_misattributed")
    G["C6 two-class, one misattributed -> PASS d=4/5 (= attribution accuracy when K=2)"] = (
        r3b["verdict"] == "PASS" and r3b["cal"]["d"] == F(4, 5) and r3b["cal"]["lam"] == F(1, 5) and r3b["cal"]["sig"] == F(1, 5))
    r4, v4 = face_of("three_class_one_misattributed")
    G["C7 three-class: d = 1 - 2(1-acc)/K (K=3, acc=5/6 -> d=8/9)"] = (
        r4["cal"]["d"] == F(8, 9) and r4["s_pairs"] == 6 and r4["d_pairs"] == 12
        and r4["cal"]["d"] == 1 - 2 * (1 - F(5, 6)) / 3)
    r5, v5 = face_of("single_class_with_stats")
    G["C8 single stats-bearing class -> INCONCLUSIVE / ZERO_CONTRAST"] = (
        r5["verdict"] == "INCONCLUSIVE" and r5["reason_code"] == "ZERO_CONTRAST" and r5["cal"]["lam"] is None)

    # C9 independent enumeration equals the builder for every vector
    agree = True
    for key in ("dr2_published", "two_class_all_correct", "two_class_one_misattributed",
                "two_class_two_misattributed", "three_class_one_misattributed", "single_class_with_stats"):
        v = vectors[key]
        built = build_pairs(v["pkgs"], v["attributions"])[0]
        bf = _bruteforce_pairs(v["pkgs"], v["attributions"])
        agree = agree and sorted((p["probe"], p["face"], p["cls"], p["mark"]) for p in built) == bf
    G["C9 builder == independent enumeration (6 vectors)"] = agree

    # C10 single-label invariant: exactly one "same" mark per probe
    single = True
    for key in ("dr2_published", "two_class_all_correct", "two_class_two_misattributed", "three_class_one_misattributed"):
        built = build_pairs(vectors[key]["pkgs"], vectors[key]["attributions"])[0]
        per = {}
        for p in built:
            if p["mark"] == "same":
                per[p["probe"]] = per.get(p["probe"], 0) + 1
        single = single and all(n == 1 for n in per.values()) and len(per) == len({p["probe"] for p in built})
    G["C10 single-label invariant: exactly one 'same' mark per probe"] = single

    # C11 fail-loud on an attribution that is not a computable face
    try:
        build_pairs(v2["pkgs"], dict(v2["attributions"], a0="Z"))
        loud = False
    except ValueError:
        loud = True
    G["C11 malformed attribution fails loud"] = loud

    ok_all = all(v is True for v in G.values())
    if verbose:
        for k, v in G.items():
            print(("PASS" if v is True else "FAIL"), k)
        print("DR-2 calibration face:", r1["verdict"], r1["reason_code"], "| faces/probe", r1["faces_per_probe"],
              "| S/D", r1["s_pairs"], r1["d_pairs"], "| main-1 (pre-registered) acc", dr2["main1_attribution_acc"], ">=", dr2["main1_threshold"])
        print("descrev_calibration gate: %s (%d/%d)" % ("ALL PASS" if ok_all else "FAILED",
                                                         sum(1 for v in G.values() if v is True), len(G)))
    return ok_all, G


if __name__ == "__main__":
    sys.exit(0 if run_gate()[0] else 1)
