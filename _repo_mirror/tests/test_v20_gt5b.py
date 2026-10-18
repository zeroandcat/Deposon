# -*- coding: utf-8 -*-
# GT-5b（全语料单调性复核 + 主张收窄）回归测试：判定字段机械锁定 + 微型合成图冒烟。
import numpy as np
import pytest

from deposon_diffusion import DiffusionConfig, forward_diffuse
from run_v20_gt5b import (GT5B_DEAD_MIN_GRAPHS, GT5B_MONO_DEAD,
                          GT5B_PASS_GRAPH_FRAC, gt5b_verdict)
from run_v20_gt5 import phi_trajectory, reverse_denoise_traj
from run_v15_experiment import row_normalize


def _pg(rates):
    return {f"g{i}": {"meanfield_monotone_rate": r} for i, r in enumerate(rates)}


def test_verdict_supports_when_frac_full_above_pass():
    pg = _pg([1.0] * 18 + [0.9] * 4)  # 18/22 ≈ 0.818 ≥ 0.8
    v = gt5b_verdict(pg)
    assert v["verdict"] == "supports_narrowed_monotonicity"
    assert v["supported_narrowed_claim"] is True
    assert v["frac_graphs_full_monotonicity"] == pytest.approx(18 / 22)


def test_verdict_dead_when_three_graphs_below_half():
    pg = _pg([1.0] * 19 + [0.4, 0.3, 0.1])
    v = gt5b_verdict(pg)
    assert v["verdict"] == "H_GT5b_dead"
    assert v["supported_narrowed_claim"] is False
    assert len(v["graphs_below_50pct_monotonicity"]) == GT5B_DEAD_MIN_GRAPHS


def test_verdict_inconclusive_band():
    pg = _pg([1.0] * 15 + [0.9] * 7)  # 15/22 ≈ 0.68 < 0.8, 无判死图
    v = gt5b_verdict(pg)
    assert v["verdict"] == "inconclusive_preregistered_undefined_band"
    assert v["supported_narrowed_claim"] is False


def test_verdict_threshold_constants_frozen():
    assert GT5B_PASS_GRAPH_FRAC == 0.8
    assert GT5B_MONO_DEAD == 0.5
    assert GT5B_DEAD_MIN_GRAPHS == 3


def test_tiny_graph_monotonicity_smoke():
    """5 节点 DAG 冒烟：轨迹 Φ 有限且单调率 ∈ [0,1]。"""
    N = 5
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (1, 4)]
    adj = np.zeros((N, N))
    for (u, v) in edges:
        adj[u, v] = 1.0
    W = row_normalize(adj)
    W[0, 1] = 0.0
    mask = np.zeros((N, N), bool)
    mask[0, :] = True
    mask[0, 0] = False
    cfg = DiffusionConfig(n_steps=6, seed=5, energy_mode="aggregate",
                          field_guidance=True)
    WT = forward_diffuse(W, mask, cfg)[-1]
    states = reverse_denoise_traj(WT, mask, cfg, 0, 4, init_mode="prior_mean")
    phi = phi_trajectory(states, 0, 4)
    assert all(np.isfinite(v) for v in phi)
    from run_v20_gt5 import monotone_rate
    rate = monotone_rate(phi)
    assert 0.0 <= rate <= 1.0
