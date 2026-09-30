# -*- coding: utf-8 -*-
"""E-48 只读复算脚本 4：v30 追加节源件 SHA-12 链逐件复算。"""
import hashlib
import io
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = r"D:\私人资料\deposon-repo"
FILES = [
    r"docs\V3X\TRAE_V3_ASSET_ERRATUM_2026_09_23.md",
    r"results\_v3_recheck_01_rescript_2026_09_27.md",
    r"results\_v3_recheck_04_rescript_2026_09_27.md",
    r"results\_v3_recheck_05_rescript_2026_09_28.md",
    r"results\_v3_recheck_08_rescript_2026_09_27.md",
    r"results\_v3_recheck_08b_executor\rescript_2026_09_27.md",
    r"results\_v3_recheck_10_rescript_2026_09_27.md",
    r"results\_v3_recheck_12_rescript_2026_09_27.md",
    r"results\_v3_recheck_19_rescript_2026_09_27.md",
    r"results\_v3_recheck_26_rescript_2026_09_27.md",
    r"results\_v3_recheck_26b_rescript_2026_09_27.md",
    r"results\_v3_recheck_27_rescript_2026_09_27.md",
    r"results\_v3_recheck_28_rescript_2026_09_27.md",
    r"results\_v3_recheck_21_rescript_2026_09_27.md",
    r"results\_v3_recheck_35_rescript_2026_09_27.md",
    r"results\_v3_recheck_08c_preexp_data\rescript_2026_09_27.md",
    r"results\_v3_s1_executor\rescript_2026_09_27.md",
    r"results\_v3_s2_executor\rescript_2026_09_27.md",
    r"results\_v3_s3_wordexpand_data\rescript_2026_09_28.md",
    r"results\_v3_s3_wordexpand_data\rescript_r1_2026_09_28.md",
    r"results\_v3_s_phrasetemplate_preexp_data\rescript_2026_09_27.md",
    r"results\_v4_pi_cot_v3_v3r1_rescript_2026_09_27.md",
    r"letters\_v4_walkthrough_bugfix_reply_trae_code_2026_09_27.md",
    r"letters\TRAE_V4_WALKTHROUGH_BUGFIX_REQUEST_2026_09_27.md",
    r"results\_v4_effective_register_2026_09_28.md",
    r"results\_v4_pi_cot_v3_lock_and_rejudge_register_2026_09_28.md",
    r"results\_v3_recheck_12_rj5_provenance_2026_09_27.md",
    r"results\_v3_recheck_prereg_v1p2_2026_09_27.md",
    r"results\_v3_recheck_prereg_v1p3_2026_09_27.md",
    r"results\_v3_recheck_prereg_v1p4_2026_09_27.md",
    r".tmp\_e48_docwriter_hash.py",
    r".tmp\_e48_docwriter_hash2.py",
    r".tmp\_e48_docwriter_enum.py",
    r".tmp\_e48_probe_register.py",
]

print("rel\tsha12\tbytes\tBOM\tCRLF")
for rel in FILES:
    p = os.path.join(ROOT, rel)
    if not os.path.isfile(p):
        print("%s\tMISSING\t-\t-\t-" % rel)
        continue
    d = open(p, "rb").read()
    print("%s\t%s\t%d\t%s\t%d" % (
        rel, hashlib.sha256(d).hexdigest()[:12].upper(), len(d),
        "BOM" if d[:3] == b"\xef\xbb\xbf" else "noBOM", d.count(b"\r\n")))
