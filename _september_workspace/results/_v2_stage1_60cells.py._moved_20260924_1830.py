# -*- coding: utf-8 -*-
"""
deposon V2 阶段 1 (60 cells 全量 + F-1 6 embedding 散射截面)
- 30 已有 (gsm8k_1-15 + strategyqa_1-15) 沿用 dpath_cross_modal_2026_09_10.json
- 30 新增 (gsm8k_16-30 + strategyqa_16-30) 重跑 doubao-seed-2.0-lite
- F-1: 6 embedding model 散射截面(0 新调用,纯 numpy 算 T/R/A)
- 严守 7 铁律
"""
import os
import sys
import io
import re
import json
import time
import hashlib
import base64
import urllib.request
import urllib.error
import numpy as np
from datetime import datetime, timezone, timedelta

# ============== Config ==============
KEY_FILE = r'C:\Users\Administrator\Desktop\AI\LLM API.txt'
CORPUS_DIR = r'D:\私人资料\deposon-repo\corpus\v20'
PNG_DIR = r'D:\私人资料\deposon-repo\figures\v3x\corpus_pngs'
GSM8K_FILE = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_gsm8k_details.json'
STQ_FILE = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_strategyqa_details.json'
DPATH_REF = r'D:\私人资料\deposon-repo\results\deposon_dpath_cross_modal_2026_09_10.json'
OPENROUTER_5MODEL_REF = r'D:\私人资料\deposon-repo\results\deposon_openrouter_5model_rag_30cells_2026_09_10.json'
VOLC_22CAP_REF = r'D:\私人资料\deposon-repo\results\deposon_volcengine_22caption_embedding_2026_09_10.json'
OR_5MODEL_EMB_REF = r'D:\私人资料\deposon-repo\results\deposon_openrouter_embedding_5model_2026_09_10.json'

OUTPUT_JSON = r'D:\私人资料\deposon-repo\results\deposon_v2_phase1_60cells_2026_09_11.json'
OUTPUT_LOG = r'D:\私人资料\deposon-repo\results\deposon_v2_phase1_60cells_2026_09_11.log'

BASE_URL = 'https://ark.cn-beijing.volces.com/api/coding/v3'
MODEL_EMB = 'doubao-embedding-vision-251215'
MODEL_CHAT = 'doubao-seed-2.0-lite'
SANITY_PROMPT = 'What is 1+1?'
SANITY_MAX_TOKENS = 256
SANITY_TIMEOUT = 20
CELL_MAX_TOKENS = 1024
CELL_TIMEOUT = 30
EMB_BATCH = 10
EMB_TIMEOUT = 30
N_GSM8K_NEW = 15  # 16-30
N_STQ_NEW = 15    # 16-30
TOP_K = 3
PROXY_KEYS = ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy']

# 6 embedding models for F-1
F1_MODELS = [
    {'name': 'doubao-embedding-vision-251215', 'gateway': 'volcengine', 'dim': 2048, 'kind': 'text+image'},
    {'name': 'liquid/lfm-2.5-embedding-350m:free', 'gateway': 'openrouter', 'dim': 1024, 'kind': 'text'},
    {'name': 'nvidia/nemotron-3-embed-1b:free', 'gateway': 'openrouter', 'dim': 2048, 'kind': 'text'},
    {'name': 'nvidia/llama-nemotron-embed-vl-1b-v2:free', 'gateway': 'openrouter', 'dim': 2048, 'kind': 'text'},
    {'name': 'thenlper/gte-base', 'gateway': 'openrouter', 'dim': 768, 'kind': 'text'},
    {'name': 'voyageai/voyage-4', 'gateway': 'openrouter', 'dim': 1024, 'kind': 'text'},
]

# ============== Logging ==============
LOG_FP = None
def log(msg):
    line = f'[{time.strftime("%H:%M:%S")}] {msg}'
    print(line, flush=True)
    if LOG_FP is not None:
        try:
            LOG_FP.write(line + '\n')
            LOG_FP.flush()
        except Exception:
            pass


