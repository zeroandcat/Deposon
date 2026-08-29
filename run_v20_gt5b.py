# -*- coding: utf-8 -*-
# Deposon v2.0 博弈论 GT-5b：全语料 mean-field 势函数单调性复核 + 主张收窄预登记
#   → results/deposon_v20_gt5b.json
#
# 背景（docs/GT_RECONSTRUCTION.md §2 纪律声明）：GT-5 的终点条件已按预登记
# 判 inconclusive，不可回溯改写。本实验是**新版预登记**（先于本实验任何数据
# 产生，冻结于本文件常量）：主张收窄为
#     「mean-field 反向动态的势函数轨迹单调不减」
# 不再含终点条件（dirichlet 臂不运行——收窄后主张不涉及它，而非隐藏它；
# GT-5 的终点反转已在 docs/GT_RECONSTRUCTION.md §2 如实披露）。
#
# 图集 = 全部 22 图（族 S 16 + 族 L 6，corpus/v20 只读加载，零 API）。
# 每图 GT5B_TASKS_PER_GRAPH=10 条 named 留一任务（降采样控制算力，种子
# GT5B_SAMPLE_SEED+图序；named 边不足 10 的图全取并披露）。
#
# 判定（预登记，机械求值，见 gt5b_verdict）：
#   支持：mean-field Φ 单调率 = 100% 的图占比 ≥ 80% ⇒ 支持收窄后主张；
#   斩杀线 H_GT5b_dead：单调率 < 50% 的图 ≥ 3 张 ⇒ 收窄后主张判死；
#   其余：inconclusive（预登记未定义区间，如实报）。
#
# 零 LLM API；复用 run_v20_gt5.py 的 Φ 定义/轨迹记录/单调率函数（只读 import，
# 既有文件一行不动）。
import json
import os
import time

import numpy as np

from deposon_diffusion import DiffusionConfig, config_dict, forward_diffuse
from mindmap_corpus_v20 import CORPUS_DIR, load_corpus
from run_v15_experiment import row_normalize
from run_v19_fullrank import full_candidate_mask
from run_v20_gt5 import (ENERGY_MODE, GT5_TOL, monotone_rate, phi_trajectory,
                         reverse_denoise_traj)

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
OUT_PATH = os.path.join(RESULTS, "deposon_v20_gt5b.json")

# ------------------------------------------------------------ 预登记冻结常量
GT5B_TASKS_PER_GRAPH = 10        # 每图 ≤10 任务（算力降采样，披露）
GT5B_SAMPLE_SEED = 505_500       # 抽样种子（+图序），区别于 GT-5 的 505_000
GT5B_PASS_GRAPH_FRAC = 0.8       # 单调率=100% 的图占比 ≥ 0.8 ⇒ 支持
GT5B_MONO_FULL = 1.0             # 「单调率=100%」满分线
GT5B_MONO_DEAD = 0.5             # 单调率 < 50% 计为判死图
GT5B_DEAD_MIN_GRAPHS = 3         # 判死图 ≥ 3 ⇒ H_GT5b_dead


# ------------------------------------------------------------ 判定规则（冻结）
def gt5b_verdict(per_graph, pass_frac=GT5B_PASS_GRAPH_FRAC,
                 mono_full=GT5B_MONO_FULL, mono_dead=GT5B_MONO_DEAD,
                 dead_min_graphs=GT5B_DEAD_MIN_GRAPHS):
    """GT-5b 冻结判定（机械求值，纯函数，tests/test_v20_gt5b.py 锁定）：

    per_graph: {gid: {"meanfield_monotone_rate": float}}
    支持：单调率=100% 的图占比 ≥ pass_frac ⇒ supports_narrowed_monotonicity；
    斩杀：单调率 < 50% 的图 ≥ dead_min_graphs ⇒ H_GT5b_dead；
    其余：inconclusive_preregistered_undefined_band。
    """
    gids = list(per_graph)
    n = len(gids)
    full_mono = [g for g in gids
                 if per_graph[g]["meanfield_monotone_rate"] >= mono_full]
    dead_graphs = [g for g in gids
                   if per_graph[g]["meanfield_monotone_rate"] < mono_dead]
    frac_full = (len(full_mono) / n) if n else None
    if len(dead_graphs) >= dead_min_graphs:
        verdict = "H_GT5b_dead"
    elif frac_full is not None and frac_full >= pass_frac:
        verdict = "supports_narrowed_monotonicity"
    else:
        verdict = "inconclusive_preregistered_undefined_band"
    return {"verdict": verdict,
            "supported_narrowed_claim": bool(
                verdict == "supports_narrowed_monotonicity"),
            "graphs_with_full_monotonicity": full_mono,
            "frac_graphs_full_monotonicity": frac_full,
            "graphs_below_50pct_monotonicity": dead_graphs,
            "n_graphs": n,
            "thresholds": {"pass_graph_frac": pass_frac,
                           "mono_full": mono_full, "mono_dead": mono_dead,
                           "dead_min_graphs": dead_min_graphs,
                           "tol": GT5_TOL}}


