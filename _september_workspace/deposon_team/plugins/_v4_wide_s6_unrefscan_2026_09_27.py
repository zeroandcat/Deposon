# -*- coding: utf-8 -*-
"""_v4_wide_s6_unrefscan — 找出「未被任何其它件引用」的新 .py（可安全原地修）+ 其缺陷（只读）"""
import hashlib, os, re
from datetime import datetime
from pathlib import Path
CUTOFF = datetime(2026, 9, 23, 12, 0, 0).timestamp()
ROOTS = [r'D:\私人资料\deposon-repo', r'D:\私人资料\deposon-sub']
SKIP = {'__pycache__', '.git', '.trae'}

newfiles = []
for root in ROOTS:
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in SKIP]
        for fn in fns:
            q = os.path.join(dp, fn)
            try: st = os.stat(q)
            except OSError: continue
            if st.st_mtime >= CUTOFF: newfiles.append((q, st.st_size))

def sha12(q): return hashlib.sha256(Path(q).read_bytes()).hexdigest()[:12]

py = [(q, s) for q, s in newfiles if q.endswith('.py')]
sha_of = {sha12(q): q for q, s in py}

# 收集所有新件文本，检测谁引用了谁
texts = {}
for q, s in newfiles:
    if s > 12_000_000: continue
    try: texts[q] = open(q, 'rb').read().decode('utf-8', 'ignore')
    except Exception: pass

refd = {}
for q, t in texts.items():
    for s12, owner in sha_of.items():
        if s12 in t and Path(q) != Path(owner):
            refd.setdefault(owner, set()).add(q)

unref = [q for q, s in py if q not in refd]
print(f'=== 新 .py {len(py)} 件；被其它件引用者 {len(refd)} 件；未被引用者 {len(unref)} 件 ===')
print()
print('--- 未被引用的 .py 及其缺陷（可安全原地修者）---')
DEFECTS = []
for q in sorted(unref):
    p = Path(q); raw = p.read_bytes(); rel = str(p).replace(r'D:\私人资料' + os.sep, '')
    t = raw.decode('utf-8', 'ignore')
    d = []
    if raw[:3] == b'\xef\xbb\xbf': d.append('BOM')
    if re.search(r'except Exception:\s*\n\s*return \[\]', t): d.append('SILENT_CKPT')
    if 'C:/Users/Administrator/Desktop/AI/LLM API.txt' in t: d.append('KEYPATH_ABS')
    if re.search(r'except\s*:\s*(pass|continue)\b', t): d.append('BARE_EXCEPT')
    if re.search(r'\bopen\([^)]*\)\s*\.read\(\)', t): d.append('OPEN_NO_WITH')
    if d:
        DEFECTS.append((rel, len(raw), d))
        print(f'  {rel:<72} {len(raw):>7}B  {",".join(d)}')
if not DEFECTS:
    print('  （无）')
print()
print('--- 未被引用且无上述缺陷者（抽查计数）---')
clean = [q for q in unref if not any(True for rel, _, _ in DEFECTS if rel == str(Path(q)).replace(r"D:\私人资料"+os.sep, ""))]
print(f'  {len(clean)} 件')
print('_wide_s6 DONE')
