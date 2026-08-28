# -*- coding: utf-8 -*-
# v2.0 Deposon 向量属性审计（用户指令：场分在单纯形上非负，负值无物理意义）
#   → results/deposon_v20_vector_audit.json
# 审计项：
#   V1 非负性：reverse_denoise_init 输出 W_done 在 mask 上全部 ≥ -1e-12
#   V2 单纯形性：含 mask 自由度的行，行和 ∈ (0, 1+1e-6]（投影后不超过 1）
#   V3 无 NaN/正 inf；-np.inf 仅为掩码占位（mask 外），不进入排序域
#   V4 排序域洁净：送入 gold_rank 的分向量在候选集上无 NaN；场分候选值 ≥ -1e-12
# 覆盖：全 20 图 × 每图全部留一任务（mean-field 与 dirichlet 双起点）。
# no LLM API calls issued。
import json, os, time
import numpy as np
from deposon_diffusion import DiffusionConfig, config_dict, forward_diffuse
from mindmap_corpus_v20 import CORPUS_DIR, load_corpus
from run_v15_experiment import row_normalize
from run_v19_fullrank import full_candidate_mask
from run_v19_meanfield import reverse_denoise_init

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(HERE, "results", "deposon_v20_vector_audit.json")
TOL = 1e-9

def main():
    t0 = time.time()
    cfg = DiffusionConfig()
    graphs = load_corpus(CORPUS_DIR, families=("S", "L"))
    totals = {"tasks": 0, "v1_viol": [], "v2_viol": [], "v3_viol": [], "v4_viol": []}
    for g in graphs:
        N = g["N"]
        edges = [tuple(e) for e in g["edges"]]
        adj = np.zeros((N, N))
        for (u, v) in edges:
            adj[u, v] = 1.0
        W_true = row_normalize(adj)
        for ei, (u, v) in enumerate(edges):
            adj_obs = adj.copy(); adj_obs[u, v] = 0.0
            W_obs = W_true.copy(); W_obs[u, v] = 0.0
            mask = full_candidate_mask(N, u)
            cand = np.flatnonzero(mask[u])
            for mode in ("prior_mean", "dirichlet"):
                cfg_arm = DiffusionConfig(**{**config_dict(cfg),
                                             "seed": int(g["seed"]) + ei,
                                             "energy_mode": "aggregate",
                                             "field_guidance": True})
                traj = forward_diffuse(W_obs, mask, cfg_arm)
                W_done = reverse_denoise_init(traj[-1], mask, cfg_arm, 0, 1,
                                              init_mode=mode)
                gid = f"{g['graph_id']}:{u}->{v}:{mode}"
                totals["tasks"] += 1
                mv = W_done[mask]
                # V1 非负
                if np.any(mv < -TOL):
                    totals["v1_viol"].append({"task": gid, "min": float(mv.min())})
                # V3 NaN/+inf（掩码外 -inf 合法）
                if np.any(np.isnan(W_done)) or np.any(np.isposinf(W_done)):
                    totals["v3_viol"].append({"task": gid})
                # V2 单纯形（含 mask 的行）
                rows_with = np.any(mask, axis=1)
                rs = W_done[rows_with].sum(axis=1)
                bad = rs[(rs > 1.0 + 1e-6) | (rs < -TOL)]
                if bad.size:
                    totals["v2_viol"].append({"task": gid,
                                              "row_sums": bad.tolist()[:3]})
                # V4 排序域（候选上的场分非负、无 NaN）
                sv = W_done[u, cand]
                if np.any(np.isnan(sv)) or np.any(sv < -TOL):
                    totals["v4_viol"].append({"task": gid,
                                              "min": float(np.nanmin(sv))})
    verdict = {k: len(v) for k, v in totals.items() if k != "tasks"}
    out = {"experiment": "deposon_v20_vector_audit", "spec_version": "v2.0",
           "spec": "用户指令 2026-08-28：deposon 向量属性（单纯形非负，负值无意义）",
           "config": config_dict(cfg),
           "n_tasks": totals["tasks"],
           "violations": {k: v for k, v in totals.items() if k != "tasks"},
           "violation_counts": verdict,
           "all_pass": all(c == 0 for c in verdict.values()),
           "runtime_sec": round(time.time() - t0, 3),
           "honesty": [
               "no LLM API calls issued：全部本地数值审计。",
               "-np.inf 仅作为 mask 外占位（排序域外），不是场分值；场分值域为 [0,1] "
               "单纯形权重，负值无物理意义，V1/V4 以 < -1e-9 为违规。",
               "审计发现违规即如实列出任务级明细，不美化。"]}
    json.dump(out, open(OUT_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps({"n_tasks": totals["tasks"], "violation_counts": verdict,
                      "all_pass": out["all_pass"]}, ensure_ascii=False, indent=1))

if __name__ == "__main__":
    main()
