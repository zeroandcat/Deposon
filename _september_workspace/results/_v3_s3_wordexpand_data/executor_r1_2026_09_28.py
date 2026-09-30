#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V3-S S3 段 executor · **r1 修正版**（loader_r1 修复 + 覆盖率重算）· worker 出件 · 2026-09-28

========================================================================
r1 修正版登记（2026-09-28 · worker 执行类 · PI 2026-09-28 拍板「T-S3-2 loader 按 F1 先例直修」）
========================================================================
母件: results/_v3_s3_wordexpand_data/executor_2026_09_28.py
      SHA-12 = 80f1445ce45d / 46,005 B（母件 0 字节改动，本件为其派生修正件）
本件: results/_v3_s3_wordexpand_data/executor_r1_2026_09_28.py（新名，不覆盖母件）
落盘: results/_v3_s3_wordexpand_recheck_r1_2026_09_28.json（派生 JSON 独立，0 合并既有 result）

【缺陷面（母件登记 S3-F1，源头 = v3 executor load_addendum_event_v3）】
宿主件: results/_v4_pi_cot_v3_ruleset_v3_executor.py
      SHA-12 = 8a81d90c69ba / 58,794 B（只读，0 触动）
  母件第 775-788 行 reasoning_full 装载 if/elif 链：
      第 775 行 = if "reasoning_full" in sup and sup["reasoning_full"]:   （排他 if 链首项）
      第 777-778 行 = critical_reflection_supplement 拼接**嵌套在首项内部**
      第 783-788 行 = elif disposition_text / elif other_text / else ""  （并列兜底分支）
  ⇒ D1 addendum 3 件**只有 critical_reflection_supplement、无 reasoning_full 字段**
    ⇒ supplement 无任何拼接入口 → 落 else: "" 被静默丢弃（0 报错 / 0 告警 / 0 计数）
  ⇒ S3 扩词段母件经 `V3.load_all_events_v3()` 装载同一 loader ⇒ idx 37 / 38 / 39
    的盘上批判反思文本**从未进入** ev["reasoning_full"] ⇒ 覆盖率被系统性低估。

【本件修法（沿 F1 先例同款处方）】
先例件: results/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py
      SHA-12 = ee8671a28c2f / 62,115 B（V3 期 F1 已拍板直修件，只读引用，0 改动）
  先例处方 = 「拼接入口由『嵌套于排他 if 链首项』提为『base 已定后全分支统一后置追加』」
  本件修法 = **只切换装载面引用**（本件事件构造面 = 先例 r1 executor，母件 v3 executor
  仅作「修复前」对照臂读数用），**0 改词表 / 0 改阈值 / 0 改特征 / 0 改判定公式 / 0 改 seed /
  0 改 held-out 划分 / 0 改 ALT 口径定义 / 0 改 per_event 标签来源**。
  语义等价性：先例 r1 修法在 base 非空时输出逐字不变 = base + " " + supplement；
  本件不复制先例修法代码，只引用先例件（避免同一修法两份实现漂移）。

【本件读数口径（诚实边界，防误读）】
  - per_event 的 pred / actual / divergent **沿 result_v3 登记值**（只读），
    **0 重训决策树** ⇒ 本件覆盖率重算只反映 reasoning_full 面变化，
    **不反映「若重训、pred 会否变化」**（该面属未评估项，见 open_items）。
  - ALT 口径沿 S3 母件**显式定义**（主 held-out 23 剔 correction 子集 = 18 件），
    **不静默沿用 v3 登记的不可复现 ALT 值**（T-S3-4 仍挂 PI）。
  - 词表：**36 词原口径照常判 K-V3S-3-4**（沿 prereg §2.3 字面）；
    PI 2026-09-28 拍板「39 词部分入锁」（推翻 / 冲突 / 庖丁解牛 入锁；非 / 小是具体 出锁）
    本件落盘为 `locked_pending_effective`（待生效锁）⇒ **只报读数，0 判**。

铁律（严守）:
  - 0 LLM / 0 proxy / 0 gateway；key 永不明文（不落盘 / 不入 prompt / JSON / log）
  - 判死线 0 私设 / 0 擅调（K-V3S-3-4 沿 1.00；跨日 5 / 单日 0.60 / N≥50 + 纠正≥5 一字不动）
  - 显式布尔命名（S-40）：`*_hit = true` = 触发 FAIL 方向；`*_ok = true` = 达标方向
  - SHA-12 = hashlib.sha256(全文字节).hexdigest()[:12] 小写
  - 派生 JSON 独立落盘，0 合并任何既有 result JSON
  - 既有件 0 触动（母件 / 宿主件 / 先例件 / dataset / result / verdict 全部只读）
  - 时间戳冻结（re-entrancy-safe，逐字可重跑）

依据（纪律锚，全部只读）:
  - results/_v3_s_prereg_v1_2026_09_27.md (ef5a40554960) §2.3 K-V3S-3-1..3-4 + §2.6 P-S3-1
  - results/_v4_pi_cot_v3_ruleset_v3_executor.py (8a81d90c69ba) —— 修复前对照臂 loader
  - results/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py (ee8671a28c2f) —— 修复臂 loader（F1 先例）
  - results/_v3_s3_wordexpand_data/executor_2026_09_28.py (80f1445ce45d) —— 母件计算面（只读复用）
  - results/_v3_s3_wordexpand_data/result_2026_09_28.json (f7f6d875d73a) —— 上游扩词段读数 + loader_drop_finding
  - results/_v4_pi_cot_v3_result_v3.json (585714f9660c) —— per_event 标签 + held_out_idx + missing_events_ledger
  - docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md §22.31.1 E-42.1（死因改判：idx 37/39 系装载缺陷）

末行署名: Mavis 团队 worker 出件 | 2026-09-28
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

import numpy as np

# ---------------------------------------------------------------------------
# 0. 路径 / 锚 / 冻结常量
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
RESULTS_DIR = REPO_ROOT / "results"
OUT_DIR = RESULTS_DIR / "_v3_s3_wordexpand_data"

