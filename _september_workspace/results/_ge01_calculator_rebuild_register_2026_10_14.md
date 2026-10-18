# G-E01 缺口 `G3` ｜ `tools/distortion_calculator.py` **重建执行登记件** —— 2026-10-14

> **出件**：worker｜**日期**：2026-10-14
> **触发**：PI **2026-10-14 15:35** 裁「**甲 授权棒推 G3 计算器重建（设计已成，前置已具）**」（**派工单转录**；⛔ **0 断言卡面原文逐字**、⛔ **0 断言卡号**）
> **件名**：`results/_ge01_calculator_rebuild_register_2026_10_14.md`（新建，⛔ 0 覆盖）
> **本棒射程**：**只做重建**（写 `tools/distortion_calculator.py` ＋ 静态／单元级自测）｜⛔ **0 开跑任何实验**｜⛔ **0 建 5 锚 JSON**｜⛔ **0 回改既有件**｜⛔ **0 代 PI 裁**｜⛔ **0 宣告①毕**
> **状态**：**重建已完成 · 自测 9/9 通过 · 锚面未冻结 · 全部待裁项候 PI**

---

## §1 方法与授权

### §1-1 PI 裁（**派工单转录 · ⛔ 0 断言卡面**）

| 项 | 内容 |
|:--|:--|
| **PI 裁字面** | 「**甲 授权棒推 G3 计算器重建（设计已成，前置已具）**」 |
| **时点** | 2026-10-14 15:35 |
| **出处** | **派工单元所载**（本棒唯一来源） |
| ⚠ **卡面状态** | 🔴 `Q12` 之**题面与卡面 0 在盘**（本棒内容检索 `results/` 全域：`Q12`／`授权棒推`／`计算器重建` 之命中**全为在册他件之转引**，⛔ 无任何 PI 卡面实体）⇒ 与 `a68b2971b8e1` §1-5 之双通道实测**逐位相符**（该件 L89–L91 逐字：「`Q12` 之问卷件在三根内 **0 在盘**」／「本棒**无法逐字回读**其题面」）⇒ **沿该件既有体例**（`_ge01_c3_gaps_disposition_2026_10_14.md` L4 逐字：「（**派工单转录**；⛔ **0 断言卡面原文逐字**、⛔ **0 断言卡号**）」）登记 |

### §1-2 方法（逐条声明 · 本棒自证）

1. **逐字回读**：§2 之正典字面、设计件之实现规格、正典口径四条，**开卷回读实体文件**；凡转引他件者**标明节位／行号**。
2. **元数据逐件自算**：`hashlib.sha256` 全文字节取前 12 位（⛔ 禁内建 `hash()`）；⛔ **0 沿用**他件自报值。
3. **阴性结论双通道**：① 文件名通道（`os.walk` 全树，basename 含 `distortion_calculator` 大小写不敏感）＋ ② 目录 census／字节通道；两通道皆 0 方作阴性判据。
4. **本棒 0 重跑任何实验**：0 调 LLM／0 调 API／0 读 key／0 读 `.env`／0 上传／0 远端写；自测为**离线 `Fraction` 精确枚举 ＋ 网格枚举**（0 calls）。
5. **⛔ 0 编造**：凡盘上 0 命中之件如实登记为 KD，⛔ 0 虚构其内容。

### §1-3 本棒实测之源件指纹（SHA-12／bytes · **本棒自算**）

| # | 件（相对仓根） | SHA-12 | bytes | 本棒动作 |
|:-:|:--|:-:|--:|:--|
| 1 | `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md`（**正典 spec · 活件**） | `423c84de20d5` | 15,457 | **逐字回读**（L10/L12/L22/L30/L32/L56/L61/L66/L68/L88/L91/L103–L110/L116/L121–L124/L134）＋ 字节面（CR=0／TAB=0／BOM=False） |
| 2 | `results/_ge01_prereg_seven_requirements_draft_2026_10_13.md`（§6 四条正典口径） | `0a031a9795a9` | 39,337 | **逐字回读** §6 L170–L173 四条 ＋ L177／L178 两条实现纪律（CR=0） |
| 3 | `results/_ge01_calculator_rebuild_design_2026_10_14.md`（**本棒实现规格来源**） | `8ab699f017c8` | 46,007 | **逐字回读**（§0／§1／§2／§3-1 至 §3-5／§4-1 至 §4-4／§5／§6／§7／§8 全篇） |
| 4 | `results/_r5_spec_pack_retrieved_2026_10_13/鲍勃_minimax实验委托规格包_2026_10_12.md` | `bb66c577673b` | 14,758 | **逐字回读** §1.2–§1.6 关键行（判死线／阈值纪律／D1 缺失／产物链／验收口径） |
| 5 | `tools/llm_client.py`（对照锚① · 重建前 census） | `1722500da4aa` | 8,118 | 字节实算（与设计件 §1-4 之自报值**逐位相符**） |

> 📌 件 1／2／3／4 之实测值与设计件 §1-2 之自报值**逐位相符**；本棒系**独立复测**，⛔ 非转述。
> ⚠ **件 4 之锚值坐标问题**（沿设计件 §1-2 之注）：该包 §1.3 记 spec 之远端锚为 `aab9d78ada2d`／15,549 B（受托方 Linux 克隆），与我方盘**终态** `423c84de20d5`／15,457 B **不同** ⇒ 本件引用其**字面**（§1.3 表末行 D1 缺失、§5 指纹纪律），⛔ **0 以其 spec 锚值为我方可复算之值**。

