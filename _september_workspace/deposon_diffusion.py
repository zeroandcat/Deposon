# -*- coding: utf-8 -*-
# ============================================================
# Deposon v1.5 凝子扩散原型: 固定节点集上的边权场补全 (masked edge completion)
# 落实 docs/Roadmap_v1.5.md 的最小可验证原型, 接口契约见 SPEC_v1.5。
#
# 物理约定 (与 v1.4 论文符号一致, 不得矛盾):
#   - 行单纯形投影: 每个有出边的节点 i, 出边权重行 W[i,:] 归一到概率单纯形
#     (Σ_j W[i,j]=1, W>=0)。这是 v1.4 T+R+A=1 幺正性硬投影在生成场上的对应物,
#     代码与文档字符串中统一表述为 "T+R+A=1 analog"。
#   - 透射率内核 (复用 v1.4 定义): 对边 e, t_e = 1/(1+g_eff+g_aether),
#     g_eff = g_couple/(1+δ²); 路径透射率为边 t 连乘。
#   - W → 散射参数固定单调映射: g_couple = 1/max(W,eps) - 1, g_aether = 0.1 (常数),
#     δ = 0; 即 W 越大透射越高。单调即可, 禁止引入与 v1.4 冲突的新物理参数。
#   - 边界值条件化: 观测边集合 O (Dirichlet 边界) 在任何前向/反向步骤中逐元素冻结;
#     掩码边集合 M 才是生成自由度。
#
# G2 教训 (硬约束): field_guidance=False 为无场引导消融臂, 能量退化为纯平滑项,
#   用于证明 (或证伪) 场引导项的必要性。
#
# 全部种子确定论 (numpy Generator), 无网络与外部服务调用, numpy 之外零依赖。
# ============================================================
from dataclasses import asdict, dataclass

import numpy as np

_EPS = 1e-12          # 单调映射与投影的数值容差 (SPEC: 容差 1e-12)
_G_AETHER = 0.1       # g_aether 常数 (SPEC 固定映射)
_DELTA = 0.0          # δ (SPEC 固定映射)
_TOL = 1e-12          # 行单纯形投影零行判据 (SPEC: 容差 1e-12)
# scatter_energy 签名不含 cfg (SPEC 接口契约), 其平滑项系数取 DiffusionConfig 默认值;
# reverse_denoise 内部的能量梯度使用 cfg.lam_smooth, 二者默认一致。
_LAM_SMOOTH_DEFAULT = 0.01


@dataclass
class DiffusionConfig:
    """扩散配置 (SPEC 接口契约, 字段不得改)。"""
    n_steps: int = 50              # 扩散步数
    beta_schedule: str = "linear"  # "linear" | "cosine"
    prior: str = "uniform_out"     # 行均匀先验
    lr: float = 0.1                # 反向退火步长
    lam_smooth: float = 0.01       # 平滑正则
    field_guidance: bool = True    # False = G2 消融 (无场引导)
    energy_mode: str = "aggregate"  # "aggregate" (v1.5.1 聚合透射率) | "max_path" (首轮对照)
    seed: int = 0


def _check_square(W: np.ndarray, mask: np.ndarray | None = None) -> None:
    if W.ndim != 2 or W.shape[0] != W.shape[1]:
        raise ValueError("W must be a square 2D array")
    if mask is not None and mask.shape != W.shape:
        raise ValueError("mask must have the same shape as W")


def project_simplex_rows(W: np.ndarray) -> np.ndarray:
    """把每行裁剪到非负并归一化到概率单纯形; 零行映射到均匀行 (1/N)。

    这是 v1.4 T+R+A=1 硬投影在生成场上的对应物 (T+R+A=1 analog):
    每个节点的出边权重行满足 Σ_j W[i,j]=1, W>=0。容差 1e-12。
    """
    W = np.asarray(W, dtype=float)
    _check_square(W)
    n = W.shape[0]
    out = np.maximum(W, 0.0)
    for i in range(n):
        s = float(out[i].sum())
        if s <= _TOL:
            out[i] = 1.0 / n          # 零行 → 均匀行
        else:
            out[i] /= s
    return out


def _beta_schedule(cfg: DiffusionConfig) -> np.ndarray:
    """噪声率序列 b_1..b_T, 单调且 b_T = 1 (前向充分步 ⇒ 收敛到先验)。"""
    t = np.arange(1, cfg.n_steps + 1, dtype=float)
    if cfg.n_steps <= 0:
        return np.empty(0)
    if cfg.beta_schedule == "linear":
        b = t / cfg.n_steps
    elif cfg.beta_schedule == "cosine":
        b = 1.0 - np.cos(0.5 * np.pi * t / cfg.n_steps)
    else:
        raise ValueError(f"unknown beta_schedule: {cfg.beta_schedule}")
    b[-1] = 1.0  # 末段精确到 1, 保证充分前向 ⇒ 行均匀先验 (TV 可 < 1e-6)
    return b


