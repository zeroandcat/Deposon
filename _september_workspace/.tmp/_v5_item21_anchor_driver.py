"""V5 #21 锚版复算驱动（只读执行锚版 3 件，0 字节改动）。

锚版以 .bak 后缀，用 SourceFileLoader 显式指定 loader（Python 3.14 已移除 load_module）。
不 import 任何 LLM/网络/key 相关；纯本地数值。
"""
import hashlib
import json
import sys
import time
from importlib.machinery import SourceFileLoader
from importlib.util import spec_from_loader, module_from_spec

ANCHOR_DIR = r"D:/私人资料/_non_upload_local_archive/scripts/scripts/kt_b1"
V19 = "results/deposon_v19_benchmark_fixes.json"


def sha12(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()[:12]


def load(name, path):
    loader = SourceFileLoader(name, path)
    spec = spec_from_loader(name, loader)
    mod = module_from_spec(spec)
    loader.exec_module(mod)
    return mod


def main():
    which = sys.argv[1]
    out = {}

    if which == "b1count":
        m = load("boss_b1_anchor", f"{ANCHOR_DIR}/boss_b1_sinkhorn_ot.py.bak")
        d = m.load_v19_benchmark(V19)
        qs = m._extract_200_questions(d)
        out["questions_extracted"] = len(qs)
        out["vocab_size"] = len(m._build_vocabulary(qs))
        out["questions_empty_best_path"] = sum(1 for q in qs if not q.get("best_path"))
        out["questions_predicted_zero"] = sum(1 for q in qs if q.get("predicted") == 0.0)
        out["questions_answer_zero"] = sum(1 for q in qs if q.get("answer") == 0.0)
    elif which == "b1":
        m = load("boss_b1_anchor", f"{ANCHOR_DIR}/boss_b1_sinkhorn_ot.py.bak")
        d = m.load_v19_benchmark(V19)
        qs = m._extract_200_questions(d)
        out["questions_extracted"] = len(qs)
        out["vocab_size"] = len(m._build_vocabulary(qs))
        out["questions_empty_best_path"] = sum(1 for q in qs if not q.get("best_path"))
        out["questions_predicted_zero"] = sum(1 for q in qs if q.get("predicted") == 0.0)
        t = time.time()
        d10 = m.compute_distortion_upper_bound(d, reg=0.1)
        out["sinkhorn_distortion_ub_reg_0p1"] = d10
        out["elapsed_s_reg_0p1"] = round(time.time() - t, 2)
        out["verdict_selfreport"] = m.boss_b1_verdict(d10, 0.5)
        out["threshold"] = m.SINKHORN_DISTORTION_UB_THRESHOLD
        out["deposon_ref_placeholder"] = 0.5
    elif which == "b2":
        m = load("boss_b2_anchor", f"{ANCHOR_DIR}/boss_b2_kd.py.bak")
        d = m.load_v19_benchmark(V19)
        t = time.time()
        ts = m.sample_teacher_distribution(d)
        out["teacher_questions"] = len(ts)
        out["samples_per_question"] = len(ts[0]) if ts else 0
        st = m.train_kd_student(ts)
        v = m.compute_kd_distortion_upper_bound(st, d)
        out["kd_distortion_ub"] = v
        out["elapsed_s"] = round(time.time() - t, 2)
        out["verdict_selfreport"] = m.boss_b2_verdict(v, 0.5)
        out["threshold"] = m.KD_DISTORTION_UB_THRESHOLD
        out["deposon_ref_placeholder"] = 0.5
    elif which == "b3":
        m = load("boss_b3_anchor", f"{ANCHOR_DIR}/boss_b3_llmlingua.py.bak")
        d = m.load_v19_benchmark(V19)
        t = time.time()
        op = m.build_prompts(d)
        out["prompt_questions"] = len(op)
        flat = [p for ps in op for p in ps]
        cf = m.compress_with_llmlingua(flat, target_ratio=m.LLMLINGUA_TARGET_COMPRESSION_RATIO)
        cp, idx = [], 0
        for ps in op:
            cp.append(cf[idx:idx + len(ps)])
            idx += len(ps)
        v = m.compute_llmlingua_distortion(op, cp, d)
        out["llmlingua_distortion"] = v
        out["elapsed_s"] = round(time.time() - t, 2)
        out["verdict_selfreport"] = m.boss_b3_verdict(v, 0.05)
        out["threshold"] = m.LLMLINGUA_DISTORTION_THRESHOLD
        out["deposon_ref_placeholder"] = 0.05
    elif which in ("d2", "d3", "d1"):
        base = {"d1": "boss_b1_sinkhorn_ot.py",
                "d2": "boss_b2_kd.py",
                "d3": "boss_b3_llmlingua.py"}[which]
        m = load("drift_" + which, f"{ANCHOR_DIR}/{base}")
        d = m.load_v19_benchmark(V19)
        if which == "d1":
            qs = m._extract_200_questions(d)
            out["questions_extracted"] = len(qs)
            out["vocab_size"] = len(m._build_vocabulary(qs))
            t = time.time()
            v = m.compute_distortion_upper_bound(d, reg=0.1)
            out["sinkhorn_distortion_ub_reg_0p1"] = v
            out["elapsed_s"] = round(time.time() - t, 2)
        elif which == "d2":
            t = time.time()
            ts = m.sample_teacher_distribution(d)
            st = m.train_kd_student(ts)
            v = m.compute_kd_distortion_upper_bound(st, d)
            out["kd_distortion_ub"] = v
            out["elapsed_s"] = round(time.time() - t, 2)
        else:
            t = time.time()
            op = m.build_prompts(d)
            flat = [p for ps in op for p in ps]
            cf = m.compress_with_llmlingua(
                flat, target_ratio=m.LLMLINGUA_TARGET_COMPRESSION_RATIO)
            cp, idx = [], 0
            for ps in op:
                cp.append(cf[idx:idx + len(ps)])
                idx += len(ps)
            v = m.compute_llmlingua_distortion(op, cp, d)
            out["llmlingua_distortion"] = v
            out["elapsed_s"] = round(time.time() - t, 2)
    else:
        raise SystemExit("unknown target")

    print("###JSON###" + json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
