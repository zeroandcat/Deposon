# -*- coding: utf-8 -*-
"""Audit 3: exact scope of the D-artifact fix + the out-of-.tmp carve-outs (rule 4/5)."""
import io, os, json, hashlib

REPO = r"D:\私人资料\deposon-repo"
P = os.path.join(REPO, ".tmp", "cleanup511_manifest_2026_10_17.json")
m = json.load(io.open(P, encoding="utf-8"))
held, clean = m["held"], m["clean"]
EMPTY = hashlib.sha256(b"").hexdigest()

print("=== A. zero-byte candidates: held for what reason? ===")
for h in held:
    if h["bytes"] == 0:
        d_only = h["blocked_channels"] == ["D"]
        print("   %-58s ch=%-12s excl=%-22s D-EMPTY=%s D-ONLY=%s"
              % (h["rel"][:58], ",".join(h["blocked_channels"]) or "-",
                 ",".join(h["excl"]) or "-", h["sha12"] == EMPTY[:12], d_only))

print("\n=== B. the 4 clean .pyc + where the pycache dirs sit ===")
for c in clean:
    if c["rel"].lower().endswith(".pyc"):
        print("   %-58s %7d  %s" % (c["rel"], c["bytes"], c["mdate"]))
for d in (r".tmp\__pycache__", r".tmp\_pre_mod\__pycache__", r"results\__pycache__"):
    fp = os.path.join(REPO, d)
    if os.path.isdir(fp):
        fs = os.listdir(fp)
        print("   DIR %-34s files=%d %s" % (d, len(fs), fs))
    else:
        print("   DIR %-34s ABSENT" % d)

print("\n=== C. empty dirs (rule 5) ===")
for d in (r".tmp\numaudit_20261013", r"results\_archive_2026_09_20", r"results\_archive_2026_09_21"):
    fp = os.path.join(REPO, d)
    if os.path.isdir(fp):
        print("   %-34s entries=%d" % (d, len(os.listdir(fp))))

print("\n=== D. smallest clean .py files (probe candidates) ===")
cands = sorted([c for c in clean if c["name"].lower().endswith(".py")], key=lambda x: x["bytes"])
for c in cands[:10]:
    print("   %7d  %-52s %s" % (c["bytes"], c["rel"][:52], c["mdate"]))

print("\n=== E. projected clean count after D-artifact fix ===")
extra = [h for h in held if h["bytes"] == 0 and h["blocked_channels"] == ["D"] and h["sha12"] == EMPTY[:12]]
print("   zero-byte files held by D alone on the empty-hash :", len(extra))
print("   %d -> %d" % (len(clean), len(clean) + len(extra)))
for h in extra:
    print("      +", h["rel"], h["mdate"])
