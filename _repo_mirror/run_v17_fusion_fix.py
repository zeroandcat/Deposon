# -*- coding: utf-8 -*-
# Deposon v1.7.1 同协议融合修复 + 零 API 阴性对照 (docs/SPEC_v1.7.1.md)
# 不改 v1.6 留一协议；零 API；null 先验全部标记 synthetic_null，严禁冒充 LLM。
import json, os, time, math
import numpy as np
from deposon_diffusion import DiffusionConfig, config_dict
from run_v15_experiment import (N_NEG, TOP_K, arm_scores, mean_std,
                                reconstruct_mindmap, row_normalize,
                                top3_hit_per_edge)
from run_v16_llm_prior import prior_score_matrix, LAMBDAS
import llm_prior

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
OUT_PATH = os.path.join(RESULTS, "deposon_v17_fusion_fix.json")
CACHE_PATH = os.path.join(RESULTS, "llm_prior_cache.json")
BOOT_SEED, BOOT_B = 12345, 20000
RAND_PRIOR_SEEDS = list(range(5))
BASE_ARMS = ("field_guided", "random", "degree")
RAW_ARMS = tuple(f"hybrid_raw@{lam}" for lam in LAMBDAS)
NORM_ARMS = tuple(f"hybrid_norm@{lam}" for lam in LAMBDAS)
NULL_ARMS = ("llm_prior_confshuffle", "hybrid_norm_confshuffle@0.5") + tuple(
    f"llm_prior_rand{s}" for s in RAND_PRIOR_SEEDS) + tuple(
    f"hybrid_norm_rand{s}@0.5" for s in RAND_PRIOR_SEEDS)


def minmax_mask(vals):
    vals = np.asarray(vals, float)
    lo, hi = float(vals.min()), float(vals.max())
    if hi - lo < 1e-12:
        return np.zeros_like(vals)
    return (vals - lo) / (hi - lo)


def norm_hybrid(fg_scores, P, mask, lam, tiebreak):
    out = np.full(P.shape, -np.inf)
    fgn = minmax_mask(fg_scores[mask])
    prn = minmax_mask(P[mask])
    # 与 random/degree/llm_prior 同口径的确定性微扰破平局：防止 λ→1 或稀疏先验
    # 全零时退化为"按列号稳定排序"的低索引偏置（本轮运行已发现该 artifact）。
    out[mask] = (1.0 - lam) * fgn + lam * prn + 1e-6 * tiebreak
    return out


def raw_hybrid(fg_scores, P, mask, lam):
    out = np.full(P.shape, -np.inf)
    out[mask] = fg_scores[mask] + lam * P[mask]
    return out


def prior_only(P, mask, tiebreak):
    out = np.full(P.shape, -np.inf)
    out[mask] = P[mask] + 1e-6 * tiebreak
    return out


def shuffle_conf_prior(prior, seed):
    rng = np.random.default_rng(seed)
    keys = list(prior.keys())
    vals = np.array([prior[k] for k in keys], float)
    rng.shuffle(vals)
    return {k: float(v) for k, v in zip(keys, vals)}


def random_edge_prior(N, confs, seed):
    rng = np.random.default_rng(910000 + seed)
    pairs = [(i, j) for i in range(N) for j in range(N) if i != j]
    take = rng.choice(len(pairs), size=len(confs), replace=False)
    return {pairs[int(k)]: float(c) for k, c in zip(take, confs)}


def mcnemar(x, y):
    b = sum(1 for a, c in zip(x, y) if a and not c)
    c = sum(1 for a, c in zip(x, y) if (not a) and c)
    n = b + c
    if n == 0:
        return {"b": b, "c": c, "n_disc": 0, "p_exact": 1.0}
    k = min(b, c)
    tail = sum(math.comb(n, i) for i in range(k + 1)) / (2 ** n)
    return {"b": b, "c": c, "n_disc": n, "p_exact": min(1.0, 2 * tail)}


