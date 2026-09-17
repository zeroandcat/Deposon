# -*- coding: utf-8 -*-
"""
P-L v3 Phase 2 - Vector embedding stub
Real embeddings NOT computed (no endpoint available). This produces 4 stub JSONs documenting:
1. What cells/prompts would be embedded
2. Which embedding endpoint would be used
3. Why embeddings are missing (TeamoRouter DNS unreachable, OR text-embedding 403)
4. SHA-12 of cells source for downstream reproducibility
"""
import os, re, sys, json, hashlib
from pathlib import Path
from datetime import datetime, timezone, timedelta

CST = timezone(timedelta(hours=8))
TS = '20260917_142748'  # match other Phase 2 files
DEPOSON_ROOT = Path(r'D:\私人资料\deposon-repo')
RESULTS_DIR = DEPOSON_ROOT / 'results'

# Load baseline cells
BASELINE_JSON = RESULTS_DIR / 'deposon_volcengine_seed_code_30cells_2026_09_10.json'
baseline = json.loads(BASELINE_JSON.read_text(encoding='utf-8'))

cells_prompts = []
for c in baseline['cells']:
    cells_prompts.append({
        'cell_id': c['cell_id'],
        'task': c['task'],
        'prompt': f"Question: {c['question']}\nAnswer in one {('number' if c['task']=='gsm8k' else 'Yes or No')}:",
        'gold_answer': c['gold_answer'],
        'baseline_is_correct': c['is_correct'],
    })

# Probe results already exist
probe_emb_path = DEPOSON_ROOT / '_p_l_v3_phase2_probe_emb.log'

# 4 backbone × L=30 combinations (use whatever backbone JSON exists)
target_backbones = ['qwen3', 'glm53', 'mistral', 'doubao']

for bb in target_backbones:
    out_path = RESULTS_DIR / f'_p_l_v3_vector_embedding_{bb}_L30_{TS}.json'
    out = {
        'backbone': bb,
        'L': 30,
        'task': 'P-L v3 Phase 2 向量化扩展 (BGE-large-en-v1.5 或 text-embedding-3-large)',
        'status': 'INCOMPLETE - no embedding endpoint available',
        'embedding_endpoint_evaluation': {
            'BGE-large-en-v1.5': 'REJECTED - torch/transformers/sentence-transformers not installed in this environment',
            'openai/text-embedding-3-large via OpenRouter': 'REJECTED - 403 "The request is prohibited due to a violation of provider Terms of Service"',
            'openai/text-embedding-3-small via OpenRouter': 'REJECTED - 403 same as above',
            'TeamoRouter text-embedding-3-large': 'REJECTED - TeamoRouter DNS unreachable (api.teamo.io / api.teamorouter.ai / teamo.ai / teamo-router.ai / teamorouter.com / api.teamo-router.ai all getaddrinfo failed)',
            'volcengine doubao-embedding-vision-241215': 'NOT PROBED (no chat model available for embedding dim sanity)',
        },
        'cells_to_embed': cells_prompts,
        'cosine_similarity_matrix': None,  # No embeddings computed
        'cross_backbone_beta_ci': None,    # No embeddings means no cosine β CI
        'iron_7_compliance': {
            'no_llm_rehash': True,  # 0 LLM (no embedding calls attempted beyond probe)
            'no_proxy': True,
            'no_gateway': True,
            'no_key_in_prompt_json_disk': True,
            'no_18_frozen_touch': True,
            'no_p_g_v0_touch': True,
            'no_p_g_v01_touch': True,
            'no_plugin_spec_touch': True,
            'no_verifier_mavis_builtin_scripts_touch': True,
        },
        'probe_log_evidence': str(probe_emb_path) if probe_emb_path.exists() else None,
        '_meta': {
            'timestamp': datetime.now(CST).isoformat(),
            'phase': 'P-L v3 Phase 2',
            'baseline_json_sha256_12': hashlib.sha256(BASELINE_JSON.read_bytes()).hexdigest()[:12],
            'note': 'Stub JSON documenting missing embeddings. Downstream can populate by installing torch + sentence-transformers, or by using a non-OpenAI embedding endpoint.',
        },
    }
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"[SAVED] {out_path.name} size={out_path.stat().st_size}B")