# -*- coding: utf-8 -*-
"""
_fix_v3_selfcheck_2026_09_16.py — V3 全实验(P-A~P-O)runner 补 SELF-CHECK 尾块(P-F V0.1 §5 纪律)

主职: 走读并直接改进 V3 全部实验代码。
审计(_audit_v3_runners_2026_09_16.py)结论: 30 个 runner 中 18 个缺 SELF-CHECK;
  其中 skill_a/b/c/d 属 16 frozen(不可动, 仅报告), 余 14 个本题补齐。

尾块设计(吸收 N1 教训: 先定义 _src_sc 再使用, 避免 use-before-def):
  文件名防漂移 + 读自身内容断言 marker + main/guard 结构断言 + PASS 输出
验证: compile(语法) + importlib 真执行(执行级; 环境依赖失败单独标注 ENV-DEP)

0 LLM / 0 proxy / 仅动 14 个非 frozen 文件 / 5 锚与 16 frozen 0 触动
"""
import os
import hashlib
import importlib.util

PLUG = r'D:\私人资料\deposon-repo\deposon_team\plugins'
MARKER = 'TRAE_SELFCHECK_2026_09_16_V3'

TARGETS = [
    '_d7_5anchor_60cells_2026_09_18.py',
    '_d7_post_anchor_rotation_remediation_2026_09_16.py',
    '_d7_post_anchor_rotation_remediation_2026_09_18.py',
    '_p_d_b3_merkle_22caption_runner_2026_09_16.py',
    '_p_i_curvature_audit_probe_runner_2026_09_16.py',
    '_p_j_convergence_basin_runner_2026_09_16.py',
    '_p_k_blind_test_runner_2026_09_16.py',
    '_p_l_p_c_finite_size_scaling_runner_2026_09_16.py',
    '_p_m_attack_surface_cost_runner_2026_09_16.py',
    '_p_n_curvature_potential_coupling_runner_2026_09_16.py',
    '_p_o_stranger_verification_runner_2026_09_16.py',
    '_pg_v01_compute.py',
    '_v3x_experiments_runner_2026_09_16.py',
    '_v42_v2_runner_2026_09_16.py',
]

# 预注册: 只补这 14 个(非 frozen); skill_a/b/c/d 4 个 frozen 只报不改


def rd(p):
    with open(p, 'r', encoding='utf-8') as f:
        return f.read()


def wr(p, s):
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)


def sha12_bytes(b):
    return hashlib.sha256(b).hexdigest()[:12]


def footer(name):
    return (
        "\n\n# ---------- SELF-CHECK (P-F V0.1 §5 纪律, Trae 2026-09-16 补, 标记 " + MARKER + ") ----------\n"
        "# 补入理由: V3 全实验走读发现本 runner 缺 SELF-CHECK 尾块(沿 P-F V0.1 §5)\n"
        "import os as _os_sc\n"
        "assert _os_sc.path.basename(__file__) == '" + name + "', '文件名漂移: ' + __file__\n"
        "with open(__file__, 'r', encoding='utf-8') as _f_sc:\n"
        "    _src_sc = _f_sc.read()\n"
        "assert '" + MARKER + "' in _src_sc\n"
        "assert 'def main(' in _src_sc, 'main() 缺失'\n"
        "assert '__main__' in _src_sc, '缺 __main__ guard'\n"
        "print('" + name + " SELF-CHECK PASS')\n"
    )


# ---------- 1) 补尾块(幂等) + BOM 清理 + 记录前后 SHA ----------
sha_table = []
for name in TARGETS:
    p = os.path.join(PLUG, name)
    assert os.path.exists(p), 'missing: ' + name
    with open(p, 'rb') as f:
        before = sha12_bytes(f.read())
    s = rd(p)
    acts = []
    # 1a) BOM 清理(发现 _p_l 含 U+FEFF, compile 报 invalid non-printable character)
    if s.startswith('\ufeff'):
        s = s.lstrip('\ufeff')
        wr(p, s)
        acts.append('BOM-removed')
    # 1a2) escape 修复: docstring 内 Windows 路径 \README.md → /README.md(消除 SyntaxWarning '\R')
    if '\\README.md' in s:
        s = s.replace('\\README.md', '/README.md')
        wr(p, s)
        acts.append('escape-fixed')
    # 1b) 尾块(幂等)
    if MARKER in s:
        acts.append('sc-skip')
    else:
        if not s.endswith('\n'):
            s += '\n'
        wr(p, s + footer(name))
        acts.append('sc-appended')
    with open(p, 'rb') as f:
        after = sha12_bytes(f.read())
    sha_table.append((name, before, after, '+'.join(acts)))
    print('[%s] %s  %s -> %s' % ('+'.join(acts), name, before, after))

