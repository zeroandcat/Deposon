#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# slot_space_crosscheck.py — dual-implementation cross-check of the slot-space
# caliber gate (interface F). preview.9 closes the "Lean mirror candidate"
# item left open by the preview.7/8 review.
# ----------------------------------------------------------------------------
# Lean side   : gates/slot_space_caliber.lean (lean 4.15.0 core-only, 0 sorry,
#               machine-checked locally; the axiom audit is transcribed in
#               docs/slot-space-caliber.md — CI carries no Lean toolchain).
# Python side : the integer mirror of the Lean definitions below, plus the
#               executable face gates/slot_space_caliber.py (fractions).
# What this script enforces in CI:
#   X0 source policy of the Lean file: 0 sorry, 0 import lines (prelude
#      only), no Mathlib, every theorem carries an axiom-audit line.
#   X1 every vector-theorem statement of the Lean file is re-verified by the
#      mirror in exact integer arithmetic (an unmirrored statement fails loud).
#   X2 the universally quantified theorems are spot-checked on deterministic
#      pseudo-random inputs (the proofs themselves live in Lean).
#   X3 the published mock vectors agree across mirror and executable face.
# Usage: python3 gates/slot_space_crosscheck.py   (exit 0 = ALL PASS)
# ============================================================================
import os
import re
import sys
import json
import random
import importlib.util
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LEAN_PATH = os.path.join(HERE, "slot_space_caliber.lean")
VECTORS_PATH = os.path.join(ROOT, "mocks", "slot_space_vectors.json")


# ----- integer mirror of the Lean definitions (same names, same order) -------
def sq(x):
    return x * x


def sumSq(L):
    return sum(sq(x) for x in L)


def sumL(L):
    return sum(L)


def shiftL(c, L):
    return [x - c for x in L]


def moment(L, c):
    return sumSq(shiftL(c, L))


def varNum(L):
    return len(L) * sumSq(L) - sq(sumL(L))


def posNum(L, c):
    return sq(sumL(L) - len(L) * c)


def scaleL(k, L):
    return [k * x for x in L]


def verdictF(hi, L, c):
    if not L:
        return "INCONCLUSIVE"
    if not all(0 <= x and x <= hi for x in L):
        return "INVALID"
    if 2 * posNum(L, c) <= len(L) * moment(L, c):
        return "VALID"
    return "INVALID"


# ----- X0 source policy -------------------------------------------------------
def strip_comments(src):
    """Remove Lean comments: nested block comments and `--` line comments."""
    out, i, n, depth = [], 0, len(src), 0
    while i < n:
        if src.startswith("/-", i):
            depth += 1
            i += 2
            continue
        if depth and src.startswith("-/", i):
            depth -= 1
            i += 2
            continue
        if depth:
            if src[i] == "\n":
                out.append("\n")
            i += 1
            continue
        if src.startswith("--", i):
            j = src.find("\n", i)
            if j < 0:
                break
            i = j
            continue
        out.append(src[i])
        i += 1
    assert depth == 0, "unterminated block comment"
    return "".join(out)


REQUIRED = [
    "moment_decomposition", "share_half_iff", "share_lt_half_iff",
    "boundary_half_holds", "just_over_half_kills", "degenerate_at_center",
    "share_band_scale_invariant", "membership_scale2_list",
    "out_of_space_kills", "verdict_in_space", "boundary_half_valid",
    "just_over_half_invalid", "verdict_scale2", "degenerate_valid",
    "verdict_empty",
]

# ----- X1 vector-theorem mirror ------------------------------------------------
A = r"(?:-?\d+|[A-Za-z_]\w*|\[[^\]]*\])"          # atom: number | name | list literal


def _atom(tok, env):
    if tok.startswith("["):
        return [int(t) for t in re.findall(r"-?\d+", tok)]
    if re.match(r"-?\d+$", tok):
        return int(tok)
    return env[tok]


def _lst(m, g):
    return [int(t) for t in re.findall(r"-?\d+", m.group(g))]


