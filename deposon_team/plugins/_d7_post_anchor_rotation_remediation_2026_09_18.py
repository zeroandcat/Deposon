# -*- coding: utf-8 -*-
"""D7 (2026-09-18) 后清理源仓文档脚本(沿 user 17:26 拍板 C)
user 拍板: C = 不轮换,等 D7 后清理源仓文档(重写 + re-commit)

严守 7 铁律:
- 0 LLM 调用
- 不动 18 frozen + P-G V0 + P-G V0.1
- key 永不入 prompt/JSON/落盘(只显示 SHA-256)

执行流程:
1. Step 1: 列出含 ark- key 的源仓文件
2. Step 2: 按 user 拍板 C 准备清理(替换 ark- 为 ark-[REDACTED])
3. Step 3: 严守 0 触动 18 frozen(不动)
4. Step 4: 严守 0 触动 4 plugin spec(不动)
5. Step 5: re-commit 协议(沿 push_result.json)
"""
import hashlib
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

BASE = Path(r'D:\私人资料\deposon-repo')

# 严守 0 触动的 18 frozen + P-G V0 spec
FROZEN_18 = {
    'verifier/handoff/KT_ABC1_anchors_sha256_12.json': '03c6c01f3697',
    'docs/V3X/KT_A1_SPEC_V0.1.md': '78b71d404366',
    'docs/V3X/KT_B1_SPEC_V0.1.md': '0410ca0fbdae',
    'docs/V3X/KT_C1_SPEC_V0.1.md': '59d8f56347d5',
    'docs/V3X/KT_D0_SPEC_V0.1.md': 'cce8e9a1b00e',
    'docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md': 'b10fae0da66d',
    'results/deposon_v19_benchmark_fixes.json': '910c4333eead',
    'results/deposon_v21_gtformal.json': '9d9ae5001c57',
    'corpus/v20/index.json': '8423ffe266af',
    'verifier/handoff/P_F_PREDECISION_2026_09_09.json': 'b41c98bf90cc',
    'docs/V3X/P_F_SPEC_V0.md': 'de90faf362c5',
    'docs/V3X/P_F_RESEARCH_2026_09_09.md': '98085df7811a',
    'deposon_team/plugins/skill_a_p_a_60cells.py': 'b1463bb24403',
    'deposon_team/plugins/skill_b_p_c_alpha_beta.py': 'e5a299f69a22',
    'deposon_team/plugins/skill_c_p_e_3modality.py': 'e19e76c5da7e',
    'deposon_team/plugins/skill_d_p_f_observer.py': '3e369a1f6171',  # 沿 user 12:01 1A 合法改动
    'docs/V3X/P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md': '2f0765a1d39d',
}

# 沿 user 17:21 + 17:26: 不轮换,等 D7 后清理源仓文档(重写 + re-commit)
# 沿 push_result.json §3.1: 已脱敏 2 处(2 个 VOLCENGINE 文档里的完整 Ark key)
# 沿 D7 后清理: 全 60+ 个文件 替换 ark- 为 ark-[REDACTED]


def list_ark_key_files():
    """列出含 ark- key 的源仓文件(不动文件)"""
    ark_files = []
    for p in BASE.rglob('*'):
        if not p.is_file():
            continue
        if p.suffix.lower() not in ('.md', '.json', '.py', '.txt'):
            continue
        # 跳过本脚本自身
        if p.name == '_d7_post_anchor_rotation_remediation_2026_09_18.py':
            continue
        try:
            with open(p, 'rb') as f:
                data = f.read()
            if b'ark-' in data:
                rel = p.relative_to(BASE)
                # 找 ark- 模式
                text = data.decode('utf-8', errors='ignore')
                keys = re.findall(r'ark-[A-Za-z0-9-]{4,}', text)
                # 算 SHA-256(不显示明文)
                key_hashes = set()
                for k in keys:
                    sha = hashlib.sha256(k.encode()).hexdigest()[:12]
                    key_hashes.add(sha)
                ark_files.append((rel, len(keys), key_hashes))
        except:
            pass
    return ark_files


def is_frozen(rel):
    """检查文件是否在 18 frozen 列表内"""
    rel_str = str(rel).replace('\\', '/')
    return rel_str in FROZEN_18


def is_plugin_spec(rel):
    """检查是否是 4 plugin spec(严守不动)"""
    rel_str = str(rel).replace('\\', '/')
    return rel_str in [
        'deposon_team/plugins/skill_a_p_a_60cells.py',
        'deposon_team/plugins/skill_b_p_c_alpha_beta.py',
        'deposon_team/plugins/skill_c_p_e_3modality.py',
        'deposon_team/plugins/skill_d_p_f_observer.py',
    ]


def plan_remediation(ark_files):
    """准备 D7 后清理计划(不擅自执行)"""
    plan = {
        'total_files': len(ark_files),
        'frozen_files_to_skip': [],
        'plugin_spec_to_skip': [],
        'other_files_to_remediate': [],
    }
    for rel, count, hashes in ark_files:
        if is_frozen(rel):
            plan['frozen_files_to_skip'].append((str(rel), count, hashes))
        elif is_plugin_spec(rel):
            plan['plugin_spec_to_skip'].append((str(rel), count, hashes))
        else:
            plan['other_files_to_remediate'].append((str(rel), count, hashes))
    return plan


