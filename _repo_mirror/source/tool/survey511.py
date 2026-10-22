# -*- coding: utf-8 -*-
"""
CLEANUP-EXEC-511 :: four-channel inbound-reference re-test over the .tmp deletion surface.
v2 - performance-corrected. Read-only: writes ONE manifest json, deletes nothing.

Channel reduction (proved, not assumed):
  every Channel-A form (abs path, rel path with / or \, ".tmp/<name>", ".tmp\\<name>")
  CONTAINS the bare filename as a substring.  =>  hit(A) => hit(B-name).
  So A is *derived* from the B-name hit set instead of being searched separately.

Channels:
  A path reference  : a path form of the file occurs in a non-.tmp repo file
  B bare-name ref   : the bare filename (with ext) occurs, or the stem occurs (len>=3)
  C dynamic load    : a glob/dynamic-enumeration construct in the corpus resolves to the file
  D hash/BOM pinning: the file's sha256 (prefix len 12/16/20/32/64) occurs as a hex token

Absolute exclusions (block regardless of channels):
  R2 trajectory data plane : *measurement* *llm_calls* *records* three_seed* *_detail*
  R3 same-day 2026-10-17   : mtime calendar date
  RX sub-zone collision    : same repo-relative path (with the ".tmp/" staging
                             prefix stripped) exists under 〔本地绝对路径·脱敏略:�〕�人资料\\deposon-sub
"""
import os, re, io, json, time, fnmatch, hashlib
from bisect import bisect_right
from collections import defaultdict

REPO  = r"_repo_mirror"
TMP   = os.path.join(REPO, ".tmp")
SUB   = r"_repo_mirror"
SELF  = os.path.join(REPO, ".mavis", "scripts", "cleanup511")
OUT   = os.path.join(TMP, "cleanup511_manifest_2026_10_17.json")
TODAY = "2026-10-17"
STEM_MIN = 3

TRAJ = ("*measurement*", "*llm_calls*", "*records*", "three_seed*", "*_detail*")
HEX = re.compile(rb"[0-9a-fA-F]{12,64}")
DYN_TOKENS = ("glob(", "rglob(", "iterdir(", "os.listdir", "os.walk", "scandir",
              "importlib", "spec_from_file_location", "module_from_spec",
              "exec(", "runpy", "os.remove", "shutil.rmtree", "unlink(")


