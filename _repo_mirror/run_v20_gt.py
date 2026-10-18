# -*- coding: utf-8 -*-
# Deposon v2.0 博弈论首批 GT-1 / GT-4（docs/SPEC_v2.0.md §3，预登记冻结）
#   → results/deposon_v20_gt.json
#
# GT-1 势博弈收敛：S6 锚点图上随机抽 10 条 named 留一边（全候选协议，
#   E9.2 口径），噪声反向（dirichlet，T=20 个独立运行）vs 确定性反向
#   （mean-field）的命中率差与收敛分布。判定（冻结）：dirichlet 命中率均值
#   < mean-field − 0.2 且 20 运行中 ≥15 劣于 mean-field → 支持势博弈框架；
#   否则 GT-1 判死。
# GT-4 无政府代价（PoA）：每张图上 PoA = field_mean named Hits@3 /
#   max(greedy 自利臂 named Hits@3)，自利臂 = {random, degree, llm_prior}
#   （llm_prior 族 S 不可得——no LLM API calls issued，自利集如实退化为
#   {random, degree} 并披露）。判定（冻结）：全图 median PoA > 1.2 → 场有
#   协调价值；median PoA ≤ 1.05 → GT-4 判死；区间 (1.05, 1.2] 预登记未定义，
#   如实报 inconclusive。
# 判定规则抽为纯函数 gt1_verdict / gt4_verdict，tests/test_v20.py 重算锁定。
import json
import os
import time

import numpy as np

from deposon_diffusion import DiffusionConfig, config_dict
from mindmap_corpus_v20 import CORPUS_DIR, load_corpus
from run_v15_experiment import row_normalize
from run_v19_fullrank import full_candidate_mask, gold_rank
from run_v19_meanfield import field_scores_init

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
EVAL_PATH = os.path.join(RESULTS, "deposon_v20_corpus_eval.json")
OUT_PATH = os.path.join(RESULTS, "deposon_v20_gt.json")
GT1_GRAPH = "S6"
GT1_N_EDGES = 10
GT1_RUNS = 20
GT1_SAMPLE_SEED = 777
GT1_SEED_BASE = 300_000
GT1_MARGIN = 0.2          # dirichlet 均值 < mean-field − 0.2（冻结）
GT1_MIN_LOSERS = 15       # 且 ≥15/20 运行劣于 mean-field（冻结）
GT4_PASS = 1.2            # median PoA > 1.2 → 场有协调价值（冻结）
GT4_DEAD = 1.05           # median PoA ≤ 1.05 → GT-4 判死（冻结）
SELFISH_ARMS_AVAILABLE = ("random", "degree")   # llm_prior 族 S 不可得（披露）


# ---------------------------------------------------------------- 判定规则（冻结）
def gt1_verdict(dirichlet_rates, meanfield_rate,
                margin=GT1_MARGIN, min_losers=GT1_MIN_LOSERS):
    """GT-1 冻结判定：dirichlet 命中率均值 < mean-field − margin 且
    ≥min_losers 个运行严格劣于 mean-field → 支持势博弈框架；否则判死。"""
    rates = [float(r) for r in dirichlet_rates]
    mean_rate = float(np.mean(rates)) if rates else None
    n_losers = int(sum(r < meanfield_rate for r in rates))
    supported = bool(mean_rate is not None
                     and mean_rate < meanfield_rate - margin
                     and n_losers >= min_losers)
    return {"supported_potential_game": supported,
            "verdict": ("supports_potential_game_framework"
                        if supported else "GT1_dead"),
            "dirichlet_mean_rate": mean_rate,
            "meanfield_rate": float(meanfield_rate),
            "gap_meanfield_minus_dirichlet_mean": (
                None if mean_rate is None else float(meanfield_rate - mean_rate)),
            "n_runs_below_meanfield": n_losers, "n_runs": len(rates),
            "margin": margin, "min_losers": min_losers}


def gt4_verdict(poa_per_graph: dict, pass_thr=GT4_PASS, dead_thr=GT4_DEAD):
    """GT-4 冻结判定：median PoA > pass_thr → 协调价值；≤ dead_thr → 判死；
    中间带预登记未定义 → inconclusive。PoA=inf（自利臂为 0 而场 >0）与
    undefined（两者皆 0）单独计数，不进入 median（如实披露）。"""
    finite = {g: float(p) for g, p in poa_per_graph.items()
              if p is not None and np.isfinite(p)}
    n_inf = int(sum(1 for p in poa_per_graph.values()
                    if p is not None and not np.isfinite(p)))
    n_undef = int(sum(1 for p in poa_per_graph.values() if p is None))
    med = float(np.median(list(finite.values()))) if finite else None
    if med is None:
        verdict = "undefined_no_finite_poa"
    elif med > pass_thr:
        verdict = "field_coordination_value_supported"
    elif med <= dead_thr:
        verdict = "GT4_dead"
    else:
        verdict = "inconclusive_band_(1.05,1.2]_preregistered_undefined"
    return {"verdict": verdict, "median_poa": med,
            "poa_per_graph_finite": finite, "n_poa_inf": n_inf,
            "n_poa_undefined": n_undef,
            "pass_threshold": pass_thr, "dead_threshold": dead_thr}


