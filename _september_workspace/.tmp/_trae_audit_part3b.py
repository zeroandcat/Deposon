# -*- coding: utf-8 -*-
"""Trae 余项核验 part3b: root-agnostic + 每节 try/except 隔离。"""
import hashlib
import json
import pathlib
import re
import traceback

MAIN = pathlib.Path("D:/私人资料/deposon-repo")
SUB = pathlib.Path("D:/私人资料/deposon-sub")
ROOTS = [MAIN / "results", MAIN / "letters", MAIN / "docs", MAIN / "paper", MAIN / "corpus", MAIN]


def sha12(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def out(tag, obj):
    print(f"\n===== {tag} =====")
    print(json.dumps(obj, ensure_ascii=False, indent=1, default=str))


def fstat(p):
    if not p.exists():
        return {"exists": False}
    return {"exists": True, "bytes": p.stat().st_size, "sha12": sha12(p).upper()}


def find(name):
    hits = [p for r in ROOTS for p in r.rglob(name) if p.is_file()]
    return sorted(set(hits))


def lines_of(p, pat, flags=0, limit=30):
    t = p.read_text(encoding="utf-8", errors="replace")
    rx = re.compile(pat, flags)
    return {f"L{i}": ln.strip()[:300] for i, ln in enumerate(t.splitlines(), 1)
            if rx.search(ln)}


def sec(tag, fn):
    try:
        out(tag, fn())
    except Exception:
        out(tag + " [ERROR]", {"traceback": traceback.format_exc()[-900:]})


# ---- R-6: 三组委托信 (v3 与 v4) 定位 ----
def r6():
    res = {}
    for label in ["commission_paper", "commission_线上", "commission_upload_executor"]:
        found = []
        for r in ROOTS:
            for p in r.glob(f"*{label}*"):
                if p.is_file():
                    found.append(p)
        res[label] = [{"path": str(p.relative_to(MAIN)), **fstat(p)}
                      for p in sorted(set(found))]
    return res


sec("R-6 inventory", r6)


def r6_heads():
    res = {}
    for p in find("*commission_*"):
        if "_v3" not in p.name:
            continue
        ls = p.read_text(encoding="utf-8", errors="replace").splitlines()
        res[p.name] = {"stat": fstat(p), "head": [ln.strip()[:220] for ln in ls[:10]]}
    return res


sec("R-6 v3 letter heads", r6_heads)


def r11():
    p = find("*upload_channel_authorization_2026_09_26.md")
    if not p:
        return {"found": False}
    p = p[0]
    return {"path": str(p.relative_to(MAIN)), "stat": fstat(p),
            "E35_E36": lines_of(p, r"E-3[56]", limit=40)}


sec("R-11", r11)


def r13():
    p = find("*commission_upload_executor_reply_v3_2026_09_24.md")
    if not p:
        return {"found": False}
    p = p[0]
    ls = p.read_text(encoding="utf-8", errors="replace").splitlines()
    rows = {f"L{i}": ln.strip()[:120] for i, ln in enumerate(ls, 1)
            if re.match(r"^\s*\|\s*\d+\s*\|", ln)}
    return {"path": str(p.relative_to(MAIN)), "stat": fstat(p),
            "L14": ls[13].strip()[:400] if len(ls) > 13 else None,
            "n_numeric_table_rows": len(rows), "rows": rows,
            "sum_TagA_TagB": lines_of(p, r"Tag-A|Tag-B", limit=12)}


sec("R-13", r13)


def r14():
    p = find("*_v4_supp_prereg_v02_add_L14V3_2026_09_24.md")
    if not p:
        return {"found": False}
    p = p[0]
    return {"path": str(p.relative_to(MAIN)), "stat": fstat(p),
            "48738": lines_of(p, r"48,?738", limit=10),
            "52942": lines_of(p, r"52,?942", limit=10),
            "802DECE2286A": lines_of(p, r"802DECE2286A", flags=re.I, limit=10)}


sec("R-14", r14)


def r15():
    res = {}
    for key, nm in [("executor_t15r2", "_v4_supp_t15r2_executor.py"),
                    ("prereg_add_T15r2", "_v4_supp_prereg_v02_add_T15r2_2026_09_26.md"),
                    ("result_t15r2", "_v4_supp_t15r2_result.json"),
                    ("verdict_t15r2", "_v4_supp_t15r2_verdict.md")]:
        f = find(nm)
        if not f:
            res[key] = {"found": False}
            continue
        p = f[0]
        res[key] = {"path": str(p.relative_to(MAIN)), "stat": fstat(p),
                    "mentions_62": lines_of(p, r"\b62\b", limit=6),
                    "mentions_60": lines_of(p, r"\+?60 calls|\b60\b", limit=6),
                    "mentions_180": lines_of(p, r"\b180\b", limit=6)}
    return res


sec("R-15", r15)


def r16():
    p = find("*_v3_v4_achievements_inventory_2026_09_24.md")
    if not p:
        return {"found": False}
    p = p[0]
    d = {"path": str(p.relative_to(MAIN)), "stat": fstat(p),
         "NOT_ON_DISK": lines_of(p, r"NOT-ON-DISK|NOT_ON_DISK", limit=25)}
    for nm in ["_v4_pi_cot_v2_ruleset_result.json", "_v4_pi_cot_v2_ruleset_verdict.md",
               "_v4_pi_cot_v2_ruleset_prereg.md", "_v4_pi_cot_v2_result.json",
               "_v4_pi_cot_v2_verdict.md", "_v4_pi_cot_v2_prereg.md"]:
        d[f"exists::{nm}"] = bool(find(nm))
    return d


sec("R-16", r16)


def r17():
    a = SUB / "_tmp_v2_redesign.py"
    b = find("_v4_pi_cot_v2_ruleset_v2_executor.py")
    d = {"sub": fstat(a), "main": fstat(b[0]) if b else {"found": False}}
    ta = a.read_text(encoding="utf-8", errors="replace") if a.exists() else ""
    tb = b[0].read_text(encoding="utf-8", errors="replace") if b else ""
    ma = re.search(r"KW_V2\s*=\s*\[(.*?)\]", ta, re.S)
    mb = re.search(r"KEYWORDS_V2\s*=\s*\[(.*?)\]", tb, re.S)
    la = re.findall(r"[\"'][^\"']+[\"']", ma.group(1)) if ma else []
    lb = re.findall(r"[\"'][^\"']+[\"']", mb.group(1)) if mb else []
    d["sub_n"] = len(la)
    d["main_n"] = len(lb)
    d["same_set"] = set(la) == set(lb)
    d["same_order"] = la == lb
    d["sub_dups"] = sorted({x for x in la if la.count(x) > 1})
    d["main_dups"] = sorted({x for x in lb if lb.count(x) > 1})
    d["only_in_sub"] = sorted(set(la) - set(lb))
    d["only_in_main"] = sorted(set(lb) - set(la))
    return d


sec("R-17", r17)


def r18():
    res = {}
    for p in find("*commission_*"):
        if "_v4" not in p.name:
            continue
        ls = p.read_text(encoding="utf-8", errors="replace").splitlines()
        res[p.name] = {"stat": fstat(p),
                       "Z_lines": {f"L{i}": ln.strip()[:200]
                                   for i, ln in enumerate(ls, 1)
                                   if re.search(r"31,?167|21,?069|31,?531|21,?433|D5337702CEC9|802C705E1469", ln)}}
    return res


sec("R-18", r18)


def r19():
    res = {}
    for p in (sorted((MAIN / "results").glob("_v4_maindir_cleanup_manifest_*.md"))
              + sorted((MAIN / "results").glob("_v4_noise_cleanup_manifest_v*.md"))):
        res[p.name] = {"stat": fstat(p),
                       "delta_lines": lines_of(p, r"after\s*[−\-]\s*before|before\s*[−\-]\s*after", limit=10),
                       "delete_count_lines": lines_of(p, r"实际删除|真删", limit=10)}
    return res


sec("R-19", r19)


def r20():
    p = SUB / "_check_conv_archive.ps1"
    if not p.exists():
        return {"found": False}
    b = p.read_bytes()
    return {"path": str(p), "stat": fstat(p), "BOM": b[:3] == b"\xef\xbb\xbf",
            "crlf": b.count(b"\r\n"),
            "tail": b.decode("utf-8-sig", errors="replace").splitlines()[-14:]}


sec("R-20", r20)


def r21():
    res = {}
    for p in find("*_v4_track2_multimodel_verdict_2026_09_23.md"):
        res[p.name] = {"stat": fstat(p),
                       "selfscan": lines_of(p, r"11 模式|10 模式|SENSITIVE_PATTERNS|模式", limit=12)}
    for p in MAIN.rglob("rerun.py"):
        t = p.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"SENSITIVE_PATTERNS\s*=\s*\[(.*?)\n\]", t, re.S)
        res[f"rerun::{p.relative_to(MAIN)}"] = {
            "stat": fstat(p),
            "n_patterns": len(re.findall(r"\(\s*\"", m.group(1))) if m else None,
            "names": re.findall(r"\(\s*\"([^\"]+)\"", m.group(1)) if m else None}
    return res


sec("R-21", r21)
