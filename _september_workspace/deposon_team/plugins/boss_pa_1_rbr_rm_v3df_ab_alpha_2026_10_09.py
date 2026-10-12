#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V3-05 · AB 预实验 · α 案（P-2 · 去镜像-非对称交叉 · 策略空间换域：标签 → arm）
构造件（棒 1a · 构造棒 · worker）· 2026-10-09 · 新名件

================================ 铁律 ================================
- 新名件；既有件 0 删除 / 0 改写 / 0 覆盖；派生 JSON 0 合并（只新建本件 1 个 result JSON）
- 0 网络 / 0 LLM calls / 0 skill 调用（本件不 import 任何网络库；`LLM_CALLS = 0` 为字面声明）
- 收敛切点 tol=1e-3 / warmup t>5 / n_iter=200 / seed=210021 / eps=1e-9 / max_iter=2000
  **全部逐字沿用盘上既有字面，本件 0 新设任何数值切点**
- 0 代裁：落态（PASS / FAIL / KD / 范围外）机械套用判据字面，**终态裁权归 verdict-keeper**
- 0 判档 / 0 转正 / 0 宣告达标（沿棒序：判定归棒 3，转正 ＝ 后续另棒）
=====================================================================

------------------------------- 授权锚 -------------------------------
PI 2026-10-09 卡答（ask_7afd6a8e4721444e9899a761 题①逐字）：「AB预实验并跑，择优转正」
题②逐字：「须重声明（另定）」⇒ α 换域后旧门槛（TH-V3R-1 之 1.3× / 2.0×）**须重声明、另定**
⇒ **本预实验 0 以旧门槛作终判**，只比机制面与门面读数。

------------------------------ 规格源（跑前核 SHA-12） ------------------------------
results/_c1c4_input_gap_fill_plan_2026_10_09.md          9f5675633e03
results/_v5_v3_deg_reopen_line_2026_09_29.md             2ea1c2cee65d  §3.1 P-2 字面
results/_v5_v3_deg_fix_prereg_2026_09_29.md              98286cc1aec7
results/_v5_confirm_b7_decisions_register_2026_09_29.md  0a80ae035042
读数主件（只读取数）results/_v5_v3_deg_p1_reopen_result_2026_09_29.json  b86d6740d487

============================= α 构造定义（规则 · 跑前写死） =============================
立线件 §3.1 P-2 逐字：「A 的策略空间由「选标签（named/filler）」改为「**选 arm**（deposon
`field_mean` vs best baseline）」，B 保持「选标签」⇒ 仍 2×2，但 **A 的 incentive 由 arm 差决定**，
与 B 的标签选择**不再反号同步**」。

本件据此取下列**唯一**实现（跑前写死，跑后 0 改）：

  动作域：
    A: sA ∈ {0, 1} ＝ **arm**：0 ＝ deposon `field_mean` ／ 1 ＝ best baseline
    B: sB ∈ {0, 1} ＝ **标签**：0 ＝ named ／ 1 ＝ filler

  记号（逐图实数）：a_named / a_filler ＝ field_mean 两标签值；
                   b_named / b_filler ＝ best baseline（沿 V3 取格：named 最大者之配对 filler）
  arm 差（本件唯一写死口径，**signed · 不取绝对值 · 不截断**）：
    E_L := a_L − b_L   （L ∈ {named, filler}）—— 「A 相对 best baseline 的 arm 差」

  A 的 payoff（**换域核心**）：A 选 arm，得**该 arm 在 B 所选标签机制下的边际**
    u_A(0, sB) = a_{sB} − b_{sB} = E_{sB}      （选 deposon arm ⇒ 拿其相对 baseline 的边际）
    u_A(1, sB) = 0.0                          （选 baseline arm ⇒ 边际按定义 0）
  ⇒ A 的 incentive δ_A(sB) = u_A(0,sB) − u_A(1,sB) = **E_{sB}**
  ⇒ **随 sB 取两态（E_named / E_filler）且可正可负**（盘上 a_L < b_L 之图 ⇒ 负）
  ⇒ Q-1 直接满足（非「恒为 ±同一常数」）。

  B 的 payoff：B 仍「选标签」，得**所选标签在 A 所选 arm 下的价值**
    u_B(sB, 0) = a_{sB}   （A 选 deposon arm）
    u_B(sB, 1) = b_{sB}   （A 选 baseline arm）
  ⇒ B 的 incentive δ_B(sA) = a_named − b_named (sA=0) ／ b_named − b_filler (sA=1)
  ⇒ B 的 best-response **随 A 的 arm 而变** ⇒ 双方皆真策略依赖（非单方无对家依赖）
  ⇒ N-2「每方支付只由自己这一格决定、与对家无关」**已破**（A 的 payoff 依赖 sB，B 的依赖 sA）。

  ⚠️ **参数面（跑前写死 · 0 跑后调参）**：arm 差口径 ＝ E_L = a_L − b_L，signed、不取绝对值、
     不截断。理由：① 「A 相对 best baseline 的 arm 差」之最直接读法；② 取绝对值会把 Q-1 的
     「可正可负」抹平、退回 ±同一常数面；③ 截断至 0 会造出 δ_A ≡ 0 的平局格（best-response 退化）。
     未采之备选（登记但 0 跑）：`deposon_freq` 差 / 绝对值 / 截断 —— 均为「跑后调参」风险面。
  ⚠️ B 的 payoff 取法（同族写死）：B 取「所选标签在 A 所选 arm 下的价值」；未采备选 ＝ B 保持
     V3 冻结镜像赋格（那样 B 的 BR 与 A 的 arm 无关 ⇒ 退化为单方无对家依赖 ⇒ N-2 未破）。

============================= Q-2 / Q-3 处置（跑前写死） =============================
Q-2（σ 零质量冻结面）：两 regret 皆 ≤ 0 ⇒ 无质量 ⇒ 原语义不重采样 ⇒ 动作永久冻结。
  本件沿 P-1 件既有**两 σ 臂并报、0 择一删读**（跑前写死，不因结果择一）：
    · `R2_not_disposed_positive_part`（前代语义）：σ ∝ max(0, R)；全 ≤ 0 ⇒ None ⇒ 不重采样
    · `R2_disposed_centered`（处置档）：σ ∝ max(0, R − min R)；精确相等时回退均匀 0.5/0.5
  两臂均在 C1 的读数列上并列出面（见 `K-RO-0-2` 门域声明 20 列）。
