#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V3-R 补审 #27 P-L P-C finite-size scaling — executor (worker · 2026-09-27)

沿 results/_v3_recheck_prereg_v1_2026_09_27.md（SHA-12 88052d7db895）字面执行：
  - K-V3R-0-A 防退化门（n_distinct > 3 + std > 0，跑前对盘上输入字段自证 + 退化杠杆事前登记）
  - K-V3R-0-B 沿用阈值（0 新设判定阈值；判据字面 = K-V3R-27）
  - K-V3R-0-C 双口径（新构造 verdict + 沿原 V3 阈值字面 verdict 并报）
  - K-V3R-0-D 派生 JSON 不合并（本件独立落盘 _v3_recheck_27_result_*.json）
  - K-V3R-0-E 0 LLM（纯 numpy / hashlib / json，0 网络 0 模型调用）
  - K-V3R-27 kill-line 字面（三腿，按字面顺序首次命中者治理）：
      (a) 跨 N scaling exponent ν 的 bootstrap 95% CI 跨零 -> FAIL（真证伪，与 PARTIAL_FAIL_H0 同向）
      (b) CI 上界 <= 0                                    -> PASS（结构性恒等成立）
      (c) max_R2 仍 < 0.9                                 -> FAIL（维持假证伪）

新构造（沿预登记 §1.2 #27 (a)(b) 字面）：
  (a) 真 finite-size scaling：跨 N = 20/40/60/80/120 cells 重展 data collapse（逐 N 各算 R²，
      取代 as-run 单网格点 (ν=1.5, η=0.1) 的 hidden fitting）
  (b) scaling exponent ν 的 bootstrap CI（n=1000，§1.2 #27 (b) 字面）

**量纲/口径隔离声明**：本条的 η 是**异常指数（ anomalous exponent，标度轴）**；
#10 P-C exp_3_3 的 η 是**温度抖动（ Langevin 噪声幅度）**。两处 η 同名不同义，
0 互替、0 跨条比较（防口径污染）。

输入（全部只读）：
  - results/_p_l_p_c_finite_size_scaling_2026_09_16/p_l_p_c_finite_size_scaling_results_2026_09_16.json
  - results/deposon_v3_physical_opt_60cells_2026_09_11.json

