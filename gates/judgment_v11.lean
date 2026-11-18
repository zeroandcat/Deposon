/-
judgment_v11.lean — 判死线 v1.1 三接口 Lean 机检件（插件面·2026-11-18）
======================================================================
对应 Python 双实现位：gates/judgment_v11.py（可执行面·mock 向量全等）
＋ mocks/judgment_v11_vectors.json（发布向量风格·纯数零网络）。

三接口语义钉死（core-only·0 sorry·0 mathlib·Rat 不在 core → 交叉相乘 Nat 落地）：

  T1 三层带裁决（primary / reference / annotation）：
     裁决结构返回 verdict＋参照带＋注记带；参照带与注记带均为「报告位」，
     机检定理证明二者取值变化不改变 verdict（参照带 0 代裁语义）。
     主判方向 ge 的边界含等（值恰在判死线上 → KILL）。

  T2 量具判别（measure-locator / granularity discrimination）：
     键级测度展平为 token 级时，总体规模按每键 token 数放大
     （152 键 × 16 token = 2432 单元 ≠ 152 键）——分母非均匀重写使测度值
     漂移，在判死线邻域可双向翻转裁决；定位子注册表（Python 面）在
     裁决前拒绝粒度错配的判断。

  T3 全量原文落盘义务（raw_full obligation）：
     记录级谓词：raw_full 非空且 raw_head 是其前缀；义务 = 全记录逐条过。
     仅存 raw_head（截断头部）的记录破坏义务（fail-loud·逐条可定位）。

工程注记：String.isPrefixOf 的核归约需 elevated maxRecDepth（实测默认深度
对 8+ 字符串字面量卡死·40K 过）——全局 set_option 如下·与 48/120 规模
decide 深度坑同族（体例沿 NingziContainer 工程注记）。
-/

set_option maxRecDepth 100000

-- T1：三层带裁决 ---------------------------------------------------------
inductive Verdict where
  | KILL | PASS | INCONCLUSIVE

structure ThreeBand where
  verdict : Verdict
  reference_band : List Nat   -- 报告位（side-by-side）
  annotation_band : List Nat  -- 报告位（flag-only）

def adjudicate3 (primary : Option Bool) (refs : List Nat) (anns : List Nat) : ThreeBand :=
  { verdict :=
      match primary with
      | none => Verdict.INCONCLUSIVE
      | some true => Verdict.KILL
      | some false => Verdict.PASS
  , reference_band := refs
  , annotation_band := anns }

-- 参照带取值变化不改变 verdict（0 代裁·机检）
theorem verdict_indep_of_refs (p : Option Bool) (r1 r2 : List Nat) :
    (adjudicate3 p r1 []).verdict = (adjudicate3 p r2 []).verdict := by
  cases p <;> rfl

-- 注记带触发与否不改变 verdict（flag-only·机检）
theorem verdict_indep_of_anns (p : Option Bool) (a1 a2 : List Nat) :
    (adjudicate3 p [] a1).verdict = (adjudicate3 p [] a2).verdict := by
  cases p <;> rfl

-- 主判读数缺位（退化段）→ INCONCLUSIVE（不因退化解锁为 PASS）
theorem missing_primary_inconclusive (refs anns : List Nat) :
    (adjudicate3 none refs anns).verdict = Verdict.INCONCLUSIVE := rfl

-- 主判方向 ge 的边界含等：交叉相乘相等（分数相等）→ KILL
def crossedGe (a b c d : Nat) : Bool := decide (c * b ≤ a * d)

theorem ge_boundary_inclusive (a b c d : Nat) (h : a * d = c * b) :
    crossedGe a b c d = true := by
  rw [crossedGe, h]
  exact decide_eq_true (Nat.le_refl (c * b))

-- T2：量具判别（粒度判别）-----------------------------------------------
-- 均匀 token 长（每键 k token）的键列表，展平后单元数 = k × 键数
theorem flatten_len_uniform (k : Nat) (L : List (List Nat))
    (h : ∀ x ∈ L, x.length = k) :
    L.flatten.length = k * L.length := by
  rw [List.length_flatten]
  induction L with
  | nil => simp
  | cons x xs ih =>
      have hx : x.length = k := h x (by simp)
      have hxs : ∀ y ∈ xs, y.length = k := fun y hy => h y (by simp [hy])
      have hsum := ih hxs
      simp only [List.map_cons, List.sum_cons, List.length_cons, hx, hsum, Nat.mul_succ]
      omega

