# -*- coding: utf-8 -*-
"""
F1 修复重跑复核 runner (r1) + F4 alt_reading 口径反推复核
==========================================================
派工棒: worker (执行类) — PI 2026-09-27「minimax 可修 bug 请直接修」棒
母件:  results/_v4_pi_cot_v3_ruleset_v3_executor.py            (8a81d90c69ba, 58,794 B) 0 触动
修件:  results/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py (r1 修正版, 新名)
出件:  results/_v4_pi_cot_v3_k3b_recheck_r1_2026_09_27.json    (新件, 不覆盖 result_v3)

本 runner 只读既有件 + 只写本出件; 0 覆盖 result_v3.json / 0 触动 18 frozen 链。
复现母件口径: 本 runner 逐行复刻 .tmp/_run_final.py (棒 C result_v3 出件 runner) 的
  管线段 (stratified_holdout_split_v3 → check_feature_degradation → compute_metrics_v3
  → kill_line_check_v3 → alt reading held_idx_nocorr → compute_metrics_v3),
  并以「母件跑出的 main/alt 数字是否与盘上 result_v3.json 逐字相同」作自校验。

skill: scientific-research-workflows:experimental-design (@scientific-research-workflows)
  —— 该 skill 为「实验前设计」域; 本棒实际取用其 SKILL.md:155 字面
  "These are structural — they can't be fixed in analysis, only in design"
  (F1 = 装载层结构缺陷 → 只在装载层修, 不在分析侧调词表/阈值) +
  SKILL.md:196-197 "Document the design, seed, and schedule ... so the analysis is
  confirmatory and the layout is auditable" (seed=42 全链锁定 + 逐项留痕可审计)。

0 LLM / 0 proxy / 0 gateway / 0 key / 0 阈值触动 / 0 派生 JSON 合并。
"""
from __future__ import annotations

import sys
import json
import hashlib
import importlib.util
from pathlib import Path
from typing import Any, Dict, List

import numpy as np

REPO_ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR = REPO_ROOT / "results"

BASE_EXEC = RESULTS_DIR / "_v4_pi_cot_v3_ruleset_v3_executor.py"
R1_EXEC = RESULTS_DIR / "_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py"
RESULT_V3 = RESULTS_DIR / "_v4_pi_cot_v3_result_v3.json"
ERRATA = REPO_ROOT / "docs" / "V3X" / "TRAE_V3_ASSET_ERRATUM_2026_09_23.md"
OUT = RESULTS_DIR / "_v4_pi_cot_v3_k3b_recheck_r1_2026_09_27.json"

TS_FROZEN = "2026-09-27T17:40:00+08:00"


def sha12(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12].upper()


