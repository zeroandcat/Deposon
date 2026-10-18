# -*- coding: utf-8 -*-
# ============================================================
# 候选④合并测试: deposon_agents.py 单模块 + version 配置,
# deposon_agents_v1_3/v1_4 薄转发 shim。
#
# 红绿纪律: 测公开行为 (decompose/spawn_from_graph/process_path/reason/
# evaluate_math/ablation_study/cot_solve/import 面), 不测私有实现细节。
# 冻结哈希 (TestFrozenEquivalence) 的常数在合并前由原始 deposon_agents_v1_3.py /
# deposon_agents_v1_4.py 生成 (2026-08-30, sha256 over 规范化 JSON),
# 合并后逐位不变即通过 —— 见 docs/REFACTOR_v2.md 候选④。
# ============================================================
import hashlib
import importlib
import json
import math
import os
import random
import sys
import time

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.pop('KIMI_API_KEY', None)
os.environ.pop('DECOMPOSE_FORCE_STEPS', None)
os.environ.pop('DEPOSON_V14_HIGH_COUPLE_ALIAS', None)

import deposon_agents as core
import deposon_agents_v1_3 as v13
import deposon_agents_v1_4 as v14

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------------------------------------------------------------- 工具
def canon(obj):
    """确定性规范化 (与合并前基线 harness 逐字一致)."""
    if isinstance(obj, dict):
        return [[canon(k), canon(v)] for k, v in
                sorted(obj.items(), key=lambda kv: repr(kv[0]))]
    if isinstance(obj, (list, tuple)):
        return [canon(x) for x in obj]
    if isinstance(obj, (set, frozenset)):
        return sorted((canon(x) for x in obj), key=repr)
    if isinstance(obj, np.ndarray):
        return {'__ndarray__': canon(obj.tolist())}
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.floating,)):
        return float(obj)
    if isinstance(obj, float):
        if math.isnan(obj):
            return 'NaN'
        if math.isinf(obj):
            return 'Inf' if obj > 0 else '-Inf'
        return obj
    return obj


def H(obj):
    blob = json.dumps(canon(obj), sort_keys=True, ensure_ascii=False).encode('utf-8')
    return hashlib.sha256(blob).hexdigest()


def reset_seeds():
    random.seed(42)
    np.random.seed(42)


QUERIES_CN = [
    "小明有5个苹果，给了小红2个，还剩几个？",
    "一件商品原价120元，先打八折再减10元，现价多少元？",
    "每组6个橙子，一共7组，平均每个篮子装几个？",
]
QUERIES_EN = [
    "Natalia sold clips to 48 friends in April, and then she sold half as many clips in May. How many clips did she sell altogether in April and May?",
    "A robe takes 2 bolts of blue fiber and half that much white fiber. How many bolts in total does it take?",
]

TOY_GRAPH = {
    'nodes': {
        'N1': {'energy': 0.3, 'type': 'number', 'value': 6.0},
        'N2': {'energy': 0.35, 'type': 'number', 'value': 2.0},
        'OP1': {'energy': 0.4, 'type': 'operation', 'op_type': 'multiplication'},
        'Goal': {'energy': 0.0, 'type': 'answer'},
        'Trap_X': {'energy': 0.1, 'type': 'trap', 'trap_type': 'wrong_op',
                   'wrong_op': 'addition'},
        'Trap_Dead': {'energy': 0.1, 'type': 'trap', 'trap_type': 'dead_end'},
    },
    'edges': {
        ('N1', 'OP1'): {'weight': 0.6, 'migration_barrier': 0.3},
        ('N2', 'OP1'): {'weight': 0.6, 'migration_barrier': 0.3},
        ('OP1', 'Goal'): {'weight': 0.8, 'migration_barrier': 0.2},
        ('N1', 'Trap_X'): {'weight': 0.9, 'migration_barrier': 0.1},
        ('Trap_X', 'Goal'): {'weight': 0.55, 'migration_barrier': 0.3},
        ('N1', 'Trap_Dead'): {'weight': 0.8, 'migration_barrier': 0.1},
    },
}
FIELD_MODES = ['unified', 'v1_blocking', 'v2_tunneling', 'high_couple',
               'resonant', 'resonant_hybrid', 'labelfree',
               'arrhenius', 'arrhenius_hybrid']
