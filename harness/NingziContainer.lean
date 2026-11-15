/-
凝子场容器 v2 · Lean 4 形式化（core only · 0 mathlib · 工具链已落地·lake build 编译回执在案）
================================================
基据：0.6B-deposon 容器实验设计案 A 轨 2026-11-13（sha256-12 `58ea2b458d54`）§1 P1 数学规格。
令源：coordinator 派单两窗（2026-11-14）·方向注记：「仿物理→自行 Lean 形式化校验·可能发现新线」
＋「新线合流双审代裁·备全前置」。

v2 变更注记（第二窗·编译驱动勘正，详见呈报件）：
  · 工具链 Lean 4.15.0 standalone 落地（~/.elan 内容流 0 B/s → GitHub releases 直取 264 MB tar.zst）；
  · 系数域勘正：v1 期 ℚ 字面量（ηw := 1/10 等）在 Int 域恒为 0——v2 全面换 80 尺度定点
    （ηw=8·ηr=4·α=32·β=24·γc=24·lamJ=40·m=|∩|×5·γ 百分制 100↔1.0）；
  · List.NoDup 不在 core 4.15（Batteries 位）→ 自建 Nodup（Pairwise 基座）；
  · eraseK 谓词 v1 Bool（x.1 != k）→ v2 decide（x.1 ≠ k）（语义等价·Prop 重写友好）；
  · 债1 cliff_n 通式清偿（**勘正版陈述**：首窗版对非空 C 不成立——见 §7 注记）；
  · 债5 JSymm 保持清偿（hebbW2 对称双条目版·构造性方案）；
  · 债2/3/4 保留（Rat/Real.log 与测度论/电路复杂度库不在 core——候 mathlib/Complexitylib·文献互证位 N5）。

环境注记：Lean 4.15.0 core（无 mathlib·Std.Data.Rat 实测 0 命中）。ℝ/Real.log/Real.sqrt 不在 core——
  · E_i 规格中的 (·)^0.5 以 `qsqrt` oracle 占位呈现（0 计算语义·不进任何证明前提）；
  · D50 实数版以 Nat decide 夹逼（68, 69）落锚＋通式 sorry 债；
  · D1/D2/D5 定理夹逼＝陈述级带入（代理谓词可证部分已证·真定理位 sorry 债）。

v3 变更注记（第三窗·17:27 回位帧·五簇 staged patch 采认合入·build 全绿）：
  · 簇 A（8 error）：eraseK_not_mem nil 支补 intro；insertK_keys 会员残局 rw 后补 Or.inl rfl＋
    mem_map.mpr 显式构造；pickMin_in 展开 pickMin 后 if_pos/if_neg 消解（4.15 的
    List.mem_cons_of_mem 新签名 (y){a}{l}(h)——387 处删中间显式实参 ks）；
  · 簇 B（4 error）：writeOp let-in 结构的 split 失败——unfold writeOp（不做 zeta）改
    simp only [writeOp]（zeta 归约 let 后 if 显形·split 可分）·四处统一；
  · 簇 C（5 error）：F^[i] 记号在 4.15 core 不存在且 Function.iterate 实测 unknown identifier
    （探针核）——自建 fiter 迭代算子零歧义替代（外部提示 Function.iterate 不可用·实测异议修正）；
  · 簇 D（1 error）：cliff_n 内 hp.1 已绑定键参——去掉多余实参 k（勘正版陈述语义 0 触）；
  · 簇 E（3 error）：jget 解除 List.lookup/BEq 方程引理依赖——自建首匹配递归 DecidableEq 版
    （LawfulBEq 域与 lookup 语义等价·首个匹配条目值·缺省 0）·jget_cons_eq/hit1/hit2/miss
    全部重写为 show + if_pos/if_neg 可控形态；
  · 追加勘正：argminKey_mem 尾步 simp only [h] 误作用于目标（no progress）——改 rw [h] at this；
    resetOp 参数匿名化消 unused variable warning；
  · 编译回执（17:37·.lake/build 清空后 lake build NingziContainer 全新构建·显式目标）：
    **Build completed successfully·0 error·3 sorry warning（债2/3/4 预注册保留位）·.olean 产出**。
    lakefile.toml 加 defaultTargets（裸 lake build 假成功陷阱封堵）。

证明债台账（sorry）在文件尾部 SORRY-LEDGER 区集中登记；已清偿债在 §7 债清偿区登记。
-/

import Init

local notation "ℕ" => Nat

-- ============================================================
-- §0 基本类型与配置（设计案 §1.1 / §2 预注册 config）
-- ============================================================

abbrev Tok := Nat          -- token id ∈ [8192]
abbrev Key := List Tok     -- 16-token 键（良构长度由 probe 冻结账承载·此处不强制）
abbrev Val := List Tok     -- 24-token 值
abbrev Ver := Nat          -- 版本号（同键覆写语义的版本计数）

-- 预注册配置（设计案 §2：CAP∈{256,∞}·γ=1.0·η_w=0.1·η_r=0.05·θ_c=2·K_max=64·α=0.4·β=0.3·γ_c=0.3·λ_J=0.5）
structure CFG where
  CAP : ℕ
  γ : Int
  ηw : Int
  ηr : Int
  θc : ℕ
  Kmax : ℕ
  α : Int
  β : Int
  γc : Int
  lamJ : Int

-- v2 系数域＝Int 定点（80 尺度：ηw=8↔0.1·ηr=4↔0.05·α=32↔0.4·β=24↔0.3·γc=24↔0.3·lamJ=40↔0.5；
-- m=|∩|×5↔|∩|/16 精确可除；γ 百分制：100↔1.0·95↔0.95 衰减带 P4）
def cfgV1 : CFG where
  CAP := 256
  γ := 100          -- γ=1.0 主跑（百分制·在册语义：不随时间漂移）；衰减带 [95,100] 为 P4 参数位
  ηw := 8           -- 8/80 = 0.1
  ηr := 4           -- 4/80 = 0.05
  θc := 2
  Kmax := 64
  α := 32           -- 32/80 = 0.4
  β := 24           -- 24/80 = 0.3
  γc := 24          -- 24/80 = 0.3
  lamJ := 40        -- 40/80 = 0.5

