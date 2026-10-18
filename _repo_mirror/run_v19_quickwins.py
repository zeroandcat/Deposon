# -*- coding: utf-8 -*-
# Deposon v1.9-E9.6 速赢固化（docs/SPEC_v1.9.md Part A，预登记）
# (a) 图级符号检验（对既有 20 图 overall，R3 口径）；
# (b) field_mean 种子敏感扫描（每边 4 个额外种子，纯本地）；
# (c) hybrid_norm@2.0 阴性消融（confshuffle + random-edge null×5，synthetic_null）。
# 零 API；v1.5–v1.8 代码/结果只读不改。
import json, math, os, time
import numpy as np
from deposon_diffusion import DiffusionConfig, config_dict
from run_v15_experiment import N_NEG, reconstruct_mindmap, row_normalize, mean_std
from run_v16_llm_prior import prior_score_matrix
from run_v17_fusion_fix import (norm_hybrid, prior_only, shuffle_conf_prior,
                                random_edge_prior)
from run_v19_meanfield import field_scores_init
import llm_prior

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
OUT_PATH = os.path.join(RESULTS, "deposon_v19_quickwins.json")
MULTIGRAPH_PATH = os.path.join(RESULTS, "deposon_v17_multigraph.json")
CACHE_PATH = os.path.join(RESULTS, "llm_prior_cache.json")
EXTRA_SEED_BASE = 990000          # seed = 990000 + ei*100 + s（SPEC v1.9 E9.6b）
EXTRA_SEEDS = list(range(4))
RAND_PRIOR_SEEDS = list(range(5))
CONF_SHUFFLE_SEED = 424242        # 与 v1.7.1 一致


def sign_test(diffs):
    """精确双侧符号检验：剔除平局，p = 2·Σ_{i≤min(n+,n−)} C(n,i)/2^n（封顶 1）。"""
    d = np.asarray(diffs, dtype=float)
    n_pos = int(np.sum(d > 0)); n_neg = int(np.sum(d < 0))
    n = n_pos + n_neg
    if n == 0:
        return {"n_pos": 0, "n_neg": 0, "n_tie": int(d.size), "p_exact": 1.0}
    k = min(n_pos, n_neg)
    tail = sum(math.comb(n, i) for i in range(k + 1)) / (2 ** n)
    return {"n_pos": n_pos, "n_neg": n_neg, "n_tie": int(d.size - n),
            "p_exact": min(1.0, 2 * tail)}


def graph_level_sign_tests(multigraph):
    """(a) 对 20 图 overall：random−hybrid_norm@2.0 与 hybrid_norm@2.0−field_guided。"""
    graphs = multigraph["graphs"]
    def ov(g, arm):
        return g["arms"][arm]["overall"]
    d_rh = [ov(g, "random") - ov(g, "hybrid_norm@2.0") for g in graphs]
    d_hf = [ov(g, "hybrid_norm@2.0") - ov(g, "field_guided") for g in graphs]
    return {"random_minus_hybrid_norm@2.0": sign_test(d_rh),
            "hybrid_norm@2.0_minus_field_guided": sign_test(d_hf),
            "k_graphs": len(graphs),
            "r3_reference": {"random_ge_hybrid_p": 0.0013, "hybrid_gt_field_p": 0.0075}}


