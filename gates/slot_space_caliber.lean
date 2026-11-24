/-
slot_space_caliber.lean — slot 空间口径门 Lean 镜像面（插件 preview.9 接口 F·2026-11-24）
======================================================================
对应 Python 可执行面：gates/slot_space_caliber.py（mock 向量 9/9·CI 门步）
＋ mocks/slot_space_vectors.json（发布向量·纯数零网络）。
preview.7/8 状态：接口 F 为 Python-only 面（送审件「Lean 镜像候选」）——本件补齐
双实现口径（judgment_v11.lean 先例沿：core-only·0 sorry·0 mathlib·0 外部数据）。

口径钉死（与 Python 面逐项对表）：
  F1 中心口径（主判带·裁决）：share = pos_term / moment ≤ 1/2（含等）⇒ 离散读数成立；
     share > 1/2 ⇒ INVALID（报告的统计量过半是中心偏移项·非离散度·须重算）。
     矩分解恒等式 E[(x−c)²] = Var(x) + (mean−c)² 的整数落地（Rat 不在 core）：
       n · Σ(xᵢ−c)² = (n·Σxᵢ² − S²) + (S − n·c)²     其中 S = Σxᵢ, n = 观测数
     share = (S−n·c)² / (n·Σ(xᵢ−c)²)  ⇒  share ≤ 1/2 ↔ 2·pos ≤ n·moment ↔ pos ≤ var。
  F2 槽空间成员（主判带·裁决）：每槽 ∈ [0, space_hi]；违例 ⇒ INVALID（先于 F1）。
  F3 比值口径（参照带·永不裁决）：ratio_true = var_true / uniform_var；
     ratio_defective = moment / uniform_var 并列报告（Lean 面不裁决·Python 面报告）。
  退化位：n = 0 ⇒ INCONCLUSIVE；moment = 0 ⇒ share := 0（恰在中心·与 2·pos ≤ n·moment
  退化式同判 VALID——机证 pos = var = 0）。
  半整数中心：c = 63.5 类中心以「倍化」表示（x ↦ 2x, c ↦ 2c）——T5 机证 share 带、
  成员位、判决在倍化下不变（k ≠ 0）·故 D1／f8j 锚以倍化列表＋整数中心 127 入向量。

工程注记：core-only 环境无 ring/ring_nf（mathlib）——非线性积经 `alg` 规范集
（乘法分配＋字面 2 展为加法＋AC 规范形）化为原子线性式后由 omega 收口；
`Nat.cast_add`/`two_mul` 等系 mathlib 名（core 无）→ 自备 two_mulI/mul_twoI＋Int.natCast_add。
-/

set_option maxRecDepth 100000

-- ===== 基元 ==============================================================
def sq (x : Int) : Int := x * x

def sumSq : List Int → Int
  | [] => 0
  | x :: xs => sq x + sumSq xs

def sumL : List Int → Int
  | [] => 0
  | x :: xs => x + sumL xs

/-- 中心平移：(x − c) 逐元 -/
def shiftL (c : Int) : List Int → List Int
  | [] => []
  | x :: xs => (x - c) :: shiftL c xs

/-- 报告二阶矩（未除 n）：Σ(xᵢ−c)² -/
def moment (L : List Int) (c : Int) : Int := sumSq (shiftL c L)

/-- 方差分子口径（中心无关）：n·Σxᵢ² − S² ＝ n²·Var(x) -/
def varNum (L : List Int) : Int := (L.length : Int) * sumSq L - sq (sumL L)

/-- 位置项分子口径：(S − n·c)² ＝ n²·(mean − c)² -/
def posNum (L : List Int) (c : Int) : Int := sq (sumL L - (L.length : Int) * c)

theorem two_mulI (a : Int) : 2 * a = a + a := by omega
theorem mul_twoI (a : Int) : a * 2 = a + a := by rw [Int.mul_comm]; exact two_mulI a

