# -*- coding: utf-8 -*-
# deposon_fast.py — Deposon 场计算加固层（防超时，2026-08-28）
# 动机：复杂脑图/博弈论场景下原路径逐任务重复计算导致超时：
#   (i) 同一任务的前向轨迹在 mean-field/dirichlet 双臂间重复计算（≈2×浪费）；
#   (ii) 反向退火固定 50 步，0.9 收缩使后期更新指数级衰减（≈1.5–2×浪费）；
#   (iii) 逐任务/逐边重复建配置对象。
# 设计：新模块，旧代码（deposon_diffusion.py / run_v19_meanfield.py）零改动；
# 快路径等价性由 tests/test_fast.py 与 run_v20_fastcheck.py 证明：
#   早停判据触发时输出与完整 50 步的逐元差 < FAST_TOL（默认 1e-10，
#   远小于任何排序决策阈值 1e-6 tiebreak 间距）。
# no LLM API calls issued。
import time

import numpy as np

from deposon_diffusion import (DiffusionConfig, config_dict, denoise,
                               forward_diffuse)

FAST_TOL = 1e-10          # 早停输出与完整步数的最大逐元差硬上限（回归锁定）
EARLY_STOP_REL = 1e-12    # 相对更新阈值：max|ΔW|/max(W,eps) 低于此值即停
MIN_STEPS = 10            # 至少走的步数（避免过早退出）


def make_arm_cfg(cfg, inst_seed):
    return DiffusionConfig(**{**config_dict(cfg), "seed": inst_seed,
                              "energy_mode": "aggregate",
                              "field_guidance": True})


def reverse_denoise_fast(WT, mask, cfg, source, target, init_mode="dirichlet",
                         rel_tol=EARLY_STOP_REL, min_steps=MIN_STEPS):
    """reverse_denoise_init 的早停版：主体逐行相同，仅增加收敛早停。

    早停条件：步数 ≥ min_steps 且本步最大相对更新 < rel_tol。
    0.9 收缩下相对更新单调衰减 ⇒ 触发后剩余步数的累计影响 < 1e-10
    （run_v20_fastcheck.py 实测最大逐元差并锁定 FAST_TOL）。
    返回 (W_done, steps_taken)。

    候选 1 重构：实现已统一收敛到 deposon_diffusion.denoise（薄转发，
    early_stop=(rel_tol, min_steps)，数值逐位不变，tests/test_fast.py 锁定）。
    """
    W, steps_taken, _states = denoise(WT, mask, cfg, source, target,
                                      init_mode=init_mode,
                                      early_stop=(rel_tol, min_steps))
    return W, steps_taken


def field_scores_fast(W_obs, mask, cfg, source, target, inst_seed,
                      modes=("dirichlet", "prior_mean")):
    """同一任务的前向轨迹只算一次，多起点模式共享（核心 ≈2× 提速）。

    返回 {mode: (scores_matrix, steps_taken)}；scores 矩阵 mask 外为 -inf（掩码约定）。
    """
    cfg_arm = make_arm_cfg(cfg, inst_seed)
    traj = forward_diffuse(W_obs, mask, cfg_arm)
    WT = traj[-1]
    out = {}
    for mode in modes:
        W_done, steps = reverse_denoise_fast(WT, mask, cfg_arm, source, target,
                                             init_mode=mode)
        s = np.full_like(W_obs, -np.inf, dtype=float)
        s[mask] = W_done[mask]
        out[mode] = (s, steps)
    return out


# ---------------------------------------------------------------- 复杂度缩放基准
def scaling_benchmark(graphs, cfg, repeats=1):
    """逐图计时：整图全部留一任务（mean-field+dirichlet 共享轨迹）墙钟时间。
    返回 {graph_id: {N, n_edges, sec, sec_per_task, steps_mean}}。"""
    from run_v19_fullrank import full_candidate_mask
    from run_v15_experiment import row_normalize
    report = {}
    for g in graphs:
        N = g["N"]
        edges = [tuple(e) for e in g["edges"]]
        adj = np.zeros((N, N))
        for (u, v) in edges:
            adj[u, v] = 1.0
        W_true = row_normalize(adj)
        t0 = time.time()
        steps = []
        for _r in range(repeats):
            for ei, (u, v) in enumerate(edges):
                adj_obs = adj.copy(); adj_obs[u, v] = 0.0
                W_obs = W_true.copy(); W_obs[u, v] = 0.0
                mask = full_candidate_mask(N, u)
                out = field_scores_fast(W_obs, mask, cfg, g["source"],
                                        g["target"], int(g["seed"]) + ei)
                steps.append(out["prior_mean"][1])
        sec = (time.time() - t0) / repeats
        report[g["graph_id"]] = {
            "N": N, "n_edges": len(edges), "sec": round(sec, 3),
            "sec_per_task": round(sec / max(1, len(edges)), 4),
            "steps_mean": round(float(np.mean(steps)), 1),
            "steps_max": int(np.max(steps))}
    return report