PATHS = [['N1', 'OP1', 'Goal'], ['N1', 'Trap_X', 'Goal'], ['N2', 'OP1', 'Goal'],
         ['N1', 'Trap_Dead']]

CANNED_SPEC = json.dumps({
    "query_type": "math",
    "numbers": [{"value": 48.0, "order": 1}, {"value": 0.5, "order": 2}],
    "operations": [{"op": "multiplication", "operands": [1, 2]},
                   {"op": "addition", "operands": [3, 1]}],
    "traps": [{"type": "surface_addition", "why": "x"}],
    "difficulty": "easy", "computed_answer": 72.0})


# ---------------------------------------------------------------- 冻结任务体
def task_rule_fallback(M):
    reset_seeds()
    out = []
    llm = M.KimiLLMBackend(enable_cache=False)
    for q in QUERIES_CN + QUERIES_EN:
        g = llm.decompose(q)
        out.append(M.KimiLLMBackend._serialize_decomposition(g))
    out.append(llm.get_stats())
    return out


def task_mocked_decompose(M):
    reset_seeds()
    traces = {}
    for tag, q in [('cn', QUERIES_CN[1]), ('en', QUERIES_EN[0])]:
        for force_steps in (False, True):
            llm = M.KimiLLMBackend(enable_cache=False)
            calls = []

            def fake_chat(system_prompt, user_content):
                calls.append(hashlib.sha256(
                    (system_prompt + '||' + user_content).encode('utf-8')).hexdigest()[:16])
                return CANNED_SPEC

            llm._chat = fake_chat
            if force_steps:
                os.environ['DECOMPOSE_FORCE_STEPS'] = '1'
            try:
                g = llm.decompose(q)
            finally:
                os.environ.pop('DECOMPOSE_FORCE_STEPS', None)
            traces[f'{tag}_force{int(force_steps)}'] = {
                'calls': calls,
                'graph': M.KimiLLMBackend._serialize_decomposition(g),
            }
    return traces


def task_legacy_cache(M, cdir):
    reset_seeds()
    os.makedirs(cdir, exist_ok=True)
    probe = M.KimiLLMBackend(cache_dir=cdir, cache_version='probe')
    q = QUERIES_CN[0]
    legacy_entry = probe._serialize_decomposition({
        'nodes': {'N1': {'energy': 0.3, 'value': 9.0, 'type': 'number', 'role': 'x'},
                  'Goal': {'energy': 0.0, 'type': 'answer'}},
        'edges': {('N1', 'Goal'): {'weight': 0.8, 'migration_barrier': 0.2}},
        'query_type': 'math', 'numbers': [9.0], 'number_roles': {0: 'x'},
        'operations': [], 'operation_chain': [], 'trap_nodes': {},
        'computed_answer': 9.0, 'difficulty': 'easy', 'raw_llm_traps': [],
        'source': 'kimi_api'})
    pv = probe.LEGACY_PROMPT_VERSIONS[0] if probe.LEGACY_PROMPT_VERSIONS else '1.3.0'
    probe.cache.set(probe._legacy_cache_key('decompose', q, pv), legacy_entry)
    rule_entry = dict(legacy_entry)
    rule_entry['source'] = 'rule_fallback'
    probe.cache.set(probe._cache_key('decompose', q), rule_entry)
    probe.cache.save()
    llm = M.KimiLLMBackend(cache_dir=cdir, cache_version='probe')
    llm._chat = lambda s, u: CANNED_SPEC
    g = llm.decompose(q)
    return {'graph': M.KimiLLMBackend._serialize_decomposition(g),
            'stats': llm.get_stats(), 'legacy_pver_used': pv}


def task_field_physics(M):
    out = {}
    for mode in FIELD_MODES:
        reset_seeds()
        f = M.DeposonField()
        f.spawn_from_graph(TOY_GRAPH, mode=mode)
        rec = {'bindings': {nid: (d.g_couple, d.g_aether, d.resonance_energy)
                            for nid, d in f.deposons.items()}}
        rec['paths'] = [f.process_path(list(p)) for p in PATHS]
        rec['stats'] = f.get_stats()
        out[mode] = rec
    return out


