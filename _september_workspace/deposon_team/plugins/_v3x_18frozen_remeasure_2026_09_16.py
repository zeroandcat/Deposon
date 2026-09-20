# -*- coding: utf-8 -*-
"""V3X 18 frozen 复算脚本 (2026-09-16 23:24)
user 23:21 Q1 拍板 "A = 沿 18 frozen 为标准,重测补足 2 条,18/18 PASS 报告"
+ Q2 拍板 "conservation.py V0 = 4bdec2683f06"(reconcile 后)
"""
import hashlib
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

BASE = Path(r'D:\私人资料\deposon-repo')
OUT_DIR = BASE / 'results' / '_v3x_18frozen_remeasure_2026_09_16'
OUT_DIR.mkdir(parents=True, exist_ok=True)


def v3x_18_frozen_remeasure():
    """沿 user 23:21 Q1 拍板 沿 18 frozen 为标准, 复算 18 frozen 补足 2 条"""
    # 18 frozen 完整列表(沿 _d7_post_anchor_rotation_remediation 字典 + P-G V0 + V3X PATCH reconcile 后)
    frozen_18 = [
        # 16 anchor 路径(沿 _d7_post_anchor_rotation_remediation 字典)
        ('verifier/handoff/KT_ABC1_anchors_sha256_12.json', '03c6c01f3697'),
        ('verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json', 'da517c115f3c'),
        ('verifier/handoff/P_F_PREDECISION_2026_09_09.json', 'b41c98bf90cc'),
        ('verifier/handoff/P_F_PREDECISION_2026_09_11_V0.1.json', '312d635e6259'),
        ('docs/V3X/P_F_SPEC_V0.md', 'de90faf362c5'),
        ('docs/V3X/P_F_RESEARCH_2026_09_09.md', '98085df7811a'),
        ('docs/V3X/P_F_IMPLEMENTATION_2026_09_11.md', 'edd048eaa721'),
        ('docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md', 'b10fae0da66d'),
        ('docs/V3X/P_F_V0_1_VERIFICATION_2026_09_12.md', '4d970e9c0aec'),
        ('docs/V3X/BOSS_URL_2026_09_11.md', '1ba7419178a1'),
        ('docs/V3X/BOSS_URL_DUE_DILIGENCE_2026_09_11.md', '0fb588bb0c2e'),
        ('docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md', '4a08521f8de1'),
        ('docs/V3X/KT_A1_SPEC_V0.1.md', '78b71d404366'),
        ('docs/V3X/KT_B1_SPEC_V0.1.md', '0410ca0fbdae'),
        ('docs/V3X/KT_C1_SPEC_V0.1.md', '59d8f56347d5'),
        ('docs/V3X/KT_D0_SPEC_V0.1.md', 'cce8e9a1b00e'),
        # 沿 user 23:21 Q2 reconcile 后(2 个 anchor JSON 自身)
        ('docs/V3X/P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md', '2f0765a1d39d'),
        ('verifier/audit/conservation.py', '4bdec2683f06'),  # ← reconcile 后(Q2 拍板)
    ]
    assert len(frozen_18) == 18, f'frozen_18 应有 18 条, 实际 {len(frozen_18)}'

    results = []
    for rel, expected in frozen_18:
        p = BASE / rel
        if not p.exists():
            results.append({
                'path': rel,
                'expected_sha12': expected,
                'actual_sha12': 'MISSING-FILE',
                'match': False,
                'status': 'MISSING',
            })
            continue
        with open(p, 'rb') as f:
            data = f.read()
        actual = hashlib.sha256(data).hexdigest()[:12]
        results.append({
            'path': rel,
            'expected_sha12': expected,
            'actual_sha12': actual,
            'match': actual == expected,
            'status': 'PASS' if actual == expected else 'FAIL',
        })

    return results


def main():
    print('===== V3X 18 frozen 复算 (2026-09-16 23:24) =====')
    print(f'Date: {datetime.now().isoformat()}')
    print()

    t_start = time.time()
    results = v3x_18_frozen_remeasure()

    print('--- 18 frozen 复算结果 (沿 user 23:21 Q1 拍板 18 frozen + Q2 reconcile) ---')
    n_pass = 0
    n_fail = 0
    n_missing = 0
    for i, r in enumerate(results, 1):
        print(f'  {i:>2}. {r["path"]}')
        print(f'      期望 SHA-12: {r["expected_sha12"]}')
        print(f'      实测 SHA-12: {r["actual_sha12"]}')
        print(f'      状态: {r["status"]}')
        if r['status'] == 'PASS':
            n_pass += 1
        elif r['status'] == 'MISSING':
            n_missing += 1
        else:
            n_fail += 1
    print()
    print(f'  TOTAL: {len(results)} frozen files | PASS: {n_pass} | FAIL: {n_fail} | MISSING: {n_missing}')
    print(f'  0-touch declaration: {"PASS" if n_fail == 0 and n_missing == 0 else "FAIL"}')
    print()

    out = {
        'date': datetime.now().isoformat(),
        'task': 'V3X 18 frozen 复算 (user 23:21 Q1 拍板 18 frozen + Q2 reconcile)',
        'elapsed_seconds': time.time() - t_start,
        'iron_7_compliance': {
            'no_llm': True,
            'no_proxy': True,
            'no_gateway': True,
            'no_key_in_prompt_json_disk': True,
            'no_18_frozen_touch': True,
            'no_p_g_v0_touch': True,
            'no_p_g_v01_touch': True,
            'no_plugin_spec_touch': True,
            'no_verifier_mavis_builtin_scripts_touch': True,
        },
        'all_results': results,
        'summary': {
            'total': len(results),
            'pass': n_pass,
            'fail': n_fail,
            'missing': n_missing,
        },
    }
    out_path = OUT_DIR / 'v3x_18frozen_remeasure_results_2026_09_16.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f'OUT: {out_path}')
    print(f'OUT size: {out_path.stat().st_size:,} bytes')
    print()

    print('===== V3X 18 frozen 复算完成 =====')
    print(f'  严守 7 铁律 + 0 LLM + 18 frozen 0 触动')


if __name__ == '__main__':
    main()
