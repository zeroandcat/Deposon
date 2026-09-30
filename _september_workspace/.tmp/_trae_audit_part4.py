# -*- coding: utf-8 -*-
"""Trae 余项核验 part4: R-13 行数 / R-14 字节 / R-16 / R-17 / R-18 / R-19 / R-20 / R-21"""
import hashlib
import pathlib
import re

MAIN = pathlib.Path("D:/私人资料/deposon-repo")
SUB = pathlib.Path("D:/私人资料/deposon-sub")
OUT = MAIN / ".tmp/_audit_part4.txt"
buf = []


def w(s=""):
    buf.append(str(s))


def sha12(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12].upper()


def st(p):
    return f"{p.stat().st_size} B / {sha12(p)}" if p.exists() else "MISSING"


# ---------- R-13 ----------
w("===== R-13 =====")
p = MAIN / "letters/_v4_commission_upload_executor_reply_v3_2026_09_24.md"
ls = p.read_text(encoding="utf-8").splitlines()
tagA = [ln for ln in ls if re.match(r"^\|\s*\d{1,2}\s*\|", ln)]
tagB = [ln for ln in ls if re.match(r"^\|\s*B-\d+", ln)]
etag = [ln for ln in ls if re.match(r"^\|\s*E-\d+", ln)]
w(f"  reply file: {st(p)}")
w(f"  numeric rows (Tag-A style) = {len(tagA)}")
w(f"  B- rows                     = {len(tagB)}")
w(f"  E- rows                     = {len(etag)}")
w(f"  TOTAL listed rows           = {len(tagA)+len(tagB)+len(etag)}")
w(f"  header claim L14            = {ls[13].strip()}")
nums = sorted(int(re.match(r"^\|\s*(\d+)", ln).group(1)) for ln in tagA)
w(f"  Tag-A numbering range       = {min(nums) if nums else '-'}..{max(nums) if nums else '-'} "
  f"(n={len(nums)}, dup={len(nums)!=len(set(nums))})")
w("  --- raw table-ish lines sample (first 6 / last 6 of any | at line start) ---")
anyrows = [ln for ln in ls if re.match(r"^\|\s*\S", ln)]
for ln in anyrows[:6] + anyrows[-6:]:
    w(f"    {ln.strip()[:150]}")
bs = sorted(re.match(r"^\|\s*(B-\d+)", ln).group(1) for ln in tagB)
w(f"  Tag-B ids                   = {bs}")
es = sorted(re.match(r"^\|\s*(E-\d+)", ln).group(1) for ln in etag)
w(f"  E ids                       = {es}")
# 源件 v3 §2.4 E 表
src = MAIN / "letters/_v4_commission_upload_executor_2026_09_24_v3.md"
sls = src.read_text(encoding="utf-8").splitlines()
srcE = [ln for ln in sls if re.match(r"^\|\s*E-\d+", ln)]
srcA = [ln for ln in sls if re.match(r"^\|\s*\d{1,2}\s*\|", ln)]
srcB = [ln for ln in sls if re.match(r"^\|\s*B-\d+", ln)]
w(f"  SOURCE v3: {st(src)}")
w(f"  SOURCE v3 Tag-A rows={len(srcA)}  Tag-B rows={len(srcB)}  E rows={len(srcE)} "
  f"=> total {len(srcA)+len(srcB)+len(srcE)}")
w(f"  SOURCE v3 E ids = {sorted(set(re.findall(r'E-\\d+', ln)) for ln in srcE for ln in [str(sorted(set(re.findall(r'E-[0-9]+', x)) for x in srcE))])[:1] if False else sorted({m for ln in srcE for m in re.findall(r'E-[0-9]+', ln)})}")

# ---------- R-14 ----------
w("\n===== R-14 =====")
for nm in ["_v4_supp_prereg_v02_add_T1_2026_09_24.md",
           "_v4_supp_prereg_v02_add_T15_2026_09_24.md",
           "_v4_supp_prereg_v02_add_T15r2_2026_09_26.md",
           "_v4_supp_prereg_v02_add_L14V3_2026_09_24.md"]:
    f = MAIN / "results" / nm
    w(f"  {nm:56s} {st(f) if f.exists() else 'MISSING'}")
w("  --- 各件自记 add_T1 值 ---")
for f in sorted(MAIN.glob("results/_v4_supp_prereg_v02_add_*.md")):
    t = f.read_text(encoding="utf-8", errors="replace")
    hits = {f"L{i}": ln.strip()[:200] for i, ln in enumerate(t.splitlines(), 1)
            if re.search(r"48,?738|52,?942", ln)}
    w(f"  {f.name}: {hits if hits else '(无 48,738/52,942 字面)'}")

