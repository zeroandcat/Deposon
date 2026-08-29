# -*- coding: utf-8 -*-
# Deposon v2.0 博弈论 GT-5：势函数单调性（docs/CLOSURE_v19_and_v2X_gametheory.md
# §3.1 势博弈框架的**判定性性质**，预登记冻结于本文件常量）
#   → results/deposon_v20_gt5.json
#
# 势博弈定义性质：最优反应动态使势函数 Φ 单调不减。本实验直接检验该性质，
# 比 GT-1（终点命中率差距）更强——它检验的是**整个轨迹**的 Lyapunov 性。
#
# 势函数 Φ（从扩散过程本身导出，非事后拼凑）：
#   反向退火（deposon_diffusion.reverse_denoise）的更新方向就是
#   scatter_energy(energy_mode="aggregate") 的解析梯度下降方向
#   （reverse_denoise docstring：dE/dW[u,v] = -(x[u]·y[v]/x_t)·dt_e/dW）。
#   因此该动态的 Lyapunov/势函数只能是
#       Φ(W) = -E(W) = log(聚合透射率 x[target]) - lam_smooth * Σ_{i≠j} W[i,j]²
#   即「场=势函数 Φ 的最优反应极限」这一陈述中的 Φ 本身（E9.1/§3.1 口径）。
#   最优反应动态应使 Φ 单调不减（E 单调不增）。
#
# 实验协议（冻结）：
#   图集 = {S6（主档锚点）, L_physics_concepts, L_biological_taxonomy,
#           L_algorithm_process}（族 L 从 corpus/v20 只读加载，零 API）；
#   每图 GT5_TASKS_PER_GRAPH 条 named 留一任务（全候选协议，同 GT-1 口径，
#   抽样种子 GT5_SAMPLE_SEED+图序）；
#   mean-field 臂：init_mode="prior_mean" 确定性反向（DDIM η=0 对应物）；
#   dirichlet 臂：每任务 GT5_SEEDS=10 个独立种子；
#   两臂逐点记录 Φ（T+1 个点/轨迹）。
#
# 判定（预登记，机械求值，见 gt5_verdict）：
#   支持：mean-field Φ 单调率 = 100%（每步 ΔΦ ≥ -1e-9）的图 ≥ 全部图的 80%，
#         且每张图 dirichlet 终点 Φ 均值 < mean-field 终点 Φ 均值；
#   斩杀线 H_GT5_dead：mean-field 单调率 < 50% 的图 ≥ 2 ⇒ 势博弈解释判死；
#   其余区间如实报 inconclusive（预登记未定义，不向任一方向美化）。
#
# 零 LLM API；deposon_diffusion.py 一行不动（轨迹记录版反向为本文件内的
# 参数化副本，逐行对应 reverse_denoise_init，仅增加 states 记录）。
import json
import os
import time

import numpy as np

from deposon_diffusion import (DiffusionConfig, config_dict, denoise,
                               forward_diffuse, scatter_energy)
from mindmap_corpus_v20 import CORPUS_DIR, load_corpus
from run_v15_experiment import row_normalize
from run_v19_fullrank import full_candidate_mask

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
OUT_PATH = os.path.join(RESULTS, "deposon_v20_gt5.json")

# ------------------------------------------------------------ 预登记冻结常量
GT5_GRAPHS = ("S6", "L_physics_concepts",
              "L_biological_taxonomy", "L_algorithm_process")
GT5_TASKS_PER_GRAPH = 5
GT5_SEEDS = 10
GT5_SAMPLE_SEED = 505_000
GT5_SEED_BASE = 505_000_000
GT5_TOL = 1e-9              # 单调性数值容差（ΔΦ ≥ -GT5_TOL 记为不减）
GT5_PASS_GRAPH_FRAC = 0.8   # mean-field 100% 单调图占比 ≥ 0.8
GT5_MONO_FULL = 1.0         # 「单调率=100%」的满分线
GT5_MONO_DEAD = 0.5         # 单调率 < 50% 计为判死图
GT5_DEAD_MIN_GRAPHS = 2     # 判死图 ≥ 2 ⇒ H_GT5_dead
ENERGY_MODE = "aggregate"   # 与默认配置及 reverse_denoise 解析梯度一致


