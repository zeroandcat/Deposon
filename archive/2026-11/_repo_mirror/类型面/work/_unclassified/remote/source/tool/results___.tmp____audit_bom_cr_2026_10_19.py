import os, sys, hashlib

p = r'_repo_mirror/work/note/_root_session_history_memo_2026_10_14.md'
data = open(p, 'rb').read()
bom_seq = data[:3]
bom_seq2 = data[3:6]
print('first_12_bytes_hex:', data[:12].hex())
print('first_12_bytes_repr:', repr(data[:12]))
print('BOM_count_at_head:', data[:3].hex(), '×', data[:6].count(bom_seq * 1))
print('CR_count:', data.count(b'\r'))
print('LF_count:', data.count(b'\n'))
print('CRLF_count:', data.count(b'\r\n'))
print('total_bytes:', len(data))
print('LF_minus_CRLF:', data.count(b'\n') - data.count(b'\r\n'))
print('tail_20_bytes_hex:', data[-20:].hex())
print('SHA256:', hashlib.sha256(data).hexdigest())
print('SHA12 :', hashlib.sha256(data).hexdigest()[:12].upper())
print('UTF8_BOM_in_middle_after_pos6:', b'\xef\xbb\xbf' in data[6:])
print('U+FFFD_count:', data.count(b'\xef\xbf\xbd'.decode('utf-8').encode('utf-8')))
