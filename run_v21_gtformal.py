# -*- coding: utf-8 -*-
# Deposon v2.1 GT-FORMAL：docs/GT_FORMALIZATION_v1.md §7 判死检验落地
#   → results/deposon_v21_gtformal.json。判读规则为预登记纯函数机械求值
#   （tests/test_v21_gtformal.py 锁定）：
#   T-P1b（§6 最脆弱环节）：n≤8 系统采样图族（≥50 图），同图同初始化逐步比较
#     d_mf 与构造 B（行玩家）BR 方向；判死线 = 任一状态余弦<0 或 ΔΦ<−1e-9；
#     并量化 P1a 偏差 max‖T−BR‖∞ 与 O(lr²) 项（lr 扫描）。
#   T-P2：r=‖F−B·pinv(B)F‖/‖F‖；无环图 r>1e-9 即死；含环图 r>0.30 占比>1/3 降级。
#   T-P3：g_a∈{0,0.1,1} 的 r 差异与 BR 不动点差异；判死线 1e-9。
# 零 API、零网络、种子冻结（SEED=210021，mean-field 臂零随机性）。
import json
import os
import time

import numpy as np

from deposon_diffusion import (DiffusionConfig, denoise, _walk_sums,
                               _G_AETHER, _EPS, _topological_order)
from deposon_protocol import row_normalize, full_candidate_mask
from gt_common import phi_potential

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(HERE, "results", "deposon_v21_gtformal.json")

SEED = 210021            # 冻结种子（图族采样）
TRAJ_STEPS = 20          # mean-field 轨迹步数（逐步判死）
LAM = 0.01               # lam_smooth（DiffusionConfig 默认）
BR_TOL, BR_MAXITER, BR_ETA = 1e-10, 1000, 0.5
MONO_TOL = 1e-9          # GT5B_TOL 口径
GA_GRID = (0.0, 0.1, 1.0)
LR_SWEEP = (0.025, 0.05, 0.1, 0.2)


# ---------------------------------------------------------- 小图图族（系统采样）
def graph_suite(seed=SEED):
    rng = np.random.default_rng(seed)
    suite = []

    def add(gid, fam, adj):
        adj = np.asarray(adj, float)
        np.fill_diagonal(adj, 0.0)
        if pick_source_target(adj) is not None:
            suite.append({"gid": gid, "family": fam, "adj": adj})

    for n in range(2, 9):
        add(f"chain_n{n}", "chain", np.eye(n, k=1))
    for n in range(3, 9):
        a = np.zeros((n, n)); a[0, 1:] = 1; add(f"star_out_n{n}", "star", a)
        a = np.zeros((n, n)); a[1:, 0] = 1; add(f"star_in_n{n}", "star", a)
        add(f"cycle_n{n}", "cyclic", np.eye(n, k=1) + np.eye(n, k=1 - n))
    for k in range(8):  # 随机树：节点 i≥1 向均匀父节点连边
        n = int(rng.integers(4, 9)); a = np.zeros((n, n))
        for i in range(1, n):
            a[int(rng.integers(0, i)), i] = 1.0
        add(f"tree_{k}_n{n}", "tree", a)
    for k in range(14):  # 随机 DAG（上三角 p=0.35）/ 随机含环图（双向 p=0.30）
        n = int(rng.integers(4, 9))
        a = (rng.random((n, n)) < 0.35).astype(float)
        a[np.tril_indices(n)] = 0.0
        add(f"rdag_{k}_n{n}", "dag", a)
        n = int(rng.integers(3, 9))
        add(f"rcyc_{k}_n{n}", "cyclic", (rng.random((n, n)) < 0.30).astype(float))
    return suite


