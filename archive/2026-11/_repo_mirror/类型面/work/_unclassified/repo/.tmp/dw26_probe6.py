# -*- coding: utf-8 -*-
"""§26 探针六：新窗实测（会话树／base64／A级落件直证／台账正确窗／GBK 还原）"""
import os, json, base64, hashlib, sqlite3, datetime, glob, re

TZ = datetime.timezone(datetime.timedelta(hours=8))
def ts(ms):
    return datetime.datetime.fromtimestamp(ms / 1000, TZ).strftime('%Y-%m-%d %H:%M:%S')

SESS = r'〔本地路径已脱敏〕'
MAIN = os.path.join(SESS, '2026', '09', '01',
                    '02-38-47-809-session_bXZzX2JiZWI4MDRiMWE2YTQxMTA5YmU3NDA2MzZlZWQxNzA5')

# 1) 全 sessions 树含 messages.jsonl 之目录数
allmp = glob.glob(os.path.join(SESS, '**', 'messages.jsonl'), recursive=True)
print('== SESSIONS TREE ==')
print('  dirs with messages.jsonl (all tree):', len(allmp))
for d in ('29', '30'):
    p = os.path.join(SESS, '2026', '10', d)
    print('  10/%s exists=%s' % (d, os.path.isdir(p)))
    if os.path.isdir(p):
        for n in sorted(os.listdir(p)):
            fp = os.path.join(p, n)
            if os.path.isdir(fp):
                mp = os.path.join(fp, 'messages.jsonl')
                print('     %-46s msgs=%s' % (n[:46], os.path.getsize(mp) if os.path.isfile(mp) else 'NONE'))

# 2) 六棒 + 本棒 base64 后缀命中
RODS = [
    ('bg_06f1b9dc', 'mvs_cb29b473c89f46178787fb5220395d5b'),
    ('bg_8b9bdf59', 'mvs_a39520194bf44a5eb79c5be3e3d37896'),
    ('bg_156b760e', 'mvs_4c563591758a4831aee21c5b050b9b94'),
    ('bg_d53d8381', 'mvs_4c563591758a4831aee21c5b050b9b94'),
    ('bg_7c16da20', 'mvs_4c563591758a4831aee21c5b050b9b94'),
    ('bg_5b4fcb87', 'mvs_4c563591758a4831aee21c5b050b9b94'),
    ('bg_eed597a7', 'mvs_8574f789e4f4421dac486ffaf096b87e'),
]
def b64(s):
    return base64.b64encode(s.encode('utf-8')).decode('ascii').rstrip('=')
names = []
for mp in allmp:
    names.append(os.path.basename(os.path.dirname(mp)))
print('\n== BASE64 SUFFIX MATCH ==')
for rod, sid in RODS:
    t = b64(sid)
    hit = [n for n in names if t in n]
    print('  %-12s %-6s hits=%d %s' % (rod, sid[-6:], len(hit), hit[:1]))
neg = ''.join(['mvs_', 'nonexistent', '_probe_zz'])
print('  NEG built      hits=%d' % len([n for n in names if b64(neg) in n]))

# 3) A 级落件直证：在盘之棒会话目录内取写调用回文
print('\n== A-LEVEL WRITE EVIDENCE (write-call echo) ==')
def scan_writes(path, label):
    if not os.path.isfile(path):
        print('  %s : messages.jsonl NOT ON DISK' % label)
        return
    hits = []
    with open(path, 'rb') as f:
        for i, line in enumerate(f, 1):
            s = line.decode('utf-8', 'replace')
            for pat in (r'Successfully wrote (\d+) bytes to ([^"\\\\]+)',
                        r'"path"\s*:\s*"([^"]+\.(?:md|jsonl|py|json))"',
                        r"Wrote (\d+) bytes to ([^'\"\\\\]+)"):
                for m in re.finditer(pat, s):
                    hits.append((i, m.group(0)[:160]))
    print('  %s : %d hits (lines up to %d)' % (label, len(hits), len(hits) and hits[-1][0]))
    for i, h in hits[:60]:
        print('     L%d %s' % (i, h))
    return hits

for d in sorted(os.listdir(os.path.join(SESS, '2026', '10', '29'))):
    p = os.path.join(SESS, '2026', '10', '29', d, 'messages.jsonl')
    if os.path.isfile(p):
        scan_writes(p, d[:14])

# 4) 台账正确窗：bg_06f1b9dc 讫 (20:59:57) → now
LED = r'〔本地路径已脱敏〕'
con = sqlite3.connect('file:' + LED.replace('\\', '/') + '?mode=ro', uri=True)
cur = con.cursor()
T = 'local_runtime_background_tasks'
W0 = 1793290000000  # placeholder, replaced below by computed from known ms
# 用 bg_06f1b9dc 的 ended_at_ms 作为窗起点
cur.execute("SELECT ended_at_ms FROM %s WHERE task_id LIKE 'bg_06f1b9dc%%'" % T)
end25 = cur.fetchone()[0]
print('\n== LEDGER WINDOW since bg_06f1b9dc ended (%s) ==' % ts(end25))
cur.execute("SELECT kind, status, owner_session_id FROM %s WHERE created_at_ms >= ?" % T, (end25,))
rows = cur.fetchall()
from collections import Counter
print('  rows', len(rows), 'kind', dict(Counter(r[0] for r in rows)), 'status', dict(Counter(r[1] for r in rows)))
print('  bash by owner', dict(Counter(r[2] for r in rows if r[0] == 'bash')))
cur.execute("SELECT COUNT(*) FROM %s WHERE created_at_ms >= ?" % T, (end25,))
print('  total rows since', cur.fetchone()[0])
# 正控：全表
for k in ('subagent', 'bash'):
    cur.execute("SELECT COUNT(*) FROM %s WHERE kind=?" % T, (k,))
    print('  FULL kind=%s %d' % (k, cur.fetchone()[0]))
# 阴断
cur.execute("SELECT COUNT(*) FROM %s WHERE task_id LIKE 'bg_deadbee0%%'" % T)
print('  NEG bg_deadbee0 rows', cur.fetchone()[0])
# 各 subagent 行在本窗内者
cur.execute("SELECT task_id,status,created_at_ms,ended_at_ms FROM %s WHERE kind='subagent' AND created_at_ms >= ? ORDER BY created_at_ms" % T, (end25,))
print('  subagent rows in window:')
for r in cur.fetchall():
    print('   ', r[0], r[1], ts(r[2]), ts(r[3]) if r[3] else 'NONE')
con.close()

# 5) L80 之 plugin-hook-context 之 GBK 还原（原始字节）
print('\n== GBK RESTORE of L80 hook context (raw bytes) ==')
raw = open(os.path.join(MAIN, 'messages.jsonl'), 'rb').read().split(b'\n')
l80 = raw[79]
for m in re.finditer(rb'plugin-hook-context\\?"\s*:\s*\\?"(.{0,400}?)\\?"\s*,', l80, re.S):
    frag = m.group(1)
    for enc in ('gbk', 'gb18030'):
        try:
            print('  %s -> %r' % (enc, frag.decode(enc)))
            break
        except Exception as e:
            print('  %s fail %s' % (enc, e))
