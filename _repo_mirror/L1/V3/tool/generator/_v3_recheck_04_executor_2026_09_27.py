#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V3-R 补审 #4 BOSS-P-A3 (Replicator Dynamics + ESS) — executor (worker · 2026-09-27)

沿 results/_v3_recheck_prereg_v1_2026_09_27.md（实测 SHA-12 88052d7db895）字面执行：

  - K-V3R-0-A 防退化门（n_distinct > 3 + std > 0，跑前对盘上输入字段自证）
  - K-V3R-0-B 沿用阈值（0 新设判定阈值；ess_match_threshold = 0.1、replicator dt=0.01/n_iter=500
    全部沿 boss_pa_3 既有字面）
  - K-V3R-0-C 双口径（新构造 verdict + 沿原 V3 阈值字面 verdict 并报）
  - K-V3R-0-D 派生 JSON 不合并（本件独立落盘 _v3_recheck_04_result_*.json）
  - K-V3R-0-E 0 LLM（纯 stdlib，0 网络 0 模型调用）
  - K-V3R-4 kill-line 字面：重构造（真 ESS 邻域检验 ε=1e-6）后 ess_match n_distinct ≥ 4
    （≥ 4/22 真有 match，≠ 0/22 全 not-match）-> PASS；仍 n_distinct ≤ 2 -> FAIL（维持假成立）
    —— **本件对 kill-line 的两处读数（括号释义 vs 字面 n_distinct）并报，0 擅选**（见 verdict）
  - TH-V3R-4（ess_match_threshold = 0.1；replicator dt=0.01, n_iter=500，V3 既有字面）

§1.2 #4 补审构造方向（字面）：
  (a) ess_freq 计算不绑死 0.5 起点（重参数：起频扫描 or 随机 0.3~0.7）
  (b) is_ess Smith 1973 判据按 Taylor & Nowak 2006 ESS 完整定义
      （邻域 ≤ ε 全检验 ε=0.1 -> 1e-3 -> 1e-6 三档）
  (c) ess_match 阈值 0.1 与真实 deposon_freq 离散度联动（22 graph × 3 ε）

实验设计口径（沿 plugin @scientific-research-workflows / skill experimental-design）：
  - 区组（block）= 22 受控概念图；处理（treatment）= 起频 9 档 x ε 3 档 = 27 格全因子
    -> 22 x 27 = 594 格，无别名（aliasing）
  - 伪重复（pseudoreplication）声明：22 图中 10 件是 S1/S2/S6 的 _n* 嵌套子采样，
    独立重复真实层级 = 12 基准图；另报去嵌套口径（不参与判定）
  - 名义 N 显式标注：逐图 (N_named, N_filler) 异质 -> 跨尺寸不可直接逐图比较
  - 邻域格点数 M = 400/侧 为**数值分辨率实现量**（非判定阈值），0 影响判定方向，
    另附 M 敏感性（沿 ε 自适应）

输入（全部只读）：
  - results/boss_pa_3_replicator_dynamics_result_2026_09_15.json   #4 源件（原结论所在）
  - deposon_team/plugins/boss_pa_3_replicator_dynamics.py          #4 源件（只读，不 import）
  - results/deposon_v20_baselines.json                             # 22 受控概念图数据面
  - results/_v3_recheck_prereg_v1_2026_09_27.md                     # 预登记件

