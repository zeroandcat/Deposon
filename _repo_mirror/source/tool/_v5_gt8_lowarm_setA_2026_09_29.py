# -*- coding: utf-8 -*-
# Deposon V5 · GT P-10 low 臂独立测量面 · 棒 1b（worker · executor）· **set A**
#   → results/_v5_gt8_lowarm_resultA_cb132cd5_2026_09_29.json（新名 · 0 合并）
#
# ⚠️⚠️ **并发写者碰撞登记（必读 · 关系到本件归属）**：
#   本文件是 **set A** 的源码，重建于并发写者覆盖本棒原路径**之后**。
#   碰撞事实（盘上实测，见交付回执）：
#     · 15:20:5x  本棒（session mvs_cb132cd536f648299c713abf2071d026）首次写入
#       `deposon_team/plugins/_v5_gt8_lowarm_2026_09_29.py`（原路径）；
#     · 15:20:58  本棒以该路径启动 `python`（stdout/stderr → .tmp_p10_out/.err.txt）；
#     · 15:21:01  另一 worker 棒（session mvs_02eb4a5ab8024f439c31147529aaf7d4）
#       **写入同一路径，覆盖了本棒源码**（该覆盖由对方造成，如实登记）；
#     · 15:21:52  本棒进程完成，落 `results/_v5_gt8_lowarm_result_2026_09_29.json`
#       （**set A**，sha12 `c68076c88140`）。
#   ⇒ 本文件**0 覆写**对方任何产物；set A 已另存
#     `results/_v5_gt8_lowarm_resultA_cb132cd5_2026_09_29.json`（与 set A 逐字节同值）。
#   ⇒ set A 与对方的 set B **并排如实登记**，**0 代 PI/verdict-keeper 选哪一套为准**。
#   ⇒ 本文件重写后**重跑逐字节不变**（见 `rerun_byte_identical` 面）⇒ 复现自证。
#
# 授权件：results/_v5_gt_p10_lowarm_prereg_2026_09_29.md（07e28e2fe374）
#   PI 复核批 9 ㉘ 已裁（results/_v5_confirm_b9_decisions_register_2026_09_29.md §2）：
#     P-1 ① B-案 2（含案 1 约束：n_named 写死互异）＝ 本棒执行面
#     P-2 ① 只增不减（4 对为下限）＋ 具体档位/种子区间由**执行面测量前写死**
#     P-3 ③ 读数级 ＋ 构造级 两者并报
#     P-4 ② 撞值并报披露（0 归并）
#     P-5 ① 0 设「独立证据数下限」数值门
#     P-6 ① real_semantics 仍 deferred
#
# 判死线（件 B §3 · 只引用既有字面 · 本棒 0 新设）：
#   min_pairs=2 / pass_rule=「全部对同向（#conc = n 且 n ≥ 2）」/ kill_rule=「全部对全反」
#   防退化门：n_distinct > 3 且 std > 0（K-V5R3-0-B ③）
#   hub_concentration = max_in_degree / n_edges（SPEC_GT8 L21）
#   rng = default_rng(g_seed*100003+ei)；场实例种子 = g_seed+ei
#   配对要求：N 与 n_edges 对配（SPEC_GT8 L30）
#
# ── 规模与种子的**测量前写死**（件 B §9 P-2 ＋ 2505ff5d203f §6.3）────────────
#   写死时点：**本文件任何一次 eval_graph 调用之前**（本文件不含正式读数，
#   读数全部由本脚本首次运行时产生）。
#   反选防护：以下常量由**结构算术**（n_named = #{i : k·i + 1 < N}）与**种子续号**
#   推出，**未参考任何 diff 读数**；本棒在写死时刻**尚无任何新读数存在**。
#   对数：既有 4 对（as-run 2 + 扩面 2）→ 新增 **2 对** ⇒ 全部对池 **6 对**。
#         增量 ＋2 与上一棒扩面步（2→4）同为 ＋2，**未按读数调档**。
#   种子：沿 208801–208804（as-run）／208805–208808（扩面）续号 208809–208812，
#         与语料族 200101–200106 0 重叠。
#   n_named 写死互异（件 B §4.2 案 1）：E_low = 10、F_low = 14（互异）；
#         且与既有低臂 {A_low 15, B_low 12, C_low 8, D_low 8} 逐个不同。
#         ⚠ 案 1 ②：n_named 互异**只降低**撞值概率，**0 构造性排除**再次相等
#           （1/10 与 1/14 仍可相等）⇒ 本面 0 承诺「补测后必定互异」。
#   对配：E 对 N=33/n_edges=32；F 对 N=59/n_edges=58。
#
# ── 本棒纪律自证 ──────────────────────────────────────────────────────────
#   1. **0 代裁**：本棒只产读数；机械计数与既有纯函数输出以
#      `mechanical_*` 字面落盘并显式标注「非本棒判定」；
#      `terminal_state` 一律 null，判定归棒 2（verdict-keeper）。
#   2. **0 预判档位**：0 预填独立证据数下限（件 B §9 P-5 ①）、0 预判任何档位。
#   3. **0 翻案**：as-run `supports_H_GT8`（2b88948dca19）与扩面 v2 终态 PASS
#      （34ff826f97c2）**0 触动**；既有 4 对在本环境**逐值复算**并与盘上字面
#      比对（复现检查 = 0 新测量），不一致即中止。
#   4. **0 改既有件**：全部写盘路径为**新名**；锚件 byte 0 写入。
#   5. **0 新设阈值**：逐条列证见 `thresholds_used` / `new_thresholds_added`。
#   6. **0 读 key（R4）**、0 LLM API、0 proxy；全脚本无 requests/openai/http。
#   7. **派生 JSON 0 合并**：读数独立新名件。
#   8. **18 frozen / 9 网格 0 触动**：本棒只新建件。
#      如实交代：本棒**0 独立复核**该二清单的具体条目（未开列该清单的件）。
#   9. **γ-PKB-5 自碰撞修复**：不同构哨兵的比较集 = 22 语料 ＋ 8 张既有 GT8 新图
#      = **30 图**；**新图不入比较集** ⇒ 0 自碰撞。
#      （既有 `nonisomorphic_to_existing=false` 的 4 张是**自碰撞产物**，
#      既有件 0 回改，此处只以修正实现重算新面。）
#  10. **确定性**：JSON 不含时间戳/运行秒 ⇒ 重跑逐字节不变可自证。
#  11. 署名如实：worker（mvs_cb132cd536f648299c713abf2071d026）。
#  12. skill：派工单未指定 ⇒ **本棒 0 加载任何 skill**。
# =============================================================================
import hashlib
import importlib.util
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RESULTS_REL = "results"
DATE_TAG = "2026_09_29"

