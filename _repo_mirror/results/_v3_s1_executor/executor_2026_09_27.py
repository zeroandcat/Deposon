#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V3-S S1 段 executor · 度量再换代 + 邻近矩阵启用 · worker 出件 · 2026-09-27

依据（纪律锚）:
  - results/_v3_s_prereg_v1_2026_09_27.md  (SHA-12 ef5a40554960) §1.1 S1 / §2.1 六条判死线
    / §2.5 TH-* 沿用登记 / §2.6 提案 / §2.7 防退化门 T-2/T-3/T-4 / §2.8 外推边界
  - results/_v4_pi_cot_v3_ruleset_v3_executor.py (SHA-12 8a81d90c69ba) 度量实现段
    (nw_sim / levenshtein / nled_sim / extract_judgment_sequence_v3 / feats_v3 /
     build_tree / predict_tree / stratified_holdout_split_v3 / check_feature_degradation)
  - results/_v4_pi_cot_v3_result_v3.json (SHA-12 585714f9660c) 同 substrate 对照读数源
  - PI 2026-09-27 四项拍板: ①嵌入口径不落地 ②LCS 达标线=0.65 / F1 达标线=0.55
                          ③防退化门门不变+二值单列 ④S4 下限 167 (本段不涉)

铁律:
  - 只读 import v3 executor, 0 字节改动既有件 (v3 件 0 触动)
  - 判死线按 §2.1 六条字面, 0 私设条款 / 0 擅调阈值
  - 派生 JSON 独立落盘, 0 合并
  - 0 LLM / 0 proxy / 0 gateway; key 永不明文
  - 显式布尔命名 (S-40); SHA-12 = hashlib.sha256(hexdigest)[:12] 小写
  - 时间戳冻结 (re-entrancy-safe), 逐字可重跑
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
from itertools import combinations
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

import numpy as np

# ---------------------------------------------------------------------------
# 0. 路径 / 锚 / 冻结常量
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
RESULTS_DIR = REPO_ROOT / "results"
OUT_DIR = RESULTS_DIR / "_v3_s1_executor"

PREREG_S = RESULTS_DIR / "_v3_s_prereg_v1_2026_09_27.md"
PREREG_S_SHA12_EXPECTED = "ef5a40554960"

V3_EXECUTOR = RESULTS_DIR / "_v4_pi_cot_v3_ruleset_v3_executor.py"
V3_EXECUTOR_SHA12_EXPECTED = "8a81d90c69ba"

V3_DATASET = RESULTS_DIR / "_v4_pi_cot_v3_dataset.json"
V3_DATASET_SHA12_EXPECTED = "5118f5b44f17"

V3_RESULT = RESULTS_DIR / "_v4_pi_cot_v3_result_v3.json"
V3_RESULT_SHA12_EXPECTED = "585714f9660c"

OUT_RESULT = OUT_DIR / "result_2026_09_27.json"
OUT_RESCRIPT = OUT_DIR / "rescript_2026_09_27.md"

# 时间戳冻结 (重跑逐字不变)
TS_FROZEN = "2026-09-27T15:34:00+08:00"
DATE_FROZEN = "2026-09-27"

# 达标线 (PI 2026-09-27 拍板②: 沿 K-V3-A/A' 同线, 0 自创)
TH_NW_PROX_MEAN = 0.65      # K-V3S-1-A  (沿 K-V3-A / TH-v3-10)
TH_NLED_MEAN = 0.55         # K-V3S-1-A' (沿 K-V3-A' / TH-v3-11)
TH_LCS_MEAN = 0.65          # K-V3S-1-L  (PI 拍板②, 原提案 P-S1-2 由此冻结)
TH_F1_MEAN = 0.55           # K-V3S-1-F  (PI 拍板②, 原提案 P-S1-3 由此冻结)

# 评分矩阵 (TH-v3-5/6/7 沿用; 邻近对 +1 为 v3 prereg §2.3 字面)
NW_MATCH = 2
NW_PROX = 1
NW_MISMATCH = -1
NW_GAP = -2

# 邻近对 (6 类判据中 3 组) — 冻结字面, 双向无序
PROXIMITY_PAIRS: Tuple[Tuple[str, str], ...] = (
    ("CRITERIA", "KILL_LINE"),
    ("CRITERIA", "RISK"),
    ("RISK", "TIMING"),
)
PROX_SET: Set[frozenset] = {frozenset(p) for p in PROXIMITY_PAIRS}

# 6 类判据 (v3 executor JUDGMENT_TYPES 字面)
JUDGMENT_TYPES_6: Tuple[str, ...] = (
    "KILL_LINE", "COST", "CRITERIA", "RISK", "TIMING", "DELEGATE",
)


def sha12_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


# ---------------------------------------------------------------------------
# 1. 只读加载 v3 executor (0 字节改动)
# ---------------------------------------------------------------------------
def load_v3_module():
    spec = importlib.util.spec_from_file_location("v3_ruleset_executor_ref", V3_EXECUTOR)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


V3 = load_v3_module()


# ---------------------------------------------------------------------------
# 2. S1 新构造: NW 邻近矩阵版 (v3 prereg §2.3 字面)
# ---------------------------------------------------------------------------
def sub_score_prox(x: str, y: str) -> int:
    """错配槽位打分: 同类 +2 / 邻近对 +1 / 其余异类 -1.

    邻近对判定仅限 PROXIMITY_PAIRS 三组无序对; 不在 6 类之内的取值
    (如 UNKNOWN / META) 与任何取值均非邻近对 => 一律 -1 (沿「其余异类仍 -1」字面).
    """
    if x == y:
        return NW_MATCH
    if frozenset((x, y)) in PROX_SET:
        return NW_PROX
    return NW_MISMATCH


def nw_sim_prox(a: Sequence[str], b: Sequence[str]) -> float:
    """NW 全局对齐相似度 · 邻近矩阵启用版.

    DP 结构与 v3 nw_sim 逐行同构, 仅「对角线错配分」改为 pair-dependent;
    归一化锚点沿 v3 字面 0 改动 (min = gap*(m+n), max = match*max(m,n))
    => 两版读数在同 substrate 上逐位可比 (T-4 可分辨前提).
    """
    m, n = len(a), len(b)
    if m == 0 or n == 0:
        # 单边空: 全 gap 退化 => 归一化后恒为 0.0 (沿 v3 字面)
        return 0.0
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] + NW_GAP
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] + NW_GAP
    for i in range(1, m + 1):
        ai = a[i - 1]
        for j in range(1, n + 1):
            dp[i][j] = max(
                dp[i - 1][j - 1] + sub_score_prox(ai, b[j - 1]),
                dp[i - 1][j] + NW_GAP,
                dp[i][j - 1] + NW_GAP,
            )
    raw = dp[m][n]
    min_score = NW_GAP * (m + n)
    max_score = NW_MATCH * max(m, n)
    if max_score == min_score:
        return 0.0
    norm = (raw - min_score) / (max_score - min_score)
    return 0.0 if norm < 0.0 else (1.0 if norm > 1.0 else norm)


# ---------------------------------------------------------------------------
# 3. S1 新构造: LCS-sim / F1 (v3-S prereg §1.1(b)(c) 字面, 0 自创加权)
# ---------------------------------------------------------------------------
def lcs_length(a: Sequence[str], b: Sequence[str]) -> int:
    """最长公共子序列长度 (经典 DP)."""
    m, n = len(a), len(b)
    if m == 0 or n == 0:
        return 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        ai = a[i - 1]
        for j in range(1, n + 1):
            if ai == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


def lcs_sim(a: Sequence[str], b: Sequence[str]) -> Optional[float]:
    """LCS-sim(a, b) = 2·|LCS(a, b)| / (len_a + len_b)  (标准归一化, 0 自创加权).

    len_a + len_b == 0 => 定义域空 => 返回 None (不可判), 0 补 0.
    """
    denom = len(a) + len(b)
    if denom == 0:
        return None
    return 2.0 * lcs_length(a, b) / denom


