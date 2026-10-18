# -*- coding: utf-8 -*-
"""
_tdf_s1_2026_10_12.py — 项 1–12 验收判准机检（只读；归档区 0 访问）
沿委托 §3.2「succeeded ≠ 跑完」：每项附可复算读数。
"""
import hashlib, json, os, re
from pathlib import Path

REPO = Path(r'_september_workspace'); RES = REPO / 'results'
def sha12b(b): return hashlib.sha256(b).hexdigest()[:12]
def sha12(p): return sha12b(Path(p).read_bytes())
def T(p): return Path(p).read_text(encoding='utf-8', errors='ignore')

print('='*104); print('项 1 · C-7 19 项特征（S2 rescript + result）'); print('='*104)
r1 = RES / '_v3_s2_executor' / 'rescript_2026_09_27.md'
r1j = RES / '_v3_s2_executor' / 'result_2026_09_27.json'
print(f'  rescript 现值: {sha12(r1)} / {r1.stat().st_size:,} B (委托记 331022480a57/23,039)')
j = json.loads(T(r1j))
print(f'  result 现值:   {sha12(r1j)} / {r1j.stat().st_size:,} B (委托记 d73d51e670de/51,039)')
ce = j['construction_equivalence']
print(f"  v3_n_features={ce['v3_n_features']}  n_features_used_v3={ce['n_features_used_v3']}  n_features_used_repro={ce['n_features_used_repro']}")
fu = ce['features_used_v3']
from collections import Counter
c = Counter(fu)
print(f'  features_used_v3 distinct={len(set(fu))} 总项次={len(fu)}')
for k, v in sorted(c.items(), key=lambda x: -x[1]):
    print(f'      {k:<24} x{v}')
EXPECT9 = {'is_corr_pair','judge_type_J1','judge_type_J2','judge_type_J3','n_keywords_hit','opt_bucket_8','rf_len_bucket','rf_pos_density','scene_bucket_8'}
print(f'  distinct 9 键 ⊆ 委托列 9 键: {set(fu) <= EXPECT9 and len(set(fu))==9}')
ls = T(r1).splitlines()
print(f'  L48: {ls[47][:80]}')
print(f'  L49: {ls[48][:80]}')
print(f'  L32: {ls[31][:80]}')

print()
print('='*104); print('项 2 · C-8 r2_function_sha12 null 成因'); print('='*104)
import importlib.util, sys
e08b_path = RES / '_v3_recheck_08b_executor' / 'executor_2026_09_27.py'
print(f'  08b executor: {sha12(e08b_path)} / {e08b_path.stat().st_size:,} B (委托记 b292410d9a69/43,901)')
spec = importlib.util.spec_from_file_location('e08b', str(e08b_path))
m = importlib.util.module_from_spec(spec); sys.modules['e08b'] = m; spec.loader.exec_module(m)
print(f'  hasattr(ex08b,"sha12_file") = {hasattr(m,"sha12_file")}')
print(f'  hasattr(ex08b,"sha12")      = {hasattr(m,"sha12")}')
print(f'  修正实现产出: ex08b.sha12(08b executor bytes) = {m.sha12(e08b_path.read_bytes())}  (期望 b292410d9a69)')
e08c = RES / '_v3_recheck_08c_preexp_data' / 'executor_2026_09_27.py'
r08c = RES / '_v3_recheck_08c_preexp_data' / 'result_2026_09_27.json'
print(f'  08c executor: {sha12(e08c)} / {e08c.stat().st_size:,} B (委托记 cb6eb9164df3/37,775)')
print(f'  08c result:   {sha12(r08c)} / {r08c.stat().st_size:,} B (委托记 689a6e4427a8/146,601)')
t = T(e08c)
i526 = [i for i, l in enumerate(t.splitlines(), 1) if 'hasattr' in l]
for i in i526[:3]:
    print(f'  08c executor L{i}: {t.splitlines()[i-1].strip()[:110]}')

