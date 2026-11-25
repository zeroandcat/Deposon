# -*- coding: utf-8 -*-
# ============================================================================
# 【EXP-06 · self_verified_only 硬写修正版副本】· 新名件 · 原件 0 触动 · 2026-10-10
# ----------------------------------------------------------------------------
# 授权锚：PI 2026-10-10 10:39「轮 34」卡（ask_2901c721b5788ebbb00670a5 step exp06_finds）
#         裁「授权 runner 修正」
# 勘误源：results/_exp06_supplement_four_gaps_2026_10_10.md · SHA-12 9f86cc5be8e9
#         §2.3.3（规格与实现之张力）＋ §3 勘误登记 E-EXP06-S3
# 规格源：results/_criterion_application_scope_prereg_2026_10_01.md · SHA-12 c4e3338619c6
#         §3.3②「全 true 字段须附独立验证件（可核、0 与被验证件同源）；⛔0 预置为 true」
# 原件  ：deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py
#         SHA-12 de16bc002198 · 20,322 B（本棒跑前＝跑后复测一致 ⇒ 0 回改）
# 本件  ：原件之全量副本；**唯一语义改动 ＝ 原 L232 之 self_verified_only 硬写**
# 同步件：results/_exp06_selfverified_runner_fix_note_2026_10_10.md
# ----------------------------------------------------------------------------
# 【缺陷实体】原件 L230-L232 之第二行: c["chain"]["self_verified_only"] = True
#            —— 无条件字面量, 0 依赖 rewalk_ok, 0 任何比较, 0 任何探测
#            ⇒ 该位之 true 值非由任何验证面求出 ⇒ 与 §3.3② 之「0 预置为 true」相悖
#            （读数不变: 22/22 仍为 true; 独立性在实现级未满足）
#
# 【修正形式 · 本棒选定并论证之形式】运行期实测求值 ＋ 计算来源显式标注 ＋ 独立验证面探测
#            ＋ 0 静默欠缺警报（四件套, 单一改动面）:
#   (1) 求值  : 值 ＝ bool(rewalk_ok) and not independent_verification_verified
#               —— 由自证复走之真实结果 ＋ 独立验证面之真实探测共同决定, ⛔0 预置
#   (2) 标注  : per_caption[].chain.self_verified_only_basis ＋ 顶层 independence_verification 节
#               —— 载 §3.3① 三要素（置位者/置位时机/依据件）＋ 计算式 ＋ 取值（§3.3① 之落面要求）
#   (3) 探测  : probe_independent_evidence() 于运行期实测独立验证面
#               （在位/哈希相符/异源 ⇒ 方计 verified; 「0 与被验证件同源」之异源判据）
#   (4) 警报  : independence_deficiency_alarm（burden 未满足即亮起, ⛔0 静默）
#               —— 沿 §3.3④「0 记为通过、0 静默」之同族纪律
#
# 【⛔ 未代裁项 · 归 PI】原件该键名 self_verified_only 之语义本身与 §3.3② 之
#   「全 true 须附独立验证件」存在结构性张力（若验证确为「仅自证」, 则按定义无独立
#   验证件可附）。本棒 0 代裁「改键名 / 拆位 / 改语义」, 只把「可求值化 ＋ 可核化 ＋
#   不静默」三项落成; 是否进一步改键名 须 PI 另裁。
#
# 【身份改写 · 与语义改动严格分离登记】详见同步注记件 §3
#   DATE / GENERATOR / task_id / 两组输出路径常量(P_OUT_INDEX_V3,P_OUT_RESULTS,
#   REL_INDEX_V3,REL_RESULTS) / docstring 件名与 out件名 —— 共 9 行, 0 语义影响
#   （必要性: 输出路径若不改写, 本副本一跑即覆写原件产出 33ad1c01f745 ⇒ 违反 0 回改）
#   落位同目录（deposon_team/plugins/）之因: 原件 L40 BASE = Path(__file__).resolve().parents[2]
#   同深度落位 ⇒ BASE 解析 0 改动; 若改落 results/ 则 parents[2] 指向仓外, 须连带改写 BASE
#
# 【本棒纪律】⛔0 回改原件 1 byte ｜ ⛔0 重跑任何实验载荷（本件 0 运行, 未生成任何产出）
#            ｜ ⛔0 网络 ｜ ⛔0 skill ｜ ⛔0 LLM ｜ 0 读 key ｜ ⛔0 改任何既有产出件
#   验证止于 parse / AST 级 ＋ 静态 grep（0 硬写残留）＋ 离线代数核验
# 标记 EXP06_SELFVERIFY_FIXCOPY_2026_10_10（与原件 0 并存标记）
# ============================================================================
"""
P-D B3 Merkle 22 caption dual chain re-walk runner -- V0.4 coordinate space
CORRECTED COPY (self_verified_only 去 hard-write; 0 touch on the original of 2026-09-29)

V3X-C5B-RUNNER-2026-10-10-A1-FIXCOPY
out件 (new names, 0 overwrite the 2026-09-16 / 2026-09-29 assets):
  1. corpus/v20/index_v3_selfverify_fix_2026_10_10.json
  2. results/deposon_p_d_b3_merkle_22_caption_selfverify_fix_2026_10_10.json

Basis: 提案件 _v5_v3_deg_c5_proposal_2026_09_29.md §4.2 步 6-7 + §5 (N-3 连带),
       PI 确认批 5 裁: B 组 (SVD 2->3) + 码长随投影维数同步 + N-3 连带新写新名 runner.

Parameter derivation (all values verified offline by .tmp/_v5_c5_b_clause4_consistency_check.py):
  hyperplanes per dim = 12 / 2 = 6        (on-disk literal, V0.2 spec L38 randn(12, 2))
  n_components k      = 3                 (B 组)
  n_plane  = 6 * 3    = 18
  code len  = 18 bit
  zfill(3) -> zfill(5)                     (18 bit = 5 hex, leading digit holds 2 bits; lossless)
  d/2 reference = 9.0                     (K-V3DF-5-2 随维度派生值; 0 新设阈值)
  dual = byte_hash[:6] + semantic_hash = 11 hex (42 bit)

Hard discipline:
  - 0 overwrite: does NOT write corpus/v20/index.json, corpus/v20/index_v2_2026_09_16.json,
    results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json, nor the 2026-09-16 runner.
    The 2 existing B3 outputs are SHA-256 pinned and re-verified after write.
  - 0 network / 0 LLM / 0 API call inside this runner. Raw 22x2048 vectors are an INPUT
    (produced by the fetch step). If the input is absent the runner exits 2 and writes nothing.
  - 0 filename SELF-CHECK assert (the 2026-09-16 runner L411 pins its own filename; a new-named
    runner must not inherit that block -- 提案件 §5.2-⑩).
  - 0 judgement / 0 verdict tier. No PASS/FAIL on the new caliber.
  - 0 key of any kind: this runner never reads a key.
"""
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parents[2]

