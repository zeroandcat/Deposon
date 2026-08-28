# -*- coding: utf-8 -*-
# v2.0 大型题库验证（bloom 题型 × 攻击者扩池干扰项，6 域全覆盖）
#   → results/quizbank_v20_big.json（大题库）+ results/deposon_v20_bigquiz_eval.json
# 规模：6 域全部 named 边逐边一题（~160 题，4 倍于 v20 小题库 40 题）。
# 干扰项：attacker_xl_cache（40 标签/域自适应陷阱）×2 + 图内随机节点 ×1。
# 臂：llm_prior / field_mean / rule_filter / ngram_tfidf（BOSS 常驻臂）/ random。
# CoT 臂：复用 cot_quiz_cache（4 旧域抽样题），按 gold_edge 映射到大题库。
# no LLM API calls issued：全部读缓存。
import json
import os
import time

import numpy as np

from deposon_diffusion import DiffusionConfig, config_dict
from mindmap_corpus_v20 import CORPUS_DIR, load_corpus
from llm_prior import _extract_json_array, _validate_prior
from run_v15_experiment import row_normalize
from run_v16_llm_prior import prior_score_matrix
from run_v19_fullrank import full_candidate_mask
from run_v19_meanfield import field_scores_init
from run_v20_corpus_eval import RULE_KEYWORDS
from run_v20_baselines import ngram_tfidf_cosine_row

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
BANK_PATH = os.path.join(RESULTS, "quizbank_v20_big.json")
EVAL_PATH = os.path.join(RESULTS, "deposon_v20_bigquiz_eval.json")
BANK_SEED = 20260829
ARMS = ("llm_prior", "field_mean", "ngram_tfidf", "rule_filter", "random")


def build_big_bank(graphs):
    rng = np.random.default_rng(BANK_SEED)
    bank = []
    for domain, g in graphs.items():
        labels = g["labels"]
        named = [tuple(e) for e in g["named_edges"]]
        atk = json.load(open(os.path.join(RESULTS, "attacker_xl_cache",
                                          f"{domain}.json"), encoding="utf-8"))
        traps = [str(it["label"]) for it in _extract_json_array(atk["response_text"])]
        for k, (u, v) in enumerate(named):
            others = [j for j in range(g["N"]) if j != v]
            decoy = int(others[rng.integers(len(others))])
            tpair = [traps[(2 * k) % len(traps)], traps[(2 * k + 1) % len(traps)]]
            options = [labels[v], tpair[0], tpair[1], labels[decoy]]
            perm = rng.permutation(4)
            bank.append({
                "item_id": f"{domain}#e{k:03d}", "domain": domain,
                "bloom_level": "L4_analyze", "question_type": "single_choice",
                "stem": f"在概念体系「{domain}」中，与「{labels[u]}」存在最直接"
                        f"合理后继关系的是哪一个？",
                "gold_edge": [int(u), int(v)],
                "options": [options[int(i)] for i in perm],
                "answer_index": int(np.flatnonzero(perm == 0)[0]),
                "distractor_provenance": {
                    "trap_labels": tpair, "source": "attacker_xl_cache（40/域扩池）",
                    "random_node_label": labels[decoy]}})
    return bank


def eval_domain(graph, prior, cfg, items):
    N = graph["N"]
    labels = graph["labels"]
    adj = np.zeros((N, N))
    for (u, v) in [tuple(e) for e in graph["edges"]]:
        adj[u, v] = 1.0
    W_true = row_normalize(adj)
    P = prior_score_matrix(prior, (N, N)) if prior else None
    g_seed = int(graph["seed"])
    recs = []
    for it in items:
        u, v = it["gold_edge"]
        rng = np.random.default_rng(g_seed * 97 + (u * 131 + v) % 1000)
        adj_obs = adj.copy(); adj_obs[u, v] = 0.0
        W_obs = W_true.copy(); W_obs[u, v] = 0.0
        mask = full_candidate_mask(N, u)
        cand = np.flatnonzero(mask[u])
        fm = field_scores_init(W_obs, mask, cfg, graph["source"], graph["target"],
                               g_seed + (u * 131 + v) % 100000, "prior_mean")
        tf = ngram_tfidf_cosine_row(labels, u, cand)
        opts = it["options"]
        ans = {}
        for arm in ("field_mean", "llm_prior", "ngram_tfidf"):
            if arm == "llm_prior" and P is None:
                ans[arm] = None
                continue
            scores = {}
            if arm == "field_mean":
                scores = {labels[j]: float(fm[u][j]) for j in cand}
            elif arm == "llm_prior":
                scores = {labels[j]: float(P[u][j]) for j in cand}
            else:
                scores = {labels[j]: float(tf[j]) for j in cand}
            best, bs = None, -np.inf
            for o in opts:
                sv = scores.get(o, -np.inf)
                if sv > bs:
                    best, bs = o, sv
            ans[arm] = best
        surviving = [o for o in opts
                     if not any(k in o.lower() for k in RULE_KEYWORDS)]
        ans["rule_filter"] = surviving[0] if surviving else opts[0]
        ans["random"] = opts[int(rng.integers(4))]
        gold = opts[it["answer_index"]]
        recs.append({"item_id": it["item_id"],
                     "correct": {a: (ans[a] == gold if ans[a] else None)
                                 for a in ans}})
    acc = {a: float(np.mean([r["correct"][a] for r in recs
                             if r["correct"][a] is not None]))
           for a in ARMS}
    return {"accuracy": acc, "n_items": len(recs), "records": recs}


