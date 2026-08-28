# -*- coding: utf-8 -*-
# Deposon v1.9-E9.2 全候选排序协议（docs/SPEC_v1.9.md Part A，预登记）
# 候选 = 全部 N−1 个非自身节点（raw/unfiltered：金边 v 在候选中，不剔除其他观测边）。
# 指标 MRR / Hits@1 / Hits@3（overall/named/filler + 真实/占位标签切分）。
# 无负采样 ⇒ 采样器敏感性按构造归零。零 API，缓存只读。
import json, os, time
import numpy as np
from deposon_diffusion import DiffusionConfig, config_dict
from run_v15_experiment import reconstruct_mindmap, row_normalize, mean_std
from run_v16_llm_prior import prior_score_matrix
from run_v17_fusion_fix import minmax_mask
from run_v19_meanfield import field_scores_init, is_placeholder, PLACEHOLDER_NAMED
import llm_prior

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
OUT_PATH = os.path.join(RESULTS, "deposon_v19_fullrank.json")
CACHE_PATH = os.path.join(RESULTS, "llm_prior_cache.json")
LAMBDAS_E92 = (0.5, 2.0)
ARMS = ("field_mean", "field_guided", "random", "degree", "llm_prior",
        "hybrid_norm@0.5", "hybrid_norm@2.0")


def full_candidate_mask(N, u):
    """全候选 mask：行 u 的全部非自身列（含其他观测出边——raw 口径，预登记）。"""
    mask = np.zeros((N, N), bool)
    mask[u, :] = True
    mask[u, u] = False
    return mask


def rank_metrics(ranks):
    """由金边秩（0 基）列表计算 MRR / Hits@1 / Hits@3。"""
    r = np.asarray(ranks, dtype=float)
    if r.size == 0:
        return {"mrr": None, "hits@1": None, "hits@3": None, "n": 0,
                "mean_rank": None, "median_rank": None}
    return {"mrr": float(np.mean(1.0 / (r + 1.0))),
            "hits@1": float(np.mean(r < 1)), "hits@3": float(np.mean(r < 3)),
            "n": int(r.size), "mean_rank": float(r.mean()),
            "median_rank": float(np.median(r))}


def gold_rank(scores_row, cand, v):
    """金边 v 在候选 cand 中按 scores_row 降序（mergesort 稳定）的秩（0 基）。"""
    order = cand[np.argsort(-scores_row[cand], kind="mergesort")]
    return int(np.flatnonzero(order == v)[0])


