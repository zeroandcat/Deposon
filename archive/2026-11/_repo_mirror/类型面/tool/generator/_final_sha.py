# -*- coding: utf-8 -*-
"""出件前自核: 既有件 0 触动 + 新件 SHA-12 台账。"""
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


MAIN = pathlib.Path(_dep_path(""))
FROZEN = {
    "results/_v4_supp_t15r2_executor.py": "4b5b720d5cda",
    "results/_v4_supp_t15_executor.py": "558e635f9ba6",
    "results/_v4_supp_t15r2_result.json": None,
    "results/_v4_supp_t15r2_verdict.md": None,
    "docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md": None,
}
NEW = ["results/_v4_supp_t15r2_executor_r1_2026_09_28.py"]

lines = []
for rel, exp in FROZEN.items():
    p = MAIN / rel
    act = hashlib.sha256(p.read_bytes()).hexdigest()[:12] if p.exists() else "MISSING"
    ok = "" if exp is None else ("MATCH" if act.lower() == exp else f"!! MISMATCH exp={exp}")
    lines.append("FROZEN %-58s %s %s" % (rel, act.upper(), ok))
for rel in NEW:
    p = MAIN / rel
    b = p.read_bytes()
    lines.append("NEW    %-58s %d B / %s  crlf=%d bom=%s"
                 % (rel, len(b), hashlib.sha256(b).hexdigest()[:12].upper(),
                    b.count(b"\r\n"), b[:3] == b"\xef\xbb\xbf"))
# 原 F1 修复件复核
for rel in ["results/_v4_supp_t15_executor_r1_2026_09_27.py"]:
    p = MAIN / rel
    b = p.read_bytes()
    lines.append("PRIOR  %-58s %d B / %s"
                 % (rel, len(b), hashlib.sha256(b).hexdigest()[:12].upper()))

out = "\n".join(lines)
pathlib.Path(".tmp/_final_sha.txt").write_text(out, encoding="utf-8")
print(out)