/-- 代数规范化集（非线性乘积原子化·字面 2 展为加法·AC 规范形） -/
macro "alg" : tactic => `(tactic| simp only [Int.sub_mul, Int.mul_sub, Int.mul_add, Int.add_mul,
  two_mulI, mul_twoI, Int.one_mul, Int.mul_one, Int.mul_assoc, Int.mul_left_comm, Int.mul_comm,
  Int.natCast_add, Int.natCast_one, List.length_cons])

-- ===== 引理：平移后的和／平方和 ==================================================
theorem sumL_shiftL (c : Int) (L : List Int) :
    sumL (shiftL c L) = sumL L - (L.length : Int) * c := by
  induction L with
  | nil => simp [shiftL, sumL]
  | cons x xs ih => simp only [shiftL, sumL, ih] <;> (alg <;> try omega)

theorem sumSq_shiftL (c : Int) (L : List Int) :
    sumSq (shiftL c L) = sumSq L - 2 * c * sumL L + (L.length : Int) * sq c := by
  induction L with
  | nil => simp [shiftL, sumSq, sumL]
  | cons x xs ih => simp only [shiftL, sumSq, sumL, sq, ih] <;> (alg <;> try omega)

-- ===== T1 矩分解恒等式 ========================================================
/-- T1：n·Σ(xᵢ−c)² = (n·Σxᵢ² − S²) + (S − n·c)² —— E[(x−c)²] = Var + (mean−c)² 的整数口径 -/
theorem moment_decomposition (L : List Int) (c : Int) :
    (L.length : Int) * moment L c = varNum L + posNum L c := by
  simp only [moment]
  rw [sumSq_shiftL c L]
  simp only [varNum, posNum, sq]
  alg
  omega

-- ===== T2 share 带 ⇔ pos ≤ var ==============================================
/-- T2：share ≤ 1/2（含等）↔ 位置项分子 ≤ 方差分子（判死线两侧只看两分子） -/
theorem share_half_iff (L : List Int) (c : Int) :
    (2 * posNum L c ≤ (L.length : Int) * moment L c) ↔ (posNum L c ≤ varNum L) := by
  have h := moment_decomposition L c
  omega

/-- T2′：share < 1/2（严格）↔ pos < var -/
theorem share_lt_half_iff (L : List Int) (c : Int) :
    (2 * posNum L c < (L.length : Int) * moment L c) ↔ (posNum L c < varNum L) := by
  have h := moment_decomposition L c
  omega

theorem sq_nonneg (x : Int) : 0 ≤ sq x := by
  rcases Int.le_total 0 x with h | h
  · exact Int.mul_nonneg h h
  · have hn : 0 ≤ -x := Int.neg_nonneg_of_nonpos h
    have := Int.mul_nonneg hn hn
    simpa [sq, Int.neg_mul_neg] using this

theorem posNum_nonneg (L : List Int) (c : Int) : 0 ≤ posNum L c := sq_nonneg _

-- ===== T3 边界含等 / 刚过半 ========================================================
theorem sq_pos_of_ne_zero {k : Int} (hk : k ≠ 0) : 0 < sq k := by
  have h1 : 0 ≤ k * k := sq_nonneg k
  have h2 : k * k ≠ 0 := by
    intro h
    rcases Int.mul_eq_zero.mp h with h0 | h0
    · exact hk h0
    · exact hk h0
  unfold sq at *
  omega

/-- T3a 边界含等：pos = var ⇒ share 恰 1/2 ⇒ 带内（VALID·非 KILL） -/
theorem boundary_half_holds {L : List Int} {c : Int} (h : posNum L c = varNum L) :
    2 * posNum L c ≤ (L.length : Int) * moment L c := by
  have h1 := moment_decomposition L c
  have h2 := posNum_nonneg L c
  omega

/-- T3b 刚过半：pos > var（整数域即 ≥ var+1）⇒ share > 1/2 ⇒ 越线（KILL·无浮点比较） -/
theorem just_over_half_kills {L : List Int} {c : Int} (h : varNum L < posNum L c) :
    ¬ 2 * posNum L c ≤ (L.length : Int) * moment L c := by
  have h1 := moment_decomposition L c
  omega

-- ===== T4 退化位（moment = 0 ⇔ 全部恰在中心）====================================
theorem sumSq_nonneg : ∀ (L : List Int), 0 ≤ sumSq L
  | [] => by simp [sumSq]
  | x :: xs => by
      simp only [sumSq]
      have := sq_nonneg x
      have := sumSq_nonneg xs
      omega

theorem sumSq_eq_zero_implies_all_zero : ∀ (L : List Int), sumSq L = 0 → ∀ x ∈ L, x = 0
  | [], _, x, hx => absurd hx (List.not_mem_nil x)
  | y :: ys, h, x, hx => by
      simp only [sumSq] at h
      have hy : sq y = 0 := by
        have := sq_nonneg y
        have := sumSq_nonneg ys
        omega
      have hy0 : y = 0 := (Int.mul_eq_zero.mp hy).elim id id
      have hrest : sumSq ys = 0 := by
        have := sq_nonneg y
        have := sumSq_nonneg ys
        omega
      rcases List.mem_cons.mp hx with h' | h'
      · rw [h', hy0]
      · exact sumSq_eq_zero_implies_all_zero ys hrest x h'

theorem sumL_zero_of_all_zero {L : List Int} (h : ∀ x ∈ L, x = 0) : sumL L = 0 := by
  induction L with
  | nil => simp [sumL]
  | cons x xs ih =>
      have hx : x = 0 := h x (List.mem_cons_self x xs)
      have hrest : ∀ y ∈ xs, y = 0 := fun y hy => h y (List.mem_cons_of_mem x hy)
      simp [sumL, hx, ih hrest]

/-- T4：moment = 0 ⇒ pos = 0 ∧ var = 0（退化式与「share := 0」约定同判 VALID） -/
theorem degenerate_at_center {L : List Int} {c : Int} (h : moment L c = 0) :
    posNum L c = 0 ∧ varNum L = 0 := by
  have hall : ∀ x ∈ shiftL c L, x = 0 :=
    sumSq_eq_zero_implies_all_zero (shiftL c L) h
  have hs : sumL (shiftL c L) = 0 := sumL_zero_of_all_zero hall
  have h1 : sumL L - (L.length : Int) * c = 0 := by
    rw [sumL_shiftL c L] at hs
    omega
  have hz : sumL L - (L.length : Int) * c = 0 := h1
  have hp : posNum L c = 0 := by
    simp only [posNum, hz, sq, Int.mul_zero]
  have hv : varNum L = 0 := by
    have t := moment_decomposition L c
    rw [h] at t
    simp only [Int.mul_zero] at t
    omega
  exact ⟨hp, hv⟩

-- ===== T5 倍化不变（半整数中心表示的合法性）====================================
def scaleL (k : Int) (L : List Int) : List Int := L.map (fun x => k * x)

theorem len_scaleL (k : Int) (L : List Int) : (scaleL k L).length = L.length := by simp [scaleL]

theorem shift_scaleL (k : Int) (c : Int) (L : List Int) :
    shiftL (k * c) (scaleL k L) = scaleL k (shiftL c L) := by
  unfold scaleL
  induction L with
  | nil => rfl
  | cons x xs ih => simp only [shiftL, List.map_cons, ih, Int.mul_sub] <;> (try rfl)

theorem sumSq_scaleL (k : Int) (L : List Int) : sumSq (scaleL k L) = sq k * sumSq L := by
  unfold scaleL
  induction L with
  | nil => simp [sumSq]
  | cons x xs ih => simp only [List.map_cons, sumSq, sq, ih] <;> (alg <;> try omega)

theorem sumL_scaleL (k : Int) (L : List Int) : sumL (scaleL k L) = k * sumL L := by
  unfold scaleL
  induction L with
  | nil => simp [sumL]
  | cons x xs ih => simp only [List.map_cons, sumL, ih] <;> (alg <;> try omega)

theorem moment_scale (k : Int) (L : List Int) (c : Int) :
    moment (scaleL k L) (k * c) = sq k * moment L c := by
  simp only [moment, shift_scaleL, sumSq_scaleL]

theorem posNum_scale (k : Int) (L : List Int) (c : Int) :
    posNum (scaleL k L) (k * c) = sq k * posNum L c := by
  simp only [posNum, len_scaleL, sumL_scaleL, sq] <;> (alg <;> try omega)

/-- T5c：share 带在倍化下不变（k ≠ 0）——倍化表示合法的核心 -/
theorem share_band_scale_invariant {k : Int} (hk : k ≠ 0) (L : List Int) (c : Int) :
    (2 * posNum (scaleL k L) (k * c) ≤ ((scaleL k L).length : Int) * moment (scaleL k L) (k * c))
      ↔ (2 * posNum L c ≤ (L.length : Int) * moment L c) := by
  rw [moment_scale, posNum_scale, len_scaleL]
  have hpos : 0 < sq k := sq_pos_of_ne_zero hk
  have hnn : 0 ≤ sq k := Int.le_of_lt hpos
  have norm : ∀ (a b : Int),
      (2 * (sq k * a) ≤ (L.length : Int) * (sq k * b)) ↔ (sq k * (2 * a) ≤ sq k * ((L.length : Int) * b)) := by
    intro a b
    simp only [Int.mul_assoc, Int.mul_left_comm, Int.mul_comm]
  constructor
  · intro h
    have h' : sq k * (2 * posNum L c) ≤ sq k * ((L.length : Int) * moment L c) :=
      (norm (posNum L c) (moment L c)).mp h
    exact Int.le_of_mul_le_mul_left h' hpos
  · intro h
    have h' : sq k * (2 * posNum L c) ≤ sq k * ((L.length : Int) * moment L c) :=
      Int.mul_le_mul_of_nonneg_left h hnn
    exact (norm (posNum L c) (moment L c)).mpr h'

-- ===== F2 成员位 ============================================================
/-- 成员位倍化不变：0 ≤ 2x ≤ 2·hi ↔ 0 ≤ x ≤ hi -/
theorem membership_scale2 (x hi : Int) :
    (0 ≤ 2 * x ∧ 2 * x ≤ 2 * hi) ↔ (0 ≤ x ∧ x ≤ hi) := by omega

theorem membership_decide_scale2 (x hi : Int) :
    (decide (0 ≤ 2 * x) && decide (2 * x ≤ 2 * hi)) = (decide (0 ≤ x) && decide (x ≤ hi)) := by
  have e : decide (0 ≤ 2 * x ∧ 2 * x ≤ 2 * hi) = decide (0 ≤ x ∧ x ≤ hi) := by
    simp only [decide_eq_decide]
    exact membership_scale2 x hi
  simpa only [Bool.decide_and] using e

theorem membership_scale2_list (L : List Int) (hi : Int) :
    (scaleL 2 L).all (fun x => 0 ≤ x && x ≤ 2 * hi) = L.all (fun x => 0 ≤ x && x ≤ hi) := by
  unfold scaleL
  induction L with
  | nil => rfl
  | cons x xs ih => simp only [List.map_cons, List.all_cons, membership_decide_scale2, ih, Bool.and_assoc]

-- ===== 判决函数（Python 面 verdict 同构）========================================
inductive FVerdict where
  | VALID
  | INVALID
  | INCONCLUSIVE
deriving DecidableEq, Repr

/-- 接口 F 判决：n=0 → INCONCLUSIVE；成员违例 → INVALID（先于 F1）；F1 主判带 → VALID/INVALID -/
def verdictF (hi : Int) (L : List Int) (c : Int) : FVerdict :=
  if L.isEmpty then FVerdict.INCONCLUSIVE
  else if !(L.all (fun x => 0 ≤ x && x ≤ hi)) then FVerdict.INVALID
  else if 2 * posNum L c ≤ (L.length : Int) * moment L c then FVerdict.VALID
  else FVerdict.INVALID

theorem verdict_empty (hi : Int) (c : Int) : verdictF hi [] c = FVerdict.INCONCLUSIVE := by
  simp [verdictF]

/-- 成员违例先于口径位：含越界槽 ⇒ INVALID（无论 share） -/
theorem out_of_space_kills {hi : Int} {L : List Int} {c : Int}
    (hne : L ≠ []) (hviol : ¬ L.all (fun x => 0 ≤ x && x ≤ hi)) :
    verdictF hi L c = FVerdict.INVALID := by
  have hf : (L.all (fun x => 0 ≤ x && x ≤ hi)) = false := by
    simpa using hviol
  simp [verdictF, List.isEmpty_eq_false.mpr hne, hf]

/-- 无成员违例时 F1 主判带裁决 -/
theorem verdict_in_space {hi : Int} {L : List Int} {c : Int}
    (hne : L ≠ []) (hin : L.all (fun x => 0 ≤ x && x ≤ hi)) :
    verdictF hi L c =
      (if 2 * posNum L c ≤ (L.length : Int) * moment L c then FVerdict.VALID
       else FVerdict.INVALID) := by
  simp [verdictF, List.isEmpty_eq_false.mpr hne, hin]

theorem boundary_half_valid {hi : Int} {L : List Int} {c : Int}
    (hne : L ≠ []) (hin : L.all (fun x => 0 ≤ x && x ≤ hi)) (h : posNum L c = varNum L) :
    verdictF hi L c = FVerdict.VALID := by
  rw [verdict_in_space hne hin]
  rw [if_pos (boundary_half_holds h)]

theorem just_over_half_invalid {hi : Int} {L : List Int} {c : Int}
    (hne : L ≠ []) (hin : L.all (fun x => 0 ≤ x && x ≤ hi)) (h : varNum L < posNum L c) :
    verdictF hi L c = FVerdict.INVALID := by
  rw [verdict_in_space hne hin]
  rw [if_neg (just_over_half_kills h)]

/-- 倍化后判决不变（hi 同倍·非空） -/
theorem verdict_scale2 {hi : Int} {L : List Int} {c : Int} (hne : L ≠ []) :
    verdictF (2 * hi) (scaleL 2 L) (2 * c) = verdictF hi L c := by
  have hall : (scaleL 2 L).all (fun x => 0 ≤ x && x ≤ 2 * hi) = L.all (fun x => 0 ≤ x && x ≤ hi) :=
    membership_scale2_list L hi
  have hne' : scaleL 2 L ≠ [] := by
    intro hc
    apply hne
    have hl := len_scaleL 2 L
    rw [hc] at hl
    simp only [List.length_nil] at hl
    exact List.length_eq_zero.mp hl.symm
  by_cases hv : L.all (fun x => 0 ≤ x && x ≤ hi)
  · have hv' : (scaleL 2 L).all (fun x => 0 ≤ x && x ≤ 2 * hi) := by rw [hall]; exact hv
    rw [verdict_in_space hne hv, verdict_in_space hne' hv']
    simp only [← share_band_scale_invariant (k := 2) (by decide) L c, len_scaleL]
  · rw [out_of_space_kills hne hv]
    have hv' : ¬ (scaleL 2 L).all (fun x => 0 ≤ x && x ≤ 2 * hi) := by rw [hall]; exact hv
    rw [out_of_space_kills hne' hv']

/-- 退化（moment = 0）⇒ 判决 VALID 且 pos = var = 0（与 Python 面「share := 0」同判） -/
theorem degenerate_valid {hi : Int} {L : List Int} {c : Int}
    (hne : L ≠ []) (hin : L.all (fun x => 0 ≤ x && x ≤ hi)) (h : moment L c = 0) :
    verdictF hi L c = FVerdict.VALID ∧ posNum L c = 0 ∧ varNum L = 0 := by
  obtain ⟨hp, hv⟩ := degenerate_at_center h
  rw [verdict_in_space hne hin, if_pos (by rw [h, hp]; simp)]
  exact ⟨rfl, hp, hv⟩

-- ===== 向量锚（mocks/slot_space_vectors.json 同数·decide 0 公理）================
-- D1 G2/V3R3 R1 枚举坍缩 {0..11}（中心 63.5 → 倍化列表＋中心 127）→ INVALID·share 40368/40511
def d1d : List Int := [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]

theorem d1_is_scale_of_raw : scaleL 2 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] = d1d := by decide
theorem d1_verdict : verdictF 254 d1d 127 = FVerdict.INVALID := by decide
theorem d1_pos : posNum d1d 127 = 1937664 := by decide
theorem d1_var : varNum d1d = 6864 := by decide
theorem d1_moment : moment d1d 127 = 162044 := by decide
/-- share ＝ 40368/40511（交叉相乘恒等） -/
theorem d1_share_fraction : 40511 * posNum d1d 127 = 40368 * (12 * moment d1d 127) := by decide
theorem d1_share_over_half : 40511 * 2 * posNum d1d 127 > 40511 * (12 * moment d1d 127) := by decide
theorem d1_pos_exceeds_var : posNum d1d 127 > varNum d1d := by decide

-- f8j call04 合法锚（slots [20,96,88,66,62,89,25,87,0,69,86,83]·中心 63.5）→ VALID·share 27/44764
def f8jd : List Int := [40, 192, 176, 132, 124, 178, 50, 174, 0, 138, 172, 166]

theorem f8j_is_scale_of_raw :
    scaleL 2 [20, 96, 88, 66, 62, 89, 25, 87, 0, 69, 86, 83] = f8jd := by decide
theorem f8j_verdict : verdictF 254 f8jd 127 = FVerdict.VALID := by decide
theorem f8j_share_fraction : 44764 * posNum f8jd 127 = 27 * (12 * moment f8jd 127) := by decide
theorem f8j_pos : posNum f8jd 127 = 324 := by decide
theorem f8j_var : varNum f8jd = 536844 := by decide

-- 边界 share = 1/2（slots [0,2]·整数中心 2）→ VALID（含等）
theorem boundary_half_verdict : verdictF 127 [0, 2] 2 = FVerdict.VALID := by decide
theorem boundary_half_pos_eq_var : posNum [0, 2] 2 = varNum [0, 2] := by decide
theorem boundary_half_via_T3a : verdictF 127 [0, 2] 2 = FVerdict.VALID :=
  boundary_half_valid (hne := by decide) (hin := by decide) boundary_half_pos_eq_var

-- 刚过半 share = 9/13（slots [0,2]·中心 2.5 → 倍化 [0,4]·中心 5）→ INVALID
theorem just_over_verdict : verdictF 254 [0, 4] 5 = FVerdict.INVALID := by decide
theorem just_over_share_fraction : 13 * posNum [0, 4] 5 = 9 * (2 * moment [0, 4] 5) := by decide
theorem just_over_pos_exceeds_var : posNum [0, 4] 5 = varNum [0, 4] + 20 := by decide
theorem just_over_via_T3b : verdictF 254 [0, 4] 5 = FVerdict.INVALID :=
  just_over_half_invalid (hne := by decide) (hin := by decide) (h := by decide)

-- 越界槽 [62,63,64,128]（128 > 127）→ INVALID（成员门先于口径位）
theorem oos_verdict : verdictF 254 [124, 126, 128, 256] 127 = FVerdict.INVALID := by decide
theorem oos_has_violation : ¬ ([124, 126, 128, 256] : List Int).all (fun x => 0 ≤ x && x ≤ 254) := by decide
theorem oos_via_TF2 : verdictF 254 [124, 126, 128, 256] 127 = FVerdict.INVALID :=
  out_of_space_kills (hne := by decide) oos_has_violation

-- 退化 [c, c, c] → moment 0 → VALID（share := 0 约定）
theorem degenerate_moment_zero : moment [63, 63, 63] 63 = 0 := by decide
theorem degenerate_verdict : verdictF 127 [63, 63, 63] 63 = FVerdict.VALID :=
  (degenerate_valid (hi := 127) (L := [63, 63, 63]) (c := 63) (hne := by decide) (hin := by decide)
    (h := degenerate_moment_zero)).1

theorem empty_verdict : verdictF 127 [] 63 = FVerdict.INCONCLUSIVE := verdict_empty 127 63

/-- 倍化不变的可判示例：[0,2]·c=2·hi=127 与其倍化像判决恒等 -/
theorem scale2_demo : verdictF 254 (scaleL 2 [0, 2]) (2 * 2) = verdictF 127 [0, 2] 2 :=
  verdict_scale2 (hi := 127) (c := 2) (L := [0, 2]) (hne := by decide)

-- ===== 台账证据（0 sorry·0 外部公理预期）========================================
#print axioms two_mulI
#print axioms mul_twoI
#print axioms sumL_shiftL
#print axioms sumSq_shiftL
#print axioms moment_decomposition
#print axioms share_half_iff
#print axioms share_lt_half_iff
#print axioms sq_nonneg
#print axioms posNum_nonneg
#print axioms sq_pos_of_ne_zero
#print axioms boundary_half_holds
#print axioms just_over_half_kills
#print axioms sumSq_nonneg
#print axioms sumSq_eq_zero_implies_all_zero
#print axioms sumL_zero_of_all_zero
#print axioms degenerate_at_center
#print axioms len_scaleL
#print axioms shift_scaleL
#print axioms sumSq_scaleL
#print axioms sumL_scaleL
#print axioms moment_scale
#print axioms posNum_scale
#print axioms share_band_scale_invariant
#print axioms membership_scale2
#print axioms membership_decide_scale2
#print axioms membership_scale2_list
#print axioms verdict_empty
#print axioms out_of_space_kills
#print axioms verdict_in_space
#print axioms boundary_half_valid
#print axioms just_over_half_invalid
#print axioms verdict_scale2
#print axioms degenerate_valid
#print axioms d1_is_scale_of_raw
#print axioms d1_verdict
#print axioms d1_pos
#print axioms d1_var
#print axioms d1_moment
#print axioms d1_share_fraction
#print axioms d1_share_over_half
#print axioms d1_pos_exceeds_var
#print axioms f8j_is_scale_of_raw
#print axioms f8j_verdict
#print axioms f8j_share_fraction
#print axioms f8j_pos
#print axioms f8j_var
#print axioms boundary_half_verdict
#print axioms boundary_half_pos_eq_var
#print axioms boundary_half_via_T3a
#print axioms just_over_verdict
#print axioms just_over_share_fraction
#print axioms just_over_pos_exceeds_var
#print axioms just_over_via_T3b
#print axioms oos_verdict
#print axioms oos_has_violation
#print axioms oos_via_TF2
#print axioms degenerate_moment_zero
#print axioms degenerate_verdict
#print axioms empty_verdict
#print axioms scale2_demo