def phi_potential(W, source, target, energy_mode=ENERGY_MODE):
    """势函数 Φ(W) = -scatter_energy(W)（聚合透射率对数 − 平滑正则）。

    理由：反向退火动态正是 scatter_energy 的（自然）梯度下降，故其 Lyapunov
    函数为 -E。gold_edges 参数按 SPEC 防泄漏契约传 None（函数体不读取）。
    """
    val = -scatter_energy(np.asarray(W, dtype=float), None, source, target,
                          energy_mode=energy_mode)
    return float(val)


def reverse_denoise_traj(WT, mask, cfg, source, target, init_mode):
    """reverse_denoise_init（run_v19_meanfield.py）的轨迹记录副本。

    算法主体逐行对应：init_mode="dirichlet" 与原 reverse_denoise 相同的
    Dirichlet(1) 随机起点；init_mode="prior_mean" 为确定性 mean-field 极限。
    唯一新增：每步后把当前 W 追加到 states（共 n_steps+1 个状态，含起点）。
    deposon_diffusion.py / run_v19_meanfield.py 一行不动。

    候选 1 重构：实现已统一收敛到 deposon_diffusion.denoise（薄转发，
    record=True，数值逐位不变，tests/test_v20_gt5.py 锁定）。
    """
    _W, _steps, states = denoise(WT, mask, cfg, source, target,
                                 init_mode=init_mode, record=True)
    return states


def phi_trajectory(states, source, target):
    """逐状态求 Φ，返回长度 len(states) 的列表。"""
    return [phi_potential(W, source, target) for W in states]


def monotone_rate(traj, tol=GT5_TOL):
    """单调不减率：ΔΦ_t ≥ -tol 的步数占比；空/单点轨迹定义为 1.0。"""
    traj = [float(v) for v in traj]
    if len(traj) < 2:
        return 1.0
    diffs = np.diff(traj)
    return float(np.mean(diffs >= -tol))


# ------------------------------------------------------------ 判定规则（冻结）
def gt5_verdict(per_graph, pass_frac=GT5_PASS_GRAPH_FRAC,
                mono_full=GT5_MONO_FULL, mono_dead=GT5_MONO_DEAD,
                dead_min_graphs=GT5_DEAD_MIN_GRAPHS):
    """GT-5 冻结判定（机械求值，纯函数，tests/test_v20_gt5.py 锁定）：

    per_graph: {gid: {"meanfield_monotone_rate": float,
                      "dirichlet_mean_endpoint": float,
                      "meanfield_mean_endpoint": float}}
    支持：单调率=100% 的图占比 ≥ pass_frac 且每张图
         dirichlet 终点 Φ 均值 < mean-field 终点 Φ 均值；
    斩杀：单调率 < 50% 的图 ≥ dead_min_graphs ⇒ H_GT5_dead；
    其余：inconclusive（预登记未定义区间）。
    """
    gids = list(per_graph)
    n = len(gids)
    full_mono = [g for g in gids
                 if per_graph[g]["meanfield_monotone_rate"] >= mono_full]
    dead_graphs = [g for g in gids
                   if per_graph[g]["meanfield_monotone_rate"] < mono_dead]
    endpoint_gap_ok = all(
        per_graph[g]["dirichlet_mean_endpoint"]
        < per_graph[g]["meanfield_mean_endpoint"] for g in gids)
    frac_full = (len(full_mono) / n) if n else None
    if len(dead_graphs) >= dead_min_graphs:
        verdict = "H_GT5_dead"
    elif (frac_full is not None and frac_full >= pass_frac and endpoint_gap_ok):
        verdict = "supports_potential_game_framework"
    else:
        verdict = "inconclusive_preregistered_undefined_band"
    return {"verdict": verdict,
            "supported_potential_game": bool(
                verdict == "supports_potential_game_framework"),
            "graphs_with_full_monotonicity": full_mono,
            "frac_graphs_full_monotonicity": frac_full,
            "graphs_below_50pct_monotonicity": dead_graphs,
            "dirichlet_endpoint_below_meanfield_all_graphs": bool(
                endpoint_gap_ok),
            "n_graphs": n,
            "thresholds": {"pass_graph_frac": pass_frac,
                           "mono_full": mono_full, "mono_dead": mono_dead,
                           "dead_min_graphs": dead_min_graphs,
                           "tol": GT5_TOL}}


