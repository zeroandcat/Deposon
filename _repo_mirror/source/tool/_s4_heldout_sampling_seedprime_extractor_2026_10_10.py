#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CH-D 替代留出集抽取器（seed′ 之可审实现）· 2026-10-10
================================================================================
件性质：可审实现脚本（executable implementation of the FROZEN spec）——依
  · `_g5_ccp_execution_prereqs_2026_10_10.md`（ab1a07ae2fd1）§4-1 之 R0–R7
  · `_s4_heldout_sampling_caliber_ruling_2026_10_09.md`（fb1b696de1d6）§5 伪码
  · `_g5_ccp_seed_designation_revision_2026_10_10.md`（b53f40abb90b）§2 之 seed′
三项逐字实现；**0 改一字**。

自审门（FTFB 之等价实现 · 本脚本内置）：
  · 门 A（域校验）    输入域 ＝ results/ 全域 *addendum*.json，逐件 SHA-256／bytes／
                       supplements 之长度须与 fb1b696de1d6 §5.1 登记值逐件全等。
                       任一不等 ⇒ print("ABORT: domain mismatch") + sys.exit(2)。
  · 门 B（seed42 自审）以 seed=42 复跑同一实现，26 件须与现集
                       `_s4_heldout_sampling_seed42_items_2026_10_09.json`（6a670e629dca）
                       **逐件全等**（R1 键序、per_cell、指纹）。
                       不等 ⇒ print("ABORT: seed42 self-audit failed") + sys.exit(3)，
                       ⛔ 0 继续抽取新集（实现有误即停手）。
  门 B 通过后，方以 seed′ 抽取新集并落盘。

执行：
  python results/_s4_heldout_sampling_seedprime_extractor_2026_10_10.py
  （在 repo 根目录执行；仅读 inputs，仅写本脚本自身之 JSON 产出）

R0–R7（本文件之实现映射，逐条对应）：
  R0 域    ＝ 同一 S4 冻结面 179 行（results/ 之 21 件 *addendum*.json）。
  R1 排序  ＝ 件名【字节序 utf-8 bytes 升序】× 件内 #idx 升序（0 基）。
  R2 RNG   ＝ np.random.RandomState(seed) —— legacy MT19937 · **全局单流** ·
             ⛔ 0 逐格重播/派生；⛔ 0 换家族（0 default_rng / 0 PCG64）。
  R3 取法  ＝ rng.shuffle(候选副本) → 取前 k；⛔ 0 choice/sample/permutation 等價改写。
  R4 序    ＝ 格序 b→s→o 升序；**k=0 之格 0 次抽取**（⛔ 0 对其调用 shuffle）。
  R5 取量  ＝ k = math.floor(0.30·n)，双轨校验 (3n)//10；⛔ 0 round/ceil/max(1,·)。
  R6 落面  ＝ selected 与全域 heldout_rows 均按 R1 键字节序升序；指纹 ＝
             sha256(R1 序 "file#idx" 以 "|" 连接)[:12]。
  R7 种子  ＝ seed′ = 1830975565（全域单一种子值；⛔ 0 逐格派生、0 加格号偏移）。

硬约束（本脚本遵行）：
  ⛔ 0 手工挑选 / 0 由读数反推：seed′ 系公式输出，0 用任何读数。
  ⛔ 0 判档 / 0 代裁 / 0 宣告主案成立：只做「抽取＋登记」，判定与裁决归他棒。
  ⛔ 0 回改任何既有件：本脚本 0 编辑既有件。
  ⛔ 0 网络 / 0 skill / 0 LLM / 0 端点 / 0 key：纯本机只读计算。
  ⛔ 0 触及 〔本地绝对路径·脱敏略:�〕�人资料\\〔归档区〕。
  ⛔ 0 贴 dataset 内部文本字段（reasoning_full / scene_verbatim /
     pi_answer_verbatim）：产出件只载 (file, idx, q_id, cell) 等标识面。
