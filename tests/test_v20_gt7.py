# -*- coding: utf-8 -*-
# GT-7（温度-命中率-势前沿扫描）回归测试：α=1 逐位复现 GT-5 dirichlet 臂、
# α 单调性语义、判定规则机械锁定。微型合成图 + 少步数，毫秒级完成；
# 不触碰 results 主档。
import numpy as np
import pytest

from deposon_diffusion import DiffusionConfig, forward_diffuse
from run_v15_experiment import row_normalize
from run_v20_gt5 import phi_potential, reverse_denoise_traj
from run_v20_gt7 import (GT7_ALPHAS, GT7_HIT_FRAC, GT7_PASS_GRAPH_FRAC,
                         GT7_SEEDS, frontier_shape, gt7_verdict, hit_at_3,
                         reverse_denoise_traj_alpha)


def _tiny_instance(n_steps=8, seed=5):
    """5 节点 DAG 留一实例：source=0, target=4（同 test_v20_gt5 口径）。"""
    N = 5
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (1, 4)]
    adj = np.zeros((N, N))
    for (u, v) in edges:
        adj[u, v] = 1.0
    W = row_normalize(adj)
    u, v = 0, 1
    W_obs = W.copy()
    W_obs[u, v] = 0.0
    mask = np.zeros((N, N), bool)
    mask[u, :] = True
    mask[u, u] = False
    cfg = DiffusionConfig(n_steps=n_steps, seed=seed, energy_mode="aggregate",
                          field_guidance=True)
    WT = forward_diffuse(W_obs, mask, cfg)[-1]
    return WT, mask, cfg


def test_alpha1_bitwise_reproduces_gt5_dirichlet():
    """α=1.0 档必须与 GT-5 的 dirichlet 臂逐位一致（同一 rng 调用次序）。"""
    WT, mask, cfg = _tiny_instance()
    a = reverse_denoise_traj_alpha(WT, mask, cfg, 0, 4, alpha=1.0)
    b = reverse_denoise_traj(WT, mask, cfg, 0, 4, init_mode="dirichlet")
    assert len(a) == len(b) == cfg.n_steps + 1
    for sa, sb in zip(a, b):
        np.testing.assert_array_equal(sa, sb)


def test_alpha_controls_init_concentration():
    """α 语义：小 α 起点更集中（高温探索），大 α 起点更接近均匀（低温）。

    用起点（轨迹第 0 点）行 0 的最大权重刻画集中度；多种子下
    α=0.3 的集中度期望必须严格高于 α=20。
    """
    WT, mask, _ = _tiny_instance()
    n = mask[0].sum()

    def concentration(alpha, seed):
        cfg = DiffusionConfig(n_steps=8, seed=seed, energy_mode="aggregate",
                              field_guidance=True)
        st0 = reverse_denoise_traj_alpha(WT, mask, cfg, 0, 4, alpha)[0]
        return float(np.max(st0[0, mask[0]]))

    hot = np.mean([concentration(0.3, s) for s in range(20)])
    cold = np.mean([concentration(20.0, s) for s in range(20)])
    assert hot > cold
    # 大 α 起点接近期望质量均分
    assert cold == pytest.approx(1.0 / n, rel=0.35)


def test_meanfield_arm_is_deterministic_and_rng_free():
    """alpha=None（T=0 端点）两次运行逐位一致且与 seed 无关。"""
    WT, mask, _ = _tiny_instance()
    cfg1 = DiffusionConfig(n_steps=8, seed=1, energy_mode="aggregate",
                           field_guidance=True)
    cfg2 = DiffusionConfig(n_steps=8, seed=999, energy_mode="aggregate",
                           field_guidance=True)
    a = reverse_denoise_traj_alpha(WT, mask, cfg1, 0, 4, None)
    b = reverse_denoise_traj_alpha(WT, mask, cfg2, 0, 4, None)
    for sa, sb in zip(a, b):
        np.testing.assert_array_equal(sa, sb)
    # 终点 Φ 有限
    assert np.isfinite(phi_potential(a[-1], 0, 4))


