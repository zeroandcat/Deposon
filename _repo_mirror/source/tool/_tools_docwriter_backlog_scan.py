import os, re, json, datetime, sys

ROOT = r'_repo_mirror'
SCAN_DIRS = [os.path.join(ROOT, 'pi_rulings'), os.path.join(ROOT, 'results')]
CUTOFF = datetime.datetime(2026, 10, 19).timestamp()   # mtime >= 2026-10-19 00:00 local

LITERALS = ['\u5019 PI', '\u4fdf PI', '\u5f85\u88c1', '\u5019\u88c1']  # 候 PI / 俟 PI / 待裁 / 候裁

# exhaustive counter: count non-overlapping occurrences of each literal
def count_lit(text, lit):
    n = 0
    start = 0
    while True:
        i = text.find(lit, start)
        if i < 0:
            break
        n += 1
        start = i + len(lit)
    return n

rows = []
totals = {lit: 0 for lit in LITERALS}
files_scanned = 0
files_with_hits = 0
grand = 0

for sd in SCAN_DIRS:
    if not os.path.isdir(sd):
        print('DIR_MISSING', sd)
        continue
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
            try:
                raw = open(p, 'rb').read()
            except Exception:
                continue
            try:
                text = raw.decode('utf-8')
            except Exception:
                text = raw.decode('utf-8', 'replace')
            files_scanned += 1
            per = {}
            tot = 0
            for lit in LITERALS:
                c = count_lit(text, lit)
                per[lit] = c
                totals[lit] += c
                tot += c
            if tot > 0:
                files_with_hits += 1
                grand += tot
                rows.append((os.path.relpath(p, ROOT), st.st_mtime, len(raw), per, tot))

rows.sort(key=lambda r: (-r[4], r[0]))
print('=== SCOPE ===')
print('scan_dirs =', [os.path.relpath(d, ROOT) for d in SCAN_DIRS])
print('mtime_cutoff_local = 2026-10-19 00:00:00')
print('files_scanned(md, mtime>=cutoff) =', files_scanned)
print('files_with_hits =', files_with_hits)
print('grand_total_occurrences =', grand)
print('=== PER-LITERAL TOTALS ===')
for lit in LITERALS:
    print('  %s = %d' % (lit, totals[lit]))
print('=== PER-FILE (name | mtime | bytes | 候PI | 俟PI | 待裁 | 候裁 | total) ===')
for rel, mt, ln, per, tot in rows:
    print('%-70s | %s | %8d | %4d %4d %4d %4d | %5d' % (
        rel, datetime.datetime.fromtimestamp(mt).strftime('%m-%d %H:%M'), ln,
        per[LITERALS[0]], per[LITERALS[1]], per[LITERALS[2]], per[LITERALS[3]], tot))
print('=== DISTINCT FILES WITH HITS LISTED ABOVE; count =', len(rows), '===')
