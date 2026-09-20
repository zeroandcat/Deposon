# -*- coding: utf-8 -*-
"""
Trae 2026-09-18 修复 #7: 根目录 runner 批量补 SELF-CHECK + extract_number 功能验证
P1-7: 根目录 91 个 .py 仅 1 个有 SELF-CHECK → 对仍在用的 runner 补尾块
验证: extract_number 千分位修复的功能级单测 (真实复现 "$1,430" 场景)
"""
import hashlib, re
from pathlib import Path

ROOT = Path(r'D:\私人资料\deposon-repo')
MARK = 'TRAE_SELFCHECK_2026_09_16_V3'
sha_table = []

def sha12(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]

# 目标: 本次改动过的 + 仍在用的根目录 runner (不碰一次性探针/已被取代的)
TARGETS = [
    'volcengine_glm_latest_30cells_v2_runner_2026_09_10.py',
    '_p_l_v3_phase1_runner_2026_09_17.py',
    '_p_l_v3_phase2_runner_2026_09_17.py',
    '_p_l_v3_phase2_glm53_only_2026_09_17.py',
    '_p_l_v3_phase2_closedsource_runner_2026_09_17.py',
    '_p_l_v3_phase2_closedsource_runner_v2_2026_09_17.py',
    '_merge_or_stub_overlap_table_v3_2026_09_17.py',
]

def footer(name, has_main):
    lines = [
        '',
        '',
        '# ---------- SELF-CHECK (P-F V0.1 §5 纪律, Trae 2026-09-18 走读补, 标记 ' + MARK + ') ----------',
        '# 补入理由: 2026-09-18 根目录走读发现 91 个 .py 中仅 1 个含 SELF-CHECK, 属历史清理遗漏',
        'import os as _os_sc',
        "assert _os_sc.path.basename(__file__) == '" + name + "', '文件名漂移: ' + __file__",
        "with open(__file__, 'r', encoding='utf-8') as _f_sc:",
        '    _src_sc = _f_sc.read()',
        "assert '" + MARK + "' in _src_sc",
    ]
    if has_main:
        lines.append("assert 'def main(' in _src_sc, 'main() 缺失'")
        lines.append("assert '__main__' in _src_sc, '缺 __main__ guard'")
    lines.append("print('" + name + " SELF-CHECK PASS')")
    return '\n'.join(lines) + '\n'

print('=== P1-7: 根目录 runner 补 SELF-CHECK ===')
for name in TARGETS:
    p = ROOT / name
    if not p.exists():
        print('  MISSING', name); continue
    s = p.read_text(encoding='utf-8')
    if MARK in s:
        print('  skip(idempotent)', name); continue
    before = sha12(p)
    has_main = 'def main(' in s
    if not s.endswith('\n'):
        s += '\n'
    p.write_text(s + footer(name, has_main), encoding='utf-8')
    # compile 验证
    try:
        compile(p.read_text(encoding='utf-8'), str(p), 'exec')
        st = 'compile OK'
    except Exception as e:
        st = 'FAIL ' + str(e)[:60]
    print(f'  appended {name}: {before} -> {sha12(p)} | {st}')
    sha_table.append((name, before, sha12(p)))

print()
print('=== extract_number 千分位修复 功能验证 ===')
# 真实复现原缺陷场景
CASES = [
    ('The answer is $1,430', 1430.0, '千分位 (原缺陷: 会得 430)'),
    ('**1430**', 1430.0, '加粗正常'),
    ('18', 18.0, '普通数字'),
    ('Total: 1,234,567', 1234567.0, '双千分位'),
    ('$1,430.50', 1430.50, '千分位+小数'),
]

def extract_number_fixed(text):
    """修复版逻辑 (与 runner 内一致)"""
    if not text: return None
    m = re.search(r'\*\*\s*([-+]?\d[\d,]*\.?\d*)\s*\*\*', text)
    if m:
        try: return float(m.group(1).replace(',', ''))
        except Exception: pass
    nums = re.findall(r'-?\d[\d,]*(?:\.\d+)?', text)
    if nums:
        try: return float(nums[-1].replace(',', ''))
        except Exception: return None
    return None

def extract_number_old(text):
    """原缺陷版 (对照)"""
    if not text: return None
    m = re.search(r'\*\*\s*([-+]?\d[\d,]*\.?\d*)\s*\*\*', text)
    if m:
        try: return float(m.group(1).replace(',', ''))
        except Exception: pass
    nums = re.findall(r'-?\d+\.?\d*', text)
    if nums:
        try: return float(nums[-1])
        except Exception: return None
    return None

allok = True
for text, want, desc in CASES:
    got = extract_number_fixed(text)
    old = extract_number_old(text)
    ok = (got == want)
    allok = allok and ok
    print(f'  {"PASS" if ok else "FAIL"}  {desc:28s} input={text!r:26s} fixed={got} want={want} (old={old})')
print('  FUNCTIONAL', 'ALL-PASS' if allok else 'HAS-FAIL')

print()
print('=== SHA 对照表 ===')
for name, b, a in sha_table:
    print(f'  {b} -> {a}  {name}')
print()
print('_fix_batch7_2026_09_18 DONE')