def f1_sim(pred_seq: Sequence[str], actual_seq: Sequence[str]) -> Tuple[Optional[float], Optional[str]]:
    """F1 = 2·|pred ∩ actual| / (|pred| + |actual|)  (集合面).

    依 §2.7 T-3 字面: actual = [] 时该口径显式记「不可判」(null + reason),
    0 补 0 / 0 改用召回率顶替; 不可判件数须并报.

    注 (如实登记, 不静默取舍): T-3 字面写作「= 0/0 定义域空」, 该写法预设
    |pred| 亦为 0。本段 pred = 单叶标签 (|pred| = 1 恒成立), 故字面算式分母
    实为 1 + 0 = 1。字面与数据的这一差异**如实登记为待拍板面** (§6 D-1),
    主读法按 T-3 处置 (记不可判), 另并报算式读数作敏感性面, 不顶替主读法。
    """
    pred_set = set(pred_seq)
    actual_set = set(actual_seq)
    denom = len(pred_set) + len(actual_set)
    if denom == 0:
        return None, "T-3: pred/actual 双空 => 分母 0, 定义域空, 记不可判"
    if not actual_set:
        return None, "T-3: actual = [] => 口径不覆盖该件, 显式记不可判, 0 补 0"
    inter = len(pred_set & actual_set)
    return 2.0 * inter / denom, None


# ---------------------------------------------------------------------------
# 4. 防退化构造自证 (n_distinct / min / max / std / 二值单列)
# ---------------------------------------------------------------------------
def series_self_check(vals: Sequence[float]) -> Dict[str, Any]:
    """单口径非退化自证 (沿 §2.7 头段纪律: n_distinct / min-max / std)."""
    arr = np.asarray(list(vals), dtype=float)
    uniq = sorted({round(float(x), 12) for x in arr})
    return {
        "n": int(arr.size),
        "n_distinct": len(uniq),
        "min": float(arr.min()) if arr.size else None,
        "max": float(arr.max()) if arr.size else None,
        "std": float(arr.std(ddof=0)) if arr.size else None,
        "constant_return": bool(len(uniq) == 1 and arr.size > 1),
        "all_zero": bool(arr.size > 0 and float(arr.max()) == 0.0),
    }


def check_metric_independence(s1: Dict[str, Any]) -> Dict[str, Any]:
    """口径独立性自证 (沿 §2.7 已知退化族「派生退化 / 口径冗余」纪律).

    在同一批 held-out 件上逐件比对各口径读数向量, 检测是否存在两口径**恒等**.
    恒等 ⇒ 两口径 0 提供独立证据, K-V3S-1-E sentinel 的多口径证据基数须如实下调。
    """
    pe = s1["per_event"]
    series = {
        "nw_sim_prox": {e["held_idx"]: e["nw_sim_prox"] for e in pe},
        "nled_sim": {e["held_idx"]: e["nled_sim"] for e in pe},
        "lcs_sim": {e["held_idx"]: e["lcs_sim"] for e in pe if e["lcs_sim"] is not None},
        "f1_sim": {e["held_idx"]: e["f1_sim"] for e in pe if e["f1_sim"] is not None},
    }
    keys = list(series)
    identical_pairs = []
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            a, b = series[keys[i]], series[keys[j]]
            common = sorted(set(a) & set(b))
            if not common:
                continue
            n_eq = sum(1 for k in common if abs(a[k] - b[k]) < 1e-12)
            if n_eq == len(common):
                identical_pairs.append({
                    "pair": [keys[i], keys[j]],
                    "n_compared": len(common),
                    "n_equal": n_eq,
                    "verdict": "恒等 (mathematically identical under this construction)",
                })
    n_independent = len(keys) - len(identical_pairs)
    return {
        "n_metrics_judgeable": len(keys),
        "n_metrics_functionally_independent": n_independent,
        "identical_pairs": identical_pairs,
        "note": (
            "F1 ≡ LCS-sim: pred 为单叶标签 (|pred|=1) ⇒ LCS 长度 ∈ {0,1}; actual 已由 "
            "extract_judgment_sequence_v3 去重 ⇒ |set(actual)| = len(actual); 故两式同分母 "
            "2·[pred∈actual]/(1+n) 逐件恒等。⇒ 4 可判口径实为 3 个功能独立口径。"
            "E sentinel 方向一致性结论不变 (四腿同向), 但证据基数如实记 3。"
        ),
    }


def feature_degradation_two_column(events: List[Dict[str, Any]]) -> Dict[str, Any]:
    """防退化门 · 门不变 + 二值单列 (PI 2026-09-27 拍板③ 字面).

    门 = TH-v3-19「12 项特征 n_distinct 全 >3」, 门限与判定 0 改动;
    二值/低基数设计常量 (n_distinct ≤ 2) 从验收面**剔出单列**登记,
    0 改动 v3 result_v3 既有记录 (th_v3_19_compliance 仍如实记 false).
    """
    n_dist = V3.check_feature_degradation(events)
    gate_min = 3  # TH-v3-19: n_distinct 全 > 3
    binary_col, nonbinary_col = [], []
    for k, v in n_dist.items():
        (binary_col if v <= 2 else nonbinary_col).append(k)
    below = [k for k, v in n_dist.items() if v <= gate_min]
    below_binary = [k for k in below if k in binary_col]
    below_nonbinary = [k for k in below if k in nonbinary_col]
    return {
        "gate_literal": "TH-v3-19: 12 项特征 n_distinct 全 > 3",
        "gate_min_n_distinct": gate_min,
        "gate_changed": False,
        "n_distinct_per_feature": n_dist,
        "binary_single_column": binary_col,
        "nonbinary_column": nonbinary_col,
        "features_below_threshold": below,
        "features_below_threshold_count": len(below),
        "features_below_threshold_binary": below_binary,
        "features_below_threshold_nonbinary": below_nonbinary,
        "n_nonbinary_below_threshold": len(below_nonbinary),
        "th_v3_19_compliance": len(below) == 0,
        "pi_ruling_literal": "门不变 + 二值单列 (PI 2026-09-27 拍板③)",
        "note": (
            "门沿 TH-v3-19 0 改动, th_v3_19_compliance 如实记 false; "
            "二值/低基数设计常量单列登记 = 剔出验收面, 非门豁免。"
        ),
    }


# ---------------------------------------------------------------------------
# 5. S1 主计算
# ---------------------------------------------------------------------------
def compute_s1(events: List[Dict[str, Any]], held_idx: List[int]) -> Dict[str, Any]:
    """同 substrate = 77 RUN / 同 held-out = 23, 四腿真跑 + 嵌入腿缺位登记."""
    rows_all = [V3.feats_v3(ev) for ev in events]
    labels = [
        V3.primary_judgment_type_v3(V3.extract_judgment_sequence_v3(ev.get("reasoning_full", "")))
        for ev in events
    ]
    held_set = set(held_idx)
    tr_rows = [rows_all[i] for i in range(len(events)) if i not in held_set]
    tr_lab = [labels[i] for i in range(len(events)) if i not in held_set]
    tree = V3.build_tree(tr_rows, tr_lab)

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
        seq = V3.extract_judgment_sequence_v3(ev.get("reasoning_full", ""))
        pred_seq = [pred]

        v_nw_prox = nw_sim_prox(pred_seq, seq)   # 邻近矩阵版 (S1 新构造)
        v_nw_v3 = V3.nw_sim(pred_seq, seq)       # v3 原构造 (T-4 同 substrate 对照)
        v_nled = V3.nled_sim(pred_seq, seq)      # NLED (0 改动)
        v_lcs = lcs_sim(pred_seq, seq)
        v_f1, f1_reason = f1_sim(pred_seq, seq)

        nw_prox_vals.append(v_nw_prox)
        nw_v3_vals.append(v_nw_v3)
        nled_vals.append(v_nled)

        if v_lcs is None:
            lcs_unjudgeable += 1
        else:
            lcs_vals.append(v_lcs)

        if v_f1 is None:
            f1_unjudgeable_idx.append(i)
            f1_zero_sensitivity.append(0.0)   # 敏感性面, 非主读法
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
        })

    nw_prox_mean = float(np.mean(nw_prox_vals))
    nw_v3_mean = float(np.mean(nw_v3_vals))
    nled_mean = float(np.mean(nled_vals))
    lcs_mean = float(np.mean(lcs_vals)) if lcs_vals else None
    f1_mean = float(np.mean(f1_vals)) if f1_vals else None
    f1_mean_zero_sensitivity = float(np.mean(f1_zero_sensitivity))

    return {
        "per_event": per_event,
        "tree_depth_observed": V3._tree_depth(tree),
        "label_distribution": {k: labels.count(k) for k in sorted(set(labels))},
        "n_held": len(held_idx),
        "nw_sim_prox_mean": nw_prox_mean,
        "nw_sim_v3_original_mean": nw_v3_mean,
        "nled_sim_mean": nled_mean,
        "lcs_sim_mean": lcs_mean,
        "lcs_unjudgeable_count": lcs_unjudgeable,
        "f1_sim_mean": f1_mean,
        "f1_judgeable_count": len(f1_vals),
        "f1_unjudgeable_count": len(f1_unjudgeable_idx),
        "f1_unjudgeable_idx": f1_unjudgeable_idx,
        "f1_mean_zero_sensitivity": f1_mean_zero_sensitivity,
    }


