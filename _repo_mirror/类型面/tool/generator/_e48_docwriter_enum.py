# -*- coding: utf-8 -*-
"""E-48 只读复算脚本 3：勘误链既有 E-编号全集清点（供 E-48「登记总数对齐」用）。"""
import collections
import io
import re
import sys

def _dep_path(rel=""):
    """按名搜索：先在仓内候选根按相对路径找，再按件名全树找；皆不中则回原样。"""
    import os as _os
    from pathlib import Path as _P
    base = _P(__file__).resolve()
    roots = []
    for _i in range(1, 8):
        try:
            roots.append(base.parents[_i])
        except IndexError:
            break
    rel = rel.replace("\\", "/").lstrip("/")
    for _c in roots:
        if rel:
            _p = _c / rel
            if _p.exists():
                return str(_p)
    _name = rel.split("/")[-1] if rel else ""
    if _name:
        for _c in roots:
            for _dp, _dn, _fn in _os.walk(str(_c)):
                if _name in _fn:
                    return _os.path.join(_dp, _name)
    return rel


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open(r_dep_path("docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md"), encoding="utf-8").read()
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