def _masked_row_stats(W: np.ndarray, mask: np.ndarray, i: int):
    """第 i 行: 边界质量 S_b (冻结), 掩码位置, 每位置均匀先验值。

    先验质量 = 1 - S_b: 边界被 Dirichlet 冻结后, 掩码自由度在该行可分配的总质量。
    行均匀先验 ("uniform_out"): 可用质量在掩码位置上均分。
    """
    idx = mask[i]
    m = int(idx.sum())
    s_b = float(W[i, ~idx].sum())
    mass = max(1.0 - s_b, 0.0)
    return idx, m, mass / m if m > 0 else 0.0


def _project_masked(W: np.ndarray, mask: np.ndarray) -> np.ndarray:
    """掩码自由度的单纯形投影 (T+R+A=1 analog 在掩码子向量上的形式):
    逐行把掩码位置裁剪到非负并归一到质量 (1 - 边界质量); 全零掩码子向量
    映射到行均匀先验。边界元素 (mask=False) 一律不触碰, 即逐元素冻结。
    """
    n = W.shape[0]
    for i in range(n):
        idx, m, p = _masked_row_stats(W, mask, i)
        if m == 0:
            continue
        w = np.maximum(W[i, idx], 0.0)
        mass = p * m
        s = float(w.sum())
        if s <= _TOL:
            W[i, idx] = p            # 全零 → 行均匀先验
        else:
            W[i, idx] = w * (mass / s)
    return W


def forward_diffuse(W0: np.ndarray, mask: np.ndarray, cfg: DiffusionConfig) -> list:
    """前向热化加噪: W_t[i,:] = (1-b_t)*W_{t-1}[i,:] + b_t*prior_row (掩码行),
    每步后做掩码单纯形投影; 边界元素每步保持 W0 原值 (逐元素冻结)。

    mask[i,j]=True 表示该边是被掩码的生成自由度; False=边界, 冻结。
    返回轨迹 [W_0, W_1, ..., W_T]; n_steps=0 时返回 [W0] (恒等)。
    """
    W0 = np.asarray(W0, dtype=float)
    mask = np.asarray(mask, dtype=bool)
    _check_square(W0, mask)
    if cfg.prior != "uniform_out":
        raise ValueError(f"unknown prior: {cfg.prior}")
    betas = _beta_schedule(cfg)
    W = W0.copy()
    states = [W.copy()]
    for b in betas:
        for i in range(W.shape[0]):
            idx, m, p = _masked_row_stats(W, mask, i)
            if m == 0:
                continue
            W[i, idx] = (1.0 - b) * W[i, idx] + b * p
        # 边界元素冻结: _project_masked 只写掩码位置, 边界保持 W0 原值
        _project_masked(W, mask)
        states.append(W.copy())
    return states


def _edge_transmittance(W: np.ndarray) -> np.ndarray:
    """边透射率 t_e, 由 W 经固定映射得到:
    g_couple = 1/max(W,eps) - 1, g_eff = g_couple/(1+δ²) (δ=0),
    t_e = 1/(1+g_eff+g_aether) = 1/(1/max(W,eps) + g_aether), g_aether=0.1。
    W<=0 的位置视为无边 (t=0); 自环 t=0。
    """
    t = 1.0 / (1.0 / np.maximum(W, _EPS) + _G_AETHER)
    t[W <= 0.0] = 0.0
    np.fill_diagonal(t, 0.0)
    return t


def _edge_cost(W: np.ndarray) -> np.ndarray:
    """Dijkstra 费用 -log t_e (t_e 的固定映射见 _edge_transmittance)。
    W<=0 的位置视为无边 (费用 inf); 自环费用 inf。
    """
    t = _edge_transmittance(W)
    cost = np.full_like(t, np.inf)
    pos = t > 0.0
    cost[pos] = -np.log(t[pos])
    return cost


def _topological_order(support: np.ndarray):
    """Kahn 拓扑排序: support[i,j]=True 表示边 i→j。含环时返回 None。"""
    n = support.shape[0]
    indeg = support.sum(axis=0).astype(int)
    order = []
    ready = [i for i in range(n) if indeg[i] == 0]
    while ready:
        u = ready.pop()
        order.append(u)
        for v in np.flatnonzero(support[u]):
            indeg[v] -= 1
            if indeg[v] == 0:
                ready.append(int(v))
    return order if len(order) == n else None


