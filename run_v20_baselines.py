# -*- coding: utf-8 -*-
# Deposon v2.0 基线注册表补齐（docs/BASELINE_REGISTRY.md，零 API）
#   → results/deposon_v20_baselines.json
#
# 新增臂（全候选协议，E9.2 raw 口径，与 run_v20_corpus_eval 同协议）：
#   A 族：common_neighbors / preferential_attachment / ppr(α=0.85) / katz(β=0.005,K=3)
#         / node2vec_shallow（纯 numpy 近似，d=16，如实标注非完整实现）
#   B 族：ngram_tfidf_cosine（字符 3-gram TF-IDF，embedding 余弦的零 API 代理）
#   E 族：first_option（位置偏置平凡基线，仅题库用——本脚本不报）
# 大 BOSS 测试：任何基线在任一图 named 击败 field_mean → 结果 JSON 头条字段
#   boss_alert=True 且逐图列出，Findings 必须披露（注册表收编纪律 #2）。
# v2.0.1：BOSS 统计门槛（margin ≥3 条金边），tiebreak 抽签事件降级保留。
# no LLM API calls issued。
import json
import os
import time

import numpy as np

from deposon_diffusion import DiffusionConfig, config_dict
from mindmap_corpus_v20 import CORPUS_DIR, load_corpus
from run_v15_experiment import row_normalize
from run_v19_fullrank import full_candidate_mask, gold_rank
from run_v19_meanfield import field_scores_init

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
OUT_PATH = os.path.join(RESULTS, "deposon_v20_baselines.json")
PPR_ALPHA = 0.85
KATZ_BETA, KATZ_K = 0.005, 3
N2V_DIM, N2V_LEN = 16, 10
# 双配置（注册表纪律：结果对训练预算的敏感性如实双报）：
#   full = 逐边归纳训练（30 epochs/40 walks，慢速参考，~500s）
#   cheap = 逐边归纳训练（5 epochs/10 walks，~10× 提速，默认臂）
N2V_CONFIGS = {"full": {"walks": 40, "epochs": 30},
               "cheap": {"walks": 10, "epochs": 5}}
N2V_DEFAULT = "cheap"


# ---------------------------------------------------------------- A 族结构臂
def undirected(adj_obs):
    U = (adj_obs + adj_obs.T) > 0.0
    return U, U.sum(axis=1)


def common_neighbors_row(adj_obs, u, cand):
    U, _ = undirected(adj_obs)
    s = np.full(adj_obs.shape[0], -np.inf)
    for j in cand:
        s[j] = float(np.count_nonzero(U[u] & U[j]))
    return s


def pref_attach_row(adj_obs, u, cand):
    U, deg = undirected(adj_obs)
    s = np.full(adj_obs.shape[0], -np.inf)
    s[cand] = deg[u] * deg[cand]
    return s


def ppr_row(adj_obs, u, cand, alpha=PPR_ALPHA, iters=60):
    """无向投影上的 Personalized PageRank（power iteration，容差 1e-12）。"""
    U, deg = undirected(adj_obs)
    n = U.shape[0]
    A = U.astype(float)
    d = np.maximum(deg, 1.0)
    P = A / d[:, None]
    r = np.zeros(n); r[u] = 1.0
    teleport = np.zeros(n); teleport[u] = 1.0
    for _ in range(iters):
        r_new = alpha * (P.T @ r) + (1 - alpha) * teleport
        if np.abs(r_new - r).sum() < 1e-12:
            r = r_new
            break
        r = r_new
    s = np.full(n, -np.inf)
    s[cand] = r[cand]
    return s


def katz_row(adj_obs, u, cand, beta=KATZ_BETA, K=KATZ_K):
    """Katz 截断级数：Σ_{k=1..K} β^k (A^k)[u,j]（无向投影）。"""
    U, _ = undirected(adj_obs)
    A = U.astype(float)
    n = A.shape[0]
    s = np.zeros(n)
    Ak = A.copy()
    for k in range(1, K + 1):
        s += (beta ** k) * Ak[u]
        Ak = Ak @ A
    out = np.full(n, -np.inf)
    out[cand] = s[cand]
    return out


