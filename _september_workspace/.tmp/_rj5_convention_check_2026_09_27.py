# R-J5 约定自洽性核验脚本（stdlib only; 0 联网; 0 LLM; 只读输入）
# 配套件：results/_v3_recheck_12_rj5_provenance_2026_09_27.md
# 目的：在 #12 自声明约定下，逐字对照其「临界条件 / 闭式 / t_rel」三者是否自洽。
# 0 修改任何既有件；0 重裁 #12 判定；仅给出可复算读数。
import json
import math
import hashlib
from pathlib import Path

ROOT = Path(r"D:/私人资料/deposon-repo")
V3 = ROOT / "results/deposon_v3_physical_opt_60cells_2026_09_11.json"

T_REL_GRID = [round(0.2 + 0.1 * i, 1) for i in range(10)]   # 与 executor 同网格
J_REL_GRID = [round(0.5 + 0.25 * i, 1) for i in range(10)]
TOL_STRICT, TOL_LOOSE = 0.05, 0.15                          # TH-V3R-12 既有字面


# ---------- 段 A · 1D TFIM -> 2D 经典各向异性 Ising 的精确映射（矩阵恒等式核验） ----------
# 恒等式：e^{2b σx} = (e^{2b σz} - e^{-2b σz}) / (2 sinh 2b)
# => 虚时间方向耦合 2K2 = 2b  =>  K2 = b = β h_phys / 2
def mat2(m):
    return tuple(tuple(m[r][c] for c in range(2)) for r in range(2))


def matmul(A, B):
    return tuple(tuple(sum(A[r][k] * B[k][c] for k in range(2)) for c in range(2))
                 for r in range(2))


def expm2(sigma, a):
    """exp(a * sigma) 的 2x2 数值矩阵（sigma = ±1 的 Pauli 表示）。"""
    c, s = math.exp(a), math.exp(-a)
    if sigma == "z":                       # diag(e^a, e^-a)
        return ((c, 0.0), (0.0, s))
    raise ValueError(sigma)


def sigma_x():
    return ((0.0, 1.0), (1.0, 0.0))


def sigma_z():
    return ((1.0, 0.0), (0.0, -1.0))


def mapping_identity_max_abs_err(b_list=(0.3, 0.7, 1.1, 2.0, 5.0)):
    worst = 0.0
    sx, sz = sigma_x(), sigma_z()
    for b in b_list:
        ez_p, ez_m = expm2("z", 2.0 * b), expm2("z", -2.0 * b)
        den = 2.0 * math.sinh(2.0 * b)
        rhs = tuple(tuple((ez_p[r][c] - ez_m[r][c]) / den for c in range(2))
                     for r in range(2))
        # lhs = exp(2b σx) = cosh(2b) I + sinh(2b) σx
        c2, s2 = math.cosh(2.0 * b), math.sinh(2.0 * b)
        lhs = ((c2 + s2 * sx[0][1], s2 * sx[0][1]), (s2 * sx[1][0], c2 + s2 * sx[1][1]))
        worst = max(worst, max(abs(lhs[r][c] - rhs[r][c]) for r in range(2) for c in range(2)))
    _ = (matmul, sigma_z)
    return worst


# ---------- 段 B · 2D 方格 Ising 精确临界耦合的代数核验 ----------
def square_lattice_check():
    k_c = 0.5 * math.log(1.0 + math.sqrt(2.0))   # 经典精确值
    return {"K_c_analytic": k_c, "sinh_2Kc_minus_1": math.sinh(2.0 * k_c) - 1.0}


# ---------- 段 C · 两条候选临界条件（各自在 #12 声明约定下的闭式） ----------
def repo_hc(t):          # #12 executor 逐字实现：h_c/J = 2 t asinh(1/sinh(1/(2t)))
    return 2.0 * t * math.asinh(1.0 / math.sinh(1.0 / (2.0 * t)))


def fixed_hc(t):         # #12 声明约定（H = -(J/4)Σσzσz - (h/4)Σσx）下应有的闭式
    # 精确条件：sinh(β J_phys) sinh(β h_phys) = 1, J_phys = J/4, h_phys = h/4
    #  => sinh(K) sinh(Γ) = 1  (K = βJ/4, Γ = βh/4)
    #  => Γ_c = asinh(1/sinh(K)), h_c/J = Γ_c/K, K = 1/(4 t_rel)
    return 4.0 * t * math.asinh(1.0 / math.sinh(1.0 / (4.0 * t)))


def repo_resid(t):        # #12 自校验口径：sinh(2K)sinh(2Γ) - 1，K = 1/(4t)
    K = 1.0 / (4.0 * t)
    G = repo_hc(t) * K
    return math.sinh(2.0 * K) * math.sinh(2.0 * G) - 1.0


def fixed_resid(t):       # 同一 h_c/J 值代入「声明约定应有的条件」sinh(K)sinh(Γ) - 1
    K = 1.0 / (4.0 * t)
    G = repo_hc(t) * K
    return math.sinh(K) * math.sinh(G) - 1.0


def fixed_resid_selfcheck(t):   # 修正闭式代入修正条件（应为 ~0）
    K = 1.0 / (4.0 * t)
    G = fixed_hc(t) * K
    return math.sinh(K) * math.sinh(G) - 1.0


