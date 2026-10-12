# -*- coding: utf-8 -*-
# Deposon v2.0 横向对比评估（主代理实现，SPEC v2.0 §2 辅助臂 + §4 GT-2）
#   → results/deposon_v20_crossval.json
#
# A) 族 L 先验臂横向对比（labels-only 先验，零泄漏）：
#    - 四图全候选留一：llm_prior / hybrid_norm@0.5（λ∈[0,1] 凸组合，v1.9 教训）
#      与既有七臂并列；
#    - 方向分析：先验边 vs 金边——无向骨架重叠、共有对方向一致率、
#      按域类型（抽象→具体 ×2 / 过程→结果 ×2）分组的 GOAL 中心反向检验
#      （v1.9 开放问题 #3 的廉价版，SPEC §1 对立统一设计）。
# B) GT-2 自适应攻击者（SPEC §4，判定规则冻结于本文件 GT2_* 常量）：
#    - 攻击有效性：攻击标签绕过关键词表的比例（须 =1.0 才是有效自适应攻击）；
#    - 注入：每张图对采样 named 边 (u,v) 注入陷阱节点 t（u→t），候选行 u 多出
#      强语义干扰项；比较 rule_filter 与 field_mean 注入前后 named Hits@3；
#    - 判定：rule 塌陷 >20pp 且 field_mean 保持（塌陷 ≤20pp）→ 场有独立于
#      关键词的防御价值（H-C 潜在反例）；两者都塌陷 → 防御主张全面降级。
# no LLM API calls issued：只读 results/familyL_prior_cache 与 gt2_attacker_cache。
import json
import os
import time

import numpy as np

from deposon_diffusion import DiffusionConfig, config_dict
from mindmap_corpus_v20 import CORPUS_DIR, FAMILY_L_DOMAINS, load_corpus
from llm_prior import _extract_json_array, _validate_prior
from run_v15_experiment import row_normalize
from run_v16_llm_prior import prior_score_matrix
from run_v17_fusion_fix import minmax_mask
from run_v19_fullrank import full_candidate_mask, gold_rank
from run_v19_meanfield import field_scores_init
from run_v20_corpus_eval import (adamic_adar_row, jaccard_row, rule_filter_row,
                                 RULE_KEYWORDS)

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
PRIOR_DIR = os.path.join(RESULTS, "familyL_prior_cache")
ATK_DIR = os.path.join(RESULTS, "gt2_attacker_cache")
OUT_PATH = os.path.join(RESULTS, "deposon_v20_crossval.json")

DOMAIN_KIND = {"physics_concepts": "abstract_to_specific",
               "biological_taxonomy": "abstract_to_specific",
               "algorithm_process": "process_to_result",
               "historical_causality": "process_to_result"}
HYBRID_LAM = 0.5            # λ∈[0,1] 凸组合（v1.9 λ>1 反场 artifact 教训）
GT2_N_INJECT = 10           # 每图注入的 named 边数（采样）
GT2_SAMPLE_SEED = 20260828
GT2_COLLAPSE_PP = 0.20      # 塌陷阈值 20pp（SPEC §4 预登记）


# ---------------------------------------------------------------- 先验解析
def load_prior_cache(domain):
    path = os.path.join(PRIOR_DIR, f"{domain}.json")
    rec = json.load(open(path, encoding="utf-8"))
    items = _extract_json_array(rec["response_text"])
    n = len(json.load(open(os.path.join(CORPUS_DIR, f"L_{domain}.json"),
                           encoding="utf-8"))["labels"])
    prior = _validate_prior(items, n)
    return prior, rec


