# -*- coding: utf-8 -*-
"""Trae 余项核验 part3: R-6 / R-11 / R-13 / R-14 / R-15 / R-16 / R-17 / R-18 / R-19 / R-20 / R-21"""
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


def lines_of(p, pat, flags=0, limit=30):
    t = p.read_text(encoding="utf-8", errors="replace")
    rx = re.compile(pat, flags)
    return {f"L{i}": ln.strip()[:300] for i, ln in enumerate(t.splitlines(), 1)
            if rx.search(ln)}


def fstat(p):
    if not p.exists():
        return {"exists": False}
    return {"exists": True, "bytes": p.stat().st_size, "sha12": sha12(p).upper()}


# ---------- R-6: 三组 v3 委托信 v2 槽位错挂 v1 身份值 ----------
r6 = {}
for label, pat in [
    ("paper", "_v4_commission_paper*"),
    ("线上", "_v4_commission_线上*"),
    ("upload_executor", "_v4_commission_upload_executor*"),
]:
    cands = sorted(list((MAIN / "results").glob(pat)) + list((MAIN / "letters").glob(pat))
                   + list((MAIN / "docs").rglob(pat)))
    r6[label] = [{"file": str(c.relative_to(MAIN)), **fstat(c)} for c in cands]
out("R-6 file inventory (v3/v4 commission letters)", r6)

# 在每份里找 v1/v2 版本槽位行
slot = {}
for c in sorted(list((MAIN / "results").glob("*commission_paper*v3*"))
                + list((MAIN / "results").glob("*commission_线上*v3*"))
                + list((MAIN / "results").glob("*commission_upload_executor*v3*"))
                + list((MAIN / "letters").glob("*commission_paper*v3*"))
                + list((MAIN / "letters").glob("*commission_线上*v3*"))):
    slot[c.name] = {"L1-12": [ln.strip()[:200] for ln in
                              c.read_text(encoding="utf-8", errors="replace")
                              .splitlines()[:12]]}
out("R-6 slot heads", slot)

# ---------- R-11: E-35 / E-36 边界 ----------
p = MAIN / "results/_v4_commission_upload_channel_authorization_2026_09_26.md"
r11 = {"stat": fstat(p)}
if p.exists():
    r11["E35_E36_lines"] = lines_of(p, r"E-3[56]", limit=40)
out("R-11", r11)

# ---------- R-13: 43 vs 44 ----------
p = MAIN / "results/_v4_commission_upload_executor_reply_v3_2026_09_24.md"
r13 = {"stat": fstat(p)}
if p.exists():
    ls = p.read_text(encoding="utf-8", errors="replace").splitlines()
    r13["L14_verbatim"] = ls[13].strip()[:400] if len(ls) > 13 else None
    r13["section2_table_rows"] = {
        f"L{i}": ln.strip()[:120] for i, ln in enumerate(ls, 1)
        if re.match(r"^\s*\|\s*\d+\s*\|", ln)}
    r13["count_numeric_rows_in_sec2"] = len(
        [ln for ln in ls if re.match(r"^\s*\|\s*\d+\s*\|", ln)])
out("R-13", r13)

# ---------- R-14: add_T1 陈旧值 48,738 vs 52,942 ----------
p = MAIN / "results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md"
r14 = {"stat": fstat(p)}
if p.exists():
    r14["lines_48738"] = lines_of(p, r"48,?738", limit=10)
    r14["lines_52942"] = lines_of(p, r"52,?942", limit=10)
    r14["lines_sha_802DECE2286A"] = lines_of(p, r"802DECE2286A", ignoreCase=True, limit=10)
out("R-14", r14)

# ---------- R-15: t15r2 executor +62 vs prereg +60/180 ----------
r15 = {}
for key, path in [
    ("executor_t15r2", MAIN / "results/_v4_supp_t15r2_executor.py"),
    ("prereg_add_T15r2", MAIN / "results/_v4_supp_prereg_v02_add_T15r2_2026_09_26.md"),
    ("result_t15r2", MAIN / "results/_v4_supp_t15r2_result.json"),
]:
    p = path
    if p.exists():
        r15[key] = {"stat": fstat(p),
                    "plus62": lines_of(p, r"\+?\s*62\s*(new\s*)?calls|62 新 calls|62 calls", limit=8),
                    "plus60": lines_of(p, r"\+?\s*60\s*calls|60 calls", limit=8),
                    "180": lines_of(p, r"\b180\b", limit=8)}
out("R-15", r15)

# ---------- R-16: achievements inventory §2.2 NOT-ON-DISK 误报 ----------
p = MAIN / "results/_v3_v4_achievements_inventory_2026_09_24.md"
r16 = {"stat": fstat(p)}
if p.exists():
    ls = p.read_text(encoding="utf-8", errors="replace").splitlines()
    r16["NOT_ON_DISK_lines"] = {f"L{i}": ln.strip()[:260]
                               for i, ln in enumerate(ls, 1)
                               if re.search(r"NOT-ON-DISK|NOT_ON_DISK", ln)}
    # 含 _ruleset_ 中缀的三个文件名是否真不存在
    for nm in ["_v4_pi_cot_v2_ruleset_result.json", "_v4_pi_cot_v2_ruleset_verdict.md",
               "_v4_pi_cot_v2_ruleset_prereg.md"]:
        r16[f"exists_with_ruleset::{nm}"] = (MAIN / "results" / nm).exists()
    for nm in ["_v4_pi_cot_v2_result.json", "_v4_pi_cot_v2_verdict.md",
               "_v4_pi_cot_v2_prereg.md"]:
        r16[f"exists_no_ruleset::{nm}"] = (MAIN / "results" / nm).exists()