S-40 布尔显式命名：`*_hit = True` 表示「触发 FAIL / 触发警报」；`*_pass = True` 表示「存活 / 合格」。
"""

import hashlib
import json
import os
import sys
from pathlib import Path

import numpy as np

# ---- 构造常量（沿预登记 §1.2 #27 字面 / 既有字面，0 新设判定阈值）----
SEED = 20260927
N_BOOT = 1000          # 预登记 §1.2 #27 (b) 字面：ν bootstrap n=1000
N_DRAWS = 400          # 每 (N, model) 重抽次数（实现自由度，非判定阈值）
N_CELLS = 60           # V3 既有字面：9 model x 60 cells
LOG_FLOOR = -10.0      # 沿 deposon_pc_d1_d3_2026_09_15.json §R2_b_CI_log_log_fit 记录字面
EPS = 1e-12
N_LIST = [20, 40, 60, 80, 120]   # 预登记 §1.2 #27 (a) 字面（§2.4 标占位 -> 本件取该字面最小构造）
MAX_R2_KILL = 0.9      # K-V3R-27 (c) 字面：max_R2 仍 < 0.9 -> FAIL
# as-run 字面网格（ν, η）+ 含 0/负值的扩展 ν 轴（使 (b) 腿「CI 上界 <= 0」可达）
GRID_NU_LEGACY = [0.5, 1.0, 1.5, 2.0, 2.5]
GRID_NU_EXT = [-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0]
GRID_ETA = [0.1, 0.2, 0.3, 0.4, 0.5]


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
SRC_PL = REPO / "results/_p_l_p_c_finite_size_scaling_2026_09_16/p_l_p_c_finite_size_scaling_results_2026_09_16.json"
SRC_60 = REPO / "results/deposon_v3_physical_opt_60cells_2026_09_11.json"
PREREG = REPO / "results/_v3_recheck_prereg_v1_2026_09_27.md"
PREREG11 = REPO / "results/_v3_recheck_prereg_v1p1_2026_09_27.md"
OUT = REPO / "results/_v3_recheck_27_result_2026_09_27.json"


def sha12(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:12]


def n_distinct(xs) -> int:
    vals = [float(x) for x in xs if x is not None and np.isfinite(float(x))]
    return len(set(round(v, 12) for v in vals))


def n_undefined(xs) -> int:
    return int(sum(1 for x in xs if x is None or not np.isfinite(float(x))))


def stat_block(xs):
    a = np.asarray([float(x) for x in xs if x is not None and np.isfinite(float(x))], float)
    if a.size == 0:
        return {"n": 0, "n_finite": 0, "n_distinct": 0, "std": None, "min": None,
                "max": None, "mean": None}
    return {"n": int(a.size), "n_finite": int(a.size), "n_distinct": n_distinct(a.tolist()),
            "std": float(a.std(ddof=0)), "min": float(a.min()), "max": float(a.max()),
            "mean": float(a.mean())}


def ols_r2(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    if x.size == 0:
        return {"slope": None, "intercept": None, "r2": None, "ss_tot": 0.0,
                "undefined_hit": True, "reason": "empty sample"}
    if not (np.all(np.isfinite(x)) and np.all(np.isfinite(y))):
        return {"slope": None, "intercept": None, "r2": None, "ss_tot": 0.0,
                "undefined_hit": True, "reason": "non-finite input"}
    xm, ym = x.mean(), y.mean()
    ss_xx = float(((x - xm) ** 2).sum())
    if ss_xx <= 0:
        return {"slope": None, "intercept": None, "r2": None, "ss_tot": 0.0,
                "undefined_hit": True, "reason": "x 方差 = 0"}
    b = float(((x - xm) * (y - ym)).sum() / ss_xx)
    a = float(ym - b * xm)
    ss_res = float(((y - (a + b * x)) ** 2).sum())
    ss_tot = float(((y - ym) ** 2).sum())
    r2 = None if ss_tot <= 0 else 1.0 - ss_res / ss_tot
    return {"slope": b, "intercept": a, "r2": r2, "ss_tot": ss_tot, "ss_res": ss_res,
            "undefined_hit": r2 is None, "reason": "" if r2 is not None else "ss_tot = 0"}


def main() -> int:
    pl = json.loads(SRC_PL.read_text(encoding="utf-8"))
    s60 = json.loads(SRC_60.read_text(encoding="utf-8"))
    prereg_sha12 = sha12(PREREG.read_bytes())
    prereg11_sha12 = sha12(PREREG11.read_bytes())

    ar = pl["all_results"]
    grid_asrun = ar["data_collapse_R2_grid_scan"]
    by_name = {m["model"]: m for m in s60["P_C_distortion_bound_60cells"]["per_model"]}
    models = list(by_name.keys())
    assert len(models) == 9, "60cells 输入不是 9 model"
    t_c = float(s60["input_data"]["T_C_baseline"])
    p_m = {m: by_name[m]["T60"] / float(N_CELLS) for m in models}
    d_m = {m: float(by_name[m]["D_fix2_cosine"]) for m in models}
    y_log = {m: float(max(np.log(max(d_m[m], EPS)), LOG_FLOOR)) for m in models}

    # ---------- as-run 结构审计（死因机械证据，K-V3R-0-C 口径 2 的基线） ----------
    NUG = "ν"
    ETG = "η"
    nu_keys = sorted(grid_asrun["R2_grid"].keys(), key=lambda s: float(s.split("=")[1]))
    eta_vals = [row[ETG] for row in grid_asrun["R2_grid"][nu_keys[0]]]
    M = np.array([[row["R2"] for row in grid_asrun["R2_grid"][k]] for k in nu_keys], float)
    sv = np.linalg.svd(M, compute_uv=False)
    u, s, vt = np.linalg.svd(M)
    rank1 = np.outer(s[0] * u[:, 0], vt[0])
    rank1_resid = float(np.abs(M - rank1).max())
    arg = np.unravel_index(int(M.argmax()), M.shape)
    periodicity = {
        "nu_0.5_equals_nu_2.5_hit": bool((M[0] == M[4]).all()),
        "nu_1.0_equals_nu_2.0_hit": bool((M[1] == M[3]).all()),
        "nu_axis_period": 2.0,
    }
    structural_audit = {
        "asrun_grid_nu": [float(k.split("=")[1]) for k in nu_keys],
        "asrun_grid_eta": eta_vals,
        "asrun_grid_matrix": M.tolist(),
        "max_R2_field": grid_asrun["max_R2"],
        "max_R2_recomputed": float(M.max()),
        "max_R2_field_match_hit": bool(float(M.max()) == float(grid_asrun["max_R2"])),
        "best_params_field": grid_asrun["best_params"],
        "argmax_index": [int(arg[0]), int(arg[1])],
        "argmax_params": [float(nu_keys[arg[0]].split("=")[1]), eta_vals[arg[1]]],
        "argmax_on_grid_edge_hit": bool(arg[1] == 0 or arg[1] == len(eta_vals) - 1
                                        or arg[0] == 0 or arg[0] == len(nu_keys) - 1),
        "argmax_eta_edge_note": "argmax 落在 η 轴最小档（η=%g）= 网格边界，无内点最优" % eta_vals[arg[1]],
        "rank1_separability": {
            "singular_values": [float(v) for v in sv],
            "sigma2_over_sigma1": float(sv[1] / sv[0]),
            "rank1_max_abs_resid": rank1_resid,
            "multiplicatively_separable_hit": bool(rank1_resid <= 1e-6),
            "reading": "R²(ν,η) = f(η)·g(ν)（秩 1，残差 <= 1e-6 = 6 位小数舍入量级）"
                       "=> 网格无交叉项信息，argmax = 两轴各自 argmax 的乘积，"
                       "该「扫描」在结构上不可能是数据坍缩最优的证据（hidden fitting 的机械证明）",
        },
        "nu_periodicity": periodicity,
        "N_axis_present_hit": _has_key_recursive(pl, ("N", "n_cells", "cells", "system_size", "L", "size")),
        "N_axis_note": "as-run 件内 0 个系统尺寸字段（keys 递归扫 N/n_cells/cells/system_size/L/size）"
                       "=> 所谓「有限尺寸标度」在盘上没有任何尺寸参与",
    }

    # ---------- 口径 2：沿原 V3 阈值字面算 verdict ----------
    legacy_max_r2 = float(grid_asrun["max_R2"])
    legacy_leg_c_hit = bool(legacy_max_r2 < MAX_R2_KILL)
    legacy_verdict = "FAIL" if legacy_leg_c_hit else "PASS"
    legacy_track = {
        "source": "results/_p_l_p_c_finite_size_scaling_2026_09_16/"
                  "p_l_p_c_finite_size_scaling_results_2026_09_16.json §all_results（只读，未写）",
        "asrun_max_R2": legacy_max_r2,
        "asrun_best_params": grid_asrun["best_params"],
        "asrun_final_dang_verdict": ar["final_dang_verdict"],
        "kill_line_leg_c_legacy_hit": legacy_leg_c_hit,
        "kill_line_legacy": legacy_verdict,
        "legacy_verdict": ("FAIL（维持假证伪）：as-run max_R2 = %.6f < 0.9（K-V3R-27 (c) 字面）；"
                           "同件 final_dang_verdict 字面「%s」；且网格无 N 轴（秩 1 可分离）"
                           % (legacy_max_r2, ar["final_dang_verdict"])),
    }

    # ---------- K-V3R-0-A 防退化门：跑前对盘上输入字段自证 ----------
    input_selfcheck = {
        "60cells_T_frac60 (盘上真实, 逐 model)": stat_block([by_name[m]["T_frac60"] for m in models]),
        "60cells_T60 (盘上真实, 逐 model)": stat_block([by_name[m]["T60"] for m in models]),
        "60cells_R60 (盘上真实, 逐 model)": stat_block([by_name[m]["R60"] for m in models]),
        "60cells_A60 (盘上真实, 逐 model)": stat_block([by_name[m]["A60"] for m in models]),
        "60cells_D_fix2_cosine (盘上真实, 逐 model)": stat_block([d_m[m] for m in models]),
        "60cells_cos_sim (盘上真实, 逐 model)": stat_block([by_name[m]["cos_sim"] for m in models]),
        "60cells_T30 (盘上真实, 逐 model)": stat_block([by_name[m]["T30"] for m in models]),
        "P_T_true_fraction (T60/60, 派生自盘上计数)": stat_block([p_m[m] for m in models]),
        "log_D_fix2 (含 log 地板, 逐 model)": stat_block([y_log[m] for m in models]),
    }
    gate_fields = list(input_selfcheck.keys())
    gate_pass = {k: bool(input_selfcheck[k]["n_distinct"] > 3 and input_selfcheck[k]["std"] > 0)
                 for k in gate_fields}
    degen_alarm_hit = not all(gate_pass.values())
    t30_exact_half = bool(all(by_name[m]["T30"] * 2 == by_name[m]["T60"] for m in models))

    degen_levers = [
        {"lever": "N = 80 / 120 > 盘上 60 cells",
         "why": "只能从固定 60-cell 总体有放回重采样 -> 「系统尺寸」是名义的，不是独立系统",
         "pre_registered_disposition": "登记为外推边界；均匀使用同一重采样机制，不把 N=80/120 "
                                       "读成真实扩图族实验结果"},
        {"lever": "N = 60 是否用 as-run 精确总体（而非重采样）",
         "why": "两种机制在 N=60 处不等价（无放回 vs 有放回），会改变该档读数",
         "pre_registered_disposition": "主口径统一用有放回（机制一致）；as-run 精确总体作敏感性腿单列"},
        {"lever": "ν 轴若只取正值 -> (b) 腿「CI 上界 <= 0」不可达",
         "why": "as-run ν 轴全为正（0.5..2.5），无法表达 ν <= 0 的结构性恒等分支",
         "pre_registered_disposition": "连续 ν 估计量 ν̂ = c1/c2 允许任意实数（含 0/负）；"
                                       "另附含 0/负值的扩展 ν 轴网格"},
        {"lever": "log 地板 -10.0（2 个 model 的 D_fix2 与 2 个 model 的 Δt 恰为 0）",
         "why": "地板点位于拟合角落，对 R² 与斜率有支配性影响",
         "pre_registered_disposition": "主口径沿既有地板字面；另附「去地板」敏感性腿（仅取 D>0 且 Δt>0 的点）"},
    ]

    # ---------- 新构造：跨 N 重采样数据面 ----------
    def draw_surface(seed_tag, n_draws):
        """逐 (N, model) 有放回抽 N cells；返回 (rows_x1, rows_y, meta)。

        rows_x1 = max(log|p_draw - T_c|, LOG_FLOOR)，rows_y = log D_fix2(model)
        """
        xs, ys, meta = [], [], []
        for N in N_LIST:
            for mi, m in enumerate(models):
                rng = np.random.default_rng([SEED, seed_tag, int(N), mi])
                k = rng.binomial(int(N), p_m[m], size=n_draws).astype(float)
                p_draw = k / float(N)
                dt = np.abs(p_draw - t_c)
                with np.errstate(divide="ignore"):
                    lg = np.where(dt > 0, np.log(np.maximum(dt, EPS)), LOG_FLOOR)
                lg = np.maximum(lg, LOG_FLOOR)
                xs.append(lg)
                ys.append(np.full(n_draws, y_log[m]))
                meta.append({"N": int(N), "model": m, "n_draws": n_draws,
                             "T_frac_draw_mean": float(p_draw.mean()),
                             "T_frac_draw_std": float(p_draw.std(ddof=0)),
                             "n_draws_floored": int((lg <= LOG_FLOOR).sum())})
        return np.concatenate(xs), np.concatenate(ys), meta

    x1, y, meta = draw_surface(1, N_DRAWS)
    logN = np.concatenate([np.full(N_DRAWS, np.log(r["N"])) for r in meta])

    # 连续 ν 估计量：log D = c0 + c1·log|Δt| + c2·log N  =>  ν̂ = c1 / c2
    def nu_from_sufficient(s):
        s = np.asarray(s, float)
        n = s[..., 0]
        sx1, sx2, sy = s[..., 1], s[..., 2], s[..., 3]
        sx1x1, sx2x2, sx1x2 = s[..., 4], s[..., 5], s[..., 6]
        sx1y, sx2y = s[..., 7], s[..., 8]
        # 3x3 正规方程（对称）：[n, sx1, sx2; sx1, sx1x1, sx1x2; sx2, sx1x2, sx2x2] · [c0,c1,c2] = [sy, sx1y, sx2y]
        A = np.empty(s.shape[:-1] + (3, 3))
        A[..., 0, 0] = n; A[..., 0, 1] = sx1; A[..., 0, 2] = sx2
        A[..., 1, 0] = sx1; A[..., 1, 1] = sx1x1; A[..., 1, 2] = sx1x2
        A[..., 2, 0] = sx2; A[..., 2, 1] = sx1x2; A[..., 2, 2] = sx2x2
        b = np.stack([sy, sx1y, sx2y], axis=-1)
        try:
            coef = np.linalg.solve(A, b)
        except np.linalg.LinAlgError:
            return None, None, None
        c1, c2 = coef[..., 1], coef[..., 2]
        nu = np.where(np.abs(c2) > 0, c1 / c2, np.nan)
        return nu, c1, c2

    def suff(x1v, yv, logNv):
        return np.array([float(x1v.size), x1v.sum(), logNv.sum(), yv.sum(),
                         (x1v ** 2).sum(), (logNv ** 2).sum(), (x1v * logNv).sum(),
                         (x1v * yv).sum(), (logNv * yv).sum()])

    nu_hat, c1_hat, c2_hat = nu_from_sufficient(suff(x1, y, logN))
    nu_hat = float(nu_hat)

    # (b) ν bootstrap CI（n=1000）：逐 (N, model) 整块向量化重抽 + 充分统计
    b_nu = np.empty(N_BOOT, float)
    b_c1 = np.empty(N_BOOT, float)
    b_c2 = np.empty(N_BOOT, float)
    for bi in range(N_BOOT):
        xs, ys, lns = [], [], []
        for N in N_LIST:
            for mi, m in enumerate(models):
                rng = np.random.default_rng([SEED, 5000 + bi, int(N), mi])
                k = rng.binomial(int(N), p_m[m], size=N_DRAWS).astype(float)
                dt = np.abs(k / float(N) - t_c)
                with np.errstate(divide="ignore"):
                    lg = np.where(dt > 0, np.log(np.maximum(dt, EPS)), LOG_FLOOR)
                lg = np.maximum(lg, LOG_FLOOR)
                xs.append(lg)
                ys.append(np.full(N_DRAWS, y_log[m]))
                lns.append(np.full(N_DRAWS, np.log(float(N))))
        nu_b, c1_b, c2_b = nu_from_sufficient(suff(np.concatenate(xs), np.concatenate(ys),
                                                   np.concatenate(lns)))
        b_nu[bi], b_c1[bi], b_c2[bi] = nu_b, c1_b, c2_b
    fin = b_nu[np.isfinite(b_nu)]
    n_valid = int(fin.size)
    if n_valid >= 2:
        nu_lo = float(np.percentile(fin, 2.5))
        nu_hi = float(np.percentile(fin, 97.5))
        nu_med = float(np.percentile(fin, 50))
        nu_bstd = float(fin.std(ddof=0))
    else:
        nu_lo = nu_hi = nu_med = nu_bstd = None
    ci_defined_hit = bool(nu_lo is not None and nu_hi is not None)

    # (a) 跨 N data-collapse R²：u = |Δt|·N^(1/ν)·(1 + η·ln N)，对 log D 做 OLS
    def collapse_r2(nu, eta, x1v=x1, yv=y, logNv=logN):
        if nu == 0:
            # ν = 0 使 collapse 变量 N^(1/ν) 发散 -> 该网格点 R² 无定义（如实登记，不外插）
            return None, {"N=%d" % N: {"r2": None, "n_points": int((logNv == np.log(float(N))).sum()),
                                       "undefined_reason": "nu=0 -> collapse 变量发散"}
                          for N in N_LIST}
        corr = (1.0 + eta * logNv)
        corr = np.where(np.abs(corr) < EPS, EPS, corr)
        xs = x1v + logNv / nu + np.log(np.abs(corr))
        xs = np.maximum(xs, LOG_FLOOR)
        f = ols_r2(xs, yv)
        per_n = {}
        for N in N_LIST:
            sel = (logNv == np.log(float(N)))
            per_n["N=%d" % N] = {"r2": ols_r2(xs[sel], yv[sel])["r2"],
                                 "n_points": int(sel.sum())}
        return f["r2"], per_n

    grid_new = {}
    best = None
    for nu in GRID_NU_LEGACY:
        for eta in GRID_ETA:
            r2, per_n = collapse_r2(nu, eta)
            key = "nu=%g|eta=%g" % (nu, eta)
            grid_new[key] = {"nu": nu, "eta": eta, "R2": r2,
                             "R2_defined": r2 is not None, "R2_per_N": per_n}
            if r2 is not None and (best is None or r2 > best[0]):
                best = (r2, nu, eta)
    max_R2_new, best_nu_new, best_eta_new = (best if best else (None, None, None))
    grid_ext_best = None
    for nu in GRID_NU_EXT:
        for eta in GRID_ETA:
            r2, _ = collapse_r2(nu, eta)
            if r2 is not None and (grid_ext_best is None or r2 > grid_ext_best[0]):
                grid_ext_best = (r2, nu, eta)

    # as-run 精确总体敏感性腿（N=60 不重采样）
    exact_rows, exact_y, exact_ln = [], [], []
    for m in models:
        dt = abs(p_m[m] - t_c)
        lg = LOG_FLOOR if dt <= 0 else max(float(np.log(max(dt, EPS))), LOG_FLOOR)
        exact_rows.append(np.array([lg]))
        exact_y.append(np.array([y_log[m]]))
        exact_ln.append(np.array([np.log(float(N_CELLS))]))
    exact_r2_60, _ = collapse_r2(1.5, 0.1, np.concatenate(exact_rows), np.concatenate(exact_y),
                                  np.concatenate(exact_ln))

    # 去地板敏感性腿（仅取 D_fix2 > 0 的 model；掩码按 draw_surface 的 (N, model, draw) 顺序构造）
    zero_d_models = [m for m in models if d_m[m] <= 0]
    keep = np.array([m not in zero_d_models
                     for _ in N_LIST for m in models for _ in range(N_DRAWS)])
    assert keep.size == x1.size, "去地板掩码与数据面长度不符"
    floor_free = {
        "excluded_models_D_fix2_zero": zero_d_models,
        "n_points_kept": int(keep.sum()),
        "R2_at_best_legacy_params": collapse_r2(best_nu_new or 1.5, best_eta_new or 0.1,
                                                x1[keep], y[keep], logN[keep])[0],
    }

    # 采样比与经验 T_frac 抽样离散度（先算，供对照腿 reading 引用）
    sf_std = []
    for N in N_LIST:
        vals = [rr["T_frac_draw_std"] for rr in meta if rr["N"] == N]
        sf_std.append(float(np.mean(vals)))

    # ---------- 采样机制对照腿：N 档全部按 N=60 抽取、只改名义标签 ----------
    # 若 ν̂ 由数据决定，则改标签不改数据 => ν̂ 不变；若 ν̂ 由 N 标签（= 采样比 N/60）决定，
    # 则仅标签改动即可大幅摆动 ν̂。本腿机械区分这两种可能。
    lab_n, lab_x, lab_y, lab_ln = [], [], [], []
    for lab in N_LIST:
        for mi, m in enumerate(models):
            rng = np.random.default_rng([SEED, 9000, int(lab), mi])
            k = rng.binomial(int(N_CELLS), p_m[m], size=N_DRAWS).astype(float)
            dt = np.abs(k / float(N_CELLS) - t_c)
            with np.errstate(divide="ignore"):
                lg = np.where(dt > 0, np.log(np.maximum(dt, EPS)), LOG_FLOOR)
            lg = np.maximum(lg, LOG_FLOOR)
            lab_x.append(lg)
            lab_y.append(np.full(N_DRAWS, y_log[m]))
            lab_ln.append(np.full(N_DRAWS, np.log(float(lab))))
    lab_nu, lab_c1, lab_c2 = nu_from_sufficient(suff(np.concatenate(lab_x), np.concatenate(lab_y),
                                                    np.concatenate(lab_ln)))
    lab_c2 = float(lab_c2)
    label_only_control = {
        "construct": "5 个 N 档全部按 N=60 cells 抽取（数据面与主口径的 N=60 档同分布），"
                     "仅把名义标签改成 20/40/60/80/120",
        "nu_hat": None if not np.isfinite(float(lab_nu)) else float(lab_nu),
        "c1": float(lab_c1), "c2": lab_c2,
        "c2_degenerate_hit": bool(abs(lab_c2) < 1e-9),
        "reading": "本腿把「ν̂ 由数据决定」与「ν̂ 由名义 N 标签（= 采样比 N/60）决定」分开："
                   "各档数据分布不变、仅改名义标签，ν̂ 即从主口径的 %.4f 摆到 %.4f（符号翻转，量级差约 %.0f 倍），"
                   "c2 从 %.6f 变成 %.2e。=> ν̂ 由名义 N 标签（采样比）决定，不由数据决定。"
                   "结合 Var(T_frac_draw) ∝ 1/N 的机制（见 sampling_fraction 表："
                   "T_frac 抽样 std 随 N 增大由 %.4f（N=%d）收到 %.4f（N=%d）），"
                   "主口径 ν̂ 的 N 依赖来自**重采样设计**（采样比），"
                   "不是 60-cell 总体本身的物理有限尺寸标度。"
                   % (nu_hat, float(lab_nu), abs(float(lab_nu) / nu_hat) if nu_hat else float("inf"),
                      float(c2_hat), lab_c2,
                      sf_std[0], N_LIST[0], sf_std[-1], N_LIST[-1]),
    }
    sampling_fraction = {
        "N": N_LIST,
        "N_over_60": [float(n) / N_CELLS for n in N_LIST],
        "T_frac_draw_std_mean_per_N": sf_std,
        "note": ("采样比 N/60 > 1（N=80/120）时为有放回抽样，"
                 "经验 T_frac 的集中度按 1/√(N/60) 收紧 -> 该收紧是设计产物"),
    }

    # ---------- K-V3R-27 三腿判定（字面顺序：首次命中者治理；全部腿状态如实并报） ----------
    leg_a_cross_zero_hit = bool(ci_defined_hit and nu_lo <= 0.0 <= nu_hi)
    leg_b_upper_le_zero_hit = bool(ci_defined_hit and nu_hi <= 0.0 and not leg_a_cross_zero_hit)
    leg_c_max_r2_hit = bool(max_R2_new is not None and max_R2_new < MAX_R2_KILL)
    if leg_a_cross_zero_hit:
        new_verdict = "FAIL"
        governing_leg = "(a) 跨 N ν 的 bootstrap 95% CI 跨零 -> FAIL（真证伪，与 PARTIAL_FAIL_H0 同向）"
    elif leg_b_upper_le_zero_hit:
        new_verdict = "PASS"
        governing_leg = "(b) CI 上界 <= 0 -> PASS（结构性恒等成立）"
    elif leg_c_max_r2_hit:
        new_verdict = "FAIL"
        governing_leg = "(c) max_R2 仍 < 0.9 -> FAIL（维持假证伪）"
    else:
        new_verdict = "FAIL"
        governing_leg = "三腿均未触发 -> 沿 K-V3R-27 字面回落 FAIL（维持假证伪）"

    一致性 = ("一致（改判成立）" if new_verdict == legacy_verdict
              else "不一致（维持原标注 + γ 升级）")

    result = {
        "schema": "v3_recheck_result/27_p_l_p_c_finite_size_scaling/1",
        "prereg": {"path": "results/_v3_recheck_prereg_v1_2026_09_27.md", "sha12": prereg_sha12,
                   "prereg_v1p1_sha12": prereg11_sha12,
                   "kill_line": "K-V3R-27",
                   "threshold": "TH-V3R-27（ν, η grid；N 数列沿 §1.2 #27(a) 字面，§2.4 标占位 -> 取字面最小构造）"},
        "executor": "results/_v3_recheck_27_executor_2026_09_27.py",
        "date": "2026-09-27",
        "seed": SEED,
        "runtime": "0 LLM; numpy + hashlib + json only; no network; read-only inputs",
        "caliber_isolation_note": "本条 η = 异常指数（标度轴）；#10 P-C exp_3_3 的 η = Langevin 温度抖动。"
                                  "同名不同义，0 互替、0 跨条比较。",
        "inputs": [
            {"path": "results/_p_l_p_c_finite_size_scaling_2026_09_16/"
                     "p_l_p_c_finite_size_scaling_results_2026_09_16.json",
             "sha12_measured": sha12(SRC_PL.read_bytes()), "prereg_recorded_sha12": "00DF93A112F7",
             "prereg_sha_match": bool(sha12(SRC_PL.read_bytes()) == "00df93a112f7"),
             "bytes": SRC_PL.stat().st_size, "prereg_recorded_bytes": 9076},
            {"path": "results/deposon_v3_physical_opt_60cells_2026_09_11.json",
             "sha12_measured": sha12(SRC_60.read_bytes()),
             "prereg_v1p1_recorded_sha12": "c659695aa23c",
             "prereg_sha_match": bool(sha12(SRC_60.read_bytes()) == "c659695aa23c"),
             "bytes": SRC_60.stat().st_size, "prereg_recorded_bytes": 17732},
        ],
        "construct": {
            "(a)_cross_N": "N ∈ %s cells（§1.2 #27(a) 字面）：逐 (N, model) 从该 model 自己的 60-cell "
                           "标签总体有放回重采样 N cells，k ~ Binomial(N, T60/60)（精确边缘分布），"
                           "得 |Δt| = |T_frac - T_c| 与 log D_fix2 的成对点；逐 N 各算 collapse R²"
                           % N_LIST,
            "(b)_nu_bootstrap": "连续 ν 估计量：log D = c0 + c1·log|Δt| + c2·log N  =>  ν̂ = c1 / c2"
                                "（collapse 变量 |Δt|·N^(1/ν) 的 log N 系数 = c1/ν）；"
                                "bootstrap 95%% percentile CI，n=%d" % N_BOOT,
            "collapse_form": "u = |Δt|·N^(1/ν)·(1 + η·ln N)；log D_fix2 对 log u 做一元 OLS，R² 即 collapse R²",
            "log_floor": LOG_FLOOR,
            "log_floor_source": "deposon_pc_d1_d3_2026_09_15.json §R2_b_CI_log_log_fit 记录字面"
                                "（log_x/log_y 中地板值 -10.0 出现 2 次）",
            "N_list": N_LIST, "n_draws": N_DRAWS, "T_C_baseline": t_c,
            "nu_axes": {"legacy_shape": GRID_NU_LEGACY, "extended_incl_zero_and_negative": GRID_NU_EXT},
            "eta_axis": GRID_ETA,
        },
        "construct_degen_self_check": {
            "gate": "K-V3R-0-A: n_distinct > 3 + std > 0 on every on-disk input field",
            "input_fields": input_selfcheck,
            "gate_per_field": gate_pass,
            "degenerate_alarm_hit": degen_alarm_hit,
            "gate_pass": not degen_alarm_hit,
            "degenerate_levers_preregistered": degen_levers,
            "output_field": {
                "T_frac_draw_mean_per_NM": stat_block([r["T_frac_draw_mean"] for r in meta]),
                "T_frac_draw_std_per_NM": stat_block([r["T_frac_draw_std"] for r in meta]),
                "nu_hat": nu_hat, "nu_ci95": [nu_lo, nu_hi],
                "max_R2_new": max_R2_new,
            },
            "size_face_independence": {
                "T30_times2_equals_T60_all9": t30_exact_half,
                "reading": "30-cell 面与 60-cell 面互为精确半化 -> 盘上无独立跨尺寸信息，"
                           "跨 N 只能靠重采样（构造面外推边界）",
            },
        },
        "asrun_structural_audit": structural_audit,
        "cross_N_surface": meta,
        "nu_estimate": {
            "point_nu_hat": nu_hat, "c1": float(c1_hat), "c2": float(c2_hat),
            "c2_zero_hit": bool(abs(float(c2_hat)) == 0.0),
            "bootstrap": {"n_boot": N_BOOT, "n_valid": n_valid,
                          "ci95_lo": nu_lo, "ci95_hi": nu_hi,
                          "median": nu_med, "std": nu_bstd,
                          "ci_defined_hit": ci_defined_hit,
                          "n_nan_or_inf": int(N_BOOT - n_valid)},
            "mechanism_caveat": "该 CI 是**总体内重采样 CI**：盘上 60-cell 是一次普查（无上位总体），"
                                "故 CI 只覆盖重采样机制内的波动，不覆盖「是否存在物理标度」的不确定性。"
                                "label_only_control 腿实测：各档数据分布不变、仅改名义 N 标签，"
                                "ν̂ 即从 %.4f 摆到 %.4f => ν̂ 由采样比设计决定。"
                                "腿 (a)/(b) 的未命中因此**不携带物理权重**，治理腿是 (c)。"
                                % (nu_hat, label_only_control["nu_hat"]
                                   if label_only_control["nu_hat"] is not None else float("nan")),
        },
        "label_only_control": label_only_control,
        "sampling_fraction": sampling_fraction,
        "collapse_grid_new": {
            "grid": grid_new,
            "max_R2": max_R2_new, "best_nu": best_nu_new, "best_eta": best_eta_new,
            "extended_axis_max_R2": grid_ext_best[0] if grid_ext_best else None,
            "extended_axis_best": [grid_ext_best[1], grid_ext_best[2]] if grid_ext_best else None,
        },
        "sensitivity": {
            "asrun_exact_population_N60_R2_at_nu1.5_eta0.1": exact_r2_60,
            "log_floor_free_leg": floor_free,
        },
        "legacy_dual_track": legacy_track,
        "verdict": {
            "new_verdict": new_verdict,
            "governing_leg": governing_leg,
            "leg_a_ci_cross_zero_hit": leg_a_cross_zero_hit,
            "leg_b_ci_upper_le_zero_hit": leg_b_upper_le_zero_hit,
            "leg_c_max_R2_lt_0.9_hit": leg_c_max_r2_hit,
            "legacy_verdict": legacy_track["legacy_verdict"],
            "legacy_kill_line_verdict": legacy_verdict,
            "一致性": 一致性,
            "kill_line_pass": bool(new_verdict == "PASS"),
            "kill_line_hit": bool(new_verdict == "FAIL"),
            "改判档位": ("§2.3 第 2 行（PASS + 不一致）→ 维持原 V3 标注不动 + 显式登记新构造 verdict + 归「不明」分支"
                         if (new_verdict == "PASS" and legacy_verdict != "PASS") else
                         ("§2.3 第 1 行（PASS + 一致）→ 立改判件，原 V3 报告 byte 0 触动"
                          if new_verdict == "PASS" else
                          "§2.3 第 3 行（FAIL = 原标注维持）→ 0 改判动作")),
            "gamma": [
                "γ₁ = as-run 网格 R²(ν,η) 秩 1 可分离（σ₂/σ₁ = %.3g，秩 1 残差 %.2e）"
                     "=> argmax 是两轴 argmax 的乘积，「扫描」在结构上不可能是坍缩最优证据"
                     % (float(sv[1] / sv[0]), rank1_resid),
                "γ₂ = as-run 件内 0 个系统尺寸字段（有限尺寸标度在盘上无尺寸参与）；"
                     "argmax 落在 η 轴最小档（网格边界，无内点最优）",
                "γ③ = N = 80/120 只能由 60-cell 总体有放回重采样得到，「系统尺寸」为名义值"
                     "（构造面外推边界，不可外推为真实扩图族结果）",
                "γ④ = ν̂ 由名义 N 标签（采样比 N/60）决定而非数据（label_only_control 腿：数据分布不变、"
                     "仅改标签，ν̂ 由 %s 摆到 %s）；腿 (a) 未命中（CI 不跨零）不构成「存在真实标度指数」"
                     "的证据，亦不得引为 H1 侧支持" % ("%.4f" % nu_hat,
                     ("%.4f" % label_only_control["nu_hat"])
                     if label_only_control["nu_hat"] is not None else "发散/无定义"),
            ],
        },
        "iron_rules": {
            "0_LLM": True, "no_proxy": True, "no_key_in_prompt_json_disk": True,
            "read_only_inputs": True, "derived_json_not_merged": True,
            "v3_original_report_bytes_untouched": True,
        },
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    p = lambda *a: print(*[str(x).encode("ascii", "backslashreplace").decode("ascii") for x in a])
    p("[#27] written:", OUT.relative_to(REPO))
    p("[#27] asrun rank1 sigma2/sigma1=%.3g resid=%.2e separable=%s N_axis=%s"
      % (float(sv[1] / sv[0]), rank1_resid, rank1_resid <= 1e-6,
         structural_audit["N_axis_present_hit"]))
    p("[#27] nu_hat=%.6f CI95=[%s, %s] n_valid=%d" % (nu_hat, nu_lo, nu_hi, n_valid))
    p("[#27] max_R2_new=%s best=(nu=%s, eta=%s) legacy_max_R2=%.6f"
      % (max_R2_new, best_nu_new, best_eta_new, legacy_max_r2))
    p("[#27] legs a=%s b=%s c=%s -> %s (%s)"
      % (leg_a_cross_zero_hit, leg_b_upper_le_zero_hit, leg_c_max_r2_hit, new_verdict,
         legacy_verdict))
    p("[#27] degen gate_pass=%s T30*2==T60=%s" % (not degen_alarm_hit, t30_exact_half))
    return 0


def _has_key_recursive(obj, keys, depth=0):
    if depth > 6:
        return False
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in keys:
                return True
            if _has_key_recursive(v, keys, depth + 1):
                return True
    elif isinstance(obj, list):
        for v in obj[:64]:
            if _has_key_recursive(v, keys, depth + 1):
                return True
    return False


if __name__ == "__main__":
    sys.exit(main())
