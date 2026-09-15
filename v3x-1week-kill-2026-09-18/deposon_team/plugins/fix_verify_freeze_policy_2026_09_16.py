# -*- coding: utf-8 -*-
# DECISION: option_A (修复点 3 派生 JSON 读取顺序; 修复点 6 动态冻结政策; 修复点 2 race reconcile)
"""
fix_verify_freeze_policy_2026_09_16.py — 修复点 2/3/6: verify 脚本 reconcile + 冻结政策注释

委托: LETTER_TO_TRAE_REVIEW_2026_09_16.md §2/§3/§6
裁定:
  - 修复点 3 = option_A: 派生 JSON (KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json) 保持独立,
    下游读 P_A_LLM_CLIENT / P_A_HARNESS 时先查派生 JSON(value_v3x_new), fallback 5 锚 JSON 旧值;
    D7 后 5 锚 JSON V0.2/V3X 正式升级时统一 reconcile(沿派生 JSON 自带 metadata.note)
    —— option B 否决: 任何"保持 03c6c01f3697 的同时改 5 锚 JSON 内容"在 SHA 语义上不可能(SHA 变更即指纹变更)
  - 修复点 2 = race reconcile: _verify_pg_v0.py 的 skill_d 期望值仍是旧 f4c68d146141(Mavis 只更新了
    _verify_15frozen.py), 即信中 BOSS-PE-3 worker 观察到的 "1/15 frozen FAIL" 实证 → 本 patch reconcile
  - 修复点 6 = 动态冻结政策: frozen 契约 = "不得未经拍板修改"; user 拍板的合法改动由 verifier 按协议
    reconcile(OLD→NEW 审计痕迹留在条目 name 字段), 并修 "TOTAL: 15" 标签 bug(实为 16 项)
"""
import hashlib

BASE = r'D:\私人资料\deposon-repo'
V15 = BASE + r'\deposon_team\plugins\_verify_15frozen.py'
VPG = BASE + r'\deposon_team\plugins\_verify_pg_v0.py'

POLICY_MARKER = '=== FROZEN POLICY (2026-09-16, Trae'
POLICY_BLOCK = '''# === FROZEN POLICY (2026-09-16, Trae, 修复点 6; DEPSON-TRAE-REVIEW-2026-09-16) ===
# 本列表是"动态冻结"(dynamic freeze with reconcile protocol):
#   - frozen 契约 = "不得未经拍板修改文件"; 未经授权的 SHA 漂移 = FAIL(0 触动声明破)
#   - user 拍板的合法改动(如 skill_d 2026-09-15 12:01 拍板 1A, OLD f4c68d146141 → NEW 3e369a1f6171)
#     由 verifier 按协议 reconcile:
#       1) 改动须有 user 拍板记录(时间 + 拍板编号 + 改动摘要)
#       2) 期望值 OLD → NEW, 并在本条目 name 字段保留 OLD→NEW 审计痕迹
#       3) reconcile 后其余条目仍须全 PASS(不允许"顺手"改其他期望值)
#   - P-A 锚派生补丁读取顺序(修复点 3, option_A): 下游读 P_A_LLM_CLIENT / P_A_HARNESS 时
#     先查派生 JSON verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json
#     (value_v3x_new: 1722500da4aa / 275e480ba4d9), fallback 5 锚 JSON 旧值(055e874ea5c1 / 9f383935c00c);
#     待 D7 后 5 锚 JSON V0.2/V3X 正式升级统一 reconcile(沿派生 JSON metadata.note)
# ============================================================

'''

OLD_SKILLD_PG = "('deposon_team/plugins/skill_d_p_f_observer.py', 'f4c68d146141', 'plugin_d 10981B')"
NEW_SKILLD_PG = ("('deposon_team/plugins/skill_d_p_f_observer.py', '3e369a1f6171', "
                 "'plugin_d 15927B (D5 1A user 拍板 2026-09-15 12:01, reconcile by Trae 2026-09-16: "
                 "OLD f4c68d146141 10981B -> NEW 3e369a1f6171 15927B)')")


