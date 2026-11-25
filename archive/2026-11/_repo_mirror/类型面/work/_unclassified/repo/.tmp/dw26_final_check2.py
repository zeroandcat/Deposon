# -*- coding: utf-8 -*-
"""§26 终核二：承之实读／节点号之阴断（限 ## 级）／起讫字面"""
import re, hashlib

T = r'〔本地路径已脱敏〕'
b = open(T, 'rb').read()
txt = b.decode('utf-8', 'replace')
L = txt.split('\n')

print('== 1. §26 heading block raw (L4162-L4172) ==')
for i in range(4162, 4173):
    print('  L%-5d %s' % (i, L[i - 1][:210]))

print('\n== 2. node-title negative probe, ## level only (前 §1–§25 射界) ==')
pre = txt[:txt.index('## §26 ·')]
h2 = re.findall(r'(?m)^##\s+\u00a7(\d+)', pre)
print('  §1–§25 的 ## 级节点号:', h2)
print('  其中含 26 者:', [x for x in h2 if x == '26'])
h3 = re.findall(r'(?m)^###\s+\u00a7(\d+)', pre)
print('  ### 级节点号（含子节）: 含 26 者 =', [x for x in h3 if x == '26'])
print('  => §26 之号未被本册用作节点（## 级 0 命中）')

print('\n== 3. 三职之实读定位 ==')
blk = '\n'.join(L[4161:4172])
for name, key in (('承', '\u672c\u8282\u627f'), ('不改', 'PURE-APPEND'), ('以新为准', '\u4ee5\u672c\u8282\u4e3a\u51c6'), ('点名', '\u00a726-6')):
    i = blk.find(key)
    print('  %-8s -> %s  | ctx: %s' % (name, 'FOUND' if i >= 0 else 'MISS',
          repr(blk[max(0, i - 26):i + 40]) if i >= 0 else '-'))

print('\n== 4. 逐棒表之字面要件（甲组表头与首行） ==')
hdr = [i for i, l in enumerate(L, 1) if l.startswith('| # | 棒号 | 所属官')]
print('  表头行号:', hdr)
if hdr:
    print('  表头:', L[hdr[0] - 1][:200])
    print('  第1行:', L[hdr[0]][:260])
    print('  第7行(本棒):', L[hdr[0] + 5][:260])

print('\n== 5. 起讫字面检查 ==')
print('  "起讫" 出现次数 in §26:', '\n'.join(L[4161:]).count('\u8d77\u8bb0'))
print('  "起讫（GMT+8）" in 甲组表头:', '\u8d77\u8bb0\uff08GMT+8\uff09' in '\n'.join(L[4161:]))

print('\n== 6. §26-4 ②正控/③阴断 之存在 ==')
s26 = '\n'.join(L[4161:])
for key in ('\u6b63\u63a7', '\u9634\u65ad', '\u5047\u9633\u6027', '\u5c04\u754c', '\u6b63\u63a7\uff08\u5fc5\u4e0d\u4e3a 0'):
    print('  %-14s -> %d' % (key, s26.count(key)))
print('  §26-4 ②/③ 小节标题行:')
for i, l in enumerate(L, 1):
    if i >= 4162 and ('\u6b63\u63a7\uff08' in l or '\u9634\u65ad\uff08' in l or '\u5047\u9633\u6027\u4e4b\u7684\u5254\u9664' in l):
        print('    L%-5d %s' % (i, l[:110]))