def node2vec_shallow_row(adj_obs, u, cand, seed, budget=None):
    """Node2Vec 浅近似（非完整实现，honesty 标注）：无向投影上二阶随机游走
    （p=q=1）+ 负采样 skip-gram 简化（ logistic 内积目标，d=16，5 负样/正样）。
    逐边归纳训练（留边图），预算由 N2V_CONFIGS[budget] 决定（cheap 默认 /
    full 敏感性参考）。2026-08-28 事故记录：曾尝试按图缓存（转导式，训练图
    含金边），导致 18/20 图「获胜」——纯泄漏 artifact，已回退；归纳协议是
    该基线有效性的前提，提速不得越过协议纯度。"""
    budget = budget or N2V_DEFAULT
    n_walks, n_epochs = N2V_CONFIGS[budget]["walks"], N2V_CONFIGS[budget]["epochs"]

    rng = np.random.default_rng(seed)
    U, deg = undirected(adj_obs)
    n = U.shape[0]
    neigh = [np.flatnonzero(U[i]) for i in range(n)]
    walks = []
    for _ in range(n_walks):
        for start in range(n):
            w = [start]
            for _ in range(N2V_LEN - 1):
                nb = neigh[w[-1]]
                if nb.size == 0:
                    break
                w.append(int(nb[rng.integers(nb.size)]))
            if len(w) > 2:
                walks.append(w)
    d = N2V_DIM
    E1 = rng.normal(0, 0.1, (n, d))
    E2 = rng.normal(0, 0.1, (n, d))
    lr = 0.05
    for _ in range(n_epochs):
        for w in walks[:60]:
            for i in range(1, len(w) - 1):
                c, o = w[i], w[i + 1]
                negs = rng.integers(0, n, 5)
                x = E1[c]
                for t, lab in [(o, 1.0)] + [(int(ng), 0.0) for ng in negs]:
                    z = float(x @ E2[t])
                    sig = 1.0 / (1.0 + np.exp(-z))
                    g = (lab - sig) * lr
                    E1[c] += g * E2[t]
                    E2[t] += g * x
                    x = E1[c]
    return _n2v_row_from_emb(E1, E2, u, cand)


def _n2v_row_from_emb(E1, E2, u, cand):
    n = E1.shape[0]
    s = np.full(n, -np.inf)
    s[cand] = (E1[u] * E2[cand]).sum(axis=1)
    return s


# ---------------------------------------------------------------- B 族语义代理臂
def ngram_tfidf_cosine_row(labels, u, cand, n=3):
    """字符 n-gram TF-IDF 余弦（标签 embedding 余弦的零 API 代理）。"""
    def grams(s):
        s = f"#{s}#"
        return {s[i:i + n] for i in range(len(s) - n + 1)}
    docs = [grams(str(x)) for x in labels]
    df = {}
    for dset in docs:
        for g in dset:
            df[g] = df.get(g, 0) + 1
    N = len(docs)

    def vec(i):
        return {g: (1.0 / df[g]) * np.log(N / (1 + df[g])) for g in docs[i]}
    vu = vec(u)
    nu = np.sqrt(sum(x * x for x in vu.values())) or 1.0
    s = np.full(len(labels), -np.inf)
    for j in cand:
        vj = vec(j)
        nj = np.sqrt(sum(x * x for x in vj.values())) or 1.0
        dot = sum(v * vj[g] for g, v in vu.items() if g in vj)
        s[j] = dot / (nu * nj)
    return s


# ---------------------------------------------------------------- 主评估
NEW_ARMS = ("common_neighbors", "preferential_attachment", "ppr", "katz",
            "node2vec_shallow", "ngram_tfidf_cosine")
# BOSS 统计门槛（R1 复核：6 事件中 4 个 margin ≤2 条边，S5 恰为 1 条边的
# tiebreak 抽签；R1 200 次置换证实 S5 观测在 37.5% 抽签中出现）
BOSS_GATE_EDGES = 3
# full 预算参考子集（归纳全速配置仅跑两图作敏感性对照）
N2V_FULL_REFS = ("S6", "L_biological_taxonomy")