def task_system_endtoend(M):
    out = {}
    for mode in ['unified', 'v1_blocking', 'v2_tunneling', 'high_couple']:
        reset_seeds()
        agent = M.DeposonAgentSystem(llm_backend=M.LLMBackend(mode='mock'),
                                     mode=mode)
        ev = M.BenchmarkEvaluator(agent, use_validation=False)
        recs = []
        for q, ans in [(QUERIES_CN[0], 3.0), (QUERIES_CN[1], 86.0),
                       (QUERIES_EN[0], 72.0)]:
            recs.append(ev.evaluate_math(q, correct_answer=ans))
        out[mode] = recs
    return out


def task_ablation(M):
    reset_seeds()
    agent = M.DeposonAgentSystem(llm_backend=M.LLMBackend(mode='mock'))
    res = agent.ablation_study(QUERIES_CN[1], domain_hint='math')
    return {'ablation': res, 'report_sha': hashlib.sha256(
        agent.report_ablation(res).encode('utf-8')).hexdigest()}


def task_evaluator_edges(M):
    reset_seeds()
    agent = M.DeposonAgentSystem(llm_backend=M.LLMBackend(mode='mock'))
    ev = M.BenchmarkEvaluator(agent, use_validation=False)
    graph_dup = {
        'nodes': {'N1': {'type': 'number', 'value': 5.0},
                  'N2': {'type': 'number', 'value': 3.0},
                  'N3': {'type': 'number', 'value': 3.0},
                  'OP1': {'type': 'operation', 'op_type': 'addition'}},
        'operation_chain': [{'node': 'OP1', 'op': 'addition',
                             'operands': [2, 2, 3]}],
        'trap_nodes': {}, 'computed_answer': 11.0,
    }
    graph_ca = {
        'nodes': {'N1': {'type': 'number', 'value': 5.0},
                  'N2': {'type': 'number', 'value': 3.0}},
        'operation_chain': [{'node': 'OP1', 'op': 'division', 'operands': [1]}],
        'trap_nodes': {}, 'computed_answer': 42.5,
    }
    return {
        'dup_operands': ev._compute_answer_from_path(graph_dup, ['N1', 'OP1']),
        'computed_answer_fallback': ev._compute_answer_from_path(graph_ca, None),
        'trap_path': ev._compute_answer_from_path(
            dict(graph_dup, trap_nodes={'OP1': 'subtraction'}), ['N1', 'OP1']),
    }


def task_chat_transport(M, monkeypatch):
    """stub requests.post: 403配额/空content/正常 三场景."""
    reset_seeds()
    monkeypatch.setattr(time, 'sleep', lambda s: None)
    out = {}
    for scenario in ['quota403', 'empty_content', 'ok']:
        llm = M.KimiLLMBackend(api_key='probe-key', enable_cache=False,
                               timeout=90.0, max_retries=3)
        post_calls = []

        class FakeResp:
            def __init__(self, status, text, payload=None):
                self.status_code = status
                self.text = text
                self._payload = payload or {}

            def json(self):
                return self._payload

        def fake_post(url, headers=None, json=None, timeout=None):
            post_calls.append({'url': url, 'timeout': timeout, 'payload': json})
            if scenario == 'quota403':
                return FakeResp(403, 'usage limit exceeded')
            if scenario == 'empty_content':
                return FakeResp(200, '', {'usage': {'total_tokens': 5},
                                          'choices': [{'message': {'content': ''}}]})
            return FakeResp(200, '', {'usage': {'total_tokens': 7},
                                      'choices': [{'message': {'content': 'OK'}}]})

        class FakeRequests:
            post = staticmethod(fake_post)

        impl_mod = sys.modules[M.KimiLLMBackend._chat.__module__]
        monkeypatch.setattr(impl_mod, 'requests', FakeRequests)
        try:
            res, exc = llm._chat('sys', 'user'), None
        except Exception as e:
            res, exc = None, f'{type(e).__name__}: {e}'
        out[scenario] = {
            'result': res, 'exception': exc,
            'n_posts': len(post_calls),
            'timeouts': [c['timeout'] for c in post_calls],
            'max_tokens_payload': [c['payload']['max_tokens'] for c in post_calls],
            'stats': llm.get_stats(),
        }
    return out


def task_cot(M):
    reset_seeds()
    llm = M.KimiLLMBackend(enable_cache=False)
    llm._chat = lambda s, u: 'Some reasoning... #### 42'
    r1 = llm.cot_solve(QUERIES_EN[0])
    llm._chat = lambda s, u: 'no number here'
    r2 = llm.cot_solve(QUERIES_EN[1])
    return {'ok_case': r1, 'bad_case': r2, 'stats': llm.get_stats()}


