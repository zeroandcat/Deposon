# Deposon (凝子) 统一场论 -- 算法实现需求文档

> **命名声明**: 中文"凝子"取凝华(Deposition)之义--能量从气态直接凝华为固态,散失于无限维正交以太,不可逆。英文 Deposon = Deposition + -on。
> 
> **版本**: v1.0 Unified Field Theory  
> **日期**: 2026-08-21  
> **状态**: 概念验证完成,待工程实现

---

## 一、核心概念(已实现,不再拓展)

### 1.1 统一命题

v1(阻塞)与 v2(穿越)是同一 Deposon 实体的两种极限态:

| 极限 | 以太耦合 g_aether | 能量分配 | 算法表现 |
|------|------------------|----------|----------|
| **v1(阻塞)** | g_aether = 0 | E_in = E_reflected + E_transmitted | 错误路径本地反射衰减 |
| **v2(穿越)** | g_aether >> 0 | E_in = E_transmitted + E_aether | 错误能量凝华到以太,正确路径无损透射 |
| **一般态** | 0 < g_aether < inf | E_in = E_transmitted + E_reflected + E_aether | 三通道均分,由比值 eta = g_aether/g_couple 决定行为 |

### 1.2 散射方程(Feshbach 共振)

S_eff(E) = S_bg(E) - [S_bg(E) |W><W| S_bg(E)] / [E - E_0 + i*Gamma_aether/2]

- S_bg: 背景散射矩阵(无以太耦合)
- |W>: 光子-Deposon 耦合态
- E_0: 共振能量
- Gamma_aether: 以太诱导线宽

---

## 二、代码需求(Code Requirements)

### 2.1 核心模块: DeposonState

**需求**: 实现 Deposon 单体态,封装散射参数与三通道计算。

**接口规范**:

```python
class DeposonState:
    def __init__(self, id: str, center: np.ndarray, 
                 g_couple: float = 1.0, g_aether: float = 0.0,
                 resonance_energy: float = 0.0)

    @property
    def transmission(self) -> float
        """透射振幅 |t|^2"""

    @property  
    def reflection(self) -> float
        """反射振幅 |r|^2"""

    @property
    def dissipation(self) -> float
        """耗散振幅 |a|^2"""

    def scatter(self, photon_energy: float) -> Dict[str, float]
        """
        统一散射计算
        返回: {
            'transmitted': float,  # |t|^2
            'reflected': float,    # |r|^2  
            'dissipated': float,   # |a|^2
            'amplitudes': {'t': float, 'r': float, 'a': float}
        }
        """
```

**实现约束**:
- 必须处理 g_aether = 0 的除零保护
- 散射结果必须满足幺正性: |t|^2 + |r|^2 + |a|^2 = 1.0(容差 1e-6)
- 共振因子计算: resonance_factor = 1 / (1 + detuning^2)

---

### 2.2 核心模块: EtherChannel

**需求**: 实现无限维正交以太的能量耗散接口。

**接口规范**:

```python
class EtherChannel:
    def __init__(self, capacity: float = float('inf'), 
                 dissipation_rate: float = 1.0)

    def dissipate(self, energy: float) -> float
        """
        将能量散失到以太
        返回实际耗散量(受容量限制)
        累计耗散能量不可回流
        """

    @property
    def energy_dissipated(self) -> float

    @property
    def capacity_remaining(self) -> float
```

**实现约束**:
- capacity=inf 为默认配置,表示无限维以太
- 耗散操作必须原子化(线程安全)
- 不提供 recover() 方法--能量一旦耗散不可逆

---

### 2.3 核心模块: DeposonField

**需求**: 管理 Deposon 态集合,提供统一场计算、共轭映射、路径处理。

**接口规范**:

```python
class DeposonField:
    def __init__(self, feature_dim: int = 64,
                 default_g_couple: float = 1.0,
                 default_g_aether: float = 0.0,
                 ether_capacity: float = float('inf'))

    def spawn(self, deposon_id: str, center: np.ndarray,
              g_couple: Optional[float] = None,
              g_aether: Optional[float] = None,
              resonance_energy: float = 0.0)
        """在认知空间中生成 Deposon 态"""

    def interact(self, photon_feature: np.ndarray, 
                 photon_energy: float,
                 deposon_id: str) -> Dict[str, float]
        """单 Deposon 相互作用,更新能量预算"""

    def process_path(self, path: List[str], 
                     path_energy: float) -> Dict[str, Any]
        """
        处理完整推理路径
        返回: {
            'path': List[str],
            'fate': str,              # 'transmitted' | 'blocked' | 'tunneling'
            'transmitted': float,     # 累计透射能量
            'reflected': float,       # 累计反射能量
            'dissipated': float       # 累计耗散能量
        }
        """

    def find_conjugates(self, node_ids: List[str],
                        max_pairs: Optional[int] = None) -> int
        """
        识别节点共轭对(v2 特性)
        共轭条件: 嵌入距离近 + 能量互补 + 都在"暗区"
        返回识别的共轭对数量
        """

    def set_mode(self, mode: DeposonMode)
        """
        批量设置全场工作模式
        BLOCKING: g_aether=0, g_couple>=2.0
        TUNNELING: g_aether>=2.0, g_couple<=0.2
        GENERAL: 保持当前
        ADAPTIVE: 由外部控制器调节
        """

    def get_budget_report(self) -> Dict[str, float]
        """
        能量预算报告
        返回 transmitted_ratio, reflected_ratio, 
               dissipated_ratio, system_efficiency
        """
```

**实现约束**:
- process_path 必须遍历路径中每个节点与所有 Deposon 的相互作用
- find_conjugates 复杂度 O(|V|^2 * d),需支持大规模图的近似加速
- 能量预算统计必须线程安全

---

### 2.4 集成模块: DeposonEnhancedSystem

**需求**: 将 DeposonField 集成到现有 v3 仿光子推理系统中。

**接口规范**:

```python
class DeposonEnhancedSystem:
    def __init__(self, base_system: PhotonSemiSystem_v3,
                 deposon_field: DeposonField)

    def reason(self, start: str, goal: str, 
               observation: Any, domain: str,
               enable_deposon: bool = True) -> Dict[str, Any]
        """
        带 Deposon 审计的推理

        步骤:
        1. 注入节点特征与能量到 DeposonField
        2. 识别共轭对(若 v2 模式)
        3. 调用基线 PII-BT 生成候选路径
        4. 对每个候选路径调用 DeposonField.process_path()
        5. 根据 fate 调整候选概率:
           - blocked: final_prob *= 0.1
           - tunneling: computation_cost *= 0.5
        6. 重新排序并返回

        返回结果必须包含:
        - 'deposon_budget': 能量预算报告
        - 'n_conjugate_pairs': 共轭对数量
        - 每个候选的 'deposon_fate', 'deposon_transmission', 
          'deposon_reflection', 'deposon_dissipation'
        """
```

---

### 2.5 硬件抽象层(HAL)

**需求**: 将 Deposon 参数映射到半导体器件控制接口。

**接口规范**:

```python
class DeposonHAL:
    """硬件抽象层: Deposon 参数 -> 半导体器件控制"""

    # PCM 控制
    def pcm_set_coupling(pcm_cell, target_g_couple: float)
        """
        通过 SET/RESET 脉冲调节 PCM 晶态比例
        p_target = 1 - exp(-g_couple)
        SET (1.5V, 100ns): 晶化,增大 p
        RESET (3.0V, 10ns): 非晶化,减小 p
        """

    # MZI 控制
    def mzi_set_aether(mzi_array, target_g_aether: float)
        """
        调节 MZI 分束比
        eta = g_aether / (1 + g_aether)
        eta=0: 全反射(v1)
        eta=1: 全透射到以太端口(v2)
        """

    # ECM 控制
    def ecm_set_dissipation(ecm_cell, target_gamma: float)
        """
        通过 ECM 离子迁移调节耗散率
        Gamma_aether = gamma_ECM * psi(t)
        """
```

