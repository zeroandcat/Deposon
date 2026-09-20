# -*- coding: utf-8 -*-
"""
Trae 2026-09-18 修复 #3: FTFB v3 包文件名乱码修复 + manifest 对齐 + verifier 归档件标注
P0-2: 简报 md 文件名 GBK/UTF-8 乱码 → 重命名为 manifest 记录名 (戴夫_FTFB双审包简报v3_2026-09-17.md)
P1-4: v36/v37 check.sh 失效引用加 archive-only 标注 (引用文件已随 358 件归档移出)
幂等 / 0 LLM / 前后 SHA 落账
"""
import hashlib, os
from pathlib import Path

ROOT = Path(r'D:\私人资料\deposon-repo')
PKG = ROOT / 'results' / '_ftfb_external_review_v3_20260917_extracted' / 'ftfb_external_review_v3_20260917'

def sha12(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]

print('=== P0-2: FTFB v3 简报文件名乱码修复 ===')
target_name = '戴夫_FTFB双审包简报v3_2026-09-17.md'
garbled = None
for f in PKG.iterdir():
    if f.suffix == '.md' and 'FTFB' in f.name and 'fiction' not in f.name:
        garbled = f
        break
if garbled is None:
    print('  未找到乱码 md (可能已修复)')
else:
    if garbled.name == target_name:
        print('  skip(idempotent): 已是正确名')
    else:
        dst = PKG / target_name
        h_before = sha12(garbled)
        sz = garbled.stat().st_size
        if dst.exists():
            print('  目标名已存在, 删除乱码副本', garbled.name)
            garbled.unlink()
        else:
            garbled.rename(dst)
            print(f'  renamed: {garbled.name!r} -> {target_name!r} ({sz}B, sha12={h_before} 不变)')

# 校验 manifest 5/5
print()
print('=== FTFB v3 包 manifest 校验 ===')
man = PKG / 'SHA256_MANIFEST.txt'
if man.exists():
    text = man.read_text(encoding='utf-8')
    ok = True
    for line in text.strip().splitlines():
        parts = line.split()
        if len(parts) < 2:
            continue
        h, name = parts[0], parts[1]   # 格式: <sha256>  <filename>  [size bytes]
        if len(h) != 64:
            continue
        p = PKG / name
        if not p.exists():
            print(f'  MISSING {name}'); ok = False; continue
        actual = hashlib.sha256(p.read_bytes()).hexdigest()
        m = actual[:12] == h[:12]
        print(f'  {"MATCH" if m else "MISMATCH"} {name} (manifest={h[:12]}, actual={actual[:12]})')
        ok = ok and m
    print('  MANIFEST', 'ALL-MATCH' if ok else 'HAS-MISMATCH')

print()
print('=== P1-4: v36/v37 check.sh 归档件标注 ===')
for v in ['v36', 'v37']:
    p = ROOT / 'verifier' / v / 'check.sh'
    if not p.exists():
        print('  MISSING', v); continue
    s = p.read_text(encoding='utf-8')
    if 'TRAE_ARCHIVE_NOTE_2026_09_18' in s:
        print('  skip(idempotent)', v); continue
    before = sha12(p)
    note = ('# [TRAE_ARCHIVE_NOTE_2026_09_18] 本 check.sh 引用的部分交付件 (deposon_v3定义与博弈论贡献思考_2026.md /\n'
            '#   deposon_成果汇报_2026.md 等) 已随 358 件归档移出本仓, 本地直接复跑将 FAIL;\n'
            '#   如需复跑请先恢复对应归档件 (见 results/_letter_to_kimi_push_v3_final_v2_2026_09_17.md 归档清单)。\n')
    p.write_text(note + s, encoding='utf-8')
    print('  annotated', v, before, '->', sha12(p))

print()
print('_fix_batch3_2026_09_18 DONE')
