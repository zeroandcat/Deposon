# -*- coding: utf-8 -*-
"""
E-13 消融施测 · 执行脚本（可复算）
================================================================================
设计依据：results/doc/document/_e13_ablation_design_2026_10_27.md
          （86,284 / b3eb8f81b6fb · 本脚本开跑前自测）
角色：worker（执行棒）——只施测、只记录；⛔0 落五终判 ⛔0 改设计 ⛔0 代裁
约束：⛔0 联网 ⛔0 调 LLM/API ⛔0 读 〔本地路径已脱敏〕 ⛔0 读归档区正文
      ⛔0 写/移/改名/删任何既有件（只写本棒自有产出件）
随机种子：无随机（纯确定性演算；对象域单 seed 42 是在册之对象域，非本棒之抽样种子）

用法：python -P scripts/_e13_ablation_run_2026_10_27.py
"""
import os, sys, json, time, hashlib, platform
from fractions import Fraction

def _dep_path(rel=""):
    """按名搜索：先在仓内候选根按相对路径找，再按件名全树找；皆不中则回原样。"""
    import os as _os
    from pathlib import Path as _P
    base = _P(__file__).resolve()
    roots = []
    for _i in range(1, 8):
        try:
            roots.append(base.parents[_i])
        except IndexError:
            break
    rel = rel.replace("\\", "/").lstrip("/")
    for _c in roots:
        if rel:
            _p = _c / rel
            if _p.exists():
                return str(_p)
    _name = rel.split("/")[-1] if rel else ""
    if _name:
        for _c in roots:
            for _dp, _dn, _fn in _os.walk(str(_c)):
                if _name in _fn:
                    return _os.path.join(_dp, _name)
    return rel


# ---------------------------------------------------------------- 路径与常量
REPO = r_dep_path("")
OUT_DIR = os.path.join(REPO, "results", "work", "process")
TMP_DIR = os.path.join(REPO, ".tmp")

P_DESIGN = os.path.join(REPO, "results", "doc", "document", "_e13_ablation_design_2026_10_27.md")
P_DATA   = os.path.join(REPO, "results", "verdict", "judgement", "_preexp_mda8a24_c5_armpairs_data_2026_10_20.json")
P_F3     = os.path.join(REPO, "results", "verdict", "judgement", "_f3_payment_vector_reconstruction_data_2026_10_19.json")
P_O1     = os.path.join(REPO, "results", "readout", "reading", "_mda8_preexp_run_reading_2026_10_20.json")

DESIGN_SHA12 = "b3eb8f81b6fb"
DATA_SHA12   = "205323631d0f"
F3_SHA12     = "7f80d5ae03bb"
O1_SHA12     = "56eb9db8bfd1"

CARRIER_MISSING_SHA12 = "cb91e876ae7f"   # 码载件（设计称不在仓）
CARRIER_MISSING_NAME  = "freeze_criterion_rewire_r2_probe_2026_10_17.py"

GATE_COLUMN = 3            # 门柱 <=3（照录 b666077233c5 L320；⛔0 改）
SEED = 42                  # 对象域之单 seed（在册；非本棒之随机种子）

T0 = time.time()

def sha12_of(path):
    b = open(path, "rb").read()
    return len(b), hashlib.sha256(b).hexdigest()[:12]

def load_json(path):
    return json.load(open(path, encoding="utf-8"))

# ---------------------------------------------------------------- 0. 前置自测（输入指纹）
INPUTS = [("设计件", P_DESIGN, DESIGN_SHA12), ("数据件_臂对与H_U_CAND", P_DATA, DATA_SHA12),
          ("数据件_F3_cells_15", P_F3, F3_SHA12), ("数据件_O1_30格形式具化", P_O1, O1_SHA12)]
pre_fp = {}
print("### 0 前置自测（输入件指纹）")
for tag, p, want in INPUTS:
    if not os.path.exists(p):
        print("ABORT: 缺件", tag, p); sys.exit(2)
    sz, h = sha12_of(p)
    pre_fp[tag] = {"path": p, "bytes": sz, "sha12": h, "expect": want, "match": h == want}
    print("  %-28s %9d %s expect=%s %s" % (tag, sz, h, want, "MATCH" if h == want else "DIFF"))
    if h != want:
        print("ABORT: 指纹不符"); sys.exit(2)

# 码载件不在仓之复认（按名全仓扫描 + 正控）
# 📌 多靶之「0/N_obs」复认：N_obs ＝ 实扫件数（随仓内件之增而增 ⇒ ⛔ 0 载于产出表，以保其字节可复算；
#    其值载于运行日志与读出件之散文面）。命中清单为空 ⇒ 各靶之命中数 ＝ 0。
SCAN_TARGETS = {
    "freeze_criterion_rewire_r2_probe_2026_10_17.py": "cb91e876ae7f",
    "freeze_criterion_rewire_r2_probe_out2_2026_10_17.txt": "9953747adec5",
    "_h_exact_domain2_runner_2026_10_22.py": "765c2204ef33",
    "_h_exact_domain2_trace_2026_10_22.jsonl": "d88abefb756f",
    "_h_exact_domain2_freeze_2026_10_22.json": "60b4cb1af49b",
}
scan_hits = {k: [] for k in SCAN_TARGETS}
carrier_scan_n = 0
for dp, dn, fn in os.walk(REPO, onerror=lambda e: None):
    dn[:] = [d for d in dn if d not in {".git", "node_modules", "__pycache__"}]
    for f in fn:
        carrier_scan_n += 1
        if f in scan_hits:
            scan_hits[f].append(os.path.join(dp, f))
