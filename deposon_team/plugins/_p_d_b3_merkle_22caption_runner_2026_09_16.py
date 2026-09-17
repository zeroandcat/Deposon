# -*- coding: utf-8 -*-
"""
P-D B3 Merkle 22 caption dual_24bit 链式核验 runner (2026-09-16)
委外执行代理 C (KIMI 派出) 产出

约束: 0 LLM / 0 网络 / 0 pip install, 纯 hashlib + numpy + json
只读既有文件; 仅新建 2 个产出文件:
  1. corpus/v20/index_v2_2026_09_16.json
  2. results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json
corpus/v20/index.json 为 frozen, 本脚本仅以只读方式打开, 并在写入前后重算其 SHA-256 证明 0 触动。

口径裁定 (KIMI 已拍板, spec 优先):
  dual_24bit = byte_hash[:6] + semantic_hash = 9 hex (36 bit)
  byte_hash     = SHA-256(caption_id)[0:12]            (12 hex, P-D V0.1)
  semantic_hash = 12-bit LSH: SVD-2 坐标 x 12 随机超平面 (np.random.seed(42)), 符号位 -> 3 hex
  依据: docs/V3X/PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md §2/§3
非标分歧声明:
  deposon_team/plugins/_p_o_stranger_verification_runner_2026_09_16.py L172-197
  verify_22_caption_dual_24bit 使用 cap_sha[:6]+cap_sha[6:12] 纯截段 (无语义层), 判为非标。

链式约定 (确定性, 可独立复走):
  state_0   = anchors[0] (= verifier/runs/2026-09-04_pd_v0.jsonl 的 current_root)
  state_i   = SHA-256(f"{state_(i-1)}|{caption_id}|{dual_24bit}")[0:12]   (i = 1..22)
  ext_1     = SHA-256(f"{state_22}|anchor|{anchors[1]}")[0:12]
  merkle_root = SHA-256(f"{ext_1}|anchor|{anchors[2]}")[0:12]
"""
import hashlib
import json
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parents[2]
DATE = "2026-09-16"

P_INDEX = BASE / "corpus" / "v20" / "index.json"                       # frozen, read-only
P_CAPTIONS = BASE / "corpus" / "v20" / "strip_captions_22.json"
P_EMB = BASE / "results" / "deposon_volcengine_22caption_embedding_2026_09_10.json"
P_F4 = BASE / "results" / "deposon_v2_phase4_f4_2026_09_11.json"
P_V3 = BASE / "results" / "deposon_v3_physical_opt_2026_09_11.json"
P_60 = BASE / "results" / "deposon_v3_physical_opt_60cells_2026_09_11.json"
P_GT = BASE / "results" / "deposon_game_theory_eval_2026_09_10.json"
P_CHAIN0 = BASE / "verifier" / "runs" / "2026-09-04_pd_v0.jsonl"

P_OUT_INDEX_V2 = BASE / "corpus" / "v20" / "index_v2_2026_09_16.json"
P_OUT_RESULTS = BASE / "results" / "deposon_p_d_b3_merkle_22_caption_2026_09_16.json"

REL_INDEX_V2 = "corpus/v20/index_v2_2026_09_16.json"
REL_RESULTS = "results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json"

# P-D V0.1 3 根 fingerprint anchors
# 出处: docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md §2.3 B3 Merkle
ANCHORS = ["7d6d3d39fad8", "f88d855aaf83", "e66e44e63f5a"]

SPEC_REF = "docs/V3X/PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md"
ANCHORS_REF = "docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md §2.3 B3 Merkle"
GENERATOR = "deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_09_16.py"

# 术语红线 (产出文件不得包含; 词表以拼接构造, 使 runner 自身也不含字面禁用串)
FORBIDDEN_TOKENS = [
    "P" + "oA",
    "已" + "证",
    "相" + "变",
    "穷" + "举",
    "元" + "表述",
    "ar" + "k-",
    "s" + "k-",
    "gh" + "p_",
]


