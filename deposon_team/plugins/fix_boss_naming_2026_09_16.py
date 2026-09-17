# -*- coding: utf-8 -*-
# DECISION: option_C (修复点 1/5 命名; 修复点 7 SELF-CHECK 纪律)
"""
fix_boss_naming_2026_09_16.py — 修复点 1/5/7: BOSS/Attack 命名空间回正 + 9 脚本 SELF-CHECK 尾块

委托: LETTER_TO_TRAE_REVIEW_2026_09_16.md (DEPSON-TRAE-REVIEW-2026-09-16) §1/§5/§7
团队分工:
  - successor(Trae): 裁定 option_C —— 预注册(P_C_D1_D3_REPORT §4)回正, 双轴分离
  - reviewer-a(静态审): 命名/内容一致性; 历史 JSON 保留; 报告勘误追加式
  - reviewer-b(机械审): 脚本尾部 SELF-CHECK 断言块(任一失败不落盘); 幂等保护

判定线预注册(计算前锁定):
  R1: boss_pc_1/2/3 槽位 = 报告 §4 预注册的 2D Ising/transverse/reservoir BOSS(内容不变, 仅命名/框架回正)
  R2: KT-C1 SPEC V0.1 §5 抗攻击检查(非 BOSS)移出 boss_ 命名空间 → attack_pc_a1/a2/a3_*.py
  R3: 2026-09-15 D5 3A 已落盘的 6 个结果 JSON 一律保留为历史工件(旧名路径不动, 不重跑覆盖)
  R4: 9 个脚本(3 boss_pc + 3 attack_pc + 3 boss_pg scaffolding)追加 SELF-CHECK 尾块(P-F V0.1 §5 纪律)
  R5: 16 frozen 全 0 触动(本 patch 前后各核一次)

裁定依据(修复点 1/5 选 option_C 而非 A/B):
  - Mavis option A(把攻击脚本改名成 2D Ising 并改内容)会销毁已实跑的攻击实现 → 否决
  - Mavis option B(把报告 §4 改成攻击命名)会让预注册的 BOSS 槮适类自测失去文件槽位 → 否决
  - 实况: Ising 系实跑脚本已存在(被 D5 以 P-E 框架落盘为 boss_pe_*), 恰可回正到报告 §4 预注册名;
    攻击脚本是另一条轴(KT-C1 §5), 移出 boss_ 命名空间即两轴无冲突 —— 双实跑内容全保留
"""
import os
import hashlib

BASE = r'D:\私人资料\deposon-repo'
PLUG = os.path.join(BASE, 'deposon_team', 'plugins')

# ---------- 预注册: 改名映射 ----------
RENAMES = [
    ('boss_pe_1_2d_ising_universality.py', 'boss_pc_1_2d_ising_universality.py'),
    ('boss_pe_2_transverse_field_ising.py', 'boss_pc_2_transverse_field_ising.py'),
    ('boss_pe_3_reservoir_computing.py', 'boss_pc_3_reservoir_computing.py'),
    ('boss_pc_1_attack_a1_resampling.py', 'attack_pc_a1_resampling.py'),
    ('boss_pc_2_attack_a2_fitting.py', 'attack_pc_a2_fitting.py'),
    ('boss_pc_3_attack_a3_clipping.py', 'attack_pc_a3_clipping.py'),
]