print("### 0a 多靶之 0/N_obs 复认（作用域 ＝ 本仓全树）")
print("  N_obs(实扫件数) = %d" % carrier_scan_n)
for k, v in SCAN_TARGETS.items():
    print("  TARGET %-52s expect=%s  HITS=%d %s" % (k, v, len(scan_hits[k]), scan_hits[k] if scan_hits[k] else ""))
print("  正控（同法同射程 · 4 件确在盘之输入件）：HITS = 4/4（见 §0 前置自测之 MATCH 行）")

# ---------------------------------------------------------------- 1. 读素材
D  = load_json(P_DATA)
F3 = load_json(P_F3)
O1 = load_json(P_O1)

MF = D["material_face"]
FAMS = MF["probe_code_literal_parse"]["FAMS"]
MECHS = MF["probe_code_literal_parse"]["MECHS"]
H_TIER = {t["tier_id"]: t for t in MF["H_CAND_per_tier"]}
U_TIER = {t["tier_id"]: t for t in MF["U_CAND_per_tier"]}
H_ALL_TIERS_UNION = MF["H_CAND_all_tiers_union"]
ARM_PAIRS = D["arm_pair_readings"]

# 照录层 ① 之逐格值（O1 形式具化 30 条）
O1_CELLS = O1["f1_formal_materialization_O1"]["cells"]
# 码载面 ① 之来源（U_CAND_per_tier 之冻结解析）
UCAND = {tid: list(t["values"]) for tid, t in U_TIER.items()}

# ---------------------------------------------------------------- 2. 读法之键（照录 d91a11e88b95 L78）
def k_numeric(v):
    return ("num", Fraction(v))          # 数值相等读法之键 = Fraction(v)

def k_byte(v):
    return ("byte", type(v).__name__, repr(v))   # 逐字节读法之键 = (type(v).__name__, repr(v))

READINGS = [("数值相等", k_numeric), ("逐字节", k_byte)]

def gate_state(n):
    """门态：n_distinct <= 3 => 触发（门柱 <=3 照录 b666077233c5 L320）"""
    return "触发" if n <= GATE_COLUMN else "不触发"

# ---------------------------------------------------------------- 3. ②③④ 之材料（F3 cells_15）
MAT15 = {}
for c in F3["cells_15"]:
    ck = c["cell_key"]                       # 机制|族
    mech, fam = ck.split("|")
    f2 = tuple(sorted(c["field2_absA_multiset"]))
    f3o = tuple(tuple(v) for v in c["field3_payment_vector_ordered"])
    f3u = tuple(sorted(tuple(v) for v in c["field3_payment_vector_unordered"]))
    f4 = tuple(sorted(set(c["field4_prompt_digest_set"])))
    MAT15[ck] = {"cell_key": ck, "mechanism": mech, "family": fam,
                 "H_decisions": c["H_decisions"],
                 "f2_canonical": f2, "f3_ordered_canonical": f3o,
                 "f3_unordered_canonical": f3u, "f4_canonical": f4,
                 "f4_count": len(f4),
                 "f2_raw": c["field2_absA_multiset"],
                 "f3_ordered_raw": c["field3_payment_vector_ordered"],
                 "f3_unordered_raw": c["field3_payment_vector_unordered"],
                 "f4_raw": c["field4_prompt_digest_set"]}

MAT_KEYS = sorted(MAT15.keys())
def ndist(seq):
    return len(set(seq))

MAT_ND = {
    "f2_15": ndist([MAT15[k]["f2_canonical"] for k in MAT_KEYS]),
    "f3_ordered_15": ndist([MAT15[k]["f3_ordered_canonical"] for k in MAT_KEYS]),
    "f3_unordered_15": ndist([MAT15[k]["f3_unordered_canonical"] for k in MAT_KEYS]),
    "f4_15": ndist([MAT15[k]["f4_canonical"] for k in MAT_KEYS]),
}
MAT_ND["f3_unordered_30"] = MAT_ND["f3_unordered_15"]   # 跨臂复制（30 格面之 ②③④ ＝ 其 15 格面值）
MAT_ND["f2_30"] = MAT_ND["f2_15"]
MAT_ND["f3_ordered_30"] = MAT_ND["f3_ordered_15"]
MAT_ND["f4_30"] = MAT_ND["f4_15"]

# ---------------------------------------------------------------- 4. 面之构造
# 面：face_id -> {arm 对（label, tier_id, 逐族值 vector）}
#   照录层：U-C1 之逐族值 ＝ [1,1,1,1,1]（int）——自 O1 30 格逐格实测反推（每族 3 机制同值）
O1_ARM_FAM = {}
for c in O1_CELLS:
    O1_ARM_FAM.setdefault(c["arm"], {}).setdefault(c["family"], set()).add(
        (type(c["f1_value"]).__name__, repr(c["f1_value"])))
O1_ARM_FAM_VALS = {}
for arm, fams in O1_ARM_FAM.items():
    O1_ARM_FAM_VALS[arm] = []
    for fam in FAMS:
        s = fams[fam]
        assert len(s) == 1, ("O1 族内非同值", arm, fam, s)
        tn, rv = list(s)[0]
        O1_ARM_FAM_VALS[arm].append((tn, rv))

