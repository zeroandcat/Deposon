# -*- coding: utf-8 -*-
"""V5 #35 v2 · GT2b 场免疫性 · 扩矩阵执行面（K-V5R2-35-AR1…AR6 + §3.2.1 + §3.3）。

来源纪律锚（只读，0 触动）：
  - results/_v5_item35_prereg_v2_2026_09_28.md        （1fb2419c6e96，生效即锁）
        §3.2 AR1/AR2/AR3/AR4/AR5/AR6 / §3.2.1 刀锋格 / §3.3 三态终态表
        §3.4 反假判 / §4 扩矩阵执行面参数 / §5 防退化审查 / §6 阈值 0 新设 / §9 γ
  - results/_v3_recheck_35_result_2026_09_27.json     （v1.1 9 格，只读并列双记）
  - deposon_team/plugins/_v3r1p1_35_gt2b_bankseed_2026_09_27.py（62353279cd0c，只读参照）

本棒职责（PI 2026-09-29 派工）：
  1. 跑扩矩阵 6 BANK_SEED × 3 T = 18 格 × α/β 双口径（AR2）
  2. 逐格留边际 + 逐腿机械落档（三态 PASS/FAIL/KD），**交 verdict-keeper 裁定；本棒 0 代判**
  3. 防退化门按 AR4 施于读法 D（逐臂 × 全矩阵 72 值），A/C 双记并报
  4. 刀锋格按 AR6 判带唯一 = float64 字面档（0 round / 0 ±ε / 0 双计）
  5. K-V3R-35 (b) 四类触发**照旧逐条检测、照旧逐条登记 γ**（仅终点归属由 §3.1 叠加为 KD）

0 新设阈值：`field_tol = 0.05` 一字不动（启动即 assert）。刀锋格标签 `1e-6` 沿 v1 executor
既有实现字面，只打标签、0 参与档位判定。

派生 JSON 0 合并：写新名独立件 `results/_v5_item35_v2_matrix_result_2026_09_29.json`，
0 并入 `deposon_v20_gt2b.json` 或任何 `_v3_*` / `_v5_*` 既有件（沿 K-V3R1P1-0-D）。

0 LLM / 0 proxy / 0 key 读取（沿 K-V3R1P1-0-E）。无墙钟时间戳 ⇒ 同输入重跑逐字节一致。
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
OUT_PATH = os.path.join(REPO, "results", "_v5_item35_v2_matrix_result_2026_09_29.json")

# ---- v2 §4.1 冻结值（构造型设计参数，0 阈值）----
BANK_SEED_SET_V2 = (20260828, 20260829, 20260830,   # 既有 3 档（v1.1 字面，0 删）
                    20260831, 20260832, 20260833)   # v2 新增 3 档（连续整数，读数未知前固定）
SEEDS_EXISTING = (20260828, 20260829, 20260830)
SEEDS_V2_NEW = (20260831, 20260832, 20260833)
AS_RUN_SEED = 20260828
CHANCE_LEVEL = 0.25            # TH-V3R1P1-35-c
N_OPTIONS_FIXED = 4            # TH-V3R1P1-35-c
T1_CONTROL_MARGIN = 0.025      # γ-V2-4 对照留档，0 作阈值
KNIFE_EDGE_LABEL_EPS = 1e-6    # 沿 v1 executor 既有实现字面，只打标签
DEGEN_N_DISTINCT_MIN = 4       # K-V3R1P1-0-A：n_distinct > 3

# ---- 0 触动件（跑前/跑后逐件复读 sha12 + bytes）----
ZERO_TOUCH = {
    "prereg_v2": "results/_v5_item35_prereg_v2_2026_09_28.md",
    "prereg_v1p1": "results/_v3_recheck_prereg_v1p1_2026_09_27.md",
    "prereg_v1": "results/_v3_recheck_prereg_v1_2026_09_27.md",
    "v1_rescript_35": "results/_v3_recheck_35_rescript_2026_09_27.md",
    "v1_result_35": "results/_v3_recheck_35_result_2026_09_27.json",
    "v1_executor_35": "deposon_team/plugins/_v3r1p1_35_gt2b_bankseed_2026_09_27.py",
    "verdict_register": "results/_v3_recheck_verdict_register_2026_09_27.md",
    "verdict_3item": "results/_v3_n_recheck_llm_verdict_2026_09_27.md",
    "runner_gt2b": "run_v20_gt2b.py",
    "runner_meanfield": "run_v19_meanfield.py",
    "protocol": "deposon_protocol.py",
    "corpus_loader": "mindmap_corpus_v20.py",
    "as_run_result": "results/deposon_v20_gt2b.json",
    "spec_gt2b": "docs/SPEC_GT2B.md",
    "corpus_index": "corpus/v20/index.json",
}

sys.path.insert(0, REPO)

import numpy as np  # noqa: E402

import run_v20_gt2b as R  # noqa: E402（只读导入，0 改既有 runner）
from deposon_diffusion import DiffusionConfig, config_dict  # noqa: E402
from llm_prior import _extract_json_array  # noqa: E402

FIELD_TOL = R.FIELD_TOL   # 一字不动（TH-V3R1P1-35-a）
T_LEVELS = R.T_LEVELS
ARMS = R.ARMS


# ---------------------------------------------------------------- 只读工具
def sha12(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def nbytes(path: str) -> int:
    return os.path.getsize(path)


def fingerprint(paths: dict) -> dict:
    return {k: {"path": v, "sha12": sha12(os.path.join(REPO, v)),
                "bytes": nbytes(os.path.join(REPO, v)), "access": "read_only"}
            for k, v in paths.items()}


def load_traps_ext(domain: str) -> list:
    """仓外缓存只读取用（K-V3R1P1-0-F）：0 写入 / 0 复制入仓 / 0 删除 / 0 改 ACL。"""
    with open(os.path.join(EXT_CACHE, f"{domain}.json"), encoding="utf-8") as f:
        atk = json.load(f)
    return [str(it["label"]) for it in _extract_json_array(atk["response_text"])]


def load_family_l_graphs() -> dict:
    """与 mindmap_corpus_v20.load_corpus(CORPUS_DIR, families=("L",)) 等价的只读加载。

    偏离登记（沿 v1 executor γ-V2-5 / G35-5 字面，诚实交代不隐藏）：既有 load_corpus 的
    孤儿哨兵在本仓现状下抛错 ⇒ 走等价只读路径（index.json 登记顺序 + family=="L" 过滤），
    0 改既有模块 / 0 改 index.json / 0 改语料。构造顺序与 v1 executor **逐字一致**
    （rng 消费顺序依赖 graphs 迭代序 ⇒ 顺序变了即破坏 §4.5 逐位复现自证）。
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
    """防退化门统计量（K-V3R1P1-0-A 字面：n_distinct > 3 + std > 0）。"""
    s = [float(x) for x in series]
    nd = len(set(s))
    std = float(np.std(s))
    return {"n": len(s), "n_distinct": nd, "std": std,
            "min": min(s), "max": max(s),
            "is_binary": bool(nd <= 2),
            "gate_non_degenerate": bool(nd > (DEGEN_N_DISTINCT_MIN - 1) and std > 0.0)}


