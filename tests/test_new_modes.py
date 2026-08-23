# -*- coding: utf-8 -*-
# ============================================================
# W3-A: 新模式回归测试与物理一致性自检 (零 API)
# 覆盖: unified/v1_blocking/v2_tunneling/high_couple/resonant/resonant_hybrid/
#       labelfree/arrhenius/arrhenius_hybrid + G2 Boltzmann/路径积分
#
# 不变量:
#   1. 幺正性: 逐路径 t+r+a=1 (arrhenius 系为 t+r+a+barrier_loss=1), 容差 1e-12
#   2. 条件等效: arrhenius T→∞ ⇒ unified; 路径积分 K=1 ⇒ 单轨迹 argmax;
#      resonant δ=0 ⇒ unified; labelfree 标签打乱逐位一致; boltzmann T→0 ⇒ argmax
#   3. 决定论: 同 seed 两次逐位一致
#   4. labelfree 不读取 type 标签 (静态源码检查)
#
# 文档条件声明缺口 (测试按现状锁定行为, 见各 docstring):
#   [C1] DeposonState.scatter 未对 g_couple<0 / g_aether<0 做防御:
#        g_aether∈(-1,0) 时 t>1 仍守恒; g_aether<=-1 时 denom<=0 产生负 t ——
#        需论文声明前置条件 g_couple>=0 且 g_aether>=0。
#   [C2] arrhenius 的 k=min(1, exp(-b/T)) 对负 barrier 截断为1 (防御已内置);
#        T<=0 由 max(T,1e-9) 防御 —— 条件 T>0 已内建, 无需论文声明。
#   [C3] "arrhenius T→∞ 退化 unified" 是极限命题: T=1e6 时 k=1-b/1e6 ≈ 1-3e-7,
#        逐路径透射率有 ~1e-6 量级残差; 等效性在 argmax 路径选择层面成立
#        (本测试断言选择一致 + 数值容差内一致, 而非逐位一致)。
# ============================================================
import copy
import inspect
import math
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from deposon_agents_v1_3 import (
    DeposonField, DeposonState, DeposonAgentSystem, BenchmarkEvaluator,
    LLMBackend, deterministic_embedding,
)
from deposon_g2_modes import (
    boltzmann_walk, boltzmann_annealed, path_integral_born, find_start_goal,
)

TOL = 1e-12


# ---------------------------------------------------------------- fixture
def make_graph():
    """与 v1.3 LLM 建图同构的最小图: 正确链 N1->OP1->Goal (subtraction 5-2=3),
    诱饵 N1->Trap->Goal (高权0.9低垒0.1), 死胡同 Trap_DeadEnd。"""
    nodes = {
        'N1':   {'energy': 0.30, 'value': 5.0, 'type': 'number', 'role': 'initial'},
        'N2':   {'energy': 0.35, 'value': 2.0, 'type': 'number', 'role': 'given'},
        'OP1':  {'energy': 0.40, 'type': 'operation', 'op_type': 'subtraction'},
        'Goal': {'energy': 0.0, 'type': 'answer'},
        'Trap_WrongOp_addition': {'energy': 0.10, 'type': 'trap',
                                  'trap_type': 'wrong_op', 'wrong_op': 'addition'},
        'Trap_DeadEnd': {'energy': 0.10, 'type': 'trap', 'trap_type': 'dead_end'},
    }
    edges = {
        ('N1', 'OP1'): {'weight': 0.6, 'migration_barrier': 0.3, 'allowed_domains': ['math']},
        ('N2', 'OP1'): {'weight': 0.6, 'migration_barrier': 0.3, 'allowed_domains': ['math']},
        ('OP1', 'Goal'): {'weight': 0.8, 'migration_barrier': 0.2, 'allowed_domains': ['math']},
        ('N1', 'Trap_WrongOp_addition'): {'weight': 0.9, 'migration_barrier': 0.1,
                                          'allowed_domains': ['math']},
        ('Trap_WrongOp_addition', 'Goal'): {'weight': 0.55, 'migration_barrier': 0.3,
                                            'allowed_domains': ['math']},
        ('N1', 'Trap_DeadEnd'): {'weight': 0.8, 'migration_barrier': 0.1,
                                 'allowed_domains': ['math']},
    }
    return {'nodes': nodes, 'edges': edges}


