# -*- coding: utf-8 -*-
"""
V3X Stage 3 minimal - one cell at a time, no hangs
- Use existing stage 2 T+R+A
- Run remaining cells (gsm8k_7, gsm8k_8-15, strategyqa_1-15) one at a time
- timeout=60s (shorter to avoid hangs)
- If hang, skip and continue
"""
import io, os, re, sys, json, time, urllib.request, urllib.error
import numpy as np
from datetime import datetime, timezone, timedelta

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', line_buffering=True)

# Key
with io.open(r'C:\Users\Administrator\Desktop\AI\LLM API.txt', 'r', encoding='gb18030') as f:
    key_text = f.read()
all_ark = re.findall(r'ark-[a-zA-Z0-9-]+', key_text)
API_KEY = all_ark[1] if len(all_ark) >= 2 else all_ark[0]
KEY_MASK = API_KEY[:4] + '...' + API_KEY[-4:]
del key_text
os.environ['ARK_CODING_PLAN_KEY'] = API_KEY
for p in ('HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy'):
    os.environ.pop(p, None)
print(f"[INIT] key={KEY_MASK}, no proxy")

CHAT_ENDPOINT = 'https://ark.cn-beijing.volces.com/api/coding/v3/chat/completions'
CHAT_MODEL = 'doubao-seed-code-preview-251028'