# ---------------------------------------------------------------- 转发与同一性
class TestShimForwarding:
    SHARED = ['AgentConfig', 'DeposonState', 'EtherChannel',
              'VectorizedDeposonScatter', 'PersistentCache', 'LLMBackend',
              'ConceptDecomposer', 'deterministic_embedding',
              'HundredQuestionBenchmark', 'TrapBenchmark']
    PINNED = ['KimiLLMBackend', 'DeposonField', 'DeposonAgentSystem',
              'BenchmarkEvaluator']

    @pytest.mark.parametrize('name', SHARED)
    def test_shared_names_are_identical_objects(self, name):
        assert getattr(v13, name) is getattr(core, name)
        assert getattr(v14, name) is getattr(core, name)

    def test_v14_extra_names_identical(self):
        assert v14.resolve_high_couple_config is core.resolve_high_couple_config
        assert v14.HIGH_COUPLE_GAIN is core.HIGH_COUPLE_GAIN

    @pytest.mark.parametrize('name', PINNED)
    def test_pinned_classes_single_implementation(self, name):
        """钉定类是核心类的单行 version 钉定子类: 全部方法为同一实现。"""
        import inspect
        for shim, ver in ((v13, '1.3'), (v14, '1.4')):
            cls = getattr(shim, name)
            assert issubclass(cls, getattr(core, name))
            assert cls.version == ver
            # shim 子类不定义任何新方法 (仅 version/常量类属性)
            for attr, val in cls.__dict__.items():
                assert not inspect.isfunction(val), (shim.__name__, name, attr)
            # 核心类的每个方法在钉定类上就是同一对象
            # (version/PROMPT_VERSION 等类属性是有意的钉定覆盖, 不在此列)
            for meth, impl in cls.__mro__[1].__dict__.items():
                if meth.startswith('__'):
                    continue
                if not (inspect.isfunction(impl)
                        or isinstance(impl, (staticmethod, classmethod))):
                    continue
                assert inspect.getattr_static(cls, meth) is impl, \
                    (shim.__name__, name, meth)

    def test_no_duplicate_hierarchy(self):
        """同名双层级已消除: 核心实现只在 deposon_agents 定义一次。"""
        for name in self.PINNED:
            assert getattr(core, name).__module__ == 'deposon_agents'
            for shim in (v13, v14):
                assert getattr(shim, name).__mro__[1] is getattr(core, name)