def fixed_hc_numeric(t, n=200):
    """不使用 asinh：对 sinh(K)sinh(Γ)-1 沿 Γ 二分（独立核验修正闭式）"""
    K = 1.0 / (4.0 * t)
    lo, hi = 1e-12, 1.0
    while math.sinh(K) * math.sinh(hi) - 1.0 < 0.0 and hi < 1e6:
        hi *= 2.0
    for _ in range(n):
        mid = (lo + hi) / 2.0
        if math.sinh(K) * math.sinh(mid) - 1.0 < 0.0:
            lo = mid
        else:
            hi = mid
    return ((lo + hi) / 2.0) / K


def t_where_hc_equals_one(fn, lo=1e-3, hi=50.0, n=200):
    for _ in range(n):
        mid = (lo + hi) / 2.0
        if fn(mid) < 1.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def main():
    out = {}
    out["A_mapping_identity_max_abs_err"] = mapping_identity_max_abs_err()
    out["B_square_lattice"] = square_lattice_check()

    axis = []
    for t in T_REL_GRID:
        a, b = repo_hc(t), fixed_hc(t)
        axis.append({"t_rel": t, "h_c_over_J_12": a, "h_c_over_J_fixed": b,
                     "ratio_12_over_fixed": a / b, "ratio_minus_1": a / b - 1.0,
                     "resid_12_condition_at_12_value": repo_resid(t),
                     "resid_fixed_condition_at_12_value": fixed_resid(t),
                     "resid_fixed_condition_at_fixed_value": fixed_resid_selfcheck(t),
                     "absdiff_fixed_closed_vs_bisect": abs(b - fixed_hc_numeric(t))})
    out["C_axis"] = axis
    out["C_max_abs_resid_12_cond_at_12_value"] = max(abs(r["resid_12_condition_at_12_value"]) for r in axis)
    out["C_min_abs_resid_fixed_cond_at_12_value"] = min(abs(r["resid_fixed_condition_at_12_value"]) for r in axis)
    out["C_max_abs_resid_fixed_cond_at_fixed_value"] = max(abs(r["resid_fixed_condition_at_fixed_value"]) for r in axis)
    out["C_max_absdiff_fixed_closed_vs_bisect"] = max(r["absdiff_fixed_closed_vs_bisect"] for r in axis)
    out["D_t_rel_where_hc_over_J_eq_1__12_curve"] = t_where_hc_equals_one(repo_hc)
    out["D_t_rel_where_hc_over_J_eq_1__fixed_curve"] = t_where_hc_equals_one(fixed_hc)

    # ---------- 段 E · (b) 臂敏感性（阈值 0.05/0.15 与 verdict 规则一字不动） ----------
    v3 = json.loads(V3.read_text(encoding="utf-8"))
    models9 = {m["name"]: m for m in v3["input_data"]["9_models"]}
    rows = []
    for name, m in models9.items():
        tf, rf = m["T"] / 60.0, m["R"] / 60.0
        drive_p = rf / tf if tf > 0 else 0.0
        drive_a = rf
        d12p = min(abs(drive_p - repo_hc(t)) for t in T_REL_GRID for _ in J_REL_GRID)
        dfxp = min(abs(drive_p - fixed_hc(t)) for t in T_REL_GRID for _ in J_REL_GRID)
        d12a = min(abs(drive_a - repo_hc(t)) for t in T_REL_GRID for _ in J_REL_GRID)
        dfxa = min(abs(drive_a - fixed_hc(t)) for t in T_REL_GRID for _ in J_REL_GRID)
        rows.append({"model": name, "T_frac": round(tf, 4), "R_frac": round(rf, 4),
                     "drive_primary": round(drive_p, 6),
                     "dist_min_primary_12curve": round(d12p, 4),
                     "dist_min_primary_fixedcurve": round(dfxp, 4),
                     "dist_min_alternate_12curve": round(d12a, 4),
                     "dist_min_alternate_fixedcurve": round(dfxa, 4)})
    rows.sort(key=lambda r: r["T_frac"], reverse=True)

    def dist_bucket(key):
        ds = [r[key] for r in rows]
        s = sum(1 for d in ds if d <= TOL_STRICT)
        g = sum(1 for d in ds if TOL_STRICT < d <= TOL_LOOSE)
        o = sum(1 for d in ds if d > TOL_LOOSE)
        if s >= 7:
            v = "FAIL (>= 7/9 model enter transverse Ising region)"
        elif o >= 7:
            v = "PASS (>= 7/9 model significantly deviate from transverse Ising)"
        else:
            v = "GRAY (mixed distribution)"
        return {"in_strict_lte_0.05": s, "in_gray_0.05_to_0.15": g, "outside_gt_0.15": o,
                "verdict": v}

    out["E_rows"] = rows
    out["E_primary_12curve"] = dist_bucket("dist_min_primary_12curve")
    out["E_primary_fixedcurve"] = dist_bucket("dist_min_primary_fixedcurve")
    out["E_alternate_12curve"] = dist_bucket("dist_min_alternate_12curve")
    out["E_alternate_fixedcurve"] = dist_bucket("dist_min_alternate_fixedcurve")

    print(json.dumps(out, ensure_ascii=False, indent=2, sort_keys=False))


if __name__ == "__main__":
    main()
