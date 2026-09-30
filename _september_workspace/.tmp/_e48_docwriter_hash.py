# -*- coding: utf-8 -*-
"""E-48 只读复算脚本（doc-writer agent-0032834a3e04 / 2026-09-28）
用途：对 results/ 下 V3-R rescript 系列逐件复算 SHA-12 + 字节数 + 件内 E-41.x 自注行。
只读：0 写入被检件。输出为 stdout。
"""
import hashlib
import os
import re

ROOT = r"D:\私人资料\deposon-repo"
RES = os.path.join(ROOT, "results")

CANDIDATES = [
    "_v3_recheck_01_rescript_2026_09_27.md",
    "_v3_recheck_04_rescript_2026_09_27.md",
    "_v3_recheck_05_rescript_2026_09_28.md",
    "_v3_recheck_08_rescript_2026_09_27.md",
    os.path.join("_v3_recheck_08b_executor", "rescript_2026_09_27.md"),
    "_v3_recheck_10_rescript_2026_09_27.md",
    "_v3_recheck_12_rescript_2026_09_27.md",
    "_v3_recheck_19_rescript_2026_09_27.md",
    "_v3_recheck_21_rescript_2026_09_27.md",
    "_v3_recheck_26_rescript_2026_09_27.md",
    "_v3_recheck_26b_rescript_2026_09_27.md",
    "_v3_recheck_27_rescript_2026_09_27.md",
    "_v3_recheck_28_rescript_2026_09_27.md",
    "_v3_recheck_35_rescript_2026_09_27.md",
    "_v4_pi_cot_v3_v3r1_rescript_2026_09_27.md",
]

PAT = re.compile(r"E-41")


def sha12(path):
    data = open(path, "rb").read()
    return hashlib.sha256(data).hexdigest()[:12], len(data), data


print("name\tsha12\tbytes\tE41_hits\tfirst_selfdecl_line\tfirst_selfdecl_text")
for rel in CANDIDATES:
    p = os.path.join(RES, rel)
    if not os.path.isfile(p):
        print("%s\tMISSING\t-\t-\t-\t-" % rel)
        continue
    s12, n, data = sha12(p)
    bom = "BOM" if data[:3] == b"\xef\xbb\xbf" else "noBOM"
    crlf = data.count(b"\r\n")
    text = data.decode("utf-8")
    lines = text.split("\n")
    hits = [i + 1 for i, ln in enumerate(lines) if PAT.search(ln)]
    selfdecl = None
    for i, ln in enumerate(lines):
        if "勘误链位" in ln or ("E-41" in ln and "勘误" in ln):
            selfdecl = (i + 1, ln.strip())
            break
    if selfdecl:
        dl, dt = selfdecl
    else:
        dl, dt = "-", "-"
    print("%s\t%s\t%d\t%d\t%s\t%s [%s crlf=%d]" % (
        rel, s12, n, len(hits), dl, dt.replace("\t", " "), bom, crlf))

print("")
print("--- ALL E-41 hits per file ---")
for rel in CANDIDATES:
    p = os.path.join(RES, rel)
    if not os.path.isfile(p):
        continue
    data = open(p, "rb").read()
    text = data.decode("utf-8")
    lines = text.split("\n")
    hs = [(i + 1, lines[i].strip()[:110]) for i in range(len(lines)) if PAT.search(lines[i])]
    if hs:
        print("## %s  (%d hits)" % (rel, len(hs)))
        for ln, tx in hs:
            print("   L%d | %s" % (ln, tx))