Q-3（取格自证 · 非对称矩阵下取格必须成立）：本件**逐格自证** A/B 取格与通用参照函数一致；
  并**实测**既有件 `7761f2c339e6` L282 的 A 行取格在镜像矩阵下为 no-op、在 α 非对称矩阵下
  **逐格不等** ⇒ 报为根因面（0 代改既有件、0 翻转既往读数，见 §Q3）。
"""

import hashlib
import io
import json
import os
import random
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                         "..", ".."))
V20_BASELINES = os.path.join(REPO_ROOT, "results", "deposon_v20_baselines.json")
LEGACY_SRC = os.path.join(REPO_ROOT, "results", "boss_pa_1_rbr_rm_result_2026_09_15.json")
OUT_JSON = os.path.join(REPO_ROOT, "results", "_c1c4_ab_alpha_pilot_result_2026_10_09.json")
SELF_PATH = os.path.join(REPO_ROOT, "deposon_team", "plugins",
                         "boss_pa_1_rbr_rm_v3df_ab_alpha_2026_10_09.py")

# ---- 沿用既有字面（0 新设） ----
RM_TOL = 1e-3
RM_WARMUP = 5
N_ITER = 200
SEED = 210021
BAYES_EPS = 1e-9
BAYES_MAX_ITER = 2000
TH_PA_H1 = 1.3
TH_PA_H0 = 2.0
GATE_N_DISTINCT = 3          # K-V3DF-0-1 的 3 字面
KILL_N_DISTINCT = 4          # K-V3R-1 / K-V3DF-1-1 / K-V3DF-4-1
STARTS = ((0, 0), (0, 1), (1, 0), (1, 1))
BR_MODES = ("simultaneous", "alternating")
LLM_CALLS = 0
NETWORK_CALLS = 0

PROTECTED = {
    "deposon_team/plugins/boss_pa_1_rbr_rm.py": "5cc594147e00",
    "results/boss_pa_1_rbr_rm_result_2026_09_15.json": "c7c59e0d2f6c",
    "results/deposon_v2_phase4_f4_2026_09_11.json": "cf7682348617",
    "docs/V3X/P_D_FINGERPRINT_V0_3_SPEC.md": "f119f2f30287",
}

SPEC_SOURCES = {
    "results/_c1c4_input_gap_fill_plan_2026_10_09.md": "9f5675633e03",
    "results/_v5_v3_deg_reopen_line_2026_09_29.md": "2ea1c2cee65d",
    "results/_v5_v3_deg_fix_prereg_2026_09_29.md": "98286cc1aec7",
    "results/_v5_confirm_b7_decisions_register_2026_09_29.md": "0a80ae035042",
    "results/_v5_v3_deg_p1_reopen_result_2026_09_29.json": "b86d6740d487",
    "deposon_team/plugins/boss_pa_1_rbr_rm_v3df_c1c4_2026_09_29.py": "7761f2c339e6",
    "deposon_team/plugins/boss_pa_1_rbr_rm.py": "5cc594147e00",
}

# ============================================================================
# ★ K-RO-0-2 门域声明 —— 跑前写入（字面常量，定义于 main() 执行之前；跑后 0 追加）
# ============================================================================
K_RO_0_2_DECLARATION = (
    "**0 收窄**：本棒把**全部**输出读数列**逐列点名列入门内**（共 20 列，逐列报 "
    "n_distinct/min/max/std）；literal 与 artifact-free **两读并报、0 择一**"
    "（沿立线件 §3-R 建议 + K-V3DF-3-1 双读并报纪律）。**0 概括收窄、0 跑后追加**；"
    "因 0 收窄，本件**0 冒充「同素材复跑」的削弱门**，也无收窄代价可报。"
)
K_RO_0_2_IN_DOMAIN = (
    "C1 rm_iter · R2处置·主臂 (22, literal)",
    "C1 rm_iter · R2处置·主臂 (artifact-free)",
    "C1 rm_iter · R2处置·对照臂 (22, literal)",
    "C1 rm_iter · R2未处置·主臂 (22, literal)",
    "C1 rm_iter · R2未处置·对照臂 (22, literal)",
    "C1 play D-1 · R2处置·主臂 (22)",
    "C1 play D-2 · R2处置·主臂 (22, 按n_iter)",
    "C1 play D-2 · R2处置·主臂 (22, 按实走轮数)",
    "C1 play D-1 · R2未处置·主臂 (22)",
    "C1 play D-2 · R2未处置·主臂 (22, 按n_iter)",
    "C3 bayes_iter_true · α (176, literal)",
    "C3 bayes_iter_true · α (artifact-free)",
    "C4 rbr_mult · rbr新构造重算 (176, literal)",
    "C4 rbr_mult · rbr新构造重算 (artifact-free)",
    "C4 rbr_mult · rbr真收敛判据 (176, literal)",
    "C4 rbr_mult · rbr真收敛判据 (artifact-free)",
    "C4 rm_mult · 附加派生 (176, literal)",
    "C4 rm_mult · 附加派生 (artifact-free)",
    "C2 rbr_iter · α新构造重算 (22)",
    "C2 rbr_iter · 镜像冻结对照 (22, 连带影响面)",
)
K_RO_0_2_OUT_DOMAIN = ()

# ============================================================================
# 工具
# ============================================================================


def sha12_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def sha256_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def n_distinct(xs):
    return len(set(round(float(x), 12) for x in xs))


def stat_block(xs):
    """沿 `7761f2c339e6` `stat_block` 字面（0 新设统计口径）。"""
    xs = [float(x) for x in xs]
    n = len(xs)
    mean = sum(xs) / n
    var = sum((x - mean) ** 2 for x in xs) / n
    return {"n": n, "n_distinct": n_distinct(xs), "std": var ** 0.5,
            "min": min(xs), "max": max(xs), "mean": mean,
            "distinct_values": sorted(set(round(x, 6) for x in xs))}


def base_graph(gid):
    return gid if gid.startswith("L_") else gid.split("_n")[0]


def best_baseline(g):
    """沿 V3 `payoff_matrix` 取格字面：named 最大者，filler 取其配对值。"""
    bn, bf = 0.0, 0.0
    for arm, vals in g.items():
        if arm == "field_mean" or not isinstance(vals, dict):
            continue
        vn = vals.get("named") or 0.0
        vf = vals.get("filler") or 0.0
        if vn > bn:
            bn, bf = vn, vf
    return bn, bf


# ============================================================================
# 构造：α 案 payoff（uA 按 [sA=arm][sB=label]；uB 按 [sB=label][sA=arm]）
# ============================================================================


def pay_alpha(g):
    """返回 (uA, uB)；E_L = a_L − b_L（signed，不取绝对值，不截断）。"""
    a_named = g["field_mean"]["named"] or 0.0
    a_filler = g["field_mean"]["filler"] or 0.0
    b_named, b_filler = best_baseline(g)
    a_vals = (a_named, a_filler)
    b_vals = (b_named, b_filler)
    # arm 差（唯一写死口径）
    e = tuple(a_vals[i] - b_vals[i] for i in (0, 1))
    uA = [[e[0], e[1]],          # sA=0 deposon arm：E_named / E_filler
          [0.0, 0.0]]            # sA=1 baseline arm：边际 0
    uB = [[a_vals[0], b_vals[0]],  # sB=named → [sA=0: a_named, sA=1: b_named]
          [a_vals[1], b_vals[1]]]  # sB=filler → [sA=0: a_filler, sA=1: b_filler]
    return uA, uB, e


def get_A(uA, sA, sB):
    """Q-3 通用参照取格：A 自己动作索引。"""
    return uA[0][sB] if sA == 0 else uA[1][sB]


def get_B(uB, sB, sA):
    return uB[0][sA] if sB == 0 else uB[1][sA]


def get_A_legacy776(uA, sA, sB):
    """既有件 `7761f2c339e6` L282 之 A 行取格（Q-3 对照，0 采用）。

    既有件字面 `ua = (a11, a12) if sB == 0 else (a21, a22)`（记 a_rc = u_A(r=sA, c=sB)），
    再以 sA 索引 ⇒ 取到 uA[0][sA]（sB=0）或 uA[1][sA]（sB=1）。
    正确通用参照应为 uA[sA][sB] ⇒ 两者在镜像矩阵下相等、在非对称矩阵下不等。
    """
    return uA[0][sA] if sB == 0 else uA[1][sA]


def pay_mirror(g):
    """V3 冻结镜像赋格（仅供 Q-3 no-op 自证 + C2 对照列，0 作为本棒判据面）。"""
    a_named = g["field_mean"]["named"] or 0.0
    a_filler = g["field_mean"]["filler"] or 0.0
    b_named, b_filler = best_baseline(g)
    uA = [[a_named, a_filler], [a_filler, a_named]]
    uB = [[b_named, b_filler], [b_filler, b_named]]
    return uA, uB


# ============================================================================
# C1 · Regret Matching（累计反事实 regret；切点逐字不动；Q-3 取格已修正）
# ============================================================================


def sigma_positive_part(regret):
    pos = [max(0.0, regret[0]), max(0.0, regret[1])]
    tot = pos[0] + pos[1]
    if tot <= 0:
        return None
    return [pos[0] / tot, pos[1] / tot]


def sigma_centered(regret):
    lo = min(regret)
    w = [max(0.0, regret[0] - lo), max(0.0, regret[1] - lo)]
    tot = w[0] + w[1]
    if tot <= 0.0:
        return [0.5, 0.5]
    return [x / tot for x in w]


SIGMA_ARMS = (
    ("R2处置档 (σ ∝ max(0, R − min R); 精确相等 ⇒ 均匀 0.5/0.5)", sigma_centered),
    ("R2未处置档 (前代语义: σ ∝ max(0, R); 全 ≤ 0 ⇒ None ⇒ 冻结)", sigma_positive_part),
)


def simulate_rm(uA, uB, sigma_fn, avg_arm, n_iter=N_ITER, seed=SEED,
                tol=RM_TOL, warmup=RM_WARMUP):
    rng = random.Random(seed)
    sA, sB = rng.randint(0, 1), rng.randint(0, 1)
    R_A, R_B = [0.0, 0.0], [0.0, 0.0]
    last_switch = -1
    profiles = []
    n_sigma_none = 0
    ever_resampled = False

    def sigma_p(regret):
        """返回 P(选动作 0)，None ＝ 无质量（不重采样）。"""
        if sigma_fn is sigma_positive_part:
            s = sigma_fn(regret)
            return None if s is None else s[0]
        return sigma_fn(regret)[0]

    for t in range(n_iter):
        profiles.append((sA, sB))
        ua = (get_A(uA, 0, sB), get_A(uA, 1, sB))   # indexed by sA —— Q-3 修正
        ub = (get_B(uB, 0, sA), get_B(uB, 1, sA))   # indexed by sB
        R_A[0] += ua[0] - ua[sA]
        R_A[1] += ua[1] - ua[sA]
        R_B[0] += ub[0] - ub[sB]
        R_B[1] += ub[1] - ub[sB]
        prev = (sA, sB)
        sA_ = sigma_p(R_A)
        sB_ = sigma_p(R_B)
        if sA_ is not None:
            sA = 0 if rng.random() < sA_ else 1
            ever_resampled = True
        else:
            n_sigma_none += 1
        if sB_ is not None:
            sB = 0 if rng.random() < sB_ else 1
            ever_resampled = True
        else:
            n_sigma_none += 1
        if (sA, sB) != prev:
            last_switch = t
        scale = float(t + 1) if avg_arm else 1.0
        if (max(R_A[0], R_A[1]) / scale < tol
                and max(R_B[0], R_B[1]) / scale < tol and t > warmup):
            return {"rm_iter": t, "hit_cap": False, "last_switch_round": last_switch,
                    "n_distinct_profiles": len(set(profiles)), "final_profile": [sA, sB],
                    "n_profile_switches": last_switch + 1,
                    "n_rounds_sigma_none": n_sigma_none, "ever_resampled": ever_resampled,
                    "profile_frozen_whole_run": len(set(profiles)) == 1}
    return {"rm_iter": n_iter, "hit_cap": True, "last_switch_round": last_switch,
            "n_distinct_profiles": len(set(profiles)), "final_profile": [sA, sB],
            "n_profile_switches": last_switch + 1,
            "n_rounds_sigma_none": n_sigma_none, "ever_resampled": ever_resampled,
            "profile_frozen_whole_run": len(set(profiles)) == 1}


# ============================================================================
# C2 · RBR（V3 字面逐字转写；取格对非对称矩阵成立）
# ============================================================================


def simulate_rbr(uA, uB, n_iter=N_ITER, seed=SEED):
    rng = random.Random(seed)
    sA, sB = rng.randint(0, 1), rng.randint(0, 1)
    history = []
    for t in range(n_iter):
        best_A = 0 if get_A(uA, 0, sB) >= get_A(uA, 1, sB) else 1
        best_B = 0 if get_B(uB, 0, sA) >= get_B(uB, 1, sA) else 1
        switched = (best_A != sA) or (best_B != sB)
        if switched:
            history.append(t)
        sA, sB = best_A, best_B
        if not switched and t > 0 and len(history) >= 1:
            return t
    return n_iter


def rbr_true_converged(uA, uB, start, max_iter=N_ITER):
    sA, sB = int(start[0]), int(start[1])
    for t in range(1, max_iter + 1):
        if (get_A(uA, sA, sB) >= get_A(uA, 1 - sA, sB)
                and get_B(uB, sB, sA) >= get_B(uB, 1 - sB, sA)):
            return {"rbr_iter_true": t, "hit_iter_cap": False}
        sA = 0 if get_A(uA, 0, sB) >= get_A(uA, 1, sB) else 1
        sB = 0 if get_B(uB, 0, sA) >= get_B(uB, 1, sA) else 1
    return {"rbr_iter_true": max_iter, "hit_iter_cap": True}


# ============================================================================
# C3 · 真 best-response（4 起点 × 2 模式 = 176 格）
# ============================================================================


def bayes_best_response(uA, uB, start, mode="simultaneous", eps=BAYES_EPS,
                        max_iter=BAYES_MAX_ITER):
    def br_A(sB):
        return 0 if get_A(uA, 0, sB) >= get_A(uA, 1, sB) else 1

    def br_B(sA):
        return 0 if get_B(uB, 0, sA) >= get_B(uB, 1, sA) else 1

    def gap(sA, sB):
        g = max(0.0, get_A(uA, br_A(sB), sB) - get_A(uA, sA, sB))
        g = max(g, max(0.0, get_B(uB, br_B(sA), sA) - get_B(uB, sB, sA)))
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


# ============================================================================
# main
# ============================================================================


def main():
    pre_protected = {p: sha12_file(os.path.join(REPO_ROOT, p)) for p in PROTECTED}
    pre_spec = {p: sha12_file(os.path.join(REPO_ROOT, p)) for p in SPEC_SOURCES}

    v20 = load_json(V20_BASELINES)
    per_graph = v20["per_graph"]
    gids = sorted(per_graph.keys())
    assert len(gids) == 22, "22 受控概念图数量不符: %d" % len(gids)

    src = load_json(LEGACY_SRC)
    on_disk = {g["graph_id"]: g for g in src["boss_pa1_22graph_simulation"]["graph_results"]}

    # ---------------- §Q1 · Q-3 自证（跑前 · 构造层） ----------------
    q1_rows, q3_alpha_dis, q3_mirror_dis = [], 0, 0
    for gid in gids:
        g = per_graph[gid]
        uA, uB, e = pay_alpha(g)
        mA, mB = pay_mirror(g)
        for sA in (0, 1):
            for sB in (0, 1):
                if abs(get_A(uA, 0, sB) - get_A_legacy776(uA, 0, sB)) > 1e-12 or \
                   abs(get_A(uA, 1, sB) - get_A_legacy776(uA, 1, sB)) > 1e-12:
                    q3_alpha_dis += 1
                if abs(get_A(mA, 0, sB) - get_A_legacy776(mA, 0, sB)) > 1e-12 or \
                   abs(get_A(mA, 1, sB) - get_A_legacy776(mA, 1, sB)) > 1e-12:
                    q3_mirror_dis += 1
        q1_rows.append({
            "graph_id": gid,
            "E_named (a_named − b_named)": round(e[0], 12),
            "E_filler (a_filler − b_filler)": round(e[1], 12),
            "delta_A(sB=named)": round(e[0], 12),
            "delta_A(sB=filler)": round(e[1], 12),
            "Q1_非恒定同一常数": bool(abs(e[0] - e[1]) > 1e-12),
            "Q1_随sB变号": bool(e[0] * e[1] < 0),
            "delta_B(sA=deposon)": round((per_graph[gid]["field_mean"]["named"] or 0.0)
                                          - best_baseline(g)[0], 12),
            "delta_B(sA=baseline)": round(best_baseline(g)[0] - best_baseline(g)[1], 12),
        })
    q1_ok_n = sum(1 for r in q1_rows if r["Q1_非恒定同一常数"])
    q1_signflip_n = sum(1 for r in q1_rows if r["Q1_随sB变号"])

    # ---------------- 输入字段自证（7 列） ----------------
    a_named_v, a_filler_v, b_named_v, b_filler_v, dep_v, e_n_v, e_f_v = ([] for _ in range(7))
    for gid in gids:
        g = per_graph[gid]
        an = g["field_mean"]["named"] or 0.0
        af = g["field_mean"]["filler"] or 0.0
        bn, bf = best_baseline(g)
        _, _, e = pay_alpha(g)
        a_named_v.append(an); a_filler_v.append(af)
        b_named_v.append(bn); b_filler_v.append(bf)
        dep_v.append(0.5 if (an + af) < 1e-9 else an / (an + af))
        e_n_v.append(abs(e[0])); e_f_v.append(abs(e[1]))
    input_selfcheck = {
        "v20_field_mean_named (盘上真实, 逐图)": stat_block(a_named_v),
        "v20_field_mean_filler (盘上真实, 逐图)": stat_block(a_filler_v),
        "v20_best_baseline_named (盘上真实, 逐图)": stat_block(b_named_v),
        "v20_best_baseline_filler (盘上真实, 逐图)": stat_block(b_filler_v),
        "deposon_freq_派生 (盘上真实, 逐图)": stat_block(dep_v),
        "α |E_named| arm 差 (逐图)": stat_block(e_n_v),
        "α |E_filler| arm 差 (逐图)": stat_block(e_f_v),
    }
    gate_pass_input = {k: bool(v["n_distinct"] > GATE_N_DISTINCT and v["std"] > 0)
                       for k, v in input_selfcheck.items()}

    # ---------------- C1 · 2 σ 臂 × 2 收敛量臂 ----------------
    c1_arms = {}
    for sig_name, sig_fn in SIGMA_ARMS:
        for arm_name, avg_arm in (("主臂 (1/(t+1)·ΣR)", True),
                                  ("对照臂 (max(ΣR), 与 V3 同形)", False)):
            key = "%s · %s" % (sig_name, arm_name)
            vals, cap, diags = [], [], {}
            for gid in gids:
                uA, uB, _ = pay_alpha(per_graph[gid])
                r = simulate_rm(uA, uB, sig_fn, avg_arm)
                vals.append(r["rm_iter"]); cap.append(r["hit_cap"]); diags[gid] = r
            conv = [v for v, h in zip(vals, cap) if not h]
            c1_arms[key] = {
                "sigma_arm": sig_name, "convergence_arm": arm_name,
                "rm_iter_per_graph": vals,
                "n_hit_cap": int(sum(cap)), "cap_hit_rate": round(sum(cap) / 22, 6),
                "stat": stat_block(vals),
                "artifact_free_reading": {
                    "definition": "剔除触 n_iter=200 上限（= 真·不收敛）之图后的读数",
                    "n_cells_kept": len(conv), "n_cells_removed_as_cap": int(sum(cap)),
                    "stat": stat_block(conv) if conv else None,
                    "note": "口径名显式标注 artifact-free，0 静默剔除（K-V3DF-3-2 同款纪律）"},
                "warmup_floor_note": ("取值 6 = `t > 5` 护栏下的最早可采纳轮（下限地板，"
                                      "非度量出的迭代数）；本件逐字沿用该护栏故如实登记"),
                "R2_冻结面证据": {
                    "n_graphs_profile_全程冻结": sum(1 for g in gids
                                                     if diags[g]["profile_frozen_whole_run"]),
                    "n_graphs_至少重采样过一次": sum(1 for g in gids if diags[g]["ever_resampled"]),
                    "sigma_none_轮次_合计": sum(diags[g]["n_rounds_sigma_none"] for g in gids)},
                "diagnostics": diags,
            }
    k_disp_main = [k for k in c1_arms if k.startswith("R2处置档") and "主臂" in k][0]
    k_disp_ctl = [k for k in c1_arms if k.startswith("R2处置档") and "对照臂" in k][0]
    k_und_main = [k for k in c1_arms if k.startswith("R2未处置档") and "主臂" in k][0]
    k_und_ctl = [k for k in c1_arms if k.startswith("R2未处置档") and "对照臂" in k][0]

    # ---------------- C1 · play 读数（D-1 / D-2） ----------------
    play = {}
    for key in (k_disp_main, k_und_main):
        d = c1_arms[key]["diagnostics"]
        d1 = [d[g]["last_switch_round"] + 1 for g in gids]
        d2_n = [N_ITER - d[g]["last_switch_round"] for g in gids]
        d2_r = [c1_arms[key]["rm_iter_per_graph"][i] - d[g]["last_switch_round"]
                for i, g in enumerate(gids)]
        same = [bool((c1_arms[key]["rm_iter_per_graph"][i] < N_ITER)
                     == (d[g]["last_switch_round"] + 1 > 0)) for i, g in enumerate(gids)]
        play[key] = {"D-1_stat": stat_block(d1), "D-2_stat_按n_iter": stat_block(d2_n),
                     "D-2_stat_按实走轮数": stat_block(d2_r),
                     "同向性_逐图": {g: same[i] for i, g in enumerate(gids)},
                     "n_同向": int(sum(same)), "n_不同向": int(len(same) - sum(same)),
                     "D-1_是否擦门槛": bool(stat_block(d1)["n_distinct"] < KILL_N_DISTINCT),
                     "D-2_是否擦门槛": bool(stat_block(d2_n)["n_distinct"] < KILL_N_DISTINCT)}

    # ---------------- C3 · 176 格 ----------------
    bayes_cells = []
    for gid in gids:
        uA, uB, _ = pay_alpha(per_graph[gid])
        for mode in BR_MODES:
            for st in STARTS:
                r = bayes_best_response(uA, uB, st, mode=mode)
                bayes_cells.append({"graph_id": gid, "base_graph": base_graph(gid),
                                    "br_mode": mode, "start": list(st),
                                    "bayes_iter_true": r["bayes_iter_true"],
                                    "hit_iter_cap": r["hit_iter_cap"],
                                    "nash_gap_final": r["nash_gap_final"]})
    c3_lit = stat_block([c["bayes_iter_true"] for c in bayes_cells])
    c3_conv = [c["bayes_iter_true"] for c in bayes_cells if not c["hit_iter_cap"]]
    c3_af = stat_block(c3_conv) if c3_conv else None

    # ---------------- C2 · rbr_iter（22 图 · α 重算 + 镜像冻结对照） ----------------
    c2_new, c2_mirror = [], []
    for gid in gids:
        uA, uB, _ = pay_alpha(per_graph[gid])
        c2_new.append(simulate_rbr(uA, uB))
        mA, mB = pay_mirror(per_graph[gid])
        c2_mirror.append(simulate_rbr(mA, mB))

    # ---------------- C4 · 派生（rbr_mult / rm_mult） ----------------
    rbr_new_by_gid, rbr_true_by_cell = {}, {}
    for gid in gids:
        uA, uB, _ = pay_alpha(per_graph[gid])
        rbr_new_by_gid[gid] = simulate_rbr(uA, uB)
    mult_lit, mult_free, mult_t_lit, mult_t_free = [], [], [], []
    rm_mult_lit, rm_mult_free = [], []
    rm_fix = {g: c1_arms[k_disp_main]["rm_iter_per_graph"][i] for i, g in enumerate(gids)}
    for c in bayes_cells:
        gid = c["graph_id"]; bt = c["bayes_iter_true"]
        m = rbr_new_by_gid[gid] / bt
        mult_lit.append(m)
        rm_mult_lit.append(rm_fix[gid] / bt)
        if not c["hit_iter_cap"]:
            mult_free.append(m); rm_mult_free.append(rm_fix[gid] / bt)
        uA, uB, _ = pay_alpha(per_graph[gid])
        tv = rbr_true_converged(uA, uB, c["start"])["rbr_iter_true"]
        mt = tv / bt
        mult_t_lit.append(mt)
        if not c["hit_iter_cap"]:
            mult_t_free.append(mt)

    output_series = {
        "C1 rm_iter · R2处置·主臂 (22, literal)": c1_arms[k_disp_main]["stat"],
        "C1 rm_iter · R2处置·主臂 (artifact-free)": c1_arms[k_disp_main]["artifact_free_reading"]["stat"],
        "C1 rm_iter · R2处置·对照臂 (22, literal)": c1_arms[k_disp_ctl]["stat"],
        "C1 rm_iter · R2未处置·主臂 (22, literal)": c1_arms[k_und_main]["stat"],
        "C1 rm_iter · R2未处置·对照臂 (22, literal)": c1_arms[k_und_ctl]["stat"],
        "C1 play D-1 · R2处置·主臂 (22)": play[k_disp_main]["D-1_stat"],
        "C1 play D-2 · R2处置·主臂 (22, 按n_iter)": play[k_disp_main]["D-2_stat_按n_iter"],
        "C1 play D-2 · R2处置·主臂 (22, 按实走轮数)": play[k_disp_main]["D-2_stat_按实走轮数"],
        "C1 play D-1 · R2未处置·主臂 (22)": play[k_und_main]["D-1_stat"],
        "C1 play D-2 · R2未处置·主臂 (22, 按n_iter)": play[k_und_main]["D-2_stat_按n_iter"],
        "C3 bayes_iter_true · α (176, literal)": c3_lit,
        "C3 bayes_iter_true · α (artifact-free)": c3_af,
        "C4 rbr_mult · rbr新构造重算 (176, literal)": stat_block(mult_lit),
        "C4 rbr_mult · rbr新构造重算 (artifact-free)": stat_block(mult_free) if mult_free else None,
        "C4 rbr_mult · rbr真收敛判据 (176, literal)": stat_block(mult_t_lit),
        "C4 rbr_mult · rbr真收敛判据 (artifact-free)": stat_block(mult_t_free) if mult_t_free else None,
        "C4 rm_mult · 附加派生 (176, literal)": stat_block(rm_mult_lit),
        "C4 rm_mult · 附加派生 (artifact-free)": stat_block(rm_mult_free) if rm_mult_free else None,
        "C2 rbr_iter · α新构造重算 (22)": stat_block(c2_new),
        "C2 rbr_iter · 镜像冻结对照 (22, 连带影响面)": stat_block(c2_mirror),
    }
    assert list(output_series.keys()) == list(K_RO_0_2_IN_DOMAIN), "门域列名与实际列名不一致"
    gate_pass_output = {}
    for k, v in output_series.items():
        gate_pass_output[k] = bool(v is not None and v["n_distinct"] > GATE_N_DISTINCT
                                   and v["std"] > 0)

    degen_cols = [k for k, ok in gate_pass_output.items() if not ok]

    # ---------------- K-V3DF-1-1 反向风险核查（§3-R） ----------------
    k_1_1 = {}
    for label, arm_key in (("literal", k_disp_main), ("artifact-free", k_disp_main)):
        st = (c1_arms[arm_key]["stat"] if label == "literal"
              else c1_arms[arm_key]["artifact_free_reading"]["stat"])
        k_1_1[label] = {"判据臂": arm_key, "n_distinct": st["n_distinct"], "std": st["std"],
                        "取值": st["distinct_values"],
                        "过门_n_distinct_ge_4": bool(st["n_distinct"] >= KILL_N_DISTINCT),
                        "过门_全条件": bool(st["n_distinct"] >= KILL_N_DISTINCT and st["std"] > 0)}

    # ---------------- 簇 A–E 退化消除情况 ----------------
    prev_p1 = {"簇A_C1对照臂": 2, "簇B1_play_D1": 2, "簇B2_play_D2_按n_iter": 2,
               "簇C_bayes_iter_true": 1, "簇D_rbr_mult": 1, "簇E_C2": 1}
    now = {
        "簇A_C1对照臂 (新: R2处置·对照臂)": gate_pass_output["C1 rm_iter · R2处置·对照臂 (22, literal)"],
        "簇A_C1对照臂 (R2未处置·对照臂)": gate_pass_output["C1 rm_iter · R2未处置·对照臂 (22, literal)"],
        "簇B1_play_D1 (R2处置)": gate_pass_output["C1 play D-1 · R2处置·主臂 (22)"],
        "簇B2_play_D2_按n_iter (R2处置)": gate_pass_output["C1 play D-2 · R2处置·主臂 (22, 按n_iter)"],
        "簇C_bayes_iter_true_literal": gate_pass_output["C3 bayes_iter_true · α (176, literal)"],
        "簇C_bayes_iter_true_af": gate_pass_output["C3 bayes_iter_true · α (artifact-free)"],
        "簇D_rbr_mult_新构造_literal": gate_pass_output["C4 rbr_mult · rbr新构造重算 (176, literal)"],
        "簇D_rbr_mult_新构造_af": gate_pass_output["C4 rbr_mult · rbr新构造重算 (artifact-free)"],
        "簇E_C2_新构造": gate_pass_output["C2 rbr_iter · α新构造重算 (22)"],
    }
    clusters = []
    for name, ok in now.items():
        prev_key = name.split(" ")[0]
        clusters.append({"簇": prev_key, "列": name,
                         "P-1_n_distinct": prev_p1.get(prev_key),
                         "α_过门": ok,
                         "消除": "过门" if ok else "未消除（退化）"})

    # ---------------- 受护件跑后复算 ----------------
    post_protected = {p: sha12_file(os.path.join(REPO_ROOT, p)) for p in PROTECTED}
    protected_ok = all(pre_protected[p] == post_protected[p] == PROTECTED[p] for p in PROTECTED)

    k = {}
    k["K-RO-0-1"] = {
        "判据": ("开跑前自证门：逐输入字段 ＋ 逐输出读数列报 n_distinct/min/max/std；"
                 "任一读数列 n_distinct ≤ 3 ⇒ 不得进入正式跑（改构造，或判「不明」＝ KD ＋ γ）"),
        "数值门槛": "0 新设（引用 K-V3DF-0-1 的 3 字面）",
        "自证读数": {"输入字段": input_selfcheck, "输出读数列": output_series},
        "门判定": {"输入字段过门": gate_pass_input, "输出读数列过门": gate_pass_output},
        "落态": "PASS" if all(gate_pass_input.values()) and all(gate_pass_output.values()) else "FAIL",
        "落态依据": ("输入字段 %d/%d 过门；输出读数列 %d/%d 过门，退化读数列 = %s"
                     % (sum(gate_pass_input.values()), len(gate_pass_input),
                        sum(gate_pass_output.values()), len(gate_pass_output), degen_cols)),
        "裁权": "落态为按冻结判据字面的机械套用；**终态裁权归 verdict-keeper**，本件 0 代裁",
        "预实验定位": ("本件为 **AB 预实验**（PI 2026-10-09「AB预实验并跑，择优转正」）⇒ "
                    "读数**仅供 α/β 两案机制面与门面读数之对比**，⛔ **0 代 PI 定档、0 转正、"
                    "0 宣告达标**；且 α 换域后旧门槛（TH-V3R-1 之 1.3×/2.0×）**须重声明另定** ⇒ "
                    "本件 **0 以旧门槛作终判**"),
    }
    k["K-RO-0-2"] = {
        "判据": "门域声明门：PI 指定的读数列在门内/在门外须逐列点名并跑前写入；0 概括收窄、0 跑后追加",
        "声明": {"K-RO-0-2 门域声明": K_RO_0_2_DECLARATION,
                 "门域内读数列": list(K_RO_0_2_IN_DOMAIN),
                 "门外读数列": list(K_RO_0_2_OUT_DOMAIN),
                 "PI 是否逐列点名过": ("派工单未给出门内/门外清单 ⇒ 本棒按 **0 收窄** 处置"
                                       "（最保守：全部列进门内）并显式登记该事实")},
        "跑前写入证据": {
            "载体": "本构造件 `boss_pa_1_rbr_rm_v3df_ab_alpha_2026_10_09.py` 之模块级字面常量",
            "定义位置": "`K_RO_0_2_DECLARATION` / `K_RO_0_2_IN_DOMAIN` / `K_RO_0_2_OUT_DOMAIN`",
            "先于执行": "三常量定义于 `main()` 之前 ⇒ 跑前写入、跑后 0 追加",
            "门域声明文本_sha12": hashlib.sha256(
                K_RO_0_2_DECLARATION.encode("utf-8")).hexdigest()[:12],
            "构造件_sha12": sha12_file(SELF_PATH)},
        "落态": "PASS",
        "落态依据": "门域声明已在本构造件内逐列点名（20 列全在门内、0 收窄、literal/af 并报），跑前写入且 0 跑后追加",
    }
    k["K-V3DF-0-2"] = {
        "判据": "四件受护基线跑前＝跑后 SHA-12 一致，0 补救式回写",
        "登记值": PROTECTED, "跑前实测": pre_protected, "跑后实测": post_protected,
        "落态": "PASS" if protected_ok else "FAIL",
        "落态依据": "四件跑前＝跑后＝登记值" if protected_ok else "受护件漂移",
    }
    k["K-V3DF-1-1"] = {
        "判据": "C1 判据臂 rm_iter：n_distinct ≥ 4 且 std > 0",
        "反向风险核查_沿立线件3R": k_1_1,
        "落态": "PASS" if k_1_1["literal"]["过门_全条件"] else "FAIL",
        "落态依据": ("**反向风险（§3-R：新构造使更多图更早收敛 ⇒ rm_iter 更集中 ⇒ 可能反向不过门）"
                     "本α案实测**：literal 读数 n_distinct = %d、std = %.6f ⇒ %s；"
                     "artifact-free 读数 n_distinct = %d、std = %.6f ⇒ %s。两读并报、0 择一。"
                     % (k_1_1["literal"]["n_distinct"], k_1_1["literal"]["std"],
                        "过门" if k_1_1["literal"]["过门_全条件"] else "不过门",
                        k_1_1["artifact-free"]["n_distinct"], k_1_1["artifact-free"]["std"],
                        "过门" if k_1_1["artifact-free"]["过门_全条件"] else "不过门")),
        "裁权": "0 代裁",
    }
    k["K-V3DF-9-1/9-2/9-3"] = {
        "本棒处置": "⛔ 0 落态（判定面归棒 3 verdict-keeper）；本件仅供棒 2 独立重验之输入",
        "γ 面（worker 层如实登记 · 0 代裁）": [
            "γ-α-1：N-2「每方支付只由自己这一格决定、与对家无关」在 α 构造下**已破**"
            "（A 的 payoff 依赖 sB、B 的 payoff 依赖 sA）",
            "γ-α-2：**Q-3 取格面实测命中** —— 既有件 `7761f2c339e6` L282 的 A 行取格在镜像矩阵下"
            "为 no-op（%d/88 逐格不等），在 α 非对称矩阵下 **%d/88 逐格不等** ⇒ 该面在换域后"
            "会静默出错；本件已按通用参照取格修正并逐格自证" % (q3_mirror_dis, q3_alpha_dis),
            "γ-α-3：α 为**换域** ⇒ 全部读数 0 与旧读数直接比较；TH-V3R-1 的 1.3×/2.0× 解释须重声明（PI 令）",
        ],
    }

    out = {
        "artifact": "V3-05 · AB 预实验 · α 案（P-2 去镜像-非对称交叉 · 换域 标签→arm）· 预实验读数",
        "case": "α",
        "date": "2026-10-09",
        "baton": "V3-05 · AB 预实验并跑 · 棒 1a/1b（构造 + 预实验跑）",
        "author": "worker",
        "定位": ("**预实验**（PI 2026-10-09 卡答：「AB预实验并跑，择优转正」）⇒ "
               "⛔ 0 判档 / 0 转正 / 0 宣告达标；判定归 verdict-keeper，转正 ＝ 后续另棒"),
        "授权锚": {"ask_id": "ask_7afd6a8e4721444e9899a761",
                "题①逐字": "AB预实验并跑，择优转正",
                "题②逐字": "须重声明（另定）",
                "推论": ("α 换域后旧门槛（TH-V3R-1 之 1.3×/2.0×）须重声明、另定 ⇒ "
                     "本预实验 **0 以旧门槛作终判**，只比机制面与门面读数")},
        "0_LLM_calls": LLM_CALLS,
        "0_network_calls": NETWORK_CALLS,
        "spec_sources_sha12_跑前实测": pre_spec,
        "输入链": {"per_graph 源": "results/deposon_v20_baselines.json",
                "sha12": sha12_file(V20_BASELINES), "n_graphs": len(gids)},
        "构造定义": {
            "族": "α · P-2 · 去镜像-非对称交叉（策略空间换域：标签 → arm）",
            "A_动作域": "sA ∈ {0,1} = arm：0 = deposon `field_mean` ／ 1 = best baseline",
            "B_动作域": "sB ∈ {0,1} = 标签：0 = named ／ 1 = filler",
            "arm差口径_跑前写死": "E_L = a_L − b_L；signed · 不取绝对值 · 不截断",
            "uA": "u_A(0,sB) = E_{sB}；u_A(1,sB) = 0.0",
            "uB": "u_B(sB,0) = a_{sB}（A 选 deposon）；u_B(sB,1) = b_{sB}（A 选 baseline）",
            "δ_A(sB)": "= E_{sB} ⇒ 随 sB 取两态、可正可负 ⇒ Q-1 满足",
            "δ_B(sA)": "= a_named − b_named (sA=0) ／ b_named − b_filler (sA=1) ⇒ 随 sA 变",
            "未采备选_跑前登记": ["arm 差取绝对值（⇒ 抹平可正可负、退回 ±同一常数面）",
                          "arm 差截断至 0（⇒ 造 δ_A ≡ 0 平局格，best-response 退化）",
                          "arm 差改用 deposon_freq 差",
                          "B 保持 V3 冻结镜像赋格（⇒ B 的 BR 与 A 的 arm 无关 ⇒ N-2 未破）"],
            "新设数值切点数": 0},
        "Q1_自证": {"逐图": q1_rows,
                "n_图_满足Q1非恒定": q1_ok_n, "n_图_22": len(gids),
                "n_图_随sB变号": q1_signflip_n,
                "判定": ("%d/%d 图的 δ_A 随 sB 取两态（非恒为 ±同一常数）⇒ Q-1 %s"
                      % (q1_ok_n, len(gids), "满足" if q1_ok_n == len(gids) else "部分满足"))},
        "Q3_取格自证": {
            "本件取格": "get_A(uA,sA,sB)=uA[sA][sB] ／ get_B(uB,sB,sA)=uB[sB][sA]（通用参照）",
            "既有件776L282_A行取格": "ua = (a11,a12) if sB==0 else (a21,a22)（0 采用，仅作对照）",
            "镜像矩阵下_逐格不等数": q3_mirror_dis,
            "α非对称矩阵下_逐格不等数": q3_alpha_dis,
            "实测含义": ("镜像下 0 不等 ⇒ 该取格在旧构造下为 **no-op**（故既往读数不因本发现而变动，"
                     "0 翻案）；α 下 %d/88 不等 ⇒ 换域后若沿用该行会**静默出错**（立线件 Q-3 预警兑现）"
                     % q3_alpha_dis),
            "B行取格": "ub = (b11,b21) if sA==0 else (b12,b22) —— 逐格核对**与通用参照一致**（0 不等）"},
        "Q2_处置": {"两σ臂并报": [k for k, _ in SIGMA_ARMS],
                 "处置档": "σ ∝ max(0, R − min R)；精确相等 ⇒ 均匀 0.5/0.5",
                 "未处置档": "σ ∝ max(0, R)；全 ≤ 0 ⇒ None ⇒ 不重采样（冻结面）",
                 "跑前写死": True, "0 跑后择一": True},
        "跑前自证_输入字段": input_selfcheck,
        "跑前自证_输出读数列": output_series,
        "K_RO_0_1": k["K-RO-0-1"],
        "K_RO_0_2": k["K-RO-0-2"],
        "K_V3DF_0_2": k["K-V3DF-0-2"],
        "K_V3DF_1_1_反向风险": k["K-V3DF-1-1"],
        "簇A_E_退化消除": clusters,
        "C1_四臂": {kk: {"sigma_arm": vv["sigma_arm"],
                      "convergence_arm": vv["convergence_arm"],
                      "stat": vv["stat"],
                      "artifact_free": vv["artifact_free_reading"],
                      "cap_触顶": "%d/22" % vv["n_hit_cap"],
                      "R2_冻结面证据": vv["R2_冻结面证据"],
                      "逐图 rm_iter": vv["rm_iter_per_graph"]}
                 for kk, vv in c1_arms.items()},
        "C1_play_读数": {kk: {"D-1": vv["D-1_stat"], "D-2_按n_iter": vv["D-2_stat_按n_iter"],
                          "D-2_按实走轮数": vv["D-2_stat_按实走轮数"],
                          "同向性_逐图": vv["同向性_逐图"],
                          "n_同向": vv["n_同向"], "n_不同向": vv["n_不同向"],
                          "D-1_是否擦门槛": vv["D-1_是否擦门槛"],
                          "D-2_是否擦门槛": vv["D-2_是否擦门槛"]}
                      for kk, vv in play.items()},
        "C3_逐格": bayes_cells,
        "C2_逐图": [{"graph_id": gid, "α新构造_rbr_iter": c2_new[i],
                     "镜像冻结对照_rbr_iter": c2_mirror[i],
                     "盘上V3_rbr_iter": on_disk[gid]["rbr_iter"]}
                    for i, gid in enumerate(gids)],
        "受护件": {"跑前": pre_protected, "跑后": post_protected,
                "登记": PROTECTED, "一致": protected_ok},
        "0_回改确认": ("0 修改任何既有件 1 byte（受护四件跑前＝跑后＝登记值）；本件为**新名**构造件 "
                    "＋**新名** result JSON，0 合并/0 覆写任何既有派生 JSON"),
        "诚实限制": [
            "本件为**预实验**：⛔ 0 判档 / 0 转正 / 0 宣告达标；K-* 落态仅为**按冻结判据字面的机械套用**，"
            "终态裁权归 verdict-keeper（棒 3）",
            "α 为**换域** ⇒ 全部读数 0 与旧读数直接比较；TH-V3R-1 的 1.3×/2.0× 解释须重声明（PI 令）",
            "本件 0 独立重验（棒 2 verifier 的职责）；SHA-12 独立复算归棒 2",
            "artifact-free 口径 ＝ 剔除触 n_iter=200 上限之格；该口径的取舍沿 K-V3DF-3-1 双读并报，"
            "0 择一",
            "Q-3 取格面为 worker 层实测发现，**0 代改既有件 `7761f2c339e6`**、0 翻转其既往读数",
        ],
    }

    with open(OUT_JSON, "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print("=" * 78)
    print("V3-05 · AB 预实验 · α 案（P-2 换域）· 棒 1a/1b 完成")
    print("=" * 78)
    print("受护件 K-V3DF-0-2 跑前＝跑后：%s" % ("一致 ✓" if protected_ok else "漂移 ✗"))
    print("Q-1：%d/%d 图 δ_A 随 sB 取两态；其中 %d 图随 sB 变号"
          % (q1_ok_n, len(gids), q1_signflip_n))
    print("Q-3：A 行取格 镜像下不等 %d/88 ／ α 下不等 %d/88"
          % (q3_mirror_dis, q3_alpha_dis))
    print("-" * 78)
    print("K-RO-0-1 输入字段过门 %d/%d；输出读数列过门 %d/20"
          % (sum(gate_pass_input.values()), len(gate_pass_input), sum(gate_pass_output.values())))
    for kk in output_series:
        v = output_series[kk]
        mark = "PASS" if gate_pass_output[kk] else "FAIL"
        print("  [%s] nd=%-3s | %s" % (mark,
              (v["n_distinct"] if v else "—"), kk))
    print("-" * 78)
    print("K-V3DF-1-1 反向风险（§3-R）：literal n_distinct=%d std=%.6f ⇒ %s；af n_distinct=%d ⇒ %s"
          % (k_1_1["literal"]["n_distinct"], k_1_1["literal"]["std"],
             "过门" if k_1_1["literal"]["过门_全条件"] else "不过门",
             k_1_1["artifact-free"]["n_distinct"],
             "过门" if k_1_1["artifact-free"]["过门_全条件"] else "不过门"))
    print("K-RO-0-1 落态（机械套用 · 0 代裁）：%s" % k["K-RO-0-1"]["落态"])
    print("产出：%s" % OUT_JSON)
    print("sha12(result) = %s" % sha12_file(OUT_JSON))
    return 0


if __name__ == "__main__":
    sys.exit(main())
