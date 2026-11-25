import os, json, hashlib, re

ROOTS = {'repo': r'〔本地路径已脱敏〕', 'sub': r'〔本地路径已脱敏〕'}
V9 = r'〔本地路径已脱敏〕'
OUT = r'〔本地路径已脱敏〕'

# §20-4 理论值面（可传）＋ PI 令「蒸馏 LLM 件仍上传」
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

base = {}
for line in open(V9, 'rb'):
    line = line.strip()
    if not line:
        continue
    r = json.loads(line.decode('utf-8'))
    p = os.path.join(ROOTS[r['zone']], r['rel'].replace('/', os.sep))
    if os.path.isfile(p):
        base[(r['zone'], r['rel'])] = r

def judge(zone, rel, fn):
    low = rel.lower()
    if fn in EXEMPT:
        return None
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
            return None          # PI 令：蒸馏 LLM 件仍上传
        if re.search(r'commission|letter|reply|委托|回函', fn):
            return 'S21:letters委托回函面'
        return None
    if fn.startswith('_v') and fn.endswith('_body.md'):
        return 'PROC:本部落册中间体'
    if fn.startswith('_clue_') or fn.startswith('_nonupload_union_v'):
        return 'PROC:内部过程件'
    if fn.startswith('_delivery_list_'):
        return None
    if fn.startswith('README'):
        return None
    if fn.startswith('_HANDOVER'):
        return 'PROC:内部交接件'
    return None

added, kept, newpass = [], 0, []
for zone, root in ROOTS.items():
    for dp, _, fs in os.walk(root):
        for fn in fs:
            p = os.path.join(dp, fn)
            rel = os.path.relpath(p, root).replace('\\', '/')
            sz = os.path.getsize(p)
            k = (zone, rel)
            if k in base:
                kept += 1
                continue
            why = judge(zone, rel, fn)
            if why:
                base[k] = {'zone': zone, 'rel': rel, 'why': [why], 'bytes': sz}
                added.append((why, zone, rel, sz))
            else:
                newpass.append((zone, rel, sz))

with open(OUT, 'wb') as f:
    for k in sorted(base):
        f.write(json.dumps(base[k], ensure_ascii=False, sort_keys=True).encode('utf-8') + b'\n')

from collections import Counter
c = Counter(a[0] for a in added)
print('V9_ON_DISK', kept)
print('NEWLY_BLOCKED', len(added))
for k, v in c.most_common():
    print('   %-28s %3d' % (k, v))
print('NEWLY_PASSABLE', len(newpass))
print('V10_TOTAL', len(base))
print('OUT_BYTES', os.path.getsize(OUT))
print('OUT_SHA12', hashlib.sha256(open(OUT, 'rb').read()).hexdigest()[:12])
print()
print('--- 新判入者（按字节前 12）---')
for why, zone, rel, sz in sorted(added, key=lambda x: -x[3])[:12]:
    print('  %9d %-5s %-22s %s' % (sz, zone, why.split(':')[0], rel[:70]))
