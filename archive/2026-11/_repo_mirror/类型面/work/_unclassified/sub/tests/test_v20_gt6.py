# -*- coding: utf-8 -*-
# GT-6（Candogan 流分解）回归测试：Hodge 分解正交性/幂等性 + 判定机械锁定。
import numpy as np
import pytest

from run_v20_gt6 import (GT6_APPROX_MEDIAN, GT6_COMPLETE_MEDIAN, gt6_verdict,
                         hodge_decomposition)


def test_pure_gradient_flow_has_zero_residual():
    """由节点势生成的流 F_e = p_u - p_v 残余必须为 0（势博弈完备）。"""
    N = 6
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 5), (2, 5)]
    p = np.array([0.0, 1.0, 2.0, 0.5, -1.0, 3.0])
    F = np.array([p[u] - p[v] for (u, v) in edges])
    r, g2, r2, tot = hodge_decomposition(N, edges, F)
    assert r == pytest.approx(0.0, abs=1e-10)
    assert r2 == pytest.approx(0.0, abs=1e-12)


def test_cycle_flow_is_pure_residual():
    """三角形上的单位循环流不可由节点势解释，残余占比 = 1。"""
    edges = [(0, 1), (1, 2), (0, 2)]
    F = np.array([1.0, 1.0, -1.0])  # 绕环流：0→1→2 且 0→2 反向
    r, g2, r2, tot = hodge_decomposition(3, edges, F)
    assert r == pytest.approx(1.0, abs=1e-10)
    assert g2 == pytest.approx(0.0, abs=1e-12)


def test_decomposition_orthogonality():
    """一般流：梯度分量与残余正交，能量可加分解 ||F||² = ||grad||² + ||resid||²。"""
    rng = np.random.default_rng(7)
    N = 8
    edges = [(int(u), int(v)) for u in range(N) for v in range(N)
             if u < v and rng.random() < 0.5]
    F = rng.normal(size=len(edges))
    r, g2, r2, tot = hodge_decomposition(N, edges, F)
    assert g2 + r2 == pytest.approx(tot, rel=1e-9)
    assert r == pytest.approx(r2 / tot, rel=1e-9)
    assert 0.0 <= r <= 1.0


def test_zero_flow_defined_as_zero_residual():
    r, g2, r2, tot = hodge_decomposition(3, [(0, 1), (1, 2)],
                                         np.zeros(2))
    assert r == 0.0 and tot == 0.0


def _pg(vals):
    return {f"g{i}": {"residual_ratio_mean": v} for i, v in enumerate(vals)}


def test_verdict_complete_below_010():
    v = gt6_verdict(_pg([0.05] * 22))
    assert v["verdict"] == "potential_game_explanation_complete"
    assert v["median_residual_ratio"] == pytest.approx(0.05)


def test_verdict_downgraded_above_030():
    v = gt6_verdict(_pg([0.5] * 22))
    assert v["verdict"] == "downgraded_to_approximate_potential_game"


def test_verdict_inconclusive_band():
    v = gt6_verdict(_pg([0.2] * 22))
    assert v["verdict"] == "inconclusive_band_reported_as_is"


def test_verdict_threshold_constants_frozen():
    assert GT6_COMPLETE_MEDIAN == 0.10
    assert GT6_APPROX_MEDIAN == 0.30