---

## §2 重建执行记录

### §2-1 落盘前检查（**阴性 · 双通道 · 0 覆盖**）

| 通道 | 检查 | 本棒实测（**落盘前**） |
|:--|:--|:--|
| ① 文件名通道 | `Test-Path tools/distortion_calculator.py` | 🔴 **False** |
| ① 文件名通道 | glob `tools/distortion_calculator*.py`（窄根） | 🔴 **0 命中** |
| ① 文件名通道 | `os.walk` 三根：basename 含 `distortion_calculator`（大小写不敏感） | 🔴 **0 命中**｜`deposon-repo` **2,224** 件 ＋ `deposon-sub` **1,189** 件 ＋ `.minimax/workspace` **1** 件 ＝ **3,414** 件 |
| ① 文件名通道（扩展射程） | `os.walk` 运行时全域 `C:\Users\Administrator\.minimax` | 🔴 **0 命中**｜**70,312** 件 |
| ② 目录 census 通道 | `tools/` 逐件字节 census（**落盘前**） | 🔴 **5 件**（`exp_harness.py`／`llm_client.py`／`make_figures_v2.py`／`make_figures_v2_en.py`／`read_key.py`）⇒ **无该件** |
| **遍历完整性** | `os.walk` `onerror` 计数 | ✅ **0**（两次全树遍历皆 0） |

> 📌 **阴性结论之射程** ＝ 上列四根（`deposon-repo`／`deposon-sub`／运行时附件面 `.minimax`）；⛔ **0 断言**「全机全域 0 命中」。
> ⇒ **该路径 0 在盘 ⇒ 本棒系新建，⛔ 0 覆盖、0 需 `_r1`**（`Test-Path results/_ge01_calculator_rebuild_register_2026_10_14.md` ＝ **False**、`_r1` 命名亦 **False**）。

### §2-2 重建件（**本棒唯一代码产物**）

**路径**（锚②字面，0 改）：`tools/distortion_calculator.py`｜**绝对路径**：`D:\私人资料\deposon-repo\tools\distortion_calculator.py`

| 层 | 内容（设计件 §3-1 之五层） | 本棒落法 |
|:-:|:--|:--|
| **L0 文件头** | docstring（来源件逐件登记 ＋ 逐字节位 ＋ 铁律 7 条）＋ `ANCHOR_ID`／`ANCHOR_PATH`／`VERSION`／`SUPPORTED_VERSION` | 锚 ID/路径/`version=2026-09-11` **逐字照录** spec L30 |
| **L1 常量区** | `PAY_DOMAIN`／`DEFAULT_C`／`BOOTSTRAP_RESAMPLES`／`BOOTSTRAP_SEED`／`BOOTSTRAP_SEEDS`／`CI_LOWER_LEVEL`／`CI_UPPER_LEVEL`／`CI_METHOD`／`GRID_*`／`T5_*`／`T9_BOUNDARY_POINTS` | `DEFAULT_C=Fraction(1)`（五族全 1）｜`10000`／`42`／`(42,123,456)` **⛔ 0 新设**（照录 L91／L116） |
| **L2 守卫层** | `assert_eps`／`assert_weights_sum_one`／`assert_same_length` ＋ 私有 `_as_fraction`／`_resolve_weights`／`_check_max_u` | **失败即 raise**（类型不合 `TypeError`／值不合 `ValueError`），⛔ 0 静默通过、⛔ 0 静默替值 |
| **L3 精确核** | `distortion_indicator`／`distortion_gapwise`／`guarded_denominator`／`guarded_denominator_rescaled`／`distortion_multiplier`／`aggregate_cells`／`bootstrap_ci`／`kill_decision` | **核内 0 float 运算**（全程 `Fraction`）；`kill_decision` 函数体 **逐字转引** spec L103–L110 |
| **L4 产表轨** | `distortion_multiplier_float`／`cell_table_row` | 薄封装，`float` 转换**只在出口**；每处转换**同时输出 `exact_str`**（分数字面），⛔ 0 以 float 列覆盖 exact 列 |
| **L5 自测** | `self_test`（`T1`–`T9`）＋ 私有 `_build_trajectory`／`_multiplier_float_impl`／`_bit_identical`／`_print_report`／`_reconfigure_stdout`／`main` | 唯一输出面为 `--self-test` 之 stdout，⛔ **0 写盘** |

**13 个公开函数签名 vs 设计件 §3-2**（逐条实测 **13/13 逐字命中**）：

