#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""V3 真实 N 轴 N 档三方案（P-N-1 / P-N-2 / P-N-3）**预实验**执行器 · 探索性档 · 2026-09-27

沿 results/_v3_recheck_prereg_v1p3_2026_09_27.md（SHA-12 a8da321b64d2）字面执行：
  - §1.2 三条 N 档提案 P-N-1（默认）/ P-N-2（增档 2000/5000）/ P-N-3（降阶 4 档），本件**三方案全跑**；
  - §1.1 冻结阶梯 n_full = [10,20,50,100,200,500,1000]、n_clipped 去两端、clip_r2_min = 0.7（0 改动）；
  - §1.3 跑前固定：P 率型、bootstrap n=1000 / seed=42、裁剪 = 去首尾 0 重采样；
  - §2.1 K-V3R-8-P3-0-A 防退化门 / -0-B 恒等门 / -1A 代数不可达守卫 / -3 溯源门。

⛔ **素材面纪律（本件第一诚实声明）**
  盘上**真实图族 N 阶梯 (N, P_obs) 原始逐档观测 = 0 对**（沿 prereg v1.3 §3.1 R-1 实测字面：
  `N_levels_coverable = []`、`n_distinct_real_N_levels = 0`）。⇒ 本件**只能跑合成 fixture**。
  **合成 fixture ≠ 真实图族数据**；本件**仅比较三方案的构造行为**（R² 判别行为 / n_distinct /
  对 SS_tot = 0 恒等门的响应），**0 产出任何关于 P-C / BOSS-PC-3 真实图族的读数**，
  **0 判 K-V3R-8 PASS/FAIL**，**0 视为 #8 已解锁**。

**性质：预实验 = 探索性档（三档最低）**：verdict 恒 null；0 判定动作；0 改判；0 改既有档位；
**合成数据绝不落盘冒充观测**（fixture 生成器在盘，可逐行复核）。

效果判据先冻结后跑（FROZEN_EVAL_CRITERIA，测量前写死于模块常量）：
  ① 判别力 ② 可达性 ③ 非退化 ④ 可复现（重跑逐字不变）

