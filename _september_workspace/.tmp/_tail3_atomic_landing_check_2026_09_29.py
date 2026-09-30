# -*- coding: utf-8 -*-
"""[尾 3 件修订棒] 落盘核验 + 报告声明值对账 + 0 触动终检"""
import hashlib
import sys
from pathlib import Path

REPO = Path(r"D:\私人资料\deposon-repo")


def s12(rel):
    return hashlib.sha256((REPO / rel).read_bytes()).hexdigest()[:12]


PRODUCTS = [
    ("results/_v4_supp_t15_executor_r0_atomic_2026_09_29.py", "7da23c0e94cf"),
    ("results/_v4_supp_t15r2_executor_r0_atomic_2026_09_29.py", "678032f726a8"),
    ("results/_archive_2026_09_24/l14_runner_v2_r1_atomic_2026_09_29.py", "b1923528ab84"),
]
REPORT = "results/_v5_checkpoint_tail3_revision_2026_09_29.md"
UNTOUCHED = [
    ("results/_v4_supp_t15_executor.py", "558e635f9ba6"),
    ("results/_v4_supp_t15r2_executor.py", "4b5b720d5cda"),
    ("results/_archive_2026_09_24/l14_runner_v2.py", "acf1cd6ccbd4"),
    ("results/_v4_supp_t15_executor_r1_2026_09_27.py", "6d22444c65af"),
    ("results/_v4_supp_t15_executor_r2_atomic_2026_09_28.py", "9e89e021ea03"),
    ("results/_v4_supp_t15_executor_r3_2026_09_28.py", "b86cce242abe"),
    ("results/_v4_supp_t15r2_executor_r1_2026_09_28.py", "e0936a68fa82"),
    ("results/_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py", "215db16a0556"),
    ("results/_v4_supp_t15r2_executor_r3_2026_09_28.py", "4f514b3fb4b8"),
    ("results/_v4_checkpoint_atomic_and_pycache_2026_09_28.md", "52b3dec13e06"),
    ("results/_v4_exec_surface_switch_2026_09_28.md", "3bc852e0d48b"),
    ("deposon_team/plugins/_v4_wide_s5_prescan_2026_09_27.py", None),
    ("docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md", None),
]

ok = True
print("=== A. 4 件产物落盘核验 (bytes / sha12 / CR / BOM) ===")
for rel in [p for p, _ in PRODUCTS] + [REPORT]:
    b = (REPO / rel).read_bytes()
    print(f"  {len(b):>7} B  {s12(rel)}  CR={b.count(bytes([13]))}  "
          f"BOM={b[:3] == bytes([239, 187, 191])}  {rel}")

print()
print("=== B. 报告内声明 SHA-12 vs 盘上实测 ===")
rep = (REPO / REPORT).read_text(encoding="utf-8")
for rel, claim in PRODUCTS:
    got = s12(rel)
    hit = got == claim
    ok &= hit
    print(f"  claim={claim} disk={got} match={hit} claim_in_report={claim in rep}  {rel}")

print()
print("=== C. 0 触动终检 (登记件落盘后再复算) ===")
for rel, exp in UNTOUCHED:
    got = s12(rel)
    if exp is None:
        print(f"  ----  {got}  (既有引用件, 0 需期望值)  {rel}")
        continue
    hit = got == exp
    ok &= hit
    print(f"  {'OK  ' if hit else 'FAIL'} {got} expect={exp}  {rel}")

print()
print("=== D. 沙箱已清走? ===")
print(f"  .tmp/_tail3_scratch exists = {(REPO / '.tmp' / '_tail3_scratch').exists()}")
print()
print("FINAL:", "ALL OK" if ok else "MISMATCH FOUND")
sys.exit(0 if ok else 1)