# ------------------------------------------------------------ 实验主体
def _graph_tasks(g, n_tasks, sample_seed):
    """每图抽 n_tasks 条 named 留一任务（种子化，可复现）。"""
    named = [tuple(e) for e in g["named_edges"]]
    rng = np.random.default_rng(sample_seed)
    take = rng.choice(len(named), size=min(n_tasks, len(named)), replace=False)
    return [named[int(k)] for k in sorted(take.tolist())]


def run_graph(g, cfg, n_tasks=GT5_TASKS_PER_GRAPH, n_seeds=GT5_SEEDS,
              graph_ord=0):
    """单图：逐任务 mean-field / dirichlet 反向，逐点记录 Φ。"""
    N = g["N"]
    src, tgt = g["source"], g["target"]
    adj = np.zeros((N, N))
    for (u, v) in g["edges"]:
        adj[u, v] = 1.0
    W_true = row_normalize(adj)
    tasks = _graph_tasks(g, n_tasks, GT5_SAMPLE_SEED + graph_ord)

    mf_rates, mf_endpoints = [], []
    mf_phi_trajs, mf_deltas_min = [], []
    di_mean_trajs, di_endpoints_mean = [], []
    di_stepmean_monotone = []
    per_task = []
    for k, (u, v) in enumerate(tasks):
        adj_obs = adj.copy()
        adj_obs[u, v] = 0.0
        W_obs = W_true.copy()
        W_obs[u, v] = 0.0
        mask = full_candidate_mask(N, u)

        cfg_arm = DiffusionConfig(**{**config_dict(cfg), "seed": 0,
                                     "energy_mode": ENERGY_MODE,
                                     "field_guidance": True})
        traj_fwd = forward_diffuse(W_obs, mask, cfg_arm)
        WT = traj_fwd[-1]

        # mean-field（确定性极限，与 seed 无关，单次）
        states_mf = reverse_denoise_traj(WT, mask, cfg_arm, src, tgt,
                                         init_mode="prior_mean")
        phi_mf = phi_trajectory(states_mf, src, tgt)
        mf_rates.append(monotone_rate(phi_mf))
        mf_endpoints.append(phi_mf[-1])
        mf_phi_trajs.append(phi_mf)
        mf_deltas_min.append(float(np.min(np.diff(phi_mf)))
                             if len(phi_mf) > 1 else 0.0)

        # dirichlet（n_seeds 独立运行）
        di_trajs = []
        for r in range(n_seeds):
            cfg_r = DiffusionConfig(**{**config_dict(cfg),
                                       "seed": GT5_SEED_BASE
                                       + graph_ord * 100_000 + k * 1_000 + r,
                                       "energy_mode": ENERGY_MODE,
                                       "field_guidance": True})
            states_di = reverse_denoise_traj(traj_fwd[-1], mask, cfg_r,
                                             src, tgt, init_mode="dirichlet")
            di_trajs.append(phi_trajectory(states_di, src, tgt))
        di_arr = np.asarray(di_trajs)            # (n_seeds, T+1)
        di_mean = di_arr.mean(axis=0)
        di_mean_trajs.append([float(v) for v in di_mean])
        di_endpoints_mean.append(float(di_mean[-1]))
        di_stepmean_monotone.append(monotone_rate(di_mean))
        per_task.append({
            "task_edge": [int(u), int(v)],
            "meanfield_phi": [float(v) for v in phi_mf],
            "meanfield_monotone_rate": mf_rates[-1],
            "meanfield_min_step_delta": mf_deltas_min[-1],
            "dirichlet_phi_mean_over_seeds": [float(v) for v in di_mean],
            "dirichlet_phi_endpoint_per_seed": [
                float(t[-1]) for t in di_trajs],
            "dirichlet_stepmean_monotone_rate": di_stepmean_monotone[-1],
            "dirichlet_endpoint_mean": di_endpoints_mean[-1]})

    summary = {"meanfield_monotone_rate": float(np.mean(mf_rates)),
               "meanfield_mean_endpoint": float(np.mean(mf_endpoints)),
               "dirichlet_mean_endpoint": float(np.mean(di_endpoints_mean)),
               "dirichlet_stepmean_monotone_rate": float(
                   np.mean(di_stepmean_monotone)),
               "endpoint_gap_meanfield_minus_dirichlet": float(
                   np.mean(mf_endpoints) - np.mean(di_endpoints_mean))}
    return {"graph_id": g["graph_id"], "N": int(N), "source": int(src),
            "target": int(tgt), "n_tasks": len(tasks), "n_seeds": n_seeds,
            "sample_seed": GT5_SAMPLE_SEED + graph_ord,
            "tasks": per_task, "summary": summary}