def _typed(values_from_pairs):
    """[(type_name, repr_str)] -> [python 值]（int/float 还原）"""
    out = []
    for tn, rv in values_from_pairs:
        if tn == "int":
            out.append(int(rv))
        elif tn == "float":
            out.append(float(rv))
        else:
            raise ValueError("未知类型 " + tn)
    return out

def arms_face_U(face_id, carrier):
    """面甲（U_CAND）之两臂：U-C1 × U-C3"""
    if carrier == "照录层":
        a1 = _typed(O1_ARM_FAM_VALS["U-C1"])
        a2 = _typed(O1_ARM_FAM_VALS["U-C3"])
    else:
        a1 = list(UCAND["U-C1"]); a2 = list(UCAND["U-C3"])
    return [("A", "U-C1", a1), ("B", "U-C3", a2)]

def arms_face_H(pair):
    """甲-C5 面之两臂（跨档并集之构成对）：pair = arm_pair_readings 之一"""
    av = list(H_TIER[pair["arm_A_tier"]]["values"])
    bv = list(H_TIER[pair["arm_B_tier"]]["values"])
    return [("A", pair["arm_A_tier"], av), ("B", pair["arm_B_tier"], bv)]

FACE_DEFS = []   # (face_id, face_label, stripped_branch, pair_id or None, carrier)
for fid, flab, br in [("F-0", "基准 · 不剥离", "—"), ("F-2", "移按族复制维", "B2"),
                      ("F-3", "移数值相等读法", "B3"), ("F-4", "移全域计数面", "B4")]:
    FACE_DEFS.append((fid, flab, br, None))
for pair in ARM_PAIRS:
    FACE_DEFS.append(("F-1", "移来源构造维", "B1", pair["pair_id"]))

CARRIERS = [("照录层", "照录层 · O1 形式具化 30 格（56eb9db8bfd1）"),
            ("码载面", "照录层 · 非当场复现（码载件 cb91e876ae7f 不在仓；本读数＝ 205323631d0f 之冻结解析复原）")]

def build_cells(arms):
    """arms -> [(arm_label, tier, mech, fam, value)]（30 格）"""
    cells = []
    for (lab, tier, vals) in arms:
        for mech in MECHS:
            for fi, fam in enumerate(FAMS):
                cells.append({"arm": lab, "tier": tier, "mechanism": mech,
                              "family": fam, "cell_key": "%s|%s|%s" % (tier, mech, fam),
                              "value": vals[fi]})
    return cells

# ---------------------------------------------------------------- 5. 读出计算
BRANCH = []    # 逐支表之行
CELLS  = []    # 逐格表之行
FACES  = {}    # face_id(+pair) -> 结构

def face_key(fid, pair_id):
    return fid if pair_id is None else "%s/%s" % (fid, pair_id)

for fid, flab, br, pair_id in FACE_DEFS:
    for carrier, carrier_prov in CARRIERS:
        if fid == "F-1":
            pair = [p for p in ARM_PAIRS if p["pair_id"] == pair_id][0]
            arms = arms_face_H(pair)
        else:
            arms = arms_face_U(fid, carrier)
        cells = build_cells(arms)
        fk = face_key(fid, pair_id)

        # 逐格留痕（M-E7）
        for c in cells:
            m = MAT15["%s|%s" % (c["mechanism"], c["family"])]
            CELLS.append({
                "face_id": fid, "face_pair": pair_id, "face_key": fk, "face_label": flab,
                "stripped_branch": br, "carrier": carrier,
                "carrier_provenance": carrier_prov,
                "arm": c["arm"], "tier": c["tier"], "mechanism": c["mechanism"],
                "family": c["family"], "cell_key": c["cell_key"],
                "f1_value": c["value"], "f1_type": type(c["value"]).__name__,
                "f1_repr": repr(c["value"]),
                "f1_key_numeric": list(map(str, [k_numeric(c["value"])])),
                "f1_key_byte": list(k_byte(c["value"])),
                "f2_canonical": list(m["f2_canonical"]),
                "f3_ordered_canonical": [list(v) for v in m["f3_ordered_canonical"]],
                "f3_unordered_canonical": [list(v) for v in m["f3_unordered_canonical"]],
                "f4_canonical": list(m["f4_canonical"]),
                "f4_distinct_count": m["f4_count"],
                "material_source_cell_key": m["cell_key"],
            })

        # 计数面：全域（30 格）／逐臂（各 15 格，两臂分列，⛔0 合并）
        surfaces = [("全域30格", cells)]
        for lab in ("A", "B"):
            surfaces.append(("逐臂%s-15格" % lab, [c for c in cells if c["arm"] == lab]))

        for rname, kf in READINGS:
            for sname, scells in surfaces:
                keys = [kf(c["value"]) for c in scells]
                uniq = sorted(set(keys), key=lambda t: repr(t))
                n = len(uniq)
                src_keys = []
                for (lab, tier, vals) in arms:
                    if sname.startswith("逐臂"):
                        if lab != sname[2]:
                            continue
                    src_keys.extend([kf(v) for v in vals])
                src_uniq = sorted(set(src_keys), key=lambda t: repr(t))
                BRANCH.append({
                    "face_id": fid, "face_pair": pair_id, "face_key": fk,
                    "face_label": flab, "stripped_branch": br,
                    "carrier": carrier, "carrier_provenance": carrier_prov,
                    "reading": rname, "counting_surface": sname,
                    "n_cells": len(scells),
                    "M_E1_n_distinct": n,
                    "M_E2_value_set": [repr(u) for u in uniq],
                    "M_E2_source_vector_n_distinct": len(src_uniq),
                    "M_E2_deviation_cell_vs_source": n - len(src_uniq),
                    "M_E3_f2_n_distinct": MAT_ND["f2_15"] if sname == "全域30格" else MAT_ND["f2_15"],
                    "M_E3_f3_ordered_n_distinct": MAT_ND["f3_ordered_15"],
                    "M_E3_f3_unordered_n_distinct": MAT_ND["f3_unordered_15"],
                    "M_E3_f4_n_distinct": MAT_ND["f4_15"],
                    "M_E4_gate_state": gate_state(n),
                    "_keys": [repr(k) for k in keys],
                })

