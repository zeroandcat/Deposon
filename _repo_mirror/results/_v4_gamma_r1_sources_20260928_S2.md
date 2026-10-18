# γ-R1 逐源记录 S2（worker · 2026-09-28）

> 出证方 = **worker**（本棒执行段），不冒充他方。判读口径 = 预登记件 `02c072833cca` §2.2 式 3 + §5 + §7.1，**0 改动**。

## 四件套核对

| # | 件 | 本源状态 |
|---|---|---|
| 1 | 完整书目 | ✅ 见下 |
| 2 | 公开 URL | ✅ `https://arxiv.org/pdf/0808.1816`（arXiv 全文 PDF，开放获取；抓取时刻 2026-09-28 17:31:49 CST，142,817 B，SHA-12 `e377d6ef2afe`） |
| 3 | 页码 / 式号 | ⚠️ 该文哈密顿量在 **PDF 第 2 页 式 (5)**；**`K`、`Γ` 定义处：不存在**（全文 0 处 `sinh`/`asinh`/`cosh`/`K =`/`K ≡`/`κ`） |
| 4 | `K`/`Γ` 定义原文逐字摘录 | ❌ **缺**（该文未定义 `K`、`Γ`） |

## 完整书目

- 作者：Jian Ma, Lei Xu, Xiaoguang Wang（Zhejiang Institute of Modern Physics）
- 年：2008（arXiv:0808.1816v1 [quant-ph]，2008-08-13）
- 题名：Reduced fidelity susceptibility in the one-dimensional transverse field Ising model
- 载体：arXiv:0808.1816v1（全文 PDF 开放获取）
- DOI：无（本棒未核，**0 编造**）

## 逐字摘录（该文自身哈密顿量与临界点，PDF 第 2 页）

> The Hamiltonian of the 1D TFIM reads HI = − M∑ j=−M [ λσx j σx j+1 + σz j ] , (5) where σα j (α = x, y, z) is a Pauli matrix at site j, λ is the Ising coupling constant in units of the transverse ﬁeld, and periodic boundary conditions ( σ−M = σM ) are as- sumed.

> …As is well known, there is a critical point exactly at λc = 1 in the thermodynamic limit.

> 抽取说明：`ﬁeld`/`as- sumed` 为 PDF 文本抽取产生的连字与断词，**0 回改**（逐字原则）。

## 判读（`r_K`、`r_Γ`）

- 该文把模型写成**单一无量纲参数** `λ`（`λ ≡ c_trans / c_ferro`，横场以耦合为单位）：`H_I = -M Σ_j [ λ σ^x_j σ^x_{j+1} + σ^z_j ]`，其中纵向耦合系数 `c_ferro = M`、横场系数 `c_trans = M·λ`（按该文写法）。
- 但该文**只写零温临界比 `λ_c = 1`**，**未写** `sinh(2K)·sinh(2Γ) = 1` 或任何有限温 `h_c(T)` 形式，**亦未定义** `K`、`Γ`。
- 依 §7.1「两侧必须各自来自同一条文献的原文」：分子侧（`K_lit`、`Γ_lit` 定义式）**缺失** ⇒ **不可判读**；**不得**用零温 `λ_c = 1` 反推有限温因子（§7.1 明文 0 允许从方程形式反推）。

⇒ `r_K` = **不可判读（null）**；`r_Γ` = **不可判读（null）**。

## 级与计数归属

- 级：**非 A 级**（`K-GR1-0-A` 缺第 3、4 件）。
- 三分类归档：**0 命中源**，**0 计入**任何一类。
- 构造面：`n_distinct` 贡献 = 0。