VECTOR_PATTERNS = [
    # scaleL 2 [..] = name   (doubled representation of a published anchor)
    (re.compile(r"scaleL 2 \[([^\]]*)\] = ([A-Za-z_]\w*)$"),
     lambda m, env: scaleL(2, _lst(m, 1)) == env[m.group(2)]),
    # a * posNum L c = b * (n * moment L c)      (share = a/b, cross-multiplied)
    (re.compile(r"(-?\d+) \* posNum (%s) (-?\d+) = (-?\d+) \* \((-?\d+) \* moment \2 \3\)$" % A),
     lambda m, env: int(m.group(1)) * posNum(_atom(m.group(2), env), int(m.group(3)))
     == int(m.group(4)) * (int(m.group(5)) * moment(_atom(m.group(2), env), int(m.group(3))))),
    # a * 2 * posNum L c > b * (n * moment L c)  (share strictly over 1/2)
    (re.compile(r"(-?\d+) \* 2 \* posNum (%s) (-?\d+) > (-?\d+) \* \((-?\d+) \* moment \2 \3\)$" % A),
     lambda m, env: int(m.group(1)) * 2 * posNum(_atom(m.group(2), env), int(m.group(3)))
     > int(m.group(4)) * (int(m.group(5)) * moment(_atom(m.group(2), env), int(m.group(3))))),
    (re.compile(r"posNum (%s) (-?\d+) = (-?\d+)$" % A),
     lambda m, env: posNum(_atom(m.group(1), env), int(m.group(2))) == int(m.group(3))),
    (re.compile(r"posNum (%s) (-?\d+) = varNum (%s)$" % (A, A)),
     lambda m, env: posNum(_atom(m.group(1), env), int(m.group(2))) == varNum(_atom(m.group(3), env))),
    (re.compile(r"posNum (%s) (-?\d+) = varNum (%s) \+ (-?\d+)$" % (A, A)),
     lambda m, env: posNum(_atom(m.group(1), env), int(m.group(2))) == varNum(_atom(m.group(3), env)) + int(m.group(4))),
    (re.compile(r"posNum (%s) (-?\d+) > varNum (%s)$" % (A, A)),
     lambda m, env: posNum(_atom(m.group(1), env), int(m.group(2))) > varNum(_atom(m.group(3), env))),
    (re.compile(r"varNum (%s) = (-?\d+)$" % A),
     lambda m, env: varNum(_atom(m.group(1), env)) == int(m.group(2))),
    (re.compile(r"moment (%s) (-?\d+) = (-?\d+)$" % A),
     lambda m, env: moment(_atom(m.group(1), env), int(m.group(2))) == int(m.group(3))),
    # verdictF hi L c = FVerdict.V
    (re.compile(r"verdictF (%s) (%s) (%s) = FVerdict\.(VALID|INVALID|INCONCLUSIVE)$" % (A, A, A)),
     lambda m, env: verdictF(_atom(m.group(1), env), _atom(m.group(2), env), _atom(m.group(3), env)) == m.group(4)),
    # verdictF (2*hi) (scaleL 2 L) (2*c) = verdictF hi L c
    (re.compile(r"verdictF (-?\d+) \(scaleL 2 (%s)\) \((-?\d+) \* (-?\d+)\) = verdictF (-?\d+) \2 (-?\d+)$" % A),
     lambda m, env: verdictF(int(m.group(1)), scaleL(2, _atom(m.group(2), env)), int(m.group(3)) * int(m.group(4)))
     == verdictF(int(m.group(5)), _atom(m.group(2), env), int(m.group(6)))),
    # not ([..] : List Int).all (fun x => 0 <= x && x <= hi)
    (re.compile("¬ \\(\\[([^\\]]*)\\] : List Int\\)\\.all \\(fun x => 0 ≤ x && x ≤ (-?\\d+)\\)$"),
     lambda m, env: not all(0 <= x and x <= int(m.group(2)) for x in _lst(m, 1))),
]


