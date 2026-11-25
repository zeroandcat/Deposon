/-
DeposonThermo.lean — machine-checked conservation of the thermodynamic ledger core
(companion to `mcp/thermo_core.py`; phantom-limb generation, interface H).

Model (integer exergy over ℕ — no temperature, no potential function, axiom A5):
  a ledger state carries the injected exergy `e0` (rows + queries), the terminal
  accounts `phi` (transmitted) / `refl` (reflected) / `diss` (dissipated), and the
  in-presence pool `us` (remaining quanta of every row, in ledger order; a row
  deposited by the Python core is carried here as a `0` entry — T9 shows that
  deleting a `0` entry preserves the pool sum).

  First law  (attribution conservation):  e0 = phi + refl + diss + us.sum
  Second law (direction anchor):          `diss` never decreases — there is no
                                          `recover` transition in the signature
  Aether interface (erasure):             depositing a row moves ALL its remaining
                                          quanta into `diss` in one step (T5)

Machine-checked claims (lean 4.15.0 core-only, no mathlib, no `sorry`):

  T0  sum_set               — updating one pool entry: new sum + old = sum + paid
  T1  conserved_inject      — injecting a row of q quanta preserves conservation
  T2  conserved_dissipate   — a gate reject / decay of a ≤ u_i quanta preserves it
  T3  conserved_transmit    — paying c quanta of query exergy into phi preserves it
  T4  conserved_reflect     — paying c quanta of query exergy into refl preserves it
  T5  conserved_deposit     — depositing row i (all u_i → diss) preserves it
  T6  diss_monotone         — inject / dissipate / transmit / reflect / deposit
                              never decrease `diss` (no recover)
  T7  pool_monotone         — dissipate never increases the in-presence pool
  T8  settle_close          — hand-computed scenario (decay + horizon deposit)
                              equals the vector; conservation holds by `decide`
  T9  sum_drop_zero         — deleting a deposited (0) entry preserves the pool sum
-/

namespace DeposonThermo

/-- Ledger state: injected exergy, terminal accounts, in-presence pool. -/
structure State where
  e0 : Nat
  phi : Nat
  refl : Nat
  diss : Nat
  us : List Nat
  deriving Repr

/-- First law: E⁰ = Φ + R + D + U. -/
def Conserved (s : State) : Prop := s.e0 = s.phi + s.refl + s.diss + s.us.sum

/-- Inject a row of `q` quanta. -/
def inject (s : State) (q : Nat) : State :=
  { s with e0 := s.e0 + q, us := q :: s.us }

/-- Gate reject / decay: row `i` pays `a` quanta into the dissipation account
    (out-of-range index: no event — the Python core rejects it fail-loud). -/
def dissipate (s : State) (i a : Nat) : State :=
  { s with
    diss := s.diss + (if h : i < s.us.length then a else 0),
    us := if h : i < s.us.length then s.us.set i (s.us[i] - a) else s.us }

/-- Transmit: `c` quanta of query exergy flow into phi. -/
def transmit (s : State) (c : Nat) : State :=
  { s with e0 := s.e0 + c, phi := s.phi + c }

/-- Reflect (phantom readback): `c` quanta of query exergy flow into refl. -/
def reflect (s : State) (c : Nat) : State :=
  { s with e0 := s.e0 + c, refl := s.refl + c }

/-- Deposit row `i`: all its remaining quanta dissipate (aether interface). -/
def deposit (s : State) (i : Nat) : State :=
  { s with
    diss := s.diss + (if h : i < s.us.length then s.us[i] else 0),
    us := if h : i < s.us.length then s.us.set i 0 else s.us }

theorem sum_set (l : List Nat) (i a : Nat) (h : i < l.length) :
    (l.set i a).sum + l[i] = l.sum + a := by
  induction l generalizing i with
  | nil => simp at h
  | cons x xs ih =>
    cases i with
    | zero => simp only [List.set_cons_zero, List.sum_cons, List.getElem_cons_zero]; omega
    | succ i =>
      have h' : i < xs.length := Nat.lt_of_succ_lt_succ h
      have hs := ih i h'
      simp only [List.set_cons_succ, List.sum_cons, List.getElem_cons_succ]
      omega

theorem conserved_inject {s : State} (h : Conserved s) (q : Nat) :
    Conserved (inject s q) := by
  unfold Conserved at h ⊢
  simp only [inject, List.sum_cons]
  omega