"""

import hashlib
import json
import math
import os
import sys
import zlib

import numpy as np

# ---------------------------------------------------------------- 配置（R0/R7）
HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.abspath(os.path.join(HERE, os.pardir, "results"))
REPO_RESULTS = r"〔目录引用·未上传:results〕"

SEED_BASE = 42            # 门 B 自审用（现集之种子）
SEED_PRIME = 1830975565   # R7 正式抽取用（PI 已裁「照采」，b53f40abb90b §2-1）
RATIO = 0.30

OUT_ITEMS_JSON = os.path.join(
    REPO_RESULTS, "_s4_heldout_sampling_seedprime_items_2026_10_10.json"
)
CURRENT_ITEMS_JSON = os.path.join(
    REPO_RESULTS, "_s4_heldout_sampling_seed42_items_2026_10_09.json"
)

# 裁定 fb1b696de1d6 §5.1 之输入域登记（21 件 · 字节序）——用于门 A 逐件全等校验。
DOMAIN_REGISTERED = [
    ("_r_pair_addendum_2026_10_09.json", "cebc2f6ef5ec", 110510, 8),
    ("_s4_open_questions_addendum_2026_10_09.json", "4378dcc20624", 35215, 4),
    ("_s4_substrate_topup_addendum_2026_10_09.json", "1780542f0014", 85861, 18),
    ("_v4_pi_cot_v2_dataset_addendum_2026_09_24.json", "172093a23e4b", 4103, 3),
    ("_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json", "439721007aaf", 6132, 4),
    ("_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json", "41d6c28ca87c", 7566, 4),
    ("_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json", "99c58906f792", 6666, 4),
    ("_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json", "c6d092f77932", 7668, 4),
    ("_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json", "26f110a6e571", 10257, 4),
    ("_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json", "6e104e2db038", 11589, 4),
    ("_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json", "d96b747bfc6c", 14722, 4),
    ("_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json", "401bd614cdf7", 19615, 4),
    ("_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json", "cbf60a630c9f", 20194, 5),
    ("_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json", "6eed9acdb99a", 18714, 0),
    ("_v4_pi_cot_v3_dataset_addendum_d5_2026_09_27.json", "990c0c42a6f6", 16587, 2),
    ("_v4_pi_cot_v3_dataset_addendum_d6_2026_09_28.json", "9669efa804b7", 19214, 2),
    ("_v4_pi_cot_v3_dataset_addendum_d6b_2026_09_28.json", "5d94a8617b5b", 27009, 2),
    ("_v4_pi_cot_v3_dataset_addendum_d8_bhalf_2026_09_30.json", "b02ef31f1e4e", 58581, 3),
    ("_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json", "769ef8b71462", 374072, 93),
    ("_v4_pi_cot_v3_dataset_addendum_s3_d1fill_2026_10_01.json", "b9026cbf5ca2", 46909, 6),
    ("_v4_pi_cot_v3_dataset_addendum_s3_d7_2026_09_29.json", "c0ebbd1f4633", 17252, 1),
]


# ------------------------------------------------------- R0 · 域读取（只读）
def sha12_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()[:12]


def load_domain():
    """R0 · 读取 results/ 全域 *addendum*.json（只读）。"""
    files = sorted(
        [f for f in os.listdir(REPO_RESULTS) if f.endswith(".json") and "addendum" in f],
        key=lambda x: x.encode("utf-8"),  # R1 · 显式字节序（⛔ 0 collation）
    )
    per_file = {}
    total_rows = 0
    for name in files:
        p = os.path.join(REPO_RESULTS, name)
        with open(p, "r", encoding="utf-8") as f:
            data = json.load(f)
        sup = data.get("supplements", [])
        if not isinstance(sup, list):
            raise SystemExit("ABORT: supplements not a list in %s" % name)
        per_file[name] = sup
        total_rows += len(sup)
    return files, per_file, total_rows


def domain_gate(files, per_file):
    """门 A · 逐件 SHA-256／bytes／supplements 长度须与 §5.1 登记逐件全等。"""
    reg = {n: (s, b, c) for (n, s, b, c) in DOMAIN_REGISTERED}
    if len(files) != 21:
        print("ABORT: domain file count %d != 21" % len(files))
        sys.exit(2)
    if set(files) != set(reg):
        print("ABORT: domain file set mismatch")
        sys.exit(2)
    rows = 0
    for name in files:
        p = os.path.join(REPO_RESULTS, name)
        s12 = sha12_of(p)
        b = os.path.getsize(p)
        c = len(per_file[name])
        rows += c
        exp = reg[name]
        if s12 != exp[0] or b != exp[1] or c != exp[2]:
            print(
                "ABORT: domain mismatch %s got sha12=%s bytes=%d supp=%d expected %s"
                % (name, s12, b, c, exp)
            )
            sys.exit(2)
    if rows != 179:
        print("ABORT: total rows %d != 179" % rows)
        sys.exit(2)
    return {"files": 21, "event_rows": rows}


# ------------------------------------------------------- 分格键（§5.2 · 0 改）
def cell_of(ev):
    """fb1b696de1d6 §5.2 分格键——逐字复刻（0 补值、0 剔除）。"""
    scene = ev.get("scene_tag", "") or ""
    opt = ev.get("option_chosen", "") or ""
    s = zlib.crc32(scene.encode("utf-8")) % 8
    o = zlib.crc32(opt.encode("utf-8")) % 8
    m = ev.get("is_correction", False)
    b = 1 if (
        (isinstance(m, str) and (m.endswith("_pair_pending") or m == "R_pair"))
        or (m is True)
    ) else 0
    return (b, s, o)


# --------------------------------- R1 候选表 ＋ R5 取量 + R2/R3/R4 抽取（R6 落面）
def build_candidates(files, per_file):
    """R1 · 候选表：rows = [(f, i)]，按 (件字节序, idx 升序)；逐格候选表。"""
    rows = []
    for f in files:
        for i in range(len(per_file[f])):
            rows.append((f, i))
    # 平局：179 (file, idx) 对唯一 ⇒ 结构上无平局。
    if len(set(rows)) != len(rows):
        print("ABORT: duplicate (file, idx) key")
        sys.exit(2)
    candidates = {}
    for (b, s, o) in [(b_, s_, o_) for b_ in (0, 1) for s_ in range(8) for o_ in range(8)]:
        cell_rows = []
        for (f, i) in rows:
            if cell_of(per_file[f][i]) == (b, s, o):
                cell_rows.append((f, i))
        candidates[(b, s, o)] = cell_rows
    return rows, candidates


def r1_key(item):
    """R1 键字节序（落面序）。"""
    f, i = item
    return (f.encode("utf-8"), i)


def take_amount(n):
    """R5 · k = floor(0.30·n)，双轨 (3n)//10；0 round/ceil/max(1,·)。"""
    k = math.floor(RATIO * n)
    assert k == (3 * n) // 10, "R5 dual-track divergence at n=%d" % n
    return k


