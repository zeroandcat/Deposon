# -*- coding: utf-8 -*-
"""_v5_wa_s4 — 终验：交付件 SHA + 修复件自证 + 冻结链 0 触动（只读）"""
import hashlib, os
from pathlib import Path
REPO = Path(r'D:\私人资料\deposon-repo')
def sha12(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]

print('=== 交付件 / 新增件 ===')
for rel in ['letters/_walkthrough_bugfix_audit_reply_trae_code_2026_09_30.md',
            'results/_plan_v3_pending_verify_2026_09_30.md']:
    p = REPO / rel.replace('/', os.sep)
    print(f'  {sha12(p).upper()}  {p.stat().st_size:>8,}B  {rel}')

print()
print('=== 修复件纯追加自证 ===')
p = REPO / 'results' / '_plan_v3_pending_verify_2026_09_30.md'
b = p.read_bytes()
print(f'  当前 {sha12(p)} / {len(b):,} B（改前 4ba2ca44d8f7 / 39,193 B → 改后 {sha12(p)}）')
print(f'  尾部含附录A标记: {"附录 A · 勘误注记" in b.decode("utf-8")}')

print()
print('=== 冻结链 / 判定层 / 并发写入 7 件 0 触动 ===')
GUARD = [
 ('verifier/handoff/KT_ABC1_anchors_sha256_12.json', '03c6c01f3697'),
 ('results/_v4_pi_cot_v3_ruleset_v3_executor.py', '8a81d90c69ba'),
 ('results/_v4_pi_cot_v3_result_v3.json', '585714f9660c'),
 ('deposon_team/plugins/skill_a_p_a_60cells.py', 'b1463bb24403'),
 ('results/_v5_bulk_activation_2026_09_28.md', 'b5a50447b4da'),
 ('results/_v5_trae_doubt6_verify_2026_09_28_r3verifier.md', '58101ef93a6f'),
 ('results/_v5_sub_artifact_ledger_2026_09_28.md', 'dd38c77ea486'),
 ('results/_v5_fake_verdict_v1x_prereg_2026_09_28.md', '088085d6c90d'),
 ('results/_v5_c3_reading_b_prereg_2026_09_28.md', '8dcf5e1e6dde'),
 ('results/_v5_closing_register_2026_09_28.md', '522b08506290'),
 ('results/_v5_fake_verdict_session_log_2026_09_28.md', '132bfa0c02f5'),
 ('docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md', 'bb7ca9838150'),
]
ok = 0
for rel, exp in GUARD:
    p = REPO / rel.replace('/', os.sep)
    a = sha12(p) if p.exists() else 'MISSING'
    ok += (a == exp)
    print(f'  {"OK " if a==exp else "CHG"}  {a} (记 {exp})  {rel}')
print(f'  ⇒ 未变 {ok}/{len(GUARD)}')
print('_wa_s4 DONE')
