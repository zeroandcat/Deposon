# -*- coding: utf-8 -*-
# Deposon GT-2B（预登记 docs/SPEC_GT2B.md）：GT-2 多陷阱强度升级，题库轨。
#   → results/deposon_v20_gt2b.json
#
# 设计：固定 4 选项（机会恒 25%），陷阱数 T ∈ {1,2,3}，其余干扰位用图内
# 随机节点补足 ⇒ 隔离陷阱强度与选项数两个自由度。臂：rule_filter /
# field_mean / random（llm_prior 属 API 轨，本轮零 API 不跑）。
# no LLM API calls issued：仅复用 results/gt2_attacker_cache 既有缓存，
# 不合成/改写陷阱标签。确定性：显式种子 + crc32 稳定哈希（禁用进程随机
# hash()），结果 JSON 无运行时字段，同种子两次运行逐字节一致。
import json
import os
import zlib

import numpy as np

from deposon_diffusion import DiffusionConfig, config_dict
from mindmap_corpus_v20 import CORPUS_DIR, load_corpus
from llm_prior import _extract_json_array
from run_v15_experiment import row_normalize
from run_v19_fullrank import full_candidate_mask
from run_v19_meanfield import field_scores_init
from run_v20_corpus_eval import RULE_KEYWORDS

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
OUT_PATH = os.path.join(RESULTS, "deposon_v20_gt2b.json")
N_ITEMS_PER_MAP = 10
BANK_SEED = 20260828           # 沿用 run_v20_quizbank 选题种子
T_LEVELS = (1, 2, 3)
FIELD_TOL = 0.05               # SPEC §4 场免疫容差带
ARMS = ("rule_filter", "field_mean", "random")


def load_json(p):
    return json.load(open(p, encoding="utf-8"))


def load_traps(domain):
    """读缓存攻击者陷阱标签（不合成/改写）。"""
    atk = load_json(os.path.join(RESULTS, "gt2_attacker_cache", f"{domain}.json"))
    return [str(it["label"]) for it in _extract_json_array(atk["response_text"])]


def stable_seed(g_seed, item_id):
    """crc32 稳定哈希替代进程随机的 hash()，保证跨进程确定性。"""
    return int(g_seed) * 97 + zlib.crc32(item_id.encode("utf-8")) % 1000


def build_bank_t(graphs, traps_by_domain, T):
    """陷阱强度 T 的题库：选项 = 1 金 + T 陷阱 + (3-T) 图内随机节点，恒 4 项。"""
    rng = np.random.default_rng(BANK_SEED)
    bank = []
    for domain, g in graphs.items():
        labels = g["labels"]
        named = [tuple(e) for e in g["named_edges"]]
        traps = traps_by_domain[domain]
        take = rng.choice(len(named), size=min(N_ITEMS_PER_MAP, len(named)),
                          replace=False)
        for k in take:
            u, v = named[int(k)]
            tset = [traps[(T * int(k) + j) % len(traps)] for j in range(T)]
            others = [j for j in range(g["N"]) if j != v]
            decoys = [labels[int(others[rng.integers(len(others))])]
                      for _ in range(3 - T)]
            options = [labels[v]] + tset + decoys
            perm = rng.permutation(4)
            bank.append({
                "item_id": f"{domain}#q{int(k):02d}",
                "domain": domain, "bloom_level": "L4_analyze",
                "stem": f"在概念体系「{domain}」中，与「{labels[u]}」存在最直接"
                        f"合理后继关系的是哪一个？",
                "gold_edge": [int(u), int(v)],
                "gold_label": labels[v],
                "options": [options[int(i)] for i in perm],
                "answer_index": int(np.flatnonzero(perm == 0)[0]),
                "n_traps": T,
                "trap_labels": tset,
                "random_node_labels": decoys})
    return bank


def answer_quiz(graph, cfg, bank):
    """三臂作答（rule_filter / field_mean / random），逐题正误。"""
    N = graph["N"]
    labels = graph["labels"]
    adj = np.zeros((N, N))
    for (u, v) in [tuple(e) for e in graph["edges"]]:
        adj[u, v] = 1.0
    W_true = row_normalize(adj)
    g_seed = int(graph["seed"])
    records = []
    for item in bank:
        u, v = item["gold_edge"]
        rng = np.random.default_rng(stable_seed(g_seed, item["item_id"]))
        adj_obs = adj.copy(); adj_obs[u, v] = 0.0
        W_obs = W_true.copy(); W_obs[u, v] = 0.0
        mask = full_candidate_mask(N, u)
        fm = field_scores_init(W_obs, mask, cfg, graph["source"], graph["target"],
                               g_seed + (u * 131 + v) % 100000, "prior_mean")
        # 陷阱标签不在图节点集内 ⇒ field 对其打 -inf（机制性免疫，如实披露）
        fscores = {labels[j]: float(fm[u][j]) for j in range(N) if j != u}
        opts = item["options"]
        ans = {}
        best, best_s = None, -np.inf
        for o in opts:
            s = fscores.get(o, -np.inf)
            if s > best_s:
                best, best_s = o, s
        ans["field_mean"] = best
        surviving = [o for o in opts
                     if not any(k in o.lower() for k in RULE_KEYWORDS)]
        ans["rule_filter"] = surviving[0] if surviving else opts[0]
        ans["random"] = opts[int(rng.integers(4))]
        gold = opts[item["answer_index"]]
        records.append({"item_id": item["item_id"], "gold": gold,
                        "answers": ans,
                        "correct": {a: ans[a] == gold for a in ARMS}})
    acc = {a: float(np.mean([r["correct"][a] for r in records])) for a in ARMS}
    return {"accuracy": acc, "n_items": len(records), "records": records}


