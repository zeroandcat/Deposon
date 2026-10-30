# -*- coding: utf-8 -*-
import hashlib

P = r'〔本地路径已脱敏〕'
b = open(P, 'rb').read()
b = b.replace(b'\xef\xbb\xbf', b'').replace(b'\r', b'')
t = b.decode('utf-8')
lines = t.split('\n')

NEW = [
 '1. **347 之口径**：并集**已全量重判**（v11）——原 v9 之 520 条中，**277 条支撑于「22 类内容判据」者**，经 PI 裁「**22 类不作上传判据**」后重判：**252 条转可传**、**13 条改归「内部册」新据**、9 条另有独立依据；其余各判原样承继。⇒ **v11 之 347 件皆为现值禁传界**（本部逐条核其在盘）。**⛔ 0 再引 v9 之 520 充现值**。',
 '',
 '2. **内部册禁传（新增依据·不赖 22 类）**：PI 裁「**内部册整体禁传**」⇒ 本部另立独立依据，扣 **34 件**：树册（346,571）／主代理册（**769,343**）／子代理册（**758,741**）／合册 `_book_*`、`_cardbook_*`（含 `_book_01` 5,673,128 等）／成果清单 `_achievements_*`（443,173／350,245）／候 PI 余额册 `_pending_pi_master_*`／对账清单／盘面编目／盘面快照／线索册／镜像面勘查／收尾桶／内部真册／清册。**唯一例外**：`_book_08_pi_cot_v2_verdict_2026_10_22.md`（60,347）——PI 明答「**可传**」，故**不扣**。',
 '',
 '3. **上传面件数** 之现值：**本部自测 repo 2,342 ＋ sub 1,531 ＝ 3,873**（观测 2026-10-30 15:0x）｜**禁传 347**｜**可上传 3,526**｜**以受托方执行前实测为准**（盘面在动，差数须如实报）。',
]

i0 = None
for i, l in enumerate(lines):
    if l.startswith('1. **520 与 516**'):
        i0 = i
        break
assert i0 is not None, 'anchor not found'
# 原三行（320/321/322）＝ lines[i0..i0+2]，含其间空行为 i0+1? 实测：三行连续无空行
old3 = lines[i0:i0+3]
assert old3[0].startswith('1. **520'), old3[0][:40]
assert old3[1].startswith('2. **⚠ 并集 v9'), old3[1][:40]
assert old3[2].startswith('3. **上传面件数**'), old3[2][:40]

lines[i0:i0+3] = NEW
out = '\n'.join(lines)
open(P, 'wb').write(out.encode('utf-8'))
c = open(P, 'rb').read()
print('NEW_BYTES', len(c), 'SHA12', hashlib.sha256(c).hexdigest()[:12])
print('CR', c.count(b'\r'), 'LAST', hex(c[-1]), 'LF', c.count(b'\n'))
for probe in ('520 与 516', 'v9 系快照', '3,831', '3,815'):
    print('  residual %-12s %d' % (probe, c.decode('utf-8').count(probe)))
