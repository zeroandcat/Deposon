#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V3-S S3 段 executor · 批判反思词表扩词 + 覆盖率敏感性重算 · worker 出件 · 2026-09-28

依据（纪律锚）:
  - results/_v3_s_prereg_v1_2026_09_27.md (SHA-12 ef5a40554960) §1.3 S3 三合一
    / §2.3 S3 四条判死线 K-V3S-3-1..3-4 字面 / §2.6 提案 P-S3-1 扩词清单本体
    / §2.7 T-1 素材面不覆盖 claim / §2.8 外推边界
  - results/_v4_pi_cot_v2_questionnaire_v1.md (SHA-12 7b14cdb31d21) §0 采集协议
  - results/_v4_pi_cot_v3_ruleset_v3_executor.py (SHA-12 8a81d90c69ba) 构造面
    (CRITICAL_REFLECTION_MARKERS_V3 / has_critical_reflection_v3 /
     load_all_events_v3 / stratified_holdout_split_v3 / feats_v3 /
     extract_judgment_sequence_v3 / build_tree / predict_tree) — 只读 import, 0 触动
  - results/_v4_pi_cot_v3_result_v3.json (SHA-12 585714f9660c) per_event 同 substrate 对照源
  - results/_v4_pi_cot_v3_verdict_v3.md (SHA-12 bb44fdc7ab0f) §2.3 K-V3-B 根因 8 件字面

本段范围（严格限定）:
  (a) 扩词提案 — 依据三源实证词, 提案入件, **status = unfrozen_pending_PI**
  (b) 77 件 RUN substrate 上扩词前后 K-V3S-3-4 批判覆盖率敏感性重算（双口径并报）
  (c) 跨日账字面登记

铁律:
  - 判死线 0 私设 / 0 擅调阈值（K-V3S-3-4 判定沿 1.00 沿 K-V3-B / TH-v2-5b 字面）
  - 扩词清单未入锁 ⇒ 扩词口径 **不判**, status = unfrozen（P-S3-1 字面）
  - 0 LLM / 0 proxy / 0 gateway; 词表扩词为本地机械扫描; key 永不明文
  - 显式布尔命名 (S-40 教训); SHA-12 = hashlib.sha256(hexdigest)[:12] 小写
  - 只读 import 既有件, 0 字节改动; 派生件独立落盘, 0 合并
  - 采集题面 **0 代答**（PI 实时答题由 parent 走 ask_user 问卷）
  - 时间戳冻结 (re-entrancy-safe), 逐字可重跑
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

QUESTIONNAIRE_V1 = RESULTS_DIR / "_v4_pi_cot_v2_questionnaire_v1.md"

V3_EXECUTOR = RESULTS_DIR / "_v4_pi_cot_v3_ruleset_v3_executor.py"
V3_EXECUTOR_SHA12_EXPECTED = "8a81d90c69ba"

V3_RESULT = RESULTS_DIR / "_v4_pi_cot_v3_result_v3.json"
V3_RESULT_SHA12_EXPECTED = "585714f9660c"

V3_DATASET = RESULTS_DIR / "_v4_pi_cot_v3_dataset.json"
V3_DATASET_SHA12_EXPECTED = "5118f5b44f17"

DATASET_V2_V11 = RESULTS_DIR / "_v4_pi_cot_v2_dataset.json"
DATASET_V2_V11_SHA12_EXPECTED = "7b01cd835a41"

ADDENDUM_D1 = RESULTS_DIR / "_v4_pi_cot_v2_dataset_addendum_2026_09_24.json"
ADDENDUM_D1_SHA12_EXPECTED = "172093a23e4b"

ADDENDUM_D3C = RESULTS_DIR / "_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json"
ADDENDUM_D3C_SHA12_EXPECTED = "401bd614cdf7"

VERDICT_V3 = RESULTS_DIR / "_v4_pi_cot_v3_verdict_v3.md"
VERDICT_V3_SHA12_EXPECTED = "bb44fdc7ab0f"

S2_RESULT = RESULTS_DIR / "_v3_s2_executor" / "result_2026_09_27.json"
S1_RESULT = RESULTS_DIR / "_v3_s1_executor" / "result_2026_09_27.json"

OUT_RESULT = OUT_DIR / "result_2026_09_28.json"
OUT_RESCRIPT = OUT_DIR / "rescript_2026_09_28.md"

# 时间戳冻结 (重跑逐字不变)
TS_FROZEN = "2026-09-28T13:20:00+08:00"
DATE_FROZEN = "2026-09-28"

# ---------------------------------------------------------------------------
# 判死线（全部沿既有件字面, 0 自创）
# ---------------------------------------------------------------------------
TH_CRITICAL_COV = 1.00       # K-V3S-3-4 沿 K-V3-B / TH-v2-5b 字面, 0 新数值
TH_CROSS_DAYS = 5           # K-V3S-3-1 沿 verdict_v3 §3.3 字面
TH_SINGLE_DAY_RATIO = 0.60  # K-V3S-3-2 沿 TH-v2-3 / TH-v3-3 字面
TH_N_MIN = 50               # K-V3S-3-3 沿 TH-v2-1 / TH-v3-1 字面
TH_N_CORRECTION = 5         # K-V3S-3-3 沿 TH-v2-2 / TH-v3-2 字面
SEED = 42                   # TH-v3-15
HELD_OUT_RATIO = 0.30       # TH-v3-4

