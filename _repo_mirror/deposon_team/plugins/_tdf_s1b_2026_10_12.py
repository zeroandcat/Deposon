# -*- coding: utf-8 -*-
"""_tdf_s1b — Part 2：项 4 表原文 + 项 5/6/7/8/10/11/12 验收机检（只读；归档区 0 访问）"""
import hashlib, json, os, re
from pathlib import Path
REPO = Path(r'D:\私人资料\deposon-repo'); RES = REPO / 'results'
def sha12b(b): return hashlib.sha256(b).hexdigest()[:12]
def sha12(p): return sha12b(Path(p).read_bytes())
def T(p): return Path(p).read_text(encoding='utf-8', errors='ignore')

print('='*104); print('项 4 · verdict §0 表原文定位'); print('='*104)
vt = RES / '_v4_supp_t15r2_verdict.md'
tvt = T(vt)
ls = tvt.splitlines()
start = next((i for i, l in enumerate(ls) if l.startswith('#') and '§0' in l), 0)
end = next((i for i, l in enumerate(ls[start+1:], start+1) if l.startswith('#')), len(ls))
for i in range(start, min(end, start+40)):
    print(f'  L{i+1}: {ls[i][:150]}')

print()
print('='*104); print('项 4 补充 · t15r2 result/executor/activation 实际文件名'); print('='*104)
for pat in ('_v4_supp_t15r2_*', '_v4_supp_t15r2_activation*'):
    for p in sorted(RES.glob(pat)):
        print(f'  {p.name}  {sha12(p)}  {p.stat().st_size:,} B')

print()
print('='*104); print('项 5 · B11 FIX-D vs no-op（08c result）'); print('='*104)
r08c = json.loads(T(RES / '_v3_recheck_08c_preexp_data' / 'result_2026_09_27.json'))
def walk(o, path=''):
    if isinstance(o, dict):
        for k, v in o.items(): yield from walk(v, path+'/'+k)
    elif isinstance(o, list):
        for i, v in enumerate(o): yield from walk(v, f'{path}[{i}]')
    else: yield path, o
runs = r08c.get('runs', [])
fixd_delta = [r.get('delta') for r in runs if r.get('scheme')=='FIX-D' or 'FIX-D' in str(r.get('scheme_id','')) or 'FIX-D' in str(r.get('label',''))]
# 通用：找 delta 字段
n_fixd = 0; fixd_zeros = 0; noop_nulls = 0; ident_undef = 0
for r in runs:
    sid = str(r.get('scheme') or r.get('scheme_id') or r.get('scheme_name') or '')
    if 'FIX-D' in sid:
        n_fixd += 1
        d = r.get('delta', r.get('delta_r2', 'ABSENT'))
        if d == 0.0: fixd_zeros += 1
    if 'no-op' in sid.lower() or 'noop' in sid.lower():
        v = r.get('verdict', r.get('gate_verdict', 'ABSENT'))
        if v is None: noop_nulls += 1
print(f'  runs 总数 = {len(runs)}')
print(f'  FIX-D 条数 = {n_fixd}，delta == 0.0 计数 = {fixd_zeros}')
print(f'  no-op 门判 null 计数 = {noop_nulls}')
# 恒等族字段是否存在于 result 键面
allkeys = set()
def keyset(o, path=''):
    if isinstance(o, dict):
        for k, v in o.items():
            allkeys.add(k); keyset(v, path+'/'+k)
    elif isinstance(o, list):
        for v in o: keyset(v, path)
keyset(r08c)
ident_fields = [k for k in allkeys if 'ident' in k.lower() or 'two_point' in k.lower() or 'ss_tot' in k.lower()]
print(f'  恒等族相关键: {sorted(ident_fields)[:10]}')
# 逐 run 列 scheme 样本
schemes = {}
for r in runs[:60]:
    sid = str(r.get('scheme') or r.get('scheme_id') or '')
    schemes[sid] = schemes.get(sid, 0) + 1
print(f'  scheme 分布: {schemes}')

print()
print('='*104); print('项 6 · B13 PHRASE_PATTERNS_V3'); print('='*104)
ex = T(RES / '_v4_pi_cot_v3_ruleset_v3_executor.py')
m = re.search(r'PHRASE_PATTERNS_V3\s*=\s*\[([\s\S]*?)\]', ex)
pats = re.findall(r"'([^']+)'", m.group(1)) if m else []
print(f'  PHRASE_PATTERNS_V3 长度 = {len(pats)}')
print(f'  全列: {pats}')
print(f"  '大一统定义' in pats: {'大一统定义' in pats}  下标 = {pats.index('大一统定义') if '大一统定义' in pats else 'X'}")
print(f"  '判据序列' in pats: {'判据序列' in pats}  下标 = {pats.index('判据序列') if '判据序列' in pats else 'X'}")
print(f"  '万物理论' in pats: {'万物理论' in pats}  '判据优先序' in pats: {'判据优先序' in pats}")
rsv = json.loads(T(RES / '_v4_pi_cot_v3_ruleset_v3.json'))
phrase_keys = [k for k in str(rsv) if False]
pp = rsv.get('phrase_patterns_v3') or rsv.get('phrase_patterns')
if pp:
    print(f'  ruleset phrase 类数 = {len(pp)}: {[str(x)[:40] for x in pp]}')

