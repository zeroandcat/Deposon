# -*- coding: utf-8 -*-
import hashlib

P = r'〔本地路径已脱敏〕'
t = open(P, 'rb').read().replace(b'\xef\xbb\xbf', b'').replace(b'\r', b'').decode('utf-8')

A1 = '| **对外成果清单（新版）** | 仓根 `_delivery_list_external_<新日期>.md` | **对外成果索引**（⛔ 0 覆写 `…_2026_10_30.md`，旧件 0 触动） |'
B1 = ('| **对外成果清单（新版）** | **⛔ 不放仓根**（PI 令：根目录**只放 README 一份对外件**，清单属镜像区）'
      '——**本地暂存** `results/work/process/_delivery_list_external_<新日期>.md`；'
      '**云端落点** ＝ `_repo_mirror/doc/_delivery_list_external_<日期>.md`（§4-3 之 M5） | '
      '**对外成果索引**（⛔ 0 覆写 `…_2026_10_30.md`，旧件 0 触动） |')

A2 = '| **镜像区门面 README（新版）** | 仓根 **`README.md`**'
B2 = '| **镜像区门面 README（新版）**（**对外件中唯一置根者**·PI 令） | 仓根 **`README.md`**'

n1 = t.count(A1)
n2 = t.count(A2)
t = t.replace(A1, B1).replace(A2, B2)

open(P, 'wb').write(t.encode('utf-8'))
c = open(P, 'rb').read()
print('REPLACED', n1, n2)
print('BYTES', len(c), 'SHA12', hashlib.sha256(c).hexdigest()[:12], 'CR', c.count(b'\r'), 'LAST', hex(c[-1]))
s = c.decode('utf-8')
for probe in ('仓根 `_delivery_list_external_<新日期>.md`', '不放仓根', '唯一置根者'):
    print('  has %-40s %d' % (probe, s.count(probe)))