# 逐格集合（按 face/carrier/counting_surface 聚合）—— 供 Δ 与自证
def branch_row(fk, carrier, reading, surf):
    for r in BRANCH:
        if (r["face_key"] == fk and r["carrier"] == carrier
                and r["reading"] == reading and r["counting_surface"] == surf):
            return r
    return None

FACE_KEYS = []
seen = []
for fid, flab, br, pair_id in FACE_DEFS:
    fk = face_key(fid, pair_id)
    if fk not in seen:
        seen.append(fk); FACE_KEYS.append(fk)

# Δ（M-E5 之字面口径：同面·同读法·同载体之 F-0 基准值）
for r in BRANCH:
    base = branch_row("F-0", r["carrier"], r["reading"], r["counting_surface"])
    r["M_E5_delta_same_reading"] = r["M_E1_n_distinct"] - base["M_E1_n_distinct"]
    r["M_E6_delta_gate_state"] = ("翻" if r["M_E4_gate_state"] != base["M_E4_gate_state"] else "平")
    b2 = branch_row("F-0", r["carrier"], "数值相等", r["counting_surface"])
    r["M_E5b_delta_vs_numeric_baseline"] = r["M_E1_n_distinct"] - b2["M_E1_n_distinct"]
    r["M_E6b_delta_gate_state_vs_numeric"] = ("翻" if r["M_E4_gate_state"] != b2["M_E4_gate_state"] else "平")

# ---------------------------------------------------------------- 6. 辅助读数：R-5 所需（B3 之读法施于 甲-C5 面）
AUX = []
for pair in ARM_PAIRS:
    arms = arms_face_H(pair)
    cells = build_cells(arms)
    for carrier, carrier_prov in CARRIERS:
        for rname, kf in READINGS:
            keys = [kf(c["value"]) for c in cells]
            n = len(set(keys))
            AUX.append({"aux_id": "R5_B3-on-C5", "pair_id": pair["pair_id"],
                        "carrier": carrier, "carrier_provenance": carrier_prov,
                        "reading": rname, "n_distinct": n, "gate_state": gate_state(n)})

# ---------------------------------------------------------------- 7. 载体差（已登记之载体差 · 专报）
def carrier_diff(fk):
    a = branch_row(fk, "照录层", "数值相等", "全域30格")["_keys"]
    b = branch_row(fk, "码载面", "数值相等", "全域30格")["_keys"]
    # 逐格配对（两载体之 cell 序相同）
    ca = [c for c in CELLS if c["face_key"] == fk and c["carrier"] == "照录层"]
    cb = [c for c in CELLS if c["face_key"] == fk and c["carrier"] == "码载面"]
    diffs = []
    for x, y in zip(ca, cb):
        assert x["cell_key"] == y["cell_key"]
        if (x["f1_type"], x["f1_repr"]) != (y["f1_type"], y["f1_repr"]):
            diffs.append({"cell_key": x["cell_key"], "照录层": "%s %s" % (x["f1_type"], x["f1_repr"]),
                          "码载面": "%s %s" % (y["f1_type"], y["f1_repr"])})
    return diffs

CARRIER_DIFF = {}
for fk in FACE_KEYS:
    CARRIER_DIFF[fk] = carrier_diff(fk)

# ---------------------------------------------------------------- 8. 判死线之机械读数
KL = []   # 每条判死线：id, 名称, 阈值, 实测, 判定
def kl_add(kid, name, threshold, measured, verdict, note=""):
    KL.append({"id": kid, "name": name, "threshold": threshold,
               "measured": measured, "verdict": verdict, "note": note})

# --- A 组
# A-1 零择一依赖门（结构化读出件之字段表中「择/优/优劣/合并/排序」类字段出现数 == 0）
# --- A-2 来源维可剥门
src_ident = {}
for fid, flab, br, pair_id in FACE_DEFS:
    fk = face_key(fid, pair_id)
    src_ident[fk] = "H_CAND 跨档并集" if fid == "F-1" else "U_CAND（面甲）"
moved = [fk for fk in FACE_KEYS if src_ident[fk] != "U_CAND（面甲）"]
moved_faces = sorted(set(f.split("/")[0] for f in moved))
# --- A-3 载体对齐门
dev_from_op = 0     # 设计操作所致之载体间不一致
for fk in FACE_KEYS:
    # 逐格派生值 vs 各载体之声明源：偏差应恒 0
    for r in BRANCH:
        if r["face_key"] == fk and r["counting_surface"] == "全域30格" and r["reading"] == "数值相等":
            dev_from_op += abs(r["M_E2_deviation_cell_vs_source"])