theorem cfgV1_CAP : cfgV1.CAP = 256 := rfl
theorem cfgV1_γ_main : cfgV1.γ = 100 := rfl   -- γ=1.0 主跑（百分制 100）
theorem cfgV1_θc : cfgV1.θc = 2 := rfl

-- ============================================================
-- §1 状态空间 C = (D, J, M, L)（设计案 §1.1）
-- ============================================================

structure Meta where          -- M：单元元数据
  rho : Int                     -- ρ_i 存活度（80u 定点）
  r : ℕ                       -- 读计数
  w : ℕ                       -- 写计数
  t : ℕ                       -- 末访问时步

abbrev JField := List ((Key × Key) × Int)   -- J：稀疏耦合场（有限条目表·jget 取值）

inductive Event where          -- L：链式账本事件（只追加·probe_harness.Ledger 的形状位）
  | write (k : Key) (v : Val)
  | read (k : Key)
  | evict (k : Key)
  | step

structure CState where
  D : List (Key × (Val × Ver)) -- 显式字典（在册本体·同键最新值为现行值）
  J : JField
  M : Key → Meta
  clock : ℕ
  L : List Event

def live (C : CState) : ℕ := C.D.length   -- 在册单元数（D 无重复键时 length 即单元数——Nodup 前提见 T2）

-- J 场取值（缺省 0＝无耦合）
--（v3 编译驱动勘正：List.lookup/BEq 方程引理链在 core 4.15 的 sorry-free 证明上不稳——
--  自建首匹配递归·DecidableEq 版（LawfulBEq 域与 lookup 语义等价：取首个匹配条目值·缺省 0））
def jget : JField → Key → Key → Int
  | [], _, _ => 0
  | (pair, w) :: rest, i, j => if pair = (i, j) then w else jget rest i j

-- 对称性谓词（设计案：稀疏**对称**耦合场——v1 单侧写条目·对称保持已由 hebbW2 清偿·§7）
def JSymm (J : JField) : Prop := ∀ i j, jget J i j = jget J j i

-- 无重复键谓词（core 4.15 无 List.NoDup——Batteries 位·自建于 Pairwise 基座）
def Nodup (l : List Key) : Prop := l.Pairwise (fun a b => a ≠ b)

theorem Nodup_nil : Nodup [] := List.Pairwise.nil

theorem Nodup_cons_mp {a : Key} {l : List Key} (h : Nodup (a :: l)) : a ∉ l ∧ Nodup l :=
  match h with
  | .cons hhead htail => ⟨fun hb => hhead a hb rfl, htail⟩