| # | 签名（设计件 §3-2 之字面） | 实测 |
|:-:|:--|:-:|
| 1 | `def assert_eps(eps) -> "Fraction":` | ✅ |
| 2 | `def assert_weights_sum_one(weights) -> None:` | ✅ |
| 3 | `def assert_same_length(seqs: tuple) -> int:` | ✅ |
| 4 | `def distortion_indicator(choices, key_sets, weights=None) -> "Fraction":` | ✅ |
| 5 | `def distortion_gapwise(choices, optimal_payoffs, actual_payoffs,`（次行 `max_u=DEFAULT_C, weights=None) -> "Fraction":`） | ✅ |
| 6 | `def guarded_denominator(d_bayesian, eps, c=DEFAULT_C) -> "Fraction":` | ✅ |
| 7 | `def guarded_denominator_rescaled(g_bayesian, eps, c=DEFAULT_C) -> "Fraction":` | ✅ |
| 8 | `def distortion_multiplier(d_llm, d_bayesian, eps, c=DEFAULT_C) -> "Fraction":` | ✅ |
| 9 | `def aggregate_cells(cell_readings, weights=None) -> "Fraction"` | ✅ |
| 10 | `def bootstrap_ci(values, resamples=BOOTSTRAP_RESAMPLES, seed=BOOTSTRAP_SEED):` | ✅ |
| 11 | `def kill_decision(mean_mult, ci_lo, ci_hi, theory_U_hit_rate) -> str:` | ✅ |
| 12 | `def distortion_multiplier_float(d_llm, d_bayesian, eps, c=1.0) -> float` | ✅ |
| 13 | `def cell_table_row(choice_readings, eps, c=1.0) -> dict` | ✅ |

**边界守卫 `B1`–`B12` 之落位**（逐条 · 设计件 §3-4）：

| # | 守卫 | 落位（实测） |
|:-:|:--|:--|
| **B1** | 分母非零 | `assert_eps` ＋ `guarded_denominator`（`max(G_B, c·eps) ≥ c·eps > 0`）；非法 `ε` → `raise`，⛔ 0 静默替值 |
| **B2** | `G_B＝0` 守卫支路保 `c` | `guarded_denominator` 分支 `cc*e`（T2 实测 `c=2/ε=0.1` → `1/5`，倍数 **10**） |
| **B3** | 无守卫支路 `c` 精确消去 | `guarded_denominator` 分支 `g_b`（T2 实测 `G_B=5,c=2` → 分母 **5**，`(8/2)/(5/2) == 8/5` 逐位相等） |
| **B4** | 边界并列 `G_B＝c·ε` | 数值上两支路**同值**读数无歧义（`g_b >= cc*e` 之 `>=` 归一无守卫支路）；⚠ **支路标签规则未闭** ⇒ 见 §5 KD-A3 |
| **B5** | `D∈[0,H]` | `cell_table_row` 之 `in_range`（`H` 由 `choice_readings["h"]` 入参传入，⛔ 0 硬编码）；T4 实测端点全过 |
| **B6** | 权重和 ＝ 1 | `assert_weights_sum_one`（**`Fraction` 轨精确判定**，⛔ 0 用 float 容差）；负向用例实测 `raise` |
| **B7** | 序列长度一致性 | `assert_same_length`（A_τ／K_τ／u\*_τ／u_τ 逐轨迹等长，不等即 `raise`） |
| **B8** | `c` 之退化维 | `c` **保留于全部签名**，`DEFAULT_C=Fraction(1)`；`c` ⛔ **0 作网格轴**（仅 T2／T3 代数自测取 `c=2` 之 10 值） |
| **B9** | `max_u` 语义禁越界 | `_check_max_u`（须 `>0`）＋ docstring 载「⛔ 非任务名数值选择·⛔ 非模型性能测量」逐字 |
| **B10** | 二进制损失不入 `D` | `distortion_indicator` ⛔ 0 除以 `H`／0 取对数；T4 实测全拒 `D=33`（非 1） |
| **B11** | 禁内建 `hash()` | 指纹面一律 `hashlib.sha256`；T8 实测源码内内建散列调用出现 **0** 次 |
| **B12** | 凭据与网络 | 静态扫描实测：`requests`／`urllib`／`socket`／`http://`／`https://`／`os.environ`／`getenv` 各 **0** 次；`.env` 仅 1 次且为**禁令陈述**（docstring 铁律 1「0 读 `.env`」）；唯一 `io.open` 为 T8 **读自身** |

### §2-3 落盘后字节级自报（**本棒外部实测** · 非件内自报）

| 项 | 值 |
|:--|:--|
| 路径 | `D:\私人资料\deposon-repo\tools\distortion_calculator.py` |
| **SHA-256（全文 → 前 12 位）** | **`410a12482eef`** |
| **bytes** | **40,611** |
| BOM | **False** |
| CR | **0** |
| TAB | **0** |
| CTRL（非 LF 之控制字节） | **0** |
| **nonAscii** | **3,220 字符 ／ 9,607 字节**（**双口径并列**：字符口径 ＝ 码点数；字节口径 ＝ UTF-8 编码后非 ASCII 字节数） |
| **U+FFFD** | **0** |
| 末尾换行 | **True**（纯 LF，合计 **861** 个 LF；沿仓内 `tools/` 同族 5 件之既有惯例） |
| 件内自报（T8 自测面） | `sha256_12=410a12482eef`／`bytes=40611`／BOM=False／CR=0／TAB=0／U+FFFD=0 ⇒ **与外部实测逐位相符** |

