# R-J5 重推导棒 · 推导附录（数值证据 + 方法审计 · worker · 2026-09-28）

> 主件：`results/_v4_rj5_rederive_2026_09_28.md`（SHA-12 见派工回报）。
> 本附录只装**可复算的原始数值**与**方法审计**，**0 新增结论**。全部本地计算，**0 网络**，**0 触动既有件**。
> 环境：Python 3.14.7 / numpy / scipy / pypdf。

---

## A. 第一步证据：二维各向异性经典 Ising 临界线

脚本：`.scratch_rj5/derive_local.py`

```
=== A) classical 2D anisotropic Ising ===
K* (sinh(2K*)=1)            = 0.4406867935
ln(1+sqrt2)/2 check          = 0.4406867935
K2        K1=-0.5ln tanhK2   sinh2K1*sinh2K2   K1(dup eq2)   |diff|
0.0500  1.498283  1.000000000000  0.050000  1.45e+00
0.1937  0.826796  1.000000000000  0.193750  6.33e-01
0.3375  0.561590  1.000000000000  0.337500  2.24e-01
0.4812  0.402325  1.000000000000  0.481250  7.89e-02
0.6250  0.294754  1.000000000000  0.625000  3.30e-01
0.7688  0.218322  1.000000000000  0.768750  5.50e-01
0.9125  0.162637  1.000000000000  0.912500  7.50e-01
1.0562  0.121530  1.000000000000  1.056250  9.35e-01
1.2000  0.090968  1.000000000000  1.200000  1.11e+00
```

**读法**：
- 第 3 列 `sinh(2K₁)·sinh(2K₂)` 在 `K₂ ∈ [0.05, 1.2]` 全程 = `1.000000000000`（12 位）⇒ 对偶式 `K₁ = -½ ln tanh K₂` 与临界线式 `sinh(2K₁)sinh(2K₂)=1` **等价**，数值证实。
- 第 4、5 列 `|diff|` 非零 **是预期**：临界线上一般点**不是**自对偶点；只有 `K₁=K₂=K*` 处自对偶。**此列非缺陷**。

```
=== self-dual point ===
K*    = 0.4406867935098175
sinh(2K*)  = 1.0000000000001301
sinh(2K*)² = 1.0000000000002602
```

自对偶点 `K* = ½ asinh(1) = ½ ln(1+√2)`，恒等式在 13 位内成立。

---

## B. 第二步证据：1D TFIM 零温临界线

脚本：`.scratch_rj5/derive_b_v3.py`（钉住判据）、`derive_b_v4.py`（标度比）

### B.0 方法审计 —— **两版作废，一版采用**

| 版本 | 判据 | 读数 | 裁定与理由 |
|---|---|---|---|
| v1 | `prod(σ^z)=(-1)^{N↓}` 奇偶扇区 | `b_c/a = 1.5` | ❌ **作废**。`prod(σ^z)` 与每个 `σ^x_i` **反对易**：`[prod(σ^z), σ^x_i] = -2σ^x_i·prod(σ^z) ≠ 0` ⇒ **非守恒量**，扇区最小值不构成能级交叉；且偶数 L 时全上/全下同属一扇区，仍简并。 |
| v2 | 全谱隙 `E₁-E₀` | `h_c/J ≈ 0.5` | ❌ **作废**。铁磁相基态**二重简并**（全局自旋翻转），`E₁-E₀` 量的是该简并而非激发隙。 |
| **v3** | 钉住自旋 0（基限制 `bit0=0`）＋开边界 ⇒ 简并消除；再用 `r(h)=gap(2N,h)/gap(N,h)`（临界时 `gap~1/L` ⇒ `r=½`）定标 | **`h_c/J = 1.00`** | ✅ **采用** |

### B.1 简并消除校验（v2 失效原因的直接反证）

```
L=8 : gap(h=0)=2.0000000000   E0=-8.0000000000  E1=-8.0000000000   ← 未钉住：二重简并，隙读作 0
L=8 : gap(h=0.01) gap=3.553e-15                                      ← 伪「临界」
L=8 (钉住) : gap(0)=2.000000   gap(J=1)=0.780361
L=10(钉住) : gap(0)=2.000000   gap(J=1)=0.625738
```

