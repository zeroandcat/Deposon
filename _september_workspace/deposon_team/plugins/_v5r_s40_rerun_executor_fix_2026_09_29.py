"""V5 清卷 M-R3 ｜ S-40 kill-line 双因修复版重算 executor（新名件 · 2026-09-29）。

任务
----
deposon V4 清卷·轮 11 裁项 M-R3 ＝ A「采纳补正建议行＋汇入勘误链」：
按 `results/_v4_s40_semantics_verdict_2026_09_23.md`（SHA-12 0d6b3c74dc98）L153/L155
两条修复建议修执行棒，**0 回改既有 executor**，**0 回改升格件 c398cf82b3ea 一字**，
S-40 按**预登记字面**复算。

双因（照录 065e57820c36 / 0d6b3c74dc98）
----------------------------------------
致命 1：源执行棒 L833 `failed` 公式新增**非预登记条款 `range_val > 1.0`**（单独驱动翻转）
致命 2：源执行棒 L837 `kill_lines` 字典**丢弃 pass 命名 wrapper**，
        致「True = hit」与预登记字面「CV >= 0.50 即 FAIL」**方向相反**

本件行为边界
------------
- **0 回改既有件**：源执行棒 `_v4_rerun_executor_2026_09_23.py`、升格件、预登记、
  语义复核件、勘误建议件**全部只读**（跨仓外 `D:/私人资料/_non_upload_local_archive/`）。
- **0 触预登记字面**：`TH_TAU_CV = 0.50` 与 K-S40-1/2/3 三条判死线**一字不动**。
  本件修的是**实现**（failed 公式里多出来的非预登记子句 ＋ 命名方向），
  **不是判死线**（沿「判死线先于实验」）。
- **0 LLM / 0 API / 0 proxy / 0 gateway**：纯本地 `random.Random(seed=42)` 复算。
- **0 预判结论**：读数照实落盘；verdict 由公式算出，不写死。
- **禁内建 `hash()`**：用 hashlib.sha256（沿源执行棒同款约定）。
- 读数照实、0 编造；若复算结果与「应判 PASS」不符，本件照实落盘并由注记件如实报告。

复算路径
--------
本件对 `run_S40()` 的数值路径做**逐行等价复刻**（rng 序列 / 公式 / bootstrap 均同源），
并提供 `--cross-check` 开关：把源执行棒以 **只读** 方式 import 进来、调用其 `run_S40()`，
与本件复刻结果逐字段比对，输出 `equivalent: true/false` 作为等价性证据。

Usage
-----
    python _v5r_s40_rerun_executor_fix_2026_09_29.py            # 复算 + 落盘
    python _v5r_s40_rerun_executor_fix_2026_09_29.py --cross-check   # 追加只读等价性核对

出件
----
    results/_v5r_s40_recompute_2026_09_29.json   （新名结果件）

Author: Mavis worker（delegated sub-task 2026-09-29, M-R3 裁 A）
"""
from __future__ import annotations

import hashlib
import json
import math
import random
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

# ============================================================
# 路径（绝对，不依赖 cwd）
# ============================================================
REPO_ROOT = Path("D:/私人资料/deposon-repo")
SURFACE_DIR = REPO_ROOT / "corpus" / "v20_caption_surface"
RESULTS_DIR = REPO_ROOT / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

CAPTIONS_PATH = SURFACE_DIR / "strip_captions_22.json"

# 源执行棒（**只读**，本件 0 回改）
SRC_EXECUTOR = Path(
    "D:/私人资料/_non_upload_local_archive/results/_v4_rerun_executor_2026_09_23.py"
)

# ============================================================
# 常量 —— 逐字沿用源执行棒 L46 / L55；**阈值 0.50 一字不动**（0 擅调阈值）
# ============================================================
SEED = 42            # 源 L46
TH_TAU_CV = 0.50     # 源 L55（K-τ-1）—— 预登记字面「CV >= 0.50 即 FAIL」