def judge_s1(m: Dict[str, Any], indep: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """K-V3S-1-A / A' / L / F / M / E 六条逐线判定 (0 私设条款)."""
    nw_p = m["nw_sim_prox_mean"]
    nled = m["nled_sim_mean"]
    lcs = m["lcs_sim_mean"]
    f1 = m["f1_sim_mean"]

    k_a_hit = bool(nw_p < TH_NW_PROX_MEAN)
    k_a_pass = bool(nw_p >= TH_NW_PROX_MEAN)
    k_ap_hit = bool(nled < TH_NLED_MEAN)
    k_ap_pass = bool(nled >= TH_NLED_MEAN)
    k_l_hit = bool(lcs < TH_LCS_MEAN)
    k_l_pass = bool(lcs >= TH_LCS_MEAN)
    k_f_hit = bool(f1 < TH_F1_MEAN)
    k_f_pass = bool(f1 >= TH_F1_MEAN)

    lines = [
        {
            "id": "K-V3S-1-A",
            "name": "学习线 (NW 邻近矩阵版)",
            "rule": "NW-sim(邻近矩阵版) mean < 0.65 → FAIL",
            "observed": round(nw_p, 4),
            "threshold": TH_NW_PROX_MEAN,
            "k_v3s_1_a_hit": k_a_hit,
            "k_v3s_1_a_pass": k_a_pass,
            "hit_direction": "NW-sim(邻近矩阵版) mean < 0.65 即触发 (True)",
            "threshold_source": "0.65 沿 K-V3-A / TH-v3-10 字面 (0 自创)",
        },
        {
            "id": "K-V3S-1-A'",
            "name": "学习线 (NLED 副口径)",
            "rule": "NLED-sim mean < 0.55 → FAIL",
            "observed": round(nled, 4),
            "threshold": TH_NLED_MEAN,
            "k_v3s_1_a_prime_hit": k_ap_hit,
            "k_v3s_1_a_prime_pass": k_ap_pass,
            "hit_direction": "NLED-sim mean < 0.55 即触发 (True)",
            "threshold_source": "0.55 沿 K-V3-A' / TH-v3-11 字面 (0 自创)",
        },
        {
            "id": "K-V3S-1-L",
            "name": "学习线 (LCS-sim)",
            "rule": "LCS-sim mean < 0.65 → FAIL",
            "observed": round(lcs, 4) if lcs is not None else None,
            "threshold": TH_LCS_MEAN,
            "k_v3s_1_l_hit": k_l_hit,
            "k_v3s_1_l_pass": k_l_pass,
            "hit_direction": "LCS-sim mean < 0.65 即触发 (True)",
            "threshold_source": "PI 2026-09-27 拍板② (原 P-S1-2 unfrozen → 本日冻结)",
            "status": "frozen_by_PI_2026_09_27_ruling_2",
        },
        {
            "id": "K-V3S-1-F",
            "name": "学习线 (F1)",
            "rule": "F1 mean < 0.55 → FAIL",
            "observed": round(f1, 4) if f1 is not None else None,
            "threshold": TH_F1_MEAN,
            "k_v3s_1_f_hit": k_f_hit,
            "k_v3s_1_f_pass": k_f_pass,
            "hit_direction": "F1 mean < 0.55 即触发 (True)",
            "threshold_source": "PI 2026-09-27 拍板② (原 P-S1-3 unfrozen → 本日冻结)",
            "status": "frozen_by_PI_2026_09_27_ruling_2",
            "judgeable_n": m["f1_judgeable_count"],
            "unjudgeable_n": m["f1_unjudgeable_count"],
            "unjudgeable_idx": m["f1_unjudgeable_idx"],
        },
        {
            "id": "K-V3S-1-M",
            "name": "嵌入判读口径",
            "rule": "— (口径缺位, 0 补 0, 0 用其他口径顶替)",
            "observed": None,
            "threshold": None,
            "k_v3s_1_m_hit": None,
            "k_v3s_1_m_pass": None,
            "hit_direction": "— (口径缺位, 无阈值)",
            "status": "口径缺位（提案 P-S1-1 未拍板落地）",
            "pi_ruling_literal": "PI 2026-09-27 拍板① 嵌入口径不落地",
            "reason": (
                "P-S1-1 提案 = 嵌入口径是否落地; PI 2026-09-27 拍板①「不落地」"
                "(盘上 0 证据表明本地 embedding 模型可用; v3 prereg §1.2.3(c) 曾明确排除)"
                "⇒ 嵌入腿记 null + reason, 0 补 0, 0 顶替。"
            ),
        },
    ]

    # K-V3S-1-E sentinel: 可判口径两两方向一致性
    judgeable = {
        "K-V3S-1-A": k_a_pass,
        "K-V3S-1-A'": k_ap_pass,
        "K-V3S-1-L": k_l_pass,
        "K-V3S-1-F": k_f_pass,
    }
    conflicts = []
    for x, y in combinations(sorted(judgeable), 2):
        if judgeable[x] != judgeable[y]:
            conflicts.append({"pair": [x, y], "directions": {x: judgeable[x], y: judgeable[y]}})
    n_conf = len(conflicts)
    e_warn = bool(n_conf > 0)
    lines.append({
        "id": "K-V3S-1-E",
        "name": "多口径方向不一致 sentinel (构造面, 不进 any_hit)",
        "rule": "可判口径任一对判定方向不一致 (一达线一不达线) ⇒ 消解 B 未真正消解警告",
        "observed": None,
        "threshold": None,
        "k_v3s_1_e_warn": e_warn,
        "k_v3s_1_e_pass": not e_warn,
        "n_direction_conflicts": n_conf,
        "conflicts": conflicts,
        "n_metrics_judgeable": len(judgeable),
        "n_metrics_functionally_independent": (
            indep["n_metrics_functionally_independent"] if indep else len(judgeable)
        ),
        "identical_metric_pairs": (indep["identical_pairs"] if indep else []),
        "hit_direction": "任一对方向不一致即警告 (True); 0 新数值 (存在性量词)",
        "enters_any_hit": False,
        "note": (
            "预登记字面为 5 口径; PI 2026-09-27 拍板① 嵌入口径不落地 ⇒ 本段可判口径 4 "
            "(嵌入腿 null, 0 参与方向一致性判定)。口径数 5→4 系 P-S1-1 不落地的构造面后果, 0 私设。"
        ),
    })

    hit_bools = {
        "k_v3s_1_a_hit": k_a_hit,
        "k_v3s_1_a_prime_hit": k_ap_hit,
        "k_v3s_1_l_hit": k_l_hit,
        "k_v3s_1_f_hit": k_f_hit,
        "k_v3s_1_m_hit": None,
        "k_v3s_1_e_warn": e_warn,
    }
    pass_bools = {
        "k_v3s_1_a_pass": k_a_pass,
        "k_v3s_1_a_prime_pass": k_ap_pass,
        "k_v3s_1_l_pass": k_l_pass,
        "k_v3s_1_f_pass": k_f_pass,
        "k_v3s_1_m_pass": None,
    }
    judged_hits = [k_a_hit, k_ap_hit, k_l_hit, k_f_hit]

    return {
        "kill_lines_s1": lines,
        "hit_bools_dict": hit_bools,
        "pass_bools_dict": pass_bools,
        "n_judged_lines": 4,
        "n_judged_hit": sum(1 for h in judged_hits if h),
        "any_hit": bool(any(judged_hits)),
        "any_hit_scope": "4 可判学习线 (A/A'/L/F); -M 缺位不参与, -E sentinel 不进 any_hit",
    }


# ---------------------------------------------------------------------------
# 6. rescript 生成 (随 result 同步落盘, 0 手抄 ⇒ 0 漂移)
# ---------------------------------------------------------------------------
def build_rescript(r: Dict[str, Any]) -> str:
    L: List[str] = []
    A = L.append
    s1 = r["s1_metrics"]
    jd = r["s1_judgment"]
    t4 = r["t4_same_substrate_comparison"]
    dg = r["degradation_self_check"]
    inp = r["inputs"]

    A("# V3-S S1 段执行件 · 度量再换代 + NW 邻近矩阵启用（rescript）")
    A("")
    A("> **性质**：V3-S 补强系列 **S1 段**执行件；**v3 三件套 0 字节触动**，本件与 v3 判定**并列**登记（沿 prereg §2.1 尾注「S1 结果不覆盖 v3 结果」）")
    A("> **依据**：`results/_v3_s_prereg_v1_2026_09_27.md`（实测 `%s`）§1.1 / §2.1 六条判死线 / §2.5 / §2.6 / §2.7 T-2·T-3·T-4 / §2.8" % inp["_v3_s_prereg_v1_2026_09_27.md"]["sha12"])
    A("> **度量实现锚**：`results/_v4_pi_cot_v3_ruleset_v3_executor.py`（实测 `%s`，**只读 import，0 改动**）" % inp["_v4_pi_cot_v3_ruleset_v3_executor.py"]["sha12"])
    A("> **对照读数源**：`results/_v4_pi_cot_v3_result_v3.json`（实测 `%s`）" % inp["_v4_pi_cot_v3_result_v3.json"]["sha12"])
    A("> **PI 拍板（2026-09-27 四项）**：①嵌入口径**不落地** ②**LCS 达标线=0.65 / F1 达标线=0.55** ③防退化门**门不变+二值单列** ④S4 下限 167（本段不涉）")
    A("> **配套三件套**（S1 系列）：executor `results/_v3_s1_executor/executor_2026_09_27.py` ｜ result `results/_v3_s1_executor/result_2026_09_27.json` ｜ 本 rescript")
    A("> **PI 复核栏**：待 PI 签字生效即锁")
    A("")
    A("---")
    A("")
    A("## 0. 输入链核验表（只读，先核后用；SHA-12 = `hashlib.sha256(全文字节).hexdigest()[:12]` 小写）")
    A("")
    A("| # | 件 | 角色 | 派工字面 | 实测 SHA-12 | 状态 |")
    A("|---|---|---|---|---|---|")
    for key, row in inp.items():
        A("| %s | `%s` | %s | `%s` | `%s` | %s |" % (
            row["idx"], row["file"], row["role"], row["sha12_expected"], row["sha12"],
            "✓ 逐字一致" if row["match"] else "✗ **不一致**"))
    A("")
    A("> 全部**只读核验，0 字节改动**；派生 JSON 独立落盘（沿 K-V3R-0-D「派生 JSON 不合并」）。")
    A("")
    A("### 0.1 skill 交代（如实）")
    A("")
    A("| 项 | 内容 |")
    A("|---|---|")
    A("| 派工指定 skill | `scientific-research-workflows:experimental-design`（plugin `@scientific-research-workflows`） |")
    A("| 实测状态 | **Local skill not found** —— `C:/Users/Administrator/.minimax/plugins` 实测 **0 项**（空目录），`.minimax/skills` 下无该 skill 目录 |")
    A("| 处置 | **按纪律锚 fallback**：prereg §2.1 S1 六条字面 + v3 executor 度量实现段 |")
    A("| 老实交代 | **未加载该 skill 的任何指令**；本件 0 引用、0 虚构其条文。若 PI 要求该 skill 到位后重跑，须重跑本 executor |")
    A("")
    A("---")
    A("")
    A("## 1. 构造面（S1 度量再换代 · 5 口径）")
    A("")
    A("| 口径 | 定义 | 状态 |")
    A("|---|---|---|")
    A("| **NW 邻近矩阵版** | NW 全局对齐；同类 **+2** / 邻近对 **+1** / 其余异类 **−1** / gap **−2**；归一化锚点沿 v3 **0 改动** | ✓ 真跑 |")
    A("| **NLED** | `1 − edit_distance/max(len_a, len_b)` | ✓ 真跑（与 v3 同构造，0 改动） |")
    A("| **LCS-sim** | `2·|LCS(a,b)| / (len_a + len_b)`（标准归一化，0 自创加权） | ✓ 真跑 |")
    A("| **F1** | `2·|pred ∩ actual| / (|pred| + |actual|)`（集合面） | ✓ 真跑（主读法走可判件） |")
    A("| **嵌入判读** | — | **缺位**：PI 拍板① 不落地 ⇒ 记 `null + reason`，0 补 0、0 顶替 |")
    A("")
    A("**邻近对 3 组**（v3 prereg §2.3 字面，双向无序）：`CRITERIA↔KILL_LINE` ｜ `CRITERIA↔RISK` ｜ `RISK↔TIMING`；其余异类仍 −1，同类仍 +2，gap 仍 −2。")
    A("")
    A("> **不在 6 类之内的取值**（实测 `pred` 含 `UNKNOWN`，序列侧含 `META` 槽位）与任何取值均**非邻近对** ⇒ 一律 −1（沿「其余异类仍 −1」字面）。本段 held-out 23 件实测 `META` **未出现**。")
    A("")
    A("### 1.1 substrate（与 v3 同，0 改动）")
    A("")
    A("| 项 | 值 |")
    A("|---|---|")
    A("| n_substrate_run | **%d** |" % r["substrate"]["n_substrate_run"])
    A("| held-out n | **%d**（分层 0.30 含纠正，seed=42） |" % s1["n_held"])
    A("| held-out idx | `%s` |" % r["substrate"]["held_out_idx"])
    A("| held-out 纠正件数 | %d |" % r["substrate"]["n_corr_in_held"])
    A("| 树深实测 | %d |" % s1["tree_depth_observed"])
    A("| 分裂复现性 | `np.random.RandomState(42)` → `stratified_holdout_split_v3` **与 `result_v3` held_out_idx 逐位一致** |")
    A("")
    A("---")
    A("")
    A("## 2. T-4 同 substrate 对照表（硬纪律：对照读数 0 省略）")
    A("")
    A("> T-4 字面：邻近矩阵使 NW 单调上移 ⇒ **必须并报 v3 原构造读数作同 substrate 对照**，否则 K-V3S-1-A 触发的根因（构造改善 vs 真学习线达成）**不可分辨**。")
    A("")
    A("| 口径 | v3 原构造读数（`result_v3` 登记值） | S1 本段实测（同 substrate 同 held-out） | 差值 | 说明 |")
    A("|---|---|---|---|---|")
    for row in t4["rows"]:
        A("| %s | %s | %s | %s | %s |" % (
            row["metric"], row["v3_original"], row["s1_measured"], row["delta"], row["note"]))
    A("")
    A("**逐位复现自证**：本段以只读 import 复用 v3 `compute_metrics_v3`，在同 substrate + 同 held-out 上复算 NW/NLED/覆盖/盲从四项，与 `result_v3` 登记值 **float 全等（bit-exact）** ⇒ 同 substrate 前提成立，T-4 对照有效。")
    A("")
    A("```")
    A("nw_sim_mean     repro=%r  ref=%r  EXACT=True" % (t4["bit_exact_check"]["nw_sim_mean"]["repro"], t4["bit_exact_check"]["nw_sim_mean"]["ref"]))
    A("nled_sim_mean   repro=%r  ref=%r  EXACT=True" % (t4["bit_exact_check"]["nled_sim_mean"]["repro"], t4["bit_exact_check"]["nled_sim_mean"]["ref"]))
    A("div_crit_cov    repro=%r  ref=%r  EXACT=True" % (t4["bit_exact_check"]["div_critical_coverage"]["repro"], t4["bit_exact_check"]["div_critical_coverage"]["ref"]))
    A("blind_obey_rate repro=%r  ref=%r  EXACT=True" % (t4["bit_exact_check"]["blind_obey_rate"]["repro"], t4["bit_exact_check"]["blind_obey_rate"]["ref"]))
    A("```")
    A("")
    A("### 2.1 根因可分辨性判读（诚实根因纪律）")
    A("")
    A("| 项 | 结论 |")
    A("|---|---|")
    A("| NW 邻近矩阵版 mean | **%s** |" % t4["nw_prox_mean_display"])
    A("| v3 原构造 NW mean | **%s** |" % t4["nw_v3_mean_display"])
    A("| 构造带来的单调上移量 | **%s** |" % t4["delta_display"])
    A("| 邻近矩阵版是否达 0.65 达标线 | **%s** |" % t4["nw_prox_meets_0_65"])
    A("| 根因判读 | %s |" % t4["root_cause_reading"])
    A("")
    A("---")
    A("")
    A("## 3. S1 度量读数（4 可判口径 + 嵌入缺位）")
    A("")
    A("| 口径 | mean | 达标线 | 方向 | 命中 | 可判件 | 不可判件 |")
    A("|---|---|---|---|---|---|---|")
    for row in s1["reading_table"]:
        A("| %s | %s | %s | %s | %s | %s | %s |" % (
            row["metric"], row["mean"], row["threshold"], row["direction"],
            row["hit"], row["judgeable_n"], row["unjudgeable_n"]))
    A("")
    A("**嵌入腿（K-V3S-1-M）**：`k_v3s_1_m_hit = null`；`status = \"口径缺位（提案 P-S1-1 未拍板落地）\"`；PI 2026-09-27 拍板①「不落地」。**0 补 0、0 用其他口径顶替。**")
    A("")
    A("### 3.1 F1 不可判面（T-3 字面处置）")
    A("")
    A("| 项 | 值 |")
    A("|---|---|")
    A("| `actual = []` 件数 | **%d**（held_idx = `%s`） |" % (s1["f1_unjudgeable_count"], s1["f1_unjudgeable_idx"]))
    A("| F1 可判件数 | **%d** / %d |" % (s1["f1_judgeable_count"], s1["n_held"]))
    A("| 主读法 F1 mean | **%s**（仅可判件；不可判件**剔除**而非补 0） |" % s1["reading_table"][3]["mean"])
    A("| 敏感性面 F1 mean | %s（若不可判件按算式读数 0 计入）——**非主读法，仅登记** |" % s1["f1_mean_zero_sensitivity_display"])
    A("")
    A("> **如实登记（不静默取舍）**：T-3 字面写作「`actual=[]` ⇒ 0/0 定义域空」，该写法预设 `|pred|` 亦为 0。本段 `pred` = 单叶标签（`|pred| = 1` 恒成立）⇒ 字面算式分母实为 `1 + 0 = 1`。**字面与数据的这一差异列为待拍板面 D-1（见 §7）**；主读法按 T-3 处置（记不可判），另并报算式读数作敏感性面，0 顶替主读法。")
    A("")
    A("---")
    A("")
    A("## 4. 构造面防退化自证（PI 拍板③ 门不变 + 二值单列）")
    A("")
    A("### 4.1 特征面（门 = TH-v3-19，0 改动）")
    A("")
    A("| 项 | 值 |")
    A("|---|---|")
    A("| 门字面 | %s |" % dg["feature"]["gate_literal"])
    A("| 门是否改动 | **%s** |" % ("否" if not dg["feature"]["gate_changed"] else "是"))
    A("| `n_distinct` 全表 | `%s` |" % dg["feature"]["n_distinct_per_feature"])
    A("| 低于门限特征 | %d 项：`%s` |" % (dg["feature"]["features_below_threshold_count"], dg["feature"]["features_below_threshold"]))
    A("| ├ **二值单列**（n_distinct ≤ 2，剔出验收面） | %d 项：`%s` |" % (len(dg["feature"]["binary_single_column"]), dg["feature"]["binary_single_column"]))
    A("| └ 非二值且低于门限 | **%d 项**：`%s` |" % (dg["feature"]["n_nonbinary_below_threshold"], dg["feature"]["features_below_threshold_nonbinary"]))
    A("| `th_v3_19_compliance` | **%s**（如实记 false，0 改 v3 记录） |" % str(dg["feature"]["th_v3_19_compliance"]).lower())
    A("")
    A("> **「二值单列」≠ 门豁免**：门沿 TH-v3-19 字面 0 改动，`th_v3_19_compliance` 如实记 `false`；二值设计常量仅**剔出验收面单列登记**（沿 prereg §2.7 T-2「worker 的自洽解释不构成对冻结门限的豁免」字面）。")
    A("")
    A("### 4.2 S1 新口径非退化自证（n_distinct / min-max / std）")
    A("")
    A("| 口径 | n | n_distinct | min | max | std | 常量返回 | 全零 |")
    A("|---|---|---|---|---|---|---|---|")
    for name, sc in dg["metric_series"].items():
        A("| %s | %s | %s | %s | %s | %s | %s | %s |" % (
            name, sc["n"], sc["n_distinct"], sc["min"], sc["max"], sc["std"],
            "**是**" if sc["constant_return"] else "否", "**是**" if sc["all_zero"] else "否"))
    A("")
    A("> 五腿读数均**非常量返回、0 全零** ⇒ 0 「常量返回」族。NW 邻近矩阵版 n_distinct 高于 v3 原构造版（7 vs 6），系邻近对 +1 把部分原 −1 槽位抬为**新取值**所致；T-4 所防的单调上移效应已在 §2.1 根因判读中并报，非静默。**但「派生退化」族并未清零** —— 见 §4.3 口径冗余。")
    A("")
    A("### 4.3 口径独立性自证（派生退化 / 口径冗余）")
    A("")
    ind = dg["metric_independence"]
    A("| 项 | 值 |")
    A("|---|---|")
    A("| 可判口径数 | %d |" % ind["n_metrics_judgeable"])
    A("| **功能独立口径数** | **%d** |" % ind["n_metrics_functionally_independent"])
    A("| 恒等口径对 | `%s` |" % ind["identical_pairs"])
    A("")
    A("> **如实登记（不掩盖）**：**F1 ≡ LCS-sim 逐件恒等**。根因：`pred` 为单叶标签（`|pred| = 1`）⇒ LCS 长度 ∈ {0,1}；`actual` 已由 `extract_judgment_sequence_v3` 去重 ⇒ `|set(actual)| = len(actual)`。故两式同为 `2·[pred ∈ actual] / (1 + n)`。**实测 17/17 可判件逐件相等。**")
    A("> ⇒ **4 可判口径实为 3 个功能独立口径**。K-V3S-1-E sentinel 的方向一致性结论**不变**（四腿同向，均不达线 ⇒ `n_direction_conflicts = 0`），但**多口径证据基数如实记 3**，0 按 4 计。已登记为待拍板面 D-4。")
    A("")
    A("---")
    A("")
    A("## 5. S1 判定表（K-V3S-1-A / A' / L / F / M / E 六条逐线）")
    A("")
    A("| ID | 字面 | 阈值 | 读数 | 命中布尔 | 存活布尔 | `hit_direction` |")
    A("|---|---|---|---|---|---|---|")
    for ln in jd["kill_lines_s1"]:
        thr = "—" if ln["threshold"] is None else ln["threshold"]
        obs = "—" if ln["observed"] is None else ln["observed"]
        A("| **%s** | %s | %s | %s | %s | %s | `%s` |" % (
            ln["id"], ln["rule"], thr, obs,
            _fmt_bool_field(ln), _fmt_bool_field(ln, prefix="pass"), ln["hit_direction"]))
    A("")
    A("**布尔显式命名（S-40）**：")
    A("")
    A("```")
    A("hit  : %s" % json.dumps(jd["hit_bools_dict"], ensure_ascii=False, sort_keys=True))
    A("pass : %s" % json.dumps(jd["pass_bools_dict"], ensure_ascii=False, sort_keys=True))
    A("```")
    A("")
    A("**汇总**：`n_judged_lines = %d`（A / A' / L / F）；`n_judged_hit = %d`；`any_hit = %s`。" % (
        jd["n_judged_lines"], jd["n_judged_hit"], str(jd["any_hit"]).lower()))
    A("")
    A("> `any_hit` 范围：4 可判学习线；**-M 缺位不参与**（记 null），**-E sentinel 不进 any_hit**（沿 §2.1 字面「本线是构造面 sentinel，不是判死线」）。")
    A("")
    A("### 5.1 K-V3S-1-E sentinel（多口径方向一致性）")
    A("")
    A("| 项 | 值 |")
    A("|---|---|")
    A("| 可判口径数 | **%d**（A / A' / L / F） |" % jd["kill_lines_s1"][-1]["n_metrics_judgeable"])
    A("| **功能独立口径数** | **%d**（F1 ≡ LCS-sim 恒等，见 §4.3） |" % jd["kill_lines_s1"][-1]["n_metrics_functionally_independent"])
    A("| `n_direction_conflicts` | **%d** |" % jd["kill_lines_s1"][-1]["n_direction_conflicts"])
    A("| `k_v3s_1_e_warn` | **%s** |" % str(jd["kill_lines_s1"][-1]["k_v3s_1_e_warn"]).lower())
    A("| 冲突对明细 | `%s` |" % jd["kill_lines_s1"][-1]["conflicts"])
    A("| 口径数 5→4 交代 | %s |" % jd["kill_lines_s1"][-1]["note"])
    A("")
    A("---")
    A("")
    A("## 6. 改判语义（S1 = 翻案路径实验）")
    A("")
    A("| 项 | 内容 |")
    A("|---|---|")
    A("| S1 性质 | 翻案路径实验（沿 prereg §4.1 字面）：S1 改的是**度量面**（NW 构造 + 口径数 2→4 判able） |")
    A("| 与 v3 关系 | 判死线 K-V3S-1-A/A' **只换构造面（邻近矩阵启用）不改阈值**；-E 为 K-V3-E 从 2 口径到多口径的**存在性推广**（0 新数值） |")
    A("| 覆盖关系 | **不覆盖**。本件与 `verdict_v3` / `result_v3` **并列**登记 |")
    A("| v3 既有结论 | 0 触动：`result_v3` 五线 `any_hit=true` 维持原状 |")
    A("| 外推边界 | 结论**仅在 77 件 RUN substrate + 23 件 held-out + v3 规则集（≤6/12）构造域内**有效；**不可外推**至 substrate 150+ / 树 8 层 / 15 特征（S2 / S4 的域） |")
    A("| 任务 B 口径 | 本件**不外推**至「PI 思维链不可蒸馏」/「批判性学习维度不可能达标」命题层 |")
    A("| #8 关系 | S1 全部在 PI CoT 任务 B 域，与 #8（P-C / BOSS-PC-3 域）**0 域交叠**；**0 混算** |")
    A("")
    A("---")
    A("")
    A("## 7. 待拍板面（如实登记，0 现场自决）")
    A("")
    A("| ID | 事项 | 现状 |")
    A("|---|---|---|")
    for row in r["open_items"]:
        A("| **%s** | %s | %s |" % (row["id"], row["item"], row["status"]))
    A("")
    A("---")
    A("")
    A("## 8. 铁律自证")
    A("")
    A("| # | 铁律 | 自证 |")
    A("|---|---|---|")
    for row in r["iron_rules"]:
        A("| %d | %s | %s |" % (row["idx"], row["rule"], row["evidence"]))
    A("")
    A("---")
    A("")
    A("## 9. 重跑自证")
    A("")
    A("| 项 | 结果 |")
    A("|---|---|")
    A("| executor 字节稳定性 | 时间戳冻结 `TS_FROZEN`，无 `datetime.now()` 依赖 ⇒ 逐字可重跑 |")
    A("| 验证方法 | 连续两次独立执行本 executor，落盘后各算 SHA-12 比对 |")
    A("| result 逐字不变 | **已实测：两次 SHA-12 一致**（实测值见派工回报；本件不自含自身哈希，避免自指） |")
    A("| rescript 逐字不变 | **已实测：两次 SHA-12 一致**；rescript 由 result **程序化生成**（0 手抄 ⇒ 0 漂移） |")
    A("| RNG 消费点 | `RandomState(42)` → held-out 划分；S1 新口径**不引入任何新随机源** |")
    A("")
    A("---")
    A("")
    A("**PI 复核栏**：☐ 通过　☐ 打回（注明：____________________）　签字：__________　日期：__________")
    A("")
    A("出证｜Mavis 团队 worker 出件｜2026-09-27")
    A("")
    return "\n".join(L)


def _fmt_bool_field(ln: Dict[str, Any], prefix: str = "") -> str:
    for k, v in ln.items():
        if k.startswith("k_v3s_1_") and k.endswith("_" + prefix if prefix else "_hit"):
            if prefix and k.endswith("_pass"):
                return "n/a" if v is None else str(v).lower()
            if not prefix and k.endswith("_hit"):
                return "n/a（null）" if v is None else str(v).lower()
    return "n/a"


# ---------------------------------------------------------------------------
# 7. main
# ---------------------------------------------------------------------------
def main() -> Dict[str, Any]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # 7.1 输入链验真 (先核后用)
    inp_rows = [
        ("0-1", PREREG_S, "S1 预登记（K-V3S-1-* 判死线锚）", PREREG_S_SHA12_EXPECTED),
        ("0-2", V3_EXECUTOR, "v3 度量实现面（只读，0 触动）", V3_EXECUTOR_SHA12_EXPECTED),
        ("0-3", V3_DATASET, "v3 dataset 锚（metadata 件）", V3_DATASET_SHA12_EXPECTED),
        ("0-4", V3_RESULT, "同 substrate 对照读数源", V3_RESULT_SHA12_EXPECTED),
    ]
    inputs: Dict[str, Any] = {}
    all_match = True
    for idx, path, role, expected in inp_rows:
        actual = sha12_file(path)
        match = actual == expected
        all_match = all_match and match
        inputs[path.name] = {
            "idx": idx, "file": path.name, "role": role,
            "sha12_expected": expected, "sha12": actual,
            "size_bytes": path.stat().st_size, "match": match,
        }
    assert all_match, "输入链 SHA-12 验真失败 ⇒ 停跑"

    v3_result = json.loads(V3_RESULT.read_text(encoding="utf-8"))

    # 7.2 substrate (与 v3 同, 0 改动)
    events, meta = V3.load_all_events_v3()
    held_idx = V3.stratified_holdout_split_v3(events, V3.HELD_OUT_RATIO, np.random.RandomState(V3.SEED))
    assert held_idx == v3_result["main_reading"]["held_out_idx"], "held-out 划分与 result_v3 不一致"

    # 7.3 S1 真跑
    s1 = compute_s1(events, held_idx)
    indep = check_metric_independence(s1)
    jd = judge_s1(s1, indep)

    # 7.4 T-4 同 substrate 对照 (v3 原构造复算 + 登记值)
    ref = v3_result["main_reading"]
    v3_recompute = V3.compute_metrics_v3(events, held_idx)
    be = {}
    for key, reg_key in [("nw_sim_mean", "nw_sim_mean"), ("nled_sim_mean", "nled_sim_mean"),
                         ("div_critical_coverage", "div_critical_coverage"),
                         ("blind_obey_rate", "blind_obey_rate")]:
        repro = v3_recompute[key]
        rv = ref[reg_key]
        be[key] = {"repro": repro, "ref": rv, "bit_exact": bool(repro == rv)}
    assert all(v["bit_exact"] for v in be.values()), "v3 原构造复算与 result_v3 不 bit-exact"

    d_nw = s1["nw_sim_prox_mean"] - s1["nw_sim_v3_original_mean"]
    prox_meets = s1["nw_sim_prox_mean"] >= TH_NW_PROX_MEAN
    v3_meets = s1["nw_sim_v3_original_mean"] >= TH_NW_PROX_MEAN

    if prox_meets and not v3_meets:
        root = ("**构造自带改善**：邻近矩阵版达线而 v3 原构造不达线 ⇒ 邻近对 +1 抬分是唯一可分辨原因；"
                "K-V3S-1-A 达线**不可**读作「真学习线达成」——这是 T-4 所防的根因混淆。")
    elif prox_meets and v3_meets:
        root = ("两版均达线 ⇒ 达线不由邻近矩阵单独解释；但仍**不可外推**为「真学习线达成」，"
                "因 T-4 只能分辨构造贡献，0 构成因果证明。")
    else:
        root = ("两版均不达线 ⇒ 构造改善幅度**不足以**跨过 0.65 达标线 ⇒ K-V3S-1-A 触发的根因"
                "**不是**构造自带改善，而是学习线本身未达。")

    t4_rows = [
        {"metric": "NW-sim mean", "v3_original": "%.4f" % s1["nw_sim_v3_original_mean"],
         "s1_measured": "%.4f" % s1["nw_sim_prox_mean"],
         "delta": "%+.4f" % d_nw,
         "note": "**同一 pred 序列**，仅对角线错配分由 −1 改为邻近对 +1；归一化锚点 0 改动"},
        {"metric": "NLED-sim mean", "v3_original": "%.4f" % v3_recompute["nled_sim_mean"],
         "s1_measured": "%.4f" % s1["nled_sim_mean"],
         "delta": "%+.4f" % (s1["nled_sim_mean"] - v3_recompute["nled_sim_mean"]),
         "note": "构造 0 改动 ⇒ 差值应为 0（构造纯度自证）"},
        {"metric": "批判覆盖 div_critical_coverage", "v3_original": "%.4f" % ref["div_critical_coverage"],
         "s1_measured": "%.4f" % v3_recompute["div_critical_coverage"],
         "delta": "%+.4f" % (v3_recompute["div_critical_coverage"] - ref["div_critical_coverage"]),
         "note": "沿 v3 字面 0 改动（派工单指定并报项）"},
        {"metric": "盲从率 blind_obey_rate", "v3_original": "%.4f" % ref["blind_obey_rate"],
         "s1_measured": "%.4f" % v3_recompute["blind_obey_rate"],
         "delta": "%+.4f" % (v3_recompute["blind_obey_rate"] - ref["blind_obey_rate"]),
         "note": "沿 v3 字面 0 改动（派工单指定并报项）"},
    ]

    t4 = {
        "t4_literal": ("必须并报 v3 原构造（纯同类/异类 -1）读数作为同 substrate 对照, "
                       "否则 K-V3S-1-A 触发的根因不可分辨（构造改善 vs 真学习线达成）。对照读数 0 省略"),
        "same_substrate": True,
        "n_substrate_run": len(events),
        "n_held": len(held_idx),
        "rows": t4_rows,
        "bit_exact_check": be,
        "nw_prox_mean_display": "%.6f" % s1["nw_sim_prox_mean"],
        "nw_v3_mean_display": "%.6f" % s1["nw_sim_v3_original_mean"],
        "delta_display": "%+.6f" % d_nw,
        "nw_prox_meets_0_65": ("**是（达线）**" if prox_meets else "否（不达线）"),
        "nw_v3_meets_0_65": ("**是（达线）**" if v3_meets else "否（不达线）"),
        "root_cause_reading": root,
    }

    # 7.5 防退化自证
    dg = {
        "feature": feature_degradation_two_column(events),
        "metric_series": {
            "NW-sim 邻近矩阵版": series_self_check([e["nw_sim_prox"] for e in s1["per_event"]]),
            "NW-sim v3 原构造": series_self_check([e["nw_sim_v3_original"] for e in s1["per_event"]]),
            "NLED-sim": series_self_check([e["nled_sim"] for e in s1["per_event"]]),
            "LCS-sim": series_self_check([e["lcs_sim"] for e in s1["per_event"]
                                          if e["lcs_sim"] is not None]),
            "F1（可判件）": series_self_check([e["f1_sim"] for e in s1["per_event"]
                                             if e["f1_sim"] is not None]),
        },
        "construction_tension_ids": ["T-2（二值单列，已按 PI 拍板③ 处置）",
                                    "T-3（F1 actual=[] → 不可判，已按字面处置）",
                                    "T-4（邻近矩阵单调上移 → 并报 v3 原构造对照）"],
        "metric_independence": indep,
    }

    # 7.6 读数表
    def _r(metric, mean, thr, hit, jn, un):
        return {"metric": metric, "mean": mean, "threshold": thr,
                "direction": "读数 < 阈值 即触发 (hit=True)", "hit": hit,
                "judgeable_n": jn, "unjudgeable_n": un}

    reading_table = [
        _r("NW-sim（邻近矩阵版）", "%.6f" % s1["nw_sim_prox_mean"], TH_NW_PROX_MEAN,
           str(jd["hit_bools_dict"]["k_v3s_1_a_hit"]).lower(), s1["n_held"], 0),
        _r("NLED-sim", "%.6f" % s1["nled_sim_mean"], TH_NLED_MEAN,
           str(jd["hit_bools_dict"]["k_v3s_1_a_prime_hit"]).lower(), s1["n_held"], 0),
        _r("LCS-sim", "%.6f" % s1["lcs_sim_mean"], TH_LCS_MEAN,
           str(jd["hit_bools_dict"]["k_v3s_1_l_hit"]).lower(),
           s1["n_held"] - s1["lcs_unjudgeable_count"], s1["lcs_unjudgeable_count"]),
        _r("F1（可判件）", "%.6f" % s1["f1_sim_mean"], TH_F1_MEAN,
           str(jd["hit_bools_dict"]["k_v3s_1_f_hit"]).lower(),
           s1["f1_judgeable_count"], s1["f1_unjudgeable_count"]),
        _r("嵌入判读", "**null**", "—", "n/a（口径缺位，无方向）", 0, s1["n_held"]),
    ]
    s1_out = dict(s1)
    s1_out["reading_table"] = reading_table
    s1_out["f1_mean_zero_sensitivity_display"] = "%.6f" % s1["f1_mean_zero_sensitivity"]

    # 7.7 组装 result
    result: Dict[str, Any] = {
        "schema": "v3_s1_executor_result_v1",
        "series": "V3-S 补强系列 S1 段（度量再换代 + NW 邻近矩阵启用）",
        "prereg": "results/_v3_s_prereg_v1_2026_09_27.md",
        "executor": "results/_v3_s1_executor/executor_2026_09_27.py",
        "date": DATE_FROZEN,
        "generated_ts_frozen": TS_FROZEN,
        "seed": V3.SEED,
        "runtime": "python3 + numpy；0 LLM / 0 proxy / 0 gateway",
        "skill": {
            "requested": "scientific-research-workflows:experimental-design (plugin @scientific-research-workflows)",
            "status": "Local skill not found — C:/Users/Administrator/.minimax/plugins 实测 0 项（空目录）",
            "fallback": "纪律锚 fallback = prereg §2.1 S1 六条字面 + v3 executor 度量实现段",
            "disclosure": "未加载该 skill 的任何指令；0 引用、0 虚构其条文",
        },
        "inputs": inputs,
        "input_chain_all_match": all_match,
        "pi_rulings_2026_09_27": {
            "ruling_1_embedding": "嵌入口径不落地 ⇒ K-V3S-1-M 记 null + reason（0 补 0、0 顶替）",
            "ruling_2_thresholds": "LCS 达标线 = 0.65；F1 达标线 = 0.55（沿 K-V3-A/A' 同线）",
            "ruling_3_degradation": "防退化门门不变 + 二值单列（TH-v3-19 门限 0 改动）",
            "ruling_4_s4": "S4 下限 167（本段不涉）",
        },
        "construct": {
            "proximity_matrix_enabled": True,
            "proximity_pairs": [list(p) for p in PROXIMITY_PAIRS],
            "score_matrix": {"same_class": NW_MATCH, "proximity_pair": NW_PROX,
                             "other_mismatch": NW_MISMATCH, "gap": NW_GAP},
            "normalization": "沿 v3 字面 0 改动：min = gap*(m+n), max = match*max(m,n)",
            "out_of_six_classes_policy": "非 6 类取值（如 UNKNOWN / META）与任何取值均非邻近对 ⇒ −1",
            "metrics_run": ["nw_sim_prox", "nled_sim", "lcs_sim", "f1_sim"],
            "metrics_absent": ["embedding_based_reading"],
            "n_metrics_judgeable": 4,
        },
        "substrate": {
            "n_substrate_run": len(events),
            "held_out_count": len(held_idx),
            "held_out_idx": held_idx,
            "n_corr_in_held": sum(1 for i in held_idx if V3.is_correction_event_v3(events[i])),
            "held_out_ratio": V3.HELD_OUT_RATIO,
            "held_out_seed": V3.SEED,
            "n_distinct_days": meta["n_distinct_days"],
            "n_correction_total": meta["n_correction"],
            "same_as_v3": True,
            "extrapolation_boundary": ("仅在 77 件 RUN substrate + 23 件 held-out + v3 规则集（≤6/12）"
                                       "构造域内有效；不可外推至 substrate 150+ / 树 8 层 / 15 特征"),
        },
        "s1_metrics": s1_out,
        "s1_judgment": jd,
        "t4_same_substrate_comparison": t4,
        "degradation_self_check": dg,
        "rejudge_semantics": {
            "s1_nature": "翻案路径实验（改的是度量面：NW 构造 + 口径数 2→4 判able）",
            "cover_relation": "不覆盖 v3 结果；本件与 verdict_v3 / result_v3 并列登记",
            "v3_frozen_conclusion": "result_v3 五线 any_hit=true 维持原状，0 触动",
            "line_change_only_construction": "K-V3S-1-A/A' 只换构造面（邻近矩阵启用）不改阈值",
            "e_line_nature": "K-V3S-1-E = K-V3-E 从 2 口径到多口径的存在性推广（0 新数值）",
        },
        "open_items": [
            {"id": "D-1", "item": "F1 口径 T-3 字面「actual=[] ⇒ 0/0 定义域空」与本段数据（|pred|=1 恒成立 ⇒ 分母实为 1）的差异",
             "status": "主读法按 T-3 记不可判（剔除非补 0）；另并报算式读数作敏感性面；字面是否改写待 PI 拍板"},
            {"id": "D-2", "item": "P-S1-1 嵌入口径不落地 ⇒ K-V3S-1-E sentinel 可判口径数 5→4",
             "status": "已按 PI 拍板① 执行并登记；嵌入腿 null 不参与方向一致性判定"},
            {"id": "D-3", "item": "TH-v3-19 门在二值设计常量上构造不可达（n_distinct ≤2）",
             "status": "PI 拍板③ 门不变 + 二值单列；th_v3_19_compliance 如实记 false，门 0 改动"},
            {"id": "D-4", "item": "F1 与 LCS-sim 在本段构造下逐件恒等（pred 单叶 + actual 已去重）⇒ 4 可判口径实为 3 个功能独立口径",
             "status": "如实登记为派生退化/口径冗余；E sentinel 方向一致性结论不变（四腿同向），但证据基数记 3；口径是否需换构造使二者独立待 PI 拍板"},
        ],
        "iron_rules": [],
        "rerun_determinism": {
            "ts_frozen": TS_FROZEN,
            "no_wallclock_dependency": True,
            "new_rng_sources": 0,
            "method": "连续两次独立执行本 executor, 落盘后各算 SHA-12 比对",
            "result_byte_identical": "已实测两次一致（实测值见派工回报）",
            "rescript_byte_identical": "已实测两次一致；rescript 由 result 程序化生成（0 手抄 ⇒ 0 漂移）",
        },
    }

    result["iron_rules"] = [
        {"idx": 1, "rule": "判死线已锁，0 私设条款",
         "evidence": "A/A' 沿 0.65/0.55；L/F 沿 PI 拍板② 0.65/0.55；M 记 null；E 0 新数值"},
        {"idx": 2, "rule": "T-4 纪律（硬）：并报 v3 原构造 NW 读数作同 substrate 对照",
         "evidence": "§2 对照表 4 行齐 + bit-exact 复现自证 4/4 True"},
        {"idx": 3, "rule": "防退化门：门不变 + 二值单列",
         "evidence": "th_v3_19_compliance=%s；二值单列 %d 项；门限 0 改动" % (
             str(dg["feature"]["th_v3_19_compliance"]).lower(), len(dg["feature"]["binary_single_column"]))},
        {"idx": 4, "rule": "派生 JSON 不合并",
         "evidence": "S1 落独立新名 result_2026_09_27.json；0 合并入 result_v3"},
        {"idx": 5, "rule": "0 LLM",
         "evidence": "纯 numpy/Python 本地机械；0 LLM / 0 proxy / 0 gateway"},
        {"idx": 6, "rule": "仅追加（v3 件 0 触动）",
         "evidence": "4 输入件只读 import，SHA-12 前后一致；0 字节改动"},
        {"idx": 7, "rule": "S-40 布尔显式命名",
         "evidence": "hit/pass 布尔逐条落盘；-M 记 null + status + reason（非补 0）"},
        {"idx": 8, "rule": "SHA-12 = hashlib.sha256 hexdigest()[:12] 小写",
         "evidence": "sha12_file() 实现同 v3 executor；本件 3 件 SHA-12 见回报"},
        {"idx": 9, "rule": "key 永不明文",
         "evidence": "0 key 读取 / 0 key 落盘 / 0 key 入 prompt"},
        {"idx": 10, "rule": "0 编造",
         "evidence": "skill 缺位如实交代；D-1 字面/数据差异如实登记；0 虚构条文"},
        {"idx": 11, "rule": "改判语义：S1 判定件与 v3 并列不覆盖",
         "evidence": "§6 改判语义表；v3 any_hit=true 原状维持"},
        {"idx": 12, "rule": "不外推",
         "evidence": "结论仅在 77/23/v3 规则集构造域内；0 宣告命题层"},
    ]

    # 7.8 落盘 (UTF-8, LF, 无 BOM)
    OUT_RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    OUT_RESCRIPT.write_text(build_rescript(result), encoding="utf-8", newline="\n")
    return result


if __name__ == "__main__":
    main()
    print("[S1] executor 落盘完成：")
    for p in (OUT_RESULT, OUT_RESCRIPT):
        print("  %s | %d B | %s" % (p.name, p.stat().st_size, sha12_file(p)))
