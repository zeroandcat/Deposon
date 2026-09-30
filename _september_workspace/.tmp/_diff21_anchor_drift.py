"""V5 #21 副本补丁棒 · 锚版 vs 漂移版 全文 diff（只读，供归因用）。

用 difflib 生成 unified diff（不依赖 git，避免 CRLF 警告干扰）。
0 字节改动：只读两版本，输出到 stdout。
"""
import difflib
import sys

D = r"D:/私人资料/_non_upload_local_archive/scripts/scripts/kt_b1"
PAIRS = [
    ("boss_b1_sinkhorn_ot.py.bak", "boss_b1_sinkhorn_ot.py"),
    ("boss_b2_kd.py.bak", "boss_b2_kd.py"),
    ("boss_b3_llmlingua.py.bak", "boss_b3_llmlingua.py"),
]


def read(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().splitlines(keepends=True)


for a, b in PAIRS:
    la = read(f"{D}/{a}")
    lb = read(f"{D}/{b}")
    print(f"###DIFF### {a} -> {b}")
    diff = list(difflib.unified_diff(la, lb, fromfile=a, tofile=b, n=3))
    if not diff:
        print("(identical)")
    else:
        sys.stdout.writelines(diff)
    print(f"###ENDFILE### lines {len(la)} -> {len(lb)}")
