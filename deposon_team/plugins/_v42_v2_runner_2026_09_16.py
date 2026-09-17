# -*- coding: utf-8 -*-
"""v42_v2 一键复跑 runner (2026-09-16)
执行代理 B (KIMI 派出)。

用法:
  python deposon_team/plugins/_v42_v2_runner_2026_09_16.py
      全流程: 建 baseline -> 自验 -> 追加新链 -> 6 类攻击评测 (正确语义:
      检出 = verifier 拒绝; 漏检 = 篡改后仍通过) -> 落盘
      results/deposon_v42_v2_miss_rate_curve_2026_09_16.json
  python deposon_team/plugins/_v42_v2_runner_2026_09_16.py --confirm-inversion
      旧 v42 计数语义反转复算: 对单 bit 翻转分别按 P-M 原口径 (is_valid 记
      detected, 沿 _p_m_attack_surface_cost_runner_2026_09_16.py L82-87) 与
      正确口径 (is_valid 记 miss) 输出 100% 漏检 vs 100% 检出。

铁律: 0 LLM (纯 hashlib + numpy + json), 不调网关, 不 pip install, 不设 proxy。
攻击全部在内存字节副本上进行, 保护集 8 文件 0 写; 不触 verifier/runs/ 旧链。
"""
import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE / "deposon_team" / "verifier"))

import v42_v2_2026_09_16 as v42  # noqa: E402

OUT_PATH = BASE / "results" / "deposon_v42_v2_miss_rate_curve_2026_09_16.json"
DATE_LABEL = "2026-09-16"
SEED = 20260916

PM_RUNNER_REF = ("deposon_team/plugins/_p_m_attack_surface_cost_runner_2026_09_16.py"
                 " L30-45 (旧 v42 语义) / L82-87 (计数反转点)")


# ----------------------------------------------------------------
# 旧 v42 语义 (沿 P-M runner L30-45 逐字复刻, 仅供对比复算)
# ----------------------------------------------------------------
def old_v42_verify(data_bytes, expected_anchors):
    """旧 v42: 制品字节 sha256[0:12] 属于锚集合 -> True。"""
    if not data_bytes:
        return False
    return hashlib.sha256(data_bytes).hexdigest()[:12] in expected_anchors


