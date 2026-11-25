import hashlib, io, os, sys

# 用法：python -P _append_generic.py <body> <target> <exp_size> <exp_sha12> [tag]
if len(sys.argv) < 5:
    print('USAGE: _append_generic.py BODY TARGET EXP_SIZE EXP_SHA12 [TAG]'); sys.exit(2)

BODY = sys.argv[1]
TARGET = sys.argv[2]
EXP_SZ = int(sys.argv[3])
EXP_SHA = sys.argv[4]
TAG = sys.argv[5] if len(sys.argv) > 5 else 'TARGET'

def sha12(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()[:12]

if not os.path.exists(BODY):
    print('ABORT BODY_MISSING'); sys.exit(1)
raw = open(BODY, 'rb').read()
bom = raw[:3] == b'\xef\xbb\xbf'
cr = raw.count(b'\r')
last = raw[-1]
fffd = raw.decode('utf-8', errors='replace').count('\ufffd')
print('BODY bytes=%d bom=%s cr=%d last=0x%02x fffd=%d' % (len(raw), bom, cr, last, fffd))
if bom or cr or last != 0x0a or fffd:
    print('ABORT BODY_BAD'); sys.exit(1)

if not os.path.exists(TARGET):
    print('ABORT TARGET_MISSING'); sys.exit(1)
cur_sz = os.path.getsize(TARGET)
cur_sha = sha12(TARGET)
ok = (cur_sz == EXP_SZ and cur_sha == EXP_SHA)
print('%s prefix bytes=%d sha12=%s expect=%d/%s %s'
      % (TAG, cur_sz, cur_sha, EXP_SZ, EXP_SHA, 'OK' if ok else 'MISMATCH'))
if not ok:
    print('ABORT PREFIX_MISMATCH'); sys.exit(1)

with open(TARGET, 'rb') as f:
    base = f.read()
with io.open(TARGET, 'ab') as f:
    f.write(raw)
with open(TARGET, 'rb') as f:
    cur = f.read()
same = cur[:len(base)] == base
tail = cur[len(base):]
print('%s AFTER bytes=%d sha12=%s PREFIX_IDENTICAL=%s APPENDED=%d CR=%d BOM=%s FFFD=%d LF_TAIL=%d LAST=0x%02x'
      % (TAG, len(cur), sha12(TARGET), same, len(tail),
         cur.count(b'\r'), cur[:3] == b'\xef\xbb\xbf',
         cur.decode('utf-8', errors='replace').count('\ufffd'),
         tail.count(b'\n'), cur[-1]))
if not same:
    print('ABORT PREFIX_CHANGED'); sys.exit(1)
print('DONE')
