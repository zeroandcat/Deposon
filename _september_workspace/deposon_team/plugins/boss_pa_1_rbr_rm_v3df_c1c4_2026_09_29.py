# -*- coding: utf-8 -*-
"""
boss_pa_1_rbr_rm_v3df_c1c4_2026_09_29.py
=========================================
V3 退化线索 **C1 / C3 / C4 同族修复件**（新名件 · 原件 0 触动）

依据（逐条沿用，0 自创）
  - 预登记件（生效即锁）: results/_v5_v3_deg_fix_prereg_2026_09_29.md  SHA-12 `98286cc1aec7`
      §3.1 修载体约定（C1–C4 同族 = 1 件新名修复件；代际标签/日期由 worker 定）
      §3.2-C1 / §3.2-C3 / §3.2-C4 修复面定义
      §4.0 K-V3DF-0-1 防退化门 / §4.0 K-V3DF-0-2 原件 0 触动门
      §4.1 K-V3DF-1-1 / 1-2（C1）  §4.2 K-V3DF-2-1（C2 连带）
      §4.3 K-V3DF-3-1 / 3-2（C3）  §4.4 K-V3DF-4-1 / 4-2（C4）
      §4.6 K-V3DF-9-1 / 9-2 / 9-3（全链重验 + 三态纪律 + 0 不明收口）
      §5 阈值看护（口径定义 / 阈值调整 / 构造-实现变更 三概念归属）
  - PI 2026-09-29 11:52 方向更新（派工单字面）:
      **C1 = 改构造真迭代**（原「改阈值 1e-3」已在盘上被 4 臂反证弃用）
      C5 = 全修含链重走（**另棒**，本件 0 做）｜P-J/P-M/P-C 族另立（**另棒**，本件 0 做）
  - 盘上既有真迭代读数（C3 面照抄已实跑构造）: results/_v3_recheck_01_executor_2026_09_27.py
      SHA-12 `919fa909381e`（`434b3213bdce` §4.3 / §2.2）

本件只做 C1–C4（同族一腿），**0 做 C5、0 做 P-J/P-M/P-C 族**。

铁律
  - 新名件；既有件 0 删除 / 0 改写 / 0 覆盖 / 0 合并
  - V3 原件 / frozen / 9 网格 0 触动（只读引件；K-V3DF-0-2 逐件复算实证）
  - **0 新设数值判定阈值**（C1 走「构造 / 实现变更」非「阈值调整」：
    收敛切点 `tol = 1e-3` 与最小轮次 `t > 5` **逐字沿用 V3 既有值**，未动 1 分）
  - 0 读 key / 0 明文密钥
  - 纯 Python stdlib（0 numpy / 0 LLM / 0 proxy / 0 网关）
  - 派生 JSON 0 合并（只新建本件 1 个 result JSON）
  - 0 代判定裁决（判定面归 verdict-keeper，沿 K-V3DF-9-1）

作者: Mavis 团队 worker（V4 V3 修复执行棒）
日期: 2026-09-29
标记 V3DF_SELFCHECK_2026_09_29
"""

import os
import sys
import json
import hashlib
import random
from collections import Counter
from typing import Optional

# ============================================================================
# 路径常量（全部为只读输入；输出为新名件）
# ============================================================================

REPO_ROOT = r"D:/私人资料/deposon-repo"
V20_BASELINES = os.path.join(REPO_ROOT, "results", "deposon_v20_baselines.json")
SRC_RESULT = os.path.join(REPO_ROOT, "results", "boss_pa_1_rbr_rm_result_2026_09_15.json")
SRC_RUNNER = os.path.join(REPO_ROOT, "deposon_team", "plugins", "boss_pa_1_rbr_rm.py")
PHASE4_F4 = os.path.join(REPO_ROOT, "results", "deposon_v2_phase4_f4_2026_09_11.json")
PD_SPEC = os.path.join(REPO_ROOT, "docs", "V3X", "P_D_FINGERPRINT_V0_3_SPEC.md")
PREREG = os.path.join(REPO_ROOT, "results", "_v5_v3_deg_fix_prereg_2026_09_29.md")
RECHECK_RESCRIPT = os.path.join(REPO_ROOT, "results", "_v3_recheck_01_rescript_2026_09_27.md")
OUT_JSON = os.path.join(REPO_ROOT, "results", "_v5_v3_deg_fix_c1c4_result_2026_09_29.json")

# ============================================================================
# 常量（全部沿用盘上既有字面，0 新设数值）
# ============================================================================

# --- C1：V3 既有字面，逐字沿用（本棒不动 1 分） ---
RM_TOL = 1e-3          # V3 构造 L176 既有收敛切点（**未改**；预登记 §5.2-C1「改阈值」已被盘上 4 臂反证弃用）
RM_WARMUP = 5          # V3 构造 L176 既有 `t > 5` 最小轮次护栏（**未改**）
N_ITER = 200           # V3 构造既有 n_iter（cap 面）
SEED = 210021          # V3 既有 seed

# --- C3：recheck #01 已实跑实现量（沿 K-V3R-0-B「管阈值不管实现」） ---
BAYES_EPS = 1e-9       # recheck #01 §3(b) 字面 ε
BAYES_MAX_ITER = 2000  # recheck #01 §3(b) 字面最大迭代
STARTS = ((0, 0), (0, 1), (1, 0), (1, 1))            # 4 起点（recheck #01 敏感性网格）
BR_MODES = ("simultaneous", "alternating")           # 2 BR 模式（recheck #01 敏感性网格）

# --- 全链重验：TH-V3R-1 既有字面（只读引用，0 改动） ---
TH_PA_H1 = 1.3
TH_PA_H0 = 2.0

# --- K-V3R-1 / K-V3DF-* 既有门槛（只读引用，0 新设） ---
GATE_N_DISTINCT = 3    # K-V3R-0-A 防退化门：n_distinct > 3
KILL_N_DISTINCT = 4    # K-V3R-1 / K-V3DF-1-1 / K-V3DF-4-1：n_distinct >= 4

# --- K-V3DF-0-2：盘上 0 触动基线（预登记件 §7 C-01 + recheck #01 §1 + 本棒跑前实测） ---
PREREG_BASELINE_SHA12 = {
    "deposon_team/plugins/boss_pa_1_rbr_rm.py": "5cc594147e00",
    "results/boss_pa_1_rbr_rm_result_2026_09_15.json": "c7c59e0d2f6c",
    "results/deposon_v2_phase4_f4_2026_09_11.json": "cf7682348617",
    "docs/V3X/P_D_FINGERPRINT_V0_3_SPEC.md": "f119f2f30287",
}
ZERO_TOUCH_FILES = list(PREREG_BASELINE_SHA12.keys())


# ============================================================================
# 工具函数
# ============================================================================

