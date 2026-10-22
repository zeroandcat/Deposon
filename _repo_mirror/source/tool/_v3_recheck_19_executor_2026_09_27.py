#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V3-R v1.1 追加补审 #19 BOSS-PG-1 velocity 敏感性扫描 — executor (worker · 2026-09-27)

沿 results/_v3_recheck_prereg_v1p1_2026_09_27.md（实测 SHA-12 bcc3cee23e82）字面执行：
  - K-V3R1P1-0-A 防退化门（n_distinct > 3 + std > 0；退化杠杆 v=(0,0) 事前登记，禁作扫描变量）
  - K-V3R1P1-0-B 沿用阈值（0 新设；判带沿 boss_pg_1 97fede6c8a4e 的 0.01 / 0.10 字面）
  - K-V3R1P1-0-C 双口径（#19 强制 raw / r6 双记；判带用 raw；边界歧义节点双带并报）
  - K-V3R1P1-0-D 派生 JSON 不合并（本件独立落盘 _v3_recheck_19_result_*.json）
  - K-V3R1P1-0-E 0 LLM（纯 numpy / json / math，0 网络 0 模型调用）
  - K-V3R-19 网格（构造面，非阈值）：v = (v_T, v_A)，v_T, v_A ∈ {−0.10,−0.08,…,+0.10}（步长 0.02，11×11 = 121 节点）
  - K-V3R-19 判带：median < 0.01 → FAIL；median ∈ [0.01, 0.10) → GRAY；median ≥ 0.10 → PASS
  - K-V3R-19 退化节点处置（测量前冻结）：v=(0,0) 单列为结构性退化节点，0 计入 120 节点非退化集
  - K-V3R-19 判死线三档：(a) 存在 GRAY 区/边界 → 敏感如实登记（不改原 GRAY）；(b) 120 节点全一致 → 排除；
                                    (c) 不可跑/退化/歧义无法双判 → 不明 + γ
  - TH-V3R1P1-19-a/b/c：C_TRUE_HYPERBOLIC=1.0 / C_NEAR_EUCLIDEAN=0.001 / max_norm_ball=0.95 / n_models=9
  - as-run 节点 (0.08, −0.02) 作 bit 级复现对照

输入（全部只读）：
  - results/deposon_pg_v01_9m60c_2026_09_15.json（9 model 的 T_frac60 / A_frac60）
  - deposon_team/plugins/_v3n_pg_boss_live_2026_09_27.py（实现面，只读 0 改动，仅参数化 v）
  - deposon_team/plugins/boss_pg_1_riemannian_degenerate.py（判带阈值字面，只读）
  - results/_v3_n_pg_boss_live_data_2026_09_27.json（as-run 读数，作 bit 级对照）

