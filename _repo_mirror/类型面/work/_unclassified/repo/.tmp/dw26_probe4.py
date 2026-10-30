# -*- coding: utf-8 -*-
"""§26 探针四：新窗之棒况 + 委托函面 + 会话树 + 快照代次"""
import json, os, sqlite3, hashlib, glob, datetime, base64

TZ = datetime.timezone(datetime.timedelta(hours=8))
def ts(ms):
    return datetime.datetime.fromtimestamp(ms / 1000, TZ).strftime('%Y-%m-%d %H:%M:%S')

W25_END = 1793252556590          # §24 棒讫（§25 之起）— 备注：§25 观测时点 20:52
W26_START = 1793253120000         # 粗取 §25 观测时点 20:52:00
print('W26_START human', ts(W26_START))

LED = r'〔本地路径已脱敏〕'
con = sqlite3.connect('file:' + LED.replace('\\', '/') + '?mode=ro', uri=True)
cur = con.cursor()
T = 'local_runtime_background_tasks'

cur.execute("SELECT task_id, kind, status, created_at_ms, ended_at_ms, owner_session_id, record_json FROM %s WHERE created_at_ms >= ? ORDER BY created_at_ms" % T, (W26_START,))
rows = cur.fetchall()
print('\n== LEDGER ROWS SINCE 20:52 (2026-10-29) ==', len(rows))
from collections import Counter
print('  kind dist', Counter(r[1] for r in rows))
print('  status dist', Counter(r[2] for r in rows))

print('\n== SUBAGENT ROWS (full) ==')
for r in rows:
    if r[1] != 'subagent':
        continue
    rj = json.loads(r[6]) if r[6] else {}
    md = rj.get('metadata') or {}
    print('  task_id=%s' % r[0])
    print('     owner=%s' % r[5])
    print('     status=%s  created=%s  ended=%s' % (r[2], ts(r[3]), ts(r[4]) if r[4] else 'NONE'))
    print('     desc=%r' % (rj.get('description') or '')[:150])
    print('     agentName=%s execMode=%s childSessionId=%s' % (md.get('agentName'), md.get('executionMode'), md.get('childSessionId')))
    print('     final_result_present=%s' % (bool(rj.get('finalResult'))))

print('\n== BASH AGG (owner split) ==')
own = Counter(r[5] for r in rows if r[1] == 'bash')
print('  bash by owner:', dict(own))
print('  total rows', len(rows))
# 正控：全表 kind 计数
for k in ('subagent', 'bash'):
    cur.execute("SELECT COUNT(*) FROM %s WHERE kind=?" % T, (k,))
    print('  FULL kind=%s -> %d' % (k, cur.fetchone()[0]))

print('\n== MY ROD record_json keys ==')
cur.execute("SELECT record_json FROM %s WHERE task_id=?" % T, ('bg_eed597a7-aa1a-45b1-831c-8f5a31fa582c',))
rj = json.loads(cur.fetchone()[0])
print('  keys', sorted(rj.keys()))
md = rj.get('metadata') or {}
print('  metadata keys', sorted(md.keys()))
for k in ('agentName', 'executionMode', 'childSessionId', 'description', 'requestRef', 'agentConfigDir'):
    print('   ', k, '=', str(md.get(k))[:120])
print('  desc=', str(rj.get('description'))[:300])
con.close()

print('\n== SESSIONS TREE: dirs with messages.jsonl under 2026/10/29 and 10/30 ==')
base = r'〔本地路径已脱敏〕'
for day in ('29', '30'):
    d = os.path.join(base, '10', day)
    if not os.path.isdir(d):
        print('  10/%s : MISSING' % day)
        continue
    for name in sorted(os.listdir(d)):
        p = os.path.join(d, name)
        mp = os.path.join(p, 'messages.jsonl')
        if os.path.isfile(mp):
            print('  10/%s %s  msgs=%d B  mtime=%s' % (day, name, os.path.getsize(mp), ts(os.path.getmtime(mp) * 1000)))

print('\n== BASE64 SUFFIX MATCH for my session id ==')
def b64(s):
    return base64.b64encode(s.encode('utf-8')).decode('ascii').rstrip('=')
MY = 'mvs_8574f789e4f4421dac486ffaf096b87e'
print('  my b64 tail', b64(MY))
hit = 0
for mp2 in glob.glob(os.path.join(base, '**', 'messages.jsonl'), recursive=True):
    nm = os.path.basename(os.path.dirname(mp2))
    if b64(MY) in nm:
        print('  HIT', nm)
        hit += 1
print('  hits', hit)

print('\n== DELEGATE LETTER FILES (name match) ==')
roots = [r'〔本地路径已脱敏〕', r'〔归档区〕', r'〔本地路径已脱敏〕']
for rt in roots:
    if not os.path.isdir(rt):
        print('  ROOT MISSING', rt)
        continue
    n = 0
    for dp, dn, fn in os.walk(rt):
        dn[:] = [x for x in dn if x not in ('.git', 'node_modules', '__pycache__', '.tmp')]
        for f in fn:
            if ('\u59d4\u6258\u51fd' in f) or ('\u4e0a\u4f20' in f) or ('letter' in f.lower()):
                p = os.path.join(dp, f)
                try:
                    sz = os.path.getsize(p)
                    mt = ts(os.path.getmtime(p) * 1000)
                    hh = hashlib.sha256(open(p, 'rb').read()).hexdigest()[:12]
                except Exception as e:
                    sz, mt, hh = -1, str(e), 'ERR'
                print('  %s  %d B  mtime=%s  %s' % (hh, sz, mt, p))
                n += 1
    print('  root %s -> %d hits' % (rt, n))