# 判死线显式布尔名 + hit_direction 字面（沿 prereg §2.0 纪律, 显式落盘不省略）
KILL_LINES_S3 = [
    {
        "id": "K-V3S-3-1",
        "name": "跨日天数达标线",
        "rule": "distinct calendar days >= 5",
        "threshold": TH_CROSS_DAYS,
        "threshold_source": "verdict_v3 §3.3 字面 (PI 2026-09-27 拍板值); TH-v2-3 自身 '>=3' 沿用不动, 取 max(3,5)=5",
        "hit_direction": "跨日 < 5 天即不达标 (ok=False)",
        "boolean_field": "k_v3s_3_1_ok",
    },
    {
        "id": "K-V3S-3-2",
        "name": "单日占比达标线",
        "rule": "单日最大占比 <= 0.60 (全部入库后重算)",
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
        "rule": "原 36 词 coverage 与扩词后 N 词 coverage 两者并报, 判定沿 1.00; 扩词清单须先落盘入锁",
        "threshold": TH_CRITICAL_COV,
        "threshold_source": "1.00 沿 K-V3-B / TH-v2-5b 字面; 扩词后档位数 0 自设",
        "hit_direction": "任一口径 coverage < 1.00 即触发 (hit=True)",
        "boolean_field": "k_v3s_3_4_hit",
    },
]

# ---------------------------------------------------------------------------
# 扩词提案（三源实证, 0 自创）
#
# 源 A = 双复核实证边界词「推翻 / 冲突 / 非」（派工单字面指认的三词）
#         —— 本棒逐词在 77 件 substrate 上实测落点, 不代为归因 verifier 呈文原意
# 源 B = G5 caliber_echo（「小是具体」等）—— d3c addendum caliber_echo 字段字面
# 源 C = S2 per-class 未命中分布 —— result_2026_09_27.json per_event 字面
#         （源 C 只指出**未命中的件**, 本身不提供新词; 词的来源仍须归源 A / 源 B）
# ---------------------------------------------------------------------------
EXPANSION_PROPOSAL_S3: Tuple[Dict[str, Any], ...] = (
    {
        "word": "推翻",
        "source": "A",
        "source_label": "双复核实证边界词（派工单字面指认）",
        "empirical_hit_events": [12, 20],
        "empirical_hit_events_already_critical": [9, 67],
        "note": "idx=12 held-out 分歧件, reasoning_full 含「注意后一步可以推翻前一步结论」——结论可被后一步推翻 = 判死线/批判反思语义的直接承载",
    },
    {
        "word": "冲突",
        "source": "A",
        "source_label": "双复核实证边界词（派工单字面指认）",
        "empirical_hit_events": [28],
        "empirical_hit_events_already_critical": [13, 24],
        "note": "idx=28 held-out 分歧件, reasoning_full 含「与外界硬性冲突时」",
    },
    {
        "word": "非",
        "source": "A",
        "source_label": "双复核实证边界词（派工单字面指认）",
        "empirical_hit_events": [25, 72],
        "empirical_hit_events_already_critical": [13, 67],
        "note": "idx=72 held-out 分歧件（D4_Q1 PI 字面「严格按 prereg 字面达标, 非 supersede」）; idx=25 含「非欧几何」——**单字过宽风险见 §词表风险面**",
    },
    {
        "word": "庖丁解牛",
        "source": "B",
        "source_label": "G5 caliber_echo（d3c addendum caliber_echo 字段字面）",
        "empirical_hit_events": [23],
        "empirical_hit_events_already_critical": [71],
        "note": "idx=23 = K-V3-C 盲从事件（agree 且无批判词）; caliber_echo 字面记「庖丁解牛与 D1 event24 呼应」",
    },
    {
        "word": "小是具体",
        "source": "B",
        "source_label": "G5 caliber_echo（d3c addendum caliber_echo 字段字面）",
        "empirical_hit_events": [],
        "empirical_hit_events_already_critical": [70],
        "note": "仅命中 idx=70（已批判词命中）⇒ 对 coverage **0 边际增益**; 仅作口径登记价值保留",
    },
)


def sha12_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# 只读 import v3 executor（0 字节改动）
V3 = _load_module("v3_ruleset_executor_ref_s3_wordexpand", V3_EXECUTOR)


# ---------------------------------------------------------------------------
# 1. 批判反思词命中扫描（本地机械, 0 LLM）
# ---------------------------------------------------------------------------
def has_critical_custom(reasoning: str, markers: Sequence[str]) -> bool:
    """批判反思词命中判定 — 与 v3 has_critical_reflection_v3 同语义, 仅词表可参数化."""
    if not reasoning:
        return False
    for m in markers:
        if m in reasoning:
            return True
    return False


def coverage_on(markers: Sequence[str], idxs: Sequence[int],
                events: List[Dict[str, Any]],
                per_event: Dict[int, Dict[str, Any]]) -> Dict[str, Any]:
    """在给定 held-out idx 集上算 K-V3S-3-4 批判覆盖率.

    分母 = divergent 件数; 分子 = divergent 且批判词命中件数.
    口径沿 v3 executor 字面: div_crit_cov = n_critical_among_div / n_div;
    n_div = 0 时沿 v3 字面记 1.0（0 触发）.
    """
    div = [i for i in idxs if per_event[i]["divergent"]]
    crit = [i for i in div
            if has_critical_custom(events[i].get("reasoning_full", ""), markers)]
    n_div = len(div)
    cov = (len(crit) / n_div) if n_div > 0 else 1.0
    return {
        "n_held": len(idxs),
        "n_divergent": n_div,
        "n_critical_among_divergent": len(crit),
        "div_critical_coverage": cov,
        "critical_idx": sorted(crit),
        "divergent_no_critical_idx": sorted(set(div) - set(crit)),
    }


def blind_obey_on(markers: Sequence[str], idxs: Sequence[int],
                  events: List[Dict[str, Any]],
                  per_event: Dict[int, Dict[str, Any]]) -> Dict[str, Any]:
    """盲从率（K-V3-C 面）— 扩词的**副作用面**, 必并报（诚实纪律）."""
    agree = [i for i in idxs if not per_event[i]["divergent"]]
    blind = [i for i in agree
             if not has_critical_custom(events[i].get("reasoning_full", ""), markers)]
    return {
        "n_agree": len(agree),
        "n_blind_obey": len(blind),
        "blind_obey_rate": (len(blind) / len(agree)) if agree else 0.0,
        "blind_obey_idx": sorted(blind),
    }