# ---------- R-16 ----------
w("\n===== R-16 =====")
inv = MAIN / "results/_v3_v4_achievements_inventory_2026_09_24.md"
w(f"  inventory: {st(inv)}")
il = inv.read_text(encoding="utf-8").splitlines()
w("  --- NOT-ON-DISK lines ---")
for i, ln in enumerate(il, 1):
    if re.search(r"NOT-ON-DISK|NOT_ON_DISK", ln):
        w(f"   L{i}: {ln.strip()[:240]}")
w("  --- on-disk existence ---")
for nm in ["_v4_pi_cot_v2_ruleset_result.json", "_v4_pi_cot_v2_ruleset_verdict.md",
           "_v4_pi_cot_v2_ruleset_prereg.md", "_v4_pi_cot_v2_result.json",
           "_v4_pi_cot_v2_verdict.md", "_v4_pi_cot_v2_prereg.md"]:
    w(f"   {'EXISTS ' if (MAIN / 'results' / nm).exists() else 'ABSENT '} {nm}")
err = MAIN / "results/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md"
w(f"  erratum(3dir): {st(err) if err.exists() else 'MISSING'}")

# ---------- R-17 ----------
w("\n===== R-17 =====")
a = SUB / "_tmp_v2_redesign.py"
b = MAIN / "results/_v4_pi_cot_v2_ruleset_v2_executor.py"
w(f"  sub  {st(a)}")
w(f"  main {st(b)}")
ta = a.read_text(encoding="utf-8", errors="replace")
tb = b.read_text(encoding="utf-8", errors="replace")
for label, txt, var in [("sub", ta, "KW_V2"), ("main", tb, "KEYWORDS_V2")]:
    idx = txt.find(var)
    w(f"  --- {label} {var} @char {idx} ---")
    if idx >= 0:
        seg = txt[idx:idx + 2600]
        w("   " + seg[:1400].replace("\n", "\n   "))
        lst = re.findall(r'"([^"]+)"', seg[:seg.find("]")])
        w(f"   n_literals={len(lst)} first5={lst[:5]} last5={lst[-5:]}")
        dups = sorted({x for x in lst if lst.count(x) > 1})
        w(f"   dups={dups}")
    else:
        w(f"   !! {var} NOT FOUND in {label}")

# ---------- R-18 ----------
w("\n===== R-18 =====")
for nm in ["_v4_commission_paper_final_glm_2026_09_24_v4.md",
           "_v4_commission_wechat_report_coze_2026_09_24_v4.md"]:
    f = MAIN / "letters" / nm
    if not f.exists():
        w(f"  {nm}: MISSING")
        continue
    t = f.read_text(encoding="utf-8").splitlines()
    w(f"  {nm}: {st(f)}")
    for i, ln in enumerate(t, 1):
        if re.search(r"§Z|31,?167|21,?069|D5337702CEC9|802C705E1469|31,?531|21,?433", ln):
            w(f"    L{i}: {ln.strip()[:220]}")

# ---------- R-19 ----------
w("\n===== R-19 =====")
for pat in ["_v4_maindir_cleanup_manifest_*.md", "_v4_noise_cleanup_manifest_v*.md"]:
    for f in sorted((MAIN / "results").glob(pat)):
        t = f.read_text(encoding="utf-8", errors="replace").splitlines()
        w(f"  {f.name}: {st(f)}")
        for i, ln in enumerate(t, 1):
            if re.search(r"活态计数|after\s*[−-]\s*before|实际删除|真删", ln):
                w(f"    L{i}: {ln.strip()[:230]}")

# ---------- R-20 ----------
w("\n===== R-20 =====")
p = SUB / "_check_conv_archive.ps1"
if p.exists():
    b = p.read_bytes()
    w(f"  {p}: {st(p)}")
    w(f"  BOM={b[:3] == b'\xef\xbb\xbf'}  CRLF={b.count(b'\r\n')}")
    lines = b.decode("utf-8-sig", errors="replace").splitlines()
    w(f"  total lines = {len(lines)}; last 10 lines verbatim:")
    for i, ln in enumerate(lines[-10:], len(lines) - 9):
        w(f"    L{i}: {ln!r}")

# ---------- R-21 ----------
w("\n===== R-21 =====")
v = MAIN / "results/_v4_track2_multimodel_verdict_2026_09_23.md"
if v.exists():
    w(f"  verdict: {st(v)}")
    for i, ln in enumerate(v.read_text(encoding="utf-8").splitlines(), 1):
        if re.search(r"模式|SENSITIVE_PATTERNS|自扫", ln):
            w(f"    L{i}: {ln.strip()[:220]}")
for rp in sorted(MAIN.rglob("rerun.py")):
    t = rp.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"SENSITIVE_PATTERNS\s*=\s*\[(.*?)\n\]", t, re.S)
    if m:
        names = re.findall(r'\(\s*"([^"]+)"', m.group(1))
        w(f"  rerun.py {rp.relative_to(MAIN)}: {st(rp)} n_patterns={len(names)}")
        w(f"    names={names}")

OUT.write_text("\n".join(buf), encoding="utf-8")
print("written", OUT)
