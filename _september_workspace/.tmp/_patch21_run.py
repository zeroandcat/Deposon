"""V5 #21 副本补丁棒 · 适配后锚版口径读数驱动。

读数口径：**适配后读数（.tmp 副本 + 兼容补丁），非原样锚版读数**。
- 锚版本体 0 触动：本驱动只 load .tmp 副本，不碰 D:/私人资料/_non_upload_local_archive
- Python 3.14：load_module 已移除 -> SourceFileLoader 显式 loader（沿用上棒）
- 0 LLM / 0 proxy / 0 gateway / 0 key 读取 / 0 网络

用法: python _patch21_run.py <b1|b2|b3> <semA_none_default|semB_none_skip>
"""

import hashlib
import json
import sys
import time
from importlib.machinery import SourceFileLoader
from importlib.util import spec_from_loader, module_from_spec

OUT_DIR = r"D:/私人资料/deposon-repo/.tmp"
V19 = "results/deposon_v19_benchmark_fixes.json"

BOSS_FILE = {
    "b1": "_v5_item21_patched_b1_{sem}.py",
    "b2": "_v5_item21_patched_b2_{sem}.py",
    "b3": "_v5_item21_patched_b3_{sem}.py",
}


def sha12_file(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def load(name, path):
    loader = SourceFileLoader(name, path)
    spec = spec_from_loader(name, loader)
    mod = module_from_spec(spec)
    loader.exec_module(mod)
    return mod


def main():
    boss = sys.argv[1]
    sem = sys.argv[2]
    path = f"{OUT_DIR}/" + BOSS_FILE[boss].format(sem=sem)
    mod_name = f"patched_{boss}_{sem}"
    m = load(mod_name, path)

    out = {
        "boss": boss,
        "semantic": sem,
        "patched_file": path.rsplit("/", 1)[-1],
        "patched_sha12": sha12_file(path),
        "input_v19_sha12": sha12_file(V19),
        "reading_kind": "适配后读数（非原样锚版读数）",
    }

    d = m.load_v19_benchmark(V19)

    if boss == "b1":
        qs = m._extract_200_questions(d)
        out["questions_extracted"] = len(qs)
        out["vocab_size"] = len(m._build_vocabulary(qs))
        out["questions_empty_best_path"] = sum(
            1 for q in qs if not q.get("best_path"))
        out["questions_predicted_zero"] = sum(
            1 for q in qs if q.get("predicted") == 0.0)
        out["questions_answer_zero"] = sum(
            1 for q in qs if q.get("answer") == 0.0)
        out["questions_predicted_negative"] = sum(
            1 for q in qs if q.get("predicted", 0.0) < 0)
        t = time.time()
        v = m.compute_distortion_upper_bound(d, reg=0.1)
        out["sinkhorn_distortion_ub_reg_0p1"] = v
        out["elapsed_s"] = round(time.time() - t, 2)
        out["threshold"] = m.SINKHORN_DISTORTION_UB_THRESHOLD
        out["script_declared_n_questions"] = m.N_QUESTIONS
    elif boss == "b2":
        t = time.time()
        ts = m.sample_teacher_distribution(d)
        out["teacher_questions"] = len(ts)
        out["samples_per_question"] = len(ts[0]) if ts else 0
        st = m.train_kd_student(ts)
        v = m.compute_kd_distortion_upper_bound(st, d)
        out["kd_distortion_ub"] = v
        out["elapsed_s"] = round(time.time() - t, 2)
        out["threshold"] = m.KD_DISTORTION_UB_THRESHOLD
    else:
        t = time.time()
        op = m.build_prompts(d)
        out["prompt_groups"] = len(op)
        out["prompts_per_group"] = len(op[0]) if op else 0
        flat = [p for ps in op for p in ps]
        out["prompts_flat"] = len(flat)
        cf = m.compress_with_llmlingua(
            flat, target_ratio=m.LLMLINGUA_TARGET_COMPRESSION_RATIO)
        cp, idx = [], 0
        for ps in op:
            cp.append(cf[idx:idx + len(ps)])
            idx += len(ps)
        v = m.compute_llmlingua_distortion(op, cp, d)
        out["llmlingua_distortion"] = v
        out["elapsed_s"] = round(time.time() - t, 2)
        out["threshold"] = m.LLMLINGUA_DISTORTION_THRESHOLD
        out["target_compression_ratio"] = m.LLMLINGUA_TARGET_COMPRESSION_RATIO

    print("###JSON###" + json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
