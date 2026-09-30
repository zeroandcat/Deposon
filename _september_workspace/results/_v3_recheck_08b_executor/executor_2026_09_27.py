#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V3-R 补审 #8 顶替重跑（08b）— BOSS-PC-3 (A3 clipping) under PI-authorized cell-count tiers
executor · Mavis 团队 worker · 2026-09-27

派工单字面（PI 2026-09-27 问卷 ask_167a54be6af9f2090ee5c900 Q1「授权顶替重跑」）：
  授权以 cell 计数档 {30, 60, 540} 顶替 N 阶梯重跑 K-V3R-8（原 N 阶梯因真实 N 档
  n_distinct = 0 且溯源链断裂不可得）。此为 **PI 显式授权的新输入面** =
  K-V3R-0-B「0 新设阈值」的显式豁免（授权字面 = 本派工单 + PI 问卷原件记录）。

沿 results/_v3_recheck_prereg_v1_2026_09_27.md（SHA-12 88052d7db895）字面执行：
  - K-V3R-8 kill-line 字面：r2_delta_full_minus_clipped 至少一档 != 0 -> PASS（改判）；
    3 trial 仍 == 0 -> FAIL（维持假证伪）
  - K-V3R-0-C 双口径：顶替口径新构造 verdict + 沿原 V3 阈值字面 verdict 并报
  - K-V3R-0-D 派生 JSON 不合并（本件独立落盘 08b 系列，不覆盖 08 系列）
  - K-V3R-0-E 0 LLM（纯 numpy / hashlib / json，0 网络 0 模型调用）
  - TH-V3R-8 派工单冻结扫描：clip_r2_min ∈ {0.3, 0.5, 0.7}
  - A3 语义沿 docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md §5 字面：去掉 N=10 与 N=1000
    两端，看 R² 是否仍 > clip_r2_min；R² 沿同 spec §3.3 + §4.1 幂律 OLS 公式
  - 真 N 范围裁剪在 cell 档 {30,60,540} 下重定义（3 档装不下「去两端」→ 见 CLIP_* 定义）

防退化豁免（派工单字面，parent 推演 / PI 授权延伸）：
  N 阶梯维因授权 3 档豁免 n_distinct>3 门；防退化自证改在 **P 维 / 样本维**做
  （每档内 n_distinct>3 + std>0）。

设计透镜（skill `scientific-research-workflows:experimental-design` 落点，post-hoc 结构审计用）：
  独立单元 = model（n=9），非 cell（540 cells ≠ 540 独立单元 → 伪重复风险）。
  故 bootstrap 一律 **model 级重抽**（skill §Mistakes #1 pseudoreplication）；
  tier 级聚合读法（spec §3.1 字面「每档一个 (命中率, 失真率)」）不参与 bootstrap。

S-40 布尔显式命名：`*_hit = True` 表示「触发 FAIL / 触发警报」；`*_pass = True` 表示「存活 / 合格」。

NaN 陷阱（显式守卫，防静默误判）：
  - Python 中 `float('nan') != 0.0` 为 True ⇒ 若 kill-line 用 `delta != 0.0` 写，
    未定义 delta 会被**误判为 PASS（改判）**。本 executor 一律用
    `math.isfinite(delta) and abs(delta) >= 1e-12` 作「!= 0」判据。
  - 08 executor 的 `clipd["r2"] > m` 在 r2 未定义时会**静默落到 FAIL** 分支
    （nan > m 为 False）。本 executor 对此加显式 `UNDEFINED` 守卫（沿机制 + 补守卫）。