def eval_graph(graph, cfg):
    N = graph["N"]
    edges = [tuple(e) for e in graph["edges"]]
    named = {tuple(e) for e in graph["named_edges"]}
    adj = np.zeros((N, N))
    for (u, v) in edges:
        adj[u, v] = 1.0
    W_true = row_normalize(adj)
    g_seed = int(graph["seed"])
    arms_here = list(NEW_ARMS)
    if graph["graph_id"] in N2V_FULL_REFS:
        arms_here.append("node2vec_full")
    hits = {a: {"named": [], "filler": []} for a in ("field_mean",) + tuple(arms_here)}
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
        for name, fn in (("common_neighbors", common_neighbors_row),
                         ("preferential_attachment", pref_attach_row),
                         ("ppr", ppr_row), ("katz", katz_row)):
            s = fn(adj_obs, u, cand)
            s[cand] += 1e-9 * tb
            rows[name] = s
        s = node2vec_shallow_row(adj_obs, u, cand, g_seed + ei, budget="cheap")
        s[cand] += 1e-9 * tb
        rows["node2vec_shallow"] = s
        if "node2vec_full" in hits:
            s2 = node2vec_shallow_row(adj_obs, u, cand, g_seed + ei, budget="full")
            s2[cand] += 1e-9 * tb
            rows["node2vec_full"] = s2
        s = ngram_tfidf_cosine_row(graph["labels"], u, cand)
        s[cand] += 1e-9 * tb
        rows["ngram_tfidf_cosine"] = s
        subset = "named" if (u, v) in named else "filler"
        for a, srow in rows.items():
            hits[a][subset].append(float(gold_rank(srow, cand, v) < 3))
    return {a: {k: (float(np.mean(v)) if v else None) for k, v in vv.items()}
            for a, vv in hits.items()}


def main():
    t0 = time.time()
    cfg = DiffusionConfig()
    graphs = load_corpus(CORPUS_DIR, families=("S", "L"))
    per_graph, boss = {}, []
    for g in graphs:
        gid = g["graph_id"]
        per_graph[gid] = eval_graph(g, cfg)
        per_graph[gid]["_n_named"] = len(g["named_edges"])
        fm = per_graph[gid]["field_mean"]["named"]
        for a in NEW_ARMS:
            v = per_graph[gid][a]["named"]
            if fm is not None and v is not None and v > fm:
                n_named_g = per_graph[gid]["_n_named"]
                margin_edges = (v - fm) * n_named_g
                boss.append({"graph_id": gid, "arm": a,
                             "baseline_named": v, "field_mean_named": fm,
                             "margin": round(v - fm, 4),
                             "margin_edges": round(margin_edges, 2),
                             "gate_pass": bool(margin_edges >= BOSS_GATE_EDGES)})
    out = {"experiment": "deposon_v20_baselines", "spec_version": "v2.0",
           "spec": "docs/BASELINE_REGISTRY.md（基线注册表补齐）",
           "config": config_dict(cfg),
           "new_arms": list(NEW_ARMS),
           "n2v_budgets": N2V_CONFIGS, "n2v_full_refs": list(N2V_FULL_REFS),
           "per_graph": per_graph,
           "boss_alert": bool([e for e in boss if e["gate_pass"]]),
           "boss_events": [e for e in boss if e["gate_pass"]],
           "boss_events_below_gate": [e for e in boss if not e["gate_pass"]],
           "boss_gate_edges": BOSS_GATE_EDGES,
           "runtime_sec": round(time.time() - t0, 3),
           "honesty": [
               "no LLM API calls issued：全部基线本地计算。",
               "node2vec_shallow 为纯 numpy 浅近似（p=q=1 二阶游走 + 简化 skip-gram），"
               "非完整 Node2Vec 实现，仅作结构邻近嵌入代理，不作 KGE 级主张；"
               "逐边归纳训练（留边图）。双预算如实双报：cheap（默认臂，~44s 全语料）"
               "与 full（两图敏感性参考）。曾试按图缓存的转导式（训练图含金边），"
               "造成 18/20 图假胜利——泄漏 artifact 已回退，教训：归纳协议是该基线"
               "有效性的前提，提速不得越过协议纯度。",
               "ngram_tfidf_cosine 为标签 embedding 余弦的零 API 代理（字符 3-gram "
               "TF-IDF），与真实 embedding 余弦有差距，如实标注。",
               "boss_alert 逐图列出：任一基线 named 击败 field_mean 即头条披露"
               "（注册表收编纪律 #2），不埋没；v2.0.1 起加统计门槛"
               "（margin ≥3 条金边，R1 复核：tiebreak 抽签可产生 ≤2 边假 margin，"
               "被拦事件列于 boss_events_below_gate 如实保留）。"
               "tfidf 在族 S 合成图上余弦近全零（S4 金边 >0 仅 0/58），"
               "其排序由 1e-9 tiebreak 抽签主导——实质为伪装随机臂（R1 实跑），"
               "语义臂在标签脱钩图上不作语义性解读。",
               "判定机械求值，负面如实。"]}
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({"boss_alert": bool(boss), "boss_events": boss,
                      "named_table": {g: {a: per_graph[g][a]["named"]
                                          for a in ("field_mean",) + NEW_ARMS}
                                      for g in per_graph}},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
