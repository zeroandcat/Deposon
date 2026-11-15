/-
G7p.lean — G7′ 解耦门 Lean 裁决件（P2′ 复跑）· 2026-11-15
======================================================================
令源：coordinator 14:54:31 派单（PI 14:44:00 令「G7' 由 lean 裁决·G6′ 补位」）。
工具链：Lean 4.15.0 core-only（0 mathlib）。体例沿 NingziContainer 工程注记：
  Rat 不在 core（OfNat Rat 实测 0 命中）→ 全部分数比较经交叉相乘以 Nat 落地、
  decide 机证；通式代数引理以 Nat.mul_add/加法消去律/AC 化简自持。

数据基据（P2′ 读数包 25 件·shared/ops_P2p读数包_2026_11_15/·本机只读实测）：
  · 盲化件 p2p_blind_kh_frozen.json：K_h 32 键冻结集——低半区(k<64) nL=13 键
    ＋高半区(k≥64) nH=19 键（k5/6/7 为显示序前三）。
  · switch 段（v4_2 ops 1,152 条·slot 字段＝键号 0..127 逐键）：
    低半区 op m=971·高半区 op n=181；K_h 命中 a=191（低）/b=53（高）；
    ops 直算 freq ≡ readout freq_post（恒等核毕）。
  · A 主胞（v4_1 freq_pre）：a=360（k5/k6/k7 各 120）/b=0；ops 件仅 smoke 账
    （432 条·0 正式段键级）→ m/n 缺位。
  · KIMI（v4_1 freq_pre）：a=288/b=74（总命中 362）；ops 件仅 smoke 账 → m/n 缺位。

形式化判据（本件钉死·期望校正位主判＋归一位副判）：
  · 完美成员解耦（模型定义）：op 半区分布任意（L2 一般偏好自由·显示序固定
    保连续性＝D1 容忍位），半区内成员中性——给定半区，选中键 ∈ K_h 的边际
    概率＝该半区构成密度（低 13/64·高 19/64）；期望线性 E[a]=m·nL/64、
    E[b]=n·nH/64（指示变量求和·模型层注记·见 SORRY-LEDGER 边界）。
  · A 口径（mock 认证实现沿·A 轨 FAIL 读法）：
      D_A = a/(a+b) − nL/(nL+nH)            〔P(低|K_h 命中)−构成份额〕
  · 解耦期望偏置（A 口径在完美解耦下的 plug-in 期望）：
      bias(m,n) = m·nL/(m·nL+n·nH) − nL/(nL+nH)
  · 耦合分量（期望校正·本裁决主判据）：
      κ = a/(a+b) − m·nL/(m·nL+n·nH)
    完美解耦下 plug-in 锚 κ=0；κ 非零 ⟺ 成员-序数耦合检出。
  · B 归一口径（比值差·副判据·B 轨双口径的归一位）：
      B_norm = (b/n)/(nH/64) − (a/m)/(nL/64)
  · B 原始口径（注册文本字面直读·B 轨原始位）：
      B_raw = b/n − a/m（解耦期望＝(nH−nL)/64＝构成不对称位）

交叉相乘语义（分母恒正）：x/p > t/u ⟺ u·x > t·p（差式先通分）。
代数核心（通式引理证）：κ 与 B_norm 同零位点＝2×2 表（半区×K_h 命中）
  独立性方程 a·n·nH = b·m·nL（kappa_zero_iff_indep）。
-/

-- ================================================================
-- §1 形式化定义（交叉相乘谓词·分母恒正下与分数比较等价）
-- ================================================================

/-- A 口径 D_A = a/(a+b) − nL/(nL+nH) > t/u
    ⟺ u·a·(nL+nH) > t·(a+b)·(nL+nH) + u·nL·(a+b) -/
abbrev aCaliberGT (a b nL nH t u : Nat) : Prop :=
  u * a * (nL + nH) > t * (a + b) * (nL + nH) + u * nL * (a + b)

