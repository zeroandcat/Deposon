# -*- coding: utf-8 -*-
import hashlib, io, os, sys, time

sys.stdout.reconfigure(encoding='utf-8')

REPO = r'_repo_mirror'
GLM = r'〔本地资料区〕\GLM'

def fp(p):
    b = io.open(p, 'rb').read()
    return {
        'sha12': hashlib.sha256(b).hexdigest()[:12],
        'bytes': len(b),
        'lf': b.count(b'\n'),
        'bom': 1 if b.startswith(b'\xef\xbb\xbf') else 0,
        'crlf': b.count(b'\r\n'),
        'fffd': b.decode('utf-8', 'replace').count('\ufffd'),
    }

print('=== A. FILE FINGERPRINTS (direct measure) ===')
targets = [
    os.path.join(REPO, 'results', '_c5_split_into_c5a_c5b_2026_10_17.md'),
    os.path.join(REPO, 'letters', '_commission_t2_t3_theory_inputs_copilot_agent_2026_10_17.md'),
    os.path.join(REPO, 'letters', '_commission_t2_t3_theory_inputs_grok_2026_10_17.md'),
]
for t in targets:
    print(os.path.relpath(t, REPO), '| exists=', os.path.exists(t), '|', fp(t) if os.path.exists(t) else 'N/A')

print()
print('=== B. TARGET PATH OCCUPANCY ===')
tp = os.path.join(REPO, 'results', '_copilot_agent_t2_t3_reply_register_2026_10_17.md')
print('target=', tp)
print('Test-Path equivalent exists=', os.path.exists(tp))
hits = [f for f in os.listdir(os.path.join(REPO, 'results'))
        if 'copilot_agent_t2_t3_reply_register' in f]
print('glob hits in results/ =', hits)

print()
print('=== C. REPLY / RECEIPT PRESENCE SCAN ===')
pats = ['REPLY_FROM_COPILOT', 'RECEIPT_COPILOT', 'copilot', 'COPILOT', 'REPLY_FROM', 'RECEIPT_']
def scan(root, label):
    print('--- %s : %s ---' % (label, root))
    if not os.path.isdir(root):
        print('  DIR NOT FOUND')
        return
    n = 0
    for dp, dn, fn in os.walk(root):
        for f in fn:
            if any(p in f for p in pats):
                n += 1
                fp_ = os.path.join(dp, f)
                try:
                    info = fp(fp_)
                except Exception as e:
                    info = 'ERR %s' % e
                print('  ', os.path.relpath(fp_, root), '|', info)
    print('   total hits =', n)
scan(os.path.join(REPO, 'letters'), 'letters/')
scan(GLM, 'GLM')
scan(os.path.join(REPO, 'results'), 'results/')

print()
print('=== D. EXACT FILENAME CHECK ===')
for root, label in [(os.path.join(REPO, 'letters'), 'letters/'), (GLM, 'GLM'),
                    (os.path.join(REPO, 'results'), 'results/')]:
    for name in ['REPLY_FROM_COPILOT_AGENT_T2_T3_THEORY_INPUTS_2026_10_17.md',
                 'RECEIPT_COPILOT_AGENT_T2_T3_2026_10_17.txt']:
        p = os.path.join(root, name)
        print(label, name, '->', os.path.exists(p))

print()
print('=== E. TIMESTAMP ===')
print('local now =', time.strftime('%Y-%m-%d %H:%M:%S %Z'))
print('utc now   =', time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()) + ' UTC')
print('epoch ms  =', int(time.time() * 1000))