def is_finite(x) -> bool:
    return bool(x is not None and not isinstance(x, bool) and np.isfinite(float(x)))


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
    assert BANK_SEED_SET_V2[:3] == SEEDS_EXISTING and len(BANK_SEED_SET_V2) == 6
    assert list(BANK_SEED_SET_V2[3:]) == list(SEEDS_V2_NEW)

    # ---- 1. 跑前 0 触动基线 + 跑前仓外缓存基线 ----
    zt_pre = fingerprint(ZERO_TOUCH)
    ext_pre = {fn: {"path": os.path.join(EXT_CACHE, fn),
                    "sha12": sha12(os.path.join(EXT_CACHE, fn)),
                    "bytes": nbytes(os.path.join(EXT_CACHE, fn)),
                    "access": "read_only_external_archive"}
               for fn in EXT_CACHE_ITEMS}
    ext_read_ok = True
    ext_read_error = None
    try:
        for fn in EXT_CACHE_ITEMS:
            with open(os.path.join(EXT_CACHE, fn), "rb") as f:
                f.read(1)
    except Exception as exc:                                    # pragma: no cover
        ext_read_ok, ext_read_error = False, repr(exc)

    # ---- 2. 资产面（仓外只读，构造顺序与 v1 逐字一致）----
    graphs_all = load_family_l_graphs()
    graphs = {d: g for d, g in graphs_all.items()
              if os.path.exists(os.path.join(EXT_CACHE, f"{d}.json"))}
    excluded_domains = sorted(set(graphs_all) - set(graphs))
    traps = {d: load_traps_ext(d) for d in sorted(graphs)}

    # ---- 3. 开跑前 · 防退化自证（v2 §5.1 已知退化杠杆：cfg["seed"]）----
    #   静态自证 + 实测 bit-identical 自证，**在 18 格主矩阵开跑前**完成
    src = open(os.path.join(REPO, "run_v20_gt2b.py"), encoding="utf-8").read()
    proto = open(os.path.join(REPO, "deposon_protocol.py"), encoding="utf-8").read()
    cfg_seed_static = {
        "lever": "cfg[\"seed\"]",
        "runner_cfg_subscript_seed_hits": src.count('cfg["seed"]') + src.count("cfg['seed']"),
        "runner_passed_seed_arg_literal":
            'g_seed + (u * 131 + v) % 100000' in src,
        "protocol_field_scores_init_overwrites_seed": '"seed": inst_seed' in proto,
        "static_reading": ("run_v20_gt2b.py 内 cfg[\"seed\"] 0 消费点；field_scores_init "
                           "在 deposon_protocol.py 内以 {\"seed\": inst_seed} 覆盖传入 cfg 的 "
                           "seed 字段，inst_seed 源 = graph[\"seed\"] + 边序，与 cfg.seed 无关"),
    }
    cfg2 = DiffusionConfig()
    cfg2.seed = 987654321
    R.BANK_SEED = AS_RUN_SEED
    probe_bank = R.build_bank_t(graphs, traps, 2)
    pd = "physics_concepts"
    p_items = [q for q in probe_bank if q["domain"] == pd]
    base_cfg = DiffusionConfig()
    probe_a = R.answer_quiz(graphs[pd], base_cfg, p_items)
    probe_b = R.answer_quiz(graphs[pd], cfg2, p_items)
    cfg_seed_static["empirical_bit_identical_when_cfg_seed_changed"] = (
        json.dumps(probe_a, sort_keys=True) == json.dumps(probe_b, sort_keys=True))
    cfg_seed_static["probe_result"] = {a: probe_a["accuracy"][a] for a in ARMS}
    cfg_seed_static["lever_status"] = (
        "0 消费点已双重自证（静态 + 实测 bit-identical）⇒ 禁作杠杆登记成立，"
        "本件 0 以 cfg.seed 为扫描变量（v2 §4.4 / §5.1）")
    cfg_seed_static["other_known_levers"] = {
        "BANK_SEED": ("唯一扫描变量；有真实消费点（stable_seed → graph[\"seed\"] → "
                      "field_scores_init），故 v2 扩档只改此一项"),
        "T_levels": "一字不动（1,2,3）",
    }
    pre_run_selfcheck = {
        "field_tol_literal": FIELD_TOL,
        "field_tol_unchanged": True,
        "new_numeric_thresholds_introduced": 0,
        "knife_edge_label_eps_source": "v1 executor 62353279cd0c 既有实现字面（只打标签）",
        "domains_available": sorted(graphs),
        "domains_excluded_no_cache": excluded_domains,
        "traps_available_per_domain": {d: len(t) for d, t in sorted(traps.items())},
        "external_read_only_reachable": ext_read_ok,
        "external_read_only_error": ext_read_error,
        "n_domains_in_matrix": len(graphs),
        "n_items_per_cell_expected": len(graphs) * R.N_ITEMS_PER_MAP,
        "cfg_seed_lever_double_selfproof": cfg_seed_static,
        "gate_sequence_frozen_before_measurement": (
            "读法 D（逐臂 × 全矩阵域级正确率池化）—— v2 §5.2 AR4 测量前唯一冻结；"
            "读法 A / C 继续双记并报、仅作对照登记，0 再作为判死线分支"),
    }

    # ---- 4. 主构造：6 seed × 3 T = 18 格 × α/β 双口径（AR2）----
    cfg = DiffusionConfig()
    cells = []
    for seed in BANK_SEED_SET_V2:
        for T in T_LEVELS:
            r = run_cell(cfg, graphs, traps, seed, T)
            cells.append({"bank_seed": seed, "T": T, "n_items": r["n_items"],
                          "accuracy": r["overall"],
                          "per_domain_accuracy": {d: v["accuracy"]
                                                  for d, v in sorted(r["per_domain"].items())},
                          "per_domain_n_items": {d: v["n_items"]
                                                 for d, v in sorted(r["per_domain"].items())}})
    acc = {(c["bank_seed"], c["T"]): c["accuracy"] for c in cells}

    # ---- 5. 逐格留边际：α / β 双口径（0 互替，K-V3R1P1-0-C）----
    matrix = []
    for c in cells:
        seed, T = c["bank_seed"], c["T"]
        a = c["accuracy"]
        strongest = max(a["rule_filter"], a["random"])   # 「最强对手」定义冻结
        delta_beta = a["field_mean"] - strongest
        delta_alpha = abs(a["field_mean"] - acc[(seed, 1)]["field_mean"])

        # β 刀锋格（AR6 / §3.2.1）：标签 1e-6 只打标签；判带唯一 = float64 字面档
        knife = bool(abs(delta_beta - FIELD_TOL) < KNIFE_EDGE_LABEL_EPS)
        band_float = "PASS" if delta_beta >= FIELD_TOL else "BELOW_TOL"
        band_math = "PASS" if round(delta_beta, 10) >= FIELD_TOL else "BELOW_TOL"

        # α 腿：T=1 为结构性恒等格（§5.4），登记但 0 计入判定分母
        alpha_band = "IMMUNE" if delta_alpha <= FIELD_TOL else "NOT_IMMUNE"
        alpha_in_denom = bool(T != 1)

        alpha_vals_ok = all(is_finite(a[k]) for k in ARMS)
        beta_vals_ok = all(is_finite(a[k]) for k in ARMS) and is_finite(delta_beta) \
            and is_finite(delta_alpha)
        n_items_ok = c["n_items"] == pre_run_selfcheck["n_items_per_cell_expected"]

        matrix.append({
            "cell": f"seed{seed}_T{T}",
            "bank_seed": seed, "T": T,
            "seed_origin": ("existing_v1p1" if seed in SEEDS_EXISTING else "new_v2_consecutive"),
            "n_items": c["n_items"],
            "n_items_expected": pre_run_selfcheck["n_items_per_cell_expected"],
            "n_items_as_expected": n_items_ok,
            "accuracy": a,
            "per_domain_accuracy": c["per_domain_accuracy"],
            "per_domain_n_items": c["per_domain_n_items"],
            "strongest_opponent_value": strongest,
            "strongest_opponent_arm": ("rule_filter" if a["rule_filter"] >= a["random"]
                                       else "random"),
            "kou_jing_alpha": {
                "definition": "|field_mean(T) - field_mean(T=1)| (run_v20_gt2b.py L129 字面)",
                "value": delta_alpha, "value_float_literal": repr(delta_alpha),
                "field_tol": FIELD_TOL,
                "band": alpha_band,
                "field_immune": bool(delta_alpha <= FIELD_TOL),
                "knife_edge_like_label_CONTROL_ONLY": ({
                    "value_float_literal": repr(delta_alpha),
                    "label_eps": KNIFE_EDGE_LABEL_EPS,
                    "mathematical_value_note": "两侧读数落在 0.025 粒度网格上 ⇒ 数学值恰 = 0.05",
                    "band_float_literal": alpha_band,
                    "band_if_math_value_used": "IMMUNE" if 0.05 <= FIELD_TOL else "NOT_IMMUNE",
                    "band_changes_under_either_reading": False,
                    "why": ("AR6 / §3.2.1 刀锋格字面施于 β 的 Δ；α 用「≤ field_tol」判带，"
                            "0.05 恰在带内 ⇒ 取整档与字面档同档，**对 α 腿结论 0 影响**。"
                            "此处仅披露事实，0 引入新判据、0 新增阈值"),
                } if abs(delta_alpha - FIELD_TOL) < KNIFE_EDGE_LABEL_EPS else None),
                "in_alpha_denominator": alpha_in_denom,
                "denominator_exclusion_reason": (
                    None if alpha_in_denom else
                    "T=1 结构性恒等格（|field_mean(1) − field_mean(1)| ≡ 0 ⇒ 恒判 immune，"
                    "无鉴别力）⇒ 沿 v2 §5.4 单列登记、0 计入 α 腿判定分母；β 腿 T=1 仍为合法格"),
                "values_finite": alpha_vals_ok,
                "computable": bool(alpha_vals_ok and n_items_ok),
            },
            "kou_jing_beta": {
                "definition": "delta = field_mean(T) - max(rule_filter(T), random(T))",
                "value": delta_beta, "value_float_literal": repr(delta_beta),
                "field_tol": FIELD_TOL,
                "band": band_float,
                "band_float_literal": band_float,
                "beta_pass": bool(delta_beta >= FIELD_TOL),
                "is_knife_edge": knife,
                "knife_edge_disclosure": ({
                    "value_float_literal": repr(delta_beta),
                    "value_math_note": "两侧读数落在 0.025 粒度网格上 ⇒ 数学值恰 = 0.05",
                    "band_float_literal": band_float,
                    "band_math_rounded_control_only": band_math,
                    "counted_as": "按 float64 字面档计入档位计数（使计数唯一可复算）",
                    "double_counted": False,
                    "rounded": False,
                    "tolerance_band_used": False,
                } if knife else None),
                "values_finite": beta_vals_ok,
                "computable": bool(beta_vals_ok and n_items_ok),
            },
            "chance_level": CHANCE_LEVEL,
            "n_options_fixed": N_OPTIONS_FIXED,
        })

    # ---- 6. 逐腿落档（§3.3 三态终态表 · AR3 全矩阵同档）----
    alpha_cells = [m for m in matrix if m["kou_jing_alpha"]["in_alpha_denominator"]]
    beta_cells = matrix
    alpha_bands = [m["kou_jing_alpha"]["band"] for m in alpha_cells]
    beta_bands = [m["kou_jing_beta"]["band"] for m in beta_cells]
    alpha_flags = [m["kou_jing_alpha"]["field_immune"] for m in matrix]     # 含 T=1，仅对照

    alpha_uncomputable = [m["cell"] for m in alpha_cells
                          if not m["kou_jing_alpha"]["computable"]]
    beta_uncomputable = [m["cell"] for m in beta_cells
                         if not m["kou_jing_beta"]["computable"]]
    alpha_not_immune = [m["cell"] for m in alpha_cells
                        if m["kou_jing_alpha"]["band"] == "NOT_IMMUNE"]
    beta_below = [m["cell"] for m in beta_cells
                  if m["kou_jing_beta"]["band"] == "BELOW_TOL"]

    def leg_state(uncomputable, fail_cells, n_denom):
        """逐腿三态落档（§3.3）。分母格不可算 ⇒ KD（构造/素材不可算优先，属硬阻断）；
        否则存在异档格 ⇒ FAIL；全档一致 ⇒ PASS。"""
        if uncomputable:
            return "KD"
        if fail_cells:
            return "FAIL"
        return "PASS"

    alpha_state = leg_state(alpha_uncomputable, alpha_not_immune, len(alpha_cells))
    beta_state = leg_state(beta_uncomputable, beta_below, len(beta_cells))

    # 复合 claim 落档（§3.3 复合表）
    compound_covered = True
    if alpha_state == "PASS" and beta_state == "PASS":
        compound_state = "PASS"
    elif alpha_state == "FAIL" or beta_state == "FAIL":
        compound_state = "FAIL"
    elif alpha_state == "KD" and beta_state == "KD":
        compound_state = "KD"
    else:
        # §3.3 复合表未覆盖「PASS+KD / FAIL+KD」混合分支 ⇒ 按 AR5「0 不明收口」落 KD + γ
        compound_state = "KD"
        compound_covered = False

    knife_cells = [m for m in beta_cells if m["kou_jing_beta"]["is_knife_edge"]]

    consistency = {
        "n_cells": len(matrix),
        "alpha_denominator_cells": len(alpha_cells),
        "alpha_denominator_note": "6 seed × T∈{2,3} = 12 格；T=1 结构性恒等格排除（§5.4）",
        "beta_cells": len(beta_cells),
        "alpha_band_counts": {b: alpha_bands.count(b) for b in sorted(set(alpha_bands))},
        "alpha_all_same_band_in_denominator": len(set(alpha_bands)) == 1,
        "alpha_not_immune_cells": alpha_not_immune,
        "alpha_all_T2T3_immune": bool(not alpha_not_immune),
        "beta_band_counts": {b: beta_bands.count(b) for b in sorted(set(beta_bands))},
        "beta_all_same_band": len(set(beta_bands)) == 1,
        "beta_below_tol_cells": beta_below,
        "beta_all_PASS": bool(not beta_below),
        "alpha_flags_incl_T1_control_only": {
            "counts": {str(k): int(v) for k, v in
                       {True: sum(alpha_flags), False: len(alpha_flags) - sum(alpha_flags)}.items()},
            "all_same_flag_incl_T1": len(set(alpha_flags)) == 1,
            "note": "含 T=1 的 α 一致性仅作对照登记，0 参与判定（§5.4）",
        },
        "beta_knife_edge_cells": [{
            "cell": m["cell"],
            "value_float_literal": m["kou_jing_beta"]["value_float_literal"],
            "value_math_note": m["kou_jing_beta"]["knife_edge_disclosure"]["value_math_note"],
            "band_float_literal": m["kou_jing_beta"]["band_float_literal"],
            "is_knife_edge": True,
        } for m in knife_cells],
        "beta_band_counts_if_knife_edge_rounded_CONTROL_ONLY": {
            "PASS": sum(1 for m in beta_cells
                        if m["kou_jing_beta"]["band"] == "PASS"
                        or m["kou_jing_beta"]["is_knife_edge"]),
            "BELOW_TOL": sum(1 for m in beta_cells
                             if m["kou_jing_beta"]["band"] == "BELOW_TOL"
                             and not m["kou_jing_beta"]["is_knife_edge"]),
            "participates_in_judgement": False,
            "note": "沿 v1 既有字段 beta_band_counts_if_knife_edge_rounded 口径；AR6 "
                    "0 参与判定，仅作对照登记",
        },
        "leg_states_mechanical": {
            "alpha_leg": alpha_state, "beta_leg": beta_state,
            "alpha_uncomputable_cells": alpha_uncomputable,
            "beta_uncomputable_cells": beta_uncomputable,
            "precedence_rule_disclosed": (
                "分母格不可算 ⇒ KD 优先（构造/素材不可算属硬阻断，机械优先于档位异同）；"
                "否则异档 ⇒ FAIL；全档一致 ⇒ PASS。§3.3 三态表未明写优先级，"
                "本处为机械优先级的显式披露，0 新增阈值、0 新增数值切点"),
        },
        "compound_claim_state_mechanical": compound_state,
        "compound_table_covered_both_legs": compound_covered,
        "aggregation_note": "α/β 双口径强制并报、0 互替（K-V3R1P1-0-C）；0 合取掩盖任一腿",
    }

    # ---- 7. legacy verdict（既有字面另报，0 并入新面矩阵）----
    legacy = []
    for seed in BANK_SEED_SET_V2:
        acc_by_T = {a: {T: acc[(seed, T)][a] for T in T_LEVELS} for a in ARMS}
        v, detail = R.verdict(acc_by_T)
        legacy.append({"bank_seed": seed, "legacy_verdict": v, "legacy_detail": detail,
                       "legacy_beta_margin_T1": acc_by_T["field_mean"][1] -
                       max(acc_by_T["rule_filter"][1], acc_by_T["random"][1])})

    # ---- 8. 防退化门自证（AR4：门施于读法 D；A / C 双记并报）----
    degen = {
        "rule": "n_distinct > 3 + std > 0（K-V3R1P1-0-A，字面不变）",
        "gate_sequence_frozen": "D",
        "gate_sequence_frozen_basis": "v2 §5.2 / AR4 测量前唯一冻结；D 为 A 的严格超集池化",
        "reading_A_per_domain_item_accuracy": {
            "definition": "每格每臂的 4 个域 item 级正确率序列（n=4/格）",
            "role": "CONTROL_ONLY（AR4：0 再作为判死线分支）",
            "per_cell": {f"seed{c['bank_seed']}_T{c['T']}":
                         {a: series_stats([c["per_domain_accuracy"][d][a]
                                           for d in c["per_domain_accuracy"]])
                          for a in ARMS} for c in cells},
        },
        "reading_B_per_item_correctness": {
            "definition": "每格每臂 40 条 item 级 0/1 正确性序列（n=40/格）",
            "role": "永禁作门序列（结构性二值 ⇒ n_distinct ≤ 2 恒成立，§5.2）",
            "is_binary_by_construction": True,
        },
        "reading_C_cell_level_readout": {
            "definition": "18 格格级读数序列（每臂 n=18）",
            "role": "CONTROL_ONLY（AR4）",
            "per_arm": {a: series_stats([acc[(s, T)][a]
                                         for s in BANK_SEED_SET_V2 for T in T_LEVELS])
                        for a in ARMS},
        },
        "reading_D_matrix_pooled": {
            "definition": "逐臂 × 全矩阵的域级正确率池化序列（4 域 × 18 格 = 72 值/臂）",
            "role": "GATE_SEQUENCE（v2 §5.2 冻结）",
            "per_arm": {a: series_stats([c["per_domain_accuracy"][d][a]
                                         for c in cells
                                         for d in c["per_domain_accuracy"]])
                        for a in ARMS},
        },
    }
    _a_vals = [v for cell in degen["reading_A_per_domain_item_accuracy"]["per_cell"].values()
               for v in cell.values()]
    degen["reading_A_summary"] = {
        "n_cell_arm_series": len(_a_vals),
        "n_pass": sum(1 for v in _a_vals if v["gate_non_degenerate"]),
        "n_fail": sum(1 for v in _a_vals if not v["gate_non_degenerate"]),
        "fail_series": [f"{cell}|{a}" for cell, arms in
                        degen["reading_A_per_domain_item_accuracy"]["per_cell"].items()
                        for a, v in arms.items() if not v["gate_non_degenerate"]],
    }
    degen["reading_A_all_cells_pass"] = bool(degen["reading_A_summary"]["n_fail"] == 0)
    degen["reading_C_all_arms_pass"] = bool(all(
        v["gate_non_degenerate"] for v in degen["reading_C_cell_level_readout"]["per_arm"].values()))
    degen["reading_D_all_arms_pass"] = bool(all(
        v["gate_non_degenerate"] for v in degen["reading_D_matrix_pooled"]["per_arm"].values()))
    degen["cfg_seed_lever"] = cfg_seed_static
    degen["reading_dependence_disclosure"] = (
        "AR4 冻结：门施于读法 D（全矩阵池化，72 值/臂）。读法 A（per-cell 4 域序列）"
        f"{degen['reading_A_summary']['n_fail']}/{degen['reading_A_summary']['n_cell_arm_series']} "
        "条不过门（粒度不匹配：n=4 要 4 值全互异）、读法 C 过门与否见上表 —— "
        "**A / C 事实照旧逐条落盘并随判定披露，0 隐瞒**；但 0 再作为判死线分支，"
        "故「双读并列 ⇒ 不明」路径在本件生效范围内结构性不可达（AR4 + AR5）")
    degen["leg_readout_series_self_check"] = {
        "definition": "α/β 两腿读数序列自身的非退化自证（§5.5）",
        "beta_delta_all_18": series_stats([m["kou_jing_beta"]["value"] for m in beta_cells]),
        "alpha_T2T3_12": series_stats([m["kou_jing_alpha"]["value"] for m in alpha_cells]),
        "note": "n_distinct > 3 + std > 0 ⇒ 逐格判档具备鉴别力（非在常量面上判档）",
    }

    # ---- 9. as-run 环境自证（0 环境漂移，§4.5）----
    as_run = json.load(open(os.path.join(REPO, "results", "deposon_v20_gt2b.json"),
                            encoding="utf-8"))
    recomputed_as_run = {a: {str(T): acc[(AS_RUN_SEED, T)][a] for T in T_LEVELS}
                         for a in ARMS}
    as_run_check = {
        "as_run_bank_seed": as_run["bank_seed"],
        "as_run_accuracy_by_T": as_run["accuracy_by_T"],
        "recomputed_accuracy_by_T_seed20260828": recomputed_as_run,
        "bit_identical": bool(as_run["accuracy_by_T"] == recomputed_as_run),
        "as_run_legacy_verdict": as_run["verdict"],
        "recomputed_legacy_verdict_seed20260828": legacy[0]["legacy_verdict"],
        "T1_beta_margin_as_run_control": T1_CONTROL_MARGIN,
        "T1_beta_margin_recomputed": legacy[0]["legacy_beta_margin_T1"],
        "control_used_as_threshold": False,
    }

    # ---- 10. v1.1 9 格并列双记（AR2：0 用 9 格外推、0 以 9 格代替 18 格裁决）----
    v1 = json.load(open(os.path.join(REPO, "results", "_v3_recheck_35_result_2026_09_27.json"),
                       encoding="utf-8"))
    v1_9 = [{"cell": c["cell"],
             "alpha_value": c["kou_jing_alpha"]["value"],
             "alpha_field_immune": c["kou_jing_alpha"]["field_immune"],
             "beta_value": c["kou_jing_beta"]["value"],
             "beta_band": c["kou_jing_beta"]["band"]}
            for c in v1["matrix_9cells"]]
    v2_by_cell = {m["cell"]: m for m in matrix}
    v1_crosscheck = []
    for c in v1_9:
        m = v2_by_cell.get(c["cell"])
        v1_crosscheck.append({
            "cell": c["cell"],
            "v1_1_beta_value": c["beta_value"],
            "v2_beta_value": (m["kou_jing_beta"]["value"] if m else None),
            "beta_value_identical": bool(m is not None
                                         and m["kou_jing_beta"]["value"] == c["beta_value"]),
            "beta_band_identical": bool(m is not None
                                        and m["kou_jing_beta"]["band"] == c["beta_band"]),
        })
    parallel = {
        "rule": "AR2：v1.1 的 9 格读数原样保留、0 回头改写，与 v2 的 18 格并列双记",
        "v1_1_9cells_readonly_mirror": v1_9,
        "v1_1_9cells_sha12": zt_pre["v1_result_35"]["sha12"],
        "v2_vs_v1_1_overlap_crosscheck": v1_crosscheck,
        "overlap_all_identical": bool(all(x["beta_value_identical"] and x["beta_band_identical"]
                                          for x in v1_crosscheck)),
        "not_used_for_adjudication": True,
        "note": "本字段只作复现性交叉核验（3 既有 seed × 3 T = 9 格），0 用于任何档位裁决",
    }

    # ---- 11. K-V3R-35 (b) 四类触发检测（照旧逐条检测、照旧逐条登记 γ）----
    triggers = {
        "1_仓外只读被拒": {"triggered": not ext_read_ok,
                          "evidence": ext_read_error or "4 件全部可读（只读）"},
        "2_缓存域缺": {"triggered": bool(excluded_domains),
                    "evidence": {"excluded_domains": excluded_domains,
                                 "included_domains": sorted(graphs)}},
        "3_跑不完": {"triggered": bool(len(matrix) != 18
                                or any(not m["n_items_as_expected"] for m in matrix)
                                or alpha_uncomputable or beta_uncomputable),
                  "evidence": {"n_cells_produced": len(matrix), "n_cells_expected": 18,
                               "n_items_mismatched_cells": [m["cell"] for m in matrix
                                                            if not m["n_items_as_expected"]],
                               "uncomputable_cells": sorted(set(alpha_uncomputable)
                                                            | set(beta_uncomputable))}},
        "4_item级正确率_n_distinct<=3退化": {
            "triggered": bool(degen["reading_A_summary"]["n_fail"] > 0),
            "evidence": {"reading_A_n_fail": degen["reading_A_summary"]["n_fail"],
                         "reading_A_n_total": degen["reading_A_summary"]["n_cell_arm_series"]}},
    }
    triggered_four = [k for k, v in triggers.items() if v["triggered"]]
    degen_gate_hit = not degen["reading_D_all_arms_pass"]

    # ---- 12. γ 登记（逐条复核更新，v2 §9）----
    gamma = [
        {"id": "γ-V2-1",
         "item": "v1.1 K-V3R-35 (b) 已触发（读法 A 21/27 不过门）⇒ 旧终态「不明」",
         "v2_status": "历史事实保留、0 删除；终态改由 §3.3 三态表落定",
         "triggered_now": triggers["4_item级正确率_n_distinct<=3退化"]["triggered"],
         "detail": {"reading_A_n_fail": degen["reading_A_summary"]["n_fail"],
                    "reading_A_n_total": degen["reading_A_summary"]["n_cell_arm_series"]}},
        {"id": "γ-V2-2", "item": "另 2 域无 gt2_attacker_cache",
         "v2_status": "待采集（沿 v1.1 事实，0 虚构缓存、0 外推全 6 域）",
         "triggered_now": triggers["2_缓存域缺"]["triggered"],
         "detail": triggers["2_缓存域缺"]["evidence"]},
        {"id": "γ-V2-3", "item": "β 刀锋格",
         "v2_status": "按 AR6 float64 字面档计数；0 round / 0 容差 / 0 双计",
         "triggered_now": bool(knife_cells),
         "detail": {"cells": [m["cell"] for m in knife_cells],
                    "band_counts_literal": consistency["beta_band_counts"],
                    "band_counts_if_rounded_CONTROL_ONLY":
                        consistency["beta_band_counts_if_knife_edge_rounded_CONTROL_ONLY"]}},
        {"id": "γ-V2-4", "item": "T=1 档 as-run 对照边际 +0.025",
         "v2_status": "对照留档，0 作阈值、0 参与判定",
         "triggered_now": True,
         "detail": {"value": T1_CONTROL_MARGIN, "used_as_threshold": False,
                    "used_in_judgement": False}},
        {"id": "γ-V2-5", "item": "corpus 孤儿哨兵在本仓现状抛错",
         "v2_status": "沿 v1 同一等价只读路径；0 改既有模块 / 0 改 index.json / 0 改语料",
         "triggered_now": True,
         "detail": {"orphan_non_graph_json": ["all.json", "index_v2_2026_09_16.json",
                                              "strip_captions_22.json"],
                    "existing_modules_modified": 0, "corpus_files_modified": 0}},
        {"id": "γ-V2-6", "item": "读法 A 不过门（若 PI 坚持 per-cell 门粒度）",
         "v2_status": "默认档 = 读法 D（AR4 / §10 P-2）；PI 改判 ⇒ KD 并 γ",
         "triggered_now": triggers["4_item级正确率_n_distinct<=3退化"]["triggered"],
         "detail": {"default": "D", "reading_A_n_fail": degen["reading_A_summary"]["n_fail"]}},
        {"id": "γ-V2-7", "item": "v2 新增 3 个 seed 的读数本件 0 预测、0 填值",
         "v2_status": "本棒逐格实测落盘；0 以 v1 的 9 格外推新 seed",
         "triggered_now": True,
         "detail": {"new_seeds": list(SEEDS_V2_NEW),
                    "per_cell_readings": {m["cell"]: {
                        "accuracy": m["accuracy"],
                        "alpha": m["kou_jing_alpha"]["value"],
                        "beta": m["kou_jing_beta"]["value"],
                        "beta_band": m["kou_jing_beta"]["band"]}
                        for m in matrix if m["bank_seed"] in SEEDS_V2_NEW}}},
        {"id": "γ-V2-8", "item": "锚件 sha12 漂移（v2 预登记件所记 vs 盘上实测）",
         "v2_status": "如实登记；0 回改既有件、0 以锚值覆盖实测值",
         "triggered_now": zt_pre["v1_result_35"]["sha12"] != "e9aa6e5180ca",
         "detail": {"prereg_v2_claimed_v1_result_sha12": "e9aa6e5180ca",
                    "on_disk_actual_sha12": zt_pre["v1_result_35"]["sha12"],
                    "on_disk_actual_bytes": zt_pre["v1_result_35"]["bytes"],
                    "prereg_v2_claimed_bytes": 34547,
                    "read_policy": "以盘上实测件为只读源；0 修改任何既有件"}},
        {"id": "γ-V2-9", "item": "产物命名与 v2 §4.6 字面的偏离（PI 派工单指定新名）",
         "v2_status": "以 PI 2026-09-29 派工单字面为准（后于 §4.6）；如实登记",
         "triggered_now": True,
         "detail": {"prereg_v2_clause": {
             "executor": "deposon_team/plugins/_v5_item35_v2_matrix_{执行日期}.py",
             "readout": "results/_v5_item35_v2_matrix_{执行日期}.json",
             "report": "results/_v5_item35_v2_rescript_{执行日期}.md"},
             "actually_written": {
                 "executor": "deposon_team/plugins/_v5_item35_v2_matrix_2026_09_29.py",
                 "readout": "results/_v5_item35_v2_matrix_result_2026_09_29.json",
                 "report": "results/_v5_item35_v2_matrix_exec_2026_09_29.md"},
             "nature": "仅命名偏离，0 改任何阈值/判据/口径"}},
        {"id": "γ-V2-10",
         "item": "α 腿读数中出现「数学值恰 = 0.05」型近刀锋值（AR6 刀锋格字面只施于 β）",
         "v2_status": "如实披露；α 判带用「≤ field_tol」⇒ 两种读法同档，0 影响 α 腿结论",
         "triggered_now": any(m["kou_jing_alpha"]["knife_edge_like_label_CONTROL_ONLY"]
                              for m in matrix),
         "detail": {"cells": [m["cell"] for m in matrix
                              if m["kou_jing_alpha"]["knife_edge_like_label_CONTROL_ONLY"]],
                    "rule": "AR6 / §3.2.1 刀锋格字面施于 β 的 Δ；本项 0 扩展该规则的适用范围"}},
    ]

    # ---- 13. 跑后：仓外只读复读 + 0 触动复读 ----
    ext_post = {fn: {"path": os.path.join(EXT_CACHE, fn),
                     "sha12": sha12(os.path.join(EXT_CACHE, fn)),
                     "bytes": nbytes(os.path.join(EXT_CACHE, fn))}
                for fn in EXT_CACHE_ITEMS}
    ext_readonly = {
        "external_archive": "D:/私人资料/_non_upload_local_archive/",
        "items_pre": ext_pre, "items_post": ext_post,
        "pre_post_identical": bool(
            {fn: (v["sha12"], v["bytes"]) for fn, v in ext_pre.items()} ==
            {fn: (v["sha12"], v["bytes"]) for fn, v in ext_post.items()}),
        "copied_into_repo": 0, "wrote_external": False,
        "repo_cache_dir_exists": os.path.exists(os.path.join(REPO, "results",
                                                              "gt2_attacker_cache")),
        "declaration": "只读取用授权：0 复制入仓 / 0 写入 / 0 移出 / 0 删除 / 0 改 ACL",
    }
    zt_post = fingerprint(ZERO_TOUCH)
    zero_touch_evidence = {
        "anchors_pre": zt_pre, "anchors_post": zt_post,
        "all_identical": bool(
            {k: (v["sha12"], v["bytes"]) for k, v in zt_pre.items()} ==
            {k: (v["sha12"], v["bytes"]) for k, v in zt_post.items()}),
        "existing_files_modified": 0,
    }

    # ---- 14. 打包（0 代判：机械落档 ≠ 裁定；裁定权属 verdict-keeper）----
    out = {
        "task": "V5 #35 v2 · GT2b 场免疫性 · 扩矩阵执行面（6 seed × 3 T = 18 格 × α/β 双口径）",
        "date": "2026-09-29",
        "author": "Mavis 团队 worker（agent worker）",
        "prereg_v2": "results/_v5_item35_prereg_v2_2026_09_28.md",
        "prereg_v2_sha12": zt_pre["prereg_v2"]["sha12"],
        "kill_line": ("K-V5R2-35-AR1…AR6 + §3.2.1 刀锋格 + §3.3 三态终态表（生效即锁）；"
                      "field_tol = 0.05 一字不动"),
        "adjudication_ownership": {
            "this_baton": "worker",
            "this_baton_did_not_adjudicate": True,
            "verdict_owner": "verdict-keeper",
            "note": ("本件提供逐格读数 + 逐腿**机械落档**（按 §3.3 表机械求值）；"
                     "claim 级裁定、根因分类、对外表述属 verdict-keeper，本棒 0 代判"),
            "mechanical_state_is_not_verdict": True,
        },
        "frozen_params": {
            "field_tol": FIELD_TOL, "field_tol_unchanged": True,
            "bank_seed_set_v2": list(BANK_SEED_SET_V2),
            "seeds_existing": list(SEEDS_EXISTING), "seeds_v2_new": list(SEEDS_V2_NEW),
            "seed_selection_basis": "连续整数、读数未知前固定（v2 §4.1），0 依既有读数反选",
            "T_levels": list(T_LEVELS), "ARMS": list(ARMS),
            "n_options_fixed": N_OPTIONS_FIXED, "chance_level": CHANCE_LEVEL,
            "n_items_per_map": R.N_ITEMS_PER_MAP,
            "matrix_size": {"seeds": 6, "T": 3, "cells": 18,
                            "alpha_denominator_cells": 12, "beta_cells": 18},
            "config": config_dict(cfg),
            "new_numeric_thresholds_introduced": 0,
        },
        "zero_touch_anchors": zero_touch_evidence,
        "pre_run_selfcheck": pre_run_selfcheck,
        "external_readonly": ext_readonly,
        "assets": {
            "domains_included": sorted(graphs),
            "domains_excluded_no_cache": excluded_domains,
            "traps_available_per_domain": {d: len(t) for d, t in sorted(traps.items())},
            "scope_limit": "仅 4 缓存域；不得外推至全 6 域（v2 §4.3 / §8）",
        },
        "kou_jing_fields": {
            "alpha": "|field_mean(T) - field_mean(T=1)| <= 0.05 ⇒ immune（沿既有字面）",
            "beta": "delta = field_mean(T) - max(rule_filter(T), random(T)); >= 0.05 ⇒ PASS",
            "strongest_opponent_definition": "max(rule_filter(T), random(T))（两对照臂取大）",
            "alpha_beta_not_interchangeable": True,
            "aggregation": "逐腿机械落档 + 计数；0 合取掩盖任一腿（AR3）",
        },
        "matrix_18cells": matrix,
        "consistency": consistency,
        "legacy_verdict_separate": legacy,
        "construct_degen_self_check": degen,
        "as_run_environment_self_check": as_run_check,
        "v1_1_parallel_double_record": parallel,
        "kill_line_b_four_triggers": {
            "rule": "K-V3R-35 (b) 四类触发照旧逐条检测、照旧逐条登记 γ（v2 §3.1 叠加只改终点归属）",
            "per_trigger": triggers,
            "n_triggered": len(triggered_four),
            "triggered_ids": triggered_four,
            "degeneracy_gate_D_hit": degen_gate_hit,
            "terminal_membership": ("KD（判死构造）" if (degen_gate_hit or len(triggered_four) > 0)
                                    else "非门不达分支"),
            "note": ("「不明」在本件生效范围内结构性不可达（AR4 + AR5）；"
                     "触发信息一字不删，终点不再悬置"),
        },
        "root_cause_evidence_for_adjudicator": {
            "note": ("§3.3 要求每条 FAIL 附根因三分类（真证伪/假证伪/混合）。"
                     "根因**分类权属 verdict-keeper**；本棒 0 代判 ⇒ "
                     "root_cause_class 留空，仅提供机械可核证据供其取证"),
            "alpha_fail_cells_mechanical_evidence": {
                "cells": alpha_not_immune,
                "field_mean_by_T_per_seed": {str(s): {str(T): acc[(s, T)]["field_mean"]
                                                     for T in T_LEVELS}
                                             for s in BANK_SEED_SET_V2},
                "note": "T=3 格 field_mean 抬升是 α 腿全部 FAIL 的来源",
            },
            "beta_fail_cells_mechanical_evidence": {
                "cells": beta_below,
                "dominant_source_T": sorted({m["cell"].split("_T")[1]
                                             for m in beta_cells
                                             if m["kou_jing_beta"]["band"] == "BELOW_TOL"}),
                "mechanism_note": ("T=1 档 option 数被 T 个陷阱占位 ⇒ field_mean 相对两对照臂的"
                                   "边际最小；trap 标签不在图节点集内 ⇒ field_mean 对其打 -inf"
                                   "（机制性免疫，run_v20_gt2b.py honesty 字面），"
                                   "故 T=1 的小边际不等价于语义识别能力不足"),
            },
        },
        "gamma_registry": gamma,
        "zero_touch_declaration": {
            "existing_files_modified": 0,
            "runner_modified": False,
            "corpus_or_index_modified": False,
            "derived_json_merged_into_existing": False,
            "llm_calls": 0, "proxy": False, "key_reads": 0,
            "new_thresholds": 0,
        },
        "determinism": "无墙钟时间戳；同输入重跑本 JSON 逐字节一致",
    }
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=False)

    print(json.dumps({
        "out": OUT_PATH,
        "n_cells": len(matrix),
        "alpha_denominator": len(alpha_cells),
        "alpha_leg_mechanical": alpha_state,
        "beta_leg_mechanical": beta_state,
        "compound_mechanical": compound_state,
        "alpha_not_immune_cells": alpha_not_immune,
        "beta_below_tol_cells": beta_below,
        "beta_band_counts": consistency["beta_band_counts"],
        "alpha_band_counts": consistency["alpha_band_counts"],
        "knife_edge_cells": [m["cell"] for m in knife_cells],
        "reading_D_all_pass": degen["reading_D_all_arms_pass"],
        "reading_A_n_fail": degen["reading_A_summary"]["n_fail"],
        "reading_C_all_pass": degen["reading_C_all_arms_pass"],
        "as_run_bit_identical": as_run_check["bit_identical"],
        "v1_overlap_identical": parallel["overlap_all_identical"],
        "zero_touch_all_identical": zero_touch_evidence["all_identical"],
        "ext_readonly_identical": ext_readonly["pre_post_identical"],
        "four_triggers_triggered": triggered_four,
    }, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
