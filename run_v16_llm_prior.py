# -*- coding: utf-8 -*-
# ============================================================
# Deposon v1.6 LLM 语义先验实验脚本 (SPEC v1.6 §2)
#   → results/deposon_v16_llm_prior.json
#
# 假说 (用户提出): v1.5 物理场在语义边上输随机 (named_path 0.176 vs random 0.412)
#   是因为未做 LLM 集成; 纯仿物理不含语义信息。本实验在同一留一协议下比较
#   纯物理 / 纯LLM先验 / 物理×LLM融合。
#
# 协议: 完全复用实验 B 的 49 实例留一 (reconstruct_mindmap 同图, 同种子
#   70000+ei, 同 N_NEG=10 同行负采样; reconstruct_mindmap / arm_scores /
#   top3_hit_per_edge 直接 import 自 run_v15_experiment, 不复制改写其逻辑)。
#
# 六臂 (SPEC v1.6 §2):
#   field_guided   energy_mode="aggregate" 纯物理完整臂 (同 v1.5.1)
#   llm_prior      纯 LLM 语义先验分数 (confidence; 先验未覆盖的候选为 0)
#   hybrid@λ       post-hoc 融合: W_done + λ·prior_scores, λ ∈ {0.25,0.5,1,2}
#                  (预登记, 全部报告防 p-hacking)
#   random / degree  基线 (同 v1.5)
#
# 成功判据 (预登记, 写入输出 JSON): hybrid 在 named_path 子集 top-3 ≥ 0.4
#   且 > field_guided 的 named_path top-3。
#
# 无 KIMI_API_KEY 时: 非 LLM 臂照跑, JSON 标注 "llm_arms": "pending_no_key",
#   llm_prior/hybrid 臂留空, 严禁 mock 冒充真实调用结果。
# key 就位后复跑本脚本即可补齐 LLM 臂 (若 results/llm_prior_cache.json 已存在
#   则直接复用缓存, 不重复消耗 API 预算)。
# ============================================================
import json
import os
import time

import numpy as np

from deposon_diffusion import DiffusionConfig, config_dict
import llm_prior
from run_v15_experiment import (N_NEG, TOP_K, arm_scores, mean_std,
                                reconstruct_mindmap, row_normalize,
                                top3_hit_per_edge)

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
OUT_PATH = os.path.join(RESULTS, "deposon_v16_llm_prior.json")
CACHE_PATH = os.path.join(RESULTS, "llm_prior_cache.json")

LAMBDAS = (0.25, 0.5, 1.0, 2.0)          # 预登记, 全部报告
NONLLM_ARMS = ("field_guided", "random", "degree")
HYBRID_ARMS = tuple(f"hybrid@{lam}" for lam in LAMBDAS)
LLM_ARMS = ("llm_prior",) + HYBRID_ARMS
ALL_ARMS = ("field_guided", "llm_prior") + HYBRID_ARMS + ("random", "degree")
SUCCESS_NAMED_MIN = 0.4                   # 预登记成功判据阈值


# ---------------------------------------------------------------- 先验打分
# prior_score_matrix 已迁入 deposon_protocol（候选 2 重构）; 此处薄转发,
# 保持 11 个下游脚本 "from run_v16_llm_prior import prior_score_matrix" 不破。
from deposon_protocol import prior_score_matrix  # noqa: F401


def prior_arm_scores(P: np.ndarray, mask: np.ndarray,
                     tiebreak: np.ndarray) -> np.ndarray:
    """纯先验臂: 分数=confidence; 未覆盖候选=0; 1e-6 级确定性微扰破平局
    (tiebreak 由实例种子 rng 产生, 与 random/degree 臂同一破平局口径)。"""
    out = np.full(P.shape, -np.inf, dtype=float)
    out[mask] = P[mask] + 1e-6 * tiebreak
    return out


def hybrid_scores(fg_scores: np.ndarray, P: np.ndarray, mask: np.ndarray,
                  lam: float) -> np.ndarray:
    """hybrid@λ: post-hoc 融合 W_done + λ·prior_scores, 仅掩码位置参与排序。"""
    out = np.full(P.shape, -np.inf, dtype=float)
    out[mask] = fg_scores[mask] + lam * P[mask]
    return out


