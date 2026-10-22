# -*- coding: utf-8 -*-
"""C5 guard-surface min/max/std backfill -- pure local recompute, 0 network, 0 key read.

Reads (read-only):
  results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json   (B3 output, 22 sections)
  corpus/v20/index_v3_2026_09_29.json                              (B3 index output)
  results/c5_b_group_fix_readings_2026_10_01.json                  (post-fix readings)

Writes (new name, 0 overwrite):
  results/c5_guard_minmaxstd_readings_2026_10_01.json

std convention: ddof=0 (population) primary, ddof=1 (sample) reported alongside.
All hex-string fields: lexicographic min/max; hex->int surrogate reading marked as
  derivation (0 threshold), std for the string field itself is undefined.
"""
import json
import hashlib
import statistics
from collections import Counter, OrderedDict

REPO = r"_repo_mirror"
B3 = REPO + "/results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json"
IDX = REPO + "/corpus/v20/index_v3_2026_09_29.json"
FIX = REPO + "/results/c5_b_group_fix_readings_2026_10_01.json"
OUT = REPO + "/results/c5_guard_minmaxstd_readings_2026_10_01.json"

OLD_ROOT = "75596bbabdb8"


def sha12(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def nums(vals):
    """population/sample std + min/max/mean/median/range for a numeric column."""
    v = [float(x) for x in vals]
    return OrderedDict([
        ("n", len(v)),
        ("min", min(v)),
        ("max", max(v)),
        ("mean", round(statistics.fmean(v), 6)),
        ("median", round(statistics.median(v), 6)),
        ("std_ddof0", round(statistics.pstdev(v), 6)),
        ("std_ddof1", round(statistics.stdev(v), 6) if len(v) > 1 else None),
        ("range", round(max(v) - min(v), 6)),
    ])


def strcol(vals):
    """lexicographic min/max for a string/hex column (std undefined for non-numeric)."""
    c = Counter(vals)
    return OrderedDict([
        ("n", len(vals)),
        ("n_distinct", len(c)),
        ("lex_min", min(vals)),
        ("lex_max", max(vals)),
        ("lex_width_all_equal", len({len(x) for x in vals}) == 1),
        ("lex_width", sorted({len(x) for x in vals})),
        ("std", None),
        ("std_note", "string column: std undefined; see hex2int_surrogate where numeric surrogate wanted"),
        ("top_counts", c.most_common(3)),
    ])


def hex2int(vals):
    return [int(x, 16) for x in vals]


def hamming(a, b, width):
    ai, bi = int(a, 16), int(b, 16)
    return bin(ai ^ bi).count("1")


b3 = json.load(open(B3, encoding="utf-8"))
idx = json.load(open(IDX, encoding="utf-8"))
fix = json.load(open(FIX, encoding="utf-8"))

pc = b3["per_caption"]
assert len(pc) == 22, len(pc)
ids = [c["caption_id"] for c in pc]
byte_h = [c["byte_hash"] for c in pc]
sem_h = [c["semantic_hash"] for c in pc]
dual = [c["dual"] for c in pc]
dhw = [c["dual_hex_width"] for c in pc]
node_state = [c["chain"]["node_state"] for c in pc]
parent_state = [c["chain"]["parent_state"] for c in pc]
link_input = [c["chain"]["link_input"] for c in pc]
link_verified = [c["chain"]["link_verified"] for c in pc]
self_verified = [c["chain"]["self_verified_only"] for c in pc]
diff_f4_sem = [c["diff_registration_vs_f4"]["semantic_hash_identical"] for c in pc]
diff_v3_sem = [c["diff_registration_vs_v3phys"]["semantic_hash_identical"] for c in pc]
coords = [c["coords_k"] for c in pc]
cap_idx = {c["caption_id"]: c for c in idx["captions"]}
graphs = idx["graphs"]

# cross-check: index_v3 per-caption values vs B3 per-caption
xcheck = OrderedDict()
xcheck["n_id_positional_match"] = [c["caption_id"] for c in idx["captions"]] == ids
xcheck["byte_hash_all_match"] = all(cap_idx[i]["byte_hash"] == b for i, b in zip(ids, byte_h))
xcheck["semantic_hash_all_match"] = all(cap_idx[i]["semantic_hash"] == s for i, s in zip(ids, sem_h))
xcheck["dual_vs_dual_v04_all_match"] = all(cap_idx[i]["dual_v04"] == d for i, d in zip(ids, dual))
xcheck["fix_per_caption_dual_all_match"] = all(
    r["dual"] == d for r, d in zip(fix["per_caption"], dual))
xcheck["fix_per_caption_byte_hash_all_match"] = all(
    r["byte_hash"] == b for r, b in zip(fix["per_caption"], byte_h))

# ---------------- guard item 1 : dual / semantic_hash ----------------
g1 = OrderedDict()
g1["dual"] = strcol(dual)
g1["dual"]["hex2int_surrogate"] = nums(hex2int(dual))
g1["dual"]["hex2int_derivation"] = "int(hex,16) over 11 hex = 42 bit; 0 设阈值, 仅读数辅助"
g1["semantic_hash"] = strcol(sem_h)
g1["semantic_hash"]["hex2int_surrogate"] = nums(hex2int(sem_h))
g1["semantic_hash"]["hex2int_derivation"] = "int(hex,16) over 5 hex = 18 bit LSH code; 读数辅助"
g1["semantic_hash"]["popcount_18bit"] = nums([bin(int(s, 16)).count("1") for s in sem_h])
g1["semantic_hash"]["stored_distribution_crosscheck"] = OrderedDict(
    sorted(Counter(sem_h).items()))
g1["semantic_hash"]["stored_n_distinct_on_disk"] = \
    fix["readings"]["KV3DF_5_1_four_readings"]["stored_n_distinct_codes"]

# ---------------- guard item 2 : new root field ----------------
cs = b3["chain_summary"]
root_fields = OrderedDict([
    ("b3_merkle_root", cs["b3_merkle_root"]),
    ("ext_1", cs["ext_1_after_anchor2"]),
    ("state_22", cs["state_22_after_22_captions"]),
])
g2 = OrderedDict()
g2["scalar_fields"] = OrderedDict(
    (k, OrderedDict([("value", v), ("n", 1), ("n_distinct", 1),
                     ("min_lex", v), ("max_lex", v), ("std", None),
                     ("std_note", "scalar field: n=1 => std undefined (ddof=0 => 0.0)")]))
    for k, v in root_fields.items())
g2["root_triple_as_column"] = strcol(list(root_fields.values()))
g2["root_triple_as_column"]["hex2int_surrogate"] = nums(hex2int(list(root_fields.values())))
g2["old_root_literal"] = OLD_ROOT
g2["new_root_equals_old_root_bool"] = (cs["b3_merkle_root"] == OLD_ROOT)
g2["old_root_present_anywhere_in_b3"] = OLD_ROOT in json.dumps(b3, ensure_ascii=False)
g2["old_root_present_anywhere_in_index_v3"] = OLD_ROOT in json.dumps(idx, ensure_ascii=False)

# ---------------- guard item 3 : code length / dual_hex_width ----------------
g3 = OrderedDict()
g3["dual_hex_width"] = nums(dhw)
g3["dual_hex_width"]["n_distinct"] = len(set(dhw))
g3["semantic_hash_hex_width"] = nums([len(s) for s in sem_h])
g3["byte_hash_hex_width"] = nums([len(b) for b in byte_h])
g3["dual_hex_width_str"] = nums([len(d) for d in dual])
g3["caliber_code_len_bit"] = b3["caliber"]["code_len_bit"]
g3["caliber_hex_width"] = b3["caliber"]["hex_width"]
g3["caliber_d_over_2_reference"] = b3["caliber"]["d_over_2_reference"]
g3["semantic_hash_popcount"] = nums([bin(int(s, 16)).count("1") for s in sem_h])
g3["byte_hash_popcount"] = nums([bin(int(b, 16)).count("1") for b in byte_h])
g3["dual_popcount"] = nums([bin(int(d, 16)).count("1") for d in dual])
g3["link_input_char_len"] = nums([len(x) for x in link_input])

# ---------------- guard item 4 : byte_hash primary key ----------------
g4 = OrderedDict()
g4["byte_hash"] = strcol(byte_h)
g4["byte_hash"]["hex2int_surrogate"] = nums(hex2int(byte_h))
g4["byte_hash"]["hex2int_derivation"] = "int(hex,16) over 12 hex = 48 bit slice of SHA-256; 读数辅助"
g4["byte_hash_popcount"] = nums([bin(int(b, 16)).count("1") for b in byte_h])
g4["byte_hash_prefix6"] = strcol([b[:6] for b in byte_h])
g4["byte_hash_prefix6"]["hex2int_surrogate"] = nums(hex2int([b[:6] for b in byte_h]))
g4["byte_hash_suffix6"] = strcol([b[6:] for b in byte_h])
g4["byte_hash_suffix6"]["hex2int_surrogate"] = nums(hex2int([b[6:] for b in byte_h]))
g4["caption_id"] = strcol(ids)
g4["n_distinct_on_disk_declared"] = fix["degradation_guard"]["byte_hash_primary_n_distinct"]

# ---------------- guard item 5 : 22 node_state ----------------
ns_count = Counter(node_state)
dups = OrderedDict((k, v) for k, v in sorted(ns_count.items()) if v > 1)
g5 = OrderedDict()
g5["node_state"] = strcol(node_state)
g5["node_state"]["hex2int_surrogate"] = nums(hex2int(node_state))
g5["node_state"]["duplicate_count_values"] = len(dups)
g5["node_state"]["duplicates"] = dups
g5["node_state"]["n_duplicate_slots"] = sum(v - 1 for v in dups.values())
g5["parent_state"] = strcol(parent_state)
g5["parent_state"]["hex2int_surrogate"] = nums(hex2int(parent_state))
g5["parent_state"]["position0_equals_anchor0"] = (
    parent_state[0] == b3["anchors"]["values"][0])
for _i in range(1, 22):
    g5["parent_state"]["pos%d_equals_pos%d_node_state" % (_i, _i - 1)] = (
        parent_state[_i] == node_state[_i - 1])
g5["parent_state"]["chain_linkage_all_21_true"] = all(
    g5["parent_state"]["pos%d_equals_pos%d_node_state" % (_i, _i - 1)]
    for _i in range(1, 22))
g5["link_input"] = strcol(link_input)
g5["link_verified_bool_as_0_1"] = nums([1 if x else 0 for x in link_verified])
g5["self_verified_only_bool_as_0_1"] = nums([1 if x else 0 for x in self_verified])
g5["diff_f4_semantic_identical_bool"] = nums([1 if x else 0 for x in diff_f4_sem])
g5["diff_v3phys_semantic_identical_bool"] = nums([1 if x else 0 for x in diff_v3_sem])
g5["diff_f4_semantic_identical_n_distinct"] = len(set(diff_f4_sem))
g5["diff_v3phys_semantic_identical_n_distinct"] = len(set(diff_v3_sem))

# ---------------- additional unreported numeric columns (K-V3DF-0-1 "each input field / each output column") ----------------
extra = OrderedDict()
for dim in range(3):
    extra["coords_k_dim%d" % dim] = nums([c[dim] for c in coords])
norms = [sum(v * v for v in c) ** 0.5 for c in coords]
extra["coords_k_l2_norm"] = nums(norms)
extra["coords_k_l2_norm"]["n_distinct"] = len({round(x, 12) for x in norms})
for fld in ("N", "n_edges", "n_named", "n_filler", "source", "target", "seed"):
    col = [g[fld] for g in graphs]
    extra["index_v3_graphs_%s" % fld] = nums(col)
    extra["index_v3_graphs_%s" % fld]["n_distinct"] = len(set(col))
extra["index_v3_captions_n_labels"] = nums([c["n_labels"] for c in idx["captions"]])
extra["index_v3_captions_n_labels"]["n_distinct"] = len(
    {c["n_labels"] for c in idx["captions"]})
extra["index_v3_captions_text_char_len"] = nums([len(c["text"]) for c in idx["captions"]])
extra["index_v3_captions_family"] = strcol([c["family"] for c in idx["captions"]])
extra["index_v3_captions_structure"] = strcol(
    [c["structure"] for c in idx["captions"]])

# output reading columns from the post-fix readings file
h_all = [hamming(a, b, 5) for i, a in enumerate(sem_h) for b in sem_h[i + 1:]]
r51 = fix["readings"]["KV3DF_5_1_four_readings"]
readings_cols = OrderedDict()
readings_cols["hamming_pairwise_all_231"] = nums(h_all)
readings_cols["hamming_pairwise_all_231"]["n_pairs"] = len(h_all)
readings_cols["hamming_pairwise_all_231"]["mean_recompute"] = round(statistics.fmean(h_all), 6)
readings_cols["hamming_pairwise_all_231"]["mean_on_disk"] = r51["hamming_mean_observed"]
readings_cols["hamming_pairwise_all_231"]["zero_count_recompute"] = sum(1 for x in h_all if x == 0)
readings_cols["hamming_pairwise_all_231"]["zero_count_on_disk"] = r51["hamming_pairs_zero"]
readings_cols["hamming_pairwise_all_231"]["total_pairs_on_disk"] = r51["hamming_pairs_total"]
readings_cols["cluster_size_distribution_9codes"] = nums(
    list(r51["stored_distribution"].values()))
readings_cols["class_intra_hamming_4classes"] = nums(
    list(r51["class_intra_hamming"].values()))
cs_by_seed = fix["readings"]["KV3DF_5_3_cross_seed"]
readings_cols["cross_seed_n_distinct_42_48"] = nums(
    [s["n_distinct"] for s in cs_by_seed["repaired_per_seed"]])
readings_cols["cross_seed_hamming_mean_42_48"] = nums(
    [s["hamming_mean_observed"] for s in cs_by_seed["repaired_per_seed"]])
readings_cols["cross_seed_hamming_zero_42_48"] = nums(
    [s["hamming_pairs_zero"] for s in cs_by_seed["repaired_per_seed"]])
readings_cols["baseline_12bit_n_distinct_42_48"] = nums(
    [s["n_distinct"] for s in cs_by_seed["baseline_12bit_per_seed_on_disk"]])
readings_cols["svd_var_explained_k2_k3_k4"] = nums(
    [fix["input_selfcheck"]["svd_var_explained"][k]
     for k in ("2", "3", "4")])
readings_cols["d_over_2_reference_scalar"] = nums(
    [fix["readings"]["KV3DF_5_2_reference"]["d_over_2"],
     fix["readings"]["KV3DF_5_2_reference"]["code_len_bit"] / 2.0])

# declared-but-unreported fields in the post-fix readings file
declared_missing = {
    "degradation_guard_fields_reported_on_disk": sorted(fix["degradation_guard"].keys()),
    "fields_with_n_distinct_only_no_min_max_std": ["degradation_guard.* (4 n_distinct + 2 alarm bool)",
                                                   "KV3DF_5_1_four_readings.stored_n_distinct_codes",
                                                   "KV3DF_5_1_four_readings.hamming_pairs_total",
                                                   "KV3DF_5_3_cross_seed.repaired_per_seed[].n_distinct"],
    "per_caption_scalar_columns_in_fix_file": ["coords_k (3 floats x 22)"],
    "min_max_std_literal_occurrence_in_fix_file": {
        "min": json.dumps(fix).count('"min"'), "max": json.dumps(fix).count('"max"'),
        "std": json.dumps(fix).count('"std"')},
}

out = OrderedDict()
out["task_id"] = "V3X-C5B-GUARD-MINMAXSTD-2026-10-01-A1"
out["task"] = ("C5 guard-surface backfill: per-guard-item n_distinct/min/max/std "
               "for the five S9 items, recomputed now on the B3 output surface")
out["date"] = "2026-10-01"
out["generator"] = ".tmp/c5_guard_minmaxstd_2026_10_01.py"
out["scope_rule"] = ("field list follows S9 of results/c5_b_group_root_candidate_2026_10_01.md "
                     "verbatim; extra columns added only where K-V3DF-0-1 literal "
                     "('each input field / each output reading column') is unsatisfied -- "
                     "0 new threshold, 0 self-invented criterion")
out["no_verdict_notice"] = ("0 判门是否转态; PASS/FAIL/KD 归 verdict-keeper 复算. "
                            "This file reports readings only.")
out["inputs_sha12_recomputed"] = OrderedDict([
    ("results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json", sha12(B3)),
    ("corpus/v20/index_v3_2026_09_29.json", sha12(IDX)),
    ("results/c5_b_group_fix_readings_2026_10_01.json", sha12(FIX)),
])
out["input_crosscheck"] = xcheck
out["conventions"] = OrderedDict([
    ("hash", "sha256(file bytes).hexdigest()[:12] lowercase"),
    ("std_ddof0", "population std = primary reading (the 22-cell set is the whole population)"),
    ("std_ddof1", "sample std reported alongside; 0 声称与盘上其他件口径一致"),
    ("string_columns", "min/max = lexicographic; std undefined; hex->int surrogate marked as derivation"),
    ("recompute_mode", "pure local python3, 0 network, 0 key read, 0 existing file modified"),
])
out["guard_1_dual_semantic_hash"] = g1
out["guard_2_new_root_field"] = g2
out["guard_3_codelen_dual_hex_width"] = g3
out["guard_4_byte_hash_primary"] = g4
out["guard_5_node_state"] = g5
out["extra_numeric_columns"] = extra
out["output_reading_columns"] = readings_cols
out["declared_but_unreported_on_disk"] = declared_missing

with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
    f.write("\n")
print("written", OUT, sha12(OUT))