out("R-16", r16)

# ---------- R-17: KW_V2 vs KEYWORDS_V2 ----------
r17 = {}
a = SUB / "_tmp_v2_redesign.py"
b = MAIN / "results/_v4_pi_cot_v2_ruleset_v2_executor.py"
for key, p in [("sub_tmp_v2_redesign", a), ("main_ruleset_v2_executor", b)]:
    r17[key] = fstat(p)
if a.exists():
    t = a.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"KW_V2\s*=\s*\[(.*?)\]", t, re.S)
    r17["sub_KW_V2_raw"] = (m.group(1)[:400] if m else None)
    if m:
        lst = re.findall(r"[\"'][^\"']+[\"']", m.group(1))
        r17["sub_KW_V2_n"] = len(lst)
        r17["sub_KW_V2_dups"] = sorted({x for x in lst if lst.count(x) > 1})
if b.exists():
    t = b.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"KEYWORDS_V2\s*=\s*\[(.*?)\]", t, re.S)
    r17["main_KEYWORDS_V2_raw"] = (m.group(1)[:400] if m else None)
    if m:
        lst = re.findall(r"[\"'][^\"']+[\"']", m.group(1))
        r17["main_KEYWORDS_V2_n"] = len(lst)
        r17["main_KEYWORDS_V2_dups"] = sorted({x for x in lst if lst.count(x) > 1})
if a.exists() and b.exists():
    ta = a.read_text(encoding="utf-8", errors="replace")
    tb = b.read_text(encoding="utf-8", errors="replace")
    ma = re.search(r"KW_V2\s*=\s*\[(.*?)\]", ta, re.S)
    mb = re.search(r"KEYWORDS_V2\s*=\s*\[(.*?)\]", tb, re.S)
    if ma and mb:
        la = re.findall(r"[\"'][^\"']+[\"']", ma.group(1))
        lb = re.findall(r"[\"'][^\"']+[\"']", mb.group(1))
        r17["same_set"] = set(la) == set(lb)
        r17["same_order"] = la == lb
        r17["only_in_sub"] = sorted(set(la) - set(lb))
        r17["only_in_main"] = sorted(set(lb) - set(la))
out("R-17", r17)

# ---------- R-18: paper / 线上 v4 委托信 §Z 自记字节 ----------
r18 = {}
for pat in ["*commission_paper*v4*", "*commission_线上*v4*"]:
    for p in sorted(list((MAIN / "results").glob(pat)) + list((MAIN / "letters").glob(pat))):
        t = p.read_text(encoding="utf-8", errors="replace")
        r18[p.name] = {"stat": fstat(p),
                       "self_bytes_lines": lines_of(p, r"31,?167|21,?069|31,?531|21,?433|§Z", limit=12)}
out("R-18", r18)

# ---------- R-19: cleanup manifest after−before ----------
r19 = {}
for pat in ["_v4_maindir_cleanup_manifest_*.md", "_v4_noise_cleanup_manifest_v*.md"]:
    for p in sorted((MAIN / "results").glob(pat)):
        t = p.read_text(encoding="utf-8", errors="replace")
        r19[p.name] = {"stat": fstat(p),
                       "before_after_lines": lines_of(p, r"after\s*[−\-]\s*before|before.*after", limit=8),
                       "actual_delete_lines": lines_of(p, r"实际删除|真删|deleted", ignoreCase=True, limit=8)}
out("R-19", r19)

# ---------- R-20: deposon-sub/_check_conv_archive.ps1 尾部死输出 ----------
p = SUB / "_check_conv_archive.ps1"
r20 = {"stat": fstat(p)}
if p.exists():
    b = p.read_bytes()
    r20["BOM"] = b[:3] == b"\xef\xbb\xbf"
    r20["crlf"] = b.count(b"\r\n")
    r20["tail_last_12_lines"] = b.decode("utf-8-sig", errors="replace").splitlines()[-12:]
out("R-20", r20)

# ---------- R-21: 11 模式 vs SENSITIVE_PATTERNS 10 ----------
r21 = {}
for pat in ["_v4_track2_multimodel_verdict_*.md"]:
    for p in sorted((MAIN / "results").glob(pat)):
        r21[p.name] = {"stat": fstat(p),
                       "selfscan_lines": lines_of(p, r"11 模式|10 模式|模式|SENSITIVE_PATTERNS", limit=12)}
for p in sorted(MAIN.rglob("rerun.py")):
    t = p.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"SENSITIVE_PATTERNS\s*=\s*\[(.*?)\n\]", t, re.S)
    r21[f"rerun::{p.relative_to(MAIN)}"] = {
        "stat": fstat(p),
        "n_patterns": len(re.findall(r"\(\s*\"", m.group(1))) if m else None,
        "names": re.findall(r"\(\s*\"([^\"]+)\"", m.group(1)) if m else None}
out("R-21", r21)
