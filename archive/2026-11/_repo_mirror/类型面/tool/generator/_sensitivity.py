#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sensitivity test (替代读法):
- Read 1 (主读法): full sample
- Read 2: drop coze (代表采样边界)
- Read 3: drop GLM_2 (近缘对同 model 不同语料 — but 模型相同 = 难区分)
- Read 4: drop kimi (teacher 侧数据缺 21 calls)
- Read 5: drop both coze + GLM_2 + kimi (3 边界教师剔除)
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

SEED = 42
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

def extract_teacher(quad):
    md = quad.get('per_call_metadata', {})
    return md.get('teacher_label') or md.get('teacher') or '?'

teacher_order = ['kimi', 'GLM_1', 'GLM_2', 'coze', 'minimax']
per_teacher_data = {}
for t in teacher_order:
    tqs_teacher = cells.get(f'teacher_{t}', [])
    tqs_distill = cells.get(f'distill_{t}', [])
    per_teacher_data[t] = tqs_teacher + tqs_distill

def compute_metrics(teacher_subset, label):
    print(f"\n=== {label} ===")
    print(f"  teachers = {teacher_subset}")
    # Per-teacher accuracy
    k1_per_teacher = {}
    for t in teacher_subset:
        qs = per_teacher_data[t]
        X = np.array([extract_features(q) for q in qs])
        y = np.array([extract_label(q) for q in qs])
        if len(set(y)) < 2:
            k1_per_teacher[t] = None
            continue
        if len(qs) < 2 * N_SPLITS:
            k1_per_teacher[t] = None
            continue
        skf = StratifiedKFold(n_splits=N_SPLITS, shuffle=True, random_state=SEED)
        accs = []
        for tr, te in skf.split(X, y):
            sc = StandardScaler()
            Xtr = sc.fit_transform(X[tr])
            Xte = sc.transform(X[te])
            clf = LogisticRegression(random_state=SEED, max_iter=1000, solver='lbfgs')
            clf.fit(Xtr, y[tr])
            accs.append(accuracy_score(y[te], clf.predict(Xte)))
        k1_per_teacher[t] = float(np.mean(accs))
    valid = [v for v in k1_per_teacher.values() if v is not None]
    k1_mean = float(np.mean(valid)) if valid else None
    k1_hit = k1_mean is not None and k1_mean >= 0.70
    n_below_060 = sum(1 for v in k1_per_teacher.values() if v is not None and v < 0.60)
    k3_hit = n_below_060 >= 4
    # Pooled AUC
    all_qs = []
    for t in teacher_subset:
        all_qs.extend(per_teacher_data[t])
    Xa = np.array([extract_features(q) for q in all_qs])
    ya = np.array([extract_label(q) for q in all_qs])
    skf = StratifiedKFold(n_splits=N_SPLITS, shuffle=True, random_state=SEED)
    aucs = []
    for tr, te in skf.split(Xa, ya):
        sc = StandardScaler()
        Xtr = sc.fit_transform(Xa[tr])
        Xte = sc.transform(Xa[te])
        clf = LogisticRegression(random_state=SEED, max_iter=1000, solver='lbfgs')
        clf.fit(Xtr, ya[tr])
        aucs.append(roc_auc_score(ya[te], clf.predict_proba(Xte)[:, 1]))
    k2_auc = float(np.mean(aucs))
    k2_hit = k2_auc < 0.75
    print(f"  per_teacher_acc = {k1_per_teacher}")
    print(f"  K-N26-1 mean_teacher_acc = {k1_mean:.4f} hit={k1_hit}")
    print(f"  K-N26-2 pooled_AUC       = {k2_auc:.4f} hit={k2_hit}")
    print(f"  K-N26-3 n_below_0.60     = {n_below_060} hit={k3_hit}")
    return {
        "subset": teacher_subset,
        "k1_per_teacher": k1_per_teacher,
        "k1_mean": k1_mean,
        "k1_hit": k1_hit,
        "k2_auc": k2_auc,
        "k2_hit": k2_hit,
        "n_below_060": n_below_060,
        "k3_hit": k3_hit,
        "N_total": len(all_qs),
    }

results = {
    "main_full": compute_metrics(teacher_order, "主读法 · 全样本"),
    "drop_coze": compute_metrics([t for t in teacher_order if t != 'coze'], "替代读法 1 · 剔除 coze (代表采样边界)"),
    "drop_glm2": compute_metrics([t for t in teacher_order if t != 'GLM_2'], "替代读法 2 · 剔除 GLM_2 (近缘对同 model)"),
    "drop_kimi": compute_metrics([t for t in teacher_order if t != 'kimi'], "替代读法 3 · 剔除 kimi (teacher 侧数据缺 21 calls)"),
    "drop_all3": compute_metrics([t for t in teacher_order if t not in ('coze', 'GLM_2', 'kimi')], "替代读法 4 · 剔除 coze+GLM_2+kimi (3 边界教师全剔)"),
}

with open('.tmp/_l14v3_sensitivity_v2.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print(f"\nSensitivity results saved to .tmp/_l14v3_sensitivity_v2.json")

# print summary table
print()
print("=" * 100)
print(f"{'read':35s} {'K-N26-1':>10s} {'K-N26-2 AUC':>14s} {'K-N26-3 n<0.6':>14s} {'N_total':>8s}")
print("-" * 100)
for k, v in results.items():
    k1h = "TRIGGER" if v['k1_hit'] else "no"
    k2h = "TRIGGER" if v['k2_hit'] else "no"
    k3h = "TRIGGER" if v['k3_hit'] else "no"
    print(f"{k:35s} {v['k1_mean']:.4f}/{k1h:6s} {v['k2_auc']:.4f}/{k2h:6s} {v['n_below_060']}/{k3h:6s} {v['N_total']:8d}")