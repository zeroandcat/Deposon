# -*- coding: utf-8 -*-
"""Verify the 3 recycled empty dirs. NB: build the bindir via bin_dir_for() --
os.path.join("D:", x) yields a DRIVE-RELATIVE path and silently resolves to nothing."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recycle_exec import bin_dir_for, list_bin

REPO = r"D:\私人资料\deposon-repo"
DIRS = [r".tmp\numaudit_20261013", r"results\_archive_2026_09_20", r"results\_archive_2026_09_21"]

bindir = bin_dir_for(os.path.join(REPO, "x"))
print("bindir       :", bindir)
print("is_absolute  :", os.path.isabs(bindir), " exists:", os.path.isdir(bindir))
ents = sorted(list_bin(bindir))
Is = sorted(e for e in ents if e.startswith("$I"))
Rs = sorted(e for e in ents if e.startswith("$R"))
print("entries=%d  $I=%d  $R=%d  suffix-paired=%s"
      % (len(ents), len(Is), len(Rs), [x[2:] for x in Is] == [x[2:] for x in Rs]))

for d in DIRS:
    full = os.path.join(REPO, d)
    print("\n=== %s ===" % d)
    print("  still on disk :", os.path.exists(full))
    found = []
    for n in Is:
        p = os.path.join(bindir, n)
        try:
            with open(p, "rb") as f:
                raw = f.read()
        except OSError as e:
            print("  %s unreadable: %r" % (n, e)); continue
        off = raw.lower().find(full.lower().encode("utf-16-le"))
        if off >= 0:
            r = n.replace("$I", "$R", 1)
            rp = os.path.join(bindir, r)
            found.append((n, r, off, os.path.exists(rp)))
    if not found:
        print("  NO $I record decodes to this path")
    for n, r, off, rex in found:
        print("  $I=%s  $R=%s  path_at_byte_offset=%d  $R_exists=%s  $R_is_dir=%s"
              % (n, r, off, rex, os.path.isdir(os.path.join(bindir, r))))
