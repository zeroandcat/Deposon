# -*- coding: utf-8 -*-
# Deposon v2.0 族 S 语料全评估（docs/SPEC_v2.0.md §1–§2，预登记冻结）
#   → results/deposon_v20_corpus_eval.json
#
# 协议：每张图每边留一，全候选协议（E9.2 raw 口径：候选 = 全部 N−1 个非自身
# 节点，金边在候选中，不剔除其他观测边；无负采样 ⇒ 采样器敏感性按构造归零）。
# 主终点：每张图 named Hits@3，主臂 = field_mean。
# 臂：field_mean / field_guided / random / degree / adamic_adar / jaccard /
#     rule_filter（纯结构/标签字符串平凡基线，无需 LLM）。
# 图级统计：符号检验（field_mean vs random、vs degree）+ 图级 cluster
# bootstrap（B=10000，整图重采样）95% CI；Holm 校正（4 检验族，α=0.05）。
# SPEC §2 判定：H-A1 / H-A2 / H-B1 / H-S6 + 斩杀线触发状态，机械求值。
# no LLM API calls issued。
import json
import math
import os
import time

import numpy as np

from deposon_diffusion import DiffusionConfig, config_dict
from mindmap_corpus_v20 import CORPUS_DIR, SCAN_SIZES, load_corpus
from run_v15_experiment import row_normalize
from run_v17_fusion_fix import minmax_mask  # noqa: F401  (融合函数复用约定)
from run_v19_fullrank import full_candidate_mask, gold_rank, rank_metrics
from run_v19_meanfield import field_scores_init
from run_v19_quickwins import sign_test

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
OUT_PATH = os.path.join(RESULTS, "deposon_v20_corpus_eval.json")
ARMS = ("field_mean", "field_guided", "random", "degree",
        "adamic_adar", "jaccard", "rule_filter")
RULE_KEYWORDS = ("trap", "dead", "end", "impossible", "guess", "wrong")
BOOT_SEED, BOOT_B = 20260828, 10000
ALPHA = 0.05
HOLM_FAMILY = 4           # SPEC §2：Holm 校正 4 检验
PRIMARY_GRAPHS = ("S1", "S2", "S3", "S4", "S5", "S6")
KILL_REVERSAL_MIN = 3     # ≥3 张图效应反转 → H-A 判死
H_B1_THRESHOLD = 0.15     # filler Hits@3 边界
H_B1_KILL_MIN = 3         # ≥3 张图 filler ≥0.15 → 边界主张撤回
H_S6_THRESHOLD = 0.8      # S6 复现阈值
PHASE_TRANSITION_DELTA = 0.3   # 相邻两档 named 差 ≥0.3 = 相变点（SPEC §1）


# ---------------------------------------------------------------- 臂打分
def undirected_projection(adj_obs):
    U = (adj_obs + adj_obs.T) > 0.0
    return U, U.sum(axis=1)


def adamic_adar_row(adj_obs, u, cand):
    """Adamic-Adar（无向投影）：AA(u,j)=Σ_{w∈N(u)∩N(j)} 1/log(max(deg(w),2))。"""
    U, deg = undirected_projection(adj_obs)
    nu = U[u]
    invlog = 1.0 / np.log(np.maximum(deg, 2.0))
    s = np.full(adj_obs.shape[0], -np.inf)
    for j in cand:
        common = nu & U[j]
        s[j] = float(invlog[common].sum())
    return s


def jaccard_row(adj_obs, u, cand):
    """Jaccard（无向投影）：|N(u)∩N(j)| / |N(u)∪N(j)|，空并集记 0。"""
    U, deg = undirected_projection(adj_obs)
    nu = U[u]
    s = np.full(adj_obs.shape[0], -np.inf)
    for j in cand:
        inter = float(np.count_nonzero(nu & U[j]))
        union = float(np.count_nonzero(nu | U[j]))
        s[j] = inter / union if union > 0 else 0.0
    return s


def rule_filter_row(labels, cand):
    """规则过滤（E9.5 关键词表，纯标签字符串，无需 LLM）：候选标签命中
    关键词表 → 0 分（过滤降权），否则 1 分；大小写不敏感。"""
    s = np.full(len(labels), -np.inf)
    for j in cand:
        lab = str(labels[j]).lower()
        s[j] = 0.0 if any(k in lab for k in RULE_KEYWORDS) else 1.0
    return s


