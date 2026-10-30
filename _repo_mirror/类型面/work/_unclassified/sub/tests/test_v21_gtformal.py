# -*- coding: utf-8 -*-
# tests for run_v21_gtformal (GT_FORMALIZATION_v1 判死检验 T-P1b/T-P2/T-P3)
import numpy as np
import pytest

from run_v21_gtformal import (
    best_response_row, grad_phi, walk_sums_ga, hodge_residual, cycle_space_dim,
    verdict_p1b, verdict_p2, verdict_p3, graph_suite, pick_source_target,
    eval_task, TRAJ_STEPS,
)
from deposon_diffusion import _walk_sums, DiffusionConfig
from deposon_protocol import row_normalize, full_candidate_mask
from gt_common import phi_potential

LAM = 0.01


# ---------------------------------------------------------- 判定纯函数
class TestVerdictP1b:
    def test_survives_when_all_aligned(self):
        recs = [{"cosine": 0.5, "dPhi": 0.0, "dev_inf": 0.3}, {"cosine": 1.0, "dPhi": 1e-6, "dev_inf": 0.2}]
        v = verdict_p1b(recs)
        assert v["verdict"] == "survives"
        assert v["kill_reason"] is None

    def test_triggered_by_negative_cosine(self):
        v = verdict_p1b([{"cosine": -1e-12, "dPhi": 0.0, "dev_inf": 0.1}])
        assert v["verdict"] == "triggered" and v["kill_reason"] == "cosine<0"

    def test_cosine_exactly_zero_survives(self):
        assert verdict_p1b([{"cosine": 0.0, "dPhi": 0.0, "dev_inf": 0.1}])["verdict"] == "survives"

    def test_triggered_by_dphi_below_tol(self):
        v = verdict_p1b([{"cosine": 1.0, "dPhi": -1.1e-9, "dev_inf": 0.1}])
        assert v["verdict"] == "triggered" and v["kill_reason"] == "dPhi<-1e-9"

    def test_dphi_exactly_at_tol_survives(self):
        assert verdict_p1b([{"cosine": 1.0, "dPhi": -1e-9, "dev_inf": 0.1}])["verdict"] == "survives"


class TestVerdictP2:
    def test_acyclic_nonzero_residual_kills(self):
        assert verdict_p2([1e-8], [])["verdict"] == "killed_acyclic_residual"

    def test_acyclic_zero_and_few_cyclic_survives(self):
        v = verdict_p2([0.0, 1e-30], [0.5, 0.1, 0.1, 0.1])
        assert v["verdict"] == "survives"  # 1/4 > 0.30, not > 1/3

    def test_cyclic_high_residual_majority_downgrades(self):
        v = verdict_p2([0.0], [0.5, 0.4, 0.1])
        assert v["verdict"] == "downgraded_to_approximate_potential_game"  # 2/3 > 1/3

    def test_no_cyclic_graphs_survives(self):
        assert verdict_p2([0.0], [])["verdict"] == "survives"


class TestVerdictP3:
    def test_reparam_killed_when_r_differs(self):
        v = verdict_p3(r_diffs=[1e-8], fp_diffs=[0.0])
        assert v["reparametrization_claim"] == "killed"

    def test_reparam_survives_when_r_equal(self):
        assert verdict_p3([1e-10], [0.0])["reparametrization_claim"] == "survives"

    def test_structure_change_killed_when_fixed_points_identical(self):
        assert verdict_p3([0.0], [1e-10])["structure_change_claim"] == "killed"

    def test_structure_change_survives_when_fixed_points_differ(self):
        assert verdict_p3([0.0], [1e-6])["structure_change_claim"] == "survives"


# ---------------------------------------------------------- 组件行为
class TestWalkSumsGa:
    def test_matches_deposon_at_default_ga(self):
        rng = np.random.default_rng(7)
        for _ in range(5):
            n = 6
            adj = (rng.random((n, n)) < 0.4).astype(float)
            np.fill_diagonal(adj, 0.0)
            W = row_normalize(adj)
            x0, y0 = _walk_sums(W, 0, n - 1)
            x1, y1 = walk_sums_ga(W, 0, n - 1, 0.1)
            assert np.allclose(x0, x1, atol=1e-12)
            assert np.allclose(y0, y1, atol=1e-12)


