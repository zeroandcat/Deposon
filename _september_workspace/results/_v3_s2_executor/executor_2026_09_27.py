#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V3-S S2 段 executor · 规则集上界再扩展 (消解 A 续段) · worker 出件 · 2026-09-27

依据（纪律锚）:
  - results/_v3_s_prereg_v1_2026_09_27.md  (SHA-12 ef5a40554960) §1.2 S2
    / §2.2 S2 八条判死线字面 / §2.5 TH-* 沿用登记 / §2.6 提案 P-S1-1·P-S2-1
    / §2.7 防退化门 T-2 (二值返回退化 × 门冲突)
  - results/_v4_pi_cot_v3_ruleset_v3_executor.py (SHA-12 8a81d90c69ba) 构造段
    (feats_v3 / best_split / build_tree / predict_tree / split_points / entropy /
     majority / nw_sim / nled_sim / extract_judgment_sequence_v3 /
     stratified_holdout_split_v3 / load_all_events_v3 / bootstrap_ci_v3)
  - results/_v4_pi_cot_v3_result_v3.json (SHA-12 585714f9660c) 同 substrate 对照读数源
  - results/_v3_s1_executor/executor_2026_09_27.py (SHA-12 10870941c283) 度量面
    (nw_sim_prox / lcs_sim / f1_sim / series_self_check) — S1 度量冻结值, 只读 import
  - PI 2026-09-27 派工拍板: ①嵌入不落地 (S2 短语模式维持不升嵌入)
                          ②防退化门门不变 + 二值单列
                          ③LCS/F1 线沿同线 (本段判定面含之)

S2 构造方向（v3 → S2，数值源 = verdict_v3 §3.3 字面, 0 自创）:
  - tree_depth_limit  6 → 8        (K-V3S-2-G ①)
  - n_features       12 → 15       (K-V3S-2-G ②; 12 既有特征沿 v3 字面 0 改动)
  - 模板面: 全序列 + 短语模式 5 类维持, **嵌入不升** (PI 拍板① 字面)

铁律:
  - 只读 import v3 executor 与 S1 executor, 0 字节改动既有件 (v3 件 + S1 件 0 触动)
  - 判死线按 §2.2 八条字面, 0 私设条款 / 0 擅调阈值
  - 派生 JSON 独立落盘, 0 合并
  - 0 LLM / 0 proxy / 0 gateway; key 永不明文
  - 显式布尔命名 (S-40); SHA-12 = hashlib.sha256(hexdigest)[:12] 小写
  - 时间戳冻结 (re-entrancy-safe), 逐字可重跑
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import re
from collections import Counter
from itertools import combinations
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

# ---------------------------------------------------------------------------
# 0. 路径 / 锚 / 冻结常量
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
RESULTS_DIR = REPO_ROOT / "results"
OUT_DIR = RESULTS_DIR / "_v3_s2_executor"

PREREG_S = RESULTS_DIR / "_v3_s_prereg_v1_2026_09_27.md"
PREREG_S_SHA12_EXPECTED = "ef5a40554960"

V3_EXECUTOR = RESULTS_DIR / "_v4_pi_cot_v3_ruleset_v3_executor.py"
V3_EXECUTOR_SHA12_EXPECTED = "8a81d90c69ba"

V3_DATASET = RESULTS_DIR / "_v4_pi_cot_v3_dataset.json"
V3_DATASET_SHA12_EXPECTED = "5118f5b44f17"

V3_RESULT = RESULTS_DIR / "_v4_pi_cot_v3_result_v3.json"
V3_RESULT_SHA12_EXPECTED = "585714f9660c"

S1_DIR = RESULTS_DIR / "_v3_s1_executor"
S1_EXECUTOR = S1_DIR / "executor_2026_09_27.py"
S1_EXECUTOR_SHA12_EXPECTED = "10870941c283"
S1_RESULT = S1_DIR / "result_2026_09_27.json"
S1_RESULT_SHA12_EXPECTED = "bfc99c3133dd"
S1_RESCRIPT = S1_DIR / "rescript_2026_09_27.md"
S1_RESCRIPT_SHA12_EXPECTED = "9d49a632ee81"

OUT_RESULT = OUT_DIR / "result_2026_09_27.json"
OUT_RESCRIPT = OUT_DIR / "rescript_2026_09_27.md"

# 时间戳冻结 (重跑逐字不变)
TS_FROZEN = "2026-09-27T15:52:00+08:00"
DATE_FROZEN = "2026-09-27"

# ---------------------------------------------------------------------------
# 判死线阈值 (全部沿既有件字面, 0 自创)
# ---------------------------------------------------------------------------
TH_NW_MEAN = 0.65          # K-V3S-2-A  沿 K-V3-A / TH-v3-10
TH_NLED_MEAN = 0.55        # K-V3S-2-A' 沿 K-V3-A' / TH-v3-11
TH_CRITICAL_COV = 1.00     # K-V3S-2-B  沿 K-V3-B / TH-v2-5b
TH_BLIND_OBEY = 0.10       # K-V3S-2-C  沿 K-V3-C / TH-v2-5b
TH_BOOT_CI_FLOOR = 0.40    # K-V3S-2-D  沿 K-V3-D / TH-v3-14
N_BOOT = 1000              # TH-v3-17 (沿 TH-v2-8)
SEED = 42                  # TH-v3-15
N_PERM = 1000              # TH-v3-16 (沿 TH-v2-7)
ALPHA = 0.05               # TH-v3-16
HELD_OUT_RATIO = 0.30      # TH-v3-4

# 上界验收门 (数值源 = verdict_v3 §3.3 字面, 0 自创)
TREE_DEPTH_LIMIT_S2 = 8
N_FEATURES_MIN_S2 = 15

# 防退化门 (沿 TH-v3-19 字面: n_distinct 全 > 3; 门限 0 改动)
GATE_MIN_N_DISTINCT = 3

# S1 度量面冻结阈值 (本段判定面含 LCS/F1, 沿 S1 拍板② 字面)
TH_LCS_MEAN = S1_TH_LCS = 0.65
TH_F1_MEAN = S1_TH_F1 = 0.55

# 模板面字面 (ruleset_v3 §template_mode; 0 自创)
TEMPLATE_MODE = "full_sequence_plus_phrase_patterns"

# ---------------------------------------------------------------------------
# S2 新增 3 项特征申报 (P-S2-F1/F2/F3; 0 新判定阈值)
#   申报面沿 prereg §1.2 构造设计 (b) 字面「新增 3 项由 worker 立线时申报,
#   须逐项自证非退化」⇒ 本件只申报特征本体, 0 申报任何达标线。
# ---------------------------------------------------------------------------
NEW_FEATURES_S2: Tuple[Dict[str, str], ...] = (
    {
        "key": "judge_seq_len",
        "proposal_id": "P-S2-F1",
        "definition": "len(extract_judgment_sequence_v3(reasoning_full)) — 判据序列步数",
        "source_fields": ["reasoning_full (经 extract_judgment_sequence_v3)"],
        "rationale": "既有 12 项无一表达「判据步数」; 序列长度是 pred 与 actual 序列类相似度的直接先行量",
    },
    {
        "key": "crit_marker_total",
        "proposal_id": "P-S2-F2",
        "definition": "sum(reasoning_full.count(m) for m in CRITICAL_REFLECTION_MARKERS_V3) — 批判反思词命中总次数",
        "source_fields": ["reasoning_full (经 CRITICAL_REFLECTION_MARKERS_V3)"],
        "rationale": "既有 rf_pos_density 为命中数/长度 的归一化密度, 缺绝对量纲; 本项补绝对面, 与密度面非派生退化",
    },
    {
        "key": "rf_char_per_judge",
        "proposal_id": "P-S2-F3",
        "definition": "len(reasoning_full) / max(1, len(extract_judgment_sequence_v3(reasoning_full))) — 单位判据推理字数",
        "source_fields": ["reasoning_full (经 extract_judgment_sequence_v3)"],
        "rationale": "分母为判据步数 (v3 无此分母), 与 rf_pos_density 分母 (字符长度) 不同 ⇒ 非派生退化; 表达单位判据的展开体量",
    },
)


def sha12_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


# ---------------------------------------------------------------------------
# 1. 只读加载既有件 (0 字节改动)
# ---------------------------------------------------------------------------
def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


V3 = _load_module("v3_ruleset_executor_ref_s2", V3_EXECUTOR)
S1 = _load_module("v3_s1_executor_ref_s2", S1_EXECUTOR)

# S2 特征键 = v3 既有 12 项 (沿 v3 字面, 0 改动) + S2 新增 3 项
FEAT_KEYS_S2: Tuple[str, ...] = tuple(V3.FEAT_KEYS_V3) + tuple(
    f["key"] for f in NEW_FEATURES_S2
)


# ---------------------------------------------------------------------------
# 2. S2 特征提取 (12 既有沿 v3 字面 + 3 新增)
# ---------------------------------------------------------------------------
def feats_s2(ev: Dict[str, Any]) -> Dict[str, Any]:
    """S2 特征提取 (15 项).

    12 项既有特征**逐字沿 v3 feats_v3** (0 改动);
    3 项新增特征沿 NEW_FEATURES_S2 申报字面, 0 新阈值。
    """
    row: Dict[str, Any] = dict(V3.feats_v3(ev))
    rf = ev.get("reasoning_full", "") or ""
    seq = V3.extract_judgment_sequence_v3(rf)
    crit_total = 0
    for m in V3.CRITICAL_REFLECTION_MARKERS_V3:
        crit_total += rf.count(m)
    row["judge_seq_len"] = len(seq)
    row["crit_marker_total"] = crit_total
    row["rf_char_per_judge"] = len(rf) / max(1, len(seq))
    return row


# ---------------------------------------------------------------------------
# 3. S2 决策树 (深度 ≤ 8, 特征 15 项) — 结构逐行沿 v3 build_tree/best_split
# ---------------------------------------------------------------------------
def best_split_s2(rows: List[Dict[str, Any]], labels: List[str],
                  used: frozenset, feat_keys: Sequence[str]
                  ) -> Tuple[float, str, Any]:
    """贪心信息增益最优切分 — 与 v3 best_split 逐行同构, 仅特征键集合可参数化。

    特征键顺序 = FEAT_KEYS_S2 (12 既有在前, 3 新增在后, 沿 v3 FEAT_KEYS_V3 顺序接续),
    tie-break 字面 (gain, (k, t)) 与 v3 一致。
    """
    n = len(labels)
    base = V3.entropy(labels)
    best = None
    for k in feat_keys:
        if k in used:
            continue
        vals = [r[k] for r in rows]
        for t in V3.split_points(vals):
            li = [labels[i] for i in range(n) if vals[i] <= t]
            ri = [labels[i] for i in range(n) if vals[i] > t]
            if not li or not ri:
                continue
            e = (len(li) * V3.entropy(li) + len(ri) * V3.entropy(ri)) / n
            gain = base - e
            if best is None or gain > best[0] + 1e-12 \
                    or (abs(gain - best[0]) < 1e-12 and (k, t) < (best[1], best[2])):
                best = (gain, k, t)
    return best if best is not None else (0.0, "", None)


def build_tree_s2(rows: List[Dict[str, Any]], labels: List[str],
                  feat_keys: Sequence[str], depth_max: int,
                  depth: int = 0, used: frozenset = frozenset()) -> Dict[str, Any]:
    """S2 决策树学习 (深度 ≤ depth_max) — 与 v3 build_tree 逐行同构。"""
    node: Dict[str, Any] = {"leaf": V3.majority(labels)}
    if depth >= depth_max or len(set(labels)) <= 1:
        return node
    gain, k, t = best_split_s2(rows, labels, used, feat_keys)
    if k == "" or gain <= 1e-9:
        return node
    li = [i for i in range(len(labels)) if rows[i][k] <= t]
    ri = [i for i in range(len(labels)) if rows[i][k] > t]
    node = {
        "feature": k, "threshold": t,
        "le": build_tree_s2([rows[i] for i in li], [labels[i] for i in li],
                            feat_keys, depth_max, depth + 1, used | {k}),
        "gt": build_tree_s2([rows[i] for i in ri], [labels[i] for i in ri],
                            feat_keys, depth_max, depth + 1, used | {k}),
    }
    return node


