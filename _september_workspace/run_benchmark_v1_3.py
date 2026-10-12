#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================
# Deposon v1.3 百题消融评测 Runner
# - HundredQuestionBenchmark(seed=42, 100题) / TrapBenchmark(seed=42, 100题)
# - 五变体: no_deposon / v1_blocking / v2_tunneling / unified / high_couple
# - decompose 每题只调一次 (五变体共享 PersistentCache)
# - API key 仅从环境变量 KIMI_API_KEY 读取, 不写入任何输出文件
# ============================================================
import os
import sys
import json
import time
import threading
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deposon_agents_v1_3 import (
    KimiLLMBackend, LLMBackend, DeposonAgentSystem, BenchmarkEvaluator,
    HundredQuestionBenchmark, TrapBenchmark, DeposonState
)

OUT_DIR = "/mnt/agents/output"
MAX_WORKERS = 8
N_QUESTIONS = 100
SEED = 42

VARIANTS = {
    'no_deposon': {'mode': 'unified', 'use_deposon': False},
    'v1_blocking': {'mode': 'v1_blocking', 'use_deposon': True},
    'v2_tunneling': {'mode': 'v2_tunneling', 'use_deposon': True},
    'unified': {'mode': 'unified', 'use_deposon': True},
    'high_couple': {'mode': 'high_couple', 'use_deposon': True},
}

_print_lock = threading.RLock()  # RLock: log() 可能在持有锁的 work() 内被调用


def log(msg):
    with _print_lock:
        print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def phase1_warm_decompose(llm, questions):
    """每题 decompose 只调一次, 结果进持久缓存, 五变体共享"""
    results = {}
    done = [0]

    def work(q):
        d = llm.decompose(q)
        with _print_lock:
            done[0] += 1
            if done[0] % 20 == 0:
                log(f"decompose 进度 {done[0]}/{len(questions)}")
        return q, d

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        for q, d in ex.map(work, questions):
            results[q] = d
    return results


def evaluate_variant(variant_name, cfg, dataset, llm):
    """逐题独立 DeposonAgentSystem 实例, 避免场状态串扰; decompose 全部缓存命中"""
    details = []

    def work(case):
        agent = DeposonAgentSystem(llm_backend=llm, mode=cfg['mode'])
        agent.use_deposon = cfg['use_deposon']
        ev = BenchmarkEvaluator(agent, use_validation=False)
        return ev.evaluate_math(case['question'], case.get('answer'))

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        details = list(ex.map(work, dataset))

    n_correct = sum(1 for d in details if d['is_correct'])
    n = len(details)
    avg_ether = sum(d['ether_dissipated'] for d in details) / n if n else 0.0
    return {
        'n_total': n,
        'n_correct': n_correct,
        'accuracy': n_correct / n if n else 0.0,
        'avg_ether_dissipated': avg_ether,
    }, details


def by_operation(details, dataset, key_mode='predicted'):
    """key_mode='predicted': 按系统识别op (v1.2口径, 无op->unknown);
       key_mode='gold': 按数据及金标op"""
    agg = {}
    for det, case in zip(details, dataset):
        if key_mode == 'predicted':
            k = det.get('op_type') or 'unknown'
        else:
            k = case.get('op', 'unknown')
        a = agg.setdefault(k, {'correct': 0, 'total': 0})
        a['total'] += 1
        if det['is_correct']:
            a['correct'] += 1
    return {k: {**v, 'accuracy': v['correct'] / v['total'] if v['total'] else 0.0}
            for k, v in agg.items()}


def v12_unknown_subset_questions(dataset):
    """用 v1.2 KimiLLMBackend 规则引擎(纯本地)识别 v1.2 中的 unknown 题
    (规则未检测到任何运算 -> op_type=None -> v1.2评测归入'unknown')"""
    from deposon_agents_v1_3 import KimiLLMBackend as _KB
    rule_engine = _KB.__new__(_KB)  # 仅借用规则方法, 不触发任何API
    subset = []
    for case in dataset:
        ops = _KB._detect_ops(rule_engine, case['question'])
        if not ops:
            subset.append(case['question'])
    return set(subset)