/-- 解耦期望偏置 bias = m·nL/(m·nL+n·nH) − nL/(nL+nH) > t/u
    ⟺ u·m·nL·(nL+nH) > t·(m·nL+n·nH)·(nL+nH) + u·nL·(m·nL+n·nH) -/
abbrev aBiasGT (m n nL nH t u : Nat) : Prop :=
  u * m * nL * (nL + nH) > t * (m * nL + n * nH) * (nL + nH) + u * nL * (m * nL + n * nH)

/-- 耦合分量 κ = a/(a+b) − m·nL/(m·nL+n·nH) > t/u
    ⟺ u·a·(m·nL+n·nH) > t·(a+b)·(m·nL+n·nH) + u·m·nL·(a+b) -/
abbrev kappaGT (a b m n nL nH t u : Nat) : Prop :=
  u * a * (m * nL + n * nH) > t * (a + b) * (m * nL + n * nH) + u * m * nL * (a + b)

/-- κ ≤ t/u ⟺ u·a·(m·nL+n·nH) ≤ t·(a+b)·(m·nL+n·nH) + u·m·nL·(a+b) -/
abbrev kappaLE (a b m n nL nH t u : Nat) : Prop :=
  u * a * (m * nL + n * nH) ≤ t * (a + b) * (m * nL + n * nH) + u * m * nL * (a + b)

/-- κ ≥ −t/u ⟺ u·m·nL·(a+b) ≤ t·(a+b)·(m·nL+n·nH) + u·a·(m·nL+n·nH) -/
abbrev kappaGE (a b m n nL nH t u : Nat) : Prop :=
  u * m * nL * (a + b) ≤ t * (a + b) * (m * nL + n * nH) + u * a * (m * nL + n * nH)

/-- κ = 0 ⟺ a·(m·nL+n·nH) = m·nL·(a+b) -/
abbrev kappaZero (a b m n nL nH : Nat) : Prop :=
  a * (m * nL + n * nH) = m * nL * (a + b)

/-- B 归一口径 B_norm = 64·b/(n·nH) − 64·a/(m·nL) ≤ t/u
    ⟺ u·64·b·m·nL ≤ t·n·nH·m·nL + u·64·a·n·nH -/
abbrev bNormLE (a b m n nL nH t u : Nat) : Prop :=
  u * 64 * b * m * nL ≤ t * n * nH * m * nL + u * 64 * a * n * nH

/-- B_norm ≥ −t/u ⟺ u·64·a·n·nH ≤ t·n·nH·m·nL + u·64·b·m·nL -/
abbrev bNormGE (a b m n nL nH t u : Nat) : Prop :=
  u * 64 * a * n * nH ≤ t * n * nH * m * nL + u * 64 * b * m * nL

/-- B 原始口径 B_raw = b/n − a/m ≤ t/u ⟺ u·b·m ≤ t·n·m + u·a·n -/
abbrev bRawLE (a b m n t u : Nat) : Prop :=
  u * b * m ≤ t * n * m + u * a * n

-- ================================================================
-- §2 通式引理（一般性·非数据点）
-- ================================================================

/-- 通式① A 口径 null 的均匀充分条件：op 半区均匀（m=n=M）时
    解耦期望偏置为零（交叉相乘方程成立）——AC 化简机证。 -/
theorem aBias_zero_of_uniform (M nL nH : Nat) :
    M * nL * (nL + nH) = nL * (M * nL + M * nH) := by
  simp [Nat.mul_add, Nat.add_mul, Nat.mul_assoc, Nat.mul_left_comm, Nat.mul_comm]

/-- 通式② A 口径 null 的均匀必要条件（取消律）：解耦期望偏置为零
    ⟹ op 半区均匀 m=n（nL·nH 正）。即：op 分布非均匀时 A 口径解耦
    期望必不为零——A 口径 null 仅在 op 位置均匀时成立（机器证）。 -/
