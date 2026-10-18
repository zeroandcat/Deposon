#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================
# Deposon SPEC v1.9 Part B — 基准侧修正与对照实验 (E9.3/E9.4/E9.5)
#
# E9.3 high_couple 别名真修复: 默认 mode='high_couple' 真实放大 g_couple
#      耦合路径; v1.4 旧别名仅在 DEPOSON_V14_HIGH_COUPLE_ALIAS=1 下复现。
# E9.4 等权诱饵中性对照: 所有边权拉平为 FLAT_WEIGHT, 重跑 no_deposon/unified。
# E9.5 规则基线: 纯规则标签关键词过滤 (无 LLM), 与 LLM 先验臂对比。
#
# no LLM API calls issued; inputs read from cache (sha256 on record).
# 缓存缺失 -> CacheMissingError, 显式失败, 绝不伪造数据。
# 输出: results/deposon_v19_benchmark_fixes.json
# ============================================================
import os
import sys
import json
import math
import random
import hashlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

os.environ.pop('KIMI_API_KEY', None)  # 硬约束: 本进程不存在任何 API key

from deposon_agents_v1_4 import (KimiLLMBackend, DeposonAgentSystem,
                                 BenchmarkEvaluator, DeposonField,
                                 resolve_high_couple_config, HIGH_COUPLE_GAIN)

REPO = os.path.dirname(os.path.abspath(__file__))
OUT = "/mnt/agents/output"
CACHE_DIR = os.path.join(OUT, "deposon_cache")
CACHE_VERSION = "1.3.0"
GSM8K_SAMPLE_FILE = os.path.join(OUT, "gsm8k_sample100_seed42.json")
STRATEGYQA_FILE = os.path.join(OUT, "strategyqa_train.json")
RESULT_FILE = os.path.join(REPO, "results", "deposon_v19_benchmark_fixes.json")

SEED = 42
FLAT_WEIGHT = 0.7          # E9.4: 等权常数 (SPEC v1.9 Part B)
RULE_KEYWORDS = ("trap", "dead", "end", "impossible", "guess", "wrong")  # E9.5


class CacheMissingError(RuntimeError):
    """所需 LLM 缓存缺失: 显式失败 (禁止伪造数据 / 禁止触发 API)。"""


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


class Provenance:
    """记录每个被读取的输入/缓存文件的 sha256。"""

    def __init__(self):
        self.files = {}

    def record(self, path: str):
        if path not in self.files:
            if not os.path.exists(path):
                raise CacheMissingError(f"输入文件缺失: {path}")
            self.files[path] = sha256_file(path)

    def as_dict(self):
        return dict(sorted(self.files.items()))


def make_offline_backend() -> KimiLLMBackend:
    """构造仅缓存后端: 无 key, 任何缓存缺失在调用前即被拦截。"""
    llm = KimiLLMBackend(api_key=None, cache_dir=CACHE_DIR,
                         cache_version=CACHE_VERSION)
    if llm.api_key:
        raise RuntimeError("offline 后端不得持有 API key")
    return llm


def _cache_file(llm: KimiLLMBackend, key: str) -> str:
    return os.path.join(llm.cache.version_dir,
                        f"{hashlib.md5(key.encode()).hexdigest()}.json")


def offline_decompose_math(llm, question, prov: Provenance):
    """GSM8K: 复刻 KimiLLMBackend.decompose 的缓存查找序, 缺失即抛错。"""
    keys = [llm._cache_key("decompose_mini", question),
            llm._cache_key("decompose", question)] + \
        [llm._legacy_cache_key("decompose", question, pv)
         for pv in llm.LEGACY_PROMPT_VERSIONS]
    for k in keys:
        cached = llm.cache.get(k)
        if cached is not None and cached.get("source") == "kimi_api":
            prov.record(_cache_file(llm, k))
            break
    else:
        raise CacheMissingError(
            f"GSM8K decompose 缓存缺失 (source=kimi_api): {question[:60]}...")
    # 缓存命中已验证, decompose 将走纯缓存路径, 不会触及 _chat
    result = llm.decompose(question)
    if result.get("source") != "kimi_api":
        raise CacheMissingError("decompose 非缓存来源, 拒绝使用降级结果")
    return result


