# -*- coding: utf-8 -*-
"""Audit 2: locate the Channel-D artifact, profile B-only holds, and size the 511 delta."""
import io, os, json, hashlib
from collections import Counter

REPO = r"D:\私人资料\deposon-repo"
P = os.path.join(REPO, ".tmp", "cleanup511_manifest_2026_10_17.json")
m = json.load(io.open(P, encoding="utf-8"))
held, clean = m["held"], m["clean"]
EMPTY_SHA12 = hashlib.sha256(b"").hexdigest()[:12]

# ---- 1. where does the empty-string sha appear in the corpus? ----
print("=== 1. empty-string sha %s provenance ===" % EMPTY_SHA12)
tmpn = os.path.normcase(os.path.join(REPO, ".tmp"))
selfn = os.path.normcase(os.path.join(REPO, ".mavis", "scripts", "cleanup511"))
full = EMPTY_SHA12 + hashlib.sha256(b"").hexdigest()[12:]
for dp, dns, fns in os.walk(REPO, followlinks=False):
    dn = os.path.normcase(dp)
    if dn == tmpn or dn.startswith(tmpn + os.sep) or dn == selfn or dn.startswith(selfn + os.sep):
        dns[:] = []
        continue
    for fn in fns:
        p = os.path.join(dp, fn)
        try:
            with open(p, "rb") as f:
                b = f.read().lower()
        except OSError:
            continue
        i = b.find(EMPTY_SHA12.encode())
        if i >= 0:
            print("   HIT %s  full64=%s" % (os.path.relpath(p, REPO), full.encode() in b))
            ctx = b[max(0, i - 120):i + 60].decode("utf-8", "replace").replace("\n", " ")
            print("        ctx: ...%s..." % ctx)

# ---- 2. how many candidates are zero-byte (all carry that same sha12)? ----
zb = [h for h in held if h["bytes"] == 0] + [c for c in clean if c["bytes"] == 0]
print("\n=== 2. zero-byte candidates: %d (all share sha12 %s) ===" % (len(zb), EMPTY_SHA12))
print("   of which HELD:", sum(1 for h in held if h["bytes"] == 0))

# ---- 3. B-only holds inside the 10-13..10-16 window ----
win = [h for h in held if "2026-10-13" <= h["mdate"] <= "2026-10-16" and "R3_sameday" not in h["excl"]]
b_only = [h for h in win if h["blocked_channels"] == ["B"]]
print("\n=== 3. B-only holds in 10-13..10-16: %d ===" % len(b_only))
srcs = Counter()
for h in b_only:
    for s in h["chan"]["B"]["name"] + h["chan"]["B"]["stem"]:
        srcs[s] += 1
for s, n in srcs.most_common(15):
    print("   %-58s %d" % (s, n))
print("\n   sample B-only held files:")
for h in b_only[:10]:
    nm = h["chan"]["B"]["name"]
    sm = h["chan"]["B"]["stem"]
    print("   %-52s name_src=%s stem_src=%s" % (h["rel"][:52], nm[:1], sm[:1]))

# ---- 4. the 511 delta, per day ----
want = {"2026-10-13": 46, "2026-10-14": 120, "2026-10-15": 84, "2026-10-16": 261}
got = Counter(c["mdate"] for c in clean)
print("\n=== 4. delta vs the 511 rod (survey rod vs my four-channel measurement) ===")
print("   %-12s %6s %6s %6s" % ("day", "rod511", "mine", "delta"))
for d in sorted(want):
    print("   %-12s %6d %6d %+6d" % (d, want[d], got.get(d, 0), want[d] - got.get(d, 0)))
print("   %-12s %6d %6d %+6d" % ("TOTAL", sum(want.values()), sum(got.values()), sum(want.values()) - sum(got.values())))

# ---- 5. clean set profile ----
print("\n=== 5. clean set (%d files, %d bytes) ===" % (len(clean), sum(c["bytes"] for c in clean)))
print("   ext mix:", dict(Counter(os.path.splitext(c["name"])[1] or "(none)" for c in clean).most_common(10)))
print("   largest 8:")
for c in sorted(clean, key=lambda x: -x["bytes"])[:8]:
    print("      %9d  %s" % (c["bytes"], c["rel"]))
print("   clean by day:", dict(sorted(Counter(c["mdate"] for c in clean).items())))
