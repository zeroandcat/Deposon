# -*- coding: utf-8 -*-
"""_dfr_s2 — D 族精确原文补抽（只读）"""
import hashlib, os, re
from pathlib import Path
REPO = Path(r'_repo_mirror'); SUB = Path(r'_repo_mirror')
def sha12b(b): return hashlib.sha256(b).hexdigest()[:12]
def find(fn):
    for root in (REPO, SUB):
        for dp, dns, fns in os.walk(root):
            dns[:] = [d for d in dns if d not in {'__pycache__', '.git', '.trae', '〔归档区〕'}]
            if fn in fns:
                p = os.path.join(dp, fn); b = open(p, 'rb').read()
                return p, sha12b(b), len(b), b
    return None

def grab(fn, pats, ctx=0, limit=8):
    r = find(fn)
    if not r: print(f'  [{fn}] 0 命中'); return
    p, s, n, b = r
    t = b.decode('utf-8', 'ignore')
    ls = t.splitlines()
    hits = 0
    for i, ln in enumerate(ls):
        if any(re.search(pat, ln) for pat in pats):
            hits += 1
            print(f'  [{os.path.basename(fn)}] L{i+1}: {ln.strip()[:200]}')
            if hits >= limit: return

print('=== D-6 · L171 时序块原文 + 判死线本体 stat ===')
grab('_s6doubleprime_terminal_verdicts_2026_10_11.md', [r'14:03:16', r'全部为本棒实测', r'本棒实测'], limit=8)
r = find('_s4_kex_killline_freeze_2026_10_10.md')
if r:
    import datetime
    st = os.stat(r[0])
    print(f'  判死线本体 stat: mtime={datetime.datetime.fromtimestamp(st.st_mtime)}  ctime={datetime.datetime.fromtimestamp(st.st_ctime)}  {r[1]}/{r[2]:,}B')

print()
print('=== D-10 · 轮53卡号 + 补正件 ===')
grab('_questionnaire_cards_intake_register_supplement_7_2026_10_10.md', [r'ask_9bb02f1b', r'轮53', r'轮 53'], limit=6)
grab('_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md', [r'若存在', r'确实存在', r'ask_9bb02f1b'], limit=6)

print()
print('=== D-12 · §1 四处指纹漂移逐处 ===')
grab('_registry_lag_correction_batch_2026_10_01.md', [r'26_preexp_report', r'26b_rescript', r'c3_reading_b_prereg', r'bulk_activation', r'旧值'], limit=14)
print('  -- 37 版勘误链件定位 --')
grab('TRAE_V3_ASSET_ERRATUM_2026_09_23.md', [r'v3[1-7]|v37|37 版'], limit=3)

print()
print('=== D-14 · 17168119eccc 锚件定位 ===')
for root in (REPO, SUB):
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in {'__pycache__', '.git', '.trae', '〔归档区〕'}]
        for fn in fns:
            if not fn.endswith(('.md', '.json')): continue
            q = os.path.join(dp, fn)
            try:
                if os.path.getsize(q) > 12_000_000: continue
                t = open(q, 'rb').read().decode('utf-8', 'ignore')
            except Exception: continue
            if '17168119eccc' in t:
                print(f'  含 "17168119eccc": {q.replace("〔本地绝对路径·脱敏略:�〕�人资料\\", "")}')
                for i, ln in enumerate(t.splitlines()):
                    if '17168119eccc' in ln:
                        print(f'      L{i+1}: {ln.strip()[:180]}')

print()
print('=== D-15 · b01 L5 + e6 前言 + c5 γ-VK-1 + s4_v11 ===')
grab('_b01_recompute_sec4_2_erratum_2026_10_10.md', [r'b14_caliber', r'0 命中'], limit=4)
grab('_c5_b_group_verdict_2026_10_01.md', [r'γ-VK-1', r'_v4_piml_c5_prereg', r'_v5_v3_deg_fix_prereg'], limit=4)
r = find('_s4_v11_axis2_displacement_2026_10_11.json')
if r: print(f'  _s4_v11_axis2_displacement_2026_10_11.json: {r[1]}/{r[2]:,}B')
grab('_s4_v11_axis2_displacement_2026_10_11.json', [r'card_face_on_disk'], limit=3)

print()
print('=== D-8 · 移 723 件 + 路径失效（批2 未问但子代理有） ===')
grab('_gate_one_declared_adoption_register_2026_10_11.md', [r'results/_', r'Test-Path', r'路径'], limit=4)

print()
print('=== D-13 · 占位哈希残留宿主 ===')
r = find('_asset_identity_reconciliation_2026_10_01.md')
if r:
    print(f'  宿主: {r[1]}/{r[2]:,}B @ {r[0]}')
    t = r[3].decode('utf-8', 'ignore')
    for i, ln in enumerate(t.splitlines()):
        if 'B18FF4177289' in ln or 'post_birth_self_hash' in ln:
            print(f'      L{i+1}: {ln.strip()[:180]}')
else:
    print('  _asset_identity_reconciliation_2026_10_01.md 0 命中')

print()
print('=== D-16 · 三件分布原文（krj_all vs gate_one 互斥实锤） ===')
grab('_krj_all_terminal_verdicts_2026_10_11.md', [r'K-RJ-4.*挂账|挂账.*K-RJ-4|K-RJ-6.*全闭|全闭.*K-RJ-6', r'维持挂账 2'], limit=4)
grab('_gate_one_pi_endorsement_register_2026_10_12.md', [r'5c0efd663847', r'31e32ccc59bf'], limit=4)
print('_dfr_s2 DONE')