# ============== Key + Proxy ==============
def load_key():
    text = None
    for enc_name in ('gb18030', 'gbk', 'utf-8', 'utf-16'):
        try:
            text = io.open(KEY_FILE, 'r', encoding=enc_name).read()
            if 'ark-[REDACTED]' in text:
                break
        except Exception:
            pass
    if not text:
        raise RuntimeError('FATAL: key file read failed for all encodings')
    m = re.search(r'ark-[REDACTED][a-zA-Z0-9-]+', text)
    if not m:
        raise RuntimeError('FATAL: ark-[REDACTED]* key not found')
    api_key = m.group(0)
    key_truncated = api_key[:20] + '...' + api_key[-4:]
    os.environ['ARK_CODING_PLAN_KEY'] = api_key
    for k in PROXY_KEYS:
        os.environ.pop(k, None)
    del text
    return api_key, key_truncated


# ============== HTTP helpers ==============
def http_post(url, payload, headers, timeout):
    data = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
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
        try:
            err_raw = e.read().decode('utf-8', errors='replace') if e.fp else ''
        except Exception:
            err_raw = ''
        return {'status': e.code, 'ms': round(elapsed_ms, 1), 'body': None, 'error': err_raw[:500]}
    except Exception as e:
        elapsed_ms = (time.time() - t0) * 1000
        return {'status': -1, 'ms': round(elapsed_ms, 1), 'body': None,
                'error': f'{type(e).__name__}: {str(e)[:300]}'}


def query_chat(api_key, prompt, model, max_tokens, timeout, temperature=0.0):
    url = f'{BASE_URL}/chat/completions'
    headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}
    payload = {
        'model': model,
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': max_tokens,
        'temperature': temperature,
    }
    return http_post(url, payload, headers, timeout)


def query_embedding_text(api_key, captions, model=MODEL_EMB, batch=EMB_BATCH):
    url = f'{BASE_URL}/embeddings'
    headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}
    chunks = [captions[i:i + batch] for i in range(0, len(captions), batch)]
    out = []
    for ci, chunk in enumerate(chunks):
        payload = {'model': model, 'input': chunk}
        res = http_post(url, payload, headers, timeout=EMB_TIMEOUT)
        if res['status'] != 200:
            raise RuntimeError(f'emb-text chunk {ci} status={res["status"]} error={res["error"][:200]}')
        data = res['body'].get('data', [])
        data.sort(key=lambda x: x.get('index', 0))
        for d in data:
            out.append(d['embedding'])
        log(f'  EMB_TEXT chunk {ci+1}/{len(chunks)} n={len(chunk)} status=200 ms={res["ms"]}')
    return out


def encode_png_for_embedding(png_path, max_b64_bytes=90000, target_dim=400):
    from PIL import Image
    img = Image.open(png_path)
    if img.mode == 'RGBA':
        bg = Image.new('RGB', img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[3])
        img = bg
    elif img.mode != 'RGB':
        img = img.convert('RGB')
    if max(img.size) > target_dim:
        scale = target_dim / max(img.size)
        new_size = (int(img.size[0] * scale), int(img.size[1] * scale))
        img = img.resize(new_size, Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format='PNG', optimize=True)
    raw = buf.getvalue()
    b64 = base64.b64encode(raw).decode('utf-8')
    if len(b64) > max_b64_bytes:
        target_dim2 = int(target_dim * 0.7)
        if max(img.size) > target_dim2:
            scale = target_dim2 / max(img.size)
            new_size = (int(img.size[0] * scale), int(img.size[1] * scale))
            img = img.resize(new_size, Image.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, format='PNG', optimize=True)
        raw = buf.getvalue()
        b64 = base64.b64encode(raw).decode('utf-8')
    if len(b64) > max_b64_bytes:
        buf = io.BytesIO()
        img.save(buf, format='JPEG', quality=80)
        raw = buf.getvalue()
        b64 = base64.b64encode(raw).decode('utf-8')
        ext = 'jpeg'
    else:
        ext = 'png'
    return f'data:image/{ext};base64,{b64}', len(raw), len(b64)


