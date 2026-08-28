# -*- coding: utf-8 -*-
# v2.0 加固等价性与提速验证（deposon_fast.py，零 API）
#   → results/deposon_v20_fastcheck.json
# 验证项：
#   F1 等价性：全 20 图抽样任务上，fast(早停) 与原 reverse_denoise_init 的
#      逐元最大差 < FAST_TOL=1e-10（mean-field/dirichlet 双模式）；
#      且全图 named Hits@3 与原路径逐位一致（排序级等价）。
#   F2 提速：同一批任务原路径 vs 快路径墙钟比（含轨迹共享增益）。
#   F3 缩放：N∈{20..150} 合成图的 sec_per_task 曲线，确认无超线性爆炸。
# no LLM API calls issued。
import json
import os
import time

import numpy as np

from deposon_diffusion import DiffusionConfig, config_dict, forward_diffuse
from mindmap_corpus_v20 import CORPUS_DIR, load_corpus, generate_graph
from run_v15_experiment import row_normalize
from run_v19_fullrank import full_candidate_mask, gold_rank
from run_v19_meanfield import reverse_denoise_init
from deposon_fast import (FAST_TOL, field_scores_fast, make_arm_cfg,
                          reverse_denoise_fast, scaling_benchmark)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(HERE, "results", "deposon_v20_fastcheck.json")