def pick_source_target(adj):
    """BFS 最短路最长的可达有序对（平局取字典序最小）；无可达对返回 None。"""
    best, best_d = None, 0
    for s in range(adj.shape[0]):
        dist, q = {s: 0}, [s]
        while q:
            u = q.pop(0)
            for v in np.flatnonzero(adj[u] > 0):
                if int(v) not in dist:
                    dist[int(v)] = dist[u] + 1
                    q.append(int(v))
        for t, d in dist.items():
            if t != s and d > best_d:
                best, best_d = (s, t), d
    return best  # 例：3-环 (0,2)，链 (0,n-1)


# ---------------------------------------------------------- 场 / 势 / 梯度（g_a 可参数化）
def walk_sums_ga(W, source, target, g_a):
    """闭式游走和（谱半径 <1 保证），g_a 显式化；g_a=0.1 与 _walk_sums 逐位一致。"""
    W = np.asarray(W, float)
    t = 1.0 / (1.0 / np.maximum(W, _EPS) + g_a)
    t[W <= 0.0] = 0.0
    np.fill_diagonal(t, 0.0)
    n = W.shape[0]
    e_s = np.zeros(n); e_s[source] = 1.0
    e_t = np.zeros(n); e_t[target] = 1.0
    order = _topological_order(t > 0.0)
    if order is not None:  # DAG：拓扑序 DP（g_a=0 也良定义，与 _walk_sums 同口径）
        x = e_s.copy()
        for v in order:
            x[v] += float(t[:, v] @ x)
        y = e_t.copy()
        for u in reversed(order):
            y[u] += float(t[u, :] @ y)
        return x, y
    # 含环：g_a=0 时 t=W 行随机 ⇒ ρ(G)=1 ⇒ (I−G) 奇异（Neumann 级数发散，
    # 即备忘录 §5-3 的谱条件在 g_a=0 含环图上失效——如实抛出，由调用方标记）。
    return (np.linalg.solve(np.eye(n) - t.T, e_s),
            np.linalg.solve(np.eye(n) - t, e_t))


def grad_phi(W, source, target, lam=LAM, g_a=_G_AETHER):
    """∇Φ = (x[u]·y[v]/x_t)·dt_e/dW − 2λW（denoise 场梯度的相反数，aggregate）。"""
    x, y = (_walk_sums(W, source, target) if g_a == _G_AETHER
            else walk_sums_ga(W, source, target, g_a))
    xt = max(float(x[target]), _EPS)
    wpos = np.maximum(W, _EPS)
    dtdw = np.where(W > _EPS, 1.0 / (1.0 + g_a * wpos) ** 2, 0.0)
    g = (x[:, None] * y[None, :]) * (dtdw / xt) - 2.0 * lam * W
    np.fill_diagonal(g, 0.0)
    return g


def phi_ga(W, source, target, g_a, lam=LAM):
    if g_a == _G_AETHER:
        return phi_potential(W, source, target)
    x, _ = walk_sums_ga(W, source, target, g_a)
    off = W ** 2
    np.fill_diagonal(off, 0.0)
    return float(np.log(max(float(x[target]), _EPS)) - lam * off.sum())


def best_response_row(W, u, idx, mass, source, target, lam=LAM, g_a=_G_AETHER,
                      tol=BR_TOL, max_iter=BR_MAXITER, eta=BR_ETA):
    """构造 B（行玩家）BR：argmax_{w∈Δ(mass)} Φ(w, w_{-u})，镜像上升 + 回溯线搜索。"""
    W = np.array(W, float, copy=True)
    w = np.maximum(W[u, idx], 0.0)
    w = w * (mass / w.sum()) if w.sum() > 0 else np.full(len(idx), mass / len(idx))
    W[u, idx] = w
    phi, step = phi_ga(W, source, target, g_a, lam), eta
    for _ in range(max_iter):
        g = grad_phi(W, source, target, lam, g_a)[u, idx]
        w_new = w * np.exp(np.clip(step * g, -50.0, 50.0))
        w_new *= mass / w_new.sum()
        W[u, idx] = w_new
        phi_new = phi_ga(W, source, target, g_a, lam)
        if phi_new < phi - 1e-15:      # 回溯：收缩步长重试
            step *= 0.5
            W[u, idx] = w
            if step < 1e-12:
                break
            continue
        if np.max(np.abs(w_new - w)) < tol:
            w = w_new
            break
        w, phi, step = w_new, phi_new, min(step * 1.2, eta)
    return w