def query_embedding_image(api_key, png_paths, model=MODEL_EMB, batch=EMB_BATCH):
    url = f'{BASE_URL}/embeddings'
    headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}
    chunks = [png_paths[i:i + batch] for i in range(0, len(png_paths), batch)]
    out = []
    for ci, chunk in enumerate(chunks):
        inputs = []
        for p in chunk:
            data_url, raw_size, b64_size = encode_png_for_embedding(p)
            inputs.append(data_url)
        payload = {'model': model, 'input': inputs}
        res = http_post(url, payload, headers, timeout=EMB_TIMEOUT)
        if res['status'] != 200:
            err = (res['error'] or '')[:300]
            raise RuntimeError(f'emb-img chunk {ci} status={res["status"]} error={err}')
        data = res['body'].get('data', [])
        data.sort(key=lambda x: x.get('index', 0))
        for d in data:
            out.append(d['embedding'])
        log(f'  EMB_IMAGE chunk {ci+1}/{len(chunks)} n={len(chunk)} status=200 ms={res["ms"]}')
    return out


# ============== Extractors ==============
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
    m = re.findall(r'\*\*\s*(-?\d+(?:\.\d+)?)\s*\*\*', s)
    if m:
        try:
            return float(m[-1])
        except Exception:
            pass
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