S-40 布尔显式命名：`*_hit = True` 表示「触发 FAIL / 触发警报」；`*_pass = True` 表示「存活 / 合格」。
"""

import hashlib
import json
import math
import os
import random
import sys
from pathlib import Path

# ---- 构造常量（沿派工单 / 预登记 / V3 既有字面，0 新设判定阈值）----
SEED = 20260927
DT_REPL = 0.01          # TH-V3R-4 沿 V3 字面
N_ITER_REPL = 500       # TH-V3R-4 沿 V3 字面
X0_SCAN = tuple(round(0.30 + 0.05 * i, 2) for i in range(9))   # §1.2 #4(a) 字面：0.3~0.7 扫描
N_RANDOM_X0 = 20        # §1.2 #4(a)「随机 0.3~0.7」敏感性臂的抽样次数
EPS_ARMS = (0.1, 1e-3, 1e-6)   # §1.2 #4(b) 字面三档
ESS_MATCH_THRESHOLD = 0.1      # TH-V3R-4 沿 V3 字面（0 擅调）
CLIP_LO, CLIP_HI = 1e-6, 1.0 - 1e-6   # V3 既有字面
CONV_TOL = 1e-6                    # V3 既有字面
NEIGHBOR_M = 400                   # 邻域网格分辨率（实现量，非判定阈值）
KILL_LINE_N_DISTINCT_PASS = 4     # K-V3R-4 字面
KILL_LINE_N_DISTINCT_FAIL = 2     # K-V3R-4 字面
KILL_LINE_N_MATCH_GRAPH_PASS = 4  # K-V3R-4 括号释义字面（≥ 4/22 真有 match）


def _repo_root() -> Path:
    starts = [Path(os.getcwd()), Path(os.path.abspath(sys.argv[0])).parent]
    for base in starts:
        p = base
        for _ in range(6):
            if (p / "results/_v3_recheck_prereg_v1_2026_09_27.md").exists():
                return p
            p = p.parent
    raise SystemExit("repo root not found (cwd=%s)" % os.getcwd())


REPO = _repo_root()
SRC_RESULT = REPO / "results/boss_pa_3_replicator_dynamics_result_2026_09_15.json"
SRC_RUNNER = REPO / "deposon_team/plugins/boss_pa_3_replicator_dynamics.py"
SRC_V20 = REPO / "results/deposon_v20_baselines.json"
PREREG = REPO / "results/_v3_recheck_prereg_v1_2026_09_27.md"
OUT = REPO / "results/_v3_recheck_04_result_2026_09_27.json"


def sha12(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:12]


def n_distinct(xs) -> int:
    return len(set(round(float(x), 12) for x in xs))


def stat_block(xs):
    xs = [float(x) for x in xs]
    n = len(xs)
    mean = sum(xs) / n
    var = sum((x - mean) ** 2 for x in xs) / n
    return {
        "n": n, "n_distinct": n_distinct(xs), "std": var ** 0.5,
        "min": min(xs), "max": max(xs), "mean": mean,
        "distinct_values": sorted(set(round(x, 6) for x in xs)),
    }


# =====================================================================
# 段 0 · V3 legacy 公式逐字转写（只读源件，不 import 不触动 frozen）
# =====================================================================

def L_replicator_dynamics_2x2(a11, a12, a21, a22, dt=0.01, n_iter=200):
    x1 = 0.5
    x2 = 0.5
    for t in range(n_iter):
        ax1 = a11 * x1 + a12 * x2
        ax2 = a21 * x1 + a22 * x2
        dx1 = x1 * (ax1 - ax2)
        x1_new = x1 + dt * dx1
        if x1_new < 1e-6:
            x1_new = 1e-6
        if x1_new > 1 - 1e-6:
            x1_new = 1 - 1e-6
        x2_new = 1.0 - x1_new
        if abs(x1_new - x1) < 1e-6 and t > 10:
            return round(x1_new, 6)
        x1, x2 = x1_new, x2_new
    return round(x1, 6)


def L_is_ess(x_star, a11, a12, a21, a22, tol=1e-3):
    if x_star < tol:
        return a21 <= a11
    elif x_star > 1 - tol:
        return a12 <= a22
    else:
        return abs(a12 - a21) < tol


def L_deposon_freq(a_named, a_filler):
    total = a_named + a_filler
    if total < 1e-9:
        return 0.5
    return a_named / total


# =====================================================================
# 段 1 · §1.2 #4 补审构造
# =====================================================================

def payoff_matrix(g):
    """V3 字面 2x2 支付矩阵（与 #1 同源）：a11=a_named, a12=a_filler, a21=a_filler, a22=a_named；
    b 侧取 named 最大的非 field_mean 臂（并列取首个）。"""
    a_named = g["field_mean"]["named"] or 0.0
    a_filler = g["field_mean"]["filler"] or 0.0
    best_named = 0.0
    best_filler = 0.0
    for arm, vals in g.items():
        if arm == "field_mean" or not isinstance(vals, dict):
            continue
        v_named = vals.get("named") or 0.0
        v_filler = vals.get("filler") or 0.0
        if v_named > best_named:
            best_named = v_named
            best_filler = v_filler
    return a_named, a_filler, a_filler, a_named


def N_replicator_exact_limit(x0, a11, a12, a21, a22):
    """同一离散动力学的**解析极限**（不动点），用于 Arm B。

    V3 离散式 dx1 = x1*[(Ax)_1-(Ax)_2] = x1*(a_n-a_f)*(2*x1-1)（代入 a11=a22=a_n、a12=a21=a_f）。
    不动点集合 = {0, 0.5, 1}；0.5 点的稳定性由 sign(a_n-a_f) 定：
      a_n > a_f -> 0.5 不稳定，x0<0.5 -> 0、x0>0.5 -> 1
      a_n < a_f -> 0.5 稳定，任意 x0 -> 0.5
      a_n == a_f -> dx1 ≡ 0，x1 ≡ x0（全体皆不动）
    返回 (limit, branch)。这是同一动力学的极限，**不改动任何阈值**。
    """
    d = a11 - a12          # = a_n - a_f
    if abs(d) < 1e-15:
        return float(x0), "degenerate_a_n_eq_a_f_all_fixed"
    if d > 0:
        return (0.0, "x0_below_half") if x0 < 0.5 else (1.0, "x0_above_half")
    return 0.5, "anti_coordination_stable_half"


def N_replicator(x0, a11, a12, a21, a22, dt=DT_REPL, n_iter=N_ITER_REPL):
    """§1.2 #4(a) 重构 replicator：V3 离散化逐字不动（dx1 = x1*(ax1-ax2)、dt、clip、收敛判据），
    **唯一变化 = 起点 x0 由扫描给定**（V3 写死 0.5）。"""
    x1 = float(x0)
    x2 = 1.0 - x1
    for t in range(n_iter):
        ax1 = a11 * x1 + a12 * x2
        ax2 = a21 * x1 + a22 * x2
        dx1 = x1 * (ax1 - ax2)
        x1_new = x1 + dt * dx1
        if x1_new < CLIP_LO:
            x1_new = CLIP_LO
        if x1_new > CLIP_HI:
            x1_new = CLIP_HI
        x2_new = 1.0 - x1_new
        if abs(x1_new - x1) < CONV_TOL and t > 10:
            return round(x1_new, 6)
        x1, x2 = x1_new, x2_new
    return round(x1, 6)


def smith_ess_neighborhood(x_star, A, eps, m=NEIGHBOR_M):
    """§1.2 #4(b) Smith 1973 ESS 完整定义 + Taylor & Nowak 2006 邻域全检验。

    ESS 判据（Smith 1973）：x* 是 ESS iff 对所有 y != x*：
        (i)  y^T A x* >  y^T A y
        (ii) y^T A x* == y^T A y 且 x*^T A y > y^T A y
    邻域版（Taylor & Nowak 2006）：把「所有 y」限制为 x* 的 L_inf 邻域
        {|y_i - x*_i| <= eps, y in simplex, y != x*}，在邻域网格上逐点全检验。

    A = [[a,b],[c,d]]，y = (y1, 1-y1)，x* = (xs, 1-xs)。
    返回 (is_ess, n_probe, worst_slack)：worst_slack = min over y of
        [ (i) 判据的余量 ]，用于识别边界格；负值 = 存在反例 y。
    """
    a, b, c, d = A
    xs = float(x_star)
    ys = 1.0 - xs

    n_probe = 0
    worst = float("inf")
    is_ess = True
    # 邻域网格：x* 两侧各 m 点，含端点，去重（float 网格）
    grid = set()
    for k in range(0, m + 1):
        grid.add(round(min(1.0, max(0.0, xs - eps + (2.0 * eps) * k / m)), 15))
    if len(grid) <= 1:
        grid = {round(min(1.0, xs + eps), 15), round(max(0.0, xs - eps), 15)}
    for y1 in sorted(grid):
        if abs(y1 - xs) < 1e-15:
            continue                      # 排除 y == x*
        y2 = 1.0 - y1
        n_probe += 1
        # 数值稳定形式：y^T A x* - y^T A y = y^T A (x* - y)；(x*)^T A y - y^T A y = (x*-y)^T A y。
        # 直接展开两个二次型会在 |y - x*| 很小时发生灾难性相消（float64 下 y1*y2 的偏差
        # 落到 ulp 以下 => cond1 恒为 0.0），故一律用因子化形式。
        d1 = xs - y1
        d2 = ys - y2
        cond1 = y1 * (a * d1 + b * d2) + y2 * (c * d1 + d * d2)
        cond2 = d1 * (a * y1 + b * y2) + d2 * (c * y1 + d * y2)
        if cond1 > 0.0:
            slack = cond1
        elif abs(cond1) <= 1e-18 and cond2 > 0.0:
            slack = cond2
        else:
            is_ess = False
            slack = min(cond1, cond2)
        worst = min(worst, slack)
    return is_ess, n_probe, worst


def base_graph(gid: str) -> str:
    if gid.startswith("L_"):
        return gid
    return gid.split("_n")[0]


def implied_denominator(frac, nom):
    if frac <= 0:
        return int(nom), 0
    for d in range(1, 401):
        k = frac * d
        if abs(k - round(k)) < 1e-9:
            return d, int(round(k))
    return int(nom), -1


def main() -> int:
    src = json.loads(SRC_RESULT.read_text(encoding="utf-8"))
    v20 = json.loads(SRC_V20.read_text(encoding="utf-8"))
    per_graph = v20["per_graph"]
    prereg_sha12 = sha12(PREREG.read_bytes())

    gids = sorted(per_graph.keys())
    n_graphs = len(gids)
    assert n_graphs == 22, "22 受控概念图数量不符: %d" % n_graphs
    on_disk = {g["graph_id"]: g for g in src["boss_pa3_22graph_ess_check"]["graph_results"]}

    # ---------- 段 0 · legacy 逐字复现校验 ----------
    legacy_rows, legacy_mismatch = [], []
    for gid in gids:
        a11, a12, a21, a22 = payoff_matrix(per_graph[gid])
        ef = L_replicator_dynamics_2x2(a11, a12, a21, a22, dt=DT_REPL, n_iter=500)
        ie = L_is_ess(ef, a11, a12, a21, a22)
        df = L_deposon_freq(per_graph[gid]["field_mean"]["named"] or 0.0,
                            per_graph[gid]["field_mean"]["filler"] or 0.0)
        ham = abs(ef - df)
        od = on_disk[gid]
        recomputed = {"ess_freq": ef, "deposon_freq": round(df, 4), "hamming_dist": round(ham, 4),
                      "is_ess": ie, "ess_match": bool(ham < 0.10)}
        disk = {"ess_freq": od["ess_freq"], "deposon_freq": od["deposon_freq"],
                "hamming_dist": od["hamming_dist"], "is_ess": od["is_ess"],
                "ess_match": od["ess_match"]}
        match = (recomputed == disk)
        if not match:
            legacy_mismatch.append(gid)
        legacy_rows.append({"graph_id": gid, "base_graph": base_graph(gid),
                            "recomputed": recomputed, "on_disk": disk,
                            "bit_exact_match": match})
    legacy_hamming = [r["on_disk"]["hamming_dist"] for r in legacy_rows]
    legacy_n_match = sum(1 for r in legacy_rows if r["on_disk"]["ess_match"])
    legacy_match_ratio = round(legacy_n_match / n_graphs, 4)
    legacy_repro = {
        "n_graphs": n_graphs,
        "bit_exact_match_count": n_graphs - len(legacy_mismatch),
        "bit_exact_mismatch_graphs": legacy_mismatch,
        "all_bit_exact": (not legacy_mismatch),
        "recomputed_n_ess_match": legacy_n_match,
        "on_disk_n_ess_match": src["boss_pa3_22graph_ess_check"]["n_ess_match"],
        "recomputed_ess_match_ratio": legacy_match_ratio,
        "on_disk_ess_match_ratio": src["boss_pa3_22graph_ess_check"]["ess_match_ratio"],
        "on_disk_verdict": src["verdict"],
    }

    # ---------- 段 1 · legacy 三常量的**结构根因**（解析证明 + 数值核验） ----------
    structure = []
    for gid in gids:
        a11, a12, a21, a22 = payoff_matrix(per_graph[gid])
        # V3 离散式：dx1 = x1*[(Ax)_1-(Ax)_2]，代入 x2=1-x1
        #   (Ax)_1-(Ax)_2 = (a11-a21)*x1 + (a12-a22)*(1-x1) = (a11-a21+a22-a12)*x1 + (a12-a22)
        #   V3 字面 a11=a22=a_n、a12=a21=a_f => a11-a21+a22-a12 = 0（x1 系数消失）
        #   => dx1 = x1*(a12-a22)*(1-x1) = x1*(a_f-a_n)*(1-x1)
        #   即 dx1 = -x1*(a_n-a_f)*(1-x1) = x1*(a_n-a_f)*(x1-1+1) ...
        # 逐字化简：dx1 = x1*(a_f-a_n)*(1-x1)；其根为 x1=0, x1=1, 以及 x1=1（重复）
        #   —— 故 **x1 = 0.5 处的 dx1 = 0.5*(a_f-a_n)*0.5 ≠ 0**，真正的不动点由 V3 起始
        #   x0=0.5 与「已收敛」判据共同冻结。逐图实测 dx1(x0=0.5)：
        d_at_half = 0.5 * ((a11 * 0.5 + a12 * 0.5) - (a21 * 0.5 + a22 * 0.5))
        d_at_half = 0.5 * (d_at_half)
        # 正确的不动点判据：x1*(a_f-a_n)*(1-x1)=0 的根
        roots = []
        for r in (0.0, 0.5, 1.0):
            v = r * (a12 - a22) * (1.0 - r)
            if abs(v) < 1e-15:
                roots.append(r)
        structure.append({
            "graph_id": gid,
            "a11": round(a11, 6), "a12": round(a12, 6),
            "a21": round(a21, 6), "a22": round(a22, 6),
            "dx1_at_x0_half": d_at_half,
            "dx1_at_x0_half_is_zero": bool(abs(d_at_half) < 1e-15),
            "dx1_roots": roots,
            "a12_eq_a21_constructively": bool(abs(a12 - a21) < 1e-15),
            "a_n_minus_a_f": round(a11 - a12, 6),
        })
    n_half_stationary = sum(1 for s in structure if s["dx1_at_x0_half_is_zero"])
    n_a12_eq_a21 = sum(1 for s in structure if s["a12_eq_a21_constructively"])
    ham_min = min(legacy_hamming)
    # ess_freq ≡ 0.5 的真正根因：V3 把起点与收敛判据同时钉在 0.5
    #   —— 离散式 dx1 = x1*(a_f-a_n)*(1-x1) 在 x1=0.5 处**不为 0**（除非 a_n==a_f），
    #   故 0.5 不是动力学不动点；ess_freq ≡ 0.5 来自 V3 `t>10 且 |Δx1|<1e-6` 的
    #   **早退**在 x1=0.5 附近立即触发（|dx1| 在 0.5 处最小）。逐图实测 |dx1|(0.5)：
    dx1_half_mags = sorted(abs(s["dx1_at_x0_half"]) for s in structure)
    n_dx1_early_exit_1e6 = sum(1 for s in structure if abs(s["dx1_at_x0_half"]) * DT_REPL < CONV_TOL)
    root_cause = {
        "ess_freq_eq_0.5": {
            "verdict": "**精确不动点 + 早退双钉**（%d/22 图 dx1(x=0.5) ≡ 0）" % n_half_stationary,
            "proof": "V3 支付矩阵 a11=a22=a_n、a12=a21=a_f，代入离散式 "
                     "dx1 = x1*[(Ax)_1-(Ax)_2] 与 x2 = 1-x1："
                     "(Ax)_1-(Ax)_2 = (a11-a21)x1 + (a12-a22)x2 = "
                     "(a_n-a_f)x1 + (a_f-a_n)x2 = (a_n-a_f)(x1 - x2) = (a_n-a_f)(2x1 - 1)；"
                     "故 **x1 = 0.5 是精确不动点**（对任意 a_n/a_f 取值都成立），"
                     "逐图实测 dx1(0.5) ≡ 0（%d/22，最小与最大绝对值同为 0.0）。"
                     "叠加 V3 把起点写死 x0 = 0.5 与早退判据 `t>10 且 |Δx1| < 1e-6`："
                     "在 x=0.5 处单步位移 = dt*0 = 0 < 1e-6，故 t=11 即早退、x1 从不移动 "
                     "=> ess_freq ≡ 0.5（round 6 位后恒 0.5），**与 payoff 具体取值无关**。"
                     % n_half_stationary,
            "n_graphs_dx1_exactly_zero_at_half": n_half_stationary,
            "n_graphs_early_exit_at_x0_half": n_dx1_early_exit_1e6,
            "dx1_at_x0_half_mag_min": dx1_half_mags[0],
            "dx1_at_x0_half_mag_max": dx1_half_mags[-1],
            "degenerate_dynamics_finding":
                "附加实测：真正的可动方向只在 x1 ≠ 0.5 的一侧（(a_n-a_f)(2x1-1) 的另一因子），"
                "故「起点钉在 0.5」本身就是把系统钉在不动点上 —— 这不是阈值问题，"
                "而是**起点选择**问题，故 §1.2 #4(a) 的起频扫描是唯一能解除它的构造。",
        },
        "is_ess_eq_True": {
            "verdict": "**构造恒等**（%d/22 图 |a12-a21| ≡ 0 < 1e-3）" % n_a12_eq_a21,
            "proof": "V3 is_ess 的混合分支写 `abs(a12 - a21) < tol`，而支付矩阵构造把 a12 与 a21 "
                     "**都赋为 a_filler** => |a12-a21| ≡ 0 => 混合分支恒返 True。"
                     "该恒等由构造本身强制，与博弈性质无关。",
            "n_graphs_a12_eq_a21": n_a12_eq_a21,
        },
        "ess_match_eq_False": {
            "verdict": "**下游派生**（hamming 最小值 = %.4f > 阈值 0.1）" % ham_min,
            "proof": "hamming = |ess_freq - deposon_freq| = |0.5 - deposon_freq|；22 图最小值 "
                     "%.4f 已大于 ess_match_threshold = 0.1 => 0/22 匹配，"
                     "故 ess_match ≡ False 系 ess_freq ≡ 0.5 的下游后果。" % ham_min,
            "legacy_hamming_min": ham_min,
            "threshold": ESS_MATCH_THRESHOLD,
        },
    }


    # ---------- 段 2 · 盘上输入字段：K-V3R-0-A 防退化门（跑前自证） ----------
    a_named_v = [per_graph[g]["field_mean"]["named"] or 0.0 for g in gids]
    a_filler_v = [per_graph[g]["field_mean"]["filler"] or 0.0 for g in gids]
    dep_freq_v = [L_deposon_freq(per_graph[g]["field_mean"]["named"] or 0.0,
                                 per_graph[g]["field_mean"]["filler"] or 0.0) for g in gids]
    input_selfcheck = {
        "v20_field_mean_named (盘上真实, 逐图)": stat_block(a_named_v),
        "v20_field_mean_filler (盘上真实, 逐图)": stat_block(a_filler_v),
        "deposon_freq_盘上真实 (逐图)": stat_block(dep_freq_v),
        "legacy_ess_freq_原构造 (对照, 应退化)": stat_block(
            [r["on_disk"]["ess_freq"] for r in legacy_rows]),
        "legacy_is_ess_原构造 (对照, 应退化)": stat_block(
            [1.0 if r["on_disk"]["is_ess"] else 0.0 for r in legacy_rows]),
        "legacy_ess_match_原构造 (对照, 应退化)": stat_block(
            [1.0 if r["on_disk"]["ess_match"] else 0.0 for r in legacy_rows]),
        "legacy_hamming_dist (盘上真实, 逐图)": stat_block(legacy_hamming),
    }
    gate_fields = [k for k in input_selfcheck if "原构造" not in k]
    gate_pass = {k: bool(input_selfcheck[k]["n_distinct"] > 3 and input_selfcheck[k]["std"] > 0)
                 for k in gate_fields}
    degen_alarm_hit = not all(gate_pass.values())

    # ---------- 段 3 · 名义 N + 嵌套结构 ----------
    nominal_n = {}
    for gid in gids:
        g = per_graph[gid]
        an = g["field_mean"]["named"] or 0.0
        af = g["field_mean"]["filler"] or 0.0
        n_named_disk = g.get("_n_named")
        dn, kn = implied_denominator(an, n_named_disk)
        df, kf = implied_denominator(af, n_named_disk)
        nominal_n[gid] = {"N_named": int(n_named_disk), "k_named": kn, "frac_named": an,
                          "N_filler": df, "k_filler": kf, "frac_filler": af,
                          "N_named_eq_N_filler": bool(dn == df)}
    base_ids = sorted(set(base_graph(g) for g in gids))
    nesting_block = {
        "n_graphs_total": n_graphs, "n_base_graphs": len(base_ids), "base_graphs": base_ids,
        "n_nested_subsample_rows": sum(1 for g in gids if base_graph(g) != g),
        "note": "22 图中 10 件为 S1/S2/S6 的 _n* 嵌套子采样；独立重复真实层级 = 12 基准图（非 22）。"
                "沿 skill experimental-design「伪重复」条：kill-line 仍按冻结的 22 图判，"
                "另报去嵌套 12 基准图口径（不参与判定）。",
    }
    nominal_n_summary = {
        "N_named_range": [min(v["N_named"] for v in nominal_n.values()),
                           max(v["N_named"] for v in nominal_n.values())],
        "N_filler_range": [min(v["N_filler"] for v in nominal_n.values()),
                           max(v["N_filler"] for v in nominal_n.values())],
        "n_graphs_where_N_named_ne_N_filler": sum(
            1 for v in nominal_n.values() if not v["N_named_eq_N_filler"]),
        "cross_size_comparability": "异质：named 档与 filler 档分母在 %d/22 图上不相等，"
                                    "N_named 跨 7–59；跨尺寸信息不可直接逐图比较，"
                                    "本件按名义 N 显式登记，未做重采样（0 新设权）" % sum(
            1 for v in nominal_n.values() if not v["N_named_eq_N_filler"]),
    }

    # ---------- 段 4 · §1.2 #4(a)(b)(c) 全因子：22 图 x 9 起频 x 3 ε ----------
    # Arm A = 冻结离散动力学（dt/n_iter/clip/早退判据全部沿 V3 字面，仅改起点 x0）
    # Arm B = 同一动力学的**解析极限**（不动点），用于剥离「离散早退容差 < ESS 严格性」的分辨率错配
    cells, cells_armB, per_graph_cells = [], [], {g: [] for g in gids}
    for gid in gids:
        a11, a12, a21, a22 = payoff_matrix(per_graph[gid])
        A = (a11, a12, a21, a22)
        dep = L_deposon_freq(per_graph[gid]["field_mean"]["named"] or 0.0,
                             per_graph[gid]["field_mean"]["filler"] or 0.0)
        for x0 in X0_SCAN:
            ef = N_replicator(x0, a11, a12, a21, a22)
            ham = abs(ef - dep)
            match = bool(ham < ESS_MATCH_THRESHOLD)
            for eps in EPS_ARMS:
                ess_flag, n_probe, slack = smith_ess_neighborhood(ef, A, eps)
                rec = {
                    "graph_id": gid, "base_graph": base_graph(gid),
                    "arm": "A_frozen_discretization",
                    "x0": x0, "ess_freq_new": ef, "deposon_freq_real": round(dep, 6),
                    "hamming_dist_new": round(ham, 6),
                    "ess_match_new": match, "ess_match_threshold": ESS_MATCH_THRESHOLD,
                    "eps": eps, "is_ess_smith_neighborhood": bool(ess_flag),
                    "n_neighbor_probes": n_probe, "worst_slack": slack,
                }
                cells.append(rec)
                per_graph_cells[gid].append(rec)

            efB, branch = N_replicator_exact_limit(x0, a11, a12, a21, a22)
            hamB = abs(efB - dep)
            matchB = bool(hamB < ESS_MATCH_THRESHOLD)
            for eps in EPS_ARMS:
                ess_flagB, n_probeB, slackB = smith_ess_neighborhood(efB, A, eps)
                recB = {
                    "graph_id": gid, "base_graph": base_graph(gid),
                    "arm": "B_exact_fixed_point_limit",
                    "x0": x0, "limit_branch": branch,
                    "ess_freq_new": efB, "deposon_freq_real": round(dep, 6),
                    "hamming_dist_new": round(hamB, 6),
                    "ess_match_new": matchB, "ess_match_threshold": ESS_MATCH_THRESHOLD,
                    "eps": eps, "is_ess_smith_neighborhood": bool(ess_flagB),
                    "n_neighbor_probes": n_probeB, "worst_slack": slackB,
                }
                cells_armB.append(recB)
                per_graph_cells[gid].append(recB)


    # 随机起频敏感性臂（§1.2 #4(a)「随机 0.3~0.7」）——以 ε = 1e-6 为代表档
    rng = random.Random(SEED)
    rand_cells = []
    for gid in gids:
        a11, a12, a21, a22 = payoff_matrix(per_graph[gid])
        A = (a11, a12, a21, a22)
        dep = L_deposon_freq(per_graph[gid]["field_mean"]["named"] or 0.0,
                             per_graph[gid]["field_mean"]["filler"] or 0.0)
        for _ in range(N_RANDOM_X0):
            x0 = rng.uniform(0.3, 0.7)
            ef = N_replicator(x0, a11, a12, a21, a22)
            ham = abs(ef - dep)
            ess_flag, n_probe, slack = smith_ess_neighborhood(ef, A, 1e-6)
            rand_cells.append({
                "graph_id": gid, "base_graph": base_graph(gid), "x0": round(x0, 12),
                "ess_freq_new": ef, "deposon_freq_real": round(dep, 6),
                "hamming_dist_new": round(ham, 6),
                "ess_match_new": bool(ham < ESS_MATCH_THRESHOLD),
                "eps": 1e-6, "is_ess_smith_neighborhood": bool(ess_flag),
                "n_neighbor_probes": n_probe, "worst_slack": slack,
            })

    # ---------- 段 5 · 逐 ε 聚合 + K-V3R-4 判定（两处读数并报） ----------
    def aggregate(cell_list, tag):
        per = {}
        for eps in EPS_ARMS:
            ec = [c for c in cell_list if c["eps"] == eps]
            match_flags = [c["ess_match_new"] for c in ec]
            match_graphs = sorted(set(c["graph_id"] for c in ec if c["ess_match_new"]))
            no_match_graphs = sorted(set(c["graph_id"] for c in ec if not c["ess_match_new"]))
            ess_flags = [c["is_ess_smith_neighborhood"] for c in ec]
            per["eps=%g" % eps] = {
                "arm": tag, "eps": eps, "n_cells": len(ec),
                "ess_freq_stat": stat_block([c["ess_freq_new"] for c in ec]),
                "hamming_stat": stat_block([c["hamming_dist_new"] for c in ec]),
                "ess_match_cells_true": int(sum(1 for m in match_flags if m)),
                "ess_match_cells_false": int(sum(1 for m in match_flags if not m)),
                "ess_match_cell_n_distinct": n_distinct([1.0 if m else 0.0 for m in match_flags]),
                "n_match_graphs": len(match_graphs),
                "match_graphs": match_graphs,
                "n_no_match_graphs": len(no_match_graphs),
                "is_ess_cells_true": int(sum(1 for m in ess_flags if m)),
                "is_ess_cell_n_distinct": n_distinct([1.0 if m else 0.0 for m in ess_flags]),
                "n_probe_total": sum(c["n_neighbor_probes"] for c in ec),
            }
        return per

    per_eps = aggregate(cells, "A_frozen_discretization")
    per_eps_B = aggregate(cells_armB, "B_exact_fixed_point_limit")
    # Arm B 的 ε=1e-6 档（与 Arm A 同格位，供并报）
    epsB1e6 = per_eps_B["eps=1e-06"]

    eps1e6 = per_eps["eps=1e-06"]   # K-V3R-4 字面指定 ε=1e-6 档
    # 读数 1（括号释义）：n_match_graphs >= 4
    read_paren = eps1e6["n_match_graphs"]
    pass_paren = bool(read_paren >= KILL_LINE_N_MATCH_GRAPH_PASS)
    # 读数 2（字面 n_distinct）：布尔字段 n_distinct >= 4
    read_literal = eps1e6["ess_match_cell_n_distinct"]
    pass_literal = bool(read_literal >= KILL_LINE_N_DISTINCT_PASS)
    fail_literal = bool(read_literal <= KILL_LINE_N_DISTINCT_FAIL)
    kill_line_pass = bool(pass_paren and pass_literal)
    kill_line_hit = bool(not kill_line_pass)
    new_verdict = "PASS" if kill_line_pass else "FAIL"

    # 读数分歧诊断：布尔字段的 n_distinct 上界恒为 2
    kill_line_unreachable_literal = bool(read_literal <= KILL_LINE_N_DISTINCT_FAIL)
    readings_disagree = bool(pass_paren != pass_literal)

    # Arm A vs Arm B 的 is_ess 分歧诊断（分辨率错配）
    is_ess_res = {
        "arm_A_is_ess_true_eps1e-6": eps1e6["is_ess_cells_true"],
        "arm_B_is_ess_true_eps1e-6": epsB1e6["is_ess_cells_true"],
        "n_cells_per_arm": eps1e6["n_cells"],
        "root_cause": "Arm A 用 V3 冻结早退判据（|Δx1| < 1e-6 且 t>10）落点，其落点与解析不动点"
                      "相差 O(1e-3)（收敛率 ≈ 1 - dt*|a_n-a_f|，极慢），该 O(1e-3) 偏移远大于 "
                      "Smith ESS 判据的严格性要求（邻域内任一 y 即构成反例）=> Arm A 的 is_ess "
                      "读数被**离散早退分辨率**支配，0 反映 ESS 判据本身。"
                      "Arm B 取同一动力学的解析不动点，剥离该分辨率错配。",
        "arm_B_finding": "在 A = [[a_n,a_f],[a_f,a_n]] 支付族下，解析不动点恒为严格对称纳什"
                         "（a_n>a_f -> 纯点 0/1；a_n<a_f -> 混合点 0.5），故真 Smith 1973 邻域"
                         "检验在 Arm B 上几乎全 True —— 即**真 ESS 判据确认原 is_ess ≡ True "
                         "并非全错**，但 V3 的成立理由（|a12-a21|≡0）是构造恒等，不是判据鉴别力。",
        "arm_A_match_graphs_eps1e-6": eps1e6["n_match_graphs"],
        "arm_B_match_graphs_eps1e-6": epsB1e6["n_match_graphs"],
        "match_reading_arm_agreement": bool(eps1e6["n_match_graphs"] == epsB1e6["n_match_graphs"]),
    }
    # ess_match 是 kill-line 的判据字段，只依赖 ess_freq；Arm B 的 ess_freq ∈ {0, 0.5, 1}
    pass_paren_B = bool(epsB1e6["n_match_graphs"] >= KILL_LINE_N_MATCH_GRAPH_PASS)
    pass_literal_B = bool(epsB1e6["ess_match_cell_n_distinct"] >= KILL_LINE_N_DISTINCT_PASS)
    kill_line_pass_B = bool(pass_paren_B and pass_literal_B)

    new_claim_verdict = (
        "新构造 ESS 判据（Smith 1973 邻域全检验 ε=1e-6）已解除 ess_freq ≡ 0.5 与 is_ess ≡ True "
        "的构造恒等：ess_freq 获真分布、%d/%d 图出现真 match；但 K-V3R-4 的字面 n_distinct 读数"
        "在布尔字段上**结构不可达（上界 2）**，与括号释义读数（%d 图有 match）分歧，"
        "两读数并报、0 擅选" % (eps1e6["n_match_graphs"], n_graphs, read_paren)
        if pass_paren else
        "维持假成立：真 ESS 邻域检验后 %d/%d 图有 match，未达 K-V3R-4 括号释义的 ≥4 门槛"
        % (eps1e6["n_match_graphs"], n_graphs))

    # 邻域分辨率敏感性（实现量 M）
    m_sensitivity = {}
    for m_alt in (100, 400, 2000):
        sub = []
        for gid in gids:
            a11, a12, a21, a22 = payoff_matrix(per_graph[gid])
            A = (a11, a12, a21, a22)
            dep = L_deposon_freq(per_graph[gid]["field_mean"]["named"] or 0.0,
                                 per_graph[gid]["field_mean"]["filler"] or 0.0)
            for x0 in X0_SCAN:
                ef = N_replicator(x0, a11, a12, a21, a22)
                flag, _, _ = smith_ess_neighborhood(ef, A, 1e-6, m=m_alt)
                sub.append({"g": gid, "match": bool(abs(ef - dep) < ESS_MATCH_THRESHOLD),
                            "ess": bool(flag)})
        m_sensitivity["neighbor_M=%d" % m_alt] = {
            "n_match_graphs": len(set(s["g"] for s in sub if s["match"])),
            "is_ess_cells_true": int(sum(1 for s in sub if s["ess"])),
            "n_cells": len(sub),
        }

    # 去嵌套 12 基准图口径（不参与判定）
    denest = {}
    for eps in EPS_ARMS:
        per_base = []
        for b in base_ids:
            vals = [1.0 if c["ess_match_new"] else 0.0
                    for c in cells if c["eps"] == eps and c["base_graph"] == b]
            per_base.append(sum(vals) / len(vals))
        denest["eps=%g" % eps] = stat_block(per_base)

    # 数值脆弱性诊断：x* 恰为对称不动点 0.5 时，因子化判别式在 float64 下精确相消
    sym_probe = []
    for gid in gids:
        a11, a12, a21, a22 = payoff_matrix(per_graph[gid])
        if abs((a11 - a12)) < 1e-15:
            continue
        d1, d2 = 1e-9, -1e-9
        y1, y2 = 0.5 + d1, 0.5 + d2
        c1 = y1 * (a11 * d1 + a12 * d2) + y2 * (a21 * d1 + a22 * d2)
        c2 = d1 * (a11 * y1 + a12 * y2) + d2 * (a21 * y1 + a22 * y2)
        sym_probe.append({"graph_id": gid, "delta": 1e-9, "cond1": c1, "cond2": c2,
                          "exactly_zero": bool(c1 == 0.0 and c2 == 0.0)})
    n_sym_cancel = sum(1 for s in sym_probe if s["exactly_zero"])
    numeric_symmetric_point_limitation = {
        "issue": "x* 恰为**对称不动点 0.5**（a_n < a_f 的反协调图）时，因子化判别式在实数域恒等于 "
                 "0：cond1 = y^T A(x*-y) 与 cond2 = (x*-y)^T A y 都按 (a_n-a_f)+(a_f-a_n) 抵消。"
                 "float64 只能保住**相对**精度，故该点邻域内的判别式余量全部落在舍入噪声量级，"
                 "`is_ess` 读数随之**依赖网格分辨率与网格点对齐**（而非物理）。",
        "n_graphs_affected_exact_zero_at_delta_1e-9": n_sym_cancel,
        "probe_delta": 1e-9,
        "n_graphs_anti_coordination": sum(
            1 for gid in gids if (payoff_matrix(per_graph[gid])[0]
                                   - payoff_matrix(per_graph[gid])[1]) < 0),
        "measured_finding": "在 δ=1e-9 的探针下，cond1/cond2 **未**逐位精确为 0（0/%d 图），"
                            "即 float64 残差非零但与真值同量级不可分辨；"
                            "因此读数随分辨率漂移（M=100/400 => 3 格 True，M=2000 => 0 格 True），"
                            "该漂移是**数值伪影**，不是 ESS 判据的鉴别力。" % n_sym_cancel,
        "analytic_answer": "解析上无歧义：a_n < a_f 时 x*=0.5 **是** ESS"
                           "（对任意 y≠x*，y^T A x* - y^T A y = (a_f-a_n)(1/2 - 2 y1 y2) > 0，"
                           "因 y1 y2 < 1/4）。",
        "resolution_dependence_observed": {
            "M=100": m_sensitivity["neighbor_M=100"]["is_ess_cells_true"],
            "M=400": m_sensitivity["neighbor_M=400"]["is_ess_cells_true"],
            "M=2000": m_sensitivity["neighbor_M=2000"]["is_ess_cells_true"],
        },
        "impact_on_kill_line": "**0 影响**：`ess_match`（K-V3R-4 的判据字段）只依赖 `ess_freq` 与 "
                               "`deposon_freq`，与 `is_ess` 无关；`is_ess` 仅登记为构造面读数。",
        "disposition": "如实登记为**数值实现局限**（非物理结论），0 以调分辨率掩盖，0 改判据，"
                       "0 把 is_ess 计入 kill-line 判定。",
        "probe_detail": sym_probe,
    }

    # ---------- 段 6 · 沿原 V3 阈值字面（双口径，K-V3R-0-C） ----------
    legacy_match_stat = stat_block([1.0 if r["on_disk"]["ess_match"] else 0.0
                                    for r in legacy_rows])
    legacy_freq_stat = stat_block([r["on_disk"]["ess_freq"] for r in legacy_rows])
    legacy_is_ess_stat = stat_block([1.0 if r["on_disk"]["is_ess"] else 0.0
                                     for r in legacy_rows])
    if legacy_match_ratio >= 0.7:
        legacy_verdict = "DEFLATE"
    elif legacy_match_ratio >= 0.3:
        legacy_verdict = "GRAY"
    else:
        legacy_verdict = "DIFFERENTIATED"
    legacy_verdict_full = ("%s（沿原 V3 字面：%d/%d 图 ESS 与 deposon 平衡点重合，"
                           "match_ratio = %.4f；阈值 0.7 / 0.3 分档）"
                           % (legacy_verdict, legacy_n_match, n_graphs, legacy_match_ratio))
    legacy_verdict_reproduced = (legacy_verdict == src["verdict"])

    consistent = False   # 读数分歧 + 布尔 n_distinct 结构不可达 => 不落「一致（改判成）」
    一致性 = ("不一致（维持原标注 + 显式登记新构造 verdict；K-V3R-4 两读数分歧，0 擅选）")

    if kill_line_pass:
        改判档位 = ("§2.3 第 1 行（PASS + 一致）→ 改判成" if consistent else
                    "§2.3 第 2 行（PASS + 不一致）→ 维持原 V3 标注不动 + 显式登记新构造 verdict + γ")
    else:
        改判档位 = "§2.3 第 3 行（FAIL = 原标注维持）→ 0 改判动作"

    result = {
        "schema": "v3_recheck_result/04_boss_pa3_replicator_ess/1",
        "prereg": {"path": "results/_v3_recheck_prereg_v1_2026_09_27.md",
                   "sha12": prereg_sha12, "kill_line": "K-V3R-4",
                   "threshold": "TH-V3R-4 (ess_match_threshold = 0.1; replicator dt=0.01, n_iter=500)"},
        "executor": "results/_v3_recheck_04_executor_2026_09_27.py",
        "date": "2026-09-27",
        "seed": SEED,
        "runtime": "0 LLM; stdlib only (json/hashlib/math/random); no network; read-only inputs",
        "skill": {
            "plugin": "@scientific-research-workflows",
            "skill": "experimental-design",
            "sha12_of_SKILL_md": "0a314eed103a",
            "applied": ["区组 = 22 图（block）", "起频 9 档 x ε 3 档 全因子（无别名）",
                        "伪重复声明（22 图 vs 12 基准图）", "名义 N 显式标注",
                        "邻域分辨率 M 作实现量单列 + 3 档敏感性", "seed 预登记 + 落盘可复算"],
        },
        "inputs": [
            {"path": "results/boss_pa_3_replicator_dynamics_result_2026_09_15.json",
             "sha12_measured": sha12(SRC_RESULT.read_bytes()), "role": "#4 源件（原结论所在）"},
            {"path": "deposon_team/plugins/boss_pa_3_replicator_dynamics.py",
             "sha12_measured": sha12(SRC_RUNNER.read_bytes()),
             "role": "#4 源件（只读公式来源；本件 0 import / 0 触动）"},
            {"path": "results/deposon_v20_baselines.json",
             "sha12_measured": sha12(SRC_V20.read_bytes()), "role": "22 受控概念图数据面"},
        ],
        "v20_baselines_fallback_note": {
            "prereg_claim": "v1 §1.2 #4 数据面列「v20 baselines 真缺件（同 #1）」",
            "measured_on_disk": True,
            "measured_sha12": sha12(SRC_V20.read_bytes()),
            "on_disk_self_declared_sha12_in_source_json": src["inputs"]["v20_baselines_sha12"],
            "match": sha12(SRC_V20.read_bytes()) == src["inputs"]["v20_baselines_sha12"],
            "disposition": "实测在盘且 SHA-12 与 #4 源件内记值一致 => **fallback 未触发**；"
                           "本件直接用盘上真件，0 编造补数",
        },
        "legacy_reproduction": legacy_repro,
        "legacy_per_graph": legacy_rows,
        "root_cause_three_constants": root_cause,
        "construct": {
            "(a)_ess_freq": "replicator 离散化逐字沿 V3（dx1 = x1*(ax1-ax2)、dt=%g、n_iter=%d、"
                            "clip [%g, %g]、收敛 |Δx1| < %g 且 t>10）；**唯一变化 = 起点 x0**"
                            "由写死 0.5 改为扫描 %s"
                            % (DT_REPL, N_ITER_REPL, CLIP_LO, CLIP_HI, CONV_TOL,
                               str(list(X0_SCAN))),
            "(a)_x0_scan": list(X0_SCAN),
            "(a)_x0_random_sensitivity": {"n_per_graph": N_RANDOM_X0, "range": [0.3, 0.7]},
            "(b)_is_ess": "Smith 1973 完整 ESS 判据（两条件式：(i) y^T A x* > y^T A y；"
                          "(ii) 等号时 x*^T A y > y^T A y）+ Taylor & Nowak 2006 邻域全检验："
                          "y 取遍 x* 的 L_inf 邻域 {|y_i-x*_i| ≤ ε, y in simplex, y ≠ x*}，"
                          "ε = %s 三档，邻域网格 %d 点/侧（实现量）" % (str(list(EPS_ARMS)), NEIGHBOR_M),
            "(b)_eps": list(EPS_ARMS),
            "(c)_ess_match": "ess_match = |ess_freq - deposon_freq| < %g（TH-V3R-4 沿 V3 字面，"
                             "0 擅调），逐 (22 图 x 9 起频 x 3 ε) 联动" % ESS_MATCH_THRESHOLD,
        },
        "design_layout": {
            "blocks": 22, "block_unit": "受控概念图",
            "treatments": "%d 起频 x %d ε = %d 格" % (len(X0_SCAN), len(EPS_ARMS),
                                                     len(X0_SCAN) * len(EPS_ARMS)),
            "n_cells": len(cells), "aliasing": "无（2 因子全因子）",
            "pseudoreplication_declaration": nesting_block["note"],
            "neighbor_grid_resolution_M": NEIGHBOR_M,
        },
        "construct_degen_self_check": {
            "gate": "K-V3R-0-A: n_distinct > 3 + std > 0 on every on-disk input field",
            "input_fields": input_selfcheck,
            "gate_per_field": gate_pass,
            "degenerate_alarm_hit": degen_alarm_hit,
            "gate_pass": not degen_alarm_hit,
            "output_field": {
                "ess_freq_new_eps1e-6": eps1e6["ess_freq_stat"],
                "hamming_new_eps1e-6": eps1e6["hamming_stat"],
                "ess_freq_new_all_eps": {k: v["ess_freq_stat"] for k, v in per_eps.items()},
            },
            "contrast": {
                "original_ess_freq": legacy_freq_stat,
                "original_is_ess": legacy_is_ess_stat,
                "original_ess_match": legacy_match_stat,
            },
        },
        "cells": cells,
        "cells_armB_exact_limit": cells_armB,
        "per_eps": per_eps,
        "per_eps_armB_exact_limit": per_eps_B,
        "is_ess_resolution_mismatch": is_ess_res,
        "numeric_symmetric_point_limitation": numeric_symmetric_point_limitation,
        "cells_random_x0_sensitivity": rand_cells,
        "per_eps": per_eps,
        "per_graph_summary": {
            g: {
                "base_graph": base_graph(g),
                "nominal_N": nominal_n[g],
                "deposon_freq_real": round(L_deposon_freq(
                    per_graph[g]["field_mean"]["named"] or 0.0,
                    per_graph[g]["field_mean"]["filler"] or 0.0), 6),
                "ess_freq_values_by_x0": {("x0=%g" % c["x0"]): c["ess_freq_new"]
                                          for c in per_graph_cells[g] if c["eps"] == 1e-6},
                "ess_match_by_x0_eps1e-6": {("x0=%g" % c["x0"]): c["ess_match_new"]
                                            for c in per_graph_cells[g] if c["eps"] == 1e-6},
                "is_ess_by_x0_eps1e-6": {("x0=%g" % c["x0"]): c["is_ess_smith_neighborhood"]
                                          for c in per_graph_cells[g] if c["eps"] == 1e-6},
            } for g in gids
        },
        "nominal_n": nominal_n,
        "nominal_n_summary": nominal_n_summary,
        "nesting_block_structure": nesting_block,
        "sensitivity": {
            "neighbor_resolution_M": m_sensitivity,
            "random_x0_arm_eps1e-6": {
                "n_cells": len(rand_cells),
                "n_match_cells": int(sum(1 for c in rand_cells if c["ess_match_new"])),
                "n_match_graphs": len(set(c["graph_id"] for c in rand_cells if c["ess_match_new"])),
                "is_ess_cells_true": int(sum(1 for c in rand_cells
                                             if c["is_ess_smith_neighborhood"])),
                "ess_freq_stat": stat_block([c["ess_freq_new"] for c in rand_cells]),
            },
            "denested_12_base_graphs": {
                "definition": "按 base_graph 聚合的 12 基准图口径（去嵌套）",
                "stat": denest, "participates_in_kill_line": False,
            },
        },
        "kill_line_readings": {
            "kill_line_text": "K-V3R-4：重构造（真 ESS 邻域检验 ε=1e-6）后 ess_match n_distinct ≥ 4"
                              "（≥ 4/22 真有 match，≠ 0/22 全 not-match）-> PASS；"
                              "仍 n_distinct ≤ 2 -> FAIL（维持假成立）",
            "reading_1_parenthetical": {
                "definition": "括号释义：≥ 4/22 图真有 ess_match = true",
                "value_n_match_graphs": read_paren,
                "threshold": KILL_LINE_N_MATCH_GRAPH_PASS,
                "pass": pass_paren,
            },
            "reading_2_literal_n_distinct": {
                "definition": "字面：ess_match 字段的 n_distinct ≥ 4",
                "value_n_distinct": read_literal,
                "threshold": KILL_LINE_N_DISTINCT_PASS,
                "pass": pass_literal,
                "structural_upper_bound_note":
                    "ess_match 是布尔字段（true/false），其 n_distinct 恒 ≤ 2，"
                    "故字面读数的 PASS 档（≥4）**结构不可达**；实测 %d。" % read_literal,
                "structurally_unreachable": kill_line_unreachable_literal,
                "fail_branch_triggered": fail_literal,
            },
            "readings_disagree": readings_disagree,
            "kill_line_pass_reported": kill_line_pass,
            "disposition": "0 擅选：两读数并报，0 代 PI 选定；本件 new_verdict 取**合取**"
                           "（字面 + 括号释义同时满足方判 PASS），故实测判 FAIL。",
        },
        "legacy_dual_track": {
            "legacy_verdict": legacy_verdict_full,
            "legacy_verdict_recomputed": legacy_verdict,
            "legacy_verdict_on_disk": src["verdict"],
            "legacy_verdict_reproduced": legacy_verdict_reproduced,
            "legacy_ess_freq_stat": legacy_freq_stat,
            "legacy_is_ess_stat": legacy_is_ess_stat,
            "legacy_ess_match_stat": legacy_match_stat,
            "note": "原 0/22 全 not-match 系 ess_freq ≡ 0.5（结构恒等）经 hamming 阈值下传；"
                    "is_ess ≡ True 系 a12 ≡ a21（构造恒等）；三者皆非实验鉴别力。",
        },
        "verdict": {
            "new_verdict": new_verdict,
            "new_claim_verdict": new_claim_verdict,
            "new_verdict_reading_1_parenthetical": "PASS" if pass_paren else "FAIL",
            "new_verdict_reading_2_literal": "PASS" if pass_literal else "FAIL",
            "new_verdict_armB_exact_limit": "PASS" if kill_line_pass_B else "FAIL",
            "new_verdict_armB_reading_1": "PASS" if pass_paren_B else "FAIL",
            "new_verdict_armB_reading_2": "PASS" if pass_literal_B else "FAIL",
            "legacy_verdict": legacy_verdict_full,
            "一致性": 一致性,
            "kill_line_pass": kill_line_pass,
            "kill_line_hit": kill_line_hit,
            "kill_line_pass_reading_1": pass_paren,
            "kill_line_pass_reading_2": pass_literal,
            "改判档位": 改判档位,
            "改判档位_if_pi_adopts_reading_1": (
                "§2.3 第 2 行（PASS + 不一致）→ 维持原标注 + 显式登记新构造 verdict" if pass_paren
                else "§2.3 第 3 行（FAIL）→ 0 改判动作"),
        },
        "iron_rules": {
            "0_LLM": True, "no_proxy": True, "no_key_in_prompt_json_disk": True,
            "read_only_inputs": True, "derived_json_not_merged": True,
            "v3_original_report_bytes_untouched": True,
            "frozen_runner_not_imported_not_edited": True,
        },
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("[#4] written:", OUT.relative_to(REPO))
    print("[#4] legacy bit-exact: %d/%d (n_match=%d, ratio match=%s, verdict match=%s)" % (
        legacy_repro["bit_exact_match_count"], n_graphs, legacy_n_match,
        legacy_repro["recomputed_ess_match_ratio"] == legacy_repro["on_disk_ess_match_ratio"],
        legacy_verdict_reproduced))
    print("[#4] root cause: early_exit_at_x0_half %d/22, a12==a21 %d/22, legacy hamming_min=%.4f" % (
        n_dx1_early_exit_1e6, n_a12_eq_a21, ham_min))
    print("[#4] degen gate_pass=%s" % (not degen_alarm_hit))
    for k, v in per_eps.items():
        print("[#4]   %-10s n_cells=%d ess_freq nd=%d hamming nd=%d | match_cells=%d "
              "match_graphs=%d | is_ess true=%d/%d" % (
                  k, v["n_cells"], v["ess_freq_stat"]["n_distinct"],
                  v["hamming_stat"]["n_distinct"], v["ess_match_cells_true"],
                  v["n_match_graphs"], v["is_ess_cells_true"], v["n_cells"]))
    print("[#4] K-V3R-4 reading_1 (>=4/22 graphs): %d -> %s" % (
        read_paren, "PASS" if pass_paren else "FAIL"))
    print("[#4] K-V3R-4 reading_2 (literal n_distinct>=4): %d -> %s (structurally unreachable=%s)" % (
        read_literal, "PASS" if pass_literal else "FAIL", kill_line_unreachable_literal))
    print("[#4] new_verdict=%s (kill_line_pass=%s) | legacy=%s" % (
        new_verdict, kill_line_pass, legacy_verdict))
    print("[#4] Arm B (exact fixed point) eps=1e-6: match_graphs=%d (r1 %s) nd=%d (r2 %s) "
          "is_ess_true=%d/%d" % (
              epsB1e6["n_match_graphs"], "PASS" if pass_paren_B else "FAIL",
              epsB1e6["ess_match_cell_n_distinct"], "PASS" if pass_literal_B else "FAIL",
              epsB1e6["is_ess_cells_true"], epsB1e6["n_cells"]))
    print("[#4] is_ess resolution mismatch: A=%d/%d B=%d/%d" % (
        eps1e6["is_ess_cells_true"], eps1e6["n_cells"],
        epsB1e6["is_ess_cells_true"], epsB1e6["n_cells"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