> 📌 落盘方式：`write` 工具直写（⛔ **0 经 PowerShell 管道中转 UTF-8 正文**），其后以 Python `io.open(..., encoding='utf-8', errors='strict')` 读回校验，并以 `io.open(p, 'w', encoding='utf-8', newline='\n', errors='strict')` 补齐末尾 LF（与仓内 5 件同族 `.py` 之惯例对齐）⇒ 纯 LF ＋ 无 BOM ＋ 严格 UTF-8 三项由构造保证。
> ⚠ **本棒清理**：独立复核脚本之 `import` 一度在 `tools/` 生成 `__pycache__/distortion_calculator.cpython-314.pyc`（52,156 B）⇒ **已移除**（`mavis-trash`）；现 `tools/` 为 **6 件**（5 件既有 ＋ 本棒 1 件），既有 5 件字节与 SHA **全部未变**（`1722500da4aa`／`275e480ba4d9`／`0dc3ea09f42d`／`b4e880a6af33`／`a9b56c4e775f`）。

### §2-4 正典式逐字落位（**spec 原字面 10/10 命中**）

| 正典字面（`423c84de20d5` 之 ASCII 原字面） | 出处 | 命中 |
|:--|:--|:-:|
| `D(M, T) = E_pi[ Sum_t \|u*(a_t) - u(a_t)\| / max_u ]` | L61 | ✅ |
| `max_u` | L66 | ✅ |
| `失真倍数 = D_LLM(M, T) / max(D_Bayesian(M, T), eps)` | L68 | ✅ |
| `distortion_multiplier(M, T) = D_LLM(M, T) / max(D_Bayesian(M, T), eps)` | L88 | ✅ |
| `version=2026-09-11` | L30 | ✅ |
| `P_B_DISTORTION_CALC` | L30 | ✅ |
| `tools/distortion_calculator.py` | L30 | ✅ |
| `任何 >= 1 锚漂移 -> 全 V0 撤回。` | L32 | ✅ |
| `跨 (M, T) 算 mean + 95% bootstrap CI(10k resamples)。` | L91 | ✅ |
| `seed=42, 123, 456 三套, 看 std/mean > 0.2 则报` | L116 | ✅ |

**`kill_decision` 函数体 vs spec L103–L110 之逐字比对**（逐行子串实测 **5/5 命中**，⛔ 0 改写）：

```
    if mean_mult >= 2.0 or theory_U_hit_rate >= 0.3:
        return "FAIL_H0"  # 机制不可行 或 30%+ cell 超理论界
    elif mean_mult <= 1.5 and ci_hi <= 1.8 and theory_U_hit_rate <= 0.1:
        return "PASS_H1"  # 机制可商用
    else:
        return "GRAY"  # 1.5 < mean < 2.0 或 CI 跨边界
```

---

## §3 自测结果（**静态／单元级 · 0 calls · 0 网络**）

### §3-1 设计件 §6 之 `T1`–`T9`（**逐项 · 9/9 通过**）

执行命令：`python tools/distortion_calculator.py --self-test`｜退出码 **0**

| # | 自测项 | 判据（照录正典／代数恒等） | 实测结果 | 判定 |
|:-:|:--|:--|:--|:-:|
| **T1** | 正典例向量 | `G_L＝2, G_B＝0, ε＝0.1` ⇒ `c＝1` 得 **20**／`c＝2` 得 **10**（`Fraction` 轨逐位相等） | `c=1 得 20`；`c=2 得 10` | ✅ |
| **T2** | 守卫两支路 | ① `G_B ≥ c·ε` ⇒ 分母 ＝ `G_B` 且 `c` 精确消去；② `G_B＝0` ⇒ `G_L/(c·ε)` 且 `c` 不消去 | ① 分母 ＝ 5，`(8/2)/(5/2)==8/5` 逐位相等；② `c=1` 分母 `1/10` 倍数 20／`c=2` 分母 `1/5` 倍数 10 | ✅ |
| **T3** | 代数恒等式网格 | `∀(G_L,G_B,c,ε)` ∈ 网格：`G_L/max(G_B,c·ε) == (G_L/c)/max(G_B/c,ε)`，**逐点精确相等，⛔ 0 用容差** | 网格点数 **10,000**（期望 10,000）／失配 **0** | ✅ |
| **T4** | `D∈[0,H]` 边界 | 逐格 `0 ≤ D ≤ H`（`H` 入参）；含 `D＝0`／`D＝H` 两端点；**B10** 基数不入 `D` | `H=1/4/33 × n_rej∈{0,H}` 全过；全拒 `D=33`（非 1） | ✅ |
| **T5** | 枚举面自检 | ① A 对象：**15 键非空**；② C 对象：`3H/4`（`H＝1..100`）；③ D 对象：**三处更正代数**（恒等式网格 ＋ 例值 20／10） | ① 非空键集 **15**（期望 15）；② 可达（`H%4==0`）**25** 例／非整除 **75** 例（见 §3-3 留痕）；③ 全过 | ✅ |
| **T6** | 聚合面 | ① 权重和精确 ＝ 1（否则 `raise`）；② `err_τ＝Σ_t 1{A_t∉K_t}` 与手算相符；③ **⛔ 0 以轨迹内决策数再加权** | ① 和为 `11/12` 之组 `raise`、和为 1 之组通过；② 手算 2 ／实现 2；③ 异长轨迹 (2,1) 均匀权 `D=1/2`（决策数加权将给 1/3） | ✅ |
| **T7** | 双轨一致率 `S7` | 两轨下精确断言之一致率；逐项明细随件报 | 逐位相符 **200/200**（一致率 **1**）；最大相对偏差 **0** | ✅（⚠ 判据未闭 ⇒ §3-3 留痕） |
| **T8** | 指纹面自测 | ① 件自身 `sha256` 由 `hashlib.sha256` 算定；② 源码内 **0** 出现内建散列调用；③ BOM＝False／CR＝0／TAB＝0 | `sha256_12=410a12482eef`／`bytes=40611`；内建散列调用 **0** 次；BOM=False／CR=0／TAB=0／U+FFFD=0 | ✅ |
| **T9** | 判死面转引测试 | `kill_decision` 三分支在边界点（`1.5`／`1.8`／`2.0`／`0.1`／`0.3`）之输出**逐字相符** | 五例：`FAIL_H0 ×2`／`PASS_H1 ×1`／`GRAY ×2`，边界点全用 `T9_BOUNDARY_POINTS` | ✅ |

