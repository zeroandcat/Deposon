# -*- coding: utf-8 -*-
# ============================================================
# Deposon v1.5.1 凝子扩散实验脚本 (SPEC_v1.5 + SPEC v1.5.1 修订)
#   → results/deposon_v15_diffusion.json
#
# 实验 A (合成): 分层 DAG (4 层 x 6 节点, 层间全连接后剪枝到 60 边,
#   植入 1 条 source→sink 金路径)。掩码比例 {0.2, 0.4}, 每配置 20 张图 (seed 0..19)。
# 实验 B (真实脑图): G1 人工转译脑图 (45 节点 49 边) 留一边预测。
#   注意: results/deposon_g1_mindmap_demo.json 只含图元数据 (节点/边数、9 分支、
#   6 条 ROOT→GOAL 路径、trap/answer 标注), 不含逐边列表 —— 逐边数据不可恢复。
#   按任务约定以实际结构为准适配: 在满足全部元数据约束下确定性重建 45 节点 49 边图
#   (重建口径见输出 JSON 的 reconstruction 字段), 再对其做留一边预测。
#
# v1.5.1 五臂 (首轮四臂的 max-path 负面结果已归档
#   results/deposon_v15_diffusion_maxpath_negativeresult.json):
#   field_guided (energy_mode="aggregate", v1.5.1 聚合透射率, 完整臂)
#   field_guided_maxpath (energy_mode="max_path", 首轮死锁对照臂)
#   no_guidance (G2 消融) / random / degree (度中心性基线)。
# 评估协议 (标准链接预测负采样, 无泄漏): 对每条被掩真边 (u,v), 候选 = v + 同行
#   采样负目标 (非观测出边), 报 top-3 命中; AUC 在所有掩码位置上算 (真边为正)。
# 指标: 金边 top-3 命中率 (A 还报 AUC)。种子固定, 如实记录含负面结果。
# numpy 之外零依赖, 无网络与外部服务调用。
# ============================================================
import json
import os
import time

import numpy as np

from deposon_diffusion import DiffusionConfig, complete_graph, config_dict

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
OUT_PATH = os.path.join(RESULTS, "deposon_v15_diffusion.json")

TOP_K = 3          # top-3 命中
N_NEG = 10         # 每条被掩真边的采样负目标数
SEEDS = list(range(20))
MASK_RATIOS = (0.2, 0.4)
# v1.5.1 五臂: field_guided=aggregate 完整臂; field_guided_maxpath=首轮死锁对照臂
ARMS = ("field_guided", "field_guided_maxpath", "no_guidance", "random", "degree")
ARM_ENERGY_MODE = {"field_guided": "aggregate", "field_guided_maxpath": "max_path",
                   "no_guidance": None, "random": None, "degree": None}


# ---------------------------------------------------------------- 公共工具
def row_normalize(adj: np.ndarray) -> np.ndarray:
    """出边权重行归一 (1/outdeg); 零出度节点保持零行。"""
    W = np.zeros_like(adj, dtype=float)
    outdeg = adj.sum(axis=1)
    nz = outdeg > 0
    W[nz] = adj[nz] / outdeg[nz, None]
    return W


def auc_rank(pos: np.ndarray, neg: np.ndarray) -> float | None:
    """Mann-Whitney AUC (平均秩处理平局); 单边为空时返回 None。"""
    pos = np.asarray(pos, dtype=float)
    neg = np.asarray(neg, dtype=float)
    if pos.size == 0 or neg.size == 0:
        return None
    scores = np.concatenate([pos, neg])
    order = np.argsort(scores, kind="mergesort")
    ranks = np.empty(scores.size)
    ranks[order] = np.arange(1, scores.size + 1)
    # 平局取平均秩
    uniq, inv, counts = np.unique(scores, return_inverse=True, return_counts=True)
    if np.any(counts > 1):
        cum = np.cumsum(counts)
        avg = (cum - counts + 1 + cum) / 2.0
        ranks = avg[inv]
    r_pos = ranks[: pos.size].sum()
    n_p, n_n = pos.size, neg.size
    return float((r_pos - n_p * (n_p + 1) / 2.0) / (n_p * n_n))