-- 发布向量锚：152 键 × 16 token = 2432 单元（Python 面同向量）
theorem token_as_key_population_mismatch :
    (List.replicate 152 (List.replicate 16 (0:Nat))).flatten.length = 16 * 152 := by
  have huni : ∀ x ∈ List.replicate 152 (List.replicate 16 (0:Nat)), x.length = 16 := by
    intro x hx
    have hx2 : x = List.replicate 16 (0:Nat) := (List.mem_replicate.mp hx).2
    rw [hx2, List.length_replicate]
  rw [flatten_len_uniform 16 _ huni, List.length_replicate]

-- 展平总体 ≠ 键总体：token 当键的粒度错配在数值上可判
theorem flattened_population_differs_from_key_population :
    16 * 152 ≠ 152 := by decide

-- T3：全量原文落盘义务 ---------------------------------------------------
-- 建模注记：String.isPrefixOf 系 String.Iterator/UInt32 位，核归约不闭合
-- （实测 1-8 字符字面量 rfl/decide 全卡·与 maxRecDepth 无关）；字符码
-- List Nat 建模同构语义（前缀＋非空），core-only 可机检——与「Rat 不在
-- core → 交叉相乘 Nat 落地」同体例。码位：32=空格 48='0' 49='1' 78='N'
-- 88='X' 89='Y' 114='r' 119='w'。
def listPrefix : List Nat → List Nat → Bool
  | [], _ => true
  | _, [] => false
  | a :: as, b :: bs => (a == b) && listPrefix as bs

def rawFullOkN (head full : List Nat) : Bool :=
  (match full with | [] => false | _ => true) && (listPrefix head full)

def rawObligationN : List (List Nat × List Nat) → Bool
  | [] => true
  | (h, f) :: rest => rawFullOkN h f && rawObligationN rest

-- 仅存 raw_head（raw_full 空）的记录破坏义务（fail-loud·逐条可定位）
theorem headonly_record_breaks_obligation :
    rawObligationN [([119, 48], []), ([119, 48, 48], [119, 48, 48, 114, 49])] = false := by decide

-- 三处置态（accepted / gate_rejected / parse_fail）全覆盖且原文齐 → 义务成立
theorem full_coverage_three_dispositions_holds :
    rawObligationN [([119, 48], [119, 48, 114, 49]),
                    ([119, 48, 48], [119, 48, 48, 114, 49]),
                    ([89], [89, 78, 89, 78])] = true := by decide

-- raw_head 非前缀（截断头与原文不一致）→ 破坏义务
theorem non_prefix_head_breaks_obligation :
    rawObligationN [([119, 48, 88], [119, 48, 114, 49])] = false := by decide

-- 向量锚（与 Python 面 mocks/judgment_v11_vectors.json 全等·交叉相乘 Nat 落地）
theorem v11_keylevel_below_line : crossedGe 38 152 13 50 = false := by decide
theorem v11_keylevel_at_line : crossedGe 13 50 13 50 = true := by decide
theorem v11_flattened_would_kill : crossedGe 646 2432 13 50 = true := by decide
theorem v11_flattened_would_pass : crossedGe 620 2432 13 50 = false := by decide

-- 台账证据（0 sorry·0 外部公理预期）
#print axioms verdict_indep_of_refs
#print axioms verdict_indep_of_anns
#print axioms missing_primary_inconclusive
#print axioms ge_boundary_inclusive
#print axioms flatten_len_uniform
#print axioms token_as_key_population_mismatch
#print axioms flattened_population_differs_from_key_population
#print axioms headonly_record_breaks_obligation
#print axioms full_coverage_three_dispositions_holds
#print axioms non_prefix_head_breaks_obligation
#print axioms v11_keylevel_below_line
#print axioms v11_keylevel_at_line
#print axioms v11_flattened_would_kill
#print axioms v11_flattened_would_pass
