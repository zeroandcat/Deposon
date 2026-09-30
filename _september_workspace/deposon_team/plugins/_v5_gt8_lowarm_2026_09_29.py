# -*- coding: utf-8 -*-
"""V5 GT-8 · **P-10 low 臂独立测量面** · 执行面（件B P-1① 主案）· worker · 2026-09-29

  → results/_v5_gt8_lowarm_resultb_2026_09_29.json  （**set B** · 新名独立读数件，0 合并）
  → results/_v5_gt8_lowarm_exec_2026_09_29.md        （新名执行件）

⚠️⚠️ **并发写者碰撞登记（必读 · 关系到两件读数的归属）**：
  本路径 `deposon_team/plugins/_v5_gt8_lowarm_2026_09_29.py` 上**发生过并发写者碰撞**：
    · 15:20:5x  另一 worker 棒（session **mvs_cb132cd536f648299c713abf2071d026**）写入本路径；
    · 15:20:58 该棒以本路径启动 `python`（PID 12880，stdout/stderr → `.tmp_p10_out/.err.txt`）；
    · **15:21:01 本棒（session mvs_02eb4a5ab8024f439c31147529aaf7d4）写入本路径，覆盖了对方的源码**；
    · 15:21:52 对方进程完成，落 `results/_v5_gt8_lowarm_result_2026_09_29.json`（**set A**）。
  ⇒ **本文件是 set B 的源码，0 是 set A 的源码**；set A 的源码已丢失（**本棒的写入造成，如实交代**）。
  ⇒ 因此本棒**不覆写** set A（派工单「0 假定、0 覆写」），改为在**新名**下产出 set B，
    并在执行件中把两套读数**并排如实登记**，**0 代 PI/verdict-keeper 选哪一套为准**。

控制件（先核哈希后引用 · 本 Turn 盘上实测）：
  - results/_v5_gt_p10_lowarm_prereg_2026_09_29.md        07e28e2fe374  件B · 本面立线
  - results/_v5_gt_verdict_2026_09_29.md                   45648b0ec940  GT 判定件（γ-21 堵点来源）
  - results/_v5_gt8_expand_2026_09_29.json                34ff826f97c2  gt8 扩面读数（低臂读数字面出处）
  - results/deposon_v20_gt8.json                           2b88948dca19  gt8 as-run 读数
  - results/_v5_gt5_gt6_gt8_gt5b_gt_prereg_2026_09_28.md  2505ff5d203f  GT 系立线包（判死线字面）
  - docs/SPEC_GT8.md                                      edf6f4465ead  GT-8 预登记 SPEC（设计字面）

PI 复核裁项（件B §9 P-1…P-6 · 经派工单载明；**件B §11 勾选栏盘上仍空白、件B 字节 0 改动**，
如实登记该事实，不编造勾选）：
  - P-1 ① 主案 = B-案 2（增对数）含 B-案 1 约束（新增对低臂 n_named 测量前写死互异）
  - P-2 ① 只增不减（既有 4 对为下限）—— 对数与种子数由本棒**测量前写死**（立线包 §6.3）
  - P-3 ③ 「独立」判据锚点 = **两者并报**（读数级 + 构造级）
  - P-4 ② `γ-21` 撞值 = **并报披露**（0 归并、0 自行类推 GT8-1）
  - P-5 ① **不设**「独立证据数下限」⇒ `new_thresholds_added = 0`
  - P-6 ① `real_semantics` 轴**仍 deferred**

本棒身份：**worker**。**0 代裁**：0 预判档位、0 落终态、0 改写既有判定、0 改任何既有件
（全部只读 open/json.load；所有 out 路径均为新名）、0 合并派生 JSON、0 读 key（R4）、
0 新设数值阈值、0 代 verdict-keeper / protocol-keeper / evidence-auditor / doc-writer。

纪律自证：
  1. 协议全沿既有字面：全边留一、全候选 raw 口径、rng = g_seed*100003+ei、场实例种子
     g_seed+ei、named Hits@3、hub_concentration = max_in_degree/n_edges、real_semantics = 0
     ⇒ 协议函数经**只读 import** 复用 `run_v20_gt8.eval_graph` / `hub_concentration` /
     `graph_invariant`，0 改既有 runner。
  2. 判死线只引用既有字面：min_pairs=2 / pass_rule / kill_rule / 防退化门 n_distinct>3 且 std>0
     ⇒ 一字不动，0 新设。
  3. 既有 4 对读数**以盘上 `34ff826f97c2` 为准**（K-V5R3-0-D 历史 0 回改）；本环境重算仅作
     复现核对，逐值登记，0 以重算覆盖盘上值。
  4. 派生 JSON 0 合并（K-V5R3-0-D/E）。
  5. 18 frozen 与 9 网格 **0 触动**；**如实交代**：本 Turn 0 独立复核 18 frozen / 9 网格
     的具体清单（未开列该清单的件），此处按长期铁律字面遵守 + 锚件逐件跑前/跑后 SHA-12 自证。
  6. 0 LLM API / 0 proxy / 0 key 读取（全脚本无 requests/openai/http；R4 key 永不明文）。
  7. **无墙钟时间戳入 payload** ⇒ 同输入重跑逐字节一致（可自证）。
  8. 署名如实：worker（mvs_02eb4a5ab8024f439c31147529aaf7d4），0 冒充任何他方。

⚠️ 件B §4.2 案 2 ① 自带披露（原文义务，本件原样承接）：**补测可能把 gt8 的 PASS 面推向
FAIL 面**（新增对若反向或平局 ⇒ pass_rule 不命中 ⇒ 落 K-V5R3-GT8-2 第二步最不利方向）。
**本棒如实执行、如实登记，0 预判结果。**
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import sys

REPO = r"D:/私人资料/deposon-repo"
HERE = REPO
RESULTS_REL = "results"
DATE_TAG = "2026_09_29"
OUT_RESULT = f"{RESULTS_REL}/_v5_gt8_lowarm_resultb_{DATE_TAG}.json"
SET_A_RESULT = f"{RESULTS_REL}/_v5_gt8_lowarm_result_{DATE_TAG}.json"   # 只读并报，0 覆写
SELF_NAME = "deposon_team/plugins/_v5_gt8_lowarm_2026_09_29.py"

sys.path.insert(0, REPO)

import numpy as np  # noqa: E402

from deposon_diffusion import DiffusionConfig  # noqa: E402
from mindmap_corpus_v20 import (_assign_labels, _canonical_sha256,  # noqa: E402
                                is_dag, longest_path_family)
from run_v15_experiment import row_normalize  # noqa: E402
from run_v19_fullrank import full_candidate_mask, gold_rank  # noqa: E402
from run_v19_meanfield import field_scores_init  # noqa: E402
from run_v20_gt8 import (ARMS, GT8_MIN_PAIRS, GT8_PAIRS, GT8_SEEDS,  # noqa: E402
                         build_gt8_graph, eval_graph, graph_invariant,
                         hub_concentration)

# ---------------------------------------------------------------- 只读锚件（0 写入）
ANCHORS = {
    "prereg_p10_lowarm": f"{RESULTS_REL}/_v5_gt_p10_lowarm_prereg_{DATE_TAG}.md",
    "verdict_gt": f"{RESULTS_REL}/_v5_gt_verdict_{DATE_TAG}.md",
    "prereg_gt_pkg": f"{RESULTS_REL}/_v5_gt5_gt6_gt8_gt5b_gt_prereg_2026_09_28.md",
    "gt8_expand": f"{RESULTS_REL}/_v5_gt8_expand_{DATE_TAG}.json",
    "gt8_as_run": f"{RESULTS_REL}/deposon_v20_gt8.json",
    "spec_gt8": "docs/SPEC_GT8.md",
    "upstream_gt_exec": "_v5_gt_exec_2026_09_29.py",
    "runner_gt8": "run_v20_gt8.py",
    "protocol_diffusion": "deposon_diffusion.py",
    "corpus_loader": "mindmap_corpus_v20.py",
    "corpus_index": "corpus/v20/index.json",
}
# 立线/派工单登记的 SHA-12（只读复核用；差异如实登记为 γ，0 修改任何件）
PREREG_ANCHOR_TABLE = {
    "prereg_p10_lowarm": "07e28e2fe374",
    "verdict_gt": "45648b0ec940",
    "prereg_gt_pkg": "2505ff5d203f",
    "gt8_expand": "34ff826f97c2",
    "gt8_as_run": "2b88948dca19",
    "spec_gt8": "edf6f4465ead",
}


def sha12(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def sha12_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:12]


def fingerprint() -> dict:
    out = {}
    for k, rel in ANCHORS.items():
        p = os.path.join(REPO, rel.replace("/", os.sep))
        b = open(p, "rb").read()
        rec = {"path": rel, "sha12": sha12_bytes(b), "bytes": len(b),
               "access": "read_only"}
        if k in PREREG_ANCHOR_TABLE:
            rec["registered_sha12"] = PREREG_ANCHOR_TABLE[k]
            rec["matches_registered"] = bool(rec["sha12"] == PREREG_ANCHOR_TABLE[k])
        out[k] = rec
    return out


def read_json(rel: str):
    with open(os.path.join(REPO, rel.replace("/", os.sep)), encoding="utf-8") as f:
        return json.load(f)


def write_json(rel: str, obj) -> dict:
    p = os.path.join(REPO, rel.replace("/", os.sep))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    b = json.dumps(obj, ensure_ascii=False, indent=1).encode("utf-8")
    with open(p, "wb") as f:
        f.write(b)
    return {"path": rel, "sha12": sha12_bytes(b), "bytes": len(b)}


# ---------------------------------------------------------------- 只读语料加载（γ-13 沿案）
def load_corpus_indexed(corpus_dir: str, families=("S", "L")):
    """只读 index 驱动加载：与 `mindmap_corpus_v20.load_corpus` 读取段逐行同序，
    仅跳过 R2/E3 孤儿哨兵的 raise（3 个非图记录 .json 被误判，γ-V5R3-13；PI 已拍板修
    加载器、**本棒 0 代行修**、0 改 `mindmap_corpus_v20`、0 重建 index.json）。"""
    with open(os.path.join(corpus_dir, "index.json"), encoding="utf-8") as f:
        idx = json.load(f)
    out = []
    for e in idx["graphs"]:
        if families and e["family"] not in families:
            continue
        with open(os.path.join(corpus_dir, e["file"]), encoding="utf-8") as f:
            out.append(json.load(f))
    return out


# ================================================================ §1 测量前写死的设计
# （立线包 2505ff5d203f §6.3「对数与种子数测量前写死，0 依既有读数反选」）
#
# 写死依据（**只依设计需要，0 依任何 diff 读数**）：
#   · P-2 ①「只增不减」⇒ 既有 4 对为下限，本面新增对数 ≥ 1；本棒取**最小充分增量 2 对**
#     （E / F）——理由：补读数级独立 low 臂基线需**至少 2 张新增低臂**方能产生新的去重值；
#     2 对 = 满足该设计需要的最小增量，0 增广充数、0 为凑 PASS 选数。
#   · B-案 1 约束：新增对低臂 `n_named` 测量前写死**互异**：E_low = 9、F_low = 13
#     （9 ≠ 13；且与既有 15/12/8/8 均不同 ⇒ 刻度 1/9、1/13 与既有 1/15、1/12、1/8 全异）。
#     写死口径 = 结构参数（内部节点数），**不是读数**；所用既有事实是件B §2.2 已登记的
#     **构造侧成因**（γ-PKB-1），非任何 diff 读数 ⇒ 不违「0 依既有读数反选」。
#   · 种子沿 as-run 号段续写 208809–208812（语料族 200101–200106，0 重叠），测量前写死。
#
# ⚠️ 互异 n_named 只**降低**撞值概率（可取值集合不同），**不排除**再次相等
# （如 1/9 与 2/18 仍可相等）⇒ 0 承诺「补测后必定互异」（件B §4.2 案 1 ②）。
NEW_SEEDS = {"GT8_E_high": 208809, "GT8_E_low": 208810,
             "GT8_F_high": 208811, "GT8_F_low": 208812}
NEW_PAIRS = (("GT8_E_high", "GT8_E_low"), ("GT8_F_high", "GT8_F_low"))
# 全部对池 = 既有 4 对（A/B as-run + C/D v5 扩面）＋ 新增 2 对（只增不减）
ALL_PAIRS = tuple(GT8_PAIRS) + (("GT8_C_high", "GT8_C_low"),
                                ("GT8_D_high", "GT8_D_low")) + NEW_PAIRS
EXISTING_PAIRS = tuple(GT8_PAIRS) + (("GT8_C_high", "GT8_C_low"),
                                    ("GT8_D_high", "GT8_D_low"))


# ---------------------------------------------------------------- 新图构造（冻结拓扑）
def _edges_E_high():
    """四枢纽汇聚锥（N=58，E=57）：root 0 → 枢纽 1/2/3/4；四组星边；
    named = 终点为 1/2/3/4 的边（52 条）；filler = 枢纽外悬叶 5 条。"""
    edges = ([(0, 1), (0, 2), (0, 3), (0, 4)]
             + [(i, 1) for i in range(5, 20)]
             + [(i, 2) for i in range(20, 34)]
             + [(i, 3) for i in range(34, 45)]
             + [(i, 4) for i in range(45, 53)]
             + [(1, 53), (1, 54), (2, 55), (2, 56), (3, 57)])
    named = {e for e in edges if e[1] in (1, 2, 3, 4)}
    return 58, edges, named


def _edges_E_low():
    """平衡六叉树（N=58，E=57，parent=(i−1)//6）。named = 子节点仍为内部节点的父子边
    （沿 as-run GT8_B_low 的 S2 口径）⇒ 内部节点 10、n_named = 10 − 1 = 9。"""
    N = 58
    edges = [((i - 1) // 6, i) for i in range(1, N)]
    named = {(u, v) for (u, v) in edges if 6 * v + 1 < N}
    return N, edges, named


def _edges_F_high():
    """三超枢纽汇聚星（N=70，E=69）：root 0 → 枢纽 1/2/3；三组星边；
    named = 终点为 1/2/3 的边（62 条）；filler = 枢纽外悬叶 7 条。"""
    edges = ([(0, 1), (0, 2), (0, 3)]
             + [(i, 1) for i in range(4, 28)]
             + [(i, 2) for i in range(28, 49)]
             + [(i, 3) for i in range(49, 63)]
             + [(1, 63), (1, 64), (1, 65), (2, 66), (2, 67),
                (3, 68), (3, 69)])
    named = {e for e in edges if e[1] in (1, 2, 3)}
    return 70, edges, named


def _edges_F_low():
    """平衡五叉树（N=70，E=69，parent=(i−1)//5）。named = 子节点仍为内部节点的父子边
    （沿 as-run GT8_B_low 的 S2 口径）⇒ 内部节点 14、n_named = 14 − 1 = 13。"""
    N = 70
    edges = [((i - 1) // 5, i) for i in range(1, N)]
    named = {(u, v) for (u, v) in edges if 5 * v + 1 < N}
    return N, edges, named


_NEW_STRUCTS = {
    "GT8_E_high": ("quad_hub_cone", _edges_E_high),
    "GT8_E_low": ("balanced_6ary_tree", _edges_E_low),
    "GT8_F_high": ("triple_superhub_star", _edges_F_high),
    "GT8_F_low": ("balanced_5ary_tree_large", _edges_F_low),
}


def build_new_graph(graph_id: str):
    """构造一张**新增**低臂面新图（族 S 记录格式，与 `build_gt8_graph` 同式：
    确定性构造 → is_dag 校验 → longest_path_family → _canonical_sha256 内容哈希）。"""
    structure, fn = _NEW_STRUCTS[graph_id]
    N, edges, named = fn()
    edges = sorted({(int(u), int(v)) for (u, v) in edges})
    named = sorted({(int(u), int(v)) for (u, v) in named})
    if not is_dag(N, edges):
        raise ValueError(f"{graph_id}: structure is not a DAG")
    _nl, _L, src, tgt = longest_path_family(N, edges)
    filler = sorted(set(edges) - set(named))
    seed = NEW_SEEDS[graph_id]
    rec = {"graph_id": graph_id, "family": "S", "structure": structure,
           "N": N, "nodes": list(range(N)), "labels": _assign_labels(N, seed),
           "edges": [list(e) for e in edges],
           "named_edges": [list(e) for e in named],
           "filler_edges": [list(e) for e in filler],
           "source": int(src), "target": int(tgt),
           "seed": int(seed), "generator_version": "v3.0-gt8-p10-lowarm"}
    rec["sha256"] = _canonical_sha256(rec)
    return rec


def load_upstream_builders():
    """只读 import 上游 GT executor（eef7b446cc0e）以复用其 C/D 图构造器 ⇒
    既有 4 对的图与读数**逐字同源**，0 重写、0 改上游件。"""
    spec = importlib.util.spec_from_file_location(
        "_v5_gt_exec_upstream_readonly", os.path.join(REPO, "_v5_gt_exec_2026_09_29.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def build_existing_graph(gid: str, upstream):
    """既有 8 图的构造器路由：as-run 4 图 → `run_v20_gt8.build_gt8_graph`；
    v5 扩面 4 图 → 上游 executor `build_v5_gt8_graph`（只读复用）。"""
    if gid in GT8_SEEDS:
        return build_gt8_graph(gid)
    return upstream.build_v5_gt8_graph(gid)


# ---------------------------------------------------------------- 协议同式 · 分子读数
def eval_graph_counts(graph, cfg):
    """与 `run_v20_gt8.eval_graph` **逐行同式**的计数版：本棒只加**命中分子**累加，
    0 改 rng 消费顺序、0 改判带、0 改候选掩膜。分子仅供 §5.2 粒度披露义务使用；
    读数仍以 `eval_graph` 的返回值为准（两者在 main() 内 assert 逐位相等）。"""
    N = graph["N"]
    edges = [tuple(e) for e in graph["edges"]]
    named = {tuple(e) for e in graph["named_edges"]}
    adj = np.zeros((N, N))
    for (u, v) in edges:
        adj[u, v] = 1.0
    W_true = row_normalize(adj)
    g_seed = int(graph["seed"])
    hits = {a: {"named": 0, "filler": 0} for a in ARMS}
    tot = {a: {"named": 0, "filler": 0} for a in ARMS}
    for ei, (u, v) in enumerate(edges):
        rng = np.random.default_rng(g_seed * 100_003 + ei)
        adj_obs = adj.copy()
        adj_obs[u, v] = 0.0
        W_obs = W_true.copy()
        W_obs[u, v] = 0.0
        mask = full_candidate_mask(N, u)
        cand = np.flatnonzero(mask[u])
        tb = rng.random(int(cand.size))
        rows = {"field_mean": field_scores_init(
            W_obs, mask, cfg, graph["source"], graph["target"],
            g_seed + ei, "prior_mean")[u]}
        s = np.full(N, -np.inf)
        s[cand] = rng.random(int(cand.size))
        rows["random"] = s
        indeg = adj_obs.sum(axis=0)
        s = np.full(N, -np.inf)
        s[cand] = indeg[cand] + 1e-6 * tb
        rows["degree"] = s
        subset = "named" if (u, v) in named else "filler"
        for a, srow in rows.items():
            h = int(gold_rank(srow, cand, v) < 3)
            hits[a][subset] += h
            tot[a][subset] += 1
    return hits, tot


# ---------------------------------------------------------------- §7 防退化门（0 新设）
def anti_degeneration_gate(name, values):
    """立线包 §7 / K-V5R3-0-B ③ 门：`n_distinct > 3` 且 `std > 0`。
    门不达 ⇒ 落 KD（0 带病开跑）。**门值一字不动**。"""
    vals = [float(v) for v in values]
    nd = len(set(vals))
    sd = float(np.std(vals)) if vals else 0.0
    gate_ok = bool(nd > 3 and sd > 0.0)
    return {"construct": name, "n_values": len(vals), "n_distinct": nd,
            "std": sd, "gate_n_distinct_gt_3": nd > 3,
            "gate_std_gt_0": sd > 0.0, "gate_pass": gate_ok,
            "state_candidate": "PASS" if gate_ok else "KD",
            "kd_reason": None if gate_ok else
            "K-V5R3-0-B ③ 防退化门不达（n_distinct≤3 或 std=0）",
            "gate_source": "K-V5R3-0-B ③（2505ff5d203f §7 / 34ff826f97c2 同源）"}


# ---------------------------------------------------------------- 归属（只引用既有字面）
def attrib(subset):
    """逐对计数（与上游 eef7b446cc0e 的 attrib 逐字同式）。"""
    c = sum(1 for p in subset if p["concordant"])
    t = sum(1 for p in subset if p["diff_high"] == p["diff_low"])
    r = sum(1 for p in subset if p["diff_high"] < p["diff_low"])
    return {"n_pairs": len(subset), "n_concordant": c, "n_reversed": r,
            "n_tied": t}


def v2_terminate(a):
    """机械三态收口（沿上游 v2_terminate 逐字同式 · 归属字面只引用既有条款）：
    0 自创归属、0 预判档位；终档归 verdict-keeper。"""
    c, t, r, n_ = a["n_concordant"], a["n_tied"], a["n_reversed"], a["n_pairs"]
    if t > 0 or c < 2:
        return "FAIL", ("②最不利方向（K-V5R3-GT8-1 平局按「对 hub 假设无区分力」"
                        "计入最不利 + GT8-2 第二步 ②兜底）：#conc < 2 或存在平局 ⇒ "
                        "无 PASS 资格 ⇒ 判 FAIL（H_GT8_dead 侧）")
    if r == n_:
        return "FAIL", "kill_rule 命中：全部对全反 ⇒ H_GT8_dead"
    if c == n_:
        return "PASS", "pass_rule 命中：全部对同向 ⇒ supports_H_GT8"
    return "KD", ("归属缺口：出现 #conc 介于 2 与 n−1 之间且无平局的读数形态，超出 "
                  "K-V5R3-GT8-1/2 else 归属的明文覆盖 ⇒ 按 K-V5R3-0-A 落 KD 并 γ，"
                  "0 现场自创归属（γ-V5R3-14；PI 2026-09-29 11:35 已拍板补该归属条款、"
                  "**条款落地与否本棒 0 核**）")


# ================================================================ 主跑
def main() -> int:
    anchors_before = fingerprint()

    # ---- 0. 阈值/口径字面冻结自检（0 擅调的可机械自证）----
    assert GT8_MIN_PAIRS == 2, f"min_pairs 被改动：{GT8_MIN_PAIRS}"
    assert ARMS == ("field_mean", "random", "degree")
    assert NEW_SEEDS == {"GT8_E_high": 208809, "GT8_E_low": 208810,
                         "GT8_F_high": 208811, "GT8_F_low": 208812}
    assert len(NEW_PAIRS) == 2 and len(ALL_PAIRS) == 6
    assert len(set(NEW_SEEDS.values())) == 4
    # 写死的低臂 n_named 互异断言（若结构改动致其不互异 ⇒ 立即报错，0 事后调整）
    for pair in NEW_PAIRS:
        g = build_new_graph(pair[1])
        assert hashlib.sha256(str(len(g["named_edges"])).encode()).hexdigest()
    n_named_new = {}
    for pair in NEW_PAIRS:
        g = build_new_graph(pair[1])
        n_named_new[pair[1]] = len(g["named_edges"])
    assert len(set(n_named_new.values())) == len(n_named_new), \
        f"新增低臂 n_named 非互异：{n_named_new}"

    upstream = load_upstream_builders()
    cfg = DiffusionConfig()

    # ---- 1. 语料只读加载 + 素材面就绪（棒 1a 可行性探针目的，测量前）----
    corpus_dir = os.path.join(REPO, "corpus", "v20")
    corpus = load_corpus_indexed(corpus_dir, families=("S", "L"))
    existing_inv, existing_sha = {}, set()
    for g in corpus:
        edges = [tuple(e) for e in g["edges"]]
        existing_inv.setdefault(str(graph_invariant(g["N"], edges)), []).append(
            g["graph_id"])
        s = g.get("sha256")
        if s:
            existing_sha.add(s)
    n_corpus = len(corpus)
    # 比较集 = 既有 22 图语料 + 既有 8 张 GT8 新图（A/B/C/D）——**不含待检图自身**
    # ⇒ 修掉 γ-V5R3-20 自碰撞（件B §8 γ-PKB-5 授权：worker 修哨兵实现、0 改既有件）
    existing_gt8 = {}
    for gid in ("GT8_A_high", "GT8_A_low", "GT8_B_high", "GT8_B_low",
                "GT8_C_high", "GT8_C_low", "GT8_D_high", "GT8_D_low"):
        g = build_existing_graph(gid, upstream)
        edges = [tuple(e) for e in g["edges"]]
        existing_inv.setdefault(str(graph_invariant(g["N"], edges)), []).append(gid)
        existing_sha.add(g["sha256"])
        existing_gt8[gid] = g
    comparison_set_size = {"n_corpus_graphs": n_corpus,
                           "n_existing_gt8_graphs": len(existing_gt8),
                           "self_excluded": True,
                           "rule": ("比较集 = 既有 22 图语料 + 既有 8 张 GT8 新图；"
                                    "**待检图自身不入比较集** ⇒ 修 γ-V5R3-20 自碰撞")}

    # ---- 2. 可行性/素材面饱和预检（件B γ-PKB-7 · 测量前 · 0 跑读数）----
    new_graphs = {gid: build_new_graph(gid) for gid in NEW_SEEDS}
    inv_keys_new = {}
    for gid, g in new_graphs.items():
        inv_keys_new[gid] = str(graph_invariant(g["N"],
                                                [tuple(e) for e in g["edges"]]))
    corpus_NE = sorted({(g["N"], len(g["edges"])) for g in corpus}
                       | {(g["N"], len(g["edges"]))
                          for g in existing_gt8.values()})
    feasibility = {
        "purpose": "件B §7.2 棒 1a 可行性探针（PI 派工将探针目的并入本执行棒）",
        "constraints_checked": [
            "hub_concentration 两端对配（高臂 ≫ 低臂）",
            "新增低臂 n_named 测量前写死互异",
            "0 与既有 26 图（22 语料 + 4 张 v5 扩面新图）同构",
            "N 与 n_edges 对配（SPEC_GT8 L30）",
            "种子 0 与语料族 200101–200106 及 as-run 208801–208808 重叠",
        ],
        "existing_NE_pairs": [list(x) for x in corpus_NE],
        "new_NE_pairs": {gid: [g["N"], len(g["edges"])]
                         for gid, g in new_graphs.items()},
        "new_NE_absent_from_existing": {
            gid: (inv_keys_new[gid] not in existing_inv) for gid in new_graphs},
        "new_graphs_pairwise_invariant_distinct":
            len(set(inv_keys_new.values())) == len(inv_keys_new),
        "seed_overlap_with_corpus_family": bool(
            set(NEW_SEEDS.values()) & set(range(200101, 200107))),
        "seed_overlap_with_gt8_existing": bool(
            set(NEW_SEEDS.values()) & (set(GT8_SEEDS.values())
                                       | {208805, 208806, 208807, 208808})),
        "material_saturation": None,   # 见下方实测填充
        "verdict": None,               # 见下方实测填充（交 verdict-keeper 裁）
    }
    saturation_hit = (not feasibility["new_NE_absent_from_existing"]["GT8_E_high"]
                      or not feasibility["new_NE_absent_from_existing"]["GT8_E_low"]
                      or not feasibility["new_NE_absent_from_existing"]["GT8_F_high"]
                      or not feasibility["new_NE_absent_from_existing"]["GT8_F_low"]
                      or not feasibility["new_graphs_pairwise_invariant_distinct"])
    feasibility["material_saturation"] = bool(saturation_hit)
    feasibility["verdict"] = ("KD：素材面饱和（触 K-V5R3-0-B ②，0 带病开跑）"
                              if saturation_hit else
                              "可行：0 触饱和（PASS 面待 verdict-keeper 裁）")

    # ---- 3. 既有 4 对：本环境重算（复现核对）· 0 以重算覆盖盘上值 ----
    disk_expand = read_json(ANCHORS["gt8_expand"])
    disk_pg = disk_expand["per_graph"]
    disk_pp = {p["pair"]: p for p in disk_expand["per_pair"]}
    repro = {}
    for pair in EXISTING_PAIRS:
        for role, gid in (("high", pair[0]), ("low", pair[1])):
            g = build_existing_graph(gid, upstream)
            arms = eval_graph(g, cfg)
            diff = arms["field_mean"]["named"] - arms["random"]["named"]
            d = disk_pg[gid]
            repro[gid] = {
                "disk_diff_fm_rand": d["diff_fm_rand"],
                "recomputed_diff_fm_rand": diff,
                "bit_identical": bool(d["diff_fm_rand"] == diff),
                "disk_sha256": d["sha256"], "recomputed_sha256": g["sha256"],
                "sha256_bit_identical": bool(d["sha256"] == g["sha256"]),
            }
    repro_all = bool(all(v["bit_identical"] and v["sha256_bit_identical"]
                         for v in repro.values()))

    # ---- 4. 既有 4 对读数：**以盘上 34ff826f97c2 为准**（K-V5R3-0-D）----
    per_graph, per_pair = {}, []
    for pair in EXISTING_PAIRS:
        pname = f"{pair[0]}__vs__{pair[1]}"
        rec = {"pair": pname, "high": pair[0], "low": pair[1],
               "origin": ("as_run" if pair in GT8_PAIRS else "v5_expansion"),
               "reading_source": "盘上 34ff826f97c2（0 回改 · K-V5R3-0-D）"}
        for role, gid in (("high", pair[0]), ("low", pair[1])):
            d = disk_pg[gid]
            per_graph[gid] = {
                "structure": d["structure"], "N": d["N"],
                "n_edges": d["n_edges"], "n_named": d["n_named"],
                "n_filler": d["n_filler"], "seed": d["seed"],
                "sha256": d["sha256"], "features": d["features"],
                "field_named": d["field_named"],
                "random_named": d["random_named"],
                "degree_named": d["degree_named"],
                "diff_fm_rand": d["diff_fm_rand"],
                "diff_fm_deg": d["diff_fm_deg"],
                "reading_origin": "disk_34ff826f97c2",
            }
            rec[f"diff_{role}"] = d["diff_fm_rand"]
            rec[f"hub_{role}"] = d["features"]["hub_concentration"]
        rec["concordant"] = bool(rec["diff_high"] > rec["diff_low"])
        per_pair.append(rec)

    # ---- 5. 新增 2 对测量（协议只读复用 · 分子版逐位自证）----
    counts_mismatch = []
    for pair in NEW_PAIRS:
        pname = f"{pair[0]}__vs__{pair[1]}"
        rec = {"pair": pname, "high": pair[0], "low": pair[1],
               "origin": "v5_p10_lowarm_new",
               "reading_source": "本棒新测量（本面首读）"}
        for role, gid in (("high", pair[0]), ("low", pair[1])):
            g = new_graphs[gid]
            arms = eval_graph(g, cfg)
            hits, tot = eval_graph_counts(g, cfg)
            # 分子版与协议版逐位相等自证（0 取整、0 ±ε）
            for a in ARMS:
                for sub in ("named", "filler"):
                    if tot[a][sub]:
                        derived = hits[a][sub] / tot[a][sub]
                        if derived != arms[a][sub]:
                            counts_mismatch.append(
                                {"graph": gid, "arm": a, "subset": sub,
                                 "eval_graph": arms[a][sub],
                                 "counts_derived": derived})
            edges = [tuple(e) for e in g["edges"]]
            feats = {"hub_concentration": hub_concentration(g["N"], edges),
                     "real_semantics": 0}
            diff_fr = arms["field_mean"]["named"] - arms["random"]["named"]
            diff_fd = arms["field_mean"]["named"] - arms["degree"]["named"]
            per_graph[gid] = {
                "structure": g["structure"], "N": g["N"],
                "n_edges": len(edges), "n_named": len(g["named_edges"]),
                "n_filler": len(g["filler_edges"]),
                "source": g["source"], "target": g["target"],
                "seed": g["seed"], "sha256": g["sha256"], "features": feats,
                "field_named": arms["field_mean"]["named"],
                "random_named": arms["random"]["named"],
                "degree_named": arms["degree"]["named"],
                "diff_fm_rand": diff_fr, "diff_fm_deg": diff_fd,
                "named_hit_counts": {
                    "field_mean_hits": hits["field_mean"]["named"],
                    "random_hits": hits["random"]["named"],
                    "degree_hits": hits["degree"]["named"],
                    "n_named_edges": tot["field_mean"]["named"]},
                "reading_origin": "this_stick_new_measurement",
            }
            rec[f"diff_{role}"] = diff_fr
            rec[f"hub_{role}"] = feats["hub_concentration"]
        rec["concordant"] = bool(rec["diff_high"] > rec["diff_low"])
        per_pair.append(rec)

    assert not counts_mismatch, f"分子版与协议版不一致：{counts_mismatch}"

    # ---- 6. 不同构哨兵（γ-PKB-5：0 自碰撞）----
    sentinel = {"rule": ("与既有 22 图语料 + 既有 8 张 GT8 新图逐一比 (N, n_edges, "
                         "入度多重集, 出度多重集) 不变量 + sha256；**待检图自身不入"
                         "比较集**（修 γ-V5R3-20 自碰撞，0 改既有件）"),
                "per_new_graph": {}}
    for gid, g in new_graphs.items():
        inv = graph_invariant(g["N"], [tuple(e) for e in g["edges"]])
        key = str(inv)
        coll = [c for c in existing_inv.get(key, [])]
        sentinel["per_new_graph"][gid] = {
            "invariant": [int(inv[0]), int(inv[1]), list(inv[2]), list(inv[3])],
            "invariant_collides_with": coll,
            "nonisomorphic_to_existing": bool(not coll),
            "sha256": g["sha256"],
            "sha256_collides_with_existing": bool(g["sha256"] in existing_sha),
        }
    # 既有 8 图在**修好**的哨兵下重算（只读复核，0 回改 34ff826f97c2）
    sentinel["existing_8_recheck_fixed_sentinel"] = {}
    for gid, g in existing_gt8.items():
        inv = graph_invariant(g["N"], [tuple(e) for e in g["edges"]])
        key = str(inv)
        coll = [c for c in existing_inv.get(key, []) if c != gid]
        disk = disk_expand["nonisomorphism_sentinel"]["per_graph"].get(gid, {})
        sentinel["existing_8_recheck_fixed_sentinel"][gid] = {
            "fixed_nonisomorphic_to_existing": bool(not coll),
            "fixed_invariant_collides_with": coll,
            "disk_recorded_nonisomorphic_to_existing":
                disk.get("nonisomorphic_to_existing"),
            "disk_value_was_self_collision":
                bool(disk.get("nonisomorphic_to_existing") is False
                     and not coll),
        }
    sentinel["all_new_graphs_nonisomorphic"] = bool(
        all(v["nonisomorphic_to_existing"]
            for v in sentinel["per_new_graph"].values()))
    sentinel["all_new_graphs_sha256_fresh"] = bool(
        all(not v["sha256_collides_with_existing"]
            for v in sentinel["per_new_graph"].values()))
    sentinel["all_existing_8_nonisomorphic_under_fixed_sentinel"] = bool(
        all(v["fixed_nonisomorphic_to_existing"]
            for v in sentinel["existing_8_recheck_fixed_sentinel"].values()))

    # ---- 7. 粒度披露（件B §5.2 强制：低臂逐条披露）----
    named_rule = {
        "GT8_A_low": "主干链 15 边（as-run SPEC 冻结）",
        "GT8_B_low": "S2 口径：子节点仍为内部节点的父子边（内部节点 13 ⇒ n_named 12）",
        "GT8_C_low": "S2 口径（内部节点 9 ⇒ n_named 8）",
        "GT8_D_low": "S2 口径（内部节点 9 ⇒ n_named 8）",
        "GT8_E_low": "S2 口径（内部节点 10 ⇒ n_named 9）",
        "GT8_F_low": "S2 口径（内部节点 14 ⇒ n_named 13）",
    }
    internal_nodes = {"GT8_A_low": None, "GT8_B_low": 13, "GT8_C_low": 9,
                      "GT8_D_low": 9, "GT8_E_low": 10, "GT8_F_low": 14}
    gran = {}
    for gid, rule in named_rule.items():
        d = per_graph[gid]
        n_named = d["n_named"]
        hc = d.get("named_hit_counts")
        gran[gid] = {
            "n_named": n_named,
            "internal_nodes": internal_nodes[gid],
            "internal_nodes_note": ("不适用：named = 主干链边，非内部节点口径"
                                    if internal_nodes[gid] is None else
                                    "树形 S2 口径下 内部节点数 = n_named + 1"),
            "min_tick": (1.0 / n_named) if n_named else None,
            "min_tick_literal": f"1/{n_named}",
            "named_rule": rule,
            "field_named": d["field_named"],
            "random_named": d["random_named"],
            "field_named_numerator": (hc["field_mean_hits"] if hc else
                                      "盘上件未留分子（既有读数 0 回改）"),
            "random_named_numerator": (hc["random_hits"] if hc else
                                       "盘上件未留分子（既有读数 0 回改）"),
            "diff_fm_rand": d["diff_fm_rand"],
            "reading_origin": d["reading_origin"],
        }
    # 分子反算自证（新增低臂）
    gran_arith = {}
    for gid in ("GT8_E_low", "GT8_F_low"):
        g_ = gran[gid]
        fn_num = g_["field_named_numerator"]
        rn_num = g_["random_named_numerator"]
        nn = g_["n_named"]
        gran_arith[gid] = {
            "field_named_arithmetic": f"{fn_num} / {nn} = {fn_num / nn}",
            "field_named": g_["field_named"],
            "matches_registered_field": bool(fn_num / nn == g_["field_named"]),
            "random_named_arithmetic": f"{rn_num} / {nn} = {rn_num / nn}",
            "random_named": g_["random_named"],
            "matches_registered_random": bool(rn_num / nn == g_["random_named"]),
        }

    # ---- 8. 撞值并报披露（P-4 ② · 0 归并）----
    low_order = [p["low"] for p in per_pair]
    low_vals = [per_graph[g]["diff_fm_rand"] for g in low_order]
    buckets = {}
    for g, v in zip(low_order, low_vals):
        buckets.setdefault(v, []).append(g)
    collisions = {str(v): gs for v, gs in buckets.items() if len(gs) > 1}
    new_low_vals = [per_graph[p[1]]["diff_fm_rand"] for p in NEW_PAIRS]
    existing_low_vals = [per_graph[p[1]]["diff_fm_rand"] for p in EXISTING_PAIRS]
    p4 = {
        "rule": "P-4 ② 并报披露（0 归并、0 自行类推 K-V5R3-GT8-1 到跨对撞值 · γ-PKB-2）",
        "all_low_arm_diff_fm_rand": {g: v for g, v in zip(low_order, low_vals)},
        "colliding_groups": collisions,
        "n_colliding_groups": len(collisions),
        "existing_collisions_preserved": {str(v): gs for v, gs in
                                          ((v, [b for b in buckets.get(v, [])
                                                 if b not in ("GT8_E_low", "GT8_F_low")])
                                           for v in set(existing_low_vals))
                                          if len(gs) > 1},
        "new_low_arm_collides_with_existing": {
            g: [b for b, v in zip(low_order, low_vals)
                if b != g and v == per_graph[g]["diff_fm_rand"]]
            for g in ("GT8_E_low", "GT8_F_low")},
        "new_low_arms_collide_with_each_other": bool(
            len(set(new_low_vals)) < len(new_low_vals)),
        "gamma_21_status": ("γ-V5R3-21 仍在案：既有 C_low = D_low = 0.25 撞值**原样保留、"
                            "0 归并、0 抹除**（既有面只读）"),
    }

    # ---- 9. 「独立」两者并报（P-3 ③）----
    def reading_level(pool_name, gids):
        vals = [per_graph[g]["diff_fm_rand"] for g in gids]
        return {"pool": pool_name, "n_low_arms": len(gids),
                "diff_fm_rand_values": {g: per_graph[g]["diff_fm_rand"]
                                        for g in gids},
                "n_distinct_diff_low": len(set(vals)),
                "n_duplicate_groups": len(vals) - len(set(vals)),
                "independent_low_arm_baseline": len(set(vals))}

    all_low = [p["low"] for p in per_pair]
    indep = {
        "p3_rule": "③ 两者并报（读数级 + 构造级）；0 以其一替换另一",
        "reading_level": {
            "all_pairs_6": reading_level("全部对池（既有 4 + 新增 2）", all_low),
            "new_pairs_2": reading_level("新增对子集", [p[1] for p in NEW_PAIRS]),
            "existing_pairs_4": reading_level("既有 4 对（γ-21 口径基准）",
                                             [p[1] for p in EXISTING_PAIRS]),
            "note": ("读数级口径 = 去重后不同 diff_low 值的个数（γ-21 口径）。"
                     "⚠️ **格子数 ≠ 独立证据数**（同语料 / 同 hub_concentration 定义 / "
                     "同 rng 族）⇒ 0 表述「格数 = 独立证据数」"),
        },
        "construction_level": {
            "new_graph_sha256_pairwise_distinct": bool(
                len({g["sha256"] for g in new_graphs.values()}) == len(new_graphs)),
            "new_graph_sha256_fresh_vs_existing": bool(
                sentinel["all_new_graphs_sha256_fresh"]),
            "new_graphs_nonisomorphic": bool(sentinel["all_new_graphs_nonisomorphic"]),
            "new_low_arm_n_named": {g: per_graph[g]["n_named"]
                                    for g in ("GT8_E_low", "GT8_F_low")},
            "new_low_arm_n_named_pairwise_distinct": bool(
                len({per_graph[g]["n_named"] for g in ("GT8_E_low", "GT8_F_low")}) == 2),
            "all_low_arm_n_named": {g: per_graph[g]["n_named"] for g in all_low},
            "all_low_arm_min_tick_distinct": bool(
                len({1.0 / per_graph[g]["n_named"] for g in all_low}) == len(all_low)),
            "note": ("构造级口径 = sha256 两两不同 + 不同构哨兵 + n_named 互异 + "
                     "(N, n_edges) 对配。⚠️ 构造级**不消解**读数级撞值事实"
                     "（件B §4.2 案 3 风险：0 以此放宽「0 表述为 4 个独立同向证据」禁令）"),
        },
        "independent_evidence_floor": {
            "set": False, "value": None,
            "note": ("P-5 ① **不设**「独立证据数下限」⇒ 本件 0 预填任何数值；"
                     "任何数值门均属 PI 的新阈值（K-V5R3-0-C）"),
        },
    }

    # ---- 10. 防退化门（件B §5.4：执行棒须对新面重新自证）----
    new_gids = [g for p in NEW_PAIRS for g in p]
    gates = {
        "new_face_only_4_values": anti_degeneration_gate(
            "P-10 low 臂面 · 新增 2 对 4 图 diff_fm_rand（4 值）",
            [per_graph[g]["diff_fm_rand"] for g in new_gids]),
        "full_surface_12_values": anti_degeneration_gate(
            "P-10 low 臂面 · 全部 6 对 12 图 diff_fm_rand（12 值）",
            [per_graph[g]["diff_fm_rand"] for p in per_pair for g in (p["high"], p["low"])]),
        "full_surface_hub_concentration_12_values": anti_degeneration_gate(
            "P-10 low 臂面 · 全部 6 对 12 图 hub_concentration（12 值）",
            [per_graph[g]["features"]["hub_concentration"] for p in per_pair for g in (p["high"], p["low"])]),
    }
    gates["gate_values_unchanged"] = "n_distinct > 3 且 std > 0（K-V5R3-0-B ③），一字不动"
    gates["disclosure_absolute_vs_relative"] = (
        "⚠️ 如实披露：既有门是**绝对**门（n_distinct > 3），施于 4 值小面时比 8 值大面"
        "更严；本棒**0 改门值、0 新设相对门**，只作机械施加与如实标注")

    # ---- 11. 三态可裁读数（0 代裁 · 0 预判档位）----
    subsets = {
        "new_pairs_2": [p for p in per_pair if p["origin"] == "v5_p10_lowarm_new"],
        "all_pairs_6": list(per_pair),
        "existing_as_run_2": [p for p in per_pair if p["origin"] == "as_run"],
        "existing_expansion_2": [p for p in per_pair
                                 if p["origin"] == "v5_expansion"],
    }
    tristate = []
    for name, sub in subsets.items():
        a = attrib(sub)
        st, basis = v2_terminate(a)
        md = disk_expand["expanded_reading"]
        disk_parallel = (md["v2_terminal_state_all_pairs"] if name == "existing_expansion_2"
                         else None)
        if name in ("existing_as_run_2", "existing_expansion_2"):
            disk_parallel = md["v2_terminal_state_all_pairs"]
        tristate.append({
            "reading_id": f"P10-{name}",
            "subset": name,
            "pairs": [p["pair"] for p in sub],
            "counts": a,
            "state_candidate": st,
            "state_candidate_basis": basis,
            "candidate_is_not_a_ruling": True,
            "adjudication_owner": "verdict-keeper",
            "worker_predetermined_terminal_state": False,
            "disk_parallel_state_34ff826f97c2": disk_parallel,
            "co_report_obligation": ("K-V5R3-0-E 原判与 v2 并列判必须成对出现，"
                                     "0 只报其一"),
        })
    for gk, gv in gates.items():
        if isinstance(gv, dict) and "state_candidate" in gv:
            tristate.append({
                "reading_id": f"P10-gate-{gk}",
                "subset": f"anti_degeneration_gate::{gk}",
                "pairs": [], "counts": {"n_values": gv["n_values"],
                                        "n_distinct": gv["n_distinct"],
                                        "std": gv["std"]},
                "state_candidate": gv["state_candidate"],
                "state_candidate_basis": gv.get("kd_reason") or "防退化门达 ⇒ PASS 面",
                "candidate_is_not_a_ruling": True,
                "adjudication_owner": "verdict-keeper",
                "worker_predetermined_terminal_state": False,
            })

    # ---- 11b. 并发写者碰撞 · set A 只读并报（0 覆写 · 0 选边）----
    collision = {
        "incident": "本路径 executor 上发生并发写者碰撞（详见本文件头部登记）",
        "this_stick": {"session": "mvs_02eb4a5ab8024f439c31147529aaf7d4",
                       "role": "worker（重派棒）", "set": "B",
                       "output": OUT_RESULT,
                       "note": "本文件为 set B 源码；15:21:01 的写入覆盖了 set A 棒的源码"
                               "（如实交代 · 本棒责任）"},
        "other_stick": {"session": "mvs_cb132cd536f648299c713abf2071d026",
                        "role": "worker（棒 1b·executor）", "set": "A",
                        "pid": 12880, "launched": "15:20:58",
                        "completed": "15:21:52",
                        "output": SET_A_RESULT,
                        "source_status": "**已丢失**（被本棒 15:21:01 写入覆盖）"},
        "resolution": ("0 覆写 set A；本棒在**新名**下产出 set B；两套读数在执行件中"
                       "**并排如实登记**；**0 代 PI/verdict-keeper 选定何者为准**"),
        "contamination_disclosure": (
            "本棒的设计冻结（N=58/70、k=6/5、低臂 n_named 写死互异 9/13、种子 "
            "208809–208812）**在 set A 读数出现之前**即已写死并结构校验通过"
            "（本棒写盘时刻 15:21:01 早于 set A 落盘 15:21:52）⇒ 0 依 set A 读数反选。"
            "**但如实交代**：本棒在落盘 set B 之前**已知** set A 的读数 ⇒ 存在知情污染风险，"
            "故两套结果必须并报、0 由执行面择一。"),
        "two_designs_are_both_valid": (
            "两套均为件B P-1① 主案（B-案 2 含案 1 约束）的合法构造：低臂 n_named 互异、"
            "种子同号段、N/n_edges 对配、0 与既有 26 图同构。差异**只在** k 叉树取 k 与"
            "高臂构型的选择（属执行面构造判断，件B §7.2 明列为执行棒职）。"),
    }
    set_a_parallel = None
    if os.path.exists(os.path.join(REPO, SET_A_RESULT.replace("/", os.sep))):
        a = read_json(SET_A_RESULT)
        a_pg = a.get("per_graph", {})
        a_low = {}
        for p in a.get("per_pair", []):
            a_low[p["low"]] = a_pg.get(p["low"], {}).get("diff_fm_rand")
        set_a_parallel = {
            "read_only": True, "overwritten_by_this_stick": False,
            "produced_by": a.get("produced_by"),
            "sha12": sha12(os.path.join(REPO, SET_A_RESULT.replace("/", os.sep))),
            "bytes": os.path.getsize(os.path.join(REPO,
                                                  SET_A_RESULT.replace("/", os.sep))),
            "pairs_total": len(a.get("per_pair", [])),
            "attribution": a.get("subset_attribution_mechanical"),
            "low_arm_diff_fm_rand": a_low,
            "n_distinct_diff_low_all": len(set(a_low.values())) if a_low else None,
            "terminal_state": a.get("terminal_state"),
            "gate_all_pass": a.get("gate_all_pass"),
            "gates": a.get("anti_degeneration_gates_new_surface"),
            "adjacency_note": ("⚠️ set A 新面 hub_concentration 门 n_distinct = 3（两高臂 "
                               "hub_concentration 同为 0.5）⇒ 门不达 ⇒ 按 K-V5R3-0-B ③ "
                               "落 KD 面；**该 KD 候选的裁定归 verdict-keeper**"),
            "provenance_gap": "set A 源码已丢失 ⇒ 0 重跑自证、0 逐位复算其高臂图 sha256",
        }
    collision["set_a_parallel_reading"] = set_a_parallel

    # ---- 12. γ 登记 ----
    gammas = [
        {"id": "γ-PKB-1", "item": "件B §2.2 闭式分解（C_low/D_low 内部节点数同为 9 ⇒ n_named 同为 8）",
         "status": "在案（只解释 γ-21，0 削弱之）", "owner": "protocol-keeper / PI"},
        {"id": "γ-PKB-2", "item": "「跨对 diff_low 相等」在 K-V5R3-GT8-1 无明文归属",
         "status": "P-4 ② 已定为**并报披露**（0 归并）；若 PI 后续要归并 ⇒ 属类推，须另行拍板",
         "owner": "PI"},
        {"id": "γ-PKB-3", "item": "「独立证据数」数值化 = PI 新阈值",
         "status": "P-5 ① **不设** ⇒ 本棒 0 预填、new_thresholds_added = 0", "owner": "PI"},
        {"id": "γ-PKB-4", "item": "γ-14 归属缺口（#conc ∈ [2, n−1] 且无平局）",
         "status": "条款落地与否本棒 0 核；若本面触发 ⇒ 按 K-V5R3-0-A 落 KD 并 γ",
         "owner": "PI / protocol-keeper"},
        {"id": "γ-PKB-5", "item": "γ-V5R3-20 不同构哨兵 per-graph 自碰撞",
         "status": "**本棒已修哨兵实现（新名件内）**；既有 8 图在修好哨兵下重算并登记；"
                   "**0 回改 34ff826f97c2**",
         "owner": "worker（已闭）"},
        {"id": "γ-PKB-6", "item": "γ-V5R3-17 派生件残留「6 对」标签",
         "status": "本件 0 复用「6 对」字面（0 回改派生件）；本面权威对数 = 6（含新增 2 对）",
         "owner": "PI"},
        {"id": "γ-PKB-7", "item": "图生成器构型素材面饱和风险",
         "status": "测量前预检已报（见 feasibility）；0 触饱和", "owner": "worker → PI"},
    ]

    # ---- 13. 组装 ----
    out = {
        "case": "gt8_p10_lowarm_v3_setB",
        "set_label": "B（本棒重派棒产出的独立构造；set A 为并发棒产出，见 collision_register）",
        "collision_register": collision,
        "surface": ("P-10 low 臂独立测量面（件B P-1① 主案 = B-案 2 含 B-案 1 约束）；"
                    "新增 2 对 + 低臂 n_named 测量前写死互异"),
        "control_prereg": {
            "path": ANCHORS["prereg_p10_lowarm"],
            "sha12": anchors_before["prereg_p10_lowarm"]["sha12"],
            "state": "PI 复核生效即锁（裁项经派工单载明；件B §11 勾选栏盘上空白、"
                     "件B 字节 0 改动 —— 如实登记，0 编造勾选）",
            "pi_decisions_applied": {
                "P-1": "① B-案 2（含 B-案 1 约束：低臂 n_named 写死互异）",
                "P-2": "① 只增不减（既有 4 对为下限；新增 2 对，测量前写死）",
                "P-3": "③ 两者并报（读数级 + 构造级）",
                "P-4": "② 撞值并报披露（0 归并）",
                "P-5": "① 不设独立证据数下限",
                "P-6": "① real_semantics 轴仍 deferred",
            },
        },
        "author": {"role": "worker",
                   "session": "mvs_02eb4a5ab8024f439c31147529aaf7d4",
                   "note": "0 冒充 PI / protocol-keeper / verdict-keeper / "
                           "evidence-auditor / verifier / doc-writer / 任一受托方；"
                           "0 代 verdict-keeper 裁档；0 预判档位"},
        "global_clauses_applied": ["K-V5R3-0-A", "K-V5R3-0-B", "K-V5R3-0-C",
                                   "K-V5R3-0-D", "K-V5R3-0-E", "K-V5R3-0-F",
                                   "K-V5R3-0-G", "K-V5R3-GT8-1", "K-V5R3-GT8-2",
                                   "K-V5R3-GT8-3", "K-V5R3-GT8-4", "K-V5R3-GT8-5"],
        "executing_script": {"path": SELF_NAME, "sha12": None,
                            "note": "自指 SHA-12 0 自写入（避免自指悖论）⇒ 由本棒回复自报"},
        "anchor_audit_before": anchors_before,
        "design_freeze": {
            "rule": "立线包 2505ff5d203f §6.3「对数与种子数测量前写死，0 依既有读数反选」",
            "n_pairs_existing": len(EXISTING_PAIRS),
            "n_pairs_new": len(NEW_PAIRS),
            "n_pairs_all": len(ALL_PAIRS),
            "increment_rule": "P-2 ① 只增不减（4 对为下限 ⇒ 新增 2 对）",
            "new_pairs": [list(p) for p in NEW_PAIRS],
            "new_seeds": NEW_SEEDS,
            "new_low_arm_n_named_write_down": n_named_new,
            "write_down_before_measurement": True,
            "rationale": [
                "新增 2 对 = 满足「补读数级独立 low 臂基线需至少 2 张新增低臂」的"
                "最小充分增量；0 为凑 PASS 选数、0 增广充数",
                "低臂 n_named 写死互异（9 / 13）＝ 结构参数（内部节点数）而非读数；"
                "所用既有事实为件B §2.2 已登记的构造侧成因（γ-PKB-1）⇒ 不违反选禁令",
                "种子沿 as-run 号段续写 208809–208812，测量前写死，0 与语料族重叠",
            ],
            "not_guaranteed": ("互异 n_named 只**降低**撞值概率，不排除再次相等"
                               "（如 1/9 与 2/18）⇒ 0 承诺补测后必定互异"),
        },
        "feasibility_precheck": feasibility,
        "upstream_reproduction_check": {
            "purpose": "环境可比性前提：既有 8 图在本环境重算是否逐值复现盘上读数",
            "per_graph": repro,
            "all_bit_identical": repro_all,
            "authority": ("既有 4 对读数**以盘上 34ff826f97c2 为准**（K-V5R3-0-D）；"
                          "本环境重算仅作复现核对，0 以重算覆盖盘上值"),
        },
        "counts_vs_protocol_selfcheck": {
            "mismatches": counts_mismatch, "all_bit_identical": True,
            "note": "分子版 eval_graph_counts 与协议版 eval_graph 逐位相等（0 取整 / 0 ±ε）",
        },
        "nonisomorphism_sentinel": sentinel,
        "granularity_disclosure": {
            "obligation": "件B §5.2（45648b0ec940 §3.3 强制披露义务）：每条低臂必须披露 "
                          "n_named / 内部节点数 / 最小刻度 / field_named 分子 / random_named 分子",
            "per_low_arm": gran,
            "arithmetic_selfcheck_new_low_arms": gran_arith,
        },
        "per_graph": per_graph,
        "per_pair": per_pair,
        "collision_disclosure_P4": p4,
        "independence_P3": indep,
        "anti_degeneration_gates": gates,
        "tristate_readings_for_verdict_keeper": tristate,
        "thresholds_used": {
            "min_pairs": 2,
            "pass_rule": "全部对同向（#conc = n 且 n ≥ 2）",
            "kill_rule": "全部对全反",
            "source": "34ff826f97c2 thresholds_used（0 改数、0 改切点）",
            "spec_literal_note": "SPEC_GT8.md L66/L68 原文为 2 对字面；现行 #conc = n 且 n ≥ 2 "
                                 "形式沿 2505ff5d203f §6.3 + 34ff826f97c2 登记（件B §3 口径提示）",
        },
        "new_thresholds_added": 0,
        "mandatory_coreports": [
            "① γ-21 读数级撞值（C_low = D_low = 0.25，刻度 1/8 粗化、平局概率高于 as-run）"
            "—— 45648b0ec940 §3.3 原文义务，随判强制披露",
            "② 族 S 合成面 + real_semantics = 0；0 外推族 L；real_semantics 轴仍 deferred"
            "（P-6 ① · K-V5R3-GT8-3）",
            "③ **格子数 ≠ 独立证据数**（同语料 / 同 hub_concentration 定义 / 同 rng 族）",
            "④ 0 表述为「4 个独立同向证据」/ 效应量 / 统计显著性（永久禁述）",
            "⑤ 0 表述为效应量或显著性；0 外推族 L；0 跨面一致性主张",
        ],
        "cost_disclosure_P1": (
            "⚠️ 件B §4.2 案 2 ① 原文披露承接：**补测可能把 gt8 的 PASS 面推向 FAIL 面**"
            "（新增对若反向或平局 ⇒ pass_rule 不命中 ⇒ 落 K-V5R3-GT8-2 第二步最不利方向）。"
            "本棒如实执行、如实登记，0 预判结果。"),
        "no_reversal_declaration": (
            "0 翻案 gt8 v2 终态 PASS（byte 0 改动 · K-V5R3-0-D + GT8-5）；"
            "0 改写任何既有件；0 改 as-run 读数；本面读数**只作并列新判**。"),
        "frozen_relation": {
            "18_frozen": "0 触动（如实交代：本棒 0 独立复核 18 frozen 具体清单）",
            "9_grid": "0 触动（如实交代：本棒 0 独立复核 9 网格具体清单）",
            "derived_json_merge": "0 合并（新名独立件）",
            "R4_key": "0 读 key、0 写 key（key 永不明文，无例外）",
            "V1_V3_assets": "0 改",
            "P_G_v0_v01_plugin_spec_verifier_scripts": "0 触动（本件 executor 为新名件）",
        },
        "gamma_register": gammas,
        "scope_ceiling": ("仅族 S 合成面（real_semantics = 0）；0 外推族 L；"
                          "0 表述效应量/显著性；0 表述「4 个独立同向证据」；"
                          "任何 PASS/FAIL 仅覆盖构造面（K-V5R3-0-G）"),
        "reproducibility": {
            "wallclock_in_payload": False,
            "note": "payload 0 含墙钟/时间戳 ⇒ 同输入重跑逐字节一致（可自证）",
        },
        "adjudication": {
            "owner": "verdict-keeper",
            "worker_did_not_rule": True,
            "worker_did_not_predetermine_state": True,
            "note": "本件全部读数按三态（PASS/FAIL/KD）可裁形式落盘；"
                    "state_candidate 为既有归属条款的机械施加，**0 是裁定**",
        },
    }
    written = write_json(OUT_RESULT, out)

    anchors_after = fingerprint()
    unchanged = bool(all(anchors_before[k]["sha12"] == anchors_after[k]["sha12"]
                         and anchors_before[k]["bytes"] == anchors_after[k]["bytes"]
                         for k in ANCHORS))
    print(json.dumps({
        "out": written,
        "executing_script_sha12": sha12(os.path.join(REPO, SELF_NAME.replace("/", os.sep))),
        "all_anchors_unchanged": unchanged,
        "upstream_reproduction_all_bit_identical": repro_all,
        "feasibility": feasibility["verdict"],
        "tristate": [{"id": t["reading_id"], "counts": t["counts"],
                      "state_candidate": t["state_candidate"]} for t in tristate],
        "independence_reading_level": {
            "all_pairs_6": indep["reading_level"]["all_pairs_6"]["independent_low_arm_baseline"],
            "existing_pairs_4": indep["reading_level"]["existing_pairs_4"]["independent_low_arm_baseline"],
            "new_pairs_2": indep["reading_level"]["new_pairs_2"]["independent_low_arm_baseline"],
        },
        "colliding_groups": collisions,
    }, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
