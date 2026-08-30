#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================
# Deposon Agents —— 仿物理AGI系统 (v1.3/v1.4 合并单模块, 候选④)
# 凝子(Deposon)统一场论算法实现
# 版本: 由 AgentConfig/类属性 version ∈ {"1.3","1.4"} 钉定
#   "1.3" = 原 deposon_agents_v1_3.py (1.3.0) 默认行为
#   "1.4" = 原 deposon_agents_v1_4.py (1.4.0, GSM8K真实数据评测 + CoT基线) 默认行为
# 日期: 2026-08-22 (合并: 2026-08-30, 见 docs/REFACTOR_v2.md 候选④)
# 兼容: deposon_agents_v1_3.py / deposon_agents_v1_4.py 保留为钉定版本的薄转发,
#       全部既有 import 路径与默认数值行为逐位不变。
# ============================================================
# 特性:
#   - 向量化Deposon散射 (NumPy矩阵运算)
#   - 无限维正交以太能量耗散
#   - 持久化JSON缓存 (版本隔离, 线程安全)
#   - LLM后端接口层 (Mock/DeepSeek/OpenAI)
#   - Kimi真实API后端 (kimi-for-coding) + 规则引擎自动降级
#   - LLM结构化语义分解 -> 多步运算链图构建
#   - 百题消融评估框架
# ============================================================

import numpy as np
import math
import random
import re
import json
import hashlib
import time
import os
import threading
from typing import Dict, List, Tuple, Optional, Set, Callable, Any
from dataclasses import dataclass, field
from collections import defaultdict, deque

try:
    import requests
except ImportError:  # pragma: no cover
    requests = None

# ============================================================
# 模块零: 版本配置 (候选④合并) —— AgentConfig + version 钉定协议
# ============================================================
# 版本分异行为全部以实例/类属性 `version` 为唯一开关:
#   - 类属性 version = "1.4" 为模块默认 (= 原 v1_4 行为);
#   - 构造函数均接受 version=... 显式覆盖;
#   - deposon_agents_v1_3.py / deposon_agents_v1_4.py 两个薄转发 shim
#     以 `class X(deposon_agents.X): version = "1.3"/"1.4"` 单行钉定,
#     从而旧 import 路径的默认行为逐位不变 (全部方法为继承的同一实现)。

AGENTS_VERSIONS = ("1.3", "1.4")


@dataclass(frozen=True)
class AgentConfig:
    """agents 层版本配置: version 锁定全部 v1.3/v1.4 分异行为。"""
    version: str = "1.4"

    def __post_init__(self):
        if self.version not in AGENTS_VERSIONS:
            raise ValueError(
                f"未知 agents 版本: {self.version!r} (期望 {AGENTS_VERSIONS})")


def _resolve_version(version, fallback: str) -> str:
    """version 形参统一解析: None->fallback; str/AgentConfig 皆可; 校验合法性。"""
    if version is None:
        return fallback
    if isinstance(version, AgentConfig):
        return version.version
    if version not in AGENTS_VERSIONS:
        raise ValueError(
            f"未知 agents 版本: {version!r} (期望 {AGENTS_VERSIONS})")
    return version


# ============================================================
# 模块一: Deposon核心 —— 凝子单体态
# ============================================================

@dataclass
class DeposonState:
    """
    凝子单体态: 统一v1(阻塞)与v2(隧穿)的准粒子

    物理类比:
    - g_couple: 光子-Deposon耦合强度 (v1: 阻塞过滤)
    - g_aether: 以太耦合开放度 (v2: 能量耗散/隧穿)
    - resonance_energy: 共振能量 (Feshbach共振)

    三通道散射: E_in = E_transmitted + E_reflected + E_aether
    """
    id: str
    center: np.ndarray
    g_couple: float = 1.0
    g_aether: float = 0.0
    resonance_energy: float = 0.0
    conjugate_map: Dict[str, str] = field(default_factory=dict)

    def scatter(self, photon_energy: float) -> Dict[str, float]:
        """Feshbach共振散射 —— 确保能量守恒"""
        detuning = abs(photon_energy - self.resonance_energy)
        resonance_factor = 1.0 / (1.0 + detuning ** 2)
        g_eff = self.g_couple * resonance_factor
        denom = 1.0 + g_eff + self.g_aether
        return {
            'transmitted': 1.0 / denom,
            'reflected': g_eff / denom,
            'dissipated': self.g_aether / denom
        }

    def get_limit(self) -> str:
        """判断当前处于哪个极限态"""
        eta = self.g_aether / (self.g_couple + 1e-10)
        if eta < 0.1:
            return 'v1_blocking'
        elif eta > 10.0:
            return 'v2_tunneling'
        else:
            return 'mixed'

    def __repr__(self):
        limit = self.get_limit()
        return (f"DeposonState(id={self.id}, limit={limit}, "
                f"g_couple={self.g_couple:.3f}, g_aether={self.g_aether:.3f})")


# ============================================================
# 模块二: EtherChannel —— 无限维正交以太
# ============================================================

