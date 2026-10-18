# -*- coding: utf-8 -*-
"""Reconcile the state of the two probe files after the mid-verify crash."""
import os, sys, io, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recycle_exec import bin_dir_for, list_bin, decode_i

REPO = r"_repo_mirror"
PROBE = r".tmp\h_mq20.py"
abs_p = os.path.join(REPO, PROBE)
bindir = bin_dir_for(abs_p)

print("bindir        :", bindir)
print("still on disk :", os.path.exists(abs_p))
entries = sorted(list_bin(bindir))
print("bin entries   :", entries)

# find the $I record whose decoded path is our probe
# NB: match case-insensitively -- the stored path keeps its original drive-letter case.
want = abs_p
low = raw_needle = None
for n in entries:
    if not n.startswith("$I"):
        continue
    p = os.path.join(bindir, n)
    try:
        dec, raw = decode_i(p)
    except Exception as e:
        print("  %s decode error %r" % (n, e)); continue
    raw_needle = want.encode("utf-16-le")
    low = want.lower().encode("utf-16-le")
    off = raw.find(raw_needle)
    how = "exact"
    if off < 0:
        off = raw.lower().find(low)
        how = "case-insensitive"
    if off >= 0:
        r = n.replace("$I", "$R", 1)
        rp = os.path.join(bindir, r)
        print("\nMATCH %s (%s) -> $I path at byte offset %d" % (n, how, off))
        print("  $I bytes      :", dec["bytes"])
        print("  $I version    :", dec.get("version"))
        print("  $I file_size  :", dec.get("file_size"))
        print("  path decoded  :", raw[off:off + len(raw_needle)].decode("utf-16-le", "replace"))
        print("  pair $R       :", r, "exists=", os.path.exists(rp))
        if os.path.exists(rp):
            print("  $R bytes      :", os.path.getsize(rp))
            with open(rp, "rb") as f:
                head = f.read(64)
            print("  $R first64    :", head[:64])
        else:
            print("  $R MISSING -> would be a PERMANENT delete")