# ---------------------------------------------------------------- A) 先验臂评估
def eval_prior_arm(graph, prior, cfg):
    N = graph["N"]
    edges = [tuple(e) for e in graph["edges"]]
    named = {tuple(e) for e in graph["named_edges"]}
    adj = np.zeros((N, N))
    for (u, v) in edges:
        adj[u, v] = 1.0
    W_true = row_normalize(adj)
    P = prior_score_matrix(prior, (N, N))
    g_seed = int(graph["seed"])
    arms = ("field_mean", "llm_prior", f"hybrid_norm@{HYBRID_LAM}",
            "random", "degree", "adamic_adar", "jaccard", "rule_filter")
    hits = {a: {"named": [], "filler": []} for a in arms}
    for ei, (u, v) in enumerate(edges):
        rng = np.random.default_rng(g_seed * 100_003 + ei)
        adj_obs = adj.copy(); adj_obs[u, v] = 0.0
        W_obs = W_true.copy(); W_obs[u, v] = 0.0
        mask = full_candidate_mask(N, u)
        cand = np.flatnonzero(mask[u])
        tiebreak = rng.random(int(cand.size))
        rows = {}
        fm_full = field_scores_init(W_obs, mask, cfg, graph["source"],
                                    graph["target"], g_seed + ei, "prior_mean")
        rows["field_mean"] = fm_full[u]
        s = np.full(N, -np.inf); s[cand] = P[u, cand] + 1e-6 * tiebreak
        rows["llm_prior"] = s
        fgn = minmax_mask(fm_full[u][cand]); prn = minmax_mask(P[u, cand])
        s = np.full(N, -np.inf)
        s[cand] = (1 - HYBRID_LAM) * fgn + HYBRID_LAM * prn + 1e-6 * tiebreak
        rows[f"hybrid_norm@{HYBRID_LAM}"] = s
        s = np.full(N, -np.inf); s[cand] = rng.random(int(cand.size))
        rows["random"] = s
        indeg = adj_obs.sum(axis=0)
        s = np.full(N, -np.inf); s[cand] = indeg[cand] + 1e-6 * tiebreak
        rows["degree"] = s
        s = adamic_adar_row(adj_obs, u, cand); s[cand] += 1e-6 * tiebreak
        rows["adamic_adar"] = s
        s = jaccard_row(adj_obs, u, cand); s[cand] += 1e-6 * tiebreak
        rows["jaccard"] = s
        s = rule_filter_row(graph["labels"], cand); s[cand] += 1e-6 * tiebreak
        rows["rule_filter"] = s
        subset = "named" if (u, v) in named else "filler"
        for a, srow in rows.items():
            hits[a][subset].append(float(gold_rank(srow, cand, v) < 3))
    return {a: {k: (float(np.mean(v)) if v else None) for k, v in vv.items()}
            for a, vv in hits.items()}


def direction_analysis(graph, prior):
    """先验边 vs 金边：无向骨架重叠、共有对方向一致率、hub 中心性反向。"""
    gold_dir = {tuple(e) for e in graph["edges"]}
    gold_und = {frozenset(e) for e in gold_dir}
    prior_dir = set(prior.keys())
    prior_und = {frozenset(e) for e in prior_dir}
    inter = prior_und & gold_und
    agree = sum(1 for fs in inter if tuple(sorted(fs)) in prior_dir)
    # hub 中心反向：先验中指向全图最大入度 hub 的边，金图中方向相反的比例
    indeg = {}
    for (u, v) in gold_dir:
        indeg[v] = indeg.get(v, 0) + 1
    hub = max(indeg, key=indeg.get) if indeg else None
    hub_prior = [e for e in prior_dir if hub is not None and hub in e]
    hub_reversed = sum(1 for (u, v) in hub_prior
                       if (u, v) not in gold_dir and (v, u) in gold_dir)
    return {"n_prior_edges": len(prior_dir),
            "undirected_overlap": len(inter),
            "undirected_jaccard": (round(len(inter) / len(prior_und | gold_und), 4)
                                   if (prior_und | gold_und) else 0.0),
            "direction_agreement_on_shared": (round(agree / len(inter), 4)
                                              if inter else None),
            "hub_node": hub, "hub_prior_edges": len(hub_prior),
            "hub_reversed_edges": hub_reversed}


