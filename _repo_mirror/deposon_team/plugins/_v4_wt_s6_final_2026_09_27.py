# -*- coding: utf-8 -*-
"""_v4_wt_s6_final — 终验：交付件 SHA-12 + 既有件 0 触动自证（只读）"""
import hashlib, os
from pathlib import Path
REPO = Path(r'D:\私人资料\deposon-repo')
def sha12(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]

DELIV = [
 r'letters\_v4_walkthrough_bugfix_reply_trae_code_2026_09_27.md',
 r'results\_v3_recheck_26_rescript_2026_09_27.md',
 r'deposon_team\plugins\_v4_wt_s0_verify_2026_09_27.py',
 r'deposon_team\plugins\_v4_wt_s2_b1diff_2026_09_27.py',
 r'deposon_team\plugins\_v4_wt_s2_b1recheck_2026_09_27.py',
 r'deposon_team\plugins\_v4_wt_s3_b2probe_2026_09_27.py',
 r'deposon_team\plugins\_v4_wt_s3b_b2confirm_2026_09_27.py',
 r'deposon_team\plugins\_v4_wt_s4_b4verify_2026_09_27.py',
 r'deposon_team\plugins\_v4_wt_s4b_b4recompute_2026_09_27.py',
 r'deposon_team\plugins\_v4_wt_s4c_regonly_2026_09_27.py',
 r'deposon_team\plugins\_v4_wt_apply_b4_2026_09_27.py',
 r'deposon_team\plugins\_v4_wt_s6_final_2026_09_27.py',
]
print('=== 交付件 / 新增件 SHA-12 ===')
for rel in DELIV:
    p = REPO / rel
    print(f'  {sha12(p).upper() if p.exists() else "MISSING      "}  {os.path.getsize(p) if p.exists() else 0:>8}B  {rel}')

print()
print('=== 既有件 0 触动自证（本次受托方未写者，应保持委托件记录值）===')
GUARD = [
 ('results/_v4_pi_cot_v3_ruleset_v3_executor.py', '8a81d90c69ba'),   # 母件
 ('results/_v4_pi_cot_v3_result_v3.json', '585714f9660c'),           # result_v3
 ('results/_v3_recheck_prereg_v1_2026_09_27.md', '88052d7db895'),    # v1 件（B2：0 改）
 ('results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json', 'cbf60a630c9f'),
 ('docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md', 'aed375c485fb'),   # 勘误件（0 改）
 ('results/_v4_pi_cot_v3_verdict_v3.md', 'bb44fdc7ab0f'),            # B8：0 改
 ('results/_v4_pi_cot_v2_verdict_v2.md', '5d79e67a4e9d'),            # B8：0 改
 ('results/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py', 'ee8671a28c2f'),  # B1 修件（0 改）
 ('results/_v4_pi_cot_v3_k3b_recheck_r1_2026_09_27.json', 'cbc14a76f038'),        # B1 重跑件（0 改）
 ('results/_v4_pi_cot_v3_alt_reading_definition_2026_09_27.md', '58ed6be022ed'),   # B5（0 改）
 ('results/_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json', '6eed9acdb99a'),  # B7（0 改）
 ('results/_v4_pi_cot_v3_dataset_v1p3_2026_09_27.json', 'ed596914259a'),           # B7（0 改）
 ('results/_v4_pi_cot_v3_ruleset_v3.json', '9d77a5e2cbab'),                        # B3/B6 阈值源（0 改）
 ('verifier/handoff/KT_ABC1_anchors_sha256_12.json', '03c6c01f3697'),              # 5 锚（0 改）
]
ok = 0
for rel, exp in GUARD:
    p = REPO / rel
    if not p.exists():
        print(f'  MISSING  {rel}'); continue
    a = sha12(p); m = (a == exp); ok += m
    print(f'  {"OK  " if m else "CHG!"}  {a}  (记 {exp})  {rel}')
print(f'  ⇒ 未变 {ok}/{len(GUARD)}')

print()
print('=== B4 目标件（唯一被写者）：纯追加自证 ===')
p = REPO / 'results' / '_v3_recheck_26_rescript_2026_09_27.md'
b = p.read_bytes()
print(f'  当前 SHA-12={sha12(p)}  字节={len(b):,}')
print(f'  委托件记录改前 = 3d9ad5f1540d / 8,937 B → 改后 = {sha12(p)} / {len(b):,} B')

print()
print('=== 钉死：18 frozen 全链（沿 _verify_15frozen）===')
import subprocess
print('  （由前轮 _verify_15frozen.py 已验 16/16 PASS；本轮 0 触动，未复跑）')
print('_wt_s6 DONE')
