#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
向-1 第三集 held-out 抽取器（`seed″` 之可审实现）· 2026-10-11
================================================================================
件性质：可审实现脚本（executable implementation of the FROZEN spec）——依
  · `_s4_heldout_sampling_caliber_ruling_2026_10_09.md`（fb1b696de1d6）§5 伪码
  · `_g5_ccp_execution_prereqs_2026_10_10.md`（ab1a07ae2fd1）§4-1 之 R0–R7
  · `_f4_direction1_domain_effectivity_2026_10_11.md`（fd4ec7559342）S0′ 之 K-RJ-8′／K-RJ-9′
  · `_seed_double_identifier_finalization_2026_10_11.md`（6904852f8ceb）之 `seed″` ＝ 3223484571
四项逐字实现；**0 改一字**。

自审门（本脚本内置 · FTFB 之等价实现）：
  · 门 A（域校验）    输入域 ＝ results/ 全域 *addendum*.json，逐件 SHA-256／bytes／
                       supplements 长度须与 fb1b696de1d6 §5.1 登记值逐件全等。
                       任一不等 ⇒ print("ABORT: domain mismatch") + sys.exit(2)。
  · 门 B（seed42 自审）以 seed=42 复跑同一实现，26 件须与现集
                       `_s4_heldout_sampling_seed42_items_2026_10_09.json`（6a670e629dca）
                       **逐件全等**（R1 键序、per_cell、指纹）。不等 ⇒ 停手（⛔ 0 抽取新集）。
  · 门 B′（seed′ 复算核）以 seed′=1830975565 复跑同一实现，须与第二集
                       `_s4_heldout_sampling_seedprime_items_2026_10_10.json`（6cbb8ba01bfb）
                       逐件全等 ⇒ 证明实现对「换 seed」族之普适性（⛔ 0 用其读数择任何事）。
  门 B 通过后，方以 seed″ 抽取第三集并落盘。

执行：
  python results/_s4_heldout_sampling_seedthird_extractor_2026_10_11.py
  （在 repo 根目录执行；仅读 inputs，仅写本脚本自身之 JSON ＋ 登记件 2 件新名）

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
  R7 种子  ＝ seed″ = 3223484571（全域单一种子值；⛔ 0 逐格派生、0 加格号偏移）。

派生面（均为 R6 之后之机械后处理，⛔ 0 回灌抽取）：
  · 三集对照（第三集 ∩／∖ 前两集 · 对称差）
  · 可动件实测（依 KEYWORDS_T1 ⊊ KEYWORDS_V31 差 9 词之机制；★ 判据 ＝
    **seq_t1_only 与 seq_v31 之逐位序列比对**；⛔ 0 以「语料含 9 词中任一」径判
    —— 依 e7fcbc290a7e §3-1「当且仅当」条件 ＋ B-8 之实测反例 d3c#1）
  · `in_heldout` 逐件重算（对照面 ＝ 面 II 位移面 24 件 · 依 26c8278e3552 步 10 之口径）

硬约束（本脚本遵行）：
  ⛔ 0 手工挑选 / 0 由读数反推：seed″ 系公式输出，0 用任何读数；⛔ 0 枚举试值。
  ⛔ 0 判档 / 0 代裁 / 0 宣告主案成立：只做「抽取＋登记」，判定与裁决归他棒。
  ⛔ 0 换 seed 重抽（PI 定「一次抽取」· fd4ec7559342 §7）：本脚本只跑一个 seed″。
  ⛔ 0 回改任何既有件：本脚本 0 编辑既有件；产出为另名新件 3 件（物理分离）。
  ⛔ 0 改 K-RJ-8′／K-RJ-9′ 判死线条文：新值以本登记件承载，⛔ 0 回改 fd4ec7559342 一字。
  ⛔ 0 网络 / 0 skill / 0 LLM / 0 端点 / 0 key：纯本机只读计算（R4：0 读 key / 0 读 .env）。
  ⛔ 0 跑 S4′ 读数面：⛔ 0 调 compute_readings / build_tree / predict_tree / bootstrap_ci_v3。
  ⛔ 0 贴 dataset 内部文本字段（reasoning_full / scene_verbatim / pi_answer_verbatim）：
     产出件只载标识面 ＋ 派生之序列层（层名，非语料文本），依 fb1b696de1d6 §5.6 登记面规定。
  ⛔ 0 触及 〔本地资料区〕\\_non_upload_local_archive。
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
REPO = os.path.abspath(os.path.join(HERE, os.pardir))
RESULTS = os.path.abspath(os.path.join(HERE))

SEED_BASE = 42            # 门 B 自审用（现集之种子）
SEED_PRIME = 1830975565   # 门 B′ 复算核用（第二集之种子）
SEED_THIRD = 3223484571   # R7 正式抽取用（`seed″` · 6904852f8ceb §2-3）
LAMBDA_ID = "fd4ec7559342"  # `seed″` 之登记标识字面（6904852f8ceb §2-1）
RATIO = 0.30