COMPLETE_PATHS = [
    ['N1', 'OP1', 'Goal'],
    ['N1', 'Trap_WrongOp_addition', 'Goal'],
    ['N1', 'Trap_DeadEnd'],            # 不完整路径也须守恒
    ['N2', 'OP1', 'Goal'],
]

FIELD_MODES = ['unified', 'v1_blocking', 'v2_tunneling', 'high_couple',
               'resonant', 'resonant_hybrid', 'labelfree']
ARRHENIUS_MODES = ['arrhenius', 'arrhenius_hybrid']


def make_field(mode, graph, arrhenius_T=0.3):
    f = DeposonField()
    f.arrhenius_T = arrhenius_T          # spawn 前设置 (实例属性, process_path 时读取)
    f.spawn_from_graph(graph, mode=mode)
    return f


# ---------------------------------------------------------------- 1. 幺正性
@pytest.mark.parametrize('mode', FIELD_MODES)
@pytest.mark.parametrize('path', COMPLETE_PATHS)
def test_unitarity_field_modes(mode, path):
    """所有非 arrhenius 模式: t+r+a=1, 容差 1e-12"""
    field = make_field(mode, make_graph())
    res = field.process_path(path, path_energy=1.0)
    s = res['transmitted'] + res['reflected'] + res['dissipated']
    assert abs(s - 1.0) < TOL, f'{mode} {path}: t+r+a={s}'
    assert not any(math.isnan(res[k]) for k in ('transmitted', 'reflected', 'dissipated'))


@pytest.mark.parametrize('mode', ARRHENIUS_MODES)
@pytest.mark.parametrize('T', [0.05, 0.1, 0.3, 1.0, 1e6])
@pytest.mark.parametrize('path', COMPLETE_PATHS)
def test_unitarity_arrhenius(mode, T, path):
    """arrhenius 系: t+r+a+barrier_loss=1, 容差 1e-12 (含 T→0 极限)"""
    field = make_field(mode, make_graph(), arrhenius_T=T)
    res = field.process_path(path, path_energy=1.0)
    s = (res['transmitted'] + res['reflected'] + res['dissipated']
         + res['barrier_loss'])
    assert abs(s - 1.0) < TOL, f'{mode} T={T} {path}: sum={s}'


# ---------------------------------------------------------------- 2. 条件等效
def test_arrhenius_high_T_degenerates_to_unified():
    """T_eff→∞ (T=1e6) 时 k=exp(-b/T)→1: 逐路径数值近似一致 + argmax 路径选择一致。
    注 [C3]: 极限命题, 非逐位一致; 用 rtol=1e-5 锁定。"""
    g = make_graph()
    fu = make_field('unified', g)
    fa = make_field('arrhenius', g, arrhenius_T=1e6)
    for path in COMPLETE_PATHS:
        ru, ra = fu.process_path(path), fa.process_path(path)
        assert ra['barrier_loss'] < 1e-4, 'k→1 时势垒损失应→0'
        assert abs(ru['transmitted'] - ra['transmitted']) < 1e-5
        assert ru['fate'] == ra['fate']
    # argmax 路径选择一致
    def best(f):
        return max(COMPLETE_PATHS,
                   key=lambda p: f.process_path(p)['transmitted'])
    assert best(make_field('unified', make_graph())) == \
           best(make_field('arrhenius', make_graph(), arrhenius_T=1e6))


def test_arrhenius_zero_barrier_is_exactly_unified():
    """b=0 ⇒ k=1 恒等: arrhenius 与 unified 逐位一致 (任何 T)。"""
    g = make_graph()
    for e in g['edges'].values():
        e['migration_barrier'] = 0.0
    fu = make_field('unified', g)
    fa = make_field('arrhenius', g, arrhenius_T=0.1)
    for path in COMPLETE_PATHS:
        ru, ra = fu.process_path(path), fa.process_path(path)
        assert ra['barrier_loss'] == 0.0
        assert ru['transmitted'] == ra['transmitted']  # 逐位
        assert ru['fate'] == ra['fate']


