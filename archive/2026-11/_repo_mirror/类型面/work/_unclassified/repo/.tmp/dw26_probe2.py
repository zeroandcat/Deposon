# -*- coding: utf-8 -*-
"""§26 探针二：记录形态枚举 + 派工/PI令定位 + 台账只读取本棒"""
import json, os, sqlite3, datetime

D = r'〔本地路径已脱敏〕'
MP = os.path.join(D, 'messages.jsonl')
b = open(MP, 'rb').read()
lines = [l for l in b.decode('utf-8', errors='replace').splitlines() if l.strip()]
recs = [json.loads(l) for l in lines]

print('== RECORD SHAPE ==')
from collections import Counter
print('topkeys', Counter(tuple(sorted(r.keys())) for r in recs).most_common(6))
for i, r in enumerate(recs[:3], 1):
    print('  L%d keys=%s' % (i, sorted(r.keys())))

def role_of(r):
    m = r.get('message')
    if isinstance(m, dict):
        return str(m.get('role') or m.get('author') or '')
    return str(r.get('role') or r.get('type') or r.get('author') or '')

def text_of(r):
    m = r.get('message')
    src = m if isinstance(m, dict) else r
    c = src.get('content')
    if isinstance(c, list):
        parts = []
        for x in c:
            if isinstance(x, dict):
                parts.append(str(x.get('text') or x.get('thinking') or ''))
        return '\n'.join(parts)
    if isinstance(c, str):
        return c
    return ''

print('== ROLE DIST ==')
print(' ', Counter(role_of(r) for r in recs).most_common())

KEYS = {
    'PI_委托函': '\u59d4\u6258\u51fd',
    'PI_上传方': '\u4e0a\u4f20\u65b9',
    'PI_体例之正修三册': '\u4f53\u4f8b\u4e4b\u6b63\u4fee\u4e09\u518c',
    'PI_上下文已压缩': '\u4e0a\u4e0b\u6587\u5df2\u538b\u7f29',
    '棒号bg_': 'bg_',
    'doc-writer': 'doc-writer',
    '子代理册': '\u5b50\u4ee3\u7406\u518c',
}
print('== HIT LINES (role, key, snippet) ==')
for i, r in enumerate(recs, 1):
    t = text_of(r)
    if not t.strip():
        continue
    hit = [k for k in KEYS if k in t]
    if not hit:
        continue
    if role_of(r) != 'user':
        continue
    print('  L%d [%s] %s' % (i, '/'.join(hit), t.replace('\n', ' | ')[:300]))
    print('      ...tail: %s' % t.replace('\n', ' | ')[-260:])
    print()

print('== ALL bg_ IDS IN messages.jsonl ==')
import re
ids = sorted(set(re.findall(r'bg_[0-9a-f]{8}', b.decode('utf-8', 'replace'))))
print('  distinct', len(ids))
print(' ', ids)