def extract(candidates, seed):
    """R2+R3+R4+R5+R6 · 全局单流抽取，落面按 R1 键字节序升序。"""
    rng = np.random.RandomState(seed)  # R2 · legacy MT19937 · 全局单流
    held = []
    per_cell = []
    contributing = []
    for (b, s, o) in sorted(candidates.keys(), key=lambda c: (c[0], c[1], c[2])):
        cand = candidates[(b, s, o)]
        n = len(cand)
        k = take_amount(n)
        if k == 0:
            # R4 · k=0 之格 0 次抽取（⛔ 0 调用 shuffle）
            continue
        contributing.append((b, s, o))
        cand2 = list(cand)
        rng.shuffle(cand2)  # R3 · 在副本上洗牌，取前 k
        sel = cand2[:k]
        held.extend(sel)
        per_cell.append(
            {
                "cell": "%d,%d,%d" % (b, s, o),
                "b": b, "s": s, "o": o,
                "n": n, "k": k,
                "selected": sorted(sel, key=r1_key),  # R6 · 按 R1 键字节序升序
            }
        )
    # R6 · 全域落面：按 R1 键字节序升序
    held_sorted = sorted(held, key=r1_key)
    return held_sorted, per_cell, contributing


# ------------------------------------------------------------ R6 · 指纹重算
def fingerprint(held_sorted):
    """R6 · 指纹 = sha256(R1 序 'file#idx' 以 '|' 连接)[:12]（小写）。"""
    concat = "|".join("%s#%d" % (f, i) for (f, i) in held_sorted)
    sha256 = hashlib.sha256(concat.encode("utf-8")).hexdigest()
    return concat, sha256, sha256[:12]


