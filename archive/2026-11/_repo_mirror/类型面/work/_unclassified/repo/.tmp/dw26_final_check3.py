# -*- coding: utf-8 -*-
"""§26 终核三：起讫字面之真形（探针之误 vs 册面之缺）"""
import re, hashlib

T = r'〔本地路径已脱敏〕'
b = open(T, 'rb').read()
txt = b.decode('utf-8', 'replace')
L = txt.split('\n')
s26 = '\n'.join(L[4161:])

print('== 起讫 字形诊断 ==')
for name, s in (('A 异体(讠+乞?)', '\u8d77\u8bb0'), ('B 讠+己', '\u8d77\u8bb0'),
                ('C 起止', '\u8d77\u6b62'), ('D 起讫(常用)', '\u8d77\u8bb0')):
    print('  %-16s count=%d' % (name, txt.count(s)))

# 逐字枚举：§26 表头行 L4214 之中，所有两字组合
hdr = L[4213]
print('\n  header L4214 =', hdr[:120])
# 找「起」之后一字符
for m in re.finditer('\u8d77', hdr):
    print('   起 at %d -> next char %r U+%04X' % (m.start(), hdr[m.start() + 1], ord(hdr[m.start() + 1])))

# 全册：凡「起」后接某字之分布
from collections import Counter
c = Counter()
for l in L:
    for m in re.finditer('\u8d77', l):
        if m.start() + 1 < len(l):
            c[l[m.start() + 1]] += 1
print('\n  全册「起」后接字分布:', dict(c))

# 定位本册 §25 之同口径写法（对照）
i = txt.find('\u8d77')
print('\n  §26 内「起」总数:', s26.count('\u8d77'))
print('  §26 内含「起」的行首 5 例:')
n = 0
for i, l in enumerate(L[4161:], 4162):
    if '\u8d77' in l:
        print('    L%-5d %s' % (i, l[:150]))
        n += 1
        if n >= 5:
            break