print()
print('='*104); print('项 7 · 勘误件现值五项 + 3 跳点'); print('='*104)
err = REPO / 'docs' / 'V3X' / 'TRAE_V3_ASSET_ERRATUM_2026_09_23.md'
b = err.read_bytes()
print(f'  SHA-12 = {sha12b(b)}  bytes = {len(b):,}  首3字节 = {b[:3].hex()}  CR = {b.count(bytes([13]))}  LF = {b.count(bytes([10]))}')
# 3 个跳点：从件内抽取 v25-v36 登记字节（如「857,551」等）
t = b.decode('utf-8', 'ignore')
for m3 in re.finditer(r'(v2[4-9]|v3[0-6])[^\n]{0,60}?([\d,]{6,9})\s*B', t):
    pass
# 直接找版本头行
ver_lines = [(i+1, l.strip()[:120]) for i, l in enumerate(t.splitlines()) if re.match(r'^>\s*[-*]?\s*[^|]*v(2[4-9]|3[0-6])', l.strip()) or ('当前版本' in l and 'B' in l)]
for i, l in ver_lines[:12]:
    print(f'  L{i}: {l}')
# 找 62eed1f4dfa0（v24）与 v25 值
for kw in ('62eed1f4dfa0', 'v25', 'v36', '当前'):
    hits = [(i+1, l.strip()[:130]) for i, l in enumerate(t.splitlines()) if kw in l]
    print(f'  含 "{kw}" 行 {len(hits)} 处（前3）:')
    for i, l in hits[:3]:
        print(f'      L{i}: {l}')

print()
print('='*104); print('项 8 · 勘误件 L4009/L4013 + 26b 现值 + 旧值全仓'); print('='*104)
ls = t.splitlines()
for ln in (4009, 4013):
    print(f'  L{ln}: {ls[ln-1][:160]}')
r26b = RES / '_v3_recheck_26b_rescript_2026_09_27.md'
print(f'  26b rescript 现值: {sha12(r26b)} / {r26b.stat().st_size:,} B (委托记 ae81d9b59054/30,552)')
# 旧值 c300e74a082c 全仓命中（排除归档区）
cnt = 0; where = []
for dp, dns, fns in os.walk(REPO):
    dns[:] = [d for d in dns if d not in {'__pycache__','.git','.trae'}]
    for fn in fns:
        if not fn.endswith(('.md','.json','.txt','.py','.tsv')): continue
        q = os.path.join(dp, fn)
        try:
            if os.path.getsize(q) > 12_000_000: continue
            tt = open(q,'rb').read().decode('utf-8','ignore')
        except Exception: continue
        n = tt.count('c300e74a082c')
        if n:
            # 排除「登记文本自身引用」：只统计作为「当前哈希」出现的（无法机械区分，先报全文）
            cnt += n; where.append((q.replace(str(REPO)+os.sep,''), n))
print(f'  "c300e74a082c" 全仓（repo，含文本引用）命中 {cnt} 处:')
for w, n in where[:12]:
    print(f'      {w}  x{n}')

print()
print('='*104); print('项 10 · 五锚机检'); print('='*104)
plc = REPO / 'tools' / 'llm_client.py'
print(f'  llm_client: {sha12(plc)} / {plc.stat().st_size:,} B (委托记 1722500da4aa/8,118)')
t_lc = T(plc)
print(f'  version 字面命中数 = {len(re.findall(chr(39)+r'version'+chr(39), t_lc))} + {t_lc.count('2026-09-11')}')
gt = sorted(RES.glob('deposon_v20_gt*.json'))
print(f'  deposon_v20_gt*.json = {len(gt)} 件')
dc = list(REPO.rglob('*distortion_calculator*'))
print(f'  *distortion_calculator* = {len(dc)} 命中')
spec = REPO / 'docs' / 'V3X' / 'P_B_DISTORTION_BOUND_V0_SPEC.md'
print(f'  P_B spec 现值: {sha12(spec)} / {spec.stat().st_size:,} B (委托记 423c84de20d5/15,457; 我 09-30 回函载 bb7ca9838150/7,126)')
t_sp = T(spec)
print(f'  KILL_LINE 路径级点名: {re.findall(r'GT[^\\n]{0,50}(\\.json|\\.md|verifier[^\\s]{0,40})', t_sp)[:5]}')

print()
print('='*104); print('项 11 · 撞名双副本'); print('='*104)
for rel in ('letters/trae_walkthrough_bugfix_audit_request_2026_09_30.md',
            'letters/TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md',
            '.tmp/_docwriter_wt2_enum_2026_09_30.tsv',
            '.tmp/_docwriter_wt2_enum_final_2026_09_30.tsv'):
    p = REPO / rel.replace('/', os.sep)
    if p.exists():
        print(f'  {sha12(p)}  {p.stat().st_size:,} B  {rel}')
    else:
        print(f'  MISSING  {rel}')

print()
print('='*104); print('项 12 · 混合体现状（仓内面；归档区 0 访问）'); print('='*104)
r3 = RES / '_v5_trae_doubt6_verify_2026_09_28_r3verifier.md'
print(f'  r3verifier: {sha12(r3)} / {r3.stat().st_size:,} B (委托记 58101ef93a6f/30,192)')
orig = RES / '_v5_trae_doubt6_verify_2026_09_28.md'
print(f'  原路径 Test-Path = {orig.exists()}')

print()
print('_tdf_s1b DONE')