def _walk_sums(W: np.ndarray, source: int, target: int):
    """聚合透射率游走和 (aggregate-T analog of v1.4 §scattering audit)。

    x[v] = Σ_{walks source⇝v} Π_{e∈walk} t_e,  y[v] = Σ_{walks v⇝target} Π t_e。
    支持图 (t>0) 为 DAG 时用拓扑序 DP (SPEC v1.5.1 公式):
        T(v) = Σ_{u→v} T(u)·t(u,v),  T(source)=1   (y 为反向同理)。
    支持图含环时 (掩码候选边可指向任意节点而成环) 用闭式解
    x = (I-Gᵀ)⁻¹e_s, y = (I-G)⁻¹e_t (G[u,v]=t(u,v)): 非零行满足
    Σ_j t(i,j) < Σ_j W[i,j] ≤ 1 ⇒ 谱半径 ρ(G)<1 ⇒ Neumann 级数收敛,
    且 DAG 特例下与拓扑序 DP 逐元素一致。
    """
    t = _edge_transmittance(W)
    n = W.shape[0]
    e_s = np.zeros(n)
    e_s[source] = 1.0
    e_t = np.zeros(n)
    e_t[target] = 1.0
    order = _topological_order(t > 0.0)
    if order is not None:
        x = e_s.copy()
        for v in order:  # 拓扑序保证所有 u→v 的 x[u] 已就位
            x[v] += float(t[:, v] @ x)
        y = e_t.copy()
        for u in reversed(order):  # 逆拓扑序保证所有 u→v 的 y[v] 已就位
            y[u] += float(t[u, :] @ y)
    else:
        x = np.linalg.solve(np.eye(n) - t.T, e_s)
        y = np.linalg.solve(np.eye(n) - t, e_t)
    return x, y


def _shortest_path(W: np.ndarray, source: int, target: int):
    """最大路径透射率 = exp(-最短路费用), 最短路用 Dijkstra on -log t_e (O(N^2) 稠密)。
    返回 (min_cost, path_edges); 不可达时 (inf, [])。"""
    cost = _edge_cost(W)
    n = W.shape[0]
    dist = np.full(n, np.inf)
    prev = np.full(n, -1, dtype=int)
    done = np.zeros(n, dtype=bool)
    dist[source] = 0.0
    for _ in range(n):
        d = np.where(done, np.inf, dist)
        u = int(np.argmin(d))
        if not np.isfinite(dist[u]):
            break
        done[u] = True
        if u == target:
            break
        nd = dist[u] + cost[u]
        better = nd < dist
        dist[better] = nd[better]
        prev[better] = u
    if not np.isfinite(dist[target]):
        return np.inf, []
    path = []
    v = target
    while v != source:
        u = int(prev[v])
        if u < 0:
            return np.inf, []
        path.append((u, v))
        v = u
    path.reverse()
    return float(dist[target]), path


def scatter_energy(W: np.ndarray, gold_edges, source: int, target: int,
                   energy_mode: str = "aggregate") -> float:
    """场引导能量 (SPEC v1.5.1: 可选 energy_mode, 向后兼容):

    - energy_mode="aggregate" (默认): E = -log(Σ_{p: source⇝target} Π_{e∈p} t_e)
      + lam_smooth*平滑项 —— aggregate-T analog of v1.4 §scattering audit。
      聚合透射率在 DAG 上用拓扑序 DP (T(v)=Σ_{u→v}T(u)·t(u,v), T(source)=1),
      含环支持图用闭式游走和 (见 _walk_sums); 每条位于任一 s⇝t 通路的边
      对能量都有非零解析梯度 (消除 max_path 的子梯度死锁)。
    - energy_mode="max_path" (首轮对照): E = -log(最大路径透射率) + 平滑项,
      最大路径透射率用 Dijkstra on -log t_e; 当最短路全由观测边组成时,
      掩码边子梯度恒为 0 (首轮证伪的死锁)。

    t_e 由 W[i,j] 经固定映射得到 (g_couple = 1/max(W,eps) - 1, g_aether = 0.1, δ = 0)。
    平滑项 = Σ_{i≠j} W[i,j]^2 (行场上鼓励权重弥散的 L2 正则);
    其系数取 DiffusionConfig.lam_smooth 的默认值 (签名契约不含 cfg)。

    防泄漏: gold_edges 仅用于评估上下文, 不得进入能量 —— 本函数体不读取该参数。
    """
    del gold_edges  # 防泄漏: 能量不读取金边 (SPEC 接口保留该参数仅用于评估对齐)
    W = np.asarray(W, dtype=float)
    _check_square(W)
    if energy_mode == "aggregate":
        x, _y = _walk_sums(W, source, target)
        field = -float(np.log(max(float(x[target]), _EPS)))
    elif energy_mode == "max_path":
        min_cost, _ = _shortest_path(W, source, target)
        field = float(min_cost)
    else:
        raise ValueError(f"unknown energy_mode: {energy_mode}")
    off_diag = W ** 2
    np.fill_diagonal(off_diag, 0.0)
    smooth = float(off_diag.sum())
    return float(field + _LAM_SMOOTH_DEFAULT * smooth)


