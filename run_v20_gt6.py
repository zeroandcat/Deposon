# -*- coding: utf-8 -*-
# Deposon v2.0 博弈论 GT-6：Candogan 流分解——非势残余量化
#   → results/deposon_v20_gt6.json
#
# 思想来源：reviews/literature_scan_v2X_A.md 锚点 1-7（Candogan, Menache,
# Ozdaglar, Parrilo 2011, MOR 36(3):474–503）「博弈 = 图上势流 + 调和流」的
# 分解语言；docs/GT_RECONSTRUCTION.md §5 下一步第 2 条（零 API，可立即做）。
#
# 可操作性分解（冻结）：
#   对每图每条 named 留一任务（观测图 W_obs），取反向退火场引导的边效用向量
#       F_e = (x[u]·y[v]/x_t)·dt_e/dW   （e=(u,v) 遍历 W_obs 支持集上的边）
#   即 scatter_energy(aggregate) 梯度中「场」分量本身（与 reverse_denoise 逐行
#   一致，见 deposon_diffusion._walk_sums 口径；平滑分量 -2·lam·W 恒为
#   「自身指向」的节点独立项，天然属于势/梯度分量，不计入非势残余——披露）。
#   图 Hodge 分解：把 F 视为有向图 1-流，投影到梯度空间
#       grad = argmin_{p∈R^N} ||F - B p||²,  (B p)_e = p_u - p_v
#   （B 为 |E|×N 有向关联矩阵；最小二乘解 p = pinv(B) F）
#       势分量 = B p（可由节点势函数解释的部分）
#       非势残余 = F − B p（循环/调和流，Candogan 口径的 non-strategic/harmonic 残余）
#   残余能量占比 r = ||非势残余||² / ||F||²（逐任务；图级取任务均值，同时报中位数）。
#
# 判定（预登记，机械求值，见 gt6_verdict）：
#   22 图（图级均值 r）的中位数 < 0.10 ⇒ 势博弈解释「完备」；
#   中位数 > 0.30 ⇒ 降级为「近似势博弈」；
#   之间 ⇒ 如实报区间 inconclusive（不美化）。
#
# 零 LLM API；deposon_diffusion.py 一行不动（边效用向量用其公开/内部函数
# 只读计算）。
import json
import os
import time

import numpy as np

from deposon_diffusion import (DiffusionConfig, config_dict, _walk_sums,
                               _edge_transmittance, _G_AETHER, _EPS)
from mindmap_corpus_v20 import CORPUS_DIR, load_corpus
from run_v15_experiment import row_normalize

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
OUT_PATH = os.path.join(RESULTS, "deposon_v20_gt6.json")

# ------------------------------------------------------------ 预登记冻结常量
GT6_TASKS_PER_GRAPH = 10        # 每图 ≤10 任务（与 GT-5b 同口径，披露）
GT6_SAMPLE_SEED = 606_000       # 抽样种子（+图序）
GT6_COMPLETE_MEDIAN = 0.10      # 图级均值 r 的中位数 < 0.10 ⇒ 完备
GT6_APPROX_MEDIAN = 0.30        # 中位数 > 0.30 ⇒ 降级为近似势博弈
ENERGY_MODE = "aggregate"


def edge_utility_vector(W_obs, source, target):
    """场引导边效用向量 F 与边列表。

    F_e = (x[u]·y[v]/x_t)·dt_e/dW（reverse_denoise 场引导梯度分量的相反数；
    符号不影响投影分解的残余占比，取与梯度下降方向一致的符号便于解读）。
    只含 W_obs>0 的边（含 filler 与未留出的 named；留出任务边不在支持集）。
    """
    W = np.asarray(W_obs, dtype=float)
    x, y = _walk_sums(W, source, target)
    xt = max(float(x[target]), _EPS)
    wpos = np.maximum(W, _EPS)
    dtdw = np.where(W > _EPS, 1.0 / (1.0 + _G_AETHER * wpos) ** 2, 0.0)
    score = (x[:, None] * y[None, :]) * (dtdw / xt)
    us, vs = np.nonzero(W > 0.0)
    F = score[us, vs]
    return [ (int(u), int(v)) for u, v in zip(us, vs) ], np.asarray(F, float)


def hodge_decomposition(N, edges, F):
    """图 Hodge 分解：F = 势(梯度)分量 + 非势(循环/调和)残余。

    返回 (residual_ratio r, ||grad||², ||resid||², ||F||²)。
    F 全零时 r 定义为 0.0（无非势残余可言，披露于 honesty）。
    """
    F = np.asarray(F, dtype=float)
    E = len(edges)
    B = np.zeros((E, N))
    for k, (u, v) in enumerate(edges):
        B[k, u] = 1.0
        B[k, v] = -1.0
    p = np.linalg.pinv(B) @ F
    grad = B @ p
    resid = F - grad
    total = float(F @ F)
    r = float(resid @ resid) / total if total > 0.0 else 0.0
    return r, float(grad @ grad), float(resid @ resid), total


# ------------------------------------------------------------ 判定规则（冻结）
def gt6_verdict(per_graph, complete_median=GT6_COMPLETE_MEDIAN,
                approx_median=GT6_APPROX_MEDIAN):
    """GT-6 冻结判定（机械求值，纯函数，tests/test_v20_gt6.py 锁定）：

    per_graph: {gid: {"residual_ratio_mean": float}}
    中位数 < complete_median ⇒ potential_game_explanation_complete；
    中位数 > approx_median ⇒ downgraded_to_approximate_potential_game；
    之间 ⇒ inconclusive_band_reported_as_is。
    """
    vals = [per_graph[g]["residual_ratio_mean"] for g in per_graph]
    med = float(np.median(vals)) if vals else None
    if med is not None and med < complete_median:
        verdict = "potential_game_explanation_complete"
    elif med is not None and med > approx_median:
        verdict = "downgraded_to_approximate_potential_game"
    else:
        verdict = "inconclusive_band_reported_as_is"
    return {"verdict": verdict,
            "median_residual_ratio": med,
            "n_graphs": len(vals),
            "thresholds": {"complete_median": complete_median,
                           "approx_median": approx_median}}


