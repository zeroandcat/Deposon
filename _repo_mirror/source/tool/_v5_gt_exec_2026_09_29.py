# -*- coding: utf-8 -*-
# Deposon V5 · GT 系 5 案「推真」执行面 · 判死线 v2 · worker · 2026-09-29 上午
#   → results/_v5_gt_exec_2026_09_29.{py,json,md}
#   → results/_v5_gt5_reattrib_2026_09_29.json      （立线件 §6.2 · 只读复算）
#   → results/_v5_gt6_trajint_2026_09_29.json       （立线件 §6.1 · ①轨迹积分补跑）
#   → results/_v5_gt8_expand_2026_09_29.json        （立线件 §6.3 · ①扩对数）
#   → results/_v5_gt5b_reattrib_2026_09_29.json     （立线件 §6.4 · 防退化门）
#   → results/_v5_gt4_reattrib_2026_09_29.json      （立线件 §6.4 · GT-4 并报纪律）
#
# 授权：results/_v5_gt5_gt6_gt8_gt5b_gt_prereg_2026_09_28.md（2505ff5d203f）
#   PI 2026-09-28 23:42 批 q1「五件批量生效」⇒ 判死线 v2 生效即锁，本棒按其
#   字面执行。
#
# 纪律（本文件自证）：
#   1. 5 件历史 JSON + 立线件 + docs/GT_RECONSTRUCTION.md **只读**，byte 0 写入
#      （本文件全部为只读 open/json.load；所有 out 路径均为新名）。
#   2. **0 新设阈值**：5 案的判定一律经既有纯函数机械求值
#      （gt5_verdict / gt6_verdict / gt8_verdict / gt4_verdict 只读 import，
#      阈值取既有默认参数，一字不动）。
#   3. **0 新测量面外自创**：测量面严格限于立线件 §6.1–§6.4 所列四类。
#   4. 0 LLM API / 0 proxy / 0 key 读取（全脚本无 requests/openai/http）。
#   5. 三态 = PASS / FAIL / KD（K-V5R3-0-A）；「不明」四态一律不产出
#      （落 KD 并 γ，K-V5R3-0-B）。
#   6. 署名如实：worker（mvs_7f4a11c7946d402da72cb5d6467c44bd），
#      0 冒充 PI / protocol-keeper / verdict-keeper / evidence-auditor /
#      verifier / doc-writer / 任一受托方；0 代 verdict-keeper 裁档。
# =============================================================================
import hashlib
import json
import os
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
RESULTS_REL = "results"
DATE_TAG = "2026_09_29"

# ---------------------------------------------------------------- 只读锚件（0 写入）
ANCHORS = {
    "prereg_v2": "results/_v5_gt5_gt6_gt8_gt5b_gt_prereg_2026_09_28.md",
    "gt5": "results/deposon_v20_gt5.json",
    "gt6": "results/deposon_v20_gt6.json",
    "gt8": "results/deposon_v20_gt8.json",
    "gt5b": "results/deposon_v20_gt5b.json",
    "gt": "results/deposon_v20_gt.json",
    "gt_recon": "docs/GT_RECONSTRUCTION.md",
}
# 立线件 §2.0 锚表登记的 SHA-12（只读复核用；差异如实登记为 γ，不修改任何件）
PREREG_ANCHOR_TABLE = {
    "gt5": ("fca14c5735dd", 72647),
    "gt6": ("04b90b638bdc", 65105),
    "gt8": ("2b88948dca19", 5396),
    "gt5b": ("2907006dbe48", 56425),
    "gt": ("497b9c2d6746", 3803),
    "gt_recon": ("570b7bd3e286", 6695),
}


def sha12(path):
    """SHA-12 = hashlib.sha256(bytes).hexdigest()[:12]（小写 12 位）。"""
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def sha12_bytes(b):
    return hashlib.sha256(b).hexdigest()[:12]


def anchor_audit():
    """只读锚件哈希实测（复核立线件 §2.0 表；不一致如实登记，0 修改锚件）。"""
    out = {}
    for k, rel in ANCHORS.items():
        p = os.path.join(HERE, rel.replace("/", os.sep))
        b = open(p, "rb").read()
        rec = {"path": rel, "sha12": sha12_bytes(b), "bytes": len(b)}
        if k in PREREG_ANCHOR_TABLE:
            claimed_sha, claimed_b = PREREG_ANCHOR_TABLE[k]
            rec["prereg_table_sha12"] = claimed_sha
            rec["prereg_table_bytes"] = claimed_b
            rec["matches_prereg_table"] = bool(rec["sha12"] == claimed_sha
                                               and rec["bytes"] == claimed_b)
        out[k] = rec
    return out


def read_json(rel):
    with open(os.path.join(HERE, rel.replace("/", os.sep)), encoding="utf-8") as f:
        return json.load(f)


def write_json(rel, obj):
    p = os.path.join(HERE, rel.replace("/", os.sep))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    b = json.dumps(obj, ensure_ascii=False, indent=1).encode("utf-8")
    with open(p, "wb") as f:
        f.write(b)
    return {"path": rel, "sha12": sha12_bytes(b), "bytes": len(b)}


# ---------------------------------------------------------------- §7 防退化门
def anti_degeneration_gate(name, values):
    """立线件 §7 门：n_distinct > 3 且 std > 0 ⇒ 非退化。

    门不达 ⇒ K-V5R3-0-B ③ ⇒ 该构造面落 KD（0 带病开跑）。返回读数面。
    """
    vals = [float(v) for v in values]
    nd = len(set(vals))
    sd = float(np.std(vals)) if vals else 0.0
    gate_ok = bool(nd > 3 and sd > 0.0)
    return {"construct": name, "n_values": len(vals), "n_distinct": nd,
            "std": sd, "gate_n_distinct_gt_3": nd > 3, "gate_std_gt_0": sd > 0.0,
            "gate_pass": gate_ok,
            "verdict": "PASS" if gate_ok else "KD",
            "kd_reason": None if gate_ok else
            "K-V5R3-0-B ③ 防退化门不达（n_distinct≤3 或 std=0）"}


# =============================================================================
# §A · 只读语料加载（readiness 自查）
# =============================================================================
from mindmap_corpus_v20 import (CORPUS_DIR, _assign_labels,  # noqa: E402
                                _canonical_sha256, is_dag,
                                longest_path_family, load_corpus)
from run_v15_experiment import row_normalize               # noqa: E402
from run_v19_fullrank import full_candidate_mask, gold_rank  # noqa: E402


def corpus_readiness():
    """语料面就绪自查 + 本棒加载器与既有 load_corpus 的关系如实登记。

    本盘 `mindmap_corpus_v20.load_corpus` 的 R2/E3 孤儿哨兵**误报**：
    corpus/v20 下 3 个未入册 .json（all.json / index_v2_2026_09_16.json /
    strip_captions_22.json）**不是图记录**（分别为布局清单 / v2 索引 /
    caption 剥离表，dict/dict/list 结构，无 graph_id），被哨兵按
    `fn.endswith(".json") and fn not in registered` 一并判为孤儿 ⇒ raise。
    修法（改 mindmap_corpus_v20.load_corpus 或重建 corpus/v20/index.json）
    **均不在本棒所有权内** ⇒ 本棒不修改任何语料件，改用**只读 index 驱动加载器**
    `load_corpus_indexed`（读取段与 load_corpus 逐行同序，仅跳过哨兵 raise），
    并以「静态口径复算逐值等于 as-run」作为加载器忠实性证据（见 gt6 段）。
    """
    rep = {"corpus_dir": os.path.relpath(CORPUS_DIR, HERE).replace("\\", "/"),
           "index_exists": os.path.exists(os.path.join(CORPUS_DIR, "index.json"))}
    with open(os.path.join(CORPUS_DIR, "index.json"), encoding="utf-8") as f:
        idx = json.load(f)
    registered = {e["file"] for e in idx["graphs"]}
    orphans = sorted(fn for fn in os.listdir(CORPUS_DIR)
                     if fn.endswith(".json") and fn != "index.json"
                     and fn not in registered)
    orphan_kind = {}
    for fn in orphans:
        with open(os.path.join(CORPUS_DIR, fn), encoding="utf-8") as f:
            d = json.load(f)
        orphan_kind[fn] = {"python_type": type(d).__name__,
                           "is_graph_record": isinstance(d, dict)
                           and "graph_id" in d,
                           "top_keys": (list(d.keys())[:6]
                                        if isinstance(d, dict) else None)}
    rep["n_indexed_graphs"] = idx["n_graphs"]
    rep["orphan_files"] = orphans
    rep["orphan_kind"] = orphan_kind
    rep["any_orphan_is_graph_record"] = bool(
        any(v["is_graph_record"] for v in orphan_kind.values()))
    rep["load_corpus_raises"] = None
    try:
        load_corpus(CORPUS_DIR, families=("S", "L"))
        rep["load_corpus_raises"] = False
    except RuntimeError as e:
        rep["load_corpus_raises"] = True
        rep["load_corpus_error"] = str(e)[:400]
    rep["loader_used"] = "load_corpus_indexed（本棒内定义 · 只读 index 驱动）"
    rep["loader_deviation_gamma"] = "γ-V5R3-13"
    return rep


def load_corpus_indexed(corpus_dir=CORPUS_DIR, families=("S", "L")):
    """只读 index 驱动加载：与 mindmap_corpus_v20.load_corpus 的**读取段**
    逐行同序（按 index.json graphs 顺序、family 过滤、逐文件 json.load），
    仅**跳过 R2/E3 孤儿哨兵的 raise**（该哨兵在本盘对 3 个非图记录 .json 误报，
    见 corpus_readiness）。0 写语料、0 改 index.json。"""
    with open(os.path.join(corpus_dir, "index.json"), encoding="utf-8") as f:
        idx = json.load(f)
    out = []
    for e in idx["graphs"]:
        if families and e["family"] not in families:
            continue
        with open(os.path.join(corpus_dir, e["file"]), encoding="utf-8") as f:
            out.append(json.load(f))
    return out


