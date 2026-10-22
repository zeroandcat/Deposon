# -*- coding: utf-8 -*-
"""注记件 §2.3/§2.4 所引行号之逐条复核（工具件 · 0 属证据面）。"""
import io
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
BASE = Path(r"_repo_mirror")
FIX = BASE / "deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_fix_2026_10_10.py"
REN = BASE / "deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_rename_2026_10_10.py"

MARKS = ("# ---- 独立验证面声明位", "INDEP_VERIFY_DECL", "def probe_independent_evidence",
         "return probe", "# ---------- 5b", "indep = probe_", "indep_verified = indep",
         '"independence_verification"', '"runner_fix_notice"', "CORRECTED COPY",
         'c["chain"]["self_verified_only"]', 'c["chain"]["self_verified_only_basis"]',
         'independence_deficiency_alarm"] = not indep_verified', "prescription_ref",
         'c["chain"]["verification_basis_self_rewalk_only"]',
         '"key_rename_migration"', "self_verified_only", "P_OUT_", "PINNED = {",
         'GENERATOR = "', '"task_id"')

for p, tag in ((FIX, "①"), (REN, "②")):
    L = p.read_text(encoding="utf-8").split("\n")
    print(f"===== {tag} {p.name} (lines={len(L)-1}) =====")
    for i, ln in enumerate(L, 1):
        s = ln.strip()
        if any(s.startswith(m) for m in MARKS) or (s.startswith("#") and "独立验证面声明位" in s):
            print(f"  L{i:>4d} | {ln.strip()[:104]}")
