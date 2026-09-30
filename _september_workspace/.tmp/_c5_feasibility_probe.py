import json, numpy as np
a = json.load(open('results/deposon_v2_phase3_strip_embeddings_2026_09_11.json', encoding='utf-8'))
e = json.load(open('results/deposon_volcengine_22caption_embedding_2026_09_10.json', encoding='utf-8'))
ids = a['concept_ids']; E = np.array(a['embs_strip'], dtype=float)
stored = e['svd2_coords']
print('E shape', E.shape)
# attempt 1: center then SVD
Ec = E - E.mean(axis=0, keepdims=True)
U,S,Vt = np.linalg.svd(Ec, full_matrices=False)
proj = Ec @ Vt[:2].T
for k in range(2):
    d = max(abs(proj[:,k] - np.array([stored[c][k] for c in ids])))
    print(f'centered+SVD col{k}: max abs diff = {d:.6f}')
# attempt 2: no centering
U2,S2,Vt2 = np.linalg.svd(E, full_matrices=False)
p2 = E @ Vt2[:2].T
for k in range(2):
    d = max(abs(p2[:,k] - np.array([stored[c][k] for c in ids])))
    print(f'raw+SVD col{k}: max abs diff = {d:.6f}')
print('svd_top2_var_explained stored =', e['sim_matrix_stats']['svd_top2_var_explained'])
print('recomputed var explained top2 =', float((S[:2]**2).sum()/(S**2).sum()))