# ---------------------------------------------------------------- version 钉定行为
class TestVersionPinning:
    def test_agent_config_validation(self):
        assert core.AgentConfig().version == '1.4'
        assert core.AgentConfig(version='1.3').version == '1.3'
        with pytest.raises(ValueError):
            core.AgentConfig(version='9.9')
        with pytest.raises(ValueError):
            core.DeposonField(version='9.9')

    def test_backend_prompt_and_token_defaults(self):
        b13 = v13.KimiLLMBackend(enable_cache=False)
        b14 = v14.KimiLLMBackend(enable_cache=False)
        assert (b13.PROMPT_VERSION, b13.max_tokens) == ('1.3.1', 4000)
        assert (b14.PROMPT_VERSION, b14.max_tokens) == ('1.3.2', 8000)
        assert b13.LEGACY_PROMPT_VERSIONS == ['1.3.0']
        assert b14.LEGACY_PROMPT_VERSIONS == ['1.3.1', '1.3.0']
        # 显式 max_tokens 覆盖不受 version 影响
        assert v13.KimiLLMBackend(enable_cache=False, max_tokens=123).max_tokens == 123

    def test_core_default_is_v14_and_explicit_override(self):
        assert core.KimiLLMBackend(enable_cache=False).version == '1.4'
        b = core.KimiLLMBackend(enable_cache=False, version='1.3')
        assert (b.PROMPT_VERSION, b.max_tokens) == ('1.3.1', 4000)
        assert core.DeposonField(version=core.AgentConfig(version='1.3')).version == '1.3'

    def test_cache_keys_bit_identical_across_paths(self):
        """shim 与核心显式 version 的缓存键逐位一致 (缓存布局不变)。"""
        a = v13.KimiLLMBackend(enable_cache=False)
        b = core.KimiLLMBackend(enable_cache=False, version='1.3')
        assert a._cache_key('decompose', 'q') == b._cache_key('decompose', 'q')
        c = v14.KimiLLMBackend(enable_cache=False)
        d = core.KimiLLMBackend(enable_cache=False)  # 默认 1.4
        assert c._cache_key('decompose_mini', 'q') == d._cache_key('decompose_mini', 'q')

    def test_field_operation_binding_versions(self):
        f13 = v13.DeposonField()
        f13.spawn_from_graph(TOY_GRAPH, mode='unified')
        f14 = v14.DeposonField()
        f14.spawn_from_graph(TOY_GRAPH, mode='unified')
        deg = 3  # OP1 度数: N1,N2,Goal
        assert f13.deposons['OP1'].g_couple == pytest.approx(0.3 * (1 + 0.02 * deg))
        assert f13.deposons['OP1'].g_aether == pytest.approx(0.2)
        assert f14.deposons['OP1'].g_couple == pytest.approx(0.15 * (1 + 0.02 * deg))
        assert f14.deposons['OP1'].g_aether == pytest.approx(0.05)

    def test_high_couple_semantics_per_version(self):
        f13 = v13.DeposonField()
        f13.spawn_from_graph(TOY_GRAPH, mode='high_couple')
        u13 = v13.DeposonField()
        u13.spawn_from_graph(TOY_GRAPH, mode='unified')
        # v1.3: g_couple x3, g_aether 不变
        for nid in TOY_GRAPH['nodes']:
            assert f13.deposons[nid].g_couple == pytest.approx(
                u13.deposons[nid].g_couple * 3.0)
            assert f13.deposons[nid].g_aether == u13.deposons[nid].g_aether
        # v1.4: g_aether=0 + g_couple x HIGH_COUPLE_GAIN
        f14 = v14.DeposonField()
        f14.spawn_from_graph(TOY_GRAPH, mode='high_couple')
        u14 = v14.DeposonField()
        u14.spawn_from_graph(TOY_GRAPH, mode='unified')
        for nid in TOY_GRAPH['nodes']:
            assert f14.deposons[nid].g_aether == 0.0
            assert f14.deposons[nid].g_couple == pytest.approx(
                u14.deposons[nid].g_couple * v14.HIGH_COUPLE_GAIN)

    def test_process_path_record_keys_per_version(self):
        r13 = v13.DeposonField()
        r13.spawn_from_graph(TOY_GRAPH)
        out13 = r13.process_path(['N1', 'OP1', 'Goal'])
        assert 'barrier_loss' in out13 and 'delta' in out13['per_node'][0]
        r14 = v14.DeposonField()
        r14.spawn_from_graph(TOY_GRAPH)
        out14 = r14.process_path(['N1', 'OP1', 'Goal'])
        assert 'barrier_loss' not in out14 and 'delta' not in out14['per_node'][0]

    def test_v13_only_modes_fallthrough_on_v14(self):
        """v1.3 专属模式 (resonant/labelfree/arrhenius) 在 v1.4 场无分支,
        行为与 unified 逐位一致 (= 原 v1_4 fallthrough)。"""
        for mode in ('resonant', 'labelfree', 'arrhenius'):
            fu = v14.DeposonField()
            fu.spawn_from_graph(TOY_GRAPH, mode='unified')
            fm = v14.DeposonField()
            fm.spawn_from_graph(TOY_GRAPH, mode=mode)
            assert H(fu.process_path(['N1', 'OP1', 'Goal'])) == \
                H(fm.process_path(['N1', 'OP1', 'Goal']))
        # v1.3 场则确实激活 (arrhenius 产生 barrier_loss>0)
        fa = v13.DeposonField()
        fa.spawn_from_graph(TOY_GRAPH, mode='arrhenius')
        assert fa.process_path(['N1', 'OP1', 'Goal'])['barrier_loss'] > 0

    def test_ablation_high_couple_entry_per_version(self):
        a13 = v13.DeposonAgentSystem(llm_backend=v13.LLMBackend(mode='mock'))
        a14 = v14.DeposonAgentSystem(llm_backend=v14.LLMBackend(mode='mock'))
        r13 = a13.ablation_study(QUERIES_CN[1])
        r14 = a14.ablation_study(QUERIES_CN[1])
        assert set(r13) == set(r14) == {
            'no_deposon', 'v1_blocking', 'v2_tunneling', 'unified', 'high_couple'}
        # v1.4 E9.3: high_couple 结果不同于 v1_blocking (真修复, 非别名)
        assert H(r14['high_couple']) != H(r14['v1_blocking'])

    def test_resolve_high_couple_config_switch(self, monkeypatch):
        assert v14.resolve_high_couple_config() == {
            'mode': 'high_couple', 'use_deposon': True}
        monkeypatch.setenv('DEPOSON_V14_HIGH_COUPLE_ALIAS', '1')
        assert v14.resolve_high_couple_config() == {
            'mode': 'v1_blocking', 'use_deposon': True}

    def test_evaluator_version_follows_agent(self):
        a13 = v13.DeposonAgentSystem(llm_backend=v13.LLMBackend(mode='mock'))
        assert core.BenchmarkEvaluator(a13).version == '1.3'
        a14 = v14.DeposonAgentSystem(llm_backend=v14.LLMBackend(mode='mock'))
        assert core.BenchmarkEvaluator(a14).version == '1.4'
        assert v13.BenchmarkEvaluator(a14).version == '1.3'  # shim 钉定优先

    def test_evaluator_fold_dedup_per_version(self):
        g = {'nodes': {'N1': {'type': 'number', 'value': 5.0},
                       'N2': {'type': 'number', 'value': 3.0}},
             'operation_chain': [{'node': 'OP1', 'op': 'addition',
                                  'operands': [1, 1, 2]}],
             'trap_nodes': {}, 'computed_answer': None}
        a13 = v13.DeposonAgentSystem(llm_backend=v13.LLMBackend(mode='mock'))
        a14 = v14.DeposonAgentSystem(llm_backend=v14.LLMBackend(mode='mock'))
        p13, _, _ = v13.BenchmarkEvaluator(a13)._compute_answer_from_path(
            g, ['N1', 'OP1'])
        p14, _, _ = v14.BenchmarkEvaluator(a14)._compute_answer_from_path(
            g, ['N1', 'OP1'])
        assert p13 == 5.0 + 5.0 + 3.0   # v1.3: 不去重, 重复作用
        assert p14 == 5.0 + 3.0         # v1.4: 连续重复折叠