theorem uniform_of_aBias_zero (m n nL nH : Nat) (hnL : 0 < nL) (hnH : 0 < nH)
    (h : m * nL * (nL + nH) = nL * (m * nL + n * nH)) : m = n := by
  have e1 : m * nL * (nL + nH) = m * nL * nL + m * nL * nH := Nat.mul_add _ _ _
  have e2 : nL * (m * nL + n * nH) = nL * (m * nL) + nL * (n * nH) := Nat.mul_add _ _ _
  rw [e1, e2] at h
  have e3 : nL * (m * nL) = m * nL * nL := by
    simp [Nat.mul_comm, Nat.mul_assoc, Nat.mul_left_comm]
  rw [e3] at h
  have e4 : nL * (n * nH) = n * nH * nL := by
    simp [Nat.mul_comm, Nat.mul_assoc, Nat.mul_left_comm]
  rw [e4] at h
  have h5 : m * nL * nH = n * nH * nL := Nat.add_left_cancel h
  have e6 : m * nL * nH = m * (nL * nH) := Nat.mul_assoc m nL nH
  have e7 : n * nH * nL = n * (nH * nL) := Nat.mul_assoc n nH nL
  have e8 : nH * nL = nL * nH := Nat.mul_comm _ _
  rw [e6, e7, e8] at h5
  exact Nat.eq_of_mul_eq_mul_right (Nat.mul_pos hnL hnH) h5

/-- 通式③ 耦合分量零位点＝2×2 独立性：κ=0 ⟺ a·(n·nH) = (m·nL)·b
    （半区×K_h 命中列联表独立方程；B 归一口径同零位点——两判据
    检同一耦合·仅归一化分母不同）。 -/
theorem kappa_zero_iff_indep (a b m n nL nH : Nat) :
    kappaZero a b m n nL nH ↔ (a * (n * nH) = (m * nL) * b) := by
  constructor
  · intro h
    unfold kappaZero at h
    have e1 : a * (m * nL + n * nH) = a * (m * nL) + a * (n * nH) := Nat.mul_add _ _ _
    have e2 : m * nL * (a + b) = m * nL * a + m * nL * b := Nat.mul_add _ _ _
    rw [e1, e2] at h
    have e3 : a * (m * nL) = m * nL * a := by
      simp [Nat.mul_comm, Nat.mul_assoc, Nat.mul_left_comm]
    rw [e3] at h
    exact Nat.add_left_cancel h
  · intro h
    unfold kappaZero
    have e1 : a * (m * nL + n * nH) = a * (m * nL) + a * (n * nH) := Nat.mul_add _ _ _
    have e2 : m * nL * (a + b) = m * nL * a + m * nL * b := Nat.mul_add _ _ _
    have e3 : a * (m * nL) = m * nL * a := by
      simp [Nat.mul_comm, Nat.mul_assoc, Nat.mul_left_comm]
    rw [e1, e2, e3, ← h]

-- ================================================================
-- §3 switch 段数据定理（a=191 b=53 m=971 n=181 nL=13 nH=19·decide 机证）
-- ================================================================

/-- S1〔A 轨读法复现〕A 口径实测 D_A = 191/244 − 13/32 = 735/1952 ≈ 0.3765 > 0.10。
    两轨复算恒等位（A 轨 0.377·B 轨副签 0.3765）。 -/
theorem g7p_switch_aCal_gt_tenth : aCaliberGT 191 53 13 19 1 10 := by decide

/-- S2〔A 口径无效性见证·本裁决核心〕完美成员解耦下（期望锚
    m·nL/(m·nL+n·nH) = 12623/16062），A 口径期望偏置
    = 12623/16062 − 13/32 = 195130/513984 ≈ +0.3796 仍 > 0.10——
    即：对完美解耦模型，A 口径在本 op 分布（971/181）下必 FAIL。
    A 口径超阈信号不可归因于耦合失败（≈100% 系 L2 一般偏好混淆）。 -/
theorem g7p_switch_aBias_gt_tenth : aBiasGT 971 181 13 19 1 10 := by decide

