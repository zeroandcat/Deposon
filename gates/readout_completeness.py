#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# readout_completeness.py — readings-package completeness validator
# (preview.9 interface G). Scores a readings package against the eight
# required contents of docs/readings-package-spec.md:
#   1 MANIFEST (per-file sha256_12 + mtime; zero post-delivery modifications)
#   2 frozen criteria copy     3 frozen tool copy (tool_sha)
#   4 blind / frozen faces (frozen_sha)
#   5 per-round logs           6 per-op (key-level) ledger
#   7 readout JSON             8 recompute script (+ identity check)
# Principles enforced mechanically:
#   * "If a number cannot be recomputed from the package, it is not a reading."
#   * a missing key-level ledger makes key-level gates UNDECIDABLE — it is
#     never silently passed (item 6 is reported separately from the score);
#   * fail-loud: any FAIL/MISSING yields PARTIAL with reasons.
# Zero network, zero credentials. `python gates/readout_completeness.py` with no
# arguments runs the self-test (fixtures are built deterministically in a
# temporary directory; expected outcomes live in
# mocks/readout_completeness_vectors.json).
# ----------------------------------------------------------------------------
import fnmatch
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# default role patterns; a MANIFEST "roles" map (role -> [filenames]) overrides
DEFAULT_PATTERNS = {
    "manifest": ["MANIFEST.json", "manifest.json"],
    "criteria": ["*criteria*", "*判据*", "*prereg*", "*gate_text*", "*gate-text*"],
    "tool": ["*.sh", "*launch*.py", "*fire*.py", "*tool*.py", "*driver*.py", "*harness*.py"],
    "faces": ["*face*", "*frozen*", "*blind*"],
    "logs": ["*.log", "*progress*", "*events*", "*status*", "*trace*"],
    "ops_ledger": ["*ops*", "*op_ledger*", "*ledger*"],
    "readout": ["*readout*", "*results*", "*summary*", "*verdict*"],
    "recompute": ["*recompute*", "*recalc*", "*cmp*.py", "*readout*.py"],
}
KEY_FIELDS = ("key", "slot", "k", "key_id", "slot_id")


