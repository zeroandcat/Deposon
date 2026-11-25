# -*- coding: utf-8 -*-
import json, urllib.request, sys

UA = 'mavis-deposon-audit'
BASE = 'https://api.github.com/repos/zeroandcat/Deposon'

def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': 'application/vnd.github+json'})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode('utf-8'))

print('== repo meta ==')
meta = get(BASE)
default = meta.get('default_branch')
print('default_branch', default)

print('\n== ref head ==')
ref = get(BASE + '/git/ref/heads/' + default)
head_sha = ref['object']['sha']
print('HEAD', head_sha)

print('\n== tree (recursive) ==')
tree = get(BASE + '/git/trees/' + head_sha + '?recursive=1')
truncated = tree.get('truncated')
entries = tree.get('tree', [])
print('truncated', truncated, 'entries', len(entries))

blobs = [e for e in entries if e.get('type') == 'blob']
trees = [e for e in entries if e.get('type') == 'tree']
print('blobs', len(blobs), 'trees', len(trees))

# total bytes
tot = sum(e.get('size', 0) for e in blobs)
print('total_bytes', tot)

def under(prefix):
    sel = [e for e in blobs if e['path'].startswith(prefix)]
    return len(sel), sum(e.get('size', 0) for e in sel)

for p in ('_repo_mirror/', '_repo_mirror/agent_shared_2026_10_23/'):
    n, b = under(p)
    print('%-45s files=%5d bytes=%d' % (p, n, b))

# root README blob sha
readme = [e for e in blobs if e['path'] == 'README.md']
if readme:
    print('\nREADME.md blob_sha', readme[0]['sha'], 'size', readme[0].get('size'))

# save
out = r'〔本地路径已脱敏〕'
with open(out, 'w', encoding='utf-8', newline='\n') as f:
    json.dump({'head': head_sha, 'default_branch': default, 'truncated': truncated,
               'blobs': len(blobs), 'trees': len(trees), 'total_bytes': tot,
               'entries': entries}, f, ensure_ascii=False)
print('\nSAVED', out)