/-- S3〔null 方程不成立〕观测 op 分布（m=971≠n=181）下解耦 null
    交叉相乘方程不成立（通式②逆否实例）。 -/
theorem g7p_switch_null_eq_false : ¬ (971 * 13 * 32 = 13 * (971 * 13 + 181 * 19)) := by decide

/-- S4〔主判据·注册阈〕耦合分量 κ = 191/244 − 12623/16062
    = −12170/3919128 ≈ −0.00311，|κ| ≤ 0.10（且 S5 紧界 ≤ 0.01）。
    耦合分量≈0：无成员-序数耦合检出（解耦相容）。 -/
theorem g7p_switch_kappa_le_tenth : kappaLE 191 53 971 181 13 19 1 10 := by decide
theorem g7p_switch_kappa_ge_ntenth : kappaGE 191 53 971 181 13 19 1 10 := by decide

/-- S5〔主判据·紧界〕|κ| ≤ 0.01（距注册阈 0.10 十倍冗余）。 -/
theorem g7p_switch_kappa_le_hundredth : kappaLE 191 53 971 181 13 19 1 100 := by decide
theorem g7p_switch_kappa_ge_nhundredth : kappaGE 191 53 971 181 13 19 1 100 := by decide

/-- S6〔副判据·B 归一位〕B_norm = 64·(53·971·13 − 191·181·19)/(181·19·971·13)
    = 778880/43410497 ≈ +0.01794，|B_norm| ≤ 0.10（符号正·S6c）。
    与 κ 同零位点（通式③）·同判一致。 -/
theorem g7p_switch_bNorm_le_tenth : bNormLE 191 53 971 181 13 19 1 10 := by decide
theorem g7p_switch_bNorm_ge_ntenth : bNormGE 191 53 971 181 13 19 1 10 := by decide
theorem g7p_switch_bNorm_pos : 191 * 181 * 19 ≤ 53 * 971 * 13 := by decide

/-- S7〔B 原始位〕B_raw = 53/181 − 191/971 = 16892/175751 ≈ 0.09611 ≤ 0.10
    （贴阈·距阈 6831/521461）；解耦期望原始差 = (nH−nL)/64 = 6/64 =
    0.09375 ≤ 0.10（阈盲位：完美解耦下原始差即占阈 94%——原始位
    无分离力·须归一·见 S6）。 -/
theorem g7p_switch_bRaw_le_tenth : bRawLE 191 53 971 181 1 10 := by decide
theorem g7p_decoupled_bRaw_expected_le : (6 : Nat) * 10 ≤ 64 * 1 := by decide

-- ================================================================
-- §4 A 主胞 / KIMI 段：κ 非可辨识（m/n 缺位）见证对·decide 机证
-- ================================================================

/- 可行性约束注记（见证合法性）：任一 (m,n) 见证须满足 m ≥ a、n ≥ b、
   m+n ≥ a+b（K_h 命中是 op 的子集）。下述见证全满足：
   (1440,0)≥(360,0)·(720,720)≥(360,0)·(720,720)≥(288,74)·(575,100)≥(288,74)。 -/

/-- A1〔解耦相容见证〕A 主胞（a=360 b=0）：取 m=1440·n=0（全 op 低半区·
    极端 L2 偏好态·可行性满足）→ κ = 360/360 − 18720/18720 = 0。
    同一 (a,b) 下存在完美解耦相容的 op 分布使 κ=0。 -/
theorem g7p_amain_kappa_zero_witness : kappaZero 360 0 1440 0 13 19 := by decide

/-- A2〔耦合需求见证〕同一 (a=360 b=0)：取 m=720·n=720（均匀 op）→
    κ = D_A = 360/360 − 13/32 = 27/32 ≈ 0.594 > 0.10。
    同一 (a,b) 下亦存在 op 分布使 κ 超阈。
    A1×A2 ⟹ m/n 缺位时 κ 非可辨识（不可判·非静默）。 -/
theorem g7p_amain_kappa_gt_witness : kappaGT 360 0 720 720 13 19 1 10 := by decide