钉住后 `gap(h=0) = 2J`（开边界下翻一个自旋断 1 键，代价 2J），**简并已消除**，隙读数可信。

### B.2 隙极小位置（**偏置估计量**，仅作趋势）

```
L=8 : min gap at h = 0.9239 (gap=7.654e-01)
L=10: min gap at h = 0.9511 (gap=6.180e-01)
```

随 L 上漂（0.9239 → 0.9511），**尚未收敛**；故本棒**不采用**极小位置法定标。

### B.3 标度比定标（**采用**）

`r(h) = gap(10,h) / gap(5,h)`；临界时 `gap ~ 1/L` ⇒ `r = ½`。

```
  h=0.60  gap(5)=1.24769 gap(10)=0.93538  r=0.7497
  h=0.70  gap(5)=1.19562 gap(10)=0.79629  r=0.6660
  h=0.80  gap(5)=1.17571 gap(10)=0.68792  r=0.5851
  h=0.90  gap(5)=1.18957 gap(10)=0.62641  r=0.5266
  h=0.95  gap(5)=1.20891 gap(10)=0.61804  r=0.5112
  h=1.00  gap(5)=1.23607 gap(10)=0.62574  r=0.5062   ← 极小
  h=1.05  gap(5)=1.27053 gap(10)=0.64894  r=0.5108
  h=1.10  gap(5)=1.31174 gap(10)=0.68608  r=0.5230
  h=1.20  gap(5)=1.41189 gap(10)=0.79364  r=0.5621
  h=1.40  gap(5)=1.66704 gap(10)=1.09003  r=0.6539
  h=1.60  gap(5)=1.97093 gap(10)=1.43752  r=0.7294
  h=2.00  gap(5)=2.65626 gap(10)=2.18703  r=0.8233
```

**`r_min = 0.5062` 落在 `h = 1.00`**，且 `0.5062 ≈ ½`（有限尺寸修正使 r 略高于 ½）。

⟹ **`H = -J Σ σ^z_i σ^z_{i+1} - h Σ σ^x_i`（Pauli）的零温临界线为 `c_trans = c_ferro`，即 `h_c = J`。**

### B.4 与 γ-R1 已核源的同相印证（**非本棒新证据**）

| γ-R1 源 | 该文自记零温临界比 | 与本棒 `h_c/J = 1` |
|---|---|---|
| S3 Xiong & Wang, arXiv:cond-mat/0512369v2 | `t ≡ h/|J|`，`t_c = 1` | 同相 |
| S2 Ma, Xu & Wang, arXiv:0808.1816v1 | `λ_c = 1` | 同相 |
| S4 Zhang & Ding, arXiv:1910.12538v2 | `g_c = 1` | 同相 |

---

## C. 第三步：断点 —— Trotter–Suzuki 生成因子

**未推、未猜、未补。** 断点内容与成因见主件 §3.3。

**可明确排除的**（代数，不依赖外部约定）：

取任意有限生成因子 `K = c_K·β·J`、`Γ = c_Γ·β·h`（`c_K, c_Γ` 为正常数），条件为 `sinh(2K)·sinh(2Γ) = 1`。

当 `T→0`（`β→∞`，`J, h > 0` 固定）时：
- `sinh(2K) → +∞`，故必须 `sinh(2Γ) → 0`，即 `Γ → 0`；
- 更精细地 `2Γ_c ≈ 2e^{-2c_K βJ}` ⇒ `h_c = Γ_c/c_Γ·β^{-1} → 0`（**指数趋零**）。

⟹ **对任意 `c_K`、`c_Γ`，该形式的临界线都给不出非零的 `h_c(T→0)`。**
⟹ 正确对应**必须**额外含层间距 `Δτ` 因子 —— 该因子正是断点本身。

---

## D. 第四步：`#12` 闭式与本棒临界线的定量对照

`#12` 闭式（`_v3_recheck_12_executor_2026_09_27.py:133-148`）本棒实测：

```
t_rel = k_BT/J   h_c/J = 2*t_rel*asinh(1/sinh(1/(2*t_rel)))
  10   ->  7.378176e+01
   3   ->  1.492331e+01
   1   ->  2.813658e+00
 0.5   ->  7.719368e-01
 0.2   ->  6.581609e-02
 0.1   ->  2.695220e-03
 0.05  ->  9.079986e-06
 0.01  ->  7.714999e-24
```

