# -*- coding: utf-8 -*-
"""
_ofc_s1 — 10 月件全量机扫（repo 477/478 + sub 458）
产出：逐件 SHA-12/bytes/BOM/CR/类别/compile 状态 + 各类汇总 + 项 G 两分初判 + 项 E/F 指纹
只读；归档区 0 访问。
"""
import hashlib, os, re, json
from datetime import datetime
from pathlib import Path

REPO = Path(r'_repo_mirror'); SUB = Path(r'_repo_mirror')
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
print(f'=== 边界复算（mtime >= 2026-10-01）===')
print(f'  repo = {len(repo_f)} 件（委托记 477/478）')
print(f'  sub  = {len(sub_f)} 件（委托记 458）')
print(f'  合计 = {len(repo_f)+len(sub_f)}（委托 934/935）')

# 全件数据（SHA + bytes + BOM + CR）
rows = []
for q, st in repo_f + sub_f:
    b = open(q, 'rb').read()
    rows.append(dict(
        path=q.replace('〔本地资料区〕\\', ''), sha=sha12b(b), n=len(b),
        bom=b[:3] == b'\xef\xbb\xbf', cr=b.count(b'\r'),
        ext=os.path.splitext(q)[1].lower(), mtime=datetime.fromtimestamp(st.st_mtime).strftime('%m-%d %H:%M'),
        ctime=datetime.fromtimestamp(st.st_ctime).strftime('%m-%d %H:%M'),
    ))

# 汇总
from collections import Counter
print()
print('=== 逐区类别计数（机扫） ===')
def cat(p):
    r = p.replace('\\', '/')
    if '/.tmp/' in r: return 'A_tmp'
    if '/results/' in r and '/deposon-repo/' in r: return 'B_results'
    if '/letters/' in r: return 'C_letters'
    if '/deposon_team/' in r: return 'D_plugins'
    if '/corpus/' in r: return 'E_corpus'
    if '/docs/' in r: return 'F_docs'
    if '/deposon-sub/' in r: return 'G_sub'
    if r.startswith('deposon-repo/') and r.count('/') == 1: return 'X_root'
    return 'Z_other'
c = Counter(cat(r['path']) for r in rows)
for k, v in sorted(c.items()):
    print(f'  {k:<12} {v}')
print(f'  字节合计 = {sum(r["n"] for r in rows):,}')

print()
print('=== 扩展名分布 ===')
ce = Counter(r['ext'] for r in rows)
for k, v in ce.most_common(12):
    print(f'  {k:<8} {v}')

print()
print('=== BOM / CR 面 ===')
boms = [r for r in rows if r['bom']]
crs = [r for r in rows if r['cr'] > 0]
print(f'  BOM {len(boms)} 件: {[r["path"].split("/")[-1] for r in boms][:12]}')
print(f'  CR>0 {len(crs)} 件: {[(r["path"].split("/")[-1], r["cr"]) for r in crs][:8]}')

print()
print('=== .py compile 全检 ===')
nbad = []
for r in rows:
    if r['ext'] != '.py': continue
    try:
        compile(open(r['path'].replace('deposon-repo/', '_repo_mirror/', 1).replace('deposon-sub/', '_repo_mirror/', 1) if not r['path'].startswith('D:') else r['path'], 'rb').read() if False else open(r['path'], 'rb').read(), r['path'], 'exec')
    except SyntaxError as e:
        nbad.append((r['path'], f'L{e.lineno}: {e.msg}'))
    except Exception as e:
        nbad.append((r['path'], f'{type(e).__name__}: {e}'))
print(f'  .py 共 {sum(1 for r in rows if r["ext"]==".py")} 件，语法错误 {len(nbad)} 件')
for it in nbad[:15]:
    print(f'      {it}')

print()
print('=== 项 G 两分初判（sub 458 件：内容自载日期字面） ===')
n_new = n_moved = n_unk = 0
moved_samples, new_samples = [], []
for r in rows:
    if cat(r['path']) != 'G_sub': continue
    b = open(r['path'], 'rb').read()[:4000]
    t = b.decode('utf-8', 'ignore')
    m = re.search(r'202[56]-(09|0[1-9])-([0-3]\d)', t)
    if m:
        if m.group(1) == '09' or m.group(0) < '2026-10-01':
            n_moved += 1; moved_samples.append((r['path'].split('/')[-1], m.group(0)))
        else:
            n_new += 1; new_samples.append((r['path'].split('/')[-1], m.group(0)))
    else:
        # 文件名日期
        m2 = re.search(r'2026_?10[_-]?\d{0,2}', r['path'])
        if m2: n_new += 1
        else: n_unk += 1
print(f'  内容/名载 09 月或更早（转移落位初判）= {n_moved}')
print(f'  内容/名载 10 月（十月新出产初判）= {n_new}')
print(f'  无日期字面（未判）= {n_unk}')
print(f'  三者之和 = {n_moved+n_new+n_unk}（须 = {sum(1 for r in rows if cat(r["path"])=="G_sub")}）')

print()
print('=== 项 E 指纹（corpus/v20 两版） ===')
for r in rows:
    if cat(r['path']) == 'E_corpus':
        print(f'  {r["sha"]} / {r["n"]:,} B  {r["path"].split("/")[-1]}  mtime={r["mtime"]}')

print()
print('=== 项 D 指纹（plugins 14+ 件） ===')
for r in sorted(rows, key=lambda x: x['path']):
    if cat(r['path']) == 'D_plugins':
        print(f'  {r["sha"]} / {r["n"]:>7,} B  {r["path"].split("/")[-1]}  mtime={r["mtime"]}')

print()
print('=== 项 C 19 件指纹复核 ===')
for r in sorted(rows, key=lambda x: x['path']):
    if cat(r['path']) == 'C_letters':
        print(f'  {r["sha"]} / {r["n"]:>7,} B  {r["path"].split("/")[-1]}')

print()
print('=== 项 F docs 十月区 ===')
for r in rows:
    if cat(r['path']) == 'F_docs':
        print(f'  {r["sha"]} / {r["n"]:,} B  {r["path"]}')

# 落盘逐件清单（供后续引用）
outp = REPO / '.tmp' / '_ofc_s1_inventory.json'
outp.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding='utf-8')
print(f'\n逐件清单落盘: {outp}  {len(rows)} 行')
print('_ofc_s1 DONE')
