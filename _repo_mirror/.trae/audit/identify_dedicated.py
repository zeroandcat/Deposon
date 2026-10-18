# -*- coding: utf-8 -*-
"""Identify which version lives in the dedicated folder paper/deposon_arxiv_2026
and any other clean source dirs. Hash + structural fingerprint. Read-only."""
import os, re, hashlib

PAPER = r'd:\私人资料\deposon-repo\paper'
WORK = r'c:\Users\Administrator\.trae-cn\work\6a9a7e1c7578e46bf7c7f60c'

def sha(b): return hashlib.sha256(b).hexdigest()

def fingerprint(path):
    raw = open(path, 'rb').read()
    t = raw.decode('utf-8', errors='replace')
    secs = re.findall(r'\\section\*?\{([^}]*)\}', t)
    tail_kw_en = ['Data and Artifact Availability', 'Data availability', 'Artifact availability',
                  'Use of Generative AI', 'AI use disclosure']
    tail_kw_cn = ['数据与工件可用性', '数据可用性', '制品可用性', '生成式 AI', 'AI 使用声明', 'AI使用声明']
    return {
        'size': len(raw), 'sha16': sha(raw)[:16],
        'labels': len(re.findall(r'\\label\{', t)),
        'refs': len(re.findall(r'\\ref\{', t)),
        'footnotes': len(re.findall(r'\\footnote\{', t)),
        'n_sections': len(secs),
        'dup_tail_en': sum(1 for s in secs if any(k.lower() in s.lower() for k in ['Data and Artifact','Data availability','Artifact availability','Use of Generative','AI use disclosure'])),
        'dup_tail_cn': sum(1 for s in secs if any(k in s for k in ['数据与工件','数据可用性','制品可用性','生成式 AI','AI 使用声明','AI使用声明'])),
        'pdfoutput': t.splitlines()[0].strip() if t.splitlines() else '',
        'has_cjkutf8': 'CJKutf8' in t,
        'quote_b': len(re.findall(r'\\begin\{quote\}', t)), 'quote_e': len(re.findall(r'\\end\{quote\}', t)),
        'bibitems': len(re.findall(r'\\bibitem', t)),
        'secs': secs,
    }

def find_tex(folder):
    out = {}
    for r, d, fs in os.walk(folder):
        for f in fs:
            if f.endswith('.tex'):
                out[f] = os.path.join(r, f)
    return out

print('### paper/deposon_arxiv_2026 (dedicated folder)')
d2026 = os.path.join(PAPER, 'deposon_arxiv_2026')
for f, p in sorted(find_tex(d2026).items()):
    fp = fingerprint(p)
    print('\nFILE', f)
    for k in ['size','sha16','labels','refs','footnotes','n_sections','dup_tail_en','dup_tail_cn','pdfoutput','has_cjkutf8','quote_b','quote_e','bibitems']:
        print('   %-12s %s' % (k, fp[k]))
    print('   sections:', fp['secs'])

print('\n### reference: audit3 (ours) vs audit4 (minimax) sha16/size')
for tag, base in [('OURS', os.path.join(WORK,'audit3_extract')), ('MINIMAX', os.path.join(WORK,'audit4_extract'))]:
    for f, p in sorted(find_tex(base).items()):
        fp = fingerprint(p)
        print('  %-8s %-28s size=%-6d sha=%s labels=%d refs=%d fn=%d dupTail(en/cn)=%d/%d' % (
            tag, f, fp['size'], fp['sha16'], fp['labels'], fp['refs'], fp['footnotes'], fp['dup_tail_en'], fp['dup_tail_cn']))

# does 2026 match ours or minimax?
print('\n### matching 2026 tex to a lineage by sha')
ours = {os.path.basename(p): fingerprint(p)['sha16'] for p in find_tex(os.path.join(WORK,'audit3_extract')).values()}
mini = {os.path.basename(p): fingerprint(p)['sha16'] for p in find_tex(os.path.join(WORK,'audit4_extract')).values()}
for f, p in sorted(find_tex(d2026).items()):
    h = fingerprint(p)['sha16']
    match = 'OURS-audit3' if h in ours.values() else ('MINIMAX-audit4' if h in mini.values() else 'UNKNOWN-third')
    print('  ', f, '->', match, h)

# list any stray files in the dedicated folder
print('\n### stray-file scan in deposon_arxiv_2026')
for r, d, fs in os.walk(d2026):
    for f in sorted(fs):
        ext = os.path.splitext(f)[1].lower()
        flag = '  <-- STRAY' if ext in ('.pdf','.aux','.out','.log','.toc','.bbl','.blg','.broken','.old') else ''
        print('   ', os.path.relpath(os.path.join(r,f), d2026), flag)
