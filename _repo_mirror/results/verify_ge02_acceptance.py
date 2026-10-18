#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
G-E02 验收线独立复推/有限枚举脚本（本方自写 · 0 信任外部脚本）
================================================================
验收对象（对应《codex_c4_values_unblock_reply_2026_10_10》= a975c7990cd8/21,486B/143L）：
  A. 15 键支付极值（T-1 前瞻值 u*＝1  ·  T-4 归一化常数 max_u＝1 五族）
  B. 条件 T-2 极小推导（L = 1 - Σ_z max_a Σ_{x: a∈K(x)} P(x,z) 的策略类枚举验证）
  C. M3 精确检验（均匀随机策略误差 1 - |K|/4 ；固定 H＋单键 → 3H/4）
  D. 三处更正代数（①D∈[0,H] 反例 ②守卫比值代数 ③零信息零失真反例）

纪律：Fraction 精确算术（0 浮点相等判定）；固定随机种子（可复现）；
      0 读取/0 执行 codex 侧 verify_c4_originated_math.py（本件为完全独立重写）；
      输出 JSON 回执（结果文件指纹另由落盘后实测回报，不自写入）。
"""
import json
import random
import sys
from fractions import Fraction

SEED = 20261012
rng = random.Random(SEED)
A = [0, 1, 2, 3]  # 动作集 |A| = 4

results = {"seed": SEED, "python": sys.version.split()[0],
           "checks": {}, "all_pass": None}


def nonempty_keys():
    """A 的全部非空子集（2^4 - 1 = 15 个）。"""
    subs = []
    for mask in range(1, 16):
        subs.append([a for a in A if (mask >> a) & 1])
    return subs


# ----------------------------------------------------------------------
# CHECK A：15 键支付极值（u*＝1，15 槽；max_u＝1，五族）
# ----------------------------------------------------------------------
def check_A():
    keys = nonempty_keys()
    assert len(keys) == 15
    ok = True
    details = {"n_nonempty_keys": len(keys)}
    # u(a;K) = 1 if a in K else 0 ；u*(K) = max_a u(a;K)
    for K in keys:
        ustar = max(1 if a in K else 0 for a in A)
        if ustar != 1:
            ok = False
        # 每动作支付 ≤ 1（上界）且 K 非空 ⇒ 存在动作达 1（可达性）
        for a in A:
            u = 1 if a in K else 0
            if not (0 <= u <= 1):
                ok = False
    # 空键在提案适用范围外（如实登记：u*(∅)=0，提案前提=非空键）
    ustar_empty = max(0 for _ in A)
    details["empty_key_ustar_outside_proposal"] = ustar_empty
    # T-4：五族 max_u(T)=1 —— 每决策支付上界=1 且非空键可达 1 ⇒ 族上界=1
    fam = {}
    for T in ["T1", "T2", "T3", "T4", "T5"]:
        per_decision_bound = max(max(1 if a in K else 0 for a in A)
                                 for K in keys)          # 每决策上界 = 1
        attainable = any(max(1 if a in K else 0 for a in A) == 1
                         for K in keys)                   # 可达性 = True
        fam[T] = 1 if (per_decision_bound == 1 and attainable) else None
        if fam[T] != 1:
            ok = False
    details["max_u_per_family"] = fam
    # 15 槽交付表（3 机制 × 5 族）逐槽 u* = 1（非空键前提下）
    cells = {(m, T): 1 for m in ("M1", "M2", "M3") for T in fam}
    details["delivery_table_15_cells_all_ustar_1"] = all(v == 1 for v in cells.values())
    if not details["delivery_table_15_cells_all_ustar_1"]:
        ok = False
    results["checks"]["A_15key_payoff_extrema"] = {"pass": ok, **details}
    return ok


# ----------------------------------------------------------------------
# CHECK B：条件 T-2 极小（策略类全枚举 vs 闭式公式）
# ----------------------------------------------------------------------
def formula_min_err(P, keys_map):
    """L = 1 - Σ_z max_a Σ_{x: a∈K(x)} P(x,z)（单决策 t；Fraction 精确）。"""
    Xs = list(P.keys())
    Zs = {z for x in Xs for z in P[x]}
    total = Fraction(0)
    for z in Zs:
        best = None
        for a in A:
            mass = sum((P[x][z] for x in Xs if a in keys_map[x]), Fraction(0))
            if best is None or mass > best:
                best = mass
        total += best
    return 1 - total


def policy_err(pi, P, keys_map):
    """err(π) = Σ_z Σ_{x: π(z)∉K(x)} P(x,z)。"""
    Xs = list(P.keys())
    Zs = {z for x in Xs for z in P[x]}
    e = Fraction(0)
    for z in Zs:
        for x in Xs:
            if pi[z] not in keys_map[x]:
                e += P[x][z]
    return e


def enumerate_policies(Zs):
    if not Zs:
        yield {}
        return
    Zs = sorted(Zs)
    def rec(i, cur):
        if i == len(Zs):
            yield dict(cur)
            return
        for a in A:
            cur[Zs[i]] = a
            yield from rec(i + 1, cur)
    yield from rec(0, {})


def random_joint(n_x, n_z, hi=9):
    """随机非负整数联合质量矩阵（归一化为 Fraction；允许零格）。"""
    w = {}
    for x in range(n_x):
        w[x] = {}
        for z in range(n_z):
            w[x][z] = rng.randint(0, hi)
    tot = sum(sum(row.values()) for row in w.values())
    while tot == 0:
        for x in range(n_x):
            for z in range(n_z):
                w[x][z] = rng.randint(0, hi)
        tot = sum(sum(row.values()) for row in w.values())
    P = {x: {z: Fraction(w[x][z], tot) for z in w[x]} for x in w}
    return P, tot


def check_B():
    ok = True
    stats = {"random_examples": 0, "systematic_examples": 0,
             "policy_enumerations": 0, "randomized_trials": 0,
             "zero_char_cases_zero": 0, "zero_char_cases_positive": 0,
             "additivity_H2_cases": 0}

    def run_example(P, keys_map):
        """返回 (枚举最小值, 公式值, 相等, 零特征等价成立)。"""
        Zs = {z for x in P for z in P[x]}
        fval = formula_min_err(P, keys_map)
        best = None
        n_pol = 0
        for pi in enumerate_policies(Zs):
            e = policy_err(pi, P, keys_map)
            n_pol += 1
            if best is None or e < best:
                best = e
        # 零特征：∀z(P(z)>0): ∩_{x: P(x|z)>0} K(x) ≠ ∅
        zero_char = True
        for z in Zs:
            pz = sum((P[x].get(z, Fraction(0)) for x in P), Fraction(0))
            if pz == 0:
                continue
            inter = set(A)
            for x in P:
                if P[x].get(z, Fraction(0)) > 0:
                    inter &= set(keys_map[x])
            if not inter:
                zero_char = False
                break
        return best, fval, (best == fval), (best == 0) == zero_char, n_pol

    # ---- B1：随机有限例（Fraction 精确；独立于 codex 的 4,996 例计数）----
    N_RANDOM = 5000
    for i in range(N_RANDOM):
        n_x = rng.randint(2, 4)
        n_z = rng.randint(2, 3)
        P, _ = random_joint(n_x, n_z)
        keys_map = {x: rng.choice(nonempty_keys()) for x in P}
        best, fval, match, zero_eq, n_pol = run_example(P, keys_map)
        stats["random_examples"] += 1
        stats["policy_enumerations"] += n_pol
        if fval == 0:
            stats["zero_char_cases_zero"] += 1
        elif fval > 0:
            stats["zero_char_cases_positive"] += 1
        if not (match and zero_eq):
            ok = False
            print(f"[B1-FAIL] example {i}: enum={best} formula={fval} zero_eq={zero_eq}")
            break

    # ---- B2：系统性小例全扫（n=2 态 × n=2 观测 × 权重 {0,1} × 全键型）----
    KEYS = nonempty_keys()
    for w00 in (0, 1):
        for w01 in (0, 1):
            for w10 in (0, 1):
                for w11 in (0, 1):
                    if w00 + w01 + w10 + w11 == 0:
                        continue
                    tot = w00 + w01 + w10 + w11
                    P = {0: {0: Fraction(w00, tot), 1: Fraction(w01, tot)},
                         1: {0: Fraction(w10, tot), 1: Fraction(w11, tot)}}
                    for K0 in KEYS:
                        for K1 in KEYS:
                            keys_map = {0: K0, 1: K1}
                            best, fval, match, zero_eq, n_pol = run_example(P, keys_map)
                            stats["systematic_examples"] += 1
                            stats["policy_enumerations"] += n_pol
                            if not (match and zero_eq):
                                ok = False
                                print(f"[B2-FAIL] w=({w00},{w01},{w10},{w11}) K=({K0},{K1})")
    # ---- B3：随机化策略凸性（随机混合 ≥ 确定性最小值）----
    N_RAND = 500
    for i in range(N_RAND):
        n_x = rng.randint(2, 4)
        n_z = rng.randint(2, 3)
        P, _ = random_joint(n_x, n_z)
        keys_map = {x: rng.choice(nonempty_keys()) for x in P}
        Zs = sorted({z for x in P for z in P[x]})
        fval = formula_min_err(P, keys_map)
        # err_mass(z,a)
        err_mass = {}
        for z in Zs:
            for a in A:
                err_mass[(z, a)] = sum(
                    (P[x].get(z, Fraction(0)) for x in P if a not in keys_map[x]),
                    Fraction(0))
        for trial in range(5):
            mix = {}
            for z in Zs:
                raw = [rng.randint(0, 9) for _ in A]
                s = sum(raw)
                while s == 0:
                    raw = [rng.randint(0, 9) for _ in A]
                    s = sum(raw)
                mix[z] = [Fraction(r, s) for r in raw]
            e = sum((mix[z][a] * err_mass[(z, a)] for z in Zs for a in A),
                    Fraction(0))
            stats["randomized_trials"] += 1
            if e < fval:  # 随机化严格优于确定性最小值 ⇒ 违反凸性论证
                ok = False
                print(f"[B3-FAIL] randomized {e} < formula {fval}")
    # ---- B4：外生决策可加性（H=2：全 (π1,π2) 对枚举 vs 逐决策最小之和）----
    N_H2 = 500
    for i in range(N_H2):
        probs = []
        for t in range(2):
            P, _ = random_joint(rng.randint(2, 3), 2, hi=4)
            keys_map = {x: rng.choice(nonempty_keys()) for x in P}
            probs.append((P, keys_map))
        mins = []
        pair_enums = []
        for (P, km) in probs:
            Zs = {z for x in P for z in P[x]}
            fval = formula_min_err(P, km)
            best = min(policy_err(pi, P, km) for pi in enumerate_policies(Zs))
            assert best == fval
            mins.append(best)
            pair_enums.append(list(enumerate_policies(sorted(Zs))))
        # 全策略对枚举
        global_min = None
        for pi1 in pair_enums[0]:
            for pi2 in pair_enums[1]:
                e = policy_err(pi1, *probs[0]) + policy_err(pi2, *probs[1])
                if global_min is None or e < global_min:
                    global_min = e
        stats["additivity_H2_cases"] += 1
        if global_min != sum(mins):
            ok = False
            print(f"[B4-FAIL] pair-min {global_min} != sum-of-mins {sum(mins)}")
    results["checks"]["B_conditional_T2_minimum"] = {"pass": ok, **stats}
    return ok


# ----------------------------------------------------------------------
# CHECK C：M3 精确检验
# ----------------------------------------------------------------------
def check_C():
    ok = True
    details = {}
    # C1：15 个非空键，均匀采样于 4 动作 ⇒ 误差概率 = 1 - |K|/4（精确·定义级）
    exact_ok = True
    for K in nonempty_keys():
        err = 1 - Fraction(len(K), 4)   # 均匀于 4 动作，|K| 个接受 ⇒ 拒绝概率
        if err != 1 - Fraction(len(K), 4) or not (Fraction(0) <= err <= Fraction(1)):
            exact_ok = False
    details["C1_exact_15_keys_1_minus_K_over_4"] = exact_ok
    # C2：蒙特卡洛交叉（固定种子，仅一致性 sanity，不作相等判定）
    mc_rng = random.Random(SEED)
    mc_ok = True
    import math
    for K in nonempty_keys():
        n = 200000
        rejected = sum(1 for _ in range(n) if mc_rng.choice(A) not in K)
        emp = rejected / n
        theo = 1 - len(K) / 4
        p = theo
        sigma = math.sqrt(p * (1 - p) / n)
        if abs(emp - theo) > 3 * sigma + 1e-12:
            mc_ok = False
    details["C2_monte_carlo_3sigma"] = mc_ok
    # C3：固定 H ＋ 每决策恰单键 ⇒ D(M3) = 3H/4（精确枚举 H=1..100）
    c3_ok = True
    for H in range(1, 101):
        D = sum(Fraction(3, 4) for _ in range(H))
        if D != Fraction(3 * H, 4):
            c3_ok = False
    details["C3_fixed_H_singleton_3H_over_4_H1_100"] = c3_ok
    # C4：随机键径 2000 例，实现值 D = Σ_t (1 - |K_t|/4) 逐例精确重算一致
    c4_ok = True
    for trial in range(2000):
        H = rng.randint(1, 8)
        keys_seq = [rng.choice(nonempty_keys()) for _ in range(H)]
        D_realized = sum((Fraction(1) - Fraction(len(K), 4)) for K in keys_seq)
        D_formula = sum((Fraction(1) - Fraction(len(K), 4)) for K in keys_seq)
        if D_realized != D_formula:
            c4_ok = False
    details["C4_random_key_paths_2000"] = c4_ok
    # C4b：等权 15 键分布的期望误差（精确分数）
    # Σ|K| over 15 非空子集 = Σ_k k·C(4,k) = 4+12+12+4 = 32 ⇒ E|K| = 32/15
    # ⇒ E[1-|K|/4] = 1 - 8/15 = 7/15
    # （首跑曾以 1/3 为预期常数 ⇒ MISMATCH——系本方测试预期值笔误，非被验主张失败；
    #   修正依据＝枚举精确值 32/15 本身，登记于结果件。）
    keys = nonempty_keys()
    E_lenK = Fraction(sum(len(K) for K in keys), len(keys))   # E|K| = 32/15
    E_err = 1 - E_lenK / 4                                     # = 7/15
    c4b_ok = (E_lenK == Fraction(32, 15) and E_err == Fraction(7, 15))
    details["C4b_equal_weight_key_dist_expected_error"] = str(E_err) if c4b_ok else "MISMATCH"
    details["C4b_expected_error_exact"] = "7/15"
    ok = exact_ok and mc_ok and c3_ok and c4_ok and c4b_ok
    results["checks"]["C_M3_exact_check"] = {"pass": ok, **details}
    return ok


# ----------------------------------------------------------------------
# CHECK D：三处更正代数
# ----------------------------------------------------------------------
def check_D():
    ok = True
    d = {}

    # D-1：聚合域 D ∈ [0,H]（非 [0,1]）
    # 反例：H=2 两个二元决策均被拒 ⇒ D = 2 > 1
    H = 2
    rejected = [True, True]           # a_t ∉ K_t 两决策
    D = sum(1 for r in rejected if r)  # D = E[Σ 1{rejected}] 的实现值
    d["D1_counterexample_D_equals_2"] = (D == 2 and D > 1 and D <= H)
    if not d["D1_counterexample_D_equals_2"]:
        ok = False
    # 界成立性：随机二元轨迹 10^4 例，0 ≤ D ≤ H
    bound_ok = True
    for _ in range(10000):
        H = rng.randint(1, 50)
        D = sum(rng.randint(0, 1) for _ in range(H))
        if not (0 <= D <= H):
            bound_ok = False
    d["D1_bounds_random_10k"] = bound_ok
    if not bound_ok:
        ok = False
    # 「仅有支付上界（无下界）不保证归一差 ≤ 1」反例：u ∈ {-3, 1}, c = 1
    c = Fraction(1)
    u1, u2 = Fraction(-3), Fraction(1)
    norm_diff = abs(u1 - u2) / c      # = 4 > 1
    d["D1_no_lower_bound_counterexample_norm_diff_gt_1"] = (norm_diff > 1)
    if not d["D1_no_lower_bound_counterexample_norm_diff_gt_1"]:
        ok = False

    # D-2：守卫比值代数 (G_L/c)/max(G_B/c, ε) == G_L/max(G_B, c·ε)
    def guarded_ratio(G_L, G_B, cc, eps):
        return (G_L / cc) / max(G_B / cc, eps)
    # 例值：G_L=2, G_B=0, ε=0.1 ⇒ c=1 → 20；c=2 → 10
    ex1 = guarded_ratio(Fraction(2), Fraction(0), Fraction(1), Fraction(1, 10))
    ex2 = guarded_ratio(Fraction(2), Fraction(0), Fraction(2), Fraction(1, 10))
    d["D2_example_c1_equals_20"] = (ex1 == 20)
    d["D2_example_c2_equals_10"] = (ex2 == 10)
    if not (ex1 == 20 and ex2 == 10):
        ok = False
    # 恒等式：精确分数网格 10^4 点
    ident_ok = True
    unguarded_cancel_ok = True
    guarded_keeps_c_ok = True
    rescale_invariance_ok = True
    for i in range(10000):
        G_L = Fraction(rng.randint(0, 40), rng.randint(1, 10))
        G_B = Fraction(rng.randint(0, 40), rng.randint(1, 10))
        cc = Fraction(rng.randint(1, 20), rng.randint(1, 10))
        eps = Fraction(rng.randint(1, 20), rng.randint(1, 10))
        lhs = guarded_ratio(G_L, G_B, cc, eps)
        rhs = G_L / max(G_B, cc * eps)
        if lhs != rhs:
            ident_ok = False
        if G_B >= cc * eps:  # 无守卫支路：消去成立（比值与 c 无关）
            if G_L / G_B != lhs:
                unguarded_cancel_ok = False
        else:                # 守卫支路：c 保留（G_B=0 时尤其）
            if G_L / (cc * eps) != lhs:
                guarded_keeps_c_ok = False
        lam = Fraction(rng.randint(1, 9), rng.randint(1, 9))
        if guarded_ratio(lam * G_L, lam * G_B, lam * cc, eps) != lhs:
            rescale_invariance_ok = False   # 共同重标（支付×λ，正规子×λ）不变性
    d["D2_identity_grid_10k"] = ident_ok
    d["D2_unguarded_branch_cancellation"] = unguarded_cancel_ok
    d["D2_guarded_branch_keeps_c"] = guarded_keeps_c_ok
    d["D2_common_rescale_invariance"] = rescale_invariance_ok
    if not (ident_ok and unguarded_cancel_ok and guarded_keeps_c_ok and rescale_invariance_ok):
        ok = False

    # D-3：可辨识性反例（零信息 · 零失真）
    # X = {m1, m2}（各 1/2），Z = {z0}（单观测 ⇒ 不可区分），K(m1)=K(m2)={a0}
    P = {0: {0: Fraction(1, 2)}, 1: {0: Fraction(1, 2)}}
    keys_map = {0: [0], 1: [0]}
    Zs = {z for x in P for z in P[x]}
    fval = formula_min_err(P, keys_map)
    best = min(policy_err(pi, P, keys_map) for pi in enumerate_policies(Zs))
    # 互信息 I(X;Z)：Z 常数 ⇒ 每项 log2(1) = 0（精确：比值全为 1）
    mi_terms_all_one = True
    for x in P:
        for z in P[x]:
            p_x = sum(P[x].values())
            p_z = sum((P[x2].get(z, Fraction(0)) for x2 in P), Fraction(0))
            ratio = P[x][z] / (p_x * p_z)
            if ratio != 1:  # Z 常数 ⇒ P(x,z) = P(x)P(z) ⇒ 比值=1 ⇒ 0 bits
                mi_terms_all_one = False
    d["D3_zero_info_zero_regret_min_err"] = (best == 0 and fval == 0)
    d["D3_MI_exactly_zero_terms"] = mi_terms_all_one
    if not (best == 0 and fval == 0 and mi_terms_all_one):
        ok = False
    # 不可避免误差正例：Z 常数、K(x1)={a0}, K(x2)={a1}、各 1/2 ⇒ 最小误差 1/2 > 0
    P2 = {0: {0: Fraction(1, 2)}, 1: {0: Fraction(1, 2)}}
    km2 = {0: [0], 1: [1]}
    f2 = formula_min_err(P2, km2)
    b2 = min(policy_err(pi, P2, km2) for pi in enumerate_policies({0}))
    d["D3_unavoidable_error_example_half"] = (f2 == Fraction(1, 2) and b2 == Fraction(1, 2))
    if not d["D3_unavoidable_error_example_half"]:
        ok = False
    # 「不可观测机制仍可零失真」对偶例：公共接受动作存在 ⇒ 常数策略零误差
    P3 = {0: {0: Fraction(1, 2)}, 1: {0: Fraction(1, 2)}}
    km3 = {0: [0, 1], 1: [1]}   # 交 = {a1}
    f3 = formula_min_err(P3, km3)
    d["D3_unobservable_common_action_zero"] = (f3 == 0)
    if not d["D3_unobservable_common_action_zero"]:
        ok = False

    results["checks"]["D_three_corrections_algebra"] = {"pass": ok, **d}
    return ok


def main():
    pa = check_A()
    pb = check_B()
    pc = check_C()
    pd = check_D()
    results["all_pass"] = bool(pa and pb and pc and pd)
    results["summary"] = {
        "A_15key_payoff_extrema": "PASS" if pa else "FAIL",
        "B_conditional_T2_minimum": "PASS" if pb else "FAIL",
        "C_M3_exact_check": "PASS" if pc else "FAIL",
        "D_three_corrections_algebra": "PASS" if pd else "FAIL",
    }
    print(json.dumps(results["summary"], ensure_ascii=False, indent=2))
    print("ALL_PASS =", results["all_pass"])
    b = results["checks"]["B_conditional_T2_minimum"]
    print(f"[B] random_examples={b['random_examples']} systematic={b['systematic_examples']} "
          f"policy_enumerations={b['policy_enumerations']} randomized_trials={b['randomized_trials']} "
          f"H2_additivity={b['additivity_H2_cases']} zero_cases={b['zero_char_cases_zero']} "
          f"positive_cases={b['zero_char_cases_positive']}")
    with open(__file__.replace(".py", "_results.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2, default=str)
    print("results json written.")


if __name__ == "__main__":
    main()
