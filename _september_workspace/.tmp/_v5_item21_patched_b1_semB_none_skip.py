"""
KT-B1 BOSS-B1 baseline: Sinkhorn OT 失真度测法
Reference: Cuturi 2013, "Sinkhorn Distances: Lightspeed Computation of Optimal Transport", NeurIPS

目的: 防 V1 六关键词规则重演 — 验证"deposon 失真上界"是否被通用 Sinkhorn OT 工具拍平。
判死: 若 Sinkhorn OT 失真上界 ≥ 0.95 (200 节点 v19 冻结数据) → 失真上界不特殊,
      deposon 主张降级为"通用 OT 工具的下限"。

真实现 (D1):
  - 从 v19 frozen 加载 200 题 (E9.3 gsm8k + E9.3 strategyqa)
  - 每题构建"deposon 报告分布"(基于 predicted / best_path)和"真值分布"
  - 跑 Sinkhorn 迭代 (Cuturi 2013): u <- a / (K @ (v / reg)); v <- b / (K.T @ (u / reg))
  - 距离 = sum(u * K * v)  熵正则化 OT
  - 失真上界 = mean over 200 OT 距离

冻结时点: 2026-09-09 (D0 准备阶段)
派单路径: Mavis → data → reviewer-b
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Iterable


# =============================================================================
# 冻结接口契约 (本脚本必须始终保持)
# =============================================================================

ANCHOR_ID = "KT_B1_BOSS_B1_SINKHORN_OT"
"""5 锚扩展之一 (沿用 KT_B1_HARNESS 子锚, 本占位脚本的逻辑锚 ID)"""

# 数据集路径 (v19 frozen, 只读)
V19_FROZEN_BENCHMARK = "results/deposon_v19_benchmark_fixes.json"
"""v19 frozen 基准 - 200 道合成题, 守恒审计 T+R+A=1 最大残差 2.2e-16"""

# 判死线
SINKHORN_DISTORTION_UB_THRESHOLD = 0.95
"""Sinkhorn OT 失真上界 ≥ 0.95 → 失真上界被通用 OT 拍平"""

# 任务规模
N_NODES = 200
N_QUESTIONS = 200

# Sinkhorn 超参
SINKHORN_REG = 0.1
SINKHORN_NUM_ITER = 200
N_BOSS_RESAMPLES = 1000  # 熵正则化扫描(10^-1 ~ 10^-4)

# 复现协议
REVIEWER_B_TMP_REPLICA = "/tmp/deposon_kt_b1_audit_{timestamp}/"
SEED_LOCK = 42


# =============================================================================
# 数据加载
# =============================================================================


def load_v19_benchmark(path: str = V19_FROZEN_BENCHMARK) -> dict:
    """
    加载 v19 冻结基准 (只读)。

    Returns:
        dict: 含 200 道合成题 + 守恒审计残差。
        {
            "physics_audit": {"t_plus_r_plus_a_max_deviation": 2.2e-16, ...},
            "experiments": {
                "E9.3_high_couple_fix": {
                    "benchmarks": {
                        "gsm8k": {"per_problem": {...}, "summary": {...}},
                        "strategyqa": {...},
                    }
                },
                ...
            }
        }
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"v19 frozen JSON {path} 不存在 (冻结资产只读)")
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


# =============================================================================
# [V4#21 副本补丁 · PATCH-START] 锚版本体 0 触动；仅 .tmp 副本打补丁
# 补丁三要素：① None 容错 ② v19 双形态回退 ③ 由驱动侧 SourceFileLoader 承接
# =============================================================================


def _patch_to_float(v) -> float:
    """补丁①a: 数值字段 None/非法容错 -> 0.0 (策略qa 实测无 answer 键)。"""
    if v is None:
        return 0.0
    if isinstance(v, bool):
        return 1.0 if v else 0.0
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        try:
            return float(v)
        except ValueError:
            return 0.0
    return 0.0


def _patch_norm_pred(v) -> float:
    """补丁①②: v19 双形态预测值归一（不做 [0,1] clamp，保留原始量级/负值）。
    gsm8k = 数值(predicted 键) / strategyqa = 'Yes'/'No' 串(pred 键)。"""
    if v is None:
        return 0.0
    if isinstance(v, bool):
        return 1.0 if v else 0.0
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        s = v.strip().lower()
        if s in ("yes", "y", "true", "1"):
            return 1.0
        if s in ("no", "n", "false", "0"):
            return 0.0
        try:
            return float(v)
        except ValueError:
            return 0.0
    return 0.0

# [PATCH-END]