def physics_audit():
    """幺正性/能量守恒审计: t+r+a=1 (v1.2散射定义), 容差1e-6"""
    import numpy as np
    d = DeposonState(id='audit', center=np.zeros(4), g_couple=1.0, g_aether=0.3,
                     resonance_energy=0.2)
    worst = 0.0
    for e in [0.0, 0.1, 0.2, 0.5, 1.0, 3.7]:
        s = d.scatter(e)
        dev = abs(s['transmitted'] + s['reflected'] + s['dissipated'] - 1.0)
        worst = max(worst, dev)
    return {'t_plus_r_plus_a_max_deviation': worst, 'tolerance': 1e-6,
            'passed': worst < 1e-6}


def run_benchmark(name, dataset, llm):
    log(f"=== {name}: {len(dataset)} 题, 五变体 ===")
    variant_results, all_details = {}, {}
    for vname, cfg in VARIANTS.items():
        t0 = time.time()
        res, details = evaluate_variant(vname, cfg, dataset, llm)
        variant_results[vname] = res
        all_details[vname] = details
        log(f"  {vname:<12} acc={res['accuracy']*100:.1f}% ({res['n_correct']}/{res['n_total']}) "
            f"ether={res['avg_ether_dissipated']:.4f} [{time.time()-t0:.1f}s]")

    baseline_acc = variant_results['no_deposon']['accuracy']
    unified_acc = variant_results['unified']['accuracy']
    effect = unified_acc - baseline_acc

    unified_details = all_details['unified']
    out = {
        'version': '1.3.0',
        'llm_backend': 'kimi-for-coding (real API, rule-fallback)',
        'n_questions': len(dataset),
        'baseline_accuracy': baseline_acc,
        'unified_accuracy': unified_acc,
        'effect_size': effect,
        'is_better': effect > 0,
        'variant_results': variant_results,
        'by_operation': by_operation(unified_details, dataset, key_mode='predicted'),
        'by_gold_operation': by_operation(unified_details, dataset, key_mode='gold'),
    }

    # v1.2 unknown 子集对比
    unknown_qs = v12_unknown_subset_questions(dataset)
    if unknown_qs:
        sub = [d for d in unified_details if d['question'] in unknown_qs]
        n_sub_ok = sum(1 for d in sub if d['is_correct'])
        out['v12_unknown_subset'] = {
            'n': len(sub),
            'v12_accuracy': 0.0,
            'v13_unified_accuracy': n_sub_ok / len(sub) if sub else 0.0,
            'v13_unified_correct': n_sub_ok,
        }

    if name == 'traps':
        dist = {}
        for c in dataset:
            dist[c['trap_type']] = dist.get(c['trap_type'], 0) + 1
        out['trap_distribution'] = dist
        # 按陷阱类型的 unified 准确率
        tacc = {}
        for det, case in zip(unified_details, dataset):
            a = tacc.setdefault(case['trap_type'], {'correct': 0, 'total': 0})
            a['total'] += 1
            if det['is_correct']:
                a['correct'] += 1
        out['unified_by_trap_type'] = {
            k: {**v, 'accuracy': v['correct'] / v['total']} for k, v in tacc.items()}
    return out, all_details