def reverse_denoise(WT: np.ndarray, mask: np.ndarray, cfg: DiffusionConfig,
                    source: int, target: int) -> np.ndarray:
    """反向退火去噪: 从前向末端状态出发, 每步对掩码自由度做
    (i) 能量的解析 (子) 梯度下降, 采用单纯形自然梯度 (乘以 W, 即 mirror descent),
        避免大步长单边锁死; 平滑项梯度 2*lam_smooth*W。场引导项按 cfg.energy_mode:
        - "aggregate" (v1.5.1 默认): dE/dW[u,v] = -(x[u]·y[v]/x_t)·dt_e/dW,
          其中 x/y 为 source⇝v / v⇝target 的聚合透射率游走和 (见 _walk_sums),
          x_t=x[target]; 位于任一 s⇝t 通路的边都有非零解析梯度, 消除死锁;
        - "max_path" (首轮对照): 最短路 (Dijkstra on -log t_e) 上掩码边的
          d(-log t_e)/dW; 最短路不含掩码边时子梯度恒为 0 (死锁)。
    (ii) 向 W_obs 收缩: W ← (1-lr)*W + lr*W_obs (W_obs 由 WT 的边界/掩码值承载);
    步后做掩码单纯形投影 + 边界重置 (逐元素冻结为 WT 的边界值 = W0 原值)。

    field_guidance=False 时能量退化为纯平滑项 (G2 消融臂)。
    n_steps=0 时恒等返回 (仅投影语义: 输入已是合法场时逐元素不变)。
    反向起点是行均匀先验的样本而非均值: 每个掩码行从 Dirichlet(1,...,1) 采样
    (均值为均匀分布, 即 "uniform_out" 先验的正则采样, x_T ~ prior), 种子由
    cfg.seed 固定 (决定论)。先验采样是扩散生成的标准做法, 也是场引导项得以
    检验的前提。
    """
    W, _steps, _states = denoise(WT, mask, cfg, source, target)
    return W