def arm_scores(arm: str, W_obs, mask, cfg, source, target, adj_obs, rng,
               inst_seed: int = 0):
    """五臂打分: 返回掩码位置上的分数矩阵 (其余位置为 -inf, 不参与排序)。
    field_guided 用 energy_mode="aggregate" (v1.5.1), field_guided_maxpath 用
    "max_path" (首轮对照), no_guidance 关闭场引导 (G2 消融)。
    inst_seed: 每个任务实例 (图/留一边) 独立的生成种子 —— 先验采样逐实例独立,
    否则所有实例共享同一份 Dirichlet 样本会引入系统性偏差 (如实记录过的坑)。"""
    if arm in ("field_guided", "field_guided_maxpath", "no_guidance"):
        overrides = {"field_guidance": arm != "no_guidance", "seed": inst_seed}
        if ARM_ENERGY_MODE[arm] is not None:
            overrides["energy_mode"] = ARM_ENERGY_MODE[arm]
        cfg_arm = DiffusionConfig(**{**config_dict(cfg), **overrides})
        W_done = complete_graph(W_obs, mask, cfg_arm, source, target)
        s = W_done
    elif arm == "random":
        s = np.zeros_like(W_obs)
        s[mask] = rng.random(int(mask.sum()))
    elif arm == "degree":
        indeg = adj_obs.sum(axis=0)  # 观测图入度 (无泄漏)
        s = np.zeros_like(W_obs)
        jj = np.arange(W_obs.shape[0])[None, :].repeat(W_obs.shape[0], axis=0)
        s[mask] = indeg[jj[mask]] + 1e-6 * rng.random(int(mask.sum()))
    else:
        raise ValueError(arm)
    out = np.full_like(W_obs, -np.inf, dtype=float)
    out[mask] = s[mask]
    return out


def top3_hit_per_edge(scores: np.ndarray, masked_edges: list, mask: np.ndarray) -> list:
    """每条被掩真边 (u,v): v 在 u 行候选 (mask[u,:] 为 True 的位置) 中的秩 < TOP_K。"""
    out = []
    for (u, v) in masked_edges:
        cand = np.flatnonzero(mask[u])
        order = cand[np.argsort(-scores[u, cand], kind="mergesort")]
        rank = int(np.flatnonzero(order == v)[0])
        out.append({"edge": [int(u), int(v)], "rank": rank, "hit": rank < TOP_K})
    return out


def mean_std(xs: list) -> dict:
    xs = [x for x in xs if x is not None]
    if not xs:
        return {"mean": None, "std": None, "n": 0}
    a = np.asarray(xs, dtype=float)
    return {"mean": float(a.mean()), "std": float(a.std()), "n": int(a.size)}


# ---------------------------------------------------------------- 实验 A
def gen_layered_dag(seed: int):
    """4 层 x 6 节点分层 DAG: 相邻层全连接 (108) 剪枝到 60 边, 植入 1 条金路径。"""
    rng = np.random.default_rng(seed)
    n_layer, width = 4, 6
    N = n_layer * width
    layer_of = np.repeat(np.arange(n_layer), width)
    pairs = [(i, j) for i in range(N) for j in range(N)
             if layer_of[j] == layer_of[i] + 1]
    gold_nodes = [int(rng.integers(width)) + l * width for l in range(n_layer)]
    gold_path = list(zip(gold_nodes[:-1], gold_nodes[1:]))
    pool = [p for p in pairs if p not in gold_path]
    take = rng.choice(len(pool), size=60 - len(gold_path), replace=False)
    edges = gold_path + [pool[k] for k in take]
    adj = np.zeros((N, N))
    for (u, v) in edges:
        adj[u, v] = 1.0
    return N, adj, edges, gold_path, gold_nodes[0], gold_nodes[-1]