# ------------------------------------------------------- 门 B · seed42 自审
def seed42_self_audit(files, per_file, candidates):
    """以 seed=42 复跑本实现，与现集 6a670e629dca 逐件全等；不等即停手。"""
    held_sorted, per_cell, _ = extract(candidates, SEED_BASE)
    concat, sha256, sha12 = fingerprint(held_sorted)

    with open(CURRENT_ITEMS_JSON, "r", encoding="utf-8") as f:
        cur = json.load(f)

    # (1) 26 件 (file, idx) 全等（R1 键序）
    cur_items = [(d["file"], d["idx"]) for d in cur["heldout_items"]]
    mine_items = [(f, i) for (f, i) in held_sorted]
    items_match = cur_items == mine_items

    # (2) 逐格对账：per_cell 的 (n, k, selected)
    cur_cells = {}
    for c in cur["per_cell"]:
        cur_cells[c["cell"]] = (
            c["n"], c["k"], [(s["file"], s["idx"]) for s in c["selected"]],
        )
    mine_cells = {}
    for c in per_cell:
        mine_cells[c["cell"]] = (
            c["n"], c["k"], [(s[0], s[1]) for s in c["selected"]],
        )
    cells_match = cur_cells == mine_cells

    # (3) 指纹全等
    cur_fp = cur["reproduction"]["heldout_ordered_fingerprint"]
    fp_match = (cur_fp["concat"] == concat and cur_fp["sha256"] == sha256
                and cur_fp["sha12"] == sha12)

    ok = items_match and cells_match and fp_match
    audit = {
        "seed": SEED_BASE,
        "heldout_n": len(mine_items),
        "items_match": items_match,
        "cells_match": cells_match,
        "fingerprint_match": fp_match,
        "sha12": sha12,
        "self_audit_pass": ok,
    }
    return audit