class EtherChannel:
    """
    无限维正交以太通道

    物理类比:
    - 无限维希尔伯特空间的正交补空间 H_aether
    - 能量一旦沉积，Poincare回归失效，永不可恢复
    - 作为认知系统的无限热浴，吸收错误能量防止"过热"
    """

    def __init__(self, capacity: float = float('inf')):
        self.capacity = capacity
        self._deposits: List[Dict] = []
        self._total_dissipated: float = 0.0
        self._locked: bool = False

    def deposit(self, energy: float, source: str = "",
                metadata: Optional[Dict] = None) -> bool:
        if energy <= 0:
            return False
        if self.capacity != float('inf') and self._total_dissipated + energy > self.capacity:
            energy = self.capacity - self._total_dissipated
            if energy <= 0:
                return False
        self._deposits.append({
            'energy': energy,
            'source': source,
            'metadata': metadata or {}
        })
        self._total_dissipated += energy
        self._locked = True
        return True

    def get_total_dissipated(self) -> float:
        return self._total_dissipated

    def query(self, source_filter: Optional[str] = None) -> List[Dict]:
        if source_filter:
            return [d for d in self._deposits if d['source'] == source_filter]
        return list(self._deposits)

    def reset(self):
        self._deposits.clear()
        self._total_dissipated = 0.0
        self._locked = False

    def is_locked(self) -> bool:
        return self._locked

    def to_dict(self) -> Dict:
        return {
            'deposits': self._deposits,
            'total_dissipated': self._total_dissipated,
            'locked': self._locked
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'EtherChannel':
        ec = cls()
        ec._deposits = data.get('deposits', [])
        ec._total_dissipated = data.get('total_dissipated', 0.0)
        ec._locked = data.get('locked', False)
        return ec

    def __repr__(self):
        return (f"EtherChannel(dissipated={self._total_dissipated:.4f}, "
                f"n={len(self._deposits)}, locked={self._locked})")


# ============================================================
# 模块三: 向量化Deposon散射引擎 (v1.2核心优化)
# ============================================================

class VectorizedDeposonScatter:
    """
    向量化Deposon散射引擎

    核心优化: 用NumPy矩阵运算替代Python循环
    性能目标: 1000条路径散射 < 1ms
    """

    def scatter_batch(self,
                      g_couple: np.ndarray,
                      g_aether: np.ndarray,
                      resonance_energy: np.ndarray,
                      photon_energy: np.ndarray) -> Dict[str, np.ndarray]:
        """批量计算N个Deposon的散射参数"""
        detuning = np.abs(photon_energy - resonance_energy)
        resonance_factor = 1.0 / (1.0 + detuning ** 2)
        g_eff = g_couple * resonance_factor
        denom = 1.0 + g_eff + g_aether
        return {
            'transmitted': 1.0 / denom,
            'reflected': g_eff / denom,
            'dissipated': g_aether / denom
        }

    def process_paths_batch(self,
                            paths: List[List[str]],
                            path_energies: np.ndarray,
                            node_ids: List[str],
                            g_couple: np.ndarray,
                            g_aether: np.ndarray,
                            resonance_energy: np.ndarray,
                            node_energy_map: Dict[str, float]) -> List[Dict[str, Any]]:
        """批量处理多条路径的Deposon散射"""
        results = []
        for i, path in enumerate(paths):
            path_energy = path_energies[i]
            path_node_indices = []
            path_photon_energies = []
            for node_id in path:
                if node_id in node_ids:
                    path_node_indices.append(node_ids.index(node_id))
                    path_photon_energies.append(node_energy_map.get(node_id, 0.0))

            if not path_node_indices:
                results.append({
                    'fate': 'empty',
                    'transmitted': 0.0,
                    'reflected': 0.0,
                    'dissipated': 0.0
                })
                continue

            idx_arr = np.array(path_node_indices)
            pe_arr = np.array(path_photon_energies)
            sr = self.scatter_batch(
                g_couple[idx_arr],
                g_aether[idx_arr],
                resonance_energy[idx_arr],
                pe_arr
            )
            t, r, a = sr['transmitted'], sr['reflected'], sr['dissipated']

            E_prev = path_energy
            total_reflected = 0.0
            total_dissipated = 0.0
            for j in range(len(t)):
                reflected_here = E_prev * r[j]
                dissipated_here = E_prev * a[j]
                E_prev = E_prev * t[j]
                total_reflected += reflected_here
                total_dissipated += dissipated_here

            max_r = float(np.max(r)) if len(r) > 0 else 0.0
            max_a = float(np.max(a)) if len(a) > 0 else 0.0
            fate = 'blocked' if max_r > 0.7 else                    ('tunneling' if max_a > 0.5 else 'transmitted')

            results.append({
                'fate': fate,
                'transmitted': E_prev / path_energy,
                'reflected': total_reflected / path_energy,
                'dissipated': total_dissipated / path_energy,
                'final_energy': E_prev,
                'max_reflection_rate': max_r,
                'max_dissipation_rate': max_a
            })
        return results


# ============================================================
# 模块四: 持久化缓存
# ============================================================

class PersistentCache:
    """磁盘持久化缓存 —— JSON存储，版本隔离"""

    def __init__(self, cache_dir: str = "./deposon_cache", version: str = "1.2.0"):
        self.cache_dir = cache_dir
        self.version = version
        self._memory_cache: Dict[str, Any] = {}
        self._stats = {'hits': 0, 'misses': 0, 'disk_reads': 0, 'disk_writes': 0}
        self._lock = threading.RLock()  # v1.3: 线程安全缓存
        self.version_dir = os.path.join(cache_dir, f"v{version}")
        os.makedirs(self.version_dir, exist_ok=True)
        self._index_file = os.path.join(self.version_dir, "cache_index.json")
        self._load_index()

    def _load_index(self):
        if os.path.exists(self._index_file):
            try:
                with open(self._index_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if data.get('version') == self.version:
                        self._memory_cache = data.get('entries', {})
            except Exception:
                pass

    def _save_index(self):
        with open(self._index_file, 'w', encoding='utf-8') as f:
            json.dump({
                'version': self.version,
                'entries': self._memory_cache,
                'stats': self._stats
            }, f, ensure_ascii=False, indent=2)

    def get(self, key: str) -> Optional[Any]:
        with self._lock:
            if key in self._memory_cache:
                self._stats['hits'] += 1
                return self._memory_cache[key]
            file_path = os.path.join(self.version_dir,
                                     f"{hashlib.md5(key.encode()).hexdigest()}.json")
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        value = json.load(f)
                    self._memory_cache[key] = value
                    self._stats['hits'] += 1
                    self._stats['disk_reads'] += 1
                    return value
                except Exception:
                    pass
            self._stats['misses'] += 1
            return None

    def set(self, key: str, value: Any, persist: bool = True) -> None:
        with self._lock:
            self._memory_cache[key] = value
            if persist:
                file_path = os.path.join(self.version_dir,
                                         f"{hashlib.md5(key.encode()).hexdigest()}.json")
                tmp_path = file_path + ".tmp"
                with open(tmp_path, 'w', encoding='utf-8') as f:
                    json.dump(value, f, ensure_ascii=False, indent=2)
                os.replace(tmp_path, file_path)  # 原子写，防并发损坏
                self._stats['disk_writes'] += 1

    def get_stats(self) -> Dict:
        total = self._stats['hits'] + self._stats['misses']
        return {
            **self._stats,
            'hit_rate': self._stats['hits'] / total if total > 0 else 0.0,
            'memory_size': len(self._memory_cache)
        }

    def clear(self):
        self._memory_cache.clear()
        for f in os.listdir(self.version_dir):
            if f.endswith('.json') and f != 'cache_index.json':
                os.remove(os.path.join(self.version_dir, f))
        self._stats = {'hits': 0, 'misses': 0, 'disk_reads': 0, 'disk_writes': 0}
        self._save_index()

    def save(self):
        self._save_index()


# ============================================================
# 模块五: LLM后端接口层
# ============================================================

class LLMBackend:
    """
    LLM后端接口封装层
    模式: 'mock' | 'deepseek' | 'openai' | 'local'
    自动降级: 真实API失败时回退到mock
    """

    def __init__(self, mode: str = 'mock', api_key: Optional[str] = None,
                 model: str = 'deepseek-chat', timeout: float = 10.0):
        self.mode = mode
        self.api_key = api_key
        self.model = model
        self.timeout = timeout
        self._stats = {'calls': 0, 'fallbacks': 0, 'errors': 0}

    def decompose(self, query: str) -> Dict[str, Any]:
        self._stats['calls'] += 1
        try:
            if self.mode == 'mock':
                return self._mock_decompose(query)
            elif self.mode == 'deepseek':
                return self._deepseek_decompose(query)
            elif self.mode == 'openai':
                return self._openai_decompose(query)
            else:
                return self._mock_decompose(query)
        except Exception:
            self._stats['errors'] += 1
            self._stats['fallbacks'] += 1
            return self._mock_decompose(query)

    def validate(self, query: str, reasoning_chain: List[str],
                 predicted_answer: Any) -> Dict[str, Any]:
        self._stats['calls'] += 1
        try:
            return self._mock_validate(query, reasoning_chain, predicted_answer)
        except Exception:
            self._stats['errors'] += 1
            return self._mock_validate(query, reasoning_chain, predicted_answer)

    def generate_answer(self, query: str, context: Optional[Dict] = None) -> str:
        if self.mode == 'mock':
            return self._mock_generate_answer(query, context)
        return "[需要接入真实LLM API]"

    def _mock_decompose(self, query: str) -> Dict[str, Any]:
        numbers = [float(m) for m in re.findall(r'(\d+\.?\d*)', query)]
        ops, op_order = [], []

        sub_kws = ['给', '送', '减少', '减去', '剩', '还有', '用去', '吃掉', '游走', '拿走', '去掉', '扣除']
        if any(kw in query for kw in sub_kws):
            ops.append('subtraction')
            op_order.append(('subtraction', min([query.find(kw) for kw in sub_kws if kw in query] or [999])))

        add_kws = ['买', '增加', '加上', '总共', '一共', '又', '再来', '得到']
        if any(kw in query for kw in add_kws):
            ops.append('addition')
            op_order.append(('addition', min([query.find(kw) for kw in add_kws if kw in query] or [999])))

        mul_kws = ['倍', '乘', '每', '单价', '面积', '体积', '总价']
        if any(kw in query for kw in mul_kws):
            ops.append('multiplication')
            op_order.append(('multiplication', min([query.find(kw) for kw in mul_kws if kw in query] or [999])))

        div_kws = ['平均', '分', '每人', '每份', '几组']
        if any(kw in query for kw in div_kws):
            ops.append('division')
            op_order.append(('division', min([query.find(kw) for kw in div_kws if kw in query] or [999])))

        op_order.sort(key=lambda x: x[1])
        ordered_ops = [op for op, _ in op_order]

        nodes, edges = {}, {}
        for i, n in enumerate(numbers):
            nodes[f'N{i+1}'] = {'energy': 0.3 + i * 0.05, 'value': n, 'type': 'number'}
        for i, op in enumerate(ordered_ops):
            nodes[f'OP{i+1}'] = {'energy': 0.4, 'type': 'operation', 'op_type': op}
        nodes['Goal'] = {'energy': 0.0, 'type': 'answer'}

        nids = [f'N{i+1}' for i in range(len(numbers))]
        oids = [f'OP{i+1}' for i in range(len(ordered_ops))]

        if len(oids) >= 1 and len(nids) >= 2:
            for nid in nids[:2]:
                edges[(nid, oids[0])] = {'weight': 0.6, 'migration_barrier': 0.3, 'allowed_domains': ['math']}
            prev_op = oids[0]
            for i in range(1, len(oids)):
                edges[(prev_op, oids[i])] = {'weight': 0.7, 'migration_barrier': 0.2, 'allowed_domains': ['math']}
                if i + 1 < len(nids):
                    edges[(nids[i+1], oids[i])] = {'weight': 0.6, 'migration_barrier': 0.3, 'allowed_domains': ['math']}
                prev_op = oids[i]
            edges[(oids[-1], 'Goal')] = {'weight': 0.8, 'migration_barrier': 0.2, 'allowed_domains': ['math']}
        elif len(oids) == 1:
            for nid in nids:
                edges[(nid, oids[0])] = {'weight': 0.6, 'migration_barrier': 0.3, 'allowed_domains': ['math']}
            edges[(oids[0], 'Goal')] = {'weight': 0.8, 'migration_barrier': 0.2, 'allowed_domains': ['math']}
        else:
            if nids:
                edges[(nids[0], 'Goal')] = {'weight': 0.8, 'migration_barrier': 0.2, 'allowed_domains': ['math']}

        if len(numbers) >= 2:
            wrong_ops = [op for op in ['addition', 'subtraction', 'multiplication', 'division'] if op not in ops]
            for i, wop in enumerate(wrong_ops[:2]):
                tid = f'Trap_WrongOp_{wop}'
                nodes[tid] = {'energy': 0.1, 'type': 'trap', 'trap_type': 'wrong_op', 'wrong_op': wop}
                if nids:
                    edges[(nids[0], tid)] = {'weight': 0.9, 'migration_barrier': 0.1, 'allowed_domains': ['math']}

        if len(numbers) >= 1:
            nodes['Trap_DeadEnd'] = {'energy': 0.1, 'type': 'trap', 'trap_type': 'dead_end'}
            if nids:
                edges[(nids[0], 'Trap_DeadEnd')] = {'weight': 0.8, 'migration_barrier': 0.1, 'allowed_domains': ['math']}

        return {
            'nodes': nodes,
            'edges': edges,
            'query_type': 'math' if numbers else 'commonsense',
            'numbers': numbers,
            'operations': ordered_ops
        }

    def _mock_validate(self, query: str, reasoning_chain: List[str],
                       predicted_answer: Any) -> Dict[str, Any]:
        score = 0.7
        issues = []
        traps = [n for n in reasoning_chain if 'Trap' in n]
        if traps:
            score -= 0.3 * len(traps)
            issues.append(f"路径包含陷阱节点: {traps}")
        if len(reasoning_chain) < 3:
            score -= 0.2
            issues.append("路径过短")
        if reasoning_chain and reasoning_chain[-1] != 'Goal':
            score -= 0.2
            issues.append("路径未到达Goal")
        nums_q = re.findall(r'\d+\.?\d*', query)
        n_used = len([n for n in reasoning_chain if n.startswith('N')])
        if n_used < len(nums_q):
            score -= 0.1
            issues.append(f"未使用所有数字 ({n_used}/{len(nums_q)})")
        score = max(0.0, min(1.0, score))
        return {
            'is_valid': score > 0.6,
            'validation_score': score,
            'issues': issues,
            'confidence': score
        }

    def _mock_generate_answer(self, query: str, context: Optional[Dict] = None) -> str:
        if context and 'predicted_answer' in context:
            return f"根据分析，答案是{context['predicted_answer']}。"
        return "根据推理路径分析，问题已解决。"

    def _deepseek_decompose(self, query: str) -> Dict[str, Any]:
        if not self.api_key:
            raise ValueError("DeepSeek API key未设置")
        raise NotImplementedError("需要requests库和有效API key")

    def _openai_decompose(self, query: str) -> Dict[str, Any]:
        if not self.api_key:
            raise ValueError("OpenAI API key未设置")
        raise NotImplementedError("需要openai库和有效API key")

    def get_stats(self) -> Dict:
        return dict(self._stats)


# ============================================================
# 模块六: Kimi增强LLM后端
# ============================================================

# ---- v1.3 钉定常量 (version="1.3" 时 KimiLLMBackend 使用; 与 v1.4 类属性逐位区分) ----
_V13_PROMPT_VERSION = "1.3.1"
_V13_LEGACY_PROMPT_VERSIONS = ["1.3.0"]

_V13_DECOMPOSE_PROMPT = """你是数学应用题语义分解器。把题目分解为严格JSON（不要任何额外文字、不要markdown围栏）。

输出schema:
{"query_type":"math","numbers":[{"value":24.0,"role":"初始量","order":1}],"operations":[{"op":"multiplication","operands":[1,2],"reason":"单价×数量"}],"traps":[{"type":"surface_addition","why":"看到'一共'误加"}],"difficulty":"easy","computed_answer":48.0}

规则:
1. numbers: 题目中每个有意义的数字, order从1开始编号; 派生常数(如打八折->0.8, 打五折->0.5, 半价->0.5)也要作为number列入, role标"派生系数"。
2. operations: 按计算先后顺序排列。op∈{addition,subtraction,multiplication,division}。
   operands为number的order编号列表: 第一个运算给两个操作数(如[1,2]); 后续运算给[上一步结果要作用的number编号](单元素列表, 表示 上一步结果 op 该number)。
   例「先打八折再减10元」: numbers=[原价order1, 0.8派生order2, 10元order3], operations=[{op:multiplication,operands:[1,2]},{op:subtraction,operands:[3]}]
3. traps: 该题最易诱发的1~3个错误做法, type∈{surface_addition,surface_subtraction,surface_multiplication,surface_division,wrong_order,unit_confusion}。
4. computed_answer: 按operations链算出的最终数值(逐步认真计算)。
5. 【关键】先确定问题最终求的是什么量, 再选运算, 不要被表面词诱导:
   - 「每组X个, 一共Y组, 问平均每班/每箱几个」这类题, 若分组对象与所问对象其实是同一批东西(题目故意用'平均'制造除法假象), 实际求的是总量X×Y, 只有一步乘法。
   - 「有X个, 每Y个装一袋, 可以装几袋」是真除法 X÷Y。
   - 「给了/又给了/飞来」按实际增减方向判断加减, 不要只看「给」字。
6. 只输出JSON对象本身。"""


class KimiLLMBackend:
    """
    Kimi真实API LLM后端 (v1.3/v1.4 合并) —— kimi-for-coding (OpenAI兼容接口)

    特性:
    - 真实 decompose: LLM输出严格JSON (numbers/operations/traps/difficulty),
      支持多步运算链 (如「先打八折再满减」), 再按 v1.2 同款 nodes/edges 结构建图
    - 真实 validate: LLM判断推理链逻辑正确性
    - 真实 generate_answer: 自然语言回答
    - 自动降级: 任何API/解析失败 -> 规则引擎基线 (继承v1.2正则逻辑), 统计fallbacks
    - 持久化缓存: PersistentCache 线程安全, key=sha256(kind|prompt_version|query)
    - API key 仅从构造参数或环境变量 KIMI_API_KEY 读取, 不写入任何输出
    """

    ENDPOINT = "https://api.kimi.com/coding/v1/chat/completions"
    # 候选④: version 类属性 (=shim 钉定位); 下列 prompt 常量为 v1.4 默认,
    # __init__ 在 version="1.3" 时以实例属性覆盖为 _V13_* 值。
    version = "1.4"
    PROMPT_VERSION = "1.3.2"

    DECOMPOSE_PROMPT = """你是数学应用题语义分解器(支持中文和英文题目)。把题目分解为严格JSON（不要任何额外文字、不要markdown围栏）。英文题同样处理, traps的why字段可用英文。

输出schema:
{"query_type":"math","numbers":[{"value":24.0,"role":"初始量","order":1}],"operations":[{"op":"multiplication","operands":[1,2],"reason":"单价×数量"}],"traps":[{"type":"surface_addition","why":"看到'一共'误加"}],"difficulty":"easy","computed_answer":48.0}

规则:
1. numbers: 题目中每个有意义的数字, order从1开始编号; 派生常数(如打八折->0.8, 打五折->0.5, 半价->0.5)也要作为number列入, role标"派生系数"。
2. operations: 按计算先后顺序排列。op∈{addition,subtraction,multiplication,division}。
   operands为number的order编号列表: 第一个运算给两个操作数(如[1,2]); 后续运算给[上一步结果要作用的number编号](单元素列表, 表示 上一步结果 op 该number)。
   例「先打八折再减10元」: numbers=[原价order1, 0.8派生order2, 10元order3], operations=[{op:multiplication,operands:[1,2]},{op:subtraction,operands:[3]}]
3. traps: 该题最易诱发的1~3个错误做法, type∈{surface_addition,surface_subtraction,surface_multiplication,surface_division,wrong_order,unit_confusion}。
4. computed_answer: 按operations链算出的最终数值(逐步认真计算)。
5. 【关键】先确定问题最终求的是什么量, 再选运算, 不要被表面词诱导:
   - 「每组X个, 一共Y组, 问平均每班/每箱几个」这类题, 若分组对象与所问对象其实是同一批东西(题目故意用'平均'制造除法假象), 实际求的是总量X×Y, 只有一步乘法。
   - 「有X个, 每Y个装一袋, 可以装几袋」是真除法 X÷Y。
   - 「给了/又给了/飞来」按实际增减方向判断加减, 不要只看「给」字。
6. 只输出JSON对象本身。"""

    VALIDATE_PROMPT = """你是推理链验证器。判断给定推理链是否逻辑正确解答了题目。
输出严格JSON: {"score":0.0~1.0,"verdict":"correct或incorrect","issues":["问题1",...]}
只输出JSON对象本身。"""

    # v1.4: 精简分解prompt (英文/难题防reasoning耗尽max_tokens导致空content)
    DECOMPOSE_MINI_PROMPT = """Decompose the math word problem into JSON only. No explanation, no reasoning text.
{"numbers":[{"value":number,"order":1},...],"operations":[{"op":"addition|subtraction|multiplication|division","operands":[order,...]}],"computed_answer":number}
Rules: operands refer to numbers' order (1-based). First operation takes two operands; each later operation takes a single operand meaning (previous_result op that_number). computed_answer is the final numeric result. Output the JSON object only. / 分解数学题只输出JSON: operands是numbers的order编号, 第一个运算两个操作数, 后续运算单元素表示 上一步结果 op 该数值。只输出JSON。"""

    # v1.4 W2: 抗死循环兜底prompt —— 部分英文题在纯schema指令下触发reasoning死循环
    # (max_tokens全烧在reasoning_content, content为空)。实测"先算一行再输出简易JSON"可绕开。
    DECOMPOSE_STEPS_SUFFIX = """
First compute briefly in one line. Then output ONLY this JSON object:
{"numbers":[<num>,...],"operations":["<a> <+|−|-|*|x|/> <b> = <r>", ...],"computed_answer":<num>}
numbers: every meaningful number from the problem in order of appearance (derived constants like 0.8 for 80% discount may be appended).
operations: the calculation steps in order as arithmetic expressions. computed_answer: the final numeric result."""

    def _convert_simple_spec(self, query: str, spec: Dict) -> Dict:
        """把简易steps-JSON转成标准schema (numbers带order, operations带op/operands)。

        链语义: 首运算 [oa,ob] 双操作数; 后续运算若左操作数≈上一步结果则为 [ob] 单操作数
        (previous_result op b); 表达式引用的中间结果作为派生number追加, 保证可引用。
        无法解析的步跳过; 该路径是抗死循环兜底, 尽力而为。
        """
        raw_nums = spec.get('numbers') or []
        values = []
        for n in raw_nums:
            v = n.get('value') if isinstance(n, dict) else n
            try:
                values.append(float(v))
            except Exception:
                pass
        if not values:
            raise ValueError("simple spec无numbers")

        def find_order(x, used):
            for i, v in enumerate(values):
                if i not in used and abs(v - x) < 1e-9:
                    return i + 1
            for i, v in enumerate(values):  # 允许复用
                if abs(v - x) < 1e-9:
                    return i + 1
            return None

        op_map = {'+': 'addition', '-': 'subtraction', '−': 'subtraction',
                  '*': 'multiplication', 'x': 'multiplication', '×': 'multiplication',
                  '/': 'division', '÷': 'division'}
        operations = []
        used_operand_orders = set()
        prev_r = None
        for expr in spec.get('operations') or []:
            if isinstance(expr, dict):  # 模型偶尔直接给标准schema
                operations.append(expr)
                continue
            m = re.match(r'\s*([\-0-9\.]+)\s*([+\-−\*x×/÷])\s*([\-0-9\.]+)\s*=\s*([\-0-9\.]+)',
                         str(expr))
            if not m:
                continue
            a, sym, b, r = float(m.group(1)), m.group(2), float(m.group(3)), float(m.group(4))
            op = op_map.get(sym)
            if op is None:
                continue
            oa = find_order(a, used_operand_orders)
            ob = find_order(b, used_operand_orders)
            if oa is None:
                values.append(a); oa = len(values)
            if ob is None:
                values.append(b); ob = len(values)
            if not operations:
                operands = [oa, ob]
            else:
                if prev_r is not None and abs(a - prev_r) < 1e-6:
                    operands = [ob]          # prev_result op b
                elif prev_r is not None and abs(b - prev_r) < 1e-6:
                    operands = [oa]          # prev_result op a (交换情形)
                else:
                    operands = [oa, ob]      # 并行子计算: 链形式主义表达受限, 尽力而为
            operations.append({'op': op, 'operands': operands,
                               'reason': f'steps-fallback: {expr}'})
            used_operand_orders.update(operands)
            prev_r = r
            # 中间结果作为派生number登记, 便于后续步引用
            if find_order(r, set()) is None:
                values.append(r)
        return {'query_type': 'math',
                'numbers': [{'value': v, 'order': i + 1,
                             'role': 'derived' if i >= len(raw_nums) else 'unknown'}
                            for i, v in enumerate(values)],
                'operations': operations,
                'traps': [], 'difficulty': 'unknown',
                'computed_answer': spec.get('computed_answer')}

    def __init__(self, api_key: Optional[str] = None,
                 model: str = "kimi-for-coding",
                 endpoint: Optional[str] = None,
                 cache_dir: str = "/mnt/agents/output/deposon_cache",
                 cache_version: str = "1.3.0",
                 timeout: float = 90.0, max_retries: int = 3,
                 max_tokens: Optional[int] = None, enable_cache: bool = True,
                 version=None):
        # 候选④: version None -> 类属性钉定值 (shim 子类 "1.3" / 本类 "1.4")
        self.version = _resolve_version(version, type(self).version)
        if self.version == "1.3":
            # v1.3 钉定: prompt/legacy 版本与 max_tokens 默认值 (实例属性覆盖类属性)
            self.PROMPT_VERSION = _V13_PROMPT_VERSION
            self.DECOMPOSE_PROMPT = _V13_DECOMPOSE_PROMPT
            self.LEGACY_PROMPT_VERSIONS = list(_V13_LEGACY_PROMPT_VERSIONS)
        # key 只存在于运行时变量/环境变量, 绝不写入日志或输出文件
        self.api_key = api_key or os.environ.get("KIMI_API_KEY")
        self.model = model
        self.endpoint = endpoint or self.ENDPOINT
        self.timeout = timeout
        self.max_retries = max_retries
        # v1.3 默认 4000 / v1.4 默认 8000; 显式传入优先
        self.max_tokens = (max_tokens if max_tokens is not None
                           else (4000 if self.version == "1.3" else 8000))
        self._stats = {'calls': 0, 'fallbacks': 0, 'errors': 0,
                       'cache_hits': 0, 'tokens_used': 0}
        self._stats_lock = threading.Lock()
        self._quota_exhausted = False  # W1: 403 usage-limit 快速失败标志 (仅 v1.4 分支消费)
        self.cache = PersistentCache(cache_dir=cache_dir, version=cache_version) if enable_cache else None

    # ---------------- 统计 ----------------
    def _bump(self, key: str, delta: int = 1):
        with self._stats_lock:
            self._stats[key] = self._stats.get(key, 0) + delta

    def get_stats(self) -> Dict:
        with self._stats_lock:
            return dict(self._stats)

    # ---------------- HTTP 调用 (指数退避重试) ----------------
    def _chat(self, system_prompt: str, user_content: str) -> str:
        if requests is None:
            raise RuntimeError("requests库不可用")
        if not self.api_key:
            raise ValueError("Kimi API key未设置")
        if self.version != "1.3" and self._quota_exhausted:
            # v1.4 W1: 配额已耗尽时快速失败 (v1.3 无此检查)
            raise RuntimeError("配额已耗尽(403), 本窗口不再尝试API")
        headers = {"Authorization": f"Bearer {self.api_key}",
                   "Content-Type": "application/json"}
        payload = {"model": self.model, "max_tokens": self.max_tokens,
                   "messages": [{"role": "system", "content": system_prompt},
                                {"role": "user", "content": user_content}]}
        # v1.4: timeout 下限 200s; v1.3: 原样 self.timeout
        req_timeout = max(self.timeout, 200) if self.version != "1.3" else self.timeout
        last_err = None
        for attempt in range(self.max_retries):
            try:
                resp = requests.post(self.endpoint, headers=headers,
                                     json=payload, timeout=req_timeout)
                if (self.version != "1.3" and resp.status_code == 403
                        and 'usage limit' in resp.text):
                    self._quota_exhausted = True  # 计费周期配额耗尽: 快速失败, 不重试
                    raise RuntimeError("配额耗尽(403 usage limit)")
                if resp.status_code != 200:
                    raise RuntimeError(f"HTTP {resp.status_code}: {resp.text[:200]}")
                data = resp.json()
                usage = data.get('usage') or {}
                self._bump('tokens_used', int(usage.get('total_tokens', 0)))
                content = data['choices'][0]['message'].get('content')
                if not content:
                    # v1.4: 空content = reasoning耗尽max_tokens的死循环问题题; 重试同prompt无效且每次烧8k tokens
                    raise RuntimeError("空content响应(不重试)" if self.version != "1.3"
                                       else "空content响应")
                return content
            except Exception as e:
                last_err = e
                self._bump('errors')
                if (self.version != "1.3"
                        and (self._quota_exhausted or '空content' in str(e))):
                    break  # 配额耗尽/空content: 立即退出重试循环 (仅 v1.4)
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)  # 指数退避 1s,2s
        raise RuntimeError(f"Kimi API重试{self.max_retries}次仍失败: {last_err}")

    @staticmethod
    def _extract_json(text: str) -> Dict:
        """strip ```json 围栏, 正则兜底提取第一个 {...} 块"""
        t = text.strip()
        t = re.sub(r'^```(?:json)?\s*', '', t)
        t = re.sub(r'\s*```$', '', t)
        try:
            return json.loads(t)
        except Exception:
            pass
        m = re.search(r'\{.*\}', t, re.DOTALL)
        if m:
            return json.loads(m.group(0))
        raise ValueError("无法从响应中解析JSON")

    def _cache_key(self, kind: str, payload: str) -> str:
        raw = f"{kind}|prompt_v{self.PROMPT_VERSION}|{payload}"
        return hashlib.sha256(raw.encode('utf-8')).hexdigest()

    # 旧prompt版本的缓存也可复用 (仅当其为真实API结果), 避免重复计费
    LEGACY_PROMPT_VERSIONS = ["1.3.1", "1.3.0"]

    def _legacy_cache_key(self, kind: str, payload: str, pver: str) -> str:
        raw = f"{kind}|prompt_v{pver}|{payload}"
        return hashlib.sha256(raw.encode('utf-8')).hexdigest()

    @staticmethod
    def _is_english(query: str) -> bool:
        return sum(1 for ch in query if '一' <= ch <= '鿿') < 3

    # ================= decompose =================
    def decompose(self, query: str) -> Dict[str, Any]:
        if self.version == "1.3":
            return self._decompose_v13(query)
        self._bump('calls')
        english = self._is_english(query)
        kind = "decompose_mini" if english else "decompose"
        key = self._cache_key(kind, query)
        if self.cache is not None:
            cached = self.cache.get(key)
            if cached is not None and cached.get('source') == 'kimi_api':
                self._bump('cache_hits')
                return self._deserialize_decomposition(cached)
            # 旧prompt版本/完整prompt缓存复用: 只接受真实API结果, 规则降级结果不复用
            legacy_keys = [self._cache_key("decompose", query)] + \
                [self._legacy_cache_key("decompose", query, pv) for pv in self.LEGACY_PROMPT_VERSIONS]
            for lk in legacy_keys:
                if lk == key:
                    continue
                legacy = self.cache.get(lk)
                if legacy is not None and legacy.get('source') == 'kimi_api':
                    self._bump('cache_hits')
                    return self._deserialize_decomposition(legacy)
            # v1.4: 缓存的规则降级结果不短路返回 —— 继续尝试真实API, 仅在API也失败时降级
        try:
            if english:
                # 精简prompt防reasoning耗尽token; 失败则升级"先算后JSON"简易schema(抗死循环),
                # 再失败才升级完整prompt。已知死循环题可用 DECOMPOSE_FORCE_STEPS=1 跳过mini直达steps。
                if os.environ.get('DECOMPOSE_FORCE_STEPS'):
                    raw = self._chat("You are a precise math problem decomposer.",
                                     query + self.DECOMPOSE_STEPS_SUFFIX)
                    spec = self._convert_simple_spec(query, self._extract_json(raw))
                else:
                    try:
                        raw = self._chat(self.DECOMPOSE_MINI_PROMPT, query)
                        spec = self._extract_json(raw)
                    except Exception:
                        try:
                            raw = self._chat("You are a precise math problem decomposer.",
                                             query + self.DECOMPOSE_STEPS_SUFFIX)
                            spec = self._convert_simple_spec(query, self._extract_json(raw))
                        except Exception:
                            raw = self._chat(self.DECOMPOSE_PROMPT, query)
                            spec = self._extract_json(raw)
            else:
                raw = self._chat(self.DECOMPOSE_PROMPT, query)
                spec = self._extract_json(raw)
            result = self._build_from_llm_spec(query, spec)
            result['source'] = 'kimi_api'
        except Exception:
            self._bump('fallbacks')
            result = self._rule_decompose(query)
            result['source'] = 'rule_fallback'
        if self.cache is not None:
            try:
                self.cache.set(key, self._serialize_decomposition(result))
            except Exception:
                pass
        return result

    def _decompose_v13(self, query: str) -> Dict[str, Any]:
        """version="1.3" 的 decompose 路径 (原 deposon_agents_v1_3.decompose 逐字保留)。

        与 v1.4 的差异: 缓存键恒为 kind="decompose" (无英文 mini 区分);
        legacy 复用仅遍历 LEGACY_PROMPT_VERSIONS; 当前版本的规则降级缓存
        短路返回 (v1.4 不短路); 无 mini/steps 升级链, 直接用完整 prompt。
        """
        self._bump('calls')
        key = self._cache_key("decompose", query)
        if self.cache is not None:
            cached = self.cache.get(key)
            if cached is not None and cached.get('source') == 'kimi_api':
                self._bump('cache_hits')
                return self._deserialize_decomposition(cached)
            # 旧prompt版本缓存复用: 只接受真实API结果, 规则降级结果不复用
            for pver in self.LEGACY_PROMPT_VERSIONS:
                legacy = self.cache.get(self._legacy_cache_key("decompose", query, pver))
                if legacy is not None and legacy.get('source') == 'kimi_api':
                    self._bump('cache_hits')
                    return self._deserialize_decomposition(legacy)
            if cached is not None:  # 当前版本仅有规则降级结果时才用之
                self._bump('cache_hits')
                return self._deserialize_decomposition(cached)
        try:
            raw = self._chat(self.DECOMPOSE_PROMPT, query)
            spec = self._extract_json(raw)
            result = self._build_from_llm_spec(query, spec)
            result['source'] = 'kimi_api'
        except Exception:
            self._bump('fallbacks')
            result = self._rule_decompose(query)
            result['source'] = 'rule_fallback'
        if self.cache is not None:
            try:
                self.cache.set(key, self._serialize_decomposition(result))
            except Exception:
                pass
        return result

    # ---- LLM spec -> v1.2 结构 nodes/edges 图 ----
    def _build_from_llm_spec(self, query: str, spec: Dict) -> Dict[str, Any]:
        numbers_spec = spec.get('numbers') or []
        ops_spec = spec.get('operations') or []
        traps_spec = spec.get('traps') or []
        if not numbers_spec:
            raise ValueError("LLM返回无numbers")

        numbers = []          # [(value, role)]
        for i, ns in enumerate(numbers_spec):
            val = float(ns.get('value'))
            role = str(ns.get('role', 'unknown'))
            numbers.append((val, role))

        chain = []            # [{'node','op','operands':[order...]}]
        valid_ops = {'addition', 'subtraction', 'multiplication', 'division', 'percentage'}
        for i, ospec in enumerate(ops_spec):
            op = str(ospec.get('op', '')).strip()
            if op not in valid_ops:
                continue
            operands = [int(o) for o in (ospec.get('operands') or [])
                        if isinstance(o, (int, float)) and 1 <= int(o) <= len(numbers)]
            if not operands:
                operands = [min(i + 2, len(numbers))]
            if self.version != "1.3":
                # v1.4: 去除连续重复的操作数编号(如[3,3]->[3], 防折叠时重复作用)
                deduped = []
                for o in operands:
                    if not deduped or deduped[-1] != o:
                        deduped.append(o)
                operands = deduped
            chain.append({'node': f'OP{len(chain)+1}', 'op': op,
                          'operands': operands,
                          'reason': str(ospec.get('reason', ''))})

        # ---- 节点 ----
        nodes, edges = {}, {}
        for i, (val, role) in enumerate(numbers):
            nodes[f'N{i+1}'] = {'energy': 0.3 + i * 0.05, 'value': val,
                                'type': 'number', 'role': role}
        for c in chain:
            nodes[c['node']] = {'energy': 0.4, 'type': 'operation', 'op_type': c['op']}
        nodes['Goal'] = {'energy': 0.0, 'type': 'answer'}
        nids = [f'N{i+1}' for i in range(len(numbers))]
        oids = [c['node'] for c in chain]

        # ---- 正确运算链边 (与v1.2 mock相同的语义绑定) ----
        if len(oids) >= 1 and len(nids) >= 2:
            for nid in nids[:2]:
                edges[(nid, oids[0])] = {'weight': 0.6, 'migration_barrier': 0.3,
                                         'allowed_domains': ['math']}
            prev_op = oids[0]
            for i in range(1, len(oids)):
                edges[(prev_op, oids[i])] = {'weight': 0.7, 'migration_barrier': 0.2,
                                             'allowed_domains': ['math']}
                if i + 1 < len(nids):
                    edges[(nids[i+1], oids[i])] = {'weight': 0.6, 'migration_barrier': 0.3,
                                                   'allowed_domains': ['math']}
                prev_op = oids[i]
            edges[(oids[-1], 'Goal')] = {'weight': 0.8, 'migration_barrier': 0.2,
                                         'allowed_domains': ['math']}
        elif len(oids) == 1:
            for nid in nids:
                edges[(nid, oids[0])] = {'weight': 0.6, 'migration_barrier': 0.3,
                                         'allowed_domains': ['math']}
            edges[(oids[0], 'Goal')] = {'weight': 0.8, 'migration_barrier': 0.2,
                                        'allowed_domains': ['math']}
        else:
            if nids:
                edges[(nids[0], 'Goal')] = {'weight': 0.8, 'migration_barrier': 0.2,
                                            'allowed_domains': ['math']}

        # ---- 陷阱节点 (v1.3: 陷阱通向Goal, 成为 Deposon 需要阻断的诱饵路径) ----
        # 权重 0.9 > 正确边0.6, 使 no_deposon 的贪心游走被陷阱捕获;
        # 陷阱g_couple=5.0 -> unified/v1 下被反射阻断。N1出边上陷阱<=3条, 保证OP1边仍在top-4邻居内。
        trap_nodes_meta = {}
        trap2wrongop = {
            'surface_addition': 'addition', 'surface_subtraction': 'subtraction',
            'surface_multiplication': 'multiplication', 'surface_division': 'division',
            'wrong_order': 'wrong_order', 'unit_confusion': 'unit_confusion'}
        trap_candidates = []
        # 1) LLM 语义陷阱
        for ts in traps_spec:
            ttype = str(ts.get('type', '')).strip()
            if ttype in trap2wrongop:
                trap_candidates.append((f'Trap_{ttype}', trap2wrongop[ttype],
                                        str(ts.get('why', '')), 0.9))
        # 2) 通用错误运算陷阱 (补足, 与v1.2一致)
        correct_ops = {c['op'] for c in chain}
        for wop in ['addition', 'subtraction', 'multiplication', 'division']:
            if wop not in correct_ops:
                trap_candidates.append((f'Trap_WrongOp_{wop}', wop, '错误运算', 0.9))
        # 去重并限量: 最多3条N1陷阱出边
        seen, n_trap_edges = set(), 0
        for tid, wop, why, w in trap_candidates:
            if tid in seen or n_trap_edges >= 3:
                continue
            seen.add(tid)
            nodes[tid] = {'energy': 0.1, 'type': 'trap', 'trap_type': 'wrong_op',
                          'wrong_op': wop, 'why': why}
            edges[(nids[0], tid)] = {'weight': w, 'migration_barrier': 0.1,
                                     'allowed_domains': ['math']}
            edges[(tid, 'Goal')] = {'weight': 0.55, 'migration_barrier': 0.3,
                                    'allowed_domains': ['math']}
            trap_nodes_meta[tid] = wop
            n_trap_edges += 1
        if len(chain) >= 2 and 'Trap_wrong_order' not in seen and n_trap_edges < 3:
            nodes['Trap_Order'] = {'energy': 0.12, 'type': 'trap',
                                   'trap_type': 'wrong_order', 'wrong_op': 'wrong_order'}
            edges[(nids[0], 'Trap_Order')] = {'weight': 0.85, 'migration_barrier': 0.1,
                                              'allowed_domains': ['math']}
            edges[('Trap_Order', 'Goal')] = {'weight': 0.55, 'migration_barrier': 0.3,
                                             'allowed_domains': ['math']}
            trap_nodes_meta['Trap_Order'] = 'wrong_order'
            n_trap_edges += 1
        # 死胡同陷阱 (不出边, 同v1.2)
        nodes['Trap_DeadEnd'] = {'energy': 0.1, 'type': 'trap', 'trap_type': 'dead_end'}
        edges[(nids[0], 'Trap_DeadEnd')] = {'weight': 0.8, 'migration_barrier': 0.1,
                                            'allowed_domains': ['math']}

        return {
            'nodes': nodes,
            'edges': edges,
            'query_type': spec.get('query_type', 'math' if numbers else 'commonsense'),
            'numbers': [v for v, _ in numbers],
            'number_roles': {i: r for i, (v, r) in enumerate(numbers)},
            'operations': [c['op'] for c in chain],
            'operation_chain': chain,
            'trap_nodes': trap_nodes_meta,
            'computed_answer': spec.get('computed_answer'),
            'difficulty': spec.get('difficulty', 'unknown'),
            'raw_llm_traps': traps_spec,
        }

    # ---- 缓存序列化 (tuple边键 -> list) ----
    @staticmethod
    def _serialize_decomposition(result: Dict) -> Dict:
        out = dict(result)
        out['edges'] = [[u, v, attrs] for (u, v), attrs in result['edges'].items()]
        return out

    @staticmethod
    def _deserialize_decomposition(data: Dict) -> Dict:
        out = dict(data)
        out['edges'] = {(u, v): attrs for u, v, attrs in data['edges']}
        return out

    # ================= validate =================
    def validate(self, query: str, reasoning_chain: List[str],
                 predicted_answer: Any) -> Dict[str, Any]:
        self._bump('calls')
        payload = json.dumps({'query': query, 'chain': reasoning_chain,
                              'answer': predicted_answer}, ensure_ascii=False)
        key = self._cache_key("validate", payload)
        if self.cache is not None:
            cached = self.cache.get(key)
            if cached is not None:
                self._bump('cache_hits')
                return cached
        try:
            user = (f"题目: {query}\n推理链(节点路径): {' -> '.join(map(str, reasoning_chain))}\n"
                    f"预测答案: {predicted_answer}")
            raw = self._chat(self.VALIDATE_PROMPT, user)
            spec = self._extract_json(raw)
            score = max(0.0, min(1.0, float(spec.get('score', 0.5))))
            result = {'is_valid': str(spec.get('verdict', '')).lower() == 'correct',
                      'validation_score': score,
                      'verdict': spec.get('verdict', 'unknown'),
                      'issues': [str(i) for i in (spec.get('issues') or [])],
                      'confidence': score, 'source': 'kimi_api'}
        except Exception:
            self._bump('fallbacks')
            result = self._rule_validate(query, reasoning_chain, predicted_answer)
            result['source'] = 'rule_fallback'
        if self.cache is not None:
            try:
                self.cache.set(key, result)
            except Exception:
                pass
        return result

    # ================= generate_answer =================
    def generate_answer(self, query: str, context: Optional[Dict] = None) -> str:
        self._bump('calls')
        try:
            ctx = ""
            if context:
                safe_ctx = {k: v for k, v in context.items()
                            if k in ('predicted_answer', 'best_path', 'validation')}
                ctx = f"\n上下文: {json.dumps(safe_ctx, ensure_ascii=False, default=str)}"
            raw = self._chat(
                "你是简洁的数学助手。用一两句中文自然语言回答题目, 给出最终数值答案。",
                f"{query}{ctx}")
            return raw.strip()
        except Exception:
            self._bump('fallbacks')
            if context and 'predicted_answer' in context:
                return f"经过分析，答案是{context['predicted_answer']}。"
            return "推理完成。"

    # ================= CoT 基线 (v1.4, GSM8K: LLM本身水位线) =================
    COT_PROMPT = """Solve the math word problem step by step (concise). End with a final line exactly of the form: #### <number>"""

    def cot_solve(self, query: str) -> Dict[str, Any]:
        """直接CoT答题, 无Deposon图。失败不缓存(返回ok=False)以便续跑。"""
        self._bump('calls')
        key = self._cache_key("cot", query)
        if self.cache is not None:
            cached = self.cache.get(key)
            if cached is not None:
                self._bump('cache_hits')
                return cached
        try:
            raw = self._chat(self.COT_PROMPT, query)
            m = re.search(r'####\s*([\-0-9,\.]+)', raw)
            answer = None
            if m:
                try:
                    answer = float(m.group(1).replace(',', ''))
                except ValueError:
                    answer = None
            result = {'answer': answer, 'raw_tail': raw[-300:], 'ok': answer is not None,
                      'source': 'kimi_api'}
            if answer is None:
                raise ValueError("CoT响应缺少####数值")
        except Exception:
            self._bump('errors')
            return {'answer': None, 'ok': False, 'source': 'error'}
        if self.cache is not None:
            try:
                self.cache.set(key, result)
            except Exception:
                pass
        return result

    # ================= 规则基线 (继承v1.2, 作为降级后备) =================
    def _rule_decompose(self, query: str) -> Dict[str, Any]:
        numbers = [(m.start(), float(m.group(1))) for m in re.finditer(r'(\d+\.?\d*)', query)]
        ops = self._detect_ops(query)
        number_roles = self._assign_roles(query, numbers)
        nodes, edges = self._build_graph(numbers, ops, number_roles)
        self._add_traps(nodes, edges, ops, query, numbers)
        # v1.3: 为规则路径补 operation_chain, 供评估器统一计算
        chain = []
        for i, op in enumerate(ops):
            operands = [1, 2] if i == 0 else [min(i + 2, len(numbers))]
            chain.append({'node': f'OP{i+1}', 'op': op,
                          'operands': [o for o in operands if o <= max(1, len(numbers))],
                          'reason': 'rule'})
        trap_nodes_meta = {nid: attrs.get('wrong_op', 'dead_end')
                           for nid, attrs in nodes.items()
                           if attrs.get('type') == 'trap'}
        return {
            'nodes': nodes,
            'edges': edges,
            'query_type': 'math' if numbers else 'commonsense',
            'numbers': [v for _, v in numbers],
            'operations': ops,
            'number_roles': number_roles,
            'operation_chain': chain,
            'trap_nodes': trap_nodes_meta,
            'computed_answer': None,
        }

    def _detect_ops(self, query: str) -> List[str]:
        detected = {}
        if '折' in query or '折扣' in query or '%' in query or '百分之' in query:
            detected['percentage'] = 0
        if re.search(r'每\w*\d+\w*元.*买\d+', query) or re.search(r'\d+元.*买\d+\w+', query):
            detected['multiplication'] = detected.get('multiplication', 0)
        elif re.search(r'每个\w*\d+\w+.*\d+个\w+', query):
            detected['multiplication'] = detected.get('multiplication', 0)
        elif re.search(r'每个盒子装\d+.*\d+个盒子', query) or re.search(r'每\w+装\d+.*\d+\w+', query):
            detected['multiplication'] = detected.get('multiplication', 0)
        if '平均' in query and ('分' in query or '给' in query):
            detected['division'] = detected.get('division', query.find('平均'))
        elif re.search(r'每\d+人.*组', query) or re.search(r'每\d+个.*份', query):
            detected['division'] = detected.get('division', 0)
        elif '分' in query and '组' in query:
            detected['division'] = detected.get('division', query.find('分'))
        if '给了' in query and not any(kw in query for kw in ['又', '再']):
            detected['subtraction'] = detected.get('subtraction', query.find('给了'))
        elif '给' in query and '剩' in query:
            detected['subtraction'] = detected.get('subtraction', query.find('给'))
        elif any(kw in query for kw in ['减去', '用去', '吃掉', '拿走', '去掉', '扣除', '剪去', '开走', '满减']):
            pos = min([query.find(kw) for kw in ['减去', '用去', '吃掉', '拿走', '去掉', '扣除', '剪去', '开走', '满减'] if kw in query] or [999])
            detected['subtraction'] = detected.get('subtraction', pos)
        elif re.search(r'满\d+减\d+', query) or re.search(r'减\d+', query):
            detected['subtraction'] = detected.get('subtraction', query.find('减'))
        elif '便宜' in query or '优惠' in query:
            detected['subtraction'] = detected.get('subtraction', query.find('便宜') if '便宜' in query else query.find('优惠'))
        if '又' in query and '给' in query:
            detected['addition'] = detected.get('addition', query.find('又'))
        elif '再' in query and '给' in query:
            detected['addition'] = detected.get('addition', query.find('再'))
        elif any(kw in query for kw in ['飞来', '来了', '开来', '增加', '加上', '合并', '合计']):
            pos = min([query.find(kw) for kw in ['飞来', '来了', '开来', '增加', '加上', '合并', '合计'] if kw in query] or [999])
            detected['addition'] = detected.get('addition', pos)
        elif ('总共' in query or '一共' in query) and 'multiplication' not in detected:
            detected['addition'] = detected.get('addition', query.find('总共') if '总共' in query else query.find('一共'))

        if 'multiplication' in detected and 'division' in detected:
            if re.search(r'每\w*\d+\w*元.*买\d+', query) or re.search(r'每\w+装\d+', query):
                del detected['division']
        if 'division' in detected and 'multiplication' in detected:
            if '平均' in query:
                del detected['multiplication']
        if 'addition' in detected and 'subtraction' in detected:
            if '又' in query or '再' in query or '飞来' in query or '开来' in query:
                del detected['subtraction']

        priority = {'percentage': 5, 'multiplication': 4, 'division': 4, 'subtraction': 3, 'addition': 3}
        sorted_ops = sorted(detected.keys(), key=lambda op: (-priority[op], detected[op]))
        return sorted_ops

    def _assign_roles(self, query: str, numbers: List[Tuple[int, float]]) -> Dict[int, str]:
        roles = {}
        for i, (pos, val) in enumerate(numbers):
            role = 'unknown'
            after = query[pos:pos+10]
            if '元' in after or '块' in after or '钱' in after:
                role = 'price'
            elif any(kw in after for kw in ['个', '只', '本', '支', '辆', '盒', '组', '份', '人']):
                role = 'quantity'
            if val <= 10 and '折' in query:
                role = 'discount'
            roles[i] = role
        return roles

    def _build_graph(self, numbers: List[Tuple[int, float]], ops: List[str],
                     number_roles: Dict[int, str]) -> Tuple[Dict, Dict]:
        nodes, edges = {}, {}
        for i, (pos, val) in enumerate(numbers):
            nid = f'N{i+1}'
            nodes[nid] = {'energy': 0.3 + i*0.05, 'value': val, 'type': 'number', 'role': number_roles.get(i, 'unknown')}
        for i, op in enumerate(ops):
            nodes[f'OP{i+1}'] = {'energy': 0.4, 'type': 'operation', 'op_type': op}
        nodes['Goal'] = {'energy': 0.0, 'type': 'answer'}
        nids = [f'N{i+1}' for i in range(len(numbers))]
        oids = [f'OP{i+1}' for i in range(len(ops))]
        if len(oids) >= 1 and len(nids) >= 2:
            for nid in nids[:2]:
                edges[(nid, oids[0])] = {'weight': 0.6, 'migration_barrier': 0.3, 'allowed_domains': ['math']}
            prev_op = oids[0]
            for i in range(1, len(oids)):
                edges[(prev_op, oids[i])] = {'weight': 0.7, 'migration_barrier': 0.2, 'allowed_domains': ['math']}
                if i + 1 < len(nids):
                    edges[(nids[i+1], oids[i])] = {'weight': 0.6, 'migration_barrier': 0.3, 'allowed_domains': ['math']}
                prev_op = oids[i]
            edges[(oids[-1], 'Goal')] = {'weight': 0.8, 'migration_barrier': 0.2, 'allowed_domains': ['math']}
        elif len(oids) == 1:
            for nid in nids:
                edges[(nid, oids[0])] = {'weight': 0.6, 'migration_barrier': 0.3, 'allowed_domains': ['math']}
            edges[(oids[0], 'Goal')] = {'weight': 0.8, 'migration_barrier': 0.2, 'allowed_domains': ['math']}
        else:
            if nids:
                edges[(nids[0], 'Goal')] = {'weight': 0.8, 'migration_barrier': 0.2, 'allowed_domains': ['math']}
        return nodes, edges

    def _add_traps(self, nodes: Dict, edges: Dict, ops: List[str], query: str, numbers: List[Tuple[int, float]]):
        nids = [k for k in nodes if k.startswith('N')]
        if len(numbers) >= 2:
            all_ops = ['addition', 'subtraction', 'multiplication', 'division', 'percentage']
            wrong_ops = [op for op in all_ops if op not in ops]
            for i, wop in enumerate(wrong_ops[:3]):
                tid = f'Trap_WrongOp_{wop}'
                nodes[tid] = {'energy': 0.1, 'type': 'trap', 'trap_type': 'wrong_op', 'wrong_op': wop}
                if nids:
                    edges[(nids[0], tid)] = {'weight': 0.9, 'migration_barrier': 0.1, 'allowed_domains': ['math']}
            if '给' in query and 'subtraction' in ops:
                nodes['Trap_Surface'] = {'energy': 0.15, 'type': 'trap', 'trap_type': 'surface_association'}
                if nids:
                    edges[(nids[0], 'Trap_Surface')] = {'weight': 0.85, 'migration_barrier': 0.1, 'allowed_domains': ['math']}
            if len(ops) >= 2:
                nodes['Trap_Order'] = {'energy': 0.12, 'type': 'trap', 'trap_type': 'wrong_order'}
                if nids:
                    edges[(nids[0], 'Trap_Order')] = {'weight': 0.8, 'migration_barrier': 0.1, 'allowed_domains': ['math']}
        if len(numbers) >= 1:
            nodes['Trap_DeadEnd'] = {'energy': 0.1, 'type': 'trap', 'trap_type': 'dead_end'}
            if nids:
                edges[(nids[0], 'Trap_DeadEnd')] = {'weight': 0.8, 'migration_barrier': 0.1, 'allowed_domains': ['math']}

    def _rule_validate(self, query: str, reasoning_chain: List[str], predicted_answer: Any) -> Dict[str, Any]:
        score = 0.75
        issues = []
        traps = [n for n in reasoning_chain if 'Trap' in n]
        if traps:
            score -= 0.35 * len(traps)
            issues.append(f"陷阱: {traps}")
        op_nodes = [n for n in reasoning_chain if n.startswith('OP')]
        if len(op_nodes) >= 2:
            score += 0.05
        nums_q = re.findall(r'\d+\.?\d*', query)
        n_used = len([n for n in reasoning_chain if n.startswith('N')])
        if n_used < len(nums_q):
            score -= 0.1
            issues.append(f"数字未全用 ({n_used}/{len(nums_q)})")
        elif n_used == len(nums_q):
            score += 0.05
        if reasoning_chain and reasoning_chain[-1] != 'Goal':
            score -= 0.15
            issues.append("未达Goal")
        else:
            score += 0.05
        if not op_nodes and len(nums_q) >= 2:
            score -= 0.15
            issues.append("缺运算")
        score = max(0.0, min(1.0, score))
        return {'is_valid': score > 0.55, 'validation_score': score, 'issues': issues, 'confidence': score}


# ============================================================
# 模块七: 概念分解器
# ============================================================

class ConceptDecomposer:
    def __init__(self, llm_backend=None):
        self.llm_backend = llm_backend or KimiLLMBackend()

    def decompose(self, query: str, domain_hint: Optional[str] = None) -> Dict[str, Any]:
        return self.llm_backend.decompose(query)

    def to_brain_graph(self, decomposition: Dict) -> Dict[str, Any]:
        graph = {'nodes': decomposition['nodes'], 'edges': decomposition['edges']}
        # v1.3: 透传运算链/陷阱元数据, 供评估器沿存活路径计算答案
        for k in ('operation_chain', 'trap_nodes', 'computed_answer',
                  'numbers', 'query_type', 'source'):
            if k in decomposition:
                graph[k] = decomposition[k]
        return graph


def deterministic_embedding(node_id: str, feature_dim: int, seed_offset: int = 0) -> np.ndarray:
    """确定性节点嵌入生成"""
    h = hashlib.sha256(f"{node_id}:{feature_dim}:{seed_offset}".encode()).digest()
    vals = []
    idx = 0
    while len(vals) < feature_dim + 1:
        iv = int.from_bytes(h[idx:idx+4], 'big')
        idx = (idx + 4) % len(h)
        vals.append((iv % 2**32) / 2**32)
    res = []
    for i in range(0, len(vals) - 1, 2):
        u1, u2 = max(vals[i], 1e-10), vals[i + 1]
        mag = np.sqrt(-2.0 * np.log(u1))
        res.append(mag * np.cos(2 * np.pi * u2))
        if len(res) < feature_dim:
            res.append(mag * np.sin(2 * np.pi * u2))
    c = np.array(res[:feature_dim], dtype=np.float64)
    n = np.linalg.norm(c)
    return c / n if n > 0 else c


# ============================================================
# 模块八: DeposonField —— 统一场
# ============================================================

# v1.9 E9.3: high_couple 模式的 g_couple 放大系数 (SPEC v1.9 Part B)
HIGH_COUPLE_GAIN = 5.0


def resolve_high_couple_config() -> Dict[str, Any]:
    """v1.9 E9.3: 默认返回真修复配置; 仅当显式设置环境变量
    DEPOSON_V14_HIGH_COUPLE_ALIAS=1 时返回 v1.4 旧别名配置 (历史复现用)。"""
    if os.environ.get('DEPOSON_V14_HIGH_COUPLE_ALIAS') == '1':
        return {'mode': 'v1_blocking', 'use_deposon': True}
    return {'mode': 'high_couple', 'use_deposon': True}


class DeposonField:
    """Deposon统一场 (v1.3/v1.4 合并, version 钉定)"""

    def __init__(self, feature_dim: int = 64,
                 default_g_couple: float = 0.05,
                 default_g_aether: float = 0.05,
                 version=None):
        self.version = _resolve_version(
            version, getattr(type(self), 'version', '1.4'))
        self.feature_dim = feature_dim
        self.default_g_couple = default_g_couple
        self.default_g_aether = default_g_aether
        self.deposons: Dict[str, DeposonState] = {}
        self.aether = EtherChannel()
        self._stats = {'spawned': 0, 'blocked': 0, 'tunneled': 0,
                       'transmitted': 0, 'total_paths': 0,
                       'reflected': 0.0, 'dissipated': 0.0}

    def spawn_from_graph(self, graph: Dict, mode: str = 'unified',
                         node_energies: Optional[Dict[str, float]] = None):
        """
        从知识图谱生成Deposon场

        模式:
        - 'unified'/'v1_blocking'/'v2_tunneling': 基于节点类型绑定 (原v1.2)
        - 'energy': 节点自身resonance_energy (delta≡0, 共振休眠, 原行为)
        - 'resonant': 路径-节点语义匹配 (delta≠0, 激活共振通道)
        - 'resonant_hybrid': 仅非trap节点用匹配值, trap保持类型强绑定
        - 'high_couple': v1.3=g_couple×3 / v1.4(E9.3)=g_aether=0+g_couple×HIGH_COUPLE_GAIN
        - 'arrhenius': v1.3 专属, Arrhenius势垒 k=exp(-b/T) 散射
        """
        nodes = graph.get('nodes', {})
        for node_id, attrs in nodes.items():
            node_type = attrs.get('type', 'unknown')
            energy = attrs.get('energy', 0.0)
            if node_energies and node_id in node_energies:
                energy = node_energies[node_id]
            center = deterministic_embedding(node_id, self.feature_dim)

            g_couple = self.default_g_couple
            g_aether = self.default_g_aether
            if node_type == 'trap':
                g_couple, g_aether = 5.0, 0.0
            elif node_type == 'answer':
                g_couple, g_aether = 0.01, 0.0
            elif node_type == 'operation':
                if self.version == "1.3":
                    # v1.3: 度数越大绑定越强
                    degree = sum(1 for (u, v) in graph.get('edges', {})
                                 if u == node_id or v == node_id)
                    g_couple = 0.3 * (1 + 0.02 * degree)
                    g_aether = 0.2
                else:
                    # v1.4: operation 绑定下调, 减小过阻塞
                    degree = sum(1 for (u, v) in graph.get('edges', {})
                                 if u == node_id or v == node_id)
                    g_couple = 0.15 * (1 + 0.02 * degree)
                    g_aether = 0.05
            elif node_type == 'number':
                g_couple, g_aether = 0.05, 0.05

            if mode == 'v1_blocking':
                g_aether = 0.0
                if node_type == 'trap':
                    g_couple = 5.0
            elif mode == 'v2_tunneling':
                if node_type == 'trap':
                    g_couple = 0.1
                    g_aether = 2.0
            elif mode == 'high_couple':
                if self.version == "1.3":
                    g_couple = g_couple * 3.0
                else:
                    # v1.9 E9.3 真修复: 全节点 g_aether=0 (无隧穿耗散) + g_couple 放大
                    g_aether = 0.0
                    g_couple = g_couple * HIGH_COUPLE_GAIN
            elif mode in ('resonant', 'resonant_hybrid') and self.version == "1.3":
                pass  # v1.3: 共振模式在 process_path 中按路径匹配覆盖 resonance_energy
            elif mode in ('labelfree', 'arrhenius', 'arrhenius_hybrid') and self.version == "1.3":
                pass  # v1.3: 实验模式 (arrhenius 在 process_path 中生效)
            # v1.4: resonant/labelfree/arrhenius 等 v1.3 专属模式无分支 -> fallthrough (= 原 v1_4 行为)

            self.deposons[node_id] = DeposonState(
                id=node_id, center=center,
                g_couple=g_couple, g_aether=g_aether,
                resonance_energy=energy)
            self._stats['spawned'] += 1

    def process_path(self, path: List[str],
                     initial_energy: float = 1.0) -> Dict[str, Any]:
        """处理单条路径, 返回散射结果 (version 钉定记录键)"""
        self._stats['total_paths'] += 1
        E = initial_energy
        total_reflected = 0.0
        total_dissipated = 0.0
        per_node = []
        fate = 'transmitted'

        for node_id in path:
            deposon = self.deposons.get(node_id)
            if deposon is None:
                continue
            photon_energy = deposon.resonance_energy
            sr = deposon.scatter(photon_energy)
            t, r, a = sr['transmitted'], sr['reflected'], sr['dissipated']

            # v1.3 arrhenius 模式: 边势垒修正 (g_aether -> arrhenius 透射率)
            barrier_loss = 0.0
            if (self.version == "1.3" and getattr(self, '_arrhenius_mode', False)
                    and node_id in self._edge_barrier):
                b = self._edge_barrier[node_id]
                w = self._edge_weight.get(node_id, 1.0)
                k = math.exp(-b / self._arrhenius_T)
                if getattr(self, '_arrhenius_kramers', False):
                    k *= w  # Kramers 尝试频率 ~ 边权
                k = min(1.0, k)
                barrier_loss = E * t * (1 - k)
                E = E * t * k
            else:
                E = E * t

            reflected_here = (initial_energy if not per_node else per_node[-1]['E_in']) * r
            dissipated_here = (initial_energy if not per_node else per_node[-1]['E_in']) * a
            total_reflected += reflected_here
            total_dissipated += dissipated_here
            if barrier_loss > 0:
                total_dissipated += barrier_loss

            per_node.append({'node': node_id, 'E_in': E / t if t > 0 else 0.0,
                             't': t, 'r': r, 'a': a, 'E_out': E})

            if r > 0.7 and fate == 'transmitted':
                fate = 'blocked'
            elif a > 0.5 and fate == 'transmitted':
                fate = 'tunneling'

        transmitted_frac = E / initial_energy if initial_energy > 0 else 0.0
        if fate == 'transmitted' and transmitted_frac < 0.3:
            fate = 'blocked'

        self._stats[fate if fate in ('blocked', 'tunneled', 'transmitted') else 'transmitted'] += 1
        self._stats['reflected'] += total_reflected
        self._stats['dissipated'] += total_dissipated
        if total_dissipated > 0:
            self.aether.deposit(total_dissipated,
                                source=f"path_{'_'.join(path)}",
                                metadata={'path': path, 'fate': fate})

        result = {
            'fate': fate,
            'transmitted': transmitted_frac,
            'reflected': total_reflected / initial_energy if initial_energy > 0 else 0.0,
            'dissipated': total_dissipated / initial_energy if initial_energy > 0 else 0.0,
            'final_energy': E,
            'per_node': per_node
        }
        if self.version == "1.3":
            result['barrier_loss'] = barrier_loss if 'barrier_loss' in dir() else 0.0
            for rec in per_node:
                rec['delta'] = abs(rec['E_in'] - rec['E_out'])
        return result

    def get_stats(self) -> Dict:
        return dict(self._stats)


# ============================================================
# 模块九: DeposonAgentSystem —— 顶层系统
# ============================================================

class DeposonAgentSystem:
    """Deposon Agent 系统 (v1.3/v1.4 合并, version 钉定)"""

    def __init__(self, llm_backend=None, mode: str = 'unified',
                 feature_dim: int = 64,
                 version=None):
        self.version = _resolve_version(
            version, getattr(type(self), 'version', '1.4'))
        self.mode = mode
        self.llm = llm_backend or LLMBackend(mode='mock')
        self.decomposer = ConceptDecomposer(llm_backend=self.llm)
        self.feature_dim = feature_dim

    def reason(self, query: str, domain_hint: Optional[str] = None) -> Dict[str, Any]:
        """完整推理管线: 分解 -> 建图 -> 生成场 -> 路径评估"""
        decomposition = self.decomposer.decompose(query, domain_hint)
        graph = self.decomposer.to_brain_graph(decomposition)

        field_obj = DeposonField(feature_dim=self.feature_dim,
                                 version=self.version)
        field_obj.spawn_from_graph(graph, mode=self.mode)

        paths = self._generate_paths(graph)
        results = []
        for p in paths:
            r = field_obj.process_path(p)
            r['path'] = p
            results.append(r)

        results.sort(key=lambda x: x['transmitted'], reverse=True)
        best = results[0] if results else None

        return {
            'query': query,
            'decomposition': decomposition,
            'graph_stats': {'n_nodes': len(graph.get('nodes', {})),
                            'n_edges': len(graph.get('edges', {}))},
            'n_paths': len(paths),
            'best_path': best['path'] if best else None,
            'best_transmitted': best['transmitted'] if best else 0.0,
            'best_fate': best['fate'] if best else 'none',
            'all_candidates': [{'path': r['path'],
                                'transmitted': r['transmitted'],
                                'fate': r['fate']} for r in results[:5]],
            'field_stats': field_obj.get_stats(),
            'aether_dissipated': field_obj.aether.get_total_dissipated()
        }

    def _generate_paths(self, graph: Dict, max_paths: int = 30) -> List[List[str]]:
        """贪心生成候选路径 (从起点到Goal)"""
        nodes = graph.get('nodes', {})
        edges = graph.get('edges', {})
        start_nodes = [nid for nid, attrs in nodes.items()
                       if attrs.get('type') == 'number']
        if not start_nodes:
            start_nodes = [nid for nid in nodes if nid != 'Goal'][:1]
        if not start_nodes:
            return []
        start = sorted(start_nodes)[0]
        goal = 'Goal'
        paths = []
        queue = deque([(start, [start])])
        while queue and len(paths) < max_paths:
            cur, pth = queue.popleft()
            if cur == goal:
                paths.append(pth)
                continue
            outs = []
            for (u, v), attrs in edges.items():
                if u == cur and (v not in pth or v == goal):
                    outs.append((v, attrs.get('weight', 0.5),
                                 attrs.get('migration_barrier', 0.3)))
            outs.sort(key=lambda x: x[1], reverse=True)
            for neighbor, weight, barrier in outs[:8]:  # v1.3: 4->8, 防止陷阱边挤占正确链入口
                queue.append((neighbor, pth + [neighbor]))
        return paths

    def ablation_study(self, query: str, domain_hint: Optional[str] = None) -> Dict[str, Any]:
        """消融实验: 对比 no_deposon / v1_blocking / v2_tunneling / unified / high_couple"""
        decomposition = self.decomposer.decompose(query, domain_hint)
        graph = self.decomposer.to_brain_graph(decomposition)
        results = {}

        for mode_name, use_field in [('no_deposon', False),
                                     ('v1_blocking', True),
                                     ('v2_tunneling', True),
                                     ('unified', True)]:
            paths = self._generate_paths(graph)
            if not use_field:
                scored = [(p, 1.0) for p in paths]
            else:
                f = DeposonField(feature_dim=self.feature_dim,
                                 version=self.version)
                f.spawn_from_graph(graph, mode=mode_name)
                scored = [(p, f.process_path(p)['transmitted']) for p in paths]
            scored.sort(key=lambda x: x[1], reverse=True)
            best = scored[0] if scored else (None, 0.0)
            results[mode_name] = {
                'best_path': best[0],
                'best_score': best[1],
                'n_paths': len(paths)
            }

        # high_couple 变体 (version 钉定语义)
        hc_cfg = resolve_high_couple_config() if self.version != "1.3" else \
            {'mode': 'high_couple', 'use_deposon': True}
        f = DeposonField(feature_dim=self.feature_dim, version=self.version)
        f.spawn_from_graph(graph, mode=hc_cfg['mode'])
        paths = self._generate_paths(graph)
        scored = [(p, f.process_path(p)['transmitted']) for p in paths]
        scored.sort(key=lambda x: x[1], reverse=True)
        best = scored[0] if scored else (None, 0.0)
        results['high_couple'] = {'best_path': best[0], 'best_score': best[1],
                                  'n_paths': len(paths)}
        return results

    def report_ablation(self, results: Dict[str, Any]) -> str:
        lines = ["Deposon 消融实验报告", "=" * 40]
        for mode, r in results.items():
            lines.append(f"[{mode}] best_path={' -> '.join(r['best_path'] or [])} "
                         f"score={r['best_score']:.4f} n_paths={r['n_paths']}")
        return "\n".join(lines)


# ============================================================
# 模块十: BenchmarkEvaluator —— 基准评估器
# ============================================================

class BenchmarkEvaluator:
    """基准评估 (v1.3/v1.4 合并, version 跟随 agent 或 shim 钉定)"""

    def __init__(self, agent: DeposonAgentSystem, use_validation: bool = True,
                 version=None):
        self.version = _resolve_version(
            version, getattr(type(self), 'version', agent.version))
        self.agent = agent
        self.use_validation = use_validation

    def evaluate_math(self, query: str, correct_answer: Optional[float] = None,
                      **kwargs) -> Dict[str, Any]:
        """评估单道数学题 (沿最优存活路径计算答案)"""
        result = self.agent.reason(query, domain_hint='math')
        dec = result['decomposition']
        graph = {'nodes': dec['nodes'], 'edges': dec['edges'],
                 'operation_chain': dec.get('operation_chain', []),
                 'trap_nodes': dec.get('trap_nodes', {}),
                 'computed_answer': dec.get('computed_answer')}
        best_path = result['best_path']
        predicted, path_detail, trap_hit = self._compute_answer_from_path(graph, best_path)
        is_correct = (predicted is not None and correct_answer is not None
                      and abs(predicted - correct_answer) < 1e-6)
        rec = {
            'query': query,
            'correct_answer': correct_answer,
            'predicted_answer': predicted,
            'is_correct': bool(is_correct),
            'best_path': best_path,
            'best_fate': result['best_fate'],
            'trap_hit': trap_hit,
            'decompose_source': dec.get('source', 'unknown'),
            'all_candidates': [{'path': c['path'], 'transmitted': c['transmitted'],
                                'fate': c['fate']}
                               for c in result['all_candidates'][:5]]
        }
        if self.use_validation:
            try:
                v = self.agent.llm.validate(query, best_path or [], predicted)
                rec['validation'] = v
            except Exception:
                rec['validation'] = {'error': 'validate failed'}
        return rec

    def _compute_answer_from_path(self, graph: Dict, path: Optional[List[str]]):
        """沿路径推进运算链 (v1.3: 不去重 / v1.4: 连续重复折叠)。

        返回 (predicted, detail, trap_hit)。
        """
        chain = graph.get('operation_chain') or []
        trap_nodes = graph.get('trap_nodes') or {}
        numbers = {}
        for nid, attrs in (graph.get('nodes') or {}).items():
            if attrs.get('type') == 'number':
                try:
                    numbers[int(nid[1:])] = float(attrs.get('value'))
                except Exception:
                    pass
        number_values = [numbers[k] for k in sorted(numbers)]

        trap_hit = False
        if path:
            for nid in path:
                if nid in trap_nodes or (graph.get('nodes', {}).get(nid, {}).get('type') == 'trap'):
                    trap_hit = True
                    break

        if not chain:
            ca = graph.get('computed_answer')
            try:
                return (float(ca) if ca is not None else None), {'mode': 'computed_answer'}, trap_hit
            except Exception:
                return None, {'mode': 'none'}, trap_hit

        # 选择要执行的运算: 路径上的 OP 节点; 无路径则全链
        if path:
            ops_on_path = [c for c in chain if c['node'] in path]
        else:
            ops_on_path = list(chain)
        if not ops_on_path:
            ops_on_path = list(chain)

        raw_ops = []
        for c in ops_on_path:
            for o in c.get('operands', []):
                raw_ops.append(o)
        if self.version == "1.3":
            ops_idx = raw_ops  # v1.3: 不去重
        else:
            ops_idx = []  # v1.4: 折叠时去除连续重复操作数编号
            for o in raw_ops:
                if not ops_idx or ops_idx[-1] != o:
                    ops_idx.append(o)

        # 陷阱路径: 用错误运算替换
        op_list = [c['op'] for c in ops_on_path]
        if trap_hit and path:
            for nid in path:
                if nid in trap_nodes:
                    wrong = trap_nodes[nid]
                    if wrong in ('addition', 'subtraction', 'multiplication', 'division'):
                        op_list = [wrong] * len(op_list)
                    break

        # 执行链: acc = numbers[ops_idx[0]]; 逐步 op numbers[next]
        detail = {'mode': 'chain', 'ops': op_list, 'ops_idx': ops_idx}
        if not number_values:
            return None, detail, trap_hit
        try:
            acc = number_values[0]
            if len(number_values) >= 2 and op_list:
                acc = number_values[0]
                nxt = 1
                for op in op_list:
                    if nxt >= len(number_values):
                        break
                    b = number_values[nxt]
                    if op == 'addition':
                        acc = acc + b
                    elif op == 'subtraction':
                        acc = acc - b
                    elif op == 'multiplication':
                        acc = acc * b
                    elif op == 'division':
                        acc = acc / b if b != 0 else float('nan')
                    elif op == 'percentage':
                        acc = acc * b
                    nxt += 1
                    if op in ('multiplication', 'addition',
                              'subtraction',
                                 'division', 'percentage') and len(number_values) >= 2:
                        pass
                return acc, detail, trap_hit
            return acc, detail, trap_hit
        except Exception:
            return None, detail, trap_hit


# ============================================================
# 模块十一: 百题基准
# ============================================================

class HundredQuestionBenchmark:
    """百题基准测试集 (内置样例)"""

    SAMPLE_QUESTIONS = [
        {"q": "小明有5个苹果，给了小红2个，还剩几个？", "a": 3.0, "domain": "math"},
        {"q": "一件商品原价120元，先打八折再减10元，现价多少元？", "a": 86.0, "domain": "math"},
        {"q": "每组6个橙子，一共7组，平均每个篮子装几个？", "a": 42.0, "domain": "math"},
    ]

    def __init__(self, agent: DeposonAgentSystem):
        self.agent = agent
        self.evaluator = BenchmarkEvaluator(agent)

    def run(self, questions: Optional[List[Dict]] = None) -> Dict[str, Any]:
        questions = questions or self.SAMPLE_QUESTIONS
        records = []
        for item in questions:
            rec = self.evaluator.evaluate_math(item['q'], correct_answer=item['a'])
            rec['domain'] = item.get('domain', 'math')
            records.append(rec)
        n = len(records)
        n_correct = sum(1 for r in records if r['is_correct'])
        return {'n_total': n, 'n_correct': n_correct,
                'accuracy': n_correct / n if n else 0.0,
                'records': records}


class TrapBenchmark:
    """陷阱题基准 (v1.3 保留)"""

    TRAPS = [
        {"q": "树上10只鸟，猎人打死1只，还剩几只？",
         "naive": "9只", "correct": "0只（其他全飞走）",
         "trap": "surface_subtraction"},
        {"q": "1公斤铁和1公斤棉花哪个重？",
         "naive": "铁重", "correct": "一样重",
         "trap": "density_intuition"},
    ]

    def __init__(self, agent: DeposonAgentSystem):
        self.agent = agent

    def run(self) -> Dict[str, Any]:
        results = []
        for item in self.TRAPS:
            r = self.agent.reason(item['q'])
            results.append({'question': item['q'], 'naive': item['naive'],
                            'correct': item['correct'],
                            'agent_best_path': r['best_path'],
                            'agent_fate': r['best_fate']})
        return {'n': len(results), 'results': results}


if __name__ == '__main__':
    agent = DeposonAgentSystem(llm_backend=LLMBackend(mode='mock'))
    r = agent.reason("小明有5个苹果，给了小红2个，还剩几个？")
    print(json.dumps({'best_path': r['best_path'],
                      'transmitted': r['best_transmitted']},
                     ensure_ascii=False, indent=1))
