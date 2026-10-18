# -*- coding: utf-8 -*-
# DECISION: option_A (N2: 断言算子 < 改 <=, 阈值本身不动)
"""
fix_selfcheck_bug_n2_2026_09_15.py — N2 修补: boss_pc_1/3 尾块 D_FIX2 阈值断言自相矛盾

委托: LETTER_TO_TRAE_FIX_SELFCHECK_2026_09_15.md §2 (委托信 2026-09-15 15:30 落盘, 本修补执行 2026-09-16)
缺陷根因(Trae 自省): 上轮尾块断言 `D_FIX2_PASS_LT < D_FIX2_GRAY_GE` 与阈值定义
  (PASS_LT=0.05, GRAY_GE=0.05) 冲突 → 0.05 < 0.05 恒 False → import 即 AssertionError。
  D_fix2 strict 阈值语义 = [0, 0.05) PASS / [0.05, 0.15) GRAY / [0.15, +inf) FAIL,
  PASS 上界与 GRAY 下界本就应**相等衔接**, 断言写 < 是我对语义的误写。

方案裁定:
  option_A(断言 < 改 <=) = 修断言使其匹配阈值语义, 阈值数值 0.05/0.15 不动 → 采纳
  option_B(GRAY_GE 改 0.06) = 动阈值本身, 破坏 D5 1A 拍板的 strict 口径 → 否决
  (沿委托信推荐 A)

预注册判定线(计算前锁定):
  R1: 修后 boss_pc_1 + boss_pc_3 中不再存在 `D_FIX2_PASS_LT < D_FIX2_GRAY_GE`
  R2: 修后两文件 importlib 真执行无异常
  R3: 阈值常数值不动(0.05/0.05/0.15); boss_pc_2(断言本就正确)不动; 其他 9 文件不动
  R4: 幂等
"""
import os

BASE = r'D:\私人资料\deposon-repo'
PLUG = os.path.join(BASE, 'deposon_team', 'plugins')
N2_FILES = [
    'boss_pc_1_2d_ising_universality.py',
    'boss_pc_3_reservoir_computing.py',
]
OLD = 'assert D_FIX2_PASS_LT < D_FIX2_GRAY_GE <= D_FIX2_FAIL_GE'
NEW = 'assert D_FIX2_PASS_LT <= D_FIX2_GRAY_GE <= D_FIX2_FAIL_GE  # PASS 上界==GRAY 下界衔接(strict 语义)'


def rd(p):
    with open(p, 'r', encoding='utf-8') as f:
        return f.read()


def wr(p, s):
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)


def main():
    for fname in N2_FILES:
        p = os.path.join(PLUG, fname)
        s = rd(p)
        if OLD in s:
            s = s.replace(OLD, NEW, 1)
            wr(p, s)
            print(f'  [N2] {fname}: 断言算子 < → <=')
        else:
            assert NEW in s, f'{fname}: 旧断言不在且新断言不在, 状态异常'
            print(f'  [N2] {fname}: 已修, 跳过')


# ---------- SELF-CHECK (import 级真执行) ----------
main()

import importlib.util

for fname in N2_FILES:
    p = os.path.join(PLUG, fname)
    s = rd(p)
    # R1
    assert OLD not in s, f'{fname}: 旧断言残留'
    assert NEW in s, f'{fname}: 新断言缺失'
    # R3: 阈值常数值未动
    for line in s.splitlines():
        if line.startswith('D_FIX2_PASS_LT'):
            assert '0.05' in line, f'{fname}: D_FIX2_PASS_LT 数值被改: {line}'
        if line.startswith('D_FIX2_GRAY_GE'):
            assert '0.05' in line, f'{fname}: D_FIX2_GRAY_GE 数值被改: {line}'
        if line.startswith('D_FIX2_FAIL_GE'):
            assert '0.15' in line, f'{fname}: D_FIX2_FAIL_GE 数值被改: {line}'
    # R2: import 真执行
    spec = importlib.util.spec_from_file_location(fname[:-3], p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    print(f'  [SC] {fname}: 断言修正 + 阈值未动 + import 真执行 PASS')

# boss_pc_2 未动核验(R3)
s2 = rd(os.path.join(PLUG, 'boss_pc_2_transverse_field_ising.py'))
assert 'assert D_FIX2_PASS_LT < D_FIX2_FAIL_GE' in s2, 'boss_pc_2 不应被动'
print('  [SC] boss_pc_2 未动 PASS')

print('fix_selfcheck_bug_n2 SELF-CHECK ALL PASS')
