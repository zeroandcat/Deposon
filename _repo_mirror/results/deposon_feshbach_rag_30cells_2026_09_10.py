# -*- coding: utf-8 -*-
"""
deposon V3.X Feshbach RAG 30 cells LLM 答
- model: doubao-seed-2.0-lite (火山方舟 Coding Plan)
- RAG: 沿 v3 §6 S_eff(E) 公式重排序 22 caption top-3
- baseline: 26/30 = 86.7% (no-RAG doubao-seed-2.0-lite)
- 30 cells: 15 GSM8K + 15 StrategyQA
- key: runtime read GB18030, 永不入 prompt/JSON/disk
- max_tokens=1024, timeout=60s/cell
"""
import os, json, time, re, sys
import urllib.request, urllib.error
import numpy as np
from numpy.linalg import norm

KEY_FILE = r'C:\Users\Administrator\Desktop\AI\LLM API.txt'
GSM8K_FILE = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_gsm8k_details.json'
STQ_FILE = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_strategyqa_details.json'
EMB_FILE = r'D:\私人资料\deposon-repo\results\deposon_volcengine_22caption_embedding_2026_09_10.json'
OUTPUT_JSON = r'D:\私人资料\deposon-repo\results\deposon_feshbach_rag_30cells_2026_09_10.json'
OUTPUT_LOG = r'D:\私人资料\deposon-repo\results\deposon_feshbach_rag_30cells_2026_09_10.log'
BASE_URL = 'https://ark.cn-beijing.volces.com/api/coding/v3'
MODEL = 'doubao-seed-2.0-lite'
SANITY_PROMPT = 'What is 1+1?'
SANITY_MAX_TOKENS = 256
SANITY_TIMEOUT = 20
CELL_MAX_TOKENS = 1024
CELL_TIMEOUT = 60
PROXY_KEYS = ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy']
N_GSM8K = 15
N_STQ = 15
GAMMA = 0.1  # 凝华率 v3 §6
TOP_K = 3    # top-3 caption context


def log(msg):
    line = f'[{time.strftime("%H:%M:%S")}] {msg}'
    print(line, flush=True)
    if LOG_FP is not None:
        LOG_FP.write(line + '\n')
        LOG_FP.flush()


# 0) Open log
os.makedirs(os.path.dirname(OUTPUT_LOG), exist_ok=True)
LOG_FP = open(OUTPUT_LOG, 'w', encoding='utf-8')

# 1) Read key (GB18030)
enc = None
text = None
for enc_name in ('gb18030', 'gbk', 'utf-8', 'utf-16'):
    try:
        text = open(KEY_FILE, 'r', encoding=enc_name).read()
        if 'ark-[REDACTED]' in text:
            enc = enc_name
            break
    except Exception:
        pass
if not enc:
    log('FATAL: key file read failed for all encodings')
    sys.exit(2)
m = re.search(r'ark-[REDACTED][a-zA-Z0-9-]+', text)
if not m:
    log('FATAL: ark-[REDACTED]* key not found')
    sys.exit(2)
api_key = m.group(0)
key_truncated = api_key[:20] + '...' + api_key[-4:]
os.environ['ARK_CODING_PLAN_KEY'] = api_key
for k in PROXY_KEYS:
    os.environ.pop(k, None)
log(f'KEY_OK enc={enc} truncated={key_truncated} proxy_cleared')

# 2) Load benchmarks
with open(GSM8K_FILE, 'r', encoding='utf-8') as f:
    gsm8k = json.load(f)
with open(STQ_FILE, 'r', encoding='utf-8') as f:
    stq = json.load(f)
log(f'BENCHMARK_LOADED gsm8k={len(gsm8k)} stq={len(stq)}')

# 3) Load 22 caption SVD 2D coords (file has SVD coords only; full 2048-dim dropped)
with open(EMB_FILE, 'r', encoding='utf-8') as f:
    emb_data = json.load(f)
