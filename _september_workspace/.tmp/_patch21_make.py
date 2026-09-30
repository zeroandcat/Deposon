"""V5 #21 副本补丁棒 · 补丁生成器。

铁律：锚版 3 件只读复制到 .tmp/ 副本打补丁；锚版本体 0 字节触动。
产出：
  .tmp/_v5_item21_patched_<boss>_<sem>.py   6 件（3 BOSS × 2 None 语义）
  .tmp/_v5_item21_patch.diff                补丁 diff 全文（逐行）
补丁三要素（派工单 §三.1）：
  ① None 容错      语义 A = None 视同缺失走默认 0.0（主跑）
                   语义 B = 显式跳过该条（敏感性对照）
  ② 形态回退      predicted→pred（strategyqa）、best_path→path（strategyqa）、
                   answer 缺失走 0.0（strategyqa 实测无 answer 键）
  ③ Python 3.14   load_module 已移除 -> 沿用上棒 SourceFileLoader（在本驱动内，
                   不改锚本体的 import 面；锚本体实测无 load_module 调用）
"""

import difflib
import hashlib
import io
import os

ANCHOR_DIR = r"D:/私人资料/_non_upload_local_archive/scripts/scripts/kt_b1"
OUT_DIR = r"D:/私人资料/deposon-repo/.tmp"
DIFF_PATH = os.path.join(OUT_DIR, "_v5_item21_patch.diff")

BOSSES = [
    ("b1", "boss_b1_sinkhorn_ot.py.bak"),
    ("b2", "boss_b2_kd.py.bak"),
    ("b3", "boss_b3_llmlingua.py.bak"),
]

# 三件共用的锚版抽取块（实测逐字一致：b1:114-118 / b2:95-99 / b3:88-92）
OLD_BLOCK = (
    '            for p in problems:\n'
    '                out.append(\n'
    '                    {\n'
    '                        "id": int(p.get("id", 0)),\n'
    '                        "experiment": "E9.3_high_couple_fix",\n'
    '                        "benchmark": bm_name,\n'
    '                        "condition": cond,\n'
    '                        "predicted": float(p.get("predicted", 0.0)),\n'
    '                        "answer": float(p.get("answer", 0.0)),\n'
    '                        "is_correct": bool(p.get("is_correct", False)),\n'
    '                        "best_path": list(p.get("best_path", [])),\n'
    '                        "trap_hit": p.get("trap_hit", ""),\n'
    '                    }\n'
    '                )\n'
)

HELPERS = '''# =============================================================================
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


'''

ANCHOR_FN = "def _extract_200_questions(v19_data: dict) -> list[dict]:"

# 语义 A：None 视同缺失走默认 0.0（主跑）
NEW_BLOCK_A = (
    '            for p in problems:\n'
    '                # [PATCH ①②] v19 双形态: pred 键(strategyqa) / predicted 键(gsm8k)\n'
    '                _raw_pred = p.get("pred", p.get("predicted", 0.0))\n'
    '                # [PATCH ① 语义A] None 视同缺失, 走默认 0.0（保留该条）\n'
    '                out.append(\n'
    '                    {\n'
    '                        "id": int(p.get("id", 0)),\n'
    '                        "experiment": "E9.3_high_couple_fix",\n'
    '                        "benchmark": bm_name,\n'
    '                        "condition": cond,\n'
    '                        "predicted": _patch_norm_pred(_raw_pred),\n'
    '                        "answer": _patch_to_float(p.get("answer", 0.0)),\n'
    '                        "is_correct": bool(p.get("is_correct", False)),\n'
    '                        # [PATCH ②] best_path 键(gsm8k) / path 键(strategyqa)\n'
    '                        "best_path": list(p.get("best_path", p.get("path", []))),\n'
    '                        "trap_hit": p.get("trap_hit", ""),\n'
    '                    }\n'
    '                )\n'
)

# 语义 B：None 显式跳过该条（敏感性对照）
NEW_BLOCK_B = (
    '            for p in problems:\n'
    '                # [PATCH ①②] v19 双形态: pred 键(strategyqa) / predicted 键(gsm8k)\n'
    '                _raw_pred = p.get("pred", p.get("predicted", 0.0))\n'
    '                # [PATCH ① 语义B] None 显式跳过该条（不计入题集）\n'
    '                if _raw_pred is None:\n'
    '                    continue\n'
    '                out.append(\n'
    '                    {\n'
    '                        "id": int(p.get("id", 0)),\n'
    '                        "experiment": "E9.3_high_couple_fix",\n'
    '                        "benchmark": bm_name,\n'
    '                        "condition": cond,\n'
    '                        "predicted": _patch_norm_pred(_raw_pred),\n'
    '                        "answer": _patch_to_float(p.get("answer", 0.0)),\n'
    '                        "is_correct": bool(p.get("is_correct", False)),\n'
    '                        # [PATCH ②] best_path 键(gsm8k) / path 键(strategyqa)\n'
    '                        "best_path": list(p.get("best_path", p.get("path", []))),\n'
    '                        "trap_hit": p.get("trap_hit", ""),\n'
    '                    }\n'
    '                )\n'
)

SEMANTICS = [("semA_none_default", NEW_BLOCK_A), ("semB_none_skip", NEW_BLOCK_B)]


def sha12_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:12]


def sha12_file(p: str) -> str:
    with open(p, "rb") as f:
        return sha12_bytes(f.read())


def main():
    report = {"generated": [], "anchor_sha12": {}}
    diff_buf = io.StringIO()

    for key, fname in BOSSES:
        src = os.path.join(ANCHOR_DIR, fname)
        with open(src, "r", encoding="utf-8", newline="") as f:
            original = f.read()
        report["anchor_sha12"][key] = {
            "file": fname,
            "sha12": sha12_file(src),
            "bytes": os.path.getsize(src),
        }

        for sem_name, new_block in SEMANTICS:
            assert original.count(OLD_BLOCK) == 1, (
                f"{key}/{sem_name}: anchor block not uniquely found "
                f"(count={original.count(OLD_BLOCK)})"
            )
            assert original.count(ANCHOR_FN) == 1, (
                f"{key}/{sem_name}: _extract_200_questions not unique")

            patched = original.replace(OLD_BLOCK, new_block)
            patched = patched.replace(ANCHOR_FN, HELPERS + ANCHOR_FN, 1)

            dst = os.path.join(OUT_DIR, f"_v5_item21_patched_{key}_{sem_name}.py")
            # LF 保持（锚版本体实测 0 CRLF，纯 LF）
            with open(dst, "w", encoding="utf-8", newline="") as f:
                f.write(patched)

            report["generated"].append({
                "boss": key,
                "semantic": sem_name,
                "out": os.path.basename(dst),
                "sha12": sha12_file(dst),
                "bytes": os.path.getsize(dst),
            })

            diff_buf.writelines(difflib.unified_diff(
                original.splitlines(keepends=True),
                patched.splitlines(keepends=True),
                fromfile=f"ANCHOR/{fname}",
                tofile=f"PATCHED/.tmp/_v5_item21_patched_{key}_{sem_name}.py",
                n=3,
            ))
            diff_buf.write(
                f"###PATCH-END### {key}/{sem_name} "
                f"orig_bytes={len(original.encode('utf-8'))} "
                f"patched_bytes={len(patched.encode('utf-8'))}\n")

    with open(DIFF_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(diff_buf.getvalue())

    report["diff_file"] = os.path.basename(DIFF_PATH)
    report["diff_sha12"] = sha12_file(DIFF_PATH)
    report["diff_bytes"] = os.path.getsize(DIFF_PATH)
    print("###PATCHGEN###")
    import json
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
