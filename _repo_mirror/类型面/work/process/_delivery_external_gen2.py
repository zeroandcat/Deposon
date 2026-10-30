import os, json, re, hashlib
from collections import defaultdict

ROOTS = {'repo': r'〔本地路径已脱敏〕', 'sub': r'〔本地路径已脱敏〕'}
UNION = r'〔本地路径已脱敏〕'
OUT = r'〔幽灵引用·未上传:_delivery_list_external_2026_10_30.md〕'

TYPE_FACES = ['verdict', 'evidence', 'doc', 'tool', 'readout', 'review', 'work', 'source']

# 词表（据 v636 §19 / v638 §20 之 PI 答）
WORDS = [
    ('大模型教师', '〔教师〕'), ('〔W老师〕', '〔教师〕'), ('W老师', '〔教师〕'), ('〔当事人W〕', '〔人员〕'),
    ('KIMI', '〔受托方A〕'), ('Kimi', '〔受托方A〕'), ('GLM', '〔受托方B〕'), ('Coze', '〔受托方C〕'),
    ('Trae', '〔受托方D〕'), ('OpenRouter', '〔平台〕'), ('Copilot', '〔受托方E〕'),
    ('Cohere', '〔受托方F〕'), ('Grok', '〔受托方G〕'), ('〔IM〕', '〔通讯平台〕'), ('〔IM〕', '〔通讯平台〕'),
    ('GPT', '〔模型〕'), ('Claude', '〔模型〕'), ('Gemini', '〔模型〕'), ('doubao', '〔模型〕'), ('豆包', '〔模型〕'),
    ('Qwen', '〔模型〕'), ('DeepSeek', '〔模型〕'), ('Codex', '〔受托方H〕'), ('MiniMax', '〔模型〕'),
    ('volcengine', '〔平台〕'), ('TEAMO', '〔平台〕'), ('workbuddy', '〔受托方I〕'),
]
DESENS = 0
def desense(s):
    global DESENS
    for a, b in WORDS:
        n = s.count(a)
        if n:
            DESENS += n
            s = s.replace(a, b)
    return s

blocked = set()
for line in open(UNION, 'rb'):
    line = line.strip()
    if not line:
        continue
    r = json.loads(line.decode('utf-8'))
    blocked.add((r['zone'], r['rel']))

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
            d = nodes[node]
            d['n'] += 1
            d['b'] += sz
            d['cls'][cls] += 1
            if (zone, rel) in blocked:
                d['nb'] += 1

order = {'L1': 0, 'L2': 1, 'L3': 2, 'L4': 3, 'L5': 4, '类型面': 5, 'results': 6, '顶层': 7, '根': 8}
rows = sorted(nodes.items(), key=lambda kv: (order.get(kv[0][0], 9), -kv[1]['n']))
tot_all = sum(v['n'] for _, v in rows)
tot_blk = sum(v['nb'] for _, v in rows)
tot_b = sum(v['b'] for _, v in rows)

L = []
L.append('# 成果清单（对外册 · 已脱敏）· 2026-10-30')
L.append('')
L.append('> 📌 **本件之职**：**对外册 ＝ 成果清单**（PI 逐字「**成果清单即对外册**，脱敏＋相对路径，**不再另立对外线索册**」）。')
L.append('> 📌 **脱敏之法**（PI 卡答 `v636` §19 逐字）：隐去「**大模型教师／〔W老师〕／W老师**」＋「**外部受托方与平台名**」＋「**各模型名**」——**本件正文已按词表替换为占位**（共替换 %d 处）。' % DESENS)
L.append('> 📌 **不隐节点**：`pi_rulings` **照列**（PI 逐字「pi_rulings不需要隐」）。')
L.append('> 📌 **路径**：一律**相对路径**（⛔ 不载本机绝对路径）。')
L.append('> 📌 **观测时点**：2026-10-30 04:4x')
L.append('')
L.append('## §0 总')
L.append('')
L.append('| 项 | 值 |')
L.append('|:--|--:|')
L.append('| 树节点数 | %d |' % len(rows))
L.append('| 上传面件数 | %d |' % tot_all)
L.append('| 其中在册禁传 | %d |' % tot_blk)
L.append('| **可上传** | **%d** |' % (tot_all - tot_blk))
L.append('| 字节 | %d（%.1f MB） |' % (tot_b, tot_b / 1048576))
L.append('')
L.append('## §1 依树分节点')
L.append('')
L.append('| 层 | 节点 | 件数 | 禁传 | **可上传** |')
L.append('|:--|:--|--:|--:|--:|')
for (layer, name), v in rows:
    L.append('| %s | %s | %d | %d | **%d** |' % (layer, name, v['n'], v['nb'], v['n'] - v['nb']))
L.append('')
L.append('## §2 L1 十二族')
L.append('')
L.append('| 族 | 类分布 | 件数 | 可上传 |')
L.append('|:--|:--|--:|--:|')
for (layer, name), v in rows:
    if layer != 'L1':
        continue
    cs = '；'.join('%s %d' % (c, n) for c, n in sorted(v['cls'].items(), key=lambda x: -x[1])[:6])
    L.append('| **%s** | %s | %d | **%d** |' % (name, cs, v['n'], v['n'] - v['nb']))
L.append('')
L.append('## §3 脱敏说明')
L.append('')
L.append('1. 本件正文**已按词表替换**：人（教师／人员）／外部受托方与平台／模型名 → 占位符。')
L.append('2. 此为本件之**唯一隐项**；**节点不隐、件不删**。')
L.append('3. 全件名不列（依 PI「只是罗列的话根本不需要清单」）；全表见内部清单。')

body = '\n'.join(L) + '\n'
DESENS = 0
body = desense(body)
open(OUT, 'wb').write(body.encode('utf-8'))
print('NODES', len(rows), 'ALL', tot_all, 'BLOCKED', tot_blk, 'PASS', tot_all - tot_blk)
print('DESENSITIZED_HITS', DESENS)
print('OUT_BYTES', os.path.getsize(OUT), 'SHA12', hashlib.sha256(open(OUT, 'rb').read()).hexdigest()[:12])