# 预登记出处（只读引用，不改）
PREREG_FILE = "_v4_seeds_prereg_supplement_2026_09_23.md"
PREREG_SHA12 = "113cbe555643"
PREREG_LINES = "L367 (K-S40-1) / L368 (K-S40-2) / L369 (K-S40-3) / L510 (S-40 汇总行)"


# ============================================================
# 纯函数 —— 逐字复刻自源执行棒 L294-L297 / L314-L326
# ============================================================
def mean(xs: List[float]) -> float:
    if not xs:
        return 0.0
    return sum(xs) / len(xs)


def bootstrap_ci(
    xs: List[float], n_boot: int = 1000, alpha: float = 0.05, seed: int = SEED
) -> Tuple[float, float]:
    if not xs:
        return (0.0, 0.0)
    rng = random.Random(seed)
    n = len(xs)
    boots = []
    for _ in range(n_boot):
        s = sum(rng.choice(xs) for _ in range(n))
        boots.append(s / n)
    boots.sort()
    lo = boots[int(n_boot * alpha / 2)]
    hi = boots[int(n_boot * (1 - alpha / 2))]
    return (lo, hi)


def sha12_hex(data: bytes) -> str:
    """SHA-12 口径 = hashlib.sha256(字节).hexdigest()[:12]，小写。"""
    return hashlib.sha256(data).hexdigest()[:12]


def file_sha12(path: Path) -> Tuple[str, int]:
    data = path.read_bytes()
    return sha12_hex(data), len(data)


# ============================================================
# S-40 数值路径 —— 逐行复刻源执行棒 L812-L832
# ============================================================
def load_cap_texts() -> List[str]:
    caps = json.loads(CAPTIONS_PATH.read_text(encoding="utf-8"))
    return [c["text"] for c in caps]


def compute_s40_metrics(cap_texts: List[str]) -> Dict[str, Any]:
    """返回 S-40 全部观测量（全精度，不四舍五入）。

    逐行对应源执行棒 L814-L832；**rng 序列 / 公式 / bootstrap 调用一字不改**。
    """
    rng = random.Random(SEED + 47)
    cvs: List[float] = []
    for _ in range(min(100, len(cap_texts) * 5)):  # 源 L819
        v2 = rng.uniform(8, 12)
        v3 = rng.uniform(7.5, 12.5)
        d7 = rng.uniform(9, 11)
        m = (v2 + v3 + d7) / 3
        s = math.sqrt(((v2 - m) ** 2 + (v3 - m) ** 2 + (d7 - m) ** 2) / 2)
        c = s / abs(m) if m != 0 else 0.0
        cvs.append(c)
    cv_val = mean(cvs)
    ci = bootstrap_ci(cvs, n_boot=500)
    range_val = (max(cvs) - min(cvs)) / max(mean(cvs), 1e-9)
    rng2 = random.Random(SEED + 53)
    cvs_shuf = list(cvs)
    rng2.shuffle(cvs_shuf)
    cv_shuf = mean(cvs_shuf)
    return {
        "cvs": cvs,
        "cv_val": cv_val,
        "ci": ci,
        "range_val": range_val,
        "cv_shuf": cv_shuf,
        "n_cells": len(cvs),
    }


# ============================================================
# 修复点 ①（L833）：删非预登记子句
# ============================================================
def failed_prereg_only(m: Dict[str, Any]) -> bool:
    """**修复后** failed 公式 —— 只含预登记 K-S40-1/2/3 三项。

    源执行棒改前 L833 为：
        failed = cv_val >= TH_TAU_CV or ci[1] >= TH_TAU_CV
                 or range_val > 1.0                      # ← 非预登记条款（致命 1）
                 or (cv_shuf >= TH_TAU_CV and cv_val <= cv_shuf)
    本件（0 触预登记字面）改为：
        failed = cv_val >= TH_TAU_CV or ci[1] >= TH_TAU_CV
                 or (cv_shuf >= TH_TAU_CV and cv_val <= cv_shuf)
    """
    cv_val, ci, cv_shuf = m["cv_val"], m["ci"], m["cv_shuf"]
    return (
        cv_val >= TH_TAU_CV
        or ci[1] >= TH_TAU_CV
        or (cv_shuf >= TH_TAU_CV and cv_val <= cv_shuf)
    )


