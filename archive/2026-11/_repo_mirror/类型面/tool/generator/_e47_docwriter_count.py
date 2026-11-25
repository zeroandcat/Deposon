"""E-47 登记包 · 只读复算脚本（doc-writer）
仅对盘上既有件做只读核验：KEYWORDS_V2 词表计数（对齐 M-8 登记值 263 / unique 260 / dups 3）。
0 写入既有件 / 0 派生 JSON / 0 网络 / 0 LLM。
"""
import ast
import hashlib
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


P = pathlib.Path(r_dep_path("results/_v4_pi_cot_v2_ruleset_v2_executor.py"))
src = P.read_text(encoding="utf-8")
tree = ast.parse(src)
target = None
for node in ast.walk(tree):
    if isinstance(node, ast.AnnAssign) and getattr(node.target, "id", "") == "KEYWORDS_V2":
        target = node.value
        break
if target is None:
    raise SystemExit("KEYWORDS_V2 not found")

values = []
keys = []
for k, v in zip(target.keys, target.values):
    keys.append(k.value)
    values.extend([e.value for e in v.elts])

uniq = sorted(set(values))
dups = sorted({x for x in values if values.count(x) > 1})
print("keys:", keys)
print("total_values =", len(values))
print("unique =", len(uniq))
print("dups =", len(dups), dups)
print("sha12 =", hashlib.sha256(P.read_bytes()).hexdigest()[:12].upper())
print("bytes =", P.stat().st_size)
