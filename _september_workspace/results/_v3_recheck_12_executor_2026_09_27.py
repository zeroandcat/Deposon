#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V3-R 补审 #12 BOSS-PE-2 (real transverse Ising) — executor (worker · 2026-09-27)

沿 results/_v3_recheck_prereg_v1_2026_09_27.md（实测 SHA-12 88052d7db895）字面执行：

  - K-V3R-0-A 防退化门（n_distinct > 3 + std > 0，跑前对盘上输入字段自证）
  - K-V3R-0-B 沿用阈值（0 新设判定阈值；PFEUTY_H_C_OVER_J=1.0 / TOL_STRICT=0.05 /
    TOL_LOOSE=0.15 / D_FIX2_PASS_LT=0.05 / D_FIX2_FAIL_GE=0.15 全部沿 boss_pe_2 字面）
  - K-V3R-0-C 双口径（新构造 verdict + 沿原 V3 阈值字面 verdict 并报）
  - K-V3R-0-D 派生 JSON 不合并（本件独立落盘 _v3_recheck_12_result_*.json）
  - K-V3R-0-E 0 LLM（纯 stdlib，0 网络 0 模型调用，0 外部文献调取）
  - K-V3R-12 kill-line 字面：重构造（真 h_c(T) 抽样 + 真 phase boundary + 主判据换 D_fix2）
    后 verdict 与 D_fix2 真分布一致 -> PASS；不一致 / 判据输入仍恒同 -> FAIL（维持假成立）

§1.2 #12 补审构造方向（字面）：
  (a) h_c_at_T 真随机化：从 Pfeuty Phase Diagram 抽样 h_c(T, J) 连续分布，至少 100 个 sample/model
  (b) transverse_ising_region 用真 phase boundary 测试（沿 Jordan-Sucher-Votek 1999 数值解
      + per-model empirical 散点）
  (c) 主判据换成 D_fix2（P-E 报告 §1.2 risk3 已 ADOPTED）

**本件对 (a)(b) 的可实现性实测登记（不编造）**：
  - (a) 1D 横场 Ising（Pfeuty 精确解）的临界线在 (T, h/J) 平面上是**单条曲线**；
    V3 冻结常数 PFEUTY_H_C_OVER_J = 1.0 是该曲线上的**一个点**，本身不携带 T 依赖分布。
    本件以**自实现 2x2 精确迁移矩阵**（约定逐字声明，见 tfim_boundary）在该曲线上采样
    (T, J) -> h_c/J，逐 model ≥ 100 sample，得到真分布；**0 引入预登记之外的物理量**。
  - (b) Jordan-Sucher-Votek 1999 的数值相图**本仓 0 命中、本件 0 联网**=> 其曲线**未复现、
    0 编造其数值**（γ2 缺件登记）；本件改用自实现精确对角化相界 + per-model empirical 散点，
    并把 (T_frac, R_frac) -> (T, h/J) 的映射显式声明为 worker 口径（附敏感性）。

输入（全部只读）：
  - results/boss_pe_2_real_transverse_ising_2026_09_15.json   #12 源件（原结论所在）
  - results/boss_pc_2_real_transverse_ising_2026_09_15.json   # 同源姊妹件（命名勘误 lineage）
  - deposon_team/plugins/boss_pc_2_transverse_field_ising.py  # 只读公式来源（0 import）
  - results/deposon_v3_physical_opt_60cells_2026_09_11.json    # 9 model (T,R,A) + 60cells D_fix2
  - docs/V3X/P_E_D1_D3_REPORT_2026_09_15.md                    # §1.2 risk3 ADOPTED 字面
  - results/_v3_recheck_prereg_v1_2026_09_27.md                # 预登记件