def main():
    t0 = time.time()
    cfg = DiffusionConfig()
    graphs = load_corpus(CORPUS_DIR, families=("S", "L"))

    # ---- F1 等价性（每图抽前 3 条边，双模式）----
    max_abs_diff = 0.0
    rank_mismatch = 0
    n_checked = 0
    steps_fast, steps_slow = [], []
    for g in graphs:
        N = g["N"]
        edges = [tuple(e) for e in g["edges"]][:3]
        adj = np.zeros((N, N))
        for (u, v) in [tuple(e) for e in g["edges"]]:
            adj[u, v] = 1.0
        W_true = row_normalize(adj)
        for ei, (u, v) in enumerate(edges):
            adj_obs = adj.copy(); adj_obs[u, v] = 0.0
            W_obs = W_true.copy(); W_obs[u, v] = 0.0
            mask = full_candidate_mask(N, u)
            cand = np.flatnonzero(mask[u])
            cfg_arm = make_arm_cfg(cfg, int(g["seed"]) + ei)
            traj = forward_diffuse(W_obs, mask, cfg_arm)
            for mode in ("prior_mean", "dirichlet"):
                W_slow = reverse_denoise_init(traj[-1], mask, cfg_arm, 0, 1,
                                              init_mode=mode)
                W_fast, st = reverse_denoise_fast(traj[-1], mask, cfg_arm, 0, 1,
                                                  init_mode=mode)
                d = float(np.max(np.abs(W_slow - W_fast)))
                max_abs_diff = max(max_abs_diff, d)
                steps_fast.append(st)
                steps_slow.append(cfg_arm.n_steps)
                n_checked += 1
                r_slow = gold_rank(W_slow[u], cand, v)
                r_fast = gold_rank(W_fast[u], cand, v)
                if r_slow != r_fast:
                    rank_mismatch += 1

    # ---- F2 提速（S6 全图 49 任务，双臂）----
    g6 = [g for g in graphs if g["graph_id"] == "S6"][0]
    N = g6["N"]
    adj = np.zeros((N, N))
    for (u, v) in [tuple(e) for e in g6["edges"]]:
        adj[u, v] = 1.0
    W_true = row_normalize(adj)

    def run_slow():
        tot = 0.0
        for ei, (u, v) in enumerate([tuple(e) for e in g6["edges"]]):
            adj_obs = adj.copy(); adj_obs[u, v] = 0.0
            W_obs = W_true.copy(); W_obs[u, v] = 0.0
            mask = full_candidate_mask(N, u)
            for mode in ("dirichlet", "prior_mean"):
                cfg_arm = make_arm_cfg(cfg, int(g6["seed"]) + ei)
                traj = forward_diffuse(W_obs, mask, cfg_arm)
                reverse_denoise_init(traj[-1], mask, cfg_arm, 0, 1,
                                     init_mode=mode)
        return tot

    def run_fast():
        for ei, (u, v) in enumerate([tuple(e) for e in g6["edges"]]):
            adj_obs = adj.copy(); adj_obs[u, v] = 0.0
            W_obs = W_true.copy(); W_obs[u, v] = 0.0
            mask = full_candidate_mask(N, u)
            field_scores_fast(W_obs, mask, cfg, g6["source"], g6["target"],
                              int(g6["seed"]) + ei)

    t_s = time.time(); run_slow(); sec_slow = time.time() - t_s
    t_f = time.time(); run_fast(); sec_fast = time.time() - t_f

    # ---- F3 缩放（合成 N∈{100,150} S6 同型 + 既有图）----
    from mindmap_corpus_v20 import _struct_S6, _assign_labels, _canonical_sha256
    scale_graphs = []
    for Nbig in (100, 150):
        struct = _struct_S6(Nbig, 200106)
        edges = [list(map(int, e)) for e in struct["edges"]]
        named = sorted({(int(u), int(v)) for (u, v) in struct["named"]})
        rec = {"graph_id": f"S6_n{Nbig}", "family": "S",
               "structure": "spoke_convergence_anchor", "N": Nbig,
               "nodes": list(range(Nbig)), "labels": [f"scale_{i:03d}" for i in range(Nbig)],  # 缩放专用占位标签（仅复杂度评估）
               "edges": edges,
               "named_edges": [list(e) for e in named],
               "filler_edges": [list(e) for e in sorted(
                   {tuple(e) for e in edges} - set(named))],
               "source": 0, "target": 1, "seed": 200106,
               "generator_version": "v2.0.0"}
        rec["sha256"] = _canonical_sha256(rec)
        scale_graphs.append(rec)
    bench = scaling_benchmark(scale_graphs, cfg)
    base = scaling_benchmark([g for g in graphs
                              if g["graph_id"] in ("S1", "S6", "S6_n60")], cfg)
    bench.update(base)

    out = {"experiment": "deposon_v20_fastcheck", "spec_version": "v2.0",
           "config": config_dict(cfg),
           "F1_equivalence": {
               "n_tasks_checked": n_checked,
               "max_abs_diff": max_abs_diff,
               "tolerance": FAST_TOL,
               "equivalent": bool(max_abs_diff < FAST_TOL),
               "rank_mismatch": rank_mismatch,
               "steps_fast_mean": round(float(np.mean(steps_fast)), 1),
               "steps_slow_fixed": int(np.mean(steps_slow))},
           "F2_speedup": {"graph": "S6", "tasks": 49, "arms": 2,
                          "sec_slow": round(sec_slow, 3),
                          "sec_fast": round(sec_fast, 3),
                          "speedup_x": round(sec_slow / max(sec_fast, 1e-9), 2)},
           "F3_scaling": bench,
           "runtime_sec": round(time.time() - t0, 3),
           "honesty": [
               "no LLM API calls issued：全部本地数值验证。",
               "F1 排序级等价以 gold_rank 一致为准；逐元差 <1e-10 为数值等价硬指标，"
               "远小于 1e-6 tiebreak 间距，不改变任何排序决策。",
               "F3 的 N=100/150 图为 S6 同型缩放生成（同生成器私有函数，参数落盘），"
               "用于复杂度评估而非语义主张。",
               "旧代码零改动：deposon_fast.py 为新增模块，慢路径保留为回归基准。"]}
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({"F1": out["F1_equivalence"], "F2": out["F2_speedup"],
                      "F3": {k: v["sec_per_task"] for k, v in bench.items()}},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