def offline_decompose_yesno(llm, question, prov: Provenance):
    key = llm._cache_key("decompose_yesno", question)
    cached = llm.cache.get(key)
    if cached is None:
        raise CacheMissingError(
            f"StrategyQA decompose_yesno 缓存缺失: {question[:60]}...")
    prov.record(_cache_file(llm, key))
    return cached


# ---------------------------------------------------------------- 样本
def load_gsm8k_sample(prov: Provenance):
    prov.record(GSM8K_SAMPLE_FILE)
    with open(GSM8K_SAMPLE_FILE, encoding="utf-8") as f:
        return json.load(f)


def load_strategyqa_sample(prov: Provenance, n=100, seed=SEED):
    prov.record(STRATEGYQA_FILE)
    with open(STRATEGYQA_FILE, encoding="utf-8") as f:
        data = json.load(f)["examples"]
    rng = random.Random(seed)
    picked = rng.sample(data, n)
    sample = []
    for i, ex in enumerate(picked):
        gold = "Yes" if ex["target_scores"].get("Yes", 0) == 1 else "No"
        sample.append({"id": i + 1, "question": ex["input"].strip(),
                       "answer": gold})
    return sample


# ---------------------------------------------------------------- 统计
def mcnemar(correct_a, correct_b):
    """精确双侧 McNemar (与 v1.4 runner 同口径)"""
    b = sum(1 for x, y in zip(correct_a, correct_b) if x and not y)
    c = sum(1 for x, y in zip(correct_a, correct_b) if not x and y)
    n = b + c
    if n == 0:
        return {"b": b, "c": c, "p_value": 1.0}
    k = min(b, c)
    p = sum(math.comb(n, i) for i in range(0, k + 1)) / (2 ** (n - 1))
    return {"b": b, "c": c, "p_value": min(1.0, p)}


def physics_audit():
    import numpy as np
    from deposon_agents_v1_4 import DeposonState
    d = DeposonState(id="audit", center=np.zeros(4), g_couple=1.0,
                     g_aether=0.3, resonance_energy=0.2)
    worst = max(abs(sum(d.scatter(e).values()) - 1.0)
                for e in [0.0, 0.1, 0.5, 1.0, 3.7])
    return {"t_plus_r_plus_a_max_deviation": worst,
            "tolerance": 1e-6, "passed": worst < 1e-6}


# ---------------------------------------------------------------- GSM8K 物理重跑
def reason_with_graph(agent, brain_graph, n_candidates=10):
    """复刻 DeposonAgentSystem.reason, 但使用调用方提供的 (可改权) 图。"""
    if agent.use_deposon:
        agent.field = DeposonField(feature_dim=agent.field.feature_dim)
        agent.field.spawn_from_graph(brain_graph, mode=agent.mode)
    candidates = agent._generate_paths(brain_graph, n_candidates * 3)
    processed = agent._process_sequential(candidates)
    processed.sort(key=lambda x: x["final_score"], reverse=True)
    passed = [c for c in processed if c["passed"]]
    return {"brain_graph": brain_graph, "all_candidates": processed,
            "passed_candidates": passed,
            "best_path": passed[0]["path"] if passed else None,
            "deposon_stats": agent.field.get_stats() if agent.use_deposon
            else {"ether_dissipated": 0.0}}


def flatten_graph_weights(brain_graph, weight=FLAT_WEIGHT):
    """E9.4: 所有边 (含陷阱边) 权重拉平; migration_barrier 不动。"""
    edges = {k: dict(v) for k, v in brain_graph["edges"].items()}
    for attrs in edges.values():
        attrs["weight"] = weight
    g = dict(brain_graph)
    g["edges"] = edges
    return g


