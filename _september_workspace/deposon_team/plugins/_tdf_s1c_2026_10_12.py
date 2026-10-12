# -*- coding: utf-8 -*-
"""_tdf_s1c — Part 3：项 4 逐行复算 + 项 5 FIX-D 定位 + 项 6 模式提取 + 项 8 哈希级 + 项 9 引用链（只读）"""
import hashlib, json, os, re
from pathlib import Path
REPO = Path(r'D:\私人资料\deposon-repo'); RES = REPO / 'results'
def sha12b(b): return hashlib.sha256(b).hexdigest()[:12]
def sha12(p): return sha12b(Path(p).read_bytes())
def T(p): return Path(p).read_text(encoding='utf-8', errors='ignore')

print('='*104); print('项 4 · 九行逐行复算（表记 vs 本棒实测）'); print('='*104)
NINE = [
 ('17', 'T1.5r2 result',    'results/_v4_supp_t15r2_result.json',                          'c69ab0e3002e', 73526),
 ('18', 'T1.5r2 executor',  'results/_v4_supp_t15r2_executor.py',                           '4b5b720d5cda', 84884),
 ('19', 'T1.5r2 prereg',    'results/_v4_supp_prereg_v02_add_T15r2_2026_09_26.md',          '883dced872b4', 53923),
 ('20', 'T1.5r2 activation','results/_v4_supp_prereg_v02_add_T15r2_activation_2026_09_26.md','f6ed61c25572', 35977),
 ('21', 'T1.5 verdict',     'results/_v4_supp_t15_verdict.md',                              '52c985429c91', 55352),
 ('22', 'T1.5 prereg',      'results/_v4_supp_prereg_v02_add_T15_2026_09_24.md',            '8898b964a9d9', 76991),
 ('23', 'T1.5 activation',  'results/_v4_supp_prereg_v02_add_T15_activation_2026_09_24.md', '443efb39804a', 20751),
 ('24', 'T1.5 result',      'results/_v4_supp_t15_result.json',                             '6b47d389b7ae', 53265),
 ('25', 'T1.5 executor',    'results/_v4_supp_t15_executor.py',                             '558e635f9ba6', 62285),
]
n_bdiff = 0; n_sdiff = 0
for num, name, rel, s12, bsz in NINE:
    p = REPO / rel.replace('/', os.sep)
    if not p.exists():
        print(f'  #{num} {name}: MISSING {rel}'); continue
    b = p.read_bytes()
    s_ok = (sha12b(b) == s12); b_ok = (len(b) == bsz)
    n_bdiff += (not b_ok); n_sdiff += (not s_ok)
    print(f'  #{num} {name:<18} SHA {"=" if s_ok else "≠"} ({sha12b(b)})  bytes {"=" if b_ok else "≠"} {len(b):,} vs 表记 {bsz:,}  Δ={len(b)-bsz:+,}')
print(f'  ⇒ 9 行中字节不符 {n_bdiff} 行、SHA 不符 {n_sdiff} 行')

# activation CRLF 折算复现
act = REPO / 'results' / '_v4_supp_prereg_v02_add_T15r2_activation_2026_09_26.md'
if act.exists():
    b = act.read_bytes()
    n_lf = b.count(b'\n')
    print(f'  activation: bytes={len(b):,}  LF={n_lf}  CR={b.count(bytes([13]))}  BOM={b[:3]==bytes([0xEF,0xBB,0xBF])}')
    print(f'  CRLF 全量折算 = {len(b)+n_lf:,}（须 ≠ 35,977）')
    print(f'  表记 − 实测 = {35977-len(b):+,}（须 = −1,782）')
# T1.5 verdict 三时点读数核对
tv = REPO / 'results' / '_v4_supp_t15_verdict.md'
print(f'  T1.5 verdict 当前: {sha12(tv)} / {tv.stat().st_size:,} B（表记 52c985429c91/55,352；委托棒实测 52,884）')

print()
print('='*104); print('项 5 · FIX-D 定位（08c runs 结构）'); print('='*104)
r08c = json.loads(T(RES / '_v3_recheck_08c_preexp_data' / 'result_2026_09_27.json'))
runs = r08c['runs']
r0 = runs[0]
print(f'  run 键: {sorted(r0.keys())}')
# 按 fixture 分组找 FIX-D
fixtures = {}
for r in runs:
    fx = str(r.get('fixture') or r.get('fixture_id') or r.get('fixture_name') or '')
    fixtures.setdefault(fx, []).append(r)
for fx, rs in fixtures.items():
    print(f'  fixture "{fx}": {len(rs)} runs  例子键值: scheme={rs[0].get("scheme")} delta={rs[0].get("delta")} verdict={rs[0].get("verdict")}')
    for k in rs[0]:
        if 'delta' in k or 'r2' in k or 'ident' in k:
            print(f'      {k} = {rs[0][k]}')