def rd(p):
    with open(p, 'r', encoding='utf-8') as f:
        return f.read()


def wr(p, s):
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)


def main():
    # ---------- _verify_15frozen.py: 政策注释(幂等) ----------
    s15 = rd(V15)
    if POLICY_MARKER not in s15:
        anchor = 'files_15 = ['
        assert anchor in s15, '_verify_15frozen.py 缺 files_15 锚点'
        s15 = s15.replace(anchor, POLICY_BLOCK + anchor, 1)
        print('  _verify_15frozen.py: FROZEN POLICY 注释已插入')
    else:
        print('  _verify_15frozen.py: 政策注释已存在, 跳过')

    # 标签 bug: "TOTAL: 15 frozen files" 实为 16 项 → 动态 len()
    if 'TOTAL: 15 frozen files' in s15:
        s15 = s15.replace(
            "print('TOTAL: 15 frozen files | OK: {} | FAIL: {}'.format(ok, fail))",
            "print('TOTAL: {} frozen files | OK: {} | FAIL: {}'.format(len(files_15), ok, fail))", 1)
        print('  _verify_15frozen.py: TOTAL 标签 15 → len(files_15) 修正')
    # NEWLY LANDED 指针刷新到本次委托信
    if 'TRAE_FIX_REQUEST_3RISKS_2026_09_11.md' in s15:
        s15 = s15.replace('TRAE_FIX_REQUEST_3RISKS_2026_09_11.md', 'LETTER_TO_TRAE_REVIEW_2026_09_16.md')
        print('  _verify_15frozen.py: NEWLY LANDED 指针刷新为 2026-09-16 委托信')
    wr(V15, s15)

    # ---------- _verify_pg_v0.py: skill_d 期望值 reconcile(幂等) ----------
    spg = rd(VPG)
    if OLD_SKILLD_PG in spg:
        assert NEW_SKILLD_PG not in spg
        spg = spg.replace(OLD_SKILLD_PG, NEW_SKILLD_PG, 1)
        wr(VPG, spg)
        print('  _verify_pg_v0.py: skill_d 期望值 reconcile (f4c68d146141 -> 3e369a1f6171)')
    else:
        assert NEW_SKILLD_PG in spg, '_verify_pg_v0.py skill_d 行状态异常(既无旧值也无新值)'
        print('  _verify_pg_v0.py: skill_d 已 reconcile, 跳过')


# ---------- SELF-CHECK (reviewer-b 机械审, 任一失败抛异常) ----------
main()

s15 = rd(V15)
spg = rd(VPG)
compile(s15, V15, 'exec')  # 语法完整, 0 pyc
compile(spg, VPG, 'exec')
assert POLICY_MARKER in s15, '政策注释缺失'
# 注意: 审计痕迹(NEW_SKILLD_PG 的 name 字段)合法包含旧值字符串 f4c68d146141,
# 故断言对象是"旧期望值元组"而非旧值字符串本身(初版断言自相矛盾, 2026-09-16 首跑实算抓出后修正)
assert OLD_SKILLD_PG not in spg, '_verify_pg_v0.py 仍残留旧期望值元组'
assert '3e369a1f6171' in spg and '3e369a1f6171' in s15, '新期望值缺失'
assert 'TOTAL: 15 frozen files' not in s15, '标签 bug 未修'
assert 'LETTER_TO_TRAE_REVIEW_2026_09_16.md' in s15, 'NEWLY LANDED 指针未刷新'
assert "len(files_15), ok, fail" in s15, '动态 TOTAL 未生效'
# frozen 16 本 patch 0 触动复核(嵌入式独立复算, 不信脚本自报)
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
import os
for rel, exp in FROZEN16:
    with open(os.path.join(BASE, rel), 'rb') as f:
        got = hashlib.sha256(f.read()).hexdigest()[:12]
    assert got == exp, f'frozen 触动: {rel} {exp} -> {got}'
print('  [SC] 16 frozen 嵌入式复核 0 触动 PASS')

print('fix_verify_freeze_policy SELF-CHECK ALL PASS')
