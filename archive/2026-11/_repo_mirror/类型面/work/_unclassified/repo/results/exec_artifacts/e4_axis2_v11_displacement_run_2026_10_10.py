# -*- coding: utf-8 -*-
"""
E-4 轴二实跑 · v1.1 基础面 4 件位移逐件提取 (worker · 2026-10-10)

只读脚本 (⛔ 0 写任何既有件 / 0 网络 / 0 LLM / 0 读 key / 0 skill)
机制逐字沿 results/_v4_pi_cot_v3_ruleset_v3_executor.py (8a81d90c69ba) L478-L519
面构造逐字沿 results/_s4_v31_regen_gold_register_2026_10_10.md §1.4
输出: stdout JSON (唯一写动作 = 本棒回执 / 联合出件)
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RESULTS = REPO / "results"

# ---------- 1. 只读 import executor (取其常量与纯函数, 0 就地改) ----------
spec = importlib.util.spec_from_file_location(
    "exec_v3", RESULTS / "_v4_pi_cot_v3_ruleset_v3_executor.py"
)
exec_v3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(exec_v3)

KEYWORDS_V3 = exec_v3.KEYWORDS_V3
PHRASE_PATTERNS_V3 = exec_v3.PHRASE_PATTERNS_V3
load_addendum_event_v3 = exec_v3.load_addendum_event_v3

# ---------- 2. V3.1 = V3 ⊎ 15 词 (逐字取自 1b7bcbcce589 §4.1/§4.2) ----------
V31_NEW_WORDS = {
    "CRITERIA": ["复核", "质量", "保证", "对齐", "失实"],
    "RISK": ["回退", "遗忘", "记忆效应", "噪声", "缺陷", "观察者效应"],
    "KILL_LINE": ["推翻", "检验"],
    "TIMING": ["挂起", "后面"],
}
KEYWORDS_V31 = {k: tuple(v) for k, v in KEYWORDS_V3.items()}
for _layer, _words in V31_NEW_WORDS.items():
    KEYWORDS_V31[_layer] = tuple(KEYWORDS_V31[_layer]) + tuple(_words)
NEW_WORD_SET = {w for ws in V31_NEW_WORDS.values() for w in ws}


def extract_seq(reasoning: str, kwtable) -> list:
    """逐字复制 executor L478-L519 之 extract_judgment_sequence_v3, 唯一差异 = 词表入参。"""
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
    seq, seen = [], set()
    for _, jt in earliest:
        if jt not in seen:
            seen.add(jt)
            seq.append(jt)
    for pat in PHRASE_PATTERNS_V3:
        if pat["pattern"] in reasoning:
            for jt in pat["target_seq"]:
                if jt not in seen:
                    seen.add(jt)
                    seq.append(jt)
    return seq


def is_proper_subsequence(small, big) -> bool:
    """V3 序列是否为 V3.1 序列之真子序列 (按序)。"""
    if len(small) >= len(big):
        return False
    it = iter(big)
    return all(any(x == y for y in it) for x in small)


def classify(seq_v3, seq_v31) -> str:
    """V-CLAUSE-1.6' §3.2 之四类封闭词表之机械判据。"""
    if not seq_v3 and seq_v31:
        return "T3"                      # [] -> 非空
    if not seq_v3 and not seq_v31:
        return "T4"                      # 两皆 []
    if is_proper_subsequence(seq_v3, seq_v31):
        return "T1"                      # 真子序列 (按序)
    if set(seq_v3) == set(seq_v31):
        return "T2"                      # 层集合相等 + 首现位置序不同
    return "OUT_OF_VOCAB"                # 判停并呈 PI (沿 §3.2)


def new_hits(reasoning: str) -> list:
    """★新增词逐字命中 (词 @ 字符位置 -> 层), 全部位置 (0 漏计)。"""
    out = []
    for layer, words in V31_NEW_WORDS.items():
        for w in words:
            start = 0
            while True:
                i = reasoning.find(w, start)
                if i < 0:
                    break
                out.append({"word": w, "layer": layer, "char_pos": i})
                start = i + 1
    out.sort(key=lambda d: (d["char_pos"], d["word"]))
    return out


