# -*- coding: utf-8 -*-
# deposon_photonics.py — Deposon 光子硬件映射层（兑现 v1.4 roadmap: PCM/MZI/ECM → 光子芯片）
# 2026-08-29。范围声明：组件级一阶数值模型，非流片、非 SPICE 级仿真；
# 参数取 SiPh/SiN 集成光子学文献典型区间（标注为 TYPICAL，非某具体 PDK 保证值）。
#
# 映射表（抽象模型 → 光子组件）：
#   节点 = ring 谐振器（全通型）：g_eff = g_couple/(1+detuning²) 与 ring 的
#          Lorentzian 谐振天然同构——detuning δ ↔ (ω−ω0)/γ（γ=线宽）。
#   t/r 分束 = MZI（Mach-Zehnder）：输出臂功率比 cos²(Δφ/2)/sin²(Δφ/2)，
#          Δφ 由热相移器设置（heater 功耗 P_h ∝ Δφ）。
#   耗散 a（以太不可逆沉积）= PCM 相变单元（如 GST）：吸收能量超阈值 E_th 后
#          非易失地从晶态转非晶态——物理上真正的"不可逆沉积"，
#          这是 v1.4 叙事中"以太"最直接的可制造化身。
#   g_couple 可调性 = ECM/EAM（电吸收调制器）：载流子注入改变耦合强度。
#   反向退火（50 步 ×0.9 收缩）= 绝热相位斜坡（adiabatic phase ramp）：
#          逐步调谐各 ring 的 Δω，收缩因子 ↔ 斜坡步进。
#
# 损耗参数（TYPICAL，区间见注释，非保证值）：
#   波导传播损耗: SiN 0.1 dB/cm（Si 2-3 dB/cm）
#   MZI 插入损耗: 0.5–1.0 dB/个（取 0.7）
#   ring 插入损耗: 0.5 dB/个；ring FSR 内串扰: -20 dB
#   PCM 单元: 1.5 dB/个（晶态），切换阈值能量 E_th ~ 10 nJ 量级
#   耦合器（directional coupler）: 0.2 dB/个
#   探测器噪声等效功率 NEP: ~1 pW/√Hz
import numpy as np

# ---------------------------------------------------------------- 组件参数（TYPICAL）
P = {
    "wg_loss_db_per_cm": 0.1,      # SiN
    "mzi_il_db": 0.7,
    "ring_il_db": 0.5,
    "ring_xtalk_db": -20.0,
    "pcm_il_db": 1.5,
    "coupler_il_db": 0.2,
    "pcm_eth_nj": 10.0,            # 切换阈值能量（量级）
    "nep_pw": 1.0,                 # 探测器 NEP (pW/√Hz)
    "input_power_mw": 1.0,         # 片上输入光功率
    "node_pitch_cm": 0.05,         # 节点间距（500 µm，布局估算）
}

GAMMA = 1.0  # ring 线宽归一化（detuning 与 g_couple 同单位）


# ---------------------------------------------------------------- 组件传递函数
def ring_g_eff(g_couple, detuning, gamma=GAMMA):
    """ring 谐振器有效耦合（drop 口 Lorentzian 峰）。"""
    return g_couple / (1.0 + (detuning / gamma) ** 2)


def mzi_split(delta_phi):
    """MZI 两臂功率比：t=cos²(Δφ/2), r=sin²(Δφ/2)。"""
    t = np.cos(delta_phi / 2.0) ** 2
    r = np.sin(delta_phi / 2.0) ** 2
    return t, r


def heater_power_mw(delta_phi, pi_shift_mw=20.0):
    """热相移器功耗估算：P = P_π · (Δφ/π)（线性一阶模型）。"""
    return pi_shift_mw * abs(delta_phi) / np.pi


def pcm_state(absorbed_nj, eth_nj=None):
    """PCM 状态：累积吸收能量 ≥ E_th → 非易失切换（不可逆沉积的物理实现）。"""
    eth = P["pcm_eth_nj"] if eth_nj is None else eth_nj
    return {"switched": bool(absorbed_nj >= eth),
            "absorbed_nj": float(absorbed_nj), "threshold_nj": eth}