def eval_math_question(llm, entry, mode, use_deposon, prov,
                       flat_weights=False):
    dec = offline_decompose_math(llm, entry["question"], prov)
    agent = DeposonAgentSystem(llm_backend=llm, mode=mode)
    agent.use_deposon = use_deposon
    graph = agent.decomposer.to_brain_graph(dec)
    if flat_weights:
        graph = flatten_graph_weights(graph)
    result = reason_with_graph(agent, graph)
    ev = BenchmarkEvaluator(agent, use_validation=False)
    cands = result["passed_candidates"] or result["all_candidates"]
    best = cands[0] if cands else None
    best_path = best["path"] if best else None
    predicted, op_type, path_hit = ev._compute_answer_from_path(graph, best_path)
    is_correct = (predicted is not None
                  and abs(predicted - entry["answer"]) < 0.01)
    return {"id": entry["id"], "predicted": predicted,
            "answer": entry["answer"], "is_correct": bool(is_correct),
            "best_path": best_path, "trap_hit": path_hit}


def label_hits_rule(node_label: str) -> bool:
    lab = str(node_label).lower()
    return any(kw in lab for kw in RULE_KEYWORDS)


def eval_math_rule_baseline(llm, entry, prov):
    """E9.5: 无物理场; 贪心路径序中丢弃命中关键词标签节点的路径。"""
    dec = offline_decompose_math(llm, entry["question"], prov)
    agent = DeposonAgentSystem(llm_backend=llm, mode="unified")
    agent.use_deposon = False
    graph = agent.decomposer.to_brain_graph(dec)
    paths = agent._generate_paths(graph, 30)
    ordered = [p["path"] for p in paths]
    surviving = [p for p in ordered
                 if not any(label_hits_rule(n) for n in p)]
    filtered_out = len(ordered) - len(surviving)
    best_path = surviving[0] if surviving else (ordered[0] if ordered else None)
    ev = BenchmarkEvaluator(agent, use_validation=False)
    predicted, op_type, path_hit = ev._compute_answer_from_path(graph, best_path)
    is_correct = (predicted is not None
                  and abs(predicted - entry["answer"]) < 0.01)
    return {"id": entry["id"], "predicted": predicted,
            "answer": entry["answer"], "is_correct": bool(is_correct),
            "best_path": best_path, "trap_hit": path_hit,
            "n_paths": len(ordered), "n_filtered": filtered_out}


# ---------------------------------------------------------------- StrategyQA 物理重跑
def build_yesno_graph(dec, flat_weights=False):
    """与 run_benchmark_v1_4_strategyqa.build_yesno_graph 同构。"""
    nodes, edges = {}, {}
    steps = dec["steps"]
    for i, s in enumerate(steps):
        nodes[f"S{i+1}"] = {"energy": 0.3 + i * 0.05, "type": "step", "text": s}
    nodes["Goal"] = {"energy": 0.0, "type": "answer"}
    nodes["Trap_guess"] = {"energy": 0.1, "type": "trap",
                           "trap_type": "surface_guess"}
    for i in range(len(steps) - 1):
        edges[(f"S{i+1}", f"S{i+2}")] = {"weight": 0.7, "migration_barrier": 0.2}
    edges[(f"S{len(steps)}", "Goal")] = {"weight": 0.8, "migration_barrier": 0.2}
    edges[("S1", "Trap_guess")] = {"weight": 0.9, "migration_barrier": 0.1}
    edges[("Trap_guess", "Goal")] = {"weight": 0.55, "migration_barrier": 0.3}
    if flat_weights:
        for attrs in edges.values():
            attrs["weight"] = FLAT_WEIGHT
    return {"nodes": nodes, "edges": edges}


def generate_yesno_paths(nodes, edges, max_paths=30):
    from collections import deque
    start, goal = "S1", "Goal"
    paths, queue = [], deque([(start, [start])])
    while queue and len(paths) < max_paths:
        cur, pth = queue.popleft()
        if cur == goal:
            paths.append(pth)
            continue
        outs = [(v, a.get("weight", 0.5)) for (u, v), a in edges.items()
                if u == cur and (v not in pth or v == goal)]
        outs.sort(key=lambda x: x[1], reverse=True)
        for v, w in outs[:8]:
            queue.append((v, pth + [v]))
    return paths


