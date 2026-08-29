# -*- coding: utf-8 -*-
# GT-8b「领域鉴定器 v0」real_semantics 轴预登记复现评分
# （docs/SPEC_GT8B.md，判定规则冻结于本文件 GT8B_* 常量与 gt8b_verdict）
#   → results/deposon_v20_gt8b.json
#
# 协议：仿 run_v20_crossval_eval.py 全边留一、全候选 raw 口径
#   （full_candidate_mask）；臂 = field_mean / random / degree / llm_prior
#   四臂；每边 rng = default_rng(g_seed*100003+ei)，场实例种子 g_seed+ei；
#   指标 = named Hits@3（gold_rank < 3）。
# 零 API：只读 results/gt8b_cache/（图 + 先验缓存）；任一缓存缺失 →
#   该域记 cache_missing/fetch_failed，不计入判定分母，优雅跳过并逐字
#   披露缺失文件清单（pytest 不依赖缓存存在）。
import json
import os
import time

import numpy as np

from deposon_diffusion import DiffusionConfig, config_dict
from llm_prior import _extract_json_array, _validate_prior
from mindmap_corpus_v20 import CacheMissingError
from run_v15_experiment import row_normalize
from run_v16_llm_prior import prior_score_matrix
from run_v19_fullrank import full_candidate_mask, gold_rank
from run_v19_meanfield import field_scores_init
from run_v20_gt8b_fetch import CACHE_DIR, GT8B_DOMAINS
from run_v20_gt8b_ingest import GRAPH_DIR, graph_path_for

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
OUT_PATH = os.path.join(RESULTS, "deposon_v20_gt8b.json")

# ------------------------------------------------- SPEC_GT8B §1/§5 冻结判定常量
ARMS = ("field_mean", "random", "degree", "llm_prior")
GT8B_PRIOR_MIN = 0.6          # prior_named ≥ 0.6
GT8B_MARGIN = 0.2             # 且 prior_named > field_named + 0.2
GT8B_MIN_DOMAINS = 2          # 成功标准：2/2 有效新域


# ------------------------------------------------------------ 缓存加载
def load_graph(domain, graph_dir=GRAPH_DIR):
    path = graph_path_for(domain, graph_dir)
    if not os.path.exists(path):
        raise CacheMissingError(
            f"GT-8b graph missing: {path} — 请先由主代理执行 "
            "run_v20_gt8b_fetch.py 并运行 run_v20_gt8b_ingest.py；"
            "no LLM API calls issued by this script。")
    return json.load(open(path, encoding="utf-8"))


def load_prior(domain, n_labels, cache_dir=CACHE_DIR):
    path = os.path.join(cache_dir, f"prior_{domain}.json")
    if not os.path.exists(path):
        raise CacheMissingError(
            f"GT-8b prior cache missing: {path} — 请先由主代理执行 "
            "run_v20_gt8b_fetch.py（先验臂阶段）。")
    rec = json.load(open(path, encoding="utf-8"))
    return _validate_prior(_extract_json_array(rec["response_text"]),
                           n_labels), rec


# ------------------------------------------------------------ 四臂评估（协议同式）
def eval_graph(graph, prior, cfg):
    """单图全边留一（全候选协议），臂 = field_mean/random/degree/llm_prior，
    与 run_v20_crossval_eval.eval_prior_arm 逐行同式（仅取本实验四臂）。"""
    N = graph["N"]
    edges = [tuple(e) for e in graph["edges"]]
    named = {tuple(e) for e in graph["named_edges"]}
    adj = np.zeros((N, N))
    for (u, v) in edges:
        adj[u, v] = 1.0
    W_true = row_normalize(adj)
    P = prior_score_matrix(prior, (N, N))
    g_seed = int(graph["seed"])
    hits = {a: {"named": [], "filler": []} for a in ARMS}
    for ei, (u, v) in enumerate(edges):
        rng = np.random.default_rng(g_seed * 100_003 + ei)
        adj_obs = adj.copy(); adj_obs[u, v] = 0.0
        W_obs = W_true.copy(); W_obs[u, v] = 0.0
        mask = full_candidate_mask(N, u)
        cand = np.flatnonzero(mask[u])
        tb = rng.random(int(cand.size))
        rows = {"field_mean": field_scores_init(
            W_obs, mask, cfg, graph["source"], graph["target"],
            g_seed + ei, "prior_mean")[u]}
        s = np.full(N, -np.inf); s[cand] = rng.random(int(cand.size))
        rows["random"] = s
        indeg = adj_obs.sum(axis=0)
        s = np.full(N, -np.inf); s[cand] = indeg[cand] + 1e-6 * tb
        rows["degree"] = s
        s = np.full(N, -np.inf); s[cand] = P[u, cand] + 1e-6 * tb
        rows["llm_prior"] = s
        subset = "named" if (u, v) in named else "filler"
        for a, srow in rows.items():
            hits[a][subset].append(float(gold_rank(srow, cand, v) < 3))
    return {a: {k: (float(np.mean(v)) if v else None)
                for k, v in vv.items()} for a, vv in hits.items()}


