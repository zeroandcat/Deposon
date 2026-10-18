# -*- coding: utf-8 -*-
"""_v3_review_r6_final_sha — 交付件落盘 SHA-12 汇总 + frozen 现状复核（只读）"""
import hashlib, os

REPO = r'D:\私人资料\deposon-repo'
def sha12(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]

DELIV = [
    r'letters\_v4_distillation_reply_trae_code_v3_review_2026_09_23.md',
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
]
print('=== 交付/新增件 SHA-12（落盘报值） ===')
for rel in DELIV:
    p = os.path.join(REPO, rel)
    if os.path.exists(p):
        print(f'  {sha12(p).upper()}  {os.path.getsize(p):>7}B  {rel}')
    else:
        print(f'  MISSING                     {rel}')

print()
print('=== frozen 现状（唯一 FAIL 应仍为 E-15） ===')
p = os.path.join(REPO, r'verifier\handoff\KT_ABC1_anchors_sha256_12.json')
print(f'  {sha12(p).upper()}  {os.path.getsize(p):>7}B  verifier/handoff/KT_ABC1_anchors_sha256_12.json  (frozen 期望 03C6C01F3697)')
for rel, exp in ((r'deposon_team\plugins\skill_a_p_a_60cells.py', 'B1463BB24403'),
                 (r'deposon_team\plugins\skill_b_p_c_alpha_beta.py', 'E5A299F69A22'),
                 (r'deposon_team\plugins\skill_c_p_e_3modality.py', 'E19E76C5DA7E'),
                 (r'deposon_team\plugins\skill_d_p_f_observer.py', '3E369A1F6171')):
    p = os.path.join(REPO, rel)
    s = sha12(p).upper()
    print(f'  {s}  {"MATCH" if s == exp else "DIFF "}  {rel}')
print('_r6 DONE')
