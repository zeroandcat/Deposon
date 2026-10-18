# -*- coding: utf-8 -*-
"""_tdf_s3_jumps — 项 7 三跳点独立复算（只读）"""
import hashlib
from pathlib import Path
REPO = Path(r'_september_workspace')
b = (REPO / 'docs' / 'V3X' / 'TRAE_V3_ASSET_ERRATUM_2026_09_23.md').read_bytes()
def psha(n): return hashlib.sha256(b[:n]).hexdigest()[:12]
JUMPS = [(327975, '62eed1f4dfa0', 'v24 末态'), (360692, '8c8610ced9fa', 'v25'), (407284, 'aed375c485fb', 'v26')]
for n, exp, name in JUMPS:
    a = psha(n)
    print(f'  {name}: 前 {n:,} B prefix SHA-12 = {a}  期望 {exp}  {"MATCH" if a == exp else "DIFF"}')
print(f'  当前全件: {hashlib.sha256(b).hexdigest()[:12]} / {len(b):,} B')
print('_tdf_s3 DONE')
