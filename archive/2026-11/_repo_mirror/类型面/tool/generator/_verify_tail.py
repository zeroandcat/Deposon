# -*- coding: utf-8 -*-
import sys, os

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

F = _dep_path("/docs//V3X//TRAE_V3_ASSET_ERRATUM_2026_09_23.md")
size = os.path.getsize(F)
with open(F, 'rb') as fh:
    raw = fh.read()

# output last ~500 bytes as escaped (avoid console GBK)
tail = raw[-700:]
sys.stdout.buffer.write(b"--- tail bytes (escaped hex bytes for last 700) ---\n")
sys.stdout.buffer.write(tail.hex().encode('ascii'))
sys.stdout.buffer.write(b"\n--- end ---\n")
sys.stdout.buffer.write(("total bytes=" + str(size)).encode())
sys.stdout.buffer.write(b"\n")
# also write a decoded tail to a temp file for viewing
out = _dep_path("/.tmp//_v16_tail_dump.txt")
with open(out, 'wb') as fout:
    fout.write(raw)
print('wrote', out)
