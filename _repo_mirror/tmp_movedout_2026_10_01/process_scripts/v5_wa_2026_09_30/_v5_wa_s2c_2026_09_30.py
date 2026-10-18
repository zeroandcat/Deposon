# -*- coding: utf-8 -*-
"""_v5_wa_s2c — 0 覆盖自检（区前缀归一后）+ .tmp BOM 件引用图（只读）"""
import hashlib, os, re
from datetime import datetime
from pathlib import Path
REPO = Path(r'D:\私人资料\deposon-repo')
B0 = datetime(2026,9,27,20,28,20).timestamp()
EXCL = ('.evidence_backup_2026_09_28', '.evidence_backup_2026_09_30', '_movedout_scratch_2026_09_30')
def sha12(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]

com = Path(r'D:\私人资料\deposon-repo\letters\TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md').read_text(encoding='utf-8')
rows = re.findall(r'\|\s*\d+\s*\|\s*`([^`]+)`\s*\|\s*(\d+)\s*\|', com)
def norm2(p):
    p = p.replace('\\','/').lower()
    for pre in ('deposon-repo/','deposon-sub/'):
        if p.startswith(pre): return p[len(pre):]
    return p
comm = {norm2(r[0]): int(r[1]) for r in rows}

mine = {}
for area, strip in ((r'D:\私人资料\deposon-repo', 'deposon-repo'), (r'D:\私人资料\deposon-sub', 'deposon-sub'), (r'D:\私人资料\_non_upload_local_archive', '_non_upload_local_archive')):
    for dp, dns, fns in os.walk(area):
        dns[:] = [d for d in dns if d not in {'__pycache__','.git','.trae','.mavis'}]
        if any(x in dp for x in EXCL): continue
        for fn in fns:
            q = os.path.join(dp, fn)
            try: st = os.stat(q)
            except OSError: continue
            if st.st_mtime > B0:
                key = norm2(q.replace('D:\\私人资料\\' + strip + '\\', ''))
                mine[key] = st.st_size

only_mine = sorted(k for k in mine if k not in comm)
only_comm = sorted(k for k in comm if k not in mine)
print(f'实测 {len(mine)} / 附录 {len(comm)}')
print(f'实测有而附录无 = {len(only_mine)}:')
for k in only_mine: print(f'    {mine[k]:>8}B  {k}')
print(f'附录有而实测无 = {len(only_comm)}:')
for k in only_comm: print(f'    {comm[k]:>8}B  {k}')
drift = [(k, comm[k], mine[k]) for k in mine if k in comm and comm[k] != mine[k]]
print(f'字节漂移 = {len(drift)}:')
for k, a, b in drift: print(f'    {a}B -> {b}B  {k}')

print()
print('=== repo/.tmp 9 件 BOM 件的引用（决定可否原地修）===')
bomfiles = ['_en_verify_2026_09_28.py','_en_verify2_2026_09_28.py','_en_verify3_2026_09_28.py',
            '_en_verify4_2026_09_28.py','_en_final_2026_09_28.py','_probe21.py','_hash21.py',
            '_c5_feasibility_probe.py','_r4_cleanup_worker_keyscan_2026_09_29.py']
shas = {sha12(REPO/'.tmp'/f): f for f in bomfiles}
found = {}
for dp, dns, fns in os.walk(REPO):
    dns[:] = [d for d in dns if d not in {'__pycache__','.git'}]
    for fn in fns:
        if not fn.endswith(('.md','.json','.txt','.py')): continue
        q = os.path.join(dp, fn)
        try:
            if os.path.getsize(q) > 12_000_000: continue
            t = open(q,'rb').read().decode('utf-8','ignore')
        except Exception: continue
        for s, name in shas.items():
            if s in t and fn != name:
                found.setdefault(name, []).append(os.path.basename(q))
for s, name in shas.items():
    h = found.get(name, [])
    print(f'  {name:<40} 被引 {len(h)} 处 {h[:4]}')
print('_wa_s2c DONE')
