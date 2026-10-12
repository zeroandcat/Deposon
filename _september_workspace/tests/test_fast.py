# -*- coding: utf-8 -*-
# tests/test_fast.py — deposon_fast 加固层回归（等价性/共享轨迹/缩放不爆炸）
import numpy as np
import pytest

from deposon_diffusion import DiffusionConfig, forward_diffuse
from mindmap_corpus_v20 import CORPUS_DIR, load_corpus
from run_v15_experiment import row_normalize
from run_v19_fullrank import full_candidate_mask, gold_rank
from run_v19_meanfield import reverse_denoise_init
from deposon_fast import (FAST_TOL, field_scores_fast, make_arm_cfg,
                          reverse_denoise_fast)

cfg = DiffusionConfig()
_graphs = {g["graph_id"]: g for g in load_corpus(CORPUS_DIR, families=("S",))}


def _setup(gid, ei=0):
    g = _graphs[gid]
    N = g["N"]
    edges = [tuple(e) for e in g["edges"]]
    adj = np.zeros((N, N))
    for (u, v) in edges:
        adj[u, v] = 1.0
    W_true = row_normalize(adj)
    u, v = edges[ei]
    adj_obs = adj.copy(); adj_obs[u, v] = 0.0
    W_obs = W_true.copy(); W_obs[u, v] = 0.0
    mask = full_candidate_mask(N, u)
    return g, N, u, v, W_obs, mask


@pytest.mark.parametrize("gid", ["S1", "S2", "S6"])
@pytest.mark.parametrize("mode", ["prior_mean", "dirichlet"])
def test_fast_equals_slow_bit_identical(gid, mode):
    """快路径（早停版）与原 reverse_denoise_init 逐位一致（早停不触发时）。"""
    g, N, u, v, W_obs, mask = _setup(gid)
    ca = make_arm_cfg(cfg, int(g["seed"]))
    traj = forward_diffuse(W_obs, mask, ca)
    W_slow = reverse_denoise_init(traj[-1], mask, ca, 0, 1, init_mode=mode)
    W_fast, _st = reverse_denoise_fast(traj[-1], mask, ca, 0, 1, init_mode=mode)
    assert np.max(np.abs(W_slow - W_fast)) < FAST_TOL


@pytest.mark.parametrize("mode", ["prior_mean", "dirichlet"])
def test_shared_trajectory_modes_identical_to_slow(mode):
    """field_scores_fast 共享轨迹的两臂输出与独立慢路径逐位一致。"""
    g, N, u, v, W_obs, mask = _setup("S6", ei=2)
    ca = make_arm_cfg(cfg, int(g["seed"]) + 2)
    traj = forward_diffuse(W_obs, mask, ca)
    W_slow = reverse_denoise_init(traj[-1], mask, ca, 0, 1, init_mode=mode)
    out = field_scores_fast(W_obs, mask, cfg, g["source"], g["target"],
                            int(g["seed"]) + 2)
    s_fast, _st = out[mode]
    assert np.allclose(s_fast[mask], W_slow[mask], atol=FAST_TOL, rtol=0)


def test_rank_preserved_on_all_families():
    """全部 6 族主档图上 named Hits@3 快慢路径逐位一致（排序级等价）。"""
    for gid, g in _graphs.items():
        N = g["N"]
        edges = [tuple(e) for e in g["edges"]]
        named = {tuple(e) for e in g["named_edges"]}
        adj = np.zeros((N, N))
        for (u, v) in edges:
            adj[u, v] = 1.0
        W_true = row_normalize(adj)
        hits_slow, hits_fast = [], []
        for ei, (u, v) in enumerate(edges[:6]):
            adj_obs = adj.copy(); adj_obs[u, v] = 0.0
            W_obs = W_true.copy(); W_obs[u, v] = 0.0
            mask = full_candidate_mask(N, u)
            cand = np.flatnonzero(mask[u])
            ca = make_arm_cfg(cfg, int(g["seed"]) + ei)
            traj = forward_diffuse(W_obs, mask, ca)
            W_slow = reverse_denoise_init(traj[-1], mask, ca,
                                          g["source"], g["target"],
                                          init_mode="prior_mean")
            out = field_scores_fast(W_obs, mask, cfg, g["source"],
                                    g["target"], int(g["seed"]) + ei)
            W_fast = out["prior_mean"][0]
            hits_slow.append(gold_rank(W_slow[u], cand, v))
            hits_fast.append(gold_rank(W_fast[u], cand, v))
        assert hits_slow == hits_fast, gid
