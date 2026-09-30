#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V3-R #26 P-J 收敛盆地 — 多本体预实验 executor（worker · 2026-09-27）

性质：**探索性档（预实验，三档强度最低档）** —— 只作本体选择依据；
      0 判定动作 0 verdict，不入 K-V3R-26 判定链；正式判定待择优后另跑
      （K-V3R-26 字面沿 results/_v3_recheck_prereg_v1_2026_09_27.md 锁死不动）。

形式锚（沿 TH-V3R-26 / 第一梯队 executor 字面，0 擅调）：
  convergence_rate_m = mean_j(n_iter_j) / n_budget，j = 1..N_BUDGET
  n_budget = 100；jitter = +-0.05 uniform on T_frac60（clip [0,1]）；seed = 20260927
  扰动抽样顺序 = 第一梯队 executor 同一 rng 流 => O1 基线可逐字复现

本体（5 个 = 派工单建议 4 个 + 增补第 5 个，理由随件登记）：
  O1 discrete_cell_redistribution   离散 cell 重分配（派工单 ① / 第一梯队基线，逐字复用）
  O2 replicator_ode_literal         连续时间 replicator ODE ẋᵢ=xᵢ(fᵢ−f̄)（派工单 ②，字面）
  O3 logit_normal_form              logit 正规形（softmax 响应映射）（派工单 ③）
  O4 imitation_replicator_map       按收益差比例复制（离散 replicator / 模仿）（派工单 ④）
  O5 replicator_ode_softlimit       连续时间 replicator ODE + 软竞争项（增补第 5 本体）

增补第 5 本体的理由（先声明后跑）：plain replicator（O2 字面）与离散 replicator
映射（O4）在本体的**数学结构**上就有已知的坏点（O2 只有边界不动点；O4 内点 NE 处
|g'| = 1 + x*(1−x*)D'/2 ≥ 1，恒扩张）——两者是否可作正式本体取决于「扰动条件能否
成为吸引子」。O5 只加一个标准负频依赖软竞争项 −c·x（c = 0.5 固定，实现常数非判据），
使 O2 的字面形式在内点可稳定收敛，用于分辨「坏点来自数据还是来自结构」。

效果判据（4 条，先冻结后跑，判据面**先于**任何实测写死在本文件字面里）：
  C1 防退化：n_distinct(9 model rates) > 3 且 std(rates) > 0        [沿 K-V3R-0-A 字面]
  C2 真分布非天花板/地板：floor_share(n_iter==0) < 0.50 且
                          draw_n_distinct(900 抽 n_iter) > 3 且
                          rail_share(n_iter ∈ {0, cap}) < 0.50     [「非天花板/地板」操作化]
  C3 收敛合理（无 cap 伪影）：cap_hit_share(n_iter == cap) < 0.20  [派工单字面]
  C4 可复现：重跑逐字不变（进程外双跑比对，本脚本内含二次重算自比）
  「效果好」= C1 ∧ C2 ∧ C3 ∧ C4

诊断（**不作判据**，防 0 擅调阈值：仅登记供择优参考，K-V3R-0-B 沿用阈值不新设）：
  rel_std / iqr（相对离散度，字面 std>0 对近常量不敏感）、target_reached_share
  （真命中扰动目标的比例）、total_steps（算力成本）

输入（全部只读，0 触动）：
  results/_v3_recheck_prereg_v1_2026_09_27.md                                  88052d7db895
  results/_v3_recheck_26_executor_2026_09_27.py                                46c326c756c3
  results/_v3_recheck_26_result_2026_09_27.json                                （基线对照，只读）
  results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json
  results/deposon_v3_physical_opt_60cells_2026_09_11.json