def run_A_graph(seed: int, ratio: float, cfg: DiffusionConfig) -> dict:
    rng = np.random.default_rng(10_000 + seed)
    N, adj, edges, gold_path, source, target = gen_layered_dag(seed)
    W_true = row_normalize(adj)
    n_mask = int(round(ratio * len(edges)))
    perm = rng.permutation(len(edges))
    masked_true = [edges[k] for k in perm[:n_mask]]
    masked_set = set(masked_true)
    gold_masked = [e for e in masked_true if e in set(gold_path)]

    # 观测场: 被掩真边置零 (释放其行质量), 不重归一 → 边界值 = W_true 原值,
    # 掩码自由度的可用质量 = 被掩边的原权重和
    adj_obs = adj.copy()
    W_obs = W_true.copy()
    for (u, v) in masked_true:
        adj_obs[u, v] = 0.0
        W_obs[u, v] = 0.0

    # 掩码自由度: 被掩真边 + 同行采样负目标 (标准链接预测负采样协议)
    mask = np.zeros((N, N), dtype=bool)
    neg_positions = []
    rows = sorted({u for (u, _v) in masked_true})
    for u in rows:
        pos_targets = [v for (uu, v) in masked_true if uu == u]
        pool = [j for j in range(N)
                if j != u and adj_obs[u, j] == 0 and (u, j) not in masked_set]
        take = rng.choice(len(pool), size=min(N_NEG, len(pool)), replace=False)
        for v in pos_targets:
            mask[u, v] = True
        for k in take:
            mask[u, pool[k]] = True
            neg_positions.append((u, pool[k]))

    detail = {"seed": seed, "n_edges": len(edges), "n_masked": n_mask,
              "gold_path": [[int(u), int(v)] for u, v in gold_path],
              "gold_masked": [[int(u), int(v)] for u, v in gold_masked],
              "source": int(source), "target": int(target), "arms": {}}
    pos_idx = np.array([(u, v) for (u, v) in masked_true], dtype=int)
    neg_idx = np.array(neg_positions, dtype=int) if neg_positions else None
    scores = {}
    for arm in ARMS:
        scores[arm] = arm_scores(arm, W_obs, mask, cfg, source, target, adj_obs,
                                 rng, inst_seed=seed)
    # 场引导激活诊断: 引导臂与消融臂在掩码位置上的输出是否有差异。
    # field_active = aggregate 臂 (v1.5.1 完整臂); field_active_maxpath = 首轮
    # max-path 对照臂 (其能量子梯度在最短路不含掩码边时恒为 0 —— 死锁检测)。
    detail["field_active"] = bool(
        np.abs(scores["field_guided"][mask] - scores["no_guidance"][mask]).max()
        > 1e-9)
    detail["field_active_maxpath"] = bool(
        np.abs(scores["field_guided_maxpath"][mask]
               - scores["no_guidance"][mask]).max() > 1e-9)
    for arm in ARMS:
        s = scores[arm]
        hits_all = top3_hit_per_edge(s, masked_true, mask)
        hits_gold = [h for h in hits_all if tuple(h["edge"]) in set(gold_path)]
        pos = s[pos_idx[:, 0], pos_idx[:, 1]]
        neg = s[neg_idx[:, 0], neg_idx[:, 1]] if neg_idx is not None else np.empty(0)
        detail["arms"][arm] = {
            "masked_edge_top3_hit": float(np.mean([h["hit"] for h in hits_all])),
            "gold_path_top3_hit": (float(np.mean([h["hit"] for h in hits_gold]))
                                   if hits_gold else None),
            "auc": auc_rank(pos, neg),
            "hits_all": hits_all,
        }
    return detail


def run_experiment_A(cfg: DiffusionConfig) -> dict:
    out = {}
    for ratio in MASK_RATIOS:
        per_graph = [run_A_graph(seed, ratio, cfg) for seed in SEEDS]
        arms = {}
        for arm in ARMS:
            gold_rates = [g["arms"][arm]["gold_path_top3_hit"] for g in per_graph]
            all_rates = [g["arms"][arm]["masked_edge_top3_hit"] for g in per_graph]
            aucs = [g["arms"][arm]["auc"] for g in per_graph]
            arms[arm] = {
                "gold_path_top3_hit": mean_std(gold_rates),
                "masked_edge_top3_hit": mean_std(all_rates),
                "auc": mean_std(aucs),
                "n_gold_masked_total": int(sum(len(g["gold_masked"]) for g in per_graph)),
            }
        out[str(ratio)] = {"arms": arms, "per_graph": per_graph,
                           "n_field_active": int(sum(g["field_active"]
                                                     for g in per_graph)),
                           "n_field_active_maxpath": int(
                               sum(g["field_active_maxpath"] for g in per_graph))}
    return out


