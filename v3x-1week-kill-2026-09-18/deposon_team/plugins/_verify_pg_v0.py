import hashlib, os

# 1) 16 frozen verify (沿 _verify_15frozen.py 同款 16 项)
frozen_16 = [
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
    ('deposon_team/plugins/skill_d_p_f_observer.py', '3e369a1f6171', 'plugin_d 15927B (D5 1A user 拍板 2026-09-15 12:01, reconcile by Trae 2026-09-16: OLD f4c68d146141 10981B -> NEW 3e369a1f6171 15927B)'),
]

base = r'D:\私人资料\deposon-repo'
ok, fail = 0, 0
print('16 frozen files verify:')
print('PATH'.ljust(70) + ' EXPECTED'.ljust(15) + ' OBSERVED'.ljust(15) + ' MATCH '.ljust(7) + 'NAME')
print('-' * 130)
for rel, expected, name in frozen_16:
    p = os.path.join(base, rel)
    if not os.path.exists(p):
        print(rel.ljust(70) + ' MISSING'.ljust(15) + ' -'.ljust(15) + ' FAIL '.ljust(7) + name)
        fail += 1
        continue
    with open(p, 'rb') as f:
        data = f.read()
    sha12 = hashlib.sha256(data).hexdigest()[:12]
    match = (sha12 == expected)
    print(rel.ljust(70) + ' ' + expected.ljust(15) + ' ' + sha12.ljust(15) + ' ' + str(match).ljust(7) + ' ' + name)
    if match:
        ok += 1
    else:
        fail += 1

print('-' * 130)
print('16 frozen TOTAL: OK: {} | FAIL: {}'.format(ok, fail))
print('0-touch declaration: {}'.format('PASS' if fail == 0 else 'FAIL'))
print()

# 2) P-G V0 spec 自身 SHA-12 实算
pg_path = os.path.join(base, 'docs/V3X/P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md')
print('P-G V0 spec (新落盘):')
print('  path:', pg_path)
print('  size:', os.path.getsize(pg_path), 'bytes')
with open(pg_path, 'rb') as f:
    pg_data = f.read()
pg_sha12 = hashlib.sha256(pg_data).hexdigest()[:12]
pg_sha256 = hashlib.sha256(pg_data).hexdigest()
print('  SHA-12:', pg_sha12)
print('  SHA-256 full:', pg_sha256)
print()

# 3) 5 锚预注册占位 SHA-12 实算 (沿 R3 erratum: 算法定义 + 算法不变 → 占位可复算)
pg_anchors = [
    ('P_G_HYPERBOLIC_TRANSPORT', '230b5caee415'),
    ('P_G_CURVATURE_BOUND', 'dcbcf2b8d45f'),
    ('P_G_LLM_CLIENT', '2c1f572aa2bf'),
    ('P_G_HARNESS', '8b90c53f1e01'),
    ('P_G_FROZEN_BENCHMARK', '91db66afecc3'),
]
print('P-G 5 锚预注册 SHA-12 占位 (沿 R3 erratum 算法):')
print('ANCHOR_ID'.ljust(35) + ' PLACEHOLDER SHA-12'.ljust(20) + ' RECOMPUTED'.ljust(15) + ' MATCH')
print('-' * 80)
for anchor_id, placeholder in pg_anchors:
    # 沿 §2 预注册 SHA-12 生成算法
    seed = 'P_G_V0_PLACEHOLDER_{}_2026_09_15'.format(anchor_id).encode()
    recomputed = hashlib.sha256(seed).hexdigest()[:12]
    match = (recomputed == placeholder)
    print(anchor_id.ljust(35) + ' ' + placeholder.ljust(20) + ' ' + recomputed.ljust(15) + ' ' + str(match))
print()
print('注: P-G V0 spec §2 表格中填写的 5 锚 SHA-12 是 Mavis 在 spec 落盘前手填的占位,')
print('    沿 R3 erratum 要求: 占位 SHA-12 必须可由算法独立复算 → 本 verify 给出 recomputed 公式')
print('    若手填占位 != recomputed, 则 spec 需修正(目前手填是手算生成,非算法生成)')