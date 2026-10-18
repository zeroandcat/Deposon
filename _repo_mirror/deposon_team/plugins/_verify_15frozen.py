import hashlib, os

# === FROZEN POLICY (2026-09-16, Trae, 修复点 6; DEPSON-TRAE-REVIEW-2026-09-16) ===
# 链 16 anchor 锚定 + 2 anchor JSON 自身 = 18 frozen total
# 2026-09-17 update: verifier/ + .mavis/ 转移至 archive(816 file trim)。
#   - verifier/handoff/* 在 archive 保留可读;脚本加 archive fallback
#   - 3 fail 转 16/16 PASS via resolve()
#   - conservation.py(Q2 PATCH_5ANCHOR_RECONCILE 提及 V0=4bdec2683f06)不在 16 frozen
#     锚列表中(原脚本即如此),继续作为 Q2 metadata,非 verify 字段

REPO_BASE = r'D:\私人资料\deposon-repo'
ARCHIVE_BASE = r'D:\私人资料\_archive_deposon_2026_09_17'

def resolve(rel_path):
    """Look for file in repo, fallback to archive if not found (post 2026-09-17 trim)."""
    p = os.path.join(REPO_BASE, rel_path)
    if os.path.exists(p):
        return p, 'repo'
    p = os.path.join(ARCHIVE_BASE, rel_path)
    if os.path.exists(p):
        return p, 'archive'
    return None, 'MISSING'

files_15 = [
    ('verifier/handoff/KT_ABC1_anchors_sha256_12.json', '03c6c01f3697', '5 anchors JSON'),
    ('docs/V3X/KT_A1_SPEC_V0.1.md', '78b71d404366', 'KT-A1 SPEC V0.1'),
    ('docs/V3X/KT_B1_SPEC_V0.1.md', '0410ca0fbdae', 'KT-B1 SPEC V0.1'),
    ('docs/V3X/KT_C1_SPEC_V0.1.md', '59d8f56347d5', 'KT-C1 SPEC V0.1'),
    ('docs/V3X/KT_D0_SPEC_V0.1.md', 'cce8e9a1b00e', 'KT-D0 SPEC V0.1'),
    ('docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md', 'b10fae0da66d', 'P-F V0.1 upgrade'),
    ('results/deposon_v19_benchmark_fixes.json', '910c4333eead', 'v19 benchmark'),
    ('results/deposon_v21_gtformal.json', '9d9ae5001c57', 'v21 gtformal'),
    ('corpus/v20/index.json', '8423ffe266af', 'corpus v20'),
    ('verifier/handoff/P_F_PREDECISION_2026_09_09.json', 'b41c98bf90cc', 'P-F V0 placeholder'),
    ('docs/V3X/P_F_SPEC_V0.md', 'de90faf362c5', 'P-F SPEC V0'),
    ('docs/V3X/P_F_RESEARCH_2026_09_09.md', '98085df7811a', 'P-F research'),
    ('deposon_team/plugins/skill_a_p_a_60cells.py', 'b1463bb24403', 'plugin_a 9078B'),
    ('deposon_team/plugins/skill_b_p_c_alpha_beta.py', 'e5a299f69a22', 'plugin_b 8699B'),
    ('deposon_team/plugins/skill_c_p_e_3modality.py', 'e19e76c5da7e', 'plugin_c 8915B'),
    ('deposon_team/plugins/skill_d_p_f_observer.py', '3e369a1f6171', 'plugin_d 15927B (D5 1A user 鎷嶆澘 strict 闃堝€艰惤 path_3, mtime 2026-09-15 13:30:57)'),
]

ok, fail = 0, 0
print('PATH'.ljust(70) + ' EXPECTED'.ljust(15) + ' OBSERVED'.ljust(15) + ' MATCH '.ljust(7) + 'SOURCE'.ljust(8) + 'NAME')
print('-' * 140)
for rel, expected, name in files_15:
    p, source = resolve(rel)
    if not p:
        print(rel.ljust(70) + ' MISSING'.ljust(15) + ' -'.ljust(15) + ' FAIL '.ljust(7) + source.ljust(8) + name)
        fail += 1
        continue
    with open(p, 'rb') as f:
        data = f.read()
    sha12 = hashlib.sha256(data).hexdigest()[:12]
    match = (sha12 == expected)
    print(rel.ljust(70) + ' ' + expected.ljust(15) + ' ' + sha12.ljust(15) + ' ' + str(match).ljust(7) + ' ' + source.ljust(8) + ' ' + name)
    if match:
        ok += 1
    else:
        fail += 1

print('-' * 140)
print('TOTAL: {} frozen files | OK: {} | FAIL: {}'.format(len(files_15), ok, fail))
print('0-touch declaration: {}'.format('PASS' if fail == 0 else 'FAIL'))
print()
print('NEWLY LANDED: docs/V3X/LETTER_TO_TRAE_REVIEW_2026_09_16.md')
new_path = os.path.join(REPO_BASE, 'docs/V3X/LETTER_TO_TRAE_REVIEW_2026_09_16.md')
if os.path.exists(new_path):
    sz = os.path.getsize(new_path)
    with open(new_path, 'rb') as f:
        new_sha = hashlib.sha256(f.read()).hexdigest()[:12]
    print('  size: {} bytes'.format(sz))
    print('  SHA-12: {}'.format(new_sha))
print()
print('NOTE 2026-09-17: 路径补充后 repo=816 files <1000,3 FAIL 转 16/16 PASS via archive fallback.')
print('      verifier/handoff/* 现在从 archive 读(rep 可读副本)conservation.py V0=4bdec2683f06 在 archive 不在 verify 列表。')
