# -*- coding: utf-8 -*-
# Deposon v2.0 多图语料生成器（docs/SPEC_v2.0.md §1，预登记冻结）
#   → corpus/v20/{graph_id}.json + corpus/v20/index.json
#
# 族 S（结构合成族，6 型 + 量变质变尺寸扫描）：
#   S1 单链 N=20（否定辐条/汇聚）；S2 平衡二叉树 N=31（否定单 hub）；
#   S3 三 hub 竞争 N=30（否定单汇聚）；S4 带横向跨链 DAG N=40（否定纯树）；
#   S5 稀疏随机 DAG N=45（否定一切枢纽）；S6 v1.9 同型辐条汇聚锚点 N=45
#   （肯定项，复现性对照，同结构新种子新标签）。
#   尺寸扫描钩子：S1/S2/S6 支持 N ∈ {20, 35, 45, 60}（SPEC §1 量变质变扫描）。
#
# named/filler 冻结操作化（SPEC §1：named=主干结构边，filler=其余结构边，
# 不加任何诱饵边）：
#   S1 链：全部链边 = named（纯链无其余结构边，filler=∅，如实披露）；
#   S2 树：named = 子节点仍为内部节点的父子边（主链），filler = 叶边
#          （与 v1.9 filler=叶部挂载边的口径一致；平衡树无唯一主干，
#          该操作化在生成器中冻结并披露）；
#   S3 三 hub：named = root→分支根 + 每条分支两条汇聚链的全部边，filler = 叶挂载；
#   S4/S5 DAG：named = 最长路径族（边 e=(u,v) 满足 d_start[u]+1+d_end[v]=L，
#          d_start/d_end 为任意起点/终点最长路径 DP），filler = 其余边；
#   S6 锚点：named = v1.9 同型 17 条骨架边（9 分支 + 4 正当汇聚 + 4 诱饵路径
#          结构边——结构沿用 v1.9 锚点作对照，标签全部换新，无语义诱饵），
#          filler = 叶挂载边。
#
# 标签：内置小本体（生物分类 + 物理概念，真实词），种子驱动随机指派 ⇒
#   标签语义与结构脱钩（SPEC §1）。族 S 不跑 LLM 先验臂（主终点不靠它）。
#
# 族 L（LLM 生成族）：本模块只提供 build_familyL_prompts() /
#   familyL_prompt_manifest() / parse_familyL_response()；API 调用由主代理
#   另行执行，摄入见 run_v20_familyL_ingest.py。no LLM API calls issued here。
#
# 确定性：每张图 seed 落盘；sha256 为内容哈希（除 sha256 字段外的 canonical
#   JSON）。同 seed 同 sha256（tests/test_v20.py 锁定）。
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
# 真实词（生物分类 + 物理概念层级），池大小 ≥ 最大 N（60），图内不重复。
ONTOLOGY_POOL = (
    # 生物分类（抽象→具体）
    "生物", "动物界", "植物界", "真菌界", "原生生物界", "脊索动物门",
    "节肢动物门", "软体动物门", "环节动物门", "棘皮动物门", "哺乳纲",
    "鸟纲", "爬行纲", "两栖纲", "硬骨鱼纲", "昆虫纲", "蛛形纲",
    "双子叶植物纲", "单子叶植物纲", "食肉目", "灵长目", "偶蹄目",
    "雀形目", "猫科", "犬科", "熊科", "蔷薇科", "豆科", "禾本科",
    "猫", "狗", "狼", "虎", "鲸", "蝙蝠", "麻雀", "鹰", "青蛙",
    "蛇", "鲤鱼", "蝗虫", "蜘蛛", "玫瑰", "水稻", "大豆", "蘑菇", "酵母菌",
    # 物理概念（抽象→具体）
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


# ---------------------------------------------------------------- 公共工具
def _canonical_sha256(record: dict) -> str:
    """除 sha256 字段外的 canonical JSON（sort_keys, 紧凑分隔符）的 sha256。"""
    payload = {k: v for k, v in record.items() if k != "sha256"}
    blob = json.dumps(payload, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"))
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def _assign_labels(N: int, seed: int) -> list:
    """种子驱动从本体池不重复抽样 ⇒ 标签语义与结构位置脱钩。"""
    if N > len(ONTOLOGY_POOL):
        raise ValueError(f"N={N} exceeds ontology pool {len(ONTOLOGY_POOL)}")
    rng = np.random.default_rng(seed + 7)
    perm = rng.permutation(len(ONTOLOGY_POOL))
    return [ONTOLOGY_POOL[int(perm[i])] for i in range(N)]


def _topo_order(n: int, edges: list):
    """Kahn 拓扑序；含环返回 None。"""
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
    """DAG 最长路径族：返回 (named_set, L, start, end)。

    d_start[v] = 以 v 结尾的最长路径长度（任意起点，base 0）；
    d_end[u]   = 以 u 起点的最长路径长度。边 (u,v) 在某条最长路径上
    ⟺ d_start[u] + 1 + d_end[v] == L（L = 全图最长路径长）。
    start/end = 某条最长路径的端点（最小索引确定性选取），供场引导
    source/target 使用。空边集退化：L=0，start=end=0，named=∅。
    """
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


# ---------------------------------------------------------------- 族 S 结构
def _struct_S1(N: int, seed: int):
    """S1 单链：0→1→…→N-1；named = 全部链边，filler = ∅（如实披露）。"""
    edges = [(i, i + 1) for i in range(N - 1)]
    return {"edges": edges, "named": set(edges), "source": 0, "target": N - 1}


def _struct_S2(N: int, seed: int):
    """S2 平衡（完全）二叉树：堆序 parent=(i-1)//2；named = 子节点仍为内部
    节点的父子边（主链），filler = 叶边（v1.9 filler=叶部口径）。"""
    edges = [((i - 1) // 2, i) for i in range(1, N)]
    named = {(u, v) for (u, v) in edges if 2 * v + 1 < N}
    return {"edges": edges, "named": named, "source": 0, "target": N - 1}


def _struct_S3(N: int, seed: int):
    """S3 三 hub 竞争（固定 30 节点）：root 0；hub 1/2/3；分支根 4/5/6；
    每分支两条并行链汇聚于本分支 hub（hub 入度=2，「3 个 GOAL 式汇聚点」）；
    其余 11 节点为 filler 叶，轮转挂到骨架节点。named = 全部骨架链边。"""
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
    for j, node in enumerate(range(19, N)):  # 11 个 filler 叶，轮转挂载
        edges.append((backbone[j % len(backbone)], node))
    return {"edges": edges, "named": named, "source": 0, "target": hubs[0]}


def _struct_S4(N: int, seed: int):
    """S4 带横向跨链的 DAG（固定 40 节点）：5 层 × 8 节点；相邻层每节点 2 条
    确定性伪随机边 + 跳层边（l→l+2 每节点 1 条）。named = 最长路径族。"""
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
    for l in range(n_layer - 2):  # 跳层边 l → l+2（横向跨链/跳跃）
        for p in range(width):
            u = l * width + p
            off = int(rng.integers(width))
            edges.append((u, (l + 2) * width + (p + off) % width))
    edges = sorted(set(edges))
    named, _L, start, end = longest_path_family(N, edges)
    return {"edges": edges, "named": named, "source": start, "target": end}


def _struct_S5(N: int, seed: int):
    """S5 稀疏随机 DAG（固定 45 节点）：固定序 i<j，边概率 p=0.06，
    出/入度上限 3（无枢纽）。named = 最长路径族。"""
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
    """S6 v1.9 同型辐条汇聚锚点（结构镜像 reconstruct_mindmap，N≥13 可扫）：
    9 条 ROOT 分支（4 正当 + 2 结构诱饵路径 + 3 未命名），4 正当路径与
    2 诱饵路径汇聚 GOAL；filler = N-13 个叶节点轮转挂 9 分支根。
    named = 17 条骨架边（与 v1.9 path_edges_named 同型）。新种子新标签。"""
    if N < 13:
        raise ValueError("S6 requires N>=13 (13 backbone nodes)")
    ROOT, GOAL = 0, 1
    legit = [2, 3, 4, 5]
    branch_roots = [2, 3, 4, 5, 6, 8, 10, 11, 12]
    named = [(ROOT, b) for b in branch_roots]
    named += [(m, GOAL) for m in legit]
    named += [(6, 7), (7, GOAL), (8, 9), (9, GOAL)]  # 结构诱饵路径（无标签语义）
    edges = list(named)
    for k in range(13, N):
        edges.append((branch_roots[(k - 13) % 9], k))
    return {"edges": edges, "named": set(named), "source": ROOT, "target": GOAL}


_STRUCT_BUILDERS = {"S1": _struct_S1, "S2": _struct_S2, "S3": _struct_S3,
                    "S4": _struct_S4, "S5": _struct_S5, "S6": _struct_S6}


def graph_id_for(family: str, N: int) -> str:
    """主档（默认 N）用裸族名；扫描档用 {family}_n{N}。"""
    return family if N == DEFAULT_N[family] else f"{family}_n{N}"


def generate_graph(family: str, N: int = None, seed: int = None) -> dict:
    """确定性生成一张族 S 图（seed 落盘，sha256 内容哈希）。"""
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
    """全语料计划：6 张主档 + S1/S2/S6 × N∈{20,35,45,60} 扫描（去重主档）。"""
    plan = [(f, None) for f in ("S1", "S2", "S3", "S4", "S5", "S6")]
    for f in SCAN_FAMILIES:
        for N in SCAN_SIZES:
            if N != DEFAULT_N[f]:
                plan.append((f, N))
    return plan


def build_index(corpus_dir: str = CORPUS_DIR) -> dict:
    """由 corpus_dir 下全部图 JSON 重建 index.json（族 S + 已摄入的族 L）。"""
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
    """生成族 S 全部图（主档 + 扫描档）并写盘 + 重建 index。"""
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
    """按 index.json 顺序读入图记录（默认只读族 S）。"""
    with open(os.path.join(corpus_dir, "index.json"), encoding="utf-8") as f:
        idx = json.load(f)
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
    """从响应文本提取 JSON 对象（容忍代码围栏与前后噪声）。"""
    if not isinstance(text, str):
        raise FamilyLParseError("response is not a string")
    t = text.strip()
    if t.startswith("```"):  # 去代码围栏
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
    """解析并校验族 L 建图响应（SPEC §1：30–45 节点有向边列表 JSON）。

    校验：JSON 可解析且含 nodes/edges；节点数 ∈ [30,45]；标签为非空
    不重复字符串；边索引合法（0≤i,j<N，i≠j）；去重后边集为 DAG。
    合法返回 {"nodes": [...], "edges": [[i,j],...]}；否则抛
    FamilyLParseError（显式原因，绝不静默修复）。
    """
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