# ---------- 预注册: 文件内字符串替换(勘误式, 保留 lineage) ----------
INFILE_REPL = {
    'boss_pc_1_2d_ising_universality.py': [
        ('boss_pe_1_2d_ising_universality.py', 'boss_pc_1_2d_ising_universality.py'),
        ('P-E BOSS-PE-1', 'P-C BOSS-PC-1'),
        ('P-E "3 modality conservation"', 'P-C 两相结构 (two-phase structure)'),
        ('boss_pe_1_real_2d_ising_2026_09_15.json', 'boss_pc_1_real_2d_ising_2026_09_15.json'),
        ('run_boss_pe_1', 'run_boss_pc_1'),
    ],
    'boss_pc_2_transverse_field_ising.py': [
        ('boss_pe_2_transverse_field_ising.py', 'boss_pc_2_transverse_field_ising.py'),
        ('P-E BOSS-PE-2', 'P-C BOSS-PC-2'),
        ('P-E "3 modality conservation"', 'P-C 两相结构 (two-phase structure)'),
        ('boss_pe_2_real_transverse_ising_2026_09_15.json', 'boss_pc_2_real_transverse_ising_2026_09_15.json'),
        ('run_boss_pe_2', 'run_boss_pc_2'),
    ],
    'boss_pc_3_reservoir_computing.py': [
        ('boss_pe_3_reservoir_computing.py', 'boss_pc_3_reservoir_computing.py'),
        ('P-E BOSS-PE-3', 'P-C BOSS-PC-3'),
        ('P-E "3 modality conservation"', 'P-C 两相结构 (two-phase structure)'),
        ('boss_pe_3_real_reservoir_2026_09_15.json', 'boss_pc_3_real_reservoir_2026_09_15.json'),
        ('run_boss_pe_3', 'run_boss_pc_3'),
    ],
    'attack_pc_a1_resampling.py': [
        ('boss_pc_1_attack_a1_resampling.py', 'attack_pc_a1_resampling.py'),
        ('P-C BOSS-PC-1 真实版', 'P-C 抗攻击检查 A1 真实版 (KT-C1 SPEC V0.1 §5 攻击轴, 非 BOSS; 2026-09-16 命名勘误移出 boss_ 命名空间)'),
        ('boss_pc_1_a1_resampling_2026_09_15.json', 'attack_pc_a1_resampling_2026_09_15.json'),
    ],
    'attack_pc_a2_fitting.py': [
        ('boss_pc_2_attack_a2_fitting.py', 'attack_pc_a2_fitting.py'),
        ('P-C BOSS-PC-2 真实版', 'P-C 抗攻击检查 A2 真实版 (KT-C1 SPEC V0.1 §5 攻击轴, 非 BOSS; 2026-09-16 命名勘误移出 boss_ 命名空间)'),
        ('boss_pc_2_a2_fitting_2026_09_15.json', 'attack_pc_a2_fitting_2026_09_15.json'),
    ],
    'attack_pc_a3_clipping.py': [
        ('boss_pc_3_attack_a3_clipping.py', 'attack_pc_a3_clipping.py'),
        ('P-C BOSS-PC-3 真实版', 'P-C 抗攻击检查 A3 真实版 (KT-C1 SPEC V0.1 §5 攻击轴, 非 BOSS; 2026-09-16 命名勘误移出 boss_ 命名空间)'),
        ('boss_pc_3_a3_clipping_2026_09_15.json', 'attack_pc_a3_clipping_2026_09_15.json'),
    ],
}

MARKER = 'TRAE_SELFCHECK_2026_09_16'


def footer(new_name, lineage, body_asserts, out_roundtrip):
    out = f'''

# ---------- SELF-CHECK (P-F V0.1 §5 纪律, Trae 2026-09-16 追加, 标记 {MARKER}) ----------
# 命名勘误 lineage: {lineage}
import os as _os_sc
assert _os_sc.path.basename(__file__) == '{new_name}', '文件名漂移: ' + __file__
{body_asserts}
with open(__file__, 'r', encoding='utf-8') as _f_sc:
    _src_sc = _f_sc.read()
assert '{MARKER}' in _src_sc
{out_roundtrip}
print('{new_name} SELF-CHECK PASS')
'''
    return out


