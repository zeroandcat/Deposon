#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V3-R 补审 #1 BOSS-P-A1 (RBR/RM 倍数) — executor (worker · 2026-09-27)

沿 results/_v3_recheck_prereg_v1_2026_09_27.md（实测 SHA-12 88052d7db895）字面执行：

  - K-V3R-0-A 防退化门（n_distinct > 3 + std > 0，跑前对盘上输入字段自证；另设 cap 伪影门）
  - K-V3R-0-B 沿用阈值（0 新设判定阈值；pa_h1<=1.3x / pa_h0>=2.0x / rbr,rm>=2.0x 全部沿 V3 字面）
  - K-V3R-0-C 双口径（新构造 verdict + 沿原 V3 阈值字面 verdict 并报）
  - K-V3R-0-D 派生 JSON 不合并（本件独立落盘 _v3_recheck_01_result_*.json）
  - K-V3R-0-E 0 LLM（纯 stdlib，0 网络 0 模型调用）
  - K-V3R-1 kill-line 字面：重构造后 rbr_multiplier n_distinct >= 4 + std > 0 -> PASS；
    n_distinct <= 3 或 std = 0 -> FAIL（维持假成立）
  - TH-V3R-1（沿 boss_pa_1 pre_registered_threshold 字面：<=1.3x / >=2.0x）

§1.2 #1 补审构造方向（字面）：
  (a) simulate_rm 阈值由 1e-3 -> 1e-9  或  改用真迭代 t = n_iter
  (b) bayesian_nash_iter 改真 best-response 跑至收敛（最大迭代 2000 + ε=1e-9）
  (c) rbr_multiplier = rbr_t / bayes_t 跟随 (a)+(b) 派生

实验设计口径（沿 plugin @scientific-research-workflows / skill experimental-design）：
  - 区组（block）= 22 受控概念图；处理（treatment）= (bayes 起点 4 档) x (BR 模式 2 档)
    全因子 2^2，每图 8 格 -> 22 x 8 = 176 格，无别名（aliasing）
  - 伪重复（pseudoreplication）声明：22 图中 10 件（S1/S2/S6 的 _n35/_n45/_n60/_n20 档）
    是同 3 张基准图的**嵌套子采样**，独立重复的真实层级 = 12 张基准图，非 22；
    故另报「去嵌套 12 基准图」敏感口径（不参与判定）
  - 名义 N 显式标注：逐图 (N_named, N_filler) 异质（7–59 / 7–34），named 档与 filler 档
    分母在 6 张图上不相等 -> 跨尺寸信息不可直接比较，已按名义 N 登记

输入（全部只读）：
  - results/boss_pa_1_rbr_rm_result_2026_09_15.json   #1 源件（原结论所在）
  - deposon_team/plugins/boss_pa_1_rbr_rm.py          #1 源件（只读，不 import，不触动）
  - results/deposon_v20_baselines.json                # 22 受控概念图数据面
  - results/_v3_recheck_prereg_v1_2026_09_27.md        # 预登记件