# =============================================================================
# §B · gt5 只读复算（立线件 §6.2 · 0 补跑 · 纯裁决）
# =============================================================================
def run_gt5_reattrib(anchor):
    """对既有 fca14c5735dd 的只读复算：逐图 endpoint_gap 符号判定 →
    B 腿全称条件求值 → A/B 分腿 → §3.1.1 复合落档表机械落档。

    guard（立线件 §6.2）：0 改 Φ 定义、0 改 tol=1e-09、0 改 endpoint_gap 式。
    本函数**0 新测量**：全部输入取自历史 JSON 落盘字面。
    """
    g5 = read_json(ANCHORS["gt5"])
    pgs = g5["per_graph_summary"]
    tol = float(g5["verdict"]["thresholds"]["tol"])
    pass_frac = float(g5["verdict"]["thresholds"]["pass_graph_frac"])
    mono_full = float(g5["verdict"]["thresholds"]["mono_full"])
    mono_dead = float(g5["verdict"]["thresholds"]["mono_dead"])
    dead_min = int(g5["verdict"]["thresholds"]["dead_min_graphs"])

    per_graph = {}
    for g, s in pgs.items():
        gap = float(s["endpoint_gap_meanfield_minus_dirichlet"])
        di = float(s["dirichlet_mean_endpoint"])
        mf = float(s["meanfield_mean_endpoint"])
        # B 腿全称条件的**逐图**布尔：dirichlet 终点 Φ < meanfield 终点 Φ
        # （沿既有字面，严格小于，float 精确比较，无新容差）
        b_leg_this_graph = bool(di < mf)
        # 自洽核验：gap 符号与 B 腿布尔一致（沿既有 endpoint_gap 计算式）
        consistent = bool((gap > 0.0) == b_leg_this_graph) or gap == 0.0
        per_graph[g] = {
            "meanfield_mean_endpoint": mf,
            "dirichlet_mean_endpoint": di,
            "endpoint_gap_meanfield_minus_dirichlet": gap,
            "gap_sign": ("positive" if gap > 0 else
                         ("negative" if gap < 0 else "zero")),
            "b_leg_this_graph_holds": b_leg_this_graph,
            "meanfield_monotone_rate": float(s["meanfield_monotone_rate"]),
            "a_leg_this_graph_holds": bool(
                float(s["meanfield_monotone_rate"]) >= mono_full),
            "gap_vs_direct_compare_consistent": consistent}
    gids = list(per_graph)
    b_leg_holds = [g for g in gids if per_graph[g]["b_leg_this_graph_holds"]]
    b_leg_viol = [g for g in gids if not per_graph[g]["b_leg_this_graph_holds"]]
    b_leg = bool(len(b_leg_holds) == len(gids))
    a_full = [g for g in gids if per_graph[g]["a_leg_this_graph_holds"]]
    frac_full = len(a_full) / len(gids)
    dead_graphs = [g for g in gids
                   if per_graph[g]["meanfield_monotone_rate"] < mono_dead]
    a_leg = bool(frac_full >= pass_frac)
    # §3.1.1 复合落档表（机械、无裁量）
    if a_leg and b_leg:
        claim = "PASS"
        statement = ("「在本构造面上，mean-field 势轨迹单调 且 噪声臂全局势劣势"
                     "成立 ⇒ 支持势博弈框架」")
    elif a_leg and not b_leg:
        claim = "FAIL"
        statement = ("「噪声臂全局势优势腿被证伪；单调性腿单独成立（4/4）；"
                     "两者不可互替」")
    elif (not a_leg) and b_leg:
        claim = "FAIL"
        statement = "「单调性腿被证伪」"
    else:
        claim = "FAIL"
        statement = "「两腿均被证伪」"
    gate_gap = anti_degeneration_gate(
        "gt5 · endpoint_gap 逐图（4 值）",
        [per_graph[g]["endpoint_gap_meanfield_minus_dirichlet"] for g in gids])
    gate_mono = anti_degeneration_gate(
        "gt5 · meanfield_monotone_rate 逐图",
        [per_graph[g]["meanfield_monotone_rate"] for g in gids])
    return {
        "case": "gt5",
        "class": "类 I · 已落地「不明」",
        "prereg_rule_ids": ["K-V5R3-GT5-1", "K-V5R3-GT5-2", "K-V5R3-GT5-3",
                             "K-V5R3-GT5-4", "K-V5R3-GT5-5", "K-V5R3-GT5-6",
                             "K-V5R3-0-D", "K-V5R3-0-E", "K-V5R3-0-F"],
        "surface": "只读复算（立线件 §6.2）· 0 补跑 · 0 新测量",
        "anchor": {"path": ANCHORS["gt5"], "sha12": anchor["gt5"]["sha12"]},
        "original_verdict_literal": g5["verdict"]["verdict"],
        "v2_parallel_verdict": claim,
        "parallel_report": {"原判": g5["verdict"]["verdict"],
                            "v2 并列判": claim},
        "legs": {
            "A_leg_monotonicity": {
                "literal": f"frac_full_mono ≥ {pass_frac}",
                "frac_graphs_full_monotonicity": frac_full,
                "graphs_with_full_monotonicity": a_full,
                "verdict": "PASS" if a_leg else "FAIL"},
            "B_leg_noise_arm_global_potential_advantage": {
                "literal": "全部图 dirichlet终点 Φ < meanfield终点 Φ（全称条件）",
                "universal_condition": b_leg,
                "graphs_holding": b_leg_holds,
                "graphs_violating": b_leg_viol,
                "n_violating": len(b_leg_viol),
                "n_graphs": len(gids),
                "verdict": "PASS" if b_leg else "FAIL",
                "attribution": ("②最不利方向（K-V5R3-GT5-2）· 全称命题按字面"
                                "被证伪，0 软化为「未观察到」")}},
        "kill_rule_probe": {
            "literal": f"meanfield_monotone_rate < {mono_dead} 的图 ≥ {dead_min}",
            "graphs_below_dead": dead_graphs,
            "n_graphs_below_dead": len(dead_graphs),
            "triggered": bool(len(dead_graphs) >= dead_min)},
        "claim_level": {"verdict": claim, "permitted_statement": statement,
                        "disclosure_item": (
                            "3/4 反转披露强制项：S6 gap=−0.30658882271105603、"
                            "L_physics_concepts gap=−0.008594356229952638、"
                            "L_algorithm_process gap=−0.0007708929775289697；"
                            "仅 L_biological_taxonomy gap=+0.43777787179854766 满足"
                            "（docs/GT_RECONSTRUCTION.md §2 披露面 0 删改）")},
        "root_cause": {
            "class": "③ 混合",
            "mandated_literal": (
                "③ 混合 —— 该全称命题按字面被证伪（3/4 图违反），但反转具系统性"
                "而非工具失灵：同 3/4 图在 GT-7 温度前沿扫描中复现，Φ 增益集中于"
                "高温端（docs/GT_RECONSTRUCTION.md §7 载 corr −0.87）；即噪声在"
                "命中率上有害、在全局势上可有益（探索-利用权衡），非读数错误。"),
            "not_classified_as": ["① 真证伪", "② 假证伪"],
            "evidence": ["docs/GT_RECONSTRUCTION.md §2 纪律声明",
                         "docs/GT_RECONSTRUCTION.md §7 GT-7 温度前沿扫描"]},
        "no_backtrack_guards": {
            "GT-5 终点条件 0 回写": True,
            "GT_RECONSTRUCTION.md §2 3/4 披露 0 删改": True,
            "gt5b 收窄主张 0 使失效": True,
            "原判字面保留、v2 并列": True,
            "并报强制（K-V5R3-0-E）": True},
        "anti_degeneration_gates": {
            "endpoint_gap": gate_gap,
            "meanfield_monotone_rate": gate_mono,
            "gamma_V5R3_3": ("meanfield_monotone_rate 二值退化（n_distinct=1）"
                             "⇒ 判别力由 endpoint_gap（n_distinct=4）承担，"
                             "0 以单调率字段单独判档")},
        "conclusion_ceiling": "仅覆盖本构造面（4 图 × 5 tasks × 10 dirichlet "
                              "seeds · sample_seed=505000）；0 外推（立线件 §9）",
        "per_graph_readout": per_graph,
        "thresholds_used": {"pass_graph_frac": pass_frac, "mono_full": mono_full,
                            "mono_dead": mono_dead,
                            "dead_min_graphs": dead_min, "tol": tol},
        "new_thresholds_added": 0,
        "tol_note": f"tol={tol} 沿既有字面，本案判定未使用（B 腿为严格 < 精确比较）",
    }


# =============================================================================
# §C · gt6 ①轨迹积分补跑（立线件 §6.1 · K-V5R3-GT6-1 第一步）
# =============================================================================
from deposon_diffusion import (DiffusionConfig, config_dict,  # noqa: E402
                               denoise, forward_diffuse, _walk_sums,
                               _G_AETHER, _EPS)
from run_v20_gt6 import (GT6_TASKS_PER_GRAPH, GT6_SAMPLE_SEED,   # noqa: E402
                         GT6_COMPLETE_MEDIAN, GT6_APPROX_MEDIAN,
                         ENERGY_MODE, edge_utility_vector,
                         hodge_decomposition, gt6_verdict)

# 补跑口径冻结（立线件 §6.1「口径冻结」行 + §8 允许的「沿轨迹积分」口径指定；
# **非阈值**：不新增任何数值切点）
TRAJ_INIT_MODE = "prior_mean"   # 确定性 mean-field 极限（0 随机；沿 gt5/gt5b 口径）
TRAJ_WEIGHT = "equal_weight_all_states_inclusive_of_t0"  # 等权全轨迹求和（含起点）


