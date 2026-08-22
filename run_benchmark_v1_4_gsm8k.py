#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================
# Deposon v1.4 GSM8K 评测 Runner
# 三组核心对比: CoT基线(LLM本身) vs no_deposon vs unified
# (配额允许跑全五变体)。所有API结果进持久缓存, 分块可续跑。
# 用法: python run_benchmark_v1_4_gsm8k.py [cot|decompose|validate|eval] [budget_s]
# ============================================================
import os, sys, json, time, random, math, re
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deposon_agents_v1_4 import (KimiLLMBackend, DeposonAgentSystem,
                                 BenchmarkEvaluator, DeposonState)

OUT_DIR = "/mnt/agents/output"
GSM8K = os.path.join(OUT_DIR, "gsm8k_test.jsonl")
SAMPLE_FILE = os.path.join(OUT_DIR, "gsm8k_sample100_seed42.json")
DETAILS_FILE = os.path.join(OUT_DIR, "deposon_benchmark_v1_4_gsm8k_details.json")
RESULT_FILE = os.path.join(OUT_DIR, "deposon_benchmark_v1_4_gsm8k.json")

VARIANTS = {
    'no_deposon': {'mode': 'unified', 'use_deposon': False},
    'v1_blocking': {'mode': 'v1_blocking', 'use_deposon': True},
    'v2_tunneling': {'mode': 'v2_tunneling', 'use_deposon': True},
    'unified': {'mode': 'unified', 'use_deposon': True},
    'high_couple': {'mode': 'v1_blocking', 'use_deposon': True},
}


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def load_sample():
    """seed=42 抽100题; 答案解析 '#### N' (去逗号)"""
    rows = []
    with open(GSM8K, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    random.seed(42)
    idx = random.sample(range(len(rows)), 100)
    sample = []
    for i, ridx in enumerate(sorted(idx)):
        r = rows[ridx]
        m = re.search(r'####\s*([\-0-9,\.]+)', r['answer'])
        assert m, f"no answer in row {ridx}"
        sample.append({'id': i + 1, 'gsm8k_index': ridx,
                       'question': r['question'],
                       'answer': float(m.group(1).replace(',', ''))})
    return sample


def get_llm():
    return KimiLLMBackend(api_key=os.environ.get('KIMI_API_KEY'),
                          cache_dir=os.path.join(OUT_DIR, 'deposon_cache'),
                          cache_version='1.3.0')


def phase_api(sample, kind, budget):
    """kind in {cot, decompose, validate}; 分块执行, 3 workers 防限流"""
    llm = get_llm()
    details = {}
    if os.path.exists(DETAILS_FILE):
        details = json.load(open(DETAILS_FILE, encoding='utf-8'))

    def need(e):
        if kind == 'cot':
            return llm.cache.get(llm._cache_key('cot', e['question'])) is None
        if kind == 'decompose':
            q = e['question']
            keys = [llm._cache_key('decompose_mini', q), llm._cache_key('decompose', q)] + \
                   [llm._legacy_cache_key('decompose', q, pv) for pv in llm.LEGACY_PROMPT_VERSIONS]
            for k in keys:
                c = llm.cache.get(k)
                if c is not None and c.get('source') == 'kimi_api':
                    return False
            return True
        if kind == 'validate':
            v = details.get(str(e['id']), {}).get('validation')
            return not (isinstance(v, dict) and v.get('source') == 'kimi_api')

    todo = [e for e in sample if need(e)]
    log(f"{kind}: todo={len(todo)}/100")
    if not todo:
        return True

    # validate 需要先算 unified 路径
    def work(e):
        if kind == 'cot':
            r = llm.cot_solve(e['question'])
            if not r.get('ok'):
                raise RuntimeError('cot failed')
            return
        if kind == 'decompose':
            llm.decompose(e['question'])
            return
        if kind == 'validate':
            agent = DeposonAgentSystem(llm_backend=llm, mode='unified')
            ev = BenchmarkEvaluator(agent, use_validation=False)
            r = ev.evaluate_math(e['question'], e['answer'])
            v = llm.validate(e['question'], r.get('best_path') or [], r.get('predicted_answer'))
            rec = details.setdefault(str(e['id']), {})
            rec.update({'question': e['question'], 'answer': e['answer'],
                        'unified_predicted': r.get('predicted_answer'),
                        'unified_path': r.get('best_path'),
                        'unified_is_correct': r.get('is_correct'),
                        'validation': v})

    t0 = time.time()
    per_call = 45.0 if kind == 'decompose' else 18.0
    batch = todo[:max(1, int(3 * budget / per_call))]
    done = [0]
    errors = [0]

    def guarded(e):
        try:
            work(e)
            done[0] += 1
        except Exception:
            errors[0] += 1

    with ThreadPoolExecutor(max_workers=int(os.environ.get("WORKERS", "3"))) as ex:
        list(ex.map(guarded, batch))

    if kind == 'validate':
        tmp = DETAILS_FILE + '.tmp'
        json.dump(details, open(tmp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        os.replace(tmp, DETAILS_FILE)
    log(f"{kind}: done={done[0]} errors={errors[0]} elapsed={time.time()-t0:.1f}s stats={llm.get_stats()}")
    return len([e for e in sample if need(e)]) == 0


def mcnemar(correct_a, correct_b):
    """精确双侧 McNemar (二项检验), a vs b 配对正确性"""
    b = sum(1 for x, y in zip(correct_a, correct_b) if x and not y)
    c = sum(1 for x, y in zip(correct_a, correct_b) if not x and y)
    n = b + c
    if n == 0:
        return {'b': b, 'c': c, 'p_value': 1.0}
    k = min(b, c)
    p = sum(math.comb(n, i) for i in range(0, k + 1)) / (2 ** (n - 1))
    return {'b': b, 'c': c, 'p_value': min(1.0, p)}


def physics_audit():
    import numpy as np
    d = DeposonState(id='audit', center=np.zeros(4), g_couple=1.0, g_aether=0.3,
                     resonance_energy=0.2)
    worst = max(abs(sum(d.scatter(e).values()) - 1.0) for e in [0.0, 0.1, 0.5, 1.0, 3.7])
    return {'t_plus_r_plus_a_max_deviation': worst, 'tolerance': 1e-6, 'passed': worst < 1e-6}


def evaluate(sample):
    llm = get_llm()
    details = {}
    if os.path.exists(DETAILS_FILE):
        details = json.load(open(DETAILS_FILE, encoding='utf-8'))

    # CoT 基线
    cot_correct, cot_answers = [], {}
    for e in sample:
        r = llm.cot_solve(e['question'])
        ans = r.get('answer')
        cot_answers[e['id']] = ans
        cot_correct.append(ans is not None and abs(ans - e['answer']) < 0.01)

    # 五变体
    variant_results, variant_correct = {}, {}
    for vname, cfg in VARIANTS.items():
        details_v = []
        def work(e):
            agent = DeposonAgentSystem(llm_backend=llm, mode=cfg['mode'])
            agent.use_deposon = cfg['use_deposon']
            ev = BenchmarkEvaluator(agent, use_validation=False)
            return ev.evaluate_math(e['question'], e['answer'])
        with ThreadPoolExecutor(max_workers=4) as ex:
            details_v = list(ex.map(work, sample))
        n_ok = sum(1 for d in details_v if d['is_correct'])
        variant_results[vname] = {
            'n_total': len(sample), 'n_correct': n_ok,
            'accuracy': n_ok / len(sample),
            'avg_ether_dissipated': sum(d['ether_dissipated'] for d in details_v) / len(sample)}
        variant_correct[vname] = [bool(d['is_correct']) for d in details_v]
        for e, d in zip(sample, details_v):
            rec = details.setdefault(str(e['id']), {})
            rec.update({'question': e['question'], 'answer': e['answer']})
            rec[f'{vname}_predicted'] = d.get('predicted_answer')
            rec[f'{vname}_is_correct'] = d['is_correct']
            rec[f'{vname}_path'] = d.get('best_path')
            rec[f'{vname}_trap_hit'] = d.get('path_hit_trap')
        log(f"{vname:<12} acc={variant_results[vname]['accuracy']*100:.1f}%")
        # 保存中间结果(防中断丢失)
        tmp = DETAILS_FILE + '.tmp'
        json.dump(details, open(tmp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2, default=str)
        os.replace(tmp, DETAILS_FILE)

    for e in sample:
        details[str(e['id'])]['cot_answer'] = cot_answers[e['id']]
        details[str(e['id'])]['cot_is_correct'] = bool(cot_correct[sample.index(e)])

    cot_acc = sum(cot_correct) / len(sample)
    unified_acc = variant_results['unified']['accuracy']
    nodep_acc = variant_results['no_deposon']['accuracy']

    # validate 统计
    vdist, vagree, nv = {}, 0, 0
    for e in sample:
        v = details.get(str(e['id']), {}).get('validation')
        if isinstance(v, dict) and v.get('source') == 'kimi_api':
            nv += 1
            vdist[v.get('verdict', '?')] = vdist.get(v.get('verdict', '?'), 0) + 1
            uc = details[str(e['id'])].get('unified_is_correct')
            if uc is not None and (v.get('verdict') == 'correct') == bool(uc):
                vagree += 1

    out = {
        'version': '1.4.0',
        'benchmark': 'GSM8K official test split, seed=42 sample 100',
        'llm_backend': 'kimi-for-coding (real API, persistent cache)',
        'n_questions': len(sample),
        'cot_baseline_accuracy': cot_acc,
        'baseline_accuracy': nodep_acc,
        'unified_accuracy': unified_acc,
        'effect_size_unified_vs_no_deposon': unified_acc - nodep_acc,
        'effect_size_unified_vs_cot': unified_acc - cot_acc,
        'is_better_than_no_deposon': unified_acc > nodep_acc,
        'is_better_than_cot': unified_acc > cot_acc,
        'mcnemar_unified_vs_cot': mcnemar(variant_correct['unified'], cot_correct),
        'mcnemar_unified_vs_no_deposon': mcnemar(variant_correct['unified'], variant_correct['no_deposon']),
        'variant_results': variant_results,
        'validate_stats': {'n_validated': nv, 'verdict_distribution': vdist,
                           'agreement_with_is_correct': vagree / nv if nv else None},
        'llm_stats_final_run': llm.get_stats(),
        'physics_audit': physics_audit(),
    }
    json.dump(out, open(RESULT_FILE, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    tmp = DETAILS_FILE + '.tmp'
    json.dump(details, open(tmp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2, default=str)
    os.replace(tmp, DETAILS_FILE)
    log(f"CoT={cot_acc*100:.1f}% no_deposon={nodep_acc*100:.1f}% unified={unified_acc*100:.1f}%")
    log(f"McNemar unified vs CoT: {out['mcnemar_unified_vs_cot']}")
    log(f"输出: {RESULT_FILE} / {DETAILS_FILE}")


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'eval'
    budget = float(sys.argv[2]) if len(sys.argv) > 2 else 200.0
    sample = load_sample()
    if len(sys.argv) > 1 and sys.argv[1] == 'prep':
        json.dump(sample, open(SAMPLE_FILE, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        log(f"sample saved: {SAMPLE_FILE}")
        return
    if mode in ('cot', 'decompose', 'validate'):
        complete = phase_api(sample, mode, budget)
        log(f"{mode} {'COMPLETE' if complete else 'PARTIAL(续跑)'}")
    elif mode == 'eval':
        evaluate(sample)


if __name__ == '__main__':
    main()
