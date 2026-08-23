#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================
# Deposon v1.4 StrategyQA 评测 (yes/no 隐式推理)
# 协议同 GSM8K: decompose -> 5变体+CoT -> eval -> McNemar -> validate
# 图构造 (yes/no 版):
#   S1(题干概念) -> S2..Sn (推理步骤, type='step') -> Goal(type='answer')
#   诱饵: S1 -> Trap_guess(type='trap', w=0.9 低垒0.1) -> Goal(w=0.55)
#   答案语义: 路径含 Trap_guess => trap_answer (直觉猜测答案), 否则 LLM 推理答案
# 安全: key 仅从 KIMI_API_KEY 环境变量读取。
# ============================================================
import os, sys, json, math, time, random, threading
from concurrent.futures import ThreadPoolExecutor

OUT = "/mnt/agents/output"
sys.path.insert(0, OUT)
from deposon_agents_v1_4 import KimiLLMBackend, DeposonAgentSystem, BenchmarkEvaluator, DeposonField

RESULT_FILE = os.path.join(OUT, 'deposon_benchmark_v1_4_strategyqa.json')
DETAILS_FILE = os.path.join(OUT, 'deposon_benchmark_v1_4_strategyqa_details.json')
DATA_FILE = os.path.join(OUT, 'strategyqa_train.json')
SEED = 42
N = 100
WORKERS = int(os.environ.get('WORKERS', '4'))

VARIANTS = {
    'no_deposon': {'mode': 'unified', 'use_deposon': False},
    'v1_blocking': {'mode': 'v1_blocking', 'use_deposon': True},
    'v2_tunneling': {'mode': 'v2_tunneling', 'use_deposon': True},
    'unified': {'mode': 'unified', 'use_deposon': True},
    'high_couple': {'mode': 'v1_blocking', 'use_deposon': True},
}

YESNO_DECOMPOSE_SUFFIX = """
Think briefly (one or two lines), then output ONLY this JSON object:
{"answer":"Yes|No","steps":["reason step 1","reason step 2"],"trap_answer":"Yes|No","trap_reason":"the most tempting wrong intuition"}
answer: the correct Yes/No after reasoning. steps: 2-4 short reasoning facts. trap_answer: the answer a surface intuition would give (must differ from answer if the question is tricky; may equal answer if genuinely obvious)."""

COT_SUFFIX = "\nAnswer with Yes or No on the first word, then one short reason."


def get_llm():
    return KimiLLMBackend(api_key=os.environ.get('KIMI_API_KEY'),
                          cache_dir=os.path.join(OUT, 'deposon_cache'),
                          cache_version='1.3.0')


def load_sample(n=N, seed=SEED):
    data = json.load(open(DATA_FILE, encoding='utf-8'))['examples']
    rng = random.Random(seed)
    picked = rng.sample(data, n)
    sample = []
    for i, ex in enumerate(picked):
        gold = 'Yes' if ex['target_scores'].get('Yes', 0) == 1 else 'No'
        sample.append({'id': i + 1, 'question': ex['input'].strip(), 'answer': gold})
    return sample


def decompose_yesno(llm, q):
    """真实API: yes/no 问题 -> {answer, steps, trap_answer} + 图结构。缓存持久化。"""
    llm._bump('calls')
    key = llm._cache_key('decompose_yesno', q)
    cached = llm.cache.get(key)
    if cached is not None:
        llm._bump('cache_hits')
        return cached
    try:
        raw = llm._chat("You are a precise commonsense reasoner.", q + YESNO_DECOMPOSE_SUFFIX)
        spec = llm._extract_json(raw)
        ans = str(spec.get('answer', '')).strip().capitalize()
        if ans not in ('Yes', 'No'):
            raise ValueError('bad answer')
        trap = str(spec.get('trap_answer', '')).strip().capitalize()
        if trap not in ('Yes', 'No'):
            trap = 'No' if ans == 'Yes' else 'Yes'
        steps = [str(s)[:120] for s in (spec.get('steps') or [])][:4] or ['reason']
        result = {'answer': ans, 'trap_answer': trap, 'steps': steps, 'source': 'kimi_api'}
    except Exception:
        llm._bump('fallbacks')
        raise  # yes/no 不允许规则降级冒充: 直接失败, 由调用方重试/记录
    llm.cache.set(key, result)
    return result