def arm_rows(graph, adj_obs, W_obs, mask, cand, u, rng, cfg, inst_seed):
    """七臂打分（行向量，非候选位置 -inf；确定性微扰破平局）。"""
    tiebreak = rng.random(int(cand.size))
    rows = {}
    rows["field_mean"] = field_scores_init(
        W_obs, mask, cfg, graph["source"], graph["target"], inst_seed,
        "prior_mean")[u]
    rows["field_guided"] = field_scores_init(
        W_obs, mask, cfg, graph["source"], graph["target"], inst_seed,
        "dirichlet")[u]
    s = np.full_like(W_obs, -np.inf, dtype=float)[u].copy()
    s[cand] = rng.random(int(cand.size))
    rows["random"] = s
    indeg = adj_obs.sum(axis=0)
    s = np.full(len(indeg), -np.inf)
    s[cand] = indeg[cand] + 1e-6 * tiebreak
    rows["degree"] = s
    s = adamic_adar_row(adj_obs, u, cand)
    s[cand] += 1e-6 * tiebreak
    rows["adamic_adar"] = s
    s = jaccard_row(adj_obs, u, cand)
    s[cand] += 1e-6 * tiebreak
    rows["jaccard"] = s
    s = rule_filter_row(graph["labels"], cand)
    s[cand] += 1e-6 * tiebreak
    rows["rule_filter"] = s
    return rows


# ---------------------------------------------------------------- 单图评估
def eval_graph(graph, cfg):
    """单图全边留一（全候选协议）。返回 arms 指标 + per_edge 明细。"""
    N = graph["N"]
    edges = [tuple(e) for e in graph["edges"]]
    named = {tuple(e) for e in graph["named_edges"]}
    adj = np.zeros((N, N))
    for (u, v) in edges:
        adj[u, v] = 1.0
    W_true = row_normalize(adj)
    g_seed = int(graph["seed"])
    per_edge = []
    for ei, (u, v) in enumerate(edges):
        rng = np.random.default_rng(g_seed * 100_003 + ei)
        adj_obs = adj.copy()
        adj_obs[u, v] = 0.0
        W_obs = W_true.copy()
        W_obs[u, v] = 0.0
        mask = full_candidate_mask(N, u)
        cand = np.flatnonzero(mask[u])
        rows = arm_rows(graph, adj_obs, W_obs, mask, cand, u, rng, cfg,
                        inst_seed=g_seed + ei)
        rec = {"edge": [int(u), int(v)],
               "edge_label": [graph["labels"][u], graph["labels"][v]],
               "on_named_path": (u, v) in named,
               "n_candidates": int(cand.size),
               "arms": {a: {"rank": gold_rank(srow, cand, v)}
                        for a, srow in rows.items()}}
        per_edge.append(rec)

    def ranks(arm, flag):
        return [r["arms"][arm]["rank"] for r in per_edge
                if flag == "overall" or
                (flag == "named" and r["on_named_path"]) or
                (flag == "filler" and not r["on_named_path"])]

    arms = {a: {f: rank_metrics(ranks(a, f))
                for f in ("overall", "named", "filler")} for a in ARMS}
    return {"graph_id": graph["graph_id"], "family": graph["family"],
            "structure": graph["structure"], "N": N, "n_edges": len(edges),
            "n_named": len(named), "n_filler": len(edges) - len(named),
            "source": graph["source"], "target": graph["target"],
            "seed": g_seed, "sha256": graph["sha256"],
            "arms": arms, "per_edge": per_edge}


# ---------------------------------------------------------------- 图级统计
def cluster_bootstrap(gids, values, seed=BOOT_SEED, B=BOOT_B):
    """图级 cluster bootstrap：整图重采样 G 张图，统计量 = 图均值。

    values: {gid: scalar}。返回均值与 95% 分位 CI。"""
    rng = np.random.default_rng(seed)
    gids = list(gids)
    base = np.array([values[g] for g in gids], dtype=float)
    stats = np.empty(B)
    G = len(gids)
    for b in range(B):
        idx = rng.integers(0, G, G)
        stats[b] = float(base[idx].mean())
    lo, hi = np.quantile(stats, [0.025, 0.975])
    return {"mean": float(base.mean()), "ci95": [float(lo), float(hi)],
            "G": G, "B": B, "seed": seed, "unit": "graph (cluster resample)"}