def cycle_space_dim(W):
    """有向关联矩阵 B 的左零空间维数 = E_dir − n + c（c=无向支撑连通分量数）。
    = 0 ⇔ 无向支撑为森林 ⇔ r 必须恒 0（备忘录 T-P2「无环」的正确口径：
    有向 DAG 但无向含三角时循环空间非空，r 无恒零义务——如实修正首版 bug）。"""
    e_dir = int(np.count_nonzero(W) - np.count_nonzero(np.diag(W)))
    parent = list(range(W.shape[0]))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    us, vs = np.nonzero(W > 0.0)
    for a, b in zip(us, vs):
        if a != b:
            parent[find(int(a))] = find(int(b))
    return e_dir - W.shape[0] + len({find(i) for i in range(W.shape[0])})


# ---------------------------------------------------------- Hodge 残余（GT-6 口径，范数比）
def hodge_residual(W, source, target, g_a=_G_AETHER):
    """r = ‖F−B·pinv(B)F‖/‖F‖，F_e=(x_u·y_v/x_t)·dt_e/dW 遍历支持边 (W>0)。"""
    g = grad_phi(W, source, target, lam=0.0, g_a=g_a)  # 纯场分量
    us, vs = np.nonzero(W > 0.0)
    keep = us != vs
    us, vs = us[keep], vs[keep]
    F = g[us, vs]
    total = float(F @ F)
    if total <= 0.0:
        return 0.0
    B = np.zeros((len(F), W.shape[0]))
    B[np.arange(len(F)), us] = 1.0
    B[np.arange(len(F)), vs] = -1.0
    resid = F - B @ (np.linalg.pinv(B) @ F)
    return float(np.sqrt(resid @ resid / total))


# ---------------------------------------------------------- 单任务评估（图 × 掩码行）
def eval_task(adj, source, target, u, cfg):
    """单节点全候选掩码下的 mean-field 轨迹 + 逐步 d_mf/d_br/cosine/ΔΦ。"""
    mask = full_candidate_mask(adj.shape[0], u)
    WT = row_normalize(adj)
    WT[mask] = 0.0
    _, _, states = denoise(WT, mask, cfg, source, target,
                           init_mode="prior_mean", record=True)
    idx = np.flatnonzero(mask[u])
    recs = []
    for k in range(len(states) - 1):
        W0, W1 = states[k], states[k + 1]
        w_br = best_response_row(W0, u, idx, 1.0, source, target)  # 全候选掩码 mass=1
        d_mf, d_br = (W1 - W0)[u, idx], w_br - W0[u, idx]
        n_mf, n_br = float(np.linalg.norm(d_mf)), float(np.linalg.norm(d_br))
        cos = (float(d_mf @ d_br) / (n_mf * n_br)
               if n_mf > 1e-14 and n_br > 1e-14 else 1.0)  # 零向量定义为平凡对齐（披露）
        recs.append({"step": k, "cosine": cos, "br_row": w_br if k == 0 else None,
                     "dPhi": phi_potential(W1, source, target)
                             - phi_potential(W0, source, target),
                     "dev_inf": float(np.max(np.abs(W1[u, idx] - w_br)))})
    W_init = states[0]
    rs, fp = {}, {}
    for ga in GA_GRID:
        try:
            rs[str(ga)] = hodge_residual(W_init, source, target, g_a=ga)
            fp[str(ga)] = best_response_row(W_init, u, idx, 1.0, source, target, g_a=ga)
        except np.linalg.LinAlgError:  # g_a=0 含环发散（见 walk_sums_ga）
            rs[str(ga)] = fp[str(ga)] = None
    pairs = [(a, b) for i, a in enumerate(GA_GRID) for b in GA_GRID[i + 1:]]
    fp_diffs = [float(np.max(np.abs(fp[str(a)] - fp[str(b)])))
                for a, b in pairs if fp[str(a)] is not None and fp[str(b)] is not None]
    r_diff = (abs(rs["0.1"] - rs["0.0"])
              if rs["0.1"] is not None and rs["0.0"] is not None else None)
    return {"states": recs, "cyclic": cycle_space_dim(W_init) > 0, "r_by_ga": rs,
            "r_diff_01_vs_00": r_diff, "W_init": W_init, "idx": idx, "u": u,
            "fp_diff_max": max(fp_diffs) if fp_diffs else None,
            "source": source, "target": target, "br_row": recs[0]["br_row"]}


