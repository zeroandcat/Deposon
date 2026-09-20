# -*- coding: utf-8 -*-
"""
V3X 6-Direction Comprehensive Verification (2026-09-10)
========================================================
6 directions:
  A. Deposon-aware Embedding (2048d → 3D T+R+A)
  B. 3-channel LLM inference evaluation (T/R/A breakdown of V4.1-Flash 25/30)
  C. Deposon scattering field replaces RAG (主推)
  D. LLM inference = scattering operator (S_eff(E) analogy)
  E. V3X distortion bound (T+R+A conservation)
  F. Deposon-aware LLM eval + Embedding integrated (终极形式)

Stages:
  1. theoretical analysis (A, B, D, E, F): 5-10 min
  2. 22 caption Deposon-aware Embedding 3D projection + KMeans: 5-10 min
  3. Deposon-aware RAG 30 cells re-test (doubao-seed-code-preview-251028): 5-15 min
  4. comprehensive report: 5-10 min

7 铁律 (hard rules):
  1. coding-plan key runtime read from LLM API.txt (GB18030)
  2. no proxy
  3. do NOT call OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan
  4. key never in prompt / JSON / disk (auth field mask only)
  5. do NOT switch model (stage 3: strict doubao-seed-code-preview-251028)
  6. do NOT touch 5 anchor JSON (verifier/handoff/KT_ABC1_anchors_sha256_12.json)
  7. do NOT touch 4 SPEC V0.1 frozen + v19/v21 frozen JSON
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
# Per previous worker sanity report: the SECOND ark key is the verified 3/3 PASS
# (the first is stale: 401 Unauthorized)
all_ark = re.findall(r'ark-[a-zA-Z0-9-]+', key_text)
if not all_ark:
    print("[FATAL] no ark key in LLM API.txt", file=sys.stderr)
    sys.exit(1)
API_KEY = all_ark[1] if len(all_ark) >= 2 else all_ark[0]
KEY_MASK = API_KEY[:4] + '...' + API_KEY[-4:] if len(API_KEY) >= 8 else 'ark-...'
os.environ['ARK_CODING_PLAN_KEY'] = API_KEY
del key_text

# No proxy
for p in ('HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy'):
    os.environ.pop(p, None)

print(f"[INIT] key loaded: len={len(API_KEY)} mask={KEY_MASK}")
print(f"[INIT] proxy cleared: HTTP_PROXY/HTTPS_PROXY etc all popped")
print(f"[INIT] 7 铁律 honored (no model switch / no proxy / no 5-anchor touch)")

# ---------------- 1. Constants ----------------
CORPUS_DIR = r'D:\私人资料\deposon-repo\corpus\v20'
GSM8K_PATH = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_gsm8k_details.json'
STRATEGYQA_PATH = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_strategyqa_details.json'
EMBED_ENDPOINT = 'https://ark.cn-beijing.volces.com/api/coding/v3/embeddings'
CHAT_ENDPOINT = 'https://ark.cn-beijing.volces.com/api/coding/v3/chat/completions'
EMBED_MODEL = 'doubao-embedding-vision-251215'
CHAT_MODEL = 'doubao-seed-code-preview-251028'  # strict, no switch
MAX_TOKENS_CHAT = 2048
TIMEOUT_S = 120


# ---------------- Helpers ----------------
def query_embed(inputs, model=EMBED_MODEL, timeout=TIMEOUT_S):
    """One call to embeddings API. Returns (data, latency_ms, status, err)."""
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


def query_chat(prompt, model=CHAT_MODEL, max_tokens=MAX_TOKENS_CHAT, timeout=TIMEOUT_S):
    """One call to chat completions API."""
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


# ---------------- 2. Reconstruct 22 captions ----------------
print("\n[CAPTIONS] reconstructing from corpus/v20/index.json + per-graph labels (read-only)")
index = json.load(open(os.path.join(CORPUS_DIR, 'index.json'), encoding='utf-8'))
assert index['n_graphs'] == 22
captions = []
concept_ids = []
for g in index['graphs']:
    d = json.load(open(os.path.join(CORPUS_DIR, g['file']), encoding='utf-8'))
    labels = d.get('labels', [])
    cap = (f"Concept graph {g['graph_id']} "
           f"(family={g['family']}, structure={g['structure']}, "
           f"N={g['N']}, n_named={g['n_named']}): " + '; '.join(labels))
    captions.append(cap)
    concept_ids.append(g['graph_id'])
print(f"[CAPTIONS] reconstructed 22 captions")


# ---------------- 3. Re-fetch 22 caption embeddings (2048d) ----------------
# Stage 2 需要完整 2048-d 投影到 3D T+R+A。原 JSON 只有 SVD2 坐标,没有 2048-d。
# 必须重 fetch,1 逻辑 batch (3 chunk: 10+10+2),与之前一致。
print("\n[STAGE 2 PREP] re-fetching 22 caption embeddings (2048d) for 3D T+R+A projection")
CHUNK = 10
chunks = [captions[i:i + CHUNK] for i in range(0, len(captions), CHUNK)]
all_emb_data = []
total_lat = 0.0
for ci, chunk in enumerate(chunks):
    body, lat, status, err = query_embed(chunk)
    if status != 200 or not body:
        print(f"[FATAL] embed chunk {ci+1} status={status} err={(err or '')[:300]}")
        sys.exit(2)
    emb_data = body.get('data', [])
    all_emb_data.extend(emb_data)
    total_lat += lat
    print(f"  chunk {ci+1}/{len(chunks)} status=200 latency={lat:.1f}ms")
    time.sleep(0.3)
all_emb_data.sort(key=lambda x: x.get('index', 0))
embs_22 = np.array([item['embedding'] for item in all_emb_data], dtype=np.float32)
assert embs_22.shape == (22, 2048), f"bad shape: {embs_22.shape}"
print(f"[EMB 22] shape={embs_22.shape} total_latency={total_lat:.1f}ms")
del all_emb_data  # free


# ---------------- 4. Stage 2: 3D T+R+A projection + KMeans ----------------
def deposon_project(embs, n_components=2):
    """
    Deposon 3D T+R+A 投影:
    - PCA 取 n_components 主方向 -> T+R 通道
    - 残差方差 -> A 通道(凝华)
    - T 沿最大方向 / R 沿次大方向 / A 沿剩余
    - 归一化: T + R + A = 1
    """
    from sklearn.decomposition import PCA
    pca = PCA(n_components=n_components)
    proj = pca.fit_transform(embs)  # (N, n_components)
    full_var = (embs ** 2).sum(axis=1)  # |x|² 总方差
    proj_var = (proj ** 2).sum(axis=1)
    A_var = np.maximum(full_var - proj_var, 0)  # 凝华方差
    T_var = (proj[:, 0] ** 2)  # 沿最大方向 = T(透射)
    R_var = (proj[:, 1] ** 2) if n_components >= 2 else np.zeros_like(T_var)
    total = T_var + R_var + A_var + 1e-10
    T = T_var / total
    R = R_var / total
    A = A_var / total
    return T, R, A, proj


print("\n[STAGE 2] 22 caption Deposon-aware 3D T+R+A projection ...")
T_22, R_22, A_22, proj_22 = deposon_project(embs_22, n_components=2)
print(f"  T  mean={T_22.mean():.4f}  std={T_22.std():.4f}  range=[{T_22.min():.4f}, {T_22.max():.4f}]")
print(f"  R  mean={R_22.mean():.4f}  std={R_22.std():.4f}  range=[{R_22.min():.4f}, {R_22.max():.4f}]")
print(f"  A  mean={A_22.mean():.4f}  std={A_22.std():.4f}  range=[{A_22.min():.4f}, {A_22.max():.4f}]")

# T+R+A = 1 校验
conservation_check = T_22 + R_22 + A_22
print(f"  T+R+A  mean={conservation_check.mean():.6f}  max_dev={np.abs(conservation_check - 1).max():.2e}")

# GT 4 class labels (per existing JSON)
gt_labels_22 = []
for g in index['graphs']:
    if g['family'] == 'L':
        gt_labels_22.append(0)
    elif g['graph_id'].startswith('S1'):
        gt_labels_22.append(1)
    elif g['graph_id'].startswith('S2'):
        gt_labels_22.append(2)
    else:
        gt_labels_22.append(3)
class_names_22 = ['L(llm_dag)', 'S1(chain)', 'S2(tree)', 'S3-S6(misc)']
print(f"  GT: L=6 S1=4 S2=5 S3-S6=7")


# ---- T-channel intra/inter class ----
# Deposon-aware Embedding 核心:在 T 通道上做 intra/inter class ratio
def channel_ratio(channel_values, gt):
    intra = []
    inter = []
    n = len(gt)
    for i in range(n):
        for j in range(i + 1, n):
            if gt[i] == gt[j]:
                intra.append(channel_values[i])
            else:
                inter.append(channel_values[i])
    intra_avg = float(np.mean(intra)) if intra else 0.0
    inter_avg = float(np.mean(inter)) if inter else 0.0
    return intra_avg, inter_avg, intra_avg / inter_avg if inter_avg > 1e-9 else 0.0


T_intra, T_inter, T_ratio = channel_ratio(T_22, gt_labels_22)
R_intra, R_inter, R_ratio = channel_ratio(R_22, gt_labels_22)
A_intra, A_inter, A_ratio = channel_ratio(A_22, gt_labels_22)
print(f"\n[STAGE 2: T-R-A channel intra/inter ratio]")
print(f"  T:  intra={T_intra:.4f}  inter={T_inter:.4f}  ratio={T_ratio:.4f}")
print(f"  R:  intra={R_intra:.4f}  inter={R_inter:.4f}  ratio={R_ratio:.4f}")
print(f"  A:  intra={A_intra:.4f}  inter={A_inter:.4f}  ratio={A_ratio:.4f}")

# Cosine sim baseline (for comparison with T channel)
norms_22 = np.linalg.norm(embs_22, axis=1, keepdims=True)
embs_22_n = embs_22 / (norms_22 + 1e-12)
sim_22 = embs_22_n @ embs_22_n.T
cos_intra, cos_inter, cos_ratio = channel_ratio(sim_22[np.triu_indices(22, k=1)], 
                                                  np.array([gt_labels_22[i] for i in range(22) for j in range(i+1, 22)]))
print(f"  Cosine:  intra={cos_intra:.4f}  inter={cos_inter:.4f}  ratio={cos_ratio:.4f}")


# ---- KMeans k=4 on T channel ----
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
np.random.seed(42)
# Use T channel for clustering (Deposon-aware: only the "transmission" axis)
T_features = T_22.reshape(-1, 1)
km_t = KMeans(n_clusters=4, n_init=10, random_state=42)
km_t.fit(T_features)
km_t_labels = km_t.labels_.tolist()
ari_t = adjusted_rand_score(gt_labels_22, km_t_labels)
print(f"  KMeans on T channel: ARI={ari_t:.4f}, labels={km_t_labels}")

# For comparison: KMeans on full 2048d (baseline, from previous worker)
km_full = KMeans(n_clusters=4, n_init=10, random_state=42)
km_full.fit(embs_22_n)
ari_full = adjusted_rand_score(gt_labels_22, km_full.labels_.tolist())
print(f"  KMeans on 2048d (baseline): ARI={ari_full:.4f}")


# ---- 4-class 2D T/R scatter plot (text) ----
print(f"\n[STAGE 2: 2D T-R scatter]")
for c in range(4):
    members = [(concept_ids[i], round(float(T_22[i]), 4), round(float(R_22[i]), 4))
               for i in range(22) if gt_labels_22[i] == c]
    print(f"  Class {c} ({class_names_22[c]}):")
    for mid, t, r in members:
        print(f"    {mid:30s}  T={t:.4f}  R={r:.4f}")


# ---- Verdict for Stage 2 (A) ----
print(f"\n[STAGE 2 VERDICT]")
if T_ratio > 1.5:
    verdict_A = 'MEANINGFUL'
elif T_ratio < 1.2:
    verdict_A = 'NOISE'
else:
    verdict_A = 'GRAY'
print(f"  Direction A (Deposon-aware Embedding T-channel): ratio={T_ratio:.4f} → {verdict_A}")
print(f"  Compare Cosine: ratio={cos_ratio:.4f} (NOISE)")
if T_ratio > cos_ratio * 1.1:
    print(f"  → T-channel ratio > Cosine ratio by {(T_ratio/cos_ratio - 1)*100:.1f}%, Deposon-aware helps")
else:
    print(f"  → T-channel ratio NOT better than Cosine by {(T_ratio/cos_ratio - 1)*100:.1f}%, A path NOT winning")

# Save stage 2 result
stage2_result = {
    'timestamp': datetime.now(timezone(timedelta(hours=8))).isoformat(timespec='seconds'),
    'stage': 'Stage 2: 22 caption Deposon-aware 3D T+R+A projection',
    'embed_model': EMBED_MODEL,
    'embed_endpoint': EMBED_ENDPOINT,
    'auth': KEY_MASK,
    'caption_count': 22,
    'T_channel_ratio': round(T_ratio, 4),
    'R_channel_ratio': round(R_ratio, 4),
    'A_channel_ratio': round(A_ratio, 4),
    'cosine_ratio_baseline': round(cos_ratio, 4),
    'kmeans_ari_on_T_channel': round(ari_t, 4),
    'kmeans_ari_on_2048d_baseline': round(ari_full, 4),
    'verdict_A': verdict_A,
    'T_R_A_conservation_max_dev': float(np.abs(conservation_check - 1).max()),
    'T_values': {concept_ids[i]: round(float(T_22[i]), 6) for i in range(22)},
    'R_values': {concept_ids[i]: round(float(R_22[i]), 6) for i in range(22)},
    'A_values': {concept_ids[i]: round(float(A_22[i]), 6) for i in range(22)},
    'gt_labels': gt_labels_22,
    'gt_class_names': class_names_22,
}
STAGE2_JSON = r'D:\私人资料\deposon-repo\results\deposon_v3x_6way_stage2_2026_09_10.json'
with open(STAGE2_JSON, 'w', encoding='utf-8') as f:
    json.dump(stage2_result, f, ensure_ascii=False, indent=2)
print(f"\n[OK] Stage 2 result saved: {STAGE2_JSON} ({os.path.getsize(STAGE2_JSON)} bytes)")


# ---------------- 5. Stage 3: Deposon-aware RAG 30 cells re-test ----------------
# 用 22 caption 的 3 维 T+R/A 散射场 + 30 cells 题目 3 维散射场
# top-3 caption 选 T 通道相似度最高 (Deposon-aware: 不再用全 2048-d cosine)
# prompt: Context (3 most relevant concepts) + Question + Answer
print("\n" + "="*80)
print("[STAGE 3] Deposon-aware RAG 30 cells re-test (doubao-seed-code-preview-251028)")
print("="*80)

# 加载 30 cells
gsm8k_data = json.load(open(GSM8K_PATH, encoding='utf-8'))
strategyqa_data = json.load(open(STRATEGYQA_PATH, encoding='utf-8'))

# 30 cell questions
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
print(f"[CELLS] loaded 30 cells (15 GSM8K + 15 StrategyQA)")

# 1-cell sanity check (required per 7 铁律 #3)
print("\n[SANITY] 1-cell check: What is 1+1?")
body, lat, status, err = query_chat("What is 1+1?")
if status == 200 and body and '2' in (body.get('choices', [{}])[0].get('message', {}).get('content', '') or ''):
    print(f"  [OK] sanity PASS, latency={lat:.0f}ms")
else:
    print(f"  [FATAL] sanity FAIL status={status} err={(err or '')[:300]}")
    sys.exit(4)

# 30 cells: 嵌入 → 投影 → top-3 captions by T-channel → RAG prompt
print("\n[STAGE 3] embedding 30 cell questions ...")
cell_questions = [c['question'] for c in cells]
# Chunked 10+10+10
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
assert cell_embs.shape == (30, 2048)
print(f"[CELL EMB] shape={cell_embs.shape}")

# 投影到 3D T+R+A (用 22 caption 同一个 PCA 拟合器? 不行,每个 dataset 单独 PCA)
# 但方向 A 的核心是 30 cells 也做同样的 projection
T_cells, R_cells, A_cells, proj_cells = deposon_project(cell_embs, n_components=2)
print(f"[CELL PROJ] T mean={T_cells.mean():.4f}, R mean={R_cells.mean():.4f}, A mean={A_cells.mean():.4f}")

# T-channel cosine similarity: each cell vs 22 captions
# 用归一化的 T 值
T_22_n = T_22 / (np.linalg.norm(T_22) + 1e-12)
T_cells_n = T_cells / (np.linalg.norm(T_cells) + 1e-12)
# Cosine sim
T_sim_matrix = T_cells.reshape(-1, 1) * T_22.reshape(1, -1)  # use raw T (positive)
T_sim_matrix = T_sim_matrix / (np.outer(np.linalg.norm(T_cells.reshape(-1, 1), axis=1) + 1e-12,
                                          np.linalg.norm(T_22.reshape(1, -1), axis=1) + 1e-12))

# Or: 3D cosine using (T, R, A) as 3D coordinates
TRA_22 = np.stack([T_22, R_22, A_22], axis=1)  # (22, 3)
TRA_cells = np.stack([T_cells, R_cells, A_cells], axis=1)  # (30, 3)
# 3D cosine
TRA_22_n = TRA_22 / (np.linalg.norm(TRA_22, axis=1, keepdims=True) + 1e-12)
TRA_cells_n = TRA_cells / (np.linalg.norm(TRA_cells, axis=1, keepdims=True) + 1e-12)
TRA_sim = TRA_cells_n @ TRA_22_n.T  # (30, 22)
print(f"[TRA sim 3D] shape={TRA_sim.shape}, range=[{TRA_sim.min():.4f}, {TRA_sim.max():.4f}], mean={TRA_sim.mean():.4f}")

# For top-3: use 3D TRA cosine
print(f"\n[STAGE 3] running 30 cells with Deposon-aware RAG ...")
results_3 = []
for ci, cell in enumerate(cells):
    sims = TRA_sim[ci]
    top3_idx = np.argsort(-sims)[:3]
    top3_caps = [captions[j] for j in top3_idx]
    top3_sims = [float(sims[j]) for j in top3_idx]
    # Build prompt
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
        time.sleep(0.5)
        continue
    msg = body.get('choices', [{}])[0].get('message', {})
    content = msg.get('content', '') or ''
    if cell['task'] == 'gsm8k':
        extracted = extract_number(content)
        is_correct = (extracted is not None and abs(extracted - cell['gold_answer']) < 1e-3)
    else:
        extracted = extract_yes_no(content)
        is_correct = (extracted is not None and extracted.lower() == cell['gold_answer'].lower())
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
    time.sleep(0.5)

# Summary
gsm_ok = sum(1 for r in results_3 if r['task'] == 'gsm8k' and r['is_correct'])
strat_ok = sum(1 for r in results_3 if r['task'] == 'strategyqa' and r['is_correct'])
total_ok = gsm_ok + strat_ok
verdict_3 = 'PASS' if total_ok >= 24 else ('GRAY' if total_ok >= 18 else 'FAIL')
print(f"\n[STAGE 3 VERDICT]")
print(f"  GSM8K: {gsm_ok}/15 = {gsm_ok/15*100:.1f}%")
print(f"  StrategyQA: {strat_ok}/15 = {strat_ok/15*100:.1f}%")
print(f"  Total: {total_ok}/30 = {total_ok/30*100:.1f}% → {verdict_3}")

# Save stage 3 result
stage3_result = {
    'timestamp': datetime.now(timezone(timedelta(hours=8))).isoformat(timespec='seconds'),
    'stage': 'Stage 3: Deposon-aware RAG 30 cells re-test',
    'chat_model': CHAT_MODEL,
    'chat_endpoint': CHAT_ENDPOINT,
    'auth': KEY_MASK,
    'embed_model': EMBED_MODEL,
    'rag_method': 'Deposon T+R+A 3D cosine top-3',
    'max_tokens': MAX_TOKENS_CHAT,
    'temperature': 0.0,
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
print(f"\n[OK] Stage 3 result saved: {STAGE3_JSON} ({os.path.getsize(STAGE3_JSON)} bytes)")

# Final summary
print(f"\n" + "="*80)
print(f"[FINAL SUMMARY]")
print(f"="*80)
print(f"Stage 2 (Direction A): T-channel ratio={T_ratio:.4f} → {verdict_A}")
print(f"  vs Cosine baseline: ratio={cos_ratio:.4f}")
print(f"Stage 3 (Direction C): {total_ok}/30 = {total_ok/30*100:.1f}% → {verdict_3}")
print(f"  Compare V4.1-Flash 25/30 (no-RAG): 83.3%")
print(f"  Compare V4.1-Flash 24/30 (RAG-OpenRouter): 80.0%")

# Stage 1+4 will be done in the markdown report
# Save final summary JSON for report generation
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
        'T_channel_ratio': round(T_ratio, 4),
        'R_channel_ratio': round(R_ratio, 4),
        'A_channel_ratio': round(A_ratio, 4),
        'cosine_ratio_baseline': round(cos_ratio, 4),
        'kmeans_ari_on_T_channel': round(ari_t, 4),
        'kmeans_ari_on_2048d_baseline': round(ari_full, 4),
        'verdict_A': verdict_A,
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
print(f"\n[OK] Final summary saved: {FINAL_JSON}")

# Free memory
del embs_22, cell_embs
print(f"\n[OK] All stages done. See JSON files in results/ and report in docs/V3X/")