def boot_diff(x, y, seed=BOOT_SEED, B=BOOT_B):
    x, y = np.asarray(x, float), np.asarray(y, float)
    rng = np.random.default_rng(seed)
    n = len(x)
    d = np.empty(B)
    for i in range(B):
        idx = rng.integers(0, n, n)
        d[i] = float(np.mean(x[idx] - y[idx]))
    lo, hi = np.quantile(d, [0.025, 0.975])
    return {"diff_mean": float(np.mean(x - y)), "ci95": [float(lo), float(hi)],
            "seed": seed, "B": B}


def main():
    t0 = time.time()
    cfg = DiffusionConfig()
    N, adj, edges, labels, meta = reconstruct_mindmap()
    W_true = row_normalize(adj)
    named = {tuple(e) for e in meta["path_edges_named"]}
    prior, prior_source, prior_err = None, None, None
    if os.path.exists(CACHE_PATH):
        prior = llm_prior.load_prior(CACHE_PATH)
        prior_source = "cache"
    else:
        prior_err = "results/llm_prior_cache.json missing"
    P = prior_score_matrix(prior, (N, N)) if prior is not None else None
    P_conf = random_edge_priors = None
    if prior is not None:
        confs = list(prior.values())
        P_conf = prior_score_matrix(shuffle_conf_prior(prior, 424242), (N, N))
        random_edge_priors = [prior_score_matrix(random_edge_prior(N, confs, s), (N, N))
                              for s in RAND_PRIOR_SEEDS]

    per_edge = []
    for ei, (u, v) in enumerate(edges):
        rng = np.random.default_rng(70_000 + ei)  # 与 v1.6 完全一致
        adj_obs = adj.copy(); adj_obs[u, v] = 0.0
        W_obs = W_true.copy(); W_obs[u, v] = 0.0
        mask = np.zeros((N, N), bool); mask[u, v] = True
        pool = [j for j in range(N) if j != u and adj_obs[u, j] == 0]
        take = rng.choice(len(pool), size=min(N_NEG, len(pool)), replace=False)
        for k in take:
            mask[u, pool[k]] = True
        rec = {"edge": [int(u), int(v)], "edge_label": [labels[u], labels[v]],
               "on_named_path": (u, v) in named, "arms": {}}
        scores = {a: arm_scores(a, W_obs, mask, cfg, 0, 1, adj_obs, rng,
                                inst_seed=70_000 + ei) for a in BASE_ARMS}
        if P is not None:
            tiebreak = rng.random(int(mask.sum()))
            scores["llm_prior"] = prior_only(P, mask, tiebreak)
            for lam in LAMBDAS:
                scores[f"hybrid_raw@{lam}"] = raw_hybrid(scores["field_guided"], P, mask, lam)
                scores[f"hybrid_norm@{lam}"] = norm_hybrid(scores["field_guided"], P, mask, lam, tiebreak)
            # N1: 置信度打乱（端点不变）
            scores["llm_prior_confshuffle"] = prior_only(P_conf, mask, tiebreak)
            scores["hybrid_norm_confshuffle@0.5"] = norm_hybrid(
                scores["field_guided"], P_conf, mask, 0.5, tiebreak)
            # N2: 随机边先验 ×5（synthetic_null）
            for s, Pr in zip(RAND_PRIOR_SEEDS, random_edge_priors):
                scores[f"llm_prior_rand{s}"] = prior_only(Pr, mask, tiebreak)
                scores[f"hybrid_norm_rand{s}@0.5"] = norm_hybrid(
                    scores["field_guided"], Pr, mask, 0.5, tiebreak)
        for a, s in scores.items():
            hit = top3_hit_per_edge(s, [(u, v)], mask)[0]
            rec["arms"][a] = {"rank": hit["rank"], "hit": hit["hit"]}
        per_edge.append(rec)

    run_arms = list(scores.keys())
    def xs(arm, named_only=None):
        return [float(r["arms"][arm]["hit"]) for r in per_edge
                if named_only is None or (named_only and r["on_named_path"])
                or (named_only is False and not r["on_named_path"])]
    arms = {}
    for a in run_arms:
        arms[a] = {"top3_hit": mean_std(xs(a)),
                   "top3_hit_named_path": mean_std(xs(a, True)),
                   "top3_hit_filler": mean_std(xs(a, False))}

    def cmp(a, b, named_only=None):
        return {"mcnemar": mcnemar(xs(a, named_only), xs(b, named_only)),
                "bootstrap": boot_diff(xs(a, named_only), xs(b, named_only))}
    paired = {}
    if "hybrid_norm@0.5" in run_arms:
        for subset, flag in (("overall", None), ("named_path", True), ("filler", False)):
            paired[subset] = {
                "hybrid_norm@0.5_vs_field_guided": cmp("hybrid_norm@0.5", "field_guided", flag),
                "hybrid_norm@0.5_vs_random": cmp("hybrid_norm@0.5", "random", flag),
                "hybrid_norm@0.5_vs_llm_prior": cmp("hybrid_norm@0.5", "llm_prior", flag),
                "real_vs_confshuffle": cmp("hybrid_norm@0.5", "hybrid_norm_confshuffle@0.5", flag),
            }
            rand_hits = np.array([xs(f"hybrid_norm_rand{s}@0.5", flag) for s in RAND_PRIOR_SEEDS])
            paired[subset]["real_vs_randomedge_mean"] = {
                "randomedge_mean_hit": float(rand_hits.mean()),
                "randomedge_per_seed_hit": [float(r.mean()) for r in rand_hits],
                "real_hit": float(np.mean(xs("hybrid_norm@0.5", flag)))}

    fg_named = arms["field_guided"]["top3_hit_named_path"]["mean"]
    hn_named = arms.get("hybrid_norm@0.5", {}).get("top3_hit_named_path", {}).get("mean")
    success = {"status": "evaluated" if P is not None else "pending_no_cache",
               "lambda_invariance_explained": True,
               "E5b_fusion_fix_gain": bool(P is not None and hn_named is not None and hn_named > fg_named),
               "note": "探索性；不回溯改写 v1.6 成功/失败表述。null 先验均为 synthetic_null。"}
    out = {"experiment": "deposon_v17_fusion_fix", "spec_version": "v1.7.1",
           "config": config_dict(cfg), "protocol": {
               "same_as_v16": "同图/同种子70000+ei/同N_NEG=10/top-3；仅新增评分时刻归一融合与阴性对照",
               "null_controls": "N1 confidence shuffle (endpoints fixed); N2 random directed prior edges x5 (synthetic_null)"},
           "llm_prior": {"source": prior_source, "cache_path": CACHE_PATH,
                         "n_prior_edges": len(prior) if prior else 0, "error": prior_err},
           "arms": run_arms, "experiment_B": {"reconstruction": meta, "arms": arms,
                                              "per_edge": per_edge},
           "paired_stats": paired, "success_evaluation_exploratory": success,
           "runtime_sec": round(time.time() - t0, 3),
           "honesty": ["零 API：仅复用 llm_prior_cache.json；未读取/写入 key；无网络。",
                       "同 v1.6 留一协议；新增臂全部为评分时刻修复或 synthetic_null 对照。",
                       "λ 不变性根因：稀疏先验 confidence 量纲远大于 field 候选内差距，λ=0.25 已饱和。",
                       "不多重比较校正：本实验不依赖 p<0.05 作正向主张。"]}
    os.makedirs(RESULTS, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({"out": OUT_PATH, "runtime_sec": out["runtime_sec"],
                      "named": {a: round(arms[a]["top3_hit_named_path"]["mean"], 4) for a in run_arms},
                      "overall": {a: round(arms[a]["top3_hit"]["mean"], 4) for a in run_arms},
                      "success": success}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