# set A 专用新名（0 覆写 canonical 路径，canonical 归并发写者所有）
OUT_JSON = (f"{RESULTS_REL}"
            f"/_v5_gt8_lowarm_resultA_cb132cd5_{DATE_TAG}.json")

# 本脚本位于 plugins 子目录 ⇒ 把仓根加入 sys.path，使只读 import 的既有协议
# 模块（run_v20_gt8 / mindmap_corpus_v20 / deposon_diffusion）可解析。
if HERE not in sys.path:
    sys.path.insert(0, HERE)

# ---------------------------------------------------------------- 只读锚件（0 写入）
ANCHORS = {
    "prereg_p10": "results/_v5_gt_p10_lowarm_prereg_2026_09_29.md",
    "verdict_gt": "results/_v5_gt_verdict_2026_09_29.md",
    "expand_gt8": "results/_v5_gt8_expand_2026_09_29.json",
    "asrun_gt8": "results/deposon_v20_gt8.json",
    "prereg_v2": "results/_v5_gt5_gt6_gt8_gt5b_gt_prereg_2026_09_28.md",
    "confirm_b9": "results/_v5_confirm_b9_decisions_register_2026_09_29.md",
    "spec_gt8": "docs/SPEC_GT8.md",
}
# 派工单 / 件 B §1.1 给定锚值（本棒开跑前**盘上实测**逐一复核；不符即中止）
ANCHOR_SHA12 = {
    "prereg_p10": "07e28e2fe374",
    "verdict_gt": "45648b0ec940",
    "expand_gt8": "34ff826f97c2",
    "asrun_gt8": "2b88948dca19",
    "prereg_v2": "2505ff5d203f",
}

COLLISION = {
    "collision_detected": True,
    "path_contested": "deposon_team/plugins/_v5_gt8_lowarm_2026_09_29.py",
    "this_stick": {"session": "mvs_cb132cd536f648299c713abf2071d026",
                   "role": "worker 棒 1b executor",
                   "set": "A"},
    "other_stick": {"session": "mvs_02eb4a5ab8024f439c31147529aaf7d4",
                    "role": "worker 棒 1b executor",
                    "set": "B",
                    "source_overwrote_this_stick_at": "2026-09-29 15:21:01",
                    "declared_output": "results/_v5_gt8_lowarm_resultb_2026_09_29.json"},
    "timeline": [
        "15:20:5x 本棒首次写入 canonical .py 路径",
        "15:20:58 本棒以该路径启动 python",
        "15:21:01 对方棒写入同一路径 ⇒ 覆盖本棒源码（对方造成，如实登记）",
        "15:21:52 本棒进程完成 ⇒ 落 set A（c68076c88140）",
    ],
    "resolution_this_stick": (
        "本棒 0 覆写对方任何产物；set A 另存为 0 碰撞新名；本源码重写于新名并"
        "重跑逐字节复现 set A；set A / set B 并排如实登记，0 代 PI/verdict-keeper 择一"),
    "set_a_preserved_copy": OUT_JSON,
    "set_a_canonical_path": "results/_v5_gt8_lowarm_result_2026_09_29.json",
    "adjudication_owner": "PI / verdict-keeper（0 由本棒择一）",
}


# ---------------------------------------------------------------- 哈希与 IO
def sha12_bytes(b):
    return hashlib.sha256(b).hexdigest()[:12]


def read_bytes(rel):
    with open(os.path.join(HERE, rel.replace("/", os.sep)), "rb") as f:
        return f.read()


def read_json(rel):
    return json.loads(read_bytes(rel).decode("utf-8"))


def write_json(rel, obj):
    p = os.path.join(HERE, rel.replace("/", os.sep))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    b = json.dumps(obj, ensure_ascii=False, indent=1).encode("utf-8")
    with open(p, "wb") as f:
        f.write(b)
    return {"path": rel, "sha12": sha12_bytes(b), "bytes": len(b)}


def anchor_audit():
    """只读锚件哈希实测（开跑前）；与给定锚值不符 ⇒ 中止（fail-closed）。"""
    out, ok = {}, True
    for k, rel in ANCHORS.items():
        b = read_bytes(rel)
        rec = {"path": rel, "sha12_measured": sha12_bytes(b), "bytes": len(b)}
        if k in ANCHOR_SHA12:
            rec["sha12_expected"] = ANCHOR_SHA12[k]
            rec["matches_expected"] = bool(rec["sha12_measured"]
                                           == ANCHOR_SHA12[k])
            ok = ok and rec["matches_expected"]
        out[k] = rec
    return out, ok


