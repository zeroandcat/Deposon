import sys, hashlib
p = r'_repo_mirror/work/note/_root_session_history_memo_2026_10_14.md'
data = open(p, 'rb').read()
# read last ~600 chars (utf-8) by decoding tail bytes
tail = data[-1500:]
txt = tail.decode('utf-8', errors='replace')
import sys
sys.stdout.buffer.write(b'===TAIL_TEXT===\n')
sys.stdout.buffer.write(tail)
sys.stdout.buffer.write(b'\n===END===\n')
print('---')
print('total_bytes:', len(data))
print('SHA12:', hashlib.sha256(data).hexdigest()[:12].upper())
print('SHA256:', hashlib.sha256(data).hexdigest())
print('CRLF:', data.count(b'\r\n'))
print('LF_total:', data.count(b'\n'))
print('CR_count:', data.count(b'\r'))
print('BOM_in_head:', data[:3] == b'\xef\xbb\xbf')
