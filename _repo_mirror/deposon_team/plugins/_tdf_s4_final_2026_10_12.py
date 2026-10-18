# -*- coding: utf-8 -*-
"""_tdf_s4_final — 终验：交付件 SHA + 追加件前缀自证 + 守护件（只读）"""
import hashlib
from pathlib import Path
REPO = Path(r'D:\私人资料\deposon-repo')
def sha12b(b): return hashlib.sha256(b).hexdigest()[:12]

print('=== 交付件 ===')
for rel, _ in [('letters/_trae_direct_fix_reply_trae_code_2026_10_12.md', 0),
               ('results/_v3_recheck_08c_preexp_data/_v3_recheck_08c_sha12fix_r1_2026_10_12.py', 0)]:
    p = REPO / rel
    b = p.read_bytes()
    print(f'  {sha12b(b).upper()}  {len(b):>7,}B  {rel}')

print()
print('=== 追加 3 件前缀自证 ===')
CASES = [
 ('results/_v3_s2_executor/rescript_2026_09_27.md', 23039, '331022480a57'),
 ('results/_v3_s_phrasetemplate_preexp_data/rescript_2026_09_27.md', 14510, '6df402298557'),
 ('results/_v3_recheck_08c_preexp_data/rescript_2026_09_27.md', 15211, 'aa02cbfc84e3'),
]
for rel, n, pre in CASES:
    b = (REPO / rel).read_bytes()
    ok = sha12b(b[:n]) == pre
    print(f'  {"OK " if ok else "FAIL"}  前 {n:,} B prefix = {sha12b(b[:n])}（记 {pre}）  全件 = {sha12b(b)} / {len(b):,} B')

print()
print('=== 守护件（本棒前后未变） ===')
G = [('verifier/handoff/KT_ABC1_anchors_sha256_12.json', '03c6c01f3697'),
     ('results/_v4_pi_cot_v3_ruleset_v3_executor.py', '8a81d90c69ba'),
     ('results/_v4_pi_cot_v3_result_v3.json', '585714f9660c'),
     ('results/_v4_pi_cot_v3_ruleset_v3.json', '9d77a5e2cbab'),
     ('docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md', '41f5f1689d09'),
     ('results/_v3_recheck_08b_executor/executor_2026_09_27.py', 'b292410d9a69'),
     ('results/_v3_recheck_08c_preexp_data/executor_2026_09_27.py', 'cb6eb9164df3'),
     ('results/_v3_recheck_08c_preexp_data/result_2026_09_27.json', '689a6e4427a8'),
     ('results/_v5_trae_doubt6_verify_2026_09_28_r3verifier.md', '58101ef93a6f'),
     ('results/_trae_sixitem_disposal_and_collision_register_2026_10_01.md', '545b17d403be'),
     ('results/_trae_errata_sha_drift_attribution_2026_10_01.md', '6d5836cc6d3a'),
     ('letters/_walkthrough_bugfix_audit_reply_trae_code_2026_09_30.md', '5bfc26bbaa41'),
     ('results/_v4_supp_t15r2_verdict.md', '963725dbd82a'),
     ('results/_v3_recheck_26b_rescript_2026_09_27.md', 'ae81d9b59054'),
     ('results/_v3_s2_executor/result_2026_09_27.json', 'd73d51e670de'),
     ('tools/llm_client.py', '1722500da4aa'),
     ('docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md', '423c84de20d5'),
     ]
ok = 0
for rel, exp in G:
    p = REPO / rel
    a = sha12b(p.read_bytes()) if p.exists() else 'MISSING'
    ok += (a == exp)
    print(f'  {"OK " if a==exp else "CHG"}  {a} (记 {exp})  {rel}')
print(f'  ⇒ 未变 {ok}/{len(G)}')
print('_tdf_s4 DONE')