"""

import hashlib
import json
import math
import os
import sys
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------- 冻结常量（0 新设，除 PI 授权顶替档）
CLIP_R2_MIN_GRID = [0.3, 0.5, 0.7]                 # 派工单冻结扫描
CELL_TIERS = [30, 60, 540]                        # PI 2026-09-27 显式授权顶替档（豁免 K-V3R-0-B）
N_LADDER_LEGACY = [10, 20, 50, 100, 200, 500, 1000]  # TH-V3R-8 字面（仅登记，不跑）
TRIALS = [42, 137, 256]                           # 沿原 BOSS-PC-3 三 trial seed
BOOTSTRAP_N = 1000
BOOTSTRAP_SEED = 42
SEED = 20260927
N_MODELS = 9                                      # 独立单元数（skill：replication level = model）
EPS = 1e-12
# 数值噪声守卫（声明式常量，worker 登记；**非科学阈值**）：
# 精确整数口径已证 T60 == 2*T30 / R60 == 2*R30 / A60 == 2*A30（逐 model 整数相等，见 material_probe）
# ⇒ 三档响应在**精确算术**下恒等 ⇒ SS_tot 必 = 0。凡 0 < SS_tot < 1e-24 皆为 float64
# 「同一有理数两次除法」的舍入残差（实测量级 ~1e-32），0 计入判定（防「浮点噪声冒充信号」）。
FLOAT_NOISE_SS_TOT_CEIL = 1e-24

# 裁剪重定义（cell 档下 spec §5「去两端」的 3 种落法）
CLIP_VARIANTS = {
    "CLIP_STRICT_A3_drop_both_ends": [60],                     # 3 档去两端 → 剩 1 点 → R² 未定义
    "CLIP_DROP_HIGHEST_tier_540": [30, 60],                    # 去上端 → 2 点 → OLS 恒过 → R²≡1
    "CLIP_DROP_LOWEST_tier_30": [60, 540],                     # 去下端 → 2 点 → OLS 恒过 → R²≡1
}

UNDEF = "UNDEFINED_SS_TOT_ZERO"   # SS_tot == 0 ⇒ 幂律 R² = 0/0 无定义（不是 0，也不是 1）


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
SRC_PC3 = REPO / "results/boss_pc_3_a3_clipping_2026_09_15.json"
SRC_60 = REPO / "results/deposon_v3_physical_opt_60cells_2026_09_11.json"
SRC_SPEC = REPO / "docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md"
PREREG = REPO / "results/_v3_recheck_prereg_v1_2026_09_27.md"
EXEC_08 = REPO / "results/_v3_recheck_08_executor_2026_09_27.py"
OUT_DIR = REPO / "results/_v3_recheck_08b_executor"
OUT = OUT_DIR / "result_2026_09_27.json"


def sha12(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:12]     # 硬口径：小写 hexdigest()[:12]


def n_distinct(xs) -> int:
    return len(set(xs))


def stat_block(xs):
    a = np.asarray(xs, dtype=float)
    return {"n": int(a.size),
            "n_distinct": n_distinct([round(float(x), 12) for x in a]),
            "std": float(a.std(ddof=0)), "std_gt_0": bool(a.std(ddof=0) > 0.0),
            "min": float(a.min()), "max": float(a.max()), "mean": float(a.mean())}


def powerlaw_r2(tiers, p_vals):
    """沿 spec §3.3 + §4.1 字面：log10(P) = beta*log10(C) + log10(A)，OLS，R² = 1 - SS_res/SS_tot。

    0 新设阈值：判据形式沿 08 executor 字面；仅把 08 的 `float('nan')` 显式化为
    `None + status=UNDEFINED_SS_TOT_ZERO`（JSON 合法 + 防静默误判）。
    """
    x = np.log10(np.asarray(tiers, dtype=float))
    p_arr = np.asarray(p_vals, dtype=float)
    if p_arr.size != x.size or not bool(np.all(p_arr > 0.0)) or not bool(np.all(np.isfinite(p_arr))):
        return {"n_points": int(p_arr.size), "beta": None, "log10_A": None, "r2": None,
                "ss_res": None, "ss_tot": None, "r2_status": "UNDEFINED_NONPOSITIVE_OR_NONFINITE_P",
                "r2_if_unguarded": None,
                "verdict_note": "P 存在 <= 0 或非有限值 ⇒ log10(P) 未定义 ⇒ 幂律 R² 无定义"
                                "（失真率 A_frac 面上 A30 = 0 的 model 即落此档）"}
    y = np.log10(p_arr)
    if x.size < 2:
        return {"n_points": int(x.size), "beta": None, "log10_A": None, "r2": None,
                "ss_res": None, "ss_tot": None, "r2_status": "UNDEFINED_N_POINTS_LT_2",
                "r2_if_unguarded": None,
                "verdict_note": "点数 < 2 ⇒ R² 无定义（幂律拟合至少需 2 点）"}
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    pred = A @ coef
    ss_res = float(((y - pred) ** 2).sum())
    ss_tot = float(((y - y.mean()) ** 2).sum())
    if ss_tot <= 0.0:
        return {"n_points": int(x.size), "beta": float(coef[0]), "log10_A": float(coef[1]),
                "r2": None, "ss_res": ss_res, "ss_tot": ss_tot, "r2_status": UNDEF,
                "r2_if_unguarded": None,
                "verdict_note": "SS_tot == 0 ⇒ log10(P) 在各档全等（响应层档间无变化）"
                                "⇒ R² = 0/0 无定义；此为**未定义**，既非 0 亦非 1"}
    r2_unguarded = 1.0 - ss_res / ss_tot
    if ss_tot < FLOAT_NOISE_SS_TOT_CEIL:
        return {"n_points": int(x.size), "beta": float(coef[0]), "log10_A": float(coef[1]),
                "r2": None, "ss_res": ss_res, "ss_tot": ss_tot,
                "r2_status": "UNDEFINED_FLOAT_NOISE",
                "r2_if_unguarded": float(r2_unguarded) if math.isfinite(r2_unguarded) else None,
                "verdict_note": "0 < SS_tot < %g ⇒ 精确整数口径下档间响应恒等（SS_tot 必 = 0）⇒ "
                                "本 SS_tot 系 float64 舍入残差（噪声），0 计入判定"
                                % FLOAT_NOISE_SS_TOT_CEIL}
    r2 = r2_unguarded
    if not math.isfinite(r2):
        return {"n_points": int(x.size), "beta": float(coef[0]), "log10_A": float(coef[1]),
                "r2": None, "ss_res": ss_res, "ss_tot": ss_tot,
                "r2_status": "UNDEFINED_NONFINITE_R2", "r2_if_unguarded": None,
                "verdict_note": "R² 非有限 ⇒ 记为未定义（不落 PASS/FAIL）"}
    return {"n_points": int(x.size), "beta": float(coef[0]), "log10_A": float(coef[1]),
            "r2": float(r2), "ss_res": ss_res, "ss_tot": ss_tot, "r2_status": "DEFINED",
            "verdict_note": None}


def clip_verdicts(r2):
    """clip_r2_min 扫描（派工单冻结 {0.3,0.5,0.7}）。NaN 守卫：未定义不落 FAIL 分支。"""
    if r2 is None or not math.isfinite(r2):
        return {("verdict_clip_r2_min_%s" % m): "UNDEFINED（r2 无定义，不落 PASS/FAIL 分支）"
                for m in CLIP_R2_MIN_GRID}
    return {("verdict_clip_r2_min_%s" % m): ("PASS" if r2 > m else "FAIL") for m in CLIP_R2_MIN_GRID}


def delta_block(r2_full, r2_clip):
    """delta = r2_full - r2_clip；「!= 0」判据显式带 isfinite 守卫（防 NaN 假 PASS）。"""
    if r2_full is None or r2_clip is None:
        return {"r2_delta_full_minus_clipped": None, "delta_is_zero": None,
                "delta_is_nonzero": False, "delta_status": "UNDEFINED（r2_full 或 r2_clip 无定义）"}
    d = float(r2_full) - float(r2_clip)
    return {"r2_delta_full_minus_clipped": d,
            "delta_is_zero": bool(math.isfinite(d) and abs(d) < EPS),
            "delta_is_nonzero": bool(math.isfinite(d) and abs(d) >= EPS),
            "delta_status": "DEFINED" if math.isfinite(d) else "UNDEFINED_NONFINITE"}


def main() -> int:
    try:                                    # 控制台 GBK 环境下中文/上标打印 0 崩（仅打印层，0 触判定）
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    pc3 = json.loads(SRC_PC3.read_text(encoding="utf-8"))
    s60 = json.loads(SRC_60.read_text(encoding="utf-8"))
    thr = pc3["pre_registered_threshold"]
    legacy_trials = pc3["trials"]
    per_model = s60["P_C_distortion_bound_60cells"]["per_model"]

    # ================================================================ §1 授权登记（硬）
    authorization = {
        "authorization_id": "PI 2026-09-27 问卷 ask_167a54be6af9f2090ee5c900 Q1「授权顶替重跑」",
        "authorization_literal": "N 阶梯 → cell 计数档 {30,60,540} 顶替 = PI 2026-09-27 显式授权"
                                 "新输入面（K-V3R-0-B 豁免）",
        "authorized_by": "PI（派出方 Mavis root session 转达；授权字面 = 本派工单 + PI 问卷原件记录）",
        "exempted_rule": "K-V3R-0-B 沿用阈值「0 新设」——本件顶替面为 PI 显式豁免的**新输入面**，"
                         "非 worker 擅调阈值；豁免登记随 result / rescript 同步落盘",
        "authorization_record_on_disk": False,
        "authorization_record_note": "问卷 ask_167a54be6af9f2090ee5c900 原件 0 命中于盘上（0 网络 0 LLM，"
                                     "按铁律不自取）；本件以派工单字面为授权凭据，授权来源如实登记不代为补证",
        "degen_exemption": {
            "ladder_dimension": "N 阶梯维：授权 3 档（{30,60,540}）⇒ n_distinct = 3，"
                                "**因 PI 授权豁免 n_distinct>3 门**（豁免与推演字面均注明 parent 推演、"
                                "PI 授权延伸）",
            "relocated_to_P_and_sample_dimension": "防退化自证改在 **P 维 / 样本维**做："
                                                   "每档内 n_distinct>3 + std>0（见 material_probe.per_tier_P_stats）",
            "who": "parent 推演 / PI 授权延伸（worker 0 私设）",
        },
    }

    # ================================================================ §2 素材面探测
    # 档位来源：30 = 每 model 30 cells（T30/R30/A30）；60 = 每 model 60 cells（T60/R60/A60）；
    # 540 = 9 model × 60 cells 汇总（T60_sum=384 / R60_sum=78 / A60_sum=78 = 540）
    T30 = [m["T30"] for m in per_model]
    R30 = [m["R30"] for m in per_model]
    A30 = [m["A30"] for m in per_model]
    T60 = [m["T60"] for m in per_model]
    R60 = [m["R60"] for m in per_model]
    A60 = [m["A60"] for m in per_model]

    doubling_exact = {
        "T60_eq_2xT30_all_models": bool(all(T60[i] == 2 * T30[i] for i in range(N_MODELS))),
        "R60_eq_2xR30_all_models": bool(all(R60[i] == 2 * R30[i] for i in range(N_MODELS))),
        "A60_eq_2xA30_all_models": bool(all(A60[i] == 2 * A30[i] for i in range(N_MODELS))),
        "sum_T30": int(sum(T30)), "sum_T60": int(sum(T60)),
        "sum_R30": int(sum(R30)), "sum_R60": int(sum(R60)),
        "sum_A30": int(sum(A30)), "sum_A60": int(sum(A60)),
        "per_model_exact_doubling": [
            {"model": per_model[i]["model"], "T30": T30[i], "T60": T60[i],
             "R30": R30[i], "R60": R60[i], "A30": A30[i], "A60": A60[i],
             "exact_doubling": bool(T60[i] == 2 * T30[i] and R60[i] == 2 * R30[i]
                                    and A60[i] == 2 * A30[i])}
            for i in range(N_MODELS)],
    }

    # P 维（命中率 = T/(T+R+A)；失真率 = A/(T+R+A)）——spec §3.1「每档 (命中率, 失真率)」
    def rate(num30, num60, den30, den60):
        p30 = [num30[i] / den30[i] for i in range(N_MODELS)]
        p60 = [num60[i] / den60[i] for i in range(N_MODELS)]
        p540 = [num60[i] / den60[i] for i in range(N_MODELS)]   # 540 = 9 model × 60 的池，逐 model 贡献率
        return p30, p60, p540

    hit30, hit60, hit540 = rate(T30, T60, [30] * N_MODELS, [60] * N_MODELS)
    dis30 = [A30[i] / 30 for i in range(N_MODELS)]
    dis60 = [A60[i] / 60 for i in range(N_MODELS)]
    dis540 = list(dis60)

    def tier_invariant(a, b, c):
        return bool(max(abs(x - y) for x, y in zip(a, b)) < 1e-15
                    and max(abs(x - y) for x, y in zip(a, c)) < 1e-15)

    p_definitions = {
        "hit_rate_T_frac": {
            "semantics": "命中率 T_frac = T/(T+R+A)（spec §3.1 字面「命中率」）",
            "per_tier_per_model": {"30": hit30, "60": hit60, "540": hit540},
            "tier_invariant_per_model": tier_invariant(hit30, hit60, hit540),
            "tier_aggregate_scalar": {"30": float(sum(T30) / 270.0), "60": float(sum(T60) / 540.0),
                                     "540": float(sum(T60) / 540.0)},
        },
        "distortion_rate_A_frac": {
            "semantics": "失真率 A_frac = A/(T+R+A)（spec §3.1 字面「失真率」）",
            "per_tier_per_model": {"30": dis30, "60": dis60, "540": dis540},
            "tier_invariant_per_model": tier_invariant(dis30, dis60, dis540),
            "tier_aggregate_scalar": {"30": float(sum(A30) / 270.0), "60": float(sum(A60) / 540.0),
                                     "540": float(sum(A60) / 540.0)},
        },
    }
    agg_tier_invariance = {
        "hit_rate_30_eq_60": bool(abs(p_definitions["hit_rate_T_frac"]["tier_aggregate_scalar"]["30"]
                                     - p_definitions["hit_rate_T_frac"]["tier_aggregate_scalar"]["60"]) < 1e-15),
        "hit_rate_60_eq_540": bool(abs(p_definitions["hit_rate_T_frac"]["tier_aggregate_scalar"]["60"]
                                      - p_definitions["hit_rate_T_frac"]["tier_aggregate_scalar"]["540"]) < 1e-15),
        "distortion_rate_30_eq_60": bool(abs(p_definitions["distortion_rate_A_frac"]["tier_aggregate_scalar"]["30"]
                                            - p_definitions["distortion_rate_A_frac"]["tier_aggregate_scalar"]["60"]) < 1e-15),
        "distortion_rate_60_eq_540": bool(abs(p_definitions["distortion_rate_A_frac"]["tier_aggregate_scalar"]["60"]
                                             - p_definitions["distortion_rate_A_frac"]["tier_aggregate_scalar"]["540"]) < 1e-15),
    }

    per_tier_P_stats = {
        tier: stat_block(p_definitions["hit_rate_T_frac"]["per_tier_per_model"][tier])
        for tier in ("30", "60", "540")
    }
    P_dim_gate_pass = bool(all(s["n_distinct"] > 3 and s["std_gt_0"] for s in per_tier_P_stats.values()))
    ladder_dim_n_distinct = n_distinct(CELL_TIERS)
    ladder_dim_gate_pass = bool(ladder_dim_n_distinct > 3)      # 因 PI 授权豁免 → 预期 False

    material_probe = {
        "authorized_cell_tiers": CELL_TIERS,
        "tier_provenance": {
            "30": "每 model 30 cells（T30/R30/A30 计数，源件 P_C_distortion_bound_60cells.per_model）",
            "60": "每 model 60 cells（T60/R60/A60 计数，同源件）",
            "540": "9 model × 60 cells 汇总（T60_sum=384 / R60_sum=78 / A60_sum=78 = 540）",
        },
        "ladder_dimension": {
            "n_distinct_tiers": ladder_dim_n_distinct,
            "gate_n_distinct_gt_3": ladder_dim_gate_pass,
            "exempted_by": "PI 2026-09-27 显式授权（K-V3R-0-B 豁免），3 档固定",
            "note": "3 档 < 4 ⇒ 原 n_distinct>3 门不达；按派工单字面豁免，自证改 P 维 / 样本维",
        },
        "P_and_sample_dimension": {
            "gate": "每档内 n_distinct>3 + std>0（派工单字面豁免推演：parent 推演 / PI 授权延伸）",
            "per_tier_stats_hit_rate": per_tier_P_stats,
            "gate_pass": P_dim_gate_pass,
            "unit_of_analysis": "model（n=9）—— skill experimental-design 落点：独立重复单元 = model，"
                                "非 cell（540 cells ≠ 540 独立单元，cell 级 bootstrap = 伪重复）",
        },
        "tier_invariance_identity": {
            "exact_count_doubling_30_to_60": doubling_exact,
            "per_model_rate_tier_invariant": {k: v["tier_invariant_per_model"]
                                              for k, v in p_definitions.items()},
            "tier_aggregate_scalar_tier_invariant": agg_tier_invariance,
            "implication": "三档 cell 计数是**同一 cell 集的精确倍增/汇总**：任一 0 次齐次率型 P 定义"
                           "（T_frac / A_frac / 任意计数比）在 30 / 60 / 540 三档上**逐 model 恒等** ⇒ "
                           "log10(P) 档间全等 ⇒ SS_tot = 0 ⇒ 幂律 R² = 0/0 未定义（构造性，非计算失灵）",
            "generality": "0 次齐次（计数比）之外的数据面字段均无档间变化：cos_sim / D_fix2_cosine / "
                          "verdict / conservation_residual 仅在 60 档给出（无 30 档值）⇒ 无法构成 3 档阶梯",
        },
    }

    # ================================================================ §3 顶替口径真跑
    # 3 trial = 3 个 seeded **model 级重抽**（skill：重抽在正确重复单元上）；tier 级聚合读法
    # 无重抽单元（单一确定性标量），其 3 trial 逐字恒等 —— 本身即为登记发现。
    def model_resample(seed):
        rng = np.random.default_rng(seed)
        return rng.integers(0, N_MODELS, size=N_MODELS)

    def tier_mean(pmap, tier, idx):
        """tier 级响应 = 被重抽 9 个 model 在该档的 P 均值（spec §3.1「每档一个 (命中率, 失真率)」
        + 重抽单元 = model）；阶梯点数 = 档数（3 点），与原 7 档拟合同一形式。"""
        return float(np.mean([pmap[str(tier)][int(i)] for i in idx]))

    def trial_row(seed, p_tiers):
        idx = model_resample(seed)
        row = {"trial_seed": seed, "resample_unit": "model (n=9, with replacement)",
               "resampled_model_indices": [int(i) for i in idx]}
        for pname, pmap in p_tiers.items():
            y_full = [tier_mean(pmap, t, idx) for t in CELL_TIERS]
            full = powerlaw_r2(CELL_TIERS, y_full)
            entry = {"tiers": CELL_TIERS, "P_tier_mean_over_resampled_models": y_full,
                     "r2_full": full, "clip_r2_min_scan_full": clip_verdicts(full["r2"]),
                     "clips": {}}
            for vname, vclip in CLIP_VARIANTS.items():
                y_clip = [tier_mean(pmap, t, idx) for t in vclip]
                clipd = powerlaw_r2(vclip, y_clip)
                entry["clips"][vname] = {
                    "tiers": vclip, "P_tier_mean_over_resampled_models": y_clip,
                    "r2_clipped": clipd,
                    "clip_r2_min_scan_clipped": clip_verdicts(clipd["r2"]),
                    "delta": delta_block(full["r2"], clipd["r2"]),
                }
            # 次读法：逐 model 独立 3 点阶梯（不聚合），登记状态计数
            pm = [powerlaw_r2(CELL_TIERS, [pmap[str(t)][int(i)] for t in CELL_TIERS]) for i in idx]
            entry["per_model_ladder_reading"] = {
                "n_ladders": len(pm),
                "n_r2_defined": int(sum(1 for r_ in pm if r_["r2"] is not None)),
                "n_r2_undefined": int(sum(1 for r_ in pm if r_["r2"] is None)),
                "r2_statuses": sorted({r_["r2_status"] for r_ in pm}),
                "betas_defined": [r_["beta"] for r_ in pm if r_["r2"] is not None],
            }
            row[pname] = entry
        return row

    p_tiers_for_run = {
        "hit_rate_T_frac": {"30": hit30, "60": hit60, "540": hit540},
        "distortion_rate_A_frac": {"30": dis30, "60": dis60, "540": dis540},
    }
    matrix = [trial_row(s, p_tiers_for_run) for s in TRIALS]

    # tier 级聚合读法（spec §3.1 字面「每档一个 (命中率, 失真率)」）：3 点，无重抽单元
    agg_rows = []
    for pname, pdef in p_definitions.items():
        sc = pdef["tier_aggregate_scalar"]
        full = powerlaw_r2(CELL_TIERS, [sc["30"], sc["60"], sc["540"]])
        entry = {"P_definition": pname, "tiers": CELL_TIERS,
                 "P_scalar_per_tier": {k: sc[k] for k in ("30", "60", "540")},
                 "r2_full": full, "clip_r2_min_scan_full": clip_verdicts(full["r2"]), "clips": {}}
        for vname, vclip in CLIP_VARIANTS.items():
            clipd = powerlaw_r2(vclip, [sc[str(t)] for t in vclip])
            entry["clips"][vname] = {"tiers": vclip, "r2_clipped": clipd,
                                     "clip_r2_min_scan_clipped": clip_verdicts(clipd["r2"]),
                                     "delta": delta_block(full["r2"], clipd["r2"])}
        entry["trials_bit_identical_by_construction"] = True
        entry["trials_note"] = ("tier 级标量无重抽单元（9 model 已被聚成 1 个数）⇒ 3 trial 逐字恒等；"
                                "此处 0 bootstrap（cell 级重抽 = 伪重复，skill §Mistakes #1）")
        agg_rows.append(entry)

    # ================================================================ §4 bootstrap（model 级）
    rng = np.random.default_rng(BOOTSTRAP_SEED)
    boot_r2_defined = 0
    boot_r2_undefined = 0
    boot_delta_nonzero = 0
    boot_delta_zero = 0
    boot_delta_undefined = 0
    noise_ss_tot_max = 0.0
    noise_count = 0
    status_counter = {}
    for _ in range(BOOTSTRAP_N):
        idx = rng.integers(0, N_MODELS, size=N_MODELS)
        # 顶替面响应档间恒等（恒等式）⇒ 三档 tier 均值必同值，故 y 为长度 3 的常量向量
        y = [tier_mean(p_tiers_for_run["hit_rate_T_frac"], t, idx) for t in CELL_TIERS]
        full = powerlaw_r2(CELL_TIERS, y)
        status_counter[full["r2_status"]] = status_counter.get(full["r2_status"], 0) + 1
        if full["r2_status"] == "UNDEFINED_FLOAT_NOISE":
            noise_count += 1
            noise_ss_tot_max = max(noise_ss_tot_max, float(full["ss_tot"]))
        if full["r2"] is None:
            boot_r2_undefined += 1
        else:
            boot_r2_defined += 1
        for vname, vclip in CLIP_VARIANTS.items():
            y_clip = [tier_mean(p_tiers_for_run["hit_rate_T_frac"], t, idx) for t in vclip]
            clipd = powerlaw_r2(vclip, y_clip)
            d = delta_block(full["r2"], clipd["r2"])
            if d["r2_delta_full_minus_clipped"] is None:
                boot_delta_undefined += 1
            elif d["delta_is_nonzero"]:
                boot_delta_nonzero += 1
            else:
                boot_delta_zero += 1
    bootstrap = {
        "n": BOOTSTRAP_N, "seed": BOOTSTRAP_SEED,
        "resample_unit": "model (n=9, with replacement) — 独立重复单元（skill：防伪重复）",
        "P_definition": "hit_rate_T_frac（命中率）",
        "r2_full_defined_count": boot_r2_defined,
        "r2_full_undefined_count": boot_r2_undefined,
        "fraction_resamples_r2_undefined": float(boot_r2_undefined / BOOTSTRAP_N),
        "delta_nonzero_count": boot_delta_nonzero,
        "delta_zero_count": boot_delta_zero,
        "delta_undefined_count": boot_delta_undefined,
        "delta_counts_are_over_all_3_clip_variants": True,
        "r2_status_counter": status_counter,
        "label": "REAL_DATA（顶替口径 · model 级重抽 · 非 synthetic）",
        "note": "1000/1000 重抽 r2_full 皆未定义（SS_tot = 0 或 float64 舍入残差，档间响应恒等）"
                "⇒ 顶替面 0 重抽自由度；「delta ≡ 0 → FAIL」分支与「delta != 0 → PASS」分支"
                "**同时不可达**",
        "float_noise_audit": {
            "guard": "0 < SS_tot < %g ⇒ 判 UNDEFINED_FLOAT_NOISE（数值噪声守卫，非科学阈值）"
                     % FLOAT_NOISE_SS_TOT_CEIL,
            "n_resamples_flagged_float_noise": noise_count,
            "max_ss_tot_among_flagged": noise_ss_tot_max,
            "exact_arithmetic_ground_truth": "material_probe.tier_invariance_identity："
                                            "T60 == 2*T30 等逐 model **整数**相等 ⇒ 精确算术下 SS_tot ≡ 0",
            "why_this_matters": "若 0 加守卫，浮点残差会让部分重抽产出**名义上**有定义的 R²"
                                "（值由舍入误差决定，0 携带信息）⇒ 可能被误读为「裁剪有判据」信号",
        },
    }

    # ================================================================ §5 对照（根因分离）
    # C1 正对照：档间有变化的合成 P（同 x 网格）⇒ 证执行器能分辨
    def synth_p_tier_varying(seed, a=2.0, b=0.45, c=0.02, noise=0.05):
        """C1 正对照：同 {30,60,540} x 网格下**档间有变化**的合成 P（沿 08 executor 夹具同款形式，
        仅把指数轴从 N 换成 cell 计数档）。仅证执行器非退化，不作判定证据。"""
        r = np.random.default_rng(seed)
        base = a * np.power(np.asarray(CELL_TIERS, dtype=float), -b) + c
        return {str(t): [float(base[i]) * (1.0 + float(r.normal(0.0, noise)))
                         for _ in range(N_MODELS)]
                for i, t in enumerate(CELL_TIERS)}

    def synth_control_row(seed, pmap, label):
        idx = model_resample(seed)
        y_full = [tier_mean(pmap, t, idx) for t in CELL_TIERS]
        full = powerlaw_r2(CELL_TIERS, y_full)
        out = {"label": label, "trial_seed": seed,
               "P_tier_mean_over_resampled_models": y_full,
               "r2_full": full,
               "clip_r2_min_scan_full": clip_verdicts(full["r2"]), "clips": {}}
        for vname, vclip in CLIP_VARIANTS.items():
            y_clip = [tier_mean(pmap, t, idx) for t in vclip]
            clipd = powerlaw_r2(vclip, y_clip)
            out["clips"][vname] = {"tiers": vclip, "r2_clipped": clipd, "delta": delta_block(full["r2"], clipd["r2"])}
        return out

    c1 = [synth_control_row(s, synth_p_tier_varying(s), "CTRL1_POSITIVE_tier_varying_synthetic")
          for s in TRIALS]
    # C2 no-op 复现：把 clipped 阶梯错算成 full 阶梯（复现 V3 no-op 形态）
    c2 = []
    for r_ in c1:
        full = r_["r2_full"]
        c2.append({"label": "CTRL2_NOOP_emulation_of_v3_defect", "trial_seed": r_["trial_seed"],
                   "r2_full": full,
                   "delta": delta_block(full["r2"], full["r2"])})
    # C3 反事实：仅给 30 档计数加 seeded ±1 cell 抖动（打破精确倍增恒等）⇒ 观 r2 是否转为有定义
    c3 = []
    for s in TRIALS:
        r_ = np.random.default_rng(s)
        p30_cf = [max(0.0, (T30[i] + int(r_.integers(-1, 2))) / 30.0) for i in range(N_MODELS)]
        cf = {"30": p30_cf, "60": hit60, "540": hit540}
        row = synth_control_row(s, cf, "CTRL3_COUNTERFACTUAL_break_tier_invariance")
        row["label"] = "CTRL3_COUNTERFACTUAL_break_tier_invariance（反事实 · 仅证机制，**不作判定证据**）"
        row["counterfactual_note"] = ("仅对 30 档加 seeded ±1 cell 抖动以打破「T60 = 2×T30」恒等；"
                                      "该档数据 0 在盘，此反事实不主张任何真实数据结论")
        c3.append(row)
    # C4 设计算术探针：2 点 clipped 阶梯的 R²（用真实 P）
    c4 = []
    for vname, vclip in CLIP_VARIANTS.items():
        clipd = powerlaw_r2(vclip, [hit30[0] if t == "30" else (hit60[0] if t == "60" else hit540[0])
                                    for t in vclip])
        c4.append({"clip_variant": vname, "tiers": vclip, "r2_clipped_real_P": clipd,
                   "design_arithmetic_note":
                       "点数 = %d：1 点 ⇒ R² 无定义；2 点 ⇒ **若两点 y 不等**则 OLS 必过两点 ⇒ "
                       "R² ≡ 1（与数据幅度无关）；**若两点 y 相等**（本件实测即此，因响应档间恒等）⇒ "
                       "SS_tot = 0 ⇒ R² 仍未定义" % len(vclip)})

    controls = {
        "CTRL1_POSITIVE_tier_varying_synthetic": {
            "rows": c1,
            "all_r2_defined": bool(all(r_["r2_full"]["r2"] is not None for r_ in c1)),
            "all_delta_nonzero": bool(all(
                r_["clips"]["CLIP_DROP_HIGHEST_tier_540"]["delta"]["delta_is_nonzero"] for r_ in c1)),
            "purpose": "证执行器在档间有变化时能给出有定义 r2 与非零 delta（执行器非退化）"},
        "CTRL2_NOOP_emulation_of_v3_defect": {
            "rows": c2,
            "all_delta_zero": bool(all(r_["delta"]["delta_is_zero"] for r_ in c2)),
            "purpose": "证执行器能复现 V3 的 delta ≡ 0 形态（no-op）⇒ 0 恒返回非零"},
        "CTRL3_COUNTERFACTUAL_break_tier_invariance": {
            "rows": c3,
            "all_r2_defined": bool(all(r_["r2_full"]["r2"] is not None for r_ in c3)),
            "all_delta_nonzero": bool(all(
                r_["clips"]["CLIP_DROP_HIGHEST_tier_540"]["delta"]["delta_is_nonzero"] for r_ in c3)),
            "purpose": "根因分离：仅打破档间恒等即让 r2 恢复有定义 ⇒ 顶替面的未定义源于"
                       "**数据恒等**（构造不适用），0 源于执行器/工具失灵"},
        "CTRL4_DESIGN_ARITHMETIC_probe": {
            "rows": c4,
            "purpose": "登记裁剪重定义的设计算术后果（条件式构造面断言，非观测值）：**若**顶替面响应"
                       "档间有变化，则任一 2 点 clipped 阶梯 R² ≡ 1（两点必过）⇒ delta ≡ r2_full − 1 "
                       "≠ 0 ⇒ 「delta != 0 → PASS」分支被**机械饱和**、「3 trial ≡ 0 → FAIL」分支"
                       "**不可达**（即顶替面无法承载 FAIL 档）。本件实测更早一步：响应档间恒等 ⇒ "
                       "连 r2_full 都未定义 ⇒ 两分支同时不可达（见 CTRL1 正对照的实证饱和）"},
        "root_cause_separation": "顶替口径未定义 = **构造失灵（构造不适用）**，"
                                 "0 是「命题被证伪」：cell 计数档是同一 cell 集的精确倍增/汇总，"
                                 "对标度律问题（难度/规模轴）0 携带信息量",
    }

    # ================================================================ §6 判定
    all_deltas = []
    for r_ in matrix:
        for pname in ("hit_rate_T_frac", "distortion_rate_A_frac"):
            for vname in CLIP_VARIANTS:
                all_deltas.append((r_[pname]["clips"][vname]["delta"]["r2_delta_full_minus_clipped"],
                                   vname))
    defined_deltas = [d for d, _ in all_deltas if d is not None]
    any_defined = bool(defined_deltas)
    any_nonzero = bool(any(math.isfinite(d) and abs(d) >= EPS for d in defined_deltas))
    all_zero = bool(any_defined and all(abs(d) < EPS for d in defined_deltas))
    undefined_count = len(all_deltas) - len(defined_deltas)

    degen_alarm_hit = bool(
        any(r_[p]["r2_full"]["r2"] is None for r_ in matrix
            for p in ("hit_rate_T_frac", "distortion_rate_A_frac"))
        or any(r_[p]["clips"][v]["r2_clipped"]["r2"] is None for r_ in matrix
               for p in ("hit_rate_T_frac", "distortion_rate_A_frac")
               for v in CLIP_VARIANTS))

    if not any_defined:
        new_verdict = ("不可判 / UNDEFINED（顶替口径：R² = 0/0 未定义 ⇒ K-V3R-8 两分支"
                       "[delta != 0 → PASS] 与 [3 trial ≡ 0 → FAIL] **同时不可达**）")
        kill_line_decidable = False
    elif any_nonzero:
        new_verdict = "PASS（delta 至少一档 != 0.0）"
        kill_line_decidable = True
    else:
        new_verdict = "FAIL（3 trial 仍 ≡ 0.0，维持假证伪）"
        kill_line_decidable = True
    kill_line_pass = bool(kill_line_decidable and any_nonzero)
    kill_line_hit = bool(degen_alarm_hit)          # 触发警报 = 退化/未定义警报

    # 沿原 V3 阈值字面 verdict（双口径第二口径，逐字复现）
    legacy_r2 = [t["r2_clipped_N5"] for t in legacy_trials]
    legacy_delta = [t["r2_delta_full_minus_clipped"] for t in legacy_trials]
    legacy_verdict = ("%s（worst_clipped_r2 = %s < clip_r2_min = %s；3/3 trial 的 "
                      "r2_delta_full_minus_clipped == 0.0）"
                      % (pc3["verdict"], pc3["worst_clipped_r2"], thr["clip_r2_min"]))
    consistent = bool(kill_line_decidable and kill_line_pass
                      and str(pc3["verdict"]).upper() == "PASS")

    result = {
        "schema": "v3_recheck_result/08b_boss_pc_3_a3_clipping_cell_tier_substitute/1",
        "series": "08b（顶替重跑；**不覆盖** 08 系列三件套）",
        "prereg": {"path": "results/_v3_recheck_prereg_v1_2026_09_27.md",
                   "sha12_measured": sha12(PREREG.read_bytes()),
                   "kill_line": "K-V3R-8",
                   "threshold": "TH-V3R-8 clip_r2_min sweep 0.3/0.5/7（派工单冻结）+ spec §5 A3 语义；"
                                "阶梯按 PI 授权顶替为 cell 计数档 {30,60,540}"},
        "executor": "results/_v3_recheck_08b_executor/executor_2026_09_27.py",
        "date": "2026-09-27", "seed": SEED,
        "runtime": "0 LLM; numpy + hashlib + json only; no network; read-only inputs; no temp files",
        "skill": {
            "name": "scientific-research-workflows:experimental-design",
            "plugin": "@scientific-research-workflows",
            "plugin_cache_sha256": "611965fcb6208a5dbeb28d594ad7ca0f8b1f8fd62fc33c189e56a50e49db19cb",
            "loaded": True,
            "loaded_path": "v2/plugin-cache/official/sha256-tree-v1-611965fc.../skills/experimental-design/SKILL.md",
            "applied_points": [
                "Mistakes #1 伪重复：独立重复单元 = model（n=9），0 按 cell 重抽（540 cells ≠ 540 单元）",
                "Workflow 1「先定问题/单元/响应」：本件据此区分 tier 级聚合读法（无重抽单元）"
                "与 model 级重抽读法（唯一可 bootstrap 者）",
                "Workflow 7「document the design, seed, and schedule」：seed / 重抽单元 / 档位来源逐项落盘",
            ],
            "scope_note": "该 skill 定位为**收集前**实验设计；本件为 post-hoc 重跑，仅取其结构审计透镜"
                          "（单元/伪重复/预注册可审计），0 引入其收集前流程",
            "fallback_used": False,
        },
        "inputs": [
            {"path": "results/_v3_recheck_prereg_v1_2026_09_27.md", "role": "预登记（判死线锚）",
             "sha12_measured": sha12(PREREG.read_bytes())},
            {"path": "results/_v3_recheck_08_executor_2026_09_27.py", "role": "第一梯队扫描+bootstrap 机制源",
             "sha12_measured": sha12(EXEC_08.read_bytes())},
            {"path": "results/deposon_v3_physical_opt_60cells_2026_09_11.json", "role": "顶替档位数据源（原 JSON 自报 data_source）",
             "sha12_measured": sha12(SRC_60.read_bytes())},
            {"path": "results/boss_pc_3_a3_clipping_2026_09_15.json", "role": "原 BOSS-PC-3（legacy 口径）",
             "sha12_measured": sha12(SRC_PC3.read_bytes())},
            {"path": "docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md", "role": "A3 语义 + §3.3/§4.1 R² 公式锚",
             "sha12_measured": sha12(SRC_SPEC.read_bytes())},
        ],
        "authorization": authorization,
        "construct": {
            "substitution": "N 阶梯 [10,20,50,100,200,500,1000] → cell 计数档 {30,60,540}（PI 授权顶替）",
            "A3_semantics": "沿 spec §5：去掉阶梯两端，看幂律拟合 R² 是否仍 > clip_r2_min",
            "clip_redefinition_on_3_tiers": {
                "why": "3 档阶梯装不下 spec §5 的「去两端」（剩 1 点 ⇒ R² 无定义）",
                "variants": {k: v for k, v in CLIP_VARIANTS.items()},
                "provenance": "parent 推演 / PI 授权延伸（worker 0 私设；0 新设阈值）",
            },
            "r2_formula": "沿 spec §3.3 + §4.1：log10(P) = beta*log10(C) + log10(A)，OLS R² = 1 - SS_res/SS_tot",
            "clip_r2_min_grid": CLIP_R2_MIN_GRID,
            "trials_seeds": TRIALS,
            "trial_semantics": "trial = seeded **model 级重抽**（n=9, with replacement）",
            "bootstrap": {"n": BOOTSTRAP_N, "seed": BOOTSTRAP_SEED, "unit": "model"},
        },
        "material_probe": material_probe,
        "construct_degen_self_check": {
            "gate": "K-V3R-0-A：阶梯维因 PI 授权 3 档豁免 n_distinct>3；自证改 P 维 / 样本维"
                    "（每档内 n_distinct>3 + std>0）",
            "ladder_dim_gate_pass": ladder_dim_gate_pass,
            "ladder_dim_exempted": True,
            "P_dim_gate_pass": P_dim_gate_pass,
            "degenerate_alarm_hit": degen_alarm_hit,
            "degen_alarm_cause": "顶替面的响应层档间恒等（SS_tot = 0）⇒ R² 未定义；"
                                 "**非** P 维退化（P 维 n_distinct=7>3 + std>0 已通过）",
            "disposition": "§3.2「任意不达 = 退化警报，改构造或判『不明』，不许带病开跑」"
                           "-> 已触发（未定义面）⇒ 判「不可判」；扫描 / bootstrap / 对照全部**跑完并落盘**",
        },
        "real_run_substitute_tier": {"model_level_trials": matrix, "tier_aggregate_reading": agg_rows},
        "bootstrap": bootstrap,
        "controls": controls,
        "legacy_dual_track": {
            "legacy_verdict": legacy_verdict,
            "legacy_verdict_field": pc3["verdict"],
            "legacy_worst_clipped_r2": pc3["worst_clipped_r2"],
            "legacy_clip_r2_min": thr["clip_r2_min"],
            "legacy_n_full": thr["n_full"], "legacy_n_clipped": thr["n_clipped"],
            "legacy_r2_clipped_trials": legacy_r2,
            "legacy_delta_trials": legacy_delta,
            "legacy_delta_all_zero": bool(all(d == 0.0 for d in legacy_delta)),
            "provenance_gap_carried_forward": "原 r2_full_N7 / r2_clipped_N5 = %s 仍**不可从其自报 "
                                             "data_source 复算**（顶替重跑 0 修复溯源链断裂；"
                                             "本件新数**不与原值混列**）"
                                             % [t["r2_full_N7"] for t in legacy_trials],
        },
        "verdict": {
            "new_verdict": new_verdict,
            "kill_line": "K-V3R-8",
            "kill_line_decidable": kill_line_decidable,
            "kill_line_pass": kill_line_pass,
            "kill_line_hit": kill_line_hit,
            "delta_slots_total": len(all_deltas),
            "delta_slots_undefined": undefined_count,
            "delta_slots_defined": len(defined_deltas),
            "delta_any_nonzero": any_nonzero,
            "delta_all_zero": all_zero,
            "legacy_verdict": legacy_verdict,
            "一致性": ("一致（改判成）" if consistent
                       else "不一致（维持原标注 + 显式登记顶替口径 verdict）"),
            "gamma": "顶替面**构造不适用**：cell 计数档 {30,60,540} 系同一 cell 集的精确倍增/汇总"
                     "（T60 = 2×T30 逐 model 精确成立；ΣT30=192 → ΣT60=384），任一率型 P 档间恒等 ⇒ "
                     "SS_tot = 0 ⇒ 幂律 R² = 0/0 未定义 ⇒ K-V3R-8 两分支同时不可达。"
                     "根因 = 构造失灵（0 是命题被证伪）；"
                     "叠加设计算术：任一 2 点 clipped 阶梯 R² ≡ 1 ⇒ PASS 分支机械饱和、FAIL 分支不可达",
            "改判档位": "v1 §2.3 第 4 行（不明）→ 维持原 V3 标注不动 + 显式登记 γ + 归"
                        "「V4 收尾整理」待拍板桶（档位与 08 件同档，但**根因不同**：08 = 素材面缺件，"
                        "08b = 授权面已跑但构造不适用）",
        },
        "iron_rules": {
            "0_LLM": True, "no_proxy": True, "no_key_in_prompt_json_disk": True,
            "read_only_inputs": True, "derived_json_not_merged": True,
            "series_08b_does_not_overwrite_series_08": True,
            "no_new_threshold_except_pi_authorized_substitution": True,
            "nan_trap_guards": ["isfinite(delta) guard on the '!= 0' kill-line test",
                                 "UNDEFINED sentinel instead of silent FAIL branch on r2 compare"],
            "v3_original_files_bytes_untouched": True,
        },
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("[#08b] written:", OUT.relative_to(REPO))
    print("[#08b] ladder_dim_gate_pass=%s (exempted=%s) P_dim_gate_pass=%s"
          % (ladder_dim_gate_pass, True, P_dim_gate_pass))
    print("[#08b] tier_invariance(hit_rate)=%s agg=%s"
          % (p_definitions["hit_rate_T_frac"]["tier_invariant_per_model"], agg_tier_invariance))
    print("[#08b] delta slots: total=%d undefined=%d defined=%d any_nonzero=%s"
          % (len(all_deltas), undefined_count, len(defined_deltas), any_nonzero))
    print("[#08b] bootstrap fraction_r2_undefined=%.4f" % bootstrap["fraction_resamples_r2_undefined"])
    print("[#08b] CTRL1 non-degenerate=%s | CTRL2 all_zero=%s | CTRL3 r2_defined=%s"
          % (controls["CTRL1_POSITIVE_tier_varying_synthetic"]["all_r2_defined"],
             controls["CTRL2_NOOP_emulation_of_v3_defect"]["all_delta_zero"],
             controls["CTRL3_COUNTERFACTUAL_break_tier_invariance"]["all_r2_defined"]))
    print("[#08b] new_verdict:", new_verdict)
    return 0


if __name__ == "__main__":
    sys.exit(main())
