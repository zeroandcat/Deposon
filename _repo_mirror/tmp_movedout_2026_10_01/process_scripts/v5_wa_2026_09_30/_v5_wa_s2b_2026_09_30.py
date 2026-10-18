# -*- coding: utf-8 -*-
"""_v5_wa_s2b — 0 覆盖自检（路径规范化对比）+ 571 vs 574 差异定位 + 8 件 keypath 引用图（只读）"""
import hashlib, os, re
from datetime import datetime
from pathlib import Path
REPO = Path(r'D:\私人资料\deposon-repo')
B0 = datetime(2026,9,27,20,28,20).timestamp()
EXCL = ('.evidence_backup_2026_09_28', '.evidence_backup_2026_09_30', '_movedout_scratch_2026_09_30')
def norm(p): return p.replace('\\', '/').lower().lstrip('/')

com = Path(r'D:\私人资料\deposon-repo\letters\TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md').read_text(encoding='utf-8')
# 抽附录表行路径（| n | `path` | bytes | mtime | sha |）
rows = re.findall(r'\|\s*\d+\s*\|\s*`([^`]+)`\s*\|\s*(\d+)\s*\|', com)
comm = {norm(r[0].replace('D:\\私人资料\\', '')): (int(r[1]), r[0]) for r in rows}
print(f'  委托附录行抽取（规范化键）{len(comm)} 条')

def sha12(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]

mine = {}
for area, prefix in ((r'D:\私人资料\deposon-repo', 'deposon-repo/'), (r'D:\私人资料\deposon-sub', 'deposon-sub/'), (r'D:\私人资料\_non_upload_local_archive', '')):
    for dp, dns, fns in os.walk(area):
        dns[:] = [d for d in dns if d not in {'__pycache__','.git','.trae','.mavis'}]
        if any(x in dp for x in EXCL): continue
        for fn in fns:
            q = os.path.join(dp, fn)
            try: st = os.stat(q)
            except OSError: continue
            if st.st_mtime > B0:
                key = norm(q.replace('D:\\私人资料\\', ''))
                mine[key] = (st.st_size, q, st.st_mtime)

only_mine = [k for k in mine if k not in comm]
only_comm = [k for k in comm if k not in mine]
print(f'  实测 {len(mine)} 件 / 附录 {len(comm)} 条')
print(f'  实测有而附录无 = {len(only_mine)}:')
for k in sorted(only_mine)[:20]:
    print(f'      {mine[k][0]:>8}B  {datetime.fromtimestamp(mine[k][2]).strftime("%m-%d %H:%M")}  {k}')
print(f'  附录有而实测无 = {len(only_comm)}:')
for k in sorted(only_comm)[:20]:
    print(f'      {comm[k][0]:>8}B  {k}')

# 字节漂移面（两边都有但字节不同）
drift = [(k, comm[k][0], mine[k][0]) for k in mine if k in comm and comm[k][0] != mine[k][0]]
print(f'  两边都有但字节不同 = {len(drift)}:')
for k, a, b in drift[:20]:
    print(f'      附录 {a}B -> 实测 {b}B  {k}')

print()
print('=== 8 件 keypath 执行器的引用图（决定可否原地改）===')
def sha12(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]
targets = {}
for r in ('r1_2026_09_27','r2_atomic_2026_09_28','r3_2026_09_28','r0_atomic_2026_09_29'):
    for base in ('_v4_supp_t15_executor_', '_v4_supp_t15r2_executor_'):
        p = REPO / 'results' / f'{base}{r}.py'
        if p.exists():
            targets[sha12(p)] = str(p.name)
print(f'  目标 {len(targets)} 件: {targets}')
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
        for s, name in targets.items():
            if s in t and os.path.basename(q) != name:
                found.setdefault(name, []).append(os.path.basename(q))
for s, name in targets.items():
    h = found.get(name, [])
    print(f'  {name:<44} 被引 {len(h)} 处: {h[:6]}')
print('_wa_s2b DONE')