# ------------------------------------------------------------ 实验主体
def run_graph(g, cfg, n_tasks=GT5B_TASKS_PER_GRAPH, graph_ord=0):
    """单图：逐任务 mean-field 反向，逐点记录 Φ（仅 mean-field 臂）。"""
    N = g["N"]
    src, tgt = g["source"], g["target"]
    adj = np.zeros((N, N))
    for (u, v) in g["edges"]:
        adj[u, v] = 1.0
    W_true = row_normalize(adj)
    named = [tuple(e) for e in g["named_edges"]]
    rng = np.random.default_rng(GT5B_SAMPLE_SEED + graph_ord)
    take = rng.choice(len(named), size=min(n_tasks, len(named)), replace=False)
    tasks = [named[int(k)] for k in sorted(take.tolist())]

    mf_rates, mf_endpoints, mf_deltas_min = [], [], []
    per_task = []
    for (u, v) in tasks:
        W_obs = W_true.copy()
        W_obs[u, v] = 0.0
        mask = full_candidate_mask(N, u)
        cfg_arm = DiffusionConfig(**{**config_dict(cfg), "seed": 0,
                                     "energy_mode": ENERGY_MODE,
                                     "field_guidance": True})
        WT = forward_diffuse(W_obs, mask, cfg_arm)[-1]
        states = reverse_denoise_traj(WT, mask, cfg_arm, src, tgt,
                                      init_mode="prior_mean")
        phi = phi_trajectory(states, src, tgt)
        mf_rates.append(monotone_rate(phi))
        mf_endpoints.append(phi[-1])
        mf_deltas_min.append(float(np.min(np.diff(phi)))
                             if len(phi) > 1 else 0.0)
        per_task.append({"task_edge": [int(u), int(v)],
                         "meanfield_monotone_rate": mf_rates[-1],
                         "meanfield_min_step_delta": mf_deltas_min[-1],
                         "meanfield_endpoint_phi": mf_endpoints[-1]})

    summary = {"meanfield_monotone_rate": float(np.mean(mf_rates)),
               "meanfield_min_step_delta": float(np.min(mf_deltas_min)),
               "meanfield_mean_endpoint": float(np.mean(mf_endpoints))}
    return {"graph_id": g["graph_id"], "family": g["family"], "N": int(N),
            "n_named_edges": len(named), "n_tasks": len(tasks),
            "tasks": per_task, "summary": summary}


def main():
    t0 = time.time()
    cfg = DiffusionConfig()
    graphs = load_corpus(CORPUS_DIR, families=("S", "L"))
    per_graph, details = {}, {}
    for ord_, g in enumerate(graphs):
        res = run_graph(g, cfg, graph_ord=ord_)
        details[g["graph_id"]] = res
        per_graph[g["graph_id"]] = res["summary"]
    verdict = gt5b_verdict(per_graph)
    runtime = round(time.time() - t0, 3)
    out = {"experiment": "deposon_v20_gt5b", "spec_version": "v2.0",
           "spec": ("docs/GT_RECONSTRUCTION.md §2/§5：GT-5 终点条件 inconclusive "
                    "不可回溯；本实验为新版预登记，主张收窄为「mean-field 反向动态"
                    "的势函数轨迹单调不减」"),
           "config": config_dict(cfg),
           "preregistered": {
               "graphs": "全部 22 图（族 S 16 + 族 L 6）",
               "tasks_per_graph_max": GT5B_TASKS_PER_GRAPH,
               "sample_seed": GT5B_SAMPLE_SEED,
               "arm": "mean-field only（收窄后主张不涉及 dirichlet 臂）",
               "tol": GT5_TOL,
               "pass_rule": (f"单调率=100% 的图占比 ≥ {GT5B_PASS_GRAPH_FRAC} "
                             "⇒ supports_narrowed_monotonicity"),
               "kill_rule": (f"单调率 < {GT5B_MONO_DEAD} 的图 ≥ "
                             f"{GT5B_DEAD_MIN_GRAPHS} ⇒ H_GT5b_dead，如实宣布")},
           "per_graph_summary": per_graph,
           "per_graph_detail": details,
           "verdict": verdict,
           "runtime_sec": runtime,
           "honesty": [
               "no LLM API calls issued: 全语料从 corpus/v20 只读加载，全部"
               "实验为本地种子化 numpy 运行。",
               "本实验是新版预登记（常量冻结于脚本，先于本实验数据）；GT-5 的"
               "终点条件按原预登记判 inconclusive，未回溯改写；GT-5 的 dirichlet"
               "终点反转（3/4 图噪声臂终点 Φ 更高）继续在 docs/GT_RECONSTRUCTION.md"
               " §2 披露，不因主张收窄而删除。",
               "Φ 定义与 GT-5 逐字相同（Φ=-scatter_energy(aggregate)），函数"
               "经只读 import 复用，未为重跑全语料而改函数。",
               "每图任务数降采样为 ≤10（GT-5 为 5，图数 4→22）；named 边不足"
               "10 的图全取，n_tasks 逐图披露。",
               "判定规则为纯函数 gt5b_verdict 机械求值，tests/test_v20_gt5b.py "
               "锁定；落在预登记未定义区间时报 inconclusive，不美化。",
               "反向动态含向 W_obs 的收缩步与单纯形投影，理论上不保证 Φ 逐步"
               "单调；任何非单调步均计入单调率，不剔除。",
               f"总运行 {runtime}s（预算 600s 内）"
               if runtime <= 600 else
               f"总运行 {runtime}s 超预算，如实披露。"]}
    os.makedirs(RESULTS, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({"out": OUT_PATH, "runtime_sec": runtime,
                      "verdict": verdict["verdict"],
                      "frac_full": verdict["frac_graphs_full_monotonicity"],
                      "per_graph": {g: round(s["meanfield_monotone_rate"], 4)
                                    for g, s in per_graph.items()}},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
