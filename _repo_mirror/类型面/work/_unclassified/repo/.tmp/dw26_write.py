# -*- coding: utf-8 -*-
"""§26 落盘器：截回 §26 边界 → 写体稿 → 复跑前缀核与字节五项"""
import os, hashlib, sys

T = r'〔本地路径已脱敏〕'
BODY = r'〔本地路径已脱敏〕'
MARK = '## §26 · 子路之实录（续 §25）· 2026-10-30（独立更新节 · PURE-APPEND）'
EXP_SIZE = 758741
EXP_SHA = 'e9a2ce33c7f5'

def sha12(b):
    return hashlib.sha256(b).hexdigest()[:12]

cur = open(T, 'rb').read()
print('BEFORE  bytes=%d sha12=%s' % (len(cur), sha12(cur)))

raw = open(BODY, 'rb').read()
print('BODY    bytes=%d bom=%s cr=%d fffd=%d last=0x%02x' % (
    len(raw), raw[:3] == b'\xef\xbb\xbf', raw.count(b'\r'),
    raw.decode('utf-8', 'replace').count('\ufffd'), raw[-1]))
assert raw[:3] != b'\xef\xbb\xbf' and raw.count(b'\r') == 0 and raw[-1] == 0x0a
assert raw.decode('utf-8', 'replace').count('\ufffd') == 0

# 截回 §26 边界：找本棒骨架起点（骨架已在盘，故全件 > EXP_SIZE；前缀仍须逐位相符）
idx = cur.find(MARK.encode('utf-8'))
assert idx != -1, 'ABORT_MARK_NOT_FOUND'
print('  §26 mark at byte offset %d' % idx)
prefix = cur[:idx]
print('  prefix to be kept: bytes=%d sha12=%s' % (len(prefix), sha12(prefix)))
assert len(prefix) == EXP_SIZE and sha12(prefix) == EXP_SHA, 'ABORT_PREFIX_MISMATCH'
print('  prefix check OK (758741/%s)' % EXP_SHA)

out = prefix + raw
with open(T, 'wb') as f:
    f.write(out)

after = open(T, 'rb').read()
same = after[:EXP_SIZE] == cur[:EXP_SIZE]
print('AFTER   bytes=%d sha12=%s PREFIX_IDENTICAL=%s CR=%d BOM=%s FFFD=%d LAST=0x%02x LF=%d' % (
    len(after), sha12(after), same, after.count(b'\r'),
    after[:3] == b'\xef\xbb\xbf',
    after.decode('utf-8', 'replace').count('\ufffd'), after[-1], after.count(b'\n')))
assert same, 'ABORT_PREFIX_CHANGED'
# 前缀四级正控
for n, exp in ((758741, 'e9a2ce33c7f5'), (727052, '6062233c9ec5'),
               (694612, 'ede5675a6a79'), (657076, '1661d09fc948')):
    got = sha12(after[:n])
    print('  prefix %d B -> %s expect %s  %s' % (n, got, exp, 'OK' if got == exp else 'MISMATCH'))
    assert got == exp
print('DONE')