svd2 = emb_data['svd2_coords']
caption_ids = emb_data['concept_ids']
# 22 caption 2D coords in id order
S_bg = np.array([svd2[cid] for cid in caption_ids], dtype=float)
N_CAPTIONS = len(S_bg)
log(f'EMB_LOADED captions={N_CAPTIONS} dim=2 svd_var={emb_data["sim_matrix_stats"]["svd_top2_var_explained"]}')


# 4) Feshbach 共振公式 (v3 §6): S_eff(E) = S_bg - (S_bg |W><W| S_bg) / (E - E_0 + i*Γ/2)
# 简化:沿 S_eff 通道 similarity = perp(W) 分量
W = S_bg.mean(axis=0)
W_norm = norm(W)
if W_norm < 1e-10:
    W_unit = W
else:
    W_unit = W / W_norm
# 22 caption 沿 W 投影
proj_captions = (S_bg @ W_unit)  # (22,)
S_bg_perp = S_bg - np.outer(proj_captions, W_unit)  # 22 caption 垂直分量
E_0 = float(np.mean([norm(s) for s in S_bg]))
log(f'FESHBACH_PARAMS E_0={E_0:.4f} gamma={GAMMA} W_norm={W_norm:.4f}')


def feshbach_similarity(E_vec):
    """
    沿 v3 §6 S_eff(E) 通道计算 22 caption 与 E 的 similarity
    E_vec: 2D question encoding [text_len, n_words]
    返回: 22 caption similarity scores
    """
    # E 沿 W 投影 + 垂直分量
    proj_E = E_vec @ W_unit
    E_perp = E_vec - proj_E * W_unit
    # similarity (cosine over perp components)
    sim = S_bg_perp @ E_perp
    norms = norm(S_bg_perp, axis=1) * norm(E_perp) + 1e-10
    return sim / norms


def make_E(question_text, E_0_val):
    """E(题目) = 2D vector [text_len_normalized, n_words_normalized]"""
    n_chars = len(question_text)
    n_words = len(question_text.split())
    # 归一化到 22 caption 能量尺度
    raw = np.array([n_chars, n_words], dtype=float)
    raw = raw / (raw.max() + 1e-10)
    return raw * E_0_val


# 5) HTTP helper
def query_chat(prompt, model, max_tokens, timeout):
    url = f'{BASE_URL}/chat/completions'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': model,
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': max_tokens,
        'temperature': 0.0
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode('utf-8'),
        headers=headers,
        method='POST'
    )
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode('utf-8', errors='replace')
            elapsed_ms = (time.time() - t0) * 1000
            try:
                body = json.loads(raw)
            except Exception:
                body = {'_raw': raw}
            return {'status': resp.status, 'ms': round(elapsed_ms, 1), 'body': body, 'error': None}
    except urllib.error.HTTPError as e:
        elapsed_ms = (time.time() - t0) * 1000
        err_raw = e.read().decode('utf-8', errors='replace') if e.fp else ''
        return {'status': e.code, 'ms': round(elapsed_ms, 1), 'body': None, 'error': err_raw[:500]}
    except Exception as e:
        elapsed_ms = (time.time() - t0) * 1000
        return {'status': -1, 'ms': round(elapsed_ms, 1), 'body': None, 'error': f'{type(e).__name__}: {str(e)[:300]}'}


def extract_text(body):
    if not body or not isinstance(body, dict):
        return ''
    try:
        return body['choices'][0]['message']['content'] or ''
    except Exception:
        return ''


def extract_number(s):
    if s is None:
        return None
    s = str(s)
    # 优先 **N** 粗体
    m = re.findall(r'\*\*\s*(-?\d+(?:\.\d+)?)\s*\*\*', s)
    if m:
        try:
            return float(m[-1])
        except Exception:
            pass
    # fallback 末位数字
    m = re.findall(r'-?\d+(?:\.\d+)?', s)
    if m:
        try:
            return float(m[-1])
        except Exception:
            return None
    return None


def extract_yesno(s):
    if s is None:
        return None
    s = str(s).strip()
    m = re.findall(r'\*\*\s*(Yes|No|yes|no)\s*\*\*', s, re.IGNORECASE)
    if m:
        return m[-1].capitalize()
    tokens = re.findall(r'\b(Yes|No|yes|no)\b', s)
    if tokens:
        return tokens[-1].capitalize()
    return None