K_COMPONENTS = 3                 # B 组: SVD 主成分数 2 -> 3
PLANES_PER_DIM = 6               # 盘上字面 12/2
N_PLANE = PLANES_PER_DIM * K_COMPONENTS   # 18
CODE_LEN_BIT = N_PLANE                    # 18
HEX_WIDTH = CODE_LEN_BIT // 4 + (1 if CODE_LEN_BIT % 4 else 0)   # 5
D_OVER_2 = CODE_LEN_BIT / 2.0              # 9.0
LSH_SEED = 42
DATE = "2026-10-10"              # 身份改写: 修正版副本落盘日 (原件 2026-09-29)

# ---- inputs (read-only) ----
P_INDEX = BASE / "corpus" / "v20" / "index.json"                    # frozen
P_CAPTIONS = BASE / "corpus" / "v20" / "strip_captions_22.json"
P_RAW = BASE / "results" / "_v5_v3_deg_c5_b_raw_embeddings_2026_09_29.json"   # B 组原料
P_F4 = BASE / "results" / "deposon_v2_phase4_f4_2026_09_11.json"
P_V3 = BASE / "results" / "deposon_v3_physical_opt_2026_09_11.json"
P_60 = BASE / "results" / "deposon_v3_physical_opt_60cells_2026_09_11.json"
P_GT = BASE / "results" / "deposon_game_theory_eval_2026_09_10.json"
P_CHAIN0 = BASE / "verifier" / "runs" / "2026-09-04_pd_v0.jsonl"