def mirror_vector_theorems(code):
    env = {}
    for name, body in re.findall(r"^def (\w+) : List Int := \[([^\]]*)\]", code, re.M):
        env[name] = [int(t) for t in re.findall(r"-?\d+", body)]
    i = code.index("def d1d :")
    j = code.index("#print axioms moment_decomposition")
    res = {}
    for line in code[i:j].splitlines():
        m = re.match(r"theorem\s+(\w+)\s*:\s*(.*?)\s*:=", line)
        if not m:
            continue
        name, stmt = m.group(1), m.group(2)
        hits = [p for p in VECTOR_PATTERNS if p[0].match(stmt)]
        if len(hits) != 1:
            res[name] = "UNMIRRORED" if not hits else "AMBIGUOUS"
            continue
        res[name] = bool(hits[0][1](hits[0][0].match(stmt), env))
    return res, env


# ----- X2 property spot-checks (one entry per universally quantified theorem) --
PROPERTIES = {
    "sumL_shiftL": lambda L, c, k: sumL(shiftL(c, L)) == sumL(L) - len(L) * c,
    "sumSq_shiftL": lambda L, c, k: sumSq(shiftL(c, L)) == sumSq(L) - 2 * c * sumL(L) + len(L) * sq(c),
    "moment_decomposition": lambda L, c, k: len(L) * moment(L, c) == varNum(L) + posNum(L, c),
    "share_half_iff": lambda L, c, k: (2 * posNum(L, c) <= len(L) * moment(L, c)) == (posNum(L, c) <= varNum(L)),
    "share_lt_half_iff": lambda L, c, k: (2 * posNum(L, c) < len(L) * moment(L, c)) == (posNum(L, c) < varNum(L)),
    "boundary_half_holds": lambda L, c, k: posNum(L, c) != varNum(L) or 2 * posNum(L, c) <= len(L) * moment(L, c),
    "just_over_half_kills": lambda L, c, k: not (varNum(L) < posNum(L, c)) or not (2 * posNum(L, c) <= len(L) * moment(L, c)),
    "degenerate_at_center": lambda L, c, k: moment(L, c) != 0 or (posNum(L, c) == 0 and varNum(L) == 0),
    "moment_scale": lambda L, c, k: moment(scaleL(k, L), k * c) == sq(k) * moment(L, c),
    "posNum_scale": lambda L, c, k: posNum(scaleL(k, L), k * c) == sq(k) * posNum(L, c),
    "len_scaleL": lambda L, c, k: len(scaleL(k, L)) == len(L),
    "share_band_scale_invariant": lambda L, c, k: k == 0 or (
        (2 * posNum(scaleL(k, L), k * c) <= len(L) * moment(scaleL(k, L), k * c))
        == (2 * posNum(L, c) <= len(L) * moment(L, c))),
    "membership_scale2_list": lambda L, c, k: all(0 <= 2 * x and 2 * x <= 2 * c for x in L) == all(0 <= x and x <= c for x in L),
    "verdict_empty": lambda L, c, k: bool(L) or verdictF(c, L, c) == "INCONCLUSIVE",
    "out_of_space_kills": lambda L, c, k: not L or all(0 <= x and x <= c for x in L) or verdictF(c, L, 0) == "INVALID",
    "verdict_in_space": lambda L, c, k: not L or not all(0 <= x and x <= c for x in L) or verdictF(c, L, 0) == (
        "VALID" if 2 * posNum(L, 0) <= len(L) * moment(L, 0) else "INVALID"),
    "boundary_half_valid": lambda L, c, k: not L or not all(0 <= x and x <= c for x in L) or posNum(L, 0) != varNum(L)
    or verdictF(c, L, 0) == "VALID",
    "just_over_half_invalid": lambda L, c, k: not L or not all(0 <= x and x <= c for x in L) or not (varNum(L) < posNum(L, 0))
    or verdictF(c, L, 0) == "INVALID",
    "verdict_scale2": lambda L, c, k: not L or verdictF(2 * c, scaleL(2, L), 2 * 0) == verdictF(c, L, 0),
    "degenerate_valid": lambda L, c, k: not L or not all(0 <= x and x <= c for x in L) or moment(L, 0) != 0
    or (verdictF(c, L, 0) == "VALID" and posNum(L, 0) == 0 and varNum(L) == 0),
}