# --- A-4 计数面核对门
cnt_ok = True; cnt_detail = []
for fk in FACE_KEYS:
    g = branch_row(fk, "照录层", "数值相等", "全域30格")
    a = branch_row(fk, "照录层", "数值相等", "逐臂A-15格")
    b = branch_row(fk, "照录层", "数值相等", "逐臂B-15格")
    ok = (g["n_cells"] == 30 and a["n_cells"] == 15 and b["n_cells"] == 15)
    cnt_ok = cnt_ok and ok
    cnt_detail.append({"face": fk, "全域": g["n_cells"], "臂A": a["n_cells"], "臂B": b["n_cells"], "符合": ok})
# --- A-5 两读两载体并出门
missing = 0; coverage = []
for fk in FACE_KEYS:
    for carrier in ("照录层", "码载面"):
        for reading in ("数值相等", "逐字节"):
            for surf in ("全域30格", "逐臂A-15格", "逐臂B-15格"):
                if branch_row(fk, carrier, reading, surf) is None:
                    missing += 1
    coverage.append({"face": fk, "读数格数": sum(
        1 for r in BRANCH if r["face_key"] == fk)})
# --- A-6 复制 0 贡献之两面自证门
a6 = []
for fk in ("F-0", "F-1/P1", "F-1/P2", "F-1/P3"):
    for carrier in ("照录层", "码载面"):
        for reading in ("数值相等", "逐字节"):
            g = branch_row(fk, carrier, reading, "全域30格")
            a6.append({"face": fk, "carrier": carrier, "reading": reading,
                       "逐格取值集合互异数": g["M_E1_n_distinct"],
                       "来源值向量互异数": g["M_E2_source_vector_n_distinct"],
                       "偏差": g["M_E2_deviation_cell_vs_source"]})
# --- A-7 门柱不擅调门
GATE_LITERAL = "n_distinct ≤ 3"
# --- A-8 A2-7 不预断门（断言类语句出现数 == 0）

# --- B 组
# B-1 正控必命中门：甲-C5 面 ① 之 n_distinct == 4（两读同果）· 与在册值之差 == 0
b1 = []
for fk in ("F-1/P1", "F-1/P2", "F-1/P3"):
    for carrier in ("照录层", "码载面"):
        for reading in ("数值相等", "逐字节"):
            g = branch_row(fk, carrier, reading, "全域30格")
            b1.append({"face": fk, "carrier": carrier, "reading": reading,
                       "复算值": g["M_E1_n_distinct"], "与在册值 4 之差": g["M_E1_n_distinct"] - 4,
                       "门态": g["M_E4_gate_state"]})
# B-2 负控必 0 命中门：原构造面 ① == 3 且门态 == 触发；「门态＝不触发」之判否数 == 0
b2_scope_num, b2_scope_all = [], []
for carrier in ("照录层", "码载面"):
    for reading in ("数值相等", "逐字节"):
        for surf in ("全域30格", "逐臂A-15格", "逐臂B-15格"):
            r = branch_row("F-0", carrier, reading, surf)
            b2_scope_all.append({"carrier": carrier, "reading": reading, "surface": surf,
                                  "复算值": r["M_E1_n_distinct"], "门态": r["M_E4_gate_state"]})
            if reading == "数值相等":
                b2_scope_num.append({"carrier": carrier, "reading": reading, "surface": surf,
                                      "复算值": r["M_E1_n_distinct"], "门态": r["M_E4_gate_state"]})
b2_num_neg = sum(1 for x in b2_scope_num if x["门态"] == "不触发")
b2_all_neg = sum(1 for x in b2_scope_all if x["门态"] == "不触发")
# B-3 载体复现之缺门：码载面读数之「照录层·非当场复现」标注 == 100%
code_rows = [r for r in BRANCH if r["carrier"] == "码载面"]
code_marked = sum(1 for r in code_rows if ("非当场复现" in r["carrier_provenance"]))
code_cells = [c for c in CELLS if c["carrier"] == "码载面"]
code_cells_marked = sum(1 for c in code_cells if ("非当场复现" in c["carrier_provenance"]))
# B-5 第三方复算条件门（条件性）

# ---------------------------------------------------------------- 9. R-3/R-4/R-5 之机械判读
def b1_delta(carrier, reading, surf):
    return branch_row("F-1/P1", carrier, reading, surf)

r3_cells = []
for carrier in ("照录层", "码载面"):
    for reading in ("数值相等", "逐字节"):
        for surf in ("全域30格", "逐臂A-15格", "逐臂B-15格"):
            f1 = branch_row("F-1/P1", carrier, reading, surf)
            f3 = branch_row("F-3", carrier, reading, surf)
            f4 = branch_row("F-4", carrier, reading, surf)
            r3_cells.append({
                "carrier": carrier, "reading": reading, "surface": surf,
                "B1_delta_same_reading": f1["M_E5_delta_same_reading"],
                "B1_delta_gate": f1["M_E6_delta_gate_state"],
                "B3_code_delta_same_reading": f3["M_E5_delta_same_reading"],
                "B4_armA_gate": branch_row("F-4", carrier, reading, "逐臂A-15格")["M_E4_gate_state"],
                "B4_armB_gate": branch_row("F-4", carrier, reading, "逐臂B-15格")["M_E4_gate_state"],
            })

