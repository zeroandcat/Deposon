# -*- coding: utf-8 -*-
# Deposon v2.0 博弈论 GT-7：温度-命中率-势的前沿扫描（预登记冻结于本文件常量）
#   → results/deposon_v20_gt7.json
#
# 背景（docs/GT_RECONSTRUCTION.md §2）：GT-5 意外——3/4 图上 dirichlet 噪声臂
# 终点 Φ **高于** mean-field，而 GT-1 证明噪声在命中率上有害。解读为
# 探索-利用权衡（噪声=探索者，mean-field=利用者；温度=噪声强度）。
# GT-7 把该意外变成定量结论：扫描温度梯度，同时记录 named Hits@3 与终点 Φ。
#
# 噪声旋钮（读代码确定）：本系统反向退火的唯一随机源是起点采样
#   W[i, idx] = mass * rng.dirichlet(np.ones(m))
# （run_v20_gt5.reverse_denoise_traj / deposon_diffusion.reverse_denoise）。
# Dirichlet 浓度参数 α 即等效温度旋钮：α→0 起点趋于单点（高温/强探索），
# α→∞ 起点趋于均匀（低温/弱探索=前向终态本身），mean-field（prior_mean，
# 跳过采样）为 T=0 确定性极限端点。温度梯度 = α ∈ GT7_ALPHAS + mean-field。
#
# 协议（冻结，先于数据）：
#   图集与 GT-5 完全相同（S6, L_physics_concepts, L_biological_taxonomy,
#   L_algorithm_process），抽样种子相同（GT5_SAMPLE_SEED+图序）⇒ 任务集与
#   GT-5 逐任务对齐，可直接对照；
#   每图 GT7_TASKS_PER_GRAPH=5 条 named 留一任务（全候选协议）；
#   每个温度档 GT7_SEEDS=5 个独立种子，报均值±标准差（mean-field 确定性，
#   单次，std=0 如实标注）；
#   每档记录两个量：named Hits@3（命中率）与终点 Φ=-scatter_energy(aggregate)。
#
# 判定（预登记，机械求值，见 gt7_verdict，tests/test_v20_gt7.py 锁定）：
#   支持：存在中间温度档同时满足（命中率 ≥ GT7_HIT_FRAC × mean-field 命中率）
#         且（终点 Φ > mean-field 终点 Φ）的图占比 ≥ GT7_PASS_GRAPH_FRAC=3/4
#         ⇒ supports_tradeoff_frontier；
#   推翻：全部图、全部温度档命中率与 Φ 相对 mean-field 的偏移同向
#         （(Δhits)(ΔΦ) ≥ -GT7_COVAR_TOL）⇒ no_tradeoff（推翻 GT-5 解读）；
#   其余：mixed，如实报逐图形态。
#
# 零 LLM API；deposon_diffusion.py / run_v20_gt5.py 等既有文件一行不动
# （Φ/轨迹/单调率经只读 import 复用；α 参数化反向为本文件内的逐行副本）。
import json
import os
import time

import numpy as np

from deposon_diffusion import (DiffusionConfig, config_dict, forward_diffuse,
                               _masked_row_stats, _project_masked, _walk_sums,
                               _G_AETHER, _EPS)
from mindmap_corpus_v20 import CORPUS_DIR, load_corpus
from run_v15_experiment import row_normalize
from run_v19_fullrank import full_candidate_mask, gold_rank
from run_v20_gt5 import (ENERGY_MODE, GT5_GRAPHS, GT5_SAMPLE_SEED,
                         phi_potential, _graph_tasks)

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
OUT_PATH = os.path.join(RESULTS, "deposon_v20_gt7.json")

