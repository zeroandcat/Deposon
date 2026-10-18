# -*- coding: utf-8 -*-
"""
_v3_review_r7_fix_e15 — E-15 锚链复位（PI 授权「你直接修正」, 2026-09-23）
动作（三步，全部可回滚）：
  1) 备份顶替件（11,318B / 6E9CD8CD8E07）→ verifier/handoff/ 下新名 .bak（不覆盖任何既有文件）
  2) 从 _non_upload_local_archive 复制冻结期望件（6,680B / 03C6C01F3697）→ 冻结主路径
  3) 修后自验：主路径 SHA-12 == 03c6c01f3697
不改任何结论/判定；除主路径这一件外 0 字节写入。
"""
import hashlib, os, shutil, sys

REPO = r'D:\私人资料\deposon-repo'
PRIMARY = os.path.join(REPO, r'verifier\handoff\KT_ABC1_anchors_sha256_12.json')
SOURCE = r'D:\私人资料\_non_upload_local_archive\verifier\handoff\KT_ABC1_anchors_sha256_12.json'
BACKUP = os.path.join(REPO, r'verifier\handoff\KT_ABC1_anchors_sha256_12.root_session_11318B.bak_2026_09_23.json')
EXPECT = '03c6c01f3697'

def sha12(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]

print('=== 修前状态 ===')
pre_primary = sha12(PRIMARY)
pre_size = os.path.getsize(PRIMARY)
src_sha = sha12(SOURCE)
src_size = os.path.getsize(SOURCE)
print(f'  PRIMARY : {pre_primary.upper()}  {pre_size:>6}B  {PRIMARY}')
print(f'  SOURCE  : {src_sha.upper()}  {src_size:>6}B  {SOURCE}')
print(f'  EXPECT  : {EXPECT.upper()}')
assert pre_primary != EXPECT, '主路径已是期望值，无需修复（幂等保护）'
assert src_sha == EXPECT, '源件不是期望值，中止（防错源）'
assert src_size == 6680, '源件尺寸与 _v4_reader_verify 记录(6680B)不符，中止'

# --- 步骤 1: 备份顶替件 ---
assert not os.path.exists(BACKUP), '备份名已被占用，中止（防覆盖）'
shutil.copy2(PRIMARY, BACKUP)
b_sha, b_size = sha12(BACKUP), os.path.getsize(BACKUP)
assert b_sha == pre_primary and b_size == pre_size, '备份校验失败'
print()
print('=== 步骤 1: 顶替件已备份 ===')
print(f'  {b_sha.upper()}  {b_size:>6}B  verifier/handoff/KT_ABC1_anchors_sha256_12.root_session_11318B.bak_2026_09_23.json')

# --- 步骤 2: 复位冻结期望件 ---
shutil.copy2(SOURCE, PRIMARY)
print()
print('=== 步骤 2: 冻结期望件已复位至主路径 ===')
print(f'  copy2: _non_upload_local_archive -> verifier/handoff/KT_ABC1_anchors_sha256_12.json')

# --- 步骤 3: 修后自验 ---
post_sha = sha12(PRIMARY)
post_size = os.path.getsize(PRIMARY)
print()
print('=== 修后状态 ===')
print(f'  PRIMARY : {post_sha.upper()}  {post_size:>6}B  (期望 {EXPECT.upper()})')
ok = (post_sha == EXPECT and post_size == 6680)
print(f'  RESULT  : {"FIXED" if ok else "FAILED"}')

print()
print('=== 前后 SHA-12 对照（E-15） ===')
print(f'  verifier/handoff/KT_ABC1_anchors_sha256_12.json : {pre_primary.upper()} (11,318B) -> {post_sha.upper()} (6,680B)')
print(f'  新增备份件 bak_2026_09_23                        : {b_sha.upper()} (11,318B)')
print('_r7 DONE' if ok else '_r7 FAILED')
sys.exit(0 if ok else 1)