### §3-2 独立复核（**本棒另立只读脚本 · 0 写盘**）

| 面 | 实测 |
|:--|:--|
| **模块可导入面** | ✅ `importlib` 装载 0 异常；`VERSION`／`SUPPORTED_VERSION` ＝ `2026-09-11`；`ANCHOR_ID`／`ANCHOR_PATH` ＝ `P_B_DISTORTION_CALC`／`tools/distortion_calculator.py`；`DEFAULT_C` ＝ `Fraction(1)`；`PAY_DOMAIN` ＝ `(0, 1)`；`BOOTSTRAP_*` ＝ `10000`／`42`／`(42,123,456)`；网格点数 **10,000** ＝ 期望 |
| **L3 核冒烟** | `distortion_multiplier` c=1 → **20**／c=2 → **10**；`guarded_denominator(0, 1/10, 2)` → **1/5**；`guarded_denominator_rescaled(0, 1/10, 2)` → **1/10**；`distortion_indicator`（2 轨迹，各 2 位）→ **3/2**；`distortion_gapwise`（`u*=[1,1]`／`u=[1,0]`）→ **1**；`aggregate_cells([1,3,5])` → **3** |
| **`assert_eps` 之类型面** | `float 0.1` → `3602879701896397/36028797018963968`（**精确二进制值**）；`Fraction(1,10)` → `1/10` ⇒ 二者**不相等**（已在 T1 留痕栏登记） |
| **`bootstrap_ci` 之可复现性** | 同种子 (`42`) 复跑 → `ci_lo`/`ci_hi` **逐位相同**（✅ 固定种子成立）；异种子 (`123`) → `ci_hi` ＝ `7/2`（≠ `7/4`）⇒ 种子敏感性**可见**，报出口径（`std/mean > 0.2` ⇒ 报「种子敏感」）属**分析层**，⛔ 本件 0 代判 |
| **L4 产表轨** | `distortion_multiplier_float(2,0,0.1,1.0)` → **20.0**；`cell_table_row` 返回 **`exact` 列（`Fraction` ＋ `exact_str` 分数字面）＋ `float` 列 ＋ `in_range` ＋ `tests_side_correction_note` 留痕栏**（读数：`d_exact=1`／`multiplier_exact=10`／`in_range=True`） |
| **守卫负向面（13 例 · 须 raise）** | ✅ **13/13** 如期 raise：`eps=0`／`eps<0`／`eps=inf`／`eps=nan`／`eps=str`／权重和≠1／长度不一致／`c<=0`／`D_Bayesian<0`／`max_u<=0`／轨迹数不符／空轨迹集／`cell_table_row` 缺键 |

### §3-3 「测试侧修正留痕」栏（**照录 `0a031a9795a9` §6 **L178** 逐字要求**：「报出口径须容『测试侧修正留痕』栏位」；修正依据 ＝ **枚举精确值本身（0 依赖对方数值）**）

| # | 留痕 | 性质 |
|:-:|:--|:--|
| **T1** | `ε` 以 `Fraction(1,10)` 给；若以 float 字面 `0.1` 给，`assert_eps` 精确化为 `3602879701896397/36028797018963968`，倍数**非 20** ⇒ 正典例向量**一律以 `Fraction` 给** | **口径澄清**（非失败） |
| **T5** | C 对象 `3H/4` 于 `H%4≠0` 时**非整数** ⇒ 非可达之拒绝计数（拒绝计数必为整数）⇒ 75/100 例**如实登记、不计入失败**；可达 25 例（`H%4==0`）全过 | **如实登记**（非失败） |
| **T6** | **首跑用例侧有误**：初写权重 `(1/3, 1/3, 1/3)`，而精确有理求和 `1/3×3 == 1` ⇒ 守卫**正确地未 raise** ⇒ 系**用例侧**之误、**非守卫失效**；已改用精确和为 `11/12` 的非单位权重组 `(1/3, 1/3, 1/4)` 复测通过，并**补测**精确和为 1 之组须通过 | **测试侧修正（已修）** |
| **T7** | 双轨对照规则（容差有无及其值）**盘上 0 候选**（KD-A3）⇒ 本件**仅报**实测一致率（200/200）与最大相对偏差（0），⛔ **0 代定判据** | **候 PI 另给** |
| **T5（首跑）** | 首跑另有一处**代码侧**缺陷：报告格式化串含 `H%4==0` 之裸 `%` 被 `%`-格式化误解析（`ValueError: unsupported format character '='`）⇒ 已改为 `H%%4==0` | **代码缺陷（已修）** |

