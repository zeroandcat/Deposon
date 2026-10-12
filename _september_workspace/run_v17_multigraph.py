# -*- coding: utf-8 -*-
# Deposon v1.7.1-E2 多图稳健性（零 API）：固定 17 条 named 语义路径与 9 分支，
# 仅随机化 32 条 filler 挂载（20 张图，种子固定），检验 v1.6/v1.7.1 结论是否依赖单图 filler 排布。
import json, os, time
import numpy as np
from deposon_diffusion import DiffusionConfig, config_dict
from run_v15_experiment import N_NEG, reconstruct_mindmap, row_normalize
from run_v16_llm_prior import prior_score_matrix
from run_v17_fusion_fix import norm_hybrid, raw_hybrid, prior_only
import llm_prior

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
OUT_PATH = os.path.join(RESULTS, "deposon_v17_multigraph.json")
CACHE_PATH = os.path.join(RESULTS, "llm_prior_cache.json")
K_GRAPHS = 20
ARMS = ("field_guided", "random", "degree", "llm_prior",
        "hybrid_raw@0.5", "hybrid_norm@0.5", "hybrid_norm@2.0")


def graph_variant(gi):
    N, adj0, edges0, labels, meta = reconstruct_mindmap()
    named_edges = edges0[:17]                  # 固定语义骨架
    branch_roots = [2, 3, 4, 5, 6, 8, 10, 11, 12]
    rng = np.random.default_rng(550000 + gi)
    edges = list(named_edges)
    for k in range(13, 45):                    # 32 filler 随机挂 9 分支根
        edges.append((int(rng.choice(branch_roots)), k))
    adj = np.zeros((N, N))
    for u, v in edges:
        adj[u, v] = 1.0
    meta = dict(meta); meta["note"] += f"；E2 多图变体 gi={gi}：named 17 边固定，filler 32 边随机重挂"
    return N, adj, edges, labels, meta


def run_graph(cfg, adj, edges, named, P, N):
    from run_v15_experiment import arm_scores, top3_hit_per_edge
    W_true = row_normalize(adj)
    hits = {a: [] for a in ARMS}
    hits_named = {a: [] for a in ARMS}
    for ei, (u, v) in enumerate(edges):
        rng = np.random.default_rng(70_000 + ei)
        adj_obs = adj.copy(); adj_obs[u, v] = 0.0
        W_obs = W_true.copy(); W_obs[u, v] = 0.0
        mask = np.zeros((N, N), bool); mask[u, v] = True
        pool = [j for j in range(N) if j != u and adj_obs[u, j] == 0]
        take = rng.choice(len(pool), size=min(N_NEG, len(pool)), replace=False)
        for k in take:
            mask[u, pool[k]] = True
        sc = {"field_guided": arm_scores("field_guided", W_obs, mask, cfg, 0, 1,
                                         adj_obs, rng, inst_seed=70_000 + ei),
              "random": arm_scores("random", W_obs, mask, cfg, 0, 1, adj_obs, rng,
                                   inst_seed=70_000 + ei),
              "degree": arm_scores("degree", W_obs, mask, cfg, 0, 1, adj_obs, rng,
                                   inst_seed=70_000 + ei)}
        if P is not None:
            tie = rng.random(int(mask.sum()))
            sc["llm_prior"] = prior_only(P, mask, tie)
            sc["hybrid_raw@0.5"] = raw_hybrid(sc["field_guided"], P, mask, 0.5)
            sc["hybrid_norm@0.5"] = norm_hybrid(sc["field_guided"], P, mask, 0.5, tie)
            sc["hybrid_norm@2.0"] = norm_hybrid(sc["field_guided"], P, mask, 2.0, tie)
        for a in ARMS:
            if a not in sc:
                continue
            h = top3_hit_per_edge(sc[a], [(u, v)], mask)[0]["hit"]
            hits[a].append(float(h))
            if (u, v) in named:
                hits_named[a].append(float(h))
    return {a: {"overall": float(np.mean(hits[a])), "named": float(np.mean(hits_named[a]))}
            for a in ARMS if a in hits}


def main():
    t0 = time.time()
    cfg = DiffusionConfig()
    N0, _a, _e, labels, _m = reconstruct_mindmap()
    prior = llm_prior.load_prior(CACHE_PATH) if os.path.exists(CACHE_PATH) else None
    P = prior_score_matrix(prior, (N0, N0)) if prior is not None else None
    graphs = []
    for gi in range(K_GRAPHS):
        N, adj, edges, _labels, meta = graph_variant(gi)
        named = {tuple(e) for e in edges[:17]}
        graphs.append({"gi": gi, "arms": run_graph(cfg, adj, edges, named, P, N)})
    summary = {}
    for a in ARMS:
        if a not in graphs[0]["arms"]:
            continue
        ov = np.array([g["arms"][a]["overall"] for g in graphs])
        nm = np.array([g["arms"][a]["named"] for g in graphs])
        summary[a] = {"overall_mean": float(ov.mean()), "overall_sd_graphs": float(ov.std()),
                      "named_mean": float(nm.mean()), "named_sd_graphs": float(nm.std()),
                      "k_graphs": K_GRAPHS}
    out = {"experiment": "deposon_v17_multigraph", "spec_version": "v1.7.1-E2",
           "config": config_dict(cfg), "k_graphs": K_GRAPHS,
           "protocol": {"named_skeleton": "17 条 named 边固定（同 reconstruct_mindmap 前 17 边）",
                        "filler_randomization": "32 filler 节点随机挂 9 分支根，seed=550000+gi",
                        "loo": "每图 49 边留一，同种子 70000+ei，N_NEG=10，top-3"},
           "llm_prior": {"source": "cache" if prior is not None else "missing",
                         "n_prior_edges": len(prior) if prior else 0},
           "summary_graph_level": summary, "graphs": graphs,
           "runtime_sec": round(time.time() - t0, 3),
           "honesty": ["零 API；先验缓存复用；filler 重挂为 synthetic 稳健性对照，不冒充新真实脑图。",
                       "named 语义骨架跨图固定，因此本实验检验的是 filler 排布/单图依赖，而非新语义分布。"]}
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({"out": OUT_PATH, "runtime_sec": out["runtime_sec"], "summary": summary},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
