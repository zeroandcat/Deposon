# -*- coding: utf-8 -*-
"""
V3X Stage 3 Final Consolidation
- Use partial data from the minimal run
- Be honest about timeouts
"""
import io, os, re, sys, json
from datetime import datetime, timezone, timedelta

# Hardcoded results from the minimal run (gsm8k_1-10)
# gsm8k_1-6 from main run (max_tokens=2048), gsm8k_7-10 from minimal run (max_tokens=1024)
PARTIAL_RESULTS = [
    # cell_id, task, gold, extracted, is_correct, latency_ms, status, top1_caption, top1_sim, top2_caption, top2_sim, top3_caption, top3_sim, source
    ('gsm8k_1', 'gsm8k', 18.0, 18.0, True, 13729, 200, 'S2', 0.998, '', 0, '', 0, 'main_run'),
    ('gsm8k_2', 'gsm8k', 5.0, 5.0, True, 4065, 200, 'S2', 0.994, '', 0, '', 0, 'main_run'),
    ('gsm8k_3', 'gsm8k', 40.0, 40.0, True, 14398, 200, 'L_historical_causality', 0.998, '', 0, '', 0, 'main_run'),
    ('gsm8k_4', 'gsm8k', 1430.0, 1430.0, True, 6209, 200, 'S6_n20', 1.000, '', 0, '', 0, 'main_run'),
    ('gsm8k_5', 'gsm8k', 36.0, 36.0, True, 5566, 200, 'S1_n35', 0.999, '', 0, '', 0, 'main_run'),
    ('gsm8k_6', 'gsm8k', 8000.0, 8000.0, True, 4585, 200, 'S2', 0.998, '', 0, '', 0, 'main_run'),
    ('gsm8k_7', 'gsm8k', 36.0, None, False, 60023, 0, 'S2', 1.000, '', 0, '', 0, 'minimal_timeout_60s'),
    ('gsm8k_8', 'gsm8k', 6.0, 6.0, True, 14541, 200, 'L_historical_causality', 0.995, '', 0, '', 0, 'minimal'),
    ('gsm8k_9', 'gsm8k', 40.0, 40.0, True, 10889, 200, 'S2', 0.999, '', 0, '', 0, 'minimal'),
    ('gsm8k_10', 'gsm8k', 140.0, None, False, 60033, 0, 'S2', 0.999, '', 0, '', 0, 'minimal_timeout_60s'),
]

# Load question texts
gsm = json.load(open(r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_gsm8k_details.json', encoding='utf-8'))
strat = json.load(open(r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_strategyqa_details.json', encoding='utf-8'))

# Build results
cells = []
for r in PARTIAL_RESULTS:
    cid, task, gold, ext, ok, lat, st, top1, sim1, top2, sim2, top3, sim3, src = r
    q = gsm[str(int(cid.split('_')[1]))]['question'] if task == 'gsm8k' else strat[str(int(cid.split('_')[1]))]['question']
    cells.append({
        'cell_id': cid,
        'task': task,
        'question': q,
        'gold_answer': gold,
        'llm_extracted': ext,
        'is_correct': ok,
        'latency_ms': lat,
        'http_status': st,
        'top3_captions': [top1, top2, top3] if top2 else [top1],
        'top3_sims': [sim1, sim2, sim3] if sim2 else [sim1],
        'source': src,
    })

# Mark not-run cells
for i in range(1, 16):
    cid = f'gsm8k_{i}'
    if cid not in [c['cell_id'] for c in cells]:
        q = gsm[str(i)]['question']
        cells.append({
            'cell_id': cid,
            'task': 'gsm8k',
            'question': q,
            'gold_answer': gsm[str(i)]['answer'],
            'llm_extracted': None,
            'is_correct': None,
            'latency_ms': None,
            'http_status': None,
            'top3_captions': [],
            'top3_sims': [],
            'source': 'NOT_RUN (model hung on prior cells)',
        })
for i in range(1, 16):
    cid = f'strategyqa_{i}'
    q = strat[str(i)]['question']
    cells.append({
        'cell_id': cid,
        'task': 'strategyqa',
        'question': q,
        'gold_answer': strat[str(i)]['answer'],
        'llm_extracted': None,
        'is_correct': None,
        'latency_ms': None,
        'http_status': None,
        'top3_captions': [],
        'top3_sims': [],
        'source': 'NOT_RUN (model hung on prior cells)',
    })

# Summary (only count cells with is_correct != None)
run_cells = [c for c in cells if c['is_correct'] is not None]
gsm_ok = sum(1 for c in run_cells if c['task'] == 'gsm8k' and c['is_correct'])
gsm_total = sum(1 for c in run_cells if c['task'] == 'gsm8k')
strat_ok = sum(1 for c in run_cells if c['task'] == 'strategyqa' and c['is_correct'])
strat_total = sum(1 for c in run_cells if c['task'] == 'strategyqa')
total_ok = gsm_ok + strat_ok
total_run = gsm_total + strat_total
print(f"Run summary:")
print(f"  GSM8K: {gsm_ok}/{gsm_total} = {gsm_ok/max(gsm_total,1)*100:.1f}% (on run cells)")
print(f"  StrategyQA: {strat_ok}/{strat_total} = {strat_ok/max(strat_total,1)*100:.1f}% (on run cells)")
print(f"  Total: {total_ok}/{total_run} = {total_ok/max(total_run,1)*100:.1f}% (on run cells)")
print(f"  NOT RUN: {30-total_run} cells (model hang on gsm8k_7 and gsm8k_10)")

# Save
out = {
    'timestamp': datetime.now(timezone(timedelta(hours=8))).isoformat(timespec='seconds'),
    'stage': 'Stage 3: Deposon-aware RAG 30 cells (PARTIAL, model hang)',
    'chat_model': 'doubao-seed-code-preview-251028',
    'auth': 'ark-...e219',
    'rag_method': 'Deposon T+R+A 3D cosine top-3',
    'max_tokens_main_run': 2048,
    'max_tokens_recovery': 1024,
    'timeout_main': 120,
    'timeout_recovery': 60,
    'no_proxy': True,
    'note': (
        'PARTIAL: gsm8k_7 and gsm8k_10 hit 60s+ read timeouts. '
        'StrategyQA cells 1-15 not run. '
        '7 铁律: no model switch (strict doubao-seed-code-preview-251028) honored. '
        'Per user task spec 30 cells = 15 GSM8K + 15 StrategyQA, but model hung on gsm8k_7 + gsm8k_10. '
        'Captured result: 8/10 GSM8K (80%) on run cells. '
        'This is on par with V4.1-Flash OpenRouter RAG baseline (24/30 = 80%) at per-cell level.'
    ),
    'cells': cells,
    'gsm8k_passed_run': gsm_ok,
    'gsm8k_total_run': gsm_total,
    'strategyqa_passed_run': strat_ok,
    'strategyqa_total_run': strat_total,
    'total_passed_run': total_ok,
    'total_run': total_run,
    'not_run_count': 30 - total_run,
    'verdict_partial': 'GRAY (8/10 on run GSM8K cells, model hung on 2/10; StrategyQA not run)',
}
OUT = r'D:\私人资料\deposon-repo\results\deposon_v3x_6way_stage3_2026_09_10.json'
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print(f"\n[OK] Stage 3 (partial) saved: {OUT} ({os.path.getsize(OUT)} bytes)")
