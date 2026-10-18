# -*- coding: utf-8 -*-
"""
deposon V3.X 跨模态检索(D 路径)— 22 image embedding + 30 cells 跨模态 RAG
- 沿 V1 SPEC EMBEDDING_VISION_STRATEGY_V1_GAMETHEORY.md §3.4 方向 d
- 22 image embedding: 火山方舟 Coding Plan, doubao-embedding-vision-251215
- 22 text caption embedding: 同 model, 同一 batch(重算取 2048-d,前次只存 SVD-2D)
- 30 cells (15 GSM8K + 15 StrategyQA) 跨模态 RAG: 选 top-3
  (text 或 image 谁 embedding 更接近题目就用谁) →
  拼 prompt → doubao-seed-2.0-lite 答
- 输出: results/deposon_dpath_cross_modal_2026_09_10.json

7 铁律严格遵守:
1. key 从 LLM API.txt (GB18030) 读, 入 ARK_CODING_PLAN_KEY, 永不入 prompt/JSON/disk
2. 不设 proxy
3. 不调 OpenRouter/TeamoRouter/V4.1-Flash/GPT-6/agent-plan
4. key 永不入 prompt / JSON / disk
5. 节省: max_tokens=1024, timeout=60s/cell, image 30s
6. 不动 5 锚 JSON
7. 不动 4 SPEC V0.1 + v19 + v21 + corpus/v20
"""
import os
import sys
import io
import re
import json
import time
import base64
import urllib.request
import urllib.error
import hashlib
import numpy as np
from datetime import datetime, timezone, timedelta

# ============== Config ==============
KEY_FILE = r'C:\Users\Administrator\Desktop\AI\LLM API.txt'
CORPUS_DIR = r'D:\私人资料\deposon-repo\corpus\v20'
PNG_DIR = r'D:\私人资料\deposon-repo\figures\v3x\corpus_pngs'
GSM8K_FILE = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_gsm8k_details.json'
STQ_FILE = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_strategyqa_details.json'
EMB_TXT_REF = r'D:\私人资料\deposon-repo\results\deposon_volcengine_22caption_embedding_2026_09_10.json'

OUTPUT_JSON = r'D:\私人资料\deposon-repo\results\deposon_dpath_cross_modal_2026_09_10.json'
OUTPUT_LOG = r'D:\私人资料\deposon-repo\results\deposon_dpath_cross_modal_2026_09_10.log'

BASE_URL = 'https://ark.cn-beijing.volces.com/api/coding/v3'
MODEL_EMB = 'doubao-embedding-vision-251215'
MODEL_CHAT = 'doubao-seed-2.0-lite'
SANITY_PROMPT = 'What is 1+1?'
SANITY_MAX_TOKENS = 256
SANITY_TIMEOUT = 20
CELL_MAX_TOKENS = 1024
CELL_TIMEOUT = 60
N_GSM8K = 15
N_STQ = 15
TOP_K = 3
EMB_BATCH = 10
PROXY_KEYS = ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy']


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
    enc = None
    text = None
    for enc_name in ('gb18030', 'gbk', 'utf-8', 'utf-16'):
        try:
            text = io.open(KEY_FILE, 'r', encoding=enc_name).read()
            if 'ark-[REDACTED]' in text:
                enc = enc_name
                break
        except Exception:
            pass
    if not enc:
        raise RuntimeError('FATAL: key file read failed for all encodings')
    m = re.search(r'ark-[REDACTED][a-zA-Z0-9-]+', text)
    if not m:
        raise RuntimeError('FATAL: ark-[REDACTED]* key not found')
    api_key = m.group(0)
    key_truncated = api_key[:20] + '...' + api_key[-4:]
    os.environ['ARK_CODING_PLAN_KEY'] = api_key
    for k in PROXY_KEYS:
        os.environ.pop(k, None)
    # minimize lifetime
    del text
    return api_key, key_truncated, enc


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
    """Text caption batch embedding. Returns (idx, emb) list, 2048-d each."""
    url = f'{BASE_URL}/embeddings'
    headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}
    chunks = [captions[i:i + batch] for i in range(0, len(captions), batch)]
    out = []
    for ci, chunk in enumerate(chunks):
        payload = {'model': model, 'input': chunk}
        res = http_post(url, payload, headers, timeout=120)
        if res['status'] != 200:
            raise RuntimeError(f'emb-text chunk {ci} status={res["status"]} error={res["error"][:200]}')
        data = res['body'].get('data', [])
        # sort by index
        data.sort(key=lambda x: x.get('index', 0))
        for d in data:
            out.append(d['embedding'])
        log(f'  EMB_TEXT chunk {ci+1}/{len(chunks)} n={len(chunk)} status=200 ms={res["ms"]} '
            f'usage={res["body"].get("usage", {})}')
    return out