def test_question_level_arrhenius_high_T_equivalence(monkeypatch):
    """逐题层面: T=1e6 arrhenius 与 unified 同 seed 逐题一致 (predicted+best_path)。"""
    orig_init = DeposonField.__init__

    def patched(self, *a, **kw):
        orig_init(self, *a, **kw)
        self.arrhenius_T = 1e6
    monkeypatch.setattr(DeposonField, '__init__', patched)

    mock = LLMBackend(mode='mock')
    questions = [
        ("小明有5个苹果，给了小红2个，还剩几个？", 3.0),
        ("商店里每支笔3元，小明买了4支，一共要付多少钱？", 12.0),
        ("有24个苹果，平均分给6个小朋友，每人几个？", 4.0),
    ]
    for q, ans in questions:
        au = DeposonAgentSystem(llm_backend=mock, mode='unified')
        aa = DeposonAgentSystem(llm_backend=mock, mode='arrhenius')
        ru = BenchmarkEvaluator(au, use_validation=False).evaluate_math(q, ans)
        ra = BenchmarkEvaluator(aa, use_validation=False).evaluate_math(q, ans)
        assert ru['best_path'] == ra['best_path'], q
        assert ru['predicted_answer'] == ra['predicted_answer'], q
        assert ru['is_correct'] == ra['is_correct'], q


def test_path_integral_K1_is_single_trajectory():
    """路径积分 K=1 ⇒ 单轨迹 argmax: Born 聚合退化为该轨迹本身。"""
    g = make_graph()
    seed = 7
    r = path_integral_born(g['nodes'], g['edges'],
                           lambda: make_field('unified', g), K=1, T=0.5, seed=seed)
    rng = np.random.default_rng(seed)
    start, goal = find_start_goal(g['nodes'])
    single = boltzmann_walk(g['nodes'], g['edges'], start, goal, 0.5, rng)
    assert len(r['trajectories']) == 1
    assert r['trajectories'][0]['path'] == single
    assert r['best_path'] == single  # 唯一轨迹即 argmax


def test_boltzmann_T_zero_is_argmax():
    """Boltzmann T→0 ⇒ 出边选择退化为边能 argmax (低能=高w低b), 零涨落。"""
    g = make_graph()
    # 50 次 T=0 walk 全部逐位一致, 且每步都走 (w-b) 最大边
    paths = set()
    for s in range(50):
        rng = np.random.default_rng(s)
        p = boltzmann_walk(g['nodes'], g['edges'], 'N1', 'Goal', 0.0, rng)
        paths.add(tuple(p))
    assert len(paths) == 1
    greedy = list(paths)[0]
    assert greedy[1] == 'Trap_WrongOp_addition'  # w-b=0.9-0.1=0.8 最大 → 无场时贪心被诱饵捕获
    # T=1e-6 softmax 分支 (不触发 argmax 捷径) 也应在 50 次内全部 argmax
    for s in range(50):
        rng = np.random.default_rng(1000 + s)
        p = boltzmann_walk(g['nodes'], g['edges'], 'N1', 'Goal', 1e-6, rng)
        assert tuple(p) == greedy


