# -*- coding: utf-8 -*-
import hashlib, os
F = 'D:\\私人资料\\deposon-repo\\docs\\V3X\\TRAE_V3_ASSET_ERRATUM_2026_09_23.md'
size = os.path.getsize(F)
with open(F, 'rb') as fh:
    raw = fh.read()

text = raw.decode('utf-8')
out = 'D:\\私人资料\\deposon-repo\\.tmp\\_v16_tail_only.txt'
with open(out, 'w', encoding='utf-8') as fout:
    fout.write(text[-2200:])
print('wrote tail length 2200 to:', out)
print('file size:', size)
