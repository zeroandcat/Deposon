# -*- coding: utf-8 -*-
"""§26 探针五：体例之正自算指纹 + 新窗落件候选面 + 会话目录现况"""
import os, hashlib, datetime, glob, json

TZ = datetime.timezone(datetime.timedelta(hours=8))
def ts(ms):
    return datetime.datetime.fromtimestamp(ms / 1000, TZ).strftime('%Y-%m-%d %H:%M:%S')

C = r'〔本地路径已脱敏〕'
b = open(C, 'rb').read()
print('== CONSTITUTION (self-measured) ==')
print('  bytes', len(b), 'sha12', hashlib.sha256(b).hexdigest()[:12], 'lines', b.count(b'\n'),
      'mtime', ts(os.path.getmtime(C) * 1000), 'last 0x%02x' % b[-1], 'cr', b.count(b'\r'))

T = r'〔本地路径已脱敏〕'
tb = open(T, 'rb').read()
print('\n== TARGET (self-measured, pre-write) ==')
print('  bytes', len(tb), 'sha12', hashlib.sha256(tb).hexdigest()[:12], 'lines', tb.count(b'\n'))

# 新窗落件候选面：results/ 全树 mtime in [20:59:57, now]
W0 = 1793252397000  # 2026-10-29 20:59:57 (bg_06f1b9dc 讫)
NOW = 1793293500000
print('\n== results/ files with mtime in [20:59:57 10-29, ~01:05 10-30] ==')
cands = []
for dp, dn, fn in os.walk(r'〔本地路径已脱敏〕'):
    dn[:] = [x for x in dn if x not in ('.git', '__pycache__', 'node_modules')]
    for f in fn:
        p = os.path.join(dp, f)
        try:
            mt = os.path.getmtime(p) * 1000
        except Exception:
            continue
        if W0 <= mt <= NOW + 3600000:
            cands.append((mt, p))
cands.sort()
print('  count', len(cands))
for mt, p in cands:
    sz = os.path.getsize(p)
    hh = hashlib.sha256(open(p, 'rb').read()).hexdigest()[:12]
    print('   %s  %8d B  %s  %s' % (ts(mt), sz, hh, p))

print('\n== session dirs under 2026/10/29 and 10/30 (full listing) ==')
for day in ('29', '30'):
    d = os.path.join(r'〔本地路径已脱敏〕', day)
    if not os.path.isdir(d):
        print('  10/%s MISSING' % day)
        continue
    for name in sorted(os.listdir(d)):
        p = os.path.join(d, name)
        if not os.path.isdir(p):
            continue
        items = []
        for f in sorted(os.listdir(p)):
            fp = os.path.join(p, f)
            if os.path.isfile(fp):
                items.append('%s(%dB)' % (f, os.path.getsize(fp)))
            else:
                n = len(os.listdir(fp))
                items.append('%s/ (%d)' % (f, n))
        print('  10/%s %s :: %s' % (day, name[:46], ', '.join(items)))

# §17–§25 五要件 spot-check：自陈 / 不可得 / 来源 / 取径
print('\n== FIVE-REQUIREMENT SPOT CHECK in target (grep-like, self-measured) ==')
txt = tb.decode('utf-8', 'replace')
KEYS = {
    'R4_不互抄': '\u4e0d\u4e92\u62c4',
    'R3_记录不可得': '\u8bb0\u5f55\u4e0d\u53ef\u5f97',
    'R3b_其因': '\u5176\u56e0',
    'R5_一手取径': '\u4e00\u624b',
    'R2_来源列': '\u6765\u6e90',
    'R1_棒号': '\u68d2\u53f7',
}
for k, v in KEYS.items():
    print('  %-16s %d' % (k, txt.count(v)))