def test_resonant_zero_detuning_equals_unified():
    """resonant δ=0 ⇒ unified: 把 resonant 实际散射输入 (E_photon=(1+cos)/2) 回写为
    图节点 energy 后, unified 在该路径上的逐节点 t/r/a 与 resonant 逐位一致。
    同时验证共轭映射公式本身: 记录的散射输入 == 外部重算的 (1+cos(path_emb,·))/2。"""
    g = make_graph()
    path = ['N1', 'OP1', 'Goal']

    # 1) 捕获 resonant 模式的实际散射输入
    recorded = {}
    orig_scatter = DeposonState.scatter

    def spy(self, photon_energy):
        recorded[self.id] = photon_energy
        return orig_scatter(self, photon_energy)

    fr = make_field('resonant', g)
    DeposonState.scatter = spy
    try:
        res_r = fr.process_path(path)
    finally:
        DeposonState.scatter = orig_scatter

    # 2) 外部重算共轭映射值并断言公式一致
    embs = [fr.deposons[n].center for n in path]
    m = np.mean(embs, axis=0)
    path_emb = m / np.linalg.norm(m)
    for n in path:
        expect = float((1.0 + np.dot(path_emb, fr.deposons[n].center)) / 2.0)
        assert abs(recorded[n] - expect) < 1e-15, f'E_photon公式不一致: {n}'

    # 3) δ=0 条件构造: 节点 energy := resonant 散射输入 (E*)。
    #    嵌入只依赖节点id, 与energy无关 ⇒ g2 上 resonant 的散射输入仍是 E*,
    #    此时共振能=E* ⇒ δ≡0; unified 的散射输入=节点energy=E*。两者应逐位一致。
    g2 = copy.deepcopy(g)
    for n in path:
        g2['nodes'][n]['energy'] = recorded[n]
    fr2 = make_field('resonant', g2)
    fu = make_field('unified', g2)
    res_r2 = fr2.process_path(path)
    res_u = fu.process_path(path)
    # δ≡0 验证: per_node delta 应全为 0
    assert all(pn['delta'] == 0.0 for pn in res_r2['per_node'])
    assert all(pn['delta'] == 0.0 for pn in res_u['per_node'])
    for pn_r, pn_u in zip(res_r2['per_node'], res_u['per_node']):
        assert pn_r['transmitted'] == pn_u['transmitted']
        assert pn_r['reflected'] == pn_u['reflected']
        assert pn_r['dissipated'] == pn_u['dissipated']
    assert res_r2['transmitted'] == res_u['transmitted']
    assert res_r2['fate'] == res_u['fate']


def test_labelfree_type_shuffle_bitwise():
    """labelfree: type 标签任意打乱 ⇒ g 绑定与逐路径结果逐位一致。"""
    g1 = make_graph()
    g2 = copy.deepcopy(g1)
    rng = np.random.default_rng(123)
    types = [attrs['type'] for attrs in g2['nodes'].values()]
    rng.shuffle(types)  # 打乱标签 (含 trap/answer/operation 错位)
    for attrs, t in zip(g2['nodes'].values(), types):
        attrs['type'] = t
    f1 = make_field('labelfree', g1)
    f2 = make_field('labelfree', g2)
    for nid in g1['nodes']:
        d1, d2 = f1.deposons[nid], f2.deposons[nid]
        assert d1.g_couple == d2.g_couple, nid
        assert d1.g_aether == d2.g_aether, nid
    for path in COMPLETE_PATHS:
        r1, r2 = f1.process_path(path), f2.process_path(path)
        assert r1['transmitted'] == r2['transmitted']
        assert r1['fate'] == r2['fate']


def test_labelfree_source_reads_no_type_label():
    """静态检查: _apply_labelfree_bindings 源码不得读取 type 标签"""
    src = inspect.getsource(DeposonField._apply_labelfree_bindings)
    assert "'type'" not in src and '"type"' not in src


# ---------------------------------------------------------------- 3. 决定论
@pytest.mark.parametrize('mode', FIELD_MODES + ARRHENIUS_MODES)
def test_field_determinism(mode):
    outs = []
    for _ in range(2):
        f = make_field(mode, make_graph(), arrhenius_T=0.3)
        outs.append([f.process_path(p)['transmitted'] for p in COMPLETE_PATHS])
    assert outs[0] == outs[1]


def test_boltzmann_pathintegral_determinism():
    g = make_graph()
    r1 = boltzmann_annealed(g['nodes'], g['edges'],
                            lambda: make_field('unified', g), K=8, seed=42)
    r2 = boltzmann_annealed(g['nodes'], g['edges'],
                            lambda: make_field('unified', g), K=8, seed=42)
    assert r1['best_path'] == r2['best_path']
    assert [t['path'] for t in r1['trajectories']] == [t['path'] for t in r2['trajectories']]
    p1 = path_integral_born(g['nodes'], g['edges'],
                            lambda: make_field('unified', g), K=8, seed=42)
    p2 = path_integral_born(g['nodes'], g['edges'],
                            lambda: make_field('unified', g), K=8, seed=42)
    assert p1['born_weights'] == p2['born_weights']
    assert p1['best_path'] == p2['best_path']


