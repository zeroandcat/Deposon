#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================
# Deposon Agents v1.3 —— 薄转发 shim (候选④合并, 2026-08-30)
# 实现已并入 deposon_agents.py (单模块 + version 配置);
# 本模块仅以单行类属性钉定 version="1.3", 与原 deposon_agents_v1_3.py
# (版本 1.3.0) 的默认数值行为逐位一致。全部方法为继承的同一实现。
# ============================================================
import deposon_agents as _core
from deposon_agents import (  # noqa: F401  (同名对象直接转发, `is` 同一)
    AgentConfig, DeposonState, EtherChannel, VectorizedDeposonScatter,
    PersistentCache, LLMBackend, ConceptDecomposer, deterministic_embedding,
    HundredQuestionBenchmark, TrapBenchmark,
)


class KimiLLMBackend(_core.KimiLLMBackend):
    """v1.3 钉定: PROMPT_VERSION=1.3.1, max_tokens 默认 4000,
    LEGACY_PROMPT_VERSIONS=["1.3.0"], decompose 无英文 mini 链/规则缓存短路。"""
    version = "1.3"
    PROMPT_VERSION = _core._V13_PROMPT_VERSION
    DECOMPOSE_PROMPT = _core._V13_DECOMPOSE_PROMPT
    LEGACY_PROMPT_VERSIONS = list(_core._V13_LEGACY_PROMPT_VERSIONS)


class DeposonField(_core.DeposonField):
    """v1.3 钉定: 运算节点 g_c/g_a=0.3/0.2; high_couple 为 g_couple x3;
    支持 resonant/resonant_hybrid/labelfree/arrhenius/arrhenius_hybrid 模式;
    process_path 记录含 delta 与 barrier_loss。"""
    version = "1.3"


class DeposonAgentSystem(_core.DeposonAgentSystem):
    """v1.3 钉定: ablation 的 high_couple 固定 {'mode': 'high_couple'};
    内部 DeposonField 随 version="1.3"。"""
    version = "1.3"


class BenchmarkEvaluator(_core.BenchmarkEvaluator):
    """v1.3 钉定: 折叠不去重连续操作数; 无 computed_answer 兜底。"""
    version = "1.3"