theorem conserved_dissipate {s : State} (h : Conserved s) {i a : Nat}
    (hl : i < s.us.length) (ha : a ≤ s.us[i]) :
    Conserved (dissipate s i a) := by
  unfold Conserved at h ⊢
  have hs := sum_set s.us i (s.us[i] - a) hl
  simp only [dissipate, dif_pos hl]
  omega

theorem conserved_transmit {s : State} (h : Conserved s) (c : Nat) :
    Conserved (transmit s c) := by
  unfold Conserved at h ⊢
  simp only [transmit]; omega

theorem conserved_reflect {s : State} (h : Conserved s) (c : Nat) :
    Conserved (reflect s c) := by
  unfold Conserved at h ⊢
  simp only [reflect]; omega

theorem conserved_deposit {s : State} (h : Conserved s) {i : Nat}
    (hl : i < s.us.length) :
    Conserved (deposit s i) := by
  unfold Conserved at h ⊢
  have hs := sum_set s.us i 0 hl
  simp only [deposit, dif_pos hl]
  omega

theorem diss_monotone_inject (s : State) (q : Nat) : (inject s q).diss ≥ s.diss := Nat.le_refl _
theorem diss_monotone_dissipate (s : State) (i a : Nat) : (dissipate s i a).diss ≥ s.diss := by
  unfold dissipate
  split <;> simp_all
theorem diss_monotone_transmit (s : State) (c : Nat) : (transmit s c).diss ≥ s.diss := Nat.le_refl _
theorem diss_monotone_reflect (s : State) (c : Nat) : (reflect s c).diss ≥ s.diss := Nat.le_refl _
theorem diss_monotone_deposit (s : State) (i : Nat) : (deposit s i).diss ≥ s.diss := by
  unfold deposit
  split <;> simp_all

theorem pool_monotone {s : State} {i a : Nat} (hl : i < s.us.length) (ha : a ≤ s.us[i]) :
    (dissipate s i a).us.sum ≤ s.us.sum := by
  have hs := sum_set s.us i (s.us[i] - a) hl
  simp only [dissipate, dif_pos hl]
  omega

/-- Hand-computed settlement vector (mirrored in Python by `mcp/thermo_crosscheck.py`
    through the real event Reducer, so both implementations agree on every digit):
    inject `a` then `b` with 100 quanta each (the pool prepends: index 0 = `b`, 1 = `a`);
    one transmit of 10; `b` pays 30 + 10 + 10 = 50 (50 quanta stay in presence),
    `a` pays 20 + 10 = 30 and deposits its remaining 70;
    diss = 30 + 20 + 10 + 10 + 10 + 70 = 150, e0 = 100 + 100 + 10 = 210,
    210 = phi 10 + refl 0 + diss 150 + sum [50, 0]. -/
def s0 : State := ⟨0, 0, 0, 0, []⟩

def run : State :=
  deposit
    (dissipate (dissipate (dissipate (dissipate (dissipate
      (transmit (inject (inject s0 100) 100) 10)
      0 30) 1 20) 0 10) 1 10) 0 10)
    1

theorem settle_close :
    run.e0 = 210 ∧ run.phi = 10 ∧ run.refl = 0 ∧ run.diss = 150 ∧ run.us = [50, 0] := by
  decide

theorem settle_conserved : Conserved run := by
  unfold Conserved
  decide

theorem sum_drop_zero : ∀ (l₁ l₂ : List Nat), (l₁ ++ 0 :: l₂).sum = (l₁ ++ l₂).sum
  | [], l₂ => by simp only [List.nil_append, List.sum_cons, List.sum_nil, Nat.zero_add]
  | x :: xs, l₂ => by simp only [List.cons_append, List.sum_cons, sum_drop_zero xs l₂]

-- Axiom audit: one `#print axioms` per theorem (15/15). Acceptable set = Lean's own
-- `propext` / `Quot.sound` (no `sorryAx`, no `Classical.choice`); `decide` data theorems
-- are axiom-free. CI greps the build log for `sorryAx`.
#print axioms sum_set
#print axioms conserved_inject
#print axioms conserved_dissipate
#print axioms conserved_transmit
#print axioms conserved_reflect
#print axioms conserved_deposit
#print axioms diss_monotone_inject
#print axioms diss_monotone_dissipate
#print axioms diss_monotone_transmit
#print axioms diss_monotone_reflect
#print axioms diss_monotone_deposit
#print axioms pool_monotone
#print axioms settle_close
#print axioms settle_conserved
#print axioms sum_drop_zero

end DeposonThermo