def failed_with_unprereg_clause(m: Dict[str, Any]) -> bool:
    """**改前** failed 公式（仅作对照留痕，**不驱动 verdict**）。

    保留 `or range_val > 1.0` 供根因核对；按 0d6b3c74dc98 L153 建议，
    该子句在修复版里已从判死面**迁出为独立构造警告**（见 `construction_warning`）。
    """
    cv_val, ci, cv_shuf = m["cv_val"], m["ci"], m["cv_shuf"]
    return (
        cv_val >= TH_TAU_CV
        or ci[1] >= TH_TAU_CV
        or m["range_val"] > 1.0
        or (cv_shuf >= TH_TAU_CV and cv_val <= cv_shuf)
    )


# ============================================================
# 修复点 ②（L837）：恢复 pass 命名 wrapper / 修正方向
# ============================================================
def kill_lines_fixed(m: Dict[str, Any]) -> Dict[str, Any]:
    """**修复后** kill_lines —— 逐字对应 0d6b3c74dc98 L157-L163 建议块。

    命名方向：`pass = True` 表示 **kill-line 未触发 = claim 存活**，
    与预登记字面「CV >= 0.50 即 FAIL」**同向**（源执行棒改前丢 wrapper，
    存 raw bool `cv_val < TH_TAU_CV`，若按「True = hit」读则方向相反 —— 致命 2）。
    """
    cv_val, ci, cv_shuf = m["cv_val"], m["ci"], m["cv_shuf"]
    return {
        "K-S40-1": {
            "threshold_desc": "CV>=0.50即FAIL",
            "prereg_src": f"{PREREG_FILE} {PREREG_LINES}",
            "observed": round(cv_val, 4),
            "pass": bool(cv_val < TH_TAU_CV),
        },
        "K-S40-2": {
            "threshold_desc": "CI95%上界>=0.50即FAIL",
            "prereg_src": f"{PREREG_FILE} {PREREG_LINES}",
            "observed_ci_hi": round(ci[1], 4),
            "pass": bool(ci[1] < TH_TAU_CV),
        },
        "K-S40-3": {
            "threshold_desc": "CV_shuffle>=0.50且CV_proxy<=CV_shuffle即FAIL",
            "prereg_src": f"{PREREG_FILE} {PREREG_LINES}",
            "observed": [round(cv_val, 4), round(cv_shuf, 4)],
            "pass": bool(not (cv_shuf >= TH_TAU_CV and cv_val <= cv_shuf)),
        },
    }


def kill_lines_prefix_raw(m: Dict[str, Any]) -> Dict[str, Any]:
    """**改前** kill_lines（仅作对照留痕，**不驱动 verdict**）—— 源执行棒改前 L837。

    丢 wrapper 的 raw bool 形态：方向歧义，消费方须重新解析。
    """
    cv_val, ci, cv_shuf = m["cv_val"], m["ci"], m["cv_shuf"]
    return {
        "K-S40-1": bool(cv_val < TH_TAU_CV),
        "K-S40-2": bool(ci[1] < TH_TAU_CV),
        "K-S40-3": bool(not (cv_shuf >= TH_TAU_CV and cv_val <= cv_shuf)),
    }


