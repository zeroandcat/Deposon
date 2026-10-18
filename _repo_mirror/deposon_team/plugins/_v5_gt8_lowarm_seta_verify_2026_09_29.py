# -*- coding: utf-8 -*-
"""set A（并发棒 mvs_cb132cd536f648299c713abf2071d026 产出）· **只读核验面** · worker · 2026-09-29

  → results/_v5_gt8_lowarm_seta_verify_2026_09_29.json   （新名核验件，0 覆写、0 合并）

背景：本路径 executor 上发生并发写者碰撞（详见
`deposon_team/plugins/_v5_gt8_lowarm_2026_09_29.py` 头部登记）。set A 的读数件
`results/_v5_gt8_lowarm_result_2026_09_29.json` 落盘完整，但**其源码已被覆盖丢失**
⇒ 无法重跑自证。本件按派工单「有则**核**后接续 · 0 假定」对 set A 做**只读核验**：

可核部分（set A 自身落盘字段 + 可确定性重建的构造）：
  - set A 的两条**低臂**结构由 (N, k) 唯一决定（平衡 k 叉树 · S2 口径）⇒ 可重建；
    重建后以 recorded seed 重算协议读数 ⇒ 与 set A 记录值**逐位比对**（决定性证据：
    命中全边留一协议的全命中模式，非偶然可复现）。
  - set A 的机械计数（#conc / #rev / #tie）、读数级去重数、撞值分组、5 个防退化门
    ⇒ 全部可由 set A 自身落盘的 per_graph / per_pair **纯算术复算**。

不可核部分（如实登记，0 补造）：
  - set A 两条**高臂**的边集 0 落盘（源码丢失）⇒ 其 sha256、读数、hub_concentration
    **无法独立复算**；本件 0 猜测重建、0 编造校验和。

0 改任何既有件（全部只读 open/json.load）｜0 覆写 set A｜0 新测量面（重算沿既有协议，
只为核验，0 产生新对数）｜0 新设阈值｜0 代 verdict-keeper 裁档｜0 读 key。
"""
from __future__ import annotations

import hashlib
import json
import os
import sys

REPO = r"D:/私人资料/deposon-repo"
RESULTS_REL = "results"
SET_A = f"{RESULTS_REL}/_v5_gt8_lowarm_result_2026_09_29.json"
SET_B = f"{RESULTS_REL}/_v5_gt8_lowarm_resultb_2026_09_29.json"
OUT = f"{RESULTS_REL}/_v5_gt8_lowarm_seta_verify_2026_09_29.json"

sys.path.insert(0, REPO)

import numpy as np  # noqa: E402

from deposon_diffusion import DiffusionConfig  # noqa: E402
from mindmap_corpus_v20 import (_assign_labels, is_dag,  # noqa: E402
                                longest_path_family)
from run_v20_gt8 import eval_graph, hub_concentration  # noqa: E402


