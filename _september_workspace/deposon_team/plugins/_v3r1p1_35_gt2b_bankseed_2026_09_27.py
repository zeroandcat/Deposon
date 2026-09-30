# -*- coding: utf-8 -*-
"""V3-R #35 · v20 GT2b BANK_SEED 复现面重评（执行棒，K-V3R-35 字面）。

来源纪律锚（只读，0 触动）：
  - results/_v3_recheck_prereg_v1p1_2026_09_27.md  §1.2 / §2.1 K-V3R1P1-0-A·0-F·0-G
                                                  §2.2 K-V3R-35 / §2.3 TH-V3R1P1-35-* / §3.2
  - results/_v3_recheck_prereg_v1_2026_09_27.md    §2.3 TH-V3R-0-common-a（改判四档沿 v1 §4）

判死线字面（冻后 0 私设、0 擅调）：
  - 唯一变量 = BANK_SEED ∈ {20260828(既有/对照), 20260829, 20260830}；config 其余字段与
    T_levels/4 域/n_options_fixed=4/chance_level=0.25 一字不动；**field_tol = 0.05 一字不动**。
  - α（既有字面，run_v20_gt2b.py L129）: |field_mean(T) − field_mean(T=1)| ≤ 0.05 ⇒ field_immune
  - β（派工字面）: Δ = field_mean(T) − max(rule_filter(T), random(T))；Δ ≥ 0.05 ⇒ 该格 PASS
  - 聚合规则：**不聚合为单一 verdict**；落 3 seed × 3 T = 9 格 × α/β 双口径矩阵 + 一致性计数。
  - 既有 verdict（strict_inc/strict_dec/inconclusive，rf 驱动）按原字面**另报**，0 并入新面矩阵。
  - 对照留档：T=1 档 as-run 边际 +0.025 —— 0 作阈值、0 参与判定。
  - 禁作杠杆：cfg["seed"]（v1.1 §1.3 实测 0 消费点）⇒ 本件 0 改之，并给出静态+实测双重自证。
  - 资产面：results/gt2_attacker_cache 本仓 0 命中 ⇒ 沿 K-V3R1P1-0-F **只读**仓外
    D:/私人资料/_non_upload_local_archive/results/gt2_attacker_cache/（4 件），0 复制入仓、0 改动。

输出（派生 JSON 0 合并，K-V3R1P1-0-D）：
  results/_v3_recheck_35_result_2026_09_27.json
  results/_v3_recheck_35_rescript_2026_09_27.md（由 rescript 手写落盘，executor 0 写 md）

0 LLM / 0 proxy / 0 key 读取（K-V3R1P1-0-E）。无墙钟时间戳 ⇒ 同输入重跑逐字节一致。
"""
from __future__ import annotations

import hashlib
import json
import os
import sys

REPO = r"D:/私人资料/deposon-repo"
EXT_CACHE = r"D:/私人资料/_non_upload_local_archive/results/gt2_attacker_cache"
EXT_CACHE_ITEMS = ["algorithm_process.json", "biological_taxonomy.json",
                   "historical_causality.json", "physics_concepts.json"]
OUT_PATH = os.path.join(REPO, "results", "_v3_recheck_35_result_2026_09_27.json")

BANK_SEED_SET = (20260828, 20260829, 20260830)   # K-V3R-35 冻结字面
AS_RUN_SEED = 20260828                            # 既有值（对照格）
CHANCE_LEVEL = 0.25                               # TH-V3R1P1-35-c
N_OPTIONS_FIXED = 4                               # TH-V3R1P1-35-c
T1_CONTROL_MARGIN = 0.025                         # 对照留档，0 作阈值
DEGEN_N_DISTINCT_MIN = 4                          # K-V3R1P1-0-A：n_distinct > 3

sys.path.insert(0, REPO)

import numpy as np  # noqa: E402

import run_v20_gt2b as R  # noqa: E402  （只读导入，0 改既有 runner）
from deposon_diffusion import DiffusionConfig, config_dict  # noqa: E402
from llm_prior import _extract_json_array  # noqa: E402

FIELD_TOL = R.FIELD_TOL  # 一字不动（TH-V3R1P1-35-a）
T_LEVELS = R.T_LEVELS
ARMS = R.ARMS