def holm_adjust(pvals: dict, m: int = HOLM_FAMILY, alpha: float = ALPHA):
    """Holm 校正：p 升序，第 k 小与 alpha/(m-k+1) 比较，顺序停止。
    SPEC §2 预登记 4 检验族（H-A1/H-A2/H-B1/H-S6）；H-B1/H-S6 为确定性
    阈值规则无 p 值，仅两个符号检验进入 Holm 序列但族规模 m=4 保守计。
    """
    items = sorted(pvals.items(), key=lambda kv: kv[1])
    out, stopped = {}, False
    for k, (name, p) in enumerate(items):
        thresh = alpha / (m - k)
        sig = bool((not stopped) and p < thresh)
        out[name] = {"p_raw": float(p), "holm_threshold": float(thresh),
                     "significant_holm": sig}
        if not sig:
            stopped = True
    return out


def phase_scan(per_graph):
    """量变质变扫描：S1/S2/S6 × N∈{20,35,45,60} 的 field_mean named Hits@3
    曲线；相变点 = 相邻两档 named 差 ≥0.3（SPEC §1 预登记定义）。"""
    by_id = {g["graph_id"]: g for g in per_graph}

    def scan_gid(fam, N):
        if (fam == "S1" and N == 20) or (fam == "S6" and N == 45):
            return fam  # 扫描档与主档重合，复用主档
        return f"{fam}_n{N}"

    scan = {}
    for fam in ("S1", "S2", "S6"):
        sizes, curve, refs = [], {}, {}
        for N in SCAN_SIZES:
            gid = scan_gid(fam, N)
            g = by_id[gid]
            val = g["arms"]["field_mean"]["named"]["hits@3"]
            sizes.append(N)
            curve[str(N)] = val
            refs[str(N)] = {"graph_id": gid,
                            "random_named": g["arms"]["random"]["named"]["hits@3"]}
        pts = [curve[str(N)] for N in sizes]
        transitions = []
        for a, b, va, vb in zip(sizes[:-1], sizes[1:], pts[:-1], pts[1:]):
            if va is not None and vb is not None and abs(vb - va) >= PHASE_TRANSITION_DELTA:
                transitions.append({"from_N": a, "to_N": b,
                                    "delta": float(vb - va),
                                    "direction": "up" if vb > va else "down"})
        scan[fam] = {"sizes": sizes, "field_mean_named_hits3": curve,
                     "reference": refs, "phase_transition_threshold": PHASE_TRANSITION_DELTA,
                     "phase_transitions": transitions,
                     "phase_transition_detected": bool(transitions)}
    scan["note"] = ("S2 主档 N=31 不在扫描档位内（完全二叉树 2^k−1），扫描用 "
                    "N∈{20,35,45,60} 完全二叉树；S1@20=S1、S6@45=S6 主档复用。")
    return scan