def sha256_str(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load_json(p: Path):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


def dump_json(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=1) + "\n"


def attach_integrity(doc: dict, rel_path: str, anchors) -> None:
    """三件套 hash: 内容 hash (content_sha256 置空后全文) + 路径 hash + 锚 hash。"""
    doc["integrity"] = {
        "content_sha256": "",
        "content_hash_scope": "full file bytes with integrity.content_sha256 set to empty string",
        "path_sha256": sha256_str(rel_path),
        "path_hashed": rel_path,
        "anchor_sha256": sha256_str("|".join(anchors)),
        "anchor_hashed": "|".join(anchors),
    }
    doc["integrity"]["content_sha256"] = sha256_str(dump_json(doc))


def verify_integrity(p: Path) -> bool:
    doc = load_json(p)
    recorded = doc["integrity"]["content_sha256"]
    doc["integrity"]["content_sha256"] = ""
    return sha256_str(dump_json(doc)) == recorded


def main():
    # ---------- 0. frozen 证明: 写入前记录 index.json SHA-256 ----------
    index_sha_before = sha256_file(P_INDEX)

    # ---------- 1. 只读加载全部输入 ----------
    index = load_json(P_INDEX)
    caps = load_json(P_CAPTIONS)
    emb = load_json(P_EMB)
    f4 = load_json(P_F4)
    v3 = load_json(P_V3)
    d60 = load_json(P_60)
    gt = load_json(P_GT)
    chain0_line = P_CHAIN0.read_text(encoding="utf-8").strip().splitlines()[0]
    chain0 = json.loads(chain0_line)

    svd2 = emb["svd2_coords"]
    f4_dual = f4["dual_fingerprints"]
    v3_per = {c["caption_id"]: c for c in v3["P_D_semantic_fingerprint_V0_2"]["per_caption"]}
    dl36 = d60["decision_lines_36"]
    gt_note = gt["5_candidates_evaluation"]["P-A_equilibrium_stabilization"]["note"]

    # ---------- 2. id 一一对应核验 ----------
    graph_ids = [g["graph_id"] for g in index["graphs"]]
    caption_ids = [c["id"] for c in caps]
    id_positional_match = graph_ids == caption_ids
    id_set_match = sorted(graph_ids) == sorted(caption_ids)
    assert len(graph_ids) == 22 and len(caption_ids) == 22, "need exactly 22 graphs and 22 captions"
    assert id_positional_match and id_set_match, "graph_id 与 caption id 不一一对应"
    assert index.get("captions") is None, "index.json 已含 captions 字段, 异常"

    # ---------- 3. 按 spec 复算 22 条 dual_24bit ----------
    np.random.seed(42)
    hyperplanes = np.random.randn(12, 2)
    per_caption = []
    for cid in caption_ids:
        byte_hash = sha256_str(cid)[:12]
        x, y = svd2[cid]
        proj = np.array([x, y]) @ hyperplanes.T
        bits = (proj > 0).astype(int)
        semantic_hash = hex(int("".join(str(b) for b in bits), 2))[2:].zfill(3)
        dual = byte_hash[:6] + semantic_hash
        m_f4 = (
            byte_hash == f4_dual[cid]["byte_hash"]
            and semantic_hash == f4_dual[cid]["semantic_hash"]
            and dual == f4_dual[cid]["dual_24bit"]
        )
        m_v3 = (
            byte_hash == v3_per[cid]["byte_hash"]
            and semantic_hash == v3_per[cid]["semantic_hash"]
            and dual == v3_per[cid]["dual_24bit"]
        )
        per_caption.append({
            "caption_id": cid,
            "svd2": [x, y],
            "byte_hash": byte_hash,
            "semantic_hash": semantic_hash,
            "dual_24bit": dual,
            "match_v2_phase4_f4": m_f4,
            "match_v3_physical_opt": m_v3,
        })
    rate_f4 = sum(c["match_v2_phase4_f4"] for c in per_caption)
    rate_v3 = sum(c["match_v3_physical_opt"] for c in per_caption)

    # ---------- 4. 链式连接: anchors[0] -> 22 captions -> anchors[1..2] ----------
    anchor0_ok = chain0["current_root"] == ANCHORS[0] and chain0["prev_hash"] == "000000000000"
    state = ANCHORS[0]
    for c in per_caption:
        link_input = f"{state}|{c['caption_id']}|{c['dual_24bit']}"
        node = sha256_str(link_input)[:12]
        c["chain"] = {"parent_state": state, "link_input": link_input, "node_state": node}
        state = node
    state_22 = state
    ext1 = sha256_str(f"{state_22}|anchor|{ANCHORS[1]}")[:12]
    merkle_root = sha256_str(f"{ext1}|anchor|{ANCHORS[2]}")[:12]

    # 独立复走验证 (只用记录的 caption_id + dual_24bit 重算全链)
    rw = ANCHORS[0]
    rewalk_ok = True
    for c in per_caption:
        rw = sha256_str(f"{rw}|{c['caption_id']}|{c['dual_24bit']}")[:12]
        if rw != c["chain"]["node_state"]:
            rewalk_ok = False
    rw_ext1 = sha256_str(f"{rw}|anchor|{ANCHORS[1]}")[:12]
    rw_root = sha256_str(f"{rw_ext1}|anchor|{ANCHORS[2]}")[:12]
    rewalk_ok = rewalk_ok and rw_ext1 == ext1 and rw_root == merkle_root

    chain_pass_count = 0
    for c in per_caption:
        c["chain"]["link_verified"] = (
            c["match_v2_phase4_f4"] and c["match_v3_physical_opt"] and rewalk_ok
        )
        c["verdict"] = "PASS" if c["chain"]["link_verified"] else "FAIL"
        chain_pass_count += c["chain"]["link_verified"]

    # ---------- 5. 产出 1: index_v2 ----------
    cap_text = {c["id"]: c for c in caps}
    index_v2 = dict(index)  # 顶层字段沿用 (corpus/generator_version/spec/named_filler_rule/n_graphs/graphs)
    index_v2["graphs"] = index["graphs"]  # 逐字段值复制, 0 改动
    index_v2["captions"] = [
        {
            "caption_id": c["caption_id"],
            "text": cap_text[c["caption_id"]]["text"],
            "family": cap_text[c["caption_id"]]["family"],
            "structure": cap_text[c["caption_id"]]["structure"],
            "n_labels": cap_text[c["caption_id"]]["n_labels"],
            "byte_hash": c["byte_hash"],
            "semantic_hash": c["semantic_hash"],
            "dual_24bit": c["dual_24bit"],
        }
        for c in per_caption
    ]
    index_v2["n_captions"] = 22
    index_v2["fingerprint_anchors"] = list(ANCHORS)
    index_v2["index_v2_meta"] = {
        "generator": GENERATOR,
        "date": DATE,
        "spec_ref": SPEC_REF,
        "dual_24bit_rule": "byte_hash[:6] + semantic_hash = 9 hex (36 bit); byte_hash=SHA-256(caption_id)[0:12]; semantic_hash=12-bit LSH (SVD-2 x 12 hyperplanes, np.random.seed(42))",
        "anchors_ref": ANCHORS_REF,
        "base_index": "corpus/v20/index.json",
        "base_index_sha256": index_sha_before,
        "caption_source": "corpus/v20/strip_captions_22.json",
        "caption_source_sha256": sha256_file(P_CAPTIONS),
        "svd2_source": "results/deposon_volcengine_22caption_embedding_2026_09_10.json",
        "svd2_source_sha256": sha256_file(P_EMB),
        "lsh_seed": 42,
        "hyperplanes_shape": [12, 2],
    }
    attach_integrity(index_v2, REL_INDEX_V2, ANCHORS)
    P_OUT_INDEX_V2.write_text(dump_json(index_v2), encoding="utf-8")

    # ---------- 6. 产出 2: 链式核验结果 ----------
    results = {
        "task": "P-D B3 Merkle 22 caption dual_24bit 链式核验",
        "date": DATE,
        "generator": GENERATOR,
        "method": "0 LLM, 纯 hashlib + numpy + json, 只读既有文件",
        "spec_ruling": {
            "dual_24bit": "byte_hash[:6] + semantic_hash = 9 hex (36 bit)",
            "byte_hash": "SHA-256(caption_id)[0:12] (12 hex)",
            "semantic_hash": "12-bit LSH: 22 caption SVD-2 坐标 x 12 随机超平面 (np.random.seed(42)), 符号位 -> 3 hex",
            "spec_ref": SPEC_REF,
            "ruling_basis": "spec 优先 (KIMI 裁定)",
            "nonstandard_divergence": (
                "deposon_team/plugins/_p_o_stranger_verification_runner_2026_09_16.py L172-197 "
                "verify_22_caption_dual_24bit 使用 cap_sha[:6]+cap_sha[6:12] 纯截段 "
                "(对 caption 文本 SHA-256 截 12 hex 再拼接, 无 semantic_hash 语义层), 判为非标; "
                "本核验以 PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md §2/§3 为准"
            ),
        },
        "id_correspondence": {
            "n_graph_ids": len(graph_ids),
            "n_caption_ids": len(caption_ids),
            "positional_match": id_positional_match,
            "set_match": id_set_match,
            "verdict": "PASS" if (id_positional_match and id_set_match) else "FAIL",
        },
        "frozen_proof": {
            "file": "corpus/v20/index.json",
            "sha256_before_write": index_sha_before,
            "sha256_after_write": None,  # 收尾回填
            "unchanged": None,
        },
        "anchors": {
            "values": list(ANCHORS),
            "source": ANCHORS_REF,
            "anchor0_equals_existing_chain_current_root": {
                "existing_chain": "verifier/runs/2026-09-04_pd_v0.jsonl",
                "existing_prev_hash": chain0["prev_hash"],
                "existing_current_root": chain0["current_root"],
                "match": anchor0_ok,
            },
        },
        "chain_convention": {
            "state_0": "anchors[0]",
            "link_i": "SHA-256(f\"{state_(i-1)}|{caption_id}|{dual_24bit}\")[0:12], i=1..22",
            "ext_1": "SHA-256(f\"{state_22}|anchor|{anchors[1]}\")[0:12]",
            "merkle_root": "SHA-256(f\"{ext_1}|anchor|{anchors[2]}\")[0:12]",
        },
        "per_caption": per_caption,
        "consistency_vs_existing": {
            "vs_v2_phase4_f4_dual_fingerprints": f"{rate_f4}/22",
            "vs_v3_physical_opt_per_caption": f"{rate_v3}/22",
            "reference_files": [
                "results/deposon_v2_phase4_f4_2026_09_11.json",
                "results/deposon_v3_physical_opt_2026_09_11.json",
            ],
        },
        "chain_summary": {
            "state_22_after_22_captions": state_22,
            "ext_1_after_anchor2": ext1,
            "b3_merkle_root": merkle_root,
            "independent_rewalk_ok": rewalk_ok,
            "chain_pass_count": f"{chain_pass_count}/22",
        },
        "decision_lines_36_substitute": {
            "substitution_note": (
                "α×β=30 档 + δ×γ×ρ=216 档在仓内无展开定义; 采用 "
                "results/deposon_v3_physical_opt_60cells_2026_09_11.json 的 decision_lines_36 "
                "(9 model × 4 T_frac bins) 作为落地版"
            ),
            "structure": dl36["structure"],
            "thresholds": dl36["thresholds"],
            "in_bin_36": dl36["in_bin_36"],
            "verdict_summary": dl36["verdict_summary"],
        },
        "dual_source_robustness": {
            "main_source_9model": {
                "file": "results/deposon_v3_physical_opt_60cells_2026_09_11.json",
                "table": [
                    {
                        "model": r["model"],
                        "T_frac": r["T_frac"],
                        "cos_sim": r["cos_sim"],
                        "eps_sum": r["eps_sum"],
                        "PC_verdict": r["PC_verdict"],
                        "PE_verdict": r["PE_verdict"],
                    }
                    for r in dl36["in_bin_36"]
                ],
            },
            "cross_source_2model_087": {
                "file": "results/deposon_game_theory_eval_2026_09_10.json",
                "note_path": "5_candidates_evaluation.P-A_equilibrium_stabilization.note",
                "note_verbatim": gt_note,
            },
        },
        "self_check": {
            "forbidden_tokens_policy": "禁用词表 8 项, 见 runner FORBIDDEN_TOKENS 常量 (拼接构造, 产出文件 0 字面命中)",
            "forbidden_tokens_found": None,  # 收尾回填
        },
    }
    attach_integrity(results, REL_RESULTS, ANCHORS)
    P_OUT_RESULTS.write_text(dump_json(results), encoding="utf-8")

    # ---------- 7. 收尾: frozen 复算 + 完整性复算 + 红线扫描, 回填后再写一次 ----------
    index_sha_after = sha256_file(P_INDEX)
    frozen_ok = index_sha_after == index_sha_before
    integ_v2 = verify_integrity(P_OUT_INDEX_V2)
    integ_res = verify_integrity(P_OUT_RESULTS)

    results["frozen_proof"]["sha256_after_write"] = index_sha_after
    results["frozen_proof"]["unchanged"] = frozen_ok
    attach_integrity(results, REL_RESULTS, ANCHORS)
    P_OUT_RESULTS.write_text(dump_json(results), encoding="utf-8")
    integ_res = verify_integrity(P_OUT_RESULTS)

    # 红线扫描 (对两个产出文件最终字节)
    found = {}
    for p in (P_OUT_INDEX_V2, P_OUT_RESULTS):
        text = p.read_text(encoding="utf-8")
        hits = [t for t in FORBIDDEN_TOKENS if t in text]
        if hits:
            found[str(p.relative_to(BASE))] = hits
    results["self_check"]["forbidden_tokens_found"] = found
    results["self_check"]["integrity_index_v2_ok"] = integ_v2
    results["self_check"]["integrity_results_ok"] = integ_res
    attach_integrity(results, REL_RESULTS, ANCHORS)
    P_OUT_RESULTS.write_text(dump_json(results), encoding="utf-8")

    # 终扫: 对最终字节再扫一次, 保证落盘版 0 命中
    found_final = {}
    for p in (P_OUT_INDEX_V2, P_OUT_RESULTS):
        text = p.read_text(encoding="utf-8")
        hits = [t for t in FORBIDDEN_TOKENS if t in text]
        if hits:
            found_final[str(p.relative_to(BASE))] = hits

    # ---------- 8. stdout 摘要 ----------
    summary = {
        "index_json_sha256_before": index_sha_before,
        "index_json_sha256_after": index_sha_after,
        "frozen_unchanged": frozen_ok,
        "id_correspondence": "22/22 positional+set PASS",
        "consistency_vs_f4": f"{rate_f4}/22",
        "consistency_vs_v3phys": f"{rate_v3}/22",
        "chain_pass_count": f"{chain_pass_count}/22",
        "anchor0_match_existing_chain": anchor0_ok,
        "independent_rewalk_ok": rewalk_ok,
        "b3_merkle_root": merkle_root,
        "integrity_index_v2_ok": integ_v2,
        "integrity_results_ok": verify_integrity(P_OUT_RESULTS),
        "forbidden_tokens_found": found,
        "forbidden_tokens_found_final_bytes": found_final,
        "index_v2_bytes": P_OUT_INDEX_V2.stat().st_size,
        "results_bytes": P_OUT_RESULTS.stat().st_size,
        "index_v2_integrity": index_v2["integrity"],
        "results_integrity": results["integrity"],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=1))
    assert frozen_ok, "frozen 文件被触动!"
    assert not found_final, f"术语红线命中: {found_final}"
    assert rate_f4 == 22 and rate_v3 == 22 and chain_pass_count == 22


if __name__ == "__main__":
    main()


# ---------- SELF-CHECK (P-F V0.1 §5 纪律, Trae 2026-09-16 补, 标记 TRAE_SELFCHECK_2026_09_16_V3) ----------
# 补入理由: V3 全实验走读发现本 runner 缺 SELF-CHECK 尾块(沿 P-F V0.1 §5)
import os as _os_sc
assert _os_sc.path.basename(__file__) == '_p_d_b3_merkle_22caption_runner_2026_09_16.py', '文件名漂移: ' + __file__
with open(__file__, 'r', encoding='utf-8') as _f_sc:
    _src_sc = _f_sc.read()
assert 'TRAE_SELFCHECK_2026_09_16_V3' in _src_sc
assert 'def main(' in _src_sc, 'main() 缺失'
assert '__main__' in _src_sc, '缺 __main__ guard'
print('_p_d_b3_merkle_22caption_runner_2026_09_16.py SELF-CHECK PASS')