# ---------------------------------------------------------------- 5. 物理公式一致性与边界
def test_vectorized_vs_sequential_consistency():
    """向量化散射与串行散射公式一致性: 同题同变体, 逐候选 transmitted/fate 一致。
    注意: 向量化路径不实现 resonant/arrhenius 通道 (photon_mode/edge_mode 不参与
    process_paths_batch) —— 属文档声明的条件限制, 见 docstring [C4]。
    [C4] use_vectorized=True 仅在 photon_mode='energy' 且 edge_mode=None 时与串行
    等效; 论文若报告向量化结果需声明该前提。"""
    mock = LLMBackend(mode='mock')
    q = "小明有5个苹果，给了小红2个，还剩几个？"
    outs = []
    for vec in (False, True):
        agent = DeposonAgentSystem(llm_backend=mock, mode='unified')
        agent.use_vectorized = vec
        r = agent.reason(q, domain_hint='math', n_candidates=10)
        outs.append([(c['path'], round(c['final_score'], 12), c['fate'])
                     for c in r['all_candidates']])
    assert outs[0] == outs[1], '向量化与串行散射结果不一致'


def test_scatter_boundary_g_zero():
    """g_couple=0 ⇒ 无反射; g=ga=0 ⇒ 完全透射; 大失谐 ⇒ 反射→0。均无 NaN。"""
    d = DeposonState(id='t', center=np.zeros(4), g_couple=0.0, g_aether=0.3,
                     resonance_energy=0.2)
    s = d.scatter(0.2)
    assert s['reflected'] == 0.0 and abs(s['transmitted'] + s['dissipated'] - 1) < TOL
    d2 = DeposonState(id='t2', center=np.zeros(4), g_couple=0.0, g_aether=0.0,
                      resonance_energy=0.2)
    s2 = d2.scatter(0.2)
    assert s2['transmitted'] == 1.0 and s2['reflected'] == 0.0 and s2['dissipated'] == 0.0
    d3 = DeposonState(id='t3', center=np.zeros(4), g_couple=5.0, g_aether=0.0,
                      resonance_energy=0.0)
    s3 = d3.scatter(1e9)  # 极大失谐 → resonance_factor→0 → 全透射
    assert abs(s3['transmitted'] - 1.0) < 1e-6
    assert abs(s3['transmitted'] + s3['reflected'] + s3['dissipated'] - 1) < TOL


def test_scatter_negative_g_undefended_documented():
    """[C1] 现状锁定: 负 g_aether 无防御。g_aether=-0.5 时 t=1/(1+0-0.5)=2>1
    (仍守恒但超1); g_aether=-1 时 denom=0 → 除零。论文需声明前置条件 g>=0。"""
    d = DeposonState(id='neg', center=np.zeros(4), g_couple=0.0, g_aether=-0.5,
                     resonance_energy=0.2)
    s = d.scatter(0.2)
    assert s['transmitted'] > 1.0  # 锁定现状行为 (文档化缺口, 非理想行为)


def test_arrhenius_negative_T_and_barrier_defense():
    """T<=0 由 max(T,1e-9) 防御 (不 NaN); 负 barrier 被 k=min(1,·) 截断 (无损失)。"""
    g = make_graph()
    f = make_field('arrhenius', g, arrhenius_T=-1.0)
    res = f.process_path(['N1', 'OP1', 'Goal'])
    assert not math.isnan(res['transmitted'])
    assert abs(res['transmitted'] + res['reflected'] + res['dissipated']
               + res['barrier_loss'] - 1) < TOL
    g2 = make_graph()
    for e in g2['edges'].values():
        e['migration_barrier'] = -5.0   # 负势垒 ⇒ k=min(1, e^{+…})=1
    f2 = make_field('arrhenius', g2, arrhenius_T=0.3)
    res2 = f2.process_path(['N1', 'OP1', 'Goal'])
    assert res2['barrier_loss'] == 0.0


def test_arrhenius_kramers_weight_prefactor_bounded():
    """Kramers 修正在 w∈[0,1] 下 k=w·exp(-b/T) ≤ 1 恒成立, 且 ≤ 纯 arrhenius 的 k。"""
    g = make_graph()
    fa = make_field('arrhenius', g, arrhenius_T=0.3)
    fk = make_field('arrhenius_hybrid', g, arrhenius_T=0.3)
    for path in COMPLETE_PATHS:
        ra, rk = fa.process_path(path), fk.process_path(path)
        assert rk['transmitted'] <= ra['transmitted'] + 1e-15
        assert not math.isnan(rk['transmitted'])


