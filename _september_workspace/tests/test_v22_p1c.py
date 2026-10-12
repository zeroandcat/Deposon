# -*- coding: utf-8 -*-
# T-P1c 判定纯函数与方向构造的测试锁定（先于/独立于主运行）。
import json
import os

import numpy as np

from run_v22_p1c import (TAU_GRID, COS_STRONG, COS_WEAK, verdict_p1c,
                         d_kl_direction, cos_align, sign_agreement)

HERE = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(HERE, "..", "results", "deposon_v22_p1c.json")


# ---- 判定纯函数：判死线机械求值 ----
def test_verdict_strong_survives():
    v = verdict_p1c([0.9999, 1.0], [0.9995] * 81)
    assert v["verdict"] == "survives_global_tau"
    assert v["tau_star_global"] is not None


def test_verdict_strong_dead_weak_alive():
    # 全局 τ 最高只能 0.9985 < 0.999，但逐状态 τ* 均 ≥0.99
    v = verdict_p1c([0.995, 1.0], [0.9985] * 81)
    assert v["verdict"] == "survives_state_dependent"
    assert v["tau_star_global"] is None


def test_verdict_weak_dead():
    # 逐状态 best ≥ 全局 min 恒成立（best 是 max_τ），故一致输入须满足此约束
    v = verdict_p1c([0.985, 1.0], [0.9985] * 81)   # 一状态连 τ* 都 <0.99
    assert v["verdict"] == "killed"
    assert v["strong_global_tau"] == "killed"


def test_verdict_threshold_boundaries():
    assert verdict_p1c([COS_WEAK], [COS_STRONG] * 81)["verdict"] == "survives_global_tau"
    assert verdict_p1c([COS_WEAK - 1e-12], [1.0] * 81)["verdict"] == "killed"
    assert verdict_p1c([1.0], [COS_STRONG - 1e-12] * 81)["verdict"] == "survives_state_dependent"


# ---- 方向构造 ----
def test_tau_grid_frozen():
    assert len(TAU_GRID) == 81 and TAU_GRID[0] == 0.0 and abs(TAU_GRID[-1] - 4.0) < 1e-12


def test_d_kl_tangent_zero_sum():
    rng = np.random.default_rng(0)
    w = rng.random(5); w /= w.sum()
    d = d_kl_direction(w, rng.random(5), 1.3)
    assert abs(float(d.sum())) < 1e-10      # 落在行单纯形切空间


def test_d_kl_tau0_is_plain_mirror():
    w = np.array([0.5, 0.3, 0.2])
    g = np.array([1.0, -0.5, 0.25])
    d = d_kl_direction(w, g, 0.0)
    expect = w * g - w * float((w * g).sum())
    np.testing.assert_allclose(d, expect, atol=1e-12)


def test_cos_align_zero_vector_trivial():
    c, triv = cos_align(np.zeros(3), np.array([1.0, 0, 0]))
    assert c == 1.0 and triv


def test_sign_agreement():
    assert sign_agreement(np.array([1.0, -1.0]), np.array([2.0, -0.5])) == 1.0
    assert sign_agreement(np.array([1.0, -1.0]), np.array([2.0, 0.5])) == 0.5


# ---- 主结果（若已运行）：口径与判定重算 ----
def test_result_json_recomputes_verdict():
    if not os.path.exists(JSON_PATH):
        return
    out = json.load(open(JSON_PATH, encoding="utf-8"))
    v = out["verdict"]
    assert v["verdict"] in ("killed", "survives_state_dependent", "survives_global_tau")
    assert out["seed"] == 210021 and out["n_states"] > 0
    # 机械一致性：min 值与档位自洽
    if v["min_cos_at_best_global_tau"] >= COS_STRONG:
        assert v["verdict"] == "survives_global_tau"
    elif v["min_cos_per_state_best_tau"] >= COS_WEAK:
        assert v["verdict"] == "survives_state_dependent"
    else:
        assert v["verdict"] == "killed"


def test_result_deterministic_rerun(tmp_path):
    """同种子重跑主脚本，结果 JSON（除 runtime_sec）逐字段一致。"""
    if not os.path.exists(JSON_PATH):
        return
    import subprocess, sys
    repo = os.path.join(HERE, "..")
    subprocess.run([sys.executable, "run_v22_p1c.py"], cwd=repo, check=True,
                   capture_output=True, timeout=600)
    a = json.load(open(JSON_PATH, encoding="utf-8"))
    a.pop("runtime_sec", None)
    subprocess.run([sys.executable, "run_v22_p1c.py"], cwd=repo, check=True,
                   capture_output=True, timeout=600)
    b = json.load(open(JSON_PATH, encoding="utf-8"))
    b.pop("runtime_sec", None)
    assert a == b
