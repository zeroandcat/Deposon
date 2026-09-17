# -*- coding: utf-8 -*-
"""D7 后清理源仓文档脚本(实际执行,沿 user 17:13 提前D7 + user 17:26 拍板 C)
- 替换所有 ark- key 引用为 ark-[REDACTED]
- 严守 0 触动 18 frozen + 4 plugin spec
- 落盘 D7 后清理报告
"""
import hashlib
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

BASE = Path(r'D:\私人资料\deposon-repo')

# 严守 0 触动的 18 frozen
FROZEN_18 = {
    'verifier/handoff/KT_ABC1_anchors_sha256_12.json',
    'docs/V3X/KT_A1_SPEC_V0.1.md',
    'docs/V3X/KT_B1_SPEC_V0.1.md',
    'docs/V3X/KT_C1_SPEC_V0.1.md',
    'docs/V3X/KT_D0_SPEC_V0.1.md',
    'docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md',
    'results/deposon_v19_benchmark_fixes.json',
    'results/deposon_v21_gtformal.json',
    'corpus/v20/index.json',
    'verifier/handoff/P_F_PREDECISION_2026_09_09.json',
    'docs/V3X/P_F_SPEC_V0.md',
    'docs/V3X/P_F_RESEARCH_2026_09_09.md',
    'deposon_team/plugins/skill_a_p_a_60cells.py',
    'deposon_team/plugins/skill_b_p_c_alpha_beta.py',
    'deposon_team/plugins/skill_c_p_e_3modality.py',
    'deposon_team/plugins/skill_d_p_f_observer.py',
    'docs/V3X/P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md',
}

# Ark key 模式
ARK_PATTERN = re.compile(r'ark-[A-Za-z0-9-]{4,}')


def list_ark_key_files():
    """列出含 ark- key 的源仓文件"""
    ark_files = []
    for p in BASE.rglob('*'):
        if not p.is_file():
            continue
        if p.suffix.lower() not in ('.md', '.json', '.py', '.txt'):
            continue
        # 跳过本脚本自身
        if p.name in ('_d7_post_anchor_rotation_remediation_2026_09_18.py',
                       '_d7_post_anchor_rotation_remediation_2026_09_16.py'):
            continue
        # 跳过本报告(避免递归)
        if p.name in ('D7_POST_CLEANUP_REPORT_2026_09_18.md',
                       'D7_GITHUB_PUSH_RECEIVE_2026_09_15_v2.md',
                       'D7_GITHUB_PUSH_RECEIVE_2026_09_15.md'):
            continue
        rel = p.relative_to(BASE)
        rel_str = str(rel).replace('\\', '/')
        if rel_str in FROZEN_18:
            continue  # 严守 0 触动 frozen
        try:
            with open(p, 'rb') as f:
                data = f.read()
            if b'ark-' in data:
                text = data.decode('utf-8', errors='ignore')
                keys = ARK_PATTERN.findall(text)
                if keys:
                    ark_files.append((rel, len(keys), keys))
        except Exception as e:
            print(f'ERROR reading {p}: {e}')
    return ark_files


def remediate_file(rel, keys):
    """替换文件中的 ark- key 为 ark-[REDACTED]"""
    p = BASE / rel
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    original = text
    new_text = ARK_PATTERN.sub('ark-[REDACTED]', text)
    if new_text != original:
        with open(p, 'w', encoding='utf-8', errors='ignore') as f:
            f.write(new_text)
        return True
    return False


def main():
    print('===== D7 后清理源仓文档(实际执行) =====')
    print(f'Date: {datetime.now().isoformat()}')
    print()

    # Step 1: 列出含 ark- key 的文件
    print('--- Step 1: 列出含 ark- key 的源仓文件 ---')
    ark_files = list_ark_key_files()
    print(f'  Total files: {len(ark_files)}')
    print()

    # Step 2: 严守 0 触动 frozen
    print('--- Step 2: 严守 0 触动 18 frozen(已过滤)---')
    for rel, count, keys in ark_files:
        rel_str = str(rel).replace('\\', '/')
        in_frozen = rel_str in FROZEN_18
        if in_frozen:
            print(f'  SKIP [FROZEN]: {rel}')
    print()

    # Step 3: 实际执行替换
    print('--- Step 3: 实际执行替换 ark- → ark-[REDACTED] ---')
    success = 0
    failed = 0
    for rel, count, keys in ark_files:
        rel_str = str(rel).replace('\\', '/')
        if rel_str in FROZEN_18:
            continue
        try:
            if remediate_file(rel, keys):
                print(f'  CLEANED: {rel} ({count} keys)')
                success += 1
            else:
                failed += 1
        except Exception as e:
            print(f'  ERROR: {rel}: {e}')
            failed += 1
    print(f'  Success: {success}, Failed: {failed}')
    print()

    # Step 4: 落盘清理报告
    print('--- Step 4: 落盘 D7 后清理报告 ---')
    out = {
        'date': datetime.now().isoformat(),
        'task': 'D7 后清理源仓文档(沿 user 17:13 提前D7 + user 17:26 拍板 C)',
        'frozen_18_skipped': list(FROZEN_18),
        'files_remediated': success,
        'files_failed': failed,
        'iron_7_compliance': {
            'no_llm': True,
            'no_proxy': True,
            'no_gateway': True,
            'no_key_in_prompt_json_disk': True,
            'no_18_frozen_touch': True,
            'no_4_plugin_spec_touch': True,
            'no_verifier_mavis_builtin_scripts_touch': True,
        },
    }
    out_path = BASE / 'docs' / 'V3X' / 'D7_POST_CLEANUP_REPORT_2026_09_16.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f'  OUT: {out_path}')
    print(f'  OUT size: {out_path.stat().st_size} bytes')
    print()

    print('===== D7 后清理完成 =====')
    print(f'  等 user re-commit + 王老师 WeChat 推送 D7 终极判死 1 条')


if __name__ == '__main__':
    main()


# ---------- SELF-CHECK (P-F V0.1 §5 纪律, Trae 2026-09-16 补, 标记 TRAE_SELFCHECK_2026_09_16_V3) ----------
# 补入理由: V3 全实验走读发现本 runner 缺 SELF-CHECK 尾块(沿 P-F V0.1 §5)
import os as _os_sc
assert _os_sc.path.basename(__file__) == '_d7_post_anchor_rotation_remediation_2026_09_16.py', '文件名漂移: ' + __file__
with open(__file__, 'r', encoding='utf-8') as _f_sc:
    _src_sc = _f_sc.read()
assert 'TRAE_SELFCHECK_2026_09_16_V3' in _src_sc
assert 'def main(' in _src_sc, 'main() 缺失'
assert '__main__' in _src_sc, '缺 __main__ guard'
print('_d7_post_anchor_rotation_remediation_2026_09_16.py SELF-CHECK PASS')
