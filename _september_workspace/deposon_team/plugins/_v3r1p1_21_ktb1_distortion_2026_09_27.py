# -*- coding: utf-8 -*-
"""V3-R #21 · KT-B1 失真上界重评（执行棒，K-V3R-21 字面，三面并报 0 合并）。

来源纪律锚（只读，0 触动）：
  - results/_v3_recheck_prereg_v1p1_2026_09_27.md §1.2（量纲互斥声明）§2.1 K-V3R1P1-0-A/0-F/0-G
                                                  §2.2 K-V3R-21（三步 + 判死线 (a)(b)(c)）
                                                  §2.3 TH-V3R1P1-21-* / §2.4 提案 A·B·C / §3.2
  - results/_v3_n_recheck_llm_verdict_2026_09_27.md §三条实测现状

三面（强制并报，0 合并，K-V3R1P1-0-C）：
  面 1 恒等口径对照：`T+R+A ≡ 1` 守恒残差（对照留档，0 鉴别力）
  面 2 原 D(M,T) 口径：**通用基线侧**（仓外漂移版 3 BOSS 脚本只读取用复算），deposon 侧不可算
  面 3 非恒等 `D_dec` 决策轴（提案 B 冻结算式；逐 benchmark 落盘，0 跨 benchmark 合并）

量纲互斥硬声明：`D_dec` = 决策不一致率量纲；0.0004/0.0028/0.4634 = D(M,T) 失真上界量纲；
**二者不可并排比大小**；面 3 不得据此宣称 deposon 优于/不优于 OT·KD·LLMLingua。

0 LLM / 0 proxy / 0 key 读取（K-V3R1P1-0-E）。无墙钟时间戳 ⇒ 同输入重跑逐字节一致。
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import sys

REPO = r"D:/私人资料/deposon-repo"
EXT_ROOT = r"D:/私人资料/_non_upload_local_archive"
EXT_BOSS_DIR = os.path.join(EXT_ROOT, "scripts", "scripts", "kt_b1")
BOSS_DRIFT = {"B1_Sinkhorn_OT": "boss_b1_sinkhorn_ot.py",
              "B2_KD": "boss_b2_kd.py",
              "B3_LLMLingua": "boss_b3_llmlingua.py"}
ANCHOR_SHA12 = {"B1_Sinkhorn_OT": "19325960b8be",
                "B2_KD": "1781ea2f742d",
                "B3_LLMLingua": "c0b55e0385a4"}   # 锚版 SHA-12（源件登记，全仓 0 命中）
REPORTED_GENERIC = {"B1_Sinkhorn_OT": 0.0004, "B2_KD": 0.0028, "B3_LLMLingua": 0.4634}
REPRO_TOL = 0.05           # TH-V3R1P1-21-d（±5%）
CONS_TOL = 1e-6            # TH-V3R1P1-21-c
N_RESAMPLES = 10000        # TH-V3R1P1-21-e
SEEDS = (42, 123, 456)     # TH-V3R1P1-21-e
KT_B1_KILL_LINE = 0.95     # TH-V3R1P1-21-a
V19_REL = "results/deposon_v19_benchmark_fixes.json"
OUT_PATH = os.path.join(REPO, "results", "_v3_recheck_21_result_2026_09_27.json")

sys.path.insert(0, REPO)
import numpy as np  # noqa: E402


def sha12(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def nbytes(path: str) -> int:
    return os.path.getsize(path)


def load_drift_boss(name: str):
    """仓外漂移版 BOSS 脚本**只读取用**加载（K-V3R1P1-0-F/0-G）：0 复制入仓、0 改动。"""
    path = os.path.join(EXT_BOSS_DIR, BOSS_DRIFT[name])
    spec = importlib.util.spec_from_file_location(f"_drift_{name}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod, path


def stats(series) -> dict:
    s = [float(x) for x in series]
    arr = np.asarray(s, dtype=float)
    nd = int(len(set(s)))
    std = float(arr.std())
    return {"n": len(s), "n_distinct": nd, "std": std, "is_binary": bool(nd <= 2),
            "gate_non_degenerate": bool(nd > 3 and std > 0.0),
            "mean": float(arr.mean()) if len(s) else None}


def boot_ci(series, idx_matrix) -> dict:
    arr = np.asarray([float(x) for x in series], dtype=float)
    means = arr[idx_matrix].mean(axis=1)
    return {"mean_bootstrap": float(means.mean()),
            "ci95_lo": float(np.percentile(means, 2.5)),
            "ci95_hi": float(np.percentile(means, 97.5))}


def boss_files_manifest() -> dict:
    return {name: {"path": os.path.join(EXT_BOSS_DIR, fn),
                   "sha12": sha12(os.path.join(EXT_BOSS_DIR, fn)),
                   "bytes": nbytes(os.path.join(EXT_BOSS_DIR, fn)),
                   "anchor_sha12": ANCHOR_SHA12[name],
                   "drift": True,
                   "access": "read_only_external_archive"}
            for name, fn in BOSS_DRIFT.items()}


def compute_face2(v19: dict) -> dict:
    """面 2：通用基线侧 D(M,T) 复现（漂移版 3 BOSS 脚本只读取用）。

    复算序列逐字沿各脚本自身 main() 的调用序（0 改脚本、0 自创流程）：
      B1: load_v19_benchmark → scan_regularization → 取 reg = SINKHORN_REG(0.1)
      B2: load_v19_benchmark → sample_teacher_distribution → train_kd_student
          → compute_kd_distortion_upper_bound
      B3: load_v19_benchmark → build_prompts → compress_with_llmlingua
          → compute_llmlingua_distortion
    """
    boss_files = boss_files_manifest()
    b1, _p1 = load_drift_boss("B1_Sinkhorn_OT")
    b2, _p2 = load_drift_boss("B2_KD")
    b3, _p3 = load_drift_boss("B3_LLMLingua")
    v19_for_boss = json.loads(json.dumps(v19))  # 只读副本（脚本内 0 写入，仅防御性隔离）
    reg_scan = b1.scan_regularization(v19_for_boss)
    b1_val = reg_scan[b1.SINKHORN_REG]
    teacher = b2.sample_teacher_distribution(v19_for_boss)
    student = b2.train_kd_student(teacher)
    b2_val = b2.compute_kd_distortion_upper_bound(student, v19_for_boss)
    orig_prompts = b3.build_prompts(v19_for_boss)
    flat = [p for ps in orig_prompts for p in ps]
    comp_flat = b3.compress_with_llmlingua(flat,
                                           target_ratio=b3.LLMLINGUA_TARGET_COMPRESSION_RATIO)
    comp = []
    i = 0
    for ps in orig_prompts:
        comp.append(comp_flat[i:i + len(ps)])
        i += len(ps)
    b3_val = b3.compute_llmlingua_distortion(orig_prompts, comp, v19_for_boss)

    face2_items = []
    for name, val, thr, dep_ref, verdict_fn in (
            ("B1_Sinkhorn_OT", b1_val, b1.SINKHORN_DISTORTION_UB_THRESHOLD, 0.5,
             b1.boss_b1_verdict),
            ("B2_KD", b2_val, b2.KD_DISTORTION_UB_THRESHOLD, 0.5, b2.boss_b2_verdict),
            ("B3_LLMLingua", b3_val, b3.LLMLINGUA_DISTORTION_THRESHOLD, 0.05,
             b3.boss_b3_verdict)):
        rep = REPORTED_GENERIC[name]
        lo, hi = rep * (1 - REPRO_TOL), rep * (1 + REPRO_TOL)
        rep_txt = repr(rep)
        disp_decimals = len(rep_txt.split(".")[1]) if "." in rep_txt else 0
        disp_halfstep = 0.5 * (10.0 ** (-disp_decimals))
        abs_diff = abs(val - rep)
        face2_items.append({
            "boss": name, "implementation": "漂移版（回填件 ≠ 原件）",
            "recomputed_value": val, "reported_value": rep,
            "repro_tolerance": REPRO_TOL,
            "repro_window": [lo, hi],
            "repro_pass": bool(lo <= val <= hi),
            "repro_alert_hit": bool(not (lo <= val <= hi)),
            "rel_deviation": (abs(val - rep) / rep) if rep else None,
            "script_internal_threshold": thr,
            "script_internal_deposon_reference_placeholder": dep_ref,
            "script_verdict_with_own_placeholder": verdict_fn(val, dep_ref),
            "verdict_caveat": "脚本内部裁定用占位 deposon 值比较，仅登记 0 主张（占位 0.5/0.05）",
            "absolute_difference": abs_diff,
            "reported_value_display_decimals": disp_decimals,
            "display_halfstep": disp_halfstep,
            "abs_diff_within_display_halfstep": bool(abs_diff <= disp_halfstep),
            "tolerance_window_halfwidth": rep * REPRO_TOL,
            "precision_note": (f"报告值仅 {disp_decimals} 位小数显示 ⇒ ±5% 相对窗半宽 "
                               f"{rep * REPRO_TOL:.2e} 窄于显示粒度半步 {disp_halfstep:.2e}；"
                               "机械判超差如实登记，**0 擅改容差、0 改判**"),
        })
    return {
        "kou_jing": "原 D(M,T) 口径 · 通用基线侧（通用基线值 vs 报告值复现性检查）",
        "source": "仓外漂移版 3 BOSS 脚本（只读取用，0 复制入仓）+ v19 frozen 只读",
        "recompute_label": "以漂移版实现复算（K-V3R1P1-0-G）",
        "anchor_version_available": False,
        "anchor_version_note": ("锚版 SHA-12 全仓 0 命中 ⇒ 漂移差异内容不可核 ⇒ "
                                "0 归因、0 编造差异说明"),
        "boss_files": boss_files,
        "b1_reg_scan": {str(k): v for k, v in sorted(reg_scan.items())},
        "b1_records_actually_extracted": len(b1._extract_200_questions(v19_for_boss)),
        "b1_script_declared_n_questions": b1.N_QUESTIONS,
        "b1_record_count_note": ("漂移版 B1 实抽记录数 = 995（E9.3 两基准 × 5 臂 × 99~100）"
                                 "，与脚本 docstring/常量 N_QUESTIONS=200 不一致；"
                                 "**0 归因、0 编造差异说明**，仅事实登记"),
        "b1_selected_reg": b1.SINKHORN_REG,
        "b2_kd_hyperparams": {"T": b2.KD_TEMPERATURE, "alpha": b2.KD_ALPHA,
                              "lr": b2.KD_LEARNING_RATE, "epochs": b2.KD_EPOCHS,
                              "batch": b2.KD_BATCH_SIZE},
        "b3_target_compression_ratio": b3.LLMLINGUA_TARGET_COMPRESSION_RATIO,
        "items": face2_items,
        "n_within_tolerance": sum(1 for x in face2_items if x["repro_pass"]),
        "n_items": len(face2_items),
        "deposon_side": {
            "computable": False,
            "reason": ("tools/distortion_calculator.py 本仓 + 仓外按名全扫 0 命中；"
                       "核心理论输入 u*(a_t) 与理论界 L/U 未交付（bb7ca9838150 §3.5/§8/§9："
                       "理论界由王老师给定、不在 P-B 内自创）⇒ 逆向重建须自创理论 = 违 §9"),
            "proposal_A3_ruling": "不可行 + γ（提案 A-3，PI 已照案采纳）",
            "fallback_condition_A4": "PI 不允仓外只读或回填件跑不动 ⇒ 面 2 判不可算 + γ",
            "reverse_rebuild_attempted": False,
        },
    }


def main() -> int:
    with open(os.path.join(REPO, V19_REL), encoding="utf-8") as f:
        v19 = json.load(f)

    # ---- 0. 输入链核验（先核后用）----
    in_repo = {
        "prereg_v1p1": "results/_v3_recheck_prereg_v1p1_2026_09_27.md",
        "prereg_v1": "results/_v3_recheck_prereg_v1_2026_09_27.md",
        "verdict_3item": "results/_v3_n_recheck_llm_verdict_2026_09_27.md",
        "ktb1_data_prev": "results/_v3_n_ktb1_distortion_bound_data_2026_09_27.json",
        "v19_frozen": V19_REL,
        "conservation_py": "verifier/audit/conservation.py",
        "kt_b1_spec": "docs/V3X/KT_B1_SPEC_V0.1.md",
        "kt_b1_rework": "docs/V3X/KT_B1_REWORK_REPORT_2026_09_10.md",
        "p_b_spec": "docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md",
        "kt_anchor_bak": "verifier/handoff/KT_ABC1_anchors_sha256_12.root_session_11318B.bak_2026_09_23.json",
    }
    input_chain = {k: {"path": v, "sha12": sha12(os.path.join(REPO, v)),
                       "bytes": nbytes(os.path.join(REPO, v)), "access": "read_only"}
                  for k, v in in_repo.items()}
    boss_files = {name: {"path": os.path.join(EXT_BOSS_DIR, fn),
                        "sha12": sha12(os.path.join(EXT_BOSS_DIR, fn)),
                        "bytes": nbytes(os.path.join(EXT_BOSS_DIR, fn)),
                        "anchor_sha12": ANCHOR_SHA12[name],
                        "drift": True,
                        "access": "read_only_external_archive"}
                  for name, fn in BOSS_DRIFT.items()}

    # ---- 1. 面 1：恒等口径对照（复算 + 存储值对齐）----
    import importlib
    cons = importlib.import_module("verifier.audit.conservation")
    graded = cons.check_conservation_graded(v19, v19)
    stored = v19["physics_audit"]
    face1 = {
        "kou_jing": "恒等口径：T+R+A ≡ 1 守恒残差（对照留档）",
        "recomputed_max_deviation": graded.get("max_deviation"),
        "stored_t_plus_r_plus_a_max_deviation": stored["t_plus_r_plus_a_max_deviation"],
        "tolerance": CONS_TOL,
        "tolerance_source": "conservation.py physics_audit.tolerance (TH-V3R1P1-21-c)",
        "stored_vs_recomputed_match": bool(
            graded.get("max_deviation") == stored["t_plus_r_plus_a_max_deviation"]),
        "equals_ieee754_eps_2^-52": bool(
            graded.get("max_deviation") == 2.220446049250313e-16),
        "graded_verdict": graded.get("verdict"),
        "discriminating_power": ("构造恒等 ⇒ 该测法轴无鉴别力（承 #21 原结论，0 改判）"),
        "n_records_checked": graded.get("n_records_checked",
                                        len(graded.get("records", []) or []) or None),
    }

    # ---- 2. 面 2：通用基线侧 D(M,T) 复现（漂移版只读取用；B1 Sinkhorn 纯 Python 约 10 min
    #         ⇒ 置于面 3 之后调用，先跑廉价面以便失败早暴露）----
    face2 = compute_face2(v19)

    # ---- 3. 面 3：D_dec 决策轴（提案 B 冻结算式，逐 benchmark 落盘）----
    ex = v19["experiments"]
    REQUIRED_FIELDS = ("predicted", "trap_hit", "n_paths", "n_filtered")
    field_avail = {}
    for ename, e in ex.items():
        for bm, bv in e["benchmarks"].items():
            pp = bv.get("per_problem")
            groups = [("(flat_unnamed)", pp)] if isinstance(pp, list) else \
                     [(arm, arr) for arm, arr in pp.items()]
            for arm, arr in groups:
                field_avail[f"{ename}|{bm}|{arm}"] = {
                    "n": len(arr),
                    **{f: {"key_hits": sum(1 for r in arr if f in r),
                           "value_nonnull": sum(1 for r in arr if r.get(f) is not None)}
                       for f in REQUIRED_FIELDS},
                }

    face3_bench = {}
    e93 = ex["E9.3_high_couple_fix"]["benchmarks"]
    e95 = ex["E9.5_rule_baseline"]["benchmarks"]
    for bm in ("gsm8k", "strategyqa"):
        arms = {arm: {int(r["id"]): r for r in arr}
                for arm, arr in e93[bm]["per_problem"].items()}
        flat = e95[bm]["per_problem"]
        flat_arm = "rule_baseline"
        implied = sum(1 for r in flat if r["is_correct"]) / len(flat)
        arms[flat_arm] = {int(r["id"]): r for r in flat}
        # 四字段逐条命中（提案 B 可算性前置，benchmark 粒度）
        pred_field = "predicted" if "predicted" in flat[0] else "pred"
        hit = {f: sum(1 for ids in arms.values() for r in ids.values() if f in r)
               for f in REQUIRED_FIELDS}
        computable = all(hit[f] > 0 for f in REQUIRED_FIELDS)
        entry = {
            "benchmark": bm,
            "n_ids": len(next(iter(arms.values()))),
            "arms": sorted(arms),
            "flat_arm_identification": {
                "arm": flat_arm,
                "evidence_implied_accuracy": implied,
                "e95_rule_baseline_accuracy": e95[bm]["rule_baseline"]["accuracy"],
                "e95_unified_accuracy": e95[bm]["unified_llm_prior"]["accuracy"],
                "identified": bool(abs(implied - e95[bm]["rule_baseline"]["accuracy"]) < 1e-12),
                "unified_also_matches": bool(
                    abs(implied - e95[bm]["unified_llm_prior"]["accuracy"]) < 1e-12),
                "identification_unique": bool(
                    abs(implied - e95[bm]["rule_baseline"]["accuracy"]) < 1e-12
                    and abs(implied - e95[bm]["unified_llm_prior"]["accuracy"]) >= 1e-12),
                "identification_caveat": ("strategyqa 实测 rule_baseline 与 unified 精度完全相同 "
                                        "⇒ 臂归属证据不唯一；该 benchmark 已按 `predicted` "
                                        "0 命中判不可算 ⇒ 归属不参与任何读数"),
            },
            "prediction_field_name_observed": pred_field,
            "four_field_hits": hit,
            "computable": computable,
        }
        if not computable:
            entry["verdict"] = "INCOMPUTABLE_GAMMA"
            entry["gamma"] = [{"id": "G21-F3",
                               "trigger": f"四字段之一 0 命中（{pred_field}/predicted 面："
                                          f"predicted 键命中 = {hit['predicted']}）"
                                          f" ⇒ 按 benchmark 粒度判不可算",
                               "observation": (f"该 benchmark 预测字段实测名为 "
                                               f"'{pred_field}'；0 归因、0 用别名改判")}]
            face3_bench[bm] = entry
            continue

        common = sorted(set.intersection(*[set(a) for a in arms.values()]))
        N = len(common)
        idx_mats = {s: np.random.default_rng(s).integers(0, N, size=(N_RESAMPLES, N))
                    for s in SEEDS}

        d_dec, d_trap, d_flux = {}, {}, {}
        d_dec_diag, d_trap_diag, d_flux_diag = {}, {}, {}
        for a1 in arms:
            for a2 in arms:
                if a1 >= a2:
                    continue
                series = [1.0 if arms[a1][i].get("predicted", "MISSING") !=
                          arms[a2][i].get("predicted", "MISSING") else 0.0 for i in common]
                key = f"{a1}|{a2}"
                d_dec[key] = {"point": float(np.mean(series)), "N": N,
                              **{f"seed{s}": boot_ci(series, idx_mats[s]) for s in SEEDS}}
                d_dec_diag[key] = stats(series)
        for a1 in arms:
            series = [1.0 if bool(arms[a1][i].get("trap_hit")) else 0.0 for i in common]
            d_trap[a1] = {"point": float(np.mean(series)), "N": N,
                          **{f"seed{s}": boot_ci(series, idx_mats[s]) for s in SEEDS}}
            d_trap_diag[a1] = stats(series)
            if hit["n_paths"] > 0 and "n_paths" in arms[a1][common[0]] and \
                    "n_filtered" in arms[a1][common[0]]:
                series_f = [abs(arms[a1][i]["n_filtered"] - arms[a1][i]["n_paths"]) /
                            arms[a1][i]["n_paths"] if arms[a1][i]["n_paths"] else 0.0
                            for i in common]
                d_flux[a1] = {"point": float(np.mean(series_f)), "N": N,
                              **{f"seed{s}": boot_ci(series_f, idx_mats[s]) for s in SEEDS}}
                d_flux_diag[a1] = stats(series_f)
            else:
                d_flux[a1] = {"point": None, "N": N, "computable": False,
                              "reason": "n_paths/n_filtered 在该臂 0 命中"}
        arm_level_gap = sorted(set(arms) - set(d_flux_diag))

        # 防退化门（二值单列，PI 拍板③）：n_distinct > 3 + std > 0 只施于非二值序列
        nonbinary_pass_pairs = [k for k, v in d_dec_diag.items()
                                if not v["is_binary"] and v["gate_non_degenerate"]]
        nonbinary_pass_arms = [k for k, v in d_flux_diag.items()
                               if v["gate_non_degenerate"]]
        degen = {
            "rule": "n_distinct > 3 + std > 0（K-V3R1P1-0-A）",
            "binary_single_column": {  # 二值单列，不与 n_distinct>3 门混算
                "D_dec_per_pair_indicator": {k: {"n_distinct": v["n_distinct"],
                                                "std": v["std"], "is_binary": True}
                                             for k, v in d_dec_diag.items()},
                "D_trap_indicator": {k: {"n_distinct": v["n_distinct"],
                                         "std": v["std"], "is_binary": True}
                                     for k, v in d_trap_diag.items()},
                "note": "D_dec / D_trap 的 per-item 序列为 0/1 指示量 ⇒ 结构性二值，"
                        "n_distinct ≤ 2 恒成立；沿 PI 拍板③ 二值单列",
            },
            "non_binary_series_gate": {
                "D_flux_per_arm": {k: {"n_distinct": v["n_distinct"], "std": v["std"],
                                       "gate_non_degenerate": v["gate_non_degenerate"]}
                                   for k, v in d_flux_diag.items()},
                "D_dec_pairs_passing": nonbinary_pass_pairs,
                "D_flux_arms_passing": nonbinary_pass_arms,
            },
        }

        # (b) 面 3 有鉴别力：deposon 侧值在 ≥3 个臂对上 n_distinct > 3 且 std > 0
        n_pairs_total = len(d_dec_diag)
        b_qualifying = len(nonbinary_pass_pairs) + len(nonbinary_pass_arms)
        judgment_b = {
            "criterion": "≥3 个臂对上 n_distinct > 3 且 std > 0",
            "arm_pairs_total_D_dec": n_pairs_total,
            "arm_pairs_passing_non_binary_gate": len(nonbinary_pass_pairs),
            "arm_level_passing_D_flux": len(nonbinary_pass_arms),
            "qualifying_count": b_qualifying,
            "pass": bool(b_qualifying >= 3),
            "alert_hit": bool(b_qualifying < 3),
            "reading_registered": ("臂对级读数只有 D_dec（提案 B 字面 D_flux 为单臂指标）；"
                                   "D_dec per-item 序列结构性二值 ⇒ 二值单列后臂对级"
                                   "n_distinct>3 通过数 = 0；D_flux 仅 rule_baseline 单臂可算"),
        }

        # (c) 稳定性：3 seed 下臂间大小序 3/3 不变
        def order_by(seed_key):
            od = sorted(d_dec.items(), key=lambda kv: (kv[1][seed_key]["mean_bootstrap"],
                                                       kv[0]))
            return [k for k, _ in od]
        orders = {f"seed{s}": order_by(f"seed{s}") for s in SEEDS}
        point_order = [k for k, _ in sorted(d_dec.items(),
                                            key=lambda kv: (kv[1]["point"], kv[0]))]
        identical = len({tuple(v) for v in orders.values()}) == 1
        ent = sorted(d_dec)

        def _discordant(seed_a, seed_b):
            oa = {k: i for i, k in enumerate(orders[f"seed{seed_a}"])}
            ob = {k: i for i, k in enumerate(orders[f"seed{seed_b}"])}
            out = []
            for i in range(len(ent)):
                for j in range(i + 1, len(ent)):
                    x, y = ent[i], ent[j]
                    if (oa[x] < oa[y]) != (ob[x] < ob[y]):
                        out.append([x, y])
            return out
        d_42_123 = _discordant(42, 123)
        d_123_456 = _discordant(123, 456)
        d_42_456 = _discordant(42, 456)
        judgment_c = {
            "criterion": "3 seed（42/123/456）× 10k resamples 下臂间大小序 3/3 不变",
            "n_resamples": N_RESAMPLES, "seeds": list(SEEDS),
            "orders_by_seed": orders,
            "point_estimate_order": point_order,
            "orders_identical_3of3": bool(identical),
            "discordant_pairs": {"seed42_vs_seed123": d_42_123,
                                 "seed123_vs_seed456": d_123_456,
                                 "seed42_vs_seed456": d_42_456},
            "n_pairwise_comparisons": len(ent) * (len(ent) - 1) // 2,
            "n_agreements_all3seeds": (len(ent) * (len(ent) - 1) // 2
                                       - len({tuple(sorted(p)) for p in
                                              d_42_123 + d_123_456 + d_42_456})),
            "pass": bool(identical),
            "alert_hit": bool(not identical),
            "ci_overlap_note": ("面 3 各臂对 95% CI 宽度见 D_dec 条目；"
                                "序稳定 ≠ CI 互不重叠（0 跨面主张）"),
        }

        entry.update({
            "verdict": "COMPUTED",
            "D_dec": d_dec, "D_dec_diag": d_dec_diag,
            "D_trap": d_trap, "D_trap_diag": d_trap_diag,
            "D_flux": d_flux, "D_flux_diag": d_flux_diag,
            "D_flux_arm_level_gap": arm_level_gap,
            "construct_degen_self_check": degen,
            "judgment_b": judgment_b,
            "judgment_c": judgment_c,
            "predicted_none_records": {
                a: sum(1 for i in common if arms[a][i].get("predicted") is None)
                for a in sorted(arms)},
            "none_treatment": ("predicted 为 null 的 item 按字面参与 1[pred_a≠pred_b] 比较"
                               "（null 与数值互异）；0 归一化、0 剔除（剔除即私设）"),
        })
        face3_bench[bm] = entry

    face3 = {
        "kou_jing": "非恒等 D_dec 决策轴（提案 B 冻结算式；0 使用 T/R/A、0 使用 u*）",
        "definitions": {
            "D_dec": "D_dec(a,b) = (1/N) · Σ_i 1[pred_a(i) ≠ pred_b(i)]",
            "D_trap": "D_trap(a) = (1/N) · Σ_i 1[trap_hit(i) = True]",
            "D_flux": "D_flux(a) = (1/N) · Σ_i |n_filtered(i) − n_paths(i)| / n_paths(i)",
        },
        "bootstrap": {"n_resamples": N_RESAMPLES, "seeds": list(SEEDS),
                      "ci": "95% percentile", "shared_index_matrix_per_seed": True},
        "output_rule": "逐 benchmark 分别落盘（0 合并，沿 K-V3R1P1-0-D）",
        "field_availability_audit": field_avail,
        "per_benchmark": face3_bench,
    }

    # ---- 4. 判死线 (a)(b)(c) 机械落定 ----
    a_ok = face2["n_within_tolerance"] == face2["n_items"]
    per_bm_b = {bm: v.get("judgment_b", {}).get("pass")
                for bm, v in face3_bench.items()}
    per_bm_c = {bm: v.get("judgment_c", {}).get("pass")
                for bm, v in face3_bench.items()}
    computable_bms = [bm for bm, v in face3_bench.items() if v.get("computable")]
    b_ok = bool(computable_bms) and all(per_bm_b[bm] for bm in computable_bms)
    c_ok = bool(computable_bms) and all(per_bm_c[bm] for bm in computable_bms)
    all_ok = bool(a_ok and b_ok and c_ok)
    new_verdict = "DETERMINABLE" if all_ok else "REMAINS_UNKNOWN"

    gamma = [
        {"id": "G21-1", "trigger": "面 3 四字段之一 0 命中 ⇒ 该 benchmark 不可算",
         "status": "triggered_for_strategyqa",
         "detail": {"benchmark": "strategyqa", "field": "predicted",
                    "observed_field_name": face3_bench["strategyqa"]
                    ["prediction_field_name_observed"]}},
        {"id": "G21-2", "trigger": "n_paths/n_filtered 在 E9.3/E9.4 臂 0 命中 ⇒ D_flux 仅单臂可算",
         "status": "registered_as_arm_level_limit",
         "detail": {"arm_level_gap": face3_bench["gsm8k"]["D_flux_arm_level_gap"]}},
        {"id": "G21-3", "trigger": "deposon 侧 D(M,T) 逆向重建判不可行（提案 A-3）",
         "status": "triggered", "detail": face2["deposon_side"]},
        {"id": "G21-4", "trigger": "锚版 3 BOSS 脚本全仓 0 命中 ⇒ 漂移差异内容不可核",
         "status": "unverifiable_no_attribution"},
        {"id": "G21-5", "trigger": "D_dec per-item 序列结构性二值 ⇒ 防退化门 n_distinct>3 在臂对级不可达",
         "status": "triggered", "detail": judgment_b_summary(face3_bench)},
    ]

    out = {
        "task": "V3-R #21 KT-B1 失真上界重评（K-V3R-21，三面并报）",
        "date": "2026-09-27",
        "author": "Mavis 团队 worker",
        "prereg": "results/_v3_recheck_prereg_v1p1_2026_09_27.md",
        "kill_line": ("K-V3R-21：(a) 面 2 3/3 ±5% 一致 (b) 面 3 ≥3 臂对 n_distinct>3 且 std>0 "
                      "(c) 3 seed × 10k resamples 臂间大小序 3/3 不变；全满足 ⇒ 可判，"
                      "任一不满足 ⇒ 维持不明 + γ"),
        "conclusion_ceiling_frozen": ("分面结论；deposon 侧 D(M,T) 真值不可算 ⇒ 不得升级为"
                                      "「deposon 优于/不优于 OT·KD·LLMLingua」的跨面结论"),
        "dimension_exclusivity_declaration": (
            "D_dec = 决策不一致率量纲；0.0004/0.0028/0.4634 = D(M,T) 失真上界量纲；"
            "二者不可并排比大小（0 混算、0 跨面主张）"),
        "frozen_params": {
            "kt_b1_kill_line_0.95": KT_B1_KILL_LINE,
            "repro_tolerance": REPRO_TOL, "conservation_tolerance": CONS_TOL,
            "n_resamples": N_RESAMPLES, "seeds": list(SEEDS),
            "new_thresholds_introduced": 0,
        },
        "input_chain": input_chain,
        "external_readonly": {
            "external_archive": "D:/私人资料/_non_upload_local_archive/",
            "items": boss_files,
            "copied_into_repo": 0, "wrote_external": False,
            "declaration": "只读取用授权：0 复制入仓 / 0 写入 / 0 移出 / 0 删除 / 0 改 ACL",
        },
        "face_1_identity_control": face1,
        "face_2_generic_baseline": face2,
        "face_3_d_dec": face3,
        "judgment": {
            "a_face2_repro_3of3_within_5pct": {"pass": a_ok, "alert_hit": bool(not a_ok),
                                               "n_within": face2["n_within_tolerance"],
                                               "n_total": face2["n_items"]},
            "b_face3_discriminating": {"per_benchmark": per_bm_b, "pass": b_ok,
                                    "alert_hit": bool(not b_ok)},
            "c_face3_order_stability": {"per_benchmark": per_bm_c, "pass": c_ok,
                                      "alert_hit": bool(not c_ok)},
            "all_three_pass": all_ok,
            "any_alert_hit": bool(not all_ok),
        },
        "new_verdict": new_verdict,
        "legacy_verdict": "item_21 = 不明（占位已除，测法轴恒等 + 资产缺口双重根因）",
        "rejudge_tier_v1_4tier": (
            "PASS（可判）+ 一致 ⇒ 另立改判件，原标注 0 触动" if all_ok else
            "不明分支（判据未全满足 + γ）⇒ 维持原标注，显式登记 γ，归 V4 收尾整理待拍板桶"),
        "gamma_registry": gamma,
        "zero_touch_declaration": {
            "existing_files_modified": 0, "derived_json_merged_into_existing": False,
            "llm_calls": 0, "proxy": False, "key_reads": 0,
        },
        "determinism": "无墙钟时间戳；同输入重跑本 JSON 逐字节一致（重跑自证见汇报）",
    }
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=False)
    print(json.dumps({"out": OUT_PATH, "new_verdict": new_verdict,
                      "a": a_ok, "b": b_ok, "c": c_ok,
                      "face2": {x["boss"]: [x["recomputed_value"], x["reported_value"],
                                            x["repro_pass"]]
                                for x in face2["items"]},
                      "face1_max_dev": face1["recomputed_max_deviation"],
                      "face3_benchmarks": {bm: v.get("verdict") for bm, v
                                           in face3_bench.items()}},
                     ensure_ascii=False, indent=1))
    return 0


def judgment_b_summary(face3_bench) -> dict:
    out = {}
    for bm, v in face3_bench.items():
        if v.get("verdict") == "COMPUTED":
            out[bm] = v["judgment_b"]
    return out


if __name__ == "__main__":
    sys.exit(main())