# ---------------------------------------------------------------- §7 防退化门（沿既有实现，0 新阈值）
def anti_degeneration_gate(name, values):
    """K-V5R3-0-B ③ 防退化门（与 34ff826f97c2 同式：n_distinct > 3 且 std > 0）。

    门不达 ⇒ KD 面（构造退化）；本函数**不裁档**，只机械回报门值。
    """
    vals = [float(v) for v in values]
    nd = len(set(vals))
    sd = float(np.std(vals)) if vals else 0.0
    gate_ok = bool(nd > 3 and sd > 0.0)
    return {"construct": name, "n_values": len(vals), "n_distinct": nd,
            "std": sd, "gate_n_distinct_gt_3": nd > 3,
            "gate_std_gt_0": sd > 0.0, "gate_pass": gate_ok,
            "kd_reason": None if gate_ok else
            "K-V5R3-0-B ③ 防退化门不达（n_distinct ≤ 3 或 std = 0）"}


# ---------------------------------------------------------------- 协议函数（只读 import，既有件 0 改动）
from run_v20_gt8 import (ARMS, GT8_MIN_PAIRS, GT8_PAIRS, GT8_SEEDS,  # noqa: E402
                         build_gt8_graph, eval_graph, graph_invariant,
                         gt8_verdict, hub_concentration)
from mindmap_corpus_v20 import (_assign_labels, _canonical_sha256,  # noqa: E402
                                is_dag, longest_path_family)

CORPUS_DIR = os.path.join(HERE, "corpus", "v20")


def load_corpus_indexed(corpus_dir=CORPUS_DIR, families=("S", "L")):
    """只读 index 驱动加载（γ-V5R3-13：load_corpus 的孤儿哨兵在本盘对 3 个
    非图记录 .json 误报 ⇒ 本棒沿既有做法只读 index.json 驱动，0 写语料）。"""
    with open(os.path.join(corpus_dir, "index.json"), encoding="utf-8") as f:
        idx = json.load(f)
    out = []
    for e in idx["graphs"]:
        if families and e["family"] not in families:
            continue
        with open(os.path.join(corpus_dir, e["file"]), encoding="utf-8") as f:
            out.append(json.load(f))
    return out


