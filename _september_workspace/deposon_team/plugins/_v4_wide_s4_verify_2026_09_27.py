# -*- coding: utf-8 -*-
"""_v4_wide_s4_verify — 核验子代理所报高severity断言（只读）"""
import hashlib, json, os, re
from pathlib import Path
REPO = Path(r'D:\私人资料\deposon-repo'); RES = REPO / 'results'
SUB = Path(r'D:\私人资料\deposon-sub')

def T(p): return Path(p).read_text(encoding='utf-8', errors='ignore')
def lines_around(txt, pat, ctx=4, limit=3):
    out = []; ls = txt.splitlines()
    for i, ln in enumerate(ls):
        if re.search(pat, ln):
            out.append((i+1, ls[max(0,i-ctx):i+ctx+1]))
            if len(out) >= limit: break
    return out

print('='*100); print('A. t1 executor load_checkpoint except: return [] ？'); print('='*100)
t1 = T(RES / '_v4_supp_t1_executor.py')
for ln, blk in lines_around(t1, r'def load_checkpoint', ctx=8, limit=1):
    print(f'  L{ln} 起:')
    for j, l in enumerate(blk): print(f'    {l}')
for ln, blk in lines_around(t1, r'except Exception:\s*$', ctx=2, limit=6):
    print(f'  except@L{ln}: {blk[-3:]}')

print()
print('='*100); print('B. tun_compliance 判据 endswith("/chat/completions") ?'); print('='*100)
for f in ['_v4_supp_l14v3_batch1_executor.py', '_v4_supp_l14v3_batch2_r1_executor.py']:
    t = T(RES / f)
    for ln, blk in lines_around(t, r'tun_compliance|endswith\(', ctx=3, limit=3):
        print(f'  [{f}] L{ln}:')
        for l in blk: print(f'      {l[:170]}')

print()
print('='*100); print('C. batch10 proxy_used 硬编码 False ?'); print('='*100)
b10 = T(RES / '_v4_supp_l14v3_batch10_r1_executor.py')
for ln, blk in lines_around(b10, r'proxy_used|no_proxy_compliance', ctx=3, limit=5):
    print(f'  L{ln}:')
    for l in blk: print(f'      {l[:170]}')

print()
print('='*100); print('D. result.json 是否记录 executor 的 SHA-12（防误改）'); print('='*100)
r1 = json.loads(T(RES / '_v4_supp_l14v3_batch2_r1_result.json'))
s = json.dumps(r1, ensure_ascii=False)
for kw in ['executor_sha', 'sha12', 'prereg_sha12', 'executor']:
    hits = re.findall(r'"%s[^"]*"\s*:\s*"[^"]*"' % kw, s)
    print(f'  含 "{kw}": {len(hits)} 处 {hits[:4]}')

print()
print('='*100); print('E. deposon-sub/results/_test_conv_out.txt 真身'); print('='*100)
p = SUB / 'results' / '_test_conv_out.txt'
raw = p.read_bytes()
print(f'  {p}  {len(raw)}B')
t = raw.decode('utf-8', 'ignore')
print(f'  前 400 字符: {t[:400]}')
print(f'  含 aaaaabbbbbb: {"aaaaabbbbbb" in t}')
try:
    j = json.loads(t); print(f'  JSON 解析 OK; 顶层键: {list(j.keys())[:15]}')
except Exception as e:
    print(f'  JSON 解析失败: {e}')
# 与 d2b addendum 比对
for cand in sorted(RES.glob('_v4_pi_cot_v2_dataset_addendum*_2026_09_2*.json')):
    if hashlib.sha256(cand.read_bytes()).hexdigest() == hashlib.sha256(raw).hexdigest():
        print(f'  == 与 {cand.name} 逐字节相同')
print()
print('_wide_s4 DONE')