`#12` 自身约定下（`c_ferro = J/4`、`c_trans = h/4`）的精确零温临界点：`c_trans = c_ferro` ⇒ `h_c = J` ⇒ **`h_c/J = 1`**。

| `t_rel` | `#12` 闭式 `h_c/J` | 本棒精确 `h_c/J` |
|---|---|---|
| 0.1 | 2.695e-03 | 1 |
| 0.01 | **7.715e-24** | 1 |

**偏差随 `T→0` 发散。** 此为一致性检验结果，**0 改判 `#12`**（档位归 verdict-keeper）。

---

## E. deposon 定义锚点实测（逐字计数）

```
Deposon_Requirements_v1.md            : Ising=0  sinh=0  β=0  → 无 K/Γ/J/h 的伊辛学声明
Deposon_凝子_统一场论研究报告_v1.pdf   : Ising=0  sinh=0  cosh=0  beta=0  transverse=0
                                        Gamma=5（全为 Gamma_aether / gamma_aether）
README.md:5                           : 无 Ising / 无 K / 无 Γ
```

`Gamma_aether` 逐字（统一场论研究报告）：

```
S_eff(E) = S_bg(E) - [S_bg(E) |W><W| S_bg(E)] / [E - E_0 + i*Gamma_aether/2]
- Gamma_aether: Ether-induced linewidth
d(rho)/dt = -i[H, rho] + gamma_aether * (L rho L^(dagger) - {L^(dagger) L, rho}/2)
Gamma_aether = gamma_ECM * psi(t)
```

**量纲判读**：`Gamma_aether` 与 `E - E_0` 在同一分母内相加 ⇒ **有量纲能量**；TFIM 的 `Γ ≡ βh/4` **无量纲**。二者不同物，识别**过不了量纲关**。

---

## F. 检索逐次台账（14 次 / 上限 15）

机器台账：`.scratch_rj5/rj5_query_log.jsonl`（14 行，逐行含 URL / CST 时刻 / 状态 / bytes）。

```
Q1  arXiv API  200      810  abs:"transverse field Ising" AND abs:"classical two-dimensional"   total 0
Q2  arXiv API  200    6929  all:"quantum-classical correspondence" AND all:"Ising"               total 3
Q3  SciPost     ERR      0  SSL UNEXPECTED_EOF
Q4  arXiv API  200      810  all:"anharmonic oscillator" AND all:"Ising" AND all:"duality"       total 0
Q5  arXiv API  200    5404  all:"anharmonic oscillator" AND all:"Ising model"                   total 2
Q6  arXiv API  200   35533  all:"transverse-field Ising model" AND all:"exact solution"        total 16
Q7  arXiv PDF   ERR      0  SSL UNEXPECTED_EOF
Q8  arXiv PDF   200 2321493  2307.06946v2   (SHA-12 0591262207aa)
Q9  arXiv API  200   59484  abs:"Kramers-Wannier" AND abs:"transverse field"                   total 25
Q10 arXiv PDF   200 2245043  2508.20167v3   (SHA-12 de5306e894b6)
Q11 arXiv PDF   200  344851  2509.01853v1   (SHA-12 38de7803076a)
Q12 arXiv API  200   13300  abs:"quantum-classical correspondence" AND abs:"transverse"        total 6
Q13 arXiv API  200    3549  ti:"exactly solvable quench protocol"                               total 1
Q14 arXiv PDF   200 1509169  1706.02322v2   (SHA-12 93927159b2c1)
```

**四份全文的 `sinh` / `Γ` 机械计数**：

```
p1706_02322: sinh=1 (作者姓氏 Sinha)   Γ/γ 定义: γ = 耗散参数（γ = 0.1, 0.2, 0.5）
p2307_06946: sinh=0                    Γ: 集体噪声宽度（Γ ≡ 0）
p2508_20167: sinh=0                    Γ: 0
p2509_01853: sinh=1 (作者姓氏 Sinha)   Γ: 0
```

**A 级合格源 = 0。** `sinh(2K)·sinh(2Γ)=1` 与 `K`/`Γ` 的定义式，四源**全未出现**。

---

**出证｜worker（本棒执行段）出件｜2026-09-28｜附录 0 新增结论，全部数值可由 `.scratch_rj5/` 脚本复算**