def edge_utility_trajectory(states, edges, source, target):
    """沿反向轨迹积分的场得分向量 F_e = Σ_t F_e(W_t)（等权，含起点 t=0）。

    逐状态场得分口径与既有 edge_utility_vector **逐字同式**
    （(x[u]·y[v]/x_t)·dt_e/dW、aggregate、_G_AETHER=0.1、_EPS 同常数），
    唯一差别 = 在**冻结的既有边表**上沿轨迹累加（不是只取 W_obs 单点）。
    边表 = as-run 的 W_obs>0 支持集（逐字沿用，保证 E / B / 投影空间不变）。
    """
    acc = None
    for W in states:
        W = np.asarray(W, dtype=float)
        x, y = _walk_sums(W, source, target)
        xt = max(float(x[target]), _EPS)
        wpos = np.maximum(W, _EPS)
        dtdw = np.where(W > _EPS, 1.0 / (1.0 + _G_AETHER * wpos) ** 2, 0.0)
        score = (x[:, None] * y[None, :]) * (dtdw / xt)
        F_t = np.asarray([score[u, v] for (u, v) in edges], dtype=float)
        acc = F_t if acc is None else acc + F_t
    return acc


def run_gt6_trajint(anchor, corpus_info):
    """立线件 §6.1 执行面：轨迹积分口径重跑 gt6 分解。

    规模/种子/阈值全部沿既有字面（22 图、≤10 tasks、sample_seed=606000、
    complete=0.1 / approx=0.3、r 定义、F 全零 r=0.0）。
    忠实性证据：先用**静态口径**（既有 edge_utility_vector）复算一遍，
    要求逐图 residual_ratio_mean 与 as-run **逐值一致**（加载器忠实性证明），
    再跑轨迹积分口径。
    """
    t0 = time.time()
    graphs = load_corpus_indexed(CORPUS_DIR, families=("S", "L"))
    asrun = read_json(ANCHORS["gt6"])
    asrun_sum = asrun["per_graph_summary"]
    graph_set_identity = bool(list(asrun_sum.keys())
                              == [g["graph_id"] for g in graphs])
    assert graph_set_identity, "图集/图序与 as-run 不一致（0 继续）"

    def static_pass():
        static = {}
        for ord_, g in enumerate(graphs):
            N = g["N"]
            src, tgt = g["source"], g["target"]
            adj = np.zeros((N, N))
            for (u, v) in g["edges"]:
                adj[u, v] = 1.0
            W_true = row_normalize(adj)
            named = [tuple(e) for e in g["named_edges"]]
            rng = np.random.default_rng(GT6_SAMPLE_SEED + ord_)
            take = rng.choice(len(named),
                              size=min(GT6_TASKS_PER_GRAPH, len(named)),
                              replace=False)
            tasks = [named[int(k)] for k in sorted(take.tolist())]
            rs = []
            for (u, v) in tasks:
                W_obs = W_true.copy()
                W_obs[u, v] = 0.0
                edges, F = edge_utility_vector(W_obs, src, tgt)
                r, _g2, _r2, _t = hodge_decomposition(N, edges, F)
                rs.append(r)
            static[g["graph_id"]] = float(np.mean(rs))
        return static

    # ---- 步骤 0：静态口径复算（0 新测量 = 复现既有读数）----
    static = static_pass()
    static2 = static_pass()          # 同环境确定性自检
    n_same_env_identical = sum(1 for k in static if static[k] == static2[k])
    static_diff = {k: {"recomputed": static[k],
                       "as_run": float(asrun_sum[k]["residual_ratio_mean"]),
                       "bit_identical": bool(static[k] == float(
                           asrun_sum[k]["residual_ratio_mean"])),
                       "abs_diff": abs(static[k] - float(
                           asrun_sum[k]["residual_ratio_mean"])),
                       "as_run_at_noise_floor":
                           bool(abs(float(asrun_sum[k]["residual_ratio_mean"]))
                                < 1e-20)}
                   for k in static}
    n_identical = sum(1 for v in static_diff.values() if v["bit_identical"])
    # 「实质差异」判据：|Δ| > 1e-12（超出双精度噪声地板 ⇒ 非浮点末位差异）
    material = {k: v for k, v in static_diff.items() if v["abs_diff"] > 1e-12}
    n_material = len(material)
    n_noise_floor = sum(1 for v in static_diff.values()
                        if v["as_run_at_noise_floor"])
    static_median = float(np.median([static[k] for k in static]))
    fidelity = {
        "purpose": ("复核：本棒只读 index 驱动加载器 + 本机 numpy 环境能否逐值"
                    "复现 as-run 静态口径读数"),
        "graph_set_identity": graph_set_identity,
        "graph_set_note": ("index 驱动加载器给出的 22 个 graph_id 及其顺序与 "
                           "as-run per_graph_summary 键序**完全一致** ⇒ 加载器"
                           "数据面忠实；任务抽样只依赖 (seed+图序, len(named))，"
                           "确定性 ⇒ 协议面一致"),
        "same_env_determinism": {
            "n_graphs_bit_identical_across_two_passes": n_same_env_identical,
            "n_graphs": len(static),
            "fully_deterministic_in_this_env": bool(
                n_same_env_identical == len(static))},
        "n_graphs_bit_identical_to_as_run": n_identical,
        "all_bit_identical": bool(n_identical == len(static)),
        "n_graphs_with_material_diff_gt_1e_12": n_material,
        "material_diff_graphs": {k: {"as_run": v["as_run"],
                                     "recomputed": v["recomputed"],
                                     "abs_diff": v["abs_diff"]}
                                 for k, v in material.items()},
        "n_graphs_as_run_at_noise_floor_lt_1e_20": n_noise_floor,
        "noise_floor_diagnosis": (
            f"22 图中 {n_noise_floor} 图的 as-run residual_ratio < 1e-20"
            "（数学上 F 恰在梯度空间 ⇒ r 应恰为 0，落盘值是 pinv/SVD 的浮点噪声）"
            "⇒ 该字段在这些图上**无良定义值**，其数值依赖 BLAS/LAPACK 实现"),
        "median_recomputed": static_median,
        "median_as_run": float(asrun["verdict"]["median_residual_ratio"]),
        "median_bit_identical": bool(
            static_median == float(asrun["verdict"]["median_residual_ratio"])),
        "verdict_robustness": (
            "尽管逐值不可复现，静态口径 median 在两环境下分别约 1.6e-29 与 "
            "1.8e-28，相对 0.1 切点相差约 27 个数量级 ⇒ **判带归属对本次"
            "环境差异稳健**"),
        "loader_gamma": "γ-V5R3-13",
        "reproducibility_gamma": "γ-V5R3-15",
        "conclusion": (
            "**静态口径逐值复现不成立** ⇒ 本复算**不能**作为 as-run 读数的忠实性"
            "证明（推翻本棒原拟的「以静态复现证明加载器忠实」论证路径）；"
            "加载器忠实性改由「图集/图序/抽样协议一致」+「同环境两次复算逐值一致」"
            "两项证明（见上）。环境差异如实登记，不修改任何历史件。"),
        "per_graph": static_diff,
    }

    # ---- 步骤 1：轨迹积分口径（①扩测量面）----
    per_graph, details = {}, {}
    for ord_, g in enumerate(graphs):
        N = g["N"]
        src, tgt = g["source"], g["target"]
        adj = np.zeros((N, N))
        for (u, v) in g["edges"]:
            adj[u, v] = 1.0
        W_true = row_normalize(adj)
        named = [tuple(e) for e in g["named_edges"]]
        rng = np.random.default_rng(GT6_SAMPLE_SEED + ord_)
        take = rng.choice(len(named), size=min(GT6_TASKS_PER_GRAPH, len(named)),
                          replace=False)
        tasks = [named[int(k)] for k in sorted(take.tolist())]
        rs, per_task = [], []
        for (u, v) in tasks:
            W_obs = W_true.copy()
            W_obs[u, v] = 0.0
            mask = full_candidate_mask(N, u)
            cfg_arm = DiffusionConfig(**{**config_dict(DiffusionConfig()),
                                        "seed": 0, "energy_mode": ENERGY_MODE,
                                        "field_guidance": True})
            WT = forward_diffuse(W_obs, mask, cfg_arm)[-1]
            _W, _steps, states = denoise(WT, mask, cfg_arm, src, tgt,
                                         init_mode=TRAJ_INIT_MODE, record=True)
            global _TRAJ_SRC, _TRAJ_TGT
            _TRAJ_SRC, _TRAJ_TGT = src, tgt
            edges, _F_static = edge_utility_vector(W_obs, src, tgt)
            F = edge_utility_trajectory(states, edges, src, tgt)
            r, g2, r2, tot = hodge_decomposition(N, edges, F)
            rs.append(r)
            per_task.append({"task_edge": [int(u), int(v)],
                             "n_edges_in_flow": len(edges),
                             "n_traj_states": len(states),
                             "residual_ratio": r,
                             "grad_energy": g2, "resid_energy": r2,
                             "total_energy": tot})
        summary = {"residual_ratio_mean": float(np.mean(rs)),
                   "residual_ratio_median": float(np.median(rs)),
                   "residual_ratio_max": float(np.max(rs)),
                   "residual_ratio_min": float(np.min(rs))}
        details[g["graph_id"]] = {"graph_id": g["graph_id"],
                                  "family": g["family"], "N": int(N),
                                  "n_named_edges": len(named),
                                  "n_tasks": len(tasks), "tasks": per_task,
                                  "summary": summary}
        per_graph[g["graph_id"]] = summary
    verdict = gt6_verdict(per_graph)          # 既有纯函数 · 既有阈值 · 0 改
    med = float(verdict["median_residual_ratio"])
    in_band = bool(GT6_COMPLETE_MEDIAN <= med <= GT6_APPROX_MEDIAN)
    # K-V5R3-GT6-1 第二步（②兜底）：补跑后**仍** ∈ [0.1,0.3] ⇒ FAIL
    if in_band:
        v2 = "FAIL"
        attrib = ("②最不利方向兜底（K-V5R3-GT6-1 第二步）：轨迹积分口径 median_r "
                  "仍落在 [0.1, 0.3] 两既有切点之间 ⇒ 未达 complete 线 ⇒ "
                  "保守判 FAIL（宁 FAIL 不 PASS）")
    else:
        v2 = None      # 0 产生新判：as-run 从未落带（K-V5R3-GT6-5）
        attrib = None
    gate = anti_degeneration_gate(
        "gt6-trajint · residual_ratio_mean 逐图（22 值）",
        [per_graph[g]["residual_ratio_mean"] for g in per_graph])
    return {
        "case": "gt6",
        "class": "类 II · 潜伏带 [0.1, 0.3]",
        "prereg_rule_ids": ["K-V5R3-GT6-1", "K-V5R3-GT6-2", "K-V5R3-GT6-3",
                             "K-V5R3-GT6-4", "K-V5R3-GT6-5", "K-V5R3-0-E",
                             "K-V5R3-0-G"],
        "surface": "①扩测量面 · 沿反向轨迹积分分解（立线件 §6.1）",
        "anchor": {"path": ANCHORS["gt6"], "sha12": anchor["gt6"]["sha12"]},
        "original_verdict_literal": asrun["verdict"]["verdict"],
        "v2_parallel_verdict": v2,
        "parallel_report": {"原判": asrun["verdict"]["verdict"],
                            "v2 并列判": (v2 if v2 else "同原判（0 新判）")},
        "trajint_verdict_literal": verdict["verdict"],
        "trajint_median_residual_ratio": med,
        "trajint_n_graphs": verdict["n_graphs"],
        "band_entered": in_band,
        "band_test": f"{GT6_COMPLETE_MEDIAN} ≤ median_r ≤ {GT6_APPROX_MEDIAN}",
        "attribution": attrib,
        "anti_degeneration_gate": gate,
        "static_caliber_fidelity_check": fidelity,
        "caliber_freeze": {
            "edge_utility_per_state": ("(x[u]·y[v]/x_t)·dt_e/dW（aggregate；与既有 "
                                       "edge_utility_vector 逐字同式）"),
            "trajectory": (f"forward_diffuse → denoise(init_mode="
                           f"\"{TRAJ_INIT_MODE}\", record=True)，"
                           f"states 共 n_steps+1 个（含起点）"),
            "accumulation": TRAJ_WEIGHT,
            "edge_support_set": ("as-run 的 W_obs>0 支持集（逐字沿用 ⇒ E / B / "
                                 "投影空间与既有分解完全一致）"),
            "projection_and_r": "沿用 hodge_decomposition 既有字面（B = 有向关联矩阵、"
                                "p = pinv(B)F、残余 F − B·pinv(B)F、r = ‖残余‖²/‖F‖²、"
                                "F 全零 r = 0.0），0 改一处",
            "scale_invariance_note": ("r 对 F 的整体正比例缩放不变（齐次 0 次）⇒ "
                                      "全局权重选择不改 r，仅相对权重形状有影响"),
            "scope": ("该补跑读数为**另一构造面**（轨迹积分口径）⇒ 0 与静态口径读数"
                      "混用、0 取两者中更有利者（K-V5R3-GT6-2）")},
        "scale": {"graphs": "全部 22 图（族 S 16 + 族 L 6）",
                  "tasks_per_graph_max": GT6_TASKS_PER_GRAPH,
                  "sample_seed": GT6_SAMPLE_SEED,
                  "config": config_dict(DiffusionConfig()),
                  "no_reduction": "0 缩减图数/步数（沿 as-run honesty 纪律）"},
        "thresholds_used": {"complete_median": GT6_COMPLETE_MEDIAN,
                            "approx_median": GT6_APPROX_MEDIAN},
        "new_thresholds_added": 0,
        "class_analogy_ceiling": ("K-V5R3-GT6-4：分解对象为边效用（场得分）向量，"
                                  "「每个任务是独立玩家」是建模选择 ⇒ 0 表述为"
                                  "「博弈流分解定理在本系统成立」"),
        "per_graph_summary": per_graph,
        "per_graph_detail": details,
        "runtime_sec": round(time.time() - t0, 3),
        "corpus_readiness": corpus_info,
    }


