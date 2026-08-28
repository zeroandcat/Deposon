# -*- coding: utf-8 -*-
# Deposon v2.0 多图语料生成器（docs/SPEC_v2.0.md §1，预登记冻结）
#   → corpus/v20/{graph_id}.json + corpus/v20/index.json
# 修正（R2/E3，2026-08-29）：load_corpus 增加孤儿哨兵——目录中存在未入册图
# JSON 时显式报错（防「摄入未建索引导致静默漏图」复发）。
import hashlib
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS_DIR = os.path.join(HERE, "corpus", "v20")

GENERATOR_VERSION = "v2.0.0"
FAMILY_SEEDS = {"S1": 200101, "S2": 200102, "S3": 200103,
                "S4": 200104, "S5": 200105, "S6": 200106}
DEFAULT_N = {"S1": 20, "S2": 31, "S3": 30, "S4": 40, "S5": 45, "S6": 45}
SCAN_FAMILIES = ("S1", "S2", "S6")
SCAN_SIZES = (20, 35, 45, 60)
STRUCTURE_NAMES = {
    "S1": "single_chain", "S2": "balanced_binary_tree",
    "S3": "three_hub_competition", "S4": "crosslinked_layered_dag",
    "S5": "sparse_random_dag", "S6": "spoke_convergence_anchor",
    "L": "llm_generated_dag"}

# ---------------------------------------------------------------- 内置小本体
ONTOLOGY_POOL = (
    "生物", "动物界", "植物界", "真菌界", "原生生物界", "脊索动物门",
    "节肢动物门", "软体动物门", "环节动物门", "棘皮动物门", "哺乳纲",
    "鸟纲", "爬行纲", "两栖纲", "硬骨鱼纲", "昆虫纲", "蛛形纲",
    "双子叶植物纲", "单子叶植物纲", "食肉目", "灵长目", "偶蹄目",
    "雀形目", "猫科", "犬科", "熊科", "蔷薇科", "豆科", "禾本科",
    "猫", "狗", "狼", "虎", "鲸", "蝙蝠", "麻雀", "鹰", "青蛙",
    "蛇", "鲤鱼", "蝗虫", "蜘蛛", "玫瑰", "水稻", "大豆", "蘑菇", "酵母菌",
    "物理学", "经典力学", "热力学", "电磁学", "光学", "声学",
    "量子力学", "相对论", "统计物理", "牛顿运动定律", "万有引力",
    "动量守恒", "能量守恒", "角动量", "熵", "温度", "热容量",
    "电场", "磁场", "电磁波", "麦克斯韦方程组", "电流", "电压",
    "电阻", "折射", "反射", "干涉", "衍射", "偏振", "波函数",
    "不确定性原理", "薛定谔方程", "量子纠缠", "光子", "电子",
    "质子", "中子", "原子核", "时空弯曲", "黑洞", "引力波",
    "狭义相对论", "广义相对论", "普朗克常数", "玻尔模型",
)


class FamilyLParseError(ValueError):
    """族 L 响应解析/校验失败（节点数、索引合法、DAG 性）。"""


class CacheMissingError(RuntimeError):
    """族 L 响应缓存缺失：显式报错，绝不伪造数据、不触发 API。"""