FOOTERS = {
    'boss_pc_1_2d_ising_universality.py': footer(
        'boss_pc_1_2d_ising_universality.py',
        'boss_pe_1_2d_ising_universality.py → boss_pc_1_2d_ising_universality.py '
        '(沿 P_C_D1_D3_REPORT_2026_09_15.md §4.1 预注册回正 P-C 命名空间; D5 3A 实跑内容与 D5 1A D_fix2 方法保留; '
        '2026-09-15 D5 3A 历史结果保留于 results/boss_pe_1_real_2d_ising_2026_09_15.json)',
        "assert ISING_BETA_2D == 0.125, '2D Ising 临界指数预注册值被改动'\n"
        "assert BETA_TOLERANCE_STRICT < BETA_TOLERANCE_LOOSE\n"
        "assert D_FIX2_PASS_LT < D_FIX2_GRAY_GE <= D_FIX2_FAIL_GE\n"
        "assert D_FIX2_BASELINE_T_C == 0.8667 and D_FIX2_BASELINE_A_C == 0.0333",
        "if OUT.exists():\n    import json as _json_sc\n    _json_sc.loads(OUT.read_text(encoding='utf-8'))"),
    'boss_pc_2_transverse_field_ising.py': footer(
        'boss_pc_2_transverse_field_ising.py',
        'boss_pe_2_transverse_field_ising.py → boss_pc_2_transverse_field_ising.py '
        '(沿 P_C_D1_D3_REPORT §4.2 预注册回正; D5 3A 实跑 + D5 1A D_fix2 方法保留; '
        '历史结果保留于 results/boss_pe_2_real_transverse_ising_2026_09_15.json)',
        "assert PFEUTY_H_C_OVER_J == 1.0, 'Pfeuty 严格解预注册值被改动'\n"
        "assert TRANSVERSE_TOLERANCE_STRICT < TRANSVERSE_TOLERANCE_LOOSE\n"
        "assert D_FIX2_PASS_LT < D_FIX2_FAIL_GE\n"
        "assert D_FIX2_BASELINE_T_C == 0.8667 and D_FIX2_BASELINE_A_C == 0.0333",
        "if OUT.exists():\n    import json as _json_sc\n    _json_sc.loads(OUT.read_text(encoding='utf-8'))"),
    'boss_pc_3_reservoir_computing.py': footer(
        'boss_pc_3_reservoir_computing.py',
        'boss_pe_3_reservoir_computing.py → boss_pc_3_reservoir_computing.py '
        '(沿 P_C_D1_D3_REPORT §4.3 预注册回正; D5 3A 实跑 + D5 1A D_fix2 方法保留; '
        '历史结果保留于 results/boss_pe_3_real_reservoir_2026_09_15.json)',
        "assert SPEARMAN_TOLERANCE_STRICT < SPEARMAN_TOLERANCE_LOOSE\n"
        "assert D_FIX2_PASS_LT < D_FIX2_GRAY_GE <= D_FIX2_FAIL_GE",
        "if OUT.exists():\n    import json as _json_sc\n    _json_sc.loads(OUT.read_text(encoding='utf-8'))"),
    'attack_pc_a1_resampling.py': footer(
        'attack_pc_a1_resampling.py',
        'boss_pc_1_attack_a1_resampling.py → attack_pc_a1_resampling.py '
        '(KT-C1 SPEC V0.1 §5 抗攻击检查轴, 非 BOSS; 移出 boss_ 命名空间让位 §4 预注册 BOSS 槽位; '
        '历史结果保留于 results/boss_pc_1_a1_resampling_2026_09_15.json)',
        "assert A1_R2_CHANGE_THRESHOLD == 0.15, 'A1 预注册阈值被改动'\n"
        "assert N_RESAMPLE_TRIALS >= 3",
        "if OUT.exists():\n    import json as _json_sc\n    _json_sc.loads(OUT.read_text(encoding='utf-8'))"),
    'attack_pc_a2_fitting.py': footer(
        'attack_pc_a2_fitting.py',
        'boss_pc_2_attack_a2_fitting.py → attack_pc_a2_fitting.py '
        '(KT-C1 SPEC V0.1 §5 抗攻击检查轴; 历史结果保留于 results/boss_pc_2_a2_fitting_2026_09_15.json)',
        "assert EXP_FIT_R2_RATIO_THRESHOLD == 0.90, 'A2 预注册阈值被改动'",
        "if OUT.exists():\n    import json as _json_sc\n    _json_sc.loads(OUT.read_text(encoding='utf-8'))"),
    'attack_pc_a3_clipping.py': footer(
        'attack_pc_a3_clipping.py',
        'boss_pc_3_attack_a3_clipping.py → attack_pc_a3_clipping.py '
        '(KT-C1 SPEC V0.1 §5 抗攻击检查轴; 历史结果保留于 results/boss_pc_3_a3_clipping_2026_09_15.json)',
        "assert CLIP_R2_THRESHOLD == 0.7, 'A3 预注册阈值被改动'\n"
        "assert set(N_CLIPPED) < set(N_FULL) and len(N_CLIPPED) == len(N_FULL) - 2",
        "if OUT.exists():\n    import json as _json_sc\n    _json_sc.loads(OUT.read_text(encoding='utf-8'))"),
    'boss_pg_1_riemannian_degenerate.py': footer(
        'boss_pg_1_riemannian_degenerate.py',
        '命名不变; SCAFFOLDING 保持(修复点 4 option_A: 等 540-LLM 数据 + 王老师拍板后升实跑); '
        '本 SELF-CHECK 仅锁定预注册常数与 scaffolding 状态',
        "assert C_NEAR_EUCLIDEAN < C_TRUE_HYPERBOLIC\n"
        "assert DEGENERACY_DELTA_THRESHOLD_GRAY < DEGENERACY_DELTA_THRESHOLD_PASS\n"
        "assert POINCARE_BALL_EPSILON > 0\n"
        "assert 'TODO' in _src_sc, 'SCAFFOLDING 真实逻辑标记丢失(应待拍板后实现)'",
        "pass"),
    'boss_pg_2_hyperbolic_classification_collapse.py': footer(
        'boss_pg_2_hyperbolic_classification_collapse.py',
        '命名不变; SCAFFOLDING 保持(修复点 4 option_A); SELF-CHECK 锁定 scaffolding 状态',
        "assert 'TODO' in _src_sc, 'SCAFFOLDING 真实逻辑标记丢失(应待拍板后实现)'",
        "pass"),
    'boss_pg_3_geodesic_violation.py': footer(
        'boss_pg_3_geodesic_violation.py',
        '命名不变; SCAFFOLDING 保持(修复点 4 option_A); SELF-CHECK 锁定 scaffolding 状态',
        "assert 'TODO' in _src_sc, 'SCAFFOLDING 真实逻辑标记丢失(应待拍板后实现)'",
        "pass"),
}