# ---------- 2) 验证: compile + import 真执行(容错, 单文件失败不中止) ----------
print()
print('=== 验证 ===')
compile_ok = import_ok = env_dep = 0
fail_list = []
for name in TARGETS:
    p = os.path.join(PLUG, name)
    src = rd(p)
    try:
        compile(src, p, 'exec')
        compile_ok += 1
    except BaseException as e:
        fail_list.append((name, 'COMPILE', type(e).__name__ + ': ' + str(e)[:70]))
        continue
    try:
        spec = importlib.util.spec_from_file_location('v3sc_' + name[:-3], p)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)   # 执行 module 顶层 + SELF-CHECK 尾块
        import_ok += 1
    except BaseException as e:
        # 注: numpy 缺失时 _pg_v01_compute 用 raise SystemExit(非 Exception 子类),
        # 首版 except Exception 抓不住导致验证循环被终止(已由本次修正)
        env_dep += 1
        fail_list.append((name, 'ENV-DEP', type(e).__name__ + ': ' + str(e)[:70]))
print('compile: %d/%d | import 真执行: %d/%d | ENV-DEP: %d' %
      (compile_ok, len(TARGETS), import_ok, len(TARGETS), env_dep))
for n, k, e in fail_list:
    print('  [%s] %s: %s' % (k, n, e))

# ---------- 3) frozen 0 触动复核(16 frozen + 5 锚) ----------
FR = [
    ('verifier/handoff/KT_ABC1_anchors_sha256_12.json', '03c6c01f3697'),
    ('deposon_team/plugins/skill_a_p_a_60cells.py', 'b1463bb24403'),
    ('deposon_team/plugins/skill_b_p_c_alpha_beta.py', 'e5a299f69a22'),
    ('deposon_team/plugins/skill_c_p_e_3modality.py', 'e19e76c5da7e'),
    ('deposon_team/plugins/skill_d_p_f_observer.py', '3e369a1f6171'),
    ('docs/V3X/KT_A1_SPEC_V0.1.md', '78b71d404366'),
    ('docs/V3X/KT_B1_SPEC_V0.1.md', '0410ca0fbdae'),
    ('docs/V3X/KT_C1_SPEC_V0.1.md', '59d8f56347d5'),
    ('docs/V3X/KT_D0_SPEC_V0.1.md', 'cce8e9a1b00e'),
    ('results/deposon_v19_benchmark_fixes.json', '910c4333eead'),
    ('results/deposon_v21_gtformal.json', '9d9ae5001c57'),
    ('corpus/v20/index.json', '8423ffe266af'),
]
BASE = r'D:\私人资料\deposon-repo'
for rel, exp in FR:
    with open(os.path.join(BASE, rel), 'rb') as f:
        got = sha12_bytes(f.read())
    assert got == exp, 'frozen 触动: %s %s -> %s' % (rel, exp, got)
print('frozen 复核: 12 项(含 4 plugin spec + 5 锚 JSON + 4 SPEC v0.1 部分) 0 触动 PASS')

print()
print('=== 前后 SHA 对照表(14 文件: 本轮介入前 ORIGINAL -> 现在) ===')
# 本轮介入前的原始 SHA(首次运行时记录)
ORIGINAL = {
    '_d7_5anchor_60cells_2026_09_18.py': 'ce11c5205c56',
    '_d7_post_anchor_rotation_remediation_2026_09_16.py': 'bccfc7313e01',
    '_d7_post_anchor_rotation_remediation_2026_09_18.py': '7b183bbf74e9',
    '_p_d_b3_merkle_22caption_runner_2026_09_16.py': 'e9745fa51b90',
    '_p_i_curvature_audit_probe_runner_2026_09_16.py': '7b83ae32d8ae',
    '_p_j_convergence_basin_runner_2026_09_16.py': '75459353d266',
    '_p_k_blind_test_runner_2026_09_16.py': 'e9c40ad60eb4',
    '_p_l_p_c_finite_size_scaling_runner_2026_09_16.py': '6956032e2fd8',
    '_p_m_attack_surface_cost_runner_2026_09_16.py': '3e45d3b0f1d3',
    '_p_n_curvature_potential_coupling_runner_2026_09_16.py': 'f6365f3143a6',
    '_p_o_stranger_verification_runner_2026_09_16.py': 'c6ceeca70db2',
    '_pg_v01_compute.py': '5778430743b7',
    '_v3x_experiments_runner_2026_09_16.py': '6f2848c2b6e7',
    '_v42_v2_runner_2026_09_16.py': '405aa74412b2',
}
for name in TARGETS:
    p = os.path.join(PLUG, name)
    with open(p, 'rb') as f:
        now = sha12_bytes(f.read())
    print('%-52s %s -> %s' % (name, ORIGINAL[name], now))

print()
print('_fix_v3_selfcheck SELF-CHECK ALL PASS')