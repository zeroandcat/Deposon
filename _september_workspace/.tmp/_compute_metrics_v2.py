#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
K-N26 指标实算 v2：用 v4 聚合数据
口径（保守确定性，禁调参）：
  特征 = [log1p(latency_ms), log1p(prompt_tokens), log1p(completion_tokens),
          log1p(total_tokens), log1p(reasoning_tokens), log1p(cached_tokens)]
  标签 = side (0=teacher, 1=distill)
  分类器 = sklearn LogisticRegression (deterministic, no hyperparam search)
  K-N26-1 = mean of 5 teachers' per-teacher 5-fold CV accuracy
  K-N26-2 = pooled 5-fold CV AUC (cross teacher)
  K-N26-3 = count teachers where per-teacher 5-fold CV accuracy < 0.60
"""
import json
import os
import math
import statistics
from collections import defaultdict

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.preprocessing import StandardScaler

SEED = 42  # 沿 TH-15 一字不动
N_SPLITS = 5

with open('.tmp/_l14v3_aggregated_10cells_v4.json', 'r', encoding='utf-8') as f:
    cells = json.load(f)

def extract_features(quad):
    md = quad.get('per_call_metadata', {})
    u = md.get('usage', {})
    if not isinstance(u, dict):
        u = {}
    latency = md.get('latency_ms', 0.0) or 0.0
    p_tok = u.get('prompt_tokens', 0) or 0
    c_tok = u.get('completion_tokens', 0) or 0
    t_tok = u.get('total_tokens', 0) or 0
    r_tok = u.get('completion_tokens_details', {}).get('reasoning_tokens', 0) or 0
    cache = u.get('prompt_tokens_details', {}).get('cached_tokens', 0) or 0
    return [
        math.log1p(max(0.0, float(latency))),
        math.log1p(max(0, int(p_tok))),
        math.log1p(max(0, int(c_tok))),
        math.log1p(max(0, int(t_tok))),
        math.log1p(max(0, int(r_tok))),
        math.log1p(max(0, int(cache))),
    ]

def extract_label(quad):
    side = quad.get('per_call_metadata', {}).get('side', '?')
    return 0 if side == 'teacher' else 1

teacher_order = ['kimi', 'GLM_1', 'GLM_2', 'coze', 'minimax']

per_teacher_data = {}
for t in teacher_order:
    tqs_teacher = cells.get(f'teacher_{t}', [])
    tqs_distill = cells.get(f'distill_{t}', [])
    per_teacher_data[t] = tqs_teacher + tqs_distill

print(f"{'teacher':10s} {'quads':>5s} {'ok':>5s} {'teacher':>8s} {'distill':>8s}")
for t in teacher_order:
    qs = per_teacher_data[t]
    n_teach = sum(1 for q in qs if extract_label(q) == 0)
    n_dist = sum(1 for q in qs if extract_label(q) == 1)
    ok = sum(1 for q in qs if q.get('per_call_metadata', {}).get('ok'))
    print(f"{t:10s} {len(qs):5d} {ok:5d} {n_teach:8d} {n_dist:8d}")

# ===== K-N26-1: per-teacher 5-fold CV accuracy =====
print()
print("===== K-N26-1: per-teacher 5-fold CV accuracy =====")
k_n26_1_per_teacher = {}
k_n26_1_per_teacher_perfold = {}
for t in teacher_order:
    qs = per_teacher_data[t]
    if len(qs) < 2 * N_SPLITS:
        print(f"  {t}: too few samples ({len(qs)}), skip")
        k_n26_1_per_teacher[t] = None
        continue
    X = np.array([extract_features(q) for q in qs])
    y = np.array([extract_label(q) for q in qs])
    if len(set(y)) < 2:
        print(f"  {t}: only one class in y ({set(y)}), skip")
        k_n26_1_per_teacher[t] = None
        continue
    skf = StratifiedKFold(n_splits=N_SPLITS, shuffle=True, random_state=SEED)
    accs = []
    for train_idx, test_idx in skf.split(X, y):
        scaler = StandardScaler()
        X_tr = scaler.fit_transform(X[train_idx])
        X_te = scaler.transform(X[test_idx])
        clf = LogisticRegression(random_state=SEED, max_iter=1000, solver='lbfgs')
        clf.fit(X_tr, y[train_idx])
        y_pred = clf.predict(X_te)
        accs.append(accuracy_score(y[test_idx], y_pred))
    mean_acc = float(np.mean(accs))
    k_n26_1_per_teacher[t] = mean_acc
    k_n26_1_per_teacher_perfold[t] = accs
    print(f"  {t:10s} per_fold = [{', '.join(f'{a:.4f}' for a in accs)}] mean = {mean_acc:.4f}")

valid = [v for v in k_n26_1_per_teacher.values() if v is not None]
k_n26_1_teacher_acc = float(np.mean(valid)) if valid else None
print(f"\nK-N26-1 教师准确率 (5 教师 mean) = {k_n26_1_teacher_acc}")
print(f"K-N26-1 字面 = 教师准确率 ≥ K_N26_1_ACC = 0.70")
k_n26_1_hit = k_n26_1_teacher_acc is not None and k_n26_1_teacher_acc >= 0.70
print(f"K-N26-1 hit = {k_n26_1_hit} ({'TRIGGERED' if k_n26_1_hit else 'NOT TRIGGERED'})")

# ===== K-N26-2: pooled 5-fold CV AUC =====
print()
print("===== K-N26-2: pooled 5-fold CV AUC =====")
all_qs = []
for t in teacher_order:
    all_qs.extend(per_teacher_data[t])
X_all = np.array([extract_features(q) for q in all_qs])
y_all = np.array([extract_label(q) for q in all_qs])
print(f"  pooled N = {len(all_qs)}, y=teacher {sum(y_all==0)}, y=distill {sum(y_all==1)}")
skf = StratifiedKFold(n_splits=N_SPLITS, shuffle=True, random_state=SEED)
aucs = []
for train_idx, test_idx in skf.split(X_all, y_all):
    scaler = StandardScaler()
    X_tr = scaler.fit_transform(X_all[train_idx])
    X_te = scaler.transform(X_all[test_idx])
    clf = LogisticRegression(random_state=SEED, max_iter=1000, solver='lbfgs')
    clf.fit(X_tr, y_all[train_idx])
    y_prob = clf.predict_proba(X_te)[:, 1]
    auc = roc_auc_score(y_all[test_idx], y_prob)
    aucs.append(auc)
k_n26_2_auc = float(np.mean(aucs))
print(f"  per_fold = [{', '.join(f'{a:.4f}' for a in aucs)}]")
print(f"  pooled AUC = {k_n26_2_auc}")
k_n26_2_hit = k_n26_2_auc < 0.75
print(f"K-N26-2 hit = {k_n26_2_hit} ({'TRIGGERED' if k_n26_2_hit else 'NOT TRIGGERED'}) (字面 AUC < 0.75)")

# ===== K-N26-3: count teachers where per-teacher 5-fold CV accuracy < 0.60 =====
print()
print("===== K-N26-3: count teachers where per-teacher accuracy < 0.60 =====")
n_below = sum(1 for v in k_n26_1_per_teacher.values() if v is not None and v < 0.60)
print(f"  per-teacher accuracy: {k_n26_1_per_teacher}")
print(f"  n_teachers_below_0.60 = {n_below}")
k_n26_3_hit = n_below >= 4
print(f"K-N26-3 hit = {k_n26_3_hit} (字面 ≥4 教师 <0.60)")

# ===== Per-teacher additional details =====
print()
print("===== Per-teacher additional details =====")
for t in teacher_order:
    qs = per_teacher_data[t]
    captions = set(q.get('per_call_metadata', {}).get('caption_id') for q in qs)
    by_side = {'teacher': 0, 'distill': 0}
    for q in qs:
        s = q.get('per_call_metadata', {}).get('side', '?')
        by_side[s] = by_side.get(s, 0) + 1
    print(f"  {t}: N={len(qs)} unique_captions={len(captions)} by_side={by_side}")

# ===== Save metrics =====
metrics = {
    "seed": SEED,
    "n_splits": N_SPLITS,
    "feature_names": ["log1p_latency_ms", "log1p_prompt_tokens", "log1p_completion_tokens",
                      "log1p_total_tokens", "log1p_reasoning_tokens", "log1p_cached_tokens"],
    "classifier": "sklearn.linear_model.LogisticRegression(random_state=42, max_iter=1000, solver='lbfgs')",
    "thresholds": {
        "K_N26_1_ACC": 0.70,
        "K_N26_2_AUC": 0.75,
        "K_N26_3_TEACHERS_LT": 0.60
    },
    "K_N26_1": {
        "per_teacher_acc": k_n26_1_per_teacher,
        "per_teacher_perfold": k_n26_1_per_teacher_perfold,
        "mean_teacher_acc": k_n26_1_teacher_acc,
        "hit": k_n26_1_hit,
        "rule": "teacher_acc >= 0.70 -> hit=True -> 真证伪 (metadata 可区分)"
    },
    "K_N26_2": {
        "per_fold_auc": aucs,
        "pooled_auc": k_n26_2_auc,
        "hit": k_n26_2_hit,
        "rule": "pooled_auc < 0.75 -> hit=True -> 真证伪 (metadata 不可区分)"
    },
    "K_N26_3": {
        "n_teachers_below_0_60": n_below,
        "per_teacher_acc": k_n26_1_per_teacher,
        "hit": k_n26_3_hit,
        "rule": "n_teachers_with_acc<0.60 >= 4 -> hit=True -> 真证伪 (多数教师 metadata 不可区分)"
    },
    "n_cells_total": sum(len(v) for v in cells.values()),
    "n_per_teacher": {t: len(per_teacher_data[t]) for t in teacher_order},
}

with open('.tmp/_l14v3_n26_metrics_v2.json', 'w', encoding='utf-8') as f:
    json.dump(metrics, f, ensure_ascii=False, indent=2)
print(f"\nMetrics saved to .tmp/_l14v3_n26_metrics_v2.json")