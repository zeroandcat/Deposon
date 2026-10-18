# EXP-06 four-gap supplement : local read-only probe (tool only, not evidence)
# 0 network / 0 key / 0 existing-file write. Read-only on all evidence files.
import hashlib, json, statistics, io
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
OUT = {}

def sha256_str(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def dump_json(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=1) + "\n"

def load_json(p: Path):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

B3 = BASE / "results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json"
doc = load_json(B3)

# ---- (2) integrity chain self-verification (replicating runner verify_integrity) ----
recorded = doc["integrity"]["content_sha256"]
probe = json.loads(json.dumps(doc))
probe["integrity"]["content_sha256"] = ""
recomputed = sha256_str(dump_json(probe))
OUT["integrity_verify"] = {
    "scope": doc["integrity"]["content_hash_scope"],
    "recorded_content_sha256": recorded,
    "recomputed_content_sha256": recomputed,
    "match": recorded == recomputed,
    "path_sha256_recorded": doc["integrity"]["path_sha256"],
    "path_sha256_recomputed": sha256_str(doc["integrity"]["path_hashed"]),
    "path_match": doc["integrity"]["path_sha256"] == sha256_str(doc["integrity"]["path_hashed"]),
    "anchor_sha256_recorded": doc["integrity"]["anchor_sha256"],
    "anchor_sha256_recomputed": sha256_str("|".join(doc["anchors"]["values"])),
    "anchor_match": doc["integrity"]["anchor_sha256"] == sha256_str("|".join(doc["anchors"]["values"])),
    "self_check_integrity_results_ok": doc["self_check"]["integrity_results_ok"],
}

# ---- (4) independent re-walk of the root chain from per_caption dual values ----
ANCHORS = doc["anchors"]["values"]
state = ANCHORS[0]
for c in doc["per_caption"]:
    state = sha256_str(f"{state}|{c['caption_id']}|{c['dual']}")[:12]
state_22 = state
ext1 = sha256_str(f"{state_22}|anchor|{ANCHORS[1]}")[:12]
root = sha256_str(f"{ext1}|anchor|{ANCHORS[2]}")[:12]
OUT["rewalk"] = {
    "state_22_recomputed": state_22,
    "state_22_on_disk": doc["chain_summary"]["state_22_after_22_captions"],
    "ext_1_recomputed": ext1,
    "ext_1_on_disk": doc["chain_summary"]["ext_1_after_anchor2"],
    "merkle_root_recomputed": root,
    "merkle_root_on_disk": doc["chain_summary"]["b3_merkle_root"],
    "all_three_match": (state_22 == doc["chain_summary"]["state_22_after_22_captions"]
                         and ext1 == doc["chain_summary"]["ext_1_after_anchor2"]
                         and root == doc["chain_summary"]["b3_merkle_root"]),
    "node_state_chain_match": all(
        c["chain"]["node_state"] == sha256_str(f"{c['chain']['parent_state']}|{c['caption_id']}|{c['dual']}")[:12]
        for c in doc["per_caption"]),
}

# ---- (1) derived column (5): per-component four readings, recomputed ----
comps = [
    ("chain_summary.state_22_after_22_captions", state_22),
    ("chain_summary.ext_1_after_anchor2", ext1),
    ("chain_summary.b3_merkle_root", root),
]
per_comp = {}
for name, val in comps:
    on_disk = doc["chain_summary"][name.split(".")[1]]
    per_comp[name] = {
        "n": 1,
        "n_distinct": 1,
        "min_lex": min(on_disk, on_disk),
        "max_lex": max(on_disk, on_disk),
        "min_eq_max": on_disk == on_disk,
        "std": None,
        "std_note": "scalar field: n=1 => std undefined (ddof=0 => 0.0), reported as null, 0 fake-filled 0.0",
        "std_ddof0_numeric_surrogate": 0.0,
        "value_on_disk": on_disk,
        "value_recomputed": val,
        "match": on_disk == val,
        "hex2int_surrogate": int(on_disk, 16),
        "hex_width": len(on_disk),
    }
merged = [v for _, v in comps]
ints = [int(v, 16) for v in merged]
OUT["derived_col_5"] = {
    "definition_source": "c4e3338619c6 §5.1 item 7 / §4.2 (1 auxiliary derived column + 3 components)",
    "components_each_own_four_readings": per_comp,
    "merged_column_for_reference_only": {
        "n": 3,
        "n_distinct": len(set(merged)),
        "lex_min": min(merged),
        "lex_max": max(merged),
        "std": None,
        "std_note": "string column: std undefined",
        "hex2int_surrogate": {
            "min": min(ints), "max": max(ints),
            "mean": round(statistics.fmean(ints), 2),
            "median": statistics.median(ints),
            "std_ddof0": round(statistics.pstdev(ints), 2),
            "std_ddof1": round(statistics.stdev(ints), 2),
            "range": max(ints) - min(ints),
        },
    },
}

# ---- (2) identity check on dual_hex_width ----
widths = [c["dual_hex_width"] for c in doc["per_caption"]]
dlen = [len(c["dual"]) for c in doc["per_caption"]]
OUT["identity_check"] = {
    "field": "per_caption[].dual_hex_width",
    "n": len(widths),
    "n_distinct": len(set(widths)),
    "min": min(widths), "max": max(widths),
    "mean": statistics.fmean(widths),
    "std_ddof0": statistics.pstdev(widths),
    "all_eq_11": all(w == 11 for w in widths),
    "violations": [i for i, w in enumerate(widths) if w != 11],
    "cross_check_equals_len_dual": all(c["dual_hex_width"] == len(c["dual"]) for c in doc["per_caption"]),
    "identity_check_field_present_in_produced_file": False,
    "definition_source_on_disk": "index_v3_meta.dual_rule (in corpus/v20/index_v3_2026_10_09.json), 0 in produced file",
}

# ---- boolean / diff fields recount ----
def cnt(fn):
    vals = [fn(c) for c in doc["per_caption"]]
    return {"n": len(vals), "n_true": sum(1 for v in vals if v is True),
            "n_false": sum(1 for v in vals if v is False),
            "n_distinct": len(set(vals))}
OUT["boolean_fields"] = {
    "chain.link_verified": cnt(lambda c: c["chain"]["link_verified"]),
    "chain.self_verified_only": cnt(lambda c: c["chain"]["self_verified_only"]),
    "diff_f4.semantic_hash_identical": cnt(lambda c: c["diff_registration_vs_f4"]["semantic_hash_identical"]),
    "diff_f4.dual_identical": cnt(lambda c: c["diff_registration_vs_f4"]["dual_identical"]),
    "diff_v3phys.semantic_hash_identical": cnt(lambda c: c["diff_registration_vs_v3phys"]["semantic_hash_identical"]),
    "diff_v3phys.dual_identical": cnt(lambda c: c["diff_registration_vs_v3phys"]["dual_identical"]),
    "chain_summary.independent_rewalk_ok": {"value": doc["chain_summary"]["independent_rewalk_ok"]},
}

# ---- index_v3 integrity ----
IX = BASE / "corpus/v20/index_v3_2026_10_09.json"
ix = load_json(IX)
ixrec = ix["integrity"]["content_sha256"]
ixp = json.loads(json.dumps(ix)); ixp["integrity"]["content_sha256"] = ""
OUT["index_v3"] = {
    "generator_declared": ix["index_v3_meta"]["generator"],
    "integrity_match": ixrec == sha256_str(dump_json(ixp)),
    "n_graphs": len(ix["graphs"]), "n_captions": len(ix["captions"]),
    "family_graphs": sorted(set(g["family"] for g in ix["graphs"])),
    "family_captions": sorted(set(c["family"] for c in ix["captions"])),
    "source_graphs": sorted(set(g["source"] for g in ix["graphs"])),
}

# ---- identity-key presence scan on produced file (raw text) ----
raw = B3.read_text(encoding="utf-8")
OUT["identity_field_scan"] = {
    "identity": raw.count("identity"),
    "identity_check": raw.count("identity_check"),
    "identity_ok": raw.count("identity_ok"),
    "恒等": raw.count("恒等"),
    "note": "'ident' 92 hits are substring of *_identical keys, not an identity-check field",
}

print(json.dumps(OUT, ensure_ascii=False, indent=1))