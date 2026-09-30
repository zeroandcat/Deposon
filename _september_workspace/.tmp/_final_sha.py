# -*- coding: utf-8 -*-
"""出件前自核: 既有件 0 触动 + 新件 SHA-12 台账。"""
import hashlib
import pathlib

MAIN = pathlib.Path("D:/私人资料/deposon-repo")
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
