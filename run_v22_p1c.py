# -*- coding: utf-8 -*-
# Deposon v2.2 T-P1c：残余主张「一阶方向 = 熵正则势 Φ_τ = Φ + τ·H 的镜像上升」
# 的证明/证伪检验 → results/deposon_v22_p1c.json。
#
# 预登记（先于运行承诺，判定为纯函数机械求值，tests/test_v22_p1c.py 锁定）：
#   对象：与 v21 同一穷举集（SEED=210021 图族 × 全节点 u × 轨迹状态对），
#         mean-field 实际位移 d = (W1−W0)[u,idx]（含乘性更新+衰减+投影全结构）。
#   候选方向：KL 几何下 Φ_τ 的一阶镜像上升位移（切空间投影）
#         d_kl(τ) = w∘ĝ − w·(w·ĝ)·1,  ĝ = ∇Φ_row + τ·∇H_row,
#         ∇H_e = −(log w_e + 1)（行熵 H = −Σ w log w）。
#   τ 网格：TAU_GRID = linspace(0, 4, 81)，冻结，不看结果调格。
#   判死线（两条，任一触发即记）：
#     强式（全局 τ）：max_τ min_states cos(d, d_kl(τ)) < 0.999
#         ⇒ 「存在单一 τ 使一阶方向在全穷举集一致」判死。
#     弱式（逐状态 τ*）：min_states max_τ cos < 0.99
#         ⇒ 即使允许 τ 随状态变化也不一致 ⇒ P1c 完全判死。
#   披露口径：d 或 d_kl 零向量（‖·‖≤1e-14）按平凡对齐 cos=1.0 计数并单列；
#         另报逐状态 τ* 分布与 best-τ 下逐分量符号一致率（描述性，不入判定）。
# 零 API、零网络、种子冻结（复用 v21 图族与 mean-field 轨迹口径）。
import json
import os
import time

import numpy as np

from deposon_diffusion import DiffusionConfig, denoise, _EPS
from deposon_protocol import row_normalize, full_candidate_mask
from run_v21_gtformal import (graph_suite, pick_source_target, grad_phi,
                              SEED, TRAJ_STEPS)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(HERE, "results", "deposon_v22_p1c.json")

TAU_GRID = np.linspace(0.0, 4.0, 81).round(10)   # 冻结 τ 网格
COS_STRONG, COS_WEAK, ZERO_TOL = 0.999, 0.99, 1e-14


def state_pairs(adj, source, target, u, cfg):
    """与 v21 eval_task 同口径的 mean-field 轨迹状态对。"""
    mask = full_candidate_mask(adj.shape[0], u)
    WT = row_normalize(adj)
    WT[mask] = 0.0
    _, _, states = denoise(WT, mask, cfg, source, target,
                           init_mode="prior_mean", record=True)
    idx = np.flatnonzero(mask[u])
    return states, idx


def d_kl_direction(w, g_phi, tau):
    """KL 切空间一阶镜像上升位移：w∘ĝ 投影到行单纯形切空间。"""
    g = g_phi + tau * (-(np.log(np.maximum(w, _EPS)) + 1.0))
    d = w * g
    return d - w * float(d.sum()) / max(float(w.sum()), _EPS)


def cos_align(a, b):
    na, nb = float(np.linalg.norm(a)), float(np.linalg.norm(b))
    if na <= ZERO_TOL or nb <= ZERO_TOL:
        return 1.0, True           # 零向量：平凡对齐（披露口径）
    return float(a @ b) / (na * nb), False


def sign_agreement(a, b):
    nz = (np.abs(a) > ZERO_TOL) | (np.abs(b) > ZERO_TOL)
    if not nz.any():
        return None
    return float(np.mean(np.sign(a[nz]) == np.sign(b[nz])))