print()
print('='*104); print('项 3 · C-9 T4 冻结表 9 标量 + 差集'); print('='*104)
ept = RES / '_v3_s_phrasetemplate_preexp_data' / 'executor_2026_09_27.py'
rpt = RES / '_v3_s_phrasetemplate_preexp_data' / 'rescript_2026_09_27.md'
print(f'  短语 executor: {sha12(ept)} / {ept.stat().st_size:,} B (委托记 96f491a8e2bf/35,555)')
print(f'  短语 rescript: {sha12(rpt)} / {rpt.stat().st_size:,} B (委托记 6df402298557/14,510)')
t2 = T(ept)
m2 = re.search(r'T4_FROZEN_READINGS\s*=\.*?\{', t2)
mm = re.search(r'"rows"\s*:\s*\{([^}]*)\}', t2, re.S)
keys = re.findall(r'"([a-z0-9_]+)"\s*:', mm.group(1)) if mm else []
print(f'  T4 rows 键数 = {len(keys)}: {keys}')
s2rows = j['t4_same_substrate_comparison']['rows']
s2keys = set()
for row in s2rows:
    s2keys.add(row.get('metric') or row.get('name') or str(list(row.keys())[:2]))
pt_keys = set(keys)
print(f'  S2 8 行键: {sorted(s2keys)}')
nonT4 = [k for k in keys if k not in s2keys and not any(k in str(r) for r in s2rows)]
print(f'  非 T-4 键（4 键差集）: {sorted(set(keys) - set(map(str, s2keys)))}')

print()
print('='*104); print('项 4 · B9 t15r2 verdict §0 九行链复算'); print('='*104)
vt = RES / '_v4_supp_t15r2_verdict.md'
print(f'  verdict 件现值: {sha12(vt)} / {vt.stat().st_size:,} B (委托 0 实测, 本棒补齐)')
tvt = T(vt)
sec0 = tvt.split('## §0')[1].split('## §')[0] if '## §0' in tvt else tvt[:3000]
rowpat = re.findall(r'\|\s*#?(\d+)\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([0-9,]+)\s*\|\s*([0-9a-fA-F]{12})\s*\|', sec0)
if not rowpat:
    rowpat = re.findall(r'\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([\d,]+)\s*\|\s*([0-9a-fA-F]{12})', tvt)
print(f'  §0 表行抽取 {len(rowpat)} 行')
mapping = [
 ('17', 'T15r2 result', 'results/_v4_supp_t15r2_result_2026_09_28.json'),
 ('18', 'T15r2 executor', 'results/_v4_supp_t15r2_executor_2026_09_28.py'),
 ('19', 'T15r2 prereg', 'results/_v4_supp_prereg_v02_add_T15r2_2026_09_26.md'),
 ('20', 'T15r2 activation', 'results/_v4_supp_t15r2_activation_2026_09_26.md'),
 ('21', 'T15 verdict', 'results/_v4_supp_t15_verdict.md'),
 ('22', 'T15r2 verdict', None),
]
for num, name, rel in mapping:
    if rel is None: continue
    p = REPO / rel
    if not p.exists():
        print(f'  #{num} {name}: MISSING {rel}'); continue
    b = p.read_bytes()
    print(f'  #{num} {name}: 实测 {len(b):,} B / {sha12b(b)}  @{rel}')
for line in tvt.splitlines():
    if re.match(r'^\|\s*1[7-9]\s*\|', line) or re.match(r'^\|\s*2[0-5]\s*\|', line):
        print(f'    RAW: {line[:150]}')

# 项 4 CRLF 折算
act = REPO / 'results' / '_v4_supp_t15r2_activation_2026_09_26.md'
if act.exists():
    b = act.read_bytes()
    n_lf = b.count(b'\n'); n_cr = b.count(b'\r')
    print(f'  activation: bytes={len(b):,} LF={n_lf} CR={n_cr} BOM={b[:3]==bytes([0xEF,0xBB,0xBF])}')
    print(f'  CRLF 全量折算 = {len(b)+n_lf:,} (须 ≠ 35,977)')

print()
print('_tdf_s1 PART1 DONE')
