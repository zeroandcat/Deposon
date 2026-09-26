# -*- coding: utf-8 -*-
"""v16 post-append SHA self-check.

Verifies:
  1. Full file SHA-12 + bytes post-append
  2. Prefix 158,079 B SHA-12 = 6844BF36F762 (v15 末态不变证据)
  3. Last line = new v16 closing line
"""
import hashlib, os, sys

F = 'D:\\私人资料\\deposon-repo\\docs\\V3X\\TRAE_V3_ASSET_ERRATUM_2026_09_23.md'
size = os.path.getsize(F)
with open(F, 'rb') as fh:
    raw = fh.read()

# full sha12
full_sha256 = hashlib.sha256(raw).hexdigest().upper()
full_sha12 = full_sha256[:12]

# prefix SHA12 on first 158079 bytes
prefix = raw[:158079]
prefix_sha256 = hashlib.sha256(prefix).hexdigest().upper()
prefix_sha12 = prefix_sha256[:12]

# last 3 lines
bom3 = raw[:3].hex().upper()

# decode last 600 bytes utf-8 (tail)
tail = raw[-600:].decode('utf-8', errors='replace')

print(f"file_len          = {size}")
print(f"file_full_sha256  = {full_sha256}")
print(f"file_full_sha12   = {full_sha12}")
print(f"prefix_158079_sha12 = {prefix_sha12}  (expect = 6844BF36F762)")
print(f"prefix_match_v15  = {prefix_sha12 == '6844BF36F762'}")
print(f"bom3              = {bom3}  (expect = efbbbf if BOM or 任意 if no BOM)")
print()
print("--- last 600 bytes (decoded) ---")
print(tail)
print("--- end tail ---")

# Count lines
n_lines = raw.count(b"\n")
print(f"\nnewlines_count    = {n_lines}")

# Check v15 末行 remains unchanged (前 158079 字节 sha 应等于 6844BF36F762)
