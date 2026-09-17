# -*- coding: utf-8 -*-
"""
V3X 6-Way Stage 3 Recovery Script
- Re-run all 30 cells with timeout=180s (longer for seed-code reasoning chain)
- Use T+R+A 3D cosine from existing stage2 JSON (no re-fetch)
- Save to existing stage3 JSON structure
"""
import io
import os
import re
import sys
import json
import time
import urllib.request
import urllib.error
import numpy as np
from datetime import datetime, timezone, timedelta

# Force UTF-8 stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', line_buffering=True)
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', line_buffering=True)

# ---------------- 0. Load API key (GB18030) ----------------
KEY_FILE = r'C:\Users\Administrator\Desktop\AI\LLM API.txt'
with io.open(KEY_FILE, 'r', encoding='gb18030') as f:
    key_text = f.read()
all_ark = re.findall(r'ark-[a-zA-Z0-9-]+', key_text)
API_KEY = all_ark[1] if len(all_ark) >= 2 else all_ark[0]
KEY_MASK = API_KEY[:4] + '...' + API_KEY[-4:] if len(API_KEY) >= 8 else 'ark-...'
del key_text
os.environ['ARK_CODING_PLAN_KEY'] = API_KEY
for p in ('HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy'):
    os.environ.pop(p, None)
print(f"[INIT] key mask={KEY_MASK}, no proxy, 7 铁律 honored")

# ---------------- 1. Constants ----------------
GSM8K_PATH = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_gsm8k_details.json'
STRATEGYQA_PATH = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_strategyqa_details.json'
CHAT_ENDPOINT = 'https://ark.cn-beijing.volces.com/api/coding/v3/chat/completions'
EMBED_ENDPOINT = 'https://ark.cn-beijing.volces.com/api/coding/v3/embeddings'
CHAT_MODEL = 'doubao-seed-code-preview-251028'  # strict, no switch
EMBED_MODEL = 'doubao-embedding-vision-251215'
MAX_TOKENS = 2048
TIMEOUT_S = 180  # increased from 120s for long reasoning chains