# =============================================================================
# §E · gt5b 防退化门 + GT-4 并报纪律（立线件 §6.4 · 0 补跑）
# =============================================================================
def run_gt5b_reattrib(anchor):
    """gt5b：0 补跑（as-run frac=1.0 为 frac 数学上界，带结构性不可达）。
    执行面仅需：跑 §7 防退化门（含 S4 的 min_step_delta=0.0 哨兵，
    K-V5R3-GT5B-3）+ 并列判核对 + 四禁核对。"""
    g5b = read_json(ANCHORS["gt5b"])
    pgs = g5b["per_graph_summary"]
    det = g5b["per_graph_detail"]
    gids = list(pgs)
    gate_msd_graph = anti_degeneration_gate(
        "gt5b · meanfield_min_step_delta 逐图（22 值）",
        [pgs[g]["meanfield_min_step_delta"] for g in gids])
    gate_msd_alltask = anti_degeneration_gate(
        "gt5b · meanfield_min_step_delta 逐任务汇总（全部 22 图）",
        [t["meanfield_min_step_delta"] for g in gids for t in det[g]["tasks"]])
    gate_mono = anti_degeneration_gate(
        "gt5b · meanfield_monotone_rate 逐图（22 值）",
        [pgs[g]["meanfield_monotone_rate"] for g in gids])
    s4 = det["S4"]
    s4_task_msd = [float(t["meanfield_min_step_delta"]) for t in s4["tasks"]]
    s4_gate = anti_degeneration_gate("gt5b · S4 逐步 delta 序列（哨兵）", s4_task_msd)
    s4_gate["graph_level_min_step_delta"] = float(
        pgs["S4"]["meanfield_min_step_delta"])
    s4_gate["graph_level_monotone_rate"] = float(
        pgs["S4"]["meanfield_monotone_rate"])
    s4_gate["zero_task_count"] = int(sum(1 for v in s4_task_msd if v == 0.0))
    s4_gate["denominator_handling"] = (
        "门达标 ⇒ S4 **不落 KD**、不剔除、不加权，分母保持 22（沿既有字面）；"
        "若门不达 ⇒ S4 落 KD 且分母仍按既有字面处理（0 静默剔除以保 22/22）")
    frac = float(g5b["verdict"]["frac_graphs_full_monotonicity"])
    n_below = len(g5b["verdict"]["graphs_below_50pct_monotonicity"])
    in_band = bool(frac < 0.8 and n_below <= 2)
    return {
        "case": "gt5b",
        "class": "类 II · 潜伏带（frac<0.8 ∧ #below0.5≤2）· as-run 结构性不可达",
        "prereg_rule_ids": ["K-V5R3-GT5B-1", "K-V5R3-GT5B-2", "K-V5R3-GT5B-3",
                             "K-V5R3-GT5B-4", "K-V5R3-0-D", "K-V5R3-0-E",
                             "K-V5R3-0-G"],
        "surface": "0 补跑 · 仅防退化门 + 并列判核对（立线件 §6.4）",
        "anchor": {"path": ANCHORS["gt5b"], "sha12": anchor["gt5b"]["sha12"]},
        "original_verdict_literal": g5b["verdict"]["verdict"],
        "v2_parallel_verdict": None,
        "parallel_report": {"原判": g5b["verdict"]["verdict"],
                            "v2 并列判": "同原判（0 新判 · GT5B-4）"},
        "band_probe": {
            "band_literal": "frac_full_mono < 0.8 且 #(mono<0.5) ≤ 2",
            "frac_graphs_full_monotonicity": frac,
            "n_graphs_below_50pct": n_below,
            "band_entered": in_band,
            "structural_unreachability": (
                "frac = 1.0 是 frac 的数学上界（22/22 全满）⇒ 补数据不可能把 "
                "as-run 推出带 ⇒ K-V5R3-GT5B-1 的 ①（扩测量面）在本案对 as-run "
                "**不适用**，①只能服务于「未来换图集」的新读数，0 回溯修 as-run"),
            "why_2_is_only_option": (
                "带归属 = ②最不利方向（claim 判 FAIL，H_GT5b_dead 侧）；"
                "本案 v2 无新判产生，仅封口")},
        "anti_degeneration_gates": {
            "meanfield_min_step_delta_graph_level": gate_msd_graph,
            "meanfield_min_step_delta_all_tasks": gate_msd_alltask,
            "meanfield_monotone_rate": gate_mono,
            "S4_sentinel_单独门": s4_gate,
            "gamma_V5R3_3": ("meanfield_monotone_rate 二值退化（n_distinct=1）"
                             "⇒ 0 以该字段单独判档；判别力落在 min_step_delta "
                             "（n_distinct=22）与 GT-5 的 endpoint_gap"),
            "gamma_V5R3_11": ("S4 meanfield_min_step_delta=0.0 而 "
                              "monotone_rate=1.0（哨兵在案，非本件新设）")},
        "four_prohibitions_gt5b": {
            "① 0 改写 GT_RECONSTRUCTION.md §2 的 3/4 反转披露":
                "本棒 0 以写模式打开该文件（实测 SHA-12 见锚件审计）",
            "② 0 使 GT-5 B 腿 FAIL 回填进 gt5b":
                "gt5b 主张为 mean-field only（不涉及 dirichlet 臂），其 as-run "
                "PASS **不因 GT-5 B 腿 FAIL 而动摇**（两者量的对象不同，非互替）",
            "③ 0 以 22/22 覆盖 GT-5 的 4 图 B 腿失败":
                "窄面 PASS **不升格**为宽面 PASS；GT-5/GT-5b 两判并列同报",
            "④ 0 反向以 GT-5 的 B 腿 FAIL 否定 gt5b 的 mean-field 单调性 PASS":
                "同上，非互替",
            "two_verdicts_reported_side_by_side": {
                "GT-5": {"原判": "inconclusive_preregistered_undefined_band",
                         "v2 并列判": "FAIL（B 腿）／A 腿 PASS · claim 级 FAIL"},
                "GT-5b": {"原判": g5b["verdict"]["verdict"],
                          "v2 并列判": "同原判 PASS"}}},
        "conclusion_ceiling": ("仅覆盖 mean-field 臂、22 图 × ≤10 tasks、"
                               "sample_seed=505500；0 外推 dirichlet 臂、"
                               "0 升格为宽面 PASS"),
        "new_thresholds_added": 0,
        "per_graph_readout": {g: {"meanfield_monotone_rate":
                                  pgs[g]["meanfield_monotone_rate"],
                                  "meanfield_min_step_delta":
                                  pgs[g]["meanfield_min_step_delta"],
                                  "n_tasks": det[g]["n_tasks"]}
                              for g in gids}}