def db(x):
    return 10.0 * np.log10(max(x, 1e-30))


def lin(dbv):
    return 10.0 ** (dbv / 10.0)


# ---------------------------------------------------------------- 图编译：Deposon 图 → 光子网表
def compile_graph_to_netlist(adj, source, target):
    """把 Deposon 邻接矩阵编译为光子网表。

    每节点: 1 ring + 1 PCM 单元; 每有向边 (u,v): 1 MZI(分束=耦合权重) + 1 coupler。
    返回 {nodes:[...], edges:[...], stats}。组件计数是优化对象的基线拓扑（naive）。
    """
    N = adj.shape[0]
    nodes = [{"id": i, "ring": True, "pcm": True,
              "is_source": i == source, "is_target": i == target}
             for i in range(N)]
    edges = []
    for u in range(N):
        for v in range(N):
            if adj[u, v] > 0:
                edges.append({"u": int(u), "v": int(v), "w": float(adj[u, v]),
                              "mzi": True, "coupler": True})
    return {"nodes": nodes, "edges": edges,
            "stats": {"n_nodes": N, "n_edges": len(edges),
                      "n_mzi": len(edges), "n_ring": N, "n_pcm": N,
                      "n_couplers": len(edges)}}


def netlist_loss_db(netlist, path):
    """一条路径（节点序列）的端到端光损耗预算（dB）。"""
    loss = 0.0
    for k in range(len(path) - 1):
        u, v = path[k], path[k + 1]
        edge = next((e for e in netlist["edges"] if e["u"] == u and e["v"] == v),
                    None)
        if edge is None:
            return float("inf")
        loss += (P["wg_loss_db_per_cm"] * P["node_pitch_cm"]
                 + P["mzi_il_db"] + P["coupler_il_db"] + P["ring_il_db"]
                 + P["pcm_il_db"])
    return loss


def path_transmission(netlist, path, input_mw=None):
    """路径端到端残余光功率（mW）。"""
    pin = P["input_power_mw"] if input_mw is None else input_mw
    return pin * lin(-netlist_loss_db(netlist, path))


# ---------------------------------------------------------------- 等价性：抽象模型 vs 硬件模型
def hardware_tra(adj_row, g_couple=1.0, g_aether=0.3):
    """硬件级 t/r/a：g_eff 由 ring（δ=0 谐振）给出，散射公式与抽象模型同式。
    返回 (t, r, a) 与守恒偏差。"""
    g_eff = ring_g_eff(g_couple, 0.0)
    denom = 1.0 + g_eff + g_aether
    t, r, a = 1.0 / denom, g_eff / denom, g_aether / denom
    return {"t": t, "r": r, "a": a, "conservation_err": abs(t + r + a - 1.0)}


def hardware_scores(adj, source, target, g_aether=0.3):
    """硬件级路径打分：每节点 t/r/a 由 ring+MZI 实现，路径透射率连乘；
    PCM 逐节点累积吸收（耗散的物理对应），返回 {v: score}（对全部 v≠source）。
    与抽象 DeposonField.process_path 的 transmitted 同构的一阶模型。"""
    N = adj.shape[0]
    scores = {}
    for v in range(N):
        if v == source:
            continue
        if adj[source, v] > 0:
            path = [source, v]
        else:
            # 两跳路径 source→k→v（一跳优先，与贪心选路同构）
            mids = [k for k in range(N)
                    if adj[source, k] > 0 and adj[k, v] > 0]
            path = [source, mids[0], v] if mids else None
        if path is None:
            scores[v] = 0.0
            continue
        prod = 1.0
        for k in path[1:]:
            u_prev = path[path.index(k) - 1]
            gc = float(adj[u_prev, k])
            tra = hardware_tra(None, g_couple=gc, g_aether=g_aether)
            prod *= tra["t"]
        scores[v] = prod
    return scores