**实现约束**:
- HAL 为可选模块,软件模拟时可用 stub 实现
- 实际硬件调用需通过 SPI/I2C 接口
- 所有器件操作必须包含超时和错误回退

---

## 三、测试需求(Test Requirements)

### 3.1 单元测试

#### 3.1.1 DeposonState 散射测试

**测试用例集**:

| 用例ID | g_couple | g_aether | 预期行为 | 断言条件 |
|--------|----------|----------|----------|----------|
| DS-001 | 0.0 | 0.0 | 全透射 | transmission==1.0, reflection==0.0, dissipation==0.0 |
| DS-002 | 5.0 | 0.0 | 强反射(v1极限) | reflection > 0.8, transmission < 0.2, dissipation==0.0 |
| DS-003 | 0.1 | 5.0 | 强透射+耗散(v2极限) | transmission > 0.8, dissipation > 0.0, reflection < 0.1 |
| DS-004 | 1.0 | 1.0 | 三通道均分 | 各通道 in [0.25, 0.5] |
| DS-005 | 1.0 | 0.0 | 共振效应 | detuning=0时 reflection最大,detuning->inf时 transmission->1.0 |
| DS-006 | 任意 | 任意 | 幺正性守恒 | transmission^2 + reflection^2 + dissipation^2 == 1.0 +/- 1e-6 |

#### 3.1.2 EtherChannel 耗散测试

| 用例ID | 操作 | 预期行为 |
|--------|------|----------|
| EC-001 | dissipate(10.0) on inf capacity | 返回 10.0, energy_dissipated == 10.0 |
| EC-002 | dissipate(10.0) on capacity=5.0 | 返回 5.0, energy_dissipated == 5.0 |
| EC-003 | 多线程并发 dissipate | 最终 energy_dissipated 等于各线程返回值之和 |
| EC-004 | capacity=0 | 返回 0.0, 所有耗散被拒绝 |

#### 3.1.3 DeposonField 路径处理测试

| 用例ID | 路径 | Deposon配置 | 预期 fate | 断言 |
|--------|------|-------------|-----------|------|
| DF-001 | ['A','B','C'] | g_aether=0, g_couple=5 | blocked | dissipated==0, reflected>0.5 |
| DF-002 | ['A','B','C'] | g_aether=5, g_couple=0.1 | tunneling | dissipated>0.5 |
| DF-003 | ['A','B','C'] | g_aether=0, g_couple=0 | transmitted | transmitted>0.9 |
| DF-004 | 空路径 | 任意 | transmitted | 无异常 |

---

### 3.2 集成测试

#### 3.2.1 DeposonEnhancedSystem 端到端测试

**测试场景**:

```
场景 E2E-001: GSM8K 数学推理
- 输入: 小学数学应用题
- Deposon 配置: v1 模式(g_aether=0, g_couple=2.0)
- 预期: 错误计算路径被阻塞,最终答案准确率 > 基线
- 指标: path_accuracy, n_blocked, avg_reflection_ratio

场景 E2E-002: StrategyQA 策略推理  
- 输入: 需要多步推理的是/否问题
- Deposon 配置: v2 模式(g_aether=3.0, g_couple=0.2)
- 预期: 探索更多候选路径,共轭边加速推理
- 指标: search_efficiency, n_conjugate_pairs_used, latency_reduction

场景 E2E-003: HumanEval 代码生成
- 输入: 函数签名 + 文档字符串
- Deposon 配置: 自适应模式(负载感知)
- 预期: 高负载时阻塞语法错误路径,低负载时允许探索
- 指标: compilation_rate, pass@k, energy_budget_efficiency

场景 E2E-004: Long Context 长文本理解
- 输入: 10万字文档 + 复杂查询
- Deposon 配置: v2 + Kimi 长文本
- 预期: 全局 Deposon 场计算,跨文档共轭对识别
- 指标: recall, F1, memory_usage, inference_time
```

#### 3.2.2 消融测试(六变体对比)

