# -*- coding: utf-8 -*-
"""R-6 精确取证: v3 委托信沿革行的 v2 槽位值 vs 实际 v2/v1 件 SHA-12。UTF-8 自写盘。"""
import hashlib
import json
import pathlib
import re

MAIN = pathlib.Path("D:/私人资料/deposon-repo")
L = MAIN / "letters"
OUT = MAIN / ".tmp/_r6_evidence.txt"


def sha12(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12].upper()


buf = []


def w(s=""):
    buf.append(str(s))


groups = {
    "paper": [L / "_v4_commission_paper_final_glm_2026_09_24.md",
              L / "_v4_commission_paper_final_glm_2026_09_24_v2.md",
              L / "_v4_commission_paper_final_glm_2026_09_24_v3.md",
              L / "_v4_commission_paper_final_glm_2026_09_24_v4.md"],
    "线上": [L / "_v4_commission_online_report_coze_2026_09_24.md",
               L / "_v4_commission_online_report_coze_2026_09_24_v2.md",
               L / "_v4_commission_online_report_coze_2026_09_24_v3.md",
               L / "_v4_commission_online_report_coze_2026_09_24_v4.md"],
    "upload_executor": [L / "_v4_commission_upload_executor_2026_09_24.md",
                        L / "_v4_commission_upload_executor_2026_09_24_v2.md",
                        L / "_v4_commission_upload_executor_2026_09_24_v3.md"],
}

for g, files in groups.items():
    w(f"\n===== {g} =====")
    actual = {}
    for p in files:
        actual[p.name] = sha12(p) if p.exists() else "MISSING"
        w(f"  actual {p.name:58s} {p.stat().st_size if p.exists() else 0:>7} B  {actual[p.name]}")
    v3 = [p for p in files if p.name.endswith("_v3.md")]
    for p in v3:
        t = p.read_text(encoding="utf-8", errors="replace")
        w(f"\n  --- {p.name} 沿革/版本槽位行 ---")
        for i, ln in enumerate(t.splitlines(), 1):
            if re.search(r"v2|v1|沿革|版本|承", ln) and (
                    "```" not in ln) and len(ln) < 400:
                w(f"   L{i}: {ln.strip()}")
    # 判定
    v1n = files[0].name
    v2n = files[1].name
    for p in v3:
        t = p.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"v2[^0-9A-F]{0,12}([0-9A-F]{12})", t)
        claimed = m.group(1) if m else None
        w(f"\n  VERDICT {p.name}: 沿革行称 'v2 = {claimed}'")
        w(f"     实际 v1 {v1n} = {actual[v1n]}")
        w(f"     实际 v2 {v2n} = {actual[v2n]}")
        w(f"     → claimed == v1 值? {claimed == actual[v1n]}")
        w(f"     → claimed == v2 值? {claimed == actual[v2n]}")

OUT.write_text("\n".join(buf), encoding="utf-8")
print("written", OUT)