# ---------------------------------------------------------------------------
# 2. 主流程
# ---------------------------------------------------------------------------
def main() -> Dict[str, Any]:
    # --- 2.1 输入链 SHA-12 核验（先核后用, 只读）---
    inputs_meta = []
    for p, exp, role in [
        (PREREG_S, PREREG_S_SHA12_EXPECTED, "S 预登记（K-V3S-3-* 四条判死线锚 + P-S3-1 扩词提案锚）"),
        (V3_EXECUTOR, V3_EXECUTOR_SHA12_EXPECTED, "v3 构造实现面（只读 import, 0 触动）"),
        (V3_RESULT, V3_RESULT_SHA12_EXPECTED, "同 substrate 对照读数源（per_event 字面）"),
        (V3_DATASET, V3_DATASET_SHA12_EXPECTED, "v3 dataset 锚（metadata 件, 只读）"),
        (DATASET_V2_V11, DATASET_V2_V11_SHA12_EXPECTED, "v1.1 events 源（37 件）"),
        (ADDENDUM_D1, ADDENDUM_D1_SHA12_EXPECTED, "D1 addendum（含 critical_reflection_supplement 字面）"),
        (ADDENDUM_D3C, ADDENDUM_D3C_SHA12_EXPECTED, "D3c addendum（caliber_echo 字面源）"),
        (VERDICT_V3, VERDICT_V3_SHA12_EXPECTED, "K-V3-B 根因 8 件字面源"),
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

    for p in (QUESTIONNAIRE_V1, S2_RESULT, S1_RESULT):
        inputs_meta.append({
            "path": str(p.relative_to(REPO_ROOT)).replace("\\", "/"),
            "sha12_expected": None,
            "sha12": sha12_file(p),
            "size_bytes": p.stat().st_size,
            "match": None,
            "role": "引用面基线（无派工字面 SHA, 只登记实测）",
        })

    # --- 2.2 substrate 载入 + held-out 复现 ---
    events, meta = V3.load_all_events_v3()
    v3_res = json.loads(V3_RESULT.read_text(encoding="utf-8"))
    per_event = {p["held_idx"]: p for p in v3_res["main_reading"]["per_event"]}
    held_ref = sorted(per_event.keys())

    rng = np.random.RandomState(SEED)
    held_repro = V3.stratified_holdout_split_v3(events, HELD_OUT_RATIO, rng)
    held_repro_ok = (held_repro == held_ref)

    # ALT 口径 = 主 held-out 剔 correction 子集（本棒**显式定义**, 见 §alt_caliber）
    corr_idx = sorted(i for i in held_ref if V3.is_correction_event_v3(events[i]))
    alt_idx = [i for i in held_ref if i not in set(corr_idx)]

    # --- 2.3 词表基数自证 ---
    base_markers = V3.CRITICAL_REFLECTION_MARKERS_V3
    base_n = len(base_markers)
    base_n_distinct = len(set(base_markers))
    dup_words = sorted({w for w, c in Counter(base_markers).items() if c > 1})

    # --- 2.4 逐词实测（扩词前 / 扩词后双口径）---
    nonempty = [i for i, e in enumerate(events) if (e.get("reasoning_full") or "").strip()]
    base_critical_idx = sorted(
        i for i in nonempty if has_critical_custom(events[i]["reasoning_full"], base_markers)
    )
    per_word = []
    for item in EXPANSION_PROPOSAL_S3:
        w = item["word"]
        hit_idx = [i for i in nonempty if w in events[i]["reasoning_full"]]
        newly = [i for i in hit_idx if i not in base_critical_idx]
        already = [i for i in hit_idx if i in base_critical_idx]
        held_newly = sorted(i for i in newly if i in held_ref)
        alt_newly = sorted(i for i in newly if i in alt_idx)
        div_newly = [i for i in held_newly if per_event[i]["divergent"]]
        agree_newly = [i for i in held_newly if not per_event[i]["divergent"]]
        per_word.append({
            "word": w,
            "source": item["source"],
            "source_label": item["source_label"],
            "n_events_containing": len(hit_idx),
            "total_occurrences": sum(events[i]["reasoning_full"].count(w) for i in hit_idx),
            "hit_idx_all": sorted(hit_idx),
            "newly_critical_idx": sorted(newly),
            "already_critical_idx": sorted(already),
            "held_newly_critical": held_newly,
            "alt_newly_critical": alt_newly,
            "held_newly_critical_divergent": sorted(div_newly),
            "held_newly_critical_agree": sorted(agree_newly),
            "margin_gain_main": len(div_newly),
            "margin_gain_alt": len([i for i in alt_newly if per_event[i]["divergent"]]),
            "note": item["note"],
        })

    # --- 2.5 敏感性矩阵（扩词前后 × 双口径）---
    expanded_markers = base_markers + tuple(
        it["word"] for it in EXPANSION_PROPOSAL_S3
    )
    expanded_n = len(expanded_markers)
    expanded_n_distinct = len(set(expanded_markers))

    cov_base_main = coverage_on(base_markers, held_ref, events, per_event)
    cov_base_alt = coverage_on(base_markers, alt_idx, events, per_event)
    cov_exp_main = coverage_on(expanded_markers, held_ref, events, per_event)
    cov_exp_alt = coverage_on(expanded_markers, alt_idx, events, per_event)

    blind_base_main = blind_obey_on(base_markers, held_ref, events, per_event)
    blind_exp_main = blind_obey_on(expanded_markers, held_ref, events, per_event)

    # 逐源增量矩阵（源 A 单跑 / 源 B 单跑 / A+B）
    srcA = tuple(it["word"] for it in EXPANSION_PROPOSAL_S3 if it["source"] == "A")
    srcB = tuple(it["word"] for it in EXPANSION_PROPOSAL_S3 if it["source"] == "B")
    src_matrix = []
    for label, extra in [
        ("BASE_36 (扩词前)", ()),
        ("SRC_A_ONLY (推翻/冲突/非)", srcA),
        ("SRC_B_ONLY (庖丁解牛/小是具体)", srcB),
        ("SRC_A_PLUS_B (提案全量)", srcA + srcB),
    ]:
        mk = base_markers + extra
        cm = coverage_on(mk, held_ref, events, per_event)
        ca = coverage_on(mk, alt_idx, events, per_event)
        src_matrix.append({
            "arm": label,
            "n_markers_tuple": len(mk),
            "n_markers_distinct": len(set(mk)),
            "main_reading": {
                "n_divergent": cm["n_divergent"],
                "n_critical_among_divergent": cm["n_critical_among_divergent"],
                "div_critical_coverage": cm["div_critical_coverage"],
            },
            "alt_reading": {
                "n_divergent": ca["n_divergent"],
                "n_critical_among_divergent": ca["n_critical_among_divergent"],
                "div_critical_coverage": ca["div_critical_coverage"],
            },
        })

    # --- 2.6 8 件未命中根因（本棒逐件机械复核, 0 代为归因）---
    target8 = [12, 28, 37, 39, 47, 50, 72, 74]
    root_cause_8 = []
    for i in target8:
        e = events[i]
        rf = e.get("reasoning_full", "") or ""
        prov = e.get("_provenance", {})
        root_cause_8.append({
            "held_idx": i,
            "event_id": e.get("event_id"),
            "q_id": e.get("q_id"),
            "date": e.get("date"),
            "source_wave": prov.get("source_wave"),
            "pred": per_event[i]["pred"],
            "actual": per_event[i]["actual"],
            "divergent": per_event[i]["divergent"],
            "reasoning_full_len": len(rf),
            "reasoning_missing_flag": bool(e.get("reasoning_missing", False)),
            "covered_by_expansion": any(
                it["word"] in rf for it in EXPANSION_PROPOSAL_S3
            ),
            "covering_words": [it["word"] for it in EXPANSION_PROPOSAL_S3 if it["word"] in rf],
            "structural_class": (
                "EMPTY_TEXT" if not rf.strip()
                else ("COVERED_BY_EXPANSION" if any(it["word"] in rf for it in EXPANSION_PROPOSAL_S3)
                      else "NOT_COVERED_BY_PROPOSED_WORDS")
            ),
        })

    n_empty = sum(1 for r in root_cause_8 if r["structural_class"] == "EMPTY_TEXT")
    n_covered = sum(1 for r in root_cause_8 if r["structural_class"] == "COVERED_BY_EXPANSION")
    n_not_covered = sum(1 for r in root_cause_8 if r["structural_class"] == "NOT_COVERED_BY_PROPOSED_WORDS")

    # 覆盖率天花板（素材面结构性上限）
    ceiling_main = (cov_base_main["n_divergent"] - n_empty) / cov_base_main["n_divergent"]
    ceiling_alt = (cov_base_alt["n_divergent"] - n_empty) / cov_base_alt["n_divergent"]

    # --- 2.7 D1_supp loader 丢弃面（诚实交代, 0 修既有件）---
    d1_supp = json.loads(ADDENDUM_D1.read_text(encoding="utf-8"))
    loader_drop_finding = []
    for sup in d1_supp.get("supplements", []):
        has_rf = bool(sup.get("reasoning_full"))
        supp = sup.get("critical_reflection_supplement") or ""
        if not supp:
            continue
        idxs = [i for i, e in enumerate(events)
                if e.get("event_id") == sup.get("event_id")
                and e.get("_provenance", {}).get("source_wave") == "D1_supp"]
        for i in idxs:
            loaded = events[i].get("reasoning_full", "") or ""
            loader_drop_finding.append({
                "event_id": sup.get("event_id"),
                "held_idx": i,
                "q_id": sup.get("q_id"),
                "supplement_present_on_disk": bool(supp),
                "supplement_len": len(supp),
                "reasoning_full_present_on_disk": has_rf,
                "loaded_reasoning_full_len": len(loaded),
                "dropped_by_loader": (not has_rf) and bool(supp),
                "would_hit_36word_if_appended": has_critical_custom(supp, base_markers),
                "supplement_literal_head": supp[:60],
            })

    n_dropped = sum(1 for f in loader_drop_finding if f["dropped_by_loader"])
    n_dropped_would_hit = sum(
        1 for f in loader_drop_finding
        if f["dropped_by_loader"] and f["would_hit_36word_if_appended"]
    )

    # 情景读数（**仅诊断腿, 0 参与 K-V3S-3-4 判定**）:
    # 若 S3-F1 loader 分支条件修复（把 critical_reflection_supplement 并入 reasoning_full）,
    # idx=37/39 由「空文本」转为「有文本」⇒ 覆盖率读数变化多少？
    # 本腿 0 修既有件, 0 写盘既有件; 只在内存中构造对照文本。
    loaderfix_idx = sorted(
        f["held_idx"] for f in loader_drop_finding
        if f["dropped_by_loader"] and f["would_hit_36word_if_appended"]
    )
    _supp_by_idx = {
        f["held_idx"]: next(
            (s.get("critical_reflection_supplement") or ""
             for s in d1_supp.get("supplements", [])
             if s.get("event_id") == f["event_id"]),
            "",
        )
        for f in loader_drop_finding
    }
    _events_fix = [dict(e) for e in events]
    for i in loaderfix_idx:
        _events_fix[i] = dict(_events_fix[i])
        _events_fix[i]["reasoning_full"] = (
            (_events_fix[i].get("reasoning_full") or "") + " " + _supp_by_idx.get(i, "")
        ).strip()

    cov_fix_base_main = coverage_on(base_markers, held_ref, _events_fix, per_event)
    cov_fix_base_alt = coverage_on(base_markers, alt_idx, _events_fix, per_event)
    cov_fix_exp_main = coverage_on(expanded_markers, held_ref, _events_fix, per_event)
    cov_fix_exp_alt = coverage_on(expanded_markers, alt_idx, _events_fix, per_event)
    # 修复后天花板: 分母不变, 4 件空文本 -> 2 件真无文本(idx=47/50 reasoning_missing) + 2 件已被词覆盖
    n_empty_after_fix = sum(
        1 for r in root_cause_8
        if r["held_idx"] in loaderfix_idx
    )
    ceiling_main_after_fix = (
        (cov_base_main["n_divergent"] - (n_empty - n_empty_after_fix))
        / cov_base_main["n_divergent"]
    )
    ceiling_alt_after_fix = (
        (cov_base_alt["n_divergent"] - (n_empty - n_empty_after_fix))
        / cov_base_alt["n_divergent"]
    )

    # --- 2.8 S2 per-class 未命中分布（源 C 证据面）---
    s2 = json.loads(S2_RESULT.read_text(encoding="utf-8"))
    s2_pe = s2["s2_metrics"]["per_event"]
    s2_miss = [p for p in s2_pe if p["divergent"] and not p["critical"]]
    s2_per_class = {
        "n_divergent": sum(1 for p in s2_pe if p["divergent"]),
        "n_divergent_no_critical": len(s2_miss),
        "miss_idx": [p["held_idx"] for p in s2_miss],
        "miss_pred_class_distribution": dict(Counter(p["pred"] for p in s2_miss)),
        "miss_actual_class_distribution": dict(Counter(
            a for p in s2_miss for a in p["actual"]
        )),
        "all_pred_class_distribution": dict(Counter(p["pred"] for p in s2_pe)),
        "reading": (
            "S2 面 8 件未命中与 v3 K-V3-B 8 件（idx 12/28/37/39/47/50/72/74）**同集**; "
            "pred 类分布 CRITERIA 4 / UNKNOWN 4 ⇒ UNKNOWN 4 件全部 reasoning_full 为空 = "
            "**素材面缺料**（非词表覆盖不足）⇒ 源 C 只用于分诊, 不提供新词"
        ),
    }

    # --- 2.9 跨日 / 单日账（K-V3S-3-1 / -2 / -3 现状登记）---
    day_counts = Counter(e.get("date", "") for e in events)
    n_total = len(events)
    n_corr = meta["n_correction"]
    days = meta["distinct_days"]
    max_day, max_day_n = max(day_counts.items(), key=lambda kv: kv[1])
    max_ratio = max_day_n / n_total

    k_v3s_3_1_ok = bool(len(days) >= TH_CROSS_DAYS)
    k_v3s_3_2_ok = bool(max_ratio <= TH_SINGLE_DAY_RATIO)
    k_v3s_3_3_ok = bool(n_total >= TH_N_MIN and n_corr >= TH_N_CORRECTION)

    # K-V3S-3-4: 原 36 词口径判; 扩词口径 unfrozen 不判
    k_v3s_3_4_hit = bool(
        cov_base_main["div_critical_coverage"] < TH_CRITICAL_COV
        or cov_base_alt["div_critical_coverage"] < TH_CRITICAL_COV
    )

    result: Dict[str, Any] = {
        "schema": "v3_s3_wordexpand_result_v1",
        "series": "V3-S 补强系列 S3 段（数据面三合一 · 批判反思词表扩词段 · 本棒）",
        "prereg": "results/_v3_s_prereg_v1_2026_09_27.md",
        "executor": "results/_v3_s3_wordexpand_data/executor_2026_09_28.py",
        "date": DATE_FROZEN,
        "generated_ts_frozen": TS_FROZEN,
        "seed": SEED,
        "runtime": "python3 + numpy；0 LLM / 0 proxy / 0 gateway；词表扩词扫描为本地机械",
        "skill": {
            "requested": "scientific-research-workflows:experimental-design (plugin @scientific-research-workflows)",
            "status": "Local skill not found — C:/Users/Administrator/.minimax/plugins 实测 0 项（空目录）",
            "fallback": (
                "纪律锚 fallback = prereg §2.3 S3 四条字面 + questionnaire_v1 §0 采集协议 + "
                "verdict_v3 §2.3 K-V3-B 8 件字面"
            ),
            "disclosure": "未加载该 skill 的任何指令；0 引用、0 虚构其条文",
        },
        "inputs": inputs_meta,
        "input_chain_all_match": input_chain_all_match,
        "substrate": {
            "n_substrate_run": n_total,
            "held_out_count": len(held_ref),
            "held_out_ratio": HELD_OUT_RATIO,
            "held_out_seed": SEED,
            "held_out_idx": held_ref,
            "held_out_repro_bit_exact": held_repro_ok,
            "alt_reading_n": len(alt_idx),
            "alt_reading_idx": alt_idx,
            "alt_reading_correction_excluded_idx": corr_idx,
            "n_correction_total": n_corr,
            "same_as_v3": True,
            "extrapolation_boundary": (
                "仅在 77 件 RUN substrate + 23 件 held-out + v3 词表 36 词构造域内有效；"
                "不可外推至 S3 补采后的 substrate（≥85）或 S4 扩样（≥167）"
            ),
        },
        "alt_caliber": {
            "definition": "本棒 ALT = 主 held-out 23 件剔 correction 子集（is_correction_event_v3）= 18 件",
            "definition_source": "prereg §2.3 K-V3S-3-4「双口径并报」字面；v2 verdict §3.4 替代读法字面",
            "discrepancy_with_v3_registered": {
                "v3_registered_alt": {
                    "held_out_count": v3_res["alt_reading_corr_excluded"]["held_out_count"],
                    "n_divergent": v3_res["alt_reading_corr_excluded"]["n_divergent"],
                    "n_critical_among_divergent": v3_res["alt_reading_corr_excluded"]["n_critical_among_divergent"],
                    "div_critical_coverage": v3_res["alt_reading_corr_excluded"]["div_critical_coverage"],
                },
                "this_bench_alt_on_same_held_minus_correction": {
                    "n_divergent": cov_base_alt["n_divergent"],
                    "n_critical_among_divergent": cov_base_alt["n_critical_among_divergent"],
                    "div_critical_coverage": cov_base_alt["div_critical_coverage"],
                },
                "finding": (
                    "v3 result 登记的替代读法 (n_div=11 / n_crit=4) **不可由主 held-out 剔 correction 直接复算**"
                    "（该口径得 n_div=10 / n_crit=3）；v3 executor 内**无 alt_reading 实现函数**，"
                    "且 result_v3 alt 段**未登记 held_out_idx** ⇒ 该口径不可复现。"
                    "本棒 ALT 采用**显式可复现定义**并如实登记差异，0 静默沿用 v3 值"
                ),
                "root_cause": (
                    "构造/边界存疑（β）——口径不可复现，非观测差异；"
                    "0 代为归因 v3 worker 的实现过程"
                ),
                "probe": "本棒 0 穷举还原 v3 alt 的 seed / 划分；不作为 S3 判死输入",
            },
        },
        "word_table_baseline": {
            "n_markers_tuple": base_n,
            "n_markers_distinct": base_n_distinct,
            "duplicate_words_in_tuple": dup_words,
            "discrepancy_note": (
                f"v3 executor 字面记「36 词」/ ruleset_v3 §taxonomy 记 `v2_critical_marker_count=36`，"
                f"但 tuple 实际 distinct = {base_n_distinct}（重复字面 {dup_words}）"
                "⇒ 「36 词」= tuple 长度口径，非去重口径。**0 触动既有件**，如实登记"
            ),
            "n_events_with_reasoning": len(nonempty),
            "n_events_empty_reasoning": n_total - len(nonempty),
            "n_events_critical_36word": len(base_critical_idx),
            "critical_idx_36word": base_critical_idx,
        },
        "expansion_proposal": {
            "status": "unfrozen_pending_PI",
            "status_reason": (
                "P-S3-1 字面: 扩词清单 = 词表语义层变更，须先落盘入锁才允许重算覆盖率；"
                "本件为 worker 提案件，未入锁 ⇒ 扩词口径 **不判**"
            ),
            "n_proposed_words": len(EXPANSION_PROPOSAL_S3),
            "words": [it["word"] for it in EXPANSION_PROPOSAL_S3],
            "evidence_sources": {
                "A": "双复核实证边界词（派工单字面指认「推翻/冲突/非」）——本棒逐词 substrate 实测落点",
                "B": "G5 caliber_echo（d3c addendum caliber_echo 字段字面「小是具体」「庖丁解牛」）",
                "C": "S2 per-class 未命中分布（result_2026_09_27.json per_event 字面）——**只分诊，不提供新词**",
                "not_used": "0 自创词；未在三源实证面出现的候选词一律不提案",
            },
            "per_word_empirical": per_word,
            "proposal_list_literal": [it["word"] for it in EXPANSION_PROPOSAL_S3],
        },
        "sensitivity_matrix": {
            "caliber_note": (
                "同一 77 件 substrate / 同一 held-out 23 / 同一 v3 词表实现面，"
                "仅词表变 ⇒ Δ 可归因于扩词；双口径（MAIN / ALT）并报不择优"
            ),
            "before_after": {
                "before_36word": {
                    "n_markers_tuple": base_n,
                    "n_markers_distinct": base_n_distinct,
                    "main_reading": cov_base_main,
                    "alt_reading": cov_base_alt,
                },
                "after_expanded": {
                    "n_markers_tuple": expanded_n,
                    "n_markers_distinct": expanded_n_distinct,
                    "main_reading": cov_exp_main,
                    "alt_reading": cov_exp_alt,
                },
                "delta": {
                    "main_coverage_delta": cov_exp_main["div_critical_coverage"] - cov_base_main["div_critical_coverage"],
                    "alt_coverage_delta": cov_exp_alt["div_critical_coverage"] - cov_base_alt["div_critical_coverage"],
                    "main_newly_critical_divergent": sorted(
                        set(cov_exp_main["critical_idx"]) - set(cov_base_main["critical_idx"])
                    ),
                    "alt_newly_critical_divergent": sorted(
                        set(cov_exp_alt["critical_idx"]) - set(cov_base_alt["critical_idx"])
                    ),
                },
            },
            "by_source_arm": src_matrix,
            "side_effect_blind_obey": {
                "note": "扩词对 K-V3-C 盲从率的**副作用必并报**（诚实纪律：0 只报 coverage 改善）",
                "before_36word": blind_base_main,
                "after_expanded": blind_exp_main,
                "blind_rate_delta": blind_exp_main["blind_obey_rate"] - blind_base_main["blind_obey_rate"],
            },
        },
        "eight_miss_root_cause": {
            "target_idx": target8,
            "source_literal": "verdict_v3 §2.3 K-V3-B 字面 8 件无批判词分歧事件",
            "per_event": root_cause_8,
            "tally": {
                "n_empty_reasoning_structural": n_empty,
                "n_covered_by_expansion": n_covered,
                "n_not_covered_by_proposed_words": n_not_covered,
            },
            "finding": (
                f"8 件中 **{n_empty} 件 reasoning_full 为空**（idx 37/39/47/50）⇒ "
                "**素材面缺料（T-1）**，任何词表扩词对其 0 边际增益；"
                f"**{n_covered} 件**被本提案词覆盖；"
                f"**{n_not_covered} 件**（idx=74）未被三源实证词覆盖 ⇒ 覆盖率无法达 1.00"
            ),
            "coverage_ceiling_given_current_material": {
                "main_reading_ceiling": ceiling_main,
                "alt_reading_ceiling": ceiling_alt,
                "ceiling_reason": (
                    f"分母 {cov_base_main['n_divergent']} 件分歧中 {n_empty} 件无文本可命中 ⇒ "
                    f"理论上限 = ({cov_base_main['n_divergent']} - {n_empty}) / "
                    f"{cov_base_main['n_divergent']} = {ceiling_main}"
                ),
                "alt_ceiling_reason": (
                    f"ALT 分母 {cov_base_alt['n_divergent']} 件分歧中同为 {n_empty} 件无文本 ⇒ "
                    f"上限 = {ceiling_alt}"
                ),
                "implication": (
                    "⇒ **K-V3S-3-4 的 1.00 阈值在本盘素材面结构性不可达**（天花板 "
                    f"{ceiling_main:.4f} MAIN / {ceiling_alt:.4f} ALT）；"
                    "补 D1 8 件 / 补 reasoning_missing 件是唯一可达路径，**词表扩词不是**"
                ),
                "after_loaderfix_ceiling": {
                    "main_reading_ceiling": ceiling_main_after_fix,
                    "alt_reading_ceiling": ceiling_alt_after_fix,
                    "note": (
                        f"若 S3-F1 loader 修复（idx {loaderfix_idx} 文本并入），"
                        f"空文本件 {n_empty} → {n_empty - n_empty_after_fix}；"
                        "**即便如此仍 < 1.00**（idx 47/50 为 reasoning_missing=true 的真缺料件）"
                    ),
                },
            },
        },
        "loaderfix_diagnostic_leg": {
            "purpose": (
                "**诊断腿**: 量化 S3-F1 修复后的读数变化; **0 参与 K-V3S-3-4 判定**, "
                "**0 修既有件**（内存构造对照文本, 0 写盘）"
            ),
            "loaderfix_idx": loaderfix_idx,
            "before_fix": {
                "base36_main": cov_base_main["div_critical_coverage"],
                "base36_alt": cov_base_alt["div_critical_coverage"],
                "expanded_main": cov_exp_main["div_critical_coverage"],
                "expanded_alt": cov_exp_alt["div_critical_coverage"],
            },
            "after_fix": {
                "base36_main": cov_fix_base_main["div_critical_coverage"],
                "base36_alt": cov_fix_base_alt["div_critical_coverage"],
                "expanded_main": cov_fix_exp_main["div_critical_coverage"],
                "expanded_alt": cov_fix_exp_alt["div_critical_coverage"],
            },
            "per_caliber_detail_after_fix": {
                "base36_main": {
                    "n_divergent": cov_fix_base_main["n_divergent"],
                    "n_critical_among_divergent": cov_fix_base_main["n_critical_among_divergent"],
                    "div_critical_coverage": cov_fix_base_main["div_critical_coverage"],
                    "divergent_no_critical_idx": cov_fix_base_main["divergent_no_critical_idx"],
                },
                "base36_alt": {
                    "n_divergent": cov_fix_base_alt["n_divergent"],
                    "n_critical_among_divergent": cov_fix_base_alt["n_critical_among_divergent"],
                    "div_critical_coverage": cov_fix_base_alt["div_critical_coverage"],
                    "divergent_no_critical_idx": cov_fix_base_alt["divergent_no_critical_idx"],
                },
            },
            "honesty_note": (
                "本腿**只量化 loader 缺陷的影响面**, 不构成「修 loader 即达标」的结论; "
                "修复后覆盖率**仍 < 1.00**（idx 47/50 为 reasoning_missing=true 真缺料件）"
            ),
        },
        "loader_drop_finding": {
            "id": "S3-F1",
            "name": "D1_supp critical_reflection_supplement 被 loader 丢弃",
            "mechanism": (
                "v3 executor load_addendum_event_v3 的 reasoning 分支条件为 "
                "`if \"reasoning_full\" in sup and sup[\"reasoning_full\"]`；"
                "D1 addendum 3 件**只有 critical_reflection_supplement、无 reasoning_full 字段** ⇒ "
                "整条 supplement 从未进入 ev[\"reasoning_full\"]"
            ),
            "per_event": loader_drop_finding,
            "tally": {
                "n_supplements_present_on_disk": len(loader_drop_finding),
                "n_dropped_by_loader": n_dropped,
                "n_dropped_that_would_hit_36word_if_appended": n_dropped_would_hit,
            },
            "impact": (
                "idx=37 / idx=39（均 held-out 且 divergent、均计入 K-V3-B 8 件）"
                "在盘上**已有**批判反思文本却按空文本计入分母 ⇒ "
                "K-V3-B / K-V3S-3-4 的覆盖率**被系统性低估**；"
                "这是**构造面（loader）缺陷**，**不是词表覆盖不足**"
            ),
            "action_taken": (
                "**0 修既有件**（`ruleset_v3_executor.py` 只读）；本件仅登记发现 + 量化影响面，"
                "修复须另立预登记并由 PI 拍板"
            ),
            "root_cause_class": "β 构造面失灵（loader 分支条件过窄）",
            "pi_decision_required": True,
        },
        "s2_per_class_miss_distribution": s2_per_class,
        "kill_lines": KILL_LINES_S3,
        "judgment": {
            "k_v3s_3_1_ok": k_v3s_3_1_ok,
            "k_v3s_3_1_note": (
                f"distinct days = {len(days)} {days} vs 阈值 {TH_CROSS_DAYS} ⇒ "
                f"{'达标' if k_v3s_3_1_ok else '不达标'}；"
                "D1 8 件补采（今日 09-28）+ D6 波入库后重算；明日 D7 波达 5 天"
            ),
            "k_v3s_3_2_ok": k_v3s_3_2_ok,
            "k_v3s_3_2_note": (
                f"最大单日 = {max_day} {max_day_n}/{n_total} = {max_ratio:.4f} vs 阈值 {TH_SINGLE_DAY_RATIO} ⇒ "
                f"{'达标' if k_v3s_3_2_ok else '不达标'}（补采全部入库后须重算, 0 沿用旧值）"
            ),
            "k_v3s_3_3_ok": k_v3s_3_3_ok,
            "k_v3s_3_3_note": (
                f"N = {n_total} vs {TH_N_MIN} ⇒ {'达标' if n_total >= TH_N_MIN else '不达标'}; "
                f"纠正/反转 = {n_corr} vs {TH_N_CORRECTION} ⇒ "
                f"{'达标' if n_corr >= TH_N_CORRECTION else '不达标'}"
            ),
            "k_v3s_3_4_hit": k_v3s_3_4_hit,
            "k_v3s_3_4_note": (
                f"原 36 词口径：MAIN {cov_base_main['div_critical_coverage']:.4f} / "
                f"ALT {cov_base_alt['div_critical_coverage']:.4f}，均 < {TH_CRITICAL_COV} ⇒ hit=True"
            ),
            "k_v3s_3_4_expanded_caliber": {
                "status": "unfrozen_pending_PI",
                "judged": False,
                "reason": "扩词清单未入锁（P-S3-1 字面）⇒ 扩词口径 **不判**",
                "reported_value_only": {
                    "main_reading": cov_exp_main["div_critical_coverage"],
                    "alt_reading": cov_exp_alt["div_critical_coverage"],
                },
            },
            "any_hit_scope": "K-V3S-3-4 为判定面命中线（进判定汇总）; K-V3S-3-1/2/3 为采集面达标线（不进 FAIL 汇总）",
            "any_hit": k_v3s_3_4_hit,
            "root_cause": (
                "**β 构造/边界存疑主导**：8 件未命中中 4 件 reasoning_full 为空（素材面缺料）+ "
                "2 件（idx 37/39）loader 丢弃盘上已有文本 + 1 件（idx=74）三源实证词未覆盖 ⇒ "
                "词表覆盖不足**不是主因**；**α 真证伪面证据弱**（无非空文本件因词表边界漏检的显著证据）"
            ),
            "root_cause_three_way": {
                "alpha_true_falsification": "弱",
                "beta_construct_or_boundary": "主导",
                "sentinel_warning": "S3-F1 loader 丢弃面（覆盖率系统性低估）",
            },
        },
        "boundary_statement": {
            "no_extrapolation": (
                "本段结论仅在 77 件 RUN substrate + 23 件 held-out + v3 36 词构造域内有效；"
                "**不可外推**至补采后 substrate / S4 扩样 / 命题层"
            ),
            "no_killline_invention": "K-V3S-3-1..4 四条阈值全部沿既有件字面, 本棒 0 自设",
            "no_threshold_adjustment": "0 擅调; 1.00 未动",
            "no_derived_json_merge": "本件独立落盘, 0 合并任何既有 result JSON",
            "no_existing_file_touched": (
                "只读 import 既有件 0 字节改动; 目标件开跑前实测不在盘 ⇒ 纯新建"
            ),
            "no_llm": "0 LLM / 0 proxy / 0 gateway; 词表扫描为本地机械",
            "key_never_plaintext": "0 key 读取 / 0 落盘 / 0 入 prompt / 0 入 JSON / 0 入 log",
            "no_answer_substitution": (
                "采集题面 **0 代答**；PI 实时答题由 parent 走 ask_user 问卷，本棒仅出题面清单"
            ),
            "succeeded_not_done": "本件 = 扩词**提案**段, 非生效判定段; 入锁后方可重算并判",
        },
        "pi_pending_items": [
            {
                "id": "T-S3-1",
                "item": "扩词清单（推翻/冲突/非/庖丁解牛/小是具体 共 5 词）是否入锁",
                "recommendation": "建议**部分入锁**: 推翻/冲突/庖丁解牛 入锁; 非（单字过宽, 命中「非欧几何」）与小是具体（0 边际增益）不入锁",
                "worker_stance": "0 自决; 本棒仅列实测落点供 PI 裁断",
            },
            {
                "id": "T-S3-2",
                "item": "S3-F1 loader 丢弃面（D1_supp supplement 未进入 reasoning_full）是否修",
                "recommendation": "建议另立预登记修 loader 分支条件; 影响 idx=37/39 两件 held-out 分歧件的覆盖率分子",
                "worker_stance": "0 修既有件; 本棒只登记发现 + 量化影响",
            },
            {
                "id": "T-S3-3",
                "item": "K-V3S-3-4 的 1.00 阈值在本盘素材面结构性不可达（天花板 ~0.71）是否调整口径",
                "recommendation": "**0 擅调**; 建议 PI 明确: 是走补 reasoning_missing 件路径, 还是另立口径（阈值变更须 PI 显式给）",
                "worker_stance": "0 自决; 如实报天花板",
            },
            {
                "id": "T-S3-4",
                "item": "v3 登记的替代读法口径（n_div=11/n_crit=4）不可复现, 本棒 ALT 用了显式定义（n_div=10/n_crit=3）",
                "recommendation": "建议 PI 明示以哪一口径为准; 本棒 0 静默沿用 v3 值",
                "worker_stance": "如实登记差异, 0 代为归因 v3 worker 实现过程",
            },
        ],
        "honesty_note": (
            "本件所有读数均为盘上实测: substrate 由 v3 executor load_all_events_v3 只读载入（77 件）；"
            "held-out 23 由 RandomState(42) 复现 result_v3 登记值 **bit-exact**；"
            "coverage 分母/分子沿 v3 executor 字面（divergent 件数 / divergent 且批判词命中件数）。"
            "扩词 5 词全部出自派工单指认的三源实证面, **0 自创词**; 每词落点在 77 件 substrate 上逐件实测。"
            "本件为**提案件非生效件**: 扩词清单未入锁 ⇒ K-V3S-3-4 扩词口径 status=unfrozen_pending_PI, **不判**。"
            "如实登记三处不利读数: (i) 8 件未命中中 4 件 reasoning_full 为空（素材面缺料, 词表扩词 0 边际增益）; "
            "(ii) idx 37/39 的批判反思文本**在盘上存在**但被 v3 loader 分支条件丢弃（S3-F1, β 构造面缺陷）"
            "⇒ 覆盖率被系统性低估; (iii) v3 登记的替代读法口径不可复现, 本棒 ALT 用显式定义。"
            "扩词对盲从率的副作用（idx 23 由盲从转非盲从）**并报**, 0 只报 coverage 改善。"
        ),
        "next_link_in_chain": (
            "results/_v3_s3_collection_brief_2026_09_28.md（D1 补采 8 件 + D6 波题面清单）"
        ),
    }

    return result


if __name__ == "__main__":
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    res = main()
    OUT_RESULT.write_text(
        json.dumps(res, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"written: {OUT_RESULT}")
    print(f"sha12: {sha12_file(OUT_RESULT)}")
    print(f"bytes: {OUT_RESULT.stat().st_size}")
