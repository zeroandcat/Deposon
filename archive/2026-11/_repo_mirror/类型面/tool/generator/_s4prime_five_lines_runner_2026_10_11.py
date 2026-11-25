#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S4' 五线面 · 重判实跑 runner (worker 面 · §5-2 `S4'` 行 · 卡九 `s4_lines`＝甲·授权(仅五线面))

只读复用 executor `8a81d90c69ba` (results/_v4_pi_cot_v3_ruleset_v3_executor.py):
  ⛔ 0 编辑 / 0 覆写 / 0 就地改 / 0 monkey-patch 常量 —— 仅 `importlib` 只读加载并逐字调用其函数。

复现路径 (26c8278e3552 §4 十步): 步 1-9 全沿用 · 步 10 之 `in_heldout` 换新 held-out (3c25e1a2ea94)。

五线 (沿旧域同名线 · 80d765f34163 §5.1 / 73550514152d §3.7):
  A  = nw_sim_mean        (gold=KEYWORDS_V3.1 · model=V3)
  A' = nled_sim_mean      (同上)
  B  = n_critical_among_divergent / n_divergent
  C  = n_blind_obey / n_agree
  D  = A 线 NW-sim 主口径 bootstrap CI 下界 (= A 之 CI 本身, executor L1164-L1166)

⛔ 0 否决轴 / 0 触发量 (其门控未闭 · 不开跑) · ⛔ 0 判档 / 0 代裁 / 0 改阈值 / 0 预写结论
⛔ 0 网络 / 0 LLM / 0 API key / 0 读 .env
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import pathlib
from typing import Any, Dict, List, Tuple

import numpy as np

RESULTS = pathlib.Path(__file__).resolve().parent
REPO = RESULTS.parent
EXECUTOR = RESULTS / "_v4_pi_cot_v3_ruleset_v3_executor.py"
EXECUTOR_SHA12_EXPECTED = "8a81d90c69ba"

# 新构造域锚 (CH-D) — PI 核准生效
NEW_HELDOUT_JSON = RESULTS / "_s4_heldout_sampling_seedprime_items_2026_10_10.json"
NEW_HELDOUT_SHA12_EXPECTED = "6cbb8ba01bfb"
OLD_HELDOUT_JSON = RESULTS / "_s4_heldout_sampling_seed42_items_2026_10_09.json"  # 仅供管道同源自证
OLD_HELDOUT_SHA12_EXPECTED = "6a670e629dca"
NEW_FP_EXPECTED = "3c25e1a2ea94"

# 步 2 · source_wave 三层映射 (26c8278e3552 §3 全表逐字)
WAVE_LAYER_A = {
    "_v4_pi_cot_v2_dataset_addendum_2026_09_24.json": "D1_supp",
    "_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json": "D2_w1",
    "_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json": "D2_w2",
    "_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json": "D2_w3",
    "_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json": "D2_w4",
    "_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json": "D2_w5",
    "_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json": "D3_w1",
    "_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json": "D3_w2",
    "_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json": "D3_w3",
}
WAVE_LAYER_B = {"_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json": "D4_w1"}
WAVE_LAYER_C_LABEL = "S4_face_unregistered_wave"  # 层 C 惰性标签 (常量字面)

# 步 8 · KEYWORDS_V3.1 = KEYWORDS_V3 ⊎ 15 词 (1b7bcbcce589 §4.1/§4.2 逐字 · 0 增 0 删 0 改层)
V31_ADD15: Dict[str, Tuple[str, ...]] = {
    "CRITERIA": ("复核", "质量", "保证", "对齐", "失实"),          # T1 复核/质量/保证 · T2 对齐/失实
    "RISK": ("回退", "遗忘", "记忆效应", "噪声", "缺陷", "观察者效应"),  # T1 回退/遗忘 · T2 其余四
    "KILL_LINE": ("推翻", "检验"),                                  # T1 推翻 · T2 检验
    "TIMING": ("挂起", "后面"),                                     # T2 挂起/后面
    "COST": (),                                                    # 无新增
    "DELEGATE": (),                                                # 无新增
}


