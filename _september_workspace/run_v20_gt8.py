# -*- coding: utf-8 -*-
# Deposon v2.0 博弈论 GT-8：「领域鉴定器 v0」hub_concentration 轴语料外
# 预登记复现（docs/SPEC_GT8.md，先于本实验任何数据提交，git 时间戳为证）
#   → results/deposon_v20_gt8.json
#
# 背景：OLS（n=20，results/v20_regression_field_v2.json）hub_concentration
#   β=+2.12（p=0.00028）→ 高 hub 图结构场更强。评审要求 ≥2 张语料外新图
#   预登记复现。本实验 2 对族 S 新图（高 hub vs 低 hub，N 与 n_edges 完全
#   对配，real_semantics=0），判定见 gt8_verdict（预登记，机械求值）。
#
# 协议与 run_v20_corpus_eval.py 逐行同式（全边留一、全候选 raw 口径、
#   臂 field_mean/random/degree、rng=default_rng(g_seed*100003+ei)、
#   场实例种子 g_seed+ei、named Hits@3）；协议函数经只读 import 复用，
#   既有文件一行不动。复用正确性由 tests/test_v20_gt8.py 锚定：对语料
#   S1/S2/S3 重算特征公式应逐值等于 results/v20_graph_features.csv。
#
# 零 LLM API：四张新图本地构造（族 S 合成标签，语义与结构脱钩，
#   real_semantics=0）；real_semantics 轴需先验 API 预算，本轮 deferred。
import json
import os
import time

import numpy as np

from deposon_diffusion import DiffusionConfig, config_dict
from mindmap_corpus_v20 import (_assign_labels, _canonical_sha256, is_dag,
                                longest_path_family)
from run_v15_experiment import row_normalize
from run_v19_fullrank import full_candidate_mask, gold_rank
from run_v19_meanfield import field_scores_init

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
OUT_PATH = os.path.join(RESULTS, "deposon_v20_gt8.json")

# ------------------------------------------------------------ 预登记冻结常量
GT8_SEEDS = {"GT8_A_high": 208801, "GT8_A_low": 208802,
             "GT8_B_high": 208803, "GT8_B_low": 208804}
GT8_PAIRS = (("GT8_A_high", "GT8_A_low"), ("GT8_B_high", "GT8_B_low"))
GT8_MIN_PAIRS = 2          # 成功标准：≥2/2 对同向
ARMS = ("field_mean", "random", "degree")


# ------------------------------------------------------------ 新图构造（冻结拓扑）
def _edges_A_high():
    """星-链双汇聚（N=31，E=30）：root 0；枢纽 1/2；13+7 条星边 +
    两条汇聚链（23→24→1，25→26→27→2）+ 3 条枢纽外悬叶。
    named = 全部以枢纽（1/2）为终点的汇聚边。"""
    edges = ([(0, 1), (0, 2)]
             + [(i, 1) for i in range(3, 16)]
             + [(i, 2) for i in range(16, 23)]
             + [(23, 24), (24, 1), (25, 26), (26, 27), (27, 2)]
             + [(1, 28), (1, 29), (2, 30)])
    named = {e for e in edges if e[1] in (1, 2)}
    return 31, edges, named


def _edges_A_low():
    """毛虫链（N=31，E=30）：主干链 0→…→15（15 边）+ 15 叶指回主干
    （叶 16+k → 主干节点 k+1，最大入度 2）。named = 主干链边。"""
    edges = [(i, i + 1) for i in range(15)] + [(16 + k, k + 1)
                                               for k in range(15)]
    named = set(edges[:15])
    return 31, edges, named