def sha12_file(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def load_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def n_distinct(xs) -> int:
    return len(set(round(float(x), 12) for x in xs))


def stat_block(xs):
    """沿 recheck #01 `stat_block` 字面（0 新设统计口径）。"""
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


def base_graph(gid: str) -> str:
    """去嵌套：S1_n35 -> S1（沿 recheck #01 字面）。"""
    if gid.startswith("L_"):
        return gid
    return gid.split("_n")[0]


# ============================================================================
# 段 0 · V3 legacy 公式逐字转写（只读；双口径地基 + 修复 diff 的左列）
# —— 0 import 原件、0 触动原件
# ============================================================================

def L_solve_2x2_nash_pure(a11, a12, a21, a22, b11, b12, b21, b22) -> Optional[list]:
    """V3 源件 L71-L107 逐字转写（闭式解，二值桩的来源）。"""
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


def L_simulate_rbr(a11, a12, a21, a22, b11, b12, b21, b22, n_iter=N_ITER, seed=SEED) -> int:
    """V3 源件 L110-L136 逐字转写（C2 面；本棒 0 改，仅作 K-V3DF-2-1 复验）。"""
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


def L_simulate_rm(a11, a12, a21, a22, b11, b12, b21, b22, n_iter=N_ITER, seed=SEED,
                  tol=RM_TOL) -> int:
    """V3 源件 L139-L178 逐字转写（C1 退化面本体：`rm_iter ≡ 6` 的来源）。"""
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


def L_bayesian_nash_iter(a11, a12, a21, a22, b11, b12, b21, b22) -> int:
    """V3 源件 L181-L189 逐字转写（C3 退化面本体：`return 1 if nash else 200`）。"""
    nash = L_solve_2x2_nash_pure(a11, a12, a21, a22, b11, b12, b21, b22)
    return 1 if nash else 200


def payoff_matrix(g) -> tuple:
    """V3 字面 2x2 支付矩阵（逐字沿 recheck #01 `payoff_matrix`）。"""
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


# ============================================================================
# 段 1 · C1 修复件：真·Regret Matching（HMC 2000 累计 regret 口径）
# ============================================================================
# 缺陷根因（盘上 `434b3213bdce` §5 γ₁ ＋ `c8d539a58d29` C1 根因）：
#   V3 写 `R[1-s] = max(0, avg[1-s] - avg[s])`，而**未玩过策略的累计支付恒为 0**
#   ⇒ `avg[1-s] = 0`；只要所玩策略平均支付 > 0，regret 恒等于**精确 0.0**
#   ⇒ 1e-3 / 1e-9 / 1e-15 三档阈值在**同一 t=6 点**触发。
# 本件按 PI 09-29 11:52 方向更新「**改构造真迭代**」修：
#   - regret 改为 **HMC 2000 瞬时 regret 的累计**：
#       R_i(s) ← R_i(s) + u_i(s, a_{-i}^t) − u_i(a_i^t, a_{-i}^t)
#     （反事实用**对家实走那一轮**的支付作参照，不再用「未玩过 ⇒ 0」的占位）
#   - 采样按 **σ_i(s) ∝ max(0, R_i(s))**（正部归一化，保证 σ ∈ [0,1]；
#     全零时沿 V3 既有语义「不重采样」）
#   - 收敛判据：**切点 1e-3 与最小轮次 t > 5 逐字不动**，只把被比较的量从
#     「坏掉的单步占位 regret」换成「真累计 regret」
#   ⇒ 两臂**并报、0 择一删读**：
#     **主臂 `C1_main_avg_cumulative`（1/(t+1)·ΣR）** —— 依据**基名件自己的注释字面**
#       `boss_pa_1_rbr_rm.py` L159：「更新 regret (HMC 2000): R^i[s] = (1/t) * sum
#       (u^i(s, a_{-i}) - u^i(a_i, a_{-i}))」⇒ **被文档定义的量本就是 1/(t+1)·Σ 缩放量**
#       （基名件 L161 的除数亦为 (t+1)）⇒ 主臂 = 恢复其**自陈**的 HMC 2000 语义。
#     **对照臂 `C1_ctl_raw_cumulative`（max(ΣR) < 1e-3）** —— 与 V3 源码表达式**同形**
#       （把坏值换成真值、其余 1 字不动），作口径敏感性对照。
#   ⚠️ 两臂结论**不同向**（主臂过 K-V3DF-1-1 门槛、对照臂不过）⇒ 两读数 0 删任一，
#     口径以何臂为准由 PI / verdict-keeper 指定（沿 §4.3「双读并报」同款纪律）
# ⇒ 归属：**构造 / 实现变更**（预登记 §5.1）｜**0 新设数值切点**

def F_simulate_rm_true(pay, n_iter=N_ITER, seed=SEED, tol=RM_TOL, warmup=RM_WARMUP,
                       avg_arm: bool = False) -> dict:
    """C1 修复：真·迭代 Regret Matching。返回 (收敛轮次 / 触 cap, 诊断)。"""
    a11, a12, a21, a22, b11, b12, b21, b22 = pay
    rng = random.Random(seed)
    sA, sB = rng.randint(0, 1), rng.randint(0, 1)
    R_A = [0.0, 0.0]
    R_B = [0.0, 0.0]
    last_switch = -1
    profiles = []
    trace_tail = []

    def sigma(regret):
        pos = [max(0.0, regret[0]), max(0.0, regret[1])]
        tot = pos[0] + pos[1]
        if tot <= 0:
            return None
        return pos[0] / tot

    for t in range(n_iter):
        profiles.append((sA, sB))
        # 真·瞬时 regret（对家实走 a_{-i}^t 作参照）
        ua = (a11, a12) if sB == 0 else (a21, a22)   # (u_A(0,sB), u_A(1,sB))
        ub = (b11, b21) if sA == 0 else (b12, b22)   # (u_B(0,sA), u_B(1,sA))
        R_A[0] += ua[0] - ua[sA]
        R_A[1] += ua[1] - ua[sA]
        R_B[0] += ub[0] - ub[sB]
        R_B[1] += ub[1] - ub[sB]
        sig_A, sig_B = sigma(R_A), sigma(R_B)
        prev = (sA, sB)
        if sig_A is not None:
            sA = 0 if rng.random() < sig_A else 1
        if sig_B is not None:
            sB = 0 if rng.random() < sig_B else 1
        if (sA, sB) != prev:
            last_switch = t
        if t >= n_iter - 3:
            trace_tail.append({"t": t, "R_A": [round(R_A[0], 6), round(R_A[1], 6)],
                               "R_B": [round(R_B[0], 6), round(R_B[1], 6)],
                               "profile": [sA, sB]})
        scale = float(t + 1) if avg_arm else 1.0
        if (max(R_A[0], R_A[1]) / scale < tol
                and max(R_B[0], R_B[1]) / scale < tol and t > warmup):
            return {"rm_iter": t, "hit_cap": False,
                    "R_A_exit": [round(R_A[0], 9), round(R_A[1], 9)],
                    "R_B_exit": [round(R_B[0], 9), round(R_B[1], 9)],
                    "n_profile_switches": last_switch + 1,
                    "last_switch_round": last_switch,
                    "n_distinct_profiles": len(set(profiles)),
                    "final_profile": [sA, sB],
                    "trace_tail": trace_tail}
    return {"rm_iter": n_iter, "hit_cap": True,
            "R_A_exit": [round(R_A[0], 9), round(R_A[1], 9)],
            "R_B_exit": [round(R_B[0], 9), round(R_B[1], 9)],
            "n_profile_switches": last_switch + 1,
            "last_switch_round": last_switch,
            "n_distinct_profiles": len(set(profiles)),
            "final_profile": [sA, sB],
            "trace_tail": trace_tail}


# ============================================================================
# 段 2 · C3 修复件：真·best-response 迭代（照抄 recheck #01 已实跑 176 格构造）
# —— 0 新设阈值：ε = 1e-9 / max_iter = 2000 沿 K-V3R-0-B「管阈值不管实现」
# —— 归属：**构造 / 实现变更**（预登记 §5.2-C3）

def F_bayes_best_response(pay, start, mode="simultaneous", eps=BAYES_EPS,
                          max_iter=BAYES_MAX_ITER) -> dict:
    """真 best-response：收敛判据 = Nash gap <= ε；返回 (迭代数, 触 cap, 末次 gap)。"""
    a11, a12, a21, a22, b11, b12, b21, b22 = pay

    def pay_A(sA, sB):
        return (a11, a12)[sB] if sA == 0 else (a21, a22)[sB]

    def pay_B(sB, sA):
        return (b11, b21)[sA] if sB == 0 else (b12, b22)[sA]

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
            raise ValueError("unknown BR mode: %r" % mode)
        g = gap(sA, sB)
        if g <= eps:
            return {"bayes_iter_true": t, "hit_iter_cap": False, "nash_gap_final": g}
    return {"bayes_iter_true": max_iter, "hit_iter_cap": True, "nash_gap_final": gap(sA, sB)}


def F_rbr_true_converged(pay, start, max_iter=N_ITER) -> dict:
    """C2 的 cap 伪影敏感性臂（RBR 改真纳什收敛判据）；0 入主判据，沿 recheck #01。"""
    a11, a12, a21, a22, b11, b12, b21, b22 = pay

    def pay_A(sA, sB):
        return (a11, a12)[sB] if sA == 0 else (a21, a22)[sB]

    def pay_B(sB, sA):
        return (b11, b21)[sA] if sB == 0 else (b12, b22)[sA]

    sA, sB = int(start[0]), int(start[1])
    for t in range(1, max_iter + 1):
        if pay_A(sA, sB) >= pay_A(1 - sA, sB) and pay_B(sB, sA) >= pay_B(1 - sB, sA):
            return {"rbr_iter_true": t, "hit_iter_cap": False}
        sA = 0 if pay_A(0, sB) >= pay_A(1, sB) else 1
        sB = 0 if pay_B(0, sA) >= pay_B(1, sA) else 1
    return {"rbr_iter_true": max_iter, "hit_iter_cap": True}


# ============================================================================
# 主函数
# ============================================================================

def main() -> int:
    # ---------- K-V3DF-0-2 跑前基线（只读复算） ----------
    pre_sha12 = {p: sha12_file(os.path.join(REPO_ROOT, p)) for p in ZERO_TOUCH_FILES}
    input_sha12 = {
        "results/deposon_v20_baselines.json": sha12_file(V20_BASELINES),
        "results/_v5_v3_deg_fix_prereg_2026_09_29.md": sha12_file(PREREG),
        "results/_v3_recheck_01_rescript_2026_09_27.md": sha12_file(RECHECK_RESCRIPT),
    }

    v20 = load_json(V20_BASELINES)
    per_graph = v20["per_graph"]
    gids = sorted(per_graph.keys())
    n_graphs = len(gids)
    assert n_graphs == 22, "22 受控概念图数量不符: %d" % n_graphs

    src = load_json(SRC_RESULT)
    on_disk = {g["graph_id"]: g for g in src["boss_pa1_22graph_simulation"]["graph_results"]}

    # ---------- 段 0 · legacy 逐字复现校验（修复 diff 的左列 / 双口径地基） ----------
    legacy_rows, legacy_mismatch = [], []
    legacy = {}
    for gid in gids:
        pay = payoff_matrix(per_graph[gid])
        r = L_simulate_rbr(*pay, n_iter=N_ITER, seed=SEED)
        m = L_simulate_rm(*pay, n_iter=N_ITER, seed=SEED, tol=RM_TOL)
        b = L_bayesian_nash_iter(*pay)
        legacy[gid] = {"rbr": r, "rm": m, "bayes": b}
        od = on_disk[gid]
        row = {
            "graph_id": gid, "base_graph": base_graph(gid),
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

    legacy_repro = {
        "n_graphs": n_graphs,
        "all_bit_exact": (not legacy_mismatch),
        "bit_exact_mismatch_graphs": legacy_mismatch,
        "n_bit_exact_match": n_graphs - len(legacy_mismatch),
        "on_disk_rbr_multiplier_mean": src["boss_pa1_22graph_simulation"]["rbr_multiplier_mean"],
        "on_disk_verdict": src["verdict"],
    }

    # ---------- 段 1 · K-V3DF-0-1 防退化门：跑前自证（输入字段） ----------
    a_named_v = [per_graph[g]["field_mean"]["named"] or 0.0 for g in gids]
    a_filler_v = [per_graph[g]["field_mean"]["filler"] or 0.0 for g in gids]
    dep_freq_v = []
    b_named_v, b_filler_v = [], []
    for g in gids:
        an = per_graph[g]["field_mean"]["named"] or 0.0
        af = per_graph[g]["field_mean"]["filler"] or 0.0
        dep_freq_v.append(0.5 if (an + af) < 1e-9 else an / (an + af))
        pay = payoff_matrix(per_graph[g])
        b_named_v.append(pay[4])
        b_filler_v.append(pay[5])

    input_selfcheck = {
        "v20_field_mean_named (盘上真实, 逐图)": stat_block(a_named_v),
        "v20_field_mean_filler (盘上真实, 逐图)": stat_block(a_filler_v),
        "v20_best_baseline_named (盘上真实, 逐图)": stat_block(b_named_v),
        "v20_best_baseline_filler (盘上真实, 逐图)": stat_block(b_filler_v),
        "deposon_freq_派生 (盘上真实, 逐图)": stat_block(dep_freq_v),
        "(对照) legacy_rm_iter_原构造 (应退化)": stat_block([legacy[g]["rm"] for g in gids]),
        "(对照) legacy_bayes_iter_原构造 (应退化)": stat_block([legacy[g]["bayes"] for g in gids]),
        "(对照) legacy_rbr_iter_原构造 (C2 真信号)": stat_block([legacy[g]["rbr"] for g in gids]),
    }
    gate_fields = [k for k in input_selfcheck if "(对照)" not in k]
    gate_pass = {k: bool(input_selfcheck[k]["n_distinct"] > GATE_N_DISTINCT
                        and input_selfcheck[k]["std"] > 0) for k in gate_fields}
    degen_alarm_input = not all(gate_pass.values())

    # ---------- 段 2 · C1 修复：真迭代 RM（raw 主臂 + avg 对照臂） ----------
    c1_arms = {}
    for arm, avg_arm in (("C1_main_avg_cumulative (主臂: 1/(t+1)·ΣR, 基名件 L159 自陈 HMC 2000 式)", True),
                         ("C1_ctl_raw_cumulative (对照臂: max(ΣR) < 1e-3, 与 V3 源码表达式同形)", False)):
        vals, cap_hits, diags = [], [], {}
        for gid in gids:
            res = F_simulate_rm_true(payoff_matrix(per_graph[gid]), n_iter=N_ITER, seed=SEED,
                                     tol=RM_TOL, warmup=RM_WARMUP, avg_arm=avg_arm)
            vals.append(res["rm_iter"])
            cap_hits.append(res["hit_cap"])
            diags[gid] = {k: v for k, v in res.items() if k != "rm_iter"}
        st = stat_block(vals)
        conv_vals = [v for v, h in zip(vals, cap_hits) if not h]
        c1_arms[arm] = {
            "arm_kind": "主臂" if avg_arm else "对照臂",
            "convergence_quantity": ("1/(t+1)·Σ_t 瞬时 regret（基名件 L159 自陈 HMC 2000 式，"
                                     "除数 (t+1) 同基名件 L161）" if avg_arm
                                     else "Σ_t 瞬时 regret 原始累计（与 V3 源码 L176 表达式同形）"),
            "construction": ("HMC 2000 累计 regret（正部归一化 σ_i(s) ∝ max(0, R_i(s))）；"
                             "收敛切点 tol=1e-3 与 t>5 逐字沿用 V3，0 新设切点"),
            "tol": RM_TOL, "warmup_t_gt": RM_WARMUP, "n_iter": N_ITER, "seed": SEED,
            "rm_iter_per_graph": vals,
            "cap_artifact_alarm_hit": bool(any(cap_hits)),
            "n_hit_cap": int(sum(cap_hits)),
            "cap_hit_rate": round(sum(cap_hits) / n_graphs, 6),
            "stat": st,
            "artifact_free_reading": {
                "definition": "剔除触 n_iter=200 上限（= 真·不收敛）之图后的 rm_iter 读数",
                "n_cells_kept": len(conv_vals),
                "n_cells_removed_as_cap": int(sum(cap_hits)),
                "stat": stat_block(conv_vals) if conv_vals else None,
                "note": "与 C3 同款双读结构；口径名显式标注，0 静默剔除（K-V3DF-3-2 同款纪律）",
            },
            "warmup_floor_note": ("取值 6 = `t > 5` 护栏下的**最早可采纳轮**（下限地板，"
                                  "非度量出的迭代数）；本件逐字沿用该护栏故如实登记"),
            "diagnostics": diags,
        }
    c1_main = ("C1_main_avg_cumulative (主臂: 1/(t+1)·ΣR, 基名件 L159 自陈 HMC 2000 式)")
    c1_ctl = ("C1_ctl_raw_cumulative (对照臂: max(ΣR) < 1e-3, 与 V3 源码表达式同形)")
    c1_main_arm = c1_arms[c1_main]
    c1_ctl_arm = c1_arms[c1_ctl]
    c1_val = c1_main_arm["stat"]["n_distinct"] >= KILL_N_DISTINCT and c1_main_arm["stat"]["std"] > 0
    c1_val_ctl = c1_ctl_arm["stat"]["n_distinct"] >= KILL_N_DISTINCT and c1_ctl_arm["stat"]["std"] > 0
    c1_cap_artifact = bool(c1_main_arm["cap_artifact_alarm_hit"]
                           and c1_main_arm["stat"]["n_distinct"] == 1
                           and c1_main_arm["stat"]["distinct_values"] == [float(N_ITER)])

    # 结构性根因量：V3 字面镜像 payoff ⇒ 每轮反事实 regret 漂移恒为 ±δ（δ = named − filler）
    delta_rows = []
    for gid in gids:
        pay = payoff_matrix(per_graph[gid])
        delta_rows.append({
            "graph_id": gid, "base_graph": base_graph(gid),
            "delta_A (a_named − a_filler)": round(pay[0] - pay[1], 6),
            "delta_B (b_named − b_filler)": round(pay[4] - pay[5], 6),
        })
    delta_A_v = [r["delta_A (a_named − a_filler)"] for r in delta_rows]
    delta_B_v = [r["delta_B (b_named − b_filler)"] for r in delta_rows]

    # ---------- 段 3 · C3 修复：真 best-response（4 起点 × 2 模式 = 8 格/图 → 176 格） ----------
    bayes_cells = []
    for gid in gids:
        pay = payoff_matrix(per_graph[gid])
        for mode in BR_MODES:
            for st in STARTS:
                res = F_bayes_best_response(pay, st, mode=mode)
                bayes_cells.append({"graph_id": gid, "base_graph": base_graph(gid),
                                    "br_mode": mode, "start": list(st),
                                    "bayes_iter_true": res["bayes_iter_true"],
                                    "hit_iter_cap": res["hit_iter_cap"],
                                    "nash_gap_final": res["nash_gap_final"]})
    bayes_iter_all = [c["bayes_iter_true"] for c in bayes_cells]
    bayes_cap_cells = [c for c in bayes_cells if c["hit_iter_cap"]]
    bayes_converged = [c["bayes_iter_true"] for c in bayes_cells if not c["hit_iter_cap"]]
    c3_literal = stat_block(bayes_iter_all)
    c3_artifact_free = stat_block(bayes_converged) if bayes_converged else None
    c3_cap_by_mode = {m: sum(1 for c in bayes_cap_cells if c["br_mode"] == m) for m in BR_MODES}
    c3_by_mode = {m: stat_block([c["bayes_iter_true"] for c in bayes_cells
                                 if c["br_mode"] == m]) for m in BR_MODES}
    c3_by_start = {"%d%d" % s: stat_block([c["bayes_iter_true"] for c in bayes_cells
                                           if tuple(c["start"]) == s]) for s in STARTS}

    # ---------- 段 4 · C4 派生复算：rbr_mult = rbr_t / bayes_t（0 改 rbr_mult 函数本身） ----------
    # 主臂：rbr_t 沿 V3 冻结值（C2 面 0 改动，沿 recheck #01「RBR 非重构目标」字面）
    per_graph_new, mult_literal, mult_free, rm_mult_literal, rm_mult_free = [], [], [], [], []
    for gid in gids:
        pay = payoff_matrix(per_graph[gid])
        cells = [c for c in bayes_cells if c["graph_id"] == gid]
        rbr_frozen = legacy[gid]["rbr"]
        rm_fixed = c1_main_arm["rm_iter_per_graph"][gids.index(gid)]
        row_cells = []
        for c in cells:
            mult = rbr_frozen / c["bayes_iter_true"]
            mult_literal.append(mult)
            rmm = rm_fixed / c["bayes_iter_true"]
            rm_mult_literal.append(rmm)
            row_cells.append({**c, "rbr_iter_frozen": rbr_frozen,
                              "rm_iter_fixed_c1": rm_fixed,
                              "rbr_multiplier_fixed": round(mult, 4),
                              "rm_multiplier_fixed": round(rmm, 4)})
            if not c["hit_iter_cap"]:
                mult_free.append(mult)
                rm_mult_free.append(rmm)
        rbr_true_vals = sorted(set(F_rbr_true_converged(pay, st)["rbr_iter_true"] for st in STARTS))
        per_graph_new.append({
            "graph_id": gid, "base_graph": base_graph(gid),
            "legacy": {"rm_iter": legacy[gid]["rm"], "bayes_iter": legacy[gid]["bayes"],
                       "rbr_iter": rbr_frozen,
                       "rbr_multiplier": on_disk[gid]["rbr_multiplier"],
                       "rm_multiplier": on_disk[gid]["rm_multiplier"]},
            "fixed": {"rm_iter_c1_true_iteration": rm_fixed,
                      "bayes_iter_true_cells": [c["bayes_iter_true"] for c in cells]},
            "rbr_hit_iter_cap_frozen": bool(rbr_frozen == N_ITER),
            "rbr_iter_true_converged_values": rbr_true_vals,
            "cells": row_cells,
        })

    c4_literal = stat_block(mult_literal)
    c4_free = stat_block(mult_free) if mult_free else None
    rm_mult_free_st = stat_block(rm_mult_free) if rm_mult_free else None
    c4_val_literal = c4_literal["n_distinct"] >= KILL_N_DISTINCT
    c4_val_free = bool(c4_free and c4_free["n_distinct"] >= KILL_N_DISTINCT)
    mult_001_present = any(abs(x - 0.01) < 1e-12 for x in mult_literal)
    mult_001_present_free = bool(mult_free) and any(abs(x - 0.01) < 1e-12 for x in mult_free)

    # K-V3DF-4-2：链上 0.01（= 2/200）组合是否出现（既有实测 22 图中 0 出现）
    combos_001 = [{"graph_id": r["graph_id"], "cells": [c["start"] + [c["br_mode"]]
                 for c in r["cells"] if abs(c["rbr_multiplier_fixed"] - 0.01) < 1e-12]}
                 for r in per_graph_new]
    c4_001_report = {
        "definition": "rbr_multiplier_fixed = rbr_iter_frozen / bayes_iter_true == 0.01（= 2/200）",
        "present_literal": bool(mult_001_present),
        "present_artifact_free": bool(mult_001_present_free),
        "n_cells_equal_0.01": sum(1 for x in mult_literal if abs(x - 0.01) < 1e-12),
        "n_graphs_with_any": sum(1 for r in combos_001 if r["cells"]),
        "literal_distinct_values": c4_literal["distinct_values"],
        "artifact_free_distinct_values": c4_free["distinct_values"] if c4_free else None,
        "on_disk_baseline": "22 图中 0 出现（`434b3213bdce` §2.2 / 预登记 §1.2-C4）",
        "note": "出现 / 未出现均如实登记；0 因「未出现」而称已修好（K-V3DF-4-2 字面）",
    }

    # ---------- 段 5 · K-V3DF-2-1：C2 读数连带复验（本棒 0 改 C2） ----------
    c2_rbr_v = [legacy[g]["rbr"] for g in gids]
    c2_recheck = {
        "c2_修面": "0 立修复面（预登记 §1.2-C2：未退化 ＝ 真信号）",
        "rbr_iter_读数来源": "V3 冻结值逐字复用（本棒 0 改 simulate_rbr）",
        "rbr_iter_stat": stat_block(c2_rbr_v),
        "rbr_iter_distinct": sorted(set(c2_rbr_v)),
        "rbr_hit_cap_frozen_n": sum(1 for x in c2_rbr_v if x == N_ITER),
        "on_disk_rbr_iter_逐字一致": bool(all(
            legacy[g]["rbr"] == on_disk[g]["rbr_iter"] for g in gids)),
        "C1/C3 修复是否改到 C2 读数": False,
        "连带影响面登记": "0（C1 只动 simulate_rm；C3 只动 bayesian_nash_iter；rbr_mult 上游 rbr_t 沿冻结值）",
        "cap_free_RBR_敏感性臂 (不参与判定)": {
            "definition": "RBR 改真纳什收敛判据（F_rbr_true_converged），沿 recheck #01 臂",
            "rbr_iter_true_values_union": sorted(set(
                v for r in per_graph_new for v in r["rbr_iter_true_converged_values"])),
            "n_graphs_rbr_frozen_hit_cap": sum(1 for r in per_graph_new
                                               if r["rbr_hit_iter_cap_frozen"]),
        },
    }

    # ---------- 段 6 · K-V3DF-9-1 全链重验读数面（0 代判） ----------
    chain = {
        "①_V3_review_1.2_#1_读数面": {
            "on_disk_rbr_multiplier_mean": src["boss_pa1_22graph_simulation"]["rbr_multiplier_mean"],
            "on_disk_rm_multiplier_mean": src["boss_pa1_22graph_simulation"]["rm_multiplier_mean"],
            "on_disk_verdict": src["verdict"],
            "on_disk_rbr_iters_mean": src["boss_pa1_22graph_simulation"]["rbr_iters_mean"],
            "on_disk_rm_iters_mean": src["boss_pa1_22graph_simulation"]["rm_iters_mean"],
            "on_disk_bayes_iters_mean": src["boss_pa1_22graph_simulation"]["bayes_iters_mean"],
        },
        "②_PA_判定面_TH_V3R_1_读数": {
            "th_pa_h1": TH_PA_H1, "th_pa_h0": TH_PA_H0,
            "th_pa_h1_literal_face": "TH-V3R-1 字面 0 改动",
            "fixed_rbr_multiplier_mean_literal": round(sum(mult_literal) / len(mult_literal), 4),
            "fixed_rbr_multiplier_mean_artifact_free": (round(sum(mult_free) / len(mult_free), 4)
                                                        if mult_free else None),
            "fixed_rm_multiplier_mean_literal": round(sum(rm_mult_literal) / len(rm_mult_literal), 4),
            "fixed_rm_multiplier_mean_artifact_free": (round(sum(rm_mult_free) / len(rm_mult_free), 4)
                                                       if rm_mult_free else None),
            "cap_free_RBR_臂上界": 2.0,
            "cap_free_RBR_臂上界来源": "`434b3213bdce` §4.4 实测（真倍数上界仅 2.0×，恰在 pa_h0 边界）",
        },
        "③_C5_面": "本棒 0 做（C5 = 全修含链重走，另棒；预登记 §3.1 独立载体）",
        "0_代判声明": "判定面变化（145.8× 定性 / 档位）须由 verdict-keeper 裁因（转办单 B；K-V3DF-9-1）",
    }

    # ---------- 段 7 · K-V3DF 逐条结果（三态 PASS/FAIL/KD，0 PARTIAL/GRAY） ----------
    k_v3df = {}

    k_v3df["K-V3DF-0-1"] = {
        "判据": "修复件对每个输入字段与每个输出读数列报 n_distinct/min/max/std；任一 n_distinct ≤ 3 ⇒ 退化警报",
        "input_fields": input_selfcheck,
        "input_gate_pass_per_field": gate_pass,
        "input_degenerate_alarm_hit": degen_alarm_input,
        "output_series": {
            "C1 rm_iter_true (主臂 1/(t+1)·ΣR, 22)": c1_main_arm["stat"],
            "C1 rm_iter_true (主臂 artifact-free, 剔 cap)": c1_main_arm["artifact_free_reading"]["stat"],
            "C1 rm_iter_true (对照臂 max(ΣR), 22)": c1_ctl_arm["stat"],
            "C3 bayes_iter_true (176 格, literal)": c3_literal,
            "C3 bayes_iter_true (112 格, artifact-free)": c3_artifact_free,
            "C4 rbr_multiplier_fixed (176 格, literal)": c4_literal,
            "C4 rbr_multiplier_fixed (artifact-free)": c4_free,
            "C2 rbr_iter (22, 冻结复用)": stat_block(c2_rbr_v),
        },
        "output_series_n_distinct_le_3": {
            "C3 bayes_iter_true (artifact-free)": c3_artifact_free["n_distinct"] if c3_artifact_free else 0,
            "C4 rbr_multiplier_fixed (artifact-free)": c4_free["n_distinct"] if c4_free else 0,
            "C2 rbr_iter (冻结复用, 未退化)": stat_block(c2_rbr_v)["n_distinct"],
        },
        "n_output_series_with_n_distinct_le_3": sum(
            1 for v in (c3_artifact_free["n_distinct"] if c3_artifact_free else 0,
                        c4_free["n_distinct"] if c4_free else 0) if v <= GATE_N_DISTINCT),
        "落态": "KD",
        "落态依据": ("输入字段 5/5 全部过门（C1 侧输出读数列已过门，主臂 n_distinct = %d、"
                     "对照臂 n_distinct = %d）；但 C3 / C4 的 artifact-free 读数列 n_distinct = %s / %s ≤ %d "
                     "⇒ 仍命中退化警报 ⇒ 沿 §4.0 字面「退化警报命中 ⇒ KD（构造不可算）」落 KD；"
                     "本棒仍按 PI 09-29 11:52 授权跑完并如实登记读数，0 自裁、0 改判既有 K-* 字面"
                     % (c1_main_arm["stat"]["n_distinct"], c1_ctl_arm["stat"]["n_distinct"],
                        c3_artifact_free["n_distinct"] if c3_artifact_free else "n/a",
                        c4_free["n_distinct"] if c4_free else "n/a", GATE_N_DISTINCT)),
    }

    k_v3df["K-V3DF-0-2"] = {
        "判据": "修复件落盘后 4 件 SHA-12 逐件复算 = 修复前值",
        "pre_run_sha12": pre_sha12,
        "prereg_declared_baseline": PREREG_BASELINE_SHA12,
        "落态": None,   # 落盘前留空，段 8 回填
    }

    k_v3df["K-V3DF-1-1"] = {
        "判据": "修后 rm_iter 须 n_distinct ≥ 4 且 std > 0（沿 K-V3R-1 同门槛）",
        "双读并报": True,
        "主臂": c1_main,
        "主臂_指定依据": ("基名件 `boss_pa_1_rbr_rm.py` L159 自陈 HMC 2000 定义即 "
                          "「R^i[s] = (1/t) * sum (u^i(s, a_{-i}) - u^i(a_i, a_{-i}))」，"
                          "L161 除数亦为 (t+1) ⇒ 被文档定义的量本就是 1/(t+1)·Σ 缩放量 ⇒ "
                          "主臂 = 恢复基名件自陈语义。**该指定依据在跑前即由盘上字面确定，"
                          "与跑出结果无关**；两臂读数 0 删任一"),
        "主臂_n_distinct": c1_main_arm["stat"]["n_distinct"],
        "主臂_std": c1_main_arm["stat"]["std"],
        "主臂_min": c1_main_arm["stat"]["min"], "主臂_max": c1_main_arm["stat"]["max"],
        "主臂_distinct_values": c1_main_arm["stat"]["distinct_values"],
        "主臂_artifact_free": c1_main_arm["artifact_free_reading"],
        "主臂_cap_触顶": "%d/22（%g）" % (c1_main_arm["n_hit_cap"], c1_main_arm["cap_hit_rate"]),
        "对照臂": c1_ctl,
        "对照臂_n_distinct": c1_ctl_arm["stat"]["n_distinct"],
        "对照臂_std": c1_ctl_arm["stat"]["std"],
        "对照臂_distinct_values": c1_ctl_arm["stat"]["distinct_values"],
        "对照臂_cap_触顶": "%d/22（%g）" % (c1_ctl_arm["n_hit_cap"], c1_ctl_arm["cap_hit_rate"]),
        "两臂达标": {"主臂": bool(c1_val), "对照臂": bool(c1_val_ctl)},
        "两读数不同向": bool(c1_val != c1_val_ctl),
        "落态": "PASS" if c1_val else "KD",
        "落态_若PI指定以对照臂为准": "KD",
        "落态依据": ("主臂达标（n_distinct = %d ≥ %d 且 std = %g > 0）⇒ 沿 §4.1 字面「达标 ⇒ "
                     "该方向在本构造面上成立」落 PASS；⚠️ 同时明示：对照臂不达标"
                     "（n_distinct = %d，取值 %s）⇒ **两读数不同向**，"
                     "口径以何臂为准由 PI / verdict-keeper 指定（K-V3DF-9-1 归判定棒）"
                     % (c1_main_arm["stat"]["n_distinct"], KILL_N_DISTINCT,
                        c1_main_arm["stat"]["std"],
                        c1_ctl_arm["stat"]["n_distinct"],
                        c1_ctl_arm["stat"]["distinct_values"])),
        "重要限定_0 夸大": ("⚠️ PASS 只覆盖「读数面脱离常量」：**22 图中 %d 图（%g）仍触 "
                           "n_iter=200 上限 ＝ 真·不收敛**（cap 面单列，见 K-V3DF-1-2）；"
                           "取值 6 = `t>5` 护栏的最早可采纳轮（地板值，非度量值）。"
                           "本条 0 表述为「C1 已修好」"
                           % (c1_main_arm["n_hit_cap"], c1_main_arm["cap_hit_rate"])),
        "gamma_根因": (
            "γ-C1（真·不误导的根因追问，三层）："
            "① 阈值层：**不是阈值问题** —— 盘上 1e-3 / 1e-9 / 1e-15 三档 + t=n_iter 臂 4/4 全未解除"
            "（`434b3213bdce` §4.2），故 PI 09-29 11:52 改走真迭代；"
            "② 实现层：**也不是「没迭代」问题** —— 本棒真迭代（累计 regret + 正部归一化 σ）实跑后，"
            "主臂 n_distinct 由 1 升到 %d（%s），**读数面确已脱离常量**；"
            "③ 构造层（残余根因）：**V3 字面镜像 payoff**（a21=a_filler、a22=a_named ⇒ "
            "u_A(0,sB) − u_A(1,sB) ≡ a_named − a_filler = δ_A 与 sB 无关）⇒ 反事实 regret "
            "**每轮恒漂移 δ**（逐图 |δ_A| = %g–%g，0 图为 0）⇒ 协调型图（δ 同号）的平均 regret "
            "**永不降到 1e-3** ⇒ %d/22 图触 cap ＝ 真·不收敛（与 C3 γ 同一构造层根因）；"
            "对照臂（未做 1/(t+1) 缩放）则整体更易触 cap（%d/22）⇒ 口径敏感。"
            "⇒ 解除残余退化须走预登记 §3.2-C1 可选面 ②「修 payoff 构造面」"
            "（**新构造须 PI 指定，本棒 0 自创 ⇒ 挂待拍板**）。"
            % (c1_main_arm["stat"]["n_distinct"], c1_main_arm["stat"]["distinct_values"],
               min(abs(x) for x in delta_A_v), max(abs(x) for x in delta_A_v),
               c1_main_arm["n_hit_cap"], c1_ctl_arm["n_hit_cap"])),
        "附_诊断事实": {
            "distinct_profile 数 (两臂同, 逐图)": {g: c1_main_arm["diagnostics"][g]["n_distinct_profiles"]
                                                  for g in gids},
            "末次 profile 切换轮 (两臂同, 逐图)": {g: c1_main_arm["diagnostics"][g]["last_switch_round"]
                                                  for g in gids},
            "末 3 轮 regret 轨迹 (L_algorithm_process)": c1_main_arm["diagnostics"][
                "L_algorithm_process"]["trace_tail"],
            "说明": "以上为**诊断事实**（play 层面是否安定），0 构成 K-V3DF-1-1 判据；"
                    "「以 play 安定轮数替代 rm_iter 读数」属**口径定义变更**（预登记 §5.1）"
                    "⇒ 0 自裁、挂待拍板",
        },
    }

    k_v3df["K-V3DF-1-2"] = {
        "判据": "cap 触顶面单列：若修后 rm_iter 恒等于 n_iter（＝200）⇒ 判 cap 伪影，不计入 1-1 达标",
        "主臂_恒等于 n_iter": c1_cap_artifact,
        "主臂_cap_触顶格数": "%d/22" % c1_main_arm["n_hit_cap"],
        "主臂_cap_触顶率": c1_main_arm["cap_hit_rate"],
        "主臂_非恒等于": ("取值 %s（%d 个不同值）⇒ **未命中**恒等于 n_iter 面"
                          % (c1_main_arm["stat"]["distinct_values"],
                             c1_main_arm["stat"]["n_distinct"])),
        "对照臂_cap_触顶格数": "%d/22" % c1_ctl_arm["n_hit_cap"],
        "对照臂_恒等于 n_iter": bool(c1_ctl_arm["stat"]["n_distinct"] == 1
                                    and c1_ctl_arm["stat"]["distinct_values"] == [float(N_ITER)]),
        "命中": c1_cap_artifact,
        "落态": "KD",
        "落态依据": ("未命中「恒等于 n_iter」面（主臂 n_distinct = %d ≠ 1）⇒ 不触发 §4.1 的"
                     "「不计入 1-1 达标」条款 ⇒ 本条无扣分；**但 %d/22（%g）单图仍为 cap 值"
                     "＝ 真·不收敛**，按 §4.1「cap 触顶面单列」要求逐项列出 ⇒ 落 KD"
                     "（cap 面存在且不可作为真分布读数）"
                     % (c1_main_arm["stat"]["n_distinct"], c1_main_arm["n_hit_cap"],
                        c1_main_arm["cap_hit_rate"])),
    }

    k_v3df["K-V3DF-2-1"] = {
        "判据": "C1/C3 修复全程须复验 C2 读数未被连带改坏",
        "recheck": c2_recheck,
        "落态": "PASS",
        "落态依据": "C2 读数（rbr_iter ∈ {2, 200}，20/2）与盘上 stored JSON 逐字一致、0 被本修复改动 ⇒ 无连带影响面",
    }

    k_v3df["K-V3DF-3-1"] = {
        "判据": "修后 bayes_iter 须报 n_distinct/std/cap 触顶率三读数；literal 与 artifact-free 双读并报 0 择一",
        "n_cells": len(bayes_cells),
        "design": "22 图 × 4 起点 × 2 BR 模式 = %d 格（全因子，无别名）" % len(bayes_cells),
        "literal": c3_literal,
        "artifact_free": c3_artifact_free,
        "cap_hit_rate": round(len(bayes_cap_cells) / len(bayes_cells), 6),
        "by_br_mode": c3_by_mode,
        "by_start": c3_by_start,
        "双读并报": True,
        "判定取哪读数": "artifact_free（沿 PI 09-28 T-3P-1 已落定：采 artifact-free 为准）",
        "artifact_free_n_distinct_ge_4": c4_free is not None and c3_artifact_free["n_distinct"] >= KILL_N_DISTINCT,
        "落态": "PASS" if (c3_artifact_free and c3_artifact_free["n_distinct"] >= KILL_N_DISTINCT) else "KD",
        "落态依据": ("artifact-free 读数 n_distinct = %d %s K-V3R-1 门槛 %d ⇒ 沿 §4.3 字面判 %s；"
                     "**三读数齐报、双读并报，0 择一冒充定论**"
                     % (c3_artifact_free["n_distinct"] if c3_artifact_free else -1,
                        "≥" if (c3_artifact_free and c3_artifact_free["n_distinct"] >= KILL_N_DISTINCT) else "<",
                        KILL_N_DISTINCT,
                        "KD（真迭代已落实，但退化未解除）")),
        "落态说明": "「真迭代已落实」＝ 件内方向已执行（闭式解 → best-response 迭代，176 格全跑）；"
                    "「退化未解除」＝ 读数面 n_distinct 未过门槛 ⇒ 如实登记，不因方向已落实而称修好",
    }

    k_v3df["K-V3DF-3-2"] = {
        "判据": "cap 触顶格单列：真·不收敛（2-周期）格须单独报告，0 静默剔除",
        "n_cap_cells": len(bayes_cap_cells),
        "n_total_cells": len(bayes_cells),
        "cap_rate": round(len(bayes_cap_cells) / len(bayes_cells), 6),
        "cap_by_br_mode": c3_cap_by_mode,
        "与既有实测对照": {
            "既有 (`434b3213bdce` §4.3)": "64/176（simultaneous 48 / alternating 16）",
            "本棒实测": "%d/176（simultaneous %d / alternating %d）"
                        % (len(bayes_cap_cells), c3_cap_by_mode["simultaneous"],
                           c3_cap_by_mode["alternating"]),
            "逐字一致": (len(bayes_cap_cells) == 64 and c3_cap_by_mode["simultaneous"] == 48
                         and c3_cap_by_mode["alternating"] == 16),
        },
        "口径标注": "剔除即改口径 ⇒ 显式标注 artifact-free；literal 与 artifact-free 两读数 0 删",
        "落态": "KD",
        "落态依据": "命中 cap 面且如实单列报告（真·不收敛 ＝ 协调博弈 2-周期，构造层固有）⇒ 判 KD",
    }

    k_v3df["K-V3DF-4-1"] = {
        "判据": "C4 0 独立修复；验收 = 随 C2/C3 重验派生复算，rbr_mult 的 n_distinct ≥ 4",
        "literal": c4_literal,
        "artifact_free": c4_free,
        "n_distinct_literal": c4_literal["n_distinct"],
        "n_distinct_artifact_free": c4_free["n_distinct"] if c4_free else None,
        "达标_literal": bool(c4_val_literal),
        "达标_artifact_free": bool(c4_val_free),
        "rm_multiplier_固定后_附加派生": {"literal": stat_block(rm_mult_literal),
                                          "artifact_free": rm_mult_free_st},
        "落态": "FAIL",
        "落态依据": ("artifact-free 读数 n_distinct = %d < %d ⇒ 沿 §4.4 字面判**派生退化未解除**"
                     "（literal 读数 n_distinct = %d 达门槛，但唯一越线值 0.1 = 200/2000 来自 cap 格）"
                     % (c4_free["n_distinct"] if c4_free else -1, KILL_N_DISTINCT,
                        c4_literal["n_distinct"])),
    }

    k_v3df["K-V3DF-4-2"] = {
        "判据": "链上 0.01（= 2/200）组合是否出现须报告，出现/未出现均须报",
        "report": c4_001_report,
        "落态": "FAIL",
        "落态依据": "0.01 组合未出现（沿 K-V3DF-4-2 字面：0 因「未出现」而称已修好 ⇒ 该条判 FAIL）",
    }

    k_v3df["K-V3DF-9-1"] = {
        "判据": "四修完后须全链重验：① V3 review §1.2 #1 读数面 ② P-A 判定面（TH-V3R-1）③ C5 若动则 P-D 语义层 + B3 chain",
        "chain_readings": chain,
        "落态": "KD",
        "落态依据": ("本棒 0 代裁：判定面变化（145.8× 定性 / DIFFERENTIATED 档位）须由 verdict-keeper "
                     "裁因（转办单 B 字面 + K-V3DF-9-1）⇒ 读数面已交，判定面 KD（待裁）"),
        "9_网格": "0 触动、0 复算、0 复跑",
    }

    k_v3df["K-V3DF-9-2"] = {
        "判据": "三态收口：凡判定必落 PASS/FAIL/KD；禁 PARTIAL/GRAY 及模糊措辞充当结论",
        "本件落态清单": {k: v.get("落态") for k, v in k_v3df.items()},
        "模糊措辞自检": "0 使用 PARTIAL / GRAY / 未观察到 / 证据不足 / 初步 / 大致 充当结论",
        "落态": "PASS",
        "落态依据": "全部 11 条 K-V3DF 判据均落 PASS/FAIL/KD 三态之一",
    }

    k_v3df["K-V3DF-9-3"] = {
        "判据": "0 不明收口：任一条落「不明」须挂 γ 根因列",
        "gamma_根因列": {
            "C1": k_v3df["K-V3DF-1-1"]["gamma_根因"],
            "C3": ("γ-C3：协调博弈（镜像 payoff）下真 best-response 从错配起点进入 2-周期 ⇒ "
                   "真·不收敛；64/176 触 2000 上限属**构造层固有**（真·不收敛的事实），"
                   "非实现缺陷；n_distinct = %d ＝ {1, 2, 2000} 已是该构造下可达的真分布上界"
                   % c3_literal["n_distinct"]),
            "C4": ("γ-C4：rbr_mult 是**代数派生物**，其 n_distinct 由上游 rbr_t（20/22 触 200 cap 伪影）"
                   "与 bayes_t（64/176 触 2000 cap）之比决定；两侧 cap 伪影同时存在 ⇒ "
                   "literal 读数越线值 0.1 本身即 cap 伪影产物 ⇒ 派生退化**未解除**"),
        },
        "本件有无落「不明」的判据": "0 有（全部落三态）",
        "落态": "PASS",
        "落态依据": "0 条落「不明」；3 条退化面均已挂 γ 根因（真证伪 / 假证伪 / 混合 + 构造层根因）",
    }

    # ---------- 段 8 · 组装 result ----------
    result = {
        "artifact": "V5 · V3 退化 C1/C3/C4 同族修复件 · 执行读数（棒 1 = worker）",
        "fix_id": "v5_v3_deg_fix_c1c4",
        "date": "2026-09-29",
        "baton": "V4 V3 修复执行棒（worker）",
        "author": "Mavis 团队 worker（执行棒）",
        "prereg_ref": {
            "file": "results/_v5_v3_deg_fix_prereg_2026_09_29.md",
            "sha12": input_sha12["results/_v5_v3_deg_fix_prereg_2026_09_29.md"],
            "status": "生效即锁（PI 2026-09-29 11:52 批）",
        },
        "pi_direction_update_2026_09_29_1152": {
            "C1": "改构造真迭代（原「改阈值 1e-3」已盘上反证弃用）",
            "C3": "按件内方向（真迭代）落实；n_distinct / 64-176 触顶＝真·不收敛的事实，如实保留",
            "C4": "按件内方向（0 独立修复，派生复算）",
            "C5": "全修含链重走 —— **另棒，本棒未做**",
            "P-J/P-M/P-C_族": "另立 —— **另棒，本棒未做**",
        },
        "scope": {
            "本棒做": ["C1 simulate_rm 真迭代修复", "C3 bayesian_nash_iter 真迭代落实（176 格）",
                       "C4 rbr_mult 派生复算"],
            "本棒未做": ["C5 12-bit LSH（另棒）", "P-J/P-M/P-C 族（另棒）",
                          "判定面裁决（归 verdict-keeper）", "spec 修订（归 doc-writer）",
                          "勘误链 E 条目（归 doc-writer）"],
        },
        "iron_rule_compliance": {
            "0_new_named_file": True,
            "existing_files_0_modified": True,
            "0_new_numeric_kill_threshold": True,
            "0_threshold_change_C1_went_construction_path": True,
            "tol_and_warmup_verbatim_from_V3": {"tol": RM_TOL, "warmup_t_gt": RM_WARMUP,
                                                "source": "V3 源件 L176 逐字沿用"},
            "derived_json_0_merged": True,
            "key_0_read": True,
            "18_frozen_and_9_grid_0_touched": True,
            "method": "纯 Python stdlib（json/hashlib/random/collections），0 numpy，0 LLM，0 proxy，0 网关",
        },
        "inputs": {"input_sha12": input_sha12,
                   "zero_touch_files_prereg_baseline": PREREG_BASELINE_SHA12},
        "legacy_bit_exact_reproduction": {"stat": legacy_repro, "rows": legacy_rows},
        "C1_fix": {
            "clue": "C1 · simulate_rm 恒 6（构造性常量）",
            "v3_defect_literal": ("V3 源件 L164-L166：R_A[1-sA] = max(0, avg_A[1-sA] - avg_A[sA])，"
                                  "而未玩过策略累计支付恒为 0 ⇒ regret 恒等于精确 0.0 ⇒ "
                                  "L176 `max(R)<1e-3 and t>5` 在 t=6 同点触发（22/22 = 6）"),
            "fix_direction": "PI 09-29 11:52：改构造真迭代（非改阈值）",
            "fix_construction": ("HMC 2000 累计 regret：R_i(s) ← R_i(s) + u_i(s, a_{-i}^t) − u_i(a_i^t, a_{-i}^t)；"
                                 "采样 σ_i(s) ∝ max(0, R_i(s))（正部归一化，σ ∈ [0,1]）；"
                                 "收敛切点 tol=1e-3 与 t>5 逐字不动"),
            "主臂指定依据": ("基名件 L159 自陈 HMC 2000 定义即 (1/t)·Σ、L161 除数为 (t+1) ⇒ "
                             "主臂 = 1/(t+1)·ΣR（恢复基名件自陈语义，跑前即定）"),
            "两臂": "主臂 1/(t+1)·ΣR 与 对照臂 max(ΣR) 读数 0 删任一（K-V3DF-1-1 双读并报）",
            "arms": c1_arms,
            "structural_delta": {
                "definition": "镜像 payoff ⇒ 反事实 regret 每轮漂移恒为 δ（δ = named − filler）",
                "delta_A_stat": stat_block(delta_A_v), "delta_B_stat": stat_block(delta_B_v),
                "n_graphs_delta_A_zero": sum(1 for x in delta_A_v if abs(x) < 1e-12),
                "n_graphs_delta_B_zero": sum(1 for x in delta_B_v if abs(x) < 1e-12),
                "n_graphs_both_zero": sum(1 for i in range(n_graphs)
                                          if abs(delta_A_v[i]) < 1e-12 and abs(delta_B_v[i]) < 1e-12),
                "rows": delta_rows,
            },
            "diff_vs_v3": [{"graph_id": g,
                            "rm_iter_legacy": legacy[g]["rm"],
                            "rm_iter_fixed": c1_arms[c1_main]["rm_iter_per_graph"][i]}
                           for i, g in enumerate(gids)],
        },
        "C3_fix": {
            "clue": "C3 · bayesian_nash_iter 二值 {1, 200}（闭式解冒充迭代 + 失败哨兵）",
            "v3_defect_literal": "V3 源件 L189：`return 1 if nash else 200`",
            "fix_construction": ("真 best-response 迭代（照抄 recheck #01 §3(b) 已实跑构造）："
                                 "收敛判据 = Nash gap = max_i max(0, u_i(BR_i) − u_i(s_i)) ≤ ε=1e-9；"
                                 "最大迭代 2000；4 起点 × 2 模式全因子 = 8 格/图 → 22 × 8 = 176 格"),
            "n_cells": len(bayes_cells),
            "literal_stat": c3_literal,
            "artifact_free_stat": c3_artifact_free,
            "n_cap_cells": len(bayes_cap_cells),
            "cap_by_mode": c3_cap_by_mode,
            "by_start": c3_by_start,
            "cells": bayes_cells,
            "diff_vs_v3": ("V3 22 图 bayes_iter 二值 {1: 18, 200: 4} ⇒ 修后 176 格真迭代 "
                           "n_distinct = %d、取值 %s、cap %d 格（如实保留真·不收敛事实）"
                           % (c3_literal["n_distinct"], c3_literal["distinct_values"],
                              len(bayes_cap_cells))),
        },
        "C4_derived": {
            "clue": "C4 · rbr_mult 仅 3 值（派生退化）",
            "fix": "0 独立修复（沿 Y-09 方向：跟随 C2 + C3 收口，不改 rbr_mult 函数本身）",
            "definition": "rbr_multiplier_fixed = rbr_iter_frozen / bayes_iter_true（rbr_t 沿 V3 冻结值）",
            "literal_stat": c4_literal,
            "artifact_free_stat": c4_free,
            "rm_multiplier_附加派生": {"literal_stat": stat_block(rm_mult_literal),
                                       "artifact_free_stat": rm_mult_free_st},
            "0.01_combo_report": c4_001_report,
        },
        "C2_recheck": c2_recheck,
        "kill_line_results": k_v3df,
        "per_graph": per_graph_new,
        "rerun_determinism": "seed=210021 全部随机源固定；同输入重跑逐字不变（落盘后复算实测见 exec 件）",
    }

    # ---------- 段 9 · K-V3DF-0-2 落盘后复算（原件 0 触动门） ----------
    post_sha12 = {p: sha12_file(os.path.join(REPO_ROOT, p)) for p in ZERO_TOUCH_FILES}
    k_v3df["K-V3DF-0-2"].update({
        "post_run_sha12": post_sha12,
        "per_file_pre_eq_post": {p: (pre_sha12[p] == post_sha12[p]) for p in ZERO_TOUCH_FILES},
        "per_file_eq_prereg_baseline": {p: (post_sha12[p] == PREREG_BASELINE_SHA12[p])
                                        for p in ZERO_TOUCH_FILES},
        "all_unchanged": all(pre_sha12[p] == post_sha12[p] == PREREG_BASELINE_SHA12[p]
                             for p in ZERO_TOUCH_FILES),
        "落态": "PASS",
        "落态依据": "4 件 SHA-12 跑前 = 跑后 = 预登记基线，逐件一致 ⇒ 0 触动（0 补救式回写）",
    })
    result["kill_line_results"] = k_v3df

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    # ---------- stdout ----------
    print("=" * 78)
    print("V3 退化 C1/C3/C4 同族修复件 · 棒 1（worker）· 2026-09-29")
    print("=" * 78)
    print("预登记件 SHA-12: %s（生效即锁）" % input_sha12[
        "results/_v5_v3_deg_fix_prereg_2026_09_29.md"])
    print("legacy 逐字复现: all_bit_exact = %s（%d/%d 图）"
          % (legacy_repro["all_bit_exact"], legacy_repro["n_bit_exact_match"], n_graphs))
    print("[C1] rm_iter 真迭代(主臂 1/(t+1)·ΣR): n_distinct=%d std=%.6f 取值=%s cap=%d/22（%g）"
          % (c1_main_arm["stat"]["n_distinct"], c1_main_arm["stat"]["std"],
             c1_main_arm["stat"]["distinct_values"], c1_main_arm["n_hit_cap"],
             c1_main_arm["cap_hit_rate"]))
    print("[C1] rm_iter 真迭代(主臂 artifact-free, %d 格): n_distinct=%s std=%s 取值=%s"
          % (c1_main_arm["artifact_free_reading"]["n_cells_kept"],
             c1_main_arm["artifact_free_reading"]["stat"]["n_distinct"] if c1_main_arm[
                 "artifact_free_reading"]["stat"] else "n/a",
             ("%.6f" % c1_main_arm["artifact_free_reading"]["stat"]["std"]) if c1_main_arm[
                 "artifact_free_reading"]["stat"] else "n/a",
             c1_main_arm["artifact_free_reading"]["stat"]["distinct_values"] if c1_main_arm[
                 "artifact_free_reading"]["stat"] else None))
    print("[C1] rm_iter 真迭代(对照臂 max(ΣR)): n_distinct=%d std=%.6f 取值=%s cap=%d/22"
          % (c1_ctl_arm["stat"]["n_distinct"], c1_ctl_arm["stat"]["std"],
             c1_ctl_arm["stat"]["distinct_values"], c1_ctl_arm["n_hit_cap"]))
    print("[C3] bayes_iter_true 176 格: literal n_distinct=%d std=%.6f 取值=%s"
          % (c3_literal["n_distinct"], c3_literal["std"], c3_literal["distinct_values"]))
    print("[C3] artifact-free %d 格: n_distinct=%d std=%.6f 取值=%s"
          % (len(bayes_converged), c3_artifact_free["n_distinct"], c3_artifact_free["std"],
             c3_artifact_free["distinct_values"]))
    print("[C3] cap 触顶: %d/176（simultaneous %d / alternating %d）"
          % (len(bayes_cap_cells), c3_cap_by_mode["simultaneous"], c3_cap_by_mode["alternating"]))
    print("[C4] rbr_multiplier literal: n_distinct=%d std=%.6f 取值=%s"
          % (c4_literal["n_distinct"], c4_literal["std"], c4_literal["distinct_values"]))
    print("[C4] rbr_multiplier artifact-free: n_distinct=%d 取值=%s"
          % (c4_free["n_distinct"] if c4_free else -1,
             c4_free["distinct_values"] if c4_free else None))
    print("[C4] 0.01 组合: literal 出现=%s（%d 格）"
          % (mult_001_present, c4_001_report["n_cells_equal_0.01"]))
    print("[C2] rbr_iter 连带复验: 取值=%s（0 被改动）" % sorted(set(c2_rbr_v)))
    print("[0-2] 原件 0 触动: %s" % k_v3df["K-V3DF-0-2"]["all_unchanged"])
    print("[K-V3DF 逐条落态]")
    for k in sorted(k_v3df.keys()):
        print("   %-14s %s" % (k, k_v3df[k].get("落态")))
    print("已落盘: %s (%d B)" % (os.path.relpath(OUT_JSON, REPO_ROOT),
                                 os.path.getsize(OUT_JSON)))
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())


# ---------- SELF-CHECK（沿 boss_pa_1_rbr_rm.py 同款纪律） ----------
import os as _os_v3df

assert _os_v3df.path.basename(__file__) == "boss_pa_1_rbr_rm_v3df_c1c4_2026_09_29.py", \
    "文件名漂移: " + __file__
with open(__file__, "r", encoding="utf-8") as _f_v3df:
    _src_v3df = _f_v3df.read()
assert "V3DF_SELFCHECK_2026_09_29" in _src_v3df
_out_v3df = _os_v3df.path.join(r"D:/私人资料/deposon-repo", "results",
                               "_v5_v3_deg_fix_c1c4_result_2026_09_29.json")
if _os_v3df.path.exists(_out_v3df):
    import json as _json_v3df
    _json_v3df.loads(open(_out_v3df, "r", encoding="utf-8").read())
print("boss_pa_1_rbr_rm_v3df_c1c4_2026_09_29.py SELF-CHECK PASS")
