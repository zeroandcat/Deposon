# -*- coding: utf-8 -*-
"""_v4_wide_s3b_uuidctx — 判定 _l14v3_aggregated_10cells.json 的 UUID 是否真 key（只读）"""
import json, os, re
from pathlib import Path
REPO = Path(r'D:\私人资料\deposon-repo')
p = REPO / '.tmp' / '_l14v3_aggregated_10cells.json'
print(f'件: {p}  {p.stat().st_size:,}B')
txt = p.read_text(encoding='utf-8', errors='ignore')
print(f'行数: {len(txt.splitlines())}')
UUID = re.compile(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')
# 命中所在行的上下文（取首次出现的 5 处，打印前后各 1 行）
lines = txt.splitlines()
shown = 0
for i, ln in enumerate(lines):
    if UUID.search(ln):
        print(f'\n--- L{i+1} 命中 ---')
        for j in range(max(0, i-2), min(len(lines), i+3)):
            mark = '>>' if j == i else '  '
            print(f' {mark} L{j+1}: {lines[j][:230]}')
        shown += 1
        if shown >= 5: break

# 该 UUID 出现的字段名统计
keys = {}
for m in re.finditer(r'"([A-Za-z0-9_]+)"\s*:\s*"([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})"', txt):
    keys[m.group(1)] = keys.get(m.group(1), 0) + 1
print('\n=== UUID 值所挂字段名统计 ===')
for k, v in sorted(keys.items(), key=lambda x: -x[1]):
    print(f'  {k:<34} {v}')

# 顶层结构
j = json.loads(txt)
print('\n=== 顶层键 ===')
print(' ', list(j.keys())[:20] if isinstance(j, dict) else f'list[{len(j)}]')
# 唯一 UUID 数
uniq = set(UUID.findall(txt))
print(f'\n唯一 UUID 数 = {len(uniq)}')
# 是否与 request_id 类字段同现
for name in ('request_id', 'id', 'trace', 'key', 'token', 'authorization', 'Authorization'):
    print(f'  含 "{name}" 次数: {txt.count(name)}')
print('_wide_s3b DONE')