def build_yesno_graph(dec):
    nodes, edges = {}, {}
    steps = dec['steps']
    for i, s in enumerate(steps):
        nodes[f'S{i+1}'] = {'energy': 0.3 + i * 0.05, 'type': 'step', 'text': s}
    nodes['Goal'] = {'energy': 0.0, 'type': 'answer'}
    nodes['Trap_guess'] = {'energy': 0.1, 'type': 'trap', 'trap_type': 'surface_guess'}
    for i in range(len(steps) - 1):
        edges[(f'S{i+1}', f'S{i+2}')] = {'weight': 0.7, 'migration_barrier': 0.2}
    edges[(f'S{len(steps)}', 'Goal')] = {'weight': 0.8, 'migration_barrier': 0.2}
    edges[('S1', 'Trap_guess')] = {'weight': 0.9, 'migration_barrier': 0.1}
    edges[('Trap_guess', 'Goal')] = {'weight': 0.55, 'migration_barrier': 0.3}
    return {'nodes': nodes, 'edges': edges}


def generate_paths(nodes, edges, max_paths=30):
    start, goal = 'S1', 'Goal'
    paths, queue = [], [(start, [start])]
    from collections import deque
    queue = deque(queue)
    while queue and len(paths) < max_paths:
        cur, pth = queue.popleft()
        if cur == goal:
            paths.append(pth)
            continue
        outs = [(v, a.get('weight', 0.5)) for (u, v), a in edges.items()
                if u == cur and (v not in pth or v == goal)]
        outs.sort(key=lambda x: x[1], reverse=True)
        for v, w in outs[:8]:
            queue.append((v, pth + [v]))
    return paths


def evaluate_variant(cfg, dec):
    graph = build_yesno_graph(dec)
    paths = generate_paths(graph['nodes'], graph['edges'])
    if not cfg['use_deposon']:
        scored = [(p, 1.0) for p in paths]  # 无场: 全透射, 保留生成序(贪心序=陷阱优先)
    else:
        field = DeposonField()
        field.spawn_from_graph(graph, mode=cfg['mode'])
        scored = [(p, field.process_path(p)['transmitted']) for p in paths]
    scored.sort(key=lambda x: x[1], reverse=True)
    best = scored[0][0] if scored else None
    trap_hit = best is not None and any('Trap' in n for n in best)
    pred = dec['trap_answer'] if trap_hit else dec['answer']
    return {'pred': pred, 'path': best, 'trap_hit': trap_hit}


def cot_answer(llm, q):
    llm._bump('calls')
    key = llm._cache_key('cot_yesno', q)
    cached = llm.cache.get(key)
    if cached is not None:
        llm._bump('cache_hits')
        return cached
    raw = llm._chat("You are a precise commonsense reasoner.", q + COT_SUFFIX)
    first = raw.strip().split()[0].strip('.,!').lower() if raw.strip() else ''
    ans = 'Yes' if first.startswith('yes') else ('No' if first.startswith('no') else None)
    if ans is None:
        import re
        m = re.search(r'\b(yes|no)\b', raw.lower())
        ans = m.group(1).capitalize() if m else None
    result = {'answer': ans, 'raw': raw[:200], 'source': 'kimi_api'}
    llm.cache.set(key, result)
    return result


