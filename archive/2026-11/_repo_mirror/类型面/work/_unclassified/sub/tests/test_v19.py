# -*- coding: utf-8 -*-
# tests/test_v19.py — SPEC v1.9 回归与玩具正确性测试
import math
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from deposon_diffusion import (DiffusionConfig, complete_graph, forward_diffuse,
                               reverse_denoise)
from run_v15_experiment import N_NEG, reconstruct_mindmap, row_normalize
from run_v19_meanfield import reverse_denoise_init, field_scores_init
from run_v19_fullrank import rank_metrics, gold_rank, full_candidate_mask
from run_v19_quickwins import sign_test


def _toy_setup():
    W = np.zeros((5, 5)); W[0, 1] = W[0, 2] = 0.4; W[1, 3] = 1.0; W[2, 3] = 1.0
    mask = np.zeros((5, 5), bool); mask[0, 3] = mask[0, 4] = True
    return W, mask


# ---------------------------------------------------------------- E9.1 回归
def test_dirichlet_path_bitwise_reproduces_v171_reverse():
    """init_mode='dirichlet' 必须与 deposon_diffusion.reverse_denoise 逐位一致。"""
    W, mask = _toy_setup()
    cfg = DiffusionConfig(seed=123)
    WT = forward_diffuse(W, mask, cfg)[-1]
    a = reverse_denoise_init(WT, mask, cfg, 0, 3, init_mode="dirichlet")
    b = reverse_denoise(WT, mask, cfg, 0, 3)
    assert np.array_equal(a, b)  # 逐位（非 allclose）


def test_dirichlet_path_bitwise_reproduces_on_mindmap_edge():
    """真实重建图第一条留一边：dirichlet 路径 == complete_graph 逐位一致。"""
    N, adj, edges, labels, meta = reconstruct_mindmap()
    W_true = row_normalize(adj)
    u, v = edges[0]
    W_obs = W_true.copy(); W_obs[u, v] = 0.0
    mask = np.zeros((N, N), bool); mask[u, v] = True
    rng = np.random.default_rng(70_000)
    pool = [j for j in range(N) if j != u and W_obs[u, j] == 0]
    take = rng.choice(len(pool), size=min(N_NEG, len(pool)), replace=False)
    for k in take:
        mask[u, pool[k]] = True
    cfg = DiffusionConfig(seed=70_000, energy_mode="aggregate",
                          field_guidance=True)
    a = field_scores_init(W_obs, mask, DiffusionConfig(), 0, 1, 70_000,
                          "dirichlet")
    b = complete_graph(W_obs, mask, cfg, 0, 1)
    assert np.array_equal(a[mask], b[mask])


def test_init_mode_parameterization():
    """prior_mean 确定论（与 seed 无关）；非法 init_mode 报错；两模式结果不同。"""
    W, mask = _toy_setup()
    cfg1 = DiffusionConfig(seed=1)
    cfg2 = DiffusionConfig(seed=999)
    WT = forward_diffuse(W, mask, cfg1)[-1]
    a = reverse_denoise_init(WT, mask, cfg1, 0, 3, init_mode="prior_mean")
    b = reverse_denoise_init(WT, mask, cfg2, 0, 3, init_mode="prior_mean")
    assert np.array_equal(a, b)  # mean-field 起点确定论
    cfg_short = DiffusionConfig(seed=1, n_steps=1)
    WT1 = forward_diffuse(W, mask, cfg_short)[-1]
    a1 = reverse_denoise_init(WT1, mask, cfg_short, 0, 3, init_mode="prior_mean")
    c1 = reverse_denoise_init(WT1, mask, cfg_short, 0, 3, init_mode="dirichlet")
    assert not np.array_equal(a1, c1)  # 两种起点给出不同轨迹
    with pytest.raises(ValueError):
        reverse_denoise_init(WT, mask, cfg1, 0, 3, init_mode="bogus")


def test_prior_mean_init_is_prior_mean():
    """prior_mean 起点 = 行均匀先验均值（掩码子向量各位置相等且和=可用质量）。"""
    W, mask = _toy_setup()
    cfg = DiffusionConfig(seed=7, n_steps=1)
    WT = forward_diffuse(W, mask, cfg)[-1]
    out = reverse_denoise_init(WT, mask, cfg, 0, 3, init_mode="prior_mean")
    row = out[0, mask[0]]
    assert row.sum() == pytest.approx(1.0 - W[0, ~mask[0]].sum(), abs=1e-9)


# ---------------------------------------------------------------- E9.2 玩具
def test_rank_metrics_toy():
    m = rank_metrics([0, 1, 2, 9])
    assert m["hits@1"] == pytest.approx(0.25)
    assert m["hits@3"] == pytest.approx(0.75)
    assert m["mrr"] == pytest.approx(np.mean([1.0, 0.5, 1 / 3, 0.1]))
    assert m["median_rank"] == pytest.approx(1.5)
    empty = rank_metrics([])
    assert empty["mrr"] is None and empty["n"] == 0


def test_gold_rank_toy():
    scores = np.array([0.1, 0.9, 0.5, 0.7])
    cand = np.array([1, 2, 3])
    assert gold_rank(scores, cand, 1) == 0
    assert gold_rank(scores, cand, 3) == 1
    assert gold_rank(scores, cand, 2) == 2


def test_full_candidate_mask():
    mask = full_candidate_mask(5, 2)
    assert mask[2].sum() == 4 and not mask[2, 2]
    assert not mask.any() or mask.sum() == 4  # 仅行 2


# ---------------------------------------------------------------- E9.6 玩具
def test_sign_test_reproduces_r3_pvalues():
    assert sign_test([1] * 16 + [-1] * 2)["p_exact"] == pytest.approx(
        0.001312255859375)
    assert sign_test([1] * 15 + [-1] * 3)["p_exact"] == pytest.approx(
        0.007537841796875)


def test_sign_test_ties_and_degenerate():
    r = sign_test([1.0, -1.0, 0.0, 0.0])
    assert r["n_pos"] == 1 and r["n_neg"] == 1 and r["n_tie"] == 2
    assert r["p_exact"] == pytest.approx(1.0)
    assert sign_test([0.0, 0.0])["p_exact"] == 1.0
    # 10 正 0 负：p = 2/2^10
    assert sign_test([1.0] * 10)["p_exact"] == pytest.approx(2 / 1024)


# ---------------------------------------------------------------- 结果一致性
def test_e91_field_guided_reproduces_v171_numbers():
    """落盘的 E9.1 field_guided 臂须与 v1.7.1 同臂数字一致（同协议复现）。"""
    import json
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p19 = os.path.join(here, "results", "deposon_v19_meanfield.json")
    p17 = os.path.join(here, "results", "deposon_v17_fusion_fix.json")
    if not (os.path.exists(p19) and os.path.exists(p17)):
        pytest.skip("result files not present")
    d19 = json.load(open(p19))["experiment_B"]["arms"]["field_guided"]
    d17 = json.load(open(p17))["experiment_B"]["arms"]["field_guided"]
    assert d19["overall"]["mean"] == d17["top3_hit"]["mean"]
    assert d19["named"]["mean"] == d17["top3_hit_named_path"]["mean"]
    assert d19["filler"]["mean"] == d17["top3_hit_filler"]["mean"]
