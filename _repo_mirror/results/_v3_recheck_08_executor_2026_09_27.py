#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V3-R 补审 #8 BOSS-PC-3 (A3 clipping) — executor (worker · 2026-09-27)

沿 results/_v3_recheck_prereg_v1_2026_09_27.md（SHA-12 88052d7db895）字面执行：
  - K-V3R-0-A 防退化门（n_distinct > 3 + std > 0，跑前对盘上素材面自证；本件素材面实测不达标
    -> 退化警报触发 -> 按 §3.2「不许带病开跑」判「不明」，仅跑构造自检，不作判定证据）
  - K-V3R-0-B 沿用阈值（0 新设阈值）
  - K-V3R-0-C 双口径（构造口径 verdict + 沿原 V3 阈值字面 verdict 并报）
  - K-V3R-0-D 派生 JSON 不合并（本件独立落盘 _v3_recheck_08_result_*.json）
  - K-V3R-0-E 0 LLM（纯 numpy / hashlib / json，0 网络 0 模型调用）
  - K-V3R-8 kill-line 字面：r2_delta_full_minus_clipped 至少一档 != 0.0 -> PASS；3 trial 仍 == 0 -> FAIL
  - TH-V3R-8（boss_pc_3 pre_registered_threshold 字面 + PI 派工单冻结扫描）：
      clip_r2_min ∈ {0.3, 0.5, 0.7}；n_full = [10,20,50,100,200,500,1000]；n_clipped = [20,50,100,200,500]
  - A3 语义沿 docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md §5 字面：去掉 N=10 与 N=1000 两端，
    看 R² 是否仍 > clip_r2_min（"幂律非端点驱动"）；R² 沿 spec §4.1 幂律 OLS 公式。

输入（全部只读）：
  - results/boss_pc_3_a3_clipping_2026_09_15.json（原 BOSS-PC-3）
  - results/deposon_v3_physical_opt_60cells_2026_09_11.json（原 JSON 自报 data_source）

