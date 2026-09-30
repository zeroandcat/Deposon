# -*- coding: utf-8 -*-
"""_v4_wt_s5_verify — §C 关键断言核验 + B5/B7 落地面核验（只读）"""
import hashlib, json, os, re
from pathlib import Path

REPO = Path(r'D:\私人资料\deposon-repo')
RES = REPO / 'results'

def sha12(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]

def read(p):
    return Path(p).read_text(encoding='utf-8')

print('=' * 100)
print('A. 断言核验：S1/S2/短语预实验 executor 是否 import 母件装载器 load_all_events_v3')
print('=' * 100)
for rel in [r'_v3_s1_executor\executor_2026_09_27.py',
            r'_v3_s2_executor\executor_2026_09_27.py',
            r'_v3_s_phrasetemplate_preexp_data\executor_2026_09_27.py',
            r'_v3_recheck_08c_preexp_data\executor_2026_09_27.py']:
    p = RES / rel
    t = read(p)
    n_load = t.count('load_all_events_v3')
    n_sup = t.count('critical_reflection_supplement')
    n_imp = len(re.findall(r'load_mod|importlib.*spec_from_file_location', t))
    imp_v3 = 'ruleset_v3_executor' in t
    print(f'  {rel}')
    print(f'      load_all_events_v3 x{n_load} | critical_reflection_supplement x{n_sup} | import 母件={imp_v3} | load_mod x{n_imp}')

print()
print('=' * 100)
print('B. 断言核验：S1/S2 result 的 f1_unjudgeable_idx 是否含 37/39')
print('=' * 100)
for rel in [r'_v3_s1_executor\result_2026_09_27.json', r'_v3_s2_executor\result_2026_09_27.json']:
    j = json.loads(read(RES / rel))
    def find(o, k, path=''):
        out = []
        if isinstance(o, dict):
            for kk, vv in o.items():
                if kk == k:
                    out.append((path + '/' + kk, vv))
                out += find(vv, k, path + '/' + kk)
        elif isinstance(o, list):
            for i, vv in enumerate(o):
                out += find(vv, k, f'{path}[{i}]')
        return out
    hits = find(j, 'f1_unjudgeable_idx')
    print(f'  {rel}: {len(hits)} 处')
    for pth, v in hits[:3]:
        print(f'      {pth} = {v}')

print()
print('=' * 100)
print('C. 断言核验：D1_supp 3 件源件字段 + 底料中是否重复成 3 新事件')
print('=' * 100)
add = json.loads(read(RES / '_v4_pi_cot_v2_dataset_addendum_2026_09_24.json'))
sups = add.get('supplements', add if isinstance(add, list) else [])
print(f'  addendum supplements n={len(sups)}')
for s in sups:
    print(f"      event_id={s.get('event_id')} q_id={s.get('q_id')} keys={sorted(s.keys())}")

v2ds = json.loads(read(RES / '_v4_pi_cot_v2_dataset.json'))
v3ds = json.loads(read(RES / '_v4_pi_cot_v3_dataset.json'))
print(f'  v2 dataset 顶层键: {list(v2ds.keys())[:12]}')
print(f'  v3 dataset 顶层键: {list(v3ds.keys())[:12]}')

print()
print('=' * 100)
print('D. B5 落地面：alt_reading_definition 文件 + 关键结论')
print('=' * 100)
p = RES / '_v4_pi_cot_v3_alt_reading_definition_2026_09_27.md'
t = read(p)
print(f'  {p.name}  sha12={sha12(p)}  {os.path.getsize(p)}B')
for ln in t.splitlines()[:40]:
    if any(w in ln for w in ('结论', '可反推', '不可反推', '复现', '定义')):
        print(f'      | {ln[:130]}')

print()
print('=' * 100)
print('E. B7 落地面：d4_relabel + dataset_v1p3 的 judge_type 改动')
print('=' * 100)
p = RES / '_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json'
j = json.loads(read(p))
print(f'  {p.name} sha12={sha12(p)} {os.path.getsize(p)}B')
print(f'  顶层键: {list(j.keys())[:15]}')
t = json.dumps(j, ensure_ascii=False)
for m in re.finditer(r'"D4_Q\d"[^}]{0,160}', t):
    print('      | ' + m.group(0)[:160])

print()
print('=' * 100)
print('F. 勘误链 E-41.x 现占用者（B2/§C D1 相关）')
print('=' * 100)
err = read(REPO / 'docs' / 'V3X' / 'TRAE_V3_ASSET_ERRATUM_2026_09_23.md')
print(f'  erratum sha12={sha12(REPO / "docs" / "V3X" / "TRAE_V3_ASSET_ERRATUM_2026_09_23.md")}  {os.path.getsize(REPO / "docs" / "V3X" / "TRAE_V3_ASSET_ERRATUM_2026_09_23.md")}B')
for pat in [r'E-41\.\d+[^\n]{0,90}', r'E-42\.\d+[^\n]{0,90}', r'E-43\.\d+[^\n]{0,90}']:
    hits = re.findall(pat, err)
    print(f'  {pat[:6]} 命中 {len(hits)} 处（前 4）:')
    for h in hits[:4]:
        print(f'      | {h[:110]}')
print(f'  全件含 "_v3_recheck_" 次数: {err.count("_v3_recheck_")}')

print()
print('=' * 100)
print('G. B2 断言核验：v1 §0.2 表 SHA 列 vs 盘上实测')
print('=' * 100)
v1 = read(RES / '_v3_recheck_prereg_v1_2026_09_27.md')
print(f'  prereg_v1 sha12={sha12(RES / "_v3_recheck_prereg_v1_2026_09_27.md")}  {os.path.getsize(RES / "_v3_recheck_prereg_v1_2026_09_27.md")}B')
# 抓 §0.2 表行
lines = v1.splitlines()
in_tbl = False
rows = []
for i, ln in enumerate(lines):
    if '0.2' in ln and ('SHA' in ln or '表' in ln):
        in_tbl = True
    if in_tbl and ln.strip().startswith('|') and ln.count('|') >= 4:
        rows.append((i + 1, ln))
    if in_tbl and len(rows) > 22:
        break
print(f'  §0.2 区抓取 {len(rows)} 行:')
for ln_no, r in rows[:20]:
    print(f'      L{ln_no}: {r[:150]}')

print()
print('_wt_s5 DONE')