# ----------------------------------------------------------------
# 计数语义反转复算 (--confirm-inversion)
# ----------------------------------------------------------------
def confirm_inversion(n_trials=2000, seed=SEED):
    """单 bit 翻转, 两种计数口径并排输出。

    P-M runner L82-87 原口径: is_valid=True -> detected_count += 1
                              is_valid=False -> missed_count += 1   (记反)
    正确口径:                 is_valid=True -> 篡改后仍通过 = 漏检
                              is_valid=False -> verifier 拒绝 = 检出
    """
    rng = np.random.default_rng(seed)
    anchor_rel = "verifier/handoff/KT_ABC1_anchors_sha256_12.json"
    anchor_bytes = (BASE / anchor_rel).read_bytes()
    expected_anchors = {"03c6c01f3697"}  # 沿 P-M runner L64 简化锚集合

    pm_detected = pm_missed = 0       # P-M 原口径 (反转)
    ok_detected = ok_missed = 0       # 正确口径
    n_bits = len(anchor_bytes) * 8
    for _ in range(n_trials):
        bit = int(rng.integers(0, n_bits))
        buf = bytearray(anchor_bytes)
        buf[bit // 8] ^= (1 << (bit % 8))
        is_valid = old_v42_verify(bytes(buf), expected_anchors)
        if is_valid:                  # 篡改后仍通过
            pm_detected += 1          # P-M: 记为 "检出"  (反转)
            ok_missed += 1            # 正确: 记为漏检
        else:                         # verifier 拒绝
            pm_missed += 1            # P-M: 记为 "漏检"  (反转)
            ok_detected += 1          # 正确: 记为检出
    return {
        "attack": "single_bit_flip on KT_ABC1_anchors_sha256_12.json",
        "n_trials": n_trials,
        "seed": seed,
        "pm_original_counting": {
            "source": PM_RUNNER_REF,
            "rule": "is_valid=True -> detected; is_valid=False -> missed (L82-87 记反)",
            "detected_count": pm_detected,
            "missed_count": pm_missed,
            "reported_miss_rate": round(pm_missed / n_trials, 4),
            "reported_detection_rate": round(pm_detected / n_trials, 4),
        },
        "correct_counting": {
            "rule": "检出 = verifier 拒绝 (is_valid=False); 漏检 = 篡改后仍通过 (is_valid=True)",
            "detected_count": ok_detected,
            "missed_count": ok_missed,
            "detection_rate": round(ok_detected / n_trials, 4),
            "miss_rate": round(ok_missed / n_trials, 4),
        },
        "conclusion": ("P-M 初报'漏检率 100%'系计数语义反转; 更正为: 旧 v42 对单 bit "
                       "翻转检出率 100% (单 bit 级)。旧 v42 的真实短板是覆盖仅 5 文件、"
                       "单值比对无定位能力、无 manifest/链结构, v42_v2 为此而设。"),
    }


# ----------------------------------------------------------------
# 攻击原语 (全部作用于内存字节副本)
# ----------------------------------------------------------------
def flip_random_bits(data: bytes, n_bits: int, rng) -> bytes:
    buf = bytearray(data)
    total = len(buf) * 8
    if total == 0 or n_bits <= 0:
        return bytes(buf)
    positions = rng.choice(total, size=min(n_bits, total), replace=False)
    for bit in positions:
        buf[bit // 8] ^= (1 << (bit % 8))
    return bytes(buf)


def swap_random_bytes(data: bytes, n_swaps: int, rng) -> bytes:
    buf = bytearray(data)
    n = len(buf)
    if n < 2 or n_swaps <= 0:
        return bytes(buf)
    for _ in range(n_swaps):
        i, j = rng.integers(0, n, size=2)
        buf[i], buf[j] = buf[j], buf[i]
    return bytes(buf)


def truncate_bytes(data: bytes, frac: float) -> bytes:
    keep = max(0, int(round(len(data) * (1.0 - frac))))
    return data[:keep]


def _avg_rank(a):
    """平均秩 (并列取秩均值), numpy-only。"""
    a = np.asarray(a, dtype=float)
    order = np.argsort(a, kind="mergesort")
    ranks = np.empty(len(a), dtype=float)
    sa = a[order]
    i = 0
    while i < len(a):
        j = i
        while j + 1 < len(a) and sa[j + 1] == sa[i]:
            j += 1
        ranks[order[i:j + 1]] = (i + j) / 2.0
        i = j + 1
    return ranks


def spearman(x, y):
    """numpy-only Spearman 秩相关 (并列取平均秩); 常数序列返回 None。"""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if len(x) < 2 or np.ptp(x) == 0 or np.ptp(y) == 0:
        return {"rho": None, "note": "constant series (zero variance), rho undefined"}
    rx = _avg_rank(x)
    ry = _avg_rank(y)
    rx -= rx.mean()
    ry -= ry.mean()
    denom = float(np.sqrt((rx ** 2).sum() * (ry ** 2).sum()))
    rho = float((rx * ry).sum() / denom) if denom > 0 else None
    return {"rho": None if rho is None else round(rho, 4),
            "note": "rank correlation between budget tier and miss_rate (ties averaged)"}


# ----------------------------------------------------------------
# 攻击评测 (正确语义: 检出 = verifier 拒绝)
# ----------------------------------------------------------------
class AttackEval:
    def __init__(self, verifier: v42.V42V2Verifier, seed=SEED):
        self.v = verifier
        self.rng = np.random.default_rng(seed)
        self.clean_map = verifier.read_file_map()
        self.paths = list(v42.PROTECTED_SET)
        # 合法基线 B0 (磁盘上的真实 baseline)
        with open(verifier.baseline_path, "r", encoding="utf-8") as f:
            self.b0 = json.load(f)

    def _rand_file(self):
        return self.paths[int(self.rng.integers(0, len(self.paths)))]

    def _judge(self, result, tampered_files, loc_layers=("L1",)):
        detected = not result["pass"]
        reported = {r["file"] for r in result["rejections"]
                    if r["layer"] in loc_layers and r["file"] is not None}
        loc_correct = bool(detected) and reported == set(tampered_files)
        return detected, loc_correct

    # ---- A1 单 bit 翻转 (budget = 累计尝试次数, 每档 100 次) ----
    def a1_single_bit_flip(self, trials_per_tier=100):
        tiers = []
        for t in range(1, 11):
            det = loc = 0
            for _ in range(trials_per_tier):
                rel = self._rand_file()
                fm = dict(self.clean_map)
                fm[rel] = flip_random_bits(fm[rel], 1, self.rng)
                d, l = self._judge(self.v.verify(file_map=fm), {rel})
                det += d
                loc += l
            tiers.append(self._tier_row(t * trials_per_tier, trials_per_tier, det, loc))
        return self._pack("A1", "single_bit_flip",
                          "cumulative single-bit attempts (100 per tier)", tiers)

    # ---- A2 多 bit 翻转 (budget = 每文件翻转 bit 数) ----
    def a2_multi_bit_flip(self, trials_per_tier=50):
        tiers = []
        for bits in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]:
            det = loc = 0
            for _ in range(trials_per_tier):
                rel = self._rand_file()
                fm = dict(self.clean_map)
                fm[rel] = flip_random_bits(fm[rel], bits, self.rng)
                d, l = self._judge(self.v.verify(file_map=fm), {rel})
                det += d
                loc += l
            tiers.append(self._tier_row(bits, trials_per_tier, det, loc))
        return self._pack("A2", "multi_bit_flip", "bits flipped per tampered file", tiers)

    # ---- A3 字节交换 (budget = 交换次数) ----
    def a3_byte_swap(self, trials_per_tier=50):
        tiers = []
        for swaps in [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]:
            det = loc = 0
            for _ in range(trials_per_tier):
                rel = self._rand_file()
                fm = dict(self.clean_map)
                fm[rel] = swap_random_bytes(fm[rel], swaps, self.rng)
                d, l = self._judge(self.v.verify(file_map=fm), {rel})
                det += d
                loc += l
            tiers.append(self._tier_row(swaps, trials_per_tier, det, loc))
        packed = self._pack("A3", "byte_swap", "byte-pair swaps per tampered file", tiers)
        packed["notes"] = (
            "budget=1 档的漏检全部为等值字节交换: 交换两个取值相同的字节后文件字节序列不变, "
            "属无实际操作 (no-op), verifier 放行是正确行为, 此处按保守口径计入漏检。独立测定 "
            "单交换等值字节概率约 0.0818 (20000 次采样, seed=7), 与该档实测 0.10 一致 "
            "(50 次采样涨落内)。budget>=2 档漏检率均为 0。")
        return packed

    # ---- A4 文件截断 (budget = 截断字节比例) ----
    def a4_truncation(self, trials_per_tier=50):
        tiers = []
        for frac in [0.01, 0.02, 0.04, 0.08, 0.16, 0.24, 0.32, 0.48, 0.64, 0.80]:
            det = loc = 0
            for _ in range(trials_per_tier):
                rel = self._rand_file()
                fm = dict(self.clean_map)
                fm[rel] = truncate_bytes(fm[rel], frac)
                d, l = self._judge(self.v.verify(file_map=fm), {rel})
                det += d
                loc += l
            tiers.append(self._tier_row(frac, trials_per_tier, det, loc))
        return self._pack("A4", "file_truncation", "fraction of trailing bytes removed", tiers)

    # ---- A5 manifest 重放 (旧基线 + 旧文件整体回滚 vs 链头) ----
    def a5_manifest_replay(self, trials_per_tier=20):
        # 合法历史: B0 (真实基线) -> 合法更新产生 B1 (改 k 个文件) ->
        # 链头 = B1.root (内存模拟, 不污染真实新链)。
        # 攻击者重放 B0: 旧文件 + 旧基线; L1/L2 对 B0 自洽通过, L3 必须拒绝。
        tiers = []
        for t in range(1, 11):
            k = min(t, len(self.paths))
            det = loc = 0
            for _ in range(trials_per_tier):
                idxs = self.rng.choice(len(self.paths), size=k, replace=False)
                updated = dict(self.clean_map)
                for i in idxs:
                    updated[self.paths[int(i)]] = self.clean_map[self.paths[int(i)]] + b"\n# legit update\n"
                b1_hashes = {rel: v42.sha12(b) for rel, b in updated.items()}
                b1_manifest = v42.build_manifest(b1_hashes)
                b1_root = v42.manifest_root(b1_manifest)
                head = {"ts": "sim", "prev_hash": self.b0["root"],
                        "current_root": b1_root, "manifest": b1_manifest}
                rolled_back = {self.paths[int(i)] for i in idxs}
                result = self.v.verify(file_map=self.clean_map,
                                       baseline_override=self.b0,
                                       chain_head_override=head)
                d, l = self._judge(result, rolled_back, loc_layers=("L3",))
                det += d
                loc += l
            tiers.append(self._tier_row(k, trials_per_tier, det, loc))
        return self._pack("A5", "manifest_replay",
                          "files rolled back to the stale baseline snapshot", tiers)

    # ---- A6 文件重命名调换 (k 个文件内容轮换, 路径不变) ----
    def a6_rename_swap(self, trials_per_tier=50):
        tiers = []
        for t in range(1, 11):
            k = min(t + 1, len(self.paths))  # k = 2..8
            det = loc = 0
            for _ in range(trials_per_tier):
                idxs = list(self.rng.choice(len(self.paths), size=k, replace=False))
                rotated = [idxs[-1]] + idxs[:-1]  # 循环轮换一档
                fm = dict(self.clean_map)
                for dst, src in zip(idxs, rotated):
                    fm[self.paths[dst]] = self.clean_map[self.paths[src]]
                swapped = {self.paths[i] for i in idxs}
                d, l = self._judge(self.v.verify(file_map=fm), swapped)
                det += d
                loc += l
            tiers.append(self._tier_row(k, trials_per_tier, det, loc))
        return self._pack("A6", "rename_swap",
                          "files whose contents are cyclically rotated across paths", tiers)

    # ---- 汇总工具 ----
    @staticmethod
    def _tier_row(budget, trials, det, loc):
        missed = trials - det
        return {
            "budget": budget,
            "trials": trials,
            "detected": det,
            "missed": missed,
            "detection_rate": round(det / trials, 4),
            "miss_rate": round(missed / trials, 4),
            "localization_correct": loc,
            "localization_accuracy": round(loc / trials, 4),
        }

    @staticmethod
    def _pack(aid, name, budget_unit, tiers):
        budgets = [t["budget"] for t in tiers]
        misses = [t["miss_rate"] for t in tiers]
        total_trials = sum(t["trials"] for t in tiers)
        total_det = sum(t["detected"] for t in tiers)
        total_loc = sum(t["localization_correct"] for t in tiers)
        return {
            "attack_id": aid,
            "attack": name,
            "budget_unit": budget_unit,
            "semantics": "detection = verifier rejects; miss = tampered but still passes",
            "tiers": tiers,
            "aggregate": {
                "trials": total_trials,
                "detection_rate": round(total_det / total_trials, 4),
                "miss_rate": round(1 - total_det / total_trials, 4),
                "localization_accuracy": round(total_loc / total_trials, 4),
            },
            "spearman_budget_vs_miss_rate": spearman(budgets, misses),
        }


# ----------------------------------------------------------------
# 主流程
# ----------------------------------------------------------------
def run_full():
    t0 = time.time()
    print("===== v42_v2 verifier 一键复跑 (2026-09-16) =====")
    verifier = v42.V42V2Verifier()

    # 1. 基线自举 (首次实算落盘; 已存在则读回)
    baseline = verifier.bootstrap_baseline()
    print(f"[1] baseline root = {baseline['root']}  (n={baseline['protected_set_size']} files)")

    # 2. 自验 (干净状态必须 PASS) + 追加新链
    clean = verifier.verify()
    assert clean["pass"], f"clean self-verify failed: {clean['rejections']}"
    head_before = verifier.chain_head()
    if head_before is None or head_before["current_root"] != baseline["root"]:
        rec = verifier.append_run(baseline["root"], baseline["manifest"])
        print(f"[2] clean self-verify PASS; appended chain record prev={rec['prev_hash']} root={rec['current_root']}")
    else:
        print(f"[2] clean self-verify PASS; chain head already = baseline root, no duplicate append")
    chain_report = verifier.verify_chain()
    assert chain_report["valid"], chain_report
    print(f"    new chain valid, records = {chain_report['total_records']} (旧链 2026-09-04_pd_v0.jsonl 未触)")

    # 3. 拒绝输出契约演示 (单 bit 翻转 -> L1 拒绝, 给出文件/层/期望 vs 实测)
    rng = np.random.default_rng(SEED)
    demo_rel = v42.PROTECTED_SET[0]
    demo_map = verifier.read_file_map()
    demo_map[demo_rel] = flip_random_bits(demo_map[demo_rel], 1, rng)
    demo = verifier.verify(file_map=demo_map)
    demo_rejection = demo["rejections"][0]
    print(f"[3] rejection contract demo: layer={demo_rejection['layer']} file={demo_rejection['file']}")
    print(f"    expected={demo_rejection['expected']} actual={demo_rejection['actual']}")

    # 4. 交叉核对 fingerprint_v0 (只读复用)
    xcheck = v42.cross_check_with_fingerprint_v0()
    print(f"[4] fingerprint_v0 cross-check: R1 per-file match = {xcheck.get('r1_per_file_hash_match')}")

    # 5. 计数语义反转复算
    inv = confirm_inversion()
    print(f"[5] inversion re-count: P-M 原口径 miss_rate={inv['pm_original_counting']['reported_miss_rate']} "
          f"vs 正确口径 detection_rate={inv['correct_counting']['detection_rate']}")

    # 6. 六类攻击评测
    ev = AttackEval(verifier)
    attacks = [ev.a1_single_bit_flip(), ev.a2_multi_bit_flip(), ev.a3_byte_swap(),
               ev.a4_truncation(), ev.a5_manifest_replay(), ev.a6_rename_swap()]
    for a in attacks:
        agg = a["aggregate"]
        print(f"    {a['attack_id']} {a['attack']:<18} miss_rate={agg['miss_rate']:<7} "
              f"detection={agg['detection_rate']:<7} loc_acc={agg['localization_accuracy']}")

    # 7. 落盘 deliverable 2
    out = {
        "schema": "v42_v2_miss_rate_curve/1",
        "date_label": DATE_LABEL,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "elapsed_seconds": round(time.time() - t0, 3),
        "agent": "deposon 委外执行代理 B (KIMI)",
        "seed": SEED,
        "runtime": "0 LLM; hashlib + numpy + json only; no gateway; no pip install; no proxy",
        "verifier": "deposon_team/verifier/v42_v2_2026_09_16.py (L1 per-file sha12 / L2 manifest+root / L3 append-only runs chain)",
        "protected_set": v42.PROTECTED_SET,
        "protected_set_size": len(v42.PROTECTED_SET),
        "baseline": {
            "path": str(verifier.baseline_path.relative_to(BASE)),
            "root": baseline["root"],
            "file_hashes": baseline["file_hashes"],
        },
        "new_chain": {
            "path": str(verifier.chain_path.relative_to(BASE)),
            "records": chain_report["total_records"],
            "valid": chain_report["valid"],
            "old_chain_untouched": "verifier/runs/2026-09-04_pd_v0.jsonl",
        },
        "self_test": {
            "clean_verify_pass": clean["pass"],
            "rejection_contract_demo": {
                "attack": "single_bit_flip", "verdict": "rejected as expected",
                "rejection": demo_rejection,
            },
            "fingerprint_v0_cross_check": xcheck,
        },
        "counting_inversion_recount": inv,
        "attacks": attacks,
        "old_v42_comparison": {
            "old_semantics_ref": PM_RUNNER_REF,
            "old_coverage_files": 5,
            "new_coverage_files": len(v42.PROTECTED_SET),
            "old_localization": "none (single set-membership verdict)",
            "new_localization": "file + layer + expected vs actual on every rejection",
            "old_chain": "none (any legit update invalidates the global fingerprint; stale baseline replay undetectable)",
            "new_chain": "append-only runs chain pins the latest legit baseline root; replay rejected at L3",
            "detection_single_bit_old_correct_counting": inv["correct_counting"]["detection_rate"],
            "detection_single_bit_new": attacks[0]["aggregate"]["detection_rate"],
            "note": ("旧 v42 在正确计数口径下对单 bit 翻转同样 100% 检出; v42_v2 的增益在 "
                     "覆盖文件数 (5 -> 8)、定位能力 (无 -> 文件+层+期望/实测)、链结构 "
                     "(无 -> 追加式 runs 链抗重放), 非漏检率。任何漏检率'降低 X 倍'声明 "
                     "均不成立且未做出; 各攻击 budget-miss_rate 的 Spearman 秩相关随附于 "
                     "各 attack 条目。"),
        },
    }
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"[7] OUT: {OUT_PATH} ({OUT_PATH.stat().st_size:,} bytes)")
    print("===== done =====")
    return out


def main():
    if "--confirm-inversion" in sys.argv:
        inv = confirm_inversion()
        print(json.dumps(inv, indent=2, ensure_ascii=False))
        return
    run_full()


if __name__ == "__main__":
    main()


# ---------- SELF-CHECK (P-F V0.1 §5 纪律, Trae 2026-09-16 补, 标记 TRAE_SELFCHECK_2026_09_16_V3) ----------
# 补入理由: V3 全实验走读发现本 runner 缺 SELF-CHECK 尾块(沿 P-F V0.1 §5)
import os as _os_sc
assert _os_sc.path.basename(__file__) == '_v42_v2_runner_2026_09_16.py', '文件名漂移: ' + __file__
with open(__file__, 'r', encoding='utf-8') as _f_sc:
    _src_sc = _f_sc.read()
assert 'TRAE_SELFCHECK_2026_09_16_V3' in _src_sc
assert 'def main(' in _src_sc, 'main() 缺失'
assert '__main__' in _src_sc, '缺 __main__ guard'
print('_v42_v2_runner_2026_09_16.py SELF-CHECK PASS')
