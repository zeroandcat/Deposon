# γ-R1 逐源记录 S1（worker · 2026-09-28）

> 出证方 = **worker**（本棒执行段），不冒充 protocol-keeper / verdict-keeper / evidence-auditor / PI / 任一受托方。
> 判读口径 = 预登记件 `_v4_gamma_r1_prereg_2026_09_28.md`（`02c072833cca`）§2.2 式 3 + §5 四件套 + §7.1 判读式，**0 改动**。

## 四件套核对

| # | 件 | 本源状态 |
|---|---|---|
| 1 | 完整书目 | ✅ 见下 |
| 2 | 公开 URL | ✅ `https://arxiv.org/pdf/2207.09547`（arXiv 全文 PDF，开放获取；抓取时刻 2026-09-28 17:31:43 CST，1,168,885 B，SHA-12 `eca05c215a3c`） |
| 3 | 页码 / 式号 | ⚠️ **仅对「该文写了什么」可给**（PDF 第 2–3 页，式 (1)–(4)）；**对 `K`、`Γ` 的定义：不存在**（全文 0 处 `sinh`/`asinh`/`cosh`/`K =`/`K ≡`/`κ`） |
| 4 | `K`/`Γ` 定义原文逐字摘录 | ❌ **缺**（该文未定义 `K`、`Γ`，故无可摘录之定义处） |

## 完整书目

- 作者：Hui Yu, Sudip Chakravarty
- 年：2022（arXiv v1 2022-07-19；PDF 标注 "Dated: July 21, 2022"）
- 题名：Quantum critical points, lines and surfaces
- 载体：arXiv:2207.09547v1 [cond-mat.str-el]（全文 PDF 开放获取）
- DOI：无（本棒未核，**0 编造**；arXiv 记录未在已抓数据中给出 DOI 字段）

## 逐字摘录（该文自身模型写法，PDF 第 2 页）

> The Hamiltonian, H, is H =− ∑ i (hiσx i +λ2σx iσz i−1σz i+1 +λ1σz iσz i−1) (1) written in terms of standard Pauli matrices. In this section we discuss its phase diagram. We shall set hi =h =cst.

逐字摘录（该文「critical line」所指，PDF 第 3 页）：

> For the Ising model in a transverse ﬁeld without three spin interaction, the gaps collapse at the Bril- louin zone boundaries, k = ±π at the self-dual point λ1 = 1 and λ2 = 0.

> 抽取说明：上段 `ﬁ`/`Bril- louin` 为 PDF 文本抽取产生的连字与断词，**0 回改**（逐字原则）。

## 判读（`r_K`、`r_Γ`）

- 分子 `K_lit` / `Γ_lit`：**该文未定义** ⇒ 分子侧缺失。
- 分母 `c_ferro` / `c_trans`：该文哈密顿量为 3 自旋扩展 TFIM（纵向耦合 `λ1`、横场 `h_i`、三自旋 `λ2`），自旋为 Pauli 矩阵；即便强行以 `λ1`、`h` 代 `K_lit`、`Γ_lit`，**该文亦未写出 `sinh(2K)·sinh(2Γ) = 1` 或其等价 `h_c(T)` 形式**。
- 该文 critical line 位于 `(λ1, λ2)` 参数面（三自旋模型），**不是** §6.1 构造域所指「1D 精确临界方程 `sinh(2K)·sinh(2Γ) = 1` 所在处」。

⇒ `r_K` = **不可判读（null）**；`r_Γ` = **不可判读（null）**。

## 级与计数归属

- 级：**非 A 级**（`K-GR1-0-A`：缺第 3、4 件 ⇒ 0 计入 A 级合格源）。
- 三分类归档：**0 命中源**（该文在预登记构造域上无定义因子可读数），**0 计入**「一半 / 本身 / 不可判读」三类中的任何一类计数。
- 构造面：`n_distinct` 贡献 = 0。