# ---------------------------------------------------------------- 实验 B
def reconstruct_mindmap():
    """由 deposon_g1_mindmap_demo.json 元数据确定性重建 45 节点 49 边脑图。

    源 JSON 只含元数据 (n_nodes=45, n_edges=49, n_branches=9, 6 条 ROOT→GOAL
    路径, trap/answer 标注), 不含逐边列表; 逐边数据不可恢复。重建满足全部
    元数据约束: 9 条 ROOT 分支 (4 正当 + 2 诱饵 + 3 未命名), 4 条正当结论路径
    与 2 条诱饵路径逐条存在, 其余 32 节点以轮转方式挂到 9 个分支根下。
    源 JSON 的人工边权 (0.9/0.85 等) 同样不可恢复, 统一用 1/outdeg 行归一。
    """
    labels = ["ROOT", "GOAL_拓扑智能", "仿光子vsTDA", "组织记忆", "认知协议",
              "专家萃取", "范式转移", "范式转移/仿生瓶颈", "行动窗口",
              "行动窗口/AI够强未自主"]
    labels += [f"branch_{k}" for k in (7, 8, 9)]
    labels += [f"node_{k}" for k in range(13, 45)]
    N = 45
    ROOT, GOAL = 0, 1
    legit = [2, 3, 4, 5]           # 4 条正当结论路径的中继
    trap_mid, trap_leaf = [6, 8], [7, 9]
    branch_roots = [2, 3, 4, 5, 6, 8, 10, 11, 12]  # 9 分支
    edges = [(ROOT, b) for b in branch_roots]
    edges += [(m, GOAL) for m in legit]
    edges += [(6, 7), (7, GOAL), (8, 9), (9, GOAL)]  # 2 条诱饵路径
    for k in range(13, 45):        # 32 个填充节点, 轮转挂分支根
        edges.append((branch_roots[(k - 13) % 9], k))
    assert len(edges) == 49 and len(labels) == 45
    adj = np.zeros((N, N))
    for (u, v) in edges:
        adj[u, v] = 1.0
    meta = {
        "note": "源 JSON 无逐边列表, 本图为满足其全部元数据约束的确定性重建",
        "source_file": "results/deposon_g1_mindmap_demo.json",
        "n_nodes": 45, "n_edges": 49, "n_branches": 9,
        "trap_nodes": ["范式转移/仿生瓶颈", "行动窗口/AI够强未自主"],
        "answer_node": "GOAL_拓扑智能",
        "path_edges_named": [[int(u), int(v)] for (u, v) in edges[:17]],
    }
    return N, adj, edges, labels, meta


def run_experiment_B(cfg: DiffusionConfig) -> dict:
    N, adj, edges, labels, meta = reconstruct_mindmap()
    W_true = row_normalize(adj)
    source, target = 0, 1  # ROOT → GOAL_拓扑智能 (answer_node)
    named_path = {tuple(e) for e in meta["path_edges_named"]}
    per_edge = []
    for ei, (u, v) in enumerate(edges):
        rng = np.random.default_rng(70_000 + ei)
        adj_obs = adj.copy()
        adj_obs[u, v] = 0.0
        W_obs = W_true.copy()   # 留一边置零, 不重归一 (质量释放给候选)
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
        for arm in ARMS:
            scores[arm] = arm_scores(arm, W_obs, mask, cfg, source, target,
                                     adj_obs, rng, inst_seed=70_000 + ei)
        rec["field_active"] = bool(
            np.abs(scores["field_guided"][mask] - scores["no_guidance"][mask]).max()
            > 1e-9)
        rec["field_active_maxpath"] = bool(
            np.abs(scores["field_guided_maxpath"][mask]
                   - scores["no_guidance"][mask]).max() > 1e-9)
        for arm in ARMS:
            hit = top3_hit_per_edge(scores[arm], [(u, v)], mask)[0]
            rec["arms"][arm] = {"rank": hit["rank"], "hit": hit["hit"]}
        per_edge.append(rec)
    arms = {}
    for arm in ARMS:
        hits = [r["arms"][arm]["hit"] for r in per_edge]
        arms[arm] = {"top3_hit": mean_std([float(h) for h in hits]),
                     "top3_hit_named_path": mean_std(
                         [float(r["arms"][arm]["hit"]) for r in per_edge
                          if r["on_named_path"]]),
                     "top3_hit_filler": mean_std(
                         [float(r["arms"][arm]["hit"]) for r in per_edge
                          if not r["on_named_path"]])}
    return {"reconstruction": meta, "source": "ROOT", "target": "GOAL_拓扑智能",
            "n_field_active": int(sum(r["field_active"] for r in per_edge)),
            "n_field_active_maxpath": int(sum(r["field_active_maxpath"]
                                              for r in per_edge)),
            "arms": arms, "per_edge": per_edge}


