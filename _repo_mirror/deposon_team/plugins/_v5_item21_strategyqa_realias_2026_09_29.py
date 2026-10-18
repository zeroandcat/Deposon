# -*- coding: utf-8 -*-
"""V5 · H2-30 strategyqa「补字段别名后重算」执行棒（面 3 单面，0 扩面）。

授权面（批 11 §2 ㊱，逐字三条硬约束）：
  1. 授权面**仅限「补 `pred` → `predicted` 的字段别名」** ⇒ 0 改算法、0 改判据、0 改读数定义
     （别名是**读取面兼容**，不是测量口径变更）；
  2. 重算范围**仅面 3**（按 benchmark 粒度）⇒ 0 扩到其他面、0 借重算扩面；
  3. 产出落**新名件**；派生 JSON **0 合并**；既有结果 JSON **0 覆写、0 改写**。

实现口径（防「0 改算法」失守的硬措施）：
  * 数值例程 `stats()` / `boot_ci()` 与冻结参数 `N_RESAMPLES` / `SEEDS` **不由本件定义**，
    而是从原 executor `_v3r1p1_21_ktb1_distortion_2026_09_27.py` **按路径只读加载**后
    直接调用 ⇒ 数值代码即原件字节，非本件复写。
  * 唯一增量 = `FIELD_ALIAS = {"pred": "predicted"}` 读取面别名（canonical → 实测名）
    + 读取访问器 `get_field()`；命中审计、公式、bootstrap 抽样、门规则、
    judgment_b / judgment_c 逻辑**逐字沿原件**。
  * **自证**：`--selfcheck-gsm8k` 令同一代码路径在 gsm8k 上跑（gsm8k 无别名命中）
    并与既有结果 JSON 的 gsm8k 条目**逐键比对** ⇒ 别名以外 0 差异为可核事实。

0 LLM / 0 proxy / 0 网络 / 0 key 读取。无墙钟时间戳 ⇒ 同输入重跑逐字节一致。
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import importlib.util
import json
import os
import sys

REPO = r"D:/私人资料/deposon-repo"
ORIG_EXECUTOR = os.path.join(REPO, "deposon_team", "plugins",
                             "_v3r1p1_21_ktb1_distortion_2026_09_27.py")
V19_REL = "results/deposon_v19_benchmark_fixes.json"
PRIOR_RESULT = "results/_v3_recheck_21_result_2026_09_27.json"
SRC_REPORT = "results/_v3_recheck_21_rescript_2026_09_27.md"
B11_REGISTER = "results/_v5_confirm_b11_decisions_register_2026_09_29.md"
PREREG = "results/_v3_recheck_prereg_v1p1_2026_09_27.md"
OUT_PATH = os.path.join(REPO, "results",
                        "_v5_item21_strategyqa_realias_recompute_2026_09_29.json")

# 提案 B 可算性前置四字段（canonical 名，沿原 executor REQUIRED_FIELDS 字面）
REQUIRED_FIELDS = ("predicted", "trap_hit", "n_paths", "n_filtered")

# ★ 授权面唯一增量：canonical 字段名 → 该 benchmark 实测字段名（读取面别名，非口径变更）
#   即「实测 `pred` 的记录按 canonical 名 `predicted` 读出」＝ 批 11 §2 ㊱ 授权字面。
FIELD_ALIAS = {"predicted": "pred"}

MISSING_SENTINEL = "MISSING"   # 沿原 executor L325-326 的缺键哨兵字面

sys.path.insert(0, REPO)
import numpy as np  # noqa: E402


def sha12(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def nbytes(path: str) -> int:
    return os.path.getsize(path)


def load_orig_executor():
    """原 executor **只读取用**加载（importlib 按路径）：复用其 stats / boot_ci / 冻结参数。"""
    spec = importlib.util.spec_from_file_location("_v3r1p1_21_orig", ORIG_EXECUTOR)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)   # 原件 main() 受 __main__ 守卫，本处 0 触发面 1/面 2
    return mod


def get_field(rec: dict, canonical: str):
    """读取面访问器：canonical 名优先，命中别名则取别名键的值。**0 改值、0 转换、0 剔除。**"""
    if canonical in rec:
        return True, rec[canonical]
    alias = FIELD_ALIAS.get(canonical)
    if alias is not None and alias in rec:
        return True, rec[alias]
    return False, MISSING_SENTINEL


def build_arms(e93_bm: dict, e95_bm: dict) -> dict:
    """臂集识别**逐字沿原 executor L269-274**：E9.3 五臂 + E9.5 平铺 ⇒ `rule_baseline`。"""
    arms = {arm: {int(r["id"]): r for r in arr}
            for arm, arr in e93_bm["per_problem"].items()}
    flat = e95_bm["per_problem"]
    flat_arm = "rule_baseline"
    arms[flat_arm] = {int(r["id"]): r for r in flat}
    return arms, flat, flat_arm


def face3_for_benchmark(bm: str, ex: dict, orig, with_alias: bool) -> dict:
    """面 3 单 benchmark 全量指标。`with_alias=False` ⇒ 关别名（对照/自证用）。"""
    stats, boot_ci = orig.stats, orig.boot_ci
    N_RESAMPLES, SEEDS = orig.N_RESAMPLES, orig.SEEDS

    e93 = ex["E9.3_high_couple_fix"]["benchmarks"]
    e95 = ex["E9.5_rule_baseline"]["benchmarks"]
    arms, flat, flat_arm = build_arms(e93[bm], e95[bm])

    def gf(rec, canonical):
        if canonical == "predicted" and not with_alias:
            return (canonical in rec), rec.get(canonical, MISSING_SENTINEL)
        return get_field(rec, canonical)

    implied = sum(1 for r in flat if r["is_correct"]) / len(flat)
    ident = {
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
    }

    # 四字段逐条命中（提案 B 可算性前置，benchmark 粒度）——别名后重数
    hit = {f: sum(1 for ids in arms.values() for r in ids.values() if gf(r, f)[0])
           for f in REQUIRED_FIELDS}
    hit_raw_noalias = {f: sum(1 for ids in arms.values() for r in ids.values()
                              if f in r) for f in REQUIRED_FIELDS}
    computable = all(hit[f] > 0 for f in REQUIRED_FIELDS)

    entry = {
        "benchmark": bm,
        "n_ids": len(next(iter(arms.values()))),
        "arms": sorted(arms),
        "arm_insertion_order": list(arms),
        "flat_arm_identification": ident,
        "prediction_field_name_observed": ("predicted" if "predicted" in flat[0] else "pred"),
        "alias_applied": with_alias,
        "alias_table_canonical_to_observed": dict(FIELD_ALIAS) if with_alias else {},
        "four_field_hits": hit,
        "four_field_hits_without_alias": hit_raw_noalias,
        "computable": computable,
    }
    if not computable:
        entry["verdict"] = "INCOMPUTABLE_GAMMA"
        return entry

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
            series = [1.0 if gf(arms[a1][i], "predicted")[1] !=
                      gf(arms[a2][i], "predicted")[1] else 0.0 for i in common]
            key = f"{a1}|{a2}"
            d_dec[key] = {"point": float(np.mean(series)), "N": N,
                          **{f"seed{s}": boot_ci(series, idx_mats[s]) for s in SEEDS}}
            d_dec_diag[key] = stats(series)
    for a1 in arms:
        series = [1.0 if bool(gf(arms[a1][i], "trap_hit")[1]) else 0.0 for i in common]
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
        "binary_single_column": {
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
        "reading_used": "B-1（本件机械判定沿用读法；门施于指标自身 per-item 序列）",
        "reading_attribution": ("(b) 判据读法归属属 PI 拍板项（批 11 §3 ㊲ H2-31）"
                                "⇒ 本件 0 代裁、0 择一；B-2 读法读数见 reading_B2_arm_level"),
    }

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
        "ci_overlap_note": "面 3 各臂对 95% CI 宽度见 D_dec 条目；"
                           "序稳定 ≠ CI 互不重叠（0 跨面主张）",
    }

    # ---- (b) 读法 B-2（源值序列）· 补充实测，0 计入 judgment_b ----
    # 源件 §3 读法 B-2 字面：门施于**源值序列**（每臂的预测值序列）。
    b2 = {}
    for a1 in arms:
        raw = [gf(arms[a1][i], "predicted")[1] for i in common]
        try:
            st = stats(raw)          # 原件 stats()：float 域算 std
            b2[a1] = {"n": st["n"], "n_distinct": st["n_distinct"], "std": st["std"],
                      "gate_non_degenerate": st["gate_non_degenerate"],
                      "computable": True, "note": "沿原件 stats() 实测"}
        except (TypeError, ValueError) as e:
            nd = len(set(map(repr, raw)))   # 0 编码的纯基数计数（非测量变更）
            b2[a1] = {
                "n": len(raw), "n_distinct": nd, "std": None,
                "gate_non_degenerate": False, "computable": False,
                "distinct_count_method": "repr 级去重计数（0 编码、0 转换）",
                "std_not_computable_reason": (
                    f"源值序列取值域 = {sorted(set(map(repr, raw)))[:6]} 为字符串布尔域；"
                    f"原件 stats() 的 std 定义需 float 域 ⇒ std 不可算（{type(e).__name__}）"),
                "n_distinct_gt_3": bool(nd > 3),
                "first_conjunct_fails": bool(nd <= 3),
                "encoding_invented": False,
                "note": "门规则首个合取项 n_distinct > 3 已不满足 ⇒ 无需 std 即可机械落读；"
                        "0 自创 Yes/No→数值编码（编码即私设读数定义）",
            }
    reading_b2 = {
        "reading": "B-2（源件 §3 读法 B-2：门施于源值序列）",
        "status": "supplementary_measured_not_counted_in_judgment_b",
        "per_arm": b2,
        "n_arms_total": len(b2),
        "n_arms_measurable": sum(1 for v in b2.values() if v["computable"]),
        "n_arms_passing_gate": sum(1 for v in b2.values() if v["gate_non_degenerate"]),
    }

    entry.update({
        "verdict": "COMPUTED",
        "D_dec": d_dec, "D_dec_diag": d_dec_diag,
        "D_trap": d_trap, "D_trap_diag": d_trap_diag,
        "D_flux": d_flux, "D_flux_diag": d_flux_diag,
        "D_flux_arm_level_gap": arm_level_gap,
        "construct_degen_self_check": degen,
        "judgment_b": judgment_b,
        "reading_B2_arm_level": reading_b2,
        "judgment_c": judgment_c,
        "n_common_ids": N,
        "id_sets_identical_across_arms": bool(
            len({tuple(sorted(set(a))) for a in arms.values()}) == 1),
        "predicted_none_records": {
            a: sum(1 for i in common if gf(arms[a][i], "predicted")[1] is None)
            for a in sorted(arms)},
        "none_treatment": ("predicted 为 null 的 item 按字面参与 1[pred_a≠pred_b] 比较"
                           "（null 与数值互异）；0 归一化、0 剔除（剔除即私设）"),
        "missing_key_records": {
            a: sum(1 for i in common if not gf(arms[a][i], "predicted")[0])
            for a in sorted(arms)},
        "prediction_value_domain": {
            a: sorted({repr(gf(arms[a][i], "predicted")[1]) for i in common})[:6]
            for a in sorted(arms)},
    })

    # ---- 并列结构披露（0 改判据、0 改序；仅登记「(c) 满足」的覆盖面边界）----
    pts = collections.Counter(round(v["point"], 12) for v in d_dec.values())
    tied_groups = {p: sorted(k for k, v in d_dec.items() if round(v["point"], 12) == p)
                   for p, c in pts.items() if c > 1}
    entry["tie_structure_disclosure"] = {
        "n_pairs_total": len(d_dec),
        "n_pairs_in_tied_groups": sum(len(v) for v in tied_groups.values()),
        "n_pairs_with_unique_point": len(d_dec) - sum(len(v) for v in tied_groups.values()),
        "tied_groups": tied_groups,
        "order_tiebreak_source": ("源件 order_by 排序键 = (bootstrap 均值, 臂对名字符串) "
                                  "⇒ 点估计完全并列处由**臂对名 tiebreak** 决定次序"),
        "implication_for_criterion_c": (
            "判据 (c) 字面为「全序 3/3 不变」⇒ 机械判定按字面落读；"
            "但绝大多数臂对点估计完全相同 ⇒ 该「稳定」含名 tiebreak 成分，"
            "**不可**据此宣称读数具备鉴别力（0 放宽、0 改判、仅披露）"),
    }

    # ---- 别名后臂归属披露（原 caveat 的「归属不参与任何读数」前提已失效）----
    if ident["identified"] and not ident["identification_unique"]:
        entry["arm_attribution_disclosure_post_alias"] = {
            "issue": ("strategyqa 平铺 E9.5 臂的 `rule_baseline` 标签证据**不唯一**"
                      "（rule_baseline 与 unified 精度同为 0.898989898989899）"),
            "premise_now_void": ("源件/原 executor 的 caveat「该 benchmark 已判不可算 ⇒ "
                                 "归属不参与任何读数」**在别名重算后不再成立**"
                                 "（benchmark 现已 computable）⇒ 如实披露"),
            "arm_label_source": ("沿原 executor L272 硬编码 flat_arm='rule_baseline'；"
                                 "本件 0 改臂名、0 重命名、0 替 PI 裁定归属"),
            "readings_involving_this_arm": {
                "D_dec_pairs": sorted(k for k in d_dec if flat_arm in k.split("|")),
                "D_trap_arm": flat_arm in d_trap,
                "D_flux_computable_arms": sorted(d_flux_diag),
                "note": ("D_flux 唯一可算臂即该归属不唯一的平铺臂 ⇒ D_flux 读数"
                         "完全依赖此归属；0 归因、0 编造归属说明"),
            },
        }
    return entry


def diff_vs_prior(gsm8k_entry: dict, prior_path: str) -> dict:
    """自证：同一代码路径（关别名）在 gsm8k 上的读数 vs 既有结果 JSON 逐键比对。"""
    with open(prior_path, encoding="utf-8") as f:
        prior = json.load(f)["face_3_d_dec"]["per_benchmark"]["gsm8k"]
    keys = ["D_dec", "D_trap", "D_flux", "D_dec_diag", "D_trap_diag", "D_flux_diag",
            "D_flux_arm_level_gap", "four_field_hits", "computable", "n_ids", "arms"]
    out, all_eq = {}, True
    for k in keys:
        eq = json.dumps(gsm8k_entry.get(k), sort_keys=True, ensure_ascii=False) == \
             json.dumps(prior.get(k), sort_keys=True, ensure_ascii=False)
        out[k] = bool(eq)
        all_eq = all_eq and eq
    cb_eq = json.dumps(gsm8k_entry["judgment_c"]["orders_by_seed"], sort_keys=True) == \
        json.dumps(prior["judgment_c"]["orders_by_seed"], sort_keys=True)
    jb_eq = (gsm8k_entry["judgment_b"]["qualifying_count"]
             == prior["judgment_b"]["qualifying_count"])
    return {"compared_keys": out, "judgment_c_orders_equal": bool(cb_eq),
            "judgment_b_qualifying_equal": bool(jb_eq),
            "all_equal": bool(all_eq and cb_eq and jb_eq),
            "prior_gsm8k_n_ids": prior["n_ids"],
            "meaning": ("同一代码路径在 gsm8k（无别名命中）上与既有结果 JSON 逐键相等 "
                        "⇒ 别名之外 0 算法/0 判据/0 读数定义差异（可核自证）")}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=OUT_PATH)
    args = ap.parse_args()

    orig = load_orig_executor()
    with open(os.path.join(REPO, V19_REL), encoding="utf-8") as f:
        v19 = json.load(f)
    ex = v19["experiments"]

    sq = face3_for_benchmark("strategyqa", ex, orig, with_alias=True)
    gsm_noalias = face3_for_benchmark("gsm8k", ex, orig, with_alias=False)
    selfcheck = diff_vs_prior(gsm_noalias, os.path.join(REPO, PRIOR_RESULT))

    inputs = {k: {"path": p, "sha12": sha12(os.path.join(REPO, p)),
                  "bytes": nbytes(os.path.join(REPO, p)), "access": "read_only"}
              for k, p in (("src_report_04f6ecd482b9", SRC_REPORT),
                           ("b11_register", B11_REGISTER),
                           ("prereg_v1p1", PREREG),
                           ("prior_result_354ae9c14fe2", PRIOR_RESULT),
                           ("v19_frozen", V19_REL))}
    inputs["orig_executor"] = {"path": os.path.relpath(ORIG_EXECUTOR, REPO).replace("\\", "/"),
                               "sha12": sha12(ORIG_EXECUTOR),
                               "bytes": nbytes(ORIG_EXECUTOR),
                               "access": "read_only_importlib_reuse_stats_boot_ci"}

    out = {
        "task": "V5 · H2-30 strategyqa 补字段别名（pred → predicted）后面 3 重算",
        "date": "2026-09-29",
        "author": "Mavis 团队 worker（纯执行棒）",
        "authorization": "PI 确认批 11 §2 ㊱（落册册 _v5_confirm_b11_decisions_register_2026_09_29.md）",
        "scope_lock": {
            "authorized_surface": "仅补字段别名 pred → predicted（读取面兼容）",
            "algorithm_changed": False, "criterion_changed": False,
            "reading_definition_changed": False,
            "face": "面 3（按 benchmark 粒度）", "faces_1_2_recomputed": False,
            "face_2_boss_rerun": False, "cross_benchmark_merged": False,
            "benchmark_ordering_comparison_claimed": False,
            "existing_files_modified": 0, "derived_json_merged_into_existing": False,
            "prior_result_json_overwritten": False,
        },
        "frozen_params_inherited_from_orig_executor": {
            "n_resamples": orig.N_RESAMPLES, "seeds": list(orig.SEEDS),
            "repro_tolerance_面2_unused": orig.REPRO_TOL,
            "conservation_tolerance_面1_unused": orig.CONS_TOL,
            "required_fields_canonical": list(REQUIRED_FIELDS),
            "new_thresholds_introduced": 0,
        },
        "definitions_inherited_verbatim": {
            "D_dec": "D_dec(a,b) = (1/N) · Σ_i 1[pred_a(i) ≠ pred_b(i)]",
            "D_trap": "D_trap(a) = (1/N) · Σ_i 1[trap_hit(i) = True]",
            "D_flux": "D_flux(a) = (1/N) · Σ_i |n_filtered(i) − n_paths(i)| / n_paths(i)",
            "bootstrap": "95% percentile，10k resamples，每 seed 共享一份索引矩阵（沿原件）",
        },
        "input_chain": inputs,
        "alias_evidence": {
            "gsm8k_observed_field": "predicted", "strategyqa_observed_field": "pred",
            "uniform_within_strategyqa": True,
            "cross_arm_consistency": "strategyqa 6/6 臂均用 `pred`；gsm8k 6/6 臂均用 `predicted`"
                                    "⇒ 别名无跨臂冲突、无混合命名（0 归因，仅事实登记）",
        },
        "face_3_per_benchmark": {"strategyqa": sq},
        "algorithm_fidelity_selfcheck_gsm8k": selfcheck,
        "zero_touch_declaration": {
            "existing_files_modified": 0, "derived_json_merged_into_existing": False,
            "llm_calls": 0, "proxy": False, "network_calls": 0, "key_reads": 0,
            "external_archive_touched": False,
        },
        "verdict_boundary": ("本件 0 判档位、0 代裁 (b) 读法归属（属 verdict-keeper / PI）；"
                             "0 跨 benchmark 合并、0 跨 benchmark 比大小"),
        "determinism": "无墙钟时间戳；同输入重跑本 JSON 逐字节一致",
    }
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=False)

    print(json.dumps({
        "out": args.out,
        "strategyqa_verdict": sq["verdict"],
        "computable": sq["computable"],
        "four_field_hits": sq["four_field_hits"],
        "four_field_hits_noalias": sq["four_field_hits_without_alias"],
        "n_common_ids": sq.get("n_common_ids"),
        "arm_pairs": len(sq.get("D_dec", {})),
        "judgment_b": {k: sq["judgment_b"][k] for k in
                       ("qualifying_count", "pass", "alert_hit")},
        "reading_B2_arms_passing": sq["reading_B2_arm_level"]["n_arms_passing_gate"],
        "reading_B2_arms_measurable": sq["reading_B2_arm_level"]["n_arms_measurable"],
        "judgment_c": {k: sq["judgment_c"][k] for k in
                       ("orders_identical_3of3", "pass", "n_pairwise_comparisons",
                        "n_agreements_all3seeds")},
        "selfcheck_all_equal": selfcheck["all_equal"],
        "predicted_none": sq["predicted_none_records"],
    }, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
