# γ-R1 逐源记录 S4（worker · 2026-09-28）

> 出证方 = **worker**（本棒执行段），不冒充他方。判读口径 = 预登记件 `02c072833cca` §2.2 式 3 + §5 + §7.1 + §7.3 别名表，**0 改动**。

## 四件套核对

| # | 件 | 本源状态 |
|---|---|---|
| 1 | 完整书目 | ✅ 见下 |
| 2 | 公开 URL | ✅ `https://arxiv.org/pdf/1910.12538`（arXiv 全文 PDF，开放获取；抓取时刻 2026-09-28 17:33:43 CST，410,040 B，SHA-12 `b622cd5c853c`） |
| 3 | 页码 / 式号 | ⚠️ 1D TFIM 哈密顿量在 **PDF 第 3 页 式 (10)**；**`K`、`Γ`（无量纲横场）定义处：不存在**（全文 0 处 `sinh`/`asinh`/`cosh`/`K =`/`K ≡`/`κ`） |
| 4 | `K`/`Γ` 定义原文逐字摘录 | ❌ **缺**（该文未定义无量纲 `K`、`Γ`） |

## 完整书目

- 作者：Long Zhang（中国科学院大学理论物理研究所）, Chengxiang Ding（安徽工业大学）
- 年：2023（arXiv:1910.12538v2 [cond-mat.str-el]，2023-01-09）
- 题名：Finite-Size Scaling Theory at a Self-Dual Quantum Critical Point
- 载体：arXiv:1910.12538v2（全文 PDF 开放获取）
- DOI：无（本棒未核，**0 编造**）

## 逐字摘录 1（PDF 第 3 页，式 (10)）

> The 1DTFIM can be exactly solved with the Jordan- Wigner transformation [11, 12],σz i =∏ l<i (2c† lcl−1)(ci−c† i) and σx i = 2c† ici− 1, in which ci and c† i are fermion operators. The Hamiltonian is mapped to free fermions, H(g) =− ∑ i (ci−c† i)(c† i+1+ci+1)−g ∑ i (2c† ici− 1). (10)

## 逐字摘录 2（PDF 第 2 页，自对偶临界点）

> The Hamiltonian H(g) is mapped into gH(1/g), thus the QCP at gc = 1 is self-dual.

## 逐字摘录 3（PDF 第 1 页，式 (1)）—— **`Γ` 假阳性防误挂留痕**

> The GR can be gen- eralized by replacing p and V with a pair of conjugate variables, i.e., a generalized force (a tuning parameter of the Hamiltonian) g and the generalized displacement vg = (∂f/∂g )T , Γ(T,g ) = ∂Tvg(T,g ) ∂Tϵ(T,g ) . (1)

> **该处 `Γ` 是广义 Grüneisen 比（thermodynamic 量），不是无量纲横场。** 本棒实测该文全文 `Γ` 出现 35 次，**逐处均属此义**（`Γ(T,g) = ∂_T v_g / ∂_T ε`）。按预登记 §7.3「符号名 0 参与判定，只认 `r` 读数」，此处**不得**因符号同名而误挂为 `Γ_lit`。

## 判读（`r_K`、`r_Γ`）

- 该文把 1D TFIM 写成单一调参 `g` 的 Jordan–Wigner 自由费米子形式 `H(g) = -Σ_i (c_i - c†_i)(c†_{i+1}+c_{i+1}) - g Σ_i (2c†_i c_{i-1})`，自对偶点 `g_c = 1`。
- 该文**未写** `sinh(2K)·sinh(2Γ) = 1` 或等价 `h_c(T)`；**未定义**无量纲 `K`、`Γ` ⇒ 分子侧缺失 ⇒ **不可判读**（§7.1）。

⇒ `r_K` = **不可判读（null）**；`r_Γ` = **不可判读（null）**（且同名 `Γ` 已按上留痕排除误挂）。

## 级与计数归属

- 级：**非 A 级**（`K-GR1-0-A` 缺第 3、4 件）。
- 三分类归档：**0 命中源**，**0 计入**任何一类。
- 构造面：`n_distinct` 贡献 = 0。
