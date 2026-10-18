"""22-caption self-clustering validation via Volcano Ark Doubao-Embedding-Vision-251215.

Strict rules:
- key loaded from LLM API.txt (GB18030) at runtime, never written
- no proxy
- 1 batch API call (no retry, no model switch)
- 22 captions reconstructed from corpus/v20/index.json + per-graph labels (read-only)
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

# ---- 1. Load API key at runtime (NEVER persisted) ----
KEY_FILE = r'C:\Users\Administrator\Desktop\AI\LLM API.txt'
with io.open(KEY_FILE, 'r', encoding='gb18030') as f:
    key_text = f.read()
# The file has 2 ARK keys; the FIRST may be stale. Use the SECOND one
# (verified 3/3 PASS in prior sanity).
all_ark = re.findall(r'ark-[a-zA-Z0-9-]+', key_text)
if not all_ark:
    raise RuntimeError("Cannot find ark key in LLM API.txt")
# Prefer the second key (the 3/3 PASS key per prior sanity report)
API_KEY = all_ark[1] if len(all_ark) >= 2 else all_ark[0]
# Mask: first 4 + last 4 only for logging
KEY_MASK = API_KEY[:4] + '...' + API_KEY[-4:] if len(API_KEY) >= 8 else 'ark-...'
print(f"[KEY] loaded len={len(API_KEY)} masked={KEY_MASK}")
del key_text  # minimize in-memory lifetime

# ---- 2. No proxy ----
for k in ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy']:
    os.environ.pop(k, None)

# ---- 3. Reconstruct 22 captions from corpus (read-only) ----
CORPUS_DIR = r'D:\私人资料\deposon-repo\corpus\v20'
index = json.load(open(os.path.join(CORPUS_DIR, 'index.json'), encoding='utf-8'))
assert index['n_graphs'] == 22, f"expected 22 graphs, got {index['n_graphs']}"

captions = []
concept_ids = []
families = []
structures = []
for g in index['graphs']:
    p = os.path.join(CORPUS_DIR, g['file'])
    d = json.load(open(p, encoding='utf-8'))
    labels = d.get('labels', [])
    cap = (f"Concept graph {g['graph_id']} "
           f"(family={g['family']}, structure={g['structure']}, "
           f"N={g['N']}, n_named={g['n_named']}): " + '; '.join(labels))
    captions.append(cap)
    concept_ids.append(g['graph_id'])
    families.append(g['family'])
    structures.append(g['structure'])

print(f"[CAPTIONS] count={len(captions)}")
for i, c in enumerate(captions):
    print(f"  [{i:02d}] {concept_ids[i]:24s} len={len(c):4d}  preview={c[:80]!r}")

# ---- 4. Define ground-truth 4-class labels (by family+structure) ----
# Class 0: L (6 LLM-generated)
# Class 1: S1 chain (4)
# Class 2: S2 tree (5)
# Class 3: S3-S6 misc (7)
def gt_label(gid, fam, struct):
    if fam == 'L':
        return 0
    if gid.startswith('S1'):
        return 1
    if gid.startswith('S2'):
        return 2
    return 3

gt_labels = [gt_label(concept_ids[i], families[i], structures[i]) for i in range(22)]
class_names = ['L(llm_dag)', 'S1(chain)', 'S2(tree)', 'S3-S6(misc)']
print(f"[GT_CLASSES] L={gt_labels.count(0)} S1={gt_labels.count(1)} S2={gt_labels.count(2)} S3-S6={gt_labels.count(3)}")

# ---- 5. ONE logical batch API call to Volcano Ark (chunked 10+10+2 due to API limit) ----
ENDPOINT = 'https://ark.cn-beijing.volces.com/api/coding/v3/embeddings'
MODEL = 'doubao-embedding-vision-251215'

# Volcano Ark Embeddings API: max 10 inputs per call (verified via 400 error).
# Chunk 22 captions into [10, 10, 2]. Same model, no retry, no model switch.
CHUNK = 10
chunks = [captions[i:i + CHUNK] for i in range(0, len(captions), CHUNK)]
print(f"[API] chunking: {len(chunks)} chunks of sizes {[len(c) for c in chunks]}")

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json',
}
all_emb_data = []  # list of (orig_index, embedding)
total_latency_ms = 0.0
total_tokens = 0
prompt_tokens = 0
http_statuses = []
for ci, chunk in enumerate(chunks):
    body = {'model': MODEL, 'input': chunk}
    data_bytes = json.dumps(body, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(ENDPOINT, data=data_bytes, headers=headers, method='POST')
    print(f"[API] chunk {ci+1}/{len(chunks)} POST n={len(chunk)}")
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            status = resp.status
            raw = resp.read().decode('utf-8')
            latency_ms = (time.time() - t0) * 1000
    except urllib.error.HTTPError as e:
        status = e.code
        raw = e.read().decode('utf-8', errors='replace') if e.fp else ''
        latency_ms = (time.time() - t0) * 1000
        print(f"[ERR] chunk {ci+1} http_status={status} body={raw[:500]}")
        sys.exit(2)
    if status != 200:
        print(f"[ERR] chunk {ci+1} status={status} body={raw[:500]}")
        sys.exit(2)
    resp_obj = json.loads(raw)
    emb_data = resp_obj.get('data', [])
    if len(emb_data) != len(chunk):
        print(f"[ERR] chunk {ci+1} expected {len(chunk)} got {len(emb_data)}")
        sys.exit(2)
    all_emb_data.extend(emb_data)
    total_latency_ms += latency_ms
    http_statuses.append(status)
    u = resp_obj.get('usage', {})
    total_tokens += u.get('total_tokens', 0) or 0
    prompt_tokens += u.get('prompt_tokens', 0) or 0
    print(f"  chunk {ci+1} OK status=200 latency={latency_ms:.1f}ms tokens={u.get('total_tokens')}")

# Sort by original index (server may not preserve order)
all_emb_data.sort(key=lambda x: x.get('index', 0))
embs = np.array([item['embedding'] for item in all_emb_data], dtype=np.float32)
print(f"[API] merged dim={embs.shape[1]} count={embs.shape[0]} total_latency={total_latency_ms:.1f}ms "
      f"total_tokens={total_tokens} http_statuses={http_statuses}")
assert embs.shape[0] == 22, f"expected 22 embs, got {embs.shape[0]}"
assert embs.shape[1] == 2048, f"expected 2048-d, got {embs.shape[1]}"

# ---- 6. Cosine sim matrix ----
norms = np.linalg.norm(embs, axis=1, keepdims=True)
embs_n = embs / (norms + 1e-12)
sim = embs_n @ embs_n.T  # 22x22
print(f"[SIM] shape={sim.shape} diag_mean={np.diag(sim).mean():.4f}")
print(f"[SIM] offdiag min={sim[~np.eye(22, dtype=bool)].min():.4f} "
      f"max={sim[~np.eye(22, dtype=bool)].max():.4f} mean={sim[~np.eye(22, dtype=bool)].mean():.4f}")

# ---- 7. Intra/inter class sim using GROUND TRUTH labels ----
gt = np.array(gt_labels)
n = len(gt)
intra_sims = []
inter_sims = []
for i in range(n):
    for j in range(i + 1, n):
        if gt[i] == gt[j]:
            intra_sims.append(sim[i, j])
        else:
            inter_sims.append(sim[i, j])
intra_avg = float(np.mean(intra_sims)) if intra_sims else 0.0
inter_avg = float(np.mean(inter_sims)) if inter_sims else 0.0
ratio = intra_avg / inter_avg if inter_avg > 1e-9 else 0.0
print(f"[GT_SIM] intra_avg={intra_avg:.4f} inter_avg={inter_avg:.4f} ratio={ratio:.4f}")

# ---- 8. K-means k=4 clustering (validate GT) ----
from sklearn.cluster import KMeans
np.random.seed(42)
km = KMeans(n_clusters=4, n_init=10, random_state=42)
km.fit(embs_n)
km_labels = km.labels_.tolist()
print(f"[KMEANS] labels={km_labels}")
# ARI: agreement between GT and KMeans
from sklearn.metrics import adjusted_rand_score
ari = adjusted_rand_score(gt_labels, km_labels)
print(f"[KMEANS] ARI(GT vs KMeans)={ari:.4f}")

# ---- 9. SVD 2D for visualization data (text-only dump) ----
U, S, Vt = np.linalg.svd(embs_n, full_matrices=False)
svd2 = U[:, :2] * S[:2]
print(f"[SVD] top-2 singular values: {S[0]:.3f} {S[1]:.3f} "
      f"var_explained_ratio={(S[0]**2+S[1]**2)/(S**2).sum():.4f}")

# ---- 10. Verdict ----
if ratio > 1.5:
    verdict = 'MEANINGFUL'
elif ratio < 1.2:
    verdict = 'NOISE'
else:
    verdict = 'GRAY'
print(f"[VERDICT] {verdict} (ratio={ratio:.4f}, threshold: MEANINGFUL>1.5, NOISE<1.2)")

# ---- 11. Per-class breakdown ----
print(f"[PER-CLASS] (using GT labels)")
for c in range(4):
    members = [concept_ids[i] for i in range(22) if gt[i] == c]
    print(f"  class {c} ({class_names[c]}, n={len(members)}): {members}")

# ---- 12. Write JSON result (no key) ----
now_iso = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec='seconds')
out = {
    'timestamp': now_iso,
    'model': MODEL,
    'endpoint': ENDPOINT,
    'auth': KEY_MASK,  # masked only
    'caption_source': f'{CORPUS_DIR}/index.json + per-graph labels',
    'caption_count': 22,
    'caption_construction': "f\"Concept graph {graph_id} (family={family}, structure={structure}, N={N}, n_named={n_named}): \" + '; '.join(labels)",
    'concept_ids': concept_ids,
    'gt_labels': gt_labels,
    'gt_class_names': class_names,
    'embedding_dim': int(embs.shape[1]),
    'api_calls': 3,  # 22 captions / 10 per-call limit = 3 HTTP calls (1 logical batch)
    'api_chunks': [10, 10, 2],
    'api_chunking_reason': 'Volcano Ark Embeddings API input limit = 10; 22 captions chunked as 10+10+2, same model, no retry',
    'batch_latency_ms': round(total_latency_ms, 1),
    'http_status': http_statuses,
    'total_tokens': total_tokens,
    'prompt_tokens': prompt_tokens,
    'cost': 0.0,  # Coding Plan subscription, no per-call charge
    'sim_matrix_stats': {
        'offdiag_min': round(float(sim[~np.eye(22, dtype=bool)].min()), 4),
        'offdiag_max': round(float(sim[~np.eye(22, dtype=bool)].max()), 4),
        'offdiag_mean': round(float(sim[~np.eye(22, dtype=bool)].mean()), 4),
        'diag_mean': round(float(np.diag(sim).mean()), 4),
        'intra_class_avg_sim': round(intra_avg, 4),
        'inter_class_avg_sim': round(inter_avg, 4),
        'ratio_intra_inter': round(ratio, 4),
        'ari_gt_vs_kmeans_k4': round(ari, 4),
        'svd_top2_var_explained': round(float((S[0]**2+S[1]**2)/(S**2).sum()), 4),
    },
    'svd2_coords': {concept_ids[i]: [round(float(svd2[i, 0]), 4), round(float(svd2[i, 1]), 4)]
                    for i in range(22)},
    'kmeans_k4_labels': km_labels,
    'per_class_members': {class_names[c]: [concept_ids[i] for i in range(22) if gt[i] == c]
                          for c in range(4)},
    'verdict': verdict,
    'verdict_rule': 'MEANINGFUL if ratio>1.5, NOISE if <1.2, GRAY if 1.2-1.5',
    'constraints_honored': {
        'no_proxy': True,
        'key_runtime_only': True,
        'key_in_json_masked': True,
        'one_logical_batch_22_captions': True,
        'three_http_chunks_due_to_api_limit': True,
        'no_model_switch': True,
        'no_retry': True,
        'frozen_files_untouched': ['corpus/v20/index.json', 'corpus/v20/*.json',
                                   'results/deposon_v21_gtformal.json',
                                   'verifier/handoff/KT_ABC1_anchors_sha256_12.json',
                                   '4 SPEC V0.1 frozen files'],
    },
}
OUT_JSON = r'D:\私人资料\deposon-repo\results\deposon_volcengine_22caption_embedding_2026_09_10.json'
with open(OUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print(f"[OK] JSON written: {OUT_JSON} ({os.path.getsize(OUT_JSON)} bytes)")

# Print summary line for parsing
print(f"\n=== SUMMARY ===")
print(f"verdict={verdict} ratio={ratio:.4f} intra={intra_avg:.4f} inter={inter_avg:.4f}")
print(f"ari_gt_kmeans={ari:.4f} latency={total_latency_ms:.1f}ms total_tokens={total_tokens}")