def lr_scaling_substudy(tasks, n_take=10):
    """P1a 偏差分解：1−cos(lr) ≈ c·lr² 的实测（纯镜像上升方向 vs BR 方向）。"""
    out = []
    for t in tasks[:n_take]:
        W0, u, idx = t["W_init"], t["u"], t["idx"]
        w, d_br = W0[u, idx], t["br_row"] - W0[u, idx]
        if float(np.linalg.norm(d_br)) < 1e-12:
            continue
        g = grad_phi(W0, t["source"], t["target"])[u, idx]
        row = {}
        for lr in LR_SWEEP:  # d = 纯镜像上升位移（无收缩/投影）
            d = w * np.expm1(lr * w * g)
            n_d = float(np.linalg.norm(d))
            row[str(lr)] = (1.0 - float(d @ d_br) / (n_d * np.linalg.norm(d_br))
                            if n_d > 1e-14 else 0.0)
        out.append(row)
    cs = [row[str(lr)] / lr ** 2 for row in out for lr in LR_SWEEP
          if row[str(lr)] > 0]
    return {"per_task": out, "median_c_lr2": float(np.median(cs)) if cs else None,
            "note": "1-cos(lr) = c·lr^2 + O(lr^3)；median_c_lr2 为 c 的中位数实测"}


# ---------------------------------------------------------- 判定纯函数（预登记，先承诺）
def verdict_p1b(recs, tol=MONO_TOL):
    min_cos = min(r["cosine"] for r in recs)
    min_dphi = min(r["dPhi"] for r in recs)
    kill = ("cosine<0" if min_cos < 0.0
            else "dPhi<-1e-9" if min_dphi < -tol else None)
    return {"verdict": "triggered" if kill else "survives", "kill_reason": kill,
            "min_cosine": float(min_cos), "min_dPhi": float(min_dphi),
            "max_dev_inf": float(max(r["dev_inf"] for r in recs)),
            "n_states": len(recs)}


def verdict_p2(dag_rs, cyc_rs, dag_tol=MONO_TOL, cyc_thr=0.30, frac_thr=1.0 / 3.0):
    if any(r > dag_tol for r in dag_rs):
        return {"verdict": "killed_acyclic_residual", "frac_cyclic_high": None}
    frac = (float(np.mean([r > cyc_thr for r in cyc_rs])) if cyc_rs else 0.0)
    v = ("downgraded_to_approximate_potential_game" if frac > frac_thr
         else "survives")
    return {"verdict": v, "frac_cyclic_high": frac,
            "n_dag": len(dag_rs), "n_cyclic": len(cyc_rs)}  # 预登记阈值 0.30 / 1/3


def verdict_p3(r_diffs, fp_diffs, tol=MONO_TOL):
    return {"reparametrization_claim": ("killed" if max(r_diffs) > tol
                                        else "survives"),
            "structure_change_claim": ("killed" if max(fp_diffs) <= tol
                                       else "survives"),
            "max_r_diff": float(max(r_diffs)),
            "max_fp_diff": float(max(fp_diffs))}


