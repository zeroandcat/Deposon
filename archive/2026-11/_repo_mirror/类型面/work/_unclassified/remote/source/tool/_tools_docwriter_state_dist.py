import os, re, hashlib, collections, io

ROOT = r'_repo_mirror'
TARGET = os.path.join(ROOT, 'results', '_pi_decision_backlog_consolidated_2026_10_21.md')
text = open(TARGET, 'rb').read().decode('utf-8')
out = io.StringIO()

ROW = re.compile(r'^\|\s*\*\*(?P<face>[A-L])-(?P<num>\d{2})\*\*\s*\|(?P<rest>.*)$', re.M)
LABELS = ['已裁', '候裁·须文字面', '俟棒果', '外部窗口', '待采集', '候裁']

def unbold(s):
    return s.replace('**', '').strip()

states = collections.Counter()
form = collections.Counter()
ct = collections.Counter()
rows = 0
for m in ROW.finditer(text):
    rows += 1
    cols = [unbold(c) for c in m.group('rest').split('|')]
    st = cols[2] if len(cols) > 2 else ''
    fm = cols[4] if len(cols) > 4 else ''
    hit = next((L for L in LABELS if st.startswith(L)), 'UNMATCHED:' + st[:40])
    states[hit] += 1
    ct[(m.group('face'), hit)] += 1
    if 'PI 外部动作' in fm:
        form['PI 外部动作'] += 1
    elif '须 PI 文字面' in fm:
        form['须 PI 文字面（给值/生效/明写）'] += 1
    elif '卡面可裁' in fm:
        form['卡面可裁'] += 1
    else:
        form['UNMATCHED:' + fm[:50]] += 1

out.write('rows = %d\n\n' % rows)
out.write('=== 现态 distribution (column-4 parsed, bold-stripped) ===\n')
for k, v in states.most_common():
    out.write('  %-30s %d\n' % (k, v))
out.write('  sum = %d\n\n' % sum(states.values()))
out.write('=== 候裁之形式 distribution (column-6 parsed) ===\n')
for k, v in form.most_common():
    out.write('  %-40s %d\n' % (k, v))
out.write('  sum = %d\n\n' % sum(form.values()))
out.write('=== face x state ===\n')
for f in 'ABCDEFGHIJKL':
    line = {k[1]: v for k, v in ct.items() if k[0] == f}
    tot = sum(line.values())
    out.write('  %s: %s (sum=%d)\n' % (f, dict(sorted(line.items(), key=lambda x: -x[1])), tot))
out.write('\n=== scratch files created by this rod (repo root) ===\n')
n = 0
for fn in sorted(os.listdir(ROOT)):
    if fn.startswith('_tools_docwriter_'):
        p = os.path.join(ROOT, fn)
        out.write('  %-52s %8d B\n' % (fn, os.path.getsize(p)))
        n += 1
out.write('  total = %d\n' % n)
out.write('\n=== final byte self-scan ===\n')
raw = open(TARGET, 'rb').read()
out.write('  bytes = %d\n  sha12 = %s\n  BOM = %s\n  CR = %d\n  TAB = %d\n  VT = %d\n  U+FFFD = %d\n  LF = %d\n' % (
    len(raw), hashlib.sha256(raw).hexdigest()[:12], raw[:3] == b'\xef\xbb\xbf',
    raw.count(b'\r'), raw.count(b'\t'), raw.count(b'\x0b'), raw.count('\ufffd'.encode('utf-8')), raw.count(b'\n')))

open(os.path.join(ROOT, '_tools_docwriter_state_dist.txt'), 'w', encoding='utf-8', newline='\n').write(out.getvalue())
print('WROTE state distribution file')