# ---------- 3. S4 冻结面 (179 行) · R1 字节序 × idx 升序 ----------
sampling = json.loads((RESULTS / "_s4_heldout_sampling_seed42_items_2026_10_09.json").read_text(encoding="utf-8"))
R1_FILES = sampling["domain"]["r1_byte_sorted_files"]

# 已登记 10 件之 wave 映射 (逐字沿 executor provenance_wave_map + D4);
# 余 11 件用惰性标签 (逐字沿 gold register §1.4)。
WAVE_MAP = {
    "_v4_pi_cot_v2_dataset_addendum_2026_09_24.json": "D1_supp",
    "_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json": "D2_w1",
    "_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json": "D2_w2",
    "_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json": "D2_w3",
    "_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json": "D2_w4",
    "_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json": "D2_w5",
    "_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json": "D3_w1",
    "_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json": "D3_w2",
    "_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json": "D3_w3",
    "_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json": "D4_w1",
}
LAZY_WAVE = "S4_face_unregistered_wave"

heldout_keys = {(it["file"], it["idx"]) for it in sampling["heldout_items"]}

s4_rows = []
for fname in R1_FILES:
    ad = json.loads((RESULTS / fname).read_text(encoding="utf-8"))
    wave = WAVE_MAP.get(fname, LAZY_WAVE)
    for i, sup in enumerate(ad.get("supplements", [])):
        ev = load_addendum_event_v3(sup, wave, fname)
        s4_rows.append({
            "face": "S4",
            "q_id": ev.get("q_id", ""),
            "file": fname,
            "src_idx": i,
            "in_heldout": (fname, i) in heldout_keys,
            "reasoning_full": ev.get("reasoning_full", "") or "",
        })

for r in s4_rows:
    r["seq_v3"] = extract_seq(r["reasoning_full"], KEYWORDS_V3)
    r["seq_v31"] = extract_seq(r["reasoning_full"], KEYWORDS_V31)
    r["dtype"] = classify(r["seq_v3"], r["seq_v31"])
    r["displaced"] = r["seq_v3"] != r["seq_v31"]

s4_displaced = [r for r in s4_rows if r["displaced"]]

# ---------- 4. 回归对照: 面 II 件 6f020c03e52c 之 24 件 ----------
registered = json.loads((RESULTS / "_s4_v31_displacement_items_2026_10_10.json").read_text(encoding="utf-8"))
reg_by_key = {(it["q_id"], it["file"], it["src_idx"]): it for it in registered["items"]}
reg_keys = set(reg_by_key)

my_by_key = {(r["q_id"], r["file"], r["src_idx"]): r for r in s4_displaced}
regression = {
    "n_s4_rows": len(s4_rows),
    "n_s4_displaced_mine": len(s4_displaced),
    "n_registered_24": len(registered["items"]),
    "keys_identical": reg_keys == set(my_by_key),
    "only_in_registered": sorted([list(k) for k in (reg_keys - set(my_by_key))]),
    "only_in_mine": sorted([list(k) for k in (set(my_by_key) - reg_keys)]),
    "field_mismatches": [],
}
for k in sorted(reg_keys & set(my_by_key)):
    a, b = reg_by_key[k], my_by_key[k]
    if a["seq_v3"] != b["seq_v3"] or a["seq_v31"] != b["seq_v31"] or a["displacement_type"] != b["dtype"]:
        regression["field_mismatches"].append({
            "key": list(k),
            "registered": [a["seq_v3"], a["seq_v31"], a["displacement_type"]],
            "mine": [b["seq_v3"], b["seq_v31"], b["dtype"]],
        })

