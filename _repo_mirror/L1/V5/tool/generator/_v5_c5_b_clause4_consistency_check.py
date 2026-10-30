# -*- coding: utf-8 -*-
"""
V5 / V3 修复线 C5 / 棒 2a -- 裁项④「码长随投影维数同步」与 B 组自洽性离线核验
V3X-C5B-CLAUSE4-2026-09-29-A1

背景: 提案件 §7 第 2 题列为 B 组专属; PI 确认批 5 裁「码长随投影维数同步」,
      并附条件: 若 2a 实测显示该条与 B 组不自洽 => 停步报告, 0 自裁.

本脚本 0 调网络 / 0 读 key / 0 写 results/ / 0 改任何既有件, 纯只读 + stdout.
只读输入:
  results/deposon_volcengine_22caption_embedding_2026_09_10.json  (svd2_coords, per_class_members)
  results/deposon_v2_phase4_f4_2026_09_11.json                    (semantic_hash / dual_24bit)
  results/_v3_construct_degradation_diag_2026_09_23.json          (基线四读数核对)

⚠️ 本脚本 0 产出修复件读数; 第 6 节为「码长臂隔离诊断」, 0 替代 B 组, 0 判档位.
"""
import json
from itertools import combinations
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parents[1]
EMB = json.load(open(BASE / "results/deposon_volcengine_22caption_embedding_2026_09_10.json",
                     encoding="utf-8"))
F4 = json.load(open(BASE / "results/deposon_v2_phase4_f4_2026_09_11.json", encoding="utf-8"))
DIAG = json.load(open(BASE / "results/_v3_construct_degradation_diag_2026_09_23.json",
                      encoding="utf-8"))

svd2 = EMB["svd2_coords"]
IDS = EMB["concept_ids"]
CLASSES = EMB["per_class_members"]
CID2CLS = {cid: c for c, ms in CLASSES.items() for cid in ms}
F4D = F4["dual_fingerprints"]  # dict keyed by caption_id


def bits_of(coords, hyperplanes):
    p = np.asarray(coords) @ hyperplanes.T
    return (p > 0).astype(int)


def code(bits):
    return hex(int("".join(str(b) for b in bits), 2))[2:]


def pair_stats(bits_list):
    n = len(bits_list)
    zero, tot, s = 0, 0, 0
    intra = {c: [] for c in CLASSES}
    ids = [b[0] for b in bits_list]
    arrs = [b[1] for b in bits_list]
    for i, j in combinations(range(n), 2):
        d = int(np.sum(arrs[i] != arrs[j]))
        tot += 1
        s += d
        if d == 0:
            zero += 1
        if ids[i] in CID2CLS and CID2CLS[ids[i]] == CID2CLS[ids[j]]:
            intra[CID2CLS[ids[i]]].append(d)
    return {
        "n_distinct": len({tuple(a) for a in arrs}),
        "hamming_pairs_total": tot,
        "hamming_pairs_zero": zero,
        "hamming_mean_observed": round(s / tot, 3),
        "class_intra_hamming": {c: (round(float(np.mean(v)), 2) if v else None)
                                for c, v in intra.items()},
    }


def lsh(coords_map, n_plane, dim, seed):
    np.random.seed(seed)
    hp = np.random.randn(n_plane, dim)
    out = []
    for cid in IDS:
        b = bits_of(coords_map[cid], hp)
        out.append((cid, b))
    return out


out = {}

# ---- 1. 12-bit 基线离线复现 (校准机具) ----
np.random.seed(42)
hp12 = np.random.randn(12, 2)
base_codes = {}
for cid in IDS:
    b = bits_of(svd2[cid], hp12)
    base_codes[cid] = code(b).zfill(3)
stored_match = sum(1 for c in IDS if base_codes[c] == F4D[c]["semantic_hash"])
out["1_baseline_reproduction"] = {
    "semantic_hash_match_vs_f4": f"{stored_match}/22",
    "n_distinct": len(set(base_codes.values())),
    "dual_match_vs_f4": f"{sum(1 for c in IDS if F4D[c]['byte_hash'][:6] + base_codes[c] == F4D[c]['dual_24bit'])}/22",
    "diag_claims": {
        "n_distinct": DIAG["summary"]["diagnosis"][4]["evidence"]["stored_n_distinct_codes"],
        "hamming_pairs_zero": DIAG["summary"]["diagnosis"][4]["evidence"]["hamming_pairs_zero"],
        "hamming_mean_observed": DIAG["summary"]["diagnosis"][4]["evidence"]["hamming_mean_observed"],
    },
}

