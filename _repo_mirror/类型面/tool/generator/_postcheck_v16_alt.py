# -*- coding: utf-8 -*-
import hashlib, os
F = _dep_path("/docs//V3X//TRAE_V3_ASSET_ERRATUM_2026_09_23.md")
size = os.path.getsize(F)
with open(F, 'rb') as fh:
    raw = fh.read()

# full sha12
full_sha256 = hashlib.sha256(raw).hexdigest().upper()
full_sha12 = full_sha256[:12]

# prefix SHA12 on first 158079 bytes (v15 末态)
prefix = raw[:158079]
prefix_sha256 = hashlib.sha256(prefix).hexdigest().upper()
prefix_sha12 = prefix_sha256[:12]

# also write decoded entire file to temp
import tempfile

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

out = _dep_path("/.tmp//_v16_full_decoded.txt")
with open(out, 'wb') as fout:
    fout.write(raw)

# Now open the decoded file and report last 1500 bytes
with open(out, 'rb') as fin:
    allb = fin.read()

# strip BOM if present
if allb[:3] == b'\xef\xbb\xbf':
    print(f"BOM detected: {allb[:3].hex().upper()}")
    allb = allb[3:]
else:
    print(f"No BOM (starts: {allb[:3].hex().upper()})")

# count lines in decoded text
text = allb.decode('utf-8')
n_lines = text.count('\n')
print(f"lines (newlines count) = {n_lines}")
print(f"size = {size}, full_sha12 = {full_sha12}, prefix_sha12 = {prefix_sha12}")

# print last 1500 chars decoded
print()
print("=== last 1500 chars decoded ===")
print(text[-1500:])
print()
print("=== end ===")