def _canonical_sha256(record: dict) -> str:
    payload = {k: v for k, v in record.items() if k != "sha256"}
    blob = json.dumps(payload, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"))
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def _assign_labels(N: int, seed: int) -> list:
    if N > len(ONTOLOGY_POOL):
        raise ValueError(f"N={N} exceeds ontology pool {len(ONTOLOGY_POOL)}")
    rng = np.random.default_rng(seed + 7)
    perm = rng.permutation(len(ONTOLOGY_POOL))
    return [ONTOLOGY_POOL[int(perm[i])] for i in range(N)]


def _topo_order(n: int, edges: list):
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        adj[u].append(v)
        indeg[v] += 1
    ready = [i for i in range(n) if indeg[i] == 0]
    order = []
    while ready:
        u = ready.pop()
        order.append(u)
        for w in adj[u]:
            indeg[w] -= 1
            if indeg[w] == 0:
                ready.append(w)
    return order if len(order) == n else None


def is_dag(n: int, edges: list) -> bool:
    return _topo_order(n, edges) is not None


def longest_path_family(n: int, edges: list):
    order = _topo_order(n, edges)
    if order is None:
        raise ValueError("longest_path_family requires a DAG")
    adj = [[] for _ in range(n)]
    preds = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        preds[v].append(u)
    d_start = [0] * n
    for v in order:
        if preds[v]:
            d_start[v] = 1 + max(d_start[p] for p in preds[v])
    d_end = [0] * n
    for u in reversed(order):
        if adj[u]:
            d_end[u] = 1 + max(d_end[w] for w in adj[u])
    L = max(d_start) if n else 0
    named = {(u, v) for (u, v) in edges
             if d_start[u] + 1 + d_end[v] == L}
    start = min((v for v in range(n) if d_end[v] == L), default=0)
    end = min((v for v in range(n) if d_start[v] == L), default=0)
    return named, L, start, end


def _struct_S1(N: int, seed: int):
    edges = [(i, i + 1) for i in range(N - 1)]
    return {"edges": edges, "named": set(edges), "source": 0, "target": N - 1}


def _struct_S2(N: int, seed: int):
    edges = [((i - 1) // 2, i) for i in range(1, N)]
    named = {(u, v) for (u, v) in edges if 2 * v + 1 < N}
    return {"edges": edges, "named": named, "source": 0, "target": N - 1}


def _struct_S3(N: int, seed: int):
    if N != 30:
        raise ValueError("S3 structure is frozen at N=30 (SPEC v2.0 §1)")
    branch_roots = [4, 5, 6]
    hubs = [1, 2, 3]
    named = set()
    edges = []
    for k in range(3):
        b = branch_roots[k]
        i1, i2, i3, i4 = 7 + 4 * k, 8 + 4 * k, 9 + 4 * k, 10 + 4 * k
        hub = hubs[k]
        chain = [(0, b), (b, i1), (i1, i2), (i2, hub),
                 (b, i3), (i3, i4), (i4, hub)]
        edges += chain
        named.update(chain)
    backbone = [0] + branch_roots + list(range(7, 19))
    for j, node in enumerate(range(19, N)):
        edges.append((backbone[j % len(backbone)], node))
    return {"edges": edges, "named": named, "source": 0, "target": hubs[0]}


def _struct_S4(N: int, seed: int):
    if N != 40:
        raise ValueError("S4 structure is frozen at N=40 (SPEC v2.0 §1)")
    rng = np.random.default_rng(seed)
    n_layer, width = 5, 8
    edges = []
    for l in range(n_layer - 1):
        for p in range(width):
            u = l * width + p
            offs = rng.choice(width, size=2, replace=False)
            for off in offs:
                edges.append((u, (l + 1) * width + int((p + off) % width)))
    for l in range(n_layer - 2):
        for p in range(width):
            u = l * width + p
            off = int(rng.integers(width))
            edges.append((u, (l + 2) * width + (p + off) % width))
    edges = sorted(set(edges))
    named, _L, start, end = longest_path_family(N, edges)
    return {"edges": edges, "named": named, "source": start, "target": end}


def _struct_S5(N: int, seed: int):
    if N != 45:
        raise ValueError("S5 structure is frozen at N=45 (SPEC v2.0 §1)")
    rng = np.random.default_rng(seed)
    p, cap = 0.06, 3
    outdeg = np.zeros(N, dtype=int)
    indeg = np.zeros(N, dtype=int)
    edges = []
    for i in range(N):
        for j in range(i + 1, N):
            if outdeg[i] >= cap or indeg[j] >= cap:
                continue
            if rng.random() < p:
                edges.append((i, j))
                outdeg[i] += 1
                indeg[j] += 1
    named, _L, start, end = longest_path_family(N, edges)
    return {"edges": edges, "named": named, "source": start, "target": end}


def _struct_S6(N: int, seed: int):
    if N < 13:
        raise ValueError("S6 requires N>=13 (13 backbone nodes)")
    ROOT, GOAL = 0, 1
    legit = [2, 3, 4, 5]
    branch_roots = [2, 3, 4, 5, 6, 8, 10, 11, 12]
    named = [(ROOT, b) for b in branch_roots]
    named += [(m, GOAL) for m in legit]
    named += [(6, 7), (7, GOAL), (8, 9), (9, GOAL)]
    edges = list(named)
    for k in range(13, N):
        edges.append((branch_roots[(k - 13) % 9], k))
    return {"edges": edges, "named": set(named), "source": ROOT, "target": GOAL}


_STRUCT_BUILDERS = {"S1": _struct_S1, "S2": _struct_S2, "S3": _struct_S3,
                    "S4": _struct_S4, "S5": _struct_S5, "S6": _struct_S6}


def graph_id_for(family: str, N: int) -> str:
    return family if N == DEFAULT_N[family] else f"{family}_n{N}"


def generate_graph(family: str, N: int = None, seed: int = None) -> dict:
    if family not in _STRUCT_BUILDERS:
        raise ValueError(f"unknown family: {family}")
    N = DEFAULT_N[family] if N is None else int(N)
    if seed is None:
        seed = FAMILY_SEEDS[family] + (0 if N == DEFAULT_N[family] else N)
    struct = _STRUCT_BUILDERS[family](N, seed)
    edges = [list(map(int, e)) for e in struct["edges"]]
    named = sorted({(int(u), int(v)) for (u, v) in struct["named"]})
    edge_set = {tuple(e) for e in edges}
    named_set = set(named)
    if not named_set <= edge_set:
        raise ValueError(f"{family}: named edges not subset of edges")
    if not is_dag(N, [tuple(e) for e in edges]):
        raise ValueError(f"{family}: structure is not a DAG")
    filler = sorted(edge_set - named_set)
    labels = _assign_labels(N, seed)
    rec = {"graph_id": graph_id_for(family, N), "family": "S",
           "structure": STRUCTURE_NAMES[family], "N": N,
           "nodes": list(range(N)), "labels": labels, "edges": edges,
           "named_edges": [list(e) for e in named],
           "filler_edges": [list(e) for e in filler],
           "source": int(struct["source"]), "target": int(struct["target"]),
           "seed": int(seed), "generator_version": GENERATOR_VERSION}
    rec["sha256"] = _canonical_sha256(rec)
    return rec


def corpus_plan() -> list:
    plan = [(f, None) for f in ("S1", "S2", "S3", "S4", "S5", "S6")]
    for f in SCAN_FAMILIES:
        for N in SCAN_SIZES:
            if N != DEFAULT_N[f]:
                plan.append((f, N))
    return plan


def build_index(corpus_dir: str = CORPUS_DIR) -> dict:
    entries = []
    for fn in sorted(os.listdir(corpus_dir)):
        if not fn.endswith(".json") or fn == "index.json":
            continue
        with open(os.path.join(corpus_dir, fn), encoding="utf-8") as f:
            g = json.load(f)
        entries.append({"graph_id": g["graph_id"], "family": g["family"],
                        "structure": g["structure"], "N": g["N"],
                        "n_edges": len(g["edges"]),
                        "n_named": len(g["named_edges"]),
                        "n_filler": len(g["filler_edges"]),
                        "source": g["source"], "target": g["target"],
                        "seed": g["seed"], "sha256": g["sha256"], "file": fn})
    entries.sort(key=lambda e: e["graph_id"])
    idx = {"corpus": "v20", "generator_version": GENERATOR_VERSION,
           "spec": "docs/SPEC_v2.0.md §1",
           "named_filler_rule": ("named=主干结构边（链/树父子主链、DAG 最长路径族），"
                                 "filler=其余结构边；无诱饵边（SPEC §1 冻结）"),
           "n_graphs": len(entries), "graphs": entries}
    with open(os.path.join(corpus_dir, "index.json"), "w", encoding="utf-8") as f:
        json.dump(idx, f, ensure_ascii=False, indent=1)
    return idx


def build_corpus(corpus_dir: str = CORPUS_DIR) -> dict:
    os.makedirs(corpus_dir, exist_ok=True)
    written = []
    for family, N in corpus_plan():
        rec = generate_graph(family, N)
        path = os.path.join(corpus_dir, f"{rec['graph_id']}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(rec, f, ensure_ascii=False, indent=1)
        written.append(rec["graph_id"])
    idx = build_index(corpus_dir)
    return {"written": written, "n_graphs": idx["n_graphs"]}


def load_corpus(corpus_dir: str = CORPUS_DIR, families=("S",)) -> list:
    """按 index.json 顺序读入图记录（默认只读族 S）。
    孤儿哨兵（R2/E3）：目录中存在未入册的图 JSON 时显式报错——
    防「摄入未建索引导致静默漏图」复发。"""
    with open(os.path.join(corpus_dir, "index.json"), encoding="utf-8") as f:
        idx = json.load(f)
    registered = {e["file"] for e in idx["graphs"]}
    orphans = sorted(fn for fn in os.listdir(corpus_dir)
                     if fn.endswith(".json") and fn != "index.json"
                     and fn not in registered)
    if orphans:
        raise RuntimeError(
            f"corpus orphan graphs (not in index.json): {orphans} — "
            "先运行 build_index()（R2/E3 哨兵）")
    out = []
    for e in idx["graphs"]:
        if families and e["family"] not in families:
            continue
        with open(os.path.join(corpus_dir, e["file"]), encoding="utf-8") as f:
            out.append(json.load(f))
    return out


# ---------------------------------------------------------------- 族 L（LLM 生成族）
# 只构造 prompt 与解析校验响应；API 调用由主代理另行执行（本模块不发起任何
# LLM 调用）。主题域按 SPEC §1 对立统一：两个「抽象→具体」域 + 两个
# 「过程→结果」域；v2.0-BigQuiz 扩展为 6 域（+geography_world/project_management）。
FAMILY_L_DOMAINS = ("physics_concepts", "biological_taxonomy",
                    "algorithm_process", "historical_causality",
                    "geography_world", "project_management")
FAMILY_L_MIN_NODES, FAMILY_L_MAX_NODES = 30, 45

_DOMAIN_BRIEF = {
    "physics_concepts": (
        "物理学概念层级（抽象→具体：从「物理学」逐层细化到具体定律/粒子，"
        "方向语义 = 抽象概念指向其具体化）"),
    "biological_taxonomy": (
        "生物分类层级（抽象→具体：从「生物」逐层细化到具体物种，"
        "方向语义 = 上位分类指向下位分类）"),
    "algorithm_process": (
        "算法流程（过程→结果：从输入/初始化经中间步骤指向输出/终止状态，"
        "方向语义 = 前驱步骤指向后继步骤）"),
    "historical_causality": (
        "历史因果（过程→结果：从背景/起因经关键事件指向结果/影响，"
        "方向语义 = 原因指向结果）"),
    "geography_world": (
        "世界地理层级（抽象→具体：从「世界」逐层细化到大洲/国家/"
        "城市/地标，方向语义 = 大区域指向其组成部分）"),
    "project_management": (
        "项目管理流程（过程→结果：从立项/需求经计划/执行/监控"
        "到交付/复盘，方向语义 = 前驱阶段指向后继阶段）"),
}

_PROMPT_TEMPLATE = """你是一个概念脑图构建器。请为主题域「{domain}」构建一张有向无环概念脑图。

主题域要求：{brief}

硬性结构约束（必须全部满足，输出前自检）：
1. 节点数在 30 到 45 之间（含两端）。
2. 图为有向无环图（DAG）：不允许出现任何有向环，不允许自环。
3. 边为有向边 [i, j]（节点索引，0 基），语义方向按主题域要求。
4. 图应连通（任一节点可由某根节点沿有向边到达），允许分支与汇聚。
5. 节点标签为简短真实概念词（中文，≤12 字），不得重复，不得使用占位符。

输出格式：只输出一个 JSON 对象，不要输出任何其他文字、不要用代码围栏：
{{"nodes": ["标签0", "标签1", ...], "edges": [[0, 1], [0, 2], ...]}}"""


def build_familyL_prompts() -> dict:
    """按 SPEC §1 族 L 生成 6 个主题域的建图 prompt（不执行 API）。
    返回 {domain: prompt}。"""
    return {d: _PROMPT_TEMPLATE.format(domain=d, brief=_DOMAIN_BRIEF[d])
            for d in FAMILY_L_DOMAINS}


def familyL_prompt_manifest() -> dict:
    """{domain: {"prompt_sha256": ...}}；prompt_sha256 落盘纪律（SPEC §5）。"""
    return {d: {"prompt_sha256": hashlib.sha256(
                p.encode("utf-8")).hexdigest()}
            for d, p in build_familyL_prompts().items()}


def _extract_json_object(text: str) -> str:
    if not isinstance(text, str):
        raise FamilyLParseError("response is not a string")
    t = text.strip()
    if t.startswith("```"):
        lines = t.splitlines()
        lines = [ln for ln in lines if not ln.strip().startswith("```")]
        t = "\n".join(lines).strip()
    lo, hi = t.find("{"), t.rfind("}")
    if lo < 0 or hi <= lo:
        raise FamilyLParseError("no JSON object found in response")
    return t[lo:hi + 1]


def parse_familyL_response(text: str,
                           min_nodes: int = FAMILY_L_MIN_NODES,
                           max_nodes: int = FAMILY_L_MAX_NODES) -> dict:
    blob = _extract_json_object(text)
    try:
        obj = json.loads(blob)
    except json.JSONDecodeError as e:
        raise FamilyLParseError(f"invalid JSON: {e}") from e
    if not isinstance(obj, dict) or "nodes" not in obj or "edges" not in obj:
        raise FamilyLParseError("response must contain 'nodes' and 'edges'")
    nodes, edges = obj["nodes"], obj["edges"]
    if not isinstance(nodes, list) or not all(isinstance(x, str) and x.strip()
                                              for x in nodes):
        raise FamilyLParseError("nodes must be a list of non-empty strings")
    if len(set(nodes)) != len(nodes):
        raise FamilyLParseError("node labels must be unique")
    n = len(nodes)
    if not (min_nodes <= n <= max_nodes):
        raise FamilyLParseError(
            f"node count {n} outside [{min_nodes}, {max_nodes}]")
    if not isinstance(edges, list) or not edges:
        raise FamilyLParseError("edges must be a non-empty list")
    clean = []
    for e in edges:
        if (not isinstance(e, (list, tuple)) or len(e) != 2
                or not all(isinstance(x, int) and not isinstance(x, bool)
                           for x in e)):
            raise FamilyLParseError(f"edge must be [int, int], got {e!r}")
        u, v = int(e[0]), int(e[1])
        if u == v:
            raise FamilyLParseError(f"self-loop edge [{u}, {v}]")
        if not (0 <= u < n and 0 <= v < n):
            raise FamilyLParseError(
                f"edge index [{u}, {v}] out of range for N={n}")
        clean.append((u, v))
    clean = sorted(set(clean))
    if not is_dag(n, clean):
        raise FamilyLParseError("edge set contains a directed cycle (not a DAG)")
    return {"nodes": list(nodes), "edges": [list(e) for e in clean]}


def main():
    summary = build_corpus()
    manifest = familyL_prompt_manifest()
    print(json.dumps({"corpus_dir": CORPUS_DIR, "written": summary["written"],
                      "n_graphs": summary["n_graphs"],
                      "familyL_prompt_sha256": manifest},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
