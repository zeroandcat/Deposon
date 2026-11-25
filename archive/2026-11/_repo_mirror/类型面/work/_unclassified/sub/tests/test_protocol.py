# -*- coding: utf-8 -*-
"""deposon_protocol 边界测试 + 退火统一入口 (deposon_diffusion.denoise) 等价性测试。

覆盖 ARCH_AUDIT v2 指出的缺口：row_normalize 被 18 个脚本依赖却无直接边界测试。
等价性断言锁定候选 1 重构的行为保持性（5 份复制循环 → 单入口 denoise）。
"""
import numpy as np
import pytest

from deposon_diffusion import (DiffusionConfig, denoise, forward_diffuse,
                               reverse_denoise)
from deposon_protocol import (field_scores_init, full_candidate_mask,
                              gold_rank, prior_score_matrix, row_normalize)
# 薄转发位置也必须保持可用（18/14/11/11/8 个既有 import 路径）
from run_v15_experiment import row_normalize as row_normalize_v15
from run_v16_llm_prior import prior_score_matrix as psm_v16
from run_v19_fullrank import full_candidate_mask as fcm_fr, gold_rank as gr_fr
from run_v19_meanfield import field_scores_init as fsi_mf, reverse_denoise_init
from deposon_fast import reverse_denoise_fast
from run_v20_gt5 import reverse_denoise_traj
from run_v20_gt7 import reverse_denoise_traj_alpha


# ------------------------------------------------------------ row_normalize 边界
class TestRowNormalize:
    def test_basic_rows_sum_to_one(self):
        adj = np.array([[0.0, 2.0, 2.0], [1.0, 0.0, 3.0], [0.0, 0.0, 0.0]])
        W = row_normalize(adj)
        assert np.allclose(W[0], [0.0, 0.5, 0.5])
        assert np.allclose(W[1], [0.25, 0.0, 0.75])

    def test_zero_row_stays_zero(self):
        adj = np.zeros((4, 4))
        adj[1, 2] = 5.0
        W = row_normalize(adj)
        assert np.all(W[0] == 0.0) and np.all(W[2] == 0.0) and np.all(W[3] == 0.0)
        assert W[1, 2] == 1.0
        assert W.shape == (4, 4)

    def test_empty_matrix(self):
        W = row_normalize(np.zeros((0, 0)))
        assert W.shape == (0, 0)

    def test_negative_values_passthrough(self):
        # 协议不做符号校验：负值按代数和归一（如实记录现状语义）
        adj = np.array([[0.0, -1.0, 3.0]])  # 单行
        W = row_normalize(adj)
        assert np.allclose(W, [[0.0, -0.5, 1.5]])

    def test_nan_row_falls_back_to_zero_row(self):
        # 现状语义锁定：outdeg 为 nan 时 nan > 0 == False ⇒ 该行按零行处理
        adj = np.array([[np.nan, 1.0], [0.0, 0.0]])
        W = row_normalize(adj)
        assert np.all(W[0] == 0.0) and np.all(W[1] == 0.0)

    def test_non_square_input_elementwise_rows(self):
        adj = np.array([[1.0, 1.0, 0.0], [0.0, 2.0, 2.0]])  # 非方阵 (2,3)
        W = row_normalize(adj)
        assert W.shape == (2, 3)
        assert np.allclose(W[0], [0.5, 0.5, 0.0])
        assert np.allclose(W[1], [0.0, 0.5, 0.5])

    def test_forwarding_identity(self):
        assert row_normalize_v15 is row_normalize


# ------------------------------------------------------------ 其余协议函数边界
class TestProtocolFunctions:
    def test_prior_score_matrix_bounds_and_fill(self):
        P = prior_score_matrix({(0, 1): 0.9, (9, 9): 1.0, (-1, 0): 0.5}, (3, 3))
        assert P.shape == (3, 3)
        assert P[0, 1] == 0.9 and P.sum() == 0.9  # 越界键被忽略

    def test_full_candidate_mask_excludes_self(self):
        m = full_candidate_mask(5, 2)
        assert m.shape == (5, 5) and m.dtype == bool
        assert m[2].sum() == 4 and not m[2, 2]
        assert not m[:2].any() and not m[3:].any()

    def test_gold_rank_stable_order(self):
        scores = np.array([0.5, 0.5, 0.5, 0.1])
        cand = np.array([0, 1, 2, 3])
        assert gold_rank(scores, cand, 0) == 0  # mergesort 稳定 ⇒ 平局按候选序
        assert gold_rank(scores, cand, 3) == 3

    def test_forwarding_identity(self):
        assert psm_v16 is prior_score_matrix
        assert fcm_fr is full_candidate_mask
        assert gr_fr is gold_rank
        assert fsi_mf is field_scores_init