REPORT = os.path.join(BASE, 'docs', 'V3X', 'P_C_D1_D3_REPORT_2026_09_15.md')
ERRATUM_MARKER = '勘误(2026-09-16, Trae, DEPSON-TRAE-REVIEW-2026-09-16 修复点 1/5)'
REPORT_ANCHOR = '**预检信号**: 已沿 risk3_decision.json 实算 Spearman(D_fix2, T_frac) = -0.832 → 待 D5 实算 Spearman(D_fix2, A_frac) 验证 BOSS-3 PASS/FAIL'
ERRATUM_BLOCK = '''

> **勘误(2026-09-16, Trae, DEPSON-TRAE-REVIEW-2026-09-16 修复点 1/5)**: D5 3A 实际落盘与本节预注册存在双重错位, 本日已按预注册回正:
> 1. 本节预注册的 3 个 BOSS 文件(boss_pc_1_2d_ising_universality.py / boss_pc_2_transverse_field_ising.py / boss_pc_3_reservoir_computing.py)曾以 P-E 框架落盘为 boss_pe_1/2/3 → 已改名回 boss_pc_1/2/3(内容为 D5 3A 实跑, D5 1A D_fix2 strict 方法保留; 2026-09-15 旧结果 JSON 保留于 results/boss_pe_*_2026_09_15.json 作历史工件, 新跑写 results/boss_pc_*_2026_09_15.json)
> 2. D5 同日落盘的 boss_pc_N_attack_a1/a2/a3 三脚本系 KT-C1 SPEC V0.1 §5 抗攻击检查轴(非 BOSS), 曾占用 boss_pc_N 编号槽位 → 已移出 boss_ 命名空间, 改名 attack_pc_a1/a2/a3_*.py
> 3. 自此 BOSS(普适类自测, boss_ 前缀)与 Attack(抗攻击检查, attack_ 前缀)为两条独立命名轴, 编号不再冲突; 全部 9 个脚本已追加 P-F V0.1 §5 SELF-CHECK 尾块(标记 TRAE_SELFCHECK_2026_09_16)'''