> 📌 **如实交代**：首轮 `--self-test` 实测 **7/9 通过**（`T5`／`T6` 失败），经上述两处修正后复跑 **9/9 通过** ⇒ 记入本栏，⛔ **0 隐匿首跑结果**。

---

## §4 与 5 锚之同批重锚（依设计件 §4-2 之 `S1`–`S9` · **⛔ 0 代裁**）

| 序 | 动作 | 本棒状态 | 实测／依据 |
|:-:|:--|:--|:--|
| **S1** | **前置全闭**（`P1`–`P9` ＋ `C1`–`C6`） | 🔴 **未闭** | `C1` 闭／`C2` 裁生效／**`C3` 不通过**（不合行 3→2）／**`C4` 未满足**（三载体 0 在盘 —— 本棒补其一）／`C5` 待裁／`C6` 未明示 ⇒ 沿 S1 之 ⛔「**0 跳步**」，本棒**未以「纸面可跑」充闭** |
| **S2** | **本设计件核准**（PI 明示） | 🟡 **以派工转录满足 · 卡面 0 在盘** | PI 裁字面含「**设计已成，前置已具**」＋「**授权棒推**」⇒ 视为设计件获准执行之授权；⚠ **卡面 0 在盘**（§1-1）⇒ **⛔ 0 断言**卡号／卡面原文；⛔ **0 棒自签生效** |
| **S3** | **实现**（本棒） | 🟢 **已毕** | `tools/distortion_calculator.py` ＝ `410a12482eef`／40,611 B；⛔ 0 内建 `hash()`／⛔ 0 读 key／⛔ 0 网络／⛔ 0 改 kill-line（静态扫描 ＋ T8 实测） |
| **S4** | **自测通过**（`T1`–`T9`） | 🟢 **已毕** | **9/9 PASS**（退出码 0）；自测留痕见 §3（含「测试侧修正留痕」栏 5 条）｜⛔ 0 以他方自报值为验收依据（本棒自测**全为本方精确枚举**） |
| **S5** | **双轨一致率**（`S7`） | 🟡 **已测 · 判据未闭** | 逐位相符 **200/200**（一致率 **1**），最大相对偏差 **0**；⚠ **容差之有无 0 代定**（KD-A3）⇒ 报读数而**不报合格判据** |
| **S6** | **实测新指纹**（锚②现值） | 🟢 **已毕** | `{sha256_12: "410a12482eef", bytes: 40611}`（**本棒自算**，`hashlib.sha256` 全文取前 12 位）⇒ 见 §2-3 |
| **S7** | **建 5 锚 JSON**（`G7` 之出件动作） | 🔴 **未执行（⛔ 0 建锚）** | 本棒射程为「**只做重建**」⇒ `results/ge01_prereg_5anchor.json`／`results/_ge01_prereg_5anchor.json` **两命名仍 0 在盘**（**本棒实测 `Test-Path` 皆 False**；设计件 §8-3 亦记二者于其落盘前皆 False）；⚠ **重建已实体化而锚面未冻结 ⇒ `G7` 仍未闭** |
| **S8** | **追认／生效登记件** | 🟡 **本件为执行登记（非生效登记）** | 本件载**授权链**（§1-1 PI 裁）＋**现值复测**（§2-3）＋`OLD→NEW` 对照（见下）；⚠ 正式**追认／生效登记件**（另立）未出 ⇒ ⛔ **0 宣告**要件⑤ 闭（`C4` 未满足） |
| **S9** | **连带判定**：撤回条款**是否触发**、射程为何 | 🔴 **未决 · ⛔ 0 代裁** | 射程**分叉未裁**：「全 **KT-A1** 撤回」（`78b71d404366` L263）vs「全 **V0** 撤回」（上游 P-A L54／spec L32）⇒ 见 KD-A5；⛔ **0 由棒代 PI 明示射程** |

**锚② `OLD → NEW` 对照（供 S7／S8 填表用 · 值均为本棒实测）**：

| 项 | OLD（重建前） | NEW（重建后 · 本棒现值） |
|:--|:--|:--|
| `path` | `tools/distortion_calculator.py` | 同左（**未移动、未重命名**） |
| **在盘状态** | 🔴 **0 在盘**（双通道 · 三根 3,414 件 ＋ 运行时全域 70,312 件 皆 0 命中） | 🟢 **在盘** |
| `sha256_12` | **无**（实体不存在） | **`410a12482eef`** |
| `bytes` | **无** | **40,611** |
| `role`／`status` | — | `distortion_calculator`／**`unfrozen_pending_PI`**（拟；⚠ 设计件 §4-3 之拟登记行写 `"status": "frozen"`，本棒⛔ **0 自签冻结** ⇒ 改拟 `unfrozen_pending_PI`，登记为 KD-A6 之一） |
| `version` 字段 | — | `version=2026-09-11`（沿锚字段字面，⛔ 0 改 ⇒ KD-A7） |

