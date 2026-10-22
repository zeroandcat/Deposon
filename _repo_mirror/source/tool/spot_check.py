# -*- coding: utf-8 -*-
"""Payload integrity spot-check: for N sampled deleted files, prove the $R payload in the
recycle bin still hashes to the pre-delete SHA-12 recorded in exec_list.json."""
import os, io, json, sys, random, hashlib
sys.path.insert(0, r"〔目录引用·未上传:cleanup511〕")
from recycle_exec import bin_dir_for, list_bin

REPO = r"_repo_mirror"
L = json.load(io.open(os.path.join(REPO, ".mavis", "scripts", "cleanup511", "exec_list.json"), encoding="utf-8"))
b = bin_dir_for(os.path.join(REPO, "x"))
ents = sorted(list_bin(b))
I = [e for e in ents if e.startswith("$I")]

# read every $I once, build path -> $I map.
# NB: in UTF-16LE each ASCII char is followed by \x00, so search the DECODED text, not raw bytes.
import re
PATHRE = re.compile(r"[dD]:\\[^\x00]+")
index = {}
for n in I:
    with io.open(os.path.join(b, n), "rb") as f:
        raw = f.read()
    txt = raw.decode("utf-16-le", "replace")
    m = PATHRE.search(txt)
    if not m:
        continue
    index[m.group(0).lower()] = (n, m.start())

print("indexed %d / %d $I records" % (len(index), len(I)))

random.seed(20261017)
pool = [x for x in L["files"] if x["sha12"] and x["sha12"] != "(empty-dir)"]
sample = random.sample(pool, 15)
ok = bad = miss = 0
for x in sample:
    key = os.path.abspath(x["abs"]).lower().replace("/", "\\")
    hit = index.get(key)
    if not hit:
        print("  NO-I   %s" % x["rel"]); miss += 1; continue
    n, off = hit
    rp = os.path.join(b, n.replace("$I", "$R", 1))
    h = hashlib.sha256()
    with open(rp, "rb") as fh:
        for bb in iter(lambda: fh.read(1 << 20), b""):
            h.update(bb)
    got = h.hexdigest()[:12]
    same = got == x["sha12"]
    ok += same; bad += (not same)
    print("  %s %-44s $I=%-15s off=%2d  $R_sha12=%s  expect=%s"
          % ("OK  " if same else "DIFF", x["rel"][:44], n, off, got, x["sha12"]))

# full-coverage index reconciliation
matched = sum(1 for x in L["files"]
              if os.path.abspath(x["abs"]).lower().replace("/", "\\") in index)
print("\nfull reconciliation: %d / %d planned files have a $I record in the bin"
      % (matched, len(L["files"])))
print("spot-check: ok=%d diff=%d missing=%d" % (ok, bad, miss))