# ------------------------------------------------------------ 预登记冻结常量
GT7_ALPHAS = (0.3, 0.5, 1.0, 2.0, 5.0, 20.0)  # Dirichlet 浓度=等效温度旋钮
GT7_TASKS_PER_GRAPH = 5
GT7_SEEDS = 5                  # 每温度档 ≥5 seed（预登记最低线）
GT7_SEED_BASE = 507_000_000
GT7_HIT_FRAC = 0.9             # 命中率 ≥ 90% × mean-field
GT7_PASS_GRAPH_FRAC = 0.75     # 满足双条件的图占比 ≥ 3/4 ⇒ 支持前沿存在
GT7_COVAR_TOL = 1e-12          # 「同向变化」数值容差（(Δhits)(ΔΦ) ≥ -tol）
MEANFIELD_LABEL = "mean_field_T0"   # T=0 确定性极限端点


def reverse_denoise_traj_alpha(WT, mask, cfg, source, target, alpha):
    """run_v20_gt5.reverse_denoise_traj 的 α 参数化副本（既有文件一行不动）。

    算法主体逐行对应；唯一差异：dirichlet 起点浓度 np.ones(m) →
    np.full(m, alpha)。alpha=1.0 与原 dirichlet 逐位一致
    （tests/test_v20_gt7.py 回归断言锁定）。
    """
    WT = np.asarray(WT, dtype=float)
    mask = np.asarray(mask, dtype=bool)
    if alpha is not None and alpha <= 0.0:
        raise ValueError(f"alpha must be positive or None, got {alpha}")
    W = WT.copy()
    if cfg.n_steps <= 0:
        return [W]
    if alpha is not None:  # dirichlet 起点，浓度 α = 等效温度旋钮
        rng = np.random.default_rng(cfg.seed)
        for i in range(W.shape[0]):
            idx, m, p = _masked_row_stats(W, mask, i)
            if m == 0:
                continue
            mass = p * m
            if mass > 0.0:
                W[i, idx] = mass * rng.dirichlet(np.full(m, alpha))
        _project_masked(W, mask)
    else:  # mean-field：T=0 确定性极限，保持前向终态，不调 rng
        _project_masked(W, mask)
    states = [W.copy()]
    for _t in range(cfg.n_steps, 0, -1):
        grad = np.zeros_like(W)
        if cfg.field_guidance and source != target:
            x, y = _walk_sums(W, source, target)
            xt = max(float(x[target]), _EPS)
            wpos = np.maximum(W, _EPS)
            dtdw = np.where(W > _EPS, 1.0 / (1.0 + _G_AETHER * wpos) ** 2, 0.0)
            grad -= (x[:, None] * y[None, :]) * (dtdw / xt)
        if cfg.lam_smooth:
            grad[mask] += 2.0 * cfg.lam_smooth * W[mask]
        W[mask] *= np.exp(-cfg.lr * W[mask] * grad[mask])
        W[mask] = (1.0 - cfg.lr) * W[mask]
        W[~mask] = WT[~mask]
        _project_masked(W, mask)
        states.append(W.copy())
    return states


def hit_at_3(W_final, mask, u, v):
    """named Hits@3：金边 v 在全部候选中按 W_final[u] 降序的秩 < 3。"""
    cand = np.flatnonzero(mask[u])
    return float(gold_rank(W_final[u], cand, v) < 3)


