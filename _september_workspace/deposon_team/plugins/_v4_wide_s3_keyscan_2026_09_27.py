# -*- coding: utf-8 -*-
"""
_v4_wide_s3_keyscan — 新件全量密钥样式扫描（沿 R4 铁律「key 永不明文·无例外」）
扫全部 mtime>=09-23 12:00 的**所有扩展名**新件；命中只记 文件+行号+样式名+前 8 字符，不打印完整 key。
"""
import os, re
from datetime import datetime

CUTOFF = datetime(2026, 9, 23, 12, 0, 0).timestamp()
ROOTS = [r'D:\私人资料\deposon-repo', r'D:\私人资料\deposon-sub']
SKIP = {'__pycache__', '.git', 'node_modules', '.trae'}
PAT = [
    ("api_key_literal", re.compile(r"(?i)api[_-]?key\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}")),
    ("sk_literal", re.compile(r"(?<![A-Za-z])sk-[A-Za-z0-9_\-]{16,}")),
    ("sk_or", re.compile(r"sk-or-v1-[A-Za-z0-9]{16,}")),
    ("sk_teamo", re.compile(r"sk-teamo-[A-Za-z0-9]{8,}")),
    ("sk_sp", re.compile(r"sk-sp-[A-Za-z0-9_\-\.]{8,}")),
    ("Bearer_tok", re.compile(r"Bearer\s+[A-Za-z0-9_\-\.]{30,}")),
    ("tp_token", re.compile(r"(?<![A-Za-z])tp-[A-Za-z0-9]{16,}")),
    ("ark_uuid", re.compile(r"(?<![A-Za-z0-9])[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}(?![A-Za-z0-9])")),
]
# 排除本扫描器自身与已知占位
EXCL_SELF = {'_v4_wide_s3_keyscan_2026_09_27.py', '_v4_wide_s2_scan_2026_09_27.py'}

hits = []
files_scanned = 0
for root in ROOTS:
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in SKIP]
        for fn in fns:
            if fn in EXCL_SELF: continue
            p = os.path.join(dp, fn)
            try:
                st = os.stat(p)
            except OSError: continue
            if st.st_mtime < CUTOFF: continue
            if st.st_size > 12_000_000: continue
            try:
                txt = open(p, 'rb').read().decode('utf-8', 'ignore')
            except Exception:
                continue
            files_scanned += 1
            for i, ln in enumerate(txt.splitlines(), 1):
                for name, rx in PAT:
                    m = rx.search(ln)
                    if m:
                        frag = m.group(0)[:14]
                        hits.append((p.replace(r'D:\私人资料' + os.sep, ''), i, name, frag))

print(f'=== 扫描新件 {files_scanned} 件（mtime >= 2026-09-23 12:00）===')
print(f'=== 命中 {len(hits)} 处 ===')
for h in hits[:80]:
    print(f'  {h[2]:<16} L{h[1]:<6} {h[3]:<16} {h[0]}')
if not hits:
    print('  0 命中 —— 新件内未发现任何密钥样式明文')

# 汇总：ark_uuid 属高误报类，单列计数
from collections import Counter
c = Counter(h[2] for h in hits)
print('\n=== 按样式汇总 ===')
for k, v in c.most_common():
    print(f'  {k:<18} {v}')
print('_wide_s3 DONE')
