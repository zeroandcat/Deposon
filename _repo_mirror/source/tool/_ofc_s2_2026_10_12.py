# -*- coding: utf-8 -*-
"""
_ofc_s2 — 项 A（.tmp 281 件引用面核查）+ 项 E（两版索引比对）+ 项 C19（verify_c4 脚本走读，只读）
"""
import hashlib, json, os, re
from pathlib import Path
REPO = Path(r'_repo_mirror')
def sha12b(b): return hashlib.sha256(b).hexdigest()[:12]

print('='*104); print('项 A · .tmp 281 件「被冻结/登记/判定面按路径引用」核查'); print('='*104)
# 引用方 = 冻结面/登记面/判定面（.md/.json with register/verdict/errata/frozen 判据）
tmp_files = []
for dp, dns, fns in os.walk(REPO / '.tmp'):
    dns[:] = [d for d in dns if d != '__pycache__']
    for fn in fns:
        q = os.path.join(dp, fn)
        if os.path.getmtime(q) >= 1e18: continue
        from datetime import datetime
        if datetime.fromtimestamp(os.path.getmtime(q)) >= datetime(2026, 10, 1):
            tmp_files.append(fn)
print(f'  .tmp 十月区 {len(tmp_files)} 件（待检被引面）')
# 引用面 = 全仓 md/json/txt（排除 .tmp 自身与我的脚本）
referencing = {}
for dp, dns, fns in os.walk(REPO):
    dns[:] = [d for d in dns if d not in {'__pycache__', '.git', '.trae', '.tmp'}]
    for fn in fns:
        if not fn.endswith(('.md', '.json', '.txt', '.py', '.tsv')): continue
        q = os.path.join(dp, fn)
        try:
            if os.path.getsize(q) > 12_000_000: continue
            t = open(q, 'rb').read().decode('utf-8', 'ignore')
        except Exception: continue
        for tf in tmp_files:
            if tf in t:
                referencing.setdefault(tf, []).append(os.path.basename(q))
n_ref = sum(1 for tf in tmp_files if tf in referencing)
print(f'  被仓内（.tmp 之外）文本引用的 .tmp 件 = {n_ref} / {len(tmp_files)}')
for tf in list(referencing)[:25]:
    print(f'      {tf}  <- {referencing[tf][:4]}')

print()
print('='*104); print('项 E · corpus/v20 两版索引比对'); print('='*104)
a = REPO / 'corpus' / 'v20' / 'index_v3_2026_09_29.json'
b_ = REPO / 'corpus' / 'v20' / 'index_v3_2026_10_09.json'
ja = json.loads(a.read_bytes().decode('utf-8'))
jb = json.loads(b_.read_bytes().decode('utf-8'))
print(f'  09-29 版: {sha12b(a.read_bytes())} / {a.stat().st_size:,} B  顶层键: {list(ja.keys())[:8]}')
print(f'  10-09 版: {sha12b(b_.read_bytes())} / {b_.stat().st_size:,} B  顶层键: {list(jb.keys())[:8]}')
def cnt(j):
    if isinstance(j, dict):
        for k, v in j.items():
            if isinstance(v, list): return k, len(v)
        return list(j.keys())[0] if j else '-', 0
    return '-', len(j) if isinstance(j, list) else 0
ka, na = cnt(ja); kb, nb = cnt(jb)
print(f'  09-29 主列表: {ka} = {na} 条')
print(f'  10-09 主列表: {kb} = {nb} 条')
# 引用面：谁引用哪版
t_all = {}
for dp, dns, fns in os.walk(REPO):
    dns[:] = [d for d in dns if d not in {'__pycache__', '.git', '.trae'}]
    for fn in fns:
        if not fn.endswith(('.md', '.json', '.py')): continue
        q = os.path.join(dp, fn)
        try:
            if os.path.getsize(q) > 12_000_000: continue
            t = open(q, 'rb').read().decode('utf-8', 'ignore')
        except Exception: continue
        for kw in ('index_v3_2026_09_29', 'index_v3_2026_10_09'):
            if kw in t:
                t_all.setdefault(kw, []).append(os.path.basename(q))
for kw in ('index_v3_2026_09_29', 'index_v3_2026_10_09'):
    h = t_all.get(kw, [])
    print(f'  引用 "{kw}" 的件 = {len(h)}: {h[:6]}')

print()
print('='*104); print('项 C19 · verify_c4_originated_math.py 走读（只读，先不跑）'); print('='*104)
p = REPO / 'letters' / 'verify_c4_originated_math.py'
src = p.read_text(encoding='utf-8')
print(f'  指纹: {sha12b(p.read_bytes())} / {p.stat().st_size:,} B（委托记 3042cf59448e/4,115 ✓）')
print(f'  行数: {len(src.splitlines())}')
print('  --- 全文（4,115 B，核心段） ---')
for i, ln in enumerate(src.splitlines(), 1):
    print(f'  {i:>3}| {ln[:150]}')
print()
print('_ofc_s2 DONE')