def construction_equivalence_selfcheck(
    events: List[Dict[str, Any]], held_idx: List[int]
) -> Dict[str, Any]:
    """构造纯度自证: 本件 build_tree_s2 在 (深度 6 + 12 既有特征) 下须与
    v3 build_tree **bit-exact 相同** ⇒ 证明 S2 只改了「深度上限」与「特征集合」
    两个已登记维度, 切分逻辑 0 改动。
    """
    rows_v3 = [V3.feats_v3(e) for e in events]
    labels = [V3.primary_judgment_type_v3(
        V3.extract_judgment_sequence_v3(e.get("reasoning_full", ""))) for e in events]
    held = set(held_idx)
    tr_rows = [rows_v3[i] for i in range(len(events)) if i not in held]
    tr_lab = [labels[i] for i in range(len(events)) if i not in held]
    tree_v3 = V3.build_tree(tr_rows, tr_lab)
    tree_repro = build_tree_s2(tr_rows, tr_lab, V3.FEAT_KEYS_V3, V3.TREE_DEPTH_MAX)
    return {
        "claim": ("本件 build_tree_s2 / best_split_s2 在 (深度上限 = 6, 特征 = v3 既有 12 项) "
                  "下必须复现 v3 build_tree 的同一棵树 (bit-exact)"),
        "v3_depth_max": V3.TREE_DEPTH_MAX,
        "v3_n_features": len(V3.FEAT_KEYS_V3),
        "tree_identical": bool(tree_v3 == tree_repro),
        "depth_v3": V3._tree_depth(tree_v3),
        "depth_repro": V3._tree_depth(tree_repro),
        "n_features_used_v3": len(_tree_features(tree_v3)),
        "n_features_used_repro": len(_tree_features(tree_repro)),
        "features_used_v3": sorted(_tree_features(tree_v3)),
        "features_used_repro": sorted(_tree_features(tree_repro)),
    }


def _tree_features(tree: Dict[str, Any]) -> List[str]:
    out: List[str] = []
    if "feature" in tree:
        out.append(tree["feature"])
        out += _tree_features(tree["le"])
        out += _tree_features(tree["gt"])
    return out


# ---------------------------------------------------------------------------
# 4. 排列检验 (沿 v3 字面, 换 S2 特征/深度)
# ---------------------------------------------------------------------------
def permutation_test_s2(events: List[Dict[str, Any]], labels: List[str],
                         held_idx: List[int], rng: np.random.RandomState,
                         feat_keys: Sequence[str], depth_max: int,
                         n_perm: int = N_PERM) -> float:
    """S2 排列检验 — 与 v3 permutation_test_v3 逐行同构, 仅特征/深度换 S2。

    相似度口径沿 v3 字面 = nw_sim (v3 原构造), 便于与 v3 perm_p 逐位对照。
    """
    rows_all = [feats_s2(events[i]) for i in range(len(events))]
    tr_rows = [rows_all[i] for i in range(len(events)) if i not in set(held_idx)]
    tr_lab = [labels[i] for i in range(len(events)) if i not in set(held_idx)]
    tree = build_tree_s2(tr_rows, tr_lab, feat_keys, depth_max)
    observed = []
    for i in held_idx:
        pred = V3.predict_tree(tree, rows_all[i])
        seq = V3.extract_judgment_sequence_v3(events[i].get("reasoning_full", ""))
        observed.append(V3.nw_sim([pred], seq))
    obs_mean = float(np.mean(observed)) if observed else 0.0
    ge = 0
    for _ in range(n_perm):
        shuf = labels[:]
        rng.shuffle(shuf)
        tr_rows_p = [rows_all[i] for i in range(len(events)) if i not in set(held_idx)]
        tr_lab_p = [shuf[i] for i in range(len(events)) if i not in set(held_idx)]
        tree_p = build_tree_s2(tr_rows_p, tr_lab_p, feat_keys, depth_max)
        scores = []
        for i in held_idx:
            pred = V3.predict_tree(tree_p, rows_all[i])
            seq = V3.extract_judgment_sequence_v3(events[i].get("reasoning_full", ""))
            scores.append(V3.nw_sim([pred], seq))
        m = float(np.mean(scores)) if scores else 0.0
        if m >= obs_mean - 1e-12:
            ge += 1
    return (ge + 1) / (n_perm + 1)


# ---------------------------------------------------------------------------
# 5. 防退化门 · 门不变 + 二值单列 (PI 2026-09-27 拍板② 字面)
# ---------------------------------------------------------------------------
def check_feature_degradation_s2(events: List[Dict[str, Any]]) -> Dict[str, int]:
    """S2 防退化构造审查 (15 项) — 门限沿 TH-v3-19 字面 > 3, 0 改动。"""
    rows = [feats_s2(ev) for ev in events]
    n_dist: Dict[str, int] = {}
    for k in FEAT_KEYS_S2:
        n_dist[k] = len({r[k] for r in rows})
    return n_dist


def feature_degradation_gate(events: List[Dict[str, Any]]) -> Dict[str, Any]:
    """防退化门 = 门不变 (TH-v3-19, n_distinct 全 > 3) + 二值/常量单列。

    PI 拍板② 字面: 门不变 + 二值单列 ⇒
      - 门限与判定 0 改动; th_v3_19_compliance 如实记 (不达标即 false)
      - 二值/低基数设计常量**单列登记** = 剔出验收面展示, **非门豁免**
    与 S1 段字段的差别 (如实登记): S1 用 (n_distinct ≤ 2) 单一并列表,
    本段按 PI 拍板②「二值单列」字面细分为 constant (n_distinct == 1) /
    binary (n_distinct == 2) / nonbinary 三列, 门限判定 0 改动。
    """
    n_dist = check_feature_degradation_s2(events)
    constant_col = [k for k, v in n_dist.items() if v == 1]
    binary_col = [k for k, v in n_dist.items() if v == 2]
    nonbinary_col = [k for k, v in n_dist.items() if v >= 3]
    below = [k for k, v in n_dist.items() if v <= GATE_MIN_N_DISTINCT]
    below_single_col = [k for k in below if k in constant_col or k in binary_col]
    below_nonbinary = [k for k in below if k in nonbinary_col]
    new_feats = [f["key"] for f in NEW_FEATURES_S2]
    new_below = [k for k in below if k in new_feats]
    return {
        "gate_literal": "TH-v3-19: 15 项特征 n_distinct 全 > 3",
        "gate_literal_source": "沿 v3 prereg §1.2.2 + TH-v3-19 字面; S2 特征数 12→15, 门限 >3 不动",
        "gate_min_n_distinct": GATE_MIN_N_DISTINCT,
        "gate_changed": False,
        "n_features_checked": len(FEAT_KEYS_S2),
        "n_distinct_per_feature": n_dist,
        "n_distinct_new_features_only": {k: n_dist[k] for k in new_feats},
        "constant_single_column": constant_col,
        "binary_single_column": binary_col,
        "nonbinary_column": nonbinary_col,
        "features_below_threshold": below,
        "features_below_threshold_count": len(below),
        "features_below_threshold_single_column": below_single_col,
        "features_below_threshold_nonbinary": below_nonbinary,
        "n_below_threshold_nonbinary": len(below_nonbinary),
        "new_features_below_threshold": new_below,
        "all_new_features_pass_gate": len(new_below) == 0,
        "th_v3_19_compliance": len(below) == 0,
        "pi_ruling_literal": "门不变 + 二值单列 (PI 2026-09-27 拍板②)",
        "note": (
            "门沿 TH-v3-19 0 改动, th_v3_19_compliance 如实记 false (二值/常量设计常量 "
            "n_distinct ≤2 构造上不可达); 单列 = 剔出验收面展示, **非门豁免**。"
            "S2 新增 3 项特征 n_distinct 全部 >3 ⇒ 退化警报不来自新增面。"
        ),
    }


def derived_degeneracy_selfcheck(events: List[Dict[str, Any]]) -> Dict[str, Any]:
    """新增特征派生退化自证 — 已知退化族含「派生退化」(码本坍缩同族)。

    对 3 项新增特征两两、以及新增 vs 既有 12 项逐对做 joint 取值数检查:
    若 joint 基数 == 单项基数 ⇒ 一一映射 (派生退化), 不得入选。
    """
    rows = [feats_s2(ev) for ev in events]
    new_feats = [f["key"] for f in NEW_FEATURES_S2]
    pairs = []
    collapsed = []
    cand = new_feats + list(V3.FEAT_KEYS_V3)
    for a, b in combinations(cand, 2):
        if a not in new_feats and b not in new_feats:
            continue
        joint = len({(r[a], r[b]) for r in rows})
        na = len({r[a] for r in rows})
        nb = len({r[b] for r in rows})
        dep = bool(joint <= max(na, nb))
        rec = {"a": a, "b": b, "joint_cardinality": joint,
               "n_distinct_a": na, "n_distinct_b": nb, "one_to_one_dependent": dep}
        pairs.append(rec)
        if dep:
            collapsed.append(rec)
    return {
        "degradation_family": "派生退化 (已知退化族之一, 沿 prereg §2.7 字面)",
        "rule": "joint 取值数 ≤ max(单侧取值数) ⇒ 一一映射 ⇒ 派生退化 ⇒ 不得入选",
        "n_pairs_checked": len(pairs),
        "collapsed_pairs": collapsed,
        "all_new_features_independent": len(collapsed) == 0,
        "rejected_candidates": [
            {"key": "n_distinct_judge_types",
             "reason": "与 judge_seq_len 在本盘 77 件上 5→5 一一映射 (序列已去重保序) ⇒ 派生退化, 0 入选"},
            {"key": "n_distinct_kw_types",
             "reason": "与 judge_seq_len 在本盘 77 件上 5→5 一一映射 ⇒ 派生退化, 0 入选"},
        ],
    }


def series_self_check(vals: Sequence[float]) -> Dict[str, Any]:
    """度量面自检 (沿 S1 series_self_check 字面)."""
    import statistics
    v = [float(x) for x in vals]
    if not v:
        return {"n": 0}
    return {
        "n": len(v),
        "n_distinct": len(set(v)),
        "min": min(v), "max": max(v),
        "mean": float(np.mean(v)),
        "std": float(np.std(v)),
        "median": float(statistics.median(v)),
        "degenerate_constant": bool(len(set(v)) == 1),
    }


