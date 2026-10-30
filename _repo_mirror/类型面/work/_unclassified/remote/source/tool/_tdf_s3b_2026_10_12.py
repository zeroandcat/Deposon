# -*- coding: utf-8 -*-
"""_tdf_s3b — 项 7 v24 跳点（去首行段法）复算（只读）"""
import hashlib, re
from pathlib import Path
REPO = Path(r'_repo_mirror')
p = REPO / 'docs' / 'V3X' / 'TRAE_V3_ASSET_ERRATUM_2026_09_23.md'
b = p.read_bytes()
t = b.decode('utf-8')
first_line = t.splitlines()[0]
n_first = len(first_line.encode('utf-8')) + 1  # +LF
print(f'当前首行: {first_line[:80]}')
print(f'首行字节（含 LF） = {n_first}  (v25 新标题须 = 125)')
# 去首行段的前 327,907 B（= v24 去首行段）
seg = b[n_first: n_first + 327907]
print(f'去首行段前 327,907 B SHA-12 = {hashlib.sha256(seg).hexdigest()[:12]}  (委托 L2828 记 v24 去首行 = 2E51A9FBC8FE)')
# 找旧标题 67 B 字面（勘误件 §22.32 段）
for m in re.finditer(r'[^\n]{0,60}旧标题[^\n]{0,120}', t):
    print(f'  候选行: {m.group(0)[:180]}')
for m in re.finditer(r'回填[^\n]{0,160}', t):
    print(f'  回填行: {m.group(0)[:180]}')
# 尝试：v24 标题 = 当前标题去掉 v25 增补段（猜：新旧标题公共前缀）
# 直接找 §22.32 上下文
i = t.find('§22.32')
if i >= 0:
    print('--- §22.32 段（前 1600 字符） ---')
    print(t[i:i+1600])
print('_tdf_s3b DONE')