PREREG_S = RESULTS_DIR / "_v3_s_prereg_v1_2026_09_27.md"
PREREG_S_SHA12_EXPECTED = "ef5a40554960"

# 修复前对照臂（缺陷宿主件，只读）
V3_EXECUTOR_BEFORE = RESULTS_DIR / "_v4_pi_cot_v3_ruleset_v3_executor.py"
V3_EXECUTOR_BEFORE_SHA12_EXPECTED = "8a81d90c69ba"

# 修复臂（F1 先例直修件，只读引用，0 改动、0 复制修法代码）
V3_EXECUTOR_AFTER = RESULTS_DIR / "_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py"
V3_EXECUTOR_AFTER_SHA12_EXPECTED = "ee8671a28c2f"

# 母件（S3 扩词段计算面，只读复用 coverage_on / blind_obey_on / has_critical_custom）
S3_EXECUTOR_MOTHER = OUT_DIR / "executor_2026_09_28.py"
S3_EXECUTOR_MOTHER_SHA12_EXPECTED = "80f1445ce45d"

S3_RESULT_MOTHER = OUT_DIR / "result_2026_09_28.json"
S3_RESULT_MOTHER_SHA12_EXPECTED = "f7f6d875d73a"

V3_RESULT = RESULTS_DIR / "_v4_pi_cot_v3_result_v3.json"
V3_RESULT_SHA12_EXPECTED = "585714f9660c"

ADDENDUM_D1 = RESULTS_DIR / "_v4_pi_cot_v2_dataset_addendum_2026_09_24.json"
ADDENDUM_D1_SHA12_EXPECTED = "172093a23e4b"

VERDICT_V3 = RESULTS_DIR / "_v4_pi_cot_v3_verdict_v3.md"

OUT_RESULT = RESULTS_DIR / "_v3_s3_wordexpand_recheck_r1_2026_09_28.json"

TS_FROZEN = "2026-09-28T14:40:00+08:00"
DATE_FROZEN = "2026-09-28"

# ---------------------------------------------------------------------------
# 判死线（全部沿既有件字面, 0 自创, 0 擅调）
# ---------------------------------------------------------------------------
TH_CRITICAL_COV = 1.00       # K-V3S-3-4 沿 K-V3-B / TH-v2-5b 字面
TH_CROSS_DAYS = 5           # K-V3S-3-1 沿 verdict_v3 §3.3 字面
TH_SINGLE_DAY_RATIO = 0.60  # K-V3S-3-2 沿 TH-v2-3 / TH-v3-3 字面
TH_N_MIN = 50               # K-V3S-3-3 沿 TH-v2-1 / TH-v3-1 字面
TH_N_CORRECTION = 5         # K-V3S-3-3 沿 TH-v2-2 / TH-v3-2 字面
SEED = 42                   # TH-v3-15
HELD_OUT_RATIO = 0.30       # TH-v3-4

# ---------------------------------------------------------------------------
# PI 2026-09-28 拍板词表（39 词部分入锁）
#   入锁 3 词: 推翻 / 冲突 / 庖丁解牛（源 = S3 扩词段实测面）
#   出锁 2 词: 非（单字过宽，命中「非欧几何」idx 25）/ 小是具体（0 边际增益）
#   lock_status = locked_pending_effective（待生效锁）⇒ 只报读数, 0 判
# ---------------------------------------------------------------------------
LOCKED_IN_WORDS: Tuple[str, ...] = ("推翻", "冲突", "庖丁解牛")
LOCKED_OUT_WORDS: Tuple[str, ...] = ("非", "小是具体")
LOCK_STATUS = "locked_pending_effective"

KILL_LINES_S3 = [
    {
        "id": "K-V3S-3-1",
        "name": "跨日天数达标线",
        "rule": "distinct calendar days >= 5",
        "threshold": TH_CROSS_DAYS,
        "threshold_source": "verdict_v3 §3.3 字面 (PI 2026-09-27 拍板值)",
        "hit_direction": "跨日 < 5 天即不达标 (ok=False)",
        "boolean_field": "k_v3s_3_1_ok",
    },
    {
        "id": "K-V3S-3-2",
        "name": "单日占比达标线",
        "rule": "单日最大占比 <= 0.60",
        "threshold": TH_SINGLE_DAY_RATIO,
        "threshold_source": "TH-v2-3 / TH-v3-3 字面 0.60",
        "hit_direction": "单日占比 > 0.60 即不达标 (ok=False)",
        "boolean_field": "k_v3s_3_2_ok",
    },
    {
        "id": "K-V3S-3-3",
        "name": "样本量 + 纠正事件达标线",
        "rule": "N >= 50 且 纠正/反转事件 >= 5",
        "threshold": [TH_N_MIN, TH_N_CORRECTION],
        "threshold_source": "TH-v2-1/2 = TH-v3-1/2 字面",
        "hit_direction": "任一不达即不达标 (ok=False)",
        "boolean_field": "k_v3s_3_3_ok",
    },
    {
        "id": "K-V3S-3-4",
        "name": "批判覆盖双口径线（判定面命中线）",
        "rule": "原 36 词 coverage 与入锁后 N 词 coverage 两者并报, 判定沿 1.00",
        "threshold": TH_CRITICAL_COV,
        "threshold_source": "1.00 沿 K-V3-B / TH-v2-5b 字面",
        "hit_direction": "任一口径 coverage < 1.00 即触发 (hit=True)",
        "boolean_field": "k_v3s_3_4_hit",
    },
]


def sha12_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# 只读装载三件（0 字节改动）
V3_BEFORE = _load_module("v3_executor_before_s3r1", V3_EXECUTOR_BEFORE)
V3_AFTER = _load_module("v3_executor_after_s3r1", V3_EXECUTOR_AFTER)
S3 = _load_module("s3_wordexpand_mother_s3r1", S3_EXECUTOR_MOTHER)

