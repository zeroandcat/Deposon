#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================
# G2 时间换质量: Boltzmann退火路径选择 + 路径积分(Born规则)集成
# 【重写版】原始一次性脚本未入库, 本脚本依据 deposon_g2_boltzmann_pathintegral.json
# 的 setup 描述重写 (2026-08-23, W3-A7), 算法实现见 deposon_g2_modes.py
# (有 pytest 覆盖: tests/test_new_modes.py)。
#
# 零 API: 分解图全部来自 deposon_cache 的 kimi_api 缓存结果; 无缓存的题跳过并报告。
# 复现目标 (Table 9): Born 100%/100%, 投票 ~19%/17%, argmax_field 100%/100%。
#
# 方法定义 (与原始 setup 一致):
#   argmax_field:       BFS候选 + unified场透射 argmax (= BenchmarkEvaluator unified)
#   boltzmann_single:   单轨迹 T=0.3, 无场, p_i∝exp((w_i-b_i)/T)
#   boltzmann_annealed: K=20 退火轨迹 (T:1.0→0.05 几何) + unified场透射择优
#   path_integral_born: K=20 轨迹 (T=0.5), Born规则按答案聚合 argmax_a Σ_p t_p^2
#   majority_vote:      K=20 轨迹 (T=0.5), 无场, 答案多数决
# cost 定义: 节点级散射评估次数 (walk节点不计散射, 仅计场处理); single/vote 无场=0,
#   另报告轨迹长度作参考。与原记录口径不同处已在 cost_note 标注。
# ============================================================
import os, sys, json, math
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deposon_agents_v1_3 import (
    KimiLLMBackend, DeposonAgentSystem, BenchmarkEvaluator, DeposonField,
    HundredQuestionBenchmark, TrapBenchmark)
from deposon_g2_modes import (boltzmann_walk, boltzmann_annealed,
                              path_integral_born, majority_vote)

OUT = os.path.dirname(os.path.abspath(__file__))
SEED = 42


def get_llm():
    return KimiLLMBackend(api_key=os.environ.get('KIMI_API_KEY'),
                          cache_dir='/mnt/agents/output/deposon_cache',
                          cache_version='1.3.0')


def cached_graph_only(llm, q):
    """只读缓存, 绝不触发API。无 kimi_api 缓存返回 None。"""
    keys = [llm._cache_key('decompose', q)] + \
           [llm._legacy_cache_key('decompose', q, pv) for pv in llm.LEGACY_PROMPT_VERSIONS]
    for k in keys:
        c = llm.cache.get(k)
        if c is not None and c.get('source') == 'kimi_api':
            return llm._deserialize_decomposition(c)
    return None


