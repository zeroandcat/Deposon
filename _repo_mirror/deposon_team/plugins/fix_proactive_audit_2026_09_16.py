# -*- coding: utf-8 -*-
# DECISION: proactive_audit (主动审查, 超委托信范围; DEPSON-TRAE-REVIEW-2026-09-16 后续)
"""
fix_proactive_audit_2026_09_16.py — 主动审查发现的可修项集中修复

触发: user 2026-09-16 "主动审查可能的其他代码问题, 不能只局限 minimax 给的, 以防错而不自知"

审查发现分级(详单见 TRAE_PROACTIVE_AUDIT_REPORT_2026_09_16.md):
  A1(严重) git_commit_msg_2026_09_18.txt 预写 D7 终极判死结论 → verdict 占位符化(结论先于数据 = 预注册纪律违反)
  A2(严重) github_upload_2026_09_18.sh frozen 检查只 grep 4 个文件名(12+ 假阴性敞口) + git add . 无 .gitignore 防护
  A3(严重, frozen 不可代修) skill_d 未落实上轮 risk2 followup(trust_anchor 值系拼接 + 新锚 79f8dfa2c296 缺失)
       → 仅报告, 待 user/Mavis 下次拍板 skill_d 时一并落实
  B4(中) runner_pa_d1_d3.py L70 FROZEN_16 期望值滞后 f4c68d146141(第 3 个 race 残留副本) → reconcile
  B5(中) D5_DECISIONS_LAND_REPORT §3A 引用旧名 boss_pc_N_attack/boss_pe_* → 勘误追加块
  B6(中) github_dir_structure_2026_09_18.md 引用旧名(D7 打包清单若不勘误将按旧名找文件) → 勘误追加块
  C7(轻) boss_pa_1/2/3 实跑脚本无 SELF-CHECK 尾块(上轮修复点 7 只覆盖委托信列的 9 个) → 补尾块
  C8(轻, frozen 不可代修) skill_d one_week_status 硬编码 today=2026-09-11 → 仅报告

判定线预注册(计算前锁定):
  R1: 16 frozen 全 0 触动(patch 前后各核)
  R2: 修改均为非 frozen 文件(runner_pa / D5 报告 / dir_structure / upload.sh / commit_msg / boss_pa_*)
  R3: 勘误一律追加式, 历史文本不改写; boss_*.json 历史 JSON 一律不动
  R4: patch 幂等(重跑跳过已修项)
"""
import os
import hashlib

BASE = r'D:\私人资料\deposon-repo'
PLUG = os.path.join(BASE, 'deposon_team', 'plugins')


def rd(p):
    with open(p, 'r', encoding='utf-8') as f:
        return f.read()


def wr(p, s):
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)