# ---------------------------------------------------------------- 冻结等价性
# 常数由合并前原始模块 (deposon_agents_v1_3.py @66dbdc74 / _v1_4.py @6a34dab3,
# 2026-08-30) 用本文件 task_* 任务体生成; sha256 over 规范化 JSON。
FROZEN = {
    '1.3': {
        'rule_fallback': '3f50b85d88d7244b729af58d56167654234ac336dfe7934de9cc68de2cce7e43',
        'mocked_decompose': '772d5937241b2e458feb73e934180aba9716e91194949cb73ad1e47f382f43f1',
        'legacy_cache': 'f2121c70fa5645288ace51acbc475142f83ced122aa20d2c9a47423bc3279619',
        'field_physics': '043902e8675e309948254e53bafdc883efdb91ecec7397721749157d683e504b',
        'system_endtoend': '03df882c941791b0c006a579ed414267d9790e97c4eb52e3951c48adc62c483f',
        'ablation': '31d77d4289404c46b27be5d93eb629248fedc3273999ca6881a6532816892a68',
        'ablation_alias': '31d77d4289404c46b27be5d93eb629248fedc3273999ca6881a6532816892a68',
        'evaluator_edges': '816c7d630d8a5e1dd1526f640646db0f14f8a447f88504f0d6eb3ea7d8c6c21d',
        'chat_transport': '58250868eb2decab682278206e210dffc1de204dedd2a23b7645b20dee9b13e5',
    },
    '1.4': {
        'rule_fallback': '3f50b85d88d7244b729af58d56167654234ac336dfe7934de9cc68de2cce7e43',
        'mocked_decompose': '9ee70b2990f69216fb408f7946ff26584b6c0f854201592f729104379c4d4de9',
        'legacy_cache': '82ed9d2e72d515b61957b8b747730f567a41f60cb55dc7ef5daf05de165f3567',
        'field_physics': 'bb2003d2c76259d2f2ab45da578a4a65aa20172f9d64f3bfcb8ca8ef0ed86caf',
        'system_endtoend': 'dc812a20ef84709e58d5f845139a36a624238df7323a6d160aca6c04d2629fb2',
        'ablation': 'c27305543f9b34de845bd8f192edaa6ade8f80367e51645d3c238ff5149e3b60',
        'ablation_alias': '9dc3b96e286845974c85d52b475ad86e537a9c7cf1cc2af46ca912803b8fcfb9',
        'evaluator_edges': '48381412cf0183bf2a0b7acca343b8773d835d02fd8145c1f30eb5868adce3b4',
        'chat_transport': '29321adb9d5bf9751e5a3353e76aefdf225bd9775382b60ed2ac714a94043787',
        'cot': '8508997ee3cfc29c97f1dd3b6918f361fe3a07ee0b51e2f6049044e1ffd4b211',
    },
}


