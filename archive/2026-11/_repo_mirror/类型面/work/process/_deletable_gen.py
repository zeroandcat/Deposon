import os, json, hashlib
from collections import defaultdict

ARCH = r'〔归档区〕'
BATCHES = [
    ('tmp_archive_2026_10_29', '`.tmp` 过程件（HF-J）'),
    ('log_archive_2026_10_30', '运行日志（含已打码 34 件·密钥前缀）'),
    ('workprocess_archive_2026_10_30', '一次性仪器＋过程数据'),
    ('workprocess2_archive_2026_10_30', '一次性仪器＋body 中间件'),
    ('verifier_archive_2026_10_29', 'verifier runs 运行记录'),
    ('trae_ide_archive_2026_10_30', 'Trae 工具与交付物（含 arXiv tarball）'),
    ('deposon_team_archive_2026_10_30', '团队插件一次性脚本＋旧设计'),
    ('keyed_archive_2026_10_30', '含密钥件（已打码）'),
]

rows = []
for batch, desc in BATCHES:
    d = os.path.join(ARCH, batch)
    if not os.path.isdir(d):
        continue
    for dp, _, fs in os.walk(d):
        for fn in fs:
            p = os.path.join(dp, fn)
            try:
                sz = os.path.getsize(p)
            except Exception:
                continue
            rel = os.path.relpath(p, d).replace('\\', '/')
            ext = os.path.splitext(fn)[1].lower()
            rows.append((batch, desc, rel, sz, ext))

agg = defaultdict(lambda: {'n': 0, 'b': 0, 'ext': defaultdict(int)})
for batch, desc, rel, sz, ext in rows:
    a = agg[batch]
    a['n'] += 1
    a['b'] += sz
    a['ext'][ext] += 1

# 判：可删 / 须留
def verdict(batch, ext, fn):
    if batch.startswith('log_archive'):
        return ('可删', '运行日志·过程记录；其读数已在登记件')
    if batch.startswith('tmp_archive'):
        return ('可删', '`.tmp` 过程件（HF-J 明令禁传）')
    if batch.startswith('workprocess'):
        if ext in ('.py', '.ps1'):
            return ('可删', '一次性仪器脚本；结果已在登记件')
        if ext in ('.jsonl', '.csv', '.txt', '.json'):
            return ('可删', '过程数据（迁移/扫描/清理之产物）')
        return ('可删', 'body 中间件（内容已入正册）')
    if batch.startswith('verifier_archive'):
        return ('可删', 'runs 运行记录；`check.py` 与锚件、裁定件皆已留主区')
    if batch.startswith('deposon_team_archive'):
        if '/plugins/' in ('/' + rel_of.get(fn, '')):
            pass
        return ('可删', '一次性执行/审查脚本与旧设计报告')
    if batch.startswith('trae_ide'):
        if ext in ('.tar', '.gz') or fn.endswith('.tar.gz'):
            return ('须留', 'arXiv 投稿交付物（对外交付实体）')
        return ('可删', 'Trae 工具脚本与编译证据')
    if batch.startswith('keyed_archive'):
        return ('须留', '含密钥件（已打码）——留作审计凭据')
    return ('待判', '—')

rel_of = {}
for batch, desc, rel, sz, ext in rows:
    rel_of[(batch, os.path.basename(rel))] = rel

L = []
L.append('# 可删候选清单（候 KIMI 上传轮次执行）· 2026-10-30')
L.append('')
L.append('> 📌 **PI 之令**：「**有的件甚至可删，先归档等KIMI上传的同时再删**」＋卡答「**先仅归档，等KIMI上传时因不触归档区，安全删**」＋「**你来删**」。')
L.append('> 📌 **本件之职**：**只拟清单，不执行**——删之时点＝KIMI 上传那一轮（其理：上传不触归档区）。')
L.append('> 📌 **范围**：**只及归档区之八批**（本段所移 708 件所在）；主区（repo＋sub）之件**不在本清单**。')
L.append('> 📌 **观测时点**：2026-10-30 05:1x')
L.append('')
L.append('## §1 各批汇总（可删 / 须留）')
L.append('')
L.append('| 批 | 其性 | 件 | 字节 | 判 |')
L.append('|:--|:--|--:|--:|:--:|')
tot_del = tot_keep = 0
tot_del_b = tot_keep_b = 0
for batch, desc in BATCHES:
    if batch not in agg:
        continue
    a = agg[batch]
    # 批级判：trae 与 keyed 部分须留
    if batch.startswith('trae_ide'):
        v = '部分须留'
    elif batch.startswith('keyed'):
        v = '须留'
    else:
        v = '可删'
    if v == '可删':
        tot_del += a['n']; tot_del_b += a['b']
    else:
        tot_keep += a['n']; tot_keep_b += a['b']
    L.append('| `%s` | %s | %d | %d | **%s** |' % (batch, desc, a['n'], a['b'], v))
L.append('| **合** | — | **%d** | **%d** | 可删 %d／须留 %d |' % (tot_del + tot_keep, tot_del_b + tot_keep_b, tot_del, tot_keep))
L.append('')
L.append('## §2 须留者之明细（不删）')
L.append('')
L.append('| 类 | 件 | 由 |')
L.append('|:--|--:|:--|')
trae_keep = [r for r in rows if r[0].startswith('trae_ide') and (r[4] in ('.tar', '.gz'))]
keyed = [r for r in rows if r[0].startswith('keyed')]
L.append('| arXiv 投稿 tarball | %d | 对外交付实体（`deposon_arxiv_cn/en.tar.gz` 各约 1.6 MB） |' % len(trae_keep))
L.append('| 含密钥件（已打码） | %d | 审计凭据（manifest 记 sha12_before／after） |' % len(keyed))
L.append('')
L.append('## §3 执行之法（候上传轮次）')
L.append('')
L.append('1. **可恢复删除**（⛔0 永久删除）：经 mavis-trash 路由，逐件或按清单批。')
L.append('2. **删前复验**：每件核其仍在归档区原位、bytes 未变。')
L.append('3. **留 manifest**：删前记 `path／bytes／sha12`，可复建（内容另存于远端或他处者除外）。')
L.append('4. **时点**：与 KIMI 上传**同一轮**；因上传**不触归档区**，删归档区之件不影响上传。')
L.append('')
L.append('## §4 限')
L.append('')
L.append('1. 本清单**未逐件开卷**——批级判据来自各批移入时之开卷结论（见 `v647`–`v654`）。')
L.append('2. `deposon_team_archive` 之 `_designs/` 11 件为 **9 月设计报告**——删则 9 月设计脉络断；本部列「可删」**候 PI 一句**。')
L.append('3. 本件**未删任何件**。')

body = '\n'.join(L) + '\n'
OUT = r'〔本地路径已脱敏〕'
open(OUT, 'wb').write(body.encode('utf-8'))
print('BATCHES', len(agg), 'FILES', len(rows))
print('可删', tot_del, tot_del_b, ' 须留', tot_keep, tot_keep_b)
print('OUT_BYTES', os.path.getsize(OUT), 'SHA12', hashlib.sha256(open(OUT, 'rb').read()).hexdigest()[:12])
for b, a in sorted(agg.items(), key=lambda x: -x[1]['n']):
    print('  %-38s %4d 件 %12d B' % (b, a['n'], a['b']))
