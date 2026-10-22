# γ-R1 逐源记录 S3（worker · 2026-09-28）

> 出证方 = **worker**（本棒执行段），不冒充他方。判读口径 = 预登记件 `02c072833cca` §2.2 式 3 + §5 + §7.1，**0 改动**。

## 四件套核对

| # | 件 | 本源状态 |
|---|---|---|
| 1 | 完整书目 | ✅ 见下 |
| 2 | 公开 URL | ✅ `https://arxiv.org/pdf/cond-mat/0512369`（arXiv 全文 PDF，开放获取；抓取时刻 2026-09-28 17:32:29 CST，108,240 B，SHA-12 `a35361b1dccc`） |
| 3 | 页码 / 式号 | ⚠️ 1D TFIM 方程在 **PDF 第 2 页 式 (9)–(12)**；**`K`、`Γ` 定义处：不存在**（全文 0 处 `sinh`/`asinh`/`cosh`/`K =`/`K ≡`/`κ`） |
| 4 | `K`/`Γ` 定义原文逐字摘录 | ❌ **缺**（该文未定义 `K`、`Γ`） |

## 完整书目

- 作者：Gang Xiong（北京师范大学）, X. R. Wang（香港科技大学）
- 年：2006（arXiv:cond-mat/0512369v2 [cond-mat.stat-mech]，2006-02-04；PDF 标注 "Dated: Draft on November 8, 2018"）
- 题名：A direct calculation of critical exponents of two-dimensional anisotropic Ising model
- 载体：arXiv:cond-mat/0512369v2（全文 PDF 开放获取）
- DOI：无（本棒未核，**0 编造**）

## 逐字摘录（PDF 第 2 页，式 (10)–(12)）

> eG(k) = −2 ( h + J cos k + √ h2 + 2J hcos k + J 2 ) . (10) Denote t = h |J| , (11) the excitation gap of ˆH is ∆ E = 2|J||t − 1|. (12) Thus the critical point of the ground-state CPT of the 1D TFIM is at t = tc = 1 where ∆ E vanishes.

## 判读（`r_K`、`r_Γ`）

- 该文对 1D TFIM 用 **Pauli 矩阵 + `J`（纵向）、`h`（横场）**，导出的判据是**零温**的 `t ≡ h/|J| = 1`（`ΔE = 2|J||t−1|`）。
- 该文**未出现** `sinh`/`asinh`/`cosh` 任何字样 ⇒ **未写** `sinh(2K)·sinh(2Γ) = 1` 或其等价 `h_c(T)` 形式；**未定义** `K`、`Γ`。
- 依 §7.1：分子侧缺失 ⇒ **不可判读**；**不得**由 `t_c = 1`（零温极限）反推有限温定义因子。

⇒ `r_K` = **不可判读（null）**；`r_Γ` = **不可判读（null）**。

## 抽取质量如实交代

同页式 (2)（1D TFIM → 2D 经典各向异性 Ising 的极限关系）在 PDF 抽取中**下标与指数被吞**，出现 `Jx kBT ≡ J h e − 2Jy kB T → 0` 一类**不可靠串**。本棒**因此 0 引用该式**，只引用抽取可靠的式 (10)–(12)（**0 凭抽取残串推断**）。

## 级与计数归属

- 级：**非 A 级**（`K-GR1-0-A` 缺第 3、4 件）。
- 三分类归档：**0 命中源**，**0 计入**任何一类。
- 构造面：`n_distinct` 贡献 = 0。