def sha12_file(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def load_executor():
    """只读加载 executor (⛔ 0 修改磁盘字节 · 0 monkey-patch)。"""
    got = sha12_file(EXECUTOR)
    if got != EXECUTOR_SHA12_EXPECTED:
        raise SystemExit(f"executor SHA-12 mismatch: {got} != {EXECUTOR_SHA12_EXPECTED}")
    spec = importlib.util.spec_from_file_location("exec_v3_ro", EXECUTOR)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def build_kwtable_v31(ex) -> Dict[str, Tuple[str, ...]]:
    """KEYWORDS_V3.1 = KEYWORDS_V3 单调增广 15 词 (⛔ 0 删 0 改 0 改层)。"""
    kw: Dict[str, Tuple[str, ...]] = {k: tuple(v) for k, v in ex.KEYWORDS_V3.items()}
    for layer, words in V31_ADD15.items():
        kw[layer] = tuple(kw[layer]) + tuple(words)
    return kw


def extract_seq(reasoning: str, kwtable: Dict[str, Tuple[str, ...]],
                phrase_patterns, ex) -> List[str]:
    """步 7 · extract_judgment_sequence_v3 之逐字复制 (ex L478-L519 · 唯一差别 = 词表入参)。

    机制不变: 逐层取最早位置 → 按位置排序 + dedup 保序 → 5 条短语模式追加。
    """
    if not reasoning or not reasoning.strip():
        return []
    earliest = []
    for jt, kws in kwtable.items():
        pos = -1
        for kw in kws:
            idx = reasoning.find(kw)
            if idx >= 0 and (pos < 0 or idx < pos):
                pos = idx
        if pos >= 0:
            earliest.append((pos, jt))
    earliest.sort(key=lambda x: x[0])
    seq: List[str] = []
    seen = set()
    for _, jt in earliest:
        if jt not in seen:
            seen.add(jt)
            seq.append(jt)
    for pat in phrase_patterns:
        if pat["pattern"] in reasoning:
            for jt in pat["target_seq"]:
                if jt not in seen:
                    seen.add(jt)
                    seq.append(jt)
    return seq


def build_face(ex, r1_files: List[str]) -> Tuple[List[Dict[str, Any]], List[Tuple[str, int]]]:
    """步 1-6 · 重建 179 行面 (R1 字节序 × 件内 idx 升序 · 三层 wave · is_correction 真值化)。

    Returns: (events, key_index)  key_index[i] = (filename, idx) of events[i]
    """
    events: List[Dict[str, Any]] = []
    key_index: List[Tuple[str, int]] = []

    for fname in r1_files:                                   # 步 1 · R1 字节序
        fp = RESULTS / fname
        ad = json.loads(fp.read_text(encoding="utf-8"))
        if fname in WAVE_LAYER_A:                            # 步 2 · 层 A canonical
            wave = WAVE_LAYER_A[fname]
        elif fname in WAVE_LAYER_B:                          # 步 2 · 层 B D4_w1
            wave = WAVE_LAYER_B[fname]
        else:                                                # 步 2 · 层 C 惰性标签
            wave = WAVE_LAYER_C_LABEL
        sups = ad.get("supplements", []) or []               # 步 3 · 0 去重 0 改序
        for idx, sup in enumerate(sups):                     # 步 3 · 件内 idx 升序
            ev = ex.load_addendum_event_v3(sup, wave, fname)  # 步 4 · 逐字调用
            # 步 6 · is_correction 真值化适配 (73550514152d §2.3(b) · 0 改 executor)
            raw = sup.get("is_correction")
            if raw is True or (isinstance(raw, str)
                               and (raw.endswith("_pair_pending") or raw == "R_pair")):
                ev["is_correction"] = "R_pair"
            else:
                ev["is_correction"] = False
            events.append(ev)
            key_index.append((fname, idx))
    return events, key_index


def grid_domain_selfproof(events: List[Dict[str, Any]], ex) -> Dict[str, Any]:
    """面构造自证一 · 13 项格域 (73550514152d §1.3 · 与 24ea764daeac 逐值复现)。"""
    cells: Dict[Tuple[int, int, int], int] = {}
    n_b1_rows = 0
    for ev in events:
        f = ex.feats_v3(ev)
        cell = (f["is_corr_pair"], f["scene_bucket_8"], f["opt_bucket_8"])
        cells[cell] = cells.get(cell, 0) + 1
        n_b1_rows += f["is_corr_pair"]
    n_list = [cells[c] for c in cells]
    total = len(events)
    return {
        "occupied_cells": len(cells),
        "empty_cells": 128 - len(cells),
        "sum_floor_0.30n": sum((3 * n) // 10 for n in n_list),
        "cells_n_ge_4": sum(1 for n in n_list if n >= 4),
        "cells_n_le_3": sum(1 for n in n_list if n <= 3),
        "cells_n_eq_1": sum(1 for n in n_list if n == 1),
        "n_min": min(n_list),
        "n_max": max(n_list),
        "n_sum": sum(n_list),
        "b0_occupied_cells": sum(1 for c in cells if c[0] == 0),
        "b1_occupied_cells": sum(1 for c in cells if c[0] == 1),
        "b1_rows": n_b1_rows,
        "grid_total": 128,
        "n_events": total,
    }


def boot_ci(scores: List[float], n_boot: int = 1000,
            lo_pct: float = 0.025, hi_pct: float = 0.975) -> Tuple[float, float]:
    """逐字复制 ex.bootstrap_ci_v3 (L1086-L1102) · 含其 `hi=accs[int(0.975*n)-1]` 偏保守取法。"""
    n = len(scores)
    if n == 0:
        return 0.0, 0.0
    rng = np.random.RandomState(ex_seed_holder[0].SEED + 13)   # executor L1164 · 0 自造偏移
    accs = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        accs.append(float(np.mean([scores[i] for i in idx])))
    accs.sort()
    lo = accs[int(lo_pct * n_boot)]
    j = int(hi_pct * n_boot) - 1
    hi = accs[j] if j < len(accs) else accs[-1]
    return lo, hi


def ratio_ci_sub(ind: List[int], n_boot: int = 1000) -> Tuple[float, float]:
    """B/C 构造①「自身域」· 仅在子集内重采样 0/1 指示量 (6db4d0fb2452 §3)。"""
    n = len(ind)
    if n == 0:
        return 0.0, 0.0
    rng = np.random.RandomState(ex_seed_holder[0].SEED + 13)
    accs = []
    for _ in range(n_boot):
        j = rng.randint(0, n, size=n)
        accs.append(float(np.mean([ind[i] for i in j])))
    accs.sort()
    lo = accs[25]
    hi = accs[974] if 974 < len(accs) else accs[-1]
    return lo, hi


def ratio_ci_full(items: List[Tuple[bool, int]], which: str,
                  n_boot: int = 1000) -> Tuple[float, float, int]:
    """B/C 构造②「全体 held-out」· 对全部 held-out (R1 键序, 0 重排) 重采样, 每次内重算比率。

    items[i] = (is_divergent, indicator); indicator = 批判反思 (B) 或 盲从 (C) 之 0/1。
    子集为空时按 executor 字面取 B=1.0 / C=0.0 (6db4d0fb2452 §3 构造②)。
    """
    ex = ex_seed_holder[0]
    n = len(items)
    rng = np.random.RandomState(ex.SEED + 13)
    accs = []
    degen = 0
    for _ in range(n_boot):
        j = rng.randint(0, n, size=n)
        if which == "B":
            den = sum(1 for i in j if items[i][0])
            num = sum(items[i][1] for i in j if items[i][0])
            if den == 0:
                degen += 1
                accs.append(1.0)
            else:
                accs.append(num / den)
        else:
            den = sum(1 for i in j if not items[i][0])
            num = sum(items[i][1] for i in j if not items[i][0])
            if den == 0:
                degen += 1
                accs.append(0.0)
            else:
                accs.append(num / den)
    accs.sort()
    lo = accs[25]
    hi = accs[974] if 974 < len(accs) else accs[-1]
    return lo, hi, degen


ex_seed_holder: List[Any] = [None]


def held_idx_from(keys: List[Tuple[str, int]],
                  held_keys: List[Tuple[str, int]]) -> List[int]:
    """held-out 键 (file#idx) → 全局面索引 (R1 序) · 口径沿步 10 0 改判据。"""
    lookup = {k: i for i, k in enumerate(keys)}
    return [lookup[k] for k in held_keys]


def run_five_lines(ex, events, keys, held_keys, kw_gold) -> Dict[str, Any]:
    """五线 + CI + 逐件 (单一 gold 口径 · model 侧恒 V3)。"""
    kw_model = ex.KEYWORDS_V3                       # model 侧 = V3 (标签 + n_keywords_hit 特征)
    held_idx = held_idx_from(keys, held_keys)
    held_set = set(held_idx)

    rows_all = [ex.feats_v3(ev) for ev in events]    # 特征 12 项 (ex L548-L601 · V3 词表)
    labels = [ex.primary_judgment_type_v3(
        extract_seq(ev.get("reasoning_full", ""), kw_model, ex.PHRASE_PATTERNS_V3, ex))
        for ev in events]                             # 训练标签源 = KEYWORDS_V3

    tr_rows = [rows_all[i] for i in range(len(events)) if i not in held_set]
    tr_lab = [labels[i] for i in range(len(events)) if i not in held_set]
    tree = ex.build_tree(tr_rows, tr_lab)             # 贪心信息增益 · 深度 ≤ 6

    per_item = []
    per_nw, per_nled, div_flags, crit_flags = [], [], [], []
    for i in held_idx:                                # held-out 按 R1 键序
        ev = events[i]
        pred = ex.predict_tree(tree, rows_all[i])
        rf = ev.get("reasoning_full", "")
        seq_gold = extract_seq(rf, kw_gold, ex.PHRASE_PATTERNS_V3, ex)      # gold = V3.1
        seq_v3 = extract_seq(rf, kw_model, ex.PHRASE_PATTERNS_V3, ex)      # 定位列 (非五线)
        nw = ex.nw_sim([pred], seq_gold)
        nled = ex.nled_sim([pred], seq_gold)
        nw_v3 = ex.nw_sim([pred], seq_v3)
        nled_v3 = ex.nled_sim([pred], seq_v3)
        is_div = (pred not in seq_gold)
        crit = ex.has_critical_reflection_v3(rf)
        per_nw.append(nw)
        per_nled.append(nled)
        if is_div:
            div_flags.append(1 if crit else 0)
            crit_flags.append(1 if crit else 0)
        else:
            div_flags.append(None)
            crit_flags.append(1 if crit else 0)
        per_item.append({
            "face_index": i, "key": list(keys[i]), "q_id": ev.get("q_id"),
            "pred": pred, "gold_seq_v31": seq_gold, "gold_seq_v3": seq_v3,
            "nw_v31": nw, "nled_v31": nled, "nw_v3": nw_v3, "nled_v3": nled_v3,
            "divergent": bool(is_div), "critical": bool(crit),
            "corpus_len": len(rf or ""),
        })

    nw_mean = float(np.mean(per_nw))
    nled_mean = float(np.mean(per_nled))

    # B / C 分子分母 (executor L1151-L1159 字面)
    n_div = sum(1 for f in div_flags if f is not None)
    n_crit_among_div = sum(f for f in div_flags if f is not None)
    b_point = (n_crit_among_div / n_div) if n_div > 0 else 1.0
    agree_idx = [i for i, f in enumerate(div_flags) if f is None]
    n_agree = len(agree_idx)
    n_blind = sum(1 for i in agree_idx if crit_flags[i] == 0)
    c_point = (n_blind / n_agree) if n_agree > 0 else 0.0

    a_lo, a_hi = boot_ci(per_nw)
    ap_lo, ap_hi = boot_ci(per_nled)

    # B 指示量 = 分歧子集内「批判反思」指示 (0/1); C 指示量 = 一致子集内「盲从」(非批判) 指示 (0/1)
    div_inds = [1 if crit_flags[i] else 0 for i in range(len(per_item)) if div_flags[i] is not None]
    agree_inds = [0 if crit_flags[i] else 1 for i in agree_idx]
    b1_lo, b1_hi = ratio_ci_sub(div_inds)
    c1_lo, c1_hi = ratio_ci_sub(agree_inds)
    items_b = [(div_flags[i] is not None, (1 if crit_flags[i] else 0)
                if div_flags[i] is not None else 0) for i in range(len(per_item))]
    items_c = [(div_flags[i] is not None, (0 if crit_flags[i] else 1)
                if div_flags[i] is None else 0) for i in range(len(per_item))]
    b2_lo, b2_hi, b2_deg = ratio_ci_full(items_b, "B")
    c2_lo, c2_hi, c2_deg = ratio_ci_full(items_c, "C")

    def hw(lo, hi):
        return (hi - lo) / 2.0

    return {
        "n_events": len(events), "n_held": len(held_idx), "n_train": len(tr_rows),
        "tree_depth_observed": ex._tree_depth(tree),
        "A": {"point": nw_mean, "ci": [a_lo, a_hi], "halfwidth": hw(a_lo, a_hi), "fullwidth": a_hi - a_lo},
        "Ap": {"point": nled_mean, "ci": [ap_lo, ap_hi], "halfwidth": hw(ap_lo, ap_hi), "fullwidth": ap_hi - ap_lo},
        "B": {"num_den": [n_crit_among_div, n_div], "point": b_point,
              "ci_construct1": [b1_lo, b1_hi], "ci_construct2": [b2_lo, b2_hi],
              "degenerate_construct2": b2_deg,
              "K2_one_sided_lower_c1": b1_lo, "K2_one_sided_lower_c2": b2_lo,
              "halfwidth_c1": hw(b1_lo, b1_hi), "halfwidth_c2": hw(b2_lo, b2_hi)},
        "C": {"num_den": [n_blind, n_agree], "point": c_point,
              "ci_construct1": [c1_lo, c1_hi], "ci_construct2": [c2_lo, c2_hi],
              "degenerate_construct2": c2_deg,
              "K2_one_sided_upper_c1": c1_hi, "K2_one_sided_upper_c2": c2_hi,
              "halfwidth_c1": hw(c1_lo, c1_hi), "halfwidth_c2": hw(c2_lo, c2_hi)},
        "D": {"ci": [a_lo, a_hi], "ci_lower": a_lo, "halfwidth": hw(a_lo, a_hi),
              "note": "D 之读数面与 A 完全重合 (executor L1164-L1166 · D 0 需另算)"},
        "per_item": per_item,
    }


def main() -> None:
    ex = load_executor()
    ex_seed_holder[0] = ex
    kw31 = build_kwtable_v31(ex)

    # 锚件指纹 (自测复核 · 0 沿用他件转述)
    anchors = {
        "executor": (EXECUTOR, EXECUTOR_SHA12_EXPECTED),
        "new_heldout": (NEW_HELDOUT_JSON, NEW_HELDOUT_SHA12_EXPECTED),
        "old_heldout_selftest_only": (OLD_HELDOUT_JSON, OLD_HELDOUT_SHA12_EXPECTED),
    }
    print("=== ANCHORS ===")
    for name, (p, exp) in anchors.items():
        got = sha12_file(p)
        print(f"  {name:28s} {got}  expect={exp}  {'OK' if got == exp else 'MISMATCH'}")
        if got != exp:
            raise SystemExit(f"anchor mismatch: {name}")

    old_ds = json.loads(OLD_HELDOUT_JSON.read_text(encoding="utf-8"))
    r1_files = old_ds["domain"]["r1_byte_sorted_files"]     # 步 1 · 两集共用同一 S4 冻结面
    events, keys = build_face(ex, r1_files)
    print(f"\n=== FACE (steps 1-6) ===\n  rows={len(events)} files={len(r1_files)} (expect 179 / 21)")

    print("\n=== GRID SELF-PROOF (13 items) ===")
    g = grid_domain_selfproof(events, ex)
    expect = {"occupied_cells": 54, "empty_cells": 74, "sum_floor_0.30n": 26, "cells_n_ge_4": 16,
              "cells_n_le_3": 38, "cells_n_eq_1": 16, "n_min": 1, "n_max": 16, "n_sum": 179,
              "b0_occupied_cells": 43, "b1_occupied_cells": 11, "b1_rows": 15,
              "grid_total": 128, "n_events": 179}
    for k, v in expect.items():
        ok = g[k] == v
        print(f"  {k:22s} {g[k]:>6}  registered={v:>6}  {'OK' if ok else 'MISMATCH'}")

    # ---- 管道同源自证 (旧构造域重算 vs 在册旧值; ⛔ 非新旧读数面比较) ----
    old_held_keys = [(it["file"], it["idx"]) for it in old_ds["heldout_items"]]
    print("\n=== PIPELINE SELF-CERT (old domain, gold=V3 · vs 73550514152d §3.7) ===")
    st = run_five_lines(ex, events, keys, old_held_keys, ex.KEYWORDS_V3)
    reg = {"A": (0.32032967032967036, [0.18186813186813186, 0.44999999999999996]),
           "Ap": (0.14743589743589744, [0.038461538461538464, 0.28205128205128205]),
           "B": (0.42857142857142855, None), "C": (0.6, None), "D": (0.18186813186813186, None)}
    for line in ("A", "Ap", "B", "C", "D"):
        if line == "B":
            mine, theirs = st["B"]["point"], reg["B"][0]
        elif line == "C":
            mine, theirs = st["C"]["point"], reg["C"][0]
        elif line == "D":
            mine, theirs = st["D"]["ci_lower"], reg["D"][0]
        else:
            mine, theirs = st[line]["point"], reg[line][0]
        print(f"  {line:3s} point mine={mine!r} registered={theirs!r} "
              f"{'BIT-IDENTICAL' if mine == theirs else 'MISMATCH'}")
    for line in ("A", "Ap"):
        print(f"  {line:3s} CI    mine={st[line]['ci']} registered={list(reg[line][1])} "
              f"{'BIT-IDENTICAL' if list(st[line]['ci']) == list(reg[line][1]) else 'MISMATCH'}")
    print(f"  B num/den mine={st['B']['num_den']} registered=[9, 21]  "
          f"{'OK' if st['B']['num_den'] == [9, 21] else 'MISMATCH'}")
    print(f"  C num/den mine={st['C']['num_den']} registered=[3, 5]   "
          f"{'OK' if st['C']['num_den'] == [3, 5] else 'MISMATCH'}")
    # B/C 之 CI 亦纳入自证 (旧域在册值 · 73550514152d §3.3/§3.4)
    reg_bc = {
        "B_ci1": ([0.23809523809523808, 0.6190476190476191], st["B"]["ci_construct1"]),
        "B_ci2": ([0.22727272727272727, 0.65], st["B"]["ci_construct2"]),
        "C_ci1": ([0.2, 1.0], st["C"]["ci_construct1"]),
        "C_ci2": ([0.0, 1.0], st["C"]["ci_construct2"]),
    }
    for k, (theirs, mine) in reg_bc.items():
        print(f"  {k:6s} mine={mine} registered={theirs} "
              f"{'BIT-IDENTICAL' if list(mine) == list(theirs) else 'MISMATCH'}")
    print(f"  C degenerate c2 count mine={st['C']['degenerate_construct2']} registered=2 (旧域登记 2 次退化重抽样)")
    selfcert_bc_ok = all(list(m) == list(t) for t, m in reg_bc.values())
    print(f"  => B/C CI 自证: {'PASS' if selfcert_bc_ok else 'FAIL'}")

    # ---- 新构造域主跑 (S4') ----
    new_ds = json.loads(NEW_HELDOUT_JSON.read_text(encoding="utf-8"))
    new_items = new_ds["heldout_items"]
    new_held_keys = [(it["file"], it["idx"]) for it in new_items]
    concat = "|".join(f"{f}#{i}" for f, i in new_held_keys)
    fp = hashlib.sha256(concat.encode("utf-8")).hexdigest()
    print("\n=== HELD-OUT FINGERPRINT (K-RJ-8' new criterion) ===")
    print(f"  recomputed={fp[:12]}  full={fp}")
    print(f"  registered={new_ds['reproduction']['heldout_ordered_fingerprint']['sha12']}  "
          f"full={new_ds['reproduction']['heldout_ordered_fingerprint']['sha256']}")
    print(f"  expect={NEW_FP_EXPECTED}  match={fp[:12] == NEW_FP_EXPECTED}")
    print(f"  n={len(new_held_keys)} (expect 26)  order_in_r1_key ascending="
          f"{[it['order_in_r1_key'] for it in new_items] == list(range(26))}")
    missing = [k for k in new_held_keys if k not in dict(zip(*[iter([])] * 2))]
    miss = [k for k in new_held_keys if k not in set(keys)]
    print(f"  all keys resolve in face: {len(miss) == 0}  (unresolved={len(miss)})")

    print("\n=== S4' FIVE-LINE RUN (new domain · gold=V3.1 · model=V3) ===")
    res = run_five_lines(ex, events, keys, new_held_keys, kw31)
    print(f"  n_events={res['n_events']} n_held={res['n_held']} n_train={res['n_train']} "
          f"tree_depth={res['tree_depth_observed']}")
    for line in ("A", "Ap"):
        print(f"  {line:3s} point={res[line]['point']!r}  ci={res[line]['ci']}")
        print(f"      halfwidth={res[line]['halfwidth']!r} fullwidth={res[line]['fullwidth']!r}")
    for line in ("B", "C"):
        d = res[line]
        print(f"  {line:3s} {d['num_den'][0]}/{d['num_den'][1]} = {d['point']!r}")
        print(f"      ci1={d['ci_construct1']}  ci2={d['ci_construct2']}  degen2={d['degenerate_construct2']}")
    print(f"  D   ci={res['D']['ci']}  ci_lower={res['D']['ci_lower']!r}")

    n_empty = sum(1 for p in res["per_item"] if not p["gold_seq_v31"])
    n_div = sum(1 for p in res["per_item"] if p["divergent"])
    n_crit = sum(1 for p in res["per_item"] if p["critical"])
    n_crit_div = sum(1 for p in res["per_item"] if p["divergent"] and p["critical"])
    print(f"\n=== PER-ITEM FACTS ===")
    print(f"  empty gold seq={n_empty}/26  divergent={n_div}  critical={n_crit}  "
          f"critical&divergent={n_crit_div}")
    print(f"  nw changed vs V3-gold locator column: "
          f"{sum(1 for p in res['per_item'] if p['nw_v31'] != p['nw_v3'])}/26")
    print(f"  nled changed vs V3-gold locator column: "
          f"{sum(1 for p in res['per_item'] if p['nled_v31'] != p['nled_v3'])}/26")
    print("\n  idx | q_id | pred | gold_v31 | nw_v31 | nled_v31 | nw_v3 | nled_v3 | div | crit")
    for i, p in enumerate(res["per_item"]):
        print(f"  {i:3d} | {str(p['q_id']):9s} | {p['pred']:9s} | {str(p['gold_seq_v31']):45s} | "
              f"{p['nw_v31']:.6f} | {p['nled_v31']:.6f} | {p['nw_v3']:.6f} | {p['nled_v3']:.6f} | "
              f"{'Y' if p['divergent'] else 'n'} | {'Y' if p['critical'] else 'n'}")

    out = {
        "artifact": "_s4prime_five_lines_readings_2026_10_11.json",
        "date": "2026-10-11",
        "kind": "summary_readings",
        "step": "S4' 五线面 · 重判实跑 (worker 面)",
        "note": "汇总 JSON; 0 与逐件 JSON 合并 (沿 K-EX-10 同族); 0 判档; 0 并入否决轴/触发量",
        "authority": {
            "change_plan": {"file": "results/_g5_rejudgment_construction_change_plan_2026_10_10.md",
                            "sha12": "fa0001a6dd0a"},
            "chd_declaration": {"file": "results/_chd_construction_domain_declaration_draft_2026_10_10.md",
                                "sha12": "17cf0d59cd7b"},
            "new_heldout_items": {"file": "results/_s4_heldout_sampling_seedprime_items_2026_10_10.json",
                                  "sha12": NEW_HELDOUT_SHA12_EXPECTED},
            "new_heldout_register": {"file": "results/_s4_heldout_sampling_seedprime_items_register_2026_10_10.md",
                                     "sha12": "9da183328f18"},
            "in_heldout_recompute": {"file": "results/_s4_seedprime_inheldout_recompute_2026_10_10.md",
                                     "sha12": "cf3368e7d5a0"},
            "source_wave_mapping": {"file": "results/_s4_source_wave_mapping_registration_2026_10_10.md",
                                    "sha12": "26c8278e3552"},
            "kwtable_v31": {"file": "results/_s4_v31_keyword_table_final_2026_10_10.md",
                            "sha12": "1b7bcbcce589"},
            "executor_readonly": {"file": "results/_v4_pi_cot_v3_ruleset_v3_executor.py",
                                  "sha12": EXECUTOR_SHA12_EXPECTED},
            "old_readings_anchor_readonly": {
                "file": "results/_s4_v31_readings_execution_2026_10_10.md", "sha12": "80d765f34163"},
            "old_domain_readings_readonly": {
                "file": "results/_s4_face_five_lines_ci_readings_execution_2026_10_09.md",
                "sha12": "73550514152d"},
        },
        "runtime": {"python": "3.14.7", "numpy": "2.5.3", "network": 0, "endpoint_calls": 0,
                    "api_key": 0, "skill": 0, "llm": 0},
        "face_selfproof_grid13": {"measured": g, "registered": expect,
                                  "all_match": g == expect},
        "pipeline_selfcert_old_domain": {
            "purpose": "同代码路径于旧构造域(gold=V3/旧 held-out)重算, 与 73550514152d §3.7 在册值逐位比对; "
                       "系管道同源性自证, ⛔ 非新旧读数面之比较, ⛔ 0 并表 0 比大小",
            "A": st["A"]["point"], "A_ci": st["A"]["ci"],
            "Ap": st["Ap"]["point"], "Ap_ci": st["Ap"]["ci"],
            "B_num_den": st["B"]["num_den"], "C_num_den": st["C"]["num_den"],
            "D_ci_lower": st["D"]["ci_lower"],
        },
        "heldout_fingerprint": {
            "sha12_recomputed": fp[:12], "full_sha256_recomputed": fp,
            "sha12_registered": new_ds["reproduction"]["heldout_ordered_fingerprint"]["sha12"],
            "match": fp[:12] == NEW_FP_EXPECTED, "n": len(new_held_keys),
        },
        "model_side_declaration": {
            "gold_kwtable": "V3.1 (= KEYWORDS_V3 ⊎ 15 词, 1b7bcbcce589 §4 逐字)",
            "gold_kwtable_sha12": "1b7bcbcce589",
            "model_tree": "V3",
            "training_label_kwtable": "KEYWORDS_V3",
            "n_keywords_hit_feature_kwtable": "KEYWORDS_V3",
            "K_EX_8": "feature == label == declared model kwtable == KEYWORDS_V3 -> consistent",
            "mixed_object": False,
            "mixed_object_note": "本面 gold 与 model 皆 V3.1 同词表口径下之纯 V3.1 面; "
                                 "旧件之 mixed_object=true 系 V3.1 gold × V3 model 之混合构造, "
                                 "本面 model 侧恒 KEYWORDS_V3 且训练面同, ⛔ 本件 0 就其可比性作任何断言",
        },
        "five_lines_new_domain": {
            "A_nw_sim_mean": res["A"]["point"], "A_bootstrap_ci": res["A"]["ci"],
            "A_halfwidth": res["A"]["halfwidth"], "A_fullwidth": res["A"]["fullwidth"],
            "Ap_nled_sim_mean": res["Ap"]["point"], "Ap_bootstrap_ci": res["Ap"]["ci"],
            "Ap_halfwidth": res["Ap"]["halfwidth"], "Ap_fullwidth": res["Ap"]["fullwidth"],
            "B_num_den": res["B"]["num_den"], "B_point": res["B"]["point"],
            "B_ci_construct1": res["B"]["ci_construct1"], "B_ci_construct2": res["B"]["ci_construct2"],
            "B_degenerate_c2": res["B"]["degenerate_construct2"],
            "B_K2_one_sided_lower_c1": res["B"]["K2_one_sided_lower_c1"],
            "B_K2_one_sided_lower_c2": res["B"]["K2_one_sided_lower_c2"],
            "C_num_den": res["C"]["num_den"], "C_point": res["C"]["point"],
            "C_ci_construct1": res["C"]["ci_construct1"], "C_ci_construct2": res["C"]["ci_construct2"],
            "C_degenerate_c2": res["C"]["degenerate_construct2"],
            "C_K2_one_sided_upper_c1": res["C"]["K2_one_sided_upper_c1"],
            "C_K2_one_sided_upper_c2": res["C"]["K2_one_sided_upper_c2"],
            "D_bootstrap_ci": res["D"]["ci"], "D_ci_lower": res["D"]["ci_lower"],
            "D_note": res["D"]["note"],
        },
        "face": {"n_events": res["n_events"], "n_held": res["n_held"],
                 "n_train": res["n_train"], "tree_depth_observed": res["tree_depth_observed"],
                 "empty_gold_seq_items": n_empty, "n_divergent": n_div,
                 "n_critical": n_crit, "n_critical_and_divergent": n_crit_div,
                 "nw_changed_vs_v3_gold": sum(1 for p in res["per_item"] if p["nw_v31"] != p["nw_v3"]),
                 "nled_changed_vs_v3_gold": sum(1 for p in res["per_item"]
                                                if p["nled_v31"] != p["nled_v3"])},
        "per_item": res["per_item"],
        "thresholds_untouched": {
            "TH_NW_SIM_MEAN": ex.TH_NW_SIM_MEAN, "TH_NLED_SIM_MEAN": ex.TH_NLED_SIM_MEAN,
            "TH_CRITICAL_COV": ex.TH_CRITICAL_COV, "TH_BLIND_OBEY": ex.TH_BLIND_OBEY,
            "TH_BOOT_CI_FLOOR": ex.TH_BOOT_CI_FLOOR,
            "note": "沿 8a81d90c69ba 原值, 仅作定位; ⛔ 0 判读 0 比阈值 0 赋任一 k_v3s_4_4_* 布尔",
        },
        "not_run": {
            "veto_axis": "⛔ 0 开跑 (门控未闭 · 卡九仅授权五线面)",
            "trigger_volume": "⛔ 0 开跑 (同上)",
            "verdict": "⛔ 0 判档 (归 verdict-keeper)",
        },
    }
    op = RESULTS / "_s4prime_five_lines_readings_2026_10_11.json"
    op.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print(f"\nwrote {op.name}  sha12={sha12_file(op)}  bytes={op.stat().st_size}")


if __name__ == "__main__":
    main()
