# -*- coding: utf-8 -*-
"""Debug: locate the $I record for one specific deleted file."""
import os, io, sys
sys.path.insert(0, r"〔目录引用·未上传:cleanup511〕")
from recycle_exec import bin_dir_for, list_bin

REPO = r"_repo_mirror"
b = bin_dir_for(os.path.join(REPO, "x"))
target = os.path.join(REPO, ".tmp", "_t3probe_peek.py")
print("target:", target)
print("exists:", os.path.exists(target))
print("abspath == target:", os.path.abspath(target) == target)

ents = sorted(list_bin(b))
I = [e for e in ents if e.startswith("$I")]
print("scanning %d $I records ..." % len(I))

for enc, label in ((target.encode("utf-16-le"), "utf16le"),
                   (target.encode("utf-16-le").lower(), "utf16le-lowered"),
                   (target.encode("utf-8", "replace"), "utf8")):
    found = []
    for n in I:
        with io.open(os.path.join(b, n), "rb") as f:
            raw = f.read()
        hay = raw.lower()
        off = hay.find(enc if label != "utf16le-lowered" else enc.lower())
        if off >= 0:
            found.append((n, off))
    print("  %-18s -> %s" % (label, found[:3] if found else "NO MATCH"))

# what does one $I actually contain?
n0 = I[0]
with io.open(os.path.join(b, n0), "rb") as f:
    raw = f.read()
txt = raw.decode("utf-16-le", "replace")
print("\nsample %s bytes=%d" % (n0, len(raw)))
print("  hex[24:40] =", " ".join("%02x" % x for x in raw[24:40]))
print("  decoded    =", repr(txt[:90]))
