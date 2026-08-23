# -*- coding: utf-8 -*-
# ============================================================
# Deposon v1.5 凝子扩散原型测试 (SPEC_v1.5 规定的 6 组 + SPEC v1.5.1 新增 2 组, 零外部调用)
#   1. 投影: 非负、行和=1 (1e-12)、零行→均匀
#   2. 条件等效 A: n_steps=0 ⇒ complete_graph 恒等 (仅投影)
#   3. 条件等效 B: 前向充分步 (β 末段→1) ⇒ mask 行收敛到均匀先验 (TV<1e-6)
#   4. 边界冻结: forward/reverse 任意步, 边界元素与 W0 之差 = 0
#   5. 无泄漏: scatter_energy 不读取 gold_edges (改 gold_edges 值, 输出不变)
#   6. smoke: 合成图上 complete_graph 对金边的 top-3 命中率 > 随机基线
#   7. v1.5.1: aggregate 能量在实验 B 真实脑图 ≥1 个留一实例上 field_active=True
#   8. v1.5.1 死锁回归: 可行 s→t 路径上的被掩边, aggregate 反向一步更新量 > 0
#      (max_path 模式同一更新量恒为 0 —— 首轮死锁, 按 SPEC 仅作对照注释不断言)
# ============================================================
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from deposon_diffusion import (DiffusionConfig, complete_graph, forward_diffuse,
                               project_simplex_rows, reverse_denoise, scatter_energy)


def _tv(p: np.ndarray, q: np.ndarray) -> float:
    return 0.5 * float(np.abs(p - q).sum())


# ---------------------------------------------------------------
# 1. 投影: 非负、行和=1 (1e-12)、零行→均匀 (T+R+A=1 analog)
# ---------------------------------------------------------------
def test_project_simplex_rows():
    rng = np.random.default_rng(0)
    W = rng.normal(size=(6, 6)) * 3.0  # 含负值
    P = project_simplex_rows(W)
    assert np.all(P >= 0.0), "投影后必须非负"
    assert np.allclose(P.sum(axis=1), 1.0, atol=1e-12), "行和必须为 1 (容差 1e-12)"

    Z = np.zeros((4, 4))
    PZ = project_simplex_rows(Z)
    assert np.allclose(PZ, 0.25, atol=1e-12), "零行必须映射到均匀行"

    W1 = project_simplex_rows(rng.random((5, 5)))
    assert np.allclose(project_simplex_rows(W1), W1, atol=1e-12), "已合法行必须幂等"


# ---------------------------------------------------------------
# 2. 条件等效 A: n_steps=0 ⇒ complete_graph 恒等 (仅投影)
# ---------------------------------------------------------------
def test_identity_at_zero_steps():
    rng = np.random.default_rng(1)
    N = 8
    W_true = project_simplex_rows(rng.random((N, N)))
    np.fill_diagonal(W_true, 0.0)
    W_true = project_simplex_rows(W_true)
    mask = np.zeros((N, N), dtype=bool)
    mask[0, 3] = True
    mask[2, 5] = True
    mask[4, :] = True  # 整行掩码
    np.fill_diagonal(mask, False)
    W_obs = W_true.copy()
    W_obs[mask] = 0.0  # 观测场: 掩码位置置零 (质量被释放), 不重归一
    cfg = DiffusionConfig(n_steps=0, seed=7)
    out = complete_graph(W_obs, mask, cfg, source=0, target=N - 1)
    assert np.allclose(out, W_obs, atol=0.0), "n_steps=0 必须恒等 (输入已合法 ⇒ 仅投影)"


# ---------------------------------------------------------------
# 3. 条件等效 B: 前向充分步 (β 末段→1) ⇒ mask 行收敛到均匀先验 (TV<1e-6)
# ---------------------------------------------------------------
def test_forward_converges_to_uniform_prior():
    rng = np.random.default_rng(2)
    N = 7
    W0 = project_simplex_rows(rng.random((N, N)))
    mask = np.zeros((N, N), dtype=bool)
    mask[1, :] = True   # 整行掩码: 先验 = 均匀 1/N
    mask[3, :] = True
    for sched in ("linear", "cosine"):
        cfg = DiffusionConfig(n_steps=50, beta_schedule=sched, seed=3)
        traj = forward_diffuse(W0, mask, cfg)
        WT = traj[-1]
        for row in (1, 3):
            assert _tv(WT[row], np.full(N, 1.0 / N)) < 1e-6, \
                f"{sched}: 充分前向后 mask 行必须收敛到均匀先验 (TV<1e-6)"


