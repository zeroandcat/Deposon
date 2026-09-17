# P-E 火山引擎 doubao-embedding-vision 集成 V0 规范(草稿)

> **状态**: 草稿(2026-09-08,待用户确认后冻结)
> **作者**: Mavis(继任 orchestrator)
> **方向定位**: "其他可能潜力方向"——将 deposon 向量属性(守恒/单调性/可分性)发挥到 LLM 推理路径中,通过火山引擎 `doubao-embedding-vision` 引入 multi-vector 嵌入(2026 新模型,支持视频输入与压缩传输)
> **强度声明前置**: 沿用三档纪律——**判死**(已预登记并执行)、**观察性**(数值规律)、**探索性**(猜想)

---

## 0. 背景与定位

王老师 WeChat 2026-09-08 回复"无指示",开放 V3.X 5 候选自由探索(博弈论转向 / 原脑图 / 其他潜力方向)。用户定义"其他可能潜力方向"包括 LLM 议价与 deposon 向量属性发挥。

V3.X 原 4 方向(P-A / P-B / P-C / P-D)中 P-D 已接近收尾(代码 PASS,仅 A1 CLI 衔接 P1 待修),P-A/P-B/P-C 是博弈论转向,本提案不重复。

**P-E 的具体落点**: 在不重写 V3.X 主线工程的前提下,沿**已冻结的 deposon 向量属性**(T+R+A=1 守恒 / 散射层)路径,集成 `doubao-embedding-vision` 提供的 multi-vector 嵌入层,实证检验 3 项预登记猜想是否在嵌入空间成立。**不**与 P-D 冲突(指纹协议在更上层,本方向在嵌入层)。

### 与王老师工作的挂点

- 王老师近期议程"机制设计 × 信息设计"对应"玩家向机制证明什么"
- P-D 是"披露承诺装置",P-E 是"披露的内容(向量表示)是否在嵌入空间守恒"
- 两者互补:P-E 回答"向量属性跨嵌入维度是否保持",P-D 回答"声明是否可独立验证"

### 我方已有可复用资产

- 守恒审计: T+R+A=1 逐路径通过(2.2×10⁻¹⁶ 残差,v19 冻结基准 200 道题)
- 散射层: 三通道(transmission / reflection / dissipation)结构
- 数据集: GSM8K 0.87 / StrategyQA 0.899 / physics 0.484 等关键数字溯源到冻结 JSON
- 工程: `fingerprint_v0.py` 已通过 11/11 测试 + 3/3 攻击(Trae 已优化版)

### 引入模型

- **doubao-embedding-vision**: 火山引擎 2026 年新模型
- 关键特性: multi-vector 输出 + 压缩传输 + 视频输入(本研究只用文本/图节点,视频特性留接口)
- **API 沿用之前 KIMI/GLM 鉴权流程,只换模型 ID**
- **API key 路径**: `C:/Users/Administrator/Desktop/AI/新建文本文档.txt`
- **7 条铁律**: runtime `Path().read_text()` 读取,**永不落盘/永不进 prompt/永不写入检测规则**
- spec 阶段不读 key,实现 step 才读

---

## 0.5 已知陷阱(避免 P-D P1 复现)

> **强制节**: 任何 V0 spec 必须显式标出"已知陷阱+本次如何避开",避免复现历史阻断项。

### 历史 bug 列表(必读)

| bug | 来源 | 后果 | 修复 |
|---|---|---|---|
| **P-D V0.1.1 P1** | reviewer-a 报告(2026-09-04): A1 攻击脚本 CLI 模式与 spec §6 判死命令衔接缺口 | 照 spec L182 命令字面执行(`--missing docs/SPEC_GT8C.md`),A1 不删除该路径 → `compute_root` 正常返回 → verdict=FAIL → "任一 FAIL → V0 死、直接归档"误杀 V0 | Trae V0.1.2 改"无参 + 临时副本自建"(`tempfile.TemporaryDirectory` 内自建 5 锚 + 自删第 3 个 + 副本外绝不删除) |
| **P-D V0.1.1 P1 衍生风险** | 上述 A1 CLI 分支会诱导操作者在真实仓库对冻结锚 `docs/SPEC_GT8C.md` 执行 `rm` | 一旦误操作,冻结锚永久损坏,后续 5 锚 SHA-256 全部失效 | Trae V0.1.2 删除 `--missing` 分支,改为完全无参 + 全 tmpdir 隔离 |
| **P-D V0.1.1 P2: E_GENESIS_PREV_HASH 未落地** | 错误码 spec §5 列出但实现未输出 | 不影响判死但阻碍审计可读性 | V0.1.x 顺手收敛(本方向 P-E 不重蹈,所有错误码 spec 列出的必须实现输出) |

