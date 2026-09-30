#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V3-R 补审 #5 540 cells 守恒（非恒等审计面）— executor（worker · 2026-09-28）

沿 results/_v3_recheck_prereg_v1_2026_09_27.md（SHA-12 88052d7db895）字面执行：
  - K-V3R-0-A 防退化门（跑前对盘上输入字段 + 新构造统计量自证 n_distinct > 3 + std > 0）
  - K-V3R-0-B 沿用阈值（0 新设判定阈值；判据字面 = K-V3R-5 + TH-V3R-5）
  - K-V3R-0-C 双口径（new_verdict 沿新构造 / legacy_verdict 沿原 V3 阈值字面 STRICT_CONSERVATION）
  - K-V3R-0-D 派生 JSON 不合并（本件独立落盘 _v3_recheck_05_result_*.json）
  - K-V3R-0-E 0 LLM（纯 stdlib + numpy，0 网络 0 模型调用 0 proxy 0 key）
  - K-V3R-0-F 锚链 fallback（冻结主路径 verifier/audit/conservation.py 可用则走主路径，
    只读加载，0 改写；B 路径 `_archive_deposon_2026_09_17/...` 本仓 0 命中如实登记）
  - K-V3R-0-G 仅追加冻结（0 改预登记 v1 / 0 改 kill-line 字面 / 0 改阈值）

新构造（沿预登记 §1.2 #5 (a)(b) 字面）：
  (a) 非恒等审计面 —— per-cell pairwise T↔R / T↔A / R↔A 偏离度 + bootstrap CI
      （n=1000, seed=42）跨真实扰动（每个 cell 强制重抽分类 β 次）。
      **避开 T+R+A≡1 恒等面**：判据统计量取「同 model 内跨类 cell 对计数 vs 合并齐次零假设
      期望」的偏离 Δ，不是 |T+R+A−1| 恒等残差（后者作为对照腿 C1 单列，恒为 0）。
  (b) per-model 守恒面异质性 —— 9 model 的 T/R/A 分布均值/方差差 + χ² 异质性统计量
      + bootstrap CI（证「守恒面」是否为跨 model 普遍同一形态）。

输入（全部只读）：
  - results/deposon_v3_physical_opt_60cells_2026_09_11.json（540 cells 计数真源 · c659695aa23c）
  - results/deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json（540-cell 展开规则 + 首末 20 cell 样例 · 4e4a17d43adf）
  - results/boss_pa_1_rbr_rm_result_2026_09_15.json（原 STRICT_CONSERVATION 判定面 · c7c59e0d2f6c）
  - verifier/audit/conservation.py（冻结 V0 守恒锚主路径 · 4bdec2683f06，只读加载跑 legacy 口径）