def sha256_of(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def rel(p):
    return os.path.relpath(p, REPO).replace("\\", "/")


def corpus_files():
    out = []
    for dp, dns, fns in os.walk(REPO, followlinks=False):
        dn = os.path.normcase(dp)
        if dn == os.path.normcase(TMP) or dn.startswith(os.path.normcase(TMP) + os.sep):
            dns[:] = []
            continue
        if dn == os.path.normcase(SELF) or dn.startswith(os.path.normcase(SELF) + os.sep):
            dns[:] = []
            continue
        for fn in fns:
            p = os.path.join(dp, fn)
            if os.path.isfile(p):
                out.append(p)
    return out


def main():
    t0 = time.time()
    warnings = []

    cfiles = corpus_files()
    bodies, hex_tokens = [], set()
    dyn_lines, dyn_pats = [], []
    for p in cfiles:
        try:
            with open(p, "rb") as f:
                raw = f.read()
        except OSError as e:
            warnings.append("READ_FAIL %s %r" % (rel(p), e))
            continue
        low = raw.lower()
        bodies.append((p, low))
        for m in HEX.finditer(low):
            hex_tokens.add(m.group(0))
        txt = raw.decode("utf-8", "replace")
        for line in txt.splitlines():
            ll = line.lower()
            if ".tmp" not in ll:
                continue
            if any(t in ll for t in DYN_TOKENS):
                dyn_lines.append((rel(p), ll.strip()[:400]))
            for m in re.finditer(r"[\"'][^\"']*\.tmp[^\"']*[\"']", ll):
                dyn_pats.append((rel(p), m.group(0).strip("'\"")))

    # ---------- candidates ----------
    cands, walk_errs = [], []
    def _onerr(e):
        walk_errs.append(repr(e))
    for dp, dns, fns in os.walk(TMP, followlinks=False, onerror=_onerr):
        for fn in fns:
            p = os.path.join(dp, fn)
            try:
                st = os.stat(p)
            except OSError as e:
                walk_errs.append(repr(e))
                continue
            cands.append({
                "abs": p, "rel": rel(p), "name": fn,
                "stem": os.path.splitext(fn)[0],
                "bytes": st.st_size, "mtime": st.st_mtime,
                "mdate": time.strftime("%Y-%m-%d", time.localtime(st.st_mtime)),
            })
    cands.sort(key=lambda c: c["rel"])

    # ---------- sub-zone collision set ----------
    sub_rels = set()
    if os.path.isdir(SUB):
        for dp, dns, fns in os.walk(SUB, followlinks=False):
            for fn in fns:
                try:
                    sub_rels.add(os.path.relpath(os.path.join(dp, fn), SUB).replace("\\", "/").lower())
                except ValueError:
                    pass
    sub_names = {s.rsplit("/", 1)[-1] for s in sub_rels}   # RX name-collision face

    # ---------- build the needle set (unique) ----------
    needle_files = {}          # needle -> list of corpus paths containing it
    needles = set()
    for c in cands:
        needles.add(c["name"].lower().encode("utf-8", "replace"))
        if len(c["stem"]) >= STEM_MIN:
            needles.add(c["stem"].lower().encode("utf-8", "replace"))
    needles = sorted(needles)
    for nd in needles:
        hits = [p for p, b in bodies if nd in b]
        if hits:
            needle_files[nd] = hits

    # ---------- per-candidate verdict ----------
    for c in cands:
        name_l = c["name"].lower().encode("utf-8", "replace")
        stem_l = c["stem"].lower().encode("utf-8", "replace")
        use_stem = len(c["stem"]) >= STEM_MIN
        relwin = c["rel"].replace("/", "\\").lower()
        relposix = c["rel"].lower()
        absl = c["abs"].lower()

        n_hits = [rel(p) for p in needle_files.get(name_l, [])]
        s_hits = [rel(p) for p in needle_files.get(stem_l, [])] if use_stem else []

        # A derived from B-name hits (proof: each A form is a superstring of the name)
        a_hits = []
        if n_hits:
            nset = set(n_hits)
            for src in nset:
                body = dict(bodies).get(os.path.join(REPO, src.replace("/", os.sep)))
                if body is None:
                    continue
                forms = [f for f, tok in (("abs", absl.encode()), ("relwin", relwin.encode()),
                                          ("relposix", relposix.encode()),
                                          ("dot_tmp_win", (".tmp\\" + c["name"].lower()).encode()),
                                          ("dot_tmp_posix", (".tmp/" + c["name"].lower()).encode()))
                         if tok in body]
                if forms:
                    a_hits.append({"src": src, "forms": forms})

        # C dynamic load
        c_hits = []
        for src, pat in dyn_pats:
            pp = pat.lstrip("./")
            if pp in (relposix, relwin) or pp.endswith("/" + c["name"].lower()) or pp.endswith("\\" + c["name"].lower()):
                c_hits.append({"kind": "pattern", "src": src, "pat": pat})
        nb = name_l
        for src, line in dyn_lines:
            if nb in line.encode("utf-8", "replace"):
                c_hits.append({"kind": "dynline", "src": src, "line": line})

        # D hash pinning
        c["sha256"] = sha256_of(c["abs"])
        c["sha12"] = c["sha256"][:12]
        dpins = [n for n in (12, 16, 20, 32, 64) if c["sha256"][:n].encode() in hex_tokens]
        d_hits = [{"prefix_len": sorted(dpins)}] if dpins else []

        c["chan_n"] = {"A": len(a_hits), "B": len(n_hits) + len(s_hits),
                       "C": len(c_hits), "D": len(d_hits)}
        c["chan"] = {"A": a_hits[:8], "B": {"name": n_hits[:8], "stem": s_hits[:8]}, "C": c_hits[:8], "D": d_hits}
        c["stem_searched"] = use_stem

        excl = []
        if any(fnmatch.fnmatch(c["name"].lower(), pat) for pat in TRAJ):
            excl.append("R2_trajectory")
        if c["mdate"] == TODAY:
            excl.append("R3_sameday")
        rx_rel = c["rel"].lower()
        if rx_rel.startswith(".tmp/"):
            rx_rel = rx_rel[len(".tmp/"):]   # .tmp/ is a staging prefix, not part of the path
        if sub_rels and (rx_rel in sub_rels or c["name"].lower() in sub_names):
            excl.append("RX_sub_collision")
        c["excl"] = excl
        c["blocked_channels"] = [k for k in "ABCD" if c["chan_n"][k] > 0]
        c["clearable"] = (not excl) and (not c["blocked_channels"])

    clean = [c for c in cands if c["clearable"]]
    held = [c for c in cands if not c["clearable"]]

    def daycount(rows):
        d = defaultdict(int)
        for r in rows:
            d[r["mdate"]] += 1
        return dict(sorted(d.items()))

    meta = {
        "rod": "CLEANUP-EXEC-511", "worker": "worker",
        "generated": time.strftime("%Y-%m-%d %H:%M:%S"),
        "corpus_files": len(bodies),
        "corpus_bytes": sum(len(b) for _, b in bodies),
        "corpus_read_failures": warnings,
        "tmp_walk_errors": walk_errs,
        "candidates_total": len(cands),
        "clean_count": len(clean),
        "held_count": len(held),
        "clean_bytes": sum(c["bytes"] for c in clean),
        "clean_day_layers": daycount(clean),
        "held_day_layers": daycount(held),
        "stem_search_min_len": STEM_MIN,
        "cands_with_stem_skipped": sum(1 for c in cands if not c["stem_searched"]),
        "held_chan_tally": {k: sum(1 for c in held if c["chan_n"][k]) for k in "ABCD"},
        "clean_chan_tally": {k: sum(1 for c in clean if c["chan_n"][k]) for k in "ABCD"},
        "excl_tally": {k: sum(1 for c in held if k in c["excl"])
                       for k in ("R2_trajectory", "R3_sameday", "RX_sub_collision")},
        "excl_only_no_channel": sum(1 for c in held if not c["blocked_channels"]),
        "sub_exists": os.path.isdir(SUB), "sub_rels_n": len(sub_rels),
        "needles_searched": len(needles),
        "dyn_pattern_count": len(dyn_pats), "dyn_line_count": len(dyn_lines),
        "hex_token_count": len(hex_tokens),
        "elapsed_s": round(time.time() - t0, 2),
    }
    manifest = {"meta": meta,
                "clean": [{k: c[k] for k in ("rel", "name", "bytes", "mdate", "sha12", "sha256", "abs")} for c in clean],
                "held": [{k: c[k] for k in ("rel", "name", "bytes", "mdate", "sha12", "excl",
                                            "blocked_channels", "chan_n", "chan", "abs")} for c in held],
                "dyn_lines": dyn_lines[:400], "dyn_pats": dyn_pats[:400]}
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(manifest, ensure_ascii=False, indent=1))
    print(json.dumps(meta, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