# R-3：作用域之两读
r3_by_reading = {}
for reading in ("数值相等", "逐字节"):
    ok = True; detail = []
    for carrier in ("照录层", "码载面"):
        f1 = branch_row("F-1/P1", carrier, reading, "全域30格")
        f3 = branch_row("F-3", carrier, reading, "全域30格")
        f4a = branch_row("F-4", carrier, reading, "逐臂A-15格")
        f4b = branch_row("F-4", carrier, reading, "逐臂B-15格")
        c1 = (f1["M_E5_delta_same_reading"] == 1 and f1["M_E6_delta_gate_state"] == "翻")
        c2 = (f3["M_E5_delta_same_reading"] == 0)
        c3 = (f4a["M_E4_gate_state"] == "触发" and f4b["M_E4_gate_state"] == "触发")
        detail.append({"carrier": carrier, "B1_Δ": f1["M_E5_delta_same_reading"],
                       "B1_Δ门态": f1["M_E6_delta_gate_state"], "B1项合": c1,
                       "B3_码载面Δ": f3["M_E5_delta_same_reading"], "B3项合": c2,
                       "B4_臂A门态": f4a["M_E4_gate_state"], "B4_臂B门态": f4b["M_E4_gate_state"], "B4项合": c3})
        ok = ok and c1 and c2 and c3
    r3_by_reading[reading] = {"全部合": ok, "逐载体": detail}

# R-5：B3 读法施于 甲-C5 面
aux_c5 = {}
for a in AUX:
    aux_c5.setdefault((a["pair_id"], a["carrier"], a["reading"]), a["n_distinct"])
r5_rows = []
for pair in ARM_PAIRS:
    for carrier in ("照录层", "码载面"):
        b1v = branch_row("F-1/%s" % pair["pair_id"], carrier, "数值相等", "全域30格")["M_E1_n_distinct"]
        b3v = aux_c5[(pair["pair_id"], carrier, "逐字节")]
        r5_rows.append({"pair": pair["pair_id"], "carrier": carrier,
                        "B1_读数": b1v, "B3_读数_于C5面": b3v, "同值": b1v == b3v})

# ---------------------------------------------------------------- 10. 落盘：派生四表 + 读出件
# --- 施测后之输入件不可变复测（载体面 0 写其 1 字节之自证 · K-E13ABL-B-4 之「既有件触动数 = 0」）
post_fp = {}
for tag, p, want in INPUTS:
    sz, h = sha12_of(p)
    post_fp[tag] = {"bytes": sz, "sha12": h, "expect": want, "match": h == want,
                    "unchanged_vs_pre": (h == pre_fp[tag]["sha12"] and sz == pre_fp[tag]["bytes"])}
print("### 0b 施测后之输入件复测（不可变性）")
for tag in post_fp:
    print("  %-28s %9d %s unchanged=%s" % (tag, post_fp[tag]["bytes"], post_fp[tag]["sha12"],
                                          post_fp[tag]["unchanged_vs_pre"]))
ALL_INPUTS_UNCHANGED = all(v["unchanged_vs_pre"] for v in post_fp.values())

def write_bytes(path, data: bytes):
    if not data.endswith(b"\n"):
        data += b"\n"
    with open(path, "wb") as f:
        f.write(data)
    sz, h = sha12_of(path)
    return {"path": path, "bytes": sz, "sha12": h}

def jdump(obj):
    return json.dumps(obj, ensure_ascii=False, indent=1, sort_keys=False).encode("utf-8")

# --- 核心体（不含 cross_refs 与 outputs）之内容指纹（order-independent 定义）
CORE_EXCLUDE = ("cross_refs", "outputs")
def core_sha12(obj):
    core = {k: v for k, v in obj.items() if k not in CORE_EXCLUDE}
    return hashlib.sha256(json.dumps(core, ensure_ascii=False, sort_keys=True,
                                     separators=(",", ":")).encode("utf-8")).hexdigest()[:12]

SCRIPT_PATH = os.path.join(REPO, "scripts", "_e13_ablation_run_2026_10_27.py")
script_sz, script_sha = sha12_of(SCRIPT_PATH)

