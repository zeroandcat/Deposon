# -*- coding: utf-8 -*-
# ============================================================
# Deposon v2.0 GT 实验族共享底座（docs/ARCH_AUDIT_v2.md 候选 5 落地）
#
# 历史：run_v20_gt5b / run_v20_gt7 直接 import run_v20_gt5 的常数表与函数
# （ENERGY_MODE/GT5_TOL/GT5_GRAPHS/GT5_SAMPLE_SEED/monotone_rate/
# phi_potential/phi_trajectory/reverse_denoise_traj/_graph_tasks），
# 改 gt5 的常数会静默改变 gt5b/gt7 的口径。
#
# 本模块集中**共享函数**（实现逐字搬运自 run_v20_gt5，数值逐位不变）；
# 各 GT 脚本的**对外口径常数在各自文件内显式钉定**（GT5_TOL/GT5B_TOL、
# GT5_GRAPHS/GT7_GRAPHS、各 ENERGY_MODE 副本），跨脚本对齐由
# tests/test_gt_common.py 的相等性断言**显式锁定**（分歧即测试变红，
# 不再静默传导）。
#
# 默认参数 GT_ENERGY_MODE / GT_MONO_TOL 仅为调用便利的共享锚点；
# 各脚本调用共享函数时显式传入自己钉定的常数副本。
# ============================================================
import numpy as np

from deposon_diffusion import denoise, scatter_energy

# 共享锚点（Φ 定义口径：Φ = -scatter_energy(aggregate)；单调性数值容差）。
# 修改这两个值会同时影响全部 GT 脚本——这正是本模块存在的意义：
# 共享口径只有一个家，且每个脚本另持有自己的冻结副本显式传参。
GT_ENERGY_MODE = "aggregate"
GT_MONO_TOL = 1e-9


def phi_potential(W, source, target, energy_mode=GT_ENERGY_MODE):
    """势函数 Φ(W) = -scatter_energy(W)（聚合透射率对数 − 平滑正则）。

    理由：反向退火动态正是 scatter_energy 的（自然）梯度下降，故其 Lyapunov
    函数为 -E。gold_edges 参数按 SPEC 防泄漏契约传 None（函数体不读取）。
    （实现逐字搬运自 run_v20_gt5.phi_potential。）
    """
    val = -scatter_energy(np.asarray(W, dtype=float), None, source, target,
                          energy_mode=energy_mode)
    return float(val)


def reverse_denoise_traj(WT, mask, cfg, source, target, init_mode):
    """轨迹记录反向退火（deposon_diffusion.denoise 薄转发，record=True）。

    init_mode="dirichlet" 与原 reverse_denoise 相同的 Dirichlet(1) 随机起点；
    init_mode="prior_mean" 为确定性 mean-field 极限。返回 states 列表
    （共 n_steps+1 个状态，含起点）。（实现逐字搬运自 run_v20_gt5。）
    """
    _W, _steps, states = denoise(WT, mask, cfg, source, target,
                                 init_mode=init_mode, record=True)
    return states


def phi_trajectory(states, source, target, energy_mode=GT_ENERGY_MODE):
    """逐状态求 Φ，返回长度 len(states) 的列表。"""
    return [phi_potential(W, source, target, energy_mode) for W in states]


def monotone_rate(traj, tol=GT_MONO_TOL):
    """单调不减率：ΔΦ_t ≥ -tol 的步数占比；空/单点轨迹定义为 1.0。"""
    traj = [float(v) for v in traj]
    if len(traj) < 2:
        return 1.0
    diffs = np.diff(traj)
    return float(np.mean(diffs >= -tol))


def graph_tasks(g, n_tasks, sample_seed):
    """每图抽 n_tasks 条 named 留一任务（种子化，可复现）。

    （实现逐字搬运自 run_v20_gt5._graph_tasks；gt5/gt7 各自显式传入
    自己钉定的 sample_seed 副本。）
    """
    named = [tuple(e) for e in g["named_edges"]]
    rng = np.random.default_rng(sample_seed)
    take = rng.choice(len(named), size=min(n_tasks, len(named)), replace=False)
    return [named[int(k)] for k in sorted(take.tolist())]