/-- K1〔耦合需求见证〕KIMI（a=288 b=74）：m=720·n=720（均匀）→
    κ = D_A = 288/362 − 13/32 ≈ +0.389 > 0.10。 -/
theorem g7p_kimi_kappa_gt_witness : kappaGT 288 74 720 720 13 19 1 10 := by decide

/-- K2〔解耦相容见证〕同一 (a=288 b=74)：取 m=575·n=100
    （可行性：575≥288·100≥74·675≥362）→
    κ = 288/362 − 7475/9375 = −5940/3393750 ≈ −0.00175，|κ| ≤ 0.01。
    K1×K2 ⟹ KIMI 段 κ 非可辨识。 -/
theorem g7p_kimi_kappa_le_witness : kappaLE 288 74 575 100 13 19 1 100 := by decide
theorem g7p_kimi_kappa_ge_witness : kappaGE 288 74 575 100 13 19 1 100 := by decide

-- ================================================================
-- §5 裁决一行化（定理群的一行化读出·语义位·判读见裁决件 md）
-- ================================================================

/- G7′ Lean 裁决：switch 段——|κ| ≤ 0.01（S4/S5）且 |B_norm| ≤ 0.10（S6）→
   过（无成员-序数耦合检出·A 口径 FAIL 系 L2 混淆所致·S2 见证口径无效性）；
   A 主胞/KIMI 段——κ 非可辨识（m/n 缺位·A1×A2/K1×K2 见证对）→ 不可判
   （补 per-op 键级数据后可判·G6′ 补位令同向）。
   判据终裁：G7′ 门判采耦合分量判据 κ（期望校正位）·B 归一位同零位点互证；
   A 口径（mock 认证位）null 仅在 op 均匀时成立（通式①②）·在非均匀 op
   分布下无解耦检验效度（S2）——两轨口径差就此终裁。 -/

-- ================================================================
-- §6 SORRY-LEDGER（证明债台账·本件结算）
-- ================================================================

/- 本件 sorry 数：0（零新增编译债·build log 全绿）。
   已证（proved）清单：
     通式：aBias_zero_of_uniform（均匀→null·AC 化简）
           uniform_of_aBias_zero（null→均匀·取消律）
           kappa_zero_iff_indep（κ 零位点＝2×2 独立·两判据同核）
     switch：S1–S7 共 11 定理（decide 机证）
     非可辨识：A1/A2/K1/K2 共 5 定理（decide 机证）
   模型层注记（非 Lean 证·定义桥接位）：完美成员解耦的期望线性
     E[a]=m·nL/64、E[b]=n·nH/64 系解耦定义（给定半区成员中性）的
     指示变量线性推论；κ 以 plug-in 锚（m·nL/(m·nL+n·nH)）落地，
     其与期望的偏差属抽样噪声位（switch 段两半区超额 −0.50σ/−0.12σ·
     读数包复算在册·噪声带内）。
   边界注记：Rat/ℝ 不在 core 4.15（OfNat Rat 0 命中·NingziContainer
     体例沿）——分数比较全经交叉相乘 Nat 落地。
   邻件边界：NingziContainer（7e7025294bd6）在册 3 sorry 系其预注册
     债位（债2/3/4）；本件 0 import 邻件·0 连坐。
   关键定理公理依赖核验（#print axioms 输出见 build log）：
     全部定理 0 sorryAx·0 custom axiom。 -/

#print axioms aBias_zero_of_uniform
#print axioms uniform_of_aBias_zero
#print axioms kappa_zero_iff_indep
#print axioms g7p_switch_aBias_gt_tenth
#print axioms g7p_switch_kappa_le_tenth
#print axioms g7p_switch_kappa_le_hundredth
#print axioms g7p_switch_bNorm_le_tenth
#print axioms g7p_amain_kappa_zero_witness
#print axioms g7p_amain_kappa_gt_witness
#print axioms g7p_kimi_kappa_gt_witness
#print axioms g7p_kimi_kappa_le_witness
