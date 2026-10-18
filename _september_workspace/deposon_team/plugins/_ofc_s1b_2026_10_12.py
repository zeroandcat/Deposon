# -*- coding: utf-8 -*-
"""
_ofc_s1b — 10 月件全量机扫（修正版：绝对路径保留 + 路径归一分类 + compile 真检）
只读；归档区 0 访问。
"""
import hashlib, os, re, json
from datetime import datetime
from pathlib import Path

REPO = Path(r'D:\私人资料\deposon-repo'); SUB = Path(r'D:\私人资料\deposon-sub')
BOUND = datetime(2026, 10, 1, 0, 0, 0).timestamp()
def sha12b(b): return hashlib.sha256(b).hexdigest()[:12]

def scan(root):
    out = []
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in {'__pycache__', '.git', '.trae', '.mavis', '.evidence_backup_2026_09_28', '.evidence_backup_2026_09_30'}]
        for fn in fns:
            q = os.path.join(dp, fn)
            try: st = os.stat(q)
            except OSError: continue
            if st.st_mtime < BOUND: continue
            out.append((q, st))
    return out

repo_f = scan(REPO); sub_f = scan(SUB)
print(f'=== 边界复算 ===  repo={len(repo_f)}（委托 477/478）  sub={len(sub_f)}（458）  合计={len(repo_f)+len(sub_f)}')

rows = []
for q, st in repo_f + sub_f:
    b = open(q, 'rb').read()
    rel = q.replace('D:\\私人资料\\', '').replace('\\', '/')
    rows.append(dict(path=q, rel=rel, sha=sha12b(b), n=len(b),
        bom=b[:3] == b'\xef\xbb\xbf', cr=b.count(b'\r'), lf=b.count(b'\n'),
        ext=os.path.splitext(q)[1].lower(), mtime=datetime.fromtimestamp(st.st_mtime).strftime('%m-%d %H:%M'),
        ctime=datetime.fromtimestamp(st.st_ctime).strftime('%m-%d %H:%M'), side='repo' if q.startswith(str(REPO)) else 'sub'))

def cat(rel, side):
    r = rel
    if side == 'sub': return 'G_sub'
    if r.startswith('deposon-repo/.tmp/'): return 'A_tmp'
    if r.startswith('deposon-repo/results/'): return 'B_results'
    if r.startswith('deposon-repo/letters/'): return 'C_letters'
    if r.startswith('deposon-repo/deposon_team/'): return 'D_plugins'
    if r.startswith('deposon-repo/corpus/'): return 'E_corpus'
    if r.startswith('deposon-repo/docs/'): return 'F_docs'
    if r.count('/') == 1: return 'X_root'
    return 'Z_other'
for r in rows: r['cat'] = cat(r['rel'], r['side'])

from collections import Counter
print()
print('=== 逐类计数 ===')
c = Counter(r['cat'] for r in rows)
for k in sorted(c):
    print(f'  {k:<12} {c[k]:>4}   字节 {sum(x["n"] for x in rows if x["cat"]==k):>12,}')

print()
print('=== .py compile 真检 ===')
nbad = []
npy = 0
for r in rows:
    if r['ext'] != '.py': continue
    npy += 1
    try: compile(open(r['path'], 'rb').read(), r['path'], 'exec')
    except SyntaxError as e: nbad.append((r['rel'], f'L{e.lineno}: {e.msg}'))
    except Exception as e: nbad.append((r['rel'], f'{type(e).__name__}: {e}'))
print(f'  .py {npy} 件，语法错误 {len(nbad)} 件')
for it in nbad[:20]: print(f'      {it}')

print()
print('=== BOM 78 件分面 ===')
cb = Counter(r['cat'] for r in rows if r['bom'])
print(f'  {dict(cb)}')
print('  BOM 件名（前 24）:')
for r in [x for x in rows if x['bom']][:24]:
    print(f'      [{r["cat"]}] {r["rel"].split("/")[-1]}')

print()
print('=== CR>0 95 件分面 ===')
cc = Counter(r['cat'] for r in rows if r['cr'] > 0)
print(f'  {dict(cc)}')

print()
print('=== 项 G 两分（sub：内容自载日期字面初判） ===')
n_new = n_moved = n_unk = 0
unk_samples = []
for r in rows:
    if r['cat'] != 'G_sub': continue
    b = open(r['path'], 'rb').read()[:6000]
    t = b.decode('utf-8', 'ignore')
    ms = re.findall(r'202[56]-(?:0[1-9]|1[0-2])-(?:[0-3]\d)', t)
    ms = [m for m in ms if m >= '2026-01-01']
    if ms:
        earliest = min(ms)
        if earliest < '2026-10-01': n_moved += 1
        else: n_new += 1
    else:
        m2 = re.search(r'2026[_.]?10', r['rel'])
        if m2: n_new += 1
        else:
            n_unk += 1; unk_samples.append(r['rel'].split('/')[-1])
print(f'  内容载 10-01 前日期（转移落位初判）= {n_moved}')
print(f'  内容/名载 10 月（十月新出产初判）= {n_new}')
print(f'  无日期字面（未判）= {n_unk}   和 = {n_moved+n_new+n_unk}')
for s in unk_samples[:10]: print(f'      未判例: {s}')

# sub 与 repo SHA 交集（去重复核）
repo_shas = {r['sha'] for r in rows if r['side'] == 'repo'}
sub_shas = {r['sha'] for r in rows if r['side'] == 'sub'}
inter = repo_shas & sub_shas
print(f'  repo/sub SHA 交集 = {len(inter)} 件（委托记恰 1 件）')

outp = REPO / '.tmp' / '_ofc_s1b_inventory.json'
outp.write_text(json.dumps([{k: v for k, v in r.items() if k != 'path'} | {'path': r['rel']} for r in rows], ensure_ascii=False, indent=1), encoding='utf-8')
print(f'\n逐件清单落盘: .tmp/_ofc_s1b_inventory.json  {len(rows)} 行')
print('_ofc_s1b DONE')