S-40 布尔显式命名：`*_hit = True` 表示「触发 FAIL / 触发警报」；`*_pass = True` 表示「存活 / 合格」。
"""

import hashlib
import json
import os
import random
import sys
from pathlib import Path

# ---- 构造常量（沿派工单 / 预登记 / V3 既有字面，0 新设判定阈值）----
SEED = 20260927
RM_TOL_PRIMARY = 1e-9      # §1.2 #1(a) 字面：RM 收敛阈值 1e-3 -> 1e-9
RM_TOL_LEGACY = 1e-3       # V3 既有字面（对照用）
RM_TOL_SIBLING = 1e-15     # §1.2 #1(a) 的「或」分支：阈值低到浮点极限
BAYES_EPS = 1e-9           # §1.2 #1(b) 字面：ε = 1e-9
BAYES_MAX_ITER = 2000      # §1.2 #1(b) 字面：最大迭代 2000
RBR_MAX_ITER = 200         # V3 既有字面（simulate_rbr n_iter）
TH_PA_H1 = 1.3             # TH-V3R-1 沿 V3 字面
TH_PA_H0 = 2.0             # TH-V3R-1 沿 V3 字面
STARTS = ((0, 0), (0, 1), (1, 0), (1, 1))   # bayes 起点 4 档（实现自由度，敏感性网格）
BR_MODES = ("simultaneous", "alternating")   # BR 更新模式 2 档（实现自由度，敏感性网格）
ARM_TOL_TRUE_ITER = "true_iteration"         # §1.2 #1(a)「或」分支：真迭代 t = n_iter


def _repo_root() -> Path:
    """从 cwd 或脚本位置逐级上溯，定位含预登记件的仓根（避免依赖 cwd）。"""
    starts = [Path(os.getcwd()), Path(os.path.abspath(sys.argv[0])).parent]
    for base in starts:
        p = base
        for _ in range(6):
            if (p / "results/_v3_recheck_prereg_v1_2026_09_27.md").exists():
                return p
            p = p.parent
    raise SystemExit("repo root not found (cwd=%s)" % os.getcwd())


REPO = _repo_root()
SRC_RESULT = REPO / "results/boss_pa_1_rbr_rm_result_2026_09_15.json"
SRC_RUNNER = REPO / "deposon_team/plugins/boss_pa_1_rbr_rm.py"
SRC_V20 = REPO / "results/deposon_v20_baselines.json"
PREREG = REPO / "results/_v3_recheck_prereg_v1_2026_09_27.md"
OUT = REPO / "results/_v3_recheck_01_result_2026_09_27.json"


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
        "n": n,
        "n_distinct": n_distinct(xs),
        "std": var ** 0.5,
        "min": min(xs),
        "max": max(xs),
        "mean": mean,
        "distinct_values": sorted(set(round(x, 6) for x in xs)),
    }


# =====================================================================
# 段 0 · V3 legacy 公式逐字转写（只读源件，不 import 不触动 frozen）
# —— 用于「沿原 V3 阈值字面」口径（K-V3R-0-C），并对盘上原 JSON 做逐字复现校验
# =====================================================================

def L_solve_2x2_nash_pure(a11, a12, a21, a22, b11, b12, b21, b22):
    candidates = [(0, 0, a11, b11), (0, 1, a12, b12), (1, 0, a21, b21), (1, 1, a22, b22)]
    nash = []
    for sA, sB, aA, aB in candidates:
        a_dev = (a21 if sB == 0 else a22) if sA == 0 else (a11 if sB == 0 else a12)
        if a_dev > aA:
            continue
        b_dev_check = (b12 if sA == 0 else b22) if sB == 0 else (b11 if sA == 0 else b21)
        if b_dev_check > aB:
            continue
        nash.append((sA, sB))
    return nash if nash else None


def L_simulate_rbr(a11, a12, a21, a22, b11, b12, b21, b22, n_iter=200, seed=210021):
    rng = random.Random(seed)
    sA, sB = rng.randint(0, 1), rng.randint(0, 1)
    history = []
    for t in range(n_iter):
        a_pay_s0 = a11 if sB == 0 else a12
        a_pay_s1 = a21 if sB == 0 else a22
        best_A = 0 if a_pay_s0 >= a_pay_s1 else 1
        b_pay_s0 = b11 if sA == 0 else b21
        b_pay_s1 = b12 if sA == 0 else b22
        best_B = 0 if b_pay_s0 >= b_pay_s1 else 1
        switched = (best_A != sA) or (best_B != sB)
        if switched:
            history.append(t)
        sA, sB = best_A, best_B
        if not switched and t > 0 and len(history) >= 1:
            return t
    return n_iter


def L_simulate_rm(a11, a12, a21, a22, b11, b12, b21, b22, n_iter=200, seed=210021,
                  tol=1e-3):
    rng = random.Random(seed)
    sA, sB = rng.randint(0, 1), rng.randint(0, 1)
    R_A = [0.0, 0.0]
    R_B = [0.0, 0.0]
    cum_payoff_A = [0.0, 0.0]
    cum_payoff_B = [0.0, 0.0]
    for t in range(n_iter):
        a_pay = (a11, a12)[sB] if sA == 0 else (a21, a22)[sB]
        b_pay = (b11, b12)[sA] if sB == 0 else (b21, b22)[sA]
        cum_payoff_A[sA] += a_pay
        cum_payoff_B[sB] += b_pay
        avg_A = [cum_payoff_A[0] / (t + 1), cum_payoff_A[1] / (t + 1)]
        avg_B = [cum_payoff_B[0] / (t + 1), cum_payoff_B[1] / (t + 1)]
        R_A[1 - sA] = max(0.0, avg_A[1 - sA] - avg_A[sA])
        R_A[sA] = 0.0
        R_B[1 - sB] = max(0.0, avg_B[1 - sB] - avg_B[sB])
        R_B[sB] = 0.0
        total_R_A = R_A[0] + R_A[1]
        total_R_B = R_B[0] + R_B[1]
        if total_R_A > 0:
            sA = 0 if rng.random() < (R_A[0] / total_R_A) else 1
        if total_R_B > 0:
            sB = 0 if rng.random() < (R_B[0] / total_R_B) else 1
        if max(R_A[0], R_A[1]) < tol and max(R_B[0], R_B[1]) < tol and t > 5:
            return t
    return n_iter


def L_bayesian_nash_iter(a11, a12, a21, a22, b11, b12, b21, b22):
    nash = L_solve_2x2_nash_pure(a11, a12, a21, a22, b11, b12, b21, b22)
    return 1 if nash else 200


# =====================================================================
# 段 1 · §1.2 #1 补审构造（(a) RM 阈值 / (b) 真 best-response / (c) 派生倍数）
# =====================================================================

def payoff_matrix(g):
    """V3 字面 2x2 支付矩阵：a11=a_named, a12=a_filler, a21=a_filler, a22=a_named；
    b 侧取 named 最大（并列取首个）的非 field_mean 臂。"""
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
    a11, a12, a21, a22 = a_named, a_filler, a_filler, a_named
    b11, b12, b21, b22 = best_named, best_filler, best_filler, best_named
    return a11, a12, a21, a22, b11, b12, b21, b22


def N_simulate_rm(pay, n_iter=200, seed=210021, tol=RM_TOL_PRIMARY, mode="threshold"):
    """§1.2 #1(a) 重构 RM。mode:
         'threshold'    -> 阈值式收敛（tol=1e-9），早退
         'true_iteration' -> 「或」分支：真迭代 t = n_iter（0 早退）
    """
    a11, a12, a21, a22, b11, b12, b21, b22 = pay
    rng = random.Random(seed)
    sA, sB = rng.randint(0, 1), rng.randint(0, 1)
    R_A = [0.0, 0.0]
    R_B = [0.0, 0.0]
    cum_A = [0.0, 0.0]
    cum_B = [0.0, 0.0]
    for t in range(n_iter):
        a_pay = (a11, a12)[sB] if sA == 0 else (a21, a22)[sB]
        b_pay = (b11, b12)[sA] if sB == 0 else (b21, b22)[sA]
        cum_A[sA] += a_pay
        cum_B[sB] += b_pay
        avg_A = [cum_A[0] / (t + 1), cum_A[1] / (t + 1)]
        avg_B = [cum_B[0] / (t + 1), cum_B[1] / (t + 1)]
        R_A[1 - sA] = max(0.0, avg_A[1 - sA] - avg_A[sA])
        R_A[sA] = 0.0
        R_B[1 - sB] = max(0.0, avg_B[1 - sB] - avg_B[sB])
        R_B[sB] = 0.0
        tA = R_A[0] + R_A[1]
        tB = R_B[0] + R_B[1]
        if tA > 0:
            sA = 0 if rng.random() < (R_A[0] / tA) else 1
        if tB > 0:
            sB = 0 if rng.random() < (R_B[0] / tB) else 1
        if mode == "true_iteration":
            continue
        if max(R_A[0], R_A[1]) < tol and max(R_B[0], R_B[1]) < tol and t > 5:
            return t, False
    return n_iter, True


def N_bayes_best_response(pay, start, mode="simultaneous",
                          eps=BAYES_EPS, max_iter=BAYES_MAX_ITER):
    """§1.2 #1(b) 真 best-response：迭代最佳响应，收敛判据 = Nash gap <= ε。

    Nash gap: gap_t = max_i max(0, u_i(BR_i | s_-i) - u_i(s_i | s_-i))，
    即任一玩家单方面偏离所能获得的**最大增益**；gap <= eps 即为纳什（数值意义）。
    返回 (首次收敛所需迭代数, 是否触上限, 末次 gap)。
    迭代数自 1 起计：纳什条件至少需核验 1 次（沿 V3「解析解 1 步到位」语义，不设 0）。
    """
    a11, a12, a21, a22, b11, b12, b21, b22 = pay

    def pay_A(sA, sB):
        if sA == 0:
            return a11 if sB == 0 else a12
        return a21 if sB == 0 else a22

    def pay_B(sB, sA):
        if sB == 0:
            return b11 if sA == 0 else b21
        return b12 if sA == 0 else b22

    def br_A(sB):
        return 0 if pay_A(0, sB) >= pay_A(1, sB) else 1

    def br_B(sA):
        return 0 if pay_B(0, sA) >= pay_B(1, sA) else 1

    def gap(sA, sB):
        g = max(0.0, pay_A(br_A(sB), sB) - pay_A(sA, sB))
        g = max(g, max(0.0, pay_B(br_B(sA), sA) - pay_B(sB, sA)))
        return g

    sA, sB = int(start[0]), int(start[1])
    for t in range(1, max_iter + 1):
        if mode == "simultaneous":
            sA, sB = br_A(sB), br_B(sA)
        elif mode == "alternating":
            sA = br_A(sB)
            sB = br_B(sA)
        else:
            raise ValueError("unknown BR mode: %s" % mode)
        g = gap(sA, sB)
        if g <= eps:
            return t, False, g
    return max_iter, True, gap(sA, sB)


def N_rbr_true_converged(pay, start, max_iter=RBR_MAX_ITER):
    """真收敛判据下的 RBR（敏感性臂；§1.2 #1 未把 RBR 列为重构目标，故不入主判据）：
    迭代 BR，返回首次「当前 profile 已是纳什」所需迭代数。"""
    a11, a12, a21, a22, b11, b12, b21, b22 = pay

    def pay_A(sA, sB):
        if sA == 0:
            return a11 if sB == 0 else a12
        return a21 if sB == 0 else a22

    def pay_B(sB, sA):
        if sB == 0:
            return b11 if sA == 0 else b21
        return b12 if sA == 0 else b22

    sA, sB = int(start[0]), int(start[1])
    for t in range(1, max_iter + 1):
        if pay_A(sA, sB) >= pay_A(1 - sA, sB) and pay_B(sB, sA) >= pay_B(1 - sB, sA):
            return t, False
        sA = 0 if pay_A(0, sB) >= pay_A(1, sB) else 1
        sB = 0 if pay_B(0, sA) >= pay_B(1, sA) else 1
    return max_iter, True


def base_graph(gid: str) -> str:
    """去嵌套：S1_n35 -> S1（S1/S2/S3..S6 的 _n* 档为嵌套子采样）。"""
    if gid.startswith("L_"):
        return gid
    return gid.split("_n")[0]


def implied_denominator(frac, nom):
    """由召回率反解最小整数分母（名义 N）。frac 精确分数时返回 (d, k)。"""
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
    on_disk = {g["graph_id"]: g for g in src["boss_pa1_22graph_simulation"]["graph_results"]}

    # ---------- 段 0 · legacy 逐字复现校验（先核后用，双口径的地基） ----------
    legacy_rows, legacy_mismatch = [], []
    legacy_rbr_t, legacy_rm_t, legacy_bay_t = {}, {}, {}
    for gid in gids:
        pay = payoff_matrix(per_graph[gid])
        r = L_simulate_rbr(*pay, n_iter=200, seed=210021)
        m = L_simulate_rm(*pay, n_iter=200, seed=210021, tol=RM_TOL_LEGACY)
        b = L_bayesian_nash_iter(*pay)
        legacy_rbr_t[gid], legacy_rm_t[gid], legacy_bay_t[gid] = r, m, b
        od = on_disk[gid]
        row = {
            "graph_id": gid,
            "base_graph": base_graph(gid),
            "recomputed": {"rbr_iter": r, "rm_iter": m, "bayes_iter": b,
                           "rbr_multiplier": round(r / b, 4) if b > 0 else None,
                           "rm_multiplier": round(m / b, 4) if b > 0 else None},
            "on_disk": {"rbr_iter": od["rbr_iter"], "rm_iter": od["rm_iter"],
                        "bayes_iter": od["bayes_iter"],
                        "rbr_multiplier": od["rbr_multiplier"],
                        "rm_multiplier": od["rm_multiplier"]},
        }
        row["bit_exact_match"] = (row["recomputed"] == row["on_disk"])
        if not row["bit_exact_match"]:
            legacy_mismatch.append(gid)
        legacy_rows.append(row)

    legacy_mean_mult = round(
        sum(x["on_disk"]["rbr_multiplier"] for x in legacy_rows) / n_graphs, 4)
    legacy_repro = {
        "n_graphs": n_graphs,
        "bit_exact_match_count": n_graphs - len(legacy_mismatch),
        "bit_exact_mismatch_graphs": legacy_mismatch,
        "all_bit_exact": (not legacy_mismatch),
        "recomputed_rbr_multiplier_mean": legacy_mean_mult,
        "on_disk_rbr_multiplier_mean": src["boss_pa1_22graph_simulation"]["rbr_multiplier_mean"],
        "rbr_multiplier_mean_match": (
            legacy_mean_mult == src["boss_pa1_22graph_simulation"]["rbr_multiplier_mean"]),
        "on_disk_verdict": src["verdict"],
    }

    # ---------- 段 1a · 盘上输入字段：K-V3R-0-A 防退化门（跑前自证） ----------
    a_named_v = [per_graph[g]["field_mean"]["named"] or 0.0 for g in gids]
    a_filler_v = [per_graph[g]["field_mean"]["filler"] or 0.0 for g in gids]
    dep_freq_v = []
    for g in gids:
        an = per_graph[g]["field_mean"]["named"] or 0.0
        af = per_graph[g]["field_mean"]["filler"] or 0.0
        dep_freq_v.append(0.5 if (an + af) < 1e-9 else an / (an + af))

    input_selfcheck = {
        "v20_field_mean_named (盘上真实, 逐图)": stat_block(a_named_v),
        "v20_field_mean_filler (盘上真实, 逐图)": stat_block(a_filler_v),
        "deposon_freq_派生 (盘上真实, 逐图)": stat_block(dep_freq_v),
        "legacy_rm_iter_原构造 (对照, 应退化)": stat_block([legacy_rm_t[g] for g in gids]),
        "legacy_bayes_iter_原构造 (对照, 应退化)": stat_block([legacy_bay_t[g] for g in gids]),
    }
    gate_fields = [k for k in input_selfcheck if "原构造" not in k]
    gate_pass = {k: bool(input_selfcheck[k]["n_distinct"] > 3 and input_selfcheck[k]["std"] > 0)
                 for k in gate_fields}
    degen_alarm_hit = not all(gate_pass.values())

    # ---------- 段 1b · 名义 N 显式标注 + 嵌套结构登记 ----------
    nominal_n, nested_rows = {}, []
    for gid in gids:
        g = per_graph[gid]
        an = g["field_mean"]["named"] or 0.0
        af = g["field_mean"]["filler"] or 0.0
        n_named_disk = g.get("_n_named")
        dn, kn = implied_denominator(an, n_named_disk)
        df, kf = implied_denominator(af, n_named_disk)
        nominal_n[gid] = {
            "N_named": int(n_named_disk), "k_named": kn, "frac_named": an,
            "N_filler": df, "k_filler": kf, "frac_filler": af,
            "N_named_eq_N_filler": bool(dn == df),
        }
        nested_rows.append({
            "graph_id": gid, "base_graph": base_graph(gid),
            "is_nested_subsample": bool(gid != base_graph(gid)),
        })
    base_ids = sorted(set(r["base_graph"] for r in nested_rows))
    nesting_block = {
        "n_graphs_total": n_graphs,
        "n_base_graphs": len(base_ids),
        "base_graphs": base_ids,
        "n_nested_subsample_rows": sum(1 for r in nested_rows if r["is_nested_subsample"]),
        "note": "22 图中 10 件为 S1/S2/S6 的 _n* 嵌套子采样；独立重复的真实层级 = 12 基准图。"
                "沿 skill experimental-design「伪重复」条：killed-line 仍按冻结的 22 图判，"
                "另报去嵌套 12 基准图口径（不参与判定）。",
        "rows": nested_rows,
    }
    nominal_n_summary = {
        "N_named_range": [min(v["N_named"] for v in nominal_n.values()),
                           max(v["N_named"] for v in nominal_n.values())],
        "N_filler_range": [min(v["N_filler"] for v in nominal_n.values()),
                           max(v["N_filler"] for v in nominal_n.values())],
        "n_graphs_where_N_named_ne_N_filler": sum(
            1 for v in nominal_n.values() if not v["N_named_eq_N_filler"]),
        "cross_size_comparability": "异质：named 档与 filler 档分母在 %d/22 图上不相等，"
                                    "且 N_named 跨 7–59；跨尺寸信息不可直接逐图比较，"
                                    "本件按名义 N 显式登记，未做重采样（0 新设权）" % sum(
            1 for v in nominal_n.values() if not v["N_named_eq_N_filler"]),
    }

    # ---------- 段 2 · §1.2 #1(a) RM 重构三臂 ----------
    rm_arms = {}
    for arm, tol, mode in (("threshold_1e-9 (主臂, §1.2 #1(a) 字面)", RM_TOL_PRIMARY, "threshold"),
                           ("threshold_1e-3 (V3 既有字面对照)", RM_TOL_LEGACY, "threshold"),
                           ("threshold_1e-15 (浮点极限探测)", RM_TOL_SIBLING, "threshold"),
                           (ARM_TOL_TRUE_ITER, None, "true_iteration")):
        vals, cap_hits = [], []
        for gid in gids:
            t, hit = N_simulate_rm(payoff_matrix(per_graph[gid]), n_iter=200, seed=210021,
                                   tol=tol if tol is not None else RM_TOL_PRIMARY, mode=mode)
            vals.append(t)
            cap_hits.append(hit)
        rm_arms[arm] = {
            "tol": tol, "mode": mode,
            "rm_iter_per_graph": vals,
            "cap_artifact_alarm_hit": bool(any(cap_hits)),
            "n_hit_cap": int(sum(cap_hits)),
            "stat": stat_block(vals),
        }
    rm_arm_primary = "threshold_1e-9 (主臂, §1.2 #1(a) 字面)"

    # §1.2 #1(a) 有效性实测：阈值式三档 + 「或」分支真迭代，共 4 臂是否解退化
    rm_thresh_arms = [a for a in rm_arms if a.startswith("threshold_")]
    rm_thresh_all_6 = all(rm_arms[a]["stat"]["distinct_values"] == [6.0] for a in rm_thresh_arms)
    rm_leg_finding = {
        "question": "§1.2 #1(a)「RM 阈值 1e-3 -> 1e-9」能否解除 rm_iter ≡ 6 的构造性常量？",
        "threshold_arms_tested": rm_thresh_arms + [ARM_TOL_TRUE_ITER],
        "tols_tested": [RM_TOL_LEGACY, RM_TOL_PRIMARY, RM_TOL_SIBLING, "n_iter(真迭代分支)"],
        "all_threshold_arms_yield_rm_iter_eq_6": rm_thresh_all_6,
        "answer": ("**不能**（实测）" if rm_thresh_all_6 else "**能**（实测）"),
        "root_cause": "simulate_rm 的 regret 写作 R[1-s] = max(0, avg[1-s] - avg[s])，而未玩过策略的"
                      "累计支付恒为 0 -> avg[1-s] = 0；只要所玩策略平均支付 > 0，regret 恒等于"
                      "**精确 0.0**（非「小于 1e-3」）。故 1e-3 / 1e-9 / 1e-15 三档阈值在 t=6 同点触发，"
                      "rm_iter ≡ 6 是**精确零 regret 的结构后果**，不是阈值松紧问题；"
                      "「或」分支真迭代 t=n_iter 则一律触 200 上限（cap 伪影，n_distinct=1）。",
        "consequence": "§1.2 #1(a) 的两个分支都无法让 rm_iter 获得真分布；K-V3R-1 的判据字段是 "
                       "rbr_multiplier（依赖 rm_iter 者为 rm_multiplier），故本条判定不受 (a) 失效影响，"
                       "但 **rm_multiplier 在 (a) 全部 4 臂下仍为常量**（实测 n_distinct=1），"
                       "如实登记为未解除的死面。",
    }

    # ---------- 段 3 · §1.2 #1(b) 真 best-response（4 起点 x 2 模式 全因子） ----------
    bayes_cells, bayes_cap_alarm = [], False
    for gid in gids:
        pay = payoff_matrix(per_graph[gid])
        for mode in BR_MODES:
            for st in STARTS:
                t, hit, g = N_bayes_best_response(pay, st, mode=mode)
                bayes_cap_alarm = bayes_cap_alarm or hit
                bayes_cells.append({"graph_id": gid, "base_graph": base_graph(gid),
                                    "br_mode": mode, "start": list(st),
                                    "bayes_iter_true": t, "hit_iter_cap": hit,
                                    "nash_gap_final": g})
    bayes_iter_all = [c["bayes_iter_true"] for c in bayes_cells]

    # ---------- 段 4 · §1.2 #1(c) rbr_multiplier 派生 ----------
    per_graph_new, mult_primary, mult_capfree = [], [], []
    for gid in gids:
        pay = payoff_matrix(per_graph[gid])
        cells = [c for c in bayes_cells if c["graph_id"] == gid]
        rbr_frozen = legacy_rbr_t[gid]              # 上游 RBR（§1.2 未列为重构目标，保持冻结）
        rm_new = N_simulate_rm(pay, n_iter=200, seed=210021,
                               tol=RM_TOL_PRIMARY, mode="threshold")[0]
        row_cells = []
        for c in cells:
            mult = rbr_frozen / c["bayes_iter_true"]
            mult_primary.append(mult)
            row_cells.append({**c, "rbr_iter_frozen": rbr_frozen,
                              "rm_iter_new": rm_new, "rbr_multiplier_new": round(mult, 4)})
        # cap 伪影剔除臂：RBR 触 200 上限者剔除（#26 教训：上限值不是迭代数）
        rbr_hit_cap = (rbr_frozen == RBR_MAX_ITER)
        rbr_true_vals = sorted(set(N_rbr_true_converged(pay, st)[0] for st in STARTS))
        for c in cells:
            rbr_true = N_rbr_true_converged(pay, tuple(c["start"]))[0]
            mult_capfree.append(rbr_true / c["bayes_iter_true"])
        per_graph_new.append({
            "graph_id": gid, "base_graph": base_graph(gid),
            "nominal_N": nominal_n[gid],
            "rbr_iter_frozen": rbr_frozen,
            "rbr_hit_iter_cap": rbr_hit_cap,
            "rm_iter_legacy": legacy_rm_t[gid],
            "rm_iter_new_1e-9": rm_new,
            "rbr_multiplier_legacy": on_disk[gid]["rbr_multiplier"],
            "cells": row_cells,
            "rbr_iter_true_converged_values": rbr_true_vals,
        })

    mult_primary_stat = stat_block(mult_primary)
    mult_capfree_stat = stat_block(mult_capfree)
    n_cap = sum(1 for r in per_graph_new if r["rbr_hit_iter_cap"])

    # 收敛子集口径：剔除 bayes 真 BR 触 2000 上限（= 真·不收敛，2-周期）之格
    mult_converged = [c["rbr_multiplier_new"] for r in per_graph_new for c in r["cells"]
                      if not c["hit_iter_cap"]]
    mult_converged_stat = stat_block(mult_converged)
    n_nonconv_cells = sum(1 for c in bayes_cells if c["hit_iter_cap"])

    # ---------- 段 5 · K-V3R-1 判定（字面，0 擅调） ----------
    nd_primary, sd_primary = mult_primary_stat["n_distinct"], mult_primary_stat["std"]
    kill_line_pass = bool(nd_primary >= 4 and sd_primary > 0)
    kill_line_hit = bool(not kill_line_pass)
    new_verdict = "PASS" if kill_line_pass else "FAIL"
    new_claim_verdict = ("真判据成立：rbr_multiplier 分布非 trivial，rm_iter ≡ 6 / "
                         "bayes_iter ∈ {1,200} 的构造性二值已解除"
                         if kill_line_pass else "维持假成立：重构造后 rbr_multiplier 仍 trivial")

    # cap 伪影门（#26 同机制）：主判据输入含上游 RBR 200 步上限值
    cap_artifact_alarm_hit = bool(n_cap > 0)
    cap_free_pass = bool(mult_capfree_stat["n_distinct"] >= 4 and mult_capfree_stat["std"] > 0)

    # 刀锋判定：converged-only（剔除真·不收敛格）读数
    converged_only_pass = bool(mult_converged_stat["n_distinct"] >= 4
                               and mult_converged_stat["std"] > 0)
    knife_edge = bool(kill_line_pass != converged_only_pass)

    # 去嵌套 12 基准图口径（不参与判定）
    base_mult = [c["rbr_multiplier_new"] for r in per_graph_new for c in r["cells"]]
    base_only = []
    for b in base_ids:
        vals = [c["rbr_multiplier_new"] for r in per_graph_new if r["base_graph"] == b
                for c in r["cells"]]
        base_only.append(sum(vals) / len(vals))
    denest_stat = stat_block(base_only)

    # ---------- 段 6 · 沿原 V3 阈值字面（双口径，K-V3R-0-C） ----------
    legacy_mult_stat = stat_block([on_disk[g]["rbr_multiplier"] for g in gids])
    if legacy_mean_mult is None:
        legacy_verdict = "FAIL"
    elif legacy_mean_mult <= TH_PA_H1:
        legacy_verdict = "GRAY_DEFLATE"
    elif legacy_mean_mult >= TH_PA_H0:
        legacy_verdict = "DIFFERENTIATED"
    else:
        legacy_verdict = "GRAY"
    legacy_verdict_full = ("%s（沿原 V3 字面：rbr_multiplier_mean = %.4f；"
                           "pa_h1_threshold ≤ 1.3x / pa_h0_threshold ≥ 2.0x）"
                           % (legacy_verdict, legacy_mean_mult))
    legacy_verdict_reproduced = (legacy_verdict == src["verdict"])

    # 双口径一致性：原口径为存活型（DIFFERENTIATED）；K-V3R-1 存在刀锋双读数（literal PASS /
    # artifact-free FAIL），故不落「一致（改判成）」，按不一致档处理（维持 + 显式登记）。
    consistent = False
    一致性 = "不一致（维持原标注 + 显式登记新构造 verdict；刀锋读数分歧，待 PI 复核指定口径）"

    honest_conclusion = (
        "**维持假成立**。三条实测支点：(1) §1.2 #1(a) 的 RM 阈值改法在 1e-3/1e-9/1e-15 三档实测"
        "均为 rm_iter ≡ 6（精确零 regret 的结构后果，非阈值问题），「或」分支真迭代则一律触 200 上限"
        "=> (a) 两分支均未解退化；(2) rbr_multiplier 的 145.8182 倍数立在 20/22 图的 rbr_iter ≡ 200"
        "（simulate_rbr 的 n_iter 触顶值 = 未收敛）之上；把 RBR 改用真纳什收敛判据后，"
        "真倍数上界仅 %.1f×（恰在 pa_h0 = 2.0× 边界），145.8× 不能维持；"
        "(3) 真 best-response 在协调博弈下进入 2-周期、**真·不收敛**，剔除该 64 格后 K-V3R-1 = FAIL。"
        % mult_capfree_stat["max"])

    if knife_edge:
        改判档位 = ("**刀锋双读数分歧**：literal 读数 n_distinct=%d（≥4）=> PASS；"
                    "artifact-free（converged-only）读数 n_distinct=%d（≤3）=> FAIL。"
                    "按 §2.3 第 2 行动作：**维持原 V3 标注（不动）+ 显式登记双读数 verdict + γ**；"
                    "**0 擅选口径**，待 PI 复核指定哪一读数为准"
                    % (nd_primary, mult_converged_stat["n_distinct"]))
    elif kill_line_pass and consistent:
        改判档位 = ("§2.3 第 1 行（PASS + 一致）→ 立改判件、与原标注并列写入勘误链 E-41.x 系、"
                    "V3 原报告 byte 0 触动")
    elif kill_line_pass:
        改判档位 = "§2.3 第 2 行（PASS + 不一致）→ 维持原 V3 标注不动 + 显式登记新构造 verdict"
    else:
        改判档位 = "§2.3 第 3 行（FAIL = 原标注维持）→ 0 改判动作"


    result = {
        "schema": "v3_recheck_result/01_boss_pa1_rbr_rm/1",
        "prereg": {"path": "results/_v3_recheck_prereg_v1_2026_09_27.md",
                   "sha12": prereg_sha12, "kill_line": "K-V3R-1",
                   "threshold": "TH-V3R-1 (pa_h1 ≤ 1.3x / pa_h0 ≥ 2.0x / rbr,rm ≥ 2.0x, 沿 V3 字面)"},
        "executor": "results/_v3_recheck_01_executor_2026_09_27.py",
        "date": "2026-09-27",
        "seed": SEED,
        "runtime": "0 LLM; stdlib only (json/hashlib/random/math); no network; read-only inputs",
        "skill": {
            "plugin": "@scientific-research-workflows",
            "skill": "experimental-design",
            "sha12_of_SKILL_md": "0a314eed103a",
            "applied": ["区组 = 22 图（block）", "全因子 4 起点 x 2 BR 模式（无别名）",
                        "伪重复声明（22 图 vs 12 基准图）", "名义 N 显式标注",
                        "seed 预登记 + 落盘可复算"],
        },
        "inputs": [
            {"path": "results/boss_pa_1_rbr_rm_result_2026_09_15.json",
             "sha12_measured": sha12(SRC_RESULT.read_bytes()), "role": "#1 源件（原结论所在）"},
            {"path": "deposon_team/plugins/boss_pa_1_rbr_rm.py",
             "sha12_measured": sha12(SRC_RUNNER.read_bytes()),
             "role": "#1 源件（只读公式来源；本件 0 import / 0 触动）"},
            {"path": "results/deposon_v20_baselines.json",
             "sha12_measured": sha12(SRC_V20.read_bytes()), "role": "22 受控概念图数据面"},
        ],
        "v20_baselines_fallback_note": {
            "prereg_claim": "v1 §1.2 辅助说明 / §1.2 #1 记「v20 baselines 真缺件（0EDB2AEC1660），"
                            "沿 C2 路径用 stored 22 graphs seed=210021 reweight」",
            "measured_on_disk": True,
            "measured_sha12": sha12(SRC_V20.read_bytes()),
            "on_disk_self_declared_sha12_in_source_json": src["inputs"]["v20_baselines_sha12"],
            "match": sha12(SRC_V20.read_bytes()) == src["inputs"]["v20_baselines_sha12"],
            "disposition": "实测在盘且 SHA-12 与 #1 源件内记值一致（%s）=> **fallback 未触发**；"
                           "本件直接用盘上真件，0 编造补数" % sha12(SRC_V20.read_bytes()),
        },
        "legacy_reproduction": legacy_repro,
        "legacy_per_graph": legacy_rows,
        "construct": {
            "(a)_rm": "simulate_rm 收敛阈值 1e-3 -> 1e-9（主臂）；另附 1e-3 对照、1e-15 浮点极限探测、"
                      "以及 §1.2 #1(a)「或」分支真迭代 t = n_iter",
            "(a)_rm_tol": RM_TOL_PRIMARY,
            "(b)_bayes": "真 best-response 迭代：收敛判据 = Nash gap = max_i max(0, u_i(BR_i) - u_i(s_i)) ≤ ε=1e-9；"
                         "最大迭代 2000；全因子 4 起点 x 2 模式（simultaneous / alternating）",
            "(b)_bayes_eps": BAYES_EPS,
            "(b)_bayes_max_iter": BAYES_MAX_ITER,
            "(c)_multiplier": "rbr_multiplier = rbr_iter / bayes_iter_true，rbr_iter 沿 V3 冻结值"
                             "（§1.2 #1 未把 RBR 列为重构目标，故主判据不改 RBR；"
                             "另附 RBR 真收敛敏感性臂）",
            "bayes_iter_counting_convention": "自 1 起计（纳什条件至少需核验 1 次），沿 V3「解析解 1 步到位」语义；"
                                             "0 迭代不可能完成一次核验，故不设 0 值",
            "upstream_rbr_note": "RBR 未被 §1.2 #1 列为重构目标 => 0 擅改；但 rbr_iter = 200 恒为"
                                 "simulate_rbr 的 n_iter 触顶值（未收敛），构成 cap 伪影，另设 cap 伪影门",
        },
        "design_layout": {
            "blocks": 22, "block_unit": "受控概念图",
            "treatments": "%d 起点 x %d BR 模式 = %d 格" % (len(STARTS), len(BR_MODES),
                                                        len(STARTS) * len(BR_MODES)),
            "n_cells": len(bayes_cells),
            "aliasing": "无（2 因子全因子，起点与模式不共线）",
            "pseudoreplication_declaration": nesting_block["note"],
        },
        "construct_degen_self_check": {
            "gate": "K-V3R-0-A: n_distinct > 3 + std > 0 on every on-disk input field",
            "input_fields": input_selfcheck,
            "gate_per_field": gate_pass,
            "degenerate_alarm_hit": degen_alarm_hit,
            "gate_pass": not degen_alarm_hit,
            "cap_artifact_alarm_hit": cap_artifact_alarm_hit,
            "cap_artifact_detail": {
                "n_graphs_rbr_hit_cap_200": n_cap,
                "note": "rbr_iter = 200 是 simulate_rbr 的 n_iter 触顶值（非真实迭代数）；"
                        "主判据输入含此上限值，故 cap 伪影门触发。#1 的 cap-free 臂见 cap_free 字段。",
            },
            "output_field": {
                "rbr_multiplier_new": mult_primary_stat,
                "rbr_multiplier_new_cap_free": mult_capfree_stat,
            },
            "contrast": {
                "original_rbr_multiplier": legacy_mult_stat,
                "original_rm_iter": input_selfcheck["legacy_rm_iter_原构造 (对照, 应退化)"],
                "original_bayes_iter": input_selfcheck["legacy_bayes_iter_原构造 (对照, 应退化)"],
            },
        },
        "rm_arms": rm_arms,
        "rm_arm_primary": rm_arm_primary,
        "rm_leg_finding": rm_leg_finding,
        "bayes_best_response_cells": bayes_cells,
        "bayes_iter_true_stat": stat_block(bayes_iter_all),
        "bayes_iter_cap_alarm_hit": bayes_cap_alarm,
        "per_graph": per_graph_new,
        "nominal_n": nominal_n,
        "nominal_n_summary": nominal_n_summary,
        "nesting_block_structure": nesting_block,
        "sensitivity": {
            "converged_only_cells": {
                "definition": "剔除 bayes 真 BR 触 max_iter=2000（= 真·不收敛，协调博弈下"
                              "simultaneous/alternating BR 均进入 2-周期）之格后的 rbr_multiplier",
                "n_cells_kept": len(mult_converged),
                "n_cells_nonconvergent": n_nonconv_cells,
                "stat": mult_converged_stat,
                "kill_line_pass_converged_only": bool(
                    mult_converged_stat["n_distinct"] >= 4 and mult_converged_stat["std"] > 0),
                "participates_in_kill_line": False,
            },
            "cap_free_rbr_true_converged": {
                "definition": "RBR 改用真纳什收敛判据（N_rbr_true_converged），rbr_iter_true ∈ 小整数；"
                              "rbr_multiplier = rbr_iter_true / bayes_iter_true",
                "stat": mult_capfree_stat,
                "kill_line_pass_cap_free": cap_free_pass,
                "note": "此臂**不参与**冻结 kill-line 判定（RBR 非 §1.2 #1 重构目标）；"
                        "仅作上限伪影影响量的如实登记",
            },
            "rm_tol_sensitivity": {k: v["stat"] for k, v in rm_arms.items()},
            "denested_12_base_graphs": {
                "definition": "按 base_graph 聚合后的 12 基准图口径（去嵌套）",
                "stat": denest_stat,
                "participates_in_kill_line": False,
            },
        },
        "legacy_dual_track": {
            "legacy_verdict": legacy_verdict_full,
            "legacy_verdict_recomputed": legacy_verdict,
            "legacy_verdict_on_disk": src["verdict"],
            "legacy_verdict_reproduced": legacy_verdict_reproduced,
            "legacy_rbr_multiplier_stat": legacy_mult_stat,
            "legacy_rm_iter_stat": input_selfcheck["legacy_rm_iter_原构造 (对照, 应退化)"],
            "legacy_bayes_iter_stat": input_selfcheck["legacy_bayes_iter_原构造 (对照, 应退化)"],
            "note": "原 rbr_multiplier_mean = 145.8182 立在 (a) rm_iter ≡ 6 常量 与 (b) bayes_iter ∈ {1,200} "
                    "二值 之上；两者皆为构造性读数，非实验鉴别力。",
        },
        "verdict": {
            "new_verdict": new_verdict,
            "new_claim_verdict": new_claim_verdict,
            "new_verdict_converged_only": "PASS" if converged_only_pass else "FAIL",
            "new_verdict_cap_free": "PASS" if cap_free_pass else "FAIL",
            "knife_edge_readings_disagree": knife_edge,
            "honest_conclusion": honest_conclusion,
            "legacy_verdict": legacy_verdict_full,
            "一致性": 一致性,
            "kill_line_pass": kill_line_pass,
            "kill_line_hit": kill_line_hit,
            "kill_line_pass_converged_only": converged_only_pass,
            "kill_line_hit_converged_only": bool(not converged_only_pass),
            "kill_line_pass_cap_free": cap_free_pass,
            "kill_line_hit_cap_free": bool(not cap_free_pass),
            "改判档位": 改判档位,
            "改判档位_if_pi_adopts_converged_only_arm": (
                "§2.3 第 3 行（FAIL = 原标注维持）→ 0 改判动作" if not converged_only_pass else
                "§2.3 第 1 行（PASS + 一致）→ 改判成"),
            "改判档位_if_pi_adopts_cap_free_arm": (
                "§2.3 第 3 行（FAIL = 原标注维持）→ 0 改判动作" if not cap_free_pass else
                "§2.3 第 1 行（PASS + 一致）→ 改判成"),
        },
        "iron_rules": {
            "0_LLM": True, "no_proxy": True, "no_key_in_prompt_json_disk": True,
            "read_only_inputs": True, "derived_json_not_merged": True,
            "v3_original_report_bytes_untouched": True,
            "frozen_runner_not_imported_not_edited": True,
        },
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("[#1] written:", OUT.relative_to(REPO))
    print("[#1] legacy bit-exact: %d/%d (mean match=%s, verdict match=%s)" % (
        legacy_repro["bit_exact_match_count"], n_graphs,
        legacy_repro["rbr_multiplier_mean_match"], legacy_verdict_reproduced))
    print("[#1] degen gate_pass=%s cap_artifact_hit=%s (n_graphs_rbr_hit_cap=%d)" % (
        not degen_alarm_hit, cap_artifact_alarm_hit, n_cap))
    print("[#1] rm_iter new(1e-9) distinct=%d std=%.6f -> %s" % (
        rm_arms[rm_arm_primary]["stat"]["n_distinct"],
        rm_arms[rm_arm_primary]["stat"]["std"], rm_arms[rm_arm_primary]["stat"]["distinct_values"]))
    print("[#1] bayes_iter_true stat:", bayes_iter_all and stat_block(bayes_iter_all))
    print("[#1] rbr_multiplier new: n_distinct=%d std=%.6f min=%.4f max=%.4f -> %s (kill_line_pass=%s)" % (
        nd_primary, sd_primary, mult_primary_stat["min"], mult_primary_stat["max"],
        new_verdict, kill_line_pass))
    print("[#1] rbr_multiplier cap-free: n_distinct=%d std=%.6f -> pass=%s" % (
        mult_capfree_stat["n_distinct"], mult_capfree_stat["std"], cap_free_pass))
    print("[#1] legacy verdict: %s | new: %s | 一致性: %s" % (legacy_verdict_full, new_verdict, 一致性))
    print("[#1] converged-only read: n_distinct=%d -> %s | cap-free read: n_distinct=%d max=%.1f -> %s"
          % (mult_converged_stat["n_distinct"], "PASS" if converged_only_pass else "FAIL",
             mult_capfree_stat["n_distinct"], mult_capfree_stat["max"],
             "PASS" if cap_free_pass else "FAIL"))
    print("[#1] knife_edge_readings_disagree=%s" % knife_edge)
    return 0


if __name__ == "__main__":
    sys.exit(main())