theorem Nodup_cons {a : Key} {l : List Key} (h : a ∉ l) (h' : Nodup l) : Nodup (a :: l) :=
  List.Pairwise.cons (fun b hb he => h (by rw [he]; exact hb)) h'

-- token 集合（去重）
def tset (k : Key) : List Tok := k.eraseDups

-- ============================================================
-- §2 匹配测度与 F1 寻址评分（设计案 §1.2 / §1.5）
-- ============================================================

-- m(q,k) = |set(q) ∩ set(k)| / 16（0 嵌入·0 稠密向量·规则层可复算）——80 尺度定点：|∩|/16 ↔ |∩|×5
def m (q k : Key) : Int := 5 * (((tset q).filter (fun a => a ∈ tset k)).length : Int)

-- F1 寻址评分：score(q,i) = m(q,k_i) + λ_J·Σ_j J[(i,j)]·m(q,k_j)（E3 语义位·read 返回值语义不变）
def f1score (lamJ : Int) (J : JField) (ks : List Key) (q i : Key) : Int :=
  m q i + lamJ * (ks.foldl (fun acc j => acc + jget J i j * m q j) 0) / 6400
  -- 80² 量纲对齐：J·m 双 80u 乘积（6400u）× λ_J 80u——定义级（E3 语义位·不进证明前提）

-- ============================================================
-- §3 场能量与淘汰（设计案 §1.4）
-- ============================================================

-- recency：⚠ 欠规格位③——原始步差 vs 归一化未钉死·v1/v2 取 (now − t_i) 原始步差
def recencyQ (now : ℕ) (M : Key → Meta) (i : Key) : Int := ((now - (M i).t : ℕ) : Int)

-- sqrt oracle：mathlib ℝ 债（无计算语义·不进证明前提）
def qsqrt : Int → Int := fun _ => 0  -- ⚠ oracle 占位（0 计算语义·0 证明前提）·候 mathlib Real.sqrt 清偿

-- 耦合簇贡献：Σ_{j∈N(i)} J[(i,j)]·ρ_j / (1+|N(i)|)——N(i)＝J 表中 i 为首元的条目对端
def clusterTerm (J : JField) (M : Key → Meta) (i : Key) : Int :=
  let ns := (J.filter (fun e => e.1.1 == i)).map (fun e => e.1.2)
  (ns.foldl (fun acc j => acc + jget J i j * (M j).rho) 0) / (80 * ((ns.length : Int) + 1))
  -- 80² 量纲对齐：J·ρ 双 80u 乘积·÷80 复位（定义级·不进证明前提）

-- E_i = α·recency + β·(r+w)^0.5 + γ_c·簇贡献（α=0.4·β=0.3·γ_c=0.3）
-- 量纲注记：recency/qsqrt 项为原始计数（未缩放）·簇贡献为 80u 定点——三项量纲混合＝欠规格位③
--（recency 归一化）的深层形态·如实保留（具体式不进证明前提——淘汰定理对任意 E : Key → Int 成立）
def energy (cfg : CFG) (now : ℕ) (J : JField) (M : Key → Meta) (i : Key) : Int :=
  cfg.α * recencyQ now M i
    + cfg.β * qsqrt (((M i).r + (M i).w : ℕ) : Int)
    + cfg.γc * clusterTerm J M i

-- 严格比较（Int 原生序·Bool 化供 argminKey 使用）
def qlt (a b : Int) : Bool := decide (a < b)

-- argmin 淘汰目标：⚠ 欠规格位②——平局裁决未钉死·v1/v2 取「首见最小」（列表序·隐藏时序依赖）
def pickMin (E : Key → Int) : Key → List Key → Key
  | acc, [] => acc
  | acc, x :: xs => pickMin E (if qlt (E x) (E acc) then x else acc) xs

def argminKey (E : Key → Int) (l : List Key) : Option Key :=
  match l with
  | [] => none
  | k :: ks => some (pickMin E k ks)

-- ============================================================
-- §4 四操作语义（设计案 §1.3·E4 契约保形）
-- ============================================================

-- 字典基元：全删后插（同键最新值为现行值·覆写语义的结构保证）
--（v2：谓词 decide (x.1 ≠ k)——与 v1 Bool (x.1 != k) 语义等价·LawfulBEq 下可证同）
def eraseK (k : Key) (l : List (Key × (Val × Ver))) : List (Key × (Val × Ver)) :=
  l.filter (fun x => decide (x.1 ≠ k))

def insertK (k : Key) (v : Val) (ver : Ver) (l : List (Key × (Val × Ver))) :
    List (Key × (Val × Ver)) := (k, (v, ver)) :: eraseK k l

def getK (k : Key) (l : List (Key × (Val × Ver))) : Option (Val × Ver) := l.lookup k

-- Hebb 写更新（v1 单侧写）：对共存 j≠k 且 |set(k)∩set(k_j)| ≥ θ_c → J[(k,j)] += η_w·w_kj/16
--（⚠ 欠规格位①：更新用 pre-evict 共存集·且 evict 不清理被逐键 J 条目（悬挂耦合）·A/B 可预注册）
def hebbW (θc : ℕ) (ηw : Int) (k : Key) (D : List (Key × (Val × Ver))) (J : JField) : JField :=
  D.foldl (fun J' x =>
    let wij := ((tset k).filter (fun a => a ∈ tset x.1)).length
    if x.1 ≠ k ∧ wij ≥ θc then ((k, x.1), jget J' k x.1 + ηw * wij / 16) :: J' else J') J

-- Hebb 写更新·v2 对称双条目版（债5 清偿载体：JSymm 保持的构造性方案——(k,j)/(j,k) 双条目同增幅）
--（⚠ 欠规格位①的 A/B 对照面：v1 单侧写 vs v2 对称写＝规格分叉·呈荐候 PI）
def hebbW2 (θc : ℕ) (ηw : Int) (k : Key) (D : List (Key × (Val × Ver))) (J : JField) : JField :=
  D.foldl (fun J' x =>
    let wij := ((tset k).filter (fun a => a ∈ tset x.1)).length
    if x.1 ≠ k ∧ wij ≥ θc then
      ((k, x.1), jget J' k x.1 + ηw * wij / 16) :: ((x.1, k), jget J' x.1 k + ηw * wij / 16) :: J'
    else J') J

def evictOne (E : Key → Int) (C : CState) : CState :=
  match argminKey E (C.D.map Prod.fst) with
  | none => C
  | some k => { C with D := eraseK k C.D, L := Event.evict k :: C.L }

-- write(k,v) 主体：覆写/插入＋Hebb 更新＋元数据/账本（writeBody/容量检查分离＝v2 编译驱动重构）
def writeBody (cfg : CFG) (k : Key) (v : Val) (C : CState) : CState :=
  let ver := match getK k C.D with | some p => p.2 + 1 | none => 0
  { C with
    D := insertK k v ver C.D
    J := hebbW cfg.θc cfg.ηw k C.D C.J
    M := fun k' => if k' == k then {(C.M k') with w := (C.M k').w + 1, t := C.clock} else C.M k'
    L := Event.write k v :: C.L }

-- write(k,v)：writeBody 后容量检查（|D|>CAP → 淘汰 argmin E）
def writeOp (cfg : CFG) (k : Key) (v : Val) (C : CState) : CState :=
  let C1 := writeBody cfg k v C
  if C1.D.length > cfg.CAP then
    evictOne (fun i => energy cfg C.clock C1.J C1.M i) C1
  else C1

-- read(k)：命中→现行值直读＋读扩散（⚠ 欠规格位④：J[(k,·)]·ρ 微增 η_r 的邻居集与增幅公式未钉死·
-- v1/v2 取自键 ρ += η_r 占位）；miss→null（不抛异常·全函数世界结构性成立·幻觉阻力硬契约）
def readOpS (cfg : CFG) (k : Key) (C : CState) : Option (Val × Ver) × CState :=
  match getK k C.D with
  | some p => (some p, { C with
      M := fun k' => if k' == k then {(C.M k') with r := (C.M k').r + 1, rho := (C.M k').rho + cfg.ηr, t := C.clock} else C.M k'
      L := Event.read k :: C.L })
  | none => (none, { C with L := Event.read k :: C.L })

-- step()：γ 全局衰减（百分制：ρ ← γ·ρ/100·γ=100 主跑＝恒等；衰减带 [95,100] P4 参数位）
def stepOp (cfg : CFG) (C : CState) : CState :=
  { C with M := fun k => {(C.M k) with rho := cfg.γ * (C.M k).rho / 100}, L := Event.step :: C.L }

-- reset()：回空态（账本新链）
def resetOp (_ : CState) : CState := ⟨[], [], fun _ => ⟨0, 0, 0, 0⟩, 0, []⟩

theorem reset_live (C : CState) : (resetOp C).D.length = 0 := rfl

-- ============================================================
-- §5 基元引理（淘汰序/长度记账/键集演进/无重复保持）
-- ============================================================

theorem eraseK_cons_self (k : Key) (a : Key × (Val × Ver)) (as : List (Key × (Val × Ver)))
    (h : a.1 = k) : eraseK k (a :: as) = eraseK k as := by
  simp [eraseK, List.filter, h]

theorem eraseK_cons_ne (k : Key) (a : Key × (Val × Ver)) (as : List (Key × (Val × Ver)))
    (h : a.1 ≠ k) : eraseK k (a :: as) = a :: eraseK k as := by
  simp [eraseK, List.filter, h]

theorem eraseK_le (k : Key) : ∀ l : List (Key × (Val × Ver)), (eraseK k l).length ≤ l.length := by
  intro l
  induction l with
  | nil => simp [eraseK]
  | cons a as ih =>
    by_cases h : a.1 = k
    · rw [eraseK_cons_self k a as h]
      simp only [List.length_cons]
      omega
    · rw [eraseK_cons_ne k a as h]
      simp only [List.length_cons]
      omega

theorem eraseK_not_mem (k : Key) : ∀ l : List (Key × (Val × Ver)),
    ¬ k ∈ l.map Prod.fst → eraseK k l = l := by
  intro l
  induction l with
  | nil => intro _; rfl
  | cons a as ih =>
    intro h
    have h1 : a.1 ≠ k := fun he => h (by simp [he])
    have h2 : ¬ k ∈ as.map Prod.fst := fun hm => h (by simp [hm])
    rw [eraseK_cons_ne k a as h1, ih h2]

theorem eraseK_mem_len (k : Key) : ∀ l : List (Key × (Val × Ver)),
    k ∈ l.map Prod.fst → (eraseK k l).length + 1 ≤ l.length := by
  intro l
  induction l with
  | nil => intro h; simp at h
  | cons a as ih =>
    intro h
    by_cases h1 : a.1 = k
    · rw [eraseK_cons_self k a as h1]
      have hle := eraseK_le k as
      simp only [List.length_cons]
      omega
    · have hk : k ∈ as.map Prod.fst := by
        rcases List.mem_cons.mp h with he | hm
        · exact absurd he.symm h1
        · exact hm
      have hrec := ih hk
      rw [eraseK_cons_ne k a as h1]
      simp only [List.length_cons]
      omega

-- 键集演进引理组（债1 的债位本体）
theorem eraseK_keys (k : Key) (l : List (Key × (Val × Ver))) (x : Key)
    (h : x ∈ (eraseK k l).map Prod.fst) : x ∈ l.map Prod.fst := by
  simp only [eraseK] at h
  rcases List.mem_map.mp h with ⟨a, ha, hfa⟩
  exact List.mem_map.mpr ⟨a, (List.mem_filter.mp ha).1, hfa⟩

theorem eraseK_keys_not (k : Key) (l : List (Key × (Val × Ver))) : ¬ k ∈ (eraseK k l).map Prod.fst := by
  intro h
  rcases List.mem_map.mp h with ⟨a, ha, hfa⟩
  have hb : decide (a.1 ≠ k) = true := (List.mem_filter.mp ha).2
  rw [hfa] at hb
  simp at hb

theorem eraseK_len_exact (k : Key) : ∀ (l : List (Key × (Val × Ver))),
    Nodup (l.map Prod.fst) → k ∈ l.map Prod.fst → (eraseK k l).length + 1 = l.length := by
  intro l
  induction l with
  | nil => intro _ h; simp at h
  | cons a as ih =>
    intro hnd hmem
    simp only [List.map_cons] at hnd hmem
    have hp := Nodup_cons_mp hnd
    by_cases h1 : a.1 = k
    · have hnk : ¬ k ∈ as.map Prod.fst := fun hm => hp.1 (by rw [h1]; exact hm)
      rw [eraseK_cons_self k a as h1, eraseK_not_mem k as hnk]
      simp only [List.length_cons]
    · have hmem' : k ∈ as.map Prod.fst := by
        rcases List.mem_cons.mp hmem with he | hm
        · exact absurd he.symm h1
        · exact hm
      rw [eraseK_cons_ne k a as h1]
      have hrec := ih hp.2 hmem'
      simp only [List.length_cons]
      omega

theorem eraseK_nodup (k : Key) : ∀ (l : List (Key × (Val × Ver))),
    Nodup (l.map Prod.fst) → Nodup ((eraseK k l).map Prod.fst) := by
  intro l
  induction l with
  | nil => intro _; exact Nodup_nil
  | cons a as ih =>
    intro h
    simp only [List.map_cons] at h
    have hp := Nodup_cons_mp h
    by_cases h1 : a.1 = k
    · rw [eraseK_cons_self k a as h1]
      exact ih hp.2
    · have hnotin : a.1 ∉ (eraseK k as).map Prod.fst := fun hm => hp.1 (eraseK_keys k as a.1 hm)
      rw [eraseK_cons_ne k a as h1]
      simp only [List.map_cons]
      exact Nodup_cons hnotin (ih hp.2)

theorem insertK_le (k : Key) (v : Val) (ver : Ver) (l : List (Key × (Val × Ver))) :
    (insertK k v ver l).length ≤ l.length + 1 := by
  simp only [insertK, List.length_cons]
  exact Nat.succ_le_succ (eraseK_le k l)

theorem insertK_fresh (k : Key) (v : Val) (ver : Ver) (l : List (Key × (Val × Ver)))
    (h : ¬ k ∈ l.map Prod.fst) : (insertK k v ver l).length = l.length + 1 := by
  simp [insertK, eraseK_not_mem k l h, List.length_cons]

theorem insertK_keys (k : Key) (v : Val) (ver : Ver) (l : List (Key × (Val × Ver))) (x : Key)
    (h : x ∈ (insertK k v ver l).map Prod.fst) : x = k ∨ x ∈ l.map Prod.fst := by
  rcases List.mem_map.mp h with ⟨a, ha, hfa⟩
  rcases List.mem_cons.mp ha with he | hm
  · rw [← hfa, he]; exact Or.inl rfl
  · exact Or.inr (eraseK_keys k l x (List.mem_map.mpr ⟨a, hm, hfa⟩))

theorem insertK_nodup (k : Key) (v : Val) (ver : Ver) (l : List (Key × (Val × Ver)))
    (h : Nodup (l.map Prod.fst)) : Nodup ((insertK k v ver l).map Prod.fst) := by
  simp only [insertK, List.map_cons]
  exact Nodup_cons (eraseK_keys_not k l) (eraseK_nodup k l h)

theorem pickMin_in (E : Key → Int) : ∀ (ks : List Key) (acc : Key) (l : List Key),
    acc ∈ l → (∀ x, x ∈ ks → x ∈ l) → pickMin E acc ks ∈ l := by
  intro ks
  induction ks with
  | nil => intro acc l ha _; exact ha
  | cons x xs ih =>
    intro acc l ha hall
    simp only [pickMin]
    by_cases h : qlt (E x) (E acc)
    · rw [if_pos h]
      exact ih x l (hall x (List.mem_cons_self x xs))
        (fun y hy => hall y (List.mem_cons_of_mem x hy))
    · rw [if_neg h]
      exact ih acc l ha (fun y hy => hall y (List.mem_cons_of_mem x hy))

theorem argminKey_mem (E : Key → Int) : ∀ (l : List Key) (k : Key),
    argminKey E l = some k → k ∈ l := by
  intro l
  cases l with
  | nil => intro k h; simp [argminKey] at h
  | cons k0 ks =>
    intro k h
    simp only [argminKey, Option.some.injEq] at h
    have this := pickMin_in E ks k0 (k0 :: ks) (List.mem_cons_self k0 ks)
      (fun x hx => List.mem_cons_of_mem k0 hx)
    rw [h] at this
    exact this

theorem argminKey_isSome (E : Key → Int) : ∀ l : List Key, l ≠ [] → (argminKey E l).isSome = true := by
  intro l
  cases l with
  | nil => intro h; exact absurd rfl h
  | cons k ks => intro _; simp [argminKey]

-- 列表逐点引理
theorem map_eq_pointwise {α β} (f g : α → β) : ∀ (l : List α),
    List.map f l = List.map g l → ∀ x ∈ l, f x = g x := by
  intro l
  induction l with
  | nil => intro _ x hx; simp at hx
  | cons a as ih =>
    intro h x hx
    simp only [List.map_cons] at h
    injection h with h1 h2
    rcases List.mem_cons.mp hx with rfl | hx'
    · exact h1
    · exact ih h2 x hx'

-- evictOne 引理组（T1/T2 与债1 的淘汰支骨架）
theorem evictOne_len (E : Key → Int) (C : CState) (hC : 0 < C.D.length) :
    (evictOne E C).D.length < C.D.length := by
  have h0 : 0 < (C.D.map Prod.fst).length := by simp only [List.length_map]; exact hC
  have hne : C.D.map Prod.fst ≠ [] := by
    intro hc; rw [hc] at h0; simp at h0
  unfold evictOne
  cases hA : argminKey E (C.D.map Prod.fst) with
  | none =>
    have hcontr := argminKey_isSome E (C.D.map Prod.fst) hne
    rw [hA] at hcontr; simp at hcontr
  | some k0 =>
    have hmem := argminKey_mem E (C.D.map Prod.fst) k0 hA
    have hlen := eraseK_mem_len k0 C.D hmem
    show (eraseK k0 C.D).length < C.D.length
    omega

theorem evictOne_len_exact (E : Key → Int) (C : CState)
    (hnd : Nodup (C.D.map Prod.fst)) (hC : 0 < C.D.length) :
    (evictOne E C).D.length + 1 = C.D.length := by
  have h0 : 0 < (C.D.map Prod.fst).length := by simp only [List.length_map]; exact hC
  have hne : C.D.map Prod.fst ≠ [] := by
    intro hc; rw [hc] at h0; simp at h0
  unfold evictOne
  cases hA : argminKey E (C.D.map Prod.fst) with
  | none =>
    have hcontr := argminKey_isSome E (C.D.map Prod.fst) hne
    rw [hA] at hcontr; simp at hcontr
  | some k0 =>
    show (eraseK k0 C.D).length + 1 = C.D.length
    exact eraseK_len_exact k0 C.D hnd (argminKey_mem E (C.D.map Prod.fst) k0 hA)

theorem evictOne_nodup (E : Key → Int) (C : CState) (h : Nodup (C.D.map Prod.fst)) :
    Nodup ((evictOne E C).D.map Prod.fst) := by
  unfold evictOne
  cases hA : argminKey E (C.D.map Prod.fst) with
  | none => exact h
  | some k0 =>
    show Nodup ((eraseK k0 C.D).map Prod.fst)
    exact eraseK_nodup k0 C.D h

-- 键集演进：write 后键集 ⊆ 原键集 ∪ {k}（fresh 性沿写序列保持的根基）
theorem writeOp_keys (cfg : CFG) (k : Key) (v : Val) (C : CState) (x : Key)
    (h : x ∈ (writeOp cfg k v C).D.map Prod.fst) :
    x = k ∨ x ∈ C.D.map Prod.fst := by
  have hB : x ∈ (writeBody cfg k v C).D.map Prod.fst → x = k ∨ x ∈ C.D.map Prod.fst :=
    fun hb => insertK_keys k v (match getK k C.D with | some p => p.2 + 1 | none => 0) C.D x hb
  simp only [writeOp] at h
  unfold evictOne at h
  split at h
  · next hgt =>
    revert h
    cases hA : argminKey (fun i => energy cfg C.clock (writeBody cfg k v C).J (writeBody cfg k v C).M i)
        ((writeBody cfg k v C).D.map Prod.fst) with
    | none => intro h; exact hB h
    | some k0 => intro h; exact hB (eraseK_keys k0 _ x h)
  · exact hB h

theorem writeOp_nodup (cfg : CFG) (k : Key) (v : Val) (C : CState) (h : Nodup (C.D.map Prod.fst)) :
    Nodup ((writeOp cfg k v C).D.map Prod.fst) := by
  have hndB : Nodup ((writeBody cfg k v C).D.map Prod.fst) := by
    show Nodup ((insertK k v (match getK k C.D with | some p => p.2 + 1 | none => 0) C.D).map Prod.fst)
    exact insertK_nodup k v _ C.D h
  simp only [writeOp]
  split
  · next hgt =>
    exact evictOne_nodup (fun i => energy cfg C.clock (writeBody cfg k v C).J (writeBody cfg k v C).M i)
      (writeBody cfg k v C) hndB
  · exact hndB

-- ============================================================
-- §6 定理（可证位·逐条攻坚·编译回执在案）
-- ============================================================

/-! ### T1 容量不变量：n_live ≤ CAP（预注册 AC 档的机器侧骨架） -/
theorem cap_invariant (cfg : CFG) (k : Key) (v : Val) (C : CState)
    (hC : C.D.length ≤ cfg.CAP) : (writeOp cfg k v C).D.length ≤ cfg.CAP := by
  have hbody : (writeBody cfg k v C).D.length ≤ C.D.length + 1 := by
    show (insertK k v (match getK k C.D with | some p => p.2 + 1 | none => 0) C.D).length ≤ C.D.length + 1
    exact insertK_le k v _ C.D
  simp only [writeOp]
  split
  · rename_i hgt
    have hne : 0 < (writeBody cfg k v C).D.length := by omega
    have hev := evictOne_len (fun i => energy cfg C.clock (writeBody cfg k v C).J (writeBody cfg k v C).M i)
      (writeBody cfg k v C) hne
    omega
  · rename_i hle
    omega

/-! ### T2 断崖记账版（每写一步·fresh 键）：live = min(old+1, CAP)
    （前提含 Nodup——v1 陈述对含重复键态不成立：重复键态下 evict 单步可删多册·通式见 §7 勘正注记） -/
theorem write_live_rec (cfg : CFG) (k : Key) (v : Val) (C : CState)
    (hC : C.D.length ≤ cfg.CAP) (hnd : Nodup (C.D.map Prod.fst))
    (hfresh : ¬ k ∈ C.D.map Prod.fst) :
    (writeOp cfg k v C).D.length = min (C.D.length + 1) cfg.CAP := by
  have hfreshlen : (writeBody cfg k v C).D.length = C.D.length + 1 := by
    show (insertK k v (match getK k C.D with | some p => p.2 + 1 | none => 0) C.D).length = C.D.length + 1
    exact insertK_fresh k v _ C.D hfresh
  have hndB : Nodup ((writeBody cfg k v C).D.map Prod.fst) := by
    show Nodup ((insertK k v (match getK k C.D with | some p => p.2 + 1 | none => 0) C.D).map Prod.fst)
    exact insertK_nodup k v _ C.D hnd
  simp only [writeOp]
  split
  · rename_i hgt
    have hne : 0 < (writeBody cfg k v C).D.length := by omega
    have hev := evictOne_len_exact (fun i => energy cfg C.clock (writeBody cfg k v C).J (writeBody cfg k v C).M i)
      (writeBody cfg k v C) hndB hne
    omega
  · rename_i hle
    omega

/-! ### T3 γ=1.0 在册不漂移：step 对元数据场为恒等（百分制 γ=100＝乘法恒等·遗忘仅由容量物理驱动） -/
theorem gamma1_nodrift (C : CState) : (stepOp { cfgV1 with γ := 100 } C).M = C.M := by
  funext k
  show {(C.M k) with rho := 100 * (C.M k).rho / 100} = C.M k
  have h : 100 * (C.M k).rho / 100 = (C.M k).rho := by omega
  rw [h]

/-! ### T4 D50 实数版的 Nat 夹逼锚（γ=0.99：存活率过半发生在第 69 步·与 ln(.5)/ln(.99)≈68.97 一致） -/
theorem d50_lower : 2 * 99 ^ 69 < 100 ^ 69 := by decide    -- (99/100)^69 < 1/2
theorem d50_upper : 100 ^ 68 < 2 * 99 ^ 68 := by decide    -- 1/2 < (99/100)^68

def powQ (q : Int) : ℕ → Int
  | 0 => 1
  | n + 1 => q * powQ q n

-- 债2｜D50 通式（百分制 Int 陈述·证明债）：0 < γ < 100 ⇒ 存在整步 t 使 2·γ^(t+1) < 100^(t+1) 且 100^t < 2·γ^t
--   （＝存活率 (γ/100)^t 跨过 1/2 的整步夹逼；t=68 实例见上方 d50_lower/d50_upper 机器证·候 mathlib）
theorem d50_real_debt (γ : Int) (h1 : 0 < γ) (h2 : γ < 100) :
    ∃ t : ℕ, 2 * powQ γ (t + 1) < powQ 100 (t + 1) ∧ powQ 100 t < 2 * powQ γ t := sorry

/-! ### T5 容器操作 0 触模型参数（结构性定理：算子类型上无模型参数位） -/
structure World where
  theta : List ℕ      -- 模型参数（抽象占位·ownership_redline：模型层 0 触记忆状态）
  C : CState

def lift (op : CState → CState) (W : World) : World := { W with C := op W.C }

theorem zero_touch_structural (op : CState → CState) (W : World) : (lift op W).theta = W.theta := rfl
theorem zero_touch_write (cfg : CFG) (k : Key) (v : Val) (W : World) :
    (lift (writeOp cfg k v) W).theta = W.theta := rfl
theorem zero_touch_step (cfg : CFG) (W : World) : (lift (stepOp cfg) W).theta = W.theta := rfl

/-! ### T6 读语义：miss→null 硬语义＋现行值直读＋读守恒 -/
theorem read_miss_null (cfg : CFG) (k : Key) (C : CState) (h : getK k C.D = none) :
    (readOpS cfg k C).1 = none := by
  simp [readOpS, h]

theorem read_hit_current (cfg : CFG) (k : Key) (C : CState) (p : Val × Ver) (h : getK k C.D = some p) :
    (readOpS cfg k C).1 = some p := by
  simp [readOpS, h]

theorem read_conserv (cfg : CFG) (k : Key) (C : CState) : (readOpS cfg k C).2.D = C.D := by
  unfold readOpS
  split <;> rfl

/-! ### T7 D1 代理陈述（时延嵌入·分离性代理版——可证位）：
    若观测在时延坐标上分离态（generic 性的分离性代理），则时延映射单射（嵌入的最小代理）。
    （v3 编译驱动勘正：Lean 4.15 core 无 Function.iterate/`f^[n]` 记号——探针实测 unknown
    identifier·自建 fiter 迭代算子零歧义替代） -/
def fiter {X : Type} (F : X → X) : ℕ → X → X
  | 0, x => x
  | n + 1, x => fiter F n (F x)

def TakensSeparates {X σ : Type} (F : X → X) (φ : X → σ) (n : ℕ) : Prop :=
  ∀ x y : X, (∀ i, i ≤ n → φ (fiter F i x) = φ (fiter F i y)) → x = y

theorem d1_agent {X σ : Type} (F : X → X) (φ : X → σ) (n : ℕ)
    (h : TakensSeparates F φ n) (x y : X)
    (heq : (List.range (n + 1)).map (fun i => φ (fiter F i x)) = (List.range (n + 1)).map (fun i => φ (fiter F i y))) :
    x = y := by
  apply h x y
  intro i hi
  exact map_eq_pointwise (fun i => φ (fiter F i x)) (fun i => φ (fiter F i y)) (List.range (n + 1)) heq i
    (List.mem_range.mpr (by omega))

-- ============================================================
-- §7 债清偿区（第二窗：债1 cliff_n＋债5 JSymm 由 sorry → proved）
-- ============================================================

def writeSeq (cfg : CFG) : List (Key × Val) → CState → CState
  | [], C => C
  | (k, v) :: kvs, C => writeSeq cfg kvs (writeOp cfg k v C)

/-! ### 债1→proved｜cliff_n 通式（**勘正版陈述**）
    首窗陈述 `= min kvs.length CAP` 对**非空** C 不成立（反例：C 已有 1 册键·CAP=256·写 1 fresh 键
    → live=2 ≠ min(1,256)=1）——勘正为通式 `= min(n₀+n, CAP)`·空态起步特例恢复设计案「断崖 256/n」断言。
    债位本体（支撑集保持引理组 writeOp_keys 等）已随勘正一并清偿。 -/
theorem cliff_n (cfg : CFG) : ∀ (C : CState) (kvs : List (Key × Val)),
    C.D.length ≤ cfg.CAP → Nodup (C.D.map Prod.fst) → Nodup (kvs.map Prod.fst) →
    (∀ k ∈ kvs.map Prod.fst, ¬ k ∈ C.D.map Prod.fst) →
    (writeSeq cfg kvs C).D.length = min (C.D.length + kvs.length) cfg.CAP := by
  intro C kvs
  induction kvs generalizing C with
  | nil =>
    intro hC _ _ _
    show C.D.length = min (C.D.length + 0) cfg.CAP
    omega
  | cons kv kvs ih =>
    obtain ⟨k, v⟩ := kv
    intro hC hnd hdistinct hfresh0
    simp only [List.map_cons] at hdistinct hfresh0
    have hp := Nodup_cons_mp hdistinct
    have hdistinct1 : Nodup (kvs.map Prod.fst) := hp.2
    have hnk : ¬ k ∈ kvs.map Prod.fst := fun hk => hp.1 hk
    have hkf : ¬ k ∈ C.D.map Prod.fst := hfresh0 k (List.mem_cons_self _ _)
    have hstep := write_live_rec cfg k v C hC hnd hkf
    have hC1 := cap_invariant cfg k v C hC
    have hnd1 := writeOp_nodup cfg k v C hnd
    have hfresh1 : ∀ k' ∈ kvs.map Prod.fst, ¬ k' ∈ (writeOp cfg k v C).D.map Prod.fst := by
      intro k' hk' hmem
      rcases writeOp_keys cfg k v C k' hmem with he | hhold
      · rw [he] at hk'; exact absurd hk' hnk
      · exact hfresh0 k' (List.mem_cons_of_mem _ hk') hhold
    have ih1 := ih (writeOp cfg k v C) hC1 hnd1 hdistinct1 hfresh1
    show (writeSeq cfg kvs (writeOp cfg k v C)).D.length
      = min (C.D.length + (kvs.length + 1)) cfg.CAP
    rw [ih1]
    omega

-- 空态特例（设计案断崖 256/n 口径：reset 后 n 次互异 fresh 写 → live = min(n, CAP)）
theorem cliff_n_empty (cfg : CFG) (C₀ : CState) (kvs : List (Key × Val))
    (hdistinct : Nodup (kvs.map Prod.fst)) :
    (writeSeq cfg kvs (resetOp C₀)).D.length = min kvs.length cfg.CAP := by
  have h0 : (resetOp C₀).D.length = 0 := rfl
  have hnd : Nodup ((resetOp C₀).D.map Prod.fst) := Nodup_nil
  have hf : ∀ k ∈ kvs.map Prod.fst, ¬ k ∈ (resetOp C₀).D.map Prod.fst := by
    intro k _ hk
    simp [resetOp] at hk
  have h := cliff_n cfg (resetOp C₀) kvs (by omega) hnd hdistinct hf
  rw [h0] at h
  omega

/-! ### 债5→proved｜JSymm 保持（hebbW2 对称双条目版）
    v1 hebbW 单侧写 (k,j) 条目——结构性不对称；hebbW2 双条目 (k,j)/(j,k) 同增幅——
    JSymm J → JSymm (hebbW2 ...) 归纳证毕（jsymm_consPair 核心步：双条目值相等由 JSymm J 传入）。 -/

theorem jget_cons_eq (i j : Key) (v : Int) (J : JField) (a b : Key) :
    jget (((i, j), v) :: J) a b = if i = a ∧ j = b then v else jget J a b := by
  show (if (i, j) = (a, b) then v else jget J a b) = if i = a ∧ j = b then v else jget J a b
  by_cases h : (i, j) = (a, b)
  · rw [if_pos h, if_pos (by rw [Prod.mk.injEq] at h; exact h)]
  · rw [if_neg h, if_neg (fun hp => h (by rw [hp.1, hp.2]))]

theorem jget_hit1 (i j : Key) (v w : Int) (J : JField) :
    jget (((i, j), v) :: ((j, i), w) :: J) i j = v := by
  show (if (i, j) = (i, j) then v else jget (((j, i), w) :: J) i j) = v
  rw [if_pos rfl]

theorem jget_hit2 (i j : Key) (v w : Int) (J : JField) (hij : i ≠ j) :
    jget (((i, j), v) :: ((j, i), w) :: J) j i = w := by
  show (if (i, j) = (j, i) then v else jget (((j, i), w) :: J) j i) = w
  have hne : ¬((i, j) = (j, i)) := by
    intro hp
    rw [Prod.mk.injEq] at hp
    exact hij hp.1
  rw [if_neg hne]
  show (if (j, i) = (j, i) then w else jget J j i) = w
  rw [if_pos rfl]

theorem jget_miss (i j : Key) (v w : Int) (J : JField) (a b : Key)
    (h1 : ¬(i = a ∧ j = b)) (h2 : ¬(j = a ∧ i = b)) :
    jget (((i, j), v) :: ((j, i), w) :: J) a b = jget J a b := by
  show (if (i, j) = (a, b) then v else if (j, i) = (a, b) then w else jget J a b) = jget J a b
  rw [if_neg (fun hp => by rw [Prod.mk.injEq] at hp; exact h1 hp),
      if_neg (fun hp => by rw [Prod.mk.injEq] at hp; exact h2 hp)]

theorem jsymm_nil : JSymm ([] : JField) := by
  intro a b
  simp [jget]

-- 自环条目（i=i）：单条目即对称
theorem jsymm_consSelf (i : Key) (v : Int) (J : JField) (hJ : JSymm J) :
    JSymm (((i, i), v) :: J) := by
  intro a b
  by_cases h : i = a ∧ i = b
  · obtain ⟨rfl, rfl⟩ := h
    rfl
  · simp only [jget_cons_eq]
    have h' : ¬(i = b ∧ i = a) := fun hp => h ⟨hp.2, hp.1⟩
    rw [if_neg h, if_neg h']
    exact hJ a b

-- 互异双条目 ((i,j),v)::((j,i),w)：v=w 时对称保持
theorem jsymm_consPair (i j : Key) (v w : Int) (J : JField) (hJ : JSymm J) (hvw : v = w)
    (hij : i ≠ j) : JSymm (((i, j), v) :: ((j, i), w) :: J) := by
  intro a b
  by_cases h1 : i = a ∧ j = b
  · obtain ⟨rfl, rfl⟩ := h1
    rw [jget_hit1 i j v w J, jget_hit2 i j v w J hij]
    exact hvw
  · by_cases h2 : j = a ∧ i = b
    · obtain ⟨rfl, rfl⟩ := h2
      rw [jget_hit2 i j v w J hij, jget_hit1 i j v w J]
      exact hvw.symm
    · have h3 : ¬(i = b ∧ j = a) := fun hp => h2 ⟨hp.2, hp.1⟩
      have h4 : ¬(j = b ∧ i = a) := fun hp => h1 ⟨hp.2, hp.1⟩
      rw [jget_miss i j v w J a b h1 h2, jget_miss i j v w J b a h3 h4]
      exact hJ a b

theorem jsymm_hebbW2 (θc : ℕ) (ηw : Int) (k : Key) :
    ∀ (D : List (Key × (Val × Ver))) (J : JField), JSymm J → JSymm (hebbW2 θc ηw k D J) := by
  intro D
  induction D with
  | nil => intro J hJ; exact hJ
  | cons x xs ih =>
    intro J hJ
    simp only [hebbW2, List.foldl_cons]
    split
    · next hc =>
      refine ih _ (jsymm_consPair k x.1 _ _ J hJ (by rw [hJ k x.1]) (fun h => hc.1 h.symm))
    · exact ih J hJ

-- ============================================================
-- §8 SORRY-LEDGER（证明债台账·第三窗结算·sorry 集中登记·编译回执 17:37 全绿确认）
-- ============================================================
-- 【已清偿·二窗】债1 cliff_n 通式 → §7 cliff_n＋cliff_n_empty
--   （**勘正**：首窗陈述版对非空 C 不成立——通式 min(n₀+n, CAP) 证毕·空态特例恢复断崖 256/n 断言）
-- 【已清偿·二窗·三窗编译收尾】债5 JSymm 保持 → §7 hebbW2＋jsymm_hebbW2（对称双条目版·
--   v1 单侧写留为欠规格位① A/B 对照面）——簇 E jget 自建递归化后 jsymm 证明链通过编译器终态
-- 【在册】债2 d50_real_debt（§6 T4 区）：ℝ/Real.log 版 D50 通式——候 mathlib
--   （实测注记：Std.Data.Rat 亦不在 core 4.15·`import Std #check` 0 命中；Nat 夹逼锚 68/69 已机器证）
-- 【在册】债3 d2_prevalence_debt（下方）：D2 Embedology prevalence 版
--   （Sauer-Yorke-Casdagli 1991·prevalence 测度论位）——陈述级候令
-- 【在册】债4 d5_tc0_debt（下方）：D5 SSM≤TC⁰（Merrill-Petty-Sabharwal ICML 2024·置换复合状态追踪
--   TC⁰ 上限）——电路复杂度形式化位·陈述级候令（文献互证位 N5：Complexitylib 止步 De Morgan 门基·阈值类空白＝双侧互证）

-- 债3｜D2：「几乎每个时延映射为嵌入（分形吸引子亦然）」——prevalence 测度论位·陈述级候令
theorem d2_prevalence_debt : True := sorry

-- 债4｜D5：置换复合等状态追踪不可由 SSM 表达（TC⁰ 上限）——电路复杂度形式化位·陈述级候令
theorem d5_tc0_debt : True := sorry