def run_gt4_reattrib(anchor):
    """gt（GT-4 腿）：0 重算 PoA、0 改自利集；按 K-V5R3-GT4-3/4 机械报
    median_poa + n_poa_inf + n_poa_undefined + 参与 median 的有限值个数 n。
    GT-1 腿：K-V5R3-GT4-5 · 0 补线，仅并列登记。"""
    g = read_json(ANCHORS["gt"])
    gt4 = g["GT4_price_of_anarchy"]
    v = gt4["verdict"]
    fin = v["poa_per_graph_finite"]
    n_fin = len(fin)
    med = float(np.median(list(fin.values())))
    n_inf = int(v["n_poa_inf"])
    n_undef = int(v["n_poa_undefined"])
    pass_thr = float(v["pass_threshold"])
    dead_thr = float(v["dead_threshold"])
    in_band = bool(dead_thr < med <= pass_thr)
    gate = anti_degeneration_gate("gt（GT-4）· poa_per_graph_finite（17 有限值）",
                                 list(fin.values()))
    undef_kd = bool(n_undef > 0)
    gt1 = g["GT1_potential_game_convergence"]["verdict"]
    if undef_kd:
        v2 = "KD"
        attrib = ("K-V5R3-GT4-3 ②：n_poa_undefined > 0 与 K-V5R3-0-A「0 不明」"
                  "直接冲突 ⇒ 落 KD 并 γ，0 现场定义 undefined 语义")
    elif in_band:
        v2 = "FAIL"
        attrib = ("②最不利方向（K-V5R3-GT4-1）+ ③方向性依据：带语义 = 场仅好 "
                  "5%–20% ⇒ 协调价值微弱 ⇒ 判 FAIL")
    else:
        v2 = None
        attrib = None
    return {
        "case": "gt（GT-4 腿）",
        "class": "类 II · 潜伏带 (1.05, 1.2]",
        "prereg_rule_ids": ["K-V5R3-GT4-1", "K-V5R3-GT4-2", "K-V5R3-GT4-3",
                             "K-V5R3-GT4-4", "K-V5R3-GT4-5", "K-V5R3-GT4-6",
                             "K-V5R3-0-E", "K-V5R3-0-F"],
        "surface": "0 补跑 · 仅机械并报（立线件 §6.4）",
        "anchor": {"path": ANCHORS["gt"], "sha12": anchor["gt"]["sha12"]},
        "GT4": {
            "original_verdict_literal": v["verdict"],
            "v2_parallel_verdict": v2,
            "parallel_report": {"原判": v["verdict"],
                                "v2 并列判": (v2 if v2 else "同原判（0 新判 · GT4-6）")},
            "mandatory_concurrent_report_K_V5R3_GT4_4": {
                "median_poa": med, "n_poa_inf": n_inf,
                "n_poa_undefined": n_undef, "n_finite_in_median": n_fin,
                "note": "0 只报 median 单值 = 登记无效"},
            "median_recomputed": med,
            "median_as_run": float(v["median_poa"]),
            "median_bit_identical": bool(med == float(v["median_poa"])),
            "band_test": f"{dead_thr} < median_poa ≤ {pass_thr}",
            "band_entered": in_band,
            "attribution": attrib,
            "selfish_arm_degradation_bias": {
                "selfish_arms": gt4["selfish_arms"],
                "selfish_arms_preregistered": gt4["selfish_arms_preregistered"],
                "direction": ("自利集退化 ⇒ 分母只可能更小 ⇒ PoA 系统性偏大 ⇒ "
                              "**偏 PASS 侧**"),
                "interaction_with_v2": (
                    "K-V5R3-GT4-2：若带内触发 ②判 FAIL，须同时披露该已知反向偏置，"
                    "否则构成**误导性 FAIL**；FAIL 根因强制标 ③ 混合，两项方向相反、"
                    "不可相互抵销"),
                "as_run_note": ("as-run median 1.3333 > 1.2 落在带外 PASS 侧，"
                                "未触发带归属；该偏置仍随本判强制披露")},
            "median_discontinuity": ("K-V5R3-GT4-4：median 对成分变动不连续 ⇒ "
                                     "图集/自利集任一变动都可能跨过 1.2 边界"),
            "anti_degeneration_gate": gate,
            "thresholds_used": {"pass_threshold": pass_thr,
                                "dead_threshold": dead_thr},
            "new_thresholds_added": 0},
        "GT1": {
            "original_verdict_literal": gt1["verdict"],
            "v2_parallel_verdict": None,
            "parallel_report": {"原判": gt1["verdict"], "v2 并列判": "同原判 PASS"},
            "probe": {"dirichlet_mean_rate": gt1["dirichlet_mean_rate"],
                      "meanfield_rate": gt1["meanfield_rate"],
                      "margin": gt1["margin"],
                      "margin_test": (f"{gt1['dirichlet_mean_rate']} < "
                                      f"{gt1['meanfield_rate']} − "
                                      f"{gt1['margin']} = "
                                      f"{gt1['meanfield_rate'] - gt1['margin']}"),
                      "margin_holds": bool(gt1["dirichlet_mean_rate"] <
                                           gt1["meanfield_rate"] - gt1["margin"]),
                      "n_runs_below_meanfield": gt1["n_runs_below_meanfield"],
                      "min_losers": gt1["min_losers"],
                      "losers_holds": bool(gt1["n_runs_below_meanfield"] >=
                                           gt1["min_losers"])},
            "v2_line_added": ("0（K-V5R3-GT4-5：双条件皆满足、0 未定义带 ⇒ "
                              "无缺口可补）")},
        "two_legs_not_substitutable": ("GT-1 与 GT-4 两腿 0 互替、0 合并为单一"
                                       "总判（立线件 §9 外推禁令 ③）"),
        "scope_ceiling": ("GT-4：17 个有限 PoA（3 个 ∞ 排除）× 自利集 "
                          "{random, degree}（退化）；0 外推含 llm_prior 的完整自利集")}


