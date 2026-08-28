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
# 实测结论（Findings_v2.0_hardening §二）：本调度下早停从不触发（相对更新
# 地板 ~10%/步），固定 50 步为正确选择；提速来自轨迹共享（1.34×）。
# no LLM API calls issued。
import time

import numpy as np

from deposon_diffusion import (DiffusionConfig, config_dict, forward_diffuse,
                               _project_masked, _walk_sums, _G_AETHER, _EPS,
                               _masked_row_stats)
from run_v19_meanfield import INIT_MODES

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
    """
    WT = np.asarray(WT, dtype=float)
    mask = np.asarray(mask, dtype=bool)
    if init_mode not in INIT_MODES:
        raise ValueError(f"unknown init_mode: {init_mode}")
    W = WT.copy()
    if cfg.n_steps <= 0:
        return W, 0
    if init_mode == "dirichlet":
        rng = np.random.default_rng(cfg.seed)
        for i in range(W.shape[0]):
            idx, m, p = _masked_row_stats(W, mask, i)
            if m == 0:
                continue
            mass = p * m
            if mass > 0.0:
                W[i, idx] = mass * rng.dirichlet(np.ones(m))
        _project_masked(W, mask)
    else:
        _project_masked(W, mask)
    steps_taken = 0
    for _t in range(cfg.n_steps, 0, -1):
        grad = np.zeros_like(W)
        if cfg.field_guidance and source != target:
            x, y = _walk_sums(W, source, target)
            xt = max(float(x[target]), _EPS)
            wpos = np.maximum(W, _EPS)
            dtdw = np.where(W > _EPS, 1.0 / (1.0 + _G_AETHER * wpos) ** 2, 0.0)
            grad -= (x[:, None] * y[None, :]) * (dtdw / xt)
        if cfg.lam_smooth:
            grad[mask] += 2.0 * cfg.lam_smooth * W[mask]
        W_prev = W[mask].copy()
        W[mask] *= np.exp(-cfg.lr * W[mask] * grad[mask])
        W[mask] = (1.0 - cfg.lr) * W[mask]
        W[~mask] = WT[~mask]
        _project_masked(W, mask)
        steps_taken += 1
        if steps_taken >= min_steps:
            denom = np.maximum(np.abs(W_prev), _EPS)
            rel = np.max(np.abs(W[mask] - W_prev) / denom) if W_prev.size else 0.0
            if rel < rel_tol:
                break
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