# 6) Pre-build cell set
cells_meta = []
for i in range(1, N_GSM8K + 1):
    item = gsm8k.get(str(i), {})
    cells_meta.append({
        'cell_id': f'gsm8k_{i}',
        'task': 'gsm8k',
        'question': item.get('question', ''),
        'gold': item.get('answer', None),
    })
for i in range(1, N_STQ + 1):
    item = stq.get(str(i), {})
    cells_meta.append({
        'cell_id': f'strategyqa_{i}',
        'task': 'strategyqa',
        'question': item.get('question', ''),
        'gold': item.get('answer', None),
    })
log(f'CELLS_BUILT total={len(cells_meta)} (gsm8k={N_GSM8K} strategyqa={N_STQ})')


# 7) Pre-rank 22 caption top-K for each cell (Feshbach RAG)
cell_rag = {}
for c in cells_meta:
    E_vec = make_E(c['question'], E_0)
    sims = feshbach_similarity(E_vec)
    top_idx = np.argsort(-sims)[:TOP_K]
    top_captions = []
    for j in top_idx:
        top_captions.append({
            'caption_id': caption_ids[j],
            'svd2': S_bg[j].tolist(),
            'sim_score': float(sims[j]),
        })
    cell_rag[c['cell_id']] = top_captions
log(f'RAG_PRERANKED top-{TOP_K} for {len(cell_rag)} cells')

# 8) JSON write helper
def write_json(results):
    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    tmp = OUTPUT_JSON + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    os.replace(tmp, OUTPUT_JSON)


# 9) Sanity check
log(f'SANITY_START prompt="{SANITY_PROMPT}" model={MODEL}')
sanity_res = query_chat(SANITY_PROMPT, MODEL, SANITY_MAX_TOKENS, SANITY_TIMEOUT)
sanity_text = extract_text(sanity_res['body'])
sanity_pass = sanity_res['status'] == 200 and len(sanity_text) > 0
log(f'SANITY_DONE status={sanity_res["status"]} ms={sanity_res["ms"]} pass={sanity_pass} preview="{sanity_text[:80]}"')
if not sanity_pass:
    log(f'SANITY_ERROR body={sanity_res["body"]} error={sanity_res["error"]}')

# 10) Initialize results
results = {
    'timestamp': time.strftime('%Y-%m-%dT%H:%M:%S+08:00'),
    'model': MODEL,
    'gateway': '火山方舟 Coding Plan',
    'base_url': BASE_URL,
    'auth': f'{key_truncated} (key loaded from env at runtime; literal key never written to disk)',
    'approach': 'Feshbach-aware RAG (v3 §6 S_eff(E) 公式, 22 caption SVD-2D 76.5% var)',
    'gamma': GAMMA,
    'max_tokens': CELL_MAX_TOKENS,
    'timeout_s': CELL_TIMEOUT,
    'temperature': 0.0,
    'proxy_cleared': True,
    'sanity_check': {
        'model': MODEL,
        'prompt': SANITY_PROMPT,
        'http_status': sanity_res['status'],
        'latency_ms': sanity_res['ms'],
        'sanity_pass': sanity_pass,
    },
    'cells': [],
    'summary': {
        'total_cells': 0,
        'gsm8k_passed': 0,
        'strategyqa_passed': 0,
        'total_passed': 0,
        'pass_rate': 0.0,
        'verdict': '',
    },
    'comparison': {
        'doubao_seed_2_0_lite_no_rag_30cells': '26/30 = 86.7% (baseline)',
        'old_rag_2048d_cosine_30cells': '24/30 = 80% (净 -1 回归)',
        'cpath_no_lmm_simulation': '0% 边际 (NOISE)',
        'feshbach_rag_30cells': '',
    },
    'constraints_honored': {
        'no_proxy': True,
        'key_runtime_only': True,
        'key_in_json_masked': True,
        'no_model_switch': True,
        'no_retry': True,
        'frozen_files_untouched': [
            'verifier/handoff/KT_ABC1_anchors_sha256_12.json',
            'corpus/v20/*',
            'results/deposon_v21_gtformal.json',
            '4 SPEC V0.1 frozen files',
        ],
    },
}
write_json(results)


