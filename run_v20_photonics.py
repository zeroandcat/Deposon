# -*- coding: utf-8 -*-
# v2.0 光子硬件映射实验（deposon_photonics.py，零 API）
#   → results/deposon_v20_photonics.json
# 实验（兑现 v1.4 roadmap「PCM/MZI/ECM → 光子芯片」前瞻）：
#   P1 等价性：抽象散射 t/r/a vs 硬件级 ring+MZI+PCM 实现（守恒 + 排序一致）；
#   P2 损耗预算与可行性：22 图逐图真实最长路径损耗 dB 与可探测性（NEP 判据），
#      给出"当前集成工艺可制造的图规模"判定；
#   P3 拓扑优化：naive/bus/hybrid 三拓扑组件数与总插损对比，推荐配置；
#   P4 退火=相位斜坡：非理想相位噪声敏感性（保真度曲线）。
# 修正史（R1 深探实锤）：NEP 单位 bug（1 pW=1e-9 mW，曾误 ×1e-3 下限严 10^6 倍）
# + max_hops=10 截断 + 索引贪心 → 真最长路径 DP + 单位修正，14/22→18/22、≈27 跳。
# no LLM API calls issued。
import json
import os
import time

import numpy as np

from mindmap_corpus_v20 import CORPUS_DIR, load_corpus
import deposon_photonics as ph

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(HERE, "results", "deposon_v20_photonics.json")


def p1_equivalence(graphs):
    """抽象模型 vs 硬件模型：散射守恒 + S6 上两跳内候选排序一致率。"""
    cons = ph.hardware_tra(None, g_couple=1.0, g_aether=0.3)
    g6 = graphs["S6"]
    adj = np.zeros((g6["N"], g6["N"]))
    for (u, v) in [tuple(e) for e in g6["edges"]]:
        adj[u, v] = 1.0
    hw = ph.hardware_scores(adj, g6["source"], g6["target"])
    named = {tuple(e) for e in g6["named_edges"]}
    hits = sum(1 for (u, v) in named if u == g6["source"] and hw.get(v, 0) > 0)
    return {"conservation_err": cons["conservation_err"],
            "t_r_a_hw": {"t": cons["t"], "r": cons["r"], "a": cons["a"]},
            "s6_direct_named_reachable": f"{hits}/{sum(1 for e in named if e[0]==g6['source'])}",
            "note": "守恒偏差为浮点零（同式实现）；硬件模型与抽象模型共享"
                    "散射公式，等价性在公式层成立（一阶组件模型）"}


def p2_feasibility(graphs):
    """逐图：真实最长路径（DAG DP）损耗 + 可探测性（残余功率 vs NEP 判据）。"""
    per_graph = {}
    for gid, g in graphs.items():
        N = g["N"]
        adj = np.zeros((N, N))
        for (u, v) in [tuple(e) for e in g["edges"]]:
            adj[u, v] = 1.0
        nl = ph.compile_graph_to_netlist(adj, g["source"], g["target"])
        # 真实最长路径（DAG 上 DP，从 source 出发；R1 复核修正：原为
        # min(10, n_named) 任意截断 + 索引贪心，S1 19 跳被截 9 跳）
        order = sorted(range(N))
        dist = {g["source"]: 0}
        parent = {}
        for u in order:
            if u not in dist:
                continue
            for v in range(N):
                if adj[u, v] > 0 and dist.get(v, -1) < dist[u] + 1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
        end = max(dist, key=dist.get)
        path = [end]
        while path[-1] != g["source"]:
            path.append(parent[path[-1]])
        path = path[::-1]
        loss = ph.netlist_loss_db(nl, path)
        residual_mw = ph.path_transmission(nl, path)
        nep_floor_mw = 10 * ph.P["nep_pw"] * 1e-9  # 10× NEP@1Hz, pW→mW（1 pW=1e-9 mW；R1 复核修正：曾误 ×1e-3 使下限严 10^6 倍）
        per_graph[gid] = {"N": N, "path_hops": len(path) - 1,
                          "loss_db": round(loss, 2),
                          "residual_mw": float(f"{residual_mw:.3e}"),
                          "detectable": bool(residual_mw > nep_floor_mw)}
    n_ok = sum(1 for v in per_graph.values() if v["detectable"])
    max_loss = max(v["loss_db"] for v in per_graph.values())
    return {"per_graph": per_graph, "detectable_graphs": f"{n_ok}/{len(per_graph)}",
            "max_path_loss_db": max_loss,
            "detection_rule": "残余功率 > 10×NEP@1Hz（1 pW/√Hz，TYPICAL）",
            "feasibility_note": (
                f"22 图中 {n_ok} 图可探测、{len(per_graph)-n_ok} 图不可探测"
                "（真最长路径 DP 口径，R1 复核修正后）：规模定律每跳 ~2.9 dB，"
                "10×NEP@1Hz（正确单位 1 pW=1e-9 mW）对应阈值 ≈27 跳；"
                "不可探测图 = 长链/深层结构（S1 族长链 34–59 跳、"
                "L_algorithm_process 29 跳），需中继放大或更低损耗工艺；"
                "枢纽型浅层结构（S6 族 2 跳、L 多数 ≤20 跳）天然适配光子实现。"
                "修正史：曾因 NEP 单位错（×1e-3）得 14/22 与「14 跳」伪规则，"
                "且 max_hops=10 截断掩盖真实链长，经 R1 深探实锤更正。")}