def sha12(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def read_json(rel: str):
    with open(os.path.join(REPO, rel.replace("/", os.sep)), encoding="utf-8") as f:
        return json.load(f)


def write_json(rel: str, obj) -> dict:
    p = os.path.join(REPO, rel.replace("/", os.sep))
    b = json.dumps(obj, ensure_ascii=False, indent=1).encode("utf-8")
    with open(p, "wb") as f:
        f.write(b)
    return {"path": rel, "sha12": hashlib.sha256(b).hexdigest()[:12],
            "bytes": len(b)}


def balanced_k_ary(N: int, k: int, graph_id: str, seed: int):
    """平衡 k 叉树（S2 口径）· 与既有 C_low / D_low 同一构造式
    （parent=(i−1)//k；named = {k·v+1 < N} 的父子边）· 边集由 (N, k) 唯一决定。"""
    edges = sorted({((i - 1) // k, i) for i in range(1, N)})
    named = sorted({(u, v) for (u, v) in edges if k * v + 1 < N})
    assert is_dag(N, edges)
    _nl, _L, src, tgt = longest_path_family(N, edges)
    return {"graph_id": graph_id, "family": "S", "N": N,
            "nodes": list(range(N)), "labels": _assign_labels(N, seed),
            "edges": [list(e) for e in edges],
            "named_edges": [list(e) for e in named],
            "filler_edges": [list(e) for e in sorted(set(edges) - set(named))],
            "source": int(src), "target": int(tgt), "seed": int(seed)}


def anti_degeneration_gate(values):
    vals = [float(v) for v in values]
    nd = len(set(vals))
    sd = float(np.std(vals)) if vals else 0.0
    ok = bool(nd > 3 and sd > 0.0)
    return {"n_values": len(vals), "n_distinct": nd, "std": sd,
            "gate_n_distinct_gt_3": nd > 3, "gate_std_gt_0": sd > 0.0,
            "gate_pass": ok,
            "state_candidate": "PASS" if ok else "KD",
            "kd_reason": None if ok else
            "K-V5R3-0-B ③ 防退化门不达（n_distinct≤3 或 std=0）"}


def main() -> int:
    a = read_json(SET_A)
    a_pg, a_pp = a["per_graph"], a["per_pair"]
    cfg = DiffusionConfig()

    # ---- 1. 可重建部分：set A 两条低臂（N,k 由其落盘 n_named 唯一反解并交叉验证）----
    # n_named = floor((N−2)/k)；对 (N=33, n_named=10) ⇒ k=3； (N=59, n_named=14) ⇒ k=4
    recon = {}
    for gid, k in (("GT8_E_low", 3), ("GT8_F_low", 4)):
        rec = a_pg[gid]
        g = balanced_k_ary(rec["N"], k, gid, rec["seed"])
        arms = eval_graph(g, cfg)
        diff = arms["field_mean"]["named"] - arms["random"]["named"]
        edges = [tuple(e) for e in g["edges"]]
        recon[gid] = {
            "reconstructed_from": f"N={rec['N']}, k={k}（平衡 k 叉树 · S2 口径）",
            "seed": rec["seed"],
            "n_named_rebuilt": len(g["named_edges"]),
            "n_named_recorded": rec["n_named"],
            "n_named_match": bool(len(g["named_edges"]) == rec["n_named"]),
            "n_filler_rebuilt": len(g["filler_edges"]),
            "n_filler_recorded": rec["n_filler"],
            "source_target_match": bool(int(g["source"]) == rec["source"]
                                       and int(g["target"]) == rec["target"]),
            "hub_concentration_recomputed": hub_concentration(g["N"], edges),
            "hub_concentration_recorded": rec["features"]["hub_concentration"],
            "hub_concentration_bit_identical":
                bool(hub_concentration(g["N"], edges)
                     == rec["features"]["hub_concentration"]),
            "field_named_recomputed": arms["field_mean"]["named"],
            "field_named_recorded": rec["field_named"],
            "field_named_bit_identical":
                bool(arms["field_mean"]["named"] == rec["field_named"]),
            "random_named_bit_identical":
                bool(arms["random"]["named"] == rec["random_named"]),
            "degree_named_bit_identical":
                bool(arms["degree"]["named"] == rec["degree_named"]),
            "diff_fm_rand_recomputed": diff,
            "diff_fm_rand_recorded": rec["diff_fm_rand"],
            "diff_fm_rand_bit_identical": bool(diff == rec["diff_fm_rand"]),
            "all_readings_bit_identical": bool(
                arms["field_mean"]["named"] == rec["field_named"]
                and arms["random"]["named"] == rec["random_named"]
                and arms["degree"]["named"] == rec["degree_named"]
                and diff == rec["diff_fm_rand"]),
        }
    low_all_ok = bool(all(v["all_readings_bit_identical"] and v["n_named_match"]
                           for v in recon.values()))

    # ---- 2. 不可核部分：两条高臂 ----
    unverifiable = {}
    for gid in ("GT8_E_high", "GT8_F_high"):
        rec = a_pg[gid]
        unverifiable[gid] = {
            "recorded_sha256": rec["sha256"],
            "recorded_diff_fm_rand": rec["diff_fm_rand"],
            "recorded_hub_concentration": rec["features"]["hub_concentration"],
            "reason_unverifiable": ("set A 源码已丢失 ⇒ 边集未落盘 ⇒ 0 独立重建、"
                                    "0 复算 sha256/读数；本件 0 猜测构造、0 编造校验"),
            "internal_consistency_only": {
                "diff_equals_field_minus_random": bool(
                    rec["diff_fm_rand"]
                    == rec["field_named"] - rec["random_named"]),
                "n_named_plus_filler_equals_n_edges": bool(
                    rec["n_named"] + rec["n_filler"] == rec["n_edges"]),
                "hub_equals_max_indeg_over_n_edges_recorded": rec[
                    "features"]["hub_concentration"],
            },
        }

    # ---- 3. 机械计数 / 去重 / 撞值 / 门 的纯算术复算 ----
    def attrib(sub):
        return {"n_pairs": len(sub),
                "n_concordant": sum(1 for p in sub if p["concordant"]),
                "n_reversed": sum(1 for p in sub
                                  if p["diff_high"] < p["diff_low"]),
                "n_tied": sum(1 for p in sub
                              if p["diff_high"] == p["diff_low"])}

    low_order = [p["low"] for p in a_pp]
    low_vals = [a_pg[g]["diff_fm_rand"] for g in low_order]
    buckets = {}
    for g, v in zip(low_order, low_vals):
        buckets.setdefault(v, []).append(g)
    recomputed_gates = {
        "new_2_pairs_diff_fm_rand": anti_degeneration_gate(
            [a_pg[g]["diff_fm_rand"] for g in ("GT8_E_high", "GT8_E_low",
                                               "GT8_F_high", "GT8_F_low")]),
        "new_2_pairs_hub_concentration": anti_degeneration_gate(
            [a_pg[g]["features"]["hub_concentration"]
             for g in ("GT8_E_high", "GT8_E_low", "GT8_F_high", "GT8_F_low")]),
        "all_6_pairs_diff_fm_rand": anti_degeneration_gate(
            [a_pg[g]["diff_fm_rand"] for p in a_pp for g in (p["high"], p["low"])]),
        "all_6_pairs_hub_concentration": anti_degeneration_gate(
            [a_pg[g]["features"]["hub_concentration"] for p in a_pp for g in (p["high"], p["low"])]),
        "all_6_pairs_diff_low_only": anti_degeneration_gate(low_vals),
    }
    gate_match = {}
    for k, rec in recomputed_gates.items():
        disk = (a.get("anti_degeneration_gates_new_surface") or {}).get(k, {})
        gate_match[k] = {
            "recomputed": rec, "disk": {kk: disk.get(kk) for kk in
                                        ("n_values", "n_distinct", "std",
                                         "gate_pass")},
            "matches_disk": bool(
                rec["n_distinct"] == disk.get("n_distinct")
                and rec["gate_pass"] == disk.get("gate_pass")
                and rec["std"] == disk.get("std")),
        }
    att_sub = a.get("subset_attribution_mechanical") or {}
    recomputed_attrib = {
        "all": attrib(a_pp),
        "new_2": attrib([p for p in a_pp if p["origin"] == "p10_lowarm_new"]),
        "as_run_2": attrib([p for p in a_pp if p["origin"] == "as_run"]),
        "expansion_2": attrib([p for p in a_pp if p["origin"] == "v5_expansion"]),
    }

    # ---- 4. 与 set B 的并排（只读，0 选边）----
    b_parallel = None
    if os.path.exists(os.path.join(REPO, SET_B.replace("/", os.sep))):
        b = read_json(SET_B)
        b_pg = b["per_graph"]
        b_low = {p["low"]: b_pg[p["low"]]["diff_fm_rand"] for p in b["per_pair"]}
        b_att = b.get("tristate_readings_for_verdict_keeper", [])
        b_parallel = {
            "sha12": sha12(os.path.join(REPO, SET_B.replace("/", os.sep))),
            "case": b.get("case"),
            "n_pairs": len(b["per_pair"]),
            "low_arm_diff_fm_rand": b_low,
            "n_distinct_diff_low_all": len(set(b_low.values())),
            "new_low_arm_n_named": {g: b_pg[g]["n_named"]
                                    for g in ("GT8_E_low", "GT8_F_low")},
            "attribution_counts": {t["subset"]: t["counts"] for t in b_att
                                   if t["subset"] in
                                   ("new_pairs_2", "all_pairs_6")},
            "agreement_on_concordance": bool(
                all(p["concordant"] for p in a_pp) == all(
                    p["concordant"] for p in b["per_pair"])),
            "note": ("两套为同面两次**独立写死**的构造（低臂 k 与高臂构型不同）；"
                     "**0 由执行面择一为准**（裁定归 verdict-keeper / PI）"),
        }

    out = {
        "case": "gt8_p10_lowarm_seta_readonly_verification",
        "purpose": ("派工单「上一棒已落产物 ⇒ 先盘上核验、无则重产、有则核后接续」"
                    "之**核**环节；对 set A 只读核验，0 覆写、0 合并、0 改任何既有件"),
        "verify_of": {"path": SET_A, "sha12": sha12(os.path.join(REPO,
                                                                SET_A.replace("/", os.sep))),
                      "produced_by": a.get("produced_by")},
        "source_status": "**set A 源码已丢失**（并发写者碰撞时被本棒写入覆盖）",
        "verifiable_low_arms": recon,
        "all_low_arm_readings_bit_identical": low_all_ok,
        "unverifiable_high_arms": unverifiable,
        "recomputed_mechanical": {
            "attribution": recomputed_attrib,
            "attribution_disk": att_sub,
            "diff_low_values": {g: v for g, v in zip(low_order, low_vals)},
            "n_distinct_diff_low_all": len(set(low_vals)),
            "n_distinct_diff_low_existing_4": len(
                {a_pg[p["low"]]["diff_fm_rand"] for p in a_pp
                 if p["origin"] != "p10_lowarm_new"}),
            "collision_groups": {str(v): gs for v, gs in buckets.items()
                                 if len(gs) > 1},
            "gates_recomputed_vs_disk": gate_match,
            "all_gates_match_disk": bool(all(v["matches_disk"]
                                             for v in gate_match.values())),
            "all_attribution_match_disk": bool(
                recomputed_attrib["all"]["n_concordant"]
                == (att_sub.get("全部对池") or att_sub.get("all_6_pairs", {})
                    ).get("n_concordant")
                if att_sub else None),
        },
        "material_finding_for_verdict_keeper": (
            "⚠️ set A 新面 hub_concentration 门：n_distinct = 3 ≤ 3 ⇒ **门不达** ⇒ "
            "按 K-V5R3-0-B ③ 该面落 **KD** 面（根因：set A 两条高臂的 "
            "hub_concentration 同为 0.5 ⇒ 4 值序列只有 3 个互异值）。"
            "**该 KD 候选的裁定归 verdict-keeper，本棒 0 代裁。**"),
        "set_b_parallel": b_parallel,
        "discipline": {
            "read_only_on_existing": True,
            "no_overwrite_of_set_a": True,
            "no_new_measurement_surface": ("重算沿既有协议、0 新增对数、0 改判据；"
                                           "0 猜测 set A 高臂构造"),
            "no_new_thresholds": 0,
            "adjudication_owner": "verdict-keeper",
            "worker_predetermined_state": False,
            "key_read": 0,
            "llm_api": 0,
        },
        "author": {"role": "worker",
                   "session": "mvs_02eb4a5ab8024f439c31147529aaf7d4",
                   "note": "0 冒充 verdict-keeper / protocol-keeper / evidence-auditor / "
                           "doc-writer / PI / 并发棒会话"},
        "self_sha_note": "本件 SHA-12 0 自写入（避免自指悖论）⇒ 由交付回执自报盘上实测值",
    }
    written = write_json(OUT, out)
    print(json.dumps({"written": written,
                      "all_low_arm_readings_bit_identical": low_all_ok,
                      "unverifiable": list(unverifiable),
                      "all_gates_match_disk": out["recomputed_mechanical"]
                      ["all_gates_match_disk"],
                      "gate_recomputed": {k: (v["recomputed"]["n_distinct"],
                                              v["recomputed"]["gate_pass"])
                                          for k, v in gate_match.items()},
                      "recomputed_attrib": recomputed_attrib,
                      "attribution_disk_keys": list(att_sub.keys())},
                     ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