S-40 布尔显式命名：`*_hit = True` 表示「触发 FAIL / 触发警报」；`*_pass = True` 表示「存活 / 合格」。
"""

import hashlib
import json
import os
import sys
from pathlib import Path

import numpy as np

CLIP_R2_MIN_GRID = [0.3, 0.5, 0.7]                                     # TH-V3R-8 派工单冻结扫描
N_FULL = [10, 20, 50, 100, 200, 500, 1000]                             # TH-V3R-8 字面
N_CLIPPED = [20, 50, 100, 200, 500]                                    # TH-V3R-8 字面（去两端）
TRIALS = [42, 137, 256]                                                # 沿原 BOSS-PC-3 三 trial seed
BOOTSTRAP_N = 1000
BOOTSTRAP_SEED = 42
SEED = 20260927


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
PREREG = REPO / "results/_v3_recheck_prereg_v1_2026_09_27.md"
OUT = REPO / "results/_v3_recheck_08_result_2026_09_27.json"

# 缺失件探测目标（沿原 JSON 字面 + prereg §0.2 字面）
MISSING_PROBES = [
    "results/v3x_pc_v0",
    "docs/V3X/P_C_V0_RESULTS_2026_09_09_mavis.md",
    "results/v3x_pc_v0/attack_pc_a3_clipping.py",
    "deposon_team/plugins/attack_pc_a3_clipping.py",
    "attack_pc_a3_clipping.py",
    "tools/scaling_probe.py",
]


def sha12(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:12]


def n_distinct(xs) -> int:
    return len(set(xs))


def stat_block(xs):
    a = np.asarray(xs, dtype=float)
    return {"n": int(a.size), "n_distinct": n_distinct([round(float(x), 12) for x in a]),
            "std": float(a.std(ddof=0)), "min": float(a.min()), "max": float(a.max()),
            "mean": float(a.mean())}


def powerlaw_r2(n_vals, p_vals):
    """沿 spec §3.3/§4.1 字面：log10(P) = beta*log10(N) + log10(A)，OLS，取 R²。"""
    x = np.log10(np.asarray(n_vals, dtype=float))
    y = np.log10(np.asarray(p_vals, dtype=float))
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    pred = A @ coef
    ss_res = float(((y - pred) ** 2).sum())
    ss_tot = float(((y - y.mean()) ** 2).sum())
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    return {"beta": float(coef[0]), "log10_A": float(coef[1]), "r2": r2,
            "ss_res": ss_res, "ss_tot": ss_tot}


def clip_ladder(n_full, n_clip):
    return [n for n in n_full if n in set(n_clip)]


def main() -> int:
    pc3 = json.loads(SRC_PC3.read_text(encoding="utf-8"))
    s60 = json.loads(SRC_60.read_text(encoding="utf-8"))
    prereg_sha12 = sha12(PREREG.read_bytes())

    thr = pc3["pre_registered_threshold"]
    legacy_trials = pc3["trials"]

    # ---------- 素材面可得性探测（判定的决定性环节） ----------
    per_model = s60["P_C_distortion_bound_60cells"]["per_model"]
    # 盘上真实存在的「量级」= cell 计数档（每 model 30 / 60 cells，合计 540 cells）
    cell_count_levels = sorted({30, 60, 9 * 60})
    # 冻结阶梯的 N 是 spec §3.1 的「图族规模」，不是 cell 计数 —— 二者不可互换
    # （用 cell 计数顶替 N 即等于擅调 TH-V3R-8 阈值，K-V3R-0-B 禁止）
    real_N_levels_with_P_obs = []      # 盘上无任何 (N, P) 幂律观测对
    ladder_coverable = [n for n in N_FULL if n in set(real_N_levels_with_P_obs)]
    material_probe = {
        "declared_data_source": pc3["data_source"],
        "declared_data_source_has_N_ladder_field": bool(
            any("N_ladder" in k or k in ("P_obs", "N", "n_full", "scan")
                for k in json.dumps(s60).split('"'))),
        "N_semantics_in_spec": "spec §3.1 N = 图族规模（图张数）；P(N) = 跨该 N 档的命中率/失真率",
        "real_N_levels_with_P_observation": real_N_levels_with_P_obs,
        "N_levels_needed_by_TH_V3R_8": N_FULL,
        "N_levels_coverable": ladder_coverable,
        "n_distinct_real_N_levels": n_distinct(real_N_levels_with_P_obs),
        "cell_count_levels_available_in_declared_source": cell_count_levels,
        "n_distinct_cell_count_levels": n_distinct(cell_count_levels),
        "cell_counts_not_substitutable_for_N": True,
        "cell_count_substitution_rejected_because": "cell 计数（30/60/540）语义为分类 cell 数，"
                                                   "非 spec §3.1 图族规模；顶替即等于擅调 TH-V3R-8 阈值（违 K-V3R-0-B）",
        "per_model_counts_available": ["T30", "R30", "A30", "T60", "R60", "A60"],
        "max_cells_available": 9 * 60,
        "missing_artifacts_probe": [
            {"path": p, "exists": (REPO / p).exists()} for p in MISSING_PROBES],
        "checked_and_rejected_alternatives": [
            {"path": "results/deposon_benchmark_v1_4_gsm8k_details.json",
             "reason": "含 N 键 {10,20,50,100}，但非 P-C 两相结构命中率/失真率序列，且缺 200/500/1000 三档"},
            {"path": "results/deposon_gsm8k_stratified.json §per_question_steps",
             "reason": "N 键 {10,20,50,100} 为步数分布，非 P(N) 幂律观测序列，缺 3 档"},
        ],
    }
    # K-V3R-0-A 退化门（素材面）
    degen_alarm_hit = bool(material_probe["n_distinct_real_N_levels"] <= 3)
    material_gate_pass = not degen_alarm_hit
    kill_line_decidable = material_gate_pass

    # ---------- 构造自检（synthetic fixture，仅验证执行器非退化；不作判定证据） ----------
    def synth_p_of_n(n_vals, seed, a=2.0, b=0.45, c=0.02, noise=0.05):
        rng = np.random.default_rng(seed)
        n = np.asarray(n_vals, float)
        p = a * np.power(n, -b) + c
        p = p * (1.0 + rng.normal(0.0, noise, size=n.shape))
        return p

    def a3_matrix(seed, n_full, n_clip, emulate_v3_noop=False):
        rows = []
        n_cl = n_full if emulate_v3_noop else clip_ladder(n_full, n_clip)
        p_full = synth_p_of_n(n_full, seed)
        p_cl = synth_p_of_n(n_cl, seed) if not emulate_v3_noop else p_full
        full = powerlaw_r2(n_full, p_full)
        clipd = powerlaw_r2(n_cl, p_cl)
        delta = full["r2"] - clipd["r2"]
        row = {"trial_seed": seed, "n_full": list(n_full), "n_clipped_used": list(n_cl),
               "r2_full": full["r2"], "r2_clipped": clipd["r2"],
               "r2_delta_full_minus_clipped": delta,
               "delta_is_zero": bool(abs(delta) < 1e-12)}
        for m in CLIP_R2_MIN_GRID:
            row["verdict_clip_r2_min_%s" % m] = (
                "PASS" if clipd["r2"] > m else "FAIL")
        return row

    matrix = [a3_matrix(s, N_FULL, N_CLIPPED) for s in TRIALS]
    no_op_emulation = [a3_matrix(s, N_FULL, N_CLIPPED, emulate_v3_noop=True) for s in TRIALS]

    # bootstrap (n=1000, seed=42) on delta —— 仅对 synthetic fixture
    rng = np.random.default_rng(BOOTSTRAP_SEED)
    boot = []
    for _ in range(BOOTSTRAP_N):
        f = powerlaw_r2(N_FULL, synth_p_of_n(N_FULL, int(rng.integers(0, 2 ** 31))))
        c = powerlaw_r2(clip_ladder(N_FULL, N_CLIPPED), synth_p_of_n(clip_ladder(N_FULL, N_CLIPPED), 7))
        boot.append(f["r2"] - c["r2"])
    boot = np.asarray(boot, float)

    selftest = {
        "label": "SYNTHETIC_CONSTRUCTION_SELF_TEST（构造自检夹具，非观测数据，不参与判定证据）",
        "synthetic_p_form": "P(N) = 2.0 * N^(-0.45) + 0.02，乘性高斯噪声 sigma=0.05（seeded）",
        "matrix": matrix,
        "no_op_emulation_of_v3_defect": no_op_emulation,
        "no_op_emulation_reproduces_zero_delta": bool(
            all(abs(r["r2_delta_full_minus_clipped"]) < 1e-12 for r in no_op_emulation)),
        "bootstrap": {
            "n": BOOTSTRAP_N, "seed": BOOTSTRAP_SEED,
            "delta_mean": float(boot.mean()), "delta_std": float(boot.std(ddof=0)),
            "delta_ci95": [float(np.percentile(boot, 2.5)), float(np.percentile(boot, 97.5))],
            "fraction_of_resamples_with_delta_zero": float((np.abs(boot) < 1e-12).mean()),
            "label": "SYNTHETIC_SELF_TEST",
        },
        "executor_non_degenerate": bool(
            all(abs(r["r2_delta_full_minus_clipped"]) >= 1e-12 for r in matrix)),
    }

    # ---------- 判定 ----------
    if kill_line_decidable:
        new_verdict = "PASS" if any(abs(r["r2_delta_full_minus_clipped"]) >= 1e-12 for r in matrix) else "FAIL"
        kill_line_pass = new_verdict == "PASS"
    else:
        new_verdict = "不明（K-V3R-0-A 退化警报：真实 N 档 n_distinct=%d <= 3，素材面不足，不许带病开跑）" \
                      % material_probe["n_distinct_real_N_levels"]
        kill_line_pass = False
    kill_line_hit = bool(degen_alarm_hit)

    # ---------- 沿原 V3 阈值字面算 verdict（双口径，K-V3R-0-C） ----------
    legacy_r2 = [t["r2_clipped_N5"] for t in legacy_trials]
    legacy_delta = [t["r2_delta_full_minus_clipped"] for t in legacy_trials]
    legacy_verdict = "%s（worst_clipped_r2 = %s < clip_r2_min = %s；3/3 trial 的 r2_delta_full_minus_clipped == 0.0）" \
                     % (pc3["verdict"], pc3["worst_clipped_r2"], thr["clip_r2_min"])
    consistent = False
    一致性 = "一致（改判成）" if consistent else "不一致（维持原标注 + 显式登记新构造 verdict）"

    result = {
        "schema": "v3_recheck_result/08_boss_pc_3_a3_clipping/1",
        "prereg": {"path": "results/_v3_recheck_prereg_v1_2026_09_27.md", "sha12": prereg_sha12,
                   "kill_line": "K-V3R-8",
                   "threshold": "TH-V3R-8 (clip_r2_min sweep 0.3/0.5/0.7; n_full=[10,20,50,100,200,500,1000]; "
                                "n_clipped=[20,50,100,200,500]) + spec §5 A3 语义"},
        "executor": "results/_v3_recheck_08_executor_2026_09_27.py",
        "date": "2026-09-27",
        "seed": SEED,
        "runtime": "0 LLM; numpy + hashlib + json only; no network; read-only inputs",
        "inputs": [
            {"path": "results/boss_pc_3_a3_clipping_2026_09_15.json",
             "sha12_measured": sha12(SRC_PC3.read_bytes())},
            {"path": "results/deposon_v3_physical_opt_60cells_2026_09_11.json",
             "sha12_measured": sha12(SRC_60.read_bytes())},
        ],
        "construct": {
            "A3_semantics": "沿 spec §5：去掉 N=10 与 N=1000 两端，看幂律拟合 R² 是否仍 > clip_r2_min",
            "r2_formula": "沿 spec §3.3 + §4.1：log10(P) = beta*log10(N) + log10(A)，OLS R² = 1 - SS_res/SS_tot",
            "clip_r2_min_grid": CLIP_R2_MIN_GRID,
            "n_full": N_FULL, "n_clipped": N_CLIPPED,
            "trials_seeds": TRIALS,
            "bootstrap": {"n": BOOTSTRAP_N, "seed": BOOTSTRAP_SEED},
        },
        "construct_degen_self_check": {
            "gate": "K-V3R-0-A: 素材面须有 n_distinct > 3 + std > 0 的真 N 档分布",
            "material_probe": material_probe,
            "degenerate_alarm_hit": degen_alarm_hit,
            "gate_pass": material_gate_pass,
            "disposition": "§3.2「任意不达 = 退化警报，改构造或判「不明」，不许带病开跑」"
                           + ("-> 已触发，判「不明」" if degen_alarm_hit else "-> 未触发"),
        },
        "construction_self_test": selftest,
        "legacy_dual_track": {
            "legacy_verdict": legacy_verdict,
            "legacy_verdict_field": pc3["verdict"],
            "legacy_worst_clipped_r2": pc3["worst_clipped_r2"],
            "legacy_clip_r2_min": thr["clip_r2_min"],
            "legacy_n_full": thr["n_full"], "legacy_n_clipped": thr["n_clipped"],
            "legacy_r2_clipped_trials": legacy_r2,
            "legacy_delta_trials": legacy_delta,
            "legacy_delta_all_zero": bool(all(d == 0.0 for d in legacy_delta)),
            "provenance_gap": "原 JSON 自报 data_source = %s，该件不含任何 N 阶梯字段；"
                              "原 r2_full_N7 / r2_clipped_N5 数值（%s）无法从自报源复算；"
                              "原始执行器 %s 在盘上不存在。"
                              % (pc3["data_source"],
                                 [t["r2_full_N7"] for t in legacy_trials],
                                 "deposon_team/plugins/attack_pc_a3_clipping.py"),
        },
        "verdict": {
            "new_verdict": new_verdict,
            "kill_line_decidable": kill_line_decidable,
            "kill_line_pass": kill_line_pass,
            "kill_line_hit": kill_line_hit,
            "legacy_verdict": legacy_verdict,
            "一致性": 一致性,
            "gamma": "素材面不足：真实 P(N) 7 档序列与原始 A3 执行器双缺件，"
                     "K-V3R-8 判死线不可判（既非 PASS 亦非 FAIL）",
            "改判档位": "§2.3 第 4 行（不明）→ 维持原 V3 标注不动 + 显式登记 γ + 归「V4 收尾整理」待拍板桶",
        },
        "iron_rules": {
            "0_LLM": True, "no_proxy": True, "no_key_in_prompt_json_disk": True,
            "read_only_inputs": True, "derived_json_not_merged": True,
            "synthetic_self_test_labeled_not_evidence": True,
            "v3_original_report_bytes_untouched": True,
        },
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("[#08] written:", OUT.relative_to(REPO))
    print("[#08] material gate: n_distinct_real_N_levels=%d degen_alarm_hit=%s decidable=%s"
          % (material_probe["n_distinct_real_N_levels"], degen_alarm_hit, kill_line_decidable))
    print("[#08] new_verdict:", new_verdict)
    print("[#08] self-test executor_non_degenerate=%s no_op_emulation_reproduces_zero=%s"
          % (selftest["executor_non_degenerate"], selftest["no_op_emulation_reproduces_zero_delta"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
