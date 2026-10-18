# -*- coding: utf-8 -*-
"""Audit the four-channel manifest: is Channel D (hash pinning) producing false positives?"""
import io, json, re
from collections import Counter

P = r"_repo_mirror\.tmp\cleanup511_manifest_2026_10_17.json"
m = json.load(io.open(P, encoding="utf-8"))

held = m["held"]
print("meta.clean=%s held=%s" % (m["meta"]["clean_count"], m["meta"]["held_count"]))

# Which channels are the SOLE reason a 10-13..10-16 file is held?
win = [h for h in held if "2026-10-13" <= h["mdate"] <= "2026-10-16" and "R3_sameday" not in h["excl"]]
print("\nheld within 10-13..10-16 (excl sameday):", len(win))
print("blocked-channel combination tally:")
for combo, n in Counter(tuple(h["blocked_channels"]) for h in win).most_common():
    print("   %-14s %d" % (",".join(combo) or "(none/excl only)", n))

# Channel D deep-dive
d_only = [h for h in win if h["blocked_channels"] == ["D"]]
print("\nD-sole blockers:", len(d_only))
for h in d_only[:12]:
    print("   %-58s %s  prefixes=%s" % (h["rel"][:58], h["sha12"], h["chan"]["D"]))

# Is D matching digit-timestamps rather than real hashes?
allhex = set()
for h in held:
    for d in h["chan"]["D"]:
        allhex.update(range(0))
digit_like = 0
for h in d_only:
    pref = h["chan"]["D"][0]["prefix_len"]
    for n in pref:
        pass
    if h["sha12"].isdigit():
        digit_like += 1
print("\nD-sole blockers whose sha12 is ALL-DIGITS (timestamp-artifact risk):", digit_like, "/", len(d_only))

# What does the clean set look like?
clean = m["clean"]
print("\nclean n=%d bytes=%d" % (len(clean), sum(c["bytes"] for c in clean)))
z = [c for c in clean if c["bytes"] == 0]
print("zero-byte clean files:", len(z))
for c in z[:15]:
    print("   %-60s %s  %s" % (c["rel"][:60], c["mdate"], c["sha12"]))
print("\nclean extension mix:")
for e, n in Counter(("".join(os.path.splitext(c["name"])[1:]) or "(none)") for c in clean).most_common(12):
    print("   %-10s %d" % (e, n))
print("\nlargest clean files:")
for c in sorted(clean, key=lambda x: -x["bytes"])[:10]:
    print("   %10d  %s" % (c["bytes"], c["rel"]))