# ============== F-1: 6 embedding models 散射截面 ==============
def f1_compute_scatter_section():
    """Compute T/R/A for 6 embedding models using existing data only (0 new calls)."""
    log('F1_START 6 embedding models scatter section')
    out = {'models': [], 'best_model': None, 'verdict_counts': {}}
    
    # Load kmeans_k4_labels from volcengine 22cap (the only class info)
    volc_22 = json.load(open(VOLC_22CAP_REF, 'r', encoding='utf-8'))
    kmeans_labels = volc_22['kmeans_k4_labels']  # 22 captions → class 0/1/2/3
    concept_ids = [g['graph_id'] for g in volc_22['graphs']] if isinstance(volc_22.get('graphs'), list) else None
    # Fallback: use the keys from gt_class_names + per_class_members
    per_class = volc_22['per_class_members']  # {'L(llm_dag)': [...], 'S1(chain)': [...], ...}
    # Build caption_id → class_id mapping
    cid_to_class = {}
    for class_id, (class_name, members) in enumerate(per_class.items()):
        for m in members:
            cid_to_class[m] = class_id
    # Map 0-21 index to class_id using concept_ids order
    idx22 = volc_22.get('concept_ids', volc_22.get('gt_labels', list(range(22))))
    if concept_ids is None:
        # use index-based with kmeans_labels
        idx_to_class = {i: kmeans_labels[i] for i in range(22)}
    else:
        idx_to_class = {i: cid_to_class.get(concept_ids[i], 0) for i in range(22)}
    
    # Volcengine: use existing sim_matrix_stats directly
    volc_stats = volc_22['sim_matrix_stats']
    volc_ratio = volc_stats['ratio_intra_inter']
    volc_T = volc_ratio  # T = ratio (透射 = 信号)
    volc_R = 1.0 / volc_ratio  # R = 反射
    volc_A = 1.0 - volc_T - volc_R if volc_T + volc_R <= 1 else 0.0
    volc_verdict = ('MEANINGFUL' if volc_ratio > 1.5 
                    else 'GRAY' if volc_ratio >= 1.2 
                    else 'NOISE')
    out['models'].append({
        'name': 'doubao-embedding-vision-251215',
        'gateway': 'volcengine',
        'dim': 2048,
        'kind': 'text+image',
        'T': round(volc_T, 4),
        'R': round(volc_R, 4),
        'A': round(volc_A, 4),
        'ratio_intra_inter': round(volc_ratio, 4),
        'verdict': volc_verdict,
        'data_source': 'volcengine_22caption_embedding_2026_09_10.json (sim_matrix_stats)',
    })
    log(f'  volcengine: T={volc_T:.4f} R={volc_R:.4f} A={volc_A:.4f} ratio={volc_ratio:.4f} verdict={volc_verdict}')
    
    # OpenRouter 5 models: compute from per-cell top-3 sims
    or_data = json.load(open(OPENROUTER_5MODEL_REF, 'r', encoding='utf-8'))
    rag = or_data.get('rag_results', [])
    by_model = {}
    for r in rag:
        by_model.setdefault(r['model'], []).append(r)
    
    for m_info in F1_MODELS:
        name = m_info['name']
        if name == 'doubao-embedding-vision-251215':
            continue  # already done
        rs = by_model.get(name, [])
        # Compute per-cell sim profile
        # For each cell, get top-3 (caption_id, sim) and class of each
        # Compute intra-sim (sim of top-1 to its class centroid? Use volcengine's kmeans class) 
        # We have 22 captions; for each cell's top-3, the sim is to a specific caption
        # If multiple top-3 are in the same class → intra contribution
        # If top-3 span classes → inter contribution
        # Approximate ratio:
        #   intra_sim = mean(sim of top-3 in same class as top-1)
        #   inter_sim = mean(sim of top-3 in different class)
        intra_sims = []
        inter_sims = []
        all_top1_sims = []
        for r in rs:
            top3 = r.get('top3') or []
            if not top3:
                continue
            # top-1 class
            top1_cid = top3[0]['caption_id']
            top1_class = cid_to_class.get(top1_cid, -1)
            top1_sim = top3[0]['sim']
            all_top1_sims.append(top1_sim)
            for t in top3:
                cid = t['caption_id']
                cls = cid_to_class.get(cid, -1)
                if cls == top1_class and cls >= 0:
                    intra_sims.append(t['sim'])
                elif cls >= 0:
                    inter_sims.append(t['sim'])
        if intra_sims and inter_sims:
            intra_mean = sum(intra_sims) / len(intra_sims)
            inter_mean = sum(inter_sims) / len(inter_sims)
            ratio = intra_mean / (inter_mean + 1e-10)
        else:
            intra_mean = float('nan')
            inter_mean = float('nan')
            ratio = 1.0  # NOISE default
        
        # T/R/A derived
        T = ratio
        R = 1.0 / (ratio + 1e-10)
        A = 1.0 - T - R if T + R <= 1 else 0.0
        verdict = ('MEANINGFUL' if ratio > 1.5 
                   else 'GRAY' if ratio >= 1.2 
                   else 'NOISE')
        out['models'].append({
            'name': name,
            'gateway': 'openrouter',
            'dim': m_info['dim'],
            'kind': m_info['kind'],
            'T': round(T, 4),
            'R': round(R, 4),
            'A': round(A, 4),
            'ratio_intra_inter': round(ratio, 4),
            'intra_mean': round(intra_mean, 4) if intra_sims else None,
            'inter_mean': round(inter_mean, 4) if inter_sims else None,
            'verdict': verdict,
            'data_source': 'openrouter_5model_rag_30cells_2026_09_10.json (rag_results.top3, class from volcengine kmeans_k4)',
            'n_cells': len(rs),
            'top1_sim_mean': round(sum(all_top1_sims)/len(all_top1_sims), 4) if all_top1_sims else None,
        })
        log(f'  {name}: T={T:.4f} R={R:.4f} A={A:.4f} ratio={ratio:.4f} verdict={verdict} n_cells={len(rs)}')
    
    # Best model = highest T (透射最高)
    valid = [m for m in out['models'] if not np.isnan(m['T'])]
    if valid:
        best = max(valid, key=lambda x: x['T'])
        out['best_model'] = best['name']
    
    # Verdict counts
    vc = {}
    for m in out['models']:
        vc[m['verdict']] = vc.get(m['verdict'], 0) + 1
    out['verdict_counts'] = vc
    
    log(f'F1_DONE best_model={out["best_model"]} verdict_counts={vc}')
    return out


