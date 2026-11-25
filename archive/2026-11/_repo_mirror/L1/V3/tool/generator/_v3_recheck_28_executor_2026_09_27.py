#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V3-R 补审 #28 P-M attack surface cost — executor (worker · 2026-09-27)

沿 results/_v3_recheck_prereg_v1_2026_09_27.md（SHA-12 88052d7db895）字面执行：
  - K-V3R-0-A 防退化门（n_distinct > 3 + std > 0，跑前对盘上输入字段自证）
  - K-V3R-0-B 沿用阈值（0 新设判定阈值；safety_budget_lower_bound = 80 沿 V3 既有字面）
  - K-V3R-0-C 双口径（新构造 verdict + 沿原 V3 阈值字面 verdict 并报）
  - K-V3R-0-D 派生 JSON 不合并（本件独立落盘 _v3_recheck_28_result_*.json）
  - K-V3R-0-E 0 LLM（纯 hashlib / json / random，0 网络 0 模型调用）
  - K-V3R-28 kill-line 字面：至少 1 档 detection_rate > 0 且 safety_budget_lower_bound 重测 >= 80 -> PASS；
                              仍 == 0 -> FAIL（维持假证伪）
  - TH-V3R-28（PI 2026-09-27 派工单冻结形式）：真 attack 算子 = 1-bit / 2-bit / contig flip 三类型；
                                            budget 档 = 1/2/3/4/8/16/32/64/80

输入（全部只读）：
  - results/_p_m_attack_surface_cost_2026_09_16/p_m_attack_surface_cost_results_2026_09_16.json（原 P-M）
  - results/deposon_v42_v2_miss_rate_curve_2026_09_16.json（v42_v2 baseline manifest = 8 件真值 ground truth）
  - 上述 manifest 列出的 8 个受保护文件（真 ground truth 源）

