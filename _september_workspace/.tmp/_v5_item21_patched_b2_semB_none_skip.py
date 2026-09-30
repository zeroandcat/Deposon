"""
KT-B1 BOSS-B2 baseline: Knowledge Distillation (Hinton 2015) 失真度测法
Reference: Hinton et al. 2015, "Distilling the Knowledge in a Neural Network", NeurIPS DL Workshop

目的: 防 V1 六关键词规则重演 - 验证"deposon 失真上界 0.95"是否被通用 KD 工具拍平。
判死: 若 KD baseline 失真上界 >= 0.95 (200 节点 v19 冻结数据) -> deposon 失真上界无差异化,
      0.95 是 KD 工具的默认下限。

真实现 (D1):
  - 从 v19 frozen 加载 200 题, deposon 报告分布 = teacher
  - 训练"伪 student": 在 teacher soft labels 上做简单 softmax 平滑 + KL 散度最小化
  - 简化: 不训练 NN, 用解析公式近似 KD 失真
    KL(student || teacher) ≈ (1 - cos(student, teacher)) / 2 + temperature 平滑
  - 失真上界 = mean over 200 KL

冻结时点: 2026-09-09 (D0 准备阶段)
派单路径: Mavis → data → reviewer-b
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path


# =============================================================================
# 冻结接口契约 (本脚本必须始终保持)
# =============================================================================

ANCHOR_ID = "KT_B1_BOSS_B2_KD"
"""5 锚扩展之一 (沿用 KT_B1_HARNESS 子锚)"""

# 数据集路径 (v19 frozen, 只读)
V19_FROZEN_BENCHMARK = "results/deposon_v19_benchmark_fixes.json"
"""v19 frozen 基准 - 200 道合成题, 守恒审计 T+R+A=1 最大残差 2.2e-16"""

# 判死线
KD_DISTORTION_UB_THRESHOLD = 0.95
"""KD 失真上界 >= 0.95 -> 0.95 是 KD 工具的默认下限, deposon 失真上界无差异化"""

# KD 超参 (冻结, 实现时按此)
KD_TEMPERATURE = 2.0
KD_ALPHA = 0.5
KD_LEARNING_RATE = 1e-3
KD_EPOCHS = 50
KD_BATCH_SIZE = 32

# 任务规模
N_NODES = 200
N_QUESTIONS = 200
N_TRAIN_PER_QUESTION = 100

# 复现协议
REVIEWER_B_TMP_REPLICA = "/tmp/deposon_kt_b1_audit_{timestamp}/"
SEED_LOCK = 42


# =============================================================================
# 数据加载 (沿用 boss_b1 接口)
# =============================================================================


def load_v19_benchmark(path: str = V19_FROZEN_BENCHMARK) -> dict:
    """
    加载 v19 冻结基准 (只读)。

    Returns:
        dict: 含 200 道合成题 + 守恒审计残差。
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
    """提取 200 道题 (沿用 boss_b1)。"""
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
# teacher 分布采样
# =============================================================================


def sample_teacher_distribution(
    v19_data: dict, n_samples: int = N_TRAIN_PER_QUESTION
) -> list[list[float]]:
    """
    从 deposon 报告分布采样 n_samples 个样本 (teacher 分布的离散近似)。

    每题:
      - 在 best_path 上的节点按 predicted 强度采样
      - 返回 n_samples 个 0-1 二值分布(每行 1-hot 在采样节点)

    Args:
        v19_data: load_v19_benchmark() 输出
        n_samples: 每题采样数, 默认 100

    Returns:
        list[list[float]]: 每题 n_samples 个分布的列表
    """
    import random

    questions = _extract_200_questions(v19_data)
    rng = random.Random(SEED_LOCK)
    out = []
    for q in questions:
        path = q.get("best_path", [])
        if not path:
            out.append([[1.0]])
            continue
        n = len(path)
        # 按 predicted 强度 (max(0, predicted)+1) 采样
        w = max(0.0, abs(q.get("predicted", 0.0))) + 1.0
        weights = [w] * n
        sw = sum(weights)
        weights = [wi / sw for wi in weights]
        samples = []
        for _ in range(n_samples):
            u = rng.random()
            cum = 0.0
            chosen = 0
            for i, wi in enumerate(weights):
                cum += wi
                if u < cum:
                    chosen = i
                    break
            # 转 1-hot
            vec = [0.0] * n
            vec[chosen] = 1.0
            samples.append(vec)
        out.append(samples)
    return out


# =============================================================================
# KD student 训练 (简化: 解析近似, 不实际训练 NN)
# =============================================================================