# ============================================================
# 主复算
# ============================================================
def recompute() -> Dict[str, Any]:
    cap_texts = load_cap_texts()
    m = compute_s40_metrics(cap_texts)

    kl = kill_lines_fixed(m)
    failed = failed_prereg_only(m)
    hit = {k: (not v["pass"]) for k, v in kl.items()}

    src_sha12, src_bytes = ("—", 0)
    if SRC_EXECUTOR.exists():
        src_sha12, src_bytes = file_sha12(SRC_EXECUTOR)

    return {
        "schema": "v5r_s40_recompute/1.0",
        "id": "S-40",
        "label": "长期漂移",
        "recompute_at": "2026-09-29",
        "recompute_by": "Mavis worker（delegated sub-task 2026-09-29, M-R3 裁 A）",
        "verdict_basis": "按预登记字面 K-S40-1/2/3 三项复算（0 触预登记字面）",
        "prereg": {
            "file": PREREG_FILE,
            "sha12": PREREG_SHA12,
            "lines": PREREG_LINES,
            "threshold_used": TH_TAU_CV,
            "threshold_touched": False,
        },
        "fix_inputs": {
            "verifier_verdict_file": "_v4_s40_semantics_verdict_2026_09_23.md",
            "verifier_verdict_sha12": "0d6b3c74dc98",
            "correction_note_file": "_v4_s40_correction_note_2026_09_23.md",
            "correction_note_sha12": "065e57820c36",
            "upgrade_review_sha12_untouched": "c398cf82b3ea",
        },
        "source_executor_readonly": {
            "path": str(SRC_EXECUTOR),
            "sha12": src_sha12,
            "bytes": src_bytes,
            "modified_by_this_task": False,
        },
        "inputs": {
            "captions_file": str(CAPTIONS_PATH),
            "n_captions": len(cap_texts),
            "n_cells_subsample_cap": min(100, len(cap_texts) * 5),
            "seed": SEED,
        },
        "metrics_full_precision": {
            "cv_val": round(m["cv_val"], 6),
            "ci_lo": round(m["ci"][0], 6),
            "ci_hi": round(m["ci"][1], 6),
            "range_val": round(m["range_val"], 6),
            "cv_shuf": round(m["cv_shuf"], 6),
            "min_cvs": round(min(m["cvs"]), 6),
            "max_cvs": round(max(m["cvs"]), 6),
            "n_cells": m["n_cells"],
        },
        "metrics_rounded_4": {
            "cv_val": round(m["cv_val"], 4),
            "ci_95": [round(m["ci"][0], 4), round(m["ci"][1], 4)],
            "max_min_range": round(m["range_val"], 4),
            "negctrl_cv": round(m["cv_shuf"], 4),
        },
        "kill_lines_postfix": kl,
        "kill_line_hits": hit,
        "all_three_false": all(v is False for v in hit.values()),
        "verdict": "FAIL" if failed else "PASS",
        "root_cause": "工具或构造层面失灵" if failed else "命题层面成立",
        "failed_formula_postfix": (
            "failed = cv_val >= TH_TAU_CV or ci[1] >= TH_TAU_CV "
            "or (cv_shuf >= TH_TAU_CV and cv_val <= cv_shuf)"
        ),
        "construction_warning_not_a_killline": {
            "expr": "range_val > 1.0",
            "value": round(m["range_val"], 6),
            "triggered": bool(m["range_val"] > 1.0),
            "note": (
                "非预登记条款，已按 0d6b3c74dc98 L153 从判死面迁出为独立构造警告；"
                "**不参与 verdict**"
            ),
        },
        "counterfactual_prefix_documented_only": {
            "failed_formula_prefix": (
                "failed = cv_val >= TH_TAU_CV or ci[1] >= TH_TAU_CV "
                "or range_val > 1.0 or (cv_shuf >= TH_TAU_CV and cv_val <= cv_shuf)"
            ),
            "failed_prefix": failed_with_unprereg_clause(m),
            "verdict_prefix": "FAIL" if failed_with_unprereg_clause(m) else "PASS",
            "kill_lines_prefix_raw_bool": kill_lines_prefix_raw(m),
            "note": "改前形态仅作双因对照留痕，**不驱动本件 verdict**；0 预判",
        },
        "dual_factor_rootcause": {
            "fatal_1_l833": (
                "源执行棒 L833 failed 公式新增非预登记条款 `range_val > 1.0`；"
                "本次实测 range_val="
                f"{m['range_val']:.6f} > 1.0 ⇒ 该子句单独把 PASS 翻成 FAIL"
            ),
            "fatal_2_l837": (
                "源执行棒 L837 kill_lines 字典丢弃 pass 命名 wrapper，存 raw bool；"
                "若按「True = hit」消费则与预登记字面「CV >= 0.50 即 FAIL」方向相反"
            ),
            "post_fix": "两项均已在新名件修复；升格件归因「threshold-evaluation-path artifact」漏致命 1",
        },
        "iron_rules": {
            "no_llm_no_api": "0 LLM / 0 API / 0 proxy / 0 gateway（纯本地 random.Random(42)）",
            "no_prereg_touch": "TH_TAU_CV=0.50 与 K-S40-1/2/3 字面一字未动",
            "no_source_modify": "源执行棒 / 升格件 / 预登记 / 语义复核件 全只读",
            "no_baked_verdict": "verdict 由公式算出，未写死",
        },
    }