def denoise(WT: np.ndarray, mask: np.ndarray, cfg: DiffusionConfig,
            source: int, target: int, *, init_mode: str = "dirichlet",
            alpha: float | None = None,
            early_stop: tuple | None = None,
            record: bool = False):
    """统一反向退火入口 (候选 1 重构): 原 5 份逐行复制循环的单一实现。

    旋钮 (全部为行为保持参数化, 各历史副本的语义逐项对应):
    - init_mode: "dirichlet" (Dirichlet 随机起点, 同原 reverse_denoise) |
      "prior_mean" (跳过采样, 保持前向终态 = mean-field / DDIM η=0 极限,
      对应原 run_v19_meanfield.reverse_denoise_init 的同名模式)。
    - alpha: Dirichlet 浓度 (None ⇒ np.ones(m), 与原 dirichlet 逐位一致;
      对应原 run_v20_gt7.reverse_denoise_traj_alpha 的 α 温度旋钮)。
    - early_stop: None 或 (rel_tol, min_steps); 步数 ≥ min_steps 且本步掩码上
      最大相对更新 < rel_tol 时提前退出 (对应原 deposon_fast.reverse_denoise_fast)。
    - record: True 时记录每步后的 W (共 n_steps+1 个状态, 含起点;
      对应原 run_v20_gt5.reverse_denoise_traj)。

    返回 (W_final, steps_taken, states):
    - W_final: 退火末态 (与旧各副本返回值逐位一致);
    - steps_taken: 实际步数 (early_stop=None 时 = max(n_steps, 0));
    - states: record=True 时为状态列表, 否则 None。

    n_steps<=0 时恒等返回 (W=WT.copy(), steps=0, record 时 states=[W]),
    与全部旧副本的提前返回语义一致。
    """
    WT = np.asarray(WT, dtype=float)
    mask = np.asarray(mask, dtype=bool)
    _check_square(WT, mask)
    if cfg.energy_mode not in ("aggregate", "max_path"):
        raise ValueError(f"unknown energy_mode: {cfg.energy_mode}")
    if init_mode not in ("dirichlet", "prior_mean"):
        raise ValueError(f"unknown init_mode: {init_mode}")
    if alpha is not None and alpha <= 0.0:
        raise ValueError(f"alpha must be positive or None, got {alpha}")
    W = WT.copy()
    if cfg.n_steps <= 0:
        return W, 0, ([W] if record else None)  # 条件等效 A: n_steps=0 ⇒ 恒等
    if init_mode == "dirichlet":
        rng = np.random.default_rng(cfg.seed)
        for i in range(W.shape[0]):
            idx, m, p = _masked_row_stats(W, mask, i)
            if m == 0:
                continue
            mass = p * m
            if mass > 0.0:
                conc = np.ones(m) if alpha is None else np.full(m, alpha)
                W[i, idx] = mass * rng.dirichlet(conc)  # x_T ~ 行均匀先验
        _project_masked(W, mask)
    else:  # prior_mean: 前向终态已是行均匀先验均值, 零随机性 (不调 rng)
        _project_masked(W, mask)
    states = [W.copy()] if record else None
    steps_taken = 0
    for _t in range(cfg.n_steps, 0, -1):
        grad = np.zeros_like(W)
        if cfg.field_guidance and source != target:
            if cfg.energy_mode == "aggregate":
                # 聚合透射率解析梯度: dE/dW[u,v] = -(x[u]·y[v]/x_t)·dt_e/dW,
                # dt_e/dW = 1/(1+g_aether*W)^2 (W>0 处; W<=0 处映射为常数 ⇒ 0)。
                # x[u]·y[v]/x_t 恰为穿过 (u,v) 的 s⇝t 游走质量占比 ⇒ 任一
                # s⇝t 通路上的边都有严格负梯度 (能量随权重增大而下降), 无死锁。
                x, y = _walk_sums(W, source, target)
                xt = max(float(x[target]), _EPS)
                wpos = np.maximum(W, _EPS)
                dtdw = np.where(W > _EPS, 1.0 / (1.0 + _G_AETHER * wpos) ** 2, 0.0)
                grad -= (x[:, None] * y[None, :]) * (dtdw / xt)
            else:  # "max_path" 首轮对照臂
                _, path = _shortest_path(W, source, target)
                for (i, j) in path:
                    if mask[i, j]:
                        w = max(float(W[i, j]), _EPS)
                        # d(-log t_e)/dW = g_aether/(1+g_aether*W) - 1/W  (固定映射求导)
                        grad[i, j] += _G_AETHER / (1.0 + _G_AETHER * w) - 1.0 / w
        if cfg.lam_smooth:
            grad[mask] += 2.0 * cfg.lam_smooth * W[mask]
        if early_stop is not None:
            W_prev = W[mask].copy()
        # 单纯形自然梯度 (mirror descent): 等效乘性更新 W *= exp(-lr * W * grad)
        W[mask] *= np.exp(-cfg.lr * W[mask] * grad[mask])
        # 向 W_obs 收缩: W_obs 在掩码处为 0 (观测场不含被掩边), 即乘以 (1-lr) 衰减
        W[mask] = (1.0 - cfg.lr) * W[mask]
        W[~mask] = WT[~mask]  # 边界逐元素冻结
        _project_masked(W, mask)
        steps_taken += 1
        if record:
            states.append(W.copy())
        if early_stop is not None:
            rel_tol, min_steps = early_stop
            if steps_taken >= min_steps:
                denom = np.maximum(np.abs(W_prev), _EPS)
                rel = (np.max(np.abs(W[mask] - W_prev) / denom)
                       if W_prev.size else 0.0)
                if rel < rel_tol:
                    break
    return W, steps_taken, states


def complete_graph(W_obs: np.ndarray, mask: np.ndarray, cfg: DiffusionConfig,
                   source: int, target: int) -> np.ndarray:
    """端到端: forward_diffuse(观测场) → reverse_denoise → 返回补全场。

    边界 (mask=False) 全程逐元素冻结为 W_obs 原值; n_steps=0 时恒等 (仅投影)。
    """
    traj = forward_diffuse(W_obs, mask, cfg)
    return reverse_denoise(traj[-1], mask, cfg, source, target)


def config_dict(cfg: DiffusionConfig) -> dict:
    """配置序列化 (供实验 JSON 记录)。"""
    return asdict(cfg)
