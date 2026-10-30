import os, json, hashlib, re

ROOTS = {'repo': r'〔本地路径已脱敏〕', 'sub': r'〔本地路径已脱敏〕'}
V10 = r'〔本地路径已脱敏〕'
OUT = r'〔本地路径已脱敏〕'

EXEMPT = {
    '_commission_c4_values_EN_2026_10_10.md',
    '_commission_c4_values_EN_differences_exits_note_2026_10_10.md',
    '_commission_c4_values_unblock_EN_differences_exits_note_2026_10_10.md',
    '_codex_c4_values_reply_2026_10_10.md',
    '_codex_c4_values_followup_reply_2026_10_10.md',
    '_codex_c4_values_unblock_reply_2026_10_10.md',
    '_commission_eta_candidate_values_2026_10_20.md',
    '_commission_eta_candidate_values_EN_2026_10_20.md',
    '_reply_eta_candidate_values_copilot_2026_10_20.md',
    '_codex_theory_derivation_reply_2026_09_30.md',
    '_commission_glm_theory_derivation_2026_09_30.md',
    'REPLY_FROM_COPILOT_AGENT_T2_T3_THEORY_INPUTS_2026_10_17.md',
    'RECEIPT_COPILOT_AGENT_T2_T3_2026_10_17.txt',
    'REPLY_FROM_GEMINI4_GE01_THEORY_INPUTS_2026_10_15.md',
    '_commission_t5_inputs_external_EN_draft_2026_10_23.md',
    '_commission_t5_inputs_external_EN_round2_draft_2026_10_24.md',
    '_commission_pb_v0_experiment_k31_2026_10_28.md',
    '_commission_bo_three_columns_narrow_v1_2026_10_24.md',
    '_v5_rj5_external_rederive_request_2026_09_28.md',
    'verify_c4_originated_math.py',
}

# 内部册（PI 卡答：整体禁传）——不赖 22 类，独立依据
INTERNAL_PAT = [
    (r'^_experiment_tree_v2_main', '内部册:树册'),
    (r'^_root_session_history_memo_main', '内部册:主代理册'),
    (r'^_sub_agent_memo', '内部册:子代理册'),
    (r'_book_\d', '内部册:合册'),
    (r'_cardbook_', '内部册:合册'),
    (r'^_pending_pi_master', '内部册:候PI余额册'),
    (r'_remote_local_reconciliation', '内部册:对账清单'),
    (r'_repo_full_inventory_catalogue', '内部册:盘面编目'),
    (r'_repo_post_cleanup_snapshot', '内部册:盘面快照'),
    (r'^_clue_book_internal', '内部册:线索册'),
    (r'^_achievements_', '内部册:成果清单'),
    (r'_mirror_face_', '内部册:镜像面勘查'),
    (r'_closeout_bucket_refresh', '内部册:收尾桶'),
    (r'^_internal_true_clue_book', '内部册:内部真册'),
]

def judge(zone, rel, fn):
    low = rel.lower()
    if fn in EXEMPT:
        return None
    for pat, why in INTERNAL_PAT:
        if re.search(pat, fn) or re.search(pat, rel):
            return why
    if low.startswith('pi_rulings/') or '/pi_rulings/' in low:
        return 'HF-M:答卡登记族'
    if low.startswith('.mavis/') or '/.mavis/' in '/' + low:
        return '.gitignore:.mavis/'
    if low.startswith('.tmp/') or '/.tmp/' in '/' + low:
        return 'HF-J:.tmp/'
    if fn.lower().endswith('.log'):
        return '.gitignore:*.log'
    if low.startswith('letters/'):
        if 'distill' in fn.lower():
            return None
        if re.search(r'commission|letter|reply|委托|回函', fn):
            return 'S21:letters委托回函面'
        return None
    if fn.startswith('_v') and fn.endswith('_body.md'):
        return 'PROC:本部落册中间体'
    if fn.startswith('_clue_') or fn.startswith('_nonupload_union_v'):
        return 'PROC:内部过程件'
    if fn.startswith('_HANDOVER'):
        return 'PROC:内部交接件'
    return None

rows = []
for zone, root in ROOTS.items():
    for dp, _, fs in os.walk(root):
        for fn in fs:
            p = os.path.join(dp, fn)
            rel = os.path.relpath(p, root).replace('\\', '/')
            rows.append((zone, rel, fn, os.path.getsize(p)))

keep = {}
for zone, rel, fn, sz in rows:
    why = judge(zone, rel, fn)
    if why:
        keep[(zone, rel)] = {'zone': zone, 'rel': rel, 'why': [why], 'bytes': sz}

with open(OUT, 'wb') as f:
    for k in sorted(keep):
        f.write(json.dumps(keep[k], ensure_ascii=False, sort_keys=True).encode('utf-8') + b'\n')

from collections import Counter
c = Counter(v['why'][0].split(':')[0] for v in keep.values())
print('V11_TOTAL', len(keep))
for k, v in c.most_common():
    print('   %-12s %3d' % (k, v))
print()
print('OUT_BYTES', os.path.getsize(OUT))
print('OUT_SHA12', hashlib.sha256(open(OUT, 'rb').read()).hexdigest()[:12])
print()
# 对照 v10
v10 = sum(1 for _ in open(V10, 'rb'))
print('V10', v10, '-> V11', len(keep), '差', len(keep) - v10)
print()
print('--- 内部册之件（前 12·按字节）---')
intr = sorted([v for v in keep.values() if v['why'][0].startswith('内部册')], key=lambda x: -x['bytes'])
for v in intr[:12]:
    print('  %9d %-14s %s' % (v['bytes'], v['why'][0].split(':')[1], v['rel'][:66]))
print('  内部册合', len(intr), '件')
