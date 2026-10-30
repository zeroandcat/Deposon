# -*- coding: utf-8 -*-
"""§26 探针十二：新窗五棒之落件归属（A 级直证 + 盘面候选 + 台账 owner）+ 本棒回件面"""
import os, json, re, hashlib, sqlite3, datetime, glob

TZ = datetime.timezone(datetime.timedelta(hours=8))
def ts(ms):
    return datetime.datetime.fromtimestamp(ms / 1000, TZ).strftime('%Y-%m-%d %H:%M:%S')

# A. 主会话一手记录中，五棒之派工/回件行
MAIN = r'〔本地路径已脱敏〕'
raw = open(MAIN, 'rb').read()
lines = [l for l in raw.decode('utf-8', 'replace').splitlines() if l.strip()]
ROD_IDS = ['bg_8b9bdf59', 'bg_156b760e', 'bg_d53d8381', 'bg_7c16da20', 'bg_5b4fcb87', 'bg_eed597a7']
print('== A. MAIN SESSION lines per rod id ==')
for rid in ROD_IDS:
    hit = [(i, l) for i, l in enumerate(lines, 1) if rid in l]
    print('  %-12s hits=%d at lines %s' % (rid, len(hit), [i for i, _ in hit][:12]))
print('  total lines', len(lines), 'bytes', len(raw), 'sha12', hashlib.sha256(raw).hexdigest()[:12])

print('\n== B. task_background tags in main session ==')
for i, l in enumerate(lines, 1):
    for m in re.finditer(r'<task_background[^>]*>', l):
        print('  L%d %s' % (i, m.group(0)))

print('\n== C. rod-related assistant text (first 300 chars) for each rod ==')
for i, l in enumerate(lines, 1):
    try:
        rec = json.loads(l)
    except Exception:
        continue
    msg = rec.get('message') or {}
    c = msg.get('content')
    if not isinstance(c, list):
        continue
    for x in c:
        if not isinstance(x, dict):
            continue
        if x.get('type') == 'text':
            t = x.get('text') or ''
            hit = [r for r in ROD_IDS if r in t]
            if hit:
                print('  L%-4d role=%-9s %s :: %s' % (i, msg.get('role'), '/'.join(hit), t.replace('\n', ' | ')[:280]))
        if x.get('type') == 'toolCall' and x.get('name') == 'task':
            a = x.get('arguments') or {}
            s = json.dumps(a, ensure_ascii=False)
            hit = [r for r in ROD_IDS if r in s]
            if hit:
                print('  L%-4d TASK-CALL %s :: desc=%r agent=%s' % (i, '/'.join(hit), str(a.get('description'))[:80], a.get('agent_name')))

print('\n== D. main-session mentions of the 5 non-self rods (any line, idx) ==')
for rid in ROD_IDS:
    hit = [i for i, l in enumerate(lines, 1) if rid in l]
    print('  %-12s %s' % (rid, hit))

print('\n== E. candidate landing files for the 5 rods (letters/ + repo root, mtime in window) ==')
W0, W1 = 1793278797762, 1793293267878
cands = []
for rt in (r'〔本地路径已脱敏〕', r'〔本地路径已脱敏〕'):
    for dp, dn, fn in os.walk(rt):
        dn[:] = [x for x in dn if x not in ('.git', 'node_modules', '__pycache__', 'results', 'letters', '.tmp')]
        for f in fn:
            p = os.path.join(dp, f)
            try:
                mt = os.path.getmtime(p) * 1000
            except Exception:
                continue
            if W0 <= mt <= W1:
                cands.append((mt, p))
seen = set()
for mt, p in sorted(cands):
    if p in seen:
        continue
    seen.add(p)
    raw2 = open(p, 'rb').read()
    print('  %s  %8d B  %s  %s' % (ts(mt), len(raw2), hashlib.sha256(raw2).hexdigest()[:12], p))

print('\n== F. v0.2 / v0.1 drafts on disk? ==')
for pat in ('_commission_kimi_mirror_replace*', '_commission_kimi_upload*'):
    for p in glob.glob(os.path.join(r'〔本地路径已脱敏〕', pat)):
        raw2 = open(p, 'rb').read()
        print('  %8d B  %s  mtime=%s  %s' % (len(raw2), hashlib.sha256(raw2).hexdigest()[:12], ts(os.path.getmtime(p) * 1000), p))
