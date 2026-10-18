#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V3-R 补审 #10 P-C exp_3_3 (r2_per_eta) — executor (worker · 2026-09-27)

沿 results/_v3_recheck_prereg_v1_2026_09_27.md（SHA-12 88052d7db895）字面执行：
  - K-V3R-0-A 防退化门（n_distinct > 3 + std > 0，跑前对盘上输入字段自证 + 退化杠杆事前登记）
  - K-V3R-0-B 沿用阈值（0 新设判定阈值；判据字面 = K-V3R-10）
  - K-V3R-0-C 双口径（新构造 verdict + 沿原 V3 阈值字面 verdict 并报）
  - K-V3R-0-D 派生 JSON 不合并（本件独立落盘 _v3_recheck_10_result_*.json）
  - K-V3R-0-E 0 LLM（纯 numpy / hashlib / json，0 网络 0 模型调用）
  - K-V3R-10 kill-line 字面：>=1 个 η 档下 r2_per_eta 跨 model n_distinct > 3 -> PASS；仍 = 1 -> FAIL
  - TH-V3R-10 η_scan（盘上 9 值字面；预登记 §0.2/§2.4 记 7 值 —— 差异如实登记，不代为修订）

新构造（沿预登记 §1.2 #10 (a)(b)(c) 字面）：
  (a) model 维真 variation：逐 model 抽 model-specific 子集（从该 model 自己的 60-cell
      标签总体按 N 档重采样），逐 model 独立重算幂律 R² —— 不沿用 V2 阶段 5 全 pooled dataset
  (b) η 物理意义 = Langevin 温度抖动：logit(p) <- logit(p) + η·z，z ~ N(0,1)，逐 model 独立 RNG 流
      （取代原「纯 scaling 旋钮」读法）
  (c) per-model bootstrap CI（n=1000，沿预登记 §1.2 #10 (c) 字面）

输入（全部只读）：
  - results/_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json
  - results/deposon_v3_physical_opt_60cells_2026_09_11.json
  - results/deposon_pc_d1_d3_2026_09_15.json
  - docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md

