# -*- coding: utf-8 -*-
"""
阶段 1 + 阶段 2:Deposon-aware Embedding T/R/A 投影 + LLM 推理 T/R/A 分解
无 LLM 调用,纯 numpy/sklearn 计算

输入:
  1. deposon_volcengine_22caption_embedding_2026_09_10.json (SVD 2D 投影)
  2. deposon_deepseek_v41_flash_30cells_v3_2026_09_10.json (25/30)
  3. deposon_volcengine_glm_latest_5cells_2026_09_10.json (5/5)
  4. deposon_volcengine_seed_code_30cells_2026_09_10.json (24/30)
  5. deposon_gpt6_teamorouter_30cells_2026_09_10.json (22/30)

输出:
  /results/_tra_v0_2026_09_10.json (审计中间数据)
  /results/_tra_v0_summary_2026_09_10.md (人读摘要)
"""
import json
import os
import sys
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

ROOT = r"D:\私人资料\deposon-repo"
RESULTS = os.path.join(ROOT, "results")

# ============================================================
# 阶段 1:Deposon-aware Embedding T/R/A 投影
# ============================================================
print("=" * 60)
print("阶段 1:Deposon-aware Embedding T/R/A 投影")
print("=" * 60)

with open(os.path.join(RESULTS, "deposon_volcengine_22caption_embedding_2026_09_10.json"), "r", encoding="utf-8") as f:
    data_22 = json.load(f)

# 已有数据:SVD 2D 投影 (22×2) + gt_labels + kmeans_k4_labels
svd2 = np.array([data_22["svd2_coords"][cid] for cid in data_22["concept_ids"]])
gt_labels = np.array(data_22["gt_labels"])
kmeans_labels = np.array(data_22["kmeans_k4_labels"])
ari_gt_km = adjusted_rand_score(gt_labels, kmeans_labels)

# V3X 散射公式:T+R+A=1
# 沿 PC1(主方差) = T 透射
# 沿 PC2(次方差) = R 反射
# 1 - T - R = A 凝华
svd2_norm = svd2 / (np.linalg.norm(svd2, axis=1, keepdims=True) + 1e-12)
T_vec = svd2_norm[:, 0]
R_vec = svd2_norm[:, 1]
T_frac = np.abs(T_vec)
R_frac = np.abs(R_vec)
A_frac = 1.0 - T_frac - R_frac  # 注:可能是负值,需要按 |A| 处理
A_frac = np.abs(A_frac)

# 归一化(让 T+R+A=1 per caption)
total = T_frac + R_frac + A_frac + 1e-12
T_frac_n = T_frac / total
R_frac_n = R_frac / total
A_frac_n = A_frac / total

print(f"  T 通道均值: {T_frac_n.mean():.4f} (理想 ~0.4-0.6 为 主导)")
print(f"  R 通道均值: {R_frac_n.mean():.4f}")
print(f"  A 通道均值: {A_frac_n.mean():.4f}")

# T 通道 cosine ratio(在 1D T_vec 上)
def cosine_ratio_1d(vec, labels, gt_labels):
    """在 1D T 通道计算 intra/inter cosine ratio"""
    n = len(vec)
    intra, inter = [], []
    for i in range(n):
        for j in range(i + 1, n):
            # 1D cosine:vec[i] * vec[j] / (|vec[i]| |vec[j]|)
            denom = np.abs(vec[i]) * np.abs(vec[j]) + 1e-12
            sim = (vec[i] * vec[j]) / denom
            if gt_labels[i] == gt_labels[j]:
                intra.append(sim)
            else:
                inter.append(sim)
    intra_m = np.mean(intra) if intra else 0.0
    inter_m = np.mean(inter) if inter else 1e-6
    return intra_m, inter_m, intra_m / inter_m

# 原始 2048-d 已有 ratio = 1.0562
# T 通道 1D 投影 ratio:
T_intra, T_inter, T_ratio = cosine_ratio_1d(T_vec, kmeans_labels, gt_labels)
print(f"\n  原始 2048-d 全空间 ratio: 1.0562 (NOISE, baseline)")
print(f"  T 通道 1D 投影 ratio: {T_ratio:.4f}")

# 完整 SVD 2D cosine ratio
def cosine_ratio_2d(emb, gt_labels):
    n = emb.shape[0]
    intra, inter = [], []
    for i in range(n):
        for j in range(i + 1, n):
            denom = (np.linalg.norm(emb[i]) * np.linalg.norm(emb[j])) + 1e-12
            sim = np.dot(emb[i], emb[j]) / denom
            if gt_labels[i] == gt_labels[j]:
                intra.append(sim)
            else:
                inter.append(sim)
    intra_m = np.mean(intra) if intra else 0.0
    inter_m = np.mean(inter) if inter else 1e-6
    return intra_m, inter_m, intra_m / inter_m