def main():
    api_key = os.environ.get('KIMI_API_KEY')
    if not api_key:
        log("警告: 未设置 KIMI_API_KEY, 将全部走规则降级基线")
    llm = KimiLLMBackend(api_key=api_key,
                         cache_dir=os.path.join(OUT_DIR, 'deposon_cache'),
                         cache_version='1.3.0')

    simple_ds = HundredQuestionBenchmark().generate_dataset(N_QUESTIONS, SEED)
    trap_ds = TrapBenchmark().generate_dataset(N_QUESTIONS, SEED)

    # ---- Phase 1: 分解 (唯一产生API调用的阶段, 每题一次) ----
    all_questions = list({c['question'] for c in simple_ds} | {c['question'] for c in trap_ds})
    log(f"Phase 1: decompose {len(all_questions)} 个独立问题 (workers={MAX_WORKERS})")
    t0 = time.time()
    decomps = phase1_warm_decompose(llm, all_questions)
    n_api = sum(1 for d in decomps.values() if d.get('source') == 'kimi_api')
    n_fb = sum(1 for d in decomps.values() if d.get('source') == 'rule_fallback')
    log(f"Phase 1 完成 [{time.time()-t0:.1f}s]: kimi_api={n_api}, rule_fallback={n_fb}")

    # ---- Phase 2: 五变体评测 (缓存命中, 零API消耗) ----
    log("Phase 2: 五变体评测 (全部缓存命中)")
    simple_out, simple_details = run_benchmark('simple', simple_ds, llm)
    traps_out, traps_details = run_benchmark('traps', trap_ds, llm)

    # ---- Phase 3: LLM validate 抽样 (证明真实validate可用, 控制消耗) ----
    val_samples = []
    if '--validate-samples' in sys.argv:
        log("Phase 3: validate 抽样 x8")
        cases = [(c, simple_details['unified'][i]) for i, c in enumerate(simple_ds[:4])] + \
                [(c, traps_details['unified'][i]) for i, c in enumerate(trap_ds[:4])]
        for case, det in cases:
            v = llm.validate(case['question'], det['best_path'] or [], det['predicted_answer'])
            val_samples.append({'question': case['question'], 'predicted': det['predicted_answer'],
                                'validation': v})
        log(f"validate 抽样完成: {sum(1 for s in val_samples if s['validation'].get('source')=='kimi_api')}/8 走真实API")

    llm_stats = llm.get_stats()
    cache_stats = llm.cache.get_stats() if llm.cache else {}
    audit = physics_audit()
    log(f"物理审计: t+r+a 最大偏差 {audit['t_plus_r_plus_a_max_deviation']:.2e} (容差1e-6) -> {'PASS' if audit['passed'] else 'FAIL'}")

    simple_out['llm_stats'] = llm_stats
    simple_out['cache_stats'] = cache_stats
    simple_out['physics_audit'] = audit
    traps_out['llm_stats'] = llm_stats
    traps_out['cache_stats'] = cache_stats
    traps_out['physics_audit'] = audit

    with open(os.path.join(OUT_DIR, 'deposon_benchmark_v1_3_simple.json'), 'w', encoding='utf-8') as f:
        json.dump(simple_out, f, ensure_ascii=False, indent=2)
    with open(os.path.join(OUT_DIR, 'deposon_benchmark_v1_3_traps.json'), 'w', encoding='utf-8') as f:
        json.dump(traps_out, f, ensure_ascii=False, indent=2)
    with open(os.path.join(OUT_DIR, 'deposon_benchmark_v1_3_details.json'), 'w', encoding='utf-8') as f:
        json.dump({'simple': simple_details, 'traps': traps_details,
                   'validate_samples': val_samples}, f, ensure_ascii=False, indent=2, default=str)

    log("=== 汇总 ===")
    log(f"simple: baseline={simple_out['baseline_accuracy']*100:.1f}% unified={simple_out['unified_accuracy']*100:.1f}% effect={simple_out['effect_size']:+.2f}")
    log(f"traps : baseline={traps_out['baseline_accuracy']*100:.1f}% unified={traps_out['unified_accuracy']*100:.1f}% effect={traps_out['effect_size']:+.2f}")
    log(f"llm_stats: {llm_stats}")
    log("输出: deposon_benchmark_v1_3_simple.json / _traps.json / _details.json")


if __name__ == '__main__':
    main()
