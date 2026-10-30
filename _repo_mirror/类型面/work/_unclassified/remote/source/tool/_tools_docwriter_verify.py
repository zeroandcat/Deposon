import os, re, hashlib, datetime, collections, sys

ROOT = r'_repo_mirror'
TARGET = os.path.join(ROOT, 'results', '_pi_decision_backlog_consolidated_2026_10_21.md')

# ---------- 1. byte-level scan (pre-normalisation view) ----------
raw = open(TARGET, 'rb').read()
print('=== PRE-NORMALISATION ===')
print('bytes           =', len(raw))
print('BOM(EFBBBF)     =', raw[:3] == b'\xef\xbb\xbf')
print('CR count        =', raw.count(b'\r'))
print('TAB count       =', raw.count(b'\t'))
print('VT(U+000B)      =', raw.count(b'\x0b'))
print('U+FFFD          =', raw.count('\ufffd'.encode('utf-8')))
print('CRLF pairs      =', raw.count(b'\r\n'))

# ---------- 2. normalise to LF + strip BOM (this file only) ----------
norm = raw
if norm[:3] == b'\xef\xbb\xbf':
    norm = norm[3:]
norm = norm.replace(b'\r\n', b'\n').replace(b'\r', b'\n')
if norm != raw:
    open(TARGET, 'wb').write(norm)
    print('>>> NORMALISED (BOM stripped / CRLF -> LF)')
else:
    print('>>> NO NORMALISATION NEEDED')

# ---------- 3. independent re-read (separate open) ----------
raw2 = open(TARGET, 'rb').read()
text = raw2.decode('utf-8')          # strict decode; raises if invalid
print()
print('=== POST-NORMALISATION INDEPENDENT RE-READ ===')
print('bytes           =', len(raw2))
print('sha256[:12]     =', hashlib.sha256(raw2).hexdigest()[:12])
print('BOM             =', raw2[:3] == b'\xef\xbb\xbf')
print('CR count        =', raw2.count(b'\r'))
print('TAB count       =', raw2.count(b'\t'))
print('VT count        =', raw2.count(b'\x0b'))
print('U+FFFD          =', raw2.count('\ufffd'.encode('utf-8')))
print('LF count        =', raw2.count(b'\n'))
print('utf-8 strict decode = OK')

# ---------- 4. register-row exhaustive count ----------
rows = re.findall(r'^\|\s*\*\*(?P<face>[A-L])-(?P<num>\d{2})\*\*\s*\|', text, re.M)
by_face = collections.Counter(f for f, n in rows)
print()
print('=== REGISTER ROW COUNTS (exhaustive, by pattern) ===')
print('total rows =', len(rows))
for f in sorted(by_face):
    print('  face %s = %d' % (f, by_face[f]))
dupes = [k for k, v in collections.Counter(rows).items() if v > 1]
print('duplicate ids =', dupes if dupes else 'NONE')

# state-label distribution
label_re = re.compile(r'^\|\s*\*\*(?P<face>[A-L])-(?P<num>\d{2})\*\*\s*\|.*?\|\s*\*{0,2}(?P<state>已裁|候裁·须文字面|候裁|俟棒果|外部窗口|待采集)\*{0,2}\s*\|', re.M)
states = collections.Counter(m.group('state') for m in label_re.finditer(text))
print()
print('=== STATE-LABEL DISTRIBUTION (per row, from table col.4) ===')
for k, v in states.items():
    print('  %s = %d' % (k, v))
print('sum =', sum(states.values()), '(must equal total rows =', len(rows), ')')

# ---------- 5. long-name style re-probe (no -Filter alone) ----------
print()
print('=== LONG-NAME STYLE RE-PROBE (Get-ChildItem -Name equivalent, os.listdir) ===')
res = os.path.join(ROOT, 'results')
names = os.listdir(res)
for pat in ('*_pi_decision_backlog*', '*backlog*', '*consolidated*'):
    hits = [n for n in names if pat.strip('*') in n]
    print('  %-24s -> %d hit(s): %s' % (pat, len(hits), hits))
print('  target exists (exact)  ->', os.path.exists(TARGET))
print('  target mtime           ->', datetime.datetime.fromtimestamp(os.stat(TARGET).st_mtime).strftime('%Y-%m-%d %H:%M:%S'))

# ---------- 6. existing-file touch check: re-verify anchor fingerprints ----------
ANCHORS = {
 'results/_kd_mda8a24_clearance_verdict_2026_10_20.md': '170ab543d941',
 'results/_kd_sepcal7_final_verdict_2026_10_20.md': 'c013aeb1235f',
 'results/_kd_identified_defect_attribution_caliber_2026_10_20.md': '609943436a0d',
 'results/_v172_adoption_effect_2026_10_20.md': '9c853eec100d',
 'results/_stage1_prereq_wave1_proposals_2026_10_20.md': 'a8a9018fd67e',
 'pi_rulings/_pi_card_answers_register_2026_10_21_v174.md': '3122d39e1727',
 'letters/_reply_to_glm_dualtrack_v156_rulings_2026_10_20.md': '3ea469e5a6f3',
 'results/_kd_false9_remedy_proposals_2026_10_20.md': '77bc92c9d227',
 'results/_kd_false9_wave0_calibers_2026_10_20.md': '97ac680345ac',
 'results/_stage1_gap_exhaustive_audit_2026_10_20.md': 'cc00c068aa50',
}
print()
print('=== ANCHOR RE-VERIFICATION (existing files untouched) ===')
ok = 0
for rel, want in ANCHORS.items():
    p = os.path.join(ROOT, rel.replace('/', os.sep))
    b = open(p, 'rb').read()
    got = hashlib.sha256(b).hexdigest()[:12]
    match = (got == want)
    ok += 1 if match else 0
    print('  %-70s want=%s got=%s %s' % (rel, want, got, 'OK' if match else 'DIFF'))
print('  matched = %d / %d' % (ok, len(ANCHORS)))