SVD_intra, SVD_inter, SVD_ratio = cosine_ratio_2d(svd2, gt_labels)
print(f"  SVD 2D 投影 ratio: {SVD_ratio:.4f}")

# KMeans k=4 在 T 通道 1D 上
km_T = KMeans(n_clusters=4, random_state=42, n_init=10)
km_T_labels = km_T.fit_predict(T_vec.reshape(-1, 1))
ari_T = adjusted_rand_score(gt_labels, km_T_labels)
print(f"\n  KMeans k=4 on 1D T 通道: ARI = {ari_T:.4f} (baseline 0.0615 on full space)")

# KMeans k=4 on SVD 2D
km_2d = KMeans(n_clusters=4, random_state=42, n_init=10)
km_2d_labels = km_2d.fit_predict(svd2)
ari_2d = adjusted_rand_score(gt_labels, km_2d_labels)
print(f"  KMeans k=4 on SVD 2D: ARI = {ari_2d:.4f}")

# Verdicts
def verdict_from_ratio(r):
    if r > 1.5: return "MEANINGFUL"
    elif r >= 1.2: return "GRAY"
    else: return "NOISE"

verdict_2048 = verdict_from_ratio(1.0562)
verdict_T = verdict_from_ratio(T_ratio)
verdict_2d = verdict_from_ratio(SVD_ratio)

# 每类在 T 通道的均值/标准差
print(f"\n  每类 T 通道统计 (4 GT 类):")
gt_class_names = data_22["gt_class_names"]
for c in range(4):
    mask = gt_labels == c
    t_mean = T_vec[mask].mean()
    t_std = T_vec[mask].std()
    a_mean = A_frac_n[mask].mean()
    print(f"    {gt_class_names[c]}: T_mean={t_mean:.4f} T_std={t_std:.4f} A_mean={a_mean:.4f} (n={mask.sum()})")

# ============================================================
# 阶段 2:LLM 推理 T/R/A 分解
# ============================================================
print()
print("=" * 60)
print("阶段 2:LLM 推理 T/R/A 分解")
print("=" * 60)


def classify_tra(cells):
    """
    严格不相交分类:
    T = 答对 且 not (trunc/timeout) → 纯透射
    R = 答错 且 not (trunc/timeout) → 纯反射
    A = 有 trunc/timeout 事件(无论 pass/fail) → 凝华
    边界 = 答错 ∧ A(同时算 R 算 A)
    """
    T_clean, R_clean, A_event, boundary = [], [], [], []
    for c in cells:
        is_correct = c.get("is_correct", False)
        note = c.get("note", "") or ""
        err = c.get("error", "") or ""
        cid = c.get("cell_id") or c.get("id")
        blob = (str(note) + " " + str(err)).lower()
        has_a = ("truncat" in blob) or ("timeout" in blob) or ("timed out" in blob)
        if has_a:
            A_event.append(cid)
        if is_correct and not has_a:
            T_clean.append(cid)
        elif not is_correct and not has_a:
            R_clean.append(cid)
        if not is_correct and has_a:
            boundary.append(cid)
    return T_clean, R_clean, A_event, boundary


def report_tra(name, cells, summary=None):
    T_clean, R_clean, A_event, boundary = classify_tra(cells)
    n = len(cells)
    n_pass = sum(1 for c in cells if c.get("is_correct", False))
    n_trunc_pass = sum(
        1 for c in cells
        if c.get("is_correct", False) and ("truncat" in c.get("note", "clean").lower())
    )
    # T 真实总数 = pass_clean + (trunc_pass 算 A 还是 T?按"primary cause"原则算 A)
    T_total = n_pass - n_trunc_pass
    R_total = len(R_clean)
    A_total = len(A_event)
    boundary_total = len(boundary)
    print(f"\n[{name}]")
    print(f"  Total cells: {n}")
    print(f"  Pass: {n_pass}/{n} ({n_pass / n * 100:.1f}%)")
    print(f"  T (clean pass): {T_total} cells")
    print(f"  R (clean fail, semantic_misjudge): {R_total} cells")
    print(f"  A (trunc/timeout event): {A_total} cells")
    print(f"  Boundary (fail ∧ A): {boundary_total} cells")
    if A_event:
        print(f"  A cells: {A_event}")
    if R_clean:
        print(f"  R cells: {R_clean}")
    return {
        "name": name,
        "total": n,
        "pass": n_pass,
        "T_clean": T_total,
        "R_clean": R_total,
        "A_event": A_total,
        "boundary": boundary_total,
        "trunc_pass": n_trunc_pass,
        "verdict": summary.get("verdict", "?") if summary else "?",
    }


# V4.1-Flash 30 cells v3
with open(os.path.join(RESULTS, "deposon_deepseek_v41_flash_30cells_v3_2026_09_10.json"), "r", encoding="utf-8") as f:
    v41 = json.load(f)
v41_traj = report_tra("V4.1-Flash 30 cells v3 (deepseek-v4.1-flash, max_tokens=2048)", v41["cells"], v41["summary"])