# ---------------------------------------------------------------- B) GT-2 评估
def load_attacker_labels(domain, graph_labels):
    rec = json.load(open(os.path.join(ATK_DIR, f"{domain}.json"), encoding="utf-8"))
    items = _extract_json_array(rec["response_text"])
    labels = []
    for it in items:
        lab = str(it["label"]).strip()
        if lab:
            labels.append({"label": lab, "mislead": str(it.get("mislead", ""))})
    evasions = [t for t in labels
                if not any(k in t["label"].lower() for k in RULE_KEYWORDS)]
    novel = [t for t in evasions if t["label"] not in set(graph_labels)]
    return {"raw": labels, "evading": evasions, "novel": novel,
            "evasion_rate": (len(evasions) / len(labels)) if labels else 0.0}


def gt2_eval_graph(graph, attack_labels, cfg):
    """注入陷阱节点后比较 rule_filter 与 field_mean 的 named Hits@3。"""
    N0 = graph["N"]
    edges = [tuple(e) for e in graph["edges"]]
    named = [tuple(e) for e in graph["named_edges"]]
    rng = np.random.default_rng(GT2_SAMPLE_SEED)
    take = rng.choice(len(named), size=min(GT2_N_INJECT, len(named)), replace=False)
    inject_edges = [named[int(k)] for k in take]
    traps = attack_labels[: len(inject_edges)]
    if len(traps) < len(inject_edges):
        inject_edges = inject_edges[: len(traps)]

    def run(with_traps):
        N = N0 + (len(inject_edges) if with_traps else 0)
        adj = np.zeros((N, N))
        for (u, v) in edges:
            adj[u, v] = 1.0
        labels = list(graph["labels"])
        if with_traps:
            for k, ((u, _v), t) in enumerate(zip(inject_edges, traps)):
                adj[u, N0 + k] = 1.0
                labels.append(t["label"])
        W_true = row_normalize(adj)
        g_seed = int(graph["seed"])
        out = {"field_mean": [], "rule_filter": []}
        for k, (u, v) in enumerate(inject_edges):
            rng_e = np.random.default_rng(g_seed * 100_003 + k)
            adj_obs = adj.copy(); adj_obs[u, v] = 0.0
            W_obs = W_true.copy(); W_obs[u, v] = 0.0
            mask = full_candidate_mask(N, u)
            cand = np.flatnonzero(mask[u])
            tiebreak = rng_e.random(int(cand.size))
            fm = field_scores_init(W_obs, mask, cfg, graph["source"],
                                   graph["target"], g_seed + k, "prior_mean")
            out["field_mean"].append(float(gold_rank(fm[u], cand, v) < 3))
            s = rule_filter_row(labels, cand); s[cand] += 1e-6 * tiebreak
            out["rule_filter"].append(float(gold_rank(s, cand, v) < 3))
        return {a: float(np.mean(v)) for a, v in out.items()}

    base = run(False)
    attacked = run(True)
    return {"n_injected": len(inject_edges), "baseline": base,
            "attacked": attacked,
            "collapse_pp": {a: round(base[a] - attacked[a], 4)
                            for a in base}}


def gt2_verdict(per_graph):
    """SPEC §4 冻结判定：rule 塌陷 >20pp 且 field_mean 保持（≤20pp）→
    场有独立防御价值；两者都塌陷 → 防御主张全面降级；其他 → 未分离。"""
    rule_col = [g["collapse_pp"]["rule_filter"] for g in per_graph.values()]
    fm_col = [g["collapse_pp"]["field_mean"] for g in per_graph.values()]
    rule_mean = float(np.mean(rule_col)); fm_mean = float(np.mean(fm_col))
    if rule_mean > GT2_COLLAPSE_PP and fm_mean <= GT2_COLLAPSE_PP:
        verdict = "field_has_independent_defense_value"
    elif rule_mean > GT2_COLLAPSE_PP and fm_mean > GT2_COLLAPSE_PP:
        verdict = "both_collapse_defense_claims_downgraded"
    else:
        verdict = "no_separation_adaptive_attack_not_decisive"
    return {"verdict": verdict,
            "rule_collapse_mean_pp": round(rule_mean, 4),
            "field_mean_collapse_mean_pp": round(fm_mean, 4),
            "threshold_pp": GT2_COLLAPSE_PP,
            "per_graph_collapse": {g: v["collapse_pp"]
                                   for g, v in per_graph.items()}}


