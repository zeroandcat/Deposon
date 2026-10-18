# -*- coding: utf-8 -*-
"""_dfr_s1 — D 族 7+2 项宿主件现值机验（repo/sub 两面；只读；归档区 0 触）"""
import hashlib, os
from pathlib import Path
REPO = Path(r'_repo_mirror'); SUB = Path(r'_repo_mirror')
def sha12b(b): return hashlib.sha256(b).hexdigest()[:12]

TARGETS = {
 'D-2 宿主': ['_round56_review_effectivity_register_3_2026_10_10.md'],
 'D-2 勘误': ['_register3_bytes_erratum_2026_10_11.md'],
 'D-6 宿主': ['_s6doubleprime_terminal_verdicts_2026_10_11.md'],
 'D-6 勘误': ['_s7doubleprime_verification_erratum_2026_10_11.md'],
 'D-6 判死线本体': ['_s4_kex_killline_freeze_2026_10_10.md'],
 'D-10 宿主': ['_questionnaire_cards_intake_register_supplement_7_2026_10_10.md'],
 'D-10 补正': ['_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md'],
 'D-12 宿主': ['_registry_lag_correction_batch_2026_10_01.md'],
 'D-14 宿主(勘误件)': ['_commission_closeout_erratum_and_supplement_2026_10_11.md'],
 'D-14 R-2 委托件': ['_commission_pending_pi_gaps_closeout_EN_2026_10_11.md'],
 'D-15 样本1': ['_v5_confirm_b1_decisions_register_2026_09_29.md'],
 'D-15 样本2': ['_b01_recompute_sec4_2_erratum_2026_10_10.md'],
 'D-16 件1': ['_krj_all_terminal_verdicts_2026_10_11.md'],
 'D-16 件2': ['_gate_one_pi_endorsement_register_2026_10_12.md'],
 'D-16 件3(权威分布)': ['_f4b1... 无此', '_krj_cond4_effectivity_declaration_2026_10_11.md'],
 'D-16 件4': [],
 'D-8 关联(移723件)': ['_v4_closeout_bulk_reorganize_register_2026_10_12.md'],
}
# 额外多别名候选
EXTRA = {
 'D-16': ['_gate_one_declared_adoption_register_2026_10_11.md', '_s6d_terminal_verdicts_2026_10_11.md'],
}
def find(fn):
    for root in (REPO, SUB):
        for dp, dns, fns in os.walk(root):
            dns[:] = [d for d in dns if d not in {'__pycache__', '.git', '.trae', '_non_upload_local_archive'}]
            if fn in fns:
                p = os.path.join(dp, fn)
                b = open(p, 'rb').read()
                return (p.replace('〔本地资料区〕\\', ''), sha12b(b), len(b))
    return None

print('=== D 族宿主件现值（repo/sub 两面实测） ===')
for tag, names in TARGETS.items():
    for fn in names:
        if fn.startswith('_f4b1') or fn == '_krj_cond4_effectivity_declaration_2026_10_11.md':
            r = find(fn)
            print(f'  [{tag}] {fn}: {r if r else "两面0命中"}')
        else:
            r = find(fn)
            print(f'  [{tag}] {fn}: {("OK " + r[1] + " / " + str(r[2]) + "B @ " + r[0]) if r else "两面 0 命中"}')
for tag, names in EXTRA.items():
    for fn in names:
        r = find(fn)
        print(f'  [{tag}+] {fn}: {("OK " + r[1] + " / " + str(r[2]) + "B @ " + r[0]) if r else "两面 0 命中"}')

# D-2 须验证「五行」+ D-6 须给两端时点 + D-10 须给卡号原文 + D-14 须给两句并列 —— 读取关键行
print()
print('=== 关键原文抽取 ===')
def grab(fn, pats, ctx=2, limit=6, root_hint=None):
    r = find(fn)
    if not r:
        print(f'  [{fn}] 0 命中，跳过'); return
    p = Path(r[0].replace('deposon-repo', str(REPO), 1).replace('deposon-sub', str(SUB), 1))
    if not p.exists():
        for base in (REPO, SUB):
            q = base / fn
            if q.exists(): p = q; break
    t = p.read_text(encoding='utf-8', errors='ignore')
    ls = t.splitlines()
    hits = 0
    import re as _re
    for i, ln in enumerate(ls):
        if any(_re.search(pat, ln) for pat in pats):
            hits += 1
            print(f'  [{fn}] L{i+1}: {ln.strip()[:170]}')
            if hits >= limit: break

grab('_round56_review_effectivity_register_3_2026_10_10.md', [r'22,?431', r'26,?909', r'34,?318', r'27,?336', r'19,?845', r'25,?698', r'27,?778', r'21,?966', r'50,?079', r'24,?999'])
print()
grab('_s6doubleprime_terminal_verdicts_2026_10_11.md', [r'14:03:16', r'全部为本棒实测', r'04495ef4b343'])
print()
grab('_s4_kex_killline_freeze_2026_10_10.md', [r'04495ef4b343', r'冻结', r'2026-10-1'])
print()
grab('_questionnaire_cards_intake_register_supplement_7_2026_10_10.md', [r'若存在', r'ask_9bb02f', r'另建之他卡'])
print()
grab('_registry_lag_correction_batch_2026_10_01.md', [r'26_preexp_report', r'26b_rescript', r'c3_reading_b', r'bulk_activation', r'旧值', r'滞后'])
print()
grab('_commission_closeout_erratum_and_supplement_2026_10_11.md', [r'R-2', r'reference', r'方向登记', r'漏列'])
print()
grab('_commission_pending_pi_gaps_closeout_EN_2026_10_11.md', [r'R-2', r'pointing', r'方向登记'])
print()
grab('_v5_confirm_b1_decisions_register_2026_09_29.md', [r'ask_8977', r'逐字', r'0 命中'])
print()
grab('_krj_all_terminal_verdicts_2026_10_11.md', [r'全闭', r'挂账', r'K-RJ-4', r'K-RJ-6'])
print()
grab('_gate_one_pi_endorsement_register_2026_10_12.md', [r'13/13', r'K-RJ-4', r'K-RJ-6', r'5c0efd663847', r'31e32ccc59bf'])
print()
print('=== mtime/ctime 抽验（D-6 两端时点） ===')
r = find('_s4_kex_killline_freeze_2026_10_10.md')
if r:
    p = None
    for base in (REPO, SUB):
        q = base / '_s4_kex_killline_freeze_2026_10_10.md'
        if q.exists(): p = q; break
    import datetime
    st = p.stat()
    print(f'  判死线本体: mtime={datetime.datetime.fromtimestamp(st.st_mtime)}  ctime={datetime.datetime.fromtimestamp(st.st_ctime)}')
print('_dfr_s1 DONE')