class TestFrozenEquivalence:
    """合并后 shim 的公开行为与合并前原始模块逐位一致 (sha256)。"""
    SHIMS = {'1.3': v13, '1.4': v14}

    def _check(self, ver, key, value):
        expected = FROZEN[ver][key]
        assert H(value) == expected, f'{key}@{ver} 行为漂移'

    @pytest.mark.parametrize('ver', ['1.3', '1.4'])
    def test_rule_fallback_frozen(self, ver):
        self._check(ver, 'rule_fallback', task_rule_fallback(self.SHIMS[ver]))

    @pytest.mark.parametrize('ver', ['1.3', '1.4'])
    def test_mocked_decompose_frozen(self, ver):
        self._check(ver, 'mocked_decompose',
                    task_mocked_decompose(self.SHIMS[ver]))

    @pytest.mark.parametrize('ver', ['1.3', '1.4'])
    def test_legacy_cache_frozen(self, ver, tmp_path):
        self._check(ver, 'legacy_cache',
                    task_legacy_cache(self.SHIMS[ver], str(tmp_path / 'c')))

    @pytest.mark.parametrize('ver', ['1.3', '1.4'])
    def test_field_physics_frozen(self, ver):
        self._check(ver, 'field_physics', task_field_physics(self.SHIMS[ver]))

    @pytest.mark.parametrize('ver', ['1.3', '1.4'])
    def test_system_endtoend_frozen(self, ver):
        self._check(ver, 'system_endtoend',
                    task_system_endtoend(self.SHIMS[ver]))

    @pytest.mark.parametrize('ver', ['1.3', '1.4'])
    def test_ablation_frozen(self, ver):
        self._check(ver, 'ablation', task_ablation(self.SHIMS[ver]))

    def test_ablation_legacy_alias_frozen(self, monkeypatch):
        # v1.3: 开关无关 (无别名史); v1.4: E9.3 旧别名复现
        for ver in ('1.3', '1.4'):
            monkeypatch.setenv('DEPOSON_V14_HIGH_COUPLE_ALIAS', '1')
            self._check(ver, 'ablation_alias', task_ablation(self.SHIMS[ver]))
            monkeypatch.delenv('DEPOSON_V14_HIGH_COUPLE_ALIAS')

    @pytest.mark.parametrize('ver', ['1.3', '1.4'])
    def test_evaluator_edges_frozen(self, ver):
        self._check(ver, 'evaluator_edges',
                    task_evaluator_edges(self.SHIMS[ver]))

    @pytest.mark.parametrize('ver', ['1.3', '1.4'])
    def test_chat_transport_frozen(self, ver, monkeypatch):
        self._check(ver, 'chat_transport',
                    task_chat_transport(self.SHIMS[ver], monkeypatch))

    def test_cot_frozen_v14(self):
        self._check('1.4', 'cot', task_cot(v14))


# ---------------------------------------------------------------- import 面
class TestImportSweep:
    """全部既有 import 路径不破 (含重构前即失败、本次顺带修复的 strategyqa)。"""
    CONSUMERS = ['run_benchmark_v1_3', 'run_benchmark_v1_4_gsm8k',
                 'run_benchmark_v1_4_strategyqa', 'run_g2_ensemble',
                 'run_v19_benchmark_fixes']

    @pytest.mark.parametrize('mod', CONSUMERS)
    def test_consumer_module_imports(self, mod):
        importlib.import_module(mod)

    def test_strategyqa_gap_fixed(self):
        """run_benchmark_v1_4_strategyqa 引用的 resolve_high_couple_config
        重构前 ImportError (脚本 sys.path 指向仓库外旧副本); 合并后 shim
        转发该函数, 且脚本仓库目录优先, 缺口修复。"""
        m = importlib.import_module('run_benchmark_v1_4_strategyqa')
        assert m.VARIANTS['high_couple'] == {
            'mode': 'high_couple', 'use_deposon': True}