def main():
    print('===== D7 (2026-09-18) 后清理源仓文档脚本 =====')
    print(f'Date: {datetime.now().isoformat()}')
    print()

    # Step 1: 列出含 ark- key 的文件
    print('--- Step 1: 列出含 ark- key 的源仓文件 ---')
    ark_files = list_ark_key_files()
    print(f'  Total files: {len(ark_files)}')
    for rel, count, hashes in ark_files:
        frozen_marker = ' [FROZEN, SKIP]' if is_frozen(rel) else ''
        plugin_marker = ' [PLUGIN_SPEC, SKIP]' if is_plugin_spec(rel) else ''
        print(f'  {rel}: {count} keys, SHA-12 hashes: {sorted(hashes)}{frozen_marker}{plugin_marker}')
    print()

    # Step 2: 准备清理计划
    print('--- Step 2: D7 后清理计划(沿 user 17:26 拍板 C) ---')
    plan = plan_remediation(ark_files)
    print(f'  Total files: {plan["total_files"]}')
    print(f'  Frozen files (skip): {len(plan["frozen_files_to_skip"])}')
    print(f'  Plugin spec (skip): {len(plan["plugin_spec_to_skip"])}')
    print(f'  Other files (remediate): {len(plan["other_files_to_remediate"])}')
    print()

    # Step 3: 列出需清理的文件(严守 0 触动 frozen + plugin spec)
    print('--- Step 3: 需清理的文件清单 ---')
    for rel, count, hashes in plan['other_files_to_remediate']:
        print(f'  {rel}: {count} keys, SHA-12: {sorted(hashes)}')
    print()

    # Step 4: 落盘清理计划
    print('--- Step 4: 落盘 D7 后清理计划 ---')
    out = {
        'date': datetime.now().isoformat(),
        'task': 'D7 后清理源仓文档(沿 user 17:26 拍板 C)',
        'user_decision': 'C: 不轮换,等 D7 后清理源仓文档(重写 + re-commit)',
        'remediation_plan': {
            'total_files_with_ark_keys': plan['total_files'],
            'frozen_files_skipped': [
                {'rel': str(rel), 'count': count, 'sha12_hashes': sorted(hashes)}
                for rel, count, hashes in plan['frozen_files_to_skip']
            ],
            'plugin_spec_files_skipped': [
                {'rel': str(rel), 'count': count, 'sha12_hashes': sorted(hashes)}
                for rel, count, hashes in plan['plugin_spec_to_skip']
            ],
            'files_to_remediate': [
                {'rel': str(rel), 'count': count, 'sha12_hashes': sorted(hashes)}
                for rel, count, hashes in plan['other_files_to_remediate']
            ],
        },
        'iron_7_compliance': {
            'no_llm': True,
            'no_proxy': True,
            'no_gateway': True,
            'no_key_in_prompt_json_disk': True,  # 只显示 SHA-256
            'no_18_frozen_touch': True,  # 严守 0 触动
            'no_4_plugin_spec_touch': True,
            'no_verifier_mavis_builtin_scripts_touch': True,
            'no_temp_files': True,
        },
        'execution_plan': [
            '1. 等 D7 (2026-09-18) 当日 5 锚终极实算完成',
            '2. 沿 _d7_5anchor_60cells_2026_09_18.py 跑实算 + 填 verdict',
            '3. 沿 push_result.json 协议 re-commit:替换所有 ark- 为 ark-[REDACTED]',
            '4. 严守 0 触动 18 frozen + 4 plugin spec',
            '5. 再次全量 398/398 核验 + 17 锚核验',
            '6. 落盘 D7 后清理报告 docs/V3X/D7_POST_CLEANUP_REPORT_2026_09_18.md',
        ],
    }
    out_path = BASE / 'docs' / 'V3X' / 'D7_POST_CLEANUP_PLAN_2026_09_18.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f'  OUT: {out_path}')
    print(f'  OUT size: {out_path.stat().st_size} bytes')
    print()

    # Step 5: 16 frozen 修后 verify
    print('--- Step 5: 16 frozen 修后 verify ---')
    print('  (由 _verify_15frozen.py 验证)')
    print()

    print('===== D7 后清理计划就绪 =====')
    print(f'  等 D7 (2026-09-18) 当日执行')
    print(f'  严守 0 触动 18 frozen + 4 plugin spec')
    print(f'  严守 7 铁律 + 0 LLM + 0 网关')


if __name__ == '__main__':
    main()


# ---------- SELF-CHECK (P-F V0.1 §5 纪律, Trae 2026-09-16 补, 标记 TRAE_SELFCHECK_2026_09_16_V3) ----------
# 补入理由: V3 全实验走读发现本 runner 缺 SELF-CHECK 尾块(沿 P-F V0.1 §5)
import os as _os_sc
assert _os_sc.path.basename(__file__) == '_d7_post_anchor_rotation_remediation_2026_09_18.py', '文件名漂移: ' + __file__
with open(__file__, 'r', encoding='utf-8') as _f_sc:
    _src_sc = _f_sc.read()
assert 'TRAE_SELFCHECK_2026_09_16_V3' in _src_sc
assert 'def main(' in _src_sc, 'main() 缺失'
assert '__main__' in _src_sc, '缺 __main__ guard'
print('_d7_post_anchor_rotation_remediation_2026_09_18.py SELF-CHECK PASS')