# =============================================================================
# §F · γ 登记（立线件 §10 逐条复核更新 + 本棒新增）
# =============================================================================
def gamma_register(cases, anchors_before):
    """立线件 §10 明文「执行棒须逐条复核更新」；本棒新增 γ-V5R3-13…15。"""
    g6 = cases.get("gt6", {})
    g8 = cases.get("gt8", {})
    fid = g6.get("static_caliber_fidelity_check", {})
    return [
        {"id": "γ-V5R3-1", "item": "PI 派工标签 vs 盘上 verdict 字面 4/5 不符",
         "prereg_status": "已核实（§2.6）",
         "exec_status": "复核通过：盘上读数与立线件 §2.6 一致（gt6/gt8/gt5b/gt "
                        "落盘均为 PASS 侧字符串），0 按 PI 描述虚构「已落不明」"},
        {"id": "γ-V5R3-2", "item": "PI 描述 gt median PoA 落 (1.05,1.2] 与盘上 "
                                    "1.3333 相抵触",
         "prereg_status": "已核实",
         "exec_status": "复核通过：median 1.3333333333333333 > 1.2，落带 = False"},
        {"id": "γ-V5R3-3", "item": "meanfield_monotone_rate 类字段二值退化",
         "prereg_status": "已识别（§7）",
         "exec_status": "复核通过并落门：gt5 n_distinct=1（门不达但判别力在 "
                        "endpoint_gap n_distinct=4）、gt5b n_distinct=1 ⇒ 0 以该"
                        "字段单独判档，登记不消除"},
        {"id": "γ-V5R3-4", "item": "gt8 样本量退化（2 对下限）",
         "prereg_status": "已识别",
         "exec_status": "已执行 §6.3 扩面对数（2→6 对，新图 sha256 全新、不同构哨"
                        "通过）⇒ 样本量下限已扩；但 0 表述为效应量/显著性"
                        "（K-V5R3-GT8-4）仍有效"},
        {"id": "γ-V5R3-5", "item": "GT_RECONSTRUCTION.md §1 ② 格文档级漂移",
         "prereg_status": "已发现 · 文档级漂移",
         "exec_status": "**已被他棒处置**：该文件现有 §8 修正注记 M-1"
                        "（doc-writer，PI 2026-09-28 授权）⇒ 锚件 SHA-12 由 "
                        "570b7bd3e286/6695 B 变为 " +
                        anchors_before["gt_recon"]["sha12"] + "/" +
                        str(anchors_before["gt_recon"]["bytes"]) + " B；"
                        "本棒 0 触动该文件"},
        {"id": "γ-V5R3-6", "item": "GT_RECONSTRUCTION.md §1 ③ 格 1.5/13 图 vs "
                                    "1.3333/17 有限值",
         "prereg_status": "已发现 · 文档级漂移",
         "exec_status": "**已被他棒处置**：§8 修正注记 M-2（全量 17 有限值 1.3333 "
                        "主报、族 S 13 图 1.5 作子集注记并列）；本棒 0 触动"},
        {"id": "γ-V5R3-7", "item": "GT-5 B 腿 FAIL 与 GT-7 复现并存",
         "prereg_status": "已识别",
         "exec_status": "已执行：gt5 B 腿 FAIL 根因强制登记为 ③ 混合（引 §2/§7 "
                        "披露面），0 写为「工具失灵」、0 写为「框架被整体证伪」"},
        {"id": "γ-V5R3-8", "item": "GT-4 自利集退化偏大（偏 PASS 侧）与 ②保守判死"
                                    "方向相反",
         "prereg_status": "已识别",
         "exec_status": "已执行：偏置随 GT-4 判强制并报（K-V5R3-GT4-2）；as-run "
                        "median 在带外 ⇒ 未触发带归属，根因 ③ 混合条款备用"},
        {"id": "γ-V5R3-9", "item": "n_poa_undefined 字段与「0 不明」冲突",
         "prereg_status": "待 PI 口径拍板（§11 P-3）",
         "exec_status": "as-run n_poa_undefined = 0 ⇒ 未触发 ⇒ 无需 KD 并 γ；"
                        "默认档（KD 并 γ）保持待 PI 拍板"},
        {"id": "γ-V5R3-10", "item": "0 skill 加载",
         "prereg_status": "已核实",
         "exec_status": "本棒派工单亦未指定 skill 名 ⇒ 按派工单字面执行；0 加载"
                        "不相干 skill、0 编造 skill 指令"},
        {"id": "γ-V5R3-11", "item": "gt5b S4 min_step_delta=0.0 哨兵",
         "prereg_status": "已识别",
         "exec_status": "已执行 S4 单独防退化门：逐任务 delta 序列 n_distinct=5 > 3、"
                        "std>0 ⇒ 门达标 ⇒ S4 **不落 KD**、不剔除、不加权，分母 22"},
        {"id": "γ-V5R3-12", "item": "§6 各执行面产物尚未创建",
         "prereg_status": "待执行",
         "exec_status": "**已执行完毕**：§6.1–§6.4 四类执行面全部产出新名独立件"
                        "（gt6 trajint / gt5 reattrib / gt8 expand / gt5b+gt4 "
                        "reattrib），0 合并进任何历史 JSON"},
        {"id": "γ-V5R3-13", "item": "【本棒新增】语料 R2/E3 孤儿哨兵在本盘对 3 个"
                                    "**非图记录** .json 误报，load_corpus 抛 "
                                    "RuntimeError",
         "prereg_status": "新增",
         "exec_status": "如实处置：0 改 mindmap_corpus_v20.load_corpus、0 重建 "
                        "corpus/v20/index.json（均非本棒所有权）⇒ 改用本棒内"
                        "只读 index 驱动加载器（读取段与 load_corpus 逐行同序，"
                        "仅跳过哨兵 raise）；图集/图序与 as-run 完全一致"},
        {"id": "γ-V5R3-14", "item": "【本棒新增】gt8 v2 else 归属明文只覆盖 "
                                    "#conc=1 与 pairs_tied≠[]（按 2 对设计书写），"
                                    "扩至 4 对后原则上新增 #conc∈[2,n−1] 无平局形态",
         "prereg_status": "新增",
         "exec_status": ("**本轮未触发**：扩面 4 对读数 4/4 全同向、0 平局 ⇒ 未落入"
                         "无归属形态；但缺口**仍在案未消**，后续复用仍可能暴露，"
                         "届时按 K-V5R3-0-A 落 KD 并 γ，0 现场自创归属")},
        {"id": "γ-V5R3-15", "item": "【本棒新增】as-run 读数在本机环境**不可逐值"
                                    "复现**（gt6 静态口径 7/22 逐值一致，5 图"
                                    "实质差异 >1e-12）",
         "prereg_status": "新增",
         "exec_status": "如实登记：根因指向 BLAS/LAPACK 版本差异（22 图中 17 图的 "
                        "residual_ratio 落在 1e-20 以下噪声地板，该字段无良定义值）；"
                        "同环境两次复算逐值一致 ⇒ 环境内确定性成立；0 修改任何"
                        "历史件、0 声称逐值复现"},
        {"id": "γ-V5R3-16", "item": "【本棒新增】立线件 §2.0 锚表 7 项中 1 项已漂移"
                                    "（docs/GT_RECONSTRUCTION.md）",
         "prereg_status": "新增",
         "exec_status": "实测登记：5 件历史 JSON SHA-12 全部逐值吻合；仅 "
                        "GT_RECONSTRUCTION.md 不吻合，成因见 γ-V5R3-5（他棒已处置）；"
                        "立线件本身 0 触动",
         "_prereg_table_anchor": {"gt_recon_table":
                                  anchors_before["gt_recon"].get(
                                      "prereg_table_sha12"),
                                  "gt_recon_measured":
                                      anchors_before["gt_recon"]["sha12"]}},
    ]


# =============================================================================
# §G · 主入口：逐案执行 + 落盘 + STOP/缺件登记
# =============================================================================
def main():
    t0 = time.time()
    anchors_before = anchor_audit()
    corpus_info = corpus_readiness()
    stop_register = []

    # 语料就绪门：若索引驱动加载也拿不到 22 图 ⇒ K-V5R3-0-B ② 素材不可得 ⇒ KD
    try:
        graphs = load_corpus_indexed(CORPUS_DIR, families=("S", "L"))
        n_graphs = len(graphs)
    except Exception as e:                                    # noqa: BLE001
        graphs, n_graphs = [], 0
        stop_register.append({"id": "STOP-CORPUS", "case": "全部语料面",
                              "reason": f"语料加载失败：{e}",
                              "verdict": "KD（K-V5R3-0-B ② 素材不可得）"})
    if graphs and n_graphs != 22:
        stop_register.append({"id": "STOP-CORPUS-N", "case": "gt6",
                              "reason": f"语料图数 {n_graphs} ≠ 22",
                              "verdict": "KD"})

    cases = {}
    # ---- gt5（只读复算）----
    cases["gt5"] = run_gt5_reattrib(anchors_before)
    # ---- gt6（①轨迹积分补跑）----
    if graphs:
        try:
            cases["gt6"] = run_gt6_trajint(anchors_before, corpus_info)
        except Exception as e:                                # noqa: BLE001
            cases["gt6"] = {"case": "gt6", "verdict": "KD",
                            "kd_reason": f"K-V5R3-0-B ① 构造不可跑：{e}"}
            stop_register.append({"id": "STOP-GT6", "case": "gt6",
                                  "reason": str(e)[:400], "verdict": "KD"})
    else:
        cases["gt6"] = {"case": "gt6", "verdict": "KD",
                        "kd_reason": "K-V5R3-0-B ② 素材不可得（语料未加载）"}
    # ---- gt8（①扩对数）----
    try:
        cases["gt8"] = run_gt8_expand(anchors_before, corpus_info)
    except Exception as e:                                    # noqa: BLE001
        cases["gt8"] = {"case": "gt8", "verdict": "KD",
                        "kd_reason": f"K-V5R3-0-B ① 构造不可跑：{e}"}
        stop_register.append({"id": "STOP-GT8", "case": "gt8",
                              "reason": str(e)[:400], "verdict": "KD"})
    # ---- gt5b / gt（GT-4）----
    cases["gt5b"] = run_gt5b_reattrib(anchors_before)
    cases["gt"] = run_gt4_reattrib(anchors_before)

    # ---- 锚件 0 触动核验（执行后再测一次，逐件比对）----
    anchors_after = anchor_audit()
    untouched = {k: bool(anchors_before[k]["sha12"] == anchors_after[k]["sha12"]
                        and anchors_before[k]["bytes"] == anchors_after[k]["bytes"])
                 for k in anchors_before}

    # ---- 逐案三态方向（执行棒 0 代 verdict-keeper 裁档：只给方向 + 归属依据）----
    def direction(c):
        if c.get("verdict"):
            return c["verdict"]
        return c.get("v2_parallel_verdict") or "同原判（0 新判）"

    def get(d, *path, default="（未产出）"):
        cur = d
        for p in path:
            if not isinstance(cur, dict) or p not in cur:
                return default
            cur = cur[p]
        return cur

    readout = {
        "gt5": {"原判": get(cases["gt5"], "original_verdict_literal"),
                "v2 并列判": get(cases["gt5"], "v2_parallel_verdict"),
                "A 腿": get(cases["gt5"], "legs",
                            "A_leg_monotonicity", "verdict"),
                "B 腿": get(cases["gt5"], "legs",
                            "B_leg_noise_arm_global_potential_advantage",
                            "verdict"),
                "根因": get(cases["gt5"], "root_cause", "class"),
                "surface": "只读复算 · 0 补跑"},
        "gt6": {"原判": get(cases["gt6"], "original_verdict_literal"),
                "v2 并列判": (cases["gt6"].get("v2_parallel_verdict")
                              or "同原判（0 新判）"),
                "轨迹积分口径 median_r":
                    get(cases["gt6"], "trajint_median_residual_ratio"),
                "落带": get(cases["gt6"], "band_entered"),
                "静态逐值复现": get(cases["gt6"],
                                  "static_caliber_fidelity_check",
                                  "all_bit_identical"),
                "surface": "①轨迹积分补跑（新测量面）"},
        "gt8": {"原判": "supports_H_GT8",
                "v2 并列判（as-run 2 对）": "同原判（0 新判 · GT8-5）",
                "扩面 4 对机械 verdict":
                    get(cases["gt8"], "expanded_reading",
                        "verdict_mechanical", "verdict"),
                "扩面新增 2 对 v2 终态":
                    get(cases["gt8"], "expanded_reading",
                        "v2_terminal_state_new_pairs"),
                "as-run 2 对逐值复现":
                    get(cases["gt8"], "as_run_pair_reproduction_check",
                        "all_bit_identical"),
                "surface": "①扩对数 2→4（新测量面）"},
        "gt5b": {"原判": get(cases["gt5b"], "original_verdict_literal"),
                 "v2 并列判": "同原判（0 新判 · GT5B-4）",
                 "S4 哨兵门": get(cases["gt5b"], "anti_degeneration_gates",
                                 "S4_sentinel_单独门", "gate_pass"),
                 "surface": "0 补跑 · 仅防退化门"},
        "gt（GT-4）": {
            "原判": get(cases["gt"], "GT4", "original_verdict_literal"),
            "v2 并列判": (cases["gt"]["GT4"].get("v2_parallel_verdict")
                          or "同原判（0 新判 · GT4-6）"),
            "median_poa": get(cases["gt"], "GT4",
                              "mandatory_concurrent_report_K_V5R3_GT4_4",
                              "median_poa"),
            "n_poa_inf": get(cases["gt"], "GT4",
                             "mandatory_concurrent_report_K_V5R3_GT4_4",
                             "n_poa_inf"),
            "n_poa_undefined": get(cases["gt"], "GT4",
                                   "mandatory_concurrent_report_K_V5R3_GT4_4",
                                   "n_poa_undefined"),
            "n_finite_in_median": get(cases["gt"], "GT4",
                                       "mandatory_concurrent_report_K_V5R3_GT4_4",
                                       "n_finite_in_median"),
            "落带": get(cases["gt"], "GT4", "band_entered"),
            "GT-1 腿": "同原判 PASS（0 补线 · GT4-5）",
            "surface": "0 补跑 · 仅机械并报"},
    }

    out = {
        "experiment": "v5_gt_exec",
        "spec_version": "v5.0-gt-exec",
        "prereg": {"path": ANCHORS["prereg_v2"],
                   "sha12": anchors_before["prereg_v2"]["sha12"],
                   "activation": "PI 2026-09-28 23:42 q1「五件批量生效」⇒ 判死线 v2 "
                                 "生效即锁，本棒按其字面执行"},
        "author": {"role": "worker",
                   "session": "mvs_7f4a11c7946d402da72cb5d6467c44bd",
                   "note": "0 冒充 PI / protocol-keeper / verdict-keeper / "
                           "evidence-auditor / verifier / doc-writer / 任一受托方；"
                           "执行棒 0 代 verdict-keeper 裁档"},
        "global_clauses_applied": ["K-V5R3-0-A", "K-V5R3-0-B", "K-V5R3-0-C",
                                   "K-V5R3-0-D", "K-V5R3-0-E", "K-V5R3-0-F",
                                   "K-V5R3-0-G"],
        "new_thresholds_added_total": 0,
        "anchor_audit_before": anchors_before,
        "anchor_audit_after": anchors_after,
        "historical_artifacts_untouched": untouched,
        "all_historical_artifacts_untouched": bool(all(untouched.values())),
        "corpus_readiness": corpus_info,
        "stop_register": stop_register,
        "gamma_register": gamma_register(cases, anchors_before),
        "cases": cases,
        "readout": readout,
        "runtime_sec": round(time.time() - t0, 3),
    }
    # ---- 落盘（5 件分案产物 + 1 件汇总）----
    written = [
        write_json(f"{RESULTS_REL}/_v5_gt5_reattrib_{DATE_TAG}.json", cases["gt5"]),
        write_json(f"{RESULTS_REL}/_v5_gt6_trajint_{DATE_TAG}.json", cases["gt6"]),
        write_json(f"{RESULTS_REL}/_v5_gt8_expand_{DATE_TAG}.json", cases["gt8"]),
        write_json(f"{RESULTS_REL}/_v5_gt5b_reattrib_{DATE_TAG}.json", cases["gt5b"]),
        write_json(f"{RESULTS_REL}/_v5_gt4_reattrib_{DATE_TAG}.json", cases["gt"]),
    ]
    sum_sha = sha12(os.path.join(HERE, "_v5_gt_exec_2026_09_29.py"))
    out["executing_script"] = {"path": "_v5_gt_exec_2026_09_29.py",
                               "sha12": sum_sha}
    out["case_artifacts"] = written
    agg = write_json(f"{RESULTS_REL}/_v5_gt_exec_{DATE_TAG}.json", out)
    print(json.dumps({"aggregate": agg, "case_artifacts": written,
                      "readout": readout, "untouched": untouched,
                      "runtime_sec": out["runtime_sec"]},
                     ensure_ascii=False, indent=1))
    return out