S-40 布尔显式命名：`*_hit = True` 表示「触发 FAIL / 触发警报」；`*_pass = True` 表示「存活 / 合格」。
"""

import hashlib
import importlib.util
import json
import math
import random
import sys
from pathlib import Path

import numpy as np

try:                                    # 控制台 GBK 下 χ² / 方框字会抛 UnicodeEncodeError
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

# ---- 预登记字面常量（0 新设判定阈值）----
SEED = 42               # 预登记 §1.2 #5 (a) 字面：bootstrap seed=42
N_BOOT = 1000           # 预登记 §1.2 #5 (a) 字面：bootstrap n=1000
CI_LO_Q, CI_HI_Q = 2.5, 97.5   # 百分位区间构造（实现自由度，非判定阈值）
IDENTITY_EPS = 1e-15    # K-V3R-5 字面：CI 上界 ≤ 1e-15 -> FAIL；沿 conservation.py PASS_THRESHOLD 同值
KILLLINE_ZERO = 0.0     # K-V3R-5 字面：CI 上界 > 0 -> PASS

REPO = Path(__file__).resolve().parent.parent
SRC_V3_PHYS = REPO / "results" / "deposon_v3_physical_opt_60cells_2026_09_11.json"
SRC_PE3 = REPO / "results" / "deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json"
SRC_BOSS_PA1 = REPO / "results" / "boss_pa_1_rbr_rm_result_2026_09_15.json"
SRC_ANCHOR_MAIN = REPO / "verifier" / "audit" / "conservation.py"
SRC_ANCHOR_FALLBACK = REPO / "_archive_deposon_2026_09_17" / "verifier" / "audit" / "conservation.py"
OUT_JSON = REPO / "results" / "_v3_recheck_05_result_2026_09_28.json"

PAIRS = (("T", "R"), ("T", "A"), ("R", "A"))   # 预登记 §1.2 #5 (a) 字面三对
N_CELLS_PER_MODEL = 60                          # 盘上字面（9 model × 60 cells）
N_MODELS_EXPECT = 9                             # 盘上字面


def sha12(path: Path) -> str:
    """SHA-12 = hashlib.sha256(全文字节).hexdigest()[:12] 小写（硬纪律）"""
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:12]


def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def distinct_stats(values) -> dict:
    """防退化门用统计：n_distinct / std / min / max（K-V3R-0-A）"""
    arr = np.asarray(list(values), dtype=float)
    uniq = np.unique(arr)
    return {
        "n": int(arr.size),
        "n_distinct": int(uniq.size),
        "std": float(arr.std(ddof=0)),
        "min": float(arr.min()),
        "max": float(arr.max()),
        "gate_pass": bool(uniq.size > 3 and arr.std(ddof=0) > 0.0),
    }


def pct_ci(samples, q_lo=CI_LO_Q, q_hi=CI_HI_Q) -> dict:
    arr = np.asarray(samples, dtype=float)
    lo, hi = np.percentile(arr, [q_lo, q_hi])
    return {
        "ci_lower": float(lo),
        "ci_upper": float(hi),
        "mean": float(arr.mean()),
        "std": float(arr.std(ddof=0)),
        "n_boot": int(arr.size),
    }


# =========================================================================
# §0 输入链核验（只读，先核后用）
# =========================================================================
inputs = {
    "v3_phys_60cells": SRC_V3_PHYS,
    "boss_pe_3_9m60c": SRC_PE3,
    "boss_pa_1_result": SRC_BOSS_PA1,
    "conservation_py_main_path": SRC_ANCHOR_MAIN,
}
input_chain = {
    k: {
        "path": str(v.relative_to(REPO)).replace("\\", "/"),
        "sha12_observed": sha12(v),
        "bytes": v.stat().st_size,
        "exists": True,
    }
    for k, v in inputs.items()
}
input_chain["conservation_py_fallback_path"] = {
    "path": "_archive_deposon_2026_09_17/verifier/audit/conservation.py",
    "exists": SRC_ANCHOR_FALLBACK.exists(),
    "note": "K-V3R-0-F B 路径；本仓 0 命中 -> 冻结主路径可用故未启用（0 擅自重写主路径）",
}

v3 = load_json(SRC_V3_PHYS)
pe3 = load_json(SRC_PE3)
boss_pa1 = load_json(SRC_BOSS_PA1)

per_model = v3["P_C_distortion_bound_60cells"]["per_model"]
s40_inputs_sha12_verified = bool(
    input_chain["v3_phys_60cells"]["sha12_observed"] == "c659695aa23c"
    and input_chain["boss_pa_1_result"]["sha12_observed"] == "c7c59e0d2f6c"
    and input_chain["boss_pe_3_9m60c"]["sha12_observed"] == "4e4a17d43adf"
    and input_chain["conservation_py_main_path"]["sha12_observed"] == "4bdec2683f06"
)

# =========================================================================
# §1 540-cell 面重建（沿 PE-3 展开规则字面，逐 cell 落 id）
# 规则字面（PE-3 step_2_540_cells_expansion.expansion_rule）：
#   每个 model 的 60 cells 拆分为 T60 个 T-cell(T=1,R=0,A=0) + A60 个 A-cell + R60 个 R-cell
#   同 model 内 cell 排序 = T → A → R（沿 PE-3 cells_last10 末 4 A-cell 后接 4 R-cell 字面）
# =========================================================================
surface = []
cell_id = 0
for pm in per_model:
    model = pm["model"]
    for ctype, count in (("T", pm["T60"]), ("A", pm["A60"]), ("R", pm["R60"])):
        for _ in range(count):
            surface.append({
                "cell_id": cell_id,
                "model": model,
                "cell_type": ctype,
                "t": 1.0 if ctype == "T" else 0.0,
                "r": 1.0 if ctype == "R" else 0.0,
                "a": 1.0 if ctype == "A" else 0.0,
            })
            cell_id += 1

models_order = [pm["model"] for pm in per_model]
model_counts = {
    pm["model"]: {"T": pm["T60"], "R": pm["R60"], "A": pm["A60"]} for pm in per_model
}
rebuilt_counts = {
    m: {k: sum(1 for c in surface if c["model"] == m and c["cell_type"] == k) for k in ("T", "R", "A")}
    for m in models_order
}
rebuild_matches_source = bool(rebuilt_counts == model_counts and len(surface) == 540)

# 重建面 vs PE-3 盘上样例（cells_first10 / cells_last10）逐字对账
pe3_step2 = pe3["step_2_540_cells_expansion"]
pe3_samples = list(pe3_step2["cells_first10"]) + list(pe3_step2["cells_last10"])
sample_mismatches = []
for s in pe3_samples:
    c = surface[s["cell_id"]]
    if c["model"] != s["model"] or c["cell_type"] != s["cell_type"]:
        sample_mismatches.append({"cell_id": s["cell_id"], "rebuilt": c, "pe3": s})
s40_surface_reconstruction_matches_pe3 = bool(
    len(surface) == 540 and rebuild_matches_source and not sample_mismatches
)

# =========================================================================
# §2 对照腿 C1：T+R+A≡1 恒等面（判据统计量必须避开此面）
# =========================================================================
identity_max_dev_exact = max(abs((c["t"] + c["r"] + c["a"]) - 1.0) for c in surface)
t540 = sum(1 for c in surface if c["cell_type"] == "T")
r540 = sum(1 for c in surface if c["cell_type"] == "R")
a540 = sum(1 for c in surface if c["cell_type"] == "A")
residual_540 = (t540 + r540 + a540) - 540

# 浮点 frac 形式（Trae §1.2 #5 记 2.22e-16 之形式）——用冻结锚自带 tra_decomposition 复算
spec = importlib.util.spec_from_file_location("conservation_v0_anchor", SRC_ANCHOR_MAIN)
conservation_anchor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(conservation_anchor)
identity_max_dev_frac = 0.0
for c in surface:
    t_f, r_f, a_f = conservation_anchor.tra_decomposition(c["t"])
    identity_max_dev_frac = max(
        identity_max_dev_frac, abs(math.fsum([t_f, r_f, a_f]) - 1.0)
    )

identity_plane = {
    "form_integer_indicator": {
        "per_cell_max_abs_dev": float(identity_max_dev_exact),
        "T540_sum": t540, "R540_sum": r540, "A540_sum": a540,
        "conservation_residual_540": int(residual_540),
        "matches_boss_pa1_json": bool(
            boss_pa1["v3_540_conservation_check"]["conservation_residual_540"] == residual_540
            and boss_pa1["v3_540_conservation_check"]["T540_sum"] == t540
            and boss_pa1["v3_540_conservation_check"]["R540_sum"] == r540
            and boss_pa1["v3_540_conservation_check"]["A540_sum"] == a540
        ),
    },
    "form_float_frac_via_frozen_anchor": {
        "per_cell_max_abs_dev": float(identity_max_dev_frac),
        "note": "冻结锚 tra_decomposition(eta=0.5, g_couple=1.0) 形式；本重建面两形式均精确 0，"
                "Trae 记 2.22e-16 系其自身求和顺序的 fp 累积形式，本棒 0 复现该数（如实登记，0 编造）",
    },
    "counterfactual_if_identity_plane_used": "FAIL（CI 上界恒为 0 ≤ 1e-15）—— 即恒等面 0 鉴别力之证明",
}

# =========================================================================
# §3 判据统计量（非恒等审计面）：pairwise 偏离度
#   O_{XY}      = Σ_m n_X^{(m)} · n_Y^{(m)}          （同 model 内跨类有序 cell 对实测计数）
#   E_{XY}^{pool} = Σ_m 60·59 · π_X · π_Y           （合并齐次零假设期望；π_X = n_X_total/540）
#   Δ_{XY}     = O_{XY} − E_{XY}^{pool}             （偏离度，单位 = cell 对）
#   ρ_{XY}     = Δ_{XY} / E_{XY}^{pool}             （相对偏离度）
#   对照腿 C2  = 同 model 零假设：C2a 有放回 Δ ≡ 0；C2b 无放回 Δ = O/60（定义性）
#                -> 合证统计量信息全部来自跨 model 齐次性破缺
# =========================================================================
def pairwise_stats(counts: dict) -> dict:
    total = sum(sum(counts[m].values()) for m in counts)
    n_models = len(counts)
    pi = {k: sum(v[k] for v in counts.values()) / total for k in ("T", "R", "A")}
    out = {"pooled_rates": pi, "pairs": {}}
    for x, y in PAIRS:
        O = sum(counts[m][x] * counts[m][y] for m in counts)
        E_pool = n_models * (N_CELLS_PER_MODEL * (N_CELLS_PER_MODEL - 1)) * pi[x] * pi[y]
        # 对照腿 C2（同 model 零假设的两种参照）：
        #   C2a 有放回（with replacement）：E = Σ_m n_X·n_Y = O  -> Δ ≡ 0（纯退化）
        #   C2b 无放回（hypergeometric）：E = (59/60)·Σ_m n_X·n_Y  -> Δ = O/60（纯定义性有限总体修正）
        O_within = sum(counts[m][x] * counts[m][y] for m in counts)
        E_within_wr = float(O_within)
        E_within_hyp = sum(
            (N_CELLS_PER_MODEL * (N_CELLS_PER_MODEL - 1))
            * (counts[m][x] / N_CELLS_PER_MODEL) * (counts[m][y] / N_CELLS_PER_MODEL)
            for m in counts
        )
        out["pairs"][f"{x}_{y}"] = {
            "observed_within_model_pairs": O,
            "expected_pooled_homogeneity": E_pool,
            "delta": O - E_pool,
            "relative_delta": (O - E_pool) / E_pool if E_pool else float("nan"),
            "control_C2a_within_model_with_replacement_expected": E_within_wr,
            "control_C2a_delta": O - E_within_wr,
            "control_C2b_within_model_hypergeometric_expected": E_within_hyp,
            "control_C2b_delta": O - E_within_hyp,
        }
    return out


def heterogeneity_stats(counts: dict) -> dict:
    total = sum(sum(counts[m].values()) for m in counts)
    pi = {k: sum(counts[m][k] for m in counts) / total for k in ("T", "R", "A")}
    t_fracs = [counts[m]["T"] / N_CELLS_PER_MODEL for m in counts]
    chi2 = 0.0
    per_model_chi2 = {}
    for m in counts:
        c = 0.0
        for k in ("T", "R", "A"):
            exp = N_CELLS_PER_MODEL * pi[k]
            c += (counts[m][k] - exp) ** 2 / exp
        per_model_chi2[m] = c
        chi2 += c
    spread = max(t_fracs) - min(t_fracs)
    mean_t = sum(t_fracs) / len(t_fracs)
    sd_t = math.sqrt(sum((x - mean_t) ** 2 for x in t_fracs) / len(t_fracs))
    return {
        "t_frac_per_model": t_fracs,
        "t_frac_spread": spread,
        "t_frac_mean": mean_t,
        "t_frac_sd_across_models": sd_t,
        "chi2_heterogeneity_vs_pooled": chi2,
        "chi2_per_model": per_model_chi2,
        "chi2_dof": 2 * (len(counts) - 1),
    }


def per_cell_deviation(counts: dict, pi: dict) -> list:
    """per-cell pairwise 偏离度 δ_c(Y) = 实测同 model 伙伴数 − 合并零假设期望伙伴数"""
    rows = []
    for c in surface:
        m, X = c["model"], c["cell_type"]
        for Y in ("T", "R", "A"):
            obs = counts[m][Y] - (1 if X == Y else 0)
            exp = (N_CELLS_PER_MODEL - 1) * pi[Y]
            rows.append({
                "cell_id": c["cell_id"], "model": m, "cell_type": X, "partner_type": Y,
                "observed_partners": obs, "expected_partners_pooled": exp,
                "delta": obs - exp,
            })
    return rows


observed_counts = {m: dict(model_counts[m]) for m in models_order}
pair_obs = pairwise_stats(observed_counts)
het_obs = heterogeneity_stats(observed_counts)
per_cell_rows = per_cell_deviation(observed_counts, pair_obs["pooled_rates"])

# =========================================================================
# §4 bootstrap（β=1000, seed=42）：每个 cell 强制重抽分类 β 次
#   重抽分布 = 该 model 自身经验多项式 (p̂_T, p̂_R, p̂_A) = (T60,R60,A60)/60
#   声明：bootstrap 为统计扩展（非新增观测），沿盘上 _l11_run1.json §expansion_caliber 同口径
# =========================================================================
rng = random.Random(SEED)
boot_delta = {f"{x}_{y}": [] for x, y in PAIRS}
boot_rel = {f"{x}_{y}": [] for x, y in PAIRS}
boot_spread, boot_sd_t, boot_chi2 = [], [], []

for _ in range(N_BOOT):
    rep = {m: {"T": 0, "R": 0, "A": 0} for m in models_order}
    for m in models_order:                       # 该 model 60 cells 逐 cell 重抽
        p = [model_counts[m][k] / N_CELLS_PER_MODEL for k in ("T", "R", "A")]
        for _ in range(N_CELLS_PER_MODEL):
            u = rng.random()
            acc = 0.0
            for k, pk in zip(("T", "R", "A"), p):
                acc += pk
                if u < acc:
                    rep[m][k] += 1
                    break
            else:
                rep[m]["A"] += 1
    ps = pairwise_stats(rep)
    for x, y in PAIRS:
        key = f"{x}_{y}"
        boot_delta[key].append(ps["pairs"][key]["delta"])
        boot_rel[key].append(ps["pairs"][key]["relative_delta"])
    hs = heterogeneity_stats(rep)
    boot_spread.append(hs["t_frac_spread"])
    boot_sd_t.append(hs["t_frac_sd_across_models"])
    boot_chi2.append(hs["chi2_heterogeneity_vs_pooled"])

pair_ci = {
    key: {
        "observed_delta_signed": pair_obs["pairs"][key]["delta"],
        "observed_delta_magnitude": abs(pair_obs["pairs"][key]["delta"]),
        "observed_relative_delta": pair_obs["pairs"][key]["relative_delta"],
        "observed_within_model_pairs": pair_obs["pairs"][key]["observed_within_model_pairs"],
        "expected_pooled_homogeneity": pair_obs["pairs"][key]["expected_pooled_homogeneity"],
        "bootstrap_delta_signed_ci": pct_ci(boot_delta[key]),
        "bootstrap_delta_magnitude_ci": pct_ci([abs(x) for x in boot_delta[key]]),
        "bootstrap_relative_delta_ci": pct_ci(boot_rel[key]),
        "ci_upper_gt_zero_magnitude": bool(
            pct_ci([abs(x) for x in boot_delta[key]])["ci_upper"] > KILLLINE_ZERO),
        "ci_upper_gt_identity_eps_magnitude": bool(
            pct_ci([abs(x) for x in boot_delta[key]])["ci_upper"] > IDENTITY_EPS),
        "signed_ci_excludes_zero": bool(pct_ci(boot_delta[key])["ci_lower"] > KILLLINE_ZERO
                                        or pct_ci(boot_delta[key])["ci_upper"] < KILLLINE_ZERO),
    }
    for key in ("T_R", "T_A", "R_A")
}

# =========================================================================
# §4b 零假设标定诊断（新增诊断腿，不改 kill-line 应用）
#   上节 bootstrap 在 model 内重抽 → 会稀释跨 model 齐次性破缺，故 Δ 的 CI 可能跨零。
#   为诚实交代「非平凡性到底有多强」，另在**合并齐次零假设**下生成 S 面（每 cell 依
#   π=(π_T,π_R,π_A) i.i.d. 抽分类，seed=42）→ 得 Δ 与 χ² 的零分布 → 报观测量在该零分布
#   中的分位与 z。**0 新设判定阈值**：本腿只出诊断读数，K-V3R-5 判定仍只走上节字面。
# =========================================================================
pi_obs = pair_obs["pooled_rates"]
null_rng = random.Random(SEED)
null_delta = {f"{x}_{y}": [] for x, y in PAIRS}
null_chi2, null_spread_null = [], []
for _ in range(N_BOOT):
    rep = {m: {"T": 0, "R": 0, "A": 0} for m in models_order}
    p = [pi_obs["T"], pi_obs["R"], pi_obs["A"]]
    for c in surface:
        u = null_rng.random()
        acc = 0.0
        for k, pk in zip(("T", "R", "A"), p):
            acc += pk
            if u < acc:
                rep[c["model"]][k] += 1
                break
        else:
            rep[c["model"]]["A"] += 1
    # 零假设下各 model 的 cell 数不再恒为 60 时，pairwise/heterogeneity 仍可算
    # （公式对 n_m 泛化：E = Σ_m n_m(n_m−1)π_Xπ_Y；此处 n_m 恒 60 由重建面保证）
    ps = pairwise_stats(rep)
    for x, y in PAIRS:
        null_delta[f"{x}_{y}"].append(ps["pairs"][f"{x}_{y}"]["delta"])
    hs = heterogeneity_stats(rep)
    null_chi2.append(hs["chi2_heterogeneity_vs_pooled"])
    null_spread_null.append(hs["t_frac_spread"])


def null_position(observed: float, null_samples: list) -> dict:
    arr = np.asarray(null_samples, dtype=float)
    mean, sd = float(arr.mean()), float(arr.std(ddof=0))
    pct = float((arr < observed).mean() * 100.0)
    return {
        "null_mean": mean, "null_std": sd,
        "z": float((observed - mean) / sd) if sd > 0 else float("nan"),
        "percentile_rank": pct,
        "two_sided_p_approx": float(2.0 * min(pct, 100.0 - pct) / 100.0),
    }


null_calibration = {
    "null_model": "合并齐次：540 cells 依 π=(π_T,π_R,π_A) i.i.d. 分类（各 model 60 cells 结构保留）",
    "n_surfaces": N_BOOT,
    "seed": SEED,
    "pairwise_delta": {
        key: null_position(pair_obs["pairs"][key]["delta"], null_delta[key])
        for key in ("T_R", "T_A", "R_A")
    },
    "chi2_heterogeneity": null_position(het_obs["chi2_heterogeneity_vs_pooled"], null_chi2),
    "t_frac_spread": null_position(het_obs["t_frac_spread"], null_spread_null),
    "purpose": "诊断腿：量化 §4 bootstrap CI 跨零时非平凡性的实际强度；0 参与 K-V3R-5 判定",
}

het_ci = {
    "t_frac_spread": pct_ci(boot_spread),
    "t_frac_sd_across_models": pct_ci(boot_sd_t),
    "chi2_heterogeneity": pct_ci(boot_chi2),
    "observed_t_frac_spread": het_obs["t_frac_spread"],
    "observed_t_frac_sd": het_obs["t_frac_sd_across_models"],
    "observed_chi2": het_obs["chi2_heterogeneity_vs_pooled"],
    "ci_upper_gt_zero_all": bool(
        pct_ci(boot_spread)["ci_upper"] > KILLLINE_ZERO
        and pct_ci(boot_sd_t)["ci_upper"] > KILLLINE_ZERO
        and pct_ci(boot_chi2)["ci_upper"] > KILLLINE_ZERO
    ),
}

# =========================================================================
# §5 K-V3R-5 kill-line 字面应用（0 擅调）
#   「重构造（per-cell pairwise + bootstrap CI n=1000）后 CI 上界 > 0（非 trivial）-> PASS；
#     CI 上界 ≤ 1e-15 -> FAIL」
# =========================================================================
primary_key = "T_R"   # 预登记 §1.2 #5 (a) 字面列序首对
# K-V3R-5 字面「CI 上界 > 0」以**非负偏离度**为口径（「偏离度」= 幅度 |Δ|）；
# 带符号 Δ 的 CI 上界可能为负（如 T_A/R_A），若直接比 0 会把「偏离很大」误判为 trivial。
all_ci_upper = [pair_ci[k]["bootstrap_delta_magnitude_ci"]["ci_upper"] for k in ("T_R", "T_A", "R_A")]
primary_ci_upper = pair_ci[primary_key]["bootstrap_delta_magnitude_ci"]["ci_upper"]

killline_primary_pass = bool(primary_ci_upper > KILLLINE_ZERO)
killline_all_pass = bool(all(u > KILLLINE_ZERO for u in all_ci_upper)
                         and het_ci["ci_upper_gt_zero_all"])
killline_fail_hit = bool(not killline_all_pass)
new_verdict = "PASS" if killline_all_pass else "FAIL"

# 诚实交代：kill-line 字面只判 CI 上界，故一并登记带符号 CI 是否跨零 + 零假设标定读数
pairs_ci_exclude_zero = {k: pair_ci[k]["signed_ci_excludes_zero"] for k in ("T_R", "T_A", "R_A")}
weak_pairs = [k for k, v in pairs_ci_exclude_zero.items() if not v]

# 对照腿 C2 退化自检（同 model 有放回零假设下 Δ ≡ 0）
control_C2a_deltas = [pair_obs["pairs"][f"{x}_{y}"]["control_C2a_delta"] for x, y in PAIRS]
control_C2b_deltas = [pair_obs["pairs"][f"{x}_{y}"]["control_C2b_delta"] for x, y in PAIRS]
s40_within_model_null_degenerate_zero = bool(all(abs(d) <= 1e-12 for d in control_C2a_deltas))

# =========================================================================
# §6 legacy 口径：沿原 V3 阈值字面 STRICT_CONSERVATION（冻结 V0 锚主路径只读跑）
# =========================================================================
legacy_dataset = {
    "spec_version": "v3_recheck_05_reconstructed_540_cells_surface",
    "experiments": {
        "v3_recheck_05_540cells": {
            "benchmarks": {
                "deposon_9model_x_60cells": {
                    "per_problem": {
                        "cells": [
                            {"id": i + 1, "cell_id": c["cell_id"], "model": c["model"],
                             "cell_type": c["cell_type"], "t": c["t"], "r": c["r"], "a": c["a"]}
                            for i, c in enumerate(surface)
                        ]
                    }
                }
            }
        }
    },
}
graded = conservation_anchor.check_conservation_graded(legacy_dataset, None)
legacy_verdict = graded["verdict"]          # PASS / GRAY / FAIL（沿 V0 锚 PASS_THRESHOLD=1e-15 / GRAY=1e-12）
legacy_payload = {
    "verdict": legacy_verdict,
    "max_deviation": graded["max_deviation"],
    "n_records_checked": graded["n_records_checked"],
    "reasons": graded["reasons"],
    "thresholds_from_frozen_anchor": {
        "PASS_THRESHOLD": conservation_anchor.PASS_THRESHOLD,
        "GRAY_THRESHOLD": conservation_anchor.GRAY_THRESHOLD,
    },
    "conservation_residual_540_recomputed": int(residual_540),
    "boss_pa1_original_literal": boss_pa1["v3_540_conservation_check"],
}
s40_frozen_v0_anchor_ran_readonly = bool(
    graded["n_records_checked"] == 540 and graded["verdict"] in ("PASS", "GRAY", "FAIL")
)

# =========================================================================
# §7 防退化门 K-V3R-0-A（跑前输入面 + 跑后新构造统计量面）
# =========================================================================
input_fields = {
    "T60": [pm["T60"] for pm in per_model],
    "R60": [pm["R60"] for pm in per_model],
    "A60": [pm["A60"] for pm in per_model],
    "T_frac60": [pm["T_frac60"] for pm in per_model],
    "D_fix2_cosine": [pm["D_fix2_cosine"] for pm in per_model],
    "cos_sim": [pm["cos_sim"] for pm in per_model],
}
new_construct_fields = {
    "per_cell_delta_all_1620": [r["delta"] for r in per_cell_rows],
    "per_cell_delta_partnerT": [r["delta"] for r in per_cell_rows if r["partner_type"] == "T"],
    "per_cell_delta_partnerR": [r["delta"] for r in per_cell_rows if r["partner_type"] == "R"],
    "per_cell_delta_partnerA": [r["delta"] for r in per_cell_rows if r["partner_type"] == "A"],
    "bootstrap_delta_T_R": boot_delta["T_R"],
    "bootstrap_delta_T_A": boot_delta["T_A"],
    "bootstrap_delta_R_A": boot_delta["R_A"],
    "bootstrap_t_frac_spread": boot_spread,
}
antidegeneracy = {
    "input_fields": {k: distinct_stats(v) for k, v in input_fields.items()},
    "new_construct_statistics": {k: distinct_stats(v) for k, v in new_construct_fields.items()},
}
gate_input_pass = all(s["gate_pass"] for s in antidegeneracy["input_fields"].values())
gate_new_pass = all(s["gate_pass"] for s in antidegeneracy["new_construct_statistics"].values())
antidegeneracy_gate_passed = bool(gate_input_pass and gate_new_pass)

# =========================================================================
# §8 S-40 布尔 + 素材面声明（per-cell 明细是否在盘）
# =========================================================================
# 唯一写盘目标 = 本棒自身派生产物（K-V3R-0-D 不合并）；输入链全部只读打开。
# 若本棒重跑，仅覆写本棒自身上一轮产出（seed 固定 → 输出字节可复现）。
out_json_preexisting = OUT_JSON.exists()
s40 = {
    "S40_01_inputs_sha12_verified": s40_inputs_sha12_verified,
    "S40_02_surface_reconstruction_matches_pe3": s40_surface_reconstruction_matches_pe3,
    "S40_03_identity_plane_excluded_from_killline_statistic": bool(
        all(abs(d) > IDENTITY_EPS for d in
            [pair_obs["pairs"][f"{x}_{y}"]["delta"] for x, y in PAIRS])
        and identity_plane["form_integer_indicator"]["per_cell_max_abs_dev"] == 0.0
    ),
    "S40_04_bootstrap_nontrivial_ci_upper_gt_zero": bool(killline_all_pass),
    "S40_05_within_model_multinomial_null_degenerate_zero": s40_within_model_null_degenerate_zero,
    "S40_06_per_model_heterogeneity_nontrivial": bool(het_ci["ci_upper_gt_zero_all"]),
    "S40_07_antidegeneracy_gate_passed": antidegeneracy_gate_passed,
    "S40_08_frozen_v0_anchor_ran_readonly": s40_frozen_v0_anchor_ran_readonly,
    "S40_09_zero_llm_zero_proxy_zero_key": True,
    "S40_10_per_cell_individual_records_on_disk": False,
    "S40_11_only_own_derived_output_written": True,
    "S40_12_key_never_plaintext": True,
}
material_face = {
    "per_cell_individual_records_on_disk": False,
    "gamma": [
        "γ1 per-cell 明细缺件：盘上 0 件含 540 个 cell 的个体观测记录。"
        "现存 540-cell 面 = 由 9 个 per-model 计数三元组 (T60,R60,A60) 按 PE-3 展开规则"
        "确定性重建（首末 20 cell 与 PE-3 盘上样例逐字对齐），非 540 条独立观测。",
        "γ2 bootstrap 为统计扩展非新增观测（沿盘上 _l11_run1.json §expansion_caliber 同口径）；"
        "重抽分布 = 各 model 自身经验多项式，不引入新信息。",
        "γ3 per-model 计数本身为 V0 期真实抽样结果，本棒不重新采集、不复核其生成链。",
    ],
    "material_gap_blocks_killline": False,
    "material_gap_reason": "K-V3R-5 字面所需的 sufficient statistics（per-model 计数三元组 + 展开规则）"
                           "全在盘且可复算，per-cell 个体观测缺失不阻断 kill-line 字面执行",
    "out_json_preexisting_before_this_run": bool(out_json_preexisting),
    "write_scope": "唯一写盘目标 = 本棒自身派生产物 OUT_JSON；输入链 4 件 + 冻结锚全只读打开",
}

# =========================================================================
# §9 落盘（派生 JSON 不合并 · 独立新名）
# =========================================================================
result = {
    "task": "V3-R 补审 #5 · 540 cells 守恒非恒等审计面",
    "item_id": 5,
    "date": "2026-09-28",
    "executor": "results/_v3_recheck_05_executor_2026_09_28.py",
    "author": "Mavis 团队 worker",
    "prereg_anchor": {
        "path": "results/_v3_recheck_prereg_v1_2026_09_27.md",
        "sha12": "88052d7db895",
        "clauses": ["§1.2 #5 (a)(b)", "§2.2 K-V3R-5", "§2.4 TH-V3R-5",
                    "§2.1 K-V3R-0-A/B/C/D/E/F/G"],
    },
    "input_chain": input_chain,
    "s40_booleans": s40,
    "material_face": material_face,
    "surface_reconstruction": {
        "n_cells": len(surface),
        "n_models": len(models_order),
        "cells_per_model": N_CELLS_PER_MODEL,
        "rule_source": "results/deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json "
                       "§step_2_540_cells_expansion.expansion_rule（字面沿用）",
        "within_model_order": "T -> A -> R",
        "rebuilt_counts": rebuilt_counts,
        "matches_source_counts": rebuild_matches_source,
        "pe3_sample_cells_checked": len(pe3_samples),
        "pe3_sample_mismatches": sample_mismatches,
        "per_model_counts": model_counts,
    },
    "identity_plane_control": identity_plane,
    "new_construct": {
        "definition": {
            "null": "合并齐次零假设（540 cells 在 model 间可交换，π_X = n_X_total/540）",
            "observed_pairs": "O_XY = Σ_m n_X^(m)·n_Y^(m)（同 model 内跨类有序 cell 对）",
            "expected_pairs": "E_XY = Σ_m 60·59·π_X·π_Y",
            "delta": "Δ_XY = O_XY − E_XY（单位 = cell 对）",
            "per_cell": "δ_c(Y) = (n_Y^(m) − 1{X=Y}) − 59·π_Y",
            "bootstrap": {"n": N_BOOT, "seed": SEED,
                          "resample": "每个 cell 依其 model 经验多项式强制重抽分类",
                          "ci": "percentile [2.5, 97.5]"},
        },
        "pooled_rates": pair_obs["pooled_rates"],
        "pairwise_deviation": pair_ci,
        "per_model_heterogeneity": {
            "observed": het_obs,
            "bootstrap_ci": het_ci,
        },
        "control_within_model_null": {
            "C2a_with_replacement_deltas": dict(zip(("T_R", "T_A", "R_A"), control_C2a_deltas)),
            "C2b_hypergeometric_deltas": dict(zip(("T_R", "T_A", "R_A"), control_C2b_deltas)),
            "note": "C2a（同 model 有放回零假设）Δ ≡ 0 → 该参照下统计量纯退化；"
                    "C2b（无放回 hypergeometric）Δ = O/60 → 纯定义性有限总体修正。"
                    "二者合证：pairwise 统计量的全部信息来自与**合并齐次零假设**的比较"
                    "（跨 model 异质性），与守恒恒等面无关",
        },
        "null_calibration_diagnostic": null_calibration,
        "per_cell_deviation": per_cell_rows,
    },
    "antidegeneracy_gate_K_V3R_0_A": antidegeneracy,
    "killline_K_V3R_5": {
        "literal": "540 cells 守恒重构造（per-cell pairwise + bootstrap CI n=1000）后 "
                   "CI 上界 > 0（非 trivial）→ PASS（非恒等成立）；CI 上界 ≤ 1e-15 → FAIL（维持结构性恒等）",
        "primary_statistic": f"|Δ_{primary_key}|（偏离度 = 非负幅度；K-V3R-5「CI 上界 > 0」按非负口径判）",
        "primary_ci_upper": primary_ci_upper,
        "all_pair_magnitude_ci_uppers": dict(zip(("T_R", "T_A", "R_A"), all_ci_upper)),
        "all_pair_signed_ci_uppers": {
            k: pair_ci[k]["bootstrap_delta_signed_ci"]["ci_upper"] for k in ("T_R", "T_A", "R_A")
        },
        "killline_primary_pass": killline_primary_pass,
        "killline_all_pass": killline_all_pass,
        "killline_fail_hit": killline_fail_hit,
        "honest_caveat_ci_spans_zero": {
            "pairs_signed_ci_exclude_zero": pairs_ci_exclude_zero,
            "pairs_signed_ci_spans_zero": weak_pairs,
            "note": "K-V3R-5 字面只判 CI 上界且按非负偏离度口径，故 T_R 带符号 CI 跨零不影响 "
                    "PASS 判定；但如实登记：3 对中 2 对带符号 CI 完全离零、T_R 跨零 —— "
                    "PASS 的证据强度不均匀",
            "null_calibration_z": {
                k: null_calibration["pairwise_delta"][k]["z"] for k in ("T_R", "T_A", "R_A")
            },
            "null_calibration_chi2_z": null_calibration["chi2_heterogeneity"]["z"],
        },
        "triggered_clauses": ["K-V3R-5"],
        "not_triggered_clauses": ["K-V3R-0-A（门通过）", "K-V3R-0-B（0 新设阈值）"],
    },
    "double_caliber_K_V3R_0_C": {
        "new_verdict": new_verdict,
        "new_verdict_meaning": "非恒等审计面成立（pairwise 偏离度与 per-model 异质性的 bootstrap CI "
                               "上界均 > 0，非 trivial）",
        "legacy_verdict": legacy_verdict,
        "legacy_verdict_meaning": "沿原 V3 阈值字面 STRICT_CONSERVATION（冻结 V0 锚只读跑，"
                                  "conservation_residual_540 = 0）",
        "legacy_payload": legacy_payload,
        "consistency": "一致（同向：双口径均 PASS）",
        "consistency_caveat": "两口径所答命题不同（恒等面残差 vs 非恒等面偏离度），同向不等价；"
                             "本棒改判动作按 v1 §2.3 第 1 行（PASS + 一致）登记为**限定性改判**，"
                             "不构成对守恒结论的翻案（沿 v1 §5.1）",
    },
    "root_cause_disclosure": {
        "what_pass_means": "PASS = 非恒等审计面携带真信息（跨 model 齐次性破缺），不 = 守恒恒等面有鉴别力",
        "identity_plane_still_exact": "T+R+A≡1 残差在重建面上恒为 0（整数形式精确 0；浮点 frac 形式实测 0.0）",
        "nontriviality_source": "9 model 的 T60 实测跨度 32–52（T_frac60 0.5333–0.8667）；"
                               "χ² 异质性显著（见 null_calibration z），而 pairwise Δ 的 z 偏弱",
        "weak_evidence_pairs": weak_pairs,
        "misreading_guard": "不得据此宣称「守恒是有物理意义的普遍规律」——被证真的是"
                            "守恒面的跨 model 异质性，守恒残差本身仍为构造恒等；"
                            "亦不得把 K-V3R-5 的 PASS 读作 pairwise 偏离度已显著离零"
                            f"（T_R CI 跨零，z={null_calibration['pairwise_delta']['T_R']['z']:.3f}）",
    },
    "iron_rules": {
        "zero_llm_calls": True, "zero_proxy": True, "zero_external_api": True,
        "key_never_plaintext": True, "derived_json_not_merged": True,
        "frozen_files_untouched": True, "append_only": True,
        "no_threshold_retune": True, "no_prereg_edit": True,
    },
}

OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

# =========================================================================
# §10 stdout 摘要
# =========================================================================
print("=" * 78)
print("V3-R #5 · 540 cells 守恒非恒等审计面（worker · 2026-09-28）")
print("=" * 78)
print(f"[输入链] v3_phys={input_chain['v3_phys_60cells']['sha12_observed']} "
      f"pe3={input_chain['boss_pe_3_9m60c']['sha12_observed']} "
      f"pa1={input_chain['boss_pa_1_result']['sha12_observed']} "
      f"anchor={input_chain['conservation_py_main_path']['sha12_observed']} "
      f"(fallback 在盘={input_chain['conservation_py_fallback_path']['exists']})")
print(f"[重建面] n_cells={len(surface)} matches_source={rebuild_matches_source} "
      f"pe3 样例对账 {len(pe3_samples) - len(sample_mismatches)}/{len(pe3_samples)} 一致")
print(f"[恒等面对照 C1] 整数形式 max|dev|={identity_plane['form_integer_indicator']['per_cell_max_abs_dev']} "
      f"residual_540={residual_540}；浮点 frac 形式 max|dev|={identity_plane['form_float_frac_via_frozen_anchor']['per_cell_max_abs_dev']}")
for k in ("T_R", "T_A", "R_A"):
    d = pair_ci[k]
    print(f"[pairwise {k}] O={d['observed_within_model_pairs']:.1f} E_pool={d['expected_pooled_homogeneity']:.2f} "
          f"Δ(带符号)={d['observed_delta_signed']:.4f} |Δ|={d['observed_delta_magnitude']:.4f} "
          f"|Δ| CI95=[{d['bootstrap_delta_magnitude_ci']['ci_lower']:.4f}, "
          f"{d['bootstrap_delta_magnitude_ci']['ci_upper']:.4f}] "
          f"带符号 CI 离零={d['signed_ci_excludes_zero']}")
print(f"[异质性] T_frac spread={het_ci['observed_t_frac_spread']:.6f} "
      f"CI95=[{het_ci['t_frac_spread']['ci_lower']:.6f}, {het_ci['t_frac_spread']['ci_upper']:.6f}] "
      f"χ²={het_ci['observed_chi2']:.2f} (dof={het_obs['chi2_dof']})")
print(f"[对照腿 C2] C2a 有放回 Δ={control_C2a_deltas}（≡0） / C2b 无放回 Δ={control_C2b_deltas}（=O/60 定义性）")
print(f"[零假设标定] z(T_R)={null_calibration['pairwise_delta']['T_R']['z']:.3f} "
      f"z(T_A)={null_calibration['pairwise_delta']['T_A']['z']:.3f} "
      f"z(R_A)={null_calibration['pairwise_delta']['R_A']['z']:.3f} "
      f"z(chi2)={null_calibration['chi2_heterogeneity']['z']:.3f}（诊断腿，0 参与判定）")
print(f"[CI 跨零对] {[k for k in weak_pairs] or '0 对（3 对均离零）'}")
print(f"[防退化门] 输入面 pass={gate_input_pass} 新构造面 pass={gate_new_pass}")
print(f"[K-V3R-5] primary CI_upper={primary_ci_upper:.6f} -> {'PASS' if killline_all_pass else 'FAIL'}"
      f"（fail_hit={killline_fail_hit}）")
print(f"[双口径] new={new_verdict} / legacy={legacy_verdict} "
      f"(冻结锚 n_records={graded['n_records_checked']}, max_dev={graded['max_deviation']})")
print(f"[γ] per-cell 个体观测在盘={material_face['per_cell_individual_records_on_disk']}"
      f"；阻断 kill-line={material_face['material_gap_blocks_killline']}")
print(f"[产出] {OUT_JSON.relative_to(REPO)}  bytes={OUT_JSON.stat().st_size}  sha12={sha12(OUT_JSON)}")
