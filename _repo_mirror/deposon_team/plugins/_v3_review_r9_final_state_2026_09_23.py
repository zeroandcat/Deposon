# -*- coding: utf-8 -*-
"""_v3_review_r9_final_state — 终态汇总：交付件 SHA-12 + frozen 终验（只读）"""
import hashlib, os

REPO = r'D:\私人资料\deposon-repo'
def sha12(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]

FILES = [
    r'letters\_v4_distillation_reply_trae_code_v3_review_2026_09_23.md',
    r'letters\_v4_distillation_reply_trae_code_v3_review_2026_09_23_fix_addendum.md',
    r'docs\V3X\TRAE_V3_ASSET_ERRATUM_2026_09_23.md',
    r'deposon_team\plugins\_v3_review_r1_inventory_2026_09_23.py',
    r'deposon_team\plugins\_v3_review_r1b_2026_09_23.py',
    r'deposon_team\plugins\_v3_review_r1c_2026_09_23.py',
    r'deposon_team\plugins\_v3_review_r1d_2026_09_23.py',
    r'deposon_team\plugins\_v3_review_r2_verify_2026_09_23.py',
    r'deposon_team\plugins\_v3_review_r2b_2026_09_23.py',
    r'deposon_team\plugins\_v3_review_r2c_2026_09_23.py',
    r'deposon_team\plugins\_v3_review_r3_sha_2026_09_23.py',
    r'deposon_team\plugins\_v3_review_r4_fixscan_2026_09_23.py',
    r'deposon_team\plugins\_v3_review_r5_anchor_probe_2026_09_23.py',
    r'deposon_team\plugins\_v3_review_r6_final_sha_2026_09_23.py',
    r'deposon_team\plugins\_v3_review_r7_fix_e15_2026_09_23.py',
    r'deposon_team\plugins\_v3_review_r8_precise_scan_2026_09_23.py',
    r'deposon_team\plugins\_v3_review_r9_final_state_2026_09_23.py',
    r'verifier\handoff\KT_ABC1_anchors_sha256_12.json',
    r'verifier\handoff\KT_ABC1_anchors_sha256_12.root_session_11318B.bak_2026_09_23.json',
]
print('=== 终态 SHA-12 汇总（2026-09-23「直接修正」完成后） ===')
for rel in FILES:
    p = os.path.join(REPO, rel)
    if os.path.exists(p):
        print(f'  {sha12(p).upper()}  {os.path.getsize(p):>7}B  {rel}')
    else:
        print(f'  MISSING                     {rel}')
print()
print('=== frozen 终验锚点 ===')
p = os.path.join(REPO, r'verifier\handoff\KT_ABC1_anchors_sha256_12.json')
s = sha12(p)
print(f'  主路径 5 锚根件: {s.upper()}  (期望 03C6C01F3697)  {"MATCH -> 16/16 PASS" if s == "03c6c01f3697" else "MISMATCH"}')
print('_r9 DONE')