def domain_satisfied(named_scores):
    """SPEC_GT8B §1 冻结逐域阈值（机械求值，纯函数）：
    prior_named ≥ 0.6 且 prior_named > field_named + 0.2。"""
    p, f = named_scores["llm_prior"], named_scores["field_mean"]
    return bool(p is not None and f is not None
                and p >= GT8B_PRIOR_MIN and p > f + GT8B_MARGIN)


# ------------------------------------------------------------ 判定规则（冻结）
def gt8b_verdict(per_domain, min_domains=GT8B_MIN_DOMAINS):
    """GT-8b 冻结判定（机械求值，纯函数，tests/test_v20_gt8b.py 锁定）：

    per_domain: [{domain, satisfied}]（仅含有效域；fetch_failed 域不入列，
    不计入分母）。
    支持：≥min_domains 个有效域且全部满足 ⇒ supports_H_GT8B；
    判死：≥min_domains 个有效域且全不满足 ⇒ H_GT8B_dead，如实宣布；
    其余（1/2、或有效域数 < min_domains 含全部 fetch_failed）：
    inconclusive，如实报。
    """
    n = len(per_domain)
    sat = [d["domain"] for d in per_domain if d["satisfied"]]
    unsat = [d["domain"] for d in per_domain if not d["satisfied"]]
    if n >= min_domains and len(sat) == n:
        verdict = "supports_H_GT8B"
    elif n >= min_domains and len(unsat) == n:
        verdict = "H_GT8B_dead"
    else:
        verdict = "inconclusive"
    return {"verdict": verdict,
            "supported_H_GT8B": bool(verdict == "supports_H_GT8B"),
            "n_valid_domains": n,
            "domains_satisfied": sat,
            "domains_unsatisfied": unsat,
            "thresholds": {"prior_named_min": GT8B_PRIOR_MIN,
                           "margin_over_field": GT8B_MARGIN,
                           "min_domains": min_domains}}


# ------------------------------------------------------------ main
def main(cache_dir=CACHE_DIR, graph_dir=GRAPH_DIR, out_path=OUT_PATH):
    t0 = time.time()
    cfg = DiffusionConfig()
    per_domain_scores, per_domain_flag, cache_missing = {}, {}, {}
    for domain in GT8B_DOMAINS:
        gid = f"L_{domain}"
        try:
            g = load_graph(domain, graph_dir)
            prior, rec = load_prior(domain, g["N"], cache_dir)
        except CacheMissingError as e:
            cache_missing[domain] = str(e)
            continue
        scores = eval_graph(g, prior, cfg)
        named = {a: scores[a]["named"] for a in ARMS}
        per_domain_scores[gid] = {
            "arms": scores,
            "named_summary": {a: (round(v, 4) if v is not None else None)
                              for a, v in named.items()},
            "real_semantics": g.get("real_semantics", 1),
            "prior_named_minus_field_named": (
                round(named["llm_prior"] - named["field_mean"], 4)
                if named["llm_prior"] is not None
                and named["field_mean"] is not None else None),
            "prior_named_minus_random_named": (
                round(named["llm_prior"] - named["random"], 4)
                if named["llm_prior"] is not None
                and named["random"] is not None else None),
            "prior_cache_prompt_sha256": rec.get("prompt_sha256"),
            "graph_sha256": g.get("sha256")}
        per_domain_flag[gid] = {"domain": domain,
                                "satisfied": domain_satisfied(named)}
    verdict = gt8b_verdict(list(per_domain_flag.values()))
    out = {"experiment": "deposon_v20_gt8b",
           "spec": "docs/SPEC_GT8B.md",
           "config": config_dict(cfg),
           "domains_frozen": list(GT8B_DOMAINS),
           "per_domain": per_domain_scores,
           "cache_missing": cache_missing,
           "gt8b_verdict": verdict,
           "runtime_sec": round(time.time() - t0, 3),
           "honesty": [
               "no LLM API calls issued: 只读 results/gt8b_cache/；"
               "缓存缺失域记 cache_missing，不计入判定分母，绝不伪造数据。",
               "先验为零泄漏 labels-only（build_prior_prompt，与族 L 同构造器"
               "同模型）；先验臂与生成臂同模型族 ⇒ 同源污染风险在案。",
               "判定规则机械求值；负面结果如实写入 verdict，不美化。"]}
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({"out": out_path,
                      "named_summary": {g: v["named_summary"]
                                        for g, v in per_domain_scores.items()},
                      "cache_missing": sorted(cache_missing),
                      "gt8b_verdict": verdict}, ensure_ascii=False, indent=1))
    return out


if __name__ == "__main__":
    main()
