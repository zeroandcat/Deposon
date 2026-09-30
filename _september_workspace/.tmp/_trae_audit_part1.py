# -*- coding: utf-8 -*-
"""Trae 回函余项核验 (R-2/R-4/R-6/R-9/R-10/R-11/R-13/R-14/R-15/R-16..R-21)
只读既有件, 0 改盘。输出结构化实测结果供登记件引用。
SHA-12 = hashlib.sha256(b).hexdigest()[:12] 小写。
"""
import hashlib
import json
import pathlib
import re

MAIN = pathlib.Path("D:/私人资料/deposon-repo")
SUB = pathlib.Path("D:/私人资料/deposon-sub")


def sha12(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def stat(p: pathlib.Path):
    if not p.exists():
        return {"exists": False}
    b = p.read_bytes()
    return {"exists": True, "bytes": len(b), "sha12": sha12(p).upper(),
            "bom": b[:3] == b"\xef\xbb\xbf", "crlf": b.count(b"\r\n"),
            "mtime": __import__("datetime").datetime.fromtimestamp(
                p.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")}


def out(tag, obj):
    print(f"\n===== {tag} =====")
    print(json.dumps(obj, ensure_ascii=False, indent=1, default=str))


# ---------------- R-2: proxy_used 硬编码 -> no_proxy_compliance 自证式 ----------------
r2 = {}
for name in ["_v4_supp_l14v3_batch10_r1_executor.py"]:
    p = MAIN / "results" / name
    if p.exists():
        t = p.read_text(encoding="utf-8")
        hits = []
        for i, line in enumerate(t.splitlines(), 1):
            if "proxy_used" in line or "no_proxy_compliance" in line:
                hits.append(f"L{i}: {line.strip()}")
        r2[name] = {"stat": stat(p), "hits": hits[:24], "hits_total": len(hits)}
# 扫全 batch 族
fam = sorted((MAIN / "results").glob("_v4_supp_l14v3_batch*_r*_executor.py"))
fam_hard = 0
fam_field = 0
for p in fam:
    t = p.read_text(encoding="utf-8", errors="replace")
    if re.search(r"proxy_used\s*[:=]\s*False", t):
        fam_hard += 1
    if "no_proxy_compliance" in t:
        fam_field += 1
r2["family_scan"] = {"batch_executors_scanned": len(fam),
                     "with_proxy_used_hardcoded_False": fam_hard,
                     "with_no_proxy_compliance_field": fam_field,
                     "note": "自证式 = 字段取值恒 False ⇒ 该字段永不可能 True"}
out("R-2", r2)

# ---------------- R-4: deposon-sub/results/_test_conv_out.txt ----------------
r4 = {"stat": stat(SUB / "results/_test_conv_out.txt")}
p = SUB / "results/_test_conv_out.txt"
if p.exists():
    b = p.read_bytes()
    r4["json_load_direct"] = None
    try:
        json.loads(b.decode("utf-8"))
        r4["json_load_direct"] = "OK"
    except Exception as e:
        r4["json_load_direct"] = f"{type(e).__name__}: {e}"
    r4["json_load_utf8_sig"] = None
    try:
        json.loads(b.decode("utf-8-sig"))
        r4["json_load_utf8_sig"] = "OK"
    except Exception as e:
        r4["json_load_utf8_sig"] = f"{type(e).__name__}: {e}"
    t = b.decode("utf-8-sig", errors="replace")
    r4["placeholder_aaaaabbbbbb_count"] = t.count("aaaaabbbbbb")
    r4["schema_literal"] = (re.search(r'"schema"\s*:\s*"([^"]+)"', t) or [None, None])[1]
    m = re.search(r'"fingerprint_self_hash_after_birth"\s*:\s*"([^"]*)"', t)
    r4["fingerprint_self_hash_after_birth"] = m.group(1) if m else None
    # 该件自身 SHA-12 vs 自报指纹
    r4["file_actual_sha12"] = sha12(p).upper()
    r4["placeholder_matches_actual_sha12"] = (sha12(p).upper().lower().startswith("aaaaabbbbbb"))
out("R-4", r4)

# ---------------- R-9: C3/C4 分布互斥 ----------------
r9 = {}
md = MAIN / "results/_v3_supplement_verdict_2026_09_23.md"
js = MAIN / "results/_v3_construct_degradation_diag_2026_09_23.json"
r9["md_stat"] = stat(md)
r9["json_stat"] = stat(js)
if md.exists():
    t = md.read_text(encoding="utf-8")
    seg = []
    lines = t.splitlines()
    for i, line in enumerate(lines, 1):
        if re.search(r"\bC3\b|\bC4\b", line):
            seg.append(f"L{i}: {line.strip()[:220]}")
    r9["md_C3_C4_lines"] = seg[:30]
if js.exists():
    d = json.loads(js.read_text(encoding="utf-8"))
    r9["json_top_keys"] = list(d.keys())[:30]

    def walk(o, path="", depth=0):
        f = {}
        if depth > 4:
            return f
        if isinstance(o, dict):
            for k, v in o.items():
                f.update(walk(v, f"{path}.{k}", depth + 1))
        elif isinstance(o, list):
            f[path] = f"<list len={len(o)}>"
        else:
            f[path] = o
        return f
    flat = walk(d)
    r9["json_scalar_paths_containing_c3_c4"] = {
        k: v for k, v in flat.items()
        if re.search(r"c3|c4", k, re.I) and isinstance(v, (int, float, str, bool))}
out("R-9", r9)

# ---------------- R-10: 9 件 dataset_addendum 自指指纹漂移 ----------------
r10 = {}
adds = sorted((MAIN / "results").glob("_v4_pi_cot_v2_dataset_addendum_*"))
tbl = []
for p in adds:
    if p.suffix.lower() not in (".json", ".md"):
        continue
    row = {"file": p.name, "actual_sha12": sha12(p).upper(), "bytes": p.stat().st_size}
    if p.suffix.lower() == ".json":
        try:
            d = json.loads(p.read_text(encoding="utf-8-sig"))
            m = re.search(r'"fingerprint_self_hash_after_birth"\s*:\s*"([^"]*)"',
                          p.read_text(encoding="utf-8-sig", errors="replace"))
            row["self_reported"] = m.group(1) if m else None
            row["drift"] = (row["self_reported"] != row["actual_sha12"]) if row["self_reported"] else None
        except Exception as e:
            row["parse_error"] = f"{type(e).__name__}: {e}"
    tbl.append(row)
r10["addendum_json_files"] = len(tbl)
r10["rows"] = tbl
out("R-10", r10)
