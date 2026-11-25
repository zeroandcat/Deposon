import json
import pathlib

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


d = json.loads(pathlib.Path(_dep_path(".tmp/_cpatomic_pycache_pre_2026_09_28.json"))
               .read_text(encoding="utf-8"))
out = []
for x in d["pyc_dirs"]:
    out.append(f"DIR {x['rel']}/  files={x['n_files']}  bytes={x['total_bytes']}  "
               f"gated={x['gated_frozen_adjacent']}")
    for f in x["files"]:
        out.append(f"    {f['name']:56s} {f['bytes']:>9d}  {f['sha12']}")
print("\n".join(out))
