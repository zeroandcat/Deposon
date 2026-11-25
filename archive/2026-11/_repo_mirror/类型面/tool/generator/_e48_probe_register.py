# -*- coding: utf-8 -*-
"""E-48 只读探测：改判总表并发写状态 + #1/#4 采纳面。一次性快照。"""
import hashlib
import io
import os
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

p = r_dep_path("results/_v3_recheck_verdict_register_2026_09_27.md")
d = open(p, "rb").read()
print("NOW sha12=", hashlib.sha256(d).hexdigest()[:12], "bytes=", len(d), "mtime=", os.path.getmtime(p))
t = d.decode("utf-8")
L = t.split("\n")
print("lines=", len(L))
pat = re.compile(r"(2026-09-28|采纳|双判|ask_90f108da8b781eece9c90088|ask_[0-9a-f]{24})")
n = 0
for i, ln in enumerate(L):
    if pat.search(ln):
        n += 1
        if n <= 40:
            print(i + 1, "|", ln.strip()[:180])
print("total_hits=", n)
print("--- last 6 lines ---")
for ln in L[-6:]:
    print("   ", ln[:180])
