import os, json, hashlib
from collections import defaultdict

ROOTS = {'repo': r'〔本地路径已脱敏〕', 'sub': r'〔本地路径已脱敏〕'}
UNION = r'〔本地路径已脱敏〕'
OUT = r'〔幽灵引用·未上传:_delivery_list_external_2026_10_30.md〕'

L1_FAMS = ['V3', 'V4', 'V5', '委托面', 'S3S4', 'T', 'G-E01', 'ηETAC', 'K-杀线', 'K-EXP8', '39词']
TYPE_FACES = ['verdict', 'evidence', 'doc', 'tool', 'readout', 'review', 'work', 'source']

# 并集：不上传者（key -> why）
blocked = {}
for line in open(UNION, 'rb'):
    line = line.strip()
    if not line:
        continue
    r = json.loads(line.decode('utf-8'))
    blocked[(r['zone'], r['rel'])] = r.get('why', [])

HIDDEN_NODES = {('顶层', 'pi_rulings')}  # 整节点隐（HF-M）

nodes = defaultdict(lambda: {'n': 0, 'nb': 0, 'b': 0, 'cls': defaultdict(int)})

for zone, root in ROOTS.items():
    for dp, _, fs in os.walk(root):
        for fn in fs:
            p = os.path.join(dp, fn)
            rel = os.path.relpath(p, root).replace('\\', '/')
            parts = rel.split('/')
            try:
                sz = os.path.getsize(p)
            except Exception:
                continue
            if parts[0] == 'results' and len(parts) >= 3 and parts[1] == 'L1':
                node = ('L1', parts[2]); cls = parts[3] if len(parts) > 3 else '(flat)'
            elif parts[0] == 'results' and len(parts) >= 3 and parts[1] in ('L2', 'L3', 'L4', 'L5'):
                node = (parts[1], parts[2]); cls = parts[3] if len(parts) > 3 else '(flat)'
            elif parts[0] == 'results' and len(parts) >= 2 and parts[1] in TYPE_FACES:
                node = ('类型面', 'results/' + parts[1]); cls = parts[2] if len(parts) > 2 else '(flat)'
            elif parts[0] == 'results':
                node = ('results', '其他'); cls = parts[1] if len(parts) > 1 else '(flat)'
            elif len(parts) == 1:
                node = ('根', zone); cls = '(flat)'
            else:
                node = ('顶层', parts[0]); cls = parts[1] if len(parts) > 2 else '(flat)'
            if node in HIDDEN_NODES:
                continue
            d = nodes[node]
            d['n'] += 1
            d['b'] += sz
            d['cls'][cls] += 1
            if (zone, rel) in blocked:
                d['nb'] += 1

order = {'L1': 0, 'L2': 1, 'L3': 2, 'L4': 3, 'L5': 4, '类型面': 5, 'results': 6, '顶层': 7, '根': 8}
rows = sorted(nodes.items(), key=lambda kv: (order.get(kv[0][0], 9), -kv[1]['n']))

tot_pass = sum(v['n'] - v['nb'] for _, v in rows)
tot_all = sum(v['n'] for _, v in rows)
tot_b = sum(v['b'] for _, v in rows)

L = []
L.append('# 成果清单（对外口径）· 2026-10-30')
L.append('')
L.append('> 📌 **本件之职**：**对外清单**——**可上传**、**隐去敏感面**（PI 逐字：「**清单对外需隐去敏感面且可上传**」）。')
L.append('> 📌 **其别**：内部全提及者见 `results/work/process/_clue_book_internal_2026_10_30.md`（**该册不上传**）。')
L.append('> 📌 **隐去之面**（本件不列、不计）：`pi_rulings` 答卡族（`HF-M`）／`letters` 之非理论值面（`HF-A`）／PI 思考链蒸馏 `dataset` 族 23 件（`HF-D`）／内部真册（`HF-H`）／`E6`·`E7` 项目汇报与审计件／含密钥前缀件。')
L.append('> 📌 **观测时点**：2026-10-30 04:1x（本部当刻直算）')
L.append('')
L.append('## §0 总')
L.append('')
L.append('| 项 | 值 |')
L.append('|:--|--:|')
L.append('| 树节点数（已隐 `pi_rulings`） | %d |' % len(rows))
L.append('| 上传面件数（含待隐者） | %d |' % tot_all)
L.append('| **可上传件数（扣除在册禁传者）** | **%d** |' % tot_pass)
L.append('| 字节 | %d（%.1f MB） |' % (tot_b, tot_b / 1048576))
L.append('')
L.append('---')
L.append('')
L.append('## §1 依树分节点（件数 · 可上传数）')
L.append('')
L.append('| 层 | 节点 | 件数 | 其中禁传 | **可上传** |')
L.append('|:--|:--|--:|--:|--:|')
for (layer, name), v in rows:
    L.append('| %s | %s | %d | %d | **%d** |' % (layer, name, v['n'], v['nb'], v['n'] - v['nb']))
L.append('')
L.append('## §2 L1 十二族之细分（对外口径）')
L.append('')
L.append('| 族 | 类分布 | 件数 | 可上传 |')
L.append('|:--|:--|--:|--:|')
for (layer, name), v in rows:
    if layer != 'L1':
        continue
    cls_s = '；'.join('%s %d' % (c, n) for c, n in sorted(v['cls'].items(), key=lambda x: -x[1])[:6])
    L.append('| **%s** | %s | %d | **%d** |' % (name, cls_s, v['n'], v['n'] - v['nb']))
L.append('')
L.append('## §3 说明')
L.append('')
L.append('1. **隐去者不列也不计**——上表之「可上传」已扣在册禁传件；被隐之节点（`pi_rulings`）整节不出。')
L.append('2. **不作「罗列」**：每节点只给件数与类分布，**不列全件名**（PI 令「只是罗列的话根本不需要清单」）。')
L.append('3. 敏感面之**内部全提及**见线索册（不上传），本件与之**分置**。')
L.append('4. 归档区 20,371 件不在射程（只及上传面）。')

body = '\n'.join(L) + '\n'
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'wb').write(body.encode('utf-8'))
print('NODES', len(rows), 'ALL', tot_all, 'PASS', tot_pass)
print('OUT', OUT, os.path.getsize(OUT))
print('SHA12', hashlib.sha256(open(OUT, 'rb').read()).hexdigest()[:12])