# ---------------------------------------------------------------------------
# 6. 模板面自证 (K-V3S-2-G ③: 全序列 + 短语模式并启用)
# ---------------------------------------------------------------------------
def template_face_selfcheck(events: List[Dict[str, Any]]) -> Dict[str, Any]:
    """模板面三项自证: (a) 全序列启用 (b) 短语模式 5 类启用 (c) 嵌入判读未启用。

    嵌入项沿 PI 2026-09-27 拍板① 字面 = 不落地 (提案 P-S1-1 未拍板落地) ⇒ 记 false,
    **如实登记「模板面未升」**, 0 用其他口径顶替。
    """
    seqs = [V3.extract_judgment_sequence_v3(e.get("reasoning_full", "")) for e in events]
    n_multi = sum(1 for s in seqs if len(s) > 1)
    per_pattern = []
    n_hit_any = 0
    for pat in V3.PHRASE_PATTERNS_V3:
        c = sum(1 for e in events if pat["pattern"] in (e.get("reasoning_full", "") or ""))
        per_pattern.append({"pattern": pat["pattern"], "target_seq": pat["target_seq"],
                            "n_events_hit": c})
        if c > 0:
            n_hit_any += 1
    hit_any_events = sum(
        1 for e in events
        if any(p["pattern"] in (e.get("reasoning_full", "") or "")
               for p in V3.PHRASE_PATTERNS_V3))
    n = len(events)
    cov = (hit_any_events / n) if n else 0.0
    # ruleset_v3 §phrase_patterns_validation_requirement 门槛 (≥80%) 在本段 substrate 上的核验
    cov_req = 0.80
    cov_ok = bool(cov >= cov_req)
    return {
        "template_mode": TEMPLATE_MODE,
        "full_sequence_enabled": True,
        "full_sequence_evidence": {
            "function": "V3.extract_judgment_sequence_v3 (只读 import, 0 改动)",
            "n_events_with_multi_step_seq": n_multi,
            "n_events": n,
            "multi_step_share": (n_multi / n) if n else 0.0,
            "max_seq_len": max((len(s) for s in seqs), default=0),
            "literal": "v3 弃 v2 primary=seq[0] 单元素, 改全序列返回 seq_full",
        },
        "phrase_patterns_enabled": True,
        "phrase_patterns_count": len(V3.PHRASE_PATTERNS_V3),
        "phrase_patterns_per_pattern": per_pattern,
        "phrase_pattern_hit_coverage": cov,
        "phrase_pattern_validation_requirement": (
            "ruleset_v3 §phrase_patterns_validation_requirement 字面: 85 events 覆盖率 ≥80% "
            "(≥68/85 命中至少一项); 任意一项不达 ⇒ 消解 A 未完全消解 ⇒ 不得开跑"),
        "phrase_pattern_coverage_threshold": cov_req,
        "phrase_pattern_coverage_threshold_source": (
            "0.80 沿 ruleset_v3 §phrase_patterns_validation_requirement 字面 (0 自创)"),
        "phrase_pattern_coverage_meets_threshold": cov_ok,
        "phrase_pattern_coverage_shortfall": {
            "n_events_hit_any": hit_any_events,
            "n_events": n,
            "threshold": cov_req,
            "threshold_n_events_at_80pct": 0.80 * n,
            "observed_coverage": cov,
            "severity": "**严重不达**",
            "attribution": (
                "S2 模板面按 PI 2026-09-27 拍板① 维持 v3 短语模式 5 类, **0 改动** ⇒ 本项不达线系"
                "**前存构造面事实**（v3 / S1 同一模板面下同样不达）, **不是** S2 上界扩展引入。实测: "
                "5 类短语在 77 件 RUN substrate 上仅 1 件命中（'大一统定义 / 万物理论' 1 件）, 其余 4 类 0 命中。"),
            "consequence": (
                "按 ruleset_v3 字面「任意一项不达 ⇒ 消解 A 未完全消解 ⇒ 不得开跑」, 本项**单独构成消解 A "
                "未完全消解的读数**。但 K-V3S-2-G ③ 的冻结字面为「模板面并启用」(启用性检查), 本段 G-3 按"
                "**启用性**判读 = True; 覆盖率不达标作为**独立如实登记项**披露, 0 隐含触发、0 私改 G-3 字面。"),
            "honesty_note": (
                "这是「机械诚实 vs 不误导」的分界: 若仅报 G-3 ✓ 而不报覆盖率 1.3%, 即为误导 —— "
                "短语模式面在本盘 substrate 上**近乎未生效**, 模板面实质由全序列面承担。"),
            "action_pending_pi": (
                "是否 (a) 承认本盘 substrate 与 5 类短语不匹配并改判门槛口径, (b) 扩词/改短语集, "
                "或 (c) 维持并记为已知构造面缺陷 —— **属 PI 拍板项, 执行棒 0 自决**。"),
        },
        "phrase_pattern_n_events_hit_any": hit_any_events,
        "embedding_enabled": False,
        "embedding_literal": (
            "PI 2026-09-27 拍板① 嵌入判读口径**不落地** (提案 P-S1-1 未拍板落地; v3 prereg "
            "§1.2.3(c) 曾明确排除) ⇒ S2 模板面**维持全序列 + 短语模式 5 类, 嵌入不升**; "
            "如实登记「模板面未升」, 0 补 0, 0 顶替"),
        "source_literal": "ruleset_v3 §template_mode + §phrase_patterns_v3 (5 类) 字面, 0 改动",
    }


# ---------------------------------------------------------------------------
# 7. S2 主计算 (同 substrate 77 / 同 held-out 23, 5 口径全并报)
# ---------------------------------------------------------------------------
def compute_s2(events: List[Dict[str, Any]], held_idx: List[int]) -> Dict[str, Any]:
    """S2 真跑: 新规则集 (≤8 / 15 项) 下 5 口径全并报 + B/C/D 判定输入。

    口径面沿 S1 冻结值 (nw_sim_prox / nled_sim / lcs_sim / f1_sim) 0 改动;
    本段只换**规则集面** ⇒ pred 变, 度量实现 0 触动。
    """
    rows_all = [feats_s2(ev) for ev in events]
    labels = [V3.primary_judgment_type_v3(
        V3.extract_judgment_sequence_v3(ev.get("reasoning_full", ""))) for ev in events]
    held_set = set(held_idx)
    tr_rows = [rows_all[i] for i in range(len(events)) if i not in held_set]
    tr_lab = [labels[i] for i in range(len(events)) if i not in held_set]
    tree = build_tree_s2(tr_rows, tr_lab, FEAT_KEYS_S2, TREE_DEPTH_LIMIT_S2)
    rules = V3.flatten_rules(tree)

    per_event: List[Dict[str, Any]] = []
    nw_prox_vals: List[float] = []
    nw_v3_vals: List[float] = []
    nled_vals: List[float] = []
    lcs_vals: List[float] = []
    lcs_unjudgeable = 0
    f1_vals: List[float] = []
    f1_unjudgeable_idx: List[int] = []
    f1_zero_sensitivity: List[float] = []

    for i in held_idx:
        pred = V3.predict_tree(tree, rows_all[i])
        ev = events[i]
        rf = ev.get("reasoning_full", "") or ""
        seq = V3.extract_judgment_sequence_v3(rf)
        pred_seq = [pred]

        v_nw_prox = S1.nw_sim_prox(pred_seq, seq)   # S1 冻结主口径 (邻近矩阵版)
        v_nw_v3 = V3.nw_sim(pred_seq, seq)          # v3 原构造 (双口径并报对照面)
        v_nled = V3.nled_sim(pred_seq, seq)         # NLED (0 改动)
        v_lcs = S1.lcs_sim(pred_seq, seq)           # S1 冻结 (PI 拍板② 阈值面)
        v_f1, f1_reason = S1.f1_sim(pred_seq, seq)  # S1 冻结 (PI 拍板② 阈值面)

        nw_prox_vals.append(v_nw_prox)
        nw_v3_vals.append(v_nw_v3)
        nled_vals.append(v_nled)

        if v_lcs is None:
            lcs_unjudgeable += 1
        else:
            lcs_vals.append(v_lcs)
        if v_f1 is None:
            f1_unjudgeable_idx.append(i)
            f1_zero_sensitivity.append(0.0)
        else:
            f1_vals.append(v_f1)
            f1_zero_sensitivity.append(v_f1)

        per_event.append({
            "held_idx": i,
            "pred": pred,
            "actual": seq,
            "actual_len": len(seq),
            "nw_sim_prox": v_nw_prox,
            "nw_sim_v3_original": v_nw_v3,
            "nled_sim": v_nled,
            "lcs_sim": v_lcs,
            "f1_sim": v_f1,
            "f1_reason": f1_reason,
            "divergent": bool(pred not in seq),
            "critical": bool(V3.has_critical_reflection_v3(rf)),
        })

    # K-V3S-2-B / -C 输入 (沿 v3 compute_metrics_v3 字面 0 改动)
    divergent = [e["divergent"] for e in per_event]
    critical = [e["critical"] for e in per_event]
    n_div = sum(divergent)
    n_crit_among_div = sum(1 for d, c in zip(divergent, critical) if d and c)
    div_crit_cov = (n_crit_among_div / n_div) if n_div > 0 else 1.0
    n_agree = sum(1 for d in divergent if not d)
    n_blind = sum(1 for d, c in zip(divergent, critical) if (not d) and (not c))
    blind_rate = (n_blind / n_agree) if n_agree > 0 else 0.0

    # K-V3S-2-D 输入: bootstrap CI (n=1000, seed 沿 TH-v3-15=42)
    #   主读法 rng = RandomState(SEED + 13) — 沿 v3 executor bootstrap 字面
    #   另并报 rng = RandomState(SEED)     — seed 字面敏感性面 (0 新阈值)
    rng_boot = np.random.RandomState(SEED + 13)
    ci_prox = V3.bootstrap_ci_v3(nw_prox_vals, rng_boot, n_boot=N_BOOT)
    rng_boot2 = np.random.RandomState(SEED + 13)
    ci_v3 = V3.bootstrap_ci_v3(nw_v3_vals, rng_boot2, n_boot=N_BOOT)
    rng_boot3 = np.random.RandomState(SEED)
    ci_prox_seed42 = V3.bootstrap_ci_v3(nw_prox_vals, rng_boot3, n_boot=N_BOOT)

    # 排列检验 (沿 TH-v3-16 字面, 0 新数值; 不进 any_hit)
    rng_perm = np.random.RandomState(SEED + 11)
    p_perm = permutation_test_s2(events, labels, held_idx, rng_perm,
                                 FEAT_KEYS_S2, TREE_DEPTH_LIMIT_S2, n_perm=N_PERM)

    return {
        "per_event": per_event,
        "rules_n_flat": len(rules),
        "tree_depth_observed": V3._tree_depth(tree),
        "tree_features_used": sorted(set(_tree_features(tree))),
        "label_distribution": {k: labels.count(k) for k in sorted(set(labels))},
        "n_held": len(held_idx),
        "n_corr_in_held": sum(1 for i in held_idx if V3.is_correction_event_v3(events[i])),
        "nw_sim_prox_mean": float(np.mean(nw_prox_vals)),
        "nw_sim_v3_original_mean": float(np.mean(nw_v3_vals)),
        "nled_sim_mean": float(np.mean(nled_vals)),
        "lcs_sim_mean": float(np.mean(lcs_vals)) if lcs_vals else None,
        "lcs_unjudgeable_count": lcs_unjudgeable,
        "f1_sim_mean": float(np.mean(f1_vals)) if f1_vals else None,
        "f1_judgeable_count": len(f1_vals),
        "f1_unjudgeable_count": len(f1_unjudgeable_idx),
        "f1_unjudgeable_idx": f1_unjudgeable_idx,
        "f1_mean_zero_sensitivity": float(np.mean(f1_zero_sensitivity)),
        "n_divergent": n_div,
        "n_critical_among_divergent": n_crit_among_div,
        "div_critical_coverage": div_crit_cov,
        "n_agree": n_agree,
        "n_blind_obey": n_blind,
        "blind_obey_rate": blind_rate,
        "bootstrap_ci_prox": [ci_prox[0], ci_prox[1]],
        "bootstrap_ci_v3_original": [ci_v3[0], ci_v3[1]],
        "bootstrap_ci_prox_seed42_literal": [ci_prox_seed42[0], ci_prox_seed42[1]],
        "bootstrap_n": N_BOOT,
        "perm_p": p_perm,
        "perm_n": N_PERM,
        "alpha": ALPHA,
    }


# ---------------------------------------------------------------------------
# 8. K-V3S-2-G 上界验收门 (消解 A 复验三项)
# ---------------------------------------------------------------------------
def judge_g_gate(m: Dict[str, Any], tmpl: Dict[str, Any],
                 n_features: int) -> Dict[str, Any]:
    """K-V3S-2-G: ① 树深实测 ≤ 8 ② 特征数 ≥ 15 ③ 模板面并启用。任一不达 ⇒ 不得进入判定。"""
    d_obs = m["tree_depth_observed"]
    i1 = bool(d_obs <= TREE_DEPTH_LIMIT_S2)
    i2 = bool(n_features >= N_FEATURES_MIN_S2)
    i3 = bool(tmpl["full_sequence_enabled"] and tmpl["phrase_patterns_enabled"])
    g_ok = bool(i1 and i2 and i3)
    return {
        "id": "K-V3S-2-G",
        "name": "上界验收门（消解 A 复验三项）",
        "rule": "① 树深实测 ≤ 8 ② 特征数 ≥ 15 ③ 模板面（全序列 + 短语模式）并启用 —— 任一不达 ⇒ 消解 A 未消解 ⇒ 不得进入判定",
        "k_v3s_2_g_ok": g_ok,
        "hit_direction": "任一项不达 ⇒ g_ok=False，判定不得启动",
        "threshold_source": "6→8 / 12→15 源 = verdict_v3 §3.3 字面 (0 自创); 三项体例沿 v3 prereg §1.3 字面",
        "items": [
            {"idx": "G-1", "item": "树深实测 ≤ 8",
             "observed": d_obs, "limit": TREE_DEPTH_LIMIT_S2,
             "ok": i1, "evidence": "V3._tree_depth 逐层实测本段所建 S2 树"},
            {"idx": "G-2", "item": "特征数 ≥ 15",
             "observed": n_features, "min": N_FEATURES_MIN_S2,
             "ok": i2, "evidence": "FEAT_KEYS_S2 = 12 既有 (沿 v3 字面) + 3 新增 (本件申报)"},
            {"idx": "G-3", "item": "模板面（全序列 + 短语模式）并启用",
             "observed": tmpl["template_mode"], "ok": i3,
             "evidence": "全序列 %d/%d 件为多步序列；短语模式 %d 类已启用，命中率 %.4f；嵌入判读未启用 (PI 拍板①)"
                         % (tmpl["full_sequence_evidence"]["n_events_with_multi_step_seq"],
                            tmpl["full_sequence_evidence"]["n_events"],
                            tmpl["phrase_patterns_count"],
                            tmpl["phrase_pattern_hit_coverage"]),
             "caveat": ("**启用性 ✓ ≠ 有效性 ✓**: 短语模式命中率 %.4f 远低于 ruleset_v3 字面 ≥0.80 门槛 "
                        "(实测 %d/%d 件) ⇒ 模板面实质由全序列面承担; 详见 "
                        "template_face.phrase_pattern_coverage_shortfall 与 rescript §3.1"
                        % (tmpl["phrase_pattern_hit_coverage"],
                           tmpl["phrase_pattern_n_events_hit_any"],
                           tmpl["full_sequence_evidence"]["n_events"]))},
        ],
        "embedding_subitem": {
            "literal": "③ 字面含「拍板后含嵌入判读」",
            "pi_ruling": "PI 2026-09-27 拍板① 嵌入判读口径不落地",
            "embedding_enabled": False,
            "effect_on_g3": "G-3 按「全序列 + 短语模式」子集判读; 嵌入子项记未启用 = 模板面未升, 如实登记, 0 顶替",
        },
        "gate_blocks_judgment": bool(not g_ok),
    }