# ---------------------------------------------------------------- GT-1
def run_gt1(cfg):
    graphs = {g["graph_id"]: g for g in load_corpus(CORPUS_DIR, families=("S",))}
    if GT1_GRAPH not in graphs:
        raise RuntimeError(f"corpus missing {GT1_GRAPH} — 先运行 mindmap_corpus_v20.py")
    g = graphs[GT1_GRAPH]
    N = g["N"]
    edges = [tuple(e) for e in g["edges"]]
    named = [tuple(e) for e in g["named_edges"]]
    adj = np.zeros((N, N))
    for (u, v) in edges:
        adj[u, v] = 1.0
    W_true = row_normalize(adj)
    rng_pick = np.random.default_rng(GT1_SAMPLE_SEED)
    take = rng_pick.choice(len(named), size=GT1_N_EDGES, replace=False)
    tasks = [named[int(k)] for k in take]
    src, tgt = g["source"], g["target"]

    def hit_rate(init_mode, run=None):
        hits = []
        for k, (u, v) in enumerate(tasks):
            adj_obs = adj.copy()
            adj_obs[u, v] = 0.0
            W_obs = W_true.copy()
            W_obs[u, v] = 0.0
            mask = full_candidate_mask(N, u)
            cand = np.flatnonzero(mask[u])
            seed = (GT1_SEED_BASE + k if run is None
                    else GT1_SEED_BASE + run * 1000 + k)
            srow = field_scores_init(W_obs, mask, cfg, src, tgt, seed,
                                     init_mode)[u]
            hits.append(float(gold_rank(srow, cand, v) < 3))
        return float(np.mean(hits))

    meanfield_rate = hit_rate("prior_mean")  # 确定性极限（单次）
    dirichlet_rates = [hit_rate("dirichlet", run=r) for r in range(GT1_RUNS)]
    return {"graph": GT1_GRAPH, "n_tasks": GT1_N_EDGES,
            "task_edges": [[int(u), int(v)] for (u, v) in tasks],
            "sample_seed": GT1_SAMPLE_SEED,
            "protocol": "同一批 named 留一任务（全候选 E9.2 口径）；"
                        "dirichlet inst_seed=300000+run*1000+k，T=20 独立运行；"
                        "mean-field 为确定性极限（与 seed 无关，单次）",
            "meanfield_named_hits3": meanfield_rate,
            "dirichlet_named_hits3_per_run": dirichlet_rates,
            "verdict": gt1_verdict(dirichlet_rates, meanfield_rate)}


# ---------------------------------------------------------------- GT-4
def run_gt4():
    if not os.path.exists(EVAL_PATH):
        raise RuntimeError(f"missing {EVAL_PATH} — 先运行 run_v20_corpus_eval.py")
    ev = json.load(open(EVAL_PATH, encoding="utf-8"))
    named = ev["graph_level"]["named_hits3"]
    poa = {}
    for gid, arms in named.items():
        fm = arms["field_mean"]
        selfish = max(float(arms[a]) for a in SELFISH_ARMS_AVAILABLE)
        if fm is None:
            poa[gid] = None
        elif selfish > 0.0:
            poa[gid] = float(fm) / selfish
        else:
            poa[gid] = float("inf") if fm > 0.0 else None
    verdict = gt4_verdict(poa)
    poa_json = {g: (None if p is None else ("Infinity" if not np.isfinite(p)
                                            else float(p)))
                for g, p in poa.items()}
    return {"selfish_arms": list(SELFISH_ARMS_AVAILABLE),
            "selfish_arms_preregistered": ["random", "degree", "llm_prior"],
            "deviation": ("llm_prior 族 S 不可得（no LLM API calls issued，"
                          "SPEC §1：先验臂在族 L 才主报）⇒ 自利集退化为 "
                          "{random, degree}，如实披露"),
            "poa_per_graph": poa_json, "verdict": verdict,
            "note": "PoA=Infinity：自利臂 named=0 而 field_mean>0（场相对自利"
                    "臂无穷协调价值，不进入 median，单独计数）"}


def main():
    t0 = time.time()
    cfg = DiffusionConfig()
    gt1 = run_gt1(cfg)
    gt4 = run_gt4()
    out = {"experiment": "deposon_v20_gt", "spec_version": "v2.0",
           "spec": "docs/SPEC_v2.0.md §3（GT-1 / GT-4，先于族 L 完成）",
           "config": config_dict(cfg),
           "GT1_potential_game_convergence": gt1,
           "GT4_price_of_anarchy": gt4,
           "runtime_sec": round(time.time() - t0, 3),
           "honesty": [
               "no LLM API calls issued: GT-1/GT-4 全部本地确定性/种子化运行。",
               "GT-1 判定规则机械求值：dirichlet 均值 < mean-field − 0.2 且 "
               "≥15/20 运行劣于 mean-field → 支持势博弈框架；否则判死。",
               "GT-4 自利集退化：llm_prior 族 S 不可得，按 {random, degree} 计 "
               "PoA，相对预登记自利集为弱化口径（分母只可能更小 ⇒ PoA 只可能"
               "偏大），结论方向性如实披露。",
               "median PoA 落在 (1.05, 1.2] 区间时预登记未定义，报 inconclusive，"
               "不向任一方向美化。",
               "阴性结果如实写入 verdict，不美化。"]}
    os.makedirs(RESULTS, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({"out": OUT_PATH, "runtime_sec": out["runtime_sec"],
                      "GT1": gt1["verdict"], "GT4": gt4["verdict"]},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