OUT_ITEMS_JSON = os.path.join(
    RESULTS, "_s4_heldout_sampling_seedthird_items_2026_10_11.json"
)
OUT_REGISTER_MD = os.path.join(
    RESULTS, "_s4_heldout_sampling_seedthird_items_register_2026_10_11.md"
)
CURRENT_ITEMS_JSON = os.path.join(
    RESULTS, "_s4_heldout_sampling_seed42_items_2026_10_09.json"
)
PRIME_ITEMS_JSON = os.path.join(
    RESULTS, "_s4_heldout_sampling_seedprime_items_2026_10_10.json"
)
DISP_ITEMS_JSON = os.path.join(
    RESULTS, "_s4_v31_displacement_items_2026_10_10.json"
)
GOLD_ITEMS_JSON = os.path.join(
    RESULTS, "_s4_v31_regen_gold_items_2026_10_10.json"
)
PRIME_T1_SUPP_JSON = os.path.join(
    RESULTS, "_s4_seedprime_seq_t1_only_supplement_items_2026_10_11.json"
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


# ---------------------------------------------------------------- 工具
def sha12_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()[:12]


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_text(path, text):
    """UTF-8 无 BOM · LF。"""
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


# ------------------------------------------------------- R0 · 域读取（只读）
def load_domain():
    files = sorted(
        [f for f in os.listdir(RESULTS) if f.endswith(".json") and "addendum" in f],
        key=lambda x: x.encode("utf-8"),  # R1 · 显式字节序（⛔ 0 collation）
    )
    per_file = {}
    total_rows = 0
    for name in files:
        data = read_json(os.path.join(RESULTS, name))
        sup = data.get("supplements", [])
        if not isinstance(sup, list):
            raise SystemExit("ABORT: supplements not a list in %s" % name)
        per_file[name] = sup
        total_rows += len(sup)
    return files, per_file, total_rows


def domain_gate(files, per_file):
    reg = {n: (s, b, c) for (n, s, b, c) in DOMAIN_REGISTERED}
    if len(files) != 21:
        print("ABORT: domain file count %d != 21" % len(files))
        sys.exit(2)
    if set(files) != set(reg):
        print("ABORT: domain file set mismatch")
        sys.exit(2)
    rows = 0
    for name in files:
        p = os.path.join(RESULTS, name)
        s12 = sha12_of(p)
        b = os.path.getsize(p)
        c = len(per_file[name])
        rows += c
        exp = reg[name]
        if s12 != exp[0] or b != exp[1] or c != exp[2]:
            print("ABORT: domain mismatch %s got sha12=%s bytes=%d supp=%d expected %s"
                  % (name, s12, b, c, exp))
            sys.exit(2)
    if rows != 179:
        print("ABORT: total rows %d != 179" % rows)
        sys.exit(2)
    # 交叉核：本脚本之字节序文件表须与现集自报之 r1_byte_sorted_files 全等
    cur = read_json(CURRENT_ITEMS_JSON)
    r1_reg = cur["domain"]["r1_byte_sorted_files"]
    if list(files) != list(r1_reg):
        print("ABORT: r1 file list mismatch vs 6a670e629dca domain.r1_byte_sorted_files")
        sys.exit(2)
    return {"files": 21, "event_rows": rows, "r1_list_matches_current_set": True}


# ------------------------------------------------------- 分格键（§5.2 · 0 改）
def cell_of(ev):
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
    rows = []
    for f in files:
        for i in range(len(per_file[f])):
            rows.append((f, i))
    if len(set(rows)) != len(rows):
        print("ABORT: duplicate (file, idx) key")
        sys.exit(2)
    candidates = {}
    for b_ in (0, 1):
        for s_ in range(8):
            for o_ in range(8):
                candidates[(b_, s_, o_)] = [
                    (f, i) for (f, i) in rows
                    if cell_of(per_file[f][i]) == (b_, s_, o_)
                ]
    return rows, candidates


def r1_key(item):
    return (item[0].encode("utf-8"), item[1])


def take_amount(n):
    k = math.floor(RATIO * n)
    assert k == (3 * n) // 10, "R5 dual-track divergence at n=%d" % n
    return k


def extract(candidates, seed):
    rng = np.random.RandomState(seed)  # R2 · legacy MT19937 · 全局单流
    held = []
    per_cell = []
    contributing = []
    for (b, s, o) in sorted(candidates.keys(), key=lambda c: (c[0], c[1], c[2])):
        cand = candidates[(b, s, o)]
        n = len(cand)
        k = take_amount(n)
        if k == 0:
            continue  # R4 · k=0 之格 0 次抽取（⛔ 0 调用 shuffle）
        contributing.append((b, s, o))
        cand2 = list(cand)
        rng.shuffle(cand2)  # R3
        sel = cand2[:k]
        held.extend(sel)
        per_cell.append(
            {"cell": "%d,%d,%d" % (b, s, o), "b": b, "s": s, "o": o,
             "n": n, "k": k, "selected": sorted(sel, key=r1_key)}  # R6
        )
    return sorted(held, key=r1_key), per_cell, contributing


def fingerprint(held_sorted):
    concat = "|".join("%s#%d" % (f, i) for (f, i) in held_sorted)
    sha256 = hashlib.sha256(concat.encode("utf-8")).hexdigest()
    return concat, sha256, sha256[:12]


# ------------------------------------------------------- 门 B / B′ · 自审
def self_audit(candidates, seed, ref_path, ref_label):
    held_sorted, per_cell, _ = extract(candidates, seed)
    concat, sha256, sha12 = fingerprint(held_sorted)
    cur = read_json(ref_path)
    ref = cur
    cur_items = [(d["file"], d["idx"]) for d in ref["heldout_items"]]
    mine_items = [tuple(x) for x in held_sorted]
    items_match = cur_items == mine_items
    cur_cells = {c["cell"]: (c["n"], c["k"], [(s["file"], s["idx"]) for s in c["selected"]])
                 for c in ref["per_cell"]}
    mine_cells = {c["cell"]: (c["n"], c["k"], [(s[0], s[1]) for s in c["selected"]])
                  for c in per_cell}
    cells_match = cur_cells == mine_cells
    fp = ref["reproduction"]["heldout_ordered_fingerprint"]
    fp_match = (fp["concat"] == concat and fp["sha256"] == sha256 and fp["sha12"] == sha12)
    return {
        "seed": seed, "reference": ref_label, "reference_sha12": sha12_of(ref_path),
        "heldout_n": len(mine_items), "items_match": items_match,
        "cells_match": cells_match, "fingerprint_match": fp_match,
        "reference_fp_sha12": fp["sha12"], "recomputed_fp_sha12": sha12,
        "self_audit_pass": bool(items_match and cells_match and fp_match),
    }


# ============================================================ 可动件实测
def movable_layer(third_items, per_file):
    """★ 判据 ＝ seq_t1_only 与 seq_v31 之【逐位序列比对】（B-8）。

    ⛔ 0 以「语料含 KEYWORDS_V31 − KEYWORDS_T1 之 9 词中任一」径判
    （依 e7fcbc290a7e §3-1「当且仅当」条件；反例见 e7fcbc290a7e §7 之 B-8：
      d3c#1 含「后面」而序列未变 —— 同层已有共有词触发）。
    """
    sys.path.insert(0, os.path.join(REPO, ".tmp"))
    import s4_regen_runner as R  # 只读复用；其 import 期 0 写盘

    # KEYWORDS_T1：逐字取自 .tmp/prep.py L8–L9（⛔ 0 import prep.py：其 import 期即跑 S4′ 读数面）
    T1_WORDS = {"CRITERIA": ("复核", "质量", "保证"),
                "RISK": ("回退", "遗忘"),
                "KILL_LINE": ("推翻",)}
    KEYWORDS_T1 = {jt: tuple(R.KEYWORDS_V3[jt]) + T1_WORDS.get(jt, ())
                   for jt in R.JUDGMENT_TYPES}
    V31_ONLY = ("对齐", "失实", "挂起", "后面", "检验", "记忆效应", "噪声", "缺陷", "观察者效应")

    # ---- 词表自检（控制核）----
    v31_only = {w for jt, kws in R.KEYWORDS_V31.items() for w in kws} - {
        w for jt, kws in KEYWORDS_T1.items() for w in kws}
    assert v31_only == set(V31_ONLY), "KEYWORDS_T1/V31 差集非 9 词: %s" % sorted(v31_only)
    assert all(tuple(KEYWORDS_T1[jt])[:len(R.KEYWORDS_V3[jt])] == tuple(R.KEYWORDS_V3[jt])
               for jt in R.JUDGMENT_TYPES), "KEYWORDS_T1 未严格含 KEYWORDS_V3"

    events, meta = R.build_s4_face()
    index_map = meta["index_map"]
    pos = {(m["file"], m["idx"]): i for i, m in enumerate(index_map)}
    assert len(events) == 179, len(events)

    rows = []
    for it in third_items:
        key = (it["file"], it["idx"])
        gi = pos[key]
        rf = events[gi].get("reasoning_full", "") or ""
        seq_t1 = R.extract_sequence(rf, KEYWORDS_T1)
        seq_v31 = R.extract_sequence(rf, R.KEYWORDS_V31)
        eq = seq_t1 == seq_v31
        present = [w for w in V31_ONLY if w in rf]
        rows.append({
            "order_in_r1_key": it["order_in_r1_key"],
            "r1_key": "%s#%d" % (key[0], key[1]),
            "file": key[0], "src_idx": key[1], "global_idx": gi,
            "q_id_heldout_json": it["q_id"],
            "q_id_resolved": events[gi].get("q_id", "") or "",
            "cell": it["cell"], "corpus_len": len(rf),
            "seq_t1_only": seq_t1,
            "seq_t1_only_primary": R.primary_of(seq_t1),
            "seq_v31": seq_v31,
            "seq_v31_primary": R.primary_of(seq_v31),
            "seq_t1_only_eq_seq_v31": eq,          # ★ 可动判据之唯一依据
            "movable": (not eq),
            "n_v31_only_words_in_corpus": len(present),
            "v31_only_words_present": present,      # 诊断面，⛔ 0 作判据
            "layer_first_pos_t1": R.layer_first_pos(rf, KEYWORDS_T1),
            "layer_first_pos_v31": R.layer_first_pos(rf, R.KEYWORDS_V31),
        })
    return rows, sorted(v31_only), R


def movable_control(rows, R):
    """控制核：第二集（6cbb8ba01bfb 之 26 件）逐件复算，须与在册补层件逐位全等。"""
    if not os.path.exists(PRIME_T1_SUPP_JSON):
        return {"ran": False, "reason": "prime t1 supplement json absent"}
    prime = read_json(PRIME_ITEMS_JSON)
    supp = read_json(PRIME_T1_SUPP_JSON)
    ondisk = {it["r1_key"]: it for it in supp["items"]}
    events, meta = R.build_s4_face()
    index_map = meta["index_map"]
    pos = {(m["file"], m["idx"]): i for i, m in enumerate(index_map)}
    T1_WORDS = {"CRITERIA": ("复核", "质量", "保证"),
                "RISK": ("回退", "遗忘"), "KILL_LINE": ("推翻",)}
    KEYWORDS_T1 = {jt: tuple(R.KEYWORDS_V3[jt]) + T1_WORDS.get(jt, ())
                   for jt in R.JUDGMENT_TYPES}
    n_ok = 0
    n_mov = 0
    for it in prime["heldout_items"]:
        rk = "%s#%d" % (it["file"], it["idx"])
        rf = events[pos[(it["file"], it["idx"])]].get("reasoning_full", "") or ""
        s1 = R.extract_sequence(rf, KEYWORDS_T1)
        s31 = R.extract_sequence(rf, R.KEYWORDS_V31)
        od = ondisk[rk]
        assert od["seq_t1_only"] == s1, "控制核失败 %s" % rk
        assert od["seq_v31"] == s31, "控制核失败(seq_v31) %s" % rk
        assert od["seq_t1_only_eq_seq_v31"] == (s1 == s31), "控制核失败(eq) %s" % rk
        if s1 != s31:
            n_mov += 1
        n_ok += 1
    return {"ran": True, "n_items_recomputed": n_ok,
            "all_bit_identical_to_registered": True,
            "n_movable_prime_set": n_mov,
            "registered_n_movable_prime_set": supp["stats"]["n_movable_total"],
            "match": n_mov == supp["stats"]["n_movable_total"]}


# ============================================================ in_heldout 重算
def inheldout_recompute(third_keys):
    """依 26c8278e3552 §4 步 10 之口径：面 II 24 件之 R1 键是否属给定集。"""
    disp = read_json(DISP_ITEMS_JSON)
    rows = []
    for d in disp["items"]:
        rk = "%s#%d" % (d["file"], d["src_idx"])
        rows.append({"q_id": d.get("q_id"), "r1_key": rk, "dtype": d.get("displacement_type"),
                     "registered_in_heldout": bool(d.get("in_heldout")),
                     "in_third": rk in third_keys})
    reg_true = sum(1 for r in rows if r["registered_in_heldout"])
    new_true = sum(1 for r in rows if r["in_third"])
    return rows, {"registered_in": reg_true, "registered_out": len(rows) - reg_true,
                  "new_in": new_true, "new_out": len(rows) - new_true,
                  "denominator": len(rows)}


# ============================================================ 主流程
def main():
    files, per_file, total_rows = load_domain()
    domain_info = domain_gate(files, per_file)
    rows, candidates = build_candidates(files, per_file)

    # ---- 门 B · seed42 逐件自审（FTFB 等价）----
    audit_base = self_audit(candidates, SEED_BASE, CURRENT_ITEMS_JSON, "6a670e629dca（第一集 seed42）")
    print("== 门 B · seed42 逐件自审 ==")
    for k in ("heldout_n", "items_match", "cells_match", "fingerprint_match",
              "reference_fp_sha12", "recomputed_fp_sha12", "self_audit_pass"):
        print("  %-22s = %s" % (k, audit_base[k]))
    if not audit_base["self_audit_pass"]:
        print("ABORT: seed42 self-audit failed ⇒ 实现有误，停手（⛔ 0 抽取新集）")
        sys.exit(3)

    # ---- 门 B′ · seed′ 复算核（换 seed 族之普适性）----
    audit_prime = self_audit(candidates, SEED_PRIME, PRIME_ITEMS_JSON, "6cbb8ba01bfb（第二集 seed′）")
    print("== 门 B′ · seed′ 复算核 ==")
    for k in ("heldout_n", "items_match", "cells_match", "fingerprint_match",
              "reference_fp_sha12", "recomputed_fp_sha12", "self_audit_pass"):
        print("  %-22s = %s" % (k, audit_prime[k]))
    if not audit_prime["self_audit_pass"]:
        print("ABORT: seedprime recompute mismatch ⇒ 实现有误，停手（⛔ 0 抽取第三集）")
        sys.exit(5)

    # ---- R7 · 以 seed″ 抽取第三集（一次抽取 · ⛔ 0 重抽）----
    held_sorted, per_cell, contributing = extract(candidates, SEED_THIRD)
    held_n = len(held_sorted)
    concat, sha256, sha12 = fingerprint(held_sorted)
    print("== R7 · seed″ 抽取（一次）==")
    print("  seed″                 = %d" % SEED_THIRD)
    print("  新 heldout_n          = %d" % held_n)
    print("  FP3（sha12）          = %s" % sha12)
    if held_n != 26:
        print("ABORT: new heldout_n %d != 26" % held_n)
        sys.exit(4)

    def qid_of(item):
        return per_file[item[0]][item[1]].get("q_id")

    heldout_items = []
    for order, item in enumerate(held_sorted):
        b, s, o = cell_of(per_file[item[0]][item[1]])
        heldout_items.append({
            "file": item[0], "idx": item[1], "q_id": qid_of(item),
            "cell": "%d,%d,%d" % (b, s, o), "b": b, "s": s, "o": o,
            "order_in_r1_key": order,
        })

    third_keys = {"%s#%d" % (i["file"], i["idx"]) for i in heldout_items}
    base = read_json(CURRENT_ITEMS_JSON)
    prime = read_json(PRIME_ITEMS_JSON)
    base_keys = {"%s#%d" % (d["file"], d["idx"]) for d in base["heldout_items"]}
    prime_keys = {"%s#%d" % (d["file"], d["idx"]) for d in prime["heldout_items"]}

    def relation(a, b):
        return {"intersection": len(a & b), "only_a": len(a - b), "only_b": len(b - a),
                "symmetric_difference": len(a ^ b), "union": len(a | b)}

    rel_base = relation(third_keys, base_keys)
    rel_prime = relation(third_keys, prime_keys)
    rel_bp = relation(base_keys, prime_keys)

    # ---- 可动件实测 ----
    print("== 可动件实测（逐位序列比对）==")
    mrows, v31_only_sorted, R = movable_layer(heldout_items, per_file)
    mctrl = movable_control(mrows, R)
    n_movable = sum(1 for r in mrows if r["movable"])
    print("  V31−T1 差集词数        = %d %s" % (len(v31_only_sorted), v31_only_sorted))
    print("  可动件数（逐位比对）   = %d / %d" % (n_movable, len(mrows)))
    print("  含≥1 个 V31-only 词件数 = %d（⛔ 非判据 · 仅诊断）"
          % sum(1 for r in mrows if r["n_v31_only_words_in_corpus"] > 0))
    print("  控制核（第二集 26 件逐位全等）= %s（可动 %d 件）"
          % (mctrl.get("all_bit_identical_to_registered"), mctrl.get("n_movable_prime_set")))

    # ---- in_heldout 重算 ----
    irows, icount = inheldout_recompute(third_keys)
    irows_base, icount_base = inheldout_recompute(base_keys)
    irows_prime, icount_prime = inheldout_recompute(prime_keys)
    print("== in_heldout 重算（面 II 24 件）==")
    print("  第三集 新内/新外        = %d / %d" % (icount["new_in"], icount["new_out"]))
    print("  控制核 第一集 内/外     = %d / %d（对照在册 %d/%d）"
          % (icount_base["new_in"], icount_base["new_out"],
             icount["registered_in"], icount["registered_out"]))
    print("  对照 第二集 内/外       = %d / %d" % (icount_prime["new_in"], icount_prime["new_out"]))

    # ---- 迁移矩阵（旧集 → 第三集）----
    base_in = {r["r1_key"] for r in irows if r["registered_in_heldout"]}
    third_in = {r["r1_key"] for r in irows if r["in_third"]}
    in_to_out = sorted(base_in - third_in)
    out_to_in = sorted(third_in - base_in)
    stable_in = sorted(base_in & third_in)
    stable_out = sorted(set(r["r1_key"] for r in irows) - base_in - third_in)
    cell_of_key = {"%s#%d" % (i["file"], i["idx"]): i["cell"] for i in heldout_items}
    for r in irows:
        r["cell_if_in_third"] = cell_of_key.get(r["r1_key"])

    b1_in_heldout = sum(1 for it in heldout_items if it["b"] == 1)

    # ============================================================ 落盘 · JSON
    payload = {
        "artifact": os.path.basename(OUT_ITEMS_JSON),
        "date": "2026-10-11",
        "kind": "s4_heldout_third_set",
        "spec_source": {
            "ruling": {"file": "results/_s4_heldout_sampling_caliber_ruling_2026_10_09.md",
                       "sha12": "fb1b696de1d6", "section": "§5 伪码"},
            "prereqs": {"file": "results/_g5_ccp_execution_prereqs_2026_10_10.md",
                        "sha12": "ab1a07ae2fd1", "section": "§4-1 R0–R7"},
            "s0prime": {"file": "results/_f4_direction1_domain_effectivity_2026_10_11.md",
                        "sha12": "fd4ec7559342", "section": "K-RJ-8′／K-RJ-9′／§7"},
            "seed_double": {"file": "results/_seed_double_identifier_finalization_2026_10_11.md",
                            "sha12": "6904852f8ceb", "section": "§2-1／§2-3"},
            "status": "seed″ 已落定（6904852f8ceb）＋ S0′ 已生效（fd4ec7559342）⇒ 抽取解锁",
            "params": {
                "R0": "同一 S4 冻结面 179 行（21 件 *addendum*.json）",
                "R1": "件名字节序（ordinal）升序 × 件内 #idx 升序",
                "R2": "np.random.RandomState(seed″) 全局单流（legacy MT19937）",
                "R3": "rng.shuffle(候选副本) 后取前 k；按集合认定",
                "R4": "格序 b,s,o 升序；floor=0 之格 0 消耗（0 次 shuffle）",
                "R5": "k = floor(0.30·n)，双轨 (3n)//10，0 round/ceil/max(1,·)",
                "R6": "落面按 R1 键字节序升序；指纹 = sha256(R1 序 file#idx 以 | 连接)[:12]",
                "R7": "seed″ = 3223484571（全域单一种子值，0 逐格派生）",
            },
        },
        "runtime": {
            "python": "%d.%d.%d" % sys.version_info[:3],
            "numpy": np.__version__,
            "network": 0, "endpoint_calls": 0, "api_key": 0, "skill_calls": 0, "llm_calls": 0,
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
            {"cell": c["cell"], "b": c["b"], "s": c["s"], "o": c["o"], "n": c["n"], "k": c["k"],
             "selected": [{"file": s[0], "idx": s[1], "q_id": qid_of(s)} for s in c["selected"]]}
            for c in per_cell
        ],
        "composition": {
            "b1_items_in_heldout": b1_in_heldout,
            "stratified_with_correction_holds": b1_in_heldout > 0,
            "note": "规则内生：b=1 各占格 n<=2 ⇒ floor=0 ⇒ 换 seed″ 仍为 0 成立",
        },
        "self_audit": {
            "note": "抽取前以 seed=42 复跑本实现与第一集逐件全等（门 B）；"
                    "并以 seed′ 复跑与第二集逐件全等（门 B′）",
            "gate_B_seed42": audit_base,
            "gate_B_prime_seedprime": audit_prime,
        },
        "reproduction": {
            "seed_third": SEED_THIRD,
            "lambda_identifier": LAMBDA_ID,
            "ratio": RATIO,
            "rng_family": "legacy MT19937 via np.random.RandomState",
            "stream": "全局单流",
            "cell_order": "b,s,o 升序",
            "zero_consumption_cells": True,
            "extraction_count": 1,
            "no_resampling_with_other_seed": True,
            "heldout_ordered_fingerprint": {
                "concat": concat, "sha256": sha256, "sha12": sha12,
                "fp3": sha12,
                "note": "★ FP3 ＝ K-RJ-8′ 之锚值（fd4ec7559342 §3 之待填槽）；"
                        "按 R1 键（件名字节序 × #idx 升序）排列之 26 件指纹（R6）",
            },
        },
        "three_set_relations": {
            "note": "三集互不可比（fd4ec7559342 §5 · PI 已明示承受）⇒ ⛔ 0 混用读数；"
                    "此处仅载成员关系之机械计数",
            "set1_seed42": {"fp": "acedff01d18c", "n": len(base_keys)},
            "set2_seedprime": {"fp": "3c25e1a2ea94", "n": len(prime_keys)},
            "set3_seedthird": {"fp": sha12, "n": len(third_keys)},
            "third_vs_first": rel_base,
            "third_vs_second": rel_prime,
            "first_vs_second": rel_bp,
        },
        "movable_items": {
            "criterion": "★ seq_t1_only 与 seq_v31 之【逐位序列比对】；"
                         "movable ⇔ 两序列 ≢（e7fcbc290a7e §3-1 之「当且仅当」条件）",
            "forbidden_criterion": "⛔ 0 以「语料含 KEYWORDS_V31 − KEYWORDS_T1 之 9 词中任一」径判"
                                   "（B-8 反例：d3c#1 含「后面」而序列未变）",
            "keywords_t1_source": ".tmp/prep.py L8–L9（逐字转录；⛔ 0 import prep.py）",
            "keywords_v31_source": ".tmp/s4_regen_runner.py L54–L64（V31_NEW_WORDS ＋ KEYWORDS_V3）",
            "keywords_v3_source": "executor 8a81d90c69ba L202（只读复用）",
            "mechanism": "extract_sequence(reasoning_full, kwtable)（s4_regen_runner L67–L99）",
            "v31_minus_t1": v31_only_sorted,
            "v31_minus_t1_n": len(v31_only_sorted),
            "n_movable": n_movable,
            "n_total": len(mrows),
            "n_corpus_contains_v31only_word": sum(
                1 for r in mrows if r["n_v31_only_words_in_corpus"] > 0),
            "criterion_divergence_items": [
                r["r1_key"] for r in mrows
                if (r["n_v31_only_words_in_corpus"] > 0) != r["movable"]
            ],
            "control_check": mctrl,
            "note": "⛔ 0 贴 reasoning_full / scene_verbatim / pi_answer_verbatim（fb1b696de1d6 §5.6）；"
                    "本节只载序列层（层名）＋ 诊断计数；⛔ 0 据可动件数判档或宣告过门",
            "items": mrows,
        },
        "in_heldout_recompute": {
            "spec": "results/_s4_source_wave_mapping_registration_2026_10_10.md（26c8278e3552）§4 步 10",
            "denominator_face": "面 II 位移面 24 件（results/_s4_v31_displacement_items_2026_10_10.json · 6f020c03e52c）",
            "criterion": "面 II 24 件之 R1 键（file ＋ src_idx）是否属第三集 26 条之一",
            "counts": icount,
            "control_first_set": icount_base,
            "control_second_set": icount_prime,
            "migration": {"in_to_out": in_to_out, "out_to_in": out_to_in,
                          "stable_in": stable_in, "stable_out": stable_out,
                          "identity_check": "%d - %d + %d = %d" % (
                              icount_base["new_in"], len(in_to_out), len(out_to_in),
                              icount_base["new_in"] - len(in_to_out) + len(out_to_in))},
            "note": "⛔ 0 回写 6f020c03e52c 之 in_heldout 字段（新值仅存于本产出）；"
                    "⛔ 0 判档 / 0 代裁 / 0 改 K-RJ-9′ 条文（fd4ec7559342 §4 之重述义务归 PI）",
            "items": irows,
        },
    }
    write_text(OUT_ITEMS_JSON, json.dumps(payload, ensure_ascii=False, indent=1) + "\n")

    # ============================================================ 落盘 · 登记件
    M = []
    A = M.append
    A("# 向-1 第三集 held-out 抽取登记件（`seed″` ＝ `3223484571`）· 2026-10-11\n")
    A("\n- **件性质**：**worker 执行面 · 抽取＋登记**（**⛔ 非 protocol 面 · ⛔ 非判定面**）—— 依已生效之冻结规格抽取第三集 26 件，并落逐件表、三集对照、可动件实测、`in_heldout` 重算\n"
      "  ｜ ⛔ **0 判档**（0 出 `pass`／`af`／`kd`／`fail`／`give-up` 五终判之一）｜ ⛔ **0 代裁／0 代择**｜ ⛔ **0 换 seed 重抽**（PI 定「一次抽取」）｜ ⛔ **0 回改任何既有件一字**｜ ⛔ **0 改 `K-RJ-8′`／`K-RJ-9′` 条文**\n"
      "- **授权锚**：PI 2026-10-11 收官卡 `f4_second` ＝ **甲·复核并闭（解锁）**｜规则与种子先于抽取落定（FTFB 已守）\n"
      "- **规格源**：`fb1b696de1d6` §5 伪码（0 改一字）＋ `ab1a07ae2fd1` §4-1 之 R0–R7｜`seed″` 落定于 `6904852f8ceb`（`λ` ＝ `%s`，菜单 N ＝ 1）｜`S0′` 生效于 `fd4ec7559342`\n" % LAMBDA_ID)
    A("- **产出 3 件（皆新名新建 · 0 覆写）**：\n"
      "  1. **可审脚本** `results/_s4_heldout_sampling_seedthird_extractor_2026_10_11.py`\n"
      "  2. **新集 JSON** `results/_s4_heldout_sampling_seedthird_items_2026_10_11.json`\n"
      "  3. **本登记件** `results/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md`\n")
    A("- **出件**：**worker**（向-1 第三集抽取批 · 分支会话 `%s`｜**署名如实** · ⛔ 0 冒充 PI／parent／verifier／verdict-keeper／protocol-keeper／evidence-auditor／doc-writer）\n" % "mvs_544437291b604723b1f8a991c7e717e4")
    A("- **版式**：UTF-8 **无 BOM** · **LF（CRLF ＝ 0）**｜**R4**：key 永不明文（0 读 key／0 读 `.env`／0 落盘凭据）｜**0 网络 ／ 0 skill ／ 0 LLM ／ 0 跑 executor ／ 0 跑 S4′ 读数面**｜⛔ **0 触及 `〔本地资料区〕\\_non_upload_local_archive`**\n")
    A("- **命名合规**：`_主题_日期` 三段式；首段 `_s4_heldout_sampling_` ＝ 步骤标识非阶段号 ⇒ 合 PI 2026-09-29 命名裁（`57024f2cd30a` §1.2②）；⛔ `_v5_`／`_v4_`／`_v3_`\n")
    A("\n> 📌 **状态栏**：🟢 **第三集已抽出（一次抽取 · 26 件 · `FP3` 已生成并登记）** ＋ 🟢 **自审双门通过**（seed42 逐件全等 ＋ seed′ 逐件全等）＋ 📌 **`FP3` 待 PI 面以另立登记承载**（⛔ 0 回改 `fd4ec7559342` 一字）＋ ⛔ **0 判档 · 0 宣告过门与否 · 0 宣告 `K-RJ-5` 闭／开 · 0 宣告新链可开跑**\n")

    A("\n---\n\n## §0 一句话结论\n\n")
    A("**以 `seed″` ＝ `3223484571` 依 R0–R7 冻结规格抽出第三集 held-out 26 件，`FP3` ＝ **`%s**；"
      "抽取前双门自审通过（以 `seed=42` 与现集 `6a670e629dca` **逐件全等**、以 `seed′` 与第二集 `6cbb8ba01bfb` **逐件全等**）；"
      "可动件实测 ＝ **%d** 件（判据 ＝ `seq_t1_only` 与 `seq_v31` 之**逐位序列比对**）；"
      "`in_heldout` 重算（面 II 24 件）＝ **新内 %d ／新外 %d**（第一集 %d／%d、第二集 %d／%d）。"
      "** ⛔ 本件仅提供机械事实，⛔ 0 判档、⛔ 0 宣告过门与否、⛔ 0 代改任何判死线条文。**\n"
      % (sha12, n_movable, icount["new_in"], icount["new_out"],
         icount_base["new_in"], icount_base["new_out"],
         icount_prime["new_in"], icount_prime["new_out"]))

    A("\n---\n\n## §1 ★ `FP3`（**`K-RJ-8′` 之锚值 · 待填槽之填**）\n\n")
    A("| 项 | 值 |\n|:--|:--|\n")
    A("| **`FP3`（＝ `K-RJ-8′` 之锚值字面）** | **`%s`** |\n" % sha12)
    A("| 算法（R6 · 0 改） | `sha256( R1 键字节序之 \"file#idx\" 以 \"|\" 连接 )[:12]`（小写 hex） |\n")
    A("| 全 64 hex | `%s` |\n" % sha256)
    A("| 长度（可核） | **%d 字符**（26 条） |\n" % len(concat))
    A("| 载体 | `results/_s4_heldout_sampling_seedthird_items_2026_10_11.json` |\n")
    A("| `match`／**26／26** | 复算同值 ✅ ／ 件数 **26**（两两互异） |\n")
    A("| 与前两集 | 异于 `acedff01d18c`（第一集）、异于 `3c25e1a2ea94`（第二集）⇒ **三集互不可比**（`fd4ec7559342` §5 · PI 已明示承受） |\n")
    A("\n📌 **承载纪律**：`K-RJ-8′` 之**判据形式**已冻于 `fd4ec7559342` §3；本件**仅以另立登记承载新值**，⛔ **0 回改** `fd4ec7559342` 一字、⛔ **0 改** `04495ef4b343` 一字。** `FP3` 之正式生效归 PI／protocol 面。**\n")

    A("\n---\n\n## §2 ★ 自审双门（**抽取前 · FTFB 之等价实现**）\n\n")
    A("| 门 | 种子 | 对照集 | 件数全等 | 逐格全等 | 指纹全等 | 复算指纹 | 判定 |\n|:-:|:--|:--|:-:|:--:|:--:|:--|:--|\n")
    A("| **B** | `42` | `6a670e629dca`（第一集） | %s | %s | %s | `%s` | **%s** |\n"
      % (audit_base["items_match"], audit_base["cells_match"], audit_base["fingerprint_match"],
         audit_base["recomputed_fp_sha12"], "✅ 通过" if audit_base["self_audit_pass"] else "❌"))
    A("| **B′** | `%d` | `6cbb8ba01bfb`（第二集） | %s | %s | %s | `%s` | **%s** |\n"
      % (SEED_PRIME, audit_prime["items_match"], audit_prime["cells_match"],
         audit_prime["fingerprint_match"], audit_prime["recomputed_fp_sha12"],
         "✅ 通过" if audit_prime["self_audit_pass"] else "❌"))
    A("\n> 📌 **门 B 之意义**：同一实现以现集之种子复跑须**逐件全等** ⇒ 实现无偏；不等即 ⛔ 停手（⛔ **0 产出新集**）。\n"
      "> 📌 **门 B′ 之意义**（本棒自加之控制核）：同一实现以第二集之种子复跑亦**逐件全等** ⇒ 实现对「换 seed」族**普适**，非恰性拟合。\n"
      "> 📌 **两门皆在第三集抽取之前执行** ⇒ 任一失败即 `sys.exit`，⛔ **0 产出新集实体**。\n")

    A("\n---\n\n## §3 ★ 逐件表（**26 件 · R1 键字节序**）\n\n")
    A("| 序 | `file#idx` | `q_id` | 格 `(b,s,o)` | 位移型 | `seq_t1_only` | `seq_v31` | 逐位相等 | **可动** |\n|:-:|:--|:--|:-:|:-:|:--|:--|:-:|:-:|\n")
    dtype_by_key = {}
    for d in read_json(DISP_ITEMS_JSON)["items"]:
        dtype_by_key["%s#%d" % (d["file"], d["src_idx"])] = d.get("displacement_type")
    for r in mrows:
        A("| %d | `%s` | `%s` | `%s` | %s | `%s` | `%s` | %s | %s |\n"
          % (r["order_in_r1_key"], r["r1_key"], r["q_id_heldout_json"] if r["q_id_heldout_json"] else "null",
             r["cell"], dtype_by_key.get(r["r1_key"], "—"),
             ",".join(r["seq_t1_only"]) or "∅", ",".join(r["seq_v31"]) or "∅",
             "＝" if r["seq_t1_only_eq_seq_v31"] else "≠",
             "**是**" if r["movable"] else "否"))

    A("\n---\n\n## §4 ★ 可动件实测（**逐位序列比对 · ⛔ 0 以「含 9 词」径判**）\n\n")
    A("| 项 | 内容 |\n|:--|:--|\n")
    A("| **判据** | ★ `movable` ⇔ **`extract_sequence(reasoning_full, KEYWORDS_T1)` ≠ `extract_sequence(reasoning_full, KEYWORDS_V31)`**（**逐位序列比对**） |\n")
    A("| **⛔ 禁用判据** | 「语料含 `KEYWORDS_V31 − KEYWORDS_T1` 之 9 词中任一」—— 依 `e7fcbc290a7e` §3-1 之「当且仅当」条件 ＋ §7 之 **B-8** 实测反例（`d3c#1` 含「后面」而序列**未变**，因同层 `TIMING` 已被共有词 `补一晚` 触发） |\n")
    A("| `KEYWORDS_T1` | `KEYWORDS_V3` ＋ `{CRITERIA: 复核/质量/保证, RISK: 回退/遗忘, KILL_LINE: 推翻}`（逐字转录自 `.tmp/prep.py` L8–L9；⛔ **0 import** `prep.py`） |\n")
    A("| `KEYWORDS_V31` | `KEYWORDS_V3` ＋ 15 个 V3.1 新词（`.tmp/s4_regen_runner.py` L54–L64） |\n")
    A("| `KEYWORDS_V31 − KEYWORDS_T1` | **%d 词** ＝ `%s` |\n" % (len(v31_only_sorted), "`／`".join(v31_only_sorted)))
    A("| **可动件数（逐位比对）** | **%d** ／ %d |\n" % (n_movable, len(mrows)))
    A("| 含 ≥1 个 V31-only 词之件数 | %d（**⛔ 诊断面 · 非判据**） |\n" % sum(1 for r in mrows if r["n_v31_only_words_in_corpus"] > 0))
    divergence = [r["r1_key"] for r in mrows
                if (r["n_v31_only_words_in_corpus"] > 0) != r["movable"]]
    div_txt = ("`" + "`、`".join(divergence) + "`") if divergence else "**0 件**"
    A("| 两判据之分歧件（`含词≠可动` 或 `不含词却可动`） | %s |\n" % div_txt)
    A("\n📌 **控制核（第二集 26 件逐位复算）**：%s —— 逐件 `seq_t1_only`／`seq_v31`／相等性三项与在册补层件**逐位全等**（%s／%s 件），可动件数复算 **%d** ＝ 在册 **%s** ⇒ 本棒之可动机制与盘上已登记机制**同源**。\n"
      % (mctrl.get("all_bit_identical_to_registered"), mctrl.get("n_items_recomputed"),
         mctrl.get("n_items_recomputed"), mctrl.get("n_movable_prime_set"),
         mctrl.get("registered_n_movable_prime_set")))
    A("\n🔴 **诚实边界**：本节**仅给出可动件数之机械事实**。⛔ **0 据以判档**；⛔ **0 宣告 `n_distinct` 过门与否**（`fd4ec7559342` §7 明载：可动件 ≥1 亦**不保证**过门，且若为 **0** 件则**不重抽** ⇒ 出口归向-2～向-5／`give-up` 由 PI 择）；⛔ **0 跑 `S4′` 读数面**（`pred_model_side`、逐件贡献、五线读数 ＋ CI **均未产出**）。\n")

    A("\n---\n\n## §5 ★ 新旧三集对照（**交集／对称差**）\n\n")
    A("| 集 | 种子 | 指纹 | 件数 |\n|:--|:--|:--|--:|\n")
    A("| 第一集 | `42` | `acedff01d18c` | %d |\n" % len(base_keys))
    A("| 第二集 | `%d` | `3c25e1a2ea94` | %d |\n" % (SEED_PRIME, len(prime_keys)))
    A("| **第三集（本件）** | **`%d`** | **`%s`** | **%d** |\n" % (SEED_THIRD, sha12, len(third_keys)))
    A("\n| 对照 | 交集 | 仅 A | 仅 B | **对称差** | 并集 |\n|:--|--:|--:|--:|--:|--:|\n")
    A("| **第三集 ∩ 第一集** | %d | %d | %d | **%d** | %d |\n"
      % (rel_base["intersection"], rel_base["only_a"], rel_base["only_b"],
         rel_base["symmetric_difference"], rel_base["union"]))
    A("| **第三集 ∩ 第二集** | %d | %d | %d | **%d** | %d |\n"
      % (rel_prime["intersection"], rel_prime["only_a"], rel_prime["only_b"],
         rel_prime["symmetric_difference"], rel_prime["union"]))
    A("| 第一集 ∩ 第二集（对照） | %d | %d | %d | **%d** | %d |\n"
      % (rel_bp["intersection"], rel_bp["only_a"], rel_bp["only_b"],
         rel_bp["symmetric_difference"], rel_bp["union"]))
    A("\n> 📌 **三集互不可比**（`fd4ec7559342` §5 · PI 已明示承受）⇒ 上列**仅载成员关系之机械计数**，⛔ **0 混用三面读数**、⛔ **0 直接比大小**。\n")

    A("\n---\n\n## §6 ★ `in_heldout` 逐件重算（**对照面 ＝ 面 II 24 件**）\n\n")
    A("**口径**（依 `26c8278e3552` §4 步 10 · 0 改判据）：面 II 位移面 24 件之 R1 键（`file` ＋ `src_idx`）是否属**第三集 26 条**之一。**分母 ＝ 24**（⛔ 非 179 行全域）。\n\n")
    A("| 计数 | 第一集（旧） | 第二集 | **第三集（新）** |\n|:--|--:|--:|--:|\n")
    A("| **内** | %d | %d | **%d** |\n" % (icount_base["new_in"], icount_prime["new_in"], icount["new_in"]))
    A("| **外** | %d | %d | **%d** |\n" % (icount_base["new_out"], icount_prime["new_out"], icount["new_out"]))
    A("| 合计 | 24 | 24 | **24** |\n\n")
    A("### §6-1 控制核（**第一集复算 ＝ 在册字段**）\n\n")
    A("以第一集 `acedff01d18c` 独立复算面 II 24 件之 `in_heldout` ＝ **内 %d ／外 %d**，与 `6f020c03e52c` 在册字段（内 %d／外 %d）**全等** ⇒ 本棒判定式与产出在册 9／15 之口径**同源**（%s）。\n\n"
      % (icount_base["new_in"], icount_base["new_out"], icount["registered_in"],
         icount["registered_out"],
         "24／24 逐件相符" if icount_base["new_in"] == icount["registered_in"] else "⚠ 有分歧"))
    A("### §6-2 逐件表（面 II 24 件 · 旧 → 新）\n\n")
    A("| # | `q_id` | R1 键 | 位移型 | 旧 `in_heldout` | **新 `in_heldout`** | 依据（格） |\n|:-:|:--|:--|:-:|:-:|:-:|:--|\n")
    for n_, r in enumerate(irows, 1):
        A("| %d | `%s` | `%s` | %s | `%s` | **`%s`** | %s |\n"
          % (n_, r["q_id"], r["r1_key"], r["dtype"] or "—",
             str(r["registered_in_heldout"]).lower(), str(r["in_third"]).lower(),
             ("内 · 格 `%s`" % r["cell_if_in_third"]) if r["in_third"] else "外"))
    A("\n### §6-3 迁移矩阵（**第一集 → 第三集**）\n\n")
    def qlist(keys):
        out = []
        for k in keys:
            q = None
            for r in irows:
                if r["r1_key"] == k:
                    q = r["q_id"]
                    break
            out.append("`%s`" % (q if q else k))
        return "／".join(out)

    A("| 迁移类 | 件数 | `q_id` |\n|:--|--:|:--|\n")
    A("| `in` → `out` | **%d** | %s |\n" % (len(in_to_out), qlist(in_to_out)))
    A("| `out` → `in` | **%d** | %s |\n" % (len(out_to_in), qlist(out_to_in)))
    A("| 稳定 `in` | **%d** | %s |\n" % (len(stable_in), qlist(stable_in)))
    A("| 稳定 `out` | **%d** | 其余 |\n" % len(stable_out))
    A("| 合计 | **%d** | ✅ |\n\n" % len(irows))
    A("**对账恒等式**：旧内 `%d` − 迁出 `%d` ＋ 迁入 `%d` ＝ **新内 `%d`**；旧外 `%d` ＋ `%d` − `%d` ＝ **新外 `%d`**。\n\n"
      % (icount_base["new_in"], len(in_to_out), len(out_to_in), icount["new_in"],
         icount_base["new_out"], len(in_to_out), len(out_to_in), icount["new_out"]))
    A("> 🔴 **`K-RJ-9′` 之重述义务（归 PI／protocol 面）**：`fd4ec7559342` §4 载 `N_in3`／`N_out3` 待抽取后重算 ⇒ 本件**提供该二值之机械事实**（`N_in3` ＝ **%d**、`N_out3` ＝ **%d**；**分母 24 不变**）；⛔ **0 代拟条文**、⛔ **0 回改** `04495ef4b343` 一字、⛔ **0 宣告**重述已生效。\n"
      % (icount["new_in"], icount["new_out"]))

    A("\n---\n\n## §7 逐格落面（**16 贡献格 · R4 消耗序 `b→s→o`**）\n\n")
    A("| 格 `(b,s,o)` | `n` | `k` | `selected`（R1 键字节序） |\n|:-:|--:|--:|:--|\n")
    for c in per_cell:
        A("| `%s` | %d | %d | %s |\n" % (c["cell"], c["n"], c["k"],
             "、".join("`%s#%d`" % (s[0], s[1]) for s in c["selected"])))
    A("\n**构成报**：「分层含纠正」—— 留出集内 `b=1` 件数 = **%d**（**含 0 成立之明文**；规则内生：`b=1` 各占格 `n ≤ 2` ⇒ `floor(0.30·n) = 0`，换任何 seed 仍为 0）。\n\n" % b1_in_heldout)

    A("\n---\n\n## §8 诚实限制（如实列明 · **0 掩饰**）\n\n")
    A("1. 🔴 **0 判档／0 代裁** —— ⛔ 0 出五终判之一；⛔ 0 赋任一 `k_v3s_4_*` 布尔；⛔ **0 宣告** `P-0` 过／不过、⛔ **0 宣告** `K-RJ-5` 闭／开、⛔ **0 宣告**新链可开跑、⛔ **0 宣告**第三集可动件数「够／不够」。\n")
    A("2. 🔴 **可动件数 ≠ 过门** —— 本件 §4 之 **%d** 件仅为**逐位比对之机械事实**；`fd4ec7559342` §7 明载：可动件 ≥1 **不保证**过门（`n_distinct` 须 `S3′` 实测 ＋ 定义性退化 0 解）。\n" % n_movable)
    A("3. 🔴 **`S4′` 读数面未跑** —— ⛔ 0 产出 `pred_model_side`、⛔ 0 产出逐件贡献、⛔ 0 产出五线读数 ＋ CI ＋ bootstrap ⇒ §4 之可动件数**不可**外推为任何触发量。\n")
    A("4. 🔴 **一次抽取之界** —— 第三集**仅抽一次**（`fd4ec7559342` §7）；⛔ **0 换 seed 重抽**、⛔ **0 择其过门者**。本脚本只跑一个 `seed″`。\n")
    A("5. 🟡 **三面不可比** —— 旧两集面（`acedff01d18c`／`3c25e1a2ea94`）之读数与逐件层须**物理分离**保留；⛔ 0 视作已废，⛔ 0 混用三面读数（PI 已明示承受 · §5）。\n")
    A("6. 🟡 **0 贴语料内部文本** —— 依 `fb1b696de1d6` §5.6 登记面规定，产出件⛔ **0** 载 `reasoning_full`／`scene_verbatim`／`pi_answer_verbatim`；§3 只载序列层（层名）＋ 计数 ⇒ 语料本身须第三方另行取自 21 件域件。\n")
    A("7. 🟡 **可动机制之依赖** —— 复用 `.tmp/s4_regen_runner.py`（只读 import）与 executor `8a81d90c69ba` 之词表与纯函数；`KEYWORDS_T1` 为逐字转录（⛔ 0 import `prep.py`，其 import 期即跑 `S4′` 读数面）。本件**0 新造**任何机制。\n")

    A("\n---\n\n## §9 0 回改确认 ＋ 落前撞名实测 ＋ 纪律对照\n\n")
    A("| 纪律 | 自证 |\n|:--|:--|\n")
    A("| ⛔ **0 回改任何既有件** | ✅ 本棒**唯一写动作 ＝ 新建 3 件**（脚本 ＋ JSON ＋ 本登记件），皆新名；既有件 0 编辑／0 覆写／0 追加／0 改名／0 移动／0 删除（`6a670e629dca`／`6cbb8ba01bfb`／`6f020c03e52c`／`4125cb2df92b`／`26c8278e3552`／`fb1b696de1d6`／`ab1a07ae2fd1`／`fd4ec7559342`／`6904852f8ceb` **0 字节改动**） |\n")
    A("| ⛔ **0 改 `K-RJ-8′`／`K-RJ-9′` 条文** | ✅ 新值（`FP3`／`N_in3`／`N_out3`）**以本登记件另立承载**；⛔ 0 回改 `fd4ec7559342` 一字 |\n")
    A("| ⛔ **0 换 seed 重抽** | ✅ 抽取段只以 `seed″` ＝ `%d` 跑**一次**；门 B／B′ 之 `42`／`seed′` 复算**仅供自审**，不产生任何新集实体 |\n" % SEED_THIRD)
    A("| ⛔ **0 回写派生面** | ✅ ⛔ 0 回写 `6f020c03e52c` 之 `in_heldout` 字段；新值**仅存于**本产出 2 件 |\n")
    A("| **R4** | ✅ key 永不明文；0 读 key／0 读 `.env`／0 落盘凭据 |\n")
    A("| **0 网络／0 skill／0 LLM** | ✅ 纯本机只读计算；⛔ 0 端点调用／0 LLM 代答 |\n")
    A("| ⛔ **0 触及禁区** | ✅ `〔本地资料区〕\\_non_upload_local_archive` **0 读、0 写、0 列目录** |\n")
    A("| 编码 | ✅ UTF-8 **无 BOM** · **LF（CRLF ＝ 0）** |\n\n")
    A("\n---\n\n## §10 报回项（**⛔ 0 代裁 · 0 代立 · 0 自判闭**）\n\n")
    A("| # | 事项 | 本件处置 |\n|:-:|:--|:--|\n")
    A("| **R-1** | **`FP3` ＝ `%s`** 已生成并登记（`K-RJ-8′` 之待填槽） | 📋 已落 §1／JSON；⛔ **0 回改** `fd4ec7559342`；**生效归 PI／protocol 面** |\n" % sha12)
    A("| **R-2** | 可动件 **%d** 件（逐位比对判据） | 📋 已落 §3／§4；⛔ 0 判过门与否（§7 之「若」分支为**规则层出口约定**，非结果预测） |\n" % n_movable)
    A("| **R-3** | `N_in3` ＝ **%d**／`N_out3` ＝ **%d**（分母 24 不变） ⇒ `K-RJ-9′` 之**重述义务** | 📋 **仅提供数值事实**；⛔ 0 代拟条文、⛔ 0 回改 `04495ef4b343`、⛔ 0 宣告重述已生效 |\n" % (icount["new_in"], icount["new_out"]))
    A("| **R-4** | 三集关系（交集／对称差，见 §5） | 📋 仅机械计数；⛔ 0 混用三面读数 |\n")
    A("| **R-5** | `S4′` 读数面（`pred_model_side`／逐件贡献／五线 ＋ CI） | 🔴 **未跑 · 0 产出**；候 `S4′` 正式开跑后另棒产出 |\n")
    A("| **R-6** | 面 I（26 件全量漂移 · `E-4` 未决）之 `in_heldout` | 📌 **如实登记为未闭**；⛔ 0 自行扩域、⛔ 0 并入本批分母（分母 ＝ 24） |\n")
    A("| **R-7** | 独立复核签字 | 📋 核归 verifier／verdict-keeper；**⛔ 本件 0 自签核** |\n")
    A("\n> ⛔ **本件 0 主张**：①`FP3` 已生效或已采认；②第三集已被独立复核；③可动件数足以过门；④`K-RJ-9′` 重述已生效；⑤`K-RJ-5` 可闭。\n"
      "> 📌 **本件所主张者 ＝ 唯一**：**依已生效之冻结规格（R0–R7 ＋ `seed″` ＝ `%d`）抽出第三集 26 件，`FP3` ＝ `%s`，可动件 %d 件，`in_heldout` 新内 %d／新外 %d** —— 其**归置、重述与效力判定皆不在本棒**。\n"
      % (SEED_THIRD, sha12, n_movable, icount["new_in"], icount["new_out"]))

    write_text(OUT_REGISTER_MD, "".join(M))

    print("\n== 落盘 ==")
    print("  JSON     = %s" % os.path.relpath(OUT_ITEMS_JSON, REPO))
    print("  登记件   = %s" % os.path.relpath(OUT_REGISTER_MD, REPO))
    print("  FP3      = %s" % sha12)
    print("  可动件数 = %d" % n_movable)
    print("  新内/新外= %d / %d" % (icount["new_in"], icount["new_out"]))
    print("OK")


if __name__ == "__main__":
    main()