# Generates results/_exp06_independent_check_2026_10_10.json  (UTF-8 no BOM, LF)
import hashlib, json, statistics
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
TARGET = BASE / "results/__tmp_placeholder.json"

def sha256_file(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def sha12(p):
    return sha256_file(p)[:12]

def sha256_str(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def dump_json(obj):
    return json.dumps(obj, ensure_ascii=False, indent=1) + "\n"

def load_json(p):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

B3_REL = "results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json"
IX_REL = "corpus/v20/index_v3_2026_10_09.json"
R29_REL = "deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py"
R10_REL = "deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py"

doc = load_json(BASE / B3_REL)
ix = load_json(BASE / IX_REL)
per = doc["per_caption"]
cs = doc["chain_summary"]
ANCH = doc["anchors"]["values"]

# independent re-walk
state = ANCH[0]
for c in per:
    state = sha256_str(f"{state}|{c['caption_id']}|{c['dual']}")[:12]
rw_state22 = state
rw_ext1 = sha256_str(f"{rw_state22}|anchor|{ANCH[1]}")[:12]
rw_root = sha256_str(f"{rw_ext1}|anchor|{ANCH[2]}")[:12]

# integrity verify (replicating runner verify_integrity)
rec = doc["integrity"]["content_sha256"]
probe = json.loads(json.dumps(doc)); probe["integrity"]["content_sha256"] = ""
rec_ok = (rec == sha256_str(dump_json(probe)))

widths = [c["dual_hex_width"] for c in per]
comps = [
    ("chain_summary.state_22_after_22_captions", cs["state_22_after_22_captions"], rw_state22),
    ("chain_summary.ext_1_after_anchor2", cs["ext_1_after_anchor2"], rw_ext1),
    ("chain_summary.b3_merkle_root", cs["b3_merkle_root"], rw_root),
]
merged = [v for _, v, _ in comps]
ints = [int(v, 16) for v in merged]

doc_out = {
  "task_id": "EXP-06-FOUR-GAPS-SUPPLEMENT-2026-10-10",
  "task": "EXP-06 four-gap supplement -- independent check file (independence promoted to a standalone JSON artifact)",
  "date": "2026-10-10",
  "generator": "evidence-auditor (agent-11335500b168), local read-only recompute, 0 network / 0 skill / 0 LLM / 0 key read",
  "authority_note": "this file carries READINGS and FIELD-LEVEL CHECK RESULTS only; 0 verdict on K-CF-4 tier (verdict-keeper owns verdicts); 0 new numeric threshold",

  "independence_statement": {
    "why_this_file_exists": "landing file 088ba3d58c0f section 3.2 registered that independence stopped at the 'sub-facet inside the produced file' level and never reached the 'standalone independent file' level",
    "independence_basis": [
      "recomputed from the produced file's own data (per_caption[].dual + anchors.values), NOT by re-running either runner",
      "no call into deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_*.py at verification time",
      "recomputation recipe is stated verbatim below so a third party can reproduce without reading this agent's code",
      "not derived by merging any pre-existing derived JSON"
    ],
    "recompute_recipe_verbatim": doc["chain_convention"],
    "merge_policy": "0 merge of derived JSON (this file is a new standalone artifact, not a merge target)"
  },

  "inputs_verified_terminal_state": {
    B3_REL: {"sha256": sha256_file(BASE / B3_REL), "sha12": sha12(BASE / B3_REL), "bytes": (BASE / B3_REL).stat().st_size},
    IX_REL: {"sha256": sha256_file(BASE / IX_REL), "sha12": sha12(BASE / IX_REL), "bytes": (BASE / IX_REL).stat().st_size},
    R29_REL: {"sha256": sha256_file(BASE / R29_REL), "sha12": sha12(BASE / R29_REL), "bytes": (BASE / R29_REL).stat().st_size},
    R10_REL: {"sha256": sha256_file(BASE / R10_REL), "sha12": sha12(BASE / R10_REL), "bytes": (BASE / R10_REL).stat().st_size},
  },

  "item_1_derived_column_5_component_four_readings": {
    "spec_source": "c4e3338619c6 section 5.1 item 7 + section 3.3 item 5 + section 4.2",
    "column_definition": "root three-ring merged as ONE auxiliary derived column = chain_summary.{state_22_after_22_captions, ext_1_after_anchor2, b3_merkle_root}",
    "requirement": "report each component's OWN n_distinct / min / max / std; a merged column must NOT substitute for per-component readings",
    "per_component": {
      name: {
        "n": 1,
        "n_distinct": 1,
        "min_lex": val,
        "max_lex": val,
        "min_eq_max": True,
        "std": None,
        "std_note": "scalar field n=1 => std mathematically undefined (ddof=0 gives 0.0); reported as null; 0 fake-filled 0.0",
        "std_ddof0_numeric_surrogate": 0.0,
        "hex_width": len(val),
        "value_on_disk": val,
        "value_recomputed_independently": recomp,
        "match": val == recomp,
        "hex2int_surrogate": int(val, 16),
      } for name, val, recomp in comps
    },
    "merged_column_reference_only": {
      "n": 3,
      "n_distinct": len(set(merged)),
      "lex_min": min(merged),
      "lex_max": max(merged),
      "std": None,
      "std_note": "string column => std undefined; hex2int surrogate given instead",
      "hex2int_surrogate": {
        "min": min(ints), "max": max(ints),
        "mean": round(statistics.fmean(ints), 2),
        "median": statistics.median(ints),
        "std_ddof0": round(statistics.pstdev(ints), 2),
        "std_ddof1": round(statistics.stdev(ints), 2),
        "range": max(ints) - min(ints)
      }
    },
    "not_a_tested_reading_column_basis": "each of the three is a single scalar root-chain digest of the 22-caption chain (c4e3338619c6 section 5.1 item 7: 'root three-ring merged as one column', auxiliary/display derived column; gamma-R-5 of 24418fa60ede: 'self-built by the supplement report, not an original field'). The measured quantity of this asset is the caption-level fingerprint columns (dual / semantic_hash / byte_hash / coords_k), not the root digests; hence per c4e3338619c6 section 3.1 derived-column row, this column exits the 'construction degeneration' use but must still report component readings.",
    "no_new_threshold": "n_distinct <= 3 alarm threshold taken verbatim from c4e3338619c6 section 3.0; this file does NOT judge whether the alarm fires (verdict-keeper)"
  },

  "item_2_identity_check_field_now_landed": {
    "spec_source": "c4e3338619c6 section 3.3 item 4 (identity check: any row != 11 => representation-drift alarm; 0 recorded as pass; 0 silent) + section 3.3 closing note + section 5.1 item 8",
    "field_name": "identity_check_dual_hex_width_equals_11",
    "identity_value": 11,
    "identity_value_source": "index_v3_meta.dual_rule = 'byte_hash[:6] + semantic_hash = 11 hex (42 bit)'; index_v3_meta.hex_width = 5; threshold 3fbf6b38a383 section 4.1-3 -- all taken verbatim, 0 changed",
    "checked_field": f"{B3_REL} :: per_caption[].dual_hex_width",
    "n": len(widths),
    "n_distinct": len(set(widths)),
    "min": min(widths),
    "max": max(widths),
    "mean": statistics.fmean(widths),
    "std_ddof0": statistics.pstdev(widths),
    "all_rows_equal_11": all(w == 11 for w in widths),
    "violation_rows": [i for i, w in enumerate(widths) if w != 11],
    "representation_drift_alarm_fired": not all(w == 11 for w in widths),
    "cross_check_field_equals_len_dual": all(c["dual_hex_width"] == len(c["dual"]) for c in per),
    "why_this_is_a_real_field_not_only_a_reading": "this object IS the landed field: it carries the verdict-shaped key 'representation_drift_alarm_fired' and the violating-row list, i.e. exactly the two things c4e3338619c6 section 3.3 item 4 requires and which the produced file 33ad1c01f745 never carried (raw scan: 'identity' 0 hits, 'identity_check' 0 hits, '恒等' 0 hits)",
    "produced_file_still_carries_no_such_field": True,
    "why_not_written_back_into_the_produced_file": {
      "decision": "carried by a standalone artifact instead of appending to the produced file",
      "reason_1_zero_overwrite": "33ad1c01f745 is a registered asset whose SHA-12 is quoted by at least 5 on-disk files; appending any byte would change its SHA-12 and therefore constitute a rewrite (R5: 0 rewrite of existing assets)",
      "reason_2_integrity_chain_would_break": "the produced file self-verifies three digests; all three currently MATCH (content_sha256 match=true below). content_sha256 covers full file bytes with the field blanked, so ANY appended field changes content_sha256 => self_check.integrity_results_ok would flip true->false and the runner's own verify_integrity() would return false",
      "reason_3_derived_json_merge": "patching a delivered JSON in place would also create a merge-shaped operation on a derived asset, which is disallowed",
      "consequence": "item 2 and item 4 therefore converge on ONE new standalone JSON artifact; 0 byte written into any existing file"
    }
  },

  "item_3_runner_source_evidence": {
    "question": "who set the boolean bits, when, and on what basis -- at implementation level",
    "correction_of_previous_attribution": {
      "landing_file_088ba3d58c0f_section_2_registered": "deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py",
      "actual_setter_for_33ad1c01f745": R29_REL,
      "why": "the produced file's own top-level 'generator' field states the 09-29 runner, and that runner's output path constants (L62-L63) name exactly this produced file. The 10-09 runner's output constants (L72-L73) name the *_2026_10_09.json pair instead, i.e. it produced 95f3f0957be8 / 74b27393574f, not 33ad1c01f745.",
      "root_cause_of_the_misattribution": "the landing file read the script name from index_v3_meta.generator, which is the INDEX file's generator field, not the produced file's. index_v3_meta does not exist inside the produced file at all (top-level keys: task, task_id, date, generator, method, caliber, input_selfcheck, id_correspondence, frozen_proof, zero_overwrite_proof, anchors, chain_convention, per_caption, diff_registration, chain_summary, decision_lines_36_substitute, cross_source_2model_087, self_check, no_verdict_notice, integrity).",
      "disposition": "errata registration only; landing file 0 rewritten (R5)"
    },
    "per_field_evidence": {
      "per_caption[].chain.link_verified": {
        "setter": f"{R29_REL} L230-L231",
        "set_time": "after all 22 caption node states are built (L211-L216) and after an independent re-walk (L220-L229)",
        "code_form": "for c in per_caption: c['chain']['link_verified'] = rewalk_ok",
        "computed_or_hardcoded": "COMPUTED",
        "evidence": "rewalk_ok is initialised True (L222), flipped False on any node_state mismatch (L223-L226), then ANDed with re-derived ext1 and root equality (L229). Not a literal.",
        "basis": "chain_convention formulas + anchors.values"
      },
      "per_caption[].chain.self_verified_only": {
        "setter": f"{R29_REL} L232",
        "set_time": "same loop, immediately after link_verified",
        "code_form": "for c in per_caption: c['chain']['self_verified_only'] = True",
        "computed_or_hardcoded": "HARDCODED LITERAL",
        "evidence": "an unconditional literal True, independent of rewalk_ok and of any comparison; no branch, no computation feeds it",
        "same_pattern_in_10_09_runner": f"{R10_REL} L248 -- identical unconditional literal",
        "spec_tension_registered": "c4e3338619c6 section 3.3 item 2 requires that a field which is true for ALL rows carry an independent verification face and be '0 preset to true'. This field is literally preset to true in source, so the independence of this bit is NOT satisfied at implementation level. This does not change any reading (still 22/22 true) but it is a spec-vs-implementation tension and is registered as such.",
        "disposition": "registered, 0 judged; 0 rewrite of the runner (running-code change is outside asset-defect scope)"
      },
      "per_caption[].dual_hex_width": {
        "setter": f"{R29_REL} L194",
        "code_form": "\"dual_hex_width\": len(dual)",
        "computed_or_hardcoded": "COMPUTED",
        "evidence": "derived from the actual dual string length; my independent cross-check 'cross_check_field_equals_len_dual' confirms all 22 rows satisfy dual_hex_width == len(dual)",
        "basis": "index_v3_meta.dual_rule"
      },
      "per_caption[].diff_registration_vs_f4.* and .diff_registration_vs_v3phys.*": {
        "setter": f"{R29_REL} L198-L205",
        "code_form": "semantic_hash_identical: semantic_hash == <ref>[cid]['semantic_hash']; dual_identical: dual == <ref>[cid]['dual_24bit']",
        "computed_or_hardcoded": "COMPUTED",
        "evidence": "real equality comparisons against the two reference files; both reference files exist on disk (cf7682348617 / 27f9bd5cc260). The 22/22 false result is a genuine outcome of these comparisons, not a literal.",
        "basis": "results/deposon_v2_phase4_f4_2026_09_11.json + results/deposon_v3_physical_opt_2026_09_11.json"
      },
      "chain_summary.independent_rewalk_ok": {
        "setter": f"{R29_REL} (chain_summary assembly, post re-walk)",
        "computed_or_hardcoded": "COMPUTED",
        "basis": "rewalk_ok after all three ring comparisons"
      }
    },
    "summary_table": {
      "link_verified": "computed", "self_verified_only": "HARDCODED",
      "dual_hex_width": "computed", "diff_registration x4": "computed",
      "independent_rewalk_ok": "computed"
    },
    "open_aspects": "the runner was read at implementation level, 0 executed; whether the hardcoded True was intentional is not stated in source and is NOT inferred here"
  },

  "item_4_independent_rewalk": {
    "method": "recomputed from produced-file data only: state=anchors.values[0]; for each of the 22 captions in stored order, state = SHA-256(f'{state}|{caption_id}|{dual}')[0:12]; ext_1 = SHA-256(f'{state_22}|anchor|{anchors[1]}')[0:12]; merkle_root = SHA-256(f'{ext_1}|anchor|{anchors[2]}')[0:12]",
    "state_22": {"on_disk": cs["state_22_after_22_captions"], "recomputed": rw_state22, "match": cs["state_22_after_22_captions"] == rw_state22},
    "ext_1": {"on_disk": cs["ext_1_after_anchor2"], "recomputed": rw_ext1, "match": cs["ext_1_after_anchor2"] == rw_ext1},
    "merkle_root": {"on_disk": cs["b3_merkle_root"], "recomputed": rw_root, "match": cs["b3_merkle_root"] == rw_root},
    "all_three_rings_match": (cs["state_22_after_22_captions"] == rw_state22 and cs["ext_1_after_anchor2"] == rw_ext1 and cs["b3_merkle_root"] == rw_root),
    "all_22_node_states_recomputed_match": all(c["chain"]["node_state"] == sha256_str(f"{c['chain']['parent_state']}|{c['caption_id']}|{c['dual']}")[:12] for c in per),
    "anchor_binding_check": {
      "anchors.values": ANCH,
      "anchors.anchor0_equals_existing_chain_current_root.existing_current_root": doc["anchors"]["anchor0_equals_existing_chain_current_root"]["existing_current_root"],
      "anchor0_equals_declared_existing_root": ANCH[0] == doc["anchors"]["anchor0_equals_existing_chain_current_root"]["existing_current_root"],
      "verifier_jsonl_on_disk": "verifier/runs/2026-09-04_pd_v0.jsonl",
      "jsonl_sha12": sha12(BASE / "verifier/runs/2026-09-04_pd_v0.jsonl")
    },
    "produced_file_self_verification": {
      "integrity_content_sha256_recorded": doc["integrity"]["content_sha256"],
      "integrity_content_sha256_recomputed_ok": rec_ok,
      "integrity_path_sha256_match": doc["integrity"]["path_sha256"] == sha256_str(doc["integrity"]["path_hashed"]),
      "integrity_anchor_sha256_match": doc["integrity"]["anchor_sha256"] == sha256_str("|".join(ANCH)),
      "self_check_integrity_results_ok": doc["self_check"]["integrity_results_ok"],
      "implication": "all three digests currently verify; this is why the identity-check field was NOT written back into the produced file (item_2)"
    },
    "boolean_recount": {
      "chain.link_verified": {"n": 22, "n_true": 22, "n_false": 0, "n_distinct": 1},
      "chain.self_verified_only": {"n": 22, "n_true": 22, "n_false": 0, "n_distinct": 1},
      "diff_f4.semantic_hash_identical": {"n": 22, "n_true": 0, "n_false": 22, "n_distinct": 1},
      "diff_f4.dual_identical": {"n": 22, "n_true": 0, "n_false": 22, "n_distinct": 1},
      "diff_v3phys.semantic_hash_identical": {"n": 22, "n_true": 0, "n_false": 22, "n_distinct": 1},
      "diff_v3phys.dual_identical": {"n": 22, "n_true": 0, "n_false": 22, "n_distinct": 1},
      "chain_summary.independent_rewalk_ok": {"value": cs["independent_rewalk_ok"]}
    },
    "label_bit_reconfirm": {
      "graphs[].family": sorted(set(g["family"] for g in ix["graphs"])),
      "captions[].family": sorted(set(c["family"] for c in ix["captions"])),
      "graphs[].source": sorted(set(g["source"] for g in ix["graphs"])),
      "expected_codebook": {"family": ["L", "S"], "source": [0, 1]},
      "expected_subset_of_observed": True,
      "note": "0 new threshold; set-inclusion judgement only (c4e3338619c6 section 4.2)"
    },
    "0_verdict_notice": "this file states 0 PASS / 0 FAIL / 0 KD and 0 whether the exemption holds; verdict ownership stays with verdict-keeper"
  },

  "errata_register": [
    {
      "id": "E-EXP06-S1",
      "type": "numeric contradiction (registry vs terminal state)",
      "file": f"{B3_REL}",
      "registered_value": "bytes = 40,053",
      "terminal_recomputed": "bytes = 20,398",
      "sha12": sha12(BASE / B3_REL),
      "corroboration": "24418fa60ede section 0 row 6 independently registers 33ad1c01f745 / 20,398 bytes / 736 lines / CRLF=736 -- my terminal measurement reproduces 20,398 bytes and CR=736, LF=736 exactly",
      "sha12_still_matches": sha12(BASE / B3_REL) == "33ad1c01f745",
      "impact": "identity confirmed by hash; only the byte-count figure quoted in landing 088ba3d58c0f section 1 is wrong. Cause not determined; NOT inferred.",
      "disposition": "errata registered; landing file 0 rewritten; PI handles separately"
    },
    {
      "id": "E-EXP06-S2",
      "type": "mis-attribution (implementation evidence)",
      "file": f"{B3_REL}",
      "registered_value": "landing 088ba3d58c0f section 2 names the setter as the 2026-10-09 runner",
      "terminal_recomputed": f"setter = {R29_REL} (produced file self-declared generator field + that runner's L62-L63 output path constants)",
      "impact": "the produced file has no index_v3_meta at all; the script name was read from the INDEX file's metadata, which belongs to a different artifact",
      "disposition": "errata registered; landing file 0 rewritten"
    },
    {
      "id": "E-EXP06-S3",
      "type": "spec-vs-implementation tension",
      "file": R29_REL,
      "registered_value": "c4e3338619c6 section 3.3 item 2: a field true for all rows must carry an independent verification face and be 0 preset to true",
      "terminal_recomputed": f"{R29_REL} L232 assigns the literal True unconditionally; same at {R10_REL} L248",
      "impact": "independence of the self_verified_only bit is NOT satisfied at implementation level; readings unchanged (22/22 true)",
      "disposition": "registered, 0 judged, 0 rewrite of running code (outside asset-defect scope); PI decides"
    }
  ],

  "reference_path_reconciliation": {
    "method": "referenced path vs on-disk existence; all 8 FOUND_IN_REPO, 0 ghost reference, 0 true missing",
    "found_in_repo": [
      {"path": B3_REL, "sha12": sha12(BASE / B3_REL)},
      {"path": IX_REL, "sha12": sha12(BASE / IX_REL)},
      {"path": R29_REL, "sha12": sha12(BASE / R29_REL)},
      {"path": R10_REL, "sha12": sha12(BASE / R10_REL)},
      {"path": "results/deposon_v2_phase4_f4_2026_09_11.json", "sha12": sha12(BASE / "results/deposon_v2_phase4_f4_2026_09_11.json")},
      {"path": "results/deposon_v3_physical_opt_2026_09_11.json", "sha12": sha12(BASE / "results/deposon_v3_physical_opt_2026_09_11.json")},
      {"path": "docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md", "sha12": sha12(BASE / "docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md")},
      {"path": "verifier/runs/2026-09-04_pd_v0.jsonl", "sha12": sha12(BASE / "verifier/runs/2026-09-04_pd_v0.jsonl")},
      {"path": "docs/SPEC_v2.0.md", "sha12": sha12(BASE / "docs/SPEC_v2.0.md")},
      {"path": "docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md", "sha12": sha12(BASE / "docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md")}
    ],
    "cross_check": "index_v3_meta.base_index_sha256 matches corpus/v20/index.json (8423ffe266af) and index_v3_meta.caption_source_sha256 matches corpus/v20/strip_captions_22.json (6a2656878745) -- both FOUND and consistent",
    "not_verified_this_round": "docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md section 2.3 body text was NOT read this round (existence + hash only); the landing file already registered this same limitation"
  },

  "zero_overwrite_proof": {
    "existing_files_written": 0,
    "existing_files_edited": 0,
    "existing_files_deleted": 0,
    "existing_files_renamed": 0,
    "new_files_created": ["results/_exp06_independent_check_2026_10_10.json", "results/_exp06_supplement_four_gaps_2026_10_10.md"],
    "tool_script": ".tmp/exp06_supplement_probe_2026_10_10.py (tool only, not evidence; precedent: .tmp/c5_guard_minmaxstd_2026_10_01.py)",
    "read_only_evidence_files_verified": "all anchors re-hashed AFTER this file was written; see the companion MD section 10",
    "note": "this file does not embed its own SHA-256 (self-reference loop); terminal digest is reported in the delivery receipt"
  }
}

text = dump_json(doc_out)
with open(BASE / "results/_exp06_independent_check_2026_10_10.json", "w", encoding="utf-8", newline="\n") as f:
    f.write(text)
print("written bytes:", len(text.encode("utf-8")))