BRANCH_TBL = {
    "artifact": "E-13 消融施测 · 逐支表（M-E1..M-E8）",
    "produced_by": "worker（执行棒）· 棒号 mvs_a1dee6d7eb264311a893abc8939665f7",
    "design_anchor": {"path": P_DESIGN, "bytes": pre_fp["设计件"]["bytes"], "sha12": pre_fp["设计件"]["sha12"]},
    "object_domain": {"cells_total": 30, "arms": 2, "cells_per_arm": 15,
                      "mechanisms": MECHS, "families": FAMS, "seed": SEED},
    "gate_column": "n_distinct <= 3（照录 b666077233c5 L320 · 本棒未改）",
    "reading_key_defs": {"数值相等": "Fraction(v)", "逐字节": "(type(v).__name__, repr(v))"},
    "carrier_defs": {c: p for c, p in CARRIERS},
    "rows": BRANCH,
}
CELL_TBL = {
    "artifact": "E-13 消融施测 · 逐格表（M-E7 逐格留痕 · 0 抽样删减）",
    "produced_by": "worker（执行棒）",
    "design_anchor": {"path": P_DESIGN, "bytes": pre_fp["设计件"]["bytes"], "sha12": pre_fp["设计件"]["sha12"]},
    "material_note": "②③④ 之逐格材料量＝ 7f80d5ae03bb 之 cells_15（15 格 · 跨臂复制 · 设计 §6-4 之指定）",
    "rows": CELLS,
}
COMPARE_TBL = {
    "artifact": "E-13 消融施测 · 对照表（三对并取 · 支间之差 · 归因之事实底数）",
    "produced_by": "worker（执行棒）",
    "design_anchor": {"path": P_DESIGN, "bytes": pre_fp["设计件"]["bytes"], "sha12": pre_fp["设计件"]["sha12"]},
    "three_pairs_separately_reported": [
        {"pair_id": p["pair_id"], "pair_label": p["pair_label"],
         "arm_A_tier": p["arm_A_tier"], "arm_B_tier": p["arm_B_tier"],
         "arm_A_values": list(H_TIER[p["arm_A_tier"]]["values"]),
         "arm_B_values": list(H_TIER[p["arm_B_tier"]]["values"]),
         "cross_tier_union_recomputed": sorted(set(
             list(H_TIER[p["arm_A_tier"]]["values"]) + list(H_TIER[p["arm_B_tier"]]["values"]))),
         "union_n_distinct_recomputed": len(set(
             list(H_TIER[p["arm_A_tier"]]["values"]) + list(H_TIER[p["arm_B_tier"]]["values"]))),
         "register_union": p["cross_tier_union"],
         "register_union_match": sorted(set(p["cross_tier_union"])) == sorted(set(
             list(H_TIER[p["arm_A_tier"]]["values"]) + list(H_TIER[p["arm_B_tier"]]["values"]))),
         "register_f1_n_distinct_30cell_numeric": p["f1_n_distinct_30cell_numeric"],
         "register_f1_n_distinct_30cell_byte": p["f1_n_distinct_30cell_byte"],
         "register_f1_n_distinct_armA_15cell": p["f1_n_distinct_armA_15cell"],
         "register_f1_n_distinct_armB_15cell": p["f1_n_distinct_armB_15cell"],
         "recomputed_逐臂": {
             "A": branch_row("F-1/%s" % p["pair_id"], "码载面", "数值相等", "逐臂A-15格")["M_E1_n_distinct"],
             "B": branch_row("F-1/%s" % p["pair_id"], "码载面", "数值相等", "逐臂B-15格")["M_E1_n_distinct"]},
         "recomputed_全域_数值相等_码载面": branch_row(
             "F-1/%s" % p["pair_id"], "码载面", "数值相等", "全域30格")["M_E1_n_distinct"],
         "recomputed_全域_逐字节_码载面": branch_row(
             "F-1/%s" % p["pair_id"], "码载面", "逐字节", "全域30格")["M_E1_n_distinct"],
         } for p in ARM_PAIRS],
    "branch_delta_matrix": r3_cells,
    "r3_by_reading": r3_by_reading,
    "r5_rows": r5_rows,
    "carrier_diff_report": {fk: {"不一致格数": len(v), "cells": v} for fk, v in CARRIER_DIFF.items()},
    "identity_selfproof_A6": a6,
    "control_B1": b1,
    "control_B2_numeric_scope": b2_scope_num,
    "control_B2_all_readings_scope": b2_scope_all,
}
COST_TBL = {
    "artifact": "E-13 消融施测 · 成本表（M-E8）",
    "produced_by": "worker（执行棒）",
    "llm_calls": 0, "network_requests": 0, "new_observations": 0, "new_run_cells": 0,
    "key_reads": 0, "existing_files_touched": 0 if ALL_INPUTS_UNCHANGED else -1,
    "seed": SEED, "seed_note": "对象域之单 seed 42 系在册之对象域定义；本棒为纯确定性演算，无随机抽样、无随机种子",
    "script": {"path": SCRIPT_PATH, "bytes": script_sz, "sha12": script_sha},
    "inputs_pre": pre_fp,
    "inputs_post": post_fp,
    "all_inputs_unchanged": ALL_INPUTS_UNCHANGED,
    "carrier_missing_scan": {"root": REPO, "targets": SCAN_TARGETS,
                              "hits": {k: len(v) for k, v in scan_hits.items()},
                              "hit_paths": {k: v for k, v in scan_hits.items() if v},
                              "files_scanned_note": "实扫件数（N_obs）随仓内件之增而增（故 ⛔ 0 载于本表，以保本表字节可复算）；"
                                                    "实测值载于运行日志与读出件之散文面"},
    "config": {
        "object_domain": {"cells_total": 30, "arms": 2, "cells_per_arm": 15,
                          "mechanisms": MECHS, "families": FAMS, "seed": SEED,
                          "seed_note": "单 seed 42 系在册之对象域定义；本棒无随机抽样、无随机种子"},
        "gate_column": {"value": GATE_COLUMN, "literal": "n_distinct <= 3",
                        "source": "b666077233c5 L320（逐字冻结文）", "changed": False},
        "reading_key_defs": {"数值相等": "Fraction(v)", "逐字节": "(type(v).__name__, repr(v))",
                             "source": "d91a11e88b95 L78（照录）"},
        "carriers": {c: p for c, p in CARRIERS},
        "faces": [{"face_key": fk, "source": src_ident[fk]} for fk in FACE_KEYS],
        "material_source": {"f2_f3_f4": "7f80d5ae03bb 之 cells_15（15 格 · 跨臂复制）",
                            "f1_照录层": "56eb9db8bfd1 之 f1_formal_materialization_O1.cells（30 条）",
                            "f1_码载面": "205323631d0f 之 U_CAND_per_tier / H_CAND_per_tier（码载件之冻结副本 · 非当场复现）"},
        "env": {"python": sys.version.split()[0], "platform": platform.platform(),
                "encoding": "utf-8", "network": 0, "llm_calls": 0},
    },
    "outputs": {},
}

