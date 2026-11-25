# -*- coding: utf-8 -*-
"""§26 探针八：落件路径直证／§26 号阴断／独立第二读分布／计数异常更正"""
import os, json, re, hashlib, datetime

TZ = datetime.timezone(datetime.timedelta(hours=8))
def ts(ms):
    return datetime.datetime.fromtimestamp(ms / 1000, TZ).strftime('%Y-%m-%d %H:%M:%S')

T = r'〔本地路径已脱敏〕'
b = open(T, 'rb').read()
txt = b.decode('utf-8', 'replace')
print('== TARGET ==')
print('  bytes', len(b), 'sha12', hashlib.sha256(b).hexdigest()[:12],
      'LF', b.count(b'\n'), 'split_lines', len(txt.split('\n')), 'last 0x%02x' % b[-1])

# 1) 不互抄 计数异常更正（探针五曾报 0）
s = '\u4e0d\u4e92\u62c4'
print('\n== COUNT RECHECK ==')
print('  not-mutual-copy count =', txt.count(s), ' (probe5 had reported 0)')
print('  first 3 occurrences:')
n = 0
for i, l in enumerate(txt.split('\n'), 1):
    if s in l:
        n += 1
        if n <= 3:
            print('    L%d' % i)

# 2) §26 号可用性（阴断）：本册全文中 '§26' 之命中
print('\n== NEGATIVE PROBE for node number ==')
for tok in ('\u00a726', '\u00a7 26', '\u00a726-'):
    print('  %-8r count=%d' % (tok, txt.count(tok)))
for i, l in enumerate(txt.split('\n'), 1):
    if '\u00a726' in l:
        print('    L%d %s' % (i, l.strip()[:130]))

# 3) 独立第二读 之逐节分布
print('\n== INDEPENDENT SECOND-READ (独立第二读) per section ==')
heads = []
for i, l in enumerate(txt.split('\n'), 1):
    m = re.match(r'^(#{2,3})\s+\u00a7(\d+)(.*)$', l)
    if m:
        heads.append((i, int(m.group(2)), m.group(1), m.group(3).strip()))
for k, (ln, num, hs, rest) in enumerate(heads):
    end = heads[k + 1][0] - 1 if k + 1 < len(heads) else len(txt.split('\n'))
    body = '\n'.join(txt.split('\n')[ln - 1:end])
    has2 = body.count('\u72ec\u7acb\u7b2c\u4e8c\u8bfb')
    print('  %s L%-5d %-4s 独立第二读=%-3d %s' % (hs, ln, num, has2, rest[:50]))

# 4) 落件直证：完整路径
print('\n== WRITE-CALL FULL PATHS (both session dirs) ==')
SESS = r'〔本地路径已脱敏〕'
for d in sorted(os.listdir(SESS)):
    mp = os.path.join(SESS, d, 'messages.jsonl')
    if not os.path.isfile(mp):
        continue
    print('  --- %s ---' % d[:14])
    with open(mp, 'rb') as f:
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
            for x in c:
                if not isinstance(x, dict):
                    continue
                if x.get('type') == 'toolCall' and x.get('name') in ('write', 'edit'):
                    arg = x.get('arguments') or {}
                    p = arg.get('path') or arg.get('filePath') or arg.get('file_path')
                    print('    L%-4d %s %-5s %s' % (i, ts(stamp) if stamp else '??', x.get('name'), p))
                if x.get('type') == 'text':
                    t = x.get('text') or ''
                    for m in re.finditer(r'Successfully wrote (\d+) bytes to ([^\s"\\]+)', t):
                        print('    L%-4d %s ECHO wrote %s -> %s' % (i, ts(stamp) if stamp else '??', m.group(1), m.group(2)))