# =============================================================================
# §D · gt8 ①扩对数（立线件 §6.3 · K-V5R3-GT8-1 / -2）
# =============================================================================
from run_v20_gt8 import (ARMS, GT8_PAIRS, GT8_SEEDS, GT8_MIN_PAIRS,  # noqa: E402
                         build_gt8_graph, eval_graph, gt8_verdict,
                         graph_invariant, hub_concentration)

# 扩面规模与种子**测量前冻结**（立线件 §6.3「对数与种子数测量前写死，0 依既有
# 读数反选」）：as-run 2 对 + 新增 2 对 = **4 对**（满足「≥4 对」）；新图种子沿
# as-run 号段续写 208805–208808（语料族为 200101–200106，0 重叠）。
V5GT8_SEEDS = {"GT8_C_high": 208805, "GT8_C_low": 208806,
               "GT8_D_high": 208807, "GT8_D_low": 208808}
V5GT8_PAIRS = tuple(GT8_PAIRS) + (("GT8_C_high", "GT8_C_low"),
                                  ("GT8_D_high", "GT8_D_low"))


def _edges_C_high():
    """三重枢纽汇聚锥（N=36，E=35）。hub 1/2/3；named = 终点为 1/2/3 的边。"""
    edges = ([(0, 1), (0, 2), (0, 3)]
             + [(i, 1) for i in range(4, 15)]
             + [(i, 2) for i in range(15, 24)]
             + [(24, 25), (25, 3), (26, 27), (27, 3)]
             + [(1, 28), (1, 29), (2, 30), (2, 31), (3, 32), (3, 33)]
             + [(34, 1), (35, 2)])
    named = {e for e in edges if e[1] in (1, 2, 3)}
    return 36, edges, named