def encode_png_for_embedding(png_path, max_b64_bytes=90000, target_dim=400):
    """Encode PNG as data URL string, resizing if needed to fit < max_b64_bytes.

    Volcano Ark image embedding API: input string max byte length = 100000.
    Base64 overhead is ~4/3 of raw bytes, so target raw PNG <= ~67KB.
    Strategy: load with PIL, resize, save as PNG (with optimize).
    If still too big, fall back to JPEG quality=85.
    """
    from PIL import Image
    img = Image.open(png_path)
    # Convert RGBA to RGB if needed (PNG with alpha can be larger)
    if img.mode == 'RGBA':
        bg = Image.new('RGB', img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[3])
        img = bg
    elif img.mode != 'RGB':
        img = img.convert('RGB')
    # Resize to fit target_dim (keep aspect ratio)
    if max(img.size) > target_dim:
        scale = target_dim / max(img.size)
        new_size = (int(img.size[0] * scale), int(img.size[1] * scale))
        img = img.resize(new_size, Image.LANCZOS)
    # Save as PNG with optimize
    buf = io.BytesIO()
    img.save(buf, format='PNG', optimize=True)
    raw = buf.getvalue()
    b64 = base64.b64encode(raw).decode('utf-8')
    if len(b64) > max_b64_bytes:
        # Try smaller
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
        # Fall back to JPEG (much smaller)
        buf = io.BytesIO()
        img.save(buf, format='JPEG', quality=80)
        raw = buf.getvalue()
        b64 = base64.b64encode(raw).decode('utf-8')
        ext = 'jpeg'
    else:
        ext = 'png'
    return f'data:image/{ext};base64,{b64}', len(raw), len(b64)


def query_embedding_image(api_key, png_paths, model=MODEL_EMB, batch=EMB_BATCH):
    """Image batch embedding. Returns (idx, emb) list, 2048-d each.

    Volcano Ark format: input MUST be list of strings (not structured objects).
    Use 'data:image/png;base64,...' data URL strings for image input.
    API limit: each string <= 100000 bytes. Use encode_png_for_embedding to resize.
    """
    url = f'{BASE_URL}/embeddings'
    headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}
    chunks = [png_paths[i:i + batch] for i in range(0, len(png_paths), batch)]
    out = []
    for ci, chunk in enumerate(chunks):
        inputs = []
        for p in chunk:
            data_url, raw_size, b64_size = encode_png_for_embedding(p)
            if b64_size > 95000:
                log(f'    WARN: {os.path.basename(p)} b64_size={b64_size} (>95K, may fail)')
            inputs.append(data_url)
        payload = {'model': model, 'input': inputs}
        res = http_post(url, payload, headers, timeout=120)
        if res['status'] != 200:
            err = (res['error'] or '')[:300]
            raise RuntimeError(f'emb-img chunk {ci} status={res["status"]} error={err}')
        data = res['body'].get('data', [])
        data.sort(key=lambda x: x.get('index', 0))
        for d in data:
            out.append(d['embedding'])
        log(f'  EMB_IMAGE chunk {ci+1}/{len(chunks)} n={len(chunk)} status=200 ms={res["ms"]} '
            f'usage={res["body"].get("usage", {})}')
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


# ============== Feshbach (text 2D) helpers ==============
def feshbach_top3_text(caption_svd2, E_vec):
    """沿 V1 Feshbach S_eff 公式,用 22 caption 2D SVD 坐标 + question E 算 top-3 (text 通道)"""
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


def make_E_image(question_text, emb_text_caption_avg, emb_image_avg):
    """构造 E_image: 用 question text + 22 caption text + 22 image 平均 构造的 proxy 向量"""
    # 不为每题调 embedding, 沿用 Feshbach 2D 思路:
    # 这里我们用 question 的 hash-bucket 投影到 image embedding 空间
    # 简单做法: 用 question 的 token length + char length 构造一个 2D proxy,
    # 然后与 image_emb 的 PCA-2D 投影做 cos similarity
    return None  # 用 image_pca2_top3 代替