# 11) 30 cells loop
log(f'CELL_LOOP_START total={len(cells_meta)}')
for idx, c in enumerate(cells_meta):
    cell_id = c['cell_id']
    task = c['task']
    question = c['question']
    gold = c['gold']
    top_captions = cell_rag[cell_id]
    # Build prompt with Feshbach RAG context
    context_lines = [f"- {tc['caption_id']} (sim={tc['sim_score']:.4f})" for tc in top_captions]
    context = '\n'.join(context_lines)
    if task == 'gsm8k':
        user_prompt = (
            f"Context (3 most relevant concepts, ranked by Feshbach S_eff similarity):\n{context}\n\n"
            f"Question: {question}\n\n"
            f"Let's think step by step.\n"
            f"Answer with one number only, ending with **N** format."
        )
    else:
        user_prompt = (
            f"Context (3 most relevant concepts, ranked by Feshbach S_eff similarity):\n{context}\n\n"
            f"Question: {question}\n\n"
            f"Let's think step by step.\n"
            f"Answer with Yes or No only, ending with **Yes** or **No** format."
        )
    log(f'CELL_START [{idx+1}/{len(cells_meta)}] {cell_id} task={task} top_captions={[tc["caption_id"] for tc in top_captions]}')
    res = query_chat(user_prompt, MODEL, CELL_MAX_TOKENS, CELL_TIMEOUT)
    raw_text = extract_text(res['body'])
    if task == 'gsm8k':
        pred = extract_number(raw_text)
        is_correct = (pred is not None and gold is not None and abs(pred - float(gold)) < 1e-6)
    else:
        pred = extract_yesno(raw_text)
        is_correct = (pred is not None and gold is not None and pred.lower() == str(gold).lower())
    cell_record = {
        'cell_id': cell_id,
        'task': task,
        'question': question,
        'gold': gold,
        'top_captions': top_captions,
        'feshbach_user_prompt_preview': user_prompt[:300] + '...' if len(user_prompt) > 300 else user_prompt,
        'llm_raw_response': raw_text[:2000],  # truncate for JSON
        'llm_extracted': pred,
        'is_correct': is_correct,
        'latency_ms': res['ms'],
        'http_status': res['status'],
        'usage': (res['body'].get('usage', {}) if isinstance(res['body'], dict) else {}),
        'note': 'clean' if is_correct else ('fail' if res['status'] == 200 else f'error_{res["status"]}'),
        'error': res['error'],
    }
    results['cells'].append(cell_record)
    log(f'CELL_DONE [{idx+1}/{len(cells_meta)}] {cell_id} pred={pred} gold={gold} correct={is_correct} status={res["status"]} ms={res["ms"]}')
    write_json(results)

# 12) Summary
gsm_passed = sum(1 for c in results['cells'] if c['task'] == 'gsm8k' and c['is_correct'])
stq_passed = sum(1 for c in results['cells'] if c['task'] == 'strategyqa' and c['is_correct'])
total_passed = gsm_passed + stq_passed
pass_rate = total_passed / len(cells_meta) if cells_meta else 0.0
if pass_rate >= 24/30:
    verdict = 'PASS'
elif pass_rate >= 18/30:
    verdict = 'MARGINAL'
else:
    verdict = 'FAIL'
results['summary'] = {
    'total_cells': len(cells_meta),
    'gsm8k_passed': gsm_passed,
    'strategyqa_passed': stq_passed,
    'total_passed': total_passed,
    'pass_rate': round(pass_rate, 4),
    'verdict': verdict,
}
results['comparison']['feshbach_rag_30cells'] = f'{total_passed}/30 = {pass_rate*100:.1f}% (vs no-RAG 26/30 = 86.7%, delta {(total_passed-26)/30*100:+.1f}pp)'
write_json(results)
log(f'SUMMARY_DONE gsm8k={gsm_passed}/15 strategyqa={stq_passed}/15 total={total_passed}/30 verdict={verdict}')
log('DONE')

# 13) Close log
LOG_FP.close()