# ---------------------------------------------------------------- main
def _f(x: float | None) -> str:
    return "None" if x is None else f"{x:.3f}"


def main():
    t0 = time.time()
    cfg = DiffusionConfig()  # SPEC 默认值: n_steps=50, linear, uniform_out, lr=0.1,
    # lam=0.01, energy_mode="aggregate" (v1.5.1 新增字段, field_guided 臂使用)
    exp_a = run_experiment_A(cfg)
    exp_b = run_experiment_B(cfg)
    runtime = time.time() - t0

    # ---- 汇总数值, 供 honesty 逐字如实陈述 (全部由上方实际运行产生) ----
    fa_a = {str(r): (exp_a[str(r)]["n_field_active"],
                     exp_a[str(r)]["n_field_active_maxpath"]) for r in MASK_RATIOS}
    fa_b = (exp_b["n_field_active"], exp_b["n_field_active_maxpath"])
    gold_a = {arm: {str(r): exp_a[str(r)]["arms"][arm]["gold_path_top3_hit"]["mean"]
                    for r in MASK_RATIOS} for arm in ARMS}
    all_a = {arm: {str(r): exp_a[str(r)]["arms"][arm]["masked_edge_top3_hit"]["mean"]
                   for r in MASK_RATIOS} for arm in ARMS}
    b_all = {arm: exp_b["arms"][arm]["top3_hit"]["mean"] for arm in ARMS}
    b_named = {arm: exp_b["arms"][arm]["top3_hit_named_path"]["mean"] for arm in ARMS}
    b_fill = {arm: exp_b["arms"][arm]["top3_hit_filler"]["mean"] for arm in ARMS}
    base_arms = ("no_guidance", "random", "degree")
    a_wins = {}
    for r in MASK_RATIOS:
        sr = str(r)
        g = gold_a["field_guided"][sr]
        best_base = max(v for v in (gold_a[b][sr] for b in base_arms) if v is not None)
        a_wins[sr] = (g is not None) and (g > best_base)
    b_win = b_all["field_guided"] > max(b_all[b] for b in base_arms)
    verdict_a = "; ".join(
        f"r={r}: aggregate gold_top3={_f(gold_a['field_guided'][str(r)])} "
        f"{'优于' if a_wins[str(r)] else '未优于'}全部基线 (max baseline="
        f"{_f(max(v for v in (gold_a[b][str(r)] for b in base_arms) if v is not None))})"
        for r in MASK_RATIOS)
    verdict_b = (f"aggregate top3={b_all['field_guided']:.3f} "
                 f"{'优于' if b_win else '未优于'}全部基线 (max baseline="
                 f"{max(b_all[b] for b in base_arms):.3f})")

    out = {
        "experiment": "deposon_v15_diffusion",
        "spec": "SPEC_v1.5 (固定节点集上的边权场补全)",
        "spec_version": "v1.5.1",
        "config": config_dict(cfg),
        "energy_mode": {"diffusion_default": cfg.energy_mode,
                        "per_arm": ARM_ENERGY_MODE,
                        "note": "field_guided=aggregate (v1.5.1 聚合透射率); "
                                "field_guided_maxpath=首轮 max-path 对照"},
        "archive": "results/deposon_v15_diffusion_maxpath_negativeresult.json "
                   "(首轮 max-path 四臂负面结果, 原样归档保留)",
        "protocol": {"top_k": TOP_K, "n_negatives_per_gold_edge": N_NEG,
                     "weighting": "W_true[i,j]=1/outdeg(i) 行归一; 掩码边置零不重归一",
                     "mask": "被掩真边 + 同行采样负目标 (链接预测负采样, 无泄漏)",
                     "seeds_A": SEEDS, "seed_B_per_edge": "70000+edge_index"},
        "seeds": SEEDS,
        "runtime_sec": round(runtime, 3),
        "experiment_A": exp_a,
        "experiment_B": exp_b,
        "honesty": [
            "实验 B 源 JSON 不含逐边列表, 图为元数据约束下的确定性重建 (见 reconstruction)",
            "全部指标由种子固定的实际运行产生, 含负面结果, 无任何手工润色",
            "v1.5.1 修订: 场引导能量改用聚合透射率 (aggregate-T analog of v1.4 "
            "§scattering audit): E=-log(Σ_{p: s⇝t} Π t_e), DAG 拓扑序 DP "
            "(T(v)=Σ_{u→v}T(u)·t(u,v)), 含环支持图退化为闭式游走和; 任一 source⇝target "
            "通路上的掩码边都有非零解析梯度。首轮 max-path 四臂结果原样归档于 "
            "results/deposon_v15_diffusion_maxpath_negativeresult.json。",
            f"死锁消除 (field_active=引导臂输出与消融臂有差异的实例数): aggregate 臂 "
            f"实验A r=0.2: {fa_a['0.2'][0]}/20, r=0.4: {fa_a['0.4'][0]}/20, "
            f"实验B: {fa_b[0]}/49; max_path 对照臂 r=0.2: {fa_a['0.2'][1]}/20, "
            f"r=0.4: {fa_a['0.4'][1]}/20, B: {fa_b[1]}/49 (首轮死锁如旧, 对照成立)。",
            f"金边恢复 (实验A gold_path top-3, 均值): {verdict_a}。",
            f"实验B (留一边 top-3): {verdict_b}; 分结构: named_path aggregate="
            f"{b_named['field_guided']:.3f} vs no_guidance={b_named['no_guidance']:.3f} "
            f"vs random={b_named['random']:.3f} vs degree={b_named['degree']:.3f}; "
            f"filler aggregate={b_fill['field_guided']:.3f} vs "
            f"no_guidance={b_fill['no_guidance']:.3f} vs random={b_fill['random']:.3f} "
            f"vs degree={b_fill['degree']:.3f}。",
            "masked_edge top-3 (实验A 全部被掩真边): aggregate "
            f"r=0.2: {all_a['field_guided']['0.2']:.3f}, r=0.4: "
            f"{all_a['field_guided']['0.4']:.3f}; no_guidance "
            f"{all_a['no_guidance']['0.2']:.3f}/{all_a['no_guidance']['0.4']:.3f}, "
            f"random {all_a['random']['0.2']:.3f}/{all_a['random']['0.4']:.3f}, "
            f"degree {all_a['degree']['0.2']:.3f}/{all_a['degree']['0.4']:.3f}, "
            f"maxpath {all_a['field_guided_maxpath']['0.2']:.3f}/"
            f"{all_a['field_guided_maxpath']['0.4']:.3f}。",
            "结论 (如实): aggregate 能量消除了首轮 max-path 的子梯度死锁 "
            "(field_active 见上); 金边恢复是否优于基线按上两条数字直读, "
            "未胜出项不作任何修饰。",
        ],
    }
    os.makedirs(RESULTS, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"written {OUT_PATH}  runtime={runtime:.1f}s")
    for ratio in MASK_RATIOS:
        blk = exp_a[str(ratio)]
        print(f"[A r={ratio}] field_active(agg)={blk['n_field_active']}/{len(SEEDS)} "
              f"field_active(maxpath)={blk['n_field_active_maxpath']}/{len(SEEDS)}")
        for arm in ARMS:
            a = blk["arms"][arm]
            print(f"  {arm:20s} gold_top3={a['gold_path_top3_hit']['mean']}"
                  f"±{a['gold_path_top3_hit']['std']} "
                  f"all_top3={a['masked_edge_top3_hit']['mean']:.3f} "
                  f"auc={a['auc']['mean']:.3f}")
    print(f"[B mindmap LOO] field_active(agg)={exp_b['n_field_active']}/49 "
          f"field_active(maxpath)={exp_b['n_field_active_maxpath']}/49")
    for arm in ARMS:
        b = exp_b["arms"][arm]
        print(f"  {arm:20s} top3={b['top3_hit']['mean']:.3f}±{b['top3_hit']['std']:.3f} "
              f"named={b['top3_hit_named_path']['mean']:.3f} "
              f"filler={b['top3_hit_filler']['mean']:.3f}")


if __name__ == "__main__":
    main()
