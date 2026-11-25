import json

# ---------- Q4: 52 form-candidate rows ----------
d4 = json.load(open(r'.tmp\_b12_q4_exact_criteria_results_2026_09_29.json', encoding='utf-8')) \
    if False else json.load(open(r'.tmp\_b12_q4_exact_criteria_2026_09_29.json', encoding='utf-8'))
rows4 = d4['rows']

SHORT = {
    'CODE_REFERENCE/short_alnum_tail_below_key_threshold': 'CR/短尾',
    'CODE_REFERENCE/env_or_header_reference': 'CR/环境变量·头',
    'CODE_REFERENCE/provider_prefix_constant': 'CR/前缀常量',
}

out = []
out.append('| # | 根 | 字节 | SHA-12 | 形态命中 | alnum run 长度 | 形态类别 | 件（相对根） |')
out.append('|---:|---|---:|---|---:|---|---|---|')
for i, r in enumerate(rows4, 1):
    cats = ' + '.join(SHORT.get(k, k) for k in r['categories'])
    out.append(f"| {i} | {r['root']} | {r['bytes']:,} | `{r['sha12']}` | {r['hits']} | "
               f"{r['run_len_min']}–{r['run_len_max']} | {cats} | `{r['rel']}` |")
open(r'.tmp\_b12_q4_table.md', 'w', encoding='utf-8').write('\n'.join(out))
print('q4 rows:', len(rows4))

# ---------- Q1: reference rows ----------
d1 = json.load(open(r'.tmp\_b12_q1_refs_results_2026_09_29.json', encoding='utf-8'))
rows1 = d1['rows']
CUT = '2026-09-29 14:12:44'
pre = [r for r in rows1 if r['mtime'] < CUT]
out = []
out.append('| # | 树 | SHA-12 | 字节 | 命中数 | 命中行号 | 引用形态 | mtime | 件 |')
out.append('|---:|---|---|---:|---:|---|---|---|---|')
for i, r in enumerate(pre, 1):
    forms = ' + '.join(f'{k}×{v}' for k, v in r['forms'].items())
    lines = ','.join(str(x) for x in r['lines'][:6]) + ('…' if len(r['lines']) > 6 else '')
    out.append(f"| {i} | {r['tree']} | `{r['sha12']}` | {r['bytes']:,} | {r['hit_count']} | "
               f"{lines} | {forms} | {r['mtime']} | `{r['rel']}` |")
open(r'.tmp\_b12_q1_table.md', 'w', encoding='utf-8').write('\n'.join(out))
print('q1 rows (pre-cut):', len(pre))