def eval_yesno_question(dec, gold, mode, use_deposon, flat_weights=False):
    graph = build_yesno_graph(dec, flat_weights=flat_weights)
    paths = generate_yesno_paths(graph["nodes"], graph["edges"])
    if not use_deposon:
        scored = [(p, 1.0) for p in paths]
    else:
        field = DeposonField()
        field.spawn_from_graph(graph, mode=mode)
        scored = [(p, field.process_path(p)["transmitted"]) for p in paths]
    scored.sort(key=lambda x: x[1], reverse=True)
    best = scored[0][0] if scored else None
    trap_hit = best is not None and any("Trap" in n for n in best)
    pred = dec["trap_answer"] if trap_hit else dec["answer"]
    return {"pred": pred, "is_correct": bool(pred == gold),
            "path": best, "trap_hit": trap_hit}


def eval_yesno_rule_baseline(dec, gold):
    graph = build_yesno_graph(dec)
    paths = generate_yesno_paths(graph["nodes"], graph["edges"])
    surviving = [p for p in paths
                 if not any(label_hits_rule(n) for n in p)]
    best = surviving[0] if surviving else (paths[0] if paths else None)
    trap_hit = best is not None and any("Trap" in n for n in best)
    pred = dec["trap_answer"] if trap_hit else dec["answer"]
    return {"pred": pred, "is_correct": bool(pred == gold),
            "path": best, "trap_hit": trap_hit,
            "n_paths": len(paths), "n_filtered": len(paths) - len(surviving)}


def summarize(rows):
    n = len(rows)
    ok = sum(1 for r in rows if r["is_correct"])
    return {"n_total": n, "n_correct": ok,
            "accuracy": ok / n if n else 0.0,
            "correct_vector": [bool(r["is_correct"]) for r in rows]}