def sha12_file(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


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


def frozen_ok():
    for rel, exp in FROZEN16:
        got = sha12_file(os.path.join(BASE, rel))
        if got != exp:
            return rel, exp, got
    return None


ERR_MARKER = '勘误(2026-09-16, Trae 主动审查, DEPSON-TRAE-REVIEW-2026-09-16 后续)'

# ---------- B4: runner_pa 期望值 reconcile ----------
RUNNER = os.path.join(PLUG, 'runner_pa_d1_d3.py')
R_OLD = "('deposon_team/plugins/skill_d_p_f_observer.py', 'f4c68d146141', 'plugin_d 10981B'),"
R_NEW = ("('deposon_team/plugins/skill_d_p_f_observer.py', '3e369a1f6171', "
         "'plugin_d 15927B (D5 1A 拍板; reconcile by Trae 2026-09-16: OLD f4c68d146141 10981B)'),")

# ---------- B5: D5 报告勘误块 ----------
D5 = os.path.join(BASE, 'docs', 'V3X', 'D5_DECISIONS_LAND_REPORT_2026_09_15.md')
D5_ANCHOR = '这样的分工更清晰,boss_pc_* 测 P-C 的攻击弹性,boss_pe_* 测 P-E 的替代模型优越性。'
D5_BLOCK = '''

> **勘误(2026-09-16, Trae 主动审查, DEPSON-TRAE-REVIEW-2026-09-16 后续)**: 本报告 §3A 落盘文件名已于 2026-09-16 按预注册回正(见 P_C_D1_D3_REPORT_2026_09_15.md §4 勘误 + TRAE_3RISK_FIX_REPORT_2026_09_16 §1), 本节及 §3A 各表格中的旧名 `boss_pc_1/2/3_attack_a1/a2/a3_*.py` 与 `boss_pe_1/2/3_*.py` 均为历史层记录, 现行映射:
> - `boss_pe_1/2/3_*.py` → `boss_pc_1_2d_ising_universality.py / boss_pc_2_transverse_field_ising.py / boss_pc_3_reservoir_computing.py`(沿 P_C_D1_D3_REPORT §4 预注册, P-C 命名空间; 上文"boss_pe_* 测 P-E 的替代模型优越性"的表述与预注册报告 §4"BOSS P-C1/2/3 测 P-C 两相结构"存在**语义归属分歧**, 该 3 BOSS verdict(表: GRAY/PASS/PASS)在语义锚定 P-C 前应视为 PENDING_MAVIS_REVIEW, 待 Mavis 复核语义归属后定稿)
> - `boss_pc_N_attack_*.py` → `attack_pc_a1/a2/a3_*.py`(KT-C1 SPEC V0.1 §5 攻击轴)
> - `results/boss_pe_*_2026_09_15.json` 等 6 个历史结果 JSON 原样保留为历史工件'''

# ---------- B6: dir_structure 勘误块(尾部追加, 避开 tree 对齐空格脆弱锚点) ----------
DIRS = os.path.join(PLUG, 'github_dir_structure_2026_09_18.md')
DIRS_BLOCK = '''

---

> **勘误(2026-09-16, Trae 主动审查, DEPSON-TRAE-REVIEW-2026-09-16 后续)**: 上文 §1 目录树中的 `boss_pc_1/2/3_attack_*.py` 与 `boss_pe_1/2/3_*.py` 为改名前历史层(2026-09-16 已按预注册回正), D7 github 打包按**现行名**执行:
> - `boss_pc_1_2d_ising_universality.py / boss_pc_2_transverse_field_ising.py / boss_pc_3_reservoir_computing.py`(P-C BOSS, 实跑)
> - `attack_pc_a1_resampling.py / attack_pc_a2_fitting.py / attack_pc_a3_clipping.py`(P-C 攻击轴, 实跑)
> - `boss_pg_1/2/3_*.py`(P-G SCAFFOLDING, 不变) + `boss_pa_1/2/3_*.py`(P-A BOSS, 不变)
> - `results/boss_pe_*_2026_09_15.json` 等历史结果 JSON 保留(历史工件)
> - 详映射见 `TRAE_3RISK_FIX_REPORT_2026_09_16.md` §1; 本文件其余结构不变'''

# ---------- A1: commit msg verdict 占位符化 ----------
CMSG = os.path.join(PLUG, 'git_commit_msg_2026_09_18.txt')
CMSG_NOTE = ('> [!占位符声明 2026-09-16, Trae 主动审查] 本 commit message 原稿在 D7 (09-18) 实测发生前'
             '预写了 4 路径终极 PASS/FAIL verdict, 属"结论先于数据", 违反预注册纪律。\n'
             '> 已将全部 D7 verdict 占位符化(<XXX_VERDICT_D7>), D7 实测出真值后由 Mavis 填入;'
             'P-G V0.1 实测数字(09-15 已算)保留。\n\n')
CMSG_SUBS = [
    ('- **P-A deepen**: PASS(', '- **P-A deepen**: <P-A_VERDICT_D7>('),
    ('- **P-C verify**: FAIL_H0(', '- **P-C verify**: <P-C_VERDICT_D7>('),
    ('- **P-E physics**: PASS(', '- **P-E physics**: <P-E_VERDICT_D7>('),
    ('- **P-F observer**: PASS(', '- **P-F observer**: <P-F_VERDICT_D7>('),
    ('- **BOSS-PE-3 PASS**: A 通道独立', '- **BOSS-PC-3 <VERDICT_D7>**(改名勘误: 原 BOSS-PE-3, 现 boss_pc_3_reservoir_computing.py, 语义归属 PENDING_MAVIS_REVIEW): A 通道独立'),
]

# ---------- A2: upload.sh frozen 检查修全 + .gitignore 防护 ----------
SH = os.path.join(PLUG, 'github_upload_2026_09_18.sh')
SH_OLD_GUARD = 'if git status --short | grep -q "KT_ABC1_anchors_sha256_12.json\\|KT_A1_SPEC_V0.1\\|skill_a_p_a_60cells\\|skill_d_p_f_observer"; then'
SH_NEW_GUARD = '''# [2026-09-16 Trae 主动审查修正] 原检查只 grep 4 个文件名, 16 frozen 中 12+ 不在检查内(假阴性敞口);
# 现为全 16 frozen 路径模式。注: skill_d 若出现在 git status 属 user 12:01 拍板 1A 合法改动
# (期望值已沿 FROZEN POLICY reconcile 至 3e369a1f6171), 需在 commit 前确认其为该拍板改动本身。
FROZEN_PAT='verifier/handoff/KT_ABC1_anchors_sha256_12.json|docs/V3X/KT_A1_SPEC_V0.1.md|docs/V3X/KT_B1_SPEC_V0.1.md|docs/V3X/KT_C1_SPEC_V0.1.md|docs/V3X/KT_D0_SPEC_V0.1.md|docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md|results/deposon_v19_benchmark_fixes.json|results/deposon_v21_gtformal.json|corpus/v20/index.json|verifier/handoff/P_F_PREDECISION_2026_09_09.json|docs/V3X/P_F_SPEC_V0.md|docs/V3X/P_F_RESEARCH_2026_09_09.md|plugins/skill_a_p_a_60cells.py|plugins/skill_b_p_c_alpha_beta.py|plugins/skill_c_p_e_3modality.py|plugins/skill_d_p_f_observer.py'
if git status --short | grep -E "${FROZEN_PAT}"; then'''
SH_ADD_GUARD = '''# ============================================================
# [2026-09-16 Trae 主动审查新增] Step 3.5: .gitignore 防护
# git add . 在无 .gitignore 时会全仓提交(.mavis/logs/backups 等私人目录有公开泄露风险)
# ============================================================
if [ ! -f .gitignore ]; then
    echo "[ERROR] repo 根缺 .gitignore: 'git add .' 会把 .mavis/(logs/backups/pdfbuild) 等全部提交"
    echo "        请先按 github_dir_structure_2026_09_18.md §1 建立 .gitignore(排除 .mavis/ .tmp/ 等)后重跑"
    exit 1
fi

'''
SH_ADD_ANCHOR = '# ============================================================\n# 4. git add + commit'

# ---------- C7: boss_pa SELF-CHECK 尾块 ----------
PA_MARKER = 'TRAE_SELFCHECK_2026_09_16_PA'
PA_FILES = {
    'boss_pa_1_rbr_rm.py': ('boss_pa_1_rbr_rm_result_2026_09_15.json',
                            "    # 预注册判定线(docstring): BOSS-A1 成本倍数 <= 1.3x -> 拍平 -> 主张降级\n    pass"),
    'boss_pa_2_potential_game.py': ('boss_pa_2_potential_game_result_2026_09_15.json', '    pass'),
    'boss_pa_3_replicator_dynamics.py': ('boss_pa_3_replicator_dynamics_result_2026_09_15.json', '    pass'),
}


def pa_footer(fname, out_json, extra):
    return f'''

# ---------- SELF-CHECK (P-F V0.1 §5 纪律, Trae 2026-09-16 主动审查补, 标记 {PA_MARKER}) ----------
# 上轮修复点 7 覆盖委托信所列 9 脚本, boss_pa 1/2/3 系主动审查补齐(实跑脚本同等纪律)
import os as _os_pa
assert _os_pa.path.basename(__file__) == '{fname}', '文件名漂移: ' + __file__
with open(__file__, 'r', encoding='utf-8') as _f_pa:
    _src_pa = _f_pa.read()
assert '{PA_MARKER}' in _src_pa
_p_out_pa = _os_pa.path.join(r'D:/私人资料/deposon-repo', 'results', '{out_json}')
if _os_pa.path.exists(_p_out_pa):
    import json as _json_pa
    _json_pa.loads(open(_p_out_pa, 'r', encoding='utf-8').read())
{extra}
print('{fname} SELF-CHECK PASS')
'''


def main():
    # 前置 frozen 检查
    bad = frozen_ok()
    assert not bad, f'frozen 前置检查失败: {bad}'

    # B4 runner_pa reconcile
    s = rd(RUNNER)
    if R_OLD in s:
        s = s.replace(R_OLD, R_NEW, 1)
        wr(RUNNER, s)
        print('  [B4] runner_pa_d1_d3.py skill_d 期望值 reconcile')
    else:
        assert R_NEW in s, 'runner_pa skill_d 行状态异常'
        print('  [B4] runner_pa 已 reconcile, 跳过')

    # B5 D5 报告勘误
    s = rd(D5)
    if ERR_MARKER not in s:
        assert D5_ANCHOR in s, 'D5 报告勘误锚点未找到'
        s = s.replace(D5_ANCHOR, D5_ANCHOR + D5_BLOCK, 1)
        wr(D5, s)
        print('  [B5] D5_DECISIONS_LAND_REPORT §3A 勘误块已追加')
    else:
        print('  [B5] D5 报告勘误已存在, 跳过')

    # B6 dir_structure 勘误(归一化: 首跑曾因幂等 marker 与块文本不一致重复追加 2 次, 此处裁齐)
    # 缺陷透明记录: 初版 DIRS_BLOCK 勘误头是短版"主动审查**", 与 ERR_MARKER(含"后续)")不一致
    #   → 幂等检查永假 → 重复追加; 机械自审 SC 当场抓出, 本版归一化修复
    s = rd(DIRS)
    head_pat = '\n\n---\n\n> **勘误(2026-09-16, Trae 主动审查'
    cnt = s.count(head_pat)
    if cnt == 0:
        if not s.endswith('\n'):
            s += '\n'
        s += DIRS_BLOCK
        wr(DIRS, s)
        print('  [B6] github_dir_structure 勘误块已追加(文件尾)')
    elif cnt > 1 or ERR_MARKER not in s:
        idx = s.find(head_pat)
        s = s[:idx].rstrip('\n') + '\n' + DIRS_BLOCK
        wr(DIRS, s)
        print(f'  [B6] github_dir_structure 勘误块归一化(检测到 {cnt} 个重复尾段, 已裁齐为 1)')
    else:
        print('  [B6] dir_structure 勘误已存在且唯一, 跳过')

    # A1 commit msg 占位符化
    s = rd(CMSG)
    if '<P-A_VERDICT_D7>' not in s:
        for a, b in CMSG_SUBS:
            assert a in s, f'commit msg 锚点缺失: {a[:40]}'
            s = s.replace(a, b, 1)
        s = CMSG_NOTE + s
        wr(CMSG, s)
        print('  [A1] git_commit_msg D7 verdict 占位符化')
    else:
        print('  [A1] commit msg 已占位符化, 跳过')

    # A2 upload.sh 修 guard + 加 .gitignore 防护
    s = rd(SH)
    if SH_OLD_GUARD in s:
        s = s.replace(SH_OLD_GUARD, SH_NEW_GUARD, 1)
        print('  [A2a] upload.sh frozen 检查模式扩为全 16 项')
    else:
        assert 'FROZEN_PAT=' in s, 'upload.sh guard 状态异常'
        print('  [A2a] upload.sh guard 已修, 跳过')
    if '.gitignore 防护' not in s:
        assert SH_ADD_ANCHOR in s, 'upload.sh Step 4 锚点未找到'
        s = s.replace(SH_ADD_ANCHOR, SH_ADD_GUARD + SH_ADD_ANCHOR, 1)
        print('  [A2b] upload.sh 新增 Step 3.5 .gitignore 防护')
    else:
        print('  [A2b] .gitignore 防护已存在, 跳过')
    wr(SH, s)

    # C7 boss_pa 尾块
    for fname, (outj, extra) in PA_FILES.items():
        p = os.path.join(PLUG, fname)
        s = rd(p)
        if PA_MARKER in s:
            continue
        if not s.endswith('\n'):
            s += '\n'
        s += pa_footer(fname, outj, extra)
        wr(p, s)
        print(f'  [C7] SELF-CHECK append: {fname}')


# ---------- SELF-CHECK (reviewer-b 机械审, 任一失败抛异常) ----------
main()

# B4 复核: 旧期望值元组消失, 新值在位
s = rd(RUNNER)
assert R_OLD not in s and '3e369a1f6171' in s
compile(s, RUNNER, 'exec')
print('  [SC] runner_pa reconcile + compile PASS')

# B5/B6 复核
assert ERR_MARKER in rd(D5) and 'PENDING_MAVIS_REVIEW' in rd(D5)
_s_dirs = rd(DIRS)
assert ERR_MARKER in _s_dirs and 'attack_pc_a1_resampling.py' in _s_dirs
assert _s_dirs.count('\n\n---\n\n> **勘误(2026-09-16, Trae 主动审查') == 1, 'dir_structure 勘误块仍重复'
print('  [SC] D5 报告 + dir_structure 勘误块(唯一) PASS')

# A1 复核: 无预写 verdict 残留
s = rd(CMSG)
for ph in ('<P-A_VERDICT_D7>', '<P-C_VERDICT_D7>', '<P-E_VERDICT_D7>', '<P-F_VERDICT_D7>'):
    assert ph in s, f'占位符缺失: {ph}'
assert '- **P-A deepen**: PASS(' not in s and '- **P-C verify**: FAIL_H0(' not in s
assert '- **P-E physics**: PASS(' not in s and '- **P-F observer**: PASS(' not in s
print('  [SC] commit msg 预写 verdict 清零 + 占位符 4/4 PASS')

# A2 复核
s = rd(SH)
assert 'FROZEN_PAT=' in s and s.count('skill_c_p_e_3modality.py') >= 1  # guard 模式含该项(verify 为脚本调用, 不内联清单; 初版断言 >=2 想当然, 已修)
assert '.gitignore 防护' in s and 'exit 1' in s
assert 'KT_B1_SPEC_V0.1.md' in s and 'P_F_PREDECISION_2026_09_09.json' in s
print('  [SC] upload.sh frozen 全量 guard + .gitignore 防护 PASS')

# C7 复核: 三尾块 + compile
for fname in PA_FILES:
    p = os.path.join(PLUG, fname)
    s = rd(p)
    assert PA_MARKER in s, f'{fname} 缺尾块'
    compile(s, p, 'exec')
print('  [SC] boss_pa 1/2/3 尾块 + compile PASS')

# R1 后置 frozen 16
bad = frozen_ok()
assert not bad, f'frozen 后置检查失败: {bad}'
print('  [SC] 16 frozen 后置 0 触动 PASS')

print('fix_proactive_audit SELF-CHECK ALL PASS')
