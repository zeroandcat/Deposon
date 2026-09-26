# -*- coding: utf-8 -*-
import sys, os
F = 'D:\\私人资料\\deposon-repo\\docs\\V3X\\TRAE_V3_ASSET_ERRATUM_2026_09_23.md'
size = os.path.getsize(F)
with open(F, 'rb') as fh:
    raw = fh.read()

# output last ~500 bytes as escaped (avoid console GBK)
tail = raw[-700:]
sys.stdout.buffer.write(b"--- tail bytes (escaped hex bytes for last 700) ---\n")
sys.stdout.buffer.write(tail.hex().encode('ascii'))
sys.stdout.buffer.write(b"\n--- end ---\n")
sys.stdout.buffer.write(("total bytes=" + str(size)).encode())
sys.stdout.buffer.write(b"\n")
# also write a decoded tail to a temp file for viewing
out = 'D:\\私人资料\\deposon-repo\\.tmp\\_v16_tail_dump.txt'
with open(out, 'wb') as fout:
    fout.write(raw)
print('wrote', out)