def run_benchmark(name, dataset, llm):
    skipped, per_method = [], None
    results = {}
    for case in dataset:
        q, gold = case['question'], case['answer']
        dec = cached_graph_only(llm, q)
        if dec is None:
            skipped.append(q)
            continue
        graph = {'nodes': dec['nodes'], 'edges': dec['edges'],
                 'operation_chain': dec.get('operation_chain'),
                 'trap_nodes': dec.get('trap_nodes')}
        nodes, edges = graph['nodes'], graph['edges']
        ev = BenchmarkEvaluator(None, use_validation=False)

        def answer_fn(path, _g=graph):
            pred, _, _ = ev._compute_answer_from_path(_g, path)
            return pred

        def field_factory(_g=graph):
            f = DeposonField()
            f.spawn_from_graph(_g, mode='unified')
            return f

        row = {}
        # 1) argmax_field (= unified): BFS候选 + 场透射argmax
        agent = DeposonAgentSystem(llm_backend=llm, mode='unified')
        res = agent.reason(q, domain_hint='math', n_candidates=10)
        cands = res['all_candidates']
        best = res['passed_candidates'][0] if res['passed_candidates'] else \
               (cands[0] if cands else None)
        pred = answer_fn(best['path']) if best else None
        row['argmax_field'] = {
            'correct': bool(pred is not None and abs(pred - gold) < 0.01),
            'cost': sum(len(c['path']) for c in cands)}
        # 2) boltzmann_single
        import numpy as np
        p = boltzmann_walk(nodes, edges, 'N1', 'Goal', 0.3, np.random.default_rng(SEED))
        pred = answer_fn(p)
        row['boltzmann_single'] = {'correct': bool(pred is not None and abs(pred - gold) < 0.01),
                                   'cost': 0, 'traj_len': len(p)}
        # 3) boltzmann_annealed
        ra = boltzmann_annealed(nodes, edges, field_factory, K=20, seed=SEED)
        pred = answer_fn(ra['best_path'])
        row['boltzmann_annealed'] = {
            'correct': bool(pred is not None and abs(pred - gold) < 0.01),
            'cost': sum(len(t['path']) for t in ra['trajectories'])}
        # 4) path_integral_born (按答案聚合, 忠实于原setup文字描述)
        rb_ = path_integral_born(nodes, edges, field_factory, K=20, T=0.5,
                                 seed=SEED, answer_fn=answer_fn)
        pred = rb_['best_answer']
        row['path_integral_born'] = {
            'correct': bool(pred is not None and abs(pred - gold) < 0.01),
            'cost': sum(len(t['path']) for t in rb_['trajectories'])}
        # 4b) 对照: 按路径聚合 (检验原Table 9 Born=100%的可复现口径, 见output的reproduction_note)
        rb2 = path_integral_born(nodes, edges, field_factory, K=20, T=0.5,
                                 seed=SEED, answer_fn=lambda p: tuple(p))
        pred2 = answer_fn(rb2['best_path']) if rb2['best_path'] else None
        row['path_integral_born_by_path'] = {
            'correct': bool(pred2 is not None and abs(pred2 - gold) < 0.01),
            'cost': sum(len(t['path']) for t in rb2['trajectories'])}
        # 5) majority_vote
        mv = majority_vote(nodes, edges, K=20, T=0.5, seed=SEED, answer_fn=answer_fn)
        pred = mv['best_answer']
        row['majority_vote'] = {'correct': bool(pred is not None and abs(pred - gold) < 0.01),
                                'cost': 0,
                                'traj_len': sum(len(t['path']) for t in mv['trajectories'])}
        results[q] = row

    methods = ['argmax_field', 'boltzmann_single', 'boltzmann_annealed',
               'path_integral_born', 'path_integral_born_by_path', 'majority_vote']
    summary = {}
    n = len(results)
    for mname in methods:
        acc = sum(1 for r in results.values() if r[mname]['correct']) / n if n else 0.0
        cost = sum(r[mname]['cost'] for r in results.values()) / n if n else 0.0
        summary[mname] = {'accuracy': acc, 'avg_cost': cost}
    return {'benchmark': name, 'n': n, 'n_skipped_no_cache': len(skipped),
            'methods': summary}


def main():
    llm = get_llm()
    simple_ds = HundredQuestionBenchmark().generate_dataset(100, SEED)
    trap_ds = TrapBenchmark().generate_dataset(100, SEED)
    out = {'task': 'G2 时间换质量 (重写版, 依据 deposon_g2_boltzmann_pathintegral.json setup)',
           'rewrite': True, 'api_consumption': 0, 'seed': SEED,
           'cost_note': '重写版cost=场散射节点评估次数(single/vote无场=0); 原始记录的'
                        'argmax_field=12.1等口径未完全可考, 绝对值不可直接对齐, 倍数关系可比',
           'reproduction_note': (
               'Table 9 复现情况 (重写版, seed=42): argmax_field 100/100 ✓; '
               'boltzmann_single ~1-2% ✓; majority_vote 同量级 ✓ (原文19/17, 重写版13/8, '
               '抽样细节不可考); '
               'path_integral_born ✗ —— 按setup文字"答案聚合"仅 26/17; 按路径聚合更差 (1-2%, '
               '因正确轨迹同路径虽集中但极少被采到)。两种口径均无法复现原文 Born=100%/100%; '
               'boltzmann_annealed ✗ traps 84% vs 原文100% (16道两步题正确链在退火低温段'
               '几乎不被采样: 陷阱边w-b=0.8 vs 正确边0.3, T=0.05时 P(正确边)~e^-16)。'
               '结论: 原一次性脚本已丢失, 按其setup文字忠实重写的实现无法复现 Born/annealed '
               '的100%数字; 原实现很可能含有未记录的细节 (如轨迹集合含BFS候选或场引导采样)。'
               '建议: 论文 Table 9 的 Born/annealed 行标注"原始脚本丢失, 重写版未复现" '
               '并改用本重写版数字, 或补充实现细节后重跑。'),
           'results': {}}
    out['results']['simple'] = run_benchmark('simple', simple_ds, llm)
    out['results']['traps'] = run_benchmark('traps', trap_ds, llm)
    fp = os.path.join(OUT, 'results', 'deposon_g2_boltzmann_pathintegral_rewrite.json')
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    json.dump(out, open(fp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    for bn, r in out['results'].items():
        print(f"[{bn}] n={r['n']} skipped={r['n_skipped_no_cache']}")
        for m, s in r['methods'].items():
            print(f"  {m:<20} acc={s['accuracy']*100:.1f}% cost={s['avg_cost']:.1f}")
    print("saved:", fp)


if __name__ == '__main__':
    main()
