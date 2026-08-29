# -*- coding: utf-8 -*-
# ============================================================
# Deposon 实验协议库 (ARCH_AUDIT v2 候选 2 重构)
#
# v15–v20 实验族共享的评估协议函数集中于此。此前它们定义在带 main() 与
# 模块级实验常量的 run_* 脚本里, 被 8–18 个下游脚本跨文件 import ——
# import 一个协议函数就拖入对方脚本的全部模块级副作用。
#
# 迁移清单 (原位置均保留薄转发, 签名与数值语义逐位不变):
#   row_normalize        (原 run_v15_experiment.py:47, 18 个 import 方)
#   prior_score_matrix   (原 run_v16_llm_prior.py:55, 11 个 import 方)
#   full_candidate_mask  (原 run_v19_fullrank.py:24, 14 个 import 方)
#   gold_rank            (原 run_v19_fullrank.py:44, 8 个 import 方)
#   field_scores_init    (原 run_v19_meanfield.py:78, 11 个 import 方)
#
# 本模块零 I/O、零网络、无模块级实验常量, 仅依赖 numpy 与 deposon_diffusion。
# ============================================================
import numpy as np

from deposon_diffusion import DiffusionConfig, config_dict, denoise, forward_diffuse


def row_normalize(adj: np.ndarray) -> np.ndarray:
    """出边权重行归一 (1/outdeg); 零出度节点保持零行。"""
    W = np.zeros_like(adj, dtype=float)
    outdeg = adj.sum(axis=1)
    nz = outdeg > 0
    W[nz] = adj[nz] / outdeg[nz, None]
    return W


def prior_score_matrix(prior: dict, shape) -> np.ndarray:
    """dict[(u,v)]→confidence 展开为稠密矩阵; 先验未覆盖位置为 0。"""
    P = np.zeros(shape, dtype=float)
    for (u, v), c in prior.items():
        if 0 <= u < shape[0] and 0 <= v < shape[1]:
            P[u, v] = c
    return P


def full_candidate_mask(N, u):
    """全候选 mask：行 u 的全部非自身列（含其他观测出边——raw 口径，预登记）。"""
    mask = np.zeros((N, N), bool)
    mask[u, :] = True
    mask[u, u] = False
    return mask


def gold_rank(scores_row, cand, v):
    """金边 v 在候选 cand 中按 scores_row 降序（mergesort 稳定）的秩（0 基）。"""
    order = cand[np.argsort(-scores_row[cand], kind="mergesort")]
    return int(np.flatnonzero(order == v)[0])


def field_scores_init(W_obs, mask, cfg, source, target, inst_seed, init_mode):
    """完整臂打分（aggregate 能量），起点由 init_mode 决定。"""
    cfg_arm = DiffusionConfig(**{**config_dict(cfg), "seed": inst_seed,
                                 "energy_mode": "aggregate",
                                 "field_guidance": True})
    traj = forward_diffuse(W_obs, mask, cfg_arm)
    W_done, _steps, _states = denoise(traj[-1], mask, cfg_arm, source, target,
                                      init_mode=init_mode)
    out = np.full_like(W_obs, -np.inf, dtype=float)
    out[mask] = W_done[mask]
    return out