# ---------------------------------------------------------------- 主流程
def main():
    prov = Provenance()
    llm = make_offline_backend()
    hc_cfg = resolve_high_couple_config()
    assert hc_cfg["mode"] == "high_couple", "默认必须为真修复模式"

    output = {
        "spec_version": "v1.9-part-b",
        "seed": SEED,
        "note": "no LLM API calls issued; inputs read from cache (sha256 on record)",
        "config": {
            "cache_dir": CACHE_DIR, "cache_version": CACHE_VERSION,
            "high_couple_gain": HIGH_COUPLE_GAIN,
            "flat_weight": FLAT_WEIGHT,
            "rule_keywords": list(RULE_KEYWORDS),
            "legacy_alias_env": "DEPOSON_V14_HIGH_COUPLE_ALIAS",
        },
        "physics_audit": physics_audit(),
        "experiments": {},
    }

    gsm8k = load_gsm8k_sample(prov)
    sqa_all = load_strategyqa_sample(prov)

    # ---------------- E9.3: high_couple 真修复, 五臂离线重跑 ----------------
    variants = {
        "no_deposon": {"mode": "unified", "use_deposon": False},
        "v1_blocking": {"mode": "v1_blocking", "use_deposon": True},
        "v2_tunneling": {"mode": "v2_tunneling", "use_deposon": True},
        "unified": {"mode": "unified", "use_deposon": True},
        "high_couple": hc_cfg,
    }
    e93 = {"benchmarks": {}}

    gsm_arms = {}
    for vname, cfg in variants.items():
        rows = [eval_math_question(llm, e, cfg["mode"], cfg["use_deposon"], prov)
                for e in gsm8k]
        gsm_arms[vname] = rows
    gsm_sum = {v: summarize(r) for v, r in gsm_arms.items()}
    same_preds = all(a["is_correct"] == b["is_correct"] and a["predicted"] == b["predicted"]
                     for a, b in zip(gsm_arms["high_couple"], gsm_arms["v1_blocking"]))
    e93["benchmarks"]["gsm8k"] = {
        "n": len(gsm8k),
        "summary": {v: {k: s[k] for k in ("n_total", "n_correct", "accuracy")}
                    for v, s in gsm_sum.items()},
        "high_couple_identical_to_v1_blocking": same_preds,
        "mcnemar_high_couple_vs_v1_blocking": mcnemar(
            gsm_sum["high_couple"]["correct_vector"],
            gsm_sum["v1_blocking"]["correct_vector"]),
        "v1_4_published": {"no_deposon": 0.02, "v1_blocking": 0.86,
                           "v2_tunneling": 0.04, "unified": 0.85,
                           "high_couple": 0.86},
        "per_problem": gsm_arms,
    }

    # StrategyQA: 排除缓存缺失题 (api_blocked), 与 v1.4 同口径
    sqa_rows, sqa_excluded = [], []
    for e in sqa_all:
        try:
            dec = offline_decompose_yesno(llm, e["question"], prov)
        except CacheMissingError:
            sqa_excluded.append({"id": e["id"], "question": e["question"][:80],
                                 "reason": "api_blocked(content_filter)"})
            continue
        sqa_rows.append((e, dec))
    sqa_arms = {v: [] for v in variants}
    for e, dec in sqa_rows:
        for vname, cfg in variants.items():
            r = eval_yesno_question(dec, e["answer"], cfg["mode"],
                                    cfg["use_deposon"])
            r["id"] = e["id"]
            sqa_arms[vname].append(r)
    sqa_sum = {v: summarize(r) for v, r in sqa_arms.items()}
    same_preds_sqa = all(a["pred"] == b["pred"]
                         for a, b in zip(sqa_arms["high_couple"],
                                         sqa_arms["v1_blocking"]))
    e93["benchmarks"]["strategyqa"] = {
        "n": len(sqa_rows), "excluded": sqa_excluded,
        "summary": {v: {k: s[k] for k in ("n_total", "n_correct", "accuracy")}
                    for v, s in sqa_sum.items()},
        "high_couple_identical_to_v1_blocking": same_preds_sqa,
        "mcnemar_high_couple_vs_v1_blocking": mcnemar(
            sqa_sum["high_couple"]["correct_vector"],
            sqa_sum["v1_blocking"]["correct_vector"]),
        "v1_4_published": {"no_deposon": 0.1212, "v1_blocking": 0.8990,
                           "v2_tunneling": 0.2020, "unified": 0.8990,
                           "high_couple": 0.8990},
        "per_problem": sqa_arms,
    }
    e93["verdict_rule"] = ("PASS if high_couple 与 v1_blocking 的预测向量在两个基准上"
                           "均不完全相同 (不再是别名) 且物理守恒审计通过")
    e93["verdict"] = ("PASS" if (not same_preds and not same_preds_sqa
                                 and output["physics_audit"]["passed"]) else "FAIL")
    output["experiments"]["E9.3_high_couple_fix"] = e93

    # ---------------- E9.4: 等权诱饵中性对照 ----------------
    e94 = {"benchmarks": {}}
    flat_arms = {}
    for vname, cfg in {"no_deposon": variants["no_deposon"],
                       "unified": variants["unified"]}.items():
        rows = [eval_math_question(llm, e, cfg["mode"], cfg["use_deposon"],
                                   prov, flat_weights=True)
                for e in gsm8k]
        flat_arms[vname] = rows
    flat_sum = {v: summarize(r) for v, r in flat_arms.items()}
    mc = mcnemar(flat_sum["unified"]["correct_vector"],
                 flat_sum["no_deposon"]["correct_vector"])
    diff = abs(flat_sum["unified"]["accuracy"] - flat_sum["no_deposon"]["accuracy"])
    e94["benchmarks"]["gsm8k"] = {
        "summary": {v: {k: s[k] for k in ("n_total", "n_correct", "accuracy")}
                    for v, s in flat_sum.items()},
        "mcnemar_unified_vs_no_deposon": mc,
        "accuracy_gap": diff, "per_problem": flat_arms,
    }
    sqa_flat = {v: [] for v in ("no_deposon", "unified")}
    for e, dec in sqa_rows:
        for vname, cfg in {"no_deposon": variants["no_deposon"],
                           "unified": variants["unified"]}.items():
            r = eval_yesno_question(dec, e["answer"], cfg["mode"],
                                    cfg["use_deposon"], flat_weights=True)
            r["id"] = e["id"]
            sqa_flat[vname].append(r)
    sqa_flat_sum = {v: summarize(r) for v, r in sqa_flat.items()}
    mc_sqa = mcnemar(sqa_flat_sum["unified"]["correct_vector"],
                     sqa_flat_sum["no_deposon"]["correct_vector"])
    diff_sqa = abs(sqa_flat_sum["unified"]["accuracy"]
                   - sqa_flat_sum["no_deposon"]["accuracy"])
    e94["benchmarks"]["strategyqa"] = {
        "summary": {v: {k: s[k] for k in ("n_total", "n_correct", "accuracy")}
                    for v, s in sqa_flat_sum.items()},
        "mcnemar_unified_vs_no_deposon": mc_sqa,
        "accuracy_gap": diff_sqa, "per_problem": sqa_flat,
    }
    e94["verdict_rule"] = ("PASS (中性化成立) if 两基准上 |acc 差| < 0.10 且 "
                           "McNemar p > 0.05")
    e94["verdict"] = ("PASS" if (diff < 0.10 and mc["p_value"] > 0.05
                                 and diff_sqa < 0.10
                                 and mc_sqa["p_value"] > 0.05) else "FAIL")
    output["experiments"]["E9.4_equal_weight_decoy_control"] = e94

    # ---------------- E9.5: 规则基线 vs LLM 先验臂 ----------------
    e95 = {"benchmarks": {}}
    rule_gsm = [eval_math_rule_baseline(llm, e, prov) for e in gsm8k]
    rule_gsm_sum = summarize(rule_gsm)
    mc95 = mcnemar(gsm_sum["unified"]["correct_vector"],
                   rule_gsm_sum["correct_vector"])
    e95["benchmarks"]["gsm8k"] = {
        "rule_baseline": {k: rule_gsm_sum[k] for k in ("n_total", "n_correct", "accuracy")},
        "unified_llm_prior": {k: gsm_sum["unified"][k]
                              for k in ("n_total", "n_correct", "accuracy")},
        "delta_unified_minus_rule": (gsm_sum["unified"]["accuracy"]
                                     - rule_gsm_sum["accuracy"]),
        "mcnemar_unified_vs_rule": mc95,
        "per_problem": rule_gsm,
    }
    rule_sqa = []
    for e, dec in sqa_rows:
        r = eval_yesno_rule_baseline(dec, e["answer"])
        r["id"] = e["id"]
        rule_sqa.append(r)
    rule_sqa_sum = summarize(rule_sqa)
    mc95_sqa = mcnemar(sqa_sum["unified"]["correct_vector"],
                       rule_sqa_sum["correct_vector"])
    e95["benchmarks"]["strategyqa"] = {
        "rule_baseline": {k: rule_sqa_sum[k] for k in ("n_total", "n_correct", "accuracy")},
        "unified_llm_prior": {k: sqa_sum["unified"][k]
                              for k in ("n_total", "n_correct", "accuracy")},
        "delta_unified_minus_rule": (sqa_sum["unified"]["accuracy"]
                                     - rule_sqa_sum["accuracy"]),
        "mcnemar_unified_vs_rule": mc95_sqa,
        "per_problem": rule_sqa,
    }
    d_gsm = e95["benchmarks"]["gsm8k"]["delta_unified_minus_rule"]
    d_sqa = e95["benchmarks"]["strategyqa"]["delta_unified_minus_rule"]
    e95["verdict_rule"] = ("PASS (LLM 先验有增量) if 两基准上 unified - rule > 0 "
                           "且 McNemar p < 0.05")
    e95["verdict"] = ("PASS" if (d_gsm > 0 and mc95["p_value"] < 0.05
                                 and d_sqa > 0
                                 and mc95_sqa["p_value"] < 0.05) else "FAIL")
    output["experiments"]["E9.5_rule_baseline"] = e95

    output["cache_provenance"] = prov.as_dict()
    output["llm_stats"] = llm.get_stats()

    os.makedirs(os.path.dirname(RESULT_FILE), exist_ok=True)
    tmp = RESULT_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=1, default=str)
    os.replace(tmp, RESULT_FILE)

    for name, exp in output["experiments"].items():
        print(f"{name}: verdict={exp['verdict']}")
        for bn, b in exp["benchmarks"].items():
            if "summary" in b:
                print(f"  {bn}: {b['summary']}")
            else:
                print(f"  {bn}: rule={b['rule_baseline']} unified={b['unified_llm_prior']}")
    print(f"llm_stats={output['llm_stats']}")
    print(f"provenance files: {len(output['cache_provenance'])}")
    print(f"written: {RESULT_FILE}")


if __name__ == "__main__":
    main()