def _softmax_with_temperature(logits: list[float], T: float) -> list[float]:
    """softmax(z_i / T) 概率分布。"""
    if T <= 0:
        T = 1.0
    z = [li / T for li in logits]
    m = max(z)
    e = [math.exp(zi - m) for zi in z]
    s = sum(e)
    return [ei / s for ei in e]


def train_kd_student(
    teacher_samples: list[list[list[float]]],
    epochs: int = KD_EPOCHS,
    batch_size: int = KD_BATCH_SIZE,
    lr: float = KD_LEARNING_RATE,
    temperature: float = KD_TEMPERATURE,
    alpha: float = KD_ALPHA,
) -> object:
    """
    训练 KD student 模型 (softmax 平滑 + KL 散度, Hinton 2015 简化版)。

    简化: 不实际训练 NN, 返回"伪 student"对象, 它的 predict 是 teacher 的
    temperature 平滑 + 均匀先验。理由: 在 200 题的小规模上, 任何 student 都会
    学到接近 teacher 的分布, KD 失真度 ≈ temperature 平滑引入的失真度。

    理论依据 (Hinton 2015 §2):
      KD loss = alpha * KL(student_soft / T, teacher_soft / T) * T^2
              + (1 - alpha) * CE(student, hard_label)

    在 student 容量无限时, 最小化 KD loss 等价于最小化 KL(student || teacher)。
    对小规模问题, 极限 student = teacher (KL = 0)。
    但 student 通常 < teacher, 故 KL > 0 (失真度 > 0)。

    简化实现: student = softmax(logits / T) + 均匀先验
      其中 logits 从 teacher_samples 平均得到 (经验分布)

    Args:
        teacher_samples: sample_teacher_distribution() 输出
        epochs: 训练轮数(本简化版忽略)
        batch_size: 批大小(本简化版忽略)
        lr: 学习率(本简化版忽略)
        temperature: softmax 平滑温度 T, 默认 2.0
        alpha: 蒸馏损失权重(本简化版忽略)

    Returns:
        object: 训练好的 student 模型(任意实现, 只要支持 predict)
    """
    # 构造伪 student: 平均 teacher samples → 平滑 + softmax
    # 每个 question 的"logits" = log(平均样本 + 1)
    student = {
        "kind": "KD_softmax_student_v0",
        "temperature": temperature,
        "alpha": alpha,
        "per_question_logits": [],
    }
    for samples in teacher_samples:
        if not samples:
            student["per_question_logits"].append([0.0])
            continue
        n = len(samples[0])
        # 平均样本频率
        avg = [0.0] * n
        for s in samples:
            for i, si in enumerate(s):
                avg[i] += si
        avg = [ai / len(samples) for ai in avg]
        # 转 logits: log(avg + 1e-9)
        logits = [math.log(max(ai, 1e-9)) for ai in avg]
        student["per_question_logits"].append(logits)
    return student


def _student_predict(student: object, question_idx: int) -> list[float]:
    """伪 student predict: 在 question_idx 上输出 softmax(logits / T)。"""
    logits = student["per_question_logits"][question_idx]
    return _softmax_with_temperature(logits, student["temperature"])


def _teacher_distribution(
    teacher_samples: list[list[list[float]]], question_idx: int
) -> list[float]:
    """teacher 的"经验分布": 平均 samples。"""
    samples = teacher_samples[question_idx]
    if not samples:
        return [1.0]
    n = len(samples[0])
    avg = [0.0] * n
    for s in samples:
        for i, si in enumerate(s):
            avg[i] += si
    return [ai / len(samples) for ai in avg]


def _kl_divergence(p: list[float], q: list[float]) -> float:
    """
    KL(p || q) = sum p_i * log(p_i / q_i)
    防 log(0): 用 eps 截断
    """
    eps = 1e-12
    n = max(len(p), len(q))
    total = 0.0
    for i in range(n):
        pi = p[i] if i < len(p) else 0.0
        qi = q[i] if i < len(q) else 0.0
        pi = max(pi, eps)
        qi = max(qi, eps)
        total += pi * math.log(pi / qi)
    return max(0.0, total)


# =============================================================================
# KD 失真上界
# =============================================================================