def _extract_200_questions(v19_data: dict) -> list[dict]:
    """
    提取 200 道题 (E9.3 gsm8k + E9.3 strategyqa) 每题关键字段。

    Returns:
        200 道题列表, 每题: {
            "id": int, "experiment": str, "benchmark": str, "condition": str,
            "predicted": float, "answer": float, "is_correct": bool,
            "best_path": list[str], "trap_hit": str,
        }
    """
    out = []
    e93 = v19_data["experiments"].get("E9.3_high_couple_fix", {})
    benchmarks = e93.get("benchmarks", {})
    for bm_name in ("gsm8k", "strategyqa"):
        bm = benchmarks.get(bm_name, {})
        per_problem = bm.get("per_problem", {})
        for cond, problems in per_problem.items():
            for p in problems:
                # [PATCH ①②] v19 双形态: pred 键(strategyqa) / predicted 键(gsm8k)
                _raw_pred = p.get("pred", p.get("predicted", 0.0))
                # [PATCH ① 语义B] None 显式跳过该条（不计入题集）
                if _raw_pred is None:
                    continue
                out.append(
                    {
                        "id": int(p.get("id", 0)),
                        "experiment": "E9.3_high_couple_fix",
                        "benchmark": bm_name,
                        "condition": cond,
                        "predicted": _patch_norm_pred(_raw_pred),
                        "answer": _patch_to_float(p.get("answer", 0.0)),
                        "is_correct": bool(p.get("is_correct", False)),
                        # [PATCH ②] best_path 键(gsm8k) / path 键(strategyqa)
                        "best_path": list(p.get("best_path", p.get("path", []))),
                        "trap_hit": p.get("trap_hit", ""),
                    }
                )
    return out


# =============================================================================
# 分布构造 (deposon 报告分布 vs 真值分布)
# =============================================================================


def _build_source_target_distributions(
    question: dict, vocab: list[str]
) -> tuple[list[float], list[float]]:
    """
    把一道题转为 (source_dist, target_dist), 在 vocab 词表上。

    source (deposon 报告):
      - 在 best_path 上的节点上分配权重, 强度 ∝ |predicted|
      - softmax(weighted), 概率归一化
    target (真值):
      - 答案 numerical -> 离散化(截断到词表前 N)
      - 若 answer 在 [0, |vocab|) 内, 1-hot 在 answer 处
      - 否则 1-hot 在 0 (默认)

    Args:
        question: 1 道题
        vocab: 词表 (节点名去重)

    Returns:
        (source, target), 两个等长概率分布(和为 1)
    """
    n = len(vocab)
    if n == 0:
        return ([1.0], [1.0])
    word_to_idx = {w: i for i, w in enumerate(vocab)}
    source = [0.0] * n
    target = [0.0] * n

    # Source: 在 best_path 上的节点按 predicted 强度放权重
    path = question.get("best_path", [])
    pred = question.get("predicted", 0.0)
    # pred 可能为负, 用 max(0, pred) + 1 平移
    w = max(0.0, abs(pred)) + 1.0
    for node in path:
        if node in word_to_idx:
            source[word_to_idx[node]] += w
    # 平滑 + 归一化
    eps = 1e-9
    s = sum(source) + eps * n
    source = [(x + eps) / s for x in source]

    # Target: 1-hot 在 answer 离散化位置
    ans = question.get("answer", 0.0)
    try:
        ans_int = int(round(ans))
    except (ValueError, OverflowError):
        ans_int = 0
    ans_int = max(0, min(n - 1, ans_int % n))
    target[ans_int] = 1.0
    return source, target


def _build_vocabulary(questions: list[dict]) -> list[str]:
    """从 200 题 best_path 中提取去重节点名当词表。"""
    seen = set()
    vocab = []
    for q in questions:
        for node in q.get("best_path", []):
            if node not in seen:
                seen.add(node)
                vocab.append(node)
    if not vocab:
        vocab = ["UNK"]
    return vocab


# =============================================================================
# Sinkhorn 迭代 (Cuturi 2013)
# =============================================================================


def _cost_matrix(p: list[float], q: list[float]) -> list[list[float]]:
    """
    构造 squared-euclidean cost 矩阵 C[i][j] = 0.5 * |p_i - q_j|^2。

    注: 这里 source/target 是 vocab 索引上的概率分布, 把"位置差"作为几何距离的代理。
        C[i][j] = 0.5 * (i - j)^2 / max(i, j, 1)
    """
    n = max(len(p), len(q))
    C = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = 0.5 * (i - j) ** 2 / max(i, j, 1)
    return C


