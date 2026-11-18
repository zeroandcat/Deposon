#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# judgment_v11.py — pre-registered judgment-line interfaces (v1.1 caliber).
# ----------------------------------------------------------------------------
# Three plugin-faced interfaces, pure arithmetic over declared vectors:
#   A. Measure-locator discrimination ("gauge gate"):
#      every judgment must declare the granularity its measure was computed
#      at; the registry pins the pre-registered locator, and the gate
#      recomputes the value at the declared unit. A flattened-unit mis-read
#      (tokens treated as keys) changes both numerator and denominator
#      non-uniformly and is rejected before it can reach a verdict.
#   B. Raw-full logging obligation:
#      every response record — accepted, gate-rejected, and parse-failed
#      alike — must carry the verbatim response text (raw_full), of which
#      raw_head is a prefix. Head-only logging makes failure positions
#      unrecomputable; the obligation check fails loud per record.
#   C. Three-band adjudication:
#      (1) primary band — the only adjudicating band (pre-registered kill
#          line, boundary inclusive);
#      (2) reference band — reported side-by-side, never adjudicates;
#      (3) annotation band — thresholded flags, never adjudicates.
#      A missing primary measure yields INCONCLUSIVE (degenerate segments
#      carry zero-contrast information and need mechanism-position evidence).
#
# Dual implementation: gates/judgment_v11.lean machine-checks the structural
# theorems (lean 4.15.0 core-only, 0 sorry); this module is the executable
# face. Zero network, zero credentials, zero external data: vectors live in
# mocks/judgment_v11_vectors.json.
#
# Usage:
#   python3 gates/judgment_v11.py            # gate runner (exit 0 = ALL PASS)
#   python3 -c "import ..."                  # library face (see tests/)
# ============================================================================
import json
import os
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
VECTORS_PATH = os.path.join(ROOT, "mocks", "judgment_v11_vectors.json")

# ---------------------------------------------------------------------------
# A. Measure-locator registry (gauge gate)
# ---------------------------------------------------------------------------
# Each measure id pins its pre-registered locator: the unit the measure is
# defined on. Judgments must match the locator AND recompute exactly.
MEASURE_REGISTRY = {
    "coupling_selection": {
        "granularity": "key",
        "unit": "per-common-key",
        "recompute": lambda v: F(v["hits"], v["population"]),
    },
}


def check_measure_locator(judgment):
    """Validate one judgment against the measure-locator registry.

    judgment: {"measure_id": str, "granularity": str,
               "value": Fraction, "vectors": {"hits": int, "population": int}}
    Returns (ok: bool, detail: str).
    """
    mid = judgment.get("measure_id")
    if mid not in MEASURE_REGISTRY:
        return False, "unknown measure_id: %r (not in registry)" % (mid,)
    loc = MEASURE_REGISTRY[mid]
    if judgment.get("granularity") != loc["granularity"]:
        return False, (
            "granularity mismatch: measure %r is registered at %r, "
            "judgment declares %r — flattened-unit mis-reads change "
            "numerator and denominator non-uniformly and cannot be "
            "adjudicated" % (mid, loc["granularity"], judgment.get("granularity"))
        )
    try:
        recomputed = loc["recompute"](judgment["vectors"])
        declared = F(judgment["value"])
    except Exception as e:  # fail loud on malformed vectors
        return False, "malformed judgment: %s" % (e,)
    if recomputed != declared:
        return False, (
            "recompute mismatch: declared %s, recomputed %s at registered "
            "granularity %r" % (declared, recomputed, loc["granularity"])
        )
    return True, "locator + recompute exact at %r" % (loc["granularity"],)


# ---------------------------------------------------------------------------
# B. Raw-full logging obligation
# ---------------------------------------------------------------------------
DISPOSITIONS = ("accepted", "gate_rejected", "parse_fail")


