import os, json, hashlib, re

ROOTS = {'repo': r'〔本地路径已脱敏〕', 'sub': r'〔本地路径已脱敏〕'}
V10 = r'〔本地路径已脱敏〕'
OUT = r'〔本地路径已脱敏〕'

INTERNAL_PAT = [
    (r'^_experiment_tree_v2_main', '内部册:树册'),
    (r'^_root_session_history_memo_main', '内部册:主代理册'),
    (r'^_sub_agent_memo', '内部册:子代理册'),
    (r'_book_\d', '内部册:合册'),
    (r'_cardbook_', '内部册:合册'),
    (r'^_pending_pi_master', '内部册:候PI余额册'),
    (r'_remote_local_reconciliation', '内部册:对账清单'),
    (r'_repo_full_inventory_catalogue', '内部册:盘面编目'),
    (r'_repo_post_cleanup_snapshot', '内部册:盘面快照'),
    (r'^_clue_book_internal', '内部册:线索册'),
    (r'^_achievements_', '内部册:成果清单'),
    (r'_mirror_face_', '内部册:镜像面勘查'),
    (r'_closeout_bucket_refresh', '内部册:收尾桶'),
    (r'^_internal_true_clue_book', '内部册:内部真册'),
    (r'^_inventory_(full|by_tree)', '内部册:清册'),
]

def internal(fn, rel):
    for pat, why in INTERNAL_PAT:
        if re.search(pat, fn) or re.search(pat, rel):
            return why
    return None

# 1) 读 v10，分流：非22类者原样保留；22类者待重判
kept, redo = {}, []
for line in open(V10, 'rb'):
    line = line.strip()
    if not line:
        continue
    r = json.loads(line.decode('utf-8'))
    whys = r.get('why', [])
    if any(w.startswith('22类:') for w in whys):
        others = [w for w in whys if not w.startswith('22类:')]
        if others:
            r['why'] = others
            kept[(r['zone'], r['rel'])] = r
        else:
            redo.append(r)
    else:
        kept[(r['zone'], r['rel'])] = r

# 2) 重判 22 类之件
promoted, still = 0, 0
for r in redo:
    fn = os.path.basename(r['rel'])
    p = os.path.join(ROOTS[r['zone']], r['rel'].replace('/', os.sep))
    if not os.path.isfile(p):
        continue
    why = internal(fn, r['rel'])
    if why:
        r['why'] = [why]
        kept[(r['zone'], r['rel'])] = r
        still += 1
    else:
        promoted += 1        # 转可传（不入并集）

with open(OUT, 'wb') as f:
    for k in sorted(kept):
        f.write(json.dumps(kept[k], ensure_ascii=False, sort_keys=True).encode('utf-8') + b'\n')

from collections import Counter
c = Counter()
for v in kept.values():
    for w in v['why']:
        c[w.split(':')[0]] += 1

v10n = sum(1 for _ in open(V10, 'rb'))
print('V10', v10n, '-> V11', len(kept), ' 差', len(kept) - v10n)
print('  22类重判：转可传', promoted, '／归内部册', still)
print()
print('V11 之判据分布：')
for k, v in c.most_common():
    print('   %-12s %3d' % (k, v))
print()
print('OUT_BYTES', os.path.getsize(OUT))
print('OUT_SHA12', hashlib.sha256(open(OUT, 'rb').read()).hexdigest()[:12])

# 上传面
tot = 0
for z, root in ROOTS.items():
    for dp, _, fs in os.walk(root):
        tot += len(fs)
print()
print('盘上 repo+sub', tot, ' 扣', len(kept), ' 可传', tot - len(kept))