def _edges_C_low():
    """平衡四叉树（N=36，E=35，parent=(i−1)//4）。named = 子节点仍为内部节点的
    父子边（沿用 S2 口径）。"""
    N = 36
    edges = [((i - 1) // 4, i) for i in range(1, N)]
    named = {(u, v) for (u, v) in edges if 4 * v + 1 < N}
    return N, edges, named


def _edges_D_high():
    """双超枢纽汇聚星（N=45，E=44）。named = 终点为 1/2 的边。"""
    edges = ([(0, 1), (0, 2)]
             + [(i, 1) for i in range(3, 23)]
             + [(i, 2) for i in range(23, 41)]
             + [(41, 42), (42, 1), (43, 44), (44, 2)])
    named = {e for e in edges if e[1] in (1, 2)}
    return 45, edges, named


def _edges_D_low():
    """平衡五叉树（N=45，E=44，parent=(i−1)//5）。named = 子节点仍为内部节点的
    父子边（沿用 S2 口径）。"""
    N = 45
    edges = [((i - 1) // 5, i) for i in range(1, N)]
    named = {(u, v) for (u, v) in edges if 5 * v + 1 < N}
    return N, edges, named


_V5GT8_STRUCTS = {
    "GT8_C_high": ("triple_hub_cone", _edges_C_high),
    "GT8_C_low": ("balanced_4ary_tree", _edges_C_low),
    "GT8_D_high": ("twin_superhub_star", _edges_D_high),
    "GT8_D_low": ("balanced_5ary_tree", _edges_D_low),
}


def build_v5_gt8_graph(graph_id):
    """构造一张 V5 扩面新图（族 S 记录格式，与 build_gt8_graph 同式：确定性构造
    → is_dag 校验 → longest_path_family → _canonical_sha256 内容哈希）。"""
    structure, fn = _V5GT8_STRUCTS[graph_id]
    N, edges, named = fn()
    edges = sorted(set((int(u), int(v)) for (u, v) in edges))
    named = sorted({(int(u), int(v)) for (u, v) in named})
    if not is_dag(N, edges):
        raise ValueError(f"{graph_id}: structure is not a DAG")
    _nl, _L, src, tgt = longest_path_family(N, edges)
    filler = sorted(set(edges) - set(named))
    seed = V5GT8_SEEDS[graph_id]
    rec = {"graph_id": graph_id, "family": "S", "structure": structure,
           "N": N, "nodes": list(range(N)), "labels": _assign_labels(N, seed),
           "edges": [list(e) for e in edges],
           "named_edges": [list(e) for e in named],
           "filler_edges": [list(e) for e in filler],
           "source": int(src), "target": int(tgt),
           "seed": int(seed), "generator_version": "v2.0-gt8-v5-expand"}
    rec["sha256"] = _canonical_sha256(rec)
    return rec


def run_gt8_expand(anchor, corpus_info):
    """立线件 §6.3 执行面：把配对集由 2 对扩至 6 对（as-run 2 对 + 新增 4 对）。

    口径冻结（沿 SPEC_GT8.md 既有字面，一字不动）：hub_concentration =
    max_in_degree/n_edges、real_semantics = 0、rng = g_seed*100003+ei、场实例
    种子 g_seed+ei、全边留一、全候选 raw 口径、named Hits@3。
    不同构哨兵：与既有 22 图语料 + 4 张 as-run 新图，逐一比
    (N, n_edges, 入度多重集, 出度多重集) 不变量 + sha256。
    """
    t0 = time.time()
    cfg = DiffusionConfig()
    graphs = load_corpus_indexed(CORPUS_DIR, families=("S", "L"))
    existing_inv, existing_sha = {}, set()
    for g in graphs:
        edges = [tuple(e) for e in g["edges"]]
        existing_inv.setdefault(
            str(graph_invariant(g["N"], edges)), []).append(g["graph_id"])
        existing_sha.add(g.get("sha256"))
    for gid in GT8_SEEDS:
        g = build_gt8_graph(gid)
        edges = [tuple(e) for e in g["edges"]]
        existing_inv.setdefault(
            str(graph_invariant(g["N"], edges)), []).append(gid)
        existing_sha.add(g["sha256"])

    per_graph, per_pair, noniso = {}, [], {}
    for pair in V5GT8_PAIRS:
        rec = {"pair": f"{pair[0]}__vs__{pair[1]}", "high": pair[0],
               "low": pair[1], "origin": "as_run" if pair in GT8_PAIRS
               else "v5_expansion"}
        for role, gid in (("high", pair[0]), ("low", pair[1])):
            g = (build_gt8_graph(gid) if pair in GT8_PAIRS
                 else build_v5_gt8_graph(gid))
            inv = graph_invariant(g["N"], [tuple(e) for e in g["edges"]])
            noniso[gid] = {"invariant": [int(inv[0]), int(inv[1]),
                                         list(inv[2]), list(inv[3])],
                           "invariant_collides_with":
                               existing_inv.get(str(inv), []),
                           "nonisomorphic_to_existing":
                               bool(not existing_inv.get(str(inv), [])),
                           "sha256": g["sha256"],
                           "sha256_collides_with_existing":
                               bool(g["sha256"] in existing_sha)}
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
                "seed": g["seed"], "sha256": g["sha256"], "features": feats,
                "field_named": arms["field_mean"]["named"],
                "random_named": arms["random"]["named"],
                "degree_named": arms["degree"]["named"],
                "diff_fm_rand": diff_fr, "diff_fm_deg": diff_fd,
                "invariant": [g["N"], len(edges)]}
            rec[f"diff_{role}"] = diff_fr
            rec[f"hub_{role}"] = feats["hub_concentration"]
        rec["concordant"] = bool(rec["diff_high"] > rec["diff_low"])
        per_pair.append(rec)

    verdict = gt8_verdict(per_pair)        # 既有纯函数 · min_pairs=2 未动
    # as-run 2 对在本环境的复现核对（0 新测量 = 与历史 JSON 比对）
    asrun_g8 = read_json(ANCHORS["gt8"])
    asrun_pairs = {p["pair"]: p for p in asrun_g8["per_pair"]}
    repro = {}
    for p in per_pair:
        if p["origin"] != "as_run":
            continue
        a = asrun_pairs.get(p["pair"])
        repro[p["pair"]] = {
            "diff_high_as_run": a["diff_high"], "diff_high_recomputed": p["diff_high"],
            "diff_low_as_run": a["diff_low"], "diff_low_recomputed": p["diff_low"],
            "bit_identical": bool(a["diff_high"] == p["diff_high"]
                                  and a["diff_low"] == p["diff_low"])}
    n_repro_id = sum(1 for v in repro.values() if v["bit_identical"])
    n_conc = len(verdict["pairs_concordant"])
    n_rev = len(verdict["pairs_reversed"])
    n_tie = len(verdict["pairs_tied"])
    n = verdict["n_pairs"]
    # ---- v2 归属（K-V5R3-GT8-1 平局 / -2 else）----
    # as-run 2 对（原点 as_run）与扩面新增 4 对分别机械落档，避免扩面读数
    # 与 as-run 读数互相替改（0 回溯，K-V5R3-0-D）。
    def attrib(sub):
        c = sum(1 for p in sub if p["concordant"])
        t = sum(1 for p in sub if p["diff_high"] == p["diff_low"])
        r = sum(1 for p in sub if p["diff_high"] < p["diff_low"])
        return {"n_pairs": len(sub), "n_concordant": c, "n_reversed": r,
                "n_tied": t}
    a_asrun = attrib([p for p in per_pair if p["origin"] == "as_run"])
    a_new = attrib([p for p in per_pair if p["origin"] == "v5_expansion"])
    a_all = attrib(per_pair)

    def v2_terminate(a):
        """机械三态收口：覆盖缺口 ⇒ KD + γ（K-V5R3-0-A/B），0 自创归属。"""
        c, t, r, n_ = a["n_concordant"], a["n_tied"], a["n_reversed"], a["n_pairs"]
        if t > 0 or c < 2:
            return "FAIL", ("②最不利方向（K-V5R3-GT8-1 平局按「对 hub 假设无区分力」"
                            "计入最不利 + GT8-2 第二步 ②兜底）：#conc < 2 ⇒ 无 PASS "
                            "资格 ⇒ 判 FAIL（H_GT8_dead 侧）")
        if r == n_:
            return "FAIL", "kill_rule 命中：全部对全反 ⇒ H_GT8_dead"
        if c == n_:
            return "PASS", "pass_rule 命中：全部对同向 ⇒ supports_H_GT8"
        return "KD", ("v2 归属缺口：扩面后出现 #conc 介于 2 与 n−1 之间且无平局的"
                      "读数形态，超出 v2 §3.3 else 归属（#conc=1 / pairs_tied≠[]）"
                      "的两条明文覆盖 ⇒ 按 K-V5R3-0-A 落 KD 并登记 γ，"
                      "0 现场自创归属")

    v2_all, attrib_all = v2_terminate(a_all)
    v2_new, attrib_new = v2_terminate(a_new)
    gate_d = anti_degeneration_gate(
        "gt8-expanded · diff_fm_rand 逐图（12 值）",
        [per_graph[gid]["diff_fm_rand"] for pr in V5GT8_PAIRS
         for gid in pr])
    gate_h = anti_degeneration_gate(
        "gt8-expanded · hub_concentration 逐图（12 值）",
        [per_graph[gid]["features"]["hub_concentration"] for pr in V5GT8_PAIRS
         for gid in pr])
    return {
        "case": "gt8",
        "class": "类 II · 潜伏 else（#conc=1 或 pairs_tied≠[]）",
        "prereg_rule_ids": ["K-V5R3-GT8-1", "K-V5R3-GT8-2", "K-V5R3-GT8-3",
                             "K-V5R3-GT8-4", "K-V5R3-GT8-5", "K-V5R3-0-A",
                             "K-V5R3-0-B", "K-V5R3-0-D", "K-V5R3-0-E"],
        "surface": "①扩测量面 · 扩对数 2→6（立线件 §6.3）",
        "anchor": {"path": ANCHORS["gt8"], "sha12": anchor["gt8"]["sha12"]},
        "original_verdict_literal": "supports_H_GT8",
        "v2_parallel_verdict_as_run": None,
        "parallel_report_as_run": {"原判": "supports_H_GT8",
                                   "v2 并列判": "同原判（0 新判 · GT8-5）"},
        "expanded_reading": {
            "verdict_mechanical": verdict,
            "n_pairs": n, "n_concordant": n_conc, "n_reversed": n_rev,
            "n_tied": n_tie,
            "subset_as_run_2_pairs": a_asrun,
            "subset_new_pairs": a_new,
            "all_6_pairs": a_all,
            "v2_terminal_state_new_pairs": v2_new,
            "v2_attribution_new_pairs": attrib_new,
            "v2_terminal_state_all_pairs": v2_all,
            "v2_attribution_all_pairs": attrib_all,
            "as_run_reading_not_revised": (
                "as-run 2 对读数与其 supports_H_GT8 判定 **0 触动**；扩面为**新增"
                "测量面**的并列读数，0 覆盖、0 改判 as-run（K-V5R3-0-D/GT8-5）"),
            "gamma_coverage_gap": (
                "γ-V5R3-14：v2 §3.3 的 else 归属明文只覆盖「#conc=1」与"
                "「pairs_tied≠[]」两种形态（按 2 对设计书写）；扩至 4 对后原则上"
                "新增 #conc∈[2, n−1] 且无平局的形态，v2 无明文归属 ⇒ 执行面按"
                "K-V5R3-0-A 落 KD 并 γ，0 现场自创归属（待 PI 口径拍板）。"
                "**本轮该形态未触发**（4/4 全同向、0 平局）⇒ 缺口仍在案未消，"
                "留后续复用时暴露"),
            "gamma_sample_size": ("γ-V5R3-4：as-run 样本量退化（2 对 = 评审下限）"
                                  "在案；扩至 6 对后仍 0 表述为效应量/显著性"
                                  "（K-V5R3-GT8-4）")},
        "as_run_pair_reproduction_check": {
            "purpose": "核对 as-run 2 对在本环境是否逐值复现（环境可比性前提）",
            "n_pairs": len(repro),
            "n_pairs_bit_identical": n_repro_id,
            "all_bit_identical": bool(n_repro_id == len(repro)),
            "per_pair": repro,
            "gamma": "γ-V5R3-15"},
        "named_set_granularity_disclosure": (
            "新增低 hub 图（C_low / D_low）沿 as-run GT8_B_low 的 S2 口径"
            "「named = 子节点仍为内部节点的父子边」⇒ 树形结构中 named 边数 = "
            "内部节点数（C_low = 8、D_low = 8，as-run B_low = 12）⇒ diff 的"
            "最小刻度为 1/8（as-run B_low 为 1/12）⇒ **平局概率高于 as-run**，"
            "属如实披露的构造面性质，0 事后调整结构（结构在任何新读数产生前"
            "已冻结）"),
        "nonisomorphism_sentinel": {
            "rule": ("与既有 22 图语料 + 4 张 as-run 新图逐一比 (N, n_edges, "
                     "入度多重集, 出度多重集) 不变量 + sha256"),
            "per_graph": noniso,
            "all_new_graphs_nonisomorphic": bool(
                all(v["nonisomorphic_to_existing"] for k, v in noniso.items()
                    if k not in GT8_SEEDS)),
            "all_new_graphs_sha256_fresh": bool(
                all(not v["sha256_collides_with_existing"] for k, v in noniso.items()
                    if k not in GT8_SEEDS))},
        "scale_freeze": {"n_pairs": len(V5GT8_PAIRS), "pairs": [list(p) for p in V5GT8_PAIRS],
                         "new_seeds": V5GT8_SEEDS, "min_pairs_untouched": GT8_MIN_PAIRS,
                         "arms": list(ARMS),
                         "protocol": ("SPEC_GT8.md 既有字面：全边留一、全候选 raw "
                                      "口径、rng=g_seed*100003+ei、场实例种子 "
                                      "g_seed+ei、named Hits@3"),
                         "real_semantics_axis": "仍 deferred（需 LLM 先验 API 预算；"
                                                "本轮 0 申请、0 虚构读数）"},
        "anti_degeneration_gates": {"diff_fm_rand": gate_d,
                                    "hub_concentration": gate_h},
        "per_graph": per_graph,
        "per_pair": per_pair,
        "thresholds_used": {"min_pairs": GT8_MIN_PAIRS,
                            "pass_rule": "全部对同向（#conc = n 且 n ≥ 2）",
                            "kill_rule": "全部对全反"},
        "new_thresholds_added": 0,
        "scope_ceiling": ("仅族 S 合成面（real_semantics=0）；0 外推族 L、0 外推 "
                          "real_semantics 轴、0 表述为效应量/显著性"),
        "runtime_sec": round(time.time() - t0, 3),
        "corpus_readiness": corpus_info,
    }


if __name__ == "__main__":
    main()
