# -*- coding: utf-8 -*-
# DECISION: option_B (N1: 修正 _src_sc 定义顺序, 保留 TODO 断言而非删除)
"""
fix_selfcheck_bug_n1_2026_09_15.py — N1 修补: boss_pg_1/2/3 尾块 _src_sc use-before-def NameError

委托: LETTER_TO_TRAE_FIX_SELFCHECK_2026_09_15.md §1 (委托信 2026-09-15 15:30 落盘, 本修补执行 2026-09-16)
缺陷根因(Trae 自省, 透明记录):
  上轮 fix_boss_naming 的 footer 模板把 body_asserts 排在 `with open(...) _src_sc = ...` 之前,
  而 boss_pg 的 body_asserts 含 `assert 'TODO' in _src_sc` → use-before-def → import 即 NameError。
  上轮 SC 只做 compile()(语法级), 从未 import 执行 → "二跑 ALL PASS"对语法真、对执行假。
  本修补起, 尾块验证标准升级为 import 级真执行(本脚本 SC 即用 import)。

方案裁定:
  option_A(删除 _src_sc 引用) = 丢失 scaffolding TODO 锁定功能 → 否决
  option_B(修正定义顺序: TODO 断言移至 _src_sc 定义之后) = 保留全部断言语义 → 采纳
  (委托信推荐 A, 但沿其 option_C 自主权选 B, 理由如上)

预注册判定线(计算前锁定):
  R1: 修后 3 个 boss_pg 文件中, `assert 'TODO' in _src_sc` 行必须出现在 `_src_sc = _f_sc.read()` 之后
  R2: 修后 3 个 boss_pg 文件 importlib 真执行无异常(取代上轮 compile-only 假验证)
  R3: 不动 16 frozen + P-G V0 spec(2f0765a1d39d) + 其他 9 个 boss/attack 脚本
  R4: 幂等(重跑跳过)
"""
import os

BASE = r'D:\私人资料\deposon-repo'
PLUG = os.path.join(BASE, 'deposon_team', 'plugins')
PG_FILES = [
    'boss_pg_1_riemannian_degenerate.py',
    'boss_pg_2_hyperbolic_classification_collapse.py',
    'boss_pg_3_geodesic_violation.py',
]

BAD_LINE = "assert 'TODO' in _src_sc, 'SCAFFOLDING 真实逻辑标记丢失(应待拍板后实现)'"
GOOD_ANCHOR = "assert 'TRAE_SELFCHECK_2026_09_16' in _src_sc"
DEF_LINE = "    _src_sc = _f_sc.read()"


def rd(p):
    with open(p, 'r', encoding='utf-8') as f:
        return f.read()


def wr(p, s):
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)


def needs_fix(s):
    """坏模式 = BAD_LINE 出现在 _src_sc 定义之前"""
    if BAD_LINE not in s:
        return False
    return s.index(BAD_LINE) < s.index(DEF_LINE)


def main():
    for fname in PG_FILES:
        p = os.path.join(PLUG, fname)
        s = rd(p)
        if not needs_fix(s):
            print(f'  [N1] {fname}: 无 use-before-def, 跳过')
            continue
        assert GOOD_ANCHOR in s, f'{fname}: GOOD_ANCHOR 缺失'
        # 删除过早的 BAD_LINE(连同其行)
        s = s.replace(BAD_LINE + '\n', '', 1)
        # 在 GOOD_ANCHOR 之后补插(此时 _src_sc 已定义)
        s = s.replace(GOOD_ANCHOR, GOOD_ANCHOR + '\n' + BAD_LINE, 1)
        wr(p, s)
        print(f'  [N1] {fname}: TODO 断言已移至 _src_sc 定义后')


# ---------- SELF-CHECK (import 级真执行, 取代 compile-only) ----------
main()

import importlib.util

for fname in PG_FILES:
    p = os.path.join(PLUG, fname)
    s = rd(p)
    # R1: 顺序正确
    assert BAD_LINE in s and GOOD_ANCHOR in s and DEF_LINE in s, f'{fname}: 尾块关键行缺失'
    assert s.index(DEF_LINE) < s.index(BAD_LINE), f'{fname}: TODO 断言仍在定义前'
    assert not needs_fix(s), f'{fname}: needs_fix 应为 False'
    # R2: import 真执行(执行 module 顶层 + 尾块断言; __main__ guard 保证不触发 placeholder main)
    spec = importlib.util.spec_from_file_location(fname[:-3], p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # 任一断言失败即抛异常
    assert hasattr(mod, 'placeholder_check_' + {'boss_pg_1_riemannian_degenerate.py': 'riemannian_degenerate',
                                                'boss_pg_2_hyperbolic_classification_collapse.py': 'classification_collapse',
                                                'boss_pg_3_geodesic_violation.py': 'geodesic_violation'}[fname]), \
        f'{fname}: placeholder 函数缺失'
    print(f'  [SC] {fname}: 顺序修正 + import 真执行 PASS')

# R3: frozen 16 快核(本 patch 只碰 3 个 boss_pg, 快核 5 锚 + skill_d 足够; N3 脚本做全 16)
import hashlib
with open(os.path.join(BASE, 'verifier', 'handoff', 'KT_ABC1_anchors_sha256_12.json'), 'rb') as f:
    assert hashlib.sha256(f.read()).hexdigest()[:12] == '03c6c01f3697', '5 锚 JSON 被触动'
with open(os.path.join(BASE, 'docs', 'V3X', 'P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md'), 'rb') as f:
    assert hashlib.sha256(f.read()).hexdigest()[:12] == '2f0765a1d39d', 'P-G V0 spec 被触动'
print('  [SC] 5 锚 JSON + P-G V0 spec 0 触动 PASS')

print('fix_selfcheck_bug_n1 SELF-CHECK ALL PASS')
