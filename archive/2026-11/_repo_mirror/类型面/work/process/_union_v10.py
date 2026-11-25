import os, json, hashlib, re

ROOTS = {'repo': r'〔本地路径已脱敏〕', 'sub': r'〔本地路径已脱敏〕'}
V9 = r'〔本地路径已脱敏〕'
OUT = r'〔本地路径已脱敏〕'

# 1) 读 v9（只留仍在盘者）
base = {}
for line in open(V9, 'rb'):
    line = line.strip()
    if not line:
        continue
    r = json.loads(line.decode('utf-8'))
    p = os.path.join(ROOTS[r['zone']], r['rel'].replace('/', os.sep))
    if os.path.isfile(p):
        base[(r['zone'], r['rel'])] = r

# 2) 新件之判（不在 v9 者）
def judge(zone, rel, fn):
    low = rel.lower()
    if low.startswith('pi_rulings/') or '/pi_rulings/' in low:
        return 'HF-M:答卡登记族'
    if '/.mavis/' in '/' + low or low.startswith('.mavis/'):
        return '.gitignore:.mavis/'
    if '/.tmp/' in '/' + low or low.startswith('.tmp/'):
        return 'HF-J:.tmp/'
    if fn.lower().endswith('.log'):
        return '.gitignore:*.log'
    if low.startswith('letters/'):
        # 委托/回函面（加严①）——蒸馏件依 PI 令仍上传，不扣
        if re.search(r'commission|letter|reply|委托|回函', fn):
            return 'S21:letters委托回函面'
        return None
    if fn.startswith('_v') and fn.endswith('_body.md'):
        return 'PROC:本部落册中间体'
    if fn.startswith('_clue_') or fn.startswith('_nonupload_union_v'):
        return 'PROC:内部过程件'
    if fn.startswith('_delivery_list_'):
        return None      # 对外清单：可传
    if fn.startswith('README'):
        return None      # 门面/内部入口：可传（云端落点另定）
    if low.startswith('_handover') or fn.startswith('_HANDOVER'):
        return 'PROC:内部交接件'
    return None

added, kept, newpass = [], 0, []
allfiles = []
for zone, root in ROOTS.items():
    for dp, _, fs in os.walk(root):
        for fn in fs:
            p = os.path.join(dp, fn)
            rel = os.path.relpath(p, root).replace('\\', '/')
            allfiles.append((zone, rel, fn, os.path.getsize(p)))

for zone, rel, fn, sz in allfiles:
    k = (zone, rel)
    if k in base:
        kept += 1
        continue
    why = judge(zone, rel, fn)
    if why:
        base[k] = {'zone': zone, 'rel': rel, 'why': [why], 'bytes': sz}
        added.append((why, zone, rel, sz))
    else:
        newpass.append((zone, rel, sz))

with open(OUT, 'wb') as f:
    for k in sorted(base):
        f.write(json.dumps(base[k], ensure_ascii=False, sort_keys=True).encode('utf-8') + b'\n')

print('V9_ON_DISK', kept)
print('NEWLY_BLOCKED', len(added))
from collections import Counter
c = Counter(a[0] for a in added)
for k, v in c.most_common():
    print('   %-28s %3d' % (k, v))
print('NEWLY_PASSABLE', len(newpass))
print('V10_TOTAL', len(base))
print('OUT_BYTES', os.path.getsize(OUT))
print('OUT_SHA12', hashlib.sha256(open(OUT, 'rb').read()).hexdigest()[:12])
print()
print('--- 新判入者（前 14）---')
for why, zone, rel, sz in sorted(added, key=lambda x: -x[3])[:14]:
    print('  %9d %-6s %-26s %s' % (sz, zone, why.split(':')[0], rel[:72]))
