# -*- coding: utf-8 -*-
"""
_audit_v3_runners_2026_09_16.py — V3 全实验(P-A~P-O)runner 静态审计: 幽灵引用/纪律缺失/硬编码

主职: 走读并改进 V3 全部实验代码。本脚本自动化最高价值的三类检测:
  1) 幽灵引用: 脚本内引用的 repo 相对路径是否存在(改名/删除后未同步的引用)
  2) 纪律缺失: 是否含 SELF-CHECK 块 / __main__ guard
  3) 硬编码: 绝对路径(C:\\ / D:\\ ) / 预登记阈值是否分散硬编码

0 LLM / 只读 / 不改任何文件
"""
import os
import re
import glob

BASE = r'D:\私人资料\deposon-repo'
PLUG = os.path.join(BASE, 'deposon_team', 'plugins')

TARGETS = sorted(
    glob.glob(os.path.join(PLUG, '_p_*.py')) +
    glob.glob(os.path.join(PLUG, 'boss_*.py')) +
    glob.glob(os.path.join(PLUG, 'attack_*.py')) +
    glob.glob(os.path.join(PLUG, 'skill_*.py')) +
    glob.glob(os.path.join(PLUG, '_v3x_*.py')) +
    glob.glob(os.path.join(PLUG, '_v42_*.py')) +
    glob.glob(os.path.join(PLUG, '_d7_*.py')) +
    glob.glob(os.path.join(PLUG, '_pg_v01_compute.py'))
)

# 引用路径模式: 形如 results/xxx.json / docs/xxx.md / verifier/xxx / corpus/xxx / deposon_team/xxx
REF_RE = re.compile(r'["\']((?:results|docs|verifier|corpus|deposon_team|tools|scripts)/[A-Za-z0-9_./\-\u4e00-\u9fff]+?\.(?:json|jsonl|md|py|txt|log))["\']')
ABS_RE = re.compile(r'["\']([A-Za-z]:\\\\?[^"\']+|[A-Za-z]:/[^"\']+)["\']')

print('=== V3 P-A~P-O runner 静态审计 (%d 文件) ===' % len(TARGETS))
print()
summary = []
for path in TARGETS:
    name = os.path.basename(path)
    with open(path, 'r', encoding='utf-8') as f:
        src = f.read()
    # 1) 幽灵引用
    refs = sorted(set(REF_RE.findall(src)))
    missing = []
    for r in refs:
        if not os.path.exists(os.path.join(BASE, r)):
            missing.append(r)
    # 2) 纪律
    has_sc = ('SELF-CHECK' in src) or ('SELF_CHECK' in src) or ('TRAE_SELFCHECK' in src)
    has_guard = ('__main__' in src)
    # 3) 硬编码绝对路径(排除注释里的说明性路径不算; 这里统计出现次数)
    abs_hits = [m for m in ABS_RE.findall(src)]
    ext_abs = [p for p in abs_hits if p.startswith('C:') or p.startswith('C/')]
    summary.append((name, missing, has_sc, has_guard, len(abs_hits), ext_abs))
    flag = 'OK'
    if missing:
        flag = 'GHOST'
    if not has_sc:
        flag += '+NO_SELFCHECK'
    if not has_guard:
        flag += '+NO_GUARD'
    if ext_abs:
        flag += '+EXT_ABS'
    print('[%s] %s' % (flag, name))
    if missing:
        for m in missing:
            print('    GHOST-REF: %s' % m)
    if ext_abs:
        print('    EXT-ABS(%d): %s' % (len(ext_abs), ext_abs[:3]))

print()
print('=== 汇总 ===')
print('文件数: %d' % len(summary))
print('幽灵引用文件: %d' % sum(1 for s in summary if s[1]))
print('缺 SELF-CHECK: %d' % sum(1 for s in summary if not s[2]))
print('缺 __main__ guard: %d' % sum(1 for s in summary if not s[3]))
print('含 repo 外绝对路径: %d' % sum(1 for s in summary if s[5]))
print()
print('GHOST-REF 明细:')
for name, missing, *_ in summary:
    if missing:
        print('  %s: %s' % (name, missing))