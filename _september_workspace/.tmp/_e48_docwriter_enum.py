# -*- coding: utf-8 -*-
"""E-48 只读复算脚本 3：勘误链既有 E-编号全集清点（供 E-48「登记总数对齐」用）。"""
import collections
import io
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open(r"D:\私人资料\deposon-repo\docs\V3X\TRAE_V3_ASSET_ERRATUM_2026_09_23.md", encoding="utf-8").read()
L = t.split("\n")

base = set()
sub = collections.defaultdict(set)
for ln in L:
    for m in re.finditer(r"\bE-(\d{1,2})(\.(\d{1,2}))?\b", ln):
        n = int(m.group(1))
        if m.group(3):
            sub[n].add(m.group(3))
        else:
            base.add(n)

alln = sorted(base | set(sub))
print("base-level E numbers seen:", sorted(base))
print("sub-numbered E numbers seen:", {k: sorted(v) for k, v in sorted(sub.items())})
print()
print("ALL E numbers 1..max seen =", alln)
missing = [n for n in range(1, max(alln) + 1) if n not in alln]
print("MISSING in 1..%d =" % max(alln), missing)
print()
tot_sub = sum(len(v) for v in sub.values())
print("top-level numbered entries =", len(alln), " ; sub-entries =", tot_sub, " ; total =", len(alln) + tot_sub)
print()
print("E-44 mentions (raw grep):", [ln.strip()[:120] for ln in L if "E-44" in ln][:5])
