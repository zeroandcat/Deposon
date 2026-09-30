# -*- coding: utf-8 -*-
"""Trae 余项核验 part2: R-2 精扫 / R-4 副区对照 / R-9 JSON 分布实测 / R-10 全表"""
import hashlib
import json
import pathlib
import re

MAIN = pathlib.Path("D:/私人资料/deposon-repo")
SUB = pathlib.Path("D:/私人资料/deposon-sub")


def sha12(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def out(tag, obj):
    print(f"\n===== {tag} =====")
    print(json.dumps(obj, ensure_ascii=False, indent=1, default=str))


# ---- R-2 精扫: 硬编码 "proxy_used": False 计数 ----
fam = sorted((MAIN / "results").glob("_v4_supp_l14v3_batch*_r*_executor.py"))
hard, field, detail = [], [], []
for p in fam:
    t = p.read_text(encoding="utf-8", errors="replace")
    h = re.findall(r'"proxy_used"\s*:\s*False', t)
    c = re.findall(r"no_proxy_compliance", t)
    if h:
        hard.append(p.name)
    if c:
        field.append(p.name)
    if h or c:
        detail.append({"file": p.name, "hardcoded_False_hits": len(h),
                       "no_proxy_compliance_hits": len(c)})
out("R-2 family", {"scanned": len(fam), "hardcoded_False": len(hard),
                   "no_proxy_compliance": len(field),
                   "hardcoded_files": hard, "detail": detail})

# 单件逻辑链逐行
p = MAIN / "results/_v4_supp_l14v3_batch10_r1_executor.py"
lines = p.read_text(encoding="utf-8").splitlines()
out("R-2 batch10_r1 logic chain",
    {f"L{i}": lines[i - 1].strip() for i in (355, 677, 678, 679, 680, 681, 682)
     if i <= len(lines)})

# ---- R-4: 副区件 vs 主目录 d2b 件 对照 ----
a = SUB / "results/_test_conv_out.txt"
b = MAIN / "results/_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json"
cmp4 = {}
if a.exists() and b.exists():
    ab, bb = a.read_bytes(), b.read_bytes()
    cmp4 = {
        "sub_test_conv_out": {"bytes": len(ab), "sha12": sha12(a).upper()},
        "main_d2b_json": {"bytes": len(bb), "sha12": sha12(b).upper()},
        "byte_identical": ab == bb,
        "equal_after_strip_bom": ab.lstrip(b"\xef\xbb\xbf") == bb,
        "sub_without_bom_bytes": len(ab.lstrip(b"\xef\xbb\xbf")),
        "main_bytes": len(bb),
        "main_has_bom": bb[:3] == b"\xef\xbb\xbf",
    }
    da = json.loads(ab.decode("utf-8-sig"))
    db = json.loads(bb.decode("utf-8-sig"))
    ta, tb = ab.decode("utf-8-sig"), bb.decode("utf-8-sig")
    cmp4["json_equal_after_strip_bom"] = (da == db)
    fa = re.search(r'"fingerprint_self_hash_after_birth"\s*:\s*"([^"]*)"', ta)
    fb = re.search(r'"fingerprint_self_hash_after_birth"\s*:\s*"([^"]*)"', tb)
    cmp4["sub_self_reported"] = fa.group(1) if fa else None
    cmp4["main_self_reported"] = fb.group(1) if fb else None
    # 逐 key 差异
    diff = [k for k in set(da) | set(db) if da.get(k) != db.get(k)]
    cmp4["top_key_diffs"] = diff
out("R-4 cross-region compare", cmp4)

# ---- R-9: JSON 实测 C3/C4 分布 ----
js = MAIN / "results/_v3_construct_degradation_diag_2026_09_23.json"
d = json.loads(js.read_text(encoding="utf-8"))
r9 = {"top": list(d.keys())}


def deep(o, path="", depth=0, acc=None):
    acc = acc if acc is not None else {}
    if depth > 7:
        return acc
    if isinstance(o, dict):
        for k, v in o.items():
            deep(v, f"{path}.{k}", depth + 1, acc)
    elif isinstance(o, list):
        acc[path] = f"<list len={len(o)}>"
        if o and isinstance(o[0], dict) and len(o) <= 30:
            acc[path + "[keys]"] = sorted(o[0].keys())
    else:
        acc[path] = o
    return acc


flat = deep(d)
r9["all_scalar_paths"] = {k: v for k, v in flat.items()
                           if not isinstance(v, str) or len(v) < 120}
out("R-9 json flat", r9)