# ============== Feshbach on 2D SVD ==============
def feshbach_top3_text(caption_svd2, E_vec):
    S_bg = np.array(caption_svd2, dtype=float)
    W = S_bg.mean(axis=0)
    W_norm = np.linalg.norm(W)
    W_unit = W / (W_norm + 1e-10)
    proj_c = S_bg @ W_unit
    S_bg_perp = S_bg - np.outer(proj_c, W_unit)
    proj_E = E_vec @ W_unit
    E_perp = E_vec - proj_E * W_unit
    sim = S_bg_perp @ E_perp
    norms = np.linalg.norm(S_bg_perp, axis=1) * (np.linalg.norm(E_perp) + 1e-10) + 1e-10
    sim_n = sim / norms
    top_idx = np.argsort(-sim_n)[:TOP_K]
    return [(int(j), float(sim_n[j])) for j in top_idx]


def make_E_text(question_text, E_0):
    n_chars = len(question_text)
    n_words = len(question_text.split())
    raw = np.array([n_chars, n_words], dtype=float)
    raw = raw / (raw.max() + 1e-10)
    return raw * E_0


def image_pca2_top3(emb_image_arr, question_text):
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2, random_state=42)
    img2 = pca.fit_transform(emb_image_arr)
    E_0 = float(np.mean([np.linalg.norm(s) for s in img2]))
    n_chars = len(question_text)
    n_words = len(question_text.split())
    raw = np.array([n_chars, n_words], dtype=float)
    raw = raw / (raw.max() + 1e-10)
    E_vec = raw * E_0
    W = img2.mean(axis=0)
    W_n = np.linalg.norm(W)
    Wu = W / (W_n + 1e-10)
    proj_c = img2 @ Wu
    img2_perp = img2 - np.outer(proj_c, Wu)
    proj_E = E_vec @ Wu
    E_perp = E_vec - proj_E * Wu
    sim = img2_perp @ E_perp
    norms = np.linalg.norm(img2_perp, axis=1) * (np.linalg.norm(E_perp) + 1e-10) + 1e-10
    sim_n = sim / norms
    top_idx = np.argsort(-sim_n)[:TOP_K]
    return [(int(j), float(sim_n[j])) for j in top_idx]