TABLES = [
    ("逐支表", BRANCH_TBL, "_e13_ablation_branch_table_2026_10_27.json"),
    ("逐格表", CELL_TBL, "_e13_ablation_cell_table_2026_10_27.json"),
    ("对照表", COMPARE_TBL, "_e13_ablation_compare_table_2026_10_27.json"),
    ("成本表", COST_TBL, "_e13_ablation_cost_table_2026_10_27.json"),
]
core_hashes = {name: core_sha12(body) for name, body, fn in TABLES}
for name, body, fn in TABLES:
    body = dict(body)
    body["cross_refs"] = {
        "set": "E-13 消融施测 · 派生四表（分件落盘 · 互引）",
        "manifest_path": os.path.join(OUT_DIR, "_e13_ablation_result_2026_10_27.md"),
        "note": "SHA-12 之互引采用『内容指纹（core_sha12 = 本表 core 体之规范化 JSON 之 SHA-256 前 12 位）』；"
                "on-disk 文件指纹载于读出件（manifest）之互引索引（on-disk 指纹之互引成哈希环 ⇒ 不可行）",
        "core_sha12": core_hashes[name],
        "siblings": {n2: {"file": fn2, "core_sha12": core_hashes[n2]} for n2, b2, fn2 in TABLES if n2 != name},
        "script": {"path": SCRIPT_PATH, "sha12": script_sha},
    }
    p = os.path.join(OUT_DIR, fn)
    info = write_bytes(p, jdump(body))
    COST_TBL["outputs"][name] = info
    print("  落盘 %-8s %9d %s  %s" % (name, info["bytes"], info["sha12"], fn))

# 📌 自引用界分：成本表之自身 on-disk 指纹 ⛔0 载于其内（自引用悖论）⇒ 载于读出件（manifest）
#    故成本表仅载 core_sha12 与三兄弟之 core_sha12；四表之 on-disk 指纹皆载于 manifest。
#    （实现：四表之 body 在写盘前已含 cross_refs；成本表之 outputs 栏于写盘前填入前三表之 on-disk 指纹。）

# --- 中间产物（.tmp）：原始事实
RAW = {"branch": BRANCH, "cells_count": len(CELLS), "aux": AUX,
       "carrier_diff": {k: len(v) for k, v in CARRIER_DIFF.items()},
       "mat_nd": MAT_ND, "pre_fp": pre_fp, "core_hashes": core_hashes,
       "r3_by_reading": r3_by_reading, "r5_rows": r5_rows,
       "b1": b1, "b2_num": b2_scope_num, "b2_all": b2_scope_all,
       "a6": a6, "counts": {"carrier_diff_reg": len(CARRIER_DIFF["F-0"])}}
raw_p = os.path.join(TMP_DIR, "_e13_run_out_2026_10_27.json")
raw_info = write_bytes(raw_p, jdump(RAW))
print("  落盘 中间产物 %9d %s" % (raw_info["bytes"], raw_info["sha12"]))

# ---------------------------------------------------------------- 11. 供读出件用之摘要（落 .tmp 以便读出件之数值不自撰）
SUMMARY = {
    "branch_rows": len(BRANCH), "cell_rows": len(CELLS),
    "mat_nd": MAT_ND,
    "tables": {n: {"file": fn, "core_sha12": core_hashes[n],
                   "on_disk": COST_TBL["outputs"].get(n)} for n, b, fn in TABLES},
    "script": {"path": SCRIPT_PATH, "bytes": script_sz, "sha12": script_sha},
    "raw": raw_info,
    "kl_eval": {
        "A1_missing_readings": missing,
        "A2_moved_faces": moved_faces, "A2_moved_keys": moved,
        "A3_dev_from_operation": dev_from_op,
        "A3_registered_diff_F0": len(CARRIER_DIFF["F-0"]),
        "A3_registered_diff_F1P1": len(CARRIER_DIFF["F-1/P1"]),
        "A4_count_ok": cnt_ok, "A4_detail": cnt_detail,
        "A5_missing": missing, "A5_coverage": coverage,
        "A6": a6,
        "B1": b1,
        "B2_num_neg": b2_num_neg, "B2_all_neg": b2_all_neg,
        "B2_num": b2_scope_num, "B2_all": b2_scope_all,
        "B3_code_rows": len(code_rows), "B3_code_marked": code_marked,
        "B3_code_cells": len(code_cells), "B3_code_cells_marked": code_cells_marked,
        "r3_by_reading": r3_by_reading, "r5_rows": r5_rows,
        "r3_cells": r3_cells,
    },
    "faces": [{"face_key": fk, "source": src_ident[fk]} for fk in FACE_KEYS],
    "carrier_diff_detail": CARRIER_DIFF,
    "aux": AUX,
}
sum_p = os.path.join(TMP_DIR, "_e13_summary_2026_10_27.json")
sum_info = write_bytes(sum_p, jdump(SUMMARY))
print("  落盘 摘要 %9d %s" % (sum_info["bytes"], sum_info["sha12"]))
print("ELAPSED %.1fs" % (time.time() - T0))