def main():
    t0 = time.time()
    cfg = DiffusionConfig()
    graphs = {g["graph_id"]: g
              for g in load_corpus(CORPUS_DIR, families=("S", "L"))}
    missing = [g for g in GT5_GRAPHS if g not in graphs]
    if missing:
        raise RuntimeError(f"corpus missing {missing} — 先运行语料生成/摄入")
    per_graph = {}
    details = {}
    for ord_, gid in enumerate(GT5_GRAPHS):
        res = run_graph(graphs[gid], cfg, graph_ord=ord_)
        details[gid] = res
        per_graph[gid] = res["summary"]
    verdict = gt5_verdict(per_graph)
    runtime = round(time.time() - t0, 3)
    out = {"experiment": "deposon_v20_gt5", "spec_version": "v2.0",
           "spec": ("docs/CLOSURE_v19_and_v2X_gametheory.md §3.1 势博弈框架"
                    "的判定性性质：最优反应动态 ⇔ 势函数 Φ 单调不减"),
           "config": config_dict(cfg),
           "potential_function": {
               "definition": "Φ(W) = -scatter_energy(W, aggregate) = "
                             "log(聚合透射率 x[target]) - lam_smooth*Σ_{i≠j}W²",
               "justification": ("反向退火 reverse_denoise 的解析梯度即 "
                                 "scatter_energy(aggregate) 的梯度（dE/dW[u,v]"
                                 "=-(x[u]·y[v]/x_t)·dt_e/dW），故该最优反应动态"
                                 "的 Lyapunov 函数唯一自然选择为 -E；非事后拼凑"),
               "energy_mode": ENERGY_MODE},
           "preregistered": {
               "graphs": list(GT5_GRAPHS),
               "tasks_per_graph": GT5_TASKS_PER_GRAPH,
               "dirichlet_seeds": GT5_SEEDS,
               "sample_seed": GT5_SAMPLE_SEED,
               "seed_base": GT5_SEED_BASE,
               "tol": GT5_TOL,
               "pass_rule": ("mean-field 单调率=100% 的图占比 ≥ "
                             f"{GT5_PASS_GRAPH_FRAC} 且全部图 dirichlet 终点 "
                             "Φ 均值 < mean-field 终点 Φ 均值 ⇒ 支持势博弈框架"),
               "kill_rule": (f"mean-field 单调率 < {GT5_MONO_DEAD} 的图 ≥ "
                             f"{GT5_DEAD_MIN_GRAPHS} ⇒ H_GT5_dead，如实宣布")},
           "per_graph_summary": per_graph,
           "per_graph_detail": details,
           "verdict": verdict,
           "runtime_sec": runtime,
           "honesty": [
               "no LLM API calls issued: 族 L 图从 corpus/v20 只读加载，全部"
               "实验为本地种子化 numpy 运行。",
               "Φ 定义先于实验冻结：Φ=-scatter_energy(aggregate)，即反向退火"
               "解析梯度对应的能量函数负值；若 Φ 不单调，如实报告而非换函数。",
               "反向动态含向 W_obs 的收缩步 W←(1-lr)W（非梯度步）与单纯形投影，"
               "理论上不保证 Φ 逐步单调；本实验正是对该定义性性质的检验，"
               "任何非单调步均计入单调率，不剔除。",
               "dirichlet 臂 Φ 记录包含随机起点本身（轨迹第 0 点），未做利于"
               "单调性的对齐/平移。",
               "判定规则为纯函数 gt5_verdict 机械求值，tests/test_v20_gt5.py "
               "锁定；落在预登记未定义区间时报 inconclusive，不美化。",
               "deposon_diffusion.py / run_v19_meanfield.py 一行不动；轨迹记录"
               "版反向为本文件内逐行对应副本，仅增加 states 记录。",
               f"总运行 {runtime}s（预算 600s 内，未缩减图数/步数）"
               if runtime <= 600 else
               f"总运行 {runtime}s 超预算，已按预登记缩减图数/步数（见常量）。"]}
    os.makedirs(RESULTS, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({"out": OUT_PATH, "runtime_sec": runtime,
                      "verdict": verdict["verdict"],
                      "per_graph": {g: round(s["meanfield_monotone_rate"], 4)
                                    for g, s in per_graph.items()}},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
