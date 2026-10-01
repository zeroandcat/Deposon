# -*- coding: utf-8 -*-
"""_v4_wide_s3c_keydetail — 定位 api_key_literal 命中 + ark- 前缀真 key + Authorization 明文（只读）"""
import os, re
from datetime import datetime
CUTOFF = datetime(2026, 9, 23, 12, 0, 0).timestamp()
ROOTS = [r'D:\私人资料\deposon-repo', r'D:\私人资料\deposon-sub']
SKIP = {'__pycache__', '.git', 'node_modules', '.trae'}
PATTERNS = [
    ("api_key_literal", re.compile(r"(?i)api[_-]?key\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}")),
    ("ark_prefix", re.compile(r"(?<![A-Za-z0-9])ark-[A-Za-z0-9_\-]{12,}")),
    ("auth_bearer_lit", re.compile(r"['\"]Authorization['\"]\s*:\s*['\"]Bearer\s+[A-Za-z0-9_\-\.]{20,}")),
    ("openai_sk", re.compile(r"sk-[A-Za-z0-9]{32,}")),
]
hits = []
for root in ROOTS:
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in SKIP]
        for fn in fns:
            p = os.path.join(dp, fn)
            try: st = os.stat(p)
            except OSError: continue
            if st.st_mtime < CUTOFF or st.st_size > 12_000_000: continue
            try: txt = open(p, 'rb').read().decode('utf-8', 'ignore')
            except Exception: continue
            for i, ln in enumerate(txt.splitlines(), 1):
                for name, rx in PATTERNS:
                    m = rx.search(ln)
                    if m:
                        # 只显示遮蔽形式：前 6 + 长度
                        g = m.group(0)
                        red = g[:6] + '#' * max(0, len(g) - 6)
                        hits.append((p.replace(r'D:\私人资料' + os.sep, ''), i, name, red[:40]))

print(f'=== 命中 {len(hits)} 处 ===')
for h in hits[:60]:
    print(f'  [{h[2]}] L{h[1]}  {h[3]}')
    print(f'        {h[0]}')
if not hits:
    print('  0 命中')

print()
print('=== 反向核验：executor 中 KEY_SOURCE_PATH 的写法统计 ===')
cnt = {}
for root in ROOTS:
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in SKIP]
        for fn in fns:
            if not fn.endswith('.py'): continue
            p = os.path.join(dp, fn)
            try: st = os.stat(p)
            except OSError: continue
            if st.st_mtime < CUTOFF: continue
            txt = open(p, 'rb').read().decode('utf-8', 'ignore')
            for m in re.finditer(r'KEY_SOURCE\w*\s*=\s*["\']([^"\']+)["\']', txt):
                cnt[m.group(1)] = cnt.get(m.group(1), 0) + 1
for k, v in sorted(cnt.items(), key=lambda x: -x[1]):
    print(f'  {v:>3}x  {k}')
print('_wide_s3c DONE')