def p3_topology(graphs):
    g6 = graphs["S6"]
    adj = np.zeros((g6["N"], g6["N"]))
    for (u, v) in [tuple(e) for e in g6["edges"]]:
        adj[u, v] = 1.0
    return ph.optimize_topology(adj, g6["source"], g6["target"])


def p4_ramp_sensitivity():
    ideal = ph.annealing_phase_ramp(50, 0.9, 0.0)
    rows = []
    for sigma in (0.0, 0.01, 0.05, 0.1, 0.2):
        r = ph.ramp_fidelity(ideal, sigma, n_realizations=50)
        rows.append(r)
    return {"ramp_ideal_cum_final": ideal[49]["cum_phase"],
            "sensitivity": rows,
            "note": "σ≤0.05 rad 时保真度偏差 <σ 量级（斜坡累积相位的噪声不放大）；"
                    "热相移器典型控制精度 ~0.01–0.05 rad（TYPICAL）下退火调度"
                    "硬件可实现；σ≥0.2 rad 时噪声超过单步进(0.9^t 后期)，"
                    "需反馈稳相——硬件边界如实标注"}


def main():
    t0 = time.time()
    graphs = {g["graph_id"]: g for g in load_corpus(CORPUS_DIR, families=("S", "L"))}
    out = {"experiment": "deposon_v20_photonics", "spec_version": "v2.0",
           "spec": "v1.4 roadmap 硬件映射（PCM/MZI/ECM → 光子芯片）兑现",
           "scope": ("组件级一阶数值模型（ring/MZI/PCM/耦合器传递函数 + "
                     "SiPh/SiN 典型损耗区间），非流片、非 SPICE 级仿真；"
                     "参数标注 TYPICAL，非任何具体 PDK 保证值"),
           "P1_equivalence": p1_equivalence(graphs),
           "P2_feasibility": p2_feasibility(graphs),
           "P3_topology_optimization": p3_topology(graphs),
           "P4_ramp_sensitivity": p4_ramp_sensitivity(),
           "runtime_sec": round(time.time() - t0, 3),
           "honesty": [
               "no LLM API calls issued：全部本地一阶数值模型。",
               "本实验验证的是**映射自洽性**（抽象散射公式可由 ring+MZI+PCM "
               "组件实现且守恒）与**一阶可行性**（损耗预算/可探测性/拓扑损耗），"
               "不构成对任何具体工艺线的制造承诺。",
               "PCM 阈值能量、NEP、损耗参数均为文献典型量级（TYPICAL 标注），"
               "真实 PDK 需按具体工艺重估；损耗模型不含色散/温漂/串扰频谱细节。",
               "P4 的相位斜坡是退火调度的硬件类比演示，非声称已造出器件。"]}
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({"P1": out["P1_equivalence"],
                      "P2_detectable": out["P2_feasibility"]["detectable_graphs"],
                      "P2_max_loss_db": out["P2_feasibility"]["max_path_loss_db"],
                      "P3_recommended": out["P3_topology_optimization"]["recommended"],
                      "P4_max_dev": out["P4_ramp_sensitivity"]["sensitivity"][-1]},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