def spot_check(n_cases=3000, seed=20261124):
    rng = random.Random(seed)
    bad = {name: 0 for name in PROPERTIES}
    ks = (-2, -1, 1, 2)
    for _ in range(n_cases):
        L = [rng.randint(-3, 9) for _ in range(rng.randint(0, 6))]
        c = rng.randint(-2, 9)
        k = rng.choice(ks)
        for name, pred in PROPERTIES.items():
            try:
                if not pred(L, c, k):
                    bad[name] += 1
            except Exception:  # a mirror crash is a failed spot-check
                bad[name] += 1
    return bad


# ----- X3 published vectors ----------------------------------------------------
def _load_executable_face():
    spec = importlib.util.spec_from_file_location(
        "slot_space_caliber", os.path.join(HERE, "slot_space_caliber.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _scale_for_center(center):
    cf = F(str(center))
    k = cf.denominator
    return k, int(cf * k)


def run_crosscheck(verbose=True):
    G = {}
    raw = open(LEAN_PATH, encoding="utf-8").read()
    code = strip_comments(raw)

    theorems = re.findall(r"^(?:theorem|lemma)\s+(\w+)", code, re.M)
    audited = re.findall(r"^#print axioms (\w+)", code, re.M)
    G["X0a 0 sorry (proof and body positions)"] = re.findall(r"\bsorry\b", code) == []
    G["X0b 0 import lines (prelude only) / no Mathlib"] = (
        re.findall(r"^\s*import\b", code, re.M) == [] and "Mathlib" not in code)
    G["X0c every theorem carries exactly one axiom-audit line"] = (
        len(audited) == len(theorems) and sorted(audited) == sorted(theorems))
    G["X0d required theorem names present"] = all(n in theorems for n in REQUIRED)
    G["X0e vector block lies after the published anchors / before the audit"] = (
        code.index("def d1d :") < code.index("#print axioms moment_decomposition"))

    res, env = mirror_vector_theorems(code)
    n_vec = len(res)
    bad_vec = {k: v for k, v in res.items() if v is not True}
    G["X1 every vector theorem re-verified by the mirror (%d statements)" % n_vec] = (
        n_vec >= 20 and not bad_vec)

    bad = spot_check()
    G["X2 universally quantified theorems spot-checked (%d theorems x 3000 cases)" % len(PROPERTIES)] = (
        not any(bad.values()))

    mod = _load_executable_face()
    vectors = json.load(open(VECTORS_PATH, encoding="utf-8"))
    agree, detail = True, []
    for key, v in vectors.items():
        if not isinstance(v, dict) or "slots" not in v:
            continue
        k, c2 = _scale_for_center(v["center"])
        L2 = scaleL(k, [int(x) for x in v["slots"]])
        mv = verdictF(int(v["space_hi"]) * k, L2, c2)
        cal = mod.caliber(v["slots"], v["center"], v["space_hi"])
        ev = mod.adjudicate(cal)["verdict"]
        ok = mv == ev == v["expect"]["verdict"]
        if ok and "share" in v["expect"]:
            share = F(posNum(L2, c2), len(L2) * moment(L2, c2))
            ok = share == F(str(v["expect"]["share"])) == cal["share"]
        if ok and k == 2:
            ok = F(varNum(L2), sq(k) * sq(len(L2))) == cal["var_true"]
        agree = agree and ok
        detail.append("%s:%s" % (key, "ok" if ok else "MISMATCH"))
    G["X3 published vectors agree across mirror and executable face (%d)" % len(detail)] = agree and len(detail) >= 4

    ok_all = all(v is True for v in G.values())
    if verbose:
        for k_, v_ in G.items():
            print(("PASS" if v_ is True else "FAIL"), k_)
        if bad_vec:
            print("  X1 detail:", bad_vec)
        if any(bad.values()):
            print("  X2 detail:", {k_: v_ for k_, v_ in bad.items() if v_})
        print("  X3 detail:", " ".join(detail))
        print("slot_space_crosscheck: %s (%d/%d)" % (
            "ALL PASS" if ok_all else "FAILED",
            sum(1 for v_ in G.values() if v_ is True), len(G)))
    return ok_all, G


if __name__ == "__main__":
    sys.exit(0 if run_crosscheck()[0] else 1)
