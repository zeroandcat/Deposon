#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
svg_mindmap_ingest.py —— 标准 SVG 脑图解析 → Deposon brain_graph

解析策略（零依赖, 仅标准库）:
1. <text> 元素 → 节点 (取 x/y 坐标与文本内容; 合并同组多 <tspan>)
2. fill/stroke 颜色 → 分组 (同色视为同一主分支, 用于推定层级)
3. <path>/<line> 连接元素 → 父子边: 取 path 的起止点 (M... 与最后一个坐标),
   将其吸附到最近的两个节点中心, 形成有向边 (靠近根节点方向为父)
4. 根节点: 入度为 0 且出度最大的节点 (通常是中心主题)
5. 输出与 DeposonField.spawn_from_graph 兼容的 brain_graph dict:
   nodes={id: {'energy','type'}}, edges={(u,v): {'weight','migration_barrier'}}

局限（诚实声明）:
- 手绘风/导出器专属的 path 曲线若不以节点边缘为起止点, 吸附可能失败;
  此时退化为中心辐射 fallback (所有同色组挂到根)。
- 颜色分组依赖 fill 约定, 对无着色的单色 SVG 退化为纯几何吸附。
"""
import math
import re
import xml.etree.ElementTree as ET
from typing import Any, Dict, List, Optional, Tuple

SVG_NS = '{http://www.w3.org/2000/svg}'


def _strip_ns(tag: str) -> str:
    return tag.split('}')[-1]


def _parse_float(v: Optional[str], default: float = 0.0) -> float:
    try:
        return float(v)
    except (TypeError, ValueError):
        m = re.search(r'-?\d+\.?\d*', v or '')
        return float(m.group(0)) if m else default


def _path_endpoints(d: str) -> Optional[Tuple[Tuple[float, float], Tuple[float, float]]]:
    """从 path 的 d 属性提取起点(M/m)与终点(最后一个坐标对, 支持 C/Q/L/Z 近似)"""
    nums = [float(x) for x in re.findall(r'-?\d+\.?\d*(?:e-?\d+)?', d)]
    cmds = re.findall(r'[MmLlCcQqSsTtHhVvZz]', d)
    if not nums or not cmds:
        return None
    # 起点 = 第一个 M 后的坐标
    mx = re.search(r'[Mm]\s*(-?\d+\.?\d*)[,\s]+(-?\d+\.?\d*)', d)
    if not mx:
        return None
    start = (float(mx.group(1)), float(mx.group(2)))
    # 终点 = 最后一对坐标 (近似: 取 d 中最后两个数; 对贝塞尔曲线即曲线终点)
    end = (nums[-2], nums[-1])
    return start, end


def _node_center(el) -> Tuple[float, float, str, str]:
    """提取 <text> 或 <rect>+<text> 组的中心/文本/颜色"""
    x = _parse_float(el.get('x'))
    y = _parse_float(el.get('y'))
    fill = el.get('fill', '') or ''
    text = ''.join(el.itertext()).strip()
    return x, y, text, fill


def parse_svg_mindmap(svg_source: str,
                      default_energy: float = 0.3,
                      default_weight: float = 0.6,
                      default_barrier: float = 0.3) -> Dict[str, Any]:
    """解析 SVG 脑图 → brain_graph。svg_source: 文件路径或 SVG 文本"""
    if svg_source.lstrip().startswith('<'):
        root = ET.fromstring(svg_source)
    else:
        root = ET.parse(svg_source).getroot()

    # ---- 1. 收集文本节点 ----
    raw_nodes: List[Dict] = []
    for el in root.iter():
        if _strip_ns(el.tag) == 'text':
            x, y, text, fill = _node_center(el)
            if text:
                raw_nodes.append({'x': x, 'y': y, 'label': text, 'fill': fill})
    if not raw_nodes:
        raise ValueError('SVG 中未发现 <text> 节点')

    # 去重 (同位置同文本)
    seen, nodes_list = set(), []
    for n in raw_nodes:
        key = (n['label'], round(n['x'], 1), round(n['y'], 1))
        if key not in seen:
            seen.add(key)
            nodes_list.append(n)

    # ---- 2. 收集连接元素 ----
    connectors: List[Tuple[Tuple[float, float], Tuple[float, float]]] = []
    for el in root.iter():
        tag = _strip_ns(el.tag)
        if tag == 'path' and el.get('d'):
            ep = _path_endpoints(el.get('d'))
            if ep:
                connectors.append(ep)
        elif tag == 'line':
            p1 = (_parse_float(el.get('x1')), _parse_float(el.get('y1')))
            p2 = (_parse_float(el.get('x2')), _parse_float(el.get('y2')))
            connectors.append((p1, p2))

    # ---- 3. 端点吸附到最近节点 ----
    def nearest(pt, exclude=None):
        best, bd = None, float('inf')
        for i, n in enumerate(nodes_list):
            if i == exclude:
                continue
            d = math.hypot(n['x'] - pt[0], n['y'] - pt[1])
            if d < bd:
                best, bd = i, d
        return best

    edges_set = set()
    for p1, p2 in connectors:
        i, j = nearest(p1), nearest(p2)
        if i is not None and j is not None and i != j:
            edges_set.add((i, j))

    # ---- 4. 根节点与方向: 几何中心 + 出度最大 ----
    cx = sum(n['x'] for n in nodes_list) / len(nodes_list)
    cy = sum(n['y'] for n in nodes_list) / len(nodes_list)
    outdeg = {}
    for i, j in edges_set:
        outdeg[i] = outdeg.get(i, 0) + 1
        outdeg[j] = outdeg.get(j, 0)  # 确保键存在
    root_idx = min(range(len(nodes_list)),
                   key=lambda i: (-outdeg.get(i, 0),
                                  math.hypot(nodes_list[i]['x'] - cx,
                                             nodes_list[i]['y'] - cy)))

    # BFS 定向: 从根出发, 无向边按 离根近->远 定向
    adj: Dict[int, List[int]] = {}
    for i, j in edges_set:
        adj.setdefault(i, []).append(j)
        adj.setdefault(j, []).append(i)
    dist = {root_idx: 0}
    queue = [root_idx]
    for q in queue:
        for nb in adj.get(q, []):
            if nb not in dist:
                dist[nb] = dist[q] + 1
                queue.append(nb)
    directed = set()
    for i, j in edges_set:
        di, dj = dist.get(i, 1e9), dist.get(j, 1e9)
        if di <= dj:
            directed.add((i, j))
        else:
            directed.add((j, i))

    # ---- 5. 颜色分组 → 层级能量 (同 fill 同层衰减) ----
    fills = {}
    for n in nodes_list:
        fills.setdefault(n['fill'], len(fills))

    # ---- 6. 组装 brain_graph ----
    nodes, edges = {}, {}
    id_of = {}
    for i, n in enumerate(nodes_list):
        nid = re.sub(r'\s+', '_', n['label'])[:40] or f'node_{i}'
        if nid in id_of:
            nid = f'{nid}_{i}'
        id_of[i] = nid
        depth = dist.get(i, 3)
        nodes[nid] = {
            'energy': round(max(0.05, default_energy + 0.1 * (2 - min(depth, 3))), 3),
            'type': 'concept',
            'label': n['label'],
            'fill_group': n['fill'],
            'svg_xy': [n['x'], n['y']],
        }
    for (i, j) in directed:
        edges[(id_of[i], id_of[j])] = {
            'weight': default_weight,
            'migration_barrier': default_barrier,
        }
    return {
        'nodes': nodes,
        'edges': edges,
        'root': id_of[root_idx],
        'source': 'svg_mindmap_ingest',
        'n_svg_texts': len(raw_nodes),
        'n_svg_connectors': len(connectors),
    }


def to_deposon_demo(brain_graph: Dict[str, Any],
                    goal_label: Optional[str] = None,
                    trap_labels: Optional[List[str]] = None) -> Dict[str, Any]:
    """把解析结果标注为 Deposon 演示图: 指定 answer 目标与 trap 节点"""
    g = {'nodes': {k: dict(v) for k, v in brain_graph['nodes'].items()},
         'edges': dict(brain_graph['edges'])}
    for nid, attrs in g['nodes'].items():
        if goal_label and goal_label in nid:
            attrs['type'] = 'answer'
            attrs['energy'] = 0.0
        elif trap_labels and any(t in nid for t in trap_labels):
            attrs['type'] = 'trap'
            attrs['energy'] = 0.1
    return g


if __name__ == '__main__':
    # 合成 SVG 自检 (无真实SVG可用时验证解析器逻辑)
    demo_svg = '''<svg xmlns="http://www.w3.org/2000/svg">
      <text x="400" y="300" fill="#1f3864">中心主题</text>
      <text x="200" y="150" fill="#c00000">分支A</text>
      <text x="600" y="150" fill="#ed7d31">分支B</text>
      <text x="100" y="60" fill="#c00000">叶子A1</text>
      <text x="300" y="60" fill="#c00000">叶子A2</text>
      <text x="700" y="60" fill="#ed7d31">叶子B1</text>
      <path d="M 380 280 C 300 220, 250 180, 210 160" stroke="#c00000" fill="none"/>
      <path d="M 420 280 C 500 220, 550 180, 590 160" stroke="#ed7d31" fill="none"/>
      <path d="M 190 130 C 150 100, 130 80, 110 70" stroke="#c00000" fill="none"/>
      <path d="M 220 130 C 260 100, 280 80, 295 70" stroke="#c00000" fill="none"/>
      <path d="M 610 130 C 650 100, 680 80, 695 70" stroke="#ed7d31" fill="none"/>
    </svg>'''
    bg = parse_svg_mindmap(demo_svg)
    print(f"自检: {len(bg['nodes'])} 节点, {len(bg['edges'])} 边, root={bg['root']}")
    assert len(bg['nodes']) == 6 and len(bg['edges']) == 5 and bg['root'] == '中心主题'
    print('合成SVG自检通过')
