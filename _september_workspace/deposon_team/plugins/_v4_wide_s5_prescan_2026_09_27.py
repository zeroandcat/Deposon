# -*- coding: utf-8 -*-
"""_v4_wide_s5_prescan — 修前安全核查：跨件一致性 + 执行器 SHA 是否被引用（只读）"""
import hashlib, os, re
from datetime import datetime
from pathlib import Path
REPO = Path(r'D:\私人资料\deposon-repo'); RES = REPO / 'results'
def sha12(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]
def T(p): return Path(p).read_text(encoding='utf-8', errors='ignore')

print('='*100); print('A. batch10 r1..r5 的 proxy_used 硬编码行'); print('='*100)
for r in ('r1','r2','r3','r4','r5'):
    p = RES / f'_v4_supp_l14v3_batch10_{r}_executor.py'
    if not p.exists(): print(f'  MISSING {p.name}'); continue
    t = T(p)
    m = re.search(r'"proxy_used"\s*:\s*(\w+)', t)
    n = t.count('"proxy_used"')
    print(f'  {p.name:<48} sha12={sha12(p)}  proxy_used={m.group(1) if m else "?"}  出现 {n} 次')

print()
print('='*100); print('B. t1/t15/t15r2 的 load_checkpoint 段'); print('='*100)
for f in ('_v4_supp_t1_executor.py','_v4_supp_t15_executor.py','_v4_supp_t15r2_executor.py'):
    p = RES / f
    t = T(p); ls = t.splitlines()
    idx = [i for i,l in enumerate(ls) if 'def load_checkpoint' in l]
    print(f'  {f} sha12={sha12(p)}  def@L{idx[0]+1 if idx else "?"}')
    if idx:
        i = idx[0]
        for j in range(i, min(len(ls), i+10)):
            print(f'      L{j+1}: {ls[j]}')
    print(f'      except Exception 出现 {t.count("except Exception")} 次')

print()
print('='*100); print('C. 全仓是否引用这些执行器的 SHA-12（防误改破坏锚）'); print('='*100)
targets = {}
for f in ['_v4_supp_t1_executor.py','_v4_supp_t15_executor.py','_v4_supp_t15r2_executor.py'] + \
         [f'_v4_supp_l14v3_batch10_{r}_executor.py' for r in ('r1','r2','r3','r4','r5')]:
    p = RES / f
    if p.exists(): targets[sha12(p)] = f
print(f'  待修 8 件 SHA-12: {targets}')
# 扫全仓文本找这些 SHA
found = {}
CUT = datetime(2026,9,1).timestamp()
for root in (r'D:\私人资料\deposon-repo', r'D:\私人资料\deposon-sub'):
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in {'__pycache__','.git','.trae'}]
        for fn in fns:
            if not fn.endswith(('.md','.json','.txt','.py')): continue
            q = os.path.join(dp, fn)
            try: st = os.stat(q)
            except OSError: continue
            if st.st_size > 12_000_000: continue
            try: t = open(q,'rb').read().decode('utf-8','ignore')
            except Exception: continue
            for s, name in targets.items():
                if s in t and os.path.basename(q) != name:
                    found.setdefault(s, []).append(q.replace(r'D:\私人资料'+os.sep,''))
for s, name in targets.items():
    hits = found.get(s, [])
    print(f'  {s} ({name}) 被引 {len(hits)} 处: {hits[:5]}')
print()
print('_wide_s5 DONE')