# ---------------------------------------------------------------- main
def main():
    t0 = time.time()
    cfg = DiffusionConfig()
    graphs = {g["graph_id"]: g for g in load_corpus(CORPUS_DIR, families=("L",))}
    prior_eval, dir_analysis, atk_meta, gt2 = {}, {}, {}, {}
    for domain in FAMILY_L_DOMAINS:
        gid = f"L_{domain}"
        g = graphs[gid]
        prior, _rec = load_prior_cache(domain)
        prior_eval[gid] = eval_prior_arm(g, prior, cfg)
        dir_analysis[gid] = direction_analysis(g, prior)
        dir_analysis[gid]["domain_kind"] = DOMAIN_KIND[domain]
        atk = load_attacker_labels(domain, g["labels"])
        atk_meta[gid] = {"n_raw": len(atk["raw"]), "n_evading": len(atk["evading"]),
                         "n_novel": len(atk["novel"]),
                         "evasion_rate": round(atk["evasion_rate"], 4),
                         "labels_used": [t["label"] for t in atk["novel"]]}
        gt2[gid] = gt2_eval_graph(g, atk["novel"], cfg)

    # 方向语义分组（对立统一）：抽象→具体 vs 过程→结果
    by_kind = {}
    for gid, a in dir_analysis.items():
        k = a["domain_kind"]
        by_kind.setdefault(k, []).append(a)
    kind_summary = {}
    for k, arr in by_kind.items():
        da = [x["direction_agreement_on_shared"] for x in arr
              if x["direction_agreement_on_shared"] is not None]
        hr = [x["hub_reversed_edges"] for x in arr]
        kind_summary[k] = {
            "n_graphs": len(arr),
            "mean_direction_agreement": (round(float(np.mean(da)), 4) if da else None),
            "total_hub_reversed": int(sum(hr))}
    # GT-2 判定
    gt2_v = gt2_verdict(gt2)

    out = {"experiment": "deposon_v20_crossval", "spec_version": "v2.0",
           "spec": "docs/SPEC_v2.0.md §2（族 L 先验臂）/ §4（GT-2）",
           "config": config_dict(cfg),
           "hybrid_lambda_convex": HYBRID_LAM,
           "prior_arm_eval": prior_eval,
           "direction_analysis": dir_analysis,
           "direction_kind_summary": kind_summary,
           "gt2_attacker_meta": atk_meta,
           "gt2_eval": gt2,
           "gt2_verdict": gt2_v,
           "runtime_sec": round(time.time() - t0, 3),
           "honesty": [
               "no LLM API calls issued: 只读 familyL_prior_cache 与 gt2_attacker_cache；"
               "全部评估本地确定性/种子化。",
               "先验为零泄漏 labels-only（v1.6 同 prompt 构造器）；先验臂与生成臂同模型族"
               "（kimi-for-coding），同源污染风险在案（SPEC §1）。",
               "hybrid 用 λ=0.5 凸组合（v1.9 λ>1 反场 artifact 教训）；不探索 λ 网格。",
               "GT-2 攻击有效性以 evasion_rate=1.0 为前提；若 <1.0 则攻击非完全自适应，"
               "如实报告不美化。",
               "判定规则机械求值；负面结果如实写入 verdict，不美化。"]}
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({"out": OUT_PATH,
                      "prior_named": {g: v["llm_prior"]["named"]
                                      for g, v in prior_eval.items()},
                      "fm_named": {g: v["field_mean"]["named"]
                                   for g, v in prior_eval.items()},
                      "direction_kind_summary": kind_summary,
                      "gt2_verdict": gt2_v}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