def test_resonant_ephoton_bounded():
    """共轭映射 E_photon=(1+cos)/2 ∈ [0,1]: 随机路径/节点嵌入下区间成立"""
    rng = np.random.default_rng(0)
    for _ in range(200):
        a = rng.normal(size=64)
        b = rng.normal(size=64)
        a /= np.linalg.norm(a)
        b /= np.linalg.norm(b)
        e = float((1.0 + np.dot(a, b)) / 2.0)
        assert 0.0 <= e <= 1.0


def test_boltzmann_negative_T_rejected():
    g = make_graph()
    rng = np.random.default_rng(0)
    with pytest.raises(ValueError):
        boltzmann_walk(g['nodes'], g['edges'], 'N1', 'Goal', -0.1, rng)


def test_born_rule_aggregation_math():
    """Born 规则: 组权重 = Σ transmitted²; argmax 组获胜。构造已知透射率验证。"""
    g = make_graph()
    r = path_integral_born(g['nodes'], g['edges'],
                           lambda: make_field('unified', g), K=10, T=0.5, seed=3)
    total = sum(r['born_weights'].values())
    expect = sum(t['transmitted'] ** 2 for t in r['trajectories'])
    assert abs(total - expect) < TOL
    best_group = max(r['born_weights'].items(), key=lambda kv: kv[1])[0]
    assert r['best_group'] == best_group


# ---------------------------------------------------------------- 集成 (真实缓存图)
def _load_cached_graph():
    """从持久缓存读一张真实 LLM 分解图 (零 API); 无缓存则 skip。"""
    try:
        from deposon_agents_v1_3 import KimiLLMBackend
        llm = KimiLLMBackend.__new__(KimiLLMBackend)
        from deposon_agents_v1_3 import PersistentCache
        llm.cache = PersistentCache(cache_dir='/mnt/agents/output/deposon_cache',
                                    version='1.3.0')
        llm.PROMPT_VERSION = '1.3.1'
        llm.LEGACY_PROMPT_VERSIONS = ['1.3.0']
        q = "一件衣服原价120元，打八折后再满50减10，最终多少钱？"
        for pv in ['1.3.1', '1.3.0']:
            key = llm._legacy_cache_key('decompose', q, pv)
            c = llm.cache.get(key)
            if c is not None and c.get('source') == 'kimi_api':
                return KimiLLMBackend._deserialize_decomposition(c)
    except Exception:
        pass
    return None


def test_real_graph_unitarity_and_arrhenius_equivalence():
    """真实 LLM 图上: 全候选路径幺正性 + arrhenius T=1e6 argmax 与 unified 一致"""
    g = _load_cached_graph()
    if g is None:
        pytest.skip('无真实缓存图')
    sys.setrecursionlimit(10000)
    # 枚举全部 N1→Goal 简单路径
    edges = g['edges']
    paths = []
    stack = [('N1', ['N1'])]
    while stack:
        cur, pth = stack.pop()
        if cur == 'Goal':
            paths.append(pth)
            continue
        for (u, v) in edges:
            if u == cur and v not in pth:
                stack.append((v, pth + [v]))
    assert len(paths) >= 2, '应同时存在正确链与诱饵路径'
    fu = make_field('unified', g)
    fa = make_field('arrhenius', g, arrhenius_T=1e6)
    for pth in paths:
        res = fu.process_path(pth)
        assert abs(res['transmitted'] + res['reflected'] + res['dissipated'] - 1) < TOL
        ra = fa.process_path(pth)
        assert abs(ra['transmitted'] + ra['reflected'] + ra['dissipated']
                   + ra['barrier_loss'] - 1) < TOL
    best_u = max(paths, key=lambda p: fu.process_path(p)['transmitted'])
    best_a = max(paths, key=lambda p: fa.process_path(p)['transmitted'])
    assert best_u == best_a, 'T=1e6 时 arrhenius argmax 路径应与 unified 一致'