# ---------------------------------------------------------- 判定纯函数（预登记，先承诺）
def verdict_p1c(per_state_best_cos, global_min_cos):
    """per_state_best_cos: 逐状态 max_τ cos 列表；global_min_cos: 逐 τ 的 min_states cos。
    返回 {'strong': ..., 'weak': ..., 'verdict': ...}；不看数值内容，机械求值。"""
    strong_dead = max(global_min_cos) < COS_STRONG
    weak_dead = min(per_state_best_cos) < COS_WEAK
    if weak_dead:
        v = "killed"                     # 连逐状态 τ* 都不一致
    elif strong_dead:
        v = "survives_state_dependent"   # 仅存逐状态 τ* 版
    else:
        v = "survives_global_tau"        # 存在全局 τ（τ* 见 global_argmax）
    return {"strong_global_tau": "killed" if strong_dead else "survives",
            "weak_state_dependent": "killed" if weak_dead else "survives",
            "verdict": v,
            "tau_star_global": (float(TAU_GRID[int(np.argmax(global_min_cos))])
                                if not strong_dead else None),
            "min_cos_at_best_global_tau": float(max(global_min_cos)),
            "min_cos_per_state_best_tau": float(min(per_state_best_cos))}


def main():
    t0 = time.time()
    cfg = DiffusionConfig(n_steps=TRAJ_STEPS, seed=SEED)
    n_tau = len(TAU_GRID)
    sum_cos = np.zeros(n_tau)          # 逐 τ 的 cos 累积（取 min 用）
    min_cos = np.full(n_tau, np.inf)
    per_state_best, best_taus, sign_rates, n_trivial = [], [], [], 0
    n_states = 0
    for g in graph_suite():
        source, target = pick_source_target(g["adj"])
        for u in range(g["adj"].shape[0]):
            states, idx = state_pairs(g["adj"], source, target, u, cfg)
            for k in range(len(states) - 1):
                W0, W1 = states[k], states[k + 1]
                w = W0[u, idx]
                d = (W1 - W0)[u, idx]
                g_phi = grad_phi(W0, source, target)[u, idx]
                cos_row = np.empty(n_tau)
                for j, tau in enumerate(TAU_GRID):
                    c, triv = cos_align(d, d_kl_direction(w, g_phi, tau))
                    cos_row[j] = c
                jb = int(np.argmax(cos_row))
                per_state_best.append(float(cos_row[jb]))
                best_taus.append(float(TAU_GRID[jb]))
                sr = sign_agreement(d, d_kl_direction(w, g_phi, TAU_GRID[jb]))
                if sr is not None:
                    sign_rates.append(sr)
                min_cos = np.minimum(min_cos, cos_row)
                n_states += 1
    v = verdict_p1c(per_state_best, min_cos)
    taus = np.array(best_taus)
    out = {
        "spec": "docs/GT_FORMALIZATION_v1.md §2 P1c + 本文件头预登记判死线",
        "seed": SEED, "tau_grid": [float(TAU_GRID[0]), float(TAU_GRID[-1]), n_tau],
        "n_states": n_states,
        "verdict": v,
        "descriptive": {
            "tau_star_per_state": {"median": float(np.median(taus)),
                                   "p10": float(np.percentile(taus, 10)),
                                   "p90": float(np.percentile(taus, 90)),
                                   "frac_at_tau0": float(np.mean(taus == 0.0))},
            "sign_agreement_at_best_tau_median":
                float(np.median(sign_rates)) if sign_rates else None,
        },
        "runtime_sec": round(time.time() - t0, 2),
        "note": "判定纯函数 verdict_p1c 先于运行承诺并测试锁定；τ 网格冻结；"
                "零向量按平凡对齐披露；survives_state_dependent 如实收窄主张。",
    }
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(json.dumps(out, ensure_ascii=False, indent=1))
    print(json.dumps({"verdict": v["verdict"],
                      "strong": v["strong_global_tau"], "weak": v["weak_state_dependent"],
                      "min_cos_best_global": v["min_cos_at_best_global_tau"],
                      "min_cos_per_state": v["min_cos_per_state_best_tau"],
                      "tau_median": out["descriptive"]["tau_star_per_state"]["median"]},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
