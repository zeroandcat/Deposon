# -*- coding: utf-8 -*-
"""§26 探针三：PI令行号定位 + 本棒台账只读取"""
import json, os, sqlite3, re, datetime

D = r'〔本地路径已脱敏〕'
MP = os.path.join(D, 'messages.jsonl')
b = open(MP, 'rb').read()
lines = [l for l in b.decode('utf-8', errors='replace').splitlines() if l.strip()]
recs = [json.loads(l) for l in lines]

print('== L80 RAW SHAPE ==')
for idx in (80,):
    r = recs[idx - 1]
    s = json.dumps(r, ensure_ascii=False)
    print('  len', len(s))
    print('  head:', s[:900])
    print('  tail:', s[-1400:])

print()
print('== LINES CONTAINING agent-0032834a3e04 ==')
for i, r in enumerate(recs, 1):
    s = json.dumps(r, ensure_ascii=False)
    if 'agent-0032834a3e04' in s:
        print('  L%d role=%s' % (i, (r.get('message') or {}).get('role')))
        for m in re.finditer(r'.{170}agent-0032834a3e04.{170}', s):
            print('     ...%s...' % m.group(0).replace('\n', ' | '))
        print()

print('== LINES CONTAINING task_background ==')
for i, r in enumerate(recs, 1):
    s = json.dumps(r, ensure_ascii=False)
    if 'task_background' in s:
        for m in re.finditer(r'<task_background[^>]*>', s):
            print('  L%d %s' % (i, m.group(0)))

print()
print('== SQLITE LEDGER (read-only) ==')
LED = r'〔本地路径已脱敏〕'
print('  size', os.path.getsize(LED))
con = sqlite3.connect('file:' + LED.replace('\\', '/') + '?mode=ro', uri=True)
cur = con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tabs = [r[0] for r in cur.fetchall()]
print('  tables', tabs)

T = 'local_runtime_background_tasks'
cur.execute("PRAGMA table_info(%s)" % T)
cols = [r[1] for r in cur.fetchall()]
print('  cols', cols)

MY_SID = 'mvs_8574f789e4f4421dac486ffaf096b87e'
PARENT = 'mvs_bbeb804b1a6a41109be740636eed1709'

def q(sql, args=()):
    cur.execute(sql, args)
    return cur.fetchall()

# 本棒：childSessionId 含 MY_SID
try:
    rows = q("SELECT task_id, kind, status, created_at_ms, ended_at_ms, owner_session_id FROM %s WHERE record_json LIKE ?" % T, ('%' + MY_SID + '%',))
    print('  MY ROD (childSessionId match):', len(rows))
    for r in rows:
        print('   ', r)
except Exception as e:
    print('  MY ROD query failed:', e)

cur.execute("PRAGMA table_info(%s)" % T)
cols = [r[1] for r in cur.fetchall()]
print('  cols2', cols)
try:
    cur.execute("SELECT * FROM %s ORDER BY rowid DESC LIMIT 1" % T)
    last = cur.fetchone()
    print('  last row len', len(last))
    for c, v in zip(cols, last):
        sv = str(v)
        print('    %-22s %s' % (c, sv[:120]))
except Exception as e:
    print('  last row failed:', e)
con.close()