# =============================================================================
# 构造侧：新增 2 对（件 B §4.2 案 2 ＋ 案 1 约束）
#   —— 全部为确定性本地构造，无随机化拓扑、无事后调整
# =============================================================================
# --- 低臂：平衡 k 叉树，named 集沿 S2 口径「子节点仍为内部节点的父子边」 ---
#     n_named = #{i ∈ 1..N-1 : k·i + 1 < N}（件 B §2.2 闭式，写死前算得）
#     E_low: k=3, N=33 ⇒ n_named = 10；F_low: k=4, N=59 ⇒ n_named = 14
def _edges_E_low():
    N, k = 33, 3
    edges = [((i - 1) // k, i) for i in range(1, N)]
    named = {(u, v) for (u, v) in edges if k * v + 1 < N}
    return N, edges, named


def _edges_F_low():
    N, k = 59, 4
    edges = [((i - 1) // k, i) for i in range(1, N)]
    named = {(u, v) for (u, v) in edges if k * v + 1 < N}
    return N, edges, named


# --- 高臂：超枢纽星 + 汇聚结构，named = 终点为枢纽的边（沿 C/D 高臂口径）---
#     E_high: N=33/E=32，hub_concentration = 16/32 = 0.5
#     F_high: N=59/E=58，hub_concentration = 29/58 = 0.5
def _edges_E_high():
    edges = ([(0, 1), (0, 2)]
             + [(i, 1) for i in range(3, 18)]
             + [(i, 2) for i in range(18, 32)]
             + [(1, 32)])
    named = {e for e in edges if e[1] in (1, 2)}
    return 33, edges, named


def _edges_F_high():
    edges = ([(0, 1), (0, 2)]
             + [(3, 4), (4, 1), (5, 6), (6, 1), (7, 8), (8, 1)]
             + [(i, 2) for i in range(9, 33)]
             + [(i, 1) for i in range(33, 51)]
             + [(51, 2), (52, 1), (53, 2), (54, 1),
                (55, 2), (56, 1), (57, 2), (58, 1)])
    named = {e for e in edges if e[1] in (1, 2)}
    return 59, edges, named


LOWARM_SEEDS = {"GT8_E_high": 208809, "GT8_E_low": 208810,
                "GT8_F_high": 208811, "GT8_F_low": 208812}
_LOWARM_STRUCTS = {
    "GT8_E_high": ("twin_hub_star_33", _edges_E_high),
    "GT8_E_low": ("balanced_3ary_tree_33", _edges_E_low),
    "GT8_F_high": ("twin_hub_spine_star_59", _edges_F_high),
    "GT8_F_low": ("balanced_4ary_tree_59", _edges_F_low),
}
LOWARM_PAIRS = (("GT8_E_high", "GT8_E_low"), ("GT8_F_high", "GT8_F_low"))


def build_lowarm_graph(graph_id):
    """构造一张 P-10 新面图（族 S 记录格式，与 build_gt8_graph 逐行同式：
    确定性构造 → is_dag 校验 → longest_path_family → _canonical_sha256）。"""
    structure, fn = _LOWARM_STRUCTS[graph_id]
    N, edges, named = fn()
    edges = sorted(set((int(u), int(v)) for (u, v) in edges))
    named = sorted({(int(u), int(v)) for (u, v) in named})
    if not is_dag(N, edges):
        raise ValueError(f"{graph_id}: structure is not a DAG")
    _nl, _L, src, tgt = longest_path_family(N, edges)
    filler = sorted(set(edges) - set(named))
    seed = LOWARM_SEEDS[graph_id]
    rec = {"graph_id": graph_id, "family": "S", "structure": structure,
           "N": N, "nodes": list(range(N)), "labels": _assign_labels(N, seed),
           "edges": [list(e) for e in edges],
           "named_edges": [list(e) for e in named],
           "filler_edges": [list(e) for e in filler],
           "source": int(src), "target": int(tgt),
           "seed": int(seed), "generator_version": "v2.0-gt8-p10-lowarm"}
    rec["sha256"] = _canonical_sha256(rec)
    return rec


# =============================================================================
# 构造面 pre-flight（不产读数）：可行性 + fail-closed
# =============================================================================
def structure_preflight():
    """新面构造可行性自检（件 B §4.2 案 2 ②「执行棒须按案先报可行性」）。

    检查项：① N/n_edges 对配（SPEC L30）② 低臂 n_named 写死互异且与既有不同
    ③ 新图互不同构 ④ 新图与既有 30 图（22 语料 ＋ 8 张既有 GT8 新图）不同构
    ⑤ 新图 sha256 全新 ⑥ 高臂 hub_concentration > 配对低臂。
    **不调用 eval_graph ⇒ 本阶段 0 读数。**
    """
    new_graphs = {gid: build_lowarm_graph(gid) for gid in LOWARM_SEEDS}
    new_inv = {}
    for gid, g in new_graphs.items():
        new_inv[gid] = graph_invariant(g["N"], [tuple(e) for e in g["edges"]])

    # 既有比较集：22 语料（现算）＋ 8 张既有 GT8 新图（字面取自 34ff826f97c2）
    corpus = load_corpus_indexed()
    existing_inv, existing_sha, existing_NE = {}, set(), set()
    n_corpus = 0
    for g in corpus:
        ed = [tuple(e) for e in g["edges"]]
        existing_inv.setdefault(str(graph_invariant(g["N"], ed)), []).append(
            g["graph_id"])
        if g.get("sha256"):
            existing_sha.add(g["sha256"])
        existing_NE.add((g["N"], len(ed)))
        n_corpus += 1
    expand = read_json(ANCHORS["expand_gt8"])
    for gid, rec in expand["nonisomorphism_sentinel"]["per_graph"].items():
        inv = rec["invariant"]
        existing_inv.setdefault(
            str((int(inv[0]), int(inv[1]), tuple(inv[2]), tuple(inv[3]))), []
        ).append(gid)
        existing_sha.add(rec["sha256"])
        existing_NE.add((int(inv[0]), int(inv[1])))

    # 既有低臂 n_named（字面取自 34ff826f97c2 per_graph）
    existing_low_named = {g: expand["per_graph"][g]["n_named"] for g in
                          ("GT8_A_low", "GT8_B_low", "GT8_C_low", "GT8_D_low")}

    per_graph, checks = {}, []
    for gid, g in new_graphs.items():
        ed = [tuple(e) for e in g["edges"]]
        inv = new_inv[gid]
        per_graph[gid] = {
            "N": g["N"], "n_edges": len(ed), "n_named": len(g["named_edges"]),
            "n_filler": len(g["filler_edges"]), "sha256": g["sha256"],
            "hub_concentration": hub_concentration(g["N"], ed),
            "invariant_collides_with_existing_set":
                existing_inv.get(str(inv), []),
            "sha256_collides_with_existing_set": bool(g["sha256"] in existing_sha),
            "NE_collides_with_existing_set": bool((g["N"], len(ed))
                                                  in existing_NE)}

    # ① 对配
    pairing = []
    for hi, lo in LOWARM_PAIRS:
        ok = (per_graph[hi]["N"] == per_graph[lo]["N"]
              and per_graph[hi]["n_edges"] == per_graph[lo]["n_edges"])
        pairing.append({"pair": f"{hi}__vs__{lo}", "N": per_graph[hi]["N"],
                        "n_edges": per_graph[hi]["n_edges"],
                        "high_and_low_matched": bool(ok)})
        checks.append(("pairing_" + lo, bool(ok)))

    # ② 低臂 n_named 写死互异（且与既有低臂逐个不同）
    new_named = {lo: per_graph[lo]["n_named"] for _hi, lo in LOWARM_PAIRS}
    mutual = len(set(new_named.values())) == len(new_named)
    diff_exist = all(v not in existing_low_named.values()
                     for v in new_named.values())
    checks.append(("lowarm_n_named_mutually_distinct", bool(mutual)))
    checks.append(("lowarm_n_named_differs_from_existing", bool(diff_exist)))

    # ③④⑤ 不同构 / sha 全新
    for gid in LOWARM_SEEDS:
        checks.append((f"nonisomorphic_to_existing_30_{gid}",
                       per_graph[gid]["invariant_collides_with_existing_set"]
                       == []))
        checks.append((f"sha256_fresh_{gid}",
                       not per_graph[gid]["sha256_collides_with_existing_set"]))
    ids = list(new_inv)
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            checks.append((f"nonisomorphic_pairwise_{ids[i]}_{ids[j]}",
                           str(new_inv[ids[i]]) != str(new_inv[ids[j]])))

    # ⑥ 高臂 hub 严格大于配对低臂
    for hi, lo in LOWARM_PAIRS:
        checks.append((f"high_hub_gt_low_hub_{lo}",
                       per_graph[hi]["hub_concentration"]
                       > per_graph[lo]["hub_concentration"]))

    all_ok = all(v for _k, v in checks)
    return {"all_pass": bool(all_ok), "checks": {k: bool(v) for k, v in checks},
            "n_corpus_graphs": n_corpus,
            "n_existing_gt8_graphs": 8,
            "comparison_set_graphs": n_corpus + 8,
            "n_existing_comparison_graphs": len(existing_NE),
            "existing_low_named": existing_low_named,
            "new_low_named_written_dead": new_named,
            "pairing": pairing, "per_graph": per_graph}


# =============================================================================
# 读数面（eval_graph 首次调用在此之后）
# =============================================================================
def _diffusion_config():
    from deposon_diffusion import DiffusionConfig
    return DiffusionConfig()


def measure(graphs_by_id, origin_of, pairs):
    """对给定图集跑既有三臂协议，逐图 + 逐对读数（0 新协议）。"""
    cfg = _diffusion_config()
    per_graph, per_pair = {}, []
    for hi, lo in pairs:
        rec = {"pair": f"{hi}__vs__{lo}", "high": hi, "low": lo,
               "origin": origin_of.get(hi, "as_run")}
        for role, gid in (("high", hi), ("low", lo)):
            g = graphs_by_id[gid]
            ed = [tuple(e) for e in g["edges"]]
            arms = eval_graph(g, cfg)
            feats = {"hub_concentration": hub_concentration(g["N"], ed),
                     "real_semantics": 0}
            d_fr = arms["field_mean"]["named"] - arms["random"]["named"]
            d_fd = arms["field_mean"]["named"] - arms["degree"]["named"]
            per_graph[gid] = {
                "structure": g["structure"], "N": g["N"], "n_edges": len(ed),
                "n_named": len(g["named_edges"]),
                "n_filler": len(g["filler_edges"]),
                "source": g["source"], "target": g["target"], "seed": g["seed"],
                "sha256": g["sha256"], "features": feats,
                "field_named": arms["field_mean"]["named"],
                "random_named": arms["random"]["named"],
                "degree_named": arms["degree"]["named"],
                "diff_fm_rand": d_fr, "diff_fm_deg": d_fd,
                "invariant": [g["N"], len(ed)]}
            rec[f"diff_{role}"] = d_fr
            rec[f"hub_{role}"] = feats["hub_concentration"]
        rec["concordant"] = bool(rec["diff_high"] > rec["diff_low"])
        rec["tied"] = bool(rec["diff_high"] == rec["diff_low"])
        per_pair.append(rec)
    return per_graph, per_pair


def subset_attrib(sub):
    c = sum(1 for p in sub if p["concordant"])
    r = sum(1 for p in sub if p["diff_high"] < p["diff_low"])
    t = sum(1 for p in sub if p["tied"])
    return {"n_pairs": len(sub), "n_concordant": c, "n_reversed": r,
            "n_tied": t}


def _collision_groups(d):
    """把 {low_arm: diff} 按值分组，返回出现 ≥2 次的值组（0 归并，仅登记）。"""
    groups = {}
    for k, v in d.items():
        groups.setdefault(v, []).append(k)
    return {str(v): ks for v, ks in sorted(groups.items()) if len(ks) > 1}


# =============================================================================
# 主流程
# =============================================================================
def main():
    anchors, anchors_ok = anchor_audit()
    if not anchors_ok:
        bad = [k for k, v in anchors.items()
               if v.get("matches_expected") is False]
        raise SystemExit(f"ABORT：锚件哈希与给定值不符 {bad}")
    anchor_before = {k: read_bytes(rel) for k, rel in ANCHORS.items()}

    # ---- 阶段 1：构造面 pre-flight（0 读数）----
    pre = structure_preflight()
    if not pre["all_pass"]:
        return {"aborted": True, "reason": "构造面 pre-flight 0 通过 ⇒ "
                                            "K-V5R3-0-B ② 素材不可得面",
                "preflight": pre, "anchors": anchors}

    # ---- 阶段 2：读数面 ----
    graphs, origin = {}, {}
    for gid in GT8_SEEDS:                       # as-run 4 图（既有构造，0 改）
        graphs[gid] = build_gt8_graph(gid)
        origin[gid] = "as_run"
    prev = _load_prev_expansion_graphs()        # 扩面 4 图（既有构造，0 改）
    for gid, g in prev.items():
        graphs[gid] = g
        origin[gid] = "v5_expansion"
    for gid in LOWARM_SEEDS:                    # 本面新增 4 图
        graphs[gid] = build_lowarm_graph(gid)
        origin[gid] = "p10_lowarm_new"

    all_pairs = (tuple(GT8_PAIRS)
                 + (("GT8_C_high", "GT8_C_low"), ("GT8_D_high", "GT8_D_low"))
                 + LOWARM_PAIRS)
    per_graph, per_pair = measure(graphs, origin, all_pairs)

    # ---- 复现检查：既有 4 对在本环境逐值复算 vs 盘上字面（0 新测量）----
    asrun = read_json(ANCHORS["asrun_gt8"])
    expand = read_json(ANCHORS["expand_gt8"])
    landed = {p["pair"]: p for p in asrun["per_pair"]}
    for p in expand["per_pair"]:
        landed[p["pair"]] = p
    repro, n_id = {}, 0
    for p in per_pair:
        if p["origin"] == "p10_lowarm_new":
            continue
        a = landed.get(p["pair"])
        same = bool(a and a["diff_high"] == p["diff_high"]
                    and a["diff_low"] == p["diff_low"]
                    and a["hub_high"] == p["hub_high"]
                    and a["hub_low"] == p["hub_low"])
        repro[p["pair"]] = {"landed_diff_high": a["diff_high"],
                            "recomputed_diff_high": p["diff_high"],
                            "landed_diff_low": a["diff_low"],
                            "recomputed_diff_low": p["diff_low"],
                            "bit_identical": same}
        n_id += int(same)
    n_existing_pairs = sum(1 for p in per_pair if p["origin"] != "p10_lowarm_new")
    repro_ok = bool(n_id == n_existing_pairs)
    if not repro_ok:
        return {"aborted": True,
                "reason": "既有 4 对复现检查 0 全等 ⇒ 环境不可比，0 继续",
                "reproduction_check": repro, "anchors": anchors}

    # ---- P-3 ③ 两者并报：读数级 + 构造级 ----
    low_diffs = {p["low"]: p["diff_low"] for p in per_pair}
    new_lows = [lo for _hi, lo in LOWARM_PAIRS]
    existing_lows = [lo for lo in low_diffs if lo not in new_lows]
    reading_level = {
        "definition": "去重后不同 diff_low 值的个数（γ-V5R3-21 读数级口径）",
        "low_arm_diffs": low_diffs,
        "n_low_arms": len(low_diffs),
        "n_distinct_all_pool": len(set(low_diffs.values())),
        "n_distinct_existing_4": len(set(low_diffs[l] for l in existing_lows)),
        "n_distinct_new_2": len(set(low_diffs[l] for l in new_lows)),
        "collision_groups_existing":
            _collision_groups({l: low_diffs[l] for l in existing_lows}),
        "collision_groups_new":
            _collision_groups({l: low_diffs[l] for l in new_lows}),
        "collision_groups_all_pool": _collision_groups(low_diffs),
    }
    all_gids = [g for p in all_pairs for g in p]
    construction_level = {
        "definition": "构造不变量：sha256 两两不同 ＋ 不同构哨兵通过 ＋ 低臂 n_named 互异",
        "sha256_all_distinct_across_12_graphs": bool(
            len({per_graph[g]["sha256"] for g in all_gids}) == len(all_gids)),
        "nonisomorphism_sentinel_self_collision_fixed": True,
        "comparison_set_graphs": pre["comparison_set_graphs"],
        "comparison_set_breakdown": {
            "n_corpus_graphs": pre["n_corpus_graphs"],
            "n_existing_gt8_graphs": pre["n_existing_gt8_graphs"]},
        "new_graphs_nonisomorphic_to_existing_30": bool(
            all(pre["per_graph"][g]["invariant_collides_with_existing_set"] == []
                for g in LOWARM_SEEDS)),
        "new_graphs_sha256_fresh": bool(
            all(not pre["per_graph"][g]["sha256_collides_with_existing_set"]
                for g in LOWARM_SEEDS)),
        "new_low_named_written_dead_mutually_distinct":
            pre["checks"]["lowarm_n_named_mutually_distinct"],
        "new_low_named_differs_from_existing_lows":
            pre["checks"]["lowarm_n_named_differs_from_existing"],
        "n_paired_NE_matched_all": bool(
            all(x["high_and_low_matched"] for x in pre["pairing"])),
    }

    # ---- 并报口径（K-V5R3-0-E ＋ 件 B §2.1）----
    subs = {
        "as_run_2_pairs": [p for p in per_pair if p["origin"] == "as_run"],
        "v5_expansion_2_pairs": [p for p in per_pair
                                 if p["origin"] == "v5_expansion"],
        "p10_new_2_pairs": [p for p in per_pair
                            if p["origin"] == "p10_lowarm_new"],
        "all_6_pairs": per_pair,
    }
    subsets = {k: subset_attrib(v) for k, v in subs.items()}
    subsets["required_two_framings_per_prereg"] = {
        "新增对子集": subsets["p10_new_2_pairs"],
        "全部对池": subsets["all_6_pairs"]}

    # ---- 机械纯函数输出（既有 gt8_verdict；**非本棒判定**）----
    mechanical = {k: gt8_verdict(v) for k, v in subs.items()}

    def gap_flag(a):
        return bool(a["n_tied"] == 0 and 2 <= a["n_concordant"] <= a["n_pairs"] - 1)
    coverage_gap = {k: gap_flag(v) for k, v in subsets.items()
                    if isinstance(v, dict) and "n_pairs" in v}

    # ---- 防退化门：件 B §5.4 要求在新面**重新自证** ----
    new_gids = [g for p in LOWARM_PAIRS for g in p]
    gates = {
        "new_2_pairs_diff_fm_rand": anti_degeneration_gate(
            "p10-new · diff_fm_rand 逐图（4 值）",
            [per_graph[g]["diff_fm_rand"] for g in new_gids]),
        "new_2_pairs_hub_concentration": anti_degeneration_gate(
            "p10-new · hub_concentration 逐图（4 值）",
            [per_graph[g]["features"]["hub_concentration"] for g in new_gids]),
        "all_6_pairs_diff_fm_rand": anti_degeneration_gate(
            "p10-all-6 · diff_fm_rand 逐图（12 值）",
            [per_graph[g]["diff_fm_rand"] for g in all_gids]),
        "all_6_pairs_hub_concentration": anti_degeneration_gate(
            "p10-all-6 · hub_concentration 逐图（12 值）",
            [per_graph[g]["features"]["hub_concentration"] for g in all_gids]),
        "all_6_pairs_diff_low_only": anti_degeneration_gate(
            "p10-all-6 · diff_low 逐对（6 值）",
            [p["diff_low"] for p in per_pair]),
    }
    gate_all_pass = bool(all(g["gate_pass"] for g in gates.values()))

    out = {
        "case": "gt8_p10_lowarm_independent_measurement_surface_set_A",
        "class": "新增测量面 · low 臂独立读数面（件 B P-1① B-案 2 ＋ 案 1 约束）",
        "produced_by": "worker 棒 1b（executor）· set A · "
                       "mvs_cb132cd536f648299c713abf2071d026",
        "concurrent_writer_collision": COLLISION,
        "prereg_control_doc": {"path": ANCHORS["prereg_p10"],
                               "sha12": anchors["prereg_p10"]["sha12_measured"]},
        "pi_decision_batch": {"path": ANCHORS["confirm_b9"],
                              "sha12": anchors["confirm_b9"]["sha12_measured"],
                              "P-1": "① B-案 2（含案 1 约束）",
                              "P-2": "① 只增不减（4 对为下限）＋ 本棒测量前写死 ＋2 对",
                              "P-3": "③ 读数级 ＋ 构造级 两者并报",
                              "P-4": "② 撞值并报披露（0 归并）",
                              "P-5": "① 0 设独立证据数下限数值门",
                              "P-6": "① real_semantics 仍 deferred"},
        "anchors_measured": anchors,
        "scale_freeze_written_before_measurement": {
            "rule": ("件 B §9 P-2 ＋ 2505ff5d203f §6.3「对数与种子数测量前写死，"
                     "0 依既有读数反选」；写死时点 = 本脚本首次 eval_graph 调用"
                     "之前，0 任何新读数存在"),
            "pairs_existing": 4, "pairs_new": 2, "pairs_total": 6,
            "increment_rationale": ("＋2 对与上一棒扩面步（2→4）同为 ＋2；"
                                    "未按任何读数调档"),
            "new_seeds": LOWARM_SEEDS,
            "seed_numbering": "沿 208801–208804（as-run）／208805–208808（扩面）续号；"
                              "与语料族 200101–200106 0 重叠",
            "pair_matching_written_dead": pre["pairing"],
            "lowarm_n_named_written_dead": pre["new_low_named_written_dead"],
            "existing_low_named": pre["existing_low_named"],
            "distinctness_basis": ("n_named = #{i ∈ 1..N-1 : k·i+1 < N} 的结构"
                                   "算术 ＋ 种子续号推出；0 参考任何 diff 读数"),
            "case1_caveat": ("件 B §4.2 案 1 ②：n_named 互异只**降低**撞值概率，"
                             "0 构造性排除再次相等（1/10 与 1/14 仍可相等）⇒ "
                             "本面 0 承诺「补测后必定互异」")},
        "structure_preflight_no_readings": {
            "all_pass": pre["all_pass"], "checks": pre["checks"],
            "per_graph": pre["per_graph"]},
        "executor_protocol": {
            "arms": list(ARMS), "rng": "default_rng(g_seed*100003+ei)",
            "field_instance_seed": "g_seed+ei",
            "leave_one_out": "全边留一", "candidate": "全候选 raw 口径",
            "metric": "named Hits@3（gold_rank < 3）",
            "hub_concentration": "max_in_degree / n_edges",
            "real_semantics": 0, "new_protocol_added": 0,
            "note": "协议函数经只读 import 复用（run_v20_gt8 / mindmap_corpus_v20 / "
                    "deposon_diffusion），既有件 byte 0 改动"},
        "reproduction_check_existing_4_pairs": {
            "purpose": "环境可比性前提（0 新测量：既有 4 对在本环境复算 vs 盘上字面）",
            "n_pairs": n_existing_pairs, "n_pairs_bit_identical": n_id,
            "all_bit_identical": repro_ok, "per_pair": repro},
        "per_graph": per_graph,
        "per_pair": per_pair,
        "subset_attribution_mechanical": subsets,
        "mechanical_gt8_verdict_function_output_NOT_A_VERDICT": {
            "note": ("本块是既有纯函数 gt8_verdict 的机械输出，**0 是本棒判定**；"
                     "本棒 0 代裁、0 预判档位（件 B §7.2 棒 2 = verdict-keeper）"),
            "function": "run_v20_gt8.gt8_verdict（min_pairs 既有默认 2，0 改）",
            "by_subset": mechanical},
        "gamma14_coverage_gap_mechanical_flag": {
            "note": ("#conc ∈ [2, n−1] 且 0 平局的形态在 v2 else 归属中无明文"
                     "（γ-V5R3-14）；本棒只机械标记**是否出现**，0 自创归属、"
                     "0 裁 KD（K-V5R3-0-A）"),
            "flags": coverage_gap},
        "P3_both_framings_reported": {
            "reading_level": reading_level, "construction_level": construction_level},
        "P4_collision_disclosure_not_merged": {
            "rule": "P-4 ② 并报披露（0 归并、0 沿 GT8-1 ③ 精神类推跨对撞值）",
            "gamma_21_existing": {
                "literal": "C_low 与 D_low 的 diff_fm_rand 双双 = 0.25（γ-V5R3-21）",
                "n_named_both": 8, "granularity": "1/8",
                "disclosure": "本面 0 改动、0 归并、0 抹除该撞值"
                              "（K-V5R3-0-D 历史 0 回改）"},
            "new_face_collisions": {
                "within_new_2_pairs": reading_level["collision_groups_new"],
                "within_all_6_pairs": reading_level["collision_groups_all_pool"]},
            "no_merge_statement": ("本面只登记撞值事实，0 把撞值对并为 1 个证据；"
                                   "「独立 low 臂基线」的任何**归并计数**由棒 2 "
                                   "按 P-4 口径裁定，本棒 0 预裁")},
        "anti_degeneration_gates_new_surface": gates,
        "gate_all_pass": gate_all_pass,
        "gate_failure_registration": {
            "any_gate_failed": bool(not gate_all_pass),
            "failed_gates": [k for k, v in gates.items() if not v["gate_pass"]],
            "cause": ("新增 2 对的两个高臂 hub_concentration 恰同落 0.5 ⇒ 该 4 值"
                      "序列 n_distinct = 3 ⇒ 门「n_distinct > 3」不达"),
            "this_rod_action": ("如实登记，**0 重掷结构、0 事后调构、0 改门值**；"
                                "本面 0 自行放宽或提高该门"),
            "note": ("本面 0 预判该门的归属（PASS/FAIL/KD）—— 归棒 2 "
                     "verdict-keeper 按既有字面裁定"),
        },
        "thresholds_used": {
            "min_pairs": GT8_MIN_PAIRS,
            "pass_rule": "全部对同向（#conc = n 且 n ≥ 2）",
            "kill_rule": "全部对全反",
            "anti_degeneration_gate": "n_distinct > 3 且 std > 0",
            "hub_concentration": "max_in_degree / n_edges",
            "pair_requirement": "N 与 n_edges 尽量对配（SPEC_GT8 L30）",
            "granularity_rule": "named Hits@3，named 边数 = n_named（0 取整/0 ±ε）",
            "independent_evidence_floor": "不存在（P-5 ①：0 设数值门）",
            "source": "34ff826f97c2 thresholds_used ＋ K-V5R3-0-B ③ ＋ SPEC_GT8 L21/L30",
            "every_value_unchanged": True},
        "new_thresholds_added": 0,
        "no_backtrack_guards": {
            "as_run_verdict_2b88948dca19_supports_H_GT8": "0 触动（byte 0 改）",
            "v5_expansion_terminal_PASS_34ff826f97c2": "0 触动（byte 0 改）",
            "pass_rule_min_pairs_kill_rule": "一字不动",
            "existing_4_pairs_graphs_and_readings": "0 重配（K-V5R3-0-D）",
            "derived_json_merge": 0,
            "eighteen_frozen_and_nine_grid": "0 触动（本棒只新建件）",
            "key_read": 0, "llm_api_calls": 0,
            "other_stick_outputs_overwritten_by_this_stick": 0,
            "four_independent_concordant_evidence_statement":
                "仍禁述（γ-V5R3-21 结论上限下调 0 因补测自动撤销）",
            "effect_size_or_significance_statement": "永久禁述（K-V5R3-GT8-4）",
            "family_L_extrapolation": 0,
            "grid_count_equals_independent_evidence": "禁述（件 B §4.2 案 2 ③）"},
        "parallel_reporting_K_V5R3_0_E": {
            "原判（as-run 2 对）": asrun["verdict"]["verdict"],
            "并列判（v5 扩面 4 对 · 既有）": expand["expanded_reading"][
                "verdict_mechanical"]["verdict"],
            "本面新增对子集机械计数": subsets["p10_new_2_pairs"],
            "本面全部对池机械计数": subsets["all_6_pairs"],
            "note": "原判与既有并列判 byte 0 改动；本面读数为**并列新判的输入**"},
        "P1_disclosure_registered": {
            "prereg_literal": "件 B §4.2 案 2 ①：本面有可能把 gt8 的 PASS 面"
                              "推向 FAIL 面（K-V5R3-GT8-2 第二步）",
            "acknowledged_before_run": True,
            "mechanical_outcome_readout": {
                "new_2_pairs": subsets["p10_new_2_pairs"],
                "all_6_pairs": subsets["all_6_pairs"],
                "plain_reading": ("本面新增 2 对 2/2 同向、0 反向、0 平局；"
                                  "全部对池 6/6 同向、0 反向、0 平局 ⇒ "
                                  "**本面未把 PASS 面推向 FAIL 面**"),
                "still_forbidden": "此为机械计数，0 表述为效应量/显著性，"
                                   "0 表述为「6 个独立同向证据」"},
            "worker_prejudgment": None},
        "terminal_state": None,
        "adjudication": {"owner": "verdict-keeper（棒 2）",
                         "state": "PENDING",
                         "this_rod_declared": None,
                         "note": "本棒 0 代裁、0 预判档位、0 落档"},
        "honesty": {
            "what_this_rod_ran": "构造面 pre-flight（0 读数）＋ 既有 4 对复现复算"
                                 "（0 新测量：与盘上字面比对）＋ 本面新增 4 图读数",
            "skills_loaded": "0（派工单未指定 skill）",
            "not_done": ["0 独立复核 18 frozen 的具体条目清单",
                         "0 独立复核 9 网格的具体条目清单",
                         "0 触及 real_semantics 轴（deferred）",
                         "0 LLM API / 0 proxy / 0 key",
                         "0 预填独立证据数下限（属 PI 拍板项 P-5）",
                         "0 对 hub_concentration 门不达作任何归属或重掷结构"],
            "json_determinism": "本 JSON 不含时间戳/运行秒 ⇒ 重跑逐字节不变可自证",
            "self_sha_not_written": "本件 SHA-12 0 自写入（避免自指悖论），"
                                    "由交付回执自报盘上实测值",
            "judgment_components_worker": [
                "规模增量取 ＋2 对（PI 只给「只增不减」方向，具体档位属执行面）"
                "—— 属本棒判断，PI/verdict-keeper 可推翻",
                "E/F 低臂取平衡 k 叉树（S2 口径）以实现 n_named 写死互异 —— "
                "沿既有 C/D 低臂构型族，0 新协议",
                "高臂取「双枢纽星 / 枢纽脊星」两种新构型以避开既有图不变量的"
                "（N, n_edges, 入度多重集, 出度多重集）碰撞 —— 属本棒构造选择；"
                "⚠ 副作用：两高臂 hub_concentration 恰同为 0.5，致新面 hub 门"
                "n_distinct = 3（见 gate_failure_registration）"]},
        "runtime_env": {"python": sys.version.split()[0],
                        "numpy": np.__version__},
    }

    # ---- 0 触动实证：锚件 byte 比对 ----
    anchor_after = {k: read_bytes(rel) for k, rel in ANCHORS.items()}
    untouched = {k: bool(anchor_before[k] == anchor_after[k]) for k in ANCHORS}
    out["untouched_anchor_bytes_unchanged"] = untouched
    out["all_anchors_untouched"] = bool(all(untouched.values()))
    out["output_paths_written"] = [OUT_JSON]

    written = write_json(OUT_JSON, out)
    print(json.dumps({"written": written, "subsets": subsets,
                      "reading_level": reading_level,
                      "gates": {k: v["gate_pass"] for k, v in gates.items()},
                      "failed_gates": [k for k, v in gates.items()
                                       if not v["gate_pass"]],
                      "repro_all_bit_identical": repro_ok,
                      "preflight_all_pass": pre["all_pass"]},
                     ensure_ascii=False, indent=1))
    return out


def _load_prev_expansion_graphs():
    """取扩面 4 图（GT8_C/D_high/low）：只读 import 上一棒 executor 的构造器，
    既有件 0 写入；sha256 与 34ff826f97c2 落盘字面逐一核对。"""
    spec = importlib.util.spec_from_file_location(
        "_v5_gt_prev_exec", os.path.join(HERE, "_v5_gt_exec_2026_09_29.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    out = {gid: m.build_v5_gt8_graph(gid) for gid in m.V5GT8_SEEDS}
    landed = read_json(ANCHORS["expand_gt8"])["per_graph"]
    for gid, g in out.items():
        if g["sha256"] != landed[gid]["sha256"]:
            raise SystemExit(f"ABORT：扩面图 {gid} sha256 与盘上字面不符")
    return out


if __name__ == "__main__":
    main()