# 母件计算面原语（逐字复用，0 复制实现 → 口径不会漂移）
has_critical_custom = S3.has_critical_custom
coverage_on = S3.coverage_on
blind_obey_on = S3.blind_obey_on


# ---------------------------------------------------------------------------
# 1. 主流程
# ---------------------------------------------------------------------------
def main() -> Dict[str, Any]:
    # --- 1.1 输入链 SHA-12 核验（先核后用，只读）---
    inputs_meta = []
    for p, exp, role in [
        (PREREG_S, PREREG_S_SHA12_EXPECTED, "S 预登记（K-V3S-3-* 四条判死线 + P-S3-1 入锁规则）"),
        (V3_EXECUTOR_BEFORE, V3_EXECUTOR_BEFORE_SHA12_EXPECTED, "修复前对照臂 loader（缺陷宿主件, 只读）"),
        (V3_EXECUTOR_AFTER, V3_EXECUTOR_AFTER_SHA12_EXPECTED, "修复臂 loader（F1 先例直修件, 只读）"),
        (S3_EXECUTOR_MOTHER, S3_EXECUTOR_MOTHER_SHA12_EXPECTED, "母件计算面（原语复用, 只读）"),
        (S3_RESULT_MOTHER, S3_RESULT_MOTHER_SHA12_EXPECTED, "上游扩词段读数 + loader_drop_finding（只读）"),
        (V3_RESULT, V3_RESULT_SHA12_EXPECTED, "per_event 标签 + held_out_idx + missing_events_ledger（只读）"),
        (ADDENDUM_D1, ADDENDUM_D1_SHA12_EXPECTED, "D1 addendum（critical_reflection_supplement 字面）"),
    ]:
        got = sha12_file(p)
        inputs_meta.append({
            "path": str(p.relative_to(REPO_ROOT)).replace("\\", "/"),
            "sha12_expected": exp,
            "sha12": got,
            "size_bytes": p.stat().st_size,
            "match": got == exp,
            "role": role,
        })
    input_chain_all_match = all(m["match"] for m in inputs_meta)

    # --- 1.2 双臂 substrate 载入 ---
    ev_before, meta_before = V3_BEFORE.load_all_events_v3()
    ev_after, meta_after = V3_AFTER.load_all_events_v3()
    n_total = len(ev_after)

    # 逐件 diff（修复面 = 只可能落在 D1_supp 三件）
    loader_changed_idx = [i for i in range(n_total) if ev_before[i] != ev_after[i]]
    loader_changed_detail = []
    for i in loader_changed_idx:
        rf_b = ev_before[i].get("reasoning_full", "") or ""
        rf_a = ev_after[i].get("reasoning_full", "") or ""
        prov = ev_after[i].get("_provenance", {}) or {}
        loader_changed_detail.append({
            "held_idx": i,
            "event_id": ev_after[i].get("event_id"),
            "q_id": ev_after[i].get("q_id"),
            "source_wave": prov.get("source_wave"),
            "source_file": prov.get("source_file"),
            "reasoning_full_len_before": len(rf_b),
            "reasoning_full_len_after": len(rf_a),
            "was_empty_before": (not rf_b.strip()),
            "now_nonempty_after": bool(rf_a.strip()),
            "text_after_head": rf_a[:60],
            "other_fields_identical": {
                k: (ev_before[i].get(k) == ev_after[i].get(k))
                for k in sorted(set(ev_before[i]) | set(ev_after[i]))
                if k != "reasoning_full"
            },
        })

    # --- 1.3 per_event 标签 + held-out 复现 ---
    v3_res = json.loads(V3_RESULT.read_text(encoding="utf-8"))
    per_event = {p["held_idx"]: p for p in v3_res["main_reading"]["per_event"]}
    held_ref = sorted(per_event.keys())

    rng_after = np.random.RandomState(SEED)
    held_repro_after = V3_AFTER.stratified_holdout_split_v3(ev_after, HELD_OUT_RATIO, rng_after)
    rng_before = np.random.RandomState(SEED)
    held_repro_before = V3_BEFORE.stratified_holdout_split_v3(ev_before, HELD_OUT_RATIO, rng_before)
    held_repro_after_bit_exact = (held_repro_after == held_ref)
    held_split_identical_across_arms = (held_repro_after == held_repro_before)

    corr_idx = sorted(i for i in held_ref if V3_AFTER.is_correction_event_v3(ev_after[i]))
    alt_idx = [i for i in held_ref if i not in set(corr_idx)]

    # --- 1.4 词表三臂 ---
    base_markers = V3_AFTER.CRITICAL_REFLECTION_MARKERS_V3
    base_n = len(base_markers)
    base_n_distinct = len(set(base_markers))
    dup_words = sorted({w for w, c in Counter(base_markers).items() if c > 1})

    locked_markers = base_markers + LOCKED_IN_WORDS
    locked_n = len(locked_markers)
    locked_n_distinct = len(set(locked_markers))

    full_markers = base_markers + ("推翻", "冲突", "非", "庖丁解牛", "小是具体")  # 母件提案全量 41 词
    full_n = len(full_markers)

    arms = [
        ("BASE_36 (原口径, 判定面)", base_markers),
        ("LOCKED_39 (PI 2026-09-28 部分入锁, 待生效)", locked_markers),
        ("PROPOSAL_FULL_41 (母件提案全量, 仅对照)", full_markers),
    ]

    # --- 1.5 双臂 × 三词表 × 双口径 读数矩阵 ---
    matrix = []
    for arm_label, markers in arms:
        for event_label, events in (("BEFORE_FIX (母件 loader)", ev_before),
                                    ("AFTER_FIX (F1 先例 loader)", ev_after)):
            cm = coverage_on(markers, held_ref, events, per_event)
            ca = coverage_on(markers, alt_idx, events, per_event)
            bm = blind_obey_on(markers, held_ref, events, per_event)
            matrix.append({
                "arm": arm_label,
                "n_markers_tuple": len(markers),
                "n_markers_distinct": len(set(markers)),
                "loader_state": event_label,
                "main_reading": {
                    "n_divergent": cm["n_divergent"],
                    "n_critical_among_divergent": cm["n_critical_among_divergent"],
                    "div_critical_coverage": cm["div_critical_coverage"],
                    "critical_idx": cm["critical_idx"],
                    "divergent_no_critical_idx": cm["divergent_no_critical_idx"],
                },
                "alt_reading": {
                    "n_divergent": ca["n_divergent"],
                    "n_critical_among_divergent": ca["n_critical_among_divergent"],
                    "div_critical_coverage": ca["div_critical_coverage"],
                    "critical_idx": ca["critical_idx"],
                    "divergent_no_critical_idx": ca["divergent_no_critical_idx"],
                },
                "blind_obey_main": {
                    "n_agree": bm["n_agree"],
                    "n_blind_obey": bm["n_blind_obey"],
                    "blind_obey_rate": bm["blind_obey_rate"],
                    "blind_obey_idx": bm["blind_obey_idx"],
                },
            })

    def pick(arm_prefix: str, loader_prefix: str) -> Dict[str, Any]:
        for row in matrix:
            if row["arm"].startswith(arm_prefix) and row["loader_state"].startswith(loader_prefix):
                return row
        raise KeyError((arm_prefix, loader_prefix))

    b36_before = pick("BASE_36", "BEFORE_FIX")
    b36_after = pick("BASE_36", "AFTER_FIX")
    l39_before = pick("LOCKED_39", "BEFORE_FIX")
    l39_after = pick("LOCKED_39", "AFTER_FIX")
    f41_before = pick("PROPOSAL_FULL_41", "BEFORE_FIX")
    f41_after = pick("PROPOSAL_FULL_41", "AFTER_FIX")

    # --- 1.6 验证：母件 S3 诊断腿目标值 0.4286 → 0.5714 (MAIN, BASE_36) ---
    verify_target_main_before = 0.4286
    verify_target_main_after = 0.5714
    verify_target_alt_before = 0.3000
    verify_target_alt_after = 0.5000
    verification = {
        "target_source": (
            "母件 result_2026_09_28.json §loaderfix_diagnostic_leg.after_fix 字面"
            "（BASE_36 MAIN 0.4286→0.5714 / ALT 0.3000→0.5000）"
        ),
        "base36_main_before": b36_before["main_reading"]["div_critical_coverage"],
        "base36_main_after": b36_after["main_reading"]["div_critical_coverage"],
        "base36_alt_before": b36_before["alt_reading"]["div_critical_coverage"],
        "base36_alt_after": b36_after["alt_reading"]["div_critical_coverage"],
        # 母件登记值 0.4286 / 0.5714 / 0.3000 / 0.5000 均为 4 位小数显示面；
        # 实测为 6/14 / 8/14 / 3/10 / 5/10 ⇒ 比对容差取 4 位小数舍入档（5e-5），非精确相等
        "compare_tolerance": 5e-5,
        "match_before_main": abs(round(b36_before["main_reading"]["div_critical_coverage"], 4) - verify_target_main_before) <= 5e-5,
        "match_after_main": abs(round(b36_after["main_reading"]["div_critical_coverage"], 4) - verify_target_main_after) <= 5e-5,
        "match_before_alt": abs(round(b36_before["alt_reading"]["div_critical_coverage"], 4) - verify_target_alt_before) <= 5e-5,
        "match_after_alt": abs(round(b36_after["alt_reading"]["div_critical_coverage"], 4) - verify_target_alt_after) <= 5e-5,
        "exact_fraction_before_main": "6/14",
        "exact_fraction_after_main": "8/14",
        "exact_fraction_before_alt": "3/10",
        "exact_fraction_after_alt": "5/10",
        "newly_critical_divergent_idx_main": sorted(
            set(b36_after["main_reading"]["critical_idx"]) - set(b36_before["main_reading"]["critical_idx"])
        ),
        "newly_critical_divergent_idx_alt": sorted(
            set(b36_after["alt_reading"]["critical_idx"]) - set(b36_before["alt_reading"]["critical_idx"])
        ),
        "verdict": None,   # 下方填
    }
    verification["verdict"] = bool(
        verification["match_before_main"] and verification["match_after_main"]
        and verification["match_before_alt"] and verification["match_after_alt"]
        and verification["newly_critical_divergent_idx_main"] == [37, 39]
    )

    # --- 1.7 覆盖率天花板（修复后重算）---
    n_nonempty_before = sum(1 for e in ev_before if (e.get("reasoning_full") or "").strip())
    n_nonempty_after = sum(1 for e in ev_after if (e.get("reasoning_full") or "").strip())
    n_div_main = b36_after["main_reading"]["n_divergent"]
    n_div_alt = b36_after["alt_reading"]["n_divergent"]

    # 真缺料件（reasoning_missing=true 且文本仍空）—— 修复后仍为空者
    still_empty = [i for i in held_ref
                   if per_event[i]["divergent"] and not (ev_after[i].get("reasoning_full") or "").strip()]
    still_empty_detail = [{
        "held_idx": i,
        "event_id": ev_after[i].get("event_id"),
        "q_id": ev_after[i].get("q_id"),
        "pred": per_event[i]["pred"],
        "actual": per_event[i]["actual"],
        "reasoning_missing_flag": bool(ev_after[i].get("reasoning_missing", False)),
        "reasoning_full_len": len(ev_after[i].get("reasoning_full", "") or ""),
    } for i in still_empty]

    ceiling_main_after = (n_div_main - len(still_empty)) / n_div_main
    ceiling_alt_after = (n_div_alt - len(still_empty)) / n_div_alt

    # 8 件未命中（verdict_v3 §2.3 字面）修复后逐件根因
    target8 = [12, 28, 37, 39, 47, 50, 72, 74]
    miss8 = []
    for i in target8:
        rf_b = ev_before[i].get("reasoning_full", "") or ""
        rf_a = ev_after[i].get("reasoning_full", "") or ""
        miss8.append({
            "held_idx": i,
            "event_id": ev_after[i].get("event_id"),
            "q_id": ev_after[i].get("q_id"),
            "pred": per_event[i]["pred"],
            "actual": per_event[i]["actual"],
            "reasoning_full_len_before": len(rf_b),
            "reasoning_full_len_after": len(rf_a),
            "class_before": (
                "EMPTY_TEXT" if not rf_b.strip()
                else ("COVERED_BY_BASE36" if has_critical_custom(rf_b, base_markers) else "NOT_COVERED_BY_BASE36")
            ),
            "class_after": (
                "STILL_EMPTY_TRUE_MISSING" if not rf_a.strip()
                else ("COVERED_BY_BASE36_AFTER_FIX" if has_critical_custom(rf_a, base_markers) else "NOT_COVERED_BY_BASE36_AFTER_FIX")
            ),
            "covering_base36_words_after": [m for m in base_markers if m in rf_a],
            "covered_by_locked39_after": has_critical_custom(rf_a, locked_markers),
        })
    n_still_empty = sum(1 for r in miss8 if r["class_after"] == "STILL_EMPTY_TRUE_MISSING")
    n_covered_after = sum(1 for r in miss8 if r["class_after"] == "COVERED_BY_BASE36_AFTER_FIX")
    n_not_covered_after = sum(1 for r in miss8 if r["class_after"] == "NOT_COVERED_BY_BASE36_AFTER_FIX")

    # --- 1.8 跨日 / 单日 / N / 纠正 账（loader 修复 0 影响，登记复核）---
    day_counts = Counter(e.get("date", "") for e in ev_after)
    n_corr = meta_after["n_correction"]
    days = meta_after["distinct_days"]
    max_day, max_day_n = max(day_counts.items(), key=lambda kv: kv[1])
    max_ratio = max_day_n / n_total
    day_counts_identical_across_arms = (meta_before["distinct_days"] == meta_after["distinct_days"]
                                        and meta_before["n_correction"] == meta_after["n_correction"])

    k_v3s_3_1_ok = bool(len(days) >= TH_CROSS_DAYS)
    k_v3s_3_2_ok = bool(max_ratio <= TH_SINGLE_DAY_RATIO)
    k_v3s_3_3_ok = bool(n_total >= TH_N_MIN and n_corr >= TH_N_CORRECTION)

    # K-V3S-3-4 判定 = 原 36 词口径（修复后）
    k_v3s_3_4_hit = bool(
        b36_after["main_reading"]["div_critical_coverage"] < TH_CRITICAL_COV
        or b36_after["alt_reading"]["div_critical_coverage"] < TH_CRITICAL_COV
    )

    # --- 1.9 39 词入锁面（待生效锁 ⇒ 只报读数, 0 判）---
    lock_face = {
        "status": LOCK_STATUS,
        "status_reason": (
            "PI 2026-09-28 拍板 T-S3-1「39 词部分入锁」；本件落盘为**待生效锁**"
            "（locked_pending_effective）⇒ 读数可报、**判定 0 做**"
            "（沿 prereg §2.3 P-S3-1 字面：入锁才允许重算并判定；生效时点由 PI 另定）"
        ),
        "pi_decision_literal": (
            "词表 39 词部分入锁：推翻 / 冲突 / 庖丁解牛 入锁；非 / 小是具体 出锁"
            "（源 = S3 扩词段实测面；`unfrozen_pending_PI` → 待生效锁）"
        ),
        "words_in": list(LOCKED_IN_WORDS),
        "words_out": list(LOCKED_OUT_WORDS),
        "n_markers_tuple": locked_n,
        "n_markers_distinct": locked_n_distinct,
        "tuple_duplicate_words": dup_words,
        "n_base_markers_tuple": base_n,
        "n_base_markers_distinct": base_n_distinct,
        "caliber_note": (
            f"「39 词」= tuple 长度口径（36 + 3）；去重 distinct = {locked_n_distinct}"
            f"（母件 tuple 内「未必」重复 1 次 ⇒ {dup_words}）——沿母件 §1 字面口径，0 擅改"
        ),
        "readings_before_fix": {
            "main": l39_before["main_reading"]["div_critical_coverage"],
            "alt": l39_before["alt_reading"]["div_critical_coverage"],
        },
        "readings_after_fix": {
            "main": l39_after["main_reading"]["div_critical_coverage"],
            "alt": l39_after["alt_reading"]["div_critical_coverage"],
            "main_critical_idx": l39_after["main_reading"]["critical_idx"],
            "alt_divergent_no_critical_idx": l39_after["alt_reading"]["divergent_no_critical_idx"],
        },
        "judged": False,
        "judge_reason": "待生效锁 ⇒ 0 判（沿 P-S3-1 字面）",
        "direction_invariance_note": (
            "入锁口径 MAIN/ALT 两读数均 < 1.00 ⇒ 若生效, K-V3S-3-4 的 hit 方向与 36 词口径"
            "**同向（仍 hit=True）**；本件**不宣告**该口径已生效判定"
        ),
        "side_effect_blind_obey": {
            "note": "入锁必并报盲从率（诚实纪律：0 只报 coverage 改善）",
            "before_fix": l39_before["blind_obey_main"],
            "after_fix": l39_after["blind_obey_main"],
            "delta_from_loader_fix": l39_after["blind_obey_main"]["blind_obey_rate"] - l39_before["blind_obey_main"]["blind_obey_rate"],
            "delta_from_base36_same_loader_arm": l39_after["blind_obey_main"]["blind_obey_rate"] - b36_after["blind_obey_main"]["blind_obey_rate"],
            "base36_reference_after_fix": b36_after["blind_obey_main"],
            "note_detail": (
                "**两个 Δ 方向不同，必须分别读**：① loader 修复本身对盲从率 **0 影响**"
                "（before/after 均为 idx 5 单件，delta = 0）；② 「庖丁解牛」入锁使 idx 23 "
                "由盲从件转非盲从件（36 词臂 idx 5 + 23 → 39 词臂 idx 5），盲从率 0.2222 → 0.1111。"
                "**若只报 coverage 改善而不报此项即为误导**"
            ),
        },
    }

    result: Dict[str, Any] = {
        "schema": "v3_s3_wordexpand_recheck_r1_v1",
        "series": "V3-S 补强系列 S3 段 · loader_r1 修复后覆盖率重算（r1 修正版）",
        "executor": "results/_v3_s3_wordexpand_data/executor_r1_2026_09_28.py",
        "mother_executor": "results/_v3_s3_wordexpand_data/executor_2026_09_28.py",
        "prereg": "results/_v3_s_prereg_v1_2026_09_27.md",
        "date": DATE_FROZEN,
        "generated_ts_frozen": TS_FROZEN,
        "seed": SEED,
        "runtime": "python3 + numpy；0 LLM / 0 proxy / 0 gateway；全部为本地机械读数",
        "skill": {
            "requested": "scientific-research-workflows:experimental-design (plugin @scientific-research-workflows)",
            "status": "Local skill not found — C:/Users/Administrator/.minimax/plugins 实测 0 项（空目录）",
            "fallback": "纪律锚 = prereg §2.3 K-V3S-3-1..3-4 字面 + E-42.1 死因改判 + 母件 result §loader_drop_finding 字面",
            "disclosure": "未加载该 skill 的任何指令；0 引用、0 虚构其条文",
        },
        "r1_fix_registration": {
            "pi_decision": "T-S3-2 loader 丢弃面 = 按 F1 先例直修（PI 2026-09-28 拍板）",
            "prescription": "拼接入口由「嵌套于排他 if 链首项」提为「base 已定后全分支统一后置追加」",
            "prescription_source": "results/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py（ee8671a28c2f）文件头 r1 登记块",
            "how_applied_in_this_file": (
                "本件**只切换装载面引用**（事件构造面 = 先例 r1 executor）；"
                "母件 v3 executor 仅作修复前对照臂读数；**0 复制修法代码**（避免同一修法两份实现漂移）"
            ),
            "unchanged_discipline": (
                "0 改词表 / 0 改阈值 / 0 改特征 / 0 改判定公式 / 0 改 seed / "
                "0 改 held-out 划分 / 0 改 ALT 口径定义 / 0 改 per_event 标签来源 / 0 重训决策树"
            ),
            "defect_host_file": "results/_v4_pi_cot_v3_ruleset_v3_executor.py (8a81d90c69ba)",
            "defect_lines": "775-788（if/elif 排他链; supplement 拼接嵌在首项内）",
            "semantic_equivalence": "先例修法在 base 非空时输出逐字不变 = base + ' ' + supplement",
        },
        "inputs": inputs_meta,
        "input_chain_all_match": input_chain_all_match,
        "loader_fix_verification": {
            "substrate_n_before": len(ev_before),
            "substrate_n_after": n_total,
            "substrate_n_identical": len(ev_before) == n_total,
            "load_meta_identical": (meta_before == meta_after),
            "changed_event_idx": loader_changed_idx,
            "n_changed": len(loader_changed_idx),
            "changed_detail": loader_changed_detail,
            "all_changed_are_d1_supp": all(
                d["source_wave"] == "D1_supp" for d in loader_changed_detail
            ),
            "all_changed_were_empty_before": all(d["was_empty_before"] for d in loader_changed_detail),
            "all_changed_nonempty_after": all(d["now_nonempty_after"] for d in loader_changed_detail),
            "only_reasoning_full_field_changed": all(
                all(v is True for v in d["other_fields_identical"].values())
                for d in loader_changed_detail
            ),
            "held_out_split_identical_across_arms": held_split_identical_across_arms,
            "held_out_repro_after_bit_exact_vs_result_v3": held_repro_after_bit_exact,
            "n_events_with_reasoning_before": n_nonempty_before,
            "n_events_with_reasoning_after": n_nonempty_after,
            "verdict_0_4286_to_0_5714": verification,
        },
        "substrate": {
            "n_substrate_run": n_total,
            "held_out_count": len(held_ref),
            "held_out_ratio": HELD_OUT_RATIO,
            "held_out_seed": SEED,
            "held_out_idx": held_ref,
            "alt_reading_n": len(alt_idx),
            "alt_reading_idx": alt_idx,
            "alt_reading_correction_excluded_idx": corr_idx,
            "n_correction_total": n_corr,
            "alt_caliber_definition": (
                "ALT = 主 held-out 23 件剔 correction 子集（is_correction_event_v3）= 18 件"
                "（沿母件显式定义；**0 静默沿用** v3 result 登记的不可复现 ALT 值）"
            ),
            "extrapolation_boundary": (
                "仅在 77 件 RUN substrate + 23 件 held-out + v3 词表构造域内有效；"
                "不可外推至 S3 补采后 substrate（≥85）或 S4 扩样（≥167），更不可外推至命题层"
            ),
        },
        "word_table": {
            "base36_tuple": base_n,
            "base36_distinct": base_n_distinct,
            "tuple_duplicate_words": dup_words,
            "locked39_tuple": locked_n,
            "locked39_distinct": locked_n_distinct,
            "proposal_full_41_tuple": full_n,
        },
        "coverage_matrix": {
            "caliber_note": (
                "同一 77 件 substrate / 同一 held-out 23 / 同一 ALT 18 件 / 同一 per_event 标签源"
                "（result_v3 登记值）；**仅 loader 臂与词表臂变** ⇒ Δ 可归因"
            ),
            "matrix": matrix,
            "deltas_after_minus_before": {
                "base36_main": b36_after["main_reading"]["div_critical_coverage"] - b36_before["main_reading"]["div_critical_coverage"],
                "base36_alt": b36_after["alt_reading"]["div_critical_coverage"] - b36_before["alt_reading"]["div_critical_coverage"],
                "locked39_main": l39_after["main_reading"]["div_critical_coverage"] - l39_before["main_reading"]["div_critical_coverage"],
                "locked39_alt": l39_after["alt_reading"]["div_critical_coverage"] - l39_before["alt_reading"]["div_critical_coverage"],
                "proposal_full41_main": f41_after["main_reading"]["div_critical_coverage"] - f41_before["main_reading"]["div_critical_coverage"],
                "proposal_full41_alt": f41_after["alt_reading"]["div_critical_coverage"] - f41_before["alt_reading"]["div_critical_coverage"],
            },
        },
        "eight_miss_root_cause_after_fix": {
            "target_idx": target8,
            "source_literal": "verdict_v3 §2.3 K-V3-B 字面 8 件无批判词分歧事件",
            "per_event": miss8,
            "tally": {
                "n_still_empty_true_missing": n_still_empty,
                "n_covered_by_base36_after_fix": n_covered_after,
                "n_not_covered_by_base36_after_fix": n_not_covered_after,
            },
            "finding": (
                f"修复后：{n_covered_after} 件（idx 37 / 39）由空文本转为 36 词命中"
                f"（**构造面缺陷已消**）；{n_still_empty} 件（idx 47 / 50）**仍为空文本**"
                f"（reasoning_missing = true 的真缺料件，词表与 loader 均无法补）；"
                f"{n_not_covered_after} 件（idx 74 等）非空但 36 词未覆盖"
            ),
            "coverage_ceiling_after_fix": {
                "main_n_divergent": n_div_main,
                "main_ceiling": ceiling_main_after,
                "alt_n_divergent": n_div_alt,
                "alt_ceiling": ceiling_alt_after,
                "ceiling_formula": "(n_divergent - 真缺料空文本件数) / n_divergent",
                "still_empty_divergent_detail": still_empty_detail,
                "implication": (
                    f"⇒ 修复后天花板 MAIN {ceiling_main_after:.4f} / ALT {ceiling_alt_after:.4f}；"
                    "**K-V3S-3-4 的 1.00 在本盘素材面仍结构性不可达**"
                    "（idx 47 / 50 为 PI 当初跳过推理、采集协议允许记 null 的真缺料件）"
                ),
            },
        },
        "word_lock_39_face": lock_face,
        "proposal_full_41_face": {
            "status": "not_locked_reference_only",
            "note": (
                "母件提案全量 41 词臂**仅作对照读数**；PI 2026-09-28 拍板入锁的是 39 词臂"
                "（「非」/「小是具体」出锁）⇒ 本臂 0 判"
            ),
            "before_fix": {
                "main": f41_before["main_reading"]["div_critical_coverage"],
                "alt": f41_before["alt_reading"]["div_critical_coverage"],
            },
            "after_fix": {
                "main": f41_after["main_reading"]["div_critical_coverage"],
                "alt": f41_after["alt_reading"]["div_critical_coverage"],
            },
        },
        "kill_lines": KILL_LINES_S3,
        "judgment": {
            "k_v3s_3_1_ok": k_v3s_3_1_ok,
            "k_v3s_3_1_note": (
                f"distinct days = {len(days)} {days} vs 阈值 {TH_CROSS_DAYS} ⇒ "
                f"{'达标' if k_v3s_3_1_ok else '不达标'}（loader 修复 0 影响跨日；D6/D1 补采入库后须重算）"
            ),
            "k_v3s_3_2_ok": k_v3s_3_2_ok,
            "k_v3s_3_2_note": (
                f"最大单日 = {max_day} {max_day_n}/{n_total} = {max_ratio:.4f} vs 阈值 "
                f"{TH_SINGLE_DAY_RATIO} ⇒ {'达标' if k_v3s_3_2_ok else '不达标'}"
            ),
            "k_v3s_3_3_ok": k_v3s_3_3_ok,
            "k_v3s_3_3_note": (
                f"N = {n_total} vs {TH_N_MIN}；纠正/反转 = {n_corr} vs {TH_N_CORRECTION} ⇒ "
                f"{'达标' if k_v3s_3_3_ok else '不达标'}"
            ),
            "k_v3s_3_4_hit": k_v3s_3_4_hit,
            "k_v3s_3_4_note": (
                f"修复后原 36 词口径：MAIN {b36_after['main_reading']['div_critical_coverage']:.4f} / "
                f"ALT {b36_after['alt_reading']['div_critical_coverage']:.4f}，均 < {TH_CRITICAL_COV} ⇒ hit=True"
                f"（修复前 MAIN {b36_before['main_reading']['div_critical_coverage']:.4f} / "
                f"ALT {b36_before['alt_reading']['div_critical_coverage']:.4f}）"
            ),
            "k_v3s_3_4_locked39_face": {
                "status": LOCK_STATUS,
                "judged": False,
                "reported_value_only": {
                    "main_reading": l39_after["main_reading"]["div_critical_coverage"],
                    "alt_reading": l39_after["alt_reading"]["div_critical_coverage"],
                },
            },
            "any_hit_scope": (
                "K-V3S-3-4 = 判定面命中线（进判定汇总）；K-V3S-3-1/2/3 = 采集面达标线（不进 FAIL 汇总）；两者不混算"
            ),
            "any_hit": k_v3s_3_4_hit,
            "root_cause": (
                "**β 构造面主导但已局部修复**：修复后 idx 37 / 39 的装载缺陷面消解"
                "（覆盖率 0.4286 → 0.5714 MAIN）；剩余主因 = **素材面真缺料**"
                "（idx 47 / 50 reasoning_missing = true）+ **词表边界**（idx 74 等）；"
                "**词表覆盖不足不再是主因**，且 1.00 阈值在本盘素材面**结构性不可达**"
                "（天花板 MAIN 0.8571）—— 本棒**0 擅调阈值**"
            ),
            "root_cause_three_way": {
                "alpha_true_falsification": "弱（修复后仍无非空文本件因词表边界大规模漏检）",
                "beta_construct_or_boundary": (
                    "仍主导，但构成已变：装载缺陷面**已修**（37/39）；剩素材缺料 + 词表边界"
                ),
                "sentinel_warning": (
                    "即便 loader 修复，K-V3S-3-4 仍 hit=True（覆盖率 < 1.00）—— "
                    "sentinel 未解除，**不可宣告「修 loader 即达标」**"
                ),
            },
        },
        "boundary_statement": {
            "no_extrapolation": (
                "本件读数仅在 77 件 RUN substrate + 23 件 held-out + 23→18 ALT + v3 词表构造域内有效；"
                "不可外推至补采后 substrate / S4 扩样 / 命题层"
            ),
            "no_killline_invention": "K-V3S-3-1..4 四条阈值全部沿既有件字面，本棒 0 自设",
            "no_threshold_adjustment": "0 擅调；1.00 未动（天花板不可达 ≠ 阈值可改）",
            "no_derived_json_merge": "本件独立落盘（_v3_s3_wordexpand_recheck_r1_2026_09_28.json），0 合并任何既有 result JSON",
            "no_existing_file_touched": (
                "母件 / 宿主件 / 先例件 / dataset / result / verdict / 勘误链全部只读；"
                "本件与 r1 result 均为**新名新建**（开跑前实测不在盘）"
            ),
            "no_retrain": (
                "**0 重训决策树**：per_event 的 pred / actual / divergent 沿 result_v3 登记值；"
                "本件只重算 coverage 分子/分母 ⇒ 修复对 pred 的影响面**未评估**（见 open_items）"
            ),
            "no_llm": "0 LLM / 0 proxy / 0 gateway；全部读数为本地机械 substring 命中",
            "key_never_plaintext": "0 key 读取 / 0 落盘 / 0 入 prompt / 0 入 JSON / 0 入 log",
            "succeeded_not_done": (
                "本件 = **覆盖率重算 + 修复验证**，不是「loader 修复即达标」的宣告；"
                "亦非 substrate 重跑（0 重训、0 重划 held-out）"
            ),
        },
        "open_items": [
            {
                "id": "T-S3-3",
                "item": "K-V3S-3-4 的 1.00 在本盘素材面结构性不可达（修复后天花板 MAIN 0.8571 / ALT 0.8000）",
                "status": "仍挂 PI；本棒 0 擅调",
                "honest_note": (
                    "唯一可达路径 = 补 idx 47 / 50 的 reasoning_missing 缺料件（D1 补采 8 件题面见 "
                    "results/_v3_s3_collection_brief_2026_09_28.md）；词表扩词**不是**可达路径"
                ),
            },
            {
                "id": "T-S3-4",
                "item": "v3 登记 ALT 口径（n_div=11 / n_crit=4）不可复现；本件沿母件显式定义（n_div=10）",
                "status": "仍挂 PI；本件 0 静默沿用 v3 值",
            },
            {
                "id": "T-S3-5",
                "item": "D1 缺位 8 件的 event_id 归属（ledger 记 33–40 占位；实测 33–37 在盘）",
                "status": (
                    "已按 PI 2026-09-28 拍板落**订正新名件** "
                    "results/_v4_pi_cot_v3_missing_ledger_correction_2026_09_28.md；原 result_v3 ledger 0 改"
                ),
            },
            {
                "id": "T-S3-1R",
                "item": "39 词入锁面的**生效时点**（现 = 待生效锁 locked_pending_effective）",
                "status": "待 PI；本件只报读数 0 判",
            },
            {
                "id": "NEW-1",
                "item": "loader 修复对**决策树 pred** 的影响面（本件 0 重训 ⇒ 未评估）",
                "status": (
                    "如实登记为未评估项：idx 37 / 38 / 39 的 rf_len_bucket / rf_pos_density / "
                    "n_keywords_hit 三项特征随文本变化 ⇒ 若重训，全部 pred 可能变动；"
                    "**本棒 0 擅开重训**（会改 result_v3 判定本体，超出本派工范围）"
                ),
            },
        ],
        "honesty_note": (
            "本件全部读数为盘上实测：substrate 由 v3 executor loader 只读载入（双臂各 77 件，meta 全等）；"
            "held-out 23 沿 result_v3 登记值且修复臂复现 **bit-exact**；两臂划分**完全相同**；"
            "loader 差异**逐件仅落在 idx 37/38/39 且仅 reasoning_full 一个字段变动**（其余字段逐件全等）；"
            "覆盖率分子/分母沿母件原语（只读复用，0 复制实现）。"
            "如实登记三处不利读数：(i) 修复后 K-V3S-3-4 **仍 hit=True**（0.5714 / 0.5000 << 1.00），"
            "sentinel 未解除；(ii) idx 47 / 50 为真缺料（reasoning_missing=true），词表与 loader 均无法补 ⇒ "
            "天花板 0.8571；(iii) 本件 **0 重训**，pred 影响面未评估。"
            "39 词入锁面（待生效锁）只报读数不判；「庖丁解牛」入锁对盲从率的副作用**并报**。"
        ),
    }

    return result


if __name__ == "__main__":
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    res = main()
    OUT_RESULT.write_text(
        json.dumps(res, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    v = res["loader_fix_verification"]["verdict_0_4286_to_0_5714"]
    print(f"written: {OUT_RESULT}")
    print(f"sha12: {sha12_file(OUT_RESULT)}")
    print(f"bytes: {OUT_RESULT.stat().st_size}")
    print(f"input_chain_all_match: {res['input_chain_all_match']}")
    print(f"verification_passed: {v['verdict']} "
          f"(MAIN {v['base36_main_before']} -> {v['base36_main_after']}; "
          f"ALT {v['base36_alt_before']} -> {v['base36_alt_after']})")
    print(f"k_v3s_3_4_hit: {res['judgment']['k_v3s_3_4_hit']}")