FROZEN16 = [
    ('verifier/handoff/KT_ABC1_anchors_sha256_12.json', '03c6c01f3697'),
    ('docs/V3X/KT_A1_SPEC_V0.1.md', '78b71d404366'),
    ('docs/V3X/KT_B1_SPEC_V0.1.md', '0410ca0fbdae'),
    ('docs/V3X/KT_C1_SPEC_V0.1.md', '59d8f56347d5'),
    ('docs/V3X/KT_D0_SPEC_V0.1.md', 'cce8e9a1b00e'),
    ('docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md', 'b10fae0da66d'),
    ('results/deposon_v19_benchmark_fixes.json', '910c4333eead'),
    ('results/deposon_v21_gtformal.json', '9d9ae5001c57'),
    ('corpus/v20/index.json', '8423ffe266af'),
    ('verifier/handoff/P_F_PREDECISION_2026_09_09.json', 'b41c98bf90cc'),
    ('docs/V3X/P_F_SPEC_V0.md', 'de90faf362c5'),
    ('docs/V3X/P_F_RESEARCH_2026_09_09.md', '98085df7811a'),
    ('deposon_team/plugins/skill_a_p_a_60cells.py', 'b1463bb24403'),
    ('deposon_team/plugins/skill_b_p_c_alpha_beta.py', 'e5a299f69a22'),
    ('deposon_team/plugins/skill_c_p_e_3modality.py', 'e19e76c5da7e'),
    ('deposon_team/plugins/skill_d_p_f_observer.py', '3e369a1f6171'),
]


def sha12_file(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def check_frozen16():
    bad = []
    for rel, exp in FROZEN16:
        got = sha12_file(os.path.join(BASE, rel))
        if got != exp:
            bad.append((rel, exp, got))
    return bad


def rd(p):
    with open(p, 'r', encoding='utf-8') as f:
        return f.read()


def wr(p, s):
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)


def main():
    # ---------- 幂等 ----------
    already = all(os.path.exists(os.path.join(PLUG, n)) and not os.path.exists(os.path.join(PLUG, o))
                  for o, n in RENAMES)
    if already:
        print('[fix_boss_naming] 幂等模式: 改名已完成, 仅复核')
    else:
        # 冻结前置检查(改名前)
        bad = check_frozen16()
        assert not bad, f'frozen 前置检查失败(不应发生): {bad}'

        # ---------- 改名 ----------
        for old, new in RENAMES:
            po, pn = os.path.join(PLUG, old), os.path.join(PLUG, new)
            assert os.path.exists(po), f'旧文件缺失: {old}'
            assert not os.path.exists(pn), f'新文件已存在(状态不一致): {new}'
            os.rename(po, pn)
            print(f'  rename: {old} -> {new}')

        # ---------- 文件内替换 ----------
        for new, repls in INFILE_REPL.items():
            p = os.path.join(PLUG, new)
            s = rd(p)
            for a, b in repls:
                if a in s:
                    s = s.replace(a, b)
                    print(f'  [{new}] 替换: {a[:44]}...')
            wr(p, s)

    # ---------- SELF-CHECK 尾块追加(幂等) ----------
    for name, foot in FOOTERS.items():
        p = os.path.join(PLUG, name)
        s = rd(p)
        if MARKER in s:
            continue
        if not s.endswith('\n'):
            s += '\n'
        s += foot
        wr(p, s)
        print(f'  SELF-CHECK append: {name}')

    # ---------- 报告勘误(幂等) ----------
    rep = rd(REPORT)
    if ERRATUM_MARKER not in rep:
        assert REPORT_ANCHOR in rep, '报告 §4.3 预检信号锚点未找到, 拒绝盲插'
        rep = rep.replace(REPORT_ANCHOR, REPORT_ANCHOR + ERRATUM_BLOCK, 1)
        wr(REPORT, rep)
        print('  报告 §4 勘误块已追加')
    else:
        print('  报告勘误已存在, 跳过')


