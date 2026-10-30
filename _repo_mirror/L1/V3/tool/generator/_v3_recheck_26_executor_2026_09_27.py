#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V3-R 补审 #26 P-J convergence basin — executor (worker · 2026-09-27)

沿 results/_v3_recheck_prereg_v1_2026_09_27.md（SHA-12 88052d7db895）字面执行：
  - K-V3R-0-A 防退化门（n_distinct > 3 + std > 0，跑前对盘上输入字段自证；另设 cap 伪影门）
  - K-V3R-0-B 沿用阈值（0 新设判定阈值）
  - K-V3R-0-C 双口径（新构造 verdict + 沿原 V3 阈值字面 verdict 并报）
  - K-V3R-0-D 派生 JSON 不合并（本件独立落盘 _v3_recheck_26_result_*.json）
  - K-V3R-0-E 0 LLM（纯 numpy / hashlib / json，0 网络 0 模型调用）
  - K-V3R-26 kill-line 字面：convergence_rate n_distinct > 3 + std > 0 -> PASS；仍 n_distinct <= 1 -> FAIL
  - TH-V3R-26（PI 2026-09-27 派工单冻结形式）：convergence_rate = n_iter / n_budget

输入（全部只读）：
  - results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json
  - results/deposon_v3_physical_opt_60cells_2026_09_11.json