# ---------------------------------------------------------------- 实验 B 留一
def run_v16(cfg: DiffusionConfig, prior: dict | None) -> dict:
    """49 实例留一; 协议与 run_v15_experiment.run_experiment_B 完全一致
    (同图/同种子/同负采样), 追加 llm_prior 与 hybrid@λ 臂 (prior=None 时跳过)。"""
    N, adj, edges, labels, meta = reconstruct_mindmap()
    W_true = row_normalize(adj)
    source, target = 0, 1  # ROOT → GOAL_拓扑智能
    named_path = {tuple(e) for e in meta["path_edges_named"]}
    P = prior_score_matrix(prior, (N, N)) if prior is not None else None
    per_edge = []
    for ei, (u, v) in enumerate(edges):
        rng = np.random.default_rng(70_000 + ei)   # 与 v1.5 实验 B 同种子
        adj_obs = adj.copy()
        adj_obs[u, v] = 0.0
        W_obs = W_true.copy()
        W_obs[u, v] = 0.0
        mask = np.zeros((N, N), dtype=bool)
        mask[u, v] = True
        pool = [j for j in range(N) if j != u and adj_obs[u, j] == 0]
        take = rng.choice(len(pool), size=min(N_NEG, len(pool)), replace=False)
        for k in take:
            mask[u, pool[k]] = True
        rec = {"edge": [int(u), int(v)],
               "edge_label": [labels[u], labels[v]],
               "on_named_path": (u, v) in named_path, "arms": {}}
        scores = {}
        # 非 LLM 臂: 直接复用 v1.5 arm_scores (random/degree 消耗 rng 的顺序
        # 与 v1.5 一致 —— 中间的无 rng 消耗臂增删不影响复现)
        for arm in NONLLM_ARMS:
            scores[arm] = arm_scores(arm, W_obs, mask, cfg, source, target,
                                     adj_obs, rng, inst_seed=70_000 + ei)
        if P is not None:
            tiebreak = rng.random(int(mask.sum()))
            scores["llm_prior"] = prior_arm_scores(P, mask, tiebreak)
            for lam, h_arm in zip(LAMBDAS, HYBRID_ARMS):
                scores[h_arm] = hybrid_scores(scores["field_guided"], P, mask,
                                              lam)
        for arm, s in scores.items():
            hit = top3_hit_per_edge(s, [(u, v)], mask)[0]
            rec["arms"][arm] = {"rank": hit["rank"], "hit": hit["hit"]}
        per_edge.append(rec)

    arms = {}
    run_arms = NONLLM_ARMS + (LLM_ARMS if P is not None else ())
    for arm in run_arms:
        arms[arm] = {"top3_hit": mean_std(
            [float(r["arms"][arm]["hit"]) for r in per_edge]),
            "top3_hit_named_path": mean_std(
                [float(r["arms"][arm]["hit"]) for r in per_edge
                 if r["on_named_path"]]),
            "top3_hit_filler": mean_std(
                [float(r["arms"][arm]["hit"]) for r in per_edge
                 if not r["on_named_path"]])}
    return {"reconstruction": meta, "source": "ROOT", "target": "GOAL_拓扑智能",
            "arms": arms, "per_edge": per_edge}


# ---------------------------------------------------------------- 成功判据
def evaluate_success(exp_b: dict, llm_done: bool) -> dict:
    """预登记判据求值: hybrid 在 named_path top-3 ≥ 0.4 且 > field_guided。
    四个 λ 全部如实报告 (防 p-hacking); LLM 臂未跑时 status=pending_no_key。"""
    if not llm_done:
        return {"status": "pending_no_key",
                "note": "无 KIMI_API_KEY, LLM 臂挂起; 判据待 key 就位复跑后求值。"}
    fg_named = exp_b["arms"]["field_guided"]["top3_hit_named_path"]["mean"]
    per_lambda = {}
    for lam, h_arm in zip(LAMBDAS, HYBRID_ARMS):
        named = exp_b["arms"][h_arm]["top3_hit_named_path"]["mean"]
        per_lambda[f"lambda_{lam}"] = {
            "named_path_top3": named,
            "ge_0.4": bool(named >= SUCCESS_NAMED_MIN),
            "gt_field_guided": bool(named > fg_named),
            "pass": bool(named >= SUCCESS_NAMED_MIN and named > fg_named)}
    return {"status": "evaluated",
            "field_guided_named_path_top3": fg_named,
            "per_lambda": per_lambda,
            "any_lambda_pass": bool(any(v["pass"]
                                        for v in per_lambda.values()))}