# ---------------------------------------------------------------
# 4. 边界冻结: forward/reverse 任意步, 边界元素与 W0 之差 = 0
# ---------------------------------------------------------------
def test_boundary_frozen():
    rng = np.random.default_rng(4)
    N = 9
    W0 = project_simplex_rows(rng.random((N, N)))
    mask = rng.random((N, N)) < 0.4
    np.fill_diagonal(mask, False)
    cfg = DiffusionConfig(n_steps=30, seed=5)
    traj = forward_diffuse(W0, mask, cfg)
    for t, Wt in enumerate(traj):
        diff = np.abs(Wt[~mask] - W0[~mask]).max() if (~mask).any() else 0.0
        assert diff == 0.0, f"forward 第 {t} 步边界被改动"
    W_rec = reverse_denoise(traj[-1], mask, cfg, source=0, target=N - 1)
    diff = np.abs(W_rec[~mask] - W0[~mask]).max()
    assert diff == 0.0, "reverse 输出边界被改动"
    # 消融臂同样冻结
    cfg_ng = DiffusionConfig(n_steps=30, field_guidance=False, seed=5)
    W_rec_ng = reverse_denoise(traj[-1], mask, cfg_ng, source=0, target=N - 1)
    assert np.abs(W_rec_ng[~mask] - W0[~mask]).max() == 0.0, "消融臂 reverse 边界被改动"


# ---------------------------------------------------------------
# 5. 无泄漏: scatter_energy 不读取 gold_edges (改 gold_edges 值, 输出不变)
# ---------------------------------------------------------------
def test_scatter_energy_no_leak():
    rng = np.random.default_rng(6)
    N = 8
    W = project_simplex_rows(rng.random((N, N)))
    e0 = scatter_energy(W, None, 0, N - 1)
    e1 = scatter_energy(W, {(0, 1), (2, 3)}, 0, N - 1)
    e2 = scatter_energy(W, {(i, j) for i in range(N) for j in range(N)}, 0, N - 1)
    assert e0 == e1 == e2, "scatter_energy 读取了 gold_edges (泄漏)"
    # 能量确实由场决定 ( sanity: 改变 W 会改变能量 )
    W2 = W.copy()
    W2[0, 1] *= 0.5
    assert scatter_energy(W2, None, 0, N - 1) != e0


# ---------------------------------------------------------------
# 6. smoke: 合成图上 complete_graph 对金边的 top-3 命中率 > 随机基线
#    图结构: 观测中继 1→3; 死支链 6→7→8; 孤立节点 2。
#    金边 = 0→1, 3→5 (分属两行, 同在 source=0→target=5 的唯一可达通路上,
#    因此都会被最短路梯度持续增强); 负候选 = 各行的死路/孤立目标。
#    场引导应把这两行的质量压到金边上; 无场臂无此信号。
# ---------------------------------------------------------------
def _smoke_setup():
    N = 9
    edges = [(0, 1), (1, 3), (3, 5), (6, 7), (7, 8)]
    outdeg = {}
    for u, _v in edges:
        outdeg[u] = outdeg.get(u, 0) + 1
    W_true = np.zeros((N, N))
    for u, v in edges:
        W_true[u, v] = 1.0 / outdeg[u]
    gold = [(0, 1), (3, 5)]
    negatives = [(0, 2), (0, 6), (0, 7), (0, 8),
                 (3, 0), (3, 2), (3, 6), (3, 7), (3, 8)]
    mask = np.zeros((N, N), dtype=bool)
    for e in gold + negatives:
        mask[e] = True
    W_obs = W_true.copy()
    for e in gold:
        W_obs[e] = 0.0
    return N, W_obs, mask, gold, negatives


def _top3_hits(scores: np.ndarray, gold, candidates) -> float:
    hits = 0
    for (u, v) in gold:
        row_cand = np.array([j for (uu, j) in candidates if uu == u])
        order = row_cand[np.argsort(-scores[u, row_cand], kind="mergesort")]
        if int(np.flatnonzero(order == v)[0]) < 3:
            hits += 1
    return hits / len(gold)


def test_smoke_completion_beats_random():
    N, W_obs, mask, gold, negatives = _smoke_setup()
    candidates = gold + negatives
    cfg = DiffusionConfig(n_steps=50, seed=11)
    W_done = complete_graph(W_obs, mask, cfg, source=0, target=5)
    guided = _top3_hits(W_done, gold, candidates)
    rng = np.random.default_rng(11)
    rand_scores = np.zeros((N, N))
    rand_scores[mask] = rng.random(int(mask.sum()))
    random_hit = _top3_hits(rand_scores, gold, candidates)
    assert guided > random_hit, \
        f"smoke: 场引导 top-3 命中率 {guided} 未超过随机基线 {random_hit}"
    # G2 消融臂必须存在且可运行
    cfg_ng = DiffusionConfig(n_steps=50, field_guidance=False, seed=11)
    W_ng = complete_graph(W_obs, mask, cfg_ng, source=0, target=5)
    assert W_ng.shape == (N, N) and np.all(np.isfinite(W_ng))