def check_raw_full_obligation(manifest, records):
    """Validate the raw-full obligation over a readings record set.

    manifest: {"raw_full_obligation": {disp: bool for disp in DISPOSITIONS}}
    records:  list of {"disposition": str, "raw_head": str, "raw_full": str}
    Returns (ok: bool, detail: str). Fail-loud: the FIRST violation is named
    per record index; obligation scope must cover all three dispositions.
    """
    declared = (manifest or {}).get("raw_full_obligation") or {}
    for disp in DISPOSITIONS:
        if not declared.get(disp):
            return False, "obligation scope incomplete: %r not covered" % (disp,)
    if not records:
        return False, "empty record set: nothing to check (fail loud)"
    for i, rec in enumerate(records):
        disp = rec.get("disposition")
        if disp not in DISPOSITIONS:
            return False, "record %d: unknown disposition %r" % (i, disp)
        head, full = rec.get("raw_head") or "", rec.get("raw_full") or ""
        if not full:
            return False, (
                "record %d (%s): raw_full empty — head-only logging makes "
                "the failure position unrecomputable" % (i, disp)
            )
        if len(full) < len(head) or full[: len(head)] != head:
            return False, "record %d (%s): raw_head is not a prefix of raw_full" % (i, disp)
    return True, "raw_full present and head-consistent across %d records" % (len(records),)


# ---------------------------------------------------------------------------
# C. Three-band adjudication
# ---------------------------------------------------------------------------

def adjudicate(prereg, readings):
    """Adjudicate one judgment line under the three-band semantics.

    prereg:   {"primary": {"measure_id": str, "direction": "ge"|"le",
                           "kill_line": Fraction},
               "annotations": [{"id": str, "threshold": Fraction}]}
    readings: {"measures": {measure_id: Fraction | None},
               "annotations": {id: Fraction},
               "references": {label: Fraction}}

    Returns a three-band result dict. Only the primary band adjudicates;
    reference values and annotation triggers are reported side-by-side and
    never change the verdict (machine-checked in judgment_v11.lean, T1).
    """
    prim = prereg["primary"]
    mid, direction = prim["measure_id"], prim["direction"]
    kill = F(prim["kill_line"])
    if direction not in ("ge", "le"):
        raise ValueError("direction must be 'ge' or 'le'")
    value = (readings.get("measures") or {}).get(mid)
    if value is None:
        verdict, primary_band = "INCONCLUSIVE", {
            "measure_id": mid, "value": None, "kill_line": kill,
            "direction": direction,
            "note": "primary measure missing — degenerate segment carries "
                    "zero-contrast information; mechanism-position evidence "
                    "required, no adjudication",
        }
    else:
        value = F(value)
        crossed = (value >= kill) if direction == "ge" else (value <= kill)
        verdict = "KILL" if crossed else "PASS"
        primary_band = {"measure_id": mid, "value": value,
                        "kill_line": kill, "direction": direction,
                        "boundary_inclusive": True}
    reference_band = [
        {"label": label, "value": F(v), "adjudicates": False}
        for label, v in sorted((readings.get("references") or {}).items())
    ]
    annotation_band = []
    for ann in prereg.get("annotations") or []:
        av = (readings.get("annotations") or {}).get(ann["id"])
        if av is None:
            continue
        av = F(av)
        annotation_band.append({
            "id": ann["id"], "value": av, "threshold": F(ann["threshold"]),
            "triggered": abs(av) >= F(ann["threshold"]),
            "adjudicates": False,
        })
    return {"verdict": verdict, "primary_band": primary_band,
            "reference_band": reference_band, "annotation_band": annotation_band}


# ---------------------------------------------------------------------------
# Gate runner (vectors from mocks/judgment_v11_vectors.json)
# ---------------------------------------------------------------------------