> ⚠ **「首次实体化」而非「漂移」**：锚②之旧实体在**我方盘 0 存在** ⇒ 本次**非** spec L32「锚漂移」而是**锚②首次实体化** ⇒ `superseded_value` 之语义（`"absent"` vs 实值）**⛔ 0 代定**（沿设计件 §4-3 之同一条，KD-A6）。

---

## §5 遗留 ／ KD（**本棒 ⛔ 0 代处** · 共 13 条）

| # | KD | 级别 | 状态 | 须谁给 |
|:-:|:--|:-:|:--|:--|
| **KD-A1** | 🔴 **`D` 之两口径未择定**（指标式 `1{A_t∉K_t}` vs 差值式 `|u*−u|/max_u`）⇒ 重建件**两口径并存**（`distortion_indicator` ＋ `distortion_gapwise`），⛔ 0 择定入锁 | 高 | **未闭**（本棒 ⛔ 0 代择） | **PI 认定** |
| **KD-A2** | 🔴 **`KC-1` 互斥未裁**（以自检向量为准 ⇒ `ε` 钉死 `0.1`；以网格择优为准 ⇒ 判据①必不过）＋ **`ε` 之值仍未给** ⇒ 重建件仅提供 `ε` 入参口，⛔ **0 给值** | 高 | **未闭** | **PI 裁**（甲／乙／丙） |
| **KD-A3** | 🔴 **双轨对照规则 0 候选**（何时须逐位一致、容差若存在则何值）＋ **`B4` 并列处理规则未定** ⇒ `S7` 有读数（200/200）而无判据 | 高 | **未闭**（`T7` 留痕已登记） | **PI 另给** |
| **KD-A4** | 🔴 **自检基准件 `f5da17e62b07` 0 在盘** ⇒ `T5` **无独立外部基准**（本棒 `T5` 全为**本方精确枚举**，符合 `0a031a9795a9` §6 L177 之验收纪律，但⛔ 无第三方复现基准） | 高 | **未闭**（本棒 ⛔ 0 独立复测该 SHA） | **PI 授权补录 或 另派独立重写棒** |
| **KD-A5** | 🔴 **撤回条款射程分叉**（「全 **KT-A1** 撤回」vs「全 **V0** 撤回」）0 调和 ⇒ `S9` 无法判定 | 高 | **未闭**（⛔ 0 代裁射程、⛔ 0 宣告撤回已生效或不生效） | **PI 择** |
| **KD-A6** | 🔴 **锚②之 `superseded_value` 语义未定**（**首次实体化**，⛔ 非漂移）＋ **`status` 拟值未定**（`frozen` vs `unfrozen_pending_PI`，本棒⛔ 0 自签冻结）＋ **5 锚 JSON 未建**（`S7` 未执行） | 高 | **未闭** | **PI 明定** |
| **KD-A7** | 🟡 **`version=2026-09-11` 与新件语义之张力**（重建件沿锚字段字面 0 改，改之即改锚口径） | 中 | **未闭**（本棒沿 0 改） | **PI 确认** |
| **KD-A8** | 🟡 **`Q12` 题面／卡面 0 在盘**（本棒实测：`results/` 全域内容检索 0 命中 PI 卡面）⇒ §1 之授权仅据**派工单转录** | 中 | **未闭** | **PI 补登记件** |
| **KD-A9** | 🟡 **`H` 未锁**（`G1`）⇒ `T4` 之 `D∈[0,H]` 仅以**入参 `H`** 测（`H=1/4/33` 之样例值系**自测取值**，⛔ 0 断言为锁定值） | 中 | **未闭** | **PI 另给／授权枚举** |
| **KD-A10** | 🔴 **D1 理论输入（`u*(a_t)` ＋ `L/U`）仍缺失**（外部交付线）⇒ `distortion_gapwise` 之 `u*`/`u` 实参 ＋ `theory_U_hit_rate` 之理论界供给 **0 在盘** | 高 | **未闭**（`C4` 之一） | **PI 授权 ＋ 外部交付线** |
| **KD-B1** | 🟡 **`bootstrap_ci` 之分位法（**最近秩法 nearest-rank**）＋ `T3`／`T5` 网格档位（`D2_identity_grid_10k` 之 25×50×2×4 具体取档）系**本棒所拟之实现口径**（正典仅给「10k resamples」与项名，⛔ 0 给取档）⇒ 档位改动将使 T3 读数不可逐位复现 | 中 | **未闭 · 本棒推断** | **PI 确认／另给取档** |
| **KD-B2** | 🟡 **`cell_table_row` 之入参键名（`choices`／`key_sets`／`weights`／`h`／`d_bayesian`／`cell_id`）与留痕栏名（`tests_side_correction_note`）系本棒所拟**（设计件仅给签名，⛔ 0 给键名）⇒ 产表接口之消费方须先对键名 | 中 | **未闭 · 本棒推断** | **PI 确认** |
| **KD-B3** | 🟡 **私有辅助函数 6 个**（`_as_fraction`／`_resolve_weights`／`_check_max_u`／`_build_trajectory`／`_multiplier_float_impl`／`_bit_identical`）＋ `_print_report`／`_reconfigure_stdout`／`main` 系本棒为实现 13 签名与 `--self-test` 出口所加（设计件 0 列）⇒ **公开面严格等于 13 签名 ＋ `self_test`**，其余均私有 | 低 | **已登记 · 无阻塞** | **PI 备案** |