# ------------------------------------------------------------ 实验主体
def run_graph(g, cfg, n_tasks=GT6_TASKS_PER_GRAPH, graph_ord=0):
    """单图：逐任务构造边效用向量并做 Hodge 分解。"""
    N = g["N"]
    src, tgt = g["source"], g["target"]
    adj = np.zeros((N, N))
    for (u, v) in g["edges"]:
        adj[u, v] = 1.0
    W_true = row_normalize(adj)
    named = [tuple(e) for e in g["named_edges"]]
    rng = np.random.default_rng(GT6_SAMPLE_SEED + graph_ord)
    take = rng.choice(len(named), size=min(n_tasks, len(named)), replace=False)
    tasks = [named[int(k)] for k in sorted(take.tolist())]
    rs, per_task = [], []
    for (u, v) in tasks:
        W_obs = W_true.copy()
        W_obs[u, v] = 0.0
        edges, F = edge_utility_vector(W_obs, src, tgt)
        r, g2, r2, tot = hodge_decomposition(N, edges, F)
        rs.append(r)
        per_task.append({"task_edge": [int(u), int(v)],
                         "n_edges_in_flow": len(edges),
                         "residual_ratio": r,
                         "grad_energy": g2, "resid_energy": r2,
                         "total_energy": tot})
    summary = {"residual_ratio_mean": float(np.mean(rs)),
               "residual_ratio_median": float(np.median(rs)),
               "residual_ratio_max": float(np.max(rs)),
               "residual_ratio_min": float(np.min(rs))}
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
    verdict = gt6_verdict(per_graph)
    runtime = round(time.time() - t0, 3)
    out = {"experiment": "deposon_v20_gt6", "spec_version": "v2.0",
           "spec": ("docs/GT_RECONSTRUCTION.md §5 下一步第 2 条；Candogan et al. "
                    "2011（reviews/literature_scan_v2X_A.md 锚点 1-7）流分解："
                    "博弈 = 势流 + 循环/调和流，量化非势残余占比"),
           "config": config_dict(cfg),
           "decomposition": {
               "flow_definition": ("F_e = (x[u]·y[v]/x_t)·dt_e/dW（反向退火场引导"
                                   "梯度的场分量本身，aggregate 口径）"),
               "gradient_space": ("有向关联矩阵 B 的列空间：(Bp)_e = p_u − p_v，"
                                  "最小二乘投影 p = pinv(B)F"),
               "residual": "非势残余 = F − B·pinv(B)·F（循环/调和流）",
               "residual_ratio": "r = ||残余||² / ||F||²",
               "note": ("平滑分量 -2·lam·W 为节点独立自指项，天然属势分量，不计入"
                        "非势残余；F 全零时 r 定义为 0.0（本语料未出现）")},
           "preregistered": {
               "graphs": "全部 22 图（族 S 16 + 族 L 6）",
               "tasks_per_graph_max": GT6_TASKS_PER_GRAPH,
               "sample_seed": GT6_SAMPLE_SEED,
               "pass_rule": (f"图级均值 r 的中位数 < {GT6_COMPLETE_MEDIAN} ⇒ "
                             "potential_game_explanation_complete"),
               "downgrade_rule": (f"中位数 > {GT6_APPROX_MEDIAN} ⇒ "
                                  "downgraded_to_approximate_potential_game"),
               "band_rule": "之间 ⇒ inconclusive_band_reported_as_is，如实报区间"},
           "per_graph_summary": per_graph,
           "per_graph_detail": details,
           "verdict": verdict,
           "runtime_sec": runtime,
           "honesty": [
               "no LLM API calls issued: 全语料从 corpus/v20 只读加载，全部"
               "实验为本地种子化 numpy 线性代数运算。",
               "本分解是 Candogan 2011 博弈流分解的**可操作性类比**：原定理分解"
               "的是效用函数空间，这里分解的是图上边效用（场得分）向量——"
               "「每个任务是独立玩家」的博弈构造是建模选择（docs/GT_RECONSTRUCTION.md"
               " §3 已披露），非唯一。",
               "边效用取 W_obs（留一后、正向扩散前）上的静态场得分；未沿反向"
               "轨迹积分——轨迹依赖的分解留作后续工作，不混入本次预登记判定。",
               "判定规则为纯函数 gt6_verdict 机械求值，tests/test_v20_gt6.py "
               "锁定；落在中报区间时报 inconclusive_band_reported_as_is，不美化。",
               "deposon_diffusion.py / run_v20_gt5.py 等既有文件一行不动；"
               "本文件为新建。",
               f"总运行 {runtime}s（预算 600s 内）"
               if runtime <= 600 else
               f"总运行 {runtime}s 超预算，如实披露。"]}
    os.makedirs(RESULTS, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({"out": OUT_PATH, "runtime_sec": runtime,
                      "verdict": verdict["verdict"],
                      "median_residual_ratio": verdict["median_residual_ratio"],
                      "per_graph": {g: round(s["residual_ratio_mean"], 4)
                                    for g, s in per_graph.items()}},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