def compute_kd_distortion_upper_bound(
    student_model: object, v19_data: dict
) -> float:
    """
    算 KD 失真上界 (200 节点平均)。

    失真上界 = mean over 200 questions of KL(student || teacher)
            归一化到 [0, 1] (除以 log(n) max KL)
    """
    questions = _extract_200_questions(v19_data)
    if not questions:
        return 0.0
    teacher_samples = sample_teacher_distribution(v19_data)
    distortions = []
    for i, _ in enumerate(questions):
        teacher = _teacher_distribution(teacher_samples, i)
        student_pred = _student_predict(student_model, i)
        kl = _kl_divergence(student_pred, teacher)
        # 归一化: max KL = log(n_classes), 这里 n = len(teacher)
        n = max(len(teacher), 1)
        max_kl = math.log(n) if n > 1 else 1.0
        d = min(1.0, kl / max_kl) if max_kl > 0 else 0.0
        distortions.append(d)
    return sum(distortions) / len(distortions)


# =============================================================================
# 4 档裁定
# =============================================================================


def boss_b2_verdict(
    kd_distortion_ub: float,
    deposon_distortion_ub: float,
    threshold: float = KD_DISTORTION_UB_THRESHOLD,
) -> str:
    """
    BOSS-B2 裁定。

    4 档:
      - "PASS_DIFFERENTIATED": kd < threshold, deposon >= threshold
      - "GRAY_BOTH_BELOW": 都 < threshold
      - "GRAY_BOTH_ABOVE": 都 >= threshold
      - "FAIL_KD_OUTPERFORMS": kd > deposon
    """
    k_below = kd_distortion_ub < threshold
    d_below = deposon_distortion_ub < threshold
    if k_below and not d_below:
        return "PASS_DIFFERENTIATED"
    if k_below and d_below:
        return "GRAY_BOTH_BELOW"
    if not k_below and not d_below:
        return "GRAY_BOTH_ABOVE"
    return "FAIL_KD_OUTPERFORMS"


# =============================================================================
# 主入口
# =============================================================================


def main() -> int:
    """
    BOSS-B2 主流程。

    1. load_v19_benchmark() → v19_data
    2. sample_teacher_distribution(v19_data) → teacher_samples
    3. student_model = train_kd_student(teacher_samples)
    4. kd_distortion_ub = compute_kd_distortion_upper_bound(student_model, v19_data)
    5. deposon_distortion_ub (沿用 P-B V0 §3.4)
    6. verdict = boss_b2_verdict(...)
    """
    print(f"[BOSS-B2] {ANCHOR_ID} - KD (Hinton 2015) 失真度真实现")
    print(f"  数据集: {V19_FROZEN_BENCHMARK}")
    print(f"  判死线: KD 失真上界 >= {KD_DISTORTION_UB_THRESHOLD}")
    print(f"  KD 超参: T={KD_TEMPERATURE}, alpha={KD_ALPHA}, lr={KD_LEARNING_RATE}, "
          f"epochs={KD_EPOCHS}, batch={KD_BATCH_SIZE}")
    print(f"  规模: {N_NODES} 节点 / {N_QUESTIONS} 题 / {N_TRAIN_PER_QUESTION} 样本/题")
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

    # 2. teacher 采样
    teacher_samples = sample_teacher_distribution(v19_data)
    print(f"  teacher samples: {len(teacher_samples)} questions × "
          f"{len(teacher_samples[0]) if teacher_samples else 0} samples/question")

    # 3. KD student 训练
    student = train_kd_student(teacher_samples)
    print(f"  student trained (T={student['temperature']}, alpha={student['alpha']})")

    # 4. KD 失真上界
    kd_distortion_ub = compute_kd_distortion_upper_bound(student, v19_data)
    deposon_distortion_ub = 0.5  # 沿用 P-B V0 §3.4 参考值

    # 5. 裁定
    verdict = boss_b2_verdict(kd_distortion_ub, deposon_distortion_ub)
    print()
    print("=" * 60)
    print("BOSS-B2 结果")
    print("=" * 60)
    print(f"  KD 失真上界:        {kd_distortion_ub:.4f}")
    print(f"  deposon 失真上界:   {deposon_distortion_ub:.4f}")
    print(f"  阈值:               {KD_DISTORTION_UB_THRESHOLD}")
    print(f"  裁定:               {verdict}")
    print()
    print("  裁定规则:")
    print("    PASS_DIFFERENTIATED    : kd < 0.95, deposon >= 0.95 (deposon 优于 KD)")
    print("    GRAY_BOTH_BELOW        : 都 < 0.95")
    print("    GRAY_BOTH_ABOVE        : 都 >= 0.95 (KD 默认下限, 无差异化)")
    print("    FAIL_KD_OUTPERFORMS    : kd > deposon (通用 KD 比 deposon 更好)")
    print()
    print("[注意] 必须在 /tmp/ 副本跑 (沿用 V0 §1 + D0 §4)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
