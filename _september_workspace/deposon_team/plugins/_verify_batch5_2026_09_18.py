# -*- coding: utf-8 -*-
"""Trae 2026-09-18 验证 #5: 清理自身瑕疵 + 全量验证
1. 清理 _kimi_safe_batch_push_v3_full JSON 的多余尾部空行 (我 fix_batch4 的空 note 追加所致)
2. 验证所有改动 JSON 可解析
3. 验证所有改动 py 可 compile
4. frozen 0 触动复检
"""
import hashlib, json, os
from pathlib import Path

ROOT = Path(r'D:\私人资料\deposon-repo')

def sha12(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]

print('=== 1. 清理 v3_full JSON 尾部空行 (自身瑕疵) ===')
jp = ROOT / 'results' / '_kimi_safe_batch_push_v3_full_2026_09_17.json'
before = sha12(jp)
d = json.loads(jp.read_text(encoding='utf-8'))
jp.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'  {before} -> {sha12(jp)} (规范化重写, 内容不变)')

print()
print('=== 2. JSON 可解析验证 ===')
jsons = [
    'results/_kimi_safe_batch_push_v3_full_2026_09_17.json',
    'results/_kimi_push_v3_manifest_verifier21_cc3c92d0.json',
    'results/_d05_backbone_robustness_beta_20260918_100853.json',
    'results/_d05_i1i5_invariants_check_20260918_100853.json',
    'results/_d05_main_run_results_20260918_100853.json',
    'results/_d05_main_run_results_qwen3_failed_20260918_100853.json',
    'results/_d05_main_run_results_nemotron_3.5_20260918_100853.json',
    'results/_d05_opt_5_directions_results_20260918_100853.json',
]
for f in jsons:
    p = ROOT / f
    try:
        json.loads(p.read_text(encoding='utf-8'))
        print(f'  OK   {f}')
    except Exception as e:
        print(f'  FAIL {f}: {type(e).__name__}: {e}')

print()
print('=== 3. 改动 py compile 验证 ===')
pys = [
    'volcengine_glm_latest_30cells_v2_runner_2026_09_10.py',
    '_p_l_v3_phase1_runner_2026_09_17.py',
    '_p_l_v3_phase2_runner_2026_09_17.py',
    '_p_l_v3_phase2_glm53_only_2026_09_17.py',
    '_p_l_v3_phase2_closedsource_runner_2026_09_17.py',
    '_p_l_v3_phase2_closedsource_runner_v2_2026_09_17.py',
    '_p_l_v3_phase2_or_embedding_v3_2026_09_17.py',
    '_p_l_v3_phase2_or_embedding_2026_09_17.py',
    '_merge_or_stub_overlap_table_v3_2026_09_17.py',
    'deposon_agents.py',
    'deposon_team/plugins/_deposon_v2scripts_reverify_worker_2026_09_18.py',
    '_d05_verify_sha_2026_09_18.py',
]
okc = 0
for f in pys:
    p = ROOT / f
    try:
        compile(p.read_text(encoding='utf-8'), str(p), 'exec')
        print(f'  OK   {f}'); okc += 1
    except Exception as e:
        print(f'  FAIL {f}: {type(e).__name__}: {str(e)[:100]}')
print(f'  compile: {okc}/{len(pys)}')

print()
print('=== 4. frozen 0 触动复检 ===')
frozen = [
    ('verifier/handoff/KT_ABC1_anchors_sha256_12.json', '03c6c01f3697'),
    ('results/deposon_v19_benchmark_fixes.json', '910c4333eead'),
    ('results/deposon_v21_gtformal.json', '9d9ae5001c57'),
    ('corpus/v20/index.json', '8423ffe266af'),
    ('deposon_team/plugins/skill_a_p_a_60cells.py', 'b1463bb24403'),
    ('deposon_team/plugins/skill_b_p_c_alpha_beta.py', 'e5a299f69a22'),
    ('deposon_team/plugins/skill_c_p_e_3modality.py', 'e19e76c5da7e'),
    ('deposon_team/plugins/skill_d_p_f_observer.py', '3e369a1f6171'),
    ('deposon_team/plugins/_v3x_frozen_schema_v1.json', '9e99dcc4d920'),
    ('corpus/v20/by_model/KIMI/index_v2_2026_09_16.json', 'efe05ad775de'),
    ('corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json', '268ab1239a8a'),
    ('corpus/v20/by_model/GLM_2/glm_artifact_v_2026_09_16.json', '39732a92b5c9'),
    ('corpus/v20/by_model/coze/coze_artifact_v_2026_09_16.json', 'fee04170aa73'),
    ('corpus/v20/by_model/minimax/artifact_v_2026_09_16.json', '9e1ccbdceacc'),
    ('docs/V3X/KT_A1_SPEC_V0.1.md', '78b71d404366'),
    ('docs/V3X/KT_B1_SPEC_V0.1.md', '0410ca0fbdae'),
    ('docs/V3X/KT_C1_SPEC_V0.1.md', '59d8f56347d5'),
    ('docs/V3X/KT_D0_SPEC_V0.1.md', 'cce8e9a1b00e'),
]
fok = 0
for rel, exp in frozen:
    p = ROOT / rel
    if not p.exists():
        print(f'  MISSING {rel}'); continue
    got = sha12(p)
    if got == exp:
        fok += 1
    else:
        print(f'  DRIFT {rel}: {exp} -> {got}')
print(f'  frozen: {fok}/{len(frozen)} MATCH (0 触动)' + ('' if fok == len(frozen) else ' <-- 需检查!'))

print()
print('_verify_batch5_2026_09_18 DONE')