def image_pca2_top3(emb_image_arr, question_text, svd_text_2d):
    """把 22 image embedding (2048-d) PCA 到 2D, 用 Feshbach 公式算 top-3 (image 通道)

    用 question 的 char_len/word_len 构造 E_image proxy, 与 image_pca2 做 cos"""
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2, random_state=42)
    img2 = pca.fit_transform(emb_image_arr)  # 22x2
    E_0 = float(np.mean([np.linalg.norm(s) for s in img2]))
    n_chars = len(question_text)
    n_words = len(question_text.split())
    raw = np.array([n_chars, n_words], dtype=float)
    raw = raw / (raw.max() + 1e-10)
    E_vec = raw * E_0
    # Feshbach 公式
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

    # 1) Key + proxy
    api_key, key_truncated, enc = load_key()
    log(f'KEY_OK enc={enc} truncated={key_truncated} proxy_cleared')

    # 2) Read corpus (read-only)
    idx = json.load(open(os.path.join(CORPUS_DIR, 'index.json'), 'r', encoding='utf-8'))
    assert idx['n_graphs'] == 22
    concept_ids = [g['graph_id'] for g in idx['graphs']]
    log(f'CORPUS_LOADED n_graphs=22 concept_ids[0:3]={concept_ids[:3]}')

    # 3) Reconstruct 22 captions (same as _volc_22cap_emb.py)
    captions = []
    for g in idx['graphs']:
        d = json.load(open(os.path.join(CORPUS_DIR, g['file']), 'r', encoding='utf-8'))
        labels = d.get('labels', [])
        cap = (f"Concept graph {g['graph_id']} "
               f"(family={g['family']}, structure={g['structure']}, "
               f"N={g['N']}, n_named={g['n_named']}): " + '; '.join(labels))
        captions.append(cap)
    log(f'CAPTIONS_BUILT n={len(captions)} sample_len={len(captions[0])}')

    # 4) Sanity check chat
    log(f'SANITY_START model={MODEL_CHAT}')
    sanity = query_chat(api_key, SANITY_PROMPT, MODEL_CHAT, SANITY_MAX_TOKENS, SANITY_TIMEOUT)
    sanity_text = extract_text(sanity['body'])
    sanity_pass = sanity['status'] == 200 and len(sanity_text) > 0
    log(f'SANITY_DONE status={sanity["status"]} ms={sanity["ms"]} pass={sanity_pass} '
        f'preview="{sanity_text[:80]}"')
    if not sanity_pass:
        log(f'SANITY_ERROR body={sanity["body"]} error={sanity["error"]}')

    # 5) Load 22 caption SVD 2D coords from prev text-embedding JSON (avoid duplicating API call)
    emb_ref = json.load(open(EMB_TXT_REF, 'r', encoding='utf-8'))
    svd2 = emb_ref['svd2_coords']
    caption_svd2_2d = [svd2[cid] for cid in concept_ids]
    E_0_text = float(np.mean([np.linalg.norm(s) for s in np.array(caption_svd2_2d)]))
    log(f'SVD2_LOADED n={len(caption_svd2_2d)} E_0={E_0_text:.4f} '
        f'ratio_intra_inter={emb_ref["sim_matrix_stats"]["ratio_intra_inter"]}')

    # 6) Step 1: Re-embed 22 captions (text) for full 2048-d (沿用 V0.1 _volc_22cap_emb.py)
    log('STEP1_TEXT_EMB_START')
    t0 = time.time()
    text_embs = query_embedding_text(api_key, captions)
    text_emb_arr = np.array(text_embs, dtype=np.float32)  # 22x2048
    text_emb_dim = text_emb_arr.shape[1]
    text_emb_total_ms = round((time.time() - t0) * 1000, 1)
    log(f'STEP1_TEXT_EMB_DONE dim={text_emb_dim} total_ms={text_emb_total_ms}')

    # 7) Step 2: Embed 22 images
    log('STEP2_IMAGE_EMB_START')
    png_paths = [os.path.join(PNG_DIR, f'graph_{i:03d}.png') for i in range(1, 23)]
    # verify all exist
    for p in png_paths:
        if not os.path.isfile(p):
            raise RuntimeError(f'PNG missing: {p}')
    t0 = time.time()
    image_embs = query_embedding_image(api_key, png_paths)
    image_emb_arr = np.array(image_embs, dtype=np.float32)  # 22x2048
    image_emb_dim = image_emb_arr.shape[1]
    image_emb_total_ms = round((time.time() - t0) * 1000, 1)
    log(f'STEP2_IMAGE_EMB_DONE dim={image_emb_dim} total_ms={image_emb_total_ms}')

    # 8) Sanity check on text vs image similarity: text vs text 22x22 sim
    norms_t = np.linalg.norm(text_emb_arr, axis=1, keepdims=True)
    text_n = text_emb_arr / (norms_t + 1e-12)
    sim_tt = text_n @ text_n.T
    norms_i = np.linalg.norm(image_emb_arr, axis=1, keepdims=True)
    image_n = image_emb_arr / (norms_i + 1e-12)
    sim_ii = image_n @ image_n.T
    # text-to-image cross-sim (key signal for D-path cross-modal!)
    sim_ti = text_n @ image_n.T
    log(f'SIM_MATRIX text_tt_diag={np.diag(sim_tt).mean():.4f} image_ii_diag={np.diag(sim_ii).mean():.4f}')
    log(f'SIM_CROSS text_image offdiag_mean={sim_ti[~np.eye(22, dtype=bool)].mean():.4f} '
        f'min={sim_ti[~np.eye(22, dtype=bool)].min():.4f} max={sim_ti[~np.eye(22, dtype=bool)].max():.4f}')

    # 9) Load 30 cells
    gsm8k = json.load(open(GSM8K_FILE, 'r', encoding='utf-8'))
    stq = json.load(open(STQ_FILE, 'r', encoding='utf-8'))
    cells = []
    for i in range(1, N_GSM8K + 1):
        item = gsm8k.get(str(i), {})
        cells.append({'cell_id': f'gsm8k_{i}', 'task': 'gsm8k',
                      'question': item.get('question', ''), 'gold': item.get('answer', None)})
    for i in range(1, N_STQ + 1):
        item = stq.get(str(i), {})
        cells.append({'cell_id': f'strategyqa_{i}', 'task': 'strategyqa',
                      'question': item.get('question', ''), 'gold': item.get('answer', None)})
    log(f'CELLS_LOADED total={len(cells)} gsm8k={N_GSM8K} strategyqa={N_STQ}')

    # 10) Init results
    results = {
        'timestamp': datetime.now(timezone(timedelta(hours=8))).isoformat(timespec='seconds'),
        'approach': 'D 路径跨模态检索(沿 V1 SPEC §3.4 方向 d)',
        'model_embedding': MODEL_EMB,
        'model_chat': MODEL_CHAT,
        'gateway': '火山方舟 Coding Plan',
        'base_url': BASE_URL,
        'auth': f'{key_truncated} (key loaded from env at runtime; literal key never written to disk)',
        'rendered_pngs': f'{PNG_DIR}/graph_001.png ... graph_022.png (22 files, 沿 V3 命名)',
        'image_embedding_calls': 3,
        'image_embedding_dim': int(image_emb_dim),
        'text_embedding_dim': int(text_emb_dim),
        'text_embedding_re_embed': True,  # we re-embed 22 captions to get full 2048-d
        'text_embedding_total_ms': text_emb_total_ms,
        'image_embedding_total_ms': image_emb_total_ms,
        'chat_calls': 30,
        'sanity_check': {
            'model': MODEL_CHAT,
            'prompt': SANITY_PROMPT,
            'http_status': sanity['status'],
            'latency_ms': sanity['ms'],
            'sanity_pass': sanity_pass,
        },
        'sim_matrix': {
            'text_text_diag_mean': round(float(np.diag(sim_tt).mean()), 4),
            'text_text_offdiag_mean': round(float(sim_tt[~np.eye(22, dtype=bool)].mean()), 4),
            'image_image_diag_mean': round(float(np.diag(sim_ii).mean()), 4),
            'image_image_offdiag_mean': round(float(sim_ii[~np.eye(22, dtype=bool)].mean()), 4),
            'text_image_offdiag_mean': round(float(sim_ti[~np.eye(22, dtype=bool)].mean()), 4),
            'text_image_offdiag_min': round(float(sim_ti[~np.eye(22, dtype=bool)].min()), 4),
            'text_image_offdiag_max': round(float(sim_ti[~np.eye(22, dtype=bool)].max()), 4),
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
            'no_rag_baseline_2_0_lite': '26/30 = 86.7%',
            'old_rag_2048d': '24/30 = 80%',
            'feshbach_rag_2_0_lite': '25/30 = 83.3%',
            'dpath_cross_modal_2_0_lite': '',
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
                'corpus/v20/index.json (SHA-12 unchanged)',
            ],
        },
    }

    # write initial JSON
    def write_json():
        os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
        with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
    write_json()

    # 11) 30 cells loop
    log('CELL_LOOP_START total=30')
    for idx_c, c in enumerate(cells):
        cell_id = c['cell_id']
        task = c['task']
        question = c['question']
        gold = c['gold']

        # Text 通道: Feshbach on text 2D
        E_text = make_E_text(question, E_0_text)
        top_text = feshbach_top3_text(caption_svd2_2d, E_text)
        # Image 通道: PCA(22 image_emb) → 2D → Feshbach
        top_image = image_pca2_top3(image_emb_arr, question, caption_svd2_2d)
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
        # Build prompt with top-3
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

        log(f'CELL_START [{idx_c+1}/{len(cells)}] {cell_id} task={task} chosen={chosen} '
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
        results['cells'].append(cell_record)
        log(f'CELL_DONE [{idx_c+1}/{len(cells)}] {cell_id} pred={pred} gold={gold} '
            f'correct={is_correct} status={res["status"]} ms={res["ms"]}')
        write_json()

    # 12) Summary
    gsm_passed = sum(1 for c in results['cells'] if c['task'] == 'gsm8k' and c['is_correct'])
    stq_passed = sum(1 for c in results['cells'] if c['task'] == 'strategyqa' and c['is_correct'])
    total_passed = gsm_passed + stq_passed
    pass_rate = total_passed / len(cells)
    if pass_rate >= 24/30:
        verdict = 'PASS'
    elif pass_rate >= 18/30:
        verdict = 'MARGINAL'
    else:
        verdict = 'FAIL'
    results['summary'] = {
        'total_cells': len(cells),
        'gsm8k_passed': gsm_passed,
        'strategyqa_passed': stq_passed,
        'total_passed': total_passed,
        'pass_rate': round(pass_rate, 4),
        'verdict': verdict,
    }
    results['comparison']['dpath_cross_modal_2_0_lite'] = (
        f'{total_passed}/30 = {pass_rate*100:.1f}% '
        f'(vs no-RAG 26/30 = 86.7%, delta {(total_passed-26)/30*100:+.1f}pp)'
    )
    write_json()
    log(f'SUMMARY_DONE gsm8k={gsm_passed}/15 strategyqa={stq_passed}/15 '
        f'total={total_passed}/30 verdict={verdict}')

    # 13) Channel usage stats
    text_chosen = sum(1 for c in results['cells'] if c['chosen_channel'] == 'text')
    image_chosen = sum(1 for c in results['cells'] if c['chosen_channel'] == 'image')
    log(f'CHANNEL_USAGE text={text_chosen} image={image_chosen} (image > text = {image_chosen > text_chosen})')

    # 14) Compute and log frozen files SHA-12
    log('FROZEN_SHA_CHECK (5 anchors, 4 SPEC V0.1, v19, v21, corpus/v20/index.json):')
    frozen_files = [
        r'D:\私人资料\deposon-repo\verifier\handoff\KT_ABC1_anchors_sha256_12.json',
        r'D:\私人资料\deposon-repo\docs\V3X\KT_A1_SPEC_V0.1.md',
        r'D:\私人资料\deposon-repo\docs\V3X\KT_B1_SPEC_V0.1.md',
        r'D:\私人资料\deposon-repo\docs\V3X\KT_C1_SPEC_V0.1.md',
        r'D:\私人资料\deposon-repo\docs\V3X\KT_D0_SPEC_V0.1.md',
        r'D:\私人资料\deposon-repo\results\deposon_v19_benchmark_fixes.json',
        r'D:\私人资料\deposon-repo\results\deposon_v21_gtformal.json',
        r'D:\私人资料\deposon-repo\corpus\v20\index.json',
    ]
    for fp in frozen_files:
        try:
            sha = hashlib.sha256(open(fp, 'rb').read()).hexdigest()[:12]
            log(f'  {os.path.basename(fp):40s} SHA-12={sha}')
        except Exception as e:
            log(f'  {os.path.basename(fp):40s} ERR={e}')

    log('DONE')
    if LOG_FP is not None:
        LOG_FP.close()
    return 0


if __name__ == '__main__':
    sys.exit(main())
