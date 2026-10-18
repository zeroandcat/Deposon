# -*- coding: utf-8 -*-
# DECISION: option_A (N3: boss_pc_1/2/3 全文 BOSS-PE-N → BOSS-PC-N)
"""
fix_selfcheck_bug_n3_2026_09_15.py — N3 修补: INFILE_REPL 锚未全覆盖, BOSS-PE-N 残留清理

委托: LETTER_TO_TRAE_FIX_SELFCHECK_2026_09_15.md §3 (委托信 2026-09-15 15:30 落盘, 本修补执行 2026-09-16)
缺陷根因(Trae 自省): 上轮 INFILE_REPL 只替换带 `P-E ` 前缀的形态(`P-E BOSS-PE-1`)与文件名/run 函数名,
  漏了 4 类独立出现: docstring("升级实跑版 BOSS-PE-1")/ERROR 分支 boss_id/result boss_id/print 行
  → 每文件 4 处 × 3 = 12 处残留。
  且上轮 SC 断言写 `'P-E BOSS-PE-' not in s`(带前缀) → 对无前缀残留**抓不到**, 断言本身有洞。

方案裁定:
  option_A(全文 BOSS-PE-1/2/3 → BOSS-PC-1/2/3, 语义随文件名) = 采纳(沿委托信推荐)
  option_C(仅替换 boss_id 字段) = 留下 docstring/print 残留, 勘误不彻底 → 否决
  注: fix_*.py 补丁脚本自身的 'BOSS-PE-' 字符串是勘误历史档案(INFILE_REPL 定义/SC 断言/说明文本), 不改。

预注册判定线(计算前锁定):
  R1: 修后 3 个 boss_pc 文件全文 `BOSS-PE-` 零残留(断言用无前缀形态, 修上轮断言的洞)
  R2: 修后 3 文件 importlib 真执行无异常
  R3: **全量 12 尾块文件**(boss_pc 1/2/3 + attack_pc a1/a2/a3 + boss_pg 1/2/3 + boss_pa 1/2/3)
      import 真执行全 PASS(N1+N2+N3 修后总验证, 即委托信 "5/9 import FAIL → 9/9 PASS" 的超额口径)
  R4: 16 frozen 终验 0 触动; 幂等
"""
import os
import hashlib

BASE = r'D:\私人资料\deposon-repo'
PLUG = os.path.join(BASE, 'deposon_team', 'plugins')
N3_MAP = {
    'boss_pc_1_2d_ising_universality.py': ('BOSS-PE-1', 'BOSS-PC-1'),
    'boss_pc_2_transverse_field_ising.py': ('BOSS-PE-2', 'BOSS-PC-2'),
    'boss_pc_3_reservoir_computing.py': ('BOSS-PE-3', 'BOSS-PC-3'),
}
ALL12 = [
    'boss_pc_1_2d_ising_universality.py', 'boss_pc_2_transverse_field_ising.py', 'boss_pc_3_reservoir_computing.py',
    'attack_pc_a1_resampling.py', 'attack_pc_a2_fitting.py', 'attack_pc_a3_clipping.py',
    'boss_pg_1_riemannian_degenerate.py', 'boss_pg_2_hyperbolic_classification_collapse.py', 'boss_pg_3_geodesic_violation.py',
    'boss_pa_1_rbr_rm.py', 'boss_pa_2_potential_game.py', 'boss_pa_3_replicator_dynamics.py',
]
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


def rd(p):
    with open(p, 'r', encoding='utf-8') as f:
        return f.read()


def wr(p, s):
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)


def main():
    for fname, (old, new) in N3_MAP.items():
        p = os.path.join(PLUG, fname)
        s = rd(p)
        if old in s:
            n = s.count(old)
            s = s.replace(old, new)
            wr(p, s)
            print(f'  [N3] {fname}: {old} → {new} (×{n})')
        else:
            assert new in s, f'{fname}: 无旧串也无新串, 状态异常'
            print(f'  [N3] {fname}: 已修, 跳过')


# ---------- SELF-CHECK (import 级真执行 + 全量总验证) ----------
main()

import importlib.util

# R1: BOSS-PE- 零残留(无前缀形态, 修上轮断言的洞)
for fname in N3_MAP:
    s = rd(os.path.join(PLUG, fname))
    assert 'BOSS-PE-' not in s, f'{fname}: BOSS-PE- 残留'
    for _, new in [N3_MAP[fname]]:
        assert new in s, f'{fname}: {new} 缺失'
print('  [SC] 3 个 boss_pc 文件 BOSS-PE- 零残留 PASS')

# R3: 全量 12 尾块文件 import 真执行(N1/N2/N3 修后总验证)
for fname in ALL12:
    p = os.path.join(PLUG, fname)
    spec = importlib.util.spec_from_file_location(fname[:-3], p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # 尾块断言全部真跑, 任一失败即抛
    print(f'  [SC] import PASS: {fname}')
print('  [SC] 全量 12/12 尾块文件 import 真执行 PASS(委托信口径 9/9 的超额含 boss_pa)')

# R4: 16 frozen 终验
for rel, exp in FROZEN16:
    with open(os.path.join(BASE, rel), 'rb') as f:
        got = hashlib.sha256(f.read()).hexdigest()[:12]
    assert got == exp, f'frozen 触动: {rel} {exp} -> {got}'
print('  [SC] 16 frozen 终验 0 触动 PASS')

print('fix_selfcheck_bug_n3 SELF-CHECK ALL PASS')