def query_chat(prompt, timeout=60):
    """One call, short timeout."""
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    body = {
        'model': CHAT_MODEL,
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': 1024,  # shorter to avoid hangs
        'temperature': 0.0
    }
    data_bytes = json.dumps(body, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(CHAT_ENDPOINT, data=data_bytes, headers=headers, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode('utf-8')
            return json.loads(raw), (time.time() - t0) * 1000, resp.status, None
    except urllib.error.HTTPError as e:
        return None, (time.time() - t0) * 1000, e.code, (e.read().decode('utf-8', errors='replace') if e.fp else '')[:300]
    except Exception as e:
        return None, (time.time() - t0) * 1000, 0, str(e)[:300]


# Load stage 2
STAGE2 = json.load(open(r'D:\私人资料\deposon-repo\results\deposon_v3x_6way_stage2_2026_09_10.json', encoding='utf-8'))
T_22 = np.array([STAGE2['T_values'][k] for k in sorted(STAGE2['T_values'].keys())])
R_22 = np.array([STAGE2['R_values'][k] for k in sorted(STAGE2['R_values'].keys())])
A_22 = np.array([STAGE2['A_values'][k] for k in sorted(STAGE2['A_values'].keys())])
concept_ids = sorted(STAGE2['T_values'].keys())
TRA_22 = np.stack([T_22, R_22, A_22], axis=1)
TRA_22_n = TRA_22 / (np.linalg.norm(TRA_22, axis=1, keepdims=True) + 1e-12)

# Load cell questions
gsm = json.load(open(r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_gsm8k_details.json', encoding='utf-8'))
strat = json.load(open(r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_strategyqa_details.json', encoding='utf-8'))

# Captions
CORPUS_DIR = r'D:\私人资料\deposon-repo\corpus\v20'
idx = json.load(open(os.path.join(CORPUS_DIR, 'index.json'), encoding='utf-8'))
captions = []
for g in idx['graphs']:
    d = json.load(open(os.path.join(CORPUS_DIR, g['file']), encoding='utf-8'))
    cap = (f"Concept graph {g['graph_id']} (family={g['family']}, structure={g['structure']}, "
           f"N={g['N']}, n_named={g['n_named']}): " + '; '.join(d.get('labels', [])))
    captions.append(cap)
print(f"[INIT] 22 captions ready, T+R+A loaded")

# Sanity
print("[SANITY] What is 1+1?")
body, lat, st, err = query_chat("What is 1+1?")
if st == 200 and body and '2' in (body.get('choices', [{}])[0].get('message', {}).get('content', '') or ''):
    print(f"  [OK] sanity PASS lat={lat:.0f}ms")
else:
    print(f"  [FATAL] sanity FAIL st={st} err={err}")
    sys.exit(4)

# Existing 6 cells (from previous run) - hardcode
existing = {
    'gsm8k_1': {'extracted': 18.0, 'correct': True, 'latency': 13729, 'top1': 'S2', 'sim': 0.998},
    'gsm8k_2': {'extracted': 5.0, 'correct': True, 'latency': 4065, 'top1': 'S2', 'sim': 0.994},
    'gsm8k_3': {'extracted': 40.0, 'correct': True, 'latency': 14398, 'top1': 'L_historical_causality', 'sim': 0.998},
    'gsm8k_4': {'extracted': 1430.0, 'correct': True, 'latency': 6209, 'top1': 'S6_n20', 'sim': 1.000},
    'gsm8k_5': {'extracted': 36.0, 'correct': True, 'latency': 5566, 'top1': 'S1_n35', 'sim': 0.999},
    'gsm8k_6': {'extracted': 8000.0, 'correct': True, 'latency': 4585, 'top1': 'S2', 'sim': 0.998},
}

# Run remaining cells
def run_one_cell(cell_id, task, question, gold, top3_idx, top3_sims):
    """Run one cell, return (extracted, is_correct, latency_ms, status, err, raw)."""
    top3_caps = [captions[j] for j in top3_idx]
    if task == 'gsm8k':
        prompt = (f"Context (3 most relevant concepts, Deposon T+R+A projection):\n"
                  f"- {top3_caps[0]}\n- {top3_caps[1]}\n- {top3_caps[2]}\n\n"
                  f"Question: {question}\nAnswer in one number:")
    else:
        prompt = (f"Context (3 most relevant concepts, Deposon T+R+A projection):\n"
                  f"- {top3_caps[0]}\n- {top3_caps[1]}\n- {top3_caps[2]}\n\n"
                  f"Question: {question}\nAnswer Yes or No:")
    body, lat, st, err = query_chat(prompt, timeout=60)
    if st != 200 or not body:
        return None, False, lat, st, (err or '')[:200], None
    content = (body.get('choices', [{}])[0].get('message', {}).get('content', '') or '')
    if task == 'gsm8k':
        boxed = re.findall(r'\\boxed\{([-+]?\d+\.?\d*)\}', content)
        if boxed:
            try: extracted = float(boxed[-1])
            except: extracted = None
        else:
            nums = re.findall(r'[-+]?\d+\.?\d*', content)
            extracted = float(nums[-1]) if nums else None
        is_correct = extracted is not None and abs(extracted - gold) < 1e-3
    else:
        t = content.strip().lower()
        first = t.split('\n')[0].strip()
        if first in ('yes', 'no'):
            extracted = first[0].upper() + first[1:]
        else:
            m = re.findall(r'\b(yes|no)\b', t)
            extracted = (m[0][0].upper() + m[0][1:]) if m else None
        is_correct = extracted is not None and extracted.lower() == str(gold).lower()
    return extracted, is_correct, lat, st, None, content[:500]


# Need to compute top-3 for each cell. We have the cell_embs from the previous run - but we don't have them saved.
# Let me re-embed 30 cells (just 1 batch of 30 = 4 chunks of 10 = 4 API calls, fast)
EMBED_ENDPOINT = 'https://ark.cn-beijing.volces.com/api/coding/v3/embeddings'
EMBED_MODEL = 'doubao-embedding-vision-251215'

def query_embed(inputs, timeout=60):
    headers = {'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'}
    body = {'model': EMBED_MODEL, 'input': inputs}
    data_bytes = json.dumps(body, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(EMBED_ENDPOINT, data=data_bytes, headers=headers, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode('utf-8')
            return json.loads(raw), (time.time() - t0) * 1000, resp.status, None
    except Exception as e:
        return None, (time.time() - t0) * 1000, 0, str(e)[:300]


cells_data = []
for i in range(1, 16):
    item = gsm[str(i)]
    cells_data.append({'cell_id': f'gsm8k_{i}', 'task': 'gsm8k', 'question': item['question'], 'gold_answer': item['answer']})
for i in range(1, 16):
    item = strat[str(i)]
    cells_data.append({'cell_id': f'strategyqa_{i}', 'task': 'strategyqa', 'question': item['question'], 'gold_answer': item['answer']})

# Embed all 30 cells in 3 chunks
print("\n[EMBED] 30 cells in 3 chunks")
cell_qs = [c['question'] for c in cells_data]
emb_data = []
for ci in range(3):
    chunk = cell_qs[ci*10:(ci+1)*10]
    body, lat, st, err = query_embed(chunk)
    if st == 200 and body:
        emb_data.extend(body.get('data', []))
        print(f"  chunk {ci+1} status=200 lat={lat:.0f}ms")
    else:
        print(f"  chunk {ci+1} FAIL st={st} err={err}")
    time.sleep(0.2)
emb_data.sort(key=lambda x: x.get('index', 0))
cell_embs = np.array([item['embedding'] for item in emb_data], dtype=np.float32)
print(f"[CELL EMB] shape={cell_embs.shape}")

# Project
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
proj = pca.fit_transform(cell_embs)
full_var = (cell_embs ** 2).sum(axis=1)
proj_var = (proj ** 2).sum(axis=1)
A_var = np.maximum(full_var - proj_var, 0)
T_var = (proj[:, 0] ** 2)
R_var = (proj[:, 1] ** 2)
total = T_var + R_var + A_var + 1e-10
T_cells = T_var / total
R_cells = R_var / total
A_cells = A_var / total
TRA_cells = np.stack([T_cells, R_cells, A_cells], axis=1)
TRA_cells_n = TRA_cells / (np.linalg.norm(TRA_cells, axis=1, keepdims=True) + 1e-12)
TRA_sim = TRA_cells_n @ TRA_22_n.T
print(f"[TRA sim] range=[{TRA_sim.min():.3f}, {TRA_sim.max():.3f}], mean={TRA_sim.mean():.3f}")

# Run all 30 cells (gsm8k_1-6 from existing, 7-15 + strategyqa_1-15 fresh)
print("\n[RUN] 30 cells (6 cached + 24 fresh, timeout=60s) ...")
results = []
for ci, cell in enumerate(cells_data):
    sims = TRA_sim[ci]
    top3_idx = np.argsort(-sims)[:3]
    top3_sims = [float(sims[j]) for j in top3_idx]
    top3_caps = [concept_ids[j] for j in top3_idx]
    if cell['cell_id'] in existing:
        # Use cached
        e = existing[cell['cell_id']]
        results.append({
            'cell_id': cell['cell_id'],
            'task': cell['task'],
            'question': cell['question'],
            'gold_answer': cell['gold_answer'],
            'llm_extracted': e['extracted'],
            'is_correct': e['correct'],
            'latency_ms': e['latency'],
            'http_status': 200,
            'top3_captions': top3_caps,
            'top3_sims': top3_sims,
            'source': 'cached (from previous run)'
        })
        mark = 'OK' if e['correct'] else 'FAIL'
        print(f"  [{cell['cell_id']}] CACHED {mark} ext={e['extracted']}")
        continue
    # Run fresh
    extracted, is_correct, lat, st, err, raw = run_one_cell(
        cell['cell_id'], cell['task'], cell['question'], cell['gold_answer'],
        top3_idx, top3_sims
    )
    results.append({
        'cell_id': cell['cell_id'],
        'task': cell['task'],
        'question': cell['question'],
        'gold_answer': cell['gold_answer'],
        'llm_extracted': extracted,
        'is_correct': is_correct,
        'latency_ms': round(lat, 1),
        'http_status': st,
        'top3_captions': top3_caps,
        'top3_sims': top3_sims,
        'llm_raw_response': raw,
        'error': err
    })
    mark = 'OK' if is_correct else 'FAIL'
    print(f"  [{cell['cell_id']}] {mark} ext={extracted} lat={lat:.0f}ms top1={top3_caps[0]}({top3_sims[0]:.3f}) st={st}")
    time.sleep(0.2)

# Summary
gsm_ok = sum(1 for r in results if r['task'] == 'gsm8k' and r['is_correct'])
strat_ok = sum(1 for r in results if r['task'] == 'strategyqa' and r['is_correct'])
total_ok = gsm_ok + strat_ok
verdict = 'PASS' if total_ok >= 24 else ('GRAY' if total_ok >= 18 else 'FAIL')
print(f"\n[SUMMARY] GSM8K {gsm_ok}/15 = {gsm_ok/15*100:.1f}% | StrategyQA {strat_ok}/15 = {strat_ok/15*100:.1f}% | Total {total_ok}/30 = {total_ok/30*100:.1f}% → {verdict}")

# Save
out = {
    'timestamp': datetime.now(timezone(timedelta(hours=8))).isoformat(timespec='seconds'),
    'stage': 'Stage 3: Deposon-aware RAG 30 cells (minimal, timeout=60s, max_tokens=1024)',
    'chat_model': CHAT_MODEL,
    'auth': KEY_MASK,
    'rag_method': 'Deposon T+R+A 3D cosine top-3',
    'max_tokens': 1024,
    'timeout_s': 60,
    'no_proxy': True,
    'cells': results,
    'gsm8k_passed': gsm_ok,
    'strategyqa_passed': strat_ok,
    'total_passed': total_ok,
    'verdict': verdict,
}
OUT = r'D:\私人资料\deposon-repo\results\deposon_v3x_6way_stage3_2026_09_10.json'
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print(f"\n[OK] Stage 3 saved: {OUT} ({os.path.getsize(OUT)} bytes)")
print(f"\n[VERDICT]")
print(f"  Stage 2 (A_path Deposon-aware T-channel): ratio={STAGE2['T_channel_ratio']:.4f} → {STAGE2['verdict_A']}")
print(f"  vs Cosine baseline ratio={STAGE2['cosine_ratio_baseline']:.4f}")
print(f"  Stage 3 (C_path Deposon-aware RAG): {total_ok}/30 = {total_ok/30*100:.1f}% → {verdict}")
print(f"  vs V4.1-Flash no-RAG: 25/30 = 83.3%")
print(f"  vs V4.1-Flash OpenRouter RAG: 24/30 = 80.0%")