# ---------- 5. v1.1 基础面 (DATASET_V2_V11, 逐字沿 executor L832-833) ----------
ds = json.loads((RESULTS / "_v4_pi_cot_v2_dataset.json").read_text(encoding="utf-8"))
v11_rows = []
for ev in ds["events"]:
    v11_rows.append({
        "face": "v1.1",
        "q_id": ev.get("q_id", ""),
        "file": "_v4_pi_cot_v2_dataset.json",
        "src_idx": ev.get("event_id", ""),
        "in_heldout": False,          # v1.1 不在 S4 冻结面 179 行内
        "reasoning_full": ev.get("reasoning_full", "") or "",
    })
for r in v11_rows:
    r["seq_v3"] = extract_seq(r["reasoning_full"], KEYWORDS_V3)
    r["seq_v31"] = extract_seq(r["reasoning_full"], KEYWORDS_V31)
    r["dtype"] = classify(r["seq_v3"], r["seq_v31"])
    r["displaced"] = r["seq_v3"] != r["seq_v31"]

v11_displaced = [r for r in v11_rows if r["displaced"]]

# ---------- 6. 并集口径核: 唯一文本层 ----------
s4_texts = {r["reasoning_full"] for r in s4_rows}
v11_texts = {r["reasoning_full"] for r in v11_rows}
union_texts = s4_texts | v11_texts
overlap_texts = s4_texts & v11_texts
s4_disp_texts = {r["reasoning_full"] for r in s4_displaced}
v11_disp_texts = {r["reasoning_full"] for r in v11_displaced}

union_disp_texts = {t for t in union_texts if extract_seq(t, KEYWORDS_V3) != extract_seq(t, KEYWORDS_V31)}
new_disp_texts = union_disp_texts - s4_disp_texts

union_check = {
    "n_s4_unique_texts": len(s4_texts),
    "n_v11_unique_texts": len(v11_texts),
    "n_text_overlap": len(overlap_texts),
    "n_union_unique_texts": len(union_texts),
    "n_s4_displaced_texts": len(s4_disp_texts),
    "n_v11_displaced_texts": len(v11_disp_texts),
    "n_union_displaced_texts": len(union_disp_texts),
    "n_new_displaced_texts": len(new_disp_texts),
    "identity_24_plus_4": (len(s4_disp_texts) + len(new_disp_texts) == len(union_disp_texts)),
    "target_28": len(union_disp_texts) == 28,
    "target_4": len(new_disp_texts) == 4,
}

# 轴二 4 件之逐件结果 (取自并集新增位移文本, 逐件附 v1.1 全部同文本行)
axis2_items = []
for r in v11_displaced:
    if r["reasoning_full"] in new_disp_texts:
        axis2_items.append({
            "q_id": r["q_id"],
            "file": r["file"],
            "src_idx": r["src_idx"],
            "seq_v3": r["seq_v3"],
            "seq_v31": r["seq_v31"],
            "displacement_type": r["dtype"],
            "version_attribution": "V3.1",
            "in_heldout": r["in_heldout"],
            "new_hit_words": new_hits(r["reasoning_full"]),
            "corpus_verbatim": r["reasoning_full"],
        })

out = {
    "artifact": "e4_axis2_v11_displacement_run",
    "date": "2026-10-10",
    "mechanism_source": {
        "executor_sha12": "8a81d90c69ba",
        "excerpt": "L478-L519",
        "keyword_table_v3_sha12": "1b7bcbcce589",
    },
    "s4_face": {
        "n_rows": len(s4_rows),
        "n_displaced": len(s4_displaced),
        "type_counts": {
            t: sum(1 for r in s4_displaced if r["dtype"] == t)
            for t in ("T1", "T2", "T3", "T4", "OUT_OF_VOCAB")
        },
    },
    "regression_vs_face2_json": regression,
    "v11_face": {
        "n_rows": len(v11_rows),
        "n_displaced": len(v11_displaced),
        "type_counts": {
            t: sum(1 for r in v11_displaced if r["dtype"] == t)
            for t in ("T1", "T2", "T3", "T4", "OUT_OF_VOCAB")
        },
    },
    "union_check": union_check,
    "axis2_items": axis2_items,
    "axis2_n_items": len(axis2_items),
}
sys.stdout.write(json.dumps(out, ensure_ascii=False, indent=1))