def query_chat(prompt, model=CHAT_MODEL, max_tokens=MAX_TOKENS, timeout=TIMEOUT_S):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    body = {
        'model': model,
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': max_tokens,
        'temperature': 0.0
    }
    data_bytes = json.dumps(body, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(CHAT_ENDPOINT, data=data_bytes, headers=headers, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode('utf-8')
            latency_ms = (time.time() - t0) * 1000
            return json.loads(raw), latency_ms, resp.status, None
    except urllib.error.HTTPError as e:
        err = e.read().decode('utf-8', errors='replace') if e.fp else ''
        return None, (time.time() - t0) * 1000, e.code, err
    except Exception as e:
        return None, (time.time() - t0) * 1000, 0, str(e)[:300]


def query_embed(inputs, model=EMBED_MODEL, timeout=TIMEOUT_S):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    body = {'model': model, 'input': inputs}
    data_bytes = json.dumps(body, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(EMBED_ENDPOINT, data=data_bytes, headers=headers, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode('utf-8')
            latency_ms = (time.time() - t0) * 1000
            return json.loads(raw), latency_ms, resp.status, None
    except urllib.error.HTTPError as e:
        err = e.read().decode('utf-8', errors='replace') if e.fp else ''
        return None, (time.time() - t0) * 1000, e.code, err
    except Exception as e:
        return None, (time.time() - t0) * 1000, 0, str(e)[:300]


def extract_number(text):
    if not text:
        return None
    boxed = re.findall(r'\\boxed\{([-+]?\d+\.?\d*)\}', text)
    if boxed:
        try:
            return float(boxed[-1])
        except ValueError:
            pass
    hash_match = re.findall(r'####\s*([-+]?\d+\.?\d*)', text)
    if hash_match:
        try:
            return float(hash_match[-1])
        except ValueError:
            pass
    nums = re.findall(r'[-+]?\d+\.?\d*', text)
    if nums:
        try:
            return float(nums[-1])
        except ValueError:
            return None
    return None


def extract_yes_no(text):
    if not text:
        return None
    t = text.strip().lower()
    first_line = t.split('\n')[0].strip()
    if first_line in ('yes', 'no'):
        return first_line[0].upper() + first_line[1:]
    boxed = re.findall(r'\\boxed\{(yes|no)\}', t)
    if boxed:
        return boxed[-1][0].upper() + boxed[-1][1:]
    for word in re.findall(r'\b(yes|no)\b', t):
        return word[0].upper() + word[1:]
    return None


# ---------------- 2. Load 22 caption T+R+A from stage2 JSON ----------------
STAGE2_JSON = r'D:\私人资料\deposon-repo\results\deposon_v3x_6way_stage2_2026_09_10.json'
s2 = json.load(open(STAGE2_JSON, encoding='utf-8'))
T_22 = np.array([s2['T_values'][k] for k in sorted(s2['T_values'].keys())])
R_22 = np.array([s2['R_values'][k] for k in sorted(s2['R_values'].keys())])
A_22 = np.array([s2['A_values'][k] for k in sorted(s2['A_values'].keys())])
concept_ids = sorted(s2['T_values'].keys())
print(f"[STAGE2 LOAD] T+R+A loaded for {len(concept_ids)} captions")
print(f"  T: mean={T_22.mean():.4f}, R: mean={R_22.mean():.4f}, A: mean={A_22.mean():.4f}")

# ---------------- 3. Load 30 cell questions ----------------
gsm8k_data = json.load(open(GSM8K_PATH, encoding='utf-8'))
strategyqa_data = json.load(open(STRATEGYQA_PATH, encoding='utf-8'))
cells = []
for i in range(1, 16):
    item = gsm8k_data[str(i)]
    cells.append({
        'cell_id': f'gsm8k_{i}',
        'task': 'gsm8k',
        'question': item['question'],
        'gold_answer': item['answer'],
    })
for i in range(1, 16):
    item = strategyqa_data[str(i)]
    cells.append({
        'cell_id': f'strategyqa_{i}',
        'task': 'strategyqa',
        'question': item['question'],
        'gold_answer': item['answer'],
    })
print(f"[CELLS] loaded 30 cells")

# ---------------- 4. Sanity check (1-cell) ----------------
print("\n[SANITY] What is 1+1?")
body, lat, status, err = query_chat("What is 1+1?")
if status == 200 and body and '2' in (body.get('choices', [{}])[0].get('message', {}).get('content', '') or ''):
    print(f"  [OK] sanity PASS, latency={lat:.0f}ms")
else:
    print(f"  [FATAL] sanity FAIL status={status} err={(err or '')[:300]}")
    sys.exit(4)

# ---------------- 5. Embed 30 cell questions ----------------
print("\n[EMBED] 30 cell questions (3 chunks of 10) ...")
cell_questions = [c['question'] for c in cells]
cell_emb_data = []
for ci in range(3):
    chunk_qs = cell_questions[ci*10:(ci+1)*10]
    body, lat, status, err = query_embed(chunk_qs)
    if status != 200 or not body:
        print(f"  [FATAL] cell embed chunk {ci+1} status={status} err={(err or '')[:300]}")
        sys.exit(2)
    ed = body.get('data', [])
    cell_emb_data.extend(ed)
    print(f"  cell chunk {ci+1} status=200 latency={lat:.0f}ms")
    time.sleep(0.3)
cell_emb_data.sort(key=lambda x: x.get('index', 0))
cell_embs = np.array([item['embedding'] for item in cell_emb_data], dtype=np.float32)
print(f"[CELL EMB] shape={cell_embs.shape}")

# Project to T+R+A (each dataset separately, same recipe as 22 caption)
def deposon_project(embs, n_components=2):
    from sklearn.decomposition import PCA
    pca = PCA(n_components=n_components)
    proj = pca.fit_transform(embs)
    full_var = (embs ** 2).sum(axis=1)
    proj_var = (proj ** 2).sum(axis=1)
    A_var = np.maximum(full_var - proj_var, 0)
    T_var = (proj[:, 0] ** 2)
    R_var = (proj[:, 1] ** 2) if n_components >= 2 else np.zeros_like(T_var)
    total = T_var + R_var + A_var + 1e-10
    T = T_var / total
    R = R_var / total
    A = A_var / total
    return T, R, A, proj


T_cells, R_cells, A_cells, proj_cells = deposon_project(cell_embs, n_components=2)
print(f"[CELL PROJ] T mean={T_cells.mean():.4f}, R mean={R_cells.mean():.4f}, A mean={A_cells.mean():.4f}")

# 3D cosine (T, R, A) as 3D coordinates
TRA_22 = np.stack([T_22, R_22, A_22], axis=1)
TRA_cells = np.stack([T_cells, R_cells, A_cells], axis=1)
TRA_22_n = TRA_22 / (np.linalg.norm(TRA_22, axis=1, keepdims=True) + 1e-12)
TRA_cells_n = TRA_cells / (np.linalg.norm(TRA_cells, axis=1, keepdims=True) + 1e-12)
TRA_sim = TRA_cells_n @ TRA_22_n.T
print(f"[TRA sim 3D] shape={TRA_sim.shape}, range=[{TRA_sim.min():.4f}, {TRA_sim.max():.4f}], mean={TRA_sim.mean():.4f}")

# ---------------- 6. Reconstruct 22 captions for prompt context ----------------
# (Need to rebuild the same caption strings as stage 2 used)
CORPUS_DIR = r'D:\私人资料\deposon-repo\corpus\v20'
index = json.load(open(os.path.join(CORPUS_DIR, 'index.json'), encoding='utf-8'))
captions = []
caption_ids_in_order = []
for g in index['graphs']:
    d = json.load(open(os.path.join(CORPUS_DIR, g['file']), encoding='utf-8'))
    labels = d.get('labels', [])
    cap = (f"Concept graph {g['graph_id']} "
           f"(family={g['family']}, structure={g['structure']}, "
           f"N={g['N']}, n_named={g['n_named']}): " + '; '.join(labels))
    captions.append(cap)
    caption_ids_in_order.append(g['graph_id'])
assert caption_ids_in_order == concept_ids, f"order mismatch"
print(f"[CAPTIONS] 22 captions ready for prompt context")

# ---------------- 7. Run 30 cells ----------------
print("\n[STAGE 3] running 30 cells with Deposon-aware RAG (top-3 by 3D TRA cosine) ...")
results_3 = []
for ci, cell in enumerate(cells):
    sims = TRA_sim[ci]
    top3_idx = np.argsort(-sims)[:3]
    top3_caps = [captions[j] for j in top3_idx]
    top3_sims = [float(sims[j]) for j in top3_idx]
    if cell['task'] == 'gsm8k':
        prompt = (f"Context (3 most relevant concepts, Deposon T+R+A projection):\n"
                  f"- {top3_caps[0]}\n"
                  f"- {top3_caps[1]}\n"
                  f"- {top3_caps[2]}\n\n"
                  f"Question: {cell['question']}\n"
                  f"Answer in one number:")
    else:
        prompt = (f"Context (3 most relevant concepts, Deposon T+R+A projection):\n"
                  f"- {top3_caps[0]}\n"
                  f"- {top3_caps[1]}\n"
                  f"- {top3_caps[2]}\n\n"
                  f"Question: {cell['question']}\n"
                  f"Answer Yes or No:")
    body, lat, status, err = query_chat(prompt)
    if status != 200 or not body:
        print(f"  [{cell['cell_id']}] FAIL status={status} err={(err or '')[:200]}")
        results_3.append({
            'cell_id': cell['cell_id'],
            'task': cell['task'],
            'question': cell['question'],
            'gold_answer': cell['gold_answer'],
            'llm_raw_response': None,
            'llm_extracted': None,
            'is_correct': False,
            'latency_ms': round(lat, 1),
            'http_status': status,
            'top3_captions': [concept_ids[j] for j in top3_idx],
            'top3_sims': top3_sims,
            'error': (err[:300] if err else 'unknown')
        })
        time.sleep(0.3)
        continue
    msg = body.get('choices', [{}])[0].get('message', {})
    content = msg.get('content', '') or ''
    if cell['task'] == 'gsm8k':
        extracted = extract_number(content)
        is_correct = (extracted is not None and abs(extracted - cell['gold_answer']) < 1e-3)
    else:
        extracted = extract_yes_no(content)
        is_correct = (extracted is not None and extracted.lower() == str(cell['gold_answer']).lower())
    results_3.append({
        'cell_id': cell['cell_id'],
        'task': cell['task'],
        'question': cell['question'],
        'gold_answer': cell['gold_answer'],
        'llm_raw_response': content[:500],
        'llm_extracted': extracted,
        'is_correct': is_correct,
        'latency_ms': round(lat, 1),
        'http_status': status,
        'top3_captions': [concept_ids[j] for j in top3_idx],
        'top3_sims': top3_sims,
        'error': None
    })
    mark = 'OK' if is_correct else 'FAIL'
    print(f"  [{cell['cell_id']}] gold={cell['gold_answer']} extracted={extracted} [{mark}] "
          f"top1={concept_ids[top3_idx[0]]}({top3_sims[0]:.3f}) lat={lat:.0f}ms")
    time.sleep(0.3)

# Summary
gsm_ok = sum(1 for r in results_3 if r['task'] == 'gsm8k' and r['is_correct'])
strat_ok = sum(1 for r in results_3 if r['task'] == 'strategyqa' and r['is_correct'])
total_ok = gsm_ok + strat_ok
verdict_3 = 'PASS' if total_ok >= 24 else ('GRAY' if total_ok >= 18 else 'FAIL')
print(f"\n[STAGE 3 VERDICT]")
print(f"  GSM8K: {gsm_ok}/15 = {gsm_ok/15*100:.1f}%")
print(f"  StrategyQA: {strat_ok}/15 = {strat_ok/15*100:.1f}%")
print(f"  Total: {total_ok}/30 = {total_ok/30*100:.1f}% → {verdict_3}")

# Save
stage3_result = {
    'timestamp': datetime.now(timezone(timedelta(hours=8))).isoformat(timespec='seconds'),
    'stage': 'Stage 3: Deposon-aware RAG 30 cells re-test (recovery, timeout=180s)',
    'chat_model': CHAT_MODEL,
    'chat_endpoint': CHAT_ENDPOINT,
    'auth': KEY_MASK,
    'embed_model': EMBED_MODEL,
    'rag_method': 'Deposon T+R+A 3D cosine top-3',
    'max_tokens': MAX_TOKENS,
    'temperature': 0.0,
    'timeout_s': TIMEOUT_S,
    'no_proxy': True,
    'cells': results_3,
    'gsm8k_passed': gsm_ok,
    'strategyqa_passed': strat_ok,
    'total_passed': total_ok,
    'verdict': verdict_3,
    'verdict_rule': 'PASS if >=24/30, GRAY if 18-23, FAIL if <18',
    'constraints_honored': {
        'no_proxy': True,
        'key_runtime_only': True,
        'key_in_json_masked': True,
        'no_model_switch': True,
        'frozen_files_untouched': [
            'corpus/v20/index.json', 'corpus/v20/*.json',
            'verifier/handoff/KT_ABC1_anchors_sha256_12.json',
            '4 SPEC V0.1 frozen', 'v19/v21 frozen JSON'
        ]
    }
}
STAGE3_JSON = r'D:\私人资料\deposon-repo\results\deposon_v3x_6way_stage3_2026_09_10.json'
with open(STAGE3_JSON, 'w', encoding='utf-8') as f:
    json.dump(stage3_result, f, ensure_ascii=False, indent=2)
print(f"\n[OK] Stage 3 saved: {STAGE3_JSON} ({os.path.getsize(STAGE3_JSON)} bytes)")

# Final summary
final_summary = {
    'timestamp': datetime.now(timezone(timedelta(hours=8))).isoformat(timespec='seconds'),
    'stage1': {
        'A_verdict': 'see report',
        'B_verdict': 'see report',
        'D_verdict': 'see report',
        'E_verdict': 'see report',
        'F_verdict': 'see report',
    },
    'stage2': {
        'T_channel_ratio': s2['T_channel_ratio'],
        'R_channel_ratio': s2['R_channel_ratio'],
        'A_channel_ratio': s2['A_channel_ratio'],
        'cosine_ratio_baseline': s2['cosine_ratio_baseline'],
        'kmeans_ari_on_T_channel': s2['kmeans_ari_on_T_channel'],
        'kmeans_ari_on_2048d_baseline': s2['kmeans_ari_on_2048d_baseline'],
        'verdict_A': s2['verdict_A'],
    },
    'stage3': {
        'gsm8k_passed': gsm_ok,
        'strategyqa_passed': strat_ok,
        'total_passed': total_ok,
        'verdict_C': verdict_3,
    }
}
FINAL_JSON = r'D:\私人资料\deposon-repo\results\deposon_v3x_6way_summary_2026_09_10.json'
with open(FINAL_JSON, 'w', encoding='utf-8') as f:
    json.dump(final_summary, f, ensure_ascii=False, indent=2)
print(f"[OK] Final summary: {FINAL_JSON}")

print(f"\n[FINAL]")
print(f"Stage 2: A_path (Deposon-aware T-channel) ratio={s2['T_channel_ratio']:.4f} → {s2['verdict_A']}")
print(f"  vs Cosine baseline ratio={s2['cosine_ratio_baseline']:.4f}")
print(f"Stage 3: C_path (Deposon-aware RAG): {total_ok}/30 = {total_ok/30*100:.1f}% → {verdict_3}")
print(f"  vs V4.1-Flash no-RAG: 25/30 = 83.3%")
print(f"  vs V4.1-Flash OpenRouter RAG: 24/30 = 80.0%")
print(f"  vs Doubao coding-plan 5 cells: 5/5 = 100% (5/5 subset)")