def test_invalid_alpha_rejected():
    WT, mask, cfg = _tiny_instance()
    with pytest.raises(ValueError):
        reverse_denoise_traj_alpha(WT, mask, cfg, 0, 4, alpha=0.0)
    with pytest.raises(ValueError):
        reverse_denoise_traj_alpha(WT, mask, cfg, 0, 4, alpha=-1.0)


def test_hit_at_3_matches_gold_rank():
    """Hits@3 与 GT-1 同一 gold_rank 全候选口径：秩 < 3 记命中。"""
    WT, mask, cfg = _tiny_instance()
    W = reverse_denoise_traj_alpha(WT, mask, cfg, 0, 4, None)[-1]
    h = hit_at_3(W, mask, 0, 1)
    assert h in (0.0, 1.0)
    from run_v19_fullrank import gold_rank
    cand = np.flatnonzero(mask[0])
    assert h == float(gold_rank(W[0], cand, 1) < 3)


def _pg(specs):
    """specs: gid → (mf_hits, mf_phi, [(hits_mean, phi_mean), ...])"""
    return {gid: {"meanfield": {"hits": mh, "phi": mp},
                  "temperatures": {f"t{i}": {"hits_mean": h, "phi_mean": p}
                                   for i, (h, p) in enumerate(ts)}}
            for gid, (mh, mp, ts) in specs.items()}


def test_verdict_supports_frontier():
    """3/4 图存在中间档（命中率 ≥0.9×mf 且 Φ > mf）⇒ supports_tradeoff_frontier。"""
    pg = _pg({
        "g1": (0.5, -2.0, [(0.48, -1.9), (0.3, -1.8)]),
        "g2": (0.5, -2.0, [(0.46, -1.95)]),
        "g3": (0.5, -2.0, [(0.50, -1.99)]),
        "g4": (0.5, -2.0, [(0.2, -2.1)]),   # 无前沿档
    })
    v = gt7_verdict(pg)
    assert v["verdict"] == "supports_tradeoff_frontier"
    assert v["frac_graphs_with_frontier_temp"] == pytest.approx(0.75)
    assert set(v["graphs_with_frontier_temp"]) == {"g1", "g2", "g3"}


def test_verdict_no_tradeoff_codirectional():
    """全部图全部档同向（噪声升则两者同降）⇒ no_tradeoff。"""
    pg = _pg({
        "g1": (0.5, -2.0, [(0.4, -2.1), (0.3, -2.2)]),
        "g2": (0.6, -1.0, [(0.5, -1.1), (0.55, -1.0)]),  # 等值不算反向
    })
    v = gt7_verdict(pg)
    assert v["verdict"] == "no_tradeoff"
    assert not v["supported_tradeoff_frontier"]
    assert v["all_graphs_codirectional"]


def test_verdict_mixed():
    """部分图有反向档但不足以达 3/4 ⇒ mixed，不美化。"""
    pg = _pg({
        "g1": (0.5, -2.0, [(0.48, -1.9)]),  # 有前沿档
        "g2": (0.5, -2.0, [(0.4, -2.1)]),
        "g3": (0.5, -2.0, [(0.4, -2.1)]),
        "g4": (0.5, -2.0, [(0.4, -2.1)]),
    })
    v = gt7_verdict(pg)
    assert v["verdict"] == "mixed"
    assert v["frac_graphs_with_frontier_temp"] == pytest.approx(0.25)
    assert v["per_graph_direction"]["g1"]["frontier_temps"] == ["t0"]


def test_frontier_shape_flat_and_monotone():
    temps = {str(a): {"hits_mean": h, "phi_mean": p}
             for a, h, p in [(0.3, 0.1, -1.0), (1.0, 0.5, -1.0),
                             (20.0, 0.9, -1.0)]}
    sh = frontier_shape(temps)
    assert sh["hits_mean"]["shape"] == "increasing_with_alpha"
    assert sh["phi_mean"]["shape"] == "flat"
    assert sh["phi_mean"]["logalpha_corr"] == 0.0


def test_frozen_constants():
    assert GT7_ALPHAS == (0.3, 0.5, 1.0, 2.0, 5.0, 20.0)
    assert GT7_SEEDS >= 5
    assert GT7_HIT_FRAC == 0.9
    assert GT7_PASS_GRAPH_FRAC == 0.75