# ---------------------------------------------------------------- main
def main():
    t0 = time.time()
    cfg = DiffusionConfig()
    N, _adj, _edges, labels, _meta = reconstruct_mindmap()

    # ---- LLM 先验: 缓存优先 (复现不重复消耗预算), 否则真实 API 调用;
    #      无 key → RuntimeError → LLM 臂挂起 (严禁 mock 冒充真实结果) ----
    prior, prior_source, prior_err = None, None, None
    if os.path.exists(CACHE_PATH):
        prior = llm_prior.load_prior(CACHE_PATH)
        prior_source = "cache"
    else:
        try:
            prior = llm_prior.call_llm_prior(CACHE_PATH, labels=labels)
            prior_source = "live_api"
        except RuntimeError as e:
            prior_err = str(e)  # 消息已经 _sanitize, 不含 key
    llm_done = prior is not None

    exp_b = run_v16(cfg, prior)
    success = evaluate_success(exp_b, llm_done)
    runtime = time.time() - t0

    b_all = {a: exp_b["arms"][a]["top3_hit"]["mean"] for a in exp_b["arms"]}
    b_named = {a: exp_b["arms"][a]["top3_hit_named_path"]["mean"]
               for a in exp_b["arms"]}
    b_fill = {a: exp_b["arms"][a]["top3_hit_filler"]["mean"]
              for a in exp_b["arms"]}

    honesty = [
        "本实验只复用 v1.5 实验 B 的留一协议 (同图/同种子 70000+ei/同负采样), "
        "reconstruct_mindmap/arm_scores/top3_hit_per_edge 直接 import, 未改写其逻辑。",
        "零泄漏: LLM 只见 45 个节点标签, prompt 不含任何边/图结构信息 "
        "(build_prior_prompt 输入仅有标签列表)。",
        "API key 仅从环境变量 KIMI_API_KEY 读取, 不写入任何文件/日志/异常消息; "
        "LLM 调用预算 ≤2 次 (全局先验 1 次 + 必要时重试 1 次)。",
        "hybrid 为 post-hoc 融合 W_done + λ·prior_scores, λ∈{0.25,0.5,1,2} "
        "预登记并全部报告, 不挑 λ。",
        "全部指标由种子固定的实际运行产生, 含负面结果, 无任何手工润色; "
        "严禁 mock 冒充真实 LLM 调用结果。",
    ]
    if llm_done:
        honesty.append(
            f"LLM 先验来源: {prior_source} (cache=results/llm_prior_cache.json "
            f"复用, live_api=本次真实调用), 先验边数={len(prior)}。")
        honesty.append(
            f"成功判据求值: field_guided named_path={b_named['field_guided']:.3f}; "
            + "; ".join(
                f"λ={lam}: named={b_named[h]:.3f} "
                f"{'PASS' if success['per_lambda'][f'lambda_{lam}']['pass'] else 'fail'}"
                for lam, h in zip(LAMBDAS, HYBRID_ARMS))
            + f"。overall any_lambda_pass={success['any_lambda_pass']}。")
    else:
        honesty.append(
            f"LLM 臂挂起 (pending_no_key): {prior_err}。本次仅产出 "
            f"field_guided/random/degree 三个非 LLM 臂, llm_prior 与 hybrid@λ "
            f"臂留空; 这不是实验结果缺失的修饰, key 就位后复跑本脚本即可补齐。")
        honesty.append(
            f"非 LLM 臂实测 (与 v1.5.1 同协议应可复现): field_guided "
            f"top3={b_all['field_guided']:.3f} named={b_named['field_guided']:.3f} "
            f"filler={b_fill['field_guided']:.3f}; random "
            f"top3={b_all['random']:.3f} named={b_named['random']:.3f}; degree "
            f"top3={b_all['degree']:.3f} named={b_named['degree']:.3f}。")

    out = {
        "experiment": "deposon_v16_llm_prior",
        "spec": "SPEC v1.6 (LLM 语义先验集成 —— 纯物理/纯LLM/物理×LLM 融合比较)",
        "spec_version": "v1.6",
        "config": config_dict(cfg),
        "arms": list(ALL_ARMS),
        "llm_arms": "completed" if llm_done else "pending_no_key",
        "llm_prior": {
            "source": prior_source,
            "cache_path": "results/llm_prior_cache.json",
            "n_prior_edges": (len(prior) if llm_done else 0),
            "model": llm_prior.MODEL,
            "endpoint": llm_prior.ENDPOINT,
            "error": prior_err,
            "note": "key 仅从环境变量读取; 缓存存在则复用, 不重复消耗 API 预算 "
                    "(≤2 次)。"},
        "protocol": {"top_k": TOP_K, "n_negatives_per_gold_edge": N_NEG,
                     "seed_B_per_edge": "70000+edge_index",
                     "weighting": "W_true[i,j]=1/outdeg(i) 行归一; 留一边置零不重归一",
                     "mask": "留一真边 + 同行采样负目标 (同 v1.5 实验 B, 无泄漏)",
                     "hybrid": "W_done + λ·prior_scores (post-hoc, 仅掩码位置排序)",
                     "prior_zero_leakage": "LLM 只见节点标签, 不见任何边/结构"},
        "success_criteria_preregistered": {
            "rule": "hybrid (λ∈{0.25,0.5,1,2}, 预登记全报) 在 named_path 子集 "
                    "top-3 ≥ 0.4 且 > field_guided 的 named_path top-3",
            "lambdas": list(LAMBDAS),
            "named_path_min": SUCCESS_NAMED_MIN,
            "reference_v151_field_guided_named": 0.176},
        "success_evaluation": success,
        "runtime_sec": round(runtime, 3),
        "experiment_B": exp_b,
        "honesty": honesty,
    }
    os.makedirs(RESULTS, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"written {OUT_PATH}  runtime={runtime:.1f}s  "
          f"llm_arms={out['llm_arms']}")
    for arm in exp_b["arms"]:
        b = exp_b["arms"][arm]
        print(f"  {arm:16s} top3={b['top3_hit']['mean']:.3f} "
              f"named={b['top3_hit_named_path']['mean']:.3f} "
              f"filler={b['top3_hit_filler']['mean']:.3f}")
    if not llm_done:
        print(f"  [pending] llm_prior/hybrid@λ: {prior_err}")


if __name__ == "__main__":
    main()