def run_gate(vectors=None, verbose=True):
    if vectors is None:
        vectors = json.load(open(VECTORS_PATH, encoding="utf-8"))
    G = {}

    # --- A. gauge gate: registered locator accepts, flattened mis-read rejects,
    #        wrong value at the registered unit rejects
    ga = vectors["gauge_gate"]
    ok, detail = check_measure_locator(ga["valid_keylevel"])
    G["A1 locator+recompute accepts"] = ok
    ok, detail = check_measure_locator(ga["flattened_misread"])
    G["A2 flattened mis-read rejected"] = (not ok) and "granularity mismatch" in detail
    ok, detail = check_measure_locator(ga["wrong_value"])
    G["A3 wrong value rejected"] = (not ok) and "recompute mismatch" in detail
    ok, detail = check_measure_locator(ga["unknown_measure"])
    G["A4 unknown measure rejected"] = (not ok) and "unknown measure_id" in detail

    # --- B. raw-full obligation: full coverage passes; head-only record fails
    #        loud with its index; incomplete scope fails; bad prefix fails
    gb = vectors["raw_full_obligation"]
    ok, detail = check_raw_full_obligation(gb["manifest_full"], gb["records_full"])
    G["B1 full-coverage records pass"] = ok
    ok, detail = check_raw_full_obligation(gb["manifest_full"], gb["records_headonly"])
    G["B2 head-only record fails loud"] = (not ok) and "raw_full empty" in detail and "record 1" in detail
    ok, detail = check_raw_full_obligation(gb["manifest_partial"], gb["records_full"])
    G["B3 partial scope rejected"] = (not ok) and "not covered" in detail
    ok, detail = check_raw_full_obligation(gb["manifest_full"], gb["records_badprefix"])
    G["B4 non-prefix head rejected"] = (not ok) and "not a prefix" in detail

    # --- C. three-band: verdict from the primary band alone; both flip
    #        directions of the flattened mis-read would cross the boundary if
    #        the gauge gate did not reject them first; missing primary is
    #        INCONCLUSIVE; annotations flag but never adjudicate
    gc = vectors["three_band"]
    pre = gc["prereg"]
    r1 = adjudicate(pre, gc["reading_keylevel_pass"])
    G["C1 primary PASS"] = r1["verdict"] == "PASS"
    r2 = adjudicate(pre, gc["reading_keylevel_kill"])
    G["C2 primary KILL (inclusive boundary exactness)"] = r2["verdict"] == "KILL"
    r3 = adjudicate(pre, gc["reading_missing"])
    G["C3 missing primary INCONCLUSIVE"] = r3["verdict"] == "INCONCLUSIVE" and r3["primary_band"]["value"] is None
    r4 = adjudicate(pre, gc["reading_keylevel_pass_with_loud_refs"])
    G["C4 references never adjudicate"] = (
        r4["verdict"] == "PASS"
        and all(ref["adjudicates"] is False for ref in r4["reference_band"])
        and len(r4["reference_band"]) == len(gc["reading_keylevel_pass_with_loud_refs"]["references"])
    )
    r5 = adjudicate(pre, gc["reading_keylevel_pass_with_ann"])
    G["C5 annotation flags but never adjudicates"] = (
        r5["verdict"] == "PASS"
        and any(a["triggered"] for a in r5["annotation_band"])
        and all(a["adjudicates"] is False for a in r5["annotation_band"])
    )
    # the flattened mis-read values would flip both directions at this
    # boundary — the gauge gate (part A) is what keeps them out
    flip_up = adjudicate(pre, gc["reading_flattened_would_kill"])
    flip_down = adjudicate(pre, gc["reading_flattened_would_pass"])
    G["C6 mis-read would flip verdicts both ways (gauge gate guards)"] = (
        flip_up["verdict"] == "KILL" and flip_down["verdict"] == "PASS"
    )

    ok_all = all(v is True for v in G.values())
    if verbose:
        for k, v in G.items():
            print(("PASS" if v is True else "FAIL"), k)
        print("judgment_v11 gate: %s (%d/%d)" % (
            "ALL PASS" if ok_all else "FAILED",
            sum(1 for v in G.values() if v is True), len(G)))
    return ok_all, G


if __name__ == "__main__":
    sys.exit(0 if run_gate()[0] else 1)