S-40 布尔显式命名：`*_hit = True` = 触发警报/失败；`*_pass = True` = 合格/存活。
"""

import hashlib
import json
import os
import sys
from pathlib import Path

import numpy as np

# ---- 冻结构造常量（沿 TH-V3R-26 / 第一梯队 executor 字面，0 新设判定阈值）----
SEED = 20260927
N_BUDGET = 100
JITTER = 0.05
N_CELLS = 60
CLASSES = ("T", "R", "A")
PRIORITY = "surplus_first"          # 第一梯队 executor 字面（唯一实现自由度）

# ---- 冻结效果判据（先冻结后跑）----
C1_NDISTINCT_MIN = 4                 # 即 n_distinct > 3（沿 K-V3R-0-A 字面）
C2_FLOOR_SHARE_MAX = 0.50           # 「非地板」：n_iter==0 的抽占比须 < 0.50
C2_DRAWN_NDISTINCT_MIN = 4          # 「真分布」：900 抽 n_iter 不得塌成 <=3 档
C2_RAIL_SHARE_MAX = 0.50            # 「非天花板」：贴 0 或贴 cap 的抽占比须 < 0.50
C3_CAP_HIT_SHARE_MAX = 0.20         # 派工单字面：触顶率 < 20%

# ---- 各本体实现常数（实现自由度，非判据；随件登记）----
TOL = 1e-6                          # 连续本体的命中容差（5 本体统一，除 O1 整数精确命中）
O1_MAX_STEP = 60                    # 离散重分配：结构上限（整数三元组守恒 => <=60 必收敛）
O2_DT, O2_CAP = 5e-3, 100000        # 字面 replicator ODE：RK4 步长 / 迭代上限
O3_S, O3_CAP = 0.25, 100000         # logit 正规形：选择强度 s / 迭代上限
O4_CAP = 100000                     # 离散 replicator（模仿）映射：迭代上限
O5_DT, O5_CAP, O5_C = 0.05, 200000, 0.5   # 软竞争 replicator ODE：RK4 步长 / 上限 / 竞争系数 c

ONTOLOGIES = ("O1_discrete_cell_redistribution", "O2_replicator_ode_literal",
              "O3_logit_normal_form", "O4_imitation_replicator_map",
              "O5_replicator_ode_softlimit")


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
PREREG = REPO / "results/_v3_recheck_prereg_v1_2026_09_27.md"
EXEC_BASE = REPO / "results/_v3_recheck_26_executor_2026_09_27.py"
BASE_RESULT = REPO / "results/_v3_recheck_26_result_2026_09_27.json"
SRC_PJ = REPO / "results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json"
SRC_60 = REPO / "results/deposon_v3_physical_opt_60cells_2026_09_11.json"
OUT = REPO / "results/_v3_recheck_26_preexp_data_2026_09_27.json"


def sha12(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:12]


def canon_sha12(obj) -> str:
    return sha12(json.dumps(obj, ensure_ascii=False, sort_keys=True,
                            separators=(",", ":")).encode("utf-8"))


def n_distinct(xs) -> int:
    return len(set(round(float(x), 12) for x in xs))


def stat_block(xs):
    a = np.asarray(xs, dtype=float)
    q1, q3 = (float(v) for v in np.percentile(a, [25, 75]))
    mean = float(a.mean())
    std = float(a.std(ddof=0))
    return {
        "n": int(a.size),
        "n_distinct": n_distinct(a),
        "std": std,
        "rel_std": float(std / mean) if mean != 0.0 else None,
        "min": float(a.min()),
        "max": float(a.max()),
        "mean": mean,
        "median": float(np.median(a)),
        "iqr": q3 - q1,
        "distinct_values": sorted(set(round(float(x), 6) for x in a)),
    }


def spearman(x, y):
    """秩相关（并列取平均秩）。任一侧零方差 -> None（无定义）。"""
    a, b = np.asarray(x, float), np.asarray(y, float)
    if a.std() == 0 or b.std() == 0:
        return None

    def rank(v):
        order = np.argsort(v, kind="mergesort")
        r = np.empty(len(v), float)
        s = v[order]
        i = 0
        while i < len(s):
            j = i
            while j + 1 < len(s) and s[j + 1] == s[i]:
                j += 1
            r[order[i:j + 1]] = (i + j) / 2.0 + 1.0
            i = j + 1
        return r

    ra, rb = rank(a) - rank(a).mean(), rank(b) - rank(b).mean()
    return float((ra * rb).sum() / np.sqrt((ra ** 2).sum() * (rb ** 2).sum()))


# ======================================================================
# 扰动抽样面：与第一梯队 executor 同一 rng 流 => O1 可逐字复现基线
# ======================================================================
def draw_perturbation(models, t_frac60):
    rng = np.random.default_rng(SEED)
    table = []
    for idx in range(len(models)):
        t60 = float(t_frac60[idx])
        row = [float(np.clip(t60 + rng.uniform(-JITTER, JITTER), 0.0, 1.0))
               for _ in range(N_BUDGET)]
        table.append(row)
    return table


def target_triple(t0, r0, a0, t_target):
    """第一梯队 executor 字面：R/A 按盘上真实 r0:a0 比例吸收 T 份额差额。"""
    rest = N_CELLS - int(t_target)
    denom = r0 + a0
    if denom == 0:
        return {"T": int(t_target), "R": rest, "A": 0}
    r_target = int(round(rest * r0 / denom))
    return {"T": int(t_target), "R": r_target, "A": rest - r_target}


# ======================================================================
# O1 离散 cell 重分配（第一梯队基线，逐字复用 redistribute_n_iter）
# ======================================================================
def redistribute_n_iter(t0: int, r0: int, a0: int, t_target: int, priority: str) -> int:
    t, r, a = int(t0), int(r0), int(a0)
    tgt = target_triple(t0, r0, a0, t_target)
    for step in range(1, O1_MAX_STEP + 1):
        cur = {"T": t, "R": r, "A": a}
        if cur == tgt:
            return step - 1
        if priority == "surplus_first":
            src = max(CLASSES, key=lambda c: (cur[c] - tgt[c], -CLASSES.index(c)))
            dst = max((c for c in CLASSES if c != src),
                      key=lambda c: (tgt[c] - cur[c], -CLASSES.index(c)))
        else:
            order = ("T", "R", "A") if priority == "class_order_TRA" else ("A", "R", "T")
            src = next(c for c in order if cur[c] > tgt[c])
            dst = next(c for c in reversed(order) if cur[c] < tgt[c])
        if src == dst:
            return step - 1
        cur[src] -= 1
        cur[dst] += 1
        t, r, a = cur["T"], cur["R"], cur["A"]
    return O1_MAX_STEP


# ======================================================================
# 向量化首达时求解器（逐抽并行，逐步推进；已命中的抽冻结）
# ======================================================================
def run_vec(step_fn, hit_fn, state, cap, params=()):
    """step_fn(state, params) -> 新 state；hit_fn(state, params) -> bool 数组。
    params：与 state 同长的逐抽参数数组（fitness / 目标等），随 active 池同步收缩。
    返回 (逐抽首达步数, 终态副本)；首达步数 0 = 起点即命中，未命中 = cap。"""
    n = len(state)
    n_iter = np.full(n, -1, dtype=np.int64)
    final = np.array(state, dtype=float, copy=True)
    act = np.arange(n)
    ps = [np.asarray(p, float) for p in params]
    h = hit_fn(state, ps)
    if bool(h.any()):
        n_iter[act[h]] = 0
        keep = ~h
        act, state, ps = act[keep], state[keep], [p[keep] for p in ps]
    for k in range(1, cap + 1):
        if act.size == 0:
            break
        state = step_fn(state, ps)
        final[act] = state
        h = hit_fn(state, ps)
        if bool(h.any()):
            n_iter[act[h]] = k
            keep = ~h
            act, state, ps = act[keep], state[keep], [p[keep] for p in ps]
    n_iter[n_iter < 0] = cap
    return n_iter, final


# ======================================================================
# O2 字面连续时间 replicator ODE（2 态 T vs rest，RK4）
#   ẋ = x(1−x)(f_T − f_A)；fitness 由扰动条件植入（f = (x0, 1−x0)）
#   命中判据：到最近边界不动点（x=0 或 1）距离 <= TOL
#   先验结构缺陷（字面可证）：plain replicator 只有边界不动点，x0 不可能被吸引
# ======================================================================
def o2_run(x_start, x_target):
    x_target = np.asarray(x_target, float)
    fT, fA = x_target, 1.0 - x_target

    def rhs(x, ps):
        # 2 态：ẋ = x(1−x)(f_T − f_A)，f_T = x0（植入的扰动条件），f_A = 1 − x0
        return x * (1.0 - x) * (ps[0] - ps[1])

    def step(x, ps):
        k1 = rhs(x, ps)
        k2 = rhs(x + 0.5 * O2_DT * k1, ps)
        k3 = rhs(x + 0.5 * O2_DT * k2, ps)
        k4 = rhs(x + O2_DT * k3, ps)
        return np.clip(x + (O2_DT / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4), 0.0, 1.0)

    def hit(x, ps):
        return (np.minimum(x, 1.0 - x) <= TOL)

    return run_vec(step, hit, np.asarray(x_start, float).copy(), O2_CAP, (fT, fA))


# ======================================================================
# O3 logit 正规形（softmax / logit 响应映射；adaptive dynamics 离散对偶）
#   logit(x_{k+1}) = (1−s)·logit(x_k) + s·(f_T − f_A)，取 f_T − f_A = logit(x0)
#   => 内点不动点 = x0（恒定，且与数据无关 => 收敛必几何）
# ======================================================================
def o3_run(x_start, x_target):
    x_target = np.asarray(x_target, float)
    lg_target = np.log(x_target / (1.0 - x_target))

    def step(x, ps):
        lg = np.log(x / (1.0 - x))
        return 1.0 / (1.0 + np.exp(-((1.0 - O3_S) * lg + O3_S * ps[1])))

    def hit(x, ps):
        return np.abs(x - ps[0]) <= TOL

    return run_vec(step, hit, np.asarray(x_start, float).copy(), O3_CAP,
                   (x_target, lg_target))


# ======================================================================
# O4 模仿动力学 = 离散 replicator 映射（按收益差比例复制，Maynard Smith 字面）
#   2×2 收益矩阵 A(x0) = [[0, x0], [1−x0, 0]]（反协调 / 稳定内点 NE = x0）
#   x_{k+1} = x·u_T / (x·u_T + (1−x)·u_A)，仅依赖收益差 D(x) = x0 − x
#   命中判据：|x − x0| <= TOL
# ======================================================================
def o4_run(x_start, x_target):
    x_target = np.asarray(x_target, float)

    def step(x, ps):
        u_t = (1.0 - x) * ps[0]
        u_a = x * (1.0 - ps[0])
        return x * u_t / np.maximum(x * u_t + (1.0 - x) * u_a, 1e-300)

    def hit(x, ps):
        return np.abs(x - ps[0]) <= TOL

    return run_vec(step, hit, np.asarray(x_start, float).copy(), O4_CAP, (x_target,))


# ======================================================================
# O5 连续时间 replicator ODE + 软竞争（增补第 5 本体，RK4）
#   ẋ_i = x_i(g_i − ḡ)，g_i = c·(f_i − x_i) 即「软竞争」= 负频依赖（自有份额超出目标即降适应度）
#   f = 扰动目标三元组（归一化份额）
#   => 内点不动点 = f（可证：不动点条件 g_i = g_j ⇔ f_i − x_i = f_j − x_j ⇒ x = f + const，
#      归一化后 const = 0）；replicator 形式 ⇒ Σx_i 严格守恒；c 只定速度（不动点与 c 无关）
#   命中判据：max_i |x_i − f_i| <= TOL
# ======================================================================
def o5_run(x_start3, f_target3):
    f = np.asarray(f_target3, float).copy()

    def rhs(x, ps):
        g = O5_C * (ps[0] - x)
        gbar = (x * g).sum(axis=1)
        return x * (g - gbar[:, None])

    def step(x, ps):
        k1 = rhs(x, ps)
        k2 = rhs(x + 0.5 * O5_DT * k1, ps)
        k3 = rhs(x + 0.5 * O5_DT * k2, ps)
        k4 = rhs(x + O5_DT * k3, ps)
        xn = x + (O5_DT / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        return np.clip(xn, 0.0, 1.0)

    def hit(x, ps):
        return np.max(np.abs(x - ps[0]), axis=1) <= TOL

    return run_vec(step, hit, np.asarray(x_start3, float).copy(), O5_CAP, (f,))


# ======================================================================
# 判据 + 诊断（判据面已冻结在上方常量）
# ======================================================================
def evaluate_criteria(n_iter_by_model, cap):
    """n_iter_by_model: list[np.ndarray(100)] 逐 model；返回判据 + 诊断。"""
    rates = [float(a.mean() / N_BUDGET) for a in n_iter_by_model]
    flat = np.concatenate(n_iter_by_model)
    rstat = stat_block(rates)
    floor_share = float((flat == 0).mean())
    cap_share = float((flat == cap).mean())
    rail_share = float(((flat == 0) | (flat == cap)).mean())
    draw_nd = n_distinct(flat)

    c1 = bool(rstat["n_distinct"] >= C1_NDISTINCT_MIN and rstat["std"] > 0)
    c2 = bool(floor_share < C2_FLOOR_SHARE_MAX
              and draw_nd >= C2_DRAWN_NDISTINCT_MIN
              and rail_share < C2_RAIL_SHARE_MAX)
    c3 = bool(cap_share < C3_CAP_HIT_SHARE_MAX)
    return {
        "c1_degenerate_guard_pass": c1,
        "c2_true_distribution_pass": c2,
        "c3_convergence_sane_pass": c3,
        "rates": rstat,
        "draw_level": {
            "n": int(flat.size),
            "n_iter_n_distinct": draw_nd,
            "floor_share_n_iter_eq_0": floor_share,
            "cap_hit_share_n_iter_eq_cap": cap_share,
            "rail_share_0_or_cap": rail_share,
            "n_iter_mean": float(flat.mean()),
            "n_iter_median": float(np.median(flat)),
            "n_iter_p95": float(np.percentile(flat, 95)),
            "n_iter_max": int(flat.max()),
            "total_steps": int(flat.sum()),
        },
    }


def main() -> int:
    pj = json.loads(SRC_PJ.read_text(encoding="utf-8"))
    s60 = json.loads(SRC_60.read_text(encoding="utf-8"))
    base = json.loads(BASE_RESULT.read_text(encoding="utf-8"))

    pj_all = pj["all_results"]
    s60_by_name = {m["model"]: m for m in s60["P_C_distortion_bound_60cells"]["per_model"]}
    models = list(pj_all["convergence_rates"].keys())
    t_frac60 = list(pj_all["T_frac60"])
    assert len(models) == len(t_frac60) == 9, "输入不是 9 model"
    for m in models:
        rec = s60_by_name[m]
        assert rec["T60"] + rec["R60"] + rec["A60"] == N_CELLS, "60-cell 守恒被破坏: %s" % m

    pert = draw_perturbation(models, t_frac60)
    pert_sha12 = canon_sha12(pert)

    # ---------------- O1 离散 cell 重分配（基线，逐字复用第一梯队） ----------------
    o1_by_model, o1_info = [], []
    for idx, m in enumerate(models):
        rec = s60_by_name[m]
        t0, r0, a0 = int(rec["T60"]), int(rec["R60"]), int(rec["A60"])
        it = np.asarray([redistribute_n_iter(t0, r0, a0,
                                             int(round(pert[idx][j] * N_CELLS)),
                                             PRIORITY) for j in range(N_BUDGET)], float)
        o1_by_model.append(it)
        o1_info.append({"model": m, "start_triple_TRA": [t0, r0, a0],
                        "n_iter_mean": float(it.mean()), "n_iter_min": int(it.min()),
                        "n_iter_max": int(it.max()), "n_iter_distinct": n_distinct(it),
                        "convergence_rate": float(it.mean() / N_BUDGET)})
    base_by_model = {p["model"]: p["convergence_rate"] for p in base["per_model"]}
    o1_rates = [p["convergence_rate"] for p in o1_info]
    o1_identical = bool(all(base_by_model.get(p["model"]) == p["convergence_rate"]
                            for p in o1_info))

    # ---------------- O2 / O3 / O4（2 态，start = T60/60） ----------------
    x_start2 = [float(s60_by_name[m]["T60"]) / N_CELLS for m in models]
    o2_by_model, o3_by_model, o4_by_model = [], [], []
    o2_final, o3_final, o4_final, o5_final = [], [], [], []
    for idx, m in enumerate(models):
        tgt = np.asarray(pert[idx], float)
        st = np.full(N_BUDGET, x_start2[idx], float)
        it, fin = o2_run(st, tgt)
        o2_by_model.append(it.astype(float))
        o2_final.append(fin)
        it, fin = o3_run(st, tgt)
        o3_by_model.append(it.astype(float))
        o3_final.append(fin)
        it, fin = o4_run(st, tgt)
        o4_by_model.append(it.astype(float))
        o4_final.append(fin)

    # ---------------- O5（3 态，fitness = 扰动目标三元组） ----------------
    o5_by_model, o5_info, o5_f3 = [], [], []
    for idx, m in enumerate(models):
        rec = s60_by_name[m]
        t0, r0, a0 = int(rec["T60"]), int(rec["R60"]), int(rec["A60"])
        denom = r0 + a0
        f3 = np.zeros((N_BUDGET, 3), float)
        for j, x0 in enumerate(pert[idx]):
            rest = 1.0 - x0
            if denom == 0:
                f3[j] = (x0, rest, 0.0)
            else:
                rc = rest * r0 / denom
                f3[j] = (x0, rc, rest - rc)
        st3 = np.tile(np.asarray([t0, r0, a0], float) / N_CELLS, (N_BUDGET, 1))
        it, fin = o5_run(st3, f3)
        o5_by_model.append(it.astype(float))
        o5_final.append(fin)
        o5_f3.append(f3)
        o5_info.append({"model": m, "start_triple_TRA": [t0, r0, a0],
                        "f_target_min_component": float(f3.min(axis=1).min()),
                        "n_iter_mean": float(it.mean()), "n_iter_min": int(it.min()),
                        "n_iter_max": int(it.max()), "n_iter_distinct": n_distinct(it),
                        "convergence_rate": float(it.mean() / N_BUDGET)})

    # ---------------- 逐本体判据 + 诊断 ----------------
    caps = {"O1_discrete_cell_redistribution": O1_MAX_STEP,
            "O2_replicator_ode_literal": O2_CAP,
            "O3_logit_normal_form": O3_CAP,
            "O4_imitation_replicator_map": O4_CAP,
            "O5_replicator_ode_softlimit": O5_CAP}
    by_model = {
        "O1_discrete_cell_redistribution": o1_by_model,
        "O2_replicator_ode_literal": o2_by_model,
        "O3_logit_normal_form": o3_by_model,
        "O4_imitation_replicator_map": o4_by_model,
        "O5_replicator_ode_softlimit": o5_by_model,
    }
    per_model_raw = {"O1_discrete_cell_redistribution": o1_info,
                     "O2_replicator_ode_literal": None,
                     "O3_logit_normal_form": None,
                     "O4_imitation_replicator_map": None,
                     "O5_replicator_ode_softlimit": o5_info}
    for name in ("O2_replicator_ode_literal", "O3_logit_normal_form",
                 "O4_imitation_replicator_map"):
        per_model_raw[name] = [{
            "model": models[idx],
            "T_frac60_real": t_frac60[idx],
            "n_iter_mean": float(by_model[name][idx].mean()),
            "n_iter_min": int(by_model[name][idx].min()),
            "n_iter_max": int(by_model[name][idx].max()),
            "n_iter_distinct": n_distinct(by_model[name][idx]),
            "convergence_rate": float(by_model[name][idx].mean() / N_BUDGET),
        } for idx in range(len(models))]

    # 目标距离诊断：真「终态到扰动目标的距离」（不是 n_iter<cap 的代理量）
    #   O1 以 cell 计（整数精确命中 => 0；触顶 => 剩余 cell 差）
    #   O2/O3/O4 以 T 份额计；O5 以三元组最大分量偏差计
    tgt_dist = {}
    o1_resid = []
    for idx, m in enumerate(models):
        rec = s60_by_name[m]
        t0 = int(rec["T60"])
        it = by_model["O1_discrete_cell_redistribution"][idx]
        res = [0.0 if v < O1_MAX_STEP else float(abs(t0 - int(round(x * N_CELLS))))
               for v, x in zip(it, pert[idx])]
        o1_resid.extend(res)
    tgt_dist["O1_discrete_cell_redistribution"] = {
        "metric": "|T_final − T*|（cell）", "mean": float(np.mean(o1_resid)),
        "median": float(np.median(o1_resid)), "max": float(np.max(o1_resid))}
    for name, fins, tgts, metric in (
            ("O2_replicator_ode_literal", o2_final, [np.asarray(p, float) for p in pert],
             "|x_final − x0|（T 份额）"),
            ("O3_logit_normal_form", o3_final, [np.asarray(p, float) for p in pert],
             "|x_final − x0|（T 份额）"),
            ("O4_imitation_replicator_map", o4_final, [np.asarray(p, float) for p in pert],
             "|x_final − x0|（T 份额）")):
        d = np.concatenate([np.abs(f - t) for f, t in zip(fins, tgts)])
        tgt_dist[name] = {"metric": metric, "mean": float(d.mean()),
                          "median": float(np.median(d)), "max": float(d.max())}
    d5 = np.concatenate([np.max(np.abs(f - t), axis=1)
                         for f, t in zip(o5_final, o5_f3)])
    tgt_dist["O5_replicator_ode_softlimit"] = {
        "metric": "max_i |x_i − f_i|（三元组份额）", "mean": float(d5.mean()),
        "median": float(np.median(d5)), "max": float(d5.max())}

    ontologies = {}
    for name in ONTOLOGIES:
        ev = evaluate_criteria(by_model[name], caps[name])
        cap = caps[name]
        conv = [float((by_model[name][idx] < cap).mean()) for idx in range(len(models))]
        ontologies[name] = {
            "n_iter_cap": cap,
            "criteria": {k: ev[k] for k in
                         ("c1_degenerate_guard_pass", "c2_true_distribution_pass",
                          "c3_convergence_sane_pass")},
            "criteria_evidence": {"rates": ev["rates"], "draw_level": ev["draw_level"]},
            "diagnostics_not_criteria": {
                "rel_std_of_rates": ev["rates"]["rel_std"],
                "iqr_of_rates": ev["rates"]["iqr"],
                "convergence_rate_dispersion_max_over_min":
                    float(ev["rates"]["max"] / ev["rates"]["min"])
                    if ev["rates"]["min"] > 0 else None,
                "draw_converged_within_cap_share": float(np.mean(conv)),
                "final_target_distance": tgt_dist[name],
                "total_iteration_steps": ev["draw_level"]["total_steps"],
            },
            "per_model": per_model_raw[name],
        }
        ontologies[name]["_raw"] = [[int(v) for v in a] for a in by_model[name]]

    # ---------------- C4 可复现：进程内二次重算自比 ----------------
    # 诊断（不作判据）：本体是否携带 T_frac60 之外的信息 + O5 最小份额瓶颈假设
    for name in ONTOLOGIES:
        rates = [p["convergence_rate"] for p in ontologies[name]["per_model"]]
        gaps = [abs(rates[i] - rates[j]) / ((rates[i] + rates[j]) / 2.0)
                for i in range(len(models)) for j in range(i + 1, len(models))
                if abs(t_frac60[i] - t_frac60[j]) < 1e-12 and rates[i] > 0 and rates[j] > 0]
        ontologies[name]["diagnostics_not_criteria"].update({
            "spearman_rho_T_frac60_vs_rate": spearman(t_frac60, rates),
            "n_same_Tfrac60_pairs": len(gaps),
            "same_Tfrac60_pair_max_relative_rate_gap": (max(gaps) if gaps else None),
        })
    o5_minf = [p["f_target_min_component"] for p in per_model_raw["O5_replicator_ode_softlimit"]]
    o5_nit = [p["n_iter_mean"] for p in per_model_raw["O5_replicator_ode_softlimit"]]
    ontologies["O5_replicator_ode_softlimit"]["diagnostics_not_criteria"][
        "spearman_rho_min_target_component_vs_n_iter_mean"] = spearman(o5_minf, o5_nit)

    ev2 = {name: evaluate_criteria(by_model[name], caps[name]) for name in ONTOLOGIES}
    for name in ONTOLOGIES:
        c4 = bool(canon_sha12(ontologies[name]["_raw"])
                  == canon_sha12([[int(v) for v in a] for a in by_model[name]])
                  and canon_sha12(ev2[name]["draw_level"])
                  == canon_sha12(ontologies[name]["criteria_evidence"]["draw_level"]))
        ontologies[name]["criteria"]["c4_reproducible_pass"] = c4
        ontologies[name]["all_four_criteria_pass"] = bool(
            all(ontologies[name]["criteria"].values()))

    payload_core = {
        "schema": "v3_recheck_preexp_data/26_p_j_multi_ontology/1",
        "nature": "预实验 = 探索性档（三档强度最低档）：只作本体选择依据，0 判定动作 0 verdict，"
                  "不入 K-V3R-26 判定链；正式判定待择优后另跑（K-V3R-26 字面不动）",
        "date": "2026-09-27",
        "produced_by": "Mavis 团队 worker（Mavis root session 派工，PI 2026-09-27 问卷 "
                       "ask_ee8102884179fd206517c5b6 Q1 拍板「多本体预实验，效果好再正式实验」）",
        "dispatch_inputs": [
            {"path": "results/_v3_recheck_prereg_v1_2026_09_27.md",
             "sha12_measured": sha12(PREREG.read_bytes()),
             "role": "K-V3R-26 / TH-V3R-26 形式锚（字面沿用，0 擅调）"},
            {"path": "results/_v3_recheck_26_executor_2026_09_27.py",
             "sha12_measured": sha12(EXEC_BASE.read_bytes()),
             "role": "fallback 纪律锚：O1 构造字面 + 扰动抽样顺序 + 统计口径"},
            {"path": "results/_v3_recheck_26_result_2026_09_27.json",
             "sha12_measured": sha12(BASE_RESULT.read_bytes()),
             "role": "第一梯队落地件（只读；O1 基线逐字复现的对照面）"},
            {"path": "results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json",
             "sha12_measured": sha12(SRC_PJ.read_bytes()), "role": "9 model T_frac60 真分布"},
            {"path": "results/deposon_v3_physical_opt_60cells_2026_09_11.json",
             "sha12_measured": sha12(SRC_60.read_bytes()),
             "role": "9 model 真实 (T60,R60,A60) 起始三元组"},
        ],
        "construct": {
            "convergence_rate_form": "convergence_rate_m = mean_j(n_iter_j) / n_budget, j=1..100"
                                     "（TH-V3R-26 冻结形式，沿用不动）",
            "n_budget": N_BUDGET, "jitter": "+-0.05 uniform on T_frac60 (clip [0,1])",
            "seed": SEED,
            "perturbation_stream": "与第一梯队 executor 同一 rng 流（default_rng(SEED) 逐 model 顺序抽 100 次）"
                                   "=> O1 可逐字复现，且 5 本体共用同一批扰动抽样（配对比较）",
            "perturbation_table_sha12": pert_sha12,
            "tolerance": "TOL = 1e-6（连续本体统一；O1 为整数精确命中）",
            "models": models,
            "t_frac60_real": t_frac60,
        },
        "frozen_effect_criteria": {
            "C1_degenerate_guard": "n_distinct(9 model rates) > 3 且 std(rates) > 0"
                                   "（沿 K-V3R-0-A 字面）",
            "C2_true_distribution": "floor_share(n_iter==0) < 0.50 且 draw_n_distinct > 3 且 "
                                    "rail_share(n_iter ∈ {0, cap}) < 0.50（「非天花板/地板」操作化）",
            "C3_convergence_sane": "cap_hit_share(n_iter == cap) < 0.20（派工单字面）",
            "C4_reproducible": "重跑逐字不变（进程内二次重算自比 + 进程外双跑比对登记于报告）",
            "good_effect_definition": "C1 ∧ C2 ∧ C3 ∧ C4 全满足 = 「效果好」候选",
            "frozen_before_run": True,
        },
        "ontology_registry": [
            {"id": "O1_discrete_cell_redistribution",
             "label": "离散 cell 重分配", "dispatch_slot": "建议 ①（基线 = 第一梯队已落地）",
             "state": "60-cell 整数三元组 (T,R,A) 每步 1 个 cell 从盈余最大类移到亏缺最大类，"
                      "直到命中扰动目标三元组；步数 = n_iter；结构上限 60 必收敛",
             "target_reachable": True,
             "note": "逐字复用第一梯队 redistribute_n_iter + priority=surplus_first"},
            {"id": "O2_replicator_ode_literal",
             "label": "连续时间 replicator ODE（字面）", "dispatch_slot": "建议 ②",
             "state": "2 态 (T vs rest)，ẋ = x(1−x)(f_T − f_A)，RK4 (dt=5e-3)；fitness 由扰动条件"
                      "植入 f=(x0, 1−x0)；命中 = 到最近边界不动点距离 <= TOL",
             "target_reachable": False,
             "note": "**字面可证缺陷**：plain replicator ẋᵢ=xᵢ(fᵢ−f̄) 只有边界不动点 (x=0,1)，"
                     "扰动份额 x0 不可能是吸引子；本体的收敛判据落在「到边界的步数」，"
                     "与 O3/O4/O5 的「到扰动目标的步数」量纲不同（比较只在分布信息量层，不在数值层）"},
            {"id": "O3_logit_normal_form",
             "label": "logit/量子响应动态（logit 正规形）", "dispatch_slot": "建议 ③",
             "state": "2 态，logit(x_{k+1}) = (1−s)·logit(x_k) + s·logit(x0)，s=0.25（softmax 响应映射的"
                      "logit 正规形）；内点不动点 ≡ x0，几何收敛",
             "target_reachable": True,
             "note": "fitness 差直接设成 logit(x0) => 不动点恒为扰动目标；"
                     "收敛步数只依赖 |logit 差|，与模型自身 payoff 无关"},
            {"id": "O4_imitation_replicator_map",
             "label": "imitation dynamics（按收益差比例复制）", "dispatch_slot": "建议 ④",
             "state": "2 态离散 replicator 映射 x_{k+1}=x·u_T/(x·u_T+(1−x)·u_A)；收益矩阵 "
                      "A(x0)=[[0,x0],[1−x0,0]]（反协调，内点稳定 NE = x0，收益差 D(x)=x0−x 斜率 −1）",
             "target_reachable": True,
             "note": "Maynard Smith 字面模仿；内点 NE 处 |g'| = 1 + x*(1−x*)D'/2 > 1（恒扩张）"
                     "=> 收敛慢但几何可达，步数对模型近乎不敏感（见诊断 rel_std）"},
            {"id": "O5_replicator_ode_softlimit",
             "label": "连续时间 replicator ODE + 软竞争（增补）", "dispatch_slot": "增补第 5 本体",
             "state": "3 态 (T,R,A)，ẋ_i = x_i(g_i − ḡ)，g_i = c·(f_i − x_i)，c=0.5，RK4 (dt=0.05)；"
                      "f = 扰动目标三元组（归一化份额）=> 内点不动点 ≡ f、负频依赖稳定、Σx_i 严格守恒",
             "target_reachable": True,
             "note": "增补理由：分辨 O2/O4 的坏点是**数据**造成还是**结构**造成 —— 只加一个标准"
                     "软竞争项（自有份额超出目标即降适应度）把 O2 的字面形式修成内点可收敛；"
                     "c=0.5 为实现常数（只定速度，不动点与 c 无关），非判据"},
        ],
        "per_ontology": {name: {k: v for k, v in ontologies[name].items()
                                if k != "_raw"} for name in ONTOLOGIES},
        "raw_n_iter_by_ontology": {name: ontologies[name]["_raw"] for name in ONTOLOGIES},
        "process_register": [
            {"id": "PR-1", "kind": "implementation_bug_fixed", "ontology": "O3_logit_normal_form",
             "first_run_measurement": "全部 9 model 的 900 抽 n_iter ≡ 100000（= O3_CAP），"
                                      "rates n_distinct=1、std=0，C1/C2/C3 三判据同时判否",
             "root_cause": "命中判据 hit() 误把 log-odds 目标 lg_target 当成分数值目标比较"
                           "（|x − logit(x0)| <= TOL），该条件恒不成立 => 全部抽走到迭代上限",
             "fix": "params 改为同时携带 x_target（供 hit）与 lg_target（供 step）；判据与构造字面未改",
             "disposition": "按「不误导」纪律如实登记后重跑；两次实测值都留痕，不删改首跑记录"},
            {"id": "PR-2", "kind": "structural_degeneracy_found", "ontology": "O4_imitation_replicator_map",
             "measurement": "900 抽 n_iter ≡ 1，9 model rates ≡ 0.01 全常量，draw_n_distinct=1",
             "root_cause": "为使扰动份额成为内点 NE 而取的收益矩阵 A(x0)=[[0,x0],[1−x0,0]] 给出 "
                           "u_T=(1−x)·x0、u_A=x·(1−x0)，两式共享 x(1−x) 因子，在 replicator 映射 "
                           "x·u_T/(x·u_T+(1−x)·u_A) 中约掉 => 映射退化为常值函数 x ↦ x0（一步到点）",
             "secondary_structural_fact": "一般 Maynard Smith 离散 replicator 映射在内点 NE 处 "
                                          "|g'| = 1 + x*(1−x*)D'/2 >= 1（恒扩张）=> 不存在任何收益标定"
                                          "能让它收敛到内点目标；本体的内点收敛能力在结构上即不成立",
             "disposition": "不重调 payoff（无解且属擅调）；如实判 C1/C2 否，作为「模仿动力学不可作"
                            "正式本体」的结构性结论交付"},
            {"id": "PR-3", "kind": "semantic_mismatch_found", "ontology": "O2_replicator_ode_literal",
             "measurement": "4 条字面判据全过（C1-C4 皆 true），但终态到扰动目标的距离 mean=0.2870 / "
                            "median=0.2957 / max=0.4919（份额单位）—— 目标从未被接近",
             "root_cause": "plain replicator ẋ_i = x_i(f_i − f̄) 只有边界不动点（可证），扰动份额 x0 "
                           "不可能是吸引子；本体的 n_iter 实为「流到最近边界的步数」，其大小由 |2·x0−1| "
                           "支配（实测 ρ(T_frac60, rate) = −0.9916，近乎 T_frac60 的单调重标）",
             "disposition": "判据面 0 擅调（4 条判据的字面结果保留为「全过」）；语义错配只在诊断面"
                            "（final_target_distance）如实登记，并在报告 §5 择优建议中据此排除"},
        ],
        "runtime": "0 LLM; numpy + hashlib + json only; no network; read-only inputs; 0 改动既有件",
        "iron_rules": {
            "exploratory_only_no_verdict": True,
            "kill_line_K_V3R_26_untouched": True,
            "0_LLM": True, "no_proxy": True, "no_key_in_prompt_json_disk": True,
            "read_only_inputs": True, "derived_json_not_merged": True,
            "existing_26_series_untouched": True,
        },
        "verdict": None,
        "verdict_note": "预探索性档：verdict = null（0 判定动作 0 verdict）。本件不构成 K-V3R-26 判定。",
    }

    payload_sha12 = canon_sha12(payload_core)
    payload = dict(payload_core)
    payload["reproducibility"] = {
        "payload_sha12": payload_sha12,
        "c4_in_process_recompute_identical": True,
        "note": "C4 的进程外双跑比对（两次落盘件 SHA-12 逐字相同）由 worker 核验并登记于报告",
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("[preexp] written:", OUT.relative_to(REPO))
    print("[preexp] perturbation_table_sha12 =", pert_sha12)
    print("[preexp] O1 baseline identical to landed 26 result:", o1_identical)
    for name in ONTOLOGIES:
        c = ontologies[name]["criteria"]
        d = ontologies[name]["criteria_evidence"]["draw_level"]
        r = ontologies[name]["criteria_evidence"]["rates"]
        print("[preexp] %-34s C1=%d C2=%d C3=%d C4=%d  n_dist=%d std=%.6g rel_std=%.4g "
              "draw_nd=%d floor=%.3f cap=%.3f rail=%.3f mean_iter=%.1f"
              % (name, c["c1_degenerate_guard_pass"], c["c2_true_distribution_pass"],
                 c["c3_convergence_sane_pass"], c["c4_reproducible_pass"],
                 r["n_distinct"], r["std"], r["rel_std"] or 0.0, d["n_iter_n_distinct"],
                 d["floor_share_n_iter_eq_0"], d["cap_hit_share_n_iter_eq_cap"],
                 d["rail_share_0_or_cap"], d["n_iter_mean"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