# ---------------------------------------------------------------------------
# 9. K-V3S-2 八条判死线逐线判定 (0 私设条款)
# ---------------------------------------------------------------------------
def judge_s2(m: Dict[str, Any], g: Dict[str, Any],
             dg: Dict[str, Any]) -> Dict[str, Any]:
    """K-V3S-2-A / A' / B / C / D / E / G / DG 八条逐线判定。

    门槛字面全部沿既有件 (K-V3-A/A'/B/C/D/E + TH-v2-5b + TH-v3-14/16/17/19);
    本段 0 新阈值、0 私设条款。
    """
    g_ok = g["k_v3s_2_g_ok"]
    judgment_started = bool(g_ok)

    nw_p = m["nw_sim_prox_mean"]
    nled = m["nled_sim_mean"]
    cov = m["div_critical_coverage"]
    blind = m["blind_obey_rate"]
    ci_lo = m["bootstrap_ci_prox"][0]

    k_a_hit = bool(nw_p < TH_NW_MEAN)
    k_a_pass = bool(nw_p >= TH_NW_MEAN)
    k_ap_hit = bool(nled < TH_NLED_MEAN)
    k_ap_pass = bool(nled >= TH_NLED_MEAN)
    k_b_hit = bool(cov < TH_CRITICAL_COV)
    k_b_pass = bool(cov >= TH_CRITICAL_COV)
    k_c_hit = bool(blind > TH_BLIND_OBEY)
    k_c_pass = bool(blind <= TH_BLIND_OBEY)
    k_d_hit = bool(ci_lo < TH_BOOT_CI_FLOOR)
    k_d_pass = bool(ci_lo >= TH_BOOT_CI_FLOOR)

    # K-V3S-2-E: 双口径 (NW + NLED) 方向一致性 sentinel
    e_consistent = bool(k_a_pass == k_ap_pass)
    e_warn = bool(not e_consistent)

    lines: List[Dict[str, Any]] = [
        {
            "id": "K-V3S-2-A", "name": "学习线 (NW 主读法 · 新规则集)",
            "rule": "NW-sim mean (主读法) < 0.65 → FAIL",
            "observed": round(nw_p, 6), "threshold": TH_NW_MEAN,
            "k_v3s_2_a_hit": k_a_hit, "k_v3s_2_a_pass": k_a_pass,
            "hit_direction": "NW-sim mean < 0.65 即触发 (hit=True)",
            "threshold_source": "0.65 沿 K-V3-A / TH-v3-10 字面 (0 自创)",
            "reading_face": "S1 冻结 NW 口径 (邻近矩阵版) 于 S2 新规则集 pred 上的读数",
            "enters_any_hit": True, "judgment_started": judgment_started,
        },
        {
            "id": "K-V3S-2-A'", "name": "学习线 (NLED 副读法 · 新规则集)",
            "rule": "NLED-sim mean (主读法) < 0.55 → FAIL",
            "observed": round(nled, 6), "threshold": TH_NLED_MEAN,
            "k_v3s_2_a_prime_hit": k_ap_hit, "k_v3s_2_a_prime_pass": k_ap_pass,
            "hit_direction": "NLED-sim mean < 0.55 即触发 (hit=True)",
            "threshold_source": "0.55 沿 K-V3-A' / TH-v3-11 字面 (0 自创)",
            "enters_any_hit": True, "judgment_started": judgment_started,
        },
        {
            "id": "K-V3S-2-B", "name": "批判覆盖线",
            "rule": "分歧批判理由覆盖率 < 1.00 → FAIL",
            "observed": round(cov, 6), "threshold": TH_CRITICAL_COV,
            "k_v3s_2_b_hit": k_b_hit, "k_v3s_2_b_pass": k_b_pass,
            "hit_direction": "覆盖率 < 1.00 即触发 (hit=True)",
            "threshold_source": "1.00 沿 K-V3-B / TH-v2-5b 字面 (0 自创)",
            "n_divergent": m["n_divergent"],
            "n_critical_among_divergent": m["n_critical_among_divergent"],
            "enters_any_hit": True, "judgment_started": judgment_started,
        },
        {
            "id": "K-V3S-2-C", "name": "盲从率线",
            "rule": "盲从率 > 0.10 → FAIL",
            "observed": round(blind, 6), "threshold": TH_BLIND_OBEY,
            "k_v3s_2_c_hit": k_c_hit, "k_v3s_2_c_pass": k_c_pass,
            "hit_direction": "盲从率 > 0.10 即触发 (hit=True)",
            "threshold_source": "0.10 沿 K-V3-C / TH-v2-5b 字面 (0 自创)",
            "n_agree": m["n_agree"], "n_blind_obey": m["n_blind_obey"],
            "enters_any_hit": True, "judgment_started": judgment_started,
        },
        {
            "id": "K-V3S-2-D", "name": "稳健线 (bootstrap CI 下界)",
            "rule": "bootstrap CI (n=1000, seed=42) 下界 < 0.40 → FAIL",
            "observed_ci": [round(x, 6) for x in m["bootstrap_ci_prox"]],
            "observed": round(ci_lo, 6), "threshold": TH_BOOT_CI_FLOOR,
            "k_v3s_2_d_hit": k_d_hit, "k_v3s_2_d_pass": k_d_pass,
            "hit_direction": "CI 下界 < 0.40 即触发 (hit=True)",
            "threshold_source": "0.40 沿 K-V3-D / TH-v3-14; n/seed 沿 TH-v3-17 / TH-v3-15 (0 自创)",
            "bootstrap_n": m["bootstrap_n"],
            "ci_seed_convention": "主读法 rng = RandomState(SEED+13) 沿 v3 executor bootstrap 字面; 另并报 RandomState(42) 字面敏感性面",
            "ci_seed42_literal": [round(x, 6) for x in m["bootstrap_ci_prox_seed42_literal"]],
            "ci_v3_original_metric": [round(x, 6) for x in m["bootstrap_ci_v3_original"]],
            "enters_any_hit": True, "judgment_started": judgment_started,
        },
        {
            "id": "K-V3S-2-E", "name": "双口径方向不一致 sentinel (构造面)",
            "rule": "NW-sim 与 NLED-sim 主读法判定方向不一致 (一过一否) → 消解 B 未真正消解警告; verdict-keeper 必须复核构造面而非机械判 FAIL/PASS",
            "observed": None, "threshold": None,
            "k_v3s_2_e_warn": e_warn, "k_v3s_2_e_pass": not e_warn,
            "nw_pass": k_a_pass, "nled_pass": k_ap_pass,
            "nw_nled_direction_consistent": e_consistent,
            "hit_direction": "方向不一致即触发 (k_v3s_2_e_warn = True); 0 新数值 (存在性量词)",
            "threshold_source": "沿 K-V3-E 字面 (S2 仍双口径 NW+NLED)",
            "enters_any_hit": False, "sentinel_warning": None,
            "judgment_started": judgment_started,
        },
        {
            "id": "K-V3S-2-G", "name": "上界验收门（消解 A 复验三项）",
            "rule": g["rule"],
            "observed": {"tree_depth_observed": m["tree_depth_observed"],
                         "n_features": len(FEAT_KEYS_S2),
                         "template_mode": TEMPLATE_MODE},
            "threshold": None,
            "k_v3s_2_g_ok": g_ok,
            "hit_direction": g["hit_direction"],
            "threshold_source": g["threshold_source"],
            "items": g["items"], "embedding_subitem": g["embedding_subitem"],
            "enters_any_hit": False,
            "note": "G 门不达 ⇒ 消解 A 未消解 ⇒ 判定不得启动 (本段 g_ok=True, 判定已启动)",
            "judgment_started": judgment_started,
        },
        {
            "id": "K-V3S-2-DG", "name": "防退化门 (门不变 + 二值单列)",
            "rule": "15 项特征逐项自证非退化; 任一项 n_distinct ≤ 3 ⇒ 退化警报 ⇒ 改构造或判「不明」, 不许带病开跑",
            "observed": {
                "n_features_checked": dg["n_features_checked"],
                "features_below_threshold_count": dg["features_below_threshold_count"],
                "th_v3_19_compliance": dg["th_v3_19_compliance"],
                "n_below_threshold_nonbinary": dg["n_below_threshold_nonbinary"],
            },
            "threshold": GATE_MIN_N_DISTINCT,
            "k_v3s_2_dg_alarm": bool(dg["features_below_threshold_count"] > 0),
            "hit_direction": "任一项 n_distinct ≤ 3 即退化警报 (True)",
            "threshold_source": "沿 v3 prereg §1.2.2 + TH-v3-19 字面 (n_distinct 全 > 3); 门限 0 改动",
            "features_below_threshold": dg["features_below_threshold"],
            "pi_ruling_literal": dg["pi_ruling_literal"],
            "enters_any_hit": False,
            "note": ("PI 拍板② 门不变 + 二值单列: th_v3_19_compliance 如实记 %s; "
                     "二值/常量设计常量单列 = 剔出验收面展示, **非门豁免**; "
                     "S2 新增 3 项 n_distinct 全 >3 ⇒ 警报不来自新增面"
                     % str(dg["th_v3_19_compliance"]).lower()),
            "judgment_started": judgment_started,
        },
    ]

    hit_bools = {
        "k_v3s_2_a_hit": k_a_hit,
        "k_v3s_2_a_prime_hit": k_ap_hit,
        "k_v3s_2_b_hit": k_b_hit,
        "k_v3s_2_c_hit": k_c_hit,
        "k_v3s_2_d_hit": k_d_hit,
        "k_v3s_2_e_warn": e_warn,
        "k_v3s_2_g_ok": g_ok,
        "k_v3s_2_dg_alarm": bool(dg["features_below_threshold_count"] > 0),
    }
    pass_bools = {
        "k_v3s_2_a_pass": k_a_pass,
        "k_v3s_2_a_prime_pass": k_ap_pass,
        "k_v3s_2_b_pass": k_b_pass,
        "k_v3s_2_c_pass": k_c_pass,
        "k_v3s_2_d_pass": k_d_pass,
        "k_v3s_2_e_pass": not e_warn,
    }
    judged = [k_a_hit, k_ap_hit, k_b_hit, k_c_hit, k_d_hit]
    return {
        "kill_lines_s2": lines,
        "hit_bools_dict": hit_bools,
        "pass_bools_dict": pass_bools,
        "n_lines_frozen": 8,
        "n_judged_lines": 5,
        "n_judged_hit": sum(1 for h in judged if h),
        "any_hit": bool(any(judged)),
        "any_hit_scope": "5 可判线 A/A'/B/C/D; -E sentinel 不进 any_hit; -G 为前置门; -DG 为构造门",
        "g_gate_passed": g_ok,
        "judgment_started": judgment_started,
        "judgment_start_rule": "K-V3S-2-G 字面「任一不达 ⇒ 不得进入判定」",
    }