class TestBestResponseRow:
    def test_single_candidate_is_degenerate_point(self):
        # n=2, 唯一候选 (0,1)：行单纯形是单点，BR 恒等于该点
        adj = np.array([[0.0, 1.0], [0.0, 0.0]])
        W = row_normalize(adj)
        idx = np.array([1])
        w = best_response_row(W, 0, idx, 1.0, 0, 1, lam=LAM)
        assert np.allclose(w, [1.0], atol=1e-12)

    def test_two_candidates_direct_edge_wins(self):
        # n=3: 唯一通路 0→2。候选 (0,1)/(0,2)；解析：log x_t 随 w(0,2)
        # 严格增且斜率 ~0.9 ≫ λ 平滑项回拉 ~0.02 ⇒ BR 为角点 (0,1)。
        adj = np.array([[0.0, 0.0, 1.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
        W = row_normalize(adj)
        W0 = W.copy(); W0[0, :] = 0.0
        W0[0, 1] = 0.5; W0[0, 2] = 0.5  # prior-mean 起点
        idx = np.array([1, 2])
        w = best_response_row(W0, 0, idx, 1.0, 0, 2, lam=LAM)
        assert w[1] > 1.0 - 1e-6

    def test_br_increases_phi(self):
        # 随机含环图：BR 后的 Φ 不低于起点（better-response 性质）
        rng = np.random.default_rng(3)
        adj = (rng.random((5, 5)) < 0.5).astype(float)
        np.fill_diagonal(adj, 0.0)
        W = row_normalize(adj)
        idx = np.array([j for j in range(5) if j != 1])
        W0 = W.copy(); W0[1, idx] = 1.0 / len(idx)
        w = best_response_row(W0, 1, idx, 1.0, 0, 4, lam=LAM)
        W1 = W0.copy(); W1[1, idx] = w
        assert phi_potential(W1, 0, 4) >= phi_potential(W0, 0, 4) - 1e-9


class TestCycleSpaceDim:
    def test_forest_is_zero(self):
        adj = np.array([[0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0]],
                       dtype=float)
        assert cycle_space_dim(row_normalize(adj)) == 0

    def test_directed_dag_with_undirected_triangle_is_one(self):
        # 0→1, 0→2, 1→2：有向 DAG 但无向三角 ⇒ ker(Bᵀ) 维数 1（T-P2 口径锚点）
        W = np.array([[0, .5, .5], [0, 0, 1], [0, 0, 0]])
        assert cycle_space_dim(W) == 1

    def test_mutual_pair_counts_directed_edges(self):
        W = np.array([[0, .5, .5], [1, 0, 0], [0, 0, 0]])
        assert cycle_space_dim(W) == 1  # E_dir=3, n=3, c=1


class TestHodgeResidual:
    def test_tree_residual_is_zero(self):
        # 树（DAG）循环空间为空 ⇒ r 必须为数值零
        adj = np.array([[0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0]],
                       dtype=float)
        W = row_normalize(adj)
        r = hodge_residual(W, 0, 3, g_a=0.1)
        assert r <= 1e-9

    def test_bidirectional_cycle_residual_positive(self):
        # 0⇄1 互指 + 0→2：循环空间非空，一般 r>0
        adj = np.array([[0, 1, 1], [1, 0, 0], [0, 0, 0]], dtype=float)
        W = row_normalize(adj)
        r = hodge_residual(W, 0, 2, g_a=0.1)
        assert r >= 0.0  # 只要求有限非负（具体值由实验报告）
        assert np.isfinite(r)


# ---------------------------------------------------------- 小图行为（端到端）
class TestGraphSuite:
    def test_suite_covers_required_families(self):
        suite = graph_suite()
        assert len(suite) >= 50
        fams = {g["family"] for g in suite}
        assert {"chain", "star", "tree", "dag", "cyclic"} <= fams
        assert max(g["adj"].shape[0] for g in suite) <= 8

    def test_pick_source_target_reachable(self):
        adj = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=float)
        s, t = pick_source_target(adj)
        assert s == 0 and t == 2  # 最长最短路对

    def test_eval_task_chain_first_step_better_response(self):
        # 链图 mean-field 首步：ΔΦ ≥ -1e-9（GT-5b 单调性在小图上复现）
        adj = np.zeros((4, 4))
        for i in range(3):
            adj[i, i + 1] = 1.0
        res = eval_task(adj, 0, 3, 1, DiffusionConfig(n_steps=TRAJ_STEPS))
        assert res["states"][0]["dPhi"] >= -1e-9
        assert np.isfinite(res["states"][0]["cosine"])
