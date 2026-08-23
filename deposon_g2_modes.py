# -*- coding: utf-8 -*-
# ============================================================
# Deposon G2 模式: Boltzmann 退火路径选择 + 路径积分(Born规则)集成
# 从 deposon_g2_boltzmann_pathintegral.json 的 setup 记录还原为可测试实现
#   - boltzmann 采样: 出边 i 概率 p_i ∝ exp((w_i - b_i)/T), 边能 E_i = b_i - w_i
#   - 退火: T 从 T_hi 几何衰减到 T_lo, K 条轨迹
#   - 路径积分: K 条独立轨迹, Born 规则聚合 argmax Σ_p transmitted_p^2
# 全部 seed 确定论 (numpy Generator), 零 API。
# ============================================================
import math
from typing import Dict, List, Optional, Tuple

import numpy as np


def _out_edges(nodes: Dict, edges: Dict, current: str, path: List[str]):
    """与 v1.3 _generate_paths 相同的邻居约束: 不重复访问 (answer 节点除外)"""
    outs = []
    for (u, v), attrs in edges.items():
        if u == current and (v not in path or nodes.get(v, {}).get('type') == 'answer'):
            outs.append((v, attrs.get('weight', 0.5), attrs.get('migration_barrier', 0.3)))
    return outs


def boltzmann_walk(nodes: Dict, edges: Dict, start: str, goal: str,
                   T: float, rng: np.random.Generator,
                   max_steps: int = 12) -> List[str]:
    """单条 Boltzmann 轨迹。T<=1e-8 时退化为确定性 argmax (T→0 极限)。"""
    if T < 0:
        raise ValueError("T must be >= 0")  # 参数区间防御
    path = [start]
    current = start
    while current != goal and len(path) < max_steps:
        outs = _out_edges(nodes, edges, current, path)
        if not outs:
            break
        energies = np.array([b - w for _, w, b in outs], dtype=float)  # 低能=高权低势垒
        if T <= 1e-8:
            idx = int(np.argmin(energies))  # T→0: 零涨落, 唯一最小能量 (平局取先)
        else:
            z = -energies / T               # p ∝ exp(-E/T) = exp((w-b)/T)
            z -= z.max()                    # 数值稳定 softmax
            p = np.exp(z)
            p /= p.sum()
            idx = int(rng.choice(len(outs), p=p))
        current = outs[idx][0]
        path.append(current)
    return path


def find_start_goal(nodes: Dict) -> Tuple[Optional[str], Optional[str]]:
    start = goal = None
    for nid, attrs in nodes.items():
        t = attrs.get('type')
        if t == 'number' and start is None:
            start = nid
        if t == 'answer':
            goal = nid
    return start, goal


def boltzmann_annealed(nodes: Dict, edges: Dict, field_factory,
                       K: int = 20, T_hi: float = 1.0, T_lo: float = 0.05,
                       seed: int = 42) -> Dict:
    """K 条几何退火轨迹 + 场透射 argmax 择优。

    field_factory: () -> DeposonField  (每条轨迹一个干净场, 避免以太记账串扰)
    K=1 时退化为单轨迹 argmax (T=T_hi)。
    """
    if K < 1:
        raise ValueError("K must be >= 1")
    start, goal = find_start_goal(nodes)
    rng = np.random.default_rng(seed)
    temps = np.geomspace(T_hi, T_lo, K)
    trajs = []
    for k in range(K):
        path = boltzmann_walk(nodes, edges, start, goal, float(temps[k]), rng)
        field = field_factory()
        res = field.process_path(path, path_energy=1.0)
        trajs.append({'path': path, 'T': float(temps[k]),
                      'transmitted': res['transmitted'], 'fate': res['fate']})
    best = max(trajs, key=lambda x: x['transmitted'])
    return {'best_path': best['path'], 'best_transmitted': best['transmitted'],
            'trajectories': trajs, 'method': 'boltzmann_annealed', 'K': K, 'seed': seed}


def path_integral_born(nodes: Dict, edges: Dict, field_factory,
                       K: int = 20, T: float = 0.5, seed: int = 42,
                       answer_fn=None) -> Dict:
    """路径积分集成: K 条独立轨迹, Born 规则 w(group)=Σ_p transmitted_p^2,
    argmax 组获胜。分组键: answer_fn(path) 若提供 (按答案聚合, G2论文口径),
    否则按终点节点。K=1 时退化为单轨迹 argmax。"""
    if K < 1:
        raise ValueError("K must be >= 1")
    start, goal = find_start_goal(nodes)
    rng = np.random.default_rng(seed)
    trajs = []
    for _ in range(K):
        path = boltzmann_walk(nodes, edges, start, goal, T, rng)
        field = field_factory()
        res = field.process_path(path, path_energy=1.0)
        ans = answer_fn(path) if answer_fn else (path[-1] if path else None)
        trajs.append({'path': path, 'transmitted': res['transmitted'],
                      'fate': res['fate'], 'answer': ans})
    born = {}
    for tr in trajs:
        key = _group_key(tr['answer'])
        born[key] = born.get(key, 0.0) + tr['transmitted'] ** 2  # Born: 振幅平方求和
    best_key = max(born.items(), key=lambda kv: kv[1])[0] if born else None
    best_tr = max((t for t in trajs if _group_key(t['answer']) == best_key),
                  key=lambda x: x['transmitted'], default=None)
    return {'best_path': best_tr['path'] if best_tr else None,
            'best_answer': best_tr['answer'] if best_tr else None,
            'best_group': best_key, 'born_weights': born,
            'trajectories': trajs, 'method': 'path_integral_born', 'K': K,
            'T': T, 'seed': seed}


def majority_vote(nodes: Dict, edges: Dict, K: int = 20, T: float = 0.5,
                  seed: int = 42, answer_fn=None) -> Dict:
    """多数投票基线: K 条轨迹, 无场筛选, 按答案多数决 (G2对照组)"""
    start, goal = find_start_goal(nodes)
    rng = np.random.default_rng(seed)
    votes = {}
    trajs = []
    for _ in range(K):
        path = boltzmann_walk(nodes, edges, start, goal, T, rng)
        ans = answer_fn(path) if answer_fn else (path[-1] if path else None)
        trajs.append({'path': path, 'answer': ans})
        votes[_group_key(ans)] = votes.get(_group_key(ans), 0) + 1
    best_key = max(votes.items(), key=lambda kv: kv[1])[0] if votes else None
    best_ans = next((t['answer'] for t in trajs if _group_key(t['answer']) == best_key), None)
    return {'best_answer': best_ans, 'votes': votes, 'trajectories': trajs,
            'method': 'majority_vote', 'K': K, 'seed': seed}


def _group_key(ans):
    if isinstance(ans, float):
        return round(ans, 6)
    return ans