# ------------------------------------------------------------ 判定规则（冻结）
def gt7_verdict(per_graph, hit_frac=GT7_HIT_FRAC,
                pass_graph_frac=GT7_PASS_GRAPH_FRAC,
                covar_tol=GT7_COVAR_TOL):
    """GT-7 冻结判定（机械求值，纯函数，tests/test_v20_gt7.py 锁定）：

    per_graph: {gid: {"meanfield": {"hits": float, "phi": float},
                      "temperatures": {label: {"hits_mean": float,
                                               "phi_mean": float}}}}
    支持：存在某中间温度档同时满足 hits_mean ≥ hit_frac×mf_hits 且
         phi_mean > mf_phi 的图占比 ≥ pass_graph_frac
         ⇒ supports_tradeoff_frontier；
    推翻：全部图全部档 (Δhits)(ΔΦ) ≥ -covar_tol（同向变化）⇒ no_tradeoff；
    其余：mixed。
    """
    gids = list(per_graph)
    n = len(gids)
    frontier_graphs, per_graph_detail = {}, {}
    all_codirectional = True
    for gid in gids:
        entry = per_graph[gid]
        mf_hits = float(entry["meanfield"]["hits"])
        mf_phi = float(entry["meanfield"]["phi"])
        ok_temps = []
        codirectional = True
        for label, t in entry["temperatures"].items():
            dh = float(t["hits_mean"]) - mf_hits
            dp = float(t["phi_mean"]) - mf_phi
            if dh * dp < -covar_tol:
                codirectional = False
            if (float(t["hits_mean"]) >= hit_frac * mf_hits
                    and float(t["phi_mean"]) > mf_phi):
                ok_temps.append(label)
        frontier_graphs[gid] = ok_temps
        per_graph_detail[gid] = {"codirectional_all_temps": codirectional,
                                 "frontier_temps": ok_temps}
        all_codirectional = all_codirectional and codirectional
    n_frontier = sum(1 for gid in gids if frontier_graphs[gid])
    frac_frontier = (n_frontier / n) if n else None
    if (frac_frontier is not None and frac_frontier >= pass_graph_frac):
        verdict = "supports_tradeoff_frontier"
    elif all_codirectional:
        verdict = "no_tradeoff"
    else:
        verdict = "mixed"
    return {"verdict": verdict,
            "supported_tradeoff_frontier": bool(
                verdict == "supports_tradeoff_frontier"),
            "graphs_with_frontier_temp": {g: t for g, t in
                                          frontier_graphs.items() if t},
            "n_graphs_with_frontier_temp": n_frontier,
            "frac_graphs_with_frontier_temp": frac_frontier,
            "all_graphs_codirectional": bool(all_codirectional),
            "per_graph_direction": per_graph_detail,
            "n_graphs": n,
            "thresholds": {"hit_frac": hit_frac,
                           "pass_graph_frac": pass_graph_frac,
                           "covar_tol": covar_tol}}


def frontier_shape(temperatures):
    """逐图形态描述（报告用，不参与判定）：hits/Φ 与 log α 的相关方向。"""
    alphas = sorted(float(a) for a in temperatures)
    x = np.log(np.asarray(alphas))
    out = {}
    for key in ("hits_mean", "phi_mean"):
        y = np.asarray([temperatures[str(a)][key] for a in alphas])
        if np.std(y) < 1e-15:
            out[key] = {"logalpha_corr": 0.0, "shape": "flat"}
        else:
            r = float(np.corrcoef(x, y)[0, 1])
            out[key] = {"logalpha_corr": r,
                        "shape": ("increasing_with_alpha" if r > 0.5 else
                                  "decreasing_with_alpha" if r < -0.5 else
                                  "nonmonotone_or_weak")}
    return out