# ---------------------------------------------------------- 主驱动
def main():
    t0 = time.time()
    cfg = DiffusionConfig(n_steps=TRAJ_STEPS, seed=SEED)
    suite = graph_suite()
    all_recs, dag_rs, cyc_rs, r_diffs, fp_diffs, tasks, per_graph = [], [], [], [], [], [], {}
    for g in suite:
        source, target = pick_source_target(g["adj"])
        gstats = []
        for u in range(g["adj"].shape[0]):
            t = eval_task(g["adj"], source, target, u, cfg)
            tasks.append(t)
            all_recs.extend(t["states"])
            (cyc_rs if t["cyclic"] else dag_rs).append(t["r_by_ga"]["0.1"])
            if t["r_diff_01_vs_00"] is not None:
                r_diffs.append(t["r_diff_01_vs_00"])
            if t["fp_diff_max"] is not None:
                fp_diffs.append(t["fp_diff_max"])
            gstats.append({"u": u, "cyclic": t["cyclic"], "r_ga0.1": t["r_by_ga"]["0.1"],
                           "min_cosine": min(s["cosine"] for s in t["states"]),
                           "min_dPhi": min(s["dPhi"] for s in t["states"])})
        per_graph[g["gid"]] = {"family": g["family"], "n": int(g["adj"].shape[0]),
                               "source": source, "target": target, "tasks": gstats}
    v1, v2 = verdict_p1b(all_recs), verdict_p2(dag_rs, cyc_rs)
    v3 = verdict_p3(r_diffs, fp_diffs)
    v3["n_tasks_ga0_divergent_excluded"] = sum(
        1 for t in tasks if t["r_by_ga"]["0.0"] is None)
    overall = ("triggered" if v1["verdict"] == "triggered"
               or v2["verdict"] == "killed_acyclic_residual" else "survives")
    runtime = round(time.time() - t0, 3)
    out = {"experiment": "deposon_v21_gtformal", "spec": "docs/GT_FORMALIZATION_v1.md §7",
           "seed": SEED, "traj_steps": TRAJ_STEPS, "lam": LAM,
           "ga_grid": list(GA_GRID), "lr_sweep": list(LR_SWEEP),
           "n_graphs": len(suite), "n_tasks": len(tasks), "n_states": len(all_recs),
           "verdict": {"overall": overall, "T_P1b": v1, "T_P2": v2, "T_P3": v3,
                       "P1a_deviation": {"max_dev_inf": v1["max_dev_inf"],
                                         "lr_scaling": lr_scaling_substudy(tasks)}},
           "residuals": {"dag": [float(r) for r in dag_rs],
                         "cyclic": [float(r) for r in cyc_rs]},
           "per_graph": per_graph, "runtime_sec": runtime,
           "honesty": [
               "no LLM API calls issued：纯本地种子化 numpy 计算，mean-field 臂零随机。",
               "图族为 n≤8 系统采样（链/星/树/随机DAG/含环 ≥50 图），非 2^(n²) 全穷举。",
               "T-P2 的 r 为范数比 ‖F−Bp‖/‖F‖（GT-6 为平方能量比，差一个平方）；"
               "判死阈值按备忘录数值执行（1e-9 / 0.30 / 1/3）。",
               "方向余弦在 ‖d_mf‖或‖d_br‖<1e-14 时定义为 1.0（平凡对齐，已披露）。",
               "g_a 变体经本地 walk_sums_ga 实现，g_a=0.1 与 _walk_sums 一致性由测试锁定。",
               "verdict_p1b/p2/p3 为预登记纯函数机械求值；triggered 如实归档，不调参。",
               "deposon_* 核心模块与既有 run 脚本一行不动；本文件为新建。"]}
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({"out": OUT_PATH, "runtime_sec": runtime,
                      "overall": overall,
                      "T_P1b": {k: v1[k] for k in ("verdict", "min_cosine", "min_dPhi")},
                      "T_P2": v2["verdict"], "T_P3": v3}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