### §5-1 本棒 ⛔ 0 作之事项（逐条声明）

① ⛔ **0 开跑**任何实验（0 调 LLM／0 调 API／0 跑 runner）｜② ⛔ **0 建 5 锚 JSON**（`ge01_prereg_5anchor.json` 两命名仍 0 在盘）｜③ ⛔ **0 宣告**①毕／⛔ **0 宣告**`C4` 满足／⛔ **0 宣告**停跑解除｜④ ⛔ **0 代 PI 裁／释／择／确认／给值**（`ε` 之值、`D` 之口径、`H` 之值、`status` 拟值、射程分叉皆留 PI）｜⑤ ⛔ **0 自签生效／0 自签冻结**｜⑥ ⛔ **0 回改**任何既有件一字（触动既有件数 ＝ **0**；`tools/` 既有 5 件字节与 SHA 全部未变）｜⑦ ⛔ **0 覆盖**（落盘前双通道实测该路径 0 在盘）｜⑧ ⛔ **0 读** `.env`／⛔ **0 读** key｜⑨ ⛔ **0 上传**／⛔ **0 远端写**｜⑩ ⛔ **0 移动／0 重命名／0 删除**任何件（`__pycache__` 系本棒复核副产物，移除**前先确认其非在册交付件**，内容仅本棒自建之 `.pyc`）｜⑪ ⛔ **0 以单通道**作阴性判据｜⑫ ⛔ **0 新拟数值阈值**（`T1`–`T9` 之判据皆为照录或代数恒等式）｜⑬ ⛔ **0 沿用**他件自报值（凡引用皆逐字回读源件并标行号）｜⑭ ⛔ **0 断言** PI 卡面原文／卡号。

### §5-2 限制与未核项（如实登记 · 0 隐匿）

1. **阴性结论之射程** ＝ 四根（`deposon-repo`／`deposon-sub`／`.minimax/workspace`／运行时全域 `.minimax`）之 **3,414 件 ＋ 70,312 件**（`os.walk` `onerror` 计数 ＝ **0**）｜⛔ **0 断言**「全机全域 0 命中」。
2. **`f5da17e62b07` 之 0 在盘系转引**（`7551c47d3ece` §5-1 之 census 之转述），⛔ 本棒**0 独立复测**该 SHA（KD-A4）。
3. **`Q12` 之题面与卡面**：本件仅据**派工单元所载语义**（§1-1），⛔ **0 断言**卡面原文逐字、⛔ **0 断言**卡号（KD-A8）。
4. **`b92a7830d38a`（`C2` 裁生效登记面）本棒未开卷**：派工单元记「`C2` 裁生效（`b92a7830d38a`）」，本棒**未逐字回读该件**（不在实现规格之必需依据面）⇒ 本件⛔ **0 复述其内容**，仅据派工转录记其状态。
5. **本棒 0 开卷之面**：GLM 线实验委托回函、`verifier/handoff/` 之锚 JSON（0 在盘）、`verifier/runs/` 之 5 frozen runs 之逐件内容、`_batch8_deliberation_judgment_2026_10_14.md` 全文（仅经内容检索读取其 §1-5／§3-4 之命中片段）。
6. **`nonAscii` 双口径**：本件按「字符／字节」双口径并列自报（§2-3），两口径**不可互换**（3,220 字符 ≠ 9,607 字节，差为 UTF-8 多字节编码所致）。

---

*件止。**①段 · G-E01 `G3` 计算器重建执行登记件**（worker）· 2026-10-14 —— **PI 裁**（派工单转录）：「**甲 授权棒推 G3 计算器重建（设计已成，前置已具）**」（2026-10-14 15:35，⛔ 0 断言卡面原文）｜**重建件**：`tools/distortion_calculator.py` ＝ **`410a12482eef`**／**40,611 B**／UTF-8 无 BOM·纯 LF·TAB=0·CR=0·CTRL=0·U+FFFD=0·nonAscii 3,220 字符／9,607 字节｜**实现规格**：单文件五层 ＋ **13 签名 13/13 逐字命中** ＋ 守卫 `B1`–`B12` ＋ 正典式 **10/10 逐字命中** ＋ `kill_decision` 函数体 **5/5 逐字比对**｜**自测**：**T1–T9 9/9 通过**（退出码 0；首轮 7/9，两处修正已留痕）＋ 守卫负向面 **13/13 raise**｜**阴性结论**：四根 `os.walk`（3,414 ＋ 70,312 件 · 遍历错误 0）＋ `tools/` census 5 件 ⇒ 双通道一致 0 在盘｜**S1–S9**：`S3`／`S4`／`S6` 已毕，`S5` 已测而判据未闭，**`S7` 未执行（0 建锚）**，`S1`／`S9` 未闭，`S2`／`S8` 为转录面｜**KD 共 13 条**（A1–A10 ＋ B1–B3）｜⛔ 0 开跑 · 0 建锚 · 0 宣告①毕 · 0 回改 · 0 覆盖 · 0 代裁 · 0 读 `.env` · 0 上传/0 远端写。署名：**worker**。*
