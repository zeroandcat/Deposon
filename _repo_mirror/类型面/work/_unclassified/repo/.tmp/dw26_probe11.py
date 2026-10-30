# -*- coding: utf-8 -*-
"""§26 探针十一：会话树现况／README 归盘之谜／U+6284 vs U+62C4 定论"""
import os, json, re, hashlib, datetime, glob

TZ = datetime.timezone(datetime.timedelta(hours=8))
def ts(ms):
    return datetime.datetime.fromtimestamp(ms / 1000, TZ).strftime('%Y-%m-%d %H:%M:%S')

print('== A. SESSIONS TREE STATE ==')
SESS = r'〔本地路径已脱敏〕'
alld = [d for d in glob.glob(os.path.join(SESS, '**'), recursive=True) if os.path.isdir(d)]
withmsg = [d for d in alld if os.path.isfile(os.path.join(d, 'messages.jsonl'))]
print('  total dirs under sessions/ =', len(alld))
print('  dirs WITH messages.jsonl  =', len(withmsg))
print('  observed at', ts(datetime.datetime.now().timestamp() * 1000))
per = {}
for d in withmsg:
    parts = os.path.relpath(d, SESS).split(os.sep)
    per[parts[0]] = per.get(parts[0], 0) + 1
print('  by year-month:', dict(sorted(per.items())))

print('\n== B. README_external / Move-Item / Rename in session 14-44-11-839 ==')
mp = r'〔本地路径已脱敏〕'
raw = open(mp, 'rb').read()
print('  messages.jsonl bytes=%d sha12=%s mtime=%s' % (len(raw), hashlib.sha256(raw).hexdigest()[:12], ts(os.path.getmtime(mp) * 1000)))
for pat in (rb'README_external', rb'Move-Item', rb'Rename-Item', rb'README\.md'):
    print('  %-18s hits=%d' % (pat.decode(), raw.count(pat)))
# 逐行：找含 README_external 且含命令词者
for i, line in enumerate(raw.split(b'\n'), 1):
    if b'README_external' in line:
        s = line.decode('utf-8', 'replace')
        for m in re.finditer(r'.{0,150}README_external.{0,200}', s):
            print('   L%d %s' % (i, m.group(0).replace('\n', ' | ')[:340]))
        break
print('  -- Move-Item occurrences (context) --')
cnt = 0
for i, line in enumerate(raw.split(b'\n'), 1):
    if b'Move-Item' in line or b'Rename-Item' in line:
        s = line.decode('utf-8', 'replace')
        for m in re.finditer(r'.{0,120}(Move-Item|Rename-Item).{0,220}', s):
            print('   L%d %s' % (i, m.group(0).replace('\n', ' | ')[:330]))
            cnt += 1
            if cnt > 8:
                break
    if cnt > 8:
        break

print('\n== C. U+6284 vs U+62C4 ==')
T = r'〔本地路径已脱敏〕'
b = open(T, 'rb').read()
txt = b.decode('utf-8', 'replace')
a = '\u4e0d\u4e92\u6284'
c = '\u4e0d\u4e92\u62c4'
print('  U+6284 form count =', txt.count(a), '  U+62C4 form count =', txt.count(c))
print('  bytes of U+6284 form =', a.encode('utf-8').hex())
# 找首处并打印上下文
i = txt.find(a)
print('  first at char %d; context: %r' % (i, txt[i - 30:i + 40]))
print('  lines containing U+6284 form:',
      [n for n, l in enumerate(txt.split('\n'), 1) if a in l])
print('\n== D. target live state ==')
print('  bytes=%d sha12=%s mtime=%s LF=%d' % (len(b), hashlib.sha256(b).hexdigest()[:12],
      ts(os.path.getmtime(T) * 1000), b.count(b'\n')))
