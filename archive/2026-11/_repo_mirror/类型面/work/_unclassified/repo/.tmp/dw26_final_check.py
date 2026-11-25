# -*- coding: utf-8 -*-
"""§26 终核：三职／五要件／节次／阴断／自陈 之逐项实测"""
import re, hashlib, datetime

T = r'〔本地路径已脱敏〕'
b = open(T, 'rb').read()
txt = b.decode('utf-8', 'replace')
L = txt.split('\n')
print('== FINAL ==', len(b), 'B', hashlib.sha256(b).hexdigest()[:12], 'LF', b.count(b'\n'),
      'last 0x%02x' % b[-1], 'cr', b.count(b'\r'))

# §26 起点
idx = [i for i, l in enumerate(L, 1) if l.startswith('## §26 ·')]
print('§26 heading line =', idx)
s26 = '\n'.join(L[idx[0] - 1:])
print('§26 lines =', len(s26.split('\n')))

print('\n== 1. THREE DUTIES in §26 heading block ==')
head = '\n'.join(L[idx[0] - 1: idx[0] + 12])
for name, pat in (('承', r'\u672f\u8282\u627f'), ('不改', r'PURE-APPEND'), ('以新为准', r'\u4ee5\u672c\u8282\u4e3a\u51c6')):
    print('  %-8s in heading block: %s' % (name, bool(re.search(pat, head))))
print('  以新为准 + 点名 (指向表):', '\u89c1 \u00a726-6' in head or '\u00a726-6' in head)

print('\n== 2. §26 sub-sections ==')
for i, l in enumerate(L, 1):
    if i >= idx[0] and re.match(r'^#{3,4}\s+\u00a726', l):
        print('  L%-5d %s' % (i, l.strip()[:96]))

print('\n== 3. FIVE REQUIREMENTS present in §26 ==')
checks = {
    'R1 逐棒一行': ['\u68d2\u53f7', '\u6240\u5c5e\u5b98', '\u6240\u4e8b', '\u8d77\u8bb0', '\u843d\u4ef6', '\u5224\uff08'],
    'R2 来源可回溯': ['\u6765\u6e90'],
    'R3 记录不可得·其因': ['\u4e0d\u53ef\u5f97', '\u5176\u56e0'],
    'R4 自陈一句': ['\u4e0d\u4e92\u6284'],
    'R5 一手取径': ['\u4e00\u624b', 'messages.jsonl', 'snapshots'],
}
for k, words in checks.items():
    hit = {w: s26.count(w) for w in words}
    print('  %-16s %s' % (k, hit))

print('\n== 4. NEGATIVE PROBES re-run on final file ==')
print('  §26 as node title (^#{2,4} §26\\b):', len(re.findall(r'(?m)^#{2,4}\s+\u00a726\b', txt)))
print('  literal "§26" total hits:', txt.count('\u00a726'))
print('  §27 node titles:', len(re.findall(r'(?m)^#{2,4}\s+\u00a727\b', txt)))

print('\n== 5. 不互抄 self-statement count (U+6284) ==')
print('  U+6284 form:', txt.count('\u4e0d\u4e92\u6284'), ' U+62C4 form:', txt.count('\u4e0d\u4e92\u62c4'))

print('\n== 6. §26-5 three-duty matrix rows sanity ==')
for key in ('10 \uff0f 26', '21 \uff0f 26', '5 \uff0f 26', '4 \uff0f 26', '22 \uff0f 26'):
    print('  %-12s in §26: %s' % (key, key in s26))

print('\n== 7. last 12 lines of file ==')
for i, l in enumerate(L[-12:], len(L) - 11):
    print('  L%-5d %s' % (i, l[:150]))
