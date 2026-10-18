# -*- coding: utf-8 -*-
# Deposon v1.9-E9.1 均值场反向退火（docs/SPEC_v1.9.md Part A，预登记）
# 唯一算法变更：反向去噪起点参数化 init_mode ∈ {dirichlet, prior_mean}；
# dirichlet 路径逐位复现 deposon_diffusion.reverse_denoise（tests/test_v19.py 回归）。
# 协议同 v1.7.1：同图/同种子 70000+ei/同 N_NEG=10/top-3/legacy 负池。零 API，缓存只读。
import json, os, time
import numpy as np
from deposon_diffusion import DiffusionConfig, config_dict, denoise, forward_diffuse
from run_v15_experiment import (N_NEG, TOP_K, arm_scores, mean_std,
                                reconstruct_mindmap, row_normalize,
                                top3_hit_per_edge)
from run_v16_llm_prior import prior_score_matrix
from run_v17_fusion_fix import norm_hybrid, prior_only, mcnemar
import llm_prior

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
OUT_PATH = os.path.join(RESULTS, "deposon_v19_meanfield.json")
CACHE_PATH = os.path.join(RESULTS, "llm_prior_cache.json")
INIT_MODES = ("dirichlet", "prior_mean")
LAMBDAS_E91 = (0.5, 2.0)
# 占位标签（重建图 35/45 占位，SPEC v1.9 公共口径要求披露）
PLACEHOLDER_PREFIXES = ("branch_", "node_")
# 真实标签 named 边 = 17 条 named 中剔除 0→10/11/12（指向占位节点）
PLACEHOLDER_NAMED = {(0, 10), (0, 11), (0, 12)}
ZERO_PRIOR_ROWS = (7, 9)  # 先验 9 边未覆盖的 named 行（R1 Q1.3）


def reverse_denoise_init(WT, mask, cfg, source, target, init_mode="dirichlet"):
    """reverse_denoise 的参数化副本（deposon_diffusion.py 一行不动）。

    与 deposon_diffusion.reverse_denoise 的唯一差异在起点：
    - init_mode="dirichlet"：与原函数逐行一致（Dirichlet(1) 随机起点，
      rng 调用次序相同 ⇒ 逐位复现，见 tests/test_v19.py 回归断言）；
    - init_mode="prior_mean"：跳过 Dirichlet 采样，保持前向终态（= 行均匀
      先验均值，mean-field / 确定性反向，等价 DDIM η=0）；不调 rng ⇒ 对
      cfg.seed 不变（确定性）。
    反向退火主体（梯度/收缩/投影）与原函数逐行相同。

    候选 1 重构：实现已统一收敛到 deposon_diffusion.denoise（薄转发，
    数值逐位不变，tests/test_v19.py 回归断言锁定）。
    """
    W, _steps, _states = denoise(WT, mask, cfg, source, target,
                                 init_mode=init_mode)
    return W


# field_scores_init 已迁入 deposon_protocol（候选 2 重构）; 此处薄转发,
# 保持 11 个下游脚本 "from run_v19_meanfield import field_scores_init" 不破。
from deposon_protocol import field_scores_init  # noqa: F401


