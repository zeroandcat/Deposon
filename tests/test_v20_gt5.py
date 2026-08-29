# -*- coding: utf-8 -*-
# GT-5（势函数单调性）回归测试：轨迹长度、Φ 有限性、判定字段机械锁定。
# 使用微型合成图 + 少步数，毫秒级完成；不触碰 results 主档。
import json
import os

import numpy as np
import pytest

from deposon_diffusion import DiffusionConfig, forward_diffuse
from run_v20_gt5 import (GT5_TOL, gt5_verdict, monotone_rate, phi_potential,
                         phi_trajectory, reverse_denoise_traj)


def _tiny_instance(n_steps=8, seed=5):
    """5 节点 DAG 留一实例：source=0, target=4。"""
    N = 5
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (1, 4)]
    adj = np.zeros((N, N))
    for (u, v) in edges:
        adj[u, v] = 1.0
    from run_v15_experiment import row_normalize
    W = row_normalize(adj)  # 零出度行 → 均匀行，避免 NaN
    u, v = 0, 1
    W_obs = W.copy()
    W_obs[u, v] = 0.0
    mask = np.zeros((N, N), bool)
    mask[u, :] = True
    mask[u, u] = False
    cfg = DiffusionConfig(n_steps=n_steps, seed=seed, energy_mode="aggregate",
                          field_guidance=True)
    traj = forward_diffuse(W_obs, mask, cfg)
    states = reverse_denoise_traj(traj[-1], mask, cfg, 0, 4,
                                  init_mode="prior_mean")
    return states, cfg


def test_trajectory_length():
    """轨迹长度 = n_steps+1（含起点），mean-field 与 dirichlet 同构。"""
    n_steps = 8
    states, cfg = _tiny_instance(n_steps=n_steps)
    assert len(states) == n_steps + 1
    traj = forward_diffuse(np.zeros((5, 5)), np.zeros((5, 5), bool), cfg)
    assert len(traj) == n_steps + 1


def test_phi_finite_along_trajectory():
    """整条轨迹 Φ 有限（无 NaN/inf），且势函数与能量函数符号相反。"""
    states, _ = _tiny_instance()
    phi = phi_trajectory(states, 0, 4)
    assert len(phi) == len(states)
    assert all(np.isfinite(v) for v in phi)
    from deposon_diffusion import scatter_energy
    e = scatter_energy(states[0], None, 0, 4, energy_mode="aggregate")
    assert phi_potential(states[0], 0, 4) == pytest.approx(-e)


def test_monotone_rate_bounds_and_tol():
    """单调率定义：全不减轨迹为 1.0，含下降步按比例计，容差 1e-9。"""
    assert monotone_rate([0.0, 1.0, 2.0, 2.0]) == 1.0
    assert monotone_rate([0.0, 1.0, 0.5, 1.0]) == pytest.approx(2 / 3)
    assert monotone_rate([0.0, -GT5_TOL / 2]) == 1.0      # 容差内
    assert monotone_rate([0.0, -10 * GT5_TOL]) == 0.0     # 超容差
    assert monotone_rate([1.0]) == 1.0


def test_gt5_verdict_fields_and_mechanics():
    """判定字段存在且机械规则正确（支持 / 斩杀 / 未定义带三分支）。"""
    good = {"G1": {"meanfield_monotone_rate": 1.0,
                   "dirichlet_mean_endpoint": 0.0,
                   "meanfield_mean_endpoint": 1.0},
            "G2": {"meanfield_monotone_rate": 1.0,
                   "dirichlet_mean_endpoint": 0.0,
                   "meanfield_mean_endpoint": 1.0},
            "G3": {"meanfield_monotone_rate": 1.0,
                   "dirichlet_mean_endpoint": 0.0,
                   "meanfield_mean_endpoint": 1.0},
            "G4": {"meanfield_monotone_rate": 1.0,
                   "dirichlet_mean_endpoint": 0.0,
                   "meanfield_mean_endpoint": 1.0}}
    v = gt5_verdict(good)
    for key in ("verdict", "supported_potential_game",
                "graphs_with_full_monotonicity",
                "frac_graphs_full_monotonicity",
                "graphs_below_50pct_monotonicity",
                "dirichlet_endpoint_below_meanfield_all_graphs",
                "n_graphs", "thresholds"):
        assert key in v
    assert v["verdict"] == "supports_potential_game_framework"
    assert v["frac_graphs_full_monotonicity"] == pytest.approx(1.0)

    # 满分占比 3/4 = 0.75 < 0.8 ⇒ 落预登记未定义带，不得报支持
    band = dict(good)
    band["G4"] = {"meanfield_monotone_rate": 0.8,
                  "dirichlet_mean_endpoint": 0.0,
                  "meanfield_mean_endpoint": 1.0}
    v_band = gt5_verdict(band)
    assert v_band["frac_graphs_full_monotonicity"] == pytest.approx(0.75)
    assert v_band["verdict"] == "inconclusive_preregistered_undefined_band"

    dead = dict(good)
    dead["G2"] = {"meanfield_monotone_rate": 0.3,
                  "dirichlet_mean_endpoint": 0.0,
                  "meanfield_mean_endpoint": 1.0}
    dead["G4"] = {"meanfield_monotone_rate": 0.1,
                  "dirichlet_mean_endpoint": 0.0,
                  "meanfield_mean_endpoint": 1.0}
    assert gt5_verdict(dead)["verdict"] == "H_GT5_dead"

    # 单调率满分但终点条件不满足 ⇒ 预登记未定义带，不得报支持
    bad_end = dict(good)
    bad_end["G3"] = {"meanfield_monotone_rate": 1.0,
                     "dirichlet_mean_endpoint": 2.0,
                     "meanfield_mean_endpoint": 1.0}
    assert gt5_verdict(bad_end)["verdict"] == (
        "inconclusive_preregistered_undefined_band")


def test_results_json_schema_if_present():
    """若 results/deposon_v20_gt5.json 已生成，锁定顶层判定/honesty 字段。"""
    path = os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "results", "deposon_v20_gt5.json")
    if not os.path.exists(path):
        pytest.skip("GT-5 主档尚未生成")
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    for key in ("verdict", "honesty", "per_graph_summary",
                "potential_function", "preregistered"):
        assert key in d
    assert d["verdict"]["verdict"] in (
        "supports_potential_game_framework", "H_GT5_dead",
        "inconclusive_preregistered_undefined_band")
    assert isinstance(d["honesty"], list) and d["honesty"]