# ---------------------------------------------------------------- 只读工具
def sha12(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def nbytes(path: str) -> int:
    return os.path.getsize(path)


def load_traps_ext(domain: str) -> list:
    """仓外缓存只读取用（K-V3R1P1-0-F）：0 写入 / 0 复制入仓 / 0 删除 / 0 改 ACL。"""
    with open(os.path.join(EXT_CACHE, f"{domain}.json"), encoding="utf-8") as f:
        atk = json.load(f)
    return [str(it["label"]) for it in _extract_json_array(atk["response_text"])]


def load_family_l_graphs() -> dict:
    """与 mindmap_corpus_v20.load_corpus(CORPUS_DIR, families=("L",)) 等价的只读加载。

    偏离登记（诚实交代，不隐藏）：既有 load_corpus 的孤儿哨兵在**本仓现状**下抛错
    （corpus/v20/ 下 all.json / index_v2_2026_09_16.json / strip_captions_22.json 三个
    **非图** JSON 未入 index.json）⇒ 本 executor 走等价只读路径（index.json 登记顺序 +
    family=="L" 过滤），**0 改既有模块 / 0 改 index.json / 0 改语料**。返回集合与
    load_corpus 成功路径逐件相同（孤儿本就不在 index.json 内，哨兵只查目录列表）。
    """
    with open(os.path.join(REPO, "corpus", "v20", "index.json"), encoding="utf-8") as f:
        idx = json.load(f)
    out = {}
    for e in idx["graphs"]:
        if e["family"] != "L":
            continue
        with open(os.path.join(REPO, "corpus", "v20", e["file"]), encoding="utf-8") as f:
            out[e["graph_id"][2:]] = json.load(f)
    return out


def series_stats(series) -> dict:
    """防退化门自证统计量（K-V3R1P1-0-A 字面：n_distinct > 3 + std > 0）。"""
    s = [float(x) for x in series]
    nd = len(set(s))
    std = float(np.std(s))
    binary = bool(nd <= 2)
    return {"n": len(s), "n_distinct": nd, "std": std,
            "is_binary": binary,
            "gate_non_degenerate": bool(nd > 3 and std > 0.0)}


# ---------------------------------------------------------------- 主跑
def run_cell(cfg, graphs, traps, seed, T):
    """单 (seed, T) 格：沿 run_v20_gt2b.answer_quiz 逐题作答，0 改其逻辑。"""
    R.BANK_SEED = seed
    bank = R.build_bank_t(graphs, traps, T)
    per_dom = {}
    for domain, g in graphs.items():
        items = [q for q in bank if q["domain"] == domain]
        per_dom[domain] = R.answer_quiz(g, cfg, items)
    overall = {a: float(np.mean([v["accuracy"][a] for v in per_dom.values()]))
               for a in ARMS}
    return {"bank": bank, "per_domain": per_dom, "overall": overall,
            "n_items": len(bank)}


def main() -> int:
    # ---- 0. 阈值/口径字面冻结自检（0 擅调的可机械自证）----
    assert FIELD_TOL == 0.05, f"FIELD_TOL 被改动：{FIELD_TOL}"
    assert T_LEVELS == (1, 2, 3)
    assert ARMS == ("rule_filter", "field_mean", "random")

    # ---- 1. 输入链核验（先核后用）----
    in_repo = {
        "prereg_v1p1": "results/_v3_recheck_prereg_v1p1_2026_09_27.md",
        "prereg_v1": "results/_v3_recheck_prereg_v1_2026_09_27.md",
        "verdict_3item": "results/_v3_n_recheck_llm_verdict_2026_09_27.md",
        "runner_gt2b": "run_v20_gt2b.py",
        "runner_meanfield": "run_v19_meanfield.py",
        "protocol_field_scores_init": "deposon_protocol.py",
        "corpus_loader": "mindmap_corpus_v20.py",
        "as_run_result": "results/deposon_v20_gt2b.json",
        "spec_gt2b": "docs/SPEC_GT2B.md",
        "corpus_index": "corpus/v20/index.json",
    }
    input_chain = {k: {"path": v, "sha12": sha12(os.path.join(REPO, v)),
                       "bytes": nbytes(os.path.join(REPO, v)),
                       "access": "read_only"} for k, v in in_repo.items()}
    ext_before = {fn: {"path": os.path.join(EXT_CACHE, fn),
                       "sha12": sha12(os.path.join(EXT_CACHE, fn)),
                       "bytes": nbytes(os.path.join(EXT_CACHE, fn)),
                       "access": "read_only_external_archive"}
                  for fn in EXT_CACHE_ITEMS}

    # ---- 2. 资产面（仓外只读）----
    graphs_all = load_family_l_graphs()
    graphs = {d: g for d, g in graphs_all.items()
              if os.path.exists(os.path.join(EXT_CACHE, f"{d}.json"))}
    excluded_domains = sorted(set(graphs_all) - set(graphs))
    traps = {d: load_traps_ext(d) for d in sorted(graphs)}
    corpus_graph_files = {e: {"sha12": sha12(os.path.join(REPO, "corpus", "v20", e)),
                              "bytes": nbytes(os.path.join(REPO, "corpus", "v20", e))}
                          for e in sorted(os.listdir(os.path.join(REPO, "corpus", "v20")))
                          if e.endswith(".json")}

    # ---- 3. 退化杠杆事前登记：cfg["seed"] 静态 + 实测自证 ----
    src = open(os.path.join(REPO, "run_v20_gt2b.py"), encoding="utf-8").read()
    proto = open(os.path.join(REPO, "deposon_protocol.py"), encoding="utf-8").read()
    cfg_seed_static = {
        "runner_cfg_subscript_seed_hits": src.count('cfg["seed"]') + src.count("cfg['seed']"),
        "runner_passed_seed_arg_literal":
            'g_seed + (u * 131 + v) % 100000' in src,
        "protocol_field_scores_init_overwrites_seed":
            '"seed": inst_seed' in proto,
        "static_reading": ("run_v20_gt2b.py 内 cfg[\"seed\"] 0 消费点；field_scores_init "
                           "在 deposon_protocol.py 内以 {\"seed\": inst_seed} 覆盖传入 cfg 的 "
                           "seed 字段，inst_seed 源 = graph[\"seed\"] + 边序，与 cfg.seed 无关"),
    }
    cfg2 = DiffusionConfig()
    cfg2.seed = 987654321
    probe_T = 2
    probe_bank = None
    R.BANK_SEED = AS_RUN_SEED
    probe_bank = R.build_bank_t(graphs, traps, probe_T)
    pd = "physics_concepts"
    p_items = [q for q in probe_bank if q["domain"] == pd]
    base_cfg = DiffusionConfig()
    probe_a = R.answer_quiz(graphs[pd], base_cfg, p_items)
    probe_b = R.answer_quiz(graphs[pd], cfg2, p_items)
    cfg_seed_static["empirical_bit_identical_when_cfg_seed_changed"] = (
        json.dumps(probe_a, sort_keys=True) == json.dumps(probe_b, sort_keys=True))
    cfg_seed_static["lever_status"] = ("0 消费点已双重自证（静态 + 实测 bit-identical）"
                                       "⇒ 禁作杠杆登记成立，本件 0 以 cfg.seed 为变量")

    # ---- 4. 主构造：3 seed × 3 T = 9 格 × α/β 双口径 ----
    cfg = DiffusionConfig()
    cells = []
    for seed in BANK_SEED_SET:
        for T in T_LEVELS:
            r = run_cell(cfg, graphs, traps, seed, T)
            cells.append({"bank_seed": seed, "T": T, "n_items": r["n_items"],
                          "accuracy": r["overall"],
                          "per_domain_accuracy": {d: v["accuracy"]
                                                  for d, v in sorted(r["per_domain"].items())},
                          "per_domain_n_items": {d: v["n_items"]
                                                 for d, v in sorted(r["per_domain"].items())}})
    acc = {(c["bank_seed"], c["T"]): c["accuracy"] for c in cells}

    matrix = []
    for c in cells:
        seed, T = c["bank_seed"], c["T"]
        a = c["accuracy"]
        strongest = max(a["rule_filter"], a["random"])  # 「最强对手」定义冻结
        delta_beta = a["field_mean"] - strongest
        delta_alpha = abs(a["field_mean"] - acc[(seed, 1)]["field_mean"])
        matrix.append({
            "cell": f"seed{seed}_T{T}",
            "bank_seed": seed, "T": T, "n_items": c["n_items"],
            "accuracy": a,
            "per_domain_accuracy": c["per_domain_accuracy"],
            "per_domain_n_items": c["per_domain_n_items"],
            "strongest_opponent_value": strongest,
            "strongest_opponent_arm": ("rule_filter" if a["rule_filter"] >= a["random"]
                                       else "random"),
            "kou_jing_alpha": {
                "definition": "|field_mean(T) - field_mean(T=1)| (run_v20_gt2b.py L129)",
                "value": delta_alpha, "field_tol": FIELD_TOL,
                "field_immune": bool(delta_alpha <= FIELD_TOL),
                "alpha_pass": bool(delta_alpha <= FIELD_TOL),
                "alpha_alert_hit": bool(delta_alpha > FIELD_TOL),
                "note_T1": ("T=1 格恒为 0.0（自指恒等）⇒ field_immune 恒 True，"
                            "该格 α 不具鉴别力，单列不作敏感性证据"),
            },
            "kou_jing_beta": {
                "definition": "delta = field_mean(T) - max(rule_filter(T), random(T))",
                "value": delta_beta,
                "beta_pass": bool(delta_beta >= FIELD_TOL),
                "beta_alert_hit": bool(delta_beta < FIELD_TOL),
                "band": ("PASS" if delta_beta >= FIELD_TOL else "BELOW_TOL"),
            },
            "chance_level": CHANCE_LEVEL,
        })

    # 一致性计数（K-V3R-35 聚合规则：计数，非单一 verdict）
    beta_bands = [m["kou_jing_beta"]["band"] for m in matrix]
    alpha_flags = [m["kou_jing_alpha"]["field_immune"] for m in matrix]
    alpha_flags_nontrivial = [m["kou_jing_alpha"]["field_immune"] for m in matrix
                              if m["T"] != 1]
    # 浮点刀锋格披露（0 擅调阈值、0 round：双读并报）
    boundary_cells = [{
        "cell": m["cell"],
        "beta_value_exact_repr": repr(m["kou_jing_beta"]["value"]),
        "field_tol": FIELD_TOL,
        "float_comparison_ge_tol": bool(m["kou_jing_beta"]["value"] >= FIELD_TOL),
        "as_run_band": m["kou_jing_beta"]["band"],
        "mathematical_value_note": ("两侧读数均落在 0.1 粒度网格上（field_mean=0.375, "
                                    "最强对手=0.325）⇒ 数学值恰为 0.05，"
                                    "IEEE-754 双精度差为 0.04999999999999999"),
        "both_readings": {"float_literal_band": m["kou_jing_beta"]["band"],
                          "if_rounded_math_band": "PASS"},
    } for m in matrix if abs(m["kou_jing_beta"]["value"] - FIELD_TOL) < 1e-6]
    consistency = {
        "n_cells": len(matrix),
        "beta_band_counts": {b: beta_bands.count(b) for b in sorted(set(beta_bands))},
        "beta_band_counts_if_knife_edge_rounded": {
            "PASS": sum(1 for m in matrix
                        if m["kou_jing_beta"]["band"] == "PASS"
                        or abs(m["kou_jing_beta"]["value"] - FIELD_TOL) < 1e-6),
            "BELOW_TOL": sum(1 for m in matrix
                             if m["kou_jing_beta"]["band"] == "BELOW_TOL"
                             and abs(m["kou_jing_beta"]["value"] - FIELD_TOL) >= 1e-6)},
        "beta_boundary_knife_edge_cells": boundary_cells,
        "beta_9_of_9_same_band": len(set(beta_bands)) == 1,
        "alpha_T2T3_cells": len(alpha_flags_nontrivial),
        "alpha_field_immune_count_T2T3": int(sum(alpha_flags_nontrivial)),
        "alpha_all_T2T3_immune": bool(all(alpha_flags_nontrivial)),
        "alpha_9_of_9_same_flag_incl_T1": len(set(alpha_flags)) == 1,
        "note": ("α/β 双口径强制并报、0 互替（K-V3R1P1-0-C）；T=1 格 α 自指恒等，"
                 "一致性计数分「含 T=1」与「仅 T∈{2,3}」两读并报"),
    }

    # legacy verdict（既有字面另报，0 并入新面矩阵）
    legacy = []
    for seed in BANK_SEED_SET:
        acc_by_T = {a: {T: acc[(seed, T)][a] for T in T_LEVELS} for a in ARMS}
        v, detail = R.verdict(acc_by_T)
        legacy.append({"bank_seed": seed, "legacy_verdict": v,
                       "legacy_detail": detail,
                       "legacy_beta_margin_T1": acc_by_T["field_mean"][1] -
                       max(acc_by_T["rule_filter"][1], acc_by_T["random"][1])})

    # ---- 5. 防退化门自证（K-V3R1P1-0-A）三读并报 ----
    degen = {
        "rule": "n_distinct > 3 + std > 0（K-V3R1P1-0-A）",
        "reading_A_per_domain_item_accuracy": {
            "definition": "每格每臂的 4 个域 item 级正确率序列（n=4）",
            "per_cell": {f"seed{c['bank_seed']}_T{c['T']}":
                         {a: series_stats([c["per_domain_accuracy"][d][a] for d in c["per_domain_accuracy"]])
                          for a in ARMS} for c in cells},
        },
        "reading_B_per_item_correctness": {
            "definition": "每格每臂的 40 条 item 级 0/1 正确性序列（n=40）",
            "note": "结构性二值 ⇒ n_distinct ≤ 2 恒成立；沿 PI 拍板③ **二值单列**，"
                    "不与 n_distinct > 3 门混算",
            "is_binary_by_construction": True,
        },
        "reading_C_cell_level_readout": {
            "definition": "9 格格级读数序列（每臂 n=9）",
            "per_arm": {a: series_stats([acc[(s, T)][a] for s in BANK_SEED_SET for T in T_LEVELS])
                        for a in ARMS},
        },
    }
    _a_vals = [v for cell in degen["reading_A_per_domain_item_accuracy"]["per_cell"].values()
               for v in cell.values()]
    degen["reading_A_summary"] = {
        "n_cell_arm_series": len(_a_vals),
        "n_pass": sum(1 for v in _a_vals if v["gate_non_degenerate"]),
        "n_fail": sum(1 for v in _a_vals if not v["gate_non_degenerate"]),
        "fail_cells": [f"{cell}|{a}" for cell, arms in
                       degen["reading_A_per_domain_item_accuracy"]["per_cell"].items()
                       for a, v in arms.items() if not v["gate_non_degenerate"]],
    }
    degen["reading_A_all_cells_pass"] = bool(degen["reading_A_summary"]["n_fail"] == 0)
    degen["reading_C_all_arms_pass"] = bool(all(
        v["gate_non_degenerate"] for v in degen["reading_C_cell_level_readout"]["per_arm"].values()))
    degen["cfg_seed_lever"] = cfg_seed_static
    degen["reading_dependence_disclosure"] = (
        "防退化门结论依赖「n_distinct 取哪条序列」：读法 A（item 级 = 4 域 item 正确率序列，"
        f"{degen['reading_A_summary']['n_fail']}/{degen['reading_A_summary']['n_cell_arm_series']} "
        "条不过门）⇒ 触发 K-V3R-35 (b)「不明」；读法 C（格级读数序列）全过门 ⇒ 落 (a) 分支"
        "「按矩阵如实登记」；读法 B 结构性二值单列。**判死线字面所指为「item 级正确率」"
        "⇒ 故以读法 A 为准**；两读差异如实登记，0 合并、0 私自改门")

    # ---- 6. as-run 环境自证（0 环境漂移）----
    as_run = json.load(open(os.path.join(REPO, "results", "deposon_v20_gt2b.json"),
                            encoding="utf-8"))
    as_run_check = {
        "as_run_bank_seed": as_run["bank_seed"],
        "as_run_accuracy_by_T": as_run["accuracy_by_T"],
        "recomputed_accuracy_by_T_seed20260828": {
            a: {str(T): acc[(AS_RUN_SEED, T)][a] for T in T_LEVELS} for a in ARMS},
        "bit_identical": bool(as_run["accuracy_by_T"] == {
            a: {str(T): acc[(AS_RUN_SEED, T)][a] for T in T_LEVELS} for a in ARMS}),
        "as_run_legacy_verdict": as_run["verdict"],
        "recomputed_legacy_verdict_seed20260828": legacy[0]["legacy_verdict"],
        "T1_beta_margin_as_run_control": T1_CONTROL_MARGIN,
        "T1_beta_margin_recomputed": legacy[0]["legacy_beta_margin_T1"],
        "control_used_as_threshold": False,
    }

    # ---- 7. 改判（新构造 vs 原标注一致性，沿 v1 §4 四档）----
    all_pass_beta = consistency["beta_band_counts"].get("PASS", 0) == len(matrix)
    all_below_beta = consistency["beta_band_counts"].get("BELOW_TOL", 0) == len(matrix)
    all_alpha_immune = consistency["alpha_all_T2T3_immune"]
    if all_pass_beta and all_alpha_immune:
        new_verdict = "PASS"
    elif not degen["reading_A_all_cells_pass"]:
        new_verdict = "UNKNOWN_DEGENERACY_GATE"
    else:
        new_verdict = "INCONCLUSIVE_MARGINAL"
    rejudge = {
        "new_verdict": new_verdict,
        "legacy_verdict": [l["legacy_verdict"] for l in legacy],
        "consistency_alpha_vs_beta": {
            "alpha_T2T3_all_immune": all_alpha_immune,
            "beta_all_PASS": all_pass_beta,
            "beta_all_BELOW_TOL": all_below_beta,
            "alpha_beta_agree": bool(all_alpha_immune == all_pass_beta),
            "note": "α/β 结论不可互替（K-V3R1P1-0-C）；本字段只登记是否同向，不合并",
        },
        "rejudge_tier_v1_4tier": (
            "PASS + 与原标注一致 ⇒ 原报告 0 触动 + 另立改判件（不得不 A）"
            if new_verdict == "PASS" else
            ("不明分支（退化警报）⇒ γ 登记 + 归 V4 收尾整理待拍板桶"
             if new_verdict == "UNKNOWN_DEGENERACY_GATE" else
             "维持原标注 inconclusive；新面矩阵如实登记，双口径异档逐格留边际，0 聚合")),
    }

    # ---- 8. γ 登记 ----
    gamma = []
    if boundary_cells:
        gamma.append({"id": "G35-6",
                      "trigger": ("β 刀锋格：float 差落在阈值 1e-6 邻域（数学值恰 = 0.05，"
                                  "IEEE-754 差 = 0.04999999999999999）"),
                      "status": "triggered",
                      "detail": {"cells": boundary_cells,
                                 "band_counts_literal": consistency["beta_band_counts"],
                                 "band_counts_if_rounded": consistency
                                 ["beta_band_counts_if_knife_edge_rounded"],
                                 "action": "0 擅调阈值、0 round；双读并报，如实登记"}})
    if not degen["reading_A_all_cells_pass"]:
        gamma.append({"id": "G35-1", "trigger": "reading_A 某格 n_distinct ≤ 3 或 std = 0",
                      "status": "triggered"})
    if excluded_domains:
        gamma.append({"id": "G35-2",
                      "trigger": "缓存域缺（另 2 域无 gt2_attacker_cache）⇒ 不得外推至全 6 域",
                      "status": "registered_as_scope_limit",
                      "detail": {"excluded_domains": excluded_domains,
                                 "included_domains": sorted(graphs)}})
    if not as_run_check["bit_identical"]:
        gamma.append({"id": "G35-3", "trigger": "as-run 环境不可复现（0 环境漂移自证失败）",
                      "status": "triggered"})
    gamma.append({"id": "G35-4", "trigger": "T=1 档 as-run 边际 +0.025 沿既有字面留档",
                  "status": "control_only_not_threshold",
                  "detail": {"value": T1_CONTROL_MARGIN,
                             "used_as_threshold": False,
                             "used_in_judgement": False}})
    gamma.append({"id": "G35-5",
                  "trigger": "corpus 孤儿哨兵致既有 load_corpus 抛错 ⇒ 走等价只读加载",
                  "status": "deviation_registered",
                  "detail": {"orphan_non_graph_json": ["all.json",
                                                       "index_v2_2026_09_16.json",
                                                       "strip_captions_22.json"],
                             "existing_modules_modified": 0,
                             "corpus_files_modified": 0}})

    # ---- 9. 仓外只读自证（跑后复读）----
    ext_after = {fn: {"sha12": sha12(os.path.join(EXT_CACHE, fn)),
                      "bytes": nbytes(os.path.join(EXT_CACHE, fn))}
                 for fn in EXT_CACHE_ITEMS}
    ext_readonly = {
        "external_archive": "D:/私人资料/_non_upload_local_archive/",
        "items": ext_before,
        "pre_post_comparison_basis": "sha12 + bytes（跑前/跑后逐件复读）",
        "pre_post_identical": bool(
            {fn: (v["sha12"], v["bytes"]) for fn, v in ext_before.items()} ==
            {fn: (v["sha12"], v["bytes"]) for fn, v in ext_after.items()}),
        "copied_into_repo": 0,
        "wrote_external": False,
        "repo_cache_dir_exists": os.path.exists(os.path.join(REPO, "results",
                                                              "gt2_attacker_cache")),
        "declaration": "只读取用授权：0 复制入仓 / 0 写入 / 0 移出 / 0 删除 / 0 改 ACL",
    }

    out = {
        "task": "V3-R #35 v20 GT2b BANK_SEED 复现面重评（K-V3R-35）",
        "date": "2026-09-27",
        "author": "Mavis 团队 worker",
        "prereg": "results/_v3_recheck_prereg_v1p1_2026_09_27.md",
        "kill_line": "K-V3R-35（field_tol = 0.05 一字不动；α/β 双口径强制并报；9 格矩阵不聚合）",
        "frozen_params": {
            "field_tol": FIELD_TOL, "field_tol_unchanged": True,
            "bank_seed_set": list(BANK_SEED_SET), "as_run_seed": AS_RUN_SEED,
            "T_levels": list(T_LEVELS), "ARMS": list(ARMS),
            "n_options_fixed": N_OPTIONS_FIXED, "chance_level": CHANCE_LEVEL,
            "n_items_per_map": R.N_ITEMS_PER_MAP,
            "config": config_dict(cfg),
            "new_thresholds_introduced": 0,
        },
        "input_chain": input_chain,
        "external_readonly": ext_readonly,
        "corpus_files": corpus_graph_files,
        "assets": {
            "domains_included": sorted(graphs),
            "domains_excluded_no_cache": excluded_domains,
            "traps_available_per_domain": {d: len(t) for d, t in sorted(traps.items())},
            "scope_limit": "仅 4 缓存域；不得外推至全 6 域（v1.1 §1.3）",
        },
        "kou_jing_fields": {
            "alpha": "|field_mean(T) - field_mean(T=1)| <= 0.05 ⇒ field_immune（既有字面）",
            "beta": "delta = field_mean(T) - max(rule_filter(T), random(T)); >= 0.05 ⇒ PASS",
            "strongest_opponent_definition": "max(rule_filter(T), random(T))（两对照臂取大）",
            "aggregation": "不聚合为单一 verdict（9 格 × 双口径矩阵 + 一致性计数）",
            "alpha_beta_not_interchangeable": True,
        },
        "matrix_9cells": matrix,
        "consistency": consistency,
        "legacy_verdict_separate": legacy,
        "construct_degen_self_check": degen,
        "as_run_environment_self_check": as_run_check,
        "new_verdict": rejudge["new_verdict"],
        "legacy_verdict": [l["legacy_verdict"] for l in legacy],
        "consistency_alpha_vs_beta": rejudge["consistency_alpha_vs_beta"],
        "rejudge_tier_v1_4tier": rejudge["rejudge_tier_v1_4tier"],
        "gamma_registry": gamma,
        "zero_touch_declaration": {
            "existing_files_modified": 0,
            "runner_modified": False,
            "corpus_or_index_modified": False,
            "derived_json_merged_into_existing": False,
            "llm_calls": 0, "proxy": False, "key_reads": 0,
        },
        "determinism": "无墙钟时间戳；同输入重跑本 JSON 逐字节一致（重跑自证见汇报）",
    }
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=False)
    print(json.dumps({"out": OUT_PATH, "new_verdict": out["new_verdict"],
                      "legacy_verdict": out["legacy_verdict"],
                      "beta_band_counts": consistency["beta_band_counts"],
                      "alpha_T2T3_immune": consistency["alpha_all_T2T3_immune"],
                      "as_run_bit_identical": as_run_check["bit_identical"],
                      "reading_A_all_pass": degen["reading_A_all_cells_pass"],
                      "ext_readonly_identical": ext_readonly["pre_post_identical"]},
                     ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