| 变体 | g_couple | g_aether | 模式 | 必须测量的指标 |
|------|----------|----------|------|----------------|
| Baseline | 0 | 0 | 无 Deposon | path_accuracy, latency, memory |
| v1-Pure | 5.0 | 0 | BLOCKING | precision, recall, n_pruned |
| v2-Pure | 0.1 | 5.0 | TUNNELING | n_explored, conjugate_hits, speedup |
| Balanced | 1.0 | 1.0 | GENERAL | 三通道比例, 综合 F1 |
| Adaptive | 动态 | 动态 | ADAPTIVE | 负载-模式对应关系, 收敛速度 |
| Deposon-Full | 自适应 | 自适应 | 全局优化 | 所有上述指标 + 能耗效率 |

**统计要求**: 每个变体在至少 3 个基准上各运行 100 次,报告均值 +/- 标准差。

---

### 3.3 性能测试

#### 3.3.1 复杂度基准

| 测试项 | 输入规模 | 预期复杂度 | 可接受 slowdown |
|--------|----------|-----------|-----------------|
| DeposonState.scatter | 单次调用 | O(1) | < 1us |
| DeposonField.process_path | 路径长度 D=10, Deposon数 N=5 | O(D*N) | < 0.1ms |
| DeposonField.find_conjugates | 节点数 |V|=1000 | O(|V|^2*d) | < 5s |
| DeposonField.find_conjugates | 节点数 |V|=10000 | 需近似加速 | < 30s |
| DeposonEnhancedSystem.reason | 标准推理任务 | 基线 + 20% | < 1.2x baseline latency |

#### 3.3.2 并发测试

- 100 个并发推理请求共享同一 DeposonField
- 预期: 能量预算统计正确,无竞态条件
- 工具: ThreadSanitizer / Python threading stress test

---

### 3.4 硬件在环测试(HIL)

**前提**: HAL 模块已实现且硬件可用。

| 测试项 | 器件 | 操作 | 验证点 |
|--------|------|------|--------|
| HIL-001 | PCM | SET/RESET 循环 10^6 次 | g_couple 单调性与耐久性 |
| HIL-002 | MZI | 分束比扫描 0->1 | g_aether 线性度 |
| HIL-003 | ECM | 脉冲序列写入 | Gamma_aether 保持性 |
| HIL-004 | 全系统 | 端到端推理 | 软件模拟 vs 硬件加速一致性 |

---

## 四、诚实边界(Honesty Boundaries)

### 4.1 理论局限(不可消除)

1. **无限维近似**: 以太的理论无限维在数值中必须截断。"不可逆"是渐进性质,非绝对。
2. **参数无通用理论**: 最优 (g_couple, g_aether) 依赖任务,无闭式解。
3. **能量隐喻未验证**: "认知能量"与物理能量的对应关系仅为启发式类比。

### 4.2 工程局限(可缓解)

1. **O(|V|^2) 共轭识别**: 大规模图需近似算法(LSH、随机投影)。
2. **硬件未流片**: PCM/MZI/ECM 映射为概念设计,需 tape-out 验证。
3. **命名传播成本**: "Deposon"为新造词,学术接受度未知。

### 4.3 测试局限(必须声明)

1. 当前无真实 Deposon 芯片,所有硬件测试为软件模拟。
2. 基准测试数据集可能存在分布偏移,结果外推需谨慎。
3. 长期稳定性测试(>1 年)尚未进行。

---

## 五、文件清单

| 文件 | 说明 |
|------|------|
| Deposon_凝子_统一场论研究报告_v1.pdf | 完整研究报告(含图表) |
| deposon_unified_space.png | 统一参数空间热图 |
| deposon_physics_analogy.png | 凝华物理类比示意图 |
| deposon_hardware_mapping.png | 三层硬件映射图 |
| Deposon_Requirements_v1.md | 本文档(代码与测试需求) |

---

*文档结束。如需工程实现,请基于本文档的接口规范开发,并参照测试需求进行验证。*