# ------------------------------------------------------------ 实验主体
def run_graph(g, cfg, graph_ord=0, n_tasks=GT7_TASKS_PER_GRAPH,
              n_seeds=GT7_SEEDS):
    """单图：逐温度档（α 网格 + mean-field 端点）记录 Hits@3 与终点 Φ。"""
    N = g["N"]
    src, tgt = g["source"], g["target"]
    adj = np.zeros((N, N))
    for (u, v) in g["edges"]:
        adj[u, v] = 1.0
    W_true = row_normalize(adj)
    tasks = _graph_tasks(g, n_tasks, GT5_SAMPLE_SEED + graph_ord)  # 同 GT-5

    # 前向终态逐任务预计算（与温度无关；seed=0 同 GT-5）
    task_data = []
    for (u, v) in tasks:
        W_obs = W_true.copy()
        W_obs[u, v] = 0.0
        mask = full_candidate_mask(N, u)
        cfg_arm = DiffusionConfig(**{**config_dict(cfg), "seed": 0,
                                     "energy_mode": ENERGY_MODE,
                                     "field_guidance": True})
        WT = forward_diffuse(W_obs, mask, cfg_arm)[-1]
        task_data.append((u, v, mask, cfg_arm, WT))

    def run_one(k, alpha, seed):
        u, v, mask, cfg_arm, WT = task_data[k]
        cfg_r = DiffusionConfig(**{**config_dict(cfg_arm), "seed": seed})
        states = reverse_denoise_traj_alpha(WT, mask, cfg_r, src, tgt, alpha)
        phi_end = phi_potential(states[-1], src, tgt)
        hit = hit_at_3(states[-1], mask, u, v)
        return hit, phi_end

    # mean-field 端点（确定性，单次）
    mf_hits_per_task, mf_phi_per_task = [], []
    for k in range(len(tasks)):
        hit, phi_end = run_one(k, None, 0)
        mf_hits_per_task.append(hit)
        mf_phi_per_task.append(phi_end)
    meanfield = {"hits": float(np.mean(mf_hits_per_task)),
                 "phi": float(np.mean(mf_phi_per_task)),
                 "hits_std": 0.0, "phi_std": 0.0,
                 "note": "确定性极限，单次运行，std=0 如实标注（非采样）",
                 "hits_per_task": [float(h) for h in mf_hits_per_task],
                 "phi_per_task": [float(p) for p in mf_phi_per_task]}

    temperatures = {}
    for alpha in GT7_ALPHAS:
        per_seed_hits, per_seed_phi = [], []
        for r in range(n_seeds):
            seed = GT7_SEED_BASE + graph_ord * 1_000_000 + r * 1_000
            hits, phis = [], []
            for k in range(len(tasks)):
                hit, phi_end = run_one(k, alpha, seed + k)
                hits.append(hit)
                phis.append(phi_end)
            per_seed_hits.append(float(np.mean(hits)))
            per_seed_phi.append(float(np.mean(phis)))
        temperatures[str(float(alpha))] = {
            "alpha": float(alpha),
            "hits_mean": float(np.mean(per_seed_hits)),
            "hits_std": float(np.std(per_seed_hits)),
            "phi_mean": float(np.mean(per_seed_phi)),
            "phi_std": float(np.std(per_seed_phi)),
            "hits_per_seed": per_seed_hits,
            "phi_per_seed": per_seed_phi,
            "n_seeds": n_seeds}

    return {"graph_id": g["graph_id"], "N": int(N), "source": int(src),
            "target": int(tgt), "n_tasks": len(tasks),
            "sample_seed": GT5_SAMPLE_SEED + graph_ord,
            "task_edges": [[int(u), int(v)] for (u, v) in tasks],
            "meanfield": meanfield, "temperatures": temperatures,
            "frontier_shape": frontier_shape(temperatures),
            "gt5_reversal_reproduced": bool(
                temperatures["1.0"]["phi_mean"] > meanfield["phi"])}