# ---------------------------------------------------------------
# 7. v1.5.1: aggregate 能量在实验 B 真实脑图 ≥1 个留一实例上 field_active=True
#    (引导臂输出与消融臂不同)。首轮 max-path 能量 49 个留一实例全部死锁
#    (field_active=0/49, 见 results/deposon_v15_diffusion_maxpath_negativeresult.json);
#    aggregate-T 使位于任一 source⇝target 通路的掩码边获得非零梯度, 死锁必须消除。
#    留一实例构造与 run_v15_experiment 实验 B 逐一对齐 (rng=70000+ei, 10 个负目标)。
# ---------------------------------------------------------------
def test_field_active_real_mindmap_aggregate():
    from run_v15_experiment import reconstruct_mindmap, row_normalize
    N, adj, edges, labels, _meta = reconstruct_mindmap()
    W_true = row_normalize(adj)
    source, target = 0, 1  # ROOT → GOAL_拓扑智能 (与实验 B 一致)
    n_active = 0
    for ei, (u, v) in enumerate(edges):
        rng = np.random.default_rng(70_000 + ei)
        adj_obs = adj.copy()
        adj_obs[u, v] = 0.0
        W_obs = W_true.copy()
        W_obs[u, v] = 0.0
        mask = np.zeros((N, N), dtype=bool)
        mask[u, v] = True
        pool = [j for j in range(N) if j != u and adj_obs[u, j] == 0]
        take = rng.choice(len(pool), size=min(10, len(pool)), replace=False)
        for k in take:
            mask[u, pool[k]] = True
        seed = 70_000 + ei
        cfg_on = DiffusionConfig(n_steps=10, seed=seed, energy_mode="aggregate")
        cfg_off = DiffusionConfig(n_steps=10, seed=seed, field_guidance=False)
        W_on = complete_graph(W_obs, mask, cfg_on, source, target)
        W_off = complete_graph(W_obs, mask, cfg_off, source, target)
        if np.abs(W_on[mask] - W_off[mask]).max() > 1e-9:
            n_active += 1
    assert n_active >= 1, \
        "aggregate 能量在实验 B 49 个留一实例上仍未激活 (field_active=0/49, 死锁未消除)"


# ---------------------------------------------------------------
# 8. v1.5.1 死锁回归: 被掩边位于可行 source→target 路径上时, aggregate 模式下
#    反向一步后该边权重更新量 > 0。
#    图: 观测边 0→1(0.1), 0→5(0.9), 5→3(1.0), 2→3(1.0); 被掩边 (1,2) 与同行
#    负目标 (1,4, 死端)。可行路径 0→1→2→3 经过 (1,2), 而最短路 0→5→3 全由
#    观测边组成 —— 正是首轮 max-path 死锁的几何 (子梯度恒零)。
#    对照 (按 SPEC v1.5.1 仅注释说明, 不断言): max_path 模式下同一更新量恒为 0
#    —— 已实测 delta_mp == 0.0 (最短路不含掩码边 ⇒ 子梯度恒零, 死锁如旧)。
# ---------------------------------------------------------------
def test_aggregate_mode_unlocks_masked_edge_gradient():
    N = 6
    source, target = 0, 3
    W_obs = np.zeros((N, N))
    W_obs[0, 1] = 0.1   # 观测: s→1 (低权支路)
    W_obs[0, 5] = 0.9   # 观测: s→5 (高权支路, 组成最短路)
    W_obs[5, 3] = 1.0   # 观测: 5→t  ⇒ 最短路 0→5→3 不含掩码边
    W_obs[2, 3] = 1.0   # 观测: 2→t  ⇒ 可行路径 0→1→2→3 经过被掩边 (1,2)
    mask = np.zeros((N, N), dtype=bool)
    mask[1, 2] = True   # 被掩边: 位于可行 source→target 路径上
    mask[1, 4] = True   # 同行掩码负目标 (死端, 提供行内竞争)
    base = dict(n_steps=1, lr=0.1, seed=3)
    W_agg = reverse_denoise(W_obs, mask,
                            DiffusionConfig(energy_mode="aggregate", **base),
                            source, target)
    W_off = reverse_denoise(W_obs, mask,
                            DiffusionConfig(field_guidance=False, **base),
                            source, target)
    delta = float(W_agg[1, 2] - W_off[1, 2])  # 同一先验样本, 唯一差异=场引导梯度
    assert delta > 0.0, \
        f"aggregate: 可行 s→t 路径上的被掩边反向一步更新量应 > 0, 实际 {delta}"
    # 死锁对照 (仅记录, 不断言): max_path 模式下同一更新量实测 == 0.0
    W_mp = reverse_denoise(W_obs, mask,
                           DiffusionConfig(energy_mode="max_path", **base),
                           source, target)
    _delta_mp = float(W_mp[1, 2] - W_off[1, 2])  # == 0.0: 首轮证伪的子梯度死锁
