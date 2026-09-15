import hashlib, os

# === FROZEN POLICY (2026-09-16, Trae, 修复点 6; DEPSON-TRAE-REVIEW-2026-09-16) ===
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
    ('deposon_team/plugins/skill_d_p_f_observer.py', '3e369a1f6171', 'plugin_d 15927B (D5 1A user 拍板 strict 阈值落 path_3, mtime 2026-09-15 13:30:57)'),
]

base = r'D:\私人资料\deposon-repo'
ok, fail = 0, 0
print('PATH'.ljust(70) + ' EXPECTED'.ljust(15) + ' OBSERVED'.ljust(15) + ' MATCH '.ljust(7) + 'NAME')
print('-' * 130)
for rel, expected, name in files_15:
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
print('TOTAL: {} frozen files | OK: {} | FAIL: {}'.format(len(files_15), ok, fail))
print('0-touch declaration: {}'.format('PASS' if fail == 0 else 'FAIL'))
print()
print('NEWLY LANDED: docs/V3X/LETTER_TO_TRAE_REVIEW_2026_09_16.md')
new_path = os.path.join(base, 'docs/V3X/LETTER_TO_TRAE_REVIEW_2026_09_16.md')
if os.path.exists(new_path):
    sz = os.path.getsize(new_path)
    with open(new_path, 'rb') as f:
        new_sha = hashlib.sha256(f.read()).hexdigest()[:12]
    print('  size: {} bytes'.format(sz))
    print('  SHA-12: {}'.format(new_sha))