def field_mean_seed_scan(cfg, adj, edges, named, W_true):
    """(b) field_mean 每边 4 个额外种子（种子驱动负池采样；场起点本身确定论）。"""
    N = adj.shape[0]
    seed_families = [("base_70000+ei", lambda ei: 70_000 + ei)] + [
        (f"extra_{EXTRA_SEED_BASE}+ei*100+{s}",
         lambda ei, s=s: EXTRA_SEED_BASE + ei * 100 + s) for s in EXTRA_SEEDS]
    per_family = []
    for fam_name, seed_fn in seed_families:
        hits, hits_named, hits_filler = [], [], []
        for ei, (u, v) in enumerate(edges):
            seed = seed_fn(ei)
            rng = np.random.default_rng(seed)
            adj_obs = adj.copy(); adj_obs[u, v] = 0.0
            W_obs = W_true.copy(); W_obs[u, v] = 0.0
            mask = np.zeros((N, N), bool); mask[u, v] = True
            pool = [j for j in range(N) if j != u and adj_obs[u, j] == 0]
            take = rng.choice(len(pool), size=min(N_NEG, len(pool)), replace=False)
            for k in take:
                mask[u, pool[k]] = True
            s = field_scores_init(W_obs, mask, cfg, 0, 1, seed, "prior_mean")
            from run_v15_experiment import top3_hit_per_edge
            h = top3_hit_per_edge(s, [(u, v)], mask)[0]["hit"]
            hits.append(float(h))
            (hits_named if (u, v) in named else hits_filler).append(float(h))
        per_family.append({"seed_family": fam_name,
                           "overall": float(np.mean(hits)),
                           "named": float(np.mean(hits_named)),
                           "filler": float(np.mean(hits_filler))})
    agg = {}
    for key in ("overall", "named", "filler"):
        vals = [f[key] for f in per_family]
        agg[key] = {"mean": float(np.mean(vals)), "sd": float(np.std(vals)),
                    "per_seed_family": vals}
    return {"per_seed_family": per_family, "across_seeds": agg,
            "note": "field_mean 起点确定论；种子仅驱动负池采样。sd 量化的是负池噪声，"
                    "v1.7.1 参照量级 ≈0.066。"}


def lambda2_null_ablation(cfg, adj, edges, named, W_true, prior):
    """(c) hybrid_norm@2.0：real vs confshuffle(N1) vs random-edge null×5(N2)。"""
    N = adj.shape[0]
    null_priors = {"confshuffle": shuffle_conf_prior(prior, CONF_SHUFFLE_SEED)}
    for s in RAND_PRIOR_SEEDS:
        null_priors[f"rand{s}"] = random_edge_prior(
            N, list(prior.values()), s)
    P_real = prior_score_matrix(prior, (N, N))
    P_null = {k: prior_score_matrix(p, (N, N)) for k, p in null_priors.items()}
    arm_names = ["real", "confshuffle"] + [f"rand{s}" for s in RAND_PRIOR_SEEDS]
    hits = {a: {"overall": [], "named": []} for a in arm_names}
    zero_row_hits = {a: [] for a in arm_names}
    for ei, (u, v) in enumerate(edges):
        rng = np.random.default_rng(70_000 + ei)
        adj_obs = adj.copy(); adj_obs[u, v] = 0.0
        W_obs = W_true.copy(); W_obs[u, v] = 0.0
        mask = np.zeros((N, N), bool); mask[u, v] = True
        pool = [j for j in range(N) if j != u and adj_obs[u, j] == 0]
        take = rng.choice(len(pool), size=min(N_NEG, len(pool)), replace=False)
        for k in take:
            mask[u, pool[k]] = True
        # 复现 E9.1 的 rng 消耗次序（random/degree 臂各一次 rng.random(mask.sum())），
        # 使 real 臂逐位复现 E9.1 的 hybrid_norm@2.0（SPEC v1.9 E9.6c 口径）。
        rng.random(int(mask.sum()))  # E9.1 random 臂
        rng.random(int(mask.sum()))  # E9.1 degree 臂
        tiebreak = rng.random(int(mask.sum()))
        fm = field_scores_init(W_obs, mask, cfg, 0, 1, 70_000 + ei, "prior_mean")
        from run_v15_experiment import top3_hit_per_edge
        for a in arm_names:
            Pa = P_real if a == "real" else P_null[a]
            s = norm_hybrid(fm, Pa, mask, 2.0, tiebreak)
            h = top3_hit_per_edge(s, [(u, v)], mask)[0]["hit"]
            hits[a]["overall"].append(float(h))
            if (u, v) in named:
                hits[a]["named"].append(float(h))
            if Pa[u].sum() == 0.0 and h:
                zero_row_hits[a].append([int(u), int(v)])
    summary = {a: {"overall": mean_std(hits[a]["overall"]),
                   "named": mean_std(hits[a]["named"]),
                   "zero_prior_row_hits": zero_row_hits[a]} for a in arm_names}
    rand_named = [summary[f"rand{s}"]["named"]["mean"] for s in RAND_PRIOR_SEEDS]
    real_named = summary["real"]["named"]["mean"]
    null_mean = float(np.mean(rand_named + [summary["confshuffle"]["named"]["mean"]]))
    verdict = bool(real_named is not None and real_named > null_mean + 0.06)
    conf_eq_real = bool(summary["confshuffle"]["named"]["mean"] == real_named)
    return {"confshuffle_equals_real_named": conf_eq_real,
            "semantic_attribution_note": (
                "confshuffle（端点不变、置信度打乱）named 与 real 完全相等 ⇒ "
                "λ=2.0 下 named 命中不可归因于语义置信度，仅能归因于端点/位置与"
                "反场 artifact；机械判据（real > 两类 null 均值 +0.06）虽通过，"
                "语义性主张仍被削弱，如实披露。" if conf_eq_real else
                "confshuffle named 低于 real，机械判据与语义口径一致。"),
            "spec": "hybrid_norm@2.0，field 分量=field_mean；N1 confshuffle（seed=424242）、"
                    "N2 random-edge null×5（synthetic_null，复用 run_v17_fusion_fix 生成器）",
            "arms": summary, "randomedge_named_per_seed": rand_named,
            "null_named_mean_incl_confshuffle": null_mean,
            "real_named": real_named,
            "real_beats_null_by_0.06": verdict,
            "interpretation": "λ>1 非凸组合（场系数 −1）：先验空行等价按场降序排反，"
                              "null 命中若集中在先验空行属反场 artifact，已逐边列出。"}


