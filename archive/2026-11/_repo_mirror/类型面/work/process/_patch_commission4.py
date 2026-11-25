# -*- coding: utf-8 -*-
import hashlib

P = r'〔本地路径已脱敏〕'
t = open(P, 'rb').read().replace(b'\xef\xbb\xbf', b'').replace(b'\r', b'').decode('utf-8')

PAIRS = [
 # 1) §4-3 M5
 ('| **M5** | **门面件与清单** 之云端落点 ＝ `_repo_mirror/README.md` ＋ `_repo_mirror/doc/_delivery_list_external_<日期>.md`（**非按 M1–M4 改写**） | 逐路径核 |',
  '| **M5** | **门面件 README** 之云端落点 ＝ **远端仓根 `README.md`**（**PI 令：「readme 要落远端仓 deposon 的仓根」**·⛔ 非 `_repo_mirror/README.md`）｜**清单**之云端落点 ＝ `_repo_mirror/doc/_delivery_list_external_<日期>.md`（二者**非同处**） | 逐路径核：远端仓根 `README.md` 在新版指纹下；`_repo_mirror/` 内**无 README** |'),

 # 2) §5-9 两读 → 取甲（PI 已澄清）
 ('### 5-9 「镜像区门面 README」与「远端仓根 README.md」之别（**两读并出 · ⛔ 0 强合**）',
  '### 5-9 门面 README 之落点：**远端仓根**（PI 已澄清·本部前此两读作废）'),

 ('| # | 读 | 内容 | 在册依据 |\n|:-:|:--|:--|:--|\n| 甲 | **远端仓根 `README.md`** ＝ 外部读者进入**远端仓**之第一件 | 新版**顶替**之（PI：「旧版改名，新版取代」） | PI 逐字（§1-2 之五） |\n| 乙 | **镜像区 `_repo_mirror/README.md`** ＝ 镜像区之**门面入口件** | 新版**同批换上**（§4-3 之 M5） | PI 追加：「README 须落于镜像区根目录」 |\n\n⇒ 📌 **本件之处置**：**两处皆用新版**（同一内容、同一指纹），**由受托方在同批中一次落位**；⛔ 本件**0 代 PI 裁**「两者是否须为同一内容」——若 PI 另裁二者当有别，以 PI 裁为准（**一句话即改**）。',
  '**PI 逐字**：「**我意思是 readme 要落远端仓 deposon 的仓根**」\n\n| 面 | 落点 | 本案 |\n|:--|:--|:--|\n| **门面 README** | **远端仓根**（`https://github.com/zeroandcat/Deposon` 之 `README.md`） | 新版**顶替**之（PI：「旧版改名，新版取代」＋本轮澄清） |\n| **镜像区 `_repo_mirror/`** | **⛔ 不设 README** | 本部前此「镜像区门面 README」之读**作废**；镜像区内只放清单与按族落件 |\n\n⇒ 📌 **作废**：本部原 §5-9 之「两读并出（甲 仓根／乙 镜像区）」中，**乙读作废**——PI 已明示为**远端仓根**。'),

 # 3) §5-1 之表述
 ('⇒ 远端仓之 `README.md` ＝ **外部读者进入本仓之第一件**；其**状态列失实**',
  '⇒ **远端仓根之 `README.md`**（非镜像区内）＝ **外部读者进入本仓之第一件**；其**状态列失实**'),

 # 4) AC-5
 ('| **AC-5** | README 落 `_repo_mirror/README.md`；状态列 V3／V4 ＝ `closed`；**0 命中**争议面之任何指称字样与「V5」；**0 命中**受托方／平台／模型／人名 | 逐项 0 命中检 |',
  '| **AC-5** | README 落**远端仓根 `README.md`**（⛔ 非 `_repo_mirror/README.md`；镜像区内**无 README**）；状态列 V3／V4 ＝ `closed`；**0 命中**争议面之任何指称字样与「V5」；**0 命中**受托方／平台／模型／人名 | 逐项 0 命中检 |'),

 # 5) §4-2 之措辞（本地/远端两行之统一）
 ('| **镜像区门面 README（新版）**（**本地落点 ＝ `deposon-repo` 仓根**·PI 令：README 须放 deposon 仓根，非镜像区目录） | 仓根 **`README.md`**',
  '| **门面 README（新版）**（**本地落点 ＝ `deposon-repo` 仓根；云端落点 ＝ 远端仓根 `README.md`**·PI 令：「readme 要落远端仓 deposon 的仓根」） | 仓根 **`README.md`**'),

 # 6) §4-3 结构图：README 不属镜像区
 ('```\n云端镜像区（`_repo_mirror/`）\n├─ README.md                     ← 门面件（§5）：唯一入口，置顶\n├─ doc/',
  '```\n远端仓根（`zeroandcat/Deposon`）\n└─ README.md                     ← 门面件（§5）：**落仓根**，⛔ 不在镜像区内\n\n云端镜像区（`_repo_mirror/`）\n├─ doc/'),
]

hit = 0
miss = []
for a, b in PAIRS:
    c = t.count(a)
    if c == 0:
        miss.append(a[:46])
        continue
    t = t.replace(a, b)
    hit += 1

open(P, 'wb').write(t.encode('utf-8'))
c = open(P, 'rb').read()
print('HIT', hit, '/', len(PAIRS))
print('MISS', miss)
print('BYTES', len(c), 'SHA12', hashlib.sha256(c).hexdigest()[:12], 'CR', c.count(b'\r'), 'LAST', hex(c[-1]))
s = c.decode('utf-8')
for probe in ('_repo_mirror/README.md', '远端仓根', '镜像区内**无 README**'):
    print('  %-26s %d' % (probe, s.count(probe)))