# ---------------------------------------------------------------- 拓扑优化
TOPOLOGIES = ("naive_per_edge_mzi", "shared_bus_ring", "hybrid_tree")


def optimize_topology(adj, source, target):
    """三种布图拓扑的组件数/总损耗对比，返回最优与全表。

    naive_per_edge_mzi: 每边独立 MZI（基线，组件最多）。
    shared_bus_ring: 单总线 ring + 节点抽头（MZI 数=N-1，总线损耗随波导长度）。
    hybrid_tree: 按出度聚合的分树 MZI（组件数=非零出度节点数+叶子数）。
    """
    N = adj.shape[0]
    n_edges = int((adj > 0).sum())
    outdeg = (adj > 0).sum(axis=1)
    active = int((outdeg > 0).sum())

    def topo_loss(topo):
        if topo == "naive_per_edge_mzi":
            comps = {"mzi": n_edges, "ring": N, "pcm": N, "coupler": n_edges}
        elif topo == "shared_bus_ring":
            comps = {"mzi": max(N - 1, 1), "ring": 1, "pcm": N, "coupler": N}
        else:
            comps = {"mzi": active + n_edges // 2, "ring": N, "pcm": N,
                     "coupler": active}
        il = (comps["mzi"] * P["mzi_il_db"] + comps["ring"] * P["ring_il_db"]
              + comps["pcm"] * P["pcm_il_db"]
              + comps["coupler"] * P["coupler_il_db"])
        wg = (N * P["node_pitch_cm"] * P["wg_loss_db_per_cm"]
              * (2.0 if topo == "shared_bus_ring" else 1.0))
        return comps, il + wg

    table = {}
    for tp in TOPOLOGIES:
        comps, loss = topo_loss(tp)
        table[tp] = {"components": comps, "total_il_db": round(loss, 2),
                     "n_components": sum(comps.values())}
    best = min(table, key=lambda tp: (table[tp]["total_il_db"],
                                      table[tp]["n_components"]))
    return {"table": table, "recommended": best,
            "note": "指标最优（总插损+组件数字典序）= shared_bus_ring；"
                    "但单总线单 ring 使全部节点共享同一谐振器，丧失逐节点"
                    "独立 detuning（g_eff 个性化的物理基础）——功能折损。"
                    "工程推荐 = hybrid_tree（保留逐节点 ring，组件数居中），"
                    "双口径如实并列。"}


# ---------------------------------------------------------------- 退火 = 绝热相位斜坡
def annealing_phase_ramp(n_steps=50, shrink=0.9, nonideality_sigma=0.0):
    """反向退火 → 相位斜坡序列：第 t 步 detuning 步进 ∝ shrink^t。
    nonideality_sigma: 相位噪声 std（rad），用于敏感性分析。
    返回 {t: {"detuning_step":..., "cum_phase":..., "heater_mw":...}}。"""
    ramp = {}
    cum = 0.0
    for t in range(n_steps):
        step = shrink ** t
        cum += step
        noise = (np.random.default_rng(1234 + t).normal(0, nonideality_sigma)
                 if nonideality_sigma > 0 else 0.0)
        ramp[t] = {"detuning_step": float(step), "cum_phase": float(cum + noise),
                   "heater_mw": heater_power_mw(cum + noise)}
    return ramp


def ramp_fidelity(ramp_ideal, sigma, n_realizations=50):
    """相位噪声下斜坡保真度：cum_phase 与理想的平均绝对偏差（多次实现）。"""
    devs = []
    for r in range(n_realizations):
        noisy = annealing_phase_ramp(len(ramp_ideal), 0.9, sigma)
        d = np.mean([abs(noisy[t]["cum_phase"] - ramp_ideal[t]["cum_phase"])
                     for t in ramp_ideal])
        devs.append(float(d))
    return {"sigma": sigma, "mean_abs_dev": float(np.mean(devs)),
            "max_abs_dev": float(np.max(devs))}
