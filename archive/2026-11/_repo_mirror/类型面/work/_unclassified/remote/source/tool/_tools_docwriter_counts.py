import os, re, io, collections

ROOT = r'_repo_mirror'
TARGET = os.path.join(ROOT, 'results', '_pi_decision_backlog_consolidated_2026_10_21.md')
text = open(TARGET, 'rb').read().decode('utf-8')
out = io.StringIO()

# §0-3 fingerprint table row count
sec = text.split('### §0-3')[1].split('### §0-4')[0]
fp_rows = re.findall(r'^\|\s*`?results\\|letters\\|pi_rulings\\', sec, re.M)
out.write('§0-3 fingerprint-table rows = %d\n' % len(fp_rows))

# distinct SHA-12 tokens in the whole document
shas = set(re.findall(r'`([0-9a-f]{12})`', text))
out.write('distinct 12-hex tokens in doc = %d\n' % len(shas))

# distinct hosts cited in §2 (register rows) by backtick filename
sec2 = text.split('## §2 逐面登记')[1].split('## §3 遗漏面自查之果')[0]
hosts = set()
for m in re.finditer(r'`((?:results|letters|pi_rulings)\\[^`]+?)`', sec2):
    hosts.add(m.group(1))
out.write('distinct host filenames cited in §2 = %d\n' % len(hosts))

# scratch files
scr = sorted(f for f in os.listdir(ROOT) if f.startswith('_tools_docwriter_'))
out.write('scratch files in repo root = %d\n' % len(scr))
for f in scr:
    out.write('   %s\n' % f)

open(os.path.join(ROOT, '_tools_docwriter_counts.txt'), 'w', encoding='utf-8', newline='\n').write(out.getvalue())
print('OK')