# FIX-D 的 delta 分布
fixd = [r for r in runs if 'FIX-D' in json.dumps(r)]
print(f'  含 FIX-D 的 run = {len(fixd)}')
for r in fixd[:3]:
    print(f'    {json.dumps(r, ensure_ascii=False)[:300]}')
# 全 runs delta 分布
deltas = [r.get('delta') for r in runs]
print(f'  全 45 run delta 取值集: {sorted(set(str(d) for d in deltas))}')

print()
print('='*104); print('项 6 · PHRASE_PATTERNS_V3 提取（v3 executor）'); print('='*104)
ex = T(RES / '_v4_pi_cot_v3_ruleset_v3_executor.py')
i = [n for n, l in enumerate(ex.splitlines(), 1) if 'PHRASE_PATTERNS' in l]
for n in i[:6]:
    print(f'  L{n}: {ex.splitlines()[n-1][:150]}')
    for j in range(n, min(n+16, len(ex.splitlines()))):
        print(f'      L{j+1}: {ex.splitlines()[j][:130]}')
    print('  ---')

print()
print('='*104); print('项 8 · 旧值 c300e74a082c 作为「当前哈希」全仓复算'); print('='*104)
cnt_hash = 0
for dp, dns, fns in os.walk(REPO):
    dns[:] = [d for d in dns if d not in {'__pycache__','.git','.trae'}]
    for fn in fns:
        q = os.path.join(dp, fn)
        try:
            if os.path.getsize(q) > 20_000_000: continue
            if sha12(q) == 'c300e74a082c': cnt_hash += 1; print(f'      当前哈希命中: {q}')
        except Exception: continue
print(f'  作为当前哈希命中 = {cnt_hash} 件（须 = 0）')

print()
print('='*104); print('项 9 · BOM 17 件 + keypath 8 件 + 基线快照现值'); print('='*104)
BOMS = [r'.tmp\_en_verify_2026_09_28.py', r'.tmp\_en_verify2_2026_09_28.py', r'.tmp\_en_verify3_2026_09_28.py',
        r'.tmp\_en_verify4_2026_09_28.py', r'.tmp\_en_final_2026_09_28.py', r'.tmp\_probe21.py', r'.tmp\_hash21.py',
        r'.tmp\_c5_feasibility_probe.py', r'.tmp\_r4_cleanup_worker_keyscan_2026_09_29.py']
KEYS = [r'results\_v4_supp_t15_executor_r1_2026_09_27.py', r'results\_v4_supp_t15r2_executor_r1_2026_09_28.py',
        r'results\_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py', r'results\_v4_supp_t15_executor_r2_atomic_2026_09_28.py',
        r'results\_v4_supp_t15_executor_r3_2026_09_28.py', r'results\_v4_supp_t15r2_executor_r3_2026_09_28.py',
        r'results\_v4_supp_t15_executor_r0_atomic_2026_09_29.py', r'results\_v4_supp_t15r2_executor_r0_atomic_2026_09_29.py']
shas = {}
for rel in BOMS + KEYS:
    p = REPO / rel
    if p.exists(): shas[sha12(p)] = os.path.basename(rel)
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
n_bom = 0
for rel in BOMS:
    p = REPO / rel
    if p.exists() and p.read_bytes()[:3] == b'\xef\xbb\xbf': n_bom += 1
print(f'  repo/.tmp BOM 9 件现存 {n_bom}（归档区 8 件沿登记值，0 访问）')
for rel in BOMS:
    p = REPO / rel
    nm = os.path.basename(rel)
    if p.exists():
        h = found.get(nm, [])
        print(f'    BOM {nm:<42} 被引 {len(h)} 处')
for rel in KEYS:
    p = REPO / rel
    nm = os.path.basename(rel)
    h = found.get(nm, [])
    print(f'    KEY {nm:<44} 被引 {len(h)} 处（首3: {h[:3]}）')
# 基线快照现值（项 9 诚实标注要求）
bp = REPO / '.tmp' / 'verif_doubt6' / 'baseline_pre.json'
if bp.exists():
    print(f'  基线快照 baseline_pre.json 现值: {sha12(bp)} / {bp.stat().st_size:,} B')
    j = json.loads(T(bp))
    s = json.dumps(j, ensure_ascii=False)
    hits = [k for k, v in shas.items() if k in s]
    print(f'  快照内引用目标件 SHA 数: {len(hits)}')
else:
    print('  基线快照 baseline_pre.json MISSING')
print()
print('_tdf_s1c DONE')