# ---------------------------------------------------------------- main
def main():
    t0 = time.time()
    cfg = DiffusionConfig()
    # 族选择：默认 ("S",)（SPEC §2 主终点）；--families S,L 时含族 L（辅助口径，
    # 图级符号检验族扩大如实披露；族 L 无 llm_prior 时该臂缺省）。
    import sys as _sys
    fams = ("S",)
    for a in _sys.argv[1:]:
        if a.startswith("--families="):
            fams = tuple(a.split("=", 1)[1].split(","))
    graphs = load_corpus(CORPUS_DIR, families=fams)
    if not graphs:
        raise RuntimeError(f"corpus empty: {CORPUS_DIR} — 先运行 mindmap_corpus_v20.py")
    per_graph = [eval_graph(g, cfg) for g in graphs]
    gids = [g["graph_id"] for g in per_graph]

    def named_hits(g, arm):
        return g["arms"][arm]["named"]["hits@3"]

    def filler_hits(g, arm):
        return g["arms"][arm]["filler"]["hits@3"]

    # ---- 图级符号检验（G=全部族 S 图；另报 6 主档灵敏度） ----
    d_rand = {g["graph_id"]: named_hits(g, "field_mean") - named_hits(g, "random")
              for g in per_graph}
    d_deg = {g["graph_id"]: named_hits(g, "field_mean") - named_hits(g, "degree")
             for g in per_graph}
    sign_tests = {
        "field_mean_minus_random": sign_test(list(d_rand.values())),
        "field_mean_minus_degree": sign_test(list(d_deg.values())),
        "G_graphs": len(gids)}
    sign_tests_primary6 = {
        "field_mean_minus_random": sign_test([d_rand[g] for g in PRIMARY_GRAPHS]),
        "field_mean_minus_degree": sign_test([d_deg[g] for g in PRIMARY_GRAPHS]),
        "G_graphs": len(PRIMARY_GRAPHS)}

    # ---- 图级 cluster bootstrap（B=10000，整图重采样）----
    boot = {
        "field_mean_named_level": cluster_bootstrap(
            gids, {g["graph_id"]: named_hits(g, "field_mean") for g in per_graph}),
        "field_mean_minus_random": cluster_bootstrap(gids, d_rand),
        "field_mean_minus_degree": cluster_bootstrap(gids, d_deg),
        "field_mean_filler_level": cluster_bootstrap(
            [g["graph_id"] for g in per_graph if g["n_filler"] > 0],
            {g["graph_id"]: filler_hits(g, "field_mean") for g in per_graph
             if g["n_filler"] > 0})}

    # ---- SPEC §2 判定（机械求值）----
    holm = holm_adjust({
        "H_A1_field_mean_gt_random": sign_tests["field_mean_minus_random"]["p_exact"],
        "H_A2_field_mean_gt_degree": sign_tests["field_mean_minus_degree"]["p_exact"]})
    reversals_vs_random = sorted(g for g, d in d_rand.items() if d < 0)
    reversals_vs_degree = sorted(g for g, d in d_deg.items() if d < 0)
    filler_eval = {g["graph_id"]: filler_hits(g, "field_mean")
                   for g in per_graph if g["n_filler"] > 0}
    filler_violations = sorted(g for g, v in filler_eval.items()
                               if v is not None and v >= H_B1_THRESHOLD)
    s6_named = named_hits(per_graph[gids.index("S6")], "field_mean")
    # S6 对照：v1.9 E9.2 全候选协议锚点值（results/deposon_v19_fullrank.json，
    # 只读）。H-S6 阈值 0.8 源自 N_NEG=10 协议的 v1.9 named≈天花板口径；
    # 同协议（E9.2 raw）锚点值为 0.4706，S6 对其逐位复现亦如实报告。
    v19_anchor = None
    v19_path = os.path.join(RESULTS, "deposon_v19_fullrank.json")
    if os.path.exists(v19_path):
        with open(v19_path, encoding="utf-8") as f:
            v19_anchor = json.load(f)["results"]["arms"]["field_mean"][
                "named"]["hits@3"]

    h_a1_sig = holm["H_A1_field_mean_gt_random"]["significant_holm"]
    h_a2_sig = holm["H_A2_field_mean_gt_degree"]["significant_holm"]
    kill_ha = bool((not h_a1_sig) or len(reversals_vs_random) >= KILL_REVERSAL_MIN)
    kill_hb1 = bool(len(filler_violations) >= H_B1_KILL_MIN)
    verdicts = {
        "H_A1_field_mean_gt_random": {
            "supported": h_a1_sig,
            "sign_test": sign_tests["field_mean_minus_random"],
            "holm": holm["H_A1_field_mean_gt_random"]},
        "H_A2_field_mean_gt_degree": {
            "supported": h_a2_sig,
            "sign_test": sign_tests["field_mean_minus_degree"],
            "holm": holm["H_A2_field_mean_gt_degree"]},
        "H_B1_filler_below_0.15": {
            "supported": bool(len(filler_violations) < H_B1_KILL_MIN),
            "threshold": H_B1_THRESHOLD,
            "per_graph_filler_hits3": filler_eval,
            "n_violations": len(filler_violations),
            "violating_graphs": filler_violations,
            "note": "S1 族纯链 filler=∅ 不参与本判定（如实披露）"},
        "H_S6_anchor_reproduction": {
            "supported": bool(s6_named is not None and s6_named >= H_S6_THRESHOLD),
            "threshold": H_S6_THRESHOLD, "S6_named_hits3": s6_named,
            "v19_e92_same_protocol_anchor": v19_anchor,
            "matches_v19_e92_anchor_exactly": bool(
                v19_anchor is not None and s6_named == v19_anchor),
            "note": ("S6 逐位复现 v1.9 E9.2 全候选协议锚点（结构镜像 + 同协议）；"
                     "未达 0.8 阈值——该阈值对应 v1.9 N_NEG=10 协议的 named 天花板"
                     "口径，协议差异如实披露，不作美化")},
        "kill_lines": {
            "H_A_dead": {"triggered": kill_ha,
                         "rule": ("H-A1 不显著（Holm 后）或 ≥3 张图效应反转 "
                                  "→ H-A 判死，转「适用边界」论文"),
                         "h_a1_not_significant": bool(not h_a1_sig),
                         "reversals_vs_random": reversals_vs_random,
                         "reversals_vs_degree": reversals_vs_degree,
                         "n_reversals_vs_random": len(reversals_vs_random)},
            "H_B1_boundary_retracted": {
                "triggered": kill_hb1,
                "rule": ("H-B1 在 ≥3 张图上 filler ≥0.15 → 「骨架检测器」"
                         "边界主张撤回"),
                "n_violations": len(filler_violations),
                "violating_graphs": filler_violations}}}

    scan = phase_scan(per_graph)
    named_table = {g["graph_id"]: {a: named_hits(g, a) for a in ARMS}
                   for g in per_graph}
    filler_table = {g["graph_id"]: {a: filler_hits(g, a) for a in ARMS}
                    for g in per_graph}

    out = {"experiment": "deposon_v20_corpus_eval", "spec_version": "v2.0",
           "spec": "docs/SPEC_v2.0.md §1–§2",
           "config": config_dict(cfg),
           "protocol": {
               "candidates": "全候选协议（E9.2 raw 口径）：候选 = 全部 N−1 个非自身"
                             "节点，金边在候选中，不剔除其他观测边；无负采样 ⇒ "
                             "采样器敏感性按构造归零",
               "metrics": "MRR / Hits@1 / Hits@3（0 基秩，mergesort 稳定序 + "
                          "1e-6 确定性微扰破平局）",
               "primary_endpoint": "每张图 named Hits@3，主臂 field_mean",
               "field_source_target": "每图 source/target 冻结于图 JSON"
                                      "（最长路径端点；S6=ROOT→GOAL 锚点）",
               "per_edge_seed": "rng=default_rng(graph_seed*100003+ei)；"
                                "场臂 inst_seed=graph_seed+ei",
               "arms": list(ARMS),
               "rule_filter": f"关键词表 {RULE_KEYWORDS}（E9.5 口径，纯标签字符串）",
               "llm_prior_arm": "族 S 不跑（标签与结构脱钩，SPEC §1：先验价值在族 L 检验）"},
           "corpus": {"dir": CORPUS_DIR, "n_graphs": len(gids),
                      "graph_ids": gids},
           "graph_level": {"named_hits3": named_table,
                           "filler_hits3": filler_table,
                           "sign_tests": sign_tests,
                           "sign_tests_primary6_sensitivity": sign_tests_primary6,
                           "cluster_bootstrap": boot,
                           "holm": holm},
           "s6_reproduction": verdicts["H_S6_anchor_reproduction"],
           "phase_scan": scan,
           "verdicts": verdicts,
           "per_graph": per_graph,
           "runtime_sec": round(time.time() - t0, 3),
           "honesty": [
               "no LLM API calls issued: 族 S 评估不读任何 LLM 缓存；llm_prior 臂"
               "按 SPEC §1 不在族 S 主报（标签与结构脱钩，先验价值留族 L 检验）。",
               "named/filler 冻结口径：链/树父子主链与 DAG 最长路径族=named，其余"
               "=filler，无诱饵边；S1 纯链 filler=∅，filler 类指标为 None 如实报告。",
               "S2 平衡树无唯一主干：named 操作化为「子节点仍为内部节点的父子边」，"
               "filler=叶边（v1.9 filler=叶部口径），已在生成器冻结披露。",
               "S3 场引导 target=hub0（单目标场对三 hub 结构的必要选取），该选取"
               "偏向分支 0 的 named 边，如实披露。",
               "Holm 族规模 m=4（SPEC §2 预登记 4 检验），其中 H-B1/H-S6 为确定性"
               "阈值规则无 p 值，仅两个符号检验进入 Holm 序列（保守口径）。",
               "overall 一律非劣效口径（TOST 0.03，SPEC §2）：本评估不作 overall "
               "单信号优效主张；边级 McNemar 未报（图内 LOO 依赖，图级符号检验为主）。",
               "图级符号检验含扫描变体（G=16，同族不同尺寸相关），6 主档灵敏度"
               "分析并列报告。",
               "阴性结果与斩杀线触发状态机械求值、如实写入 verdicts，不美化。"]}
    os.makedirs(RESULTS, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({
        "out": OUT_PATH, "runtime_sec": out["runtime_sec"],
        "named_hits3": named_table, "filler_hits3_field_mean": filler_eval,
        "sign_tests": sign_tests, "holm": holm,
        "S6_named": s6_named,
        "phase_transitions": {k: v["phase_transitions"] for k, v in scan.items()
                              if isinstance(v, dict) and "phase_transitions" in v},
        "kill_lines": {k: v["triggered"] for k, v in verdicts["kill_lines"].items()}},
        ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