def main():
    t0 = time.time()
    cfg = DiffusionConfig()
    N, adj, edges, labels, meta = reconstruct_mindmap()
    W_true = row_normalize(adj)
    named = {tuple(e) for e in meta["path_edges_named"]}
    prior, prior_source = None, None
    if os.path.exists(CACHE_PATH):
        prior = llm_prior.load_prior(CACHE_PATH)
        prior_source = "cache"
    P = prior_score_matrix(prior, (N, N)) if prior is not None else None

    per_edge = []
    for ei, (u, v) in enumerate(edges):
        rng = np.random.default_rng(70_000 + ei)  # 同种子族；仅驱动 tiebreak/random 臂
        adj_obs = adj.copy(); adj_obs[u, v] = 0.0
        W_obs = W_true.copy(); W_obs[u, v] = 0.0
        mask = full_candidate_mask(N, u)
        cand = np.flatnonzero(mask[u])
        tiebreak = rng.random(int(mask.sum()))
        scores = {}
        scores["field_mean"] = field_scores_init(
            W_obs, mask, cfg, 0, 1, 70_000 + ei, "prior_mean")[u]
        scores["field_guided"] = field_scores_init(
            W_obs, mask, cfg, 0, 1, 70_000 + ei, "dirichlet")[u]
        s = np.full(N, -np.inf); s[cand] = rng.random(cand.size)
        scores["random"] = s
        indeg = adj_obs.sum(axis=0)
        s = np.full(N, -np.inf); s[cand] = indeg[cand] + 1e-6 * tiebreak
        scores["degree"] = s
        if P is not None:
            s = np.full(N, -np.inf); s[cand] = P[u, cand] + 1e-6 * tiebreak
            scores["llm_prior"] = s
            fgn = minmax_mask(scores["field_mean"][cand])
            prn = minmax_mask(P[u, cand])
            for lam in LAMBDAS_E92:
                s = np.full(N, -np.inf)
                s[cand] = (1.0 - lam) * fgn + lam * prn + 1e-6 * tiebreak
                scores[f"hybrid_norm@{lam}"] = s
        rec = {"edge": [int(u), int(v)], "edge_label": [labels[u], labels[v]],
               "on_named_path": (u, v) in named,
               "placeholder_target": is_placeholder(labels[v]),
               "placeholder_named_edge": (u, v) in PLACEHOLDER_NAMED,
               "n_candidates": int(cand.size), "arms": {}}
        for a, srow in scores.items():
            rec["arms"][a] = {"rank": gold_rank(srow, cand, v)}
        per_edge.append(rec)

    run_arms = list(scores.keys())

    def subset(flag, r):
        if flag == "overall":
            return True
        if flag == "named":
            return r["on_named_path"]
        if flag == "filler":
            return not r["on_named_path"]
        if flag == "named_real_label":
            return r["on_named_path"] and not r["placeholder_named_edge"]
        if flag == "named_placeholder":
            return r["placeholder_named_edge"]
        raise ValueError(flag)

    FLAGS = ("overall", "named", "filler", "named_real_label", "named_placeholder")
    arms = {a: {f: rank_metrics([r["arms"][a]["rank"] for r in per_edge
                                 if subset(f, r)]) for f in FLAGS}
            for a in run_arms}
    # 度保持难负样本分析（R2）：named vs filler 金边秩分布
    hard_neg = {a: {
        "named_ranks": sorted(int(r["arms"][a]["rank"]) for r in per_edge
                              if r["on_named_path"]),
        "filler_ranks": sorted(int(r["arms"][a]["rank"]) for r in per_edge
                               if not r["on_named_path"])} for a in run_arms}

    # 与 N_NEG=10 协议（E9.1）结论差异
    e91_path = os.path.join(RESULTS, "deposon_v19_meanfield.json")
    protocol_diff = None
    if os.path.exists(e91_path):
        e91 = json.load(open(e91_path))["experiment_B"]["arms"]
        protocol_diff = {}
        for a in run_arms:
            if a in e91:
                protocol_diff[a] = {
                    "neg10_top3_named": e91[a]["named"]["mean"],
                    "neg10_top3_overall": e91[a]["overall"]["mean"],
                    "fullrank_hits3_named": arms[a]["named"]["hits@3"],
                    "fullrank_hits3_overall": arms[a]["overall"]["hits@3"],
                    "fullrank_mrr_overall": arms[a]["overall"]["mrr"]}
        # 结论翻转检查：named 上各臂相对 random 的优劣在两协议间是否翻转
        flips = []
        for a in run_arms:
            if a in ("random",) or a not in e91:
                continue
            d10 = e91[a]["named"]["mean"] - e91["random"]["named"]["mean"]
            dfr = arms[a]["named"]["hits@3"] - arms["random"]["named"]["hits@3"]
            if (d10 > 0) != (dfr > 0):
                flips.append({"arm": a, "neg10_diff_vs_random": d10,
                              "fullrank_diff_vs_random": dfr})
        protocol_diff["named_vs_random_sign_flips"] = flips

    out = {"experiment": "deposon_v19_fullrank", "spec_version": "v1.9",
           "spec": "docs/SPEC_v1.9.md Part A E9.2",
           "config": config_dict(cfg),
           "protocol": {
               "candidates": "全部 N−1 个非自身节点（raw/unfiltered：金边 v 在候选中，"
                             "不剔除其他观测边；场臂 mask=该行全部非自身列，观测出边随之"
                             "成为掩码自由度——预登记口径，如实披露）",
               "metrics": "MRR / Hits@1 / Hits@3（0 基秩，mergesort 稳定序 + 1e-6 tiebreak）",
               "sampler_sensitivity": "无负采样 ⇒ 对负池种子的敏感性按构造为 0",
               "tie_policy": "1e-6 确定性微扰（同 SPEC v1.9 公共口径）"},
           "llm_prior": {"source": prior_source, "cache_path": CACHE_PATH,
                         "n_prior_edges": len(prior) if prior else 0},
           "arms": run_arms,
           "results": {"arms": arms,
                       "degree_preserving_hard_negative_analysis": hard_neg,
                       "protocol_diff_vs_neg10": protocol_diff,
                       "per_edge": per_edge},
           "runtime_sec": round(time.time() - t0, 3),
           "honesty": [
               "零 API：仅只读 llm_prior_cache.json；无 key、无网络、无 mock。",
               "raw 口径不剔除其他观测边：观测出边是合法干扰项；场臂 mask 含观测出边"
               "（其进入掩码自由度），为全候选口径的必然代价，已预登记。",
               "采样器敏感性归零仅指负池采样；随机臂/tiebreak 仍由固定种子驱动。",
               "负面与 artifact 如实报告；不回溯改写 v1.5–v1.8 结论。"]}
    os.makedirs(RESULTS, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({"out": OUT_PATH, "runtime_sec": out["runtime_sec"],
                      "mrr_overall": {a: round(arms[a]["overall"]["mrr"], 4) for a in run_arms},
                      "hits3_named": {a: round(arms[a]["named"]["hits@3"], 4) for a in run_arms},
                      "hits3_filler": {a: round(arms[a]["filler"]["hits@3"], 4) for a in run_arms},
                      "sign_flips": (protocol_diff or {}).get("named_vs_random_sign_flips")},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