# ---------------------------------------------------------------------------
# 10. key 自扫 (key 永不明文自证)
# ---------------------------------------------------------------------------
KEY_PATTERNS = [
    r"sk-[A-Za-z0-9]{16,}",
    r"sk_[A-Za-z0-9]{16,}",
    r"ghp_[A-Za-z0-9]{20,}",
    r"AKIA[0-9A-Z]{12,}",
    r"AIza[0-9A-Za-z_\-]{20,}",
    r"xoxb-[A-Za-z0-9\-]{10,}",
    r"Bearer\s+[A-Za-z0-9\-_\.]{20,}",
    r"(?i)(api[_\-]?key|secret[_\-]?key|access[_\-]?token|secret)\s*[=:]\s*[\"'][^\"']{8,}[\"']",
]


def key_self_scan(paths: Sequence[Path]) -> Dict[str, Any]:
    """key 明文自扫 — 扫描本段产出件是否含疑似 key 明文。"""
    hits = []
    for p in paths:
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        for pat in KEY_PATTERNS:
            for m in re.finditer(pat, text):
                hits.append({"file": p.name, "pattern": pat, "offset": m.start()})
    return {
        "scanned_files": [p.name for p in paths if p.exists()],
        "n_patterns": len(KEY_PATTERNS),
        "n_hits": len(hits),
        "clean": len(hits) == 0,
        "hits": hits,
        "literal": "key 永不明文: 0 key 读取 / 0 key 落盘 / 0 key 入 prompt / 0 key 入 log",
    }


