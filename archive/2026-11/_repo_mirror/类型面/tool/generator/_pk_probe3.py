import json

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

p = r_dep_path("results/_v3_recheck_08c_preexp_data/result_2026_09_27.json")
d = json.load(open(p, encoding="utf-8"))
print("=== runs[0] keys ===", list(d["runs"][0].keys()) if isinstance(d["runs"][0],dict) else type(d["runs"][0]))
# find FIX-D entries
for r in d["runs"]:
    if isinstance(r, dict) and str(r.get("fixture_id","")).upper().find("FIX-D")>=0:
        print(json.dumps(r, ensure_ascii=False, indent=1)[:1800]); break