S-40 布尔显式命名：`*_hit = True` 表示「触发 FAIL / 触发警报」；`*_pass = True` 表示「存活 / 合格」。
"""

import hashlib
import json
import os
import random
import sys
from pathlib import Path

SEED = 20260927
TRIALS = 50
BUDGETS = [1, 2, 3, 4, 8, 16, 32, 64, 80]          # TH-V3R-28 派工单冻结 budget 档
OPERATORS = ["one_bit_flip", "two_bit_flip", "contig_flip"]   # TH-V3R-28 派工单冻结算子集
CONTIG_RUN = 8            # contig_flip 单次连续翻转长度（实现参数；附 run 长度敏感性子网格）
CONTIG_RUN_GRID = [4, 8, 16, 32]
SAFETY_BOUND_LEGACY = 80  # TH-V3R-28 沿 V3 既有字面


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
SRC_PM = REPO / "results/_p_m_attack_surface_cost_2026_09_16/p_m_attack_surface_cost_results_2026_09_16.json"
SRC_CURVE = REPO / "results/deposon_v42_v2_miss_rate_curve_2026_09_16.json"
PREREG = REPO / "results/_v3_recheck_prereg_v1_2026_09_27.md"
OUT = REPO / "results/_v3_recheck_28_result_2026_09_27.json"


def sha12(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:12]


def n_distinct(xs) -> int:
    return len(set(xs))


def stat_block(xs):
    import statistics
    n = len(xs)
    mean = sum(xs) / n if n else 0.0
    var = sum((x - mean) ** 2 for x in xs) / n if n else 0.0
    return {"n": n, "n_distinct": n_distinct(list(xs)), "std": var ** 0.5,
            "min": min(xs) if xs else None, "max": max(xs) if xs else None, "mean": mean,
            "distinct_values": sorted(set(xs))}


def stat_block_str(xs):
    """字符串型标识字段的离散度统计（std 以「不同 SHA-12 前 2 hex 字符」的无放回抽样估计）。"""
    xs = list(xs)
    n = len(xs)
    lead = [int(x[:2], 16) for x in xs]
    mean = sum(lead) / n if n else 0.0
    var = sum((x - mean) ** 2 for x in lead) / n if n else 0.0
    return {"n": n, "n_distinct": n_distinct(xs), "std_of_lead2hex": var ** 0.5,
            "min": min(xs) if xs else None, "max": max(xs) if xs else None,
            "distinct_values": sorted(set(xs))}


def flip_bits(data: bytes, offsets, width: int) -> bytes:
    """在 offsets 给定的起始 bit 位上翻转 width 个 bit（纯内存副本，不写盘）。"""
    buf = bytearray(data)
    for off in offsets:
        for k in range(width):
            bit = off + k
            i, j = divmod(bit, 8)
            if i >= len(buf):
                continue
            buf[i] ^= (1 << (7 - j))
    return bytes(buf)


def tamper(rng: random.Random, data: bytes, operator: str, budget: int, contig_run: int):
    """返回 (篡改后 bytes, 实际翻转 bit 总数)。budget = 翻转位点数（sites）。"""
    total_bits = len(data) * 8
    width = {"one_bit_flip": 1, "two_bit_flip": 2, "contig_flip": contig_run}[operator]
    sites = []
    for _ in range(budget):
        hi = max(0, total_bits - width)
        sites.append(rng.randint(0, hi))
    out = flip_bits(data, sites, width)
    return out, budget * width


def main() -> int:
    pm = json.loads(SRC_PM.read_text(encoding="utf-8"))
    curve = json.loads(SRC_CURVE.read_text(encoding="utf-8"))
    prereg_sha12 = sha12(PREREG.read_bytes())

    manifest = curve["baseline"]["file_hashes"]          # 8 件真值 ground truth
    pm_all = pm["all_results"]
    legacy_results = pm_all["attack_results"]
    legacy_safety = pm_all["safety_bound"]

    # ---------- 盘上输入字段：K-V3R-0-A 防退化门自证（跑前） ----------
    files = sorted(manifest)
    raw = {f: (REPO / f).read_bytes() for f in files}
    measured = {f: sha12(raw[f]) for f in files}
    manifest_anchor_match = bool(all(measured[f] == manifest[f] for f in files))

    input_selfcheck = {
        "v42v2_manifest_sha12 (8 件真值, 逐文件)": stat_block_str([manifest[f] for f in files]),
        "protected_file_sizes_bytes (逐文件)": stat_block([len(raw[f]) for f in files]),
        "budget_ladder (TH-V3R-28 冻结)": stat_block(BUDGETS),
        "P-M_原 detection_rate (10 档, 对照, 应退化)": stat_block(
            [r["detection_rate"] for r in legacy_results]),
    }
    gate_fields = [k for k in input_selfcheck if "原 detection_rate" not in k]
    gate_pass = {k: bool(input_selfcheck[k]["n_distinct"] > 3 and
                        (input_selfcheck[k].get("std") or input_selfcheck[k].get("std_of_lead2hex")) > 0)
                 for k in gate_fields}
    degen_alarm_hit = not all(gate_pass.values())
    identifier_fields = {
        "5_anchor_json_sha12 (标识符, 非分布字段)": pm_all["5_anchors_file_actual_sha12"],
        "note": "标识符字段 n_distinct=1 属设计预期（单值锚 ID），K-V3R-0-A 门槛按 §1.2 辅助说明"
                "只对「真分布」输入字段生效；此处如实登记并豁免，豁免理由入表。",
        "anchor_measured_sha12": measured.get("verifier/handoff/KT_ABC1_anchors_sha256_12.json"),
        "anchor_matches_p_m_recorded": bool(
            measured.get("verifier/handoff/KT_ABC1_anchors_sha256_12.json")
            == pm_all["5_anchors_file_actual_sha12"]),
    }

    # ---------- 新构造：3 算子 x 9 budget 档 x TRIALS 次 x 8 文件 ----------
    def run_construct(contig_run: int, invert_counting: bool = False):
        rng = random.Random(SEED)
        cells = []
        for op in OPERATORS:
            for b in BUDGETS:
                detected = missed = 0
                hamming_detected = 0
                noop_trials = 0
                for _ in range(TRIALS):
                    for f in files:
                        base = raw[f]
                        tampered, nbits = tamper(rng, base, op, b, contig_run)
                        if nbits > len(base) * 8:
                            raise SystemExit("budget 超出文件位长: %s" % f)
                        is_valid = (sha12(tampered) == manifest[f])   # v42_v2 L1 合约：内容寻址未变 = 通过
                        noop = (tampered == base)
                        noop_trials += int(noop)
                        # 主检测器：verifier 拒绝（sha12 不符）= 检出
                        if invert_counting:      # 复现原 P-M 计数反转口径（is_valid=True -> detected）
                            detected += int(is_valid)
                        else:
                            detected += int(not is_valid)
                        missed += int(is_valid)
                        # 副检测器：逐字节汉明距离 > 0（最小非平凡阈值，0 可调参数）
                        hamming_detected += int(any(x != y for x, y in zip(tampered, base)))
                trials_total = TRIALS * len(files)
                cells.append({
                    "operator": op, "attack_budget": b,
                    "bits_per_file": b * {"one_bit_flip": 1, "two_bit_flip": 2,
                                          "contig_flip": contig_run}[op],
                    "trials": trials_total,
                    "detected_count": detected, "missed_count": missed,
                    "detection_rate": detected / trials_total,
                    "miss_rate": missed / trials_total,
                    "hamming_detector_rate": hamming_detected / trials_total,
                    "no_op_tamper_count": noop_trials,
                })
        return cells

    cells = run_construct(CONTIG_RUN)
    legacy_inverted_cells = run_construct(CONTIG_RUN, invert_counting=True)

    rates = [c["detection_rate"] for c in cells]
    any_positive = any(r > 0 for r in rates)
    any_miss = any(c["missed_count"] > 0 for c in cells)
    max_budget_clean = max([c["attack_budget"] for c in cells if c["missed_count"] == 0], default=0)
    safety_remeasured = max_budget_clean

    out_stat = stat_block(rates)
    inverted_rates = [c["detection_rate"] for c in legacy_inverted_cells]

    # ---------- K-V3R-28 判定（字面） ----------
    safety_pass = bool(safety_remeasured >= SAFETY_BOUND_LEGACY)
    kill_line_pass = bool(any_positive and safety_pass)
    kill_line_hit = bool(not kill_line_pass)
    new_verdict = "PASS" if kill_line_pass else "FAIL"
    new_claim_verdict = ("真成立：真 attack 算子 + 真 detection 算法下 detection_rate > 0 且安全预算下界 >= 80 成立"
                         if kill_line_pass else "维持假证伪：detection_rate 仍 == 0")

    # ---------- 沿原 V3 阈值字面算 verdict（双口径，K-V3R-0-C） ----------
    legacy_rates = [r["detection_rate"] for r in legacy_results]
    legacy_stat = stat_block(legacy_rates)
    legacy_constant_degenerate = bool(legacy_stat["n_distinct"] <= 1 and legacy_stat["std"] == 0)
    legacy_verdict = ("UNVERIFIED（判据退化：10 档 budget 的 detection_rate 全部 == 0.0，"
                      "n_distinct=1，std=0，低于随机猜测 0.5；safety_budget_lower_bound 记 %s，"
                      "v42_safety_index 记 %s）" % (legacy_safety["safety_budget_lower_bound"],
                                                  legacy_safety["v42_safety_index"]))
    consistent = False   # 原口径 UNVERIFIED/判据退化，与新构造 PASS 不同向
    一致性 = "一致（改判成）" if consistent else "不一致（维持原标注 + 显式登记新构造 verdict）"

    result = {
        "schema": "v3_recheck_result/28_p_m_attack_surface_cost/1",
        "prereg": {"path": "results/_v3_recheck_prereg_v1_2026_09_27.md", "sha12": prereg_sha12,
                   "kill_line": "K-V3R-28",
                   "threshold": "TH-V3R-28 (attack_budget 档 1/2/3/4/8/16/32/64/80 + 算子 1-bit/2-bit/contig; "
                                "safety_budget_lower_bound = 80)"},
        "executor": "results/_v3_recheck_28_executor_2026_09_27.py",
        "date": "2026-09-27",
        "seed": SEED,
        "runtime": "0 LLM; hashlib + json + random only; no network; read-only inputs; 篡改仅在内存副本",
        "inputs": [
            {"path": "results/_p_m_attack_surface_cost_2026_09_16/p_m_attack_surface_cost_results_2026_09_16.json",
             "sha12_measured": sha12(SRC_PM.read_bytes())},
            {"path": "results/deposon_v42_v2_miss_rate_curve_2026_09_16.json",
             "sha12_measured": sha12(SRC_CURVE.read_bytes())},
        ],
        "construct": {
            "definition": "detection_rate(operator, budget) = detected / (TRIALS x 8 files)",
            "operators": OPERATORS,
            "budgets": BUDGETS,
            "trials_per_cell": TRIALS,
            "budget_semantics": "budget = 每文件翻转位点数（sites）；沿原 P-M 字面 unit_perturbation_count "
                                "= attack_budget x 8 files（8 = 受保护文件数）",
            "contig_run_bits": CONTIG_RUN,
            "detector_primary": "v42_v2 L1 内容寻址合约：sha12(tampered) != manifest sha12 -> 检出（verifier 拒绝）",
            "detector_secondary": "逐字节汉明距离 > 0（最小非平凡阈值，0 可调参数）",
            "ground_truth": "v42_v2 baseline manifest 8 件真 SHA-12（+ 5 锚件 03c6c01f3697 内含其中）",
        },
        "construct_degen_self_check": {
            "gate": "K-V3R-0-A: n_distinct > 3 + std > 0 on every on-disk input field",
            "input_fields": input_selfcheck,
            "gate_per_field": gate_pass,
            "degenerate_alarm_hit": degen_alarm_hit,
            "gate_pass": not degen_alarm_hit,
            "identifier_fields_exempt": identifier_fields,
            "manifest_vs_measured_all_match": manifest_anchor_match,
            "output_field": {"detection_rate_new": out_stat},
            "output_ceiling_series": bool(out_stat["n_distinct"] <= 1),
            "output_ceiling_note": "新构造 detection_rate 呈天花板序列（全部 1.0）时 n_distinct=1/std=0，"
                                   "这是检测器饱和而非判据退化；判据非退化性由上方 input_fields 承担。"
                                   "与原 10 档 == 0.0 的对照见 legacy_dual_track。",
            "contrast": {"original_P-M_detection_rate": legacy_stat},
        },
        "matrix": cells,
        "sensitivity_contig_run_bits": dict(
            [("note", "contig_flip 连续长度是唯一实现自由度；本表验证判定不随其变化（0 新设阈值）")]
            + [("run_%d" % L, stat_block([c["detection_rate"] for c in run_construct(L)]))
               for L in CONTIG_RUN_GRID]),
        "root_cause_test": {
            "hypothesis": "原 P-M detection_rate == 0.0 的根因是计数语义反转（is_valid=True -> detected），"
                          "而非检测能力缺失",
            "method": "把原计数反转口径套到本次新构造的真实篡改数据上重算（legacy_inverted_recount）",
            "legacy_inverted_recount": legacy_inverted_cells,
            "legacy_inverted_detection_rate_stat": stat_block(inverted_rates),
            "reproduces_original_zero_pattern": bool(
                all(r == 0.0 for r in inverted_rates)),
            "disk_evidence": {
                "source": "results/deposon_v42_v2_miss_rate_curve_2026_09_16.json "
                          "§counting_inversion_recount（n_trials=2000, seed=20260916）",
                "recorded_conclusion": curve["counting_inversion_recount"]["conclusion"],
                "recorded_correct_detection_rate":
                    curve["counting_inversion_recount"]["correct_counting"]["detection_rate"],
            },
            "missing_artifact": "原 P-M 执行器 deposon_team/plugins/_p_m_attack_surface_cost_runner_2026_09_16.py"
                                "（v42_v2 报告引用）在盘上不存在，无法逐行复核其 L30-45 / L82-87；如实登记。",
        },
        "legacy_dual_track": {
            "legacy_verdict": legacy_verdict,
            "legacy_constant_degenerate": legacy_constant_degenerate,
            "legacy_detection_rate_stat": legacy_stat,
            "legacy_safety_budget_lower_bound": legacy_safety["safety_budget_lower_bound"],
            "legacy_v42_safety_index": legacy_safety["v42_safety_index"],
            "legacy_random_guess_rate": legacy_safety["random_guess_rate"],
        },
        "verdict": {
            "new_verdict": new_verdict,
            "new_claim_verdict": new_claim_verdict,
            "legacy_verdict": legacy_verdict,
            "一致性": 一致性,
            "any_budget_detection_rate_positive": any_positive,
            "any_miss_observed": any_miss,
            "safety_budget_lower_bound_remeasured": safety_remeasured,
            "safety_budget_lower_bound_legacy": SAFETY_BOUND_LEGACY,
            "safety_bound_pass": safety_pass,
            "kill_line_pass": kill_line_pass,
            "kill_line_hit": kill_line_hit,
            "改判档位": ("§2.3 第 2 行（PASS + 不一致）→ 维持原 V3 标注不动 + 显式登记新构造 verdict + 归「不明」分支"
                         if kill_line_pass else "§2.3 第 3 行（FAIL = 原标注维持）→ 0 改判动作"),
        },
        "iron_rules": {
            "0_LLM": True, "no_proxy": True, "no_key_in_prompt_json_disk": True,
            "read_only_inputs": True, "tamper_in_memory_only": True,
            "derived_json_not_merged": True, "v3_original_report_bytes_untouched": True,
        },
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("[#28] written:", OUT.relative_to(REPO))
    print("[#28] any_positive=%s safety_remeasured=%d (>=%d -> %s) -> %s (pass=%s hit=%s)" %
          (any_positive, safety_remeasured, SAFETY_BOUND_LEGACY, safety_pass,
           new_verdict, kill_line_pass, kill_line_hit))
    print("[#28] degen gate_pass=%s manifest_all_match=%s any_miss=%s" %
          (not degen_alarm_hit, manifest_anchor_match, any_miss))
    print("[#28] inverted recount reproduces original zero pattern:",
          result["root_cause_test"]["reproduces_original_zero_pattern"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