# ============== Main ==============
def main():
    global LOG_FP
    os.makedirs(os.path.dirname(OUTPUT_LOG), exist_ok=True)
    LOG_FP = open(OUTPUT_LOG, 'w', encoding='utf-8')

    api_key, key_truncated = load_key()
    log(f'KEY_OK truncated={key_truncated} proxy_cleared')

    # 1) Anchor SHA
    anchor_path = r'D:\私人资料\deposon-repo\verifier\handoff\KT_ABC1_anchors_sha256_12.json'
    anchor_sha = hashlib.sha256(open(anchor_path, 'rb').read()).hexdigest()[:12]
    assert anchor_sha == '03c6c01f3697', f'5 锚 SHA 变: {anchor_sha}'
    log(f'ANCHOR_OK SHA-12={anchor_sha}')

    # 2) Sanity check
    log(f'SANITY_START model={MODEL_CHAT}')
    sanity = query_chat(api_key, SANITY_PROMPT, MODEL_CHAT, SANITY_MAX_TOKENS, SANITY_TIMEOUT)
    sanity_text = extract_text(sanity['body'])
    sanity_pass = sanity['status'] == 200 and len(sanity_text) > 0
    log(f'SANITY_DONE status={sanity["status"]} ms={sanity["ms"]} pass={sanity_pass} preview="{sanity_text[:60]}"')
    if not sanity_pass:
        log(f'SANITY_FAIL body={sanity["body"]} error={sanity["error"]}')
        # Continue but mark as failed

    # 3) Read corpus (read-only)
    idx = json.load(open(os.path.join(CORPUS_DIR, 'index.json'), 'r', encoding='utf-8'))
    assert idx['n_graphs'] == 22
    concept_ids = [g['graph_id'] for g in idx['graphs']]
    log(f'CORPUS_LOADED n_graphs=22 concept_ids[0:3]={concept_ids[:3]}')

    # 4) Reconstruct 22 captions
    captions = []
    for g in idx['graphs']:
        d = json.load(open(os.path.join(CORPUS_DIR, g['file']), 'r', encoding='utf-8'))
        labels = d.get('labels', [])
        cap = (f"Concept graph {g['graph_id']} "
               f"(family={g['family']}, structure={g['structure']}, "
               f"N={g['N']}, n_named={g['n_named']}): " + '; '.join(labels))
        captions.append(cap)
    log(f'CAPTIONS_BUILT n={len(captions)} sample_len={len(captions[0])}')

    # 5) Load 22 caption SVD 2D coords (from prior run, no re-embed)
    emb_ref = json.load(open(VOLC_22CAP_REF, 'r', encoding='utf-8'))
    svd2 = emb_ref['svd2_coords']  # dict caption_id -> [x, y]
    caption_svd2_2d = [svd2[cid] for cid in concept_ids]
    E_0_text = float(np.mean([np.linalg.norm(s) for s in np.array(caption_svd2_2d)]))
    log(f'SVD2_LOADED n={len(caption_svd2_2d)} E_0={E_0_text:.4f}')

    # 6) Re-embed 22 captions (text) for full 2048-d
    log('STEP1_TEXT_EMB_START')
    t0 = time.time()
    text_embs = query_embedding_text(api_key, captions)
    text_emb_arr = np.array(text_embs, dtype=np.float32)
    text_emb_dim = text_emb_arr.shape[1]
    text_emb_total_ms = round((time.time() - t0) * 1000, 1)
    log(f'STEP1_TEXT_EMB_DONE dim={text_emb_dim} total_ms={text_emb_total_ms}')

    # 7) Re-embed 22 images
    log('STEP2_IMAGE_EMB_START')
    png_paths = [os.path.join(PNG_DIR, f'graph_{i:03d}.png') for i in range(1, 23)]
    for p in png_paths:
        if not os.path.isfile(p):
            log(f'PNG missing: {p}')
            sys.exit(1)
    t0 = time.time()
    image_embs = query_embedding_image(api_key, png_paths)
    image_emb_arr = np.array(image_embs, dtype=np.float32)
    image_emb_dim = image_emb_arr.shape[1]
    image_emb_total_ms = round((time.time() - t0) * 1000, 1)
    log(f'STEP2_IMAGE_EMB_DONE dim={image_emb_dim} total_ms={image_emb_total_ms}')

    # 8) Load 30 new cells
    gsm8k = json.load(open(GSM8K_FILE, 'r', encoding='utf-8'))
    stq = json.load(open(STQ_FILE, 'r', encoding='utf-8'))
    new_cells = []
    for i in range(16, 16 + N_GSM8K_NEW):
        item = gsm8k.get(str(i), {})
        new_cells.append({'cell_id': f'gsm8k_{i}', 'task': 'gsm8k',
                          'question': item.get('question', ''), 'gold': item.get('answer', None)})
    for i in range(16, 16 + N_STQ_NEW):
        item = stq.get(str(i), {})
        new_cells.append({'cell_id': f'strategyqa_{i}', 'task': 'strategyqa',
                          'question': item.get('question', ''), 'gold': item.get('answer', None)})
    log(f'NEW_CELLS_LOADED total={len(new_cells)} gsm8k=16-{15+N_GSM8K_NEW} strategyqa=16-{15+N_STQ_NEW}')

    # 9) Init results
    results = {
        'timestamp': datetime.now(timezone(timedelta(hours=8))).isoformat(timespec='seconds'),
        'phase': 'V2 阶段 1: 60 cells 全量 + F-1 6 embedding 散射截面',
        'model_embedding': MODEL_EMB,
        'model_chat': MODEL_CHAT,
        'gateway': '火山方舟 Coding Plan',
        'base_url': BASE_URL,
        'auth': f'{key_truncated} (key loaded from env at runtime; literal key never written to disk)',
        'image_embedding_dim': int(image_emb_dim),
        'text_embedding_dim': int(text_emb_dim),
        'text_embedding_total_ms': text_emb_total_ms,
        'image_embedding_total_ms': image_emb_total_ms,
        'sanity_check': {
            'model': MODEL_CHAT,
            'prompt': SANITY_PROMPT,
            'http_status': sanity['status'],
            'latency_ms': sanity['ms'],
            'sanity_pass': sanity_pass,
        },
        'existing_30_cells': [],
        'new_30_cells': [],
        'phase1_f1_scatter': None,
        'summary': {
            'total_cells': 60,
            'gsm8k_total_passed': 0,
            'strategyqa_total_passed': 0,
            'total_passed': 0,
            'pass_rate': 0.0,
            'verdict': '',
        },
        'comparison': {},
        'constraints_honored': {
            'no_proxy': True,
            'key_runtime_only': True,
            'key_in_json_masked': True,
            'no_openrouter': True,
            'no_teamorouter': True,
            'no_v41_flash': True,
            'no_gpt6': True,
            'no_agent_plan': True,
            'no_retry': True,
            'frozen_files_untouched': [
                'verifier/handoff/KT_ABC1_anchors_sha256_12.json (SHA-12 03c6c01f3697 unchanged)',
                'corpus/v20/* (read-only)',
                '4 SPEC V0.1 frozen',
            ],
        },
    }
    
    def write_json():
        os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
        with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
    write_json()

    # 10) Load existing 30 cells from dpath
    dpath_ref = json.load(open(DPATH_REF, 'r', encoding='utf-8'))
    for c in dpath_ref.get('cells', []):
        results['existing_30_cells'].append({
            'cell_id': c['cell_id'],
            'task': c['task'],
            'chosen_channel': c['chosen_channel'],
            'is_correct': c['is_correct'],
            'llm_extracted': c['llm_extracted'],
            'gold': c['gold'],
            'latency_ms': c['latency_ms'],
            'note': c.get('note', ''),
        })
    log(f'EXISTING_30_LOADED from dpath_cross_modal_2026_09_10.json')

    # 11) Run 30 new cells
    log('CELL_LOOP_START total=30 new')
    for idx_c, c in enumerate(new_cells):
        cell_id = c['cell_id']
        task = c['task']
        question = c['question']
        gold = c['gold']

        # Text 通道: Feshbach on text 2D
        E_text = make_E_text(question, E_0_text)
        top_text = feshbach_top3_text(caption_svd2_2d, E_text)
        # Image 通道: PCA(22 image_emb) → 2D → Feshbach
        top_image = image_pca2_top3(image_emb_arr, question)
        # 谁得分高(对 top-1)就用谁
        text_top1 = top_text[0][1]
        image_top1 = top_image[0][1]
        if text_top1 >= image_top1:
            chosen = 'text'
            top3 = top_text
        else:
            chosen = 'image'
            top3 = top_image

        top3_records = []
        for j, score in top3:
            top3_records.append({
                'caption_id': concept_ids[j],
                'family': idx['graphs'][j]['family'],
                'structure': idx['graphs'][j]['structure'],
                'sim_score': score,
            })
        context_lines = [f"- {r['caption_id']} ({r['family']}/{r['structure']}, sim={r['sim_score']:.4f})"
                         for r in top3_records]
        context = '\n'.join(context_lines)
        if task == 'gsm8k':
            user_prompt = (
                f"Context (3 most relevant concept graphs, ranked by cross-modal similarity):\n"
                f"{context}\n\n"
                f"Source: {chosen} channel\n\n"
                f"Question: {question}\n\n"
                f"Let's think step by step.\n"
                f"Answer with one number only, ending with **N** format."
            )
        else:
            user_prompt = (
                f"Context (3 most relevant concept graphs, ranked by cross-modal similarity):\n"
                f"{context}\n\n"
                f"Source: {chosen} channel\n\n"
                f"Question: {question}\n\n"
                f"Let's think step by step.\n"
                f"Answer with Yes or No only, ending with **Yes** or **No** format."
            )

        log(f'CELL_START [{idx_c+1}/{len(new_cells)}] {cell_id} task={task} chosen={chosen} '
            f'top3_ids={[r["caption_id"] for r in top3_records]}')
        res = query_chat(api_key, user_prompt, MODEL_CHAT, CELL_MAX_TOKENS, CELL_TIMEOUT)
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
            'top_text': [{'caption_id': concept_ids[j], 'sim_score': s} for j, s in top_text],
            'top_image': [{'caption_id': concept_ids[j], 'sim_score': s} for j, s in top_image],
            'chosen_channel': chosen,
            'top3_records': top3_records,
            'llm_raw_response': raw_text[:2000],
            'llm_extracted': pred,
            'is_correct': is_correct,
            'latency_ms': res['ms'],
            'http_status': res['status'],
            'usage': (res['body'].get('usage', {}) if isinstance(res['body'], dict) else {}),
            'note': 'clean' if is_correct else ('fail' if res['status'] == 200 else f'error_{res["status"]}'),
            'error': res['error'],
        }
        results['new_30_cells'].append(cell_record)
        log(f'CELL_DONE [{idx_c+1}/{len(new_cells)}] {cell_id} pred={pred} gold={gold} '
            f'correct={is_correct} status={res["status"]} ms={res["ms"]}')
        write_json()

    # 12) Summary
    new_gsm_passed = sum(1 for c in results['new_30_cells'] if c['task'] == 'gsm8k' and c['is_correct'])
    new_stq_passed = sum(1 for c in results['new_30_cells'] if c['task'] == 'strategyqa' and c['is_correct'])
    new_total_passed = new_gsm_passed + new_stq_passed
    # Existing 30 from dpath: 14 + 11 = 25 passed (86.7% baseline = 26)
    exist_gsm_passed = sum(1 for c in results['existing_30_cells'] if c['task'] == 'gsm8k' and c['is_correct'])
    exist_stq_passed = sum(1 for c in results['existing_30_cells'] if c['task'] == 'strategyqa' and c['is_correct'])
    exist_total_passed = exist_gsm_passed + exist_stq_passed
    total_passed = exist_total_passed + new_total_passed
    pass_rate = total_passed / 60
    if pass_rate >= 0.85:
        verdict = 'STRONG_PASS'
    elif pass_rate >= 0.80:
        verdict = 'PASS'
    elif pass_rate >= 0.60:
        verdict = 'MARGINAL'
    else:
        verdict = 'FAIL'
    results['summary'] = {
        'total_cells': 60,
        'existing_30_passed': exist_total_passed,
        'new_30_passed': new_total_passed,
        'gsm8k_total_passed': (sum(1 for c in results['existing_30_cells']+results['new_30_cells'] 
                                    if c['task']=='gsm8k' and c['is_correct'])),
        'strategyqa_total_passed': (sum(1 for c in results['existing_30_cells']+results['new_30_cells'] 
                                         if c['task']=='strategyqa' and c['is_correct'])),
        'total_passed': total_passed,
        'pass_rate': round(pass_rate, 4),
        'verdict': verdict,
    }
    results['comparison'] = {
        'no_rag_baseline_2_0_lite': '52/60 = 86.7% (projected, same as 30 baseline)',
        'dpath_30cells_pass_rate': f'{exist_total_passed}/30 = {exist_total_passed/30*100:.1f}% (from 2026_09_10)',
        'v2_60cells_pass_rate': f'{total_passed}/60 = {pass_rate*100:.1f}%',
        'delta_vs_30': f'{(total_passed/60 - exist_total_passed/30)*100:+.1f}pp',
    }
    write_json()
    log(f'SUMMARY_DONE existing_30={exist_total_passed} new_30={new_total_passed} '
        f'total={total_passed}/60 verdict={verdict}')

    # 13) F-1 scatter section
    f1 = f1_compute_scatter_section()
    results['phase1_f1_scatter'] = f1
    write_json()

    # 14) Channel usage
    text_chosen = sum(1 for c in results['new_30_cells'] if c['chosen_channel'] == 'text')
    image_chosen = sum(1 for c in results['new_30_cells'] if c['chosen_channel'] == 'image')
    log(f'CHANNEL_USAGE new30 text={text_chosen} image={image_chosen}')

    log('DONE')
    if LOG_FP is not None:
        LOG_FP.close()
    return 0


if __name__ == '__main__':
    sys.exit(main())