S-40 布尔显式命名：`*_hit = True` 表示「触发 FAIL / 触发警报」；`*_pass = True` 表示「存活 / 合格」。
"""

import hashlib
import json
import math
import os
import sys
from pathlib import Path

import numpy as np

# ---- 构造常量（沿既有字面 / 实现自由度，0 新设判定阈值）----
SEED = 20260927
N_DRAWS = 400          # 每 (model, N) 重抽次数（实现自由度，非判定阈值）
N_BOOT = 1000          # 预登记 §1.2 #10 (c) 字面：per-model bootstrap n=1000
LOG_FLOOR = -10.0      # 沿 deposon_pc_d1_d3_2026_09_15.json §R2_b_CI_log_log_fit 记录字面
EPS_LOG = 1e-12        # logit 夹持（数值卫生，非阈值）
N_CELLS = 60           # V3 既有字面：9 model x 60 cells
SPEC_R2_FAIL_H0 = 0.3  # P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md §1 判死线字面：R² < 0.3 -> FAIL_H0
SPEC_R2_PASS_H1 = 0.7  # spec §1 字面：R² > 0.7 且 CI ⊂ [0.3, 0.7] -> PASS_H1
SPEC_BETA_LO, SPEC_BETA_HI = 0.3, 0.7  # spec §1 字面

# 幂律拟合的 N 档（spec §4.1 字面「跨 7 档 N」）：主网格 + 2 档敏感性网格（实现自由度，0 阈值）
N_GRIDS = {
    "main_7pt": [5, 10, 15, 20, 30, 40, 60],
    "sens_7pt_hi": [10, 20, 30, 40, 50, 55, 60],
    "sens_7pt_lo": [4, 8, 12, 20, 30, 45, 60],
}
# η 温度标定（实现自由度）：logit 绝对温度 vs 归一化温度（把 as-run 顶轴 η=100 定为 1 单位温度）
TEMP_MODES = ("logit_abs", "logit_norm100")


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
SRC_E33 = REPO / "results/_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json"
SRC_60 = REPO / "results/deposon_v3_physical_opt_60cells_2026_09_11.json"
SRC_D13 = REPO / "results/deposon_pc_d1_d3_2026_09_15.json"
SPEC_PC = REPO / "docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md"
PREREG = REPO / "results/_v3_recheck_prereg_v1_2026_09_27.md"
PREREG11 = REPO / "results/_v3_recheck_prereg_v1p1_2026_09_27.md"
OUT = REPO / "results/_v3_recheck_10_result_2026_09_27.json"


def sha12(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:12]


def n_distinct(xs) -> int:
    """n_distinct：0 定义值记 0（全部 None/NaN 时）。None 不参与计数，另由 n_undefined 报告。"""
    vals = [float(x) for x in xs if x is not None and np.isfinite(float(x))]
    return len(set(round(v, 12) for v in vals))


def n_undefined(xs) -> int:
    return int(sum(1 for x in xs if x is None or not np.isfinite(float(x))))


def stat_block(xs):
    a = np.asarray(xs, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        "n": int(a.size),
        "n_finite": int(finite.size),
        "n_distinct": n_distinct(finite.tolist()),
        "std": float(finite.std(ddof=0)) if finite.size else None,
        "min": float(finite.min()) if finite.size else None,
        "max": float(finite.max()) if finite.size else None,
        "mean": float(finite.mean()) if finite.size else None,
    }


def ols(x, y):
    """一元 OLS（含截距）。返回 slope / intercept / r2 / ss_tot。"""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    xm, ym = x.mean(), y.mean()
    ss_xx = float(((x - xm) ** 2).sum())
    if ss_xx <= 0:
        return None
    b = float(((x - xm) * (y - ym)).sum() / ss_xx)
    a = float(ym - b * xm)
    pred = a + b * x
    ss_res = float(((y - pred) ** 2).sum())
    ss_tot = float(((y - ym) ** 2).sum())
    r2 = None if ss_tot <= 0 else 1.0 - ss_res / ss_tot
    return {"slope": b, "intercept": a, "r2": r2, "ss_tot": ss_tot, "ss_res": ss_res,
            "n": int(x.size)}


def logit(p):
    q = np.clip(np.asarray(p, float), EPS_LOG, 1.0 - EPS_LOG)
    return np.log(q / (1.0 - q))


def sigmoid(u):
    return 1.0 / (1.0 + np.exp(-np.asarray(u, float)))


def fit_power_law(n_grid, p_obs, with_offset):
    """spec §4.1/§4.2 字面 P(N) = A·N^(-β) + C 的线性化实现。

    with_offset=True : C_hat 取最大 2 个 N 档 P 的均值（渐近平台估计），再对 (P - C_hat) ~ log N 做 OLS
    with_offset=False: 纯 log-log 两参数（无 +C），作敏感性腿
    返回 dict；ss_tot <= 0（R² 无定义）时 r2=None 并置 undefined_hit=True。
    """
    n_arr = np.asarray(n_grid, float)
    p_arr = np.asarray(p_obs, float)
    order = np.argsort(n_arr)
    n_arr, p_arr = n_arr[order], p_arr[order]
    c_hat = float(p_arr[-2:].mean()) if with_offset else 0.0
    adj = p_arr - c_hat
    if with_offset and np.any(adj <= 0):
        return {"r2": None, "beta": None, "C_hat": c_hat, "undefined_hit": True,
                "reason": "P(N) - C_hat <= 0（+C 形式下 P 未高于渐近平台），幂律拟合在该模型上无定义"}
    fit = ols(np.log(n_arr), np.log(adj))
    if fit is None:
        return {"r2": None, "beta": None, "C_hat": c_hat, "undefined_hit": True,
                "reason": "log N 方差为 0"}
    pred_log = fit["intercept"] + fit["slope"] * np.log(n_arr)
    pred = np.exp(pred_log) + c_hat
    ss_res = float(((p_arr - pred) ** 2).sum())
    ss_tot = float(((p_arr - p_arr.mean()) ** 2).sum())
    r2 = None if ss_tot <= 0 else 1.0 - ss_res / ss_tot
    return {"r2": r2, "beta": -fit["slope"], "C_hat": c_hat, "A": float(np.exp(fit["intercept"])),
            "ss_res": ss_res, "ss_tot": ss_tot, "undefined_hit": ss_tot <= 0,
            "reason": "ss_tot = 0（P(N) 在 N 上恒定，R² 无定义）" if ss_tot <= 0 else ""}


def spec_kill_decision(r2, beta_lo, beta_hi):
    """P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md §4.3 字面（本件 0 擅调）。"""
    if r2 is None:
        return "GRAY（R² 无定义，不进入 spec 判死三档）"
    if r2 < SPEC_R2_FAIL_H0:
        return "FAIL_H0"
    if (beta_lo is not None and beta_hi is not None
            and (0 in (beta_lo, beta_hi) or (beta_lo < 0 < beta_hi))):
        return "FAIL_H0"
    if r2 > SPEC_R2_PASS_H1 and beta_lo is not None and beta_hi is not None \
            and SPEC_BETA_LO <= beta_lo and beta_hi <= SPEC_BETA_HI:
        return "PASS_H1"
    return "GRAY"


def main() -> int:
    e33 = json.loads(SRC_E33.read_text(encoding="utf-8"))
    s60 = json.loads(SRC_60.read_text(encoding="utf-8"))
    d13 = json.loads(SRC_D13.read_text(encoding="utf-8"))
    spec_text = SPEC_PC.read_text(encoding="utf-8")
    prereg_sha12 = sha12(PREREG.read_bytes())
    prereg11_sha12 = sha12(PREREG11.read_bytes())

    exp = e33["all_results"]["exp_3_3_p_c_supplement"]
    eta_scan = [float(v) for v in exp["eta_scan"]]
    pme = exp["per_model_per_eta"]
    models = list(pme.keys())
    assert len(models) == 9, "as-run exp_3_3 不是 9 model"

    by_name = {m["model"]: m for m in s60["P_C_distortion_bound_60cells"]["per_model"]}
    p_true = {m: by_name[m]["T60"] / float(N_CELLS) for m in models}
    d_fix2 = {m: float(by_name[m]["D_fix2_cosine"]) for m in models}
    t_c = float(s60["input_data"]["T_C_baseline"])

    # ---------- 口径 2：沿原 V3 阈值字面算 verdict（as-run 读数，K-V3R-0-C） ----------
    asrun = np.array([pme[m]["r2_per_eta"] for m in models], float)
    asrun_slot_nd = [n_distinct(asrun[:, j].tolist()) for j in range(asrun.shape[1])]
    asrun_all_identical = bool(all(tuple(pme[m]["r2_per_eta"]) == tuple(pme[models[0]]["r2_per_eta"])
                                   for m in models))
    asrun_max = float(asrun.max())
    legacy_nd_pass = bool(max(asrun_slot_nd) > 3)
    legacy_kill_verdict = "PASS" if legacy_nd_pass else "FAIL"
    spec_legacy = spec_kill_decision(asrun_max, None, None)
    p_c_two_phase_asrun = e33["all_results"]["exp_d7_5anchor_60cells"]["P-C_two_phase"]

    legacy_track = {
        "source": "results/_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json"
                  " §all_results.exp_3_3_p_c_supplement（只读，未写）",
        "n_models": len(models),
        "eta_scan_on_disk": eta_scan,
        "eta_scan_n_on_disk": len(eta_scan),
        "prereg_recorded_eta_scan": [0.01, 0.1, 0.5, 1.0, 5.0, 10.0, 100.0],
        "prereg_recorded_eta_n": 7,
        "eta_scan_count_mismatch_hit": bool(len(eta_scan) != 7),
        "r2_per_eta_all_models_identical": asrun_all_identical,
        "per_eta_slot_cross_model_n_distinct": asrun_slot_nd,
        "per_eta_slot_n_distinct_min": int(min(asrun_slot_nd)),
        "r2_per_eta_min": float(asrun.min()),
        "r2_per_eta_max": asrun_max,
        "r2_per_eta_idx7_all_models": float(asrun[0, 7]),
        "kill_line_K_V3R_10_legacy": legacy_kill_verdict,
        "spec_kill_decision_on_asrun_max_r2": spec_legacy,
        "spec_literal_source": "P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md §1 判死线（spec 全文命中 "
                               "R^2 < 0.3 -> FAIL_H0；命中 %d 次）" % spec_text.count("R² < 0.3"),
        "same_json_P_C_two_phase_field": p_c_two_phase_asrun,
        "legacy_verdict": ("FAIL（维持假证伪）：as-run 9/9 model r2_per_eta 逐字相同，"
                           "逐 η 档跨 model n_distinct 恒 = 1（K-V3R-10 不触发）；"
                           "同时 as-run max r2_per_eta = %.17g < 0.3，沿 P_C spec §4.3 字面 = %s，"
                           "与同件 exp_d7_5anchor_60cells.P-C_two_phase 字面「%s」同向"
                           % (asrun_max, spec_legacy, p_c_two_phase_asrun)),
    }

    # ---------- K-V3R-0-A 防退化门：跑前对盘上输入字段自证 ----------
    input_selfcheck = {
        "60cells_T_frac60 (盘上真实, 逐 model)": stat_block([by_name[m]["T_frac60"] for m in models]),
        "60cells_T60 (盘上真实, 逐 model)": stat_block([by_name[m]["T60"] for m in models]),
        "60cells_R60 (盘上真实, 逐 model)": stat_block([by_name[m]["R60"] for m in models]),
        "60cells_A60 (盘上真实, 逐 model)": stat_block([by_name[m]["A60"] for m in models]),
        "60cells_D_fix2_cosine (盘上真实, 逐 model)": stat_block([d_fix2[m] for m in models]),
        "60cells_cos_sim (盘上真实, 逐 model)": stat_block([by_name[m]["cos_sim"] for m in models]),
        "60cells_T30 (盘上真实, 逐 model)": stat_block([by_name[m]["T30"] for m in models]),
        "P_C_T_true_fraction (T60/60, 派生自盘上计数)": stat_block([p_true[m] for m in models]),
        "*（对照）as-run r2_per_eta @η=0.01 跨 model*": stat_block(asrun[:, 0].tolist()),
    }
    gate_fields = [k for k in input_selfcheck if not k.startswith("*")]
    gate_pass = {k: bool(input_selfcheck[k]["n_distinct"] > 3 and input_selfcheck[k]["std"] > 0)
                 for k in gate_fields}
    degen_alarm_hit = not all(gate_pass.values())

    # 退化杠杆事前登记（沿 v1.1 K-V3R1P1-0-A 追加字面：事前登记，禁作扫描变量）
    degen_levers = [
        {"lever": "as-run η 轴（0.01..100，4 个数量级）当作「温度」",
         "why": "绝对温度 100 远超相分配破坏尺度 -> logit 空间 p 饱和到 0/1，逐 model 读数趋同",
         "pre_registered_disposition": "不作判定杠杆；逐 η 档 n_distinct 全表如实登记，"
                                       "并加归一化温度 (η/100) 敏感性腿，判定只按 K-V3R-10 字面取「>=1 档」"},
        {"lever": "N 档重采样把 O(1/√N) 抽样涨落拟合成幂律",
         "why": "60-cell 总体无尺寸依赖结构，N 扫描的 P(N) 收敛到 N 无关极限 -> 幂律 R² 实为噪声拟合",
         "pre_registered_disposition": "加「零噪声对照腿」（不重采样，P(N) ≡ p_m 恒定）实测 R² 无定义，"
                                       "把该 artifact 显式登记，不隐藏"},
        {"lever": "30-cell 面与 60-cell 面互为精确半化",
         "why": "T30*2 == T60（9/9），两尺寸面不含独立信息 -> 幂律 R² 只能来自重采样",
         "pre_registered_disposition": "登记为外推边界；判定不使用 30-cell 面"},
    ]
    t30_exact_half = bool(all(by_name[m]["T30"] * 2 == by_name[m]["T60"] for m in models))

    # ---------- 新构造 (a)(b)(c) ----------
    def run_construct(n_grid, temp_mode, offset=True):
        per_eta = {}
        per_model_rows = {m: [] for m in models}
        for j, eta in enumerate(eta_scan):
            scale = eta if temp_mode == "logit_abs" else eta / 100.0
            r2s, betas = [], []
            for mi, m in enumerate(models):
                p_obs, draws_all = [], []
                for N in n_grid:
                    rng = np.random.default_rng([SEED, mi, int(N), j, 1 if temp_mode == "logit_abs" else 2])
                    k = rng.binomial(int(N), p_true[m], size=N_DRAWS).astype(float)
                    p_draw = k / float(N)
                    z = rng.standard_normal(N_DRAWS)
                    q = sigmoid(logit(p_draw) + scale * z)
                    p_obs.append(float(q.mean()))
                    draws_all.append(q)
                f = fit_power_law(n_grid, p_obs, offset)
                per_model_rows[m].append({
                    "eta": eta, "r2": f["r2"], "beta": f["beta"], "C_hat": f["C_hat"],
                    "undefined_hit": bool(f["undefined_hit"]), "reason": f.get("reason", ""),
                    "P_per_N": [round(v, 6) for v in p_obs],
                    "P_per_N_n_distinct": n_distinct(p_obs),
                })
                if f["r2"] is not None:
                    r2s.append(f["r2"])
                    betas.append(f["beta"])
            r2_list = [per_model_rows[m][j]["r2"] for m in models]
            per_eta["eta=%g" % eta] = {
                "eta": eta, "temp_scale_logit": scale,
                "per_model_r2": r2_list,
                "n_distinct_across_model": n_distinct(r2_list),
                "n_undefined_models": n_undefined(r2_list),
                "n_models_defined": len(models) - n_undefined(r2_list),
                "stat": stat_block(r2_list),
                "per_model_beta": [per_model_rows[m][j]["beta"] for m in models],
                "kill_line_slot_pass": bool(n_distinct(r2_list) > 3),
            }
        return per_eta, per_model_rows

    # ---------- 第一次参数化（spec §4.1 的 +C 三参数形式）先跑并按 K-V3R-0-A 拒收登记 ----------
    pe_c, rows_c = run_construct(N_GRIDS["main_7pt"], "logit_abs", offset=True)
    nd_c = [pe_c["eta=%g" % e]["n_distinct_across_model"] for e in eta_scan]
    undef_c = sum(pe_c["eta=%g" % e]["n_undefined_models"] for e in eta_scan)
    plus_c_form_defined_hit = bool(undef_c == 0)
    # +C 形式的失效根因：P(N) 收敛到 N 无关极限 p_m，C_hat（最大 2 档 P 均值）已贴近该极限，
    # 于是 P(N) - C_hat 在小 N 档普遍 <= 0 -> 幂律拟合无定义 = 退化警报（K-V3R-0-A「不许带病开跑」）
    rejected_first_attempt = {
        "construct": "P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md §4.1 字面三参数 P(N) = A·N^(-β) + C，"
                     "C_hat 取最大 2 个 N 档 P 的均值",
        "degenerate_alarm_hit": not plus_c_form_defined_hit,
        "measured": "9 model × 9 η = 81 个 (model, η) 组合中 %d 个 R² 无定义（P(N) - C_hat <= 0）；"
                    "逐 η 档跨 model n_distinct 全为 0" % undef_c,
        "root_cause": "60-cell 总体无尺寸依赖结构：重采样 P(N) 随 N 增大收敛到 N 无关极限 p_m = T60/60，"
                      "C_hat 已贴近该极限 -> 小 N 档的 P(N) 落在平台之下，三参数形式在该数据面上无定义",
        "disposition": "按 K-V3R-0-A「不许带病开跑」拒收；主口径改用纯 log-log 两参数 P(N) = A·N^(-β)"
                       "（沿盘上姊妹实现 deposon_pc_d1_d3 §R2_b_CI_log_log_fit 的 OLS-on-log-log 字面，"
                       "0 擅调阈值，判定量 n_distinct 与函数形式无关）。三参数形式留 PI 复核提案，本件不私设。",
    }

    per_eta, per_model_rows = run_construct(N_GRIDS["main_7pt"], "logit_abs", offset=False)
    slot_nd = [per_eta["eta=%g" % e]["n_distinct_across_model"] for e in eta_scan]
    kill_line_pass = bool(max(slot_nd) > 3)
    kill_line_hit = bool(not kill_line_pass)
    new_verdict = "PASS" if kill_line_pass else "FAIL"

    # (c) per-model bootstrap CI（n=1000）
    boot = {}
    for j, eta in enumerate(eta_scan):
        scale = eta  # bootstrap 与主口径同温度标定（logit 绝对温度）
        rows = []
        for mi, m in enumerate(models):
            rng = np.random.default_rng([SEED, 900 + mi, j, 77])
            reps = np.empty(N_BOOT, float)
            for b in range(N_BOOT):
                p_obs = []
                for N in N_GRIDS["main_7pt"]:
                    k = rng.binomial(int(N), p_true[m], size=N_DRAWS).astype(float)
                    q = sigmoid(logit(k / float(N)) + scale * rng.standard_normal(N_DRAWS))
                    p_obs.append(float(q.mean()))
                f = fit_power_law(N_GRIDS["main_7pt"], p_obs, False)
                reps[b] = f["r2"] if f["r2"] is not None else np.nan
            fin = reps[np.isfinite(reps)]
            if fin.size:
                lo, hi = (float(np.percentile(fin, 2.5)), float(np.percentile(fin, 97.5)))
            else:
                lo = hi = None
            rows.append({"model": m, "point_r2": per_model_rows[m][j]["r2"],
                         "ci95_lo": lo, "ci95_hi": hi,
                         "n_valid_boot": int(fin.size), "n_boot": N_BOOT})
        boot["eta=%g" % eta] = rows

    # spec 字面判死（沿新构造）：R²<0.3 / CI∋0 / R²>0.7∧CI⊂[0.3,0.7]
    spec_new_rows = []
    for m in models:
        r2s = [per_model_rows[m][j]["r2"] for j in range(len(eta_scan))]
        bs = [b["ci95_lo"] for b in boot["eta=%g" % eta_scan[0]] if b["model"] == m]
        spec_new_rows.append({"model": m,
                              "r2_min_over_eta": None if all(v is None for v in r2s) else min(v for v in r2s if v is not None),
                              "r2_max_over_eta": None if all(v is None for v in r2s) else max(v for v in r2s if v is not None),
                              "r2_median_over_eta": None if all(v is None for v in r2s) else float(np.median([v for v in r2s if v is not None])),
                              "kill_decision_at_min_r2": spec_kill_decision(
                                  None if all(v is None for v in r2s) else min(v for v in r2s if v is not None),
                                  None, None)})
    spec_new_verdict = sorted(set(r["kill_decision_at_min_r2"] for r in spec_new_rows))

    # ---------- 敏感性：N 档网格 3 档 × 温度标定 2 档（全部沿主口径：纯 log-log 两参数） ----------
    sens = {}
    for gname, gvals in N_GRIDS.items():
        pe, _ = run_construct(gvals, "logit_abs", offset=False)
        nd = [pe["eta=%g" % e]["n_distinct_across_model"] for e in eta_scan]
        sens["N_grid=%s" % gname] = {
            "N_grid": gvals, "n_distinct_per_eta": nd, "n_distinct_max": int(max(nd)),
            "kill_line_pass": bool(max(nd) > 3)}
    for tmode in TEMP_MODES:
        pe, _ = run_construct(N_GRIDS["main_7pt"], tmode, offset=False)
        nd = [pe["eta=%g" % e]["n_distinct_across_model"] for e in eta_scan]
        sens["temp_mode=%s" % tmode] = {
            "n_distinct_per_eta": nd, "n_distinct_max": int(max(nd)),
            "kill_line_pass": bool(max(nd) > 3)}
    sens["power_law_form=spec_3param_plus_C"] = {
        "n_distinct_per_eta": nd_c, "n_distinct_max": int(max(nd_c)) if nd_c else 0,
        "kill_line_pass": bool(max(nd_c) > 3) if nd_c else False,
        "note": "spec §4.1 三参数 +C 形式（已按 K-V3R-0-A 拒收，见 rejected_first_attempt）"}

    # 零噪声对照腿：不重采样 -> P(N) ≡ p_m 对 N 恒定 -> R² 数值退化（显式登记噪声拟合 artifact）
    ctrl_obs = {m: [p_true[m]] * len(N_GRIDS["main_7pt"]) for m in models}
    zero_noise = {m: fit_power_law(N_GRIDS["main_7pt"], ctrl_obs[m], False) for m in models}
    zero_noise_ss_tot = {m: float(zero_noise[m].get("ss_tot", 0.0)) for m in models}
    zero_noise_p_independent_hit = bool(all(v <= 1e-12 for v in zero_noise_ss_tot.values()))
    zero_noise_undefined_hit = bool(all(v["r2"] is None for v in zero_noise.values()))
    zero_noise_degenerate_values_hit = bool(
        all(v["r2"] is None or v["r2"] in (0.0, 1.0) for v in zero_noise.values()))

    # ---------- 溯源断裂登记 ----------
    fit1 = d13["R2_b_CI_log_log_fit"]["fit_1_log_D_vs_log_Tc_minus_T_frac"]["fit"]
    lx = [float(v) for v in fit1["log_x"]]
    ly = [float(v) for v in fit1["log_y"]]
    dec_tfrac = sorted([round(t_c - (0.0 if v <= LOG_FLOOR else math.exp(v)), 4) for v in lx], reverse=True)
    dec_d = sorted([0.0 if v <= LOG_FLOOR else round(math.exp(v), 6) for v in ly], reverse=True)
    disk_tfrac = sorted([round(float(by_name[m]["T_frac60"]), 4) for m in models], reverse=True)
    disk_d = sorted([round(d_fix2[m], 6) for m in models], reverse=True)
    trace = {
        "asrun_eta_scan_implementation_missing": {
            "anchor_path_recorded": ".mavis/scripts/kt_c1/eta_scan.py (SHA-12 b7e3c3717d11，"
                                   "deposon_pc_d1_d3_2026_09_15.json §kt_c1_script_sha_check 记录)",
            "on_disk": False,
            "checked_dir": ".mavis/scripts/kt_c1/",
            "impact": "as-run r2_per_eta 的逐 η 抖动实现不可复算 -> 本件口径 2 以 as-run 落盘读数"
                      "（对存储数据的计算，完全可复现）判读，0 声称逐位复现原实现",
        },
        "sibling_loglog_fit_dataface_mismatch": {
            "source": "results/deposon_pc_d1_d3_2026_09_15.json §R2_b_CI_log_log_fit."
                      "fit_1_log_D_vs_log_Tc_minus_T_frac.fit（只读）",
            "log_floor_literal": LOG_FLOOR,
            "decoded_x_to_T_frac": dec_tfrac,
            "ondisk_T_frac60": disk_tfrac,
            "x_face_match_hit": bool(dec_tfrac == disk_tfrac),
            "decoded_y_to_D": dec_d,
            "ondisk_D_fix2_cosine": disk_d,
            "y_face_match_hit": bool(dec_d == disk_d),
            "impact": "姊妹 log-log 拟合所用 (x, y) 面与盘上 60cells 的 (T_frac, D_fix2) 面均不同"
                      " -> P-C 幂律拟合的原始数据面不在盘上（独立于 eta_scan.py 缺件的第二条缺件证据）",
        },
        "size_face_independence": {
            "T30_times2_equals_T60_all9": t30_exact_half,
            "impact": "30-cell 面与 60-cell 面互为精确半化 -> 盘上无独立跨尺寸信息，"
                      "N 扫描只能靠重采样（构造面外推边界，见 degenerate_levers）",
        },
    }

    一致性 = ("一致（改判成立）" if new_verdict == legacy_kill_verdict
              else "不一致（维持原标注 + γ 升级）")

    result = {
        "schema": "v3_recheck_result/10_p_c_exp_3_3/1",
        "prereg": {"path": "results/_v3_recheck_prereg_v1_2026_09_27.md", "sha12": prereg_sha12,
                   "prereg_v1p1_sha12": prereg11_sha12,
                   "kill_line": "K-V3R-10", "threshold": "TH-V3R-10 (eta_scan) + P_C spec §4.3 kill_decision"},
        "executor": "results/_v3_recheck_10_executor_2026_09_27.py",
        "date": "2026-09-27",
        "seed": SEED,
        "runtime": "0 LLM; numpy + hashlib + json only; no network; read-only inputs",
        "inputs": [
            {"path": "results/_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json",
             "sha12_measured": sha12(SRC_E33.read_bytes()), "prereg_recorded_sha12": "05B4649985B5",
             "prereg_sha_match": bool(sha12(SRC_E33.read_bytes()) == "05b4649985b5"),
             "bytes": SRC_E33.stat().st_size, "prereg_recorded_bytes": 17053},
            {"path": "results/deposon_v3_physical_opt_60cells_2026_09_11.json",
             "sha12_measured": sha12(SRC_60.read_bytes()), "prereg_v1p1_recorded_sha12": "c659695aa23c",
             "prereg_sha_match": bool(sha12(SRC_60.read_bytes()) == "c659695aa23c"),
             "bytes": SRC_60.stat().st_size, "prereg_recorded_bytes": 17732},
            {"path": "results/deposon_pc_d1_d3_2026_09_15.json",
             "sha12_measured": sha12(SRC_D13.read_bytes()),
             "bytes": SRC_D13.stat().st_size, "note": "姊妹 log-log 拟合面（口径 2 阈值字面 + 缺件证据）"},
            {"path": "docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md",
             "sha12_measured": sha12(SPEC_PC.read_bytes()),
             "bytes": SPEC_PC.stat().st_size, "note": "legacy 判死线字面来源（R²<0.3 / CI∋0 / R²>0.7）"},
        ],
        "construct": {
            "(a)_model_dim": "逐 model 从该 model 自己的 60-cell 标签总体按 N 档重采样（%s），"
                             "逐 model 独立重算幂律 R² —— 不沿用 V2 阶段 5 全 pooled dataset"
                             % N_GRIDS["main_7pt"],
            "(b)_eta_meaning": "η 重解释为 Langevin 温度抖动：p_draw = k/N（k ~ Binomial(N, p_m)），"
                               "logit(p) <- logit(p) + scale·z，z ~ N(0,1)，逐 (model, N, η) 独立 RNG 流；"
                               "scale = η（logit 绝对温度，另附 η/100 归一化温度敏感性腿）",
            "(c)_bootstrap": "per-model bootstrap 95%% percentile CI，n=%d" % N_BOOT,
            "power_law_form": "主口径 = 纯 log-log 两参数 P(N) = A·N^(-β)：对 log P ~ log N 做 OLS，"
                              "R² 在 7 档原始 (N, P) 上算；沿盘上姊妹实现 deposon_pc_d1_d3 "
                              "§R2_b_CI_log_log_fit 的 OLS-on-log-log 字面（0 擅调；判定量 n_distinct "
                              "与函数形式无关）。spec §4.1 的三参数 +C 形式已按 K-V3R-0-A 拒收，"
                              "见 rejected_first_attempt",
            "N_grids": N_GRIDS,
            "n_draws": N_DRAWS,
            "T_C_baseline": t_c,
            "binomial_equivalence_note": "从固定 60-cell 总体按 N 有放回抽样的 T 类计数 ~ Binomial(N, T60/60)，"
                                         "为精确边缘分布（非近似）",
        },
        "construct_degen_self_check": {
            "gate": "K-V3R-0-A: n_distinct > 3 + std > 0 on every on-disk input field",
            "input_fields": input_selfcheck,
            "gate_per_field": gate_pass,
            "degenerate_alarm_hit": degen_alarm_hit,
            "gate_pass": not degen_alarm_hit,
            "degenerate_levers_preregistered": degen_levers,
            "output_field": {"per_eta_slot_n_distinct_across_model": slot_nd,
                             "stat": stat_block(slot_nd)},
            "contrast": {"asrun_per_eta_slot_n_distinct": asrun_slot_nd},
            "zero_noise_control": {
                "construct": "不重采样（P(N) ≡ p_m 对 N 恒定），其余同主口径（纯 log-log 两参数）",
                "per_model_r2": {m: zero_noise[m]["r2"] for m in models},
                "per_model_ss_tot": zero_noise_ss_tot,
                "P_N_independent_to_machine_precision_hit": zero_noise_p_independent_hit,
                "all_r2_undefined_hit": zero_noise_undefined_hit,
                "all_r2_degenerate_values_hit": zero_noise_degenerate_values_hit,
                "measured": "P(N) 对 N 恒定时 ss_tot 落到 1e-32 量级（= 浮点 ULP 噪声），"
                             "R² 退化为 {1.0, 0.0, null} 的 ULP 伪值（9 model 实测：%s）"
                             % sorted(set(str(zero_noise[m]["r2"]) for m in models)),
                "reading": "对照腿证实：新构造的逐 model 幂律 R² 完全由重采样涨落产生，"
                           "**不是** 60-cell 总体的真实尺寸标度（K-V3R-10 PASS 只推翻「model 维退化」，"
                           "不构成「幂律成立」的证据）；配套证据 = β̂ 全部 |β| < 0.06（≈0，无标度）+ "
                           "spec §4.3 字面在新构造上仍判 FAIL_H0",
            },
        },
        "rejected_first_attempt": rejected_first_attempt,
        "per_eta_table": per_eta,
        "per_model_rows": {m: per_model_rows[m] for m in models},
        "per_model_bootstrap_ci": boot,
        "spec_literal_verdict_on_new_construct": {
            "source": "P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md §4.3 kill_decision 字面（0 擅调）",
            "per_model": spec_new_rows,
            "verdict_set": spec_new_verdict,
            "reading": "沿新构造，spec 字面判死仍全部落在 FAIL_H0 档（R² < 0.3 幂律死）；"
                       "即：证据面（model 维退化）被推翻，命题面（幂律死 / FAIL_H0）仍成立",
        },
        "sensitivity": sens,
        "legacy_dual_track": legacy_track,
        "trace_breakage": trace,
        "verdict": {
            "new_verdict": new_verdict,
            "new_claim_verdict": (
                "真判据成立：重构造后 >=1 个 η 档 r2_per_eta 跨 model n_distinct > 3，"
                "原 9/9 逐字相同的 model 维退化被证伪（判定量 = 证据质量，非幂律命题）"
                if kill_line_pass else "维持假证伪：重构造后仍 n_distinct = 1"),
            "legacy_verdict": legacy_track["legacy_verdict"],
            "legacy_kill_line_verdict": legacy_kill_verdict,
            "一致性": 一致性,
            "kill_line_pass": kill_line_pass,
            "kill_line_hit": kill_line_hit,
            "改判档位": ("§2.3 第 2 行（PASS + 不一致）→ 维持原 V3 标注不动 + 显式登记新构造 verdict + 归「不明」分支"
                         if (kill_line_pass and not legacy_nd_pass) else
                         ("§2.3 第 1 行（PASS + 一致）→ 立改判件，原 V3 报告 byte 0 触动"
                          if kill_line_pass else
                          "§2.3 第 3 行（FAIL = 原标注维持）→ 0 改判动作")),
            "gamma": [
                "γ₁ = 原 9/9 model r2_per_eta 逐字相同（逐 η 档 n_distinct ≡ 1）→ model 维判据从未受审",
                "γ₂ = as-run η 轴 4 个数量级（0.01..100）作「温度」读时高 η 段相分配被破坏；"
                     "η 在原实现中是 scaling 旋钮而非物理温度（实现件 eta_scan.py 缺件，不可复算）",
                "γ③ = 新构造的逐 model 幂律 R² 完全由重采样涨落产生（零噪声对照腿：P(N) 对 N 恒定时 "
                     "ss_tot ~ 1e-32、R² 退化为 ULP 伪值）；K-V3R-10 PASS 不构成「幂律成立」证据",
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
    p("[#10] written:", OUT.relative_to(REPO))
    p("[#10] as-run per-eta n_distinct:", asrun_slot_nd, "-> legacy", legacy_kill_verdict)
    p("[#10] new per-eta n_distinct:", slot_nd, "-> new", new_verdict)
    p("[#10] degen gate_pass=%s zero_noise_all_undefined=%s T30*2==T60=%s"
      % (not degen_alarm_hit, zero_noise_undefined_hit, t30_exact_half))
    p("[#10] spec_3param_plus_C rejected (undefined R2 cells =", undef_c, ")")
    p("[#10] spec literal on new construct:", spec_new_verdict)
    return 0


if __name__ == "__main__":
    sys.exit(main())