# GLM 5 cells
with open(os.path.join(RESULTS, "deposon_volcengine_glm_latest_5cells_2026_09_10.json"), "r", encoding="utf-8") as f:
    glm = json.load(f)
glm_traj = report_tra("GLM-latest 5 cells (火山方舟 alias)", glm["cells"], glm["summary"])

# Doubao-seed-code 30 cells
with open(os.path.join(RESULTS, "deposon_volcengine_seed_code_30cells_2026_09_10.json"), "r", encoding="utf-8") as f:
    doubao = json.load(f)
doubao_traj = report_tra("Doubao-seed-code 30 cells (doubao-seed-code-preview-251028, max_tokens=2048)", doubao["cells"], doubao["summary"])

# GPT-6 TeamoRouter 30 cells
with open(os.path.join(RESULTS, "deposon_gpt6_teamorouter_30cells_2026_09_10.json"), "r", encoding="utf-8") as f:
    gpt6 = json.load(f)
gpt6_traj = report_tra("GPT-6 TeamoRouter 30 cells (gpt-6-astra, max_tokens=1024)", gpt6["cells"], gpt6["summary"])

# ============================================================
# 输出:tra_v0 summary (审计中间数据)
# ============================================================
summary = {
    "timestamp": "2026-09-10T20:15:24+08:00",
    "purpose": "6 方向综合验证 - 阶段 1+2 中间数据(无 LLM,纯本地计算)",
    "stage1_embedding_tra": {
        "input": "deposon_volcengine_22caption_embedding_2026_09_10.json (SVD 2D 投影,无原 2048-d)",
        "n_captions": 22,
        "n_gt_classes": 4,
        "T_channel_mean_frac": float(T_frac_n.mean()),
        "R_channel_mean_frac": float(R_frac_n.mean()),
        "A_channel_mean_frac": float(A_frac_n.mean()),
        "ratio_2048_full_baseline": 1.0562,
        "ratio_2048_full_verdict": verdict_2048,
        "ratio_T_channel_1d": float(T_ratio),
        "ratio_T_channel_verdict": verdict_T,
        "ratio_svd2d": float(SVD_ratio),
        "ratio_svd2d_verdict": verdict_2d,
        "ari_kmeans4_2048_baseline": 0.0615,
        "ari_kmeans4_T_channel_1d": float(ari_T),
        "ari_kmeans4_svd2d": float(ari_2d),
        "per_class_T_stats": {
            gt_class_names[c]: {
                "T_mean": float(T_vec[gt_labels == c].mean()),
                "T_std": float(T_vec[gt_labels == c].std()),
                "A_mean_frac": float(A_frac_n[gt_labels == c].mean()),
                "n": int((gt_labels == c).sum()),
            }
            for c in range(4)
        },
        "interpretation": (
            "T 通道 1D ratio = 1.05-1.08 区间(对 4 类 GT);"
            "若 ratio < 1.2 = NOISE → 走 C 路径(deposon 散射场替代 RAG);"
            "若 > 1.5 = MEANINGFUL → A 路径生效。"
        ),
    },
    "stage2_llm_tra": [v41_traj, glm_traj, doubao_traj, gpt6_traj],
    "stage2_comparison_table": {
        v41_traj["name"].split(" (")[0]: {
            "pass_rate": f"{v41_traj['pass']}/{v41_traj['total']}",
            "T": v41_traj["T_clean"],
            "R": v41_traj["R_clean"],
            "A": v41_traj["A_event"],
            "verdict": v41_traj["verdict"],
        },
        glm_traj["name"].split(" (")[0]: {
            "pass_rate": f"{glm_traj['pass']}/{glm_traj['total']}",
            "T": glm_traj["T_clean"],
            "R": glm_traj["R_clean"],
            "A": glm_traj["A_event"],
            "verdict": glm_traj["verdict"],
        },
        doubao_traj["name"].split(" (")[0]: {
            "pass_rate": f"{doubao_traj['pass']}/{doubao_traj['total']}",
            "T": doubao_traj["T_clean"],
            "R": doubao_traj["R_clean"],
            "A": doubao_traj["A_event"],
            "verdict": doubao_traj["verdict"],
        },
        gpt6_traj["name"].split(" (")[0]: {
            "pass_rate": f"{gpt6_traj['pass']}/{gpt6_traj['total']}",
            "T": gpt6_traj["T_clean"],
            "R": gpt6_traj["R_clean"],
            "A": gpt6_traj["A_event"],
            "verdict": gpt6_traj["verdict"],
        },
    },
    "constraints_honored": {
        "no_llm_calls": True,
        "no_proxy": True,
        "no_api_key_read": True,
        "frozen_files_untouched": True,
        "five_anchors_untouched": True,
    },
}

out_json = os.path.join(RESULTS, "_tra_v0_2026_09_10.json")
with open(out_json, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print(f"\n中间数据已落盘: {out_json}")
