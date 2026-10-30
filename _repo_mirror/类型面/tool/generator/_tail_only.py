# -*- coding: utf-8 -*-
import hashlib, os

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

text = raw.decode('utf-8')
out = _dep_path("/.tmp//_v16_tail_only.txt")
with open(out, 'w', encoding='utf-8') as fout:
    fout.write(text[-2200:])
print('wrote tail length 2200 to:', out)
print('file size:', size)