### 本次 P-E 设计如何避开

1. **攻击脚本无参直跑**: §6 三个攻击脚本全部"无参 + 临时副本自建"(`tempfile.TemporaryDirectory` 内自建工件 + 自攻击),与 V0.1.2 同款约定。**禁止**沿用 P-D V0.1.1 的 `--missing <path>` 类带参 CLI 模式。
2. **真实仓库绝对零接触**: 攻击脚本 + 实现都不在真实仓库 `d:/私人资料/deposon-repo` 下运行,全部在 `C:\Users\Administrator\AppData\Local\Temp\deposon-e-audit-<ts>\` 副本内执行。**禁止** `python attacks/X.py` 沿仓库根直跑(会触碰冻结锚)。
3. **不诱导锚删除**: §6 三个攻击脚本设计时**禁止**任何"接收路径 + 删除该路径"类 CLI 形态。若必须传路径,只能传"在 tmpdir 副本内自建的工件路径",且副本结束自动清理。
4. **错误码 spec/implementation 一致**: §5 列出的 5 个错误码必须实现完整输出(包括 `E_KEY_LEAK`),不允许 spec 列了但实现不抛。
5. **key 安全**沿用 P-D R5 思路: API 调用走 runtime `Path().read_text()`,源码无 key 字面量,无 `kimi/ark/sk-/AKIA/长 hex` 串。E5 边界扫描仿 P-D R5 静态审计。

### 禁止条款(实现 step 不得违反)

- ❌ 沿用 P-D V0.1.1 命令模板字面(`python -m attacks.X` 或 `python attacks/X.py --missing <path>`)
- ❌ 在真实仓库 `d:/私人资料/deposon-repo` 下运行任何攻击脚本
- ❌ 让 CLI 接收指向冻结锚(P-D §1 5 锚或 P-E §8 数据集)的路径并对其执行任何修改
- ❌ 源码 / 提示词 / 检测规则 含 key 字面量或可被 grep 命中的密钥片段
- ❌ spec §5 列出的错误码未在实现中输出

---

## 1. 目标与范围

### V0 包含

- **E1** = 嵌入一致性:同节点文本 → 同 multi-vector(确定性)
- **E2** = 守恒跨维: 散射层 T+R+A=1 在 multi-vector 空间是否成立(嵌入前后残差对比)
- **E3** = 散射通道可分: transmission / reflection / dissipation 三通道向量在嵌入空间是否线性可分
- **E4** = 路径追踪: 多步推理路径的向量序列可重放(同输入同路径序列)
- **E5** = 边界: API 调用安全边界(不泄漏锚点路径,种子可重放,rate-limit 友好)

### V0 不包含

- 任何对指纹协议(P-D)的修改
- 任何对散射层实现的修改
- 视频输入模式(只做文本+图节点)
- 多语言(只中文+英文双语 deposon 节点)
- 模型蒸馏/微调(只调 API,不改模型)

---

## 2. 五项需求

### E1 嵌入一致性

- **输入**: 单个 deposon 节点文本(中英双语,≤512 字符)
- **输出**: `doubao-embedding-vision` 返回的 multi-vector(定长张量,具体维度由 API 决定)
- **不变量**:
  - 同文本同 seed → 相同 multi-vector
  - 任意单字改动 → 完全不同 multi-vector(L2 距离 > 阈值,待定)
- **判死**: 重复 N=20 次同文本输入,若任一次 L∞ 距离 > 1e-6(数值误差),则一致性死

### E2 守恒跨维

- **输入**: deposon 散射层 5 锚 manifest(沿用 P-D 的 5 锚工件)+ 5 锚各自的 multi-vector
- **输出**: 守恒律 T+R+A=1 在向量空间的复算结果(每个向量的标量分量加和)
- **不变量**:
  - 同散射通道 / 同参数 / 同路径下,向量空间守恒残差 ≤ 原散射空间残差 × 1.5(放大容忍因子,因嵌入引入量化)
  - 路径级别残差与原版 2.2×10⁻¹⁶ 的相对偏差 < 0.5
- **判死**: 200 道合成题(沿用 v19 冻结基准)逐路径检查,若守恒残差 > 3.3×10⁻¹⁶(1.5×)的路径占比 ≥ 5%,则守恒跨维死

### E3 散射通道可分

- **输入**: N=200 道题的三通道向量(transmission T / reflection R / dissipation A)
- **输出**: 三通道在嵌入空间的线性可分性(SVM / logistic / cosine 三个度量至少 2 个 ≥ 0.85 AUC)
- **不变量**:
  - 跨数据集(GSM8K / StrategyQA / physics)三通道分离度一致
  - 任何数据子集的 channel entropy 不低于 0.7(无通道塌缩)
- **判死**: 若三通道在嵌入空间完全不可分(任一度量 AUC < 0.55),则散射层嵌入等价于无结构(直接落回"非嵌入退化版"对照),可分性死

### E4 路径追踪

- **输入**: deposon 散射层 N=100 条推理路径(每条 ≤ 20 步),已冻结输出
- **输出**: 路径向量序列 {v_1, v_2, ..., v_k} 可重放(同 seed / 同温度 / 同 prompt → 同序列)
- **不变量**:
  - 同输入同 seed 跑 5 次,前 5 步 L2 距离 < 1e-3
  - 任一步骤顺序改变(节点重排)→ 序列不同(嵌入感知顺序)
- **判死**: 若 L2 距离 > 0.01(数值不稳定)占比 ≥ 10%,则路径追踪死(模型非确定性过强,无工程价值)

### E5 API 边界

- **暴露**: 5 个公开 API(E1 embed_node / E2 check_conservation / E3 check_separability / E4 track_path / E5 rate_limit_safety)
- **不暴露**:
  - 任何 API key / 鉴权信息(7 条铁律)
  - 任何 P-D 锚点路径(避免通过 P-E 调用推回 P-D 工件)
  - 任何 rate-limit 内部状态(给调用方 1 个 bool 而非状态)
- **不变量**:
  - 公开 API 调用者无法通过返回值推断 API key / 锚点路径 / 内部 rate-limit 计数
  - 全部调用走运行时 `Path().read_text()` 读 key,源码无 key 字面量
- **判死**: 静态扫描 P-E 实现 + 攻击脚本,若发现任何 `sk-` / 长 hex(≥20 位)/ `kimi` / `ark` / `AKIA` / 真实 API key 片段,边界死(直接归档)

---

## 3. 数据结构伪代码

```python
# E1
def embed_node(text: str, seed: int = 0) -> np.ndarray:
    """multi-vector embedding via doubao-embedding-vision API.
    Returns: shape (D, V) where D = num_vectors (multi-vector), V = vec_dim.
    Determinism: same (text, seed) -> same array.
    """
    # API call to doubao-embedding-vision with seed
    # No key in source; runtime Path().read_text() at call time only
    ...

