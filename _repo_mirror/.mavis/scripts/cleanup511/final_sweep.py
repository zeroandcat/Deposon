# -*- coding: utf-8 -*-
"""Final integrity sweep before the register: prove scope, prove the protected sets survived."""
import os, io, json, sys, fnmatch, hashlib
from collections import Counter

REPO = r"D:\私人资料\deposon-repo"
TMP = os.path.join(REPO, ".tmp")
LST = os.path.join(REPO, ".mavis", "scripts", "cleanup511", "exec_list.json")
sys.path.insert(0, os.path.join(REPO, ".mavis", "scripts", "cleanup511"))
from recycle_exec import bin_dir_for, list_bin

L = json.load(io.open(LST, encoding="utf-8"))
targets = {os.path.normcase(f["abs"]) for f in L["files"]}
print("planned files:", len(targets))

# --- 1. os.walk with explicit traversal-error accounting (discipline: 三重自审) ---
errs = []
left = []
for dp, dns, fns in os.walk(TMP, followlinks=False, onerror=lambda e: errs.append(repr(e))):
    for fn in fns:
        p = os.path.join(dp, fn)
        left.append((os.path.normcase(p), os.path.getsize(p)))
print("os.walk traversal errors:", len(errs), errs[:3])
print("files remaining in .tmp:", len(left))
print("  of which planned-but-still-present:", sum(1 for p, _ in left if p in targets))
print("  unplanned remaining (held/protected):", sum(1 for p, _ in left if p not in targets))

# --- 2. protected sets must all still be on disk ---
prot = [f for f in L["files"] if not f["rel"].startswith(".tmp/")]
print("\nnon-.tmp targets (rule-4 pycache):", len(prot), "still present:",
      sum(1 for f in prot if os.path.exists(f["abs"])))

TRAJ = ("*measurement*", "*llm_calls*", "*records*", "three_seed*", "*_detail*")
traj = [p for p, _ in left if any(fnmatch.fnmatch(os.path.basename(p), t) for t in TRAJ)]
print("trajectory-data files still in .tmp (must be >0):", len(traj))

today = [p for p, _ in left if os.path.getmtime(p) >= 1758000000]
print("files in .tmp with a fresh mtime (kept):", len(today))

# --- 3. results/ / letters/ / docs/ untouched apart from the 2 pycache ---
for d in ("results", "letters", "docs"):
    n = sum(len(f) for _, _, f in os.walk(os.path.join(REPO, d)))
    print("  %-8s files now = %d" % (d, n))

# --- 4. recycle bin reconciliation ---
b = bin_dir_for(os.path.join(REPO, "x"))
ents = sorted(list_bin(b))
I = [e for e in ents if e.startswith("$I")]
R = [e for e in ents if e.startswith("$R")]
print("\nbin $I=%d $R=%d paired=%s (planned items=%d)"
      % (len(I), len(R), [x[2:] for x in I] == [x[2:] for x in R], len(L["files"]) + len(L["dirs"])))

# --- 5. spot-check payload integrity for 12 random targets via their $I path ---
import random
random.seed(20261017)
okc = badc = 0
sample = random.sample([f for f in L["files"] if f["sha12"] != "(empty-dir)"], 12)
for f in sample:
    needle = os.path.abspath(f["abs"]).lower().encode("utf-16-le")
    hit = None
    for n in I:
        try:
            raw = io.open(os.path.join(b, n), "rb").read()
        except OSError:
            continue
        off = raw.lower().find(needle)
        if off >= 0:
            hit = (n, off); break
    if not hit:
        print("  NO $I for", f["rel"]); badc += 1; continue
    rp = os.path.join(b, hit[0].replace("$I", "$R", 1))
    h = hashlib.sha256()
    with open(rp, "rb") as fh:
        for bb in iter(lambda: fh.read(1 << 20), b""):
            h.update(bb)
    same = h.hexdigest()[:12] == f["sha12"]
    okc += same; badc += (not same)
    print("  %-46s $I=%-16s off=%2d $R_sha12=%s match=%s"
          % (f["rel"][:46], hit[0], hit[1], h.hexdigest()[:12], same))
print("\nspot-check: %d matched, %d mismatched" % (okc, badc))