# ---- 2. 裁项④ 算术: 每维超平面数 ----
out["2_clause4_arithmetic"] = {
    "on_disk_literal": "12 hyperplanes / 2 dims = 6 planes per dim (V0.2 spec L38 randn(12,2))",
    "planes_per_dim": 12 // 2,
    "k3": {"dims": 3, "n_plane": 18, "code_len_bit": 18, "d_over_2_reference": 18 / 2},
    "k4": {"dims": 4, "n_plane": 24, "code_len_bit": 24, "d_over_2_reference": 24 / 2},
}

# ---- 3. 码长 -> hex 宽度 可表示性 (无损往返) ----
hexchk = {}
for name, blen in (("k3_18bit", 18), ("k4_24bit", 24), ("baseline_12bit", 12)):
    width = blen // 4 + (1 if blen % 4 else 0)
    rng = np.random.default_rng(0)
    vals = [0, (1 << blen) - 1, 1] + [int(v) for v in rng.integers(0, 1 << blen, 2000)]
    ok = all(int(hex(v)[2:].zfill(width), 16) == v for v in vals)
    lead_bits = blen - 4 * (width - 1)
    hexchk[name] = {
        "bit_len": blen, "zfill_width": width, "hex_chars": width,
        "leading_digit_holds_bits": lead_bits,
        "lossless_roundtrip_2004_samples": ok,
        "d_over_2": blen / 2,
        "dual_width_hex": 6 + width,
        "dual_true_bits": 24 + blen,
    }
out["3_hex_representability"] = hexchk

# ---- 4. dual_24bit 字段名实偏离 ----
out["4_dual_field_name_vs_reality"] = {
    "baseline": {"name": "dual_24bit", "hex": 9, "true_bits": 36},
    "k3": {"name": "dual_24bit", "hex": 11, "true_bits": 42},
    "k4": {"name": "dual_24bit", "hex": 12, "true_bits": 48},
    "note": "字段名 24 bit 在三档下均与实际位宽不符; k3 偏离最大(42 bit, 名实比 24/42)",
}

# ---- 5. 基线 7-seed 对照 (离线, 仅供口径对齐) ----
sw = []
for sd in range(42, 49):
    st = pair_stats(lsh(svd2, 12, 2, sd))
    sw.append({"seed": sd, "n_distinct": st["n_distinct"],
               "hamming_mean": st["hamming_mean_observed"],
               "zero_pairs": st["hamming_pairs_zero"]})
out["5_baseline_12bit_seed_sweep"] = sw

# ---- 6. 码长臂隔离诊断 (⚠️ 0 替代 B 组) ----
# 固定 2 维存储坐标, 仅把超平面数 12 -> 18 (即 6->9 面/维), 隔离「码长」臂.
# 目的: 检验裁项④ 的码长臂单独是否指向改善; 0 换坐标空间, 0 代表 B 组.
iso = {}
for sd in range(42, 49):
    st = pair_stats(lsh(svd2, 18, 2, sd))
    iso[f"seed{sd}"] = {"n_distinct": st["n_distinct"],
                        "hamming_mean": st["hamming_mean_observed"],
                        "zero_pairs": st["hamming_pairs_zero"]}
out["6_codelength_arm_isolation_2dim_18plane"] = {
    "purpose": "隔离码长臂; 0 换坐标空间; 0 替代 B 组; 0 判档位",
    "baseline_12plane_n_distinct_by_seed": {f"seed{s['seed']}": s["n_distinct"] for s in sw},
    "isolation_18plane": iso,
    "hamming_d_over_2_reference_18bit": 9.0,
    "class_intra_seed42": pair_stats(lsh(svd2, 18, 2, 42))["class_intra_hamming"],
}

print(json.dumps(out, ensure_ascii=True, indent=1))
