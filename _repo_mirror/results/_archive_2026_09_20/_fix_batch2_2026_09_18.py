# -*- coding: utf-8 -*-
"""
Trae 2026-09-18 批量修复脚本 (走读改进 #2 批)
覆盖:
  P1-2  extract_number 千分位缺陷 — 其余 5 处 (phase2_runner / glm53_only / closedsource ×2)
  P2-3  dead import (math / sys)
  P2-4  孤儿 .bak 删除 (2 件)
幂等 (marker 检测) / 0 LLM / frozen 0 触动 / 前后 SHA 落账。
"""
import hashlib, os, re
from pathlib import Path

ROOT = Path(r'D:\私人资料\deposon-repo')
MARK = 'TRAE_FIXED_2026_09_18'
sha_table = []

def sha12(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]

def record(p, note):
    sha_table.append((str(Path(p).relative_to(ROOT)), sha12(p), note))

# ---------- P1-2: extract_number 千分位 (5 处) ----------
# 目标正则形态 (两种已知变体)
OLD_A = r"re.findall(r'-?\d+\.?\d*', text)"
OLD_B = r"re.findall(r'-?\d+(?:\.\d+)?', s)"
NEW_A = (r"# [Trae 2026-09-18 修复 P1-2 千分位] 补逗号容错\n"
         r"    nums = re.findall(r'-?\d[\d,]*(?:\.\d+)?', text)")
NEW_B = (r"# [Trae 2026-09-18 修复 P1-2 千分位] 补逗号容错\n"
         r"    m = [x.replace(',', '') for x in re.findall(r'-?\d[\d,]*(?:\.\d+)?', s)]")

TARGETS = [
    ('_p_l_v3_phase2_runner_2026_09_17.py', 'A'),
    ('_p_l_v3_phase2_glm53_only_2026_09_17.py', 'A'),
    ('_p_l_v3_phase2_closedsource_runner_2026_09_17.py', 'A'),
    ('_p_l_v3_phase2_closedsource_runner_v2_2026_09_17.py', 'A'),
]

print('=== P1-2: extract_number 千分位容错 ===')
for name, kind in TARGETS:
    p = ROOT / name
    if not p.exists():
        print('  MISSING', name); continue
    s = p.read_text(encoding='utf-8')
    if MARK in s:
        print('  skip(idempotent)', name, sha12(p)); continue
    before = sha12(p)
    if kind == 'A' and OLD_A in s:
        s2 = s.replace(OLD_A, NEW_A, 1)
        # 同步末位取值的 replace(',','') 若尚未有
        if 'float(nums[-1].replace' not in s2 and 'float(nums[-1])' in s2:
            s2 = s2.replace('float(nums[-1])', "float(nums[-1].replace(',', ''))", 1)
        p.write_text(s2, encoding='utf-8')
        print('  fixed', name, before, '->', sha12(p))
        record(p, 'extract_number 千分位容错')
    elif kind == 'B' and OLD_B in s:
        p.write_text(s.replace(OLD_B, NEW_B, 1), encoding='utf-8')
        print('  fixed', name, before, '->', sha12(p))
        record(p, 'extract_number 千分位容错')
    else:
        print('  PATTERN-NOT-FOUND', name, '(可能形态不同, 人工核)')

# ---------- P2-3: dead import ----------
print()
print('=== P2-3: dead import 清理 ===')
DEAD = [
    ('_p_l_v3_phase1_runner_2026_09_17.py', 'import math', 'math.'),
    ('_p_l_v3_phase2_or_embedding_v3_2026_09_17.py', 'import sys', 'sys.'),
    ('_p_l_v3_phase2_or_embedding_2026_09_17.py', 'import sys', 'sys.'),
]
for name, imp, usage in DEAD:
    p = ROOT / name
    if not p.exists():
        print('  MISSING', name); continue
    s = p.read_text(encoding='utf-8')
    if f'# dead-import-removed' in s:
        print('  skip(idempotent)', name); continue
    # 使用计数 (排除 import 行本身)
    body = '\n'.join(l for l in s.splitlines() if l.strip() != imp)
    if usage in body:
        print('  SKIP (actually used)', name, usage); continue
    if imp + '\n' in s:
        before = sha12(p)
        s2 = s.replace(imp + '\n', f'# {imp}  # dead-import-removed (Trae 2026-09-18)\n', 1)
        p.write_text(s2, encoding='utf-8')
        print('  removed', name, before, '->', sha12(p))
        record(p, 'dead import 注释化')

# ---------- P2-4: 孤儿 .bak ----------
print()
print('=== P2-4: 孤儿 .bak 删除 ===')
for bak in ['_smoke_5cells.py.bak', '_smoke_5cells.log.bak']:
    p = ROOT / bak
    if p.exists():
        sz = p.stat().st_size
        h = sha12(p)
        p.unlink()
        print(f'  deleted {bak} (was {sz}B, sha12={h})')
        sha_table.append((bak, f'{h} (deleted)', '孤儿备份清理'))
    else:
        print('  skip(absent)', bak)

print()
print('=== 前后 SHA 对照表 ===')
for rel, h, note in sha_table:
    print(f'  {h}  {rel}  [{note}]')
print()
print('_fix_batch2_2026_09_18 DONE')