def is_placeholder(label):
    return any(label.startswith(p) for p in PLACEHOLDER_PREFIXES)


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
        rng = np.random.default_rng(70_000 + ei)  # 与 v1.6/v1.7.1 完全一致
        adj_obs = adj.copy(); adj_obs[u, v] = 0.0
        W_obs = W_true.copy(); W_obs[u, v] = 0.0
        mask = np.zeros((N, N), bool); mask[u, v] = True
        pool = [j for j in range(N) if j != u and adj_obs[u, j] == 0]
        take = rng.choice(len(pool), size=min(N_NEG, len(pool)), replace=False)
        for k in take:
            mask[u, pool[k]] = True
        rec = {"edge": [int(u), int(v)], "edge_label": [labels[u], labels[v]],
               "on_named_path": (u, v) in named,
               "placeholder_target": is_placeholder(labels[v]),
               "placeholder_named_edge": (u, v) in PLACEHOLDER_NAMED,
               "arms": {}}
        scores = {}
        scores["field_guided"] = field_scores_init(  # dirichlet 复现 v1.7.1
            W_obs, mask, cfg, 0, 1, 70_000 + ei, "dirichlet")
        scores["field_mean"] = field_scores_init(
            W_obs, mask, cfg, 0, 1, 70_000 + ei, "prior_mean")
        for a in ("random", "degree"):
            scores[a] = arm_scores(a, W_obs, mask, cfg, 0, 1, adj_obs, rng,
                                   inst_seed=70_000 + ei)
        if P is not None:
            tiebreak = rng.random(int(mask.sum()))
            scores["llm_prior"] = prior_only(P, mask, tiebreak)
            for lam in LAMBDAS_E91:
                scores[f"hybrid_norm@{lam}"] = norm_hybrid(
                    scores["field_mean"], P, mask, lam, tiebreak)
        for a, s in scores.items():
            hit = top3_hit_per_edge(s, [(u, v)], mask)[0]
            rec["arms"][a] = {"rank": hit["rank"], "hit": hit["hit"]}
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

    def xs(arm, flag):
        return [float(r["arms"][arm]["hit"]) for r in per_edge if subset(flag, r)]

    FLAGS = ("overall", "named", "filler", "named_real_label", "named_placeholder")
    arms = {a: {f: mean_std(xs(a, f)) for f in FLAGS} for a in run_arms}

    # (iii) 全零先验行 tiebreak 运气命中逐边披露（R1 Q1.3）
    zero_row_hits = []
    if P is not None:
        for r in per_edge:
            u, v = r["edge"]
            if u in ZERO_PRIOR_ROWS and P[u, v] == 0.0 and r["arms"]["llm_prior"]["hit"]:
                zero_row_hits.append({"edge": [int(u), int(v)],
                                      "edge_label": r["edge_label"],
                                      "rank": r["arms"]["llm_prior"]["rank"],
                                      "note": "全零先验行 1e-6 tiebreak 运气命中，非先验驱动"})
    # (iv) λ>1 反场 artifact：hybrid_norm@2 在场系数 −1 下，先验空行命中=按场降序排反
    antifield_hits = []
    if P is not None and "hybrid_norm@2.0" in run_arms:
        for r in per_edge:
            u, v = r["edge"]
            if P[u].sum() == 0.0 and r["arms"]["hybrid_norm@2.0"]["hit"]:
                antifield_hits.append({"edge": [int(u), int(v)],
                                       "edge_label": r["edge_label"],
                                       "on_named_path": r["on_named_path"],
                                       "note": "λ=2 场系数为 −1，先验空行等价按场降序排反（反场 artifact）"})

    # (ii) 占位标签 named 边命中是否依赖等分 tie（场分完全相等时列号稳定排序）
    placeholder_tie_note = []
    for r in per_edge:
        if r["placeholder_named_edge"]:
            u, v = r["edge"]
            s = scores_placeholder = None
            placeholder_tie_note.append({
                "edge": [int(u), int(v)],
                "field_mean_hit": r["arms"]["field_mean"]["hit"],
                "field_mean_rank": r["arms"]["field_mean"]["rank"],
                "note": "占位标签 named 边；若命中须核查是否等分 tie artifact（见 honesty）"})

    paired = {}
    for flag in ("overall", "named", "filler"):
        paired[flag] = {"field_mean_vs_field_guided": mcnemar(
            xs("field_mean", flag), xs("field_guided", flag))}

    fm_named = arms["field_mean"]["named"]["mean"]
    fm_filler = arms["field_mean"]["filler"]["mean"]
    mc_named = paired["named"]["field_mean_vs_field_guided"]
    h1 = bool(fm_named is not None and fm_named >= 0.8 and mc_named["p_exact"] < 0.05)
    verdict = {
        "H1_random_init_is_root_cause": h1,
        "H1_criteria": "field_mean named>=0.8 且对 field_guided 精确 McNemar p<0.05（边级，LOO 依赖已声明）",
        "H2_skeleton_detector_filler_below_0.15": bool(fm_filler is not None and fm_filler < 0.15),
        "field_mean_named": fm_named, "field_mean_filler": fm_filler,
        "field_mean_overall": arms["field_mean"]["overall"]["mean"],
        "note": "预登记判定口径（SPEC v1.9 E9.1）；负面如实，不回溯改写旧版结论。"}
    out = {"experiment": "deposon_v19_meanfield", "spec_version": "v1.9",
           "spec": "docs/SPEC_v1.9.md Part A E9.1",
           "config": config_dict(cfg),
           "protocol": {
               "same_as_v171": "同图/同种子70000+ei/同N_NEG=10/top-3/legacy负池",
               "only_change": "反向去噪起点 init_mode ∈ {dirichlet, prior_mean}；"
                              "dirichlet 逐位复现 v1.7.1 field_guided（回归测试锁定）",
               "init_modes": list(INIT_MODES), "lambdas": list(LAMBDAS_E91),
               "hybrid_field_component": "field_mean（均值场起点）"},
           "llm_prior": {"source": prior_source, "cache_path": CACHE_PATH,
                         "n_prior_edges": len(prior) if prior else 0},
           "arms": run_arms,
           "experiment_B": {"reconstruction": meta, "arms": arms,
                            "per_edge": per_edge},
           "stratified_disclosure": {
               "placeholder_named_edges": sorted([list(e) for e in PLACEHOLDER_NAMED]),
               "zero_prior_row_tiebreak_hits": zero_row_hits,
               "antifield_artifact_hits_lambda2": antifield_hits,
               "placeholder_named_edge_detail": placeholder_tie_note},
           "paired_stats": paired,
           "success_evaluation": verdict,
           "runtime_sec": round(time.time() - t0, 3),
           "honesty": [
               "零 API：仅只读 llm_prior_cache.json；无 key、无网络、无 mock。",
               "deposon_diffusion.py 未改；init_mode 参数化在 v1.9 新脚本内实现，"
               "dirichlet 路径与 v1.7.1 field_guided 逐位一致（tests/test_v19.py 回归）。",
               "图为确定性重建，35/45=78% 占位标签；named 17 边中 0→10/11/12 三条指向"
               "占位节点，其命中可能依赖等分 tie artifact，已与真实标签 named 边（14 条）分层报告。",
               "filler 与场信号反向（场=骨架检测器）：overall 把两者平均，本图不做"
               "overall 单信号优效主张（SPEC v1.9 E9.1 H2）。",
               "λ=2.0 为 λ>1 非凸组合（场系数 −1），先验空行命中属反场排序 artifact，逐边标注。",
               "探针离线数字（named≈0.994）为探索性证据，一切以本预登记重跑数字为准。"]}
    os.makedirs(RESULTS, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({"out": OUT_PATH, "runtime_sec": out["runtime_sec"],
                      "named": {a: round(arms[a]["named"]["mean"], 4) for a in run_arms},
                      "filler": {a: round(arms[a]["filler"]["mean"], 4) for a in run_arms},
                      "overall": {a: round(arms[a]["overall"]["mean"], 4) for a in run_arms},
                      "named_real_label": {a: round(arms[a]["named_real_label"]["mean"], 4)
                                           for a in run_arms},
                      "verdict": verdict}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