S-40 布尔显式命名：`*_hit = True` 表示「触发 FAIL / 触发警报」；`*_pass = True` 表示「存活 / 合格」。
"""

import hashlib
import json
import os
import sys
from pathlib import Path

import numpy as np

# ---- 构造常量（沿派工单冻结 / V3 既有字面，0 新设判定阈值）----
SEED = 20260927
N_BUDGET = 100        # TH-V3R-26 派工单冻结：+-0.05 抖动 100 次（perturbation budget）
JITTER = 0.05         # 同上
N_CELLS = 60          # V3 既有字面：9 model x 60 cells
MAX_STEP = N_CELLS    # 离散重分配过程步数上限（<= 60 必收敛，非判定阈值）
CLASSES = ("T", "R", "A")

# 敏感性网格：重分配优先级规则（唯一实现自由度，0 阈值）
PRIORITIES = ("surplus_first", "class_order_TRA", "class_order_ART")


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
SRC_PJ = REPO / "results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json"
SRC_60 = REPO / "results/deposon_v3_physical_opt_60cells_2026_09_11.json"
PREREG = REPO / "results/_v3_recheck_prereg_v1_2026_09_27.md"
OUT = REPO / "results/_v3_recheck_26_result_2026_09_27.json"


def sha12(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:12]


def n_distinct(xs) -> int:
    return len(set(round(float(x), 12) for x in xs))


def stat_block(xs):
    a = np.asarray(xs, dtype=float)
    return {
        "n": int(a.size),
        "n_distinct": n_distinct(a),
        "std": float(a.std(ddof=0)),
        "min": float(a.min()),
        "max": float(a.max()),
        "mean": float(a.mean()),
        "distinct_values": sorted(set(round(float(x), 6) for x in a)),
    }


def redistribute_n_iter(t0: int, r0: int, a0: int, t_target: int, priority: str) -> int:
    """离散 cell 重分配过程：每步把 1 个 cell 从盈余最大的类移到亏缺最大的类，
    直到 T 类 cell 数 == t_target。返回真实迭代步数 n_iter。

    过程在 <= 60 步内必然到达目标（整数三元组和恒为 60，t 单调朝 t_target 移动），
    故 n_iter 恒为真迭代步数，不受上限伪影污染。
    """
    t, r, a = int(t0), int(r0), int(a0)
    rest = N_CELLS - int(t_target)
    denom = r0 + a0
    if denom == 0:
        r_target, a_target = rest, 0
    else:
        r_target = int(round(rest * r0 / denom))
        a_target = rest - r_target
    tgt = {"T": int(t_target), "R": r_target, "A": a_target}
    for step in range(1, MAX_STEP + 1):
        cur = {"T": t, "R": r, "A": a}
        if cur == tgt:
            return step - 1
        if priority == "surplus_first":
            src = max(CLASSES, key=lambda c: (cur[c] - tgt[c], -CLASSES.index(c)))
            dst = max((c for c in CLASSES if c != src),
                      key=lambda c: (tgt[c] - cur[c], -CLASSES.index(c)))
        else:
            order = ("T", "R", "A") if priority == "class_order_TRA" else ("A", "R", "T")
            src = next(c for c in order if cur[c] > tgt[c])
            dst = next(c for c in reversed(order) if cur[c] < tgt[c])
        if src == dst:
            return step - 1
        cur[src] -= 1
        cur[dst] += 1
        t, r, a = cur["T"], cur["R"], cur["A"]
    return MAX_STEP


def spearman(x, y):
    """秩相关（并列取平均秩）。任一侧零方差 -> None（无定义）。"""
    a, b = np.asarray(x, float), np.asarray(y, float)
    if a.std() == 0 or b.std() == 0:
        return None
    def rank(v):
        order = np.argsort(v, kind="mergesort")
        r = np.empty(len(v), float)
        s = v[order]
        i = 0
        while i < len(s):
            j = i
            while j + 1 < len(s) and s[j + 1] == s[i]:
                j += 1
            r[order[i:j + 1]] = (i + j) / 2.0 + 1.0
            i = j + 1
        return r
    ra, rb = rank(a), rank(b)
    ra, rb = ra - ra.mean(), rb - rb.mean()
    return float((ra * rb).sum() / np.sqrt((ra ** 2).sum() * (rb ** 2).sum()))


def main() -> int:
    pj = json.loads(SRC_PJ.read_text(encoding="utf-8"))
    s60 = json.loads(SRC_60.read_text(encoding="utf-8"))
    prereg_sha12 = sha12(PREREG.read_bytes())

    pj_all = pj["all_results"]
    s60_by_name = {m["model"]: m for m in s60["P_C_distortion_bound_60cells"]["per_model"]}
    models = list(pj_all["convergence_rates"].keys())
    t_frac60_pj = pj_all["T_frac60"]
    assert len(t_frac60_pj) == len(models) == 9, "P-J 输入不是 9 model"

    # ---------- 盘上输入字段：K-V3R-0-A 防退化门自证（跑前） ----------
    orig_cr = [pj_all["convergence_rates"][m] for m in models]
    cos_sim = [s60_by_name[m]["cos_sim"] for m in models]
    d_fix2 = [s60_by_name[m]["D_fix2_cosine"] for m in models]
    t30 = [s60_by_name[m]["T30"] for m in models]

    input_selfcheck = {
        "P-J_T_frac60 (盘上真实)": stat_block(t_frac60_pj),
        "60cells_cos_sim (盘上真实, 逐 model)": stat_block(cos_sim),
        "60cells_D_fix2_cosine (盘上真实, 逐 model)": stat_block(d_fix2),
        "60cells_T30 (盘上真实, 逐 model)": stat_block(t30),
        "P-J_convergence_rates_原构造 (对照, 应退化)": stat_block(orig_cr),
    }
    gate_fields = [k for k in input_selfcheck if "原构造" not in k]
    gate_pass = {k: bool(input_selfcheck[k]["n_distinct"] > 3 and input_selfcheck[k]["std"] > 0)
                 for k in gate_fields}
    degen_alarm_hit = not all(gate_pass.values())

    # ---------- 新构造：convergence_rate = n_iter / n_budget ----------
    def run_construct(priority: str):
        rng = np.random.default_rng(SEED)
        per_model, rates = [], []
        for idx, m in enumerate(models):
            rec = s60_by_name[m]
            t0, r0, a0 = int(rec["T60"]), int(rec["R60"]), int(rec["A60"])
            assert t0 + r0 + a0 == N_CELLS, "60-cell 守恒被破坏: %s" % m
            t60 = float(t_frac60_pj[idx])
            iters, tstars, x0s = [], [], []
            for _ in range(N_BUDGET):
                x0 = float(np.clip(t60 + rng.uniform(-JITTER, JITTER), 0.0, 1.0))
                t_star = int(round(x0 * N_CELLS))
                iters.append(redistribute_n_iter(t0, r0, a0, t_star, priority))
                tstars.append(t_star)
                x0s.append(x0)
            iters = np.asarray(iters, float)
            rate = float(iters.mean() / N_BUDGET)
            rates.append(rate)
            per_model.append({
                "model": m,
                "T_frac60_real": t60,
                "start_triple_TRA": [t0, r0, a0],
                "n_iter_mean": float(iters.mean()),
                "n_iter_min": float(iters.min()),
                "n_iter_max": float(iters.max()),
                "n_iter_distinct": n_distinct(iters),
                "convergence_rate": rate,
                "t_star_range": [int(min(tstars)), int(max(tstars))],
                "x0_perturb_mean": float(np.mean(x0s)),
                "hit_max_step_cap": bool((iters >= MAX_STEP).any()),
            })
        return per_model, rates

    per_model, rates = run_construct(PRIORITIES[0])
    cap_artifact_hit = any(p["hit_max_step_cap"] for p in per_model)
    assert not cap_artifact_hit, "cap 伪影门未过（存在触顶迭代），按 K-V3R-0-A 不许带病开跑"

    sens = {}
    for pr in PRIORITIES:
        _, r = run_construct(pr)
        sens[f"priority={pr}"] = stat_block(r)

    new_stat = stat_block(rates)
    n_dist, std = new_stat["n_distinct"], new_stat["std"]

    # ---------- K-V3R-26 判定（字面） ----------
    kill_line_pass = bool(n_dist > 3 and std > 0)
    kill_line_hit = bool(not kill_line_pass)
    new_verdict = "PASS" if kill_line_pass else "FAIL"
    new_claim_verdict = ("真判据成立：convergence_rate 分布非 trivial，原 9/9 ≡ 0.1 常量判据被证伪"
                         if kill_line_pass else "维持假证伪：重定义后仍 trivial")

    # ---------- 沿原 V3 阈值字面算 verdict（双口径，K-V3R-0-C） ----------
    orig_stat = stat_block(orig_cr)
    legacy_constant_degenerate = bool(orig_stat["n_distinct"] <= 1 and orig_stat["std"] == 0)
    legacy_rho = pj_all.get("spearman_rho_T_frac60_vs_convergence_rate")
    legacy_verdict = ("UNVERIFIED（判据退化：convergence_rate 9/9 == 0.1，n_distinct=1，std=0；"
                      "对常量 vector 的 Spearman 无定义，JSON 内记 rho=%s 系 spurious）" % legacy_rho)
    consistent = False  # 原口径 = UNVERIFIED/判据退化，与新构造 PASS 不同向
    一致性 = "一致（改判成）" if consistent else "不一致（维持原标注 + 显式登记新构造 verdict）"

    result = {
        "schema": "v3_recheck_result/26_p_j_convergence_basin/1",
        "prereg": {"path": "results/_v3_recheck_prereg_v1_2026_09_27.md", "sha12": prereg_sha12,
                   "kill_line": "K-V3R-26", "threshold": "TH-V3R-26 (convergence_rate = n_iter / n_budget)"},
        "executor": "results/_v3_recheck_26_executor_2026_09_27.py",
        "date": "2026-09-27",
        "seed": SEED,
        "runtime": "0 LLM; numpy + hashlib + json only; no network; read-only inputs",
        "inputs": [
            {"path": "results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json",
             "sha12_measured": sha12(SRC_PJ.read_bytes())},
            {"path": "results/deposon_v3_physical_opt_60cells_2026_09_11.json",
             "sha12_measured": sha12(SRC_60.read_bytes())},
        ],
        "construct": {
            "definition": "convergence_rate_m = mean_j(n_iter_j) / n_budget, j=1..100（TH-V3R-26 冻结形式）",
            "n_budget": N_BUDGET,
            "jitter": "+-0.05 uniform on T_frac60 (clip to [0,1])，逐 model 100 次真实扰动",
            "dynamics": "离散 cell 重分配过程：60-cell 整数三元组 (T,R,A) 每步把 1 个 cell 从盈余最大的类移到亏缺最大的类，"
                        "直到命中目标三元组 (t_target, r_target, a_target)（R/A 按盘上真实 r0:a0 比例吸收 T 份额差额）；"
                        "步数即 n_iter（单调推进，<= 60 步必收敛，无上限伪影）",
            "initial_state": "逐 model 盘上真实 (T60,R60,A60)，来自 60cells P_C_distortion_bound_60cells.per_model",
            "priority_rule": PRIORITIES[0] + "（唯一实现自由度，附 3 档敏感性网格）",
            "max_step": MAX_STEP,
        },
        "construct_degen_self_check": {
            "gate": "K-V3R-0-A: n_distinct > 3 + std > 0 on every on-disk input field",
            "input_fields": input_selfcheck,
            "gate_per_field": gate_pass,
            "degenerate_alarm_hit": degen_alarm_hit,
            "gate_pass": not degen_alarm_hit,
            "cap_artifact_alarm_hit": cap_artifact_hit,
            "output_field": {"convergence_rate_new": new_stat},
            "contrast": {"original_convergence_rate": orig_stat},
        },
        "rejected_first_attempt": {
            "construct": "2 策略 replicator dynamics x <- x*f_T/(x*f_T+(1-x)*f_A), f_T=cos_sim_m, f_A=1.0",
            "cap_artifact_alarm_hit": True,
            "measured": "9 model 中 5 个（cos_sim≈1 者）n_iter 触 MAX_ITER=2000 顶 -> convergence_rate == 20.0",
            "root_cause": "replicator 映射在内点不动点处 |g'(x*)|=(f_T+f_A)^2/(4 f_T f_A) >= 1（AM-GM），为扩张映射，"
                          "f_T/f_A ≈ 1 时近似恒等 -> 收敛极慢或不动，迭代步数被上限支配",
            "disposition": "按 K-V3R-0-A「不许带病开跑」拒收，改用离散 cell 重分配过程重跑；本条如实登记，不参与判定",
        },
        "per_model": per_model,
        "sensitivity_priority_rule": sens,
        "legacy_dual_track": {
            "legacy_verdict": legacy_verdict,
            "legacy_constant_degenerate": legacy_constant_degenerate,
            "legacy_reported_spearman_rho": legacy_rho,
            "legacy_spearman_recomputed": spearman(t_frac60_pj, orig_cr),
            "new_spearman_recomputed": spearman(t_frac60_pj, rates),
            "note": "legacy 侧 rho 不可重算（y 为常量，无定义）；新构造侧 rho 为真秩相关。"
                    "两者量纲/构造不同，不可直接相减比较，仅作构造非退化证据。",
        },
        "verdict": {
            "new_verdict": new_verdict,
            "new_claim_verdict": new_claim_verdict,
            "legacy_verdict": legacy_verdict,
            "一致性": 一致性,
            "kill_line_pass": kill_line_pass,
            "kill_line_hit": kill_line_hit,
            "改判档位": ("§2.3 第 2 行（PASS + 不一致）→ 维持原 V3 标注不动 + 显式登记新构造 verdict + 归「不明」分支"
                         if kill_line_pass else "§2.3 第 3 行（FAIL = 原标注维持）→ 0 改判动作"),
        },
        "iron_rules": {
            "0_LLM": True, "no_proxy": True, "no_key_in_prompt_json_disk": True,
            "read_only_inputs": True, "derived_json_not_merged": True,
            "v3_original_report_bytes_untouched": True,
        },
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("[#26] written:", OUT.relative_to(REPO))
    print("[#26] n_distinct=%d std=%.6f -> %s (kill_line_pass=%s kill_line_hit=%s)" %
          (n_dist, std, new_verdict, kill_line_pass, kill_line_hit))
    print("[#26] degen gate_pass=%s cap_artifact_hit=%s" % (not degen_alarm_hit, cap_artifact_hit))
    print("[#26] rates:", [round(r, 4) for r in rates])
    return 0


if __name__ == "__main__":
    sys.exit(main())