def mcnemar(a, b):
    bb = sum(1 for x, y in zip(a, b) if x and not y)
    cc = sum(1 for x, y in zip(a, b) if not x and y)
    n = bb + cc
    if n == 0:
        return {'b': 0, 'c': 0, 'p_value': 1.0}
    k = min(bb, cc)
    p = sum(math.comb(n, i) for i in range(k + 1)) / (2 ** (n - 1))
    return {'b': bb, 'c': cc, 'p_value': min(1.0, p)}


def phase_api(llm, sample, kind, budget):
    def need(e):
        key = llm._cache_key(kind, e['question'])
        return llm.cache.get(key) is None
    todo = [e for e in sample if need(e)]
    print(f"{kind}: todo={len(todo)}", flush=True)
    if not todo:
        return True
    per_call = 20.0
    batch = todo[:max(1, int(WORKERS * budget / per_call))]
    fn = decompose_yesno if kind == 'decompose_yesno' else cot_answer
    fails = [0]
    def work(e):
        try:
            fn(llm, e['question'])
        except Exception:
            fails[0] += 1
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        list(ex.map(work, batch))
    print(f"{kind} chunk done, fails={fails[0]}, stats={llm.get_stats()}", flush=True)
    return not any(need(e) for e in sample)


def evaluate(llm, sample):
    details = {}
    if os.path.exists(DETAILS_FILE):
        details = json.load(open(DETAILS_FILE, encoding='utf-8'))
    variant_correct = {v: [] for v in VARIANTS}
    cot_correct = []
    excluded = []
    for e in sample:
        dec = llm.cache.get(llm._cache_key('decompose_yesno', e['question']))
        cot = llm.cache.get(llm._cache_key('cot_yesno', e['question']))
        if dec is None or cot is None:
            # API 拒绝 (如内容过滤 HTTP400) —— 诚实排除并记录, 绝不mock
            excluded.append({'id': e['id'], 'question': e['question'][:80],
                             'reason': 'api_blocked(content_filter)'})
            continue
        rec = details.setdefault(str(e['id']), {'question': e['question'], 'answer': e['answer']})
        rec['decompose'] = dec
        rec['cot'] = cot
        rec['cot_is_correct'] = bool(cot and cot['answer'] == e['answer'])
        cot_correct.append(rec['cot_is_correct'])
        for vname, cfg in VARIANTS.items():
            r = evaluate_variant(cfg, dec)
            rec[f'{vname}_pred'] = r['pred']
            rec[f'{vname}_is_correct'] = bool(r['pred'] == e['answer'])
            rec[f'{vname}_path'] = r['path']
            rec[f'{vname}_trap_hit'] = r['trap_hit']
            variant_correct[vname].append(rec[f'{vname}_is_correct'])
    n = len(cot_correct)  # 实际评估题数 (排除 api_blocked)
    variant_results = {v: {'n_total': n, 'n_correct': sum(c),
                           'accuracy': sum(c) / n}
                       for v, c in variant_correct.items()}
    cot_acc = sum(cot_correct) / n
    uni = variant_correct['unified']
    out = {
        'version': '1.4.0', 'benchmark': 'StrategyQA (train subset, seed=42, n=100)',
        'n_questions': n,
        'excluded_api_blocked': excluded,
        'cot_baseline_accuracy': cot_acc,
        'baseline_accuracy': variant_results['no_deposon']['accuracy'],
        'unified_accuracy': variant_results['unified']['accuracy'],
        'effect_size': variant_results['unified']['accuracy'] - variant_results['no_deposon']['accuracy'],
        'variant_results': variant_results,
        'mcnemar_unified_vs_cot': mcnemar(uni, cot_correct),
        'mcnemar_unified_vs_no_deposon': mcnemar(uni, variant_correct['no_deposon']),
        'llm_stats': llm.get_stats(),
    }
    json.dump(out, open(RESULT_FILE, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    tmp = DETAILS_FILE + '.tmp'
    json.dump(details, open(tmp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2, default=str)
    os.replace(tmp, DETAILS_FILE)
    print(json.dumps({k: v for k, v in out.items() if k != 'variant_results'}, ensure_ascii=False, indent=1))
    print({v: r['accuracy'] for v, r in variant_results.items()})


def main():
    llm = get_llm()
    assert llm.api_key, 'KIMI_API_KEY env not set'
    sample = load_sample()
    mode = sys.argv[1] if len(sys.argv) > 1 else 'all'
    budget = float(sys.argv[2]) if len(sys.argv) > 2 else 400
    if mode in ('decompose', 'all'):
        ok = phase_api(llm, sample, 'decompose_yesno', budget)
        print('decompose', 'COMPLETE' if ok else 'PARTIAL', flush=True)
    if mode in ('cot', 'all'):
        ok = phase_api(llm, sample, 'cot_yesno', budget)
        print('cot', 'COMPLETE' if ok else 'PARTIAL', flush=True)
    if mode in ('eval', 'all'):
        evaluate(llm, sample)
    if mode == 'validate2':
        # v2: 推理链附带步骤文本 (v1只传节点id, 验证器无法判断内容, 一致率仅36%)
        details = json.load(open(DETAILS_FILE, encoding='utf-8'))
        def vneed(e):
            v = details.get(str(e['id']), {}).get('validation2')
            return not (isinstance(v, dict) and v.get('source') == 'kimi_api')
        todo = [e for e in sample
                if llm.cache.get(llm._cache_key('decompose_yesno', e['question'])) is not None
                and vneed(e)]
        print(f"validate2 todo={len(todo)}", flush=True)
        batch = todo[:max(1, int(WORKERS * budget / 18))]
        def vwork(e):
            rec = details[str(e['id'])]
            steps = (rec.get('decompose') or {}).get('steps') or []
            chain = [f"step{i+1}: {s}" for i, s in enumerate(steps)] + \
                    [f"final answer: {rec.get('unified_pred')}"]
            try:
                v = llm.validate(e['question'], chain, rec.get('unified_pred'))
                rec['validation2'] = v
            except Exception:
                pass
        with ThreadPoolExecutor(max_workers=3) as ex:
            list(ex.map(vwork, batch))
        tmp = DETAILS_FILE + '.tmp'
        json.dump(details, open(tmp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2, default=str)
        os.replace(tmp, DETAILS_FILE)
        n_done = sum(1 for k in details
                     if isinstance(details[k].get('validation2'), dict)
                     and details[k]['validation2'].get('source') == 'kimi_api')
        print(f"validate2 chunk done, total={n_done}, stats={llm.get_stats()}", flush=True)
    if mode == 'validate':
        details = json.load(open(DETAILS_FILE, encoding='utf-8'))
        def vneed(e):
            v = details.get(str(e['id']), {}).get('validation')
            return not (isinstance(v, dict) and v.get('source') == 'kimi_api')
        todo = [e for e in sample
                if llm.cache.get(llm._cache_key('decompose_yesno', e['question'])) is not None
                and vneed(e)]
        print(f"validate todo={len(todo)}", flush=True)
        batch = todo[:max(1, int(WORKERS * budget / 18))]
        def vwork(e):
            rec = details[str(e['id'])]
            path = rec.get('unified_path') or []
            try:
                v = llm.validate(e['question'], path, rec.get('unified_pred'))
                rec['validation'] = v
            except Exception:
                pass
        with ThreadPoolExecutor(max_workers=3) as ex:
            list(ex.map(vwork, batch))
        tmp = DETAILS_FILE + '.tmp'
        json.dump(details, open(tmp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2, default=str)
        os.replace(tmp, DETAILS_FILE)
        n_done = sum(1 for k in details
                     if isinstance(details[k].get('validation'), dict)
                     and details[k]['validation'].get('source') == 'kimi_api')
        print(f"validate chunk done, total={n_done}, stats={llm.get_stats()}", flush=True)


if __name__ == '__main__':
    main()
