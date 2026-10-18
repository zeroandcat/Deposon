# -*- coding: utf-8 -*-
# GT-3a 跨评估者先验评估（docs/SPEC_GT3.md，判定机械求值）
#   → results/deposon_v20_gt3.json
# no LLM API calls issued：只读 results/gt3_prior_cache 与 familyL_prior_cache。
import json
import math
import os

import numpy as np

from deposon_diffusion import DiffusionConfig
from llm_prior import _extract_json_array, _validate_prior
from mindmap_corpus_v20 import CORPUS_DIR, FAMILY_L_DOMAINS, load_corpus
from run_v20_crossval_eval import eval_prior_arm

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
GT3_DIR = os.path.join(RESULTS, "gt3_prior_cache")
BASE_DIR = os.path.join(RESULTS, "familyL_prior_cache")
OUT_PATH = os.path.join(RESULTS, "deposon_v20_gt3.json")

EVALUATORS = {"E0_kimi-for-coding": BASE_DIR, "E1_moonshot-v1-8k": GT3_DIR,
              "E2_kimi-k2-thinking": GT3_DIR,
              "E3_doubao-seed-evolving": GT3_DIR,
              "E4_deepseek-v4-pro": GT3_DIR}
CACHE_NAME = {"E0_kimi-for-coding": lambda d: f"{d}.json",
              "E1_moonshot-v1-8k": lambda d: f"moonshot-v1-8k__{d}.json",
              "E2_kimi-k2-thinking": lambda d: f"kimi-k2-thinking__{d}.json",
              "E3_doubao-seed-evolving": lambda d: f"doubao-seed-evolving__{d}.json",
              "E4_deepseek-v4-pro": lambda d: f"deepseek-v4-pro-260425__{d}.json"}


def load_prior(eval_key, domain, n):
    path = os.path.join(EVALUATORS[eval_key], CACHE_NAME[eval_key](domain))
    rec = json.load(open(path, encoding="utf-8"))
    if rec.get("prompt_mismatch"):
        return None, rec, "prompt_mismatch"
    if not rec.get("response_text"):
        return None, rec, "fetch_failed"
    try:
        items = _extract_json_array(rec["response_text"])
        prior = _validate_prior(items, n)
    except Exception as e:
        return None, rec, f"parse_failure:{type(e).__name__}"
    return prior, rec, "ok"


def kendall_w(rank_matrix):
    """rank_matrix: m 评估者 × n 域的名次矩阵（1=最好）。返回 W∈[0,1]。"""
    ranks = np.asarray(rank_matrix, dtype=float)
    m, n = ranks.shape
    col_sums = ranks.sum(axis=0)
    mean_sum = col_sums.mean()
    S = float(((col_sums - mean_sum) ** 2).sum())
    return 12.0 * S / (m ** 2 * (n ** 3 - n))


def main():
    cfg = DiffusionConfig()
    graphs = {g["graph_id"].replace("L_", ""): g
              for g in load_corpus(CORPUS_DIR, families=("L",))}
    per, failures, total_attempts = [], {}, 0
    for domain in FAMILY_L_DOMAINS:
        g = graphs[domain]
        row = {"domain": domain, "evaluators": {}}
        for ekey in EVALUATORS:
            prior, rec, status = load_prior(ekey, domain, g["N"])
            total_attempts += int(rec.get("attempts", 0) or 0)
            if status != "ok":
                failures[f"{ekey}__{domain}"] = status
                row["evaluators"][ekey] = {"status": status,
                                           "named_hits3": None}
                continue
            res = eval_prior_arm(g, prior, cfg)
            row["evaluators"][ekey] = {
                "status": "ok",
                "named_hits3": res["llm_prior"]["named"],
                "filler_hits3": res["llm_prior"]["filler"],
                "field_mean_named_hits3": res["field_mean"]["named"],
                "attempts": int(rec.get("attempts", 0) or 0)}
        per.append(row)

    # ---- 判定（SPEC §1 机械求值）----
    new_evals = ("E1_moonshot-v1-8k", "E2_kimi-k2-thinking",
                 "E3_doubao-seed-evolving", "E4_deepseek-v4-pro")
    crit1 = {}
    for ekey in new_evals:
        wins = sum(1 for r in per
                   if (r["evaluators"][ekey]["named_hits3"] is not None
                       and r["evaluators"][ekey]["field_mean_named_hits3"] is not None
                       and r["evaluators"][ekey]["named_hits3"]
                       > r["evaluators"][ekey]["field_mean_named_hits3"]))
        losses = sum(1 for r in per
                     if (r["evaluators"][ekey]["named_hits3"] is not None
                         and r["evaluators"][ekey]["field_mean_named_hits3"] is not None
                         and r["evaluators"][ekey]["named_hits3"]
                         <= r["evaluators"][ekey]["field_mean_named_hits3"]))
        crit1[ekey] = {"domains_prior_gt_field": wins,
                       "domains_prior_le_field": losses,
                       "criterion_pass_ge4of6": wins >= 4,
                       "kill_triggered_ge3of6": losses >= 3}
    # W：仅三评估者均 ok 的域
    ok_domains = [r for r in per
                  if all(r["evaluators"][e]["status"] == "ok"
                         for e in EVALUATORS)]
    W = None
    if len(ok_domains) >= 3:
        from scipy.stats import rankdata
        vals = np.array([[r["evaluators"][e]["named_hits3"]
                          for r in ok_domains] for e in EVALUATORS])
        # 每个评估者对「域」排名（含 ties 平均名次），跨评估者求和谐系数
        rank_mat = np.array([rankdata(row) for row in vals])
        W = kendall_w(rank_mat)
    kill = any(c["kill_triggered_ge3of6"] for c in crit1.values())
    supported = (not kill and W is not None and W >= 0.5
                 and all(c["criterion_pass_ge4of6"] for c in crit1.values()))
    out = {"experiment": "deposon_v20_gt3", "spec": "docs/SPEC_GT3.md",
           "spec_frozen_before_data": "2026-08-30",
           "per_domain": per, "failures": failures,
           "criteria": crit1, "kendall_W": W,
           "n_domains_all_evaluators_ok": len(ok_domains),
           "verdict": {"H_GT3_supported": supported,
                       "H_GT3_dead_triggered": kill},
           "budget": {"preregistered_max": 27,
                      "probe_attempts": 3,
                      "fetch_attempts_recorded_in_caches": total_attempts,
                      "ark_gt3b_attempts": {"doubao": 12, "deepseek": 8, "probes": 3},
                      "actual_total_attempts": 28,
                      "overrun": 1,
                      "note": "修正案 A1：重试轮如实计数致超支 1 次，已披露"},
           "honesty": [
               "GT-3b 已升级为三模型族（Moonshot/ByteDance/DeepSeek）；原声明：降级为族内跨评估者（GT-3a）：生成者 kimi-for-coding，评估者为"
               "同厂商不同代际/推理模式模型；不能完全排除同厂商同源污染，"
               "GT-3b（跨厂商）待资源。",
               "parse/fetch 失败域不静默剔除，单独披露于 failures。",
               "prompt 与既有先验臂逐字节相同（prompt_sha256 校验），"
               "评估协议与 run_v20_crossval_eval 逐位相同。"]}
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps(out["verdict"], ensure_ascii=False))
    print(f"W={W} failures={failures} attempts={total_attempts}")


if __name__ == "__main__":
    main()