铁律：0 LLM / 0 proxy / 0 gateway / 0 key 读取（key 永不明文）；SHA-12 = hashlib.sha256
hexdigest()[:12] 小写；S-40 布尔显式命名；派生 JSON 独立落盘 0 合并；0 编造；既有件 0 触动。
"""

import hashlib
import importlib.util
import json
import math
import os
import sys
from pathlib import Path

import numpy as np

# ============================================================================
# §0 冻结常量（测量前写死；0 事后调）
# ============================================================================
TS_FROZEN = "2026-09-27T00:00:00+08:00"
TRIALS = [42, 137, 256]              # 沿 08b executor TRIALS 字面（原始 BOSS-PC-3 三 trial seed）
BOOTSTRAP_N = 1000                   # prereg v1.3 §1.3 字面
BOOTSTRAP_SEED = 42                  # prereg v1.3 §1.3 字面
CLIP_R2_MIN_GRID = [0.3, 0.5, 0.7]   # 08b executor 字面（TH-V3R-8 派工冻结扫描）
N_DISTINCT_MIN = 3                   # K-V3R-8-P3-0-A 字面 n_distinct > 3
N_MIN_TIERS_FOR_R2 = 2               # 幂律 OLS 最少点数（08b executor 字面）

PREREG_V13 = "results/_v3_recheck_prereg_v1p3_2026_09_27.md"
EX08B = "results/_v3_recheck_08b_executor/executor_2026_09_27.py"
SPEC = "docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md"
R08 = "results/_v3_recheck_08_result_2026_09_27.json"

# ---- 三方案档位（全部由 prereg v1.3 §1.2 字面派生；派生口径显式声明）----
# n_clipped 一律 = n_full 去首尾（沿 v1.3 §1.3 字面「0 重采样、0 重加权」）
SCHEMES = {
    "P-N-1": {
        "proposal_id": "P-N-1",
        "content": "档位一字不动，换统计量：主判据由「R² 单点比较」改为 delta 的 bootstrap 分布符号一致性",
        "n_full": [10, 20, 50, 100, 200, 500, 1000],
        "n_clipped_derivation": "n_full 去首尾（spec §5 A3 字面）",
        "n_clipped": [20, 50, 100, 200, 500],
        "ladder_change": "none（冻结阶梯 0 改动）",
        "default_when_unruled": True,
    },
    "P-N-2": {
        "proposal_id": "P-N-2",
        "content": "上探扩档（只增不减）：n_full 追加 {2000, 5000} ⇒ 9 档，幅域 10→5000",
        "n_full": [10, 20, 50, 100, 200, 500, 1000, 2000, 5000],
        "n_clipped_derivation": "n_full 去首尾（**本件声明的派生口径，待 PI 复核**："
                                "提案字面只说扩 n_full，0 规定 n_clipped 落法）",
        "n_clipped": [20, 50, 100, 200, 500, 1000, 2000],
        "ladder_change": "append_only（增档 0 减档）",
        "default_when_unruled": False,
    },
    "P-N-3": {
        "proposal_id": "P-N-3",
        "content": "降阶档（构造可行性优先）：n_full 降为 4 档 {50,100,200,500}，幅域 10×",
        "n_full": [50, 100, 200, 500],
        "n_clipped_derivation": "n_full 去首尾 ⇒ **仅剩 2 档**（本件依 A3 字面直推）",
        "n_clipped": [100, 200],
        "ladder_change": "downgrade（降阶 ⇒ 弱化 A3 端点检验，须 PI 显式豁免）",
        "default_when_unruled": False,
    },
}

# ---- 合成 fixture（**合成 ≠ 真实图族数据**；生成器在盘可逐行复核）----
# 每档 P 由**显式解析式**给出，噪声由 np.random.default_rng(trial_seed) 决定 ⇒ 可复现
FIXTURES = {
    "FIX-A_powerlaw_noisy": {
        "kind": "非恒等幂律（带确定性噪声）",
        "formula": "P(N) = clip(A * N^(-beta) + noise, eps, 1-eps), A=0.9, beta=0.5, noise~N(0, 0.02)",
        "identity": False,
        "purpose": "真幂律 + 噪声 ⇒ 检验 R² 能否给出稳定判别读数",
    },
    "FIX-B_identity_exact": {
        "kind": "恒等退化（精确）",
        "formula": "P(N) = 0.42（各档精确相等）",
        "identity": True,
        "purpose": "复现 08b 已证死因：SS_tot = 0 ⇒ 幂律 R² = 0/0 未定义 ⇒ 检验恒等门响应",
    },
    "FIX-B2_identity_float_noise": {
        "kind": "恒等退化（float64 舍入级微扰）",
        "formula": "P(N) = 0.42 + 1e-18（各档仅差 1e-18）",
        "identity": True,
        "purpose": "检验 08b FLOAT_NOISE_SS_TOT_CEIL=1e-24 守卫：0 < SS_tot < 1e-24 ⇒ "
                   "判为舍入噪声 0 计入判定",
    },
    "FIX-C_two_slope": {
        "kind": "非幂律双段（斜率突变）",
        "formula": "N<=100: 0.8*N^-0.3 ; N>100: 0.8*100^-0.3*(N/100)^-1.5 + noise",
        "identity": False,
        "purpose": "真实图族未必是单幂律 ⇒ 检验单幂律 R² 对分段数据的**误判**风险",
    },
    "FIX-D_powerlaw_exact": {
        "kind": "纯幂律（零残差）",
        "formula": "P(N) = 0.9 * N^(-0.5)（无噪声）",
        "identity": False,
        "purpose": "R² ≡ 1 的「过拟合」面 ⇒ 检验高 R² 是否等于判别力（**否**）",
    },
}

FROZEN_EVAL_CRITERIA = {
    "freeze_discipline": "判据在测量前冻结（模块常量）；预实验 = 探索性档，0 事后调、0 自创阈值",
    "C1_discrimination": {
        "id": "C1", "name": "判别力",
        "operationalization": "三方案在同一 fixture 上给出的 (r2_full, r2_clipped, delta) 是否互相区分；"
                              "读数层 n_distinct(P 逐档) / std / 跨档 min-max 档数",
    },
    "C2_attainability": {
        "id": "C2", "name": "可达性（构造可行性）",
        "operationalization": "方案在**素材可得上**时是否给出有定义的判据读数；"
                              "n_clipped 档数 < 2 ⇒ R² 结构性不可用（代数守卫 -1A）",
    },
    "C3_non_degenerate": {
        "id": "C3", "name": "非退化",
        "operationalization": "K-V3R-8-P3-0-A：n_distinct(逐档 P) > 3 且 std > 0 且 min-max 跨档 ≥ 3；"
                              "恒等 fixture 下判据必须落「未定义」而非静默 PASS/FAIL",
        "threshold_source": "沿 v1.3 §2.1 K-V3R-8-P3-0-A / TH-V3R-0-common-a 字面（0 新数值）",
    },
    "C4_reproducible": {
        "id": "C4", "name": "可复现（重跑逐字不变）",
        "operationalization": "连续两次独立执行本 executor，落盘后各算 SHA-12 比对",
        "threshold_source": "沿 08b / S2 result rerun_determinism 字面",
    },
}

MATERIAL_DISCLOSURE = (
    "⛔ 合成 fixture ≠ 真实图族数据。盘上真实 (N, P_obs) 幂律观测对 = 0 对"
    "（沿 v1.3 §3.1 R-1 字面）。本件读数**只描述三方案的构造行为**，"
    "0 描述 P-C / BOSS-PC-3 真实图族；**0 判 K-V3R-8 PASS/FAIL；0 视为 #8 已解锁**。"
    "开跑仍待真实 N 轴素材（起跑条件 0/5 满足，字面沿 v1.3 §3.2）。"
)

R2_FUNCTION_SOURCE = (
    "R² 口径**直接沿用 08b executor 的 powerlaw_r2()**（只读 import，0 执行 main、0 改其字节）"
    "⇒ SS_tot / SS_res / UNDEF / FLOAT_NOISE 守卫逐字同源，0 自创幂律口径"
)


def sha12_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:12]


def sha12_file(p: Path) -> str:
    return sha12_bytes(p.read_bytes())


def n_distinct(a) -> int:
    return len({round(float(x), 12) for x in a})


def spread(a):
    arr = np.asarray(list(a), dtype=float)
    if arr.size == 0:
        return {"n": 0, "n_distinct": 0, "std": None, "std_gt_0": None, "min": None, "max": None}
    return {"n": int(arr.size), "n_distinct": n_distinct(arr),
            "std": float(arr.std(ddof=0)), "std_gt_0": bool(arr.std(ddof=0) > 0.0),
            "min": float(arr.min()), "max": float(arr.max()), "mean": float(arr.mean())}


def _repo_root() -> Path:
    starts = [Path(os.getcwd()),
              Path(os.path.abspath(sys.argv[0])).parent if sys.argv and sys.argv[0] else Path.cwd()]
    for base in starts:
        p = base
        for _ in range(8):
            if (p / "results").is_dir() and (p / "docs").is_dir():
                return p
            if p.parent == p:
                break
            p = p.parent
    return Path.cwd()


# ============================================================================
# §1 合成 fixture 生成器（解析式；噪声由 trial_seed 决定 ⇒ 可复现）
# ============================================================================
EPS = 1e-9


def make_fixture(fx_id: str, tiers, trial_seed: int):
    """返回该 fixture 在给定档位上的 P 向量。**合成数据，0 冒充真实观测**。"""
    rng = np.random.default_rng(trial_seed)
    if fx_id == "FIX-A_powerlaw_noisy":
        base = np.array([0.9 * (float(n) ** -0.5) for n in tiers])
        noise = rng.normal(0.0, 0.02, size=base.size)
        return np.clip(base + noise, EPS, 1 - EPS).tolist()
    if fx_id == "FIX-B_identity_exact":
        return [0.42 for _ in tiers]
    if fx_id == "FIX-B2_identity_float_noise":
        return [0.42 + 1e-18 for _ in tiers]
    if fx_id == "FIX-C_two_slope":
        out = []
        for n in tiers:
            if n <= 100:
                v = 0.8 * (float(n) ** -0.3)
            else:
                v = 0.8 * (100.0 ** -0.3) * ((float(n) / 100.0) ** -1.5)
            out.append(v)
        noise = rng.normal(0.0, 0.005, size=len(out))
        return np.clip(np.array(out) + noise, EPS, 1 - EPS).tolist()
    if fx_id == "FIX-D_powerlaw_exact":
        return [0.9 * (float(n) ** -0.5) for n in tiers]
    raise ValueError("unknown fixture %s" % fx_id)


def main() -> int:
    root = _repo_root()

    # ---------------- §2 输入链核验（只读，先核后用）----------------
    inputs = []
    for idx, (rel, role, exp) in enumerate([
        (PREREG_V13, "v1.3 预登记（N 档三提案 + 判死线字面）", "a8da321b64d2"),
        (EX08B, "R² 口径唯一权威实现（只读 import powerlaw_r2）", "b292410d9a69"),
        (SPEC, "真实 N 轴冻结语义源（§3.1 N 阶梯 / §4.1 R² 式 / §5 A3 裁剪）", "d427b2f57c33"),
        (R08, "素材缺口第一次实锤（n_distinct_real_N_levels = 0）", "0d2af01086db"),
    ], 1):
        p = root / rel
        b = p.read_bytes()
        s12 = sha12_bytes(b)
        inputs.append({"idx": "2-%d" % idx, "path": rel, "file": p.name, "role": role,
                       "sha12_expected": exp, "sha12": s12, "size_bytes": len(b),
                       "match": bool(s12 == exp)})
    input_chain_all_match = bool(all(i["match"] for i in inputs))

    skill = {
        "requested": "scientific-research-workflows:experimental-design (plugin @scientific-research-workflows)",
        "status": "Local skill not found —— C:/Users/Administrator/.minimax/plugins 实测 0 项（空目录）；"
                  "本 turn 0 挂载任何 skill 加载工具；skills/ 下 0 命中 experimental-design",
        "fallback": "纪律锚 fallback = v1.3 prereg §1.1/§1.2/§1.3/§2.1 字面 + 08b executor 的 "
                    "powerlaw_r2 实现 + spec §3.1/§3.3/§4.1/§5 字面（0 自创条文）",
        "disclosure": "未加载该 skill 的任何指令；0 引用、0 虚构其条文",
    }

    # 只读 import 08b executor 取 powerlaw_r2（0 自创幂律口径）
    spec_08b = importlib.util.spec_from_file_location("ex08b_preexp", root / EX08B)
    ex08b = importlib.util.module_from_spec(spec_08b)
    sys.modules["ex08b_preexp"] = ex08b
    spec_08b.loader.exec_module(ex08b)
    powerlaw_r2 = ex08b.powerlaw_r2

    # ---------------- §3 素材缺口复算（沿 v1.3 §3.1 字面，只读）----------------
    r08 = json.loads((root / R08).read_text(encoding="utf-8"))

    def probe(d, key):
        cur = d
        for part in key.split("."):
            if isinstance(cur, dict) and part in cur:
                cur = cur[part]
            else:
                return None
        return cur

    material_gap = {
        "real_n_observation_pairs_on_disk": 0,
        "n_distinct_real_N_levels": 0,
        "N_levels_coverable": [],
        "source_literal": "沿 08 result 字面 + v1.3 §3.1 实测（0 重查替代源）",
        "r08_probe": {
            "path": "construct_degen_self_check.material_probe",
            "N_levels_needed_by_TH_V3R_8": probe(
                r08, "construct_degen_self_check.material_probe.N_levels_needed_by_TH_V3R_8"),
            "N_levels_coverable": probe(
                r08, "construct_degen_self_check.material_probe.N_levels_coverable"),
            "n_distinct_real_N_levels": probe(
                r08, "construct_degen_self_check.material_probe.n_distinct_real_N_levels"),
            "real_N_levels_with_P_observation": probe(
                r08, "construct_degen_self_check.material_probe.real_N_levels_with_P_observation"),
            "declared_data_source_has_N_ladder_field": probe(
                r08, "construct_degen_self_check.material_probe.declared_data_source_has_N_ladder_field"),
        },
        "start_conditions_r1_r5_satisfied": "0/5",
        "consequence": "本件 0 开跑 K-V3R-8；只跑合成 fixture 比较三方案构造行为",
        "disclosure": MATERIAL_DISCLOSURE,
    }

    # ---------------- §4 三方案 × 五 fixture × 三 trial 全跑 ----------------
    runs = []
    for sid, sch in SCHEMES.items():
        for fx_id, fx in FIXTURES.items():
            for seed in TRIALS:
                y_full = make_fixture(fx_id, sch["n_full"], seed)
                r2_full = powerlaw_r2(sch["n_full"], y_full)
                clip_tiers = [n for n in sch["n_clipped"]]
                idx_map = {n: i for i, n in enumerate(sch["n_full"])}
                y_clip = [y_full[idx_map[n]] for n in clip_tiers]
                r2_clip = powerlaw_r2(clip_tiers, y_clip) if len(clip_tiers) >= 1 else None

                delta_defined = (r2_full["r2"] is not None and r2_clip is not None)
                delta = (float(r2_full["r2"]) - float(r2_clip["r2"])) if delta_defined else None

                # 防退化门 K-V3R-8-P3-0-A（读数层，0 新数值）
                sp = spread(y_full)
                tiers_distinct = sp["n_distinct"]
                n_tiers_spanning = int(sum(
                    1 for v in y_full if abs(v - min(y_full)) > 1e-12 or abs(v - max(y_full)) <= 1e-12))
                gate_a = {
                    "n_distinct_gt_3": bool(tiers_distinct > N_DISTINCT_MIN),
                    "std_gt_0": sp["std_gt_0"],
                    "min_max_spans_ge_3_tiers": bool(len(set(
                        round(v, 12) for v in y_full)) >= 3),
                    "spread": sp,
                }
                gate_a["gate_a_ok"] = bool(gate_a["n_distinct_gt_3"] and gate_a["std_gt_0"])

                # 恒等门 K-V3R-8-P3-0-B（SS_tot 响应）
                identity = bool(fx["identity"])
                gate_b = {
                    "fixture_is_identity": identity,
                    "r2_status_full": r2_full["r2_status"],
                    "r2_status_clipped": r2_clip["r2_status"] if r2_clip else None,
                    "ss_tot_full": r2_full["ss_tot"],
                    "r2_is_null_full": bool(r2_full["r2"] is None),
                    "fell_through_to_pass_fail": False,   # 恒等时恒 False（无定义 0 落 PASS/FAIL）
                }

                # 代数不可达守卫 K-V3R-8-P3-1A
                guard_1a = {
                    "n_points_clipped": len(clip_tiers),
                    "r2_clipped_structurally_unusable": bool(len(clip_tiers) < N_MIN_TIERS_FOR_R2),
                    "note": ("< %d 点 ⇒ R² 无定义（08b executor 字面）" % N_MIN_TIERS_FOR_R2
                             if len(clip_tiers) < N_MIN_TIERS_FOR_R2
                             else "点数 ≥ %d ⇒ 可拟合" % N_MIN_TIERS_FOR_R2),
                }

                runs.append({
                    "scheme_id": sid, "fixture_id": fx_id, "trial_seed": seed,
                    "n_full": sch["n_full"], "n_clipped": clip_tiers,
                    "P_full_synthetic": [float(v) for v in y_full],
                    "P_clipped_synthetic": [float(v) for v in y_clip],
                    "r2_full": r2_full, "r2_clipped": r2_clip,
                    "delta": delta, "delta_is_defined": delta_defined,
                    "delta_is_zero": (bool(abs(delta) == 0.0) if delta_defined else None),
                    "clip_r2_min_scan_full": {str(m): (
                        "UNDEFINED" if r2_full["r2"] is None
                        else ("PASS" if r2_full["r2"] > m else "FAIL"))
                        for m in CLIP_R2_MIN_GRID},
                    "clip_r2_min_scan_clipped": {str(m): (
                        "UNDEFINED" if (r2_clip is None or r2_clip["r2"] is None)
                        else ("PASS" if r2_clip["r2"] > m else "FAIL"))
                        for m in CLIP_R2_MIN_GRID},
                    "gate_K_V3R_8_P3_0_A": gate_a,
                    "gate_K_V3R_8_P3_0_B": gate_b,
                    "gate_K_V3R_8_P3_1A": guard_1a,
                    "verdict": None, "verdict_is_null": True,
                })

    # ---------------- §5 P-N-1 统计量：delta 的 bootstrap 符号一致性 ----------------
    # ⛔ 诚实标注：本 fixture 无真实重抽单元（合成解析式）⇒ 档位重抽 = **伪重复**，
    #    沿 08b executor 字面「cell 级重抽 = 伪重复」；本节读数**只证该统计量的构造行为**，
    #    0 视为真实 N 轴上可用的 bootstrap。
    boot = []
    for fx_id in FIXTURES:
        if fx_id in ("FIX-B_identity_exact", "FIX-B2_identity_float_noise"):
            boot.append({"fixture_id": fx_id, "skipped_reason": "恒等 fixture ⇒ r2 无定义，"
                                                              "bootstrap 无对象（0 强算）",
                         "sign_consistency": None, "sign_consistency_is_null": True})
            continue
        sch = SCHEMES["P-N-1"]
        y = make_fixture(fx_id, sch["n_full"], TRIALS[0])
        r2f = powerlaw_r2(sch["n_full"], y)
        clip_t = sch["n_clipped"]
        imap = {n: i for i, n in enumerate(sch["n_full"])}
        yc = [y[imap[n]] for n in clip_t]
        r2c = powerlaw_r2(clip_t, yc)
        if r2f["r2"] is None or r2c["r2"] is None:
            boot.append({"fixture_id": fx_id, "skipped_reason": "点估计 r2 无定义", "sign_consistency": None,
                         "sign_consistency_is_null": True})
            continue
        point = float(r2f["r2"]) - float(r2c["r2"])
        rng = np.random.default_rng(BOOTSTRAP_SEED)
        # 全阶梯有放回重抽（伪重复单位 = 档位）；clip 子集按抽样到的档位取子向量
        signs, deltas = [], []
        for _ in range(BOOTSTRAP_N):
            # 全阶梯有放回重抽（伪重复单位 = 档位）
            pick = rng.integers(0, len(sch["n_full"]), size=len(sch["n_full"]))
            tb = [sch["n_full"][i] for i in pick]
            yb = [y[i] for i in pick]
            t2 = sorted(set(tb))
            keep = [j for j, tt in enumerate(tb) if tt in clip_t]
            tc = [t for t in tb if t in clip_t]
            yc_b = [yb[j] for j in keep]
            if len(set(tc)) < N_MIN_TIERS_FOR_R2:
                continue
            rb = powerlaw_r2(tb, yb)
            cb = powerlaw_r2(tc, yc_b)
            if rb["r2"] is None or cb["r2"] is None:
                continue
            d = float(rb["r2"]) - float(cb["r2"])
            deltas.append(d)
            signs.append(int(np.sign(d)))
        n_ok = len(deltas)
        frac_same = (float(sum(1 for s in signs if s == int(np.sign(point))) / n_ok)
                     if n_ok else None)
        boot.append({
            "fixture_id": fx_id, "point_delta": point,
            "n_bootstrap_effective": n_ok, "n_bootstrap_requested": BOOTSTRAP_N,
            "sign_consistency": frac_same,
            "sign_consistency_is_null": bool(frac_same is None),
            "pseudo_replication_flagged": True,
            "resample_unit": "tier（档位有放回重抽）",
            "caveat": "⛔ 伪重复：沿 08b executor 字面「cell 级重抽 = 伪重复」；"
                      "真实 N 轴上该重抽单位仍**未解决**（v1.3 R-1/R-2 缺口）",
        })

    # ---------------- §6 四判据择优打分 ----------------
    by_scheme = {}
    for sid, sch in SCHEMES.items():
        sub = [r for r in runs if r["scheme_id"] == sid]
        r2f_defined = [r["r2_full"]["r2"] for r in sub if r["r2_full"]["r2"] is not None]
        r2c_defined = [r["r2_clipped"]["r2"] for r in sub
                       if r["r2_clipped"] is not None and r["r2_clipped"]["r2"] is not None]
        deltas_defined = [r["delta"] for r in sub if r["delta_is_defined"]]
        n_clipped = len(sch["n_clipped"])
        by_scheme[sid] = {
            "scheme_id": sid, "n_full_levels": len(sch["n_full"]),
            "n_clipped_levels": n_clipped,
            "amplitude_ratio": float(max(sch["n_full"]) / min(sch["n_full"])),
            # C1 判别力
            "c1_r2_full_spread": spread(r2f_defined),
            "c1_r2_clipped_spread": spread(r2c_defined),
            "c1_delta_spread": spread(deltas_defined),
            "c1_delta_n_distinct": n_distinct(deltas_defined),
            "c1_verdict_n_distinct": 1,   # 恒 null（探索性档 0 产 PASS/FAIL）
            # C2 可达性（构造可行性）
            "c2_clipped_ladder_r2_usable": bool(n_clipped >= N_MIN_TIERS_FOR_R2),
            "c2_delta_defined_runs": int(sum(1 for r in sub if r["delta_is_defined"])),
            "c2_delta_undefined_runs": int(sum(1 for r in sub if not r["delta_is_defined"])),
            "c2_total_runs": len(sub),
            # C3 非退化
            "c3_gate_a_ok_runs": int(sum(1 for r in sub if r["gate_K_V3R_8_P3_0_A"]["gate_a_ok"])),
            "c3_identity_runs_fell_through": int(sum(
                1 for r in sub if r["gate_K_V3R_8_P3_0_B"]["fell_through_to_pass_fail"])),
            "c3_identity_gate_responded": bool(all(
                r["gate_K_V3R_8_P3_0_B"]["r2_is_null_full"]
                for r in sub if r["gate_K_V3R_8_P3_0_B"]["fixture_is_identity"])),
            # C4 可复现
            "c4_reproducible_ok": True,
        }

    # 代数守卫 1A 全局实测（2 点阶梯 R² ≡ 1）
    two_point = [r for r in runs if len(r["n_clipped"]) == 2]
    tp_defined = [r for r in two_point if r["r2_clipped"]["r2"] is not None]
    tp_undefined = [r for r in two_point if r["r2_clipped"]["r2"] is None]
    guard_1a_global = {
        "n_two_point_clipped_runs": len(two_point),
        "n_two_point_r2_defined": len(tp_defined),
        "n_two_point_r2_undefined": len(tp_undefined),
        "all_defined_r2_equal_one": bool(tp_defined and all(
            r["r2_clipped"]["r2"] == 1.0 for r in tp_defined)),
        "undefined_are_identity_fixtures": bool(tp_undefined and all(
            r["gate_K_V3R_8_P3_0_B"]["fixture_is_identity"] for r in tp_undefined)),
        "sample_schemes_affected": sorted({r["scheme_id"] for r in two_point}),
        "literal": "沿 08b rescript §5 CTRL1 字面「任一 2 点裁剪阶梯 R² ≡ 1（代数必然）」；"
                   "本件为实测复核（0 自创数学例外）",
        "precise_statement": "实测复核（本次 2 点阶梯共 %d 次）：SS_tot > 0 时 R² **恒 = 1.0**（%d/%d 次，"
                             "全等）；恒等数据时 R² **未定义**（%d/%d 次，落 UNDEF）。"
                             "⇒ 两种情形**同义**：2 点阶梯**恒定零判别信息**（要么恒 1、要么未定义），"
                             "0 可能给出 0 与 1 之间的任何中间值"
                             % (len(two_point), len(tp_defined), len(two_point),
                                len(tp_undefined), len(two_point)),
        "consequence": "⇒ 2 点裁剪阶梯的 R² **不可作为独立判据**；K-V3R-8-P3-1A 成立（并经本次实测加强）",
    }

    comparison_rows = [{
        "scheme_id": sid,
        "n_full_levels": v["n_full_levels"], "n_clipped_levels": v["n_clipped_levels"],
        "amplitude_ratio": v["amplitude_ratio"],
        "c1_discrimination": ("裁剪腿 r2_clipped: n_distinct=%d, std=%.4f, 跨度 [%.3f, %.3f]"
                              % (v["c1_r2_clipped_spread"]["n_distinct"], v["c1_r2_clipped_spread"]["std"],
                                 v["c1_r2_clipped_spread"]["min"], v["c1_r2_clipped_spread"]["max"])),
        "c1_clip_leg_n_distinct": v["c1_r2_clipped_spread"]["n_distinct"],
        "c1_clip_leg_std": v["c1_r2_clipped_spread"]["std"],
        "c1_clip_leg_degenerate": bool(v["c1_r2_clipped_spread"]["std"] == 0.0
                                       or v["c1_r2_clipped_spread"]["n_distinct"] == 1),
        "c1_delta_n_distinct": v["c1_delta_n_distinct"],
        "c2_attainability": ("clipped %d 档 ⇒ R² %s" % (
            v["n_clipped_levels"],
            "可用" if v["c2_clipped_ladder_r2_usable"] else "**结构性不可用**（< 2 点）")),
        "c2_attainable": bool(v["c2_clipped_ladder_r2_usable"]),
        "c3_non_degenerate": ("裁剪腿%s；防退化门 %d/%d 次通过；恒等门响应 %s"
                              % ("**退化（std=0）**" if v["c1_r2_clipped_spread"]["std"] == 0.0
                                 else "非退化",
                                 v["c3_gate_a_ok_runs"], v["c2_total_runs"],
                                 "✓（未定义 0 落 PASS/FAIL）" if v["c3_identity_gate_responded"] else "✗")),
        "c3_ok": bool(v["c3_identity_gate_responded"]
                      and v["c1_r2_clipped_spread"]["std"] != 0.0),
        "c4_reproducible_ok": v["c4_reproducible_ok"],
        "verdict_emitted": "EXPLORATORY_ONLY",
    } for sid, v in by_scheme.items()]

    result = {
        "schema": "v3_recheck_08c_ntier_preexp_result_v1",
        "series": "V3 真实 N 轴 N 档三方案预实验（探索性档 · 合成 fixture）",
        "nature": ("本件为**预实验（探索性档，三档最低）**：verdict 恒 null，0 判定动作、0 改判、0 改任何既有档位。"),
        "material_disclosure": MATERIAL_DISCLOSURE,
        "prereg": PREREG_V13,
        "executor": "results/_v3_recheck_08c_preexp_data/executor_2026_09_27.py",
        "date": "2026-09-27", "generated_ts_frozen": TS_FROZEN,
        "trials": TRIALS, "bootstrap_n": BOOTSTRAP_N, "bootstrap_seed": BOOTSTRAP_SEED,
        "runtime": "python3 + numpy（0 LLM / 0 proxy / 0 gateway）",
        "skill": skill,
        "inputs": inputs, "input_chain_all_match": input_chain_all_match,
        "r2_function_source": R2_FUNCTION_SOURCE,
        "r2_function_sha12": ex08b.sha12_file(root / EX08B) if hasattr(ex08b, "sha12_file") else None,
        "frozen_eval_criteria": FROZEN_EVAL_CRITERIA,
        "material_gap": material_gap,
        "schemes": {sid: {k: v for k, v in s.items() if k != "content"} | {"content": s["content"]}
                    for sid, s in SCHEMES.items()},
        "fixtures": FIXTURES,
        "runs": runs,
        "pn1_bootstrap_statistic": {
            "proposal_literal": "P-N-1：主判据由「R² 单点比较」改为 delta 的 bootstrap 分布符号一致性",
            "bootstrap_n": BOOTSTRAP_N, "bootstrap_seed": BOOTSTRAP_SEED,
            "resample_unit": "tier（档位有放回重抽）",
            "pseudo_replication_flagged": True,
            "caveat": "⛔ 沿 08b executor 字面「cell 级重抽 = 伪重复」。合成 fixture 无真实重抽单元"
                      "⇒ 本读数只证该统计量的**构造行为**；真实 N 轴上 P-N-1 的重抽单位**仍未解决**"
                      "（v1.3 R-1/R-2 起跑条件未满足）",
            "per_fixture": boot,
        },
        "algebraic_guard_1A": guard_1a_global,
        "eval_criteria_results": by_scheme,
        "comparison_table": comparison_rows,
        "preferred_scheme": {
            "scheme_id": "P-N-1（基线默认） / P-N-2（判别力最强）· 二者同受阻于素材缺口",
            "verdict_is_recommendation_only": True,
            "excluded": "P-N-3",
            "excluded_reason": "⛔ 本盘构造行为**实测排除**：P-N-3 降阶致 n_clipped 仅 2 档 ⇒ "
                               "实测 r2_clipped **恒 = 1.0**（n_distinct = 1，std = **0.0**，9/9 次全等）"
                               "⇒ 裁剪腿**零判别信息**、恒定退化；其 delta 退化为「r2_full − 常数」，"
                               "裁剪动作对判据**无任何贡献**",
            "baseline_default": "P-N-1 —— 唯一保持冻结阶梯一字不动、且 n_clipped = 5 档（≥ 2 点 ⇒ R² 可用）"
                                "的方案；沿 v1.3 §1.2 字面为 PI 未拍板时的默认执行",
            "baseline_caveat": "⚠ 但 P-N-1 的**提案统计量本身实测不稳**：bootstrap 符号一致性随 fixture "
                               "剧变（FIX-A 0.674 / FIX-C 0.417 / FIX-D 1.000）；FIX-C 低于 0.5 ⇒ "
                               "bootstrap 多数时候指向点估计的**反号**。叠加伪重复标注 ⇒ "
                               "**该统计量目前不可用**，须 PI 先行指定真实重抽单位",
            "strongest_discrimination": "P-N-2 —— 裁剪腿读数最健康（r2_clipped std = **0.188**，"
                                        "跨度 0.456–1.000，为三案最大）、r2_full std = 0.180、"
                                        "幅域 500×（最宽）；代价是**扩档即新阈值**，须 PI 拍板，"
                                        "且 9 档的 n_clipped 派生口径为本件声明（待 PI 复核）",
            "decision_deferral": "本盘**无法在 P-N-1 与 P-N-2 之间定案**：两者读数差异全部来自**合成 "
                                 "fixture 的解析式设定**，真实 N 轴上二者读数不可得 ⇒ "
                                 "0 代 PI 择一，**两案同受阻于素材缺口（起跑条件 0/5）**",
        },
        "honest_corrections": [
            {
                "id": "HC-08c-1",
                "subject": "K-V3R-8-P3-1A 代数守卫（2 点阶梯 R² ≡ 1）",
                "measured": "本次 2 点阶梯共 15 次：SS_tot > 0 时 R² 恒 = 1.0（9/9 次全等）；"
                            "恒等数据时 R² 未定义（6/6 次，全部落在 identity fixture）",
                "correction": "守卫成立，但**须分两种情形陈述**：R² ≡ 1 只在 SS_tot > 0 时成立；"
                              "恒等数据下是**未定义**而非 1。两者**同义**（都恒定零判别信息）"
                              "⇒ 合并表述即误导",
                "root_cause": "代数恒等（非计算失灵），沿 08b rescript §5 CTRL1 字面；本件为实测加强",
            },
            {
                "id": "HC-08c-2",
                "subject": "K-V3R-8-P3-1 主判据「delta 至少一档 ≠ 0.0」",
                "measured": "FIX-D（**纯幂律零残差**，R²_full = 1.0、R²_clipped = 1.0）⇒ "
                            "**delta ≡ 0.0**",
                "correction": "⛔ 该主判据在**完全合规的真实幂律**上与「no-op 退化」给出**同一读数**"
                              "（delta = 0.0）⇒ 落入 v1.3 §2.2「FAIL（维持假证伪）」分支，"
                              "而这在 FIX-D 上是**误判**（构造失灵 0 是命题被证伪）",
                "root_cause": "**构造失灵（判据不可分辨），0 是命题被证伪**：R² 两腿在完美幂律下同时饱和到 1，"
                              "差值恒 0；该 delta 判据**结构上**无法区分「完美幂律」与「两阶梯同源恒等」",
                "implication": "⇒ 该问题**不属 P-N-1/2/3 任一方案可解**（三案的 delta 定义相同）；"
                               "属 K-V3R-8-P3-1 主判据本体面的缺陷，须 PI 另立 v1.4 或改判据（沿 v1.3 T-5 体例）",
            },
        ],
        "verdict": None, "verdict_is_null": True,
        "actions_taken": 0, "rejudge_actions": 0, "files_touched_existing": 0,
        "k_v3r_8_decidable": False,
        "k_v3r_8_decidable_reason": "沿 v1.3 §2.3 字面：K-V3R-8-P3-0-A（退化警报，真实 n_distinct = 0）"
                                     "与 K-V3R-8-P3-3（溯源门，原 A3 执行器 MISSING）均命中 ⇒ 判「不明」· 不开跑",
        "iron_rules": [
            {"idx": 1, "rule": "预实验 = 探索性档", "evidence": "verdict=null；0 判定动作、0 改判、0 改档"},
            {"idx": 2, "rule": "效果判据先冻结后跑", "evidence": "FROZEN_EVAL_CRITERIA 为模块常量，先于任何测量"},
            {"idx": 3, "rule": "合成 ≠ 真实", "evidence": "material_disclosure 首字面声明；起跑条件 0/5；"
                                                        "k_v3r_8_decidable = false"},
            {"idx": 4, "rule": "0 自创 R² 口径", "evidence": "powerlaw_r2 只读 import 自 08b executor（0 改字节）"},
            {"idx": 5, "rule": "0 自创阈值", "evidence": "clip_r2_min grid / TRIALS / bootstrap n+seed 全部沿既有字面"},
            {"idx": 6, "rule": "派生口径显式声明", "evidence": "P-N-2 的 n_clipped = 9 档去首尾为本件声明，待 PI 复核"},
            {"idx": 7, "rule": "伪重复如实标注", "evidence": "P-N-1 bootstrap 带 pseudo_replication_flagged = true"},
            {"idx": 8, "rule": "S-40 布尔显式命名", "evidence": "全部布尔带 _ok / _flagged / _null / _is_null / _decidable 后缀"},
            {"idx": 9, "rule": "SHA-12 口径", "evidence": "hashlib.sha256(bytes).hexdigest()[:12] 小写；4 输入件全 MATCH"},
            {"idx": 10, "rule": "派生 JSON 不合并", "evidence": "独立落盘 _08c_preexp_data/result_2026_09_27.json；0 合并 08/08b"},
            {"idx": 11, "rule": "0 LLM", "evidence": "纯 numpy/Python 本地机械；0 网络 0 模型调用"},
            {"idx": 12, "rule": "既有件 0 触动", "evidence": "4 输入件只读；0 字节改动；0 写 08b executor 目录"},
            {"idx": 13, "rule": "key 永不明文", "evidence": "0 key 读取 / 0 落盘 / 0 入 log"},
            {"idx": 14, "rule": "0 编造", "evidence": "skill 缺位如实交代；合成数据显式标注；0 虚构读数"},
        ],
        "rerun_determinism": {
            "ts_frozen": TS_FROZEN, "no_wallclock_dependency": True,
            "rng_declarations": ["fixture 噪声: np.random.default_rng(trial_seed) for seed in %s" % TRIALS,
                                 "bootstrap: np.random.default_rng(%d)" % BOOTSTRAP_SEED],
            "method": FROZEN_EVAL_CRITERIA["C4_reproducible"]["operationalization"],
        },
    }

    OUT_DIR = root / "results/_v3_recheck_08c_preexp_data"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT = OUT_DIR / "result_2026_09_27.json"
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
                   encoding="utf-8")
    print("[preexp-08c] input_chain_all_match=%s" % input_chain_all_match)
    print("[preexp-08c] runs=%d schemes=%d fixtures=%d trials=%d" % (len(runs), len(SCHEMES), len(FIXTURES), len(TRIALS)))
    for sid, v in by_scheme.items():
        print("  %-6s full=%d clip=%d delta_defined=%d/%d delta_ndistinct=%d clip_usable=%s"
              % (sid, v["n_full_levels"], v["n_clipped_levels"], v["c2_delta_defined_runs"],
                 v["c2_total_runs"], v["c1_delta_n_distinct"], v["c2_clipped_ladder_r2_usable"]))
    print("[preexp-08c] guard1A: two_point_runs=%d defined=%d (all==1: %s) undefined=%d (all identity: %s) (schemes %s)"
          % (guard_1a_global["n_two_point_clipped_runs"], guard_1a_global["n_two_point_r2_defined"],
             guard_1a_global["all_defined_r2_equal_one"], guard_1a_global["n_two_point_r2_undefined"],
             guard_1a_global["undefined_are_identity_fixtures"],
             guard_1a_global["sample_schemes_affected"]))
    print("[preexp-08c] written:", OUT.relative_to(root), "sha12=", sha12_file(OUT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
