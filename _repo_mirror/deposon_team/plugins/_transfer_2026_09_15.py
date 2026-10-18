# -*- coding: utf-8 -*-
"""Transfer executor - 沿 user 14:54 + 15:40 + 15:46 "按推荐来"
严守 7 铁律 0 触动 18 frozen + P-G V0 spec + 16 frozen verify
"""
import os
import shutil
import sys
from pathlib import Path

SRC_BASE = Path(r'D:\私人资料\deposon-repo')
DST_BASE = Path(r'D:\私人资料\_mavis_external')

# 创建目标子目录
subdirs = ['installers', 'backups', 'logs', 'proposals', 'scripts', 'reports', 'cache', 'tmp']
for sub in subdirs:
    path = DST_BASE / sub
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        print(f'CREATED: {path}')
    else:
        print(f'EXISTS:  {path}')

# 转移计划
transfers = [
    (SRC_BASE / '.mavis' / 'installers', DST_BASE / 'installers'),
    (SRC_BASE / '.mavis' / 'backups', DST_BASE / 'backups'),
    (SRC_BASE / '.mavis' / 'logs', DST_BASE / 'logs'),
    (SRC_BASE / '.mavis' / 'proposals', DST_BASE / 'proposals'),
    (SRC_BASE / '.mavis' / 'scripts', DST_BASE / 'scripts'),
    (SRC_BASE / '.mavis' / 'reports', DST_BASE / 'reports'),
    (SRC_BASE / '.mavis' / 'cache', DST_BASE / 'cache'),
    (SRC_BASE / '.tmp', DST_BASE / 'tmp' / '.tmp'),
    (SRC_BASE / '.tmp_volcengine_2026_09_10', DST_BASE / 'tmp' / '.tmp_volcengine_2026_09_10'),
    (SRC_BASE / '__pycache__', DST_BASE / 'tmp' / '__pycache__'),
    (SRC_BASE / '.pytest_cache', DST_BASE / 'tmp' / '.pytest_cache'),
]

print()
print('===== Transfer start =====')
for src, dst in transfers:
    if not src.exists():
        print(f'SKIP (not exists): {src}')
        continue

    # 算大小
    total = 0
    file_count = 0
    for root, dirs, files in os.walk(src):
        for f in files:
            try:
                total += os.path.getsize(os.path.join(root, f))
                file_count += 1
            except OSError:
                pass

    print()
    print(f'TRANSFER: {src}')
    print(f'  size: {total:,} bytes ({total/1024/1024:.2f} MB) ({file_count} files)')
    print(f'  -> {dst}')

    try:
        shutil.move(str(src), str(dst))
        print(f'  STATUS: OK')
    except Exception as e:
        print(f'  STATUS: FAILED - {e}')
        sys.exit(1)

print()
print('===== Transfer complete =====')
print(f'Source: {SRC_BASE}')
print(f'Dest:   {DST_BASE}')