def _edges_B_high():
    """带超枢纽的平衡树（N=40，E=39）：节点 0..20 平衡二叉树（20 边）+
    超枢纽 21：19 条星边（20 与 22..39 → 21）。named = 超枢纽星边。"""
    edges = ([((i - 1) // 2, i) for i in range(1, 21)]
             + [(j, 21) for j in range(22, 40)] + [(20, 21)])
    named = {e for e in edges if e[1] == 21}
    return 40, edges, named


def _edges_B_low():
    """平衡三叉树（N=40，E=39）：parent=(i-1)//3，最大入度 1。
    named = 子节点仍为内部节点的父子边（沿用 S2 口径）。"""
    N = 40
    edges = [((i - 1) // 3, i) for i in range(1, N)]
    named = {(u, v) for (u, v) in edges if 3 * v + 1 < N}
    return N, edges, named


_GT8_STRUCTS = {"GT8_A_high": ("star_chain_double_convergence", _edges_A_high),
                "GT8_A_low": ("caterpillar_chain", _edges_A_low),
                "GT8_B_high": ("balanced_tree_superhub", _edges_B_high),
                "GT8_B_low": ("balanced_ternary_tree", _edges_B_low)}


def build_gt8_graph(graph_id):
    """确定性构造一张 GT-8 新图（族 S 记录格式，sha256 内容哈希）。"""
    structure, fn = _GT8_STRUCTS[graph_id]
    N, edges, named = fn()
    edges = sorted(set((int(u), int(v)) for (u, v) in edges))
    named = sorted({(int(u), int(v)) for (u, v) in named})
    if not is_dag(N, edges):
        raise ValueError(f"{graph_id}: structure is not a DAG")
    _nl, _L, src, tgt = longest_path_family(N, edges)
    filler = sorted(set(edges) - set(named))
    seed = GT8_SEEDS[graph_id]
    rec = {"graph_id": graph_id, "family": "S", "structure": structure,
           "N": N, "nodes": list(range(N)), "labels": _assign_labels(N, seed),
           "edges": [list(e) for e in edges],
           "named_edges": [list(e) for e in named],
           "filler_edges": [list(e) for e in filler],
           "source": int(src), "target": int(tgt),
           "seed": int(seed), "generator_version": "v2.0-gt8"}
    rec["sha256"] = _canonical_sha256(rec)
    return rec


# ------------------------------------------------------------ 特征（锁定操作化）
def hub_concentration(N, edges):
    """hub_concentration = max_in_degree / n_edges（SPEC_GT8 §2 逐字）。"""
    indeg = np.zeros(N, dtype=int)
    for (u, v) in edges:
        indeg[int(v)] += 1
    return float(indeg.max() / len(edges))


def graph_invariant(N, edges):
    """不同构哨兵不变量：(N, n_edges, 入度多重集, 出度多重集)。"""
    indeg = [0] * N
    outdeg = [0] * N
    for (u, v) in edges:
        outdeg[int(u)] += 1
        indeg[int(v)] += 1
    return (int(N), len(edges), tuple(sorted(indeg)), tuple(sorted(outdeg)))


# ------------------------------------------------------------ 三臂评估（协议同式）
def eval_graph(graph, cfg):
    """单图全边留一（全候选协议），臂 = field_mean/random/degree，
    与 run_v20_corpus_eval.arm_rows 逐行同式（仅取本实验所需三臂）。"""
    N = graph["N"]
    edges = [tuple(e) for e in graph["edges"]]
    named = {tuple(e) for e in graph["named_edges"]}
    adj = np.zeros((N, N))
    for (u, v) in edges:
        adj[u, v] = 1.0
    W_true = row_normalize(adj)
    g_seed = int(graph["seed"])
    hits = {a: {"named": [], "filler": []} for a in ARMS}
    for ei, (u, v) in enumerate(edges):
        rng = np.random.default_rng(g_seed * 100_003 + ei)
        adj_obs = adj.copy()
        adj_obs[u, v] = 0.0
        W_obs = W_true.copy()
        W_obs[u, v] = 0.0
        mask = full_candidate_mask(N, u)
        cand = np.flatnonzero(mask[u])
        tb = rng.random(int(cand.size))
        rows = {"field_mean": field_scores_init(
            W_obs, mask, cfg, graph["source"], graph["target"],
            g_seed + ei, "prior_mean")[u]}
        s = np.full(N, -np.inf)
        s[cand] = rng.random(int(cand.size))
        rows["random"] = s
        indeg = adj_obs.sum(axis=0)
        s = np.full(N, -np.inf)
        s[cand] = indeg[cand] + 1e-6 * tb
        rows["degree"] = s
        subset = "named" if (u, v) in named else "filler"
        for a, srow in rows.items():
            hits[a][subset].append(float(gold_rank(srow, cand, v) < 3))
    return {a: {k: (float(np.mean(v)) if v else None)
                for k, v in vv.items()} for a, vv in hits.items()}


# ------------------------------------------------------------ 判定规则（冻结）
def gt8_verdict(per_pair, min_pairs=GT8_MIN_PAIRS):
    """GT-8 冻结判定（机械求值，纯函数，tests/test_v20_gt8.py 锁定）：

    per_pair: [{pair, high, low, diff_high, diff_low}]
    支持：≥min_pairs 对且全部同向（diff_high > diff_low）⇒ supports_H_GT8；
    斩杀：全部对全反（diff_high < diff_low）⇒ H_GT8_dead，如实宣布；
    其余（含持平对、1/2）：inconclusive_preregistered_undefined_band。
    """
    n = len(per_pair)
    concordant = [p["pair"] for p in per_pair if p["diff_high"] > p["diff_low"]]
    reversed_ = [p["pair"] for p in per_pair if p["diff_high"] < p["diff_low"]]
    tied = [p["pair"] for p in per_pair if p["diff_high"] == p["diff_low"]]
    if n >= min_pairs and len(concordant) == n:
        verdict = "supports_H_GT8"
    elif n > 0 and len(reversed_) == n:
        verdict = "H_GT8_dead"
    else:
        verdict = "inconclusive_preregistered_undefined_band"
    return {"verdict": verdict,
            "supported_H_GT8": bool(verdict == "supports_H_GT8"),
            "n_pairs": n,
            "pairs_concordant": concordant,
            "pairs_reversed": reversed_,
            "pairs_tied": tied,
            "thresholds": {"min_pairs": min_pairs}}


# ------------------------------------------------------------ 实验主体
def main():
    t0 = time.time()
    cfg = DiffusionConfig()
    per_graph, per_pair = {}, []
    for pair in GT8_PAIRS:
        rec = {"pair": f"{pair[0]}__vs__{pair[1]}", "high": pair[0],
               "low": pair[1]}
        for role, gid in (("high", pair[0]), ("low", pair[1])):
            g = build_gt8_graph(gid)
            arms = eval_graph(g, cfg)
            edges = [tuple(e) for e in g["edges"]]
            feats = {"hub_concentration": hub_concentration(g["N"], edges),
                     "real_semantics": 0}
            diff_fr = arms["field_mean"]["named"] - arms["random"]["named"]
            diff_fd = arms["field_mean"]["named"] - arms["degree"]["named"]
            per_graph[gid] = {
                "structure": g["structure"], "N": g["N"],
                "n_edges": len(edges), "n_named": len(g["named_edges"]),
                "n_filler": len(g["filler_edges"]),
                "source": g["source"], "target": g["target"],
                "seed": g["seed"], "sha256": g["sha256"],
                "features": feats,
                "field_named": arms["field_mean"]["named"],
                "random_named": arms["random"]["named"],
                "degree_named": arms["degree"]["named"],
                "diff_fm_rand": diff_fr, "diff_fm_deg": diff_fd,
                "invariant": [g["N"], len(edges)]}
            rec[f"diff_{role}"] = diff_fr
            rec[f"hub_{role}"] = feats["hub_concentration"]
        rec["concordant"] = bool(rec["diff_high"] > rec["diff_low"])
        per_pair.append(rec)
    verdict = gt8_verdict(per_pair)
    runtime = round(time.time() - t0, 3)
    out = {"experiment": "deposon_v20_gt8", "spec_version": "v2.0",
           "spec": ("docs/SPEC_GT8.md：「领域鉴定器 v0」hub_concentration 轴"
                    "语料外预登记复现（SPEC 先于本实验数据提交，git 时间戳"
                    "为证）"),
           "config": config_dict(cfg),
           "preregistered": {
               "hypothesis": ("H_GT8：高 hub 新图 diff=field_named−random_named"
                              " 显著大于配对低 hub 新图"),
               "pairs": [list(p) for p in GT8_PAIRS],
               "seeds": GT8_SEEDS,
               "arms": list(ARMS),
               "protocol": ("run_v20_corpus_eval 同协议：全边留一、全候选 raw "
                            "口径、rng=g_seed*100003+ei、场实例种子 g_seed+ei、"
                            "named Hits@3"),
               "feature_rule": ("hub_concentration = max_in_degree / n_edges；"
                                "real_semantics = 0（族 S 合成标签）"),
               "pass_rule": "≥2/2 对同向 ⇒ supports_H_GT8",
               "kill_rule": "2/2 对全反 ⇒ H_GT8_dead，如实宣布",
               "else": "inconclusive（预登记未定义区间）"},
           "per_graph": per_graph,
           "per_pair": per_pair,
           "verdict": verdict,
           "runtime_sec": runtime,
           "honesty": [
               "no LLM API calls issued：四张新图本地构造，全部实验为本地"
               "种子化 numpy 运行；语料只读加载（仅用于不同构哨兵与特征"
               "锚点复核，见 tests/test_v20_gt8.py）。",
               "SPEC_GT8.md 先于本实验任何数据写盘并 git 提交（预登记时间戳"
               "为证）；拓扑、种子、named/filler 口径、判定规则全部冻结。",
               "real_semantics 轴需 LLM 先验 API 预算，本轮 deferred 不测，"
               "如实声明；本实验全部新图 real_semantics=0（族 S 合成标签）。",
               "样本仅 2 对（评审要求的下限设计）：方向性证据，非效应量"
               "估计；仅族 S，不外推至族 L。",
               "协议与 run_v20_corpus_eval 逐行同式（三臂子集）；复用正确性"
               "由 tests/test_v20_gt8.py 锚定（S1/S2/S3 特征公式重算等于 "
               "results/v20_graph_features.csv 锚点 0.0526/0.0333/0.0625）。",
               "判定规则为纯函数 gt8_verdict 机械求值，tests/test_v20_gt8.py "
               "锁定；落在预登记未定义区间时报 inconclusive，不美化。",
               f"总运行 {runtime}s（预算 600s 内）"
               if runtime <= 600 else
               f"总运行 {runtime}s 超预算，如实披露。"]}
    os.makedirs(RESULTS, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({"out": OUT_PATH, "runtime_sec": runtime,
                      "verdict": verdict["verdict"],
                      "per_pair": [{k: (round(v, 4) if isinstance(v, float)
                                        else v)
                                    for k, v in p.items()} for p in per_pair]},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
