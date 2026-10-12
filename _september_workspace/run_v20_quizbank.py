# -*- coding: utf-8 -*-
# Deposon v2.0 题库横向验证（bloom-quiz-maker 题型规范 × GT-2 攻击者干扰项）
#   → results/quizbank_v20.json（题库）+ results/deposon_v20_quiz_eval.json（各臂成绩）
#
# 题型（bloom L2 理解/L4 分析）：给定源概念标签，从 4 个候选中选出语义上
# 最合理的后继概念（有向金边）。干扰项 = GT-2 自适应攻击者标签（绕过关键词
# 表的语义陷阱，已缓存）+ 图内随机节点。
# 臂：llm_prior（argmax 先验置信度）/ field_mean（argmax 场分）/ rule_filter
# （过滤后按候选序）/ random（种子化）。no LLM API calls issued：全部读缓存。
import json
import os
import time

import numpy as np

from deposon_diffusion import DiffusionConfig, config_dict
from mindmap_corpus_v20 import CORPUS_DIR, FAMILY_L_DOMAINS, load_corpus
from llm_prior import _extract_json_array, _validate_prior
from run_v15_experiment import row_normalize
from run_v16_llm_prior import prior_score_matrix
from run_v19_fullrank import full_candidate_mask
from run_v19_meanfield import field_scores_init
from run_v20_corpus_eval import RULE_KEYWORDS

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
QUIZ_PATH = os.path.join(RESULTS, "quizbank_v20.json")
EVAL_PATH = os.path.join(RESULTS, "deposon_v20_quiz_eval.json")
N_ITEMS_PER_MAP = 10
BANK_SEED = 20260828


def load_json(p):
    return json.load(open(p, encoding="utf-8"))


def build_bank(graphs):
    """按 bloom 规范建题库：stem=源标签，4 选项（1 金 + 2 攻击者陷阱 + 1 图内随机）。"""
    rng = np.random.default_rng(BANK_SEED)
    bank = []
    for domain, g in graphs.items():
        labels = g["labels"]
        named = [tuple(e) for e in g["named_edges"]]
        atk = load_json(os.path.join(RESULTS, "gt2_attacker_cache", f"{domain}.json"))
        traps = [str(it["label"]) for it in _extract_json_array(atk["response_text"])]
        take = rng.choice(len(named), size=min(N_ITEMS_PER_MAP, len(named)),
                      replace=False)
        for k in take:
            u, v = named[int(k)]
            others = [j for j in range(g["N"]) if j != v]
            decoy_node = int(others[rng.integers(len(others))])
            tpair = [traps[(2 * k) % len(traps)], traps[(2 * k + 1) % len(traps)]]
            options = [labels[v], tpair[0], tpair[1], labels[decoy_node]]
            perm = rng.permutation(4)
            bank.append({
                "item_id": f"{domain}#q{int(k):02d}",
                "domain": domain, "bloom_level": "L4_analyze",
                "question_type": "single_choice",
                "stem": f"在概念体系「{domain}」中，与「{labels[u]}」存在最直接"
                        f"合理后继关系的是哪一个？",
                "source_label": labels[u], "gold_label": labels[v],
                "gold_edge": [int(u), int(v)],
                "options": [options[int(i)] for i in perm],
                "answer_index": int(np.flatnonzero(perm == 0)[0]),
                "distractor_provenance": {
                    "trap_labels": tpair,
                    "source": "gt2_attacker_cache（自适应绕过关键词表的语义陷阱）",
                    "random_node_label": labels[decoy_node]},
                "difficulty": "中等",
                "analysis": "金边来自脑图 named 骨架；干扰项为红队生成的语义误导"
                            "（错误归类/年代错位/因果倒置）。"})
    return bank