def sha12(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()[:12]


def _files(pkg):
    out = []
    for dp, dn, fn in os.walk(pkg):
        dn[:] = [d for d in dn if d not in ("__pycache__", ".git")]
        for f in fn:
            out.append(os.path.relpath(os.path.join(dp, f), pkg))
    return sorted(out)


def _match(files, patterns):
    pats = [p for p in patterns]
    return [f for f in files if any(fnmatch.fnmatch(os.path.basename(f), p) or fnmatch.fnmatch(f, p) for p in pats)]


def _resolve(role, files, roles):
    if roles and role in roles:
        return [f for f in roles[role] if f in files], [f for f in roles[role] if f not in files]
    return _match(files, DEFAULT_PATTERNS[role]), []


def _json_rows(path):
    rows = []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if line:
            try:
                rows.append(json.loads(line))
            except ValueError:
                rows.append(None)
    return rows


def _has_numeric_leaf(o):
    if isinstance(o, bool):
        return False
    if isinstance(o, (int, float)):
        return True
    if isinstance(o, dict):
        return any(_has_numeric_leaf(v) for v in o.values())
    if isinstance(o, list):
        return any(_has_numeric_leaf(v) for v in o)
    return False


def score_package(pkg, run_recompute=False, timeout=60):
    """Return {'items': {1..8: {...}}, 'score': n, 'verdict': ..., 'key_level': ..., 'reasons': [...]}."""
    pkg = os.path.abspath(pkg)
    res = {"package": pkg, "items": {}, "reasons": []}
    if not os.path.isdir(pkg):
        return {"package": pkg, "items": {}, "score": 0, "verdict": "PARTIAL", "key_level": "UNDECIDABLE",
                "reasons": ["package directory not found"]}
    files = _files(pkg)
    roles, manifest, man_sha, man_mtime = {}, None, None, None
    # ---- 1 MANIFEST --------------------------------------------------------
    mfiles, _ = _resolve("manifest", files, roles)
    it = {"status": "MISSING", "detail": "MANIFEST.json not found (machine check requires JSON)"}
    listed = {}
    if mfiles:
        mp = os.path.join(pkg, mfiles[0])
        try:
            manifest = json.load(open(mp, encoding="utf-8"))
            raw = manifest.get("files")
            if isinstance(raw, dict):
                listed = {k: (v if isinstance(v, dict) else {"sha256_12": v}) for k, v in raw.items()}
            elif isinstance(raw, list):
                listed = {e["name"]: e for e in raw if isinstance(e, dict) and "name" in e}
            roles = manifest.get("roles") or {}
            problems = []
            if not listed:
                problems.append("manifest lists no files")
            for name, ent in listed.items():
                s = str(ent.get("sha256_12") or ent.get("sha12") or "")
                fp = os.path.join(pkg, name)
                if len(s) != 12 or any(c not in "0123456789abcdef" for c in s):
                    problems.append(f"{name}: sha256_12 malformed")
                elif not os.path.isfile(fp):
                    problems.append(f"{name}: listed but missing")
                elif sha12(fp) != s:
                    problems.append(f"{name}: sha256_12 mismatch (post-delivery modification)")
                elif "mtime" in ent and ent["mtime"] and os.path.getmtime(fp) > os.path.getmtime(mp) + 2:
                    problems.append(f"{name}: mtime after MANIFEST (post-delivery modification)")
            unlisted = [f for f in files if f not in listed and f != mfiles[0]]
            man_sha, man_mtime = sha12(mp), os.path.getmtime(mp)
            it = {"status": "PASS" if not problems else "FAIL", "detail": problems or f"{len(listed)} files sha+mtime verified",
                  "manifest_sha12": man_sha, "n_listed": len(listed), "unlisted": unlisted}
        except Exception as e:  # fail-loud on any malformed manifest
            it = {"status": "FAIL", "detail": f"MANIFEST malformed: {type(e).__name__}: {e}"}
    res["items"][1] = it
    # ---- 2..5, 7, 8 --------------------------------------------------------
    def simple(n, role, extra=None):
        hits, declared_missing = _resolve(role, files, roles)
        nonempty = [h for h in hits if os.path.getsize(os.path.join(pkg, h)) > 0]
        r = {"status": "PASS" if nonempty else "MISSING", "detail": f"files={nonempty}" if nonempty else f"no {role} file"}
        if declared_missing:
            r["status"] = "FAIL"; r["detail"] = f"roles declare missing files {declared_missing}"
        if extra and nonempty:
            r.update(extra(nonempty))
        return r
    res["items"][2] = simple(2, "criteria")
    def _anchored(field):
        def f(hits):
            declared = manifest.get(field) if isinstance(manifest, dict) else None
            in_listed = [h for h in hits if h in listed]
            if declared and any(str(listed[h].get("sha256_12") or listed[h].get("sha12") or "") == str(declared) for h in in_listed):
                return {"status": "PASS", "anchor": field, "detail": f"files={hits}; {field}={declared} matches MANIFEST"}
            if in_listed:
                return {"status": "PASS", "anchor": field, "detail": f"files={in_listed} listed in MANIFEST"}
            return {"status": "FAIL", "detail": f"files={hits} but none carries a recorded {field}/MANIFEST entry"}
        return f
    res["items"][3] = simple(3, "tool", _anchored("tool_sha"))
    res["items"][4] = simple(4, "faces", _anchored("frozen_sha"))
    res["items"][5] = simple(5, "logs")
    # ---- 6 per-op (key-level) ledger ---------------------------------------
    hits, declared_missing = _resolve("ops_ledger", files, roles)
    ok_rows, key_field = 0, None
    for h in hits:
        if h.endswith(".jsonl"):
            rows = _json_rows(os.path.join(pkg, h))
            for r in rows:
                if isinstance(r, dict):
                    ok_rows += 1
                    kf = next((k for k in KEY_FIELDS if k in r), None)
                    if kf:
                        key_field = kf
    if ok_rows and key_field:
        it6 = {"status": "PASS", "detail": f"files={hits}; rows={ok_rows}; key field='{key_field}'"}
    elif ok_rows:
        it6 = {"status": "FAIL", "detail": f"files={hits}; rows={ok_rows} but no key-level field {KEY_FIELDS}"}
    else:
        it6 = {"status": "MISSING", "detail": f"no per-op ledger ({hits})"}
    if declared_missing:
        it6 = {"status": "FAIL", "detail": f"roles declare missing files {declared_missing}"}
    res["items"][6] = it6
    # ---- 7 readout JSON ----------------------------------------------------
    hits, declared_missing = _resolve("readout", files, roles)
    good = []
    for h in hits:
        if h.endswith(".json"):
            try:
                o = json.load(open(os.path.join(pkg, h), encoding="utf-8"))
                if isinstance(o, dict) and _has_numeric_leaf(o):
                    good.append(h)
            except Exception:
                pass
    it7 = {"status": "PASS" if good else "MISSING", "detail": f"files={good}" if good else f"no parseable readout JSON with numeric aggregates ({hits})"}
    if declared_missing:
        it7 = {"status": "FAIL", "detail": f"roles declare missing files {declared_missing}"}
    res["items"][7] = it7
    # ---- 8 recompute script (+ identity check) -----------------------------
    hits, declared_missing = _resolve("recompute", files, roles)
    pys = [h for h in hits if h.endswith(".py")]
    if declared_missing:
        it8 = {"status": "FAIL", "detail": f"roles declare missing files {declared_missing}"}
    elif not pys:
        it8 = {"status": "MISSING", "detail": f"no recompute script ({hits})"}
    elif not run_recompute:
        it8 = {"status": "UNVERIFIED", "detail": f"files={pys}; identity check not run (pass --run-recompute)"}
    else:
        fails = []
        for h in pys:
            try:
                p = subprocess.run([sys.executable, h, "--selfcheck"], cwd=pkg, capture_output=True, text=True, timeout=timeout)
                if p.returncode != 0 or "IDENTITY-OK" not in p.stdout:
                    fails.append(f"{h}: rc={p.returncode} identity check failed ({(p.stdout + p.stderr).strip()[-160:]})")
            except Exception as e:
                fails.append(f"{h}: {type(e).__name__}: {e}")
        it8 = {"status": "PASS" if not fails else "FAIL", "detail": f"files={pys}; identity IDENTITY-OK" if not fails else fails}
    res["items"][8] = it8
    # ---- verdict -----------------------------------------------------------
    n_pass = sum(1 for i in range(1, 9) if res["items"][i]["status"] == "PASS")
    unver = [i for i in range(1, 9) if res["items"][i]["status"] == "UNVERIFIED"]
    res["score"] = n_pass
    res["reasons"] = [f"item {i} {res['items'][i]['status']}: {res['items'][i]['detail']}" for i in range(1, 9) if res["items"][i]["status"] not in ("PASS", "UNVERIFIED")]
    res["key_level"] = "DECIDABLE" if res["items"][6]["status"] == "PASS" else "UNDECIDABLE"
    res["verdict"] = "PARTIAL" if res["reasons"] else ("COMPLETE-UNVERIFIED" if unver else "COMPLETE")
    return res


# ---------------------------------------------------------------------------
# self-test fixtures
# ---------------------------------------------------------------------------
RECOMPUTE = r'''#!/usr/bin/env python3
# recompute.py — regenerates headline numbers from the raw per-op ledger and
# checks them against readout.json (identity check). --selfcheck prints
# IDENTITY-OK / IDENTITY-FAIL and exits 0 / 1.
import json, os, sys
here = os.path.dirname(os.path.abspath(__file__))
rows = [json.loads(l) for l in open(os.path.join(here, "ops_ledger.jsonl")) if l.strip()]
n = len(rows); flips = sum(r["flips"] for r in rows)
ro = json.load(open(os.path.join(here, "readout.json")))
ok = ro["headline"]["n_ops"] == n and ro["headline"]["corr_flips_total"] == flips
if "--selfcheck" in sys.argv:
    print("IDENTITY-OK" if ok else "IDENTITY-FAIL", n, flips); sys.exit(0 if ok else 1)
json.dump({"n_ops": n, "corr_flips_total": flips}, open(os.path.join(here, "readout_recomputed.json"), "w"))
'''


def _write(pkg, name, text, mtime=None):
    p = os.path.join(pkg, name)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(text)
    if mtime is not None:
        os.utime(p, (mtime, mtime))


def build_fixture(root, name, mutate=None, roles_override=False):
    pkg = os.path.join(root, name)
    os.makedirs(pkg)
    base = time.time() - 1000
    _write(pkg, "criteria_frozen.md", "# frozen gate text\nline: BAcc >= 0.70\n", base)
    _write(pkg, "launcher_frozen.sh", "#!/bin/bash\necho launcher copy\n", base + 1)
    _write(pkg, "face_blind.json", json.dumps({"face": [1, 0, 1]}), base + 2)
    _write(pkg, "launch.log", "LAUNCH-START\nLAUNCH-DONE\n", base + 3)
    _write(pkg, "progress.jsonl", json.dumps({"step": 1, "loss": 0.9}) + "\n" + json.dumps({"step": 2, "loss": 0.8}) + "\n", base + 4)
    _write(pkg, "ops_ledger.jsonl", "".join(json.dumps({"key": k, "op": "write", "flips": k}) + "\n" for k in range(5)), base + 5)
    _write(pkg, "readout.json", json.dumps({"headline": {"n_ops": 5, "corr_flips_total": 10}, "segments": {"a": 1}}), base + 6)
    _write(pkg, "recompute.py", RECOMPUTE, base + 7)
    if mutate:
        mutate(pkg)
    files = {f: {"sha256_12": sha12(os.path.join(pkg, f)), "mtime": os.path.getmtime(os.path.join(pkg, f))} for f in _files(pkg)}
    man = {"package": name, "tool_sha": files["launcher_frozen.sh"]["sha256_12"], "frozen_sha": files["face_blind.json"]["sha256_12"], "files": files}
    if roles_override:
        man["roles"] = {"recompute": ["recompute.py"], "ops_ledger": ["ops_ledger.jsonl"]}
    _write(pkg, "MANIFEST.json", json.dumps(man, indent=1), base + 8)  # manifest written last
    if mutate:
        mutate(pkg, late=True)
    return pkg


def run_gate(verbose=True):
    ok_all = True
    vec = json.load(open(os.path.join(ROOT, "mocks", "readout_completeness_vectors.json"), encoding="utf-8"))
    with tempfile.TemporaryDirectory() as tmp:
        def _m_touch(pkg, late=False):
            if late:
                _write(pkg, "readout.json", json.dumps({"headline": {"n_ops": 5, "corr_flips_total": 10}, "segments": {"a": 1}}), time.time() + 50)
        def _m_sha(pkg, late=False):
            if late:
                _write(pkg, "launch.log", "LAUNCH-START\nLAUNCH-DONE\nTAMPERED\n")
        def _m_noops(pkg, late=False):
            if not late:
                os.remove(os.path.join(pkg, "ops_ledger.jsonl"))
        def _m_norec(pkg, late=False):
            if not late:
                os.remove(os.path.join(pkg, "recompute.py"))
        def _m_tamper(pkg, late=False):
            if late:
                _write(pkg, "ops_ledger.jsonl", "".join(json.dumps({"key": k, "op": "write", "flips": k + 1}) + "\n" for k in range(5)))
        def _m_flattened(pkg, late=False):
            if not late:
                _write(pkg, "ops_ledger.jsonl", json.dumps({"evict_seq": [[1, 2, 3], [4, 5]], "token_sim": 0.32}) + "\n", time.time() - 1000)
        mut = {"touch": _m_touch, "sha": _m_sha, "noops": _m_noops, "norec": _m_norec, "tamper": _m_tamper, "flattened": _m_flattened}
        for case in vec["cases"]:
            pkg = build_fixture(tmp, case["name"], mut.get(case.get("mutate")), case.get("roles_override", False))
            r = score_package(pkg, run_recompute=True)
            got = {"score": r["score"], "verdict": r["verdict"], "key_level": r["key_level"], "failed_items": sorted(int(x.split()[1]) for x in r["reasons"])}
            exp = {k: case[k] for k in got}
            ok = got == exp
            ok_all &= ok
            if verbose:
                print(f"{'PASS' if ok else 'FAIL'} {case['name']}: {got}" + ("" if ok else f"  expected {exp}"))
    if verbose:
        print("readout_completeness gate: " + ("ALL PASS" if ok_all else "FAIL") + f" ({sum(1 for c in vec['cases'])} cases)")
    return ok_all, {"all_pass": ok_all}


if __name__ == "__main__":
    _pos = [a for a in sys.argv[1:] if not a.startswith("-")]
    if _pos:  # package mode: JSON verdict only on stdout (self-test lines would break parsers)
        r = score_package(_pos[0], run_recompute="--run-recompute" in sys.argv)
        print(json.dumps(r, ensure_ascii=False, indent=1))
        sys.exit(0 if r["verdict"].startswith("COMPLETE") else 2)
    _ok, _ = run_gate(verbose=True)
    sys.exit(0 if _ok else 1)