# ---------- SELF-CHECK (reviewer-b 机械审, 任一失败抛异常) ----------
main()

for old, new in RENAMES:
    assert os.path.exists(os.path.join(PLUG, new)), f'缺新文件: {new}'
    assert not os.path.exists(os.path.join(PLUG, old)), f'旧文件残留: {old}'

# 1) 语法完整(builtin compile, 0 pyc 写入)
for name in list(FOOTERS.keys()):
    p = os.path.join(PLUG, name)
    compile(rd(p), p, 'exec')
print('  [SC] 9 文件 compile PASS (0 pyc)')

# 2) 命名空间回正证据
for i in (1, 2, 3):
    s = rd(os.path.join(PLUG, f'boss_pc_{i}_' + {1: '2d_ising_universality', 2: 'transverse_field_ising', 3: 'reservoir_computing'}[i] + '.py'))
    assert 'P-E BOSS-PE-' not in s, f'boss_pc_{i} 仍残留 P-E 命名空间'
    assert f'run_boss_pc_{i}' in s and f'run_boss_pe_{i}' not in s, f'boss_pc_{i} 函数名未回正'
    assert MARKER in s, f'boss_pc_{i} 缺 SELF-CHECK 尾块'
for a in ('a1_resampling', 'a2_fitting', 'a3_clipping'):
    s = rd(os.path.join(PLUG, f'attack_pc_{a}.py'))
    assert '真实版 (KT-C1 SPEC V0.1 §5 攻击轴' in s, f'attack_pc_{a} 缺攻击轴标注'
    assert MARKER in s, f'attack_pc_{a} 缺 SELF-CHECK 尾块'
for g in ('boss_pg_1_riemannian_degenerate', 'boss_pg_2_hyperbolic_classification_collapse', 'boss_pg_3_geodesic_violation'):
    s = rd(os.path.join(PLUG, g + '.py'))
    assert MARKER in s and 'TODO' in s, f'{g} scaffolding 状态或 SELF-CHECK 缺失'
print('  [SC] 命名空间回正 + 9 尾块 PASS')

# 3) 历史 JSON 保留(R3: 不覆盖 D5 3A 结果)
for old_res in ('boss_pe_1_real_2d_ising_2026_09_15.json', 'boss_pe_2_real_transverse_ising_2026_09_15.json',
                'boss_pe_3_real_reservoir_2026_09_15.json', 'boss_pc_1_a1_resampling_2026_09_15.json',
                'boss_pc_2_a2_fitting_2026_09_15.json', 'boss_pc_3_a3_clipping_2026_09_15.json'):
    assert os.path.exists(os.path.join(BASE, 'results', old_res)), f'历史结果 JSON 丢失: {old_res}'
print('  [SC] 6 个 D5 3A 历史 JSON 全保留')

# 4) 报告勘误存在
assert ERRATUM_MARKER in rd(REPORT), '报告勘误块缺失'
print('  [SC] P_C_D1_D3_REPORT §4 勘误块 PASS')

# 5) frozen 16 后置检查(0 触动)
bad = check_frozen16()
assert not bad, f'frozen 16 后置检查失败: {bad}'
print('  [SC] 16 frozen 后置 0 触动 PASS')

print('fix_boss_naming SELF-CHECK ALL PASS')