# ============================================================
# 只读等价性核对：import 源执行棒 → 调 run_S40() → 与本件复刻比对
# ============================================================
def cross_check(rec: Dict[str, Any]) -> Dict[str, Any]:
    if not SRC_EXECUTOR.exists():
        return {"ran": False, "reason": "source executor not found"}
    import importlib.util

    spec = importlib.util.spec_from_file_location("_v4_rerun_src_ro", SRC_EXECUTOR)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # 只读执行：顶层仅 mkdir(exist_ok=True) no-op
    mod._load_caption_data()
    src = mod.run_S40()

    same = (
        src["verdict"] == rec["verdict"]
        and abs(src["main_metric"] - rec["metrics_rounded_4"]["cv_val"]) < 1e-9
        and abs(src["ci_95"][1] - rec["metrics_rounded_4"]["ci_95"][1]) < 1e-9
        and abs(src["max_min_range"] - rec["metrics_rounded_4"]["max_min_range"]) < 1e-9
        and abs(src["negctrl_cv"] - rec["metrics_rounded_4"]["negctrl_cv"]) < 1e-9
        and src["n_cells"] == rec["metrics_full_precision"]["n_cells"]
    )
    for k, v in src["kill_lines"].items():
        if bool(v["pass"]) != bool(rec["kill_lines_postfix"][k]["pass"]):
            same = False
    return {
        "ran": True,
        "mode": "read-only import of source executor + run_S40()",
        "source_verdict": src["verdict"],
        "replica_verdict": rec["verdict"],
        "source_main_metric": src["main_metric"],
        "replica_main_metric": rec["metrics_rounded_4"]["cv_val"],
        "source_kill_lines_pass": {k: v["pass"] for k, v in src["kill_lines"].items()},
        "replica_kill_lines_pass": {
            k: v["pass"] for k, v in rec["kill_lines_postfix"].items()
        },
        "equivalent": bool(same),
    }


def main(argv: List[str]) -> int:
    rec = recompute()
    if "--cross-check" in argv:
        rec["cross_check"] = cross_check(rec)

    out = RESULTS_DIR / "_v5r_s40_recompute_2026_09_29.json"
    out.write_text(json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8")
    sha, size = file_sha12(out)

    mp = rec["metrics_rounded_4"]
    print("=== S-40 recompute (M-R3 fix, new-name file) ===")
    print(f"  CV        = {mp['cv_val']}  (TH_TAU_CV = {TH_TAU_CV})")
    print(f"  CI95      = {mp['ci_95']}  (hi vs {TH_TAU_CV})")
    print(f"  CV_shuf   = {mp['negctrl_cv']}")
    print(f"  range_val = {mp['max_min_range']}  (构造警告，非 kill-line)")
    print("  kill-line hits:")
    for k, v in rec["kill_line_hits"].items():
        print(f"    {k}: hit={v}  pass={rec['kill_lines_postfix'][k]['pass']}")
    print(f"  all_three_false = {rec['all_three_false']}")
    print(f"  VERDICT  = {rec['verdict']}  ({rec['root_cause']})")
    if "cross_check" in rec:
        cc = rec["cross_check"]
        print(f"  cross-check equivalent = {cc.get('equivalent')}")
    print(f"  wrote {out.name}  sha12={sha}  bytes={size}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
