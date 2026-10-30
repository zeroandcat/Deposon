# -*- coding: utf-8 -*-
"""§26 探针九：计数诊断／逐棒调用清单／前缀核链／落件现值"""
import os, json, re, hashlib, datetime

TZ = datetime.timezone(datetime.timedelta(hours=8))
def ts(ms):
    return datetime.datetime.fromtimestamp(ms / 1000, TZ).strftime('%H:%M:%S')

T = r'〔本地路径已脱敏〕'
b = open(T, 'rb').read()
txt = b.decode('utf-8', 'replace')
L = txt.split('\n')

print('== COUNT DIAGNOSIS ==')
target = '\u4e0d\u4e92\u62c4'
print('  str count (utf-8 decoded) =', txt.count(target))
print('  bytes count (utf-8 encoded) =', b.count(target.encode('utf-8')))
for i, l in enumerate(L, 1):
    if target in l:
        j = l.index(target)
        seg = l[j:j + 3]
        print('   L%-5d repr=%r  codepoints=%s  hexbytes=%s' % (i, seg, [hex(ord(c)) for c in seg], seg.encode('utf-8').hex()))
        break
# 逐变体排查
for name, s in (('互 U+4E92', '\u4e0d\u4e92\u62c4'), ('互 U+4E92-EF', '\u4e0d\u4e92\u62c4'),
                ('手写 不互抄', '\u4e0d\u4e92\u62c4')):
    print('   variant %s -> %d' % (name, txt.count(s)))
# 反查：以「不互」二字为锚
idx = [i for i, l in enumerate(L, 1) if '\u4e0d\u4e92' in l]
print('  lines containing 不互 =', len(idx), idx[:6])
if idx:
    l = L[idx[0] - 1]
    j = l.index('\u4e0d\u4e92')
    print('   sample repr:', repr(l[j:j + 6]))

print('\n== PREFIX CHAIN (self-measured) ==')
for n, exp in ((727052, '6062233c9ec5'), (694612, 'ede5675a6a79'), (657076, '1661d09fc948')):
    got = hashlib.sha256(b[:n]).hexdigest()[:12]
    print('  first %d B -> %s  expect %s  %s' % (n, got, exp, 'OK' if got == exp else 'MISMATCH'))
print('  whole %d B -> %s' % (len(b), hashlib.sha256(b).hexdigest()[:12]))

print('\n== SECOND-READ MENTIONS (sections 17-25) ==')
heads = []
for i, l in enumerate(L, 1):
    m = re.match(r'^(#{2,3})\s+\u00a7(\d+)(.*)$', l)
    if m:
        heads.append((i, int(m.group(2)), m.group(3).strip()))
for k, (ln, num, rest) in enumerate(heads):
    if num < 17:
        continue
    end = heads[k + 1][0] - 1 if k + 1 < len(heads) else len(L)
    body = '\n'.join(L[ln - 1:end])
    c1 = body.count('\u72ec\u7acb\u7b2c\u4e8c\u8bfb')
    c2 = body.count('\u7b2c\u4e8c\u8bfb')
    c3 = body.count('\u72ec\u7acb\u5224\u8bfb')
    print('  §%-3d L%-5d 独立第二读=%d 第二读=%d 独立判读=%d  | %s' % (num, ln, c1, c2, c3, rest[:46]))

print('\n== PER-ROD TOOLCALL INVENTORY (new window) ==')
WINDOWS = [
    ('bg_8b9bdf59', 1793289624000, 1793289813000),
    ('bg_156b760e', 1793289851000, 1793290753000),
    ('bg_d53d8381', 1793290842000, 1793291128000),
    ('bg_7c16da20', 1793291637000, 1793293061000),
    ('bg_5b4fcb87', 1793293788000, 1793294063000),
    ('bg_eed597a7', 1793293267878, 9999999999999),
]
calls = {}
mp = r'〔本地路径已脱敏〕'
mp2 = r'〔本地路径已脱敏〕'
for src in (mp, mp2):
    if not os.path.isfile(src):
        continue
    with open(src, 'rb') as f:
        for i, raw in enumerate(f, 1):
            raw = raw.strip()
            if not raw:
                continue
            try:
                rec = json.loads(raw.decode('utf-8', 'replace'))
            except Exception:
                continue
            msg = rec.get('message') or {}
            c = msg.get('content')
            if not isinstance(c, list):
                continue
            stamp = rec.get('timestamp') or msg.get('timestamp')
            if not stamp:
                continue
            for x in c:
                if isinstance(x, dict) and x.get('type') == 'toolCall':
                    arg = x.get('arguments') or {}
                    p = arg.get('path') or arg.get('filePath')
                    calls.setdefault(stamp, []).append((os.path.basename(src)[:6], x.get('name'), p, str(arg.get('command') or '')[:70]))
for rod, t0, t1 in WINDOWS:
    sel = []
    for st in sorted(calls):
        if t0 <= st <= t1:
            for c_ in calls[st]:
                sel.append((ts(st), c_[0], c_[1], c_[2], c_[3]))
    print('  --- %s : %d toolCalls ---' % (rod, len(sel)))
    for s in sel:
        print('      %s %s %-5s %s %s' % s)

print('\n== LANDING FILES ON DISK (self-measured) ==')
for p in [r'〔本地路径已脱敏〕',
          r'〔本地路径已脱敏〕',
          r'〔幽灵引用·未上传:README_external_2026_10_30.md〕',
          r'〔本地路径已脱敏〕']:
    if os.path.isfile(p):
        raw = open(p, 'rb').read()
        print('  %8d B  %s  mtime=%s  %s' % (len(raw), hashlib.sha256(raw).hexdigest()[:12], ts(os.path.getmtime(p) * 1000), p))
    else:
        print('  NOT ON DISK  %s' % p)