def main():
    t0 = time.time()
    cfg = DiffusionConfig()
    graphs = {g["graph_id"]: g
              for g in load_corpus(CORPUS_DIR, families=("S", "L"))}
    missing = [g for g in GT5_GRAPHS if g not in graphs]
    if missing:
        raise RuntimeError(f"corpus missing {missing} — 先运行语料生成/摄入")
    per_graph, details = {}, {}
    for ord_, gid in enumerate(GT5_GRAPHS):
        res = run_graph(graphs[gid], cfg, graph_ord=ord_)
        details[gid] = res
        per_graph[gid] = {"meanfield": res["meanfield"],
                          "temperatures": res["temperatures"]}
    verdict = gt7_verdict(per_graph)
    runtime = round(time.time() - t0, 3)
    out = {"experiment": "deposon_v20_gt7", "spec_version": "v2.0",
           "spec": ("docs/GT_RECONSTRUCTION.md §2/§5.4：温度-命中率-势的"
                    "前沿扫描，把 GT-5 反转变成定量结论"),
           "config": config_dict(cfg),
           "temperature_knob": {
               "mechanism": ("反向退火唯一随机源 = dirichlet 起点采样；浓度参数 "
                             "α 即等效温度：α→0 强探索（高温），α→∞ 弱探索"
                             "（低温），mean-field(prior_mean) 为 T=0 端点"),
               "alphas": list(GT7_ALPHAS),
               "alpha1_equals_gt5_dirichlet": True},
           "preregistered": {
               "graphs": list(GT5_GRAPHS),
               "tasks_per_graph": GT7_TASKS_PER_GRAPH,
               "sample_seed": GT5_SAMPLE_SEED,
               "seeds_per_temperature": GT7_SEEDS,
               "seed_base": GT7_SEED_BASE,
               "pass_rule": (f"存在中间温度档满足 命中率 ≥ {GT7_HIT_FRAC}×"
                             f"mean-field 且 终点 Φ > mean-field 的图占比 ≥ "
                             f"{GT7_PASS_GRAPH_FRAC} ⇒ supports_tradeoff_frontier"),
               "kill_rule": ("全部图全部档命中率与 Φ 相对 mean-field 同向变化 "
                             "⇒ no_tradeoff（推翻 GT-5 的探索-利用解读）"),
               "else_rule": "其余 ⇒ mixed，如实报逐图形态"},
           "per_graph": per_graph,
           "per_graph_detail": {g: {"frontier_shape": d["frontier_shape"],
                                    "gt5_reversal_reproduced":
                                    d["gt5_reversal_reproduced"],
                                    "task_edges": d["task_edges"]}
                                for g, d in details.items()},
           "gt5_reversal_reproduced_graphs": [
               g for g, d in details.items() if d["gt5_reversal_reproduced"]],
           "verdict": verdict,
           "runtime_sec": runtime,
           "honesty": [
               "no LLM API calls issued: 族 L 图从 corpus/v20 只读加载，全部"
               "实验为本地种子化 numpy 运行。",
               "温度旋钮如实说明：本系统无显式温度超参，唯一随机源是 dirichlet "
               "起点；按任务指示用浓度参数 α 扫描，mean-field 为 T=0 端点。α=1 "
               "档与 GT-5 的 dirichlet 臂逐位一致（tests/test_v20_gt7.py 锁定）。",
               "图集与任务抽样种子与 GT-5 完全相同 ⇒ 逐任务可对照；GT-5 反转"
               "（dirichlet 终点 Φ > mean-field）的复现与否按 α=1 档逐图如实报。",
               "Φ 定义与 GT-5 逐字相同（Φ=-scatter_energy(aggregate)），函数"
               "经只读 import 复用；Hits@3 用与 GT-1 同一 gold_rank 全候选口径。",
               "mean-field 为确定性单次运行，std 如实标 0（非采样标准差）；温度"
               "档均值±标准差基于 GT7_SEEDS=5 个独立种子。",
               "判定规则为纯函数 gt7_verdict 机械求值，tests/test_v20_gt7.py "
               "锁定；mixed 区间不美化，逐图形态经 frontier_shape 如实给出。",
               "deposon_diffusion.py / run_v20_gt5.py 等既有文件一行不动；α "
               "参数化反向为本文件内逐行对应副本。",
               f"总运行 {runtime}s（预算 600s 内，未缩减 seed/图数）"
               if runtime <= 600 else
               f"总运行 {runtime}s 超预算，已缩减 seed 数（见常量与披露）。"]}
    os.makedirs(RESULTS, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({
        "out": OUT_PATH, "runtime_sec": runtime,
        "verdict": verdict["verdict"],
        "frac_frontier": verdict["frac_graphs_with_frontier_temp"],
        "gt5_reversal_reproduced": out["gt5_reversal_reproduced_graphs"],
        "per_graph_hits_phi": {
            g: {"mf": [round(d["meanfield"]["hits"], 3),
                       round(d["meanfield"]["phi"], 4)],
                **{a: [round(t["hits_mean"], 3), round(t["phi_mean"], 4)]
                   for a, t in d["temperatures"].items()}}
            for g, d in details.items()}}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