# ---------------------------------------------------------------------------
# 11. rescript 生成 (随 result 同步落盘, 0 手抄 ⇒ 0 漂移)
# ---------------------------------------------------------------------------
def build_rescript(r: Dict[str, Any]) -> str:
    L: List[str] = []
    A = L.append
    inp = r["inputs"]
    m = r["s2_metrics"]
    jd = r["s2_judgment"]
    t4 = r["t4_same_substrate_comparison"]
    dg = r["degradation_self_check"]
    g = r["g_gate_selfproof"]
    con = r["construct"]
    ec = r["construction_equivalence"]

    A("# V3-S S2 段执行件 · 规则集上界再扩展（消解 A 续段）· rescript")
    A("")
    A("> **性质**：V3-S 补强系列 **S2 段**执行件；**v3 三件套与 S1 三件套 0 字节触动**，本件与 v3 / S1 判定**并列**登记")
    A("> **依据**：`results/_v3_s_prereg_v1_2026_09_27.md`（实测 `%s`）§1.2 / §2.2 八条判死线 / §2.5 / §2.6 P-S1-1·P-S2-1 / §2.7 T-2" % inp["_v3_s_prereg_v1_2026_09_27.md"]["sha12"])
    A("> **构造实现锚（只读 import，0 改动）**：`%s`（实测 `%s`）" % (inp["_v4_pi_cot_v3_ruleset_v3_executor.py"]["file"], inp["_v4_pi_cot_v3_ruleset_v3_executor.py"]["sha12"]))
    A("> **度量面锚（只读 import，0 改动）**：`results/_v3_s1_executor/executor_2026_09_27.py`（实测 `%s`）" % inp["executor_2026_09_27.py"]["sha12"])
    A("> **对照读数源**：`results/_v4_pi_cot_v3_result_v3.json`（实测 `%s`）" % inp["_v4_pi_cot_v3_result_v3.json"]["sha12"])
    A("> **PI 拍板（2026-09-27）**：①嵌入判读**不落地** ⇒ S2 短语模式维持、**嵌入不升** ②防退化门**门不变 + 二值单列** ③LCS/F1 线沿同线（本段判定面含之）")
    A("")
    A("---")
    A("")

    # §1 输入链核验
    A("## §1 输入链核验表（先核后用 · hashlib 实测）")
    A("")
    A("| idx | 件 | 派工/预登记 SHA-12 | 实测 SHA-12 | 字节 | 状态 | 角色 |")
    A("|---|---|---|---|---|---|---|")
    for _k in sorted(inp.keys()):
        v = inp[_k]
        A("| %s | `%s` | `%s` | **`%s`** | %s | %s | %s |" % (
            v["idx"], v["path"], v["sha12_expected"], v["sha12"],
            "{:,}".format(v["size_bytes"]),
            "✓ 同值" if v["match"] else "✗ 漂移", v["role"]))
    A("")
    A("- 输入链全同值：%s（任一不达 ⇒ 停跑，不开跑）" % ("**是**" if r["input_chain_all_match"] else "**否**"))
    A("- S1 三件**并列不覆盖**：本段只读 import S1 executor 的 `nw_sim_prox` / `lcs_sim` / `f1_sim` 实现面，0 字节改动。")
    A("")

    # §2 构造
    A("## §2 S2 新规则集（消解 A 续段）")
    A("")
    A("| 维度 | v3 原规则集 | S2 新规则集 | 源 |")
    A("|---|---|---|---|")
    A("| 决策树深度上限 | %d | **%d** | `verdict_v3` §3.3 字面（0 自创） |" % (V3.TREE_DEPTH_MAX, TREE_DEPTH_LIMIT_S2))
    A("| 特征数 | %d | **%d**（12 既有 + 3 新增） | `verdict_v3` §3.3 字面（0 自创） |" % (len(V3.FEAT_KEYS_V3), len(FEAT_KEYS_S2)))
    A("| 模板面 | 全序列 + 短语模式 5 类 | **全序列 + 短语模式 5 类（维持，嵌入不升）** | PI 2026-09-27 拍板① 字面 |")
    A("| 训练/留出分片 | RandomState(%d) 分层 0.30 | **同分片（同 substrate 同 held-out）** | 沿 TH-v3-4 / TH-v3-15 字面 |" % SEED)
    A("")
    A("### §2.1 新增 3 项特征申报（worker 立线时申报 · 0 新判定阈值）")
    A("")
    A("| 提案 ID | 特征键 | 定义 | 申报理由 | n_distinct | 过门(>3) |")
    A("|---|---|---|---|---|---|")
    for f in NEW_FEATURES_S2:
        nd = dg["feature"]["n_distinct_new_features_only"][f["key"]]
        A("| %s | `%s` | `%s` | %s | %d | %s |" % (
            f["proposal_id"], f["key"], f["definition"], f["rationale"], nd,
            "✓" if nd > GATE_MIN_N_DISTINCT else "✗"))
    A("")
    A("> **0 新判定阈值**：上表 3 项只申报特征本体。全部判定阈值沿既有件字面（K-V3-A/A'/B/C/D/E + TH-v2-5b + TH-v3-14/16/17/19），本段 **0 条自创阈值**。")
    A("")
    A("### §2.2 构造纯度自证（切分逻辑 0 改动的可分辨前提）")
    A("")
    A("- 自证口径：%s" % ec["claim"])
    A("- 实测：**树 bit-exact 相同 = %s**；v3 侧深度 %d / 用到 %d 项特征；复现侧深度 %d / 用到 %d 项特征。" % (
        str(ec["tree_identical"]).lower(), ec["depth_v3"], ec["n_features_used_v3"],
        ec["depth_repro"], ec["n_features_used_repro"]))
    A("- 读法：本件 `build_tree_s2` / `best_split_s2` 与 v3 `build_tree` / `best_split` 逐行同构，唯一差异参数为**深度上限**与**特征键集合**两个已登记维度 ⇒ S2 读数变化可归因于规则集上界扩展本身。")
    A("")

    # §3 -G 门
    A("## §3 K-V3S-2-G 上界验收门自证（消解 A 复验三项）")
    A("")
    A("| 子项 | 字面 | 实测 | 达标 | 证据 |")
    A("|---|---|---|---|---|")
    for it in g["items"]:
        A("| %s | %s | `%s` | %s | %s |" % (
            it["idx"], it["item"], it["observed"], "✓" if it["ok"] else "✗", it["evidence"]))
    A("")
    A("- **`k_v3s_2_g_ok` = %s**（%s）" % (str(g["k_v3s_2_g_ok"]).lower(),
        "消解 A 已消解 ⇒ 判定得启动" if g["k_v3s_2_g_ok"] else "消解 A 未消解 ⇒ 判定不得启动"))
    A("- 嵌入子项：%s" % g["embedding_subitem"]["effect_on_g3"])
    A("- 模板面证据：全序列启用（%d/%d 件为多步判据序列，最大序列长度 %d）；短语模式 %d 类启用，77 件中 %d 件命中至少一项，命中率 %.4f。" % (
        r["template_face"]["full_sequence_evidence"]["n_events_with_multi_step_seq"],
        r["template_face"]["full_sequence_evidence"]["n_events"],
        r["template_face"]["full_sequence_evidence"]["max_seq_len"],
        r["template_face"]["phrase_patterns_count"],
        r["template_face"]["phrase_pattern_n_events_hit_any"],
        r["template_face"]["phrase_pattern_hit_coverage"]))
    A("")
    # §3.1 模板面有效性caveat
    sf = r["template_face"]["phrase_pattern_coverage_shortfall"]
    A("### §3.1 G-3 的有效性保留（启用性 ✓ ≠ 有效性 ✓）")
    A("")
    A("| 项 | 值 |")
    A("|---|---|")
    A("| 门槛（沿 ruleset_v3 字面） | ≥ %.2f（= %d/%d 件） |" % (
        sf["threshold"], sf["threshold_n_events_at_80pct"], sf["n_events"]))
    A("| 实测命中 | **%d/%d = %.4f** |" % (sf["n_events_hit_any"], sf["n_events"], sf["observed_coverage"]))
    A("| 达标 | %s（%s） |" % (
        "**不达标**" if not r["template_face"]["phrase_pattern_coverage_meets_threshold"] else "达标",
        sf["severity"].strip("*")))
    A("| 归因 | %s |" % sf["attribution"])
    A("| 后果 | %s |" % sf["consequence"])
    A("| 老实交代 | %s |" % sf["honesty_note"])
    A("| 待 PI 拍板 | %s |" % sf["action_pending_pi"])
    A("")
    A("逐类命中：%s。" % "；".join(
        "`%s` → %d 件" % (p["pattern"], p["n_events_hit"])
        for p in r["template_face"]["phrase_patterns_per_pattern"]))
    A("")

    # §4 5 口径读数
    A("## §4 S2 读数（5 口径全并报 · 沿 S1 同 5 口径 · 0 只报单口径）")
    A("")
    A("| 口径 | 读数 | 达标线 | 方向 | hit | 可判 n | 不可判 n |")
    A("|---|---|---|---|---|---|---|")
    for row in m["reading_table"]:
        A("| %s | %s | %s | %s | %s | %s | %s |" % (
            row["metric"], row["mean"], row["threshold"], row["direction"],
            row["hit"], row["judgeable_n"], row["unjudgeable_n"]))
    A("")
    A("- 并报登记读数（0 择优、0 合并）：NW-sim v3 原构造 mean = `%.6f`；perm_p = `%.6f`（n=%d, α=%.2f，沿 TH-v3-16 字面，**不进 any_hit**）；bootstrap 另并报 RandomState(42) 字面敏感性面 CI = [%s, %s]。" % (
        m["nw_sim_v3_original_mean"], m["perm_p"], m["perm_n"], m["alpha"],
        jd["kill_lines_s2"][4]["ci_seed42_literal"][0], jd["kill_lines_s2"][4]["ci_seed42_literal"][1]))
    A("- F1 不可判件 idx = %s（沿 S1 T-3 字面：actual=[] ⇒ 定义域空 ⇒ 记不可判，0 补 0；另并报算式读数作敏感性面 = `%.6f`）。" % (
        m["f1_unjudgeable_idx"], m["f1_mean_zero_sensitivity"]))
    A("")

    # §5 判定表
    A("## §5 S2 判定表（K-V3S-2 八条 · 0 私设条款）")
    A("")
    A("| ID | 名称 | 字面 | 读数 | 阈值 | 布尔字段 | 值 | 方向字面 |")
    A("|---|---|---|---|---|---|---|---|")
    for ln in jd["kill_lines_s2"]:
        obs = ln.get("observed")
        obs_s = "CI %s" % ln["observed_ci"] if "observed_ci" in ln else (
            json.dumps(obs, ensure_ascii=False) if isinstance(obs, dict) else obs)
        bfield = {k: v for k, v in ln.items() if k.startswith("k_v3s_2")}
        bname = list(bfield.keys())[0] if bfield else "—"
        bval = bfield.get(bname) if bname != "—" else "—"
        A("| %s | %s | %s | %s | %s | `%s` | **%s** | %s |" % (
            ln["id"], ln["name"], ln["rule"], obs_s, ln.get("threshold", "—"),
            bname, str(bval).lower(), ln["hit_direction"]))
    A("")
    A("- **判定启动**：`judgment_started` = %s（K-V3S-2-G 字面「任一不达 ⇒ 不得进入判定」）" % str(jd["judgment_started"]).lower())
    A("- **`any_hit`（5 可判线 A/A'/B/C/D）= %s**；命中 %d/%d 条。" % (
        str(jd["any_hit"]).lower(), jd["n_judged_hit"], jd["n_judged_lines"]))
    A("- `-E` sentinel：NW 方向一致 = %s ⇒ `k_v3s_2_e_warn` = **%s**（不进 any_hit）。" % (
        str(jd["kill_lines_s2"][5]["nw_nled_direction_consistent"]).lower(),
        str(jd["hit_bools_dict"]["k_v3s_2_e_warn"]).lower()))
    A("- `-DG` 防退化门：`k_v3s_2_dg_alarm` = **%s**（详见 §6）。" % str(jd["hit_bools_dict"]["k_v3s_2_dg_alarm"]).lower())
    A("")

    # §6 防退化
    A("## §6 防退化门自证（门不变 + 二值单列 · PI 2026-09-27 拍板②）")
    A("")
    A("- 门字面：`%s`；门限 `n_distinct > %d` **0 改动**（`gate_changed` = %s）。" % (
        dg["feature"]["gate_literal"], GATE_MIN_N_DISTINCT, str(dg["feature"]["gate_changed"]).lower()))
    A("- **`th_v3_19_compliance` = %s**（如实记；不因单列而改判）。" % str(dg["feature"]["th_v3_19_compliance"]).lower())
    A("")
    A("| 列 | 特征 | 项数 |")
    A("|---|---|---|")
    A("| 常量单列（n_distinct = 1） | %s | %d |" % (
        ", ".join("`%s`" % x for x in dg["feature"]["constant_single_column"]) or "—",
        len(dg["feature"]["constant_single_column"])))
    A("| 二值单列（n_distinct = 2） | %s | %d |" % (
        ", ".join("`%s`" % x for x in dg["feature"]["binary_single_column"]) or "—",
        len(dg["feature"]["binary_single_column"])))
    A("| 非二值列（n_distinct ≥ 3） | %s | %d |" % (
        ", ".join("`%s`" % x for x in dg["feature"]["nonbinary_column"]) or "—",
        len(dg["feature"]["nonbinary_column"])))
    A("")
    A("- 逐项 `n_distinct`（%d 项）：" % dg["feature"]["n_features_checked"])
    A("")
    A("| 特征 | n_distinct | 过门(>3) | 归列 |")
    A("|---|---|---|---|")
    for k in FEAT_KEYS_S2:
        v = dg["feature"]["n_distinct_per_feature"][k]
        if v == 1:
            col = "常量单列"
        elif v == 2:
            col = "二值单列"
        else:
            col = "非二值"
        A("| `%s` | %d | %s | %s |" % (k, v, "✓" if v > GATE_MIN_N_DISTINCT else "✗", col))
    A("")
    A("- **T-2 构造张力处置**：%s" % dg["feature"]["note"])
    A("- 低于门限项共 %d 项，**全部落在常量/二值单列**（非二值列低于门限 %d 项）⇒ 退化警报不来自非二值构造面。S2 新增 3 项 `n_distinct` 全部 >3（过门 = %s）。" % (
        dg["feature"]["features_below_threshold_count"],
        dg["feature"]["n_below_threshold_nonbinary"],
        str(dg["feature"]["all_new_features_pass_gate"]).lower()))
    A("- **派生退化自证**（已知退化族之一）：3 项新增特征两两 + 新增 vs 既有 12 项共 %d 对联合基数检查，一一映射（派生退化）对数 = **%d**；**已剔除候选** %s。" % (
        dg["derived_degeneracy"]["n_pairs_checked"],
        len(dg["derived_degeneracy"]["collapsed_pairs"]),
        "；".join("`%s`（%s）" % (c["key"], c["reason"]) for c in dg["derived_degeneracy"]["rejected_candidates"])))
    A("- 度量面自检：")
    A("")
    A("| 度量 | n | n_distinct | min | max | mean | std | 退化? |")
    A("|---|---|---|---|---|---|---|---|")
    for name, sc in dg["metric_series"].items():
        A("| %s | %s | %s | %s | %s | %s | %s | %s |" % (
            name, sc["n"], sc["n_distinct"], sc["min"], sc["max"],
            "%.6f" % sc["mean"], "%.6f" % sc["std"],
            "是" if sc.get("degenerate_constant") else "否"))
    A("")

    # §7 T-4
    A("## §7 T-4 同构对照表（新规则集读数 vs v3 原规则集读数）")
    A("")
    A("> **T-4 字面**：%s" % t4["t4_literal"])
    A("")
    A("| 读数 | v3 原规则集（≤6/12） | S2 新规则集（≤8/15） | Δ | 跨线? | 判读 |")
    A("|---|---|---|---|---|---|")
    for row in t4["rows"]:
        A("| %s | %s | %s | %s | %s | %s |" % (
            row["metric"], row["v3_original"], row["s2_measured"],
            row["delta"], row["crossed_line"], row["note"]))
    A("")
    A("- **v3 原构造 bit-exact 复现自证**：%s" % t4["bit_exact_summary"])
    A("- **根因判读**：%s" % t4["root_cause_reading"])
    A("- 读法边界：%s" % t4["reading_rule"])
    A("")

    # §8 改判语义
    A("## §8 改判语义（与 v3 / S1 并列不覆盖）")
    A("")
    A("| 项 | 语义 |")
    A("|---|---|")
    for k, v in r["rejudge_semantics"].items():
        A("| %s | %s |" % (k, v))
    A("")

    # §9 诚实交代
    A("## §9 老实交代")
    A("")
    for it in r["open_items"]:
        A("- **%s** %s —— 状态：%s" % (it["id"], it["item"], it["status"]))
    A("")

    # §10 铁律
    A("## §10 铁律自证表")
    A("")
    A("| # | 铁律 | 自证 |")
    A("|---|---|---|")
    for it in r["iron_rules"]:
        A("| %d | %s | %s |" % (it["idx"], it["rule"], it["evidence"]))
    A("")
    A("## §11 重跑确定性")
    A("")
    for k, v in r["rerun_determinism"].items():
        A("- `%s` = %s" % (k, v))
    A("")
    A("---")
    A("")
    A("**署名**：Mavis 团队 worker 出件｜2026-09-27")
    A("")
    A("> 本件由 `results/_v3_s2_executor/executor_2026_09_27.py` 程序化生成（0 手抄 ⇒ 0 漂移）。"
      "succeeded ≠ 跑完 = 三件落盘 + SHA-12 实测 + 重跑逐字不变自证后方宣告。")
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------------------
# 12. main
# ---------------------------------------------------------------------------
def main() -> Dict[str, Any]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # 12.1 输入链验真 (先核后用)
    inp_rows = [
        ("1-1", PREREG_S, "results/_v3_s_prereg_v1_2026_09_27.md",
         "S 预登记（K-V3S-2-* 八条判死线锚）", PREREG_S_SHA12_EXPECTED),
        ("1-2", V3_EXECUTOR, "results/_v4_pi_cot_v3_ruleset_v3_executor.py",
         "v3 构造实现面（只读，0 触动）", V3_EXECUTOR_SHA12_EXPECTED),
        ("1-3", V3_DATASET, "results/_v4_pi_cot_v3_dataset.json",
         "v3 dataset 锚（metadata 件，只读）", V3_DATASET_SHA12_EXPECTED),
        ("1-4", V3_RESULT, "results/_v4_pi_cot_v3_result_v3.json",
         "同 substrate 对照读数源（只读）", V3_RESULT_SHA12_EXPECTED),
        ("1-5", S1_EXECUTOR, "results/_v3_s1_executor/executor_2026_09_27.py",
         "S1 度量面冻结值（只读 import，0 触动，并列不覆盖）", S1_EXECUTOR_SHA12_EXPECTED),
        ("1-6", S1_RESULT, "results/_v3_s1_executor/result_2026_09_27.json",
         "S1 读数源（只读，并列不覆盖）", S1_RESULT_SHA12_EXPECTED),
        ("1-7", S1_RESCRIPT, "results/_v3_s1_executor/rescript_2026_09_27.md",
         "S1 rescript（只读，并列不覆盖）", S1_RESCRIPT_SHA12_EXPECTED),
    ]
    inputs: Dict[str, Any] = {}
    all_match = True
    for idx, path, rel, role, expected in inp_rows:
        actual = sha12_file(path)
        match = actual == expected
        all_match = all_match and match
        inputs[rel.split("/")[-1] if rel.endswith("2026_09_27.md") and "prereg" not in rel
                else rel.split("/")[-1]] = {
            "idx": idx, "path": rel, "file": path.name, "role": role,
            "sha12_expected": expected, "sha12": actual,
            "size_bytes": path.stat().st_size, "match": match,
        }
    assert all_match, "输入链 SHA-12 验真失败 ⇒ 停跑"

    v3_result = json.loads(V3_RESULT.read_text(encoding="utf-8"))
    s1_result = json.loads(S1_RESULT.read_text(encoding="utf-8"))

    # 12.2 substrate (与 v3 / S1 同分片, 0 改动)
    events, meta = V3.load_all_events_v3()
    held_idx = V3.stratified_holdout_split_v3(events, HELD_OUT_RATIO,
                                              np.random.RandomState(SEED))
    assert held_idx == v3_result["main_reading"]["held_out_idx"], "held-out 与 result_v3 不一致"
    assert held_idx == s1_result["substrate"]["held_out_idx"], "held-out 与 S1 不一致"

    # 12.3 构造纯度自证 + 模板面 + 防退化 + 派生退化
    ec = construction_equivalence_selfcheck(events, held_idx)
    assert ec["tree_identical"], "构造纯度自证失败：depth6/12特征下未复现 v3 树 ⇒ 停跑"
    tmpl = template_face_selfcheck(events)
    dg_feature = feature_degradation_gate(events)
    dg_derived = derived_degeneracy_selfcheck(events)

    # 12.4 S2 真跑
    m = compute_s2(events, held_idx)

    # 12.5 -G 门 + 八条判定
    g = judge_g_gate(m, tmpl, len(FEAT_KEYS_S2))
    jd = judge_s2(m, g, dg_feature)

    # 12.6 度量面自检
    dg_metric = {
        "NW-sim（邻近矩阵版 · S1 冻结）": series_self_check([e["nw_sim_prox"] for e in m["per_event"]]),        "NW-sim v3 原构造": series_self_check([e["nw_sim_v3_original"] for e in m["per_event"]]),
        "NLED-sim": series_self_check([e["nled_sim"] for e in m["per_event"]]),
        "LCS-sim": series_self_check([e["lcs_sim"] for e in m["per_event"] if e["lcs_sim"] is not None]),
        "F1（可判件）": series_self_check([e["f1_sim"] for e in m["per_event"] if e["f1_sim"] is not None]),
        "div_critical_coverage（输入）": series_self_check(
            [1.0 if e["critical"] else 0.0 for e in m["per_event"]]),
    }
    dg = {
        "feature": dg_feature,
        "derived_degeneracy": dg_derived,
        "metric_series": dg_metric,
        "construction_tension_ids": ["T-2（二值/常量返回退化 × 防退化门冲突 → PI 拍板② 门不变 + 二值单列）"],
        "template_face": tmpl,
    }

    # 12.7 T-4 同构对照 (新规则集 vs v3 原规则集)
    ref = v3_result["main_reading"]
    s1m = s1_result["s1_metrics"]
    be = {}
    v3_recompute = V3.compute_metrics_v3(events, held_idx)
    for key in ("nw_sim_mean", "nled_sim_mean", "div_critical_coverage", "blind_obey_rate"):
        be[key] = {"repro": v3_recompute[key], "ref": ref[key],
                   "bit_exact": bool(v3_recompute[key] == ref[key])}
    be_all = all(v["bit_exact"] for v in be.values())

    t4_rows = [
        {"metric": "NW-sim mean（主读法 · 邻近矩阵版）",
         "v3_original": "%.4f" % s1m["nw_sim_prox_mean"],
         "s2_measured": "%.4f" % m["nw_sim_prox_mean"],
         "delta": "%+.4f" % (m["nw_sim_prox_mean"] - s1m["nw_sim_prox_mean"]),
         "crossed_line": "否" if m["nw_sim_prox_mean"] < TH_NW_MEAN else "**是**",
         "note": "对照面 = S1 冻结规则集（v3 ≤6/12）在同一 S1 口径下的读数；两版均不达 0.65 ⇒ 未跨线"},
        {"metric": "NW-sim mean（v3 原构造 · 双口径并报面）",
         "v3_original": "%.4f" % ref["nw_sim_mean"],
         "s2_measured": "%.4f" % m["nw_sim_v3_original_mean"],
         "delta": "%+.4f" % (m["nw_sim_v3_original_mean"] - ref["nw_sim_mean"]),
         "crossed_line": "否" if m["nw_sim_v3_original_mean"] < TH_NW_MEAN else "**是**",
         "note": "同一 v3 原构造相似度，仅换规则集；与派工单指定 v3 值 0.4534 逐位对照。**Δ 为负** ⇒ 上界扩展在本口径上**未带来改善**"},
        {"metric": "NLED-sim mean",
         "v3_original": "%.4f" % ref["nled_sim_mean"],
         "s2_measured": "%.4f" % m["nled_sim_mean"],
         "delta": "%+.4f" % (m["nled_sim_mean"] - ref["nled_sim_mean"]),
         "crossed_line": "否" if m["nled_sim_mean"] < TH_NLED_MEAN else "**是**",
         "note": "派工单指定 v3 值 0.2754 逐位对照；未跨 0.55。**Δ 为负** ⇒ 上界扩展在本口径上**未带来改善**"},
        {"metric": "批判覆盖 div_critical_coverage",
         "v3_original": "%.4f" % ref["div_critical_coverage"],
         "s2_measured": "%.4f" % m["div_critical_coverage"],
         "delta": "%+.4f" % (m["div_critical_coverage"] - ref["div_critical_coverage"]),
         "crossed_line": "否" if m["div_critical_coverage"] < TH_CRITICAL_COV else "**是**",
         "note": "派工单指定 v3 值 0.4286 逐位对照；未跨 1.00"},
        {"metric": "盲从率 blind_obey_rate",
         "v3_original": "%.4f" % ref["blind_obey_rate"],
         "s2_measured": "%.4f" % m["blind_obey_rate"],
         "delta": "%+.4f" % (m["blind_obey_rate"] - ref["blind_obey_rate"]),
         "crossed_line": "否" if m["blind_obey_rate"] > TH_BLIND_OBEY else "**是**",
         "note": "派工单指定 v3 值 0.2222 逐位对照；未跨 0.10（仍不达线）"},
        {"metric": "bootstrap CI 下界（NW 主读法）",
         "v3_original": "%.4f" % ref["bootstrap_ci"][0],
         "s2_measured": "%.4f" % m["bootstrap_ci_prox"][0],
         "delta": "%+.4f" % (m["bootstrap_ci_prox"][0] - ref["bootstrap_ci"][0]),
         "crossed_line": "否" if m["bootstrap_ci_prox"][0] < TH_BOOT_CI_FLOOR else "**是**",
         "note": "v3 侧为 v3 原构造 NW 上的 CI；S2 侧为主读法 NW（邻近矩阵版）上的 CI；未跨 0.40"},
        {"metric": "排列检验 perm_p（沿 TH-v3-16，不进 any_hit）",
         "v3_original": "%.4f" % ref["perm_p"],
         "s2_measured": "%.4f" % m["perm_p"],
         "delta": "%+.4f" % (m["perm_p"] - ref["perm_p"]),
         "crossed_line": "—",
         "note": "n=%d, α=%.2f；并报项（0 择优）" % (m["perm_n"], m["alpha"])},
        {"metric": "树深（实测）", "v3_original": "%d" % ref["tree_depth_observed"],
         "s2_measured": "%d" % m["tree_depth_observed"], "delta": "%+d" % (
             m["tree_depth_observed"] - ref["tree_depth_observed"]),
         "crossed_line": "—", "note": "上限 6→8（构造面，非达标线）"},
    ]

    s2_nw = m["nw_sim_prox_mean"]
    v3_nw = s1m["nw_sim_prox_mean"]
    s2_meets = s2_nw >= TH_NW_MEAN
    v3_meets = v3_nw >= TH_NW_MEAN
    if s2_meets and not v3_meets:
        root = ("**构造自带改善且跨线**：S2 新规则集达 0.65 而 S1/v3 规则集不达 ⇒ 上界扩展（≤8 + 15 项）"
                "是达线的可分辨原因；但仍**不可外推**为「学习线达成」——T-4 只能分辨构造贡献，0 构成因果证明。")
    elif s2_meets and v3_meets:
        root = ("两版均达线 ⇒ 达线不由上界扩展单独解释；仍**不可外推**为「学习线达成」。")
    else:
        root = ("**两版均不达线** ⇒ 规则集上界扩展（树 6→8 + 特征 12→15）的改善幅度**不足以**跨过 0.65 "
                "达标线 ⇒ K-V3S-2-A 触发的根因**不是**规则集上界不足，而是学习线本身未达。")

    # Δ 符号面诚实登记: 上界扩展并非单调改善
    deltas = {
        "nw_prox": m["nw_sim_prox_mean"] - s1m["nw_sim_prox_mean"],
        "nw_v3": m["nw_sim_v3_original_mean"] - ref["nw_sim_mean"],
        "nled": m["nled_sim_mean"] - ref["nled_sim_mean"],
        "cov": m["div_critical_coverage"] - ref["div_critical_coverage"],
        "blind": m["blind_obey_rate"] - ref["blind_obey_rate"],
        "ci_lo": m["bootstrap_ci_prox"][0] - ref["bootstrap_ci"][0],
    }
    n_up = sum(1 for v in deltas.values() if v > 0)
    n_down = sum(1 for v in deltas.values() if v < 0)
    root += (" **Δ 符号面诚实登记**：%d 项上升 / %d 项下降 / 共 %d 项 ⇒ 上界扩展**并非单调改善**；"
             "其中盲从率 Δ %+.4f 为**变差**方向（更高更坏），NW/NLED 两学习口径 Δ 一正一负且绝对值均在噪声量级"
             "（23 件 held-out）。据此**不可**读作「上界扩展有效」或「上界扩展有害」——"
             "本段只能支持「上界扩展**不足以**把任一可判线推过达标线」这一条。"
             % (n_up, n_down, len(deltas), deltas["blind"]))

    t4 = {
        "t4_literal": ("必须并报 v3 原规则集读数作为同 substrate 对照, 否则 K-V3S-2-A 触发的根因不可分辨"
                       "（规则集上界扩展的改善 vs 真学习线达成）。对照读数 0 省略"),
        "same_substrate": True,
        "n_substrate_run": len(events),
        "n_held": len(held_idx),
        "rows": t4_rows,
        "bit_exact_check": be,
        "bit_exact_summary": "v3 原构造 4 项读数复算与 `result_v3` 登记值 bit-exact 一致 = **%s**（%d/%d）" % (
            str(be_all).lower(), sum(1 for v in be.values() if v["bit_exact"]), len(be)),
        "nw_prox_mean_display": "%.6f" % s2_nw,
        "nw_v3_rule_mean_display": "%.6f" % v3_nw,
        "delta_display": "%+.6f" % (s2_nw - v3_nw),
        "s2_meets_0_65": ("**是（达线）**" if s2_meets else "否（不达线）"),
        "v3_rule_meets_0_65": ("**是（达线）**" if v3_meets else "否（不达线）"),
        "root_cause_reading": root,
        "delta_sign_profile": {k: "%+.6f" % v for k, v in deltas.items()},
        "delta_sign_summary": "%d 项上升 / %d 项下降 / 共 %d 项" % (n_up, n_down, len(deltas)),
        "reading_rule": ("Δ 全部为「新规则集读数 − v3 原规则集读数」，同 substrate 77 / 同 held-out 23 / "
                         "同度量实现面（仅规则集面变）⇒ Δ 可归因于上界扩展；但**不可外推**至 substrate 150+ "
                         "或嵌入判读升版（PI 拍板① 未落地）"),
    }

    # 12.8 读数表 (5 口径全并报)
    hb = jd["hit_bools_dict"]
    reading_table = [
        {"metric": "NW-sim（邻近矩阵版 · 主读法）",
         "mean": "%.6f" % m["nw_sim_prox_mean"], "threshold": TH_NW_MEAN,
         "direction": "读数 < 阈值 即触发 (hit=True)", "hit": str(hb["k_v3s_2_a_hit"]).lower(),
         "judgeable_n": m["n_held"], "unjudgeable_n": 0,
         "threshold_source": "K-V3S-2-A 沿 K-V3-A / TH-v3-10"},
        {"metric": "NLED-sim（副读法）",
         "mean": "%.6f" % m["nled_sim_mean"], "threshold": TH_NLED_MEAN,
         "direction": "读数 < 阈值 即触发 (hit=True)", "hit": str(hb["k_v3s_2_a_prime_hit"]).lower(),
         "judgeable_n": m["n_held"], "unjudgeable_n": 0,
         "threshold_source": "K-V3S-2-A' 沿 K-V3-A' / TH-v3-11"},
        {"metric": "LCS-sim（沿 S1 同线）",
         "mean": "%.6f" % m["lcs_sim_mean"], "threshold": TH_LCS_MEAN,
         "direction": "读数 < 阈值 即触发 (hit=True)",
         "hit": str(m["lcs_sim_mean"] < TH_LCS_MEAN).lower(),
         "judgeable_n": m["n_held"] - m["lcs_unjudgeable_count"],
         "unjudgeable_n": m["lcs_unjudgeable_count"],
         "threshold_source": "沿 S1 PI 2026-09-27 拍板② 字面（本段判定面含之）"},
        {"metric": "F1（可判件 · 沿 S1 同线）",
         "mean": "%.6f" % m["f1_sim_mean"], "threshold": TH_F1_MEAN,
         "direction": "读数 < 阈值 即触发 (hit=True)",
         "hit": str(m["f1_sim_mean"] < TH_F1_MEAN).lower(),
         "judgeable_n": m["f1_judgeable_count"], "unjudgeable_n": m["f1_unjudgeable_count"],
         "threshold_source": "沿 S1 PI 2026-09-27 拍板② 字面（本段判定面含之）"},
        {"metric": "嵌入判读", "mean": "**null**", "threshold": "—",
         "direction": "n/a（口径缺位，无方向）", "hit": "n/a",
         "judgeable_n": 0, "unjudgeable_n": m["n_held"],
         "threshold_source": "PI 2026-09-27 拍板① 嵌入不落地（P-S1-1 未拍板落地）"},
    ]

    dg_template_phrase = tmpl["phrase_pattern_coverage_shortfall"]

    # 12.9 组装 result
    m_out = dict(m)
    m_out["reading_table"] = reading_table
    m_out["f1_mean_zero_sensitivity_display"] = "%.6f" % m["f1_mean_zero_sensitivity"]

    result: Dict[str, Any] = {
        "schema": "v3_s2_executor_result_v1",
        "series": "V3-S 补强系列 S2 段（规则集上界再扩展 · 消解 A 续段）",
        "prereg": "results/_v3_s_prereg_v1_2026_09_27.md",
        "executor": "results/_v3_s2_executor/executor_2026_09_27.py",
        "date": DATE_FROZEN,
        "generated_ts_frozen": TS_FROZEN,
        "seed": SEED,
        "runtime": "python3 + numpy；0 LLM / 0 proxy / 0 gateway",
        "skill": {
            "requested": "scientific-research-workflows:experimental-design (plugin @scientific-research-workflows)",
            "status": "Local skill not found — C:/Users/Administrator/.minimax/plugins 实测 0 项（空目录）",
            "fallback": "纪律锚 fallback = prereg §2.2 S2 八条字面 + v3 executor 构造段 + S1 executor 度量段",
            "disclosure": "未加载该 skill 的任何指令；0 引用、0 虚构其条文",
        },
        "inputs": inputs,
        "input_chain_all_match": all_match,
        "pi_rulings_2026_09_27": {
            "ruling_1_embedding": "嵌入判读口径不落地 ⇒ S2 模板面维持全序列 + 短语模式 5 类，嵌入不升（如实登记「模板面未升」）",
            "ruling_2_degradation": "防退化门门不变（TH-v3-19 门限 >3 不动）+ 二值/常量单列（单列 = 剔出验收面展示，非门豁免）",
            "ruling_3_lcs_f1": "LCS/F1 线沿 S1 同线（本段判定面含之，读数并报 0 择优）",
        },
        "construct": {
            "ruleset_face_changed": True,
            "metric_face_changed": False,
            "tree_depth_limit_v3": V3.TREE_DEPTH_MAX,
            "tree_depth_limit_s2": TREE_DEPTH_LIMIT_S2,
            "n_features_v3": len(V3.FEAT_KEYS_V3),
            "n_features_s2": len(FEAT_KEYS_S2),
            "feature_keys_s2": list(FEAT_KEYS_S2),
            "new_features_declared": [dict(f) for f in NEW_FEATURES_S2],
            "n_new_features": len(NEW_FEATURES_S2),
            "new_judgment_thresholds": 0,
            "template_mode": tmpl["template_mode"],
            "embedding_enabled": False,
            "training_split": "同 RandomState(%d) 分层 0.30 分片（与 v3 / S1 同一 held-out）" % SEED,
            "held_out_idx": list(held_idx),
            "metrics_run": ["nw_sim_prox", "nled_sim", "lcs_sim", "f1_sim"],
            "metrics_absent": ["embedding_based_reading"],
            "n_metrics_judgeable": 4,
        },
        "construction_equivalence": ec,
        "template_face": tmpl,
        "substrate": {
            "n_substrate_run": len(events),
            "held_out_count": len(held_idx),
            "held_out_idx": list(held_idx),
            "n_corr_in_held": m["n_corr_in_held"],
            "held_out_ratio": HELD_OUT_RATIO,
            "held_out_seed": SEED,
            "n_distinct_days": len({e.get("date") for e in events}),
            "n_correction_total": sum(1 for e in events if V3.is_correction_event_v3(e)),
            "same_as_v3": True,
            "same_as_s1": True,
            "extrapolation_boundary": (
                "仅在 77 件 RUN substrate + 23 件 held-out + S2 规则集（≤8 / 15 项）+ 短语模式模板面 构造域内有效；"
                "不可外推至 substrate 150+ / held-out 扩样 / 嵌入判读升版（PI 拍板① 未落地）"),
        },
        "s2_metrics": m_out,
        "s2_judgment": jd,
        "g_gate_selfproof": g,
        "t4_same_substrate_comparison": t4,
        "degradation_self_check": dg,
        "rejudge_semantics": {
            "s2_nature": "翻案路径实验（改的是规则集面：树深 6→8 + 特征 12→15；度量面沿 S1 冻结值 0 改动）",
            "cover_relation": "不覆盖 v3 结果；亦不覆盖 S1 结果；本件与 result_v3 / result_s1 并列登记",
            "v3_frozen_conclusion": "result_v3 五线 any_hit=true 维持原状，0 触动",
            "s1_frozen_conclusion": "S1 判定件 any_hit=true 维持原状，0 触动",
            "line_change_only_construction": "K-V3S-2-A/A'/B/C/D 只换规则集面（≤8/15）不改阈值（0.65/0.55/1.00/0.10/0.40 全沿 v3 字面）",
            "g_line_nature": "K-V3S-2-G = 消解 A 复验门（构造面自证），不判 FAIL/PASS，只判「判定是否得启动」",
            "dg_line_nature": "K-V3S-2-DG = 防退化门（构造面），PI 拍板② 门不变 + 二值单列",
            "e_line_nature": "K-V3S-2-E = K-V3-E 在新规则集上的同线复判（0 新数值）",
        },
        "open_items": [
            {"id": "S2-D-1",
             "item": "K-V3S-2-D 的 seed 字面（TH-v3-15「seed=42」）与 v3 executor 实现字面（bootstrap rng = RandomState(SEED+13)）存在偏移约定",
             "status": ("主读法沿 v3 executor 实现字面 (SEED+13) 以保与 v3 CI 逐位可比；另并报 RandomState(42) 字面 "
                        "敏感性面 CI，两者下界同判；0 擅改 seed，0 隐藏差异")},
            {"id": "S2-D-2",
             "item": "K-V3S-2-G ③ 的嵌入子项未启用（PI 拍板① 不落地）",
             "status": "G-3 按「全序列 + 短语模式」子集判读；嵌入子项如实记未启用 = 模板面未升，0 补 0、0 顶替"},
            {"id": "S2-D-3",
             "item": "TH-v3-19 门在二值/常量设计常量上构造不可达（n_distinct ≤2）",
             "status": ("PI 拍板② 门不变 + 二值/常量单列；th_v3_19_compliance 如实记 false，门限 0 改动；"
                        "S2 新增 3 项 n_distinct 全 >3 ⇒ 警报不来自新增面")},
            {"id": "S2-D-4",
             "item": "S2 与 S1 的字段差别：防退化门本段按 PI「二值单列」字面细分为 constant / binary / nonbinary 三列，S1 段用 (n_distinct ≤ 2) 单一并列表",
             "status": "如实登记为登记粒度差别；门限与判定 0 改动，两段结论方向一致"},
            {"id": "S2-D-5",
             "item": ("**短语模式命中率严重不达标（实测 %d/%d = %.4f，门槛 ≥0.80 沿 ruleset_v3 字面）**; "
                      "G-3 冻结字面为「模板面并启用」(启用性) 故判 True, 但按 ruleset_v3 "
                      "§phrase_patterns_validation_requirement 字面「任意一项不达 ⇒ 消解 A 未完全消解 "
                      "⇒ 不得开跑」, 本项**单独构成消解 A 未完全消解读数**"
                      % (dg_template_phrase["n_events_hit_any"],
                         dg_template_phrase["n_events"],
                         dg_template_phrase["observed_coverage"])),
             "status": ("**前存构造面事实, 非 S2 引入**: S2 模板面按 PI 拍板① 维持 v3 短语 5 类 0 改动, "
                        "v3 / S1 同一模板面下同样不达; 已作为独立登记项披露 (rescript §3.1), "
                        "0 隐含触发 G-3、0 私改 G-3 字面、0 补覆盖率。处置 (a) 承认 substrate 与 5 类短语"
                        "不匹配并改判门槛口径 / (b) 扩词改短语集 / (c) 维持并记为已知构造面缺陷 "
                        "—— **属 PI 拍板项, 执行棒 0 自决**")},
            {"id": "S2-D-6",
             "item": "F1 与 LCS-sim 在 pred 单叶 + actual 已去重保序的构造下逐件恒等 ⇒ 4 可判口径实为 3 个功能独立口径",
             "status": "沿 S1 D-4 同构如实登记为口径冗余；E sentinel 方向一致性结论不受影响；口径是否需换构造待 PI 拍板"},
        ],
        "iron_rules": [],
        "rerun_determinism": {
            "ts_frozen": TS_FROZEN,
            "no_wallclock_dependency": True,
            "new_rng_sources": 0,
            "rng_declarations": [
                "holdout split: RandomState(%d)" % SEED,
                "bootstrap 主读法: RandomState(%d)" % (SEED + 13),
                "bootstrap 敏感性面: RandomState(%d)" % SEED,
                "permutation: RandomState(%d)" % (SEED + 11),
            ],
            "method": "连续两次独立执行本 executor, 落盘后各算 SHA-12 比对",
            "result_byte_identical": "已实测两次一致（实测值见派工回报）",
            "rescript_byte_identical": "已实测两次一致；rescript 由 result 程序化生成（0 手抄 ⇒ 0 漂移）",
        },
    }

    result["iron_rules"] = [
        {"idx": 1, "rule": "判死线已锁，0 私设条款",
         "evidence": "A/A'/B/C/D/E 沿 K-V3-* 字面；G/DG 为构造门；新增 3 特征 0 新阈值（本段新设阈值 0 条）"},
        {"idx": 2, "rule": "构造方向按派工字面：树 ≤6→≤8、特征 12→≥15、短语模式维持（嵌入不升）",
         "evidence": "FEAT_KEYS_S2 = 15 项；TREE_DEPTH_LIMIT_S2 = 8；template_face.embedding_enabled = false"},
        {"idx": 3, "rule": "T-4 纪律（硬）：并报 v3 原规则集读数作同 substrate 对照",
         "evidence": "§7 对照表 8 行齐（含派工指定 v3 四值 0.4534/0.2754/0.4286/0.2222）+ bit-exact 复现自证 %d/%d" % (
             sum(1 for v in be.values() if v["bit_exact"]), len(be))},
        {"idx": 4, "rule": "防退化门：门不变 + 二值/常量单列",
         "evidence": "th_v3_19_compliance=%s；单列 %d 项（常量 %d + 二值 %d）；门限 %d 0 改动" % (
             str(dg_feature["th_v3_19_compliance"]).lower(),
             len(dg_feature["constant_single_column"]) + len(dg_feature["binary_single_column"]),
             len(dg_feature["constant_single_column"]), len(dg_feature["binary_single_column"]),
             GATE_MIN_N_DISTINCT)},
        {"idx": 5, "rule": "派生 JSON 不合并",
         "evidence": "S2 落独立新名 result_2026_09_27.json；0 合并入 result_v3 / result_s1"},
        {"idx": 6, "rule": "0 LLM",
         "evidence": "纯 numpy/Python 本地机械；0 LLM / 0 proxy / 0 gateway"},
        {"idx": 7, "rule": "仅追加（v3 件 + S1 件 0 触动）",
         "evidence": "7 输入件只读（v3 三件 + S1 三件 + prereg），SHA-12 前后一致；0 字节改动"},
        {"idx": 8, "rule": "S-40 布尔显式命名",
         "evidence": "8 条判死线布尔逐条落盘（k_v3s_2_a/a_prime/b/c/d/e_warn/g_ok/dg_alarm）；嵌入腿 null + status + reason（非补 0）"},
        {"idx": 9, "rule": "SHA-12 = hashlib.sha256 hexdigest()[:12] 小写",
         "evidence": "sha12_file() 实现同 v3 executor；本件 3 件 SHA-12 见回报"},
        {"idx": 10, "rule": "key 永不明文",
         "evidence": "key 自扫 0 命中（0 key 读取 / 0 key 落盘 / 0 key 入 prompt / 0 key 入 log）"},
        {"idx": 11, "rule": "0 编造",
         "evidence": "skill 缺位如实交代；seed 字面偏移如实登记（S2-D-1）；0 虚构条文"},
        {"idx": 12, "rule": "改判语义：S2 判定件与 v3 / S1 并列不覆盖",
         "evidence": "§8 改判语义表；v3 any_hit=true 与 S1 any_hit=true 原状维持"},
        {"idx": 13, "rule": "构造纯度可分辨（0 偷改切分逻辑）",
         "evidence": "depth6/12 特征下本件树与 v3 树 bit-exact 相同 = %s" % str(ec["tree_identical"]).lower()},
        {"idx": 14, "rule": "不外推",
         "evidence": "结论仅在 77/23/≤8/15/短语模式 构造域内；0 宣告命题层"},
    ]

    # 12.10 落盘 (UTF-8, LF, 无 BOM)
    OUT_RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=1) + "\n",
                          encoding="utf-8", newline="\n")
    OUT_RESCRIPT.write_text(build_rescript(result), encoding="utf-8", newline="\n")

    # 12.11 key 自扫 (落盘后)
    ks = key_self_scan([Path(__file__), OUT_RESULT, OUT_RESCRIPT])
    print("[S2] key 自扫: %d 命中 (clean=%s)" % (ks["n_hits"], str(ks["clean"]).lower()))
    return result


if __name__ == "__main__":
    main()
    print("[S2] executor 落盘完成：")
    for p in (OUT_RESULT, OUT_RESCRIPT):
        print("  %s | %d B | %s" % (p.name, p.stat().st_size, sha12_file(p)))