def cot_coverage(bank):
    """把 cot_quiz_cache（旧 4 域抽样题）的答案经 quizbank_v20.json 的
    gold_edge 精确映射到大题库（旧 item_id 为采样序号不可直接对齐）。"""
    import glob
    old_bank = {q["item_id"]: q for q in json.load(
        open(os.path.join(RESULTS, "quizbank_v20.json"), encoding="utf-8"))["items"]}
    cot_by_edge = {}
    for f in glob.glob(os.path.join(RESULTS, "cot_quiz_cache", "*.json")):
        rec = json.load(open(f, encoding="utf-8"))
        items = _extract_json_array(rec["response_text"])
        for iid, it in zip(rec["item_ids"], items):
            if iid in old_bank:
                ob = old_bank[iid]
                letter = str(it.get("answer", "")).strip().upper()[:1]
                if letter in "ABCD":
                    oi = ord(letter) - 65
                    if 0 <= oi < len(ob["options"]):
                        cot_by_edge[(ob["domain"], tuple(ob["gold_edge"]))] = \
                            ob["options"][oi]  # 映射为选中**文本**（选项序不同库不同）
    per_domain, total = {}, 0
    for q in bank:
        chosen = cot_by_edge.get((q["domain"], tuple(q["gold_edge"])))
        if chosen is None:
            continue
        gold = q["options"][q["answer_index"]]
        per_domain.setdefault(q["domain"], []).append(chosen == gold)
        total += 1
    return {"n_cot_items": total,
            "per_domain": {d: float(np.mean(v)) for d, v in per_domain.items()},
            "overall": (float(np.mean([x for v in per_domain.values()
                                       for x in v])) if total else None)}


def main():
    t0 = time.time()
    cfg = DiffusionConfig()
    graphs = {g["graph_id"][2:]: g for g in load_corpus(CORPUS_DIR, families=("L",))}
    bank = build_big_bank(graphs)
    with open(BANK_PATH, "w", encoding="utf-8") as f:
        json.dump({"quizbank": "v20_big", "n_items": len(bank),
                   "spec": "bloom L4 × attacker_xl_cache（6 域全 named 边）",
                   "items": bank}, f, ensure_ascii=False, indent=1)
    per = {}
    for domain, g in graphs.items():
        rec = json.load(open(os.path.join(RESULTS, "familyL_prior_cache",
                                          f"{domain}.json"), encoding="utf-8"))
        prior = _validate_prior(_extract_json_array(rec["response_text"]), g["N"])
        items = [q for q in bank if q["domain"] == domain]
        per[domain] = eval_domain(g, prior, cfg, items)
    overall = {a: float(np.mean([v["accuracy"][a] for v in per.values()]))
               for a in ARMS}
    cot = cot_coverage(bank)
    out = {"experiment": "deposon_v20_bigquiz_eval", "spec_version": "v2.0",
           "config": config_dict(cfg),
           "quizbank_path": BANK_PATH, "n_items": len(bank),
           "per_domain": per, "overall": overall, "cot_arm": cot,
           "runtime_sec": round(time.time() - t0, 3),
           "honesty": [
               "no LLM API calls issued：题库由 attacker_xl 缓存与本机构建，作答全部本地。",
               "机制性免疫披露同小题库：陷阱标签不在图节点集内，field/prior/tfidf 对其"
               "打 -inf；rule_filter 的渗漏才是标签攻击真实战场。",
               "CoT 臂仅覆盖 4 旧域抽样题（cot_quiz_cache 复用，按同序号映射），"
               "新 2 域 CoT 待补（预算控制，如实披露）。",
               "题库为横向对比（题型效度），不作为独立基准主张。"]}
    with open(EVAL_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({"n_items": len(bank), "overall": overall, "cot": cot,
                      "per_domain": {d: v["accuracy"] for d, v in per.items()}},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
