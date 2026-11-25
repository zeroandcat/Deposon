import hashlib, os, sys

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


targets = set(sys.argv[1:])
base = _dep_path("")
skip = {'.git', 'node_modules', '__pycache__', '.venv', 'venv'}
n = 0
for root, dirs, files in os.walk(base):
    dirs[:] = [d for d in dirs if d not in skip]
    for f in files:
        p = os.path.join(root, f)
        try:
            b = open(p, 'rb').read()
        except Exception:
            continue
        n += 1
        h = hashlib.sha256(b).hexdigest()[:12]
        if h in targets:
            print(h, len(b), os.path.relpath(p, base).replace('\\', '/'))
print('SCANNED', n, file=sys.stderr)