S-40 布尔显式命名：`*_hit = True` 表示「触发 FAIL / 触发警报」；`*_pass = True` 表示「存活 / 合格」。
"""

import hashlib
import json
import math
import os
import statistics
import sys
from pathlib import Path

import numpy as np

# ---- K-V3R-19 网格（构造面，冻后 0 擅调）----
GRID = [-0.10, -0.08, -0.06, -0.04, -0.02, 0.00, 0.02, 0.04, 0.06, 0.08, 0.10]
AS_RUN_V = (0.08, -0.02)
DEGENERATE_NODE = (0.0, 0.0)        # 测量前冻结：结构性退化节点，0 计入 120 节点非退化集

# ---- TH-V3R1P1-19-a/b/c（沿 boss_pg_1 既有字面，0 新设）----
C_TRUE_HYPERBOLIC = 1.0
C_NEAR_EUCLIDEAN = 0.001
POINCARE_BALL_EPSILON = 1e-12
NORM_CLIP = 1e-9
MAX_NORM_BALL = 0.95
DEG_GRAY = 0.01       # TH-V3R1P1-19-a
DEG_PASS = 0.10       # TH-V3R1P1-19-a
R6_DIGITS = 6         # K-V3R1P1-0-C：r6 = round(raw, 6)，沿 b6040d34f0ac 字面
SEED = 20260927


def _repo_root() -> Path:
    starts = [Path(os.getcwd()), Path(os.path.abspath(sys.argv[0])).parent]
    for base in starts:
        p = base
        for _ in range(6):
            if (p / "results/_v3_recheck_prereg_v1p1_2026_09_27.md").exists():
                return p
            p = p.parent
    raise SystemExit("repo root not found (cwd=%s)" % os.getcwd())


REPO = _repo_root()
PREREG = REPO / "results/_v3_recheck_prereg_v1p1_2026_09_27.md"
PG_JSON = REPO / "results/deposon_pg_v01_9m60c_2026_09_15.json"
IMPL = REPO / "deposon_team/plugins/_v3n_pg_boss_live_2026_09_27.py"
THR_SRC = REPO / "deposon_team/plugins/boss_pg_1_riemannian_degenerate.py"
ASRUN = REPO / "results/_v3_n_pg_boss_live_data_2026_09_27.json"
OUT = REPO / "results/_v3_recheck_19_result_2026_09_27.json"


def sha12(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:12]


def n_distinct(xs) -> int:
    return len(set(round(float(x), 12) for x in xs))


def stat_block(xs):
    a = np.asarray(xs, dtype=float)
    return {"n": int(a.size), "n_distinct": n_distinct(a), "std": float(a.std(ddof=0)),
            "min": float(a.min()), "max": float(a.max()), "mean": float(a.mean())}


# ============ Poincare ball（逐字沿 b6040d34f0ac L65-108，只参数化 v）============
def project_to_ball(x, max_norm=MAX_NORM_BALL):
    x = np.asarray(x, dtype=np.float64)
    n = float(np.linalg.norm(x))
    if n < POINCARE_BALL_EPSILON:
        return x
    return x * (max_norm / n) if n >= max_norm else x


def exp_0(v, c=1.0):
    v = np.asarray(v, dtype=np.float64)
    n = float(np.linalg.norm(v))
    if n < POINCARE_BALL_EPSILON:
        return np.zeros_like(v)
    sc = math.sqrt(c)
    return math.tanh(sc * n) * v / (sc * n)


def log_0(x, c=1.0):
    x = np.asarray(x, dtype=np.float64)
    n = float(np.linalg.norm(x))
    if n < POINCARE_BALL_EPSILON:
        return np.zeros_like(x)
    sc = math.sqrt(c)
    n_clip = min(sc * n, 1.0 - NORM_CLIP)
    return math.atanh(n_clip) * x / (sc * n)


def poincare_transport(x, v, c=1.0):
    return exp_0(log_0(x, c) + np.asarray(v, dtype=np.float64), c)


def band(median: float) -> str:
    """判带沿 boss_pg_1 字面：< 0.01 FAIL / [0.01, 0.10) GRAY / >= 0.10 PASS"""
    if median < DEG_GRAY:
        return "FAIL"
    return "GRAY" if median < DEG_PASS else "PASS"


def median_delta_at(points, v):
    deltas = []
    for r in points:
        x = project_to_ball([r["T_frac60"], r["A_frac60"]])
        d = float(np.linalg.norm(poincare_transport(x, v, c=C_TRUE_HYPERBOLIC)
                                 - poincare_transport(x, v, c=C_NEAR_EUCLIDEAN)))
        deltas.append(d)
    return float(statistics.median(deltas)), deltas


def connected_gray_components(gray_flags):
    """4-邻接连通分量（退化节点视为不可穿越孔洞）。返回按 size 降序的分量列表"""
    n = len(GRID)
    seen = [[False] * n for _ in range(n)]
    comps = []
    for i in range(n):
        for j in range(n):
            if seen[i][j] or not gray_flags[i][j] or (GRID[i], GRID[j]) == DEGENERATE_NODE:
                continue
            stack, comp = [(i, j)], []
            seen[i][j] = True
            while stack:
                a, b = stack.pop()
                comp.append((a, b))
                for da, db in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    p, q = a + da, b + db
                    if 0 <= p < n and 0 <= q < n and not seen[p][q] and gray_flags[p][q] \
                            and (GRID[p], GRID[q]) != DEGENERATE_NODE:
                        seen[p][q] = True
                        stack.append((p, q))
            comps.append(sorted(comp))
    return sorted(comps, key=len, reverse=True)


def main() -> int:
    pg = json.loads(PG_JSON.read_text(encoding="utf-8"))
    asrun = json.loads(ASRUN.read_text(encoding="utf-8")) if ASRUN.exists() else None
    prereg_sha12 = sha12(PREREG.read_bytes())
    points = pg["P_G_hyperbolic_transport"]["per_model"]
    assert len(points) == 9, "9 model 预期, 实得 %d" % len(points)

    # ---------- 盘上输入字段：K-V3R1P1-0-A 防退化门自证（跑前） ----------
    t60 = [r["T_frac60"] for r in points]
    a60 = [r["A_frac60"] for r in points]
    dH = [r["d_H_to_canonical"] for r in points]
    input_selfcheck = {
        "pg_v01_T_frac60 (9 model, 盘上真实)": stat_block(t60),
        "pg_v01_A_frac60 (9 model, 盘上真实)": stat_block(a60),
        "pg_v01_d_H_to_canonical (9 model, 盘上真实)": stat_block(dH),
        "velocity_grid (11x11 构造面)": stat_block(GRID),
    }
    gate_fields = list(input_selfcheck)
    gate_pass = {k: bool(input_selfcheck[k]["n_distinct"] > 3 and input_selfcheck[k]["std"] > 0)
                 for k in gate_fields}
    degen_alarm_hit = not all(gate_pass.values())

    # ---------- 逐节点扫描（121 节点）----------
    nodes, gray_flags = [], [[False] * len(GRID) for _ in GRID]
    for i, vT in enumerate(GRID):
        for j, vA in enumerate(GRID):
            med, deltas = median_delta_at(points, (vT, vA))
            r6 = round(med, R6_DIGITS)
            b_raw, b_r6 = band(med), band(r6)
            is_degen = (vT, vA) == DEGENERATE_NODE
            if not is_degen and b_raw == "GRAY":
                gray_flags[i][j] = True
            nodes.append({
                "v_T": vT, "v_A": vA, "in_120_non_degenerate_set": not is_degen,
                "structurally_degenerate_node": is_degen,
                "median_delta_raw": med,
                "median_delta_r6": r6,
                "band_raw": b_raw, "band_r6": b_r6,
                "band_ambiguous": bool(b_raw != b_r6),
                "min_delta": min(deltas), "max_delta": max(deltas),
                "n_distinct_per_model_delta": n_distinct(deltas),
            })
    n_nodes = len(nodes)
    nondegen = [x for x in nodes if x["in_120_non_degenerate_set"]]
    degen_nodes = [x for x in nodes if not x["in_120_non_degenerate_set"]]
    ambiguous = [x for x in nondegen if x["band_ambiguous"]]

    nondegen_med = [x["median_delta_raw"] for x in nondegen]
    nd_stat = stat_block(nondegen_med)
    node_gate_pass = bool(nd_stat["n_distinct"] > 3 and nd_stat["std"] > 0)

    # as-run 节点 bit 级对照
    asrun_node = [x for x in nodes if (x["v_T"], x["v_A"]) == AS_RUN_V][0]
    asrun_recorded = None
    if asrun:
        asrun_recorded = asrun["BOSS_PG_1_riemannian_degenerate"]["median_delta"]
    asrun_bit_match = bool(asrun_recorded is not None
                           and abs(asrun_node["median_delta_raw"] - asrun_recorded) < 5e-7)

    # 网格分带统计
    band_counts = {}
    for b in ("FAIL", "GRAY", "PASS"):
        band_counts[b] = sum(1 for x in nondegen if x["band_raw"] == b)
    all_same_band = bool(len(set(x["band_raw"] for x in nondegen)) == 1)

    # GRAY 连通区 / 边界
    comps = connected_gray_components(gray_flags)
    gray_components = [{"size": len(c),
                        "v_T_range": [min(GRID[a] for a, _ in c), max(GRID[a] for a, _ in c)],
                        "v_A_range": [min(GRID[b] for _, b in c), max(GRID[b] for _, b in c)],
                        "cells_sample": [[GRID[a], GRID[b]] for a, b in c[:8]]}
                       for c in comps]
    # 边界歧义：非退化集中 raw 与 r6 判带不一致者
    dual_band_nodes = [{"v_T": x["v_T"], "v_A": x["v_A"],
                        "median_delta_raw": x["median_delta_raw"],
                        "median_delta_r6": x["median_delta_r6"],
                        "band_raw": x["band_raw"], "band_r6": x["band_r6"]}
                       for x in ambiguous]

    # ---------- K-V3R-19 判死线（三档）----------
    gray_zone_exists = bool(comps)
    band_varies = bool(not all_same_band)
    dual_judgeable = True  # 歧义节点按 K-V3R1P1-0-C 双带并报即可判
    c_condition = bool(degen_alarm_hit or not node_gate_pass)

    if c_condition:
        kill_line_hit, kill_line_pass = True, False
        new_verdict = "不明"
        gamma = ("输入面或非退化节点集防退化门不达（input_gate=%s / node_gate=%s）"
                 % (not degen_alarm_hit, node_gate_pass))
        branch = "c"
    elif gray_zone_exists and band_varies:
        kill_line_hit, kill_line_pass = False, True
        new_verdict = "GRAY 对 velocity 敏感（K-V3R-19 判死线 (a)）"
        gamma = None
        branch = "a"
    elif all_same_band:
        kill_line_hit, kill_line_pass = False, True
        new_verdict = "敏感性排除（K-V3R-19 判死线 (b)）"
        gamma = None
        branch = "b"
    else:
        kill_line_hit, kill_line_pass = True, False
        new_verdict = "不明"
        gamma = "既无 GRAY 连通区，又非全一致，且防退化门通过 -> 三档均不命中"
        branch = "c"

    # ---------- 双口径并报（K-V3R1P1-0-C）----------
    legacy_verdict = ("GRAY（median_delta = %s ∈ [0.01, 0.10)，as-run 节点 v = (0.08, −0.02)）"
                      % asrun_recorded)

    result = {
        "schema": "v3_recheck_result/19_boss_pg1_velocity_sensitivity/1",
        "prereg": {"path": "results/_v3_recheck_prereg_v1p1_2026_09_27.md", "sha12": prereg_sha12,
                   "kill_line": "K-V3R-19",
                   "thresholds": ["TH-V3R1P1-19-a (0.01 / 0.10)", "TH-V3R1P1-19-b (c=1.0 / c=0.001, eps 1e-12)",
                                  "TH-V3R1P1-19-c (max_norm_ball 0.95, canonical_idx 1, n_models 9)"]},
        "executor": "results/_v3_recheck_19_executor_2026_09_27.py",
        "date": "2026-09-27", "seed": SEED,
        "runtime": "0 LLM; numpy + json + math only; no network; read-only inputs; 仅参数化 v，实现面 0 改动",
        "inputs": [
            {"path": "results/deposon_pg_v01_9m60c_2026_09_15.json", "sha12_measured": sha12(PG_JSON.read_bytes())},
            {"path": "deposon_team/plugins/_v3n_pg_boss_live_2026_09_27.py", "sha12_measured": sha12(IMPL.read_bytes())},
            {"path": "deposon_team/plugins/boss_pg_1_riemannian_degenerate.py", "sha12_measured": sha12(THR_SRC.read_bytes())},
            {"path": "results/_v3_n_pg_boss_live_data_2026_09_27.json",
             "sha12_measured": sha12(ASRUN.read_bytes()) if ASRUN.exists() else None},
        ],
        "construct": {
            "grid": GRID, "grid_shape": [len(GRID), len(GRID)], "n_nodes_total": n_nodes,
            "n_nodes_non_degenerate": len(nondegen),
            "degenerate_node": {"v": list(DEGENERATE_NODE),
                                "handling": "测量前冻结：单列为结构性退化节点，0 计入 120 节点非退化集；"
                                            "其 FAIL 不得计为 velocity 敏感性证据"},
            "as_run_node": {"v": list(AS_RUN_V), "median_delta_raw": asrun_node["median_delta_raw"],
                            "recorded_in_as_run_json": asrun_recorded,
                            "bit_level_match": asrun_bit_match},
            "metric": "median over 9 model of ||Exp_0^{c=1}(Log_0^{c=1}(x)+v) − Exp_0^{c=0.001}(Log_0^{c=0.001}(x)+v)||_2",
            "band_rule": "median < 0.01 FAIL / [0.01, 0.10) GRAY / >= 0.10 PASS（沿 97fede6c8a4e 字面）",
            "dual_track": "raw = float64 未 round（判带用 raw）；r6 = round(raw, 6)（沿 b6040d34f0ac 字面）；"
                          "两口径不一致者 = 边界歧义节点，双带并报",
        },
        "construct_degen_self_check": {
            "gate": "K-V3R1P1-0-A: n_distinct > 3 + std > 0 on input fields and on the 120 non-degenerate nodes",
            "input_fields": input_selfcheck,
            "gate_per_field": gate_pass,
            "degenerate_alarm_hit": degen_alarm_hit,
            "input_gate_pass": not degen_alarm_hit,
            "non_degenerate_node_field": nd_stat,
            "node_gate_pass": node_gate_pass,
            "degenerate_lever_preregistered": True,
            "degenerate_lever_verified": bool(
                degen_nodes
                and all(abs(x["median_delta_raw"]) < 1e-15 and x["band_raw"] == "FAIL"
                        and x["band_r6"] == "FAIL" for x in degen_nodes)),
            "degenerate_lever_measured": {
                "median_delta_raw": degen_nodes[0]["median_delta_raw"] if degen_nodes else None,
                "median_delta_r6": degen_nodes[0]["median_delta_r6"] if degen_nodes else None,
                "max_abs_per_model_delta": max((max(abs(x["min_delta"]), abs(x["max_delta"]))
                                                for x in degen_nodes), default=None),
                "band_raw": degen_nodes[0]["band_raw"] if degen_nodes else None,
                "band_r6": degen_nodes[0]["band_r6"] if degen_nodes else None,
            },
            "degenerate_lever_note": "v=(0,0) 沿实现字面两侧同式恒等 => delta ≡ 0。实测：raw 中位数 = "
                                     "5.551115123125783e-17，9 model 单点 delta 最大 2.220446049250313e-16"
                                     "（IEEE-754 双精度舍入极限 2^-52），r6 口径 = 0.0；raw/r6 双判带均为 FAIL，"
                                     "与预登记 §1.3 事前登记「必 FAIL」一致（raw 侧非严格 0.0 而是舍入极限，"
                                     "本件如实登记，不改预登记字面）",
        },
        "band_statistics_non_degenerate_120": {
            "band_counts_raw": band_counts,
            "all_same_band": all_same_band,
            "band_varies_with_v": band_varies,
            "median_delta_stat": nd_stat,
            "n_ambiguous_boundary_nodes": len(ambiguous),
            "dual_band_nodes": dual_band_nodes,
            "dual_judgeable": dual_judgeable,
        },
        "gray_zone": {
            "n_connected_components": len(comps),
            "largest_component_size": len(comps[0]) if comps else 0,
            "components": gray_components,
            "gray_exists": gray_zone_exists,
        },
        "nodes": nodes,
        "legacy_dual_track": {
            "legacy_verdict": legacy_verdict,
            "legacy_median_delta": asrun_recorded,
            "legacy_node": list(AS_RUN_V),
            "legacy_source": "results/_v3_n_pg_boss_live_data_2026_09_27.json "
                             "§BOSS_PG_1_riemannian_degenerate（as-run 节点）",
        },
        "verdict": {
            "new_verdict": new_verdict,
            "kill_line_branch": branch,
            "kill_line_pass": kill_line_pass,
            "kill_line_hit": kill_line_hit,
            "legacy_verdict": legacy_verdict,
            "一致性": "本扫描不构成对原 GRAY 的翻案（沿 K-V3R-19 (a) 字面「不改原 GRAY」）",
            "gamma": gamma,
            "改判档位": ("v1 §2.3 第 2 行形态：维持原 V3 标注（GRAY 不动）+ 显式登记新构造读数"
                         "（velocity 敏感性），0 改判动作" if branch == "a"
                         else ("v1 §2.3 第 3 行形态：维持原标注，0 改判动作" if branch == "b"
                               else "v1 §2.3 第 4 行：维持原标注 + 显式登记 γ + 归「V4 收尾整理」待拍板桶")),
        },
        "iron_rules": {
            "0_LLM": True, "no_proxy": True, "no_key_in_prompt_json_disk": True,
            "read_only_inputs": True, "derived_json_not_merged": True,
            "implementation_face_unchanged": True, "v3_original_report_bytes_untouched": True,
        },
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("[#19] written:", OUT.relative_to(REPO))
    print("[#19] nodes=%d non_degenerate=%d band_counts=%s all_same_band=%s"
          % (n_nodes, len(nondegen), band_counts, all_same_band))
    print("[#19] gray components=%d largest=%d ambiguous_boundary_nodes=%d"
          % (len(comps), len(comps[0]) if comps else 0, len(ambiguous)))
    print("[#19] as-run bit match=%s (raw=%.6f recorded=%s)"
          % (asrun_bit_match, asrun_node["median_delta_raw"], asrun_recorded))
    print("[#19] gates: input=%s node=%s degen_lever_verified=%s"
          % (not degen_alarm_hit, node_gate_pass,
             result["construct_degen_self_check"]["degenerate_lever_verified"]))
    print("[#19] branch=%s -> %s (pass=%s hit=%s)" % (branch, new_verdict, kill_line_pass, kill_line_hit))
    return 0


if __name__ == "__main__":
    sys.exit(main())