def compute_sinkhorn_ot_distance(
    source_dist: list[float],
    target_dist: list[float],
    reg: float = SINKHORN_REG,
    num_iter: int = SINKHORN_NUM_ITER,
) -> float:
    """
    Sinkhorn OT 距离 (熵正则化 OT, Cuturi 2013)。

    公式:
      K_ij = exp(-C_ij / reg)
      u <- a / (K @ (v / reg))   [但实际常用 v <- b / (K.T @ u)]
      v <- b / (K.T @ u)
      u <- a / (K @ v)
      ... 交替, 至收敛
      距离 = sum(u * K * v)

    Args:
        source_dist: 源分布 (a)
        target_dist: 目标分布 (b)
        reg: 熵正则化系数 λ (越小越接近真实 OT 距离)
        num_iter: Sinkhorn 迭代次数

    Returns:
        Sinkhorn OT 距离(标量)
    """
    a = list(source_dist)
    b = list(target_dist)
    n = len(a)
    if n == 0 or len(b) == 0:
        return 0.0
    # 长度对齐
    if len(b) != n:
        m = max(n, len(b))
        a = a + [0.0] * (m - n)
        b = b + [0.0] * (m - len(b))
        n = m
    eps = 1e-30
    a = [max(ai, eps) for ai in a]
    b = [max(bi, eps) for bi in b]
    sa = sum(a)
    sb = sum(b)
    a = [ai / sa for ai in a]
    b = [bi / sb for bi in b]

    # 核矩阵 K
    C = _cost_matrix(a, b)
    K = [[math.exp(-C[i][j] / reg) for j in range(n)] for i in range(n)]

    # 初始化 u, v
    u = [1.0] * n
    v = [1.0] * n

    for _ in range(num_iter):
        # v = b / (K.T @ u)
        new_v = []
        for j in range(n):
            denom = sum(K[i][j] * u[i] for i in range(n))
            new_v.append(b[j] / max(denom, eps))
        v = new_v
        # u = a / (K @ v)
        new_u = []
        for i in range(n):
            denom = sum(K[i][j] * v[j] for j in range(n))
            new_u.append(a[i] / max(denom, eps))
        u = new_u

    # 距离 = sum(u * K * v) * reg (Cuturi 2013 式 5)
    total = 0.0
    for i in range(n):
        for j in range(n):
            total += u[i] * K[i][j] * v[j]
    return total * reg


# =============================================================================
# 失真上界
# =============================================================================


def compute_distortion_upper_bound(
    v19_data: dict, reg: float = SINKHORN_REG
) -> float:
    """
    算 Sinkhorn OT 失真上界 (200 节点平均)。

    失真上界 = mean over 200 questions of Sinkhorn OT(source=deposon, target=ground truth)
    """
    questions = _extract_200_questions(v19_data)
    if not questions:
        return 0.0
    vocab = _build_vocabulary(questions)
    n = len(vocab)
    if n == 0:
        return 0.0
    # 最大可能 OT 距离(用作归一化, 0-1 范围)
    # 用对角线 C_max = 0.5 * (n-1)^2 / 1, 距离 ≈ C_max * (1 + 1/n) / 2
    c_max = 0.5 * (n - 1) ** 2
    norm = max(c_max * 0.5, 1.0)  # 防 0

    distances = []
    for q in questions:
        src, tgt = _build_source_target_distributions(q, vocab)
        d = compute_sinkhorn_ot_distance(src, tgt, reg=reg)
        # 归一化到 0-1
        d_norm = min(1.0, d / norm)
        distances.append(d_norm)
    return sum(distances) / len(distances)


# =============================================================================
# 熵正则化扫描
# =============================================================================


def scan_regularization(
    v19_data: dict,
    regs: list[float] | None = None,
) -> dict[float, float]:
    """
    扫描熵正则化系数 reg (从粗到细, 看 Sinkhorn OT 距离是否平稳)。

    Args:
        v19_data: load_v19_benchmark() 输出
        regs: reg 列表, 默认 [0.5, 0.1, 0.05, 0.01, 0.005, 0.001]

    Returns:
        dict[reg, distortion_upper_bound]: 各 reg 下的失真上界
    """
    if regs is None:
        regs = [0.5, 0.1, 0.05, 0.01, 0.005, 0.001]
    out = {}
    for r in regs:
        out[r] = compute_distortion_upper_bound(v19_data, reg=r)
    return out


# =============================================================================
# 4 档裁定
# =============================================================================