# ---- outputs (NEW names; 身份改写: 0 覆写原件两产出) ----
P_OUT_INDEX_V3 = BASE / "corpus" / "v20" / "index_v3_selfverify_fix_2026_10_10.json"
P_OUT_RESULTS = BASE / "results" / "deposon_p_d_b3_merkle_22_caption_selfverify_fix_2026_10_10.json"
REL_INDEX_V3 = "corpus/v20/index_v3_selfverify_fix_2026_10_10.json"
REL_RESULTS = "results/deposon_p_d_b3_merkle_22_caption_selfverify_fix_2026_10_10.json"

# ---- 0-overwrite pins (the two 2026-09-16 B3 outputs) ----
PINNED = {
    "corpus/v20/index_v2_2026_09_16.json": "efe05ad775de",
    "results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json": "b5873afb9d29",
    "corpus/v20_caption_surface/_p_d_b3_merkle_22caption_runner_2026_09_16.py": "d2cd7acb29a1",
    # 身份改写追加 pin 面 (副本 0 覆写既有产出件 3 件 + 原件 2 件; 沿 10-09 runner L82-L86 同款纪律)
    "results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json": "33ad1c01f745",
    "corpus/v20/index_v3_2026_09_29.json": "3ba2449cf986",
    "deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py": "de16bc002198",
}

ANCHORS = ["7d6d3d39fad8", "f88d855aaf83", "e66e44e63f5a"]
SPEC_REF_BASE = "docs/V3X/PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md"
SPEC_REF_V04 = "docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md (待 doc-writer 棒 2b 新增, 本件 0 代拟正文)"
ANCHORS_REF = "docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md §2.3 B3 Merkle"
GENERATOR = "deposon_team/plugins/_p_d_b3_merkle_22caption_runner_selfverify_fix_2026_10_10.py"

# 术语红线 (拼接构造, 使本 runner 自身亦不含字面禁用串; 继承 2026-09-16 runner §⑪)
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


def pinned_snapshot() -> dict:
    return {rel: sha256_file(BASE / rel)[:12] for rel in PINNED}


# ---- 独立验证面声明位 (c4e3338619c6 §3.3②「全 true 须附独立验证件」之落面入口) ----
# 本副本 0 声明独立验证件: ⛔0 以本 runner 之自身产出充当「独立验证件」
# (§3.3② 明定「0 与被验证件同源」⇒ 同源产出无效) ⇒ 0 声明 ⇒ status="not_declared"。
# 声明形如: {"path": "results/<独立验证件>.json", "sha256": "<64 hex>"}; 声明后须重跑本 runner 方见效果。
INDEP_VERIFY_DECL = None


def probe_independent_evidence(base: Path, self_generator: str) -> dict:
    """§3.3② 独立验证面之运行期实测 (纯只读文件系统探测; 0 网络 / 0 写 / 0 LLM / 0 读 key)。

    status ∈ {not_declared, absent, unpinned_hash, sha256_mismatch, same_source, verified}
    仅 "verified" (在位 + 哈希相符 + 异源) 之状态计入 independence_burden_satisfied。
    """
    probe = {
        "declared": INDEP_VERIFY_DECL,
        "path": None,
        "sha256_expected": None,
        "sha256_actual": None,
        "sha256_match": None,
        "artifact_generator": None,
        "same_source": None,
        "exists": None,
        "status": "not_declared",
        "probe_method": "Path.exists() + hashlib.sha256(file bytes) + artifact['generator'] 字段读取",
        "same_source_criterion": "artifact['generator'] == 本 runner 之 GENERATOR ⇒ 同源 ⇒ 无效",
        "spec_ref": "results/_criterion_application_scope_prereg_2026_10_01.md §3.3②",
    }
    if not INDEP_VERIFY_DECL:
        return probe
    rel = INDEP_VERIFY_DECL.get("path")
    p = base / rel
    probe["path"] = rel
    probe["sha256_expected"] = INDEP_VERIFY_DECL.get("sha256")
    if not p.exists():
        probe["status"] = "absent"
        return probe
    probe["exists"] = True
    actual = sha256_file(p)
    probe["sha256_actual"] = actual
    if probe["sha256_expected"] is None:
        probe["status"] = "unpinned_hash"
        return probe
    probe["sha256_match"] = actual == probe["sha256_expected"]
    if not probe["sha256_match"]:
        probe["status"] = "sha256_mismatch"
        return probe
    try:
        gen = load_json(p).get("generator")
    except (OSError, ValueError):
        gen = None
    probe["artifact_generator"] = gen
    probe["same_source"] = gen == self_generator
    probe["status"] = "same_source" if probe["same_source"] else "verified"
    return probe