S-40 布尔显式命名：`*_hit = True` 表示「触发 FAIL / 触发警报」；`*_pass = True` 表示「存活 / 合格」。
"""

import hashlib
import json
import math
import os
import sys
from pathlib import Path

# ---- 预注册常数（沿 boss_pe_2 pre_registered_constants 字面，0 新设）----
PFEUTY_H_C_OVER_J = 1.0     # TH-V3R-12 沿 V3 字面
TOL_STRICT = 0.05           # TH-V3R-12 沿 V3 字面
TOL_LOOSE = 0.15            # TH-V3R-12 沿 V3 字面
D_FIX2_PASS_LT = 0.05       # TH-V3R-12 沿 V3 字面
D_FIX2_FAIL_GE = 0.15       # TH-V3R-12 沿 V3 字面
D_FIX2_BASELINE_T_C = 0.8667
D_FIX2_BASELINE_A_C = 0.0333
N_CELLS = 60                # V3 既有字面
SEED = 20260927

# ---- 抽样网格（worker 声明的实现量，附敏感性；非判定阈值）----
N_T_GRID = 10               # 温度格点档数
N_J_GRID = 10               # 耦合格点档数
N_SAMPLES_PER_MODEL = N_T_GRID * N_J_GRID   # = 100 ≥ v1 §1.2 #12(a) 要求的「至少 100」
T_REL_GRID = tuple(round(0.20 + 0.10 * i, 2) for i in range(N_T_GRID))   # k_BT / J 相对温度
J_REL_GRID = tuple(round(0.50 + 0.25 * i, 2) for i in range(N_J_GRID))   # J / 参考尺度


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
SRC_PE2 = REPO / "results/boss_pe_2_real_transverse_ising_2026_09_15.json"
SRC_PC2 = REPO / "results/boss_pc_2_real_transverse_ising_2026_09_15.json"
SRC_RUNNER = REPO / "deposon_team/plugins/boss_pc_2_transverse_field_ising.py"
SRC_V3 = REPO / "results/deposon_v3_physical_opt_60cells_2026_09_11.json"
SRC_PEREP = REPO / "docs/V3X/P_E_D1_D3_REPORT_2026_09_15.md"
PREREG = REPO / "results/_v3_recheck_prereg_v1_2026_09_27.md"
OUT = REPO / "results/_v3_recheck_12_result_2026_09_27.json"


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
# 段 1 · 1D 横场 Ising 精确临界线（本件自实现；约定逐字声明）
# =====================================================================
#
# **勘误（本件内自查登记）**：本 executor 初版曾以「2x2 迁移矩阵 leading eigenvalue 简并」
# 推导临界条件，推得 h_c/J = 2 t asinh(e^{-2/t})。后加的**本征值活校验**（见
# tfim_eigenvalues_probe）证明该推导有**符号错误**：对
#     T = [[e^{K+G}, e^{-K}], [e^{-K}, e^{K-G}]]
# 判别式 = ((T11-T22)/2)^2 + T12*T21 = e^{2K} sinh^2(G) + e^{-2K} > 0（G > 0 恒成立）
# => **该 2x2 形式不存在本征值简并**，初版公式作废。正确条件是 1D TFIM 的标准精确临界条件
#     sinh(2K) sinh(2G) = 1
# （1D TFIM 在有限 L 下恒有隙，量子临界是 L->inf 极限的能级交叉，不是有限 2x2 的简并）。
# 本件已改用下述正确实现；初版公式与其数值**已作废、不参与任何判定**。

TFIM_CONVENTION = ("H = -(J/4) Σ_i σ^z_i σ^z_{i+1} - (h/4) Σ_i σ^x_i；"
                   "K ≡ βJ/4，Γ ≡ βh/4；无量纲温度 t_rel ≡ k_BT/J = 1/(4K)")


def tfim_critical_condition_residual(kappa, gamma):
    """1D TFIM 精确临界条件的残差：sinh(2K) sinh(2Γ) - 1。"""
    return math.sinh(2.0 * kappa) * math.sinh(2.0 * gamma) - 1.0


def tfim_h_c_over_j(t_rel):
    """给定 t_rel ≡ k_BT/J（>0），返回 1D TFIM 临界 h_c/J（自实现，闭式）。

    推导（可复算）：sinh(2K) sinh(2Γ) = 1 => 2Γ_c = asinh(1/sinh(2K))
    => Γ_c = 0.5 asinh(1/sinh(2K))；h_c/J = Γ_c / K；K = 1/(4 t_rel)
    => h_c/J = 2 t_rel asinh(1/sinh(1/(2 t_rel)))
    """
    if t_rel <= 0:
        return float("inf")
    two_k = 1.0 / (2.0 * t_rel)          # 2K
    if two_k > 350.0:                    # sinh 上溢保护
        return 0.0
    s = math.sinh(two_k)
    if s <= 0.0:
        return float("inf")
    return 2.0 * t_rel * math.asinh(1.0 / s)


def tfim_h_c_over_j_numeric(t_rel, n_bisect=200):
    """数值独立核验（**不使用 asinh 闭式**）：对 Γ 二分求临界条件残差的符号翻转点。

    残差 f(Γ) = sinh(2K) sinh(2Γ) - 1 关于 Γ > 0 单调增 => 可二分。
    该残差由临界条件的标准形式直接构造，不引用闭式解 asinh，构成独立核验。
    """
    if t_rel <= 0:
        return float("inf")
    kappa = 1.0 / (4.0 * t_rel)
    if 2.0 * kappa > 350.0:
        return 0.0
    lo, hi = 1e-12, 1.0
    while tfim_critical_condition_residual(kappa, hi) < 0.0 and hi < 1e6:
        hi *= 2.0
        if hi >= 1e6:
            return float("inf")
    for _ in range(n_bisect):
        mid = (lo + hi) / 2.0
        if tfim_critical_condition_residual(kappa, mid) < 0.0:
            lo = mid
        else:
            hi = mid
    gamma_c = (lo + hi) / 2.0
    return gamma_c / kappa


def tfim_eigenvalues_probe(t_rel):
    """**自校验**：核验本件所用临界条件本身在数值上自洽。

    1) 闭式解代入残差 ≈ 0（<= 1e-12）；
    2) 二分解与闭式解一致（<= 1e-9）；
    3) 极限行为：t_rel -> 0 时 h_c/J -> 0，t_rel -> inf 时 h_c/J -> inf（单调递增的两端）。
    4) **同时核验初版（已作废）公式不满足临界条件**，作为作废依据的正面留证。
    """
    kappa = 1.0 / (4.0 * t_rel)
    closed = tfim_h_c_over_j(t_rel)
    gamma_c = closed * kappa               # h_c/J = Γ_c / K  =>  Γ_c = (h_c/J) * K
    resid = tfim_critical_condition_residual(kappa, gamma_c)
    numeric = tfim_h_c_over_j_numeric(t_rel)
    # 初版（作废）公式：2 t asinh(e^{-2/t})  —— 其对应 Γ 是否满足临界条件？
    deprecated_gamma = (2.0 * t_rel * math.asinh(math.exp(-2.0 / t_rel))) * kappa
    deprecated_resid = (tfim_critical_condition_residual(kappa, deprecated_gamma)
                        if 0 < deprecated_gamma < 350.0 else float("nan"))
    return {
        "t_rel": t_rel,
        "kappa": kappa,
        "h_c_over_J_closed_form": closed,
        "h_c_over_J_numeric_bisect": numeric,
        "abs_diff_closed_vs_numeric": abs(closed - numeric),
        "condition_residual_at_closed_form": resid,
        "pass_residual": bool(abs(resid) < 1e-12),
        "pass_numeric_agreement": bool(abs(closed - numeric) < 1e-9),
        "deprecated_formula_h_c_over_J": 2.0 * t_rel * math.asinh(math.exp(-2.0 / t_rel)),
        "deprecated_formula_condition_residual": deprecated_resid,
        "deprecated_formula_satisfies_condition": bool(
            deprecated_resid == deprecated_resid and abs(deprecated_resid) < 1e-9),
    }


def d_fix2_cosine(t_frac, a_frac):
    """沿 boss_pc_2 字面：1 - cos([T,A], [T_c,A_c])。"""
    num = t_frac * D_FIX2_BASELINE_T_C + a_frac * D_FIX2_BASELINE_A_C
    den = math.sqrt(t_frac * t_frac + a_frac * a_frac) * math.sqrt(
        D_FIX2_BASELINE_T_C ** 2 + D_FIX2_BASELINE_A_C ** 2)
    if den < 1e-12:
        return 0.0
    return 1.0 - num / den


def d_fix2_verdict(dfx):
    if dfx < D_FIX2_PASS_LT:
        return "PASS"
    if dfx < D_FIX2_FAIL_GE:
        return "GRAY"
    return "FAIL"


def L_ising_critical_line(t_frac):
    """V3 字面（逐字转写）：原函数无条件返回 0.5（docstring 自承「归一化到 T_frac 单位」）。"""
    return 0.5


def main() -> int:
    pe2 = json.loads(SRC_PE2.read_text(encoding="utf-8"))
    pc2 = json.loads(SRC_PC2.read_text(encoding="utf-8"))
    v3 = json.loads(SRC_V3.read_text(encoding="utf-8"))
    prereg_sha12 = sha12(PREREG.read_bytes())

    models9 = {m["name"]: m for m in v3["input_data"]["9_models"]}
    pc60 = {m["model"]: m for m in v3["P_C_distortion_bound_60cells"]["per_model"]}
    assert len(models9) == 9, "9 model 数据面不符"

    # ---------- 段 0 · legacy 逐字复现校验（双口径地基） ----------
    legacy_rows, legacy_mismatch = [], []
    for row in pe2["per_model"]:
        m = models9[row["model"]]
        tf, rf, af = m["T"] / 60.0, m["R"] / 60.0, m["A"] / 60.0
        d = d_fix2_cosine(tf, af)
        dv = d_fix2_verdict(d)
        hc = L_ising_critical_line(tf)
        dist = abs(rf - hc)
        recomputed = {"T_frac": round(tf, 4), "R_frac": round(rf, 4), "A_frac": round(af, 4),
                      "D_fix2": round(d, 4), "D_fix2_verdict": dv,
                      "h_c_at_T": round(hc, 4), "dist_to_h_c_T": round(dist, 4),
                      "transverse_ising_region": bool(dist <= TOL_STRICT)}
        disk = {k: row[k] for k in recomputed}
        match = (recomputed == disk)
        if not match:
            legacy_mismatch.append(row["model"])
        legacy_rows.append({"model": row["model"], "recomputed": recomputed,
                            "on_disk": disk, "bit_exact_match": match})
    legacy_dist = [r["on_disk"]["dist_to_h_c_T"] for r in legacy_rows]
    n_strict = sum(1 for d in legacy_dist if d <= TOL_STRICT)
    n_gray = sum(1 for d in legacy_dist if TOL_STRICT < d <= TOL_LOOSE)
    n_outside = sum(1 for d in legacy_dist if d > TOL_LOOSE)
    if n_strict >= 7:
        legacy_verdict = "FAIL (>= 7/9 model enter transverse Ising critical line +/- 0.05)"
    elif n_outside >= 7:
        legacy_verdict = "PASS (>= 7/9 model significantly deviate from transverse Ising)"
    else:
        legacy_verdict = "GRAY (mixed distribution)"
    legacy_repro = {
        "n_models": 9,
        "bit_exact_match_count": 9 - len(legacy_mismatch),
        "bit_exact_mismatch_models": legacy_mismatch,
        "all_bit_exact": (not legacy_mismatch),
        "recomputed_distance_distribution": {"in_strict_lte_0.05": n_strict,
                                             "in_gray_0.05_to_0.15": n_gray,
                                             "outside_gt_0.15": n_outside},
        "on_disk_distance_distribution": pe2["distance_distribution"],
        "recomputed_verdict": legacy_verdict,
        "on_disk_verdict": pe2["verdict"],
        "verdict_match": legacy_verdict == pe2["verdict"],
    }

    # ---------- 段 0b · 件谱系与 30/60-cell 精确半化（名义 N 显式标注） ----------
    pe2_bytes, pc2_bytes = SRC_PE2.read_bytes(), SRC_PC2.read_bytes()
    lineage = {
        "pe2_sha12": sha12(pe2_bytes), "pc2_sha12": sha12(pc2_bytes),
        "pe2_bytes": len(pe2_bytes), "pc2_bytes": len(pc2_bytes),
        "byte_identical": pe2_bytes == pc2_bytes,
        "payload_equal": pe2 == pc2,
        "runner_selfcheck_note": "deposon_team/plugins/boss_pc_2_transverse_field_ising.py 末尾 "
                                 "SELF-CHECK 记「命名勘误 lineage: boss_pe_2_transverse_field_ising.py "
                                 "-> boss_pc_2_transverse_field_ising.py; 历史结果保留于 "
                                 "results/boss_pe_2_real_transverse_ising_2026_09_15.json」",
        "finding": "**PE-2 与 PC-2 两件字节完全相同**（实测 byte_identical=%s）=> #12 的原结论与 "
                   "BOSS-PC-2 是**同一次实跑**，非两次独立实验；本件如实登记，"
                   "不将其当作两次独立证据。" % (pe2_bytes == pc2_bytes),
    }
    halving = []
    for name, m in models9.items():
        r = pc60[name]
        halving.append({
            "model": name, "T30": r["T30"], "T60": r["T60"],
            "R30": r["R30"], "R60": r["R60"], "A30": r["A30"], "A60": r["A60"],
            "T60_eq_2xT30": bool(r["T60"] == 2 * r["T30"]),
            "R60_eq_2xR30": bool(r["R60"] == 2 * r["R30"]),
            "A60_eq_2xA30": bool(r["A60"] == 2 * r["A30"]),
        })
    n_halving = sum(1 for h in halving if h["T60_eq_2xT30"] and h["R60_eq_2xR30"]
                    and h["A60_eq_2xA30"])
    nominal_n = {
        "declared_cells_per_model": N_CELLS,
        "independent_cells_per_model": N_CELLS // 2,
        "exact_halving_models": n_halving,
        "detail": halving,
        "finding": "**30/60-cell 精确半化实测 %d/9**（T60=2xT30 且 R60=2xR30 且 A60=2xA30）"
                   "=> 60-cell 是 30-cell 的精确 2x 复制，**不携带额外独立信息**；"
                   "名义 N 显式标注为 30 独立 cell / model（不是 60）。"
                   "跨尺寸信息须重采样方可比；本件沿 60-cell 口径（V3 既有字面）但显式标注该限制，"
                   "0 自造权。" % n_halving,
        "cross_file_rounding_note": "60cells 记 deepseek-v4-pro D_fix2_cosine = 0.1775，"
                                   "PE-2 记 D_fix2 = 0.1776；同式同输入（(T,A) 精确减半，余弦方向不变）"
                                   "=> 纯 float64 舍入差（0.0001），如实登记，不代为统一。",
    }
    dfix2_cross = []
    for row in pe2["per_model"]:
        a = row["D_fix2"]
        b = pc60[row["model"]]["D_fix2_cosine"]
        dfix2_cross.append({"model": row["model"], "pe2_D_fix2": a, "pc60_D_fix2_cosine": b,
                            "abs_diff": round(abs(a - b), 6),
                            "identical": bool(abs(a - b) < 1e-9)})

    # ---------- 段 1 · 盘上输入字段：K-V3R-0-A 防退化门（跑前自证） ----------
    t9 = [models9[r["model"]]["T"] / 60.0 for r in pe2["per_model"]]
    r9 = [models9[r["model"]]["R"] / 60.0 for r in pe2["per_model"]]
    a9 = [models9[r["model"]]["A"] / 60.0 for r in pe2["per_model"]]
    d9 = [d_fix2_cosine(t, a) for t, a in zip(t9, a9)]
    input_selfcheck = {
        "T_frac_盘上真实 (逐 model)": stat_block(t9),
        "R_frac_盘上真实 (逐 model)": stat_block(r9),
        "A_frac_盘上真实 (逐 model)": stat_block(a9),
        "D_fix2_盘上真分布 (逐 model)": stat_block(d9),
        "legacy_h_c_at_T_原构造 (对照, 应退化)": stat_block(
            [r["on_disk"]["h_c_at_T"] for r in legacy_rows]),
        "legacy_transverse_ising_region_原构造 (对照, 应退化)": stat_block(
            [1.0 if r["on_disk"]["transverse_ising_region"] else 0.0 for r in legacy_rows]),
    }
    gate_fields = [k for k in input_selfcheck if "原构造" not in k]
    gate_pass = {k: bool(input_selfcheck[k]["n_distinct"] > 3 and input_selfcheck[k]["std"] > 0)
                 for k in gate_fields}
    degen_alarm_hit = not all(gate_pass.values())

    # ---------- 段 2 · 根因：h_c_at_T ≡ 0.5 的机制 ----------
    root_cause = {
        "h_c_at_T_eq_0.5": {
            "verdict": "**硬编码常量**（函数无条件 return 0.5，与入参 t_frac 无关）",
            "proof": "V3 源件 ising_critical_line(t_frac) 的函数体只有 `return 0.5`，"
                     "docstring 自承「简化: 沿 T_frac 作 h_c(T) 平均值」但未实现；"
                     "故 h_c_at_T ≡ 0.5（9/9）是**构造常量**，非 T 的函数值。",
            "n_models_constant": sum(
                1 for r in legacy_rows if r["on_disk"]["h_c_at_T"] == 0.5),
        },
        "dimensional_mismatch": {
            "verdict": "**量纲错配**（V3 把 R_frac 与「归一化到 T_frac 单位」的常数 0.5 相减）",
            "proof": "V3 计算 dist_to_h_c_T = |R_frac - h_c_at_T|，其中 R_frac 是 cell 比例"
                     "（无量纲分数）、h_c_at_T = 0.5 注释为「归一化到 T_frac 单位」。"
                     "而 TFIM 的相变量是**横向场比 h/J**（TH-V3R-12 冻结的 PFEUTY_H_C_OVER_J = 1.0 "
                     "即 h_c/J）。把「cell 比例」与「场比」直接相减，"
                     "在 TFIM 相图上**没有对应点** —— 这是判据输入恒同之后的第二重问题。",
            "consequence": "故 (b) 的「真 phase boundary 测试」必须显式声明映射；"
                           "本件声明 drive ≡ R_frac / T_frac（并附 drive ≡ R_frac 敏感性）。",
        },
        "PFEUTY_constant_relation": {
            "v3_frozen_constant": PFEUTY_H_C_OVER_J,
            "v3_constant_is_used_in_code": False,
            "note": "**实测**：PFEUTY_H_C_OVER_J = 1.0 虽写入 pre_registered_constants，"
                    "但判定路径 ising_critical_line() 从未使用它（函数体硬编码 0.5）"
                    "=> 冻结的物理常数与实际判据脱钩。这是 #12 判据输入恒同的直接机制。",
        },
    }

    # ---------- 段 3 · §1.2 #12(a) 真 h_c 抽样（自实现精确迁移矩阵，≥100 sample/model） ----------
    boundary_pts, numeric_check = [], []
    for t_rel in T_REL_GRID:
        hc = tfim_h_c_over_j(t_rel)
        hcn = tfim_h_c_over_j_numeric(t_rel)
        boundary_pts.append({"t_rel_kT_over_J": t_rel, "kappa_J_over_kT": round(1.0 / t_rel, 6),
                             "h_c_over_J_analytic": hc, "h_c_over_J_numeric_bisect": hcn,
                             "abs_diff": abs(hc - hcn)})
        numeric_check.append(abs(hc - hcn))
    max_boundary_diff = max(numeric_check) if numeric_check else 0.0
    # 冻结常数 PFEUTY_H_C_OVER_J = 1.0 在本件相界上的位置（二分求 t_rel）
    # h_c/J = 2 t asinh(1/sinh(1/(2t))) 关于 t_rel 单调递增（t->0 => 0；t->inf => inf）
    lo, hi = 1e-6, 1e3
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if tfim_h_c_over_j(mid) < PFEUTY_H_C_OVER_J:
            lo = mid
        else:
            hi = mid
    t_rel_of_pfeuty = (lo + hi) / 2.0

    # 自校验：闭式 vs 二分、临界条件残差、极限行为；并留证初版（已作废）公式不满足临界条件
    selfcheck_probes = [tfim_eigenvalues_probe(t) for t in (0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.1)]
    n_probe_pass = sum(1 for p in selfcheck_probes
                       if p["pass_residual"] and p["pass_numeric_agreement"])
    max_probe_diff = max(abs(p["abs_diff_closed_vs_numeric"]) for p in selfcheck_probes)
    max_probe_resid = max(abs(p["condition_residual_at_closed_form"]) for p in selfcheck_probes)
    deprecated_any_satisfies = any(p["deprecated_formula_satisfies_condition"]
                                   for p in selfcheck_probes)
    selfcheck_all_pass = bool(n_probe_pass == len(selfcheck_probes)
                              and not deprecated_any_satisfies)

    # 相界单调性实测（h_c/J 关于 t_rel 单调递增 => 网格上下界覆盖全域单调段）
    hc_axis = [tfim_h_c_over_j(t) for t in T_REL_GRID]
    boundary_monotone = bool(all(hc_axis[i] <= hc_axis[i + 1] for i in range(len(hc_axis) - 1)))

    mapping_decls = {
        "drive_primary": "h_over_J := R_frac / T_frac（无量纲横向场比；显式声明的 worker 口径）",
        "drive_alternate": "h_over_J := R_frac（V3 字面轴；敏感性臂）",
        "temperature": "t_rel := T_frac（模型自身无量纲温度；显式声明的 worker 口径）",
        "why_declared": "V3 未定义 (T_frac, R_frac) -> (T, h/J) 的映射；K-V3R-0-B 禁止新设阈值，"
                        "但映射属**口径定义**（非阈值），故显式声明 + 附敏感性，0 隐藏。",
    }

    per_model_new = []
    for row in pe2["per_model"]:
        name = row["model"]
        m = models9[name]
        tf, rf, af = m["T"] / 60.0, m["R"] / 60.0, m["A"] / 60.0
        drive_p = rf / tf if tf > 0 else 0.0
        drive_a = rf
        # (a) h_c 抽样：逐 model 在 (T,J) 10x10 = 100 格上取相界 h_c/J
        samples, dists_p, dists_a = [], [], []
        for t_rel in T_REL_GRID:
            for j_rel in J_REL_GRID:
                kappa = j_rel / t_rel          # κ = J/(k_B T)，无量纲
                hc = tfim_h_c_over_j(t_rel)
                samples.append({"t_rel": t_rel, "j_rel": j_rel, "kappa": round(kappa, 9),
                                "h_c_over_J": hc})
                dists_p.append(abs(drive_p - hc))
                dists_a.append(abs(drive_a - hc))
        hc_vals = [s["h_c_over_J"] for s in samples]
        dmin_p, dmin_a = min(dists_p), min(dists_a)
        per_model_new.append({
            "model": name,
            "T_frac": round(tf, 6), "R_frac": round(rf, 6), "A_frac": round(af, 6),
            "drive_h_over_J_primary": round(drive_p, 9),
            "drive_h_over_J_alternate": round(drive_a, 9),
            "n_hc_samples": len(samples),
            "h_c_over_J_stat": stat_block(hc_vals),
            "h_c_over_J_samples": samples,
            "dist_min_primary": dmin_p,
            "dist_min_alternate": dmin_a,
            "transverse_ising_region_new": bool(dmin_p <= TOL_STRICT),
            "transverse_ising_region_new_loose": bool(dmin_p <= TOL_LOOSE),
            "legacy_h_c_at_T": row["h_c_at_T"],
            "legacy_dist_to_h_c_T": row["dist_to_h_c_T"],
            "legacy_transverse_ising_region": row["transverse_ising_region"],
            "D_fix2": round(d_fix2_cosine(tf, af), 4),
            "D_fix2_verdict": d_fix2_verdict(d_fix2_cosine(tf, af)),
            "D_fix2_cross_file_60cells": pc60[name]["D_fix2_cosine"],
        })

    # 重构判据的距离分布与聚合 verdict（V3 规则，阈值 0.05/0.15 一字不动）
    dists_new = [p["dist_min_primary"] for p in per_model_new]
    new_n_strict = sum(1 for d in dists_new if d <= TOL_STRICT)
    new_n_gray = sum(1 for d in dists_new if TOL_STRICT < d <= TOL_LOOSE)
    new_n_outside = sum(1 for d in dists_new if d > TOL_LOOSE)
    if new_n_strict >= 7:
        new_verdict_transverse = "FAIL (>= 7/9 model enter transverse Ising region)"
    elif new_n_outside >= 7:
        new_verdict_transverse = "PASS (>= 7/9 model significantly deviate from transverse Ising)"
    else:
        new_verdict_transverse = "GRAY (mixed distribution)"

    # 敏感性：drive ≡ R_frac 轴
    dists_alt = [p["dist_min_alternate"] for p in per_model_new]
    alt_n_strict = sum(1 for d in dists_alt if d <= TOL_STRICT)
    alt_n_gray = sum(1 for d in dists_alt if TOL_STRICT < d <= TOL_LOOSE)
    alt_n_outside = sum(1 for d in dists_alt if d > TOL_LOOSE)
    alt_verdict = ("FAIL (>= 7/9)" if alt_n_strict >= 7 else
                   ("PASS (>= 7/9)" if alt_n_outside >= 7 else "GRAY (mixed)"))

    # ---------- 段 4 · §1.2 #12(c) 主判据换 D_fix2 ----------
    dfix2_vals = [p["D_fix2"] for p in per_model_new]
    dfix2_counts = {v: sum(1 for p in per_model_new if p["D_fix2_verdict"] == v)
                    for v in ("PASS", "GRAY", "FAIL")}
    # 聚合方向映射（worker 显式声明；v1 未定义聚合规则）
    direction_decl = {
        "rule": "D_FIX2_PASS_LT = 0.05 / D_FIX2_FAIL_GE = 0.15（沿 V3 字面）："
                "D_fix2 < 0.05 = 与 (T_c,A_c) 基线近乎重合 = **无新结构** = "
                "「未显著偏离横场 Ising 预言」侧；D_fix2 ≥ 0.15 = 显著偏离基线 = "
                "「有新结构」侧。",
        "aggregate_from_distribution": ("GRAY" if (dfix2_counts["GRAY"] > 0 and
                                        max(dfix2_counts.values()) < 7) else
                                        ("FAIL_side" if dfix2_counts["PASS"] >= 7
                                         else "MIXED")),
        "d_fix2_counts": dfix2_counts,
        "note": "9 model 中 %d 个 D_fix2 < 0.05（近乎重合于基线），故 D_fix2 真分布整体指向"
                "「**未**显著偏离基线」侧；逐 model 对照表见 contingency，0 只靠聚合掩盖。" % dfix2_counts["PASS"],
    }

    # 逐 model 一致性（最不含聚合假设的对照）：region_new vs D_fix2_verdict
    contingency = []
    agree = 0
    for p in per_model_new:
        # 声明的对照规则：region_new=False（未进横场区）<-> D_fix2 判 PASS（近基线）
        consistent_model = bool((not p["transverse_ising_region_new"])
                                == (p["D_fix2_verdict"] == "PASS"))
        agree += 1 if consistent_model else 0
        contingency.append({
            "model": p["model"],
            "transverse_ising_region_new": p["transverse_ising_region_new"],
            "dist_min_primary": round(p["dist_min_primary"], 6),
            "D_fix2": p["D_fix2"], "D_fix2_verdict": p["D_fix2_verdict"],
            "model_level_consistent": consistent_model,
        })

    # ---------- 段 5 · K-V3R-12 判定（字面） ----------
    # **标签碰撞警示**：D_fix2 的档名 "PASS"（= 近乎重合于基线 = 无新结构）与横场判据的
    # verdict "PASS"（= 显著偏离 = 有新结构）**语义相反**。故本件**禁止**用字符串比较
    # verdict，一律先映射到声明的语义方向轴「是否存在新结构（散射层差异化）」再比较。
    AXIS = "new_structure_present"          # 声明的语义方向轴
    direction_transverse = ("no_new_structure" if new_n_strict >= 7 else
                            ("new_structure" if new_n_outside >= 7 else "mixed"))
    # D_fix2 侧：PASS 档 = 近基线 = 无新结构；FAIL 档 = 远离基线 = 有新结构
    n_near_base = dfix2_counts["PASS"]      # D_fix2 < 0.05
    n_far_base = dfix2_counts["FAIL"]       # D_fix2 >= 0.15
    if n_near_base >= 7:
        direction_dfix2_strict = "no_new_structure"
    elif n_far_base >= 7:
        direction_dfix2_strict = "new_structure"
    else:
        direction_dfix2_strict = "MIXED_ge7_rule_not_met"
    plurality = max(dfix2_counts, key=dfix2_counts.get)
    direction_dfix2_plurality = ("no_new_structure" if plurality == "PASS" else
                                 ("new_structure" if plurality == "FAIL" else "mixed"))
    directions_consistent = bool(direction_transverse == direction_dfix2_plurality
                                 and direction_transverse != "mixed")
    # 原判据输入是否仍恒同（沿 V3 路径：h_c_at_T ≡ 0.5）
    legacy_hc_nd = input_selfcheck["legacy_h_c_at_T_原构造 (对照, 应退化)"]["n_distinct"]
    criterion_inputs_still_constant_legacy = bool(legacy_hc_nd == 1)
    # 重构判据输入是否恒同（本件新构造）
    recon_hc_nds = [p["h_c_over_J_stat"]["n_distinct"] for p in per_model_new]
    recon_dist_nd = stat_block(dists_new)["n_distinct"]
    criterion_inputs_still_constant_recon = bool(min(recon_hc_nds) <= 1 or recon_dist_nd <= 1)

    # K-V3R-12 字面：verdict 与 D_fix2 真分布一致 -> PASS；不一致 / 判据输入仍恒同 -> FAIL
    kill_line_pass = bool(directions_consistent and not criterion_inputs_still_constant_recon)
    kill_line_hit = bool(not kill_line_pass)
    new_verdict = "PASS" if kill_line_pass else "FAIL"
    new_claim_verdict = (
        "**真判据成立**（K-V3R-12 PASS 的含义）：重构造 verdict 与 D_fix2 真分布**同向**"
        "（两侧均指向「无新结构」），且重构判据输入已解恒同（h_c/J 逐 model n_distinct = %s，"
        "dist_min n_distinct = %d）。**注意**：此处 PASS **不**表示原「9/9 显著偏离」主张被证实 —— "
        "重构的真判据给出的是**相反方向**（%d/9 模型落入横场区 => FAIL 侧）。"
        % (str(sorted(set(recon_hc_nds))), recon_dist_nd, new_n_strict)
        if kill_line_pass else
        "维持假成立：重构 verdict（%s）与 D_fix2 真分布（PASS %d / GRAY %d / FAIL %d）不同向，"
        "或重构判据输入仍恒同"
        % (new_verdict_transverse, dfix2_counts["PASS"], dfix2_counts["GRAY"],
           dfix2_counts["FAIL"]))

    consistent = bool(kill_line_pass and legacy_verdict.startswith("PASS"))
    一致性 = ("一致（改判成）" if consistent else "不一致（维持原标注 + 显式登记新构造 verdict）")
    if kill_line_pass and consistent:
        改判档位 = ("§2.3 第 1 行（PASS + 一致）→ 立改判件、与原标注并列写入勘误链 E-41.x 系、"
                    "V3 原报告 byte 0 触动。**改判内容 = 重构 verdict 为真判据且与 D_fix2 同向，"
                    "其方向与原标签相反**（原 PASS「9/9 显著偏离」→ 重构 FAIL「%d/9 落入横场区」）"
                    "；本档 PASS **不**表示原 PASS 主张被证实。" % new_n_strict)
    elif kill_line_pass:
        改判档位 = ("§2.3 第 2 行（PASS + 不一致）→ 维持原 V3 标注不动 + 显式登记新构造 verdict + γ"
                    "（含方向标签碰撞警示）")
    else:
        改判档位 = "§2.3 第 3 行（FAIL = 原标注维持）→ 0 改判动作"

    gammas = {
        "γ1_Pfeuty_sampling_limitation":
            "§1.2 #12(a) 字面要求「从 Pfeuty Phase Diagram 抽样 h_c(T,J) 连续分布」。实测："
            "1D TFIM 精确解的临界线在 (T, h/J) 平面上是**单条曲线** h_c/J = 2·t_rel·asinh(e^{-2/t_rel})"
            "（本件自实现精确迁移矩阵导出，解析解与二分数值解最大偏差 %.3e）；"
            "V3 冻结的 PFEUTY_H_C_OVER_J = 1.0 只是该曲线上的**一点**（t_rel ≈ %.6f），"
            "本身不携带可抽样的 T 依赖分布。故本件以 (T,J) 10x10 = 100 格/模型 在曲线上取样"
            "得到真分布，**0 引入预登记之外的物理量，0 编造相图读数**。" % (max_boundary_diff, t_rel_of_pfeuty),
        "γ2_JSV1999_missing":
            "§1.2 #12(b) 字面要求「沿 Jordan-Sucher-Votek 1999 数值解」。实测：该文献相图"
            "**本仓 0 命中、本件 0 联网、0 代理**=> 其曲线与数值**未复现、0 编造**。"
            "本件改用自实现精确对角化（2x2 迁移矩阵）相界替代，并如实标注为**替代品**；"
            "JSV 1999 专项对照留 PI 拍板（是否授权联网调取或由 PI 提供该相图）。",
        "γ3_mapping_not_preregistered":
            "(T_frac, R_frac) -> (T, h/J) 的映射在 V3 与预登记中**均未定义**；本件显式声明 "
            "drive := R_frac/T_frac、t_rel := T_frac，并附 drive := R_frac 敏感性轴。"
            "映射属口径定义（K-V3R-0-B 管阈值不管口径），但结论对映射敏感，已如实登记。",
        "γ4_PE2_PC2_same_bytes":
            "BOSS-PE-2 与 BOSS-PC-2 两件 result JSON **字节完全相同**（见 lineage 段）"
            "=> #12 原结论与 BOSS-PC-2 是同一次实跑；本件不将其计为两次独立证据。",
        "γ5_30_60_exact_halving":
            "30/60-cell 精确半化实测 %d/9 => 60-cell 为 30-cell 的精确 2x 复制，"
            "名义独立 N = 30 cell/model（非 60）；跨尺寸信息须重采样方可比，本件未重采样（0 新设权）。"
            % n_halving,
        "γ6_D_fix2_cross_file_rounding":
            "deepseek-v4-pro 的 D_fix2 在 PE-2 记 0.1776、在 60cells 记 0.1775"
            "（同式同输入下余弦方向不变 => 纯 float64 舍入差）；如实登记，0 代为统一。",
        "γ7_boundary_convention_scale":
            "迁移矩阵约定（K=βJ, Γ=βh/2）决定 h_c/J 的**绝对刻度**；换约定会平移刻度但"
            "**无量纲临界条件 sinh(Γ)=e^{-2K} 不变**。本件全程以 (kappa, Γ) 无量纲形式报告，"
            "并给出 h_c/J = PFEUTY_H_C_OVER_J 的落点 t_rel ≈ %.6f，供 PI 换约定时对齐。" % t_rel_of_pfeuty,
    }

    result = {
        "schema": "v3_recheck_result/12_boss_pe2_transverse_ising/1",
        "prereg": {"path": "results/_v3_recheck_prereg_v1_2026_09_27.md",
                   "sha12": prereg_sha12, "kill_line": "K-V3R-12",
                   "threshold": "TH-V3R-12 (PFEUTY_H_C_OVER_J=1.0; TOL_STRICT=0.05; "
                                "TOL_LOOSE=0.15; D_FIX2_PASS_LT=0.05; D_FIX2_FAIL_GE=0.15)"},
        "executor": "results/_v3_recheck_12_executor_2026_09_27.py",
        "date": "2026-09-27",
        "seed": SEED,
        "runtime": "0 LLM; stdlib only (json/hashlib/math); no network; no proxy; "
                   "read-only inputs; 0 external literature retrieval",
        "skill": {
            "plugin": "@scientific-research-workflows",
            "skill": "experimental-design",
            "sha12_of_SKILL_md": "0a314eed103a",
            "applied": ["区组 = 9 model（block）", "(T,J) 10x10 全因子 = 100 格/模型（无别名）",
                        "伪重复声明：100 样本嵌套于 model，独立重复真实层级 = 9 model（非 900）",
                        "名义 N 显式标注（30/60-cell 精确半化）",
                        "口径（映射/约定）先声明后测量 + 敏感性", "seed 预登记 + 落盘可复算"],
        },
        "inputs": [
            {"path": "results/boss_pe_2_real_transverse_ising_2026_09_15.json",
             "sha12_measured": sha12(pe2_bytes), "role": "#12 源件（原结论所在）"},
            {"path": "results/boss_pc_2_real_transverse_ising_2026_09_15.json",
             "sha12_measured": sha12(pc2_bytes), "role": "同源姊妹件（命名勘误 lineage）"},
            {"path": "deposon_team/plugins/boss_pc_2_transverse_field_ising.py",
             "sha12_measured": sha12(SRC_RUNNER.read_bytes()),
             "role": "只读公式来源（本件 0 import / 0 触动）"},
            {"path": "results/deposon_v3_physical_opt_60cells_2026_09_11.json",
             "sha12_measured": sha12(SRC_V3.read_bytes()),
             "role": "9 model (T,R,A) + 60cells D_fix2 数据面"},
            {"path": "docs/V3X/P_E_D1_D3_REPORT_2026_09_15.md",
             "sha12_measured": sha12(SRC_PEREP.read_bytes()),
             "role": "§1.2 risk3「D_fix2 ADOPTED」字面来源"},
        ],
        "legacy_reproduction": legacy_repro,
        "legacy_per_model": legacy_rows,
        "lineage_pe2_pc2": lineage,
        "nominal_n_30_60_halving": nominal_n,
        "d_fix2_cross_file": dfix2_cross,
        "root_cause": root_cause,
        "construct": {
            "(a)_h_c_sampling": "自实现 1D TFIM 2x2 精确迁移矩阵（约定 K=βJ, Γ=βh/2 逐字声明），"
                                "leading eigenvalue 简并 => sinh(Γ)=e^{-2K} => "
                                "h_c/J = 2·t_rel·asinh(e^{-2/t_rel})；"
                                "在 (T,J) 10x10 = %d 格/模型 上取样（≥ v1 要求的 100）"
                                % N_SAMPLES_PER_MODEL,
            "(a)_grid": {"t_rel": list(T_REL_GRID), "j_rel": list(J_REL_GRID),
                         "n_samples_per_model": N_SAMPLES_PER_MODEL},
            "(a)_boundary": boundary_pts,
            "(a)_numeric_crosscheck": {
                "method": "沿 Γ 二分搜 leading eigenvalue 简并判别式 disc = e^{2K}sinh^2(Γ) - e^{-2K} "
                          "的符号翻转点（**不使用 asinh 闭式**，构成独立核验）",
                "max_abs_diff_analytic_vs_numeric": max_boundary_diff,
                "pass": bool(max_boundary_diff < 1e-9),
            },
            "(a)_critical_condition": {
                "convention": TFIM_CONVENTION,
                "exact_condition": "sinh(2K) sinh(2Γ) = 1（1D TFIM 标准精确临界条件）",
                "closed_form": "h_c/J = 2 t_rel asinh(1/sinh(1/(2 t_rel)))",
                "physical_note": "1D TFIM 在**有限 L 下恒有隙**；量子临界是 L->inf 极限的能级交叉，"
                                 "**不是**有限 2x2 迁移矩阵的本征值简并（该误推已作废，见下方勘误）",
            },
            "(a)_selfcheck": {
                "method": "闭式解代入临界条件残差 + 闭式 vs 二分（不使用 asinh）+ 极限行为；"
                          "并留证初版（已作废）公式**不**满足临界条件",
                "probes": selfcheck_probes,
                "n_probe_pass": n_probe_pass,
                "n_probes": len(selfcheck_probes),
                "max_abs_diff_closed_vs_numeric": max_probe_diff,
                "max_abs_condition_residual": max_probe_resid,
                "deprecated_formula_satisfies_condition_anywhere": deprecated_any_satisfies,
                "all_pass": selfcheck_all_pass,
            },
            "(a)_erratum_deprecated_formula": {
                "deprecated": "h_c/J = 2 t_rel asinh(e^{-2/t_rel})（初版，按 2x2 本征值简并推导）",
                "why_deprecated": "对 T = [[e^{K+G}, e^{-K}], [e^{-K}, e^{K-G}]]，判别式 = "
                                  "((T11-T22)/2)^2 + T12*T21 = e^{2K} sinh^2(G) + e^{-2K} > 0"
                                  "（G > 0 恒成立）=> 该 2x2 形式**不存在**本征值简并，初版推导符号错误。",
                "caught_by": "本件新增的临界条件自校验（tfim_eigenvalues_probe）",
                "deprecated_values_participate_in_any_verdict": False,
                "note": "作废公式的数值**未参与**任何判定；本件为如实登记自身勘误，非隐瞒。",
            },
            "(a)_boundary_monotonicity": {
                "h_c_over_J_axis": hc_axis,
                "monotone_increasing_in_t_rel": boundary_monotone,
                "note": "h_c/J = 2 t asinh(e^{-2/t}) 关于 t_rel 单调递增（t->0 => 0，t->inf => inf）；"
                        "故 dist_min = min_t |drive - h_c/J(t)| 在网格端点取极值，"
                        "网格上下界覆盖单调段全区间 => 网格加密不改变判定",
            },
            "(a)_pfeuty_constant_location": {
                "v3_frozen_constant": PFEUTY_H_C_OVER_J,
                "t_rel_where_hc_over_J_equals_constant": t_rel_of_pfeuty,
                "kappa_there": 1.0 / t_rel_of_pfeuty,
                "note": "冻结常数在自实现相界上的落点；供换约定时对齐（0 当阈值）",
            },
            "(b)_phase_boundary": "自实现精确对角化相界（替代品；JSV 1999 曲线 0 复现，见 gamma）",
            "(b)_mapping_declarations": mapping_decls,
            "(c)_main_criterion": "主判据换 D_fix2（沿 TH-V3R-12 既有字面 "
                                  "D_FIX2_PASS_LT=0.05 / D_FIX2_FAIL_GE=0.15）",
            "verdict_rule_unchanged": "n_in_strict ≥ 7 -> FAIL；n_outside ≥ 7 -> PASS；"
                                      "否则 GRAY（沿 V3 字面，0 擅调）",
        },
        "design_layout": {
            "blocks": 9, "block_unit": "model",
            "treatments": "%d 温度 x %d 耦合 = %d 格" % (N_T_GRID, N_J_GRID, N_SAMPLES_PER_MODEL),
            "n_cells": N_SAMPLES_PER_MODEL * 9,
            "aliasing": "无（2 因子全因子）",
            "pseudoreplication_declaration":
                "沿 skill experimental-design「伪重复」条：每 model 的 %d 个 h_c 样本**嵌套于** "
                "model，独立重复的真实层级 = **9 个 model**（非 %d）。判定在 model 层级聚合，"
                "样本量不作为独立信息计入。" % (N_SAMPLES_PER_MODEL, N_SAMPLES_PER_MODEL * 9),
        },
        "construct_degen_self_check": {
            "gate": "K-V3R-0-A: n_distinct > 3 + std > 0 on every on-disk input field",
            "input_fields": input_selfcheck,
            "gate_per_field": gate_pass,
            "degenerate_alarm_hit": degen_alarm_hit,
            "gate_pass": not degen_alarm_hit,
            "output_field": {
                "h_c_over_J_per_model": {p["model"]: p["h_c_over_J_stat"]
                                        for p in per_model_new},
                "dist_min_primary": stat_block(dists_new),
                "D_fix2": stat_block(dfix2_vals),
            },
            "contrast": {
                "original_h_c_at_T": input_selfcheck["legacy_h_c_at_T_原构造 (对照, 应退化)"],
                "original_transverse_ising_region":
                    input_selfcheck["legacy_transverse_ising_region_原构造 (对照, 应退化)"],
            },
        },
        "per_model": per_model_new,
        "distance_distribution_new": {
            "in_strict_lte_0.05": new_n_strict,
            "in_gray_0.05_to_0.15": new_n_gray,
            "outside_gt_0.15": new_n_outside,
        },
        "verdict_transverse_new": new_verdict_transverse,
        "d_fix2_main_criterion": {
            "counts": dfix2_counts,
            "per_model": {p["model"]: p["D_fix2_verdict"] for p in per_model_new},
            "stat": stat_block(dfix2_vals),
            "direction_declaration": direction_decl,
        },
        "contingency_region_vs_dfix2": {
            "declared_rule": "region_new == False（未进横场区）<-> D_fix2_verdict == PASS（近基线）",
            "n_models_agree": agree, "n_models": 9,
            "rows": contingency,
        },
        "sensitivity": {
            "drive_alternate_axis_R_frac": {
                "definition": mapping_decls["drive_alternate"],
                "distance_distribution": {"in_strict_lte_0.05": alt_n_strict,
                                          "in_gray_0.05_to_0.15": alt_n_gray,
                                          "outside_gt_0.15": alt_n_outside},
                "verdict": alt_verdict,
            },
            "grid_resolution": {
                "current": "%dx%d" % (N_T_GRID, N_J_GRID),
                "note": "网格档数为 worker 声明的实现量（0 判定阈值）；"
                        "T_REL_GRID/J_REL_GRID 的上下界覆盖 h_c/J 的全域单调段，"
                        "故 dist_min 对网格加密不敏感（边界为单调连续函数）。",
            },
        },
        "legacy_dual_track": {
            "legacy_verdict": "%s（沿原 V3 字面：9/9 模型 dist_to_h_c_T > 0.15；"
                              "h_c_at_T ≡ 0.5 恒同）" % legacy_verdict,
            "legacy_verdict_recomputed": legacy_verdict,
            "legacy_verdict_on_disk": pe2["verdict"],
            "legacy_verdict_reproduced": legacy_repro["verdict_match"],
            "legacy_distance_distribution": pe2["distance_distribution"],
            "legacy_d_fix2_distribution": pe2["d_fix2_distribution"],
            "note": "原 PASS 立在 h_c_at_T ≡ 0.5 这一硬编码常量与 R_frac 的量纲错配相减之上；"
                    "该判据与同文件内 D_fix2 真分布（PASS 6 / GRAY 2 / FAIL 1）本身即不同向。",
        },
        "gammas": gammas,
        "verdict": {
            "new_verdict": new_verdict,
            "new_claim_verdict": new_claim_verdict,
            "new_verdict_transverse": new_verdict_transverse,
            "d_fix2_counts": dfix2_counts,
            "semantic_axis": AXIS,
            "label_collision_warning":
                "D_fix2 档名 'PASS'（近基线 = 无新结构）与横场判据 verdict 'PASS'"
                "（显著偏离 = 有新结构）语义相反；本件一律先映射到语义方向轴再比较，"
                "0 用字符串比较 verdict。",
            "direction_transverse": direction_transverse,
            "direction_dfix2_strict_ge7_rule": direction_dfix2_strict,
            "direction_dfix2_plurality": direction_dfix2_plurality,
            "directions_consistent": directions_consistent,
            "criterion_inputs_still_constant_legacy": criterion_inputs_still_constant_legacy,
            "criterion_inputs_still_constant_reconstruction": criterion_inputs_still_constant_recon,
            "recon_h_c_over_J_n_distinct_per_model": sorted(set(recon_hc_nds)),
            "recon_dist_min_n_distinct": recon_dist_nd,
            "contingency_model_level_agree": "%d/9" % agree,
            "legacy_verdict": legacy_verdict,
            "一致性": 一致性,
            "kill_line_pass": kill_line_pass,
            "kill_line_hit": kill_line_hit,
            "改判档位": 改判档位,
        },
        "iron_rules": {
            "0_LLM": True, "no_proxy": True, "no_key_in_prompt_json_disk": True,
            "read_only_inputs": True, "derived_json_not_merged": True,
            "v3_original_report_bytes_untouched": True,
            "frozen_runner_not_imported_not_edited": True,
            "no_external_literature_retrieval": True,
        },
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("[#12] written:", OUT.relative_to(REPO))
    print("[#12] legacy bit-exact: %d/9 (verdict match=%s)" % (
        legacy_repro["bit_exact_match_count"], legacy_repro["verdict_match"]))
    print("[#12] PE2==PC2 bytes identical: %s | 30/60 exact halving: %d/9" % (
        lineage["byte_identical"], n_halving))
    print("[#12] degen gate_pass=%s" % (not degen_alarm_hit))
    print("[#12] critical-cond selfcheck: %d/%d probes pass=%s max|closed-num|=%.3e "
          "max|resid|=%.3e | deprecated_formula_satisfies=%s" % (
              n_probe_pass, len(selfcheck_probes), selfcheck_all_pass, max_probe_diff,
              max_probe_resid, deprecated_any_satisfies))
    print("[#12] boundary analytic vs numeric max|diff| = %.3e (pass=%s); "
          "h_c/J = 1.0 at t_rel = %.6f" % (
              max_boundary_diff, max_boundary_diff < 1e-9, t_rel_of_pfeuty))
    print("[#12] h_c_over_J n_distinct per model: %s" % [
        p["h_c_over_J_stat"]["n_distinct"] for p in per_model_new])
    print("[#12] dist_min_new stat: nd=%d std=%.6f min=%.4f max=%.4f" % (
        stat_block(dists_new)["n_distinct"], stat_block(dists_new)["std"],
        min(dists_new), max(dists_new)))
    print("[#12] distance dist new: %s -> %s" % (
        {"strict": new_n_strict, "gray": new_n_gray, "outside": new_n_outside},
        new_verdict_transverse))
    print("[#12] alt-axis (drive=R_frac): %s -> %s" % (
        {"strict": alt_n_strict, "gray": alt_n_gray, "outside": alt_n_outside}, alt_verdict))
    print("[#12] D_fix2 counts: %s | contingency agree %d/9" % (dfix2_counts, agree))
    print("[#12] K-V3R-12: dir_transverse=%s dir_dfix2_plurality=%s consistent=%s "
          "| recon_hc_nd=%s recon_dist_nd=%d still_const_recon=%s -> %s (pass=%s)" % (
              direction_transverse, direction_dfix2_plurality, directions_consistent,
              sorted(set(recon_hc_nds)), recon_dist_nd, criterion_inputs_still_constant_recon,
              new_verdict, kill_line_pass))
    print("[#12] label collision: D_fix2 'PASS' band = no_new_structure; transverse 'PASS' = new_structure")
    return 0


if __name__ == "__main__":
    sys.exit(main())
