# -*- coding: utf-8 -*-
"""_v5_wa_s2 — §B.4 五条线索核验 + §C 审计面（只读）"""
import hashlib, os, re
from pathlib import Path
REPO = Path(r'D:\私人资料\deposon-repo'); RES = REPO / 'results'
ARCH = Path(r'D:\私人资料\_non_upload_local_archive')
def sha12(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]
def T(p): return Path(p).read_text(encoding='utf-8', errors='ignore')

print('=== B.5-① 混合体在盘坐实核验 ===')
p = ARCH / '_movedout_scratch_2026_09_29' / 'verif_doubt6_v_20260928' / '_v5_trae_doubt6_verify_2026_09_28.md'
print(f'  归档区件: exists={p.exists()}')
if p.exists():
    print(f'    sha12={sha12(p)}  bytes={p.stat().st_size}  (委托记 ffda214d1917 / 51,778)')
r3 = RES / '_v5_trae_doubt6_verify_2026_09_28_r3verifier.md'
print(f'  r3verifier: exists={r3.exists()}  sha12={sha12(r3)}  bytes={r3.stat().st_size}')
p2 = ARCH / '_movedout_scratch_2026_09_29' / 'verif_doubt6_v_20260928' / '_merged_canonical_snapshot_224910.md'
print(f'  _merged_canonical_snapshot_224910.md: sha12={sha12(p2)} (委托记 ffda214d1917)')

print()
print('=== B.5-② 26 件同秒簇：内容是否真变更（抽验：字节数与委托附录A登记比对）===')
CLUSTER = [
 ('letters/_v4_acceptance_trae_code_2026_09_20.md', 7746, '3e2f1c84e86d'),
 ('letters/_v4_distillation_invitation_2026_09_20_v1.0.md', 54784, 'e4b00fa97d03'),
 ('results/_v3_recheck_01_rescript_2026_09_27.md', 14541, 'a3c95102290f'),
 ('results/_v3_recheck_verdict_register_2026_09_27.md', 112085, 'd9b6b974cfc1'),
 ('results/_v4_supp_t1_verdict.md', 29106, '0ad42625f333'),
 ('results/_v4_evidence_audit_reconcile_2026_09_26.md', 24168, 'fe907046eda1'),
 ('results/_v3_v4_achievements_inventory_2026_09_24.md', 194083, '965db22e9130'),
]
n_same = n_diff = 0
for rel, sz, s12 in CLUSTER:
    p = REPO / rel
    if not p.exists(): print(f'  MISSING {rel}'); continue
    a = sha12(p); z = p.stat().st_size
    same = (a == s12 and z == sz)
    n_same += same; n_diff += (not same)
    print(f'  {"一致" if same else "漂移"}  {a} {z} (记 {s12}/{sz})  {rel}')
print(f'  抽验 7 件：一致 {n_same} / 漂移 {n_diff}')

print()
print('=== B.5-③ 并发写入 7 件现行值 ===')
SEVEN = [
 ('results/_v5_bulk_activation_2026_09_28.md', 'b5a50447b4da', 39378),
 ('results/_v5_trae_doubt6_verify_2026_09_28_r3verifier.md', '58101ef93a6f', 30192),
 ('results/_v5_sub_artifact_ledger_2026_09_28.md', 'dd38c77ea486', 71818),
 ('results/_v5_fake_verdict_v1x_prereg_2026_09_28.md', '088085d6c90d', 28484),
 ('results/_v5_c3_reading_b_prereg_2026_09_28.md', '8dcf5e1e6dde', 32178),
 ('results/_v5_closing_register_2026_09_28.md', '522b08506290', 27224),
 ('results/_v5_fake_verdict_session_log_2026_09_28.md', '132bfa0c02f5', 18877),
]
for rel, s12, sz in SEVEN:
    p = REPO / rel
    a = sha12(p); z = p.stat().st_size
    print(f'  {"OK " if (a==s12 and z==sz) else "CHG"}  {a} {z} (记 {s12}/{sz})  {os.path.basename(rel)}')

print()
print('=== B.5-⑤ 0 覆盖自检（盘上是否有未被清单覆盖的 mtime>B0 新件）===')
# 与委托附录 A/B/C 比对：本件以委托附录路径集合为参照
# 委托附录 repo 443 + sub 16 + 归档 115 = 574；本棒实测 571
# 列出本棒实测中「不在委托附录」的件（按文件名粗对）
from datetime import datetime
B0 = datetime(2026,9,27,20,28,20).timestamp()
commissioned = set()
for base, n in ((REPO, 443), ):
    pass
# 简化：取委托附录A/B/C 中的 basename 集合（从委托件文本抽）
com = Path(r'D:\私人资料\deposon-repo\letters\TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md').read_text(encoding='utf-8')
names = set(re.findall(r'\|\s*\d+\s*\|\s*`([^`]+)`\s*\|', com))
print(f'  委托附录表行抽取 basename {len(names)} 个')
EXCL = ('.evidence_backup_2026_09_28', '.evidence_backup_2026_09_30', '_movedout_scratch_2026_09_30')
miss = []
for area in (r'D:\私人资料\deposon-repo', r'D:\私人资料\deposon-sub', r'D:\私人资料\_non_upload_local_archive'):
    for dp, dns, fns in os.walk(area):
        dns[:] = [d for d in dns if d not in {'__pycache__','.git','.trae','.mavis'}]
        if any(x in dp for x in EXCL): continue
        for fn in fns:
            q = os.path.join(dp, fn)
            try: st = os.stat(q)
            except OSError: continue
            if st.st_mtime > B0 and fn not in names:
                miss.append((q.replace(r'D:\私人资料'+os.sep,''), st.st_size, datetime.fromtimestamp(st.st_mtime).strftime('%m-%d %H:%M')))
print(f'  实测有而附录表行未含（按 basename 匹配）= {len(miss)} 件：')
for m in miss[:30]:
    print(f'      {m}')
print(f'  （其余 {max(0,len(miss)-30)} 件从略）')

print()
print('=== §C.1 C4.1/C4.6 现状复算 ===')
p = REPO / 'tools' / 'distortion_calculator.py'
print(f'  C4.1 tools/distortion_calculator.py: exists={p.exists()}')
p2 = REPO / 'verifier' / 'handoff' / 'P_B_V0_anchors_sha256_12.json'
print(f'  C4.6 verifier/handoff/P_B_V0_anchors_sha256_12.json: exists={p2.exists()}')
vh = sorted(os.listdir(REPO / 'verifier' / 'handoff'))
print(f'  verifier/handoff/ 现有 {len(vh)} 件: {vh}')

print()
print('=== §C.2③ 5 锚可解析性（P-B spec bb7ca9838150）===')
# 找 P_B spec
cands = list(RES.glob('*P_B*')) + list((REPO/'docs').rglob('*P_B*')) + list((REPO/'docs'/'V3X').glob('*P_B*'))
print(f'  P_B spec 候选: {[str(c) for c in cands]}')
pbl = REPO / 'tools' / 'llm_client.py'
if pbl.exists():
    t = T(pbl)
    print(f'  tools/llm_client.py: sha12={sha12(pbl)} {pbl.stat().st_size}B  含 version 字面: {[l for l in t.splitlines()[:20] if "version" in l.lower() or "2026-09-11" in l][:3]}')
gts = sorted((RES).glob('deposon_v20_gt*.json'))
print(f'  results/deposon_v20_gt*.json = {len(gts)} 件: {[g.name for g in gts]}')
print()
print('_wa_s2 DONE')
