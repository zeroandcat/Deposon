#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S4' 第三构造域 (seed'' · c34835ad59cf) · 读数面实跑 runner
  (worker 面 · PI 2026-10-11 决策卡 `s4_run` = 甲·授权开跑「仅读数面」)

产出 (仅此三项):
  1. pred_model_side  (模型侧预测序列)
  2. nw_v31           (NW-sim, gold=V3.1)
  3. nled_v31         (NLED-sim, gold=V3.1)
再据此按现行生效之 MD 定义式 (5d8cd0d1676f §2) 合成 MD_i = LS_i x TV_i 之全域统计。

⛔ 0 五线 (A/A'/B/C/D) · 0 CI · 0 bootstrap · 0 阈值比较 · 0 判档 · 0 赋任一 k_v3s_4_* 布尔
⛔ 0 宣告 K-RJ-5 闭/开 (归 verdict-keeper / PI) · 0 代裁 · 0 代释条文 · 0 改 n_distinct<=3 阈值
⛔ 0 回改任何既有件

只读复用 (⛔ 0 编辑 / 0 覆写 / 0 就地改 / 0 monkey-patch 任一常量 —— 仅 importlib 只读加载并逐字调用):
  runner   `f784b2fc92f4`  results/_s4prime_five_lines_runner_2026_10_11.py
  executor `8a81d90c69ba`  results/_v4_pi_cot_v3_ruleset_v3_executor.py

自审门 (先行 · 硬停):
  以第二构造域 (3c25e1a2ea94) 跑同一实现 -> 须与在册 65a9b9be6327 之 per_item[] 逐位全等;
  不等 => SystemExit 停手报回 (⛔ 0 续跑第三域)。

⛔ 0 网络 / 0 LLM / 0 API key / 0 读 .env
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import pathlib
import statistics
from typing import Any, Dict, List, Tuple

RESULTS = pathlib.Path(__file__).resolve().parent
REPO = RESULTS.parent

# ---- 只读锚件 (指纹不符即 SystemExit) ----
RUNNER_FIVE = RESULTS / "_s4prime_five_lines_runner_2026_10_11.py"
RUNNER_FIVE_SHA12 = "f784b2fc92f4"
EXECUTOR = RESULTS / "_v4_pi_cot_v3_ruleset_v3_executor.py"
EXECUTOR_SHA12 = "8a81d90c69ba"

HOLDOUT_D1 = RESULTS / "_s4_heldout_sampling_seed42_items_2026_10_09.json"
HOLDOUT_D2 = RESULTS / "_s4_heldout_sampling_seedprime_items_2026_10_10.json"
D2_SHA12 = "6cbb8ba01bfb"
HOLDOUT_D3 = RESULTS / "_s4_heldout_sampling_seedthird_items_2026_10_11.json"
D3_SHA12 = "5777a07c608a"
D3_FP = "c34835ad59cf"
D2_FP = "3c25e1a2ea94"

D2_REGISTERED = RESULTS / "_s4prime_five_lines_readings_2026_10_11.json"
D2_REGISTERED_SHA12 = "65a9b9be6327"

OUT_JSON = RESULTS / "_stage3_trigger_readings_items_2026_10_11.json"

# ---- MD 之 LS 层序位表 (5d8cd0d1676f §2-1 · 照录 1b7bcbcce589 §3.1 行序 · 0 自创 0 重排) ----
LAYER_ORDINAL: Dict[str, int] = {
    "KILL_LINE": 0, "COST": 1, "CRITERIA": 2, "RISK": 3, "TIMING": 4, "DELEGATE": 5,
}


def sha12_file(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def load_ro(path: pathlib.Path, expected: str, label: str):
    """指纹校验后只读 importlib 加载 (⛔ 0 修改磁盘字节 · 0 monkey-patch)。"""
    got = sha12_file(path)
    if got != expected:
        raise SystemExit(f"{label} SHA-12 mismatch: {got} != {expected}")
    spec = importlib.util.spec_from_file_location(f"ro_{label}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def per_item_readings(run, ex, events, keys, held_keys, kw_gold, kw_model) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """逐件读数面 (第二域 runner `run_five_lines` 之逐件循环段逐字复制 · 仅剥离五线/CI 聚合段)。

    机制 0 改动: 特征 12 项 (ex.feats_v3) · 训练标签源 = KEYWORDS_V3 · gold 词表入参 ·
                 决策树 build_tree / predict_tree (含叶子 majority 之 UNKNOWN 空标签兜底) ·
                 nw_sim([pred], seq_gold) / nled_sim([pred], seq_gold) · 遍历序 = held_idx (R1 键序)。
    """
    held_idx = run.held_idx_from(keys, held_keys)
    held_set = set(held_idx)

    rows_all = [ex.feats_v3(ev) for ev in events]
    labels = [ex.primary_judgment_type_v3(
        run.extract_seq(ev.get("reasoning_full", ""), kw_model, ex.PHRASE_PATTERNS_V3, ex))
        for ev in events]

    tr_rows = [rows_all[i] for i in range(len(events)) if i not in held_set]
    tr_lab = [labels[i] for i in range(len(events)) if i not in held_set]
    tree = ex.build_tree(tr_rows, tr_lab)

    per_item: List[Dict[str, Any]] = []
    for i in held_idx:
        ev = events[i]
        pred = ex.predict_tree(tree, rows_all[i])
        rf = ev.get("reasoning_full", "") or ""
        seq_gold = run.extract_seq(rf, kw_gold, ex.PHRASE_PATTERNS_V3, ex)
        seq_v3 = run.extract_seq(rf, kw_model, ex.PHRASE_PATTERNS_V3, ex)
        per_item.append({
            "face_index": i, "key": list(keys[i]), "q_id": ev.get("q_id"),
            "pred": pred, "gold_seq_v31": seq_gold, "gold_seq_v3": seq_v3,
            "nw_v31": ex.nw_sim([pred], seq_gold), "nled_v31": ex.nled_sim([pred], seq_gold),
            "nw_v3": ex.nw_sim([pred], seq_v3), "nled_v3": ex.nled_sim([pred], seq_v3),
            "divergent": bool(pred not in seq_gold),
            "critical": bool(ex.has_critical_reflection_v3(rf)),
            "corpus_len": len(rf),
        })

    meta = {
        "n_events": len(events), "n_held": len(held_idx), "n_train": len(tr_rows),
        "tree_depth_observed": ex._tree_depth(tree),
        "model_side_kwtable": "KEYWORDS_V3",
        "gold_kwtable": "KEYWORDS_V3.1 (= KEYWORDS_V3 (+) 15 词, 1b7bcbcce589 §4)",
    }
    return per_item, meta


def ls_of(seq: List[str]) -> int:
    """LS_i ≡ Σ_{L ∈ seq_v31_i} 2^{idx(L)}  (5d8cd0d1676f §2 定义式 · 0 自创权重)。"""
    return sum(1 << LAYER_ORDINAL[L] for L in seq)


def md_synthesize(per_item: List[Dict[str, Any]]) -> Dict[str, Any]:
    """MD_i ≡ LS_i × TV_i,  TV_i ≡ nw_v31_i − nled_v31_i  (5d8cd0d1676f §2)。"""
    enriched = []
    for it in per_item:
        ls = ls_of(it["gold_seq_v31"])
        tv = it["nw_v31"] - it["nled_v31"]
        enriched.append({**it, "ls_v31": ls, "tv": tv, "md": ls * tv})

    md_vals = [e["md"] for e in enriched]
    ls_vals = [e["ls_v31"] for e in enriched]
    tv_vals = [e["tv"] for e in enriched]

    n = len(md_vals)
    loo = []
    for k in range(n):
        rest = [v for j, v in enumerate(md_vals) if j != k]
        loo.append(len(set(rest)))

    pred_vals = [e["pred"] for e in enriched]

    return {
        "enriched": enriched,
        "md": {
            "n": n,
            "n_distinct": len(set(md_vals)),
            "min": min(md_vals), "max": max(md_vals),
            "mean": statistics.fmean(md_vals),
            "std_population": statistics.pstdev(md_vals),
            "value_domain": sorted(set(md_vals)),
            "leave_one_out_n_distinct": sorted(set(loo)),
            "leave_one_out_min": min(loo), "leave_one_out_max": max(loo),
            "n_zero_items": sum(1 for v in md_vals if v == 0),
            "zero_item_q_ids": [e["q_id"] for e in enriched if e["md"] == 0],
            "zero_item_structural_ls0": [e["q_id"] for e in enriched
                                         if e["ls_v31"] == 0],
        },
        "ls_layer": {
            "n_distinct": len(set(ls_vals)), "min": min(ls_vals), "max": max(ls_vals),
            "mean": statistics.fmean(ls_vals), "std_population": statistics.pstdev(ls_vals),
            "value_domain": sorted(set(ls_vals)),
            "frequency": {str(v): ls_vals.count(v) for v in sorted(set(ls_vals))},
        },
        "tv_layer": {
            "n_distinct": len(set(tv_vals)), "min": min(tv_vals), "max": max(tv_vals),
            "mean": statistics.fmean(tv_vals), "std_population": statistics.pstdev(tv_vals),
            "value_domain": sorted(set(tv_vals)),
            "frequency": {repr(v): tv_vals.count(v) for v in sorted(set(tv_vals))},
        },
        "pred_model_side_field": {
            "n_distinct": len(set(pred_vals)),
            "value_domain": sorted(set(pred_vals)),
            "frequency": {v: pred_vals.count(v) for v in sorted(set(pred_vals))},
            "n_empty_gold_seq": sum(1 for e in enriched if not e["gold_seq_v31"]),
            "n_divergent": sum(1 for e in enriched if e["divergent"]),
        },
    }


def main() -> None:
    print("=== ANCHORS (read-only) ===")
    anchors = {
        "runner_five_lines": (RUNNER_FIVE, RUNNER_FIVE_SHA12),
        "executor": (EXECUTOR, EXECUTOR_SHA12),
        "heldout_d2_seedprime": (HOLDOUT_D2, D2_SHA12),
        "heldout_d3_seedthird": (HOLDOUT_D3, D3_SHA12),
        "d2_registered_readings": (D2_REGISTERED, D2_REGISTERED_SHA12),
    }
    for name, (p, exp) in anchors.items():
        got = sha12_file(p)
        ok = got == exp
        print(f"  {name:24s} {got}  expect={exp}  {'OK' if ok else 'MISMATCH'}")
        if not ok:
            raise SystemExit(f"anchor mismatch: {name}")

    run = load_ro(RUNNER_FIVE, RUNNER_FIVE_SHA12, "runner")
    ex = load_ro(EXECUTOR, EXECUTOR_SHA12, "executor")
    kw31 = run.build_kwtable_v31(ex)

    # 面: 21 件 R1 字节序 x 件内 idx 升序 (三集共用同一 S4 冻结面, 沿 runner main() 之取法)
    d1 = json.loads(HOLDOUT_D1.read_text(encoding="utf-8"))
    r1_files = d1["domain"]["r1_byte_sorted_files"]
    events, keys = run.build_face(ex, r1_files)
    print(f"\n=== FACE (steps 1-6, 沿 runner) ===\n  rows={len(events)} files={len(r1_files)}")

    g = run.grid_domain_selfproof(events, ex)
    expect = {"occupied_cells": 54, "empty_cells": 74, "sum_floor_0.30n": 26,
              "cells_n_ge_4": 16, "cells_n_le_3": 38, "cells_n_eq_1": 16,
              "n_min": 1, "n_max": 16, "n_sum": 179, "b0_occupied_cells": 43,
              "b1_occupied_cells": 11, "b1_rows": 15, "grid_total": 128, "n_events": 179}
    print("\n=== GRID SELF-PROOF (13 items) ===")
    for k, v in expect.items():
        print(f"  {k:22s} {g[k]:>6}  registered={v:>6}  "
              f"{'OK' if g[k] == v else 'MISMATCH'}")
    if g != expect:
        raise SystemExit("grid self-proof mismatch")

    # ================= 自审门: 第二构造域逐位复现 =================
    d2 = json.loads(HOLDOUT_D2.read_text(encoding="utf-8"))
    d2_keys = [(it["file"], it["idx"]) for it in d2["heldout_items"]]
    concat2 = "|".join(f"{f}#{i}" for f, i in d2_keys)
    fp2 = hashlib.sha256(concat2.encode("utf-8")).hexdigest()

    print("\n=== SELF-AUDIT: 第二构造域 (3c25e1a2ea94) 逐件复现 ===")
    print(f"  fingerprint recomputed={fp2[:12]} expect={D2_FP} "
          f"match={fp2[:12] == D2_FP}")
    if fp2[:12] != D2_FP:
        raise SystemExit("d2 fingerprint mismatch")

    d2_mine, d2_meta = per_item_readings(run, ex, events, keys, d2_keys, kw31, ex.KEYWORDS_V3)
    d2_reg = json.loads(D2_REGISTERED.read_text(encoding="utf-8"))["per_item"]

    if len(d2_mine) != len(d2_reg):
        raise SystemExit(f"d2 self-audit length mismatch {len(d2_mine)} != {len(d2_reg)}")

    diffs = []
    for i, (mine, theirs) in enumerate(zip(d2_mine, d2_reg)):
        for f in ("face_index", "key", "q_id", "pred", "gold_seq_v31", "gold_seq_v3",
                  "nw_v31", "nled_v31", "nw_v3", "nled_v3",
                  "divergent", "critical", "corpus_len"):
            if mine[f] != theirs[f]:
                diffs.append((i, f, mine[f], theirs[f]))
    print(f"  n_items={len(d2_mine)}  field-level diffs={len(diffs)}")
    if diffs:
        for d in diffs[:20]:
            print(f"    DIFF idx={d[0]} field={d[1]} mine={d[2]!r} registered={d[3]!r}")
        raise SystemExit(f"SELF-AUDIT FAILED: {len(diffs)} field mismatch vs 65a9b9be6327")
    print("  => SELF-AUDIT PASS: 26/26 items, 13 fields each, BIT-IDENTICAL")

    # ================= 第三构造域读数面实跑 =================
    d3 = json.loads(HOLDOUT_D3.read_text(encoding="utf-8"))
    d3_keys = [(it["file"], it["idx"]) for it in d3["heldout_items"]]
    concat3 = "|".join(f"{f}#{i}" for f, i in d3_keys)
    fp3 = hashlib.sha256(concat3.encode("utf-8")).hexdigest()
    print("\n=== HELD-OUT FINGERPRINT (第三构造域) ===")
    print(f"  recomputed={fp3[:12]}  expect={D3_FP}  match={fp3[:12] == D3_FP}")
    print(f"  n={len(d3_keys)}  all keys resolve in face="
          f"{all(k in set(keys) for k in d3_keys)}")
    if fp3[:12] != D3_FP:
        raise SystemExit("d3 fingerprint mismatch")

    d3_items, d3_meta = per_item_readings(run, ex, events, keys, d3_keys, kw31, ex.KEYWORDS_V3)
    print(f"  n_held={d3_meta['n_held']} n_train={d3_meta['n_train']} "
          f"tree_depth={d3_meta['tree_depth_observed']}")

    # 与机器源 5777a07c608a 逐件交叉核对 (seq_v31 / q_id)
    src = {(it["file"], it["src_idx"]): it for it in d3["movable_items"]["items"]}
    xcheck_bad = []
    for it in d3_items:
        s = src.get((it["key"][0], it["key"][1]))
        if s is None:
            xcheck_bad.append((it["key"], "NOT_FOUND"))
            continue
        if list(s["seq_v31"]) != list(it["gold_seq_v31"]):
            xcheck_bad.append((it["key"], "seq_v31", s["seq_v31"], it["gold_seq_v31"]))
        if s["q_id_resolved"] != it["q_id"]:
            xcheck_bad.append((it["key"], "q_id", s["q_id_resolved"], it["q_id"]))
    print(f"  cross-check vs 5777a07c608a (seq_v31/q_id): "
          f"{len(d3_items) - len({x[0] for x in xcheck_bad})}/{len(d3_items)} ok")
    for x in xcheck_bad[:10]:
        print(f"    XCHECK DIFF {x}")
    if xcheck_bad:
        raise SystemExit(f"d3 cross-check failed: {len(xcheck_bad)}")

    md3 = md_synthesize(d3_items)
    md2 = md_synthesize(d2_mine)

    print("\n=== MD 全域统计 (MD_i = LS_i x TV_i) ===")
    for label, s, m in (("第二域 3c25e1a2ea94", md2, d2_meta), ("第三域 c34835ad59cf", md3, d3_meta)):
        mdd = s["md"]
        print(f"  [{label}] n={mdd['n']} n_distinct={mdd['n_distinct']} "
              f"min={mdd['min']!r} max={mdd['max']!r} "
              f"std_pop={mdd['std_population']!r}")
        print(f"      value_domain={mdd['value_domain']}")
        print(f"      leave_one_out_n_distinct={mdd['leave_one_out_n_distinct']} "
              f"(min {mdd['leave_one_out_min']})")
        print(f"      n_zero_items={mdd['n_zero_items']}  "
              f"n_distinct<=3 ? {mdd['n_distinct'] <= 3}")
        print(f"      LS: n_distinct={s['ls_layer']['n_distinct']} "
              f"min={s['ls_layer']['min']} max={s['ls_layer']['max']} "
              f"std_pop={s['ls_layer']['std_population']!r}")
        print(f"      TV: n_distinct={s['tv_layer']['n_distinct']} "
              f"min={s['tv_layer']['min']!r} max={s['tv_layer']['max']!r}")
        print(f"      pred_model_side: n_distinct={s['pred_model_side_field']['n_distinct']} "
              f"domain={s['pred_model_side_field']['value_domain']}")

    # 与在册 LS 读数 (aef26b8cbe50 §4-1) 交叉核对
    reg_ls = {"n_distinct": 12, "min": 0, "max": 48,
              "mean": 12.5384615384615, "std_population": 14.3559978599961,
              "value_domain": [0, 4, 8, 12, 13, 16, 24, 27, 32, 40, 46, 48],
              "frequency": {"0": 7, "4": 4, "8": 5, "12": 2, "13": 1, "16": 1,
                            "24": 1, "27": 1, "32": 1, "40": 1, "46": 1, "48": 1}}
    reg_zero7 = ["Q49", "DF6-1", "D8-07", "D8-35", "D8-76", "SQ-08", "DF6-4"]
    got_ls = md3["ls_layer"]
    # 离散量逐位全等; 连续量 (mean/std) 因在册件系 14 位有效数字之显示值, 改以相对容差对勘
    ls_discrete_ok = (got_ls["n_distinct"] == reg_ls["n_distinct"]
                      and got_ls["min"] == reg_ls["min"]
                      and got_ls["max"] == reg_ls["max"]
                      and got_ls["value_domain"] == reg_ls["value_domain"]
                      and got_ls["frequency"] == reg_ls["frequency"])
    rel = lambda a, b: abs(a - b) / abs(b) if b else abs(a - b)
    ls_mean_rel = rel(got_ls["mean"], reg_ls["mean"])
    ls_std_rel = rel(got_ls["std_population"], reg_ls["std_population"])
    ls_cont_ok = ls_mean_rel < 1e-12 and ls_std_rel < 1e-12
    ls_ok = ls_discrete_ok and ls_cont_ok
    zero7_ok = md3["md"]["zero_item_structural_ls0"] == reg_zero7
    print("\n=== CROSS-CHECK vs 在册 LS 读数 (aef26b8cbe50 §4-1 / §4-2) ===")
    print(f"  LS 离散量 (n_distinct/min/max/取值域/频次) 逐位全等: {ls_discrete_ok}")
    print(f"  LS 连续量 mean  rel_diff={ls_mean_rel:.3e} (<1e-12) -> {ls_mean_rel < 1e-12}")
    print(f"  LS 连续量 std   rel_diff={ls_std_rel:.3e} (<1e-12) -> {ls_std_rel < 1e-12}")
    print(f"    (在册件之 mean/std 系 14 位有效数字之显示值: "
          f"reg={reg_ls['mean']!r}/{reg_ls['std_population']!r} vs "
          f"mine={got_ls['mean']!r}/{got_ls['std_population']!r})")
    print(f"  LS≡0 的 7 件 q_id 列表与在册逐位全等: {zero7_ok}")
    if not zero7_ok:
        print(f"    mine={md3['md']['zero_item_structural_ls0']}")
        print(f"    reg ={reg_zero7}")
    if not ls_ok:
        print(f"    mine={got_ls}")
        print(f"    reg ={reg_ls}")
        raise SystemExit("LS cross-check vs aef26b8cbe50 failed")

    # 对照: 在册 MD 静态读数 (5d8cd0d1676f §2-4, 域=3c25e1a2ea94) vs 本棒对第二域之复算
    reg_md_d2 = {"n_distinct": 8, "min": 0.0, "max": 16.0,
                 "loo_min": 7, "n_items": 26}
    md2d = md2["md"]
    md_d2_ok = (md2d["n_distinct"] == reg_md_d2["n_distinct"]
                and md2d["min"] == reg_md_d2["min"]
                and md2d["max"] == reg_md_d2["max"]
                and md2d["leave_one_out_min"] == reg_md_d2["loo_min"])
    print("\n=== CROSS-CHECK vs 在册 MD 静态读数 (5d8cd0d1676f §2-4 · 域 3c25e1a2ea94) ===")
    print(f"  mine  n_distinct={md2d['n_distinct']} min={md2d['min']!r} "
          f"max={md2d['max']!r} loo_min={md2d['leave_one_out_min']}")
    print(f"  reg   n_distinct={reg_md_d2['n_distinct']} min={reg_md_d2['min']!r} "
          f"max={reg_md_d2['max']!r} loo_min={reg_md_d2['loo_min']}")
    print(f"  => 逐位全等: {md_d2_ok}")

    out = {
        "artifact": OUT_JSON.name,
        "date": "2026-10-11",
        "kind": "per_item_readings",
        "step": "S4' 第三构造域 (seed'') 读数面实跑 (worker 面 · 卡 s4_run=甲·仅读数面)",
        "note": "逐件读数 JSON; ⛔ 0 与任何汇总合并 (沿 K-RJ-11 / K-EX-10 同族); "
                "⛔ 0 判档; ⛔ 0 赋任一 k_v3s_4_* 布尔; ⛔ 0 宣告 K-RJ-5 闭/开",
        "authority": {
            "pi_decision_card": {"item": "s4_run", "answer": "甲·授权开跑 (仅读数面)",
                                 "date": "2026-10-11"},
            "md_definition": {"file": "results/_md_trigger_prereg_effectivity_2026_10_11.md",
                              "sha12": "5d8cd0d1676f"},
            "stage3_trigger_recheck": {"file": "results/_stage3_trigger_recheck_2026_10_11.md",
                                       "sha12": "aef26b8cbe50"},
            "heldout_d3_register": {"file": "results/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md",
                                    "sha12": "784f042bf93d"},
            "heldout_d3_items": {"file": HOLDOUT_D3.name, "sha12": D3_SHA12},
            "runner_five_lines_readonly": {"file": RUNNER_FIVE.name, "sha12": RUNNER_FIVE_SHA12},
            "executor_readonly": {"file": EXECUTOR.name, "sha12": EXECUTOR_SHA12},
            "kwtable_v31": {"file": "results/_s4_v31_keyword_table_final_2026_10_10.md",
                            "sha12": "1b7bcbcce589"},
            "krj5_judgement_scope": {"file": "results/_s3prime_alert_disposition_judgment_2026_10_11.md",
                                     "sha12": "e7fcbc290a7e"},
        },
        "runtime": {"python": "3.14.7", "numpy": "2.5.3", "network": 0, "endpoint_calls": 0,
                    "api_key": 0, "skill": 0, "llm": 0, "env_read": 0},
        "face_selfproof_grid13": {"measured": g, "registered": expect, "all_match": g == expect},
        "selfcert_domain2": {
            "purpose": "以同一实现于第二构造域重算, 与在册 65a9b9be6327 之 per_item[] 逐位比对; "
                       "系管道同源性自证, ⛔ 非新旧读数面之比较, ⛔ 0 并表 0 比大小",
            "fingerprint": fp2[:12], "n_items": len(d2_mine),
            "fields_compared": 13, "diffs": 0, "result": "BIT_IDENTICAL",
        },
        "heldout_fingerprint": {
            "sha12_recomputed": fp3[:12], "full_sha256_recomputed": fp3,
            "sha12_registered": d3["reproduction"]["heldout_ordered_fingerprint"]["sha12"],
            "match": fp3[:12] == D3_FP, "n": len(d3_keys),
        },
        "crosscheck_vs_5777a07c608a": {
            "fields": ["seq_v31", "q_id"], "n_items": len(d3_items), "diffs": 0,
        },
        "crosscheck_LS_vs_aef26b8cbe50": {
            "discrete_bit_identical": ls_discrete_ok,
            "continuous_reldiff_mean": ls_mean_rel, "continuous_reldiff_std": ls_std_rel,
            "continuous_within_1e-12": ls_cont_ok,
            "zero7_qids_bit_identical": zero7_ok,
            "note": "在册件之 mean/std 系 14 位有效数字之显示值; 离散量 (n_distinct/min/max/"
                    "取值域/频次) 逐位全等, 连续量相对差 < 1e-12",
        },
        "crosscheck_MD_vs_5d8cd0d1676f": {
            "note": "在册 §2-4 之 MD 静态 n_distinct=8 (留一 7 · min 0.0 · max 16.0) 系域 3c25e1a2ea94; "
                    "本棒以自审门逐位复现之第二域逐件读数独立复算, 对勘之",
            "mine": {"n_distinct": md2d["n_distinct"], "min": md2d["min"],
                     "max": md2d["max"], "leave_one_out_min": md2d["leave_one_out_min"]},
            "registered": reg_md_d2, "bit_identical": md_d2_ok,
        },
        "model_side_declaration": {
            "gold_kwtable": "KEYWORDS_V3.1 (= KEYWORDS_V3 (+) 15 词, 1b7bcbcce589 §4)",
            "model_tree": "V3", "training_label_kwtable": "KEYWORDS_V3",
            "n_keywords_hit_feature_kwtable": "KEYWORDS_V3",
            "unknown_fallback": "predict_tree 叶子 = majority(labels); "
                                "primary_judgment_type_v3 空序列 -> 'UNKNOWN' (ex L522-L529, L691-L694)",
            "mixed_object": True,
            "note": "gold 侧 V3.1 × model 侧 V3 之混合构造 (沿 e91e7f52c726 同族); "
                    "⛔ 本件 0 就其可比性作任何断言",
        },
        "domain3": {"meta": d3_meta, "per_item": md3["enriched"],
                    "md": md3["md"], "ls_layer": md3["ls_layer"],
                    "tv_layer": md3["tv_layer"],
                    "pred_model_side_field": md3["pred_model_side_field"]},
        "domain2_reference": {
            "note": "仅供对照 · ⛔ 0 混用 0 直接比大小 (fd4ec7559342 §5); "
                    "由自审门逐位复现之逐件读数派生",
            "meta": d2_meta, "md": md2["md"], "ls_layer": md2["ls_layer"],
            "tv_layer": md2["tv_layer"],
            "pred_model_side_field": md2["pred_model_side_field"],
        },
        "thresholds_untouched": {
            "TH_NW_SIM_MEAN": ex.TH_NW_SIM_MEAN, "TH_NLED_SIM_MEAN": ex.TH_NLED_SIM_MEAN,
            "TH_CRITICAL_COV": ex.TH_CRITICAL_COV, "TH_BLIND_OBEY": ex.TH_BLIND_OBEY,
            "TH_BOOT_CI_FLOOR": ex.TH_BOOT_CI_FLOOR,
            "note": "沿 8a81d90c69ba 原值, 仅作定位; ⛔ 0 判读 0 比阈值",
        },
        "not_run": {
            "five_lines_A_Ap_B_C_D": "⛔ 0 出 (卡 s4_run 仅授权读数面)",
            "CI_bootstrap": "⛔ 0 出 (同上)",
            "KRJ5_verdict": "⛔ 0 宣告闭/开 (归 verdict-keeper / PI)",
            "threshold_alert_judgement": "⛔ 0 判 (归 verdict-keeper)",
            "any_upstream_edit": "⛔ 0 回改 (全部锚件 0 编辑 0 覆写)",
        },
    }
    OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                        encoding="utf-8", newline="\n")
    print(f"\nwrote {OUT_JSON.name}  sha12={sha12_file(OUT_JSON)}  "
          f"bytes={OUT_JSON.stat().st_size}")


if __name__ == "__main__":
    main()
