# SPEC — Deposon v1.5 凝子扩散原型（落到实处版）

目标：把 Roadmap_v1.5 落成最小可验证原型——**固定节点集上的边权场补全**（masked edge completion）。
不做 API 调用，不宣称 AGI。所有数字必须可复现（种子固定）。

## 表示与物理约定（与 v1.4 论文符号一致，不得矛盾）

- 图：固定节点集 {0..N-1} 的有向图。生成对象是**边权场** W ∈ R^{N×N}，W[i,j] 为 i→j 的出边权重。
- 幺正性投影：对每个有出边的节点 i，其出边权重行 W[i,:] 归一化到概率单纯形（Σ_j W[i,j]=1，W≥0）。
  这是 v1.4 T+R+A=1 硬投影在生成场上的对应物；代码注释与文档字符串中用 `T+R+A=1 analog` 表述，禁止发明新符号与之冲突。
- 透射率内核（复用 v1.4 定义）：对边 e，`t_e = 1/(1+g_eff+g_aether)`，`g_eff = g_couple/(1+δ²)`；路径透射率为边 t 连乘。
- 边界值条件化：观测边集合 O（Dirichlet 边界）在任何前向/反向步骤中**逐元素冻结**；掩码边集合 M 才是生成自由度。

## 模块 `deposon_diffusion.py`（接口契约，签名不得改）

```python
@dataclass
class DiffusionConfig:
    n_steps: int = 50          # 扩散步数
    beta_schedule: str = "linear"  # "linear" | "cosine"
    prior: str = "uniform_out"     # 行均匀先验
    lr: float = 0.1            # 反向退火步长
    lam_smooth: float = 0.01   # 平滑正则
    field_guidance: bool = True    # False = G2 消融（无场引导）
    seed: int = 0

def project_simplex_rows(W: np.ndarray) -> np.ndarray
    # 行裁剪到非负并归一；零行映射到均匀行。容差 1e-12。

def forward_diffuse(W0: np.ndarray, mask: np.ndarray, cfg: DiffusionConfig) -> list[np.ndarray]
    # mask[i,j]=True 表示该边是被掩码的生成自由度；False=边界，冻结。
    # W_t[i,:] = (1-b_t)*W_{t-1}[i,:] + b_t*prior_row，逐步推向行均匀先验；每步后投影。
    # 边界元素每步重置为 W0 原值。

def scatter_energy(W: np.ndarray, gold_edges: set[tuple[int,int]] | None,
                   source: int, target: int) -> float
    # 场引导能量：E = -log(从 source 到 target 的最大路径透射率) + lam_smooth*平滑项
    # 最大路径透射率用 Dijkstra on -log t_e。t_e 由 W[i,j] 经固定映射得到（见下）。
    # gold_edges 仅用于评估，不得进入能量（防泄漏）。

def reverse_denoise(WT: np.ndarray, mask: np.ndarray, cfg: DiffusionConfig,
                    source: int, target: int) -> np.ndarray
    # 从先验出发退火：每步对 mask 自由度做能量的数值/解析梯度下降 + 向 W_obs 收缩，
    # 步后投影 + 边界重置。field_guidance=False 时能量退化为纯平滑项（G2 消融臂）。

def complete_graph(W_obs: np.ndarray, mask: np.ndarray, cfg: DiffusionConfig,
                   source: int, target: int) -> np.ndarray
    # 端到端：forward_diffuse(观测场) → reverse_denoise → 返回补全场。
```

权重→散射参数固定映射（写进 docstring，保持物理一致）：`g_couple = 1/max(W[i,j],eps) - 1` 的单调映射、`g_aether=0.1` 常数、`δ=0`；即 W 越大透射越高，单调即可，禁止引入与 v1.4 冲突的新参数。

## 测试 `tests/test_diffusion.py`（必须全绿）

1. 投影：非负、行和=1（1e-12）、零行→均匀。
2. 条件等效 A：n_steps=0 ⇒ complete_graph 恒等（仅投影）。
3. 条件等效 B：前向充分步（β 末段→1）⇒ mask 行收敛到均匀先验（TV<1e-6）。
4. 边界冻结：forward/reverse 任意步，边界元素与 W0 之差 = 0。
5. 无泄漏：scatter_energy 不读取 gold_edges（改 gold_edges 值，输出不变）。
6. smoke：一张合成图上 complete_graph 对金边的 top-3 命中率 > 随机基线。

## 实验 `run_v15_experiment.py` → `results/deposon_v15_diffusion.json`

- 实验 A（合成）：分层 DAG（4 层×6 节点，层间全连接后剪枝到 ~60 边，植入 1 条 source→sink 金路径）。掩码比例 {0.2, 0.4}，每配置 20 张图（seed 0..19）。方法臂：`field_guided`（完整）、`no_guidance`（G2 消融）、`random`、`degree`（度中心性基线）。指标：金边 top-3 命中率、AUC。
- 实验 B（真实脑图）：G1 人工转译脑图（45 节点 49 边，数据在 results/deposon_g1_mindmap_demo.json），留一边预测（每边掩码一次），同样四臂，报 top-3 命中率。
- JSON 含：config、seeds、每臂指标均值/标准差、逐图明细、运行时长。**如实记录，包括负面。**

## 红线
禁止网络/API 调用；禁止把 mock 当真实结果；代码不得含任何 API key；numpy 依赖外不加新包（requirements 不动）。

---

## SPEC v1.5.1 修订（2026-08-23，针对首轮证伪结果）

首轮发现：max-path 能量对掩码边子梯度恒零（死锁），field_active=0/49。修订如下：

1. **能量改为聚合透射率**（v1.4 论文 aggregate T 的直接对应物）：
   `E = -log( Σ_{p: source⇝target} Π_{e∈p} t_e ) + lam_smooth*平滑项`。
   DAG 上用拓扑序 DP：T(v) = Σ_{u→v} T(u)·t(u,v)，T(source)=1。
   这使每条位于任一 s→t 路径上的掩码边都获得非零梯度，消除死锁。
   docstring 注明 "aggregate-T analog of v1.4 §scattering audit"。
2. `scatter_energy` 增加可选参数 `energy_mode: str = "aggregate"`（"aggregate"|"max_path"），
   向后兼容；max_path 保留为对照臂。`DiffusionConfig` 增加 `energy_mode: str = "aggregate"`。
3. 新增测试：在实验 B 的 ≥1 个真实实例上断言 field_active=True（引导臂输出与消融臂不同）；
   死锁回归测试：被掩边在可行 s→t 路径上时，其反向更新量 > 0。
4. 实验四臂扩展为五臂：field_guided(aggregate)、field_guided_maxpath(对照)、no_guidance、random、degree。
   旧结果 JSON 复制归档为 results/deposon_v15_diffusion_maxpath_negativeresult.json（保留负面证据），
   新结果写 results/deposon_v15_diffusion.json，JSON 内注明 energy_mode。
5. 如实报告：若 aggregate 臂仍不优于基线，照样写入结果并在报告中说明。
