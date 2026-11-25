# -*- coding: utf-8 -*-
"""§26 勘误追加行 之落盘器（append-only·不回改 §26 正文一字）"""
import hashlib

T = r'〔幽灵引用·未上传:_sub_agent_memo_10_24_v4.md〕'
T = r'〔本地路径已脱敏〕'
BODY = r'〔本地路径已脱敏〕'

def sha12(b):
    return hashlib.sha256(b).hexdigest()[:12]

cur = open(T, 'rb').read()
raw = open(BODY, 'rb').read()
print('BEFORE bytes=%d sha12=%s' % (len(cur), sha12(cur)))
print('BODY   bytes=%d bom=%s cr=%d fffd=%d last=0x%02x' % (
    len(raw), raw[:3] == b'\xef\xbb\xbf', raw.count(b'\r'),
    raw.decode('utf-8', 'replace').count('\ufffd'), raw[-1]))
assert raw[:3] != b'\xef\xbb\xbf' and raw.count(b'\r') == 0 and raw[-1] == 0x0a
assert raw.decode('utf-8', 'replace').count('\ufffd') == 0

out = cur + raw
with open(T, 'wb') as f:
    f.write(out)
after = open(T, 'rb').read()
print('AFTER  bytes=%d sha12=%s PREFIX_IDENTICAL=%s CR=%d BOM=%s FFFD=%d LAST=0x%02x' % (
    len(after), sha12(after), after[:len(cur)] == cur, after.count(b'\r'),
    after[:3] == b'\xef\xbb\xbf',
    after.decode('utf-8', 'replace').count('\ufffd'), after[-1]))
assert after[:len(cur)] == cur
for n, exp in ((758741, 'e9a2ce33c7f5'), (727052, '6062233c9ec5'),
               (694612, 'ede5675a6a79'), (657076, '1661d09fc948'), (806881, '402e7474a2c3')):
    got = sha12(after[:n])
    print('  prefix %d B -> %s expect %s  %s' % (n, got, exp, 'OK' if got == exp else 'MISMATCH'))
    assert got == exp
print('DONE')
