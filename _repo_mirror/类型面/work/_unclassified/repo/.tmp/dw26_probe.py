# -*- coding: utf-8 -*-
"""§26 一手会话记录回查探针（运行时拼接阴断串·避自写探针之假阳性）"""
import json, os, glob, hashlib

D = r'〔本地路径已脱敏〕'
MP = os.path.join(D, 'messages.jsonl')

b = open(MP, 'rb').read()
lines = [l for l in b.decode('utf-8', errors='replace').splitlines() if l.strip()]
recs, bad = [], 0
for l in lines:
    try:
        recs.append(json.loads(l))
    except Exception:
        bad += 1
print('MSG_BYTES', len(b))
print('MSG_LINES', len(lines))
print('PARSED', len(recs), 'BAD', bad)
print('MSG_SHA12', hashlib.sha256(b).hexdigest()[:12])

full = b.decode('utf-8', errors='replace')

# 正控（已知必存在之追加·PI 2026-10-30 令）
CTRL = [
    ('CTRL_1 直接更改委托稿', '\u76f4\u63a5\u66f4\u6539\u59d4\u6258\u7a3f'),
    ('CTRL_2 转发给上传方', '\u8f6c\u53d1\u7ed9\u4e0a\u4f20\u65b9'),
    ('CTRL_3 体例之正修三册', '\u4f53\u4f8b\u4e4b\u6b63\u4fee\u4e09\u518c'),
    ('CTRL_4 上下文已压缩', '\u4e0a\u4e0b\u6587\u5df2\u538b\u7f29'),
]
print('== CONTROLS ==')
for k, v in CTRL:
    print('  %-26s %d' % (k, full.count(v)))

# 阴断：运行时拼接（parts join），使字面不入探针源码之外的文件
neg_parts = ['\u4e0d', '\u5e94', '\u5b58', '\u5728', '\u4e4b', '\u4e32', 'Z', 'Q', 'X', '9']
neg = ''.join(neg_parts)
print('== NEGATIVES (runtime-built) ==')
print('  NEG_1 built-str        %d' % full.count(neg))
neg2 = ''.join(['\u4e0d', '\u5e94', '\u5b58', '\u5728', '\u4e4b', '\u4e32', 'W', 'Q', 'X', '7'])
print('  NEG_2 built-str        %d' % full.count(neg2))
print('  NEG_3 len1 ascii       %d' % full.count(''.join(['\u005a', '\u005a', '\u005a'])))

# 会话快照面：代次计数
snaps = sorted(glob.glob(os.path.join(D, 'snapshots', 'g*--ctx_*.jsonl')))
print('SNAP_FILES', len(snaps))
if snaps:
    print('SNAP_FIRST', os.path.basename(snaps[0]), os.path.getsize(snaps[0]))
    print('SNAP_LAST ', os.path.basename(snaps[-1]), os.path.getsize(snaps[-1]))
    tot = 0
    for p in snaps:
        with open(p, 'rb') as f:
            tot += sum(1 for _ in f)
    print('SNAP_TOTAL_LINES', tot)

# 抽取 PI 2026-10-30 令所在之 user 消息（逐条含行号）
def texts(rec):
    m = rec.get('message') or {}
    role = m.get('role') or rec.get('role') or m.get('author') or ''
    c = m.get('content')
    if isinstance(c, list):
        t = ''.join(x.get('text', '') for x in c if isinstance(x, dict))
    elif isinstance(c, str):
        t = c
    else:
        t = rec.get('content') if isinstance(rec.get('content'), str) else ''
    return str(role), t

KEYS = ['\u59d4\u6258\u51fd', '\u4e0a\u4f20\u65b9', '\u4f53\u4f8b\u4e4b\u6b63\u4fee\u4e09\u518c',
        '\u5b50\u4ee3\u7406\u518c', '\u72ec\u7acb\u81ea\u4fee']
print('== USER MSGS HITS (role=user & key) ==')
for i, r in enumerate(recs, 1):
    role, t = texts(r)
    if 'user' not in role.lower():
        continue
    if not t.strip():
        continue
    hit = [k for k in KEYS if k in t]
    if hit:
        print('  L%d role=%s keys=%s :: %s' % (i, role, '/'.join(hit), t.replace('\n', ' | ')[:220]))

print('== USER MSGS COUNT ==')
n = 0
for i, r in enumerate(recs, 1):
    role, t = texts(r)
    if 'user' in role.lower() and t.strip():
        n += 1
print('  USER_MSGS', n)

# 本棒（doc-writer）自身派工单之在场：搜棒号/子会话 id
print('== SELF DISPATCH PROBE ==')
for k, v in (('my session id', 'mvs_8574f789e4f4421dac486ffaf096b87e'),
             ('parent session id', 'mvs_bbeb804b1a6a41109be740636eed1709'),
             ('agent id', 'agent-0032834a3e04')):
    print('  %-20s %d' % (k, full.count(v)))