# ------------------------------------------------------------ 统一退火入口等价性
def _case(seed=7, n_steps=20):
    rng = np.random.default_rng(42)
    N = 8
    adj = (rng.random((N, N)) > 0.5).astype(float)
    np.fill_diagonal(adj, 0.0)
    adj[0, 1] = 1.0
    W_true = row_normalize(adj)
    mask = full_candidate_mask(N, 0)
    W_obs = W_true.copy()
    W_obs[0, 1] = 0.0
    cfg = DiffusionConfig(seed=seed, n_steps=n_steps)
    WT = forward_diffuse(W_obs, mask, cfg)[-1]
    return WT, mask, cfg


class TestDenoiseUnification:
    @pytest.mark.parametrize("mode", ["dirichlet", "prior_mean"])
    def test_wrapper_bitwise_equal(self, mode):
        WT, mask, cfg = _case()
        Wd, steps, states = denoise(WT, mask, cfg, 0, 1, init_mode=mode)
        assert np.array_equal(Wd, reverse_denoise_init(WT, mask, cfg, 0, 1,
                                                       init_mode=mode))
        assert steps == cfg.n_steps and states is None

    def test_default_equals_reverse_denoise(self):
        WT, mask, cfg = _case()
        Wd, _, _ = denoise(WT, mask, cfg, 0, 1)
        assert np.array_equal(Wd, reverse_denoise(WT, mask, cfg, 0, 1))

    def test_alpha_one_equals_dirichlet(self):
        WT, mask, cfg = _case()
        a = reverse_denoise_traj_alpha(WT, mask, cfg, 0, 1, 1.0)
        b = reverse_denoise_traj(WT, mask, cfg, 0, 1, init_mode="dirichlet")
        assert len(a) == len(b) == cfg.n_steps + 1
        for sa, sb in zip(a, b):
            assert np.array_equal(sa, sb)

    def test_record_final_equals_final(self):
        WT, mask, cfg = _case()
        Wf, _, _ = denoise(WT, mask, cfg, 0, 1)
        states = reverse_denoise_traj(WT, mask, cfg, 0, 1,
                                      init_mode="dirichlet")
        assert np.array_equal(states[-1], Wf)

    def test_early_stop_disabled_equals_full_run(self):
        WT, mask, cfg = _case()
        # rel_tol=0 ⇒ 永不触发早停 ⇒ 与完整步数逐位一致
        W_slow = reverse_denoise_init(WT, mask, cfg, 0, 1, init_mode="dirichlet")
        W_fast, steps = reverse_denoise_fast(WT, mask, cfg, 0, 1,
                                             init_mode="dirichlet", rel_tol=0.0)
        assert steps == cfg.n_steps
        assert np.array_equal(W_slow, W_fast)

    def test_n_steps_zero_identity(self):
        WT, mask, cfg = _case(n_steps=0)
        Wd, steps, states = denoise(WT, mask, cfg, 0, 1, record=True)
        assert steps == 0 and len(states) == 1
        assert np.array_equal(Wd, WT)
        assert np.array_equal(reverse_denoise_traj(WT, mask, cfg, 0, 1,
                                                   init_mode="dirichlet")[0], WT)

    def test_invalid_knobs_raise(self):
        WT, mask, cfg = _case()
        with pytest.raises(ValueError):
            denoise(WT, mask, cfg, 0, 1, init_mode="bogus")
        with pytest.raises(ValueError):
            denoise(WT, mask, cfg, 0, 1, alpha=0.0)
        with pytest.raises(ValueError):
            reverse_denoise_traj_alpha(WT, mask, cfg, 0, 1, alpha=-1.0)