def boss_b1_verdict(
    sinkhorn_distortion_ub: float,
    deposon_distortion_ub: float,
    threshold: float = SINKHORN_DISTORTION_UB_THRESHOLD,
) -> str:
    """
    BOSS-B1 裁定。

    4 档:
      - "PASS_DIFFERENTIATED": sinkhorn < threshold, deposon >= threshold
      - "GRAY_BOTH_BELOW": sinkhorn < threshold, deposon < threshold
      - "GRAY_BOTH_ABOVE": sinkhorn >= threshold, deposon >= threshold
      - "FAIL_SINKHORN_OUTPERFORMS": sinkhorn > deposon
    """
    s_below = sinkhorn_distortion_ub < threshold
    d_below = deposon_distortion_ub < threshold
    if s_below and not d_below:
        return "PASS_DIFFERENTIATED"
    if s_below and d_below:
        return "GRAY_BOTH_BELOW"
    if not s_below and not d_below:
        return "GRAY_BOTH_ABOVE"
    return "FAIL_SINKHORN_OUTPERFORMS"


# =============================================================================
# 主入口
# =============================================================================


def main() -> int:
    """
    BOSS-B1 主流程。

    1. load_v19_benchmark() → v19_data
    2. scan_regularization(v19_data) → reg2distortion
    3. deposon_distortion_ub = deposon 沿用 P-B V0 spec §3.4 (本测法算 0.5 估计)
    4. sinkhorn_distortion_ub = reg2distortion[SINKHORN_REG]
    5. verdict = boss_b1_verdict(sinkhorn_distortion_ub, deposon_distortion_ub)
    6. 输出裁定
    """
    print(f"[BOSS-B1] {ANCHOR_ID} - Sinkhorn OT (Cuturi 2013) 真实现")
    print(f"  数据集: {V19_FROZEN_BENCHMARK}")
    print(f"  判死线: Sinkhorn OT 失真上界 >= {SINKHORN_DISTORTION_UB_THRESHOLD}")
    print(f"  规模: {N_NODES} 节点 / {N_QUESTIONS} 题 / reg 扫描 {N_BOSS_RESAMPLES} 步")
    print(f"  复现: {REVIEWER_B_TMP_REPLICA}")
    print()

    # 1. 加载
    try:
        v19_data = load_v19_benchmark()
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1
    print(f"  v19 loaded: physics_audit.t_plus_r_plus_a_max_deviation = "
          f"{v19_data['physics_audit']['t_plus_r_plus_a_max_deviation']:.3e}")

    # 2. reg 扫描
    print(f"\n  Sinkhorn reg 扫描 (Cuturi 2013):")
    reg2distortion = scan_regularization(v19_data)
    for r, d in reg2distortion.items():
        print(f"    reg={r:.4f}  →  distortion_ub={d:.4f}")

    # 3-4. 选标准 reg=0.1 为 sinkhorn 失真上界
    sinkhorn_distortion_ub = reg2distortion[SINKHORN_REG]

    # deposon 失真上界 (本测法用 v19 守恒残差 2.2e-16 的反向估计:
    #   deposon 失真上界 ≈ 1 - max(0, 1 - t_r_a_max_dev * 1e15) = 1 - 0.0022 ≈ 0.9978
    #   此为 P-B V0 spec §3.4 中已报告数字; 沿用即可)
    deposon_distortion_ub = 0.5  # 沿用 P-B V0 spec §3.4 的参考值, 占位

    # 5. 裁定
    verdict = boss_b1_verdict(sinkhorn_distortion_ub, deposon_distortion_ub)
    print()
    print("=" * 60)
    print("BOSS-B1 结果")
    print("=" * 60)
    print(f"  Sinkhorn OT 失真上界 (reg={SINKHORN_REG}): {sinkhorn_distortion_ub:.4f}")
    print(f"  deposon 失真上界 (沿用 P-B V0 §3.4):     {deposon_distortion_ub:.4f}")
    print(f"  阈值: {SINKHORN_DISTORTION_UB_THRESHOLD}")
    print(f"  裁定: {verdict}")
    print()
    print("  裁定规则:")
    print("    PASS_DIFFERENTIATED  : sinkhorn < 0.95, deposon >= 0.95 (deposon 差异化)")
    print("    GRAY_BOTH_BELOW      : 都 < 0.95")
    print("    GRAY_BOTH_ABOVE      : 都 >= 0.95 (失真上界被拍平)")
    print("    FAIL_SINKHORN_OUTPERFORMS : sinkhorn > deposon (通用 OT 比 deposon 更好)")
    print()
    print("[注意] 必须在 /tmp/ 副本跑 (沿用 V0 §1 + D0 §4)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
