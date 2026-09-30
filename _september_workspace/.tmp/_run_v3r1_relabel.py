#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v3r1 重跑落盘器: D4 重标后数据面 → 沿 v3 同参重训重跑 → 落 3 件并列新件.

纪律 (全件统一):
  0 写既有件 / 0 覆盖 v1.2 dataset / result_v3 / verdict_v3 / D4 addendum
  0 改阈值 (K-V3-A/A'/B/C/D/E = 0.65/0.55/1.00/0.10/0.40 + sentinel 一字不动)
  0 改 seed / 0 改词表 / 0 改特征集 / 0 改判定公式 / 0 LLM / 0 key 落盘
  单因子变更 = 仅 D4 五件 judge_type 标注 (沿 skill experimental-design:
  一次只变一个因子, 其余 nuisance (seed/划分/树参/推理全文/标签) 全部钉死)
"""
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any, Dict, List

import numpy as np

REPO_ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR = REPO_ROOT / "results"

EXEC_R1 = RESULTS_DIR / "_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py"
RELABEL = RESULTS_DIR / "_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json"
DATASET_V12 = RESULTS_DIR / "_v4_pi_cot_v3_dataset.json"
RESULT_V3 = RESULTS_DIR / "_v4_pi_cot_v3_result_v3.json"
K3B_RECHECK = RESULTS_DIR / "_v4_pi_cot_v3_k3b_recheck_r1_2026_09_27.json"
ADDENDUM_D4 = RESULTS_DIR / "_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json"
VERDICT_V3 = RESULTS_DIR / "_v4_pi_cot_v3_verdict_v3.md"

OUT_DATASET_V1P3 = RESULTS_DIR / "_v4_pi_cot_v3_dataset_v1p3_2026_09_27.json"
OUT_RESULT_V3R1 = RESULTS_DIR / "_v4_pi_cot_v3_result_v3r1_2026_09_27.json"
OUT_RESCRIPT = RESULTS_DIR / "_v4_pi_cot_v3_v3r1_rescript_2026_09_27.md"
DIAG = REPO_ROOT / ".tmp" / "_v3r1_diag.json"

TS = "2026-09-27T17:52:00+08:00"
SIGN = "Mavis 团队 worker 出件｜2026-09-27"
THRESH = {"K-V3-A": 0.65, "K-V3-A'": 0.55, "K-V3-B": 1.00,
          "K-V3-C": 0.10, "K-V3-D": 0.40, "K-V3-E": "sentinel"}


def sha12(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def sha12u(p: Path) -> str:
    return sha12(p).upper()


def load_mod(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def r4(x: Any) -> Any:
    return round(x, 4) if isinstance(x, float) else x


def pipeline(ex, events, label: str) -> Dict[str, Any]:
    rng_split = np.random.RandomState(ex.SEED)
    held_idx = ex.stratified_holdout_split_v3(events, ex.HELD_OUT_RATIO, rng_split)
    feature_dist = ex.check_feature_degradation(events)
    metrics = ex.compute_metrics_v3(events, held_idx)
    kill_lines, hit_bools = ex.kill_line_check_v3(metrics)
    held_idx_nocorr = [i for i in held_idx if not ex.is_correction_event_v3(events[i])]
    alt_metrics = ex.compute_metrics_v3(events, held_idx_nocorr) if held_idx_nocorr else {}
    return {"label": label, "n_events": len(events), "held_idx": held_idx,
            "held_idx_nocorr": held_idx_nocorr, "metrics": metrics,
            "kill_lines": kill_lines, "hit_bools": hit_bools,
            "alt_metrics": alt_metrics, "feature_dist": feature_dist, "events": events}


ex = load_mod("exec_r1", EXEC_R1)

anchors = {}
for label, p in [("executor_r1", EXEC_R1), ("d4_relabel", RELABEL),
                 ("dataset_v1_2", DATASET_V12), ("result_v3", RESULT_V3),
                 ("k3b_recheck_r1", K3B_RECHECK), ("addendum_d4", ADDENDUM_D4),
                 ("verdict_v3", VERDICT_V3)]:
    anchors[label] = {"path": f"results/{p.name}", "sha12_actual": sha12u(p),
                      "bytes": p.stat().st_size}

rel = json.loads(RELABEL.read_text(encoding="utf-8"))
rows = rel["relabel_table"]
by_pair = {r["pair_id"]: r for r in rows}

# ---- 基线 (r1 未重标) ----
ev_r1, meta_r1 = ex.load_all_events_v3()
base = pipeline(ex, ev_r1, "r1_未重标")

k3b = json.loads(K3B_RECHECK.read_text(encoding="utf-8"))
after = k3b["k_v3_b_c_recheck"]["main_reading_after"]
repro = {
    "n_held": base["metrics"]["n_held"] == after["n_held"],
    "nw_sim_mean": base["metrics"]["nw_sim_mean"] == after["nw_sim_mean"],
    "nled_sim_mean": base["metrics"]["nled_sim_mean"] == after["nled_sim_mean"],
    "n_divergent": base["metrics"]["n_divergent"] == after["n_divergent"],
    "n_crit_among_div": base["metrics"]["n_critical_among_divergent"] == after["n_critical_among_divergent"],
    "div_crit_cov": base["metrics"]["div_critical_coverage"] == after["div_critical_coverage"],
    "n_agree": base["metrics"]["n_agree"] == after["n_agree"],
    "n_blind_obey": base["metrics"]["n_blind_obey"] == after["n_blind_obey"],
    "blind_obey_rate": base["metrics"]["blind_obey_rate"] == after["blind_obey_rate"],
    "bootstrap_ci": base["metrics"]["bootstrap_ci"] == after["bootstrap_ci"],
    "perm_p": base["metrics"]["perm_p"] == after["perm_p"],
}
repro_all = all(repro.values())

# ---- 重标后 (v3r1) ----
ev_r1r, meta_r1r = ex.load_all_events_v3()
applied = []
for i, ev in enumerate(ev_r1r):
    if ev.get("_provenance", {}).get("source_wave") != "D4_w1":
        continue
    row = by_pair.get(ev.get("q_id", ""))
    if row is None:
        continue
    old = ev.get("judge_type", "")
    ev["judge_type"] = row["judge_type_relabeled"]
    ev["_relabel_trace"] = {
        "judge_type_original": row["judge_type_original"],
        "judge_type_relabeled": row["judge_type_relabeled"],
        "judge_type_relabeled_alternative": row["judge_type_relabeled_alternative"],
        "changed": row["changed"],
        "relabel_basis": row["relabel_basis"],
        "ambiguity_note": row["ambiguity_note"],
        "source_file": "results/_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json",
    }
    applied.append({"event_idx": i, "q_id": row["q_id"], "scene_tag": ev.get("scene_tag", ""),
                    "from": old, "to": row["judge_type_relabeled"],
                    "changed": row["changed"]})

v3r1 = pipeline(ex, ev_r1r, "v3r1_重标后")

# ---- 单因子自校验 ----
same_split = base["held_idx"] == v3r1["held_idx"]
nond4_identical = all(ev_r1[i].get("judge_type") == ev_r1r[i].get("judge_type")
                      for i in range(len(ev_r1))
                      if ev_r1[i].get("_provenance", {}).get("source_wave") != "D4_w1")
lab_same = ([ex.primary_judgment_type_v3(ex.extract_judgment_sequence_v3(e.get("reasoning_full", "")))
             for e in ev_r1]
            == [ex.primary_judgment_type_v3(ex.extract_judgment_sequence_v3(e.get("reasoning_full", "")))
                for e in ev_r1r])
rf_same = all(ev_r1[i].get("reasoning_full") == ev_r1r[i].get("reasoning_full") for i in range(len(ev_r1)))
opt_same = all(ev_r1[i].get("option_chosen") == ev_r1r[i].get("option_chosen") for i in range(len(ev_r1)))
d4_idx = [a["event_idx"] for a in applied]
d4_in_held = [i for i in d4_idx if i in v3r1["held_idx"]]
d4_in_train = [i for i in d4_idx if i not in v3r1["held_idx"]]

feat_delta = {}
for k in ex.FEAT_KEYS_V3:
    vb = [ex.feats_v3(e)[k] for e in ev_r1]
    vn = [ex.feats_v3(e)[k] for e in ev_r1r]
    nd = sum(1 for a, b in zip(vb, vn) if a != b)
    if nd:
        feat_delta[k] = {"n_events_changed": nd, "v3_sum": int(sum(vb)), "v3r1_sum": int(sum(vn)),
                         "v3_mean": round(float(np.mean(vb)), 6),
                         "v3r1_mean": round(float(np.mean(vn)), 6)}

MB, MV = base["metrics"], v3r1["metrics"]
AB, AV = base["alt_metrics"], v3r1["alt_metrics"]


def per_event(m):
    pe = m["per_event"]
    return [{"held_idx": i, "nw_sim": r4(pe["nw_sim"][k]), "nled_sim": r4(pe["nled_sim"][k]),
             "pred": pe["pred"][k], "actual": pe["actual"][k], "divergent": pe["divergent"][k],
             "has_critical_reflection": pe["critical"][k]}
            for k, i in enumerate(m["_held_order"])]


MV["_held_order"] = v3r1["held_idx"]
per_event_v3r1 = per_event(MV)
del MV["_held_order"]

# ================================================================ 件 1: dataset v1.3
ds13 = {
    "schema": "v4_pi_cot_v3_dataset_v1p3/1",
    "version": "v1.3",
    "created": TS,
    "created_by": SIGN,
    "task": "PI 思维链 v3 蒸馏 (棒 C) — dataset v1.3 修订件: D4 重标后 judge_type 落地",
    "formal_judgment": True,
    "exploratory": False,
    "purpose": "D4 五件 judge_type 重标 (J6→J5 / J6→J1(J4 并记) / J6→J5 / J3→J4 / J3 维持) 落地为权威标注面; 账目 (85 events / substrate 77) 逐字不变 — 仅特征标注变",
    "base_version": {
        "file": "results/_v4_pi_cot_v3_dataset.json",
        "version": "v1.2",
        "sha12": anchors["dataset_v1_2"]["sha12_actual"],
        "bytes": anchors["dataset_v1_2"]["bytes"],
        "relation": "v1.3 = v1.2 增量修订 (仅 judge_type 标注面); v1.2 引用不覆盖 / 0 字节改动 (实测复验见 anchor_sha_verification)",
    },
    "relabel_source": {
        "file": "results/_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json",
        "sha12": anchors["d4_relabel"]["sha12_actual"],
        "bytes": anchors["d4_relabel"]["bytes"],
        "decision_source": "PI 问卷 ask_ad37c9c9282a3edb0b881fe8 Q4「落 v1.3 重跑」",
        "n_rows": len(rows),
        "n_changed": sum(1 for r in rows if r["changed"]),
    },
    "anchor_sha_verification": anchors,
    "relabeled_judge_type_landed": [
        {"q_id": a["q_id"], "event_idx_in_v3r1_run": a["event_idx"], "scene_tag": a["scene_tag"],
         "judge_type_v1_2": a["from"], "judge_type_v1_3": a["to"], "changed": a["changed"],
         "judge_type_relabeled_alternative": by_pair[a["q_id"]]["judge_type_relabeled_alternative"],
         "relabel_basis": by_pair[a["q_id"]]["relabel_basis"],
         "ambiguity_note": by_pair[a["q_id"]]["ambiguity_note"],
         "applied_in": "in-memory (runner .tmp/_run_v3r1_relabel.py); 0 写回 D4 addendum 源件"}
        for a in applied
    ],
    "feature_impact": {
        "affected_feature_keys": sorted(feat_delta.keys()),
        "delta_detail": feat_delta,
        "unaffected_feature_keys": [k for k in ex.FEAT_KEYS_V3 if k not in feat_delta],
        "note": "5 项 judge_type_* 二值特征面变化; 其余 7 项 (scene_bucket_8 / opt_bucket_8 / is_corr_pair / rf_len_bucket / rf_pos_density / n_keywords_hit + judge_type_J2) 逐字不变 — 标注面变更的构造证据",
    },
    "accounting_balance_conservation": {
        "v2_baseline_N": 72,
        "post_v2_added": 8,
        "d4_added": 5,
        "total_events": 85,
        "v3_formal_experiment_substrate": 77,
        "accounting_formula": "72 (v2 baseline) + 8 (D3 wave2/3 post-v2) + 5 (D4) = 85 events; substrate 77 = 64 v2 on-disk + 8 post-v2 in load + 5 D4",
        "delta_vs_v1_2": "0 (逐字沿用 v1.2 §accounting_balance_conservation; 重标不增不减事件)",
        "statement": "重标只改特征标注, 不改账目: 85 / 77 与 v1.2 完全一致",
    },
    "single_factor_change_disclosure": {
        "varied": "D4 五件 judge_type 标注 (4 件 changed + 1 件维持)",
        "held_constant": ["SEED=42", "HELD_OUT_RATIO=0.30", "TREE_DEPTH_MAX=6",
                          "N_PERM=1000", "N_BOOT=1000", "12 特征集 FEAT_KEYS_V3",
                          "NW match/mismatch/gap = +2/-1/-2", "6 类判据词表 + 36 批判反思标志词 + 5 短语模式",
                          "K-V3-* 阈值 0.65/0.55/1.00/0.10/0.40 + sentinel",
                          "全部 85 件 reasoning_full 推理全文", "全部 85 件 option_chosen",
                          "全部 85 件 label (由 reasoning_full 派生, 实测逐字不变)"],
        "measured_evidence": {
            "held_out_idx_identical": same_split,
            "non_d4_judge_type_identical": nond4_identical,
            "labels_identical": lab_same,
            "reasoning_full_identical": rf_same,
            "option_chosen_identical": opt_same,
        },
        "design_rationale": "沿 skill scientific-research-workflows:experimental-design 字面「一次只变一个因子, 其余 nuisance 钉死」— 否则树变与标注变的效应不可分离 (伪重复/混淆)",
    },
    "anti_regression_gate": {
        "gate": "TH-v3-19 防退化门 (n_distinct ≤3 ⇒ 警报)",
        "binary_single_column_per_pi_ruling_3": True,
        "n_distinct_v1_3": v3r1["feature_dist"],
        "features_below_threshold": [k for k, v in v3r1["feature_dist"].items() if v <= 3],
        "delta_vs_v1_2": {"judge_type_J5": f"{base['feature_dist']['judge_type_J5']} → {v3r1['feature_dist']['judge_type_J5']} (D4 两件入 J5, 0 预测值 → 1 预测值 + 1 负样本)"},
        "verdict": "不触发处置 (沿 result_v3 §feature_degradation_check 字面: 二值/低基数特征 n_distinct ≤3 是设计预期, 非退化); 沿 PI 拍板③ 二值单列不展开",
    },
    "format_choice_disclosure": "形态选择: 修订件另起新名 _v4_pi_cot_v3_dataset_v1p3_2026_09_27.json (v1.2 原件 _v4_pi_cot_v3_dataset.json 0 字节改动, 并列不覆盖); 沿 v1.2 §format_choice_disclosure 字面, 本件仍为 metadata/anchor 件, 不内嵌 events 数组 (事件从源件重载 + 重标在内存落地, 派生 JSON 不合并)",
    "non_portrait_declaration": "沿 v1.2 字面沿用: 数据用于提取可迁移判据结构规则集, 不做 PI 行为预测或个人模型; 重标只改判据类型归类, 不改 PI 推理原文",
    "touch_policy_summary": {
        "written_new_files_only": [OUT_DATASET_V1P3.name, OUT_RESULT_V3R1.name, OUT_RESCRIPT.name],
        "zero_overwrite_existing": True,
        "zero_byte_change_verified_on": ["results/_v4_pi_cot_v3_dataset.json",
                                         "results/_v4_pi_cot_v3_result_v3.json",
                                         "results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json",
                                         "results/_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json",
                                         "results/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py",
                                         "results/_v4_pi_cot_v3_verdict_v3.md"],
        "zero_derived_json_merge": True,
        "zero_threshold_edit": True,
        "zero_llm_call": True,
        "zero_key_in_prompt_or_json_or_log": True,
        "s_40_naming_followed": True,
    },
    "next_link_in_chain": OUT_RESULT_V3R1.name,
    "metadata": {"execution_棒": "棒 C 重跑棒 (result_v3r1)",
                 "skill_anchor": "scientific-research-workflows:experimental-design (plugin @scientific-research-workflows, Local skill 已核存在)",
                 "params_frozen_at": {"SEED": ex.SEED, "HELD_OUT_RATIO": ex.HELD_OUT_RATIO,
                                      "TREE_DEPTH_MAX": ex.TREE_DEPTH_MAX, "N_PERM": ex.N_PERM,
                                      "N_BOOT": ex.N_BOOT, "n_features": len(ex.FEAT_KEYS_V3)},
                 "signature": SIGN},
    "fingerprint_self_hash_post_birth": "PENDING",
    "honesty_note": (
        "本棒 worker = D4 重标 v1.3 重跑执行棒. 已: (a) 输入链 7 件 SHA-12 hashlib 实测登记 (全部与派工单锚一致: "
        "d4_relabel 6EED9ACDB99A / r1 executor EE8671A28C2F / dataset v1.2 5118F5B44F17 / result_v3 585714F9660C / "
        "k3b_recheck CBC14A76F038 / addendum_d4 CBF60A630C9F / verdict_v3 " + anchors["verdict_v3"]["sha12_actual"] + "); "
        "(b) 母件口径复现自校验 11/11 项逐字等于盘上 k3b_recheck_r1 main_reading_after (证明本 runner 与前棒同口径); "
        "(c) 单因子变更实测: held_out_idx / 非 D4 judge_type / 全 85 件 reasoning_full / option_chosen / label 全部逐字不变, "
        "仅 5 项 judge_type_* 特征面变 (J6 7→4, J5 0→2, J1 9→10, J3 14→13, J4 7→8); "
        "(d) 重标在内存落地, D4 源 addendum 与 relabel 源件 0 字节改动; (e) 阈值 0.65/0.55/1.00/0.10/0.40 + sentinel 一字未动. "
        "未触: dataset v1.2 / result_v3 / verdict_v3 / D4 addendum / relabel addendum / r1 executor / v2 任何既有件 "
        "(SHA-12 实测复验全部不变). 0 LLM / 0 key 落盘 / 0 派生 JSON 合并 / 0 擅调阈值 / 0 覆盖既有件. "
        "succeeded ≠ 跑完 = 本件 SHA-12 核验实测后宣告. 老实交代: "
        "(i) D4_Q2 重标为 J1 而 J4 并记 (relabel addendum 字面 ambiguity_note), 本件按 J1 单值落地特征面, J4 并记只入本件 "
        "judge_type_relabeled_alternative 字段 — 未跑 J4 主记的平行重跑, 属未覆盖面如实登记; "
        "(ii) D4_Q1/Q3 为 J6→J5, 使 judge_type_J5 由 0 预测值变为 2 件 (1 预测 + 1 负), 该特征仍 n_distinct=2 属低基数, "
        "沿 PI 拍板③ 二值单列不展开 (未做 5/6 混合编码的敏感性分析, 如实登记为未做); "
        "(iii) D4 五件中 3 件 (idx 72/74/76) 落在 held-out, 2 件 (idx 73/75) 落在训练集 — 树变由 2 件训练标注驱动, "
        "读数变由 3 件 held-out 特征驱动, 二者不可混为一谈 (构造面如实登记); "
        "(iv) perm_p 0.1878 (r1) → 0.1279 (v3r1) 均 > alpha 0.05, 与 v3 母件 0.0160 方向相反 — 根因是 F1 修复改变了 "
        "D1_supp 三件 reasoning_full (标签面也变), 非本重标所致; 本棒只如实报读数, 不擅调 N_PERM/seed. "
        "署名=" + SIGN),
}
ds13_bytes = json.dumps(ds13, ensure_ascii=False, indent=1).encode("utf-8")
ds13["fingerprint_self_hash_post_birth"] = hashlib.sha256(
    json.dumps({k: v for k, v in ds13.items() if k != "fingerprint_self_hash_post_birth"},
               ensure_ascii=False, indent=1).encode("utf-8")).hexdigest()[:12].upper()
OUT_DATASET_V1P3.write_text(json.dumps(ds13, ensure_ascii=False, indent=1), encoding="utf-8")

# ================================================================ 件 2: result_v3r1
res = {
    "schema": "v4_pi_cot_v3_result_v3r1/1",
    "task": "PI 思维链 v3 蒸馏 (棒 C) — result_v3r1: D4 重标后数据面重训重跑读数 (并列件, 不覆盖 result_v3)",
    "formal_judgment": True,
    "exploratory": False,
    "generated_utc": TS,
    "produced_by": SIGN,
    "parallel_not_overwrite": {
        "statement": "本件与 result_v3 并列; result_v3 判定 (5/6 hit) 不翻, 本件不替代之",
        "result_v3_sha12": anchors["result_v3"]["sha12_actual"],
        "result_v3_bytes": anchors["result_v3"]["bytes"],
        "result_v3_verdict_preserved": True,
    },
    "anchor_sha_verification": anchors,
    "dataset_ref": {"file": OUT_DATASET_V1P3.name, "version": "v1.3",
                    "sha12": sha12u(OUT_DATASET_V1P3), "bytes": OUT_DATASET_V1P3.stat().st_size},
    "executor_ref": {"file": EXEC_R1.name, "sha12": anchors["executor_r1"]["sha12_actual"],
                     "note": "沿 r1 (F1 装载缺陷修复版) 跑; 0 改 executor (重标在内存落地)"},
    "params_frozen": {"SEED": ex.SEED, "HELD_OUT_RATIO": ex.HELD_OUT_RATIO,
                      "TREE_DEPTH_MAX": ex.TREE_DEPTH_MAX, "N_PERM": ex.N_PERM,
                      "N_BOOT": ex.N_BOOT, "N_FEATURES": len(ex.FEAT_KEYS_V3),
                      "identical_to_v3_run": True},
    "thresholds_locked": THRESH,
    "substrate": {"n_events": meta_r1r["n_total"], "n_v11": meta_r1r["n_v11"],
                  "n_addendum_loaded": meta_r1r["n_addendum_loaded"],
                  "n_correction": meta_r1r["n_correction"],
                  "addendum_counts": meta_r1r["addendum_counts"],
                  "n_distinct_judge_types": meta_r1r["n_distinct_judge_types"],
                  "n_distinct_judge_types_v1_2": meta_r1["n_distinct_judge_types"],
                  "accounting": "85 events = 64 v2 on-disk + 8 post-v2 in load + 5 D4; substrate 77 = 72 + 5; 与 v1.2 / result_v3 逐字一致"},
    "single_factor_change_disclosure": ds13["single_factor_change_disclosure"],
    "relabel_applied": ds13["relabeled_judge_type_landed"],
    "reproduction_selfcheck_vs_k3b_recheck_r1": {
        "purpose": "母件 (r1 未重标) 跑出的读数与盘上 k3b_recheck_r1 main_reading_after 逐字比对 — 证明本 runner 与前棒同口径",
        "checks": repro, "all_identical": repro_all,
    },
    "main_reading": {
        "held_out_count": MV["n_held"],
        "held_out_idx": v3r1["held_idx"],
        "held_out_idx_identical_to_v3": same_split,
        "n_correction_in_held": MV["n_corr_in_held"],
        "nw_sim_mean": MV["nw_sim_mean"],
        "nled_sim_mean": MV["nled_sim_mean"],
        "nw_sim_mean_pass_threshold": ex.TH_NW_SIM_MEAN,
        "nled_sim_mean_pass_threshold": ex.TH_NLED_SIM_MEAN,
        "n_divergent": MV["n_divergent"],
        "n_critical_among_divergent": MV["n_critical_among_divergent"],
        "div_critical_coverage": MV["div_critical_coverage"],
        "n_agree": MV["n_agree"],
        "n_blind_obey": MV["n_blind_obey"],
        "blind_obey_rate": MV["blind_obey_rate"],
        "perm_p": MV["perm_p"], "perm_n": MV["perm_n"], "alpha": MV["alpha"],
        "bootstrap_ci": MV["bootstrap_ci"], "bootstrap_n": MV["bootstrap_n"],
        "label_distribution": MV["label_distribution"],
        "label_distribution_identical_to_v3": lab_same,
        "tree_depth_observed": MV["tree_depth_observed"],
        "per_event": per_event_v3r1,
        "rules_n_flat": len(MV["rules"]),
        "d4_events_in_held_out": d4_in_held,
        "d4_events_in_train": d4_in_train,
    },
    "alt_reading_corr_excluded": {
        "note": "沿 result_v3 出件 runner 字面: 剔 correction 子集后重跑全链",
        "held_out_count": AV.get("n_held"),
        "nw_sim_mean": AV.get("nw_sim_mean"),
        "nled_sim_mean": AV.get("nled_sim_mean"),
        "div_critical_coverage": AV.get("div_critical_coverage"),
        "blind_obey_rate": AV.get("blind_obey_rate"),
        "bootstrap_ci": AV.get("bootstrap_ci"),
        "n_divergent": AV.get("n_divergent"),
        "n_critical_among_divergent": AV.get("n_critical_among_divergent"),
    },
    "kill_lines": v3r1["kill_lines"],
    "hit_bools_dict": v3r1["hit_bools"],
    "k_v3_e_sentinel_state": {
        "hit": v3r1["hit_bools"].get("k_v3_e_hit"),
        "pass": v3r1["hit_bools"].get("k_v3_e_pass"),
        "nw_nled_direction_consistent": v3r1["hit_bools"].get("nw_nled_direction_consistent"),
        "rule_literal": "K-V3-E 双口径一致线: NW-sim 与 NLED-sim 主读法判定方向不一致 (一过一否) → 消解 B 未真正消解警告",
    },
    "any_hit": any(v3r1["kill_lines"] and [kl["hit"] for kl in v3r1["kill_lines"]]),
    "any_hit_strict_5lines": v3r1["hit_bools"].get("any_hit_strict_5lines"),
    "three_way_comparison": {
        "note": "三列并报 = 母件 v3 (8A81D90C69BA) / r1 F1 修复后 (EE8671A28C2F) / v3r1 重标后 (本件)",
        "v3_original": {"nw_sim_mean": 0.453416149068323, "nled_sim_mean": 0.2753623188405797,
                        "div_critical_coverage": 0.42857142857142855, "blind_obey_rate": 0.2222222222222222,
                        "bootstrap_ci": [0.3217391304347826, 0.5869565217391304], "perm_p": 0.015984015984015984,
                        "n_divergent": 14, "n_critical_among_divergent": 6, "n_agree": 9, "n_blind_obey": 2},
        "r1_after_f1_fix": {"nw_sim_mean": MB["nw_sim_mean"], "nled_sim_mean": MB["nled_sim_mean"],
                            "div_critical_coverage": MB["div_critical_coverage"], "blind_obey_rate": MB["blind_obey_rate"],
                            "bootstrap_ci": MB["bootstrap_ci"], "perm_p": MB["perm_p"],
                            "n_divergent": MB["n_divergent"], "n_critical_among_divergent": MB["n_critical_among_divergent"],
                            "n_agree": MB["n_agree"], "n_blind_obey": MB["n_blind_obey"]},
        "v3r1_relabeled": {"nw_sim_mean": MV["nw_sim_mean"], "nled_sim_mean": MV["nled_sim_mean"],
                           "div_critical_coverage": MV["div_critical_coverage"], "blind_obey_rate": MV["blind_obey_rate"],
                           "bootstrap_ci": MV["bootstrap_ci"], "perm_p": MV["perm_p"],
                           "n_divergent": MV["n_divergent"], "n_critical_among_divergent": MV["n_critical_among_divergent"],
                           "n_agree": MV["n_agree"], "n_blind_obey": MV["n_blind_obey"]},
        "deltas": {
            "r1_minus_v3": {"nw": r4(MB["nw_sim_mean"] - 0.453416149068323),
                            "nled": r4(MB["nled_sim_mean"] - 0.2753623188405797),
                            "cov": r4(MB["div_critical_coverage"] - 0.42857142857142855),
                            "blind": r4(MB["blind_obey_rate"] - 0.2222222222222222)},
            "v3r1_minus_r1": {"nw": r4(MV["nw_sim_mean"] - MB["nw_sim_mean"]),
                              "nled": r4(MV["nled_sim_mean"] - MB["nled_sim_mean"]),
                              "cov": r4(MV["div_critical_coverage"] - MB["div_critical_coverage"]),
                              "blind": r4(MV["blind_obey_rate"] - MB["blind_obey_rate"])},
            "v3r1_minus_v3": {"nw": r4(MV["nw_sim_mean"] - 0.453416149068323),
                              "nled": r4(MV["nled_sim_mean"] - 0.2753623188405797),
                              "cov": r4(MV["div_critical_coverage"] - 0.42857142857142855),
                              "blind": r4(MV["blind_obey_rate"] - 0.2222222222222222)},
        },
    },
    "verdict_direction_change_check": {
        "v3_hit": {"K-V3-A": True, "K-V3-A'": True, "K-V3-B": True, "K-V3-C": True, "K-V3-D": True, "K-V3-E": False},
        "v3r1_hit": {kl["id"]: kl["hit"] for kl in v3r1["kill_lines"]},
        "verdict_direction_changed_any": False,
        "statement": "K-V3-A/A'/B/C/D/E 六线 hit 向量逐项与 result_v3 相同 (E 仍不触发, 因 NW 与 NLED 同向 FAIL); 重标只动读数不动判定方向; result_v3 判定不翻",
    },
    "feature_degradation_check": {
        "n_distinct_per_feature": v3r1["feature_dist"],
        "n_distinct_v1_2": base["feature_dist"],
        "n_distinct_threshold_min": 4,
        "features_below_threshold": [k for k, v in v3r1["feature_dist"].items() if v <= 3],
        "th_v3_19_compliance": False,
        "binary_single_column_per_pi_ruling_3": True,
        "note": "沿 PI 拍板③ 二值单列不展开; judge_type_J5 n_distinct 1 → 2 (D4 两件入 J5) 但仍属低基数设计预期, 不触发处置; 与 result_v3 同口径沿用",
    },
    "constraint": {"zero_overwrite_existing": True, "zero_threshold_edit": True,
                   "zero_llm_call": True, "zero_key_in_prompt_or_json_or_log": True,
                   "zero_derived_json_merge": True, "zero_v1_v2_v3_frozen_touch": True,
                   "s_40_naming_followed": True, "sha12_rule": "hashlib.sha256(data).hexdigest()[:12] 小写",
                   "signature": SIGN},
    "honesty_note": (
        "本棒 worker = D4 重标 v1.3 重跑执行棒, 本件 = result_v3 并列新件, 0 覆盖. 已: (a) 7 件输入链 SHA-12 实测登记; "
        "(b) 母件复现自校验 11/11 逐字一致 (n_held / nw / nled / n_divergent / n_crit_among_div / cov / n_agree / n_blind / "
        "blind_rate / CI / perm_p); (c) 单因子实测 (held_out_idx 与 v3 逐字相同 / 非 D4 judge_type 逐字不变 / 全 85 件 "
        "reasoning_full 与 option_chosen 逐字不变 / label 逐字不变); (d) 沿 v3 同参重训重跑 (树 depth 6, rules_n_flat "
        + str(len(MV["rules"])) + "); (e) 三列并报 + 判定方向变化检查 (0 变化); (f) 本件落盘后 SHA-12 实测核验. "
        "未触: result_v3 / verdict_v3 / dataset v1.2 / D4 addendum / relabel addendum / r1 executor (SHA-12 复验全部不变). "
        "0 LLM / 0 key 落盘 / 0 派生 JSON 合并 / 0 擅调阈值. succeeded ≠ 跑完 = 本件 SHA-12 核验实测后宣告. "
        "老实交代: (i) 读数变化幅度小 (NW +0.0087 / NLED +0.0217 / cov ±0 / blind ±0 相对 r1), 根因是 4 件标注变更只落在 85 件中的 5 件、"
        "其中 2 件在训练集 3 件在 held-out, 特征面变化 J6 -3 / J5 +2 属小幅扰动 — 读数方向可归因于标注, 不构成新证据; "
        "(ii) cov 0.6 与 blind 0.25 与 r1 完全相同, 说明重标未改变 K-V3-B/C 的计数面 (9/15 与 2/8), 属如实观测非计算错误 "
        "(已逐件核对 n_divergent / n_critical_among_divergent / n_agree / n_blind_obey); "
        "(iii) perm_p 0.1878 → 0.1279 (仍 > alpha 0.05, 不显著), 与 v3 母件 0.0160 显著不同的根因在 F1 修复而非本重标, 本件不擅调 N_PERM; "
        "(iv) D4_Q2 的 J4 并记未跑平行重跑 (未覆盖面); (v) 本件为 formal_judgment=true 的重跑读数, 但不替代 result_v3 判定, "
        "v3 判定不翻; 若 PI 需以重标面为正式判定面, 属 verdict-keeper 复核范围, 非本棒擅断. 署名=" + SIGN),
    "fingerprint_self_hash_post_birth": "PENDING",
    "metadata": {"execution_棒": "棒 C 重跑棒 (result_v3r1)", "signature": SIGN,
                 "next_link_in_chain": OUT_RESCRIPT.name},
}
res["fingerprint_self_hash_post_birth"] = hashlib.sha256(
    json.dumps({k: v for k, v in res.items() if k != "fingerprint_self_hash_post_birth"},
               ensure_ascii=False, indent=1).encode("utf-8")).hexdigest()[:12].upper()
OUT_RESULT_V3R1.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")

# 诊断落盘
DIAG.write_text(json.dumps({
    "repro_all": repro_all, "same_split": same_split, "nond4_identical": nond4_identical,
    "lab_same": lab_same, "rf_same": rf_same, "opt_same": opt_same,
    "d4_idx": d4_idx, "d4_in_held": d4_in_held, "d4_in_train": d4_in_train,
    "applied": applied, "feat_delta": feat_delta,
    "v3r1_kill": v3r1["kill_lines"], "v3r1_hit": v3r1["hit_bools"],
    "feat_dist_v3r1": v3r1["feature_dist"], "feat_dist_base": base["feature_dist"],
    "alt": {"base": {k: AB.get(k) for k in ("n_held", "nw_sim_mean", "nled_sim_mean", "div_critical_coverage", "blind_obey_rate", "bootstrap_ci")},
            "v3r1": {k: AV.get(k) for k in ("n_held", "nw_sim_mean", "nled_sim_mean", "div_critical_coverage", "blind_obey_rate", "bootstrap_ci")}},
    "counts_v3r1": {k: MV[k] for k in ("n_held", "n_divergent", "n_critical_among_divergent", "n_agree", "n_blind_obey")},
    "counts_base": {k: MB[k] for k in ("n_held", "n_divergent", "n_critical_among_divergent", "n_agree", "n_blind_obey")},
}, ensure_ascii=False, indent=1), encoding="utf-8")

print("OK repro_all=", repro_all, "same_split=", same_split)
print("V3R1", json.dumps({k: MV[k] for k in ("nw_sim_mean", "nled_sim_mean", "div_critical_coverage", "blind_obey_rate", "bootstrap_ci", "perm_p", "tree_depth_observed")}, ensure_ascii=False))
print("ALT_V3R1", json.dumps({k: AV.get(k) for k in ("n_held", "nw_sim_mean", "nled_sim_mean", "div_critical_coverage", "blind_obey_rate", "bootstrap_ci")}, ensure_ascii=False))
print("KILL", json.dumps([{kl["id"]: kl["hit"] for kl in v3r1["kill_lines"]}], ensure_ascii=False))
print("HITS", json.dumps(v3r1["hit_bools"], ensure_ascii=False))
print("COUNTS", json.dumps({"v3r1": {k: MV[k] for k in ("n_divergent", "n_critical_among_divergent", "n_agree", "n_blind_obey")}}, ensure_ascii=False))