def verdict(acc_by_T):
    """SPEC §4 机械判定。acc_by_T: {arm: {T: acc}}。返回 (verdict, detail)。"""
    rf = [acc_by_T["rule_filter"][T] for T in sorted(acc_by_T["rule_filter"])]
    fm = [acc_by_T["field_mean"][T] for T in sorted(acc_by_T["field_mean"])]
    strict_dec = all(rf[i] > rf[i + 1] for i in range(len(rf) - 1))
    strict_inc = all(rf[i] < rf[i + 1] for i in range(len(rf) - 1))
    field_immune = all(abs(x - fm[0]) <= FIELD_TOL for x in fm[1:])
    if strict_inc:
        v = "H_GT2B_dead"
    elif strict_dec:
        v = "supports_H_GT2B"
    else:
        v = "inconclusive"
    detail = {"rule_filter_acc_by_T": rf, "field_mean_acc_by_T": fm,
              "field_immunity_ok": field_immune,
              "field_tol": FIELD_TOL}
    return v, detail


def run():
    cfg = DiffusionConfig()
    graphs_all = {d: g for d, g in
                  ((x["graph_id"][2:], x)
                   for x in load_corpus(CORPUS_DIR, families=("L",)))}
    # 缓存降级披露：仅 4 域有 gt2_attacker_cache，其余域不纳入（SPEC §2）
    graphs = {d: g for d, g in graphs_all.items()
              if os.path.exists(os.path.join(RESULTS, "gt2_attacker_cache",
                                             f"{d}.json"))}
    traps_by_domain = {d: load_traps(d) for d in graphs}
    per_T = {}
    for T in T_LEVELS:
        bank = build_bank_t(graphs, traps_by_domain, T)
        per_dom = {}
        for domain, g in graphs.items():
            items = [q for q in bank if q["domain"] == domain]
            per_dom[domain] = answer_quiz(g, cfg, items)
        per_T[str(T)] = {
            "per_domain": per_dom,
            "overall": {a: float(np.mean([v["accuracy"][a]
                                          for v in per_dom.values()]))
                        for a in ARMS},
            "items": bank}
    acc_by_T = {a: {T: per_T[str(T)]["overall"][a] for T in T_LEVELS}
                for a in ARMS}
    v, detail = verdict(acc_by_T)
    out = {"experiment": "deposon_v20_gt2b", "spec": "docs/SPEC_GT2B.md",
           "spec_version": "v2.0", "bank_seed": BANK_SEED,
           "T_levels": list(T_LEVELS), "n_options_fixed": 4,
           "chance_level": 0.25,
           "config": config_dict(cfg),
           "domains": sorted(graphs),
           "traps_available_per_domain":
               {d: len(t) for d, t in sorted(traps_by_domain.items())},
           "per_T": per_T,
           "accuracy_by_T": acc_by_T,
           "verdict": v, "verdict_detail": detail,
           "honesty": [
               "no LLM API calls issued：仅复用 results/gt2_attacker_cache 既有缓存；"
               "未合成/改写任何陷阱标签。",
               "缓存降级披露：geography_world / project_management 无攻击者缓存，"
               "本轮仅 4 域（与既有 quizbank_v20 一致）。",
               "机制性免疫披露：陷阱标签不在图节点集内，field_mean 对其打 -inf，"
               "不被骗是排序对象域的机制结果，不等价于语义识别能力。",
               "llm_prior 属 API 轨，本轮零 API 不跑（Findings §三先验臂 92.5% "
               "为上轮缓存结果，不重复主张）。",
               "判定机械求值（verdict() 纯函数），反转/判死如实。",
               "题库仅供横向对比（题型效度），不作为独立基准主张。"]}
    return out


def main():
    out = run()
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({"verdict": out["verdict"],
                      "accuracy_by_T": out["accuracy_by_T"]},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