def main():
    t0 = time.time()
    cfg = DiffusionConfig()
    N, adj, edges, labels, meta = reconstruct_mindmap()
    W_true = row_normalize(adj)
    named = {tuple(e) for e in meta["path_edges_named"]}
    mg = json.load(open(MULTIGRAPH_PATH))
    sign = graph_level_sign_tests(mg)
    scan = field_mean_seed_scan(cfg, adj, edges, named, W_true)
    prior = llm_prior.load_prior(CACHE_PATH) if os.path.exists(CACHE_PATH) else None
    abl = lambda2_null_ablation(cfg, adj, edges, named, W_true, prior) if prior else None

    out = {"experiment": "deposon_v19_quickwins", "spec_version": "v1.9",
           "spec": "docs/SPEC_v1.9.md Part A E9.6",
           "config": config_dict(cfg),
           "E9_6a_sign_tests": sign,
           "E9_6b_seed_scan": scan,
           "E9_6c_lambda2_null_ablation": abl,
           "runtime_sec": round(time.time() - t0, 3),
           "honesty": [
               "零 API；只读 deposon_v17_multigraph.json 与 llm_prior_cache.json；"
               "null 先验全部 synthetic_null，不冒充 LLM。",
               "符号检验为图级（20 图），免疫 LOO 图内依赖；数值以本次重算为准。",
               "种子扫描 sd 只反映负池采样噪声（field_mean 起点确定论），不覆盖"
               "图间（语义层）方差——图 n=1 瓶颈不变（R3）。",
               "overall 上 random 稳定不低于 hybrid_norm@2.0 ⇒ 不作 overall 优效主张。",
               "负面如实；不回溯改写 v1.5–v1.8 任何表述。"]}
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({"out": OUT_PATH, "runtime_sec": out["runtime_sec"],
                      "sign": sign, "seed_scan_across": scan["across_seeds"],
                      "abl_real_named": abl and abl["real_named"],
                      "abl_null_mean": abl and abl["null_named_mean_incl_confshuffle"],
                      "abl_verdict": abl and abl["real_beats_null_by_0.06"]},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
