# -*- coding: utf-8 -*-
# gt_common（候选 5 GT 族共享底座）边界与钉定测试：
#   1. 共享函数边界（monotone_rate 容差/graph_tasks 确定性/phi 一致性）
#   2. 口径钉定：gt5b/gt7 持有自己的冻结常量副本，不再从 run_v20_gt5
#      import 常数（切断静默传导）；与 GT-5 的协议对齐在本文件**显式**
#      断言——任何一边改动都会让测试变红，而非静默漂移。
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import gt_common
import run_v20_gt5 as gt5
import run_v20_gt5b as gt5b
import run_v20_gt7 as gt7


# ---------------------------------------------------------------- 钉定
def test_decoupling_no_gt5_constant_imports():
    """gt5b/gt7 不再持有从 gt5 导入的常数名（静默传导已切断）。"""
    for name in ("GT5_TOL", "ENERGY_MODE", "GT5_GRAPHS", "GT5_SAMPLE_SEED"):
        assert not hasattr(gt5b, name), f"gt5b 仍暴露 {name}"
        assert not hasattr(gt7, name), f"gt7 仍暴露 {name}"


def test_alignment_with_gt5_is_explicit():
    """协议要求的跨脚本对齐（同口径/同图集/同抽样种子）显式锁定。"""
    assert gt5b.GT5B_TOL == gt5.GT5_TOL == 1e-9
    assert gt5b.GT5B_ENERGY_MODE == gt5.ENERGY_MODE == "aggregate"
    assert gt7.GT7_ENERGY_MODE == gt5.ENERGY_MODE
    assert gt7.GT7_GRAPHS == gt5.GT5_GRAPHS
    assert gt7.GT7_SAMPLE_SEED == gt5.GT5_SAMPLE_SEED == 505_000
    assert gt_common.GT_MONO_TOL == gt5.GT5_TOL
    assert gt_common.GT_ENERGY_MODE == gt5.ENERGY_MODE


# ---------------------------------------------------------------- 共享函数边界
def test_monotone_rate_boundaries():
    assert gt_common.monotone_rate([]) == 1.0
    assert gt_common.monotone_rate([1.0]) == 1.0
    assert gt_common.monotone_rate([0.0, 1.0, 2.0]) == 1.0
    assert gt_common.monotone_rate([0.0, 1.0, 0.5, 1.0]) == pytest.approx(2 / 3)
    tol = gt_common.GT_MONO_TOL
    assert gt_common.monotone_rate([0.0, -tol / 2]) == 1.0   # 容差内不减
    assert gt_common.monotone_rate([0.0, -10 * tol]) == 0.0  # 超容差
    assert gt_common.monotone_rate([0.0, -1e-3], tol=1e-2) == 1.0  # 显式 tol


def test_graph_tasks_deterministic_and_sorted():
    g = {"named_edges": [(0, 1), (1, 2), (2, 3), (3, 4), (0, 2)]}
    t1 = gt_common.graph_tasks(g, 3, 505_000)
    t2 = gt_common.graph_tasks(g, 3, 505_000)
    assert t1 == t2                                # 同种子同任务集
    assert t1 == sorted(t1)                        # 输出排序确定
    assert len(t1) == 3
    assert all(tuple(e) in g["named_edges"] for e in t1)
    assert gt_common.graph_tasks(g, 99, 1) == [tuple(e)
                                               for e in g["named_edges"]]


def test_phi_trajectory_consistency():
    W = np.array([[0.0, 0.5, 0.5], [0.0, 0.0, 1.0], [0.0, 0.0, 0.0]])
    traj = gt_common.phi_trajectory([W, W * 0.5], 0, 2)
    assert traj == [gt_common.phi_potential(W, 0, 2),
                    gt_common.phi_potential(W * 0.5, 0, 2)]
    assert all(np.isfinite(traj))


def test_gt5_wrappers_bind_own_constants():
    """gt5 薄转发的默认参数钉定 gt5 自己的冻结常量。"""
    import inspect
    assert inspect.signature(gt5.monotone_rate).parameters["tol"].default \
        == gt5.GT5_TOL
    assert inspect.signature(gt5.phi_potential
                             ).parameters["energy_mode"].default \
        == gt5.ENERGY_MODE
    assert gt5.reverse_denoise_traj is gt_common.reverse_denoise_traj
    traj = [0.0, 1.0, 0.5, 1.0]
    assert gt5.monotone_rate(traj) == gt_common.monotone_rate(
        traj, tol=gt5.GT5_TOL)