def answer_quiz(graph, prior, cfg, bank):
    """四臂作答：返回逐题正误。choices 映射到图节点/陷阱标签字符串。"""
    N = graph["N"]
    labels = graph["labels"]
    adj = np.zeros((N, N))
    for (u, v) in [tuple(e) for e in graph["edges"]]:
        adj[u, v] = 1.0
    W_true = row_normalize(adj)
    P = prior_score_matrix(prior, (N, N)) if prior else None
    g_seed = int(graph["seed"])
    records = []
    for item in bank:
        u, v = item["gold_edge"]
        rng = np.random.default_rng(g_seed * 97 + hash(item["item_id"]) % 1000)
        adj_obs = adj.copy(); adj_obs[u, v] = 0.0
        W_obs = W_true.copy(); W_obs[u, v] = 0.0
        mask = full_candidate_mask(N, u)
        fm = field_scores_init(W_obs, mask, cfg, graph["source"], graph["target"],
                               g_seed + (u * 131 + v) % 100000, "prior_mean")
        # 候选：金节点 v + 其他图内节点（陷阱标签不在图内，field/prior 对其
        # 打分为 -inf ⇒ 场与先验天然不被标签陷阱骗，如实机制）
        scores = {}
        scores["field_mean"] = {labels[j]: float(fm[u][j]) for j in range(N)
                                if j != u}
        if P is not None:
            scores["llm_prior"] = {labels[j]: float(P[u][j]) for j in range(N)
                                   if j != u}
        opts = item["options"]
        ans = {}
        for arm in ("field_mean", "llm_prior"):
            if arm not in scores:
                ans[arm] = None
                continue
            best, best_s = None, -np.inf
            for o in opts:
                s = scores[arm].get(o, -np.inf)
                if s > best_s:
                    best, best_s = o, s
            ans[arm] = best
        # rule_filter：过滤含关键词选项后取首项（规则无排序信号，如实口径）
        surviving = [o for o in opts
                     if not any(k in o.lower() for k in RULE_KEYWORDS)]
        ans["rule_filter"] = surviving[0] if surviving else opts[0]
        ans["random"] = opts[int(rng.integers(4))]
        gold = item["options"][item["answer_index"]]
        records.append({"item_id": item["item_id"],
                        "gold": gold,
                        "answers": ans,
                        "correct": {a: (ans[a] == gold if ans[a] else None)
                                    for a in ans},
                        "note": "陷阱标签不在图节点集内：field/prior 对其打 -inf，"
                                "不被骗是机制性免疫而非语义判断，如实披露"})
    arms = ("llm_prior", "field_mean", "rule_filter", "random")
    acc = {a: float(np.mean([r["correct"][a] for r in records
                             if r["correct"][a] is not None]))
           for a in arms}
    return {"accuracy": acc, "n_items": len(records), "records": records}


def main():
    t0 = time.time()
    cfg = DiffusionConfig()
    graphs = {d: g for d, g in
              ((x["graph_id"][2:], x) for x in load_corpus(CORPUS_DIR, families=("L",)))}
    bank = build_bank(graphs)
    quiz_eval = {}
    for domain, g in graphs.items():
        rec = load_json(os.path.join(RESULTS, "familyL_prior_cache", f"{domain}.json"))
        prior = _validate_prior(_extract_json_array(rec["response_text"]), g["N"])
        items = [q for q in bank if q["domain"] == domain]
        quiz_eval[domain] = answer_quiz(g, prior, cfg, items)

    with open(QUIZ_PATH, "w", encoding="utf-8") as f:
        json.dump({"quizbank": "v20", "spec": "bloom-quiz-maker 题型规范 × "
                                              "gt2_attacker_cache 干扰项",
                   "n_items": len(bank), "bloom_level": "L4_analyze",
                   "items": bank}, f, ensure_ascii=False, indent=1)
    out = {"experiment": "deposon_v20_quiz_eval", "spec_version": "v2.0",
           "config": config_dict(cfg),
           "quizbank_path": QUIZ_PATH, "n_items": len(bank),
           "per_domain": quiz_eval,
           "overall": {a: float(np.mean([v["accuracy"][a]
                                         for v in quiz_eval.values()]))
                       for a in ("llm_prior", "field_mean", "rule_filter", "random")},
           "runtime_sec": round(time.time() - t0, 3),
           "honesty": [
               "no LLM API calls issued：题库由缓存攻击者标签与本机构建，作答全部本地。",
               "机制性免疫披露：陷阱标签不在图节点集内，field_mean/llm_prior 对其打 -inf，"
               "不被骗是排序对象域的机制结果，不等价于语义识别能力；rule_filter 的渗漏"
               "（GT-2）才是标签攻击的真实战场。",
               "题库仅供横向对比（题型效度），不作为独立基准主张。",
               "判定机械求值，负面如实。"]}
    with open(EVAL_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({"overall": out["overall"],
                      "per_domain": {d: v["accuracy"] for d, v in quiz_eval.items()}},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