# E2
def check_conservation(
    anchor_paths: list[str],  # P-D 5 锚路径(只读,不改)
    embeddings: dict[str, np.ndarray],  # path -> multi-vector
    tol_rel: float = 1.5,  # 放大因子
) -> dict:
    """Return per-path (T, R, A) in vector space, residual relative to v19 baseline."""
    ...

# E3
def check_separability(
    channel_vectors: dict[str, np.ndarray],  # {T, R, A} -> stacked matrix
) -> dict:
    """AUC for T vs (R+A), R vs (T+A), A vs (T+R) under SVM / logistic / cosine."""
    ...

# E4
def track_path(
    reasoning_steps: list[str],  # deposon 散射层输出
    seed: int = 0,
) -> np.ndarray:
    """Return shape (num_steps, D, V) vector sequence."""
    ...

# E5
def rate_limit_safety() -> bool:
    """Return True if safe to call API; opaque to caller."""
    ...
```

> **V0 注记**: E2 接收 P-D 5 锚路径作为"种子集",但**只读不改**(避免影响 P-D 锚完整性);E5 边界模仿 P-D R5 验证器安全边界设计。

---

## 4. 三类攻击 → 检测信号映射

| 攻击 | 输入 | 触发 | 预期输出 |
|---|---|---|---|
| **A1 嵌入非确定性** | 同 (text, seed) 重复调 E1 嵌入 | N=20 次 | L∞ 距离 ≤ 1e-6,否则 `verdict=FAIL` |
| **A2 守恒跨维放大** | E2 跑 200 道 v19 冻结题 | 守恒残差 > 3.3×10⁻¹⁶(1.5×放大)路径占比 ≥ 5% | `verdict=FAIL`,守恒跨维死 |
| **A3 通道塌缩** | E3 跑 200 道题,3 度量 SVM/logistic/cosine | 任一度量 AUC < 0.55 | `verdict=FAIL`,可分性死 |

> **V0 注记**: A1/A2/A3 全部**无参直跑**(`python attacks/a1_embedding_determinism.py` 等),沿用 P-D 攻击脚本的"无参 + 临时副本自建"约定,绝不触碰真实仓库冻结工件。

---

## 5. 实现接口签名(供 P-E-data 实现)

```python
def embed_node(text: str, seed: int = 0) -> np.ndarray  # shape (D, V)
def check_conservation(
    anchor_paths: list[str], embeddings: dict[str, np.ndarray]
) -> dict  # {"per_path": [(T, R, A, residual), ...], "max_residual": float, "fail_ratio": float}
def check_separability(channel_vectors: dict[str, np.ndarray]) -> dict  # {"svm_auc": float, "logistic_auc": float, "cosine_auc": float}
def track_path(reasoning_steps: list[str], seed: int = 0) -> np.ndarray  # shape (num_steps, D, V)
def rate_limit_safety() -> bool
```

- **错误码(V0 完整列表)**:
  - `E_EMBEDDING_API_ERROR`(API 调用失败,超时,4xx/5xx)
  - `E_CONSERVATION_DRIFT`(A2 守恒跨维失效)
  - `E_CHANNEL_COLLAPSE`(A3 通道不可分)
  - `E_PATH_DETERMINISM`(A4 路径非确定性)
  - `E_KEY_LEAK`(E5 边界违反,扫描发现密钥片段)

---

## 6. 判死线(机械命令模板)

V0 判死线 = **表达力线**(性能差异,不在 V0 范围)。

**3 个攻击脚本**(P-E-data 实现,P-E-reviewer-b 执行):

1. `python attacks/a1_embedding_determinism.py`
2. `python attacks/a2_conservation_drift.py`
3. `python attacks/a3_channel_collapse.py`

**执行前置**(reviewer-b 必跑):

```powershell
# Windows PowerShell (Win32 long path 兼容)
$ts = [DateTimeOffset]::UtcNow.ToUnixTimeSeconds()
$dst = Join-Path $env:TEMP "deposon-e-audit-$ts"
Copy-Item -Path "D:/私人资料/deposon-repo" -Destination $dst -Recurse -Force
Push-Location $dst
python attacks/a1_embedding_determinism.py
python attacks/a2_conservation_drift.py
python attacks/a3_channel_collapse.py
Pop-Location
```

**每脚本输出**(stdout JSON):

```json
{"attack": "A1|A2|A3", "verdict": "PASS|FAIL", "diff": "<定位>"}
```

**判死规则**:

- 3/3 脚本 verdict=PASS → V0 表达力存活
- 任一 verdict=FAIL → V0 死,**直接归档**为"deposon + embedding 无显著增量"否定结论,不回溯

**额外判死**(baseline 对比,**实验 step 跑**):

- 在 100-200 节点数据集上,A 组(`doubao-embedding-vision` + deposon)与 B 组(常规 LLM 无 embedding 嵌入层)在关键任务上
  - **无显著差异** → FAIL(deposon + embedding 不带来增益,回退到"向量属性原散射空间")
  - **显著差异**(+5pp 以上,Mann-Whitney p<0.05)→ PASS
- baseline 复用之前 deposon 与 LLM 整合已有数据(GSM8K 0.87 / StrategyQA 0.899 / physics 0.484)

---

## 7. 接口预留位(V0 不实接)

V0 仅保留以下占位常量与错误码,不引入任何外部对接(除 doubao-embedding-vision API):

```python
# 占位常量,V0 不消费
P_D_FINGERPRINT_INTERFACE = None  # P-D 完整性接口位(只读不接)
P_A_EQUILIBRIUM_INTERFACE = None  # P-A 接口位(只读不接)
```

任何试图在 V0 范围外调用此占位的实现,判为越界,与 V0 表达力判定正交。

---

## 8. 数据集与实验设计

### 8.1 数据集规模(用户授权"看着来")

- **起步**: 100-200 节点(沿用 v19 冻结图族子集,seed=210021)
- **中期**: 1k 节点(看初步结果决定)
- **不上**: 10k 节点(1 周内跑不完,无判死线价值)

### 8.2 Baseline 对比设计

- **A 组**: `doubao-embedding-vision` + deposon(向量层嵌入)
- **B 组**: 常规 LLM(直接推理,无 embedding 嵌入层,沿用之前 GSM8K/StrategyQA/physics 配置)
- **不**做"无 embedding 退化版"对照(意义不大,embedding 是核心)
- baseline 数据复用之前 deposon 与 LLM 整合的已有数据(无需重新跑)

### 8.3 关键风险与预案

- **风险 1**: `doubao-embedding-vision` 是 2026 新模型,可能存在 quota 限制或 API endpoint 不稳
  - **预案**: 准备 fallback 走通用 embedding 路线(`text-embedding-3-large` 或同类)
- **风险 2**: multi-vector 输出的具体维度与格式未实测确认
  - **预案**: step 2 第一个动作是"实测 1 次 API 调用确认输出格式",再定数据结构
- **风险 3**: 嵌入引入额外延迟,可能影响 1 周判死节奏
  - **预案**: 1k 节点实验前,先跑 50 节点速度测试,>1s/节点 改用 batch 调用

---

## 9. 任务拆分(5 步,1 周判死)

| step | 动作 | 输出 | 钥匙 |
|---|---|---|---|
| 1 | 选 1 方向 + 写本 spec V0(本文件) | `P_E_DOUBAN_EMBEDDING_V0_SPEC.md` | **不读** |
| 2 | 实现 + 单元测试(实测 1 次 API 确认输出格式 → 写 E1-E5) | `pe_*.py` + `tests/test_pe_*.py` | **读**(按 7 条铁律) |
| 3 | 派独立子代理双审(reviewer-a 静态 + reviewer-b /tmp 重跑) | 两份独立审查报告 | 不用 |
| 4 | 跑小规模实验(100-200 节点) | 性能对比报告 + 3/3 攻击脚本结果 | **读** |
| 5 | 决策 PASS/FAIL → 给王老师等回 | 判死报告 | 不用 |

---

## 10. 关键约束(沿用 V3.X 铁律)

1. **V3.X 5 候选 P-A/B/C/D + LLM 议价都是合法候选,不刻意避开** —— P-E 是"其他潜力方向"的子项,不替代 P-A/B/C/D
2. **王老师 = WeChat 顾问,等他回** —— 本方向独立推进,不给王老师主动推
3. **1 周判死模式** —— 任一攻击 FAIL 即归档,不回溯
4. **数字溯源公理** —— 所有数值引用自冻结 JSON 字段路径(spec §1 锁定的 5 锚 SHA-256[0:12] 即用)
5. **钥匙安全** —— runtime `Path().read_text()` 读取,**永不落盘/永不进 prompt/永不写入检测规则**
6. **预登记先于运行** —— 本 spec 已预登记 E1-E5 + A1-A3 + 判死线,实现 step 不得改判死标准
7. **推送策略** —— P-E 实现 + 数据不放 GitHub(沿用论文不推的纪律),只推 spec + 报告

---

锚点 SHA-256[0:12] 沿用 P-D §1 5 锚(不变)。判死线以 §6 表达力线为唯一依据。E1-E5 各自独立可测。

**草稿结束,待用户确认后冻结 V0 正式版。**
