import os, re, datetime, io, json

ROOT = r'_repo_mirror'
SCAN_DIRS = [os.path.join(ROOT, 'pi_rulings'), os.path.join(ROOT, 'results')]
CUTOFF = datetime.datetime(2026, 10, 19).timestamp()

HEAD_RE = re.compile(r'^(#{1,4})\s*(.+)$')

# a heading is a "candidate-list" heading if it names a decision-pending surface
HEAD_KEYS = ['\u5019 PI \u88c1\u9879', '\u5019\u88c1\u9879', '\u5f85 PI \u88c1', '\u5019 PI \u88c1',
             '\u5019\u88c1\u95ee\u9898', '\u5f85\u88c1', '\u5019\u88c1', '\u5019\u88c1\u4e4b\u9762',
             '\u5f85 PI', '\u5019 PI', '\u5019\u88c1\u6e05\u5355', '\u5f85\u88c1\u9879',
             '\u5019 PI \u62a5', '\u5019\u88c1\u4e4b\u5dee\u5f02', '\u5019 PI \u65b9\u5411',
             '\u5019\u88c1\u53e3\u5f84', '\u5f85\u67e5']

out = io.StringIO()
found_heads = []   # (relfile, mtime, heading, level, lineno)

for sd in SCAN_DIRS:
    for dp, dn, fn in os.walk(sd):
        dn[:] = [d for d in dn if d not in {'__pycache__', '.tmp'}]
        for f in sorted(fn):
            if not f.lower().endswith('.md'):
                continue
            p = os.path.join(dp, f)
            try:
                st = os.stat(p)
            except Exception:
                continue
            if st.st_mtime < CUTOFF:
                continue
            raw = open(p, 'rb').read()
            text = raw.decode('utf-8', 'replace')
            rel = os.path.relpath(p, ROOT)
            lines = text.split('\n')
            for i, ln in enumerate(lines):
                m = HEAD_RE.match(ln)
                if not m:
                    continue
                h = m.group(2)
                if any(k in h for k in HEAD_KEYS):
                    found_heads.append((rel, datetime.datetime.fromtimestamp(st.st_mtime).strftime('%m-%d %H:%M'), h.strip(), len(m.group(1)), i + 1))

found_heads.sort(key=lambda r: (r[0], r[4]))
out.write('=== CANDIDATE-SURFACE HEADINGS (files mtime>=2026-10-19) ===\n')
out.write('count = %d\n\n' % len(found_heads))
for rel, mt, h, lv, ln in found_heads:
    out.write('%-58s | %s | L%-3d | H%d | %s\n' % (rel, mt, ln, lv, h))

open(os.path.join(ROOT, '_tools_docwriter_heading_extract.txt'), 'w', encoding='utf-8', newline='\n').write(out.getvalue())
print('HEADINGS_FOUND', len(found_heads))