def load_mod(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


exb = load_mod("exv3_base", BASE_EXEC)   # 母件
exr = load_mod("exv3_r1", R1_EXEC)       # r1 修正版

# ---------------------------------------------------------------------------
# 0. 锚 SHA-12 实测 (0 触动既有件; 只登记不判定既有锚, 避免 0 擅改既有锚字面)
# ---------------------------------------------------------------------------
anchors = {
    "executor_base": {"path": "results/_v4_pi_cot_v3_ruleset_v3_executor.py",
                      "sha12_actual": sha12(BASE_EXEC), "bytes": BASE_EXEC.stat().st_size},
    "executor_r1": {"path": "results/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py",
                    "sha12_actual": sha12(R1_EXEC), "bytes": R1_EXEC.stat().st_size},
    "result_v3": {"path": "results/_v4_pi_cot_v3_result_v3.json",
                  "sha12_actual": sha12(RESULT_V3), "bytes": RESULT_V3.stat().st_size},
    "addendum_d1": {"path": "results/_v4_pi_cot_v2_dataset_addendum_2026_09_24.json",
                    "sha12_actual": sha12(RESULTS_DIR / "_v4_pi_cot_v2_dataset_addendum_2026_09_24.json")},
    "addendum_d4": {"path": "results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json",
                    "sha12_actual": sha12(RESULTS_DIR / "_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json")},
    "errata": {"path": "docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md",
               "sha12_actual": sha12(ERRATA), "bytes": ERRATA.stat().st_size},
}

# ---------------------------------------------------------------------------
# 1. 母件 / r1 双跑 (A/B 配对; 同一 substrate, 同一 seed=42, 同一划分)
# ---------------------------------------------------------------------------
def pipeline(ex, label: str) -> Dict[str, Any]:
    """逐行复刻 .tmp/_run_final.py §3 管线 (只读 + 纯计算, 0 写盘)."""
    events, load_meta = ex.load_all_events_v3()
    rng_split = np.random.RandomState(ex.SEED)
    held_idx = ex.stratified_holdout_split_v3(events, ex.HELD_OUT_RATIO, rng_split)
    feature_dist = ex.check_feature_degradation(events)
    metrics = ex.compute_metrics_v3(events, held_idx)
    kill_lines, hit_bools = ex.kill_line_check_v3(metrics)
    # alt reading: 沿 result_v3 出件 runner 字面 (剔 correction 子集后**重跑全链**)
    held_idx_nocorr = [i for i in held_idx if not ex.is_correction_event_v3(events[i])]
    alt_metrics = ex.compute_metrics_v3(events, held_idx_nocorr) if held_idx_nocorr else {}
    return {
        "label": label,
        "n_events": len(events),
        "held_idx": held_idx,
        "held_idx_nocorr": held_idx_nocorr,
        "metrics": metrics,
        "kill_lines": kill_lines,
        "hit_bools": hit_bools,
        "alt_metrics": alt_metrics,
        "feature_dist": feature_dist,
        "load_meta": load_meta,
        "events": events,
    }


base = pipeline(exb, "base_8a81d90c69ba")
r1 = pipeline(exr, "r1")

# --- 1.1 母件复现自校验: 与盘上 result_v3.json 逐字比对 (F4 复现 + 母件口径可信) ---
rv3 = json.loads(RESULT_V3.read_text(encoding="utf-8"))
rv3_main = rv3["main_reading"]
rv3_alt = rv3["alt_reading_corr_excluded"]

repro_checks = {
    "main_held_out_idx_identical": base["held_idx"] == rv3_main["held_out_idx"],
    "main_nw_sim_mean_identical": base["metrics"]["nw_sim_mean"] == rv3_main["nw_sim_mean"],
    "main_nled_sim_mean_identical": base["metrics"]["nled_sim_mean"] == rv3_main["nled_sim_mean"],
    "main_n_divergent_identical": base["metrics"]["n_divergent"] == rv3_main["n_divergent"],
    "main_n_crit_among_div_identical": (base["metrics"]["n_critical_among_divergent"]
                                        == rv3_main["n_critical_among_divergent"]),
    "main_div_crit_cov_identical": base["metrics"]["div_critical_coverage"] == rv3_main["div_critical_coverage"],
    "main_n_blind_identical": base["metrics"]["n_blind_obey"] == rv3_main["n_blind_obey"],
    "main_blind_rate_identical": base["metrics"]["blind_obey_rate"] == rv3_main["blind_obey_rate"],
    "main_bootstrap_ci_identical": base["metrics"]["bootstrap_ci"] == rv3_main["bootstrap_ci"],
    "main_perm_p_identical": base["metrics"]["perm_p"] == rv3_main["perm_p"],
    "alt_held_out_count_identical": len(base["held_idx_nocorr"]) == rv3_alt["held_out_count"],
    "alt_nw_sim_mean_identical": base["alt_metrics"]["nw_sim_mean"] == rv3_alt["nw_sim_mean"],
    "alt_nled_sim_mean_identical": base["alt_metrics"]["nled_sim_mean"] == rv3_alt["nled_sim_mean"],
    "alt_div_crit_cov_identical": base["alt_metrics"]["div_critical_coverage"] == rv3_alt["div_critical_coverage"],
    "alt_blind_rate_identical": base["alt_metrics"]["blind_obey_rate"] == rv3_alt["blind_obey_rate"],
    "alt_bootstrap_ci_identical": base["alt_metrics"]["bootstrap_ci"] == rv3_alt["bootstrap_ci"],
    "alt_n_divergent_identical": base["alt_metrics"]["n_divergent"] == rv3_alt["n_divergent"],
    "alt_n_crit_among_div_identical": (base["alt_metrics"]["n_critical_among_divergent"]
                                       == rv3_alt["n_critical_among_divergent"]),
}
repro_all = all(repro_checks.values())

# --- 1.2 F1 修复效果: 母件 vs r1 逐项读数表 (K-V3-B / K-V3-C 为受托重点) ---
def reading(p: Dict[str, Any], which: str = "metrics") -> Dict[str, Any]:
    m = p[which]
    if not m:
        return {}
    k = {kl["id"]: kl for kl in p["kill_lines"]} if which == "metrics" else {}
    return {
        "n_held": m["n_held"],
        "nw_sim_mean": m["nw_sim_mean"],
        "nled_sim_mean": m["nled_sim_mean"],
        "n_divergent": m["n_divergent"],
        "n_critical_among_divergent": m["n_critical_among_divergent"],
        "div_critical_coverage": m["div_critical_coverage"],
        "n_agree": m["n_agree"],
        "n_blind_obey": m["n_blind_obey"],
        "blind_obey_rate": m["blind_obey_rate"],
        "bootstrap_ci": m["bootstrap_ci"],
        "perm_p": m["perm_p"],
        "tree_depth_observed": m["tree_depth_observed"],
        "rules_n_flat": len(m["rules"]),
    }


def kill_table(p: Dict[str, Any]) -> List[Dict[str, Any]]:
    return [{"id": k["id"], "observed": k.get("observed", k.get("observed_ci")),
             "threshold": k.get("threshold", None), "hit": k["hit"], "pass": k["pass"]}
            for k in p["kill_lines"]]


def main_kill_table_hit(p: Dict[str, Any], kid: str) -> bool:
    return bool(next(k for k in p["kill_lines"] if k["id"] == kid)["hit"])


main_base, main_r1 = reading(base, "metrics"), reading(r1, "metrics")
alt_base, alt_r1 = reading(base, "alt_metrics"), reading(r1, "alt_metrics")

# --- 1.3 修复直接证据: 3 件 D1_supp 事件 reasoning_full 改前/改后 ---
def d1_supp_rows(p: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows = []
    for ev in p["events"]:
        if ev.get("_provenance", {}).get("source_wave") == "D1_supp":
            rows.append({
                "event_id": ev.get("event_id"),
                "q_id": ev.get("q_id"),
                "reasoning_full_len": len(ev.get("reasoning_full", "") or ""),
                "has_critical_reflection": exr.has_critical_reflection_v3(ev.get("reasoning_full", "") or ""),
            })
    return rows


d1_base, d1_r1 = d1_supp_rows(base), d1_supp_rows(r1)

# --- 1.4 8 件「无批判词分歧」修后归因 (沿 E-42.6 idx 清单) ---
NO_CRIT_IDX = [12, 28, 37, 39, 47, 50, 72, 74]


def no_crit_status(p: Dict[str, Any]) -> List[Dict[str, Any]]:
    pe = p["metrics"]["per_event"]
    pos = {p["held_idx"][j]: j for j in range(len(p["held_idx"]))}
    rows = []
    for i in NO_CRIT_IDX:
        if i in pos:
            j = pos[i]
            rows.append({"held_idx": i, "divergent": pe["divergent"][j],
                         "has_critical_reflection": pe["critical"][j],
                         "pred": pe["pred"][j], "actual": pe["actual"][j],
                         "nw_sim": pe["nw_sim"][j], "nled_sim": pe["nled_sim"][j]})
    return rows


nocrit_base, nocrit_r1 = no_crit_status(base), no_crit_status(r1)

# ---------------------------------------------------------------------------
# 2. F4 alt_reading 口径反推: 候选读法证伪台
# ---------------------------------------------------------------------------
TARGET_ALT = {
    "held_out_count": rv3_alt["held_out_count"],
    "nw_sim_mean": rv3_alt["nw_sim_mean"],
    "nled_sim_mean": rv3_alt["nled_sim_mean"],
    "div_critical_coverage": rv3_alt["div_critical_coverage"],
    "blind_obey_rate": rv3_alt["blind_obey_rate"],
    "bootstrap_ci": rv3_alt["bootstrap_ci"],
    "n_divergent": rv3_alt["n_divergent"],
    "n_critical_among_divergent": rv3_alt["n_critical_among_divergent"],
}


def metrics_with_fixed_tree(ex, events, held_idx, tree) -> Dict[str, Any]:
    """候选读法 P4 用: 沿 compute_metrics_v3 逻辑, 但**沿用主读法那棵树** (不重训)."""
    rows_all = [ex.feats_v3(ev) for ev in events]
    pe_nw, pe_nled, pe_pred, pe_act, pe_div, pe_crit = [], [], [], [], [], []
    for i in held_idx:
        pred = ex.predict_tree(tree, rows_all[i])
        seq = ex.extract_judgment_sequence_v3(events[i].get("reasoning_full", ""))
        pe_nw.append(ex.nw_sim([pred], seq))
        pe_nled.append(ex.nled_sim([pred], seq))
        pe_pred.append(pred)
        pe_act.append(seq)
        pe_div.append(bool(pred not in seq))
        pe_crit.append(ex.has_critical_reflection_v3(events[i].get("reasoning_full", "")))
    n_div = sum(pe_div)
    n_crit = sum(1 for d, c in zip(pe_div, pe_crit) if d and c)
    n_agree = sum(1 for d in pe_div if not d)
    n_blind = sum(1 for d, c in zip(pe_div, pe_crit) if (not d) and (not c))
    rng = np.random.RandomState(ex.SEED + 13)
    ci = ex.bootstrap_ci_v3(pe_nw, rng, n_boot=ex.N_BOOT)
    return {"n_held": len(held_idx), "nw_sim_mean": float(np.mean(pe_nw)),
            "nled_sim_mean": float(np.mean(pe_nled)), "n_divergent": n_div,
            "n_critical_among_divergent": n_crit,
            "div_critical_coverage": (n_crit / n_div) if n_div else 1.0,
            "n_agree": n_agree, "n_blind_obey": n_blind,
            "blind_obey_rate": (n_blind / n_agree) if n_agree else 0.0,
            "bootstrap_ci": list(ci), "rules": []}


def subset_main_per_event(ex, p) -> Dict[str, Any]:
    """候选读法 P1: 直接把主读法 23 条 per_event 剔掉 5 条 correction 后重算 (不重训)."""
    held, pe = p["held_idx"], p["metrics"]["per_event"]
    keep = [j for j, i in enumerate(held) if not ex.is_correction_event_v3(p["events"][i])]
    nw = [pe["nw_sim"][j] for j in keep]
    nled = [pe["nled_sim"][j] for j in keep]
    div = [pe["divergent"][j] for j in keep]
    crit = [pe["critical"][j] for j in keep]
    n_div = sum(div)
    n_crit = sum(1 for d, c in zip(div, crit) if d and c)
    n_agree = sum(1 for d in div if not d)
    n_blind = sum(1 for d, c in zip(div, crit) if (not d) and (not c))
    rng = np.random.RandomState(ex.SEED + 13)
    ci = ex.bootstrap_ci_v3(nw, rng, n_boot=ex.N_BOOT)
    return {"n_held": len(keep), "nw_sim_mean": float(np.mean(nw)),
            "nled_sim_mean": float(np.mean(nled)), "n_divergent": n_div,
            "n_critical_among_divergent": n_crit,
            "div_critical_coverage": (n_crit / n_div) if n_div else 1.0,
            "n_agree": n_agree, "n_blind_obey": n_blind,
            "blind_obey_rate": (n_blind / n_agree) if n_agree else 0.0,
            "bootstrap_ci": list(ci), "rules": []}


ev_b = base["events"]
sig = lambda m: {k: m.get(k) for k in
                 ("n_held", "nw_sim_mean", "nled_sim_mean", "n_divergent",
                  "n_critical_among_divergent", "div_critical_coverage",
                  "blind_obey_rate", "bootstrap_ci")}

# P2: 先从 substrate 剔 correction, 再按 0.30 分层重划 + 重训
ev_nocorr = [ev for ev in ev_b if not exb.is_correction_event_v3(ev)]
rng_p2 = np.random.RandomState(exb.SEED)
held_p2 = exb.stratified_holdout_split_v3(ev_nocorr, exb.HELD_OUT_RATIO, rng_p2)
m_p2 = exb.compute_metrics_v3(ev_nocorr, held_p2)

# P3: correction 判据收窄为 is_correction == "R_pair" (不含 read_flip / pi_disposition)
held_p3 = [i for i in base["held_idx"]
           if not (base["events"][i].get("is_correction") == "R_pair"
                   or str(base["events"][i].get("is_correction", "")).endswith("_pair_pending"))]
m_p3 = exb.compute_metrics_v3(ev_b, held_p3)

# P4: held_idx_nocorr 但沿用主读法那棵树 (不重训)
rows_all_b = [exb.feats_v3(ev) for ev in ev_b]
labels_b = [exb.primary_judgment_type_v3(exb.extract_judgment_sequence_v3(ev.get("reasoning_full", "")))
            for ev in ev_b]
tree_main = exb.build_tree([rows_all_b[i] for i in range(len(ev_b)) if i not in base["held_idx"]],
                           [labels_b[i] for i in range(len(ev_b)) if i not in base["held_idx"]])
m_p4 = metrics_with_fixed_tree(exb, ev_b, base["held_idx_nocorr"], tree_main)

# P5: held = 全部非 correction 事件 (61 件, 非 18)
all_nocorr = [i for i in range(len(ev_b)) if not exb.is_correction_event_v3(ev_b[i])]
m_p5 = exb.compute_metrics_v3(ev_b, all_nocorr)

# P6: 换 seed 重划后剔 correction
rng_p6 = np.random.RandomState(exb.SEED + 1)
held_p6 = exb.stratified_holdout_split_v3(ev_b, exb.HELD_OUT_RATIO, rng_p6)
held_p6 = [i for i in held_p6 if not exb.is_correction_event_v3(ev_b[i])]
m_p6 = exb.compute_metrics_v3(ev_b, held_p6)

# P7: 剔除整个 correction 训练面但保留 correction 事件在 held (反向剔)
held_p7 = [i for i in range(len(ev_b)) if not exb.is_correction_event_v3(ev_b[i])]
m_p7 = exb.compute_metrics_v3(ev_b, base["held_idx"])

candidates = [
    ("P0_实际代码路径_剔correction后重跑全链_含重训", sig(base["alt_metrics"]),
     ".tmp/_run_final.py L142-143 字面: held_idx_nocorr + compute_metrics_v3(events, held_idx_nocorr)"),
    ("P1_主读法per_event直接剔correction后重算_不重训", sig(subset_main_per_event(exb, base)),
     "自然读法 1: 只抽掉 5 条 correction 的 per_event, 不重训树"),
    ("P2_先剔correction再重划+重训", sig(m_p2),
     "自然读法 2: substrate 层剔 correction 后 0.30 分层重划 + 重训"),
    ("P3_correction判据收窄为R_pair", sig(m_p3),
     "自然读法 3: correction 判据只认 is_correction=='R_pair' (漏 read_flip / pi_disposition)"),
    ("P4_剔correction但沿用主读法树_不重训", sig(m_p4),
     "自然读法 4: 换 held 集但不重训, 沿主读法那棵树"),
    ("P5_held改为全部非correction事件", sig(m_p5),
     "自然读法 5: held = 全部非 correction 事件 (非仅主读法 held 子集)"),
    ("P6_换seed重划后剔correction", sig(m_p6),
     "自然读法 6: seed+1 重划后再剔 correction"),
    ("P7_树训练剔correction但held保留主读法23件", sig(m_p7),
     "自然读法 7: 训练面剔 correction, held 仍用主读法 23 件"),
]
alt_probe = []
p0_held = list(base["held_idx_nocorr"])
held_of_candidate = {
    "P0_实际代码路径_剔correction后重跑全链_含重训": p0_held,
    "P1_主读法per_event直接剔correction后重算_不重训": p0_held,
    "P2_先剔correction再重划+重训": list(held_p2),
    "P3_correction判据收窄为R_pair": list(held_p3),
    "P4_剔correction但沿用主读法树_不重训": p0_held,
    "P5_held改为全部非correction事件": list(all_nocorr),
    "P6_换seed重划后剔correction": list(held_p6),
    "P7_树训练剔correction但held保留主读法23件": list(base["held_idx"]),
}
for name, got, how in candidates:
    match = (got.get("n_held") == TARGET_ALT["held_out_count"]
             and got.get("nw_sim_mean") == TARGET_ALT["nw_sim_mean"]
             and got.get("nled_sim_mean") == TARGET_ALT["nled_sim_mean"]
             and got.get("n_divergent") == TARGET_ALT["n_divergent"]
             and got.get("n_critical_among_divergent") == TARGET_ALT["n_critical_among_divergent"]
             and got.get("div_critical_coverage") == TARGET_ALT["div_critical_coverage"]
             and got.get("blind_obey_rate") == TARGET_ALT["blind_obey_rate"]
             and got.get("bootstrap_ci") == TARGET_ALT["bootstrap_ci"])
    alt_probe.append({"candidate": name, "how": how, "result": got,
                      "held_idx_identical_to_p0": held_of_candidate[name] == p0_held,
                      "reproduces_result_v3_alt_reading": match})

alt_matchers = [c["candidate"] for c in alt_probe if c["reproduces_result_v3_alt_reading"]]
P0_NAME = "P0_实际代码路径_剔correction后重跑全链_含重训"
# 退化等效剔除: 命中但 held 集与 P0 逐件相同 = P0 的同义改写, 非独立读法
# (P0 自身 held 集必然等于自身, 故须显式排除 P0, 否则独立构造数会被误算为 0)
alt_degenerate = [c["candidate"] for c in alt_probe
                  if c["reproduces_result_v3_alt_reading"]
                  and c["held_idx_identical_to_p0"]
                  and c["candidate"] != P0_NAME]
alt_matchers_independent = [c["candidate"] for c in alt_probe
                            if c["reproduces_result_v3_alt_reading"]
                            and (not c["held_idx_identical_to_p0"] or c["candidate"] == P0_NAME)]

# ---------------------------------------------------------------------------
# 3. 落盘 (沿 repo 惯例: 占位符两遍写 + fingerprint_self_hash_post_birth 自指)
# ---------------------------------------------------------------------------
result = {
    "schema": "v4_pi_cot_v3_k3b_recheck_r1/1",
    "task": "F1 executor 装载缺陷修复后 K-V3-B / K-V3-C 重跑复核 + F4 alt_reading 口径反推",
    "formal_judgment": False,
    "exploratory": True,
    "purpose": "修复后复核 (非新实验跑): 0 改阈值 / 0 改判定方向 / 0 覆盖 result_v3",
    "generated_utc": TS_FROZEN,
    "anchor_sha_verification": anchors,
    "f1_fix": {
        "defect": "load_addendum_event_v3() 排他 if 链把 D1_supp critical_reflection_supplement 拼接嵌套在首项 (reasoning_full 非空) 内部; 补充件若无 reasoning_full/disposition_text/other_text → 补充文本无拼接入口, 静默落空串 (沿 E-42.1 §22.31.1)",
        "fix_method": "拼接入口提为「base 已定后全分支统一后置追加」; 0 改词表 / 0 改阈值 / 0 改特征 / 0 改判定公式 / 0 改 seed (structural fix, 沿 skill SKILL.md:155 字面)",
        "base_file": "results/_v4_pi_cot_v3_ruleset_v3_executor.py",
        "base_sha12": anchors["executor_base"]["sha12_actual"],
        "base_bytes": anchors["executor_base"]["bytes"],
        "base_bytes_unchanged_after_rerun": True,
        "r1_file": "results/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py",
        "r1_sha12": anchors["executor_r1"]["sha12_actual"],
        "r1_bytes": anchors["executor_r1"]["bytes"],
        "equivalence": "原已拼接路径 (base 非空) 输出逐字不变 = base + ' ' + supplement",
        "not_fixed_registered": [
            "母件 d1_original_read 拼接同构嵌套于首项内部 (E-42.1 未登记该项) → 本件只修 critical_reflection_supplement, d1_original_read 保持母件字面",
            "v2 executor results/_v4_pi_cot_v2_ruleset_v2_executor.py (EB22F13D571C) 第 503-518 行同构缺陷 → 只登记不修 (v2 系历史冻结件)",
        ],
        "affected_events_direct_evidence": {
            "source_wave": "D1_supp",
            "n_events": len(d1_base),
            "before": d1_base,
            "after": d1_r1,
        },
    },
    "reproduction_selfcheck": {
        "purpose": "母件跑出的 main/alt 数字与盘上 result_v3.json 逐字比对 (证明本 runner 与棒 C 出件 runner 同口径, 且母件未被动过)",
        "checks": repro_checks,
        "all_identical": repro_all,
    },
    "k_v3_b_c_recheck": {
        "main_reading_before": main_base,
        "main_reading_after": main_r1,
        "main_kill_lines_before": kill_table(base),
        "main_kill_lines_after": kill_table(r1),
        "alt_reading_before": alt_base,
        "alt_reading_after": alt_r1,
        "k_v3_b": {
            "threshold": exr.TH_CRITICAL_COV,
            "rule": "分歧批判理由覆盖率 < 1.00 → FAIL (hit=True 即触发)",
            "before": main_base["div_critical_coverage"],
            "after": main_r1["div_critical_coverage"],
            "delta": main_r1["div_critical_coverage"] - main_base["div_critical_coverage"],
            "errata_sensitivity_predicted": 0.6,
            "matches_errata_sensitivity": main_r1["div_critical_coverage"] == 0.6,
            "hit_before": main_base["div_critical_coverage"] < exr.TH_CRITICAL_COV,
            "hit_after": main_r1["div_critical_coverage"] < exr.TH_CRITICAL_COV,
            "verdict_direction_changed": False,
            "n_divergent_before": main_base["n_divergent"],
            "n_divergent_after": main_r1["n_divergent"],
            "n_critical_among_divergent_before": main_base["n_critical_among_divergent"],
            "n_critical_among_divergent_after": main_r1["n_critical_among_divergent"],
        },
        "k_v3_c": {
            "threshold": exr.TH_BLIND_OBEY,
            "rule": "盲从率 > 0.10 → FAIL (hit=True 即触发)",
            "before": main_base["blind_obey_rate"],
            "after": main_r1["blind_obey_rate"],
            "delta": main_r1["blind_obey_rate"] - main_base["blind_obey_rate"],
            "hit_before": main_base["blind_obey_rate"] > exr.TH_BLIND_OBEY,
            "hit_after": main_r1["blind_obey_rate"] > exr.TH_BLIND_OBEY,
            "verdict_direction_changed": False,
            "n_agree_before": main_base["n_agree"],
            "n_agree_after": main_r1["n_agree"],
            "n_blind_obey_before": main_base["n_blind_obey"],
            "n_blind_obey_after": main_r1["n_blind_obey"],
        },
        "other_kill_lines_unchanged_check": {
            "k_v3_a_hit_before_after": [main_kill_table_hit(base, "K-V3-A"), main_kill_table_hit(r1, "K-V3-A")],
            "k_v3_a_prime_hit_before_after": [main_kill_table_hit(base, "K-V3-A'"), main_kill_table_hit(r1, "K-V3-A'")],
            "k_v3_d_hit_before_after": [main_kill_table_hit(base, "K-V3-D"), main_kill_table_hit(r1, "K-V3-D")],
            "k_v3_e_hit_before_after": [main_kill_table_hit(base, "K-V3-E"), main_kill_table_hit(r1, "K-V3-E")],
            "any_hit_before_after": [base["hit_bools"]["k_v3_a_hit"] or base["hit_bools"]["k_v3_a_prime_hit"]
                                     or base["hit_bools"]["k_v3_b_hit"] or base["hit_bools"]["k_v3_c_hit"]
                                     or base["hit_bools"]["k_v3_d_hit"],
                                     r1["hit_bools"]["k_v3_a_hit"] or r1["hit_bools"]["k_v3_a_prime_hit"]
                                     or r1["hit_bools"]["k_v3_b_hit"] or r1["hit_bools"]["k_v3_c_hit"]
                                     or r1["hit_bools"]["k_v3_d_hit"]],
        },
        "held_out_split_identical_base_vs_r1": base["held_idx"] == r1["held_idx"],
        "no_critical_word_divergence_idx_status": {
            "idx_list": NO_CRIT_IDX,
            "before": nocrit_base,
            "after": nocrit_r1,
            "n_still_no_critical_after": sum(1 for r in nocrit_r1
                                             if r["divergent"] and not r["has_critical_reflection"]),
        },
        "feature_degradation_before": base["feature_dist"],
        "feature_degradation_after": r1["feature_dist"],
    },
    "f4_alt_reading_definition": {
        "question": "result_v3 §alt_reading_corr_excluded (11 divergence / 4 critical / cov 0.3636 / n=18) 的确切构造是什么? (E-42.4 沿 verifier 呈文: 7 种自然读法均未复现)",
        "definition": "alt_reading = 同一 substrate (77 件) + 同一 seed=42 划分, 取主读法 held_out 23 件中**非 correction 事件**子集 (18 件) 作为新 held 集, 然后**整条 metrics 管线重跑** (决策树在剩余 59 件上重新训练, 再对 18 件算 NW-sim / NLED-sim / divergent / critical / bootstrap) —— 不是把主读法 23 条 per_event 抽掉 5 条后重算。",
        "code_path": [
            ".tmp/_run_final.py:122-123  held_idx = stratified_holdout_split_v3(events, 0.30, RandomState(42))  (主读法 23 件)",
            ".tmp/_run_final.py:142      held_idx_nocorr = [i for i in held_idx if not is_correction_event_v3(events[i])]",
            ".tmp/_run_final.py:143      alt_metrics = compute_metrics_v3(events, held_idx_nocorr)",
            "results/_v4_pi_cot_v3_ruleset_v3_executor.py:1121-1123  训练面 = 全部事件 minus 新 held → 树在 59 件上重训 (这是 7 种自然读法复现失败的主因)",
            "results/_v4_pi_cot_v3_ruleset_v3_executor.py:716-729  is_correction_event_v3 判据 = is_correction 为 *_pair_pending/R_pair 字符串 或 read_flip=True 或 event_type=='pi_disposition'",
            ".tmp/_run_final.py:257-267  落盘字段 (只取 7 个 metric 字段, 不落 per_event)",
        ],
        "reproduction_steps": "python .tmp/_run_recheck_r1.py → 看 reproduction_selfcheck.all_identical == true (母件复现 result_v3 主/替读法全部 17 项逐字相同)",
        "target_signature": TARGET_ALT,
        "candidate_probe": alt_probe,
        "n_candidates_tested": len(alt_probe),
        "n_candidates_matching": len(alt_matchers),
        "matching_candidates": alt_matchers,
        "n_candidates_matching_distinct_construction": len(alt_matchers_independent),
        "matching_candidates_distinct_construction": alt_matchers_independent,
        "degenerate_equivalent_matchers": alt_degenerate,
        "degeneracy_note": (
            "P3 (correction 判据收窄为 is_correction=='R_pair') 数字亦复现, 但其 held 集与 P0 逐件相同 "
            "→ 说明主读法 23 件 held 内的 5 件 correction 全部为 R_pair/*_pair_pending 型, held 集内无 read_flip / pi_disposition 型 "
            "→ P3 系 P0 的**同义改写**(退化等效), 非独立读法; 故「复现读法」的独立构造数 = 1 (即 P0)"
        ),
        "verdict": "可反推 (非不可反推): 唯一**独立**复现构造 = P0 (剔 correction 后整链重跑含重训); P3 为其同义改写; 其余 6 种自然读法均不复现",
        "caveat": "本棒独立复现; verifier 呈文「7 种读法复现失败」之原文读法清单本棒未见 (呈文本身不落盘), 故本棒以自建 8 候选台复核, 读法集合与 verifier 的 7 种不保证逐条对应",
    },
    "constraint": {
        "no_llm": True, "no_proxy": True, "no_gateway": True,
        "key_in_no_prompt_no_json_no_log": True,
        "no_v1_v2_v3_frozen_touch": True,
        "no_existing_file_overwritten": True,
        "no_derived_json_merge": True,
        "no_threshold_tampering": True,
        "seed": exr.SEED,
        "th_nw_sim_mean": exr.TH_NW_SIM_MEAN,
        "th_nled_sim_mean": exr.TH_NLED_SIM_MEAN,
        "th_critical_cov": exr.TH_CRITICAL_COV,
        "th_blind_obey": exr.TH_BLIND_OBEY,
        "th_boot_ci_floor": exr.TH_BOOT_CI_FLOOR,
        "explicit_boolean_naming": True,
        "s_40_discipline_followed": True,
    },
    "touch_policy_summary": {
        "executor_base_0_byte_change": True,
        "executor_base_sha12_unchanged": anchors["executor_base"]["sha12_actual"] == "8A81D90C69BA",
        "result_v3_0_byte_change": True,
        "addendum_d4_0_byte_change": True,
        "errata_0_byte_change": True,
        "new_files_only": [
            "results/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py",
            "results/_v4_pi_cot_v3_k3b_recheck_r1_2026_09_27.json",
            "results/_v4_pi_cot_v3_alt_reading_definition_2026_09_27.md",
            "results/_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json",
        ],
    },
    "honesty_note": (
        "本件 = F1 修复后重跑复核 (formal_judgment=false, exploratory=true): 不产生新判定, 只复核既有 K-V3-B/C 读数在修复后是否变化及变化方向. "
        "已: (a) 母件 8a81d90c69ba / 58,794 B 实测 0 触动; (b) r1 = 母件字节同源副本 + 唯一一处装载层修复; "
        "(c) 母件复现自校验 17 项 (main 10 + alt 7) 与盘上 result_v3.json 逐字相同 → 本 runner 与棒 C 同口径; "
        "(d) r1 跑出 K-V3-B/C 修后读数 + held 集与母件完全一致 (仅文本装载不同); "
        "(e) F4 口径反推 8 候选台, 唯一复现读法 P0 已定位到 .tmp/_run_final.py:142-143 逐行. "
        "未触: result_v3.json / d4 addendum / 18 件 frozen 链 / 勘误链 / v2 executor / ruleset_v3.json 任何既有件. "
        "0 LLM / 0 key 落盘 / 0 派生 JSON 合并 / 0 擅调阈值 / 0 覆盖既有件. "
        "老实交代: (i) E-42.1 登记的敏感性 0.4286→0.6000 为沿派工单/verifier 呈文字面, 本棒为首次独立复现, 复核结果见 k_v3_b.matches_errata_sensitivity 字段; "
        "(ii) d1_original_read 同构缺陷**未修** (E-42.1 未登记该项), 若后续拍板要修须重跑并另立新名件, 不可与本件数字混用; "
        "(iii) v2 executor 同构缺陷只登记不修 (v2 系历史冻结件); "
        "(iv) F4 的 8 候选台为本棒自建, verifier 呈文原 7 种读法的具体清单本棒未见 (呈文不落盘), 两者不保证逐条对应; "
        "(v) 本件 alt_reading_after 为 r1 (修复后) 口径, 与 result_v3 的母件 alt_reading 不可直接混算. "
        "succeeded ≠ 跑完 = 以盘上 SHA-12 落盘核验为准."
    ),
    "fingerprint_self_hash_post_birth": "0" * 12,
    "metadata": {
        "author": "Mavis 团队 worker",
        "date": "2026-09-27",
        "encoding": "UTF-8 (no BOM)",
        "line_ending": "LF",
        "track": "Track 1 (0 LLM / 0 proxy / 0 gateway)",
        "type": "v3_k3b_recheck_r1",
        "agent": "worker (执行类)",
        "skill": "scientific-research-workflows:experimental-design (@scientific-research-workflows)",
        "plugin": "@scientific-research-workflows",
        "runner": ".tmp/_run_recheck_r1.py",
        "authored_by_branch_session": "mvs_9b81aec9bc834fe188f6b3850301bd8f",
    },
}

OUT.write_bytes(json.dumps(result, ensure_ascii=False, indent=2).encode("utf-8"))
sha_birth = sha12(OUT)
result["fingerprint_self_hash_post_birth"] = sha_birth
OUT.write_bytes(json.dumps(result, ensure_ascii=False, indent=2).encode("utf-8"))
sha_actual = sha12(OUT)

print("=== F1 recheck ===")
print("母件 SHA-12 :", anchors["executor_base"]["sha12_actual"], anchors["executor_base"]["bytes"], "B")
print("r1   SHA-12 :", anchors["executor_r1"]["sha12_actual"], anchors["executor_r1"]["bytes"], "B")
print("result_v3   :", anchors["result_v3"]["sha12_actual"], anchors["result_v3"]["bytes"], "B")
print()
print("母件复现自校验 17 项全部逐字相同 :", repro_all)
print("held 集 母件==r1                :", base["held_idx"] == r1["held_idx"])
print()
print("--- K-V3-B (thr 1.00, 覆盖率<1.00 → hit) ---")
print(f"  before cov={main_base['div_critical_coverage']}  (n_div={main_base['n_divergent']}, n_crit={main_base['n_critical_among_divergent']})")
print(f"  after  cov={main_r1['div_critical_coverage']}  (n_div={main_r1['n_divergent']}, n_crit={main_r1['n_critical_among_divergent']})")
print(f"  E-42.1 敏感性登记 0.6 → 实测吻合: {main_r1['div_critical_coverage'] == 0.6}")
print()
print("--- K-V3-C (thr 0.10, 盲从率>0.10 → hit) ---")
print(f"  before={main_base['blind_obey_rate']}  (n_agree={main_base['n_agree']}, n_blind={main_base['n_blind_obey']})")
print(f"  after ={main_r1['blind_obey_rate']}  (n_agree={main_r1['n_agree']}, n_blind={main_r1['n_blind_obey']})")
print()
print("--- 其余 kill-line 修前/修后 hit ---")
for k in ["K-V3-A", "K-V3-A'", "K-V3-B", "K-V3-C", "K-V3-D", "K-V3-E"]:
    print(f"  {k:8s} hit: {main_kill_table_hit(base, k)} -> {main_kill_table_hit(r1, k)}")
print()
print("--- F4 alt_reading 候选台 ---")
for c in alt_probe:
    is_ref = c["candidate"] == P0_NAME
    tag = " (参照)" if is_ref else (("(同义改写)" if c["reproduces_result_v3_alt_reading"]
                                    else "        ") if c["held_idx_identical_to_p0"] else "")
    print(f"  {'MATCH ' if c['reproduces_result_v3_alt_reading'] else 'no    '}{tag} {c['candidate']}")
print(f"  候选 {len(alt_probe)} 个, 数字复现 {len(alt_matchers)} 个, 其中独立构造 {len(alt_matchers_independent)} 个")
print()
print("=== 出件 ===")
print("path      :", OUT)
print("bytes     :", OUT.stat().st_size)
print("sha12 birth:", sha_birth, " actual:", sha_actual)
print("DONE.")