def main() -> int:
    # ---------- 0. 前置: B 组原料是否就位 ----------
    if not P_RAW.exists():
        print(f"[BLOCKED] B 组原料缺失: {P_RAW.relative_to(BASE)} 不存在.")
        print("[BLOCKED] B 组 = 换坐标空间, 盘上无 raw 2048-d 向量缓存 => 须先完成 embedding API 重取.")
        print("[BLOCKED] 本 runner 0 网络 0 API; 缺料即退出, 0 写任何产出, 0 触动任何既有件.")
        return 2

    pin_before = pinned_snapshot()
    mism = [r for r, h in PINNED.items() if pin_before[r] != h]
    assert not mism, f"0-overwrite pin 已漂移, 中止: {mism}"

    index_sha_before = sha256_file(P_INDEX)
    index = load_json(P_INDEX)
    caps = load_json(P_CAPTIONS)
    raw = load_json(P_RAW)
    f4 = load_json(P_F4)
    v3 = load_json(P_V3)
    d60 = load_json(P_60)
    gt = load_json(P_GT)
    chain0_line = P_CHAIN0.read_text(encoding="utf-8").strip().splitlines()[0]
    chain0 = json.loads(chain0_line)

    # ---------- 1. 原料自证 + SVD-k ----------
    ids_raw = raw["concept_ids"]
    E = np.array([raw["raw_embeddings"][c] for c in ids_raw], dtype=np.float64)
    assert E.shape == (22, 2048), f"raw 原料形状异常: {E.shape}"
    rep = raw.get("reproduction_selfcheck", {})
    E_n = E / (np.linalg.norm(E, axis=1, keepdims=True) + 1e-12)
    U, S, Vt = np.linalg.svd(E_n, full_matrices=False)
    coords = U[:, :K_COMPONENTS] * S[:K_COMPONENTS]          # 沿用原始件 U[:,:k]*S[:k] 口径
    coords_map = {ids_raw[i]: [float(coords[i, j]) for j in range(K_COMPONENTS)]
                  for i in range(22)}
    var_k = float((S[:K_COMPONENTS] ** 2).sum() / (S ** 2).sum())

    # ---------- 2. id 一一对应 ----------
    graph_ids = [g["graph_id"] for g in index["graphs"]]
    caption_ids = [c["id"] for c in caps]
    assert len(graph_ids) == 22 and len(caption_ids) == 22
    assert graph_ids == caption_ids, "graph_id 与 caption id 非一一对应"
    assert sorted(ids_raw) == sorted(caption_ids), "原料 concept_ids 与 caption ids 不一致"
    assert index.get("captions") is None, "index.json 已含 captions 字段, 异常"

    # ---------- 3. 复算 dual ----------
    np.random.seed(LSH_SEED)
    hyperplanes = np.random.randn(N_PLANE, K_COMPONENTS)
    f4_dual = f4["dual_fingerprints"]
    v3_per = {c["caption_id"]: c for c in v3["P_D_semantic_fingerprint_V0_2"]["per_caption"]}

    per_caption = []
    for cid in caption_ids:
        byte_hash = sha256_str(cid)[:12]
        proj = np.array(coords_map[cid]) @ hyperplanes.T
        bits = (proj > 0).astype(int)
        semantic_hash = hex(int("".join(str(b) for b in bits), 2))[2:].zfill(HEX_WIDTH)
        dual = byte_hash[:6] + semantic_hash
        per_caption.append({
            "caption_id": cid,
            "byte_hash": byte_hash,
            "semantic_hash": semantic_hash,
            "dual": dual,
            "dual_hex_width": len(dual),
            "coords_k": [round(v, 6) for v in coords_map[cid]],
            # 差异登记: 新口径下与 2026-09-16 件必然不一致, 仅登记, 0 作通过依据
            # (提案件 §5.3 连带后果②; 0 自裁, 留 PI 确认)
            "diff_registration_vs_f4": {
                "semantic_hash_identical": semantic_hash == f4_dual[cid]["semantic_hash"],
                "dual_identical": dual == f4_dual[cid]["dual_24bit"],
            },
            "diff_registration_vs_v3phys": {
                "semantic_hash_identical": semantic_hash == v3_per[cid]["semantic_hash"],
                "dual_identical": dual == v3_per[cid]["dual_24bit"],
            },
        })

    # ---------- 4. 链式连接 ----------
    anchor0_ok = chain0["current_root"] == ANCHORS[0] and chain0["prev_hash"] == "000000000000"
    state = ANCHORS[0]
    for c in per_caption:
        link_input = f"{state}|{c['caption_id']}|{c['dual']}"
        node = sha256_str(link_input)[:12]
        c["chain"] = {"parent_state": state, "link_input": link_input, "node_state": node}
        state = node
    state_22 = state
    ext1 = sha256_str(f"{state_22}|anchor|{ANCHORS[1]}")[:12]
    merkle_root = sha256_str(f"{ext1}|anchor|{ANCHORS[2]}")[:12]

    # ---------- 5. 独立复走自证 (步 7) ----------
    rw = ANCHORS[0]
    rewalk_ok = True
    for c in per_caption:
        rw = sha256_str(f"{rw}|{c['caption_id']}|{c['dual']}")[:12]
        if rw != c["chain"]["node_state"]:
            rewalk_ok = False
    rw_ext1 = sha256_str(f"{rw}|anchor|{ANCHORS[1]}")[:12]
    rw_root = sha256_str(f"{rw_ext1}|anchor|{ANCHORS[2]}")[:12]
    rewalk_ok = rewalk_ok and rw_ext1 == ext1 and rw_root == merkle_root
    # ---------- 5b. 独立验证面实测 (步 7 之后, 任何 chain 布尔位置位之前) ----------
    # §3.3① 三要素之声明 (逐字段): 置位者 = 本 runner (本段) ｜ 置位时机 = 22 节点建毕
    # 且自证复走毕之后 ｜ 依据件 = INDEP_VERIFY_DECL 所声明之独立验证件 + 本段探测记录。
    indep = probe_independent_evidence(BASE, GENERATOR)
    indep_verified = indep["status"] == "verified"

    for c in per_caption:
        c["chain"]["link_verified"] = rewalk_ok
        # ⛔0 预置: 该位之值由本段实测结果求值, 非无条件字面量 (§3.3②)
        c["chain"]["self_verified_only"] = bool(rewalk_ok) and not indep_verified
        # 取值语义之随件声明 (§3.3①): 值之来源与判定条件逐行可核
        c["chain"]["self_verified_only_basis"] = {
            "declared_by": "deposon_team/plugins/_p_d_b3_merkle_22caption_runner_selfverify_fix_2026_10_10.py (本副本 5b 段)",
            "declared_at": "22 节点建毕且自证复走毕之后, 任何 chain 布尔位置位之前",
            "source_evidence": "INDEP_VERIFY_DECL 所声明之独立验证件 + 5b 段运行期探测记录",
            "value_rule": "self_verified_only = (rewalk_ok 为真) 且 (独立验证面未取得 verified 状态)",
            "rewalk_ok": bool(rewalk_ok),
            "independent_verification_status": indep["status"],
            "independent_verification_verified": bool(indep_verified),
            "preset": False,
            "prescription_ref": "c4e3338619c6 §3.3① 三要素 ＋ §3.3②「0 预置为 true」",
        }
        # 独立验证件之可核指针 (§3.3② 之「附独立验证件」; 未获验证时显式记 none, 0 静默)
        c["chain"]["independent_verification_ref"] = (
            indep["path"] if indep_verified else None
        )
        c["chain"]["independent_verification_status"] = indep["status"]
        # ⛔0 记为通过、0 静默: 独立验证面未获 verified 者, 警报位显式亮起 (§3.3④ 同族纪律)
        c["chain"]["independence_deficiency_alarm"] = not indep_verified

    # ---------- 6. 产出 1: index_v3 (新名) ----------
    cap_text = {c["id"]: c for c in caps}
    index_v3 = dict(index)
    index_v3["graphs"] = index["graphs"]
    index_v3["captions"] = [
        {
            "caption_id": c["caption_id"],
            "text": cap_text[c["caption_id"]]["text"],
            "family": cap_text[c["caption_id"]]["family"],
            "structure": cap_text[c["caption_id"]]["structure"],
            "n_labels": cap_text[c["caption_id"]]["n_labels"],
            "byte_hash": c["byte_hash"],
            "semantic_hash": c["semantic_hash"],
            "dual_v04": c["dual"],
        }
        for c in per_caption
    ]
    index_v3["n_captions"] = 22
    index_v3["fingerprint_anchors"] = list(ANCHORS)
    index_v3["index_v3_meta"] = {
        "generator": GENERATOR,
        "date": DATE,
        "caliber": "V0.4 coordinate space (B 组)",
        "spec_ref_pending": SPEC_REF_V04,
        "spec_ref_base": SPEC_REF_BASE,
        "dual_rule": f"byte_hash[:6] + semantic_hash = {6 + HEX_WIDTH} hex ({24 + CODE_LEN_BIT} bit)",
        "anchors_ref": ANCHORS_REF,
        "base_index": "corpus/v20/index.json",
        "base_index_sha256": index_sha_before,
        "caption_source": "corpus/v20/strip_captions_22.json",
        "caption_source_sha256": sha256_file(P_CAPTIONS),
        "raw_embedding_source": str(P_RAW.relative_to(BASE)),
        "raw_embedding_source_sha256": sha256_file(P_RAW),
        "lsh_seed": LSH_SEED,
        "n_components": K_COMPONENTS,
        "planes_per_dim": PLANES_PER_DIM,
        "hyperplanes_shape": [N_PLANE, K_COMPONENTS],
        "code_len_bit": CODE_LEN_BIT,
        "hex_width": HEX_WIDTH,
        "d_over_2_reference": D_OVER_2,
        "svd_var_explained_k": round(var_k, 6),
    }
    attach_integrity(index_v3, REL_INDEX_V3, ANCHORS)
    P_OUT_INDEX_V3.write_text(dump_json(index_v3), encoding="utf-8")

    # ---------- 7. 产出 2: 链式核验结果 (新名) ----------
    gt_note = gt["5_candidates_evaluation"]["P-A_equilibrium_stabilization"]["note"]
    results = {
        "task": "P-D B3 Merkle 22 caption chain re-walk -- V0.4 coordinate space",
        "task_id": "V3X-C5B-RUNNER-2026-10-10-A1-FIXCOPY",   # 身份改写
        "date": DATE,
        "generator": GENERATOR,
        "method": "0 LLM, 0 network, 0 API call inside this runner; pure hashlib + numpy + json",
        "caliber": {
            "n_components": K_COMPONENTS,
            "planes_per_dim": PLANES_PER_DIM,
            "hyperplanes_shape": [N_PLANE, K_COMPONENTS],
            "code_len_bit": CODE_LEN_BIT,
            "hex_width": HEX_WIDTH,
            "d_over_2_reference": D_OVER_2,
            "d_over_2_note": "K-V3DF-5-2 随维度派生的理论参照值, 0 新设判定阈值",
            "semantic_hash": f"{CODE_LEN_BIT}-bit LSH on SVD-{K_COMPONENTS} coords x {N_PLANE} hyperplanes (np.random.seed({LSH_SEED})), sign bits -> {HEX_WIDTH} hex",
            "byte_hash": "SHA-256(caption_id)[0:12] (12 hex)",
            "dual": f"byte_hash[:6] + semantic_hash = {6 + HEX_WIDTH} hex ({24 + CODE_LEN_BIT} bit)",
            "spec_ref_pending": SPEC_REF_V04,
        },
        "input_selfcheck": {
            "raw_embedding_reproduction_max_abs_dev_vs_stored_svd2": rep.get("max_abs_dev_vs_stored_svd2"),
            "raw_embedding_reproduces_stored_svd2": rep.get("reproduce_within_4dp"),
            "svd_var_explained_k": round(var_k, 6),
        },
        "id_correspondence": {
            "n_graph_ids": len(graph_ids),
            "n_caption_ids": len(caption_ids),
            "positional_match": graph_ids == caption_ids,
            "raw_concept_ids_match": sorted(ids_raw) == sorted(caption_ids),
        },
        "frozen_proof": {
            "file": "corpus/v20/index.json",
            "sha256_before_write": index_sha_before,
            "sha256_after_write": None,
            "unchanged": None,
        },
        "zero_overwrite_proof": {
            "policy": "0 覆写 2026-09-16 两件 B3 既有产出 + 既有 runner",
            "sha12_before": pin_before,
            "sha12_after": None,
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
            "root_note": (
                "新口径下 root 由逐节 SHA-256 导出, 必异于 2026-09-16 件的 root; "
                "V0.3 spec L265「root 必须保持」与改坐标空间在数学上互斥, "
                "PI 确认批 5 裁「由新增 V0.4 专用 spec 承载」; 本件 0 代拟该 spec 正文, 0 判档位"
            ),
        },
        "chain_convention": {
            "state_0": "anchors[0]",
            "link_i": "SHA-256(f\"{state_(i-1)}|{caption_id}|{dual}\")[0:12], i=1..22",
            "ext_1": "SHA-256(f\"{state_22}|anchor|{anchors[1]}\")[0:12]",
            "merkle_root": "SHA-256(f\"{ext_1}|anchor|{anchors[2]}\")[0:12]",
        },
        "per_caption": per_caption,
        "diff_registration": {
            "note": (
                "新口径下与 2026-09-16 件的逐条比对必不一致; 本面仅作差异登记, "
                "0 作通过依据 (提案件 §5.3 连带后果②; 0 自裁, 留 PI 确认是否改判为新件自证)"
            ),
            "vs_f4_semantic_identical_count": sum(
                1 for c in per_caption if c["diff_registration_vs_f4"]["semantic_hash_identical"]),
            "vs_f4_dual_identical_count": sum(
                1 for c in per_caption if c["diff_registration_vs_f4"]["dual_identical"]),
            "vs_v3phys_semantic_identical_count": sum(
                1 for c in per_caption if c["diff_registration_vs_v3phys"]["semantic_hash_identical"]),
            "vs_v3phys_dual_identical_count": sum(
                1 for c in per_caption if c["diff_registration_vs_v3phys"]["dual_identical"]),
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
        },
        "independence_verification": {
            "note": (
                "self_verified_only 之独立验证面全局面 (置位者/时机/依据件/探测记录 逐项可核); "
                "0 判档, 0 翻转既往读数"
            ),
            "field": "per_caption[].chain.self_verified_only",
            "declared_by": GENERATOR,
            "declared_at": "22 节点建毕且自证复走毕之后, 任何 chain 布尔位置位之前",
            "source_evidence": "INDEP_VERIFY_DECL 所声明之独立验证件 + 5b 段运行期探测记录",
            "value_rule": "self_verified_only = (rewalk_ok 为真) 且 (独立验证面未取得 verified 状态)",
            "self_verified_only_value": bool(rewalk_ok) and not indep_verified,
            "preset": False,
            "independent_verification_declared": indep["declared"],
            "independent_verification_probe": indep,
            "independence_burden_satisfied": indep_verified,
            "independence_deficiency_alarm": not indep_verified,
            "deficiency_note": (
                "若 burden 未满足 (独立验证面未取得 verified), 则该位读 true 而独立验证件并未在位; "
                "此时 ⛔0 静默 —— independence_deficiency_alarm 置 true 之同时 "
                "independent_verification_status 记 none 态之实况"
            ),
            "prescription_ref": "c4e3338619c6 §3.3① 三要素 ＋ §3.3②「0 预置为 true」",
        },
        "decision_lines_36_substitute": {
            "substitution_note": (
                "α×β=30 档 + δ×γ×ρ=216 档在仓内无展开定义; 沿用 "
                "results/deposon_v3_physical_opt_60cells_2026_09_11.json 的 decision_lines_36"
            ),
            "structure": d60["decision_lines_36"]["structure"],
            "thresholds": d60["decision_lines_36"]["thresholds"],
            "verdict_summary": d60["decision_lines_36"]["verdict_summary"],
        },
        "cross_source_2model_087": {
            "file": "results/deposon_game_theory_eval_2026_09_10.json",
            "note_path": "5_candidates_evaluation.P-A_equilibrium_stabilization.note",
            "note_verbatim": gt_note,
        },
        "self_check": {
            "forbidden_tokens_policy": "禁用词表 8 项, 见本 runner FORBIDDEN_TOKENS 常量 (拼接构造)",
            "forbidden_tokens_found": None,
            "integrity_index_v3_ok": None,
            "integrity_results_ok": None,
        },
        "no_verdict_notice": "本件 0 判档位; PASS/FAIL/KD 归 verdict-keeper",
        "runner_fix_notice": (
            "本产出由修正版副本 _p_d_b3_merkle_22caption_runner_selfverify_fix_2026_10_10.py 生成; "
            "原件 _p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py 之 L232 self_verified_only 硬写 "
            "已在本副本改为运行期实测求值 (c4e3338619c6 §3.3②「0 预置为 true」); "
            "⛔0 回改原件 1 byte; 既往产出 33ad1c01f745 之读数 0 变动"
        ),
    }
    attach_integrity(results, REL_RESULTS, ANCHORS)
    P_OUT_RESULTS.write_text(dump_json(results), encoding="utf-8")

    # ---------- 8. 收尾: frozen / pin 复算 + 完整性 + 红线 ----------
    index_sha_after = sha256_file(P_INDEX)
    frozen_ok = index_sha_after == index_sha_before
    pin_after = pinned_snapshot()
    pin_ok = pin_after == pin_before
    integ_v3 = verify_integrity(P_OUT_INDEX_V3)

    results["frozen_proof"]["sha256_after_write"] = index_sha_after
    results["frozen_proof"]["unchanged"] = frozen_ok
    results["zero_overwrite_proof"]["sha12_after"] = pin_after
    results["zero_overwrite_proof"]["unchanged"] = pin_ok
    attach_integrity(results, REL_RESULTS, ANCHORS)
    P_OUT_RESULTS.write_text(dump_json(results), encoding="utf-8")

    found = {}
    for p in (P_OUT_INDEX_V3, P_OUT_RESULTS):
        text = p.read_text(encoding="utf-8")
        hits = [t for t in FORBIDDEN_TOKENS if t in text]
        if hits:
            found[str(p.relative_to(BASE))] = hits
    results["self_check"]["forbidden_tokens_found"] = found
    results["self_check"]["integrity_index_v3_ok"] = integ_v3
    results["self_check"]["integrity_results_ok"] = verify_integrity(P_OUT_RESULTS)
    attach_integrity(results, REL_RESULTS, ANCHORS)
    P_OUT_RESULTS.write_text(dump_json(results), encoding="utf-8")

    found_final = {}
    for p in (P_OUT_INDEX_V3, P_OUT_RESULTS):
        text = p.read_text(encoding="utf-8")
        hits = [t for t in FORBIDDEN_TOKENS if t in text]
        if hits:
            found_final[str(p.relative_to(BASE))] = hits

    print(json.dumps({
        "frozen_unchanged": frozen_ok,
        "zero_overwrite_unchanged": pin_ok,
        "pin_sha12_after": pin_after,
        "independent_rewalk_ok": rewalk_ok,
        "b3_merkle_root": merkle_root,
        "n_components": K_COMPONENTS,
        "hyperplanes_shape": [N_PLANE, K_COMPONENTS],
        "code_len_bit": CODE_LEN_BIT,
        "hex_width": HEX_WIDTH,
        "d_over_2_reference": D_OVER_2,
        "integrity_index_v3_ok": integ_v3,
        "integrity_results_ok": verify_integrity(P_OUT_RESULTS),
        "forbidden_tokens_found_final_bytes": found_final,
        "index_v3_bytes": P_OUT_INDEX_V3.stat().st_size,
        "results_bytes": P_OUT_RESULTS.stat().st_size,
    }, ensure_ascii=False, indent=1))

    assert frozen_ok, "frozen 文件被触动!"
    assert pin_ok, "0-overwrite pin 漂移!"
    assert rewalk_ok, "独立复走失败!"
    assert not found_final, f"术语红线命中: {found_final}"
    return 0


if __name__ == "__main__":
    sys.exit(main())