# ---------------------------------------------------------------- 主流程
def main():
    files, per_file, total_rows = load_domain()
    domain_info = domain_gate(files, per_file)

    rows, candidates = build_candidates(files, per_file)

    # ---- 门 B · seed42 自审（FTFB 等价：先复现现集，逐件全等方继续）----
    audit = seed42_self_audit(files, per_file, candidates)
    print("== 门 B · seed42 逐件自审 ==")
    print("  heldout_n            = %d" % audit["heldout_n"])
    print("  items 全等            = %s" % audit["items_match"])
    print("  per_cell 全等        = %s" % audit["cells_match"])
    print("  指纹全等              = %s" % audit["fingerprint_match"])
    print("  seed42 sha12          = %s" % audit["sha12"])
    print("  自审通过              = %s" % audit["self_audit_pass"])
    if not audit["self_audit_pass"]:
        print("ABORT: seed42 self-audit failed ⇒ 实现有误，停手（0 抽取新集）")
        sys.exit(3)

    # ---- R7 · 以 seed′ 抽取新 held-out 集 ----
    held_sorted, per_cell, contributing = extract(candidates, SEED_PRIME)
    held_n = len(held_sorted)
    concat, sha256, sha12 = fingerprint(held_sorted)

    if held_n != 26:
        print("ABORT: new heldout_n %d != 26（件数派生，0 另行指定）" % held_n)
        sys.exit(4)

    # 逐件 q_id（仅标识面，0 贴内部文本字段）
    def qid_of(item):
        f, i = item
        return per_file[f][i].get("q_id")

    def cell_str_of(item):
        f, i = item
        b, s, o = cell_of(per_file[f][i])
        return "%d,%d,%d" % (b, s, o), b, s, o

    heldout_items = []
    for order, item in enumerate(held_sorted):
        cs, b, s, o = cell_str_of(item)
        heldout_items.append(
            {
                "file": item[0],
                "idx": item[1],
                "q_id": qid_of(item),
                "cell": cs,
                "b": b, "s": s, "o": o,
                "order_in_r1_key": order,
            }
        )

    # composition（规则内生：b=1 各占格 n<=2 ⇒ floor=0）
    b1_in_heldout = sum(1 for it in heldout_items if it["b"] == 1)

    payload = {
        "artifact": "_s4_heldout_sampling_seedprime_items_2026_10_10.json",
        "date": "2026-10-10",
        "spec_source": {
            "prereqs_file": "results/_g5_ccp_execution_prereqs_2026_10_10.md",
            "prereqs_sha12": "ab1a07ae2fd1",
            "ruling_file": "results/_s4_heldout_sampling_caliber_ruling_2026_10_09.md",
            "ruling_sha12": "fb1b696de1d6",
            "seed_designation_file": "results/_g5_ccp_seed_designation_revision_2026_10_10.md",
            "seed_designation_sha12": "b53f40abb90b",
            "status": "seed′ 已 PI 裁「照采」，规则冻结生效（生效即锁）",
            "params": {
                "R0": "同一 S4 冻结面 179 行（21 件 *addendum*.json）",
                "R1": "件名字节序（ordinal）升序 × 件内 #idx 升序",
                "R2": "np.random.RandomState(seed′) 全局单流（legacy MT19937）",
                "R3": "rng.shuffle(候选副本) 后取前 k；按集合认定",
                "R4": "格序 b,s,o 升序；floor=0 之格 0 消耗（0 次 shuffle）",
                "R5": "k = floor(0.30·n)，双轨 (3n)//10，0 round/ceil/max(1,·)",
                "R6": "落面按 R1 键字节序升序；指纹 = sha256(R1 序 file#idx 以 | 连接)[:12]",
                "R7": "seed′ = 1830975565（全域单一种子值，0 逐格派生）",
            },
        },
        "runtime": {
            "python": "%d.%d.%d" % sys.version_info[:3],
            "numpy": np.__version__,
            "network": 0,
            "endpoint_calls": 0,
            "api_key": 0,
            "note": "R4 key 永不明文 / 0 读 key / 0 读 .env",
        },
        "domain": domain_info,
        "counts": {
            "grid_total": 128,
            "occupied_cells": sum(1 for c in candidates.values() if c),
            "empty_cells": sum(1 for c in candidates.values() if not c),
            "contributing_cells": len(contributing),
            "sum_n_contributing": sum(c["n"] for c in per_cell),
            "sum_n_other": total_rows - sum(c["n"] for c in per_cell),
            "sum_n_total": total_rows,
        },
        "heldout_n": held_n,
        "heldout_items": heldout_items,
        "per_cell": [
            {
                "cell": c["cell"], "b": c["b"], "s": c["s"], "o": c["o"],
                "n": c["n"], "k": c["k"],
                "selected": [
                    {"file": s[0], "idx": s[1], "q_id": qid_of(s)}
                    for s in c["selected"]
                ],
            }
            for c in per_cell
        ],
        "composition": {
            "b1_items_in_heldout": b1_in_heldout,
            "stratified_with_correction_holds": b1_in_heldout > 0,
            "note": "规则内生：b=1 各占格 n<=2 ⇒ floor=0 ⇒ 换 seed′ 仍为 0 成立",
        },
        "self_audit": {
            "note": "抽取前以 seed=42 复跑本实现，与现集 6a670e629dca 逐件自审",
            **audit,
        },
        "reproduction": {
            "seed_prime": SEED_PRIME,
            "ratio": RATIO,
            "rng_family": "legacy MT19937 via np.random.RandomState",
            "stream": "全局单流",
            "cell_order": "b,s,o 升序",
            "zero_consumption_cells": True,
            "heldout_ordered_fingerprint": {
                "concat": concat,
                "sha256": sha256,
                "sha12": sha12,
                "note": "按 R1 键（件名字节序 × #idx 升序）排列之 26 件指纹（R6）",
            },
        },
    }

    with open(OUT_ITEMS_JSON, "w", encoding="utf-8", newline="\n") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print("== R7 · seed′ 抽取 ==")
    print("  seed′                = %d" % SEED_PRIME)
    print("  新 heldout_n          = %d" % held_n)
    print("  新指纹 sha12          = %s" % sha12)
    print("  新指纹 sha256         = %s" % sha256)
    print("  b=1 件数              = %d" % b1_in_heldout)
    print("  写入                 = %s" % os.path.relpath(OUT_ITEMS_JSON))
    print("OK")


if __name__ == "__main__":
    main()
